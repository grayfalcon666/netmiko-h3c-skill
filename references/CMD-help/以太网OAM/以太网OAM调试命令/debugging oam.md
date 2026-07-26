::: {#-1475171543 .myid}
[]{#_Toc129683602}[]{#_Toc404795367}[]{#struct_0_x1739_x6365_x1025921143}

**以太网OAM \-- 以太网OAM调试命令 \-- debugging oam**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1739_x6365_394145966}

[**[debugging]{lang="EN-US"}**[ **oam** { **all** \| **error** \| **event** \| **fsm** \| **packet** \[ **receive** \| **send** \] } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1739_x6365_x1640278707}

[**[undo]{lang="EN-US"}**[ **debugging** **oam** { **all** \| **error** \| **event** \| **fsm** \| **packet** \[ **receive** \| **send** \] } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1739_x6365_x958795044}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1739_x6365_1141025697}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1739_x6365_x510663172}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1739_x6365_x1276676848}

[[network-admin]{lang="EN-US"}]{#struct_0_x1739_x6365_x1979456053}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1739_x6365_1900298923}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1739_x6365_925157634}

[**[all]{lang="EN-US"}**]{#struct_0_x1739_x6365_x319912208}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1739_x6365_1805117900}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1739_x6365_1299612060}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x1739_x6365_x104370385}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1739_x6365_1725624585}[：表示以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1739_x6365_245195065}[：表示接收的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1739_x6365_317724482}[：表示发送的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1739_x6365_837287601}[：表示指定接口，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，表示所有接口。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1739_x6365_1900364459}

[**[debugging]{lang="EN-US"}**[ **oam**]{lang="EN-US"}]{#struct_0_x1739_x6365_1297413750}[命令用来打开以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **oam**]{lang="EN-US"}[命令用来关闭以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1739_x6365_1672936019}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果不输入]{style="font-family:宋体"}**[send]{lang="EN-US"}**]{#struct_0_x1739_x6365_x1053626496}[和]{style="font-family:宋体"}**[receive]{lang="EN-US"}**[参数，则同时显示发送和接收的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文调试信息。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging oam event]{lang="EN-US"}]{#struct_0_x1739_x6365_1255348645}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x635009574}[[字段]{style="font-family:黑体"}]{#struct_0_x1739_x6365_x1430009336}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1739_x6365_x1086949698}

[[OAM Port *port*: *event*]{lang="FR"}]{#struct_0_x1739_x6365_767171051}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1739_x6365_1900429995}[接口]{style="font-family:宋体"}*[port]{lang="FR"}*[上发生了]{style="font-family:宋体"}*[event]{lang="FR"}*[事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging oam error]{lang="EN-US"}]{#struct_0_x1739_x6365_x656196384}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x606783590}[[字段]{style="font-family:黑体"}]{#struct_0_x1739_x6365_x215927205}

[[描述]{style="font-family:黑体"}]{#struct_0_x1739_x6365_756107165}

[[OAM Port ]{lang="EN-US"}]{#struct_0_x1739_x6365_1250537189}*[port]{lang="FR"}*[: ]{lang="EN-US"}*[error]{lang="FR"}*

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1739_x6365_469300281}[接口]{style="font-family:宋体"}*[port]{lang="FR"}*[在运行中发生了]{style="font-family:宋体"}*[error]{lang="FR"}*[错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging oam fsm]{lang="EN-US"}]{#struct_0_x1739_x6365_1241012850}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x608117830}[[字段]{style="font-family:黑体"}]{#struct_0_x1739_x6365_1131960995}

[[描述]{style="font-family:黑体"}]{#struct_0_x1739_x6365_1900495531}

[[OAM Port *port*: Discovery state transfers from state *state1* to state *state2*]{lang="EN-US"}]{#struct_0_x1739_x6365_2092984942}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1739_x6365_x1891951285}[接口]{style="font-family:宋体"}*[port]{lang="FR"}*[的]{style="font-family:宋体"}[Discovery]{lang="EN-US"}[状态机从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[[OAM Port *port*: Remote loopback state transfers from state *state1* to state *state2*]{lang="EN-US"}]{#struct_0_x1739_x6365_1573114244}

[[以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x1739_x6365_x1890252969}[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[状态机从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging oam packet]{lang="EN-US"}]{#struct_0_x1739_x6365_x770595960}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x604919014}[[字段]{style="font-family:黑体"}]{#struct_0_x1739_x6365_x309501898}

[[描述]{style="font-family:黑体"}]{#struct_0_x1739_x6365_1900561067}

[[Send/Receive OAM Packet Via Port *port*]{lang="EN-US"}]{#struct_0_x1739_x6365_x1829726244}

[[接口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_x1739_x6365_1100341268}[发送]{style="font-family:宋体"}[/]{lang="EN-US"}[收到了以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Pkt length]{lang="EN-US"}]{#struct_0_x1739_x6365_1583192230}

[[报文长度]{style="font-family:宋体"}]{#struct_0_x1739_x6365_998608413}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1739_x6365_x807442585}

[[\# ]{lang="EN-US"}]{#struct_0_x1739_x6365_1559300148}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能，并打开该接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[事件调试信息开关，然后拔掉网线。]{style="font-family:宋体"}

[[\<Sysname\> debugging oam event interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1739_x6365_1900626603}

[\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Event: -MDC=1;]{lang="EN-US"}

[OAM Port GigabitEthernet1/0/1: occurs link down event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1739_x6365_x239465250}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发生了]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1739_x6365_2137365391}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能，并打开该接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging oam error interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1739_x6365_x1631010569}

[\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Error: -MDC=1;]{lang="EN-US"}

[OAM Port gigabitethernet 1/0/1: Failed to enable or disable packet to CPU.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1739_x6365_x1425618771}*[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1739_x6365_622092089}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能，并打开该接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging oam fsm interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1739_x6365_1796282105}

[\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Fsm: -MDC=1;]{lang="EN-US"}

[OAM Port GigabitEthernet1/0/1: Discovery state transfers from state DIS%FAULT to state DIS%PASSIVE_WAIT.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1739_x6365_376074168}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery]{lang="EN-US"}[状态机从]{style="font-family:宋体"}[FAULT]{lang="EN-US"}[迁移到]{style="font-family:宋体"}[PASSIVE_WAIT]{lang="EN-US"}*

[[\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Fsm: -MDC=1;]{lang="EN-US"}]{#struct_0_x1739_x6365_1900692139}

[OAM Port GigabitEthernet1/0/1: Discovery state transfers from state DIS%PASSIVE_WAIT to state DIS%SEND_LOCAL_REMOTE_OK.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1739_x6365_934820463}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery]{lang="EN-US"}[状态机从]{style="font-family:宋体"}[PASSIVE_WAIT]{lang="EN-US"}[迁移到]{style="font-family:宋体"}[SEND_LOCAL_REMOTE_OK]{lang="EN-US"}*

[[\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Fsm: -MDC=1;]{lang="EN-US"}]{#struct_0_x1739_x6365_758026033}

[OAM Port GigabitEthernet1/0/1: Discovery state transfers from state DIS%SEND_LOCAL_REMOTE_OK to state DIS%SEND_ANY.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1739_x6365_x815309396}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Discovery]{lang="EN-US"}[状态机从]{style="font-family:宋体"}[SEND_LOCAL_REMOTE_OK]{lang="EN-US"}[迁移到]{style="font-family:宋体"}[SEND_ANY]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1739_x6365_x1755315582}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[功能，并打开该接口的以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging oam packet interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1739_x6365_299257804}

[\*Sep 22 17:22:30:428 2011 Sysname ETHOAM/7/Pkt: -MDC=1; Send OAM Packet via port GigabitEthernet1/0/1.]{lang="EN-US"}

[ Send Packet(Length: 46)]{lang="EN-US"}

[03 00 50 00 01 10 01 00 00 05 0d 05 dc 00 0f e2]{lang="EN-US"}

[00 00 00 00 02 10 01 00 00 02 0d 05 dc 00 0f e2]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1739_x6365_x788355205}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Sep 22 17:22:30:428 2011 Sysname ETHOAM/7/Pkt: -MDC=1; Receive OAM Packet via port GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_x1739_x6365_1899709099}

[ Rcvd Packet(Length: 46)]{lang="EN-US"}

[03 00 50 00 01 10 01 00 00 05 0d 05 dc 00 0f e2]{lang="EN-US"}

[00 00 00 00 02 10 01 00 00 02 0d 05 dc 00 0f e2]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1739_x6365_x1386004782}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到以太网]{style="font-family:宋体"}[OAM]{lang="EN-US"}[报文]{style="font-family:宋体"}*
