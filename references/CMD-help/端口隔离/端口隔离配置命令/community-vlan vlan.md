::::: {#1319232810 .myid}
[]{#_Toc297622997}[]{#_Toc297378618}[]{#_Toc185927307}[]{#_Toc123026767}[]{#_Toc29974884}[]{#_Toc25576880}[]{#_Toc15724192}[]{#_Toc404784053}[]{#_Toc381104186}[]{#struct_0_x1857_11373_1681157279}[]{#_Toc341367947}[]{#_Toc333043090}[]{#_Toc328744057}[]{#_Toc300319264}

**端口隔离 \-- 端口隔离配置命令 \-- community-vlan vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](端口隔离命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1857_11373_x1945184984}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1857_11373_x1346610831}
:::

**[ ]{lang="EN-US"}**

[**[community-vlan vlan]{lang="EN-US"}**]{#struct_0_x1857_11373_x275095464}[命令用来配置当前隔离组中的非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo community-vlan]{lang="EN-US"}**]{#struct_0_x1857_11373_1430675306}[命令用来删除当前隔离组中的所有非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1857_11373_1389940178}

[**[community-vlan vlan]{lang="EN-US"}**[ { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_x1857_11373_1511159374}

[**[undo community-vlan]{lang="EN-US"}**]{#struct_0_x1857_11373_1015821639}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1857_11373_491294595}

[[隔离组中未配置非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1857_11373_1712475301}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1606262159}

[[隔离组视图]{style="font-family:宋体"}]{#struct_0_x1857_11373_x1346545295}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x249153433}

[[network-admin]{lang="EN-US"}]{#struct_0_x1857_11373_1723243567}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1857_11373_1895535092}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1857_11373_431404516}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x1857_11373_x1412542995}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示设置当前隔离组中非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的范围。表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1857_11373_2085639265}[：表示设置]{style="font-family:宋体"}[当前隔离组中所有的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1857_11373_1782332152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令仅适用于运行模式为独立运行模式、或处于]{style="font-family:宋体"}]{#struct_0_x1857_11373_x1491104159}[IRF]{lang="EN-US"}[模式但没有配置]{style="font-family:宋体"}[IRF]{lang="EN-US"}[增强功能的设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[community-vlan vlan]{lang="EN-US"}**]{#struct_0_x1857_11373_x1405928031}[命令时，如果当前隔离组中已存在非隔离]{lang="EN-US" style="font-family:
宋体"}[VLAN]{lang="EN-US"}[，必须先执行]{lang="EN-US" style="font-family:宋体"}**[undo community-vlan]{lang="EN-US"}**[命令（重复配置除外）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1346479759}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_1295971635}[配置隔离组]{style="font-family:宋体"}[1]{lang="EN-US"}[中的]{style="font-family:宋体"}[VLAN 3]{lang="EN-US"}[为非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1857_11373_x1393302806}

[\[Sysname\] port-isolate group 1]{lang="EN-US"}

[\[Sysname-port-isolate-group1\] community-vlan vlan 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1405993567}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-isolate group]{lang="EN-US"}**]{#struct_0_x1857_11373_x1972767511}
:::::

::::: {#-1127724438 .myid}
[]{#_Toc404784054}[]{#_Toc381104187}[]{#struct_0_x1857_11373_1296593197}

**端口隔离 \-- 端口隔离配置命令 \-- display port-isolate group**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](端口隔离命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1857_11373_x1893795262}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1857_11373_x977677047}
:::

**[ ]{lang="EN-US"}**

[**[display port-isolate group]{lang="EN-US"}**]{#struct_0_x1857_11373_x1751561780}[命令用来显示隔离组的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1857_11373_96874853}

[[单隔离组设备：]{style="font-family:宋体"}]{#struct_0_x1857_11373_1218686880}

[**[display port-isolate group]{lang="EN-US"}**]{#struct_0_x1857_11373_x1346414223}

[[多隔离组设备：]{style="font-family:宋体"}]{#struct_0_x1857_11373_x1978108136}

[**[display port-isolate group ]{lang="EN-US"}**[\[ *group-number* \]]{lang="EN-US"}]{#struct_0_x1857_11373_1370742610}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x416539171}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1857_11373_1236075198}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1585918453}

[[network-admin]{lang="EN-US"}]{#struct_0_x1857_11373_1874089951}

[[network-operator]{lang="EN-US"}]{#struct_0_x1857_11373_x1316021353}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1857_11373_493703550}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1857_11373_x1508329199}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1857_11373_1836090602}

[*[group-number]{lang="EN-US"}*]{#struct_0_x1857_11373_x1346348687}[：隔离组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。（多隔离组设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1628757599}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_1613340654}[显示隔离组的信息。（单隔离组设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-isolate group]{lang="EN-US"}]{#struct_0_x1857_11373_1773339978}

[ Port isolation group information:]{lang="EN-US"}

[ Group ID: 1]{lang="EN-US"}

[ Group members:]{lang="EN-US"}

[    GigabitEthernet1/0/2]{lang="EN-US"}

[ Community VLAN ID: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_1951996855}[显示所有隔离组的信息。（多隔离组设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-isolate group]{lang="EN-US"}]{#struct_0_x1857_11373_560293965}

[ Port isolation group information:]{lang="EN-US"}

[ Group ID: 2]{lang="EN-US"}

[ Group members:]{lang="EN-US"}

[    GigabitEthernet1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Group ID: 5]{lang="EN-US"}

[ Group members:]{lang="EN-US"}

[    GigabitEthernet1/0/2            GigabitEthernet1/0/4]{lang="EN-US"}

[ Community VLAN ID: 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_x1347331727}[显示隔离组]{style="font-family:宋体"}[2]{lang="EN-US"}[的信息。（多隔离组设备）]{style="font-family:宋体"}

[[\<Sysname\> display port-isolate group 2]{lang="EN-US"}]{#struct_0_x1857_11373_x1495913528}

[ Port isolation group information:]{lang="EN-US"}

[ Group ID: 2]{lang="EN-US"}

[ Group members:]{lang="EN-US"}

[    GigabitEthernet1/0/1]{lang="EN-US"}

[ Community VLAN ID: 1(default), 2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display port-isolate group]{lang="EN-US"}]{#struct_0_x1857_11373_x534821432}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1139341934}[[字段]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1443271042}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1347266191}

[[Port isolation group information]{lang="EN-US"}]{#struct_0_x1857_11373_x2080761171}

[[端口隔离组的信息]{style="font-family:宋体"}]{#struct_0_x1857_11373_x167692023}

[[Group ID]{lang="EN-US"}]{#struct_0_x1857_11373_1124338362}

[[隔离组编号]{style="font-family:宋体"}]{#struct_0_x1857_11373_1808390361}

[[Group members]{lang="EN-US"}]{#struct_0_x1857_11373_x963501045}

[[隔离组中包含的成员端口，若显示为]{style="font-family:宋体"}[No ports]{lang="EN-US"}]{#struct_0_x1857_11373_x1346807438}[表示没有成员端口]{style="font-family:宋体"}

 

[[Community VLAN ID]{lang="EN-US"}]{#struct_0_x1857_11373_x964643517}

[[非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1857_11373_2121957206}[的编号（]{style="font-family:宋体"}[default]{lang="EN-US"}[表示缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[），若显示为]{style="font-family:宋体"}[None]{lang="EN-US"}[表示不存在非隔离]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1857_11373_1679733115}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-isolate enable]{lang="EN-US"}**]{#struct_0_x1857_11373_2061609279}

::::: {#1091911549 .myid}
[]{#_Toc404784055}[]{#_Toc381104188}[]{#struct_0_x1857_11373_2145982291}[]{#_Toc297622998}[]{#_Toc297378619}

**端口隔离 \-- 端口隔离配置命令 \-- port-isolate enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](端口隔离命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1857_11373_x1346741902}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1857_11373_1049788279}
:::

**[ ]{lang="EN-US"}**

[**[port-isolate enable]{lang="EN-US"}**]{#struct_0_x1857_11373_1797056596}[命令用来将当前端口加入到隔离组中。]{style="font-family:宋体"}

[**[undo port-isolate enable]{lang="EN-US"}**]{#struct_0_x1857_11373_x1986706981}[命令用来将当前端口从隔离组中删除。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1857_11373_594188986}

[[单隔离组设备：]{style="font-family:宋体"}]{#struct_0_x1857_11373_1535789787}

[**[port-isolate enable]{lang="EN-US"}**]{#struct_0_x1857_11373_2007254270}

[**[undo port-isolate enable]{lang="EN-US"}**]{#struct_0_x1857_11373_x1320490610}

[[多隔离组设备：]{style="font-family:宋体"}]{#struct_0_x1857_11373_1073222555}

[**[port-isolate enable ]{lang="EN-US"}[group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_x1857_11373_x1346610830}

[**[undo port-isolate enable]{lang="EN-US"}**]{#struct_0_x1857_11373_x1841179405}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x230506100}

[[当前端口未加入隔离组。]{style="font-family:宋体"}]{#struct_0_x1857_11373_1509292350}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1995949318}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1857_11373_x1124772070}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1918315031}

[[network-admin]{lang="EN-US"}]{#struct_0_x1857_11373_x1346545294}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1857_11373_1316930508}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x1857_11373_7537662}

[**[group]{lang="EN-US"}***[ group-number]{lang="EN-US"}*]{#struct_0_x1857_11373_1572990408}[：]{style="font-family:宋体"}[隔离组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1102695457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层以太网接口视图下的配置只对当前端口生效。]{style="font-family:宋体"}]{#struct_0_x1857_11373_x1932220588}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层聚合接口视图下的配置对当前接口及其成员端口生效，若某成员端口配置失败，系统会跳过该端口继续配置其他成员端口，若二层聚合接口配置失败，则不会再配置成员端口。]{style="font-family:宋体"}]{#struct_0_x1857_11373_x1651019679}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一端口不能同时配置为业务环回组成员端口和隔离组端口，即业务环回组成员端口不能加入隔离组，而隔离组成员端口不能再配置为业务环回组的成员端口。]{style="font-family:宋体"}]{#struct_0_x1857_11373_1592349711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在端口上执行该命令，会将当前端口加入系统缺省的隔离组]{style="font-family:宋体"}]{#struct_0_x1857_11373_1965178715}[1]{lang="EN-US"}[中。（单隔离组设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在端口上执行该命令将当前端口加入到指定的隔离组中前，必须先完成该隔离组的创建。（多隔离组设备）]{style="font-family:宋体"}]{#struct_0_x1857_11373_x1346479758}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个端口最多只能加入一个隔离组。（多隔离组设备）]{style="font-family:宋体"}]{#struct_0_x1857_11373_x270112306}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1408963790}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_x876901218}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[加入隔离组。（单隔离组设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1857_11373_x1135702454}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-isolate enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] port-isolate enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_x2019502937}[将二层聚合接口]{style="font-family:宋体"}[1]{lang="EN-US"}[以及其对应的成员端口加入隔离组。（单隔离组设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1857_11373_x1346414222}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port link-aggregation group 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] port link-aggregation group 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] quit]{lang="EN-US"}

[\[Sysname\] interface bridge-aggregation 1]{lang="EN-US"}

[\[Sysname-Bridge-Aggregation1\] port-isolate enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_750775219}[将端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[、]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[加入隔离组]{style="font-family:宋体"}[2]{lang="EN-US"}[。（多隔离组设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1857_11373_1343496287}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] port-isolate enable group 2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] port-isolate enable group 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x8616008}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display port-isolate group]{lang="EN-US"}**]{#struct_0_x1857_11373_1769947785}
:::::

::::: {#-1327117290 .myid}
[]{#_Toc404784056}[]{#_Toc381104189}[]{#struct_0_x1857_11373_x651984151}[]{#_Toc304821572}[]{#_Toc291763350}[]{#_Toc257705773}[]{#_Toc136860697}[]{#_Toc136071398}[]{#_Toc129677286}

**端口隔离 \-- 端口隔离配置命令 \-- port-isolate group**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](端口隔离命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1857_11373_x1346348686}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令仅多隔离组设备支持。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1857_11373_x62673658}
:::

[ ]{lang="EN-US"}

[**[port-isolate group]{lang="EN-US"}**]{#struct_0_x1857_11373_1491212364}[命令用来创建隔离组。]{style="font-family:宋体"}

[**[undo port-isolate group]{lang="EN-US"}**]{#struct_0_x1857_11373_690384827}[命令用来删除指定隔离组及其配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1857_11373_760392772}

[**[port-isolate group ]{lang="EN-US"}***[group-number]{lang="EN-US"}*]{#struct_0_x1857_11373_2014669083}

[**[undo port-isolate group ]{lang="EN-US"}**[{]{lang="EN-US"}**[ ]{lang="EN-US"}***[group-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **all** }]{lang="EN-US"}]{#struct_0_x1857_11373_x1091491557}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x331364967}

[[未创建任何隔离组。]{style="font-family:宋体"}]{#struct_0_x1857_11373_x986443828}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1857_11373_x1167536047}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1857_11373_x1347331726}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1857_11373_1232969827}

[[network-admin]{lang="EN-US"}]{#struct_0_x1857_11373_989414447}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1857_11373_x1161410299}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1857_11373_647517052}

[*[group-number]{lang="EN-US"}*]{#struct_0_x1857_11373_x625010913}[：隔离组编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1857_11373_488439924}[：删除]{style="font-family:宋体"}[所有隔离组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1857_11373_757740047}

[[\# ]{lang="EN-US"}]{#struct_0_x1857_11373_235805335}[创建隔离组]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1857_11373_x1347266190}

[\[Sysname\] port-isolate group 2]{lang="EN-US"}

[ ]{lang="EN-US"}
:::::
