::: {#672488214 .myid}
[]{#struct_0_48648_47840_1296181450}[]{#_Toc404794646}

**SRST \-- SRST配置命令 \-- authenticate realm**

------------------------------------------------------------------------

[**[authenticate realm]{lang="EN-US"}**]{#struct_0_48648_47840_1991828472}[命令用来配置语音服务器发送]{style="font-family:宋体"}[401]{lang="EN-US"}[应答中携带的域名信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_48648_47840_x1029000494}**[authenticate realm]{lang="EN-US"}**[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x356101651}

[**[authenticate realm ]{lang="EN-US"}**]{#struct_0_48648_47840_x937132696}*[string]{lang="EN-US"}*

[**[undo ]{lang="EN-US"}**]{#struct_0_48648_47840_x1923495105}**[authenticate realm]{lang="EN-US"}**[ ]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_665743324}

[[语音服务器发送]{style="font-family:宋体"}[401]{lang="EN-US"}]{#struct_0_48648_47840_1377282258}[应答中不携带域名信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1910054530}

[[全局注册视图]{style="font-family:宋体"}]{#struct_0_48648_47840_644274066}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1504631480}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1381094253}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_831474145}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1017140725}

[*[string]{lang="EN-US"}*]{#struct_0_48648_47840_x1252713358}[：]{style="font-family:黑体"}[语音服务器发送]{style="font-family:宋体"}[401]{lang="EN-US"}[应答中携带的域名信息，用于语音服务器和]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[之间的握手验证，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[50]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x356101652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备作为语音服务器时，可以通过发送域名信息使]{style="font-family:宋体"}]{#struct_0_48648_47840_x937067160}[SIP UA]{lang="EN-US"}[来选择鉴权信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备作为语音服务器工作在本地存活模式时，该命令不生效。]{style="font-family:宋体"}]{#struct_0_48648_47840_409502684}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x36688676}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_1717034344}[配置语音服务器发送]{style="font-family:宋体"}[401]{lang="EN-US"}[应答中携带的域名信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_1302058900}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\] authenticate realm server1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_537643202}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authenticate register]{lang="EN-US"}**]{#struct_0_48648_47840_1515523519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode]{lang="EN-US"}**]{#struct_0_48648_47840_415999663}
:::

::: {#1506388166 .myid}
[]{#_Toc404794647}[]{#struct_0_48648_47840_x1723837660}

**SRST \-- SRST配置命令 \-- authenticate register**

------------------------------------------------------------------------

[**[authenticate register]{lang="EN-US"}**]{#struct_0_48648_47840_x356101653}[命令用来开启全局注册鉴权。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **authenticate register**]{lang="EN-US"}]{#struct_0_48648_47840_x937001624}[命令用来关闭全局注册鉴权。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1526436586}

[**[authenticate register]{lang="EN-US"}**]{#struct_0_48648_47840_x1462102004}

[**[undo authenticate register]{lang="EN-US"}**]{#struct_0_48648_47840_x608763292}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1624341744}

[[全局注册鉴权处于关闭状态。]{style="font-family:宋体"}]{#struct_0_48648_47840_443394209}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1884166148}

[[全局注册视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1444710488}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x97893523}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_818307252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_104376259}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_1483758136}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启该命令后，设备作为语音服务器在接受]{style="font-family:宋体"}]{#struct_0_48648_47840_x356101646}[SIP UA]{lang="EN-US"}[注册时，如果需要对]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[进行鉴权。]{style="font-family:宋体"}[鉴权信息可以通过注册池视图下的]{lang="EN-US" style="font-family:宋体"}**[username]{lang="EN-US"}**[命令配置，域名信息可以通过]{lang="EN-US" style="font-family:宋体"}**[authenticate realm]{lang="EN-US"}**[命令配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接受]{style="font-family:宋体"}]{#struct_0_48648_47840_x936805017}[SIP UA]{lang="EN-US"}[注册时，工作在本地存活模式的语音服务器不会对用户信息进行鉴权，因此在该模式的语音服务器上开启全局的注册鉴权不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_805870607}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1896250642}[开启全局注册鉴权。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x455892464}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\] authenticate register]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_810748373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode]{lang="EN-US"}**]{#struct_0_48648_47840_x1107900301}
:::

::: {#-2043589798 .myid}
[]{#_Toc404794648}[]{#struct_0_48648_47840_x1889657873}[]{#_Toc370738265}[]{#_Toc205711285}[]{#_Toc176074718}

**SRST \-- SRST配置命令 \-- caller-group**

------------------------------------------------------------------------

[**[caller-group]{lang="EN-US"}**]{#struct_0_48648_47840_x1462888748}[命令用来将指定的用户组绑定到注册池。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **caller-group**]{lang="EN-US"}]{#struct_0_48648_47840_1895550657}[命令用来取消已有的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1977964551}

[**[caller-group]{lang="EN-US"}**[ { **deny** \| **permit** } *group-id*]{lang="EN-US"}]{#struct_0_48648_47840_1002571345}

[**[undo]{lang="EN-US"}**[ **caller-group** { { **deny** \| **permit** } *group-id* \| **all** }]{lang="EN-US"}]{#struct_0_48648_47840_862033886}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x356101647}

[[用户组和注册池没有绑定关系。]{style="font-family:宋体"}]{#struct_0_48648_47840_x936739481}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x36498693}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x1227104950}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x331567755}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1405385560}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_1710667229}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1847625349}

[**[deny]{lang="EN-US"}**]{#struct_0_48648_47840_x698944520}[：拒绝用户组中的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_48648_47840_x395773705}[：允许用户组中的主叫号码呼出]{style="font-family:宋体"}[/]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[*[group-id]{lang="EN-US"}*]{#struct_0_48648_47840_x805386121}[：绑定用户组]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_48648_47840_110942777}[：绑定的所有用户组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_833376746}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以将一个不存在的用户组绑定到注册池，但只有完成用户组的设置后，该用户组才能生效。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1950363446}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在注册池下只能绑定一个用户组，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1254698559}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1066085719}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x655713582}[将用户组绑定到注册池]{style="font-family:宋体"}[100]{lang="EN-US"}[，允许用户组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的主叫号码呼出。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x87649054}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] caller-group permit 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_41288323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[subscriber-group]{lang="EN-US"}**]{#struct_0_48648_47840_x1010955090}[（语音命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[拨号策略）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#795477320 .myid}
[]{#_Toc404794649}[]{#struct_0_48648_47840_x1783239594}

**SRST \-- SRST配置命令 \-- codec**

------------------------------------------------------------------------

[**[codec]{lang="EN-US"}**]{#struct_0_48648_47840_x1102013}[命令用来配置语音编解码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **codec**]{lang="EN-US"}]{#struct_0_48648_47840_x422871229}[命令用来删除配置的语音编解码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_833376745}

[]{#struct_0_48648_47840_x1950363445}[]{#_Hlt20797640}**[codec]{lang="EN-US"}**[ { **g711alaw** \| **g711ulaw** \| **g723r53** \| **g723r63** \| **g726r16** \| **g726r24** \| **g726r32** \| **g726r40** \| **g729a** \| **g729br8** \| **g729r8** } \[ **bytes** *payload-size* \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **codec** ]{lang="EN-US"}]{#struct_0_48648_47840_x851414032}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x845799394}

[[没有配置语音编解码。]{style="font-family:宋体"}]{#struct_0_48648_47840_1857104621}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1196010876}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_633199879}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1479697140}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1470165965}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x644046342}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_833376744}

[**[g711alaw]{lang="EN-US"}**]{#struct_0_48648_47840_x1950363444}[：表示]{style="font-family:宋体"}[G.711]{lang="EN-US"}[的]{style="font-family:宋体"}[A]{lang="EN-US"}[律编解码方式，带宽为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，通常被欧洲采用。]{style="font-family:宋体"}

[**[g711ulaw]{lang="EN-US"}**]{#struct_0_48648_47840_1877469323}[：表示]{style="font-family:宋体"}[G.711]{lang="EN-US"}[的]{style="font-family:宋体"}[m]{lang="EN-US" style="font-family:Symbol"}[律编解码方式，带宽为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[，通常被北美和日本等国家采用。]{style="font-family:宋体"}

[**[g723r53]{lang="EN-US"}**]{#struct_0_48648_47840_472390418}[：表示]{style="font-family:宋体"}[G.723.1 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[5.3kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g723r63]{lang="EN-US"}**]{#struct_0_48648_47840_x786412769}[：表示]{style="font-family:宋体"}[G.723.1 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[6.3kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g726r16]{lang="EN-US"}**]{#struct_0_48648_47840_196107193}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[16kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r24]{lang="EN-US"}**]{#struct_0_48648_47840_x1465202584}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[24kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r32]{lang="EN-US"}**]{#struct_0_48648_47840_x598605076}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[32kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g726r40]{lang="EN-US"}**]{#struct_0_48648_47840_x479755206}[：表示]{style="font-family:宋体"}[G.726 Annex A]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[40kbps]{lang="EN-US"}[。本参数的支持情况与实际使用的板卡有关。]{style="font-family:宋体"}

[**[g729a]{lang="EN-US"}**]{#struct_0_48648_47840_1797021811}[：表示]{style="font-family:宋体"}[G.729 Annex A]{lang="EN-US"}[编解码方式，对]{style="font-family:宋体"}[G.729]{lang="EN-US"}[编解码进行了一系列简化，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g729br8]{lang="EN-US"}**]{#struct_0_48648_47840_x1236671470}[：表示]{style="font-family:宋体"}[G.729 Annex B]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g729r8]{lang="EN-US"}**]{#struct_0_48648_47840_x1932473260}[：表示]{style="font-family:宋体"}[G.729]{lang="EN-US"}[编解码方式，带宽为]{style="font-family:宋体"}[8kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bytes]{lang="EN-US"}**[ *payload-size*]{lang="EN-US"}]{#struct_0_48648_47840_115672685}[：每秒发送的编码字节数，取值范围和选择的编解码方式有关，单位为字节：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g711alaw]{lang="EN-US"}**]{#struct_0_48648_47840_833376743}[和]{lang="EN-US" style="font-family:宋体"}**[g711ulaw]{lang="EN-US"}**[的取值范围为]{lang="EN-US" style="font-family:宋体"}[80]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[240]{lang="EN-US"}[（取值为]{lang="EN-US" style="font-family:宋体"}[80]{lang="EN-US"}[的倍数）；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g723r53]{lang="EN-US"}**]{#struct_0_48648_47840_x1950363443}[的取值范围为]{style="font-family:
宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g723r63]{lang="EN-US"}**]{#struct_0_48648_47840_x2014213446}[的取值范围为]{style="font-family:
宋体"}[24]{lang="EN-US"}[～]{style="font-family:宋体"}[144]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[24]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r16]{lang="EN-US"}**]{#struct_0_48648_47840_x1120530000}[的取值范围为]{style="font-family:
宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[220]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[20]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r24]{lang="EN-US"}**]{#struct_0_48648_47840_x1089751783}[的取值范围为]{style="font-family:
宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[210]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[30]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r32]{lang="EN-US"}**]{#struct_0_48648_47840_x2107606785}[的取值范围为]{style="font-family:
宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[40]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g726r40]{lang="EN-US"}**]{#struct_0_48648_47840_969951615}[的取值范围为]{style="font-family:
宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[50]{lang="EN-US"}[的倍数）；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[g729a]{lang="EN-US"}**]{#struct_0_48648_47840_x401842334}[、]{style="font-family:
宋体"}**[g729br8]{lang="EN-US"}**[和]{style="font-family:
宋体"}**[729r8]{lang="EN-US"}**[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[（取值为]{style="font-family:宋体"}[10]{lang="EN-US"}[的倍数）。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}**[g711]{lang="EN-US"}**]{#struct_0_48648_47840_1137838257}[为]{style="font-family:宋体"}[160]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g723r63]{lang="EN-US"}**[为]{style="font-family:宋体"}[24]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g723r53]{lang="EN-US"}**[为]{style="font-family:宋体"}[20]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r16]{lang="EN-US"}**[为]{style="font-family:宋体"}[60]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r24]{lang="EN-US"}**[为]{style="font-family:宋体"}[90]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r32]{lang="EN-US"}**[为]{style="font-family:宋体"}[120]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g726r40]{lang="EN-US"}**[为]{style="font-family:宋体"}[150]{lang="EN-US"}[字节，]{style="font-family:宋体"}**[g729]{lang="EN-US"}**[为]{style="font-family:宋体"}[30]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_1825683694}

[**[g711alaw]{lang="EN-US"}**]{#struct_0_48648_47840_1306378414}[和]{style="font-family:宋体"}**[g711ulaw]{lang="EN-US"}**[编解码可以提供高质量的语音传输，但要占用较高的带宽。]{style="font-family:宋体"}

[**[g723r53]{lang="EN-US"}**]{#struct_0_48648_47840_833376750}[和]{style="font-family:宋体"}**[g723r63]{lang="EN-US"}**[编解码提供了静音压缩技术和舒适噪音，较高速率的输出基于多脉冲多量级技术并提供某种程度上较高质量的音质，较低速率的输出基于码激励线性预测技术并为应用提供了更大的灵活性。]{style="font-family:宋体"}

[**[g729r8]{lang="EN-US"}**]{#struct_0_48648_47840_5951696}[和]{style="font-family:宋体"}**[g729a]{lang="EN-US"}**[编解码提供的话音质量与]{style="font-family:宋体"}[32kbps]{lang="EN-US"}[的]{style="font-family:宋体"}[ADPCM]{lang="EN-US"}[（]{style="font-family:宋体"}[Adaptive Differential Pulse Code Modulation]{lang="EN-US"}[，自适应差分脉冲编码调制）相似，具有长话的质量，同时具有低带宽、较小时间延迟和适中处理复杂度，因此应用广泛。]{style="font-family:宋体"}

[[为了更清晰地了解各种语音编解码算法对语音带宽、话音质量等的影响，]{style="font-family:宋体"}]{#struct_0_48648_47840_155015476}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-1]{lang="EN-US"}](?795477320#_Ref148446106)[介绍相关算法和带宽的关系。]{style="font-family:
宋体"}

[]{#struct_0_48648_47840_x1432006005}[]{#_Ref148446106}[]{#_Toc121809742}[[表1-1 ]{lang="EN-US"}[编解码方式和带宽的关系]{style="font-family:黑体"}]{#_Toc112125376}

[]{#table_struct_0_476873802}[[语音编解码]{style="font-family:黑体"}]{#struct_0_48648_47840_2138577198}
:::

[[带宽]{style="font-family:黑体"}]{#struct_0_48648_47840_104639203}

[[语音质量]{style="font-family:黑体"}]{#struct_0_48648_47840_x1487840570}

[[G.711]{lang="EN-US"}]{#struct_0_48648_47840_2010225715}[（]{style="font-family:宋体"}[A]{lang="EN-US"}[律、]{style="font-family:宋体"}[m]{lang="EN-US" style="font-family:Symbol"}[律）]{style="font-family:宋体"}

[[64Kbps]{lang="EN-US"}]{#struct_0_48648_47840_1542739508}[（没有压缩）]{style="font-family:宋体"}

[[语音质量最好]{style="font-family:宋体"}]{#struct_0_48648_47840_x974955289}

[[G.726]{lang="EN-US"}]{#struct_0_48648_47840_833376749}

[[16]{lang="EN-US"}]{#struct_0_48648_47840_x1950363449}[、]{style="font-family:宋体"}[24]{lang="EN-US"}[、]{style="font-family:宋体"}[32]{lang="EN-US"}[、]{style="font-family:宋体"}[40 Kbps]{lang="EN-US"}

[[语音质量较好]{style="font-family:宋体"}]{#struct_0_48648_47840_1474184796}

[[G.729]{lang="EN-US"}]{#struct_0_48648_47840_889259853}

[[8Kbps]{lang="EN-US"}]{#struct_0_48648_47840_1021365530}

[[语音质量较好]{style="font-family:宋体"}]{#struct_0_48648_47840_1538184757}

[[G.723 r63]{lang="EN-US"}]{#struct_0_48648_47840_224477842}

[[6.3Kbps]{lang="EN-US"}]{#struct_0_48648_47840_398318608}

[[语音质量一般]{style="font-family:宋体"}]{#struct_0_48648_47840_833376748}

[[G.723 r53]{lang="EN-US"}]{#struct_0_48648_47840_x1950363448}

[[5.3Kbps]{lang="EN-US"}]{#struct_0_48648_47840_x91899145}

[[语音质量一般]{style="font-family:宋体"}]{#struct_0_48648_47840_x1029677468}

[ ]{lang="EN-US"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_48648_47840_830607857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当通讯双方拥有的语音编解码存在交集时，双方才能正常建立呼叫。]{style="font-family:宋体"}]{#struct_0_48648_47840_x931012018}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1583756572}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_2065905869}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x843281149}[配置语音编解码为]{style="font-family:宋体"}[g711alaw]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_844072259}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] codec g711alaw]{lang="EN-US"}

::: {#71194559 .myid}
[]{#_Toc31535694}[]{#_Toc94588337}[]{#_Toc80176759}[]{#_Toc404794650}[]{#struct_0_48648_47840_x991857635}[]{#_Toc135538258}[]{#_Toc135538259}[]{#_Toc135538261}[]{#_Toc135538262}[]{#_Toc135538263}[]{#_Toc135538264}[]{#_Toc135538265}[]{#_Toc135538266}[]{#_Toc135538267}[]{#_Toc135538268}[]{#_Toc135538269}[]{#_Toc135538270}[]{#_Toc135538271}[]{#_Toc135538272}[]{#_Toc135538273}[]{#_Toc135538274}[]{#_Toc135538275}[]{#_Toc135538276}[]{#_Toc135538277}[]{#_Toc135538278}[]{#_Toc135538279}[]{#_Toc135538280}[]{#_Toc135538282}[]{#_Toc135538283}[]{#_Toc135538286}[]{#_Toc135538287}[]{#_Toc135538288}[]{#_Toc135538289}[]{#_Toc135538290}[]{#_Toc135538291}[]{#_Toc135538292}[]{#_Toc135538293}[]{#_Toc135538294}[]{#_Toc135538295}[]{#_Toc135538296}[]{#_Toc135538297}[]{#_Toc135538298}[]{#_Toc60064281}[]{#_Toc60649243}[]{#_Toc76002874}[]{#_Toc76444799}[]{#_Toc60064283}[]{#_Toc60649245}[]{#_Toc76002876}[]{#_Toc76444801}[]{#_Toc60064284}[]{#_Toc60649246}[]{#_Toc76002877}[]{#_Toc76444802}[]{#_Toc60064285}[]{#_Toc60649247}[]{#_Toc76002878}[]{#_Toc76444803}[]{#_Toc60064286}[]{#_Toc60649248}[]{#_Toc76002879}[]{#_Toc76444804}[]{#_Toc60064287}[]{#_Toc60649249}[]{#_Toc76002880}[]{#_Toc76444805}[]{#_Toc60064288}[]{#_Toc60649250}[]{#_Toc76002881}[]{#_Toc76444806}[]{#_Toc60064289}[]{#_Toc60649251}[]{#_Toc76002882}[]{#_Toc76444807}[]{#_Toc60064290}[]{#_Toc60649252}[]{#_Toc76002883}[]{#_Toc76444808}[]{#_Toc60064291}[]{#_Toc60649253}[]{#_Toc76002884}[]{#_Toc76444809}[]{#_Toc60064292}[]{#_Toc60649254}[]{#_Toc76002885}[]{#_Toc76444810}[]{#_Toc35952971}[]{#_Toc35953374}[]{#_Toc35954258}[]{#_Toc35955135}[]{#_Toc60064295}[]{#_Toc60649257}[]{#_Toc76002888}[]{#_Toc76444813}[]{#_Toc60064296}[]{#_Toc60649258}[]{#_Toc76002889}[]{#_Toc76444814}[]{#_Toc60064297}[]{#_Toc60649259}[]{#_Toc76002890}[]{#_Toc76444815}[]{#_Toc60064298}[]{#_Toc60649260}[]{#_Toc76002891}[]{#_Toc76444816}[]{#_Toc60064299}[]{#_Toc60649261}[]{#_Toc76002892}[]{#_Toc76444817}[]{#_Toc60064300}[]{#_Toc60649262}[]{#_Toc76002893}[]{#_Toc76444818}[]{#_Toc60064301}[]{#_Toc60649263}[]{#_Toc76002894}[]{#_Toc76444819}[]{#_Toc60064302}[]{#_Toc60649264}[]{#_Toc76002895}[]{#_Toc76444820}[]{#_Toc60064303}[]{#_Toc60649265}[]{#_Toc76002896}[]{#_Toc76444821}[]{#_Toc60064304}[]{#_Toc60649266}[]{#_Toc76002897}[]{#_Toc76444822}[]{#_Toc60064305}[]{#_Toc60649267}[]{#_Toc76002898}[]{#_Toc76444823}[]{#_Toc60064306}[]{#_Toc60649268}[]{#_Toc76002899}[]{#_Toc76444824}[]{#_Toc60064307}[]{#_Toc60649269}[]{#_Toc76002900}[]{#_Toc76444825}[]{#_Toc60064309}[]{#_Toc60649271}[]{#_Toc76002902}[]{#_Toc76444827}[]{#_Toc60064312}[]{#_Toc60649274}[]{#_Toc76002905}[]{#_Toc76444830}[]{#_Toc60064313}[]{#_Toc60649275}[]{#_Toc76002906}[]{#_Toc76444831}[]{#_Toc60064314}[]{#_Toc60649276}[]{#_Toc76002907}[]{#_Toc76444832}[]{#_Toc60064315}[]{#_Toc60649277}[]{#_Toc76002908}[]{#_Toc76444833}[]{#_Toc60064316}[]{#_Toc60649278}[]{#_Toc76002909}[]{#_Toc76444834}[]{#_Toc60064317}[]{#_Toc60649279}[]{#_Toc76002910}[]{#_Toc76444835}[]{#_Toc60064318}[]{#_Toc60649280}[]{#_Toc76002911}[]{#_Toc76444836}[]{#_Toc60064319}[]{#_Toc60649281}[]{#_Toc76002912}[]{#_Toc76444837}[]{#_Toc60064320}[]{#_Toc60649282}[]{#_Toc76002913}[]{#_Toc76444838}[]{#_Toc60064321}[]{#_Toc60649283}[]{#_Toc76002914}[]{#_Toc76444839}[]{#_Toc239838245}[]{#_Toc239838246}[]{#_Toc239838247}[]{#_Toc239838248}[]{#_Toc239838249}[]{#_Toc239838250}[]{#_Toc239838251}[]{#_Toc239838252}[]{#_Toc239838253}[]{#_Toc239838254}[]{#_Toc239838255}[]{#_Toc239838256}[]{#_Toc239838257}[]{#_Toc239838258}[]{#_Toc239838259}[]{#_Toc239838261}[]{#_Toc239838263}[]{#_Toc239838264}[]{#_Toc239838265}[]{#_Toc239838266}[]{#_Toc239838267}[]{#_Toc239838268}[]{#_Toc239838269}[]{#_Toc239838270}[]{#_Toc239838271}[]{#_Toc239838272}[]{#_Toc239838273}[]{#_Toc239838274}[]{#_Toc239838275}[]{#_Toc239838276}[]{#_Toc239838277}[]{#_Toc239838278}[]{#_Toc239838279}[]{#_Toc239838280}[]{#_Toc239838281}[]{#_Toc239838282}[]{#_Toc239838283}[]{#_Toc239838284}[]{#_Toc239838290}[]{#_Toc239838291}[]{#_Toc239838292}[]{#_Toc239838293}[]{#_Toc239838317}[]{#_Toc239838319}[]{#_Toc239838320}[]{#_Toc239838321}[]{#_Toc239838322}[]{#_Toc239838323}[]{#_Toc239838324}[]{#_Toc239838325}[]{#_Toc239838326}[]{#_Toc239838327}[]{#_Toc239838328}[]{#_Toc239838329}[]{#_Toc239838330}[]{#_Toc239838331}[]{#_Toc239838332}[]{#_Toc239838333}[]{#_Toc239838334}[]{#_Toc239838335}[]{#_Toc239838336}[]{#_Toc239838337}[]{#_Toc239838338}[]{#_Toc239838339}[]{#_Toc239838341}[]{#_Toc239838342}[]{#_Toc239838343}[]{#_Toc239838356}

**SRST \-- SRST配置命令 \-- display voice register entity**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **voice register entity**]{lang="EN-US"}]{#struct_0_48648_47840_x1865835707}[命令用来显示注册池产生的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_833376747}

[**[display]{lang="EN-US"}**[ **voice** **register entity** { **all** \| **pool** *tag* }]{lang="EN-US"}]{#struct_0_48648_47840_x1950363447}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_311385382}

[[任意视图]{style="font-family:宋体"}]{#struct_0_48648_47840_460496232}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_365241449}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1237142175}

[[network-operator]{lang="EN-US"}]{#struct_0_48648_47840_735968821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1550078148}

[[mdc-operator]{lang="EN-US"}]{#struct_0_48648_47840_x1752904693}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1280197666}

[**[pool]{lang="EN-US"}***[ tag]{lang="EN-US"}*]{#struct_0_48648_47840_x2094120136}[：]{style="font-family:黑体"}[注册池索引，取值范围为]{style="font-family:宋体;color:black"}[0]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体"}[200]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_48648_47840_233797586}[：表示]{style="font-family:宋体"}[所有注册池产生的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_833376754}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_5951692}[显示注册池]{style="font-family:宋体"}[2]{lang="EN-US"}[产生的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice register entity pool 2]{lang="EN-US"}]{#struct_0_48648_47840_x1814352992}

[Entities created dynamically on register pool 2:]{lang="EN-US"}

[ ]{lang="EN-US"}

[entity 40003 voip]{lang="EN-US"}

[ match-template 2000\$]{lang="EN-US"}

[ address sip ip 192.168.4.101 port 10003]{lang="EN-US"}

[ session transport udp]{lang="EN-US"}

[ priority 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[entity 40004 voip]{lang="EN-US"}

[ match-template 2000\$]{lang="EN-US"}

[ address sip ip 10.1.1.2 port 5060 : VoIP entity available]{lang="EN-US"}

[ session transport global]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display voice register entity]{lang="EN-US"}]{#struct_0_48648_47840_1993407271}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x630037395}[[字段]{style="font-family:黑体"}]{#struct_0_48648_47840_x1593127743}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_48648_47840_427323330}

[[entity 40003 voip]{lang="EN-US"}]{#struct_0_48648_47840_831821025}

[[动态创建的]{style="font-family:宋体"}[VoIP]{lang="EN-US"}]{#struct_0_48648_47840_1419779821}[语音实体。]{style="font-family:宋体"}[在独立模式或本地存活模式语音服务器上生成的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体从]{style="font-family:宋体"}[40001]{lang="EN-US"}[开始编号，如果存在从]{style="font-family:宋体"}[40001]{lang="EN-US"}[开始的手工配置的]{style="font-family:宋体"}[POTS]{lang="EN-US"}[或]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体，独立模式和本地存活模式语音服务器会跳过该编号后，继续编号]{style="font-family:宋体"}

[[match-template]{lang="EN-US"}]{#struct_0_48648_47840_x1138760611}

[[匹配语音实体号码模板]{style="font-family:宋体"}]{#struct_0_48648_47840_x1809830847}

[[address sip]{lang="EN-US"}]{#struct_0_48648_47840_1124104786}

[[SIP]{lang="EN-US"}]{#struct_0_48648_47840_1590122744}[呼叫路由]{style="font-family:宋体"}

[[ip]{lang="EN-US"}]{#struct_0_48648_47840_x1444057253}

[[呼叫目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_48648_47840_x1197844939}[地址]{style="font-family:宋体"}

[[port]{lang="EN-US"}]{#struct_0_48648_47840_x688421917}

[[目的端口号]{style="font-family:宋体"}]{#struct_0_48648_47840_992786821}

[[session transport]{lang="EN-US"}]{#struct_0_48648_47840_1017968455}

[[发起]{style="font-family:宋体"}]{#struct_0_48648_47840_2040461438}[SIP]{lang="SV"}[呼叫时使用的传输协议类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[tcp]{lang="EN-US"}]{#struct_0_48648_47840_841657463}[：发起呼叫时，使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[传输协议]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[tls]{lang="EN-US"}]{#struct_0_48648_47840_457371862}[：发起呼叫时，使用]{style="font-family:宋体"}[TLS]{lang="EN-US"}[传输协议]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[udp]{lang="EN-US"}]{#struct_0_48648_47840_x332257093}[：发起呼叫时，使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[传输协议]{style="font-family:宋体"}

[[priority]{lang="EN-US"}]{#struct_0_48648_47840_796820503}

[[指向]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}]{#struct_0_48648_47840_1057325324}[的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的优先级]{style="font-family:宋体"}

[[VoIP entity]{lang="EN-US"}]{#struct_0_48648_47840_x1898341034}

[[独立模式语音服务器可用状态，取值包括：]{style="font-family:宋体"}]{#struct_0_48648_47840_1856142519}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_48648_47840_x868926531}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unavailable]{lang="EN-US"}]{#struct_0_48648_47840_830542321}

[ ]{lang="EN-US"}

::: {#-2055414451 .myid}
[]{#_Toc404794651}[]{#struct_0_48648_47840_267362771}

**SRST \-- SRST配置命令 \-- display voice register pool all brief**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **voice** **register pool all brief**]{lang="EN-US"}]{#struct_0_48648_47840_x660508723}[命令用来显示注册池中]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x985170866}

[**[display voice sip register pool all brief]{lang="EN-US"}**]{#struct_0_48648_47840_2084062305}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x970423877}

[[任意视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1400993567}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_833376753}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_5951693}

[[network-operator]{lang="EN-US"}]{#struct_0_48648_47840_x248269051}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1065670118}

[[mdc-operator]{lang="EN-US"}]{#struct_0_48648_47840_859221225}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1995470524}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_439104651}[显示注册池信息中]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice register pool all brief]{lang="EN-US"}]{#struct_0_48648_47840_1809198305}

[Pool ID              IP Address       Ln DN  Number        State]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[1    192.168.4.100   192.168.4.100    1  1   1000\$         Registered]{lang="EN-US"}

[                                      2      2000          Unregistered]{lang="EN-US"}

[2    192.168.4.101   192.168.4.101    1      2000\$         Registered]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display voice register pool all brief]{lang="EN-US"}]{#struct_0_48648_47840_558811299}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_472549742}[[字段]{style="font-family:黑体"}]{#struct_0_48648_47840_x1122938390}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_48648_47840_x26823336}

[[Pool ]{lang="EN-US"}]{#struct_0_48648_47840_1422622317}

[[注册池索引]{style="font-family:宋体"}]{#struct_0_48648_47840_x1261167405}

[[ID ]{lang="EN-US"}]{#struct_0_48648_47840_2103554966}

[[注册池下使用]{style="font-family:宋体"}**[id]{lang="EN-US"}**]{#struct_0_48648_47840_x1260983814}[命令配置允许注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的条件]{style="font-family:宋体"}

[[IP Address ]{lang="EN-US"}]{#struct_0_48648_47840_x1182732964}

[[成功注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}]{#struct_0_48648_47840_263030718}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Ln]{lang="EN-US"}]{#struct_0_48648_47840_x1508201939}

[[使用]{style="font-family:宋体"}**[number ]{lang="EN-US"}***[tag]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *number \|* **dn** *dn-tag* }]{lang="EN-US"}]{#struct_0_48648_47840_x1122938391}[命令配置的]{style="font-family:宋体"}*[tag]{lang="EN-US"}*

[[DN]{lang="EN-US" style="color:black"}[ ]{lang="EN-US"}]{#struct_0_48648_47840_1539260605}

[[使用]{style="font-family:宋体"}**[number ]{lang="EN-US"}***[tag]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *number \|* **dn** *dn-tag* }]{lang="EN-US"}]{#struct_0_48648_47840_1796805980}[命令配置的]{style="font-family:宋体"}*[dn-tag]{lang="EN-US"}*

[[Number]{lang="EN-US" style="color:black"}]{#struct_0_48648_47840_x410864259}

[[注册池中的号码]{style="font-family:宋体"}]{#struct_0_48648_47840_x1874942584}

[[当号码处于]{style="font-family:宋体"}[Unregistered]{lang="EN-US"}]{#struct_0_48648_47840_2141188305}[状态时，显示的是配置的注册号码模板，当号码处于]{style="font-family:宋体"}[Registered]{lang="EN-US"}[状态时，显示的是成功注册到语音服务器上的号码]{style="font-family:宋体"}

[[State]{lang="EN-US" style="color:black"}]{#struct_0_48648_47840_2142034892}

[[号码的注册状态：]{style="font-family:宋体"}]{#struct_0_48648_47840_x614243102}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unregistered]{lang="EN-US"}]{#struct_0_48648_47840_x678398935}[：表示号码处于未注册状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Registered]{lang="EN-US"}]{#struct_0_48648_47840_x1122938392}[：表示号码处于成功注册状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-840517689 .myid}
[]{#_Toc404794652}[]{#struct_0_48648_47840_x1189622750}

**SRST \-- SRST配置命令 \-- id**

------------------------------------------------------------------------

[**[id]{lang="EN-US"}**]{#struct_0_48648_47840_x751528040}[命令用来配置注册池中允许注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的条件。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_48648_47840_691771205}**[id]{lang="EN-US"}**[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1469709662}

[**[id ]{lang="EN-US"}**]{#struct_0_48648_47840_x1797250252}[{ **ip** *ip-address* \| **network** *network* \[ **mask** { *mask-length* \| *mask* } \] \| **mac** *mac-address* }]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **id**]{lang="EN-US"}]{#struct_0_48648_47840_x2107889424}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1527256249}

[[没有限定允许注册的条件。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1279112465}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_736210641}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1243411914}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1341933588}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1122938393}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_376461191}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_2038022183}

[**[ip ]{lang="EN-US"}**]{#struct_0_48648_47840_1079833032}*[ip-address]{lang="EN-US"}*[：[允许注册的]{style="color:black"}]{style="font-family:宋体"}[SIP [UA]{style="color:black"}]{lang="EN-US"}[的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[**[network ]{lang="EN-US"}**]{#struct_0_48648_47840_524396699}*[network]{lang="EN-US"}*[：[允许注册的]{style="color:black"}]{style="font-family:宋体"}[SIP [UA]{style="color:black"}]{lang="EN-US"}[的]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[网段]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_48648_47840_x1138826147}[：子网掩码。其中，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为子网掩码长度，]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为点分十进制格式的子网掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。不指定]{style="font-family:宋体"}**[mask]{lang="EN-US"}**[关键字，设备默认子网掩码为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，即拒绝所有]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册请求。]{style="font-family:宋体"}

[**[mac ]{lang="EN-US"}**]{#struct_0_48648_47840_666758734}*[mac-address]{lang="EN-US"}*[：[允许注册的]{style="color:black"}]{style="font-family:宋体"}[SIP [UA]{style="color:black"}]{lang="EN-US"}[的]{style="font-family:宋体;color:black"}[MAC]{lang="EN-US" style="color:black"}[地址，格式为]{style="font-family:宋体;color:black"}[H-H-H]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1052416582}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在注册池中可以通过]{style="font-family:宋体"}]{#struct_0_48648_47840_x616605684}**[id]{lang="EN-US"}**[命令配置允许注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的条件，也可以通过]{style="font-family:宋体"}**[number]{lang="EN-US"}**[命令配置允许注册的号码。至少要选择其中一种方式来指定能够注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册信息。如果同时配置，那么只有同时满足两者条件的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[才能注册成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果当前的注册池下已经配置了]{style="font-family:宋体"}]{#struct_0_48648_47840_1877094583}**[number]{lang="EN-US"}**[命令，并生成动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体，那么增加配置]{style="font-family:宋体"}**[id]{lang="EN-US"}**[后，此注册池下生成的所有已存在的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体都会被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1240467307}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x60818357}[配置注册池]{style="font-family:宋体"}[100]{lang="EN-US"}[中[允许]{style="color:black"}注册的]{style="font-family:宋体"}[SIP [UA]{style="color:black"}]{lang="EN-US"}[的]{style="font-family:宋体;color:black"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1cbd-b9e3-b2e4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1122938386}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] id mac 1cbd-b9e3-b2e4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1136041614}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[number]{lang="EN-US"}**[(Pool view)]{lang="EN-US"}]{#struct_0_48648_47840_x521035649}
:::

::: {#-418036385 .myid}
[]{#_Toc404794653}[]{#struct_0_48648_47840_x519658850}

**SRST \-- SRST配置命令 \-- max-dn**

------------------------------------------------------------------------

[**[max-dn]{lang="EN-US"}**]{#struct_0_48648_47840_41580475}[命令用来配置]{style="font-family:宋体"}[DN]{lang="EN-US"}[（]{style="font-family:宋体"}[Directory Number]{lang="EN-US"}[，号码目录）的最大数量。]{style="font-family:宋体"}

[**[undo max-dn]{lang="EN-US"}**]{#struct_0_48648_47840_837870708}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1716819340}

[**[max-dn]{lang="EN-US"}**[ *max-dn*]{lang="EN-US"}]{#struct_0_48648_47840_1265841245}

[**[undo]{lang="EN-US"}**[ **max-dn**]{lang="EN-US"}]{#struct_0_48648_47840_x1408317597}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1137658122}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_x143541841}[的最大数量为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即不允许配置]{style="font-family:宋体"}[DN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_922846670}

[[全局注册视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x1122938387}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1592841741}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_761600160}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x451381501}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x868516467}

[*[max-dn]{lang="EN-US"}*]{#struct_0_48648_47840_x1060512567}[：]{style="font-family:宋体"}[DN]{lang="EN-US"}[的最大数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x703196989}

[[在]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_48648_47840_1468455436}[下的号码完成注册并产生动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体后，如果要修改]{style="font-family:宋体"}**[max-dn]{lang="EN-US"}**[命令的参数，可以直接将该参数增大。但是如果要将该参数减小，需要使用]{style="font-family:宋体"}**[undo voice register dn]{lang="EN-US"}**[命令先手工删除比将要配置的]{style="font-family:宋体"}*[max-dn]{lang="EN-US"}*[参数值大的]{style="font-family:宋体"}*[dn-tag]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x275146160}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x2065515112}[配置]{style="font-family:宋体"}[DN]{lang="EN-US"}[的最大数量为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x273786731}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\] max-dn 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1122938388}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[voice register dn]{lang="EN-US"}**]{#struct_0_48648_47840_329472560}
:::

::: {#109164658 .myid}
[]{#_Toc404794654}[]{#struct_0_48648_47840_x609178081}

**SRST \-- SRST配置命令 \-- max-pool**

------------------------------------------------------------------------

[**[max-pool]{lang="EN-US"}**]{#struct_0_48648_47840_1578997166}[命令用来配置注册池的最大数量。]{style="font-family:宋体"}

[**[undo max- pool]{lang="EN-US"}**]{#struct_0_48648_47840_x400786708}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1499388603}

[**[max-pool]{lang="EN-US"}**[ *max-pool*]{lang="EN-US"}]{#struct_0_48648_47840_155366392}

[**[undo max-pool]{lang="EN-US"}**]{#struct_0_48648_47840_1590478587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x253054120}

[[注册池的最大数量为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_48648_47840_722935611}[，即不允许配置注册池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1998794948}

[[全局注册视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x1672664388}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_1030147461}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_106084141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_559990622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x2045038631}

[*[max-pool]{lang="EN-US"}*]{#struct_0_48648_47840_x1122938389}[：注册池的最大数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_1895556501}

[[在注册池下的号码完成注册并产生动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}]{#struct_0_48648_47840_419381568}[语音实体后，如果要修改]{style="font-family:宋体"}**[max-pool]{lang="EN-US"}**[命令的参数，可以直接将该参数增大。但是如果要将该参数减小，需要使用]{style="font-family:宋体"}**[undo voice register pool]{lang="EN-US"}**[命令先手工删除比将要配置的]{style="font-family:宋体"}*[max-pool]{lang="EN-US"}*[参数值大的]{style="font-family:宋体"}*[pool-tag]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x166486005}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1622418202}[配置注册池的最大数量为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1675566590}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\] max-pool 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_931998008}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[voice register pool]{lang="EN-US"}**]{#struct_0_48648_47840_x1723980786}
:::

::: {#1985170617 .myid}
[]{#_Toc404794655}[]{#struct_0_48648_47840_2004855272}

**SRST \-- SRST配置命令 \-- mode**

------------------------------------------------------------------------

[**[mode]{lang="EN-US"}**]{#struct_0_48648_47840_356736367}[命令用来配置设备作为语音服务器时的工作模式。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_48648_47840_x1840797514}**[mode]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1822364855}

[**[mode ]{lang="EN-US"}**]{#struct_0_48648_47840_2022434176}[{ **alive** \| **alone** }]{lang="EN-US"}

[**[undo ]{lang="EN-US"}**]{#struct_0_48648_47840_x553167498}**[mode]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1122938382}

[[设备工作在非语音服务器模式。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1189557214}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x186271570}

[[全局注册视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x166086436}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x857940989}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1460204278}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_265889403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1176812360}

[**[alone]{lang="EN-US"}**]{#struct_0_48648_47840_x2076493107}[：设备作为语音服务器工作在独立模式。]{style="font-family:宋体"}

[**[alive]{lang="EN-US"}**]{#struct_0_48648_47840_x987082299}[：设备作为语音服务器工作在本地存活模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1941480761}

[[改变语音服务器的工作模式时，语音服务器上已有的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}]{#struct_0_48648_47840_x1882367471}[注册信息都将被自动删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1577679683}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_1072896857}[配置设备作为语音服务器工作在独立模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_2118971300}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\] mode alone]{lang="EN-US"}
:::

::: {#-1051554320 .myid}
[]{#_Toc404794656}[]{#struct_0_48648_47840_1166901952}

**SRST \-- SRST配置命令 \-- number(DN view)**

------------------------------------------------------------------------

[**[number]{lang="EN-US"}**]{#struct_0_48648_47840_x1555773627}[命令用来配置[允许]{style="color:black"}注册的号码模板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **number**]{lang="EN-US"}]{#struct_0_48648_47840_x1759136928}[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1907436996}

[**[number ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_48648_47840_1896534151}

[**[undo number]{lang="EN-US"}**]{#struct_0_48648_47840_687942259}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1215713770}

[[不存在[允许]{style="color:black"}注册的号码模板。]{style="font-family:宋体"}]{#struct_0_48648_47840_1144956666}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_389449487}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_867640092}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_1092832813}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_881946222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1645857518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1411306822}

[*[number]{lang="EN-US"}*]{#struct_0_48648_47840_x303717206}[：允许注册的号码模板，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和]{style="font-family:
宋体"}[\$]{lang="EN-US"}[。]{style="font-family:宋体"}[\$]{lang="EN-US"}[只能配置在号码的最后一位，表示号码结束，号码必须全部匹配]{style="font-family:宋体"}[\$]{lang="EN-US"}[之前的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x638562474}

[[一个]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_48648_47840_1860750254}[目录只能配置一个号码模板，例如配置]{style="font-family:宋体"}**[number]{lang="EN-US"}**[ 1000]{lang="EN-US"}[，号码]{style="font-family:宋体"}[1000]{lang="EN-US"}[是一个号码模板，表示可以匹配以]{style="font-family:宋体"}[1000]{lang="EN-US"}[号码开头的号码。如果有语音组网中有话机]{style="font-family:宋体"}[10001]{lang="EN-US"}[，]{style="font-family:宋体"}[10002]{lang="EN-US"}[，]{style="font-family:宋体"}[10003]{lang="EN-US"}[，那么这些号码都可以注册到语音服务器上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1281338512}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_1215713769}[配置[允许]{style="color:black"}注册的号码模板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_1144497913}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 100]{lang="EN-US"}

[\[Sysname-voice-register-dn100\] number 1000]{lang="EN-US"}
:::

::: {#840686108 .myid}
[]{#_Toc404794657}[]{#struct_0_48648_47840_x758121398}

**SRST \-- SRST配置命令 \-- number(Register pool view)**

------------------------------------------------------------------------

[**[number]{lang="EN-US"}**]{#struct_0_48648_47840_180911457}[命令用来配置注册池中[允许]{style="color:black"}注册的号码模板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **number**]{lang="EN-US"}]{#struct_0_48648_47840_1363015226}[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x322725163}

[**[number ]{lang="EN-US"}***[tag]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *number \|* **dn** *dn-tag* }]{lang="EN-US"}]{#struct_0_48648_47840_1825022888}

[**[undo number ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_48648_47840_616897806}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x566652392}

[[不存在[允许]{style="color:black"}注册的号码模板。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1493103932}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1215713768}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1144432377}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_48648_47840_7232025}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1008353903}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x833980118}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x298458375}

[*[tag]{lang="EN-US"}*]{#struct_0_48648_47840_1865646418}[：号码索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*]{#struct_0_48648_47840_373624619}[：允许注册的号码模板，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和]{style="font-family:
宋体"}[\$]{lang="EN-US"}[，且"]{style="font-family:宋体"}[\$]{lang="EN-US"}["只能配置在号码的最后一位。]{style="font-family:宋体"}

[**[dn]{lang="EN-US"}***[ dn-tag]{lang="EN-US"}*]{#struct_0_48648_47840_1805591337}[：应用到注册池的号码目录索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_2065733601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在注册池中可以通过]{style="font-family:宋体"}]{#struct_0_48648_47840_664577277}**[id]{lang="EN-US"}**[命令配置允许注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的条件，也可以通过]{style="font-family:宋体"}**[number]{lang="EN-US"}**[命令配置允许注册的号码。至少要选择其中一种方式来指定能够注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册信息。如果同时配置，那么只有同时满足两者条件的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[才能注册成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使用]{style="font-family:宋体"}]{#struct_0_48648_47840_1733770258}**[number]{lang="EN-US"}**[命令配置[允许]{style="color:black"}注册的号码时，可以直接配置号码，也可以通过引用]{style="font-family:宋体"}[DN]{lang="EN-US"}[（]{style="font-family:宋体"}[Directory Number]{lang="EN-US"}[，号码目录）的配置。如果使用引用目录号码方式，引用的目录号码必须已经存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果当前的注册池下已经配置了]{style="font-family:宋体"}]{#struct_0_48648_47840_1215713767}**[id]{lang="EN-US"}**[命令，并生成动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体，那么使用]{style="font-family:宋体"}**[number]{lang="EN-US"}**[命令新增配置[允许]{style="color:black"}注册的号码模板后，会删除不符合新增配置的已有动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个注册池可以配置十个号码索引，并且配置的]{style="font-family:宋体"}]{#struct_0_48648_47840_1145153273}*[number]{lang="EN-US"}*[参数是一个号码模板。例如配置]{style="font-family:宋体"}**[number]{lang="EN-US"}**[ 1000]{lang="EN-US"}[，号码]{style="font-family:宋体"}[1000]{lang="EN-US"}[是一个号码模板，表示可以匹配以]{style="font-family:宋体"}[1000]{lang="EN-US"}[号码开头的号码。如果有语音组网中有话机]{style="font-family:宋体"}[10001]{lang="EN-US"}[，]{style="font-family:宋体"}[10002]{lang="EN-US"}[，]{style="font-family:宋体"}[10003]{lang="EN-US"}[，那么这些号码都可以注册到语音服务器上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1933168415}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1364411947}[配置[允许]{style="color:black"}注册的号码模板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1376814712}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] number 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1372769603}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[voice register dn]{lang="EN-US"}**]{#struct_0_48648_47840_x2012234736}
:::

::: {#735153216 .myid}
[]{#_Toc404794658}[]{#struct_0_48648_47840_x2138582151}[]{#_Toc383611839}[]{#_Toc355262317}[]{#_Toc295911311}[]{#_Toc262031004}[]{#_Toc135295492}[]{#_Toc130097141}[]{#_Toc129160861}[]{#_Toc47776203}

**SRST \-- SRST配置命令 \-- outband**

------------------------------------------------------------------------

[**[outband]{lang="EN-US"}**]{#struct_0_48648_47840_1972853796}[命令用来配置使用带外方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[（]{style="font-family:宋体"}[Dual Tone Multi-Frequency]{lang="EN-US"}[，双音多频）信号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **outband**]{lang="EN-US"}]{#struct_0_48648_47840_850569377}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_630704302}

[**[outband]{lang="PT-BR"}**]{#struct_0_48648_47840_x2034003508}[ ]{lang="PT-BR"}[{ **nte** \| **sip** }]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **outband**]{lang="EN-US"}]{#struct_0_48648_47840_1215713774}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1145218810}

[[使用带内方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}]{#struct_0_48648_47840_x1179784977}[信号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_744631250}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1347305657}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x618535387}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1007472554}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_334933968}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_1589991672}

[**[nte]{lang="EN-US"}**]{#struct_0_48648_47840_1729096426}[：]{style="font-family:宋体"}[使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}[（]{style="font-family:宋体"}[Named Telephone Event]{lang="EN-US"}[，命名的电话事件）带外方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[**[sip]{lang="EN-US"}**]{#struct_0_48648_47840_x1196733781}[：]{style="font-family:宋体"}[使用]{style="font-family:宋体"}[SIP]{lang="EN-US"}[带外方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x879012754}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_1040313036}[配置使用]{style="font-family:宋体"}[NTE]{lang="EN-US"}[带外方式传输]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_453824353}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 10]{lang="EN-US"}

[\[Sysname-voice-register-pool10\] outband nte]{lang="EN-US"}
:::

::: {#567732879 .myid}
[]{#_Toc404794659}[]{#struct_0_48648_47840_1215713773}

**SRST \-- SRST配置命令 \-- priority**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**]{#struct_0_48648_47840_1144891130}[命令用来配置指向]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_48648_47840_x35408022}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x25890393}

[**[priority]{lang="EN-US"}**[ *order*]{lang="EN-US"}]{#struct_0_48648_47840_1425708316}

[**[undo]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_48648_47840_x1394157480}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_2028451009}

[[优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_48648_47840_x1003578242}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x30947813}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_x695953861}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[注册池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1210267466}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1479953611}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1635398867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_1215713772}

[*[order]{lang="EN-US"}*]{#struct_0_48648_47840_1144825594}[：为号码生成动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，数值越小表示优先级越高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1568611068}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x82201690}[配置为]{style="font-family:宋体"}[DN]{lang="EN-US"}[视图下号码模版]{style="font-family:宋体"}[1000]{lang="EN-US"}[生成动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的优先级为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x412739778}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 100]{lang="EN-US"}

[\[Sysname-voice-register-dn100\] number 1000]{lang="EN-US"}

[\[Sysname-voice-register-dn100\] priority 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_318636796}[配置为注册池下号码模版]{style="font-family:宋体"}[2000]{lang="EN-US"}[生成动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的优先级为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1294087078}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 10]{lang="EN-US"}

[\[Sysname-voice-register-pool10\] priority 6]{lang="EN-US"}

[\[Sysname-voice-register-pool10\] number 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1208240201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[number]{lang="EN-US"}**]{#struct_0_48648_47840_322184236}**[ ]{lang="EN-US"}**[(DN view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[number]{lang="EN-US"}**]{#struct_0_48648_47840_1215713771}**[ ]{lang="EN-US"}**[(Pool view)]{lang="EN-US"}
:::

::: {#-834486084 .myid}
[]{#_Toc404794660}[]{#struct_0_48648_47840_1145022202}[]{#_Toc378515394}

**SRST \-- SRST配置命令 \-- proxy**

------------------------------------------------------------------------

[**[proxy]{lang="EN-US"}**]{#struct_0_48648_47840_x776316256}[命令用来配置远端语音服务器地址信息及开启保活探测功能。]{style="font-family:宋体"}

[**[undo proxy]{lang="EN-US"}**]{#struct_0_48648_47840_x353583654}[命令用来删除已配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1661703326}

[**[proxy ip ]{lang="EN-US"}***[ip1 ]{lang="EN-US"}*[\[ **port** *main-port-number* \] \[ **monitor probe sip** \[ *ip2* \[ **port** *backup-port-number* \] \] \] \[ **priority** *order* \]]{lang="EN-US"}]{#struct_0_48648_47840_898609465}

[**[undo]{lang="EN-US"}**[ **proxy**]{lang="EN-US"}]{#struct_0_48648_47840_x2001247380}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x205341189}

[[没有配置语音远端服务器信息。]{style="font-family:宋体"}]{#struct_0_48648_47840_1013409188}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1393439974}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1342914227}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_1150054465}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1215713778}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_1144432378}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_48648_47840_6642201}

[**[ip]{lang="EN-US"}***[ ip1]{lang="EN-US"}*]{#struct_0_48648_47840_884975565}[：远端语音主服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *main-port-number*]{lang="EN-US"}]{#struct_0_48648_47840_1588395910}[：远端语音主服务器的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5060]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[monitor probe sip]{lang="EN-US"}**]{#struct_0_48648_47840_x1069039974}[：开启保活探测功能。]{style="font-family:宋体"}

[*[ip2]{lang="EN-US"}*]{#struct_0_48648_47840_396189685}[：远端备份语音服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *backup-port-number*]{lang="EN-US"}]{#struct_0_48648_47840_1654588799}[：远端备份语音服务器的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5060]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[priority]{lang="EN-US"}*]{#struct_0_48648_47840_x940717748}[：产生的指向远端语音主服务器的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x389756314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能在本地存活模式的语音服务器上生效。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1244254652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[此命令可以完成两个功能，一是配置远端主、备语音服务器信息，二是开启保活探测功能（可选），保活探测的具体参数由注册池下的]{lang="EN-US" style="font-family:宋体"}**[voice-class sip options-keepalive]{lang="EN-US"}**]{#struct_0_48648_47840_x1004427948}[命令确定。如果配置]{lang="EN-US" style="font-family:宋体"}**[monitor probe sip]{lang="EN-US"}**[参数开启保活探测功能，生成的指向远端语音服务器的动态]{lang="EN-US" style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体会返回保活探测结果。如果保活探测结果为]{lang="EN-US" style="font-family:宋体"}[VoIP entity available]{lang="EN-US"}[，则表示远端语音服务器可达。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_918107004}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1721592578}[配置远端服务器地址信息，并开启保活探测功能。]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[号码成功注册到语音服务上后，在语音服务上生成指向指定远端服务器（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[）的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_1215713777}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] proxy ip 1.1.1.1 monitor probe sip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1145153274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[voice-class sip options-keepalive]{lang="EN-US"}**]{#struct_0_48648_47840_x1315761132}
:::

::: {#1345102398 .myid}
[]{#_Toc404794661}[]{#struct_0_48648_47840_x1681736550}[]{#_Toc316720183}

**SRST \-- SRST配置命令 \-- registrar server**

------------------------------------------------------------------------

[**[registrar ]{lang="EN-US"}[server]{lang="EN-US"}**]{#struct_0_48648_47840_x340391712}[命令用来]{style="font-family:宋体"}[开启接受注册服务，并配置全局注册时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **registrar** **server**]{lang="EN-US"}]{#struct_0_48648_47840_x1858763383}[命令用来关闭注册服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x940872510}

[**[registrar]{lang="EN-US"}**[ **server** \[ **expires** { **max** *max * \| **min** *min* } **\*** \]]{lang="EN-US"}]{#struct_0_48648_47840_x413456229}

[**[undo registrar server]{lang="EN-US"}**]{#struct_0_48648_47840_x1983530027}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1654741855}

[[接受]{style="font-family:宋体"}]{#struct_0_48648_47840_346796047}[注册服务处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x854046166}

[[SIP]{lang="FR"}]{#struct_0_48648_47840_68171265}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x740601366}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1358002644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_61341037}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_1757837587}

[**[expires]{lang="EN-US"}**]{#struct_0_48648_47840_x1851838817}[：指定服务器接受的注册有效时间。缺省情况下，接受的注册有效时间范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[max]{lang="EN-US"}**]{#struct_0_48648_47840_402191315}[：全局注册有效时间的最大值，取值范围为]{style="font-family:宋体"}[120]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。缺省情况下，注册有效时间的最大值为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[min]{lang="EN-US"}**]{#struct_0_48648_47840_1508277088}[：全局注册有效时间的最小值，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。缺省情况下，注册有效时间的最小值为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x36470284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启该命令后，设备作为语音服务器才能接收]{style="font-family:宋体"}]{#struct_0_48648_47840_x1579087207}[SIP UA]{lang="EN-US"}[的注册。接收到]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册报文中，如果注册时间不在指定的范围内，语音服务器会通知]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[其可接受的注册有效时间。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **registrar** **server**]{lang="EN-US"}]{#struct_0_48648_47840_39888939}[命令关闭注册服务后，设备会]{lang="EN-US" style="font-family:宋体"}[拒绝新]{lang="EN-US" style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册请求，对已有注册]{lang="EN-US" style="font-family:宋体"}[SIP UA]{lang="EN-US"}[号码没有影响，已注册]{lang="EN-US" style="font-family:宋体"}[SIP UA]{lang="EN-US"}[在老化时间超时后，注销其信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在注册池下如果没有配置注册有效时间，缺省采用]{style="font-family:宋体"}]{#struct_0_48648_47840_x138808624}**[registrar server]{lang="EN-US"}**[命令配置的全局注册有效时间。如果都进行了配置，则优先采用注册池视图下注册有效时间的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_877299697}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x443937953}[配置]{style="font-family:宋体"}[开启注册服务，全局配置中注册有效时间的最大值为]{style="font-family:宋体"}[3000]{lang="EN-US"}[秒，最小值为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x740601367}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] sip]{lang="EN-US"}

[\[Sysname-voice-sip\] registrar server expires max 3000 min 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1357937108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode]{lang="EN-US"}**]{#struct_0_48648_47840_x337398650}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[voice register global]{lang="EN-US"}**]{#struct_0_48648_47840_898664207}
:::

::: {#752929333 .myid}
[]{#_Toc404794662}[]{#struct_0_48648_47840_1929488266}

**SRST \-- SRST配置命令 \-- registration-timer**

------------------------------------------------------------------------

[**[registration-timer]{lang="EN-US"}**]{#struct_0_48648_47840_x1895638990}[命令用来配置]{style="font-family:宋体"}[注册池下的注册有效时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **registration-timer**]{lang="EN-US"}]{#struct_0_48648_47840_1898835562}[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_2087236988}

[**[registration-timer max ]{lang="EN-US"}***[max]{lang="EN-US"}***[ min ]{lang="EN-US"}***[min]{lang="EN-US"}*]{#struct_0_48648_47840_x352234515}

[**[undo registration-timer]{lang="EN-US"}**]{#struct_0_48648_47840_x653516934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_2048669384}

[[注册池下没有缺省的注册有效时间]{style="font-family:宋体"}]{#struct_0_48648_47840_1024545026}[。如果该注册池下没有]{style="font-family:宋体"}[注册有效时间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[那么该注册池使用全局命令]{style="font-family:宋体"}**[registrar server]{lang="EN-US"}**[设置的全局注册有效时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_102028650}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x437040404}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x740601368}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1357347284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x134727604}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_1591641317}

[**[max]{lang="EN-US"}**]{#struct_0_48648_47840_x1074863152}[：注册有效时间的最大值，取值范围为]{style="font-family:宋体"}[120]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[min]{lang="EN-US"}**]{#struct_0_48648_47840_160959577}[：注册有效时间的最小值，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x767989174}

[[在注册池下如果没有配置注册有效时间，缺省采用]{style="font-family:宋体"}**[registrar server]{lang="EN-US"}**]{#struct_0_48648_47840_x392040088}[命令配置的全局注册有效时间。如果都进行了配置，则优先采用注册池视图下注册有效时间的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1058855623}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_777192582}[配置]{style="font-family:宋体"}[注册有效时间最大值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[，最小值为]{style="font-family:宋体"}[300]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1882555848}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] registration-timer max 2000 min 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1343041328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[registrar]{lang="EN-US"}**[ **server**]{lang="EN-US"}]{#struct_0_48648_47840_x394807181}
:::

::: {#757626371 .myid}
[]{#_Toc404794663}[]{#struct_0_48648_47840_x26567860}[]{#_Toc370738282}[]{#_Toc205711308}[]{#_Toc136850868}[]{#_Toc129160915}[]{#_Toc47776221}

**SRST \-- SRST配置命令 \-- substitute**

------------------------------------------------------------------------

[**[substitute]{lang="EN-US"}**]{#struct_0_48648_47840_x740601369}[命令用来将指定号码变换规则表绑定到注册池。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **substitute**]{lang="EN-US"}]{#struct_0_48648_47840_x1357281748}[命令用来取消已有的绑定关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1642908017}

[**[substitute]{lang="EN-US"}**[ { **called** \| **calling** } *list-number*]{lang="EN-US"}]{#struct_0_48648_47840_x914495611}

[**[undo]{lang="EN-US"}**[ **substitute** { **called** \| **calling** }]{lang="EN-US"}]{#struct_0_48648_47840_1578053741}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_445491621}

[[没有绑定号码变换规则表，即不进行号码变换。]{style="font-family:宋体"}]{#struct_0_48648_47840_867193634}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1802767196}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_2142142803}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_542002622}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1629108648}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_903862428}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x837787635}

[**[called]{lang="EN-US"}**]{#struct_0_48648_47840_1832748264}[：对被叫号码应用号码变换。]{style="font-family:宋体"}

[**[calling]{lang="EN-US"}**]{#struct_0_48648_47840_1971173784}[：对主叫号码应用号码变换。]{style="font-family:宋体"}

[*[list-number]{lang="EN-US"}*]{#struct_0_48648_47840_x740601362}[：绑定的号码变换规则表的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1357740500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以将一个不存在的号码变换规则表绑定到注册池，但只有完成号码变换规则表的配置后，该号码变换规则表才能生效。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1442772301}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在注册池下只能绑定一种号码变换规则表，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_48648_47840_905719502}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1003420657}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_884679521}[配置将号码变换规则表]{style="font-family:宋体"}[6]{lang="EN-US"}[绑定到注册池]{style="font-family:宋体"}[100]{lang="EN-US"}[，表示对被叫号码应用号码变换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_996933514}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] substitute called 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x495142662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[number-substitute]{lang="EN-US"}**]{#struct_0_48648_47840_44579942}[（语音命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[拨号策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_48648_47840_x1338293700}[（语音命令参考]{style="font-family:
宋体"}[/]{lang="EN-US"}[拨号策略）]{style="font-family:宋体"}
:::

::: {#-2032495825 .myid}
[]{#_Toc404794664}[]{#struct_0_48648_47840_1590236418}[]{#_Toc383609645}[]{#_Toc354937945}[]{#_Toc316720184}

**SRST \-- SRST配置命令 \-- username**

------------------------------------------------------------------------

[**[username]{lang="EN-US"}**]{#struct_0_48648_47840_x1080868315}[命令用来配置注册池中的]{style="font-family:宋体"}[鉴权信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**]{#struct_0_48648_47840_786065055}[ **username**]{lang="EN-US"}[命令用来]{style="font-family:宋体"}[删除已有配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_673659163}

[**[username]{lang="EN-US"}**[ *username* **password** { **cipher** \| **simple** } *password* ]{lang="EN-US"}]{#struct_0_48648_47840_x740601363}

[**[undo]{lang="EN-US"}**[ **username**]{lang="EN-US"}]{#struct_0_48648_47840_x1357674964}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1588500722}

[[不存在鉴权信息，即语音服务器不对]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}]{#struct_0_48648_47840_366074853}[进行鉴权。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x597383531}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1681246223}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x376545049}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x32743371}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_803430184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_1045346926}

[*[username]{lang="EN-US"}*]{#struct_0_48648_47840_1433962585}[：用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_48648_47840_835845426}[：以密文方式设置用户的密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_48648_47840_x1461818428}[：以明文方式设置用户的密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_48648_47840_745912822}[：明文密码或密文密码，区分大小写。明文密码的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[；密文密码的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1470058426}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[authentication register]{lang="EN-US"}**]{#struct_0_48648_47840_x740601364}[命令开启注册鉴权后，语音服务器会使用本命令配置的鉴权信息对]{lang="EN-US" style="font-family:宋体"}[SIP UA]{lang="EN-US"}[进行鉴权。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[工作在本地存活模式的语音服务器不会对用户信息进行鉴权，因此在该模式的语音服务器上配置的鉴权信息不会生效。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1358133716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需要注意的是，在注册池下配置的]{style="font-family:宋体"}]{#struct_0_48648_47840_1734427377}**[username]{lang="EN-US"}**[命令不会同步到动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1565739324}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x348775856}[配置注册池中的]{style="font-family:宋体"}[鉴权信息，用户名为]{style="font-family:
宋体"}[abcd]{lang="EN-US"}[，以明文方式设置密码为]{style="font-family:宋体"}[1234]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_1869788061}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] username abcd password simple 1234]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_949464729}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authenticate register]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_48648_47840_1619913381}
:::

::: {#1254060135 .myid}
[]{#_Toc404794665}[]{#struct_0_48648_47840_960734772}

**SRST \-- SRST配置命令 \-- voice register dn**

------------------------------------------------------------------------

[**[voice register dn]{lang="EN-US"}**]{#struct_0_48648_47840_1025220579}[命令用来创建并进入指定的]{style="font-family:宋体"}[DN]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_48648_47840_x1087097821}**[voice register dn]{lang="EN-US"}**[命令用来删除指定的]{style="font-family:宋体"}[DN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x740601365}

[**[voice register dn ]{lang="EN-US"}**]{#struct_0_48648_47840_x1358068180}*[dn]{lang="EN-US"}*[-*tag*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_48648_47840_x643818740}**[voice register dn ]{lang="EN-US"}***[dn]{lang="EN-US"}[-tag]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x2088651099}

[[不存在]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_48648_47840_x1227702911}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_426588378}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x1830970582}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x925605031}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1180804038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x170899241}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_505538956}

[*[dn-tag]{lang="EN-US"}*]{#struct_0_48648_47840_1841316979}[：号码目录索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x740601358}

[[如果需要为某个号码做特殊的配置，例如配置指向其的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}]{#struct_0_48648_47840_x1357347281}[语音实体或是为该号码开启特定的语音业务，这时可以配置]{style="font-family:宋体"}[DN]{lang="EN-US"}[，然后将]{style="font-family:宋体"}[DN]{lang="EN-US"}[引用到注册池中，实现将]{style="font-family:宋体"}[DN]{lang="EN-US"}[下号码注册到语音服务器上。需要注意的是，]{style="font-family:宋体"}[DN]{lang="EN-US"}[下的配置优先级高于]{style="font-family:宋体"}[Pool]{lang="EN-US"}[注册池下的配置。例如在注册池下配置]{style="font-family:宋体"}**[id]{lang="EN-US"}**[命令，使]{style="font-family:宋体"}[10.1.1.0]{lang="EN-US"}[网段上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[话机使用该注册池的设置，在这个网段中对于号码为]{style="font-family:宋体"}[1000]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[话机需要做特殊配置，例如修改指向号码]{style="font-family:宋体"}[1000]{lang="EN-US"}[的动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[，这时可以为号码]{style="font-family:宋体"}[1000]{lang="EN-US"}[配置]{style="font-family:宋体"}[DN]{lang="EN-US"}[，在]{style="font-family:宋体"}[DN]{lang="EN-US"}[视图配置]{style="font-family:宋体"}**[priority]{lang="EN-US"}**[ 1]{lang="EN-US"}[，该配置优先于号码]{style="font-family:宋体"}[1000]{lang="EN-US"}[所在注册池的]{style="font-family:宋体"}**[priority]{lang="EN-US"}**[命令优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x538012131}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_582404839}[创建号码目录]{style="font-family:宋体"}[100]{lang="EN-US"}[，并进入指定的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1784690757}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 100]{lang="EN-US"}

[\[Sysname-voice-register-dn100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x927783203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-dn]{lang="EN-US"}**]{#struct_0_48648_47840_276848460}
:::

::: {#39320180 .myid}
[]{#_Toc404794666}[]{#struct_0_48648_47840_563747386}

**SRST \-- SRST配置命令 \-- voice register global**

------------------------------------------------------------------------

[**[voice register global]{lang="EN-US"}**]{#struct_0_48648_47840_1610578235}[命令用来创建并进入全局注册视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **voice register global**]{lang="EN-US"}]{#struct_0_48648_47840_314943834}[命令用来删除全局注册视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x735518540}

[**[voice register global]{lang="EN-US"}**]{#struct_0_48648_47840_x66353329}

[**[undo voice register global]{lang="EN-US"}**]{#struct_0_48648_47840_x740601359}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_830345713}

[[不存在全局注册视图。]{style="font-family:宋体"}]{#struct_0_48648_47840_x735738228}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1357281745}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_883393130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_869514032}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x2041679274}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_1569107755}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x501120020}

[[配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **voice register global**]{lang="EN-US"}]{#struct_0_48648_47840_x252383008}[命令后，设备会自动删除已存在的]{style="font-family:
宋体"}[DN]{lang="EN-US"}[、注册池和所有动态]{style="font-family:
宋体"}[VoIP]{lang="EN-US"}[语音实体，并强制注销已注册的]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_705401943}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x879543355}[创建并进入全局注册视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x936872192}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\]]{lang="EN-US"}
:::

::: {#1473992474 .myid}
[]{#_Toc404794667}[]{#struct_0_48648_47840_771345492}

**SRST \-- SRST配置命令 \-- voice register pool**

------------------------------------------------------------------------

[**[voice register pool]{lang="EN-US"}**]{#struct_0_48648_47840_x384058076}[命令用来创建并进入指定的注册池视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_48648_47840_1837997867}**[voice register pool]{lang="EN-US"}**[命令用来删除指定的注册池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_220247589}

[**[voice register pool ]{lang="EN-US"}**]{#struct_0_48648_47840_1598050794}*[pool]{lang="EN-US"}*[-*tag*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_48648_47840_1118132389}**[voice register pool ]{lang="EN-US"}***[pool]{lang="EN-US"}*[-*tag*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1553916984}

[[不存在注册池。]{style="font-family:宋体"}]{#struct_0_48648_47840_1766599182}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x799923469}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_200067254}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x148230535}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1653674153}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_459297375}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_1157555340}

[*[pool-tag]{lang="EN-US"}*]{#struct_0_48648_47840_x1924080285}[：注册池索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x151287761}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[注册池是]{style="font-family:宋体"}]{#struct_0_48648_47840_402506148}[SIP UA]{lang="EN-US"}[注册信息的集合，如果]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[的注册信息匹配上注册池中配置的条件，那么这些]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[可以注册到语音服务器上。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **voice register pool**]{lang="EN-US"}]{#struct_0_48648_47840_x325741696}[命令时，由该注册池生成的所有动态]{lang="EN-US" style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体会被删除。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x271288801}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_1598050793}[创建注册池索引]{style="font-family:宋体"}[100]{lang="EN-US"}[，并进入指定的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_1117935781}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1754963497}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-pool]{lang="EN-US"}**]{#struct_0_48648_47840_x1745705332}
:::

::: {#1334524894 .myid}
[]{#_Toc404794668}[]{#struct_0_48648_47840_x1504199578}[]{#_Toc383611846}[]{#_Toc355262372}

**SRST \-- SRST配置命令 \-- voice-class codec**

------------------------------------------------------------------------

[**[voice-class codec]{lang="EN-US"}**]{#struct_0_48648_47840_x29281102}[命令用来将指定的编解码模板绑定到注册池。]{style="font-family:宋体"}

[**[undo voice-class codec]{lang="EN-US"}**]{#struct_0_48648_47840_707899920}[用来取消已有的绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_2122187511}

[**[voice-class codec]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_48648_47840_x1941917086}

[**[undo voice-class codec]{lang="EN-US"}**]{#struct_0_48648_47840_x1437856414}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x822609791}

[[编解码模板和注册池没有绑定关系。]{style="font-family:宋体"}]{#struct_0_48648_47840_1598050792}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1118001317}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1177784457}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1462040809}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_989538679}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_824401943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1163430191}

[*[tag]{lang="EN-US"}*]{#struct_0_48648_47840_573611731}[：绑定的编解码模板号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x534469083}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以将一个不存在的编解码模板绑定到注册池，但只有在使用]{style="font-family:宋体"}]{#struct_0_48648_47840_x1842998569}**[codec preference]{lang="EN-US"}**[命令完成编解码优先级的设置后，该编解码模板才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在注册池下只能绑定一个编解码模板，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_48648_47840_753653610}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1959137755}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1971784518}[将编解码模板]{style="font-family:宋体"}[1]{lang="EN-US"}[绑定到注册池]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x643039509}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] voice-class codec 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1598050791}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[codec preference]{lang="EN-US"}**]{#struct_0_48648_47840_1117804709}[（语音命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[语音实体）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[voice class codec]{lang="EN-US"}**]{#struct_0_48648_47840_975558281}[（语音命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[语音实体）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#314585580 .myid}
[]{#_Toc404794669}[]{#struct_0_48648_47840_x1802544802}[]{#_Toc383609647}[]{#_Toc354937946}[]{#_Ref350860377}[]{#_Ref350860372}[]{#_Toc350172376}

**SRST \-- SRST配置命令 \-- voice-class sip options-keepalive**

------------------------------------------------------------------------

[**[voice-class sip options-keepalive]{lang="EN-US"}**]{#struct_0_48648_47840_1977520723}[命令用来配置保活报文的参数。]{style="font-family:宋体"}

[**[undo voice-class sip options-keepalive]{lang="EN-US"}**]{#struct_0_48648_47840_x1696582558}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_2040737786}

[**[voice-class sip options-keepalive]{lang="EN-US"}**[ \[ **up-interval** *seconds* \] \[ **down-interval** *seconds* \] \[ **retry** *retries* \]]{lang="EN-US"}]{#struct_0_48648_47840_x684199897}

[**[undo voice-class sip options-keepalive]{lang="EN-US"}**]{#struct_0_48648_47840_x1353116640}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_184830185}

[**[up-interval]{lang="EN-US"}**]{#struct_0_48648_47840_753186961}[为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒，]{style="font-family:宋体"}**[down-interval]{lang="EN-US"}**[为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒，]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1980224294}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x136756590}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_1598050798}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1117345957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_914514710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_1184701112}

[**[up-interval ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_48648_47840_x1187976275}[：在标记远端语音服务器为不可用前，本地语音服务器发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}[报文的时间间隔。取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}[。单位为秒。该参数在远端语音服务器为可达时生效。]{style="font-family:宋体"}

[**[down-interval ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_48648_47840_1431539463}[：在标记远端语音服务器为可用前，本地语音服务器发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}[报文的时间间隔。取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}[。单位为秒。该参数在远端语音服务器为可达时生效。]{style="font-family:宋体"}

[**[retry ]{lang="EN-US"}***[retries]{lang="EN-US"}*]{#struct_0_48648_47840_2125939887}[：在改变远端语音服务器状态前，重复探测的次数。取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_1835810689}

[[使用]{style="font-family:宋体"}**[proxy]{lang="EN-US"}**]{#struct_0_48648_47840_x849800165}[命令开启保活功能后，本地语音服务器会按配置的]{style="font-family:宋体"}**[up-interval]{lang="EN-US"}**[参数]{style="font-family:宋体"}[定时发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}[报文，如果本地语音服务器在]{style="font-family:宋体"}**[up-interval]{lang="EN-US"}**[时间内]{style="font-family:宋体"}[收到远端语音服务器应答报文，则表示远端服务器处于可达状态，本地语音服务器继续使用]{style="font-family:宋体"}**[up-interval]{lang="EN-US"}**[参数]{style="font-family:宋体"}[定时发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}[报文；如果本地语音服务器在]{style="font-family:宋体"}**[up-interval]{lang="EN-US"}**[时间内]{style="font-family:宋体"}[没有收到应答报文或是收到的应答报文为]{style="font-family:宋体"}[408]{lang="EN-US"}[、]{style="font-family:宋体"}[499]{lang="EN-US"}[以及]{style="font-family:宋体"}[5XX]{lang="EN-US"}[（]{style="font-family:宋体"}[500]{lang="EN-US"}[、]{style="font-family:宋体"}[501]{lang="EN-US"}[、]{style="font-family:宋体"}[502]{lang="EN-US"}[、]{style="font-family:宋体"}[503]{lang="EN-US"}[、]{style="font-family:宋体"}[504]{lang="EN-US"}[、]{style="font-family:宋体"}[513]{lang="EN-US"}[除外），会开始重复探测，每次探测的时间间隔由]{style="font-family:宋体"}**[timers options]{lang="EN-US"}**[命令控制，在完成重复探测后，若还未收到表示远端语音服务器可用的应答报文，则表示本地语音服务器处于不可达状态。]{style="font-family:宋体"}

[[如果远端语音服务器被判定为处于不可达状态，则本地语音服务器会按配置的]{style="font-family:宋体"}**[down-interval]{lang="EN-US"}**]{#struct_0_48648_47840_x767684144}[参数]{style="font-family:宋体"}[定时发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}[报文，如果收到表示远端语音服务器可达的应答报文，会开始重复探测，每次探测的时间间隔由]{style="font-family:宋体"}**[timers options]{lang="EN-US"}**[命令控制，在重复探测期间，本地语音服务器每次都能收到远端]{style="font-family:宋体"} [语音服务器的]{style="font-family:宋体"}[应答报文，则将远端语音服务器的状态恢复为可达。如果一直没有收到表示远端语音服务器可达的应答报文，则本地语音服务器继续按配置的]{style="font-family:宋体"}**[down-interval]{lang="EN-US"}**[参数]{style="font-family:宋体"}[定时发送]{style="font-family:宋体"}[OPTIONS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[需要注意的是，在注册池下配置的]{style="font-family:宋体"}**[voice-class sip options-keepalive]{lang="EN-US"}**]{#struct_0_48648_47840_x439094283}[命令不会同步到动态]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[语音实体上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1598050797}

[[\# ]{lang="FR"}]{#struct_0_48648_47840_1118197925}[配置保活报文的参数，]{style="font-family:宋体"}**[up-interval]{lang="EN-US"}**[为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒，]{style="font-family:宋体"}**[down-interval]{lang="EN-US"}**[为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒，]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x66356833}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 100]{lang="EN-US"}

[\[Sysname-voice-register-pool100\] voice-class sip options-keepalive up-interval 50 down-interval 20 retry 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_458718285}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[proxy]{lang="EN-US"}**]{#struct_0_48648_47840_x848004908}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timers options]{lang="EN-US"}**]{#struct_0_48648_47840_x1965277698}[（语音命令参考]{lang="EN-US" style="font-family:宋体"}[/SIP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1526392022 .myid}
[]{#_Toc404794671}[]{#struct_0_48648_47840_860781625}

**SRST \-- SRST业务配置命令 \-- after-hours block pattern**

------------------------------------------------------------------------

[**[after-hours block pattern]{lang="EN-US"}**]{#struct_0_48648_47840_1393174451}[命令用来开启呼叫阻塞功能。]{style="font-family:
宋体"}

[**[undo after-hours block pattern]{lang="EN-US"}**]{#struct_0_48648_47840_x1489753345}[命令用来关闭呼叫阻塞功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1598050796}

[**[after-hours block pattern ]{lang="EN-US"}***[pattern-tag pattern]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **7-24** \]]{lang="EN-US"}]{#struct_0_48648_47840_1118263461}

[**[undo after-hours block pattern ]{lang="EN-US"}***[pattern-tag]{lang="EN-US"}*]{#struct_0_48648_47840_1584506776}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1637507073}

[[呼叫阻塞功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_48648_47840_2038675107}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x853556779}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_589641419}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_691149456}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1068743054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x403197631}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_180637359}

[*[pattern-tag]{lang="EN-US"}*]{#struct_0_48648_47840_1120120683}[：呼叫阻塞索引，取值范围为[1]{lang="EN-US"}]{style="font-family:宋体"}[～]{style="font-family:宋体"}[100]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[pattern]{lang="EN-US"}*]{#struct_0_48648_47840_1598050795}[：匹配阻塞的被叫号码模板]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，由"]{style="font-family:宋体"}[0-9#]{lang="EN-US"}[\*]{lang="EN-US" style="font-family:宋体"}[.!+%\[\]()-]{lang="EN-US"}["中的字符组合形成的字符串，第一个字符必须为数字。]{style="font-family:宋体"}[各符号的含义如]{style="font-family:
宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?1526392022#_Ref148492379)[所示。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加号"]{style="font-family:宋体"}]{#struct_0_48648_47840_1118066853}[+]{lang="EN-US"}["：号码模板如果以"]{style="font-family:宋体"}[+]{lang="EN-US"}["号开头，"]{style="font-family:宋体"}[+]{lang="EN-US"}["号表示整个号码是一个]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准号码，如]{style="font-family:宋体"}[+110022]{lang="EN-US"}[表示]{style="font-family:宋体"}[110022]{lang="EN-US"}[是符合]{style="font-family:宋体"}[E.164]{lang="EN-US"}[标准的号码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[美元符号"]{style="font-family:宋体"}]{#struct_0_48648_47840_343207518}[\$]{lang="EN-US"}["：只能放在结尾，表示号码结束，号码必须全部匹配]{style="font-family:宋体"}[\$]{lang="EN-US"}[之前的]{style="font-family:宋体"}*[string]{lang="EN-US"}*[部分。如果号码模板后没有]{style="font-family:宋体"}[\$]{lang="EN-US"}[字符，则表示可以匹配以此号码开头的号码，例如配置]{style="font-family:宋体"}**[match-template ]{lang="EN-US"}**[20]{lang="EN-US"}[，表示可以匹配以]{style="font-family:宋体"}[20]{lang="EN-US"}[号码开头的号码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[符号"]{style="font-family:宋体"}]{#struct_0_48648_47840_2040972698}[T]{lang="EN-US"}["：]{style="font-family:宋体"}[T]{lang="EN-US"}[表示定时器，表示在用户输入的号码超过最大长度、用户拨号码终止符或是定时器超时前，设备会等待用户拨号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[string]{lang="EN-US"}*]{#struct_0_48648_47840_860572877}[：由"]{lang="EN-US" style="font-family:宋体"}[0-9#]{lang="EN-US"}[\*]{lang="EN-US" style="font-family:宋体"}[.!+%\[\]()-]{lang="EN-US"}["中的字符组合形成的字符串。]{lang="EN-US" style="font-family:宋体"}[各符号的含义如]{style="font-family:
宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?1526392022#_Ref148492379)[所示。]{style="font-family:宋体"}

[]{#struct_0_48648_47840_x488316350}[]{#_Ref148492379}[]{#_Toc121809759}[[表1-4 ]{lang="EN-US"}[符号含义]{style="font-family:黑体"}]{#_Toc112125389}[描述表]{style="font-family:黑体"}

[]{#table_struct_0_502767554}[[符号]{style="font-family:黑体"}]{#struct_0_48648_47840_1946824132}
:::

[[含义]{style="font-family:黑体"}]{#struct_0_48648_47840_x3575709}

[[0-9]{lang="EN-US"}]{#struct_0_48648_47840_558830541}

[[一位数字表示一位号码，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_48648_47840_x1388335722}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[之间的数字]{style="font-family:宋体"}

[[\#]{lang="EN-US"}]{#struct_0_48648_47840_1598050802}[和]{style="font-family:宋体"}[\*]{lang="EN-US" style="font-family:宋体"}

[[表示一位有效号码]{style="font-family:宋体"}]{#struct_0_48648_47840_1455708332}

[[.]{lang="EN-US"}]{#struct_0_48648_47840_x372258421}

[[通配符，可以与任何一位有效号码匹配。如：]{style="font-family:宋体"}[555. . . . ]{lang="EN-US"}]{#struct_0_48648_47840_x1291887357}[可以匹配任何以]{style="font-family:宋体"}[555]{lang="EN-US"}[开头的并有四位附加字符的号码]{style="font-family:宋体"}

[[!]{lang="EN-US"}]{#struct_0_48648_47840_x375014304}

[[指明符号前的字符串重复零次或一次。如：]{style="font-family:宋体"}[56!1234]{lang="EN-US"}]{#struct_0_48648_47840_1241240583}[可以匹配]{style="font-family:宋体"}[51234]{lang="EN-US"}[和]{style="font-family:宋体"}[561234]{lang="EN-US"}

[[符号"]{style="font-family:宋体"}[!%+]{lang="EN-US"}]{#struct_0_48648_47840_714228752}["前的字符串（一位号码或号码串），作为非精确匹配的号码，处理类似"]{style="font-family:宋体"}**[.]{lang="EN-US"}**["通配符；这些符号不能作为独立号码，之前必须有有效号码或号码串]{style="font-family:宋体"}

[[+]{lang="EN-US"}]{#struct_0_48648_47840_x258088183}

[[指明符号前的字符串重复一次或多次。如：]{style="font-family:宋体"}[9876(54)+]{lang="EN-US"}]{#struct_0_48648_47840_x164784523}[可以匹配]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[%]{lang="EN-US"}]{#struct_0_48648_47840_1598050801}

[[指明符号前的字符串重复零次或多次。如：]{style="font-family:宋体"}[9876(54)%]{lang="EN-US"}]{#struct_0_48648_47840_1455511724}[可以匹配]{style="font-family:宋体"}[9876]{lang="EN-US"}[、]{style="font-family:宋体"}[987654]{lang="EN-US"}[、]{style="font-family:宋体"}[98765454]{lang="EN-US"}[、]{style="font-family:宋体"}[9876545454]{lang="EN-US"}[、......等号码]{style="font-family:宋体"}

[[-]{lang="EN-US"}]{#struct_0_48648_47840_1600630737}

[[连接符，用于连接两个数字（小的在前，大的在后），表示一个范围。如：]{style="font-family:宋体"}[\[1-9\]]{lang="EN-US"}]{#struct_0_48648_47840_220734374}[表示从]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:宋体"}[9]{lang="EN-US"}[（包括]{style="font-family:宋体"}[1]{lang="EN-US"}[和]{style="font-family:宋体"}[9]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_48648_47840_x1032216025}["只能出现在"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}["中，且连接两端只能为数字，如]{style="font-family:宋体"}[0-9]{lang="EN-US"}

[[\[ \]]{lang="EN-US"}]{#struct_0_48648_47840_x1478070565}

[[表示字符选择范围，如：]{style="font-family:宋体"}[\[1-36\]]{lang="EN-US"}]{#struct_0_48648_47840_x358264342}[表示只可匹配单个字符]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[6]{lang="EN-US"}[中的某一个]{style="font-family:宋体"}

[[符号"]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}]{#struct_0_48648_47840_877666167}["和"]{style="font-family:宋体"}[( )]{lang="EN-US"}["如果嵌套使用，则必须以"]{style="font-family:宋体"}[( \[ \] )]{lang="EN-US"}["形式出现，不允许其它形式，如"]{style="font-family:宋体"}[\[ \[ \] \]]{lang="EN-US"}["、"]{style="font-family:宋体"}[\[ ( ) \]]{lang="EN-US"}["等]{style="font-family:宋体"}

[[( )]{lang="EN-US"}]{#struct_0_48648_47840_x1521100341}

[[表示一组字符，如：]{style="font-family:宋体"}[(123)]{lang="EN-US"}]{#struct_0_48648_47840_1216100529}[表示字符串]{style="font-family:宋体"}[123]{lang="EN-US"}[，它一般与符号"]{style="font-family:宋体"}[!]{lang="EN-US"}["、"]{style="font-family:宋体"}[%]{lang="EN-US"}["、"]{style="font-family:宋体"}[+]{lang="EN-US"}["一起使用，如：]{style="font-family:宋体"}[408(12)+]{lang="EN-US"}[，可以匹配]{style="font-family:宋体"}[40812]{lang="EN-US"}[或]{style="font-family:宋体"}[408121212]{lang="EN-US"}[等字符串，但不能匹配]{style="font-family:宋体"}[408]{lang="EN-US"}[，即]{style="font-family:宋体"}[12]{lang="EN-US"}[可连续出现且至少出现一次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[**[7-24]{lang="EN-US"}**]{#struct_0_48648_47840_x22419438}[：表示]{style="font-family:宋体"}[1]{lang="EN-US"}[周]{style="font-family:宋体"}[7]{lang="EN-US"}[天，每天]{style="font-family:宋体"}[24]{lang="EN-US"}[小时呼叫都被阻塞。不指定该关键字将不开启全天候呼叫阻塞功能，用户可配合]{style="font-family:宋体"}**[after-hours day]{lang="EN-US"}**[和]{style="font-family:宋体"}**[after-hours date]{lang="EN-US"}**[命令按需配置特定时间的呼叫阻塞功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x822530463}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果被叫号码可以匹配多个]{lang="EN-US" style="font-family:宋体"}*[pattern]{lang="EN-US"}*]{#struct_0_48648_47840_x358264343}[（匹配阻塞的被叫号码模板），以]{lang="EN-US" style="font-family:宋体"}*[pattern-tag]{lang="EN-US"}*[最小的被叫号码模板为准。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在注册池下同时配置呼叫前转，呼叫阻塞的优先级高于呼叫前转功能。]{style="font-family:宋体"}]{#struct_0_48648_47840_877731703}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1615107574}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1490454107}[对被叫号码模板]{style="font-family:宋体"}[1000]{lang="EN-US"}[开启呼叫阻塞功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_310870754}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] after-hours block pattern 1 1000 7-24]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1813739872}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours date]{lang="EN-US"}**]{#struct_0_48648_47840_x1594346232}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours day]{lang="EN-US"}**]{#struct_0_48648_47840_1313586042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours exempt]{lang="EN-US"}**]{#struct_0_48648_47840_x1691554380}

::: {#-1719828089 .myid}
[]{#_Toc404794672}[]{#struct_0_48648_47840_2078508408}

**SRST \-- SRST业务配置命令 \-- after-hours date**

------------------------------------------------------------------------

[**[after-hours date]{lang="EN-US"}**]{#struct_0_48648_47840_191529937}[命令用来配置对每月的特定时间开启呼叫阻塞。]{style="font-family:宋体"}

[**[undo after-hours date]{lang="EN-US"}**]{#struct_0_48648_47840_x1946929755}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x358264344}

[**[after-hours date ]{lang="EN-US"}***[month date start-time stop-time]{lang="EN-US"}*]{#struct_0_48648_47840_878059383}

[**[undo after-hours ]{lang="EN-US"}[date ]{lang="EN-US"}***[month date]{lang="EN-US"}*]{#struct_0_48648_47840_1419516957}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1284575819}

[[没有对呼叫阻塞时间进行限定。]{style="font-family:宋体"}]{#struct_0_48648_47840_62252425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x326431630}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x806717964}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_1165446996}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x671281423}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_1045204287}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1733725788}

[*[month]{lang="EN-US"}*]{#struct_0_48648_47840_x358264345}[：]{style="font-family:宋体"}[指定的月份，取值为：]{style="font-family:宋体"}[January]{lang="EN-US"}[、]{style="font-family:宋体"}[February]{lang="EN-US"}[、]{style="font-family:宋体"}[March]{lang="EN-US"}[、]{style="font-family:宋体"}[April]{lang="EN-US"}[、]{style="font-family:宋体"}[May]{lang="EN-US"}[、]{style="font-family:宋体"}[June]{lang="EN-US"}[、]{style="font-family:宋体"}[July]{lang="EN-US"}[、]{style="font-family:宋体"}[August]{lang="EN-US"}[、]{style="font-family:宋体"}[September]{lang="EN-US"}[、]{style="font-family:宋体"}[October]{lang="EN-US"}[、]{style="font-family:宋体"}[November]{lang="EN-US"}[、]{style="font-family:宋体"}[December]{lang="EN-US"}[。]{style="font-family:宋体"}[最少输入月份拼写的前三个字符，例如]{style="font-family:宋体"}[Jan]{lang="EN-US"}[，不区分大小写。]{style="font-family:宋体"}

[*[date]{lang="EN-US"}*]{#struct_0_48648_47840_878124919}[：日期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[start-time]{lang="EN-US"}*]{#struct_0_48648_47840_x2117967610}[：呼叫阻塞的起始时间，格式是]{style="font-family:宋体"}[HH:MM]{lang="EN-US"}[，且使用]{style="font-family:宋体"}[24]{lang="EN-US"}[小时制。]{style="font-family:宋体"}[24:00]{lang="EN-US"}[是无效值。]{style="font-family:宋体"}

[*[stop-time]{lang="EN-US"}*]{#struct_0_48648_47840_x30361787}[：呼叫阻塞的结束时间，格式与]{style="font-family:宋体"}*[start-time]{lang="EN-US"}*[相同。]{style="font-family:宋体"}[24:00]{lang="EN-US"}[是无效值。如果将]{style="font-family:宋体"}[00:00]{lang="EN-US"}[作为]{style="font-family:宋体"}*[stop-time]{lang="EN-US"}*[，则会自动被修改成]{style="font-family:宋体"}[23:59]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1784131722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_48648_47840_253356870}*[start-time]{lang="EN-US"}*[和]{style="font-family:宋体"}*[stop-time]{lang="EN-US"}*[都是]{style="font-family:宋体"}[00:00]{lang="EN-US"}[，那么在指定的这一天，呼叫将会被阻塞]{style="font-family:宋体"}[24]{lang="EN-US"}[小时。如果结束时间小于起始时间，代表呼叫阻塞从当天的起始时间开始一直持续到后一天的结束时间。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果还配置了]{lang="EN-US" style="font-family:宋体"}**[after-hours day]{lang="EN-US"}**]{#struct_0_48648_47840_x557535852}[命令，那么实际阻塞时间为这两条命令的合集。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_2053614437}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x317372827}[配置从]{style="font-family:宋体"}[4]{lang="EN-US"}[月]{style="font-family:宋体"}[1]{lang="EN-US"}[日上午]{style="font-family:
宋体"}[8]{lang="EN-US"}[点到晚上]{style="font-family:宋体"}[8]{lang="EN-US"}[点开启呼叫阻塞。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1936791288}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] after-hours date apr 1 08:00 20:00]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1614634075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours block]{lang="EN-US"}**]{#struct_0_48648_47840_x1100884151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours day]{lang="EN-US"}**]{#struct_0_48648_47840_x358264338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours exempt]{lang="EN-US"}**]{#struct_0_48648_47840_877272952}
:::

::: {#-89287256 .myid}
[]{#_Toc404794673}[]{#struct_0_48648_47840_x1977273065}

**SRST \-- SRST业务配置命令 \-- after-hours day**

------------------------------------------------------------------------

[**[after-hours day]{lang="EN-US"}**]{#struct_0_48648_47840_x1608962186}[命令用来配置对每周的特定时间开启呼叫阻塞。]{style="font-family:宋体"}

[**[undo after-hours day]{lang="EN-US"}**]{#struct_0_48648_47840_304509148}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x610226185}

[**[after-hours day ]{lang="EN-US"}***[day start-time stop-time]{lang="EN-US"}*]{#struct_0_48648_47840_x459228376}

[**[undo after-hours day ]{lang="EN-US"}***[day]{lang="EN-US"}*]{#struct_0_48648_47840_489264824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x198402156}

[[没有对呼叫阻塞时间进行限定。]{style="font-family:宋体"}]{#struct_0_48648_47840_1385381106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x945820624}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1646203348}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x742338688}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1516587556}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1251432435}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x358264339}

[*[day]{lang="EN-US"}*]{#struct_0_48648_47840_877338488}[：]{style="font-family:宋体"}[指定的一周中的一天，取值为：]{style="font-family:宋体"}[Sunday]{lang="EN-US"}[、]{style="font-family:宋体"}[Monday]{lang="EN-US"}[、]{style="font-family:宋体"}[Tuesday]{lang="EN-US"}[、]{style="font-family:宋体"}[Wednesday]{lang="EN-US"}[、]{style="font-family:宋体"}[Thursday]{lang="EN-US"}[、]{style="font-family:宋体"}[Friday]{lang="EN-US"}[、]{style="font-family:宋体"}[Saturday]{lang="EN-US"}[。]{style="font-family:宋体"}[最少输入英文拼写的前三个字符，例如]{style="font-family:宋体"}[Sat]{lang="EN-US"}[，不区分大小写]{style="font-family:宋体"}[。]{style="font-size:12.0pt;font-family:宋体"}

[*[start-time]{lang="EN-US"}*]{#struct_0_48648_47840_1135747428}[：呼叫阻塞的起始时间，格式是]{style="font-family:宋体"}[HH:MM]{lang="EN-US"}[，使用的是]{style="font-family:宋体"}[24]{lang="EN-US"}[小时制。]{style="font-family:宋体"}[24:00]{lang="EN-US"}[是无效值。]{style="font-family:宋体"}

[*[stop-time]{lang="EN-US"}*]{#struct_0_48648_47840_x1549158677}[：呼叫阻塞的结束时间，格式与]{style="font-family:宋体"}*[start-time]{lang="EN-US"}*[相同。]{style="font-family:宋体"}[24:00]{lang="EN-US"}[是无效值。如果将]{style="font-family:宋体"}[00:00]{lang="EN-US"}[作为]{style="font-family:宋体"}*[stop-time]{lang="EN-US"}*[，则会自动被修改成]{style="font-family:宋体"}[23:59]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x530815487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_48648_47840_x1549820905}*[start-time]{lang="EN-US"}*[和]{style="font-family:宋体"}*[stop-time]{lang="EN-US"}*[都是]{style="font-family:宋体"}[00:00]{lang="EN-US"}[，那么在指定的这一天，呼叫将会被阻塞]{style="font-family:宋体"}[24]{lang="EN-US"}[小时。如果结束时间小于起始时间，代表呼叫阻塞从当天的起始时间开始一直持续到后一天的结束时间。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果还配置了]{lang="EN-US" style="font-family:宋体"}**[after-hours date]{lang="EN-US"}**]{#struct_0_48648_47840_x235340775}[命令，那么实际阻塞时间为这两条命令的合集。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_452387385}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_2098756416}[配置对每周一的上午]{style="font-family:宋体"}[8]{lang="EN-US"}[点到晚上]{style="font-family:宋体"}[8]{lang="EN-US"}[点开启呼叫阻塞。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_807023938}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] after-hours day mon 08:00 20:00]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1222560409}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours block]{lang="EN-US"}**]{#struct_0_48648_47840_1328663786}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours date]{lang="EN-US"}**]{#struct_0_48648_47840_1013944695}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours exempt]{lang="EN-US"}**]{#struct_0_48648_47840_x358264340}
:::

::: {#1780939059 .myid}
[]{#_Toc404794674}[]{#struct_0_48648_47840_877797239}

**SRST \-- SRST业务配置命令 \-- after-hours exempt**

------------------------------------------------------------------------

[**[after-hours]{lang="EN-US"}**[ **exempt**]{lang="EN-US"}]{#struct_0_48648_47840_x715573019}[命令用来免除呼叫阻塞。]{style="font-family:宋体"}

[**[undo after-hours]{lang="EN-US"}**]{#struct_0_48648_47840_1825535147}[命令用来取消免除呼叫阻塞。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x945891992}

[**[after-hours exempt]{lang="EN-US"}**]{#struct_0_48648_47840_x624523660}

[**[undo after-hours]{lang="EN-US"}**]{#struct_0_48648_47840_x737059057}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x960491032}

[[没有配置免除呼叫阻塞。]{style="font-family:宋体"}]{#struct_0_48648_47840_1641584096}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1191342285}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_x1197314158}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[注册池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1609209105}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x2023085844}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x358264341}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_877862775}

[[配置]{style="font-family:宋体"}**[after-hours exempt]{lang="EN-US"}**]{#struct_0_48648_47840_x1676307089}[命令后，]{style="font-family:宋体"}[DN]{lang="EN-US"}[或注]{style="font-family:宋体"}[册池下的号码可以免除呼叫阻塞的作用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_22744917}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_31961170}[对号码]{style="font-family:宋体"}[1000]{lang="EN-US"}[免除呼叫阻塞。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_2141109578}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 1]{lang="EN-US"}

[\[Sysname-voice-register-dn1\] after-hours exempt]{lang="EN-US"}

[\[Sysname-voice-register-dn1\] number 1000\$]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x554610592}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours block]{lang="EN-US"}**]{#struct_0_48648_47840_x963710253}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours day]{lang="EN-US"}**]{#struct_0_48648_47840_x435216028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[after-hours date]{lang="EN-US"}**]{#struct_0_48648_47840_344914105}
:::

::: {#1707272077 .myid}
[]{#_Toc404794675}[]{#struct_0_48648_47840_x770723883}

**SRST \-- SRST业务配置命令 \-- call-forward b2bua**

------------------------------------------------------------------------

[**[call-forward b2bua]{lang="EN-US"}**]{#struct_0_48648_47840_x358264334}[命令用来开启呼叫前转功能。]{style="font-family:宋体"}

[**[undo call-forward b2bua]{lang="EN-US"}**]{#struct_0_48648_47840_878059384}[命令用来关闭呼叫前转功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1419516950}

[[注册池视图下：]{style="font-family:宋体"}]{#struct_0_48648_47840_x198301509}

[**[call-forward b2bua ]{lang="EN-US"}**[{ **all** ]{lang="EN-US"}*[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **busy** ]{lang="EN-US"}*[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **noan** ]{lang="EN-US"}*[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **timeout** ]{lang="EN-US"}*[seconds]{lang="EN-US"}*[ \] }]{lang="EN-US"}]{#struct_0_48648_47840_x1285034571}

[**[undo call-forward b2bua ]{lang="EN-US"}**[{ **all** \| **busy** \| **noan** }]{lang="EN-US"}]{#struct_0_48648_47840_x709468037}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_x945966807}[视图下：]{style="font-family:宋体"}

[**[call-forward b2bua ]{lang="EN-US"}**[{ **all** ]{lang="EN-US"}*[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **busy** ]{lang="EN-US"}*[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **noan** ]{lang="EN-US"}*[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **timeout** ]{lang="EN-US"}*[seconds]{lang="EN-US"}*[ \] \| **unregistered** ]{lang="EN-US"}*[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[}]{lang="EN-US"}]{#struct_0_48648_47840_x231516655}

[**[undo call-forward b2bua ]{lang="EN-US"}**[{ **all** \| **busy** \| **noan** \| **unregistered** }]{lang="EN-US"}]{#struct_0_48648_47840_x429393597}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1338611260}

[[呼叫前转功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1592483784}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1614704555}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_1957308553}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[注册池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x680277495}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_423338513}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1733379857}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x358264335}

[**[all]{lang="EN-US" style="color:windowtext"}**]{#struct_0_48648_47840_878124920}[：配置无条件呼叫前转。]{style="font-family:宋体;color:windowtext"}

[**[busy]{lang="EN-US" style="color:windowtext"}**]{#struct_0_48648_47840_603021567}[：配置遇忙呼叫前转。]{style="font-family:宋体;color:windowtext"}

[**[noan]{lang="EN-US" style="color:windowtext"}**]{#struct_0_48648_47840_x1431326640}[：配置无应答呼叫前转。]{style="font-family:宋体;color:windowtext"}

[**[unregistered]{lang="EN-US" style="color:windowtext"}**]{#struct_0_48648_47840_x1472550016}[：配置未注册呼叫前转。]{style="font-family:宋体;color:windowtext"}

[**[timeout]{lang="EN-US" style="color:windowtext"}**]{#struct_0_48648_47840_1507033893}[：指定无应答呼叫前转超时时间。]{style="font-family:宋体;color:windowtext"}

[*[number]{lang="EN-US" style="color:windowtext"}*]{#struct_0_48648_47840_x655118521}[：呼叫前转的目的号码，为]{style="font-family:宋体;color:windowtext"}[1]{lang="EN-US" style="color:windowtext"}[～]{style="font-family:宋体;color:windowtext"}[31]{lang="EN-US" style="color:windowtext"}[个字符的字符串，取值范围为数字]{style="font-family:宋体;
color:windowtext"}[0]{lang="EN-US" style="color:windowtext"}[～]{style="font-family:宋体;color:windowtext"}[9]{lang="EN-US" style="color:windowtext"}[。]{style="font-family:宋体;color:windowtext"}

[*[seconds]{lang="EN-US" style="color:windowtext"}*]{#struct_0_48648_47840_x134506785}[：无应答超时时间，取值范围为]{style="font-family:宋体;color:windowtext"}[2]{lang="EN-US" style="color:windowtext"}[～]{style="font-family:宋体;color:windowtext"}[120]{lang="EN-US" style="color:windowtext"}[，单位为秒。该时间超时后，触发无应答呼叫前转。缺省值为]{style="font-family:宋体;
color:windowtext"}[20]{lang="EN-US" style="color:windowtext"}[秒。]{style="font-family:宋体;color:windowtext"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1934493370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[all]{lang="EN-US"}**]{#struct_0_48648_47840_1527363396}[、]{lang="EN-US" style="font-family:宋体"}**[busy]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[noan]{lang="EN-US"}**[参数]{lang="EN-US" style="font-family:宋体"}[可以在]{lang="EN-US" style="font-family:
宋体"}[注册池]{style="font-family:宋体"}[、]{lang="EN-US" style="font-family:宋体"}[DN]{lang="EN-US"}[视图下配置，]{lang="EN-US" style="font-family:宋体"}**[unregistered]{lang="EN-US"}**[参数只能在]{lang="EN-US" style="font-family:宋体"}[DN]{lang="EN-US"}[视图下配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[语音服务器支持无条件、遇忙、无应答和未注册四种呼叫前转，按优先级从高到低依次是：无条件前转、遇忙前转、无应答前转。未注册前转不会和其他三种前转出现在同一动态]{style="font-family:宋体"}]{#struct_0_48648_47840_1447858634}[VoIP]{lang="EN-US"}[语音实体中，其优先级与其他三种没有可比性。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[实际应用时，为了保证该功能能够正常使用，请用户合理、有效地规划前转目的号码，避免出现错号、循环呼叫。]{style="font-family:宋体"}]{#struct_0_48648_47840_x592648281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免循环前转，目前一个呼叫最多可以前转]{style="font-family:宋体"}]{#struct_0_48648_47840_831214058}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在注册池下同时配置]{style="font-family:宋体"}]{#struct_0_48648_47840_x2041700651}[DND]{lang="EN-US"}[，]{style="font-family:宋体"}[DND]{lang="EN-US"}[的优先级高于呼叫前转功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在注册池下同时配置呼叫阻塞，呼叫阻塞的优先级高于呼叫前转功能。]{style="font-family:宋体"}]{#struct_0_48648_47840_1739729263}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_28919024}

[[\# ]{lang="DA"}]{#struct_0_48648_47840_1782013776}[配置]{style="font-family:宋体"}[遇忙]{style="font-family:宋体"}[呼叫前转功能，当有电话呼叫号码]{style="font-family:宋体"}[5000]{lang="DA"}[时，如果号码]{style="font-family:宋体"}[5000]{lang="DA"}[处于通话状态，该路呼叫会被前转到目的号码]{style="font-family:宋体"}[8000]{lang="DA"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_859767517}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 3]{lang="EN-US"}

[\[Sysname-voice-register-dn3\] number 5000]{lang="EN-US"}

[\[Sysname-voice-register-dn3\] call-forward b2bua busy 8000]{lang="EN-US"}

[[\# ]{lang="DA"}]{#struct_0_48648_47840_1670565853}[配置]{style="font-family:宋体"}[未注册呼叫前转]{style="font-family:宋体"}[功能，当有电话呼叫号码]{style="font-family:宋体"}[3000]{lang="DA"}[时，如果号码]{style="font-family:宋体"}[3000]{lang="DA"}[没有应用到注册池，即生成号码]{style="font-family:宋体"}[3000]{lang="DA"}[的未注册动态]{style="font-family:宋体"}[VoIP]{lang="DA"}[语音实体，该路呼叫会被前转到目的号码]{style="font-family:宋体"}[2000]{lang="DA"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_1858441775}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 3]{lang="EN-US"}

[\[Sysname-voice-register-dn3\] number 3000]{lang="EN-US"}

[\[Sysname-voice-register-dn3\] call-forward unregistered 2000]{lang="EN-US"}
:::

::::: {#663908461 .myid}
[]{#_Toc404794676}[]{#struct_0_48648_47840_546615279}

**SRST \-- SRST业务配置命令 \-- display voice fac**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **voice** **fac**]{lang="EN-US"}]{#struct_0_48648_47840_x513397784}[命令用来显示配置的]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_831214057}

[**[display voice fac]{lang="EN-US"}**]{#struct_0_48648_47840_x2041700654}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_2143013790}

[[任意视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x664681805}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x109472224}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_638781486}

[[network-operator]{lang="EN-US"}]{#struct_0_48648_47840_x1496699553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1950539044}

[[mdc-operator]{lang="EN-US"}]{#struct_0_48648_47840_2127530096}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_547891065}

[[设备作为语音服务器或网关模式下都可以使用该命令查看配置的]{style="font-family:宋体"}[FACs]{lang="EN-US"}]{#struct_0_48648_47840_x120511751}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1418431015}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_2143691343}[显示网关模式下标准的]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display voice fac]{lang="EN-US"}]{#struct_0_48648_47840_831214056}

[Standard FACs enabled in gateway mode]{lang="EN-US"}

[  callfwd all \*57\*]{lang="EN-US"}

[  callfwd all cancel #57#]{lang="EN-US"}

[  callfwd busy \*40\*]{lang="EN-US"}

[  callfwd busy cancel #40#]{lang="EN-US"}

[  callfwd noan \*41\*]{lang="EN-US"}

[  callfwd noan cancel #41#]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x2041700653}[显示语音服务器模式下标准的]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display voice fac]{lang="EN-US"}]{#struct_0_48648_47840_x1392438619}

[Standard FACs enabled in server mode]{lang="EN-US"}

[  pickup direct \*80\*]{lang="EN-US"}

[  pickup local \*81\*]{lang="EN-US"}

[  pickup group \*82\*]{lang="EN-US"}

[  callfwd all \*57\*]{lang="EN-US"}

[  callfwd all cancel #57#]{lang="EN-US"}

[  callfwd busy \*40\*]{lang="EN-US"}

[  callfwd busy cancel #40#]{lang="EN-US"}

[  callfwd noan \*41\*]{lang="EN-US"}

[  callfwd noan cancel #41#]{lang="EN-US"}

[  callfwd unregistered \*44\*]{lang="EN-US"}

[  callfwd unregistered cancel #44#]{lang="EN-US"}

[  dnd \*70\*]{lang="EN-US"}

[  dnd cancel #70#]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SRST命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_48648_47840_916834948}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[设备作为语音服务器时，]{lang="EN-US" style="font-family:楷体_GB2312"}**[display voice fac]{lang="EN-US"}**]{#struct_0_48648_47840_831214055}[命令显示信息中会存在拨号结束符的配置信息，但该配置并不生效。]{lang="EN-US" style="font-family:
楷体_GB2312"}
:::

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display voice fac]{lang="EN-US"}]{#struct_0_48648_47840_561213378}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x588186451}[[字段]{style="font-family:黑体"}]{#struct_0_48648_47840_x1004870563}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_48648_47840_1724012792}

[[Custom]{lang="EN-US"}]{#struct_0_48648_47840_x554531869}

[[自定义的]{style="font-family:宋体"}[FACs]{lang="EN-US"}]{#struct_0_48648_47840_x198367045}

[[Standard]{lang="EN-US"}]{#struct_0_48648_47840_x1764450986}

[[标准的]{style="font-family:宋体"}[FACs]{lang="EN-US"}]{#struct_0_48648_47840_964432369}

[[gateway mode]{lang="EN-US"}]{#struct_0_48648_47840_x601651572}

[[FACs]{lang="EN-US"}]{#struct_0_48648_47840_561147842}[工作在网关模式]{style="font-family:宋体"}

[[server mode]{lang="EN-US"}]{#struct_0_48648_47840_x1004936099}

[[FACs]{lang="EN-US"}]{#struct_0_48648_47840_1723947256}[工作在语音服务器模式]{style="font-family:宋体"}

[[fac terminator]{lang="EN-US"}]{#struct_0_48648_47840_x2120681346}

[[FACs]{lang="EN-US"}]{#struct_0_48648_47840_x198432581}[结尾符]{style="font-family:宋体"}

[[callfwd]{lang="EN-US"}]{#struct_0_48648_47840_x1764516522}

[[呼叫前转，取值包括：]{style="font-family:宋体"}]{#struct_0_48648_47840_x601717108}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[all]{lang="EN-US"}]{#struct_0_48648_47840_2127166247}[：无条件呼叫前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[all-cancel]{lang="EN-US"}]{#struct_0_48648_47840_561082306}[：取消无条件前转]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[busy]{lang="EN-US"}]{#struct_0_48648_47840_x1005001635}[：遇忙前转]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[busy-cancel]{lang="EN-US"}]{#struct_0_48648_47840_x554662941}[：取消遇忙前转]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[noan]{lang="EN-US"}]{#struct_0_48648_47840_x2120746882}[：无应答前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[noan-cancel]{lang="EN-US"}]{#struct_0_48648_47840_x198498117}[：取消无应答前转]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unregistered]{lang="EN-US"}]{#struct_0_48648_47840_964301297}[：未注册前转]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unregistered-cancel]{lang="EN-US"}]{#struct_0_48648_47840_x601782644}[：取消未注册前转]{lang="EN-US" style="font-family:
  宋体"}[FACs]{lang="EN-US"}

[[dnd]{lang="EN-US"}]{#struct_0_48648_47840_561016770}

[[免打扰功能]{style="font-family:宋体"}]{#struct_0_48648_47840_x1005067171}

[[pickup]{lang="EN-US"}]{#struct_0_48648_47840_1723816184}

[[呼叫代答]{style="font-family:宋体"}[FACs]{lang="EN-US"}]{#struct_0_48648_47840_x2120812418}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[direct]{lang="EN-US"}]{#struct_0_48648_47840_x198563653}[：直接呼叫代答]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[group]{lang="EN-US"}]{#struct_0_48648_47840_x1764647594}[：组间呼叫代答]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_48648_47840_x601848180}[：组内呼叫代答]{lang="EN-US" style="font-family:宋体"}[FACs]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1028830030 .myid}
[]{#_Toc404794677}[]{#struct_0_48648_47840_x2041700656}

**SRST \-- SRST业务配置命令 \-- dnd**

------------------------------------------------------------------------

[**[dnd]{lang="EN-US"}**]{#struct_0_48648_47840_x989154092}[命令用来开启]{style="font-family:宋体"}[DND]{lang="EN-US"}[（]{style="font-family:宋体"}[Do-not Disturb]{lang="EN-US"}[，免打扰）功能。]{style="font-family:宋体"}

[**[undo dnd]{lang="EN-US"}**]{#struct_0_48648_47840_x1788864820}[命令用来关闭]{style="font-family:宋体"}[DND]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_467910110}

[**[dnd]{lang="EN-US"}**]{#struct_0_48648_47840_893037319}

[**[undo dnd]{lang="EN-US"}**]{#struct_0_48648_47840_1531093927}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x395933257}

[[DND]{lang="EN-US"}]{#struct_0_48648_47840_759548086}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1707721156}

[[注册池视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x2100942904}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_1776523417}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x728651523}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_831214062}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_296951503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启]{style="font-family:宋体"}]{#struct_0_48648_47840_1839173234}[DND]{lang="EN-US"}[功能，对注册池下的号码实现禁止入呼叫，即这些号码作为被叫接受呼叫时，会回复用户忙。但是这些号码向外发起呼叫是不受限的。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在注册池下同时配置呼叫前转，]{style="font-family:宋体"}]{#struct_0_48648_47840_1968540054}[DND]{lang="EN-US"}[的优先级高于呼叫前转功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_287855398}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x187982532}[为注册池]{style="font-family:宋体"}[1]{lang="EN-US"}[开启]{style="font-family:宋体"}[DND]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x897229800}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register pool 1]{lang="EN-US"}

[\[Sysname-voice-register-pool1\] dnd]{lang="EN-US"}
:::

::: {#-1515042309 .myid}
[]{#_Toc404794678}[]{#struct_0_48648_47840_x459535344}

**SRST \-- SRST业务配置命令 \-- fac custom**

------------------------------------------------------------------------

[**[fac]{lang="EN-US"}**[ **custom**]{lang="EN-US"}]{#struct_0_48648_47840_x628642969}[命令用来配置自定义]{style="font-family:宋体"}[FACs]{lang="EN-US"}[（]{style="font-family:宋体"}[Feature Access Codes]{lang="EN-US"}[，业务特征码）功能。]{style="font-family:宋体"}

[**[undo fac]{lang="EN-US"}**[ **custom**]{lang="EN-US"}]{#struct_0_48648_47840_889318097}[命令用来关闭]{style="font-family:宋体"}[FACs]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1012429402}

[**[fac]{lang="EN-US"}**[ **custom** { **alias ** *id* *custom-string* **to** *existing-string* \| **callfwd** { **all** \| **all-cancel** \| **busy** \| **busy-cancel** \| **noan** \| **noan-cancel** \| **unregistered** \| **unregistered-cancel** } *string* \| **dnd** \[ **cancel** \] *string* \| **pickup** { **direct** \| **group** \| **local** } *string* }]{lang="EN-US"}]{#struct_0_48648_47840_831214061}

[**[undo]{lang="EN-US"}**[ **fac** **custom** { **alias ** *id* \| **callfwd** { **all** \| **all-cancel** \| **busy** \| **busy-cancel** \| **noan** \| **noan-cancel** \| **unregistered** \| **unregistered-cancel** } \| **dnd** \| **pickup** { **direct** \| **group** \| **local** } }]{lang="EN-US"}]{#struct_0_48648_47840_296951500}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1839173237}

[[FACs]{lang="EN-US"}]{#struct_0_48648_47840_1968474518}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x101440077}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_19788135}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_927177181}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_584244756}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_462089301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1677558972}

[**[alias ]{lang="EN-US"}***[id]{lang="EN-US"}*]{#struct_0_48648_47840_1805968377}[：自定义]{style="font-family:宋体"}[FACs]{lang="EN-US"}[的标记，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:
宋体"}

[*[custom-string]{lang="EN-US"}*]{#struct_0_48648_47840_x341588066}[：自定义新]{style="font-family:宋体"}[FACs]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[和]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[existing-string]{lang="EN-US"}*]{#struct_0_48648_47840_x339298807}[：已有的]{style="font-family:宋体"}[FACs]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[和]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pickup]{lang="EN-US"}**]{#struct_0_48648_47840_831214060}[：自定义呼叫代答]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[direct]{lang="EN-US"}**]{#struct_0_48648_47840_296951501}[：自定义直接呼叫代答]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**]{#struct_0_48648_47840_1839173236}[：自定义组间呼叫代答]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_48648_47840_1968408982}[：自定义组内呼叫代答]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dnd]{lang="EN-US"}**]{#struct_0_48648_47840_x488657288}[：自定义]{style="font-family:宋体"}[DND]{lang="EN-US"}[的]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cancel]{lang="EN-US"}**]{#struct_0_48648_47840_x1949785339}[：取消自定义]{style="font-family:宋体"}[DND]{lang="EN-US"}[的]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[callfwd]{lang="EN-US"}**]{#struct_0_48648_47840_2097545173}[：自定义呼叫前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_48648_47840_x2145670623}[：自定义无条件呼叫前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all-cancel]{lang="EN-US"}**]{#struct_0_48648_47840_x926713861}[：取消自定义无条件前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[busy]{lang="EN-US"}**]{#struct_0_48648_47840_x1669439670}[：自定义遇忙前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[busy-cancel]{lang="EN-US"}**]{#struct_0_48648_47840_x32407968}[：取消自定义遇忙前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[noan]{lang="EN-US"}**]{#struct_0_48648_47840_x1473242657}[：自定义无应答前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[noan-cancel]{lang="EN-US"}**]{#struct_0_48648_47840_1814219084}[：取消自定义无应答前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[unregistered]{lang="EN-US"}**]{#struct_0_48648_47840_831214059}[：自定义未注册前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[unregistered-cancel]{lang="EN-US"}**]{#struct_0_48648_47840_x2041700652}[：取消自定义未注册前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_48648_47840_1336444736}[：自定义特征码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、]{style="font-family:
宋体"}[\*]{lang="EN-US"}[和]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_2095596076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令不能和]{lang="EN-US" style="font-family:宋体"}**[fac standard]{lang="EN-US"}**]{#struct_0_48648_47840_1480668550}[命令同时配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备作为网关或语音服务器时，均可以使用自定义]{style="font-family:宋体"}]{#struct_0_48648_47840_x1349594541}[FACs]{lang="EN-US"}[。需要注意的是，设备作为网关时，只支持呼叫前转（不包括未注册和不可用呼叫前转）]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置自定义]{style="font-family:宋体"}]{#struct_0_48648_47840_x1951096760}[FACs]{lang="EN-US"}[时，建议不要将不同业务配置共用一个]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x987813034}

[[\# ]{lang="DA"}]{#struct_0_48648_47840_1155190996}[配置自定义无条件呼叫前转]{style="font-family:宋体"}[FACs]{lang="EN-US"}[为]{style="font-family:宋体"}[1234]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_1707353323}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] fac custom callfwd all 1234]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_831214066}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fac standard]{lang="EN-US"}**]{#struct_0_48648_47840_296951507}
:::

::: {#960245182 .myid}
[]{#_Toc404794679}[]{#struct_0_48648_47840_1839173238}

**SRST \-- SRST业务配置命令 \-- fac standard**

------------------------------------------------------------------------

[**[fac]{lang="EN-US"}**[ **standard**]{lang="EN-US"}]{#struct_0_48648_47840_1968277910}[命令用来配置标准]{style="font-family:宋体"}[FACs]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo fac]{lang="EN-US"}**[ **standard**]{lang="EN-US"}]{#struct_0_48648_47840_1789822026}[命令用来关闭标准]{style="font-family:宋体"}[FACs]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1905750731}

[**[fac]{lang="EN-US"}**[ **standard**]{lang="EN-US"}]{#struct_0_48648_47840_x778236176}

[**[undo]{lang="EN-US"}**[ **fac** **standard**]{lang="EN-US"}]{#struct_0_48648_47840_x2098217607}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1145931465}

[[FACs]{lang="EN-US"}]{#struct_0_48648_47840_x803555508}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_185546826}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x1557345949}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x640005710}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_56603289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_831214065}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_296951504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令不能和]{lang="EN-US" style="font-family:宋体"}**[fac custom]{lang="EN-US"}**]{#struct_0_48648_47840_1839173241}[命令同时配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备作为网关或语音服务器时，均可以使用标准]{style="font-family:宋体"}]{#struct_0_48648_47840_1968867739}[FACs]{lang="EN-US"}[。需要注意的是，设备作为网关时，只支持呼叫前转（不包括未注册和不可用呼叫前转）]{style="font-family:宋体"}[FACs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x890076414}

[[\# ]{lang="DA"}]{#struct_0_48648_47840_x93450634}[配置标准]{style="font-family:宋体"}[FACs]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_2094070082}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] fac standard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x461812700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fac custom]{lang="EN-US"}**]{#struct_0_48648_47840_1840843518}
:::

::: {#-1542520650 .myid}
[]{#_Toc404794680}[]{#struct_0_48648_47840_x1776628174}

**SRST \-- SRST业务配置命令 \-- fac terminator**

------------------------------------------------------------------------

[**[fac]{lang="EN-US"}**[ **terminator**]{lang="EN-US"}]{#struct_0_48648_47840_1703511478}[命令用来配置匹配]{style="font-family:宋体"}[FACs]{lang="EN-US"}[的结尾符。]{style="font-family:宋体"}

[**[undo fac]{lang="EN-US"}**[ **terminator**]{lang="EN-US"}]{#struct_0_48648_47840_x938895394}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x915301353}

[**[fac]{lang="EN-US"}**[ **terminator** *character*]{lang="EN-US"}]{#struct_0_48648_47840_1973444006}

[**[undo]{lang="EN-US"}**[ **fac** **terminator**]{lang="EN-US"}]{#struct_0_48648_47840_x1125101078}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_163204071}

[[匹配]{style="font-family:宋体"}[FACs]{lang="EN-US"}]{#struct_0_48648_47840_x2017389285}[的结尾符为]{style="font-family:宋体"}[\#]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x893544567}

[[语音视图]{style="font-family:宋体"}]{#struct_0_48648_47840_1309603956}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_2044636936}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_1035107316}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_242857772}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1245728027}

[*[character]{lang="EN-US"}*]{#struct_0_48648_47840_923337767}[：结尾符，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[、"]{style="font-family:宋体"}[\#]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US" style="font-family:宋体"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x2129406604}

[[该命令仅在设备作为网关模式，并且配置使用自定]{style="font-family:宋体"}]{#struct_0_48648_47840_x2052532959}[义]{style="font-family:
宋体"}[FACs]{lang="EN-US"}[时才]{style="font-family:宋体"}[能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x944283259}

[[\# ]{lang="DA"}]{#struct_0_48648_47840_911711244}[配置匹配]{style="font-family:宋体"}[FACs]{lang="EN-US"}[的结尾符为]{style="font-family:宋体"}[\*]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1125101079}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] fac terminator ]{lang="EN-US"}[\*]{lang="EN-US" style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1402879870}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fac custom]{lang="EN-US"}**]{#struct_0_48648_47840_x1653753298}
:::

::: {#257141939 .myid}
[]{#_Toc404794681}[]{#struct_0_48648_47840_1694801680}[]{#_Toc388276774}[]{#_Toc388276821}[]{#_Toc389573631}

**SRST \-- SRST业务配置命令 \-- moh file**

------------------------------------------------------------------------

[**[moh file]{lang="EN-US"}**]{#struct_0_48648_47840_1073537809}[命令用来配置音乐保持媒体资源文件。]{style="font-family:宋体"}

[**[undo moh file]{lang="EN-US"}**]{#struct_0_48648_47840_186678123}[命令用来取消已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1256929271}

[**[moh file ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_48648_47840_1550427829}

[**[undo moh file]{lang="EN-US"}**]{#struct_0_48648_47840_545780817}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x489834630}

[[不存在音乐保持媒体资源文件。]{style="font-family:宋体"}]{#struct_0_48648_47840_1550653403}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1125101080}

[[全局注册视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x193878257}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x889945652}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_765168723}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1010771414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_301575880}

[*[filename]{lang="EN-US"}*]{#struct_0_48648_47840_895328670}[：]{style="font-family:宋体;color:black"}[媒体资源文件名]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_402031418}

[[呼叫被保持方可使用组播或单播方式接收]{style="font-family:宋体"}]{#struct_0_48648_47840_x815707046}[音乐保持媒体流]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置使用单播方式接收]{lang="EN-US" style="font-family:宋体"}]{#struct_0_48648_47840_1007568727}[音乐保持媒体流时，需要使用]{lang="EN-US" style="font-family:宋体"}**[call-hold-format sendonly]{lang="EN-US"}**[命令将]{lang="EN-US" style="font-family:宋体"}[呼叫保持的模式配置为放音模式]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置使用组播方式接收]{lang="EN-US" style="font-family:宋体"}]{#struct_0_48648_47840_x2100705251}[音乐保持媒体流时，需要使用]{lang="EN-US" style="font-family:宋体"}**[multicast]{lang="EN-US"}**[ **moh** **ip**]{lang="EN-US"}[命令配置提供音乐保持媒体流的组播地址。]{lang="EN-US" style="font-family:
宋体"}

[[目前只支持]{style="font-family:宋体"}[G.711u]{lang="EN-US"}]{#struct_0_48648_47840_x1403315481}[和]{style="font-family:宋体"}[G.711a]{lang="EN-US"}[编解码的]{style="font-family:宋体"}[wav]{lang="EN-US"}[文件作为音乐保持媒体资源文件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x292856072}

[[\# ]{lang="DA"}]{#struct_0_48648_47840_x1125101081}[配置音乐保持媒体资源文件为]{style="font-family:宋体"}[cfa0:/g711u/moh.wav]{lang="DA"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1759962198}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\] moh file cfa0:/g711u/moh.wav]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_42719019}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[call-hold-format]{lang="EN-US"}**]{#struct_0_48648_47840_x2013155325}[（语音命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[语音业务）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast]{lang="EN-US"}**[ **moh** **ip**]{lang="EN-US"}]{#struct_0_48648_47840_x935644189}
:::

::: {#-647603447 .myid}
[]{#_Toc404794682}[]{#struct_0_48648_47840_1705119857}

**SRST \-- SRST业务配置命令 \-- multicast moh**

------------------------------------------------------------------------

[**[multicast]{lang="EN-US"}**[ **moh**]{lang="EN-US"}]{#struct_0_48648_47840_1685601600}[命令用来配置提供音乐保持媒体流的组播地址。]{style="font-family:宋体"}

[**[undo multicast moh ip]{lang="EN-US"}**]{#struct_0_48648_47840_x1813910582}[命令用来删除已有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1790765852}

[**[multicast]{lang="EN-US"}**[ **moh** **ip** *multicast-address* **port** *port-number* **route** *address-list*&\<1-5\>]{lang="EN-US"}]{#struct_0_48648_47840_x452144336}

[**[undo multicast]{lang="EN-US"}**[ **moh** **ip**]{lang="EN-US"}]{#struct_0_48648_47840_580329369}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1322148204}

[[不存在提供音乐保持媒体流的组播地址。]{style="font-family:宋体"}]{#struct_0_48648_47840_x1476082968}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1211813811}

[[全局注册视图]{style="font-family:宋体"}]{#struct_0_48648_47840_x1125101074}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_1776342179}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x724689312}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x166323443}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_x432963912}

[**[ip]{lang="EN-US"}**[ *multicast-address*]{lang="EN-US"}]{#struct_0_48648_47840_x293841004}[：提供音乐保持媒体流的组播地址，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_48648_47840_1483977230}[：提供音乐保持媒体流的端口号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route ]{lang="EN-US"}***[address-list]{lang="EN-US"}*[&\<1-5\>]{lang="EN-US"}]{#struct_0_48648_47840_1991758875}[：组播路由出口地址，可以从这些出接口将音乐保持媒体流发送到配置的组播地址。]{style="font-family:宋体"}*[address-list]{lang="EN-US"}*[&\<1-5\>]{lang="EN-US"}[表示以空格为分隔，最多可以配置]{style="font-family:宋体"}[5]{lang="EN-US"}[个组播路由出接口地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1802980485}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1664576074}[配置提供音乐保持媒体流的组播地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1443177223}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register global]{lang="EN-US"}

[\[Sysname-voice-register-global\] multicast moh ip 239.1.1.1 port 2009 route 192.168.4.16]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1125101075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[moh]{lang="EN-US"}**[ **file**]{lang="EN-US"}]{#struct_0_48648_47840_210258238}
:::

::: {#-981317104 .myid}
[]{#_Toc404794683}[]{#struct_0_48648_47840_1050291790}

**SRST \-- SRST业务配置命令 \-- mwi**

------------------------------------------------------------------------

[**[mwi]{lang="EN-US"}**]{#struct_0_48648_47840_x1362710353}[命令用来开启消息等待指示功能。]{style="font-family:宋体"}

[**[undo mwi]{lang="EN-US"}**]{#struct_0_48648_47840_724346480}[命令用来关闭消息等待指示功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_231495424}

[**[mwi]{lang="EN-US"}**]{#struct_0_48648_47840_x1406809661}

[**[undo mwi]{lang="EN-US"}**]{#struct_0_48648_47840_651577256}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1146290848}

[[消息等待指示功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_48648_47840_1703239997}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1125101076}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_613542765}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_x1157523130}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1136456713}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_633232061}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_48648_47840_1636082}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_1440214676}[为号码]{style="font-family:宋体"}[1000]{lang="EN-US"}[开启消息等待指示功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x574852691}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 100]{lang="EN-US"}

[\[Sysname-voice-register-dn100\] number 1000]{lang="EN-US"}

[\[Sysname-voice-register-dn100\] mwi]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_1499196481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mode]{lang="EN-US"}**]{#struct_0_48648_47840_1296581052}
:::

::: {#1095489534 .myid}
[]{#_Toc404794684}[]{#struct_0_48648_47840_1227285356}

**SRST \-- SRST业务配置命令 \-- pickup-call any-group**

------------------------------------------------------------------------

[**[pickup-call any-group]{lang="EN-US"}**]{#struct_0_48648_47840_x1125101077}[命令用来配置代答方以"]{style="font-family:宋体"}[GPickUp]{lang="EN-US"}[软键]{style="font-family:宋体"}[\*]{lang="EN-US"}["按键实现组间代答。]{style="font-family:宋体"}

[**[undo pickup-call any-group]{lang="EN-US"}**]{#struct_0_48648_47840_x952541176}[命令用来删除已有配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_350125522}

[**[pickup-call any-group]{lang="EN-US"}**]{#struct_0_48648_47840_888496686}

[**[undo pickup-call any-group]{lang="EN-US"}**]{#struct_0_48648_47840_x1631552674}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_1085167583}

[[没有配置此命令。]{style="font-family:宋体"}]{#struct_0_48648_47840_1338168604}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_738900436}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_x87150502}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_790847535}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x440840062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x1125101070}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_48648_47840_x193026289}

[[假设被代答方]{style="font-family:宋体"}[IP Phone A]{lang="EN-US"}]{#struct_0_48648_47840_644091503}[存在某个代答组中，而代答方]{style="font-family:宋体"}[IP Phone B]{lang="EN-US"}[不在该代答组中或是不在任何代答组中，在这种情况下，为]{style="font-family:宋体"}[IP Phone B]{lang="EN-US"}[号码配置]{style="font-family:宋体"}**[pickup-call any-group]{lang="EN-US"}**[，]{style="font-family:宋体"}[IP Phone B]{lang="EN-US"}[可以用按]{style="font-family:宋体"} ["]{style="font-family:
宋体"}[GPickUp]{lang="EN-US"}[软键"，然后拨打"]{style="font-family:宋体"}[\*]{lang="EN-US"}["的方式为]{style="font-family:宋体"}[IP Phone A]{lang="EN-US"}[代答。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_x993277660}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x828728808}[配置用]{style="font-family:宋体"}[DN1]{lang="EN-US"}[注册成功的话机以"]{style="font-family:宋体"}[GPickUp]{lang="EN-US"}[软键]{style="font-family:宋体"}[\*]{lang="EN-US"}["按键实现组间代答。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_x1344100781}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 1]{lang="EN-US"}

[\[Sysname-voice-register-dn1\] number 1000]{lang="EN-US"}

[\[Sysname-voice-register-dn1\] pickup-call any-group]{lang="EN-US"}
:::

::: {#-874878932 .myid}
[]{#_Toc404794685}[]{#struct_0_48648_47840_x2106054012}

**SRST \-- SRST业务配置命令 \-- pickup-group**

------------------------------------------------------------------------

[**[pickup-group]{lang="EN-US"}**]{#struct_0_48648_47840_x1125101071}[命令用来为号码指定呼叫代答组。]{style="font-family:宋体"}

[**[undo pickup-group]{lang="EN-US"}**]{#struct_0_48648_47840_x1759110230}[命令用来删除已配置的呼叫代答组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_48648_47840_x465606893}

[**[pickup-group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_48648_47840_1600511279}

[**[undo pickup-group]{lang="EN-US"}**]{#struct_0_48648_47840_1371445214}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_48648_47840_330469971}

[[没有配置呼叫代答组。]{style="font-family:宋体"}]{#struct_0_48648_47840_1126118684}

[[【视图】]{style="font-family:黑体"}]{#struct_0_48648_47840_1262934161}

[[DN]{lang="EN-US"}]{#struct_0_48648_47840_x895736557}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_48648_47840_423825275}

[[network-admin]{lang="EN-US"}]{#struct_0_48648_47840_x215291499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_48648_47840_x47620777}

[[【参数】]{style="font-family:黑体"}]{#struct_0_48648_47840_376457437}

[*[group-number]{lang="EN-US"}*]{#struct_0_48648_47840_x1526194661}[：]{style="font-family:宋体"}[呼叫代答组]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为数字、字母、]{style="font-family:宋体"}[\#]{lang="EN-US"}[、]{style="font-family:宋体"}[\*]{lang="EN-US"}[，字母区分大小写。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_48648_47840_1213551082}

[[\# ]{lang="EN-US"}]{#struct_0_48648_47840_x1072132113}[配置用]{style="font-family:宋体"}[DN100]{lang="DA"}[注册成功的话机属于呼叫代答组]{style="font-family:宋体"}[25]{lang="DA"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_48648_47840_582067691}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] voice register dn 100]{lang="EN-US"}

[\[Sysname-voice-register-dn100\] number 1000]{lang="EN-US"}

[\[Sysname-voice-register-dn100\] pickup-group 25]{lang="EN-US"}

[]{#_Toc388276779}[]{#_Toc388276826}[]{#_Toc389573636}[]{#_Toc388276780}[]{#_Toc388276827}[]{#_Toc389573637}[ ]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
