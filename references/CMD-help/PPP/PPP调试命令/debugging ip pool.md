
**PPP \-- PPP调试命令 \-- debugging ip pool**

------------------------------------------------------------------------

【命令】

**[debugging ip pool**[ { **all** \| **error** \| **event** }]]

**[undo debugging ip pool**[ { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【使用指导】

**[debugging ip pool**]命令用来打开PPP地址池模块的调试信息开关。**undo debugging ip pool**命令用来关闭PPP地址池模块的调试信息开关。

缺省情况下，PPP地址池模块的所有调试信息开关均处于关闭状态。

表1-1 debugging ip pool error命令输出信息描述表

字段

描述

No IP address available in the IP pool *pool-name*

分配IP地址失败，地址池IP地址已耗尽

Failed to assgin IP address from the IP pool *pool-name*

从地址池申请IP地址失败

Invalid IP address assignment request

非法的IP地址分配请求

Invalid IP address release request

非法的IP地址释放请求

Failed to create an expired timer

创建回收静默地址定时器失败

IP pool *pool-name* dose not existed, failed to assign IP address

地址池不存在，分配地址失败

表1-2 debugging ip pool event命令输出信息描述表

字段

描述

Received an IP address assignment request

主控板收到地址分配请求消息

Created an expired timer

创建静默地址定时器

Destroyed an expired timer

删除静默地址定时器

Assigned an IP address *ip-address* from free-list

从空闲地址列表中分配一个地址

Assigned an IP address *ip-address* from expired-list

从静默地址列表中分配一个地址

IP address *ip-address* successfully assigned

分配地址成功

Received an IP address release request

主控板收到地址回收请求消息

Released the IP address *ip-address* to the free-list

回收地址到空闲地址列表中

Released the IP address *ip-address* to the expired-list

回收地址到静默地址列表中

IP address *ip-address* successfully released

回收地址成功

Received a smooth-start message

主控板收到接口板的地址池数据平滑开始消息

Received a smooth-end message

主控板收到接口板的地址池数据平滑结束消息

【举例】

\# 两台集中式设备用Serial接口连接，链路封装PPP协议，本端配置通过地址池为对端分配地址和本端IP地址，对端配置IP地址可协商属性，打开PPP地址池的事件调试信息开关。

\<Sysname\> debugging ip pool event

\*Nov 21 15:58:48:129 2012 Sysname PPP/7/IPPOOL_EVENT: -MDC=1;

  Assigned an IP address 1.1.1.2 from free-list.

*// 从空闲地址列表中分配一个地址*

\*Nov 21 15:58:48:130 2012 Sysname PPP/7/IPPOOL_EVENT: -MDC=1;

  IP address 1.1.1.2 successfully assigned.

*// 地址池分配地址成功*

**PPP \-- PPP调试命令 \-- debugging ppp**

------------------------------------------------------------------------

【命令】

**[debugging ppp **[{ **all** \| { **chap** \| **ipcp** \| **ipv6cp** \| **lcp** \| **mp** \| **mplscp** \| **osicp** \| **pap** } { **all** \| **error** \| **event** \| **packet** \| **state** } \| { **ip** \| **ipv6** \| **lqm** \| **mpls** \| **osi** } **packet** \| **external event** } [ **interface** *interface-type interface-number* ]]]

**[undo debugging ppp **[{ **all** \| { **chap** \| **ipcp** \| **ipv6cp** \| **lcp** \| **mp** \| **mplscp** \| **osicp** \| **pap** } { **all** \| **error** \| **event** \| **packet** \| **state** } \| { **ip** \| **ipv6** \| **lqm** \| **mpls** \| **osi** } **packet \| external event** } [ **interface** *interface-type interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：PPP的所有调试信息开关。

**[chap**]：质询握手认证协议调试信息开关。

**[ipcp**]：IP控制协议调试信息开关。

**[ipv6cp**]：IPv6控制协议调试信息开关。

**[lcp**]：链路控制协议调试信息开关。

**[mp**]：多条PPP链路捆绑协议调试信息开关。

**[mplscp**]：MPLS控制协议调试信息开关。

**[osicp**]：OSI控制协议调试信息开关。

**[pap**]：密码认证协议调试信息开关。

**[error**]：PPP的错误调试信息开关。

**[event**]：PPP的事件调试信息开关。

**[packet**]：PPP的报文调试信息开关。

**[state**]：PPP的状态调试信息开关。

**[ip**]：IP调试信息开关。

**[ipv6**]：IPv6调试信息开关。

**[lqm**]：PPP链路质量监测协议调试信息开关。

**[mpls**]：MPLS调试信息开关。

**[osi**]：OSI调试信息开关。

**[external event**]：PPP外部事件调试信息开关。

**[interface **]*interface-type interface-number*：指定的接口类型和编号。

【使用指导】

**[debugging ppp**]命令用来打开PPP的调试信息开关。**undo debugging ppp**命令用来关闭PPP的调试信息开关。

缺省情况下，PPP的所有调试信息开关均处于关闭状态。

表1-3 debugging ppp *protocol-type* error命令输出信息描述表

字段

描述

PPP Error

PPP错误信息

*[interface-name*]

接口名称

*[protocol-type*]

协议类型，取值为：LCP、IPCP、OSICP、IPv6CP、MP

*[error-string*]

错误信息内容，取值及含义：

·FSM Illegal Event：状态机非法事件

·Received bad Confack Packet：接收错误的配置确认报文

·Packet Id Error：报文ID错误

·Failed to send packet：发送报文失败

·Received illegal event：接收错误的事件

·Serial line is looped back：链路回环

·Received wrong IPCP ACK：接收错误的IPCP配置确认报文

表1-4 debugging ppp *protocol-type* event命令输出信息描述表

字段

描述

PPP Event

PPP事件

*[interface-name*]

接口名称

*[protocol-type*]

协议类型，取值为：LCP、IPCP、MPLSCP、OSICP、IPv6CP、MP

*[event*]

状态机事件*event*的取值及含义：

·Lower Up：底层up事件

·Lower Down：底层down事件

·Open：链路可供使用

·Close：链路不提供使用

·TO+(Timeout with counter \> 0)：超时重发事件（重传计数器大于0重发报文）

·TO-(Timeout with counter expired)：超时重发事件（重传计数器不大于0，不重发报文）

·RCR+(Receive Good Configure Request)：从对端收到Configure-Request报文时，触发此事件（RCR+事件指对端的配置请求可以接受，该事件发生时，发送Configure-Ack报文作为响应）

·RCR-(Receive Bad Configure Request)：从对端收到Configure-Request报文时，触发此事件（RCR-事件指不接受对端的配置请求，该事件发生时，根据情况发送Configure-Nak或Configure-Rej报文作为响应）

·RCA(Receive Configure Ack)：收到对端对本端请求选项认可的Configure-Ack报文时事件发生

·RCN(Receive Configure Nak/Reject)：收到对端拒绝本端某些或全部请求选项的Configure-Nak/Rej报文时事件发生

·RTR(Receive Terminate Request)：收到对端Terminate-Request报文，表明对端想关闭连接

·RTA(Receive Terminate Ack)：接收到对端Terminate-Ack报文

·RUC(Receive Unknown Code)：收到对端发送过来的本端无法解释的报文时触发此事件

·RXJ+(Receive permitted Code/Protocol Reject )：收到对端发送过来的Code-Reject或Protocol-Reject时此事件发生。RXJ+：表明被拒绝的选项可接受，即在正常范围内

·RXJ-(Receive catastrophic Code/Protocol Reject )：收到对端发送过来的Code-Reject或Protocol-Reject时此事件发生。RXJ-：表明被拒绝的选项对端不可接受，这将导致链接终止

·RXR(Receive EchoRequest/EchoReply/DiscardRequest)：当从对端接收到Echo-Request、Echo-Reply、Discard-Request报文时，事件发生。对Echo-Request报文回应Echo-Reply报文

*[state *]

PPP状态机状态，*state*取值见表 1-4(#aaa)

表1-5 debugging ppp external event命令输出信息描述表

字段

描述

PPP External Event

PPP外部事件

*[interface-name*]

接口名称

*[event*]

外部事件*event*的取值及含义举例：

·PPP negotiate down, start Reset-Timer：PPP协商失败，启动Reset定时器

·Reset-Timer Expired, IPCP negotiate again：Reset定时器超时，IPCP重协商

·PPP create rundb error：PPP创建运行DBM错误

·PPP updaterundb error：更新运行DBM错误

·Reset-Timer Expired, reset LCP and negotiate again：Reset定时器超时，重启协商

·Failed to free the User ID *user*-*id*.：释放User ID失败

·Successfully freed the User ID *user*-*id*.：释放User ID成功

·Failed to send free User ID asynchronism message.：发送释放User ID异步消息失败

·Failed to notify User QoS of user logon.：通知User QoS模块用户上线失败

·Successfully notifiedUser QoSof user logon.：通知User QoS模块用户上线成功

·Invalid User ID. User will be logged off.：无效的User ID。用户将下线

·Failed to notify User QoS of user logoff.：通知User QoS模块用户下线失败

·Successfully notifiedUser QoSof user logoff.：通知User QoS模块用户下线成功

·There is no user profile configurationso the user will be logged off.：没有用户配置，强制用户下线

·Notified User QoS of authorization change.：通知User QoS模块用户授权信息改变

·Successfullydistributed the User ID* user*-*id*.：分配User ID成功

·Failed to distribute user ID because user IDs have been used up.：User ID耗尽分配失败

·Failed to smooth UserQoS data.：平滑User QoS模块数据失败

·Failed to notify IPv4 multicast of userlogon.：通知IPv4组播用户上线失败

·Successfully notifiedIPv4 multicast of userlogon.：通知IPv4组播用户上线成功

·Failed to notify IPv6 multicast of userlogon.：通知IPv6组播用户上线失败

·Successfully notifiedIPv6 multicast of userlogon..：通知IPv6组播用户上线成功

·Failed to notify IPv4 multicast of userlogoff.：通知IPv4组播用户下线失败

·Successfully notifiedIPv4 multicast of userlogoff.：通知IPv4组播用户下线成功

·Failed to notify IPv6 multicast of userlogoff.：通知IPv6组播用户下线失败

·Successfully notifiedIPv6 multicast of userlogoff.：通知IPv6组播用户下线成功

·Failed to notify IPv4 multicast of authorization change.：通知IPv4组播用户授权变更失败

·Successfully notifiedIPv4 multicast of authorization change.：通知IPv4组播用户授权变更成功

·Failed to notify IPv6 multicast of authorization change.：通知IPv6组播用户授权变更失败

·Successfully notifiedIPv6 multicast of authorization change.：通知IPv6组播用户授权变更成功

·Failed to smooth IPv4 multicast data.：平滑IPv4组播数据失败

·Failed to smooth IPv6 multicast data.：平滑IPv6组播数据失败

·The user NAT seq is not equal to the local seq.：用户的NAT序号与本地的序号不一致

**

·Successfully notified NAT of user logon.：通知NAT模块用户上线成功

·Successfully notified NAT of user logoff.：通知NAT模块用户下线成功

·Failed to notify NAT of user logon.：通知NAT模块用户上线失败

·Failed to notify NAT of user logoff.：通知NAT模块用户下线失败

·Received an event to allocate a public IP address and port blocks.：收到分配公网IP及端口块事件

·Received an event to free a public IP address and port blocks.：收到释放公网IP及端口块事件

·Failed to smooth NAT data.：平滑NAT数据失败

表1-6 debugging ppp *protocol-type* state命令输出信息描述表

字段

描述

PPP State Change

链路层协议状态变化

*[interface-name*]

接口名称

*[protocol-type*]

协议类型，取值为：LCP、IPCP、MPLSCP、OSICP、IPv6CP、MP

*[state *\--\> *state*]

*[state*]取值及含义：

·initial：初始状态

·starting：启动状态

·closed：关闭状态

·stopped：停止状态

·closing：正在关闭状态

·stopping：正在停止状态

·reqsent：配置请求发送状态

·ackrcvd：收到对端确认状态

·acksent：对对端的确认报文已发送状态

·opened：链路开启状态

表1-7 debugging ppp *protocol-type* packet命令输出信息描述表

字段

描述

PPP Packet

链路层协议

*[interface-name*]

接口名称

Output/Input

发送/接收报文

*[protocol-type *Packet]

协议类型，取值为：LCP、IPCP、MPLSCP、OSICP、IPv6CP、MP、LQM

PktLen *number*

报文长度

Current State *state*

PPP状态机当前状态，*state*取值见表 1-4(#aaa)

Code *packet-type*

报文类型，*packet-type*取值及含义：

·ConfReq：配置请求

·ConfAck：配置确认

·ConfNak：配置否认

·ConfRej：配置拒绝

·TermReq：终止请求

·TermAck：终止确认

·CodeRej：代码拒绝

·ProtoRej：协议拒绝

·EchoRequest：回音请求

·EchoReply：回音应答

id *number*

报文ID

len *number*

排除PPP报文头后报文长度

MagicNumber *magic-number*

魔术字

LastOutLQRs *lqr-numer*

本端已发送的LQR报文总数

LastOutPackets *packets-number*

本端已发送的报文总数

LastOutOctets *octets-number*

本端已发送的字节总数

PeerInLQRs *lqr-number*

对端已收到的LQR报文总数

PeerInPackets *packet-number*

对端已收到的报文总数

PeerInDiscards *discard-number*

对端已丢弃的报文总数

PeerInErrors *error-number*

对端已收到的错误报文总数

PeerInOctets *octets-number*

对端已收到的字节总数

PeerOutLQRs *lqr-number*

对端已发送的LQR报文总数

PeerOutPackets *packets-number*

对端已发送的报文总数

PeerOutOctets *octets-number*

对端已发送的字节总数

*[Negotiation type*]

LCP协商选项见表 1-6(#jghgh)，IPCP协商选项见表 1-7(#sdd)

表1-8 debugging ppp lcp packet常用协商type值信息描述表

字段值

描述（英文）

描述（中文）

1

Maximum-Receive-Unit

最大接收单元

2

Async-Control-Character-Map

异步控制字符映射

3

Authentication-Protocol

验证协议

4

Quality-Protocol

质量协议

5

Magic-Number

魔术字

7

Protocol-Field-Compression

协议域压缩

8

Address-and-Control-Field-Compression

地址控制域压缩

13

Callback

PPP回呼

17

Multilink Maximum Received Reconstructed Unit

MP最大接收重组单元

18

Short Sequence Number Header Format

MP报文协商序号长度

19

Endpoint Discriminator

终端描述符

表1-9 debugging ppp ipcp packet常用协商type值信息描述表

字段值

描述（英文）

描述（中文）

2

IP CompressProt

PPP压缩类型及压缩参数协商

3

IP Address

IP地址协商

129

Primary DNS Server Address

PPP一端向另一端请求Primary DNS server地址或向另一端分配Primary DNS server地址

131

Secondary DNS Server Address

PPP一端向另一端请求Secondary DNS server地址或向另一端分配Secondary DNS server地址

【举例】

\# 两台设备用Serial接口连接，链路封装PPP协议，配置后链路开始协商。打开LCP的调试信息开关。

\<Sysname\> debugging ppp lcp all

\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_EVENT_0: -MDC=1;

  PPP Event:

      Serial2/1/0 LCP Open Event

      State initial

*[// Serial2/1/0*]*接口的LCP状态机为open，状态为initial*

\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_STATE_0: -MDC=1;

  PPP State Change:

      Serial2/1/0 LCP : initial \--\> starting

*[// Serial2/1/0*]*接口的LCP状态从initial状态切换到starting状态*

\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_EVENT_0: -MDC=1;

  PPP Event:

      Serial2/1/0 LCP Lower Up  Event

      State starting

*[// Serial2/1/0*]*接口的LCP底层UP事件，LCP状态机状态为starting状态*

\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_STATE_0: -MDC=1;

  PPP State Change:

      Serial2/1/0 LCP : starting \--\> reqsent

*[// Serial2/1/0*]*接口的LCP状态从starting状态切换到reqsent状态*

\*Dec 21 14:36:25:998 2013 Sysname PPP/7/FSM_PACKET_0: -MDC=1;

  PPP Packet:

      Serial2/1/0 Output LCP(c021) Packet, PktLen 22

      Current State reqsent, code ConfReq(01), id 2a, len 18

      MRU(1), len 4, val 05 dc

      AuthProto(3), len 4, PAP c0 23

      MagicNumber(5), len 6, val 31 18 0c 00

*[// Serial2/1/0*]*接口发送长度35的LCP报文。LCP状态机状态为reqsent状态，报文类型为ConfReq报文，报文ID为2a，取掉报文头的报文长度为22。协商最大接收单元，字段长度4，协商长度05dc。协商验证协议，字段长度4，PAP认证。魔术字，字段长度6，魔术字值31180c00*

**

\# 两台设备用Serial接口连接，链路封装PPP协议，分别在两端接口下配置PPP LQM功能。打开PPP LQM的调试信息开关。待PPP链路成功建立后，两端开始交互报文。

\<Syaname\> debugging ppp lqm packet

\<Syaname\>

\*Oct 25 11:46:45:559 2013 Syaname PPP/7/LQM_PACKET_1: -MDC=1;

  PPP Packet:

      Serial2/1/3 Output LQM(c025) Packet, PktLen 52

      Current State opened, len 48, MagicNumber 0xc60dde76

      LastOutLQRs 1, LastOutPackets 110, LastOutOctets 163

      PeerInLQRs 1, PeerInPackets 103, PeerInDiscards 105

      PeerInErrors106, PeerInOctets 102

      PeerOutLQRs 2, PeerOutPackets 110, PeerOutOctets 163

*[// Serial2/1/3*]*接口发送长度为52的LQM报文。LCP当前状态机状态为opened状态，去掉PPP头的报文长度为48，魔术字值为0xc60dde76，本端已发送的LQR报文总数为1，已发送的报文总数为110，已发送的字节总数为163，对端已收到的LQR报文总数为1，已收到的报文总数为103，已丢弃的报文总数为105，已收到的错误报文总数为106，已收到的字节总数为102，已发送的LQR报文总数为2，已发送的报文总数为110，已发送的字节总数为163*

\*Oct 25 11:46:45:561 2013 Syaname PPP/7/LQM_PACKET_1: -MDC=1;

  PPP Packet:

      Serial2/1/3 Input LQM(c025) Packet, PktLen 52

      Current State opened, len 48, MagicNumber 0xef4f8337

      LastOutLQRs 2, LastOutPackets 110, LastOutOctets 163

      PeerInLQRs 2, PeerInPackets 103, PeerInDiscards 105

      PeerInErrors 106, PeerInOctets 102

      PeerOutLQRs 2, PeerOutPackets 110, PeerOutOctets 163

*[// Serial2/1/3*]*接口收到长度为52的LQM报文。LCP当前状态机状态为opened状态，去掉PPP头的报文长度为48，魔术字值为0xef4f8337，本端已发送的LQR报文总数为2，已发送的报文总数为110，已发送的字节总数为163，对端已收到的LQR报文总数为2，已收到的报文总数为103，已丢弃的报文总数为105，已收到的错误报文总数为106，已收到的字节总数为102，已发送的LQR报文总数为2，已发送的报文总数为110，已发送的字节总数为163*

**PPP \-- PPP调试命令 \-- debugging ppp compression iphc**

------------------------------------------------------------------------

【命令】

**[debugging ppp compression iphc **[{ **rtp** \| **tcp** }]]

**[undo debugging ppp compression iphc**[ { **rtp** \| **tcp** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rtp**]：表示RTP头压缩调试信息开关。

**[tcp**]：表示TCP头压缩调试信息开关。

【使用指导】

**[debugging ppp compression iphc**]命令用来打开IPHC压缩调试信息开关。

**[undo debugging ppp compression iphc**]命令用来关闭IPHC压缩调试信息开关。

缺省情况下，PPP IPHC的所有调试信息开关均处于关闭状态。

表1-10 debugging ppp compression iphc命令输出信息描述表

字段

描述

RHC

RTP头压缩信息

THC

TCP头压缩信息

FULL_HEADER

未压缩的TCP或者RTP报文，解压端根据这个报文为解压后续的压缩报文创建或更新解压表项

CONTEXT_STATE

一种由解压端发送给压缩端的特殊报文，用来传输已经或者可能已经失去同步的压缩和解压表项的ID号来通知压缩端发送一个FULL_HEADER报文来同步压缩和解压缩表项

COMPRESSED_NON_TCP

压缩的RTP报文。接口下配置**ppp compression iphc enable** **nonstandard**命令后，成功压缩时，压缩端会将RTP报文压缩成该格式的报文

COMPRESSED_TCP

压缩的TCP报文。成功压缩时，压缩端会将TCP报文压缩成该格式的报文

COMPRESSED_RTP_8

压缩的RTP报文。当接口上允许进行RTP头压缩的最大连接数小于等于256时，成功压缩时，压缩端会将RTP报文压缩成该种格式的报文

COMPRESSED_RTP_16

压缩的RTP报文。当接口上允许进行RTP头压缩的最大连接数大于256时，成功压缩时，压缩端会将RTP报文压缩成该种格式的报文

ERROR

IPHC压缩/解压缩过程的错误信息

WARNING

IPHC压缩/解压缩过程的提示信息

received

接收报文

sent

发送报文

connect ID

报文流标识，表示压缩/解压缩的某条流。压缩端和解压端根据这个ID号来查找压缩和解压缩表项

checksum

校验和

seq

Sequence Number，报文的序列号

gen

Generation Number字段用来检测COMPRESSED_NON_TCP报文压缩和解压缩的一致性

Sent uncompressed packets

发送了没有压缩的报文。压缩过程中，当检测到压缩表项为空，不能对报文进行压缩，为保证报文传输，会发送没有经过压缩的报文，并打印该条信息

The compression context of TCP is invalid

压缩TCP报文过程中检测到压缩表项无效。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

IP header mismatched

压缩TCP报文过程中检测到IP头与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

TCP header mismatched

压缩TCP报文过程中检测到TCP头与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_URG code error

压缩TCP报文过程中检测到Delta URG字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

th_URG mismatched

压缩TCP报文过程中检测到URG字段与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_win code error

压缩TCP报文过程中检测到Delta Window字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_ACK code error

压缩TCP报文过程中检测到Delta Acknowledgment Number字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_seq code error

压缩TCP报文过程中检测到Delta Sequence字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The flag bits of th_URG, th_seq, and th_win are set

压缩TCP报文过程中检测到URG字段、Sequence Number字段和Window字段的标识位被置为1时，压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta IP ID code error

压缩TCP报文过程中检测到Delta IP ID编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The compression context of NON_TCP is invalid

将RTP报文压缩成COMPRESSED_NON_TCP报文过程中检测到COMPRESSED_NON_TCP的压缩表项无效。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

UDP checksum mismatched

压缩RTP报文过程中检测到UDP头的Checksum字段与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The number of compressed NON_TCP packets is out of range

将RTP报文压缩成COMPRESSED_NON_TCP过程中检测到在两个FULL_HEADER报文之间，发送的COMPRESSED_NON_TCP报文的数量超出了规定的范围

The time for compressing NON_TCP packet is lawless

将RTP报文压缩成COMPRESSED_NON_TCP报文的过程中检测到压缩的报文的时间段非法。这时压缩端会发送一个FULL_HEADER报文来同步压缩端和解压端（在每发送一个FULL_HEADER报文后的一段时间内压缩的COMPRESSED_NON_TCP压缩报文是合法的，不在这个时间段内对报文进行压缩是非法的）

The delta values of timestamp,sequence number, or IP ID are lawless

压缩RTP报文的过程中检测到时间戳的delta值、报文序列号的delta值或者IP ID的delta值非法。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The compression context of RTP is invalid

压缩RTP报文的过程中检测到RTP的压缩表项无效。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The delta value of the IP ID is lawless

压缩RTP报文的过程中检测到IP头Delta ID值非法。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Connect ID xx out of range

解压过程中检测到报文流标识号xx超出合法范围

the decompression context is null

解压过程中检测到解压缩表项为空。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the decompression context is  invalid

解压过程中检测到解压缩表项无效。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the TCP checksum is error

解压过程中检测到TCP Checksum字段错误。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the generation number is mismatched

解压缩过程中检测到Generation Number字段不匹配。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the time for receiving the packet is lawless

解压过程中检测到接收COMPRESSED_NON_TCP报文的时间非法。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the sequence number is mismatched

解压过程中检测到Sequence Number字段与解压表想中的不匹配。这时解压端会向压缩端发送一个CONTEXT_STATE报文

【举例】

\# 两台设备Rouetr A和Router B用Serial接口相连，两端都配置IPHC压缩，打开Router A的IPHC TCP头压缩调试信息开关。当Router A以Telnet方式登录Router B时，Router A上TCP头压缩解压缩调试信息如下。

\<RouterA\> debugging ppp compression iphc tcp

\*Dec  8 11:23:00:081 2013 RouterA IPHC/7/PACKET: -MDC=1;THC: sent FULL_HEADER, connect ID 4, checksum 0x40b8, seq 1872787448

*[// TCP*]*头压缩信息：报文流ID为4，发送FULL_HEADER报文，校验和为0x40b8，序列号为1872787448*

\*Dec  8 11:23:00:081 2013 RouterA PPP/7/PACKET: -MDC=1;

  PPP Packet:

      Serial2/1/0 output IPHC(0061) packet, pktLen 56

*[// Serial2/1/0*]*接口发送IPHC报文，报文长度为56*

\*Dec  8 11:23:00:082 2013 RouterA IPHC/7/PACKET: -MDC=1;

 THC: sent COMPRESSED_TCP, connect ID 4, checksum 0x016a, seq 1872787448

*[// TCP*]*头压缩信息：报文流ID为4，发送COMPRESSED_TCP报文，校验和为0x016a，序列号为1872787448*

\*Dec  8 11:23:00:082 2013 RouterA PPP/7/PACKET: -MDC=1;

  PPP Packet:

      Serial2/1/0 output IPHC(0063) packet, pktLen 38

*[// Serial2/1/0*]*接口发送IPHC报文，报文长度为38*

\*Dec  8 11:23:00:083 2013 RouterA PPP/7/PACKET: -MDC=1;

  PPP Packet:

      Serial2/1/0 input IPHC(0061) packet, pktLen 56

*[// Serial2/1/0*]*接口接收IPHC报文，报文长度为56*

\*Dec  8 11:23:00:083 2013 RouterA IPHC/7/PACKET: -MDC=1;

 THC: received FULL_HEADER, connect ID 52, checksum 0x40a6, seq 766841932

*[// TCP*]*头压缩信息：报文流ID为52，接收FULL_HEADER报文，校验和为0x40a6，序列号为766841932*

\*Dec  8 11:23:00:088 2013 RouterA PPP/7/PACKET: -MDC=1;

  PPP Packet:

      Serial2/1/0 input IPHC(0063) packet, pktLen 41

*[// Serial2/1/0*]*接口接收IPHC报文，报文长度为41*

\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/PACKET: -MDC=1;

 THC: received COMPRESSED_TCP, connect ID 4, checksum 0xed67, seq 766841932

*[// TCP*]*头压缩信息：报文流ID为4，接收COMPRESSED_TCP报文，校验和为0x40a6，序列号为766841932*

\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/IPHC Event: -MDC=1;

 THC ERROR: Delta th_win code error, connect ID 4

*[// TCP*]*头压缩错误信息：报文流ID为4，在压缩TCP报文过程中Delta Window字段编码错误*

\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/PACKET: -MDC=1;

 THC: sent FULL_HEADER, connect ID 4, checksum 0x4086, seq 1872787430

*[// TCP*]*头压缩信息：报文流ID为4，发送FULL_HEADER报文，校验和为0x4086，校验和为1872787430*

\*Dec  8 11:23:00:088 2013 RouterA PPP/7/PACKET: -MDC=1;

  PPP Packet:

      Serial2/1/0 output IPHC(0061) packet, pktLen 56

*[// Serial2/1/0*]*接口发送IPHC报文，报文长度为56*

\*Dec  8 11:23:00:088 2013 RouterA IPHC/7/PACKET: -MDC=1;

 THC: sent COMPRESSED_TCP, connect ID 4, checksum 0x22fa, seq 1872787430

*[// TCP*]*头压缩信息：报文流ID为4，发送COMPRESSED_TCP报文，校验和为0x016a，序列号为1872787448*

*\
*

**PPPoE \-- PPPoE Server调试命令 \-- debugging pppoe-server**

------------------------------------------------------------------------

【命令】

**[debugging pppoe-server**[ { **all** \| **error** \| **event** \| **packet** [ **receive** \| **send** ] \| **timer** }  **interface** *interface-type interface-number* ]]

**[undo**[ **debugging pppoe-server** { **all** \| **error** \| **event** \| **packet** [ **receive** \| **send** ] \| **timer** }  **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet send**]：表示PPPoE发送报文调试信息开关。

**[packet receive**]：表示PPPoE接收报文的调试信息开关。

**[timer**]：表示定时器调试信息开关。

**[interface***interface-type interface-number*]：指定的接口类型和编号。

【使用指导】

**[debugging pppoe-server**]命令用来打开PPPoE Server的调试信息开关。**undo debugging pppoe-server**命令用来关闭PPPoE Server的调试信息开关。

缺省情况下，PPPoE Server的所有调试信息开关均处于关闭状态。

表2-1 debugging pppoe-server error命令输出信息描述表

字段

描述

Failed to start the PPPoE server process on slot *slotnum*.

启动单板*slotnum*上的PPPoE server进程失败

Received a packet with an invalid-length PPP-Max-Payload tag (len=*length*).

收到的报文的PPP-Max-Payload Tag长度错误

Wrong PPP-Max-Payload tag value (value=*value*).

PPP-Max-Payload Tag的值错误

Failed to assign a session ID.

分配会话ID失败

Failed to enable VLAN broadcast on VLAN interface *interface-name*.

VLAN接口*interface-name*使能接收广播报文失败

Interface *interface-name* received a packet with an invalid-length circuit-id tag (len=*length*).

接口*interface-name*收到报文中circuit-id的数据长度错误，数据长度为*length*

Interface *interface-name* failed to parse the Enterprise Code in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的企业码错误

Interface *interface-name* failed to parse port type in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的接口类型失败

Interface *interface-name* failed to parse the frame number in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的框号失败

Interface *interface-name* failed to parse the slot number in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的板号失败

Interface *interface-name* failed to parse the subslot number in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的子卡号失败

Interface *interface-name* failed to parse the ATM port in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的ATM接口号失败

Interface *interface-name* failed to parse the ATM VPI in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的ATM VPI失败

Interface *interface-name* failed to parse the ATM VCI in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的ATM VCI失败

Interface *interface-name* failed to parse port in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的端口号失败

Interface *interface-name* failed to parse the VLAN ID in the circuit ID by using TR101.

接口*interface-name*解析TR-101格式的circuit-id的VLAN号失败

Interface *interface-name* received a packet with a zero-length remote-id tag.

接口*interface-name*接收的报文remote-id的长度为0

Interface *interface-name* failed to parse the remote ID by using format *format*.

接口*interface-name*以*format*格式解析remote-id失败。*format*为解析格式类型：1表示hex类型，2表示ascii类型

Interface *interface-name* failed to parse the Vendor-Specific tag.

接口*interface-name*解析TAG Vendor Specify失败

Interface *interface-name* failed to send a PADS packet (sid=*sessionid*).

接口*interface-name*发送PADS报文失败（会话ID为*sessionid*）

Interface *interface-name* received a PADR packet with an illegal-length Vendor-Specific tag (len=*length*).

接口*interface-name*收到的PADR报文中TAG Vendor-specify的长度非法（Tag的长度为*length*）

Interface *interface-name* received a PADR packet with a wrong Enterprise Code in the Vendor-Specific tag.

接口*interface-name*收到的PADR报文中TAG Vendor-specify的企业码错误

Interface *interface-name* received a PADR packet with a format error for the Vendor-Specific tag.

接口*interface-name*收到的PADR报文中TAG Vendor-specify的格式错误

Interface *interface-name* received a packet with  illegal tag length.

接口*interface-name*收到报文中TAG的长度非法

Interface *interface-name* received a packet with a nonzero- length End-Of-List tag.

接口*interface-name*收到报文中end-of-list tag长度不为0

Interface *interface-name* received a packet containing an ERROR tag (type = *type*).

接口*interface-name*收到报文中包含类型为*type*的错误tag

Interface *interface-name* received a packet with zero or more than one Service-Name tag.

接口*interface-name*收到报文中包含的service-name tag的个数不为1

Interface *interface-name* received a PADI packet with wrong dest-MAC.

接口*interface-name*收到的PADI报文的目的MAC地址错误

Interface *interface-name* received a PADI packet with wrong session-id *sessionid*.

接口*interface-name*收到的PADI报文的会话ID错误

Interface *interface-name* throttled the client MAC address.

接口*interface-name*扼制了对端MAC地址

Interface *interface-name* failed to add the AC-Name tag.

接口*interface-name*向报文中添加ac-name tag失败

Interface *interface-name* failed to send a PADO packet.

接口*interface-name*发送PADO报文失败

Interface *interface-name* received a PADR packet with wrong dest-MAC.

接口*interface-name*收到的PADR报文的目的MAC地址错误

Interface *interface-name* received a PADR packet with non-zero session-id *sessionid*.

接口*interface-name*收到的PADR报文的会话ID不为0，为*sessionid*

Interface *interface-name* failed to add a session.

接口*interface-name*添加会话失败

Interface *interface-name* failed to send a PADS packet (sid=*sessionid*).

接口*interface-name*发送PADS报文失败（会话ID为*sessionid*）

Interface *interface-name* received a PADT packet with illegal session-id *sessionid*.

接口*interface-name*收到的PADT报文的会话ID非法，会话ID为*sessionid*

Interface *interface-name* received too small a packet of length *length*.

接口*interface-name*收到的报文总长度过短，报文总长度为*length*

Interface *interface-name* received a packet with too large a payload of length *length*.

接口*interface-name*收到的报文负载长度过长，负载长度为*length*

Interface *interface-name* received a packet with wrong length *length*.

接口*interface-name*收到的报文总长度错误，报文总长度为*length*

Interface *interface-name* received packet with wrong ETHER_TYPE *ether_type*.

接口*interface-name*收到的报文ETHER_TYPE字段错误，ETHER_TYPE字段的值为*ether_type*

Interface *interface-name* received a packet with wrong source MAC address.

接口*interface-name*收到的报文的源MAC地址错误

Interface *interface-name* received a packet with wrong version or type.

接口*interface-name*收到的报文的VERSION字段或者TYPE字段错误

Interface *interface-name* failed to create a VA interface.

接口*interface-name*创建VA口失败

Interface *interface-name* failed to get the local MAC address.

接口*interface-name*获取本地MAC地址失败

The kernel of interface *interface-name* failed to get the local MAC address.

接口*interface-name*的内核获取本地MAC地址失败

*[interface-name* VA of %u is invalid.]

接口*interface-name*的VA接口索引非法

Interface *interface-name* received a packet with a source MAC address mismatched with the peer MAC address stored in the local session.

接口*interface-name*收到的报文包含的对端MAC地址与本地会话中保存的对端MAC地址不匹配

Interface *interface-name* received an invalid Ethernet packet with session id *sessionid*.

接口*interface-name*收到了非法以太网报文，会话ID为*sessionid*

Interface *interface-name* failed to add the PPPoE header.

接口*interface-name*为PPP报文添加PPPoE报文头失败

表2-2 debugging pppoe-server event命令输出信息描述表

字段

描述

The standby MPU received an upgrade-to-active event.

备板收到升级为主板事件

Slot *number* inserted.

插入单板*number*

Slot *number* removed.

拔出单板*number*

An interface activation event occurred on interface *interface-name*.

接口*interface-name*发生接口激活事件

An interface deactivation event occurred on interface *interface-name*.

接口*interface-name*发生接口去激活事件

An interface deletion event occurred on interface *interface-name*.

接口*interface-name*发生接口删除事件

An interface down event occurred on interface *interface-name*.

接口*interface-name*发生接口down事件

An interface shutdown event occurred on interface *interface-name*.

接口*interface-name*发生接口shutdown事件

A MAC address change event occurred on interface *interface-name*.

接口*interface-name*发生接口MAC地址变化事件

Interface *interface-name* received a PVC down event (VEMap=*number*).

接口*interface-name*接收到PVC down事件（VE接口映射为*number*）

Interface *interface-name* received a PPP down event (sid=*sessionid*).

接口*interface-name*接收到PPP down事件（会话ID为*sessionid*）

Interface *interface-name* was configured not to trust the access line ID.

接口*interface-name*配置不信任接入线路ID，忽略circuit-id

Interface *interface-name* parsed the content of the access line ID as *content*.

接口*interface-name*解析出的接入线路ID内容为*content*

Interface *interface-name* ignored data of an known type in the Vendor-Specific tag (type=*type*).

接口*interface-name*忽略未知类型为*type*的Vendor Specify数据

Interface *interface-name* ignored a tag (type=*type*).

接口*interface-name*忽略类型为*type*的tag

The session number reached per-card limit.

单板建立会话数达到上限

*[T*he session number for VLAN *number* on the peer reached per-VLAN limit on interface *interface-name*.]

接口*interface-name*下对端VLAN *number*建立的会话数达到上限

The session number reached the interface limit on interface *interface-name*.

接口*interface-name*下建立的会话数达到上限

The session number for a client MAC reached per-MAC limit on interface *interface-name*.

接口*interface-name*下对端Client MAC建立的会话数达到上限

PPPoE server was enabled on interface *interface-name*.

接口*interface-name*使能PPPoE Server成功

PPPoE server was disabled on interface *interface-name*.

接口*interface-name*去使能PPPoE Server成功

Interface *interface-name* got session information successfully.

接口*interface-name*获取会话信息成功

Interface *interface-name* deleted all sessions successfully.

接口*interface-name*删除会话信息成功

The kernel of interface *interface-name* received an interface deletion event.

接口*interface-name*的内核接收到接口删除事件

The kernel of interface *interface-name* received an interface deactivation event.

接口*interface-name*的内核接收到接口去激活事件

The kernel of interface *interface-name* received an interface down event.

接口*interface-name*的内核接收到接口down事件

The kernel of interface *interface-name* received a MAC address change event.

接口*interface-name*的内核接收到MAC地址变化事件

Connected to LICENSE module.

PPPoES模块与LICENSE模块的连接建立成功

Failed to connect to LICENSE module.

PPPoES模块与LICENSE模块的连接建立失败

Disconnected from LICENSE module.

PPPoES模块与LICENSE模块的连接断开成功

Received LICENSE event: EventType=*event-type*.

PPPoES收到LICENSE的EventType事件

EventType类型如下：

·Installed：安装

·Uninstalled：卸载

·Expired：过期

Changed the session limit from *old-value* to *new-value* per card.

**[步骤1**更新LICENSE]定制的PPPoES单板会话限制数

·*old-value*：旧的PPPoES单板会话限制数

·*new-value*：新的PPPoES单本会话限制数

表2-3 debugging pppoe-server packet send命令输出信息描述表

字段

描述

Interface *interface-name* sent a PADT packet (sid=*sessionid*, err=*errcode*).

接口*interface-name*发送PADT报文（会话ID为*sessionid*，错误码为*er-code*）

Interface *interface-name* sent a PADS packet (sid=*sessionid*).

接口*interface-name*发送PADS报文（会话ID为*sessionid*）

Interface *interface-name* sent a PADO packet.

接口*interface-name*发送PADO报文

表2-4 debugging pppoe-server packet receive命令输出信息描述表

字段

描述

Interface *interface-name* received a PADI packet.

接口*interface-name*接收到PADI报文

Interface *interface-name* received a PADR packet.

接口*interface-name*接收到PADR报文

Interface *interface-name* received a PADT packet (sid =*sessionid*)*.

接口*interface-name*接收到PADT报文，会话ID为*sessionid*

Interface *interface-name* received an unknown packet (code=*code*).

接口*interface-name*接收到未知报文，报文类型为*code*

Interface *interface-name* dropped a multicast or broadcast PPPoE packet.

接口*interface-name*丢弃目的地址不为单播的PPPoE报文

Interface *interface-name* dropped a PPPoE packet of incorrect length.

接口*interface-name*丢弃长度错误的PPPoE报文

Interface *interface-name* dropped an invalid PPPoE packet.

接口*interface-name*丢弃非法PPPoE报文

Interface *interface-name* received an error packet.

接口*interface-name*接收到错误的报文

表2-5 debugging pppoe-server timer命令输出信息描述表

字段

描述

Interface *interface-name* created aging timer for throttled MAC entries.

接口*interface-name*创建MAC扼制老化定时器

Interface *interface-name* started aging throttled MAC entries.

接口*interface-name*开始进行MAC遏制表项老化

【举例】

\# 打开PPPoE Server错误调试信息开关。在接口GigabitEthernet1/0/1上使能PPPoE Server，并绑定一个不存在的虚拟模板接口，当接口GigabitEthernet1/0/1收到会话请求后，系统将输出下列调试信息：

\<Sysname\> debugging pppoe-server error

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pppoe-server bind virtual-template 3

\*May 21 16:46:23:365 2013 Sysname PPPOES/7/ERROR: -MDC=1-Slot=0; Interface GigabitEthernet1/0/1 failed to add a session.

*// 接口GigabitEthernet1/0/1添加会话失败*

\# 打开PPPoE Server事件调试信息开关。在接口GigabitEthernet1/0/1上使能PPPoE Server。当**shutdown**接口GigabitEthernet1/0/1时，系统将输出下列调试信息：

\<Sysname\> debugging pppoe-server event

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pppoe-server bind virtual-template 2

Sysname-GigabitEthernet1/0/1 shutdown

\*May 21 16:47:45:259 2013 Sysname PPPOES/7/EVENT: -MDC=1; An interface shutdown event occurred on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1发生接口shutdown事件*

\*May 21 16:47:45:264 2013 Sysname PPPOES/7/EVENT: -MDC=1; An interface down event occurred on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1发生接口down事件*

\*May 21 16:47:45:279 2013 Sysname PPPOES/7/EVENT: -MDC=1; The kernel of interface GigabitEthernet1/0/1 received an interface down event.

*// 接口GigabitEthernet1/0/1的内核接收到接口down事件*

\# 打开PPPoE Server的PPPoE报文调试信息开关。在接口GigabitEthernet1/0/1上使能PPPoE Server（绑定的虚拟模板接口存在），当接口GigabitEthernet1/0/1收到会话请求后，系统将输出下列调试信息：

\<Sysname\> debugging pppoe-server packet

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pppoe-server bind virtual-template 2

\*May 21 17:07:10:740 2013 Sysname PPPOES/7/PACKET_RECEIVE: -MDC=1; Interface GigabitEthernet1/0/1 received a PADR packet.

\*May 21 17:07:10:751 2013 Sysname PPPOES/7/PACKET_SEND: -MDC=1; Interface GigabitEthernet1/0/1 sent a PADS packet (sid=1).

*// 接口GigabitEthernet1/0/1接收到PADR报文，回复PADS报文*

\# 打开PPPoE Server的PPPoE定时器调试信息开关。在接口GigabitEthernet1/0/1上使能PPPoE Server（绑定的虚拟模板接口存在），当接口GigabitEthernet1/0/1第一次收到会话请求时，系统将输出下列调试信息：

\<Sysname\> debugging pppoe-server timer

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pppoe-server bind virtual-template 2

Sysname-GigabitEthernet1/0/1 pppoe-server throttle per-mac 1 5 1000

\*May 21 17:07:10:740 2013 Sysname PPPOES/7/TIMER: -MDC=1; Interface GigabitEthernet1/0/1 created aging timer for throttled MAC entries.

*// 接口GigabitEthernet1/0/1创建了MAC扼制老化定时器*

**PPPoE \-- PPPoE Client调试命令 \-- debugging pppoe-client**

------------------------------------------------------------------------

【命令】

**[debugging pppoe-client **[{ **all \| data \| error \| event \| packet** } [ **interface** *interface-type interface-number* ]]]

**[undo debugging pppoe-client **[{ **all \| data \| error \| event \| packet** } [ **interface** *interface-type interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[data**]：表示session阶段的数据调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示PPPoE协议报文调试信息开关。

**[interface***interface-type interface-number*]：指定的接口类型和编号。

【使用指导】

**[debugging pppoe-client**]命令用来打开PPPoE Client的调试信息开关。**undo debugging pppoe-client**命令用来关闭PPPoE Client的调试信息开关。

缺省情况下，PPPoE Client的所有调试信息开关均处于关闭状态。

表2-6 debugging pppoe-client error命令输出信息描述表

字段

描述

The attach process timed out for bundle *number* on interface *interface-name.*

bundle *number*对应的客户端绑定处理超时，对应接口为*interface-name*

The detach process timed out for bundle *number*.

bundle *number*对应的客户端去绑定处理超时

Failed to create a session for client of bundle *number*.

为bundle *number*对应的客户端创建会话失败

The index *index* in dialer message is invalid.

拨号信息中的索引号无效

The index *index* in bundle message is invalid.

绑定信息中的索引号无效

The dialer message(*type*) is invalid, bundle *number*.

bundle *number*对应客户端的拨号信息无效，其中*type*类型如下：

·DDR_DIALPRIM_CONN_REQ：建链请求

·DDR_DIALPRIM_CONN_IND：建链成功指示

·DDR_DIALPRIM_DISCONN_REQ：断链请求

·DDR_DIALPRIM_DISCONN_IND：断链指示

Failed to process a dialer message(*type*), bundle *number*.

为bundle *number*对应的客户端处理拨号信息失败，其中*type*类型如下：

·DDR_DIALPRIM_CONN_REQ：建链请求

·DDR_DIALPRIM_CONN_IND：建链成功指示

·DDR_DIALPRIM_DISCONN_REQ：断链请求

·DDR_DIALPRIM_DISCONN_IND：断链指示

Failed to process bundle message(*type*), interface *interface-name*, bundle *number*.

为bundle *number*对应的客户端处理绑定信息失败，对应接口为*interface-name*，其中*type*类型如下：

·DDR_BUNDLEPRIM_ATTACH：绑定

·DDR_BUNDLEPRIM_DETACH：去绑定

Failed to create a timer for connection to DDR daemon.

创建用于与DDR守护进程连接的定时器失败

Failed to send a bundle message (*type*) of bundle *number* on interface *interface-name.*

为bundle *number*对应的客户端发送绑定信息失败，对应接口为*interface-name*，其中*type*类型如下：

·DDR_BUNDLEPRIM_ATTACH：绑定

Failed to send a bundle message (*type*) of bundle *number*.

为bundle *number*对应的客户端发送绑定信息失败，其中*type*类型如下：

·DDR_BUNDLEPRIM_DETACH：去绑定

Failed to send a dialer message (*type*), bundle *number*.

为bundle *number*对应的客户端发送拨号信息失败，其中*type*类型如下：

·DDR_DIALPRIM_CONN_REQ：建链请求

·DDR_DIALPRIM_CONN_IND：建链成功指示

·DDR_DIALPRIM_DISCONN_REQ：断链请求

·DDR_DIALPRIM_DISCONN_IND：断链指示

Failed to retransmit a PADR packet, bundle *number*.

为bundle *number*对应的客户端重传PADR报文失败

Failed to retransmit a PADI packet, bundle *number*.

为bundle *number*对应的客户端重传PADI报文失败

Failed to disconnect the connection to DDR daemon, bundle *number*.

为bundle *number*对应的客户端向DDR拆链失败

Failed to send a PADI packet, bundle *number*.

为bundle *number*对应的客户端发送PADI报文失败

Failed to send a PADR packet, bundle *number*.

为bundle *number*对应的客户端发送PADR报文失败

Failed to transfer the state of session, bundle *number*.

为bundle *number*对应的客户端迁移会话状态失败

HA upgrade failed.

HA升级失败

Failed to transfer the session state. Drop the PADS packet.

状态迁移失败。丢弃PADS报文

Failed to transfer the session state. Drop the PADT packet.

状态迁移失败。丢弃PADT报文

Failed to create a timer for packet retransmission, bundle *number*.

为bundle *number*对应的客户端创建报文重传定时器失败

Failed to synchronize the data to slot *slot-id* cpu *cpu-id*.

同步数据到指定板（板号为*slot-id*）的指定CPU（CPU编号为*cpu-id*）失败

Failed to synchronize the data to other slots.

同步数据到各板失败

Failed to synchronize the data to kernel.

同步数据到内核失败

Failed to add a duplicate session of session *id*.

为session *id*重复添加会话失败

Not enough memory.

内存不足

PPPoE client is not in session stage on interface *interface-name.*

接口*interface-name*上PPPOE客户端未处于会话阶段

Failed to get the session for interface *interface-name.*

接口*interface-name*上获取会话失败

Failed to process the PPP packet on link layer, session ID id, MAC mac-addr.

在链路层处理PPP报文失败，对应SESSION_ID为id且源MAC地址为mac-addr

Failed to delete a virtual-access interface.

删除Virtual-access接口失败

Failed to create a virtual-access interface.

创建Virtual-access接口失败

表2-7 debugging pppoe-client event命令输出信息描述表

字段

描述

Received a bundle message(type) for bundle *number* on interface *interface-name*.

bundle *number*对应的客户端收到绑定信息，对应接口为*interface-name*，其中*type*类型如下：

·DDR_BUNDLEPRIM_ATTACH：绑定

·DDR_BUNDLEPRIM_DETACH：去绑定

Successfully created a virtual-access interface.

成功创建Virtual-access接口

Successfully deleted a virtual-access interface.

成功删除Virtual-access接口

Successfully created a session, bundle *number*.

为bundle *number*对应的客户端创建会话成功

The session is already in PPPoE session stage, bundle *number*.

bundle *number*对应的客户端的会话已处于SESSION阶段

The session of bundle *number* does not exist.

bundle *number*对应的会话不存在

Received a dialer message(*type*) of bundle *number*.

bundle *number*对应的客户端接收到拨号信息，其中*type*类型如下：

·DDR_DIALPRIM_CONN_REQ：建链请求

·DDR_DIALPRIM_CONN_IND：建链成功指示

·DDR_DIALPRIM_DISCONN_REQ：断链请求

·DDR_DIALPRIM_DISCONN_IND：断链指示

PPPoE client function is not configured with bundle *number*.

bundle *number*对应的客户端未配置

The connection to DDR daemon disconnected. Try again.

与DDR 守护进程连接挂断。重建连接

Successfully sent a bundle message (*type*) of bundle *number* on interface *interface-name*.

为bundle *number*对应的客户端发送绑定信息成功，对应接口为*interface-name*，其中Type类型为：

·DDR_BUNDLEPRIM_ATTACH：绑定

Successfully sent a bundle message (*type*) of bundle *number*.

为bundle *number*对应的客户端发送绑定信息成功，其中Type类型为：

·DDR_BUNDLEPRIM_DETACH：去绑定

Successfully sent a dialer message (*type*), bundle *number*.

为bundle *number*对应的客户端发送拨号信息成功，其中*type*类型如下：

·DDR_DIALPRIM_CONN_REQ：建链请求

·DDR_DIALPRIM_CONN_IND：建链成功指示

·DDR_DIALPRIM_DISCONN_REQ：断链请求

·DDR_DIALPRIM_DISCONN_IND：断链指示

Successfully retransmitted a PADI packet, bundle *number*.

为bundle *number*对应的客户端重传PADI报文成功

Successfully retransmitted a PADR packet, bundle *number*.

为bundle *number*对应的客户端重传PADR报文成功

The state of session transferred from *oldstate* to *newstate*, bundle *number*.

bundle *number*对应客户端的会话状态从*oldstate*迁移到*newstate*，其中*oldstate*和*newstate*类型如下：

·IDLE：初始化状态

·PADI SENT：已发送PADI报文、等待PADO报文状态

·PADR SENT：已发送PADR报文、等待PADS报文状态

·SESSION：会话协商成功

Received an interface *event* event on interface *interface-name*.

在*interface-name*上收到接口*event*事件，事件类型如下：

·active：接口激活事件

·deactive：接口去激活事件

·delete：接口删除事件

·down：接口Down事件

·set mac：设置接口MAC地址事件

表2-8 debugging pppoe-client packet命令输出信息描述表

字段

描述

Successfully sent a PADI packet, bundle *number*.

为bundle *number*对应的客户端发送PADI报文成功

Successfully sent a PADR packet, bundle *number*.

为bundle *number*对应的客户端发送PADR报文成功

Dropped the PADO packet for incorrect SESSION_ID (*id*).

丢弃PADO报文，因为SESSION_ID(*id*)错误

Dropped the PADO packet for incorrect End-of-List tag.

丢弃PADO报文，因为End-of-List tag错误

Dropped the PADO packet for Service-Name-Error, AC-System-Error, or Generic-Error tag.

丢弃PADO报文，因为至少携带以下一种错误Tag：

·Service-Name-Error：表示没有理睬所请求的Service-Name

·AC-System-Error：表示访问集中器在处理主机请求时出现了错误

·Generic-Error tag：表示报文出错

Dropped the PADO packet for incorrect Host-Uniq tag.

丢弃PADO报文，因为Host-Uniq tag错误

No Service-Name tag in the PADO packet.

PADO报文中未携带Service-Name tag

No AC-Name tag in the PADO packet.

PADO报文中未携带AC-Name tag

Dropped the PADO packet for no client is found.

丢弃PADO报文，因为未找到会话对应的客户端

Dropped the PADS packet for incorrect SESSION_ID (*id*).

丢弃PADS报文，因为SESSION_ID(*id*)错误

Dropped the PADS packet for incorrect End-of-List tag.

丢弃PADS报文，因为End-of-List tag错误

Dropped the PADS packet for Service-Name-Error, AC-System-Error, or Generic-Error tag.

丢弃PADO报文，因为至少携带以下一种错误Tag：

·Service-Name-Error：表示没有理睬所请求的Service-Name

·AC-System-Error：表示访问集中器在处理主机请求时出现了错误

·Generic-Error tag：表示报文出错

Dropped the PADS packet for incorrect Host-Uniq tag.

丢弃PADS报文，因为Host-Uniq tag错误

No Service-Name tag in the PADS packet.

PADS报文中未携带Service-Name tag

No AC-Name tag in the PADS packet.

PADS报文中未携带AC-Name tag

Dropped the PADS packet for no client is found.

丢弃PADS报文，因为未找到会话对应的客户端

Dropped the PADT packet for incorrect SESSION_ID (*id*).

丢弃PADT报文，因为SESSION_ID(*id*)错误

Dropped the PADT packet for no client is found.

丢弃PADT报文，因为未找到会话对应的客户端

Sent a *type* packet on interface *interface-name*, length *length*.

在接口*interface-name*上发送长度为*length*的*type*报文，其中*type*类型如下：

·PADI：PADI报文

·PADR：PADR报文

·PADT：PADT报文

Received a *type* packet on interface *interface-name*, length *length*.

在接口*interface-name*上接收长度为*length*的*type*报文，其中*type*类型如下：

·PADO：PADO报文

·PADS：PADS报文

·PADT：PADT报文

表2-9 debugging pppoe-client data命令输出信息描述表

字段

描述

PPPoE Client is not configured on interface *interface-name.*

接口*interface-name*上未配置PPPoE Client

Dropped a multicast/broadcast PPPoE packet on interface *interface-name.*

接口*interface-name*上丢弃一个广播（多播）PPPoE报文

Dropped a PPPoE packet of incorrect length on interface *interface-name.*

接口*interface-name*上丢弃一个长度错误的PPPoE报文

Dropped an invalid PPPoE packet on interface *interface-name.*

接口*interface-name*上丢弃一个非法的PPPoE报文

【举例】

\# 打开PPPoE Client错误调试信息开关，在接口GigabitEthernet1/0/1配置一个PPPoE Client，对应bundle number为1，如果DDR守护进程已关闭，复位会话后，系统将输出下列调试信息。

\<Sysname\> debugging pppoe-client error

\<Sysname\> reset pppoe-client dial-bundle-number 1

\*Jun 23 15:50:40:899 2011 Sysname PPPOEC/7/ERROR: -MDC=1; Failed to disconnect the connection to DDR daemon, bundle 1.

*// 为bundle 1对应的客户端向DDR拆链失败*

\# 打开PPPoE Client事件调试信息开关，在接口GigabitEthernet1/0/1配置一个PPPoE Client，对应bundle number为1，且会话处于session阶段，复位会话后，系统将输出下列调试信息。

\<Sysname\> debugging pppoe-client event

\<Sysname\> reset pppoe-client dial-bundle-number 1

\*Jun 23 15:50:40:899 2011 Sysname PPPOEC/7/EVENT: -MDC=1; The state of session transferred from SESSION to IDLE, bundle 1.

*// 会话从SESSION状态迁移到IDLE状态*

\# 打开PPPoE Client的PPPoE协议报文调试信息开关。在接口GigabitEthernet1/0/1配置一个PPPoE Client，系统将输出下列调试信息。

\<Sysname\> debugging pppoe-client packet

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pppoe-client dial-bundle-number 1

\*Aug 21 11:05:25:202 2011 Sysname PPPOEC/7/PACKET: -MDC=1; Sent a PADI packet on interface GigabitEthernet1/0/1, length 16.

11 09 00 00 00 0a 01 01 00 00 01 03 00 02 02 00

*[// GigabitEthernet1/0/1*]*接口发送PADI报文，报文长度为16。版本为0x01，类型为0x01，SESSION_ID为0*

\# 打开PPPoE Client在session阶段的数据调试信息开关。接口GigabitEthernet1/0/1收到一个长度错误的PPPoE报文时，系统将输出下列调试信息。

\<Sysname\> debugging pppoe-client data

\*Jun 23 15:50:40:899 2011 Sysname PPPOEC/7/DATA: -MDC=1; Dropped a PPPoE packet of incorrect length on interface GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上丢弃一个长度错误的PPPoE报文*

