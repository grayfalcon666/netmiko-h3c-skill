<!-- CMD-INDEX
  debugging mvrp error                | 用户视图             | L8
  debugging mvrp event                | 用户视图             | L208
  debugging mvrp packet               | 用户视图             | L280
  debugging mvrp state                | 用户视图             | L354
-->

**MVRP \-- MVRP调试命令 \-- debugging mvrp error**

------------------------------------------------------------------------

【命令】

**[debugging mvrp error**]

**[undo debugging mvrp error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging mvrp error**]命令用来打开MVRP错误调试信息开关。**undo debugging mvrp error**命令用来关闭MVRP错误调试信息开关。

缺省情况下，MVRP错误调试信息开关处于关闭状态。

表1-1 debugging mvrp error命令输出信息描述表

字段

描述

Failed to send LeaveAll indication out of ifindex *ifindex*.

从接口*ifindex*发送LeaveAll指示失败

Failed to send Join indication out of ifindex *ifindex*.

从接口*ifindex*发送Join指示失败

Failed to add DBM-key *szKey* to configuration data.

添加DBM-key *szKey*到配置数据失败

Failed to delete DBM-key *szKey* from configuration data.

从配置数据库中删除DBM-key *szKey*失败

Failed to start timerFD *iTimerfd*.

启动定时器*iTimerfd*失败

Failed to stop timerFD *iTimerfd*.

停止定时器*iTimerfd*失败

Received an invalid packet.

收到错误报文

Failed to de-encapsulate GVRP packet for ifindex *ifindex*.

解析接口*ifindex*的GVRP报文失败

Failed to propagate VLAN for ifindex *ifindex*.

在接口*ifindex*传播VLAN失败

Received illegal GVRP packet.

收到非法的GVRP报文

Failed to create subsocket *iSocketFd*.

创建*iSocketFd*的子socket失败

Failed to add subsocket *iAcceptFd* to Epoll.

将子socket *iAcceptFd*加入Epoll失败

Failed to encapsulate packet header for ifindex *ifindex*.

接口*ifindex*封装报文头失败

Failed to encapsulate packet message for ifindex *ifindex*.

接口*ifindex*封装报文Message失败

Failed to de-encapsulate packet for ifindex *ifindex*.

在接口*ifindex*上解析报文失败

Failed to send packet for ifindex *ifindex*.

接口*ifindex*发送报文失败

Failed to create running data for ifIndex *ifindex*.

创建接口*ifindex*运行数据失败

Failed to get running CB for ifIndex *ifindex*.

获取接口*ifindex*运行数据控制块失败

Failed to create Join timer for ifIndex *ifindex*.

创建接口*ifindex*的Join定时器失败

Failed to create Leave timer for ifIndex *ifindex*.

创建接口*ifindex*的Leave定时器失败

Failed to create LeaveAll timer for ifIndex *ifindex*.

创建接口*ifindex*的LeaveAll定时器失败

Failed to create Periodic timer for ifIndex *ifindex*.

创建接口*ifindex*的Periodic定时器失败

Failed to get permitted VLAN bitmap for ifIndex *ifindex*.

获取接口*ifindex*允许通过的VLAN位图失败

Failed to get static VLAN bitmap.

获取静态VLAN位图失败

Failed to notify VLAN for ifIndex *ifindex*.

接口*ifindex*下发VLAN失败

Failed to set statistics for ifIndex *ifindex*.

设置接口*ifindex*的统计信息失败

Failed to set running data for ifIndex *ifindex*.

设置接口*ifindex*运行数据失败

Failed to get config data for ifIndex *ifindex*.

获取接口*ifindex*配置数据失败

Failed to get debug data for ifIndex *ifindex*.

获取接口*ifindex*的debug数据失败

Failed to process STP event for ifIndex *ifindex*.

处理接口*ifindex*的STP事件失败

Failed to restore configuration info for ifIndex *ifindex*.

恢复接口*ifindex*的配置数据失败

Failed to delete VLAN bitmap of ifIndex *ifindex*.

删除接口*ifindex*的VLAN位图失败

Failed to delete configuration info for ifIndex *ifindex*.

删除接口*ifindex*配置数据失败

Failed to create VLAN list.

创建VLAN列表失败

Failed to destroy VLAN list.

删除VLAN列表失败

Failed to get the bitmap for VLAN increasing operation on ifIndex *ifindex*.

获取接口*ifindex*的VLAN增加操作位图失败

Failed to get the bitmap for VLAN decreasing operation on ifIndex *ifindex*.

获取接口*ifindex*的VLAN减少操作位图失败

Failed to get stable VLAN bitmap of ifIndex *ifindex*.

获取接口*ifindex*的稳态VLAN位图失败

Failed to judge whether port *ifindex* is a aggregation group member.

