<!-- CMD-INDEX
  debugging cfd                       | ]                | L5
-->

**CFD \-- CFD调试命令 \-- debugging cfd**

------------------------------------------------------------------------

【命令】

**[debugging cfd** **[ais-track** **link-status** **packet** [ **level** *level-value*  \| **all** \| **event** \| **fsm** [ **ais** \| { **cci** \| **fng** \| **lbi** \| **mcc** \| **mme** \| **rmep** } [ **interface** *interface-type interface-number* ] \| **packet** [ **receive** \| **send** ]  **interface** *interface-type interface-number*  \| **timer** }]]

**[undo debugging cfd** **[ais-track** **link-status** **packet** [ **level** *level-value*  \| **all** \| **event** \| **fsm** [ **ais** \| { **cci** \| **fng** \| **lbi** \| **mcc** \| **mme** \| **rmep** } [ **interface** *interface-type interface-number* ] \| **packet** [ **receive** \| **send** ]  **interface** *interface-type interface-number*  \| **timer** }]]

【视图】]

用户视图]

【缺省用户角色】]

network-admin]

mdc-admin

【参数】

**[ais-track** **link-status** **packet**]：表示CFD以太网告警指示信号报文调试信息开关。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[level** *level-value*]：表示指定级别EAIS报文的调试信息开关，*level-value*的取值范围为0～7。如果未指定本参数，表示所有级别EAIS报文的调试信息开关。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：表示CFD的所有调试信息开关。

**[event**]：表示CFD事件调试信息开关。

**[fsm**]：表示CFD状态机调试信息开关。

**[ais**]：表示CFD告警指示信号状态机调试信息开关。

**[cci**]：表示CFD连通性检测状态机调试信息开关。

**[fng**]：表示CFD错误报警状态机调试信息开关。

**[lbi**]：表示CFD环回状态机调试信息开关。

**[mcc**]：表示CFD交叉连接CCM状态机调试信息开关。

**[mme**]：表示CFD错误CCM状态机调试信息开关。

**[rmep**]：表示CFD远端MEP状态机调试信息开关。

**[packet**]：表示CFD报文调试信息开关。

**[receive**]：表示接收的CFD报文调试信息开关。

**[send**]：表示发送的CFD报文调试信息开关。

**[interface*** interface-type interface-number*]：表示指定接口的调试信息开关。如果未指定本参数，表示所有接口的调试信息开关。

**[timer**]：表示CFD定时器调试信息开关。

【描述】

**[debugging cfd**]命令用来打开CFD调试信息开关。**undo debugging cfd**命令用来关闭CFD调试信息开关。

缺省情况下，CFD调试信息开关处于关闭状态。

需要注意的是：

·当未指定**send**和**receive**参数时，表示同时打开或关闭CFD报文的发送和接收调试信息开关。

·当指定了**fsm**参数而未指定**ais**、**cci**、**fng**、**lbi**、**mcc**、**mme**和**rmep**参数时，表示打开或关闭CFD所有的状态机调试信息开关。

·如果在接口上配置的是内向MEP，由于内向MEP对报文处理的特殊性，在打开接口上发送CFD报文的调试信息开关时，只会输出CCM报文，而不会输出LT和LB报文；打开接口上接收CFD报文调试信息开关时，CCM、LT和LB报文都不会输出，如果想看到所有报文，可以打开所有接口收发CFD报文的调试信息开关。

·对于开启了硬件检测功能的MEP，打开CFD报文调试信息开关后，不会输出其CCM报文的调试信息。

·如果设备上有辅助CPU，所有发送的CCM报文调试信息都不会输出，接收的高速CCM报文会抽样输出，接收的低速CCM报文则正常输出。

表1-1 debugging cfd ais-track link-status packet命令输出信息描述表

字段

描述

Send EAIS Packet

发送EAIS报文

Packet Length

报文长度

Level

EAIS报文的发送级别

