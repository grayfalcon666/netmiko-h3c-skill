
**Smart Link \-- Smart Link调试命令 \-- debugging smart-link**

------------------------------------------------------------------------

【命令】

**[debugging smart-link** [ **group** *group-id*  { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

**[undo debugging smart-link** [ **group** *group-id*  { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group*** group-id*]：表示指定Smart Link组的调试信息开关。如果未指定本参数，则表示所有Smart Link组的调试信息开关。

**[all**]：表示Smart Link组的所有调试信息开关。

**[error**]：表示Smart Link组错误调试信息开关。

**[event**]：表示Smart Link组事件调试信息开关。

**[fsm**]：表示Smart Link组状态机调试信息开关。

**[packet**]：表示Smart Link组报文调试信息开关。

【描述】

**[debugging smart-link**]命令用来打开Smart Link组调试信息开关。**undo debugging smart-link**命令用来关闭Smart Link组调试信息开关。

缺省情况下，Smart Link组调试信息开关处于关闭状态。

表1-1 debugging smart-link error命令输出信息描述表

字段

描述

Failed to allocate memory for *String*

分配内存失败。*String*表示为该操作分配内存时发生失败，包括：

·batch bak：表示批量备份

·realtime bak：表示实时备份

·create group：表示创建Smart Link组

·smart link port info：表示Smart Link端口信息

Failed to send *String* backup message

发送备份消息失败。*String*表示为该操作发送备份消息时发生失败，包括：

·batch：表示发送批量备份消息

·realtime：表示发送实时备份消息

Port *PortName:* Received error packet because *String*

端口*PortName*接收了错误的Flush报文。*String*表示错误原因，包括：

·length of smart link PDU is illegal：表示报文长度非法

·control type is illegal：表示控制类型非法

·control version is illegal：表示控制版本非法

·control VLAN is illegal：表示控制VLAN非法

·control VLAN is different：表示报文发送控制VLAN与配置的接收控制VLAN不同

Smart link group *group-id*: Failed to check control VLAN

Smart Link组*group-id*的控制VLAN不存在或者端口不允许其VLAN通过

表1-2 debugging smart-link event命令输出信息描述表

字段

描述

Smart link group *group-id* *PortName*: Deleting MAC and updating ARP on the port

删除Smart Link组*group-id*的端口*PortName*上的MAC地址转发表项并更新ARP/ND表项

Deleting MAC and updating ARP on the device

删除设备上所有端口的MAC地址转发表项并更新ARP/ND表项

Smart link group *group-id* *PortName*: Link status is up/down

Smart Link组*group-id*的端口*PortName*的链路状态变为up或down

表1-3 debugging smart-link fsm命令输出信息描述表

字段

描述

Smart link group *group-id* port *PortName*: *String*

Smart Link组*group-id*的端口*PortName*上的状态机事件。*String*表示事件，包括：

·State preempts to be active/standby：表示状态抢占为active或standby

·State doesn\'t change：表示状态没有改变

·State changes to active/standby：表示状态变为active或standby

·Delay timer starts/expires/ends：表示延时定时器启动、超时或停止

表1-4 debugging smart-link packet命令输出信息描述表

字段

描述

Smart link group *group-id* sent packet

Smart Link组*group-id*发送Flush报文

Port *PortName*: Sent flush packet

端口*PortName*发送Flush报文

Port *PortName*: Received flush packet

端口*PortName*接收Flush报文

Device ID

设备标识

Control VLAN

控制VLAN的编号

VLAN bit map

VLAN位图，表示Smart Link组中阻塞端口允许通过的VLAN列表

【举例】

\# 在一台开启接收Flush报文功能的设备上打开Smart Link组错误调试信息开关。

\<Sysname\> debugging smart-link error

\*Apr  6 15:06:18:017 2012 Sysname SMLK/7/Pkt: -MDC=1; Port GigabitEthernet1/0/1: Received error packet because control VLAN is different.

*// 端口GigabitEthernet1/0/1接收了错误的Flush报文，原因为报文发送控制VLAN与配置的接收控制VLAN不同*

\# 打开Smart Link组1的状态机调试信息开关。

\<Sysname\> debugging smart-link group 1 fsm

\*Apr  6 15:27:25:734 2012 Sysname SMLK/7/Fsm: -MDC=1; Smart link group 1 port GigabitEthernet1/0/1: State changes to active.

*// 端口GigabitEthernet1/0/1成为Smart Link组1的主端口*

\*Apr  6 15:29:45:910 2012 Sysname SMLK/7/Fsm: -MDC=1; Smart link group 1 port GigabitEthernet1/0/2: State changes to standby.

*// 端口GigabitEthernet1/0/2成为Smart Link组1的从端口*

\# 打开Smart Link组1的报文调试信息开关，并对Smart Link组1进行链路切换。

\<Sysname\> debugging smart-link group 1 packet

\*Apr  6 15:45:25:641 2012 Sysname SMLK/7/Pkt: -MDC=1;

Smart link group 1:

Port GigabitEthernet1/0/1: Sent flush packet

*// 端口GigabitEthernet1/0/1发送Flush报文*

Device ID: 0011-2200-0301

*// 设备标识为0011-2200-0301*

Control VLAN: 1

*// 控制VLAN为VLAN 1*

VLAN bit map:

02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

\*Apr  6 15:45:27:629 2012 Sysname SMLK/7/Pkt:

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

*[// VLAN*]*位图的具体内容*
