::: {#-1008849225 .myid}
[]{#_Toc404786557}[]{#struct_0_12111_16510_2136340612}[]{#_Toc340136714}

**IRDP命令 \-- IRDP配置命令 \-- ip irdp**

------------------------------------------------------------------------

[**[ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_x2086991882}[命令用来使能接口的]{style="font-family:宋体"}[IRDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_x1047780294}[命令用来关闭接口的]{style="font-family:宋体"}[IRDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_942476324}

[**[ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_x1362120868}

[**[undo ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_1798083827}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12111_16510_1731066589}

[[接口的]{style="font-family:宋体"}[IRDP]{lang="EN-US"}]{#struct_0_12111_16510_631319516}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1306770158}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12111_16510_2117634478}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12111_16510_x600519851}

[[network-admin]{lang="EN-US"}]{#struct_0_12111_16510_580127416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12111_16510_713287054}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12111_16510_2098527393}

[[只有使能接口的]{style="font-family:宋体"}[IRDP]{lang="EN-US"}]{#struct_0_12111_16510_805159137}[功能，其他]{style="font-family:宋体"}[IRDP]{lang="EN-US"}[相关配置才生效，设备才会从该接口发送路由公告消息]{style="font-family:宋体"}[RA]{lang="EN-US"}[（]{style="font-family:宋体"}[Router Advertisements]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12111_16510_569362871}

[]{#_Toc130529683}[]{#_Toc69790677}[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_1624941463}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_x1513117863}[使能接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IRDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_2117568942}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip irdp]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_1678810531}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_x1838205951}[使能]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[IRDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_x493442773}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip irdp]{lang="EN-US"}
:::

::: {#-9230451 .myid}
[]{#_Toc404786558}[]{#struct_0_12111_16510_968375540}[]{#_Toc340136715}

**IRDP命令 \-- IRDP配置命令 \-- ip irdp address**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **irdp address**]{lang="EN-US"}]{#struct_0_12111_16510_x130753473}[命令用来配置接口代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip]{lang="EN-US"}**[ **irdp address** *ip-address*]{lang="EN-US"}]{#struct_0_12111_16510_x2079303856}[命令用来取消指定的接口代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip]{lang="EN-US"}**[ **irdp address**]{lang="EN-US"}]{#struct_0_12111_16510_173168633}[命令用来取消所有接口代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_1812212641}

[**[ip]{lang="EN-US"}**[ **irdp address** *ip-address preference-value*]{lang="EN-US"}]{#struct_0_12111_16510_2117503406}

[**[undo ip]{lang="EN-US"}**[ **irdp address** \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_12111_16510_1774820086}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12111_16510_x195087354}

[[未配置接口代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12111_16510_883071447}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12111_16510_x2113315794}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12111_16510_1206252333}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12111_16510_1662597875}

[[network-admin]{lang="EN-US"}]{#struct_0_12111_16510_x1177320606}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12111_16510_x1905646914}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12111_16510_2117437870}

[*[ip-address]{lang="EN-US"}*]{#struct_0_12111_16510_2097311170}[：代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为点分十进制格式，配置后接口发送的]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息中除了该接口自己的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，还包含这个代理公告]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[preference-value]{lang="EN-US"}*]{#struct_0_12111_16510_x169486613}[：代理公告的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的优先级，取值范围为]{lang="EN-US" style="font-family:宋体"}[-2147483648]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12111_16510_x623059739}

[[该命令支持重复配置，设备上接口最多支持配置]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_12111_16510_930748905}[个代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12111_16510_x540910980}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_x802418246}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_962565694}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.8]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[1600]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_x664573941}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip irdp address 192.168.0.8 1600]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_x868057351}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_2117372334}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.8]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[1600]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_x1758654772}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip irdp address 192.168.0.8 1600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1825514253}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_1625852346}
:::

