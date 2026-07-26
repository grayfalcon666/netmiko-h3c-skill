::: {#-1019366349 .myid}
[]{#_Toc404795751}[]{#struct_0_64120_x1583_637463131}

**Smart Link \-- Smart Link调试命令 \-- debugging smart-link**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_64120_x1583_x687627838}

[**[debugging smart-link]{lang="EN-US"}**[ \[ **group** *group-id* \] { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_64120_x1583_x1811147501}

[**[undo debugging smart-link]{lang="EN-US"}**[ \[ **group** *group-id* \] { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_64120_x1583_x1936968538}

[[【视图】]{style="font-family:黑体"}]{#struct_0_64120_x1583_x1884403831}

[[用户视图]{style="font-family:宋体"}]{#struct_0_64120_x1583_x1317689176}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_64120_x1583_x1679201374}

[[network-admin]{lang="EN-US"}]{#struct_0_64120_x1583_x1177064120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_64120_x1583_x770036765}

[[【参数】]{style="font-family:黑体"}]{#struct_0_64120_x1583_x351879878}

[**[group]{lang="EN-US"}***[ group-id]{lang="EN-US"}*]{#struct_0_64120_x1583_1015751495}[：表示指定]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组的调试信息开关。如果未指定本参数，则表示所有]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组的调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_64120_x1583_103518242}[：表示]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_64120_x1583_x1811081965}[：表示]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_64120_x1583_x1404987950}[：表示]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_64120_x1583_1956886014}[：表示]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_64120_x1583_2107009126}[：表示]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_64120_x1583_1578709214}

[**[debugging smart-link]{lang="EN-US"}**]{#struct_0_64120_x1583_1644960561}[命令用来打开]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组调试信息开关。]{style="font-family:宋体"}**[undo debugging smart-link]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}]{#struct_0_64120_x1583_2113487540}[组调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging smart-link error]{lang="EN-US"}]{#struct_0_64120_x1583_x1556845121}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1589590194}[[字段]{style="font-family:黑体"}]{#struct_0_64120_x1583_x1011899153}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_64120_x1583_x1811016429}

[[Failed to allocate memory for *String*]{lang="EN-US"}]{#struct_0_64120_x1583_2035469746}

[[分配内存失败。]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_64120_x1583_x1781647017}[表示为该操作分配内存时发生失败，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[batch bak]{lang="EN-US"}]{#struct_0_64120_x1583_x1475355370}[：表示批量备份]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[realtime bak]{lang="EN-US"}]{#struct_0_64120_x1583_1383022409}[：表示实时备份]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create group]{lang="EN-US"}]{#struct_0_64120_x1583_x1988784580}[：表示创建]{lang="EN-US" style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[mart]{lang="EN-US"}]{#struct_0_64120_x1583_x1273174403}[ l]{lang="EN-US"}[ink]{lang="EN-US"}[ port info]{lang="SV"}[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:
  宋体"}[Smart Link]{lang="SV"}[端口信息]{lang="EN-US" style="font-family:宋体"}

[[Failed to send *String* backup message]{lang="EN-US"}]{#struct_0_64120_x1583_x1810426605}

[[发送备份消息失败。]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_64120_x1583_x1770624464}[表示为该操作发送备份消息时发生失败，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[batch]{lang="EN-US"}]{#struct_0_64120_x1583_x984841075}[：表示发送批量备份消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[r]{lang="EN-US"}[ealtime]{lang="EN-US"}]{#struct_0_64120_x1583_1257159174}[：表示发送实时备份消息]{lang="EN-US" style="font-family:宋体"}

[[Port *PortName:* Received error packet because *String*]{lang="EN-US"}]{#struct_0_64120_x1583_1211192626}

[[端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_64120_x1583_x164553778}[接收了错误的]{style="font-family:宋体"}[Flush]{lang="EN-US"}[报文。]{style="font-family:宋体"}*[String]{lang="EN-US"}*[表示错误原因，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[length of]{lang="EN-US"}]{#struct_0_64120_x1583_x1810361069}[ s]{lang="EN-US"}[mart link]{lang="EN-US"}[ PDU is ]{lang="EN-US"}[illegal]{lang="EN-US"}[：表示报文长度非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control type]{lang="EN-US"}]{#struct_0_64120_x1583_x849276198}[ is ]{lang="EN-US"}[illegal]{lang="EN-US"}[：表示控制类型非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[control version]{lang="IT"}]{#struct_0_64120_x1583_33641729}[ is ]{lang="EN-US"}[illegal]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示控制版本非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[control VLAN]{lang="IT"}]{#struct_0_64120_x1583_702164228}[ is ]{lang="EN-US"}[illegal]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="IT"}[非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control VLAN is different]{lang="EN-US"}]{#struct_0_64120_x1583_1489568354}[：表示报文发送控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[与配置的接收控制]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[不同]{lang="EN-US" style="font-family:宋体"}

[[Smart link group *group-id*: Failed to check control VLAN]{lang="EN-US"}]{#struct_0_64120_x1583_1600770548}

[[Smart Link]{lang="EN-US"}]{#struct_0_64120_x1583_x1810950892}[组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[的控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不存在或者端口不允许其]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[通过]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging smart-link event]{lang="EN-US"}]{#struct_0_64120_x1583_514564320}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1585910002}[[字段]{style="font-family:黑体"}]{#struct_0_64120_x1583_1936310013}

[[描述]{style="font-family:黑体"}]{#struct_0_64120_x1583_1567298879}

[[Smart link group *group-id* *PortName*: Deleting MAC and updating ARP on the port]{lang="EN-US"}]{#struct_0_64120_x1583_850636600}

[[删除]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}]{#struct_0_64120_x1583_935274249}[组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[的端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[上的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址转发表项并更新]{style="font-family:宋体"}[ARP/ND]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Deleting MAC and updating ARP on the device]{lang="EN-US"}]{#struct_0_64120_x1583_x1812833909}

[[删除设备上所有端口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_64120_x1583_1898954136}[地址转发表项并更新]{style="font-family:宋体"}[ARP/ND]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Smart link group *group-id* *PortName*: Link status is up/down]{lang="EN-US"}]{#struct_0_64120_x1583_x1810885356}

[[Smart Link]{lang="EN-US"}]{#struct_0_64120_x1583_x1289817270}[组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[的端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[的链路状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}[或]{style="font-family:宋体"}[down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging smart-link fsm]{lang="EN-US"}]{#struct_0_64120_x1583_1255529575}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1586769394}[[字段]{style="font-family:黑体"}]{#struct_0_64120_x1583_1723552934}

[[描述]{style="font-family:黑体"}]{#struct_0_64120_x1583_1162615923}

[[Smart link group *group-id* port *PortName*: *String*]{lang="EN-US"}]{#struct_0_64120_x1583_228104847}

[[Smart Link]{lang="EN-US"}]{#struct_0_64120_x1583_1517340192}[组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[的端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[上的状态机事件。]{style="font-family:宋体"}*[String]{lang="EN-US"}*[表示事件，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State preempts to be active/standby]{lang="EN-US"}]{#struct_0_64120_x1583_x1810819820}[：表示状态抢占为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[standby]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State doesn\'t change]{lang="EN-US"}]{#struct_0_64120_x1583_582745482}[：表示状态没有改变]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State changes to active/standby]{lang="EN-US"}]{#struct_0_64120_x1583_455430390}[：表示状态变为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[standby]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delay timer starts/expires]{lang="EN-US"}]{#struct_0_64120_x1583_1443607069}[/ends]{lang="EN-US"}[：表示延时定时器启动]{lang="EN-US" style="font-family:宋体"}[、]{style="font-family:
  宋体"}[超时]{lang="EN-US" style="font-family:宋体"}[或停止]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging smart-link packet]{lang="EN-US"}]{#struct_0_64120_x1583_x1102840697}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1592267282}[[字段]{style="font-family:黑体"}]{#struct_0_64120_x1583_x1284561853}

[[描述]{style="font-family:黑体"}]{#struct_0_64120_x1583_756486646}

[[Smart link group *group-id* sent packet]{lang="EN-US"}]{#struct_0_64120_x1583_x1384188175}

[[Smart Link]{lang="EN-US"}]{#struct_0_64120_x1583_x1810754284}[组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}[Flush]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Port *PortName*: Sent flush packet]{lang="EN-US"}]{#struct_0_64120_x1583_256597132}

[[端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_64120_x1583_212122266}[发送]{style="font-family:宋体"}[Flush]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Port *PortName*: Received flush packet]{lang="EN-US"}]{#struct_0_64120_x1583_528093261}

[[端口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_64120_x1583_x440435662}[接收]{style="font-family:宋体"}[Flush]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Device ID]{lang="EN-US"}]{#struct_0_64120_x1583_x2145799293}

[[设备标识]{style="font-family:宋体"}]{#struct_0_64120_x1583_x1811213036}

[[Control VLAN]{lang="SV"}]{#struct_0_64120_x1583_72368721}

[[控制]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_64120_x1583_79162838}[的编号]{style="font-family:宋体"}

[[VLAN bit map]{lang="SV"}]{#struct_0_64120_x1583_42702543}

[[VLAN]{lang="EN-US"}]{#struct_0_64120_x1583_x508496107}[位图，表示]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组中阻塞端口允许通过的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_64120_x1583_x454567273}

[[\# ]{lang="EN-US"}]{#struct_0_64120_x1583_x1856323024}[在一台开启接收]{style="font-family:宋体"}[Flush]{lang="EN-US"}[报文功能的设备上打开]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging smart-link error]{lang="NO-BOK"}]{#struct_0_64120_x1583_x1811147500}

[\*Apr  6 15:06:18:017 2012 Sysname SMLK/7/Pkt: -MDC=1; Port GigabitEthernet1/0/1: Received error packet because control VLAN is different.]{lang="NO-BOK"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_64120_x1583_791914817}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="NO-BOK"}[接收了]{style="font-family:宋体"}[错误的]{style="font-family:宋体"}[Flush]{lang="NO-BOK"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[原因为]{style="font-family:宋体"}[报文发送控制]{style="font-family:宋体"}[VLAN]{lang="NO-BOK"}[与配置的接收控制]{style="font-family:宋体"}[VLAN]{lang="NO-BOK"}[不同]{style="font-family:宋体"}*

[[\# ]{lang="NO-BOK"}]{#struct_0_64120_x1583_1241682007}[打开]{style="font-family:宋体"}[Smart Link]{lang="NO-BOK"}[组]{style="font-family:宋体"}[1]{lang="NO-BOK"}[的状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging smart-link group 1 fsm]{lang="EN-US"}]{#struct_0_64120_x1583_x1648600482}

[\*Apr  6 15:27:25:734 2012 ]{lang="EN-US"}[Sysname]{lang="NO-BOK"}[ SMLK/7/Fsm: -MDC=1; Smart link group 1 port GigabitEthernet1/0/1: State changes to active.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_64120_x1583_1059578367}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[成为]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的主端口]{style="font-family:宋体"}*

[[\*Apr  6 15:29:45:910 2012 ]{lang="EN-US"}]{#struct_0_64120_x1583_763873600}[Sysname]{lang="NO-BOK"}[ SMLK/7/Fsm: -MDC=1; Smart link group 1 port GigabitEthernet1/0/2: State changes to standby.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_64120_x1583_289935769}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[成为]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的从端口]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_64120_x1583_x253116373}[打开]{style="font-family:宋体"}[Smart Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[的报文调试信息开关，并对]{style="font-family:
宋体"}[Smart Link]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[进行链路切换。]{style="font-family:
宋体"}

[[\<Sysname\> debugging smart-link group 1 packet]{lang="EN-US"}]{#struct_0_64120_x1583_x1811081964}

[\*Apr  6 15:45:25:641 2012 ]{lang="EN-US"}[Sysname]{lang="NO-BOK"}[ SMLK/7/Pkt: -MDC=1;]{lang="EN-US"}

[Smart link group 1:]{lang="EN-US"}

[Port GigabitEthernet1/0/1: Sent flush packet]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_64120_x1583_1323895405}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Flush]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[Device ID: 0011-2200-0301]{lang="EN-US"}]{#struct_0_64120_x1583_1017566471}

[*[// ]{lang="EN-US"}*]{#struct_0_64120_x1583_x1564021325}*[设备标识为]{style="font-family:宋体"}[0011-2200-0301]{lang="EN-US"}*

[[Control VLAN: 1]{lang="EN-US"}]{#struct_0_64120_x1583_1460832017}

[*[// ]{lang="SV"}*]{#struct_0_64120_x1583_x521782279}*[控制]{style="font-family:宋体"}[VLAN]{lang="SV"}[为]{style="font-family:宋体"}[VLAN 1]{lang="SV"}*

[[VLAN bit map:]{lang="SV"}]{#struct_0_64120_x1583_x1811016428}

[02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[ ]{lang="SV"}

[\*Apr  6 15:45:27:629 2012 ]{lang="EN-US"}[Sysname]{lang="NO-BOK"}[ SMLK/7/Pkt:]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[*[// VLAN]{lang="SV"}*]{#struct_0_64120_x1583_x693413609}*[位图的具体内容]{style="font-family:宋体"}*
