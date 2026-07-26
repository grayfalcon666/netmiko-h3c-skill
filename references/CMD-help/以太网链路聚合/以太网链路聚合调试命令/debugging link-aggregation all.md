
**以太网链路聚合 \-- 以太网链路聚合调试命令 \-- debugging link-aggregation all**

------------------------------------------------------------------------

【命令】

**[debugging link-aggregation all**]

**[undo debugging link-aggregation all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging link-aggregation all**]命令用来打开链路聚合的所有调试信息开关。**undo debugging link-aggregation all**命令用来关闭链路聚合的所有调试信息开关。

缺省情况下，链路聚合的所有调试信息开关均处于关闭状态。

**以太网链路聚合 \-- 以太网链路聚合调试命令 \-- debugging link-aggregation error**

------------------------------------------------------------------------

【命令】

**[debugging link-aggregation error**]

**[undo debugging link-aggregation error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging link-aggregation error**]命令用来打开链路聚合错误调试信息开关。**undo debugging link-aggregation error**命令用来关闭链路聚合错误调试信息开关。

缺省情况下，链路聚合错误调试信息开关处于关闭状态。

表1-1 debugging link-aggregation error命令输出信息描述表

字段

描述

Failed to get the group state.

获取聚合组状态失败

Failed to update the system priority.

更新系统优先级失败

Failed to set the hash key.

设置负载分担类型失败

Failed to set the hash key mode for group %u, because the mode is not supported.

设置聚合组%u的负载分担类型失败，系统不支持该类型

Failed to set the hash key mode for group %u.

设置聚合组%u的负载分担类型失败

Calculation failed because of a logic selection failure.

因为逻辑口的选择失败导致计算失败

Failed to notify to clear statistics.

上报清除统计信息失败

%x %s LACP packet failed: Fail to send a packet.

接口索引%x上收发报文失败：发送报文失败

%x %s LACP packet failed: Fail to receive a packet.

接口索引%x上收发报文失败：接收报文失败

%x %s LACP packet failed: Invalid packet type.

接口索引%x上收发报文失败：无效的报文类型

%x %s LACP packet failed: Invalid packet length.

接口索引%x上收发报文失败：无效的报文长度

%x %s LACP packet failed: Invalid packet version.

接口索引%x上收发报文失败：无效的版本号

%x %s LACP packet failed: Invalid actor info in the packet.

接口索引%x上收发报文失败：无效的本端信息

%x %s LACP packet failed: Invalid partner info in the packet.

接口索引%x上收发报文失败：无效的对端信息

%x %s LACP packet failed: Invalid collector info in the packet.

接口索引%x上收发报文失败：无效的Collector信息

%x %s LACP packet failed: Invalid terminator info in the packet.

接口索引%x上收发报文失败：无效的Terminator信息

%x %s LACP packet failed: Self-loop packet.

接口索引%x上收发报文失败：自环报文

%x %s LACP packet failed: Incorrect system MAC address.

接口索引%x上收发报文失败：无效的系统MAC

%x %s LACP packet failed: Failed to get the port address.

接口索引%x上收发报文失败：获取端口地址失败

%x %s LACP packet failed: Failed to send LACP packets through *PAIndex*.

接口索引%x上收发报文失败：通过聚合接口发送LACP报文失败

Failed to get statistics.

获取统计信息失败

Failed to get the statistics of the group.

获取聚合组统计信息失败

Failed to clear the statistics of the group.

清除聚合组统计信息失败

Failed to send the packet to the partner.

发送报文给对端失败

【举例】

\# 打开链路聚合错误调试信息开关，查看系统运行过程中出现的错误提示信息。

\<Sysname\> debugging link-aggregation error

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 link-aggregation load-sharing mode ingress-port

\*Jan  2 15:22:35:929 2010 Sysname LAGG/7/Error: Failed to set the hash key mode for group 1, because the mode is not supported.

*// 设置聚合组1的负载分担类型失败，系统不支持该类型*

**以太网链路聚合 \-- 以太网链路聚合调试命令 \-- debugging link-aggregation event**

------------------------------------------------------------------------

【命令】

**[debugging link-aggregation event**]

**[undo debugging link-aggregation event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging link-aggregation event**]命令用来打开链路聚合事件调试信息开关。**undo debugging link-aggregation event**命令用来关闭链路聚合事件调试信息开关。

缺省情况下，链路聚合事件调试信息开关处于关闭状态。

表1-2 debugging link-aggregation event命令输出信息描述表

