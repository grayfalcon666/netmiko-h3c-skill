
**会话管理 \-- 会话管理调试命令 \-- debugging session aging-process**

------------------------------------------------------------------------

【命令】

**[debugging session aging-process** **event** [ **acl** *acl-number* ]]

**[undo debugging session aging-process event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl** *acl-number*]：指定匹配会话的ACL规则。其中，*acl-number*表示ACL编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。

【描述】

**[debugging session aging-process**]命令用来打开会话管理的老化队列处理调试信息开关。**undo debugging session aging-process**命令用来关闭会话管理的老化队列处理调试信息开关。

缺省情况下，会话管理的老化队列处理调试信息开关处于关闭状态。

表1-1 debugging session aging-process命令输出信息描述表

字段

描述

Tuple5(EVENT):

*[srcIP*]/*srcPort*\--\>*destIP*/*destPort*(*ProtoType*)

会话的五元组：

源IP/源端口\--\>目的IP/目的端口（传输层协议类型（协议号））

Aging: *PRO_STATE*

协议状态，包括如下几种：

·PERSIST

·TCP_SYN_SENT

·TCP_SYN_RECV

·TCP_ESTABLISHED

·TCP_FIN_WAIT

·TCP_CLOSE_WAIT

·TCP_LAST_ACK

·TCP_TIME_WAIT

·TCP_CLOSE

·TCP_SYN_SENT2

·UDP_OPEN

·UDP_READY

·ICMP_REQUEST

·ICMP_REPLY

·ICMPV6_REQUEST

·ICMPV6_REPLY

·UDPLITE_OPEN

·UDPLITE_READY

·SCTP_CLOSED

·SCTP_COOKIE_WAIT

·SCTP_COOKIE_ECHOED

·SCTP_ESTABLISHED

·SCTP_SHUTDOWN_SENT

·SCTP_SHUTDOWN_RECD

·SCTP_SHUTDOWN_ACK_SENT

·DCCP_REQUEST

·DCCP_RESPOND

·DCCP_PARTOPEN

·DCCP_OPEN

·DCCP_CLOSEREQ

·DCCP_CLOSING

·DCCP_TIMEWAIT

·RAWIP_OPEN

·RAWIP_READY

·FTP

·DNS

·SIP

【举例】

\# 在启用了ASPF的设备上打开会话管理的老化队列处理调试信息开关，当有相应会话建立并进入老化队列后，将输出如下调试信息。

\<Sysname\> debugging session aging-process

\<Sysname\> ping 192.168.1.58

\*May 27 10:30:28:846 2011 Sysname SESSION/7/AGING: -MDC=1;

 Tuple5(EVENT): 3.3.3.2/2048\--\>3.3.3.1/3(icmp(1))

 Aging: ICMP_REQUEST

*// 发起方为3.3.3.2，响应方为3.3.3.1的ICMP会话，处于协议状态为ICMP_REQUEST的老化队列*

**会话管理 \-- 会话管理调试命令 \-- debugging session config**

------------------------------------------------------------------------

【命令】

**[debugging session config**[ { **all** \| **error** \| **event** }]]

