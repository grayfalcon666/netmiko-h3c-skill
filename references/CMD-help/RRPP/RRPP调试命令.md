<!-- CMD-INDEX
  debugging rrpp                      | 用户视图             | L5
-->

**RRPP \-- RRPP调试命令 \-- debugging rrpp**

------------------------------------------------------------------------

【命令】

**[debugging**]**rrpp** \**[domain***domain-id * **ring** *ring-id* ]  { **all** \| **error** \| **event** \| **fast-detect-fsm** \| **fast-detect-packet** \| **fsm** \| **packet** }

**[undo**]**debugging** **rrpp** \**[domain***domain-id * **ring** *ring-id* ]  { **all** \| **error** \| **event** \| **fast-detect-fsm** \| **fast-detect-packet** \| **fsm** \| **packet** }

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain***domain-id*]：指定RRPP域。*domain-id*为RRPP域的ID，取值范围为1～128。如果未指定本参数，表示所有RRPP域。

**[ring** *ring-id*]：指定RRPP环。*ring-id*为RRPP环的ID，取值范围为1～128。如果未指定本参数，表示所有RRPP环。

**[all**]：表示RRPP所有调试信息开关。

**[error**]：表示RRPP错误调试信息开关。

**[event**]：表示RRPP事件调试信息开关。

**[fast-detect-fsm**]：表示RRPP快速检测状态机调试信息开关。

**[fast-detect-packet**]：表示RRPP快速检测报文调试信息开关。

**[fsm**]：表示RRPP状态机调试信息开关。

**[packet**]：表示RRPP报文调试信息开关。

【描述】

**[debugging** **rrpp**]命令用来打开RRPP调试信息开关。**undo** **debugging** **rrpp**命令用来关闭RRPP调试信息开关。

缺省情况下，RRPP调试信息开关处于关闭状态。

表1-1 debugging rrpp error命令输出信息描述表

字段

描述

Failed to allocate memory.

表示申请动态内存失败

Failed to allocate memory for realtime backup.

表示HA实时备份分配内存失败

Failed to allocate memory for batch backup.

表示HA批量备份分配内存失败

Failed to send batch backup message.

表示HA发送批量备份消息失败

Failed to send realtime backup message.

表示HA发送实时备份消息失败

Domain *domain* ring *ring* port *port* : Master node received Health packet from primary port.

RRPP域*domain*下的环*ring*上的端口*port*收发报文错误，错误原因为主节点主端口收到本节点的Health报文

Received packet on port *port* error. Reason: *string*.

端口*port*收到错误报文，错误原因*string*包括：

·Illegal RRPP packet length：收到报文的长度字段非法

·Illegal RRPP version：收到报文的RRPP版本号非法

·Illegal RRPP PDU length：收到报文的PDU长度字段非法

·Illegal domain ID：收到报文的域ID非法

·Inexistent domain：收到报文携带的域ID在本设备上并未配置

·Ring is inactive：收到报文携带的域ID在本设备上已配置但未被激活，即该域下的环未被激活

·Illegal level：收到报文的级别非法

·Illegal RRPP packet：收到报文的报文类型非法

·Packet received from non-ctrlvlan：报文不是从指定域的控制VLAN收到的，即控制VLAN不匹配

·Illegal ring ID：收到报文的环ID非法

·Hello time out of range：报文中携带的Hello定时器超出范围

·Fail time out of range：报文中携带的Fail定时器超出范围

·Fail time must be greater than or equal to three times of Hello time：Fail定时器必须大于等于Hello定时器的三倍

·Level mismatch：报文中携带的环的级别与设备该环的级别不匹配

·A conflicting master node of current ring was detected：环上存在两个主节点（本条消息由主节点打印）

Received fast-detect packet packet error. Reason: *string*.

收到快速检测错误报文，错误原因*string*包括：

·Illegal domain ID：收到报文的域ID非法

·Inexistentdomain：收到报文携带的域ID不属于本设备上配置的域ID

·Illegal ring ID：收到报文的环ID非法

