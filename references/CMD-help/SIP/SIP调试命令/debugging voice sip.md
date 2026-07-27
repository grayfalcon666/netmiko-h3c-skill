<!-- CMD-INDEX
  debugging voice sip                 | 用户视图             | L5
-->

**SIP \-- SIP调试命令 \-- debugging voice sip**

------------------------------------------------------------------------

【命令】

**[debugging voice sip **[{ **all** \| **error** **\| event \| fsm \| info \| message \| stack \| timer }**]]

**[undo debugging voice sip**[ { **all** \| **error** \| **event \| fsm \| info \| message \| stack \| timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示SIP所有消息类型的调试信息开关。

**[error**]：表示SIP的错误类型的消息调试信息开关。

**[event**]：表示SIP的事件类消息调试信息开关。

**[fsm**]：表示SIP的状态机类消息调试信息开关。

**[info**]：表示SIP的信息类消息调试信息开关。

**[message**]：表示SIP的报文类消息调试信息开关。

**[stack**]：表示SIP协议栈类消息调试信息开关。

**[timer**]：表示SIP的定时器消息调试信息开关。

【描述】

**[debugging voice sip**]命令用来打开SIP调试信息开关。**undo debugging voice sip**命令用来关闭SIP调试信息开关。

缺省情况下，SIP调试信息开关处于关闭状态。

表1-1 debugging voice sip error令输出信息描述表

字段

描述

Failed to allocate memory for CCB.

为CCB分配内存失败

Failed to get CCB when binding source address.

源地址绑定时获取CCB失败

Received INVITE request: Failed to get SDP media description.

收到INVITE请求：获取SDP媒体描述信息失败

Received  ALERTING message: Failed to save brother codec.

收到ALERTING消息：保存兄弟编解码类型失败

Failed to get SIP CCB in normal call back.

在正常回调中获取SIP CCB失败

Failed to set Request-Line when building INVITE message.

构建INVITE消息时设置请求行失败

Failed to create DNS CCB.

创建DNS CCB失败

Failed to process DNS response before registration because the source or destination IP address cannot be obtained.

因为无法获取源/目的地址，处理注册前的DNS应答消息失败

Failed to decode SDP.

解码SDP失败

Failed to negotiate brother and local codec set.

协商兄弟和本地编码集失败

Invalid message body.

无效的消息体

Failed to send ACK message for SIP connect.

发送SIP connect的ACK消息失败

Session Expires(*Expires-Value*) value is smaller than Min-Se(*Min-Value*)

会话有效时间小于最小有效时间

*[Expires-Value*]：Expires头域的值

*[Min-Value*]：Min-Se头域的值

TLS: Failed to create listener.

创建TLS listener失败

TLS: Failed to set connection to no-block mode.

设置TLS连接为非阻塞模式失败

TPTD:Failed to allocate memory for contex CB

TPTD：为上下文控制块申请内存失败

TPTD: Failed to generate hash key by address.

TPTD：由地址产生hash key失败

Build Contact header: Failed to set param for Contact.

建立 Contact 头域：为Contact设置参数失败

Build Allow header: Failed to create Allow header.

建立 Allow 头域：创建Allow头域失败

Build Allow header: Failed to add *method* method to Allow.

建立 Allow 头域：添加*method*方法到Allow头域失败

Allow头域支持的方法如下(*method*的取值非如下值)：

·METHOD_TYPE_ACK：Allow头域支持ACK操作方法

·METHOD_TYPE_BYE：Allow头域支持BYE操作方法

·METHOD_TYPE_CANCEL：Allow头域支持CANCEL操作方法

·METHOD_TYPE_INFO：Allow头域支持INFO操作方法

·METHOD_TYPE_INVITE：Allow头域支持INVITE操作方法

·METHOD_TYPE_NOTIFY：Allow头域支持NOTIFY操作方法

·METHOD_TYPE_PRACK：Allow头域支持PRACK操作方法

·METHOD_TYPE_REFER：Allow头域支持REFER操作方法

·METHOD_TYPE_REGISTER：Allow头域支持REGISTER操作方法

·METHOD_TYPE_UPDATE：Allow头域支持UPDATE操作方法

·METHOD_TYPE_SUBSCRIBE：Allow头域支持SUBSCRIBE操作方法

·METHOD_TYPE_OPTIONS：Allow头域支持OPTIONS操作方法

表1-2 debugging voice sip event令输出信息描述表

字段

描述

 CMC \--\> SIP : *message-type*.

SIP收到CMC发来的*message-type*消息

*[message-type*]的取值为：

·ACCP_SETUP：表示出局端，CMC向SIP发送建立新呼叫信令

·ACCP_CHANNEL_READY_ACK：表示出局端，CMC对SIP ACCP_CHANNEL_READY的应答信令

·ACCP_INDICATE：表示出局端CMC发送指示信令

·ACCP_RELEASE_COMPLETE：表示出局端CMC发送释放结束信令

SIP \--\> CMC : *message-type*.

SIP向CMC发送*message-type*消息

*[message-type*]取值为：

·ACCP_SETUP_ACK：SIP向CMC发送通话建立的确认信令

·ACCP_ALERTING：SIP向CMC发送振铃信令

·ACCP_CHANNEL_READY：SIP向CMC发送媒体通道就绪信令

·ACCP_INFORMATION：SIP向CMC发送DTMF信令

·ACCP_CONNECT：SIP向CMC发送连接信令

·ACCP_RELEASE：SIP向CMC发送通话释放信令

Adapter \--\> Stack : *message_type*.

适配层向协议栈发送*message_type*消息

*[message_type*]取值如下：

·Setup request：适配层向协议栈发送呼叫建立请求

·PRACK request：适配层向协议栈发送PRACK请求

·Connect ackrequest：适配层向协议栈发送连接确认请求

Stack \--\> Adapter : *message_type*.

协议栈向适配层发送*message_type*消息

*[message_type*]取值如下：

·Setup ack：协议栈向适配层发送连接确认消息

·Alerting indication：协议栈向适配层发送振铃指示

·Prackresponse：协议栈向适配层发送Prack应答

·Connect indication：协议栈向适配层发送连接指示

·Release indication：协议栈向适配层发送通话释放指示

The Content-Type header does not exist.

Content-Type头域不存在

Get first address by ip (*ip*)

通过ip的获取第一个地址

*[ip*]为用于地址查询的ip

Get *signaling/media* address by global configuration.

通过全局配置获取*信令**/媒体*地址

Set SDP media field: *MediaNumber*  media description(s) to be set.

设置SDP媒体域：*MediaNumber*个媒体行被设置

Codec negotiated result is voice media update.

编解码协商的结果是语音媒体更新

DNS queried done, now the state is *state*

DNS查询完成，目前状态为*state*

Audio media takes different media ip address or port

语音媒体携带了不同的媒体地址或端口

表1-3 debugging voice sip info令输出信息描述表

字段

描述

Get loopback address for local using FIB.

使用FIB表为本地获取loopback地址

SIP service(Call-Waiting) is processing.

SIP业务(呼叫等待)正在处理

Local ringing.

本地振铃

There is no SDP in SIP message.

SIP消息中不存在SDP

Reconnecting to HA daemon, Please wait\...

重连HA守护进程，请等待......

Failed to connect to HA daemon.

连接HA守护进程失败

表1-4 debugging voice sip timer令输出信息描述表

字段

描述

*module* start timer, Group id = *number1*, Index = *number2*, Duration = *number3*

*[module*]启动定时器，Group id 为*number1，*Index为*number2，*Duration为*number3*

Deleting timer within RCB *rcb_id* server *server_index* before sending unregistration message.

在发送去注册之前删除注册控制块*server_index*服务器*rcb_id*控制块内的定时器

Timer for sending REGISTER messages will be created

before adding RCB *rcb_id* to message-sending list.

在*rcb_id*控制块添加到消息发送链表之前注册报文发送定时器将被创建

SIP_REGISTER The message sending list is empty.

SIP注册：消息发送链表为空

表1-5 debugging voice sip fsm令输出信息描述表

字段

描述

SIP_CALL*id*: Process the event of *event_type* in state *state_type*.

在*state_type*状态下处理*event_type*事件

*[id*]用于标识一路呼叫

*[state_type*]取值如下：

·EVENT_ACCP_SETUP：建立连接事件

·EVENT_NO_FEATURE_SETUP：非特性连接事件

·EVENT_ADDR_IN_DAILPEER：Dial peer获取地址事件

·EVENT_LOOKUP_SUCCESS：地址查询成功事件

·EVENT_GET_ADDRINFO_SUCCESS：获取地址成功事件

·EVENT_SIP_ALERTING：振铃事件

·EVENT_EXIST_SDP_BODY：存在SDP事件

·EVENT_SIP_CONNECT：连接建立事件

·EVENT_SIP_RELEASE：释放连接事件

*[event_type*]取值如下：

·STATE_IDLE：空闲状态

·STATE_CALL_ORIGINATING：呼叫发起等待应答状态

·STATE_CONNECTED：呼叫建立状态

·STATE_CALL_TERMINATING：呼叫终止状态

·STATE_MEDIA_IDLE：媒体空闲状态

【举例】

\# 本地LGS通过IP网络建立了呼叫。打开主叫侧SIP所有类型的调试信息输出开关。

\<Sysname\>debugging voice sip all

\<Sysname\>\*Jan 23 10:21:15:262 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: CMC \--\> SIP : ACCP_SETUP.

*[// SIP*]*收到CMC发来的启动呼叫（ACCP_SETUP）消息*

\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_ACCP_SETUP in state STATE_IDLE.]

*[// SIP*]*呼叫状态机在初始状态下处理 ACCP_SETUP消息*

\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Do not exist content type.

\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: The header of ReferredBy does not exist.

\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_NO_FEATURE_SETUP in state STATE_IDLE.]

\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_ADDR_IN_DAILPEER in state STATE_IDLE.]

\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Get first address by ip (192.168.4.16).

\*Jan 23 10:21:15:263 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_LOOKUP_SUCCESS in state STATE_IDLE.]

\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Get signalling address by global.

\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG:

SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).

