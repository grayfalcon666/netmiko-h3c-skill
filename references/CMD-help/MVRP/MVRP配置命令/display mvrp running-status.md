<!-- CMD-INDEX
  display mvrp running-status         | 任意视图             | L16
  display mvrp state                  | 任意视图             | L192
  display mvrp statistics             | 任意视图             | L290
  mrp timer join                      | 二层以太网接口视图/二层聚合接口视图 | L494
  mrp timer leave                     | 二层以太网接口视图/二层聚合接口视图 | L542
  mrp timer leaveall                  | 二层以太网接口视图/二层聚合接口视图 | L592
  mrp timer periodic                  | 二层以太网接口视图/二层聚合接口视图 | L648
  mvrp enable                         | 二层以太网接口视图/二层聚合接口视图 | L698
  mvrp global enable                  | 系统视图             | L748
  mvrp gvrp-compliance enable         | 系统视图             | L794
  mvrp registration                   | 二层以太网接口视图/二层聚合接口视图 | L834
  reset mvrp statistics               | 用户视图             | L884
-->

**MVRP \-- MVRP配置命令 \-- display mvrp running-status**

------------------------------------------------------------------------

**[display mvrp running-status**]命令用来显示MVRP运行状态信息。

【命令】

**[display mvrp running-status ** **interface** *interface-list* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-list*]：显示指定端口上的MVRP运行状态信息。*interface-list*为以太网端口列表，表示方式为*interface-list*= *interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type interface-number*为端口类型和端口编号。如果指定该参数，但端口未使能MVRP功能，则只显示MVRP全局信息。如果未指定该参数，则显示MVRP全局信息和所有使能MVRP功能端口的MVRP运行状态信息。

【举例】

\# 显示所有端口的MVRP运行状态信息。

\<Sysname\> display mvrp running-status

 \-\-\-\-\-\--[MVRP Global Info\-\-\-\-\-\--]

 Global Status     : Enabled

 Compliance-GVRP   : False

 \-\-\--[GigabitEthernet1/0/1\-\-\--]

 Config Status                  : Enabled

 Running Status                 : Enabled

 Join Timer                     : 20 (centiseconds)

 Leave Timer                    : 60 (centiseconds)

 Periodic Timer                 : 100 (centiseconds)

 LeaveAll Timer                 : 1000 (centiseconds)

 Registration Type              : Normal

 Registered VLANs :

  1(default), 2-10

 Declared VLANs :

  1(default), 2-10

 Propagated VLANs :

  1(default), 2-10

 \-\-\--[GigabitEthernet1/0/2\-\-\--]

 Config Status                  : Enabled

 Running Status                 : Disabled

 Join Timer                     : 20 (centiseconds)

 Leave Timer                    : 60 (centiseconds)

 Periodic Timer                 : 100 (centiseconds)

 LeaveAll Timer                 : 1000 (centiseconds)

 Registration Type              : Normal

 Registered VLANs :

  None

 Declared  VLANs :

  None

 Propagated VLANs :

  None

表1-1 display mvrp running-status命令显示信息描述表

字段

描述

MVRP Global Info

MVRP全局信息

Global Status

MVRP全局状态：

·Enabled：使能状态

·Disabled：未使能状态

Compliance-GVRP

是否兼容GVRP：

·True：兼容GVRP

·False：不兼容GVRP

\-\-\--GigabitEthernet1/0/1\-\-\--

接口提示符，到下一提示符开始前均为该接口的运行状态信息

Config Status

接口上MVRP功能的使能状态，取值为Enabled，表示使能MVRP

Running Status

接口上MVRP功能的运行状态（由接口的链路状态、链路类型、接口是否为聚合成员口及接口上MVRP功能的使能状态决定）：

·Enabled：使能状态

·Disabled：未使能状态

Join Timer

Join定时器的值，单位是厘秒

Leave Timer

Leave定时器的值，单位是厘秒

Periodic Timer

Periodic定时器的值，单位是厘秒

LeaveAll Timer

LeaveAll定时器的值，单位是厘秒

Registration Type

MVRP的注册模式：

·Normal：表示Normal模式

·Fixed：表示Fixed模式

·Forbidden：表示Forbidden模式

Registered VLANs

接口注册的VLAN

Declared VLANs

