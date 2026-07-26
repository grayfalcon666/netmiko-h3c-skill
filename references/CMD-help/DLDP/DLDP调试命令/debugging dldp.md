
**DLDP \-- DLDP调试命令 \-- debugging dldp**

------------------------------------------------------------------------

【命令】

**[debugging dldp**[ { **all** \| **error** \| **event** \| **timer** \| { **fsm** \| **packet** } [ **interface** *interface-type* *interface-number* ] }]]

**[undo **]**debugging dldp**[{ **all** \| **error** \| **event** \| **timer** \| { **fsm** \| **packet** } [ **interface** *interface-type* *interface-number* ] }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DLDP的所有调试信息开关。

**[error**]：表示DLDP错误报文调试信息开关。

**[event**]：表示DLDP事件调试信息开关。

**[timer**]：表示DLDP定时器调试信息开关。

**[fsm**]：表示DLDP状态机调试信息开关。

**[packet**]：表示DLDP报文调试信息开关。

**[interface** *interface-type* *interface-number*]：表示指定接口的DLDP调试信息开关，*interface-type* *interface-number*为接口类型和接口编号。如果未指定本参数，则表示所有接口的DLDP调试信息开关。

【描述】

**[debugging dldp**]命令用来打开DLDP调试信息开关。**undo debugging dldp**命令用来关闭DLDP调试信息开关。

缺省情况下，DLDP调试信息开关处于关闭状态。

表1-1 debugging dldp error命令输出信息描述表

字段

描述

Port *port-name* received an error packet

接口*port-name*收到了一个错误报文

Reason types of the error packet

报文的错误类型：

·LENGTH ERROR：表示报文长度错误

·DLDP NOT ENABLE：表示DLDP未使能

·CURRENT STATE CAN\'T RECEIVE PACKET：表示在当前状态下不能接收报文

·PROTOCOL ID ERROR：表示报文协议号错误

·VERSION ERROR：表示报文版本号错误

·INTERVAL ERROR：表示报文中通告时间间隔错误

·AUTHTYPE ERROR：表示报文的认证类型错误

·PASSWORD ERROR：表示报文的认证密码错误

·LOOP PACKET：表示是自环报文

·PACKET TYPE ERROR：表示报文类型错误

表1-2 debugging dldp event命令输出信息描述表

字段

描述

Port *port-name* down/up

接口*port-name*发生物理down/up

表1-3 debugging dldp timer命令输出信息描述表

字段

描述

Port *port-name* created a delaydown/recover-probe timer

接口*port-name*上建立了delaydown/recover-probe定时器

Port *port-name* created an advertisement timer

接口*port-name*上建立了advertisement定时器

The advertisement/delaydown/recover-probe timer of port *port-name* timed out

接口*port-name*下的advertisement/delaydown/recover-probe定时器超时

Neighbor BridgeMAC

邻居桥MAC地址

Neighbor PortIndex

邻居接口索引

The neighbor of port *port-name* created a probe timer

接口*port-name*下的邻居建立了probe定时器

The neighbor of port *port-name* created an aged/echo timer

接口*port-name*下的邻居建立了aged/echo定时器

The neighbor's aged/echo/probe timer of port *port-name* timed out

接口*port-name*下邻居的aged/echo/probe定时器超时

表1-4 debugging dldp fsm命令输出信息描述表

字段

描述

Port *port-name* added/deleted a neighbor

接口*port-name*增加/删除了一个邻居

A state transition occurred to the neighbor of port *port-name*

接口*port-name*上有邻居进行状态迁移

Neighbor BridgeMAC

邻居的桥MAC地址

Neighbor PortIndex

邻居的接口索引

Neighbor state

邻居的状态：

·UNCONFIRMED：表示未确认状态

·CONFIRMED：表示确认状态

Neighbor state transition: *state1* \--\> *state2*

邻居的状态由*state1*迁移到*state2*，状态包括：

·UNCONFIRMED：表示未确认状态

·CONFIRMED：表示确认状态

Port *port-name* state transition: *state1* \--\> *state2*

接口*port-name*的状态由*state1*迁移到*state2*，状态包括：

·INITIAL：表示初始化状态

·INACTIVE：表示非活动状态

·UNIDIRECTIONAL：表示单通状态

·BIDIRECTIONAL：表示双通状态

Stimulation

激励条件：

·DLDP enable：表示使能DLDP

·DLDP disable：表示关闭DLDP

·Port down：表示接口物理down

·Port up：表示接口物理up

·No confirmed neighbor：表示没有确认邻居

·Confirmed neighbor：表示有确认邻居

表1-5 debugging dldp packet命令输出信息描述表

字段

描述

Port *port-name* sent/received a DLDP packet

接口*port-name*发送/收到了一个DLDP报文

Following is the content of the packet

该报文的具体内容如下

DLDP ID

报文中携带的协议号

DLDP version ID

报文中携带的版本号

DLDP packet type

报文类型：

·ADVERTISEMENT：表示Advertisement报文

·PROBE：表示Probe报文

·ECHO：表示Echo报文

·ADVERTISEMENT-RSY：表示RSY报文

·ADVERTISEMENT-FLUSH：表示Flush报文

·DISABLE：表示Disable报文

·LINKDOWN：表示LinkDown报文

·RECOVER-PROBE：表示RecoverProbe报文

·RECOVER-ECHO：表示RecoverEcho报文

·ILLEGAL：表示非法报文

Flags

报文RSY标志：

·NO-RSY：表示该报文是普通Advertisement报文

·RSY：表示该报文是RSY报文

·FLUSH：表示该报文是Flush报文

·NO-FLAG：表示当前的报文类型不关心Flag位

·ILLEGAL：表示非法标记

Authentication mode

报文认证方式：

·NONE：表示不认证

·SIMPLE：表示明文认证方式

·MD5：表示MD5认证方式

·ILLEGAL：标识非法的认证模式

Authentication password

报文认证密码

Interval of sending Advertisement packet

报文中携带的发送Advertisement报文时间间隔（单位为秒）

HostBridgeMAC

报文中携带的桥MAC地址

HostPortIndex

报文中携带的接口索引

Neighbor information

是否携带邻居信息：

·Carried：表示携带

·Not carried：表示未携带

【举例】

\# 在Device A和Device B上都全局使能DLDP功能，并分别在其各自的接口GigabitEthernet1/0/1上使能DLDP功能；配置Device A的Advertisement报文发送时间间隔为5秒；在Device B上打开DLDP错误报文调试信息开关，并配置其Advertisement报文发送时间间隔为10秒。

\<DeviceB\> debugging dldp error

\*Apr 26 12:05:54:962 2011 DeviceB DLDP/7/ERROR: -MDC=1; Port GigabitEthernet1/0/1 received an error packet. Reason types of the error packet: INTERVAL ERROR.

*[// Device B*]*的接口GigabitEthernet1/0/1收到了一个错误报文，报文的错误类型为"报文中通告时间间隔错误"*

\# 在Device A和Device B上都全局使能DLDP功能，并分别在其各自的接口GigabitEthernet1/0/1上使能DLDP功能；在Device B上打开DLDP事件调试信息开关，拔掉其接口GigabitEthernet1/0/1上的光纤。

\<DeviceB\> debugging dldp event

\*Apr 26 12:05:54:962 2011 DeviceB DLDP/7/EVENT: -MDC=1; Port GigabitEthernet1/0/1 down.

*[// Device B*]*的接口GigabitEthernet1/0/1发生物理down*

\# 在Device A和Device B上都全局使能DLDP功能，并在Device A的接口GigabitEthernet1/0/1上使能DLDP功能；在Device A和Device B上都打开DLDP定时器调试信息开关，并在Device B的接口GigabitEthernet1/0/1上使能DLDP功能。

\<DeviceB\> debugging dldp timer

\*Apr 26 12:05:54:962 2011 DeviceB DLDP/7/TIMER: -MDC=1; Port GigabitEthernet1/0/1 created a recover-probe timer.

*[// Device B*]*的接口GigabitEthernet1/0/1上建立了一个recover-probe定时器*

\<DeviceA\> debugging dldp timer

\*Apr 26 12:05:54:962 2011 DeviceA DLDP/7/TIMER:

The neighbor of port GigabitEthernet1/0/1 created a probe timer.

Neighbor BridgeMAC: 00e0-fc00-3331

Neighbor PortIndex: 9

*[// Device A*]*的接口GigabitEthernet1/0/1下的邻居建立了一个probe定时器，该邻居的桥MAC地址为00E0-FC00-3331，接口索引为9*

\*Apr 26 12:05:54:962 2011 DeviceA DLDP/7/TIMER: -MDC=1; The neighbor\'s probe timer of port GigabitEthernet1/0/1 timed out.

Neighbor BridgeMAC: 00e0-fc00-3331

Neighbor PortIndex: 9

*[// Device A*]*的接口GigabitEthernet1/0/1下邻居的probe定时器超时，该邻居的桥MAC地址为00E0-FC00-3331，接口索引为9*

\# 在Device A和Device B上都全局使能DLDP功能，并分别在其各自的接口GigabitEthernet1/0/1上使能DLDP功能；在Device B上打开DLDP状态机调试信息开关。

\<DeviceB\> debugging dldp fsm

\*Apr 26 12:07:07:731 2011 DeviceB DLDP/7/FSM: -MDC=1; Port GigabitEthernet1/0/1 added a neighbor.

 Neighbor BridgeMAC: 00e0-fc00-3333

 Neighbor PortIndex: 35

 Neighbor state: UNCONFIRMED

*[// Device B*]*的接口GigabitEthernet1/0/1增加了一个邻居，该邻居的桥MAC地址为00E0-FC00-3333，接口索引为35，处于未确认状态*

\*Apr 26 12:07:09:731 2011 DeviceB DLDP/7/FSM: -MDC=1; A state transition occurred to the neighbor of port GigabitEthernet1/0/1.

 Neighbor BridgeMAC: 00e0-fc00-3333

 Neighbor PortIndex: 35

 Neighbor state transition: UNCONFIRMED \--\> CONFIRMED

*[// Device B*]*的接口GigabitEthernet1/0/1上有邻居进行状态迁移，该邻居的桥MAC地址为00E0-FC00-3333，接口索引为35，由未确认状态迁移到确认状态*

\*Apr 26 12:12:22:653 2011 DeviceB DLDP/7/FSM: -MDC=1; Port GigabitEthernet1/0/1 state transition: UNIDIRECTIONAL \--\> BIDIRECTIONAL

 Stimulation: Confirmed neighbor

*[// Device B*]*的接口GigabitEthernet1/0/1发生了状态迁移，由单通状态迁移到双通状态，激励条件为有确定邻居*

\# 在Device A和Device B上都全局使能DLDP功能，并分别在其各自的接口GigabitEthernet1/0/1上使能DLDP功能；在Device A上打开接口GigabitEthernet1/0/1的DLDP报文调试信息开关。

\<DeviceA\> debugging dldp packet interface gigabitethernet 1/0/1

\*Apr 26 12:10:18:523 2011 DeviceA DLDP/7/PKT: -MDC=1; Port GigabitEthernet1/0/1 received a DLDP packet. Following is the content of the packet:

 DLDP ID: 0x0001

 DLDP version ID: 0x01

 DLDP packet type: ADVERTISEMENT

 Flags: NO-RSY

 Authentication mode: NONE

 Authentication password:

 Interval of sending Advertisement packet: 5 seconds

 HostBridgeMAC: 00e0-fc00-3331

 HostPortIndex: 9

 Neighbor information: Not carried

*[// Device A*]*的接口GigabitEthernet1/0/1收到了一个DLDP报文，其具体内容如下：协议号为1，版本号为1，报文类型为Advertisement报文，RSY标志为0（表示普通Advertisement报文），认证方式为不认证，无认证密码，发送Advertisement报文时间间隔为5秒，桥MAC地址为00E0-FC00-3331，接口索引为9，未携带邻居信息*