\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_GET_ADDRINFO_SUCCESS in state STATE_IDLE.]

\*Jan 23 10:21:15:264 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SIP \--\> CMC : ACCP_SETUP_ACK.

*[// SIP*]*向CMC回复ACCP_SETUP_ACK*消息

\*Jan 23 10:21:15:265 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SIP set SDP media field: total 1 media description(s) to be set.

\*Jan 23 10:21:15:271 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Adapter \--\> Stack : Setup Request.

*[// SIP*]*适配层向协议栈发送SETUP请求*

\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SrcAddr: 192.168.4.66, SrcPort: 5060, DestAddr: 192.168.4.16, DestPort: 5060, Protocol: UDP

\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG:

Stack\-\--\>NetWork:

INVITE sip:444@192.168.4.16:5060;user=phone SIP/2.0

Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b

Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66

From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c

To: \<sip:444@192.168.4.16;user=phone\>

CSeq: 1 INVITE

Contact: \<sip:666@192.168.4.66:5060;user=phone\>

Supported: timer,100rel

Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,REGISTER,INFO,PRACK,SUBSCRIBE,NOTIFY,UPDATE,REFER

Date: Thu, 23 Jan 2014 10:21:15 GMT

Remote-Party-ID: \<sip:666@192.168.4.66;user=phone\>;party=calling;privacy=off

Max-Forwards: 70

Content-Length: 238

Content-Type: application/sdp

v=0

o=H3C 1390472475 1390472475 IN IP4 192.168.4.66

s=Sip Call

c=IN IP4 192.168.4.66

t=0 0

m=audio 16302 RTP/AVP 18 8 0 4

a=rtpmap:18 G729/8000

a=fmtp:18 annexb=no

a=rtpmap:8 PCMA/8000

a=rtpmap:0 PCMU/8000

a=rtpmap:4 G723/8000

*[// SIP*]*协议栈向网络侧发送INVITE报文*

\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Get signalling address by global.

\*Jan 23 10:21:15:272 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TPT Start Timer, Group id = 2, Index = 411, Duration = 30000.]

\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Start Timer, Group id = 3, Index = 50, Duration = 500.]

\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Start Timer, Group id = 4, Index = 50, Duration = 32000.]

