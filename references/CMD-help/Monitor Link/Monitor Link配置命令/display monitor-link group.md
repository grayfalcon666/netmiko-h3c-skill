::: {#-919056463 .myid}
[]{#_Toc404795811}[]{#struct_0_x9413_x7376_x1027808205}[]{#_Toc178737438}

**Monitor Link \-- Monitor Link配置命令 \-- display monitor-link group**

------------------------------------------------------------------------

[**[display monitor-link group]{lang="EN-US"}**]{#struct_0_x9413_x7376_160126897}[命令用来显示]{style="font-family:
宋体"}[Monitor Link]{lang="EN-US"}[组的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_2117038144}

[**[display monitor-link group]{lang="EN-US"}**[ { *group-id* \| **all** }]{lang="EN-US"}]{#struct_0_x9413_x7376_151887232}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1829102872}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9413_x7376_x875428130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x972661336}

[[network-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_453152291}

[[network-operator]{lang="EN-US"}]{#struct_0_x9413_x7376_x1939084943}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_579170769}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9413_x7376_1507179745}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_152911169}

[*[group-id]{lang="EN-US"}*]{#struct_0_x9413_x7376_2117234752}[：显示指定]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的信息。]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x9413_x7376_973851339}[：显示所有]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1624549169}

[[使用本命令不会显示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_416435373}[组中聚合成员端口的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1237097592}

[[\# ]{lang="EN-US"}]{#struct_0_x9413_x7376_x798705855}[显示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的信息。]{style="font-family:
宋体"}

[[\<Sysname\> display monitor-link group 1]{lang="EN-US"}]{#struct_0_x9413_x7376_2117169216}

[Monitor link group 1 information:]{lang="EN-US"}

[  Group status     : UP]{lang="EN-US"}

[  Downlink up-delay: 0(s)]{lang="EN-US"}

[  Last-up-time     : 16:38:26 2012/4/21]{lang="EN-US"}

[  Last-down-time   : 16:37:20 2012/4/21]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Member                    Role       Status]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  GE1/0/1                   UPLINK     UP]{lang="EN-US"}

[  GE1/0/2                   DOWNLINK   UP]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display monitor-link group]{lang="EN-US"}]{#struct_0_x9413_x7376_x622843777}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x735581458}[[字段]{style="font-family:黑体"}]{#struct_0_x9413_x7376_573792171}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x501510541}

[[Monitor link group 1 information]{lang="EN-US"}]{#struct_0_x9413_x7376_928510278}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_828025901}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的信息]{style="font-family:宋体"}

[[Group status]{lang="EN-US"}]{#struct_0_x9413_x7376_x65904383}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_x405761066}[组的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9413_x7376_2117365824}[：故障]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9413_x7376_x1036888620}[：正常]{lang="EN-US" style="font-family:宋体"}

[[Downlink up-delay]{lang="EN-US"}]{#struct_0_x9413_x7376_x107356497}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_1215027776}[组下行接口的回切延时，单位为秒]{style="font-family:宋体"}

[[Last-up-time]{lang="EN-US"}]{#struct_0_x9413_x7376_x817923643}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_2093315373}[组最近一次]{style="font-family:宋体"}[up]{lang="EN-US"}[的时间]{style="font-family:宋体"}

[[Last-down-time]{lang="EN-US"}]{#struct_0_x9413_x7376_2117300288}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_1753217033}[组最近一次]{style="font-family:宋体"}[down]{lang="EN-US"}[的时间]{style="font-family:宋体"}

[[Member]{lang="EN-US"}]{#struct_0_x9413_x7376_x1321208556}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_x511217408}[组的成员接口]{style="font-family:宋体"}

[[Role]{lang="EN-US"}]{#struct_0_x9413_x7376_x1289337195}

[[成员接口的角色：]{style="font-family:宋体"}]{#struct_0_x9413_x7376_1747202919}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWNLINK]{lang="EN-US"}]{#struct_0_x9413_x7376_2117496896}[：下行接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UPLINK]{lang="EN-US"}]{#struct_0_x9413_x7376_509993559}[：上行接口]{lang="EN-US" style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x9413_x7376_1986241644}

[[成员接口的状态：]{style="font-family:宋体"}]{#struct_0_x9413_x7376_x1623069613}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x9413_x7376_484452599}[：故障]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x9413_x7376_2117431360}[：正常]{lang="EN-US" style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc178737439}

::: {#-697265501 .myid}
[]{#_Toc404795812}[]{#struct_0_x9413_x7376_979141771}

**Monitor Link \-- Monitor Link配置命令 \-- downlink up-delay**

------------------------------------------------------------------------

[**[downlink up-delay]{lang="EN-US"}**]{#struct_0_x9413_x7376_x833623444}[命令用来配置]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组下行接口的回切延时。]{style="font-family:宋体"}

[**[undo downlink up-delay]{lang="EN-US"}**]{#struct_0_x9413_x7376_1217943412}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1833215534}

[**[downlink up-delay ]{lang="EN-US"}***[delay]{lang="EN-US"}*]{#struct_0_x9413_x7376_x303968685}

[**[undo downlink up-delay]{lang="EN-US"}**]{#struct_0_x9413_x7376_897029799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1784321506}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_x855577553}[组下行接口的回切延时为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，即上行接口]{style="font-family:宋体"}[up]{lang="EN-US"}[后，下行接口立刻恢复为]{style="font-family:宋体"}[up]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1492008398}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_2117627968}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x235508349}

[[network-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_52332368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_x1570759770}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_130561831}

[*[delay]{lang="EN-US"}*]{#struct_0_x9413_x7376_x1183790977}[：表示延时时间，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_956213154}

[[通过延时回切机制可以避免由于]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_x1612978605}[组上行链路震荡而导致的下行链路频繁切换。其原理为：当]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的上行接口恢复为]{style="font-family:宋体"}[up]{lang="EN-US"}[状态并维持了一段时间之后，下行接口才恢复为]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，这段时间就称为]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组下行接口的回切延时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x215163823}

[[\# ]{lang="EN-US"}]{#struct_0_x9413_x7376_2117562432}[配置]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[下行接口的回切延时为]{style="font-family:
宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9413_x7376_204410766}

[\[Sysname\] monitor-link group 1]{lang="EN-US"}

[\[Sysname-mtlk-group1\] downlink up-delay 50]{lang="EN-US"}
:::

::: {#395989215 .myid}
[]{#_Toc404795813}[]{#struct_0_x9413_x7376_x954863641}

**Monitor Link \-- Monitor Link配置命令 \-- monitor-link group**

------------------------------------------------------------------------

[**[monitor-link group]{lang="EN-US"}**]{#struct_0_x9413_x7376_1796445496}[命令用来创建]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组，并进入]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组视图。]{style="font-family:宋体"}

[**[undo monitor-link group]{lang="EN-US"}**]{#struct_0_x9413_x7376_x463751678}[命令用来删除]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1803774463}

[**[monitor-link group ]{lang="EN-US"}***[group-id]{lang="EN-US"}*]{#struct_0_x9413_x7376_2001655936}

[**[undo monitor-link group ]{lang="EN-US"}***[group-id]{lang="EN-US"}*]{#struct_0_x9413_x7376_1414749873}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1410020616}

[[不存在任何]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_2117103677}[组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1392548459}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9413_x7376_2115285807}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x81439181}

[[network-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_1848860066}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_775766740}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1559897561}

[*[group-id]{lang="EN-US"}*]{#struct_0_x9413_x7376_x244483729}[：表示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x742024011}

[[\# ]{lang="EN-US"}]{#struct_0_x9413_x7376_2117038141}[创建]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:
宋体"}[Monitor Link]{lang="EN-US"}[组]{style="font-family:
宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9413_x7376_151559552}

[\[Sysname\] monitor-link group 1]{lang="EN-US"}

[\[Sysname-mtlk-group1\]]{lang="EN-US"}
:::

::: {#1212291552 .myid}
[]{#_Toc178737440}[]{#_Toc404795814}[]{#struct_0_x9413_x7376_x417045932}[]{#_Toc178737441}

**Monitor Link \-- Monitor Link配置命令 \-- port**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**]{#struct_0_x9413_x7376_856305547}[命令用来配置]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的成员接口。]{style="font-family:宋体"}

[**[undo port]{lang="EN-US"}**]{#struct_0_x9413_x7376_691647584}[命令用来取消]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组成员接口的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x88455951}

[**[port ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ { *interface-number* \| *interface-number*.*subnumber* } { **downlink** \| **uplink** }]{lang="EN-US"}]{#struct_0_x9413_x7376_x77523825}

[**[undo port ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x9413_x7376_609574145}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1638677119}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_2117234749}[组中没有成员接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_973392586}

[[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_x1406341878}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1049542347}

[[network-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_560006634}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_x2139685865}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1016034910}

[*[interface-type]{lang="EN-US"}*]{#struct_0_x9413_x7376_x1046889055}[：表示接口类型，包括二层以太网接口、三层以太网接口、三层以太网子接口、二层聚合接口、三层聚合接口、三层聚合子接口、]{style="font-family:宋体"}[S]{lang="EN-US"}[通道接口和]{style="font-family:宋体"}[S]{lang="EN-US"}[通道聚合接口。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x9413_x7376_x855926874}[：表示接口编号。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*[.*subnumber*]{lang="EN-US"}]{#struct_0_x9413_x7376_2117169213}[：表示子接口的编号。其中，]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为主接口编号；]{style="font-family:宋体"}*[subnumber]{lang="EN-US"}*[为子接口编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[downlink]{lang="EN-US"}**]{#struct_0_x9413_x7376_x623040385}[：表示下行接口。]{style="font-family:宋体"}

[**[uplink]{lang="EN-US"}**]{#struct_0_x9413_x7376_1378615403}[：表示上行接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x214068586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x9413_x7376_311195273}[已将一个]{lang="EN-US" style="font-family:宋体"}[接口的主接口配置为]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的下行接口，请勿再将该接口的子接口配置为任何]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的上行接口，否则将影响]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[协议的正常运行]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许将一个聚合接口及其所对应聚合组的成员端口加入同一个]{style="font-family:宋体"}]{#struct_0_x9413_x7376_1379234941}[Monitor Link]{lang="SV"}[组中，否则将影响]{style="font-family:宋体"}[Monitor Link]{lang="SV"}[协议的正常运行。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于同一接口的主接口和子接口的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9413_x7376_1729958473}[up/down]{lang="SV"}[状态本身是联动的，因此请勿将它们]{lang="EN-US" style="font-family:宋体"}[加入]{style="font-family:宋体"}[同一]{lang="EN-US" style="font-family:宋体"}[个]{style="font-family:宋体"}[Monitor Link]{lang="SV"}[组]{lang="EN-US" style="font-family:宋体"}[中]{style="font-family:宋体"}[，否则将影响该]{lang="EN-US" style="font-family:宋体"}[Monitor Link]{lang="SV"}[组的性能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口只能属于一个]{lang="EN-US" style="font-family:宋体"}[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_298112917}[组。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_x9413_x7376_x1175045556}[Monitor Link]{lang="EN-US"}[组的成员接口也可在接口视图下进行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_244786385}

[[\# ]{lang="EN-US"}]{#struct_0_x9413_x7376_x1006583369}[配置]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的上行接口为]{style="font-family:
宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，下行接口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9413_x7376_2117365821}

[\[Sysname\] monitor-link group 1]{lang="EN-US"}

[\[Sysname-mtlk-group1\] port gigabitethernet 1/0/1 uplink]{lang="EN-US"}

[\[Sysname-mtlk-group1\] port gigabitethernet 1/0/2 downlink]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1037085228}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port monitor-link group]{lang="EN-US"}**]{#struct_0_x9413_x7376_x1919075912}
:::

::: {#918211240 .myid}
[]{#_Toc404795815}[]{#struct_0_x9413_x7376_x1017045431}

**Monitor Link \-- Monitor Link配置命令 \-- port monitor-link group**

------------------------------------------------------------------------

[**[port monitor-link group]{lang="EN-US"}**]{#struct_0_x9413_x7376_1392265731}[命令用来配置]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的成员接口。]{style="font-family:宋体"}

[**[undo port monitor-link group]{lang="EN-US"}**]{#struct_0_x9413_x7376_490452669}[命令用来取消]{style="font-family:
宋体"}[Monitor Link]{lang="EN-US"}[组成员接口的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1828386871}

[**[port monitor-link group ]{lang="EN-US"}***[group-id]{lang="EN-US"}*[ { **downlink** \| **uplink** }]{lang="EN-US"}]{#struct_0_x9413_x7376_1452886732}

[**[undo port monitor-link group ]{lang="EN-US"}***[group-id]{lang="EN-US"}*]{#struct_0_x9413_x7376_2117300285}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_1754069001}

[[接口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9413_x7376_1994544461}[子接口不是]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的成员接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1372181904}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9413_x7376_x446302664}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道接口视图]{style="font-family:宋体"}[/S]{lang="EN-US"}[通道聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x608294979}

[[network-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_x1986280666}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9413_x7376_x987813216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_772985042}

[*[group-id]{lang="EN-US"}*]{#struct_0_x9413_x7376_x58975393}[：表示]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[downlink]{lang="EN-US"}**]{#struct_0_x9413_x7376_2117496893}[：表示下行接口。]{style="font-family:宋体"}

[**[uplink]{lang="EN-US"}**]{#struct_0_x9413_x7376_509665879}[：表示上行接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_x1354062962}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x9413_x7376_1150103898}[已将一个]{lang="EN-US" style="font-family:宋体"}[接口的主接口配置为]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的下行接口，请勿再将该接口的子接口配置为任何]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组的上行接口，否则将影响]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[协议的正常运行]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许将一个聚合接口及其所对应聚合组的成员端口加入同一个]{style="font-family:宋体"}]{#struct_0_x9413_x7376_1379431548}[Monitor Link]{lang="SV"}[组中，否则将影响]{style="font-family:宋体"}[Monitor Link]{lang="SV"}[协议的正常运行。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于同一接口的主接口和子接口的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9413_x7376_x1142503654}[up/down]{lang="SV"}[状态本身是联动的，因此请勿将它们]{lang="EN-US" style="font-family:宋体"}[加入]{style="font-family:宋体"}[同一]{lang="EN-US" style="font-family:宋体"}[个]{style="font-family:宋体"}[Monitor Link]{lang="SV"}[组]{lang="EN-US" style="font-family:宋体"}[中]{style="font-family:宋体"}[，否则将影响该]{lang="EN-US" style="font-family:宋体"}[Monitor Link]{lang="SV"}[组的性能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口只能属于一个]{lang="EN-US" style="font-family:宋体"}[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_x2013342694}[组。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[Monitor Link]{lang="EN-US"}]{#struct_0_x9413_x7376_1283494032}[组的成员]{lang="EN-US" style="font-family:宋体"}[接]{style="font-family:宋体"}[口也可在]{lang="EN-US" style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组视图下进行。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_928991579}

[[\# ]{lang="EN-US"}]{#struct_0_x9413_x7376_2089016675}[将]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[分别配置为]{style="font-family:宋体"}[Monitor Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的上行接口和下行接口。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9413_x7376_2117431357}

[\[Sysname\] monitor-link group 1]{lang="EN-US"}

[\[Sysname-mtlk-group1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port monitor-link group 1 uplink]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] port monitor-link group 1 downlink]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9413_x7376_979207306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port]{lang="EN-US"}**]{#struct_0_x9413_x7376_x967436183}
:::