·Inexistent ring：收到报文携带的环ID不属于本设备上配置的对应域的环ID

·Illegal level：收到报文的级别非法

·Illegal PDU type：收到报文的报文类型非法

·Packet receives from non-ctrlvlan：报文不是从指定域的控制VLAN收到的，即控制VLAN不匹配

表1-2 debugging rrpp event命令输出信息描述表

字段

描述

Domain *domain* ring *ring* is activated/inactivated.

RRPP域*domain*下的环*ring*被激活/解除激活

Domain *domain* ring *ring* turns to fault for link down.

由于链路down，RRPP域*domain*下的环*ring*出现故障

Domain *domain* ring *ring* turns to fault for Link-Down packet.

由于收到Link-Down报文，RRPP域*domain*下的环*ring*出现故障

Domain *domain* ring *ring* turns to fault for fail-timer timeout.

由于主节点在Fail定时器超时前未收到自身的Health报文，RRPP域*domain*下的环*ring*出现故障

Domain *domain* ring *ring* recovered for Health packet.

主节点重新收到自身的Health报文，RRPP域*domain*下的环*ring*恢复健康

表1-3 debugging rrpp fast-detect-fsm命令输出信息描述表

字段

描述

Domain *domain* ring *ring* *string* FSM.

RRPP域*domain*下的环*ring*的*string*状态机信息，*string*包括：

·RX：表示接收状态机

·TX：表示发送状态机

·RXTX：表示同时为接收状态机和发送状态机

Previous/Current state is *state*.

状态机之前/当前的状态为*state*，包括Active、Completed、Failed和Idle

Transition event: event.

迁移条件为event，包括：

·Received Fast-Detect packet：从主端口或副端口收到快速检测报文

·FastFail-Timer-Expired：Fast-Fail定时器超时

·Detect-Enabled：使能快速检测

·Detect-Disabled：关闭快速检测

表1-4 debugging rrpp fast-detect-packet命令输出信息描述表

字段

描述

Domain *domain* ring *ring* received fast-detect packet. (Length: *length*, count: *count*) *string*

RRPP域*domain*下的环*ring*收到了快速检测报文报文，报文长度为*length*，报文计数为*count*，报文内容为*string*

Domain *domain* ring *ring* sent fast-detect packet. (Length: *length*, count: *count*) *string*

RRPP域*domain*下的环*ring*发送了快速检测报文报文，报文长度为*length*，报文计数为*count*，报文内容为*string*

表1-5 debugging rrpp fsm命令输出信息描述表

字段

描述

Domain *domain* ring *ring* *string* FSM.

RRPP域*domain*下的环*ring*的*string*状态机信息，*string*包括：

·Master Node：表示主节点状态机

·Transit Node：表示传输节点状态机

·Edge Node：表示边缘节点状态机

·Assistant-Edge Node：表示辅助边缘节点状态机

Previous/Current state is *state*.

状态机之前/当前的状态为*state*，包括：Completed、Failed、Init、Link-Up、Link-Down、Preforwarding、Link-Up-Notify、Link-Down-Notify、Preforward-Notify

Transition event: *event*.

迁移条件为*event*，包括：

·Ring-Enabled：环使能

·Ring-Disabled：环去使能

·Fail-Timer-Expired：Fail定时器超时

·EdgeFail-Timer-Expired：Edge-Fail定时器超时

·Received own Health packet：收到自己的Health报文

·Received Link-Down packet：收到Link-Down报文

·Received Common-Flush-FDB packet：收到Common-Flush-FDB报文

·Received Complete-Flush-FDB packet：收到Complete-Flush-FDB报文

·Received Sub-Ring-FDB packet：收到Sub-Ring-FDB报文

·Received Edge-Hello packet：收到Edge-Hello报文

·Received Major-Fault packet：收到Major-Fault报文

·Own link down：自身链路故障

·Own link restoring：自身链路恢复

·Port joined lagg：端口加入聚合

·Port leaved lagg：端口离开聚合

