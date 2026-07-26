
**LDP \-- LDP调试命令 \-- debugging mpls ldp**

------------------------------------------------------------------------

【命令】

**[debugging mpls ldp **[{ **all** \| **error** \| **event** \| **process** [ { **ipv4** \| **ipv6** } [ **prefix-list** *prefix-list-name* ] ] \| **socket** \| **timer** }]]

**[undo debugging mpls ldp **[{ **all** \| **error** \| **event** \| **process** ** **[ { **ipv4** \| **ipv6** } \| **socket** \| **timer** } ] }]]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[all**]：表示LDP的所有调试信息开关。

**[error**]：表示LDP的错误调试信息开关。

**[event**]：表示LDP的事件调试信息开关。

**[process**]：表示LDP创建LSP过程调试信息开关。如果指定参数**ipv4，**则表示创建IPv4 LSP的过程调试信息开关；如果指定参数**ipv6，**则表示创建IPv6 LSP的过程调试信息开关；如果不指定**ipv4**和**ipv6**参数，则打开所有FEC对应的LSP维护过程调试信息开关。

**[prefix-list ***prefix-list-name*]：指定通过IP地址前缀列表对调试信息进行过滤。只有FEC目的地址通过IP地址前缀列表过滤时，才会打开该FEC对应LSP建立过程的调试信息开关。*prefix-list-name*表示IP地址前缀列表名，为1～63个字符的字符串，区分大小写。

**[socket**]：表示LDP套接字调试信息开关。

**[timer**]：表示LDP定时器调试信息开关。

【描述】

**[debugging mpls ldp**]命令用来打开LDP的调试信息开关。**undo debugging mpls ldp**命令用来关闭LDP的调试信息开关。

缺省情况下，LDP调试信息开关处于关闭状态。

表1-1 debugging mpls ldp error命令输出信息描述表

字段

描述

Failed to process a configuration command.

处理配置命令失败

Failed to create the timer.

创建定时器失败

Failed to reset the timer.

重设定时器失败

Unsupported label type.

不支持的标签类型

Unsupported address family.

不支持的地址协议族

Failed to allocate a label for *destination*.

为目的地址为*destination*的FEC分配标签失败

Failed to create a TCP socket.

在LDP会话的被动方上创建TCP套接字失败

Failed to create a UDP socket.

创建UDP套接字失败

表1-2 debugging mpls ldp event命令输出信息描述表

字段

描述

*[Module-A* created a connection to *Module-B*.]

*[Module-A*]模块与*Module-B*模块建立一个连接

Received an HA upgrade event.

收到HA升级事件

Received an HA degrade event.

收到HA降级事件

Received the interface *event* event. Interface index: *index*.

收到接口变化事件，事件为*event*，接口的索引为*index*

表1-3 debugging mpls ldp process命令输出信息描述表

字段

描述

Refreshed the LSP (*lsp-destination*) to LSM.

向LSM下发一条LSP，LSP的目的地址为*lsp-destination*

Added an LSP establishment triggering policy on the egress (VPN instance: *vpn-name*).

在Egress上添加一个VPN实例名称为*vpn-name*的LSP触发策略。

如果不显示VPN实例名称，则表示公网。下文与此相同，不再赘述

Notified LSM to delete the LSP (*lsp-destination*).

通知LSM删除一条LSP，LSP的目的地址为*lsp-destination*

Process the label distribution control mode change event. VPN instance: *vpn-name*.

处理标签分发控制方式改变事件，VPN实例名称为*vpn-name*

表1-4 debugging mpls ldp socket命令输出信息描述表

字段

描述

Accepted a new socket (*socket-id*).

接收一个新的套接字，套接字的ID为*socket-id*

Created a new socket (*socket-id*) on the passive LSR.

在LDP会话的被动方上创建一个新的套接字，套接字的ID为*socket-id*

Closed the socket (*socket-id*) on the passive LSR.

在LDP会话的被动方上关闭套接字，套接字的ID为*socket-id*

Created a new socket (*socket-id*) on the active LSR.

在LDP会话的主动方上创建一个新的套接字，套接字的ID为*socket-id*