\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Start Timer, Group id = 9, Index = 1, Duration = 600000.]

\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Stack \--\> Adapter : Setup Ack.

*[// SIP*]*协议栈向适配层发送SETUP请求的应答消息*

\*Jan 23 10:21:15:273 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TPT Stop Timer, Group id = 2, Index = 411.]

\*Jan 23 10:21:15:277 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP

\*Jan 23 10:21:15:278 2014 Sysname SIP/7/SIPDBG:

NetWork\-\--\>Stack:

SIP/2.0 100 Trying

Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b

From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c

To: \<sip:444@192.168.4.16;user=phone\>

Date: Thu, 23 Jan 2014 02:25:36 GMT

Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66

CSeq: 1 INVITE

Allow-Events: telephone-event

Server: Cisco-SIPGateway/IOS-15.2.4.M2

Content-Length: 0

*[// SIP*]*协议栈从网络侧收到100trying报文*

\*Jan 23 10:21:15:278 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Stop Timer, Group id = 3, Index = 50.]

\*Jan 23 10:21:15:323 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP

\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG:

NetWork\-\--\>Stack:

SIP/2.0 183 Session Progress

Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b

From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c

To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D

Date: Thu, 23 Jan 2014 02:25:36 GMT

Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66

CSeq: 1 INVITE

Require: 100rel

