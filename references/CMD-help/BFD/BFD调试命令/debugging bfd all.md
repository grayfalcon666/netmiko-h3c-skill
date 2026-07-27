<!-- CMD-INDEX
  debugging bfd all                   | 用户视图             | L13
  debugging bfd error                 | 用户视图             | L51
  debugging bfd event                 | 用户视图             | L371
  debugging bfd fsm                   | 用户视图             | L541
  debugging bfd ha                    | 用户视图             | L607
  debugging bfd ntfy                  | 用户视图             | L665
  debugging bfd packet                | 用户视图             | L727
  debugging bfd scm                   | 用户视图             | L969
  debugging bfd timer                 | 用户视图             | L1039
-->

**BFD \-- BFD调试命令 \-- debugging bfd all**

------------------------------------------------------------------------

【命令】

**[debugging bfd all**]

**[undo debugging bfd all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd all**]命令用来打开BFD的全部调试信息开关。**undo debugging bfd all**命令用来关闭BFD的全部调试信息开关。

缺省情况下，BFD的全部调试信息开关处于关闭状态。

BFD调试信息显示形式包括系统运行时间、设备名、BFD、调试信息级别、模块名和事件内容。

【举例】

\# 打开BFD的全部调试信息开关。

\<Sysname\> debugging bfd all

**BFD \-- BFD调试命令 \-- debugging bfd error**

------------------------------------------------------------------------

【命令】

**[debugging bfd error**]

**[undo debugging bfd error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd error**]命令用来打开BFD错误调试信息开关。**undo debugging bfd error**命令用来关闭BFD错误调试信息开关。

缺省情况下，BFD错误调试信息开关处于关闭状态。

表1-1 debugging bfd error命令输出信息描述表

字段

描述

Failed to reset session

主用板重置会话失败

Failed to encapsulate driver information

封装驱动信息失败

Failed to get LIPC address

获取LIPC地址失败

Failed to synchronize message to kernel

同步消息到内核失败

KFailed to receive configuration message, errno: *ret*, fail count: *cnt*.

接收来自用户态的配置消息失败：

·   *ret*：LIPC调用返回的错误码

·   *cnt*：接收失败的次数

K Failed to send display information, errno: *ret*, fail count: *cnt*.

向用户态发送显示信息失败：

·   *ret*：LIPC调用返回的错误码

·   *cnt*：发送失败的次数

KFailed to add file descriptor *fd* to kepoll, errno: *ret*, fail count: *cnt*.

向kepoll池添加描述符失败：

·   *fd*：文件描述符

·   *ret*：kepoll调用返回的错误码

·   *cnt*：添加失败的次数

KFailed to get driver head, return: *ret*, fail count: *cnt.*

获取发包驱动头失败：

·   *ret*：驱动接口返回的错误码，16进制形式

·   *cnt*：获取失败的次数

KMDC *id* does not exist in speed limit timer, fail count: *cnt*.

MDC *id*不存在限速定时器中：

·   *id*：MDC的编号

·   *cnt*：不存在的次数

KFailed to create socket when connect daemon. return: *ret*, MDC: *id*, fail count: *cnt*.

连接用户进程中创建socket失败：

·   *ret*：返回的错误码

·   *id*：MDC的编号

·   *cnt*：连接失败的次数

KFailed to synchronize message to daemon, type: *type*, errno: *ret*, fail count: *cnt*.

向用户进程同步消息失败：

·   *type*：同步消息类型

·   *ret*：LIPC调用返回的错误码

·   *cnt*：发送失败的次数

KDetect timer parameter error, timer: *id*, fail count: *cnt*.

检测定时器回调函数参数错误：

·   *id*：定时器的编号

·   *cnt*：参数错误的次数

KMDC *id1* does not exist in detect timer *id2*, fail count: *cnt*.

MDC *id1*不存在检测定时器*id2*中：

·   *id1*：MDC的编号

·   *id2*：定时器的编号

·   *cnt*：不存在的次数

KSend timer parameter error, timer: *id*, fail count: *cnt*.

发包定时器回调函数参数错误：

·   *id*：定时器的编号

·   *cnt*：参数错误的次数

KMDC *id1* does not exist in send timer *id2*, fail count: *cnt*.

MDC *id1*不存在发包定时器*id2*中：

·   *id1*：MDC的编号

·   *id2*：定时器的编号

·   *cnt*：不存在的次数

KFailed to create session on OAM, without running data. index: *idx*, fail count: *cnt*.

