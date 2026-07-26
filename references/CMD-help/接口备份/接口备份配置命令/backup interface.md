::: {#173683427 .myid}
[]{#_Toc404795353}[]{#struct_0_x8691_28676_x285524990}[]{#_Toc347416613}

**接口备份 \-- 接口备份配置命令 \-- backup interface**

------------------------------------------------------------------------

[**[backup interface]{lang="EN-US"}**]{#struct_0_x8691_28676_1647515456}[命令用来配置主接口的备份接口。]{style="font-family:宋体"}

[**[undo backup interface]{lang="EN-US"}**]{#struct_0_x8691_28676_x314776228}[命令用来删除备份接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1719450616}

[**[backup interface]{lang="EN-US"}**[ *interface-type interface-number* \[ *priority* \]]{lang="EN-US"}]{#struct_0_x8691_28676_1910310049}

[**[undo backup interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x8691_28676_1046676804}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1044805646}

[[没有为主接口配置备份接口。]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1736657565}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x602027201}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x8691_28676_x722579890}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8691_28676_340531890}

[[network-admin]{lang="EN-US"}]{#struct_0_x8691_28676_1757959275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8691_28676_x1625009109}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x167464668}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x8691_28676_1158869942}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[*[priority]{lang="EN-US"}*]{#struct_0_x8691_28676_x1418308534}[：指定备份接口的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。该数值越大表示优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1662357226}

[[通过为主接口配置备份接口，建立接口间的主备关系，命令所在视图的接口被指定为主接口，默认为主备方式备份，配置负载分担门限后可开启负载分担方式备份。]{style="font-family:宋体"}]{#struct_0_x8691_28676_758547497}

[[备份接口优先级仅在在用接口链路]{style="font-family:宋体"}[UP/DOWN]{lang="EN-US"}]{#struct_0_x8691_28676_1298345838}[（主备方式）和检测到流量变化（负载分担方式）时作为选取开启和关闭备份接口顺序的参考。备份接口被启用并]{style="font-family:宋体"}[up]{lang="EN-US"}[时，即使存在更高优先级的备份接口，都不再调整启用的备份接口。例如，备份接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[、]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[、]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[的优先级依此递减，当主接口]{style="font-family:宋体"}[down]{lang="EN-US"}[时先选取]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，若]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[能够]{style="font-family:宋体"}[up]{lang="EN-US"}[，则]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[成为在用备份接口，否则继续选取]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[，直至所有备份接口都被选取；若备份接口全部被选取，]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[首先]{style="font-family:宋体"}[up]{lang="EN-US"}[，则]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[成为在用备份接口，]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[将被关闭，此时即使]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[已经可以]{style="font-family:宋体"}[up]{lang="EN-US"}[或配置了更高优先级的备份接口，都不再调整启用的备份接口；若]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[作为在用备份接口]{style="font-family:宋体"}[down]{lang="EN-US"}[时，则按照优先级首先选取]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，若]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[不能]{style="font-family:宋体"}[up]{lang="EN-US"}[，继续选取]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[。备份接口的优先级相同时，先配置的备份接口将先启用。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x8691_28676_1394390692}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主备接口不可以嵌套配置，即一个主接口不能作为另外一个接口的备份接口。]{style="font-family:宋体"}]{#struct_0_x8691_28676_x438544183}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个备份接口只能为]{style="font-family:宋体"}]{#struct_0_x8691_28676_1613631504}[1]{lang="EN-US"}[个主接口提供备份。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一台设备上最多允许同时存在]{style="font-family:宋体"}]{#struct_0_x8691_28676_1376751687}[10]{lang="EN-US"}[个主接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个主接口最多允许有]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1217150973}[3]{lang="EN-US"}[个备份接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[子接口不能和其所对应的主接口建立备份关系。]{style="font-family:宋体"}]{#struct_0_x8691_28676_1858673173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[备份接口和主接口不能是逻辑链路成员接口，如三层聚合接口的成员接口。]{style="font-family:宋体"}]{#struct_0_x8691_28676_533120759}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[backup track]{lang="EN-US"}**]{#struct_0_x8691_28676_x1795512689}[命令互斥。也就是说，当在主接口上配置了]{lang="EN-US" style="font-family:宋体"}**[backup interface]{lang="EN-US"}**[后，在该主接口及其备份接口上都不能配置]{lang="EN-US" style="font-family:宋体"}**[backup track]{lang="EN-US"}**[；反之，当在某接口上配置了]{lang="EN-US" style="font-family:宋体"}**[backup track]{lang="EN-US"}**[后，也不能将该接口再配置为]{lang="EN-US" style="font-family:宋体"}**[backup interface]{lang="EN-US"}**[的主接口或备份接口。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8691_28676_543021189}

[[\# ]{lang="EN-US"}]{#struct_0_x8691_28676_1757893739}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的备份接口，其优先级为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8691_28676_x1928804806}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] backup interface gigabitethernet 1/0/2 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x358520128}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup track]{lang="EN-US"}**]{#struct_0_x8691_28676_x717360536}
:::

::: {#155518772 .myid}
[]{#_Toc404795354}[]{#struct_0_x8691_28676_x1415130536}[]{#_Toc347416614}

**接口备份 \-- 接口备份配置命令 \-- backup threshold**

------------------------------------------------------------------------

[**[backup threshold]{lang="EN-US"}**]{#struct_0_x8691_28676_446010956}[命令用来配置负载分担门限。]{style="font-family:宋体"}

[**[undo backup threshold]{lang="EN-US"}**]{#struct_0_x8691_28676_x2029384151}[命令用来取消负载分担门限的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_907307574}

[**[backup threshold ]{lang="EN-US"}***[upper-threshold lower-threshold]{lang="EN-US"}*]{#struct_0_x8691_28676_x1410224028}

[**[undo backup threshold]{lang="EN-US"}**]{#struct_0_x8691_28676_x553562115}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1556678962}

[[没有配置负载分担门限。]{style="font-family:宋体"}]{#struct_0_x8691_28676_1673972128}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x630317801}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1080064896}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x319360517}

[[network-admin]{lang="EN-US"}]{#struct_0_x8691_28676_x507391427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8691_28676_1757828203}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1112721632}

[*[upper-threshold]{lang="EN-US"}*]{#struct_0_x8691_28676_2004717612}[：指定负载分担门限的上限阈值，该参数表示数据流量占主接口带宽的百分比数值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[lower-threshold]{lang="EN-US"}*]{#struct_0_x8691_28676_x32738022}[：指定负载分担门限的下限阈值，该参数表示数据流量占主接口带宽的百分比数值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[，且必须小于]{style="font-family:宋体"}*[upper-threshold]{lang="EN-US"}*[的配置值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x8691_28676_4260089}

[[为主接口配置备份接口后，通过配置负载分担门限开启负载分担方式。负载分担门限表示数据流量占主接口带宽的百分比数值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x8691_28676_x13233361}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[，用于计算负载分担上下限阈值。]{style="font-family:宋体"}

[[当主接口上的数据流量超过了负载分担的上限阈值时，备份接口开始进行负载分担，若负载分担后主接口的流量又低于了下限阈值，备份接口将结束负载分担，导致备份接口不断地在]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x8691_28676_x1737758529}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态之间切换。为了避免这种情况的出现，配置时建议使下限阈值小于上限阈值的一半。]{style="font-family:宋体"}

[[主接口带宽可通过]{style="font-family:宋体"}**[bandwidth]{lang="EN-US"}**]{#struct_0_x8691_28676_x1415227698}[命令配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x8691_28676_x688041788}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置负载分担方式后，若主接口链路状态为]{style="font-family:宋体"}]{#struct_0_x8691_28676_1659476991}[DOWN]{lang="EN-US"}[，将仍按照主备方式备份。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup threshold]{lang="EN-US"}**]{#struct_0_x8691_28676_1959356659}[命令只能在主接口上执行，且必须在指定了备份接口之后执行。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1210881649}

[[\# ]{lang="EN-US"}]{#struct_0_x8691_28676_x807939384}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置负载分担门限的上限阈值为]{style="font-family:宋体"}[80]{lang="EN-US"}[，下限阈值为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8691_28676_1903758146}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] backup threshold 80 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1195063195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup interface]{lang="EN-US"}**]{#struct_0_x8691_28676_1757762667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup timer flow-check]{lang="EN-US"}**]{#struct_0_x8691_28676_1441553024}
:::

::: {#-1858949786 .myid}
[]{#_Toc404795355}[]{#struct_0_x8691_28676_x1186186381}[]{#_Toc347416615}

**接口备份 \-- 接口备份配置命令 \-- backup timer delay**

------------------------------------------------------------------------

[**[backup timer delay]{lang="EN-US"}**]{#struct_0_x8691_28676_1098406880}[命令用来配置接口状态切换延时。]{style="font-family:宋体"}

[**[undo backup timer delay]{lang="EN-US"}**]{#struct_0_x8691_28676_x1183628953}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1801254065}

[**[backup timer delay ]{lang="EN-US"}***[up-delay down-delay ]{lang="EN-US"}*]{#struct_0_x8691_28676_x1237322086}

[**[undo backup timer delay]{lang="EN-US"}**]{#struct_0_x8691_28676_x1582204668}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1727274778}

[[接口状态切换延时均为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x8691_28676_x1412472392}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1584487575}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x8691_28676_1814234524}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1369188399}

[[network-admin]{lang="EN-US"}]{#struct_0_x8691_28676_x15379176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8691_28676_623017487}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8691_28676_768156874}

[*[up-delay]{lang="EN-US"}*]{#struct_0_x8691_28676_x702826356}[：接口]{style="font-family:宋体"}[UP]{lang="EN-US"}[延时，即接口状态切换为]{style="font-family:宋体"}[UP]{lang="EN-US"}[前的延时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[down-delay]{lang="EN-US"}*]{#struct_0_x8691_28676_1757697131}[：接口]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[延时，即接口状态切换为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[前的延时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1188099216}

[[通常情况下，接口链路状态发生改变时，接口的状态切换应立即执行，但若接口链路状态不稳定则会引起接口状态的频繁切换，此现象可通过设置接口状态切换延迟时间来避免。若在用接口链路状态发生改变，系统将在该延迟时间后再做切换，若该延迟时间内在用接口链路状态恢复，则不进行切换。]{style="font-family:宋体"}]{#struct_0_x8691_28676_872498996}

[[需要注意的是，]{style="font-family:宋体"}**[backup timer delay]{lang="EN-US"}**]{#struct_0_x8691_28676_x1316591608}[命令只能在主接口上执行，且必须在指定了备份接口之后执行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8691_28676_700084205}

[[\# ]{lang="EN-US"}]{#struct_0_x8691_28676_x1720049095}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的备份接口，并设置接口状态切换延时均为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8691_28676_x1122045057}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] backup interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] backup timer delay 10 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x619043767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup interface]{lang="EN-US"}**]{#struct_0_x8691_28676_206992357}
:::

::: {#1233705394 .myid}
[]{#_Toc404795356}[]{#struct_0_x8691_28676_1573888972}[]{#_Toc347416616}

**接口备份 \-- 接口备份配置命令 \-- backup timer flow-check**

------------------------------------------------------------------------

[**[backup timer flow-check]{lang="EN-US"}**]{#struct_0_x8691_28676_515084077}[命令用来配置检测主接口和备份接口流量的时间间隔。]{style="font-family:宋体"}

[**[undo backup timer flow-check]{lang="EN-US"}**]{#struct_0_x8691_28676_1163924130}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x559143664}

[**[backup timer flow-check]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x8691_28676_1913885746}

[**[undo backup timer flow-check]{lang="EN-US"}**]{#struct_0_x8691_28676_x246193678}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x2050188245}

[[检测主接口和备份接口流量的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x8691_28676_1757631595}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x404508612}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x8691_28676_443061788}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x936336635}

[[network-admin]{lang="EN-US"}]{#struct_0_x8691_28676_1555953919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8691_28676_1850131991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1228165040}

[*[interval]{lang="EN-US"}*]{#struct_0_x8691_28676_x183067177}[：检测主接口和备份接口流量的时间间隔，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x8691_28676_104964564}

[[负载分担备份情况下周期性进行流量监测，根据流量信息进行备份接口启动或关闭的操作。通过本命令配置检测流量的时间间隔来设定检测的周期。]{style="font-family:宋体"}]{#struct_0_x8691_28676_1084483007}

[[需要注意的是，]{style="font-family:宋体"}**[backup timer flow-check]{lang="EN-US"}**]{#struct_0_x8691_28676_x201784749}[命令只能在主接口上执行，且必须在指定了备份接口之后执行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x316423187}

[[\# ]{lang="EN-US"}]{#struct_0_x8691_28676_x348359468}[在主接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置检测主接口和备份接口流量的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8691_28676_x2033964442}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] backup timer flow-check 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1964456714}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup interface]{lang="EN-US"}**]{#struct_0_x8691_28676_1757566059}
:::

::::: {#-193939939 .myid}
[]{#_Toc404795357}[]{#struct_0_x8691_28676_1930062022}[]{#_Toc347416617}

**接口备份 \-- 接口备份配置命令 \-- backup track**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](接口备份命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x8691_28676_1920466515}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x8691_28676_x134919643}
:::

[ ]{lang="EN-US"}

[**[backup track]{lang="EN-US"}**]{#struct_0_x8691_28676_x1194650831}[命令用来配置接口与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联。]{style="font-family:宋体"}

[**[undo backup track]{lang="EN-US"}**]{#struct_0_x8691_28676_x1501859508}[命令用来取消接口与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1216649275}

[**[backup track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_x8691_28676_357165934}

[**[undo backup track]{lang="EN-US"}**]{#struct_0_x8691_28676_x542829737}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x586339513}

[[接口没有与]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x8691_28676_x799337366}[项关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1327471224}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1543133191}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x588489106}

[[network-admin]{lang="EN-US"}]{#struct_0_x8691_28676_x987687764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8691_28676_10396415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1758549099}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_x8691_28676_x1423420239}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x8691_28676_608164839}

[[通过配置接口与]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x8691_28676_468431848}[项关联，使该接口作为备份接口，通过]{style="font-family:宋体"}[Track]{lang="EN-US"}[项来监测主链路的状态，从而可以根据网络环境的变化来改变备份接口的状态。当]{style="font-family:宋体"}[Track]{lang="EN-US"}[项为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[状态时，备份接口被启用，当]{style="font-family:宋体"}[Track]{lang="EN-US"}[项为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[状态时，备份接口被停用。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1771389569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令与]{lang="EN-US" style="font-family:宋体"}**[backup interface]{lang="EN-US"}**]{#struct_0_x8691_28676_x1091029046}[命令互斥。也就是说，当在主接口上配置了]{lang="EN-US" style="font-family:
宋体"}**[backup interface]{lang="EN-US"}**[后，在该主接口及其备份接口上都不能配置]{lang="EN-US" style="font-family:宋体"}**[backup track]{lang="EN-US"}**[；反之，当在某接口上配置了]{lang="EN-US" style="font-family:宋体"}**[backup track]{lang="EN-US"}**[后，也不能将该接口再配置为]{lang="EN-US" style="font-family:宋体"}**[backup interface]{lang="EN-US"}**[的主接口或备份接口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口只能关联一个]{style="font-family:宋体"}]{#struct_0_x8691_28676_x768116912}[Track]{lang="EN-US"}[项。如果在同一接口上多次执行本命令，则新的配置将覆盖旧的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上所关联的]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1869030303}[Track]{lang="EN-US"}[项可以是尚未创建的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。但是，只有当该]{style="font-family:宋体"}[Track]{lang="EN-US"}[项创建后，联动功能才开始生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x8691_28676_1478285338}[Track]{lang="EN-US"}[联动方式配置的备份接口的数量建议不要超过]{style="font-family:宋体"}[64]{lang="EN-US"}[个，否则可能影响设备的正常运行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1738566889}

[[\# ]{lang="EN-US"}]{#struct_0_x8691_28676_x195373231}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[关联。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x8691_28676_902416374}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] backup track 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_2009378718}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup interface]{lang="EN-US"}**]{#struct_0_x8691_28676_x739263587}
:::::

::: {#809992646 .myid}
[]{#_Toc404795358}[]{#struct_0_x8691_28676_1629574787}[]{#_Toc347416612}

**接口备份 \-- 接口备份配置命令 \-- display interface-backup state**

------------------------------------------------------------------------

[**[display interface-backup state]{lang="EN-US"}**]{#struct_0_x8691_28676_188702936}[命令用来查看主接口与备份接口的状态。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1758483563}

[**[display interface-backup state]{lang="EN-US"}**]{#struct_0_x8691_28676_x1342912839}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8691_28676_329450556}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x8691_28676_2107485791}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1911267603}

[[network-admin]{lang="EN-US"}]{#struct_0_x8691_28676_762707892}

[[network-operator]{lang="EN-US"}]{#struct_0_x8691_28676_x109723857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8691_28676_234912999}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x8691_28676_x1303818130}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1276914615}

[[\# ]{lang="EN-US"}]{#struct_0_x8691_28676_986230452}[查看主接口与备份接口的状态。]{style="font-family:宋体"}

[[\<Sysname\> display interface-backup state]{lang="EN-US"}]{#struct_0_x8691_28676_1758024810}

[Interface: GE1/0/1]{lang="EN-US"}

[  UpDelay: 10 s]{lang="EN-US"}

[  DownDelay: 5 s]{lang="EN-US"}

[  State: UP]{lang="EN-US"}

[  Backup interfaces:]{lang="EN-US"}

[    GE1/0/2             Priority: 30   State: STANDBY]{lang="EN-US"}

[    GE1/0/3             Priority: 20   State: STANDBY]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GE1/0/5]{lang="EN-US"}

[  UpDelay: 10 s]{lang="EN-US"}

[  DownDelay: 5 s]{lang="EN-US"}

[  Upper threshold: 80]{lang="EN-US"}

[  Lower threshold: 20]{lang="EN-US"}

[State: DOWN]{lang="EN-US"}

[  Backup interfaces:]{lang="EN-US"}

[    GE1/0/6             Priority: 30   State: UP_DELAY]{lang="EN-US"}

[    GE1/0/7             Priority: 20   State: STANDBY]{lang="EN-US"}

[ ]{lang="EN-US"}

[IB Track Information:]{lang="EN-US"}

[  GE1/0/4              Track: 1  State: STANDBY]{lang="EN-US"}

[  GE1/0/8              Track: 2  State: UP]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface-backup state]{lang="EN-US"}]{#struct_0_x8691_28676_156717733}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_288953114}[[字段]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1091337238}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1824562773}

[[Interface]{lang="EN-US"}]{#struct_0_x8691_28676_x1926443163}

[[主接口名称]{style="font-family:宋体"}]{#struct_0_x8691_28676_1777417736}

[[UpDelay]{lang="EN-US"}]{#struct_0_x8691_28676_x1871479924}

[[接口延时]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_x8691_28676_x1758150263}[超时时间，单位为秒]{style="font-family:宋体"}

[[DownDelay]{lang="EN-US"}]{#struct_0_x8691_28676_1436832147}

[[接口延时]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x8691_28676_193854797}[超时时间，单位为秒]{style="font-family:宋体"}

[[Upper threshold]{lang="EN-US"}]{#struct_0_x8691_28676_2134095522}

[[负载分担门限的上限阈值]{style="font-family:宋体"}]{#struct_0_x8691_28676_1757959274}

[[Lower threshold]{lang="EN-US"}]{#struct_0_x8691_28676_x1624943573}

[[负载分担门限的下限阈值]{style="font-family:宋体"}]{#struct_0_x8691_28676_1394052307}

[[State]{lang="EN-US"}]{#struct_0_x8691_28676_x3313801}

[[主接口状态：]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1492122667}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x8691_28676_1757893738}[：]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x8691_28676_x1928739270}[：]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP_DELAY]{lang="EN-US"}]{#struct_0_x8691_28676_1111353259}[：延时]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN_DELAY]{lang="EN-US"}]{#struct_0_x8691_28676_2103814004}[：延时]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Backup interfaces]{lang="EN-US"}]{#struct_0_x8691_28676_x1678907187}

[[主接口关联的所有备份接口]{style="font-family:宋体"}]{#struct_0_x8691_28676_x804402376}

[[Priority]{lang="EN-US"}]{#struct_0_x8691_28676_1279199281}

[[备份接口优先级]{style="font-family:宋体"}]{#struct_0_x8691_28676_x767812755}

[[State]{lang="EN-US"}]{#struct_0_x8691_28676_1522862842}

[[备份接口状态：]{style="font-family:宋体"}]{#struct_0_x8691_28676_1757828202}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x8691_28676_1112656096}[：]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x8691_28676_1964174880}[：]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP_DELAY]{lang="EN-US"}]{#struct_0_x8691_28676_224863761}[：延时]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN_DELAY]{lang="EN-US"}]{#struct_0_x8691_28676_x1754599279}[：延时]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STANDBY]{lang="EN-US"}]{#struct_0_x8691_28676_649936973}[：备用状态]{style="font-family:宋体"}

[[IB Track Information]{lang="EN-US"}]{#struct_0_x8691_28676_x592240365}

[[与]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x8691_28676_1520248188}[项关联的备份接口信息]{style="font-family:宋体"}

[[GE1/0/4]{lang="EN-US"}]{#struct_0_x8691_28676_1757762666}

[[备份接口]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1186251917}

[[Track]{lang="EN-US"}]{#struct_0_x8691_28676_1758735663}

[[备份接口关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x8691_28676_x959849054}[项]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x8691_28676_285483845}

[[关联了]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x8691_28676_x1948205979}[项的备份接口状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[INVALID]{lang="PT-BR"}]{#struct_0_x8691_28676_270923300}[：]{style="font-family:宋体"}[接口角色未生效（比如]{style="font-family:宋体"}[Track]{lang="EN-US"}[项未创建）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x8691_28676_1757697130}[：]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x8691_28676_1188164752}[：]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STANDBY]{lang="EN-US"}]{#struct_0_x8691_28676_x1876473404}[：备用状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#319109158 .myid}
[]{#_Toc404795359}[]{#struct_0_x8691_28676_x419118503}[]{#_Toc347416611}

**接口备份 \-- 接口备份配置命令 \-- display interface-backup statistics**

------------------------------------------------------------------------

[**[display interface-backup statistics]{lang="EN-US"}**]{#struct_0_x8691_28676_x90474766}[命令用来查看参与负载分担的接口的流量统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8691_28676_249319252}

[**[display interface-backup statistics]{lang="EN-US"}**]{#struct_0_x8691_28676_1323983507}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8691_28676_x2122608502}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x8691_28676_x82068143}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1652323890}

[[network-admin]{lang="EN-US"}]{#struct_0_x8691_28676_x1088305319}

[[network-operator]{lang="EN-US"}]{#struct_0_x8691_28676_943181653}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8691_28676_1002588790}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x8691_28676_2017577000}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8691_28676_1757631594}

[]{#_Toc320517845}[[\# ]{lang="EN-US"}]{#struct_0_x8691_28676_x404443076}[查看参与负载分担的接口的流量统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface-backup statistics]{lang="EN-US"}]{#struct_0_x8691_28676_1279491276}

[Interface: GigabitEthernet1/0/2 ]{lang="EN-US"}

[  Statistics interval: 30 s]{lang="EN-US"}

[  Bandwidth: 100000000 bps]{lang="EN-US"}

[  PrimaryTotalIn: 102 bytes]{lang="EN-US"}

[  PrimaryTotalOut: 108 bytes]{lang="EN-US"}

[  PrimaryIntervalIn: 102 bytes]{lang="EN-US"}

[  PrimaryIntervalOut: 108 bytes]{lang="EN-US"}

[  Primary used bandwidth: 28 bps]{lang="EN-US"}

[  TotalIn: 102 bytes]{lang="EN-US"}

[  TotalOut: 108 bytes]{lang="EN-US"}

[  TotalIntervalIn: 102 bytes]{lang="EN-US"}

[  TotalIntervalOut: 108 bytes]{lang="EN-US"}

[  Total used bandwidth: 28 bps]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display interface-backup statistics]{lang="EN-US"}]{#struct_0_x8691_28676_x411516955}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_317905274}[[字段]{style="font-family:黑体"}]{#struct_0_x8691_28676_x1449870407}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x8691_28676_x531478882}

[[Interface]{lang="EN-US"}]{#struct_0_x8691_28676_x401701006}

[[主接口名称]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1613404640}

[[Statistics interval]{lang="EN-US"}]{#struct_0_x8691_28676_x1932277158}

[[检测主接口和备份接口流量的时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_x8691_28676_x762945130}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x8691_28676_1757566058}

[[主接口带宽，单位为比特每秒]{style="font-family:宋体"}]{#struct_0_x8691_28676_1929996486}

[[PrimaryTotalIn]{lang="EN-US"}]{#struct_0_x8691_28676_x264418933}

[[上一次检测时主接口累计的接收字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_x548635539}

[[PrimaryTotalOut]{lang="EN-US"}]{#struct_0_x8691_28676_1771746237}

[[上一次检测时主接口累计的发送字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_x374869948}

[[PrimaryIntervalIn]{lang="EN-US"}]{#struct_0_x8691_28676_2117527948}

[[上一个时间间隔内主接口的接收字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_x235508378}

[[PrimaryIntervalOut]{lang="EN-US"}]{#struct_0_x8691_28676_52397903}

[[上一个时间间隔内主接口的发送字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_298058977}

[[Primary used bandwidth]{lang="EN-US"}]{#struct_0_x8691_28676_1584216792}

[[上一个时间间隔内主接口参与负载分担的实际带宽，单位为比特每秒]{style="font-family:宋体"}]{#struct_0_x8691_28676_1758549098}

[[TotalIn]{lang="EN-US"}]{#struct_0_x8691_28676_x1423485775}

[[上一次检测时主接口与在用备份接口累计的接收总字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_1547113326}

[[TotalOut]{lang="EN-US"}]{#struct_0_x8691_28676_x1179398371}

[[上一次检测时主接口与在用备份接口累计的发送总字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1800605851}

[[TotalIntervalIn]{lang="EN-US"}]{#struct_0_x8691_28676_x47470668}

[[上一个时间间隔内主接口与在用备份接口的接收总字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_x265765300}

[[TotalIntervalOut]{lang="EN-US"}]{#struct_0_x8691_28676_x1416730514}

[[上一个时间间隔内主接口与在用备份接口的发送总字节数，单位为字节]{style="font-family:宋体"}]{#struct_0_x8691_28676_x721244811}

[[Total used bandwidth]{lang="EN-US"}]{#struct_0_x8691_28676_1758483562}

[[上一个时间间隔内主接口与在用备份接口的实际总带宽，单位为比特每秒]{style="font-family:宋体"}]{#struct_0_x8691_28676_x1342978375}

[ ]{lang="EN-US"}