字段

描述

The hash key mode successfully set for group %u.

设置聚合组%u的负载分担类型成功

The maximum number of selected port in group %u successfully set to %u.

聚合组%u的最大选中端口数被成功设置为%u

The minimum number of selected port in group %u successfully set to %u.

聚合组%u的最小选中端口数被成功的设置为%u

Group %u updated because of %s.

聚合组%u因为%s被更新

MAD conflict is detected by LACP, member %s should be recovered

LACP检测到MAD冲突，成员%s需要被禁用

【举例】

\# 打开链路聚合事件调试信息开关，开启端口GigabitEthernet1/0/1，并更改聚合组配置。

\<Sysname\> debugging link-aggregation event

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo shutdown

\* Jun  5 10:49:06:039 2013 Sysname LAGG/7/Event:  Group 1 updated because of partner port other reason.

*// 由于成员端口对端的其他信息变化而更新聚合组1*

Sysname-GigabitEthernet1/0/1 quit

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 port hybrid vlan 2 to 4094 tagged

\*Jun  5 10:49:06:127 2013 Sysname LAGG/7/Event: -MDC=1; Group 1 updated because of aggregation interface configuration change.

*// 由于聚合接口的配置信息变化而更新聚合组1*

**以太网链路聚合 \-- 以太网链路聚合调试命令 \-- debugging link-aggregation lacp fsm**

------------------------------------------------------------------------

【命令】

**[debugging link-aggregation lacp fsm**[ { { **actorchurn** \| **mux** \| **partnerchurn** \| **ptx** \| **rx** } \* \| **all** } [ *interface-list* ]]]

