<!-- CMD-INDEX
  debugging mac-address               | 用户视图             | L5
-->

**MAC地址表 \-- MAC地址表调试命令 \-- debugging mac-address**

------------------------------------------------------------------------

【命令】

**[debugging mac-address **[{ **event** \| **hardware** \| **search** \| **synchronization** }]]

**[undo debugging mac-address **[{ **event** \| **hardware** \| **search** \| **synchronization** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：表示MAC地址表模块事件调试信息开关。

**[hardware**]：表示MAC地址表模块下驱动调试信息开关。

**[search**]：表示MAC地址表模块向驱动查找MAC地址时的调试开关。

**[synchronization**]：表示MAC地址表模块板间同步调试开关。

【描述】

**[debugging mac-address**]命令用来打开MAC地址表调试信息开关。**undo debugging mac-address**命令用来关闭MAC地址表调试信息开关。

缺省情况下，MAC地址表调试信息开关处于关闭状态。

表1-1 debugging mac-address event命令显示信息描述表

字段

描述

Received VLAN event, Event type: *type*, Interface *interface-name*, VLAN list: *list*

收到VLAN事件（非主控板、备板和当前接口所在板，接口名会显示为接口索引）

Received interface event, Event type: *type*, interface number: *number*, Sequence: *Sequence*, Interface list: *interface-name-list*

收到接口事件（非主控板、备板和当前接口所在板，接口名会显示为接口索引）

表1-2 debugging mac-address hardware命令显示信息描述表

字段

描述

Notify driver to add an item: MAC address *mac-address*, VLAN ID *vid*, State *state*, Interface *interface-name*.

Return of adding item: result *result*, Driver context0 *context*, Driver context1 *context*

通知驱动添加一条表项并返回添加结果（非主控板、备板和当前接口所在板，接口名会显示为接口索引）

Notify driver to delete an item: MAC address *mac-address*, VLAN ID *vid*, State *state*, Interface *interface-name*, Driver context0 *context*, Driver context1 *context*

Return of deleting item: result *result*

通知驱动删除一条表项并返回删除结果（非主控板、备板和当前接口所在板，接口名会显示为接口索引）

MAC change notification from driver: Type *type*, Interface *interface-name*, VLAN ID *vid*, MAC type *type*, MAC address *mac-address*

驱动MAC变化的通知（非主控板、备板和当前接口所在板，接口名会显示为接口索引）

Set the MAC *action* notification flag *flag* of interface *interface-name* to driver(1 enable, 2 disable)

向驱动设置接口的MAC变化通知标记

Set MAC address learning priority for interface *interface-name*: *priority* (1 high, 2 low)

设置接口地址学习优先级

Set forwarding status for interface *interface-name*: *status* (1 enable, 2 disable)

设置接口的转发状态：

·1：允许转发

·2：禁止转发

Set forwarding status for VLAN ID *vid*: *status* (1 enable, 2 disable)

设置VLAN的转发状态：

·1：允许转发

·2：禁止转发

Set max address number for interface *interface-name*: *number*

设置接口下的MAC学习最大个数

Set max address number for VLAN ID *vid*: *number*

设置VLAN下的MAC学习最大个数

Set learning status for VLAN ID *vid*: *status* (0 learn, 1 not learn, 3 not learn & drop, 7 not learn & drop & notify)

设置VLAN的表项学习状态，其中status的取值为：

·0：学习

·1：不学习

·3：不学习并丢弃

·7：不学习、丢弃、并通知平台

Set learning status for interface *interface-name*: *status* (0 learn, 1 not learn, 3 not learn & drop, 7 not learn & drop & notify)

设置接口的表项学习状态，其中status的取值为：

·0：学习

·1：不学习

·3：不学习并丢弃

·7：不学习、丢弃、并通知平台

Set global address learning status: status (0 learn, 1 not learn, 3 not learn & drop, 7 not learn & drop & notify)

设置全局的表项学习状态，其中status的取值为：

·0：学习

·1：不学习

·3：不学习并丢弃

·7：不学习、丢弃、并通知平台

Set MAC roaming: Action: *action*

设置MAC全局同步

Return of setting control: result *result*

设置控制信息后的返回结果

New data: Learn *data*, Drop *data*, Notify *data*

源MAC未知报文学习设置新数据

Old data: Learn *data*, Drop *data*, Notify *data*

源MAC未知报文学习设置旧数据

Check unknown MAC: Scope *scope*, VLAN ID *vid*, Interface *interface-name*, Action *action*, Result *result*

检查源MAC未知报文学习能力（非主控板、备板和当前接口所在板，接口名会显示为接口索引）

Set unknown MAC: Module *module*, Scope *scope*, VLAN ID *vid*, Interface *interface-name*, Action *action*, MDCDeletingFlag *flag*

设置源MAC未知报文学习动作（非主控板、备板和当前接口所在板，接口名会显示为接口索引）

表1-3 debugging mac-address search命令显示信息描述表

字段

描述

Find item from driver: MAC address *mac-addres*s, VLAN ID *vid*

Return of finding item: result *result*, MAC address *mac-addres*s, VLAN ID *vid*, State *state*, Interface *interface-name*

向驱动查询一条表项并返回查询结果

表1-4 debugging mac-address synchronization命令显示信息描述表

字段

描述

Received message from *channel* of chassis *chassis-number* slot *slot-number*

收到从框号为*chassis-number*板号为*slot-number*通道为*channel*的消息

Connected to *channel* of chassis *chassis-number* slot *slot-number*

与框号为*chassis-number*板号为*slot-number*的*channel*通道建立连接

Disconnected from *channel* of chassis *chassis-number* slot *slot-number*

与框号为*chassis-number*板号为*slot-number*的*channel*通道断开

Pull global configuration

从主控板拉全局配置

Pull interface configuration

从主控板拉端口下配置

Pull static configuration

从主控板拉MAC静态表项

Pull VLAN configuration

从主控板拉VLAN下配置

Pull smooth status

从主控板拉平滑状态

Failed to send synchronization message

发送同步消息失败

Enqueue message: Type: *type*, Length: *length*, Number: *number*

消息入实时同步队列

Received pull message from chassis *chassis-number* slot *slot-number*

收到从框号为*chassis-number*板号为*slot-number*的PULL消息

Sent synchronization message with length *length*

发送长度为*length*的同步消息

Received synchronization message with length *length*

接收到长度为*length*的同步消息

【举例】

\# 打开MAC地址表的event调试开关，关闭接口GigabitEthernet1/0/1。

\<Sysname\> debugging mac-address event

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 shutdown

Sysname-GigabitEthernet1/0/1 \*Dec 27 17:49:11:808 2012 Sysname MAC/7/EVENT: -MDC=1-Chassis=2

-Slot=3;

 Received interface event, Event type: 0x20000040, interface number: 1, Sequence

: 44, interface list:

\*\*[0: GE1/0/1]

\*Dec 27 17:49:11:810 2012 Sysname MAC/7/EVENT: -MDC=1;

 Received interface event, Event type: 0x20000040, interface number: 1, Sequence

: 64, interface list:

\*\*[0: GE1/0/1]

\# 打开MAC地址表的hardware调试开关，并添加一条MAC地址表项。

\<Sysname\> debugging mac-address hardware

\<Sysname\> system-view

Sysname mac-address static 3-2-2 interface gigabitethernet 1/0/1 vlan 10

Sysname \*Dec 27 17:31:26:161 2012 Sysname MAC/7/HARDWARE: -MDC=1;

 Notify driver to add an item: MAC address 0003-0002-0002, VLAN ID 0xa, State 0x

1, interface GE1/0/1.

\*Dec 27 17:31:26:161 2012 Sysname MAC/7/HARDWARE: -MDC=1;

 Return of adding item: result 0x0, Driver context[0 0xffffffffffffffff, Driver]

 context[1 0xffffffffffffffff.]

\*Dec 27 17:31:26:162 2012 Sysname MAC/7/HARDWARE: -MDC=1-Chassis=2-Slot=3;

 Notify driver to add an item: MAC address 0003-0002-0002, VLAN ID 0xa, State 0x

1, interface GE1/0/1.

\*Dec 27 17:31:26:162 2012 Sysname MAC/7/HARDWARE: -MDC=1-Chassis=2-Slot=3;

 Return of adding item: result 0x0, Driver context[0 0xffffffffffffffff, Driver]

 context[1 0xffffffffffffffff.]

\# 打开MAC地址表的search调试开关，添加一条多端口ARP并匹配多端口单播MAC地址表项。

\<Sysname\> debugging mac-address search

\<Sysname\> system-view

Sysname mac-address multiport 4-4-4 interface gigabitethernet 1/0/1 vlan 10

Sysname arp multiport 2.2.2.3 4-4-4 10

Sysname \*Dec 27 17:40:26:079 2012 Sysname MAC/7/SEARCH: -MDC=1;

 Find item from driver: MAC address 0004-0004-0004, VLAN ID 0xa.

\*Dec 27 17:40:26:079 2012 Sysname MAC/7/SEARCH: -MDC=1;

 Return of finding item: result 0x60010023, MAC address 0004-0004-0004, VLAN ID

0x0, State 0x0, Interface GE1/0/1.

\*Dec 27 17:40:26:112 2012 Sysname MAC/7/SEARCH: -MDC=1-Chassis=2-Slot=3;

 Find item from driver: MAC address 0004-0004-0004, VLAN ID 0xa.

\*Dec 27 17:40:26:112 2012 Sysname MAC/7/SEARCH: -MDC=1-Chassis=2-Slot=3;

 Return of finding item: result 0x60010023, MAC address 0004-0004-0004, VLAN ID

0xdb81, State 0x0, Interface GE1/0/1.

\# 打开MAC地址表的synchronization调试开关，添加一条静态MAC地址表项。

\<Sysname\> debugging mac-address synchronization

\<Sysname\> system-view

Sysname mac-address static 6-6-6 interface gigabitethernet 1/0/1 vlan 10

Sysname \*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;

 Connected to user synchronization channel of chassis 2 slot 1

\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;

 Received message from user synchronization channel of chassis 2 slot 1

\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;

 Enqueue message: Type: 0, Length: 64, Number: 1

\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;

 Sent synchronization message with length 64

\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1-Chassis=2-Slot=1;

 Received message from multicast synchronization channel of chassis 2 slot 1

\*Dec 27 17:46:18:217 2012 Sysname MAC/7/SYNC: -MDC=1;

 Disconnected from user synchronization channel of chassis 2 slot 1