接口声明的VLAN，即通知对端接口学习的VLAN

Propagated VLANs

接口传播的VLAN，即接口学习并通知本设备其他接口向外声明的VLAN

**MVRP \-- MVRP配置命令 \-- display mvrp state**

------------------------------------------------------------------------

**[display mvrp state**]命令用来显示指定端口在指定VLAN内的MVRP接口状态信息。

【命令】

**[display mvrp state interface ***interface-type interface-number*** vlan ***vlan-id*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示指定端口上的MVRP接口状态信息。其中，*interface-type interface-number*为端口类型和端口编号。

**[vlan ***vlan-id*]：显示指定VLAN内的MVRP接口状态信息。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。

【举例】

\# 显示端口GigabitEthernet1/0/1上VLAN 2对应的MVRP接口状态信息。

\<Sysname\> display mvrp state interface gigabitethernet 1/0/1 vlan 2

 MVRP state of VLAN 2 on port GE1/0/1:

 Port                      VLAN   App-state   Reg-state

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\-\-\--

 GE1/0/1                      2       VP          IN

表1-2 display mvrp state命令显示信息描述表

字段

描述

MVRP state of VLAN 2 on port GE1/0/1

端口GigabitEthernet1/0/1上VLAN 2对应的MVRP接口状态信息

Port

端口简单名称，显示使能MVRP的端口的MVRP状态信息

VLAN

指定的VLAN ID

App-state

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

Reg-state

属性注册状态，用来记录对端实体声明的属性在本端的注册情况。其状态包括：IN、LV和MT，各状态含义如下：

·IN：注册状态，端口已经注册了该属性

·LV：离开状态，端口正在注销该属性

·MT：注销状态，端口未注册该属性

**MVRP \-- MVRP配置命令 \-- display mvrp statistics**

------------------------------------------------------------------------

**[display mvrp statistics**]命令用来显示MVRP统计信息。

【命令】

**[display mvrp statistics** [ **interface** *interface-list* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-list*]：显示指定端口上的MVRP统计信息。*interface-list*为以太网端口列表，表示方式为*interface-list *= *interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type* *interface-number*为端口类型和端口编号。如果未指定该参数，则显示所有使能MVRP功能的端口的MVRP统计信息。

【使用指导】

如果指定的端口上没有使能MVRP功能，则不显示任何信息。

【举例】

\# 显示所有使能MVRP功能的端口的MVRP统计信息。

\<Sysname\> display mvrp statistics

 \-\-\--[GigabitEthernet1/0/1\-\-\--]

 Failed Registrations        : 1

 Last PDU Origin             : 000f-e200-0010

 Frames Received             : 201

  New Event Received          : 0

  JoinIn Event Received       : 1167

  In Event Received           : 0

  JoinMt Event Received       : 22387

  Mt Event Received           : 31

  Leave Event Received        : 210

  LeaveAll Event Received     : 63

 Frames Transmitted          : 120

  New Event Transmitted       : 0

  JoinIn Event Transmitted    : 311

  In Event Transmitted        : 0

  JoinMt Event Transmitted    : 873

  Mt Event Transmitted        : 11065

  Leave Event Transmitted     : 167

  LeaveAll Event Transmitted  : 4

 Frames Discarded            : 0

 \-\-\--[GigabitEthernet1/0/2\-\-\--]

 Failed Registrations        : 0

 Last PDU Origin             : 0000-0000-0000

 Frames Received             : 0

  New Event Received          : 0

  JoinIn Event Received       : 0

  In Event Received           : 0

  JoinMt Event Received       : 0

  Mt Event Received           : 0

  Leave Event Received        : 0

  LeaveAll Event Received     : 0

 Frames Transmitted          : 0

  New Event Transmitted       : 0

  JoinIn Event Transmitted    : 0

  In Event Transmitted        : 0

  JoinMt Event Transmitted    : 0

  Mt Event Transmitted        : 0

  Leave Event Transmitted     : 0

  LeaveAll Event Transmitted  : 0

 Frames Discarded            : 0

表1-3 display mvrp statistics命令显示信息描述表

字段

描述

\-\-\--GigabitEthernet1/0/1\-\-\--

接口提示符，到下一提示符开始前均为该接口的统计信息

Failed Registrations

本实体上通过MVRP注册VLAN失败的次数

Last PDU Origin

上一个MVRP PDU的源MAC地址

Frames Received

收到的MVRP协议帧数

New Event Received

收到的New属性事件数

JoinIn Event Received

收到的JoinIn属性事件数

In Event Received

收到的In属性事件数

JoinMt Event Received

收到的JoinMt属性事件数

Mt Event Received

收到的Mt属性事件数

Leave Event Received

收到的Leave属性事件数

LeaveAll Event Received

收到的LeaveAll属性事件数

Frames Transmitted

发送的MVRP协议帧数

New Event Transmitted

发送的New属性事件数

JoinIn Event Transmitted

发送的JoinIn属性事件数

In Event Transmitted

发送的In属性事件数

JoinMt Event Transmitted

发送的JoinMt属性事件数

Mt Event Transmitted

发送的Mt属性事件数

Leave Event Transmitted

发送的Leave属性事件数

LeaveAll Event Transmitted

发送的LeaveAll个数

Frames Discarded

丢弃的MVRP协议帧数

**MVRP \-- MVRP配置命令 \-- mrp timer join**

------------------------------------------------------------------------

**[mrp timer join**]命令用来配置Join定时器的值。

**[undo mrp timer join**]命令用来恢复缺省情况。

【命令】

**[mrp timer join ***timer-value*]

**[undo mrp timer join**]

【缺省情况】

Join定时器的值为20厘秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timer-value*]：Join定时器的值，单位为厘秒（100厘秒＝1秒）。其取值应大于等于20厘秒，小于Leave定时器值的一半，且必须是20厘秒的倍数。

【举例】

\# 配置Join定时器的值为40厘秒（假设此时Leave定时器为100厘秒）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mrp timer join 40

【相关命令】

·**display** **mvrp running-status**

·**mrp timer leave**

**MVRP \-- MVRP配置命令 \-- mrp timer leave**

------------------------------------------------------------------------

**[mrp timer leave**]命令用来配置Leave定时器的值。

**[undo mrp timer leave**]命令用来恢复缺省情况。

【命令】

**[mrp timer leave ***timer-value*]

**[undo mrp timer leave**]

【缺省情况】

Leave定时器的值为60厘秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timer-value*]：Leave定时器的值，单位为厘秒（100厘秒＝1秒）。其取值应大于Join定时器值的两倍、小于LeaveAll定时器的值，且必须是20厘秒的倍数。

