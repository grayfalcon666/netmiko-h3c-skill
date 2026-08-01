<!-- CMD-INDEX
  debugging macsec                    | 用户视图             | L7
  debugging macsec mka fsm            | 用户视图             | L211
  debugging macsec mka packet         | 用户视图             | L311
-->

**MACsec \-- MACsec调试命令 \-- debugging macsec**

------------------------------------------------------------------------

**[debugging macsec**]命令用来打开MACsec调试信息开关。

**[undo debugging macsec**]命令用来关闭MACsec调试信息开关。

【命令】

**[debugging macsec **[{ **all** \| **error** \| **event** }]]

**[undo debugging macsec **[{ **all** \| **error** \| **event** }]]

【缺省情况】

MACsec调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有的MACsec调试信息开关，包括错误调试信息开关、事件调试信息开关和MKA调试信息开关。

**[error**]：表示MACsec错误调试信息开关。

**[event**]：表示MACsec事件调试信息开关。

【描述】

表1-1 debugging macsec error命令输出信息描述表

字段

描述

Received an invalid packet (type: *invalid type*) on interface *interface-type interface-number*.

接口*interface-type interface-number*接收了错误的报文，*invalid type*表示错误类型，包括以下取值：

·invalid destination MAC address：表示非法的目的MAC地址

·invalid packet length：表示无效的报文长度

·incompatible MKA version ID：表示不兼容的MKA版本

·incompatibleEAPOLversion ID：表示不兼容的EAPOL版本

·length error in basic parameter set：表示基本参数集长度错误

·unknown algorithm agility：表示不可识别的算法灵活度

·unknown CKN：表示不可识别的CKN

·mismatched ICV：表示错误的ICV

·SCI conflict：表示收到的报文SCI和本端SCI相同

·invalid message number：表示非法的消息编号

·invalid SCI：表示非法的SCI

Failed to send packets on interface *interface-type interface-number*.

接口*interface-type interface-number*发送报文失败

Failed to get the RxSC PN on interface *interface-type interface-number*.

获取接口*interface-type interface-number*的接收通道PN（Packet Number）值失败

Failed to get the next TxSC PN on interface *interface-type interface-number*.

获取接口*interface-type interface-number*的发送通道的下一个PN值失败

Failed to set the link status on interface *interface-type interface-number*.

设置接口*interface-type interface-number*的链路状态失败

Failed to *operate* *object* on interface *interface-type interface-number*.

操作接口*interface-type interface-number*失败

*[operate*]表示操作类型，包括以下取值：

·create：表示创建

·modify：表示修改

·delete：表示删除

*[object*]表示操作对象，包括以下取值：

·TxSC：表示发送SC

·RxSC：表示接收SC

·TxSA：表示发送SA

·RxSA：表示接收SA

表1-2 debugging macsec event命令输出信息描述表

字段

描述

Received *event* event on interface *interface-type interface-number*.

接口*interface-type interface-number*收到了事件

*[event*]表示接口事件类型，包括以下取值：

·ACTIVE：表示接口激活事件

·DEACTIVE：表示接口去激活事件

·DELETE：表示接口删除事件

·UP：表示接口UP事件

·DOWN：表示接口DOWN事件

·MACCHANGE：表示接口MAC变化事件

Received *event* event of slot *slot-id*.

收到板事件，*slot-id*表示槽位号或成员编号

*[event*]表示事件类型，包括以下取值：

·INSERT：表示插入事件

·REMOVE：表示拔出事件

Received dot1x *event* event on interface *interface-type interface-number*.

接口*interface-type interface-number*收到了802.1X的事件。*event*表示事件类型，包括以下取值：

·USER_ONLINE：表示用户上线事件

·USER_OFFLINE：表示用户下线事件

The agent slot received a packet for a slot that was in the ISSU process.

代理板收到了ISSU重定向过来的报文

Connection status changed to *state* because of *reason* on interface *interface-type interface-number*.

由于*reason*，导致接口*interface-type interface-number*连接状态变化。*state*表示连接状态，包括以下取值：