RSeq: 8

Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER

Allow-Events: telephone-event

Remote-Party-ID: \<sip:444@192.168.4.16\>;party=called;screen=no;privacy=off

Contact: \<sip:444@192.168.4.16:5060\>

Supported: sdp-anat

Server: Cisco-SIPGateway/IOS-15.2.4.M2

Content-Type: application/sdp

Content-Disposition: session;handling=required

Content-Length: 191

v=0

o=CiscoSystemsSIP-GW-UserAgent 2464 7928 IN IP4 192.168.4.16

s=SIP Call

c=IN IP4 192.168.4.16

t=0 0

m=audio 20306 RTP/AVP 8

c=IN IP4 192.168.4.16

a=rtpmap:8 PCMA/8000

a=pti

\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG: continuing\...

me:20

*[// SIP*]*协议栈从网络侧收到100trying报文*

\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Stop Timer, Group id = 4, Index = 50.]

\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Start Timer, Group id = 4, Index = 50, Duration = 256000.]

\*Jan 23 10:21:15:324 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Start Timer, Group id = 5, Index = 1, Duration = 128000.]

\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Stop Timer, Group id = 9, Index = 1.]

\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Start Timer, Group id = 9, Index = 1, Duration = 600000.]

\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Stack \--\> Adapter : Alerting Indication.

*[// SIP*]*协议栈向适配层上报Alerting指令*

\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_SIP_ALERTING in state STATE_CALL_ORIGINATING.]

*[// SIP*]*状态机处理EVENT_SIP_ALERTING事件在STATE_CALL_ORIGINATING状态下*

\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Get signalling address by global.

\*Jan 23 10:21:15:325 2014 Sysname SIP/7/SIPDBG:

SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).

\*Jan 23 10:21:15:326 2014 Sysname SIP/7/SIPDBG:

SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).

\*Jan 23 10:21:15:326 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Adapter \--\> Stack: PRACK Request.