**[undo debugging session config**[ { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging session config**]命令用来打开会话配置处理调试信息开关。**undo debugging session config**命令用来关闭会话配置处理调试信息开关。

缺省情况下，会话配置处理调试信息开关处于关闭状态。

表1-2 debugging session config error命令输出信息描述表

字段

描述

Failed to send ioctl message to slot *slot-id*, message type: *msg-type*.

向板*slot-id*发送ioctl消息失败，消息类型为*msg-type*

表1-3 debugging session config event命令输出信息描述表

字段

描述

Received config message, message type: *msg-type*.

收到配置消息，消息类型为*msg-typ*e，包括如下取值：

·0：设置应用层老化时间

·1：设置传输层协议老化时间

·2：设置接口下的日志策略

·3：设置会话日志流量阈值

·4：设置会话日志时间阈值

·5：设置最大会话数限制

·6：设置长连接会话

·7：设置调试信息开关

·8： 获取应用层老化时间

·9：获取传输层协议老化时间

·10：获取调试信息开关

·11：无效消息类型

·12：获取连接数限制调试信息

·13：设置连接数限制调试信息

·14：添加连接数限制策略

·15：删除连接数限制策略

·16：添加连接数限制规则

·17：删除连接数限制规则

·18：应用连接数限制策略

·19：取消应用连接数限制策略

·20：获取连接数限制策略

·21：获取下一个连接数限制策略

·22：获取连接数限制策略应用的接口列表

·23：获取所有策略计数

Received slot insert message, slot number: *slot-id*.

收到单板插入事件，单板号为*slot-id*

Received interface event message, interface:*interface-type interface-num*, event: *event-type*.

收到接口事件，接口名为*interface-type interface-num*，事件类型为*event-type*

Received ACL event message, ACL version: *version*.

收到ACL事件，ACL版本为*version*

Received ioctl message, message type: *config-type*

收到ioctl消息，消息类型为*config-type*，包括以下取值：

·set AppAging：设置应用协议老化时间

·set L4Aging：设置四层协议老化时间

·set LogPolicy：设置会话日志的输出策略

·set LogFlow：设置输出会话日志的流量阈值

·set LogTime：设置输出会话日志的时间阈值

·set PersistSession：设置长连接会话

·set Debug：使能debug开关

·get SpecInfo：获取产品定制信息

·reset Session：删除会话表

·reset Relation：删除会话关联表

·reset Statistics：删除会话统计计数

·notify ACLChange：通知ACL规则变化

·notify IfActive：通知接口激活

·sync GloablCfg：同步全局配置

·sync IfCfg：同步接口配置

·sync start：配置同步开始

·sync end：配置同步结束

【举例】

\# 打开所有会话配置处理调试开关。

\<Sysname\> debugging session config all

\# 配置FTP协议老化的会话时间时间为50000秒。

Sysname session aging-time application ftp 50000

\*Aug 31 14:54:19:617 2011 Sysname SESSION/7/EVENT: -MDC=1; Received config message, message type: 0.

\*Aug 31 14:54:19:617 2011 Sysname SESSION/7/CONFIG: -MDC=1; Received ioctl message, message type: set AppAging.

*// 收到一个配置消息，消息类型为0*

**会话管理 \-- 会话管理调试命令 \-- debugging session ext-info**

------------------------------------------------------------------------

【命令】

**[debugging session ext-info **[{ **all** \| **event** \| **error** } [ **acl** *acl-number* ]]]

**[undo debugging session ext-info **[{ **all** \| **event** \| **error** }]]

【视图】

用户视图

【参数】

**[all**]：表示扩展信息的所有调试信息开关。

**[event**]：表示扩展信息的事件调试信息开关。

**[error**]：表示扩展信息的错误调试信息开关。

**[acl** *acl-number*]：指定匹配会话的ACL规则。其中，*acl-number*表示ACL编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。

【描述】

**[debugging session ext-info**]命令用来打开会话管理的扩展信息调试开关。**undo debugging session ext-info**命令用来关闭会话管理的扩展信息调试开关。

缺省情况下，会话管理的扩展信息调试开关处于关闭状态。

表1-4 debugging session ext-info event命令输出信息描述表

字段

描述

Add

扩展信息操作类型：添加扩展信息

Del

扩展信息操作类型：删除扩展信息

Get

扩展信息操作类型：获取扩展信息

*[module*]

业务模块，包括以下几种：

·NAT

·ASPF

·ALG

·STAT（攻击防范）

·TCPPROXY

·ENGINE（会话引擎）

·P2P

·LB

·FLOW_REDIRECT

·FLT6

·NATPT

·CONNLMT

·PBR（策略路由）

·DDOS

·SRVASST（Server Assistant）

·SESSIONLOG

Tuple5(EVENT):

*[srcIP*]/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(Proto number)*)

会话的五元组：

源IP/源端口\--\>目的IP/目的端口（传输层协议类型（协议号））

表1-5 debugging session ext-info error命令输出信息描述表

字段

描述

Add

扩展信息操作类型：添加扩展信息

Del

扩展信息操作类型：删除扩展信息

Get

扩展信息操作类型：获取扩展信息

*[module* unknown]

业务模块*module*未注册

Tuple5(EVENT):

*[srcIP*]/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(Proto number)*)