表1-6 debugging rrpp packet命令输出信息描述表

字段

描述

Port *port* received packet from domain *domain* ring *ring*. (Length: *length*, type: *type*) *string*

端口*port*从RRPP域*domain*下的环*ring*收到报文，报文长度为*length*，报文类型为*type*（取值为Health、Link-Down、Complete-Flush-FDB、Common-Flush-FDB、Edge-Hello或Major-Fault），报文内容为*string*

Port *port* sent packet to domain *domain* ring *ring*. (Length: *length*, type: *type*) *string*

端口*port*向RRPP域*domain*下的环*ring*发送报文，报文长度为*length*，报文类型为*type*（取值为Health、Link-Down、Complete-Flush-FDB、Common-Flush-FDB、Edge-Hello或Major-Fault），报文内容为*string*

【举例】

\# 在一个RRPP环上配置两个主节点，其它设备都配置成传输节点，所有设备的RRPP协议都使能，所有的环都使能。在其中一个主节点上打开RRPP异常信息调试信息开关。

\<Sysname\> debugging rrpp error

\*Jan 2 05:08:27:501 2012 Sysname RRPP/7/Error: -MDC=1; Received packet on port GigabitEthernet1/0/1 error. Reason: A conflicting master node of current ring was detected.

*// 端口GigabitEthernet1/0/1收到错误报文，错误原因为环上存在两个主节点*

\# 两台设备组网，设备A配置为主环传输节点，使能RRPP环不使能RRPP协议；设备B首先打开RRPP事件调试信息开关，然后配置为主环主节点，使能RRPP环和RRPP协议。

\<Sysname\> debugging rrpp event

\*May  2 23:48:18:579 2012 Sysname RRPP/7/Event: -MDC=1; Domain 1 ring 1 is activated.

*[// RRPP*]*域1下的环1被激活*

%May  2 23:52:47:650 2012 Sysname RRPP/7/Event: -MDC=1; Domain 1 ring 1 turns to fault for fail-timer timeout.

*// 由于主节点在Fail定时器超时前未收到自身的Health报文，RRPP域1下的环1出现故障*

\*Jan  2 05:29:35:393 2012 Sysname RRPP/7/Event: -MDC=1; Domain 1 ring 1 recovered for Health packet.

*// 使能设备A的RRPP协议，这时设备B就会打印环恢复事件*

\# 配置主环主节点，定时器使用缺省值，主端口是GigabitEthernet1/0/1，副端口是GigabitEthernet1/0/2。打开RRPP状态机调试信息开关。

\<Sysname\> debugging rrpp fsm

\*Jan  2 05:29:35:293 2012 Sysname RRPP/7/Fsm: -MDC=1; Domain 1 ring 1 Master Node FSM. Previous state is Failed. Current state is Completed. Transition event: Received Link-Down packet.

*// RRPP域1环1的主节点状态机信息。之前的状态为Failed，当前的状态为Completed，迁移条件为收到Link-Down报文*

\# 配置主环主节点，定时器使用缺省值，主端口是GigabitEthernet1/0/1，副端口是GigabitEthernet1/0/2。打开RRPP报文调试信息开关。

\<Sysname\> debugging rrpp packet

\*May  3 00:48:09:423 2012 Sysname RRPP/7/Pkt: -MDC=1; Port GigabitEthernet1/0/1 sent packet to domain 1 ring 1. (Length: 64, type: Health)

99 0b 00 40 01 05 00 01 00 01 00 00 00 00 00 00

01 11 00 01 00 03 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

*// 主端口GigabitEthernet1/0/1发送Health报文*

\*May  3 00:48:09:423 2012 Sysname RRPP/7/Pkt: -MDC=1; Port GigabitEthernet1/0/2 received packet from domain 1 ring 1. (Length: 64, type: Health)

99 0b 00 40 01 05 00 01 00 01 00 00 00 00 00 00

01 11 00 01 00 03 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

*// 副端口GigabitEthernet1/0/2收到本节点发出的Health报文*