Period

EAIS报文的发送周期

表1-2 debugging cfd event命令输出信息描述表

字段

描述

CFD processes create/delete port *port-name* event

CFD响应创建/删除接口*port-name*的事件

CFD processes port *port-name* up/down event

CFD响应接口*port-name*的up/down事件

CFD processes port *port-name* active/deactive event

CFD响应接口*port-name*的激活/去激活事件

CFD processes port *port-name* aggregation(leave) event

CFD响应接口*port-name*的加入（退出）聚合组事件

CFD responds to add port *port-name* to vlan 1

CFD响应接口*port-name*加入VLAN事件

CFD responds to delete port *port-name* from vlan 1

CFD响应接口*port-name*退出VLAN事件

表1-3 debugging cfd fsm命令输出信息描述表

字段

描述

AIS

告警指示信号状态机

CCI

连通性检测状态机

FNG

错误报警状态机

LBI

环回状态机

MCC

交叉连接CCM状态机

MME

错误CCM状态机

RMEP

远端MEP状态机

FSM

状态机

Port

MEP所在的接口

SI

MEP所在的服务实例

MEP

配置的MEP

State machine:*State-machine*

当前状态机为*State-machine*

Prestate:*State-machine*

状态机变迁前的状态为*State-machine*

Curstate:*State-machine*

状态机的当前状态为*State-machine*

表1-4 debugging cfd packet命令输出信息描述表

字段

描述

*[port-name*]/*port-index* send/recv

设备通过接口*port-name*/*port-index*发送/接收了一个CFD报文

Pkt length

报文长度

表1-5 debugging cfd timer命令输出信息描述表

字段

描述

Service-instance

MEP所在的服务实例

MEP

配置的MEP

Operation

定时器的操作，包括create、delete和refresh

FNG

错误报警状态机

LBI

环回状态机

Xcon Ccm

交叉连接CCM状态机

Err Ccm

错误CCM状态机

RMEP

远端MEP状态机

LTM

链路跟踪状态机

AutoLtm

自动发送链路跟踪报文状态机

AIS

告警指示信号

【举例】

\# 打开CFD以太网告警指示信号报文调试信息开关，使能端口状态与AIS联动功能并配置好EAIS报文的发送级别和周期。

\<Sysname\> debugging cfd ais-track link-status packet

\*Feb  2 14:55:27:492 2013 Sysname EAIS/7/PACKET: -MDC=1;

Send EAIS Packet:

20 21 04 00 00

Packet Length: 5    Level: 1    Period: 1s

*// 发送一个级别为1、周期为1秒的EAIS报文*

\# 在设备上启动CFD功能并配置相应MD、MA、服务实例和MEP。打开CFD告警指示信号状态机调试信息开关，使能告警抑制功能并配置相应的级别和周期。

\<Sysname\> debugging cfd fsm ais

\*Jul  3 10:26:51:743 2013 Sysname CFD/7/FSM: -MDC=1;

AIS: Service instance: 1,MEP: 1, PreState: IDLE, CurState: NO_RECEIVE

