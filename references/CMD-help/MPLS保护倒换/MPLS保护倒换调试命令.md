<!-- CMD-INDEX
  debugging mpls protection           | ]                | L6
  debugging tunnel-bundle             | ]                | L368
-->

**MPLS保护倒换 \-- MPLS保护倒换调试命令 \-- debugging mpls protection**

------------------------------------------------------------------------

【命令】

**[debugging mpls protection****all**[ \| ]**error**[ \| ]**event**[ \| ]**fsm **[\|]** packet** }

**[undo**]**debugging mpls protection** **[all**[ \| ]**error**[ \| ]**event**[ \| ]**fsm **[\|]** packet** }

【视图】]

用户视图]

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示MPLS保护倒换的所有调试信息开关。

**[error**]：表示MPLS保护倒换的错误调试信息开关。

**[event**]：表示MPLS保护倒换的事件调试信息开关。

**[fsm**]：表示MPLS保护倒换的有限状态机调试信息开关。

**[packet**]**：**表示MPLS保护倒换的报文调试信息开关。

【描述】

**[debugging mpls protection**]命令用来打开MPLS保护倒换的调试信息开关。**undo debugging mpls protection**命令用来关闭MPLS保护倒换的调试信息开关。

缺省情况下，所有MPLS保护倒换的调试信息开关均处于关闭状态。

表1-1 debugging mpls protection error命令输出信息描述表

字段

描述

Failed to connect to BFD.

连接BFD失败

Failed to decode message. Type: *msgtype*; length: *msglen*.

消息解码失败，消息类型为*msgtype*，消息长度为*msglen*

Received a message with invalid length *msglen*.

接收的消息长度非法，消息长度为*msglen*

Received an invalid message. Type: *msgtype*; length: *msglen*.

接收到非法的消息，消息类型为*msgtype**，*消息长度为*msglen*

Failed to send display response message.

发送显示回应消息失败

Failed to respond to HA event (*event*).

回应HA事件失败，HA事件类型为*event*

Failed to save global configurations to DBM.

向DBM存储全局配置失败

Failed to save PS configurations (PGID: *pgid*) to DBM.

DBM存储PS配置失败，保护组ID为*pgid*

Failed to delete PS configurations (PGID: *pgid*) from DBM.

从DBM中删除PS配置失败，保护组ID为*pgid*

Failed to process remote event (*event*).

处理远端事件失败，远端事件为*event*

Failed to recover protection group (PGID: *pgid*) from DBM.

二进制恢复保护组信息失败，保护组ID为*pgid*

Failed to send configuration response message.

发送配置回应消息失败

Failed to create the timer.

创建定时器失败

Failed to reset the timer.

重置定时器失败

Failed to set the timer (sec *sec*, msec *msec*) .

设置定时器时间失败，时间为*sec*秒，*msec*毫秒

Failed to process HA upgrade event because activating some modules failed.

由于激活某些模块失败，导致处理HA升级事件失败

表1-2 debugging mpls protection event命令输出信息描述表

字段

描述

Sent smooth event (*event-type*) to MPLSPS. Result: *result*.

向内核PS发送smooth事件，smooth事件类型为*event-type*，返回值为*result*

Sent session add event of protection group (PGID: *pgid*) to MPLSPS

向内核PS发送会话添加事件，保护组ID为*pgid*

Processed interface delete event. Interface index: *ifindex*.

处理接口删除事件，接口索引为*ifindex*

Downloaded protection group (PGID: *pgid*) to MPLSPS. Socket: *sockfd*; Length: *length*.

向内核PS下发保护组表项，保护组ID为*pgid*，与内核PS连接的Socket为*sockfd*，向内核PS下发数据的长度为*length*

Received an HA message (Type: *type*).

接收HA消息，消息类型为*type*

Sent an HA message (Type: *type*).

发送HA消息，消息类型为*type*

Received an event (*event*) from TBDL.

从TBDL接收到事件*event*

Tunnel interface (*tnl-index*) for receiving protocol packets is wrong.

接收协议报文的Tunnel接口不正确，Tunnel接口的索引为*tnl-ifindex*

Received an invalid protocol message. Interface index: *ifindex*.

从接口*ifindex*接收到了一个无效的协议报文

Received a BFD event (*event*) from interface *ifindex*.

从接口*ifindex*接收到了一个BFD事件*event*

表1-3 debugging mpls protection fsm命令输出信息描述表

字段

描述

Received a local event (*event*) (PGID: *pgid*).

接收本地事件*event*，保护组ID为*pgid*

Received a remote event (*event*) (PGID: *pgid*).

接收远端事件*event*，保护组ID为*pgid*

Changed the session state from *state1* to *state2* (PGID: *pgid*).

将会话状态从*state1*改变为*state2*，保护组ID为*pgid*

Created the timer (Timer type: *type*) successfully.

成功创建定时器，定时器类型为*type*

Deleted the timer (Timer type: *type*) successfully.

成功删除定时器，定时器类型为*type*

Timer expires (Timer type: type).

类型为*type*的定时器超时

表1-4 debugging mpls protection packet命令输出信息描述表