Closed the socket (*socket-id*) on the active LSR.

在LDP会话的主动方上关闭套接字，套接字的ID为*socket-id*

Created a new UDP socket (*socket-id*).

创建一个新的UDP套接字，套接字的ID为*socket-id*

表1-5 debugging mpls ldp timer命令输出信息描述表

字段

描述

Created the *timer-type* timer (size: *timer-size*).

创建一个类型为*timer-type*的定时器，定时器的值为*timer-size*

Reset the *timer-type* timer (size: *timer-size*).

重置类型为*timer-type*的定时器，定时器的值为*timer-size*

Deleted the *timer-type* timer.

删除类型为*timer-type*的定时器

*[timer-type*] timer expired.

类型为*timer-type*的定时器超时

【举例】

\# 打开LDP的错误调试信息开关。配置一个不存在对应VPN实例的LDP实例，打印如下信息。

\<Sysname\> debugging mpls ldp error

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp vpn-instance vpn1

Sysname-ldp

\*Mar 14 17:20:25:520 2011 Sysname LDP/7/ERROR: -MDC=1; Failed to process a configuration command.

*// 处理配置命令失败。*

\# 打开LDP的事件调试信息开关。将一个使能了MPLS LDP能力的接口shutdown，打印如下信息。

\<Sysname\> debugging mpls ldp event

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 shutdown

Sysname-GigabitEthernet1/0/1

\*Jun 23 15:54:30:088 2011 Sysname LDP/7/EVENT: -MDC=1; Received the interface down event. Interface index: 66794.

*// 收到接口down事件。*

\# 打开LDP的套接字调试信息开关。配置MPLS LDP实例，打印如下信息。

\<Sysname\> debugging mpls ldp socket

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp vpn-instance vpn2

Sysname-ldp

\*Mar 14 19:07:21:584 2011 Sysname LDP/7/SOCKET: -MDC=1; Created a new socket (32) on the active LSR.

\*Mar 14 19:07:21:584 2011 Sysname LDP/7/SOCKET: -MDC=1; Created a new UDP socket (33).

*// 在LDP会话的主动方上创建TCP服务套接字，创建UDP套接字。*

\# 打开LDP的定时器调试信息开关。在接口上使能MPLS LDP能力后，打印如下信息。

\<Sysname\> debugging mpls ldp timer

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls enable

Sysname-GigabitEthernet1/0/1 mpls ldp enable

\*Mar 14 18:49:45:839 2011 Sysname LDP/7/TIMER: -MDC=1; Created a hello interval timer (size: 5000).

\*Mar 14 18:49:45:842 2011 Sysname LDP/7/TIMER: -MDC=1; Created a hello hold timer (size: 15000).

*// 创建一个5000ms的hello interval定时器，创建一个15000ms的hello hold定时器。*

\# 打开LDP创建LSP过程调试信息开关。配置标签分发控制方式为独立方式后，打印如下信息。

\<Sysname\> debugging mpls ldp process

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp label-distribution independent

\*Mar 14 19:25:40:030 2011 Sysname LDP/7/PROCESS: -MDC=1; Process the label distribution control mode change event.

*// 处理标签分发控制方式改变事件。*

在Egress上配置一条掩码长度为32位的IPv4路由，在Ingress上打印如下信息。

\*Jan 6 18:25:09:172 2014 H3C LDP/7/PROCESS: -MDC=1; Refreshed the LSP (2.2.2.2/32) to LSM.

*// 向LSM下刷LSP（LSP对应的IPv4地址为2.2.2.2/32）。*

在Egress上配置一条掩码长度为128位的IPv6路由，在Ingress上打印如下信息。

\*Jan 6 18:28:41:768 2014 H3C LDP/7/PROCESS: -MDC=1; LSP refresh job (type: 8) for 200::22/128. 

*// 向LSM下刷LSP（LSP对应的IPv6地址为200::22/128）。*

**LDP \-- LDP调试命令 \-- debugging mpls ldp peer**

------------------------------------------------------------------------

【命令】