·Unknown：表示未知状态

·Pending：表示挂起状态

·Unauthenticated：表示未认证状态

·Authenticated：表示认证状态

·Secured：表示安全状态

*[reason*]表示原因，包括以下取值：

·CP initialization：表示受控端口初始化

·no active instance：表示没有激活的实例

The MKA participant with CKN *ckn* aged out on interface *interface-type interface-number.*

接口*interface-type interface-number*上CKN为*ckn*的MKA参与者老化

The *type* peer with SCI *sci*, CKN *ckn*, and MI *mi* aged out on interface *interface-type interface-number.*

接口*interface-type interface-number*上SCI为*sci*、CKN为*ckn*和MI为*mi*的peer老化。*type*表示peer的类型，包括以下取值：

·live：表示已经学习到的peer

·potential：表示正在协商中的peer

【举例】

\# 在设备上打开MACsec错误调试信息开关。使能MKA功能且配置了PSK的接口GigabitEthernet1/0/1接收到非法的加密报文时，输出如下调试信息。

\<Sysname\> debugging macsec error

\*Aug  6 19:02:52:755 2013 Sysname MACSEC/7/ERROR: -MDC=1; Received an invalid packet (type: mismatched ICV) on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1收到非法的PDU报文，原因是错误的ICV *

\# 在设备上打开MACsec事件调试信息开关。在设备的GigabitEthernet1/0/1接口上执行**shutdown**命令时，输出如下调试信息。

\<Sysname\> debugging macsec event

\*Aug 10 18:35:29:602 2013 Sysname MACSEC/7/EVENT: -MDC=1; Received DOWN event on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上发生了端口Down事件*

**MACsec \-- MACsec调试命令 \-- debugging macsec mka fsm**

------------------------------------------------------------------------

**[debugging macsec mka fsm**]命令用来打开端口的MKA状态机调试信息开关。

**[undo debugging macsec mka fsm**]命令用来关闭端口的MKA状态机调试信息开关。

【命令】

**[debugging macsec mka fsm ** **interface** *interface-type interface-number* ]

**[undo debugging macsec mka fsm ** **interface** *interface-type interface-number* ]

【缺省情况】

端口的MKA状态机调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：打开指定端口的MKA状态机调试信息开关，*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，则打开所有端口的MKA状态机调试信息开关。

【描述】

表1-3 debugging macsec mka fsm命令输出信息描述表

字段

描述

Transitioned to *state* state on interface **** *interface-type interface-number.*

接口*interface-type interface-number*的状态发生迁移，*state*表示迁移到的状态，包括以下取值：

·CP_CHANGE：表示端口连接状态变化，状态机准备迁移

·CP_ALLOWED：表示端口未认证，允许收发未加密报文

·CP_AUTHENTICATED：表示端口通过认证，允许收发未加密报文

·CP_SECURED：表示端口采用安全通信方式，准备安装收发SA

·CP_RECEIVE：表示端口安装接收SA成功

·CP_RECEIVING：表示端口入方向就绪，可接收新SA加密的报文

·CP_READY：表示端口等待Key Server通知，准备安装发送SA

·CP_TRANSMIT：表示端口使能发送SA

·CP_TRANSMITTING：表示端口出方向就绪，可以发送新SA加密的报文

·CP_ABANDON：表示端口丢弃了刚生成的SA

·CP_RETIRE：表示端口出入方向都已就绪，可使用新SA收发报文

*[timer* timer expired on interface *interface-type interface-number*.]

接口*interface-type interface-number*的定时器超时。*timer*表示定时器类型，包括以下取值：

·RetireWhen：新的SAK应用于发送SC后，强制在定时器溢出前不再应用新的SAK用于发送SC。定时器超时值为3秒。

·TransmitWhen：Key Server应用新的SAK用于发送SC前，需等待对端通知已应用新的SAK用于接收SC。为了防止Key Server无限期的等待对端通知，定时器溢出前，Key Server必须收到通知。定时器超时值为6秒。

