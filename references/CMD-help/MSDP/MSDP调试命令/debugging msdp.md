<!-- CMD-INDEX
  debugging msdp                      | 用户视图             | L5
-->

**MSDP \-- MSDP调试命令 \-- debugging msdp**

------------------------------------------------------------------------

【命令】

**[debugging** **msdp** [ **vpn-instance** *vpn-instance-name*  { **all** \| **connect** \| **event** \| **packet** \| **source-active** }]]

**[undo** **debugging** **msdp** [ **vpn-instance** *vpn-instance-name*  { **all** \| **connect** \| **event** \| **packet** \| **source-active** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

**[all**]：表示MSDP所有调试信息开关。

**[connect**]：表示MSDP对等体连接调试信息开关。

**[event**]：表示MSDP事件调试信息开关。

**[packet**]：表示MSDP报文调试信息开关。

**[source-active**]：表示MSDP活跃组播源调试信息开关。

【描述】

**[debugging msdp**]命令用来打开MSDP调试信息开关。**undo debugging msdp**命令用来关闭MSDP调试信息开关。

缺省情况下，MSDP调试信息开关处于关闭状态。

表1-1 debugging msdp connect命令输出信息描述表

字段

描述

Failed to modify epoll for peer *peer* connect, close the socket.

更改对等体*peer*连接的epoll失败，关闭socket

Connected to peer *peer* successfully.

连接对等体*peer*成功

Accepted connection request from peer *peer*.

接受对等体*peer*的连接成功

Failed to accept connection request from peer *peer*.

接受对等体*peer*的连接失败

Stopped listening for connection request from peer *peer*.

停止侦听对等体*peer*的连接请求

Failed to listen for connection request from peer *peer*.

侦听对等体*peer*的连接请求失败

Stopped connection with peer *peer*.

关闭与对等体*peer*的连接

Failed to connect to peer *peer* (errcode: *errcode*).

连接对等体*peer*失败（错误码为*errcode*）

Started a session with peer *peer*.

开始与对等体*peer*的会话

Reset connection with peer *peer*.

重置与对等体*peer*的连接

Peer *peer* state changed from *state1* to *state2*.

对等体*peer*的状态由*state1*切换到*state2*，状态包括：

·DISABLED

·CONNECTING

·LISTEN

·ESTABLISHED

表1-2 debugging msdp event命令输出信息描述表

字段

描述

Created *timer* timer for peer *peer*.

为对等体*peer*创建*timer*定时器，*timer*包括：

·ConnectRetry：重连

·session reconnection：会话重连

·SA-Reponse：SA回应

Created *timer* timer.

创建*timer*定时器，*timer*包括：

·memory threshold recover：内存门限恢复

·smooth end：平滑结束

·smooth：平滑

·resend：重发

·reconnect to MRIB：重连MRIB

Failed to create *timer* timer for peer *peer*.

为对等体*peer*创建*timer*定时器失败，*timer*包括：

·ConnectRetry：重连

·session reconnection：会话重连

·SA-Reponse：SA回应

·SA batch advertisement：SA批量通告

Failed to create *timer* timer.

创建*timer*定时器失败，*timer*包括：

·SA advertisement：SA通告

·interface reconnection：接口重连

·SA batch advertisement：SA批量通告

·memory threshold recover：内存门限恢复

·smooth end：平滑结束

·smooth：平滑

·resend：重发

·reconnect to MRIB：MRIB重连

Deleted *timer* timer for peer *peer*.

为对等体*peer*删除*timer*定时器，*timer*包括：

·ConnectRetry：重连

·Keepalive：保活

·Hold：保持

·session reconnection：会话重连

·SA-Reponse：SA回应

·SA batch advertisement：SA批量通告

Deleted *timer* timer.

删除*timer*定时器，*timer*包括：

·smooth end：平滑结束

·smooth：平滑

Peer *peer*'s *timer* timer expired.

对等体*peer*的*timer*定时器超时，*timer*包括：

·ConnectRetry：重连

·Keepalive：保活

·Hold：保持

·session reconnection：会话重连

·SA-Response：SA回应

*[Timer* timer expired.]

*[Timer*]定时器超时，*Timer*包括：

·Memory threshold recover：内存门限恢复

·Smooth end：平滑结束

·Smooth：平滑

Failed to set/reset password for peer *peer*.

为对等体*peer*设置/清除密码失败

Failed to recover original-rp/peer configuration for interface *name* from DBM.

为接口*name*从DBM恢复original-rp/peer的配置失败

Failed to cache (*source*, *group*).

缓存（*source*，*group*）失败

Failed to save original-rp/peer/global/static-rpf-peer configuration to DBM.

将original-rp/peer/global/static-rpf-peer的配置保存到DBM失败

Failed to process HA upgrade event.

处理HA的升级事件失败

Failed to recover cofiguration from DBM.

从DBM恢复配置失败

Failed to enable redirecting TCP packets to CPU.

使能TCP报文上报CPU失败

Failed to notify main thread to processing multicast enable/disable message.

通知主线程处理组播使能/关闭消息失败

Failed to notify main thread to processing message.

通知主线程处理报文失败

Failed to connect to MRIB.

连接MRIB失败

Failed to resend message to MRIB.

向MRIB重发消息失败

Failed to read message from socket (errcode: *errcode*).

从socket读取数据失败（错误码为*errcode*）

Failed to set fd limit(errno: *errcode*).

设置进程FD上限失败（错误码为errcode）

Failed to notify work thread to originate SA adv message.

通知工作线程生成SA通告消息失败

Failed to notify work thread to processing exit message.

通知工作线程处理退出的消息失败

Refreshed *timer* timer of peer *peer* to *n* seconds.

刷新对等体*peer*的*timer*定时器为*n*秒，*timer*包括：

·Keepalive：保活

·Hold：保持

Refreshed SA cache timer of (*source*, *group*) to *n* seconds.

刷新SA缓冲（*source*，*group*）的缓冲定时器为*n*秒

Received HA *event* event.

收到HA的*event*事件，*event*包括：

·stop：停止

·upgrade：升级

·degrade：降级

Received socket *n* *event* event.

收到socket *n*的*event*事件，*event*包括：

·ERROR/HUP

·IN

·OUT

Received *event* from MRIB.

从MRIB收到*event*事件，*event*包括：

·smooth start：平滑开始

·connection up：连接up

·connection down：连接down

·enable-multicast notification：组播使能通知

·disable-multicast notification：组播关闭通知

Received address event *event* on interface *name*.

收到接口*name*的地址事件*event*，*event*包括：

·add

·delete

Received *event* event on interface *name*.

收到接口*name*的*event*事件，*event*包括：

·add：添加

·delete：删除

·unbind：去绑定VPN

·insert：插入

·extract：拔出

·UP to DOWN

·DOWN to UP

Received local source (*source*, *group*) add event with *n* bytes data.

收到本地源（*source*, *group*）添加事件，同时带有*n字节的组播数据*

Droped local source (*source*, *group*) data for exceed max data length *n.*

由于携带数据的长度超过了最大数据长度*n*，将本地源（*source*, *group*）的数据丢弃

Droped local source (*source*, *group*) for exceed work thread queue limit.

由于超过了工作线程队列长度的限制，将本地源（*source*, *group*）丢弃

Left *n* bytes message to resend.

剩余*n*字节的消息需要重发

Left *n* bytes message to drop from socket.

需要从socket丢弃*n*字节的消息

Processed HA stop event successfully.

处理HA的停止事件成功

Tried to enable/disable peer *peer*.

尝试使能/关闭对等体*peer*

Shutdown peer *peer*.

手工shutdown对等体*peer*

Read *n* bytes message from socket.

从socket读取*n*字节的数据

Connection has been closed, restart peer connection.

连接已经关闭，重新启动对等体的连接

Can\'t forward (*source*, *group*) entry because the same entry had been forwarded within 30 seconds.

不能转发（*source*, *group*）表项，因为30秒内转发过相同的表项

Failed to connect to MBGP, creating reconnection timer

连接MBGP失败，创建重连定时器

Failed to create reconnection timer for MBGP

创建重连MBGP定时器失败

Startup reconnect to MBGP timer

启动重连MBGP定时器

Failed to startup reconnection to MBGP timer

启动重连MBGP定时器失败

Stop reconnect to MBGP timer

停止重连MBGP定时器

Reconnect to MBGP timer expired

重连MBGP定时器超时

Startup age MBGP timer

启动老化MBGP数据定时器

Stop age MBGP timer

停止老化MBGP数据定时器

Age MBGP timer expired

老化MBGP数据定时器超时

Receive connection close from MBGP

收到MBGP通知的连接关闭消息

Register to MBGP error: *errcode*

向MBGP注册失败（错误码为*errcode*）

表1-3 debugging msdp packet命令输出信息描述表

字段

描述

Received SA/SA-Response message from peer *peer* can\'t pass import.

从对等体*peer*收到的SA/SA-Response不能通过入策略

Received (*source*, *group*) from peer *peer* can\'t pass import ACL.

从对等体*peer*收到的SA/SA-Response报文中的（*source*，*group*）不能通过入方向的ACL

Received group *group* from peer *peer* is in SSM range.

从对等体*peer*收到的SA/SA-Response中包含的组地址*group*在SSM范围

Received SA/SA-Response message from peer *peer* with illegal RP(0.0.0.0).

从对等体*peer*收到的SA/SA-Response报文中的RP是非法的0.0.0.0地址

Received SA/SA-Response message from peer *peer* with local RP.

从对等体*peer*收到的SA/SA-Response报文中的RP是本地的RP

Received SA-Request packet from peer *peer* can\'t pass request policy.

从对等体*peer*收到的SA请求报文不能通过请求策略

Received SA/SA-Response message from peer *peer* with illegal RP/source/group address (*address*).

从对等体*peer*收到的SA/SA-Response报文的RP地址/源地址/组地址*address*非法

Received SA/SA-Response message from peer *peer* with illegal mask length (*length*).

从对等体*peer*收到的SA/SA-Response报文的地址掩码长度*length*非法

Received *message* message from peer *peer* with illegal length (*length*).

从对等体*peer*收到的*message*报文的长度*length*非法，*message*包括：

·SA：SA报文

·SA-Request：SA-Request报文

·SA-Response：SA-Response报文

·Keepalive：保活报文

·Notification：通告报文

·Traceroute in progress：路由回溯请求报文

·Traceroute reply：路由回溯回应报文

·Unknown：未知类型报文

Received SA/SA-Response message from peer *peer* with illegal entry count (*count*).

从对等体*peer*收到的SA/SA-Response报文的表项数量*count*非法

Received SA message from peer *peer* with illegal data.

从对等体*peer*收到的SA报文的数据非法

Received SA-Request message packet from peer *peer* for group *group*.

从对等体*peer*收到组*group*的SA请求报文

Received SA-Request message from peer *peer* for group *group* can\'t pass request policy.

从对等体*peer*收到组*group*的SA请求报文不能通过请求策略

Received *message* message from peer *peer*.

从对等体*peer*收到*message*报文，*message*包括：

·Notification(openbit: *openbit*, errcode: *errcode*, suberrcode: *suberrcode*)：通告报文（openbit为*openbit*/错误码为*errcode*/子错误码为*suberrcode*）

·unknown(*code*)：未知类型（类型码为*code*）

·traceroute in progress：路由回溯请求

·traceroute reply：路由回溯回应

·Keepalive：保活

Sent SA message to peer *peer*, can\'t pass export policy.

发送的SA报文不能通过出策略

Sent SA message to peer *peer*, (*source*, *group*) can\'t pass export policy.

发送的SA报文中的（*source*，*group*）不能通过出策略

Sent SA-Request message to peer *peer* for group *group*.

向对等体*peer*发送组*group*的SA请求报文

Sent Keepalive message to peer *peer*.

向对等体*peer*发送保活报文

Sent Notification(openbit: *openbit*, errcode: *errcode*, suberrcode: *suberrcode*) message to peer *peer.*

向对等体*peer*发送通告报文（openbit为*openbit*，错误码为*errcode*，子错误码为*suberrcode*）

Sent *n* bytes SA message to peer *peer*.

向对等体*peer*发送*n*字节的报文

Discarded SA message send to peer *peer* due to TTL *n* less than min-TTL *m*.

向对等体*peer*发送的SA报文由于TTL值*n*小于TTL下限值*m*而被丢弃

表1-4 debugging msdp source-active命令输出信息描述表

字段

描述

RPF check on received SA message from peer *peer* failed.

从对等体*peer*收到的SA报文RPF检查失败

Received SA message from peer *peer* with *n* bytes data (RP: *rp*, len: *length*, count: *count*).

从对等体*peer*收到携带*n*字节数据的SA报文（RP的地址为*rp*，长度为*length*，数量为*count*）

Received SA-Response message from peer *peer* (RP: *rp*, len: *length*, count: *count*).

从对等体*peer*收到SA-Response报文（RP的地址为*rp*，长度为*length*，数量为*count*）

RPF check passed for *rp* (*reason*)

RP地址为*rp*的SA报文的RPF检查通过，原因为*reason*，*reason*包括：

·Peer is the only established peer：收到报文的对等体是唯一处于Established状态的对等体

·Peer is in the mesh-group：收到报文的对等体属于全连接组

·Peer is the RP：收到报文的对等体就是RP

·Peer is MBGP nexthop：收到报文的对等体是MBGP路由的下一跳

·Peer is BGP nexthop：收到报文的对等体是BGP路由的下一跳

·Peer is IGP nexthop：收到报文的对等体是IGP路由的下一跳

·Peer with the highest IP address in AS：收到报文的对等体是AS中IP地址最大的对等体

·Peer is a static RPF-peer：收到报文的对等体是静态RPF对等体

RPF check failed for *rp* (*reason*: *rpf-peer*)

RP地址为*rp*的SA报文的RPF检查不通过，原因为*reason*（所包含内容同上），RPF对等体的地址为*rpf-peer*

RPF check failed for *rp*

RP地址为*rp*的SA报文的RPF检查不通过，且不存在任何RPF对等体

【举例】

\# 使能MSDP，并打开公网实例MSDP对等体连接调试信息开关。

\<Sysname\> debugging msdp connect

\*Dec  5 05:49:28:081 2012 Sysname MSDP/7/CONNECT: -MDC=1; Peer 10.1.1.1 state changed from DISABLED to LISTEN

*// 对等体10.1.1.1的状态由DISABLED迁移到LISTEN*

\*Dec  5 05:50:16:343 2012 Sysname MSDP/7/CONNECT: -MDC=1; Accepted connection request from peer 10.1.1.1

*// 接受对等体10.1.1.1的连接成功*

\*Dec  5 05:50:16:343 2012 Sysname MSDP/7/CONNECT: -MDC=1; Stopped listening for connection request from peer 10.1.1.1

*// 停止侦听对等体10.1.1.1的连接请求*

\*Dec  5 05:50:16:343 2012 Sysname MSDP/7/CONNECT: -MDC=1; Peer 10.1.1.1 state changed from LISTEN to ESTABLISHED

*// 对等体10.1.1.1的状态由LISTEN迁移到ESTABLISHED*

\# 使能MSDP，并打开公网实例MSDP事件调试信息开关。

\<Sysname\> debugging msdp event

\*Dec 5 05:55:15:888 2012 Sysname MSDP/7/EVENT: -MDC=1; Received socket 72 IN event

*// 收到socket 72的IN报文事件*

\*Dec 5 05:55:15:888 2012 Sysname MSDP/7/EVENT: -MDC=1; Read 3 bytes message from socket

*// 从socket读取3节的数据*

\*Dec 5 05:55:15:890 2012 Sysname MSDP/7/EVENT: -MDC=1; Refreshed Hold timer of peer 10.1.1.1 to 75 seconds

*// 刷新对等体10.1.1.1的Hold定时器为75秒*

\# 使能MSDP，并打开公网实例MSDP报文调试信息开关。

\<Sysname\> debugging msdp packet

\*Dec 5 05:58:15:645 2012 Sysname MSDP/7/PACKET: -MDC=1; Received Keepalive message from peer 10.1.1.1

*// 从对等体10.1.1.1收到Keepalive报文*

\*Dec 5 05:58:16:295 2012 Sysname MSDP/7/PACKET: -MDC=1; Sent Keepalive message to peer 10.1.1.1

*// 向对等体10.1.1.1发送Keepalive报文*

\# 在设备上使能MSDP，并打开公网实例MSDP活跃组播源调试信息开关。

\<Sysname\> debugging msdp source-active

\*Dec 5 06:05:13:680 2012 Sysname MSDP/7/SOURCE-ACTIVE: -MDC=1; Received SA message from peer 10.1.1.1 with 52 bytes data(RP: 1.1.1.1, len: 72, count: 1)

*// 从对等体10.1.1.1收到一个包含52字节数据的SA报文，RP地址为1.1.1.1，长度为72，报文中包含一个（S，G）的组播源信息*

\*Dec 5 06:05:14:684 2012 Sysname MSDP/7/SOURCE-ACTIVE: -MDC=1; RPF check passed for 1.1.1.1 (Peer is the only established peer)

*// 从对等体10.1.1.1收到的SA报文通过RPF检查，该对等体是唯一处于Established状态的对等体*
