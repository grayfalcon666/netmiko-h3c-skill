<!-- CMD-INDEX
  debugging l2tp                      | 用户视图             | L5
-->

**L2TP \-- L2TP调试命令 \-- debugging l2tp**

------------------------------------------------------------------------

【命令】

**[debugging l2tp**[ { **all** \| **avp**-**hidden** \| **control-packet** \| **data-packet** \| **dump** \| **error** \| **event** }]]

**[undo debugging l2tp**[ { **all** \| **avp**-**hidden** \| **control-packet** \| **data-packet** \| **dump** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有L2TP调试信息开关。

**[avp-hidden**]：表示隐藏AVP的调试信息开关。

**[control-packet**]：表示L2TP控制报文调试信息开关。

**[data-packet**]：表示L2TP数据报文调试信息开关。

**[dump**]：表示PPP报文调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging l2tp**]命令用来打开L2TP的调试信息开关。**undo debugging l2tp**命令用来关闭L2TP的调试信息开关。

缺省情况下，L2TP的调试信息开关处于关闭状态。

表1-1 debugging l2tp avp-hidden命令输出信息描述表

字段

描述

*[AVP-type* AVP was hidden.]

隐藏了类型为*AVP-type*的AVP

表1-2 debugging l2tp control-packet命令输出信息描述表

字段

描述

Received *message-type* packet from port 1701 (TunnelID=*tunnel-id*, length=*length*, Ns=*ns*, Nr=*nr*). Packet content: *content*

从端口1701接收到*message-type*类型的报文，报文所属隧道的Tunnel ID为*tunnel-id*，报文长度为*length*，Ns为*ns*，Nr为*nr*，报文内容为*content*

其中，*message-type*取值包括ZLB-ACK、UNKNOWN、Reserved、SCCRP、SCCCN、StopCCN、Hello、ICRQ、ICRP、ICCN、CDN、WEN和SLI

Received *message-type* packet from port 1701 (length=*length*, Ns=*ns*, Nr=*nr*). Packet content: *content*

从端口1701接收到*message-type*类型的报文，报文长度为*length*，Ns为*ns*，Nr为*nr*，报文内容为*content*

其中，*message-type*取值包括SCCRQ、UNKNOWN和Reserved

Encapsulated *AVP-type* AVP: *encapsulated-avp*

封装类型为*AVP-type*的AVP。封装后AVP的内容为*encapsulated-avp*

表1-3 debugging l2tp data-packet命令输出信息描述表

字段

描述

Encapsulated an L2TP data packet on interface *interface-name* (length*=length*):

 Source IP: *source-ip*

**[Destination IP: *destination-ip*]

 Source port: *source-port*

 Destination port: *destination-port*

 Tunnel ID: *tunnel-id*

 Session ID: *session-id*

在接口*interface-name*上封装一个L2TP数据报文

·{.TableTextChar}报文长度为*length*

·{.TableTextChar}源IP地址为*source-ip*

·{.TableTextChar}目的IP地址为*destination-ip*

·{.TableTextChar}源端口号为*source-port*

·{.TableTextChar}目的端口号为*destination-port*

·{.TableTextChar}隧道ID为*tunnel-id*

·会话ID为*session-id*

Received an L2TP data packet:

 Source IP: *source-ip*

**[Destination IP: *destination-ip*]

 Source port: *source-port*

 Destination port: *destination-port*

接收到一个L2TP数据报文

·源IP地址为*source-ip*

·目的IP地址为*destination-ip*

·源端口号为*source-port*

·目的端口号为*destination-port*

Successfully parsed the L2TP header (L2TP header length=*length*):

 Tunnel ID: *tunnel-id*

 Session ID: *session-id*

 Ns: *ns*

 Type: *type*

 Length: *length*

 Sequence: *sequence*

 Offset: *offset*

 Priority: *priority*

成功解析L2TP数据报文头，报文头长度为*length*，报文头的内容为：

·隧道ID为*tunnel-id*

·会话ID为*session-id*

·{.TableTextChar}Ns为*ns*

·{.TableTextChar}报文类型值为*type*

·{.TableTextChar}报文长度为*length*

·{.TableTextChar}报文的序列号为*sequence*

·{.TableTextChar}报文的偏移量为*offset*

·报文的优先级为*priority*

FlowCtrl: Received an L2TP data packet. TunnelID=*tunnel-id*, SessionID=*session-id*, Ns=*Ns*, ENs=*ENs1*. After receiving the packet, ENs changed to *ENs2*.

流控：收到了隧道ID为*tunnel-id*、会话ID为*session-id*的L2TP数据报文。报文的Ns为*Ns*，期望的报文序列号为*ENs1*。接收到该L2TP报文后，期望的报文序列号变成*ENs2*

No FlowCtrl: Received an L2TP data packet. TunnelID*=tunnel-id*, SessionID*=session-id.*

非流控：收到了隧道ID为*tunnel-id*、会话ID为*session-id*的L2TP数据报文

Invalid FlowCtrl: Dropped an L2TP data packet. TunnelID=*tunnel-id*, SessionID=*session-id*.

异常的流控：丢弃隧道ID为*tunnel-id*、会话ID为*session-id*的L2TP数据报文

Transparently transmitted an L2TP data packet to slot *slot-value*. TunnelID=*tunnel-id*, SessionID=*session-id*.

把隧道ID为*tunnel-id*、会话ID为*session-id*的数据报文透传到目的板*slot-value*

Processed an L2TP data packet. TunnelID*=tunnel-id*, SessionID*=session-id*.

处理隧道ID为*tunnel-id*、会话ID为*session-id*的L2TP数据报文

Dropped an L2TP data packet.

丢弃一个L2TP数据报文

表1-4 debugging l2tp dump命令输出信息描述表

字段

描述

Received a packet from PPP on interface *interface-name* (length=*length*): *packet-content*

在接口*interface-name*上从PPP收到一个数据报文，报文长度为*length*，报文内容为*packet-content*

Sent a packet to PPP on interface *interface-name* (length=*length*): *packet-content*

在接口*interface-name*上向PPP发送一个数据报文，报文长度为*length*，报文内容为*packet-content*

表1-5 debugging l2tp error命令输出信息描述表

字段

描述

Failed to reclaim tunnel ID *tunnel-id*.

回收值为*tunnel-id*的隧道ID失败

Failed to delete interface *interface-name*.

删除名为*interface-name*的接口失败

TunnelID=*tunnel-id*: Failed to save tunnel information to database.

将隧道ID为*tunnel-id*的隧道信息保存到数据库失败

TunnelID=*tunnel-id*, SessionID=*session-id*: Failed to save session information to database.

将隧道ID为*tunnel-id*、会话ID为*session-id*的会话信息保存到数据库失败

TunnelID=*tunnel-id*: Failed to update Ns and Nr information to database.

在隧道*tunnel-id*中，更新隧道的Ns和Nr信息到数据库失败

TunnelID=*tunnel-id*: Failed to resend packet, Ns=*ns*, Nr=*nr*.

在隧道*tunnel-id*中，重发Ns为*ns*、Nr为*nr*的报文失败

TunnelID=*tunnel-id*: Failed to send packet.

在隧道*tunnel-id*中，发送报文失败

Received StopCCN packet. Due to the invalid tunnel ID, processed the packet without using the state machine.

收到StopCCN报文，但报文头中的隧道ID为无效值，所以不利用状态机处理此报文

TunnelId=*tunnel-id*: Failed to reset ACK timer when acknowledging transmit window.

在隧道*tunnel-id*中，确认发送窗口时刷新ACK定时器失败

TunnelID= *tunnel-id*: Failed to reset Hello timer.

在隧道*tunnel-id*中，重置Hello定时器失败

TunnelID=*tunnel-id*: Failed to reset ACK timer.

在隧道*tunnel-id*中，重置ACK定时器失败

TunnelID= *tunnel-id*: Failed to reset Hello timer by command.

在隧道*tunnel-id*中，命令触发的Hello定时器刷新失败

TunnelID=*tunnel-id*: Failed to send ZLB-ACK packet*, Ns=ns, Nr=nr*.

在隧道*tunnel-id*中，发送ZLB-ACK报文失败，报文的Ns为*ns*、Nr为*nr*

Failed to send packet.

发送报文失败

TunnelID=*tunnel-id*: Failed to create *timer-type* timer.

在隧道*tunnel-id*中，创建类型为*timer-type*的定时器失败

其中，*timer-type*取值包括ACK、Delay-Cleanup、Hello和Delay-ACK

Failed to send packet, because the transmit window was full.

发送报文失败，因为发送窗口已满

Processed SCCRQ packet, but failed to allocate resource for a new tunnel on the server.

处理SCCRQ报文时，在LNS上为新隧道分配资源失败

The packet is invalid, because it is not a ICRQ or CDN packet but the session ID in the packet header is invalid.

此报文非法，因为收到的报文不是ICRQ、CDN报文，但是该报文头中的会话ID是无效值

The packet is invalid, because it is not a SCCRQ or StopCCN packet but the tunnel ID in the packet header is invalid.

此报文非法，因为收到的报文不是SCCRQ、StopCCN，但是报文头中的隧道ID是无效值

ICRQ packet is invalid, because the session ID in the packet header is valid.

ICRQ报文非法，因为报文头中的会话ID是有效值

SCCRQ packet is invalid, because the tunnel ID in the packet header is valid.

SCCRQ报文非法，因为报文头中的隧道ID是有效值

Invalid packet header.

报文头非法

Invalid packet length.

报文长度异常

Unknown packet type.

报文类型无法识别

The tunnel with the TunnelID *tunnel-id* in the packet header doesn\'t exist.

报文头中*tunnel-id*指定的隧道不存在

The session with the SessionID *session-id* in the packet header doesn't exist.

报文头中*session-id*指定的会话不存在

The number of necessary AVPs is wrong in *message-type* packet.

在类型为*message-type*的报文中必备AVP个数错误

其中，*message-type*取值包括SCCRQ、SCCRP、SCCCN、StopCCN、ICRQ、ICRP、ICCN、CDN、SLI

TunnelID=*tunnel-id*, SessionID=*session-id*: Failed to process *packet-type* packet in *session-state* state, so deleted the local session.

在隧道ID为*tunnel-id*、会话ID为*session-id*的会话中，在状态*session-state*下处理类型为*packet-type*的报文失败，删除本地会话

·当*session-state*为Wait-Reply时，*packet-type*为ICRP

·当*session-state*为Idle时，*packet-type*为ICRQ

·当*session-state*为Wait-Connect时，*packet-type*为ICCN

TunnelID=*tunnel-id*, SessionID=*session-id*: When processing *packet-type* packet in *session-state* state, failed to allocate resource, so sent CDN packet to the peer and deleted the local session.

在隧道ID为*tunnel-id*、会话ID为*session-id*的会话中，在状态*session-state*下处理类型为*packet-type*的报文时申请资源失败，发送CDN报文给对端，并删除本地会话

·当*session-state*为Wait-Reply时，*packet-type*为ICRP

·当*session-state*为Idle时，*packet-type*为ICRQ

·当*session-state*为Wait-Connect时，*packet-type*为ICCN

TunnelID=*tunnel-id*: Failed to start the session negotiation, so sent StopCCN packet to the peer and deleted the local tunnel.

在隧道*tunnel-id*中，发起会话协商失败，发送StopCCN给对端，并删除本地隧道

TunnelID=*tunnel-id*: Failed to process *packet-type* packet in *tunnel-state* state, so deleted the local tunnel.

在隧道*tunnel-id*中，在状态*tunnel-state*下处理类型为*packet-type*的报文失败，删除本地隧道

·当*tunnel-state*为Idle时，*packet-type*为SCCRQ

·当*tunnel-state*为Wait-Connect时，*packet-type*为SCCCN

·当*tunnel-state*为Wait-Reply时，*packet-type*为SCCRP

TunnelID=*tunnel-id*: When processing *packet-type* packet in *tunnel-state* state, failed to allocate resource, so sent StopCCN packet to the peer and deleted the local tunnel.

在隧道*tunnel-id*中，在状态*tunnel-state*下处理类型为*packet-type*的报文时申请资源失败，发送StopCCN报文给对端，并删除本地隧道

·当*tunnel-state*为Wait-Connect时，*packet-type*为SCCCN

·当*tunnel-state*为Wait-Reply时，*packet-type*为SCCRP

Failed to report PPP-UP event on interface *interface-name*.

上报接口*interface-name*上的PPP-UP事件失败

Failed to report PPP-DOWN event on interface *interface-name*.

上报接口*interface-name*上的PPP-DOWN事件失败

Failed to create a session for LAC. TunnelID=*tunnel-id*, SessionID=*session-id*.

为LAC创建会话失败，隧道ID为*tunnel-id*，会话ID为*session-id*

Failed to create a session for LNS. TunnelID*=tunnel-id* , SessionID*=session-id* .

为LNS创建会话失败，隧道ID为*tunnel-id*，会话ID为*session-id*

Failed to process the IF-CREATE event for interface *interface-name*.

接口*interface-name*的创建事件处理失败

Failed to send the packet to PPP on interface *interface-name*.

在接口*interface-name*上发送报文到PPP失败

Failed to encapsulate the PPP packet on interface *interface-name*.

在接口*interface-name*上封装PPP报文失败

表1-6 debugging l2tp event命令输出信息描述表

字段

描述

TunnelID=*tunnel-id*, SessionID=*session-id*: Processed *packet-type* packet in *session-state* state, sent CDN packet to the peer and deleted the local session.

在隧道ID为*tunnel-id*、会话ID为*session-id*的会话中，在状态*session-state*下处理类型为*packet-type*的报文，给对端发送CDN报文，并删除本地会话

·当*session-state*为Wait-Reply时，*packet-type*为ICRQ

·当*session-state*为Idle时，*packet-type*为invalid ICRQ、ICRP

·当*session-state*为Wait-Connect时，*packet-type*为invalid ICCN、ICRQ、ICRP

·当*session-state*为Established时，*packet-type*为ICRQ、ICRP、ICCN

TunnelID=*tunnel-id*, SessionID=*session-id*: Proccessed invalid *packet-type* packet in *session-state* state, sent CDN packet to the peer and deleted the local session.

在隧道ID为*tunnel-id*、会话ID为*session-id*的会话中，在状态*session-state*下处理类型为*packet-type*的非法报文，给对端发送CDN报文，并删除本地会话

·当*session-state*为Wait-Reply时，*packet-type*为ICRP

·当*session-state*为Idle时，*packet-type*为ICRQ

·当*session-state*为Wait-Connect时，*packet-type*为ICCN

TunnelID=*tunnel-id*, SessionID=*session-id*: Processed *packet-type* packet in *session-state1* state, and changed the session state to *session-state2*.

在隧道ID为*tunnel-id*、会话ID为*session-id*的会话中，在状态*session-state1*下处理类型为*packet-type*的报文，会话状态变为*session-state2*

·当*session-state1*为Wait-Reply，*session-state2*为Established时，*packet-type*为ICRP

·当*session-state1*为Idle，*session-state2*为Wait-Connect时，*packet-type*为ICRQ

·当*session-state1*为Wait-Connect，*session-state2*为Established时，*packet-type*为ICCN

TunnelID=*tunnel-id*, SessionID=*session-id*: Processed *packet-type* packet in *session-state* state, and deleted the local session.

在隧道ID为*tunnel-id*、会话ID为*session-id*的会话中，在状态*session-state*下处理类型为*packet-type*的报文，删除本地会话

其中，*session-state*的取值包括Wait-Reply、Idle和Wait-Connect；*packet-type*取值为ICCN

TunnelID=*tunnel-id*: Processed StopCCN packet in Stopping state, and sent ZLB-ACK packet to the peer. Ns=*ns*, Nr=*nr*.

在隧道*tunnel-id*中，在Stopping状态下处理StopCCN报文，发送ZLB-ACK报文给对端，报文中Ns为*ns*、Nr为*nr*

TunnelID=*tunnel-id*: Processed *packet-type* packet in *tunnel-state1* state, and changed the tunnel state to *tunnel-state2*.

在隧道*tunnel-id*中，在状态*tunnel-state1*下处理类型为*packet-type*的报文，隧道状态变为*tunnel-state2*

·当*tunnel-state1*为Wait-Reply，*tunnel-state2*为Established时，*packet-type*为SCCRP

·当*tunnel-state1*为Idle，*tunnel-state2*为Wait-Connect时，*packet-type*为SCCRQ

·当*tunnel-state1*为Wait-Connect，*tunnel-state2*为Established时，*packet-type*为SCCCN

·当*tunnel-state1*为Established、Wait-Connect或Wait-Reply，*tunnel-state2*为Stopping时，*packet-type*为StopCCN

TunnelID=*tunnel-id*: Processed *packet-type* packet in *tunnel-state* state, sent StopCCN packet to the peer and deleted the local tunnel.

在隧道*tunnel-id*中，在状态*tunnel-state*下处理类型为*packet-type*的报文，给对端发送StopCCN报文，并删除本地隧道

·当*tunnel-state*为Wait-Connect时，*packet-type*为SCCRQ、SCCRP

·当*tunnel-state*为Wait-Reply时，*packet-type*为invalid SCCRP、SCCCN

·当*tunnel-state*为Established时，*packet-type*为SCCRQ、SCCRP、SCCCN

·当*tunnel-state*为Idle时，*packet-type*为invalid SCCRQ、SCCRP

TunnelID=*tunnel-id*: Processed *packet-type* packet in *tunnel-state* state, and deleted the local tunnel.

在隧道*tunnel-id*中，在状态*tunnel-state*下处理类型为*packet-type*的报文，删除本地隧道

·当*tunnel-state*为Wait-Connect时，*packet-type*为SCCCN

·当*tunnel-state*为Idle时，*packet-type*为SCCCN、StopCCN

·当*tunnel-state*为Stopping时，*packet-type*为ZLB-ACK

TunnelID=*tunnel-id*: Processed invalid *packet-type* packet in *tunnel-state* state, sent StopCCN packet to the peer and deleted the local tunnel.

在隧道*tunnel-id*中，在状态*tunnel-state*下处理类型为*packet-type*的非法报文，给对端发送StopCCN报文，并删除本地隧道

·当*tunnel-state*为Wait-Reply时，*packet-type*为SCCRP

·当*tunnel-state*为Idle时，*packet-type*为SCCRQ

·当*tunnel-state*为Wait-Connect时，*packet-type*为SCCCN

L2TP service was not enabled, so L2TP packet *packet-type* can't be parsed.

L2TP服务未使能，无法解析L2TP控制报文

其中，*packet-type*取值包括ICRQ、SCCRQ、StoppCCN

TunnelID=*tunnel-id*: Adjusting the sequence number of control packets dynamically.

隧道*tunnel-id*正在动态调整控制报文的序列号

TunnelID=*tunnel-id*: Received duplicate Hello packet for *times* times.

隧道*tunnel-id*收到重复的Hello报文*times*次

TunnelID=*tunnel-id*: Received a duplicate packet, so sent ZLB-ACK packet to notify the peer to adjust transmit window. Ns=*ns*, Nr=*nr*.

隧道*tunnel-id*收到重复的报文，发送ZLB ACK报文通知对端调整发送窗口，报文中的Ns为*ns*、Nr为*nr*

Parsed *AVP-type* AVP: *avp-value*.

解析类型为*AVP-type*的AVP，AVP值为*avp-value*

Parsed Protocol-Version AVP. Version=*version*, Revision=*revision*.

解析Protocol-Version AVP，版本号为*version*，Revision为*revision*

Parsed Sequencing-Required AVP.

解析Sequencing-Required AVP

Parsed Q.931-Cause-Code AVP. Cause-code=*cause-code*, Cause-Message=*cause-message*, Advisory-Message=*advisory-message*.

解析Q.931-Cause-Code AVP

·{.TableTextChar}原因码为*cause-code*

·{.TableTextChar}原因信息为*cause-message*

·警告信息为*advisory-message*

Parsed ACCM AVP. Send-ACCM=*Send-ACCM*, Receive-ACCM=*recv-ACCM*.

解析ACCM AVP。发送ACCM为*send-ACCM*，接收ACCM为*recv-ACCM*

Parsed Result-Code AVP. Result-Code=*recode-code*, Error-Code=*error-code*, Error-Message=*error-message*.

解析Result code AVP

·{.TableTextChar}结果码为*result-code*

·错误码为*error-code*

·错误信息为*error-message*

Parsed unknown mandatory AVP in *message-type* packet.

在*message-type*报文中解析到不可识别的强制AVP

其中，*message-type*取值包括SCCRQ、SCCRP、SCCCN、StopCCN、ICRQ、ICRP、ICCN、CDN、SLI

TunnelID=*tunnel-id*: Delay-ACK timer expired, received duplicate Hello packet for *times* times and sent ZLB-ACK packet for *times* times. Ns=*ns*, Nr=*nr*.

隧道*tunnel-id*的Delay-ACK定时器超时，已经收到重复的Hello报文*times*次，发送ZLB-ACK报文*times*次。 报文中的Ns为*ns*、Nr为*nr*

TunnelID=*tunnel-id*: Resent the packet for *times* times.

隧道*tunnel-id*已经重发报文*times*次

TunnelID=*tunnel-id*: Delay-Cleanup timer expired and deleted the local tunnel.

隧道*tunnel-id*的Delay-Cleanup定时器超时，删除本地隧道

Received invalid packet from port 1701, and dropped it.

从1701端口收到不合法的报文，丢弃该报文

Created a new session during batch synchronization. TunnelID=*tunnel-id*, SessionID=*session-id*.

批量平滑过程中创建一个新的会话，会话所属的隧道ID为*tunnel-id*，会话ID为*session-id*

An old session found during batch synchronization. TunnelID*=tunnel-id*, SessionID*=session-id*.

批量平滑过程中发现一个旧的会话，会话所属的隧道ID为*tunnel-id*，会话ID为*session-id*

Interface *interface-name* deleted.

删除接口*interface-name*

Interface *interface-name* created.

创建接口*interface-name*

TunnelID=*tunnel-id*: Sent a Hello packet. Ns=*ns*, Nr=*nr*.

隧道*tunnel-id*成功发送Hello报文，报文中的Ns为*ns*、Nr为*nr*

【举例】

\# 在LNS侧设备上打开L2TP控制报文调试信息开关。使用PC拨号上线时，LNS侧设备上会打印如下调试信息。

\<Sysname\> debugging l2tp control-packet

\*Aug 28 00:39:40:302 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Received SCCRQ packet from port 1701 (length=114, Ns=0, Nr=0). Packet content:

 c8 02 00 72  00 00 00 00  00 00 00 00  80 08 00 00

 00 00 00 01  80 08 00 00  00 02 01 00  80 09 00 00

 00 07 6c 61  63 00 13 00  00 00 08 48  33 43 20 53

 69 6d 77 61  72 65 33 32  80 0a 00 00  00 03 00 00

 00 03 80 08  00 00 00 09  7a 31 80 0a  00 00 00 04

 00 00 00 03  80 08 00 00  00 0a 04 00  80 16 00 00

 00 0b fc dc  b2 27 82 dd  ba 9f 9b f3  0d bb 12 0c

 57 ff

*// 接收到SCCRQ报文，长度是114字节，Ns为0，Nr为0。*

\*Aug 28 00:39:40:305 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Message-Type AVP:

 80 08 00 00  00 00 00 02

\*Aug 28 00:39:40:305 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Protocol-Version AVP:

 80 08 00 00  00 02 01 00

\*Aug 28 00:39:40:305 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Host-Name AVP:

 80 09 00 00  00 07 6c 6e  73

\*Aug 28 00:39:40:306 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Vendor-Name AVP:

 00 13 00 00  00 08 48 33  43 20 53 69  6d 77 61 72

 65 33 32

\*Aug 28 00:39:40:306 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Framing-Capabilities AVP:

 80 0a 00 00  00 03 00 00  00 03

\*Aug 28 00:39:40:306 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Assigned-Tunnel-ID AVP:

 80 08 00 00  00 09 32 ce

\*Aug 28 00:39:40:307 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Bearer-Capabilities AVP:

 80 0a 00 00  00 04 00 00  00 03

\*Aug 28 00:39:40:307 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Receive-Window-Size AVP:

 80 08 00 00  00 0a 04 00

\*Aug 28 00:39:40:307 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Challenge AVP:

 80 16 00 00  00 0b 3a df  ba 35 68 60  5a 00 91 a1

 79 61 24 23  4d 73

\*Aug 28 00:39:40:307 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Challenge-Response AVP:

 80 16 00 00  00 0d b4 30  82 a4 9b 10  60 46 8c 99

 7d 92 4c 1a  b0 71

*// 封装SCCRP报文。*

\*Aug 28 00:39:40:312 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Received SCCCN packet from port 1701 (TunnelID=13006, length=42, Ns=1, Nr=1). Packet content:

 c8 02 00 2a  32 ce 00 00  00 01 00 01  80 08 00 00

 00 00 00 03  80 16 00 00  00 0d 73 e1  b8 1a 43 ff

 50 47 55 9d  9c b6 93 f6  7d 67

*// 接收到SCCCN报文，隧道ID为13006，长度是42字节，Ns为1，Nr为1。*

\*Aug 28 00:39:40:313 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Received ICRQ packet from port 1701 (TunnelID=13006, length=38, Ns=2, Nr=1). Packet content:

 c8 02 00 26  32 ce 00 00  00 02 00 01  80 08 00 00

 00 00 00 0a  80 08 00 00  00 0e 11 31  80 0a 00 00

 00 0f 00 00  11 31

*// 接收到ICRQ报文，隧道ID为13006，长度是38字节，Ns为2，Nr为1。*

\*Aug 28 00:39:40:317 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Message-Type AVP:

 80 08 00 00  00 00 00 0b

\*Aug 28 00:39:40:317 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Encapsulated Assigned-Session-ID AVP:

 80 08 00 00  00 0e c4 b0    

*// 封装ICRP报文。*

\*Aug 28 00:39:40:318 2012 Sysname L2TPV2/7/CONTROL-PKT: -MDC=1;

 Received ICCN packet from port 1701 (TunnelID=13006, length=40, Ns=3, Nr=2). Packet content:

 c8 02 00 28  32 ce c4 b0  00 03 00 02  80 08 00 00

 00 00 00 0c  80 0a 00 00  00 18 00 00  00 00 80 0a

 00 00 00 13  00 00 00 00

*// 收到ICCN报文，隧道ID为13006，长度是40字节，Ns为3，Nr为2。*

\# 在LNS侧设备上打开L2TP事件调试信息开关，PC拨号上线时，LNS侧设备上会打印如下调试信息。

\<Sysname\> debugging l2tp event

\*Aug 28 00:39:40:303 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Message-Type AVP: 1.

\*Aug 28 00:39:40:303 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Protocol-Version AVP, Version=1, Revision=0.

\*Aug 28 00:39:40:303 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Host-Name AVP: lac.

\*Aug 28 00:39:40:304 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Vendor-Name AVP: TEST.

\*Aug 28 00:39:40:304 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Framing-Capabilities AVP: 3.

\*Aug 28 00:39:40:304 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Assigned-Tunnel-ID AVP: 31281.

\*Aug 28 00:39:40:304 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Bearer-Capabilities AVP: 3.

\*Aug 28 00:39:40:305 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Receive-Window-Size AVP: 1024.

\*Aug 28 00:39:40:305 2012 Sysname L2TPV2/7/EVENT: -MDC=1;

 Parsed Challenge AVP: fc dc b2 27 82 dd ba 9f 9b f3 0d bb 12 0c 57 ff

*// 解析SCCRQ报文中携带的AVP，并输出对应的值。*

\# PC拨号上线成功后，在LNS侧设备上打开L2TP数据报文调试信息开关，会打印如下调试信息。

\<Sysname\> debugging l2tp data-packet

\*Aug 28 00:39:40:319 2012 Sysname L2TPV2/7/KDATA-PKT: -MDC=1;

 Received an L2TP data packet:

  Source IP: 192.168.4.7

  Destination IP: 192.168.4.8

  Source port: 1701

  Destination port: 1701

*// 收到一个L2TP数据报文，报文的源IP地址是192.168.4.7，目的IP地址是192.168.4.8，源端口号和目的端口号均是1701。*

\*Aug 28 00:39:40:319 2012 Sysname L2TPV2/7/KDATA-PKT: -MDC=1;

 Successfully parsed the L2TP header (L2TP header length=8):

  Tunnel ID: 13006

  Session ID: 50352

  Ns: 61811

  Type: 0

  Length: 0

  Sequence: 0

  Offset: 1

  Priority: 0

*// 成功解析了L2TP数据报文，L2TP报文头长度是8字节，报文中的隧道ID为13006，会话ID为50352，报文序列号为61811，类型值为0，长度、序列号和优先级未置位，偏移量置位。*

\# PC拨号上线成功后，在LNS侧设备上打开L2TP的PPP报文调试信息开关，会打印如下调试信息。

\<Sysname\> debugging l2tp dump

\*Aug 28 00:39:40:335 2012 Sysname L2TPV2/7/KDUMP: -MDC=1;

 Send a packet to PPP on interface Virtual-Access0 (length=19):

 ff 03 c0 21 02 00 00 0f 03 05 c2 23 05 05 06 34

 73 72 b6

*// 在接口Virtual-Access0下，将长度为19字节的报文发送给了PPP。*
