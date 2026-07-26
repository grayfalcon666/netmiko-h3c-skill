
**OAP \-- OAP调试命令 \-- debugging oap**

------------------------------------------------------------------------

【命令】

**[debugging oap **[{ **all** \| **error** \| **event** \| **packet** \| **fsm** }]]

**[undo debugging oap **[{ **all** \| **error** \| **event** \| **packet** \| **fsm** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]**：**表示OAP所有调试信息开关。

**[error**]**：**表示OAP错误调试信息开关。

**[event**]**：**表示OAP事件调试信息开关。

**[packet**]**：**表示OAP报文调试信息开关。

**[fsm**]**：**表示OAP状态机调试信息开关。

【描述】

**[debugging oap**]命令用来打开OAP的调试信息开关。

**[undo debugging oap**]命令用来关闭OAP的调试信息开关。

缺省情况下，OAP的调试信息开关处于关闭状态。

表1-1 **debugging oap error**命令输出信息描述表

字段

描述

Failed to save OAP multicast MAC address 01:0F:E2:00:00:21. Can't enable OAP function on interface *interface-name.*

保存OAP协议组播MAC地址(01:0F:E2:00:00:21)失败，不能在接口*interface-name*启用OAP功能

Failed to save OAP unicast MAC address 58:66:BA:4D:FB:2A. Can't enable OAP function on interface *interface-name.*

保存OAP协议单播MAC地址([58:66:BA:4D:FB:2A)]失败，不能在接口*interface-name*启用OAP功能

Failed to send reply message. File handle: *socketfd*; Error code: *error-code*.

发送OAP回应消息失败，*socketfd*为文件句柄*，**error-code*为返回错误码

Failed to save client information to the local running DBM.

保存OAP客户端信息到本地运行数据库失败

Failed to save OAP status to the configuration DBM.

保存OAP使能状态到配置数据库失败

Failed to save monitor time to the configuration DBM.

保存监控定时器时间到配置数据库失败

Failed to save clock synchronization time to the configuration DBM.

保存时钟同步定时器时间到配置数据库失败

Interface *ifindex* is down.

报文接收接口已经down，*ifindex*为接口索引

OAP is disabled on interface *interface-name*.

OAP协议在接口*interface-name*上未启用

Discarded packet: Invalid packet length *packet-length*.

丢弃报文，因为报文长度非法，*packet-length*为非法的报文长度，这里和下面涉及到的长度都以字节为单位

Discarded packet: Invalid version *version*.

丢弃OAP协议版本号非法的报文，*version*为非法的协议版本号

Discarded packet: The packet was from another OAP manager.

丢弃来自其他OAP manager的报文

Discarded packet: Invalid packet type *pack**et-type*.

丢弃报文，OAP manager收到非法的报文类型*packet-type*

Discarded *packet-type-description* packet: Invalid OAP head length. OAP head length: *oaphead-length*; remaining length: *remaining-length*.

丢弃*packet-type-[description]*报文，原因是OAP协议头长度字段非法，其中*oaphead-length*为头部中长度字段的值，*remaining-length*为报文剩余长度，*packet-type-[description]*取值如下：

·register：注册报文

·information：信息报文

·monitor：监控报文

·deregister：注销报文

Discarded *packet-type-description* packet: Invalid client ID *client-id*.

丢弃*packet-type-[description]*报文，原因是OAP协议头client ID字段*client-id*非法，*packet-type-[description]*取值如下：

·information：信息报文

·monitor：监控报文

Discarded register request packet: Invalid client ID *clien**t-id*.

丢弃注册请求报文，原因是OAP协议头client ID字段*client-id*非法

Discarded register request packet: Invalid destination MAC address *d**st-mac*.

丢弃注册请求报文，原因是目的MAC地址*dst-mac*非法

Discarded *packet-type-description* packet: Invalid destination MAC address *dst-ma**c*.

丢弃*packet-type-[description]*报文，原因是目的MAC地址*dst-mac*非法，*packet-type-[description]*取值如下：

·information：信息报文

·monitor：监控报文

·deregister：注销报文

Discarded deregister packet: Invalid source MAC address *src-**mac*.

丢弃注销报文，原因是源MAC地址*src-mac*非法

Discarded *packet-type-description* packet: Inconsistent interfaces. Client ID: *client-id;* Registered interface: *client-interface-name*; Inbound interface: *packet-interface-name.*

丢弃*packet-type-[description]*报文，原因是报文接收接口与客户端*client-id*注册时的接口不一致，其中*packet-interface-name*为报文接收接口名，*client-interface-name*为客户端注册时的接口名，*packet-type-[description]*取值如下：

·information：信息报文

·monitor：监控报文

·deregister：注销报文

Discarded *packet-type-description* packet: Inconsistent source MAC addresses. Client ID: *client-id;* Registered MAC: *cli**ent-Mac*; Source MAC in packet: *packet-srcMac.*

丢弃*packet-type-[description]*报文，原因是报文的源MAC与客户端*client-id*注册信息中的MAC地址不一致，其中*packet-srcMac*为报文以太头源MAC地址，*client-Mac*为客户端MAC，*packet-type-[description]*取值如下：

·information：信息报文

·monitor：监控报文

·deregister：注销报文

Discarded *packet-type-description* packet: Inconsistent protocol types. Client ID: *client-id;* Registered protocol type: *client-protocoltype*; Protocol type in packet: *packet-protocoltype.*

丢弃*packet-type-[description]*报文，原因是报文的以太网协议类型与客户端*client-id*注册信息中的不一致，其中*packet-protocoltype*为报文以太头中的协议类型，*client-protocoltype*为客户端注册时的协议类型，*packet-type-[description]*取值如下：

·information：信息报文

·monitor：监控报文

·deregister：注销报文

Discarded *packet-type-description* packet: Client *client-id* doesn't exist.

丢弃*packet-type-[description]*报文，原因是指定客户端*client-id*不存在，*packet-type-[description]*取值如下：

·information：信息报文

·monitor：监控报文

·deregister：注销报文

Discarded packet: Invalid inner head length *oapInnerH**ead-length.*

丢弃报文，原因是OAP协议内部头中的长度字段非法，*oapInnerHead-length*为非法的OAP内部头长度值

Discarded register request packet: Invalid inner code *oapInnerH**ead-code*.

丢弃注册请求报文，原因是OAP协议内部头中的code字段非法，*oapInnerHead-code*为非法的code值

Discarded monitor packet: Unsupported subtype *oapInnerHead-code*.

丢弃监控报文，原因是OAP manager收到暂不支持的监控报文子类型，oapInnerHead-code为非法的code值

Discarded register request packet: Invalid MUMA MAC TLV length *tlv-length*.

丢弃注册请求报文，原因是携带的MUMA  MAC类型TLV长度非法，*tlv-length*为非法的TLV长度

Discarded register request packet: The packet format is too old and not supported.

丢弃注册请求报文，原因是老报文格式目前已不支持

Discarded monitor request packet: Invalid magic number TLV length *tlv-length*.

丢弃监控请求报文，原因是携带的魔术数字类型TLV长度非法，*tlv-length*为非法的TLV长度

Discarded monitor ACK packet: Invalid magic number TLV length *tlv-length*.

丢弃监控确认报文，原因是携带的魔术数字类型TLV长度非法，*tlv-length*为非法的TLV长度

Discarded monitor ACK packet: Inconsistent identifiers or magic numbers. In received packet: Identifier=*packet-identifier*  Magic number=*packet-magicnum*. In client *client-id*:      Identifier*=client-identifier*  Magic number=*client-magicnum*.

丢弃监控确认报文，原因是收到客户端*client-id*的监控确认报文中的序列号或魔术数字与客户端注册信息中保存的不一致。其中*packet-identifier*为报文中的报文序列号，*packet-magicnum*为报文中携带的魔术数字，*client-identifier*为客户端注册信息中的报文序列号，*client-magicnum*为客户端注册信息中的魔术数字

Discarded extended monitor request packet: Invalid cookie TLV length *tlv-length*.

丢弃扩展监控请求报文，原因是携带Cookie类型TLV长度非法，*tlv-length*为非法的TLV长度

Invalid TLV length *tlv-length* in information packet.

客户端信息通告报文携带的TLV长度非法，*tlv-length*为非法的TLV长度

Unsupported TLV type *tlv-type* in information packet.

客户端信息通告报文携带暂不支持的TLV类型，*tlv-type*为不支持的TLV类型

Discarded information packet: All TLVs are invalid.

丢弃信息通告报文，原因是客户端信息通告报文携带的所有TLV都非法

Discarded monitor request packet: No magic number TLV.

丢弃监控请求报文，原因是没有携带魔术数字类型TLV

Discarded monitor ACK packet: No magic number TLV.

丢弃监控确认报文，原因是没有携带魔术数字类型TLV

Discarded extended monitor request packet: No cookie TLV.

丢弃扩展监控请求报文，原因是没有携带Cookie类型TLV

Failed to add client because memory is insufficient.

内存不够，添加OAP客户端失败

Failed to send packet on interface *interface-name*.

在接口*interface-name*发送报文失败

Announce timer failed.

通知定时器失败

Connect timer failed.

定时器连接失败

表1-2 **debugging oap event**命令显示信息描述表

字段

描述

Number of monitor request packets with no responses reached the upper limit.

没有得到回应的监控请求报文数达到上限

OAP *event-type* event occurred on interface *interface-name* because *reason*.

接口*interface-name*发生*event-type*事件，*event-type*取值包括：

·registered：Client注册事件

·deregistered：Client注销事件

*[reason*]包括如下：

·register packet was received：收到注册报文

·OAP was disabled：关闭OAP协议

·monitor was timed out：监控超时

·deregister packet was received：收到注销报文

·interface was inactive：接口去激活

表1-3 **debugging oap packet**命令显示信息描述表

字段

描述

Sent OAP packet

发送OAP协议报文

Received OAP packet

接收OAP协议报文

Interface: *interface-name*

报文承载接口名

Destination MAC: *dst-mac*

报文的目的MAC地址

Source MAC: *src-mac*

报文的源MAC地址

Protocol Type: *protocol-type*

以太网协议类型

Sub-Type: *sub-type*

OAP协议子类型

Reserved: *reserved-value*

报文子协议保留位

Version: *version*

OAP协议版本

Sender:*Client or Manager*

报文的发送者，*Client*表示OAP client发送的报文，*Manager*表示OAP manager发送的报文。

Packet Type: *packet-type*

报文类型，* packet-type*取值如下:

·Register：注册报文

·Inform：信息通告报文

·Operate：操作通告报文

·Monitor：监控报文

·Deregister：注销报文

Client ID: *client-id*

客户端标识

Length: *length*

OAP协议头中长度字段的值，包括OAP头和后续实际报文数据的长度

Code: *code*

注册或监控报文的子类型：

·注册报文分为以下三种，code取值如下：

¡Register request：注册请求

¡Register ACK：注册确认

¡Register reject：注册拒绝

·监控报文分为以下四种，code取值如下：

¡Monitor request：监控请求

¡Monitor ACK：监控确认

¡Extended monitor request：扩展监控请求

¡Extended monitor ACK：扩展监控确认

Identifier: *identifier*

注册或监控报文的序列号

Length: *length*

OAP协议内部头中长度字段的值，包括OAP协议内部头和后续实际报文数据的长度

TLV info:    

报文TLV信息提示，表示后续内容为报文携带TLV信息，每个TLV信息单独打印

Type: *tlv-type*

TLV类型，*tlv-type*为报文携带的TLV类型，不识别的类型显示为"Unknown TLV"

Length: *tlv-length*

单个TLV的长度

Value: *tlv-value*

TLV中的Value值，如果TLV长度为2，则该处显示为"None"

表1-4 **debugging oap fsm**命令显示信息描述表

字段

描述

Client *client-id* in *status* state: Sending *pkt-type* packet on interface *interface-name.*

OAP manager将在接口*interface-name*向状态为*status*的客户端发送*pkt-type*报文，其中：

*[client-id*]：客户端ID

*[interface-name*]：客户端注册接口

*[pkt-type*]：发送的报文类型，取值如下：

·register ACK：表示发送注册确认报文

·register reject：表示发送注册拒绝报文

·clock synchronization：表示发送时钟同步信息报文

·time zone synchronization：表示发送时区同步信息报文

·port context information：表示发送Port Context信息报文

·monitor request：表示发送监控请求报文

·monitor ACK：表示发送监控确认报文

·extended monitor ACK：表示发送扩展监控确认报文

·close operation：表示发送关闭操作报文

·reboot operation：表示发送重启操作报文

*[status*]：客户端状态，取值如下：

·registered：Client成功注册

·unregistered：Client未注册

Client *client-id* in *status* state, interface *interface-name*: Received *event-type* event*.

接口*interface-name*下注册的客户端在状态*status*下收到*event-type*事件，其中：

*[client-id*]：客户端ID

*[interface-name*]：客户端注册接口

*[event-type*]：事件类型，取值如下：

·Interface_Inactive：接口去激活

·Interface_LinkUp：接口UP

·Interface_LinkDown：接口DOWN

·Oap_Disable：OAP去使能

·Operation_Close：关闭操作

·Operation_Reboot：重启操作

·Client_Delete：删除客户端

·MonitorTimer_Pause：暂停监控定时器

·RegisterRequest_Receive：收到注册请求报文

·MonitorTimer_Expire：监控定时器超时

·MonitorResponse_Receive：收到监控确认报文

·MonitorRequest_Receive：收到监控请求报文

·ExtendedMonitorRequest_Receive：收到监控扩展请求报文

·ClockSyncTimer_Expire：时钟同步定时器超时

·Information_Receive：收到信息通告报文

·Deregister_Receive：收到注销请求报文

·Context_Change：收到驱动报文头信息

*[status*]：客户端状态，取值如下：

·registered：Client成功注册

·unregistered：Client未注册

Client *client-id*, interface *interface-name*: Entered *status* state.

接口*interface-name*下注册的客户端进入*status*状态，其中：

*[client-id*]：客户端ID

*[interface-name*]：客户端注册接口

*[status*]：客户端状态，取值如下：

·registered：Client成功注册

·unregistered：Client未注册

Client *client-id*, interface *interface-name*: Number of monitor request packets with no responses changed from *old-value* to *new-value*.

打印没有得到回应的监控请求报文数从*old-value*变到*new-value*，其中：

*[client-id*]：客户端ID

*[Interface-name*]：客户端注册接口

Client *client-id*, interface *interface-name*, *info-type* info: *info-context*.

打印驱动报文头信息或Cookie信息，其中：

*[client-id*]：唯一标识一个Client

*[interface-name*]：承载接口名

*[info-type*]：信息类型，取值包括如下：

·context：驱动报文头信息

·cookie：Cookie信息

*[info-context*]：驱动报文头信息或Cookie信息内容，如果长度为0，该字段显示"None"

Updating client information of client *client-id.*

更新客户端*client-id*信息

Client *client-id*, interface *interface-name*: Monitor timer expired, number of monitor request packets with no responses is *new-value*.

监控定时器超时，没有得到回应的监控请求报文数变为*new-value*，其中

*[client-id*]：客户端ID

*[interface-name*]：客户端注册接口

Handling registering client which has same interface index and same source MAC address as a registered client.

处理注册OAP客户端的接口索引与MAC地址和已注册的客户端相同

Handling registering client which has same interface index as a registered client but their source MAC addresses are different.

处理注册OAP客户端的接口索引与已注册的客户端相同，但MAC地址不同

Handling registering client which has same source MAC address as a registered client but their interface indexes are different.

处理注册OAP客户端的MAC地址与已注册的客户端相同，但接口索引不同

Handling registering client which has different interface index and different source MAC address as a registered client.

处理注册OAP客户端的接口索引与MAC地址和已注册的客户端都不相同

Failed to register on interface *interface-name*: *reject-reason.*

客户端在接口*interface-name*下注册失败，注册拒绝原因*reject-reason*有如下情况：

·The client has been registered with the client ID client-id OAP客户端client-id重复注册

·No client ID available 没有可分配的合法客户端ID

·Unknown reason 未知原因

Registered a new client on interface *interface-name*. Client: *client-id;* Protocol: *protocol-type;* MAC: *client-mac*; MUMA MAC: *muma-mac;* Register time: *register-time*.

在接口*interface-name*成功注册新的客户端，其中：

*[client-id*]：新注册的客户端ID

*[protocol-type*]：客户端注册时的协议类型

*[client-mac*]：客户端MAC地址

*[muma-mac*]：客户端携带的MUMA  MAC地址

*[register-time*]：注册时间

【举例】

\# OAP client向OAP manager注册。

打开OAP所有调试开关，在接口*GigabitEthernet 1/0/1*上启用OAP功能。

\<Sysname\> terminal monitor

\<Sysname\> debugging oap all

\<Sysname\> system-view

Sysname interface Ethernet 1/1

Sysname-Ethernet1/1 oap enable

\*Apr 17 08:00:33:224 2012 Sysname OAP/7/PKT: -MDC=1; Received OAP packet.

  Interface: Ethernet1/1;

  Destination MAC: 010f-e200-0021;  Source MAC: 0000-5e61-8901;

  Protocol Type: 88a7;  Sub-Type: 0007;  Reserved: 0000;

  Version: 1;  Sender: Client;  Packet Type: Register;

  Client ID: 0;  Length: 18;

  Code: Register request;  Identifier: 1;  Length: 12.

\*Apr 17 08:00:33:224 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:

  Type: Client MUMA MAC;  Length: 8;  Value: 0011-2233-4455.

*[//*]*报文调试信息：OAP manager在接口Ethernet 1/1上收到客户端（MAC地址为0000-5e61-8901）发送的注册请求报文，携带的MUMA MAC为0011-2233-4455*

\*Apr 17 08:00:33:224 2012 Sysname OAP/7/FSM: -MDC=1; Client 0 in unregistered state, interface Ethernet1/1: Received RegisterRequest_Receive event.

*[//*]*状态机调试信息：OAP manager在接口Ethernet 1/1上接受到注册请求报文*

\*Apr 17 08:00:33:224 2012 Sysname OAP/7/FSM: -MDC=1; Handling registering client which has different interface index and different source MAC address as a registered client.

*[//*]*状态机调试信息：OAP manager在接口Ethernet 1/1上处理接口索引和MAC都不相同的注册客户端*

\*Apr 17 08:00:33:225 2012 Sysname OAP/7/EVENT: -MDC=1; OAP registered event occurred on interface Ethernet1/1 because register packet was received.

*[//*]*事件调试信息：接口Ethernet 1/1发生OAP注册事件，原因是收到注册报文*

\*Apr 17 08:00:33:226 2012 Sysname OAP/7/FSM: -MDC=1; Registered a new client on interface Ethernet 1/1. Client: 1; Protocol: 0x88a7; MAC: 0000-5e61-8901; MUMA MAC: 0011-2233-4455; Register time: 04/17/2012 08:00:33.

*[//*]*状态机调试信息：接口Ethernet 1/1成功注册客户端，客户端ID(1)，协议号(0x88a7)，客户端MAC地址(0000-5e61-8901)，客户端携带MUMA MAC(0011-2233-4455)，注册时间(04/17/2012 08:00:33)*

\*Apr 17 08:00:33:226 2012 Sysname OAP/7/FSM: -MDC=1; Client 1, interface Ethernet1/1, context info:

  0x4f 41 50 20 64 72 76 20 74 65 73 74 00.

*[//*]*状态机调试信息：获取OAP manager的驱动报文头信息，按单字节十六进制格式打印*

\*Apr 17 08:00:33:226 2012 Sysname OAP/7/FSM: -MDC=1; Client 1 in registered state: Sending register ACK packet on interface Ethernet1/1.

*[//*]*状态机调试信息：OAP manager在接口Ethernet 1/1向客户端1发送注册确认报文*

\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; Sent OAP packet.

  Interface: Ethernet1/1;

  Destination MAC: 0000-5e61-8901;  Source MAC: 5866-ba4d-fb2a;

  Protocol Type: 88a7;  Sub-Type: 0007;  Reserved: 0000;

  Version: 1;  Sender: Manager;  Packet Type: Register;

  Client ID: 1;  Length: 93;

  Code: Register ACK;  Identifier: 1;  Length: 87.

\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:

  Type: Internal port attribute;  Length: 10;

  Value (interface index, attribute): 20, 3.

\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:

  Type: Driver context;  Length: 15;

  Value:

  0x4f 41 50 20 64 72 76 20 74 65 73 74 00.

\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:

  Type: Internal port slot number;  Length: 10;

  Value (interface index, slot number): 20, 0.

\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:

  Type: Internal port subslot number;  Length: 10;

  Value (interface index, subslot number): 20, 1.

\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:

  Type: Internal port name;  Length: 26;

  Value (interface index, port name): 20, Ethernet1/1.

\*Apr 17 08:00:33:227 2012 Sysname OAP/7/PKT: -MDC=1; TLV info:

  Type: Manager MUMA MAC;  Length: 12;

  Value (interface index, MUMA MAC): 20, 5866-ba4d-fb2a.

*[//*]*报文调试信息：OAP manager在接口Ethernet 1/1向客户端1发送注册确认报文*

\*Apr 17 08:16:49:519 2012 Sysname OAP/7/ERROR: -MDC=1; Discarded packet: Invalid version (2).

*[//*]*错误调试信息：OAP协议版本号非法*