**[debugging mpls ldp **[{ **advertisement  **[ { **ipv4** \| **ipv6** } [ **prefix-list** *prefix-list-name* ] ] **\| discovery** [ **ipv4** \| **ipv6** ] \| **notification** \| **packet** { **received** \| **sent** } \| **session** }  **peer** *peer-prefix-list-name* ]]

**[undo debugging mpls ldp **[{ **advertisement** [ **ipv4** \| **ipv6** ] **\| discovery** [ **ipv4** \| **ipv6** ] \| **notification** \| **packet** { **received** \| **sent** } \| **session** }]]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[advertisement**]：表示LDP标签通告和地址通告调试信息开关。如果指定参数**ipv4，**则表示IPv4 LDP标签通告和地址通告调试信息开关；如果指定参数**ipv6，**则表示IPv6 LDP标签通告和地址通告调试信息开关；如果不指定**ipv4**和**ipv6**参数，则表示打开所有FEC的通告调试信息开关。

**[prefix-list ***prefix-list-name*]：指定通过IP地址前缀列表对调试信息进行过滤。只有FEC目的地址通过IP地址前缀列表过滤时，才会打开该FEC对应标签通告和地址通告的调试信息开关。*prefix-list-name*表示IP地址前缀列表名，为1～63个字符的字符串，区分大小写。

**[discovery**]：表示LDP发现过程调试信息开关。如果指定参数**ipv4，**则表示IPv4 LDP发现过程调试信息开关；如果指定参数**ipv6，**则表示IPv6 LDP发现过程调试信息开关；如果不指定**ipv4**和**ipv6**参数，则打开所有发现过程调试信息开关。

**[notification**]：表示LDP通知消息调试信息开关。

**[packet**]：表示除Hello消息以外其他所有LDP消息的调试信息开关。

**[received**]：表示LDP接收消息调试信息开关。

**[sent**]：表示LDP发送消息调试信息开关。

**[session**]：表示LDP会话调试信息开关。

**[peer ***peer-prefix-list-name*]：表示指定对等体的LDP调试信息开关。只有对等体通过IP地址前缀过滤时，才会打开该对等体相关的调试信息开关。*peer-prefix-list-name*表示IP地址前缀列表名，为1～63个字符的字符串，区分大小写。如果不指定本参数，则打开所有对等体相关的调试信息开关。

【描述】

**[debugging mpls ldp peer**]命令用来打开LDP对等体的调试信息开关。**undo debugging mpls ldp peer**命令用来关闭LDP对等体的调试信息开关。

缺省情况下，LDP对等体的调试信息开关处于关闭状态。

表1-6 debugging mpls ldp advertisement命令输出信息描述表

字段

描述

Loop detected by hop count (hop count: *hops*, max hop count: *max-hops*).

发现环路：LSP经过的跳数*hops*超过允许的最大跳数*max-hops*

Received a label mapping message from peer (*peer-ldp-id*, VPN instance: *vpn-name*).

从VPN实例*vpn-name*内的对端*peer-ldp-id*收到标签映射消息

The label mapping message from peer (*peer-ldp-id*: *space-id*) has *fec-destination/mask-length*, label (*label*)

来自对端*peer-ldp-id*的标签映射消息，FEC为*fec-destination，*掩码长度为*mask-length*，标签为*label*

表1-7 debugging mpls ldp discovery命令信息描述表

字段

描述

Created an adjacency (index *index*, source address *source-ip*, transport address *transport-ip*, destination address *destination-ip*) for peer (*peer-ldp-id*, VPN instance: *vpn-name*).

创建一个hello邻接体，邻接体索引为*index*，源IP地址为*source-ip*，传输地址为*transport-ip，*目的地址为*destination-ip*，对端LDP ID为*peer-ldp-id*，VPN实例名称为*vpn-name*

Deleted an adjacency (index *index*, source address *source-ip*, transport address *transport-ip*, destination address *destination-ip*) for peer (*peer-ldp-id*, VPN instance: *vpn-name*).

删除一个邻接体，邻接体索引为*index*，源IP地址为*source-ip*，传输地址为*transport-ip，*目的地址为*destination-ip*，对端LDP ID为*peer-ldp-id*，VPN实例名称为*vpn-name*

