::: {#1002089605 .myid}
[]{#_Toc404794969}[]{#struct_0_17471_x3053_x914740284}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- akm mode**

------------------------------------------------------------------------

[**[akm mode]{lang="EN-US"}**]{#struct_0_17471_x3053_1190580936}[命令用来配置身份认证与密钥管理。]{style="font-family:宋体"}

[**[undo akm mode]{lang="EN-US"}**]{#struct_0_17471_x3053_x399878135}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1846050350}

[**[akm mode]{lang="EN-US"}**[ { **dot1x** \| **psk** }]{lang="EN-US"}]{#struct_0_17471_x3053_2092075841}

[**[undo akm mode]{lang="EN-US"}**]{#struct_0_17471_x3053_1632938497}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x89933614}

[[未配置身份认证与密钥管理。]{style="font-family:宋体"}]{#struct_0_17471_x3053_523767550}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1947353642}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1664466350}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x771413677}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1897171168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1469325320}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x693593352}

[**[dot1x]{lang="EN-US"}**]{#struct_0_17471_x3053_1601226807}[：表示身份认证与密钥管理的模式是]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[**[psk]{lang="EN-US"}**]{#struct_0_17471_x3053_x552333983}[：表示身份认证与密钥管理的模式是]{style="font-family:宋体"}[PSK]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1176736878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能在无线服务模板处于关闭的状态下进行配置，并且]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1833373617}[802.1X]{lang="EN-US"}[和]{style="font-family:宋体"}[PSK]{lang="EN-US"}[两种模式不能同时存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_17471_x3053_256617198}[模式和]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户认证模式相互依赖，必须同时配置。有关]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的详细介绍请参见"]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[用户接入认证"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSK]{lang="EN-US"}]{#struct_0_17471_x3053_x1833452660}[模式和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证模式或]{style="font-family:宋体"}[Bypass]{lang="EN-US"}[用户认证模式相互依赖，必须同时配置。有关]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证和]{style="font-family:宋体"}[Bypass]{lang="EN-US"}[认证的详细介绍请参见"]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[用户接入认证"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若配置了身份认证与密钥管理，则安全]{style="font-family:宋体"}]{#struct_0_17471_x3053_x2088858969}[IE]{lang="EN-US"}[和加密套件必须配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_2116992392}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x1408233956}[配置身份认证与密钥管理模式为]{style="font-family:宋体"}[PSK]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_x1664466349}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] akm mode psk]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1981332794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_1531492617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[security-ie]{lang="EN-US"}**]{#struct_0_17471_x3053_1523645901}
:::

::: {#-35893386 .myid}
[]{#_Toc404794970}[]{#struct_0_17471_x3053_567727564}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- cipher-suite**

------------------------------------------------------------------------

[**[cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_x467631599}[命令用来配置在帧加密时使用的加密套件。]{style="font-family:宋体"}

[**[undo cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_x470772184}[命令用来禁用选择的加密套件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1164907552}

[**[cipher-suite ]{lang="EN-US"}**[{ **ccmp \| tkip \| wep40 \| wep104 \| wep128** }]{lang="EN-US"}]{#struct_0_17471_x3053_1045901974}

[**[undo cipher-suite ]{lang="EN-US"}**[{ **ccmp \| tkip \| wep40 \| wep104 \| wep128** }]{lang="EN-US"}]{#struct_0_17471_x3053_x929384627}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1047122291}

[[未配置加密套件。]{style="font-family:宋体"}]{#struct_0_17471_x3053_x2073093593}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1346577300}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1664466352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1934213091}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1976992384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_608967966}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1875585156}

[**[ccmp]{lang="EN-US"}**]{#struct_0_17471_x3053_x997944782}[：]{style="font-family:宋体"}[AES-CCMP]{lang="EN-US"}[加密套件。]{style="font-family:宋体"}

[**[tkip]{lang="EN-US"}**]{#struct_0_17471_x3053_x275973890}[：]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[加密套件。]{style="font-family:宋体"}

[**[wep40]{lang="EN-US"}**]{#struct_0_17471_x3053_x2013431928}[：]{style="font-family:宋体"}[WEP40]{lang="EN-US"}[加密套件。]{style="font-family:宋体"}

[**[wep104]{lang="EN-US"}**]{#struct_0_17471_x3053_x1033870888}[：]{style="font-family:宋体"}[WEP104]{lang="EN-US"}[加密套件。]{style="font-family:宋体"}

[**[wep128]{lang="EN-US"}**]{#struct_0_17471_x3053_2021603347}[：]{style="font-family:宋体"}[WEP128]{lang="EN-US"}[加密套件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1891665270}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_17471_x3053_265401909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了安全]{style="font-family:宋体"}]{#struct_0_17471_x3053_x2072426285}[IE]{lang="EN-US"}[，则必须配置]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[或者]{style="font-family:宋体"}[CCMP]{lang="EN-US"}[加密套件中的一种。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP]{lang="EN-US"}]{#struct_0_17471_x3053_443655363}[加密套件只能配置]{lang="EN-US" style="font-family:
宋体"}[WEP40/WEP104/WEP128]{lang="EN-US"}[其中的一种]{lang="EN-US" style="font-family:宋体"}[，且需要配置与加密套件种类相对应的]{style="font-family:宋体"}[WEP]{lang="EN-US"}[密钥及]{style="font-family:宋体"}[WEP]{lang="EN-US"}[密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若配置了加密套件，则身份认证与密钥管理和安全]{style="font-family:宋体"}]{#struct_0_17471_x3053_582644951}[IE]{lang="EN-US"}[则必须配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WEP128]{lang="EN-US"}]{#struct_0_17471_x3053_1038138085}[和]{style="font-family:宋体"}[CCMP]{lang="EN-US"}[或]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1935983406}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x1664466351}[配置]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[加密套件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_1957469678}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] cipher-suite tkip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1456581433}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[security-ie]{lang="EN-US"}**]{#struct_0_17471_x3053_2025895485}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wep key]{lang="EN-US"}**]{#struct_0_17471_x3053_1640220814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wep key-id]{lang="EN-US"}**]{#struct_0_17471_x3053_1231373336}
:::

::: {#-2007331956 .myid}
[]{#_Toc404794971}[]{#struct_0_17471_x3053_1884064220}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- gtk-rekey client-offline enable**

------------------------------------------------------------------------

[**[gtk-rekey client-offline enable]{lang="EN-US"}**]{#struct_0_17471_x3053_677202400}[命令用来启动当无线客户端离线时更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[的功能。]{style="font-family:宋体"}

[**[undo gtk-rekey client-offline enable]{lang="EN-US"}**]{#struct_0_17471_x3053_1859447277}[命令用来关闭无线客户端离线更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1327756365}

[**[gtk-rekey client-offline enable]{lang="EN-US"}**]{#struct_0_17471_x3053_820726351}

[**[undo gtk-rekey client-offline enable]{lang="EN-US"}**]{#struct_0_17471_x3053_x645543653}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1791910762}

[[无线客户端离线更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}]{#struct_0_17471_x3053_x1570633641}[功能关闭。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x371868743}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1664466354}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1554185151}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1789779437}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_851789520}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1042382214}

[[只有开启了]{style="font-family:宋体"}[GTK]{lang="EN-US"}]{#struct_0_17471_x3053_x1639818556}[更新功能，无线客户端离线时更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[的功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_387911836}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_285181844}[开启无线客户端时更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_1070185572}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] gtk-rekey client-offline enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1064800956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gtk-rekey enable]{lang="EN-US"}**]{#struct_0_17471_x3053_x47426873}
:::

::: {#-1066930310 .myid}
[]{#_Toc404794972}[]{#struct_0_17471_x3053_x1767416574}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- gtk-rekey enable**

------------------------------------------------------------------------

[**[gtk-rekey enable]{lang="EN-US"}**]{#struct_0_17471_x3053_842110052}[命令用来开启更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[的功能。]{style="font-family:宋体"}

[**[undo gtk-rekey enable]{lang="EN-US"}**]{#struct_0_17471_x3053_859262346}[命令用来关闭更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1569909700}

[**[gtk-rekey enable]{lang="EN-US"}**]{#struct_0_17471_x3053_x1664466353}

[**[undo gtk-rekey enable]{lang="EN-US"}**]{#struct_0_17471_x3053_794670264}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x33734575}

[[GTK]{lang="EN-US"}]{#struct_0_17471_x3053_1766300464}[更新功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x462662672}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x625210691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1208615086}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1470851767}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1904623766}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1317278410}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x870398766}[开启更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_1265917260}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] gtk-rekey enable]{lang="EN-US"}
:::

::: {#1019637218 .myid}
[]{#_Toc404794973}[]{#struct_0_17471_x3053_2087027428}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- gtk-rekey method**

------------------------------------------------------------------------

[**[gtk-rekey method]{lang="EN-US"}**]{#struct_0_17471_x3053_674185814}[命令用来配置]{style="font-family:宋体"}[GTK]{lang="EN-US"}[更新方法。]{style="font-family:宋体"}

[**[undo gtk-rekey method]{lang="EN-US"}**]{#struct_0_17471_x3053_1334496308}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1430661985}

[**[gtk-rekey method]{lang="EN-US"}**[ { **packet-based** \[ *packet* \] \| **time-based** \[ *time* \] }]{lang="EN-US"}]{#struct_0_17471_x3053_x1724342202}

[**[undo gtk-rekey method]{lang="EN-US"}**]{#struct_0_17471_x3053_x1925343596}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1380555646}

[[GTK]{lang="EN-US"}]{#struct_0_17471_x3053_1271184850}[更新采用基于时间的方法，时间间隔为]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1331758937}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_1693235605}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x376981825}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_382111303}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_53709075}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1831889862}

[**[packet-based]{lang="EN-US"}**]{#struct_0_17471_x3053_x2129181610}[：表示基于数据包的更新方法。]{style="font-family:宋体"}

[*[packet]{lang="EN-US"}*]{#struct_0_17471_x3053_x1251219611}[：指定传输的数据包（包括组播和广播）的数目，在传送指定数目的数据包（包括组播和广播）后更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[5000]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则表示传输]{style="font-family:宋体"}[10000000]{lang="EN-US"}[个报文后进行密钥更新。]{style="font-family:宋体"}

[**[time-based]{lang="EN-US"}**]{#struct_0_17471_x3053_x888611973}[：表示基于时间的]{style="font-family:宋体"}[GTK]{lang="EN-US"}[更新方法。]{style="font-family:宋体"}

[*[time]{lang="EN-US"}*]{#struct_0_17471_x3053_674185815}[：指定]{style="font-family:宋体"}[GTK]{lang="EN-US"}[密钥更新的周期。取值范围为]{style="font-family:宋体"}[180]{lang="EN-US"}[～]{style="font-family:宋体"}[604800]{lang="EN-US"}[，单位为秒。如果未指定本参数，则表示时间间隔是]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1334496307}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有开启了]{style="font-family:宋体"}]{#struct_0_17471_x3053_1430727521}[GTK]{lang="EN-US"}[更新功能，]{style="font-family:宋体"}[GTK]{lang="EN-US"}[更新方法才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用该命令配置]{style="font-family:宋体"}]{#struct_0_17471_x3053_x2131380501}[GTK]{lang="EN-US"}[密钥更新方法，新配置的方法会覆盖前一次的配置。例如，如果先配置了基于数据包的方法，然后又配置了基于时间的方法，则最后生效的是基于时间的方法。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[若该命令在无线服务模板处于开启状态下配置，则分为以下几种情况：]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1300514074}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[基于时间的]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1300514073}[GTK]{lang="EN-US"}[的更新方式不改变，只改变时间值，则该配置在重新创建定时器后生效；]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[基于报文数的]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1407027724}[GTK]{lang="EN-US"}[更新方式不改变，只改变报文数值，则该新的配置立即生效；]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[更新方式由基于时间更新改为基于报文数更新，则删除]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1300514072}[GTK]{lang="EN-US"}[更新定时器，在组播或广播报文数大于配置的数目值之后立即生效；]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[更新方式由基于报文数更新改为基于时间更新，则]{style="font-family:宋体"}]{#struct_0_17471_x3053_1321855631}[GTK]{lang="EN-US"}[不再基于报文数目更新，而是创建]{style="font-family:宋体"}[GTK]{lang="EN-US"}[更新定时器，定时器超时之后更新]{style="font-family:宋体"}[GTK]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1718246171}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_719842975}[配置基于时间的]{style="font-family:宋体"}[GTK]{lang="EN-US"}[更新方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_x1682889525}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] gtk-rekey method time-based 3600]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_239462407}[配置基于数据包的]{style="font-family:宋体"}[GTK]{lang="EN-US"}[更新方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_1518935773}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] gtk-rekey method packet-based 600000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1844157997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gtk-rekey enable]{lang="EN-US"}**]{#struct_0_17471_x3053_1279846618}
:::

::: {#-107922847 .myid}
[]{#_Toc404794974}[]{#struct_0_17471_x3053_67864204}[]{#_Toc395108687}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- key-derivation**

------------------------------------------------------------------------

[**[key-derivation]{lang="EN-US"}**]{#struct_0_17471_x3053_x1140103476}[命令用来配置密钥衍生算法。]{style="font-family:宋体"}

[**[undo key-derivation]{lang="EN-US"}**]{#struct_0_17471_x3053_1128131236}[命令]{style="font-family:宋体"}[用来]{style="font-family:宋体"}[恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1586452389}

[**[key-derivation]{lang="EN-US"}**[ { **sha1** \| **sha1-and-sha256** \| **sha256** }]{lang="EN-US"}]{#struct_0_17471_x3053_x1308560401}

[**[undo key-derivation]{lang="EN-US"}**]{#struct_0_17471_x3053_1969494793}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1498219737}

[[密钥衍生算法为]{style="font-family:宋体"}[sha1]{lang="EN-US"}]{#struct_0_17471_x3053_x1357166324}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x554612669}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x552203882}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1159818227}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_2015228906}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1437622982}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x2102869249}

[**[sha1]{lang="EN-US"}**]{#struct_0_17471_x3053_x1517320637}[：表示]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[算法，它使用]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[算法进行迭代计算产生密钥。]{style="font-family:宋体"}

[**[sha1-and-sha256]{lang="EN-US"}**]{#struct_0_17471_x3053_551347458}[：表示]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[和]{style="font-family:宋体"}[SHA256]{lang="EN-US"}[算法，它使用]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[或]{style="font-family:宋体"}[HMAC-SHA256]{lang="EN-US"}[算法进行迭代计算产生密钥]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[sha256]{lang="EN-US"}**]{#struct_0_17471_x3053_1230663618}[：表示]{style="font-family:宋体"}[SHA256]{lang="EN-US"}[算法，它使用]{style="font-family:宋体"}[HMAC-SHA256]{lang="EN-US"}[算法进行迭代计算产生密钥。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1911523699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用]{style="font-family:宋体"}]{#struct_0_17471_x3053_1854056122}[RSNA]{lang="EN-US"}[安全机制，密钥衍生算法才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置保护管理帧功能为]{style="font-family:宋体"}]{#struct_0_17471_x3053_72968561}**[mandatory]{lang="EN-US"}**[模式，建议指定密钥衍生类型为]{style="font-family:宋体"}**[sha256]{lang="EN-US"}[。]{style="font-family:宋体"}**

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1379389080}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_455746780}[配置密钥衍生算法为]{style="font-family:宋体"}[SHA256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_902815828}

[\[Sysname\] wlan service-template 1]{lang="EN-US"}

[\[Sysname-wlan-st-1\] key-derivation sha256]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_537917097}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[akm mode]{lang="EN-US"}**]{#struct_0_17471_x3053_934159327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_x335420323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[security-ie]{lang="EN-US"}**]{#struct_0_17471_x3053_x517479787}
:::

::: {#134034940 .myid}
[]{#_Toc404794975}[]{#struct_0_17471_x3053_293929697}[]{#_Toc395108688}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf**

------------------------------------------------------------------------

[**[pmf]{lang="EN-US"}**]{#struct_0_17471_x3053_993468189}[命令用来开启保护管理帧功能。]{style="font-family:宋体"}

[**[undo pmf]{lang="EN-US"}**]{#struct_0_17471_x3053_1354612189}[命令用来关闭保护管理帧功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1546861473}

[**[pmf]{lang="EN-US"}**[ { **mandatory** \| **optional** }]{lang="EN-US"}]{#struct_0_17471_x3053_x1590249617}

[**[undo pmf]{lang="EN-US"}**]{#struct_0_17471_x3053_518479041}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1218353386}

[[保护管理帧功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_17471_x3053_968741735}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_42660451}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1901504264}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_559633125}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1273287467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1967162286}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1249324338}

[**[optional]{lang="EN-US"}**]{#struct_0_17471_x3053_x1790502709}[：指定保护管理帧功能为可选模式，即支持或不支持保护管理帧功能的客户端均可接入。]{style="font-family:宋体"}

[**[mandatory]{lang="EN-US"}**]{#struct_0_17471_x3053_x1285709268}[：指定保护管理帧功能为强制模式，即不支持保护管理帧功能的客户端无法接入。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1329615360}

[[当使用]{style="font-family:宋体"}[RSNA]{lang="EN-US"}]{#struct_0_17471_x3053_x554248761}[安全机制且配置了]{style="font-family:宋体"}[CCMP]{lang="EN-US"}[加密套件和]{style="font-family:宋体"}[RSN]{lang="EN-US"}[安全信息元素时，保护管理帧功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x974874952}

[[\# ]{lang="EN-US" style="color:black"}]{#struct_0_17471_x3053_x427633302}[开启保护管理帧功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_114918371}

[\[Sysname\] wlan service-template 1]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="EN-US" style="font-size:10.0pt"}[-wlan-st-1\] pmf optional]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x309801187}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[security-ie]{lang="EN-US"}**]{#struct_0_17471_x3053_1678141065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_x1835286446}
:::

::: {#95258087 .myid}
[]{#_Toc404794976}[]{#struct_0_17471_x3053_x1959201774}[]{#_Toc395108689}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf association-comeback**

------------------------------------------------------------------------

[**[pmf association-comeback]{lang="EN-US"}**]{#struct_0_17471_x3053_x792672155}[命令用来配置保护管理帧的关联返回时间。]{style="font-family:
宋体"}

[**[undo pmf association-comeback]{lang="EN-US"}**]{#struct_0_17471_x3053_x194167499}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1462658506}

[**[pmf]{lang="EN-US"}**[ **association-comeback** *time*]{lang="EN-US"}]{#struct_0_17471_x3053_x1808497888}

[**[undo pmf]{lang="EN-US"}**[ **association-comeback**]{lang="EN-US"}]{#struct_0_17471_x3053_1439589378}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1976941392}

[[保护管理帧的关联返回时间为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_17471_x3053_x1400095226}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1451165570}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_1929642034}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1495655215}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1611951324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_730959716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1477089384}

[*[time]{lang="EN-US"}*]{#struct_0_17471_x3053_1975516452}[：保护管理帧的关联返回时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1477046275}

[[当]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17471_x3053_33353902}[收到客户端的关联重关联请求帧，]{style="font-family:宋体"}[AP]{lang="EN-US"}[会拒绝此客户端的关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联请求帧，并且向客户端发送关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联响应帧，其中携带了保护管理帧关联返回时间。到了保护管理帧关联返回时间，]{style="font-family:宋体"}[AP]{lang="EN-US"}[才会接收客户端的关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联请求帧。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1764361499}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_1978976384}[配置保护管理帧的关联返回时间为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_471083195}

[\[Sysname\] wlan service-template 1]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="EN-US" style="font-size:10.0pt"}[-wlan-st-1\] pmf association-comeback 2]{lang="EN-US"}
:::

::: {#-1078495170 .myid}
[]{#_Toc404794977}[]{#struct_0_17471_x3053_x1808696807}[]{#_Toc395108690}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf saquery retrycount**

------------------------------------------------------------------------

[**[pmf]{lang="EN-US"}**[ **saquery retrycount**]{lang="EN-US"}]{#struct_0_17471_x3053_461535267}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[的最大重传次数]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[undo pmf saquery retrycount]{lang="EN-US"}**]{#struct_0_17471_x3053_1641744071}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1223651585}

[**[pmf]{lang="EN-US"}**[ **saquery retrycount** *count*]{lang="EN-US"}]{#struct_0_17471_x3053_1225304129}

[**[undo pmf]{lang="EN-US"}**[ **saquery retrycount** ]{lang="EN-US"}]{#struct_0_17471_x3053_x20815463}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1882178378}

[[AC]{lang="EN-US"}]{#struct_0_17471_x3053_836751998}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[帧的最大重传次数为]{style="font-family:宋体"}[4]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1400454347}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x837421618}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1095000746}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1856156993}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1188533943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1797367625}

[*[count]{lang="EN-US"}*]{#struct_0_17471_x3053_1211237498}[：表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[帧的最大重传次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x929203719}

[[若]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17471_x3053_x1480368506}[在]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[重试次数内收到]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[响应帧，则认为客户端在线，并且在关联返回时间内，不再响应关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联请求，当关联返回时间超时后，再次收到客户端的关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联请求帧时，则会再次触发]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[过程。若]{style="font-family:宋体"}[AP]{lang="EN-US"}[在]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[重试次数内未收到]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[响应帧，并且关联返回时间已经超时，则]{style="font-family:宋体"}[AP]{lang="EN-US"}[将认为客户端已经掉线，当再次收到该客户端的关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联请求帧时，允许其重新接入。若在关联返回时间内，]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[过程未完成，则当关联返回时间超时后，再次收到客户端的关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联请求帧时，]{style="font-family:宋体"}[AP]{lang="EN-US"}[将发送关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联响应帧，响应状态值为"关联]{style="font-family:宋体"}[/]{lang="EN-US"}[重关联临时被拒绝，稍后重连"，并携带通过]{style="font-family:宋体"}**[pmf]{lang="EN-US"}**[ **association-comeback**]{lang="EN-US"}[命令指定关联返回时间，但不重新触发]{style="font-family:宋体"}[SA Query]{lang="EN-US"}[过程。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1895664534}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x688039253}[设置]{style="font-family:宋体"}[AC]{lang="EN-US"}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[帧的最大重传次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_1633882609}

[\[Sysname\] wlan service-template 1]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="EN-US" style="font-size:10.0pt"}[-wlan-st-1\] pmf saquery retrycount 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1674248888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pmf]{lang="EN-US"}**]{#struct_0_17471_x3053_x285557188}[ { **mandatory** \| **optional** }]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pmf saquery retrycount]{lang="EN-US"}**]{#struct_0_17471_x3053_433496740}
:::

::: {#747121382 .myid}
[]{#_Toc404794978}[]{#struct_0_17471_x3053_1828364542}[]{#_Toc395108691}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf saquery retrytimeout**

------------------------------------------------------------------------

[**[pmf saquery retrytimeout]{lang="EN-US"}**]{#struct_0_17471_x3053_306733459}[命令用来设置]{style="font-family:
宋体"}[AP]{lang="EN-US"}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[帧的时间间隔。]{style="font-family:宋体"}

[**[undo pmf saquery retrytimeout]{lang="EN-US"}**]{#struct_0_17471_x3053_x588112546}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x975348948}

[**[pmf saquery retrytimeout]{lang="EN-US"}**[ *timeout*]{lang="EN-US"}]{#struct_0_17471_x3053_1580424522}

[**[undo pmf saquery retrytimeout]{lang="EN-US"}**]{#struct_0_17471_x3053_1122584923}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_67798668}

[[AP]{lang="EN-US"}]{#struct_0_17471_x3053_x1897406449}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[帧的时间间隔为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1437793305}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x180363681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x2081173514}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x722751702}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x820808171}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1932482895}

[*[timeout]{lang="EN-US"}*]{#struct_0_17471_x3053_211388291}[：指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[帧的时间间隔]{style="font-family:宋体"}[,]{lang="EN-US" style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_844238439}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x752841893}[设置]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送]{style="font-family:宋体"}[SA Query request]{lang="EN-US"}[帧的时间间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<]{lang="EN-US"}]{#struct_0_17471_x3053_x1498285273}[Sysname]{lang="EN-US" style="font-size:10.0pt"}[\> system-view]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="EN-US" style="font-size:10.0pt"}[\] wlan service-template 1]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="EN-US" style="font-size:10.0pt"}[-wlan-st-1\] pmf saquery retrytimeout 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x476763368}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pmf]{lang="EN-US"}**[ { **mandatory** \| **optional** }]{lang="EN-US"}]{#struct_0_17471_x3053_1588098875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pmf saquery retry]{lang="EN-US"}**]{#struct_0_17471_x3053_x228797792}**[timeout]{lang="EN-US"}**
:::

::: {#1539569968 .myid}
[]{#_Toc404794979}[]{#struct_0_17471_x3053_757198752}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- preshared-key**

------------------------------------------------------------------------

[**[preshared-key]{lang="EN-US"}**]{#struct_0_17471_x3053_2130994030}[命令用来配置]{style="font-family:宋体"}[PSK]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[**[undo preshared-key]{lang="EN-US"}**]{#struct_0_17471_x3053_x2082851614}[命令用来删除已配置的]{style="font-family:宋体"}[PSK]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_674185812}

[**[preshared-key]{lang="EN-US"}**[ { **pass-phrase \| raw-key** } { **cipher \| simple** } *key*]{lang="EN-US"}]{#struct_0_17471_x3053_1334496302}

[**[undo preshared-key]{lang="EN-US"}**]{#struct_0_17471_x3053_1431055201}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_604229140}

[[未配置]{style="font-family:宋体"}[PSK]{lang="EN-US"}]{#struct_0_17471_x3053_1103600298}[密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x86301777}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_126111898}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x681398579}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1112694839}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x889459794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_44307636}

[**[pass-phrase]{lang="EN-US"}**]{#struct_0_17471_x3053_1647081819}[：以字符串方式输入预共享密钥。]{style="font-family:宋体"}

[**[raw-key]{lang="EN-US"}**]{#struct_0_17471_x3053_x11880335}[：以十六进制数方式输入预共享密钥。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_17471_x3053_11629899}[：以密文方式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_17471_x3053_1647973323}[：以明文方式设置密钥。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_17471_x3053_x1094726123}[：设置明文密钥或密文密钥，区分大小写。密钥长度的范围与选择的密钥参数有关，具体关系如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}**[pass-phrase simple]{lang="EN-US"}**]{#struct_0_17471_x3053_674185813}[，密钥是]{lang="EN-US" style="font-family:
宋体"}[8]{lang="EN-US"}[～]{lang="EN-US" style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}**[pass-phrase cipher]{lang="EN-US"}**]{#struct_0_17471_x3053_1334496301}[，密钥是]{lang="EN-US" style="font-family:
宋体"}[8]{lang="EN-US"}[～]{lang="EN-US" style="font-family:
宋体"}[117]{lang="EN-US"}[个字符的字符串。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}**[raw-key simple]{lang="EN-US"}**]{#struct_0_17471_x3053_1431120737}[，密钥是]{lang="EN-US" style="font-family:
宋体"}[64]{lang="EN-US"}[个十六进制数。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}**[raw-key cipher]{lang="EN-US"}**]{#struct_0_17471_x3053_x1750788869}[，密钥是]{lang="EN-US" style="font-family:
宋体"}[8]{lang="EN-US"}[～]{lang="EN-US" style="font-family:
宋体"}[117]{lang="EN-US"}[个]{lang="EN-US" style="font-family:
宋体"}[字符串]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_661337956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能在无线服务模板处于关闭的状态下进行配置。并且只有认证密钥管理模式为]{style="font-family:宋体"}]{#struct_0_17471_x3053_1742411583}[PSK]{lang="EN-US"}[时，此命令才能够生效，当认证密钥管理模式为]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[时，配置了此项，无线服务模板可以使能，但此配置不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSK]{lang="EN-US"}]{#struct_0_17471_x3053_x335485859}[密钥只能配置一个。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1478969356}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_460658695}[配置使用明文字符串]{style="font-family:宋体"}[12345678]{lang="EN-US"}[作为]{style="font-family:宋体"}[PSK]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_1781332036}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] akm mode psk]{lang="EN-US"}

[\[Sysname-wlan-st-security\] akm preshared-key pass-phrase simple 12345678]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_981700187}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[akm mode]{lang="EN-US"}**]{#struct_0_17471_x3053_1644932631}
:::

::: {#1049468364 .myid}
[]{#_Toc404794980}[]{#struct_0_17471_x3053_x1780852359}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- ptk-lifetime**

------------------------------------------------------------------------

[**[ptk-lifetime]{lang="EN-US"}**]{#struct_0_17471_x3053_409008043}[命令用来配置]{style="font-family:宋体"}[PTK]{lang="EN-US"}[的生存时间。]{style="font-family:宋体"}

[**[undo ptk-lifetime]{lang="EN-US"}**]{#struct_0_17471_x3053_x1767357527}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_674185810}

[**[ptk-lifetime]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_17471_x3053_1334496304}

[**[undo ptk-lifetime]{lang="EN-US"}**]{#struct_0_17471_x3053_1430924129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_199901574}

[[PTK]{lang="EN-US"}]{#struct_0_17471_x3053_x1634421118}[的生存时间为]{style="font-family:宋体"}[43200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1569600978}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x511028348}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x549030260}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_960368743}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_419077919}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1948112237}

[*[time]{lang="EN-US"}*]{#struct_0_17471_x3053_814520784}[：指定生存时间，取值范围为]{style="font-family:宋体"}[180]{lang="EN-US"}[～]{style="font-family:宋体"}[604800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_2002654870}

[[若该命令在无线服务模板处于开启状态下配置，则在原有定时器超时后，再创建新的定时器。]{style="font-family:宋体"}]{#struct_0_17471_x3053_507898394}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x700541037}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_1537238494}[配置]{style="font-family:宋体"}[PTK]{lang="EN-US"}[生存时间为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_674185811}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] ptk-lifetime 200]{lang="EN-US"}
:::

::: {#176517669 .myid}
[]{#_Toc404794981}[]{#struct_0_17471_x3053_1334496303}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- security-ie**

------------------------------------------------------------------------

[**[security-ie]{lang="EN-US"}**]{#struct_0_17471_x3053_1430989665}[命令用来配置信标和探查响应帧携带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo security-ie]{lang="EN-US"}**]{#struct_0_17471_x3053_942097459}[命令用来配置信标和探查响应帧不携带安全]{style="font-family:宋体"}[IE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1861517218}

[**[security-ie ]{lang="EN-US"}**[{ **rsn** \| **wpa** }]{lang="EN-US"}]{#struct_0_17471_x3053_1453510068}

[**[undo security-ie ]{lang="EN-US"}**[{ **rsn** \| **wpa** }]{lang="EN-US"}]{#struct_0_17471_x3053_957621352}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1751566185}

[[信标和探查响应帧不携带]{style="font-family:宋体"}[WPA IE]{lang="EN-US"}]{#struct_0_17471_x3053_x1211668269}[或]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x2028483317}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1203535585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1829686619}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1550716415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x266180340}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1971855549}

[**[rsn]{lang="EN-US"}**]{#struct_0_17471_x3053_674185808}[：设置在]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送信标和探查响应帧时携带]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}[。]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}[通告了]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[RSN]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[wpa]{lang="EN-US"}**]{#struct_0_17471_x3053_x621818840}[：设置在]{style="font-family:宋体"}[AP]{lang="EN-US"}[发送信标和探查响应帧时携带]{style="font-family:宋体"}[WPA IE]{lang="EN-US"}[。]{style="font-family:宋体"}[WPA IE]{lang="EN-US"}[通告了]{style="font-family:宋体"}[AP]{lang="EN-US"}[的]{style="font-family:宋体"}[WPA]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1647139153}

[[该命令只能在无线服务模板处于关闭的状态下进行配置，并且必须要配置]{style="font-family:宋体"}[CCMP]{lang="EN-US"}]{#struct_0_17471_x3053_x1439197969}[或]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[加密套件。]{style="font-family:宋体"}

[[WPA IE]{lang="EN-US"}]{#struct_0_17471_x3053_1614393619}[和]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}[可以同时配置。]{style="font-family:宋体"}

[[若配置了安全]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_17471_x3053_1633789813}[，则认证密钥管理模式和加密套件必须配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1469203701}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_1678160351}[配置信标帧和探查响应帧携带]{style="font-family:宋体"}[RSN]{lang="EN-US"}[信息元素。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_x1440992022}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] security-ie rsn]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x2105037544}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_1740802127}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[akm mode]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_17471_x3053_x572302951}**[dot1x]{lang="EN-US"}**[ \| **psk** }]{lang="EN-US"}
:::

::: {#1886904327 .myid}
[]{#_Toc404794982}[]{#struct_0_17471_x3053_1656220526}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- tkip-cm-time**

------------------------------------------------------------------------

[**[tkip-cm-time]{lang="EN-US"}**]{#struct_0_17471_x3053_x618715824}[命令用来配置发起]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[反制策略时间。]{style="font-family:宋体"}

[**[undo tkip-cm-time]{lang="EN-US"}**]{#struct_0_17471_x3053_x1439485810}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_674185809}

[**[tkip-cm-time]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_17471_x3053_x621818841}

[**[undo tkip-cm-time]{lang="EN-US"}**]{#struct_0_17471_x3053_x1647073617}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1900284956}

[[发起]{style="font-family:宋体"}[TKIP]{lang="EN-US"}]{#struct_0_17471_x3053_545401199}[反制策略时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即不启动反制策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1476616327}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x616049617}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x83033610}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x2146502404}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1807756024}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_421289361}

[*[time]{lang="EN-US"}*]{#struct_0_17471_x3053_886214890}[：设置发起]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[反制策略时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x181614436}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在配置了]{style="font-family:宋体"}]{#struct_0_17471_x3053_x157018219}[TKIP]{lang="EN-US"}[加密套件时，此命令才能够生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若该命令在无线服务模板处于开启状态时配置，则原有定时器超时后，再创建新的定时器。]{style="font-family:宋体"}]{#struct_0_17471_x3053_x920339732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[启动]{style="font-family:宋体"}]{#struct_0_17471_x3053_1538365052}[TKIP]{lang="EN-US"}[反制策略后，如果相邻两次]{style="font-family:宋体"}[MIC]{lang="EN-US"}[错误的时间间隔小于等于配置的时间，则会解除所有关联到该无线服务的无线客户端，并且只有在]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[反制策略实施的时间（]{style="font-family:宋体"}[60s]{lang="EN-US"}[）后，才允许无线客户端重新建立关联。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_674185806}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x621818830}[配置发起]{style="font-family:宋体"}[TKIP]{lang="EN-US"}[反制策略时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_x1647139146}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] tkip-cm-time 180]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_2096319976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_1838101011}
:::

::::: {#-1541959685 .myid}
[]{#_Toc404794983}[]{#struct_0_17471_x3053_x355884958}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- user-authentication mode central**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](WLAN用户安全命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17471_x3053_x334226818}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:
宋体"}]{#struct_0_17471_x3053_x2036729670}
:::

[ ]{lang="EN-US"}

[**[user-authentication mode central]{lang="EN-US"}**]{#struct_0_17471_x3053_x754507620}[命令用来配置用户认证模式为集中式认证。]{style="font-family:宋体"}

[**[undo user-authentication mode central]{lang="EN-US"}**]{#struct_0_17471_x3053_x1448558034}[命令用来取消集中式认证的用户认证模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_662960358}

[**[user-authentication mode central]{lang="EN-US"}**]{#struct_0_17471_x3053_1714647805}

[**[undo user-authentication mode central]{lang="EN-US"}**]{#struct_0_17471_x3053_1847294333}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_244937129}

[[用户认证模式为集中式认证，即在]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17471_x3053_674185807}[上认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x621818831}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1647073610}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1497000429}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1520131413}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_2029614256}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x587770566}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。并且只有在]{style="font-family:宋体"}[Master AC]{lang="EN-US"}]{#struct_0_17471_x3053_4277518}[上执行该命令时，才能够生效。]{style="font-family:宋体"}

[[集中式认证是指用户认证和密钥协商不在同一个]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_17471_x3053_x500334638}[上，这种情况只有在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[和]{style="font-family:宋体"}[BAC]{lang="EN-US"}[的组网情况下才有可能发生。当配置分层认证时，无线客户端虽然在]{style="font-family:宋体"}[BAC]{lang="EN-US"}[上上线，但二层认证和三层认证却在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[上进行，在]{style="font-family:宋体"}[BAC]{lang="EN-US"}[上只进行密钥协商和下发]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当客户端在]{style="font-family:宋体"}[BAC]{lang="EN-US"}]{#struct_0_17471_x3053_136364937}[上线，在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[上统一做认证，则为集中式认证，又称分层认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当客户端在]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1035984058}[BAC]{lang="EN-US"}[上线，在]{style="font-family:宋体"}[BAC]{lang="EN-US"}[上做认证，则为分离式认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x2076296844}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x975458401}[配置在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[上进行用户接入认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_1920621991}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] user-authentication mode central]{lang="EN-US"}
:::::

::: {#1384255313 .myid}
[]{#_Toc404794984}[]{#struct_0_17471_x3053_x1294489536}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- wep key**

------------------------------------------------------------------------

[**[wep key]{lang="EN-US"}**]{#struct_0_17471_x3053_1863664214}[命令用来配置]{style="font-family:宋体"}[WEP]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[**[undo wep key]{lang="EN-US"}**]{#struct_0_17471_x3053_2086938101}[命令用来删除已配置的]{style="font-family:宋体"}[WEP]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_493274320}

[**[wep key]{lang="EN-US"}**[ *key-id* { **wep40** \| **wep104** \| **wep128** } { **pass-phrase** \| **raw-key** } { **cipher** \| **simple** } *key*]{lang="EN-US"}]{#struct_0_17471_x3053_x159615720}

[**[undo wep key]{lang="EN-US"}**[ *key-id*]{lang="EN-US"}]{#struct_0_17471_x3053_x1317360702}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1806779174}

[[未配置]{style="font-family:宋体"}[WEP]{lang="EN-US"}]{#struct_0_17471_x3053_837176761}[密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_721393043}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x1859392373}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x414460468}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1777062563}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x1098965438}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x556510239}

[*[key-id]{lang="EN-US"}*]{#struct_0_17471_x3053_878375530}[：密钥的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[wep40]{lang="EN-US"}**]{#struct_0_17471_x3053_442466489}[：设置]{style="font-family:宋体"}[WEP40]{lang="EN-US"}[密钥选项。]{style="font-family:宋体"}

[**[wep104]{lang="EN-US"}**]{#struct_0_17471_x3053_x136491728}[：设置]{style="font-family:宋体"}[WEP104]{lang="EN-US"}[密钥选项。]{style="font-family:宋体"}

[**[wep128]{lang="EN-US"}**]{#struct_0_17471_x3053_1803382266}[：设置]{style="font-family:宋体"}[WEP128]{lang="EN-US"}[密钥选项。]{style="font-family:宋体"}

[**[pass-phrase]{lang="EN-US"}**]{#struct_0_17471_x3053_x525911339}[：表示共享密钥为字符串。]{style="font-family:宋体"}

[**[raw-key]{lang="EN-US"}**]{#struct_0_17471_x3053_763197016}[：表示共享密钥为十六进制数。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_17471_x3053_x1494680449}[：以密文方式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_17471_x3053_x1961105864}[：以明文方式设置密钥。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_17471_x3053_x1461860486}[：设置明文密钥或密文密钥，区分大小写。明文密钥的长度范围和选择的密钥参数有关。具体关系如下。密文密钥为]{style="font-family:宋体"}[37]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}**[wep40 pass-phrase]{lang="EN-US"}**]{#struct_0_17471_x3053_1302140667}[，密钥是]{style="font-family:宋体"}[5]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}**[wep104 pass-phrase]{lang="EN-US"}**]{#struct_0_17471_x3053_x1003936819}[，密钥是]{style="font-family:宋体"}[13]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}**[wep128 pass-phrase]{lang="EN-US"}**]{#struct_0_17471_x3053_x2115185038}[，密钥是]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}**[wep40 raw-key]{lang="EN-US"}**]{#struct_0_17471_x3053_x948616689}[，密钥是]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}**[wep104 raw-key]{lang="EN-US"}**]{#struct_0_17471_x3053_239031798}[，密钥是]{style="font-family:宋体"}[26]{lang="EN-US"}[个]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}**[wep128 raw-key]{lang="EN-US"}**]{#struct_0_17471_x3053_x2096840660}[，密钥是]{style="font-family:宋体"}[32]{lang="EN-US"}[个]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1863664212}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_17471_x3053_2087331317}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文设置密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_17471_x3053_x697114904}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最多可以配置四个]{style="font-family:宋体"}]{#struct_0_17471_x3053_x335551395}[WEP]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1690892301}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_x634098066}[配置加密套件为]{style="font-family:宋体"}[WEP40]{lang="EN-US"}[，并配置]{style="font-family:宋体"}[WEP40]{lang="EN-US"}[密钥为明文]{style="font-family:宋体"}[12345]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_922125956}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] wep key 1 wep40 pass-phrase simple 12345]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x214340833}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher-suite]{lang="EN-US"}**]{#struct_0_17471_x3053_x386608577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wep key-id]{lang="EN-US"}**]{#struct_0_17471_x3053_912171093}
:::

::: {#-1199766313 .myid}
[]{#_Toc404794985}[]{#struct_0_17471_x3053_168120714}

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- wep key-id**

------------------------------------------------------------------------

[**[wep key-id]{lang="EN-US"}**]{#struct_0_17471_x3053_x380512888}[命令用来配置密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo wep key-id]{lang="EN-US"}**]{#struct_0_17471_x3053_x1041736803}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1873077602}

[**[wep key-id]{lang="EN-US"}**[ { **1** \| **2** \| **3** \| **4** }]{lang="EN-US"}]{#struct_0_17471_x3053_x1037707134}

[**[undo wep key-id]{lang="EN-US"}**]{#struct_0_17471_x3053_1792855115}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1863664213}

[[密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17471_x3053_2087265781}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17471_x3053_856928702}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_17471_x3053_x2095342127}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1279720088}

[[network-admin]{lang="EN-US"}]{#struct_0_17471_x3053_1815252327}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17471_x3053_x547414993}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17471_x3053_1135754986}

[**[1]{lang="EN-US"}**]{#struct_0_17471_x3053_x327794106}[：选择密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2]{lang="EN-US"}**]{#struct_0_17471_x3053_15806223}[：选择密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[3]{lang="EN-US"}**]{#struct_0_17471_x3053_x1910014339}[：选择密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[4]{lang="EN-US"}**]{#struct_0_17471_x3053_1503911109}[：选择密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17471_x3053_395417437}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只能在无线服务模板处于关闭的状态下进行配置。当配置了多个密钥，可以通过配置密钥]{style="font-family:宋体"}]{#struct_0_17471_x3053_642468363}[ID]{lang="EN-US"}[选择要使用的加密密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果使用]{style="font-family:宋体"}]{#struct_0_17471_x3053_x619089147}[RSNA]{lang="EN-US"}[安全机制，密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[不能为]{style="font-family:宋体"}[1]{lang="EN-US"}[，需要配置其它密钥索引值。因为]{style="font-family:宋体"}[RSN]{lang="EN-US"}[和]{style="font-family:宋体"}[WPA]{lang="EN-US"}[协商的密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[将为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在配置了与密钥长度相对应的]{style="font-family:宋体"}]{#struct_0_17471_x3053_114787299}[WEP]{lang="EN-US"}[加密套件时，指定]{style="font-family:宋体"}[ID]{lang="EN-US"}[的密钥才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17471_x3053_2075591153}

[[\# ]{lang="EN-US"}]{#struct_0_17471_x3053_1863664210}[配置]{style="font-family:宋体"}[WEP40]{lang="EN-US"}[加密套件，]{style="font-family:宋体"}[WEP40]{lang="EN-US"}[密钥为明文]{style="font-family:宋体"}[12345]{lang="EN-US"}[，配置密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17471_x3053_2087200245}

[\[Sysname\] wlan service-template security]{lang="EN-US"}

[\[Sysname-wlan-st-security\] cipher-suite wep40]{lang="EN-US"}

[\[Sysname-wlan-st-security\] wep key 1 wep40 pass-phrase simple 12345]{lang="EN-US"}

[\[Sysname-wlan-st-security\] wep key-id 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17471_x3053_x1080989013}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wep key]{lang="EN-US"}**]{#struct_0_17471_x3053_x1007857118}
:::