【举例】

\# 在设备上打开MKA状态机调试信息开关。当设备接口GigabitEthernet1/0/1的SAK刷新时，输出如下调试信息。

\<Sysname\> debugging macsec mka fsm

\*Sep 12 13:27:51:780 2013 Sysname MACSEC/7/FSM: -MDC=1; Transferred to CP_RECEIVE state on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上的状态机处于CP_RECEIVE状态*

\*Sep 12 13:27:51:781 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_RECEIVING state on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上的状态机处于CP_RECEIVING状态*

\*Sep 12 13:27:51:786 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_TRANSMIT state on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上的状态机处于CP_TRANSMIT状态*

\*Sep 12 13:27:51:786 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_TRANSMITTING state on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上的状态机处于CP_TRANSMITTING状态*

\*Sep 12 13:27:55:780 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_RETIRE state on interface GigabitEthernet1/0/1.

*[/ /*]*接口GigabitEthernet1/0/1上的状态机处于CP_RETIRE状态*

**MACsec \-- MACsec调试命令 \-- debugging macsec mka packet**

------------------------------------------------------------------------

**[debugging macsec mka packet**]命令用来打开端口的MKA报文调试信息开关。

**[undo debugging macsec mka packet**]命令用来关闭端口的MKA报文调试信息开关。

【命令】

**[debugging macsec mka packet**[ [ **send** \| **receive** ]  **interface** *interface-type interface-number*   **verbose** ]]

**[undo debugging macsec mka packet **[[ **send** \| **receive** ]  **interface** *interface-type interface-number* ]]

【缺省情况】

端口的MKA报文调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[send**]：打开发送MKA报文的调试信息开关。

**[receive**]：打开接收MKA报文的调试信息开关。

**[interface** *interface-type interface-number*]：打开指定端口的MKA报文调试信息开关，*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，则打开所有端口的MKA报文调试信息开关。

**[verbose**]：打开MKA报文的详细调试信息开关。如果未指定本参数，则打开MKA报文的摘要调试信息开关。

【使用指导】

需要注意的是，如果未指定**send**和**receive**参数，则表示同时打开发送和接收MKA报文的调试信息开关；**debugging all**和**debugging macsec all**命令优先打开MKA报文的摘要调试信息开关。

表1-4 debugging macsec mka packet命令输出信息描述表

字段

描述

Sent******a MACsec Packet (length: *length*) on interface **** *interface-type interface-number*.

接口*interface-type interface-number*发送报文，报文长度是*length*

Received a MACsec Packet (length: *length*) on interface interface-type interface-number

接口*interface-type interface-number*收到报文，报文长度是*length*

Basic parameters

基本参数集信息

Live Peer List parameters

Live Peer List参数集信息

Potential Peer List parameters

Potential Peer List参数集信息

Distributed SAK parameters

SAK分发参数集信息

SAK Use parameters

SAK USE参数集信息

Tx priority

报文发送端的优先级

Key Server

是否是Key Server，Yes表示是，No表示不是

MACsec desire

接口是否期望对发送的数据帧进行MACsec保护，Yes表示期望保护，No表示不期望保护

MACsec capability

发送端的MACsec能力，取值如下：

·0：表示不支持MACsec功能

·1：表示只支持完整性服务，不支持机密性服务

·2： 表示支持完整性服务，可选择支持机密性服务（加密偏移量只能为0）

·3： 表示支持完整性服务，可选择支持机密性服务（加密偏移量可支持0，30及50）

MI

Live Peer或Potential Peer的成员ID，在基本参数集中表示本端的成员ID，在Live Peer或Potential Peer参数集中表示对端的成员ID

MN

消息编号，在基本参数集中表示本端的消息标号，在Live Peer或Potential Peer参数集中表示对端的消息编号

CKN

CAK的标识，为1～32个字节的十六进制字符

Plain Tx

是否采用明文进行发送，Yes表示明文发送，No表示密文发送

Plain Rx

是否采用明文进行接收，Yes表示明文接收，No表示密文接收

Latest Key's AN

最近SAK的SA编号

Latest Key for Tx

最近SAK是否用于发送，Yes表示用于发送，No表示不用于发送

Latest Key for Rx

最近SAK是否用于接收，Yes表示用于接收，No表示不用于接收

Latest Key Server's MI

最近SAK的Key Server的成员ID

Latest KN

最近SAK的编号

Latest LPN

最近SAK的最小可接受报文编号

Old Key's AN

旧的SAK的SA编号

Old Key for Tx

旧的SAK是否用于发送，Yes表示用于发送，No表示不用于发送

Old Key for Rx

旧的SAK是否用于接收，Yes表示用于接收，No表示不用于接收

Old Key Server's MI

旧的SAK的Key Server成员ID

Old KN

旧的SAK的编号

Old LPN

旧的SAK的最小可接受报文编号

Distributed SAK's AN

分发SAK所属SA的编号，取值范围是0～3

Confidentiality offset

加密偏移,取值如下：

·Unused：表示使用明文通信,不使用MACsec加密功能

·0：表示使用加密偏移，偏移值为0

·30：表示使用加密偏移，偏移值为30

·50：表示使用加密偏移，偏移值为50

SAK No.

SAK的编号

Wrapped SAK

经过AES-CMAC算法加密的SAK

【举例】

\# 在设备上打开MKA报文的摘要调试信息开关。当设备的接口GigabitEthernet1/0/1和对端建立会话后，输出如下调试信息。

\<Sysname\> debugging macsec mka packet

\*Nov 11 10:02:55:374 2013 Sysname MACSEC/7/PKT: -MDC=1;

Received a MACsec Packet (length: 120) on interface GigabitEthernet1/0/1.

Basic Parameters

Tx priority           : 0

MACsec desire         : No

Key Server            : Yes

MACsec capability     : 3

MI                    : 1F777A1092C1702A19FC9450

MN                    : 21

CKN                   : 1234

SAK Use parameters

Plain Tx              : No

Plain Rx              : No

Old Key\'s AN          : 0

Old Key for Tx        : Yes

Old Key for Rx        : Yes

Old KN                : 1

Old LPN               : 131

Old Key Server's MI   : 1F777A1092C1702A19FC9450

Live Peer List parameters

MI                    : 229DAD7854B5E6FA42124793

MN                    : 21

*[//*]*接口GigabitEthernet1/0/1接收对端报文，长度为120字节，对报文进行解析得到如下信息：接收的报文编号是21，成员ID是1F777A1092C1702A19FC9450，对端是Key Server，优先级为0，需要加密保护，MACsec能力是3，CKN是1234，并有一个Live Peer，即本端，是Client，报文编号是21，成员ID是229DAD7854B5E6FA42124793，使用Old key加解密发送和接收的报文，Old key的编号是1，LPN是131。*

\# 在设备上打开MKA报文的详细调试信息开关。当设备的接口GigabitEthernet1/0/1和对端建立会话后，输出如下调试信息。

\<Sysname\> debugging macsec mka packet verbose

\*Nov 11 10:08:06:375 2013 Sysname MACSEC/7/PKT: -MDC=1;

Sent a MACsec Packet (length: 120) on interface GigabitEthernet1/0/1.

03 05 00 74 01 00 70 1e 00 0c 29 94 b7 5c 00 07

22 9d ad 78 54 b5 e6 fa 42 12 47 93 00 00 00 b3

00 80 c2 01 12 34 00 00 03 07 00 28 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1f 77 7a 10 92 c1 70 2a 19 fc 94 50 00 00 00 02

00 00 00 9d 01 00 00 10 1f 77 7a 10 92 c1 70 2a

19 fc 94 50 00 00 00 b0 cc 55 07 84 34 6d 7f 74

26 8e 99 bd 42 45 4e 4c

*// 接口GigabitEthernet1/0/1发送的长度为120字节的MKA报文内容*
