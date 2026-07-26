
**生成树 \-- 生成树调试命令 \-- debugging stp all**

------------------------------------------------------------------------

【命令】

**[debugging stp** **all**]

**[undo debugging stp all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging stp all**]命令用来打开生成树的所有调试信息开关。**undo debugging stp all**命令用来关闭生成树的所有调试信息开关。

缺省情况下，生成树的所有调试信息开关处于关闭状态。

【举例】

\# 打开生成树的所有调试信息开关。

\<Sysname\> debugging stp all

**生成树 \-- 生成树调试命令 \-- debugging stp error**

------------------------------------------------------------------------

【命令】

**[debugging stp** **error**]

**[undo debugging stp error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging stp error**]命令用来打开生成树错误调试信息开关。**undo debugging stp error**命令用来关闭生成树错误调试信息开关。

缺省情况下，生成树错误调试信息开关处于关闭状态。

表1-1 debugging stp error命令输出信息描述表

字段

描述

Failed to *String1* the STP *String2* configuration database

对STP配置数据库进行*String1*操作失败

*[String*]*1*的具体取值包括：

·write：表示写操作

·read：表示读操作

·delete：表示删除操作

*[String*]*2*的具体取值包括：

·region：表示域配置

·global：表示全局配置

·VLAN Ignore：表示VLAN Ignore配置

·interface：表示接口配置

·instance：表示实例配置

·instance-on-interface：表示接口实例配置

·VLAN list：表示VLAN列表配置

·VLAN：表示VLAN配置

·VLAN-on-interface：表示接口VLAN配置

Failed to move database(key *String*)

移动key为*String*的数据库失败*，**String*的具体取值包括：*PortName*

Failed to *String* the global *DataType* database

对全局DataType数据库进行String操作失败

String的具体取值包括：

·write：表示写操作

·read：表示读操作

·delete：表示删除操作

*[DataType*]的具体取值包括：

·control：表示控制数据

·run：表示运行数据

Failed to *String* the *DataType* database on instance *InstanceID*

对MSTI *InstanceID*的*DataType*数据库进行*String*操作失败

*[String*]的具体取值包括：

·write：表示写操作

·read：表示读操作

·delete：表示删除操作

*[DataType*]的具体取值包括：

·run：表示运行数据

Failed to *String* the *DataType* database for port*PortID(PortName)*

对端口*PortID(PortName)*的*DataType*数据库进行*String*操作失败

*[String*]的具体取值包括：

·write：表示写操作

·read：表示读操作

·delete：表示删除操作

*[DataType*]的具体取值包括：

·control：表示控制数据

·run：表示运行数据

Failed to open database(name= *String*)

打开数据库*String*失败，*String*的具体取值包括：

·eSTP：表示生效配置数据库

·lSTP：表示本地运行数据库

Received a *String* BPDU with invalid length

收到一个长度错误的*String*类型报文，*String*的具体取值包括：

·STP：表示生成树

·RSTP：表示快速生成树

·PVST：表示每VLAN生成树

·MSTP：表示多实例生成树

·TCN：表示拓扑变化通知消息

The protocol type ID is wrong

报文类型错误

The protocol version ID is wrong

报文版本错误

Port *PortID(PortName)* received an error BPDU with *String*

端口*PortID(PortName)*收到错误原因为*String*的报文，*String*的具体取值包括：

·invalid BPDU length：表示错误的报文长度

·invalid MSTIinformation：表示错误的多实例信息

·invalid RemainingHops of CIST：表示CIST错误的剩余跳数

·invalid IntRootPathCost of CIST：表示CIST错误的内部根路径开销

·retired root priority：表示过期的根优先级

·invalid Root：表示错误的总根

·invalid RegionRoot：表示错误的域根

·invalid ExtRootPathCost：表示错误的外部路径开销

·retired MSTI root priority：表示过期的多实例根优先级

·invalid RootPathCost：表示错误的根路径开销

·invalid RemainingHops of MSTI *InstanceID*：表示错误的MSTI *InstanceID*剩余跳数

·invalid IntRootPathCost of MSTI *InstanceID*：表示错误的MSTI *InstanceID*内部根路径开销

·Excess MessageAge：表示MessageAge值过大

·Invalid HelloTime：表示HelloTime值无效

·Invalid FwdDelay：表示FwdDelay值无效

BPDU's length is less than TCN\'s length