判断接口*ifindex*是否为聚合成员口失败

【举例】

\# 在一台启动了MVRP功能并且配置了兼容GVRP模式的设备上打开MVRP错误信息调试功能，使能MVRP功能的端口接收到错误的GVRP报文时，会打印如下调试信息。

\<Sysname\> debugging mvrp error

\*Mar 10 14:22:21:015 2012 Sysname MVRP/7/Error: -MDC=1; Failed to receive illegal gvrp packet.

**MVRP \-- MVRP调试命令 \-- debugging mvrp event**

------------------------------------------------------------------------

【命令】

**[debugging mvrp event**]

**[undo debugging mvrp event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging mvrp event**]命令用来打开MVRP事件调试信息开关。**undo debugging mvrp error**命令用来关闭MVRP事件调试信息开关。

缺省情况下，MVRP事件调试信息开关处于关闭状态。

表1-2 debugging mvrp event命令输出信息描述表

字段

描述

TimerFD has expired *n* times.

定时器超时*n*次

TimerFD is suspended or failed.

定时器暂停或处理失败

VLAN list successfully created.

成功创建VLAN列表

VLAN list successfully destroyed.

成功删除VLAN列表

IfIndex *ifIndex* successfully added to dynamic VLAN list.

将接口*ifIndex*加入动态VLAN列表处理成功

IfIndex *ifIndex* successfully deleted from dynamic VLAN list.

将接口*ifIndex*退出动态VLAN列表处理失败

MRP data successfully created on ifIndex *ifIndex*.

在接口*ifIndex*创建MRP数据成功

【举例】

\# 在一台启动了MVRP功能设备上打开MVRP事件信息调试功能，进入接口视图，使能MVRP功能，会打印如下调试信息。

\<Sysname\> debugging mvrp event

\*Mar 10 14:32:21:015 2012 Sysname MVRP/7/Event: -MDC=1; MRP data successfully created on ifIndex 1.

**MVRP \-- MVRP调试命令 \-- debugging mvrp packet**

------------------------------------------------------------------------

【命令】

**[debugging**[ **mvrp** **packet** { **send** \| **receive** } **interface** *interface-type interface-number*]]

