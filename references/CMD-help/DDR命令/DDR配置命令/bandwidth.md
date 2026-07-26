::: {#1742433432 .myid}
[]{#_Toc404785441}[]{#struct_0_x7129_13907_204879112}[]{#_Toc327888469}[]{#_Toc323804932}

**DDR命令 \-- DDR配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x7129_13907_1045605331}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x7129_13907_x1343625792}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1642519626}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x7129_13907_x612821738}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x7129_13907_x169648504}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1409711278}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_168204331}[接口的期望带宽＝接口的波特率÷]{style="font-family:宋体"}[1000]{lang="EN-US"}[（]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1845953239}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x1643327981}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1188207176}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_182643727}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1874542914}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2145718059}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x7129_13907_x612756202}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2145272843}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x7129_13907_x649889791}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_987573069}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1420406089}[配置接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[100kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x118251096}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] bandwidth 100]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc327888470}[]{#_Toc323804930}[]{#_Toc404785442}[]{#struct_0_x7129_13907_x793879209}[]{#_Toc329007815}[]{#_Toc309912009}

**DDR命令 \-- DDR配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x7129_13907_241241397}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1952422742}

[**[default]{lang="EN-US"}**]{#struct_0_x7129_13907_x613346029}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1742029937}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x2091345004}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1223463016}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x326725332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1552112723}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1559552694}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x7129_13907_341457726}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x7129_13907_x936480351}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x7129_13907_8577686}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x613280493}[将接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_2123223539}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785443}[]{#struct_0_x7129_13907_x1959164691}

**DDR命令 \-- DDR配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x7129_13907_711107275}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x7129_13907_1734279788}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_704333201}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x7129_13907_x1226424134}