OAM上创建会话失败，没有运行数据：

·   *idx*：会话索引

·   *cnt*：失败的次数

KThe session already exists, index: *idx*, repeat count: *cnt*.

待创建的会话已经存在：

·   *idx*：会话索引

·   *cnt*：重复创建的次数

KFailed to create session, index: *idx*, fail count: *cnt*.

创建会话失败：

·   *idx*：会话索引

·   *cnt*：失败的次数

Synchronize message to kernel, send failed.

同步消息到内核失败

KAuthentication type: *type* should not calculate digest.

该认证类型不必计算摘要：

l*type*：认证类型

KCan not calculate digest. Auth type: *auth-type*, Direction: *packet-direction*. CCF handle: *handle*, CCF job: *job-address*.

计算摘要错误：

l*auth-type*：认证类型

l*packet-direction*：报文出入方向

l*handle*：算法句柄

l*job-address*：CCF任务的数据地址

Configure change type error.

BFD命令行模板下配置的参数类型错误

Failed to modify session by template.

通过模板修改会话参数失败

Failed to modify template.

修改会话模板失败

Proc Sync Seq. Failed to get session.

处理内核上报的序列号时，会话获取失败

Proc Sync F Finish. Failed to get session.

处理内核上报的F报文结束事件时，会话获取失败

Failed to encapsulate digest information.

认证报文摘要封装失败

Failed to add session node to template.

模板哈希上会话节点添加失败

Failed to add session to interface. Session LD: *local-discr*

将会话节点从模板哈希加到接口会话链表资源申请失败：

l*local-discr*：会话本地鉴别码

KUnknown message type: *message-type*

未知消息类型：

l*message-type*：消息类型

KUnknown event type: *event-type*

未知事件类型：

l*event-type*：事件类型

KBFD: MDC:*mdc-id* does not exist in CCF reinit timer

Mdc数据不存在

l*mdc-id*：对应MDC的ID号

KBFD: Failed to create CCF reinit timer.

创建CCF重新初始化定时器失败

Apptype error. Apptype: *application-type*

应用类型错误：

l*application-type*：应用类型

Failed to send. Expect len: *expect-length*, Actual len: *actual-length*.

消息发送失败：

l*expect-length*：预期长度

l*actual-length*：实际长度

Scenario error. Scenario: *scenario.*

情景类型错误：

l*scenario*：情景类型

Proc Sync Down Finish. Failed to get session. Session LD: *local-discr*.

在处理内核上报down报文发送完成事件时，获取会话失败：

l*local-discr*：会话本地鉴别码

Failed to process session downLD:local-discr, Flag:*session-flag.*

处理会话down事件失败，包括内核上报与状态机变化：

l*local-discr*：会话本地鉴别码

l*session-flag*：会话标记位

Failed to disable session. Status:*session-status*.

去使能会话失败：

l*session-status*：会话状态

Failed to proccess finish delete LD: *local-discr*

删除带BFD_SESS_DELETING标记会话失败：

l*local-discr*：会话本地鉴别码

Queue entry type err:*message-type*

处理消息队列时，消息类型错误：

l*message-type*：消息类型

KUnknown mdc event:*event*

内核处理MDC事件时，遇到未知的MDC事件：

l*event*：MDC事件

【举例】

\# 打开BFD错误调试信息开关。

\<Sysname\> debugging bfd error

\*Jul  4 15:15:33:783 2011 Sysname BFD/7/DEBUG: -MDC=1; BFD: Synchronize message to kernel[, send failed.]

*// 发送消息失败*

**BFD \-- BFD调试命令 \-- debugging bfd event**

------------------------------------------------------------------------

【命令】

**[debugging bfd event**]

**[undo debugging bfd event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd event**]命令用来打开BFD事件调试信息开关。**undo debugging bfd event**命令用来关闭BFD事件调试信息开关。

缺省情况下，BFD事件调试信息开关处于关闭状态。

表1-2 debugging bfd event命令输出信息描述表

字段

描述

Response interface event packet failed

接收并解析接口事件通知报文失败

Notify driver to start receiving BFD packet

创建第一个IPv4会话时，通知驱动开始接收BFD控制报文

Notify driver to stop receiving BFD packet

通知驱动停止接收BFD控制报文

Notify driver to start receiving ipv6 BFD packet

创建第一个IPv6会话时，通知驱动开始接收BFD控制报文

Notify driver to stop receiving ipv6 BFD packet

通知驱动停止接收BFD控制报文

KWrite sync session queue success. Session LD: *local-discr*. MsgType: *message-type*.