BPDU报文长度有误

Port *PortID(PortName)* failed to send packet

端口*PortID(PortName)*发送报文失败

【举例】

\# 打开生成树错误调试信息开关。

\<Sysname\> debugging stp error

\*Mar 18 14:28:41:744 2010 Sysname STP/7/ERROR:Port2(GigabitEthernet1/0/1) received an error BPDU with invalid Root

*// 端口GigabitEthernet1/0/1收到错误的BPDU报文，错误原因是报文中的根信息有误*

**生成树 \-- 生成树调试命令 \-- debugging stp event**

------------------------------------------------------------------------

【命令】

**[debugging stp** **event** [ **interface** *interface-type interface-number* ]]

**[undo debugging stp** **event** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：打开或关闭指定端口的生成树事件调试信息开关，*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，则打开或关闭全局事件调试开关，和所有端口的事件调试信息开关。

【描述】

**[debugging stp event**]命令用来打开生成树事件调试信息开关。**undo debugging stp event**命令用来关闭生成树事件调试信息开关。

缺省情况下，生成树事件调试信息开关处于关闭状态。

表1-2 debugging stp event命令输出信息描述表

字段

描述

Instance *InstanceID* enters PRS machine

全局事件调试信息：MSTI *InstanceID*进入PRS状态机

*[String* event occured on port*PortID(PortName)*]

端口*PortID(PortName)*上发生了*String*事件，*String*的具体取值包括：

·ADD VLAN：表示端口加入VLAN，VLAN ID为65535表示批量VLAN事件

·DEL VLAN：表示端口从VLAN中删除，VLAN ID为65535表示批量VLAN事件

·SPEED CHANGE：表示端口速率变化

·DUPLEX CHANGE：表示端口双工模式变化

·FAST LINK DOWN：表示端口快速down

·LINK DOWN：表示端口down

·LINK UP：表示端口up

·DEACTIVE：表示接口去激活

·DELETE：表示接口删除

·JOIN AGG：表示端口加入聚合组

·LEAVE AGG：表示端口退出聚合组

【举例】

\# 打开端口GigabitEthernet1/0/1的生成树事件调试信息开关。

\<Sysname\> debugging stp event interface gigabitethernet 1/0/1

\*Mar 18 14:28:41:887 2010 Sysname STP/7/PEVT: LINK DOWN event occured on port2(GigabitEthernet1/0/1).

*// 端口GigabitEthernet1/0/1上发生了端口down事件*

\# 打开生成树全局事件调试信息开关。

\<Sysname\> debugging stp event

\*Sep 23 09:39:24:773 2010 Sysname STP/7/PEVT: DUPLEX CHANGE event occured on port2(GigabitEthernet1/0/1).

*// 端口GigabitEthernet1/0/1上发生了双工变化事件*

\*Sep 23 09:39:24:777 2010 Sysname STP/7/PEVT: SPEED CHANGE event occured on port2(GigabitEthernet1/0/1).

*// 端口GigabitEthernet1/0/1上发生了速率变化事件*

\*Sep 23 09:39:24:783 2010 Sysname STP/7/PEVT: LINK UP event occured on port2(GigabitEthernet1/0/1).

*// 端口GigabitEthernet1/0/1上发生了链路up事件*

**生成树 \-- 生成树调试命令 \-- debugging stp fsm**

------------------------------------------------------------------------

【命令】

**[debugging stp fsm**[ [ **instance** *instance-id* \| **vlan** *vlan-id* ]  **interface** *interface-type interface-number* ]]

**[undo**[ **debugging stp** **fsm** [ **instance** *instance-id* \| **vlan** *vlan-id* ]  **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance** *instance-id*]：打开或关闭指定MSTI的生成树状态机调试信息开关，*instance-id*为MSTI的编号，取值范围为0到设备支持的最大值（最大值与设备的型号有关，请以设备的实际情况为准），0表示CIST。如果未指定本参数，则打开或关闭所有MSTI的生成树状态机调试信息开关。本参数在PVST模式下无效。

**[vlan*** vlan-id*]：打开或关闭指定VLAN的生成树状态机调试信息开关，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，则打开所有VLAN的生成树状态机调试信息开关。本参数只在PVST模式下有效。

**[interface** *interface-type interface-number*]：打开或关闭指定端口的生成树状态机调试信息开关，*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，则打开或关闭所有端口的生成树状态机调试信息开关。

【描述】

**[debugging stp fsm**]命令用来打开生成树状态机调试信息开关。**undo debugging stp fsm**命令用来关闭生成树状态机调试信息开关。

缺省情况下，生成树状态机调试信息开关处于关闭状态。

表1-3 debugging stp fsm命令输出信息描述表

字段

描述

Instance *InstanceID*'s port *PortID(PortName)* enters *String* state

VLAN *VLANID*'s port *PortID(PortName)* enters *String* state

端口*PortID(PortName)*在MSTI *InstanceID*或VLAN *VLANID*上的状态为*String*，*String*的具体取值包括：PIM%DISABLED、PIM%AGED、PIM%UPDATE、PIM%CURRENT、PIM%RECEIVE、PIM%SUPERIOR_DESIGNATED、PIM%REPEATED_DESIGNATED、PIM%INFERIOR_DESIGNATED、PIM%NOT_DESIGNATED、PIM%OTHER、PPM%CHECKING_RSTP、PPM%SELECTING_STP、PPM%SENSING；PRT%BLOCK_PORT、PRT%BACKUP_PORT、PRT%ALTERNATE_PORT、PRT%ALTERNATE_PROPOSED、PRT%ALTERNATE_AGREED、PRT%MASTER_PORT、PRT%MASTER_PROPOSED、PRT%MASTER_AGREED、PRT%MASTER_SYNCED、PRT%MASTER_RETIRED、PRT%MASTER_DISCARD、PRT%MASTER_LEARN、PRT%MASTER_FORWARD、PRT%DESIGNATED_PORT、PRT%DESIGNATED_PROPOSE、PRT%DESIGNATED_AGREED、PRT%DESIGNATED_SYNCED、PRT%DESIGNATED_RETIRED、PRT%DESIGNATED_DISCARD、PRT%DESIGNATED_LEARN、PRT%DESIGNATED_FORWARD、PRT%ROOT_PORT、PRT%ROOT_PROPOSED、PRT%ROOT_AGREED、PRT%ROOT_SYNCED、PRT%ROOT_DISCARD、PRT%ROOT_LEARN、PRT%ROOT_FORWARD、PRT%ROOT_REROOT、PRT%ROOT_REROOTED、PRT%INIT_PORT、PRT%DISABLE_PORT、PRT%DISABLED_PORT、PTX%PERIODIC、PTX%TCN、PTX%CONFIG、PTX%RSTP、PTX%MSTP_DOT1S、PTX%MSTP_LEGACY、PST%DISCARDING、PST%LEARNING、PST%FORWARDING、TCM%INACTIVE、TCM%LEARNINGT、CM%DETECTED、TCM%ACTIVE、TCM%NOTIFIED_TCN、TCM%NOTIFIED_TC、TCM%PROPAGATING和TCM%ACKNOLEDGED。各字段%之前表示状态机名称，%之后表示具体状态

Instance *InstanceID*'s port *PortID(PortName)* is selected as *String* role

VLAN *VLANID*'s port *PortID(PortName)* is selected as *String* role

端口*PortID(PortName)*在MSTI *InstanceID*或VLAN *VLANID*上的角色为*String*，*String*的具体取值包括：

·DESIGNATED：表示指定端口

·ROOT：表示根端口

·ALTERNATE：表示替换端口

·BACKUP：表示备份端口

·MASTER：表示主端口

【举例】

\# 在MSTP模式下，打开所有MSTI端口的生成树状态机调试信息开关。

\<Sysname\> debugging stp fsm

\*Mar 18 14:28:41:739 2010 Sysname STP/7/FSMSTATE:Instance 0\'s port2(GigabitEthernet1/0/1) enters PTX%PERIODIC state.

*// 端口GigabitEthernet1/0/1上的PTX状态机处于PERIODIC状态*

\*Mar 18 14:28:41:739 2010 Sysname STP/7/FSMSTATE:Instance 0\'s port2(GigabitEthernet1/0/1) enters PTX%MSTP_DOT1S state.

*// 端口GigabitEthernet1/0/1上的PTX状态机处于MSTP_DOT1S状态*

\*Mar 18 14:28:41:741 2010 Sysname STP/7/FSMSTATE:Instance 2\'s port2(GigabitEthernet1/0/1) is selected as MASTER role

*// 端口GigabitEthernet1/0/1在MSTI 2中被选举为主端口*

\# 在PVST模式下，打开所有VLAN端口的生成树状态机调试信息开关。

\<Sysname\> debugging stp fsm

\*Mar 18 14:28:41:741 2010 Sysname STP/7/MEXS:Slot=1;VLAN 2's port105(GigabitEthernet1/0/1) enters PTX%PERIODIC state.

*// 端口GigabitEthernet1/0/1在VLAN 2上处于PTX状态机中的PERIODIC状态*

\*Mar 18 14:28:41:741 2010 Sysname STP/7/MEXS:Slot=1;VLAN 2's port105(GigabitEthernet1/0/1) is selected as MASTER role

*// 端口GigabitEthernet1/0/1在VLAN 2上被指定为主端口*

**生成树 \-- 生成树调试命令 \-- debugging stp packet**

------------------------------------------------------------------------

【命令】

**[debugging stp**[ **packet** [ **receive** \| **send** ]  **vlan** *vlan-id*   **interface** *interface-type interface-number*  [ **brief** \| **verbose** ]]]

**[undo debugging stp**[ **packet** [ **receive** \| **send** ]  **vlan** *vlan-id*   **interface** *interface-type interface-number*  [ **brief** \| **verbose** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：打开或关闭接收生成树报文的调试信息开关。

**[send**]：打开或关闭发送生成树报文的调试信息开关。

**[vlan*** vlan-id*]：打开或关闭指定VLAN的生成树报文调试信息开关，*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，则打开所有VLAN的生成树报文调试信息开关。本参数只在PVST模式下有效。

**[interface** *interface-type interface-number*]：打开或关闭指定端口的生成树报文调试信息开关，*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，则打开或关闭所有端口的生成树报文调试信息开关。

**[brief**]：打开或关闭生成树报文的简要调试信息开关。

**[verbose**]：打开或关闭生成树报文的详细调试信息开关。

【描述】

**[debugging stp packet**]命令用来打开生成树报文调试信息开关。**undo debugging stp packet**命令用来关闭生成树报文调试信息开关。

缺省情况下，生成树报文调试信息开关处于关闭状态。

需要注意的是：

·如果未指定**receive**和**send**参数，则同时打开接收和发送生成树报文的调试信息开关。

·如果未指定**brief**和**verbose**参数，则打开生成树报文的简要调试信息开关。

表1-4 debugging stp packet命令输出信息描述表

字段

描述

Port *PortID(PortName)* sent *Type* packet(Length:*number*)

端口*PortID(PortName)*发送了类型为*Type*的报文，报文的长度为*Number*（单位为字节），*Type*的具体取值包括：TCN、STP、RSTP、MSTP-dot1s和MSTP-legacy

Port *PortID(PortName)* received *Type* packet(Length:*number*)

端口*PortID(PortName)*收到了类型为*Type*的报文，报文的长度为*Number*（单位为字节），*Type*的具体取值包括：TCN、STP、RSTP、MSTP-dot1s和MSTP-legacy

Port *PortID(PortName)* VLAN *VLANID* sent *Type* packet(Length:*number*)

端口*PortID(PortName)*在VLAN *VLANID*上发送了类型为*Type*的报文，报文的长度为*Number*（单位为字节），*Type*的具体取值包括：TCN、STP和RSTP

Port *PortID(PortName)* VLAN *VLANID* received *Type* packet(Length:*number*)

端口*PortID(PortName))*在VLAN *VLANID*上收到了类型为*Type*的报文，报文的长度为*Number*（单位为字节），*Type*的具体取值包括：TCN、STP和RSTP

ProtocolVersionID

协议的版本号

BPDUType

BPDU报文的类型

CIST Root ID

CIST根桥编号

External RPC

外部根路径开销

Reg Root ID

域根桥编号

Internal RPC

内部根路径开销

CIST Bridge ID

CIST桥编号

CIST Port ID

CIST端口编号

Root ID

根桥编号

Path Cost

路径开销

Bridge ID

桥编号

Port ID

端口编号

(Instance)Flags  ： (*InstanceID*)*Port-Role*[*Flag*]

收发BPDU报文的端口在MSTI *InstanceID*上的端口角色为*Port-Role*，报文类型为*FlagA*，端口的状态为*FlagB*，其中：

·*Port-Role*的具体取值包括：Mast（表示Master端口）、Altn（表示Alternate端口或Backup端口）、Root（表示根端口）和Desi（表示指定端口）

·*FlagA*的具体取值包括：Ta（表示TCA报文）、P（表示Proposal报文）、A（表示Agreement报文）和Tc（表示TC报文）

·*FlagB*的具体取值包括：F（表示Forwarding）和L（表示Learning），如果没有显示该值，则表示Discarding

PKT

报文调试信息：包括端口号、端口名称、报文出入方向是发送还是接收、报文类型、报文长度以及十六进制显示的全部报文内容

【举例】

\# 在MSTP模式下，打开所有端口的接收生成树报文的调试信息开关。

\<Sysname\> debugging stp packet receive

\*Mar 18 14:28:41:781 2010 Sysname STP/7/PKT:

Port2(GigabitEthernet1/0/1) received MSTP-legacy packet(Length: 103)

ProtocolVersionID: 03

BPDUType         : 02

CIST Root ID     : 32768.000f-e200-3700

External RPC     : 0

Reg Root ID      : 32768.000f-e200-3700

Internal RPC     : 0

CIST Bridge ID   : 32768.000f-e200-3700

CIST Port ID     : 128.2

(Instance)Flags  : (00)Desi[  A  P  ]

*// 端口GigabitEthernet1/0/1收到长度为103字节的生成树私有格式报文，并对报文进行解析得到如下信息：对端设备运行的生成树协议版本号为3，BPDU报文类型为2，CIST根桥编号为32768.000F-E200-3700，外部根路径开销为0，域根桥编号为32768.000F-E200-3700，内部根路径开销为0，CIST桥编号为32768.000F-E200-3700，CIST端口编号为128.2，MSTI编号为00，且BPDU报文是指定端口发送的Agreement和Proposal报文*

\# 在MSTP模式下，打开所有端口的发送生成树报文的详细调试信息开关。

\<Sysname\> debugging stp packet send verbose

\*Mar 18 14:28:41:782 2010 Sysname STP/7/PKT:

Port2(GigabitEthernet1/0/1) sent MSTP-legacy Packet(Length: 103)

00 00 03 02 6c 80 00 00 e0 fc 00 00 00 00 00 00

00 80 00 00 e0 fc 00 00 00 81 81 00 00 14 00 02

00 0f 00 00 00 00 40 30 30 65 30 66 63 30 30 30

30 30 30 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 ac 36 17 7f 50 28 3c

d4 b8 38 21 d8 ab 26 de 62 80 00 00 e0 fc 00 00

00 00 00 00 00 14 00

*// 端口GigabitEthernet1/0/1发送长度为103字节的生成树私有格式报文，103字节的十六进制报文内容全部显示*

\# 在PVST模式下，打开所有端口的接收生成树报文的调试信息开关。

\<Sysname\> debugging stp packet receive

\*Mar 18 14:28:41:781 2010 Sysname STP/7/PKT:

Port386(GigabitEthernet1/0/1) VLAN 2 received RSTP-legacy packet(Length: 42)

ProtocolVersionID: 03

BPDUType         : 02

Flags            : Desi[  P  ]

*// 端口GigabitEthernet1/0/1收到长度为42字节的PVST报文，并对报文进行解析得到如下信息：对端设备运行的生成树协议版本号为3，BPDU报文类型为2，VLAN编号为2，且BPDU报文是指定端口发送的Proposal报文*

\# 在PVST模式下，打开所有端口的发送生成树报文的详细调试信息开关。

\<Sysname\> debugging stp packet send verbose

\*Mar 18 14:28:41:782 2010 Sysname STP/7/PKT:

Port385(GigabitEthernet1/0/1) VLAN 2 sent RSTP Packet(Length: 42)

00 00 02 02 6c 80 00 00 e0 fc 00 00 00 00 00 00

00 80 00 00 e0 fc 00 00 00 81 81 00 00 14 00 02

00 0f 00 00 00 00 00 02 00 02

*// 端口GigabitEthernet1/0/1发送长度为42字节的PVST报文，42字节的十六进制报文内容全部显示*

**生成树 \-- 生成树调试命令 \-- debugging stp roles**

------------------------------------------------------------------------

【命令】

**[debugging stp roles**]

**[undo debugging stp roles**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging stp roles**]命令用来打开生成树端口角色变化调试信息开关。**undo** **debugging stp** **roles**命令用来关闭生成树端口角色变化调试信息开关。

缺省情况下，生成树端口角色变化调试信息开关处于关闭状态。

表1-5 debugging stp roles命令输出信息描述表

字段

描述

Instance *InstanceID*'s port *PortID(PortName)* is the currently *String* port

VLAN *VLANID*'s port *PortID(PortName)* is the current *String* port

端口*PortID(PortName)*在MSTI *InstanceID*或VLAN *VLANID*上的角色为*String*，*String*的具体取值包括：ALTERNATE、BACKUP、ROOT、DESIGNATED和MASTER

【举例】

\# 打开生成树端口角色变化调试信息开关。

\<Sysname\> debugging stp roles

\*Mar 18 14:28:41:783 2010 Sysname STP/7/ROLES: slot=6;Instance 2\'s port2(GigabitEthernet1/0/1) is currently ROOT port.

*// 端口GigabitEthernet1/0/1在MSTI 2上的端口角色被更新为根端口*

\# 在PVST模式下，打开生成树端口角色变化调试信息开关。

\<Sysname\> debugging stp roles

\*Mar 18 14:28:41:783 2010 Sysname STP/7/UPDTROLES:Slot=1; The role of ports on VLAN 2 was updated\...

\*Mar 18 14:28:41:783 2010 Sysname STP/7/ROLES: Slot=1;VLAN 2\'s port2(GigabitEthernet1/0/1) is the current ROOT port.

*// 端口GigabitEthernet1/0/1在VLAN 2上的端口角色被更新为根端口*

**生成树 \-- 生成树调试命令 \-- debugging stp tc**

------------------------------------------------------------------------

【命令】

**[debugging stp tc** [ **interface** *interface-type* i*nterface-number* ]]

**[undo debugging stp tc** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：打开或关闭指定端口的生成树TC事件调试信息开关，*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，则打开或关闭所有端口的生成树 TC事件调试信息开关。

【描述】

**[debugging stp** **tc**]命令用来打开生成树TC事件调试信息开关。**undo** **debugging stp** **tc**命令用来关闭生成树TC事件调试信息开关。

缺省情况下，生成树TC事件调试信息开关处于关闭状态。

表1-6 debugging stp tc命令输出信息描述表

字段

描述

TC event *String* occurs on Instance *InstanceID*'s port *PortID(PortName)*

TC event *String* occurs on VLAN *VLANID*'s port *PortID(PortName*

端口*PortID(PortName)*在MSTI *InstanceID*或VLAN *VLANID*上发生的TC事件为*String*，*String*的具体取值包括：

·Receiving TCN：表示接收TCN报文

·Receiving TCA：表示接收TCA报文

·Receiving TC：表示接收TC报文

·Sending TCN：表示发送TCN报文

·Sending TC：表示发送TC报文

·Sending TCA：表示发送TCA报文

·TcWhile Expiring：表示TC报文发送定时器超时

【举例】

\# 在MSTP模式下，打开所有端口的生成树TC事件调试信息开关。

\<Sysname\> debugging stp tc

\*Mar 18 14:28:41:784 2010 Sysname STP/7/TC: TC event Sending TC occurs on Instance 1\'s port2(GigabitEthernet1/0/1).

*[// MSTI 1*]*中的端口GigabitEthernet1/0/1发出了TC报文*

\*Mar 18 14:28:41:784 2010 Sysname STP/7/TC: TC event Receiving TC occurs on Instance 1\'s port2(GigabitEthernet1/0/1).

*[// MSTI 1*]*中的端口GigabitEthernet1/0/1收到了TC报文*

\# 在PVST模式下，打开所有端口的生成树TC事件调试信息开关。

\<Sysname\> debugging stp tc

\*Mar 18 14:28:41:784 2010 Sysname STP/8/PORTMSTTC: Slot=1; TC event Sending TC occurs on VLAN 1\'s port2(GigabitEthernet1/0/1).

*[// VLAN 1*]*的端口GigabitEthernet1/0/1发出了TC报文*

\*Mar 18 14:28:41:784 2010 Sysname STP/8/PORTMSTTC: Slot=1; TC event Receiving TC occurs on VLAN 1\'s port2(GigabitEthernet1/0/1).

*[// VLAN 1*]*的端口GigabitEthernet1/0/1收到了TC报文*
