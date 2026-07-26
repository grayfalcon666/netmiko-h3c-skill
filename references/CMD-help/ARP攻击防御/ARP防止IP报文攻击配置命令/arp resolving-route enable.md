::: {#1518958378 .myid}
[]{#_Toc132514839}[]{#_Toc115165136}[]{#_Toc112743116}[]{#_Toc107214363}[]{#_Toc183856433}[]{#_Toc134168955}[]{#_Toc105573997}[]{#_Toc105125657}[]{#_Toc100374966}[]{#_Toc258334056}[]{#_Toc404793885}[]{#struct_0_x1937_17589_1007357169}[]{#_Toc291056941}

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp resolving-route enable**

------------------------------------------------------------------------

[**[arp resolving-route enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x1711177252}[命令用来开启]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[黑洞路由功能。]{style="font-family:宋体"}

[**[undo arp resolving-route enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x100436152}[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[黑洞路由功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1550919013}

[**[arp resolving-route enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x1280122245}

[**[undo arp resolving-route enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1765546542}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1195052742}

[[不同型号的设备的缺省情况不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1937_17589_2053205883}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_724457844}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_398315145}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1757813903}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1013791571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x142507675}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2101332523}

[[建议在网关设备上配置本功能。]{style="font-family:宋体"}]{#struct_0_x1937_17589_55389586}

[[如果网络中有主机通过向设备发送大量目标]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1937_17589_669559211}[地址不能解析的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文来攻击设备，则会造成下面的危害：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备向目的网段发送大量]{style="font-family:宋体"}]{#struct_0_x1937_17589_684347693}[ARP]{lang="EN-US"}[请求报文，加重目的网段的负载。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备会试图反复地对目标]{style="font-family:宋体"}]{#struct_0_x1937_17589_724523380}[IP]{lang="EN-US"}[地址进行解析，增加了]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的负担。]{style="font-family:宋体"}

[[如果发送攻击报文的源不固定，可以采用]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_106804595}[黑洞路由功能。开启该功能后，一旦接收到目标]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能解析的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文，设备立即产生一个黑洞路由，使得设备在一段时间内将去往该地址的报文直接丢弃。等待黑洞路由老化时间过后，如有报文触发则再次发起解析，如果解析成功则进行转发，否则仍然产生一个黑洞路由将去往该地址的报文丢弃。这种方式能够有效地防止]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的攻击，减轻]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的负担。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_329751254}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_490235734}[开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[黑洞路由功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1976931179}

[\[Sysname\] arp resolving-route enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_445063388}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp resolving-route probe-count]{lang="EN-US"}**]{#struct_0_x1937_17589_x1222987013}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp resolving-route probe-interval]{lang="EN-US"}**]{#struct_0_x1937_17589_x1476817234}
:::

::: {#605354710 .myid}
[]{#_Toc404793886}[]{#struct_0_x1937_17589_2011147329}

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp resolving-route probe-count**

------------------------------------------------------------------------

[**[arp resolving-route probe-count]{lang="EN-US"}**]{#struct_0_x1937_17589_x1988072228}[命令用来配置发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的次数。]{style="font-family:宋体"}

[**[undo arp resolving-route probe-count]{lang="EN-US"}**]{#struct_0_x1937_17589_x1712495937}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_837101101}

[**[arp resolving-route probe-count]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_x1937_17589_1903811062}

[**[undo arp resolving-route probe-count]{lang="EN-US"}**]{#struct_0_x1937_17589_x771909757}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1453659797}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x253358382}[请求报文的次数为]{style="font-family:宋体"}[1]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1272670456}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_1962574945}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x361505666}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x583374802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x926935276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1053336551}

[*[count]{lang="EN-US"}*]{#struct_0_x1937_17589_471951759}[：指定]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的]{style="font-family:宋体"}[次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1926194392}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_676094286}[配置发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_1886199845}

[\[Sysname\] arp resolving-route probe-count 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x120633574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp resolving-route enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1204578275}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp resolving-route probe-interval]{lang="EN-US"}**]{#struct_0_x1937_17589_x184760294}
:::

::: {#-1001967113 .myid}
[]{#_Toc404793887}[]{#struct_0_x1937_17589_1948140822}

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp resolving-route probe-interval**

------------------------------------------------------------------------

[**[arp resolving-route probe-interval]{lang="EN-US"}**]{#struct_0_x1937_17589_2099659701}[命令用来配置发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的时间间隔。]{style="font-family:宋体"}

[**[undo arp resolving-route probe-interval]{lang="EN-US"}**]{#struct_0_x1937_17589_x318557445}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x520861923}

[**[arp resolving-route probe-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1937_17589_x2066647432}

[**[undo arp resolving-route probe-interval]{lang="EN-US"}**]{#struct_0_x1937_17589_486165034}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x2072625269}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1299964921}[请求报文的时间间隔是]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1524305080}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x1107573606}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x960751000}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1617597954}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x475236073}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_132627832}

[*[interval]{lang="EN-US"}*]{#struct_0_x1937_17589_x1595680520}[：指定发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[5]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_492486264}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1537410727}[配置发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的时间间隔为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_41778861}

[\[Sysname\] arp resolving-route probe-interval 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x2055675839}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp resolving-route enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1946040405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp resolving-route probe-count]{lang="EN-US"}**]{#struct_0_x1937_17589_736838614}
:::

::: {#993204650 .myid}
[]{#_Toc404793888}[]{#struct_0_x1937_17589_1698442180}[]{#_Toc258334057}

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp source-suppression enable**

------------------------------------------------------------------------

[**[arp source-suppression enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1175482106}[命令用来使能]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[源地址抑制功能。]{style="font-family:宋体"}

[**[undo arp source-suppression enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x171696711}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_724326772}

[**[arp source-suppression enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1370612489}

[**[undo arp source-suppression enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x48751101}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1743567207}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1857749973}[源地址抑制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2084088307}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x167786983}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648108271}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_563435168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1755344986}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_724392308}

[[建议在网关设备上配置本功能。]{style="font-family:宋体"}]{#struct_0_x1937_17589_1366210198}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1391219717}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x2068693125}[使能]{style="font-family:宋体"}[ARP]{lang="EN-US"}[源地址抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x725861571}

[\[Sysname\] arp source-suppression enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_989492853}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp source-suppression]{lang="EN-US"}**]{#struct_0_x1937_17589_x1500261691}
:::

::: {#1326292289 .myid}
[]{#_Toc404793889}[]{#struct_0_x1937_17589_1692338285}[]{#_Toc258334058}[]{#_Toc183856434}[]{#_Toc134168956}[]{#_Toc105573998}[]{#_Toc105125658}[]{#_Toc100374967}

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- arp source-suppression limit**

------------------------------------------------------------------------

[**[arp source-suppression limit]{lang="EN-US"}**]{#struct_0_x1937_17589_x1113934865}[命令用来配置]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[源抑制的阈值。]{style="font-family:宋体"}

[**[undo arp source-suppression limit]{lang="EN-US"}**]{#struct_0_x1937_17589_724719988}[命令用来恢复]{style="font-family:宋体"}[缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_635716524}

[**[arp source-suppression limit ]{lang="EN-US"}***[limit-value]{lang="EN-US"}*]{#struct_0_x1937_17589_288014376}

[**[undo arp source-suppression limit]{lang="EN-US"}**]{#struct_0_x1937_17589_961476079}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x698277150}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_774478362}[源抑制的阈值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_750040305}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_522228961}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1979595920}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_724785524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_345820555}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2121127233}

[*[limit-value]{lang="EN-US"}*]{#struct_0_x1937_17589_1699394144}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[源抑制的阈值，即设备在]{style="font-family:宋体"}[5]{lang="EN-US"}[秒间隔内可以处理的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[相同，但目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能解析的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的最大数目，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_744434495}

[[如果网络中每]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1937_17589_1924159368}[秒内从某]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址向设备某接口发送目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能解析的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文超过了设置的阈值，则设备将不再处理由此]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发出的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文直至该]{style="font-family:宋体"}[5]{lang="EN-US"}[秒结束，从而避免了恶意攻击所造成的危害。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_734874934}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_690766586}[配置]{style="font-family:宋体"}[ARP]{lang="EN-US"}[源抑制的阈值为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_724588916}

[\[Sysname\] arp source-suppression limit 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_792741069}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display arp source-suppression]{lang="EN-US"}**]{#struct_0_x1937_17589_x100787859}
:::

::: {#242549683 .myid}
[]{#_Toc404793890}[]{#struct_0_x1937_17589_1590382419}[]{#_Toc258334059}[]{#_Toc183856435}[]{#_Toc134168957}[]{#_Toc132514840}[]{#_Toc115165137}[]{#_Toc112743117}[]{#_Toc107214366}

**ARP攻击防御 \-- ARP防止IP报文攻击配置命令 \-- display arp source-suppression**

------------------------------------------------------------------------

[**[display arp source-suppression]{lang="EN-US"}**]{#struct_0_x1937_17589_865955736}[命令用来显示当前]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[源抑制的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1919873515}

[**[display arp source-suppression]{lang="EN-US"}**]{#struct_0_x1937_17589_x1434402708}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1582426324}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_651265643}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_932499376}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_724654452}

[[network-operator]{lang="EN-US"}]{#struct_0_x1937_17589_316430147}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1871200385}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1937_17589_1967600513}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1672172425}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_159981087}[显示当前]{style="font-family:宋体"}[ARP]{lang="EN-US"}[源抑制的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display arp source-suppression]{lang="EN-US"}]{#struct_0_x1937_17589_x2062985301}

[ ARP source suppression is enabled]{lang="EN-US"}

[ Current suppression limit: 100]{lang="EN-US"}

[]{#struct_0_x1937_17589_x228800772}[]{#_Toc138213026}[[表1-1 ]{lang="EN-US"}[display arp source-suppression]{lang="EN-US"}]{#_Toc105466682}[显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1754307480}[[字段]{style="font-family:黑体"}]{#struct_0_x1937_17589_724982132}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1937_17589_1706336241}

[[ARP source suppression is enabled]{lang="EN-US"}]{#struct_0_x1937_17589_1154288966}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_1668008493}[源地址抑制功能处于使能状态]{style="font-family:宋体"}

[[Current suppression limit]{lang="EN-US"}]{#struct_0_x1937_17589_x1540051220}

[[设备在]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1937_17589_x2133212527}[秒时间间隔内可以接收到的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[相同，但目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能解析的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的最大数目]{style="font-family:宋体"}

[]{#_Toc124244766}[]{#_Toc138154752}[]{#_Toc138154754}[]{#_Toc138154757}[]{#_Toc138154758}[]{#_Toc138154759}[]{#_Toc138154760}[]{#_Toc138154761}[]{#_Toc138154762}[]{#_Toc138154763}[]{#_Toc138154764}[]{#_Toc138154765}[]{#_Toc138154766}[]{#_Toc138154767}[]{#_Toc138154768}[]{#_Toc138154769}[ ]{lang="EN-US"}

::: {#-1909245689 .myid}
[]{#_Toc404793892}[]{#struct_0_x1937_17589_1007291633}[]{#_Toc258334061}

**ARP攻击防御 \-- ARP报文限速配置命令 \-- arp rate-limit**

------------------------------------------------------------------------

[**[arp rate-limit]{lang="EN-US"}**]{#struct_0_x1937_17589_x1690330940}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文限速功能。]{style="font-family:宋体"}

[**[undo arp rate-limit]{lang="EN-US"}**]{#struct_0_x1937_17589_1261419604}[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文限速功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1237394187}

[**[arp]{lang="EN-US"}**[ **rate-limit** \[ *pps* \]]{lang="EN-US"}]{#struct_0_x1937_17589_1532379850}

[**[undo arp rate-limit]{lang="EN-US"}**]{#struct_0_x1937_17589_648299901}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_724457841}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_398315142}[报文限速功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1757813906}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1937_17589_x1773306458}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1536729782}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1901741310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1290246181}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1927200227}

[*[pps]{lang="EN-US"}*]{#struct_0_x1937_17589_1856560884}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[限速速率，单位为包每秒（]{style="font-family:宋体"}[pps]{lang="EN-US"}[）。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x95097147}

[[不指定限速速率时，设备使用缺省限速速率，超过限速部分的报文会被丢弃。缺省限速速率和设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1937_17589_1277591118}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_724523377}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_444511608}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文限速为]{style="font-family:宋体"}[50pps]{lang="EN-US"}[，超过限速部分的报文被丢弃。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_729576152}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp rate-limit 50]{lang="EN-US"}
:::

::: {#1257076006 .myid}
[]{#_Toc404793893}[]{#struct_0_x1937_17589_179227077}

**ARP攻击防御 \-- ARP报文限速配置命令 \-- arp rate-limit log enable**

------------------------------------------------------------------------

[**[arp rate-limit log enable]{lang="EN-US"}**]{#struct_0_x1937_17589_585586929}[命令用来开启]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[报文限速日志功能，如果设备收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的速率超过用户设定的限速值，则生成日志信息。]{style="font-family:宋体"}

[**[undo arp rate-limit log enable]{lang="EN-US"}**]{#struct_0_x1937_17589_724326769}[命令用来关闭]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[报文限速日志功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x585702642}

[**[arp rate-limit log enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x1477813286}

[**[undo arp rate-limit log enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1698580656}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1179756540}

[[设备的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x2099356964}[报文限速日志功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x764624876}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x702811148}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_724392305}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1366210203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x565816306}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1139374937}

[[当开启了]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_297903642}[限速日志功能后，设备将这个时间间隔内的超速峰值作为日志的速率值发送到设备的信息中心，通过设置信息中心的参数，最终决定日志报文的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的设置请参见"网络管理和监控配置指导"中的"信息中心"）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_957472105}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1519115821}[开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文限速日志功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x726637864}

[\[Sysname\] arp rate-limit log enable]{lang="EN-US"}
:::

::: {#-561796095 .myid}
[]{#_Toc404793894}[]{#struct_0_x1937_17589_x636121856}

**ARP攻击防御 \-- ARP报文限速配置命令 \-- arp rate-limit log interval**

------------------------------------------------------------------------

[**[arp rate-limit log interval]{lang="EN-US"}**]{#struct_0_x1937_17589_724719985}[命令用来配置当设备收到的]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[报文速率超过用户设定的限速值时，设备发送告警或日志的时间间隔。]{style="font-family:
宋体"}

[**[undo arp rate-limit log interval]{lang="EN-US"}**]{#struct_0_x1937_17589_635716513}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1668300767}

[**[arp rate-limit log interval ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x1937_17589_x1822831818}

[**[undo arp rate-limit log interval]{lang="EN-US"}**]{#struct_0_x1937_17589_x685487874}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_943628993}

[[当设备收到的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_724785521}[报文速率超过用户设定的限速值时，设备发送告警或日志的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_345820550}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_2121127238}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1698673248}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_22346389}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1770695127}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1219924627}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1937_17589_724588913}[：当端口上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文速率超过用户设定的限速值时，设备发送告警或日志的时间间隔。]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_792741064}

[[用户需要先开启发送告警或日志功能，然后配置此命令指定设备发送告警或日志的时间间隔，同时本命令必须和端口下的]{style="font-family:宋体"}**[arp rate-limit]{lang="EN-US"}**]{#struct_0_x1937_17589_x100787854}[命令配合使用，单独配置本命令无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1590054739}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_724654449}[当设备收到的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文速率超过用户设定的限速值时，配置设备发送告警或日志的时间间隔为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x2022222006}

[\[Sysname\] arp rate-limit log interval 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1114535729}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp rate-limit]{lang="EN-US"}**]{#struct_0_x1937_17589_x895589807}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp rate-limit log enable]{lang="EN-US"}**]{#struct_0_x1937_17589_530648211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent trap ]{lang="EN-US"}**]{#struct_0_x1937_17589_1060776499}**[enable ]{lang="EN-US"}[arp]{lang="EN-US"}**
:::

::: {#1012942901 .myid}
[]{#_Toc404793895}[]{#struct_0_x1937_17589_1316884230}[]{#_Toc352688165}

**ARP攻击防御 \-- ARP报文限速配置命令 \-- snmp-agent trap enable arp**

------------------------------------------------------------------------

[**[snmp-agent trap enable arp]{lang="EN-US"}**]{#struct_0_x1937_17589_724982129}[命令用来开启]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable arp]{lang="EN-US"}**]{#struct_0_x1937_17589_x249978902}[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_473282187}

[**[snmp-agent trap enable arp ]{lang="EN-US"}**[\[ **rate-limit** \]]{lang="EN-US"}]{#struct_0_x1937_17589_135236113}

[**[undo snmp-agent trap enable arp ]{lang="EN-US"}**[\[ **rate-limit** \]]{lang="EN-US"}]{#struct_0_x1937_17589_x279924580}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_725047665}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x294629632}[模块的告警功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1006963953}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x1674596819}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1030988168}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x469419858}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_724457842}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_398315143}

[**[rate-limit]{lang="EN-US"}**]{#struct_0_x1937_17589_x1757813905}[：启动]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文限速的告警功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x207222517}

[[当开启了]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_724523378}[模块的告警功能后，设备将这个时间间隔内的超速峰值作为告警信息发送出去，生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关特性。]{style="font-family:宋体"}

[[有关告警信息的详细描述，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1937_17589_x1139374938}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_444511611}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x1609076017}[启动]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文限速的告警功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1724451800}

[\[Sysname\] snmp-agent trap enable arp rate-limit]{lang="EN-US"}
:::

::: {#1937861755 .myid}
[]{#_Toc404793897}[]{#struct_0_x1937_17589_1370612487}[]{#_Toc258334065}[]{#_Toc189817044}

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac**

------------------------------------------------------------------------

[**[arp source-mac]{lang="EN-US"}**]{#struct_0_x1937_17589_x49668605}[命令用来开启源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测功能，并选择检查模式。]{style="font-family:宋体"}

[**[undo arp source-mac]{lang="EN-US"}**]{#struct_0_x1937_17589_677973920}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1253442297}

[**[arp source-mac ]{lang="EN-US"}**[{ **filter** \| **monitor** }]{lang="EN-US"}]{#struct_0_x1937_17589_x222917378}

[**[undo arp source-mac ]{lang="EN-US"}**[\[ **filter** \| **monitor** \]]{lang="EN-US"}]{#struct_0_x1937_17589_x713192163}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1976559841}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1937_17589_676469485}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_724392306}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_1366210204}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x565881842}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_607688286}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_327877054}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1556075348}

[**[filter]{lang="EN-US"}**]{#struct_0_x1937_17589_1069272367}[：检测到攻击后，打印]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息，同时对该源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文进行过滤。]{style="font-family:宋体"}

[**[monitor]{lang="EN-US"}**]{#struct_0_x1937_17589_x15844026}[：检测到攻击后，只打印]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息，不对该源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文进行过滤。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_991359631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[建议在网关设备上开启本功能。]{style="font-family:宋体"}]{#struct_0_x1937_17589_724719986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启源]{style="font-family:宋体"}]{#struct_0_x1937_17589_635716514}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测之后，该特性会对上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文按照源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[进行统计。当在一定时间（]{style="font-family:宋体"}[5]{lang="EN-US"}[秒）内收到某固定源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文超过设定的阈值，不同模式的处理方式存在差异：在]{style="font-family:宋体"}**[filter]{lang="EN-US"}**[模式下会打印]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息并对该源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文进行过滤；在]{style="font-family:宋体"}**[monitor]{lang="EN-US"}**[模式下只打印]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息，不过滤]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1937_17589_x1668300760}**[undo ]{lang="EN-US"}[arp source-mac]{lang="EN-US"}**[命令中没有指定检查模式，则关闭任意检查模式的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_906051537}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1322432595}[开启源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测功能，并选择]{style="font-family:宋体"}**[filter]{lang="EN-US"}**[检查模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_1813257369}

[\[Sysname\] arp source-mac filter]{lang="EN-US"}
:::

::: {#713870996 .myid}
[]{#_Toc189817045}[]{#_Toc404793898}[]{#struct_0_x1937_17589_x1983022588}[]{#_Toc258334066}[]{#_Toc189817046}

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac aging-time**

------------------------------------------------------------------------

[**[arp source-mac aging-time]{lang="EN-US"}**]{#struct_0_x1937_17589_1560441004}[命令用来配置源]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项的老化时间。]{style="font-family:宋体"}

[**[undo arp source-mac aging-time]{lang="EN-US"}**]{#struct_0_x1937_17589_724785522}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_345820549}

[**[arp source-mac aging-time ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_x1937_17589_x217524915}

[**[undo arp source-mac aging-time]{lang="EN-US"}**]{#struct_0_x1937_17589_x571038485}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x922985286}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1937_17589_528720884}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项的老化时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒，即]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_328384980}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x545637045}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1047672180}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_724588914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_792741071}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1855527285}

[*[time]{lang="EN-US"}*]{#struct_0_x1937_17589_464778297}[：源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项的老化时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[6000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1943517692}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_896327670}[配置源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项的老化时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_1473784121}

[\[Sysname\] arp source-mac aging-time 60]{lang="EN-US"}
:::

::: {#2113347529 .myid}
[]{#_Toc404793899}[]{#struct_0_x1937_17589_641140500}[]{#_Toc258334067}

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac exclude-mac**

------------------------------------------------------------------------

[**[arp source-mac exclude-mac]{lang="EN-US"}**]{#struct_0_x1937_17589_850609389}[命令用来配置保护]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址。当配置了保护]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址之后，即使该]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址存在攻击也不会被检测过滤。]{style="font-family:宋体"}

[**[undo arp source-mac exclude-mac]{lang="EN-US"}**]{#struct_0_x1937_17589_724654450}[命令用来取消配置的保护]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_316430145}

[**[arp source-mac exclude-mac ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*[&\<1-n\>]{lang="EN-US"}]{#struct_0_x1937_17589_x1871200383}

[**[undo arp source-mac exclude-mac]{lang="EN-US"}**[ \[ *mac-address*&\<1-n\> \]]{lang="EN-US"}]{#struct_0_x1937_17589_x1164567369}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1150414259}

[[没有配置任何保护]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1937_17589_x33205473}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_25497412}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x525621164}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_391345718}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_724982130}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1706336243}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1154420038}

[*[mac-address]{lang="EN-US"}*[&\<1-n\>]{lang="EN-US"}]{#struct_0_x1937_17589_523445390}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表。其中，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[表示配置的保护]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-n\>]{lang="EN-US"}[表示每次最多可以配置的保护]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址个数。]{style="font-family:宋体"}[n]{lang="EN-US"}[的取值范围和设备相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_102594870}

[[如果]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x1937_17589_x355412079}[命令中没有指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，则取消所有已配置的保护]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x7796392}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x1027798447}[配置源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检查的保护]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2-2-2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_725047666}

[\[Sysname\] arp source-mac exclude-mac 2-2-2]{lang="EN-US"}
:::

::: {#-1576643052 .myid}
[]{#_Toc404793900}[]{#struct_0_x1937_17589_x294629633}[]{#_Toc258334068}[]{#_Toc189817047}

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- arp source-mac threshold**

------------------------------------------------------------------------

[**[arp source-mac threshold]{lang="EN-US"}**]{#struct_0_x1937_17589_1006898417}[命令用来配置源]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文攻击检测阈值，当在固定的时间（]{style="font-family:宋体"}[5]{lang="EN-US"}[秒）内收到源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文超过该阈值则认为存在]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文攻击。]{style="font-family:宋体"}

[**[undo arp source-mac threshold]{lang="EN-US"}**]{#struct_0_x1937_17589_1359398841}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x404239864}

[**[arp source-mac threshold ]{lang="EN-US"}***[threshold-value]{lang="EN-US"}*]{#struct_0_x1937_17589_1253771821}

[**[undo arp source-mac threshold]{lang="EN-US"}**]{#struct_0_x1937_17589_1133359127}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_886654333}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1937_17589_x2076390686}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648195150}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_1094629915}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1568358135}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1498656531}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1417789026}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1800958396}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1937_17589_x2034317404}[：固定时间内源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文攻击检测的阈值，单位为报文个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_286784230}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x873320583}[配置源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文攻击检测阈值为]{style="font-family:宋体"}[30]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1648129614}

[\[Sysname\] arp source-mac threshold 30]{lang="EN-US"}
:::

::: {#510932598 .myid}
[]{#_Toc404793901}[]{#struct_0_x1937_17589_550111425}[]{#_Toc258334069}[]{#_Toc189817048}

**ARP攻击防御 \-- 源MAC地址固定的ARP攻击检测配置命令 \-- display arp source-mac**

------------------------------------------------------------------------

[**[display arp source-mac]{lang="EN-US"}**]{#struct_0_x1937_17589_x1849039571}[命令用来显示检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x559979651}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1937_17589_x864410843}

[**[display arp source-mac ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1937_17589_x1884217016}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1937_17589_x224574764}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display arp source-mac ]{lang="EN-US"}**[{ **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_x1937_17589_x45666609}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1937_17589_1519466288}[模式：]{style="font-family:宋体"}

[**[display arp source-mac ]{lang="EN-US"}**[{ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \| **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_x1937_17589_x1648326222}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1457208217}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x2132373872}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2066148361}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1766957580}

[[network-operator]{lang="EN-US"}]{#struct_0_x1937_17589_x509312279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_358352867}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1937_17589_x1702376835}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1363350594}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1937_17589_x1648260686}[：显示指定接口检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示指定接口的类型和编号。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1937_17589_557281499}[：显示指定单板检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[所在的槽位号。如果未指定本参数，则显示主用主控板检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1937_17589_x1481313025}[：显示指定成员设备检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1937_17589_802602523}[：显示指定成员设备检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1937_17589_767635774}[：显示指定成员设备上指定单板检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板]{style="font-family:宋体"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1937_17589_753725335}[：显示指定单板检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1937_17589_x94835005}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_973499898}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1551292635}[显示检测到的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测表项。]{style="font-family:宋体"}

[[\<Sysname\> display arp source-mac]{lang="EN-US"}]{#struct_0_x1937_17589_x1647933006}

[Source-MAC          VLAN ID  Interface                Aging-time]{lang="EN-US"}

[23f3-1122-3344      4094     GE1/0/1                  10]{lang="SV"}

[23f3-1122-3355      4094     GE1/0/2                  30]{lang="SV"}

[23f3-1122-33ff      4094     GE1/0/3                  25]{lang="SV"}

[23f3-1122-33ad      4094     GE1/0/4                  30]{lang="SV"}

[23f3-1122-33ce      4094     GE1/0/5                  2]{lang="SV"}

[]{#struct_0_x1937_17589_1275416039}[[表1-2 ]{lang="EN-US"}[display arp source-mac]{lang="EN-US"}]{#_Toc182191693}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1753617976}[[字段]{style="font-family:黑体"}]{#struct_0_x1937_17589_279310374}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1937_17589_x2124616203}

[[Source-MAC]{lang="EN-US"}]{#struct_0_x1937_17589_1702312592}

[[检测到攻击的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1937_17589_x510969139}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x1937_17589_241763135}

[[检测到攻击的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1937_17589_x1647867470}

[[Interface]{lang="EN-US"}]{#struct_0_x1937_17589_941274326}

[[攻击来源的接口]{style="font-family:宋体"}]{#struct_0_x1937_17589_1531954433}

[[Aging-time]{lang="EN-US"}]{#struct_0_x1937_17589_1971995016}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_597660082}[防攻击策略表项老化剩余时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1174845837 .myid}
[]{#_Toc404793903}[]{#struct_0_x1937_17589_1180916243}[]{#_Toc258334071}[]{#_Toc189817050}

**ARP攻击防御 \-- ARP报文源MAC地址一致性检查配置命令 \-- arp valid-check enable**

------------------------------------------------------------------------

[**[arp valid-check enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x1721802875}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能。]{style="font-family:宋体"}

[**[undo arp valid-check enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x2115078924}[命令用来关闭]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1323893607}

[**[arp valid-check enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x171470679}

[**[undo arp valid-check enable]{lang="EN-US"}**]{#struct_0_x1937_17589_93192836}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1743742847}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1647998542}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x314203410}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_2109502505}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1459367510}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1367471352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x151599138}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_328606374}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x876283311}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能主要应用于网关设备。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1912506761}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能后，设备会对接收的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文进行检查，如果以太网数据帧首部中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不同，则丢弃该报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1153800648}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x1647670862}[使能]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致性检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_1497279719}

[\[Sysname\] arp valid-check enable]{lang="EN-US"}
:::

::: {#1167596295 .myid}
[]{#_Toc404793905}[]{#struct_0_x1937_17589_x1511705009}[]{#_Toc258334073}

**ARP攻击防御 \-- ARP主动确认配置命令 \-- arp active-ack enable**

------------------------------------------------------------------------

[**[arp active-ack enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1380357082}[命令用来使能]{style="font-family:宋体"}[ARP]{lang="EN-US"}[主动确认功能。]{style="font-family:宋体"}

[**[undo arp active-ack enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1255134558}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1647605326}

[**[arp active-ack ]{lang="EN-US"}**[\[ **strict** \] **enable**]{lang="EN-US"}]{#struct_0_x1937_17589_x1578585071}

[**[undo arp active-ack ]{lang="EN-US"}**[\[ **strict** \] **enable**]{lang="EN-US"}]{#struct_0_x1937_17589_x1405894890}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1161259237}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_1839249350}[主动确认功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1178450531}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x171585644}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x316907467}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_408373143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1648195149}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x115158130}

[**[strict]{lang="EN-US"}**]{#struct_0_x1937_17589_x129141007}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[主动确认功能的严格模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x427199120}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_1201216070}[的主动确认功能主要应用于网关设备，防止攻击者仿冒用户欺骗网关设备。通过]{style="font-family:宋体"}**[strict]{lang="EN-US"}**[参数使能或关闭主动确认的严格模式。使能严格模式后，]{style="font-family:宋体"}[ARP]{lang="EN-US"}[主动确认功能执行更严格的检查，新建]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项前，需要本设备先对其]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发起]{style="font-family:宋体"}[ARP]{lang="EN-US"}[解析，解析成功后才能触发正常的主动确认流程，在主动确认流程成功后，才允许设备学习该表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1256590691}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1982211191}[使能]{style="font-family:宋体"}[ARP]{lang="EN-US"}[主动确认功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x958206906}

[\[Sysname\] arp active-ack enable]{lang="EN-US"}
:::

::: {#246244226 .myid}
[]{#_Toc404793907}[]{#struct_0_x1937_17589_x357094508}[]{#_Toc258334075}

**ARP攻击防御 \-- 授权ARP配置命令 \-- arp authorized enable**

------------------------------------------------------------------------

[**[arp authorized enable]{lang="EN-US"}**]{#struct_0_x1937_17589_272637753}[命令用来使能接口下的授权]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo arp authorized enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x306269661}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x153089491}

[**[arp authorized enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x589356583}

[**[undo arp authorized enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1760767446}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648326221}

[[接口下的授权]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1053923690}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1225784611}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1937_17589_100628585}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x532387018}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_627868799}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1482317148}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x371075742}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1511808872}[使能接口下授权]{style="font-family:宋体"}[ARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1648260685}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp authorized enable]{lang="EN-US"}[]{#_Toc248654956}[]{#_Toc248727072}[]{#_Toc250623547}[]{#_Toc251853203}[]{#_Toc248654957}[]{#_Toc248727073}[]{#_Toc250623548}[]{#_Toc251853204}[]{#_Toc248654959}[]{#_Toc248727075}[]{#_Toc250623550}[]{#_Toc251853206}[]{#_Toc248654960}[]{#_Toc248727076}[]{#_Toc250623551}[]{#_Toc251853207}[]{#_Toc248654961}[]{#_Toc248727077}[]{#_Toc250623552}[]{#_Toc251853208}[]{#_Toc248654962}[]{#_Toc248727078}[]{#_Toc250623553}[]{#_Toc251853209}[]{#_Toc248654963}[]{#_Toc248727079}[]{#_Toc250623554}[]{#_Toc251853210}[]{#_Toc248654964}[]{#_Toc248727080}[]{#_Toc250623555}[]{#_Toc251853211}[]{#_Toc248654965}[]{#_Toc248727081}[]{#_Toc250623556}[]{#_Toc251853212}[]{#_Toc248654966}[]{#_Toc248727082}[]{#_Toc250623557}[]{#_Toc251853213}[]{#_Toc248654967}[]{#_Toc248727083}[]{#_Toc250623558}[]{#_Toc251853214}[]{#_Toc248654968}[]{#_Toc248727084}[]{#_Toc250623559}[]{#_Toc251853215}[]{#_Toc248654969}[]{#_Toc248727085}[]{#_Toc250623560}[]{#_Toc251853216}[]{#_Toc248654972}[]{#_Toc248727088}[]{#_Toc250623563}[]{#_Toc251853219}
:::

::: {#-1802637666 .myid}
[]{#_Toc404793909}[]{#struct_0_x1937_17589_940488958}[]{#_Toc258334078}[]{#_Toc183856442}[]{#_Toc162773007}

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp detection enable**

------------------------------------------------------------------------

[**[arp detection enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1577671653}[命令用来使能]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能，即对]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文进行用户合法性检查。]{style="font-family:宋体"}

[**[undo arp detection enable]{lang="EN-US"}**]{#struct_0_x1937_17589_1429127206}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1278820570}

[**[arp detection enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x1647933005}

[**[undo arp detection enable]{lang="EN-US"}**]{#struct_0_x1937_17589_872131512}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1672540150}

[[ARP Detection]{lang="EN-US"}]{#struct_0_x1937_17589_2098410590}[功能处于关闭状态，即不进行用户合法性检查。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1991134377}

[[VLAN]{lang="EN-US"}]{#struct_0_x1937_17589_463153917}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_418984062}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x704683771}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x638419701}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1647867469}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x1431444205}[使能]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_2070566023}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] arp detection enable]{lang="EN-US"}[]{#_Toc183856443}[]{#_Toc162773008}[]{#_Toc209866593}[]{#_Toc209866594}[]{#_Toc209866595}[]{#_Toc209866596}[]{#_Toc209866597}[]{#_Toc209866598}[]{#_Toc209866599}[]{#_Toc209866600}[]{#_Toc209866601}[]{#_Toc209866602}[]{#_Toc209866603}[]{#_Toc209866604}[]{#_Toc209866605}[]{#_Toc209866606}[]{#_Toc209866607}[]{#_Toc209866608}[]{#_Toc209866609}[]{#_Toc209866610}[]{#_Toc209866611}[]{#_Toc209866612}[]{#_Toc209866613}
:::

::: {#-844016401 .myid}
[]{#_Toc404793910}[]{#struct_0_x1937_17589_x907942839}[]{#_Toc258334079}

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp detection trust**

------------------------------------------------------------------------

[**[arp detection trust]{lang="EN-US"}**]{#struct_0_x1937_17589_1687095440}[命令用来配置接口为]{style="font-family:宋体"}[ARP]{lang="EN-US"}[信任接口。]{style="font-family:宋体"}

[**[undo arp detection trust]{lang="EN-US"}**]{#struct_0_x1937_17589_x1149452676}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2072289760}

[**[arp detection trust]{lang="EN-US"}**]{#struct_0_x1937_17589_x966783285}

[**[undo arp detection trust]{lang="EN-US"}**]{#struct_0_x1937_17589_x1648064077}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1584200770}

[[接口为]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_475101110}[非信任接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x438002830}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1937_17589_x10695962}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x28701896}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x2008113364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_201128807}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1878302005}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x1647998541}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为]{style="font-family:宋体"}[ARP]{lang="EN-US"}[信任接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_1251880531}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp detection trust]{lang="EN-US"}
:::

::: {#-444899579 .myid}
[]{#_Toc404793911}[]{#struct_0_x1937_17589_2009408522}[]{#_Toc258334080}[]{#_Toc183856444}[]{#_Toc162773009}

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp detection validate**

------------------------------------------------------------------------

[**[arp detection validate]{lang="EN-US"}**]{#struct_0_x1937_17589_x1107247929}[命令用来使能对]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址或源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的有效性检查。使能有效性检查时可以指定某一种检查方式也可以配置成多种检查方式的组合。]{style="font-family:宋体"}

[**[undo arp detection validate]{lang="EN-US"}**]{#struct_0_x1937_17589_x2112973047}[命令用来关闭对]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[报文的有效性检查。关闭时可以指定关闭某一种或多种检查，在不指定检查方式时，表示关闭所有有效性检查。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_502965514}

[**[arp detection validate ]{lang="EN-US"}**[{ **dst-mac** \| **ip** \| **src-mac** } \*]{lang="EN-US"}]{#struct_0_x1937_17589_x587348523}

[**[undo arp detection validate ]{lang="EN-US"}**[\[ **dst-mac** \| **ip** \| **src-mac** \] \*]{lang="EN-US"}]{#struct_0_x1937_17589_x350117938}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1277509176}

[[不同型号的设备支持的缺省情况不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1937_17589_x1647670861}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1093995192}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_1603384672}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1532365191}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1767311536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x823736186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1515133005}

[**[dst-mac]{lang="EN-US"}**]{#struct_0_x1937_17589_1983751988}[：检查]{style="font-family:宋体"}[ARP]{lang="EN-US"}[应答报文中的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，是否为全]{style="font-family:宋体"}[0]{lang="EN-US"}[或者全]{style="font-family:宋体"}[1]{lang="EN-US"}[，是否和以太网报文头中的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址一致。全]{style="font-family:宋体"}[0]{lang="EN-US"}[、全]{style="font-family:宋体"}[1]{lang="EN-US"}[、不一致的报文都是无效的，无效的报文需要被丢弃。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_x1937_17589_x2092897372}[：检查]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}[和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，全]{style="font-family:宋体"}[1]{lang="EN-US"}[或者组播]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址都是不合法的，需要丢弃。对于]{style="font-family:宋体"}[ARP]{lang="EN-US"}[应答报文，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址都进行检查；对于]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文，只检查源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[src-mac]{lang="EN-US"}**]{#struct_0_x1937_17589_x1647605325}[：检查]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和以太网报文头中的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是否一致，一致认为有效，否则丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1150298284}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x65418717}[使能对]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的有效性检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_697090501}

[\[Sysname\] arp detection validate dst-mac src-mac ip]{lang="EN-US"}
:::

::: {#332287100 .myid}
[]{#_Toc183856446}[]{#_Toc162773011}[]{#_Toc404793912}[]{#struct_0_x1937_17589_x202934791}[]{#_Toc258334081}[]{#_Toc217213812}[]{#_Toc191870347}[]{#_Toc191870348}[]{#_Toc191870349}[]{#_Toc191870350}[]{#_Toc191870351}[]{#_Toc191870352}[]{#_Toc191870353}[]{#_Toc191870354}[]{#_Toc191870355}[]{#_Toc191870356}[]{#_Toc191870357}[]{#_Toc191870358}[]{#_Toc191870359}[]{#_Toc191870360}[]{#_Toc191870361}[]{#_Toc191870362}[]{#_Toc191870364}[]{#_Toc191870365}

**ARP攻击防御 \-- ARP Detection配置命令 \-- arp restricted-forwarding enable**

------------------------------------------------------------------------

[**[arp restricted-forwarding enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x431111108}[命令用来使能]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文强制转发功能。]{style="font-family:宋体"}

[**[undo arp restricted-forwarding enable]{lang="EN-US"}**]{#struct_0_x1937_17589_199585141}[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文强制转发功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1348869367}

[**[arp restricted-forwarding enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x1648195152}

[**[undo arp restricted-forwarding enable]{lang="EN-US"}**]{#struct_0_x1937_17589_x2037537967}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_152455401}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_1185243343}[报文强制转发功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1575353571}

[[VLAN]{lang="EN-US"}]{#struct_0_x1937_17589_x87446385}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2132244253}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1417792023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x290184518}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648129616}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1712910839}[使能]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文强制转发功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1146944514}

[\[Sysname\] vlan 2]{lang="EN-US"}

[\[Sysname-vlan2\] arp restricted-forwarding enable]{lang="EN-US"}
:::

::: {#2064166021 .myid}
[]{#_Toc404793913}[]{#struct_0_x1937_17589_1395366347}[]{#_Toc258334082}

**ARP攻击防御 \-- ARP Detection配置命令 \-- display arp detection**

------------------------------------------------------------------------

[**[display arp detection]{lang="EN-US"}**]{#struct_0_x1937_17589_x804175358}[命令用来显示使能了]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1098631197}

[**[display arp detection]{lang="EN-US"}**]{#struct_0_x1937_17589_x885044928}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x2020665740}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_47623586}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648326224}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x650639163}

[[network-operator]{lang="EN-US"}]{#struct_0_x1937_17589_x265870583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1795743280}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1937_17589_190491963}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x550749131}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x326688027}[显示所有使能了]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display arp detection]{lang="EN-US"}]{#struct_0_x1937_17589_x37575056}

[ ARP detection is enabled in the following VLANs:]{lang="EN-US"}

[ 1-2, 4-5]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display arp detection]{lang="EN-US"}]{#struct_0_x1937_17589_x1648260688}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1755482552}[[字段]{style="font-family:黑体"}]{#struct_0_x1937_17589_1720080913}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1937_17589_x638962720}

[[ARP detection is enabled in the following VLANs]{lang="EN-US"}]{#struct_0_x1937_17589_x478163921}

[[使能了]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}]{#struct_0_x1937_17589_x961317227}[功能的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1984254242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[arp detection enable]{lang="EN-US"}**]{#struct_0_x1937_17589_473909796}

::: {#-1945749790 .myid}
[]{#_Toc404793914}[]{#struct_0_x1937_17589_1629594180}[]{#_Toc258334083}[]{#_Toc183856447}[]{#_Toc162773012}

**ARP攻击防御 \-- ARP Detection配置命令 \-- display arp detection statistics**

------------------------------------------------------------------------

[**[display arp detection statistics]{lang="EN-US"}**]{#struct_0_x1937_17589_x1647933008}[命令用来显示]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能报文检查的丢弃计数的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_112616625}

[**[display arp detection statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1937_17589_x1022145904}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2022084672}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_1009603834}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_440708874}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1901507515}

[[network-operator]{lang="EN-US"}]{#struct_0_x1937_17589_1312915737}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x2074975794}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1937_17589_x1647867472}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2104073740}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1937_17589_x238247214}[：显示指定接口的统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1746895903}

[[按接口显示用户合法性检查、报文有效性检查和]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_278586620}[报文上送限速的统计情况，只显示]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能报文的丢弃情况。不指定接口时，显示所有接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x75607362}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1891210197}[显示]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[功能报文检查的丢弃计数的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display arp detection statistics]{lang="EN-US"}]{#struct_0_x1937_17589_x1648064080}

[State: U-Untrusted  T-Trusted]{lang="EN-US"}

[ARP packets dropped by ARP inspect checking:]{lang="EN-US"}

[Interface(State)            IP        Src-MAC   Dst-MAC   Inspect]{lang="EN-US"}

[GE1/0/1(U)                  40        0         0         78]{lang="NL-BE"}

[GE1/0/2(U)                  0         0         0         0]{lang="NL-BE"}

[GE1/0/3(T)                  0         0         0         0]{lang="NL-BE"}

[GE1/0/4(U)                  0         0         30        0]{lang="NL"}

[[表1-4 ]{lang="EN-US"}[display arp detection statistics]{lang="EN-US"}]{#struct_0_x1937_17589_823964987}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1750154104}[[字段]{style="font-family:黑体"}]{#struct_0_x1937_17589_1663786662}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1216540922}

[[State]{lang="EN-US"}]{#struct_0_x1937_17589_x1618369424}

[[接口状态：]{style="font-family:宋体"}]{#struct_0_x1937_17589_202344355}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x1937_17589_x1765046863}[：]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[非信任接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1937_17589_x1647998544}[：]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[信任接口]{lang="EN-US" style="font-family:宋体"}

[[Interface(State)]{lang="EN-US"}]{#struct_0_x1937_17589_492365644}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_103888489}[报文入接口，]{style="font-family:宋体"}[State]{lang="EN-US"}[表示该接口的信任状态]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_x1937_17589_1060913582}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x223629186}[报文源和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址检查不通过丢弃的报文计数]{style="font-family:宋体"}

[[Src-MAC]{lang="EN-US"}]{#struct_0_x1937_17589_832183061}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1647670864}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查不通过丢弃的报文计数]{style="font-family:宋体"}

[[Dst-MAC]{lang="EN-US"}]{#struct_0_x1937_17589_690710665}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_1346498365}[报文目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查不通过丢弃的报文计数]{style="font-family:宋体"}

[[Inspect]{lang="EN-US"}]{#struct_0_x1937_17589_x1898911704}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_477047947}[报文结合用户合法性检查不通过丢弃的报文计数]{style="font-family:宋体"}

[ ]{lang="FR"}

::: {#1982787989 .myid}
[]{#_Toc404793915}[]{#struct_0_x1937_17589_x299563239}[]{#_Toc258334084}[]{#_Toc183856448}[]{#_Toc162773013}

**ARP攻击防御 \-- ARP Detection配置命令 \-- reset arp detection statistics**

------------------------------------------------------------------------

[**[reset arp detection statistics]{lang="EN-US"}**]{#struct_0_x1937_17589_1842202676}[命令用来清除]{style="font-family:
宋体"}[ARP Detection]{lang="EN-US"}[的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1647605328}

[**[reset arp detection statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1937_17589_1197352451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1547210857}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x1800197487}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_325088943}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1188318049}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1457728839}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_910618770}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1937_17589_x1184915548}[：表示清除指定接口下的统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648195151}

[[不指定接口时，清除所有]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}]{#struct_0_x1937_17589_x471454026}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1552821011}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x758467582}[清除所有]{style="font-family:宋体"}[ARP Detection]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset arp detection statistics]{lang="EN-US"}]{#struct_0_x1937_17589_589546067}
:::

::: {#814898209 .myid}
[]{#_Toc216234554}[]{#_Toc404793917}[]{#struct_0_x1937_17589_x1648129615}[]{#_Toc258334086}

**ARP攻击防御 \-- ARP自动扫描、固化配置命令 \-- arp fixup**

------------------------------------------------------------------------

[**[arp fixup]{lang="EN-US"}**]{#struct_0_x1937_17589_2116195366}[命令用来配置]{style="font-family:宋体"}[ARP]{lang="EN-US"}[固化功能，将当前的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项转换为静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。后续学习到的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项可以通过再次执行]{style="font-family:宋体"}**[arp fixup]{lang="EN-US"}**[命令进行固化。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x648456690}

[**[arp fixup]{lang="EN-US"}**]{#struct_0_x1937_17589_x470723148}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_394819385}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1937_17589_x604256609}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1113184757}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1952700279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_1130243255}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648326223}

[[固化后的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_108875724}[表项与配置产生的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项相同。]{style="font-family:宋体"}

[[固化生成的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1680026394}[表项数量同样受到设备可以支持的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项数目的限制，由于静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项数量的限制可能导致只有部分动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项被固化。]{style="font-family:宋体"}

[[如果用户执行固化前有]{style="font-family:宋体"}[D]{lang="EN-US"}]{#struct_0_x1937_17589_x1069152420}[个动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，]{style="font-family:宋体"}[S]{lang="EN-US"}[个静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项，由于固化过程中存在动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的老化或者新建动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的情况，所以固化后的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项可能为（]{style="font-family:宋体"}[D]{lang="EN-US"}[＋]{style="font-family:宋体"}[S]{lang="EN-US"}[＋]{style="font-family:
宋体"}[M]{lang="EN-US"}[－]{style="font-family:宋体"}[N]{lang="EN-US"}[）个。其中，]{style="font-family:宋体"}[M]{lang="EN-US"}[为固化过程中新建的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项个数，]{style="font-family:宋体"}[N]{lang="EN-US"}[为固化过程中老化的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项个数。]{style="font-family:宋体"}

[[通过固化生成的静态]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_663380534}[表项，可以通过命令行]{style="font-family:宋体"}**[undo arp ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \[ *vpn-instance-name* \]]{lang="EN-US"}[逐条删除，也可以通过命令行]{style="font-family:宋体"}**[reset arp all]{lang="EN-US"}**[或]{style="font-family:宋体"}**[reset arp static]{lang="EN-US"}**[全部删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1911075226}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1806656248}[配置]{style="font-family:宋体"}[ARP]{lang="EN-US"}[固化功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1998254886}

[\[Sysname\] arp fixup]{lang="EN-US"}
:::

::: {#-2067090805 .myid}
[]{#_Toc404793918}[]{#struct_0_x1937_17589_x1648260687}[]{#_Toc258334087}

**ARP攻击防御 \-- ARP自动扫描、固化配置命令 \-- arp scan**

------------------------------------------------------------------------

[**[arp scan]{lang="EN-US"}**]{#struct_0_x1937_17589_2123365440}[命令用来启动]{style="font-family:宋体"}[ARP]{lang="EN-US"}[自动扫描功能，该功能可以对接口下指定地址范围内的邻居进行扫描。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1177864423}

[**[arp scan]{lang="EN-US"}**[ \[ *start-ip-address* **to** *end-ip-address* \]]{lang="EN-US"}]{#struct_0_x1937_17589_x1449064851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_536877039}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1937_17589_1611809640}[三层以太网子接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1640680355}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1345722421}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x2124531110}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1647933007}

[*[start-ip-address]{lang="EN-US"}*]{#struct_0_x1937_17589_x290667902}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[扫描区间的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须小于等于终止]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[end-ip-address]{lang="EN-US"}*]{#struct_0_x1937_17589_x1886217470}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[扫描区间的终止]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。终止]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须大于等于起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1031274820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户知道局域网内邻居分配的]{style="font-family:宋体"}]{#struct_0_x1937_17589_1863507129}[IP]{lang="EN-US"}[地址范围，指定了]{style="font-family:宋体"}[ARP]{lang="EN-US"}[扫描区间，则对该范围内的邻居进行扫描，减少扫描等待的时间。如果指定的扫描区间同时在接口下多个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的网段内，则发送的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址选择网段范围较小的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户不指定]{style="font-family:宋体"}]{#struct_0_x1937_17589_x261061788}[ARP]{lang="EN-US"}[扫描区间的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和终止]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则仅对接口下的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址网段内的邻居进行扫描。其中，发送的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址就是接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x747072269}[扫描区间的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和终止]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须与接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或手工配置的从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）在同一网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于已存在]{style="font-family:宋体"}]{#struct_0_x1937_17589_x1723717839}[ARP]{lang="EN-US"}[表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不进行扫描。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[扫描操作可能比较耗时，用户可以通过]{style="font-family:宋体"}]{#struct_0_x1937_17589_2090391625}[\<Ctrl_C\>]{lang="EN-US"}[来终止扫描（在终止扫描时，对于已经收到的邻居应答，会建立该邻居的动态]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1647867471}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1937_17589_x1787609029}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_1980408630}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址网段内的邻居进行扫描。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_791204375}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp scan]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x628912687}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下指定地址范围内的邻居进行扫描。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_158853882}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp scan 1.1.1.1 to 1.1.1.20]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1937_17589_x207891976}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x1495439746}[对接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[下的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址网段内的邻居进行扫描。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1648064079}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] arp scan]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x1547967112}[对接口]{style="font-family:宋体"}[Vlan-interface2]{lang="EN-US"}[下指定地址范围内的邻居进行扫描。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_324501010}

[\[Sysname\] interface vlan-interface 2 ]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] arp scan 1.1.1.1 to 1.1.1.20]{lang="EN-US"}
:::

::: {#1318534574 .myid}
[]{#_Toc217213817}[]{#_Toc404793920}[]{#struct_0_x1937_17589_593152121}[]{#_Toc258334089}

**ARP攻击防御 \-- ARP网关保护配置命令 \-- arp filter source**

------------------------------------------------------------------------

[**[arp filter source]{lang="EN-US"}**]{#struct_0_x1937_17589_x793210910}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[网关保护功能，配置受保护的网关]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo arp filter source]{lang="EN-US"}**]{#struct_0_x1937_17589_x1647998543}[命令用来删除已配置的受保护网关]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1880287351}

[**[arp filter source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1937_17589_360015845}

[**[undo arp filter source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1937_17589_x1374437349}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x35247874}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1874290843}[网关保护功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_106157424}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1937_17589_2085561745}[二层聚合接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_557309875}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x1647670863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x68804222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1442339537}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1937_17589_x770351761}[：受保护的网关]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_2018282908}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个接口最多支持配置]{style="font-family:宋体"}]{#struct_0_x1937_17589_553389868}[8]{lang="EN-US"}[个受保护的网关]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能在同一接口下同时配置命令]{lang="EN-US" style="font-family:宋体"}**[arp filter source]{lang="EN-US"}**]{#struct_0_x1937_17589_1748674430}[和]{lang="EN-US" style="font-family:
宋体"}**[arp filter binding]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_840790310}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_x19281409}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[网关保护功能，受保护的网关]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1647605327}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp filter source 1.1.1.1]{lang="EN-US"}
:::

::: {#-577238313 .myid}
[]{#_Toc404793922}[]{#struct_0_x1937_17589_x2006534423}[]{#_Toc258334091}

**ARP攻击防御 \-- ARP过滤保护配置命令 \-- arp filter binding**

------------------------------------------------------------------------

[**[arp filter binding]{lang="EN-US"}**]{#struct_0_x1937_17589_x1496442001}[命令用来开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[过滤保护功能，限制只有特定源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文才允许通过。]{style="font-family:宋体"}

[**[undo arp ]{lang="EN-US"}[filter binding]{lang="EN-US"}**]{#struct_0_x1937_17589_x875550790}[命令用来删除已配置的被允许通过的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1937_17589_532611689}

[**[arp filter binding ]{lang="EN-US"}***[ip-address mac-address]{lang="EN-US"}*]{#struct_0_x1937_17589_x1648195154}

[**[undo arp filter binding]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1937_17589_x1230968913}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x994897663}

[[ARP]{lang="EN-US"}]{#struct_0_x1937_17589_x1325360318}[过滤保护功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x143439194}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1937_17589_476588744}[二层聚合接口视图（视图的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1937_17589_1990290841}

[[network-admin]{lang="EN-US"}]{#struct_0_x1937_17589_2088327411}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1937_17589_x2057123810}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1648129618}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1937_17589_x1775487403}[：允许通过的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x1937_17589_1583250579}[：允许通过的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1937_17589_993032118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个接口最多支持配置]{style="font-family:宋体"}]{#struct_0_x1937_17589_379109043}[8]{lang="EN-US"}[组允许通过的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能在同一接口下同时配置命令]{lang="EN-US" style="font-family:宋体"}**[arp filter source]{lang="EN-US"}**]{#struct_0_x1937_17589_x1588899799}[和]{lang="EN-US" style="font-family:
宋体"}**[arp filter binding]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1937_17589_x1613840235}

[[\# ]{lang="EN-US"}]{#struct_0_x1937_17589_494510907}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[过滤保护功能，允许源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[、源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2-2-2]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1937_17589_x1648326226}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] arp filter binding 1.1.1.1 2-2-2]{lang="EN-US"}
:::