写同步会话消息队列：

l*local-discr*：会话本地鉴别码

l*message-type*：消息类型

KSync XmitAuthSeq: *sequence*. Session LD: *local-discr*.

向用户态同步序列号：

l*sequence*：认证序列号

l*local-discr*：会话本地鉴别码

KUpdate session success. Session LD: *local-discr* Status: *sess-status* Flag: *sess-flag*

更新会话成功：

l*local-discr*：会话本地鉴别码

l*sess-status*：会话状态

l*sess-flag*：会话标记位

KUpdate session LD: *local-discr*. XmitAuthSeq change to *sequence-number*.

用户态更新认证序列号到内核：

l*local-discr*：会话本地鉴别码

l*sequence-number*：同步的认证序列号

KProcess sync finish.session LD: *local-discr* Type: *message-type*.

向用户态发送报文发送完成消息：

l*local-discr*：会话本地鉴别码

l*message-type*：消息类型

KProc sync sequence.session LD: *local-discr* XmitAuthSeq: *sequence-number.*

内核向用户态同步序列号：

l*local-discr*：会话本地鉴别码

l*sequence-number*：同步的认证序列号

LD: *local-discr* increase XmitAuthSeq: *sequence-number.*

增加序列号：

l*local-discr*：会话本地鉴别码

l*seqeunce-number*：认证序列号

Encap auth part. LD: *local-discr* XmitAuthSeq: *sequence-number*.

封装认证部分报文：

l*local-discr*：会话本地鉴别码

l*seqeunce-number*：认证序列号

Proc Sync F Finish. Session LD:*local-discr*.

处理内核上报F报文发送结束事件：

l*local-discr*：会话本地鉴别码

Proc Sync Seq. Session LD: *local-discr* XmitAuthSeq: *sequence-number*.

处理内核向用户态同步序列号事件：

l*local-discr*：会话本地鉴别码

l*sequence-number*：同步的认证序列号

Proc Sync Down Finish. Session LD: *local-discr*.

处理内核上报down报文发送完成事件：

l*local-discr*：会话本地鉴别码

Proc Sync sequence.Session LD: *local-discr* XmitAuthSeq: *sequence-number.*

用户态向内核同步序列号：

l*local-discr*：会话本地鉴别码

l*sequence-number*：同步的认证序列号

Process finish delete success LD: *local-discr*

删除带BFD_SESS_DELETING标记会话成功：

l*local-discr*：会话本地鉴别码

KEnter Auth change .Update old packet buffer.

配置的认证改变，更新旧的报文缓冲区

【举例】

\# 打开BFD事件调试信息开关。

\<Sysname\> debugging bfd event

\*Jul  4 13:36:59:481 2011 Sysname BFD/7/DEBUG: -MDC=1; Notify driver to stop receiving BFD packet

*// 停止接收BFD控制报文*

**BFD \-- BFD调试命令 \-- debugging bfd fsm**

------------------------------------------------------------------------

【命令】

**[debugging bfd fsm**]

**[undo debugging bfd fsm**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd fsm**]命令用来打开BFD状态机调试信息开关。**undo debugging bfd fsm**命令用来关闭BFD状态机调试信息开关。

缺省情况下，BFD状态机调试信息开关处于关闭状态。

表1-3 debugging bfd fsm命令输出信息描述表

字段

描述

FSM Proc packet status:1, session status:1, SlotNum:0

会话状态为down时收到状态为down的报文，会话状态变为Init

FSM Proc packet status:2, session status:1, SlotNum:0

会话状态为down时收到状态为Init的报文，会话状态变为up

FSM Proc packet status:2, session status:2, SlotNum:0

会话状态为Init时收到状态为Init的报文，会话状态变为up

Pkt Sta:Up, Sess Sta:Down, Oper:Keep session state and discard the packet

会话状态为down时收到状态为up的报文，会话状态保持不变，丢弃报文

Pkt Sta: Down, Sess Sta: Init, Oper: Keep session state and discard the packet

会话状态为Init时收到状态为down的报文，会话状态保持不变，丢弃报文

【举例】

\# 打开BFD状态机调试信息开关。

\<Sysname\> debugging bfd fsm

\*Jan  1 23:38:28:329 2000 Sysname BFD/7/DEBUG: FSM Proc packet status:2, session status:1, SlotNum:3

*// 会话在down状态收到Init状态报文*

**BFD \-- BFD调试命令 \-- debugging bfd ha**

------------------------------------------------------------------------

