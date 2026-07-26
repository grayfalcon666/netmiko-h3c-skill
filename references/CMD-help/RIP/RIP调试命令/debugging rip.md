
**RIP \-- RIP调试命令 \-- debugging rip**

------------------------------------------------------------------------

【命令】

**[debugging** **rip** *process-id*]

**[undo** **debugging** **rip** *process-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

【描述】

**[debugging rip**]命令用来打开RIP所有的调试信息开关。**undo debugging rip**命令用来关闭RIP所有的调试信息开关。

缺省情况下，RIP所有的调试信息开关处于关闭状态。

【举例】

\# 打开RIP进程1所有的调试信息开关。

\<Sysname\> debugging rip 1

**RIP \-- RIP调试命令 \-- debugging rip brief**

------------------------------------------------------------------------

【命令】

**[debugging** **rip** *process-id* **brief**]

**[undo** **debugging** **rip** *process-id* **brief**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

【描述】

**[debugging rip brief**]命令用来打开RIP摘要调试信息开关。**undo debugging rip brief**命令用来关闭RIP摘要调试信息开关。

缺省情况下，RIP摘要调试信息开关处于关闭状态。

表1-1 debugging rip brief命令输出信息描述表

字段

描述

RIP *process-id*

RIP进程号

Sending *packet-version* *packet-type* on *interface-type interface-number* from *source-ip*

发送RIP报文

·*packet-version*：RIP报文的版本，取值为v1或v2

·*packet-type*：RIP报文类型，取值为request或response

·*interface-type interface-number*：接口类型和接口编号，从该接口发送RIP报文

·*source-ip*：RIP报文的源IP地址

Receiving *packet-version* *packet-type* on *interface-type interface-number* from *source-ip*

接收RIP报文

·*packet-version*：RIP报文的版本，取值为v1或v2

·*packet-type*：RIP报文类型，取值为request或response

·*interface-type interface-number*：接口类型和接口编号，从该接口接收RIP报文

·*source-ip*：RIP报文的源IP地址

Packets to be sent on interface * ip-address*  have exceeded the limit, possibly causing packet loss

接口下缓存的报文数过大，可能导致丢包

·*ip-address*：接口IP地址

【举例】

\# Router A通过GigabitEthernet1/0/1接口与Router B相连，分别在Router A和Router B上配置RIP，在Router A上打开RIP摘要调试信息开关。

\<RouterA\> debugging rip 1 brief

\*Nov 24 15:28:22:814 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Sending v2 response on GigabitEthernet1/0/1 from 40.0.0.2

*[// RIP*]*进程1从接口GigabitEthernet1/0/1发送版本2的应答报文，RIP报文源地址为40.0.0.2*

\*Nov 24 15:28:34:868 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Receiving v2 response on GigabitEthernet1/0/1 from 40.0.0.1

*[// RIP*]*进程1从接口GigabitEthernet1/0/1接收版本2的应答报文，RIP报文源地址为40.0.0.1*

\*July 18 15:28:34:824 2012 RouterA RIP/7/RIPDEBUG: RIP 1 : Packets to be sent on interface 192.16.12.1 have exceeded the limit, possibly causing packet loss

*[// RIP*]*进程1从接口GigabitEthernet1/0/1发送RIP报文，缓存报文超过接口允许最大报文长度*

**RIP \-- RIP调试命令 \-- debugging rip event**

------------------------------------------------------------------------

【命令】

**[debugging** **rip** *process-id* **event**]

**[undo** **debugging** **rip** *process-id* **event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

【描述】

**[debugging rip event**]命令用来打开RIP事件调试信息开关。**undo debugging rip event**命令用来关闭RIP事件调试信息开关。

缺省情况下，RIP事件调试信息开关处于关闭状态。

表1-2 debugging rip event命令输出信息描述表

字段

描述

RIP *process-id*

RIP进程号

TRIP *process-id*

TRIP进程号

Enabled RIP on *interface-type interface-number*

在RIP进程里发布接口对应的网段

·*interface-type interface-number*：接口类型和接口编号

Disabled RIP on *interface-type interface-number*

在RIP进程里取消发布接口对应的网段

·*interface-type interface-number*：接口类型和接口编号

Triggered update sent

路由表发生变化，发送触发更新报文

Failed to add RIP route

添加路由失败

Failed to add TRIP route

添加TRIP路由失败

Prefix list used in filter-policy export has changed

用于过滤发布路由信息的IP地址前缀列表发生变化

Prefix list used in filter-policy import has changed

用于过滤接收路由信息的IP地址前缀列表发生变化

The ACL used in filter-policy export has changed

用于过滤发布路由信息的访问控制列表发生变化

The ACL used in filter-policy import has changed

用于过滤接收路由信息的访问控制列表发生变化

Received default-route result of route-policy

收到缺省路由的路由策略上报结果

Joining multicast group failed on *interface-type interface-number*

接口加入组播组失败

·*interface-type interface-number*：接口类型和接口编号

Quitting multicast group failed on *interface-type interface-number*

接口删除组播组失败

·*interface-type interface-number*：接口类型和接口编号

Enable packet to CPU failed on *interface-type interface-number*

使能报文上送CPU失败

·*interface-type interface-number*：接口类型和接口编号

Disable packet to CPU failed on *interface-type interface-number*

去使能报文上送CPU失败

·*interface-type interface-number*：接口类型和接口编号

【举例】

\# Router A通过GigabitEthernet1/0/1接口与Router B相连，分别在Router A和Router B上配置RIP，在Router A上打开RIP事件信息调试开关。

\<RouterA\> debugging rip 1 event

\<RouterA\> system-view

\# 在Router A的RIP进程1下去使能接口GigabitEthernet1/0/1所在的网段40.0.0.0。

RouterA rip 1

RouterA-rip-1 undo network 40.0.0.0

\*Nov 24 15:33:24:194 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Disabled RIP on GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上去使能RIP进程1*

\# 在Router A的接口GigabitEthernet1/0/1所在的网段40.0.0.0使能RIP进程1。

RouterA-rip-1 network 40.0.0.0

\*Nov 24 15:36:12:162 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Enabled RIP on GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1上使能RIP进程1*

**RIP \-- RIP调试命令 \-- debugging rip packet**

------------------------------------------------------------------------

【命令】

**[debugging** **rip** *process-id* **packet** [ **interface** *interface-type interface-number* ]]

**[undo** **debugging** **rip** *process-id* **packet** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

**[interface***interface-type interface-number*]：接口类型和接口编号，打开指定接口的调试信息开关。

【描述】

**[debugging rip packet**]命令用来打开RIP报文调试信息开关。**undo debugging rip packet**命令用来关闭RIP报文调试信息开关。

缺省情况下，RIP报文调试信息开关处于关闭状态。

表1-3 debugging rip packet命令输出信息描述表

字段

描述

RIP *process-id*

RIP进程号

TRIP *process-id*

TRIP进程号

Suppressed updates because no route on *ip-address* to send

没有需要发送的路由项，定时更新被抑制

·*interface-type interface-number*：接口类型和编号，从该接口发送RIP报文

Sending *packet-type* on interface *interface-type interface-number* from *source-ip* to *dest-ip*

发送RIP报文

·*packet-type*：RIP报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口发送RIP报文

·*source-ip*：RIP报文的源IP地址

·*dest-ip*：RIP报文的目的地址

Packet\'s destination *dest-ip* is the IP address of local interface.

发送报文的目的地址是本地接口地址

·*dest-ip*：RIP报文的目的地址

Packets to be sent on interface *ip-address* have exceeded the limit, possibly causing packet loss

接口下待发送报文数过大，可能导致丢包

·*ip-address*：接口IP地址

Receiving *packet-type* from *source-ip* on *interface-type interface-number*

接收RIP报文

·*packet-type*：RIP报文类型，取值为request或response

·*source-ip*：接收RIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收RIP报文

Packet: version *packet-version*, cmd *cmd-value*, length *length*

RIP报文头信息

·*packet-version*：RIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为request或response

·*length*：报文长度

AFI *AFI-value*, destination *dest-ip/mask*, nexthop *nexthop*-*ip*, cost *cost*, tag *tag*

RIPv2路由表项信息

·*AFI-value*：AFI字段值，取值为2

·*dest-ip/mask*：路由表项目的地址、掩码

·*netxhop-ip*：路由表项的下一跳地址

·*cost**：*路由表项的度量值

·*tag*：路由表项的标签值

AFI *AFI-value*, destination *dest-ip*, cost *cost*

RIPv1路由表项信息

·*AFI-value*：AFI字段值，取值为2

·*dest-ip*：路由表项目的地址

·*cost*：路由表项的度量值

Failed to send socket on interface *interface-type interface-number,* return value *byte-length*

Socket报文发送失败

·*interface-type interface-number*：接口类型和编号

·*byte-length*：实际发送的长度

Routing table specific request: AFI *AFI-value*, destination *dest-ip/mask*

请求特定路由的请求报文

·*AFI-value*：AFI字段值，取值为2

·*dest-ip/mask*：路由表项目的地址

Routing table request (FULL)

请求全路由的请求报文

Authentication-mode: simple: *password*

报文认证模式为简单认证，密码为*password*

Authentication-mode: MD5 Digest: *string*

报文认证模式为MD5认证

·*string*：MD5认证的摘要

Sequence: *seq-number* (*number*)

MD5认证（RFC 2453）的序列号

Sequence: *seq-number*

MD5认证（RFC 2082）的序列号

Invalid authentication type: *number*

认证类型无效

·*number*：认证类型

Authentication RTE not first RTE

包含认证信息的RTE不是RIP报文的第一个RTE

Ignored this packet. Wrong packet length.

报文长度不正确，忽略接收的报文

Ignored this packet. Wrong packet version.

报文版本不正确，忽略接收的报文

Ignored this packet. Command field is illegal.

RIP报文command字段非法，忽略接收的报文

Ignored this packet. RIPv1 does not support multicast packet.

接口RIP版本为v1，不支持组播报文，忽略接收的报文

Ignored this packet. Invalid source port.

RIP报文源端口无效，忽略接收的报文

Ignored this packet. Version field is illegal.

RIP报文版本字段非法，忽略接收的报文

Ignored this packet. Version of packet does not match the version of RIP-interface.

RIP报文版本与接收报文的接口配置的RIP版本不匹配，忽略接收的报文

Ignored this packet. Must-Be-Zero fields are not zero.

RIP报文的Must-Be-Zero字段不等于零，忽略接收的报文

Ignored this packet. RIPv1 packet contains authentication information.

RIP报文版本为v1但包含认证信息，忽略接收的报文

Ignored this packet. Packet originated by itself.

RIP报文由自身产生，忽略接收的报文

Ignored this packet. Packet from different interface has the same source address.

来自不同接口的RIP报文的源地址相同，忽略此报文

Ignored this packet. Failed to add neighbor on the received packet.

添加邻居失败，忽略接收的报文

Ignored this packet. Authentication validation failed.

认证校验失败，忽略接收的报文

Ignored this packet. Wrong packet length.

报文长度错误，忽略接收的报文

Ignored this packet. Wrong packet version.

报文版本错误，忽略接收的报文

Ignored route *ip-address/mask-length*. AFI field is illegal.

AFI字段值非法，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Invalid destination network.

目的地址非法，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Mask is incorrect.

掩码非法，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Its nexthop is the local interface.

下一跳是本地接口，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Cannot find outgoing interface.

无法找到出接口，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Host route denied on this interface.

禁止接收主机路由的RIP进程接收到一条主机路由，忽略此路由

·*ip-address/mask-length*：路由信息的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Its destination address is on the same network of the receiving interface.

目的地址落在了接收RIP报文的接口所在的网段，忽略此路由

·*ip-address/mask-length*：目的地址和子网掩码

Ignored this route. Bad metric.

metric字段值不正确，忽略此路由

Ignored route *ip-address/mask-length*. Policy prohibits.

策略禁止，忽略路由

·*ip-address/mask-length*：目的地址和子网掩码

Ignored route *ip-address/mask-length*.. Default route configured is advertised.

正在发布缺省路由，忽略路由

·*ip-address/mask-length*：目的地址和子网掩码

Ignored route *ip-address/mask-length*. Its destination address is the same as local interface.

目的地址和本地接口IP相同，忽略路由

·*ip-address/mask-length*：目的地址和子网掩码

Ignored this packet. TRIP version is invalid on *interface-type interface-number*  from *source-ip*

TRIP报文版本不合法，忽略接收的报文

·*source-ip*：接收TRIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

Ignored this packet. Flush field is illegal on *interface-type interface-number*  from *source-ip*

TRIP报文flush字段不合法，忽略接收的报文

·*source-ip*：接收TRIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

Ignored this packet. Invalid TRIP interface on *interface-type interface-number*  from *source-ip*

TRIP接口无效，忽略接收的报文

·*source-ip*：接收TRIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

Ignored this packet. Neighbor IP mismatch, current neighbor IP is *neighbor-ip*

报文源地址和当前邻居IP地址不匹配，忽略接收的报文

·*neighbor-ip*：当前邻居IP地址

Invalid source IP address

报文的源地址无效

Failed to find receiving interface for source address *source-ip*.

无法根据源地址找到收接口

·*source-ip*：RIP报文的源IP地址

Ignored this response packet. BFD session was not up.

BFD会话没有up，不接收响应报文

Simple Password Authetication failure.

简单密码认证失败

MD5 failure - key Id mismatch.

key不一致，MD5失败

MD5 failure - Sequence number mismatch.

Sequence不一致，MD5失败

Authetication fail - MD5 Checksum error.

MD5校验和错误，认证失败

Packet receiving is ignored due to unreachable BFD Destination *dest-ip*

BFD目的地址不可达，忽略接收的报文

·*dest-ip*：BFD的目的地址

Sending *packet-type* on interface *interface-type interface-number* from *source-ip* to *dest-ip*

发送TRIP报文

·*packet-type*：TRIP报文类型，取值为request、response或acknowledgement

·*interface-type interface-number*：接口类型和编号，从该接口发送TRIP报文

·*dest-ip*：TRIP报文的目的地址

Retransmitting *packet-type* on interface *interface-type interface-number* from *source-ip* to *dest-ip*

重传TRIP报文

·*packet-type*：TRIP报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口重传TRIP报文

·*source-ip*：接收TRIP报文的源IP地址

·*dest-ip*：TRIP报文的目的地址

Receive *packet-type* from *source-ip* on *interface-type interface-number*

接收TRIP报文

·*packet-type*：TRIP报文类型，取值为request、response或acknowledgement

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

·*source-ip*：TRIP报文的源IP地址

Packet : vers *packet-version*, cmd *cmd-value*, length *length*, sequence num *sequence-num*

TRIP报文头信息

·*packet-version*：TRIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为response、response (FLUSH)、acknowledgement或acknowledgement (FLUSH)

·*length*：报文长度

·*sequence-num*：TRIP报文的序列号

Packet : vers *packet-version*, cmd *cmd-value*, length *length*

TRIP报文头信息

·*packet-version*：TRIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为request

·*length*：报文长度

【举例】

\# Router A通过接口GigabitEthernet1/0/1与Router B相连，分别在Router A和Router B上配置RIP，在Router A上打开指定接口的RIP报文调试信息开关。

\<RouterA\> debugging rip 1 packet interface gigabitethernet 1/0/1

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Sending response on interface GigabitEthernet1/0/1 from 40.0.0.2 to 224.0.0.9

*[// RIP*]*进程1从接口GigabitEthernet1/0/1发送应答报文，源地址40.0.0.2，目的地址224.0.0.9*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:   Packet: version 2, cmd response, length 64

*// 应答报文版本2，长度64字节*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.2/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第一个路由项AFI字段值为2，目的网段地址为50.0.0.2/255.255.255.255，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.0/255.0.0.0, nexthop 0.0.0.0, cost 1, tag 0

*// 第二个路由项AFI字段值为2，目的网段地址为50.0.0.0/255.0.0.0，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 110.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第三个路由项AFI字段值为2，目的网段地址为110.0.0.1/255.255.255.255，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Receiving response from 40.0.0.1 on GigabitEthernet1/0/1

*[// RIP*]*进程1从接口GigabitEthernet1/0/1接收应答报文，报文源地址40.0.0.1*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:   Packet : version 2, cmd response, length 84

*// 接收的应答报文版本2，长度84字节*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第一个路由项AFI字段值为2，目的网段地址为50.0.0.1/255.255.255.255，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.0/255.0.0.0, nexthop 0.0.0.0, cost 1, tag 0

*// 第二个路由项AFI字段值为2，目的网段地址为50.0.0.0/255.0.0.0，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:86 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 100.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第三个路由项AFI字段值为2，目的网段地址为100.0.0.1/255. 255. 255. 255，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:86 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 110.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 16, tag 0

*// 第四个路由项AFI字段值为2，目的网段地址为110.0.0.1/255. 255. 255. 255，下一跳为0.0.0.0，度量值为16，路由标签为0*

\*Nov 24 15:57:46:102 2010 RouterA RM/3/RMDEBUG: RIP 1 : Ignored this packet. Authentication validation failed.

*// 认证校验失败，忽略接收到的应答报文*

\# Router A通过接口Serial2/1/0与Router B的接口Serial2/1/0相连，分别在Router A和Router B上配置RIP，并在Serial2/1/0接口上使能TRIP，在Router A上打开RIP报文调试信息开关。

\<RouterA\> debugging rip 1 packet

\*Oct 17 14:14:04:352 2013 RouterA RIP/7/RIPDEBUG: -MDC=1; TRIP 1 : Sending request on interface Serial2/1/0 from 12.3.4.5 to 224.0.0.9

*[// TRIP*]*进程1从接口Serial2/1/0发送请求报文，目的地址224.0.0.9*

\*Oct 17 14:14:04:352 2013 RouterA RIP/7/RIPDEBUG: -MDC=1;   Packet: version 2, cmd request, length 8

*// 发送的请求报文版本2，长度8字节*

\*Oct 17 14:14:04:354 2013 RouterA RIP/7/RIPDEBUG: -MDC=1; TRIP 1 : Receiving response from 50.0.0.2 on Serial2/1/0

*[// TRIP*]*进程1从接口Serial2/1/0接收应答报文，报文源地址50.0.0.2*

\*Oct 17 14:14:04:354 2013 RouterA RIP/7/RIPDEBUG: -MDC=1;   Packet: version 2, cmd response (FLUSH), length 8, sequence num 0

*// 接收的应答报文版本2，带FLUSH，长度8字节，序列号0*

\*Oct 17 14:14:04:358 2013 RouterA RIP/7/RIPDEBUG: -MDC=1; TRIP 1 : Sending acknowledgement on interface Serial2/1/0 from 50.0.0.1 to 50.0.0.2

*[// TRIP*]*进程1从接口Serial2/1/0发送确认报文，源地址50.0.0.1，目的地址50.0.0.2*

\*Oct 17 14:14:04:355 2013 RouterA RIP/7/RIPDEBUG: -MDC=1;   Packet: version 2, cmd acknowledgement (FLUSH), length 8, sequence num 0

*// 发送的确认报文版本2，带FLUSH，长度8字节，序列号0*

**RIP \-- RIP调试命令 \-- debugging rip receive**

------------------------------------------------------------------------

【命令】

**[debugging** **rip** *process-id* **receive** [ **interface** *interface-type interface-number* ]]

**[undo** **debugging** **rip** *process-id* **receive** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

**[interface***interface-type interface-number*]：接口类型和接口编号，打开指定接口的调试信息开关。

【描述】

**[debugging rip receive**]命令用来打开RIP接收报文调试信息开关。**undo debugging rip receive**命令用来关闭RIP接收报文调试信息开关。

缺省情况下，RIP接收报文调试信息开关处于关闭状态。

表1-4 debugging rip receive命令输出信息描述表

字段

描述

RIP *process-id*

RIP进程号

TRIP *process-id*

TRIP进程号

Receiving *packet-type* from *source-ip* on *interface-type interface-number*

接收RIP报文

·*packet-type*：RIP报文类型，取值为request或response

·*source-ip*：接收RIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收RIP报文

Packet: version *packet-version*, cmd *cmd-value*, length *length*

RIP报文头信息

·*packet-version*：RIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为request或response

·*length*：报文长度

AFI *AFI-value*, destination *dest-ip/mask*, nexthop *nexthop*-*ip*, cost *cost*, tag *tag*

RIPv2路由表项信息

·*AFI-value*：AFI字段值，取值为2

·*dest-ip/mask*：路由表项目的地址、掩码

·*netxhop-ip*：路由表项的下一跳地址

·*cost*：路由表项的度量值

·*tag*：路由表项的标签值

AFI *AFI-value*, destination *dest-ip*, cost *cost*

RIPv1路由表项信息

·*AFI-value*：AFI字段值，取值为2

·*dest-ip*：路由表项目的地址

·*cost*：路由表项的度量值

Routing table specific request: AFI *AFI-value*, destination *dest-ip/mask*

请求特定路由的请求报文

·*AFI-value*：AFI字段值，取值为2

·*dest-ip/mask*：路由表项目的地址

Routing table request (FULL)

请求全部路由的请求报文

Authentication-mode: simple: *password*

报文认证模式为简单认证，密码为*password*

Authentication-mode: MD5 Digest: *string*

报文认证模式为MD5认证

·*string*：MD5认证的摘要

Sequence: *seq-number* (*number*)

MD5认证（RFC 2453）的序列号

Sequence: *seq-number*

MD5认证（RFC 2082）的序列号

Invalid authentication type: *number*

认证类型无效

·*number*：认证类型

Authentication RTE is not the first RTE

包含认证信息的RTE不是RIP报文的第一个RTE

Ignored this packet. Packet length improper.

报文长度不正确，忽略接收的报文

Ignored this packet. Version of packet is not correct.

报文版本不正确，忽略接收的报文

Ignored this packet. Command field is illegal.

RIP报文command字段非法，忽略接收的报文

Ignored this packet. RIPv1 does not support multicast packet.

接口RIP版本为v1，不支持组播报文，忽略接收的报文

Ignored this packet. Invalid source port.

RIP报文源端口无效，忽略接收的报文

Ignored this packet. Version field is illegal.

RIP报文版本字段非法，忽略接收的报文

Ignored this packet. Version of packet does not match the version of RIP interface.

RIP报文版本与接收报文的接口配置的RIP版本不匹配，忽略接收的报文

Ignored this packet. Must-Be-Zero fields are not zero.

RIP报文的Must-Be-Zero字段不等于零，忽略接收的报文

Ignored this packet. RIPv1 packet contains authentication information.

RIP报文版本为v1但包含认证信息，忽略接收的报文

Ignored this packet. Packet originated by itself.

RIP报文由自身产生，忽略接收的报文

Ignored this packet. Packet from different interface has the same source address.

来自不同接口的RIP报文的源地址相同，忽略此报文

Ignored this packet. Failed to add neighbor on the received packet.

添加邻居失败，忽略接收的报文

Ignored this packet. Authentication validation failed.

认证校验失败，忽略接收的报文

Ignored this packet. Wrong packet length.

报文长度错误，忽略接收的报文

Ignored this packet. Wrong packet version.

报文版本错误，忽略接收的报文

Ignored route *ip-address/mask-length*. AFI field is illegal.

AFI字段值非法，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Invalid destination network.

目的地址非法，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Mask is incorrect.

掩码非法，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Its nexthop is the local interface.

下一跳是本地接口，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Cannot find outing interface.

无法找到出接口，忽略此路由

·*ip-address/mask-length*：此条路由的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Host route denied on this interface.

禁止接收主机路由的RIP进程接收到一条主机路由，忽略此路由

·*ip-address/mask-length*：路由信息的目的地址和子网掩码

Ignored route *ip-address/mask-length*. Its destination address is the same as local interface\'s.

目的地址落在了本设备接口所在的网段，忽略此路由

·*ip-address/mask-length*：目的地址和子网掩码

Ignored this route. Bad metric.

metric字段值不正确，忽略此路由

Ignored route *ip-address/mask-length*. Policy prohibits.

策略禁止，忽略路由

·*ip-address/mask-length*：目的地址和子网掩码

Ignored route *ip-address/mask-length*.. Default route configured is advertised.

正在发布缺省路由，忽略路由

·*ip-address/mask-length*：目的地址和子网掩码

Ignored route *ip-address/mask-length*. Its destination address is the same as local interface.

目的地址和本地接口IP相同，忽略路由

·*ip-address/mask-length*：目的地址和子网掩码

Invalid source ip address

报文的源地址无效

Failed to find receiving interface for source address *source-ip*.

无法根据源地址找到收接口

·*source-ip*：RIP报文的源IP地址

Ignored this response packet. BFD session was not up.

BFD会话没有up，不接收响应报文

Simple Password Authetication failure.

简单密码认证失败

MD5 failure - key Id mismatch.

key不一致，MD5失败

MD5 failure - Sequence number mismatch.

Sequence不一致，MD5失败

Authetication fail - MD5 Checksum error.

MD5校验和错误，认证失败

Packet receiving is ignored due to unreachable BFD Destination *dest-ip*

BFD目的地址不可达，忽略接收的报文

·*dest-ip*：BFD的目的地址

Ignored this packet. TRIP version is invalid on *interface-type interface-number*  from *source-ip*

TRIP报文版本无效，忽略接收的报文

·*source-ip*：接收TRIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

Ignored this packet. Flush field is illegal on *interface-type interface-number*  from *source-ip*

TRIP报文flush字段不合法，忽略接收的报文

·*source-ip*：接收TRIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

Ignored this packet. Invalid TRIP interface on *interface-type interface-number*  from *source-ip*

TRIP接口无效，忽略接收的报文

·*source-ip*：接收TRIP报文的源IP地址

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

Ignored this packet. Neighbor IP mismatch, current neighbor IP is *neighbor-ip*

报文源地址和当前邻居IP地址不匹配，忽略接收的报文

·*neighbor-ip*：当前邻居IP地址

Receive *packet-type* from *source-ip* on *interface-type interface-number*

接收TRIP报文

·*packet-type*：TRIP报文类型，取值为request、response或acknowledgement

·*interface-type interface-number*：接口类型和编号，从该接口接收TRIP报文

·*source-ip*：TRIP报文的源IP地址

Packet : vers *packet-version*, cmd *cmd-value*, length *length*, sequence num *sequence-num*

TRIP报文头信息

·*packet-version*：TRIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为response、response (FLUSH)、acknowledgement或acknowledgement (FLUSH)

·*length*：报文长度

·*sequence-num*：TRIP报文的序列号

Packet : vers *packet-version*, cmd *cmd-value*, length *length*

TRIP报文头信息

·*packet-version*：TRIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为request

·*length*：报文长度

【举例】

\# Router A通过接口GigabitEthernet1/0/1与Router B相连，分别在Router A和Router B上配置RIP，在Router A上打开指定接口的RIP接收报文调试信息开关。

\<RouterA\> debugging rip 1 receive interface gigabitethernet 1/0/1

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Receiving response from 40.0.0.1 on GigabitEthernet1/0/1

*[// RIP*]*进程1从接口GigabitEthernet1/0/1接收应答报文，报文源地址40.0.0.1*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:   Packet : version 2, cmd response, length 84

*// 接收的应答报文版本2，长度84字节*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第一个路由项AFI字段值为2，目的网段地址为50.0.0.1/255.255.255.255，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.0/255.0.0.0, nexthop 0.0.0.0, cost 1, tag 0

*// 第二个路由项AFI字段值为2，目的网段地址为50.0.0.0/255.0.0.0，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:86 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 100.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第三个路由项AFI字段值为2，目的网段地址为100.0.0.1/255. 255. 255. 255，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:86 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 110.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 16, tag 0

*// 第四个路由项AFI字段值为2，目的网段地址为110.0.0.1/255. 255. 255. 255，下一跳为0.0.0.0，度量值为16，路由标签为0*

\# Router A通过接口Serial2/1/0与Router B的接口Serial2/0相连，分别在Router A和Router B上配置RIP，并在Serial2/1/0接口上使能TRIP，在Router A上打开RIP报文调试信息开关。

\<RouterA\> debugging rip 1 receive

\*Oct 17 14:14:04:354 2013 RouterA RIP/7/RIPDEBUG: -MDC=1; TRIP 1 : Receiving response from 50.0.0.2 on Serial2/1/0

*[// TRIP*]*进程1从接口Serial2/1/0接收应答报文，报文源地址50.0.0.2*

\*Oct 17 14:14:04:354 2013 RouterA RIP/7/RIPDEBUG: -MDC=1;   Packet: version 2, cmd response (FLUSH), length 8, sequence num 0

*// 接收的应答报文版本2，带FLUSH，长度8字节，序列号0*

**RIP \-- RIP调试命令 \-- debugging rip send**

------------------------------------------------------------------------

【命令】

**[debugging** **rip** *process-id* **send** [ **interface** *interface-type interface-number* ]]

**[undo** **debugging** **rip** *process-id* **send** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

**[interface***interface-type interface-number*]：接口类型和接口编号，打开指定接口的调试信息开关。

【描述】

**[debugging rip send**]命令用来打开RIP发送报文调试信息开关。**undo debugging rip send**命令用来关闭RIP发送报文调试信息开关。

缺省情况下，RIP发送报文调试信息开关处于关闭状态。

表1-5 debugging rip send命令输出信息描述表

字段

描述

RIP *process-id*

RIP进程号

TRIP *process-id*

TRIP进程号

Suppressed update because no route on *ip-address* to send

没有需要发送的路由项，定时更新被抑制

·*ip-address*：接口IP地址

Sending *packet-type* on interface *interface-type interface-number* from *source-ip* to *dest-ip*

发送RIP报文

·*packet-type*：RIP报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口发送RIP报文

·*source-ip*：RIP报文的源IP地址

·*dest-ip*：RIP报文的目的地址

Packet\'s destination *dest-ip* is the IP address of local interface.

发送报文的目的地址是本地接口地址

·*dest-ip*：RIP报文的目的地址

Packets to be sent on interface *ip-address*  have exceeded the limit, possibly causing packet loss

接口下报文数过大，可能导致丢包

·*ip-address*：接口IP地址

Packet: version *packet-version*, cmd *cmd-value*, length *length*

RIP报文头信息

·*packet-version*：RIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为request或response

·*length*：报文长度

AFI *AFI-value*, destination *dest-ip/mask*, nexthop *nexthop*-*ip*, cost *cost*, tag *tag*

RIPv2路由表项信息

·*AFI-value*：AFI字段值，取值为2

·*dest-ip/mask*：路由表项目的地址、掩码

·*netxhop-ip*：路由表项的下一跳地址

·*cost*：路由表项的度量值

·*tag*：路由表项的标签值

AFI *AFI-value*, destination *dest-ip*, cost *cost*

RIPv1路由表项信息

·*AFI-value*：AFI字段值，取值为2

·dest-ip：路由表项目的地址

·*cost*：路由表项的度量值

Failed to send socket on interface *interface-type interface-number*, return value *byte-length*

Socket报文发送失败

·*interface-type interface-number*：接口类型和编号

·*byte-length*：实际发送的长度

Routing table request (FULL)

请求全部路由的请求报文

Authentication-mode: simple: *password*

报文认证模式为简单认证，密码为*password*

Authentication-mode: MD5 Digest: *string*

报文认证模式为MD5认证

·*string*：MD5认证的摘要

Sequence: *seq-number* (*number*)

MD5认证（RFC 2453）的序列号

Sequence: *seq-number*

MD5认证（RFC 2082）的序列号

Invalid authentication type: *number*

认证类型无效

·*number*：认证类型

Packet sending is ignored due to unreachable BFD Destination *dest-ip*

发送RIP报文

·*dest-ip*：BFD目的地址

Packet sending is ignored on interface *interface-type interface-number*, please check max-packet-length.

RIP报文无法发送

·*interface-type interface-number*：接口类型和编号，从该接口发送RIP报文

Sending *packet-type* on interface *interface-type interface-number* from *source-ip* to *dest-ip*

发送TRIP报文

·*packet-type*：TRIP报文类型，取值为request、response或acknowledgement

·*interface-type interface-number*：接口类型和编号，从该接口发送TRIP报文

·*source-ip*：接收TRIP报文的源IP地址

·*dest-ip*：TRIP报文的目的地址

Retransmitting *packet-type* on interface *interface-type interface-number* from *source-ip* to *dest-ip*

重传TRIP报文

·*packet-type*：TRIP报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口重传TRIP报文

·*source-ip*：接收TRIP报文的源IP地址

·*dest-ip*：TRIP报文的目的地址

Packet : vers *packet-version*, cmd *cmd-value*, length *length*, sequence num *sequence-num*

TRIP报文头信息

·*packet-version*：TRIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为response、response (FLUSH)、acknowledgement或acknowledgement (FLUSH)

·*length*：报文长度

·*sequence-num*：TRIP报文的序列号

Packet : vers *packet-version*, cmd *cmd-value*, length *length*

TRIP报文头信息

·*packet-version*：TRIP报文的版本，取值为1或2

·*cmd-value*：报文的类型，取值为request

·*length*：报文长度

【举例】

\# Router A通过接口GigabitEthernet1/0/1与Router B相连，分别在Router A和Router B上配置RIP，在Router A上打开指定接口的RIP发送报文调试信息开关。

\<RouterA\> debugging rip 1 send interface gigabitethernet 1/0/1

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Sending response on interface GigabitEthernet1/0/1 from 40.0.0.2 to 224.0.0.9

*[// RIP*]*进程1从接口GigabitEthernet1/0/1发送应答报文，源地址40.0.0.2，目的地址224.0.0.9*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:   Packet : version 2, cmd response, length 64

*// 应答报文版本2，长度64字节*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.2/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第一个路由项AFI字段值为2，目的网段地址为50.0.0.2/255.255.255.255，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 50.0.0.0/255.0.0.0, nexthop 0.0.0.0, cost 1, tag 0

*// 第二个路由项AFI字段值为2，目的网段地址为50.0.0.0/255.0.0.0，下一跳为0.0.0.0，度量值为1，路由标签为0*

\*Nov 24 15:57:46:32 2010 RouterA RIP/7/RIPDEBUG:     AFI 2, destination 110.0.0.1/255.255.255.255, nexthop 0.0.0.0, cost 1, tag 0

*// 第三个路由项AFI字段值为2，目的网段地址为110.0.0.1/255.255.255.255，下一跳为0.0.0.0，度量值为1，路由标签为0*

**RIP \-- RIP调试命令 \-- debugging rip timer**

------------------------------------------------------------------------

【命令】

**[debugging** **rip** *process-id* **timer**]

**[undo** **debugging** **rip** *process-id* **timer**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

【描述】

**[debugging rip timer**]命令用来打开RIP定时器调试信息开关。**undo debugging rip timer**命令用来关闭RIP定时器调试信息开关。

缺省情况下，RIP定时器调试信息开关处于关闭状态。

表1-6 debugging rip timer命令输出信息描述表

字段

描述

RIP *process-id*

RIP进程号

Update timer expired

定时更新定时器超时

【举例】

\# 在一台启动了RIP功能的设备上打开RIP进程1的定时器调试信息开关。

\<RouterA\> debugging rip 1 timer

\*Oct 23 14:21:01:382 2010 RouterA RIP/7/RIPDEBUG: RIP 1 : Update timer expired

*[// RIP*]*进程1的定时更新定时器超时*