\*Jan 23 10:21:15:327 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SrcAddr: 192.168.4.66, SrcPort: 5060, DestAddr: 192.168.4.16, DestPort: 5060, Protocol: UDP

\*Jan 23 10:21:15:327 2014 Sysname SIP/7/SIPDBG:

Stack\-\--\>NetWork:

PRACK sip:444@192.168.4.16:5060;user=phone SIP/2.0

Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK6132dbdbd71;rport

Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66

From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c

To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D

CSeq: 2 PRACK

Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,REGISTER,INFO,PRACK,SUBSCRIBE,NOTIFY,UPDATE,REFER

Date: Thu, 23 Jan 2014 10:21:15 GMT

Max-Forwards: 70

RAck: 8 1 INVITE

Supported: timer

Content-Length: 0

*[// SIP*]*协议栈从网络侧收到183报文*

\*Jan 23 10:21:15:327 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Get signalling address by global.

\*Jan 23 10:21:15:328 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TPT Start Timer, Group id = 2, Index = 412, Duration = 30000.]

\*Jan 23 10:21:15:328 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Start Timer, Group id = 3, Index = 51, Duration = 500.]

\*Jan 23 10:21:15:328 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Start Timer, Group id = 4, Index = 51, Duration = 32000.]

\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG:

SIP STACK:

  SIP STACK DEBUG LOG: Component = User Agent

  Additional Code: 2404-2547

  Additional Info: Invalid Paramter(s) 

\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_EXIST_SDP_BODY in state STATE_CALL_ORIGINATING.]

\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Codec negotiated result is voice update.

\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Audio media take different media ip address or port.

\*Jan 23 10:21:15:329 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Receive Response: The Status Code = 183.

\*Jan 23 10:21:15:330 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SIP \--\> CMC : ACCP_ALERTING.

*[// SIP*]*向CMC发送ACCP_ALERTING消息，通知对方已振铃*

\*Jan 23 10:21:15:331 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SIP \--\> CMC : ACCP_CHANNEL_READY.

*[// SIP*]*向CMC发送ACCP_CHANNEL_READY消息，准备建立媒体通道*

\*Jan 23 10:21:15:332 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP

\*Jan 23 10:21:15:332 2014 Sysname SIP/7/SIPDBG:

NetWork\-\--\>Stack:

SIP/2.0 200 OK

Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK6132dbdbd71;rport

From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c

To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D

Date: Thu, 23 Jan 2014 02:25:36 GMT

Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66

Server: Cisco-SIPGateway/IOS-15.2.4.M2

CSeq: 2 PRACK

Content-Length: 0

\*Jan 23 10:21:15:332 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Stop Timer, Group id = 4, Index = 51.]

\*Jan 23 10:21:15:333 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Stop Timer, Group id = 3, Index = 51.]

\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Stack \--\> Adapter : Ssn Response.

\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Stack \--\> Adapter : Prack Response.

\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Receive Prack Response: The Status Code = 200.

\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Start Timer, Group id = 3, Index = 51, Duration = 5000.]

\*Jan 23 10:21:15:334 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TPT Stop Timer, Group id = 2, Index = 412.]

\*Jan 23 10:21:15:335 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: CMC \--\> SIP : ACCP_CHANNEL_READY_ACK.

\*Jan 23 10:21:15:335 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SIP \--\> CMC : ACCP_INFORMATION.

   Disable Outband Sip

\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SrcAddr: 192.168.4.16, SrcPort: 64135, DestAddr: 192.168.4.66, DestPort: 5060, Protocol: UDP

\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG:

NetWork\-\--\>Stack:

SIP/2.0 200 OK

Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bK607a839c51b

From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c

To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D

Date: Thu, 23 Jan 2014 02:25:36 GMT

Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66

CSeq: 1 INVITE

Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER

Allow-Events: telephone-event

Remote-Party-ID: \<sip:444@192.168.4.16\>;party=called;screen=no;privacy=off