会话的五元组：

源IP/源端口\--\>目的IP/目的端口（传输层协议类型（协议号））

【举例】

\# 在启用了ASPF的设备上打开扩展信息调试功能。在设备接口配置ASPF策略，并向接口发送ICMP报文时，将输出如下调试信息。

\<Sysname\> debugging session ext-info all

\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/EXTINFO: -MDC=1;

 Ext-Info: Add  ASPF

  Tuple5(EVENT): 192.168.0.92/8\--\>192.168.1.58/3840(icmp(1))

*[// ASPF*]*向会话模块添加扩展信息成功，被添加扩展信息的会话五元组为：192.168.0.92/8\--\>192.168.1.58/3840(icmp(1))*

**会话管理 \-- 会话管理调试命令 \-- debugging session packet-process**

------------------------------------------------------------------------

【命令】

**[debugging session packet-process event** [ **acl** *acl-number* ]]

**[undo debugging session packet-process event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：报文处理相关的事件调试信息开关。

**[acl** *acl-number*]：指定匹配会话的ACL规则。其中，*acl-number*表示ACL编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。

【描述】

**[debugging session packet-process**]命令用来打开会话管理的报文处理调试信息开关。**undo debugging session packet-process**命令用来关闭会话管理的报文处理调试信息开关。

缺省情况下，会话管理的报文处理调试信息开关处于关闭状态。

表1-6 debugging session packet-process命令输出信息描述表

字段

描述

Tuple3: *srcIP* \--\>*destIP* (*ProtoType(Proto number)*)

报文的三元组：源IP\--\>目的IP/目的端口（传输层协议类型（协议号））

Received:

收到的报文

Packet can\'t be resolved

报文无法解析出五元组

Packet checking failed

报文合法性检查不通过（如报文长度、字段等不符合协议或不符合会话处理要求）

【举例】

\# 在启用了ASPF的设备上打开报文处理调试功能，向该设备发送一个flag标记是非法组合的TCP报文，将看到有如下显示信息输出。

\<Sysname\> debugging session packet-process event

\<Sysname\> system-view

\*Mar 26 08:50:24:568 2011 Sysname SESSION/7/PACKETS: -MDC=1;

 Tuple3: 192.168.1.58\--\>192.168.1.11(tcp(6))

 Received: Packet checking failed

*// 收到一个单包检查不合法的TCP报文，源IP为192.168.1.58，目的IP为192.168.1.11*

**会话管理 \-- 会话管理调试命令 \-- debugging session relation**

------------------------------------------------------------------------

【命令】

**[debugging session relation **[{ **all** \| **event** \| **error** }]]

**[undo debugging session relation **[{ **all** \| **event** \| **error** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示关联表的所有调试信息开关。

**[event**]：表示关联表的事件调试信息开关。

**[error**]：表示关联表的错误调试信息开关。

【描述】

**[debugging session relation**]命令用来打开会话管理的关联表调试信息开关。**undo debugging session relation**命令用来关闭会话管理的关联表调试信息开关。

缺省情况下，会话管理的关联表调试信息开关处于关闭状态。

表1-7 debugging session relation event命令输出信息描述表

字段

描述

Tuple(EVENT):

*[srcIP/ srcPort *]\--\>*destIP*/*destPort*(*ProtoType(ProtoNumber)*)

关联表的五元组：

·*srcIP*：源IP

·*srcPort*：源Port

·*destIP*：目的IP

·*destPort*：目的Port

·*ProtoType*：传输层协议类型

·*ProtoNumber*：协议号

Relation entry was created for module calling.

业务调用触发创建关联表

Relation entry was deleted for module calling

业务调用触发删除关联表

Relation entry was deleted for timeout.

老化超时触发删除关联表

Relation entry was updated for module calling.

业务调用触发更新关联表

表1-8 debugging session relation error命令输出信息描述表

字段

描述

Error:

关联表错误

Not enough memory for relation entry.

没有足够的内存用于创建关联表

Number of relation entries exceeded the max.

关联表个数超过最大值

【举例】

\# 在启用了ASPF的设备上打开关联表调试功能，当有FTP报文经过本设备去访问远端服务器时，将看到有如下调试信息输出。

\<Sysname\> debugging session relation all

\*Mar 26 09:12:33:800 2011 Sysname SESSION/7/RELATION: -MDC=1;

 Tuple(EVENT): 192.168.1.8/- \--\>2.2.2.2/21 (tcp(6))

 Relation entry was created for module calling.

*// 因外部模块通知创建一个关联表，其五元组为192.168.1.8/\-\--\>2.2.2.2/21 (TCP)*

\*Mar 26 09:17:54:112 2011 Sysname SESSION/7/RELATION: -MDC=1;

Tuple(EVENT): 192.168.1.8/- \--\>2.2.2.2/21 (tcp(6))

 Relation entry was deleted for time out.

*// 五元组为192.168.1.8/- \--\>2.2.2.2/21 (TCP(6))的关联表因老化被删除*

\*Mar 24 18:22:13:476 2011 Sysname SESSION/7/RELATION: -MDC=1;

 Error: Not enough memory for relation entry.

*// 没有足够的内存用于创建关联表*

**会话管理 \-- 会话管理调试命令 \-- debugging session session-table**

------------------------------------------------------------------------

【命令】

**[debugging session session-table **[{ **all** \| **error** \| **event** \| **fsm** } [ **acl** *acl-number* ]]]

**[undo debugging session session-table **[{ **all** \| **error** \| **event** \| **fsm** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示会话表项的所有调试信息开关。

**[error**]：表示会话表项的错误调试信息开关。

**[event**]：表示会话表项的事件调试信息开关。

**[fsm**]：表示会话表项的状态机调试信息开关。

**[acl** *acl-number*]：指定匹配会话的ACL规则。其中，*acl-number*表示ACL编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。

【描述】

**[debugging session session-table**]命令用来打开会话管理的会话表项调试信息开关。**undo debugging session session-table**命令用来关闭会话管理的会话表项调试信息开关。

缺省情况下，会话表项的调试信息开关处于关闭状态。

表1-9 debugging session session-table error命令输出信息描述表

字段

描述

Error:

会话表错误

Not enough memory for session entry.

会话创建时内存不足

Number of session entries exceeded the max.

会话数超过上限

Updating accelerate table failed.

更新流加速表失败

Creating session entry failed

创建会话表失败

表1-10 debugging session session-table event命令输出信息描述表

字段

描述

Tuple5(EVENT):* srcIP*/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(ProtoNumber)*)

会话的五元组（事件）：

源IP/源端口\--\>目的IP/目的端口（传输层协议类型（协议号））

Session entry was created.

会话被创建

Session entry was deleted.

会话被删除

表1-11 debugging session session-table fsm命令输出信息描述表

字段

描述

Tuple5  (FSM):* srcIP*/*srcPort*\--\>*destIP*/*destPort*(*ProtoType(Proto number)*)

会话的五元组（状态机）：

源IP/源端口\--\>目的IP/目的端口（传输层协议类型（协议号））

FSM:*preState*\--\>*nextState*,

会话状态机发生变迁（原状态为*preState*，下一个状态为*nextState*）

dir

报文方向：

·ORIGIN：表示发起方发送的报文

·REPLY：表示响应方发送的报文

PacketType: *PacketType(Packetnum)*

收到的报文的类型（报文编号）：

·GENERAL

·SYN

·SYNACK

·FIN

·ACK

·RST

·REQUEST

·RESPONSE

·DATA

·ACK

·DATAACK

·CLOSEREQ

·CLOSE

·RESET

·SYNC

·SYNCACK

·INIT

·INITACK

·ABORT

·SHUTDOWN

·SHUTDOWNACK

·ERROR

·COOKIEECHO

·COOKIEACK

·SHUTDOWNCOMPLETE

【举例】

\# 在启用了ASPF的设备上打开会话表项调试功能，有ping报文通过该设备时输出如下调试信息。

\<Sysname\> debugging session session-table all

\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/TABLE: -MDC=1;

 Tuple5  (EVENT): 192.168.0.2/8\--\>192.168.1.58/3840(icmp(1))

 Session entry was created

*// 创建一个发起方为192.168.0.2，响应方为192.168.1.58，协议为ICMP的会话*

\*Mar 24 18:15:47:174 2011 Sysname SESSION/7/TABLE: -MDC=1;

 Tuple5  (FSM): 192.168.0.2/8\--\>192.168.1.58/3840(icmp(1))

 FSM:NONE  \--\> ICMP_REQUEST,dir:ORIGIN,PacketType:REQUEST(8)

*// 由于收到ICMP报文，会话状态发生变迁，变迁前状态为NONE，变迁后状态为ICMP_REQUEST，方向为发起方－\>响应方，报文的类型为REQUEST*

\*Mar 24 18:15:47:175 2011 Sysname SESSION/7/TABLE: -MDC=1;

Tuple5  (FSM): 11.1.1.247/1024\--\>11.1.1.241/2048(icmp(1))

 FSM:ICMP_REQUEST\--\>ICMP_REPLY, dir:REPLY, PacketType:REPLY(0)

*// 由于发送ICMP报文，会话状态发生变迁，变迁前状态为ICMP_REQUEST，变迁后状态为ICMP_REPLY，方向为响应方－\>发起方，报文的类型为REPLY*

\# 在启用了安全模块功能的设备上打开会话调试功能，当申请会话表资源的内存不足时，输出调试信息。

\*Mar 24 18:22:13:476 2011 Sysname SESSION/7/TABLE: -MDC=1;

 Error:  Not enough memory for session entry.

*// 由于会话创建时内存不足*，*申请会话表资源失败*

**会话管理 \-- 会话管理调试命令 \-- debugging session alg**

------------------------------------------------------------------------

【命令】

**[debugging session alg **[{ **all** \| **event** \| **error** } [ **acl** *acl-number* ]]]

**[undo debugging session alg **[{ **all** \| **event** \| **error** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示ALG的所有调试信息开关。

**[event**]：表示ALG的事件调试信息开关。

**[error**]：表示ALG的错误调试信息开关。

**[acl** *acl-number*]：指定匹配会话的ACL规则。其中，*acl-number*表示ACL编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。

【描述】

**[debugging session alg**]命令用来打开ALG调试信息开关。**undo debugging session alg**命令用来关闭ALG调试信息开关。

缺省情况下，ALG的调试信息开关处于关闭状态。

表1-12 debugging session alg event命令输出信息描述表

字段

描述

Tuple5(EVENT):* srcIP*/*srcPort*\--\>*destIP*/*destPort*(*ProtoType*)

会话的五元组（事件）：

源IP/源端口\--\>目的IP/目的端口（传输层协议类型）

ALG received packet, packet type: *type*

收到报文，ALG类型为*type*包括以下取值：

·FTP_PORT

·FTP_PASV

·FTP_EPRT

·FTP_EPSV

·RAS_GRQ

·RAS_GCF

·RAS_GRJ

·RAS_RRQ

·RAS_RCF

·RAS_RRJ

·RAS_URQ

·RAS_UCF

·RAS_URJ

·RAS_ARQ

·RAS_ACF

·RAS_ARJ

·RAS_BRQ

·RAS_BCF

·RAS_BRJ

·RAS_DRQ

·RAS_DCF

·RAS_DRJ

·RAS_LRQ

·RAS_LCF

·RAS_LRJ

·RAS_IRQ

·RAS_IRR

·Q931_NATIONAL_ESCAPE

·Q931_ALERTING

·Q931_CALL_PROCEEDING

·Q931_CONNECT

·Q931_CONNECTACK

·Q931_PROGRESS

·Q931_SETUP

·Q931_SETUP_ACK

·Q931_RESUME

·Q931_RESUME_ACK

·Q931_RESUME_REJECT

·Q931_SUSPEND

·Q931_SUSPEND_ACK

·Q931_SUSPEND_REJECT

·Q931_USER_INFORMATION

·Q931_DISCONNECT

·Q931_RELEASE

·Q931_RELEASE_COMPLETE

·Q931_RESTART

·Q931_RESTART_ACK

·Q931_SEGMENT

·Q931_CONGESTION_CTRL

·Q931_INFORMATION

·Q931_NOTIFY

·Q931_STATUS

·Q931_STATUS_ENQUIRY

·Q931_FACILITY

·MULTIMEDIA_SYS_CTRL_REQUEST

·MULTIMEDIA_SYS_CTRL_RESPONSE

·MULTIMEDIA_SYS_CTRL_COMMAND

·MULTIMEDIA_SYS_CTRL_INDICATION

表1-13 debugging session alg error命令输出信息描述表

字段

描述

Tuple5:* srcIP*/*srcPort*\--\>*destIP*/*destPort*(*ProtoType*)

会话的五元组：

源IP/源端口\--\>目的IP/目的端口（传输层协议类型）

Error: No enough memory for ALG process.

没有足够的内存用于ALG处理

Error: Encoding failed.

编码失败

Error: Decoding failed.

解码失败

【举例】

\# 在启用了安全模块功能（如ASPF）的设备上打开ALG调试功能，有RAS RRQ报文通过该设备时输出调试信息。

\<Sysname\> debugging session alg event

\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/ALG: -MDC=1;

 Tuple5(EVENT): 192.168.0.2/1018\--\>192.168.1.58/1719(UDP(17))

 ALG received packet, packet type: RAS_RRQ

*// 收到一个需要进行ALG的报文，类型为RAS_RRQ*

\# 在启用了安全模块功能（如ASPF）的设备上打开ALG调试功能，有RAS报文通过该设备，解码失败时输出调试信息。

\<Sysname\> debugging session alg error

\*Mar 24 18:15:47:164 2011 Sysname SESSION/7/ALG: -MDC=1;

Tuple5: 192.168.0.2/1018\--\>192.168.1.58/1719(UDP(17))

Error: Decoding failed

*// 报文解码失败*

**会话管理 \-- 会话管理调试命令 \-- debugging session tcp**

------------------------------------------------------------------------

【命令】

**[debugging session tcp**[ { **all** \| **packet** \| **error** } [ **acl** *acl-number* ]]]

**[undo debugging session tcp**[ { **all** \| **packet** \| **error** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[packet**]：表示报文调试信息开关。

**[error**]：表示错误调试信息开关。

**[acl** *acl-number*]：指定匹配会话的ACL规则。其中，*acl-number*表示ACL编号，取值范围为2000～3999。该参数可多次设置，但仅最后一次合法的配置生效。

【描述】

**[debugging session tcp**]命令用来打开会话模块的TCP检查调试信息开关。**undo debugging session tcp**命令用来关闭会话模块的TCP检查调试信息开关。

缺省情况下，会话模块的TCP检查调试信息开关处于关闭状态。

表1-1 debugging session tcp packet命令输出信息描述表

字段

描述

TCP seq check: Processed the first *type* packet.

TCP序列号检查：对*type*类型的首包进行了序列号检查，*type*取值包括：

·SYN：SYN报文

·ACK：ACK报文

·Other：其他报文

TCP seq check: Packet from *Dir*, seq *seq*, next seq *nextSeq*, ack *ack.*

TCP序列号检查：报文的方向为*Dir*，序列号为*seq*，下一个报文的序列号为*nextSeq*，确认序列号为*ack*

*[Dir*]的取值包括：

·Initiator

·Responder

TCP state check: Invalid SYN packet.

TCP状态机检查：非法的SYN报文

TCP state check: Current state is *state.* Invalid *type* packet.

状态机检查：当前状态为*state*，无效的报文类型为*type*

State取值包括：

·NONE

·SYN_SENT

·SYN_RECV

·ESTABLISHED

·FIN_WAIT

·CLOSE_WAIT

·LAST_ACK

·TIME_WAIT

·CLOSE

·SYN_SENT2

·MAX

·IGNORE

类型取值包括：

·SYN

·SYNACK

·FIN

·ACK

·RST

·NONE

·MAX

TCP state check: Invalid RST packet.

TCP状态机检查：非法的RST报文

TCP seq check: Invalid sequence number during slow forwarding.

TCP序列号检查：慢转处理中，检查到报文的序列号非法

TCP seq check: Invalid sequence number during fast forwarding.

TCP序列号检查：快转处理中，检查到报文的序列号非法

TCP seq check: First fragment from *Dir*, seq *seq*, sack *sack*.

TCP序列号检查：分片报文的首片报文的方向为*Dir*，序列号为*seq*，SACK为*sack*

TCP seq check: Last fragment from *Dir*, next seq *nextSeq*, total length *length*.

TCP序列号检查：分片报文的最后一片报文的方向为*Dir*，下一个报文的序列号为*nextSeq*，总长度为*length*

TCP seq check: Received a fragment from *Dir,* updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver: next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.

TCP序列号检查：收到分片报文，方向为*Dir*，更新发送方数据：确认序列号为*ack*，下一个报文序列号为*SendernextSeq*、最大序列号为*SendermaxEnd*；更新响应方数据：下一个报文序列号为*RecvnextSeq*、最大序列号为*RecvmaxEnd*

TCP seq check: Received a fragment from *Dir* during fast forwarding*,* updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver: next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.

TCP序列号检查：在快转流程中收到分片报文，方向为*Dir*，更新发送方数据：确认序列号为*ack*，下一个报文序列号为*SendernextSeq*，最大序列号为*SendermaxEnd*；更新响应方数据：下一个报文序列号为*RecvnextSeq*，最大序列号为*RecvmaxEnd*

TCP seq check: Received a packet from *Dir*, updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver: next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.

TCP序列号检查：收到报文，方向为*Dir*，更新发送方数据：确认序列号为*ack*，下一个报文序列号为*SendernextSeq*，最大序列号为*SendermaxEnd*；更新响应方数据：下一个报文序列号为*RecvnextSeq*，最大序列号为*RecvmaxEnd*

TCP seq check: Received a packet from *Dir* during fast forwarding*,* updated data of sender: ack *ack*, next seq *SendernextSeq*, maxEnd *SendermaxEnd*; and receiver next seq *RecvnextSeq*, maxEnd *RecvmaxEnd*.

TCP序列号检查：在快转流程中收到报文，方向为*Dir*，更新发送方数据：确认序列号为*ack*，下一个报文序列号为*SendernextSeq*，最大序列号为*SendermaxEnd*；更新响应方数据：下一个报文序列号为*RecvnextSeq*，最大序列号为*RecvmaxEnd*

TCP seq check: Invalid fragmented packet.

TCP序列号检查：分片报文TCP序列号检查报文非法

TCP state check: Invalid packet.

TCP状态机检查： TCP状态错误的非法报文

TCP seq check: Successfully got the last ack *ack*.

TCP序列号检查：成功获取到最后一个确认序列号为*ack*。

表1-2 debugging session tcp error命令输出信息描述表

字段

描述

Not enough memory.

没有足够的内存

Failed to get the next sequence number of the packet with a Layer 2 header.

获取带有二层帧头的报文的下一个报文序列号失败

Failed to get the next sequence number.

获取下一个报文序列号失败

【举例】

\# 在启用了安全模块功能（如ASPF）的设备上打开TCP检查调试功能，TCP报文通过该设备时输出调试信息。

\<Sysname\> debugging session tcp packet

\*May 15 01:56:15:610 2014 Sysname SESSION/7/TCP-PACKET: -MDC=1;

 TCP seq check: Processed the first SYN packet.

*// 对SYN类型的首包进行了序列号检查*

\*May 15 09:39:57:111 2014 Sysname SESSION/7/TCP-EVENT: -MDC=1;

 TCP seq check: Packet from Responder, seq 70c8e503, next seq 70c8e504, ack 445b75ff

*// 收到一个响应报文，该报文的序列号是*70c8e503*，下一个序列号是*70c8e504*，确认序列号是*445b75ff*

\*May 15 01:56:15:621 2014 Sysname SESSION/7/TCP-EVENT: -MDC=1;

TCP seq check: Invalid sequence number during fast forwarding.

*// 在快转处理流程中，报文的序列号检查不通过*