【举例】

\# 配置Leave定时器的值为100厘秒（假设此时Join和LeaveAll定时器均为缺省值）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mrp timer leave 100

【相关命令】

·**display mvrp running-status**

·**mrp timer join**

·**mrp timer leaveall**

**MVRP \-- MVRP配置命令 \-- mrp timer leaveall**

------------------------------------------------------------------------

**[mrp timer leaveall**]命令用来配置LeaveAll定时器的值。

**[undo mrp timer leaveall**]命令用来恢复缺省情况。

【命令】

**[mrp timer leaveall ***timer-value*]

**[undo mrp timer leaveall**]

【缺省情况】

LeaveAll定时器的值为1000厘秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timer-value*]：LeaveAll定时器的值，单位为厘秒（100厘秒＝1秒）。其取值应大于所有端口上Leave定时器的值、小于等于32760厘秒，且必须是20厘秒的倍数。

【使用指导】

·每一次LeaveAll定时器超时，都会引起全网当前端口对应MSTI的所有属性的注销。由于其影响范围很广，所以LeaveAll定时器的值不能太小。

·过小的LeaveAll定时器值可能会影响通过MVRP学习到的动态VLAN的稳定性，建议LeaveAll定时器的取值不要小于其缺省值（即1000厘秒）。

·为了防止每次都是同一实体的LeaveAll定时器先超时，每次重启时，LeaveAll定时器的值都将在一定范围内随机变动。

【举例】

\# 配置LeaveAll定时器的值为1500厘秒（假设此时所有端口的Leave定时器都为缺省值）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mrp timer leaveall 1500

【相关命令】

·**mrp timer leave**

·**display mvrp running-status**

**MVRP \-- MVRP配置命令 \-- mrp timer periodic**

------------------------------------------------------------------------

**[mrp timer periodic**]命令用来配置Periodic定时器的值。