*[// CFD*]*中的AIS状态机发生迁移，该状态机前一状态为IDLE，当前状态为NO_RECEIVE*

\# 在设备上启动CFD功能并配置相应MD、MA、MEP。打开CFD连通性检测状态机调试信息开关。使能配置的MEP，并使能该MEP的CC功能。

\<Sysname\> debugging cfd fsm cci

\*Mar 29 09:20:54:037 2011 Sysname CFD/7/FSM: -MDC=1;

CCI: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate:CCI_IDLE Curstate:CCI_WAITING

*[// CFD*]*中的CCI状态机发生迁移，该状态机前一状态为CCI_IDLE，当前状态为CCI_WAITING*

\# 在设备上启动CFD功能并配置相应MD、MA、MEP。打开CFD错误CCM状态机调试信息开关。该设备上的MEP收到了其它设备发来的错误CCM报文。

\<Sysname\> debugging cfd fsm mme

\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;

MME: GigabitEthernet1/0/1 Service-instance:1 mep:1

Prestate:ERRCCM_NO_DEFECT Curstate:ERRCCM_DEFECT

*[// CFD*]*中的MME状态机发生迁移，该状态机前一状态为ERRCCM_NO_DEFECT，当前状态为ERRCCM_DEFECT*

\# 在设备上启动CFD功能并配置相应MD、MA、MEP。打开CFD交叉连接CCM状态机调试信息开关。该设备上的MEP收到了其它设备发来的交叉连接CCM报文。

\<Sysname\> debugging cfd fsm mcc

\*Mar 29 15:30:56:056 2011 Sysname CFD/7/FSM: -MDC=1;

MCC: GigabitEthernet1/0/1 Service-instance:1 mep:1

Prestate:XCON_NO_DEFECT Curstate:XCON_DEFECT

*[// CFD*]*中的MME状态机发生迁移，该状态机前一状态为XCON_NO_DEFECT，当前状态为XCON_DEFECT*

\# 在设备上启动CFD功能并配置相应MD、MA、MEP。打开CFD交叉连接CCM状态机调试信息开关。该设备上的MEP收到了其它设备发来的交叉连接CCM报文。

\<Sysname\> debugging cfd fsm mcc

\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;

MCC: GigabitEthernet1/0/1 Service-instance:2 mep:3

Prestate:XCON_NO_DEFECT Curstate:XCON_DEFECT

*[// CFD*]*中的MME状态机发生迁移，该状态机前一状态为XCON_NO_DEFECT，当前状态为XCON_DEFECT*

\# 在设备上启动CFD功能并配置相应MD、MA、MEP。打开CFD RMEP状态机调试信息开关。该设备上的MEP在3.5个报文周期内没有收到了远端设备发来的CCM报文。

\<Sysname\> debugging cfd fsm rmep

\*Mar 29 15:40:45:967 2011 Sysname CFD/7/FSM: -MDC=1;

RMEP: GigabitEthernet1/0/1 Service-instance:2 mep:3

Prestate: RMEP_OK Curstate: RMEP_FAILED

*[// CFD*]*中的RMEP状态机发生迁移，该状态机前一状态为RMEP_OK，当前状态为RMEP_FAILED*

\# 在设备上启动CFD功能并配置相应MD、MA、MEP。打开CFD错误报警状态机调试信息开关。

\<Sysname\> debugging cfd fsm mme

\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;

FNG: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate: FNG_RESET Curstate: FNG_DEFECT

\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;

FNG: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate:FNG_DEFECT Curstate: FNG_DEFECT_REPORT

\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;

FNG: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate: FNG_DEFECT_REPORT Curstate: FNG_DEFECT_REPORTED

*[// CFD*]*中的FNG状态机发生迁移*

\# 在设备上启动CFD功能并配置相应MD、MA、MEP。打开CFD LBI报文状态机调试信息开关。

\<Sysname\> debugging cfd fsm lbi

\*Mar 29 15:30:56:161 2011 Sysname CFD/7/FSM: -MDC=1;

LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_IDLE Curstate: LBI_STARTING

\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM: -MDC=1;

LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_STARTING Curstate: LBI_TRANSMITTING

\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM: -MDC=1;

LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_TRANSMITTING Curstate: LBI_TRANSMIT

\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM: -MDC=1;

LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_TRANSMIT Curstate: LBI_TRANSMITTING

\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM:

LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_TRANSMITTING Curstate: LBI_WAITING

*[// CFD*]*中的LBI状态机发生迁移*

\# 在设备上配置等级为0的MD和服务实例，在接口GigabitEthernet1/0/1上配置MEP ID为100的外向MEP。打开CFD协议报文的调试信息开关。启动CFD服务和CCM发送，并通过命令向远端配置的MEP发送LTM和LBM报文。

\<Sysname\> debugging cfd packet

\*Mar 29 15:38:32:663 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 01 05 36 00 00 00 3a 00 02 04 03 6d 64 31 02

03 6d 61 31 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 01 00 02 00 00 02

00 01 02 04 00 01 01 00 00 00 00 00 00 00 00 00

00 00 00

Pkt length: 83

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的01可知是一个CCM报文*

\*Mar 29 15:38:32:630 2011 Sysname CCM/7/PACKET: -MDC=1; Interface 148 recv:

20 01 05 36 00 00 00 3a 00 02 04 03 6d 64 31 02

03 6d 61 31 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 01 00 02 00 00 02

00 01 02 04 00 01 01 00 00 00 00 00 00 00 00 00

00 00 00

Pkt length: 83

*// 通过索引号为148的接口发送了一个CFD报文，由该报文开头的01可知是一个CCM报文*

\*Mar 29 15:50:40:575 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 recv:

20 05 00 11 00 02 00 01 09 00 11 22 33 44 01 00

11 22 33 44 01 07 00 08 00 00 00 11 22 33 44 01

00 00 00 00 00 00 00 00 00 00

Pkt length: 42

*// 通过接口GigabitEthernet1/0/1收到了一个CFD报文，由该报文开头的05可知是一个LTM报文*

\*Mar 29 15:42:14:245 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 04 00 06 00 02 00 00 07 01 08 00 10 00 00 00

11 22 33 44 01 00 00 00 00 00 00 00 00 05 00 0a

01 00 11 22 33 44 01 00 00 00 06 00 0a 01 00 11

22 33 44 01 00 00 00 01 00 02 00 00 00 00 00 00

00 00 00 00 00 00 00 00

Pkt length: 72

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的04可知是一个LTR报文*

\*Mar 29 09:37:28:452 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 03 00 04 00 02 00 00 01 00 02 00 00 03 00 02

00 00 1f 00 05 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00

Pkt length: 40

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的03可知是一个LBM报文*

\*Mar 29 15:33:35:563 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 recv:

20 02 00 04 00 01 00 01 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00

Pkt length: 42

*// 通过接口GigabitEthernet1/0/1接收了一个CFD报文，由该报文开头的02可知是一个LBR报文*

\*Feb  2 15:56:30:370 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 21 04 00 00

Pkt length：5

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的21可知是一个AIS报文*

\*Feb  2 15:50:19:800 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 2d 00 10 51 4b 3b 15 09 64 e0 70 00 00 00 00

00 00 00 00 00

Pkt length: 21

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的2d可知是一个1DM报文*

\*Feb  2 15:50:30:370 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 2f 00 20 51 4b 3b b9 2d 28 26 70 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00

Pkt length: 37

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的2f可知是一个DMM报文*

\*Feb  2 15:51:30:450 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 receive:

20 2e 00 20 51 4b 3d b3 2d 28 26 70 51 48 70 d5

0f a9 43 18 51 48 70 d5 0f a9 43 18 00 00 00 00

00 00 00 00 00 00 00 00 00 00

Pkt length: 42

*// 通过接口GigabitEthernet1/0/1接收了一个CFD报文，由该报文开头的2e可知是一个DMR报文*

\*Feb  2 15:52:30:830 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 25 00 04 00 00 00 09 20 00 41 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00

Pkt length: 77

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的25可知是一个TST报文*

\*Feb  2 16:07:33:830 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:

20 2b 00 0c 00 00 00 00 00 00 00 00 00 00 00 00

00

Pkt length: 17

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的2b可知是一个LMM报文*

\*Feb  2 16:07:34:450 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 receive:

20 2a 00 0c 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00

Pkt length: 42

*// 通过接口GigabitEthernet1/0/1发送了一个CFD报文，由该报文开头的2a可知是一个LMR报文*
