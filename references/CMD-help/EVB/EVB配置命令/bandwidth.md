::: {#1742433432 .myid}
[]{#_Toc311899208}[]{#_Toc311899217}[]{#_Toc311899219}[]{#_Toc311899220}[]{#_Toc296504297}[]{#_Toc404798159}[]{#struct_0_x2095_42796_1892055009}

**EVB \-- EVB配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x2095_42796_x623987074}[命令用来配置当前接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2095_42796_1338019102}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1484604760}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x2095_42796_x1284486762}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2095_42796_691667952}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1720117579}

[[接口的期望带宽等于其所属物理端口的缺省最大带宽。]{style="font-family:宋体"}]{#struct_0_x2095_42796_2095241145}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1821567724}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_41638461}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_400031494}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_x1706499792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_1406388554}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x886847262}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x2095_42796_x1015045315}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x576971728}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_982486602}[配置]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[的期望带宽为]{style="font-family:宋体"}[2000000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_x1821371116}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[bandwidth 2000000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_1581416410}[配置]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[的期望带宽为]{style="font-family:宋体"}[2000000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_x1605672924}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[bandwidth 2000000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_1184708140}[配置]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[的期望带宽为]{style="font-family:宋体"}[2000000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_22008381}

[\[Sysname\] interface s-channel 1/0/1:10.1]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10.1\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[bandwidth 2000000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_464611400}[配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[的期望带宽为]{style="font-family:宋体"}[2000000kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_1233411077}

[\[Sysname\] interface schannel-aggregation 1:10.1]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10.1\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[bandwidth 2000000]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404798160}[]{#struct_0_x2095_42796_1742846108}

**EVB \-- EVB配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x2095_42796_1656784683}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x633122229}

[**[default]{lang="EN-US"}**]{#struct_0_x2095_42796_1884998471}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x823013002}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_x1821436652}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1243600685}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_181486492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_619632267}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x403287724}

[[接口上的某些配置被恢复为缺省情况后可能会对现有功能产生影响，请在执行本命令之前，完全了解其将对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x2095_42796_2132364943}

[[执行本命令之后，可以通过]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **this**]{lang="EN-US"}]{#struct_0_x2095_42796_x986237561}[命令来确认效果。对于未能成功恢复为缺省情况的配置，可以查阅相关的命令手册并进行手工恢复。如果手工恢复仍失败，可以通过设备给出的提示信息来定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1509138963}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x1821240044}[将]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_x1424327760}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10\] default]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1581416408}[将]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x1605148637}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\] default]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x1173443570}[将]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x1195099303}

[\[Sysname\] interface s-channel 1/0/1:10.1]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10.1\] default]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_311474759}[将]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_1581416409}

[\[Sysname\] interface schannel-aggregation 1:10.1]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10.1\] default]{lang="PT-BR"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404798161}[]{#struct_0_x2095_42796_x1836811706}

**EVB \-- EVB配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x2095_42796_565134103}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2095_42796_2121244561}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1396091733}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x2095_42796_x1821305580}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2095_42796_x1365304139}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1180299026}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_x2095_42796_x1799283791}["。比如：]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[的缺省描述信息为]{style="font-family:宋体"}[S-Channel]{lang="EN-US"}[1/0/1:10]{lang="PT-BR"}[ Interface]{lang="EN-US"}[，]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:
宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[的缺省描述信息为]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[ Interface]{lang="EN-US"}[，]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[的缺省描述信息为]{style="font-family:宋体"}[S-Channel]{lang="EN-US"}[1/0/1:10.1]{lang="PT-BR"}[ Interface]{lang="EN-US"}[，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[的缺省描述信息为]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[ Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_352585843}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_1120784076}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_914645274}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_1792374720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_x1382732999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1821108972}