字段

描述

The configurations of the protection group (PGID: *pgid*) on the local and remote devices mismatched.

两端保护组配置不一致，本地保护组ID为*pgid*

Received

接收到PSC控制报文

Sent

发送PSC控制报文

Protection Group ID

保护组ID

Channel Type

通道类型，该值固定为0x24

Protection Type

保护类型

Revertive Mode

回切模式

Request

请求类型

Fault Path

缺陷路径

Data Path

传输路径

【举例】

\# 打开MPLS保护倒换的错误调试信息开关。关闭BFD进程后，设备上打印如下调试信息。

\<Sysname\> debugging mpls protection error

\<Sysname\> process shutdown name bfd

%May  7 11:01:22:257 2013 Sysname SCMD/6/JOBINFO: -MDC=1; The service BFD is stopping\...

%May  7 11:01:22:271 2013 Sysname SCMD/6/JOBINFO: -MDC=1; The service BFD is stopped\...

\*May  7 11:01:26:050 2013 Sysname PS/7/ERROR: -MDC=1; Failed to connect to BFD.

*// 连接BFD失败。*

\# 打开MPLS保护倒换的事件调试信息开关。关闭Tunnel-Bundle接口的成员接口后，设备上打印如下调试信息。

\<Sysname\> debugging mpls protection event

\<Sysname\> system-view

Sysname interface tunnel-bundle 200

Sysname-Tunnel-Bundle200 display this

\#

interface Tunnel-Bundle200 protection oneplusone

 member interface Tunnel0

 member interface Tunnel1 protection

\#

return

Sysname-Tunnel-Bundle200 quit

Sysname interface tunnel 0

Sysname-Tunnel0 shutdown

%Jul  1 09:55:28:220 2013 Sysname IFNET/3/PHY_UPDOWN: -MDC=2; Tunnel0 link status is down.

\*Jul  1 09:55:28:220 2013 Sysname PS/7/EVENT: -MDC=2; Downloaded protection group (PGID: 200) to MPLSPS. Socket: 22; Length: 32.

*// 向内核PS下发保护组表项，保护组ID为200，与内核的连接的Socket为22，向内核下发数据的长度为32字节*

\*Jul  1 09:55:28:222 2013 Sysname PS/7/EVENT: -MDC=2; Received an event (Update) from TBDL.

*[//*]*从TBDL模块接收到更新事件。*

\# 打开MPLS保护倒换的有限状态机调试信息开关。在已创建的Tunnel-Bundle接口下执行锁定倒换命令后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls protection fsm

\<Sysname\> system-view

Sysname interface tunnel-bundle 200

Sysname-Tunnel-Bundle200 display this

\#

interface Tunnel-Bundle200 protection oneplusone

 member interface Tunnel0

 member interface Tunnel1 protection

\#

return

Sysname-Tunnel-Bundle200 protection switch lock

\*Jul  1 10:22:11:819 2013 Sysname PS/7/FSM: -MDC=2; Received a local event (Lockout of protection(LO)) (PGID: 200).

*// 保护组200接收到本地LO事件。*

\*Jul  1 10:22:11:819 2013 Sysname PS/7/FSM: -MDC=2; Changed the session state from 7 to 2 (PGID: 200).             

*// 保护组200的会话状态从7变为2。*

\# 打开MPLS保护倒换的报文转发调试信息开关。在已创建的Tunnel-Bundle接口下执行锁定倒换命令后，设备上将打印如下调试信息。

\<Sysname\> debugging mpls protection packet

\<Sysname\> system-view

Sysname interface Tunnel-Bundle 200

Sysname-Tunnel-Bundle200 display this

\#

interface Tunnel-Bundle200 protection onetoone

 member interface Tunnel0

 member interface Tunnel1 protection

 protection switching-mode bidirectional

\#

return

Sysname-Tunnel-Bundle200 protection switch lock

\*Jul  1 12:28:04:767 2013 Sysname PS/7/PACKET: -MDC=2; Sent:                       

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--                                                     

Protection Group ID : 200                                                      

Channel Type        : 36                                                       

Protection Type     : 3                                                        

Revertive Mode      : 1                                                        

Request             : 14                                                       

Fault Path          : 0                                                        

Data Path           : 0               

*// 发送PSC控制报文，并打印报文内容。*

**MPLS保护倒换 \-- MPLS保护倒换调试命令 \-- debugging tunnel-bundle**

------------------------------------------------------------------------

【命令】

**[debugging tunnel-bundle ****all **[\|]** error **[\|]** event **}

**[undo debugging tunnel-bundle ****all **[\|]** error **[\|]** event **}

【视图】]

用户视图]

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示Tunnel-Bundle接口的所有调试信息开关。

**[error**]：表示Tunnel-Bundle接口的错误调试信息开关。

**[event**]：表示Tunnel-Bundle接口的事件调试信息开关。

【描述】

**[debugging tunnel-bundle**]命令用来打开Tunnel-Bundle接口的调试信息开关。**undo debugging tunnel-bundle**命令用来关闭Tunnel-Bundle接口的调试信息开关。