**[undo mrp timer periodic**]命令用来恢复缺省情况。

【命令】

**[mrp timer periodic ***timer-value*]

**[undo mrp timer periodic**]

【缺省情况】

Periodic定时器的值为100厘秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

*[timer-value*]*：*Periodic定时器的值，单位为厘秒（100厘秒＝1秒），取值为0或100。

【使用指导】

当Periodic定时器的值为0厘秒时，定时器关闭；当Periodic定时器的值为100厘秒时，定时器开启，这时以100厘秒为周期发送MRP报文。

【举例】

\# 关闭Periodic定时器。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mrp timer periodic 0

【相关命令】

·**display mvrp running-status**

**MVRP \-- MVRP配置命令 \-- mvrp enable**

------------------------------------------------------------------------

**[mvrp enable**]命令用来使能当前端口的MVRP功能。

**[undo mvrp enable**]命令用来恢复缺省情况。

【命令】

**[mvrp enable**]

**[undo mvrp enable**]

【缺省情况】

端口的MVRP功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有全局和端口上都使能MVRP功能，同时端口链路Up、链路类型为Trunk类型，且端口不为聚合成员端口时，该端口上的MVRP功能才能生效。

【举例】

\# 使能端口GigabitEthernet1/0/1的MVRP功能。

\<Sysname\> system-view

Sysname mvrp global enable

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type trunk

Sysname-GigabitEthernet1/0/1 mvrp enable

【相关命令】

·**display mvrp running-status**

**MVRP \-- MVRP配置命令 \-- mvrp global enable**

------------------------------------------------------------------------

**[mvrp global enable**]命令用来全局使能MVRP功能。

**[undo mvrp global enable**]命令用来恢复缺省情况。

【命令】

**[mvrp global enable**]

**[undo mvrp global enable**]

【缺省情况】

全局的MVRP功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·要使端口上的MVRP功能生效，必须全局使能MVRP功能。

·关闭全局的MVRP功能的同时会关闭所有端口的MVRP功能。

【举例】

\# 全局使能MVRP功能。

\<Sysname\> system-view

Sysname mvrp global enable

【相关命令】

·**display mvrp running-status**

**MVRP \-- MVRP配置命令 \-- mvrp gvrp-compliance enable**

------------------------------------------------------------------------

**[mvrp gvrp-compliance enable**]命令用来配置MVRP兼容GVRP，此时既可以处理MVRP报文，也可以处理GVRP报文。

**[undo mvrp gvrp-compliance enable**]命令用来恢复缺省情况。

【命令】

**[mvrp gvrp-compliance enable**]

**[undo mvrp gvrp-compliance enable**]

【缺省情况】

MVRP不兼容GVRP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置MVRP兼容GVRP。

\<Sysname\> system-view

Sysname mvrp gvrp-compliance enable

【相关命令】

·**display mvrp running-status**

**MVRP \-- MVRP配置命令 \-- mvrp registration**

------------------------------------------------------------------------

**[mvrp registration**]命令用来配置端口的MVRP注册模式。

**[undo mvrp registration**]命令用来恢复缺省情况。

【命令】

**[mvrp registration**[ { **fixed** \| **forbidden** \| **normal** }]]

**[undo** **mvrp registration**]

【缺省情况】

接口的MVRP注册模式为Normal模式。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fixed**]：表示Fixed注册模式。

**[forbidden**]：表示Forbidden注册模式。

**[normal**]：表示Normal注册模式。

【举例】

\# 配置端口GigabitEthernet1/0/1的MVRP注册模式为Fixed模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mvrp registration fixed

【相关命令】

·**display mvrp running-status**

**MVRP \-- MVRP配置命令 \-- reset mvrp statistics**

------------------------------------------------------------------------

**[reset mvrp statistics**]命令用来清除端口上的MVRP统计信息。

【命令】

**[reset mvrp statistics** [ **interface** *interface-list* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-list*]：清除指定端口上的MVRP统计信息。*interface-list*为以太网端口列表，表示方式为*interface-list*＝*interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type interface-number*为端口类型和端口编号。如果未指定该参数，则清除所有端口上的MVRP统计信息。

【举例】

\# 清除所有端口上的MVRP统计信息。

\<Sysname\> reset mvrp statistics

【相关命令】

·**display mvrp statistics**