Discovered a new peer (*peer-ldp-id*, VPN instance: *vpn-name*).

在VPN实例*vpn-name*内发现一个LDP ID为*peer-ldp-id*的对端

The peer (*peer-ldp-id*, VPN instance: *vpn-name*) is lost.

与VPN实例*vpn-name*内LDP ID为*peer-ldp-id*的对端失去连接，删除该hello邻接体

表1-8 debugging mpls ldp notification命令描述表

字段

描述

Received a notification message (*event*) from peer (*peer-ldp-id*, VPN instance: *vpn-name*).

从VPN实例*vpn-name*内的对端*peer-ldp-id*收到Notification消息，通知的事件为*event*

Sent a notification message (*event*) to peer (*peer-ldp-id*, VPN instance: *vpn-name*).

向VPN实例*vpn-name*内的对端*peer-ldp-id*发送Notification消息，通知的事件为*event*

表1-9 debugging mpls ldp packet命令描述表

字段

描述

Received a keepalive message from peer (*peer-ldp-id*{.TableTextChar}, VPN instance: *vpn-name*).{.TableTextChar} message content: *content*

收到VPN实例*vpn-name*内的对端*peer-ldp-id*发送的Keepalive 消息，消息内容为*content*

Sent a keepalive message to peer (*[peer-ldp-id*]{.TableTextChar}, VPN instance: *vpn-name*). message content: *[content*]{.TableTextChar}

向VPN实例*vpn-name*内的对端*peer-ldp-id*发送Keepalive 消息，消息内容为*content*

表1-10 debugging mpls ldp session命令描述表

字段

描述

Stopped the socket (*socket-id*) to the peer (*peer-ldp-id*{.TableTextChar}, VPN instance: *vpn-name*). MD5 check is needed for the socket.

关闭到VPN实例*vpn-name*内的对端*[peer-ldp-id*]{.TableTextChar}的套接字，套接字的ID为*socket-id*，该套接字需要进行MD5检查

Started the socket (*socket-id*) to the peer (*peer-ldp-id*{.TableTextChar}, VPN instance: *vpn-name*). MD5 check is needed for the socket.

打开到VPN实例*vpn-name*内的对端*[peer-ldp-id*]{.TableTextChar}的套接字，套接字的ID为*socket-id*，该套接字需要进行MD5检查

Created a new session (*peer-ldp-id*, VPN instance: *vpn-name*). Local transport address: *local-address*, peer transport address: *peer-address*.

创建一个会话，对端LDP ID为*peer-ldp-id*，VPN实例名称为*vpn-name*，本端传输地址为*local-address*，对端传输地址为*peer-address*

Deleted the session (*peer-ldp-id*, VPN instance: *vpn-name*).

删除与VPN实例*vpn-name*内的对端*peer-ldp-id*的会话

MD5 check of the session (*peer-ldp-id*, VPN instance: *vpn-name*) failed.

与VPN实例*vpn-name*内的对端*peer-ldp-id*的会话进行MD5检查失败

【举例】

\# 打开LDP IPv4发现过程调试信息开关。在接口上使能MPLS LDP支持IPv4能力后，打印如下信息。

\<Sysname\> debugging mpls ldp discovery ipv4

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls enable

Sysname-GigabitEthernet1/0/1 mpls ldp enable

Sysname-GigabitEthernet1/0/1

\*Jan 6 14:26:32:105 2014 H3C LDP/7/DISCOVERY: -MDC=1; Created an adjacency (index 4, source address 77.99.99.99, transport address 99.99.3.3, destination address 224.0.0.2) for peer (99.99.3.3:0).

\*Jan 6 14:26:32:105 2014 H3C LDP/7/DISCOVERY: -MDC=1; Discovered a new peer (99.99.3.3:0).

*// 创建一个与对端99.99.3.3的Hello邻接体，邻接体的索引为4，源IP地址为77.99.99.99，传输地址为99.99.3.3，目的地址为224.0.0.2。*

\# 打开LDP IPv6发现过程调试信息开关。在接口上使能MPLS LDP支持Ipv6能力后，打印如下信息。