[**[undo description]{lang="EN-US"}**]{#struct_0_x7129_13907_1709150188}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1350097982}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x7129_13907_x613214957}["，比如：]{style="font-family:宋体"}[Dialer1 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x162683805}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1010925399}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1988337192}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1555235214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1816847793}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x784523611}

[*[text]{lang="EN-US"}*]{#struct_0_x7129_13907_x444477394}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_339331662}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1256863998}[设置接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[dialer-intf]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x613149421}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] description dialer-intf]{lang="EN-US"}
:::

::: {#1811650014 .myid}
[]{#_Toc404785444}[]{#struct_0_x7129_13907_x217316776}

**DDR命令 \-- DDR配置命令 \-- dialer bundle enable**

------------------------------------------------------------------------

[**[dialer bundle enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x121652359}[命令用来使能共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dialer bundle enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x1061623085}[命令用来禁止共享]{style="font-family:
宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x927554332}

[**[dialer bundle enable]{lang="EN-US"}**]{#struct_0_x7129_13907_289222348}

[**[undo dialer bundle enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x581571039}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_737458534}

[[接口上不使能任何类型的]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_1627158707}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1503713432}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x613608173}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x600279111}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_166136371}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_143897022}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1213142002}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_496245712}[分为共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[和传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[用户在使用共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x880644216}[前，必须首先使用]{style="font-family:宋体"}**[dialer]{lang="EN-US"}**[ **bundle** **enable**]{lang="EN-US"}[命令使能共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[功能，然后在物理接口下配置]{style="font-family:宋体"}**[dialer]{lang="EN-US"}**[ **bundle-member**]{lang="EN-US"}[将物理接口加入共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[中。如果此共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[还需要支持入呼叫则还需要在]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口下配置]{style="font-family:宋体"}**[dialer peer-name]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[在已经使能了传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_145561495}[的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口上配置]{style="font-family:宋体"}**[dialer bundle enable]{lang="EN-US"}**[命令，系统会清除原有的传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[相关的拨号配置。]{style="font-family:宋体"}

[[在使用]{style="font-family:宋体"}**[undo dialer bundle enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x671657378}[命令后，系统将清除拨号接口下的所有]{style="font-family:宋体"}[DDR]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x923383350}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x613542637}[在接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[上使能共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_610593096}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer bundle enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_990316302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer]{lang="EN-US"}**[ **bundle-member**]{lang="EN-US"}]{#struct_0_x7129_13907_x1938043594}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer circular enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x843676339}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer peer-name]{lang="EN-US"}**]{#struct_0_x7129_13907_x1482271253}
:::

::: {#1054877133 .myid}
[]{#_Toc404785445}[]{#struct_0_x7129_13907_190322693}

**DDR命令 \-- DDR配置命令 \-- dialer bundle-member**

------------------------------------------------------------------------

[**[dialer bundle-member]{lang="EN-US"}**]{#struct_0_x7129_13907_x1905717921}[命令用来在共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[中，将物理接口加入某个]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dialer bundle-member]{lang="EN-US"}**]{#struct_0_x7129_13907_1880851050}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x613477101}

[**[dialer bundle-member ]{lang="EN-US"}***[number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **priority** *priority* \]]{lang="EN-US"}]{#struct_0_x7129_13907_1783318327}

[**[undo dialer bundle-member]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x7129_13907_x660942150}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1689455321}

[[物理接口不属于任何一个]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}]{#struct_0_x7129_13907_x1719091722}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_713410919}

[[物理接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_764816316}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x517294697}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1287543713}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1018744914}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x613411565}

[*[number]{lang="EN-US"}*]{#struct_0_x7129_13907_1371954695}[：物理接口所属的]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}[的序号。该序号要与]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的编号相同。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}***[ priority]{lang="EN-US"}*]{#struct_0_x7129_13907_x2006186411}[：物理接口在该]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}[中的优先级。]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[值越大，优先级越高，优先级高的物理接口会被优先使用，优先级相同时，会轮询选择各物理接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_924215830}

[[一个物理接口可以是多个]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}]{#struct_0_x7129_13907_2082539159}[的成员。多次执行本命令可以将一个物理接口加入不同的]{style="font-family:宋体"}[Dialer bundle]{lang="EN-US"}[。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x1608893734}[接口不存在时，此命令会创建对应的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口，并且在]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口上使能共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x932452435}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1422904266}[设置接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[属于]{style="font-family:宋体"}[Dialer bundle1]{lang="EN-US"}[和]{style="font-family:宋体"}[Dialer bundle2]{lang="EN-US"}[，优先级均为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1505845327}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] dialer bundle-member 1 priority 50]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] dialer bundle-member 2 priority 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x612821741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer bundle enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x170238335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_1299995906}
:::

::: {#-2113380412 .myid}
[]{#_Toc404785446}[]{#struct_0_x7129_13907_x171330217}

**DDR命令 \-- DDR配置命令 \-- dialer callback-center**

------------------------------------------------------------------------

[**[dialer callback-center]{lang="EN-US"}**]{#struct_0_x7129_13907_866124319}[命令用来配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼的参照依据。]{style="font-family:宋体"}

[**[undo dialer callback-center]{lang="EN-US"}**]{#struct_0_x7129_13907_521915246}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_864094918}

[**[dialer callback-center]{lang="EN-US"}**[ \[ **dial-number** \| **user** \] \*]{lang="EN-US"}]{#struct_0_x7129_13907_x403998736}

[**[undo dialer callback-center]{lang="EN-US"}**]{#struct_0_x7129_13907_x1398172002}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2054967699}

[[未配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x7129_13907_x612756205}[回呼的参照依据，无法进行]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2144814091}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x29535912}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x943846317}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1693952465}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_2025901222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x692086097}

[**[dial-number]{lang="EN-US"}**]{#struct_0_x7129_13907_x3666321}[：根据配置的本地用户名对应的]{style="font-family:宋体"}**[authorization-attribute callback-number ]{lang="EN-US"}***[callback-number]{lang="EN-US"}*[命令中的参数]{style="font-family:宋体"}*[callback-number]{lang="EN-US"}*[确定回呼的拨号串。]{style="font-family:宋体"}

[**[user]{lang="EN-US"}**]{#struct_0_x7129_13907_x1795937345}[：根据配置的]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**[命令中的参数]{style="font-family:宋体"}**[user ]{lang="EN-US"}***[hostname]{lang="EN-US"}*[确定回呼的拨号串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1048134940}

[[当设备作为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x7129_13907_x613346028}[回呼的]{style="font-family:宋体"}[Server]{lang="EN-US"}[端时，必须配置本命令。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}**[user]{lang="EN-US"}**]{#struct_0_x7129_13907_x1741964401}[和]{style="font-family:宋体"}**[dial-number]{lang="EN-US"}**[两个参数同时被应用时，设备首先尝试按照第一个参数的设置进行回呼，当无法进行回呼时，再尝试应用第二个参数的设置进行回呼。]{style="font-family:宋体"}**[dialer callback-center]{lang="EN-US"}**[命令不带任何参数与]{style="font-family:宋体"}**[dialer callback-center]{lang="EN-US"}**[ **user dial-number**]{lang="EN-US"}[命令功能相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x684183194}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1702023106}[配置设备作为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼的]{style="font-family:宋体"}[Server]{lang="EN-US"}[端，并且设置回呼方式为]{style="font-family:宋体"}**[user]{lang="EN-US"}**[，根据]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**[命令中配置的用户名对应的拨号串进行回呼。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1310085298}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp callback server]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer callback-center user]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer route ip 1.1.1.2 8810052 user Sysnameb]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1048554542}[配置设备作为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼的]{style="font-family:宋体"}[Server]{lang="EN-US"}[端，回呼方式为]{style="font-family:宋体"}**[dial-number]{lang="EN-US"}**[，根据]{style="font-family:宋体"}[PPP]{lang="EN-US"}[认证中接收的对端用户名查找本地用户表确定回呼的拨号串。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_543032451}

[\[Sysname\] local-user usera]{lang="EN-US"}

[\[Sysname-luser-usera\] password simple usera]{lang="EN-US"}

[\[Sysname-luser-usera\] service-type ppp]{lang="EN-US"}

[\[Sysname-luser-usera\] authorization-attribute callback-number 8810048]{lang="EN-US"}

[\[Sysname-luser-usera\] quit]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp callback server]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer callback-center dial-number]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x613280492}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp callback]{lang="EN-US"}**]{#struct_0_x7129_13907_2123289075}
:::

::: {#292746133 .myid}
[]{#_Toc404785447}[]{#struct_0_x7129_13907_x1212596085}[]{#_Toc298941317}[]{#_Toc32572684}

**DDR命令 \-- DDR配置命令 \-- dialer call-in**

------------------------------------------------------------------------

[**[dialer call-in]{lang="EN-US"}**]{#struct_0_x7129_13907_161926881}[命令用来配置允许呼入的]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[主叫号码，或按照该]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[主叫号码进行回呼。]{style="font-family:宋体"}

[**[undo dialer call-in]{lang="EN-US"}**]{#struct_0_x7129_13907_116173375}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_351514945}

[**[dialer call-in]{lang="EN-US"}**[ *remote-number* \[ **callback** \]]{lang="EN-US"}]{#struct_0_x7129_13907_x19649349}

[**[undo dialer call-in]{lang="EN-US"}**[ *remote-number*]{lang="EN-US"}]{#struct_0_x7129_13907_756664411}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x709555316}

[[未配置按照]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_x7129_13907_x208127928}[主叫号码来过滤呼叫。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x613214956}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x162749341}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x544345818}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_2107224890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_396421532}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2145620497}

[*[remote-number]{lang="EN-US"}*]{#struct_0_x7129_13907_768620432}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[主叫号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个字符的字符串，不区分大小写，字符"]{style="font-family:宋体"}[\*]{lang="EN-US"}["通配任意一个字符。]{style="font-family:宋体"}

[**[callback]{lang="EN-US"}**]{#struct_0_x7129_13907_x1162596329}[：如果]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[主叫号码与参数]{style="font-family:宋体"}*[remote-number]{lang="EN-US"}*[相匹配，则设备发起回呼。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2004399740}

[**[dialer call-in]{lang="EN-US"}**]{#struct_0_x7129_13907_x2090267349}[命令用来对]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[拨入进行预处理，以确定该主叫号码用户是否允许呼入，如果程控交换机没有提供主叫号码则直接拒绝该呼叫。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}**[dialer call-in]{lang="EN-US"}**]{#struct_0_x7129_13907_837017059}[命令中携带了]{style="font-family:宋体"}**[callback]{lang="EN-US"}**[参数时，]{style="font-family:宋体"}[在配置了]{style="font-family:宋体"}**[dialer call-in]{lang="EN-US"}**[的拨号接口上同时需要配置]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[dialer number]{lang="EN-US"}**[命令，]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[dialer number]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}*[dial-number]{lang="EN-US"}*[要与]{style="font-family:宋体"}**[dialer call-in]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}*[remote-number]{lang="EN-US"}*[一致，以保证进行正确的回呼。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x613149420}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x217251240}[设置向]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[主叫号码为]{style="font-family:宋体"}[8810152]{lang="EN-US"}[的用户进行回呼。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x918790820}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] dialer route ip 100.1.1.2 8810152]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] dialer call-in 8810152 callback]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x300690750}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer callback-center]{lang="EN-US"}**]{#struct_0_x7129_13907_272101799}
:::

::: {#1513922620 .myid}
[]{#_Toc404785448}[]{#struct_0_x7129_13907_1305981642}[]{#_Toc298941320}[]{#_Toc257709105}

**DDR命令 \-- DDR配置命令 \-- dialer circular enable**

------------------------------------------------------------------------

[**[dialer circular enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x14641310}[命令用来使能传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo dialer circular enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x912089933}[命令用来禁止传统]{style="font-family:
宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x234159625}

[**[dialer circular enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x613608172}

[**[undo dialer circular enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x600213575}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2130805729}

[[接口上不使能任何类型的]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x1512325190}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x701910015}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x405605947}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1674655919}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_431067798}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x351771269}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1723826673}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x613542636}[分为共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[和传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[用户在使用传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_610658632}[前，必须首先使用]{style="font-family:宋体"}**[dialer circular enable]{lang="EN-US"}**[命令使能传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[在已经使能了共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x383521068}[的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口上配置]{style="font-family:宋体"}**[dialer circular enable]{lang="EN-US"}**[命令，系统会清除原有的共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[相关的拨号配置。]{style="font-family:宋体"}

[[在使用]{style="font-family:宋体"}**[undo dialer circular enable]{lang="EN-US"}**]{#struct_0_x7129_13907_1138145640}[命令后，系统将清除拨号接口下的所有]{style="font-family:宋体"}[DDR]{lang="EN-US"}[配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x247345671}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x417942749}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上使能传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1714940360}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer circular enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1691220989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer bundle enable]{lang="EN-US"}**]{#struct_0_x7129_13907_1769652398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer circular-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x613477100}
:::

::: {#951987976 .myid}
[]{#_Toc404785449}[]{#struct_0_x7129_13907_1783252791}[]{#_Toc298941318}[]{#_Toc32572697}

**DDR命令 \-- DDR配置命令 \-- dialer circular-group**

------------------------------------------------------------------------

[**[dialer circular-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x709521802}[命令用来在传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[中，将物理接口加入某个拨号循环组。]{style="font-family:宋体"}

[**[undo dialer circular-group]{lang="EN-US"}**]{#struct_0_x7129_13907_960783837}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1747720360}

[**[dialer circular-group]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x7129_13907_2014897004}

[**[undo dialer circular-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x291607497}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1623563017}

[[物理接口不属于任何一个拨号循环组。]{style="font-family:宋体"}]{#struct_0_x7129_13907_x594439924}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1074924723}

[[物理接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x613411564}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1371889159}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x802481521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_242902527}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1850329493}

[*[number]{lang="EN-US"}*]{#struct_0_x7129_13907_1842697578}[：物理接口所属的拨号循环组的序号。该序号要与]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的编号相同。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_490732678}

[[在传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x987826170}[中，一个物理接口只能属于一个拨号循环组，一个拨号循环组可以包含多个物理接口。当有呼叫从一个拨号循环组上发起时，按照优先级从高到低从属于该拨号循环组的物理接口中选择一个物理接口建立呼叫。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x1584714079}[接口不存在时，此命令会创建对应的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口，并且在该]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口上使能传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1974061548}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x612821740}[将接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[和]{style="font-family:宋体"}[Serial2/1/1]{lang="EN-US"}[加入拨号循环组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x170172799}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] quit]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer circular-group 1]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] quit]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/1]{lang="EN-US"}

[\[Sysname-Serial2/1/1\] dialer circular-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2045963051}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer circular enable]{lang="EN-US"}**]{#struct_0_x7129_13907_1762509164}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer priority]{lang="EN-US"}**]{#struct_0_x7129_13907_x1346559255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_x753790258}
:::

::: {#1799781636 .myid}
[]{#_Toc404785450}[]{#struct_0_x7129_13907_235729582}[]{#_Toc298941319}[]{#_Toc13387698}[]{#_Toc355282345}[]{#_Toc355343520}[]{#_Toc355357211}[]{#_Toc355282346}[]{#_Toc355343521}[]{#_Toc355357212}[]{#_Toc355282347}[]{#_Toc355343522}[]{#_Toc355357213}[]{#_Toc355282348}[]{#_Toc355343523}[]{#_Toc355357214}[]{#_Toc355282349}[]{#_Toc355343524}[]{#_Toc355357215}[]{#_Toc355282350}[]{#_Toc355343525}[]{#_Toc355357216}[]{#_Toc355282351}[]{#_Toc355343526}[]{#_Toc355357217}[]{#_Toc355282352}[]{#_Toc355343527}[]{#_Toc355357218}[]{#_Toc355282353}[]{#_Toc355343528}[]{#_Toc355357219}[]{#_Toc355282354}[]{#_Toc355343529}[]{#_Toc355357220}[]{#_Toc355282355}[]{#_Toc355343530}[]{#_Toc355357221}[]{#_Toc355282356}[]{#_Toc355343531}[]{#_Toc355357222}[]{#_Toc355282357}[]{#_Toc355343532}[]{#_Toc355357223}[]{#_Toc355282358}[]{#_Toc355343533}[]{#_Toc355357224}[]{#_Toc355282359}[]{#_Toc355343534}[]{#_Toc355357225}[]{#_Toc355282360}[]{#_Toc355343535}[]{#_Toc355357226}[]{#_Toc355282361}[]{#_Toc355343536}[]{#_Toc355357227}[]{#_Toc355282362}[]{#_Toc355343537}[]{#_Toc355357228}[]{#_Toc355282363}[]{#_Toc355343538}[]{#_Toc355357229}[]{#_Toc355282364}[]{#_Toc355343539}[]{#_Toc355357230}[]{#_Toc355282365}[]{#_Toc355343540}[]{#_Toc355357231}[]{#_Toc355282366}[]{#_Toc355343541}[]{#_Toc355357232}[]{#_Toc355282367}[]{#_Toc355343542}[]{#_Toc355357233}[]{#_Toc355282368}[]{#_Toc355343543}[]{#_Toc355357234}[]{#_Toc355282369}[]{#_Toc355343544}[]{#_Toc355357235}[]{#_Toc355282370}[]{#_Toc355343545}[]{#_Toc355357236}[]{#_Toc355282371}[]{#_Toc355343546}[]{#_Toc355357237}[]{#_Toc355282372}[]{#_Toc355343547}[]{#_Toc355357238}[]{#_Toc355282373}[]{#_Toc355343548}[]{#_Toc355357239}[]{#_Toc355282374}[]{#_Toc355343549}[]{#_Toc355357240}[]{#_Toc317002177}[]{#_Toc317002234}[]{#_Toc317002178}[]{#_Toc317002235}[]{#_Toc317002179}[]{#_Toc317002236}

**DDR命令 \-- DDR配置命令 \-- dialer disconnect**

------------------------------------------------------------------------

[]{#_Toc32639996}[**[dialer disconnect]{lang="EN-US"}**]{#struct_0_x7129_13907_x612756204}[命令用来拆除拨号链路。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2144879627}

[**[dialer disconnect]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x7129_13907_1967170994}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x329165914}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_603693829}[]{#_Toc32639998}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2012781836}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1045857259}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x178848822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2027463123}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x7129_13907_x356364068}[：拆除指定接口的拨号链路。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口类型和编号。如果不指定接口，则拆除所有接口的拨号链路。]{style="font-family:
宋体"}

[]{#struct_0_x7129_13907_1748624602}[[【举例】]{style="font-family:黑体"}]{#_Toc32640000}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_471232807}[拆除接口]{style="font-family:宋体"}[Dialer0]{lang="EN-US"}[的拔号链路。]{style="font-family:宋体"}

[[\<Sysname\> dialer disconnect interface dialer 0]{lang="EN-US"}]{#struct_0_x7129_13907_737055957}
:::

::: {#485503561 .myid}
[]{#_Toc404785451}[]{#struct_0_x7129_13907_x1948778126}[]{#_Toc298941321}[]{#_Toc41484831}

**DDR命令 \-- DDR配置命令 \-- dialer flow-interval**

------------------------------------------------------------------------

[**[dialer flow-interval]{lang="EN-US"}**]{#struct_0_x7129_13907_1734298610}[命令用来配置]{style="font-family:宋体"}[DDR]{lang="EN-US"}[提供流量统计信息的间隔时间。]{style="font-family:宋体"}

[**[undo dialer flow-interval]{lang="EN-US"}**]{#struct_0_x7129_13907_1123269173}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_756567446}

[**[dialer flow-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x7129_13907_x1765143671}

[**[undo dialer flow-interval]{lang="EN-US"}**]{#struct_0_x7129_13907_1562553663}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748559066}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x1569825629}[提供流量统计信息的间隔时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1773858773}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_601378995}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x155838767}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_466261987}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x710537390}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_500057887}

[*[interval]{lang="EN-US"}*]{#struct_0_x7129_13907_x1732528090}[：]{style="font-family:宋体"}[DDR]{lang="EN-US"}[提供流量统计信息的间隔时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1356799324}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_1748755674}[以用户配置的时间间隔为]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑提供拨号链路上的流量统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1103567460}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_72070855}[配置]{style="font-family:宋体"}[DDR]{lang="EN-US"}[提供流量统计信息的间隔时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1709221266}

[\[Sysname\] dialer flow-interval 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2085738489}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer threshold]{lang="EN-US"}**]{#struct_0_x7129_13907_x608512336}
:::

::: {#-1228391598 .myid}
[]{#_Toc404785452}[]{#struct_0_x7129_13907_1218840589}[]{#_Toc298941323}[]{#_Toc14925817}

**DDR命令 \-- DDR配置命令 \-- dialer number**

------------------------------------------------------------------------

[**[dialer number]{lang="EN-US"}**]{#struct_0_x7129_13907_x711982043}[命令用来设定呼叫单个对端的拨号串。]{style="font-family:宋体"}

[**[undo dialer number]{lang="EN-US"}**]{#struct_0_x7129_13907_x240784953}[命令用来删除已设定的拨号串。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1508589314}

[**[dialer number]{lang="EN-US"}**[ *dial-number* \[ **autodial** \]]{lang="EN-US"}]{#struct_0_x7129_13907_1748690138}

[**[undo dialer number]{lang="EN-US"}**]{#struct_0_x7129_13907_2002404242}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1864832427}

[[未配置呼叫对端的拨号串。]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1132526258}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_404765548}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_106222016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1206539280}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x710067006}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1465235885}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x738153191}

[*[dial-number]{lang="EN-US"}*]{#struct_0_x7129_13907_1748886746}[：呼叫对端的拨号串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[autodial]{lang="EN-US"}**]{#struct_0_x7129_13907_1668712239}[：表示自动拨号。如果配置了本参数，则路由器每隔一定时间会自动尝试拨号，拨号的时间间隔由命令]{style="font-family:宋体"}**[dialer timer autodial]{lang="EN-US"}**[设置，缺省的时间间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_359808157}

[[当]{style="font-family:宋体"}[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x1251419254}[接口或者物理接口作为主叫端，需要配置此命令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7129_13907_x142335354}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于传统]{lang="EN-US" style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_2070393633}[，需要呼叫多个目的地址或拨号串时，可以配置]{lang="EN-US" style="font-family:宋体"}**[dialer route]{lang="EN-US"}**[命令来替代]{lang="EN-US" style="font-family:宋体"}**[dialer number]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于共享]{lang="EN-US" style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_1474272383}[，只能使用]{lang="EN-US" style="font-family:宋体"}**[dialer number]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[配置拨号串]{style="font-family:宋体"}[，且一个]{lang="EN-US" style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口只能配置一个拨号串。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1011999113}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x246769655}[设定接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[呼叫对端的拨号串为"]{style="font-family:宋体"}[11111]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1748821210}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer number 11111]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1995552617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer route]{lang="EN-US"}**]{#struct_0_x7129_13907_602500821}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer timer autodial]{lang="EN-US"}**]{#struct_0_x7129_13907_1227209524}
:::

::: {#1668328863 .myid}
[]{#_Toc404785453}[]{#struct_0_x7129_13907_598887827}

**DDR命令 \-- DDR配置命令 \-- dialer peer-name**

------------------------------------------------------------------------

[**[dialer peer-name]{lang="EN-US"}**]{#struct_0_x7129_13907_x1341013973}[命令用来设置共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[应用的对端用户名，以便接收呼叫时能认证呼叫请求。]{style="font-family:宋体"}

[**[undo dialer peer-name]{lang="EN-US"}**]{#struct_0_x7129_13907_x1299679666}[命令用来删除共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[应用的对端用户名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_853348555}

[**[dialer peer-name ]{lang="EN-US"}***[username]{lang="EN-US"}*]{#struct_0_x7129_13907_x1321212109}

[**[undo dialer peer-name ]{lang="EN-US"}**[\[ *username* \]]{lang="EN-US"}]{#struct_0_x7129_13907_x424999836}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1749017818}

[[没有配置共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_1201339599}[应用的对端用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_79445369}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_647788462}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1923421448}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1900056405}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1933385584}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1113527094}

[*[username]{lang="EN-US"}*]{#struct_0_x7129_13907_38500646}[：对端用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，不区分大小写，用于]{style="font-family:宋体"}[PPP]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_628572838}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1748952282}[接口利用]{style="font-family:宋体"}[PPP]{lang="EN-US"}[认证得到的对端用户名决定入呼叫时的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[该命令仅在共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x1904846464}[中有效。在一个]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口下最多可以配置]{style="font-family:宋体"}[255]{lang="EN-US"}[个对端用户名。当一个]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口下配置多个对端用户名时，就实现了用一个]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口同时接入多个物理接口的连接。]{style="font-family:宋体"}

[[当共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x807959342}[接口下没有配置对端用户名时，此共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[可以支持出呼叫，无法支持入呼叫。当共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[接口下配置了对端用户名时，此共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[可以支持入呼叫。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1899301686}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1412438995}[设置共享]{style="font-family:宋体"}[DDR]{lang="EN-US"}[应用的对端用户名为]{style="font-family:宋体"}[routerb]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1213521632}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer peer-name routerb]{lang="EN-US"}
:::

::: {#1252209326 .myid}
[]{#_Toc404785454}[]{#struct_0_x7129_13907_x5921254}[]{#_Toc298941325}[]{#_Toc257709110}[]{#_Toc355282379}[]{#_Toc355343554}[]{#_Toc355357245}[]{#_Toc355282380}[]{#_Toc355343555}[]{#_Toc355357246}[]{#_Toc355282381}[]{#_Toc355343556}[]{#_Toc355357247}[]{#_Toc317002184}[]{#_Toc317002241}[]{#_Toc317002185}[]{#_Toc317002242}[]{#_Toc317002186}[]{#_Toc317002243}

**DDR命令 \-- DDR配置命令 \-- dialer priority**

------------------------------------------------------------------------

[**[dialer priority]{lang="EN-US"}**]{#struct_0_x7129_13907_1995220278}[命令用来配置传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[，设置物理接口在其所在的拨号循环组中的优先级。]{style="font-family:宋体"}

[**[undo dialer priority]{lang="EN-US"}**]{#struct_0_x7129_13907_1010194672}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1917900661}

[**[dialer priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x7129_13907_1749148890}

[**[undo dialer priority]{lang="EN-US"}**]{#struct_0_x7129_13907_x1980700539}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x566102864}

[[物理接口在拨号循环组中的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x7129_13907_x1451161100}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1830092746}

[[物理接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_1845887509}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1611859001}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x2118190572}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1402736768}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1592472899}

[*[priority]{lang="EN-US"}*]{#struct_0_x7129_13907_1749083354}[：物理接口在拨号循环组中的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[，数值越大优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_64147263}

[[此命令设定物理接口在其所在的拨号循环组中的使用顺序，高优先级的物理接口会被优先使用。优先级相同时，会轮询选择各物理接口。]{style="font-family:宋体"}]{#struct_0_x7129_13907_x293020238}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x451730110}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1652624723}[设置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[在拨号循环组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的优先级为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1507580418}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer circular-group 1]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer priority 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x242146491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer circular-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x951888606}
:::

::: {#-76599176 .myid}
[]{#_Toc404785455}[]{#struct_0_x7129_13907_1254856677}[]{#_Toc298941326}[]{#_Toc14925806}

**DDR命令 \-- DDR配置命令 \-- dialer queue-length**

------------------------------------------------------------------------

[**[dialer queue-length]{lang="EN-US"}**]{#struct_0_x7129_13907_1748624603}[命令用来设定拨号接口缓冲队列长度。]{style="font-family:宋体"}

[**[undo dialer queue-length]{lang="EN-US"}**]{#struct_0_x7129_13907_471298343}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_41062666}

[**[dialer queue-length]{lang="EN-US"}**[ *packets*]{lang="EN-US"}]{#struct_0_x7129_13907_x2136212286}

[**[undo dialer queue-length]{lang="EN-US"}**]{#struct_0_x7129_13907_x2078810883}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2058020004}

[[不对报文进行缓存。]{style="font-family:宋体"}]{#struct_0_x7129_13907_1591220368}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1648974064}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_1843163208}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1609486108}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1748559067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1569891165}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1533916193}

[*[packets]{lang="EN-US"}*]{#struct_0_x7129_13907_x270313574}[：接口缓存的数据报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x225085760}

[[没有为拨号接口配置缓冲队列的情况下，当拨号接口收到一个报文时，如果此时连接还没有成功建立，则这个报文将被丢弃。如果为拨号接口配置了缓冲队列，则在连接成功建立之前报文将被缓存，待连接成功后再发送。]{style="font-family:宋体"}]{#struct_0_x7129_13907_x456613215}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1495635193}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1598469699}[设置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的接口缓冲队列长度为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x704834}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer queue-length 10]{lang="EN-US"}
:::

::: {#1995323479 .myid}
[]{#_Toc404785456}[]{#struct_0_x7129_13907_1307567381}[]{#_Toc298941327}[]{#_Toc32572692}[]{#_Toc324941522}[]{#_Toc317002189}[]{#_Toc317002246}[]{#_Toc317002190}[]{#_Toc317002247}

**DDR命令 \-- DDR配置命令 \-- dialer route**

------------------------------------------------------------------------

[**[dialer route]{lang="EN-US"}**]{#struct_0_x7129_13907_1748755675}[命令用来配置从一个拨号接口呼叫指定目的地址，或接收对端的呼叫。]{style="font-family:宋体"}

[**[undo dialer route]{lang="EN-US"}**]{#struct_0_x7129_13907_x1103632996}[命令用来删除该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_104242907}

[**[dialer route]{lang="EN-US"}**[ **ip** *next-hop-address* \[ **mask** *network-mask-length* \] \[ **vpn-instance** *vpn-instance-name* \] \[ *dial-number* \[ **autodial** \| **interface** *interface-type interface-number* \] \* \] \[ **broadcast** \| **user** *hostname* \] \*]{lang="EN-US"}]{#struct_0_x7129_13907_x2059641662}

[**[undo dialer route]{lang="EN-US"}**[ *protocol next-hop-address* \[ **mask** *network-mask-length* \] \[ **vpn-instance** *vpn-instance-name* \] \[ *dial-number* \]]{lang="EN-US"}]{#struct_0_x7129_13907_1412713027}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1142531829}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_144816076}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1198670777}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1389910116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1496282700}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748690139}

[**[ip]{lang="EN-US"}**]{#struct_0_x7129_13907_2002338706}[：网络协议为]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[*[next-hop-address]{lang="EN-US"}*]{#struct_0_x7129_13907_2028649374}[：拨号对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}***[ network-mask-length]{lang="EN-US"}*]{#struct_0_x7129_13907_1311195415}[：拨号对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。若不设置该参数则系统默认为]{style="font-family:宋体"}[32]{lang="EN-US"}[，此时就把]{style="font-family:宋体"}*[next-hop-address]{lang="EN-US"}*[当成主机地址处理。若用户需要把]{style="font-family:宋体"}*[next-hop-address]{lang="EN-US"}*[配置成网段地址，则需要指定它的]{style="font-family:宋体"}*[network-mask-length]{lang="EN-US"}*[。当]{style="font-family:宋体"}*[next-hop-address]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[并且]{style="font-family:宋体"}*[network-mask-length]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示不限制对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，例如]{style="font-family:宋体"}**[dialer route ip]{lang="EN-US"}**[ 0.0.0.0 **mask** 0 8886]{lang="EN-US"}[，表示允许通过]{style="font-family:宋体"}[8886]{lang="EN-US"}[号码拨叫任何]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x7129_13907_156376}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[dial-number]{lang="EN-US"}*]{#struct_0_x7129_13907_x520567376}[：去往对端的拨号串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[个字符的字符串，不区分大小写。如果配置了此拨号串，则可以进行出方向拨号，否则只能接受入方向拨号。]{style="font-family:宋体"}

[**[autodial]{lang="EN-US"}**]{#struct_0_x7129_13907_x2082763614}[：表示自动拨号。如果配置了本参数，则路由器每隔一定时间会自动尝试拨号，拨号的时间间隔由命令]{style="font-family:宋体"}**[dialer timer autodial]{lang="EN-US"}**[设置，缺省的时间间隔为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x7129_13907_502979445}[：使用指定的物理接口拔号。当几个物理接口绑定到一个]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[口，且这几条拔号链路连接到不同的程控交换机时，需要配置指定拔号号码与物理接口的对应关系。此参数只能在使能传统]{style="font-family:宋体"}[DDR]{lang="EN-US"}[的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[口上配置。]{style="font-family:宋体"}

[**[broadcast]{lang="EN-US"}**]{#struct_0_x7129_13907_x1750904556}[：表示可以从本条拨号链路发送广播报文。]{style="font-family:宋体"}

[**[user]{lang="EN-US"}***[ hostname]{lang="EN-US"}*]{#struct_0_x7129_13907_x877175348}[：对端用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，不区分大小写，用于接收呼叫时进行认证。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748886747}

[[如果需要]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_1668777775}[主动呼叫，则需使用]{style="font-family:宋体"}*[dial-number]{lang="EN-US"}*[参数来配置拨号串。如果不配置]{style="font-family:宋体"}*[dial-number]{lang="EN-US"}*[参数，则只能接收对端的呼叫。]{style="font-family:宋体"}

[[如果配置了某个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7129_13907_x1589476448}[地址]{style="font-family:宋体"}*[next-hop-address]{lang="EN-US"}*[对应的拨号串]{style="font-family:宋体"}*[dial-number]{lang="EN-US"}*[，那么使用]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令时必须包含]{style="font-family:宋体"}*[dial-number]{lang="EN-US"}*[参数。]{style="font-family:宋体"}

[[如果使用]{style="font-family:宋体"}**[user]{lang="EN-US"}**]{#struct_0_x7129_13907_x2057545546}[关键字，则必须配置相关的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[认证（通过]{style="font-family:宋体"}[PPP]{lang="EN-US"}[认证获取对端的用户名，然后判断这个用户名和本命令中配置的用户名是否一致，如果一致，才接收呼叫）。]{style="font-family:宋体"}

[[一个拨号接口可以配置多条]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**]{#struct_0_x7129_13907_x1098441616}[，对应同一个目的地址也可配置多条]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**[命令指定多个拨号串以实现拨号串备份的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1772780195}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1897084076}[配置去往]{style="font-family:宋体"}[192.168.1.0/24]{lang="EN-US"}[网段的数据包都拨叫]{style="font-family:宋体"}[888066]{lang="EN-US"}[号码建立链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x851367138}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer route ip 192.168.1.0 mask 24 888066]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1495908846}[配置去往]{style="font-family:宋体"}[191.168.1.1]{lang="EN-US"}[主机地址的数据包拨叫]{style="font-family:宋体"}[888065]{lang="EN-US"}[号码建立链路。]{style="font-family:宋体"}

[[\[Sysname-Serial2/1/0\] dialer route ip 191.168.1.1 888065]{lang="EN-US"}]{#struct_0_x7129_13907_1748821211}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1995618153}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer timer autodial]{lang="EN-US"}**]{#struct_0_x7129_13907_x2069777522}
:::

::: {#1850191880 .myid}
[]{#_Toc404785457}[]{#struct_0_x7129_13907_1506098039}[]{#_Toc298941328}[]{#_Toc32572691}

**DDR命令 \-- DDR配置命令 \-- dialer threshold**

------------------------------------------------------------------------

[**[dialer threshold]{lang="EN-US"}**]{#struct_0_x7129_13907_96716996}[命令用来设定]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口上链路的负载阈值，当]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的所有链路的流量与可用带宽的比例超过设定的百分比时，启动另一条链路呼叫同一个目的地址。]{style="font-family:宋体"}

[**[undo dialer threshold]{lang="EN-US"}**]{#struct_0_x7129_13907_1107168445}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_419678375}

[**[dialer threshold ]{lang="EN-US"}***[traffic-percentage ]{lang="EN-US"}*[\[ **in** \| **in-out** \| **out** \]]{lang="EN-US"}]{#struct_0_x7129_13907_x815143359}

[**[undo dialer threshold]{lang="EN-US"}**]{#struct_0_x7129_13907_1013347398}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1810069980}

[[不启动该功能。]{style="font-family:宋体"}]{#struct_0_x7129_13907_x320260774}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1749017819}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1201274063}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1879705958}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1862724972}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1793448482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_418092597}

[*[traffic-percentage]{lang="EN-US"}*]{#struct_0_x7129_13907_x925980630}[：链路实际流量与带宽的百分比，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[in]{lang="EN-US"}**]{#struct_0_x7129_13907_1941766588}[：计算实际负载时只计算接收的流量。]{style="font-family:宋体"}

[**[in-out]{lang="EN-US"}**]{#struct_0_x7129_13907_1953990603}[：计算实际负载时计算接收和发送流量中较大的一个。]{style="font-family:宋体"}

[**[out]{lang="EN-US"}**]{#struct_0_x7129_13907_1748952283}[：计算实际负载时只计算发送的流量。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1904912000}

[[在]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x99748069}[应用中，可以配置链路的负载阈值。当负载阈值在]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[之间时，]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑根据实际流量百分比适当调节分配的带宽，即如果一条链路的实际流量与带宽的比例超过设定的负载阈值，则系统会自动启用第二条链路，并将两条链路进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑；当两条链路的流量与带宽的比例超过设定的负载阈值，系统会启动第三条链路并进行]{style="font-family:宋体"}[MP]{lang="EN-US"}[捆绑，依此类推，从而确保]{style="font-family:宋体"}[DDR]{lang="EN-US"}[链路具有合理的负载流量。]{style="font-family:宋体"}

[[相反，若]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x7129_13907_x235788756}[条（]{style="font-family:宋体"}[N]{lang="EN-US"}[为大于等于]{style="font-family:宋体"}[2]{lang="EN-US"}[的整数）链路的流量与]{style="font-family:宋体"}[N-1]{lang="EN-US"}[条链路带宽的比例小于设定的负载阈值时，系统自动关闭一条链路，以此类推，从而确保]{style="font-family:宋体"}[DDR]{lang="EN-US"}[链路的利用率保持在合理范围。]{style="font-family:宋体"}

[[目前，本命令只能用于]{style="font-family:宋体"}[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_800688011}[接口，用于物理接口不生效。另外，本命令须与]{style="font-family:宋体"}**[ppp mp]{lang="EN-US"}**[命令结合使用。]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[traffic-percentage]{lang="EN-US"}*]{#struct_0_x7129_13907_x1718862212}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，在链路由于自动拨号或者报文触发拨号而开始呼叫的时候，将自动启动所有可用的链路进行呼叫，而不依靠流量检测决定呼叫策略，对于已经呼叫建立的链路也不会因为超时而主动拆链，也就是说，]{style="font-family:宋体"}**[dialer timer idle]{lang="EN-US"}**[命令在配置了]{style="font-family:宋体"}**[dialer threshold ]{lang="EN-US"}**[0]{lang="EN-US"}[之后将会失效。]{style="font-family:宋体"}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x397880158}[按照]{style="font-family:宋体"}**[dialer]{lang="EN-US"}**[ **flow-interval**]{lang="EN-US"}[配置的时间间隔来定时进行流量统计。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2102843740}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x680671631}[设置接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[的负载阈值为]{style="font-family:宋体"}[80%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1749148891}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer threshold 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1980635003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer flow-interval]{lang="EN-US"}**]{#struct_0_x7129_13907_x258635664}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer timer idle]{lang="EN-US"}**]{#struct_0_x7129_13907_x451957818}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp mp]{lang="EN-US"}**]{#struct_0_x7129_13907_1541784242}[（二层技术]{style="font-family:
宋体"}[-]{lang="EN-US"}[广域网接入命令参考]{style="font-family:宋体"}[/PPP]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#-2018224588 .myid}
[]{#_Toc404785458}[]{#struct_0_x7129_13907_1506636036}[]{#_Toc298941329}[]{#_Toc14925801}

**DDR命令 \-- DDR配置命令 \-- dialer timer autodial**

------------------------------------------------------------------------

[**[dialer timer autodial]{lang="EN-US"}**]{#struct_0_x7129_13907_923012316}[命令用来配置]{style="font-family:宋体"}[DDR]{lang="EN-US"}[自动拨号的间隔时间。]{style="font-family:宋体"}

[**[undo dialer timer autodial]{lang="EN-US"}**]{#struct_0_x7129_13907_1107208097}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1188546811}

[**[dialer timer autodial]{lang="EN-US"}**[ *autodial-interval*]{lang="EN-US"}]{#struct_0_x7129_13907_1749083355}

[**[undo dialer timer autodial]{lang="EN-US"}**]{#struct_0_x7129_13907_64212799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1237566289}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_1163840949}[自动拨号的间隔时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x131509560}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x130608461}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x141981777}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x545094071}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1661943292}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1048792964}

[*[autodial-interval]{lang="EN-US"}*]{#struct_0_x7129_13907_1748624600}[：发起下次呼叫尝试的间隔时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[604800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_471363879}

[[该命令必须与]{style="font-family:宋体"}**[dialer number]{lang="EN-US"}**]{#struct_0_x7129_13907_x437414474}[或]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**[命令中的关键字]{style="font-family:宋体"}**[autodial]{lang="EN-US"}**[结合使用。配置该命令后，]{style="font-family:宋体"}[DDR]{lang="EN-US"}[将每隔]{style="font-family:宋体"}*[autodial-interval]{lang="EN-US"}*[时间自动尝试拨号一次，直至连接建立。自动拨号功能无需数据包的触发，并且在连接建立后不会因空闲时间超时而自动挂断，即]{style="font-family:宋体"}**[dialer timer idle]{lang="EN-US"}**[命令配置对其无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1313992660}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_646386726}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上设置]{style="font-family:宋体"}[DDR]{lang="EN-US"}[自动拨号的间隔时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_915040138}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer timer autodial 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x791622254}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer number]{lang="EN-US"}**]{#struct_0_x7129_13907_x1620755147}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer route]{lang="EN-US"}**]{#struct_0_x7129_13907_717600084}
:::

::: {#1068774529 .myid}
[]{#_Toc404785459}[]{#struct_0_x7129_13907_1748559064}[]{#_Toc298941330}[]{#_Toc32572686}

**DDR命令 \-- DDR配置命令 \-- dialer timer compete**

------------------------------------------------------------------------

[**[dialer timer compete]{lang="EN-US"}**]{#struct_0_x7129_13907_x1569694557}[命令用来配置当接口发生呼叫竞争后的链路空闲时间。]{style="font-family:宋体"}

[**[undo dialer timer compete]{lang="EN-US"}**]{#struct_0_x7129_13907_1209754277}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x100796932}

[**[dialer timer compete]{lang="EN-US"}**[ *compete-idle*]{lang="EN-US"}]{#struct_0_x7129_13907_1193335486}

[**[undo dialer timer compete]{lang="EN-US"}**]{#struct_0_x7129_13907_219264665}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x155568727}

[[接口发生呼叫竞争后的链路空闲时间为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_x7129_13907_464361280}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1115309666}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_642790787}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748755672}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1103436388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x170108297}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1036624611}

[*[compete-idle]{lang="EN-US"}*]{#struct_0_x7129_13907_1276844614}[：接口发生呼叫竞争后的链路空闲时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x259127702}

[[通常一条链路建立后]{style="font-family:宋体"}[Idle]{lang="EN-US"}]{#struct_0_x7129_13907_1892401609}[超时定时器将起作用。当]{style="font-family:宋体"}[DDR]{lang="EN-US"}[开始发起新呼叫时，若所有物理接口都被占用则进入"竞争"状态，此时]{style="font-family:宋体"}[DDR]{lang="EN-US"}[使用]{style="font-family:宋体"}[Compete-idle]{lang="EN-US"}[超时定时器取代]{style="font-family:宋体"}[Idle]{lang="EN-US"}[超时定时器，即链路空闲时间超过]{style="font-family:宋体"}[Compete-idle]{lang="EN-US"}[超时定时器的时间后将自动断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_965206926}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1947045157}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上设置接口发生呼叫竞争后的链路空闲时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1748690136}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer timer compete 10]{lang="EN-US"}
:::

::: {#761328227 .myid}
[]{#_Toc404785460}[]{#struct_0_x7129_13907_2003059602}[]{#_Toc298941331}[]{#_Toc32572685}[]{#_Toc317002195}[]{#_Toc317002252}[]{#_Toc317002196}[]{#_Toc317002253}[]{#_Toc317002197}[]{#_Toc317002254}

**DDR命令 \-- DDR配置命令 \-- dialer timer enable**

------------------------------------------------------------------------

[**[dialer timer enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x331730724}[命令用来配置接口上当链路断开后进行下次呼叫的间隔时间。]{style="font-family:宋体"}

[**[undo dialer timer enable]{lang="EN-US"}**]{#struct_0_x7129_13907_x1824267592}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1223181310}

[**[dialer timer enable]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x7129_13907_71870557}

[**[undo dialer timer enable]{lang="EN-US"}**]{#struct_0_x7129_13907_460828150}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_415204291}

[[接口上当链路断开后进行下次呼叫的间隔时间为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x7129_13907_x113432871}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1093736084}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_1748886744}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1668581167}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_329566145}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1777083435}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1862844715}

[*[interval]{lang="EN-US"}*]{#struct_0_x7129_13907_x649124561}[：当链路断开后进行下次呼叫的间隔时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x482591140}

[[当]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x1550665366}[呼叫链路因故障或挂断等原因进入断开状态，必须经过指定时间（即进行下一次呼叫的间隔时间）后才能建立新的拨号连接，从而避免对端程控交换机过载。]{style="font-family:宋体"}

[[需要注意的是：为了使]{style="font-family:宋体"}[Server]{lang="EN-US"}]{#struct_0_x7129_13907_850009914}[端有足够的时间进行回呼，]{style="font-family:宋体"}[Client]{lang="EN-US"}[端当链路断开后进行下次呼叫的间隔时间应至少比]{style="font-family:宋体"}[Server]{lang="EN-US"}[端的长]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。建议]{style="font-family:宋体"}[Server]{lang="EN-US"}[端使用默认值]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Client]{lang="EN-US"}[端配置为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_65492713}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1748821208}[设置当链路断开后进行下次呼叫的间隔时间为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1996076904}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer timer enable 15]{lang="EN-US"}
:::

::: {#44080507 .myid}
[]{#_Toc404785461}[]{#struct_0_x7129_13907_2078425571}[]{#_Toc298941332}[]{#_Toc32572688}

**DDR命令 \-- DDR配置命令 \-- dialer timer idle**

------------------------------------------------------------------------

[**[dialer timer idle]{lang="EN-US"}**]{#struct_0_x7129_13907_x1815705894}[命令用来设定当接口的呼叫建立后，允许链路空闲的时间。]{style="font-family:宋体"}

[**[undo dialer timer idle]{lang="EN-US"}**]{#struct_0_x7129_13907_719801016}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1752219863}

[**[dialer timer idle]{lang="EN-US"}**[ *idle* \[ **in** \| **in-out** \]]{lang="EN-US"}]{#struct_0_x7129_13907_346604503}

[**[undo dialer timer idle]{lang="EN-US"}**]{#struct_0_x7129_13907_x109538738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x937126374}

[[允许链路空闲的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}]{#struct_0_x7129_13907_1749017816}[秒，只有出方向的感兴趣报文报文重置定时器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1200946383}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1872622591}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_539751892}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x918248652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1648129742}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x150905555}

[*[idle]{lang="EN-US"}*]{#struct_0_x7129_13907_798862308}[：允许链路空闲的时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[in]{lang="EN-US"}**]{#struct_0_x7129_13907_974448675}[：只有入方向的感兴趣报文重置定时器。]{style="font-family:宋体"}

[**[in-out]{lang="EN-US"}**]{#struct_0_x7129_13907_x1965775532}[：出方向和入方向的感兴趣报文都重置定时器。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748952280}

[[当一条链路建立后，]{style="font-family:宋体"}**[dialer timer idle]{lang="EN-US"}**]{#struct_0_x7129_13907_x1904715392}[定时起作用。若在设定的时间内没有感兴趣报文在此链路上传送，则]{style="font-family:宋体"}[DDR]{lang="EN-US"}[自动挂断链路。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7129_13907_1210376274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置命令时不指定]{style="font-family:宋体"}]{#struct_0_x7129_13907_1390145149}**[in]{lang="EN-US"}**[和]{style="font-family:宋体"}**[in-out]{lang="EN-US"}**[参数，则表示只有出方向的感兴趣报文重置定时器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若]{style="font-family:宋体"}]{#struct_0_x7129_13907_608810595}**[dialer timer idle]{lang="EN-US"}**[设定为]{style="font-family:宋体"}[0]{lang="EN-US"}[，则相应的链路在建立后，无论是否有感兴趣报文在此链路上传送，链路将永远不被挂断。]{style="font-family:宋体"}[对于]{lang="EN-US" style="font-family:宋体"}[PPPoE Client]{lang="EN-US"}[应用，若]{lang="EN-US" style="font-family:宋体"}**[dialer timer idle]{lang="EN-US"}**[设定为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[，则将会自动触发拨号保证链接永久在线。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x555376490}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1698941284}[设置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[允许链路空闲的时间为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1941169989}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer timer idle 50]{lang="EN-US"}[]{#_Toc32572699}
:::

::: {#1706783924 .myid}
[]{#_Toc404785462}[]{#struct_0_x7129_13907_871676757}[]{#_Toc298941333}[]{#_Toc257709118}

**DDR命令 \-- DDR配置命令 \-- dialer timer wait-carrier**

------------------------------------------------------------------------

[**[dialer timer wait-carrier]{lang="EN-US"}**]{#struct_0_x7129_13907_x1849978048}[命令用来设定呼叫建立超时定时器（]{style="font-family:
宋体"}[wait-carrier]{lang="EN-US"}[定时器）的超时时间。]{style="font-family:宋体"}

[**[undo dialer timer wait-carrier]{lang="EN-US"}**]{#struct_0_x7129_13907_1749148888}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1980176250}

[**[dialer timer wait-carrier]{lang="EN-US"}**[ *wait-carrier*]{lang="EN-US"}]{#struct_0_x7129_13907_x826735057}

[**[undo dialer timer wait-carrier]{lang="EN-US"}**]{#struct_0_x7129_13907_876520359}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1603717998}

[[呼叫建立超时时间为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_x7129_13907_100303200}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x661767500}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_2090291619}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x581904560}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1749083352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_64540479}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x794434510}

[*[wait-carrier]{lang="EN-US"}*]{#struct_0_x7129_13907_38598801}[：呼叫建立超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x346090230}

[[和某些对端建立]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x298512277}[呼叫时，从呼叫发起到连接建立的时间长短不一，为了有效控制发起呼叫到呼叫连接建立之间允许等待的时间，可以配置]{style="font-family:宋体"}[wait-carrier]{lang="EN-US"}[定时器，若在指定时间内呼叫仍未建立，则]{style="font-family:宋体"}[DDR]{lang="EN-US"}[将终止该呼叫。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1270530861}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_2146298638}[设置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的呼叫建立超时时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_963566570}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer timer wait-carrier 100]{lang="EN-US"}
:::

::::: {#605863808 .myid}
[]{#_Toc404785463}[]{#struct_0_x7129_13907_1748624601}[]{#_Toc298941334}[]{#_Toc257709119}[]{#_Toc317002201}[]{#_Toc317002258}[]{#_Toc317002203}[]{#_Toc317002260}

**DDR命令 \-- DDR配置命令 \-- dialer timer warmup**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DDR命令.files/image001.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7129_13907_471429415}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7129_13907_1037353674}
:::

[ ]{lang="EN-US"}

[**[dialer timer warmup]{lang="EN-US"}**]{#struct_0_x7129_13907_x659977768}[命令用来设置动态路由备份功能在系统启动后的生效延时。]{style="font-family:宋体"}

[**[undo dialer timer warmup]{lang="EN-US"}**]{#struct_0_x7129_13907_1613152942}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_652745683}

[**[dialer timer warmup]{lang="EN-US"}**[ *delay*]{lang="EN-US"}]{#struct_0_x7129_13907_634203197}

[**[undo dialer timer warmup]{lang="EN-US"}**]{#struct_0_x7129_13907_x1961256213}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1903002402}

[[动态路由备份功能在系统启动]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x7129_13907_393755316}[秒后生效。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748559065}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1569760093}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_986480211}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1151771759}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x360703553}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x574062795}

[*[delay]{lang="EN-US"}*]{#struct_0_x7129_13907_x446567735}[：动态路由备份功能在系统启动后不生效的时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2138425895}

[[配有动态路由备份功能的路由器在启动时，主链路如果在本命令配置的时间内没有协商]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_x7129_13907_x1853177328}[，系统就会触发拨号备份链路；当主链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[后，系统会切换回主链路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_590976033}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1748755673}[设置动态路由备份功能在系统启动]{style="font-family:宋体"}[20]{lang="EN-US"}[秒后开始生效。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1103501924}

[\[Sysname\] dialer timer warmup 20]{lang="EN-US"}
:::::

::: {#1279611858 .myid}
[]{#_Toc404785464}[]{#struct_0_x7129_13907_1520686186}[]{#_Toc298941336}[]{#_Toc14925819}

**DDR命令 \-- DDR配置命令 \-- dialer-group**

------------------------------------------------------------------------

[**[dialer-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x171160977}[命令用来配置接口关联的拨号访问组，将该接口与拨号控制规则关联起来。]{style="font-family:宋体"}

[**[undo dialer-group]{lang="EN-US"}**]{#struct_0_x7129_13907_908853751}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_280621769}

[**[dialer-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_x7129_13907_1502377217}

[**[undo dialer-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x787185188}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1395755877}

[[接口不与任何拨号访问组相关联。]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1945455068}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748690137}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_2002994066}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2028464262}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x2147134091}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_267141509}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x136935727}

[*[group-number]{lang="EN-US"}*]{#struct_0_x7129_13907_x501048337}[：接口关联的拨号访问组的序号，这个序号由]{style="font-family:宋体"}**[dialer-group rule]{lang="EN-US"}**[命令设定，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1847945896}

[[一个拨号接口只能关联一个拨号访问组，重复配置]{style="font-family:宋体"}**[dialer-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x711432812}[命令则会覆盖上一次的配置。]{style="font-family:宋体"}

[[用户必须配置]{style="font-family:宋体"}**[dialer-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x1798182553}[命令，否则]{style="font-family:宋体"}[DDR]{lang="EN-US"}[将无法发送报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748886745}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1668646703}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[关联拨号访问组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x25424085}

[\[Sysname\] dialer-group 1 rule acl 3101]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x954469918}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer-group rule]{lang="EN-US"}**]{#struct_0_x7129_13907_x552066363}
:::

::: {#-657898534 .myid}
[]{#_Toc404785465}[]{#struct_0_x7129_13907_x787859968}[]{#_Toc298941337}[]{#_Toc32572701}[]{#_Toc296420457}[]{#_Toc257709115}

**DDR命令 \-- DDR配置命令 \-- dialer-group rule**

------------------------------------------------------------------------

[**[dialer-group rule]{lang="EN-US"}**]{#struct_0_x7129_13907_213062958}[命令用来创建拨号访问组，并配置拨号控制规则。]{style="font-family:宋体"}

[**[undo dialer-group rule]{lang="EN-US"}**]{#struct_0_x7129_13907_x531089135}[命令用来取消该设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_324801006}

[**[dialer-group]{lang="EN-US"}**[ *group-number* **rule** { *protocol-name* { **deny** \| **permit** } \| **acl** { *acl-number* \| **name** *acl-name* } }]{lang="EN-US"}]{#struct_0_x7129_13907_1748821209}

[**[undo dialer-group]{lang="EN-US"}**[ *group-number* **rule**]{lang="EN-US"}]{#struct_0_x7129_13907_1996142440}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x297898148}

[[不存在拨号访问组。]{style="font-family:宋体"}]{#struct_0_x7129_13907_2043642317}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_343756386}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_1742504343}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1084723006}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_189626323}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1092352795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_68710291}

[*[group-number]{lang="EN-US"}*]{#struct_0_x7129_13907_1749017817}[：拨号访问组的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[protocol-name]{lang="EN-US"}*]{#struct_0_x7129_13907_1200880847}[：网络协议名，只能为]{style="font-family:宋体"}**[ip]{lang="EN-US"}**[（表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议）。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x7129_13907_2060460774}[：表示禁止相应协议的报文。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x7129_13907_x214022194}[：表示允许相应协议的报文。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x7129_13907_x1963202438}[：拨号访问组引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[Access Control List]{lang="EN-US"}[，访问控制列表）序号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ acl-name]{lang="EN-US"}*]{#struct_0_x7129_13907_919663932}[：拨号访问组引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x753771362}

[[接口的]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x564363758}[拨号控制规则用于控制接口什么时候发起]{style="font-family:宋体"}[DDR]{lang="EN-US"}[呼叫。用户需要在]{style="font-family:宋体"}[DDR]{lang="EN-US"}[呼叫的发起端配置接口的]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拨号控制规则，在]{style="font-family:宋体"}[DDR]{lang="EN-US"}[呼叫的接收端不用配置接口的]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拨号控制规则。]{style="font-family:宋体"}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_978026190}[拨号控制规则有如下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[根据协议类型过滤报文：本方法目前只能匹配]{style="font-family:宋体"}]{#struct_0_x7129_13907_597887446}[IP]{lang="EN-US"}[协议报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[根据]{style="font-family:宋体"}]{#struct_0_x7129_13907_1748952281}[ACL]{lang="EN-US"}[过滤报文：本方法可以对报文进行更精细的区分。]{style="font-family:宋体"}

[[根据匹配]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x1904780928}[拨号控制规则的结果，报文分为两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[感兴趣]{style="font-family:宋体"}]{#struct_0_x7129_13907_x455439651}[报文：]{lang="EN-US" style="font-family:宋体"}[permit]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[协议]{style="font-family:宋体"}[报文]{lang="EN-US" style="font-family:宋体"}[或者]{style="font-family:宋体"}[符合]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[permit]{lang="EN-US"}[条件的报文]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非感兴趣报文：]{style="font-family:宋体"}]{#struct_0_x7129_13907_x3988791}[deny]{lang="EN-US"}[的]{style="font-family:宋体"}[协议报文或者不符合]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[permit]{lang="EN-US"}[条件的报文或者没有匹配任何规则的报文。]{style="font-family:宋体"}

[[对上述两种报文的处理方式如下：]{style="font-family:宋体"}]{#struct_0_x7129_13907_x740348423}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于感兴趣报文：如果相应链路没有建立，则发起新呼叫建立链路并发送报文；如果相应链路已经建立，]{style="font-family:宋体"}]{#struct_0_x7129_13907_2129966562}[DDR]{lang="EN-US"}[将通过该链路发送报文，并重置]{style="font-family:宋体"}[Idle]{lang="EN-US"}[超时定时器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于非感兴趣报文：如果相应链路没有建立，则不发起呼叫并丢弃此报文；如果相应链路已经建立，]{style="font-family:宋体"}]{#struct_0_x7129_13907_1172520154}[DDR]{lang="EN-US"}[将通过此链路发送报文，但是不重置]{style="font-family:宋体"}[Idle]{lang="EN-US"}[超时定时器。]{style="font-family:宋体"}

[[用户必须配置]{style="font-family:宋体"}[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_x1982712735}[拨号控制规则，并将拨号接口通过]{style="font-family:宋体"}**[dialer-group]{lang="EN-US"}**[命令与拨号控制规则关联起来，]{style="font-family:宋体"}[DDR]{lang="EN-US"}[才能正常拨号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1844203669}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1749148889}[设置拨号访问组]{style="font-family:宋体"}[1]{lang="EN-US"}[，对]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文进行]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拨号，并将它与接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1980110714}

[\[Sysname\] dialer-group 1 rule ip permit]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] dialer-group 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_621355976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dialer-group]{lang="EN-US"}**]{#struct_0_x7129_13907_1623922450}
:::

::: {#-1970667466 .myid}
[]{#_Toc404785466}[]{#struct_0_x7129_13907_1727601649}[]{#_Toc298941338}[]{#_Toc14925826}

**DDR命令 \-- DDR配置命令 \-- display dialer**

------------------------------------------------------------------------

[**[display dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_1704044596}[命令用来显示接口的]{style="font-family:宋体"}[DDR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_477820494}

[**[display dialer]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x7129_13907_x1724517715}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_473059307}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1715899172}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1749083353}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_64606015}

[[network-operator]{lang="EN-US"}]{#struct_0_x7129_13907_x1795639361}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x41972400}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x7129_13907_681616684}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1680920697}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x7129_13907_437417553}[：显示指定接口的]{style="font-family:宋体"}[DDR]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[用来指定接口类型和编号。如果不指定接口，则显示所有接口的]{style="font-family:
宋体"}[DDR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1501332107}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x136731990}[显示所有接口的]{style="font-family:宋体"}[DDR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1748624598}

[Dialer0:]{lang="EN-US"}

[  Dialer Route:]{lang="EN-US"}

[    NextHop: 111.111.111.111  Dialer number: 123456789012345678901234567890]{lang="EN-US"}

[    NextHop: 222.222.222.222  Dialer number: 123456789012345678901234567890]{lang="EN-US"}

[  Dialer number:]{lang="EN-US"}

[  Dialer Timers(in seconds):]{lang="EN-US"}

[    Auto-dial: 300       Compete: 20            Enable: 5]{lang="EN-US"}

[    Idle: 120            Wait-for-Carrier: 60]{lang="EN-US"}

[  Total Channels: 1]{lang="EN-US"}

[  Free Channels: 1]{lang="EN-US"}

[]{#struct_0_x7129_13907_x1102089936}[[表1-1 ]{lang="EN-US"}[display dialer]{lang="EN-US"}]{#_Toc121761884}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1386224010}[[字段]{style="font-family:黑体"}]{#struct_0_x7129_13907_314518201}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1183559168}

[[Dialer0]{lang="EN-US"}]{#struct_0_x7129_13907_x447659865}

[[DDR]{lang="EN-US"}]{#struct_0_x7129_13907_517679877}[接口，可以是]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口也可以是物理接口]{style="font-family:宋体"}

[[Dialer Route:]{lang="EN-US"}]{#struct_0_x7129_13907_1748559062}

[[  NextHop: 111.111.111.111  Dialer number: 123456789012345678901234567890]{lang="EN-US"}]{#struct_0_x7129_13907_x1569563485}

[[在接口上配置的]{style="font-family:宋体"}**[dialer route]{lang="EN-US"}**]{#struct_0_x7129_13907_1387119277}[命令指定的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，以及对应对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的拨号串]{style="font-family:宋体"}

[[Dialer number]{lang="EN-US"}]{#struct_0_x7129_13907_932136729}

[[呼叫单个对端的拨号串]{style="font-family:宋体"}]{#struct_0_x7129_13907_1553325433}

[[Dialer Timers(in seconds):]{lang="EN-US"}]{#struct_0_x7129_13907_760077865}

[[  Auto-dial: 300       Compete: 20            Enable: 5]{lang="EN-US"}]{#struct_0_x7129_13907_x1752453519}

[[  Idle: 120            Wait-for-Carrier: 60]{lang="EN-US"}]{#struct_0_x7129_13907_1748755670}

[[在接口上配置的拨号定时器设置，单位为秒，包括：]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1103305316}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auto-dial]{lang="EN-US"}]{#struct_0_x7129_13907_906226478}[：]{style="font-family:宋体"}**[dialer timer autodial]{lang="EN-US"}**[命令设定的]{lang="EN-US" style="font-family:
  宋体"}[DDR]{lang="EN-US"}[自动拨号的间隔时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Compete]{lang="EN-US"}]{#struct_0_x7129_13907_x1153809398}[：]{style="font-family:宋体"}**[dialer timer compete]{lang="EN-US"}**[命令设定的当接口发生呼叫竞争后的空闲时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_x7129_13907_274579523}[：]{style="font-family:宋体"}**[dialer timer enable]{lang="EN-US"}**[命令设定的当链路断开后进行下次呼叫的间隔时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x7129_13907_369088871}[：]{style="font-family:宋体"}**[dialer timer idle]{lang="EN-US"}**[命令设定的当接口的呼叫建立后，允许链路空闲的时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-for-Carrier]{lang="EN-US"}]{#struct_0_x7129_13907_x595482133}[：]{style="font-family:宋体"}**[dialer timer wait-carrier]{lang="EN-US"}**[命令设定]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[呼叫建立超时定时器（]{lang="EN-US" style="font-family:宋体"}[wait-carrier]{lang="EN-US"}[定时器）的超时时间]{lang="EN-US" style="font-family:宋体"}

[[Total Channels]{lang="EN-US"}]{#struct_0_x7129_13907_1748690134}

[[该接口总共的通道数（通道数指的是物理接口的个数，对于]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_x7129_13907_2003190674}[接口来说，指的是]{style="font-family:宋体"}[B]{lang="EN-US"}[通道的个数）]{style="font-family:宋体"}

[[Free Channels]{lang="EN-US"}]{#struct_0_x7129_13907_869078785}

[[空闲的通道数]{style="font-family:宋体"}]{#struct_0_x7129_13907_x231348534}

[ ]{lang="EN-US"}

::: {#-1672234898 .myid}
[]{#_Toc404785467}[]{#struct_0_x7129_13907_x1638562035}[]{#_Toc327888471}[]{#_Toc323804934}

**DDR命令 \-- DDR配置命令 \-- display interface dialer**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}[dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_1065227020}[命令用来显示]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748886742}

[**[display interface ]{lang="EN-US"}**[\[ **dialer** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x7129_13907_x421124840}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_106442341}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x502943464}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_37387561}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1663624215}

[[network-operator]{lang="EN-US"}]{#struct_0_x7129_13907_489091350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1495786640}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x7129_13907_x1956888186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1748821206}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x7129_13907_1995683688}[：显示指定]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的编号，取值范围为已创建的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x7129_13907_x2104886622}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x7129_13907_1117711003}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x7129_13907_1494746512}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x599093207}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x7129_13907_1471793007}**[dialer]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1174886079}**[dialer]{lang="EN-US"}**[参数，不指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x156351954}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1749017814}[显示接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface dialer 1]{lang="EN-US"}]{#struct_0_x7129_13907_1201077455}

[Dialer1 ]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP (spoofing)]{lang="EN-US"}

[Description: Dialer1 Interface]{lang="EN-US"}

[Bandwidth: 64kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Hold timer: 10 seconds, retry times: 5]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Link layer protocol: PPP]{lang="EN-US"}

[LCP: initial]{lang="EN-US"}

[Physical: Dialer, baudrate: 64000 bps]{lang="EN-US"}

[Output queue: (Urgent queuing: Length) 50]{lang="EN-US"}

[Output queue: (Protocol queuing: Length) 500]{lang="EN-US"}

[Output queue: (FIFO queuing: Length) 75]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1078165058}[显示接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface dialer 1 brief]{lang="EN-US"}]{#struct_0_x7129_13907_1748952278}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[Dia1                 UP   UP(s)    \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1905239683}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface dialer brief down]{lang="EN-US"}]{#struct_0_x7129_13907_1282771255}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface              Link Cause]{lang="EN-US"}

[Dia1                   ADM  Administratively]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display interface dialer]{lang="EN-US"}]{#struct_0_x7129_13907_944040881}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1380173237}[[字段]{style="font-family:黑体"}]{#struct_0_x7129_13907_1723139537}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7129_13907_1086803252}

[[Dialer1 ]{lang="EN-US"}]{#struct_0_x7129_13907_465437138}

[[Current state]{lang="EN-US"}]{#struct_0_x7129_13907_1749148886}

[[接口当前的物理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1980307322}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x7129_13907_871578557}[：该接口的物理状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x7129_13907_x523010954}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，需要通过]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x7129_13907_149094512}

[[接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x7129_13907_673166677}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x7129_13907_1017253174}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x7129_13907_1749083350}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x7129_13907_64409407}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x7129_13907_x329305285}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x7129_13907_1791075118}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x7129_13907_699053694}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x7129_13907_1280844693}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x7129_13907_1748624599}

[[Hold timer]{lang="EN-US"}]{#struct_0_x7129_13907_1059765133}

[[该接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x7129_13907_x896550011}[报文的周期]{style="font-family:宋体"}

[[retry times]{lang="EN-US"}]{#struct_0_x7129_13907_x896550006}

[[在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x7129_13907_x896550008}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路]{style="font-family:宋体"}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x7129_13907_x1102024400}

[[网络层协议处理状况]{style="font-family:宋体"}]{#struct_0_x7129_13907_517969554}

[[Link layer protocol]{lang="EN-US"}]{#struct_0_x7129_13907_x1642036578}

[[链路层封装的协议]{style="font-family:宋体"}]{#struct_0_x7129_13907_x265198617}

[[LCP: initial]{lang="EN-US"}]{#struct_0_x7129_13907_556039146}

[[LCP]{lang="EN-US"}]{#struct_0_x7129_13907_1748559063}[（链路控制协议）初始化完成]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x7129_13907_x1569629021}

[[接口的物理类型]{style="font-family:宋体"}]{#struct_0_x7129_13907_202290441}

[[baudrate]{lang="EN-US"}]{#struct_0_x7129_13907_641553321}

[[接口的波特率]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1722054391}

[[Output queue: (Urgent queuing : Length)]{lang="EN-US"}]{#struct_0_x7129_13907_1748755671}

[[紧急发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1103370852}

[[Output queue: (Protocol queuing : Length)]{lang="EN-US"}]{#struct_0_x7129_13907_1244130394}

[[协议发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x7129_13907_1241072560}

[[Output queue: (FIFO queuing : Length)]{lang="EN-US"}]{#struct_0_x7129_13907_x446342490}

[[先入先出发送队列的报文统计]{style="font-family:宋体"}]{#struct_0_x7129_13907_1748690135}

[[Last clearing of counters: Never]{lang="EN-US"}]{#struct_0_x7129_13907_2003125138}

[[最后一次清除接口统计信息的时间（]{style="font-family:宋体"}[Never]{lang="EN-US"}]{#struct_0_x7129_13907_x1077649908}[表示未清除过接口的统计信息）]{style="font-family:宋体"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_x7129_13907_1328320110}

[[最近五分钟时间内接口的输入速率]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1739508732}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_x7129_13907_1748886743}

[[最近五分钟时间内接口的输出速率]{style="font-family:宋体"}]{#struct_0_x7129_13907_1669039919}

[[Input: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}]{#struct_0_x7129_13907_1929978767}

[[该接口接收的数据报文个数、字节数，以及由于没有接收缓冲而被丢弃的报文个数]{style="font-family:宋体"}]{#struct_0_x7129_13907_x722085997}

[[Output: 0 packets, 0 bytes, 0 droped]{lang="EN-US"}]{#struct_0_x7129_13907_1748821207}

[[该接口发送的数据报文个数、字节数，以及由于没有发送缓冲而被丢弃的报文个数]{style="font-family:宋体"}]{#struct_0_x7129_13907_1995749224}

[[Brief information on interface(s) under route mode:]{lang="EN-US"}]{#struct_0_x7129_13907_x2086584613}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_x7129_13907_812864330}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x7129_13907_1749017815}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x7129_13907_1201011919}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x7129_13907_x1045784444}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x7129_13907_406195172}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x7129_13907_1748952279}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，则表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x7129_13907_x1905305219}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x7129_13907_842069368}

[[Link]{lang="EN-US"}]{#struct_0_x7129_13907_1613146880}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x7129_13907_1749148887}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x7129_13907_x1980241786}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x7129_13907_410229425}[：表示接口被手工关闭了，需要执行]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x7129_13907_x636320601}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x7129_13907_1749083351}

[[接口数据链路层协议状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x7129_13907_64474943}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x7129_13907_1377693344}[：表示接口的数据链路层是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x7129_13907_1132439900}[：表示接口的数据链路层不通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP(s)]{lang="EN-US"}]{#struct_0_x7129_13907_x1031191340}[：表示接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x7129_13907_x980258753}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7129_13907_x1169580181}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x7129_13907_x703273108}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_x7129_13907_x921994204}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_x7129_13907_x980324289}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x7129_13907_x52357379}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1671782160}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x7129_13907_x932110891}

::: {#1717908769 .myid}
[]{#_Toc404785468}[]{#struct_0_x7129_13907_x497753591}[]{#_Toc298941340}[]{#_Toc257709125}[]{#_Toc317002209}[]{#_Toc317002266}[]{#_Toc317002210}[]{#_Toc317002267}[]{#_Toc317002211}[]{#_Toc317002268}[]{#_Toc296420460}[]{#_Toc32572696}[]{#_Toc14925815}[]{#_Toc296420461}[]{#_Toc296420462}[]{#_Toc296420463}[]{#_Toc257709121}[]{#_Toc32572700}

**DDR命令 \-- DDR配置命令 \-- interface dialer**

------------------------------------------------------------------------

[**[interface dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_1921239168}[命令用创建一个]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口。如果当前已经配置该接口，此命令用来进入该接口视图。]{style="font-family:宋体"}

[**[undo interface dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_x980127681}[命令用来删除一个指定的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_748528176}

[**[interface dialer]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x7129_13907_264688203}

[**[undo interface dialer]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x7129_13907_x1918219085}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_207859864}

[[未创建]{style="font-family:宋体"}[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x208567339}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2032578797}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_1150029016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1910592845}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1628431544}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x980193217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x797126707}

[*[number]{lang="EN-US"}*]{#struct_0_x7129_13907_1935085271}[：]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口序号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1721617945}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1305132798}[接口的波特率恒定为]{style="font-family:宋体"}[64000bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1942996338}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1343904630}[创建一个接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1940877378}

[\[Sysname\] interface dialer 1]{lang="EN-US"}
:::

::: {#988247972 .myid}
[]{#_Toc404785469}[]{#struct_0_x7129_13907_371653580}[]{#_Toc327888473}[]{#_Toc296420464}[]{#_Toc257709122}

**DDR命令 \-- DDR配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x7129_13907_x1018406184}[命令用来设置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x7129_13907_x979996609}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1212464774}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x7129_13907_865916682}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x7129_13907_1868568}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_501391156}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1801420409}[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x34528410}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x532791744}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x545690082}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x980062145}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x828679476}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x910353650}

[*[size]{lang="EN-US"}*]{#struct_0_x7129_13907_295924848}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2043953874}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x7129_13907_469090125}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x229847614}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1905226432}[设置接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1200]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_322830075}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[[\[Sysname-Dialer1\] mtu 1200]{lang="EN-US"}]{#struct_0_x7129_13907_x979865537}
:::

::: {#494830852 .myid}
[]{#_Toc404785470}[]{#struct_0_x7129_13907_1378348704}[]{#_Toc351029823}

**DDR命令 \-- DDR配置命令 \-- ppp callback**

------------------------------------------------------------------------

[**[ppp callback]{lang="EN-US"}**]{#struct_0_x7129_13907_1804243026}[命令用来允许]{style="font-family:宋体"}[PPP]{lang="EN-US"}[发送或接受回呼请求。]{style="font-family:宋体"}

[**[undo ppp callback]{lang="EN-US"}**]{#struct_0_x7129_13907_2044702607}[命令用来禁止]{style="font-family:宋体"}[PPP]{lang="EN-US"}[发送或接受]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼请求。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1354936832}

[**[ppp callback]{lang="EN-US"}**[ { **client** \| **server** }]{lang="EN-US"}]{#struct_0_x7129_13907_x1277792244}

[**[undo ppp callback]{lang="EN-US"}**[ { **client** \| **server** }]{lang="EN-US"}]{#struct_0_x7129_13907_905891752}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1245975491}

[[系统未启动回呼功能。]{style="font-family:宋体"}]{#struct_0_x7129_13907_1228399847}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1377758881}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1973252154}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x459158962}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1647482584}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_54024739}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1686806290}

[[在]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x7129_13907_x365928536}[回呼的配置中，需要配置发送呼叫方作为]{style="font-family:宋体"}[Client]{lang="EN-US"}[端，同时配置接受呼叫方作为]{style="font-family:宋体"}[Server]{lang="EN-US"}[端。由]{style="font-family:宋体"}[Client]{lang="EN-US"}[端首先发起呼叫，]{style="font-family:宋体"}[Server]{lang="EN-US"}[端确认该呼叫是否进行回呼，若需要回呼，]{style="font-family:宋体"}[Server]{lang="EN-US"}[端则立即挂断该次呼入连接，并根据用户名或回呼字符串等信息向]{style="font-family:宋体"}[Client]{lang="EN-US"}[端再次发起呼叫。]{style="font-family:宋体"}

[[利用]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x7129_13907_1934654672}[回呼功能可以为]{style="font-family:宋体"}[PPP Client]{lang="EN-US"}[端节省通信费用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x650231194}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x622035644}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[允许接受回呼请求。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x964713826}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp callback server]{lang="EN-US"}
:::

::: {#7519082 .myid}
[]{#_Toc404785471}[]{#struct_0_x7129_13907_1377824417}[]{#_Toc351029824}[]{#_Toc351022527}

**DDR命令 \-- DDR配置命令 \-- ppp callback ntstring**

------------------------------------------------------------------------

[**[ppp callback ntstring]{lang="EN-US"}**]{#struct_0_x7129_13907_x1592326550}[命令用来设置从]{style="font-family:宋体"}[Windows NT Server]{lang="EN-US"}[回呼路由器时所需要的拨号串。]{style="font-family:宋体"}

[**[undo ppp callback ntstring]{lang="EN-US"}**]{#struct_0_x7129_13907_x2100513795}[命令用来取消设置的回呼拨号串。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2122415621}

[**[ppp callback ntstring]{lang="EN-US"}**[ *dial-number*]{lang="EN-US"}]{#struct_0_x7129_13907_x755250668}

[**[undo ppp callback ntstring]{lang="EN-US"}**]{#struct_0_x7129_13907_2009002464}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x287232455}

[[没有设置]{style="font-family:宋体"}[Windows NT Server]{lang="EN-US"}]{#struct_0_x7129_13907_1527995149}[回呼拨号串。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1693199125}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x158835865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2141475836}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1197008452}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1377889953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1529813647}

[*[dial-number]{lang="EN-US"}*]{#struct_0_x7129_13907_70226092}[：从]{style="font-family:宋体"}[Windows NT Server]{lang="EN-US"}[回呼路由器的拨号串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1789969206}

[[当路由器作为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x7129_13907_x116087061}[回呼的]{style="font-family:宋体"}[Client]{lang="EN-US"}[端呼叫作为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼]{style="font-family:宋体"}[Server]{lang="EN-US"}[端的]{style="font-family:宋体"}[Windows NT Server]{lang="EN-US"}[时，如果]{style="font-family:宋体"}[NT Server]{lang="EN-US"}[需要路由器发送回呼号码，则需要配置此命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x231258542}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1640462651}[设定从]{style="font-family:宋体"}[Windows NT Server]{lang="EN-US"}[回呼路由器的拨号串为]{style="font-family:宋体"}[1234567]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1109901514}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] ppp callback ntstring 1234567]{lang="EN-US"}
:::

::: {#2052875588 .myid}
[]{#_Toc404785472}[]{#struct_0_x7129_13907_x1127849771}[]{#_Toc327888474}[]{#_Toc323804933}[]{#_Toc317002216}[]{#_Toc317002273}[]{#_Toc317002218}[]{#_Toc317002275}[]{#_Toc296420465}[]{#_Toc257709123}[]{#_Toc32572705}

**DDR命令 \-- DDR配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x7129_13907_x1263715369}[命令用来清除]{style="font-family:
宋体"}[Dialer]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1304573646}

[**[reset counters interface]{lang="EN-US"}**[ \[ **dialer** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x7129_13907_1584377512}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_460641636}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x582485850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_987859957}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_319895828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x543118796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x979931073}

[**[dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_x340095420}[：清除]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x7129_13907_x1845579109}[：]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的编号。取值范围为已创建的]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_2086442081}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x7129_13907_1640596023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}**[dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_x749041774}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_436831491}[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}**[dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_1549799701}[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_922574055}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x979734465}[清除接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface dialer 1]{lang="EN-US"}]{#struct_0_x7129_13907_x344861428}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1724676497}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}[dialer]{lang="EN-US"}**]{#struct_0_x7129_13907_x491858526}
:::

::::: {#-780779607 .myid}
[]{#_Toc404785473}[]{#struct_0_x7129_13907_1494877582}[]{#_Toc356202460}[]{#_Toc355357310}[]{#_Toc342919797}[]{#_Toc335656821}[]{#_Toc303865071}[]{#_Toc215545670}[]{#_Toc215479545}

**DDR命令 \-- DDR配置命令 \-- service**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](DDR命令.files/image002.png){#图片 7 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x7129_13907_1494680974}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7129_13907_53303396}
:::

[ ]{lang="EN-US"}

[**[service]{lang="EN-US"}**]{#struct_0_x7129_13907_1494746510}[命令用来指定转发当前]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口流量的业务处理板。]{style="font-family:宋体"}

[**[undo service]{lang="EN-US"}**]{#struct_0_x7129_13907_x752336509}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2101004635}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7129_13907_1494549902}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[service slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x7129_13907_1295531671}

[**[undo service slot]{lang="EN-US"}**]{#struct_0_x7129_13907_x1384914070}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7129_13907_1494615438}[模式：]{style="font-family:宋体"}

[**[service ]{lang="EN-US"}[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x7129_13907_x373311943}

[**[undo service ]{lang="EN-US"}[chassis]{lang="EN-US"}**]{#struct_0_x7129_13907_x1697673849}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1495074189}

[[没有指定转发当前]{style="font-family:宋体"}[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_40643345}[接口流量的业务处理板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x125430311}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1495139725}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_63520537}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1494943117}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_2018507190}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1362465447}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7129_13907_1495008653}[：指定单板所在的槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7129_13907_842445784}[：指定设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x7129_13907_x1498219737}[：指定设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7129_13907_x533276570}[：指定成员设备上的指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x7129_13907_1230663618}[：指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1494812045}

[[没有通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**]{#struct_0_x7129_13907_x1896649101}[命令指定]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口流量的业务处理板时，会自动选择主控板作为转发]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口流量的业务处理板。在这种情况下，为了避免主控板处理过多的业务，建议在]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口下通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**[命令指定转发该接口流量的业务处理板。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_23410029}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1494877581}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板处理]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[接口的流量。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_807455816}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1875072655}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备处理]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[接口的流量。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1494680973}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] service slot 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_53368932}[指定在]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备的]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板处理]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[接口的流量。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_1494746509}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\]]{lang="EN-US"}[ ]{lang="EN-US"}[service ]{lang="IT"}[chassis]{lang="EN-US"}[ ]{lang="EN-US"}[2 slot 2]{lang="IT"}
:::::

::: {#1170655049 .myid}
[]{#_Toc404785474}[]{#struct_0_x7129_13907_358187475}[]{#_Toc327888475}[]{#_Toc323804931}[]{#_Toc32572702}[]{#_Toc14925821}[]{#_Toc296420466}[]{#_Toc296420467}

**DDR命令 \-- DDR配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x7129_13907_1909800944}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x7129_13907_1116611302}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1337954376}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x7129_13907_961823115}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x7129_13907_1344843352}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x979800001}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x1912274173}[接口处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_419342493}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x1681451367}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1060588107}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x2039346406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1601406334}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_558865565}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x1764184513}[关闭接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x980258752}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] shutdown]{lang="EN-US"}
:::

::: {#1864605471 .myid}
[]{#_Toc404785475}[]{#struct_0_x7129_13907_x1169514645}[]{#_Toc298941344}[]{#_Toc257709129}[]{#_Toc296420468}[]{#_Toc257709126}[]{#_Toc32572703}[]{#_Toc14925824}[]{#_Toc296420469}[]{#_Toc257709127}[]{#_Toc32572704}[]{#_Toc14925825}[]{#_Toc36458480}[]{#_Toc36458481}[]{#_Toc36458483}[]{#_Toc36458484}[]{#_Toc36458485}[]{#_Toc36458486}[]{#_Toc36458487}[]{#_Toc36458488}[]{#_Toc36458489}[]{#_Toc36458490}[]{#_Toc36458491}[]{#_Toc36458492}[]{#_Toc36458493}[]{#_Toc36458497}[]{#_Toc36458498}[]{#_Toc36458501}[]{#_Toc36458502}[]{#_Toc36458521}[]{#_Toc32572708}[]{#_Toc33360440}[]{#_Toc32572710}[]{#_Toc33360442}[]{#_Toc32572711}[]{#_Toc33360443}[]{#_Toc32572712}[]{#_Toc33360444}[]{#_Toc32572713}[]{#_Toc33360445}[]{#_Toc32572714}[]{#_Toc33360446}[]{#_Toc32572715}[]{#_Toc33360447}[]{#_Toc32572716}[]{#_Toc33360448}[]{#_Toc32572717}[]{#_Toc33360449}[]{#_Toc32572718}[]{#_Toc33360450}[]{#_Toc32572719}[]{#_Toc33360451}[]{#_Toc32572724}[]{#_Toc33360456}[]{#_Toc205799397}[]{#_Toc132770128}[]{#_Toc296420470}[]{#_Toc257709128}[]{#_Toc219967431}[]{#_Toc213490054}[]{#_Toc207010309}[]{#_Toc207010042}

**DDR命令 \-- DDR配置命令 \-- standby routing-group**

------------------------------------------------------------------------

[**[standby routing-group]{lang="EN-US"}**]{#struct_0_x7129_13907_1717886236}[命令用来在备份接口上启用动态路由备份功能，并配置引用的动态路由备份组。]{style="font-family:宋体"}

[**[undo standby routing-group]{lang="EN-US"}**]{#struct_0_x7129_13907_x1789465259}[命令用来在备份接口上关闭动态路由备份功能，或取消引用的动态路由备份组。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x867248344}

[**[standby routing-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_x7129_13907_1901296582}

[**[undo standby routing-group]{lang="EN-US"}**[ *group-number*]{lang="EN-US"}]{#struct_0_x7129_13907_x1396830886}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x36659061}

[[动态路由备份功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7129_13907_182788390}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_62886057}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x980324288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x52422915}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_342497829}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x600453352}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1739752245}

[*[group-number]{lang="EN-US"}*]{#struct_0_x7129_13907_x207369379}[：动态路由备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1259407995}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[启用动态路由备份功能之前，必须确保备份接口上已经配置了]{style="font-family:宋体"}]{#struct_0_x7129_13907_x494865321}[DDR]{lang="EN-US"}[拨号功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个备份接口上可以同时引用多个动态路由备份组。]{style="font-family:宋体"}]{#struct_0_x7129_13907_825132156}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x700921246}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x980127680}[在]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[接口上启用动态路由备份功能，并引用动态路由备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x7129_13907_748462640}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] standby routing-group 1]{lang="EN-US"}
:::

::: {#1939769910 .myid}
[]{#_Toc404785476}[]{#struct_0_x7129_13907_x116111876}[]{#_Toc298941345}[]{#_Toc132770129}[]{#_Toc296420471}

**DDR命令 \-- DDR配置命令 \-- standby routing-group rule**

------------------------------------------------------------------------

[**[standby routing-group rule]{lang="EN-US"}**]{#struct_0_x7129_13907_1382833530}[命令用来创建动态路由备份组，并配置需监控的网段。]{style="font-family:
宋体"}

[**[undo standby routing-group rule]{lang="EN-US"}**]{#struct_0_x7129_13907_758448592}[命令用来删除动态路由备份组，或删除动态路由备份组中的需监控网段。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x697523188}

[**[standby routing-group ]{lang="EN-US"}***[group-number]{lang="EN-US"}***[ rule]{lang="EN-US"}**[ **ip** *ip-address* { *mask* \| *mask-length* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x7129_13907_x1753626564}

[**[undo]{lang="EN-US"}**[ **standby routing-group** *group-number* **rule** \[ **ip** *ip-address* { *mask* \| *mask-length* } \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x7129_13907_1724417305}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1708933440}

[[没有创建动态路由备份组。]{style="font-family:宋体"}]{#struct_0_x7129_13907_x980193216}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x797061171}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x824659804}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1756961549}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_713928530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x284445620}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x760181773}

[*[group-number]{lang="EN-US"}*]{#struct_0_x7129_13907_1907594584}[：动态路由备份组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x7129_13907_569439675}[：表示需监控的网段地址。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x7129_13907_x1304350468}[：网络掩码。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x7129_13907_x979996608}[：网络掩码的长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x7129_13907_1212530310}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x688126845}

[[一个动态路由备份组内，最多可配置]{style="font-family:宋体"}[255]{lang="EN-US"}]{#struct_0_x7129_13907_1383148952}[个被监控网段。只有到一个动态路由备份组内的所有被监控网段都不存在]{style="font-family:宋体"}[[有效路由]{style="font-family:宋体"}]{.ItemListChar}[时，才认为主链路断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1507405184}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_965646122}[设置动态路由备份组]{style="font-family:宋体"}[1]{lang="EN-US"}[，用于监控到达网段]{style="font-family:宋体"}[20.0.0.0/8]{lang="EN-US"}[和]{style="font-family:宋体"}[30.0.0.0/8]{lang="EN-US"}[的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1767715429}

[\[Sysname\] standby routing-group 1 rule ip 20.0.0.1 255.0.0.0]{lang="EN-US"}

[\[Sysname\] standby routing-group 1 rule ip 30.0.0.1 255.0.0.0]{lang="EN-US"}
:::

::: {#-498056319 .myid}
[]{#_Toc404785477}[]{#struct_0_x7129_13907_1377449618}[]{#_Toc298941346}[]{#_Toc132770127}[]{#_Toc296420472}[]{#_Toc257709130}[]{#_Toc205799398}

**DDR命令 \-- DDR配置命令 \-- standby timer routing-disable**

------------------------------------------------------------------------

[**[standby timer routing-disable]{lang="EN-US"}**]{#struct_0_x7129_13907_1217338127}[命令用来配置主链路接通后断开备份链路的延迟时间。]{style="font-family:
宋体"}

[**[undo standby timer routing-disable]{lang="EN-US"}**]{#struct_0_x7129_13907_x980062144}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x828745012}

[**[standby timer routing-disable ]{lang="EN-US"}***[delay]{lang="EN-US"}*]{#struct_0_x7129_13907_1465689003}

[**[undo]{lang="EN-US"}**[ **standby timer routing-disable**]{lang="EN-US"}]{#struct_0_x7129_13907_1990533965}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_522582579}

[[主链路接通后断开备份链路的延迟时间为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_x7129_13907_x438123622}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1125165399}

[[拨号接口视图]{style="font-family:宋体"}]{#struct_0_x7129_13907_x1863022905}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1875911607}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_150978373}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x979865536}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1127915307}

[*[delay]{lang="EN-US"}*]{#struct_0_x7129_13907_x575772600}[：主链路接通后断开备份链路的延迟时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1242698793}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_203351460}[在接口]{style="font-family:宋体"}[BRI2/4/0]{lang="EN-US"}[上设置当主链路接通后断开备份链路的延迟时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x416270767}

[\[Sysname\] interface bri 2/4/0]{lang="EN-US"}

[\[Sysname-Bri2/4/0\] standby timer routing-disable 5]{lang="EN-US"}
:::

::: {#1474946988 .myid}
[]{#_Toc404785478}[]{#struct_0_x7129_13907_469553653}[]{#_Toc327888476}[]{#_Toc317856915}[]{#_Toc309228573}[]{#_Toc205607563}[]{#_Toc355282403}[]{#_Toc355343578}[]{#_Toc355357269}[]{#_Toc317002227}[]{#_Toc317002284}[]{#_Toc296420473}[]{#_Toc257709131}[]{#_Toc205799399}

**DDR命令 \-- DDR配置命令 \-- timer-hold**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**]{#struct_0_x7129_13907_x498717435}[命令用来配置接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期。]{style="font-family:宋体"}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x7129_13907_2096208614}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x979931072}

[**[timer-hold]{lang="EN-US"}**[ *period*]{lang="EN-US"}]{#struct_0_x7129_13907_x340029884}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x7129_13907_88549845}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1120420792}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_158544739}[接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_478991559}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_1207085093}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1641442024}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1908188643}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_1830253029}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x979734464}

[*[period]{lang="EN-US"}*]{#struct_0_x7129_13907_x344795892}[：接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x2074823767}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x7129_13907_x742690948}[时，链路层会定期向对端发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。用户可以通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改接口发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期。]{style="font-family:宋体"}

[[在速率非常低的链路上，参数]{style="font-family:宋体"}*[period]{lang="EN-US"}*]{#struct_0_x7129_13907_x660598381}[不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送与接收。而接口如果在多个（可以通过]{style="font-family:宋体"}**[timer-hold retry]{lang="EN-US"}**[命令修改该个数）]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期之后仍然无法收到对端的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，它就会认为链路发生故障。如果]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x237732780}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_x399782924}[配置接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的周期为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_x1138475756}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] timer-hold 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_1048206961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_x7129_13907_1048206958}
:::

::: {#518520923 .myid}
[]{#_Toc404785479}[]{#struct_0_x7129_13907_1048206959}[]{#_Toc394763468}

**DDR命令 \-- DDR配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**[ **retry**]{lang="EN-US"}]{#struct_0_x7129_13907_1048206956}[命令用来配置接口在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x7129_13907_1048206957}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_670992505}

[**[timer-hold]{lang="EN-US"}**[ **retry** *retry*]{lang="EN-US"}]{#struct_0_x7129_13907_1048206954}

[**[undo timer-hold retry]{lang="EN-US"}**]{#struct_0_x7129_13907_1048206955}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x908108174}

[[接口在]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x7129_13907_x458189390}[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1290445200}

[[Dialer]{lang="EN-US"}]{#struct_0_x7129_13907_x1290445199}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1290445202}

[[network-admin]{lang="EN-US"}]{#struct_0_x7129_13907_x1290445201}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7129_13907_788469728}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x1290445204}

[*[retry]{lang="EN-US"}*]{#struct_0_x7129_13907_x1290445203}[：接口在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7129_13907_x374329686}

[[当接口上封装的链路层协议为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x7129_13907_x1290445206}[时，链路层会定期（可以通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令修改]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送周期）向对端发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。如果在一段时间内无法收到对端发来的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，链路层会认为对端故障，上报链路层]{style="font-family:宋体"}[Down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[用户可以通过]{style="font-family:宋体"}**[timer-hold retry]{lang="EN-US"}**]{#struct_0_x7129_13907_x1290445205}[命令修改接口在多少个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[[在速率非常低的链路上，参数]{style="font-family:宋体"}*[retry]{lang="EN-US"}*]{#struct_0_x7129_13907_283532914}[不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送与接收。而接口如果在]{style="font-family:宋体"}*[retry]{lang="EN-US"}*[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期之后仍然无法收到对端的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文，它就会认为链路发生故障。如果]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7129_13907_283532915}

[[\# ]{lang="EN-US"}]{#struct_0_x7129_13907_1873688623}[配置接口]{style="font-family:宋体"}[Dialer1]{lang="EN-US"}[在]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[周期内没有收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的应答就拆除链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7129_13907_283532912}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] timer-hold retry 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7129_13907_283532913}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_x7129_13907_1873688629}

[ ]{lang="EN-US"}
:::
