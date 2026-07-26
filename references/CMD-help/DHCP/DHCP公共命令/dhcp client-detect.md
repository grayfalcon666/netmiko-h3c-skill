::: {#-268708465 .myid}
[]{#_Toc404786397}[]{#struct_0_x1331_x1769_x1241805927}

**DHCP \-- DHCP公共命令 \-- dhcp client-detect**

------------------------------------------------------------------------

[**[dhcp client-detect]{lang="EN-US"}**]{#struct_0_x1331_x1769_1071611010}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的下线用户探测功能。]{style="font-family:宋体"}

[**[undo dhcp client-detect]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2035367895}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1138595989}

[**[dhcp]{lang="EN-US"}**[ **client-detect**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1590235933}

[**[undo dhcp client-detect]{lang="EN-US"}**]{#struct_0_x1331_x1769_1701803179}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1171411379}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_882922365}[服务器或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的用户下线检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1066314617}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1413536164}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x457855792}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1552264205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1964092698}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1240953959}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1559745694}[服务器开启该功能后，当设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项老化时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器认为该表项对应的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端已经下线，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器会删除对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_751099311}[中继开启该功能后，当设备上的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项老化时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继认为该表项对应的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端已经下线，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继会删除对应的用户地址表项，并通过发]{style="font-family:宋体"}[Release]{lang="EN-US"}[报文通知]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器删除下线用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1312387403}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x2077422329}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的用户下线检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1705435951}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp client-detect]{lang="EN-US"}
:::

::: {#1901484771 .myid}
[]{#_Toc404786398}[]{#struct_0_x1331_x1769_x1490618790}

**DHCP \-- DHCP公共命令 \-- dhcp dscp**

------------------------------------------------------------------------

[**[dhcp dscp]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1097078317}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继发送]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo dhcp dscp]{lang="EN-US"}**]{#struct_0_x1331_x1769_2001341863}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1429244767}

[**[dhcp dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_x1331_x1769_329277880}

[**[undo dhcp dscp]{lang="EN-US"}**]{#struct_0_x1331_x1769_1546890102}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1351893672}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_624608829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_268618546}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x407326320}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x806102471}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_355141540}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1046882805}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1525704786}

[[DSCP]{lang="EN-US"}]{#struct_0_x1331_x1769_181513652}[优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。通过本命令可以指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继发送的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1352221352}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_96776379}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继发送的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1033858359}

[\[Sysname\] dhcp dscp 30]{lang="EN-US"}
:::

::: {#1469960007 .myid}
[]{#_Toc269455509}[]{#_Toc266880098}[]{#_Toc404786399}[]{#struct_0_x1331_x1769_x847922962}[]{#_Toc283109585}[]{#_Toc266880097}

**DHCP \-- DHCP公共命令 \-- dhcp enable**

------------------------------------------------------------------------

[[[dhcp enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1003607945}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[[undo dhcp enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x475113676}[命令用来禁止]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_524908178}

[[dhcp enable]{lang="EN-US"}]{#struct_0_x1331_x1769_920037237}

[[undo dhcp enable]{lang="EN-US"}]{#struct_0_x1331_x1769_100030686}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1352286888}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x630429271}[服务处于禁止状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1592201942}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1165550679}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_849826596}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x695349177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1210708887}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1866695648}

[[只有开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377186288}[服务后，其它相关的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[配置才能生效。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1746744972}[服务器和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继时，都需要先开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1955424549}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1952485138}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1825046834}

[\[Sysname\] dhcp enable]{lang="EN-US"}
:::

::: {#1755177064 .myid}
[]{#_Toc404786400}[]{#struct_0_x1331_x1769_959261162}

**DHCP \-- DHCP公共命令 \-- dhcp log enable**

------------------------------------------------------------------------

[**[dhcp log enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_x31260299}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器日志信息功能。]{style="font-family:宋体"}

[**[undo dhcp log enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_317122992}[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器日志信息功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2123764434}

[**[dhcp log enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1550756651}

[**[undo dhcp log enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_959195626}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_855007449}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_910978100}[服务器日志信息功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x156322260}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_11274488}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2058893065}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x614909122}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_831980352}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x111754781}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_922264884}[服务器日志是为了满足管理员审计需求。设备生成]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[日志信息会交给信息中心模块处理，信息中心模块的配置将决定日志信息的发送规则和发送方向。关于信息中心的详细描述请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[[比如大量]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1887635942}[客户端发生上下线操作时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器会输出大量日志信息，这可能会降低设备性能，影响]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的速度。为了避免该情况的发生，用户可以关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器日志信息功能，使得]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器不再输出日志信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_137746402}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x821819663}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器日志信息功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_958736871}

[\[Sysname\] dhcp log enable]{lang="EN-US"}
:::

::: {#-1029821684 .myid}
[]{#_Toc404786401}[]{#struct_0_x1331_x1769_x1160676324}[]{#_Toc344456833}

**DHCP \-- DHCP公共命令 \-- dhcp rate-limit**

------------------------------------------------------------------------

[**[dhcp rate-limit]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1193796595}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文限速功能，即限制接口接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的速率。]{style="font-family:宋体"}

[**[undo dhcp rate-limit]{lang="EN-US"}**]{#struct_0_x1331_x1769_164544104}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1377120752}

[**[dhcp rate-limit ]{lang="EN-US"}***[rate]{lang="EN-US"}*]{#struct_0_x1331_x1769_1093751137}

[**[undo dhcp rate-limit]{lang="EN-US"}**]{#struct_0_x1331_x1769_x713235532}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x815517750}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x177846498}[报文限速功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x290275668}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1612809038}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1774046116}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_503438744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377317360}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2118563478}

[*[rate]{lang="EN-US"}*]{#struct_0_x1331_x1769_x913894708}[：接口接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的最高速率，单位为]{style="font-family:宋体"}[Kbps]{lang="EN-US"}[。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1810913907}

[[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1521895806}[报文限速功能后，当接口上收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文速率超过用户设定的限速值时，丢弃超过速率限制的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1492104466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_1288140539}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_538277714}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文限速功能，即限制接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的速率为]{style="font-family:宋体"}[64Kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377251824}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp rate-limit 64]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x381528297}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1833263108}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文限速功能，即限制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的速率为]{style="font-family:宋体"}[64Kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1894545415}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] dhcp rate-limit 64]{lang="EN-US"}
:::

::: {#16523392 .myid}
[]{#_Toc404786402}[]{#struct_0_x1331_x1769_x350025828}[]{#_Toc283109584}

**DHCP \-- DHCP公共命令 \-- dhcp select**

------------------------------------------------------------------------

[[[dhcp select]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1843636896}[命令用来配置接口工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模式。]{style="font-family:宋体"}

[[[undo dhcp select]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x283473927}[命令用来取消接口工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器或]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模式，即接口将丢弃]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376924144}

[**[dhcp select]{lang="EN-US"}**[ { **relay** \[ **proxy** \] \| **server** }]{lang="EN-US"}]{#struct_0_x1331_x1769_805506338}

[**[undo dhcp select]{lang="EN-US"}**[ { **relay** \| **server** }]{lang="EN-US"}]{#struct_0_x1331_x1769_x55713583}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2054793983}

[[接口工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1922874008}[服务器模式，即当接口收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文时，将从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的地址池中分配地址等参数。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1694326892}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1237237252}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_375259881}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1337474614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376858608}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1073532532}

[[[relay]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_545660313}[：配置接口工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模式，即当接口收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文时，将报文转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器，由]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配地址等参数。]{style="font-family:宋体"}

[[[proxy]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1064380489}[：配置接口工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[代理模式，即当接口收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文时，将报文转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器，由]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配地址等参数。当接口收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发来的应答报文后，把报文中的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址修改为中继接口地址。]{style="font-family:宋体"}

[[[server]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x844450049}[：配置接口工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器模式，即当接口收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文时，将从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的地址池中分配地址等参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x80801454}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_961331942}[服务器和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端位于同一个网段时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端可以直接从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址等参数；]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端位于不同网段时，需要配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器之间转发报文。]{style="font-family:宋体"}

[[需要注意的是，接口从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x226864246}[服务器模式切换到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模式时，设备不会删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址绑定信息，也不会删除相应的授权]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。这些表项可能会与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继新生成的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项冲突。因此，建议接口从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器模式切换到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模式时，通过]{style="font-family:宋体"}[[reset dhcp server ip-in-use]{lang="EN-US"}]{.commandkeywordsChar}[命令清除已有的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2115162260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x682445053}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377055216}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1312440391}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp select relay]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x891485016}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x88636427}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1710692092}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] dhcp select relay]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1031464011}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[reset dhcp server ip-in-use]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_707869035}
:::

::: {#196224333 .myid}
[]{#_Toc404786404}[]{#struct_0_x1331_x1769_435168443}

**DHCP \-- DHCP服务器配置命令 \-- address range**

------------------------------------------------------------------------

[[[address range]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1809596011}[命令用来配置地址池动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[[undo address range]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x973009794}[命令用来删除地址池动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_502786079}

[[[address range ]{lang="EN-US"}]{.commandkeywordsChar}*[start-ip-address end-ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_1552753003}

[[undo address range]{lang="EN-US"}]{#struct_0_x1331_x1769_372033246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1077275600}

[[没有配置动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_1995919872}[地址范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376662000}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1204151605}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1866375603}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1182767994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1404864741}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_460518738}

[*[start-ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x2034144162}[：动态分配范围的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[end-ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_95987636}[：动态分配范围的结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x741610490}

[[如果没有通过本命令配置地址池动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376596464}[地址范围，则地址池下]{style="font-family:宋体"}[[network]{lang="EN-US"}]{.commandkeywordsChar}[命令指定的网段地址都可以分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端；如果通过本命令配置了地址池动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围，则只能从本命令指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围内选择地址分配给客户端。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1800652910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[address range]{lang="EN-US"}**]{#struct_0_x1331_x1769_x405783951}[命令]{style="font-family:宋体"}[后，不能再通过]{lang="EN-US" style="font-family:宋体"}**[network secondary]{lang="EN-US"}**[命令在地址池中配置从网段。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行本命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1836942105}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address range]{lang="EN-US"}**]{#struct_0_x1331_x1769_484247513}[命令]{style="font-family:宋体"}[指定的地址范围应该在]{lang="EN-US" style="font-family:宋体"}**[network]{lang="EN-US"}**[命令]{style="font-family:宋体"}[指定的网段范围内，网段范围外的地址将无法被分配。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1907568251}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_147265324}[配置地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[动态分配的地址范围为]{style="font-family:宋体"}[192.168.8.1]{lang="EN-US"}[到]{style="font-family:宋体"}[192.168.8.150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377186287}

[\[Sysname\] dhcp server ip-pool 1]{lang="EN-US"}

[\[Sysname-dhcp-pool-1\] address range 192.168.8.1 192.168.8.150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1343460445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[class]{lang="EN-US"}**]{#struct_0_x1331_x1769_143607744}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp class]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2129610930}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1294547359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_x1331_x1769_870235547}
:::

::: {#-1553376646 .myid}
[]{#_Toc404786405}[]{#struct_0_x1331_x1769_x934771491}[]{#_Toc269455513}[]{#_Toc266880102}

**DHCP \-- DHCP服务器配置命令 \-- bims-server**

------------------------------------------------------------------------

[[[bims-server]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x667062748}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口及共享密钥信息。]{style="font-family:宋体"}

[[[undo bims-server]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1751255441}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1377120751}

[[[bims-server ip]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*[ \[[ port]{.commandkeywordsChar} *port-number* \][ sharekey]{.commandkeywordsChar} { **cipher** \| **simple** } *key*]{lang="EN-US"}]{#struct_0_x1331_x1769_x472332804}

[[undo bims-server]{lang="EN-US"}]{#struct_0_x1331_x1769_x479335596}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1701879816}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1647752786}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1897578048}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_255008775}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1052514227}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1115090680}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377317359}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_254155053}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_373634934}[：指定]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[port]{lang="EN-US"}]{.commandkeywordsChar}[ *port-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_978074736}[：指定]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器的端口号。]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[为端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1382943997}[：以密文形式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1331_x1769_216998066}[：以明文形式设置密钥。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_x1331_x1769_180438524}[：指定]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器的共享密钥，区分大小写。]{style="font-family:宋体"}*[key]{lang="EN-US"}*[表示共享密钥，明文形式输入密钥时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串，密文形式输入密钥时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端获取到]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器的信息后，与]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器通信时，采用共享密钥对传递的消息进行加密，以保证消息传递的安全性。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_883190544}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_234612936}

[[以明文或密文方式设置的密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1377251823}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1540786004}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x822638638}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[80]{lang="EN-US"}[，共享密钥为]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x88103313}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] bims-server ip 1.1.1.1 port 80 sharekey simple aabbcc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1778331796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_443005829}
:::

::: {#-2137251729 .myid}
[]{#_Toc404786406}[]{#struct_0_x1331_x1769_172270841}[]{#_Toc269455514}[]{#_Toc266880103}[]{#_Toc202081849}[]{#_Toc137350268}

**DHCP \-- DHCP服务器配置命令 \-- bootfile-name**

------------------------------------------------------------------------

[[[bootfile-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1609574315}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端使用的启动文件名或远程启动文件的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[形式]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[undo bootfile-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1376924143}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端使用的启动文件名或远程启动文件的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[形式]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1116807963}

[[[bootfile-name]{lang="EN-US"}]{.commandkeywordsChar}*[ { bootfile-name \| url }]{lang="EN-US"}*]{#struct_0_x1331_x1769_1753101020}

[[undo bootfile-name]{lang="EN-US"}]{#struct_0_x1331_x1769_x2121224104}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1489451958}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_654536724}[客户端使用的启动文件名或远程启动文件的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[形式]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x653140310}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1894911484}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_477572110}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376858607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x2011581183}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1511805572}

[*[bootfile-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_1835491828}[：启动文件名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[url]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1609174930}[：远程启动文件的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[形式]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1943887874}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1243353913}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1781256031}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x990355224}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的启动文件名为]{style="font-family:宋体"}[boot.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377055215}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] bootfile-name boot.cfg]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1595304352}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的启动文件的]{style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[为]{style="font-family:宋体"}[http://10.1.1.1/boot.cfg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x43090989}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] bootfile-name http://10.1.1.1/boot.cfg]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1416442964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_525060592}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[n]{lang="EN-US"}]{.commandkeywordsChar}**[ext-serve[r]{.commandkeywordsChar}]{lang="EN-US"}**]{#struct_0_x1331_x1769_97766858}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[tftp-server domain-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1639021567}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[tftp-server ip-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1957135044}
:::

::: {#-1042484107 .myid}
[]{#_Toc404786407}[]{#struct_0_x1331_x1769_16089193}

**DHCP \-- DHCP服务器配置命令 \-- class option-group**

------------------------------------------------------------------------

[**[class option-group]{lang="EN-US"}**]{#struct_0_x1331_x1769_1187065241}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池下]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组的关联。]{style="font-family:宋体"}

[**[undo class option-group]{lang="EN-US"}**]{#struct_0_x1331_x1769_x535708035}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池下]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1656522634}

[**[class]{lang="EN-US"}**[ *class-name* **option-group** *option-group-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_16089192}

[**[undo class ]{lang="EN-US"}***[class-name]{lang="EN-US"}***[ ]{lang="EN-US"}[option-group]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1151586919}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2007809628}

[[未配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_962347916}[地址池的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组的关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_554265204}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1797933669}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x786826822}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1803103909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1299665104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_913754957}

[*[class-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_660955864}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[option-group-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_1193323123}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32768]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_16089195}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_804728217}[服务器应答]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端报文时，首先根据配置顺序逐个匹配通过]{style="font-family:宋体"}**[class option-group]{lang="EN-US"}**[命令指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类。如果匹配成功，则将该用户类对应的选项组中的选项填充到应答报文中；如果同时匹配多个]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类，且各用户类对应的选项组中有相同编号的选项，以最先匹配到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类对应的选项组中的选项为准。]{style="font-family:宋体"}

[[需要注意的是，对于一个]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1250325610}[用户类，在一个]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池中只能指定一个选项组。如果多次执行该命令为同一个]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类指定不同的选项组，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1851072978}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_999068661}[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[中，配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类]{style="font-family:宋体"}[user]{lang="EN-US"}[和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[的关联。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x660316344}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] class user option-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x673194848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp option-group ]{lang="EN-US"}**]{#struct_0_x1331_x1769_1313592419}*[option-group-number]{lang="EN-US"}*
:::

::: {#-1843167723 .myid}
[]{#_Toc404786408}[]{#struct_0_x1331_x1769_530024823}[]{#_Toc269455512}[]{#_Toc266880101}

**DHCP \-- DHCP服务器配置命令 \-- class range**

------------------------------------------------------------------------

[[[class range]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x918571011}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[[undo]{lang="EN-US"}]{.commandkeywordsChar}[ [class range]{.commandkeywordsChar}]{lang="EN-US"}]{#struct_0_x1331_x1769_x283550236}[命令用来删除为指定]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[用户类动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376989679}

[[[class]{lang="EN-US"}]{.commandkeywordsChar}[ *class-name* [range]{.commandkeywordsChar} *start-ip-address end-ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1937681160}

[[[undo class ]{lang="EN-US"}]{.commandkeywordsChar}*[class-name]{lang="EN-US"}*[ **range**]{lang="EN-US"}]{#struct_0_x1331_x1769_x321657310}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x784233218}

[[没有配置为指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1215049811}[用户类动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1964500821}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1204607522}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1605319658}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376661999}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_583813903}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x1331_x1769_1389620}

[*[class-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_72116147}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[start-ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_740411144}[：动态分配范围的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[end-ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1097761060}[：动态分配范围的结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1435783508}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1887610187}[服务器从地址池中选择地址分配给客户端时，首先根据配置顺序逐个匹配通过]{style="font-family:宋体"}**[class range]{lang="EN-US"}**[命令指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类。如果匹配成功，则从为该用户类指定的地址范围内选择地址分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端；如果该用户类中没有可供分配的地址，则继续匹配下一个用户类；如果所有匹配上的用户类地址范围都没有可供分配的地址，则从公共地址范围中选择地址分配给客户端；如果不匹配任何]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类，则会从地址池动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址范围（通过]{style="font-family:宋体"}**[address range]{lang="EN-US"}**[命令配置）中选择地址分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端；如果]{style="font-family:宋体"}**[address range]{lang="EN-US"}**[命令指定的地址范围内也没有空闲地址，或者没有配置]{style="font-family:宋体"}[[address range]{lang="EN-US"}]{.commandkeywordsChar}[命令，则地址分配失败，即]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器无法为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配地址。]{style="font-family:宋体"}

[[通过本配置可以实现将一个地址池下的地址范围划分成多个地址段，分别分配给属于不同]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1825617811}[用户类的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1376596463}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[class]{lang="EN-US"}**]{#struct_0_x1331_x1769_x928230445}**[ range]{lang="EN-US"}**[命令后，不能再通过]{lang="EN-US" style="font-family:宋体"}[[network secondary]{lang="EN-US"}]{.commandkeywordsChar}[命令在地址池中配置从网段。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[class]{lang="EN-US"}**]{#struct_0_x1331_x1769_101187762}**[ range]{lang="EN-US"}**[命令后，只能从]{lang="EN-US" style="font-family:宋体"}**[class]{lang="EN-US"}[ range]{lang="EN-US"}**[命令或]{lang="EN-US" style="font-family:宋体"}**[address range]{lang="EN-US"}**[命令指定的地址范围内选择地址分配给客户端。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址池中只能为一个]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x419858246}[DHCP]{lang="EN-US"}[用户类指定一个地址范围。如果多次执行本命令为同一个]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类指定不同的地址范围，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个地址池中可以为多个不同的]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x891455499}[DHCP]{lang="EN-US"}[用户类指定地址范围。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x872446979}[DHCP]{lang="EN-US"}[用户类不存在，则为该用户类指定的地址范围不能分配给任何]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[class range]{lang="EN-US"}**]{#struct_0_x1331_x1769_670350886}[命令指定的地址范围应该在]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令指定的主网段范围内，主网段范围外的地址将无法被分配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1307923855}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x439087860}[在地址池]{style="font-family:宋体"}[1]{lang="EN-US"}[中配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类]{style="font-family:宋体"}[user]{lang="EN-US"}[动态分配的地址范围为]{style="font-family:宋体"}[192.168.8.1]{lang="EN-US"}[到]{style="font-family:宋体"}[192.168.8.150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377186290}

[\[Sysname\] dhcp server ip-pool 1]{lang="EN-US"}

[\[Sysname-dhcp-pool-1\] class user range 192.168.8.1 192.168.8.150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2103040868}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address range]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1153359383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp class]{lang="EN-US"}**]{#struct_0_x1331_x1769_x370023039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[display dhcp server pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x2010810825}
:::

::: {#1171222275 .myid}
[]{#_Toc404786409}[]{#struct_0_x1331_x1769_x1411682671}[]{#_Toc269455515}[]{#_Toc266880104}

**DHCP \-- DHCP服务器配置命令 \-- dhcp class**

------------------------------------------------------------------------

[[[dhcp class]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1587199789}[命令用来创建]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类并进入]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类视图，如果已经创建了]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类，则直接进入该用户类视图。]{style="font-family:宋体"}

[[[undo dhcp class]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1604009930}[命令用来删除指定的用户类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1377120754}

[[[dhcp class ]{lang="EN-US"}]{.commandkeywordsChar}*[class-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_287182083}

[[[undo dhcp class]{lang="EN-US"}]{.commandkeywordsChar}[ *class-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x339531903}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1239716391}

[[不存在任何]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_106057987}[用户类。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x563076377}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x61809664}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1729215210}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1498928721}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377317362}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x955764064}

[*[class-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_x530571202}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1171156440}

[[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1100484466}[用户类视图下，可以通过]{style="font-family:宋体"}[[if-match]{lang="EN-US"}]{.commandkeywordsChar}[命令配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类的匹配规则，根据匹配规则判断]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端属于的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类，从而实现灵活的用户分类策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x96130436}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_49673045}[创建名称为]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类，并进入]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377251826}

[\[Sysname\] dhcp class test]{lang="EN-US"}

[\[Sysname-dhcp-class-test\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_781271117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address range]{lang="EN-US"}**]{#struct_0_x1331_x1769_1136817722}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}**[class]{lang="EN-US"}**]{#struct_0_x1331_x1769_657503812}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[if-match]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1960021337}
:::

::: {#133750611 .myid}
[]{#_Toc404786410}[]{#struct_0_x1331_x1769_x1940225947}

**DHCP \-- DHCP服务器配置命令 \-- dhcp option-group**

------------------------------------------------------------------------

[**[dhcp option-group]{lang="EN-US"}**]{#struct_0_x1331_x1769_x253517736}[命令用来创建]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组并进入]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组视图，如果已经创建了]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组，则直接进入该]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组视图。]{style="font-family:宋体"}

[**[undo dhcp option-group]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1940225948}[命令用来删除指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2119135259}

[**[dhcp option-group]{lang="EN-US"}**[ *option-group-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1584376305}

[**[undo dhcp option-group ]{lang="EN-US"}***[option-group-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_1484788047}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1878577725}

[[设备上未配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x540116119}[选项组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1533957415}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x2091796959}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1290412961}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1137291342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1083183321}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x814257806}

[*[option-group-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1940225945}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32768]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1236746104}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1853251594}[创建]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组]{style="font-family:宋体"}[1]{lang="EN-US"}[并进入该选项组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1731178671}

[\[Sysname\] dhcp option-group 1]{lang="EN-US"}

[\[Sysname-dhcp-option-group-1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_578795992}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[class]{lang="EN-US"}**[ *class-name* **option-group** *option-group-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_212546859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[option ]{lang="EN-US"}***[code]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ascii** ]{lang="EN-US"}*[ascii-string ]{lang="EN-US"}***[\| hex]{lang="EN-US"}***[ hex-string]{lang="EN-US"}***[ \| ip-address ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[&\<1-8\> }]{lang="EN-US"}]{#struct_0_x1331_x1769_x943207244}
:::

::: {#950319708 .myid}
[]{#_Toc404786411}[]{#struct_0_x1331_x1769_2090806215}[]{#_Toc269455517}[]{#_Toc266880106}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server always-broadcast**

------------------------------------------------------------------------

[[[dhcp server always-broadcast]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x201575333}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的广播回应报文功能。]{style="font-family:宋体"}

[[[undo dhcp server always-broadcast]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1107150775}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376924146}

[[dhcp server always-broadcast]{lang="EN-US"}]{#struct_0_x1331_x1769_x357293076}

[[undo dhcp server always-broadcast]{lang="EN-US"}]{#struct_0_x1331_x1769_1810011151}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_870158477}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x780660840}[服务器的广播回应报文功能处于关闭状态。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器根据请求报文中的广播标志位来决定以广播还是单播的形式发送应答报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x177846993}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x335495508}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x912352372}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1429214963}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376858610}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_717367708}

[[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1503420762}[服务器的广播回应报文功能后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器忽略请求报文中的广播标志位，以广播的形式发送应答报文。]{style="font-family:宋体"}

[[当已经存在]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1940774045}[地址的客户端发出请求报文（即报文中]{style="font-family:宋体"}[ciaddr]{lang="EN-US"}[字段不为]{style="font-family:宋体"}[0)]{lang="EN-US"}[时，无论是否开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的广播回应报文功能，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器都会以单播形式将回应报文发送给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端（即目的地址为]{style="font-family:宋体"}[ciaddr]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[当请求报文通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1438597338}[中继转发到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器（即报文中]{style="font-family:宋体"}[giaddr]{lang="EN-US"}[字段不为]{style="font-family:宋体"}[0]{lang="EN-US"}[）时，无论是否开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的广播回应报文功能，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器都会以单播形式将回应报文发送给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继（即目的地址为]{style="font-family:宋体"}[giaddr]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1123468145}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1486290379}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的广播回应报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_933918645}

[\[Sysname\] dhcp server always-broadcast]{lang="EN-US"}
:::

::: {#1884211345 .myid}
[]{#_Toc404786412}[]{#struct_0_x1331_x1769_x1377055218}[]{#_Toc269455516}[]{#_Toc266880105}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server apply ip-pool**

------------------------------------------------------------------------

[[[dhcp server apply ip-pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1463497131}[命令用来指定接口引用的地址池。]{style="font-family:宋体"}

[[[undo dhcp server apply ip-pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1885628718}[命令用来取消接口引用地址池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_136734801}

[[[dhcp server apply ip-pool ]{lang="EN-US"}]{.commandkeywordsChar}*[pool-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_x508317928}

[[undo dhcp server apply ip-pool]{lang="EN-US"}]{#struct_0_x1331_x1769_x475377937}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2134591784}

[[接口没有引用任何地址池。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_770675738}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1923639143}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1376989682}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1597967857}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_86035491}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_837627492}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x798678720}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_599359884}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1512070342}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1898885777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上配置了]{lang="EN-US" style="font-family:宋体"}[[dhcp server apply ip-pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1376662002}[命令后，如果接口引用的地址池不存在，则无法为客户端动态分配]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行本命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1928016277}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x683455825}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_1869450226}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1668895562}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[引用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1896913360}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp server apply ip-pool 0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x847775305}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1349733472}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[引用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376596466}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] dhcp server apply ip-pool 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1331514972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server ip-pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_599976681}
:::

::: {#1289834302 .myid}
[]{#_Toc404786413}[]{#struct_0_x1331_x1769_x115134073}[]{#_Toc269455518}[]{#_Toc266880107}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server bootp ignore**

------------------------------------------------------------------------

[[[dhcp server bootp ignore]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x103308159}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器忽略]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[请求。]{style="font-family:宋体"}

[[[undo dhcp server bootp ignore]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1686333986}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x194818547}

[[dhcp server bootp ignore]{lang="EN-US"}]{#struct_0_x1331_x1769_2084602317}

[[undo dhcp server bootp ignore]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377186289}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x180661031}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_228637124}[服务器不会忽略]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[请求。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1480318693}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_218223286}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x626359949}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x847046011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1772639431}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1377120753}

[[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1635132218}[客户端申请到的地址的租约是无限期的。在特殊的组网环境中，可能不希望出现无限期的地址租约。此时，可以通过配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器忽略]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[请求报文，避免分配无限期的地址租约。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_119366765}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1331442431}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器忽略]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1419834868}

[\[Sysname\] dhcp server bootp ignore]{lang="EN-US"}
:::

::: {#722726162 .myid}
[]{#_Toc404786414}[]{#struct_0_x1331_x1769_1421031001}[]{#_Toc269455519}[]{#_Toc266880108}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server bootp reply-rfc-1048**

------------------------------------------------------------------------

[[[dhcp server bootp reply-rfc-1048]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1901614981}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器回应]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[格式报文功能。]{style="font-family:宋体"}

[[[undo dhcp server bootp reply-rfc-1048]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1752924662}[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器回应]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[格式报文功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1406226819}

[[dhcp server bootp reply-rfc-1048]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377317361}

[[undo dhcp server bootp reply-rfc-1048]{lang="EN-US"}]{#struct_0_x1331_x1769_610319877}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1326142755}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x85903254}[服务器回应]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[格式报文功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1390409621}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x139122279}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x294139071}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_622791722}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1799594597}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1377251825}

[[有些]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1947612238}[客户端发送的请求报文中，]{style="font-family:宋体"}[vend]{lang="EN-US"}[字段的格式不符合]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[的要求。对于这种报文，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的缺省处理方法是不解析]{style="font-family:宋体"}[vend]{lang="EN-US"}[字段内容，将报文中]{style="font-family:宋体"}[vend]{lang="EN-US"}[字段的内容拷贝到回复报文中的]{style="font-family:宋体"}[vend]{lang="EN-US"}[字段回应给]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_57168488}[服务器的回应]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[格式报文功能后，对于这种格式不符合]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[要求的报文，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器会将需要回应的选项以符合]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[要求的格式，封装到回复报文的]{style="font-family:宋体"}[vend]{lang="EN-US"}[字段，并回应给]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[需要注意的是，该功能只在客户端通过]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_x33318476}[报文申请静态绑定地址时有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1168052126}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1009435388}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的回应]{style="font-family:宋体"}[RFC 1048]{lang="EN-US"}[格式报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x935173484}

[\[Sysname\] dhcp server bootp reply-rfc-1048]{lang="EN-US"}
:::

::: {#1205145582 .myid}
[]{#_Toc404786415}[]{#struct_0_x1331_x1769_x1063594058}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database filename**

------------------------------------------------------------------------

[[[dhcp server database filename]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x534389624}[命令用来指定存储]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项的文件名称。]{style="font-family:宋体"}

[[[undo dhcp server database filename]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1064183879}[命令用来删除指定的存储]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项的文件名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x370990383}

[**[dhcp server database filename]{lang="EN-US"}**[ { *filename \|* **url** *url* \[ **username** *username* \[ **password** { **cipher** \| **simple** } *key* \] \] }]{lang="EN-US"}]{#struct_0_x1331_x1769_1493566188}

[**[undo dhcp server database filename]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1387970232}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1906856434}

[[未指定存储文件名称。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_778131033}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_193158539}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1149514374}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_308343787}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1122618694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x801974147}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1064118343}

[*[filename]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1324620775}[：目标文件名，该配置用于本地存储模式。文件名取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[**[url]{lang="EN-US"}***[ url]{lang="EN-US"}*]{#struct_0_x1331_x1769_x306574106}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[，该配置用于远程文件系统模式。此参数中不能包含用户名和密码，和参数]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和]{style="font-family:宋体"}*[key]{lang="EN-US"}*[配合使用。]{style="font-family:宋体"}

[**[username]{lang="EN-US"}***[ username]{lang="EN-US"}*]{#struct_0_x1331_x1769_273007535}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[时的用户名。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1331_x1769_1016709517}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2002373374}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_x1331_x1769_279162635}[：设置的明文密码或密文密码，区分大小写。明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1637206618}

[[以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1463231998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_x1331_x1769_x1771059040}[存储]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项时，如果设备中还不存在对应名称的文件，则设备会自动创建该文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_x1331_x1769_1155920569}[执行本命令后，会立即触发一次表项备份。之后，如果未配置]{style="font-family:宋体"}**[dhcp]{lang="EN-US"}**[ ]{lang="EN-US"}**[server]{lang="EN-US"}**[ ]{lang="EN-US"}**[database]{lang="EN-US"}**[ ]{lang="EN-US"}**[update]{lang="EN-US"}**[ ]{lang="EN-US"}**[interval]{lang="EN-US"}**[命令，若表项发生变化，默认在]{style="font-family:宋体"}[300]{lang="EN-US"}[秒之后刷新存储文件；若表项未发生变化，则不再刷新存储文件。如果配置了]{style="font-family:宋体"}**[dhcp server]{lang="EN-US"}**[ ]{lang="EN-US"}**[database]{lang="EN-US"}**[ ]{lang="EN-US"}**[update]{lang="EN-US"}**[ ]{lang="EN-US"}**[interval]{lang="EN-US"}**[命令，若表项发生变化，则到达刷新时间间隔后刷新存储文件；若表项未发生变化，则不再刷新存储文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1064314951}[不支持远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[，配置远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[请使用]{lang="EN-US" style="font-family:宋体"}*[url]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[username]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[key]{lang="EN-US"}*[配合使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[频繁擦写本地存储介质可能会影响存储介质寿命，建议使用远程文件系统模式存储]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1339951750}[DHCP]{lang="EN-US"}[服务器表项文件。]{style="font-family:宋体"}

[[当进行远程存储时，支持]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1764242091}[和]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1706339676}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议时，服务器地址支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[形式或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[形式，并且支持]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名方式。服务器地址为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址形式时需使用方括号]{style="font-family:宋体"}[(]{lang="EN-US"}["]{style="font-family:宋体"}[\[]{lang="EN-US"}["和"]{style="font-family:
宋体"}[\]]{lang="EN-US"}["]{style="font-family:宋体"}[)]{lang="EN-US"}[引用。配置服务器地址为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名格式时请勿使用方括号引用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_x1331_x1769_x453231232}[当采用]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}[ftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径"的形式，如有用户名和密码请分别使用参数]{style="font-family:宋体"}[username]{lang="EN-US"}[和参数]{style="font-family:宋体"}[key]{lang="EN-US"}[进行配置，用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2137423177}[TFTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}[tftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径"的形式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2046722632}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x439179861}[配置存储]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项的文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1535185479}

[\[Sysname\] dhcp server database filename database.dhcp ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1281609209}[配置远程存储]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项至]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器工作目录下]{style="font-family:宋体"}[,]{lang="EN-US"}[用户名为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[，文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1064249415}

[\[Sysname\] dhcp server database filename url ftp://10.1.1.1/database.dhcp username 1 password simple 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x70157787}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update inte]{lang="EN-US"}**]{#struct_0_x1331_x1769_1944604440}**[r]{lang="EN-US"}[val]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update now]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1849790172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update ]{lang="EN-US"}**]{#struct_0_x1331_x1769_x258288178}**[stop]{lang="EN-US"}**
:::

::: {#-152039793 .myid}
[]{#_Toc404786416}[]{#struct_0_x1331_x1769_x164325704}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database update interval**

------------------------------------------------------------------------

[**[dhcp server database update interval]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1877055510}[命令用来配置刷新]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项存储文件的延迟时间。]{style="font-family:宋体"}

[**[undo dhcp server database update interval]{lang="EN-US"}**]{#struct_0_x1331_x1769_1544421309}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x675694612}

[**[dhcp server database update interval ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x1331_x1769_x36842195}

[**[undo dhcp server database update interval]{lang="EN-US"}**]{#struct_0_x1331_x1769_1950914018}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1064446023}

[[若]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1017332097}[服务器表项不变化，则不刷新表项存储文件；若]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项发生变化，默认在]{style="font-family:宋体"}[300]{lang="EN-US"}[秒后刷新表项存储文件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x286832416}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x2021565385}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x717461762}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x231121401}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1923116405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_113789579}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1331_x1769_1880935699}[：刷新延迟时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[864000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2119351643}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若执行该命令配置之前没有使用]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1064380487}**[dhcp server database filename]{lang="EN-US"}**[命令配置固化文件，]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[服务器不会在表项发生变化之后定时刷新表项数据到固化文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若执行该命令配置之后通过]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1196952579}**[dhcp server database filename]{lang="EN-US"}**[命令配置固化文件，则]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[服务器会在表项发生变化之后刷新表项数据到固化文件，且刷新表项的延迟时间为本命令配置的时间。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当服务器表项发生变化后，]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1232213758}[DHCP]{lang="EN-US"}[服务器开始计时，当本命令配置的延迟时间到达后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器会把这个时间段内表项所有的变化信息备份到固化文件中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1537306195}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1933366274}[若]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项发生变化，在]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟后刷新表项存储文件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1232309127}

