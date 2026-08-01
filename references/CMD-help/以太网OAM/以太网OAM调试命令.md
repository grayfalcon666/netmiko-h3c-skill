<!-- CMD-INDEX
  debugging oam                       | 用户视图             | L5
-->

**以太网OAM \-- 以太网OAM调试命令 \-- debugging oam**

------------------------------------------------------------------------

【命令】

**[debugging**[ **oam** { **all** \| **error** \| **event** \| **fsm** \| **packet** [ **receive** \| **send** ] }  **interface** *interface-type interface-number* ]]

**[undo**[ **debugging** **oam** { **all** \| **error** \| **event** \| **fsm** \| **packet** [ **receive** \| **send** ] }  **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示以太网OAM的所有调试信息开关。

**[event**]：表示以太网OAM事件调试信息开关。

**[error**]：表示以太网OAM错误调试信息开关。

**[fsm**]：表示以太网OAM状态机调试信息开关。

**[packet**]：表示以太网OAM报文调试信息开关。

**[receive**]：表示接收的以太网OAM报文调试信息开关。

**[send**]：表示发送的以太网OAM报文调试信息开关。

**[interface** *interface-type interface-number*]：表示指定接口，*interface-type interface-number*为接口类型和接口编号。如果未指定本参数，表示所有接口。

【描述】

**[debugging** **oam**]命令用来打开以太网OAM调试信息开关。**undo** **debugging** **oam**命令用来关闭以太网OAM调试信息开关。

缺省情况下，以太网OAM调试信息开关处于关闭状态。

需要注意的是，如果不输入**send**和**receive**参数，则同时显示发送和接收的以太网OAM报文调试信息。

表1-1 debugging oam event命令输出信息描述表

字段

描述

OAM Port *port*: *event*

以太网OAM接口*port*上发生了*event*事件

表1-2 debugging oam error命令输出信息描述表

字段

描述

OAM Port *port*: *error*

以太网OAM接口*port*在运行中发生了*error*错误

表1-3 debugging oam fsm命令输出信息描述表

字段

描述

OAM Port *port*: Discovery state transfers from state *state1* to state *state2*

以太网OAM接口*port*的Discovery状态机从*state1*迁移到*state2*

OAM Port *port*: Remote loopback state transfers from state *state1* to state *state2*

以太网OAM接口*port*的Loopback状态机从*state1*迁移到*state2*

表1-4 debugging oam packet命令输出信息描述表

字段

描述

Send/Receive OAM Packet Via Port *port*

接口*port*发送/收到了以太网OAM报文

Pkt length

报文长度

【举例】

\# 在接口GigabitEthernet1/0/1上使能以太网OAM功能，并打开该接口的以太网OAM事件调试信息开关，然后拔掉网线。

\<Sysname\> debugging oam event interface gigabitethernet 1/0/1

\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Event: -MDC=1;

OAM Port GigabitEthernet1/0/1: occurs link down event.

*// 接口GigabitEthernet1/0/1上发生了down事件*

\# 在接口GigabitEthernet1/0/1上使能以太网OAM功能，并打开该接口的以太网OAM错误调试信息开关。

\<Sysname\> debugging oam error interface gigabitethernet 1/0/1

\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Error: -MDC=1;

OAM Port gigabitethernet 1/0/1: Failed to enable or disable packet to CPU.

*// 在接口GigabitEthernet1/0/1上使能以太网OAM失败*

\# 在接口GigabitEthernet1/0/1上使能以太网OAM功能，并打开该接口的以太网OAM状态机调试信息开关。

\<Sysname\> debugging oam fsm interface gigabitethernet 1/0/1

\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Fsm: -MDC=1;

OAM Port GigabitEthernet1/0/1: Discovery state transfers from state DIS%FAULT to state DIS%PASSIVE_WAIT.

*// 接口GigabitEthernet1/0/1的Discovery状态机从FAULT迁移到PASSIVE_WAIT*

\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Fsm: -MDC=1;

OAM Port GigabitEthernet1/0/1: Discovery state transfers from state DIS%PASSIVE_WAIT to state DIS%SEND_LOCAL_REMOTE_OK.

*// 接口GigabitEthernet1/0/1的Discovery状态机从PASSIVE_WAIT迁移到SEND_LOCAL_REMOTE_OK*

\*Apr 26 15:12:33:211 2011 Sysname ETHOAM/7/Fsm: -MDC=1;

OAM Port GigabitEthernet1/0/1: Discovery state transfers from state DIS%SEND_LOCAL_REMOTE_OK to state DIS%SEND_ANY.

*// 接口GigabitEthernet1/0/1的Discovery状态机从SEND_LOCAL_REMOTE_OK迁移到SEND_ANY*

\# 在接口GigabitEthernet1/0/1上使能以太网OAM功能，并打开该接口的以太网OAM报文调试信息开关。

\<Sysname\> debugging oam packet interface gigabitethernet 1/0/1

\*Sep 22 17:22:30:428 2011 Sysname ETHOAM/7/Pkt: -MDC=1; Send OAM Packet via port GigabitEthernet1/0/1.

 Send Packet(Length: 46)

03 00 50 00 01 10 01 00 00 05 0d 05 dc 00 0f e2

00 00 00 00 02 10 01 00 00 02 0d 05 dc 00 0f e2

00 00 00 00 00 00 00 00 00 00 00 00 00 00

*// 从接口GigabitEthernet1/0/1发送以太网OAM报文*

\*Sep 22 17:22:30:428 2011 Sysname ETHOAM/7/Pkt: -MDC=1; Receive OAM Packet via port GigabitEthernet1/0/1.

 Rcvd Packet(Length: 46)

03 00 50 00 01 10 01 00 00 05 0d 05 dc 00 0f e2

00 00 00 00 02 10 01 00 00 02 0d 05 dc 00 0f e2

00 00 00 00 00 00 00 00 00 00 00 00 00 00

*// 从接口GigabitEthernet1/0/1收到以太网OAM报文*