Contact: \<sip:444@192.168.4.16:5060\>

Supported: replaces

Supported: sdp-anat

Server: Cisco-SIPGateway/IOS-15.2.4.M2

Supported: timer

Content-Type: application/sdp

Content-Disposition: session;handling=required

Content-Length: 191

v=0

o=CiscoSystemsSIP-GW-UserAgent 2464 7928 IN IP4 192.168.4.16

s=SIP Call

c=IN IP4 192.168.4.16

t=0 0

m=audio 20306 RTP/AVP 8

c=IN IP4 192.168.4.16

a=rtpmap:8 PCMA/8000

a=ptim

\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG: continuing\...

e:20

*[// SIP*]*协议栈从网络侧收到200ok报文*

\*Jan 23 10:21:17:093 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Stop Timer, Group id = 5, Index = 1.]

\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Start Timer, Group id = 5, Index = 1, Duration = 64000.]

\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Stop Timer, Group id = 9, Index = 1.]

\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Start Timer, Group id = 9, Index = 1, Duration = 600000.]

\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Stack \--\> Adapter : Connect Indication.

*[// SIP*]*协议栈向适配层上报Connect指令*

\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_SIP_CONNECT in state STATE_CALL_ORIGINATING.]

\*Jan 23 10:21:17:094 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_EXIST_SIP_BODY in state STATE_CALL_ORIGINATING.]

\*Jan 23 10:21:17:095 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Codec negotiated result is voice update.

\*Jan 23 10:21:17:095 2014 Sysname SIP/7/SIPDBG:

SIP FSM: [SIP_CALL1: Process the event of EVENT_OFFERMODE_PROC in state STATE_CALL_ORIGINATING.]

\*Jan 23 10:21:17:095 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SIP \--\> CMC : ACCP_CONNECT.

*[// SIP*]*向CMC发送ACCP_ALERTING消息，通知对方已摘机*

\*Jan 23 10:21:17:097 2014 Sysname SIP/7/SIPDBG:

SIP INFO: Get address from GigabitEthernet0/0(192.168.4.66).

\*Jan 23 10:21:17:097 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Adapter \--\> Stack : Connect Ack Request.

\*Jan 23 10:21:17:097 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: SrcAddr: 192.168.4.66, SrcPort: 5060, DestAddr: 192.168.4.16, DestPort: 5060, Protocol: UDP

\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG:

Stack\-\--\>NetWork:

ACK sip:444@192.168.4.16:5060;user=phone SIP/2.0

Via: SIP/2.0/UDP 192.168.4.66:5060;branch=z9hG4bKf608efafee9

Call-ID: 0330805cef6264d4830aea1c470fc37c@192.168.4.66

From: \<sip:666@192.168.4.66;user=phone\>;tag=557a839c

To: \<sip:444@192.168.4.16;user=phone\>;tag=CE097BD4-1B9D

CSeq: 1 ACK

Date: Thu, 23 Jan 2014 10:21:17 GMT

Max-Forwards: 70

Content-Length: 0

*[// SIP*]*协议栈向网络侧发送200ok的ACK报文，呼叫建立成功*

\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG:

SIP EVENT: Get signalling address by global.

\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TPT Start Timer, Group id = 2, Index = 413, Duration = 30000.]

\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Stop Timer, Group id = 5, Index = 1.]

\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Stop Timer, Group id = 9, Index = 1.]

\*Jan 23 10:21:17:098 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_UA Start Timer, Group id = 9, Index = 1, Duration = 1800000.]

\*Jan 23 10:21:17:099 2014 Sysname SIP/7/SIPDBG:

SIP TIMER: [SIP_COMP_TXN Stop Timer, Group id = 4, Index = 50.]

\*Jan 23 10:21:17:099 2014 Sysname SIP/7/SIPDBG:

SIP STACK:

  SIP STACK INFORMATIONAL LOG: Component = Transaction

  Additional Code: 1100-441

  Additional Info: Transaction block is destroyed  