\<Sysname\> debugging mpls ldp discovery ipv6

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp quit

Sysname interface ethernet 1/1

Sysname-Ethernet1/1 mpls enable

Sysname-Ethernet1/1 mpls ldp ipv6 enable

Sysname-Ethernet1/1

\*Jan 6 16:02:15:092 2014 H3C LDP/7/DISCOVERY: -MDC=1; Created an adjacency (index 5, source address FE80::20C:29FF:FEB3:BC0A, transport address 2001::2, destination address FF02::2) for peer (99.99.3.3:0).

\*Jan 6 16:02:15:093 2014 H3C LDP/7/DISCOVERY: -MDC=1; Discovered a new peer (99.99.3.3:0).

*// 创建一个与对端99.99.3.3的Hello邻接体，邻接体的索引为5，源IP地址为FE80::20C:29FF:FEB3:BC0A，传输地址为2001::2，目的地址为FF02::2。*

\# 打开LDP标签通告和地址通告调试信息开关。

在Egress上配置LSP触发策略为所有路由项都会触发LDP建立LSP后，打印如下信息。

\<Sysname\> debugging mpls ldp advertisement ipv4

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp lsp-trigger all

\*Jan 6 16:59:12:910 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; Received a label mapping message from peer (99.99.3.3:0).

\*Jan 6 16:59:12:910 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; The label mapping message from peer (99.99.3.3:0) has 20.1.1.2/32, label (3).

*// 接收到对端99.99.3.3为IPv4前缀路由20.1.1.2发送的mapping消息*

在Egress上配置LSP触发策略为所有IPv6路由项触发LDP建立LSP后，在Ingress上打印如下信息:

\<Sysname\> debugging mpls ldp advertisement ipv6

\*Jan 6 17:22:19:937 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; Received a label mapping message from peer (99.99.3.3:0).

\*Jan 6 17:22:19:937 2014 H3C LDP/7/ADVERTISEMENT: -MDC=1; The label mapping message from peer (99.99.3.3:0) has 200::24/128, label (3).

*// 接收到对端99.99.3.3为IPv6前缀路由200::24发送的mapping消息*

\# 打开LDP通知消息调试信息开关。hello定时器超时如果仍未收到hello消息，则打印如下信息。

\<Sysname\> debugging mpls ldp notification

\<Sysname\>

\*Mar 16 09:56:21:076 2011 SysnameLDP/7/NOTIFICATION: -MDC=1; Sent a notification message (hold timer expired) to peer (100.100.100.6:0).

*// 发送hello hold定时器超时的notification消息。*

\# 打开LDP接收消息调试信息开关。收到keepalive消息后，打印如下信息。

\<Sysname\> debugging mpls ldp packet received

\<Sysname\>

\*Mar 16 10:02:32:030 2011 SysnameLDP/7/PACKET RECEIVE: -MDC=1; Received a keepalive message from peer 100.100.100.6:0. message content:

 02 01 00 04 00 00 0d 67

*// 收到keepalive消息*

\# 打开LDP发送消息调试信息开关。发送keepalive消息后，打印如下信息。

\<Sysname\> debugging mpls ldp packet sent

\<Sysname\>

\*Mar 16 10:06:01:976 2011 SysnameLDP/7/PACKET SEND: -MDC=1; Sent a keepalive message to peer 100.100.100.6:0. message content:

 02 01 00 04 00 00 00 ae

*// 发送keepalive消息*

\# 打开LDP会话调试信息开关。重启MPLS LDP会话后，打印如下信息。

\<Sysname\> debugging mpls ldp session

\<Sysname\> reset mpls ldp

\<Sysname\>

\*Mar 15 16:27:01:686 2011 Sysname LDP/7/SESSION: -MDC=1; Deleted the session (100.100.100.6:0).

*// 删除会话。*

\*Mar 15 16:27:03:997 2011 Sysname LDP/7/SESSION: -MDC=1; Created a new session (100.100.100.6:0): Local transport (100.100.100.66), peer transport (100.100.100.6).

*// 创建新会话。*