缺省情况下，所有Tunnel-Bundle接口的调试信息开关均处于关闭状态。

表1-5 debugging tunnel-bundle error命令输出信息描述表

字段

描述

 

Failed to process HA upgrade event because activating some modules failed.

由于激活部分模块失败，导致HA升级事件处理失败

 

Invalid HA message type.

在进行HA时，HA消息类型为无效值

 

Failed to create ifindex for tunnel bundle interface (*bundle-number*).

为编号为*bundle-number*的Tunnel-Bundle接口创建接口索引失败

 

Failed to destroy ifindex for tunnel bundle interface (*bundle-number*).

删除编号为*bundle-number*的Tunnel-Bundle接口的接口索引失败

 

Failed to save tunnel bundle interface (*bundle-number*) to DBM.

DBM存储Tunnel-Bundle接口失败，捆绑接口编号为*bundle-number*

Failed to delete tunnel bundle interface (*bundle-number*) from DBM.

DBM中删除Tunnel-Bundle接口失败，捆绑接口编号为*bundle-number*

Failed to save member (*tnl-number*) to DBM.

DBM存储成员接口失败，成员接口编号为*tnl-number*

Failed to delete member (*tnl-number*) from DBM.

DBM删除成员接口失败，成员接口编号为*tnl-number*

The tunnel bundle interface number (*bundle-number*) is invalid.

捆绑接口的编号*bundle-number*为无效值

Failed to send display response message.

发送显示回应消息失败

Failed to respond to HA. Event: *ResponseType.*

响应HA 事件失败，事件类型为*ResponseType*

Failed to recover tunnel bundle interface (*bundle-number*) from DBM.

DBM中恢复Tunnel-Bundle接口失败，捆绑接口编号为*bundle-number*

Failed to register to *module.*

向模块*module*注册失败，*module*取值包括LSM、PS和L3V

Failed to start reconnect timer.

重启重连定时器失败

Failed to flush to LSM*.

向LSM模块flush数据失败

Failed to set the timer.

设置定时器失败

Failed to send configuration response message.

发送配置回应消息失败

表1-6 debugging tunnel-bundle event命令输出信息描述表

字段

描述

 

Received an interface event (*event*) on interface *ifIndex.*

接收到接口*ifIndex*的接口事件*event*

Updated the information of tunnel bundle interface *ifIndex* to KTBDL.

向内核更新Tunnel-Bundle接口*ifIndex*的信息

Notified KTBDL to add the member interface *member-ifindex* to the tunnel bundle interface *bundle-ifindex*.

向内核下发成员口添加，捆绑接口的接口索引为*ifIndex*

Notified KTBDL to delete the member interface *member-ifindex* from the tunnel bundle interface *bundle-ifindex*.

向内核下发成员口删除，捆绑接口的接口索引为*ifIndex*

Sent an HA message (Type: *MsgType*).

发送HA消息，消息类型为*MsgType*

Received an HA message (Type: *MsgType*).

接收HA消息，消息类型为*MsgType*

Sent bundle delete event of tunnel bundle interface *ifindex* to *module*.

向*module*模块下发删除事件，捆绑接口的接口索引为*ifIndex*，*module*的取值为LSM或PS

Sent bundle update event of tunnel bundle interface *ifindex* to *module*.

向*module*模块下发更新事件，捆绑接口的接口索引为*ifIndex*，*module*的取值为LSM或PS

Received a message with an unknown TLV (type: *tlv-type*).

接收到了一个带有未知TLV的消息，TLV的类型值为*tlv-type*

 

Sent smooth (Type: *event-type*) event to *module*. Result: *result*

向*module*模块下发平滑事件，事件类型为*event-type*，*module*的取值为PS或LSM，结果为*result*

 

【举例】

\# 打开Tunnel-Bundle接口的错误调试信息开关。关闭LSM进程时，设备上会打印如下调试信息。

\<Sysname\> debugging tunnel-bundle error

\<Sysname\> process shutdown name lsmd

\*Feb 6 16:13:36:999 2013 Sysname TBDL/7/ERROR: -MDC=1; Failed to Register to LSM.

*// 向LSM进程注册失败。*

\# 打开Tunnel-Bundle接口的事件调试信息开关。创建Tunnel-Bundle接口，并为其指定成员接口后，设备上打印如下调试信息。

\<Sysname\> debugging tunnel-bundle event

\<Sysname\> system-view

Sysname interface tunnel-bundle 200 protection onetoone

Sysname-Tunnel-Bundle200 member interface tunnel 0

\*Jul  1 09:51:39:738 2013 Sysname TBDL/7/EVENT: -MDC=1; Notified KTBDL to add the member interface 5506 to the tunnel bundle interface 5505.                           

*// 通知内核为接口索引为5505的Tunnel-Bundle接口添加成员接口，成员接口的接口索引为5506。*

\*Jul  1 09:51:39:739 2013 Sysname TBDL/7/EVENT: -MDC=1; Sent bundle update event of tunnel bundle interface 5505 to LSM.

*// 向LSM下发Tunnel-Bundle接口（5505）的更新事件。*