[\[Sysname\] dhcp server database update interval 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1478001559}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[dhcp server database filename]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x50921252}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update now]{lang="EN-US"}**]{#struct_0_x1331_x1769_1168246663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update stop]{lang="EN-US"}**]{#struct_0_x1331_x1769_2131890098}
:::

::: {#-1893218074 .myid}
[]{#_Toc404786417}[]{#struct_0_x1331_x1769_1027278747}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database update now**

------------------------------------------------------------------------

[**[dhcp server database update now]{lang="EN-US"}**]{#struct_0_x1331_x1769_1909774590}[命令用来将当前]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项保存到用户指定的文件中。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1064577095}

[**[dhcp server database update now]{lang="EN-US"}**]{#struct_0_x1331_x1769_x135352400}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x796538008}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1183284947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1648140199}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x2085141587}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1253243540}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1642987108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_x1331_x1769_x1007538414}[本命令只用来触发一次]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项的备份。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未通过]{lang="EN-US" style="font-family:宋体"}**[dhcp server database filename]{lang="EN-US"}**]{#struct_0_x1331_x1769_1340467979}[命令指定存储表项的文件，则本命令的配置不会生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1064511559}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1019842007}[将当前的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项保存到文件中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x368769557}

[\[Sysname\] dhcp server database update now]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x687345369}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[dhcp server database filename]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1214483369}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update interval]{lang="EN-US"}**]{#struct_0_x1331_x1769_x800872754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update stop]{lang="EN-US"}**]{#struct_0_x1331_x1769_x25950037}
:::

::: {#-762071215 .myid}
[]{#_Toc404786418}[]{#struct_0_x1331_x1769_277082733}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server database update stop**

------------------------------------------------------------------------

[**[dhcp server database update stop]{lang="EN-US"}**]{#struct_0_x1331_x1769_1981902369}[命令用来终止当前的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项恢复操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x40071913}

[**[dhcp server database update stop]{lang="EN-US"}**]{#struct_0_x1331_x1769_296880891}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1063659591}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x859050786}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_151843229}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_118561651}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1592893339}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x440942737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[]{lang="EN-US"}]{#struct_0_x1331_x1769_x1358026628}[本命令只用来触发一次终止]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项的恢复操作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只用来停止设备重启后从固化文件中恢复表项信息的过程，不影响除此之外的其他运行过程。当中断恢复表项信息的过程后，如果]{style="font-family:宋体"}]{#struct_0_x1331_x1769_856200735}[DHCP]{lang="EN-US"}[服务器分配了未恢复表项中的地址信息，可能会导致局域网设备地址冲突情况发生。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[从固化文件恢复表项的连接超时的最长时间为]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1274700396}[60]{lang="EN-US"}[分钟，可以通过本命令立刻终止远程恢复。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器从固化文件中恢复表项的过程中，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器不会学习新的表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1647172999}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1912579465}[终止当前的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器表项恢复操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1063594055}

[\[Sysname\] dhcp server database update stop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x937674151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **s**]{lang="EN-US"}]{#struct_0_x1331_x1769_1979650156}**[erver]{lang="EN-US"}**[ **database** **filename**]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update interval]{lang="EN-US"}**]{#struct_0_x1331_x1769_39335104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server database update now]{lang="EN-US"}**]{#struct_0_x1331_x1769_1898972449}
:::

::: {#128878807 .myid}
[]{#_Toc404786419}[]{#struct_0_x1331_x1769_1279547043}[]{#_Toc269455520}[]{#_Toc266880171}[]{#_Toc202081853}[]{#_Toc137350278}[]{#_Toc100214081}[]{#_Toc94500188}[]{#_Toc69790738}[]{#_Toc60058883}[]{#_Toc43546296}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server forbidden-ip**

------------------------------------------------------------------------

[[[dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1376924145}[命令用来配置全局不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[undo dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1923377017}[命令用来取消全局不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2125059699}

[[[dhcp server forbidden-ip ]{lang="EN-US"}]{.commandkeywordsChar}*[start-ip-address]{lang="EN-US"}*[[ ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ ]{.commandkeywordsChar}*end-ip-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_204619979}

[[[undo dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}[ *start-ip-address* \[ *end-ip-address*[ ]{.commandkeywordsChar}\] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_1950765166}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2054741423}

[[没有配置全局不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1243634728}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_916211400}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_985875489}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376858609}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x492551409}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x192368277}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x902004493}

[*[start-ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_1568850657}[：不参与自动分配的起始]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[end-ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1630645560}[：不参与自动分配的结束]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，不能小于]{style="font-family:宋体"}*[start-ip-address]{lang="EN-US"}*[。如果不指定该参数，则表示只有一个不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即]{style="font-family:宋体"}*[start-ip-address]{lang="EN-US"}*[；否则，表示]{style="font-family:宋体"}*[start-ip-address]{lang="EN-US"}*[到]{style="font-family:宋体"}*[end-ip-address]{lang="EN-US"}*[之间的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址均不能参与自动分配。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1064118344}[：指定不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示配置的是公网中不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1112598968}

[[某些服务器占用的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_1958914388}[地址（如网关地址、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器地址），不能分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端。通过本命令可以避免这些地址参与自动分配。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1377055217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{lang="EN-US" style="font-family:宋体"}[[dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x253643550}[命令将已经静态绑定的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置为不参与自动分配的地址，则该地址仍然可以分配给静态绑定的用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}[[undo dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x76442371}[命令取消不参与自动分配]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的配置时，指定的地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[地址范围必须与执行]{lang="EN-US" style="font-family:宋体"}[[dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}[命令时指定的地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[地址范围保持一致。如果配置不参与自动分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址为某一地址范围，则只能同时取消该地址范围内所有]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的配置，不能单独取消其中某个]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行]{lang="EN-US" style="font-family:宋体"}[[dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_815365909}[命令，可以配置多个不参与自动分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址段。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1350734178}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x190991491}[配置]{style="font-family:宋体"}[10.110.1.1]{lang="EN-US"}[到]{style="font-family:宋体"}[10.110.1.63]{lang="EN-US"}[之间的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不参与地址自动分配。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x414338568}

[\[Sysname\] dhcp server forbidden-ip 10.110.1.1 10.110.1.63]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_167343898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_609193906}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[static-bind]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1376989681}
:::

::: {#-1910451003 .myid}
[]{#_Toc404786420}[]{#struct_0_x1331_x1769_2001252384}[]{#_Toc269455521}[]{#_Toc266880172}[]{#_Toc202081854}[]{#_Toc137350279}[]{#_Toc100214082}[]{#_Toc94500189}[]{#_Toc69790739}[]{#_Toc60058884}[]{#_Toc43546297}[]{#_Toc37217589}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server ip-pool**

------------------------------------------------------------------------

[[[dhcp server ip-pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1403989497}[命令用来创建]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池并进入]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池视图。如果已经创建了]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池，则直接进入该地址池视图。]{style="font-family:宋体"}

[[[undo dhcp server ip-pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x248366017}[命令用来删除指定的地址池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_950359372}

[[[dhcp server ip-pool ]{lang="EN-US"}]{.commandkeywordsChar}*[pool-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_x401748779}

[[[undo dhcp server ip-pool]{lang="EN-US"}]{.commandkeywordsChar}[ *pool-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_1891341916}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2011634634}

[[不存在任何]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_984935011}[地址池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376662001}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_361932336}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_963878510}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1286870054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1457063452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x928388595}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1487821352}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，是地址池的唯一标识，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_431342329}

[[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376596465}[地址池下，可以配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、网关地址等参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_234568969}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x226340605}[创建名称为]{style="font-family:宋体"}[pool1]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_970850551}

[\[Sysname\] dhcp server ip-pool pool1]{lang="EN-US"}

[\[Sysname-dhcp-pool-pool1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1746630540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server apply ip-poo[l]{.commandkeywordsChar}]{lang="EN-US"}**]{#struct_0_x1331_x1769_717947472}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_1482157319}
:::

::: {#1117427087 .myid}
[]{#_Toc404786421}[]{#struct_0_x1331_x1769_19977509}[]{#_Toc269455522}[]{#_Toc266880173}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server ping packets**

------------------------------------------------------------------------

[[[dhcp server ping packets]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x598128401}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送回显请求报文的最大数目。]{style="font-family:宋体"}

[[[undo dhcp server ping packets]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1377186292}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x940241454}

[[[dhcp server ping packets]{lang="EN-US"}]{.commandkeywordsChar}[ *number*]{lang="EN-US"}]{#struct_0_x1331_x1769_1132954946}

[[undo dhcp server ping packets]{lang="EN-US"}]{#struct_0_x1331_x1769_x997244532}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_106362860}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x321999182}[服务器发送回显请求报文的最大数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_328473400}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_435569023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1377120756}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x875617331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_536168901}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1391268688}

[*[number]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1285508081}[：发送回显请求报文的最大数目，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[服务器将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端之前，不会通过]{style="font-family:宋体"}[ping]{lang="EN-US"}[操作探测该地址是否冲突。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1625016177}

[[为防止]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2066774857}[地址重复分配导致地址冲突，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为客户端分配地址前，需要先对该地址进行探测。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1504680240}[服务器的地址探测是通过]{style="font-family:宋体"}[ping]{lang="EN-US"}[功能实现的，通过检测是否能在指定时间内得到]{style="font-family:宋体"}[ping]{lang="EN-US"}[响应来判断是否存在地址冲突。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送目的地址为待分配地址的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文。如果在指定时间内收到回显响应报文，则认为存在地址冲突。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器从地址池中选择新的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并重复上述操作。如果在指定时间内没有收到回显响应报文，则继续发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文，直到发送的回显请求报文数目达到本命令配置的最大值。如果仍然没有收到回显响应报文，则将地址分配给客户端，从而确保客户端获得的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址唯一。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x911072349}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377317364}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器最多发送]{style="font-family:宋体"}[10]{lang="EN-US"}[个回显请求报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_207035350}

[\[Sysname\] dhcp server ping packets 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x90203010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp server ping timeout]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1943015298}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[display dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x876391964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[reset dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x685863543}
:::

::: {#610058936 .myid}
[]{#_Toc404786422}[]{#struct_0_x1331_x1769_x1389965106}[]{#_Toc269455523}[]{#_Toc266880174}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server ping timeout**

------------------------------------------------------------------------

[[[dhcp server ping timeout]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x557520206}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器等待回显响应报文的超时时间。]{style="font-family:宋体"}

[[[undo dhcp server ping timeout]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_908325481}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1377251828}

[[[dhcp server ping timeout ]{lang="EN-US"}]{.commandkeywordsChar}*[milliseconds]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1994666405}

[[undo dhcp server ping timeout]{lang="EN-US"}]{#struct_0_x1331_x1769_785246583}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1341602915}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_489946209}[服务器等待回显响应报文的超时时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_526015217}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1956654042}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1047113121}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376924148}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1876322850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2108785194}

[*[milliseconds]{lang="EN-US"}*]{#struct_0_x1331_x1769_x567648696}[：等待回显响应报文的超时时间，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端之前，不会通过]{style="font-family:宋体"}[ping]{lang="EN-US"}[操作探测该地址是否冲突。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1794802506}

[[为防止]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x528487907}[地址重复分配导致地址冲突，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为客户端分配地址前，需要先对该地址进行探测。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1193577660}[服务器的地址探测是通过]{style="font-family:宋体"}[ping]{lang="EN-US"}[功能实现的，通过检测是否能在指定时间内得到]{style="font-family:宋体"}[ping]{lang="EN-US"}[响应来判断是否存在地址冲突。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送目的地址为待分配地址的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文。如果在本命令指定的时间内收到回显响应报文，则认为存在地址冲突。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器从地址池中选择新的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并重复上述操作。如果在指定时间内没有收到回显响应报文，则继续发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[回显请求报文，直到发送的回显请求报文数目达到最大值。如果仍然没有收到回显响应报文，则将地址分配给客户端，从而确保客户端获取的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址唯一。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1334653793}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x616605967}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器等待回显响应报文的超时时间为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376858612}

[\[Sysname\] dhcp server ping timeout 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1880167122}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[dhcp server ping packets]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_133879074}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[display dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1600842562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[reset dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_256770178}
:::

::: {#-574273101 .myid}
[]{#_Toc404786423}[]{#struct_0_x1331_x1769_x1060258882}[]{#_Toc269455524}[]{#_Toc266880175}[]{#_Toc202081857}

**DHCP \-- DHCP服务器配置命令 \-- dhcp server relay information enable**

------------------------------------------------------------------------

[[[dhcp server relay information enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_849508275}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器处理]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[undo dhcp server relay information enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1971947781}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器忽略]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x986744081}

[[dhcp server relay information enable]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377055220}

[[undo dhcp server relay information enable]{lang="EN-US"}]{#struct_0_x1331_x1769_x1819924099}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_95745079}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1598450998}[服务器处理]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x501262287}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1024260223}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x8761158}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1604943472}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376989684}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1534200025}

[[当]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x640283743}[服务器收到含有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的报文时，如果]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器处理]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则将请求报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[原样复制到应答报文中；如果]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器忽略]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则不会在应答报文中携带]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1195875340}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2052240762}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器忽略]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1885792184}

[\[Sysname\] undo dhcp server relay information enable]{lang="EN-US"}
:::

::: {#1891607450 .myid}
[]{#_Toc404786424}[]{#struct_0_x1331_x1769_1651305492}[]{#_Toc269455525}[]{#_Toc266880176}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server conflict**

------------------------------------------------------------------------

[[[display dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x974397917}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[的地址冲突信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1973728986}

[[[display dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}[ \[[ ip]{.commandkeywordsChar} *ip-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376662004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_765216863}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_17150016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_74416333}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1127498062}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x261492956}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_819399293}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x898659800}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376596468}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_x168715558}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的地址冲突信息。如果不指定本参数，则显示所有的地址冲突信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1063659592}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的地址冲突信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的地址冲突信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2125817963}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2026196542}[服务器在下列几种情况下会生成地址冲突信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_615457845}[服务器在为客户端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前，通过]{style="font-family:宋体"}[ping]{lang="EN-US"}[操作检测到网络中已有主机使用该地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1630907290}[客户端向]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送]{style="font-family:宋体"}[Decline]{lang="EN-US"}[报文，报告]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为其分配的地址存在冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_68924969}[服务器检测到地址池内的可供分配的地址是设备自身的地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_870986045}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_221199997}[显示所有的地址冲突信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp server conflict]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377186291}

[IP address          Detect time]{lang="EN-US"}

[4.4.4.1             Apr 25 16:57:20 2007]{lang="EN-US"}

[4.4.4.2             Apr 25 17:00:10 2007]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display dhcp server conflict]{lang="EN-US"}]{#struct_0_x1331_x1769_x536956927}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1745552101}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_433387971}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1140469486}

[[IP address]{lang="EN-US"}]{#struct_0_x1331_x1769_996629709}

[[发生冲突的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_1637196250}[地址]{style="font-family:宋体"}

[[Detect time]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377120755}

[[检测到冲突的时间]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1853266024}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1758434897}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[reset dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x2044776405}

::: {#429157125 .myid}
[]{#_Toc404786425}[]{#struct_0_x1331_x1769_x1063594056}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server database**

------------------------------------------------------------------------

[**[display dhcp server database]{lang="EN-US"}**]{#struct_0_x1331_x1769_628409790}[命令用来显示]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[服务器的表项备份信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1505642562}

[**[display dhcp server database]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2087797922}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x231857124}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x828865208}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1078633483}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1024218776}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_501900058}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x162532311}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1747711396}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2023021425}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x581526532}[显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的表项备份信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp server database]{lang="EN-US"}]{#struct_0_x1331_x1769_361442817}

[ File name               :   database.dhcp]{lang="EN-US"}

[ Username                :   ]{lang="EN-US"}

[ Password                :   ]{lang="EN-US"}

[ Update interval         :   600 seconds]{lang="EN-US"}

[ Latest write time       :   Feb  8 16:09:53 2014]{lang="EN-US"}

[ Status                  :   Last write succeeded.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display dhcp server database]{lang="EN-US"}]{#struct_0_x1331_x1769_x733044223}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_327372559}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_501965594}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1721717436}

[[File name]{lang="EN-US"}]{#struct_0_x1331_x1769_113426144}

[[存储]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_501768986}[服务器表项的文件名称]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_x1331_x1769_1482106150}

[[配置远程目标文件时的用户名]{style="font-family:宋体"}]{#struct_0_x1331_x1769_501834522}

[[Password]{lang="EN-US"}]{#struct_0_x1331_x1769_1362514455}

[[配置远程目标文件时的密码，有配置时显示为]{style="font-family:宋体"}["\*\*\*\*\*\*"]{lang="EN-US"}]{#struct_0_x1331_x1769_501637914}

[[Update interval]{lang="EN-US"}]{#struct_0_x1331_x1769_1513890949}

[[定期刷新表项存储文件的刷新时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1719862304}

[[Latest write time]{lang="EN-US"}]{#struct_0_x1331_x1769_501703450}

[[最近一次写文件的时间]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1562822285}

[[Status]{lang="EN-US"}]{#struct_0_x1331_x1769_501506842}

[[写文件的状态，即写文件是否成功]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1112106757}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Writing]{lang="EN-US"}]{#struct_0_x1331_x1769_501572378}[[：正在写文件]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write succeeded.]{lang="EN-US"}]{#struct_0_x1331_x1769_502489882}[[：上一次写文件成功]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write failed.]{lang="EN-US"}]{#struct_0_x1331_x1769_501900057}[[：上一次写文件失败]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[ ]{lang="EN-US"}

::: {#686634791 .myid}
[]{#_Toc404786426}[]{#struct_0_x1331_x1769_x1203559345}[]{#_Toc269455526}[]{#_Toc266880177}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server expired**

------------------------------------------------------------------------

[[[display dhcp server expired]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x804168215}[命令用来显示租约过期的地址绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_448239032}

[[[display dhcp server expired ]{lang="EN-US"}]{.commandkeywordsChar}[\[ \[[ ip]{.commandkeywordsChar} *ip-address \] \[ vpn-instance vpn-instance-name \]* \| [pool]{.commandkeywordsChar} *pool-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_398811726}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1383740248}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1377317363}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1773119291}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1146428267}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_226289704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_636647044}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x177916473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x288440703}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_155534570}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的租约过期地址绑定信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_501965593}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的租约过期的地址绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的租约过期的地址绑定信息。]{style="font-family:宋体"}

[[[pool]{lang="EN-US"}]{.commandkeywordsChar}[ *pool-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1377251827}[：显示指定地址池中租约过期的地址绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x784812824}

[[执行本命令时，如果不指定任何参数，则显示所有租约过期的地址绑定信息。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x791913415}

[[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1203779401}[地址池的可用地址分配完后，租约过期的地址将被分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1243693132}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x993079562}[显示所有租约过期的地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp server expired]{lang="EN-US"}]{#struct_0_x1331_x1769_x9237556}

[IP address       Client-identifier/Hardware address    Lease expiration]{lang="EN-US"}

[4.4.4.6          3030-3066-2e65-3230-302e-3130-3234    Apr 25 17:10:47 2007]{lang="EN-US"}

[                 -2d45-7468-6572-6e65-7430-2f31]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display dhcp server expired]{lang="EN-US"}]{#struct_0_x1331_x1769_615695565}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1746241566}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376924147}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1208790865}

[[IP address]{lang="EN-US"}]{#struct_0_x1331_x1769_x2071387249}

[[租约过期的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_1145446980}[地址]{style="font-family:宋体"}

[[Client-identifier/Hardware address]{lang="EN-US"}]{#struct_0_x1331_x1769_1224574904}

[[租约过期的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1957338927}[或]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Lease expiration]{lang="EN-US"}]{#struct_0_x1331_x1769_x1376858611}

[[租约过期的时间]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x848716233}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1217549778}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[r]{lang="EN-US"}]{.commandkeywordsChar}**[eset dhcp server expired]{lang="EN-US"}**]{#struct_0_x1331_x1769_631649466}

::: {#1408438668 .myid}
[]{#_Toc404786427}[]{#struct_0_x1331_x1769_364362126}[]{#_Toc269455527}[]{#_Toc266880178}[]{#_Toc202081861}[]{#_Toc137350291}[]{#_Toc100214090}[]{#_Toc94500197}[]{#_Toc69790749}[]{#_Toc60058896}[]{#_Toc43546309}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server free-ip**

------------------------------------------------------------------------

[[[display dhcp server free-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1861201974}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池的空闲地址信息，即尚未分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1251817302}

[[[display dhcp server free-ip ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ pool ]{.commandkeywordsChar}*pool-name*[ ]{.commandkeywordsChar}\|[ vpn-instance ]{.commandkeywordsChar}vpn-instance-name[ ]{.commandkeywordsChar}\]]{lang="EN-US"}]{#struct_0_x1331_x1769_1106917713}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1170767723}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1377055219}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1265386224}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x656863341}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x588802761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1351132107}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_34518665}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1729865368}

[**[pool ]{lang="EN-US"}***[pool-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_1935041166}[：显示指定地址池的空闲地址信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有地址池的空闲地址信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_501834521}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的地址池空闲地址信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的地址池空闲地址信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376989683}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1130915498}[显示所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池的空闲地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp server free-ip]{lang="EN-US"}]{#struct_0_x1331_x1769_x1323275805}

[Pool name: 1]{lang="EN-US"}

[  Network: 10.0.0.0 mask 255.0.0.0]{lang="EN-US"}

[    IP ranges from 10.0.0.10 to 10.0.0.100]{lang="EN-US"}

[    IP ranges from 10.0.0.105 to 10.0.0.255]{lang="EN-US"}

[  Secondary networks:]{lang="EN-US"}

[    10.1.0.0 mask 255.255.0.0]{lang="EN-US"}

[      IP ranges from 10.1.0.0 to 10.1.0.255]{lang="EN-US"}

[    10.2.0.0 mask 255.255.0.0]{lang="EN-US"}

[      IP Ranges from 10.2.0.0 to 10.2.0.255]{lang="EN-US"}

[ ]{lang="EN-US"}

[Pool name: 2]{lang="EN-US"}

[  Network: 20.1.1.0 mask 255.255.255.0]{lang="EN-US"}

[    IP ranges from 20.1.1.0 to 20.1.1.255]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display dhcp server free-ip]{lang="EN-US"}]{#struct_0_x1331_x1769_2139913555}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1752937073}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2071231463}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1376662003}

[[Pool name]{lang="EN-US"}]{#struct_0_x1331_x1769_x800867078}

[[地址池的名称]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x464695372}

[[Network]{lang="EN-US"}]{#struct_0_x1331_x1769_1554278542}

[[可分配的地址网段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x594752978}

[[IP ranges]{lang="EN-US"}]{#struct_0_x1331_x1769_x1293665006}

[[可分配的地址范围]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1376596467}

[[Secondary networks]{lang="EN-US"}]{#struct_0_x1331_x1769_1397368383}

[[可分配的从地址网段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1474606064}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x645205919}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[address range]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_611955419}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[dhcp server ip-pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1587824322}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[network]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x787964416}

::: {#2095524992 .myid}
[]{#_Toc404786428}[]{#struct_0_x1331_x1769_204412857}[]{#_Toc269455528}[]{#_Toc266880219}[]{#_Toc202081863}[]{#_Toc137350292}[]{#_Toc100214091}[]{#_Toc94500198}[]{#_Toc69790750}[]{#_Toc60058897}[]{#_Toc43546310}[]{#_Toc37217593}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server ip-in-use**

------------------------------------------------------------------------

[[[display dhcp server ip-in-use]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_188897653}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1955176576}

[[[display dhcp server ip-in-use ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ ]{.commandkeywordsChar}\[[ ip]{.commandkeywordsChar} *ip-address*[ ]{.commandkeywordsChar}\][ ]{.commandkeywordsChar}\[ [vpn-instance]{.commandkeywordsChar} vpn-instance-name \][ ]{.commandkeywordsChar}\|[ pool ]{.commandkeywordsChar}*pool-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x342121516}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1191672473}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1645115281}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_564913629}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1839363863}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1185445417}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1872485168}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_188963189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_358935506}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_166835603}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的地址绑定信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_501703449}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[[[pool]{lang="EN-US"}]{.commandkeywordsChar}[ *pool-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1218113651}[：显示指定地址池的地址绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2797279}

[[执行本命令时，如果不指定任何参数，则显示所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1640524492}[地址绑定信息。]{style="font-family:宋体"}

[[需要注意的是，如果租约的截止时间超过]{style="font-family:宋体"}[2100]{lang="EN-US"}]{#struct_0_x1331_x1769_x329420595}[年，则显示为]{style="font-family:宋体"}[After 2100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2102722209}[服务器作为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的网关设备时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器上记录的该]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的地址绑定信息才会提供给其他安全特性（如]{style="font-family:宋体"}[IP Source Guard]{lang="EN-US"}[）使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_188766581}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2075639350}[显示所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp server ip-in-use]{lang="EN-US"}]{#struct_0_x1331_x1769_478285658}

[IP address       Client identifier/    Lease expiration      Type]{lang="EN-US"}

[                 Hardware address]{lang="EN-US"}

[10.1.1.1         4444-4444-4444        Not used              Static(F)]{lang="EN-US"}

[10.1.1.2         3030-3030-2e30-3030-  May 1 14:02:49 2009   Auto(C)]{lang="IT"}

[                 662e-3030-3033-2d45-]{lang="IT"}

[                 ]{lang="IT"}[7468-6572-6e65-74]{lang="EN-US"}

[10.1.1.3         1111-1111-1111        After 2100            Static(C)]{lang="EN-US"}

[]{#struct_0_x1331_x1769_66406964}[]{#_Toc138412525}[[表1-5 ]{lang="EN-US"}[display dhcp serve]{lang="EN-US"}]{#_Toc54497773}[r ip-in-use]{lang="EN-US"}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_x1750905190}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1484097652}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1124118018}

[[IP address]{lang="EN-US"}]{#struct_0_x1331_x1769_188832117}

[[分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_382069807}[客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Client identifier/Hardware address]{lang="EN-US"}]{#struct_0_x1331_x1769_46518397}

[[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x236043034}[或客户端的硬件地址]{style="font-family:宋体"}

[[Lease expiration]{lang="EN-US"}]{#struct_0_x1331_x1769_x438217141}

[[租约到期时间，取值包括：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_37127196}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[具体的时间值（如]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2144413030}[May 1 14:02:49 2009]{lang="EN-US"}[）：表示租约在该时间到期]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Not used]{lang="EN-US"}]{#struct_0_x1331_x1769_189159797}[：表示静态绑定的地址尚未分配给特定客户端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Unlimited]{lang="EN-US"}]{#struct_0_x1331_x1769_x819278688}[：表示租约为无限长]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[After 2100]{lang="EN-US"}]{#struct_0_x1331_x1769_x886737205}[：表示租约过期时间超过]{style="font-family:
  宋体"}[2100]{lang="EN-US"}[年]{style="font-family:
  宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1331_x1769_x1006001442}

[[地址绑定的类型，取值包括：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_648185871}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Static(F)]{lang="EN-US"}]{#struct_0_x1331_x1769_189225333}[：表示尚未分配给客户端的静态绑定，即静态无效绑定]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Static(O)]{lang="EN-US"}]{#struct_0_x1331_x1769_x1393034469}[：服务器从地址池选择静态绑定的]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址，并发送]{style="font-family:
  宋体"}[DHCP-OFFER]{lang="EN-US"}[报文为客户端提供该]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址后产生该类型的地址绑定信息，即静态临时绑定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Static(C)]{lang="EN-US"}]{#struct_0_x1331_x1769_x1762735409}[：表示已经分配给客户端的静态绑定，即静态正式绑定]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Auto(O)]{lang="EN-US"}]{#struct_0_x1331_x1769_1095255491}[：表示动态绑定的临时租约，即从地址池中动态选择]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址，并发送]{style="font-family:宋体"}[DHCP-OFFER]{lang="EN-US"}[报文为客户端提供该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，产生的租约]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Auto(C)]{lang="EN-US"}]{#struct_0_x1331_x1769_688109239}[：表示动态绑定的正式租约，即从地址池中动态选择]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址，并发送]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[报文成功将该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配给客户端后，产生的租约]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_191721664}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset dhcp server ip-in-use]{lang="EN-US"}**]{#struct_0_x1331_x1769_189028725}

::: {#1664471496 .myid}
[]{#_Toc404786429}[]{#struct_0_x1331_x1769_1880214925}[]{#_Toc283109634}[]{#_Toc266880221}[]{#_Toc202081865}[]{#_Toc137350294}[]{#_Toc100214093}[]{#_Toc94500200}[]{#_Toc69790752}[]{#_Toc60058899}[]{#_Toc43546312}[]{#_Toc37217595}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server pool**

------------------------------------------------------------------------

[[[display dhcp server pool]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1350322718}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x133612545}

[[[display dhcp server pool]{lang="EN-US"}]{.commandkeywordsChar}[ \[[ ]{.commandkeywordsChar}*pool-name* \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_900844559}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1117288436}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_555428739}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_247718938}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x318173510}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_189094261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1492872785}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x203788681}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1084790373}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_186545944}[：显示指定地址池的信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有地址池的信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_502424345}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x738385145}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1459119290}[显示所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp server pool]{lang="EN-US"}]{#struct_0_x1331_x1769_189487477}

[Pool name: 0]{lang="EN-US"}

[  Network 20.1.1.0 mask 255.255.255.0]{lang="EN-US"}

[  class a range 20.1.1.50 20.1.1.60]{lang="EN-US"}

[  bootfile-name abc.cfg]{lang="EN-US"}

[  dns-list 20.1.1.66 20.1.1.67 20.1.1.68]{lang="EN-US"}

[  domain-name www.aabbcc.com]{lang="EN-US"}

[  bims-server ip 192.168.0.51 sharekey cipher \$c\$3\$K13OmQPi791YvQoF2Gs1E+65LOU=]{lang="EN-US"}

[  option 2 ip-address 1.1.1.1]{lang="EN-US"}

[  expired 1 2 3 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Pool name: 1]{lang="EN-US"}

[  Network 20.1.1.0 mask 255.255.255.0]{lang="EN-US"}

[  secondary networks:]{lang="EN-US"}

[    ]{lang="EN-US"}[20.1.2.0 mask 255.255.255.0]{lang="DA"}

[    20.1.3.0 mask 255.255.255.0]{lang="DA"}

[  bims-server ip 192.168.0.51 port 50 sharekey cipher \$c\$3\$K13OmQPi791YvQoF2Gs1E+65LOU=]{lang="DA"}

[  forbidden-ip 20.1.1.22 20.1.1.36 20.1.1.37]{lang="DA"}

[  forbidden-ip 20.1.1.22 20.1.1.23 20.1.1.24]{lang="DA"}

[  ]{lang="DA"}[gateway-list 1.1.1.1 2.2.2.2 4.4.4.4]{lang="EN-US"}

[  nbns-list 5.5.5.5 6.6.6.6 7.7.7.7]{lang="EN-US"}

[  netbios-type m-node]{lang="EN-US"}

[  option 2 ip-address 1.1.1.1]{lang="EN-US"}

[  expired 1 0 0 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Pool name: 2]{lang="EN-US"}

[  Network 20.1.1.0 mask 255.255.255.0]{lang="EN-US"}

[  address range 20.1.1.1 to 20.1.1.15]{lang="EN-US"}

[  class departmentA range 20.1.1.20 to 20.1.1.29]{lang="EN-US"}

[  class departmentB range 20.1.1.30 to 20.1.1.40]{lang="EN-US"}

[  next-server 20.1.1.33]{lang="EN-US"}

[  tftp-server domain-name www.dian.org.cn]{lang="EN-US"}

[  tftp-server ip-address 192.168.0.120]{lang="EN-US"}

[  voice-config ncp-ip 10.1.1.2]{lang="EN-US"}

[  voice-config as-ip 10.1.1.5]{lang="EN-US"}

[  voice-config voice-vlan 3 enable]{lang="EN-US"}

[  voice-config fail-over 10.1.1.1 123\*]{lang="EN-US"}

[  option 2 ip-address 1.1.1.3]{lang="EN-US"}

[  expired 1 0 0 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Pool name: 3]{lang="EN-US"}

[  static bindings:]{lang="EN-US"}

[    ip-address 10.10.1.2 mask 255.0.0.0]{lang="EN-US"}

[      hardware-address 00e0-00fc-0001 ethernet]{lang="EN-US"}

[    ip-address 10.10.1.3 mask 255.0.0.0]{lang="EN-US"}

[      client-identifier aaaa-bbbb]{lang="EN-US"}

[  expired unlimited]{lang="EN-US"}

[]{#struct_0_x1331_x1769_792734230}[]{#_Toc138412527}[[表1-6 ]{lang="EN-US"}[display dhcp server pool]{lang="EN-US"}]{#_Toc54497775}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_x1757404666}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x518454481}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1067145968}

[[Pool name]{lang="EN-US"}]{#struct_0_x1331_x1769_188897654}

[[地址池的名称]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1955176571}

[[Network]{lang="EN-US"}]{#struct_0_x1331_x1769_x1101636403}

[[可分配的地址网段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x119253083}

[[secondary networks]{lang="EN-US"}]{#struct_0_x1331_x1769_x1172474846}

[[可分配的从地址网段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1405617532}

[[address range]{lang="EN-US"}]{#struct_0_x1331_x1769_188963190}

[[可分配的地址范围]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1979716661}

[[class *class-name* range]{lang="EN-US"}]{#struct_0_x1331_x1769_x1840914256}

[[为指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_33898994}[用户类分配的地址范围]{style="font-family:宋体"}

[[static bindings]{lang="EN-US"}]{#struct_0_x1331_x1769_1093482286}

[[静态绑定的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1492750597}[地址、硬件地址或客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[option]{lang="EN-US"}]{#struct_0_x1331_x1769_188766582}

[[自定义的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2075639349}[选项]{style="font-family:宋体"}

[[expired]{lang="EN-US"}]{#struct_0_x1331_x1769_477826905}

[[租约期限，其后数值的单位分别为天、小时、分钟和秒。例如，]{style="font-family:宋体"}[expired 1 2 3 4]{lang="EN-US"}]{#struct_0_x1331_x1769_1868695245}[表示租约期限为]{style="font-family:宋体"}[1]{lang="EN-US"}[天]{style="font-family:宋体"}[2]{lang="EN-US"}[小时]{style="font-family:宋体"}[3]{lang="EN-US"}[分钟]{style="font-family:宋体"}[4]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[bootfile-name]{lang="EN-US"}]{#struct_0_x1331_x1769_905091725}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_188832118}[客户端分配的启动文件名]{style="font-family:宋体"}

[[dns-list]{lang="EN-US"}]{#struct_0_x1331_x1769_382069800}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_46518392}[客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}

[[domain-name]{lang="EN-US"}]{#struct_0_x1331_x1769_x1427684122}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1043095727}[客户端分配的域名后缀]{style="font-family:宋体"}

[[bims-server ]{lang="EN-US"}]{#struct_0_x1331_x1769_189159798}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x819278675}[客户端分配的]{style="font-family:宋体"}[BIMS]{lang="EN-US"}[服务器信息]{style="font-family:宋体"}

[[forbidden-ip]{lang="EN-US"}]{#struct_0_x1331_x1769_x886409524}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_193860783}[地址池中不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[gateway-list]{lang="EN-US"}]{#struct_0_x1331_x1769_189225334}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1393034462}[客户端分配的网关地址]{style="font-family:宋体"}

[[nbns-list]{lang="EN-US"}]{#struct_0_x1331_x1769_x1809789576}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1118636913}[客户端分配的]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}

[[netbios-type]{lang="EN-US"}]{#struct_0_x1331_x1769_189028726}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1880214924}[客户端分配的]{style="font-family:宋体"}[NetBIOS]{lang="EN-US"}[节点类型]{style="font-family:宋体"}

[[next-server]{lang="EN-US"}]{#struct_0_x1331_x1769_1350257182}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_259847438}[客户端分配的下一个提供服务的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[tftp-server domain-name]{lang="EN-US"}]{#struct_0_x1331_x1769_189094262}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1492872782}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器名]{style="font-family:宋体"}

[[tftp-server ip-address]{lang="EN-US"}]{#struct_0_x1331_x1769_x204247433}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_200167054}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}

[[voice-config ncp-ip]{lang="EN-US"}]{#struct_0_x1331_x1769_189421942}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2028617594}[客户端分配的网络呼叫处理器的地址]{style="font-family:宋体"}

[[voice-config as-ip]{lang="EN-US"}]{#struct_0_x1331_x1769_x583552257}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1022778263}[客户端分配的备用服务器的地址]{style="font-family:宋体"}

[[voice-config voice-vlan]{lang="EN-US"}]{#struct_0_x1331_x1769_189487478}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_792734233}[客户端分配的语音]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[voice-config fail-over]{lang="EN-US"}]{#struct_0_x1331_x1769_x518454482}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_188897651}[客户端分配的自动故障转移呼叫路由]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1481043012 .myid}
[]{#_Toc404786430}[]{#struct_0_x1331_x1769_x1955176574}[]{#_Toc283109633}[]{#_Toc266880220}[]{#_Toc202081864}[]{#_Toc137350293}[]{#_Toc100214092}[]{#_Toc94500199}[]{#_Toc69790751}[]{#_Toc60058898}[]{#_Toc43546311}[]{#_Toc37217594}

**DHCP \-- DHCP服务器配置命令 \-- display dhcp server statistics**

------------------------------------------------------------------------

[[[display dhcp server statistics]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1504920930}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1494764373}

[**[display dhcp server statistics]{lang="EN-US"}**[ \[ **pool** *pool-name* \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x955175347}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x917394693}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x465460047}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x353689272}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1879039223}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_188963187}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_358935492}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_923615484}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1567187100}

[**[pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x740260887}[：显示指定地址池的统计信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有地址池的统计信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_501834524}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示显示的是公网中的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_997920931}

[[\# ]{lang="FR"}]{#struct_0_x1331_x1769_1639332189}[显示]{style="font-family:宋体"}[DHCP]{lang="FR"}[服务器的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp server statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_188766579}

[    Pool number:                       1]{lang="EN-US"}

[    Pool utilization:                  0.39%]{lang="EN-US"}

[    Bindings:]{lang="EN-US"}

[      Automatic:                       1]{lang="EN-US"}

[      Manual:                          0]{lang="EN-US"}

[      Expired:                         0]{lang="EN-US"}

[    Conflict:                          1]{lang="EN-US"}

[    Messages received:                10]{lang="EN-US"}

[      DHCPDISCOVER:                    5]{lang="EN-US"}

[      DHCPREQUEST:                     3]{lang="EN-US"}

[      DHCPDECLINE:                     0]{lang="EN-US"}

[      DHCPRELEASE:                     2]{lang="EN-US"}

[      DHCPINFORM:                      0]{lang="EN-US"}

[      BOOTPREQUEST:                    0]{lang="EN-US"}

[    Messages sent:                     6]{lang="EN-US"}

[      DHCPOFFER:                       3]{lang="EN-US"}

[      DHCPACK:                         3]{lang="EN-US"}

[      DHCPNAK:                         0]{lang="EN-US"}

[      BOOTPREPLY:                      0]{lang="EN-US"}

[    Bad Messages:                      0]{lang="EN-US"}

[]{#struct_0_x1331_x1769_1355595326}[]{#_Toc138412526}[[表1-7 ]{lang="EN-US"}[display dhcp server statistics]{lang="EN-US"}]{#_Toc54497774}[命令显示信息描述]{style="font-family:
黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_x1462583338}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1576870555}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1747569292}

[[Pool number]{lang="EN-US"}]{#struct_0_x1331_x1769_188832115}

[[地址池的数目，显示指定地址池的统计信息时无此字段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_382069805}

[[Pool utilization]{lang="EN-US"}]{#struct_0_x1331_x1769_46518395}

[[地址池利用率]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x618380058}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[显示所有]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1707594326}[DHCP]{lang="EN-US"}[租约统计信息时，表示所有地址池的总体利用率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[显示指定地址池的租约统计信息时，表示该地址池的利用率]{style="font-family:宋体"}]{#struct_0_x1331_x1769_19592628}

[[Bindings]{lang="EN-US"}]{#struct_0_x1331_x1769_189159795}

[[各种状态的地址绑定数，包括：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x819278686}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Automatic]{lang="EN-US"}]{#struct_0_x1331_x1769_x886606133}[：动态分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址绑定数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Manual]{lang="EN-US"}]{#struct_0_x1331_x1769_x1781125537}[：手工绑定的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址绑定数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Expired]{lang="EN-US"}]{#struct_0_x1331_x1769_170499001}[：租约过期的]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址绑定数]{style="font-family:宋体"}

[[Conflict]{lang="EN-US"}]{#struct_0_x1331_x1769_x635886911}

[[冲突地址的总数，显示指定地址池的统计信息时无此字段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_189225331}

[[Messages received]{lang="EN-US"}]{#struct_0_x1331_x1769_x1393034467}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2081893193}[服务器接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发送的报文数，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPDISCOVER]{lang="EN-US"}]{#struct_0_x1331_x1769_2001073495}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPREQUEST]{lang="EN-US"}]{#struct_0_x1331_x1769_1024762567}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[DHCPDECLINE]{lang="EN-US"}]{#struct_0_x1331_x1769_189028723}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPRELEASE]{lang="EN-US"}]{#struct_0_x1331_x1769_1880214919}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPINFORM]{lang="EN-US"}]{#struct_0_x1331_x1769_1351109151}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[BOOTPREQUEST]{lang="EN-US"}]{#struct_0_x1331_x1769_209081652}

[[显示指定地址池的统计信息时无此类字段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1753560156}

[[Messages sent]{lang="EN-US"}]{#struct_0_x1331_x1769_189094259}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x81105319}[服务器发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的报文数，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[DHCPOFFER]{lang="EN-US"}]{#struct_0_x1331_x1769_99251167}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPACK]{lang="EN-US"}]{#struct_0_x1331_x1769_2038643670}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[DHCPNAK]{lang="EN-US"}]{#struct_0_x1331_x1769_189421939}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BOOTPREPLY]{lang="EN-US"}]{#struct_0_x1331_x1769_x1074708621}

[[显示指定地址池的统计信息时无此类字段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_542738383}

[[Bad Messages]{lang="EN-US"}]{#struct_0_x1331_x1769_1579712723}

[[错误信息数，显示指定地址池的统计信息时无此类字段]{style="font-family:宋体"}]{#struct_0_x1331_x1769_37232089}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_189487475}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset dhcp server statistics]{lang="FR"}**]{#struct_0_x1331_x1769_792734228}

::: {#1424336882 .myid}
[]{#_Toc404786431}[]{#struct_0_x1331_x1769_1820197687}[]{#_Toc283109635}[]{#_Toc266880222}[]{#_Toc202081866}[]{#_Toc137350295}[]{#_Toc100214094}[]{#_Toc94500201}[]{#_Toc69790753}[]{#_Toc60058900}[]{#_Toc43546313}[]{#_Toc37217596}

**DHCP \-- DHCP服务器配置命令 \-- dns-list**

------------------------------------------------------------------------

[[[dns-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_110346014}[命令用来[]{#_Toc54599392}[]{#_Toc37143957}[]{#_Toc34553522}[]{#_Toc28082449}[配置]{#_Toc18146916}]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[[undo dns-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x2049563806}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_827126612}

[[[dns-list]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_1695091318}

[[[undo dns-list]{lang="EN-US"}]{.commandkeywordsChar}[ \[ *ip-address*&\<1-8\> \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x498867182}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_188897652}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1955176577}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1908205457}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2011094863}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1975334122}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_911426776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x2063231092}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1410917688}

[*[ip-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_188963188}[：]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_358935507}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_166835602}

[[执行]{style="font-family:宋体"}**[undo [dns-list]{.commandkeywordsChar}]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1218113650}[命令时，如果没有指定任何参数，则删除]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[地址池中的所有]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1563286662}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1283846223}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[10.1.1.254]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x351654099}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] dns-list 10.1.1.254]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1698553754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_188766580}
:::

::: {#700735607 .myid}
[]{#_Toc404786432}[]{#struct_0_x1331_x1769_2075639351}[]{#_Toc283109636}[]{#_Toc266880223}[]{#_Toc202081867}[]{#_Toc137350296}[]{#_Toc100214095}[]{#_Toc94500202}[]{#_Toc69790754}[]{#_Toc60058901}[]{#_Toc43546314}[]{#_Toc37217597}[]{#_Toc30751522}[]{#_Toc15982551}[]{#_Toc14684610}

**DHCP \-- DHCP服务器配置命令 \-- domain-name**

------------------------------------------------------------------------

[[[domain-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_478351194}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的域名。]{style="font-family:宋体"}

[[[undo domain-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1278138160}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的域名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1140027374}

[[[domain-name]{lang="EN-US"}]{.commandkeywordsChar}[ *domain-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_2043921385}

[[undo domain-name]{lang="EN-US"}]{#struct_0_x1331_x1769_x54547809}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_78100014}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_188832116}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的域名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_382069806}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_46518398}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_955598054}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x576240635}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1375601115}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_106348585}

[*[domain-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1130915254}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[50]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_289600165}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_189159796}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x819278689}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x886671669}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的域名为]{style="font-family:宋体"}[company.com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1411466807}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] domain-name company.com]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2102853677}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_681091533}
:::

::: {#474877911 .myid}
[]{#_Toc404786433}[]{#struct_0_x1331_x1769_x1482668523}[]{#_Toc283109637}[]{#_Toc266880224}[]{#_Toc202081868}[]{#_Toc137350297}[]{#_Toc100214096}[]{#_Toc94500203}[]{#_Toc69790755}[]{#_Toc60058902}[]{#_Toc43546315}[]{#_Toc37217598}

**DHCP \-- DHCP服务器配置命令 \-- expired**

------------------------------------------------------------------------

[[[expired]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1637625253}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池中分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的租约有效期限。]{style="font-family:宋体"}

[[[undo expired]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_189225332}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1393034468}

[[[expired ]{lang="EN-US"}]{.commandkeywordsChar}[{[ day ]{.commandkeywordsChar}*day*[ ]{.commandkeywordsChar}\[[ hour]{.commandkeywordsChar} *hour*[ ]{.commandkeywordsChar}\[[ minute]{.commandkeywordsChar} *minute* \[ **second** *second* \] \] \] \|[ unlimited ]{.commandkeywordsChar}}]{lang="EN-US"}]{#struct_0_x1331_x1769_966147946}

[[undo expired]{lang="EN-US"}]{#struct_0_x1331_x1769_583352496}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_123613714}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x412895441}[地址池中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的租约有效期限为]{style="font-family:宋体"}[1]{lang="EN-US"}[天。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x446418706}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1046956506}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_189028724}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1880214926}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1350388254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x201799159}

[[[day]{lang="EN-US"}]{.commandkeywordsChar}[ *day*]{lang="EN-US"}]{#struct_0_x1331_x1769_823528181}[：指定租约过期的天数，]{style="font-family:宋体"}*[day]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[365]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[hour]{lang="EN-US"}]{.commandkeywordsChar}[ *hour*]{lang="EN-US"}]{#struct_0_x1331_x1769_1669315148}[：指定租约过期的小时数，]{style="font-family:宋体"}*[hour]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[minute]{lang="EN-US"}]{.commandkeywordsChar}[ *minute*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1215849735}[：指定租约过期的分钟数，]{style="font-family:宋体"}*[minute]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[second ]{lang="EN-US"}]{.commandkeywordsChar}*[second]{lang="EN-US"}*]{#struct_0_x1331_x1769_343665426}[：指定租约过期的秒数，]{style="font-family:宋体"}*[second]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[unlimited]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x941540747}[：有效期限为无限长（实际上系统限定约为]{style="font-family:宋体"}[136]{lang="EN-US"}[年）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_189094260}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1492872784}[服务器从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池中选择]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端时，会同时将该地址池中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的租约有效期限通知给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端。在租约有效期限到达之前，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端需要进行续约申请。如果续约成功，则]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端可以继续使用该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。否则，租约有效期限到达后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端不能再继续使用该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并且]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器会将该地址添加到过期租约信息中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x203854217}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1999125423}[配置地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约有效期为]{style="font-family:宋体"}[1]{lang="EN-US"}[天]{style="font-family:宋体"}[2]{lang="EN-US"}[小时]{style="font-family:
宋体"}[3]{lang="EN-US"}[分]{style="font-family:宋体"}[4]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2011788306}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] expired day 1 hour 2 minute 3 second 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x74736291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display [dhcp server expired]{.commandkeywordsChar}]{lang="EN-US"}**]{#struct_0_x1331_x1769_2145986517}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_x784827799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[reset dhcp server expired]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_189421940}
:::

::: {#-137896786 .myid}
[]{#_Toc404786434}[]{#struct_0_x1331_x1769_2028617596}[]{#_Toc283109638}[]{#_Toc266880225}

**DHCP \-- DHCP服务器配置命令 \-- forbidden-ip**

------------------------------------------------------------------------

[[[forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x583421185}[命令用来配置指定地址池中不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[undo forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1334789748}[命令用来取消指定地址池中不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x276671303}

[[[forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_558075430}

[[[undo forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}[ \[ *ip-address*&\<1-8\>[ ]{.commandkeywordsChar}\]]{lang="EN-US"}]{#struct_0_x1331_x1769_1503803776}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x379539891}

[[没有配置指定地址池中不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_177924342}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_189487476}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_792734231}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x518454480}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1067080432}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_796158447}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1258621974}

[*[ip-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_x1698713555}[：地址池中不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x489579490}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_188897649}[地址池视图下通过]{lang="EN-US" style="font-family:宋体"}[[forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}[命令配置不参与自动分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，只有当前的地址池不能分配这些]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址，其他地址池仍然可以分配这些]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次执行]{lang="EN-US" style="font-family:宋体"}[[forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1138570}[命令，可以配置多个不参与自动分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。每个地址池最多能配置]{lang="EN-US" style="font-family:宋体"}[4096]{lang="EN-US"}[个地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}[[undo forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1590098597}[命令时，如果没有指定任何参数，则删除所有不参与自动分配的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1770903029}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2003019900}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[中不参与自动分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.1.3]{lang="EN-US"}[和]{style="font-family:宋体"}[192.168.1.10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x278581028}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] forbidden-ip 192.168.1.3 192.168.1.10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1575449149}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[dhcp server forbidden-ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x935900824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_188963185}
:::

::: {#-452439128 .myid}
[]{#_Toc404786435}[]{#struct_0_x1331_x1769_358935494}[]{#_Toc283109639}[]{#_Toc266880226}[]{#_Toc202081869}[]{#_Toc137350298}[]{#_Toc100214097}[]{#_Toc94500204}[]{#_Toc69790756}[]{#_Toc60058903}[]{#_Toc43546316}[]{#_Toc37217599}

**DHCP \-- DHCP服务器配置命令 \-- gateway-list**

------------------------------------------------------------------------

[[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_923615478}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址。]{style="font-family:宋体"}

[[[undo gateway-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x2007736160}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x820527748}

[[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*[&\<1-8\> \[ **export-route** \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1873376094}

[[[undo gateway-list]{lang="EN-US"}]{.commandkeywordsChar}[ \[ *ip-address*&\<1-8\> \] \[ **export-route** \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x11419214}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2057443104}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_334431658}[地址池、]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[从网段下均没有配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_188766577}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1355595312}[地址池视图]{style="font-family:宋体"}[/DHCP]{lang="EN-US"}[从网段视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1576608408}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_386569379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1149720236}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x697651611}

[*[ip-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_602649036}[：网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[**[export-route]{lang="EN-US"}**]{#struct_0_x1331_x1769_501637915}[：将网关列表信息下发给地址管理，通过应答客户端的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求，即可实现对不同类型的业务流量的引导。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1616701987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_188832113}[地址池视图下执行]{style="font-family:宋体"}[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}[命令，配置的是为地址池中所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址。如果用户需要为地址池下某个从网段的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配其它的网关地址，可以在地址池的从网段视图下执行]{style="font-family:宋体"}[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}[命令。如果在地址池视图和从网段视图下都配置了网关地址，则优先将从网段视图下配置的网关地址分配给从网段的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_382069811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}[[undo gateway-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1909796745}[命令时，如果没有指定任何参数，则删除所有配置的网关地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[网关地址应该和可分配的地址在同一网段。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_818311324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1513890950}**[gateway-list export-route]{lang="EN-US"}**[命令可以用来发布网关路由，如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x265741181}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_165910026}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1964694281}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] gateway-list 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2146721669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_189159793}
:::

::: {#-1354469580 .myid}
[]{#_Toc404786436}[]{#struct_0_x1331_x1769_x819278684}[]{#_Toc283109640}[]{#_Toc266880227}

**DHCP \-- DHCP服务器配置命令 \-- if-match**

------------------------------------------------------------------------

[[[if-match]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x886475061}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类的匹配规则。]{style="font-family:宋体"}

[[[undo if-match]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x232354825}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1030361032}

[[[if-match rule ]{lang="EN-US"}]{.commandkeywordsChar}*[rule-number]{lang="EN-US"}*[[ ]{lang="EN-US"}]{.commandkeywordsChar}[[{]{lang="EN-US" style="font-weight:normal"}[ option]{lang="EN-US"}]{.commandkeywordsChar}[ *option-code*[ ]{.commandkeywordsChar}\[[ hex]{.commandkeywordsChar} *hex-string*[ ]{.commandkeywordsChar}\[ [mask ]{.commandkeywordsChar}*mask*[ \| offset ]{.commandkeywordsChar}*offset* [length]{.commandkeywordsChar} *length* \] \] \| **hardware-address** *hardware-address* **mask** *hardware-address-mask* }]{lang="EN-US"}]{#struct_0_x1331_x1769_189225329}

[[[undo if-match rule ]{lang="EN-US"}]{.commandkeywordsChar}*[rule-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_563280661}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1232529031}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1715292162}[用户类的匹配规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_189028721}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1880214921}[用户类视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1350584862}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_264196604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_62093925}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1261578767}

[[[rule ]{lang="EN-US"}]{.commandkeywordsChar}*[rule-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_189094257}[：匹配规则编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。编号越小，匹配优先级越高。]{style="font-family:宋体"}

[[[option]{lang="EN-US"}]{.commandkeywordsChar}*[ option-code]{lang="EN-US"}*]{#struct_0_x1331_x1769_x81105325}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项的数值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[。]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*[用于指定匹配]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端时从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文中获取哪个选项。]{style="font-family:宋体"}

[[[hex]{lang="EN-US"}]{.commandkeywordsChar}[ *hex-string*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1474726941}[：指定用来匹配报文中指定选项的内容。]{style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[为十六进制数串，位数的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[之间的偶数。]{style="font-family:宋体"}

[[[mask]{lang="EN-US"}]{.commandkeywordsChar}[ *mask*]{lang="EN-US"}]{#struct_0_x1331_x1769_1245812038}[：指定与选项内容匹配时使用的掩码。]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为十六进制掩码数串，位数的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[之间的偶数。]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[的长度必须和]{style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[长度相同。]{style="font-family:宋体"}

[[[offset]{lang="EN-US"}]{.commandkeywordsChar}[ *offset*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1098622567}[：指定匹配]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端时获取选项内容的起始位置。]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[为选项内容偏移量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[，单位为字节。如果不指定本参数，则表示从选项值第一字节开始匹配整个选项的内容。]{style="font-family:宋体"}

[[[length]{lang="EN-US"}]{.commandkeywordsChar}[ *length*]{lang="EN-US"}]{#struct_0_x1331_x1769_1463223223}[：指定匹配]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端时获取选项内容的长度。]{style="font-family:宋体"}*[length]{lang="EN-US"}*[为选项内容的长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，单位为字节。指定的选项内容长度必须和]{style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[长度相同。]{style="font-family:宋体"}

[**[hardware-address]{lang="EN-US"}**[ *hardware-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_13926503}[：指定匹配规则的硬件地址。]{style="font-family:宋体"}*[hardware-address]{lang="EN-US"}*[表示客户端的硬件地址，为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[39]{lang="EN-US"}[个字符的字符串，字符串只能包含十六进制数和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，且形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[，除最后一个]{style="font-family:宋体"}[H]{lang="EN-US"}[表示]{style="font-family:宋体"}[2]{lang="EN-US"}[位或]{style="font-family:宋体"}[4]{lang="EN-US"}[位十六进制数外，其他均表示]{style="font-family:宋体"}[4]{lang="EN-US"}[位十六进制数。例如：]{style="font-family:宋体"}[aabb-ccdd-ee]{lang="EN-US"}[为有效的硬件地址，]{style="font-family:宋体"}[aabb-c-dddd]{lang="EN-US"}[和]{style="font-family:宋体"}[aabb-cc-dddd]{lang="EN-US"}[为无效的客户端硬件地址。]{style="font-family:宋体"}

[**[mask ]{lang="EN-US"}***[hardware-address-mask]{lang="EN-US"}*]{#struct_0_x1331_x1769_1593592046}[：指定匹配规则的硬件地址掩码。长度需要与]{style="font-family:宋体"}*[hardware-address]{lang="EN-US"}*[保持一致。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1415990819}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_189421937}[服务器通过将]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发送的报文与本命令配置的规则匹配，来判断]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端属于的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类视图下通过多次执行]{style="font-family:宋体"}[[if-match]{lang="EN-US"}]{.commandkeywordsChar}[命令，可以配置多条匹配规则。只要任意一条规则匹配成功，就认为该]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端属于该用户类。]{style="font-family:宋体"}

[[将报文与某一条]{style="font-family:宋体"}**[if-match option]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1074708611}[命令配置的规则匹配的方式为：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则中只指定了]{style="font-family:宋体"}]{#struct_0_x1331_x1769_542803919}*[option-code]{lang="EN-US"}*[参数，则只要报文中包括该选项，就认为匹配成功。]{style="font-family:宋体"}[否则，匹配失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则中只指定了]{lang="EN-US" style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_x1331_x1769_1411660886}[和]{lang="EN-US" style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[参数，则报文中指定选项的值开始的字节与]{lang="EN-US" style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[相同时，认为匹配成功。否则，匹配失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则中指定了]{lang="EN-US" style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_x1331_x1769_x267582229}[、]{lang="EN-US" style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[offset]{lang="EN-US"}*[和]{lang="EN-US" style="font-family:宋体"}*[length]{lang="EN-US"}*[参数，则将指定选项值的第]{lang="EN-US" style="font-family:宋体"}*[offset]{lang="EN-US"}*[+1]{lang="EN-US"}[位到]{lang="EN-US" style="font-family:宋体"}*[offset]{lang="EN-US"}*[+*length*]{lang="EN-US"}[位的内容与]{lang="EN-US" style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[比较，二者相同时，认为匹配成功。否则，匹配失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则中指定了]{lang="EN-US" style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_x1331_x1769_815794777}[、]{lang="EN-US" style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[mask]{lang="EN-US"}*[参数，则将指定选项值的第]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[位到]{lang="EN-US" style="font-family:宋体"}*[mask]{lang="EN-US"}*[长度]{lang="EN-US" style="font-family:宋体"}[-1]{lang="EN-US"}[位的内容与]{lang="EN-US" style="font-family:宋体"}*[mask]{lang="EN-US"}*[进行与运算，将结果与]{lang="EN-US" style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[与]{lang="EN-US" style="font-family:宋体"}*[mask]{lang="EN-US"}*[与运算的结果比较，二者相同时，认为匹配成功。否则，匹配失败。]{lang="EN-US" style="font-family:宋体"}

[[将报文与某一条]{style="font-family:宋体"}**[if-match hardware-address]{lang="EN-US"}**]{#struct_0_x1331_x1769_13926502}[命令配置的规则匹配的方式为：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[匹配硬件地址类型，目前只支持以太类型的硬件地址（即]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x745060114}[MAC]{lang="EN-US"}[地址）匹配，非以太类型的硬件地址均会匹配失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果报文中的客户端硬件地址与配置的客户端硬件地址及硬件地址掩码匹配，则认为匹配成功。否则，匹配失败。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1508249706}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[匹配时报文中的客户端硬件地址长度与配置规则中的硬件地址长度一致时才进行匹配，否则直接认为不匹配。如匹配规则为]{style="font-family:宋体"}]{#struct_0_x1331_x1769_351288734}**[if-match rule]{lang="EN-US"}**[ 1 **hardware-address** 0094-0000 **mask** ffff-0000]{lang="EN-US"}[，需匹配硬件地址长度为]{style="font-family:宋体"}[4]{lang="EN-US"}[字节的用户；若报文中客户端硬件地址长度为]{style="font-family:宋体"}[6]{lang="EN-US"}[字节（比如]{style="font-family:宋体"}[0094-0000-0010]{lang="EN-US"}[），则认为匹配失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[匹配硬件地址时，可以配置不连续匹配的硬件地址，如匹配规则为]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1665494993}**[if-match rule]{lang="EN-US"}**[ 1 **hardware-address** 0094-0000-1100 **mask** ffff-0000-ff00]{lang="EN-US"}[，则匹配硬件地址为]{style="font-family:宋体"}[0094-xxxx-11xx]{lang="EN-US"}[（]{style="font-family:宋体"}[x]{lang="EN-US"}[代表变量）的报文。]{style="font-family:宋体"}

[[需要注意的是，在同一用户类视图下不同的]{style="font-family:宋体"}[[if-match]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_189487473}[命令指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项数值]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*[可以相同，但是]{style="font-family:宋体"}*[rule-number]{lang="EN-US"}*[不能相同。多次配置相同匹配规则编号的命令，如果规则类型（包括匹配]{style="font-family:宋体"}[Option]{lang="EN-US"}[还是匹配硬件地址）相同，新的配置会覆盖已有配置；否则，后配置的命令不生效。同时，不同]{style="font-family:宋体"}*[rule-number]{lang="EN-US"}*[的匹配规则内容不能完全相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_792734226}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1820197681}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类]{style="font-family:宋体"}[exam]{lang="EN-US"}[的匹配规则为匹配规则编号]{style="font-family:宋体"}[1]{lang="EN-US"}[，报文中包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_188897650}

[\[Sysname\] dhcp class exam]{lang="EN-US"}

[\[Sysname-dhcp-class-exam\] if-match rule 1 option 82]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1955176575}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类]{style="font-family:宋体"}[exam]{lang="EN-US"}[的匹配规则为匹配规则编号]{style="font-family:宋体"}[2]{lang="EN-US"}[，报文中包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，并且该选项的前三个字节为]{style="font-family:宋体"}[0x13ae92]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1223962425}

[\[Sysname\] dhcp class exam]{lang="EN-US"}

[\[Sysname-dhcp-class-exam\] if-match rule 2 option 82 hex 13ae92 offset 0 length 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_188963186}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类]{style="font-family:宋体"}[exam]{lang="EN-US"}[的匹配规则为匹配规则编号]{style="font-family:宋体"}[3]{lang="EN-US"}[，报文中包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，并且该选项的第四个字节的最高位为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_358935493}

[\[Sysname\] dhcp class exam]{lang="EN-US"}

[\[Sysname-dhcp-class-exam\] if-match rule 3 option 82 hex 00000080 mask 00000080]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_13926505}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类]{style="font-family:宋体"}[exam]{lang="EN-US"}[的匹配规则编号为]{style="font-family:宋体"}[4]{lang="EN-US"}[，匹配硬件地址]{style="font-family:宋体"}[0094-0000-0101]{lang="EN-US"}[，硬件掩码长度为]{style="font-family:宋体"}[ffff-0000-0000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> syatem-view]{lang="EN-US"}]{#struct_0_x1331_x1769_13926504}

[\[Sysname\] dhcp class exam]{lang="EN-US"}

[\[Sysname-dhcp-class-exam\] if-match rule 4 hardware-address 0094-0000-0101 mask ffff-0000-0000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_923615483}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp class]{lang="EN-US"}**]{#struct_0_x1331_x1769_1567187095}
:::

::: {#1468867176 .myid}
[]{#_Toc404786437}[]{#struct_0_x1331_x1769_501572379}

**DHCP \-- DHCP服务器配置命令 \-- ip-in-use threshold**

------------------------------------------------------------------------

[**[ip-in-use threshold]{lang="EN-US"}**]{#struct_0_x1331_x1769_1282250480}[命令用来设置地址池使用率告警门限阈值。]{style="font-family:宋体"}

[**[undo ip-in-use threshold]{lang="EN-US"}**]{#struct_0_x1331_x1769_1358460844}[命令用来恢复缺省地址池使用率告警门限阈值。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1518263159}

[**[ip-in-use threshold ]{lang="EN-US"}***[threshold-value]{lang="EN-US"}*]{#struct_0_x1331_x1769_502424347}

[**[undo ip-in-use threshold]{lang="EN-US"}**]{#struct_0_x1331_x1769_57377000}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1641743585}

[[地址池使用率告警门限阈值为]{style="font-family:宋体"}[100%]{lang="EN-US"}]{#struct_0_x1331_x1769_2012270305}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x562890654}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2024070716}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1552586987}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1558341843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x90918756}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1560523094}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_x1331_x1769_502489883}[：地址池使用率告警阈值，为百分比形式，比如若设置为]{style="font-family:宋体"}[80]{lang="EN-US"}[，表示地址池使用率超过]{style="font-family:宋体"}[80%]{lang="EN-US"}[时，系统会生成告警信息发送给信息中心。取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1483618739}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_1173797411}**[ip-in-use threshold]{lang="EN-US"}**[命令设置地址池使用率告警阈值，在地址池中地址使用率超过阈值时，]{lang="EN-US" style="font-family:
宋体"}[系统会生成告警信息]{style="font-family:宋体"}[提醒管理员进行地址池规划，避免因为地址池中地址资源耗尽，后续用户不能上线。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个视图下重复执行此命令，新的配置覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x2040955986}

[[系统将告警信息发送给信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。有关信息中心参数配置请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1232475897}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1496722045}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_809198916}[配置地址池]{style="font-family:宋体"}[p1]{lang="EN-US"}[使用率告警门限阈值为]{style="font-family:宋体"}[85%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1347462672}

[\[Sysname\] dhcp server ip-pool p1]{lang="EN-US"}

[\[Sysname-dhcp-pool-p1\] ip-in-use threshold 85]{lang="EN-US"}
:::

::: {#-630272743 .myid}
[]{#_Toc404786438}[]{#struct_0_x1331_x1769_1598194656}[]{#_Toc283109641}[]{#_Toc266880228}

**DHCP \-- DHCP服务器配置命令 \-- nbns-list**

------------------------------------------------------------------------

[[[nbns-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_188766578}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[[undo nbns-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1355595327}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1576936091}

[[[nbns-list]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_10665185}

[[[undo nbns-list ]{lang="EN-US"}]{.commandkeywordsChar}[\[ *ip-address*&\<1-8\> \]]{lang="EN-US"}]{#struct_0_x1331_x1769_1755619124}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_453006601}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1172039968}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1669320389}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1586736154}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_188832114}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_382069804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_46518396}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2102609126}

[*[ip-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_641478940}[：]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x619833642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1755876021}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x823101522}[[undo nbns-list]{lang="EN-US"}]{.commandkeywordsChar}[命令时，如果没有指定任何参数，则删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池中的所有]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_189159794}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x819278687}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x886540597}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] nbns-list 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2108900564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2074536422}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[netbios-type]{lang="EN-US"}**]{#struct_0_x1331_x1769_x385803475}
:::

::: {#1842732746 .myid}
[]{#_Toc404786439}[]{#struct_0_x1331_x1769_1011929296}[]{#_Toc283109642}[]{#_Toc266880229}[]{#_Toc202081871}[]{#_Toc137350300}[]{#_Toc100214099}[]{#_Toc94500206}[]{#_Toc69790758}[]{#_Toc60058905}[]{#_Toc43546318}[]{#_Toc37217601}

**DHCP \-- DHCP服务器配置命令 \-- netbios-type**

------------------------------------------------------------------------

[[[netbios-type]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x451726268}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[NetBIOS]{lang="EN-US"}[节点类型。]{style="font-family:宋体"}

[[[undo netbios-type]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_189225330}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[NetBIOS]{lang="EN-US"}[节点类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1393034466}

[**[netbios-type]{lang="EN-US"}**[ { **b-node** \| **h-node** \| **m-node** \| **p-node** }]{lang="EN-US"}]{#struct_0_x1331_x1769_515809252}

[[undo netbios-type]{lang="EN-US"}]{#struct_0_x1331_x1769_1774070489}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_555955454}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_753418761}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[NetBIOS]{lang="EN-US"}[节点类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1281662371}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x473461261}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1865846250}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_189028722}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1880214920}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1350519326}

[[[b-node]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x581741399}[：]{style="font-family:宋体"}[b]{lang="EN-US"}[类节点，"]{style="font-family:
宋体"}[b]{lang="EN-US"}["代表广播（]{style="font-family:宋体"}[broadcast]{lang="EN-US"}[），此类节点采用广播方式获取主机名和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间的映射。源节点通过发送带有目的节点主机名的广播报文来获取目的节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，目的节点收到广播报文后，就将自己的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址返回给源节点。]{style="font-family:宋体"}

[[[h-node]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1216693842}[：]{style="font-family:宋体"}[h]{lang="EN-US"}[类节点，"]{style="font-family:
宋体"}[h]{lang="EN-US"}["代表混合（]{style="font-family:宋体"}[hybrid]{lang="EN-US"}[），是具备"端到端"通信机制的]{style="font-family:宋体"}[b]{lang="EN-US"}[类节点。此类节点首先发送单播报文与]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器通信来获取映射关系，如果没有获取到，再发送广播报文来获取映射关系。]{style="font-family:宋体"}

[[[m-node]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_173961724}[：]{style="font-family:宋体"}[m]{lang="EN-US"}[类节点，"]{style="font-family:
宋体"}[m]{lang="EN-US"}["代表混合（]{style="font-family:宋体"}[mixed]{lang="EN-US"}[），是具有部分广播特性的]{style="font-family:宋体"}[p]{lang="EN-US"}[类节点。此类节点首先发送广播报文来获取映射关系，如果没有获取到，则再发送单播报文与]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器通信来获取映射关系。]{style="font-family:宋体"}

[[[p-node]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1491028221}[：]{style="font-family:宋体"}[p]{lang="EN-US"}[类节点，"]{style="font-family:
宋体"}[p]{lang="EN-US"}["代表端到端（]{style="font-family:宋体"}[peer-to-peer]{lang="EN-US"}[），即此类节点采用发送单播报文与]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器通信的方式获取映射关系。源节点给]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器发送单播报文，]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器收到单播报文后，返回源节点请求的目的节点名所对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1952696599}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_189094258}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x81105320}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1474726936}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[NetBIOS]{lang="EN-US"}[节点类型为]{style="font-family:宋体"}[p]{lang="EN-US"}[类节点。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2005392461}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] netbios-type p-node]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_356724110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_95403938}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nbns-list]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1491419031}
:::

::: {#-815886662 .myid}
[]{#_Toc404786440}[]{#struct_0_x1331_x1769_1761763026}[]{#_Toc283109643}[]{#_Toc266880230}

**DHCP \-- DHCP服务器配置命令 \-- network**

------------------------------------------------------------------------

[[[network]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_189421938}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址网段。]{style="font-family:宋体"}

[[[undo network]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1074708620}[命令用来删除已经创建的用于动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址网段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2108822324}

[[[network]{lang="EN-US"}]{.commandkeywordsChar}[ *network-address* \[ *mask-length*[ ]{.commandkeywordsChar}\|[ mask]{.commandkeywordsChar} *mask* \] \[ **export-route** \] \[[ secondary ]{.commandkeywordsChar}\]]{lang="EN-US"}]{#struct_0_x1331_x1769_1443769645}

[[[undo network]{lang="EN-US"}]{.commandkeywordsChar}[ *network-address*[ ]{.commandkeywordsChar}\[[ ]{.commandkeywordsChar}*mask-length*[ ]{.commandkeywordsChar}\|[ mask ]{.commandkeywordsChar}*mask*[ ]{.commandkeywordsChar}\] \[[ secondary ]{.commandkeywordsChar}\]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1166779156}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1702757991}

[[没有配置动态分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x522616480}[地址网段，即没有可供分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1305876587}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_8719392}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_189487474}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_792734229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1820197688}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_109887262}

[*[network-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1904578959}[：用于动态分配的网段地址。不指定掩码长度和掩码时，表示采用自然掩码。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1331_x1769_1639443877}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的网络掩码长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[mask]{lang="EN-US"}]{.commandkeywordsChar}[ *mask*]{lang="EN-US"}]{#struct_0_x1331_x1769_x2089318096}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的网络掩码，]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为点分十进制形式。]{style="font-family:宋体"}

[**[export-route]{lang="EN-US"}**]{#struct_0_x1331_x1769_501834526}[：将网段信息下发给路由管理，由路由管理发布指定网段信息的路由。引导指定网段的下行数据流量。]{style="font-family:宋体"}

[[[secondary]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1134301713}[：指定配置的网段为从网段。如果不指定本参数，则表示配置的网段为主网段。主网段中的地址分配完之后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器可以在从网段中选择地址分配给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_794009764}

[[执行本命令时如果指定了]{style="font-family:宋体"}[[secondary]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111211954}[参数，则会进入从网段视图。用户可以在该视图下通过]{style="font-family:宋体"}[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}[命令配置为从网段的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x975273020}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x49514890}[DHCP]{lang="EN-US"}[地址池中只能配置一个主网段，如果多次执行]{style="font-family:宋体"}[[network]{lang="EN-US"}]{.commandkeywordsChar}[命令配置主网段，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_x1331_x1769_128090314}[DHCP]{lang="EN-US"}[地址池中最多可以配置]{style="font-family:宋体"}[32]{lang="EN-US"}[个从网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1472659892}[DHCP]{lang="EN-US"}[地址池中各个主、从网段的网络号和掩码不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在地址池下配置了]{lang="EN-US" style="font-family:宋体"}**[address range]{lang="EN-US"}**]{#struct_0_x1331_x1769_x418899111}[或]{lang="EN-US" style="font-family:
宋体"}**[class]{lang="EN-US"}**[命令后，不能再在该地址池下配置从网段。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改或删除]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1821180765}[[network]{lang="EN-US"}]{.commandkeywordsChar}[配置，会导致该地址池下现有的已分配地址被删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_x1331_x1769_501637918}**[network export-route]{lang="EN-US"}**[命令可以用来发布网段路由，如果多次执行此命令，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2043163587}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2111277490}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[动态分配的主地址网段为]{style="font-family:宋体"}[192.168.8.0/24]{lang="EN-US"}[，从地址网段为]{style="font-family:宋体"}[192.168.10.0/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1008702202}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] network 192.168.8.0 mask 255.255.255.0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] network 192.168.10.0 mask 255.255.255.0 secondary]{lang="EN-US"}

[\[Sysname-dhcp-pool-0-secondary\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1038911567}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_720609115}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_869433090}
:::

::: {#689269797 .myid}
[]{#_Toc404786441}[]{#struct_0_x1331_x1769_x62229866}[]{#_Toc283109644}[]{#_Toc266880231}

**DHCP \-- DHCP服务器配置命令 \-- next-server**

------------------------------------------------------------------------

[[[next-server]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1032608377}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的下一个提供服务的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[undo next-server]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1438793757}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的下一个提供服务的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111080882}

[[[next-server]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_x214042468}

[[undo next-server]{lang="EN-US"}]{#struct_0_x1331_x1769_745072769}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1126554242}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2102616269}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的下一个提供服务的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1050738915}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1353369993}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1048291990}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_2111146418}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1722737016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_357809890}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_11896748}[：下一个提供服务的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x949798369}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x220350905}[客户端分配的下一个提供服务的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，是在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端启动过程中，在获取到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，用于获取其他启动数据的服务器地址。例如，]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x172097289}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1088178330}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_700306042}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的下一个提供服务的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.254]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2111474098}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] next-server 10.1.1.254]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x646788211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_x20072889}
:::

::: {#-1888502768 .myid}
[]{#_Toc404786442}[]{#struct_0_x1331_x1769_x1860135322}[]{#_Toc283109645}[]{#_Toc266880232}

**DHCP \-- DHCP服务器配置命令 \-- option**

------------------------------------------------------------------------

[[[option]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x763475090}[命令用来自定义]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[[undo option]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x236361645}[命令用来删除自定义的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x449745509}

[[[option]{lang="EN-US"}]{.commandkeywordsChar}[ *code* {[ ascii ]{.commandkeywordsChar}*ascii-string* \|[ hex ]{.commandkeywordsChar}*hex-string* \|[ ip-address]{.commandkeywordsChar} *ip-address*&\<1-8\> }]{lang="EN-US"}]{#struct_0_x1331_x1769_x1902136416}

[[[undo option]{lang="EN-US"}]{.commandkeywordsChar}[ *code*]{lang="EN-US"}]{#struct_0_x1331_x1769_2111539634}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1424021247}

[[没有自定义]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_933592014}[选项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x902876144}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x785982696}[地址池视图]{style="font-family:宋体"}[/DHCP]{lang="EN-US"}[选项组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1603249121}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x618236506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_176208688}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_210571109}

[*[code]{lang="EN-US"}*]{#struct_0_x1331_x1769_2111343026}[：选项的数值，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[，不包括]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[54]{lang="EN-US"}[、]{style="font-family:宋体"}[56]{lang="EN-US"}[、]{style="font-family:宋体"}[58]{lang="EN-US"}[、]{style="font-family:宋体"}[59]{lang="EN-US"}[、]{style="font-family:宋体"}[61]{lang="EN-US"}[和]{style="font-family:宋体"}[82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[ascii]{lang="EN-US"}]{.commandkeywordsChar}[ *ascii-string*]{lang="EN-US"}]{#struct_0_x1331_x1769_1726978610}[：指定选项内容为配置的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[字符串。]{style="font-family:宋体"}*[ascii-string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[字符串。]{style="font-family:宋体"}

[[[hex]{lang="EN-US"}]{.commandkeywordsChar}*[ hex-string]{lang="EN-US"}*]{#struct_0_x1331_x1769_823580559}[：指定选项内容为配置的十六进制数串。]{style="font-family:宋体"}*[hex-string]{lang="EN-US"}*[为十六进制数串，位数的取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[之间的偶数。]{style="font-family:宋体"}

[[[ip-address]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_x683612002}[：指定选项内容为配置的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1467374581}

[[通过执行本命令，可以配置编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x1331_x1769_x865917357}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项内容为指定的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[字符串、十六进制数串或]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，即采用指定的内容来填充]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[应答报文中编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[的选项，以便将指定的选项内容分配给客户端。]{style="font-family:宋体"}

[[本命令为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_394875363}[服务器提供了灵活的选项配置方式，使得]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器可以为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端提供更加丰富的选项内容。在以下情况下，可以使用本命令自定义]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[随着]{style="font-family:宋体"}]{#struct_0_x1331_x1769_988399323}[DHCP]{lang="EN-US"}[的不断发展，新的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项会陆续出现。通过自定义]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项，可以方便地添加新的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些选项的内容，]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2111408562}[RFC]{lang="EN-US"}[中没有统一规定。厂商可以根据需要定义选项的内容，如]{style="font-family:宋体"}[Option 43]{lang="EN-US"}[。通过自定义]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项，可以为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端提供厂商指定的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备上只提供了有限的选项配置命令（如]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1414488578}[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}[、]{style="font-family:宋体"}**[dns-list]{lang="EN-US"}**[命令），对于没有专门命令来配置的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项，可以通过]{style="font-family:宋体"}**[option]{lang="EN-US"}**[命令配置选项内容。]{style="font-family:宋体"}[例如，可以通过]{lang="EN-US" style="font-family:
宋体"}**[option 4[ ip-address 1.1.1.1]{.commandkeywordsChar}]{lang="EN-US"}**[命令指定为]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的时间服务器地址为]{lang="EN-US" style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[扩展已有的]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1463264558}[DHCP]{lang="EN-US"}[选项。当前已提供的方式无法满足用户需求时（比如通过]{style="font-family:宋体"}**[dns-list]{lang="EN-US"}**[命令最多只能配置]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址，如果用户需要配置的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址数目大于]{style="font-family:宋体"}[8]{lang="EN-US"}[，则该命令无法满足需求），可以通过自定义]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项的方式进行扩展。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1988451020}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[有些]{style="font-family:宋体"}]{#struct_0_x1331_x1769_821134379}[DHCP]{lang="EN-US"}[选项既可以通过专门的命令来配置，也可以通过]{style="font-family:宋体"}**[option]{lang="EN-US"}**[命令来配置。例如，]{style="font-family:宋体"}[Option 6]{lang="EN-US"}[（]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址选项）既可以通过]{style="font-family:宋体"}**[dns-list]{lang="EN-US"}**[命令配置，也可以通过]{style="font-family:宋体"}**[option 6]{lang="EN-US"}**[命令配置。如果同时通过上述两种方式配置了这些选项，则在填充]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[应答报文的选项时，优先选择专门命令的配置。如果没有通过专门命令来配置，则采用]{style="font-family:宋体"}**[option]{lang="EN-US"}**[命令配置的内容填充选项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行本命令，并指定相同的选项数值]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x929709755}*[code]{lang="EN-US"}*[，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1942388632}[服务器在应答]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端报文时，如果]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组的选项编号和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池选项编号相同且匹配用户类时，以]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[选项组的选项为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2007767787}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1434744083}[日志服务器选项的编号为]{style="font-family:宋体"}[7]{lang="EN-US"}[。在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[中配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的日志服务器地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2111736242}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] option 7 ip-address 2.2.2.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1419255361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_648757197}
:::

::: {#-1983727137 .myid}
[]{#_Toc404786443}[]{#struct_0_x1331_x1769_938593724}[]{#_Toc283109646}[]{#_Toc266880233}

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server conflict**

------------------------------------------------------------------------

[[[reset dhcp server conflict]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1349716936}[命令用来清除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[的地址冲突信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1309140619}

[[[reset dhcp server conflict ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ ip]{.commandkeywordsChar} *ip-address*[ ]{.commandkeywordsChar}\] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1678331958}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1082402380}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1119052306}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111801778}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_177308424}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x2012215434}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_845150780}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_1532562968}[：清除指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的冲突信息。如果不指定本参数，则清除所有地址的冲突信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_502489886}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的地址冲突信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的地址冲突信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2061697621}

[[出现冲突地址，一般是由于网络配置不合理，动态分配的地址和网络中静态配置的地址冲突而产生的。在合理调整网络配置，不再存在冲突的情况后，原来的冲突地址可能不再冲突，可以被重新分配。此时，通过本命令，清除检测到的冲突地址，则该地址可以被重新分配。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1064176797}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1042222920}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1200137504}[清除全部地址冲突信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp server conflict]{lang="EN-US"}]{#struct_0_x1331_x1769_2111211955}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x975338556}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server conflict]{lang="EN-US"}**]{#struct_0_x1331_x1769_x406954677}
:::

::: {#-1613705196 .myid}
[]{#_Toc404786444}[]{#struct_0_x1331_x1769_x843398098}[]{#_Toc283109647}

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server expired**

------------------------------------------------------------------------

[[[reset dhcp server expired]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_816494030}[命令用来清除租约过期的地址绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_877883004}

[[[reset dhcp server expired ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ ]{.commandkeywordsChar}\[[ ip ]{.commandkeywordsChar}*ip-address* \] \[ **vpn-instance** *vpn-instance-name* \] \|[ pool]{.commandkeywordsChar} *pool-name*[ ]{.commandkeywordsChar}\]]{lang="EN-US"}]{#struct_0_x1331_x1769_665341851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x401298562}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2111277491}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1008767738}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_351491042}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1558182809}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1442528187}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_1562568723}[：清除指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的租约过期地址绑定信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_501900061}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的租约过期的地址绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的租约过期的地址绑定信息。]{style="font-family:宋体"}

[[[pool]{lang="EN-US"}]{.commandkeywordsChar}[ *pool-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x6640046}[：清除指定地址池中租约过期的地址绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1435636975}

[[执行本命令时，如果不指定任何参数，则清除所有租约过期的地址绑定信息。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_767896476}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111080883}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x213976932}[清除所有租约过期的地址绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp server expired]{lang="EN-US"}]{#struct_0_x1331_x1769_x1043874761}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_420172165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server expired]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1851423766}
:::

::: {#1523387353 .myid}
[]{#_Toc404786445}[]{#struct_0_x1331_x1769_290297890}[]{#_Toc283109648}[]{#_Toc266880234}[]{#_Toc202081875}[]{#_Toc137350304}[]{#_Toc100214103}[]{#_Toc94500210}[]{#_Toc69790762}[]{#_Toc60058909}[]{#_Toc43546322}[]{#_Toc37217605}

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server ip-in-use**

------------------------------------------------------------------------

[[[reset dhcp server ip-in-use]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1170193144}[命令用来清除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[的正式绑定和临时绑定信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_450931079}

[[[reset dhcp server ip-in-use ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ ]{.commandkeywordsChar}\[[ ip]{.commandkeywordsChar} *ip-address*[ ]{.commandkeywordsChar}\][ ]{.commandkeywordsChar}\[ [vpn-instance]{.commandkeywordsChar} vpn-instance-name \][ ]{.commandkeywordsChar}\|[ pool ]{.commandkeywordsChar}*pool-name*[ ]{.commandkeywordsChar}\]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1581576496}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111146419}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1722802552}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1538923538}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1394051215}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_387048465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1606025080}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_593521384}[：清除指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的正式绑定和临时绑定信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_501768989}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的正式绑定和临时绑定信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的正式绑定和临时绑定信息。]{style="font-family:宋体"}

[[[pool]{lang="EN-US"}]{.commandkeywordsChar}[ *pool-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1013024528}[：清除指定地址池的正式绑定和临时绑定信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111474099}

[[执行本命令时，如果不指定任何参数，则清除所有的正式绑定和临时绑定信息。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x646853747}

[[需要注意的是，清除静态正式绑定信息时，将使该绑定信息变为静态无效绑定。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_28613938}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1367253372}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1015263712}[清除地址]{style="font-family:宋体"}[10.110.1.1]{lang="EN-US"}[的正式绑定和临时绑定信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp server ip-in-use ip 10.110.1.1]{lang="EN-US"}]{#struct_0_x1331_x1769_1276880789}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x254004217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server [ip-in-use]{.commandkeywordsChar}]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2120933576}
:::

::: {#-1454903756 .myid}
[]{#_Toc404786446}[]{#struct_0_x1331_x1769_x265707958}[]{#_Toc283109649}[]{#_Toc266880235}[]{#_Toc202081876}[]{#_Toc137350305}[]{#_Toc100214104}[]{#_Toc94500211}[]{#_Toc69790763}[]{#_Toc60058910}[]{#_Toc43546323}

**DHCP \-- DHCP服务器配置命令 \-- reset dhcp server statistics**

------------------------------------------------------------------------

[[[reset dhcp server statistics]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111539635}[命令用来清除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1424086783}

[[[reset dhcp server statistics ]{lang="EN-US"}]{.commandkeywordsChar}[\[ [vpn-instance]{.commandkeywordsChar} vpn-instance-name \]]{lang="EN-US"}]{#struct_0_x1331_x1769_258878103}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1328406383}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1014843950}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1796954545}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1196569793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1462375736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_501834525}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_1362514458}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示清除的是公网中的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1308138233}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2111343027}[清除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp server statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_1727044146}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x255958665}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server statistics]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1431922752}
:::

::: {#1012678815 .myid}
[]{#_Toc404786447}[]{#struct_0_x1331_x1769_x2121481653}[]{#_Toc283109650}[]{#_Toc266880236}[]{#_Toc202081878}[]{#_Toc137350307}[]{#_Toc100214105}[]{#_Toc94500212}[]{#_Toc69790764}[]{#_Toc60058911}[]{#_Toc43546324}[]{#_Toc37217607}

**DHCP \-- DHCP服务器配置命令 \-- static-bind**

------------------------------------------------------------------------

[[[static-bind]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_307851746}[命令用来在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池中配置静态地址绑定，以便实现]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[或硬件地址为指定值的客户端分配固定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[undo static-bind]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1306817519}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池中的静态地址绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1695448910}

[[[static-bind ip-address]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address* \[[ ]{.commandkeywordsChar}*mask-length*[ ]{.commandkeywordsChar}\|[ mask ]{.commandkeywordsChar}*mask*[ ]{.commandkeywordsChar}\] {[ client-identifier ]{.commandkeywordsChar}*client-identifier*[ ]{.commandkeywordsChar}\| [hardware-address ]{.commandkeywordsChar}*hardware-address*[ ]{.commandkeywordsChar}\[[ ethernet ]{.commandkeywordsChar}\|[ token-ring ]{.commandkeywordsChar}\] }]{lang="EN-US"}]{#struct_0_x1331_x1769_2111408563}

[**[undo static-bind ip-address]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1414423042}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1539556051}

[[没有在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1005792060}[地址池中配置静态地址绑定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x408012199}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1743849279}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1998412871}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1073377008}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1708358705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111736243}

[[[ip-address]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1419320897}[：指定静态绑定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。不指定掩码长度和掩码时，表示采用自然掩码。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1331_x1769_920222777}[：静态绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码长度，即掩码中连续"]{style="font-family:宋体"}[1]{lang="EN-US"}["的个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[mask ]{lang="EN-US"}]{.commandkeywordsChar}*[mask]{lang="EN-US"}*]{#struct_0_x1331_x1769_1133813638}[：指定静态绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码，]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为点分十进制形式。]{style="font-family:宋体"}

[[[client-identifier]{lang="EN-US"}]{.commandkeywordsChar}*[ client-identifier]{lang="EN-US"}*]{#struct_0_x1331_x1769_127568047}[：指定静态绑定的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[client-identifier]{lang="EN-US"}*[表示客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[个字符的字符串，字符串中只能包括十六进制数和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，且形式为]{style="font-family:宋体"}[H-H-H...]{lang="EN-US"}[，除最后一个]{style="font-family:宋体"}[H]{lang="EN-US"}[表示]{style="font-family:宋体"}[2]{lang="EN-US"}[位或]{style="font-family:宋体"}[4]{lang="EN-US"}[位十六进制数外，其他均表示]{style="font-family:宋体"}[4]{lang="EN-US"}[位十六进制数。例如：]{style="font-family:宋体"}[aabb-cccc-dd]{lang="EN-US"}[为有效的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[aabb-c-dddd]{lang="EN-US"}[和]{style="font-family:宋体"}[aabb-cc-dddd]{lang="EN-US"}[为无效客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[[hardware-address]{lang="EN-US"}]{.commandkeywordsChar}*[ hardware-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_1832596670}[：指定静态绑定的客户端硬件地址。]{style="font-family:宋体"}*[hardware-address]{lang="EN-US"}*[表示客户端硬件地址，为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[39]{lang="EN-US"}[个字符的字符串，字符串中只能包括十六进制数和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，且形式为]{style="font-family:宋体"}[H-H-H...]{lang="EN-US"}[，除最后一个]{style="font-family:宋体"}[H]{lang="EN-US"}[表示]{style="font-family:宋体"}[2]{lang="EN-US"}[位或]{style="font-family:宋体"}[4]{lang="EN-US"}[位十六进制数外，其他均表示]{style="font-family:宋体"}[4]{lang="EN-US"}[位十六进制数。例如：]{style="font-family:宋体"}[aabb-cccc-dd]{lang="EN-US"}[为有效的客户端硬件地址，]{style="font-family:宋体"}[aabb-c-dddd]{lang="EN-US"}[和]{style="font-family:宋体"}[aabb-cc-dddd]{lang="EN-US"}[为无效的客户端硬件地址。]{style="font-family:宋体"}

[[[ethernet]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x282055875}[：指定客户端硬件地址类型为以太网，缺省为以太网类型。]{style="font-family:宋体"}

[[[token-ring]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1353091850}[：指定客户端硬件地址类型为令牌环网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_908308601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态绑定的]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2111801779}[IP]{lang="EN-US"}[地址不能是]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，否则会导致]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址冲突，被绑定的客户端将无法正常获取到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一地址池下可以配置多个静态地址绑定。所有地址池下配置的静态地址绑定一共不能超过]{style="font-family:宋体"}]{#struct_0_x1331_x1769_177373960}[8192]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一地址只能绑定给一个客户端。不允许通过重复执行本命令的方式修改]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1907890994}[IP]{lang="EN-US"}[地址与客户端的绑定关系。只有删除了某个地址的绑定关系，才能将该地址与其他客户端绑定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_537862889}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2126086120}[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[中配置：为客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[00aa-aabb]{lang="EN-US"}[的客户端，固定分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[10.1.1.1/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_924335659}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] static-bind ip-address 10.1.1.1 mask 255.255.255.0 client-identifier 00aa-aabb]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x978082200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1898583343}
:::

::: {#1923036125 .myid}
[]{#_Toc404786448}[]{#struct_0_x1331_x1769_2111211952}[]{#_Toc283109651}[]{#_Toc266880237}[]{#_Toc202081880}[]{#_Toc137350309}

**DHCP \-- DHCP服务器配置命令 \-- tftp-server domain-name**

------------------------------------------------------------------------

[[[tftp-server domain-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x975404092}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器域名。]{style="font-family:宋体"}

[[[undo tftp-server domain-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x452733710}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器域名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1765567268}

[[[tftp-server domain-name]{lang="EN-US"}]{.commandkeywordsChar}*[ domain-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_x474294620}

[[undo tftp-server domain-name]{lang="EN-US"}]{#struct_0_x1331_x1769_x1444752313}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x539470284}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1739398502}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器域名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111277488}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1008177915}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x827054890}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_456470015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_983383858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_806672507}

[*[domain-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_162968658}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_937839215}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_144325733}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111080880}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x213911396}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器域名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_510746224}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] tftp-server domain-name aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x720491976}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_2083485177}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[tftp-server ip-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1464185467}
:::

::: {#-671890013 .myid}
[]{#_Toc404786449}[]{#struct_0_x1331_x1769_357800630}[]{#_Toc283109652}[]{#_Toc266880238}[]{#_Toc202081881}[]{#_Toc137350310}

**DHCP \-- DHCP服务器配置命令 \-- tftp-server ip-address**

------------------------------------------------------------------------

[[[tftp-server ip-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1964304422}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}[[undo tftp-server ip-address]{lang="EN-US"}]{.commandkeywordsChar}[命令用来删除]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111146416}

[[[tftp-server ip-address]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_1721819512}

[[undo tftp-server ip-address]{lang="EN-US"}]{#struct_0_x1331_x1769_x706458549}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1229023683}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1183396409}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_460087499}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2121736223}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x342861913}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1947367828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_2111474096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x647705715}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_1261286302}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_763760560}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x274353305}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_683701945}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x573036592}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2111539632}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] tftp-server ip-address 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1424414463}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1081444829}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[tftp-server domain-name]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x206723967}
:::

::: {#-954996227 .myid}
[]{#_Toc404786450}[]{#struct_0_x1331_x1769_x752910232}

**DHCP \-- DHCP服务器配置命令 \-- valid class**

------------------------------------------------------------------------

[**[valid class]{lang="EN-US"}**]{#struct_0_x1331_x1769_x752910229}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[白名单包括的用户类名。]{style="font-family:宋体"}

[**[undo valid class]{lang="EN-US"}**]{#struct_0_x1331_x1769_200078063}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[白名单中包括的用户类名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1712908469}

[**[valid class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_1042653805}

[**[undo valid class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_x815935751}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_980693200}

[[未配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x408462939}[白名单包括的用户类。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1015543763}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1736651518}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x752910230}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_199619310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1427965251}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1203509159}

[*[class-name]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_1109474487}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[白名单包括的用户类名列表。其中]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[代表最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个用户类名，每个用户类名之间用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1314982438}

[[在配置了]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2008918856}[地址池用户白名单功能后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器才会检查用户是否属于白名单包括的用户类。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_218390018}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_508979616}[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[中配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[白名单包括的用户类名为]{style="font-family:宋体"}[test1]{lang="EN-US"}[和]{style="font-family:宋体"}[test2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1294905271}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] valid class test1 test2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_209139888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp class]{lang="EN-US"}**]{#struct_0_x1331_x1769_1585741923}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[verify class]{lang="EN-US"}**]{#struct_0_x1331_x1769_1702554537}
:::

::: {#-380918311 .myid}
[]{#_Toc404786451}[]{#struct_0_x1331_x1769_x1324419661}

**DHCP \-- DHCP服务器配置命令 \-- verify class**

------------------------------------------------------------------------

[**[verify class]{lang="EN-US"}**]{#struct_0_x1331_x1769_410411028}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类白名单功能。]{style="font-family:宋体"}

[**[undo verify class]{lang="EN-US"}**]{#struct_0_x1331_x1769_x607318386}[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类白名单功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1753508368}

[**[verify class]{lang="EN-US"}**]{#struct_0_x1331_x1769_1544397493}

[**[undo verify class]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1086128920}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2121240294}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1585741922}[用户类白名单功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1702489001}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2108146472}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1158816156}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1707310959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x411294705}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_842638439}

[[在开启了]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_65043301}[用户类白名单功能后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器才会检查用户是否属于白名单包括的用户类。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1911362373}[用户类白名单功能对获取静态绑定租约的客户端不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1295049711}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x809494362}[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[中开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户类白名单功能。]{style="font-family:宋体"}

[[\[Sysname\] syatem-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1585741925}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] verify class]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1702947753}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[valid class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_628916374}
:::

::: {#-294853326 .myid}
[]{#_Toc404786452}[]{#struct_0_x1331_x1769_x1800045336}[]{#_Toc283109653}[]{#_Toc266880239}[]{#_Toc202081882}[]{#_Toc137350311}

**DHCP \-- DHCP服务器配置命令 \-- voice-config**

------------------------------------------------------------------------

[[[voice-config]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x110795642}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[Option 184]{lang="EN-US"}[内容。]{style="font-family:宋体"}

[[[undo voice-config]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1025101683}[命令用来删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[Option 184]{lang="EN-US"}[内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1841032431}

[[[voice-config ]{lang="EN-US"}]{.commandkeywordsChar}[{[ as-ip]{.commandkeywordsChar} *ip-address*[ ]{.commandkeywordsChar}\|[ fail-over ]{.commandkeywordsChar}*ip-address* *dialer-string*[ ]{.commandkeywordsChar}\|[ ncp-ip]{.commandkeywordsChar} *ip-address*[ ]{.commandkeywordsChar}\|[ voice-vlan ]{.commandkeywordsChar}*vlan-id*[ ]{.commandkeywordsChar}{[ disable ]{.commandkeywordsChar}\|[ enable ]{.commandkeywordsChar}} }]{lang="EN-US"}]{#struct_0_x1331_x1769_x1229692268}

[**[undo voice-config]{lang="EN-US"}**[ \[ **as-ip** \| **fail-over** \| **ncp-ip** \| **voice-vlan** \]]{lang="EN-US"}]{#struct_0_x1331_x1769_2111343024}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1727109682}

[[没有配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2059816235}[地址池为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[Option 184]{lang="EN-US"}[内容。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x728998935}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x123951467}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x802392494}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1686304812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_106553801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x434393518}

[[[as-ip ]{lang="EN-US"}]{.commandkeywordsChar}*[ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_2111408560}[：指定备用服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[fail-over]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address dialer-string]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1414357506}[：指定自动故障转移]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址及呼叫字符串。]{style="font-family:宋体"}*[dialer-string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[39]{lang="EN-US"}[个字符的字符串，字符可以是数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[及"]{style="font-family:
宋体"}[\*]{lang="EN-US"}["。]{style="font-family:宋体"}

[[[ncp-ip ]{lang="EN-US"}]{.commandkeywordsChar}*[ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1547563217}[：指定网络呼叫处理器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[voice-vlan ]{lang="EN-US"}]{.commandkeywordsChar}*[vlan-id]{lang="EN-US"}*]{#struct_0_x1331_x1769_1271996482}[：指定语音]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[disable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1037897846}[：指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[处于禁止状态，即]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端不会将所指定的]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[作为语音]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x2091691601}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[处于开启状态，即]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端会将所指定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[作为语音]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1066368712}

[[如果多次执行本命令，为同一个参数配置不同的值，则新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_742853789}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111736240}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1419124289}[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[指定]{style="font-family:宋体"}[Option 184]{lang="EN-US"}[的内容：网络呼叫处理器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，备用服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.2.2.2]{lang="EN-US"}[，语音]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[，为开启状态，自动故障转移]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:
宋体"}[10.3.3.3]{lang="EN-US"}[，呼叫字符串为]{style="font-family:宋体"}[99\*]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1001184425}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] voice-config ncp-ip 10.1.1.1]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] voice-config as-ip 10.2.2.2]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] voice-config voice-vlan 3 enable]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] voice-config fail-over 10.3.3.3 99\*]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1782380085}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp server pool]{lang="EN-US"}**]{#struct_0_x1331_x1769_1655666572}
:::

::: {#1715388964 .myid}
[]{#_Toc404786453}[]{#struct_0_x1331_x1769_2067983999}

**DHCP \-- DHCP服务器配置命令 \-- vpn-instance**

------------------------------------------------------------------------

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1034509366}[命令用来指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器上的地址池所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x1331_x1769_x4672162}[命令用来删除指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器上的地址池所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2068049535}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x348317935}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1254372887}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1279455116}

[[未指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_940394467}[服务器上的地址池所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1360652982}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1701506655}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1288997642}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x142183884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1032414168}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1806405245}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_2067852927}[：指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示地址池属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_538193787}

[[当地址池绑定了]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1331_x1769_497992499}[实例后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器可以将网络划分成公网和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[私网。没有配置]{style="font-family:宋体"}[VPN]{lang="EN-US"}[属性的地址池被划分到公网，配置了]{style="font-family:宋体"}[VPN]{lang="EN-US"}[属性的地址池被划分到相应的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[私网，这样，对于处于公网或]{style="font-family:宋体"}[VPN]{lang="EN-US"}[私网中的客户端，服务器都能够选择合适的地址池来为客户端分配租约并且记录该客户端的状态信息。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x388566754}[客户端的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息可以从认证模块（如]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[）获取，也可以从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器接收报文的接口配置的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息获取。如果以上两种方式都可获取]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息，以从认证模块获取的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[信息为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1121725958}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_580507059}[指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[编号为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x312077587}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] vpn-instance abc]{lang="EN-US"}
:::

::: {#-1756003610 .myid}
[]{#_Toc137350316}[]{#_Toc202081886}[]{#_Toc404786455}[]{#struct_0_x1331_x1769_x1667425338}[]{#_Toc269455552}[]{#_Toc266880242}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay check mac-address**

------------------------------------------------------------------------

[[[dhcp relay check mac-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111801776}[命令用来启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。]{style="font-family:宋体"}

[[[undo dhcp relay check mac-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_177963784}[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x556762169}

[[dhcp relay check mac-address]{lang="EN-US"}]{#struct_0_x1331_x1769_1690306935}

[[undo dhcp relay check mac-address]{lang="EN-US"}]{#struct_0_x1331_x1769_561332738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1391159526}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1853177625}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_196408499}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1710807505}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111211953}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x975469628}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x425137906}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2102358982}

[[启用该功能后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_134205034}[中继检查接收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求报文中的]{style="font-family:宋体"}[chaddr]{lang="EN-US"}[字段和数据帧的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址字段是否一致。如果一致，则认为该报文合法，将其转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器；如果不一致，则丢弃该报文。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1529496538}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在接口上配置]{lang="EN-US" style="font-family:宋体"}**[dhcp select relay]{lang="EN-US"}**]{#struct_0_x1331_x1769_869157416}[后，]{lang="EN-US" style="font-family:
宋体"}[DHCP]{lang="EN-US"}[中继的]{lang="EN-US" style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址检查功能才会生效。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x627489702}[DHCP]{lang="EN-US"}[中继转发]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文时会修改报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，所以只能在靠近]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的第一跳]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继设备上启用]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。在非第一跳]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继设备上启用]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能，会使]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继设备错误的丢弃报文，导致客户端地址申请不成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111277489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x1008243451}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_758467172}[启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1083322014}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay check mac-address]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_1494900904}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_76896134}[启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_285274702}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay check mac-address]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x970725322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp select relay]{lang="EN-US"}**]{#struct_0_x1331_x1769_2111080881}
:::

::: {#1183160659 .myid}
[]{#_Toc404786456}[]{#struct_0_x1331_x1769_x213845860}[]{#_Toc344456830}[]{#_Toc343608025}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay check mac-address aging-time**

------------------------------------------------------------------------

[**[dhcp relay check mac-address aging-time]{lang="EN-US"}**]{#struct_0_x1331_x1769_x273731344}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查表项的老化时间。]{style="font-family:宋体"}

[**[undo dhcp relay check mac-address aging-time]{lang="EN-US"}**]{#struct_0_x1331_x1769_x332296701}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1163327675}

[**[dhcp relay check mac-address aging-time]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1331_x1769_1758364715}

[**[undo dhcp relay check mac-address aging-time]{lang="EN-US"}**]{#struct_0_x1331_x1769_x196128058}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x741113657}

[[MAC]{lang="EN-US"}]{#struct_0_x1331_x1769_2111146417}[地址检查表项的老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1721885048}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x261696246}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1194599124}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1683764062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_675826038}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1397487791}

[[如果未通过]{style="font-family:宋体"}**[dhcp relay check mac-address]{lang="EN-US"}**]{#struct_0_x1331_x1769_50996377}[命令启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能，则本命令的配置不会生效。]{style="font-family:宋体"}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_808566029}

[*[time]{lang="EN-US"}*]{#struct_0_x1331_x1769_2111474097}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查表项的老化时间，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x647771251}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1888385522}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查表项的老化时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x317339880}

[\[Sysname\] dhcp relay check mac-address aging-time 60]{lang="EN-US"}
:::

::: {#1051510496 .myid}
[]{#_Toc404786457}[]{#struct_0_x1331_x1769_1139344001}[]{#_Toc269455730}[]{#_Toc266880243}[]{#_Toc266880244}[]{#_Toc266880245}[]{#_Toc266880246}[]{#_Toc266880247}[]{#_Toc266880248}[]{#_Toc266880249}[]{#_Toc266880250}[]{#_Toc266880251}[]{#_Toc266880252}[]{#_Toc266880253}[]{#_Toc266880254}[]{#_Toc266880255}[]{#_Toc266880258}[]{#_Toc266880259}[]{#_Toc266880260}[]{#_Toc266880261}[]{#_Toc266880262}[]{#_Toc266880263}[]{#_Toc266880264}[]{#_Toc266880265}[]{#_Toc266880266}[]{#_Toc266880267}[]{#_Toc266880269}[]{#_Toc266880270}[]{#_Toc266880271}[]{#_Toc266880272}[]{#_Toc266880273}[]{#_Toc266880274}[]{#_Toc269455553}[]{#_Toc269455554}[]{#_Toc269455555}[]{#_Toc269455556}[]{#_Toc269455557}[]{#_Toc269455558}[]{#_Toc269455559}[]{#_Toc269455560}[]{#_Toc269455561}[]{#_Toc269455562}[]{#_Toc269455563}[]{#_Toc269455564}[]{#_Toc269455565}[]{#_Toc269455566}[]{#_Toc269455568}[]{#_Toc269455569}[]{#_Toc269455571}[]{#_Toc269455572}[]{#_Toc269455573}[]{#_Toc269455575}[]{#_Toc269455576}[]{#_Toc269455577}[]{#_Toc269455578}[]{#_Toc269455579}[]{#_Toc269455580}[]{#_Toc269455581}[]{#_Toc269455582}[]{#_Toc269455583}[]{#_Toc269455586}[]{#_Toc269455587}[]{#_Toc269455588}[]{#_Toc269455591}[]{#_Toc269455592}[]{#_Toc269455593}[]{#_Toc269455594}[]{#_Toc269455595}[]{#_Toc269455596}[]{#_Toc269455597}[]{#_Toc269455598}[]{#_Toc269455599}[]{#_Toc269455600}[]{#_Toc269455601}[]{#_Toc269455602}[]{#_Toc269455603}[]{#_Toc269455604}[]{#_Toc269455606}[]{#_Toc269455607}[]{#_Toc269455608}[]{#_Toc269455609}[]{#_Toc269455610}[]{#_Toc269455611}[]{#_Toc269455612}[]{#_Toc269455613}[]{#_Toc269455614}[]{#_Toc269455615}[]{#_Toc269455616}[]{#_Toc269455617}[]{#_Toc269455618}[]{#_Toc269455619}[]{#_Toc269455620}[]{#_Toc269455621}[]{#_Toc269455624}[]{#_Toc269455625}[]{#_Toc269455626}[]{#_Toc269455629}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay client-information record**

------------------------------------------------------------------------

[[[dhcp relay client-information record]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111539633}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继用户地址表项记录功能。]{style="font-family:宋体"}

[[[undo dhcp relay client-information record]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1424479999}[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继用户地址表项记录功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1687213138}

[[dhcp relay client-information record]{lang="EN-US"}]{#struct_0_x1331_x1769_x1901133033}

[[undo dhcp relay client-information record]{lang="EN-US"}]{#struct_0_x1331_x1769_469338321}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x358160966}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_820244992}[中继用户地址表项记录功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x832743808}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2111343025}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1727175218}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_124769774}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_366017673}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1423571255}

[[关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2073011032}[中继用户地址表项记录功能时，会删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继上记录的全部地址表项。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_642668626}[中继作为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的网关设备时，才会记录此]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的地址表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1110823943}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x469371876}[开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继用户地址表项记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2111408561}

[\[Sysname\] dhcp relay client-information record]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1414291970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay client-information refresh]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1439525063}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay client-information refresh enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1216524643}
:::

::: {#1478702426 .myid}
[]{#_Toc404786458}[]{#struct_0_x1331_x1769_1961505310}[]{#_Toc269455732}[]{#_Toc266880284}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay client-information refresh**

------------------------------------------------------------------------

[[[dhcp relay client-information refresh]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1519543759}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继动态用户地址表项的定时刷新周期。]{style="font-family:宋体"}

[[[undo dhcp relay client-information refresh]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1849474689}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1142132498}

[[[dhcp relay client-information refresh ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ auto ]{.commandkeywordsChar}\|[ interval ]{.commandkeywordsChar}*interval*[ ]{.commandkeywordsChar}\]]{lang="EN-US"}]{#struct_0_x1331_x1769_2111736241}

[[undo dhcp relay client-information refresh]{lang="EN-US"}]{#struct_0_x1331_x1769_x1419189825}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2086136779}

[[定时刷新周期为]{style="font-family:宋体"}[[auto]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1270994702}[，即根据表项的数目自动计算刷新时间间隔。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1028389300}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x328278288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_192456070}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1581698243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x660732947}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111801777}

[[[auto]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_178029320}[：指定根据表项的数目自动计算刷新时间间隔。表项越多，刷新时间间隔越短，但最短时间间隔不会小于]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1728445672}[：刷新时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1262840044}

[[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_583544554}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x47792744}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1200769511}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继动态用户地址表项的刷新时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x328450819}

[\[Sysname\] dhcp relay client-information refresh interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1752170839}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay client-information record]{lang="EN-US"}**]{#struct_0_x1331_x1769_2111211950}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay client-information refresh enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_x975535164}
:::

::: {#-397851732 .myid}
[]{#_Toc404786459}[]{#struct_0_x1331_x1769_x1218551757}[]{#_Toc269455731}[]{#_Toc266880283}[]{#_Toc269455633}[]{#_Toc269455636}[]{#_Toc269455637}[]{#_Toc269455638}[]{#_Toc269455639}[]{#_Toc269455640}[]{#_Toc269455641}[]{#_Toc269455642}[]{#_Toc269455643}[]{#_Toc269455644}[]{#_Toc269455645}[]{#_Toc269455646}[]{#_Toc269455647}[]{#_Toc269455648}[]{#_Toc269455649}[]{#_Toc269455651}[]{#_Toc269455654}[]{#_Toc269455655}[]{#_Toc269455656}[]{#_Toc269455657}[]{#_Toc269455658}[]{#_Toc269455659}[]{#_Toc269455660}[]{#_Toc269455661}[]{#_Toc269455663}[]{#_Toc269455664}[]{#_Toc269455665}[]{#_Toc269455666}[]{#_Toc269455667}[]{#_Toc269455668}[]{#_Toc269455669}[]{#_Toc269455670}[]{#_Toc269455671}[]{#_Toc269455672}[]{#_Toc269455673}[]{#_Toc269455674}[]{#_Toc269455675}[]{#_Toc269455676}[]{#_Toc269455678}[]{#_Toc269455681}[]{#_Toc269455682}[]{#_Toc269455683}[]{#_Toc269455684}[]{#_Toc269455685}[]{#_Toc269455687}[]{#_Toc269455688}[]{#_Toc269455689}[]{#_Toc269455690}[]{#_Toc269455691}[]{#_Toc269455692}[]{#_Toc269455693}[]{#_Toc269455694}[]{#_Toc269455695}[]{#_Toc269455696}[]{#_Toc269455697}[]{#_Toc269455698}[]{#_Toc269455699}[]{#_Toc269455700}[]{#_Toc269455701}[]{#_Toc269455703}[]{#_Toc269455704}[]{#_Toc269455706}[]{#_Toc269455707}[]{#_Toc269455708}[]{#_Toc269455710}[]{#_Toc269455711}[]{#_Toc269455712}[]{#_Toc269455713}[]{#_Toc269455714}[]{#_Toc269455715}[]{#_Toc269455716}[]{#_Toc269455717}[]{#_Toc269455718}[]{#_Toc269455721}[]{#_Toc269455722}[]{#_Toc269455723}[]{#_Toc269455726}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay client-information refresh enable**

------------------------------------------------------------------------

[[[dhcp relay client-information refresh enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x342341634}[命令用来开启]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继动态用户地址表项定时刷新功能。]{style="font-family:宋体"}

[[[undo dhcp relay client-information refresh enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1160086923}[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继动态用户地址表项定时刷新功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1616834704}

[[dhcp relay client-information refresh enable]{lang="EN-US"}]{#struct_0_x1331_x1769_x1839909059}

[[undo dhcp relay client-information refresh enable]{lang="EN-US"}]{#struct_0_x1331_x1769_729416749}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111277486}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1009095419}[中继动态用户地址表项定时刷新功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x322183862}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1432641184}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_77176902}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1542190236}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x976927817}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_234965484}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x70097617}[客户端释放动态获取的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，会向]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器单播发送]{style="font-family:宋体"}[DHCP-RELEASE]{lang="EN-US"}[报文，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继不会处理该报文的内容。如果此时]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继上记录了该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的绑定关系，则会造成]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的用户地址表项无法实时刷新。为了解决这个问题，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继支持动态用户地址表项的定时刷新功能。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2111080878}[中继动态用户地址表项定时刷新功能开启时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继每隔指定时间采用客户端获取到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址向]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送]{style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[报文：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x213387093}[DHCP]{lang="EN-US"}[中继接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器响应的]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[报文或在指定时间内没有接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的响应报文，则表明这个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址已经可以进行分配，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继会删除动态用户地址表中对应的表项，为了避免地址浪费，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继收到]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[报文后，会发送]{style="font-family:宋体"}[DHCP-RELEASE]{lang="EN-US"}[报文释放申请到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1331_x1769_84231904}[DHCP]{lang="EN-US"}[中继接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器响应的]{style="font-family:宋体"}[DHCP-NAK]{lang="EN-US"}[报文，则表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的绑定信息仍然存在，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继不会删除该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对应的表项。]{style="font-family:宋体"}

[[需要注意的是，关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_577119467}[中继动态用户地址表项定时刷新功能时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继上记录的用户地址表项不会自动老化。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端释放申请到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，需要用户执行]{style="font-family:宋体"}[[reset dhcp relay client-information]{lang="EN-US"}]{.commandkeywordsChar}[命令删除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继上对应的用户地址表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2012804684}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1325151728}[关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继动态用户地址表项定时刷新功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1303094919}

[\[Sysname\] undo dhcp relay client-information refresh enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1714488650}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay client-information record]{lang="EN-US"}**]{#struct_0_x1331_x1769_2111146414}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay client-information refresh]{lang="EN-US"}**]{#struct_0_x1331_x1769_1721950584}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol;font-weight:normal"}]{.commandkeywordsChar}[[reset dhcp relay client-information]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_496710336}
:::

::: {#9146030 .myid}
[]{#_Toc404786460}[]{#struct_0_x1331_x1769_2068573823}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay gateway**

------------------------------------------------------------------------

[[[dhcp relay gateway]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2067983998}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址。]{style="font-family:宋体"}

[[[undo dhcp relay gateway]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1034443830}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x203440505}

[[[dhcp relay gateway ]{lang="EN-US"}]{.commandkeywordsChar}[ip-address]{lang="EN-US"}]{#struct_0_x1331_x1769_x1219366558}

[[[undo dhcp relay gateway]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x100842867}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_838600878}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1290923051}[中继分配接口下主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的网关地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x717424198}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1691002129}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_167538552}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1194814728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1624806704}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2068049534}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x348252399}[：指定为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_734013293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口视图下配置此命令后，中继会使用此命令配置的地址作为客户端的网关地址。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1825750786}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行此命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1297386468}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的网关地址必须属于该命令行所在的接口。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1072253032}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1397315103}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_2139715324}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x270089866}[在接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[上配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2067852926}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay gateway 10.1.1.1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_538128251}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1846313607}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的网关地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x841304141}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] dhcp relay gateway 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x199999867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gateway-list]{lang="EN-US"}**]{#struct_0_x1331_x1769_x585691887}
:::

::: {#1834053469 .myid}
[]{#_Toc404786461}[]{#struct_0_x1331_x1769_1654430775}[]{#_Toc269455630}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information circuit-id**

------------------------------------------------------------------------

[[[dhcp relay information circuit-id]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1270143861}[命令用来配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充模式和填充格式。]{style="font-family:宋体"}

[[[undo dhcp relay information circuit-id]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1858237863}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1699738904}

[[[dhcp relay information circuit-id ]{lang="EN-US"}]{.commandkeywordsChar}[{[ bas ]{.commandkeywordsChar}\|[ string]{.commandkeywordsChar} *circuit-id*[ ]{.commandkeywordsChar}\|[ ]{.commandkeywordsChar}{[ normal ]{.commandkeywordsChar}\|[ verbose ]{.commandkeywordsChar}\[[ node-identifier ]{.commandkeywordsChar}{[ mac ]{.commandkeywordsChar}\|[ sysname ]{.commandkeywordsChar}\|[ user-defined]{.commandkeywordsChar} *node-identifier*[ ]{.commandkeywordsChar}}[ ]{.commandkeywordsChar}\] \[ **interface** \] }[ ]{.commandkeywordsChar}\[[ format ]{.commandkeywordsChar}{[ ascii ]{.commandkeywordsChar}\|[ hex ]{.commandkeywordsChar}} \] }]{lang="EN-US"}]{#struct_0_x1331_x1769_x387992717}

[[[undo dhcp relay information circuit-id]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1426891750}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111474094}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x647574643}[的]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充模式为]{style="font-family:宋体"}[Normal]{lang="EN-US"}[，填充格式为]{style="font-family:宋体"}[hex]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_882523846}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2109141633}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x526939232}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1349379280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x620051178}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x477334259}

[**[bas]{lang="EN-US"}**]{#struct_0_x1331_x1769_2067918462}[：表示支持使用电信格式的填充]{style="font-family:宋体"}[Circuit]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[[string]{lang="EN-US"}]{.commandkeywordsChar}[ *circuit-id*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1144073073}[：指定以用户配置的字符串填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}*[circuit-id]{lang="EN-US"}*[表示用户配置的用来填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的内容，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[[normal]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111539630}[：指定以]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项，填充内容为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[和端口号。]{style="font-family:宋体"}

[[[verbose]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1424283391}[：指定以]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。填充的内容为节点标识、接口信息和接口所在的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号。节点标识默认以节点的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址构成；接口信息默认由以太网类型（取值固定为"]{style="font-family:宋体"}[eth]{lang="EN-US"}["）、框号、槽号、子槽号和接口编号组成。]{style="font-family:宋体"}

[[[node-identifier ]{lang="EN-US"}]{.commandkeywordsChar}[{[ mac ]{.commandkeywordsChar}\|[ sysname ]{.commandkeywordsChar}\|[ user-defined]{.commandkeywordsChar} *node-identifier* }]{lang="EN-US"}]{#struct_0_x1331_x1769_x1568980643}[：指定接入节点标识。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[mac]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_946197982}[：表示以节点的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为节点标识。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[sysname]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x47234434}[：表示以节点的设备名称作为节点标识。设备的系统名称可以通过系统视图下的]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置。不管配置了哪种填充格式，设备的系统名称始终采用]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[user-defined]{lang="EN-US"}]{.commandkeywordsChar}*[ node-identifier]{lang="EN-US"}*]{#struct_0_x1331_x1769_650957966}[：表示以指定的字符串作为节点标识，]{lang="EN-US" style="font-family:
宋体"}*[node-identifier]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[50]{lang="EN-US"}[个字符的字符串，区分大小写。]{lang="EN-US" style="font-family:宋体"}[不管配置了哪种填充格式，指定的字符串始终采用]{style="font-family:
宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_x1331_x1769_829322448}[：表示以接口名构成接口信息，始终采用]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码格式填充。]{style="font-family:宋体"}

[[[format]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x439804148}[：指定]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充格式。]{style="font-family:宋体"}

[[[ascii]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2007371943}[：指定以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项，即将数值转换为对应的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码填充到]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[[hex]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111343022}[：指定以]{style="font-family:宋体"}[十六进制数值的]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1727240754}

[[以不同模式]{style="font-family:宋体"}]{#struct_0_x1331_x1769_922498086}[填充]{style="font-family:宋体"}[Circuit ID]{lang="FR"}[子选项时，]{style="font-family:宋体"}[填充格式有所不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[以用户配置的字符串填充]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x1984736557}[Circuit ID]{lang="FR"}[子选项时]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[填充格式固定为]{lang="EN-US" style="font-family:
宋体"}[ASCII]{lang="FR"}[码]{lang="EN-US" style="font-family:
宋体"}[格式]{lang="EN-US" style="font-family:宋体"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[以]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x1833018429}[Normal]{lang="FR"}[和]{lang="EN-US" style="font-family:宋体"}[Verbose]{lang="FR"}[模式填充]{lang="EN-US" style="font-family:宋体"}[Circuit ID]{lang="FR"}[子选项时]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[填充格式由]{lang="EN-US" style="font-family:
宋体"}[本命令的配置]{lang="EN-US" style="font-family:宋体"}[决定。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1209348644}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1443143640}[本命令中未指定填充格式，则对于]{style="font-family:
宋体"}[Normal]{lang="FR"}[模式，]{style="font-family:
宋体"}[VLAN ID]{lang="FR"}[和端口号均以]{style="font-family:宋体"}[hex]{lang="FR"}[格式填充]{style="font-family:宋体"}[；]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[Verbose]{lang="FR"}[模式，节点标识（]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、设备的系统名称或指定的字符串）]{style="font-family:宋体"}[、]{style="font-family:宋体"}[以太网类型、框号、槽号、子槽号、接口编号均以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充，]{style="font-family:宋体"}[VLAN ID]{lang="FR"}[以]{style="font-family:宋体"}[hex]{lang="FR"}[格式填充。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果本命令中指定填充格式为]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x648504392}**[ascii]{lang="EN-US"}**[，则所有内容均以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码格式填充。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本命令中指定填充格式为]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x506052919}[[hex]{lang="FR"}]{.commandkeywordsChar}[，则对于]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[和端口号均以]{style="font-family:宋体"}[hex]{lang="EN-US"}[格式填充；对于]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[模式，设备的节点标识、以太网类型以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码格式填充，其余内容均以]{style="font-family:宋体"}[hex]{lang="EN-US"}[格式填充。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果以设备的系统名称（]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2111408558}**[sysname]{lang="EN-US"}**[）作为节点标识填充]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则系统名称中不能包含空格；否则，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继添加或替换]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x1916757852}[的]{style="font-family:
宋体"}[Circuit ID]{lang="EN-US"}[子选项信息中无法携带携带接口拆分信息或子接口信息，关于"接口拆分"和"子接口"的详细介绍，请参见"以太网接口配置指导"中的"以太网接口通用配置"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1414881795}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1127224269}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_2140692920}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1697034657}[配置以]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Circuit ID]{lang="FR"}[子选项，节点标识为设备的系统名称，填充格式为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2111736238}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information strategy replace]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information circuit-id verbose node-identifier sysname format ascii]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x1419648580}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x101213067}[配置以]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Circuit ID]{lang="FR"}[子选项，节点标识为设备的系统名称，填充格式为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1588821023}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information enable]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information strategy replace]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information circuit-id verbose node-identifier sysname format ascii]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1353378566}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_x326252022}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information strategy]{lang="EN-US"}**]{#struct_0_x1331_x1769_787999210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp relay information]{lang="EN-US"}**]{#struct_0_x1331_x1769_1439172000}
:::

::: {#-231141003 .myid}
[]{#_Toc404786462}[]{#struct_0_x1331_x1769_2111801774}[]{#_Toc269455631}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information enable**

------------------------------------------------------------------------

[[[dhcp relay information enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_178094856}[命令用来启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[[undo dhcp relay information enable]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1718234760}[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_870580876}

[[dhcp relay information enable]{lang="EN-US"}]{#struct_0_x1331_x1769_x702422184}

[[undo dhcp relay information enable]{lang="EN-US"}]{#struct_0_x1331_x1769_256116787}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x700877023}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1603907656}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111211951}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x975600700}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_325124801}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1179566372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x879890431}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1851458308}

[[启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x128530075}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继将向转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的请求报文中增加]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项。选项内容由]{style="font-family:宋体"}**[dhcp relay information circuit-id]{lang="EN-US"}**[命令和]{style="font-family:宋体"}**[dhcp relay information remote-id]{lang="EN-US"}**[命令决定。如果]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[中继收到的请求报文中已经包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项，则按照]{style="font-family:宋体"}**[dhcp relay information strategy]{lang="EN-US"}**[命令配置的策略处理请求报文。]{style="font-family:
宋体"}

[[关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_362021180}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继不会向转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的请求报文中增加]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项，也不检查收到的请求报文中是否包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x57434186}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_2111277487}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1009160955}[启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1428985872}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x1196122183}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1590823606}[启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_970747744}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x782328102}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information circuit-id]{lang="EN-US"}**]{#struct_0_x1331_x1769_x678453296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information remote-id]{lang="EN-US"}**]{#struct_0_x1331_x1769_2111080879}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information strategy]{lang="EN-US"}**]{#struct_0_x1331_x1769_x213321557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp relay information]{lang="EN-US"}**]{#struct_0_x1331_x1769_1664048550}
:::

::: {#-1710198678 .myid}
[]{#_Toc94500159}[]{#_Toc69790710}[]{#_Toc29807983}[]{#_Toc266880280}[]{#_Toc202081891}[]{#_Toc404786463}[]{#struct_0_x1331_x1769_1470672632}[]{#_Toc269455727}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information remote-id**

------------------------------------------------------------------------

[[[dhcp relay information remote-id]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x355983880}[命令用来配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的填充模式和填充格式。]{style="font-family:宋体"}

[[[undo dhcp relay information remote-id]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_17536293}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_25052559}

[[[dhcp relay information remote-id ]{lang="EN-US"}]{.commandkeywordsChar}[{[ normal ]{.commandkeywordsChar}\[[ format ]{.commandkeywordsChar}{[ ascii ]{.commandkeywordsChar}\|[ hex]{.commandkeywordsChar} } \] \|[ string]{.commandkeywordsChar} *remote-id* \|[ sysname ]{.commandkeywordsChar}}]{lang="EN-US"}]{#struct_0_x1331_x1769_1543330513}

[[undo dhcp relay information remote-id]{lang="EN-US"}]{#struct_0_x1331_x1769_2111146415}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1722016120}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x28489045}[的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的填充模式为]{style="font-family:宋体"}[Normal]{lang="EN-US"}[、填充格式为]{style="font-family:宋体"}[hex]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1146993303}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_599554725}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x566248274}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1049330748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x836869488}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_155587420}

[[[normal]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111474095}[：指定以]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项，填充内容为接收报文接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[format]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x647640179}[：指定]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的填充格式。如果没有配置，则以]{style="font-family:宋体"}[hex]{lang="EN-US"}[格式填充。]{style="font-family:宋体"}

[[[ascii]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2013401490}[：指定以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项，即将数值转换为对应的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码填充到]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[[hex]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x153910138}[：指定以]{style="font-family:宋体"}[十六进制数值的]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[[string]{lang="EN-US"}]{.commandkeywordsChar}*[ remote-id]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1309674771}[：指定以用户配置的字符串填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}*[remote-id]{lang="EN-US"}*[表示用户配置的用来填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的内容，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[[sysname]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_49434744}[：指定以设备的系统名称填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。设备的系统名称可以通过系统视图下的]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2013044466}

[[以用户配置的字符串（]{style="font-family:宋体"}**[string]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1046775356}[）和设备的系统名称（]{style="font-family:宋体"}[[sysname]{lang="EN-US"}]{.commandkeywordsChar}[）填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项时，填充内容固定为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[格式；以]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项时，填充内容的格式由本命令配置的填充格式决定。]{style="font-family:宋体"}

[[需要注意的是，如果多次执行本命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1051957541}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_236581809}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_2111539631}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1424348927}[配置采用字符串]{style="font-family:宋体"}[device001]{lang="EN-US"}[填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_449134153}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information strategy replace]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information remote-id string device001]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x2015441171}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_914966982}[配置采用字符串]{style="font-family:宋体"}[device001]{lang="EN-US"}[填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1177582253}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information enable]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information strategy replace]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information remote-id string device001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2111343023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_1727306290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information strategy]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1423553853}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp relay information]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1460316710}
:::

::: {#210003079 .myid}
[]{#_Toc404786464}[]{#struct_0_x1331_x1769_x756982162}[]{#_Toc269455728}[]{#_Toc266880281}[]{#_Toc202081892}[]{#_Toc259787223}[]{#_Toc260047155}[]{#_Toc260065402}[]{#_Toc259787225}[]{#_Toc260047157}[]{#_Toc260065404}[]{#_Toc259787226}[]{#_Toc260047158}[]{#_Toc260065405}[]{#_Toc259787227}[]{#_Toc260047159}[]{#_Toc260065406}[]{#_Toc259787228}[]{#_Toc260047160}[]{#_Toc260065407}[]{#_Toc259787229}[]{#_Toc260047161}[]{#_Toc260065408}[]{#_Toc259787230}[]{#_Toc260047162}[]{#_Toc260065409}[]{#_Toc259787231}[]{#_Toc260047163}[]{#_Toc260065410}[]{#_Toc259787232}[]{#_Toc260047164}[]{#_Toc260065411}[]{#_Toc259787233}[]{#_Toc260047165}[]{#_Toc260065412}[]{#_Toc259787234}[]{#_Toc260047166}[]{#_Toc260065413}[]{#_Toc259787235}[]{#_Toc260047167}[]{#_Toc260065414}[]{#_Toc259787236}[]{#_Toc260047168}[]{#_Toc260065415}[]{#_Toc259787237}[]{#_Toc260047169}[]{#_Toc260065416}[]{#_Toc259787238}[]{#_Toc260047170}[]{#_Toc260065417}[]{#_Toc259787239}[]{#_Toc260047171}[]{#_Toc260065418}[]{#_Toc259787240}[]{#_Toc260047172}[]{#_Toc260065419}[]{#_Toc259787241}[]{#_Toc260047173}[]{#_Toc260065420}[]{#_Toc259787242}[]{#_Toc260047174}[]{#_Toc260065421}[]{#_Toc259787243}[]{#_Toc260047175}[]{#_Toc260065422}[]{#_Toc259787244}[]{#_Toc260047176}[]{#_Toc260065423}[]{#_Toc259787245}[]{#_Toc260047177}[]{#_Toc260065424}[]{#_Toc259787246}[]{#_Toc260047178}[]{#_Toc260065425}[]{#_Toc259787247}[]{#_Toc260047179}[]{#_Toc260065426}[]{#_Toc259787248}[]{#_Toc260047180}[]{#_Toc260065427}[]{#_Toc259787249}[]{#_Toc260047181}[]{#_Toc260065428}[]{#_Toc259787251}[]{#_Toc260047183}[]{#_Toc260065430}[]{#_Toc259787252}[]{#_Toc260047184}[]{#_Toc260065431}[]{#_Toc259787253}[]{#_Toc260047185}[]{#_Toc260065432}[]{#_Toc259787255}[]{#_Toc260047187}[]{#_Toc260065434}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay information strategy**

------------------------------------------------------------------------

[[[dhcp relay information strategy]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1552484789}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的请求报文的处理策略。]{style="font-family:宋体"}

[[[undo dhcp relay information strategy]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x426946008}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1464592249}

[**[dhcp relay information strategy]{lang="EN-US"}**[ { **drop** \| **keep** \| **replace** }]{lang="EN-US"}]{#struct_0_x1331_x1769_x866501620}

[[undo dhcp relay information strategy]{lang="EN-US"}]{#struct_0_x1331_x1769_2111408559}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1414816259}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x694961537}[中继对带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的请求报文的处理策略为]{style="font-family:宋体"}**[replace]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x487411217}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1360640388}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_219501458}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_873864848}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_819385169}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1794244252}

[[[drop]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_2111736239}[：如果报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则丢弃该报文。]{style="font-family:宋体"}

[[[keep]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1419714116}[：如果报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则保持该报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[不变并进行转发。]{style="font-family:宋体"}

[[[replace]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1630809002}[：如果报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则按照配置的填充内容和填充格式填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，用该选项替换报文中原有的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，并进行转发。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2107760795}

[[本命令仅对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_1637422913}[的请求报文有效。]{style="font-family:宋体"}

[[如果启用了]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1992949197}[中继支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能，则对于接收到的不包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的请求报文，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的处理方式始终为在请求报文中添加]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，并转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1968078951}[中继对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[请求报文的处理策略为]{style="font-family:宋体"}**[replace]{lang="EN-US"}**[时，需要配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的填充模式和填充格式；处理策略为]{style="font-family:宋体"}**[keep]{lang="EN-US"}**[或]{style="font-family:宋体"}**[drop]{lang="EN-US"}**[时，不需要配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项的填充模式和填充格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1182122468}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x397264022}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2111801775}[配置接收到的请求报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继保持该报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[不变并进行转发。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_178160392}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay information strategy keep]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x150273390}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1961978867}[配置接收到的请求报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继保持该报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[不变并进行转发。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_93394942}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information enable]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay information strategy keep]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_304624598}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay information enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_894033225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp relay information]{lang="EN-US"}**]{#struct_0_x1331_x1769_x617671401}
:::

::: {#-646842698 .myid}
[]{#_Toc404786465}[]{#struct_0_x1331_x1769_x1564910013}[]{#_Toc269455729}[]{#_Toc266880282}[]{#_Toc202081893}[]{#_Toc137350319}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay release ip**

------------------------------------------------------------------------

[[[dhcp relay release ip]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1954210655}[命令用来配置向]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器请求释放客户端申请到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1399661910}

[[[dhcp relay release ip ]{lang="EN-US"}]{.commandkeywordsChar}*[client-ip]{lang="EN-US"}*[ \[ [vpn-instance]{.commandkeywordsChar} *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_1611785167}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1651416434}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_334600984}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_893342915}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x617605865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1251594063}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_254832943}

[*[client-ip]{lang="EN-US"}*]{#struct_0_x1331_x1769_2117685287}[：请求释放的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[[vpn-instance]{lang="EN-US"}]{.commandkeywordsChar}*[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1331_x1769_1333352111}[：指定需要释放的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[[。]{style="font-family:宋体"}]{.MsoCommentReference}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示释放公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x1331_x1769_1834613}

[[如果]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1527678473}[中继上存在客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对应的动态用户地址表项，则配置通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继释放该客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继会主动向]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送]{style="font-family:宋体"}[DHCP-RELEASE]{lang="EN-US"}[报文。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器收到该报文后，将会释放指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的绑定信息。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继也会删除该动态用户地址表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x493136437}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1704857303}[向]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器请求释放客户端申请到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x617802473}

[\[Sysname\] dhcp relay release ip 1.1.1.1]{lang="EN-US"}
:::

::: {#-947150356 .myid}
[]{#_Toc404786466}[]{#struct_0_x1331_x1769_x9770519}[]{#_Toc269455733}[]{#_Toc266880347}[]{#_Toc202081898}[]{#_Toc137350324}[]{#_Toc263946392}[]{#_Toc263953369}[]{#_Toc264019665}[]{#_Toc264020001}[]{#_Toc265140179}[]{#_Toc266880286}[]{#_Toc263946394}[]{#_Toc263953371}[]{#_Toc264019667}[]{#_Toc264020003}[]{#_Toc265140181}[]{#_Toc266880288}[]{#_Toc263946395}[]{#_Toc263953372}[]{#_Toc264019668}[]{#_Toc264020004}[]{#_Toc265140182}[]{#_Toc266880289}[]{#_Toc263946396}[]{#_Toc263953373}[]{#_Toc264019669}[]{#_Toc264020005}[]{#_Toc265140183}[]{#_Toc266880290}[]{#_Toc263946397}[]{#_Toc263953374}[]{#_Toc264019670}[]{#_Toc264020006}[]{#_Toc265140184}[]{#_Toc266880291}[]{#_Toc263946398}[]{#_Toc263953375}[]{#_Toc264019671}[]{#_Toc264020007}[]{#_Toc265140185}[]{#_Toc266880292}[]{#_Toc263946399}[]{#_Toc263953376}[]{#_Toc264019672}[]{#_Toc264020008}[]{#_Toc265140186}[]{#_Toc266880293}[]{#_Toc263946400}[]{#_Toc263953377}[]{#_Toc264019673}[]{#_Toc264020009}[]{#_Toc265140187}[]{#_Toc266880294}[]{#_Toc263946401}[]{#_Toc263953378}[]{#_Toc264019674}[]{#_Toc264020010}[]{#_Toc265140188}[]{#_Toc266880295}[]{#_Toc263946402}[]{#_Toc263953379}[]{#_Toc264019675}[]{#_Toc264020011}[]{#_Toc265140189}[]{#_Toc266880296}[]{#_Toc263946403}[]{#_Toc263953380}[]{#_Toc264019676}[]{#_Toc264020012}[]{#_Toc265140190}[]{#_Toc266880297}[]{#_Toc263946405}[]{#_Toc263953382}[]{#_Toc264019678}[]{#_Toc264020014}[]{#_Toc265140192}[]{#_Toc266880299}[]{#_Toc263946406}[]{#_Toc263953383}[]{#_Toc264019679}[]{#_Toc264020015}[]{#_Toc265140193}[]{#_Toc266880300}[]{#_Toc263946407}[]{#_Toc263953384}[]{#_Toc264019680}[]{#_Toc264020016}[]{#_Toc265140194}[]{#_Toc266880301}[]{#_Toc263946408}[]{#_Toc263953385}[]{#_Toc264019681}[]{#_Toc264020017}[]{#_Toc265140195}[]{#_Toc266880302}[]{#_Toc263946409}[]{#_Toc263953386}[]{#_Toc264019682}[]{#_Toc264020018}[]{#_Toc265140196}[]{#_Toc266880303}[]{#_Toc263946410}[]{#_Toc263953387}[]{#_Toc264019683}[]{#_Toc264020019}[]{#_Toc265140197}[]{#_Toc266880304}[]{#_Toc263946411}[]{#_Toc263953388}[]{#_Toc264019684}[]{#_Toc264020020}[]{#_Toc265140198}[]{#_Toc266880305}[]{#_Toc263946412}[]{#_Toc263953389}[]{#_Toc264019685}[]{#_Toc264020021}[]{#_Toc265140199}[]{#_Toc266880306}[]{#_Toc263946413}[]{#_Toc263953390}[]{#_Toc264019686}[]{#_Toc264020022}[]{#_Toc265140200}[]{#_Toc266880307}[]{#_Toc263946414}[]{#_Toc263953391}[]{#_Toc264019687}[]{#_Toc264020023}[]{#_Toc265140201}[]{#_Toc266880308}[]{#_Toc263946415}[]{#_Toc263953392}[]{#_Toc264019688}[]{#_Toc264020024}[]{#_Toc265140202}[]{#_Toc266880309}[]{#_Toc263946416}[]{#_Toc263953393}[]{#_Toc264019689}[]{#_Toc264020025}[]{#_Toc265140203}[]{#_Toc266880310}[]{#_Toc263946417}[]{#_Toc263953394}[]{#_Toc264019690}[]{#_Toc264020026}[]{#_Toc265140204}[]{#_Toc266880311}[]{#_Toc263700667}[]{#_Toc263946419}[]{#_Toc263953396}[]{#_Toc264019692}[]{#_Toc264020028}[]{#_Toc265140206}[]{#_Toc266880313}[]{#_Toc263700668}[]{#_Toc263946420}[]{#_Toc263953397}[]{#_Toc264019693}[]{#_Toc264020029}[]{#_Toc265140207}[]{#_Toc266880314}[]{#_Toc263700670}[]{#_Toc263946422}[]{#_Toc263953399}[]{#_Toc264019695}[]{#_Toc264020031}[]{#_Toc265140209}[]{#_Toc266880316}[]{#_Toc263700671}[]{#_Toc263946423}[]{#_Toc263953400}[]{#_Toc264019696}[]{#_Toc264020032}[]{#_Toc265140210}[]{#_Toc266880317}[]{#_Toc263700672}[]{#_Toc263946424}[]{#_Toc263953401}[]{#_Toc264019697}[]{#_Toc264020033}[]{#_Toc265140211}[]{#_Toc266880318}[]{#_Toc263700673}[]{#_Toc263946425}[]{#_Toc263953402}[]{#_Toc264019698}[]{#_Toc264020034}[]{#_Toc265140212}[]{#_Toc266880319}[]{#_Toc263700674}[]{#_Toc263946426}[]{#_Toc263953403}[]{#_Toc264019699}[]{#_Toc264020035}[]{#_Toc265140213}[]{#_Toc266880320}[]{#_Toc263700675}[]{#_Toc263946427}[]{#_Toc263953404}[]{#_Toc264019700}[]{#_Toc264020036}[]{#_Toc265140214}[]{#_Toc266880321}[]{#_Toc263700676}[]{#_Toc263946428}[]{#_Toc263953405}[]{#_Toc264019701}[]{#_Toc264020037}[]{#_Toc265140215}[]{#_Toc266880322}[]{#_Toc263700677}[]{#_Toc263946429}[]{#_Toc263953406}[]{#_Toc264019702}[]{#_Toc264020038}[]{#_Toc265140216}[]{#_Toc266880323}[]{#_Toc263700678}[]{#_Toc263946430}[]{#_Toc263953407}[]{#_Toc264019703}[]{#_Toc264020039}[]{#_Toc265140217}[]{#_Toc266880324}[]{#_Toc263700679}[]{#_Toc263946431}[]{#_Toc263953408}[]{#_Toc264019704}[]{#_Toc264020040}[]{#_Toc265140218}[]{#_Toc266880325}[]{#_Toc263700681}[]{#_Toc263946433}[]{#_Toc263953410}[]{#_Toc264019706}[]{#_Toc264020042}[]{#_Toc265140220}[]{#_Toc266880327}[]{#_Toc263700683}[]{#_Toc263946435}[]{#_Toc263953412}[]{#_Toc264019708}[]{#_Toc264020044}[]{#_Toc265140222}[]{#_Toc266880329}[]{#_Toc263700684}[]{#_Toc263946436}[]{#_Toc263953413}[]{#_Toc264019709}[]{#_Toc264020045}[]{#_Toc265140223}[]{#_Toc266880330}[]{#_Toc263700685}[]{#_Toc263946437}[]{#_Toc263953414}[]{#_Toc264019710}[]{#_Toc264020046}[]{#_Toc265140224}[]{#_Toc266880331}[]{#_Toc263700687}[]{#_Toc263946439}[]{#_Toc263953416}[]{#_Toc264019712}[]{#_Toc264020048}[]{#_Toc265140226}[]{#_Toc266880333}[]{#_Toc263700688}[]{#_Toc263946440}[]{#_Toc263953417}[]{#_Toc264019713}[]{#_Toc264020049}[]{#_Toc265140227}[]{#_Toc266880334}[]{#_Toc263700690}[]{#_Toc263946442}[]{#_Toc263953419}[]{#_Toc264019715}[]{#_Toc264020051}[]{#_Toc265140229}[]{#_Toc266880336}[]{#_Toc263700691}[]{#_Toc263946443}[]{#_Toc263953420}[]{#_Toc264019716}[]{#_Toc264020052}[]{#_Toc265140230}[]{#_Toc266880337}[]{#_Toc263700692}[]{#_Toc263946444}[]{#_Toc263953421}[]{#_Toc264019717}[]{#_Toc264020053}[]{#_Toc265140231}[]{#_Toc266880338}[]{#_Toc263700693}[]{#_Toc263946445}[]{#_Toc263953422}[]{#_Toc264019718}[]{#_Toc264020054}[]{#_Toc265140232}[]{#_Toc266880339}[]{#_Toc263700694}[]{#_Toc263946446}[]{#_Toc263953423}[]{#_Toc264019719}[]{#_Toc264020055}[]{#_Toc265140233}[]{#_Toc266880340}[]{#_Toc263700695}[]{#_Toc263946447}[]{#_Toc263953424}[]{#_Toc264019720}[]{#_Toc264020056}[]{#_Toc265140234}[]{#_Toc266880341}[]{#_Toc263700696}[]{#_Toc263946448}[]{#_Toc263953425}[]{#_Toc264019721}[]{#_Toc264020057}[]{#_Toc265140235}[]{#_Toc266880342}[]{#_Toc263700697}[]{#_Toc263946449}[]{#_Toc263953426}[]{#_Toc264019722}[]{#_Toc264020058}[]{#_Toc265140236}[]{#_Toc266880343}[]{#_Toc263700698}[]{#_Toc263946450}[]{#_Toc263953427}[]{#_Toc264019723}[]{#_Toc264020059}[]{#_Toc265140237}[]{#_Toc266880344}[]{#_Toc263700699}[]{#_Toc263946451}[]{#_Toc263953428}[]{#_Toc264019724}[]{#_Toc264020060}[]{#_Toc265140238}[]{#_Toc266880345}

**DHCP \-- DHCP中继配置命令 \-- dhcp relay server-address**

------------------------------------------------------------------------

[[[dhcp relay server-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1861725987}[命令用来在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继上指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的地址。]{style="font-family:宋体"}

[[[undo dhcp relay server-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1069521514}[命令用来在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继上删除指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_414500805}

[[[dhcp relay server-address]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_352768936}

[[[undo dhcp relay server-address ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ ]{.commandkeywordsChar}*ip-address* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_607995160}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1023892594}

[[没有在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617736937}[中继上指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x2021082126}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1668084915}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1455498808}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_36030821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_883894965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1152098293}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1066466009}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继将]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发送的报文转发到该地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617409257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定的]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x837549346}[DHCP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址在同一网段。否则，可能导致客户端无法获得]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过多次执行]{lang="EN-US" style="font-family:宋体"}[[dhcp relay server-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1753354933}[命令可以指定多个]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址。一个接口上最多可以指定]{lang="EN-US" style="font-family:宋体"}[8]{lang="EN-US"}[个]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址。]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继接收到]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发送的报文后，将其转发给所有的]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}[[undo dhcp relay server-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1304079676}[命令时，如果没有指定]{lang="EN-US" style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[参数，则删除接口上的所有]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2021251971}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x1193501773}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_489566777}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1934771958}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp relay server-address 1.1.1.1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x617343721}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1156156280}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[上为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_346184378}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp relay server-address 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_282306475}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp select relay]{lang="EN-US"}**]{#struct_0_x1331_x1769_722687224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp relay interface]{lang="EN-US"}**]{#struct_0_x1331_x1769_1372652700}
:::

::: {#886316886 .myid}
[]{#_Toc269455736}[]{#_Toc266880381}[]{#_Toc202081903}[]{#_Toc404786467}[]{#struct_0_x1331_x1769_x1346757125}[]{#_Toc344456831}[]{#_Toc343608027}

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay check mac-address**

------------------------------------------------------------------------

[**[display dhcp relay check mac-address]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2088168753}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617540329}

[**[display dhcp relay check mac-address]{lang="EN-US"}**]{#struct_0_x1331_x1769_x795291009}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1275769063}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x2001265863}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_213143597}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_716882454}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x594997826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_235903782}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x617474793}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_768714001}

[[\# DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1121559093}[中继的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查表项。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp relay check mac-address]{lang="EN-US"}]{#struct_0_x1331_x1769_1729845751}

[Source-MAC        Interface                 Aging-time]{lang="EN-US"}

[23f3-1122-adf1    GE1/0/1                   10]{lang="EN-US"}

[23f3-1122-2230    GE1/0/2                   30]{lang="EN-US"}

[]{#struct_0_x1331_x1769_x1606626037}[[表1-8 ]{lang="EN-US"}[display ]{lang="EN-US"}]{#_Toc182191693}[dhcp relay check mac-address]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1459796732}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1641186020}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1212446118}

[[Source MAC]{lang="EN-US"}]{#struct_0_x1331_x1769_x617147113}

[[检测到攻击的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1331_x1769_x1978382669}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1331_x1769_664111960}

[[攻击来源的接口]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1947484002}

[[Aging-time]{lang="EN-US"}]{#struct_0_x1331_x1769_x1545506586}

[[DDOS]{lang="EN-US"}]{#struct_0_x1331_x1769_x617081577}[攻击检测表项剩余时间，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1233676256 .myid}
[]{#_Toc404786468}[]{#struct_0_x1331_x1769_356605212}

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay client-information**

------------------------------------------------------------------------

[]{#_Toc94500154}[]{#_Toc69790705}[]{#struct_0_x1331_x1769_x1874512771}[]{#_Toc45685354}[[display dhcp relay client-information]{lang="EN-US"}]{.commandkeywordsChar}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的用户地址表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_388169339}

[[[display dhcp relay client-information ]{lang="EN-US"}]{.commandkeywordsChar}[\[ [interface]{.commandkeywordsChar} *interface-type interface-number*[ ]{.commandkeywordsChar}\| [ip]{.commandkeywordsChar} *ip-address*[ ]{.commandkeywordsChar}\[ [vpn-instance]{.commandkeywordsChar} *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1374356850}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617671400}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1564975549}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x643874418}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x2037039258}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_292774485}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_243487959}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_1460287448}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x544373681}

[[[interface]{lang="EN-US"}]{.commandkeywordsChar}[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_885169257}[：显示指定接口上的用户地址表项信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_x617605864}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的用户地址表项信息。]{style="font-family:宋体"}

[[[vpn-instance]{lang="EN-US"}]{.commandkeywordsChar}[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1251528527}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的用户地址表项信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1707176155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有执行]{lang="EN-US" style="font-family:宋体"}**[dhcp relay client-information record]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1367282548}[命令后，]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继才会记录用户地址表项信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1385613679}[DHCP]{lang="EN-US"}[中继的用户地址表项信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1388053134}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1624964392}[显示所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的用户地址表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp relay client-information]{lang="EN-US"}]{#struct_0_x1331_x1769_x617802472}

[Total number of client-information items: 2]{lang="EN-US"}

[Total number of dynamic items: 1]{lang="EN-US"}

[Total number of temporary items: 1]{lang="EN-US"}

[IP address       MAC address      Type        Interface            VPN name ]{lang="EN-US"}

[10.1.1.1         00e0-0000-0001   Dynamic     GE1/0/1              VPN1]{lang="EN-US"}

[10.1.1.5         00e0-0000-0000   Temporary   Vlan2                VPN2]{lang="EN-US"}

[]{#struct_0_x1331_x1769_x9704983}[[表1-9 ]{lang="EN-US"}[display dhcp relay client-information]{lang="EN-US"}]{#_Toc138412529}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1464427460}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1118469866}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1102918876}

[[Total number of client-information items]{lang="EN-US"}]{#struct_0_x1331_x1769_x1666529378}

[[用户地址信息条目总数]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1191422637}

[[Total number of dynamic items]{lang="EN-US"}]{#struct_0_x1331_x1769_x617736936}

[[动态用户地址条目总数]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x2021147662}

[[Total number of temporary items]{lang="EN-US"}]{#struct_0_x1331_x1769_663004972}

[[临时用户地址条目总数]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1127536688}

[[IP address]{lang="EN-US"}]{#struct_0_x1331_x1769_x465216778}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1935858749}[客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1331_x1769_x617409256}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x837483810}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1331_x1769_x1755424979}

[[用户地址表项的取值包括：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1227636312}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_x1331_x1769_1030441575}[：动态用户地址表项，接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器对]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端]{style="font-family:宋体"}[REQUEST]{lang="EN-US"}[请求的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[应答后，创建的用户表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Temporary]{lang="EN-US"}]{#struct_0_x1331_x1769_x617343720}[：临时用户地址表项，接收]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的]{lang="EN-US" style="font-family:宋体"}[REQUEST]{lang="EN-US"}[请求，但未收到]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}[ACK]{lang="EN-US"}[应答时，创建的用户表项]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1331_x1769_x1156090744}

[[与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1733580739}[客户端相连的三层接口。如果用户地址表项中没有记录接口，则显示为]{style="font-family:宋体"}["N/A"]{lang="EN-US"}

[[VPN name]{lang="EN-US"}]{#struct_0_x1331_x1769_2068425873}

[[VPN]{lang="EN-US"}]{#struct_0_x1331_x1769_x2001367339}[实例名称，如果表项不属于任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}["N/A"]{lang="EN-US"}

[[ ]{lang="EN-US"}]{#_Toc29807979}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1997987394}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp relay client-information record]{lang="EN-US"}**]{#struct_0_x1331_x1769_x617540328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[reset dhcp relay client-information]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x795225473}

::: {#-2078384262 .myid}
[]{#_Toc137350327}[]{#_Toc404786469}[]{#struct_0_x1331_x1769_56329038}[]{#_Toc269455735}[]{#_Toc266880380}[]{#_Toc202081902}

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay information**

------------------------------------------------------------------------

[[[display dhcp relay information]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_1528068462}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继上的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x316942147}

[[[display dhcp relay information]{lang="EN-US"}]{.commandkeywordsChar}[ \[[ interface]{.commandkeywordsChar} *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1901205048}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1880653701}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x836108618}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617474792}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_768648465}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_1541091184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x452937624}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x2135113041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_778391865}

[[[interface]{lang="EN-US"}]{.commandkeywordsChar}*[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1851606529}[：显示指定接口上的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定本参数，则显示所有接口上的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1416142573}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x617147112}[显示所有接口上的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp relay information]{lang="EN-US"}]{#struct_0_x1331_x1769_x1978317133}

[Interface: Vlan-interface100]{lang="EN-US"}

[   Status: Enable]{lang="EN-US"}

[   Strategy: Replace]{lang="EN-US"}

[   Circuit ID Pattern: Verbose]{lang="EN-US"}

[   Remote ID Pattern: Sysname]{lang="EN-US"}

[   Circuit ID format: Undefined]{lang="EN-US"}

[   Remote ID format: ASCII]{lang="EN-US"}

[   Node identifier: aabbcc]{lang="EN-US"}

[Interface: Vlan-interface200]{lang="EN-US"}

[   Status: Enable]{lang="EN-US"}

[   Strategy: Replace]{lang="EN-US"}

[   Circuit ID Pattern: User Defined]{lang="EN-US"}

[   Remote ID Pattern: User Defined]{lang="EN-US"}

[   Circuit ID format: ASCII]{lang="EN-US"}

[   Remote ID format: ASCII]{lang="EN-US"}

[   User defined:]{lang="EN-US"}

[   Circuit ID: vlan100]{lang="EN-US"}

[   Remote ID: device001]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display dhcp relay information]{lang="EN-US"}]{#struct_0_x1331_x1769_1433991070}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1471641033}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617081576}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_356670748}

[[Interface]{lang="EN-US"}]{#struct_0_x1331_x1769_1599503265}

[[接口名]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1493367350}

[[Status]{lang="EN-US"}]{#struct_0_x1331_x1769_x203698840}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x828860800}[的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x1331_x1769_x617671403}[：]{lang="EN-US" style="font-family:宋体"}[启用]{style="font-family:宋体"}[了]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继支持]{lang="EN-US" style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1331_x1769_x1564778941}[：未]{lang="EN-US" style="font-family:宋体"}[启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继支持]{lang="EN-US" style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}

[[Strategy]{lang="EN-US"}]{#struct_0_x1331_x1769_752917690}

[[对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x1102040828}[的请求报文的处理策略，取值为]{style="font-family:宋体"}[Drop]{lang="EN-US"}[、]{style="font-family:宋体"}[Keep]{lang="EN-US"}[或]{style="font-family:宋体"}[Replace]{lang="EN-US"}

[[Circuit ID Pattern]{lang="EN-US"}]{#struct_0_x1331_x1769_x1220927080}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1032536997}[子选项的填充方式，取值为]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[、]{style="font-family:宋体"}[Normal]{lang="EN-US"}[或]{style="font-family:宋体"}[User Defined]{lang="EN-US"}

[[Remote ID Pattern]{lang="EN-US"}]{#struct_0_x1331_x1769_x617605867}

[[Remote ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1251462991}[子选项的填充方式，取值为]{style="font-family:宋体"}[Sysname]{lang="EN-US"}[、]{style="font-family:宋体"}[Normal]{lang="EN-US"}[或]{style="font-family:宋体"}[User Defined]{lang="EN-US"}

[[Circuit ID format]{lang="EN-US"}]{#struct_0_x1331_x1769_657556991}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1912472246}[子选项的填充格式，取值为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[、]{style="font-family:宋体"}[Hex]{lang="EN-US"}[或]{style="font-family:宋体"}[Undefined]{lang="EN-US"}

[[Remote ID format]{lang="EN-US"}]{#struct_0_x1331_x1769_6113995}

[[Remote ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x617802475}[子选项的填充格式，取值为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[、]{style="font-family:宋体"}[Hex]{lang="EN-US"}[或]{style="font-family:宋体"}[Undefined]{lang="EN-US"}

[[Node identifier]{lang="EN-US"}]{#struct_0_x1331_x1769_x10163735}

[[接入节点的标识]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1963151224}

[[User defined]{lang="EN-US"}]{#struct_0_x1331_x1769_x2008168378}

[[用户自定义的子选项内容]{style="font-family:宋体"}]{#struct_0_x1331_x1769_829248486}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x617736939}

[[用户自定义的]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x2021999630}[子选项的内容]{style="font-family:宋体"}

[[Remote ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1864889187}

[[用户自定义的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1546646794}[子选项的内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-716533614 .myid}
[]{#_Toc404786470}[]{#struct_0_x1331_x1769_1001575045}[]{#_Toc308513336}[]{#_Toc308513337}[]{#_Toc308513338}[]{#_Toc308513339}[]{#_Toc308513340}[]{#_Toc308513341}[]{#_Toc308513342}[]{#_Toc308513343}[]{#_Toc308513344}[]{#_Toc308513345}[]{#_Toc308513346}[]{#_Toc308513347}[]{#_Toc308513348}[]{#_Toc308513349}[]{#_Toc308513350}[]{#_Toc308513351}[]{#_Toc308513352}[]{#_Toc308513353}[]{#_Toc308513354}[]{#_Toc308513355}[]{#_Toc308513365}[]{#_Toc308513366}[]{#_Toc308513367}

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay server-address**

------------------------------------------------------------------------

[**[display dhcp relay server-address]{lang="EN-US"}**]{#struct_0_x1331_x1769_982870602}[命令用来显示接口上指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617409259}

[**[display dhcp relay server-address]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x836893986}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1041717178}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_868154485}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1128635618}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x321103017}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x799121753}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x594104063}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_1383593995}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617343723}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1156025208}[：显示指定接口上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定本参数，则显示所有接口上的]{style="font-family:
宋体"}[DHCP]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1033064213}

[[ # ]{lang="EN-US"}]{#struct_0_x1331_x1769_x446279591}[显示所有接口上指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp relay server-address]{lang="EN-US"}]{#struct_0_x1331_x1769_1303587350}

[Interface name                 Server IP address]{lang="EN-US"}

[GE1/0/1                        2.2.2.2]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display dhcp relay server-address]{lang="EN-US"}]{#struct_0_x1331_x1769_1307214101}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1476104562}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_669906584}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1910872316}

[[Interface name]{lang="EN-US"}]{#struct_0_x1331_x1769_x617540331}

[[接口名]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x794766722}

[[Server IP address]{lang="EN-US"}]{#struct_0_x1331_x1769_x1515253893}

[[指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_208484343}[服务器地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_568325457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[dhcp relay server-address]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x903333610}

::: {#1685243994 .myid}
[]{#_Toc404786471}[]{#struct_0_x1331_x1769_x617474795}[]{#_Toc269455737}[]{#_Toc266880422}[]{#_Toc202081907}[]{#_Toc137350331}[]{#_Toc263700706}[]{#_Toc263946458}[]{#_Toc263953465}[]{#_Toc264019761}[]{#_Toc264020097}[]{#_Toc265140275}[]{#_Toc266880382}[]{#_Toc263700707}[]{#_Toc263946459}[]{#_Toc263953466}[]{#_Toc264019762}[]{#_Toc264020098}[]{#_Toc265140276}[]{#_Toc266880383}[]{#_Toc263700708}[]{#_Toc263946460}[]{#_Toc263953467}[]{#_Toc264019763}[]{#_Toc264020099}[]{#_Toc265140277}[]{#_Toc266880384}[]{#_Toc263700709}[]{#_Toc263946461}[]{#_Toc263953468}[]{#_Toc264019764}[]{#_Toc264020100}[]{#_Toc265140278}[]{#_Toc266880385}[]{#_Toc263700710}[]{#_Toc263946462}[]{#_Toc263953469}[]{#_Toc264019765}[]{#_Toc264020101}[]{#_Toc265140279}[]{#_Toc266880386}[]{#_Toc263700711}[]{#_Toc263946463}[]{#_Toc263953470}[]{#_Toc264019766}[]{#_Toc264020102}[]{#_Toc265140280}[]{#_Toc266880387}[]{#_Toc263700712}[]{#_Toc263946464}[]{#_Toc263953471}[]{#_Toc264019767}[]{#_Toc264020103}[]{#_Toc265140281}[]{#_Toc266880388}[]{#_Toc263700713}[]{#_Toc263946465}[]{#_Toc263953472}[]{#_Toc264019768}[]{#_Toc264020104}[]{#_Toc265140282}[]{#_Toc266880389}[]{#_Toc263700714}[]{#_Toc263946466}[]{#_Toc263953473}[]{#_Toc264019769}[]{#_Toc264020105}[]{#_Toc265140283}[]{#_Toc266880390}[]{#_Toc263700715}[]{#_Toc263946467}[]{#_Toc263953474}[]{#_Toc264019770}[]{#_Toc264020106}[]{#_Toc265140284}[]{#_Toc266880391}[]{#_Toc263700716}[]{#_Toc263946468}[]{#_Toc263953475}[]{#_Toc264019771}[]{#_Toc264020107}[]{#_Toc265140285}[]{#_Toc266880392}[]{#_Toc263700717}[]{#_Toc263946469}[]{#_Toc263953476}[]{#_Toc264019772}[]{#_Toc264020108}[]{#_Toc265140286}[]{#_Toc266880393}[]{#_Toc263700718}[]{#_Toc263946470}[]{#_Toc263953477}[]{#_Toc264019773}[]{#_Toc264020109}[]{#_Toc265140287}[]{#_Toc266880394}[]{#_Toc263700720}[]{#_Toc263946472}[]{#_Toc263953479}[]{#_Toc264019775}[]{#_Toc264020111}[]{#_Toc265140289}[]{#_Toc266880396}[]{#_Toc263700721}[]{#_Toc263946473}[]{#_Toc263953480}[]{#_Toc264019776}[]{#_Toc264020112}[]{#_Toc265140290}[]{#_Toc266880397}[]{#_Toc263700722}[]{#_Toc263946474}[]{#_Toc263953481}[]{#_Toc264019777}[]{#_Toc264020113}[]{#_Toc265140291}[]{#_Toc266880398}[]{#_Toc263700723}[]{#_Toc263946475}[]{#_Toc263953482}[]{#_Toc264019778}[]{#_Toc264020114}[]{#_Toc265140292}[]{#_Toc266880399}[]{#_Toc263700724}[]{#_Toc263946476}[]{#_Toc263953483}[]{#_Toc264019779}[]{#_Toc264020115}[]{#_Toc265140293}[]{#_Toc266880400}[]{#_Toc263700725}[]{#_Toc263946477}[]{#_Toc263953484}[]{#_Toc264019780}[]{#_Toc264020116}[]{#_Toc265140294}[]{#_Toc266880401}[]{#_Toc263700726}[]{#_Toc263946478}[]{#_Toc263953485}[]{#_Toc264019781}[]{#_Toc264020117}[]{#_Toc265140295}[]{#_Toc266880402}[]{#_Toc263700734}[]{#_Toc263946486}[]{#_Toc263953493}[]{#_Toc264019789}[]{#_Toc264020125}[]{#_Toc265140303}[]{#_Toc266880410}[]{#_Toc263700735}[]{#_Toc263946487}[]{#_Toc263953494}[]{#_Toc264019790}[]{#_Toc264020126}[]{#_Toc265140304}[]{#_Toc266880411}[]{#_Toc263700745}[]{#_Toc263946497}[]{#_Toc263953504}[]{#_Toc264019800}[]{#_Toc264020136}[]{#_Toc265140314}[]{#_Toc266880421}

**DHCP \-- DHCP中继配置命令 \-- display dhcp relay statistics**

------------------------------------------------------------------------

[[[display dhcp relay statistics]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_768320785}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_696564607}

[[[display dhcp relay statistics ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ interface]{.commandkeywordsChar} *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x599265090}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_317621068}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1646799947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1153082141}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1100683610}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1299585504}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x617147115}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1978251597}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_972773010}

[[[interface]{lang="EN-US"}]{.commandkeywordsChar}*[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_2068271526}[：显示指定接口的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继相关报文统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定本参数，则显示所有的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继相关报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x1331_x1769_1489826}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1236947171}[显示所有的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继相关报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp relay statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_x617671402}

[DHCP packets dropped:                  0]{lang="EN-US"}

[DHCP packets received from clients:    0]{lang="EN-US"}

[   DHCPDISCOVER:                       0]{lang="EN-US"}

[   DHCPREQUEST:                        0]{lang="EN-US"}

[   DHCPINFORM:                         0]{lang="EN-US"}

[   DHCPRELEASE:                        0]{lang="EN-US"}

[   DHCPDECLINE:                        0]{lang="EN-US"}

[   BOOTPREQUEST:                       0]{lang="EN-US"}

[DHCP packets received from servers:    0]{lang="EN-US"}

[   DHCPOFFER:                          0]{lang="EN-US"}

[   DHCPACK:                            0]{lang="EN-US"}

[   DHCPNAK:                            0]{lang="EN-US"}

[   BOOTPREPLY:                         0]{lang="EN-US"}

[DHCP packets relayed to servers:       0]{lang="EN-US"}

[   DHCPDISCOVER:                       0]{lang="EN-US"}

[   DHCPREQUEST:                        0]{lang="EN-US"}

[   DHCPINFORM:                         0]{lang="EN-US"}

[   DHCPRELEASE:                        0]{lang="EN-US"}

[   DHCPDECLINE:                        0]{lang="EN-US"}

[   BOOTPREQUEST:                       0]{lang="EN-US"}

[DHCP packets relayed to clients:       0]{lang="EN-US"}

[   DHCPOFFER:                          0]{lang="EN-US"}

[   DHCPACK:                            0]{lang="EN-US"}

[   DHCPNAK:                            0]{lang="EN-US"}

[   BOOTPREPLY:                         0]{lang="EN-US"}

[DHCP packets sent to servers:          0]{lang="EN-US"}

[   DHCPDISCOVER:                       0]{lang="EN-US"}

[   DHCPREQUEST:                        0]{lang="EN-US"}

[   DHCPINFORM:                         0]{lang="EN-US"}

[   DHCPRELEASE:                        0]{lang="EN-US"}

[   DHCPDECLINE:                        0]{lang="EN-US"}

[   BOOTPREQUEST:                       0]{lang="EN-US"}

[DHCP packets sent to clients:          0]{lang="EN-US"}

[   DHCPOFFER:                          0]{lang="EN-US"}

[   DHCPACK:                            0]{lang="EN-US"}

[   DHCPNAK:                            0]{lang="EN-US"}

[   BOOTPREPLY:                         0]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display dhcp relay statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_x1564844477}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1472595691}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x194516720}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1074000070}

[[DHCP packets dropped]{lang="EN-US"}]{#struct_0_x1331_x1769_x1104014546}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2064112832}[中继丢掉的报文数]{style="font-family:宋体"}

[[DHCP packets received from clients]{lang="EN-US"}]{#struct_0_x1331_x1769_x1225314275}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617605866}[中继从客户端接收的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[DHCP packets received from servers]{lang="EN-US"}]{#struct_0_x1331_x1769_x1251397455}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1297046113}[中继从服务器接收的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[DHCP packets relayed to servers]{lang="EN-US"}]{#struct_0_x1331_x1769_x722058782}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1101505859}[中继转发给服务器的报文数]{style="font-family:宋体"}

[[DHCP packets relayed to clients]{lang="EN-US"}]{#struct_0_x1331_x1769_x741512629}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617802474}[中继转发给客户端的报文数]{style="font-family:宋体"}

[[DHCP packets sent to servers]{lang="EN-US"}]{#struct_0_x1331_x1769_x10098199}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1532467605}[中继主动发送给服务器的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文数，用于实现动态用户地址表项的定时刷新]{style="font-family:宋体"}

[[DHCP packets sent to clients]{lang="EN-US"}]{#struct_0_x1331_x1769_x296536513}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x347992259}[中继主动发送给客户端的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文数（目前设备作为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继时，不会主动发送]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文给客户端）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617736938}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset dhcp relay statistics]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2022065166}

::: {#136323784 .myid}
[]{#_Toc404786472}[]{#struct_0_x1331_x1769_2067590784}

**DHCP \-- DHCP中继配置命令 \-- gateway-list**

------------------------------------------------------------------------

[[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_984631142}[命令用来指定匹配该地址池的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端所在的网段的地址。]{style="font-family:宋体"}

[[[undo gateway-list]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x607398242}[命令用来删除指定的匹配该地址池的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端所在的网段的地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_570201588}

[[[gateway-list]{lang="EN-US"}]{.commandkeywordsChar}*[ ip-address]{lang="EN-US"}*[&\<1-8\> \[ **export-route** \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1690805772}

[[[undo gateway-list]{lang="EN-US"}]{.commandkeywordsChar}[ \[ *ip-address*&\<1-8\> \] \[ **export-route** \]]{lang="EN-US"}]{#struct_0_x1331_x1769_327868568}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x400520560}

[[未指定匹配该地址池的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_738718021}[客户端所在的网段地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1454154290}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2067656320}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_951649069}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x2103958975}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1452784808}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_150851264}

[*[ip-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_x1954399732}[：该地址池的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端所在的网段的地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间用空格分隔。]{style="font-family:宋体"}

[**[export-route]{lang="EN-US"}**]{#struct_0_x1331_x1769_x144620883}[：将网关列表信息下发给地址管理，通过应答客户端的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求，即可实现对不同类型的业务流量的引导。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1985810840}

[[一台]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2086696558}[中继的一个接口下可能连接不同类型的用户，当]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继转发]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端请求报文给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器时，不能再以中继接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为选择地址池的依据。为了解决这个问题，需要使用]{style="font-family:宋体"}**[gateway-list]{lang="EN-US"}**[命令指定某个类型用户所在的网段，并将该地址添加到转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的报文字段中，为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器选择地址池提供依据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1530506130}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1686977611}[指定匹配该地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端所在的网段的地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2068508288}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] gateway-list 10.1.1.1]{lang="EN-US"}
:::

::: {#1631374782 .myid}
[]{#_Toc404786473}[]{#struct_0_x1331_x1769_x730094962}

**DHCP \-- DHCP中继配置命令 \-- remote-server**

------------------------------------------------------------------------

[**[remote-server]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1667297472}[命令用来指定中继地址池对应的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[**[undo remote-server]{lang="EN-US"}**]{#struct_0_x1331_x1769_680793992}[命令用来删除为中继地址池指定的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x480829315}

[**[remote-server]{lang="EN-US"}**[ *ip-address*&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_1752634672}

[**[undo remote-server ]{lang="EN-US"}**[\[ *ip-address*&\<1-8\> \]]{lang="EN-US"}]{#struct_0_x1331_x1769_1400132189}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_339163789}

[[未指定中继地址池的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_639157503}[服务器的地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x955017167}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_2068573824}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1119790397}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_754517181}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_921411274}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1586415140}

[*[ip-address]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x1331_x1769_632546208}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个不同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，每个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之间需要用空格分隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1303248661}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_901105926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo remote-server]{lang="EN-US"}**]{#struct_0_x1331_x1769_x457420048}[命令时，如果没有指定任何参数，则删除所有配置]{lang="EN-US" style="font-family:
宋体"}[DHCP]{lang="EN-US"}[服务器地址。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1491923597}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1106704830}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池]{style="font-family:宋体"}[0]{lang="EN-US"}[为中继配置的服务器地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2067984003}

[\[Sysname\] dhcp server ip-pool 0]{lang="EN-US"}

[\[Sysname-dhcp-pool-0\] remote-server 10.1.1.1]{lang="EN-US"}
:::

::: {#1122937682 .myid}
[]{#_Toc137350332}[]{#_Toc404786474}[]{#struct_0_x1331_x1769_859173444}[]{#_Toc269455738}[]{#_Toc266880459}[]{#_Toc257789549}[]{#_Toc379616803}[]{#_Toc379720593}[]{#_Toc379967989}[]{#_Toc379993775}[]{#_Toc263673868}[]{#_Toc263700747}[]{#_Toc263946499}[]{#_Toc263953506}[]{#_Toc264019802}[]{#_Toc264020138}[]{#_Toc265140316}[]{#_Toc266880423}[]{#_Toc263673869}[]{#_Toc263700748}[]{#_Toc263946500}[]{#_Toc263953507}[]{#_Toc264019803}[]{#_Toc264020139}[]{#_Toc265140317}[]{#_Toc266880424}[]{#_Toc263673883}[]{#_Toc263700762}[]{#_Toc263946514}[]{#_Toc263953521}[]{#_Toc264019817}[]{#_Toc264020153}[]{#_Toc265140331}[]{#_Toc266880438}[]{#_Toc263673884}[]{#_Toc263700763}[]{#_Toc263946515}[]{#_Toc263953522}[]{#_Toc264019818}[]{#_Toc264020154}[]{#_Toc265140332}[]{#_Toc266880439}[]{#_Toc263673903}[]{#_Toc263700782}[]{#_Toc263946534}[]{#_Toc263953541}[]{#_Toc264019837}[]{#_Toc264020173}[]{#_Toc265140351}[]{#_Toc266880458}

**DHCP \-- DHCP中继配置命令 \-- reset dhcp relay client-information**

------------------------------------------------------------------------

[[[reset dhcp relay client-information]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_866469018}[命令用来清除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的用户地址表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1035300138}

[[[reset dhcp relay client-information ]{lang="EN-US"}]{.commandkeywordsChar}[\[ [interface]{.commandkeywordsChar} *interface-type interface-number*[ ]{.commandkeywordsChar}\| [ip]{.commandkeywordsChar} *ip-address*[ ]{.commandkeywordsChar}\[ [vpn-instance]{.commandkeywordsChar} *vpn-instance-name* \] \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x543419071}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1769854265}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x2097726810}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617409258}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x836828450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1403418646}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1195846763}

[[[interface]{lang="EN-US"}]{.commandkeywordsChar}[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_56840803}[：清除指定接口上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的用户地址表项信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[[[ip]{lang="EN-US"}]{.commandkeywordsChar}[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_x210278607}[：清除指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的用户地址表项信息。]{style="font-family:宋体"}

[[[vpn-instance]{lang="EN-US"}]{.commandkeywordsChar}[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1331_x1769_x180914477}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的用户地址表项信息。]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示清除公网的用户地址表项信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x941090890}

[[执行本命令时，如果没有指定任何参数，则清除所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1550446495}[中继的用户地址表项信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617343722}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1155959672}[清除所有]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的用户地址表项信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp relay client-information]{lang="EN-US"}]{#struct_0_x1331_x1769_1175286055}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_197783790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp relay client-information]{lang="EN-US"}**]{#struct_0_x1331_x1769_1740077830}
:::

::: {#938601904 .myid}
[]{#_Toc404786475}[]{#struct_0_x1331_x1769_240778449}[]{#_Toc269455739}[]{#_Toc266880460}[]{#_Toc202081908}

**DHCP \-- DHCP中继配置命令 \-- reset dhcp relay statistics**

------------------------------------------------------------------------

[[[reset dhcp relay statistics]{lang="EN-US"}]{.commandkeywordsChar}]{#struct_0_x1331_x1769_x1998067283}[命令用来清除]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的相关报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x239861565}

[[[reset dhcp relay statistics ]{lang="EN-US"}]{.commandkeywordsChar}[\[[ interface]{.commandkeywordsChar} *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x617540330}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x794701186}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1475038796}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1444934939}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x831411570}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_224751101}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1232557038}

[[[interface]{lang="EN-US"}]{.commandkeywordsChar}*[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1572773810}[：清除指定接口的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继相关报文统计信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果不指定本参数，则清除所有的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继相关报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1752180590}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x617474794}[清除所有的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继相关报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp relay statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_768255249}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x71470039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp relay statistics]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1685728570}
:::

::: {#-2108508026 .myid}
[]{#_Toc315706877}[]{#_Toc314080187}[]{#_Toc304314106}[]{#_Toc297218983}[]{#_Toc202081912}[]{#_Toc404786477}[]{#struct_0_x1331_x1769_x1799219102}[]{#_Toc315706879}[]{#_Toc314080189}

**DHCP \-- DHCP客户端配置命令 \-- dhcp client dad enable**

------------------------------------------------------------------------

[**[dhcp client dad enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_1814694213}[命令用来启用地址冲突检查功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp client dad enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_x538323122}[命令用来关闭地址冲突检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617147114}

[**[dhcp client dad enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1978186061}

[**[undo dhcp client dad enable]{lang="EN-US"}**]{#struct_0_x1331_x1769_839378562}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x324349950}

[[接口上地址冲突检查功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1036641681}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1098730024}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_413096014}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1697382709}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x674841796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x617081578}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_356277532}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1868272245}[客户端通过发送和接收]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文，对]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行地址冲突检测，如果攻击者仿冒地址拥有者进行]{style="font-family:宋体"}[ARP]{lang="EN-US"}[应答，就可以欺骗]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端，导致]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端无法正常使用分配到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。在网络中存在上述攻击者时，建议在客户端上关闭地址冲突检查功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1280195912}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x879575461}[关闭地址冲突检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1419993139}

[\[Sysname\] undo dhcp client dad enable]{lang="EN-US"}
:::

::: {#-1913654566 .myid}
[]{#_Toc404786478}[]{#struct_0_x1331_x1769_704357932}[]{#_Toc337719088}

**DHCP \-- DHCP客户端配置命令 \-- dhcp client dscp**

------------------------------------------------------------------------

[**[dhcp client dscp]{lang="EN-US"}**]{#struct_0_x1331_x1769_291848994}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发送]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo dhcp client dscp]{lang="EN-US"}**]{#struct_0_x1331_x1769_x617671405}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1565172157}

[**[dhcp client dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1743998113}

[**[undo dhcp client dscp]{lang="EN-US"}**]{#struct_0_x1331_x1769_x710650868}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1422273824}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x754915390}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1281862637}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1100123445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_50310964}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617605869}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1250807631}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x35744359}

[[DSCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1265855297}[优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。通过本命令可以指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1057018561}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x967849489}[配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2081550739}

[\[Sysname\] dhcp client dscp 30]{lang="EN-US"}
:::

::: {#-614252327 .myid}
[]{#_Toc404786479}[]{#struct_0_x1331_x1769_60648209}

**DHCP \-- DHCP客户端配置命令 \-- dhcp client identifier**

------------------------------------------------------------------------

[**[dhcp client identifier]{lang="EN-US"}**]{#struct_0_x1331_x1769_x617802477}[命令用来配置接口使用指定的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dhcp client identifier]{lang="EN-US"}**]{#struct_0_x1331_x1769_x10032663}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x738272710}

[**[dhcp client]{lang="EN-US"}**[ **identifier** { **ascii** *string* \| **hex** *string* *\|* **mac** *interface-type* *interface-number* }]{lang="EN-US"}]{#struct_0_x1331_x1769_x718157017}

[**[undo dhcp client]{lang="EN-US"}**[ **identifier**]{lang="EN-US"}]{#struct_0_x1331_x1769_x57522509}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_333733798}

[[根据本接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1331_x1769_1295363695}[地址生成]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[。如果本接口没有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，则获取设备第一个以太接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址生成]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1740241656}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x174475081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617736941}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x2021475335}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x783146041}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x718197352}

[**[ascii ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1331_x1769_1922975407}[：使用指定的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[字符串作为该接口的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[hex ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1331_x1769_x636365592}[：使用指定的十六进制字符串作为该接口的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1087005887}[：使用指定接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x574275347}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617409261}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[用来填充]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}[Option 61]{lang="EN-US"}[，作为识别]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的唯一标识。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器可以根据客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[为特定的客户端分配特定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。用户可以通过以下三种方法指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[：]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[字符串、十六进制字符串或使用指定接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[，以上三种方式都需要由用户保证不同客户端的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[不会相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x837418273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x1755543696}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x695214724}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使用的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[为接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1040775148}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp client identifier mac gigabitethernet 1/0/2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_1617356200}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x617343725}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] dhcp client identifier hex FFFFFFFF]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1155894136}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dhcp** **client**]{lang="EN-US"}]{#struct_0_x1331_x1769_845397670}[]{#_Toc315706878}
:::

::: {#-2021121891 .myid}
[]{#_Toc404786480}[]{#struct_0_x1331_x1769_x186219489}[]{#_Toc315706876}[]{#_Toc314080186}[]{#_Toc304314105}

**DHCP \-- DHCP客户端配置命令 \-- display dhcp client**

------------------------------------------------------------------------

[**[display dhcp]{lang="EN-US"}**[ ]{lang="EN-US"}**[client]{lang="EN-US"}**]{#struct_0_x1331_x1769_1437733891}[命令用来显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1735035214}

[**[display]{lang="EN-US"}**[ **dhcp** **client** \[ **verbose** \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_770166292}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1151393783}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2021393731}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x617540333}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x794635650}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1116306372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1094468041}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1072547346}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_415898539}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1733113931}[：显示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的详细信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1473544926}[：显示指定接口的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端相关信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x665889612}

[[如果不指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x617474797}[参数，显示所有接口上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_768451857}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_567261321}[显示所有接口的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp client]{lang="EN-US"}]{#struct_0_x1331_x1769_x1433626268}

[Vlan-interface10 DHCP client information:]{lang="EN-US"}

[ Current state: BOUND]{lang="EN-US"}

[ Allocated IP: 40.1.1.20 255.255.255.0]{lang="EN-US"}

[ Allocated lease: 259200 seconds, T1: 129600 seconds, T2: 226800 seconds]{lang="EN-US"}

[ DHCP server: 40.1.1.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1118482302}[显示所有接口的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp client verbose]{lang="EN-US"}]{#struct_0_x1331_x1769_x617147117}

[Vlan-interface10 DHCP client information:]{lang="EN-US"}

[ Current state: BOUND]{lang="EN-US"}

[ Allocated IP: 40.1.1.20 255.255.255.0]{lang="EN-US"}

[ Allocated lease: 259200 seconds, T1: 129600 seconds, T2: 226800 seconds]{lang="EN-US"}

[ Lease from May 21 19:00:29 2012   to   May 31 19:00:29 2012]{lang="EN-US"}

[ DHCP server: 40.1.1.2]{lang="EN-US"}

[ Transaction ID: 0x1c09322d]{lang="EN-US"}

[ Default router: 40.1.1.2]{lang="EN-US"}

[Classless static routes:]{lang="EN-US"}

[   Destination: 1.1.0.1, Mask: 255.0.0.0, NextHop: 192.168.40.16]{lang="EN-US"}

[   Destination: 10.198.122.63, Mask: 255.255.255.255, NextHop: 192.168.40.16]{lang="EN-US"}

[ DNS servers: 44.1.1.11 44.1.1.12]{lang="EN-US"}

[ Domain name: ddd.com]{lang="EN-US"}

[ Boot servers: 200.200.200.200  1.1.1.1]{lang="EN-US"}

[[ ACS parameter:]{lang="EN-US"}]{#struct_0_x1331_x1769_x1899102156}

[   URL: http://192.168.1.1:7547/acs]{lang="EN-US"}

[   Username: bims]{lang="EN-US"}

[   Password: \*\*\*\*\*\*]{lang="EN-US"}

[[ Client ID type: acsii(type value=00)]{lang="EN-US"}]{#struct_0_x1331_x1769_x1978120525}

[[ Client ID value: 000c.29d3.8659-GE1/0/1]{lang="EN-US"}]{#struct_0_x1331_x1769_1158169587}

[[ Client ID (with type) hex: 0030-3030-632e-3239-]{lang="EN-US"}]{#struct_0_x1331_x1769_582964519}

[[                            6433-2e38-3635-392d-]{lang="EN-US"}]{#struct_0_x1331_x1769_x87767608}

[[                            4574-6830-2f30-2f32]{lang="EN-US"}]{#struct_0_x1331_x1769_1180089963}

[[ T1 will timeout in 1 day 11 hours 58 minutes 52 seconds.]{lang="EN-US"}]{#struct_0_x1331_x1769_x617081581}

[]{#struct_0_x1331_x1769_356736277}[[表1-13 ]{lang="EN-US"}[display dhcp client]{lang="EN-US"}]{#_Toc138412532}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1446736309}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1681601563}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1990192068}

[[Vlan-interface10 DHCP client information]{lang="FR"}]{#struct_0_x1331_x1769_x1840550054}

[[作为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_107043978}[客户端的接口信息]{style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_x1331_x1769_x1987241192}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617671404}[客户端状态机的当前状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HALT]{lang="EN-US"}]{#struct_0_x1331_x1769_x1565237693}[：停止申请]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址状态；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INIT]{lang="EN-US"}]{#struct_0_x1331_x1769_x642472520}[：初始化状态；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SELECTING]{lang="EN-US"}]{#struct_0_x1331_x1769_x848418791}[：发送]{lang="EN-US" style="font-family:宋体"}[DHCP-DISCOVER]{lang="EN-US"}[报文寻找]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器后，进入该状态，等待]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的响应报文；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUESTING]{lang="EN-US"}]{#struct_0_x1331_x1769_x1953909203}[：发送]{lang="EN-US" style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[报文请求]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，进入该状态，等待]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的响应报文；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BOUND]{lang="EN-US"}]{#struct_0_x1331_x1769_x617605868}[：接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送的]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[报文，成功获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址后，进入该状态；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RENEWING]{lang="EN-US"}]{#struct_0_x1331_x1769_x1250742095}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时后，进入该状态；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REBOUNDING]{lang="EN-US"}]{#struct_0_x1331_x1769_x1387879613}[：]{lang="EN-US" style="font-family:宋体"}[T2]{lang="EN-US"}[定时器超时后，进入该状态。]{lang="EN-US" style="font-family:宋体"}

[[Allocated IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1539425937}

[[DHCP]{lang="PT-BR"}]{#struct_0_x1331_x1769_389997903}[服务器为接口分配]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址]{style="font-family:宋体"}

[[Allocated lease]{lang="EN-US"}]{#struct_0_x1331_x1769_x1394133612}

[[租约时长]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x617802476}

[[T1]{lang="EN-US"}]{#struct_0_x1331_x1769_x9967127}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1750294069}[客户端的一半左右租约时间（以秒为单位）]{style="font-family:宋体"}

[[T2]{lang="EN-US"}]{#struct_0_x1331_x1769_1535595240}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_901762412}[客户端的]{style="font-family:宋体"}[7/8]{lang="EN-US"}[租约时间（以秒为单位）]{style="font-family:宋体"}

[[Lease from....to....]{lang="EN-US"}]{#struct_0_x1331_x1769_x617736940}

[[租约起止时间]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x2021540871}

[[DHCP server]{lang="EN-US"}]{#struct_0_x1331_x1769_923289945}

[[选择的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1740596203}[服务器的地址]{style="font-family:宋体"}

[[Transaction ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x617409260}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x837352737}[客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程]{style="font-family:宋体"}

[[Default router]{lang="EN-US"}]{#struct_0_x1331_x1769_234277739}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_765653030}[客户端指定的网关地址]{style="font-family:宋体"}

[[Classless static routes]{lang="EN-US"}]{#struct_0_x1331_x1769_x1001649401}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617343724}[客户端指定的无分类静态路由]{style="font-family:宋体"}

[[Static routes]{lang="EN-US"}]{#struct_0_x1331_x1769_x1155828600}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_66194358}[客户端指定的有分类静态路由]{style="font-family:宋体"}

[[DNS servers]{lang="EN-US"}]{#struct_0_x1331_x1769_x640200112}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617540332}[客户端指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}

[[Domain name]{lang="EN-US"}]{#struct_0_x1331_x1769_x794570114}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1236477444}[客户端指定的域名后缀]{style="font-family:宋体"}

[[Boot servers]{lang="EN-US"}]{#struct_0_x1331_x1769_x1996310846}

[[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617474796}[客户端指定的]{style="font-family:宋体"}[PXE]{lang="EN-US"}[引导服务器地址，通过]{style="font-family:宋体"}[Option 43]{lang="EN-US"}[获取，最多可以获取]{style="font-family:宋体"}[16]{lang="EN-US"}[个地址]{style="font-family:宋体"}

[[ACS parameter]{lang="EN-US"}]{#struct_0_x1331_x1769_x1899888589}

[[ACS]{lang="EN-US"}]{#struct_0_x1331_x1769_x1899823053}[参数]{style="font-family:宋体"}

[[URL]{lang="EN-US"}]{#struct_0_x1331_x1769_1923198937}

[[ACS]{lang="EN-US"}]{#struct_0_x1331_x1769_x1900019661}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_x1331_x1769_x2135391846}

[[登录]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_x1331_x1769_x1899954125}[设备使用的用户名]{style="font-family:宋体"}

[[Password]{lang="EN-US"}]{#struct_0_x1331_x1769_x1899102157}

[[登录]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_x1331_x1769_1517797328}[设备使用的密码，若存在密码，则显示为"]{style="font-family:宋体"}[\*\*\*\*\*\*]{lang="EN-US"}["；若不存在密码，则不显示此项；]{style="font-family:宋体"}

[[Client ID type]{lang="EN-US"}]{#struct_0_x1331_x1769_768386321}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x469046695}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[的类型，]{style="font-family:宋体"}[type value]{lang="EN-US"}[表示类型值。类型为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[时，]{style="font-family:宋体"}[type value]{lang="EN-US"}[为]{style="font-family:宋体"}[00]{lang="EN-US"}[；为]{style="font-family:宋体"}[MAC address]{lang="EN-US"}[时，]{style="font-family:宋体"}[type value]{lang="EN-US"}[为]{style="font-family:宋体"}[01]{lang="EN-US"}[；为]{style="font-family:宋体"}[Hex]{lang="EN-US"}[时，]{style="font-family:宋体"}[type value]{lang="EN-US"}[为配置的十六进制数的前两位]{style="font-family:宋体"}

[[Client ID value]{lang="EN-US"}]{#struct_0_x1331_x1769_x672539655}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x617147116}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[的取值]{style="font-family:宋体"}

[[Client ID (with type) hex]{lang="EN-US"}]{#struct_0_x1331_x1769_x1978054989}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_563483200}[客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[的十六进制形式（带类型值字段）]{style="font-family:宋体"}

[[T1 will timeout in 1 day 11 hours 58 minutes 52 seconds.]{lang="EN-US"}]{#struct_0_x1331_x1769_x617081580}

[[在多少时间后]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_x1331_x1769_356801813}[定时器（即一半左右租约时间）将到期]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1490855536}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp client]{lang="EN-US"}**[ **identifier**]{lang="EN-US"}]{#struct_0_x1331_x1769_x90524297}

[]{#struct_0_x1331_x1769_318441347}[]{#_Toc314080188}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip address dhcp-alloc]{lang="EN-US"}**]{#_Toc304314107}

::: {#-198141140 .myid}
[]{#_Toc404786481}[]{#struct_0_x1331_x1769_365034202}

**DHCP \-- DHCP客户端配置命令 \-- ip address dhcp-alloc**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **address** **dhcp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1391643911}[命令用来配置接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **address** **dhcp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_1233390089}[命令用来取消接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761600730}

[**[ip]{lang="EN-US"}**[ **address** **dhcp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_327570312}

[**[undo]{lang="EN-US"}**[ **ip** **address** **dhcp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_1475453249}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x231954150}

[[接口不通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_737480841}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_499873712}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1482733736}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761535194}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1459001910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1444368267}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x990838598}

[[取消接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_528056792}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端会发送]{style="font-family:宋体"}[DHCP-RELEASE]{lang="EN-US"}[报文通知]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器释放租约。如果此时该接口处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，则无法保证报文成功发送。]{style="font-family:宋体"}

[[如果配置子接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x2030386014}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，在其主接口上执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令时，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端不会发送请求释放子接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约的]{style="font-family:宋体"}[DHCP-RELEASE]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_609946395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_781049048}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_511896243}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1761469658}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip address dhcp-alloc]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_724116231}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_699547900}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[上配置接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1829511473}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ip address dhcp-alloc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x471095341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dhcp** **client**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1968808088}
:::

::: {#-893657776 .myid}
[]{#_Toc69790780}[]{#_Toc25750199}[]{#_Toc137350340}[]{#_Toc135535513}[]{#_Toc108607385}[]{#_Toc154285766}[]{#_Toc202081916}[]{#_Toc404786483}[]{#struct_0_x1331_x1769_749667114}[]{#_Toc318132889}[]{#_Toc320718273}[]{#_Toc321058450}[]{#_Toc320718274}[]{#_Toc321058451}[]{#_Toc320718275}[]{#_Toc321058452}[]{#_Toc320718276}[]{#_Toc321058453}[]{#_Toc320718277}[]{#_Toc321058454}[]{#_Toc320718278}[]{#_Toc321058455}[]{#_Toc320718279}[]{#_Toc321058456}[]{#_Toc320718280}[]{#_Toc321058457}[]{#_Toc320718281}[]{#_Toc321058458}[]{#_Toc320718282}[]{#_Toc321058459}[]{#_Toc320718283}[]{#_Toc321058460}[]{#_Toc320718284}[]{#_Toc321058461}[]{#_Toc320718285}[]{#_Toc321058462}[]{#_Toc320718286}[]{#_Toc321058463}[]{#_Toc320718287}[]{#_Toc321058464}[]{#_Toc320718288}[]{#_Toc321058465}[]{#_Toc320718289}[]{#_Toc321058466}[]{#_Toc320718290}[]{#_Toc321058467}[]{#_Toc320718291}[]{#_Toc321058468}[]{#_Toc295916599}[]{#_Toc296072710}[]{#_Toc296072748}[]{#_Toc295916600}[]{#_Toc296072711}[]{#_Toc296072749}[]{#_Toc320718292}[]{#_Toc321058469}[]{#_Toc320718293}[]{#_Toc321058470}[]{#_Toc320718294}[]{#_Toc321058471}[]{#_Toc320718295}[]{#_Toc321058472}[]{#_Toc320718296}[]{#_Toc321058473}[]{#_Toc320718297}[]{#_Toc321058474}[]{#_Toc320718298}[]{#_Toc321058475}[]{#_Toc320718299}[]{#_Toc321058476}[]{#_Toc320718300}[]{#_Toc321058477}[]{#_Toc320718301}[]{#_Toc321058478}[]{#_Toc320718302}[]{#_Toc321058479}[]{#_Toc320718303}[]{#_Toc321058480}[]{#_Toc320718304}[]{#_Toc321058481}[]{#_Toc320718305}[]{#_Toc321058482}[]{#_Toc320718306}[]{#_Toc321058483}[]{#_Toc320718307}[]{#_Toc321058484}[]{#_Toc320718308}[]{#_Toc321058485}[]{#_Toc320718309}[]{#_Toc321058486}[]{#_Toc320718310}[]{#_Toc321058487}[]{#_Toc320718311}[]{#_Toc321058488}[]{#_Toc295916602}[]{#_Toc296072713}[]{#_Toc296072751}[]{#_Toc295916603}[]{#_Toc296072714}[]{#_Toc296072752}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding database filename**

------------------------------------------------------------------------

[**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_x1331_x1769_x851261086}[命令用来指定存储]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项的文件名称。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1266582204}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1040126328}

[**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename** { *filename \|* **url** *url* \[ **username** *username* \[ **password** { **cipher** \| **simple** } *key* \] \] }]{lang="EN-US"}]{#struct_0_x1331_x1769_477180562}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_x1331_x1769_x731218834}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761338586}

[[未指定存储文件名称。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x421286130}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_440670077}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x840036531}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1767986377}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_341577291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1060115345}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1321179832}

[*[filename]{lang="EN-US"}*]{#struct_0_x1331_x1769_1761273050}[：目标文件名，该配置用于本地存储模式。文件名取值范围的详细介绍，请参见"基础配置指导"中的"文件系统管理"。]{style="font-family:宋体"}

[**[url]{lang="EN-US"}***[ url]{lang="EN-US"}*]{#struct_0_x1331_x1769_x1666928157}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[，该配置用于远程文件系统模式。此参数中不能包含用户名和密码，和参数]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和]{style="font-family:宋体"}*[password]{lang="EN-US"}*[配合使用。远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[是否支持大小写和是否支持路径格式遵循远程服务器端规格。]{style="font-family:宋体"}

[**[username]{lang="EN-US"}***[ username]{lang="EN-US"}*]{#struct_0_x1331_x1769_913770624}[：配置远程目标文件]{style="font-family:宋体"}[URL]{lang="EN-US"}[时的用户名。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1331_x1769_305482128}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1331_x1769_1905698436}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_x1331_x1769_1761141978}[：设置的明文密码或密文密码，区分大小写。明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1901316172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x649458366}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[存储]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x946227669}[DHCP Snooping]{lang="EN-US"}[表项时，如果设备中还不存在对应名称的文件，则设备会自动创建该文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令后，会立即触发一次表项备份。之后，如果未配置]{style="font-family:宋体"}]{#struct_0_x1331_x1769_371313055}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}[命令，若表项发生变化，默认在]{style="font-family:宋体"}[300]{lang="EN-US"}[秒之后刷新存储文件；若表项未发生变化，则不再刷新存储文件。如果配置了]{style="font-family:宋体"}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}[命令，若表项发生变化，则到达刷新时间间隔后刷新存储文件；若表项未发生变化，则不再刷新存储文件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_x1331_x1769_x411304834}[不支持远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[，配置远程目标文件]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[请使用]{lang="EN-US" style="font-family:宋体"}*[url]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[username]{lang="EN-US"}*[、]{lang="EN-US" style="font-family:宋体"}*[key]{lang="EN-US"}*[配合使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[频繁擦写本地存储介质可能会影响存储介质寿命，建议使用远程文件系统模式存储]{style="font-family:宋体"}]{#struct_0_x1331_x1769_940027061}[DHCP Snooping]{lang="EN-US"}[表项文件。]{style="font-family:宋体"}

[[当进行远程存储时，支持]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_x1331_x1769_2053022891}[和]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1762125018}[FTP]{lang="EN-US"}[或]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[协议时，服务器地址支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[形式或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[形式，并且支持]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名方式。服务器地址为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址形式时需使用方括号]{style="font-family:宋体"}[(]{lang="EN-US"}["]{style="font-family:宋体"}[\[]{lang="EN-US"}["和"]{style="font-family:
宋体"}[\]]{lang="EN-US"}["]{style="font-family:宋体"}[)]{lang="EN-US"}[引用。配置服务器地址为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名格式时请勿使用方括号引用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1006921038}[FTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}[ftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径"的形式，如有用户名和密码请分别使用参数]{style="font-family:宋体"}*[username]{lang="EN-US"}*[和参数]{style="font-family:宋体"}*[key]{lang="EN-US"}*[进行配置，用户名和密码必须和服务器上的配置一致，如果服务器只对用户名进行认证，则不用输入密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当采用]{style="font-family:宋体"}]{#struct_0_x1331_x1769_100086711}[TFTP]{lang="EN-US"}[协议时，]{style="font-family:宋体"}[URL]{lang="EN-US"}[采用"]{style="font-family:宋体"}[tftp://]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}[\[:]{lang="EN-US"}[端口号]{style="font-family:宋体"}[\]/]{lang="EN-US"}[文件路径"的形式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1373798578}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1341485099}[配置存储]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项的文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_725010636}

[\[Sysname\] dhcp snooping binding database filename database.dhcp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1484107832}[配置远程存储]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项至]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[ftp]{lang="EN-US"}[服务器工作目录下]{style="font-family:宋体"}[,]{lang="EN-US"}[用户名为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[，文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1762059482}

[\[Sysname\] dhcp snooping binding database filename url ftp://10.1.1.1/database.dhcp username 1 password simple 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x167697530}[配置远程存储]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项至]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[tftp]{lang="EN-US"}[服务器工作目录下，文件名为]{style="font-family:宋体"}[database.dhcp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1219538496}

[\[Sysname\] dhcp snooping binding database filename tftp://10.1.1.1/database.dhcp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x654584431}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1283383298}
:::

::: {#-1993367251 .myid}
[]{#_Toc404786484}[]{#struct_0_x1331_x1769_835209194}[]{#_Toc318132890}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding database update interval**

------------------------------------------------------------------------

[**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1833055741}[命令用来配置刷新]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项存储文件的延迟时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_x1331_x1769_x20119741}[命令用来恢复缺省情况]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761600731}

[**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **interval** *seconds*]{lang="EN-US"}]{#struct_0_x1331_x1769_327635848}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database** **update** **interval**]{lang="EN-US"}]{#struct_0_x1331_x1769_970950484}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_558830550}

[[若]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_950316439}[表项不变化，则不刷新存储文件；若]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项发生变化，默认在]{style="font-family:宋体"}[300]{lang="EN-US"}[秒之后刷新存储文件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x374467515}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x332904059}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1934618487}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1474926926}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1761535195}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1458936374}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1331_x1769_x228890549}[：刷新延迟时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[864000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1986134488}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令后，当]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1899973047}[DHCP Snooping]{lang="EN-US"}[表项发生变化后，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[设备开始计时，当本命令配置的延迟时间到达后，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[会把这个时间段内表项所有的变化信息备份到固化文件中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_2097084857}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}[命令指定存储表项的文件，则本命令不会生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_147857053}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1690160029}[若]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项发生变化，在]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟后刷新表项存储文件。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1761469659}

[\[Sysname\] dhcp snooping binding database update interval 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_724181767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1611668398}
:::

::: {#-1072034692 .myid}
[]{#_Toc404786485}[]{#struct_0_x1331_x1769_x1903535861}[]{#_Toc318132891}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding database update now**

------------------------------------------------------------------------

[**[dhcp]{lang="EN-US"}**]{#struct_0_x1331_x1769_1891070513}[ **snooping** **binding** **database** **update** **now**]{lang="EN-US"}[命令用来将当前的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项保存到用户指定的文件中。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1484282028}

[**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **update** **now**]{lang="EN-US"}]{#struct_0_x1331_x1769_1071943292}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x496981884}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1761404123}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1259264587}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1208208201}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_687065348}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1927116049}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只用来触发一次]{lang="EN-US" style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1374477771}[表项的备份。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x721978489}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}[命令]{lang="EN-US" style="font-family:宋体"}[指定存储表项的文件，则本命令不会生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1108040036}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_298168532}[将当前的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项保存到文件中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1761338587}

[\[Sysname\] dhcp snooping binding database update now]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x421351666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **database** **filename**]{lang="EN-US"}]{#struct_0_x1331_x1769_2023781784}
:::

::: {#1880449383 .myid}
[]{#_Toc404786486}[]{#struct_0_x1331_x1769_979540947}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping binding record**

------------------------------------------------------------------------

[**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_x1331_x1769_1670732892}[命令用来启用端口的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项记录功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_x1331_x1769_x880796190}[命令用来关闭端口的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项记录功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1734356556}

[**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1993987062}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[dhcp]{lang="EN-US"}**[ **snooping** **binding** **record**]{lang="EN-US"}]{#struct_0_x1331_x1769_1761273051}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1666993693}

[[端口]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x1539988718}[表项记录功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1150131254}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_x194488502}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2073198925}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1014530891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x241564533}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761207515}

[[用户可在]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1867351115}[设备直接与客户端连接的端口上启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项记录功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x298967559}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_280468258}[启用端口的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1848430995}

[\[Sysname\]interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping binding record]{lang="EN-US"}
:::

::: {#-463537277 .myid}
[]{#_Toc404786487}[]{#struct_0_x1331_x1769_463900986}[]{#_Toc318132892}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping check mac-address**

------------------------------------------------------------------------

[**[dhcp]{lang="EN-US"}**[ **snooping** **check** **mac-address**]{lang="EN-US"}]{#struct_0_x1331_x1769_1386950738}[命令用来启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **check** **mac-address**]{lang="EN-US"}]{#struct_0_x1331_x1769_1761141979}[命令用来关闭]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1901381708}

[**[dhcp]{lang="EN-US"}**[ **snooping** **check** **mac-address**]{lang="EN-US"}]{#struct_0_x1331_x1769_548903080}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **check** **mac-address**]{lang="EN-US"}]{#struct_0_x1331_x1769_1137796718}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1477127045}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1968274419}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1854809721}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_1573147720}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x720077840}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1762125019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1006855502}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_984613961}

[[启用该功能后，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_126843699}[检查接收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求报文中的]{style="font-family:宋体"}[chaddr]{lang="EN-US"}[字段和数据帧的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址字段是否一致。如果一致，则认为该报文合法，将其转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器；如果不一致，则丢弃该报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1363931407}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_295483054}[启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x171239540}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping check mac-address]{lang="EN-US"}
:::

::: {#1892835444 .myid}
[]{#_Toc404786488}[]{#struct_0_x1331_x1769_1762059483}[]{#_Toc318132893}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping check request-message**

------------------------------------------------------------------------

[**[dhcp snooping check request-message]{lang="EN-US"}**]{#struct_0_x1331_x1769_x167763066}[命令用来启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求方向报文检查功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **check** **request-message**]{lang="EN-US"}]{#struct_0_x1331_x1769_x422084810}[命令用来关闭]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求方向报文检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x429052409}

[**[dhcp]{lang="EN-US"}**[ **snooping** **check** **request-message**]{lang="EN-US"}]{#struct_0_x1331_x1769_1476454826}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **check** **request-message**]{lang="EN-US"}]{#struct_0_x1331_x1769_1232144113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_605700753}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1047385938}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求方向报文检查功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_54453803}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_1761600728}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_328094599}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x871910183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1141112084}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1120006916}

[[本功能用来检查]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1390916951}[续约报文、]{style="font-family:宋体"}[DHCP-DECLINE]{lang="EN-US"}[和]{style="font-family:宋体"}[DHCP-RELEASE]{lang="EN-US"}[三种]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求方向的报文，以防止非法客户端伪造这三种报文对]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器进行攻击。]{style="font-family:宋体"}

[[如果启用了该功能，则]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x1415553247}[设备接收到上述报文后，检查本地是否存在与接收报文匹配的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。若存在，则接收报文信息与]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项信息一致时，认为该报文为合法的请求方向报文，将其转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器；不一致时，认为该报文为伪造的请求方向报文，将其丢弃。若不存在，则认为该报文合法，将其转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_632521638}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1761535192}[启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求方向报文检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1458870838}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping check request-message]{lang="EN-US"}
:::

::: {#1881117303 .myid}
[]{#_Toc404786489}[]{#struct_0_x1331_x1769_x1454038006}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping enable**

------------------------------------------------------------------------

[**[dhcp]{lang="EN-US"}**[ **snooping** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_450956033}[命令用来启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_x801763572}[命令用来关闭]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x813990679}

[**[dhcp]{lang="EN-US"}**[ **snooping** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1583688963}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_885279135}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761469656}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_724247303}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_575714510}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1966748442}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x553042419}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_360450159}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1095995486}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_679261535}

[[启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1761404120}[功能后，如果不信任端口接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送的报文，将丢弃该报文，以保证客户端从合法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。此时，设备不会记录]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x1259461195}[功能关闭后，所有端口都可转发]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的响应报文，并且不记录]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1266371453}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1325130526}[启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x1445514305}

[\[Sysname\] dhcp snooping enable]{lang="EN-US"}
:::

::::: {#691384378 .myid}
[]{#_Toc404786490}[]{#struct_0_x1331_x1769_1576677793}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information circuit-id**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DHCP命令.files/image001.png){#图片 1 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1331_x1769_176258004}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本特性的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1331_x1769_x1748479196}
:::

[ ]{lang="EN-US"}

[**[dhcp]{lang="EN-US"}**[ **snooping** **information** **circuit-id**]{lang="EN-US"}]{#struct_0_x1331_x1769_1761338584}[命令用来配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充模式和填充格式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **circuit-id**]{lang="EN-US"}]{#struct_0_x1331_x1769_x421417202}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1617267901}

[**[dhcp snooping information circuit-id ]{lang="EN-US"}**[{ \[ **vlan** *vlan-id* \] **string** *circuit-id* \| { **normal** \| **verbose** \[ **node-identifier** { **mac** \| **sysname** \| **user-defined** *node-identifier* } \] } \[ **format** { **ascii** \| **hex** } \] }]{lang="EN-US"}]{#struct_0_x1331_x1769_x444827135}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **circuit-id** \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_714459852}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1642344825}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_365339376}[的]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充模式为]{style="font-family:宋体"}[Normal]{lang="EN-US"}[，填充格式为]{style="font-family:宋体"}[hex]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x753877414}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_x567491888}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761273048}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1667452446}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_543798872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1371822106}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1331_x1769_x618978519}[：为从指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[**[string]{lang="EN-US"}**[ *circuit-id*]{lang="EN-US"}]{#struct_0_x1331_x1769_x622561320}[：指定以用户配置的字符串填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}*[circuit-id]{lang="EN-US"}*[表示用户配置的用来填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的内容，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[normal]{lang="EN-US"}**]{#struct_0_x1331_x1769_179664341}[：指定以]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项，填充内容为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[和端口号。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1331_x1769_339278490}[：指定以]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[**[node-identifier]{lang="EN-US"}**[ { **mac** \| **sysname** \| **user-defined** *node-identifier* }]{lang="EN-US"}]{#struct_0_x1331_x1769_1761207512}[：指定接入节点的标识。缺省情况下，以节点的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为节点标识。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac]{lang="EN-US"}**]{#struct_0_x1331_x1769_1867678795}[：表示以节点的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址作为节点标识。]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充内容为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、以太网类型（取值固定为"]{style="font-family:宋体"}[eth]{lang="EN-US"}["）、框号、槽号、子槽号、接口编号、]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[组成的字符串。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sysname]{lang="EN-US"}**]{#struct_0_x1331_x1769_1138732729}[：表示以节点的设备名称作为节点标识。]{style="font-family:
宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充内容为设备的系统名称、以太网类型（取值固定为"]{style="font-family:宋体"}[eth]{lang="EN-US"}["）、框号、槽号、子槽号、接口编号、]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[组成的字符串。其中，设备的系统名称可以通过系统视图下的]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置。不管配置了哪种填充格式，设备的系统名称始终采用]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-defined]{lang="EN-US"}**[ *node-identifier*]{lang="EN-US"}]{#struct_0_x1331_x1769_x275317262}[：表示以指定的字符串作为节点标识，]{lang="EN-US" style="font-family:宋体"}*[node-identifier]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[50]{lang="EN-US"}[个字符的字符串，区分大小写。]{lang="EN-US" style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的]{style="font-family:宋体"}[填充内容为指定的字符串、以太网类型（取值固定为"]{lang="EN-US" style="font-family:宋体"}[eth]{lang="EN-US"}["）、框号、槽号、子槽号、接口编号、]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[组成的字符串。]{lang="EN-US" style="font-family:宋体"}[不管配置了哪种填充格式，指定的字符串始终采用]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充。]{style="font-family:宋体"}

[**[format]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2066921173}[：指定]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项的填充格式。]{style="font-family:宋体"}

[**[ascii]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1413586614}[：指定以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项，即将数值转换为对应的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码填充到]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[**[hex]{lang="EN-US"}**]{#struct_0_x1331_x1769_x303331320}[：指定以]{style="font-family:宋体"}[十六进制数值的]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_151020958}

[[以用户配置的字符串填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_1761141976}[子选项时，填充格式固定为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式。]{style="font-family:宋体"}

[[以]{style="font-family:宋体"}[Normal]{lang="EN-US"}]{#struct_0_x1331_x1769_1901185100}[和]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项时，填充格式由]{style="font-family:宋体"}[本命令的配置]{style="font-family:宋体"}[决定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1037604142}[本命令中未指定填充格式，则对于]{style="font-family:
宋体"}[Normal]{lang="FR"}[模式，]{style="font-family:
宋体"}[VLAN ID]{lang="FR"}[和端口号均以]{style="font-family:宋体"}[hex]{lang="FR"}[格式填充]{style="font-family:宋体"}[；]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[Verbose]{lang="FR"}[模式，节点标识（]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、设备的系统名称或指定的字符串）]{style="font-family:宋体"}[、]{style="font-family:宋体"}[以太网类型、框号、槽号、子槽号、接口编号均以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充，]{style="font-family:宋体"}[VLAN ID]{lang="FR"}[以]{style="font-family:宋体"}[hex]{lang="FR"}[格式填充。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果本命令中指定填充格式为]{style="font-family:宋体"}]{#struct_0_x1331_x1769_591431661}**[ascii]{lang="EN-US"}**[，则所有内容均以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果本命令中指定填充格式为]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1169105541}**[hex]{lang="EN-US"}**[，则对于]{style="font-family:宋体"}[Normal]{lang="FR"}[模式，]{style="font-family:宋体"}[VLAN ID]{lang="FR"}[和端口号均以]{style="font-family:宋体"}[hex]{lang="FR"}[格式填充]{style="font-family:宋体"}[；]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[Verbose]{lang="FR"}[模式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[设备的节点标识、以太网类型以]{style="font-family:宋体"}[ASCII]{lang="FR"}[码]{style="font-family:宋体"}[格式填充，其余内容均以]{style="font-family:宋体"}[hex]{lang="FR"}[格式填充。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x235034736}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次执行该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1862070460}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果以设备的系统名称（]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1762125016}**[sysname]{lang="EN-US"}**[）作为节点标识填充]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则系统名称中不能包含空格；否则，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[添加或替换]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x350936050}[的]{style="font-family:
宋体"}[Circuit ID]{lang="EN-US"}[子选项信息中无法携带携带接口拆分信息或子接口信息，关于"接口拆分"和"子接口"的详细介绍，请参见"以太网接口配置指导"中的"以太网接口通用配置"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1007314254}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_535821063}[配置以]{style="font-family:宋体"}[Verbose]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Circuit ID]{lang="FR"}[子选项，节点标识为设备的系统名称，填充格式为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_90444876}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information strategy replace]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information circuit-id verbose node-identifier sysname format ascii]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1354699274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_1762059480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **strategy**]{lang="EN-US"}]{#struct_0_x1331_x1769_x167566458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp snooping information]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1590960948}
:::::

::::: {#1532821470 .myid}
[]{#_Toc404786491}[]{#struct_0_x1331_x1769_x1468974941}[]{#_Toc318132894}[]{#_Toc202081918}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DHCP命令.files/image002.png){#图片 2 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1331_x1769_1902558051}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1331_x1769_359647260}
:::

**[ ]{lang="EN-US"}**

[**[dhcp]{lang="EN-US"}**[ **snooping** **information** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_x682268808}[命令用来启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_x24797329}[命令用来禁止]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1512938785}

[**[dhcp]{lang="EN-US"}**[ **snooping** **information** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_1761600729}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_328160135}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x875502640}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x258610278}[支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1067643596}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_974238050}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_107831808}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_955748426}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1761535193}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1458805302}

[[启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x1788486398}[支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能后，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[将向转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的请求报文中增加]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项。选项内容由]{style="font-family:宋体"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **circuit-id**]{lang="EN-US"}[和]{style="font-family:宋体"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **remote-id**]{lang="EN-US"}[决定。如果]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[收到的请求报文中已经包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项，则按照]{style="font-family:宋体"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **strategy**]{lang="EN-US"}[配置的策略处理请求报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1197197099}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x2023887749}[启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_130270366}

[\[Sysname\] interface gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_550416116}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp snooping information circuit-id]{lang="EN-US"}**]{#struct_0_x1331_x1769_277251935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **remote-id**]{lang="EN-US"}]{#struct_0_x1331_x1769_1761469657}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **strategy**]{lang="EN-US"}]{#struct_0_x1331_x1769_724312839}
:::::

::::: {#176427069 .myid}
[]{#_Toc404786492}[]{#struct_0_x1331_x1769_1730334482}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information remote-id**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DHCP命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1331_x1769_1032340169}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本特性的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1331_x1769_x1220537028}
:::

[ ]{lang="EN-US"}

[**[dhcp]{lang="EN-US"}**[ **snooping** **information** **remote-id**]{lang="EN-US"}]{#struct_0_x1331_x1769_1328170558}[命令用来配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的填充模式和填充格式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **remote-id**]{lang="EN-US"}]{#struct_0_x1331_x1769_1792553926}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x153159110}

[**[dhcp]{lang="EN-US"}**[ **snooping** **information** **remote-id** { **normal** \[ **format** { **ascii** \| **hex** } \] \| \[ **vlan** *vlan-id* \] { **string** *remote-id* \| **sysname** } }]{lang="EN-US"}]{#struct_0_x1331_x1769_1761404121}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **remote-id** \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1259395659}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x404542029}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x1450113013}[的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的填充模式为]{style="font-family:宋体"}[Normal]{lang="EN-US"}[、填充格式为]{style="font-family:宋体"}[hex]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_167051424}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_1425606347}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1381714532}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1656048000}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_933874152}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761338585}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1331_x1769_x421482738}[：为从指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[**[string]{lang="EN-US"}**[ *remote-id*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1911559537}[：指定以用户配置的字符串填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}*[remote-id]{lang="EN-US"}*[表示用户配置的用来填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的内容，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[sysname]{lang="EN-US"}**]{#struct_0_x1331_x1769_x281425368}[：指定以设备的系统名称填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。设备的系统名称可以通过系统视图下的]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[**[normal]{lang="EN-US"}**]{#struct_0_x1331_x1769_1457032183}[：指定以]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项，填充内容为接收报文接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[format]{lang="EN-US"}**]{#struct_0_x1331_x1769_x2012136493}[：指定]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项的填充格式。如果没有配置，则以]{style="font-family:宋体"}[hex]{lang="EN-US"}[模式填充。]{style="font-family:宋体"}

[**[ascii]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1653466493}[：指定以]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项，即将数值转换为对应的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码填充到]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[**[hex]{lang="EN-US"}**]{#struct_0_x1331_x1769_651080794}[：指定以]{style="font-family:宋体"}[十六进制数值的]{style="font-family:宋体"}[格式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761273049}

[[以用户配置的字符串（]{style="font-family:宋体"}**[string]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1667517982}[）和设备的系统名称（]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[）填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项时，填充内容固定为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[格式；以]{style="font-family:宋体"}[Normal]{lang="EN-US"}[模式填充]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项时，填充内容的格式由本命令配置的填充格式决定。]{style="font-family:宋体"}

[[需要注意的是，如果多次执行本命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x467249299}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1907814492}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1404308139}[配置采用字符串]{style="font-family:宋体"}[device001]{lang="EN-US"}[填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_444179083}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information strategy replace]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information remote-id string device001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2135764789}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_1761207513}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **strategy**]{lang="EN-US"}]{#struct_0_x1331_x1769_1867744331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dhcp** **snooping** **information**]{lang="EN-US"}]{#struct_0_x1331_x1769_288368090}
:::::

::::: {#1420984095 .myid}
[]{#_Toc404786493}[]{#struct_0_x1331_x1769_x291542221}[]{#_Toc318132895}[]{#_Toc202081922}[]{#_Toc154285768}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping information strategy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DHCP命令.files/image001.png){#图片 3 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1331_x1769_x1130152754}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1331_x1769_767932260}
:::

[ ]{lang="EN-US"}

[**[dhcp]{lang="EN-US"}**[ **snooping** **information** **strategy**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1844575147}[命令用来配置]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的请求报文的处理策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **strategy**]{lang="EN-US"}]{#struct_0_x1331_x1769_x683300024}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761141977}

[**[dhcp]{lang="EN-US"}**[ **snooping** **information** **strategy** { **drop** \| **keep** \| **replace** }]{lang="EN-US"}]{#struct_0_x1331_x1769_1901250636}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **information** **strategy**]{lang="EN-US"}]{#struct_0_x1331_x1769_137241641}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1749749724}

[[对带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_680493096}[的请求报文的处理策略为]{style="font-family:宋体"}**[replace]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1295845134}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_1738716535}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1644637056}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1759576951}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1762125017}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1007248718}

[**[drop]{lang="EN-US"}**]{#struct_0_x1331_x1769_x226354743}[：如果报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则丢弃该报文。]{style="font-family:宋体"}

[**[keep]{lang="EN-US"}**]{#struct_0_x1331_x1769_982134415}[：如果报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则保持该报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[不变并进行转发。]{style="font-family:宋体"}

[**[replace]{lang="EN-US"}**]{#struct_0_x1331_x1769_76906396}[：如果报文中带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则按照配置的填充格式填充]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，用该选项替换报文中原有的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，并进行转发。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1334628687}

[[本命令仅对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x296803407}[的请求报文有效。]{style="font-family:宋体"}

[[如果启用了]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_846645464}[支持]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[功能，则对于接收到的不包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的请求报文，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的处理方式始终为在请求报文中添加]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，并将报文转发给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1965916259}[对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[请求报文的处理策略为]{style="font-family:宋体"}**[replace]{lang="EN-US"}**[时，需要配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的填充模式和填充格式；处理策略为]{style="font-family:宋体"}**[keep]{lang="EN-US"}**[或]{style="font-family:宋体"}**[drop]{lang="EN-US"}**[时，不需要配置]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[选项的填充模式和填充格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1762059481}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x167631994}[配置]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[对带有]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的请求报文使用]{style="font-family:宋体"}**[keep]{lang="EN-US"}**[策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1902941736}

[\[Sysname\] interface gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping information strategy keep]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_391288669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp snooping information circuit-id]{lang="EN-US"}**]{#struct_0_x1331_x1769_2112873576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **information** **remote-id**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1512269358}
:::::

::: {#1185972132 .myid}
[]{#_Toc404786494}[]{#struct_0_x1331_x1769_761280747}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping max-learning-num**

------------------------------------------------------------------------

[**[dhcp snooping max-learning-num]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1735827132}[命令用来配置接口动态学习]{style="font-family:
宋体"}[DHCP Snooping]{lang="EN-US"}[表项的最大数目。]{style="font-family:宋体"}

[**[undo dhcp snooping max-learning-num]{lang="EN-US"}**]{#struct_0_x1331_x1769_1761600726}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_327439239}

[**[dhcp snooping max-learning-num ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1331_x1769_x889776797}

[**[undo dhcp snooping max-learning-num]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1168363956}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1676994540}

[[不限制接口动态学习]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1403389519}[表项的最大数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1707818369}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_x1966749761}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761535190}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1458739766}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_122049779}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1768931016}

[*[num]{lang="EN-US"}[ber]{lang="EN-US"}*]{#struct_0_x1331_x1769_2089600830}[：]{style="font-family:宋体"}[接口动态学习]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项的最大数目。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1428581170}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1037150163}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[动态学习]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项的最大数目为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x285600514}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping max-learning-num 1000]{lang="EN-US"}
:::

::::: {#517739755 .myid}
[]{#_Toc202081923}[]{#_Toc404786495}[]{#struct_0_x1331_x1769_1761469654}[]{#_Toc318132898}[]{#_Toc320718323}[]{#_Toc321058500}[]{#_Toc320718324}[]{#_Toc321058501}[]{#_Toc320718325}[]{#_Toc321058502}[]{#_Toc320718326}[]{#_Toc321058503}[]{#_Toc320718327}[]{#_Toc321058504}[]{#_Toc320718328}[]{#_Toc321058505}[]{#_Toc320718329}[]{#_Toc321058506}[]{#_Toc320718330}[]{#_Toc321058507}[]{#_Toc320718331}[]{#_Toc321058508}[]{#_Toc320718332}[]{#_Toc321058509}[]{#_Toc320718333}[]{#_Toc321058510}[]{#_Toc320718334}[]{#_Toc321058511}[]{#_Toc320718335}[]{#_Toc321058512}[]{#_Toc320718336}[]{#_Toc321058513}[]{#_Toc320718337}[]{#_Toc321058514}[]{#_Toc320718338}[]{#_Toc321058515}[]{#_Toc320718339}[]{#_Toc321058516}[]{#_Toc320718340}[]{#_Toc321058517}[]{#_Toc320718341}[]{#_Toc321058518}[]{#_Toc320718342}[]{#_Toc321058519}[]{#_Toc320718343}[]{#_Toc321058520}[]{#_Toc320718344}[]{#_Toc321058521}[]{#_Toc320718345}[]{#_Toc321058522}[]{#_Toc320718346}[]{#_Toc321058523}[]{#_Toc320718347}[]{#_Toc321058524}[]{#_Toc320718348}[]{#_Toc321058525}[]{#_Toc320718349}[]{#_Toc321058526}[]{#_Toc320718350}[]{#_Toc321058527}[]{#_Toc320718351}[]{#_Toc321058528}[]{#_Toc320718352}[]{#_Toc321058529}[]{#_Toc320718353}[]{#_Toc321058530}[]{#_Toc320718354}[]{#_Toc321058531}[]{#_Toc320718355}[]{#_Toc321058532}[]{#_Toc320718356}[]{#_Toc321058533}[]{#_Toc320718357}[]{#_Toc321058534}[]{#_Toc320718358}[]{#_Toc321058535}[]{#_Toc320718359}[]{#_Toc321058536}[]{#_Toc320718360}[]{#_Toc321058537}[]{#_Toc320718361}[]{#_Toc321058538}[]{#_Toc320718362}[]{#_Toc321058539}[]{#_Toc320718363}[]{#_Toc321058540}[]{#_Toc320718364}[]{#_Toc321058541}[]{#_Toc320718365}[]{#_Toc321058542}[]{#_Toc320718366}[]{#_Toc321058543}[]{#_Toc320718367}[]{#_Toc321058544}[]{#_Toc320718368}[]{#_Toc321058545}[]{#_Toc320718369}[]{#_Toc321058546}[]{#_Toc320718370}[]{#_Toc321058547}[]{#_Toc320718371}[]{#_Toc321058548}[]{#_Toc320718372}[]{#_Toc321058549}[]{#_Toc320718373}[]{#_Toc321058550}[]{#_Toc320718374}[]{#_Toc321058551}[]{#_Toc320718375}[]{#_Toc321058552}[]{#_Toc320718376}[]{#_Toc321058553}[]{#_Toc320718377}[]{#_Toc321058554}[]{#_Toc320718378}[]{#_Toc321058555}[]{#_Toc320718379}[]{#_Toc321058556}[]{#_Toc320718380}[]{#_Toc321058557}[]{#_Toc320718381}[]{#_Toc321058558}[]{#_Toc320718382}[]{#_Toc321058559}[]{#_Toc320718383}[]{#_Toc321058560}[]{#_Toc320718384}[]{#_Toc321058561}[]{#_Toc320718385}[]{#_Toc321058562}[]{#_Toc320718386}[]{#_Toc321058563}[]{#_Toc320718387}[]{#_Toc321058564}[]{#_Toc320718388}[]{#_Toc321058565}[]{#_Toc320718389}[]{#_Toc321058566}[]{#_Toc320718390}[]{#_Toc321058567}[]{#_Toc320718391}[]{#_Toc321058568}[]{#_Toc320718392}[]{#_Toc321058569}[]{#_Toc320718393}[]{#_Toc321058570}[]{#_Toc320718394}[]{#_Toc321058571}[]{#_Toc320718395}[]{#_Toc321058572}[]{#_Toc320718396}[]{#_Toc321058573}[]{#_Toc320718397}[]{#_Toc321058574}[]{#_Toc320718398}[]{#_Toc321058575}[]{#_Toc320718399}[]{#_Toc321058576}[]{#_Toc320718400}[]{#_Toc321058577}[]{#_Toc320718401}[]{#_Toc321058578}[]{#_Toc320718402}[]{#_Toc321058579}[]{#_Toc320718403}[]{#_Toc321058580}[]{#_Toc320718404}[]{#_Toc321058581}[]{#_Toc320718405}[]{#_Toc321058582}[]{#_Toc320718406}[]{#_Toc321058583}[]{#_Toc320718407}[]{#_Toc321058584}[]{#_Toc320718408}[]{#_Toc321058585}[]{#_Toc320718409}[]{#_Toc321058586}[]{#_Toc320718410}[]{#_Toc321058587}[]{#_Toc320718411}[]{#_Toc321058588}[]{#_Toc320718412}[]{#_Toc321058589}[]{#_Toc320718413}[]{#_Toc321058590}[]{#_Toc320718414}[]{#_Toc321058591}[]{#_Toc320718415}[]{#_Toc321058592}[]{#_Toc320718416}[]{#_Toc321058593}[]{#_Toc320718417}[]{#_Toc321058594}[]{#_Toc320718418}[]{#_Toc321058595}[]{#_Toc320718419}[]{#_Toc321058596}[]{#_Toc320718420}[]{#_Toc321058597}[]{#_Toc320718421}[]{#_Toc321058598}[]{#_Toc320718422}[]{#_Toc321058599}[]{#_Toc320718423}[]{#_Toc321058600}[]{#_Toc320718424}[]{#_Toc321058601}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping rate-limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DHCP命令.files/image001.png){#图片 4 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1331_x1769_724378375}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1331_x1769_x611732243}
:::

[ ]{lang="EN-US"}

[**[dhcp]{lang="EN-US"}**[ **snooping** **rate-limit**]{lang="EN-US"}]{#struct_0_x1331_x1769_336325005}[命令用来启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的报文限速功能，即限制接口接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的速率。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **rate-limit**]{lang="EN-US"}]{#struct_0_x1331_x1769_x689812733}[命令用来关闭]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的报文限速功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x119907270}

[**[dhcp]{lang="EN-US"}**[ **snooping** **rate-limit** *rate*]{lang="EN-US"}]{#struct_0_x1331_x1769_1550403480}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **rate-limit**]{lang="EN-US"}]{#struct_0_x1331_x1769_x662780221}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761404118}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x1258936908}[的报文限速功能处于关闭状态，即不限制接口接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的速率。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x834683832}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_x1571072147}[二层聚合接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1099582725}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_847222724}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1028232661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_583146842}

[*[rate]{lang="EN-US"}*]{#struct_0_x1331_x1769_1337370997}[：接口接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的最高速率，单位为]{style="font-family:宋体"}[Kbps]{lang="EN-US"}[。]{style="font-family:宋体"}[本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761338582}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有启用]{lang="EN-US" style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x421548274}[功能后，本命令的配置才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口接收到的]{style="font-family:宋体"}]{#struct_0_x1331_x1769_418227732}[DHCP]{lang="EN-US"}[报文速率超过了限制，则丢弃超过速率限制的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果二层以太网接口加入了聚合组，则该接口采用对应二层聚合接口下的]{style="font-family:宋体"}]{#struct_0_x1331_x1769_79872132}[DHCP]{lang="EN-US"}[报文限速配置。如果二层以太网接口离开聚合组，则该接口采用二层以太网接口下的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文限速配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于某些产品来说，由于芯片的限制，限速速率的实际生效值只能是某个数值的整数倍。比如，某产品芯片支持的速率值是]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x350673907}[8]{lang="EN-US"}[的整数倍，当用户设置的速率值为]{style="font-family:宋体"}[67]{lang="EN-US"}[时，实际的生效值是]{style="font-family:宋体"}[64]{lang="EN-US"}[或]{style="font-family:宋体"}[72]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_91222610}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_1759943080}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的最高速率为]{style="font-family:宋体"}[64Kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_2135934496}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping rate-limit 64]{lang="EN-US"}
:::::

::: {#-1865746272 .myid}
[]{#_Toc404786496}[]{#struct_0_x1331_x1769_1761273046}[]{#_Toc318132899}[]{#_Toc295916618}[]{#_Toc296072729}[]{#_Toc296072767}[]{#_Toc295916619}[]{#_Toc296072730}[]{#_Toc296072768}

**DHCP \-- DHCP Snooping配置命令 \-- dhcp snooping trust**

------------------------------------------------------------------------

[**[dhcp]{lang="EN-US"}**[ **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1667059230}[命令用来配置端口为信任端口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1730741572}[命令用来恢复端口为不信任端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1430350423}

[**[dhcp]{lang="EN-US"}**[ **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_x943041205}

[**[undo]{lang="EN-US"}**[ **dhcp** **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1727822587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_735091807}

[[在启用]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_192262475}[功能后，设备上所有支持]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[功能的端口均为不信任端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x636133075}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_1761207510}[二层聚合接口视图]{style="font-family:宋体"}[/WLAN-BSS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/WLAN-ESS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1867547723}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x879721628}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x522613239}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1082106007}

[[指向]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x178438112}[服务器方向的端口需要设置为信任端口，其他端口设置为不信任端口，从而保证]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端只能从合法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，私自架设的伪]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器无法为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1211540058}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x99798606}[配置二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为信任端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_1761141974}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp snooping trust]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1901054028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dhcp** **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1450183080}
:::

::: {#-442415165 .myid}
[]{#_Toc404786497}[]{#struct_0_x1331_x1769_200092078}[]{#_Toc318132900}[]{#_Toc202081924}[]{#_Toc137350341}[]{#_Toc135535514}

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping binding**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **binding**]{lang="EN-US"}]{#struct_0_x1331_x1769_638719512}[命令用来显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1641848977}

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **binding** \[ **ip** *ip-address* \[ **vlan** *vlan-id* \] \]]{lang="EN-US"}]{#struct_0_x1331_x1769_37873580}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1477197158}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1762125014}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1007183182}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x220477499}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x175928124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1669505526}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x939174276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1003425695}

[**[ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_1644063348}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1331_x1769_1762059478}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x168090731}

[[执行本命令时，如果不指定任何参数，则显示设备上所有]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_967123041}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x493989167}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1368781551}[显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp snooping binding]{lang="EN-US"}]{#struct_0_x1331_x1769_x1580683173}

[ 2 DHCP snooping entries found]{lang="EN-US"}

[ IP address      MAC address    Lease        VLAN  SVLAN Interface]{lang="EN-US"}

[ =============== ============== ============ ===== ===== =================]{lang="EN-US"}

[ 1.1.1.7         0000-0101-0107 16907533     2     3     GE1/0/1]{lang="EN-US"}

[ 1.1.1.11        0000-0101-010b 16907537     2     3     GE1/0/3]{lang="EN-US"}

[]{#struct_0_x1331_x1769_1761600727}[[表1-14 ]{lang="EN-US"}[display dhcp snooping binding]{lang="EN-US"}]{#_Toc138412533}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1448547759}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_327504775}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_644445063}

[[DHCP snooping entries found]{lang="EN-US"}]{#struct_0_x1331_x1769_x470014512}

[[表项统计计数]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x771238906}

[[IP address]{lang="EN-US"}]{#struct_0_x1331_x1769_117988612}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_1761535191}[服务器为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_x1331_x1769_1458674230}

[[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1395830176}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Lease]{lang="EN-US"}]{#struct_0_x1331_x1769_x36986845}

[[绑定的租约剩余时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x679248661}

[[VLAN]{lang="EN-US"}]{#struct_0_x1331_x1769_938761470}

[[如果]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1761469655}[功能与]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能同时使用，或接收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文带有两层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，则表示外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[；否则，表示与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端连接的设备端口所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[SVLAN]{lang="EN-US"}]{#struct_0_x1331_x1769_724443911}

[[如果]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_414859998}[功能与]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[功能同时使用，或接收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文带有两层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，则表示内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[；否则，显示为"]{style="font-family:宋体"}[N/A]{lang="EN-US"}["]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1331_x1769_x1577891743}

[[与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x357003271}[客户端连接的设备端口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761404119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **enable**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1258871372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **dhcp** **snooping**]{lang="EN-US"}]{#struct_0_x1331_x1769_x132818952}**[ binding]{lang="EN-US"}**

::: {#-1473963307 .myid}
[]{#_Toc137350342}[]{#_Toc135535515}[]{#_Toc108607387}[]{#_Toc202081925}[]{#_Toc404786498}[]{#struct_0_x1331_x1769_1693485034}[]{#_Toc318132901}

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping binding database**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database**]{lang="EN-US"}]{#struct_0_x1331_x1769_x785795588}[命令用来显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项备份信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1886293019}

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **binding** **database**]{lang="EN-US"}]{#struct_0_x1331_x1769_601883416}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1771062510}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_492122471}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1761338583}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x421613810}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_2031050602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_867305626}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x646116809}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1459202776}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1905321424}[显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项备份信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp snooping binding database]{lang="EN-US"}]{#struct_0_x1331_x1769_185484121}

[File name               :   database.dhcp]{lang="EN-US"}

[[Username                :   ]{lang="EN-US"}]{#struct_0_x1331_x1769_1761273047}

[[Password                :   ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1667124766}

[[Update interval         :   600 seconds]{lang="EN-US"}]{#struct_0_x1331_x1769_890672070}

[Latest write time       :   Feb 27 18:48:04 2012]{lang="EN-US"}

[Status                  :   Last write succeeded.]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display dhcp snooping binding database]{lang="EN-US"}]{#struct_0_x1331_x1769_x258261648}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1452015737}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1867808072}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_334015985}

[[File name]{lang="EN-US"}]{#struct_0_x1331_x1769_96490669}

[[存储]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1761207511}[表项的文件名称]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_x1331_x1769_1867613259}

[[配置远程目标文件时的用户名]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x88297130}

[[Password]{lang="EN-US"}]{#struct_0_x1331_x1769_x375735830}

[[配置远程目标文件时的密码，有配置时显示为]{style="font-family:宋体"}["\*\*\*\*\*\*"]{lang="EN-US"}]{#struct_0_x1331_x1769_x1064738698}

[[Update interval]{lang="EN-US"}]{#struct_0_x1331_x1769_x1093478703}

[[定期刷新表项存储文件的刷新时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1761141975}

[[Latest write time]{lang="EN-US"}]{#struct_0_x1331_x1769_1901119564}

[[最近一次写文件的时间]{style="font-family:宋体"}]{#struct_0_x1331_x1769_508312896}

[[Status]{lang="EN-US"}]{#struct_0_x1331_x1769_x1171144335}

[[写文件的状态，即写文件是否成功]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1461806846}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Writing]{lang="EN-US"}]{#struct_0_x1331_x1769_1977162053}[：正在写文件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write succeeded.]{lang="EN-US"}]{#struct_0_x1331_x1769_1762125015}[：]{lang="EN-US" style="font-family:
  宋体"}[写文件成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Last write failed.]{lang="EN-US"}]{#struct_0_x1331_x1769_x1007117646}[：]{lang="EN-US" style="font-family:
  宋体"}[写文件失败]{style="font-family:宋体"}

[]{#_Toc318132902}[]{#_Toc202081926}[]{#_Toc312418653}[]{#_Toc295916623}[]{#_Toc296072734}[]{#_Toc296072772}[]{#_Toc295916624}[]{#_Toc296072735}[]{#_Toc296072773}[]{#_Toc295916626}[]{#_Toc296072737}[]{#_Toc296072775}[]{#_Toc295916627}[]{#_Toc296072738}[]{#_Toc296072776}[ ]{lang="EN-US"}

::: {#176521232 .myid}
[]{#_Toc404786499}[]{#struct_0_x1331_x1769_x497348147}

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping information**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dhcp snooping** **information**]{lang="EN-US"}]{#struct_0_x1331_x1769_1928429808}[命令用来显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[上]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1183665359}

[**[display]{lang="EN-US"}**[ **dhcp snooping** **information** { **all** \| **interface** *interface-type* *interface-number* }]{lang="EN-US"}]{#struct_0_x1331_x1769_884522546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1871708110}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1762059479}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x168156267}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1404904355}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1725752879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1123809399}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_377900114}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_683259877}

[**[all]{lang="EN-US"}**]{#struct_0_x1331_x1769_x720397406}[：显示所有二层以太网接口对应的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x653292421}[：显示指定接口对应的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x967282625}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_514001366}[显示所有接口对应的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp snooping information all]{lang="EN-US"}]{#struct_0_x1331_x1769_x906117579}

[Interface: Bridge-Aggregation1]{lang="EN-US"}

[   Status: Disable]{lang="EN-US"}

[   Strategy: Drop]{lang="EN-US"}

[   Circuit ID:]{lang="EN-US"}

[     Padding format: User Defined]{lang="EN-US"}

[       User defined: abcd]{lang="EN-US"}

[     Format: ASCII]{lang="EN-US"}

[   Remote ID:]{lang="EN-US"}

[     Padding format: Normal]{lang="EN-US"}

[     Format: ASCII]{lang="EN-US"}

[   VLAN 10:]{lang="EN-US"}

[     Circuit ID: abcd]{lang="EN-US"}

[     Remote ID: company]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display dhcp snooping information]{lang="EN-US"}]{#struct_0_x1331_x1769_x1048883541}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1457756394}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x967348161}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2074180625}

[[Interface]{lang="EN-US"}]{#struct_0_x1331_x1769_812328995}

[[接口名]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x789092581}

[[Status]{lang="EN-US"}]{#struct_0_x1331_x1769_x699049273}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x1919087668}[的状态，取值为]{style="font-family:宋体"}[Enable]{lang="EN-US"}[或]{style="font-family:宋体"}[Disable]{lang="EN-US"}

[[Strategy]{lang="EN-US"}]{#struct_0_x1331_x1769_x967413697}

[[对包含]{style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_x1067352292}[的请求报文的处理策略，取值为]{style="font-family:宋体"}[Drop]{lang="EN-US"}[、]{style="font-family:宋体"}[Keep]{lang="EN-US"}[或]{style="font-family:宋体"}[Replace]{lang="EN-US"}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x495814460}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1154877165}[子选项的内容]{style="font-family:宋体"}

[[Padding format]{lang="EN-US"}]{#struct_0_x1331_x1769_1511625098}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_647783100}[的填充模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在填充]{lang="EN-US" style="font-family:宋体"}[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x967479233}[子选项时，取值为]{lang="EN-US" style="font-family:宋体"}[Normal]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[User Defined]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Verbose]{lang="EN-US"}[(]{lang="EN-US"}[sysname]{lang="EN-US"}[)]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Verbose(MAC)]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Verbose(user defined)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在填充]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1824460536}[Remote ID]{lang="EN-US"}[子选项时，取值为]{style="font-family:宋体"}[Normal]{lang="EN-US"}[、]{style="font-family:宋体"}[Sysname]{lang="EN-US"}[或]{style="font-family:宋体"}[User Defined]{lang="EN-US"}

[[Node identifier]{lang="EN-US"}]{#struct_0_x1331_x1769_x1248890478}

[[接入节点的标识]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x120574508}

[[User defined]{lang="EN-US"}]{#struct_0_x1331_x1769_x967544769}

[[用户自定义的子选项内容]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x686492781}

[[Format]{lang="EN-US"}]{#struct_0_x1331_x1769_394615739}

[[Option 82]{lang="EN-US"}]{#struct_0_x1331_x1769_1932719143}[子选项的填充格式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在填充]{lang="EN-US" style="font-family:宋体"}[Circuit ID]{lang="EN-US"}]{#struct_0_x1331_x1769_997737723}[子选项时，取值为]{lang="EN-US" style="font-family:宋体"}[ASCII]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Default]{lang="EN-US"}[或]{style="font-family:宋体"}[Hex]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在填充]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x967610305}[Remote ID]{lang="EN-US"}[子选项时，取值为]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[或]{style="font-family:宋体"}[Hex]{lang="EN-US"}

[[Remote ID]{lang="EN-US"}]{#struct_0_x1331_x1769_2056790406}

[[Remote ID]{lang="EN-US"}]{#struct_0_x1331_x1769_1742411889}[子选项的内容]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x1331_x1769_x286672908}

[[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1331_x1769_x1985979402}[内收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文填充的]{style="font-family:宋体"}[Circuit ID]{lang="EN-US"}[子选项和]{style="font-family:宋体"}[Remote ID]{lang="EN-US"}[子选项内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#50833264 .myid}
[]{#_Toc404786500}[]{#struct_0_x1331_x1769_x967675841}

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping packet statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_x1331_x1769_x1525782383}[命令用来显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1368045097}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1554338490}

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_x1331_x1769_1618298888}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_x695424458}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x1290733419}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1331_x1769_x967741377}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1331_x1769_481596929}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_573382413}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_513224773}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1412979067}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_276383131}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x980370820}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_764888203}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x966758337}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2056617106}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_1411377301}[：显示指定单板的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_2031974883}[：显示指定成员设备的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1509732485}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_1685140701}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_1219150870}[：显示指定单板的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_1126702850}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x966823873}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_2063433622}[显示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp snooping packet statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_x368073310}

[ DHCP packets received                  : 100]{lang="EN-US"}

[ DHCP packets sent                      : 200]{lang="EN-US"}

[ Invalid DHCP packets dropped           : 0]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display dhcp snooping packet statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_1207467568}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1428832754}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1683718453}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1256271309}

[[DHCP packets received]{lang="EN-US"}]{#struct_0_x1331_x1769_x967282624}

[[接收的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_513935830}[报文数]{style="font-family:宋体"}

[[DHCP packets sent]{lang="EN-US"}]{#struct_0_x1331_x1769_837789970}

[[发送的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1152043483}[报文数]{style="font-family:宋体"}

[[Invalid DHCP packets dropped]{lang="EN-US"}]{#struct_0_x1331_x1769_x1565729474}

[[丢弃的无效]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x1331_x1769_954858384}[报文数]{style="font-family:宋体"}

[]{#_Toc318132903}[]{#_Toc202081927}[]{#_Toc295916629}[]{#_Toc296072740}[]{#_Toc296072778}[]{#_Toc295916630}[]{#_Toc296072741}[]{#_Toc296072779}[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x967348160}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset dhcp snooping packet statistics]{lang="EN-US"}**]{#struct_0_x1331_x1769_2074115089}

::: {#-1840435695 .myid}
[]{#_Toc404786501}[]{#struct_0_x1331_x1769_41321982}

**DHCP \-- DHCP Snooping配置命令 \-- display dhcp snooping trust**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_1073129874}[命令用来显示信任端口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_639769464}

[**[display]{lang="EN-US"}**[ **dhcp** **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_1408568426}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_166774813}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1372302991}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x967413696}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1067286756}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_1966380934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_523457522}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x278151821}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x39940769}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1100899641}[显示信任端口信息。]{style="font-family:宋体"}

[[\<Sysname\> display dhcp snooping trust]{lang="EN-US"}]{#struct_0_x1331_x1769_x967479232}

[ DHCP snooping is enabled.]{lang="EN-US"}

[ Interface                                       Trusted]{lang="EN-US"}

[ =========================                       ============]{lang="EN-US"}

[ GigabitEthernet1/0/1                            Trusted]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display dhcp snooping trust]{lang="EN-US"}]{#struct_0_x1331_x1769_x1824395000}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1429212197}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1068482206}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_772291710}

[[DHCP snooping is]{lang="EN-US"}]{#struct_0_x1331_x1769_x1593530713}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_1012757822}[功能的开启状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enable]{lang="EN-US"}]{#struct_0_x1331_x1769_x2079688351}[：启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[ Snooping]{lang="EN-US"}[[功能]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disable]{lang="EN-US"}]{#struct_0_x1331_x1769_x967544768}[：未启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[ Snooping]{lang="EN-US"}[[功能]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[Interface]{lang="EN-US"}]{#struct_0_x1331_x1769_x967610304}

[[接口名称]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2056855942}

[[Trusted]{lang="EN-US"}]{#struct_0_x1331_x1769_1036439685}

[[接口为信任接口]{style="font-family:宋体"}]{#struct_0_x1331_x1769_47858908}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1377658634}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dhcp]{lang="EN-US"}**[ **snooping** **trust**]{lang="EN-US"}]{#struct_0_x1331_x1769_x354316310}

::: {#500709883 .myid}
[]{#_Toc404786502}[]{#struct_0_x1331_x1769_x1161546105}[]{#_Toc318132904}[]{#_Toc202081928}

**DHCP \-- DHCP Snooping配置命令 \-- reset dhcp snooping binding**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **dhcp** **snooping binding**]{lang="EN-US"}]{#struct_0_x1331_x1769_x967675840}[命令用来清除]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1525716847}

[**[reset]{lang="EN-US"}**[ **dhcp** **snooping** **binding** { **all** \| **ip** *ip-address* \[ **vlan** *vlan-id* \] }]{lang="EN-US"}]{#struct_0_x1331_x1769_x1794299313}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_215176301}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1163901599}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_604030793}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1063461208}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x1987740179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x967741376}

[**[all]{lang="EN-US"}**]{#struct_0_x1331_x1769_481531393}[：清除所有的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1331_x1769_x885878225}[：清除指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1331_x1769_x449797992}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x798176653}

[[对于分布式设备，执行该命令后，将清除所有槽位上对应的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x1331_x1769_x220197166}[表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1379955660}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x1843058249}[清除所有的]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp snooping binding all]{lang="EN-US"}]{#struct_0_x1331_x1769_x966758336}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2056682642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dhcp snooping binding]{lang="EN-US"}**]{#struct_0_x1331_x1769_963981216}
:::

::: {#-1842336086 .myid}
[]{#_Toc404786503}[]{#struct_0_x1331_x1769_1056578790}[]{#_Toc318132905}[]{#_Toc202081929}

**DHCP \-- DHCP Snooping配置命令 \-- reset dhcp snooping packet statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_x1331_x1769_529123663}[命令用来清除]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_442839326}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x515736439}

[**[reset]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_x1331_x1769_x786252814}

[[分布式设备---独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1331_x1769_x531211502}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x966823872}

[[分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1331_x1769_2063368086}[模式：]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x709975592}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1358939948}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_1537324269}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1135787309}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_1148106409}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_122980373}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1912500054}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x967282627}[：清除指定单板的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[为单板所在的槽位号。如果未指定本参数，则清除主用主控板上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（分布式设备---独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_513870294}[：清除指定成员设备的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_2025719924}[：清除指定成员设备的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x1894453776}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x293388107}[：清除指定单板的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则清除全局主用主控板上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_1126702849}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_774508138}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x967348163}[清除]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dhcp snooping packet statistics]{lang="EN-US"}]{#struct_0_x1331_x1769_2074049553}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_456462104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dhcp** **snooping** **packet** **statistics**]{lang="EN-US"}]{#struct_0_x1331_x1769_1377940525}
:::

::: {#-442033247 .myid}
[]{#_Toc404786505}[]{#struct_0_x1331_x1769_651514862}[]{#_Toc315706881}

**DHCP \-- BOOTP客户端配置命令 \-- display bootp client**

------------------------------------------------------------------------

[**[display bootp client]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1203401708}[命令用来显示]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x894086713}

[**[display]{lang="EN-US"}**[ **bootp** **client** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1331_x1769_x967413699}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1067221220}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_x1053752483}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_918356903}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_921003193}

[[network-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x1300451821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x342606026}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1331_x1769_x387885588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_883002493}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_x967479235}[：显示指定接口的]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端相关信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1824591608}

[[如果不指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1331_x1769_876176252}[参数，则显示所有接口上的]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_1091917445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_1763757093}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_930579374}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display bootp client interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1331_x1769_773442810}

[GigabitEthernet1/0/1 BOOTP client information:]{lang="EN-US"}

[ Allocated IP: 169.254.0.2 255.255.0.0]{lang="EN-US"}

[ Transaction ID: 0x3d8a7431]{lang="EN-US"}

[ MAC Address: 00e0-fc0a-c3ef]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x967544771}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_x685968492}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display bootp client interface vlan-interface 10]{lang="EN-US"}]{#struct_0_x1331_x1769_x973561731}

[Vlan-interface10 BOOTP client information:]{lang="EN-US"}

[ Allocated IP: 169.254.0.2 255.255.0.0]{lang="EN-US"}

[ Transaction ID: 0x3d8a7431]{lang="EN-US"}

[ MAC Address: 00e0-fc0a-c3ef]{lang="EN-US"}

[]{#struct_0_x1331_x1769_854494660}[[表1-19 ]{lang="EN-US"}[display bootp client]{lang="EN-US"}]{#_Toc138213927}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1427351737}[[字段]{style="font-family:黑体"}]{#struct_0_x1331_x1769_124625635}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x1226536839}

[[GigabitEthernet1/0/1 BOOTP client information/Vlan-interface10 BOOTP client information]{lang="EN-US"}]{#struct_0_x1331_x1769_x967610307}

[[作为]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_2056921478}[客户端的接口信息]{style="font-family:宋体"}

[[Allocated IP]{lang="EN-US"}]{#struct_0_x1331_x1769_x971857243}

[[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_2118601222}[服务器为]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Transaction ID]{lang="EN-US"}]{#struct_0_x1331_x1769_x1161198519}

[[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_x121484893}[报文中]{style="font-family:宋体"}[XID]{lang="EN-US"}[字段值，即]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端发送]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[请求报文时选择的随机数，用来与]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[服务器的响应报文相匹配。如果响应报文的]{style="font-family:宋体"}[XID]{lang="EN-US"}[字段值与请求报文的]{style="font-family:宋体"}[XID]{lang="EN-US"}[字段值不相同，则]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[客户端丢弃该响应报文]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_x1331_x1769_x967675843}

[[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_x1525913455}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_655900949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip address ]{lang="EN-US"}**]{#struct_0_x1331_x1769_x1256441905}**[boot]{lang="EN-US"}[p-alloc]{lang="EN-US"}**

::: {#-663021119 .myid}
[]{#_Toc404786506}[]{#struct_0_x1331_x1769_x984636304}[]{#_Toc315706882}

**DHCP \-- BOOTP客户端配置命令 \-- ip address bootp-alloc**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **address** **bootp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_1660759650}[命令用来配置接口通过]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **address** **bootp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_x588373208}[命令用来取消接口通过]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x967741379}

[**[ip]{lang="EN-US"}**[ **address** **bootp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_481465857}

[**[undo]{lang="EN-US"}**[ **ip** **address** **bootp-alloc**]{lang="EN-US"}]{#struct_0_x1331_x1769_950769087}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2053390666}

[[接口不通过]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}]{#struct_0_x1331_x1769_1608521707}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_57186273}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1331_x1769_2128243077}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_x48397079}

[[network-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_822101336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1331_x1769_x966758339}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2056223890}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x133186938}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_565573849}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置接口通过]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x2085504638}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip address bootp-alloc]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1331_x1769_x430619826}

[[\# ]{lang="EN-US"}]{#struct_0_x1331_x1769_582030096}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[上配置接口通过]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1331_x1769_x966823875}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ip address bootp-alloc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1331_x1769_2063040406}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **bootp** **client**]{lang="EN-US"}]{#struct_0_x1331_x1769_414992203}
:::
