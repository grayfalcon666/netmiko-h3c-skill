::: {#-372356765 .myid}
[]{#_Toc404795729}[]{#struct_0_20339_21110_859742340}[]{#_Toc345072392}[]{#_Toc345072221}[]{#_Toc257636534}[]{#_Toc124742942}[]{#_Toc101584094}

**RRPP \-- RRPP配置命令 \-- control-vlan**

------------------------------------------------------------------------

[**[control-vlan]{lang="EN-US"}**]{#struct_0_20339_21110_x250342400}[命令用来配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的主控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **control-vlan**]{lang="EN-US"}]{#struct_0_20339_21110_x1885009678}[命令用来删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的主控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x275023802}

[**[control-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_20339_21110_x2002880970}

[**[undo]{lang="EN-US"}**[ **control-vlan**]{lang="EN-US"}]{#struct_0_20339_21110_x1460216384}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_1574514910}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1214576946}[域不存在任何控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1250226061}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x430398063}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_527795984}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x209254011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_2111068800}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_155295100}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_20339_21110_1535815502}[：主控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1039217397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户只需配置主控制]{style="font-family:宋体"}]{#struct_0_20339_21110_1787397803}[VLAN]{lang="EN-US"}[，子控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[由系统自动分配，其]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为主控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[＋]{style="font-family:宋体"}[1]{lang="EN-US"}[。因此，在配置控制]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[时请选取两个连续的、尚未创建的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，否则将导致配置失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请勿将接入]{style="font-family:宋体"}]{#struct_0_20339_21110_x200026779}[RRPP]{lang="EN-US"}[环的端口的缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[配置为控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，而且控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内不能运行]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射功能，否则]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议报文将无法正常收发。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置好]{style="font-family:宋体"}]{#struct_0_20339_21110_1669978545}[RRPP]{lang="EN-US"}[环之后不再允许用户删除或修改]{style="font-family:宋体"}[主]{lang="EN-US" style="font-family:
宋体"}[控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}[主控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[只能通过]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **control-vlan**]{lang="EN-US"}[命令删除，]{style="font-family:宋体"}[不能]{lang="EN-US" style="font-family:宋体"}[通过]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **vlan**]{lang="EN-US"}[命令删除。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_1210953168}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_x947411409}[假设]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN 101]{lang="EN-US"}[都是尚未创建的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，配置]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的主控制]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_x1565358615}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] control-vlan 100]{lang="EN-US"}
:::

::: {#1685901343 .myid}
[]{#_Toc404795730}[]{#struct_0_20339_21110_x1846158816}[]{#_Toc345072393}[]{#_Toc345072222}[]{#_Toc257636535}[]{#_Toc124742944}[]{#_Toc101584096}[]{#_Toc350937938}[]{#_display_rrpp_brief}

**RRPP \-- RRPP配置命令 \-- display rrpp brief**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rrpp** **brief**]{lang="EN-US"}]{#struct_0_20339_21110_24278146}[命令用来显示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1170886990}

[**[display]{lang="EN-US"}**]{#struct_0_20339_21110_x312807512}[ **rrpp** **brief**]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_681789371}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20339_21110_544984859}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1951738311}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1537290281}

[[network-operator]{lang="EN-US"}]{#struct_0_20339_21110_602413921}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1889718420}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20339_21110_1508048599}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1995847494}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_x2104458061}[显示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[的]{style="font-family:宋体"}[摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rrpp brief]{lang="EN-US"}]{#struct_0_20339_21110_x1021099082}

[ Flags for node mode: M --- Master, T \-- Transit, E \-- Edge, A \-- Assistant-edge]{lang="EN-US"}

[ ]{lang="EN-US"}

[ RRPP protocol status: Enabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Domain ID     : 1]{lang="EN-US"}

[ Control VLAN  : Primary 5, Secondary 6]{lang="EN-US"}

[ Protected VLAN: Reference instance 0 to 2, 4]{lang="EN-US"}

[ ]{lang="EN-US"}[Hello timer   : 1 ]{lang="NO-BOK"}[seconds, ]{lang="EN-US"}[Fail timer]{lang="NO-BOK"}[: 3 seconds]{lang="EN-US"}

[ ]{lang="EN-US"}[Fast detection status: Disabled]{lang="NO-BOK"}

[ Fast-Hello timer: 20 ms, Fast-Fail timer: 60 ms]{lang="NO-BOK"}

[ Fast-Edge-Hello timer: 10 ms, Fast-Edge-Fail timer: 30 ms]{lang="NO-BOK"}

[  ]{lang="NO-BOK"}[Ring  Ring   Node  Primary/Common            Secondary/Edge            Enable]{lang="EN-US"}

[  ID    level  mode  port                      port                      status]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  1     1      M     GE1/0/1                   GE1/0/2                   Yes]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Domain ID     : 2]{lang="EN-US"}

[ Control VLAN  : Primary 10, Secondary 11]{lang="EN-US"}

[ Protected VLAN: Reference instance 0 to 2, 4]{lang="EN-US"}

[ Hello timer   : 1 seconds, Fail timer: 3 seconds]{lang="EN-US"}

[ ]{lang="EN-US"}[Fast detection status: Disabled]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}[Fast-Hello timer: 10 ms, Fast-Fail timer: 30 ms]{lang="NO-BOK"}

[  ]{lang="NO-BOK"}[Ring  Ring   Node  Primary/Common            Secondary/Edge            Enable]{lang="EN-US"}

[  ID    level  mode  port                      port                      status]{lang="EN-US"}

[ ]{lang="EN-US"}[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="DE"}[\-\-\-\--]{lang="EN-US"}

[  ]{lang="DE"}[1     0      T     GE1/0/3                   GE1/0/4                   Yes]{lang="EN-US"}

[  2     1      E     GE1/0/3                   GE1/0/5                   Yes]{lang="EN-US"}

[                     GE1/0/4]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display rrpp brief]{lang="EN-US"}]{#struct_0_20339_21110_1219109741}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2109696830}[[字段]{style="font-family:黑体"}]{#struct_0_20339_21110_2002466119}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20339_21110_x1083703004}

[[Flags for node mode]{lang="EN-US"}]{#struct_0_20339_21110_713870278}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x275848194}[的节点角色：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}]{#struct_0_20339_21110_x1615438286}[：代表主节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_20339_21110_1836993955}[：代表传输节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_20339_21110_1041664148}[：代表边缘节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_20339_21110_x707825372}[：代表辅助边缘节点]{style="font-family:宋体"}

[[RRPP protocol status]{lang="EN-US"}]{#struct_0_20339_21110_x1562035989}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1707784273}[协议的全局使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_20339_21110_x1930299923}[d]{lang="EN-US"}[：表示全局使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_20339_21110_778054385}[d]{lang="EN-US"}[：表示全局未使能]{lang="EN-US" style="font-family:宋体"}

[[Domain ID]{lang="EN-US"}]{#struct_0_20339_21110_1395714248}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1608045892}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Control VLAN]{lang="EN-US"}]{#struct_0_20339_21110_407372279}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_162335126}[域的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_20339_21110_x2144950113}[：表示主控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[econdary]{lang="EN-US"}]{#struct_0_20339_21110_1101748857}[：表示子控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Protected VLAN]{lang="EN-US"}]{#struct_0_20339_21110_x214530028}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1153094268}[域的保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所对应的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[（]{style="font-family:宋体"}[Multiple Spanning Tree Instance]{lang="EN-US"}[，多生成树实例）。]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的映射关系可通过命令]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **stp** **region-configuration**]{lang="EN-US"}[（请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[生成树"）查看]{style="font-family:宋体"}

[[Hello timer]{lang="EN-US"}]{#struct_0_20339_21110_x1695198549}

[[Hello]{lang="EN-US"}]{#struct_0_20339_21110_x1905732879}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Fail timer]{lang="EN-US"}]{#struct_0_20339_21110_1404947867}

[[Fail]{lang="EN-US"}]{#struct_0_20339_21110_2075689110}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Fast detection status]{lang="EN-US"}]{#struct_0_20339_21110_85004118}

[[快速检测功能的使能状态：]{style="font-family:宋体"}]{#struct_0_20339_21110_236554637}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_20339_21110_1112212241}[d]{lang="EN-US"}[：表示使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_20339_21110_x1780613969}[d]{lang="EN-US"}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Fast-Hello timer]{lang="EN-US"}]{#struct_0_20339_21110_852809653}

[[Fast-Hello]{lang="EN-US"}]{#struct_0_20339_21110_466969651}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Fast-Fail timer]{lang="EN-US"}]{#struct_0_20339_21110_731577135}

[[Fast-Fail]{lang="EN-US"}]{#struct_0_20339_21110_1334343228}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Fast-Edge-Hello]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[timer]{lang="EN-US"}]{#struct_0_20339_21110_948269386}

[[Fast]{lang="EN-US"}]{#struct_0_20339_21110_2009538615}[-Edge-]{lang="NO-BOK"}[Hello]{lang="EN-US"}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Fast-Edge]{lang="NO-BOK"}[-Fail timer]{lang="EN-US"}]{#struct_0_20339_21110_1607842915}

[[Fast]{lang="EN-US"}]{#struct_0_20339_21110_x1349568084}[-Edge-]{lang="NO-BOK"}[Fail]{lang="EN-US"}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Ring ID]{lang="EN-US"}]{#struct_0_20339_21110_x1519725593}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x617814555}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Ring level]{lang="EN-US"}]{#struct_0_20339_21110_1137681801}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_636985406}[环的级别：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_20339_21110_x1525544519}[：表示主环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_20339_21110_x1631404537}[：表示子环]{lang="EN-US" style="font-family:宋体"}

[[Node mode]{lang="EN-US"}]{#struct_0_20339_21110_x1827668136}

[[设备的节点角色]{style="font-family:宋体"}]{#struct_0_20339_21110_x173182541}

[[Primary/Common port]{lang="EN-US"}]{#struct_0_20339_21110_325118766}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当节点角色为主节点或传输节点时，该字段表示主端口]{style="font-family:宋体"}]{#struct_0_20339_21110_x1489966023}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当节点角色为边缘节点或辅助边缘节点时，该字段表示公共端口]{style="font-family:宋体"}]{#struct_0_20339_21110_901215219}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口时，该字段显示为"]{style="font-family:宋体"}]{#struct_0_20339_21110_x2102445599}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Secondary/Edge port]{lang="EN-US"}]{#struct_0_20339_21110_1968608822}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当节点角色为主节点或传输节点时，该字段表示副端口]{style="font-family:宋体"}]{#struct_0_20339_21110_1467657904}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当节点角色为边缘节点或辅助边缘节点时，该字段表示边缘端口]{style="font-family:宋体"}]{#struct_0_20339_21110_2111003264}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口时，该字段显示为"]{style="font-family:宋体"}]{#struct_0_20339_21110_2118621913}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Enable ]{lang="EN-US"}]{#struct_0_20339_21110_x1201175476}[status]{lang="FR"}

[[当前]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1209528347}[环的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_20339_21110_544919323}[：表示使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_20339_21110_x1574978025}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[]{#_Toc124742945}[]{#_Toc101584097}[]{#_Toc132456273}[]{#_Toc133208358}[]{#_Toc132456274}[]{#_Toc133208359}[]{#_display_rrpp_statistics}[ ]{lang="EN-US"}

::: {#-1783119632 .myid}
[]{#_Toc404795731}[]{#struct_0_20339_21110_669895239}[]{#_Toc345072394}[]{#_Toc345072223}[]{#_Toc257636536}[]{#_Toc173836540}

**RRPP \-- RRPP配置命令 \-- display rrpp ring-group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rrpp** **ring-group** ]{lang="EN-US"}]{#struct_0_20339_21110_792154769}[命令用来显示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1420141861}

[**[display]{lang="EN-US"}**[ **rrpp** **ring-group** \[ *ring-group-id* \]]{lang="EN-US"}]{#struct_0_20339_21110_94873694}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_498153571}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20339_21110_1122281880}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1021164618}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_468865752}

[[network-operator]{lang="EN-US"}]{#struct_0_20339_21110_x134627069}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_1209107718}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20339_21110_x1627553379}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_1072799637}

[*[ring-group-id]{lang="EN-US"}*]{#struct_0_20339_21110_987437878}[：显示指定]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组的配置信息，]{style="font-family:宋体"}*[ring-group-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，将显示所有]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组的配置信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_x995316126}

[[如果是边缘节点的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x550433028}[环组，还会显示当前发送]{style="font-family:宋体"}[Edge-Hello]{lang="EN-US"}[报文的环。]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#struct_0_20339_21110_100373689}[【举例】]{style="font-family:黑体"}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_1707718737}[显示所有]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display rrpp ring-group]{lang="EN-US"}]{#struct_0_20339_21110_1563150429}

[ Ring group 1:]{lang="EN-US"}

[  Domain 1 ring 1 to 3, 5]{lang="EN-US"}

[  Domain 2 ring 1 to 3, 5]{lang="EN-US"}

[  Domain 1 ring 1 is the sending ring]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Ring group 2:]{lang="EN-US"}

[  Domain 1 ring 4, 6 to 7]{lang="EN-US"}

[  Domain 2 ring 4, 6 to 7]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display rrpp ring-group]{lang="EN-US"}]{#struct_0_20339_21110_x69512274}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2104401312}[[字段]{style="font-family:黑体"}]{#struct_0_20339_21110_1850817639}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20339_21110_1921905613}

[[Ring group 1]{lang="EN-US"}]{#struct_0_20339_21110_262788329}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x474709058}[环组]{style="font-family:宋体"}[1]{lang="EN-US"}

[[Domain 1 ring 1 to 3, 5]{lang="EN-US"}]{#struct_0_20339_21110_x214595564}

[[该环组的子环成员有]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x462671791}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的环]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[和]{style="font-family:宋体"}[5]{lang="EN-US"}

[[Domain 1 ring 1 is the sending ring]{lang="EN-US"}]{#struct_0_20339_21110_x1017539032}

[[该环组的发送环为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_770352817}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的环]{style="font-family:宋体"}[1]{lang="EN-US"}

[]{#_Toc173833055}[ ]{lang="EN-US"}

::: {#1099784667 .myid}
[]{#_Toc404795732}[]{#struct_0_20339_21110_x2121552207}[]{#_Toc345072395}[]{#_Toc345072224}[]{#_Toc257636537}[]{#_Toc350937941}[]{#_Toc350937942}[]{#_Toc350937943}

**RRPP \-- RRPP配置命令 \-- display rrpp statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rrpp** **statistics**]{lang="EN-US"}]{#struct_0_20339_21110_x1373623199}[命令用来显示]{style="font-family:
宋体"}[RRPP]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x425516894}

[**[display]{lang="EN-US"}**]{#struct_0_20339_21110_1807357964}[ **rrpp** **statistics** **domain** *domain-id* \[ **ring** *ring-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_322732508}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20339_21110_1021300020}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1780679505}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x76551297}

[[network-operator]{lang="EN-US"}]{#struct_0_20339_21110_873597535}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1576343352}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20339_21110_1619931218}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_170954593}

[**[domain]{lang="EN-US"}**]{#struct_0_20339_21110_940403278}[ ]{lang="EN-US"}*[domain-id]{lang="EN-US"}*[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="FR"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ring]{lang="EN-US"}**]{#struct_0_20339_21110_1257527364}*[ ]{lang="EN-US"}[ring-id]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定环的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[ring-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}[将显示该]{style="font-family:宋体"}[域中]{style="font-family:宋体"}[所有环的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_1294726187}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某端口属于多个环，那么其报文将按环分别计数，用户看到的报文统计信息为该端口在当前环下的报文统计。]{style="font-family:宋体"}]{#struct_0_20339_21110_x1378532998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当环由未激活状态进入激活状态时，报文统计将重新开始计数。]{style="font-family:宋体"}]{#struct_0_20339_21110_855749869}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_472572676}

[[\# ]{lang="SV"}]{#struct_0_20339_21110_948203850}[显示]{style="font-family:宋体"}[RRPP]{lang="SV"}[域]{style="font-family:宋体"}[2]{lang="SV"}[中所有环]{style="font-family:
宋体"}[的]{style="font-family:宋体"}[RRPP]{lang="SV"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rrpp statistics domain 2]{lang="EN-US"}]{#struct_0_20339_21110_x617880091}

[ Ring ID       : 1]{lang="EN-US"}

[ Ring level    : 0]{lang="EN-US"}

[ Node mode     : Master]{lang="EN-US"}

[ Active status : Yes]{lang="EN-US"}

[ Primary port  : GE1/0/3]{lang="EN-US"}

[ Fast-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[ Fast-Edge-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[  Direct Hello     Link     Common     Complete   Edge      Major     Total]{lang="EN-US"}

[                   down     flush FDB  flush FDB  hello     fault]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Out    16924     0        0          1          0         0         16925]{lang="EN-US"}

[  In     0         0        0          0          0         0         0]{lang="EN-US"}

[ Secondary port: GE1/0/4]{lang="EN-US"}

[ Fast-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[ Fast-Edge-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[  Direct Hello     Link     Common     Complete   Edge      Major     Total]{lang="EN-US"}

[                   down     flush FDB  flush FDB  hello     fault]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Out    0         0        0          0          0         0         0]{lang="EN-US"}

[  In     16878     0        0          1          0         0         16879]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Ring ID       : 2]{lang="EN-US"}

[ Ring level    : 1]{lang="EN-US"}

[ Node mode     : Edge]{lang="EN-US"}

[ Active status : No]{lang="EN-US"}

[ Common port   : GE1/0/3]{lang="EN-US"}

[ Fast-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[ Fast-Edge-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[  Direct Hello     Link     Common     Complete   Edge      Major     Total]{lang="EN-US"}

[                   down     flush FDB  flush FDB  hello     fault]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Out    0         0        0          0          0         0         0]{lang="EN-US"}

[  In     0         0        0          0          0         0         0]{lang="EN-US"}

[ Common port   : GE1/0/4]{lang="EN-US"}

[ Fast-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[ Fast-Edge-Hello packets: 0 Sent, 0 Received]{lang="EN-US"}

[  Direct Hello     Link     Common     Complete   Edge      Major     Total]{lang="EN-US"}

[                   down     flush FDB  flush FDB  hello     fault]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Out    0         0        0          0          0         0         0]{lang="EN-US"}

[  In     0         0        0          0          0         0         0]{lang="EN-US"}

[ Edge port     : GE1/0/5]{lang="EN-US"}

[  Direct Hello     Link     Common     Complete   Edge      Major     Total]{lang="EN-US"}

[                   down     flush FDB  flush FDB  hello     fault]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}[\-\-\-\-\--]{lang="SV"}

[  Out    0         0        0          0          0         0         0]{lang="EN-US"}

[  In     0         0        0          0          0         0         0]{lang="EN-US"}

[]{#_Toc124742946}[]{#_Toc101584098}[]{#struct_0_20339_21110_1893978921}[]{#_display_rrpp_verbose}[表1-3 ]{lang="EN-US"}[display rrpp statistics]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2097603612}[[字段]{style="font-family:黑体"}]{#struct_0_20339_21110_x1827733672}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20339_21110_571856855}

[[Ring ID]{lang="EN-US"}]{#struct_0_20339_21110_x858941088}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x645235109}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Ring level]{lang="EN-US"}]{#struct_0_20339_21110_2142679770}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x316321523}[环的级别：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_20339_21110_1579376035}[：表示主环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_20339_21110_801960136}[：表示子环]{lang="EN-US" style="font-family:宋体"}

[[Node mode]{lang="EN-US"}]{#struct_0_20339_21110_901149683}

[[设备的节点角色：]{style="font-family:宋体"}]{#struct_0_20339_21110_1157696384}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="SV"}]{#struct_0_20339_21110_x366384843}[：主节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_20339_21110_x162466989}[：传输节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Edge]{lang="EN-US"}]{#struct_0_20339_21110_x1336484626}[：边缘节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Assistant-edge]{lang="EN-US"}]{#struct_0_20339_21110_1117088706}[：辅助边缘节点]{lang="EN-US" style="font-family:宋体"}

[[Active status]{lang="EN-US"}]{#struct_0_20339_21110_x1010521603}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x2049746304}[环的激活状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_20339_21110_1666486607}[：表示激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_20339_21110_x700641559}[：表示未激活]{lang="EN-US" style="font-family:宋体"}

[[Primary port]{lang="EN-US"}]{#struct_0_20339_21110_x1183619517}

[[主端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_887384006}["，下面也不会有相应的报文统计信息]{style="font-family:宋体"}

[[Secondary port]{lang="EN-US"}]{#struct_0_20339_21110_1453281178}

[[副端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_679137051}["，下面也不会有相应的报文统计信息]{style="font-family:宋体"}

[[Common port]{lang="EN-US"}]{#struct_0_20339_21110_337132165}

[[公共端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_1519302534}["，下面也不会有相应的报文统计信息]{style="font-family:宋体"}

[[Edge port]{lang="EN-US"}]{#struct_0_20339_21110_x1817699314}

[[边缘端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_x600380328}["，下面也不会有相应的报文统计信息]{style="font-family:宋体"}

[[Fast-Hello packets]{lang="EN-US"}]{#struct_0_20339_21110_958525726}

[[端口上]{style="font-family:宋体"}[Fast-Hello]{lang="EN-US"}]{#struct_0_20339_21110_x886946890}[报文的统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sent]{lang="EN-US"}]{#struct_0_20339_21110_x1360515442}[：表示发送报文的统计]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Received]{lang="EN-US"}]{#struct_0_20339_21110_1616720274}[：表示接收报文的统计]{style="font-family:宋体"}

[[Fast-Edge-Hello packets]{lang="EN-US"}]{#struct_0_20339_21110_1520043196}

[[端口上]{style="font-family:宋体"}[Fast-Edge-Hello]{lang="EN-US"}]{#struct_0_20339_21110_621121961}[报文的统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sent]{lang="EN-US"}]{#struct_0_20339_21110_1841936465}[：表示发送报文的统计]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Received]{lang="EN-US"}]{#struct_0_20339_21110_213616399}[：表示接收报文的统计]{style="font-family:宋体"}

[[Packet direct]{lang="EN-US"}]{#struct_0_20339_21110_305495259}

[[端口上报文的传播方向：]{style="font-family:宋体"}]{#struct_0_20339_21110_x1634651589}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Out]{lang="EN-US"}]{#struct_0_20339_21110_x80377836}[：表示发送]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In]{lang="EN-US"}]{#struct_0_20339_21110_x1370646949}[：表示接收]{lang="EN-US" style="font-family:宋体"}

[[Hello]{lang="EN-US"}]{#struct_0_20339_21110_1536309731}

[[端口收发的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20339_21110_1897350519}[报文统计信息]{style="font-family:宋体"}

[[Link down]{lang="EN-US"}]{#struct_0_20339_21110_x2004461359}

[[端口收发的]{style="font-family:宋体"}[Link-Down]{lang="EN-US"}]{#struct_0_20339_21110_x1646461777}[报文统计信息]{style="font-family:宋体"}

[[Common flush FDB]{lang="EN-US"}]{#struct_0_20339_21110_1976695809}

[[端口收发的]{style="font-family:宋体"}[Common-Flush-FDB]{lang="EN-US"}]{#struct_0_20339_21110_x913337706}[报文统计信息]{style="font-family:宋体"}

[[Complete flush FDB]{lang="EN-US"}]{#struct_0_20339_21110_x1419950377}

[[端口收发的]{style="font-family:宋体"}[Complete-Flush-FDB]{lang="EN-US"}]{#struct_0_20339_21110_1082421578}[报文统计信息]{style="font-family:宋体"}

[[Edge hello]{lang="EN-US"}]{#struct_0_20339_21110_x2015368314}

[[端口收发的]{style="font-family:宋体"}[Edge-Hello]{lang="EN-US"}]{#struct_0_20339_21110_x1745953795}[报文统计信息]{style="font-family:宋体"}

[[Major fault]{lang="EN-US"}]{#struct_0_20339_21110_x209138978}

[[端口收发的]{style="font-family:宋体"}[Major-Fault]{lang="EN-US"}]{#struct_0_20339_21110_x483662363}[报文统计信息]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_20339_21110_x1104323592}

[[端口收发的报文总数信息。这里只统计]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1276477553}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Link-Down]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Common-Flush-FDB]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Complete-Flush-FDB]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Edge-Hello]{lang="EN-US"}[报文和]{style="font-family:宋体"}[Major-Fault]{lang="EN-US"}[报文，其它种类的报文不统计]{style="font-family:宋体"}

[]{#_display_rrpp_verbose_1}[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_133856133}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **rrpp** **statistics**]{lang="EN-US"}]{#struct_0_20339_21110_753704924}

::: {#2037181451 .myid}
[]{#_Toc404795733}[]{#struct_0_20339_21110_x1181209643}[]{#_Toc345072396}[]{#_Toc345072225}[]{#_Toc257636538}

**RRPP \-- RRPP配置命令 \-- display rrpp verbose**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **rrpp** **verbose**]{lang="EN-US"}]{#struct_0_20339_21110_x932498934}[命令用来显示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1693515944}

[**[display]{lang="EN-US"}**[ **rrpp** **verbose** **domain** *domain-id* \[ **ring** *ring-id* \]]{lang="EN-US"}]{#struct_0_20339_21110_1875584684}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_921765592}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20339_21110_980910170}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_2146481774}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_1385999475}

[[network-operator]{lang="EN-US"}]{#struct_0_20339_21110_1796294161}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x436720804}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20339_21110_x539893066}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_578574255}

[**[domain]{lang="EN-US"}**[ *domain-id*]{lang="EN-US"}]{#struct_0_20339_21110_x58229279}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="FR"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ring]{lang="EN-US"}**[ *ring-id*]{lang="EN-US"}]{#struct_0_20339_21110_1035367411}[：]{style="font-family:宋体"}[显示指定环的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}*[ring-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}[将显示该域中所有环的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1344293010}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_1466897537}[显示]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[2]{lang="EN-US"}[中所有环的]{style="font-family:
宋体"}[RRPP]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display rrpp verbose domain 2]{lang="EN-US"}]{#struct_0_20339_21110_x2049811840}

[ Domain ID     : 2]{lang="EN-US"}

[ Control VLAN  : Primary 10, Secondary 11]{lang="EN-US"}

[ Protected VLAN: Reference instance 3, 5 to 7]{lang="EN-US"}

[ ]{lang="EN-US"}[Hello timer   : 1]{lang="NO-BOK"}[ seconds, ]{lang="EN-US"}[Fail timer: 3 ]{lang="NO-BOK"}[seconds]{lang="EN-US"}

[ ]{lang="NO-BOK"}[Fast detection status: Disabled]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}[Fast-Hello timer: 20 ms, Fast-Fail timer: 60 ms]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}[Fast-Edge-Hello timer: 10 ms, Fast-Edge-Fail timer: 30 ms]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}[Ring ID       : 1]{lang="EN-US"}

[ Ring level    : 0]{lang="EN-US"}

[ Node mode     : Master]{lang="EN-US"}

[ Ring state    : Completed]{lang="EN-US"}

[ Enable status : Yes, Active status: Yes]{lang="EN-US"}

[ Primary port  : GE1/0/4                    Port status: UP]{lang="EN-US"}

[ Secondary port: GE1/0/5                    Port status: BLOCKED]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Ring ID       : 2]{lang="EN-US"}

[ Ring level    : 1]{lang="EN-US"}

[ Node mode     : Edge]{lang="EN-US"}

[ Ring state    : -]{lang="EN-US"}

[ Enable status : No, Active status: No]{lang="EN-US"}

[ ]{lang="EN-US"}[Common port   : GE1/0/4                    Port status: -]{lang="FR"}

[                 GE1/0/5                    Port status: -]{lang="FR"}

[ ]{lang="FR"}[Edge port     : GE1/0/3                    Port status: -]{lang="FR"}

[[表1-4 ]{lang="EN-US"}[display rrpp verbose]{lang="EN-US"}]{#struct_0_20339_21110_x1557541445}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2130391540}[[字段]{style="font-family:黑体"}]{#struct_0_20339_21110_1495192161}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20339_21110_826109786}

[[Domain ID]{lang="EN-US"}]{#struct_0_20339_21110_x376463980}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x390105310}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Control VLAN]{lang="EN-US"}]{#struct_0_20339_21110_218268532}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1231860280}[域的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_20339_21110_679071515}[：主控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[econdary]{lang="EN-US"}]{#struct_0_20339_21110_309827566}[：子控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Protected VLAN]{lang="EN-US"}]{#struct_0_20339_21110_x1145066056}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1162644825}[域的保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所对应的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[。]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的映射关系可通过命令]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **stp** **region-configuration**]{lang="EN-US"}[（请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[生成树"）查看]{style="font-family:宋体"}

[[Hello timer]{lang="EN-US"}]{#struct_0_20339_21110_1661704412}

[[Hello]{lang="EN-US"}]{#struct_0_20339_21110_524428757}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Fail timer]{lang="EN-US"}]{#struct_0_20339_21110_1606085638}

[[Fail]{lang="EN-US"}]{#struct_0_20339_21110_1712089843}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Fast detection status]{lang="EN-US"}]{#struct_0_20339_21110_798766437}

[[快速检测功能的使能状态：]{style="font-family:宋体"}]{#struct_0_20339_21110_x809750737}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_20339_21110_x887012426}[d]{lang="EN-US"}[：表示使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_20339_21110_x2124653870}[d]{lang="EN-US"}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Fast-Hello timer]{lang="EN-US"}]{#struct_0_20339_21110_2033837543}

[[Fast-Hello]{lang="EN-US"}]{#struct_0_20339_21110_350857669}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Fast-Fail timer]{lang="EN-US"}]{#struct_0_20339_21110_384173305}

[[Fast-Fail]{lang="EN-US"}]{#struct_0_20339_21110_1841870929}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Fast-Edge-Hello timer]{lang="EN-US"}]{#struct_0_20339_21110_591348432}

[[Fast-Edge-Hello]{lang="EN-US"}]{#struct_0_20339_21110_1721026323}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Fast-Edge-Fail timer]{lang="EN-US"}]{#struct_0_20339_21110_489704107}

[[Fast-Edge-Fail]{lang="EN-US"}]{#struct_0_20339_21110_x1633825014}[定时器的值，单位为毫秒]{style="font-family:宋体"}

[[Ring ID]{lang="EN-US"}]{#struct_0_20339_21110_x80443372}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_478641353}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Ring level]{lang="EN-US"}]{#struct_0_20339_21110_x1751716264}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_695636927}[环的级别：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_20339_21110_x708626645}[：表示主环]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_20339_21110_x1646527313}[：表示子环]{lang="EN-US" style="font-family:宋体"}

[[Node mode]{lang="EN-US"}]{#struct_0_20339_21110_x37924987}

[[设备的节点角色：]{style="font-family:宋体"}]{#struct_0_20339_21110_194177123}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_20339_21110_x1227507693}[：主节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_20339_21110_x338341991}[：传输节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Edge]{lang="EN-US"}]{#struct_0_20339_21110_1082356042}[：边缘节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Assistant-edge]{lang="EN-US"}]{#struct_0_20339_21110_x866164537}[：辅助边缘节点]{lang="EN-US" style="font-family:宋体"}

[[Ring state]{lang="EN-US"}]{#struct_0_20339_21110_1029239596}

[[当前]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1333218700}[环的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Completed]{lang="EN-US"}]{#struct_0_20339_21110_x430982603}[：表示健康状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed]{lang="EN-US"}]{#struct_0_20339_21110_x483727899}[：表示断裂状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非主节点上，或当主节点上的环未使能时将显示为"]{style="font-family:宋体"}]{#struct_0_20339_21110_838574823}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Enable ]{lang="EN-US"}]{#struct_0_20339_21110_x1287525347}[status]{lang="FR"}

[[当前]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1241906068}[环的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_20339_21110_x1693581480}[：表示使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_20339_21110_2087029376}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Active status]{lang="EN-US"}]{#struct_0_20339_21110_x1051116869}

[[当前]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1824296549}[环的激活状态，可通过该字段状态了解]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议和当前]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的激活情况，必须同时使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议和当前]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环，该环才能处于激活状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_20339_21110_1035301875}[：表示激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_20339_21110_1832689826}[：表示未激活]{lang="EN-US" style="font-family:宋体"}

[[Primary port]{lang="EN-US"}]{#struct_0_20339_21110_1649820948}

[[主端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_x157334831}["]{style="font-family:宋体"}

[[Secondary port]{lang="EN-US"}]{#struct_0_20339_21110_773070783}

[[副端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_x2049877376}["]{style="font-family:宋体"}

[[Common port]{lang="EN-US"}]{#struct_0_20339_21110_1380817226}

[[公共端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_863884349}["]{style="font-family:宋体"}

[[Edge port]{lang="EN-US"}]{#struct_0_20339_21110_679005979}

[[边缘端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20339_21110_767304123}["]{style="font-family:宋体"}

[[Port status]{lang="FR"}]{#struct_0_20339_21110_1724360420}

[[端口状态，共有]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_20339_21110_x184798208}[种取值：]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[、]{style="font-family:宋体"}[UP]{lang="EN-US"}[和]{style="font-family:宋体"}[BLOCKED]{lang="EN-US"}[；如果环处于未激活状态、未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[]{#_Toc124742947}[]{#_Toc101584099}[]{#_reset_rrpp_statistics}[ ]{lang="EN-US"}

::: {#1202472518 .myid}
[]{#_Toc404795734}[]{#struct_0_20339_21110_1572839477}[]{#_Toc345072397}[]{#_Toc345072226}[]{#_Toc257636539}[]{#_Toc173836543}

**RRPP \-- RRPP配置命令 \-- domain ring**

------------------------------------------------------------------------

[**[domain]{lang="EN-US"}**[ **ring**]{lang="EN-US"}]{#struct_0_20339_21110_x887077962}[命令用来配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组内的子环。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **domain** **ring**]{lang="EN-US"}]{#struct_0_20339_21110_x1420647979}[命令用来删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组内的子环。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1029229411}

[**[domain]{lang="EN-US"}**[ *domain-id* **ring** *ring-id-list*]{lang="EN-US"}]{#struct_0_20339_21110_x621261420}

[**[undo]{lang="EN-US"}**]{#struct_0_20339_21110_1505195342}[ **domain**]{lang="EN-US"}[ *domain-id* \[ **ring** *ring-id-list* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_x939365675}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1801427762}[环组内不存在任何子环。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_1900511541}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x249915426}[环组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_569291744}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_820558648}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1756551588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_1841805393}

[*[domain-id]{lang="EN-US"}*]{#struct_0_20339_21110_x1383865084}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="FR"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ring]{lang="EN-US"}***[ ring-id-list]{lang="EN-US"}*]{#struct_0_20339_21110_612160289}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[子环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表。]{style="font-family:宋体"}*[ring-id-list]{lang="EN-US"}*[ = { *ring-id* \[ **to** *ring-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[ring-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[子环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。如果未指定本参数，将删除该域已加入环组的所有子环。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_x623247772}

[[进行下列操作时应按规定顺序进行，否则辅助边缘节点可能会因收不到]{style="font-family:宋体"}[Edge-Hello]{lang="EN-US"}]{#struct_0_20339_21110_x585659371}[报文而误认为主环故障：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将激活的环加入环组时，应先在辅助边缘节点将环加入环组，再在边缘节点将环加入环组。]{style="font-family:宋体"}]{#struct_0_20339_21110_x1043327759}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将激活的环从环组中删除时，应先在边缘节点将环从环组中删除，再在辅助边缘节点将环从环组中删除。]{style="font-family:宋体"}]{#struct_0_20339_21110_1913765504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将整个环组删除时，应先在边缘节点删除环组，再在辅助边缘节点删除环组。]{style="font-family:宋体"}]{#struct_0_20339_21110_114647701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将环组中的环激活时，应先激活边缘节点环组中的环，再激活辅助边缘节点环组中的环。]{style="font-family:宋体"}]{#struct_0_20339_21110_x1285686198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[将环组中的环解除激活时，应先解除激活辅助边缘节点环组中的环，再解除激活边缘节点环组中的环。]{style="font-family:宋体"}]{#struct_0_20339_21110_1502496811}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x80508908}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_80153065}[创建]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将子环]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[3]{lang="EN-US"}[和]{style="font-family:宋体"}[5]{lang="EN-US"}[都加入到域]{style="font-family:宋体"}[1]{lang="EN-US"}[和域]{style="font-family:宋体"}[2]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_1264443240}

[\[Sysname\] rrpp ring-group 1]{lang="EN-US"}

[\[Sysname-ring-group1\] domain 1 ring 1 to 3 5]{lang="EN-US"}

[\[Sysname-ring-group1\] domain 2 ring 1 to 3 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1793871595}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **rrpp** **ring-group**]{lang="EN-US"}]{#struct_0_20339_21110_1352395788}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rrpp]{lang="EN-US"}**[ **ring-group**]{lang="EN-US"}]{#struct_0_20339_21110_1283841573}
:::

::: {#-408056270 .myid}
[]{#_Toc173836544}[]{#_Toc404795735}[]{#struct_0_20339_21110_x230823158}[]{#_Toc345072398}[]{#_Toc345072227}[]{#_Toc257636540}[]{#_Toc211322916}[]{#_Toc209515189}[]{#_Toc208909637}[]{#_Toc194914045}

**RRPP \-- RRPP配置命令 \-- fast-detection enable**

------------------------------------------------------------------------

[**[fast-detection]{lang="EN-US"}**]{#struct_0_20339_21110_1109809069}[ **enable**]{lang="EN-US"}[命令用来使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的快速检测功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_20339_21110_219888731}**[fast-detection]{lang="EN-US"}**[ **enable**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的快速检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_579190720}

[**[fast-detection]{lang="EN-US"}**]{#struct_0_20339_21110_x1646592849}[ **enable**]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_20339_21110_812897109}**[fast-detection]{lang="EN-US"}**[ ]{lang="EN-US"}**[enable]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1211841758}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_32453037}[域的快速检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_177127227}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1584406145}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_1255366687}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x975476342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1246446043}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_77082574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须同时使能]{style="font-family:宋体"}]{#struct_0_20339_21110_x734105290}[RRPP]{lang="EN-US"}[域的快速检测功能、]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议和]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环，]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的快速检测功能才会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能]{style="font-family:宋体"}]{#struct_0_20339_21110_x768107777}[RRPP]{lang="EN-US"}[域的快速检测功能时，请先在边缘节点上使能、再在辅助边缘节点上使能，否则辅助边缘节点可能会因收不到]{style="font-family:宋体"}[Fast-Edge-Hello]{lang="EN-US"}[报文而误认为主环故障。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_1082290506}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_x463898700}[使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的快速检测功能。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_1336966384}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] fast-detection enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1805178170}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ring]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_20339_21110_x1349420306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rrpp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_20339_21110_338734964}
:::

::: {#1122497786 .myid}
[]{#_Toc345072407}[]{#_Toc345072236}[]{#_Toc345062691}[]{#_Toc257636549}[]{#_Toc211322925}[]{#_Toc209515198}[]{#_Toc341775644}[]{#_Toc404795736}[]{#struct_0_20339_21110_179781198}[]{#_Toc363114884}

**RRPP \-- RRPP配置命令 \-- fast-edge-timer**

------------------------------------------------------------------------

[**[fast-edge-timer]{lang="EN-US"}**]{#struct_0_20339_21110_718594833}[命令用来配置]{style="font-family:宋体"}[Fast-Edge-Hello]{lang="EN-US"}[和]{style="font-family:宋体"}[Fast-Edge-Fail]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fast-edge-timer**]{lang="EN-US"}]{#struct_0_20339_21110_794212864}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x575287547}

[**[fast-edge-timer]{lang="EN-US"}**[ **hello-timer**]{lang="EN-US"}[ *hello-value* **fail-timer** *fail-value*]{lang="EN-US"}]{#struct_0_20339_21110_x483793435}

[**[undo]{lang="EN-US"}**[ **fast-edge-timer**]{lang="EN-US"}]{#struct_0_20339_21110_791859317}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_910855474}

[[Fast-Edge-Hello]{lang="EN-US"}]{#struct_0_20339_21110_x145484841}[定时器为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[Fast-Edge-Fail]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_422461158}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1101304886}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_825161329}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_1619779728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_1727476990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1867757010}

[**[hello-timer]{lang="EN-US"}**[ *hello-value*]{lang="EN-US"}]{#struct_0_20339_21110_x175505472}[：]{style="font-family:宋体"}[Fast-Edge-Hello]{lang="NO-BOK"}[定时器的值，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[fail-timer]{lang="EN-US"}***[ fail-value]{lang="EN-US"}*]{#struct_0_20339_21110_x1693647016}[：]{style="font-family:宋体"}[Fast-Edge-]{lang="EN-US"}[Fail]{lang="SV"}[定时器的值，取值范围为]{style="font-family:
宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_1477652126}

[[Fast-Edge-Fail]{lang="EN-US"}]{#struct_0_20339_21110_44047865}[定时器不得小于]{style="font-family:宋体"}[Fast-Edge-Hello]{lang="EN-US"}[定时器的]{style="font-family:宋体"}[3]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x450364219}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_1499144125}[配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[Fast-Edge-Hello]{lang="EN-US"}[定时器为]{style="font-family:
宋体"}[20]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[Fast-Edge-Fail]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[70]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_913517304}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] fast-edge-timer hello-timer 20 fail-timer 70]{lang="EN-US"}
:::

::: {#954166257 .myid}
[]{#_Toc404795737}[]{#struct_0_20339_21110_10266531}

**RRPP \-- RRPP配置命令 \-- fast-timer**

------------------------------------------------------------------------

[**[fast-timer]{lang="EN-US"}**]{#struct_0_20339_21110_1508278770}[命令用来配置]{style="font-family:宋体"}[Fast-Hello]{lang="EN-US"}[和]{style="font-family:宋体"}[Fast-Fail]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fast-timer**]{lang="EN-US"}]{#struct_0_20339_21110_1915209990}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_418067867}

[**[fast-timer]{lang="EN-US"}**[ **hello-timer**]{lang="EN-US"}[ *hello-value* **fail-timer** *fail-value*]{lang="EN-US"}]{#struct_0_20339_21110_286113372}

[**[undo]{lang="EN-US"}**[ **fast-timer**]{lang="EN-US"}]{#struct_0_20339_21110_1058710713}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_1035236339}

[[Fast-Hello]{lang="EN-US"}]{#struct_0_20339_21110_x1330172892}[定时器为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[Fast-Fail]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[60]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_x275469059}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x2000623345}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x305599605}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_336857782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1187808274}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_x416492313}

[**[hello-timer]{lang="EN-US"}**[ *hello-value*]{lang="EN-US"}]{#struct_0_20339_21110_x1479546522}[：]{style="font-family:宋体"}[Fast-Hello]{lang="NO-BOK"}[定时器的值，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[fail-timer]{lang="EN-US"}***[ fail-value]{lang="EN-US"}*]{#struct_0_20339_21110_1927489498}[：]{style="font-family:宋体"}[Fast-]{lang="EN-US"}[Fail]{lang="SV"}[定时器的值，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_x912503594}

[[Fast-Fail]{lang="EN-US"}]{#struct_0_20339_21110_x1005488970}[定时器不得小于]{style="font-family:宋体"}[Fast-Hello]{lang="EN-US"}[定时器的]{style="font-family:宋体"}[3]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x2049942912}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_1026336803}[配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[Fast-Hello]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[Fast-Fail]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[70]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_1571965645}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] fast-timer hello-timer 20 fail-timer 70]{lang="EN-US"}
:::

::: {#-2042295064 .myid}
[]{#_Toc404795738}[]{#struct_0_20339_21110_x572550732}[]{#_Toc345072399}[]{#_Toc345072228}[]{#_Toc257636541}

**RRPP \-- RRPP配置命令 \-- protected-vlan**

------------------------------------------------------------------------

[**[protected-vlan]{lang="EN-US"}**]{#struct_0_20339_21110_1642791520}[命令用来配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **protected-vlan**]{lang="EN-US"}]{#struct_0_20339_21110_x1279870963}[命令用来删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1546117958}

[**[protected-vlan]{lang="EN-US"}**[ **reference-instance** *instance-id-list*]{lang="EN-US"}]{#struct_0_20339_21110_x758055758}

[**[undo]{lang="EN-US"}**[ **protected-vlan** \[ **reference-instance** *instance-id-list* \]]{lang="EN-US"}]{#struct_0_20339_21110_1375971994}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1425096882}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_678940443}[域不保护任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_819014513}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_731566119}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_954168789}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_1164319277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_917644209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_1656109912}

[**[reference-instance]{lang="EN-US"}***[ instance-id-list]{lang="EN-US"}*]{#struct_0_20339_21110_x994224851}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[。]{style="font-family:宋体"}*[instance-id-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[instance-id-list ]{lang="EN-US"}*[= { *instance-id* \[ **to** *instance-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的映射关系可通过命令]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ **stp** **region-configuration**]{lang="EN-US"}[查看。如果未指定本参数，将删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域引用的所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_639629290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_20339_21110_x907521616}[RRPP]{lang="EN-US"}[环之前，可删除或修改已配置好的保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[；配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环之后，也允许删除或修改已配置好的保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，但不允许将该域内所有保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的相关配置都删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若]{style="font-family:宋体"}]{#struct_0_20339_21110_x1381341729}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的映射关系发生变化，]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域实际保护的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[也会随之改变。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x887143498}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_590925765}[先将]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[映射到]{style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[上，并激活]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的配置；然后配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的主控制]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[、保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[MSTI 1]{lang="EN-US"}[所映射的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_1132359924}

[\[Sysname\] stp region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\] instance 1 vlan 1 to 30]{lang="EN-US"}

[\[Sysname-mst-region\] active region-configuration]{lang="EN-US"}

[\[Sysname-mst-region\] quit]{lang="EN-US"}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] control-vlan 100]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] protected-vlan reference-instance 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1044429443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **stp** **region-configuration**]{lang="EN-US"}]{#struct_0_20339_21110_1726558416}[（二层技术]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[生成树）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rrpp]{lang="EN-US"}**[ **domain**]{lang="EN-US"}]{#struct_0_20339_21110_445175827}
:::

::: {#-1996641840 .myid}
[]{#_Toc404795739}[]{#struct_0_20339_21110_1438627148}[]{#_Toc345072400}[]{#_Toc345072229}[]{#_Toc257636542}[]{#_Toc350937950}[]{#_Toc137470866}[]{#_Toc137475401}[]{#_Toc137547100}[]{#_Toc137470867}[]{#_Toc137475402}[]{#_Toc137547101}[]{#_Toc137470868}[]{#_Toc137475403}[]{#_Toc137547102}[]{#_Toc137470869}[]{#_Toc137475404}[]{#_Toc137547103}[]{#_ring}

**RRPP \-- RRPP配置命令 \-- reset rrpp statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **rrpp** **statistics**]{lang="EN-US"}]{#struct_0_20339_21110_35305220}[命令用来清除]{style="font-family:
宋体"}[RRPP]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1221652055}

[**[reset]{lang="EN-US"}**]{#struct_0_20339_21110_965418191}[ **rrpp** **statistics** **domain** *domain-id* \[ **ring** *ring-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_1841739857}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20339_21110_1727356141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_902122192}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1190345149}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_1280480760}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1254590740}

[**[domain]{lang="EN-US"}**]{#struct_0_20339_21110_x1938621156}[ ]{lang="EN-US"}*[domain-id]{lang="EN-US"}*[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12]{lang="FR"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ring]{lang="EN-US"}**]{#struct_0_20339_21110_1963470125}*[ ]{lang="EN-US"}[ring-id]{lang="EN-US"}*[：清除]{style="font-family:宋体"}[指定环的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}*[ring-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}[将]{style="font-family:宋体"}[清除该域中]{style="font-family:宋体"}[所有环的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_1900827466}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_x1423540039}[清除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中环]{style="font-family:
宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset rrpp statistics domain 1 ring 10]{lang="EN-US"}]{#struct_0_20339_21110_884263919}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_782923417}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **rrpp** **statistics**]{lang="EN-US"}]{#struct_0_20339_21110_x80574444}
:::

::: {#-1885171422 .myid}
[]{#_Toc404795740}[]{#struct_0_20339_21110_59360237}[]{#_Toc345072401}[]{#_Toc345072230}[]{#_Toc257636543}[]{#_Toc124742948}[]{#_Toc101584100}[]{#_ring_enable}

**RRPP \-- RRPP配置命令 \-- ring**

------------------------------------------------------------------------

[**[ring]{lang="EN-US"}**]{#struct_0_20339_21110_x1489340043}[命令用来配置当前设备的节点角色、]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[端口以及环的级别。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ring**]{lang="EN-US"}]{#struct_0_20339_21110_459477267}[命令用来删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1714726181}

[**[ring]{lang="EN-US"}**[ *ring-id* **node-mode** { { **master** \| **transit** } \[ **primary-port** *interface-type interface-number* \] \[ **secondary-port** *interface-type interface-number* \] **level** *level-value \|* { **assistant-edge** \| **edge** } \[ **edge-port** *interface-type interface-number* \] }]{lang="EN-US"}]{#struct_0_20339_21110_326326240}

[**[undo]{lang="EN-US"}**[ **ring**]{lang="EN-US"}[ *ring-id*]{lang="EN-US"}]{#struct_0_20339_21110_1436628030}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_1345960366}

[[设备不是]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x2094906703}[环的节点。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_1768100659}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1775414353}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x89078687}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1646658385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_477154626}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_x378479666}

[*[ring-id]{lang="EN-US"}*]{#struct_0_20339_21110_1021634834}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[master]{lang="EN-US"}**]{#struct_0_20339_21110_390160687}[：指定当前设备为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的主节点。]{style="font-family:宋体"}

[**[transit]{lang="EN-US"}**]{#struct_0_20339_21110_160826597}[：指定当前设备为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的传输节点。]{style="font-family:宋体"}

[**[primary-port]{lang="EN-US"}**]{#struct_0_20339_21110_770140981}[：指定本节点的主端口。]{style="font-family:宋体"}

[*[i]{lang="EN-US"}[nterface-type interface-number]{lang="EN-US"}*]{#struct_0_20339_21110_1153180403}[：指定端口类型和端口编号。]{style="font-family:宋体"}

[**[secondary-port]{lang="EN-US"}**]{#struct_0_20339_21110_1783178482}[：指定本节点的副端口。]{style="font-family:宋体"}

[**[level]{lang="EN-US"}**[ ]{lang="EN-US"}*[level-value]{lang="EN-US"}*]{#struct_0_20339_21110_x1481059726}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的级别，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:
宋体"}[0]{lang="EN-US"}[表示主环，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示子环。]{style="font-family:宋体"}

[**[assistant-edge]{lang="EN-US"}**]{#struct_0_20339_21110_42471076}[：指定当前设备为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的辅助边缘节点。]{style="font-family:宋体"}

[**[edge]{lang="EN-US"}**]{#struct_0_20339_21110_1082224970}[：指定当前设备为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的边缘节点。]{style="font-family:宋体"}

[**[edge-port]{lang="EN-US"}**]{#struct_0_20339_21110_1112164897}[：指定本节点的边缘端口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_1608898411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一]{lang="EN-US" style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_2148282}[域中不同的]{lang="EN-US" style="font-family:宋体"}[RRPP]{lang="EN-US"}[环不能使用相同的环]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_20339_21110_x44545408}[RRPP]{lang="EN-US"}[环处于激活状态时不能配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置边缘节点和辅助边缘节点时，必须先配置主环再配置子环。]{style="font-family:宋体"}]{#struct_0_20339_21110_1901018858}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x646330171}[环的节点角色、]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[端口以及环的级别一经配置就不能修改，若要改变这些配置，必须先删除原有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除边缘节点或辅助边缘节点的主环配置之前，必须先删除所有的子环配置。但是，处于激活状态的]{style="font-family:宋体"}]{#struct_0_20339_21110_1606029573}[RRPP]{lang="EN-US"}[环不能被删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备上的]{style="font-family:宋体"}]{#struct_0_20339_21110_1727282531}[RRPP]{lang="EN-US"}[协议已使能时，必须先关闭]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环才能删除该环；当设备上的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议未使能时，可以直接删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环，且该环的使能配置将被一并清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1801577130}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_x483858971}[配置当前设备为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中主环]{style="font-family:
宋体"}[10]{lang="EN-US"}[的主节点，主端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，副端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_x1442471789}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] control-vlan 100]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] protected-vlan reference-instance 0 1 2]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] ring 10 node-mode master primary-port gigabitethernet 1/0/1 secondary-port gigabitethernet 1/0/2 level 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_862835618}[先配置当前设备为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中主环]{style="font-family:
宋体"}[10]{lang="FR"}[的传输节点]{style="font-family:宋体"}[，]{style="font-family:宋体"}[主端口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[，]{style="font-family:宋体"}[副端口为]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="FR"}[；再]{style="font-family:宋体"}[配置当前设备为]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中子环]{style="font-family:宋体"}[20]{lang="EN-US"}[的边缘节点，边缘端口为]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_1328964763}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] control-vlan 100]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] protected-vlan reference-instance 0 1 2]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] ring 10 node-mode transit primary-port gigabitethernet 1/0/1 secondary-port gigabitethernet 1/0/2 level 0]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] ring 20 node-mode edge edge-port gigabitethernet 1/0/3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x908566449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ring]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_20339_21110_1536023165}
:::

::: {#812327073 .myid}
[]{#_Toc404795741}[]{#struct_0_20339_21110_1561495995}[]{#_Toc345072402}[]{#_Toc345072231}[]{#_Toc257636544}[]{#_Toc124742949}[]{#_Toc101584101}[]{#_Toc137470872}[]{#_Toc137475407}[]{#_Toc137547106}[]{#_Toc137470874}[]{#_Toc137475409}[]{#_Toc137547108}[]{#_Toc137470875}[]{#_Toc137475410}[]{#_Toc137547109}[]{#_rrpp_domain}

**RRPP \-- RRPP配置命令 \-- ring enable**

------------------------------------------------------------------------

[**[ring]{lang="EN-US"}**]{#struct_0_20339_21110_60922455}[ **enable**]{lang="EN-US"}[命令用来使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**]{#struct_0_20339_21110_x1693712552}[ **ring** **enable**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_136045130}

[**[ring]{lang="EN-US"}**]{#struct_0_20339_21110_x1351366685}[ *ring-id* **enable**]{lang="EN-US"}

[**[undo]{lang="EN-US"}**]{#struct_0_20339_21110_1015141113}[ **ring** *ring-id* **enable**]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_1296666732}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_27410846}[环处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_839672140}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1791884696}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_1124215321}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_1851184719}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_738415239}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_1035170803}

[*[ring-id]{lang="EN-US"}*]{#struct_0_20339_21110_251335932}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_519710783}

[[只有当]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_355449892}[协议和]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环都使能后，当前设备的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环才能激活。]{style="font-family:宋体"}

[[在一台设备上使能子环之前必须先使能主环，而关闭主环之前也必须先关闭所有子环，否则系统将提示出错。]{style="font-family:宋体"}]{#struct_0_20339_21110_1377092072}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x2007491006}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_1929466279}[使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[RRPP]{lang="EN-US"}[环]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_859130403}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] control-vlan 100]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] protected-vlan reference-instance 0 1 2]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] ring 10 node-mode master primary-port gigabitethernet 1/0/1 secondary-port gigabitethernet 1/0/2 level 0]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] ring 10 enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1628980481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rrpp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_20339_21110_x642895168}
:::

::: {#-1669193074 .myid}
[]{#_Toc404795742}[]{#struct_0_20339_21110_x2050008448}[]{#_Toc345072403}[]{#_Toc345072232}[]{#_Toc257636545}[]{#_Toc124742950}[]{#_Toc101584102}[]{#_Toc137470879}[]{#_Toc137475414}[]{#_Toc137547113}[]{#_rrpp_enable}

**RRPP \-- RRPP配置命令 \-- rrpp domain**

------------------------------------------------------------------------

[**[rrpp]{lang="EN-US"}**[ **domain**]{lang="EN-US"}]{#struct_0_20339_21110_143636254}[命令用来创建]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域，并进入]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rrpp** **domain**]{lang="EN-US"}]{#struct_0_20339_21110_966393456}[命令用来删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x13875922}

[**[rrpp]{lang="EN-US"}**[ **domain** *domain-id*]{lang="EN-US"}]{#struct_0_20339_21110_x1101131019}

[**[undo]{lang="EN-US"}**[ **rrpp** **domain** *domain-id*]{lang="EN-US"}]{#struct_0_20339_21110_460449207}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1619188167}

[[不存在任何]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1830551586}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1065389233}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20339_21110_165142090}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_977806476}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x118872832}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_678874907}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_838084775}

[*[domain-id]{lang="EN-US"}*]{#struct_0_20339_21110_x1844842535}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_634914715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_20339_21110_1925111532}[RRPP]{lang="EN-US"}[域时，将同时删除该域所有控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和保护]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_20339_21110_1934534747}[RRPP]{lang="EN-US"}[域时，必须保证该]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域内尚未配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环，否则将导致删除失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_1699234312}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_1146694491}[创建]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:
宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_x2101186257}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1320050822}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[control-vlan]{lang="EN-US"}**]{#struct_0_20339_21110_1612827291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[protected-vlan]{lang="EN-US"}**]{#struct_0_20339_21110_x887209034}
:::

::: {#-317504513 .myid}
[]{#_Toc404795743}[]{#struct_0_20339_21110_x2125458424}[]{#_Toc345072404}[]{#_Toc345072233}[]{#_Toc257636546}[]{#_Toc124742951}[]{#_Toc101584103}[]{#_Toc137470881}[]{#_Toc137475416}[]{#_Toc137547115}[]{#_Toc137470883}[]{#_Toc137475418}[]{#_Toc137547117}[]{#_Toc124742952}[]{#_Toc124742953}[]{#_Toc124742954}[]{#_Toc124742955}[]{#_Toc124742956}[]{#_Toc124742957}[]{#_Toc124742958}[]{#_Toc124742959}[]{#_Toc124742960}[]{#_Toc124742961}[]{#_Toc124742962}[]{#_Toc124742963}[]{#_Toc124742964}[]{#_Toc124742965}[]{#_Toc124742966}[]{#_Toc124742968}[]{#_Toc124742969}[]{#_Toc124742971}[]{#_timer}

**RRPP \-- RRPP配置命令 \-- rrpp enable**

------------------------------------------------------------------------

[**[rrpp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_20339_21110_1533524016}[命令用来使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rrpp** **enable**]{lang="EN-US"}]{#struct_0_20339_21110_x1288158710}[命令用来关闭]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_90291353}

[**[rrpp]{lang="EN-US"}**]{#struct_0_20339_21110_x597899461}[ **enable**]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **rrpp** **enable**]{lang="EN-US"}]{#struct_0_20339_21110_533400883}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_x517035792}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x2040516734}[协议处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_284228091}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20339_21110_482883348}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x97879234}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_441052116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_75332528}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_1841674321}

[[只有当]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_177959206}[协议和]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环都使能后，当前设备的]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域才能激活。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1661198953}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_x50159036}[使能]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_2059333960}

[\[Sysname\] rrpp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1966914074}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ring]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_20339_21110_2024482068}
:::

::: {#776687464 .myid}
[]{#_Toc404795744}[]{#struct_0_20339_21110_853807383}[]{#_Toc345072405}[]{#_Toc345072234}[]{#_Toc257636547}[]{#_Toc173836550}

**RRPP \-- RRPP配置命令 \-- rrpp ring-group**

------------------------------------------------------------------------

[**[rrpp]{lang="EN-US"}**[ **ring-group**]{lang="EN-US"}]{#struct_0_20339_21110_1353294655}[命令用来创建]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组，并进入]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rrpp** **ring-group**]{lang="EN-US"}]{#struct_0_20339_21110_x1072016662}[命令用来删除]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_1245141003}

[**[rrpp]{lang="EN-US"}**[ **ring-group** *ring-group-id*]{lang="EN-US"}]{#struct_0_20339_21110_x1507936174}

[**[undo]{lang="EN-US"}**[ **rrpp** **ring-group** *ring-group-id*]{lang="EN-US"}]{#struct_0_20339_21110_x25755359}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_x80639980}

[[不存在任何]{style="font-family:宋体"}[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_x1963259276}[环组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1054809831}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20339_21110_x1729460271}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x380751280}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_x289883728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1415196459}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_1769058442}

[*[ring-group-id]{lang="EN-US"}*]{#struct_0_20339_21110_x978931977}[：]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1550807484}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除环组时，应先删除边缘节点环组，再删除辅助边缘节点环组，否则辅助边缘节点可能会因收不到]{style="font-family:宋体"}]{#struct_0_20339_21110_x1084159303}[Edge-Hello]{lang="EN-US"}[报文而误认为主环故障。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除环组后，原环组内的所有子环不再属于任何环组。]{style="font-family:宋体"}]{#struct_0_20339_21110_1120041120}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x273635203}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_x1646723921}[创建]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[环组]{style="font-family:宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_x660904359}

[\[Sysname\] rrpp ring-group 1]{lang="EN-US"}

[\[Sysname-ring-group1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1833241585}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **rrpp** **ring-group**]{lang="EN-US"}]{#struct_0_20339_21110_377816892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain]{lang="EN-US"}**[ **ring**]{lang="EN-US"}]{#struct_0_20339_21110_x124352629}
:::

::: {#-1113860339 .myid}
[]{#_Toc404795745}[]{#struct_0_20339_21110_1028581935}[]{#_Toc345072406}[]{#_Toc345072235}[]{#_Toc257636548}[]{#_Toc350937957}

**RRPP \-- RRPP配置命令 \-- timer**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**]{#struct_0_20339_21110_x1436506153}[命令用来配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[和]{style="font-family:宋体"}[Fail]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_20339_21110_960442587}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1206745069}

[**[timer]{lang="EN-US"}**[ **hello-timer** *hello-value* **fail-timer** *fail-value*]{lang="EN-US"}]{#struct_0_20339_21110_1769782748}

[**[undo]{lang="EN-US"}**[ **timer**]{lang="EN-US"}]{#struct_0_20339_21110_1082159434}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20339_21110_x420853995}

[[Hello]{lang="EN-US"}]{#struct_0_20339_21110_x700817484}[定时器为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Fail]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20339_21110_1937461182}

[[RRPP]{lang="EN-US"}]{#struct_0_20339_21110_1572446212}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20339_21110_x731647963}

[[network-admin]{lang="EN-US"}]{#struct_0_20339_21110_1443988741}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20339_21110_x1967528053}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20339_21110_1311178553}

[**[hello-timer]{lang="EN-US"}**[ *hello-value*]{lang="EN-US"}]{#struct_0_20339_21110_x1559057949}[：]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[fail-timer]{lang="EN-US"}***[ fail-value]{lang="EN-US"}*]{#struct_0_20339_21110_x1046916625}[：]{style="font-family:宋体"}[Fail]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20339_21110_x1361678399}

[[Fail]{lang="EN-US"}]{#struct_0_20339_21110_x483924507}[定时器]{style="font-family:宋体"}[不得小于]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器]{style="font-family:宋体"}[的]{style="font-family:宋体"}[3]{lang="EN-US"}[倍。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20339_21110_x772794437}

[[\# ]{lang="EN-US"}]{#struct_0_20339_21110_1113249034}[配置]{style="font-family:宋体"}[RRPP]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[Hello]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Fail]{lang="EN-US"}[定时器为]{style="font-family:宋体"}[7]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20339_21110_x781044319}

[\[Sysname\] rrpp domain 1]{lang="EN-US"}

[\[Sysname-rrpp-domain1\] timer hello-timer 2 fail-timer 7]{lang="EN-US"}
:::