**[undo**[ **debugging** **mvrp** **packet** { **send** \| **receive** } **interface** *interface-type interface-number*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[send**]：表示发送MVRP协议报文调试信息开关。

**[receive**]：表示接收MVRP协议报文调试信息开关。

**[interface*** interface-type interface-number*]：显示指定端口上协议报文调试信息。其中，*interface-type*为端口类型，*interface-number*为端口编号。

【描述】

**[debugging** **mvrp** **packet**]命令用来打开端口的MVRP协议报文调试信息开关。**undo** **debugging** **mvrp** **packet**命令用来关闭端口的MVRP协议报文调试信息开关。

缺省情况下，端口的MVRP报文调试开关处于关闭状态。

表1-3 debugging mvrp packet命令输出信息描述表

字段

描述

VLAN Attribute

VLAN属性值，用来表示VLAN状态。其值包括：New，JoinIn，In，JoinEmpty，Empty，Lv。具体含义如下：

·New：新声明的属性，其注册状态不确定

·JoinIn：声明并且已经注册的属性

·In：未声明但已经注册的属性

·JoinEmpty：声明但未注册的属性

·Empty：既没有声明也没有注册的属性

·Lv：注销的属性

VLAN ID

VLAN的编号

【举例】

\# 端口GigabitEthernet1/0/1使能了MVRP功能，打开该端口上MVRP发送报文调试信息开关。

\<Sysname\> debugging mvrp packet send interface gigabitethernet 1/0/1

\*Mar 10 17:23:59:860 2012 Sysname MVRP/7/Packet: PACKET.GigabitEthernet1/0/1.send:

*// 通过端口GigabitEthernet1/0/1发送MVRP协议报文*

 VLAN Attribute = JoinIn, VLAN ID = 1.

*// 报文中携带的VLAN ID是1，属性值是JoinIn*

**MVRP \-- MVRP调试命令 \-- debugging mvrp state**

------------------------------------------------------------------------

【命令】

**[debugging** **mvrp** **state** **interface** *interface-type interface-number* **vlan** *vlan-id*]

**[undo** **debugging** **mvrp** **state** **interface** *interface-type interface-number* **vlan** *vlan-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：端口类型和端口编号。

*[vlan*-id]：VLAN的编号，取值范围为1～4094。

【描述】

**[debugging** **mvrp** **state**]命令用来打开端口上指定VLAN的MVRP状态机的调试信息开关。**undo debugging** **mvrp** **state**命令用来恢复缺省情况。

缺省情况下，MVRP状态机调试信息开关处于关闭状态。

表1-4 debugging mvrp state命令输出信息描述表

字段

描述

AttrID

VLAN属性ID

APP

属性声明状态，用来记录本端向对端实体声明的属性的状态。其状态包括：VO、VP、VN、AN、AA、QA、LA、AO、QO、AP、QP和LO，每个状态都由2个字母组成，各字母含义如下：

第一个字母表示状态：

·V代表Very anxious（非常迫切的），表示该属性未曾声明过且没有收到过Join消息

·A代表Anxious（迫切的），表示该属性声明过一次或收到过一个Join消息

·Q代表Quiet（安静的），表示该属性声明过两次，或声明过一次且收到过一个Join消息，或收到过两个Join消息

·L代表Leaving（离开），表示该属性正在注销

第二个字母表示成员类型：

·A代表Active member（主动成员），表示正在声明该属性，至少已有一次发送，可以有接收

·P代表Passive member（被动成员），表示正在声明该属性，但是只有接收，没有发送

·O代表Observer（观察者），表示未在声明该属性，只是在侦听

·N代表New（新属性被动端），表示正在声明该属性，但是只有接收，没有发送

譬如，VP代表"Very anxious，Passive member"，表示Very anxious状态下的被动成员

*[Reg*]

属性注册状态，用来记录其他实体所声明属性的注册情况。其状态包括：IN、LV和MT，各状态含义如下：

·IN：注册状态，端口已经注册了该属性

·LV：离开状态，端口正在注销该属性

·MT：注销状态，端口未注册该属性

Event

引发属性状态迁移的条件：

对于属性声明状态来说，条件包括：

·Begin!：属性状态初始化

·New!：MRP应用请求声明该属性，且端口相应实例的tcDetected定时器不为0

·Join!：MRP应用请求声明该属性

·Lv!：MRP应用请求注销该属性

·rNew!：收到一个属性声明，且标记为NEW

·rJoinIn!：收到一个属性声明，且对端已经注册

·rIn!：收到一个属性消息，对端已经注册，但不声明

·rJoinMt!：收到一个属性声明，且对端尚未注册

·rMt!：收到一个属性消息，对端尚未注册且不声明

·rLv!：收到一个属性注销消息

·rLA!：收到一个LeaveAll消息

·Re-declare!：MSTP端口角色由Desi端口转换为Root或者Alte端口时，触发MVRP属性全部重新声明

·periodic!：周期发送定时器超时事件

·tx!：一个发包时机生成，且没有LeaveAll事件标记

·txLA!：一个发包时机生成，且LeaveAll事件标记置位

·txLAF!：一个发包时机生成，且LeaveAll事件标记置位，同时PDU消息中已经没有额外的空间

对于属性注册状态来说，条件包括：

·Begin!：属性状态初始化

·rNew!：收到一个新属性注册

·rJoinIn!：收到一个属性注册，对端已经注册该属性

·rJoinMt!：收到一个属性注册，对端尚未注册该属性

·rLv!：收到一个属性注销

·rLA!：收到一个LeaveAll消息

·txLA!：一个发包时机生成，且LeaveAll事件标记置位

·Re-declare!：MSTP端口角色由Desi端口转换为Root或者Alte端口时，触发MVRP属性全部重新声明

·Flush!：MSTP端口角色由Root或者Alte端口转换为Desi端口时，触发MVRP属性全部进行快速注销，同时会触发LeaveAll状态机，事件为LeaveAll定时器超时

·Leavetimer!：Leave定时器超时事件，超时后触发端口注销该属性

LeaveAll

LeaveAll标识，取值只能为True，表示LeaveAll定时器超时。当LeaveAll定时器未超时时，不打印该字段

【举例】

\# 将端口GigabitEthernet1/0/1上VLAN 2的MVRP状态机调试信息开关打开，在设备上查看端口的状态机调试信息。使能端口GigabitEthernet1/0/1及对端的MVRP功能后，在对端设备创建VLAN 2，会打印如下调试信息。

\<Sysname\> debugging mvrp state interface gigabitethernet 1/0/1 vlan 2

\*Mar 10 17:52:58:875 2012 Sysname MVRP/7/Fsm: -MDC=1;

 GigabitEthernet1/0/1: AttrID = 2: APP = VO Reg = IN, Event = rJoinMt!.

*// 端口GigabitEthernet1/0/1上VLAN 2的申请者状态机为VO，注册者状态机为IN，事件为rJoinMt!*

\# LeaveAll定时器超时后，会打印如下调试信息。

\*Mar 31 17:52:58:938 2011 Sysname MVRP/7/Fsm: -MDC=1;

 GigabitEthernet1/0/1: AttrID = 2: APP = LO Reg = LV, Event = rLA!, LeaveAll = TRUE.

*// 端口GigabitEthernet1/0/1上VLAN 2的申请者状态机为LO，注册者状态机为LV，事件为rLA!，LeaveAll标识为TRUE*