::: {#-1014974331 .myid}
[]{#_Toc404786559}[]{#struct_0_12111_16510_x723182575}[]{#_Toc340136716}

**IRDP命令 \-- IRDP配置命令 \-- ip irdp lifetime**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **irdp lifetime**]{lang="EN-US"}]{#struct_0_12111_16510_x808064505}[命令用来配置接口公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的生命周期。]{style="font-family:宋体"}

[**[undo ip]{lang="EN-US"}**[ **irdp lifetime**]{lang="EN-US"}]{#struct_0_12111_16510_944816874}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_1554908827}

[**[ip]{lang="EN-US"}**[ **irdp lifetime** *lifetime-value*]{lang="EN-US"}]{#struct_0_12111_16510_x939276093}

[**[undo ip]{lang="EN-US"}**[ **irdp lifetime**]{lang="EN-US"}]{#struct_0_12111_16510_1784084658}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12111_16510_2118355374}

[[接口公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12111_16510_x807053873}[地址的生命周期为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12111_16510_335707104}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12111_16510_x1301174288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1163433722}

[[network-admin]{lang="EN-US"}]{#struct_0_12111_16510_x1394863244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12111_16510_178770820}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12111_16510_x2078551496}

[*[lifetime-value]{lang="EN-US"}*]{#struct_0_12111_16510_x1901507701}[：公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的生命周期，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[9000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12111_16510_1453169129}

[[配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12111_16510_2118289838}[地址的生命周期必须大于等于接口发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}[的最大时间间隔，否则，系统会提示配置错误。]{style="font-family:宋体"}

[[本配置对接口公告出去的所有]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12111_16510_1090070686}[地址（包括接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和代理公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12111_16510_x2144642907}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_x443734798}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_x336576754}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的生命周期为]{style="font-family:宋体"}[2000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_x1046873789}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip irdp lifetime 2000]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_733785418}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_1345071657}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的生命周期为]{style="font-family:宋体"}[2000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_2117831087}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip irdp lifetime 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_x594771191}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_x1325616717}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip irdp interval]{lang="EN-US"}**]{#struct_0_12111_16510_552313936}
:::

::: {#-2036105994 .myid}
[]{#_Toc404786560}[]{#struct_0_12111_16510_91896877}[]{#_Toc340136717}

**IRDP命令 \-- IRDP配置命令 \-- ip irdp interval**

------------------------------------------------------------------------

[**[ip irdp interval]{lang="EN-US"}**]{#struct_0_12111_16510_660588140}[命令用来配置接口发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}[的最大时间间隔和最小时间间隔。]{style="font-family:宋体"}

[**[undo ip irdp interval]{lang="EN-US"}**]{#struct_0_12111_16510_x475956217}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_527941255}

[**[ip irdp interval ]{lang="EN-US"}***[max-interval-value ]{lang="EN-US"}*[\[ *min-interval-value* \]]{lang="EN-US"}]{#struct_0_12111_16510_12717504}

[**[undo ip irdp interval]{lang="EN-US"}**]{#struct_0_12111_16510_x476109495}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1891374974}

[[接口发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12111_16510_2117765551}[的最大时间间隔为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒，最小时间间隔为最大时间间隔的]{style="font-family:宋体"}[0.75]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1374792103}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12111_16510_x1459334260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12111_16510_x351055934}

[[network-admin]{lang="EN-US"}]{#struct_0_12111_16510_295348895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12111_16510_x1960002071}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1457314574}

[*[max-interval-value]{lang="EN-US"}*]{#struct_0_12111_16510_1692152289}[：发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}[的最大时间间隔，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[min-interval-value]{lang="EN-US"}]{#struct_0_12111_16510_x1916965041}[：发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}[的最小时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[max-interval-value]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12111_16510_x160032951}

[[发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12111_16510_2117700015}[时，设备在最小时间间隔与最大时间间隔之间随机选取一个值作为周期性发送]{style="font-family:宋体"}[RA]{lang="EN-US"}[的时间间隔。]{style="font-family:宋体"}

[[接口发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12111_16510_2136406148}[的最大时间间隔必须小于等于接口公告的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的生命周期。如果配置的最大时间间隔大于生命周期，那么系统会将生命周期自动调整为最大时间间隔的]{style="font-family:宋体"}[3]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12111_16510_x2049892380}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_2010058122}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_x852124290}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}[的最大时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_x990503021}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip irdp interval 500 300]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_x293222349}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_341720137}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[发送周期性]{style="font-family:宋体"}[RA]{lang="EN-US"}[的最大时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_902334403}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip irdp interval 500 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_2117634479}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_x600585387}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip irdp lifetime]{lang="EN-US"}**]{#struct_0_12111_16510_1718368337}
:::

::: {#-1267580367 .myid}
[]{#_Toc404786561}[]{#struct_0_12111_16510_x480073188}[]{#_Toc340136718}

**IRDP命令 \-- IRDP配置命令 \-- ip irdp multicast**

------------------------------------------------------------------------

[**[ip irdp multicast]{lang="EN-US"}**]{#struct_0_12111_16510_1334824803}[命令用来配置接口发送组播]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息，报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[224.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ip irdp multicast]{lang="EN-US"}**]{#struct_0_12111_16510_1094861223}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_724165388}

[**[ip irdp multicast]{lang="EN-US"}**]{#struct_0_12111_16510_x441731961}

[**[undo ip irdp multicast]{lang="EN-US"}**]{#struct_0_12111_16510_x1756985846}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12111_16510_386080551}

[[接口发送广播]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_12111_16510_1439666408}[消息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12111_16510_2117568943}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12111_16510_1678876067}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12111_16510_89059238}

[[network-admin]{lang="EN-US"}]{#struct_0_12111_16510_417374306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12111_16510_x824339194}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12111_16510_1334319731}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_1001145726}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_x1731958064}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送组播]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_x982434030}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip irdp multicast]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_599201623}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_2117503407}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[发送组播]{style="font-family:宋体"}[RA]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_1774885622}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip irdp multicast]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_x194407983}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_x1413309752}
:::

::: {#13395786 .myid}
[]{#_Toc404786562}[]{#struct_0_12111_16510_633840859}[]{#_Toc340136719}

**IRDP命令 \-- IRDP配置命令 \-- ip irdp preference**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **irdp preference**]{lang="EN-US"}]{#struct_0_12111_16510_x842818573}[命令用来配置接口公告的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的优先级。]{style="font-family:宋体"}

[**[undo ip]{lang="EN-US"}**[ **irdp preference**]{lang="EN-US"}]{#struct_0_12111_16510_1589884583}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1397405475}

[**[ip]{lang="EN-US"}**[ **irdp preference** *preference-value*]{lang="EN-US"}]{#struct_0_12111_16510_x502006518}

[**[undo ip]{lang="EN-US"}**[ **irdp preference**]{lang="EN-US"}]{#struct_0_12111_16510_2117437871}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12111_16510_2097245634}

[[接口公告的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12111_16510_x954095174}[地址的优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1681151333}

[[接口视图]{style="font-family:宋体"}]{#struct_0_12111_16510_911532873}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12111_16510_1034078251}

[[network-admin]{lang="EN-US"}]{#struct_0_12111_16510_970701302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12111_16510_1964690648}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12111_16510_x170044538}

[*[preference-value]{lang="EN-US"}*]{#struct_0_12111_16510_x701770744}[：公告的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的优先级，取值范围为]{style="font-family:宋体"}[-2147483648]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12111_16510_1157034376}

[[接口公告的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12111_16510_2117372335}[地址的优先级值越大，优先级越高。最小的优先级值（]{style="font-family:宋体"}[-2147483648]{lang="EN-US"}[）表示主机不要使用这个地址作为缺省路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12111_16510_x1758720308}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_195408782}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_1878848726}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[公告的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_x1658089687}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip irdp preference 1]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12111_16510_368479071}

[[\# ]{lang="EN-US"}]{#struct_0_12111_16510_523857681}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[100]{lang="EN-US"}[公告的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12111_16510_2096110407}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ip irdp preference 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12111_16510_583683019}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip irdp]{lang="EN-US"}**]{#struct_0_12111_16510_2118355375}
:::