![说明](BFD%20Debug.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【命令】

**[debugging bfd ha**]

**[undo debugging bfd ha**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd ha**]命令用来打开BFD平滑事件调试信息开关。**undo debugging bfd ha**命令用来关闭BFD平滑事件调试信息开关。

缺省情况下，BFD平滑事件调试信息开关处于关闭状态。

表1-4 debugging bfd ha命令输出信息描述表

字段

描述

Ha standby to active

BFD进程收到HA升级事件

Ha active to standby

BFD进程收到HA降级事件

【举例】

\# 在启动了BFD功能的设备上打开平滑事件调试信息开关。

\<Sysname\> debugging bfd ha

\*Feb 17 11:04:47:153 2012 Sysname BFD/7/DEBUG: Ha standby to active

*[// BFD*]*进程收到HA升级事件*

**BFD \-- BFD调试命令 \-- debugging bfd ntfy**

------------------------------------------------------------------------

【命令】

**[debugging bfd ntfy**]

**[undo debugging bfd ntfy**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd ntfy**]命令用来打开BFD事件通知调试信息开关。**undo debugging bfd ntfy**命令用来关闭BFD 事件通知调试信息开关。

缺省情况下，BFD 事件通知调试信息开关处于关闭状态。

表1-5 debugging bfd ntfy命令输出信息描述

字段

描述

Notify application:*apptype* State:(*status*)

会话状态变化

Receive message, Application: *apptype* MsgType: APP_CreateSess

收到应用的创建会话消息信息

Receive application protocol *apptype* smooth end message

收到应用的平滑结束消息

【举例】

\# 打开BFD事件通知调试信息开关。

\<Sysname\> debugging bfd ntfy

\*Feb 17 11:04:47:153 2012 Sysname BFD/7/DEBUG: Receive message, Application:STATIC MsgType:APP_CreateSess [200.0.0.1/200.0.0.2, LD/RD:0/0, Interface:Vlan200, SessType:Ctrl, LinkType:INET, vrf:1]

%Feb 17 11:04:47:266 2012 Sysname BFD/6/FSM: Sess[200.0.0.1/200.0.0.2, LD/RD:68/34, Interface:Vlan200, SessType:Ctrl, LinkType:INET, Sta: DOWN-\>UP, Diag: 0]

\*Feb 17 11:04:47:268 2012 Sysname BFD/7/DEBUG: Notify application:STATIC State:UP

*// 新建会话，收到应用创建会话的消息*

**BFD \-- BFD调试命令 \-- debugging bfd packet**

------------------------------------------------------------------------

【命令】

**[debugging bfd packet **[[ { **receive** \| **send** } [ **acl** *acl-number* \| **acl6** *acl6-number* ] ]]]

**[undo debugging bfd packet **[[ **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[receive**]：接收报文调试信息开关。

**[send**]：发送报文调试信息开关。

**[acl ***acl-number*]：指定ACL的序号。*acl-number*表示ACL的序号，取值范围为2000～2999。

**[acl6 ***acl6-number*]：指定IPv6 ACL的序号。*acl6-number*表示IPv6 ACL的序号，取值范围为2000～2999。

【描述】

**[debugging bfd packet**]命令用来打开BFD报文调试信息开关。**undo debugging bfd packet**命令用来关闭BFD报文调试信息开关。

缺省情况下，BFD报文调试信息开关处于关闭状态。

表1-6 debugging bfd packet命令输出信息描述表

字段

描述

Received Simple packet authentication type not match. Discard packet.

Simple报文的认证类型不匹配

Received Simple packet length not match. Discard packet.

Simple报文的长度不匹配

Received Simple packet key ID not match. Discard packet.

Simple文的Key ID不匹配

Received Simple packet password not correct. Discard packet.

Simple报文的密码不正确

Received (M)MD5 packet authentication type not match. Discard packet.

(M)MD5报文的类型不匹配

Received (M)MD5 packet length not match. Discard packet.

(M)MD5报文的长度不匹配

Received (M)MD5 packet key ID not match. Discard packet.

(M)MD5报文的Key ID不匹配

Received (M)MD5 packet sequence number not match. Discard packet.

(M)MD5报文的序列号不匹配

Received (M)MD5 packet digest not match or calculate failed. Discard packet.

(M)MD5报文的摘要不匹配或者计算失败

Received (M)SHA1 packet HASH not match or calculate failed. Discard packet.

(M)SHA1报文的哈希不匹配或者计算失败

Received (M)SHA1 packet authentication type not match. Discard packet.

(M)SHA1报文的认证类型不匹配

Received (M)SHA1 packet length not match. Discard packet.

(M)SHA1报文的长度不匹配

Received (M)SHA1 packet key ID not match. Discard packet.

(M)SHA1报文的Key ID不匹配

Received (M)SHA1 packet sequence number not match. Discard packet.

(M)SHA1报文的序列号不匹配

Received none authentication type packet. Discard packet.

收到不带认证报文，与本地会话认证类型不匹配

Received invalid authentication type packet. Discard packet.

收到无效认证类型的报文

Failed to check Mbuffer. Discard packet.

报文的Mbuffer检查失败

ADP master received packets from other self. Discard packet.

ADP模式下，主控板收到其它板的报文

Direct not match. Discard packet.

判断是否直连，报文与本地不匹配

SelfID not match. Discard packet.

维护板ID不匹配

Session information not match. Discard packet.

会话状态、CRTL/ECHO类型不匹配

UDP protocol error. Discard packet.

UDP报文协议字段错误

UDP checksum error. Discard packet.

UDP报文检验和验证失败

Invalid UDP source port. Discard packet.

UDP报文源端口错误

Invalid UDP destination port. Discard packet.

UDP报文目的端口错误

Incorrect UDP length. Discard packet.

UDP报文长度字段错误

Received packet source address is not match. Discard packet.

报文中源地址和本地源地址不匹配

Received packet destination address is not match. Discard packet.

报文中目的地址和本地目的地址不匹配

Interface index not match. Discard packet.

报文入接口索引不匹配

\'Vers\' bit is invalid. Discard packet.

\'Vers\'位无效

\'P\' & \'F\' bits are invalid. Discard packet.

\'P\' & \'F\'位无效

\'Multipoint\' bit is invalid. Discard packet.

保留位无效

\'Detect Mult\' bit is invalid. Discard packet.

\'Detect Mult\'位无效

\'Length\' bit is invalid. Discard packet.

\'Length\'位无效

\'My Discriminator\'(equals to zero) is invalid. Discard packet.

报文\'My Discriminator\'为0，错误的报文

Received packet discriminator is not match. Discard packet

报文中ID和本端ID匹配不成功

Received packet address is not match. Discard packet

报文中地址和本端地址匹配不成功

Interface PhyStatus is down. Discard packet.

接口物理状态down

KAuthentication type not match, session type: *sess-auth-type*, packet type: packet-auth-type.

报文与本地会话的认证类型不匹配：

l*sess-auth-type*：会话认证类型

l*packe-tauth-type*：报文认证类型

KCheck old authentication, session type: *sess-auth-type*, packet type:packet-auth-type.

报文与本地会话的旧认证类型不匹配：

l*sess-auth-type*：会话认证类型

l*packet-auth-type*：报文认证类型

Authentication type *type* is not supported

认证类型不支持：

l*type*：认证类型

KL2 Send: *packet-string* ErrCode: *error-code*.

二层发送报文：

l*packet-string*：报文转换的信息字符串，包含BFD报文的基本信息和扩展信息等

l*error-code*：报文发送后返回的错误码

【举例】

\# 打开BFD发送报文调试信息开关。

\<Sysname\> debugging bfd packet send

\*Jul  4 14:57:58:311 2011 Sysname BFD/7/DEBUG: -MDC=1; [K L2 Send:Ctrl packet, Src:10.1.1.1, Dst:10.1.1.2, Ver:1, Diag:0, Sta:3, P/F/C/A/D/M:0/0/1/0/0/0, mult:5, LD/RD:513/514, Tx:500ms, Rx:500ms, EchoRx:500ms]

*// 控制报文信息：源地址为10.1.1.2、目的地址为10.1.1.1、版本1、诊断码0、状态3、各标记位P/F/C/A/D/M分别为0/0/1/0/0/0、检测系数5、本地鉴别码513、对端鉴别码514、最小发送间隔500ms、最小接收间隔500ms、最小ECHO接收间隔500ms*

\# 打开BFD接收报文调试信息开关。

\<Sysname\> debugging bfd packet receive

\*Jul  4 15:02:20:045 2011 Sysname BFD/7/DEBUG: -MDC=1; [K Recv:Ctrl packet, Src:fe80::102, Dst:fe80::101, Ver:1, Diag:0, Sta:3, P/F/C/A/D/M:0/0/1/0/0/0, mult:10, LD/RD:517/513, Tx:500ms, Rx:500ms, EchoRx:500ms]

*// 控制报文信息：源地址为fe80::101、目的地址为fe80::102、版本1、诊断码0、状态3、各标记位P/F/C/A/D/M分别为0/0/1/0/0/0、检测系数5、本地鉴别码517、对端鉴别码513、最小发送间隔500ms、最小接收间隔500ms、最小ECHO接收间隔500ms*

**BFD \-- BFD调试命令 \-- debugging bfd scm**

------------------------------------------------------------------------

【命令】

**[debugging bfd scm**]

**[undo debugging bfd scm**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd scm**]命令用来打开BFD会话控制管理调试信息开关。**undo debugging bfd scm**命令用来关闭BFD会话控制管理调试信息开关。

缺省情况下，BFD会话控制管理调试信息开关处于关闭状态。

表1-7 debugging bfd scm命令输出信息描述表

字段

描述

Create session success:(*application message*)

创建会话成功

Delete session success:(*application message*)

删除会话成功

Reset session LD:(*Local Discriminator*)

重置会话

Switch control to *device-info*, LD *local-discr* XmitAuthSeq: *sequence-number*

会话维护权迁移到其它板：

l*device-info*：设备信息

l*local-discr*：会话本地鉴别码

l*sequence-number*：认证序列号

【举例】

\# 打开BFD会话控制管理调试信息开关。

\<Sysname\> debugging bfd scm

\*Jul  4 15:11:52:654 2011 Sysname BFD/7/DEBUG: -MDC=1; Delete session success [10.1.1.1/10.1.1.2, LD/RD:513/514, Interface:GE1/0/1, SessType:Ctrl, LinkType:INET]

\*Jul  4 15:11:52:655 2011 Sysname BFD/7/DEBUG: -MDC=1; Delete session success [10.1.1.1/10.1.1.2, LD/RD:513/514, Interface:GE1/0/1, SessType:Ctrl, LinkType:INET]

*// 删除BFD会话*

**BFD \-- BFD调试命令 \-- debugging bfd timer**

------------------------------------------------------------------------

【命令】

**[debugging bfd timer**]

**[undo debugging bfd timer**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bfd timer**]命令用来打开BFD定时器事件调试信息开关。**undo debugging bfd timer**命令用来关闭BFD定时器事件调试信息开关。

缺省情况下，BFD定时器事件调试信息开关处于关闭状态。

表1-8 debugging bfd timer命令输出信息描述表

字段

描述

Create send-packet/detect-packet timer

创建用户态发送/监测定时器

Delete session *send/ detect* timer

删除内核态发送/监测定时器

Update session *send/detect* timer

删除内核态发送/检测定时器

Detect timer expired

监测定时器超时

Start *send timer*, LD:*ldvalue*, mdc:*mdcvalue*

内核态创建发送定时器

Change *send /detect* time, LD:*ldvalue*, Old:*timevalue* ms, New: *timevalue* ms

修改定时器时间间隔

KBFD: Delete CCF reinit timer.

删除CCF重初始化定时器

KBFD: Reset CCF reinit timer.

起CCF重新初始化定时器

KBFD: Delete CCF reinit timer.

删除CCF重新初始化定时器

KBFD: Create CCF reinit timer *timer-id*.

创建CCF重新初始化定时器：

l*timer-id*：定时器ID

【举例】

\# 打开BFD定时器事件调试信息开关。

\<Sysname\> debugging bfd timer

\*Feb 17 13:42:06:576 2012 Sysname BFD/7/DEBUG: Create send timer[1000ms success, LD:68]

%Feb 17 13:42:06:743 2012 Sysname BFD/6/FSM: Sess[200.0.0.1/200.0.0.2, LD/RD:68/34, Interface:Vlan200, SessType:Ctrl, LinkType:INET, Sta: DOWN-\>UP, Diag: 0]

\*Feb 17 13:42:06:744 2012 Sysname BFD/7/DEBUG: Change detect time, LD:68, Old:5000ms, New:10000ms

\*Feb 17 13:42:06:748 2012 Sysname BFD/7/DEBUG: Delete send timer [LD:68]

\*Feb 17 13:42:06:748 2012 Sysname BFD/7/DEBUG: -Slot=1; [K Start send timer, LD:68, mdc:1]

*// 创建Ctrl报文发送定时器和控制报文发送定时器为1000ms，会话（200.0.0.1/200.0.0.2, Vlan200, Ctrl）状态由down变为up，诊断码为0（无诊断信息）的BFD会话信息*