[*[text]{lang="EN-US"}*]{#struct_0_x2095_42796_463472103}[：表示接口的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x2144171040}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x1461201431}[配置]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[的描述信息为"]{style="font-family:宋体"}[S-Channel to lab]{lang="PT-BR"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_x60709714}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[description ]{lang="EN-US"}[S-Channel to lab]{lang="PT-BR"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x2146546102}[配置]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[的描述信息为"]{style="font-family:宋体"}[Schannel-Aggregation to lab]{lang="PT-BR"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_x1745166811}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[description ]{lang="EN-US"}[Schannel-Aggregation to lab]{lang="PT-BR"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x399167018}[配置]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[的描述信息为"]{style="font-family:宋体"}[VSI to lab]{lang="PT-BR"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_x1821174508}

[\[Sysname\] interface s-channel 1/0/1:10.1]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10.1\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[description ]{lang="EN-US"}[VSI to lab]{lang="PT-BR"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x1282269346}[配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[的描述信息为"]{style="font-family:宋体"}[VSI-Aggregation to lab]{lang="PT-BR"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_108049272}

[\[Sysname\] interface schannel-aggregation 1:10.1]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10.1\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[description ]{lang="EN-US"}[VSI-Aggregation to lab]{lang="PT-BR"}
:::

::: {#1524882762 .myid}
[]{#_Toc404798162}[]{#struct_0_x2095_42796_2019331514}

**EVB \-- EVB配置命令 \-- display evb cdcp**

------------------------------------------------------------------------

[**[display evb cdcp]{lang="EN-US"}**]{#struct_0_x2095_42796_1400603493}[命令用来显示]{style="font-family:宋体"}[CDCP]{lang="EN-US"}[协商信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x29708524}

[**[display evb cdcp]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2095_42796_x343702770}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557376730}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1483576400}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1511701115}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_274501671}

[[network-operator]{lang="PT-BR"}]{#struct_0_x2095_42796_x818906191}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_1861794881}

[[mdc-operator]{lang="PT-BR"}]{#struct_0_x2095_42796_707012047}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x860611743}

[**[interface]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1264871899}[ *interface-type interface-number*]{lang="PT-BR"}[：显示指定接口（二层以太网接口或二层聚合接口）上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="PT-BR"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有已使能]{style="font-family:
宋体"}[EVB]{lang="PT-BR"}[功能的接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557442266}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1498156482}[显示所有已使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能的接口上的]{style="font-family:宋体"}[CDCP]{lang="PT-BR"}[协商信息。]{style="font-family:宋体"}

[[\<Sysname\> display evb cdcp]{lang="EN-US"}]{#struct_0_x2095_42796_538591676}

[ ]{lang="PT-BR"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Bridge-Aggregation1\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="PT-BR"}

[S-component capability               : Local-supported/Remote-not supported]{lang="PT-BR"}

[Supported S-Channel numbers per-port : Local-167/Remote-0]{lang="PT-BR"}

[SVID range                           : 2-4094]{lang="PT-BR"}

[SCID requested from remote           :]{lang="PT-BR"}

[SCID/SVID pair list allocated        :]{lang="PT-BR"}

[ \<1, 1\>]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--GigabitEthernet1/0/1\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="PT-BR"}

[S-component capability               : Local-supported/Remote-supported]{lang="PT-BR"}

[Supported S-Channel numbers per-port : Local-167/Remote-167]{lang="PT-BR"}

[SVID range                           : 2-4094]{lang="PT-BR"}

[SCID requested from remote           :]{lang="PT-BR"}

[ 1, 2, 3, 4, 6, 10, 11, 12, 34, 35, 67]{lang="PT-BR"}

[SCID/SVID pair list allocated        :]{lang="PT-BR"}

[ \<1, 1\>,         \<2, 3\>,         \<3, 2\>,         \<4, 5\>,         \<6, 4\>,]{lang="PT-BR"}

[ \<10, 9\>,        \<11, 6\>,        \<12, 7\>,        \<34, 23\>,       \<35, 35\>,]{lang="PT-BR"}

[ \<67, 67\>]{lang="PT-BR"}

[]{#struct_0_x2095_42796_x1353298281}[]{#_Toc299547455}[]{#_Toc297300298}[[表1-1 ]{lang="PT-BR"}[display evb cdcp]{lang="EN-US"}]{#_Toc297132310}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_424434696}[[字段]{style="font-family:黑体"}]{#struct_0_x2095_42796_557245658}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2095_42796_454811680}

[[S-component capability]{lang="PT-BR"}]{#struct_0_x2095_42796_2126672591}

[[本端和对端对"端口映射的]{style="font-family:宋体"}[S-VLAN]{lang="EN-US"}]{#struct_0_x2095_42796_x273805104}[组件"技术的支持情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[support]{lang="PT-BR"}]{#struct_0_x2095_42796_x1921097516}[ed]{lang="PT-BR"}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[not support]{lang="PT-BR"}]{#struct_0_x2095_42796_3394951}[ed]{lang="PT-BR"}[：表示不支持]{lang="EN-US" style="font-family:宋体"}

[[Supported S-Channel numbers per-port]{lang="PT-BR"}]{#struct_0_x2095_42796_557311194}

[[本端和对端的接口下支持的]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x2095_42796_x1839157436}[通道数目]{style="font-family:宋体"}

[[SVID range]{lang="PT-BR"}]{#struct_0_x2095_42796_x1324976999}

[[本端可分配的]{style="font-family:宋体"}[SVID]{lang="EN-US"}]{#struct_0_x2095_42796_365360375}[范围]{style="font-family:宋体"}

[[SCID requested from remote]{lang="PT-BR"}]{#struct_0_x2095_42796_x738738428}

[[对端请求的]{style="font-family:宋体"}[SCID]{lang="EN-US"}]{#struct_0_x2095_42796_821004171}[（由小到大排序）]{style="font-family:宋体"}

[[SCID/SVID pair list allocated]{lang="PT-BR"}]{#struct_0_x2095_42796_557638874}

[[本端分配的]{style="font-family:宋体"}[\<SCID]{lang="EN-US"}]{#struct_0_x2095_42796_x966361271}[，]{style="font-family:宋体"}[SVID\>]{lang="EN-US"}[对]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1664780658 .myid}
[]{#_Toc404798163}[]{#struct_0_x2095_42796_x1491430011}

**EVB \-- EVB配置命令 \-- display evb evb-tlv**

------------------------------------------------------------------------

[**[display evb evb-tlv]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1313517860}[命令用来显示]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:宋体"}[EVB TLV]{lang="PT-BR"}[协商信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1841703856}

[**[display evb evb-tlv ]{lang="EN-US"}**[\[ **interface** *interface-type* { *interface-number* \| *interface-number*:]{lang="EN-US"}]{#struct_0_x2095_42796_1737438074}*[channel-id]{lang="PT-BR"}*[ } ]{lang="PT-BR"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1771354477}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_1605109654}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557704410}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_996079214}

[[network-operator]{lang="EN-US"}]{#struct_0_x2095_42796_x1881974099}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_185242620}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2095_42796_2144823531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x405487179}

[**[interface]{lang="PT-BR"}**]{#struct_0_x2095_42796_2017480504}[：显示指定接口上的信息。如果未指定本参数，将显示所有已使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能的接口上的信息。]{style="font-family:宋体"}

[*[interface-type ]{lang="PT-BR"}*]{#struct_0_x2095_42796_x774506200}[{ *interface-number* \| *interface-number*:*channel-id* }]{lang="PT-BR"}[：表示]{style="font-family:
宋体"}[二层以太网接口、]{style="font-family:宋体"}[二层聚合接口、]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口。]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type]{lang="PT-BR"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为接口编号，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号。]{style="font-family:
宋体"}[对于]{style="font-family:宋体"}[二层以太网接口和]{style="font-family:
宋体"}[二层聚合接口，接口编号为]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[的形式；对于]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口和]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口，接口编号为]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[:*channel-id*]{lang="PT-BR"}[的形式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1379811839}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_557507802}[显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:
宋体"}[EVB TLV]{lang="PT-BR"}[协商信息。]{style="font-family:宋体"}

[[\<Sysname\> display evb evb-tlv interface gigabitethernet 1/0/1]{lang="PT-BR"}]{#struct_0_x2095_42796_557573338}

[ ]{lang="PT-BR"}

[S-Channel1/0/1:1]{lang="PT-BR"}

[EVB mode                       : Local-bridge/Remote-station]{lang="PT-BR"}

[BGID status                    : Supported]{lang="PT-BR"}

[Local RR capability            : Supported]{lang="PT-BR"}

[Local RR status                : Disabled]{lang="PT-BR"}

[Remote SGID status             : Not supported]{lang="PT-BR"}

[Remote RR request status       : Not requested]{lang="PT-BR"}

[Remote RR status               : Unknown]{lang="PT-BR"}

[Max ECP retry time             : Local-3/Remote-NA/Operative-3]{lang="PT-BR"}

[ULPDU retransmission exponent  : Local-16/Remote-NA/Operative-16]{lang="PT-BR"}

[Resource wait-delay exponent   : Local-20/Remote-NA/Operative-20]{lang="PT-BR"}

[Reinit Keep-alive exponent     : Local-25/Remote-NA/Operative-25]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[S-Channel1/0/1:100]{lang="PT-BR"}

[EVB mode                       : Local-bridge/Remote-station]{lang="PT-BR"}

[BGID status                    : Supported]{lang="PT-BR"}

[Local RR capability            : Supported]{lang="PT-BR"}

[Local RR status                : Disabled]{lang="PT-BR"}

[Remote SGID status             : Not supported]{lang="PT-BR"}

[Remote RR request status       : Not requested]{lang="PT-BR"}

[Remote RR status               : Unknown]{lang="PT-BR"}

[Max ECP retry time             : Local-3/Remote-NA/Operative-3]{lang="PT-BR"}

[ULPDU retransmission exponent  : Local-16/Remote-NA/Operative-16]{lang="PT-BR"}

[Resource wait-delay exponent   : Local-20/Remote-NA/Operative-20]{lang="PT-BR"}

[Reinit keep-alive exponent     : Local-25/Remote-NA/Operative-25]{lang="PT-BR"}

[]{#struct_0_x2095_42796_1507432764}[]{#_Toc299547454}[]{#_Toc297300297}[[表1-2 ]{lang="EN-US"}[display evb evb-tlv]{lang="PT-BR"}]{#_Toc297132309}[命令]{style="font-family:黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_420487080}[[字段]{style="font-family:黑体"}]{#struct_0_x2095_42796_190855725}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2095_42796_348356885}

[[EVB mode]{lang="PT-BR"}]{#struct_0_x2095_42796_890686074}

[[本地和对端的]{style="font-family:宋体"}[EVB]{lang="EN-US"}]{#struct_0_x2095_42796_x266912129}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bridge]{lang="PT-BR"}]{#struct_0_x2095_42796_x1527837987}[：表示]{lang="EN-US" style="font-family:宋体"}[EVB]{lang="EN-US"}[交换机]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[station]{lang="PT-BR"}]{#struct_0_x2095_42796_557901018}[：表示]{lang="EN-US" style="font-family:宋体"}[EVB]{lang="EN-US"}[服务器]{style="font-family:宋体"}

[[BGID status]{lang="PT-BR"}]{#struct_0_x2095_42796_x742251510}

[[本端是否支持]{style="font-family:宋体"}[Group ID]{lang="EN-US"}]{#struct_0_x2095_42796_x1485339321}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="PT-BR"}]{#struct_0_x2095_42796_1680428863}[upport]{lang="PT-BR"}[ed]{lang="PT-BR"}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not support]{lang="PT-BR"}]{#struct_0_x2095_42796_x300887533}[ed]{lang="PT-BR"}[：表示]{lang="EN-US" style="font-family:宋体"}[不]{style="font-family:宋体"}[支持]{lang="EN-US" style="font-family:宋体"}

[[Local RR capability]{lang="PT-BR"}]{#struct_0_x2095_42796_255610808}

[[本端是否支持]{style="font-family:宋体"}[RR]{lang="EN-US"}]{#struct_0_x2095_42796_557966554}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="PT-BR"}]{#struct_0_x2095_42796_x1895071075}[upport]{lang="PT-BR"}[ed]{lang="PT-BR"}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not support]{lang="PT-BR"}]{#struct_0_x2095_42796_1878770164}[ed]{lang="PT-BR"}[：表示]{lang="EN-US" style="font-family:宋体"}[不]{style="font-family:宋体"}[支持]{lang="EN-US" style="font-family:宋体"}

[[Local RR status]{lang="PT-BR"}]{#struct_0_x2095_42796_x152685396}

[[协商后本端的]{style="font-family:宋体"}[RR]{lang="EN-US"}]{#struct_0_x2095_42796_x2098811957}[模式]{style="font-family:宋体"}

[[Remote SGID status]{lang="PT-BR"}]{#struct_0_x2095_42796_856721106}

[[对端是否支持]{style="font-family:宋体"}[Group ID]{lang="EN-US"}]{#struct_0_x2095_42796_557376731}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="PT-BR"}]{#struct_0_x2095_42796_x1483576401}[upport]{lang="PT-BR"}[ed]{lang="PT-BR"}[：表示支持]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not support]{lang="PT-BR"}]{#struct_0_x2095_42796_x54382826}[ed]{lang="PT-BR"}[：表示]{lang="EN-US" style="font-family:宋体"}[不]{style="font-family:宋体"}[支持]{lang="EN-US" style="font-family:宋体"}

[[Remote RR request status]{lang="PT-BR"}]{#struct_0_x2095_42796_x578505049}

[[对端是否申请了]{style="font-family:宋体"}[RR]{lang="EN-US"}]{#struct_0_x2095_42796_414998580}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Requested]{lang="EN-US"}]{#struct_0_x2095_42796_557442267}[：表示已]{lang="EN-US" style="font-family:宋体"}[申请]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not requested]{lang="EN-US"}]{#struct_0_x2095_42796_1498156483}[：表示未]{lang="EN-US" style="font-family:宋体"}[申请]{style="font-family:宋体"}

[[Remote RR status]{lang="PT-BR"}]{#struct_0_x2095_42796_538657212}

[[协商后对端是否启用了]{style="font-family:宋体"}[RR]{lang="EN-US"}]{#struct_0_x2095_42796_x660505189}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x2095_42796_1277978675}[：表示已启用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x2095_42796_557245659}[：表示未启用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x2095_42796_454811681}[：表示未知]{style="font-family:宋体"}

[[Max ECP retry time]{lang="PT-BR"}]{#struct_0_x2095_42796_2126672592}

[[ECP]{lang="EN-US"}]{#struct_0_x2095_42796_x273870640}[最大重传次数，格式为：本端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[对端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[实际操作值，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示对端没有设置值]{style="font-family:宋体"}

[[ULPDU retransmission Eexponent]{lang="PT-BR"}]{#struct_0_x2095_42796_557311195}

[[ECP]{lang="EN-US"}]{#struct_0_x2095_42796_x1839157437}[重传时间指数因子，格式为：本端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[对端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[实际操作值，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示对端没有设置值]{style="font-family:宋体"}

[[Resource wait-delay exponent]{lang="PT-BR"}]{#struct_0_x2095_42796_1403906356}

[[VDP]{lang="EN-US"}]{#struct_0_x2095_42796_x1337717762}[等待应答时间指数因子，格式为：本端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[对端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[实际操作值，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示对端没有设置值]{style="font-family:宋体"}

[[Reinit keep-alive exponent]{lang="PT-BR"}]{#struct_0_x2095_42796_557638875}

[[VDP]{lang="EN-US"}]{#struct_0_x2095_42796_x966361272}[保活时间指数因子，格式为：本端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[对端协商值]{style="font-family:宋体"}[/]{lang="EN-US"}[实际操作值，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示对端没有设置值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-957537351 .myid}
[]{#_Toc404798164}[]{#struct_0_x2095_42796_x1491364475}

**EVB \-- EVB配置命令 \-- display evb s-channel**

------------------------------------------------------------------------

[**[display evb s-channel]{lang="EN-US"}**]{#struct_0_x2095_42796_x1752569497}[命令用来显示]{style="font-family:宋体"}[S]{lang="EN-US"}[通道信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x398154270}

[**[display evb s-channel]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2095_42796_2012215305}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x953199053}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_x821943744}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557704411}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_996079215}

[[network-operator]{lang="EN-US"}]{#struct_0_x2095_42796_x1881974098}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_1751326561}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2095_42796_x1961137773}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2061220105}

[**[interface]{lang="PT-BR"}**]{#struct_0_x2095_42796_1343768329}*[ interface-type interface-number]{lang="PT-BR"}*[：显示指定接口（二层以太网接口或二层聚合接口）上的信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="PT-BR"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有已使能]{style="font-family:
宋体"}[EVB]{lang="PT-BR"}[功能的接口上的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1523247183}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_557507803}[显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道信息。]{style="font-family:宋体"}

[[\<Sysname\> display evb s-channel interface gigabitethernet 1/0/1]{lang="PT-BR"}]{#struct_0_x2095_42796_387284781}

[RR status: D \-- Disabled, E \-- Enabled]{lang="PT-BR"}

[MAC learning: A \-- Allowed, F \-- Forbidden]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[S-Channel           SVID    Uptime               RR      MAC       VSI]{lang="PT-BR"}

[interface                   yyyy/mm/dd hh:mm:ss  status  learning  number]{lang="PT-BR"}

[S-Ch1/0/1:1         1       2012/12/17 03:43:13  D       A         0]{lang="PT-BR"}

[S-Ch1/0/1:100       100     2012/12/17 03:43:14  D       A         2]{lang="PT-BR"}

[]{#struct_0_x2095_42796_x100568541}[]{#_Toc299547451}[]{#_Toc298934613}[]{#_Toc297300294}[[表1-3 ]{lang="EN-US"}[display evb s-channel]{lang="EN-US"}]{#_Toc297132306}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_422452584}[[字段]{style="font-family:黑体"}]{#struct_0_x2095_42796_1170707999}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2095_42796_1270119334}

[[S-Channel interface]{lang="EN-US"}]{#struct_0_x2095_42796_x1361765516}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_557573339}[通道接口的名称]{style="font-family:宋体"}

[[SVID]{lang="EN-US"}]{#struct_0_x2095_42796_1507432763}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_190921261}[通道对应的]{style="font-family:宋体"}[S-VLAN]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_x2095_42796_381500149}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_612468751}[通道的创建时间]{style="font-family:宋体"}

[[RR status]{lang="EN-US"}]{#struct_0_x2095_42796_x148004709}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_x1052885506}[通道反射式转发模式的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x2095_42796_557901019}[：]{lang="EN-US" style="font-family:宋体"}[Disabled]{lang="EN-US"}[，表示关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x2095_42796_x742251509}[：]{lang="EN-US" style="font-family:宋体"}[Enabled]{lang="EN-US"}[，表示]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}

[[MAC learning]{lang="EN-US"}]{#struct_0_x2095_42796_x1485929146}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_1323167817}[通道的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习能力：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x2095_42796_x87245017}[：]{style="font-family:宋体"}[Allowed]{lang="EN-US"}[，表示允许学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x2095_42796_557966555}[：]{lang="EN-US" style="font-family:宋体"}[Forbidden]{lang="EN-US"}[，表示禁止]{lang="EN-US" style="font-family:宋体"}[学习]{style="font-family:宋体"}

[[VSI number]{lang="EN-US"}]{#struct_0_x2095_42796_x1895071074}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_x850113191}[通道上创建的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[数量]{style="font-family:宋体"}

[]{#_Toc311899218}[[ ]{lang="EN-US"}]{#_Toc311899221}

::: {#-537661407 .myid}
[]{#_Toc404798165}[]{#struct_0_x2095_42796_x857304018}

**EVB \-- EVB配置命令 \-- display evb summary**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **evb** **summary**]{lang="EN-US"}]{#struct_0_x2095_42796_x48422979}[命令用来显示]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[概要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1244916734}

[**[display]{lang="PT-BR"}**]{#struct_0_x2095_42796_x166220171}[ **evb** **summary**]{lang="PT-BR"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557376728}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_855075752}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x646377897}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_1282001404}

[[network-operator]{lang="PT-BR"}]{#struct_0_x2095_42796_x196678643}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_391217555}

[[mdc-operator]{lang="PT-BR"}]{#struct_0_x2095_42796_x1815651750}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1830456038}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_557442264}[显示]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[概要信息。]{style="font-family:宋体"}

[]{#_Toc299547456}[[\<Sysname\>]{lang="PT-BR"}[ ]{lang="PT-BR"}[display evb summary]{lang="EN-US"}]{#struct_0_x2095_42796_1498156480}

[Default manager ID: 192.168.1.1]{lang="PT-BR"}

[Port number: 80]{lang="PT-BR"}

[Interface               S-Channel number        VSI number]{lang="PT-BR"}

[GE1/0/1                 2                       2]{lang="PT-BR"}

[[表1-4 ]{lang="EN-US"}[display evb summary]{lang="EN-US"}]{#struct_0_x2095_42796_538460604}[命令]{style="font-family:黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_452227944}[[字段]{style="font-family:黑体"}]{#struct_0_x2095_42796_x943501202}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1721203254}

[[Default manager ID]{lang="PT-BR"}]{#struct_0_x2095_42796_x661651361}

[[默认]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_x257386974}[管理服务器]{style="font-family:宋体"}[的地址或名称，]{style="font-family:宋体"}[Not configured]{lang="PT-BR"}[表示没有配置]{style="font-family:宋体"}

[[Port number]{lang="PT-BR"}]{#struct_0_x2095_42796_557245656}

[[默认]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_454811694}[管理服务器的端口编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[Not configured]{lang="PT-BR"}[表示没有配置]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2095_42796_170357451}

[[使能了]{style="font-family:宋体"}]{#struct_0_x2095_42796_601683377}[EVB]{lang="PT-BR"}[功能的]{style="font-family:宋体"}[接口名称]{style="font-family:宋体"}

[[S-Channel number]{lang="PT-BR"}]{#struct_0_x2095_42796_1150520022}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_x11459476}[通道的数量]{style="font-family:宋体"}

[[VSI number]{lang="EN-US"}]{#struct_0_x2095_42796_557311192}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_x1839157430}[接口的数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1745887635 .myid}
[]{#_Toc404798166}[]{#struct_0_x2095_42796_1807190883}

**EVB \-- EVB配置命令 \-- display evb vsi**

------------------------------------------------------------------------

[**[display evb vsi]{lang="EN-US"}**]{#struct_0_x2095_42796_x1204411453}[命令用来显示]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1054882265}

[**[display evb vsi]{lang="EN-US"}**[ \[ **verbose** \] \[ **interface** *interface-type* { *interface-number* \| *interface-number*:]{lang="EN-US"}]{#struct_0_x2095_42796_x832816423}*[channel-id]{lang="PT-BR"}*[ ]{lang="PT-BR"}*[\| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id*]{lang="EN-US"}[ ]{lang="EN-US"}[} ]{lang="PT-BR"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x681510429}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_1598440652}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557638872}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_x966361269}

[[network-operator]{lang="EN-US"}]{#struct_0_x2095_42796_x1490905724}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_241667460}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2095_42796_457362258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_58067447}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2095_42796_1386669596}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[**[interface]{lang="PT-BR"}**]{#struct_0_x2095_42796_x649902342}[：显示指定接口上的信息。如果未指定本参数，将显示所有已使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能的接口上的信息。]{style="font-family:宋体"}

[*[interface-type ]{lang="PT-BR"}*]{#struct_0_x2095_42796_1823090808}[{ *interface-number* \| *interface-number*:*channel-id* *\| interface-number*:*channel-id*.*vsi-local-id* }]{lang="PT-BR"}[：表示]{style="font-family:宋体"}[二层以太网接口、]{style="font-family:宋体"}[二层聚合接口、]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口、]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口、]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口。]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type]{lang="PT-BR"}*[为接口类型，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为接口编号，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号，]{style="font-family:
宋体"}*[vsi-local-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号。]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[二层以太网接口和]{style="font-family:宋体"}[二层聚合接口，接口编号为]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[的形式；对于]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口和]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口，接口编号为]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[:*channel-id*]{lang="PT-BR"}[的形式；对于]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口和]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口，接口编号为]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[:*channel-id*.*vsi-local-id*]{lang="PT-BR"}[的形式。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557704408}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x960235914}[显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上的]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display evb vsi interface gigabitethernet 1/0/1]{lang="PT-BR"}]{#struct_0_x2095_42796_468674472}

[Status: A \-- Association, P \-- Pre-association]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[VSI                     VTID     Type      Instance                Status]{lang="PT-BR"}

[interface                        version   ID]{lang="PT-BR"}

[S-Ch1/0/1:100.0         NA       NA        NA                      P]{lang="PT-BR"}

[S-Ch1/0/1:100.1         NA       NA        NA                      A]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x389270211}[显示端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上的]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display evb vsi verbose interface gigabitethernet 1/0/1]{lang="PT-BR"}]{#struct_0_x2095_42796_557507800}

[S-Channel1/0/1:100]{lang="PT-BR"}

[ S-Channel1/0/1:100.0]{lang="PT-BR"}

[  VSI local-ID: 0           VSI type ID: NA         VSI type version: NA]{lang="PT-BR"}

[  VSI instance ID: NA]{lang="PT-BR"}

[  VSI manager ID: NA]{lang="PT-BR"}

[  Current VDP status: Pre-association]{lang="PT-BR"}

[  Filter type: VID]{lang="PT-BR"}

[  Filter info:]{lang="PT-BR"}

[  \<100\>]{lang="PT-BR"}

[ S-Channel1/0/1:100.1]{lang="PT-BR"}

[  VSI local-ID: 1           VSI type ID: 100        VSI type version: 0]{lang="PT-BR"}

[  VSI instance ID: 11:2233:4455:6677:8899:1234:5678:9010]{lang="PT-BR"}

[  VSI manager ID: NA]{lang="PT-BR"}

[  Current VDP status: Association]{lang="PT-BR"}

[  Filter type: MAC/VID]{lang="PT-BR"}

[  Filter info:]{lang="PT-BR"}

[  \<0011-2233-4455, 1000\>]{lang="PT-BR"}

[]{#struct_0_x2095_42796_387284778}[]{#_Toc299547453}[]{#_Toc297300296}[[表1-5 ]{lang="EN-US"}[display evb vsi]{lang="EN-US"}]{#_Toc297132308}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_446010536}[[字段]{style="font-family:黑体"}]{#struct_0_x2095_42796_x909872612}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2095_42796_380176559}

[[VSI interface]{lang="EN-US"}]{#struct_0_x2095_42796_x1619631477}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_557573336}[接口的名称]{style="font-family:宋体"}

[[VTID/VSI type ID]{lang="EN-US"}]{#struct_0_x2095_42796_1507432774}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_190855726}[类型编号，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未指定]{style="font-family:宋体"}

[[Type version/VSI type version]{lang="EN-US"}]{#struct_0_x2095_42796_348356882}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_890686079}[类型版本号，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未指定]{style="font-family:宋体"}

[[Instance ID/VSI instance ID]{lang="EN-US"}]{#struct_0_x2095_42796_x266912140}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_557901016}[实例编号，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未指定]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2095_42796_x742251520}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_x1485339324}[接口的当前状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x2095_42796_1277144336}[：]{lang="EN-US" style="font-family:宋体"}[即]{style="font-family:宋体"}[Association]{lang="EN-US"}[，表示关联属性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x2095_42796_951977811}[：]{lang="EN-US" style="font-family:宋体"}[即]{style="font-family:宋体"}[Pre-association]{lang="EN-US"}[，表示预关联属性]{lang="EN-US" style="font-family:宋体"}

[[VSI local-ID]{lang="EN-US"}]{#struct_0_x2095_42796_473941954}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_557966552}[本地编号]{style="font-family:宋体"}

[[VSI manager ID]{lang="EN-US"}]{#struct_0_x2095_42796_x1895071081}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_x447549560}[管理服务器的地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未指定]{style="font-family:宋体"}

[[Current VDP status]{lang="EN-US"}]{#struct_0_x2095_42796_182200996}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_x461943463}[接口的当前状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Association]{lang="EN-US"}]{#struct_0_x2095_42796_557376729}[：]{style="font-family:宋体"}[表示关联属性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pre-association]{lang="EN-US"}]{#struct_0_x2095_42796_855075751}[：]{style="font-family:宋体"}[表示预关联属性]{lang="EN-US" style="font-family:宋体"}

[[Filter type]{lang="EN-US"}]{#struct_0_x2095_42796_x646377894}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_1281804796}[过滤信息的类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GroupID/VID]{lang="EN-US"}]{#struct_0_x2095_42796_1472320085}[：表示]{style="font-family:宋体"}[Group ID]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[的组合]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GroupID/MAC/VID]{lang="EN-US"}]{#struct_0_x2095_42796_x110807774}[：表示]{style="font-family:宋体"}[Group ID]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[的组合]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VID]{lang="EN-US"}]{#struct_0_x2095_42796_x2039920419}[：表示]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC/VID]{lang="EN-US"}]{#struct_0_x2095_42796_557442265}[：表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[的组合]{style="font-family:宋体"}

[[Filter info]{lang="EN-US"}]{#struct_0_x2095_42796_1498156481}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_538526140}[过滤信息的具体内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#186680629 .myid}
[]{#_Toc404798167}[]{#struct_0_x2095_42796_454811695}[]{#_Toc296504298}[]{#_Toc267327363}

**EVB \-- EVB配置命令 \-- display interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_x2095_42796_170357452}[命令用来显示]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/]{lang="EN-US"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_601683380}

[**[display]{lang="EN-US"}**[ **interface** \[ { ]{lang="EN-US"}]{#struct_0_x2095_42796_x759617346}**[s-channel]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| **schannel-aggregation** } ]{lang="PT-BR"}[\[ *interface-number*:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}[ \| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x2143567215}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_325647820}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1587724779}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_557311193}

[[network-operator]{lang="EN-US"}]{#struct_0_x2095_42796_x1839157431}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_241106942}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2095_42796_x1879103261}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_390137556}

[**[s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1822924280}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[**[schannel-aggregation]{lang="PT-BR"}**]{#struct_0_x2095_42796_x969667423}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[*[interface-number]{lang="PT-BR"}*]{#struct_0_x2095_42796_x2062790207}[:*channel-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口的编号]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道所在接口的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号。]{style="font-family:
宋体"}

[*[interface-number]{lang="PT-BR"}*]{#struct_0_x2095_42796_x1488891680}[:*channel-id*.*vsi-local-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口的编号]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道所在接口的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[vsi-local-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x2095_42796_1466472372}[：显示概要信息。如果未指定本参数，将显示详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x2095_42796_x966361270}[：当用户配置的接口描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不会显示。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x2095_42796_x500360504}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果未指定本参数，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1491495547}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定接口类型，将显示设备支持的所有接口的信息。]{style="font-family:宋体"}]{#struct_0_x2095_42796_1976824957}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了接口类型而未指定接口编号，将显示所有已创建的]{style="font-family:宋体"}]{#struct_0_x2095_42796_x155253138}[S]{lang="EN-US"}[通道接口和]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x646212589}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_1204103021}[显示]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ]{lang="EN-US"}]{#struct_0_x2095_42796_557704409}[s-channel 1/0/1:10]{lang="PT-BR"}

[S-Channel]{lang="EN-US"}[1/0/1:10]{lang="PT-BR"}

[Current state: UP]{lang="EN-US"}

[IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 000c-29f9-366e]{lang="EN-US"}

[Description: S-Channel]{lang="EN-US"}[1/0/1:10]{lang="PT-BR"}[ Interface]{lang="EN-US"}

[Bandwidth: 1000000kbps]{lang="EN-US"}

[Unknown-speed mode, unknown-duplex mode]{lang="EN-US"}

[Link speed type is autonegotiation, link duplex type is autonegotiation]{lang="EN-US"}

[PVID: 1]{lang="EN-US"}

[Port link-type: trunk]{lang="EN-US"}

[ VLAN Passing:   1(default vlan), 2]{lang="EN-US"}

[ VLAN permitted: 1(default vlan), 2]{lang="EN-US"}

[ Trunk port encapsulation: IEEE 802.1q]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Input (total):  6 packets, 384 bytes]{lang="EN-US"}

[Output (total):  18 packets, 1152 bytes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x960235913}[显示]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ]{lang="EN-US"}]{#struct_0_x2095_42796_468215720}[s-channel 1/0/1:10 brief]{lang="PT-BR"}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Speed or Duplex: (a)/A - auto; H - half; F - full]{lang="EN-US"}

[Type: A - access; T - trunk; H - hybrid]{lang="EN-US"}

[Interface            Link Speed   Duplex Type PVID Description]{lang="EN-US"}

[S-Ch1/0/1:10]{lang="PT-BR"}[         UP   10G(a)  F(a)   A    1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_557507801}[显示]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ]{lang="EN-US"}]{#struct_0_x2095_42796_387284779}[s-channel 1/0/1:10.1]{lang="PT-BR"}

[S-Channel]{lang="EN-US"}[1/0/1:10.1]{lang="PT-BR"}

[Current state: UP]{lang="EN-US"}

[IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 000c-29f9-366e]{lang="EN-US"}

[Description: S-Channel]{lang="EN-US"}[1/0/1:10.1]{lang="PT-BR"}[ Interface]{lang="EN-US"}

[Bandwidth: 1000000kbps]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x909872613}[显示]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ]{lang="EN-US"}]{#struct_0_x2095_42796_380111023}[s-channel 1/0/1:10.1 brief]{lang="PT-BR"}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Speed or Duplex: (a)/A - auto; H - half; F - full]{lang="EN-US"}

[Type: A - access; T - trunk; H - hybrid]{lang="EN-US"}

[Interface            Link Speed   Duplex Type PVID Description]{lang="EN-US"}

[S-Ch1/0/1:10.1]{lang="PT-BR"}[       UP   \--      \--     \--   \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_1121655628}[显示所有物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口和]{style="font-family:
宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ]{lang="EN-US"}]{#struct_0_x2095_42796_557573337}[s-channel brief down]{lang="PT-BR"}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[S-Ch1/0/1:11]{lang="PT-BR"}[         DOWN Not connected]{lang="EN-US"}

[S-Ch1/0/1:11.1]{lang="PT-BR"}[       DOWN Not connected]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display interface ]{lang="EN-US"}]{#struct_0_x2095_42796_1507432773}[s-channel]{lang="PT-BR"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_447527752}[[字段]{style="font-family:黑体"}]{#struct_0_x2095_42796_190921262}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2095_42796_381500148}

[[Current state]{lang="EN-US"}]{#struct_0_x2095_42796_612468752}

[[接口的状态：]{style="font-family:宋体"}]{#struct_0_x2095_42796_x148004712}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively DOWN]{lang="EN-US"}]{#struct_0_x2095_42796_557901017}[：表示管理状态为关闭]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2095_42796_x742251519}[：表示管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2095_42796_x1485929145}[：表示管理状态和物理状态均为开启]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_x2095_42796_x242916124}

[[IP]{lang="EN-US"}]{#struct_0_x2095_42796_x2136582641}[报文的帧格式]{style="font-family:宋体"}

[[Hardware Address]{lang="EN-US"}]{#struct_0_x2095_42796_1972788197}

[[接口的硬件地址]{style="font-family:宋体"}]{#struct_0_x2095_42796_557966553}

[[Description]{lang="EN-US"}]{#struct_0_x2095_42796_x1895071080}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x2095_42796_1118534381}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x2095_42796_1935005430}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x2095_42796_2086587925}

[[Unknown-speed mode, unknown-duplex mode]{lang="EN-US"}]{#struct_0_x2095_42796_557376726}

[[接口的速率和双工模式均未知]{style="font-family:宋体"}]{#struct_0_x2095_42796_855075762}

[[Link speed type is autonegotiation, link duplex type is autonegotiation]{lang="EN-US"}]{#struct_0_x2095_42796_927600215}

[[接口的速率和双工模式都是通过自协商确定的]{style="font-family:宋体"}]{#struct_0_x2095_42796_x224511032}

[[PVID]{lang="EN-US"}]{#struct_0_x2095_42796_x2003208749}

[[接口缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2095_42796_557442262}[的编号]{style="font-family:宋体"}

[[Port link-type]{lang="EN-US"}]{#struct_0_x2095_42796_1498156478}

[[接口的链路类型]{style="font-family:宋体"}]{#struct_0_x2095_42796_537936327}

[[Trunk port encapsulation]{lang="EN-US"}]{#struct_0_x2095_42796_561879240}

[[Trunk]{lang="EN-US"}]{#struct_0_x2095_42796_x214037615}[端口的封装类型]{style="font-family:宋体"}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x2095_42796_557245654}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2095_42796_454811692}[命令清除接口统计信息的时间。]{style="font-family:宋体"}[Never]{lang="EN-US"}[表示设备启动后从未清除过]{style="font-family:宋体"}

[[Input (total):  6 packets, 384 bytes]{lang="EN-US"}]{#struct_0_x2095_42796_170357457}

[[接口接收的报文总数和字节总数]{style="font-family:宋体"}]{#struct_0_x2095_42796_601683375}

[[Output (total):  18 packets, 1152 bytes]{lang="EN-US"}]{#struct_0_x2095_42796_557311190}

[[接口发送的报文总数和字节总数]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1839157432}

[[Brief information on interface(s) under bridge mode]{lang="EN-US"}]{#struct_0_x2095_42796_644391469}

[[二层接口的概要信息]{style="font-family:宋体"}]{#struct_0_x2095_42796_2006930563}

[[Interface]{lang="EN-US"}]{#struct_0_x2095_42796_557638870}

[[接口名称的缩写]{style="font-family:宋体"}]{#struct_0_x2095_42796_x966361267}

[[Link]{lang="EN-US"}]{#struct_0_x2095_42796_x1491036796}

[[接口的物理连接状态：]{style="font-family:宋体"}]{#struct_0_x2095_42796_x278096418}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2095_42796_557704406}[：表示接口在物理上连通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2095_42796_x960235924}[：表示]{lang="EN-US" style="font-family:宋体"}[接口在物理上]{style="font-family:宋体"}[不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x2095_42796_468674471}[：表示接口被手工关闭，需执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}[命令才能打开]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x2095_42796_x389270208}[：表示接口为备份接口，可使用]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **interface-backup** **state**]{lang="EN-US"}[命令查看其主接口]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_x2095_42796_557507798}

[[接口的速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}]{#struct_0_x2095_42796_1929997073}

[[Duplex]{lang="EN-US"}]{#struct_0_x2095_42796_x1066156511}

[[接口的双工模式：]{style="font-family:宋体"}]{#struct_0_x2095_42796_1693707647}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[(a)/A]{lang="EN-US"}]{#struct_0_x2095_42796_557573334}[：表示速率和双工模式都]{lang="EN-US" style="font-family:宋体"}[由]{style="font-family:宋体"}[自协商确定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x2095_42796_1507432776}[：表示双工模式为半双工]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x2095_42796_190724654}[：表示双工模式为全双工]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x2095_42796_557901014}

[[接口的链路类型：]{style="font-family:宋体"}]{#struct_0_x2095_42796_x742251522}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x2095_42796_x1485470396}[：表示]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x2095_42796_x447491710}[：表示]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x2095_42796_557966550}[：表示]{lang="EN-US" style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x2095_42796_x1895071079}

[[接口物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x2095_42796_x90598304}[的原因：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_x2095_42796_557376727}[：表示链路被手工关闭（]{lang="EN-US" style="font-family:
  宋体"}[通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需执行]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}[命令才能恢复]{lang="EN-US" style="font-family:宋体"}[其]{style="font-family:宋体"}[真实物理状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_x2095_42796_855075761}[：表示没有物理连接（]{lang="EN-US" style="font-family:宋体"}[因未]{style="font-family:宋体"}[插网线或网线故障）]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_927600218}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2095_42796_x224511027}

::: {#385220866 .myid}
[]{#_Toc404798168}[]{#struct_0_x2095_42796_x2002881070}

**EVB \-- EVB配置命令 \-- evb default-manager**

------------------------------------------------------------------------

[**[evb default-manager]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x2095_42796_x1594106423}[命令用来指定默认]{style="font-family:宋体"}[VSI]{lang="EN-US"}[管理服务器。]{style="font-family:宋体"}

[**[undo evb default-manager]{lang="EN-US"}**]{#struct_0_x2095_42796_557442263}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1498156479}

[**[evb default-manager]{lang="EN-US"}**[ { { **ip** *ip-address* \| **ipv6** *ipv6-address* \| **name** *name* } \[ **port** *port-number* \] \| **local-server** }]{lang="EN-US"}]{#struct_0_x2095_42796_538001863}

[**[undo evb default-manager]{lang="PT-BR"}**]{#struct_0_x2095_42796_147702167}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1625014385}

[[未指定默认]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_74408299}[管理服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1921889074}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1959521521}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x932768190}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_557245655}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_454811693}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_170357458}

[**[ip]{lang="PT-BR"}**]{#struct_0_x2095_42796_601683386}[ *ip-address*]{lang="PT-BR"}[：]{style="font-family:宋体"}[指定默认]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器的]{style="font-family:宋体"}[IPv4]{lang="PT-BR"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="PT-BR"}**]{#struct_0_x2095_42796_430475989}[ *ipv6-address*]{lang="PT-BR"}[：]{style="font-family:宋体"}[指定默认]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器的]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}[地址。]{style="font-family:宋体"}

[**[name]{lang="PT-BR"}**]{#struct_0_x2095_42796_1196697782}[ *name*]{lang="PT-BR"}[：]{style="font-family:宋体"}[指定默认]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器的名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[name]{lang="PT-BR"}*[为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:
宋体"}[127]{lang="PT-BR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[**[port]{lang="PT-BR"}**]{#struct_0_x2095_42796_1507380494}[ *port-number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[指定默认]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器的端口]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[port-number]{lang="PT-BR"}*[为端口编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="PT-BR"}[～]{style="font-family:宋体"}[65535]{lang="PT-BR"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[8080]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[local-server]{lang="EN-US"}**]{#struct_0_x2095_42796_x241884157}[：]{style="font-family:宋体"}[指定本设备为默认]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x855097503}

[[当交换机收到服务器发来的]{style="font-family:宋体"}[VDP]{lang="EN-US"}]{#struct_0_x2095_42796_557311191}[报文（不包括去关联请求报文）时，需要与]{style="font-family:宋体"}[VSI]{lang="EN-US"}[管理服务器进行通信以申请]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口的资源和策略。]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[VSI manager ID TLV]{lang="EN-US"}[用于携带]{style="font-family:宋体"}[VSI]{lang="EN-US"}[管理服务器的地址，如果交换机收到的]{style="font-family:宋体"}[VDP]{lang="EN-US"}[报文中此]{style="font-family:宋体"}[TLV]{lang="EN-US"}[为全]{style="font-family:宋体"}[0]{lang="EN-US"}[（即未携带]{style="font-family:宋体"}[VSI]{lang="EN-US"}[管理服务器的地址），则使用通过本命令指定的默认]{style="font-family:宋体"}[VSI]{lang="EN-US"}[管理服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1839157433}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x921692472}[指定]{style="font-family:宋体"}[默认]{style="font-family:宋体"}[VSI]{lang="EN-US"}[管理服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[为]{style="font-family:宋体"}[192.168.100.20]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_659483345}

[\[Sysname\] evb default-manager ip 192.168.100.20]{lang="PT-BR"}
:::

::: {#743578633 .myid}
[]{#_Toc404798169}[]{#struct_0_x2095_42796_225042017}[]{#_Toc311899209}

**EVB \-- EVB配置命令 \-- evb enable**

------------------------------------------------------------------------

[**[evb enable]{lang="EN-US"}**]{#struct_0_x2095_42796_x1904010989}[命令用来在接口上使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能。]{style="font-family:宋体"}

[**[undo evb enabl]{lang="EN-US"}**]{#struct_0_x2095_42796_865459631}**[e]{lang="PT-BR"}**[命令用来在接口上关闭]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1249148237}

[**[evb enable]{lang="PT-BR"}**]{#struct_0_x2095_42796_557638871}

[**[undo evb enable]{lang="PT-BR"}**]{#struct_0_x2095_42796_x966361268}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1490971260}

[[接口上的]{style="font-family:宋体"}]{#struct_0_x2095_42796_936425974}[EVB]{lang="PT-BR"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x407355043}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_1522743308}[/]{lang="PT-BR"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1270583631}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_1333307646}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_1961473897}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_557704407}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[不允许在聚合组的成员端口上使能]{style="font-family:宋体"}]{#struct_0_x2095_42796_x960235923}[EVB]{lang="PT-BR"}[功能或将已使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能的端口加入聚合组，否则系统将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[在接口上使能]{style="font-family:宋体"}]{#struct_0_x2095_42796_468215719}[EVB]{lang="PT-BR"}[功能之前，建议先将该接口上的所有配置都恢复为缺省情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2095_42796_x503595033}[接]{style="font-family:
宋体"}[口上使能]{style="font-family:宋体"}[EVB]{lang="EN-US"}[功能之后，该]{style="font-family:宋体"}[接]{style="font-family:宋体"}[口上将自动创建默认]{style="font-family:宋体"}[S]{lang="EN-US"}[通道（]{style="font-family:宋体"}[SCID]{lang="PT-BR"}[和]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[均为]{style="font-family:宋体"}[1]{lang="PT-BR"}[，对应]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[的链路类型为]{style="font-family:宋体"}[Access]{lang="EN-US"}[类型）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[在已使能]{style="font-family:宋体"}]{#struct_0_x2095_42796_749090890}[EVB]{lang="PT-BR"}[功能的接口上，不建议进行]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[配置或运行其它二层协议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[在接口上关闭]{style="font-family:宋体"}]{#struct_0_x2095_42796_x817784008}[EVB]{lang="PT-BR"}[功能之前，请先删除该接口上的所有非默认]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道，默认]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道将在关闭]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能时被自动删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[不要在同一接口上同时使能]{style="font-family:宋体"}]{#struct_0_x2095_42796_888710444}[EVB]{lang="PT-BR"}[功能和]{style="font-family:宋体"}[QinQ]{lang="PT-BR"}[功能，否则二者均将无法正常工作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[不要在同一接口上同时创建以太网服务实例和使能]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1948876839}[EVB]{lang="PT-BR"}[功能，否则二者均将无法正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1360683914}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x1355959974}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_557507799}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-GigabitEthernet1/0/1\] evb enable]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1929997074}[在二层聚合接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="PT-BR"}[上使能]{style="font-family:宋体"}[EVB]{lang="PT-BR"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x1065959903}

[\[Sysname\] interface bridge-aggregation 1]{lang="PT-BR"}

[\[Sysname-Bridge-Aggregation1\] evb enable]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x2040724498}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_275853965}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[qinq enable]{lang="PT-BR"}**]{#struct_0_x2095_42796_1722960116}[（二层技术]{style="font-family:宋体"}[-]{lang="PT-BR"}[以太网交换命令参考]{style="font-family:宋体"}[/QinQ]{lang="PT-BR"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[service-instance]{lang="PT-BR"}**]{#struct_0_x2095_42796_x737771583}[（]{style="font-family:宋体"}[MPLS]{lang="PT-BR"}[命令参考]{style="font-family:宋体"}[/VPLS]{lang="PT-BR"}[）]{style="font-family:宋体"}
:::

::: {#1513344170 .myid}
[]{#_Toc311899210}[]{#_Toc404798170}[]{#struct_0_x2095_42796_1121006263}[]{#_Toc311899211}

**EVB \-- EVB配置命令 \-- evb mac-learning forbidden**

------------------------------------------------------------------------

[**[evb mac-learning forbidden]{lang="EN-US"}**]{#struct_0_x2095_42796_x1034073424}[命令用来关闭]{style="font-family:
宋体"}[S]{lang="EN-US"}[通道的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习能力。]{style="font-family:宋体"}

[**[undo evb mac-learning forbidden]{lang="EN-US"}**]{#struct_0_x2095_42796_557573335}[命令用来]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[S]{lang="EN-US"}[通道的]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址]{style="font-family:宋体"}[学习能力]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1507432775}

[**[evb mac-learning forbidden]{lang="PT-BR"}**]{#struct_0_x2095_42796_190790190}

[**[undo evb mac-learning forbidden]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1044670626}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1728223468}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_x1236102668}[通道的]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址]{style="font-family:宋体"}[学习能力处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x140488091}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_x980896211}[通道接口视图]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1200804189}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_557901015}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x742251521}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1485404860}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[对于已关闭]{style="font-family:宋体"}]{#struct_0_x2095_42796_1989196776}[RR]{lang="PT-BR"}[模式的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道，请勿再关闭其]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习能力，否则可能导致相应的虚拟机流量不通。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[关闭了]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1353555828}[S]{lang="EN-US"}[通道的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习能力之后，源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知的报文将被丢弃。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[当使用]{style="font-family:宋体"}]{#struct_0_x2095_42796_x500819254}**[undo evb mac-learning forbidden]{lang="PT-BR"}**[命令]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址]{style="font-family:宋体"}[学习能力]{style="font-family:宋体"}[时，请确保该]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址学习功能也处于开启状态]{style="font-family:宋体"}[（即]{style="font-family:宋体"}**[mac-address]{lang="PT-BR"}**[ **mac-learning** **enable**]{lang="PT-BR"}[），否则可能导致该]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道内的]{style="font-family:宋体"}[流量不通。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1498598871}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1287566125}[在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[上关闭]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址学习能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x2022088701}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname-S-Channel1/0/1:10\] evb mac-learning forbidden]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1440770343}[在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[上关闭]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址学习能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_557966551}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\] evb mac-learning forbidden]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1895071078}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb reflective-relay]{lang="EN-US"}**]{#struct_0_x2095_42796_1475485637}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[mac-address]{lang="PT-BR"}**]{#struct_0_x2095_42796_x500688182}[ **mac-learning** **enable**]{lang="PT-BR"}[（二层技术]{style="font-family:宋体"}[-]{lang="PT-BR"}[以太网交换命令参考]{style="font-family:宋体"}[/MAC]{lang="PT-BR"}[地址表）]{style="font-family:宋体"}
:::

::: {#504801263 .myid}
[]{#_Toc404798171}[]{#struct_0_x2095_42796_1665307221}[]{#_Toc311899212}

**EVB \-- EVB配置命令 \-- evb reflective-relay**

------------------------------------------------------------------------

[**[evb reflective-relay]{lang="EN-US"}**]{#struct_0_x2095_42796_1803519017}[命令用来]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo evb reflective-relay]{lang="EN-US"}**]{#struct_0_x2095_42796_x201769797}[命令用来关闭]{style="font-family:
宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_455150337}

[**[evb reflective-relay]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1073565082}

[**[undo evb reflective-relay]{lang="PT-BR"}**]{#struct_0_x2095_42796_2123460671}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_392308706}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_2096215741}[通道的]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1393448521}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_291637815}[通道接口视图]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_244096212}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x218542892}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x1919751855}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1783554533}

[[通常，服务器和交换机之间通过]{style="font-family:宋体"}]{#struct_0_x2095_42796_2123526207}[EVB TLV]{lang="PT-BR"}[协商是否开启]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式。当服务器在]{style="font-family:宋体"}[EVB TLV]{lang="PT-BR"}[中申请开启]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式、且交换机也支持该模式时，系统将自动为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道开启]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式，并转化为交换机上相应的命令行；用户也可通过本命令进行手工配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1526645172}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x1707033671}[在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[上开启]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_1928564113}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname-S-Channel1/0/1:10\] evb reflective-relay]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_868245714}[在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口]{style="font-family:
宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[上开启]{style="font-family:宋体"}[RR]{lang="PT-BR"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x503583133}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\] evb reflective-relay]{lang="PT-BR"}
:::

::: {#-1213679268 .myid}
[]{#_Toc404798172}[]{#struct_0_x2095_42796_x785154904}

**EVB \-- EVB配置命令 \-- evb s-channel**

------------------------------------------------------------------------

[**[evb s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_2123329599}[命令用来在接口上创建]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道。]{style="font-family:宋体"}

[**[undo evb s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_1529233462}[命令用来在]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[上删除]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x307719692}

[**[evb s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1673983231}*[ channel-id]{lang="PT-BR"}*[ \[ **service-vlan** *svlan-id* \]]{lang="PT-BR"}

[**[undo evb s-channel]{lang="EN-US"}**[ *channel-id*]{lang="EN-US"}]{#struct_0_x2095_42796_951677876}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_621201341}

[[已使能]{style="font-family:宋体"}[EVB]{lang="EN-US"}]{#struct_0_x2095_42796_521177552}[功能的接口上只存在自动创建的默认]{style="font-family:宋体"}[S]{lang="EN-US"}[通道（]{style="font-family:宋体"}[SCID]{lang="PT-BR"}[和]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[均为]{style="font-family:宋体"}[1]{lang="PT-BR"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x2112138597}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1649530383}[/]{lang="PT-BR"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2123395135}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x1944598292}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x796548997}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x372014796}

[*[channel-id]{lang="PT-BR"}*]{#struct_0_x2095_42796_x193014786}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[SCID]{lang="PT-BR"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2]{lang="PT-BR"}[～]{style="font-family:宋体"}[167]{lang="PT-BR"}[（]{style="font-family:宋体"}[0]{lang="PT-BR"}[为保留的]{style="font-family:
宋体"}[SCID]{lang="PT-BR"}[，]{style="font-family:宋体"}[1]{lang="PT-BR"}[为]{style="font-family:宋体"}[默认的]{style="font-family:
宋体"}[SCID]{lang="PT-BR"}[，均不可配）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[svlan-id]{lang="PT-BR"}*]{#struct_0_x2095_42796_223082405}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[S-VLAN]{lang="PT-BR"}[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2]{lang="PT-BR"}[～]{style="font-family:宋体"}[4094]{lang="PT-BR"}[（]{style="font-family:宋体"}[1]{lang="PT-BR"}[为默认]{style="font-family:
宋体"}[S]{lang="PT-BR"}[通道所使用的]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[，不可配）]{style="font-family:宋体"}[。如果未指定本参数，系统将自动分配一个尚未被其它]{style="font-family:宋体"}[S]{lang="EN-US"}[通道使用的最小]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1990970069}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_x334893894}[通道通常由服务器和交换机之间通过]{style="font-family:宋体"}[CDCP]{lang="PT-BR"}[协议协商自动创建，系统会将自动创建的结果转化为交换机上相应的命令行；用户也可以通过本命令手工创建]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道。当自动创建和手工创建的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的]{style="font-family:宋体"}[\<SCID]{lang="EN-US"}[，]{style="font-family:宋体"}[SVID\>]{lang="EN-US"}[对]{style="font-family:宋体"}[冲突时，系统将优先采用自动创建的配置。]{style="font-family:宋体"}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_1836931001}[通道创建成功后，系统将自动创建对应的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口；删除]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的同时也将自动删除对应的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口。]{style="font-family:宋体"}[手工创建的]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[的链路类型为]{style="font-family:宋体"}[Access]{lang="EN-US"}[类型，而自动创建的]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[的链路类型则为]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_2123722815}[通道如果创建在二层以太网接口上，则其对应的接口称为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口；]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道如果创建在二层聚合接口上，则其对应的接口称为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2095_42796_x348188555}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[必须在已使能]{style="font-family:宋体"}]{#struct_0_x2095_42796_1852028320}[EVB]{lang="PT-BR"}[功能的接口上创建]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道，否则系统将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[手工创建]{style="font-family:宋体"}]{#struct_0_x2095_42796_x264975893}[S]{lang="PT-BR"}[通道时，不允许使用已被其它]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道占用的]{style="font-family:宋体"}[SCID]{lang="PT-BR"}[或]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[，否则系统将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[请避免自动创建]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1775605575}[/]{lang="PT-BR"}[删除]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道与手工创建]{style="font-family:宋体"}[/]{lang="PT-BR"}[删除]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道同时进行，否则可能造成]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道创建]{style="font-family:宋体"}[/]{lang="PT-BR"}[删除结果异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_997523658}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x858452357}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[SCID]{lang="PT-BR"}[为]{style="font-family:宋体"}[10]{lang="PT-BR"}[的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道，其]{style="font-family:
宋体"}[对应的]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[为]{style="font-family:宋体"}[5]{lang="PT-BR"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_2123788351}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-GigabitEthernet1/0/1\] evb s-channel 10 service-vlan 5]{lang="PT-BR"}

[]{#_Toc311899213}[]{#_Toc311899215}[]{#_Toc311899216}[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1927203867}[在二层聚合接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[SCID]{lang="PT-BR"}[为]{style="font-family:宋体"}[10]{lang="PT-BR"}[的]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道，其]{style="font-family:
宋体"}[对应的]{style="font-family:宋体"}[SVID]{lang="PT-BR"}[为]{style="font-family:宋体"}[5]{lang="PT-BR"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x2123460107}

[\[Sysname\] interface bridge-aggregation 1]{lang="PT-BR"}

[\[Sysname-Bridge-Aggregation1\] evb s-channel 10 service-vlan 5]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1645274881}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb enable]{lang="PT-BR"}**]{#struct_0_x2095_42796_232288675}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[interface]{lang="EN-US"}**]{#struct_0_x2095_42796_x139444954}
:::

::::: {#-620347954 .myid}
[]{#_Toc404798173}[]{#struct_0_x2095_42796_x691990486}

**EVB \-- EVB配置命令 \-- evb vdp timer keepalive exponent**

------------------------------------------------------------------------

[**[evb vdp timer keepalive exponent]{lang="EN-US"}**]{#struct_0_x2095_42796_x1408751983}[命令用来配置]{style="font-family:宋体"}[VDP]{lang="EN-US"}[保活时间指数因子。]{style="font-family:宋体"}

[**[undo evb vdp timer keepalive exponent]{lang="EN-US"}**]{#struct_0_x2095_42796_x1434167618}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2123591743}

[**[evb vdp timer keepalive exponent ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x2095_42796_763206689}

[**[undo evb vdp timer keepalive exponent]{lang="PT-BR"}**]{#struct_0_x2095_42796_1928401511}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_867280886}

[[VDP]{lang="PT-BR"}]{#struct_0_x2095_42796_x2137609531}[保活时间指数因子为]{style="font-family:宋体"}[20]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x249226263}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_2125616388}[/]{lang="PT-BR"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1450983011}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_2123657279}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_1183429385}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1788393799}

[*[value]{lang="PT-BR"}*]{#struct_0_x2095_42796_x1599085829}[：表示]{style="font-family:宋体"}[VDP]{lang="PT-BR"}[保活时间指数因子]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[14]{lang="PT-BR"}[～]{style="font-family:宋体"}[31]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x43853710}

[[VDP]{lang="EN-US"}]{#struct_0_x2095_42796_33784995}[保活时间＝]{style="font-family:宋体"}[1.5]{lang="EN-US"}[×]{style="font-family:宋体"}[ \[ 2^VDP^]{lang="EN-US"}^[保活时间指数因子]{style="font-family:宋体"}^[＋（]{style="font-family:宋体"}[2]{lang="EN-US"}[×]{style="font-family:宋体"}[ECP]{lang="EN-US"}[最大重传次数＋]{style="font-family:宋体"}[1]{lang="EN-US"}[）×]{style="font-family:宋体"}[2^ECP^]{lang="EN-US"}^[重传时间指数因子]{style="font-family:宋体"}^[ \] ]{lang="EN-US"}[×]{style="font-family:宋体"}[10]{lang="EN-US"}^[---]{style="font-family:宋体"}[5]{lang="EN-US"}^[（秒），]{style="font-family:宋体"}[用户在配置时可参考]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}[1-7]{lang="PT-BR"}]{lang="EN-US"}](?-620347954#_Ref319417533)[中的实际取值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](EVB命令.files/image001.png){border="0" width="48" height="27"}]{lang="EN-US"}]{#struct_0_x2095_42796_x611906663}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[]{#struct_0_x2095_42796_1894825013}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:\"KaiTi_GB2312\",\"serif\""}[1-7]{lang="PT-BR"}]{lang="EN-US"}](?-620347954#_Ref319417533)[在计算时分别采用]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[3]{lang="EN-US"}[和]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[14]{lang="EN-US"}[作为"]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[ECP]{lang="EN-US"}[最大重传次数"和"]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[ECP]{lang="EN-US"}[重传时间指数因子"的取值。但这两个值仅仅是未与服务器协商时，交换机上的缺省值。在实际应用中，这两个参数将取交换机与服务器通过]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[EVB TLV]{lang="EN-US"}[协商后的较大值，此时]{style="font-family:\"KaiTi_GB2312\",\"serif\""}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
\"KaiTi_GB2312\",\"serif\""}[1-7]{lang="PT-BR"}]{lang="EN-US"}](?-620347954#_Ref319417533)[可能失去参考价值。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}
:::

[ ]{lang="PT-BR"}

[]{#struct_0_x2095_42796_x358763147}[[表1-7 ]{lang="EN-US"}[VDP]{lang="EN-US"}]{#_Ref319417533}[保活时间取值对照表]{style="font-family:黑体"}

[]{#table_struct_0_440010888}[[VDP]{lang="PT-BR"}]{#struct_0_x2095_42796_2123984959}[保活时间指数因子]{style="font-family:黑体"}
:::::

[[计算值（秒）]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1901112411}

[[实际取值（秒）]{style="font-family:黑体"}]{#struct_0_x2095_42796_1483571705}

[[14]{lang="EN-US"}]{#struct_0_x2095_42796_x744690838}

[[1.96608]{lang="EN-US"}]{#struct_0_x2095_42796_1563496846}

[[2]{lang="EN-US"}]{#struct_0_x2095_42796_1101467365}

[[15]{lang="EN-US"}]{#struct_0_x2095_42796_2124050495}

[[2.21184]{lang="EN-US"}]{#struct_0_x2095_42796_247342936}

[[3]{lang="EN-US"}]{#struct_0_x2095_42796_x840757355}

[[16]{lang="EN-US"}]{#struct_0_x2095_42796_580176487}

[[2.70336]{lang="EN-US"}]{#struct_0_x2095_42796_1520428536}

[[3]{lang="EN-US"}]{#struct_0_x2095_42796_611899446}

[[17]{lang="EN-US"}]{#struct_0_x2095_42796_2123460672}

[[3.68640]{lang="EN-US"}]{#struct_0_x2095_42796_392374242}

[[4]{lang="EN-US"}]{#struct_0_x2095_42796_x1863314251}

[[18]{lang="EN-US"}]{#struct_0_x2095_42796_x504234473}

[[5.65248]{lang="EN-US"}]{#struct_0_x2095_42796_x1712078042}

[[6]{lang="EN-US"}]{#struct_0_x2095_42796_2123526208}

[[19]{lang="EN-US"}]{#struct_0_x2095_42796_x1527103924}

[[9.58464]{lang="EN-US"}]{#struct_0_x2095_42796_411014962}

[[10]{lang="EN-US"}]{#struct_0_x2095_42796_1312235520}

[[20]{lang="EN-US"}]{#struct_0_x2095_42796_1833788214}

[[17.44896]{lang="EN-US"}]{#struct_0_x2095_42796_2123329600}

[[18]{lang="EN-US"}]{#struct_0_x2095_42796_x808959953}

[[21]{lang="EN-US"}]{#struct_0_x2095_42796_x287503561}

[[33.17760]{lang="EN-US"}]{#struct_0_x2095_42796_1916063794}

[[34]{lang="EN-US"}]{#struct_0_x2095_42796_2123395136}

[[22]{lang="EN-US"}]{#struct_0_x2095_42796_x1944401684}

[[64.63488]{lang="EN-US"}]{#struct_0_x2095_42796_390812528}

[[65]{lang="EN-US"}]{#struct_0_x2095_42796_1526293064}

[[23]{lang="EN-US"}]{#struct_0_x2095_42796_x944795148}

[[127.54944]{lang="EN-US"}]{#struct_0_x2095_42796_2123722816}

[[128]{lang="EN-US"}]{#struct_0_x2095_42796_x348123019}

[[24]{lang="EN-US"}]{#struct_0_x2095_42796_1501142065}

[[253.37856]{lang="EN-US"}]{#struct_0_x2095_42796_x1410516326}

[[254]{lang="EN-US"}]{#struct_0_x2095_42796_2123788352}

[[25]{lang="EN-US"}]{#struct_0_x2095_42796_1927007259}

[[505.03680]{lang="EN-US"}]{#struct_0_x2095_42796_x2065383608}

[[506]{lang="EN-US"}]{#struct_0_x2095_42796_1270459921}

[[26]{lang="EN-US"}]{#struct_0_x2095_42796_2123591744}

[[1008.35328]{lang="EN-US"}]{#struct_0_x2095_42796_763403297}

[[1009]{lang="EN-US"}]{#struct_0_x2095_42796_x1735990067}

[[27]{lang="EN-US"}]{#struct_0_x2095_42796_2123657280}

[[2014.98624]{lang="EN-US"}]{#struct_0_x2095_42796_1182970622}

[[2015]{lang="EN-US"}]{#struct_0_x2095_42796_1673623113}

[[28]{lang="EN-US"}]{#struct_0_x2095_42796_2123984960}

[[4028.25216]{lang="EN-US"}]{#struct_0_x2095_42796_x1901702236}

[[4029]{lang="EN-US"}]{#struct_0_x2095_42796_x866686545}

[[29]{lang="EN-US"}]{#struct_0_x2095_42796_x2074354388}

[[8054.78400]{lang="EN-US"}]{#struct_0_x2095_42796_2124050496}

[[8055]{lang="EN-US"}]{#struct_0_x2095_42796_247539544}

[[30]{lang="EN-US"}]{#struct_0_x2095_42796_1288734128}

[[16107.84768]{lang="EN-US"}]{#struct_0_x2095_42796_2123460669}

[[16108]{lang="EN-US"}]{#struct_0_x2095_42796_391784417}

[[31]{lang="EN-US"}]{#struct_0_x2095_42796_x1681994336}

[[32213.97504]{lang="EN-US"}]{#struct_0_x2095_42796_2123526205}

[[32214]{lang="EN-US"}]{#struct_0_x2095_42796_x1526776244}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_618759721}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x1716865288}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上配置]{style="font-family:宋体"}[VDP]{lang="PT-BR"}[保活时间指数因子为]{style="font-family:宋体"}[23]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_2123329597}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[\[Sysname-GigabitEthernet1/0/1\] evb vdp timer keepalive exponent 23]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1529626678}[在二层聚合接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="PT-BR"}[上配置]{style="font-family:宋体"}[VDP]{lang="PT-BR"}[保活时间指数因子为]{style="font-family:宋体"}[23]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x678933918}

[\[Sysname\] interface bridge-aggregation 1]{lang="PT-BR"}

[\[Sysname-Bridge-Aggregation1\] evb vdp timer keepalive exponent 23]{lang="PT-BR"}

::: {#388226591 .myid}
[]{#_Toc404798174}[]{#struct_0_x2095_42796_x1106544771}

**EVB \-- EVB配置命令 \-- evb vdp timer resource-wait-delay exponent**

------------------------------------------------------------------------

[**[evb vdp timer resource-wait-delay exponent]{lang="EN-US"}**]{#struct_0_x2095_42796_x1910293512}[命令用来配置]{style="font-family:宋体"}[VDP]{lang="EN-US"}[等待应答时间指数因子。]{style="font-family:宋体"}

[**[undo evb vdp timer resource-wait-delay exponent]{lang="EN-US"}**]{#struct_0_x2095_42796_1921163152}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1790742935}

[**[evb vdp timer resource-wait-delay exponent]{lang="EN-US"}***[ value]{lang="EN-US"}*]{#struct_0_x2095_42796_x1982042350}

[**[undo evb vdp timer resource-wait-delay exponent]{lang="PT-BR"}**]{#struct_0_x2095_42796_x354373187}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2123395133}

[[VDP]{lang="PT-BR"}]{#struct_0_x2095_42796_x1944729364}[等待应答时间指数因子为]{style="font-family:宋体"}[20]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1741308789}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_966715592}[/]{lang="PT-BR"}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x275400515}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x485424514}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x505079979}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x498005521}

[*[value]{lang="PT-BR"}*]{#struct_0_x2095_42796_2123722813}[：表示]{style="font-family:宋体"}[VDP]{lang="PT-BR"}[等待应答时间指数因子]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[15]{lang="PT-BR"}[～]{style="font-family:宋体"}[31]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x347795339}

[[VDP]{lang="EN-US"}]{#struct_0_x2095_42796_2079830947}[等待应答时间＝]{style="font-family:宋体"}[2^VDP^]{lang="EN-US"}^[等待应答时间指数因子]{style="font-family:宋体"}^[×]{style="font-family:宋体"}[10]{lang="EN-US"}^[---]{style="font-family:宋体"}[5]{lang="EN-US"}^[（秒），]{style="font-family:宋体"}[用户在配置时可参考]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}[1-8]{lang="PT-BR"}]{lang="EN-US"}](?388226591#_Ref319417523)[中的实际取值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[]{#struct_0_x2095_42796_1281501058}[[表1-8 ]{lang="EN-US"}[VDP]{lang="EN-US"}]{#_Ref319417523}[等待应答时间取值对照表]{style="font-family:黑体"}

[]{#table_struct_0_464917512}[[VDP]{lang="EN-US"}]{#struct_0_x2095_42796_1083435879}[等待应答时间指数因子]{style="font-family:黑体"}
:::

[[计算值（秒）]{style="font-family:黑体"}]{#struct_0_x2095_42796_x2011054606}

[[实际取值（秒）]{style="font-family:黑体"}]{#struct_0_x2095_42796_x664087065}

[[15]{lang="EN-US"}]{#struct_0_x2095_42796_613306522}

[[0.32768]{lang="EN-US"}]{#struct_0_x2095_42796_2123788349}

[[1]{lang="EN-US"}]{#struct_0_x2095_42796_1927728156}

[[16]{lang="EN-US"}]{#struct_0_x2095_42796_x932980644}

[[0.65536]{lang="EN-US"}]{#struct_0_x2095_42796_664855284}

[[1]{lang="EN-US"}]{#struct_0_x2095_42796_237321297}

[[17]{lang="EN-US"}]{#struct_0_x2095_42796_x2099703435}

[[1.31072]{lang="EN-US"}]{#struct_0_x2095_42796_2123591741}

[[2]{lang="EN-US"}]{#struct_0_x2095_42796_763075617}

[[18]{lang="EN-US"}]{#struct_0_x2095_42796_1231491478}

[[2.62144]{lang="EN-US"}]{#struct_0_x2095_42796_1900060665}

[[3]{lang="EN-US"}]{#struct_0_x2095_42796_x1410784272}

[[19]{lang="EN-US"}]{#struct_0_x2095_42796_2123657277}

[[5.24288]{lang="EN-US"}]{#struct_0_x2095_42796_1182774025}

[[6]{lang="EN-US"}]{#struct_0_x2095_42796_86395263}

[[20]{lang="EN-US"}]{#struct_0_x2095_42796_x872801044}

[[10.48576]{lang="EN-US"}]{#struct_0_x2095_42796_x2053861788}

[[11]{lang="EN-US"}]{#struct_0_x2095_42796_2123984957}

[[21]{lang="EN-US"}]{#struct_0_x2095_42796_x1901505627}

[[20.97152]{lang="EN-US"}]{#struct_0_x2095_42796_1992089158}

[[21]{lang="EN-US"}]{#struct_0_x2095_42796_x1158463683}

[[22]{lang="EN-US"}]{#struct_0_x2095_42796_1034592476}

[[41.94304]{lang="EN-US"}]{#struct_0_x2095_42796_2124050493}

[[42]{lang="EN-US"}]{#struct_0_x2095_42796_247736152}

[[23]{lang="EN-US"}]{#struct_0_x2095_42796_x322653366}

[[83.88608]{lang="EN-US"}]{#struct_0_x2095_42796_1407606637}

[[84]{lang="EN-US"}]{#struct_0_x2095_42796_771755227}

[[24]{lang="EN-US"}]{#struct_0_x2095_42796_2123460670}

[[167.77216]{lang="EN-US"}]{#struct_0_x2095_42796_392243170}

[[168]{lang="EN-US"}]{#struct_0_x2095_42796_121217149}

[[25]{lang="EN-US"}]{#struct_0_x2095_42796_2123526206}

[[335.54432]{lang="EN-US"}]{#struct_0_x2095_42796_x1526710708}

[[336]{lang="EN-US"}]{#struct_0_x2095_42796_1117404874}

[[26]{lang="EN-US"}]{#struct_0_x2095_42796_1696323338}

[[671.08864]{lang="EN-US"}]{#struct_0_x2095_42796_2123329598}

[[672]{lang="EN-US"}]{#struct_0_x2095_42796_1529167926}

[[27]{lang="EN-US"}]{#struct_0_x2095_42796_1632026407}

[[1342.17728]{lang="EN-US"}]{#struct_0_x2095_42796_x1607848988}

[[1343]{lang="EN-US"}]{#struct_0_x2095_42796_2123395134}

[[28]{lang="EN-US"}]{#struct_0_x2095_42796_x1944532756}

[[2684.35456]{lang="EN-US"}]{#struct_0_x2095_42796_1847316576}

[[2685]{lang="EN-US"}]{#struct_0_x2095_42796_x1317828522}

[[29]{lang="EN-US"}]{#struct_0_x2095_42796_2123722814}

[[5368.70912]{lang="EN-US"}]{#struct_0_x2095_42796_x348254091}

[[5369]{lang="EN-US"}]{#struct_0_x2095_42796_1910390327}

[[30]{lang="EN-US"}]{#struct_0_x2095_42796_2123788350}

[[10737.41824]{lang="EN-US"}]{#struct_0_x2095_42796_1927138331}

[[10738]{lang="EN-US"}]{#struct_0_x2095_42796_x1313220456}

[[31]{lang="EN-US"}]{#struct_0_x2095_42796_2123591742}

[[21474.83648]{lang="EN-US"}]{#struct_0_x2095_42796_763272225}

[[21475]{lang="EN-US"}]{#struct_0_x2095_42796_1862067200}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1664582665}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_236141660}[在端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上配置]{style="font-family:宋体"}[VDP]{lang="PT-BR"}[等待应答时间指数因子为]{style="font-family:宋体"}[23]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_2123657278}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="PT-BR"}

[[\[Sysname-GigabitEthernet1/0/1\] evb vdp timer resource-wait-delay exponent 23]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1183494921}[在二层聚合接口]{style="font-family:宋体"}[Bridge-Aggregation1]{lang="PT-BR"}[上配置]{style="font-family:宋体"}[VDP]{lang="PT-BR"}[等待应答时间指数因子为]{style="font-family:宋体"}[23]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_1284655452}

[\[Sysname\] interface bridge-aggregation 1]{lang="PT-BR"}

[\[Sysname-Bridge-Aggregation1\] ]{lang="PT-BR"}[[evb vdp timer resource-wait-delay exponent 23]{lang="EN-US"}]{.TerminalDisplayChar}

::: {#-1855845048 .myid}
[]{#_Toc404798175}[]{#struct_0_x2095_42796_x379994574}

**EVB \-- EVB配置命令 \-- evb vsi**

------------------------------------------------------------------------

[**[evb vsi]{lang="EN-US"}**]{#struct_0_x2095_42796_944887115}[命令用来创建]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口。]{style="font-family:宋体"}

[**[undo evb vsi]{lang="EN-US"}**]{#struct_0_x2095_42796_781768452}[命令用来删除]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2084027623}

[**[evb vsi]{lang="EN-US"}**[ *vsi-local-id* { **association** \| **pre-association** }]{lang="EN-US"}]{#struct_0_x2095_42796_2123984958}

[**[undo evb vsi]{lang="EN-US"}**[ *vsi-local-id*]{lang="EN-US"}]{#struct_0_x2095_42796_x1901177947}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1885153718}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_1084108734}[通道中不存在任何]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_614388346}

[[S]{lang="PT-BR"}]{#struct_0_x2095_42796_2042213052}[通道接口视图]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_721863285}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x1907883714}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_1285166004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2124050494}

[*[vsi-local-id]{lang="PT-BR"}*]{#struct_0_x2095_42796_247408472}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[用于]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口名]{style="font-family:宋体"}[，取值]{style="font-family:宋体"}[范围为]{style="font-family:宋体"}[0]{lang="PT-BR"}[～]{style="font-family:宋体"}[1023]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[association]{lang="PT-BR"}**]{#struct_0_x2095_42796_892795636}[：]{style="font-family:宋体"}[表示关联属性。关联属性]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口下的过滤信息会立即生效。]{style="font-family:宋体"}

[**[pre-association]{lang="PT-BR"}**]{#struct_0_x2095_42796_1448764768}[：]{style="font-family:宋体"}[表示预关联属性。预关联属性]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口下的过滤信息中，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息会立即生效，而]{style="font-family:宋体"}[\<VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC\>]{lang="EN-US"}[信息只有当该接口转换为关联属性时才会生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1124306673}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[通过本命令在]{style="font-family:宋体"}]{#struct_0_x2095_42796_1778791065}[S]{lang="PT-BR"}[通道接口上创建的接口称为]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口，在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口上创建的接口称为]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[通常，]{style="font-family:宋体"}]{#struct_0_x2095_42796_x2042773500}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口由]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器下发创建或删除；用户也可通过本命令手工创建或删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口，或者修改其关联]{style="font-family:宋体"}[/]{lang="EN-US"}[预关联属性。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[VSI]{lang="PT-BR"}]{#struct_0_x2095_42796_2123460667}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[/S]{lang="PT-BR"}[通道聚合接口的子接口，删除]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的同时也将删除其下的所有]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[当手工将]{style="font-family:宋体"}]{#struct_0_x2095_42796_392701921}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口由]{style="font-family:宋体"}[关联属性]{style="font-family:宋体"}[改为预关联属性时，如果虚拟机的流量特征中有]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址信息，则此]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址将从交换机的驱动中删除，虚拟机的流量可能中断。当手工将]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口由预]{style="font-family:宋体"}[关联属性]{style="font-family:宋体"}[改为关联属性时，交换机将设置该虚拟机的]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址，如果该虚拟机尚未就绪，可能会出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[VSI]{lang="PT-BR"}]{#struct_0_x2095_42796_x545962800}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口创建成功后，用户可通过]{style="font-family:宋体"}**[interface]{lang="PT-BR"}**[命令进入其视图。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1329997948}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1739832866}[在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[属性为]{style="font-family:宋体"}[关联属性的]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_410516814}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname-S-Channel1/0/1:10\] evb vsi 1 association]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x1425558694}[在]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号为]{style="font-family:宋体"}[1]{lang="PT-BR"}[、]{style="font-family:宋体"}[属性为]{style="font-family:宋体"}[关联属性的]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_2123526203}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\] evb vsi 1 association]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1526383028}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_1591174060}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb vsi filter]{lang="EN-US"}**]{#struct_0_x2095_42796_1638738687}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[interface]{lang="EN-US"}**]{#struct_0_x2095_42796_661371289}
:::

::: {#1588198540 .myid}
[]{#_Toc311899214}[]{#_Toc404798176}[]{#struct_0_x2095_42796_x1311048357}

**EVB \-- EVB配置命令 \-- evb vsi active**

------------------------------------------------------------------------

[**[evb vsi active]{lang="EN-US"}**]{#struct_0_x2095_42796_x2017058599}[命令用来激活]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo evb vsi active]{lang="EN-US"}**]{#struct_0_x2095_42796_1080737053}[命令用来取消激活]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1599067367}

[**[evb vsi]{lang="EN-US"}**[ **active**]{lang="EN-US"}]{#struct_0_x2095_42796_2123329595}

[**[undo evb vsi]{lang="EN-US"}**[ **active**]{lang="EN-US"}]{#struct_0_x2095_42796_1529495606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_861656458}

[[VSI]{lang="PT-BR"}]{#struct_0_x2095_42796_x2017529652}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[未激活。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_102147464}

[[VSI]{lang="PT-BR"}]{#struct_0_x2095_42796_1529307372}[接口视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_472039272}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_900663281}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_2123395131}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1944860436}

[[当]{style="font-family:宋体"}]{#struct_0_x2095_42796_327245330}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[激活后，流量监管（请参见"]{style="font-family:宋体"}[ACL]{lang="PT-BR"}[和]{style="font-family:宋体"}[QoS]{lang="PT-BR"}[配置指导"中的"]{style="font-family:宋体"}[QoS]{lang="PT-BR"}["）等配置才会生效；而当]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[未激活时，流量监管等配置不会生效，此时不建议对该接口进行除]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[过滤信息以外的]{style="font-family:宋体"}[其它配置。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}]{#struct_0_x2095_42796_1181852068}[在配置了]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息之后，才允许激活]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[；而在删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息之前，必须先将已激活的]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[取消]{style="font-family:宋体"}[激活]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1405717818}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x1446543013}[激活]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_2071400688}

[\[Sysname\] interface s-channel 1/0/1:10.1]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10.1\] evb vsi active]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_2123722811}[激活]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x347926411}

[\[Sysname\] interface schannel-aggregation 1:10.1]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10.1\] evb vsi active]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_162354706}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb vsi filter]{lang="EN-US"}**]{#struct_0_x2095_42796_1367391903}
:::

::: {#-1590142970 .myid}
[]{#_Toc404798177}[]{#struct_0_x2095_42796_1740228746}

**EVB \-- EVB配置命令 \-- evb vsi filter**

------------------------------------------------------------------------

[**[evb vsi filter]{lang="EN-US"}**]{#struct_0_x2095_42796_x204412685}[命令用来配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息。]{style="font-family:宋体"}

[**[undo evb vsi filter]{lang="EN-US"}**]{#struct_0_x2095_42796_x934803404}[命令用来]{style="font-family:宋体"}[删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_496261042}

[**[evb vsi filter ]{lang="EN-US"}**[\[ **group** *group-id* \] **vlan** *vlan-id* \[ **mac** *mac-address* \]]{lang="EN-US"}]{#struct_0_x2095_42796_2123788347}

[**[undo evb vsi filter]{lang="EN-US"}**[ \[ **group** *group-id* \] \[ **vlan** *vlan-id* \[ **mac** *mac-address* \] \]]{lang="EN-US"}]{#struct_0_x2095_42796_1927334940}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x2083298925}

[[不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_x395923715}[过滤信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x808073030}

[[VSI]{lang="PT-BR"}]{#struct_0_x2095_42796_x1381991452}[接口视图]{style="font-family:宋体"}[/]{lang="PT-BR"}[VSI]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1482872124}

[[network-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_x1351882807}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x2095_42796_2123591739}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_763599898}

[**[group]{lang="PT-BR"}**]{#struct_0_x2095_42796_2132451661}[ *group-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[组编号，取值]{style="font-family:宋体"}[范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[4094]{lang="PT-BR"}[。本参数用于为]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[分组]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即当要使用的]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[数量超过]{style="font-family:宋体"}[4094]{lang="PT-BR"}[个]{style="font-family:宋体"}[时]{style="font-family:宋体"}[，可通过]{style="font-family:宋体"}[由]{style="font-family:宋体"}[Group ID]{lang="PT-BR"}[和]{style="font-family:宋体"}[VLAN ID]{lang="PT-BR"}[共同标识一个]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[的方式来扩充]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[的可用数量]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vlan]{lang="PT-BR"}**]{#struct_0_x2095_42796_1702859905}[ *vlan-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[的编号，取值]{style="font-family:宋体"}[范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[4094]{lang="PT-BR"}[，]{style="font-family:宋体"}[该]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[必须存在。]{style="font-family:宋体"}

[**[mac]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1329447852}[ *mac-address*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[必须为有效的单播]{style="font-family:宋体"}[MAC]{lang="PT-BR"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1072594843}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_956434124}[过滤信息是用来标识虚拟机上]{style="font-family:宋体"}[VSI]{lang="EN-US"}[流量特征的信息，]{style="font-family:宋体"}[EVB]{lang="EN-US"}[交换机通过该信息来识别虚拟机上]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的流量。]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[过滤信息通常由]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[管理服务器下发，用户也可以通过本命令手工创建或删除。]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息分为两种：流量所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，或者流量的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址及其所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的组合。]{style="font-family:宋体"}

[[VSI]{lang="EN-US"}]{#struct_0_x2095_42796_999941781}[过滤信息中有三个参数：流量所属的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，流量所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所在的组，以及流量的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。由这三个参数形成了以下四种]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息的组合：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN ID]{lang="EN-US"}]{#struct_0_x2095_42796_1453124203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN ID + MAC]{lang="EN-US"}]{#struct_0_x2095_42796_2123657275}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group ID + VLAN ID]{lang="EN-US"}]{#struct_0_x2095_42796_1182642953}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group ID + VLAN ID + MAC]{lang="EN-US"}]{#struct_0_x2095_42796_1704562165}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x2095_42796_508508686}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1353625694}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口上配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息之前，必须将该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口所属]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口的链路类型配置为]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[类型，否则]{style="font-family:宋体"}[V]{lang="EN-US"}[SI]{lang="PT-BR"}[过滤信息的]{style="font-family:宋体"}[配置将失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当在某]{style="font-family:宋体"}]{#struct_0_x2095_42796_x359920506}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口上配置]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息时，如果该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口所属]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口（或此]{style="font-family:宋体"}[S]{lang="EN-US"}[通道所属接口）尚未允许]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息中所包含的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[通过，则该]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口（或此]{style="font-family:宋体"}[S]{lang="EN-US"}[通道所属接口）将自动允许此]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[通过；当在某]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口上删除包含某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息]{style="font-family:宋体"}[时，如果该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口所属]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口（或此]{style="font-family:宋体"}[S]{lang="EN-US"}[通道所属接口）下所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口上的其它]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息中都不包含此]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则该]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口（或此]{style="font-family:宋体"}[S]{lang="EN-US"}[通道所属接口）将自动禁止此]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当一个]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1081281810}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口上配置的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息中已包含某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，不允许在该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口或其所属]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口下的其它]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口上再配置包含该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息，否则系统将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x2095_42796_1657462240}[VSI]{lang="PT-BR"}[过滤信息为流量所属的]{style="font-family:宋体"}[VLAN]{lang="PT-BR"}[，但用户手工]{style="font-family:宋体"}[关闭了相应]{style="font-family:宋体"}[S]{lang="EN-US"}[通道的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习能力]{style="font-family:宋体"}[，将导致]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[流量无法转发。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置了]{style="font-family:宋体"}]{#struct_0_x2095_42796_2123984955}[VSI]{lang="EN-US"}[过滤信息之后，才允许激活]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[；而在删除]{style="font-family:宋体"}[VSI]{lang="EN-US"}[过滤信息之前，必须先取消激活]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[聚合接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1901374555}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x851984508}[在]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[上配置]{style="font-family:宋体"}[VLAN 1]{lang="PT-BR"}[的过滤信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_356130946}

[\[Sysname\] interface s-channel 1/0/1:10.1]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10.1\] evb vsi filter vlan 1]{lang="PT-BR"}

[]{#_Toc296504304}[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_501160617}[在]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[上配置]{style="font-family:宋体"}[VLAN 1]{lang="PT-BR"}[的过滤信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_363519518}

[\[Sysname\] interface schannel-aggregation 1:10.1]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10.1\] evb vsi filter vlan 1]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1748908678}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb mac-learning forbidden]{lang="EN-US"}**]{#struct_0_x2095_42796_2124050491}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[evb vsi ]{lang="EN-US"}**]{#struct_0_x2095_42796_247605080}**[active]{lang="EN-US"}**
:::

::: {#775541518 .myid}
[]{#_Toc404798178}[]{#struct_0_x2095_42796_x1092278138}

**EVB \-- EVB配置命令 \-- interface**

------------------------------------------------------------------------

[**[interface]{lang="EN-US"}**]{#struct_0_x2095_42796_x272746551}[命令用来进入]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/]{lang="EN-US"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_795262529}

[**[interface ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_x2095_42796_377602901}**[s-channel]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| **schannel-aggregation** } ]{lang="PT-BR"}[{ *interface-number*:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}[ \| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id* }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1279267602}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1968014256}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2123460668}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_391718881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_242590045}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_967845393}

[**[s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_x1100626232}[：]{style="font-family:宋体"}[进入]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[schannel-aggregation]{lang="PT-BR"}**]{#struct_0_x2095_42796_1944420236}[：]{style="font-family:宋体"}[进入]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[interface-number]{lang="PT-BR"}*]{#struct_0_x2095_42796_x667008173}[:*channel-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[或]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口的编号]{style="font-family:
宋体"}[。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道所在接口的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号。]{style="font-family:
宋体"}

[*[interface-number]{lang="PT-BR"}*]{#struct_0_x2095_42796_1366850438}[:*channel-id.vsi-local-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口的编号]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道所在接口的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[vsi-local-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2123526204}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x1526841780}[进入]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_x1092705039}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10\]]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1304612398}[进入]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_425278073}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\]]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_x2040197008}[进入]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x2095_42796_2123329596}

[\[Sysname\] interface s-channel 1/0/1:10.1]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10.1\]]{lang="PT-BR"}

[]{#_Toc296504317}[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1529561142}[进入]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_1265739731}

[\[Sysname\] interface schannel-aggregation 1:10.1]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10.1\]]{lang="PT-BR"}
:::

::: {#2052875588 .myid}
[]{#_Toc404798179}[]{#struct_0_x2095_42796_967779121}

**EVB \-- EVB配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2095_42796_x2058822095}[命令用来清除]{style="font-family:
宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/]{lang="EN-US"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[上的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x882989589}

[**[reset counters interface]{lang="EN-US"}**[ \[ { ]{lang="EN-US"}]{#struct_0_x2095_42796_x1854597862}**[s-channel]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| **schannel-aggregation** } ]{lang="PT-BR"}[\[ *interface-number*:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}[ \| interface-number]{lang="EN-US"}*[:]{lang="EN-US"}*[channel-id]{lang="PT-BR"}*[.*vsi-local-id* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_2123395132}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1944663828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1637107532}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_x1064585429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_x647617843}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2095_42796_816761484}

[**[s-channel]{lang="PT-BR"}**]{#struct_0_x2095_42796_x460177533}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[**[schannel-aggregation]{lang="PT-BR"}**]{#struct_0_x2095_42796_1820610813}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[*[interface-number]{lang="PT-BR"}*]{#struct_0_x2095_42796_2123722812}[:*channel-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道]{style="font-family:宋体"}[接口或]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口的编号]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道所在接口的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号。]{style="font-family:
宋体"}

[*[interface-number]{lang="PT-BR"}*]{#struct_0_x2095_42796_x347860875}[:*channel-id*.*vsi-local-id*]{lang="PT-BR"}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口的编号]{style="font-family:宋体"}[。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-number]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道所在接口的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[channel-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道的编号]{style="font-family:
宋体"}[，]{style="font-family:宋体"}*[vsi-local-id]{lang="PT-BR"}*[为]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[本地编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1658720719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在某些情况下，需要统计一定时间内某]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1931467602}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/]{lang="EN-US"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定接口类型和接口编号，将清除所有接口上的统计信息。]{style="font-family:宋体"}]{#struct_0_x2095_42796_2027064089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了接口类型而未指定接口编号，将清除所有已创建的]{style="font-family:宋体"}]{#struct_0_x2095_42796_x1578543893}[S]{lang="EN-US"}[通道]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[接口]{style="font-family:宋体"}[/]{lang="EN-US"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1121666044}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x2041083635}[清除]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface ]{lang="EN-US"}]{#struct_0_x2095_42796_2123788348}[s-channel 1/0/1:10]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1927662620}[清除]{style="font-family:宋体"}[S]{lang="PT-BR"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters ]{lang="PT-BR"}[interface ]{lang="EN-US"}]{#struct_0_x2095_42796_1056709842}[schannel-aggregation 1:10]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1390040305}[清除]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[接口]{style="font-family:宋体"}[S-Channel1/0/1:10.1]{lang="PT-BR"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface s-channel 1/0/1:10.1]{lang="PT-BR"}]{#struct_0_x2095_42796_630020269}

[[\# ]{lang="PT-BR"}]{#struct_0_x2095_42796_1084038390}[清除]{style="font-family:宋体"}[VSI]{lang="PT-BR"}[聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10.1]{lang="PT-BR"}[上的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface ]{lang="EN-US"}]{#struct_0_x2095_42796_x156904815}[schannel-aggregation 1:10.1]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1227759747}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_x2095_42796_2123591740}
:::

::: {#1170655049 .myid}
[]{#_Toc404798180}[]{#struct_0_x2095_42796_763141153}

**EVB \-- EVB配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2095_42796_x706247148}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2095_42796_1547128460}[命令用来打开当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x422123372}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2095_42796_1468030625}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2095_42796_x1430039602}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x421477612}

[[接口处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2095_42796_2123657276}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1182839561}

[[S]{lang="EN-US"}]{#struct_0_x2095_42796_1716340275}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2095_42796_1297876296}

[[network-admin]{lang="EN-US"}]{#struct_0_x2095_42796_1236877538}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2095_42796_341554755}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2095_42796_x1341951584}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_896173731}[关闭]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口]{style="font-family:宋体"}[S-Channel1/0/1:10]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_2123984956}

[\[Sysname\] interface s-channel 1/0/1:10]{lang="PT-BR"}

[\[Sysname--S-Channel1/0/1:10\]]{lang="PT-BR"}[ ]{lang="PT-BR"}[shutdown]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2095_42796_x1901571163}[关闭]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口]{style="font-family:宋体"}[Schannel-Aggregation1:10]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2095_42796_x371939138}

[\[Sysname\] interface schannel-aggregation 1:10]{lang="PT-BR"}

[\[Sysname--Schannel-Aggregation1:10\]]{lang="PT-BR"}[ shutdown]{lang="EN-US"}
:::