**LDP \-- LDP调试命令 \-- debugging isis mpls ldp sync**

------------------------------------------------------------------------

【命令】

**[debugging isis mpls ldp sync **[[ **event** \| **fsm** \| **query** ] ]]

**[undo debugging isis mpls ldp sync**[ [ **event** \| **fsm** \| **query** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：表示IS-IS进程收到的LDP-IGP同步事件调试信息开关。

**[fsm**]：表示IS-IS进程的LDP-IGP同步状态机调试开关。

**[query**]：表示IS-IS进程向LDP进程发送消息队列的调试信息开关。

【描述】

**[debugging isis mpls ldp sync**]命令用来打开LDP IS-IS同步调试信息开关。**undo debugging isis mpls ldp sync**命令用来关闭LDP IS-IS同步调试信息开关。

缺省情况下，LDP IS-IS同步调试信息开关处于关闭状态。

执行本命令时，如果没有指定任何参数，则表示所有LDP IS-IS同步调试信息开关。

表1-11 debugging isis mpls ldp sync event命令输出信息描述表

字段

描述

ISIS-LDP-SYNC

LDP IS-IS同步调试信息

Subscribe LDP global famous port successfully.

订阅LDP端口成功

Subscribe LDP global famous port failed.

订阅LDP端口失败

Unsubscribe LDP global famous port successfully.

注销LDP端口成功

LDP port state change to up.

LDP端口状态变为up

LDP port state change to down.

LDP端口状态变为down

IS-IS connect LDP daemon successfully.

ISIS与LDP进程连接成功

IS-IS disconnect from LDP daemon.

ISIS与LDP进程断开

Receive LDP if-state message: *interfaceName*, ifIndex: *ifIndex*, ldpstate: ldp*State*, vrfIndex: *vrfIndex*.

接收到LDP接口状态信息

·*interfaceName*,：接口名称

·*ifIndex*：接口索引

·*ldpState*：LDP状态

·*vrfIndex*：VPN实例索引

Receive LDP if-state message: ifIndex(inactive): *ifIndex*, ldpstate: ldp*State*, vrfIndex: *vrfIndex*.

接收到没有接口索引的LDP接口状态信息

Receive LDP push-finish message.

接收到LDP平滑结束消息

Receive LDP disable message.

接收到LDP去使能消息

Receive LDP unknown message.

接收到未知的LDP消息

Parse LDP message failed.

解析LDP信息失败

LDP waiting timer expired.

LDP等待时间超时

Create LDP waiting timer.

创建LDP等待定时器

Delete LDP waiting timer.

删除LDP等待定时器

LDP break the connection.

LDP断开连接

LDP send buffer is free.

LDP发送缓冲区为空

表1-12 debugging isis mpls ldp sync fsm命令输出信息描述表

字段

描述

ISIS-LDP-SYNC

LDP IS-IS同步调试信息

Circuit(*interfaceName*) received event(ldp*Event*), LDP_SYNC state changed from *ldpSyncState1* to *ldpSyncState2*.

接口*interfaceName*收到事件ldp*Event*后，触发LDP同步状态机变化，接口的LDP同步状态由*ldpSyncState1*变为*ldpSyncState2*

表1-13 debugging isis mpls ldp sync query命令输出信息描述表

字段

描述

ISIS-LDP-SYNC

LDP IS-IS同步调试信息

Send LDP *msgType* message *resultState*: *interfaceName*, ifIndex: *ifIndex*.

发送LDP信息

·*msgType**：*信息类型，取值为注册或注销

·*resultState*：结果状态，取值为成功或失败

·*interfaceName*：接口名称

·*ifIndex*：接口索引

Resend LDP *msgType* message *resultState*: *interfaceName*, ifIndex: *ifIndex*.

重新发送LDP信息

Send LDP smooth *msgType* message *resultState*.

发送LDP平滑信息

·*msgType*：信息类型，取值为平滑开始或结束

·*resultState*：结果状态，取值为成功或失败

Resend LDP smooth *msgType* message *resultState*.

重新发送LDP平滑信息

【举例】

\# 在设备上打开所有LDP IS-IS同步调试信息开关后，在设备上配置LDP IS-IS同步功能，设备上将打印如下调试信息。

\<Sysname\> debugging isis mpls ldp sync

\*Jun 25 14:15:57:736 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: Subscribe LDP global famous port successfully.

*// 订阅LDP全局端口成功。*

\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: LDP port state change to up.

*[// LDP*]*端口状态变为up。*

\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: IS-IS connect LDP daemon successfully.

*[// IS-IS*]*进程与LDP进程连接成功。*

\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: Send LDP smooth start message successfully.

*// 发送LDP平滑开始信息成功。*

\*Jun 25 14:15:57:737 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: Send LDP register message successfully: GigabitEthernet1/0/2, ifIndex: 3.

*// 发送LDP注册信息成功：接口为GigabitEthernet1/0/2，接口索引为3。*

\*Jun 25 14:15:57:738 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: Send LDP smooth end message successfully.

*// 发送LDP平滑结束信息成功。*

\*Jun 25 14:17:23:883 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: Receive LDP if-state message: GigabitEthernet1/0/2, ifIndex: 3, ldpstate: no-ldp, vrfIndex: 0.

*// 接收LDP接口状态信息：接口为GigabitEthernet1/0/2，接口索引为3，LDP状态为no-ldp，实例索引为0。*

\*Jun 25 14:17:23:883 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: Circuit(GigabitEthernet1/0/2) received event(IGP_LDP_IF_UP), LDP_SYNC state changed from INIT to SYNC_ACHIEVED.

*[// GigabitEthernet1/0/2*]*接口的LDP状态变为no-ldp触发LDP同步状态机变化，接口的LDP同步状态由INIT变为SYNC_ACHIEVED。*

\*Jun 25 14:17:23:884 2013 Sysname ISIS/7/ISISDBG: -MDC=1;

ISIS-LDP-SYNC: Receive LDP push-finish message.

*// 接收到LDP push-finish信息。*

**LDP \-- LDP调试命令 \-- debugging ospf mpls ldp sync**

------------------------------------------------------------------------

【命令】

**[debugging ospf mpls ldp sync **[[ **event** \| **fsm** \| **query** ] ]]

**[undo debugging ospf mpls ldp sync **[ [ **event** \| **fsm** \| **query** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[event**]：表示OSPF进程收到的LDP-IGP同步事件调试信息开关。

**[fsm**]：表示OSPF进程的LDP-IGP同步状态机调试开关。

**[query**]：表示OSPF进程向LDP进程发送消息队列的调试信息开关。

【描述】

**[debugging ospf mpls ldp sync**]命令用来打开LDP OSPF同步调试信息开关。**undo debugging ospf mpls ldp sync**命令用来关闭LDP OSPF同步调试信息开关。

缺省情况下， LDP OSPF同步调试信息开关处于关闭状态。

执行本命令时，如果没有指定任何参数，则表示所有LDP OSPF同步调试信息开关。

表1-14 debugging ospf mpls ldp sync event命令输出信息描述表

字段

描述

LDP waiting timer expired.

LDP等待定时器超时

Create LDP waiting timer.

创建LDP等待定时器

Delete LDP waiting timer.

删除LDP等待定时器

Receive LDP if-state message: *interfaceName*, ifIndex: *ifIndex*, ldpstate: *state*, vrfIndex: *vrfIndex*.

接收到LDP接口状态信息

·*interfaceName*：接口名称

·*ifIndex*：接口索引

·*state*：LDP状态

·*vrfIndex*：VPN实例索引

Receive LDP if-state message: ifIndex(inactive): *ifIndex*, ldpstate: *state*, vrfIndex: *vrfIndex*.

接收到没有接口索引的LDP接口状态信息

LDP send buffer is free.

LDP发送缓冲区为空

LDP break the connection.

LDP断开连接

Receive LDP state message.

接收到LDP状态信息

Receive LDP push-finish message.

接收到LDP平滑结束消息

Receive LDP disable message.

接收到LDP去使能消息

Receive LDP unknown message.

接收到未知的LDP消息

Parse LDP message failed.

解析LDP信息失败

OSPF connect LDP daemon successfully.

OSPF与LDP进程连接成功

OSPF disconnect from LDP daemon.

OSPF与LDP断开连接

LDP port state change to up.

LDP端口状态变为up

LDP port state change to down.

LDP端口状态变为down

Subscribe LDP global famous port successfully.

订阅LDP端口成功

Subscribe LDP global famous port failed.

订阅LDP端口失败

Unsubscribe LDP global famous port successfully.

注销LDP端口成功

表1-15 debugging ospf mpls ldp sync fsm命令输出信息描述表

字段

描述

Circuit(*interfaceName*) received event(ldp*Event*), LDP_SYNC state changed from *ldpSyncState1* to *ldpSyncState2*.

接口*interfaceName*收到事件ldp*Event*后，触发LDP同步状态机变化，接口的LDP同步状态由*ldpSyncState1*变为*ldpSyncState2*

表1-16 debugging ospf mpls ldp query命令输出信息描述表

字段

描述

Send LDP *msgType* message *resultState*: *interfaceName*, ifIndex: *ifIndex*.

发送LDP信息

·*msgType*：信息类型，取值为注册或注销

·*resultState*：结果状态，取值为成功或失败

·*interfaceName*：接口名称

·*ifIndex*：接口索引

Resend LDP *msgType* message *resultState*: *circuitName*, ifIndex: *ifIndex*.

重新发送LDP信息

Send LDP smooth *msgType resultState*.

发送LDP平滑信息

·*msgType*：信息类型，取值为平滑开始或结束

·*resultState*：结果状态，取值为成功或失败

Resend LDP smooth *msgType resultState*.

重新发送LDP平滑信息

【举例】

\# 在设备上打开所有LDP OSPF同步调试信息开关后，在设备上配置LDP OSPF同步功能，设备上将打印如下调试信息。

\<Sysname\> debugging ospf mpls ldp sync

\*Jun 25 16:34:47:352 2013 Sysname OSPF/7/DEBUG: -MDC=1; Subscribe LDP global famous port successfully.

*// 订阅LDP全局端口成功。*

\*Jun 25 16:34:47:353 2013 Sysname OSPF/7/DEBUG: -MDC=1; LDP port state change to up.

*[// LDP*]*端口状态变为up。*

\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; OSPF connect LDP daemon successfully.

*[// OSPF*]*进程与LDP进程连接成功。*

\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; Send LDP smooth start message successfully.

*// 发送LDP平滑开始信息成功。*

\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; Send LDP register message successfully: GigabitEthernet1/0/2, ifIndex: 3.

*// 发送LDP注册信息成功：接口为GigabitEthernet1/0/2，接口索引为3。*

\*Jun 25 16:34:47:354 2013 Sysname OSPF/7/DEBUG: -MDC=1; Send LDP smooth end message successfully.

*// 发送LDP平滑结束信息成功。*

\*Jun 25 16:36:13:707 2013 Sysname OSPF/7/DEBUG: -MDC=1; Receive LDP state message.

*// 接收LDP状态信息。*

\*Jun 25 16:36:13:707 2013 Sysname OSPF/7/DEBUG: -MDC=1; Receive LDP push-finish message.

*// 接收LDP push-finish信息。*

\*Jun 25 16:36:13:707 2013 Sysname OSPF/7/DEBUG: -MDC=1; Receive LDP if-state message: GigabitEthernet1/0/2, ifIndex: 3, ldpstate: no-ldp, vrfIndex: 0.

*// 接收LDP接口状态信息：接口为GigabitEthernet1/0/2，接口索引为3，LDP状态为no-ldp，实例索引为0。*

\*Jun 25 16:36:43:508 2013 Sysname OSPF/7/DEBUG: -MDC=1; Circuit(GigabitEthernet1/0/2) received event(IGP_LDP_IF_UP), LDP_SYNC state changed from INIT to SYNC_ACHIEVED.

*[// GigabitEthernet1/0/2*]*接口接收到IGP_LDP_NO_LDP事件触发LDP同步状态机裱花，接口的LDP同步状态由INIT变为SYNC_ACHIEVED*。