**[undo debugging link-aggregation lacp fsm**[ { { **actorchurn** \| **mux** \| **partnerchurn** \| **ptx** \| **rx** } \* \| **all** } [ *interface-list* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[actorchurn**]：表示Actor-churn状态机调试信息开关。

**[mux**]：表示MUX状态机调试信息开关。

**[partnerchurn**]：表示Partner-churn状态机调试信息开关。

**[ptx**]：表示PTX状态机调试信息开关。

**[rx**]：表示RX状态机调试信息开关。

**[all**]：表示所有状态机调试信息开关。

*[interface-list*]：以太网端口列表。表示方式为*interface-list* = *interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type*为接口类型，*interface-number*为接口编号。若未指定此参数，则表示对所有运行LACP协议的端口都生效。

【描述】

**[debugging link-aggregation lacp fsm**]命令用来打开端口的LACP协议状态机调试信息开关。**undo** **debugging link-aggregation lacp fsm**命令用来关闭端口的LACP协议状态机调试信息开关。

缺省情况下，端口的LACP协议状态机调试信息开关处于关闭状态。

表1-3 debugging link-aggregation lacp fsm命令输出信息描述表

字段

描述

*[state1*\--\>*state2*]

状态机由*state1*迁移到*state2*情况，所有可能出现的状态及其解释如下：

·BEGIN：状态机为已创建但未激发状态

·INITIALIZE：初始化RX状态机完毕状态

·PORT_DISABLED：RX状态机为端口非选中，未同步状态

·EXPIRED：RX状态机为超时状态，启动接收超时定时器

·DEFAULTED：RX状态机为默认状态，激励选择算法重新计算该组状态

·LACP_DISABLED：RX状态机为对端协议未使能状态，设置端口为非选中，清除对端信息，并将对端信息记录为默认值

·CURRENT：RX状态机为就绪状态，解析接收到的LACP协议报文，记录报文信息，并根据对端信息是否有变化进行相应的处理

·NO_PERIODIC：PTX状态机为非周期性发送LACP协议报文状态

·FAST_PERIODIC：PTX状态机为快速周期性发送LACP协议报文状态，周期为1秒

·SLOW_PERIODIC：PTX状态机为慢速周期性发送LACP协议报文状态，周期为30秒

·PERIODIC_TX：PTX状态机为周期性发送LACP协议报文状态

·DETACHED：阻塞端口，发送LACP协议报文

·WAITING：MUX状态机为等侍延迟状态

·ATTACHED：阻塞端口，发送LACP协议报文

·COLLECTING_DISTRIBUTING：取消端口阻塞，发送LACP协议报文

·NO_ACTOR_CHURN：本端处于非Churn状态

·ACTOR_CHURN：本端处于Churn状态

·ACTOR_CHURN_MONITOR：启动Churn定时器，记录本端处于非Churn状态

·NO_PARTNER_CHURN：对端非Churn

·PARTNER_CHURN：对端处于Churn状态

·PARTNER_CHURN_MONITOR：对端非Churn

*[conditions*]

引发状态机迁移的条件，包括以下条件：

·Begin_False：状态机已启动

·Begin_True：状态机启动

·UCT：无条件转移

·Port_Moved_True：端口发生Port Move事件

·Port_Moved_False：端口Port Move事件处理完成

·Port_Enabled：端口可用

·Port_Disabled：端口不可用

·LACP_Enabled：端口使能LACP

·LACP_Disabled：端口去使能LACP

·PDU_Indicate：收到LACP协议报文

·CurrentWaitTimer_Expired：CURRENT定时器超时

·LACP_Passive：双方都是Passive模式

·PeriodTimer_Expired：周期定时器超时

·Long_Timeout：LACP信息长超时

·Short_Timeout：LACP信息短超时

·Selected：端口为SELECTED状态

·Unselected：端口为UNSELECTED状态

·Actor_Insync：本端协议信息同步

·Actor_Outsync：本端协议信息未同步

·Partner_Insync：对端协议信息同步

·Partner_Outsync：对端协议信息未同步

·ActorChurnTimer_Expired：ACTORCHURN定时器超时

·PartnerChurnTimer_Expired：PARTNERCHURN定时器超时

·NTT_True：需要发送LACPDU

【举例】

\# 将端口GigabitEthernet1/0/2加入到动态聚合组中，打开端口GigabitEthernet1/0/2的LACP协议状态机调试信息开关，在设备上查看端口的状态机迁移状况。

\<Sysname\> debugging link-aggregation lacp fsm rx interface gigabitethernet 1/0/2

\*Nov  5 10:33:32:828 2007 Sysname LAGG/7/Fsm: GigabitEthernet1/0/2 FSM.RX BEGIN\--\>INITIALIZE, Begin_True

\*Nov  5 10:33:32:829 2007 Sysname LAGG/7/Fsm: GigabitEthernet1/0/2 FSM.RX INITIALIZE\--\>PORT_DISABLED, UCT

*[// RX*]*状态机初始化，进入到LACP去使能状态，迁移条件为状态机启动*

\*Nov  5 10:33:32:830 2007 Sysname LAGG/7/Fsm: GigabitEthernet1/0/2 FSM.RX PORT_DISABLED\--\>EXPIRED, Port_Enabled

\*Nov  5 10:33:34:645 2007 Sysname LAGG/7/Fsm: GigabitEthernet1/0/2 FSM.RX EXPIRED\--\>CURRENT, PDU_Indicate

*[// RX*]*状态机从LACP去使能状态无条件迁移到就绪状态*

**以太网链路聚合 \-- 以太网链路聚合调试命令 \-- debugging link-aggregation lacp packet**

------------------------------------------------------------------------

【命令】

**[debugging link-aggregation lacp packet**[ { **all** \| { **receive** \| **send** } \* } [ *interface-list* ]]]

**[undo debugging link-aggregation lacp packet**[ { **all** \| { **receive** \| **send** } \* } [ *interface-list* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示接收和发送LACP协议报文调试信息开关。

**[send**]：表示发送LACP协议报文调试信息开关。

**[receive**]：表示接收LACP协议报文调试信息开关。

*[interface-list*]：以太网端口列表。表示方式为*interface-list* = *interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type*为接口类型，*interface-number*为接口编号。若未指定此参数，则表示对所有运行LACP协议的端口都生效。

【描述】

**[debugging link-aggregation lacp packet**]命令用来打开端口的LACP协议报文调试信息开关。**undo debugging link-aggregation lacp packet**命令用来关闭端口的LACP协议报文调试信息开关。

缺省情况下，端口的LACP协议报文调试信息开关处于关闭状态。

表1-4 debugging link-aggregation lacp packet命令输出信息描述表

字段

描述

size

协议报文的大小，单位为字节

subtype

报文的协议子类型，对于LACP协议报文来说该值为1

version

协议版本信息，协议版本号为1表明是LACP协议

Actor

协议报文中携带的本端口的信息，其中：

·type=1：表示本端口信息

·len：表示该段信息的长度

·sys-pri：表示本端口所在系统的LACP协议优先级

·sys-mac：表示本端口所在系统的系统MAC地址

·key：表示本端口分配的操作Key值

·pri：表示本端口的LACP协议优先级

·port-index：表示本端口的端口号

·state：表示本端口目前的LACP协议状态标志

Partner

协议报文中携带的本系统保存的对端端口的信息，其中：

·type=2：表示本系统保存的对端信息

·len：表示该段信息的长度

·sys-pri：表示对端所在系统的LACP协议优先级

·sys-mac：表示对端所在系统的系统MAC地址

·key：表示对端端口分配的操作Key值

·pri：表示对端端口的LACP协议优先级

·port-index：表示对端端口的端口号

·state：表示对端端口目前的LACP协议状态标志

Collector

协议报文中的Collector字段的信息，其中：

·type=3：表示Collector字段信息

·len：表示该段信息的长度

·col-max-delay：表示最大延迟

Terminator

协议报文中的Terminator字段的信息，其中：

·type=0：表示Terminator字段，即表示协议报文结束

·len：表示该段信息的长度

【举例】

\# 将端口GigabitEthernet1/0/1加入到动态聚合组中，打开端口GigabitEthernet1/0/1的LACP报文调试信息开关，在设备上查看端口收发LACP协议报文的情况。

\<Sysname\> debugging link-aggregation lacp packet all interface gigabitethernet 1/0/1

\*Nov  2 15:51:21:15 2007 Sysname LAGG/7/Packet: PACKET.GigabitEthernet1/0/1.send.

*// 通过端口GigabitEthernet1/0/1发送LACP协议报文*

 size=110, subtype =1, version=1

*// 报文长度为110字节，协议子类型为1，版本号为1*

 Actor: type=1, len=20, sys-pri=0x8000, sys-mac=00e0-fc02-0300, key=0x1, pri=0x8000, port-index=0x2, state=0xc5

*// 报文中携带的本端口信息为：信息的长度为20，端口所在系统的LACP协议优先级为0x8000，端口所在系统的系统MAC地址为00E0-FC02-0300，端口分配的操作Key值为0x1，端口的LACP协议优先级为0x8000，端口号为0x2，端口目前的LACP协议状态标志为0xC5*

 Partner: type=2, len=20, sys-pri=0x0, sys-mac=0000-0000-0000, key=0x0, pri=0x0, port-index=0x0, state=0x32

*// 报文中携带的本系统保存的对端端口的信息为：信息的长度为20，对端所在系统的LACP协议优先级为0x0，对端所在系统的系统MAC地址为0000-0000-0000，对端端口分配的操作Key值为0x0，对端端口的LACP协议优先级为0x0，对端端口的端口号为0x0，对端端口目前的LACP协议状态标志为0x32*

 Collector: type=3, len=16, col-max-delay=0x0

*// 协议报文中的Collector字段信息为：信息的长度为16，最大延迟为0*

 Terminator: type=0, len=0

*// 协议报文中的Terminator字段信息的长度为0*

\*Nov  2 15:55:21:15 2007 Sysname LAGG/7/Packet: PACKET.GigabitEthernet1/0/1.receive.

*// 通过端口GigabitEthernet1/0/1收到LACP协议报文*

size=110, subtype =1, version=1

*// 报文长度为110字节，协议子类型为1，版本号为1*

 Actor: type=1, len=20, sys-pri=0x8000, sys-mac=00e0-fc00-0000, key=0x1, pri=0x8000, port-index=0x6, state=0xd

*// 报文中携带的本端口信息为：信息的长度为20，端口所在系统的LACP协议优先级为0x8000，端口所在系统的系统MAC地址为00E0-FC00-0000，端口分配的操作Key值为0x1，端口的LACP协议优先级为0x8000，端口的端口号为0x6，端口目前的LACP协议状态标志为0xD*

 Partner: type=2, len=20, sys-pri=0x8000, sys-mac=00e0-fc02-0300, key=0x1, pri=0x8000, port-index=0x2, state=0xc5

*// 报文中携带的本系统保存的对端端口的信息为：信息的长度为20，对端所在系统的LACP协议优先级为0x8000，对端所在系统的系统MAC地址为00E0-FC02-0300，对端端口分配的操作Key值为0x1，对端端口的LACP协议优先级为0x8000，对端端口的端口号为0x2，对端端口目前的LACP协议状态标志为0xC5*

 Collector: type=3, len=16, col-max-delay=0x0

*// 协议报文中的Collector字段信息为：信息的长度为16，最大延迟为0*

 Terminator: type=0, len=0

*// 协议报文中的Terminator字段信息的长度为0*

文中省略了其他类似的LACP协议报文信息。
