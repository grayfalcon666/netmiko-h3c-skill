
**域名解析 \-- 域名解析调试命令 \-- debugging dns**

------------------------------------------------------------------------

【命令】

**[debugging dns**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging dns**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DNS服务器的所有调试信息开关。

**[error**]：表示DNS服务器的错误调试信息开关。

**[event**]：表示DNS服务器的事件调试信息开关。

**[packet**]：表示DNS服务器的报文调试信息开关。

【描述】

**[debugging dns**]命令用来打开DNS服务器调试信息开关。

**[undo debugging dns**]命令用来关闭DNS服务器调试信息开关。

缺省情况下，DNS服务器的调试信息开关处于关闭状态。

表1-1 debugging dns packet命令输出信息描述表

字段

描述

Header:

 ID = *id*, QR = *qr*, OpCode = *opcode*, AA = *aa*, TC = *tc*, RD = *rd*

 RA = *ra*, Z = *zero*, AD = *ad*, CD = *cd*, RCode = *rcode*

QDCount = *qdcount*

ANCount = *ancount*

NSCount = *nscount*

ARCount = *arcount*

DNS报文头部分的内容：

标识字段为*id*，报文类型字段为*qr*，OpCode为*opcode*，授权回答字段 为*aa*，可截断字段为*tc*，期望递归字段为*rd*，可用递归字段为*ra*，Z为*zero*，可信数据字段为*ad*，校验字段为*cd*，返回码字段为*rcode*，问题数为*qdcount*，资源记录数为 *ancount*，授权资源记录数为*nscount*， 额外资源记录数为*arcount*

Question:

 QName = *host-name*

 QType = *query-type* (*type-number)*

 QClass = *class* (*class-number*)

DNS报文问题部分的内容：

查询名为*host-name*，查询类型为*query-type*，类型编号为*type-number*，查询类为*class*，查询类编号为*class-number*

Answer:

 Name = *host-name*

 Type = *query-type* (*type-number*)

 Class = *class* (*class-number*)

 TTL = *ttl*

 RDLength = *data-length*

 RData = *data*

DNS报文资源记录部分的内容：

主机名为*host-name*，查询类型为*query-type*，类型编号为*type-number*，查询类为*class*，查询类编号为*class-number*，生存时间 为*ttl*，资源数据长度为*data-length*，资源数据为*data*

表1-2 debugging dns event命令输出信息描述表

字段

描述

Successfully resolved *query-name*: host name is *host-name*, address is *ip-address*

解析DNS请求*query-name*成功，其主机名是*host-name*，IP地址是*ip-address*

Failed to resolve *query-name*

解析DNS请求*query-name*失败

Invalid host name *host-name*,

主机名*host-name*无效

Resolving *query-name* is in process; waiting for result

正在向服务器解析DNS请求*query-name*，等待获取查询结果

Too many resolving operations are in process.

正在处理的域名解析过多

Starting AAAA resolving for *host-name*

开始对主机名*host-name*.进行AAAA解析

Starting A resolving for *host-name*

开始对主机名*host-name*.进行A解析

Starting PTR resolving for *ip-address*

开始对地址为*ip-address*.进行PTR解析

Trying to resolve the host name for address *ip-address* in local database

从本地数据库解析地址为*ip-address*的主机的域名

Trying to resolve *host-name* in local database

从本地数据库解析*host-name*

Trying to resolve *host-name* in dynamic cache

从动态缓存解析*host-name*

No DNS server is found.

没有配置DNS服务器

Trying to resolve *host-name* by contacting DNS server *ip-address* through UDP

以UDP方式向DNS服务器*ip-address*解析主机*host-name*

Trying to resolve *host-name* by contacting DNS server *ip-address* through TCP

以TCP方式向DNS服务器*ip-address*解析主机*host-name*

Connecting to server *ip-address*

正在连接服务器*ip-address*

Connected to server *ip-address*

已连接到服务器*ip-address*

Failed to connect to server *ip-address*

连接服务器*ip-address*失败

Failed to send packets to server *ip-address*

发送数据给服务器*ip-address*失败

Waiting *time-value* seconds for server response

在*time-value*秒时间内等待服务器应答

Resolving *query-name* through DNS server *ip-address* timed out.

向服务器*ip-address*解析DNS请求*query-name*超时

Received an answer: QName = *query-name*,, ID = *transaction-id*

收到一个应答，DNS请求为*query-name*，ID号为t*ransaction-id*

Expect QName = *query-name*, ID = *transaction-id.* The received request is not as expected. Discarded it.

期望收到的DNS请求为*query-name*，ID号为t*ransaction-id*，（接收到的与期望的不符）丢弃

Resolving *query-name* is canceled.

解析DNS请求*query-name*被取消

Invalid packet; discarded it.

无效报文，丢弃

The answer is invalid.

无效的回答

Added a dynamic DNS entry *host-name*

添加一个主机名为*host-name*的动态表项

Deleted a dynamic DNS entry *host-name*

删除一个主机名为*host-name*的动态表项

The number of dynamic DNS entries has reached the maximum.

动态表项的数目已达到最大值

Listening on IPv4 TCP port 53

以TCP方式监听IPv4协议栈的53号端口

Listening on IPv6 TCP port 53

以TCP方式监听IPv6协议栈的53号端口

Listening on IPv4 UDP port 53

以UDP方式监听IPv4协议栈的53号端口

Listening on IPv6 UDP port 53

以UDP方式监听IPv6协议栈的53号端口

DNS proxy received a request for resolving *query-name.*

DNS代理收到一个解析*query-name*的查询请求

DNS proxy sent a reply for resolving *query-name.*

DNS代理发送一个解析*query-name*的应答

No DNS server is available, answered with a spoofing address *ip-address*

DNS服务器均不可达，以spoofing地址*ip-address*作为应答

Added a dynamic domain name *domain-name*

添加一个动态域名后缀*domain-name*

Deleted a dynamic domain name *domain-name*

删除一个动态域名后缀*domain-name*

Added a dynamic server *ip-address*

添加一个动态DNS服务器*ip-address*

Deleted a dynamic server *ip-address*

删除一个动态DNS服务器*ip-address*

表1-3 debugging dns error命令输出信息描述表

字段

描述

Failed to receive data

接收数据失败

Failed to allocate memory

分配内存失败

The PTR request doesn\'t support address family *family-type.*

PTR类查询不支持地址协议族*family-type*

Failed to bind socket

绑定套接字失败

Failed to connect to server

连接失败

Failed to create socket

创建套接字失败

Failed to set socket options

设置套接字选项失败

Listening socket hangs up

监听套接字关闭

Failed to get the IP address of interface *interface-name*

获取接口*interface-name*对应的IP地址失败

The number of VPN instances has reached the maximum.

VPN实例的数目已达到最大值

【举例】

\# 配置DNS服务器。

\<Sysname\> system-view

System View: return to User View with Ctrl+Z.

Sysname dns server 1.0.0.1

Sysname quit

*[//*]*打开DNS调试开关。*

\<Sysname\> terminal monitor

\<Sysname\> terminal logging level 7

\<Sysname\> debugging dns all

// ping test.com 从DNS服务器解析到地址为1.0.0.2

\<Sysname\> ping test.com

Ping test.com (1.0.0.2): 56 data bytes, press CTRL_C to break

56 bytes from 1.0.0.2: icmp_seq=0 ttl=128 time=1.000 ms

56 bytes from 1.0.0.2: icmp_seq=1 ttl=128 time=0.000 ms

56 bytes from 1.0.0.2: icmp_seq=2 ttl=128 time=0.000 ms

56 bytes from 1.0.0.2: icmp_seq=3 ttl=128 time=1.000 ms

56 bytes from 1.0.0.2: icmp_seq=4 ttl=128 time=1.000 ms

\-\-- Ping statistics for test.com \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 0.000/0.600/1.000/0.490 ms

\<Sysname\>

*// 启动查询主机test.com的IPv4地址的A类DNS查询。*

\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Starting A resolving for test.com

*// 在本地静态配置中查询。*

\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Trying to resolve test.com in local database

*// 在本地动态缓存中查询。*

\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Trying to resolve test.com in dynamic cache

*// 通过UDP向地址为1.0.0.1的DNS服务器查询。*

\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Trying to resolve test.com by contacting DNS server 1.0.0.1 through UDP

*// 发送查询报文的报文头部分的信息。*

\*Nov 16 09:56:02:480 2011 Sysname DNS/7/PACKET: -MDC=1; Sent:

Header:

 ID = 17767

 QR = 0, OpCode = 0, AA = 0, TC = 0, RD = 1

 RA = 0, Z = 0, AD = 0, CD = 0, RCode = 0

 QDCount = 1

 ANCount = 0

 NSCount = 0

 ARCount = 0

*// 发送查询报文的问题部分的内容。*

\*Nov 16 09:56:02:480 2011 Sysname DNS/7/PACKET: -MDC=1; Sent:

Question:

 QName  = test.com

 QType  = A (1)

 QClass = IN (1)

*// 等待服务器应答，等待时长为2秒。*

\*Nov 16 09:56:02:482 2011 Sysname DNS/7/EVENT: -MDC=1; Waiting 2 seconds for server response

*// 收到应答报文的报文头部分的内容。*

\*Nov 16 09:56:02:484 2011 Sysname DNS/7/PACKET: -MDC=1; Received:

Header:

 ID = 17767

 QR = 1, OpCode = 0, AA = 1, TC = 0, RD = 1

 RA = 0, Z = 0, AD = 0, CD = 0, RCode = 0

 QDCount = 1

 ANCount = 1

 NSCount = 2

 ARCount = 2

*// 收到应答报文的问题部分的内容。*

\*Nov 16 09:56:02:484 2011 Sysname DNS/7/PACKET: -MDC=1; Received:

Question:

 QName  = test.com

 QType  = A (1)

 QClass = IN (1)

*// 收到应答报文的答案部分的内容。*

\*Nov 16 09:56:02:484 2011 Sysname DNS/7/PACKET: -MDC=1; Received:

Answer:

 Name     = test.com

 Type     = A (1)

 Class    = IN (1)

 TTL      = 60

 RDLength = 4

 RData    = 192.168.20.177

\*Nov 16 09:56:02:484 2011 Sysname DNS/7/EVENT: -MDC=1; Received an answer: QName = test.com, ID = 17767

*// 添加test.com的查询记录到本地动态缓存。*

\*Nov 16 09:56:02:484 2011 Sysname DNS/7/EVENT: -MDC=1; Added a dynamic DNS entry test.com

*[// DNS*]*查询成功。*

\*Nov 16 09:56:02:484 2011 Sysname DNS/7/EVENT: -MDC=1; Successfully resolved test.com: host name is test.com, address is 1.0.0.2

\

**DDNS \-- DDNS调试命令 \-- debugging ddns**

------------------------------------------------------------------------

【命令】

**[debugging ddns**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging ddns**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DDNS服务器的所有调试信息开关。

**[error**]：表示DDNS服务器的错误调试信息开关。

**[event**]：表示DDNS服务器的事件调试信息开关。

**[packet**]：表示DDNS服务器的报文调试信息开关。

【描述】

**[debugging ddns**]命令用来打开DDNS服务器调试信息开关。

**[undo debugging ddns**]命令用来关闭DDNS服务器调试信息开关。

缺省情况下，DDNS服务器的调试信息开关处于关闭状态。

表2-1 debugging ddns packet命令输出信息描述表

字段

描述

Interface = *interface-name*, Policy = *policy-name*:

Packet sent:

*[packet-content*]

接口为*interface-name*，策略为*policy-name*，发送的数据内容为：*packet-content*

Interface = *interface-name*, Policy = *policy-name*:

Packet received:

*[packet-content*]

接口为*interface-name*，策略为*policy-name*，接收的数据内容为：*packet-content*

表2-2 debugging ddns event命令输出信息描述表

字段

描述

Interface = *interface-name*, Policy = *policy-name*: Starting DDNS update

接口为*interface-name*，策略为*policy-name*：开始DDNS更新

Interface = *interface-name*, Policy = *policy-name*: Created an update timer. The interval is *interval-value* seconds

接口为*interface-name*，策略为*policy-name*：创建一个时间间隔为*interval-value*秒更新定时器

Interface = *interface-name*, Policy = *policy-name*: Resolving IP address for server *server-name*

接口为*interface-name*，策略为*policy-name*：解析服务器*server-name*的IP地址

Interface = *interface-name*, Policy = *policy-name*: Server IP address is *ip-address*

接口为*interface-name*，策略为*policy-name*：服务器地址为*ip-address*

Interface = *interface-name*, Policy = *policy-name*: Connected to the server

接口为*interface-name*，策略为*policy-name*：已连接到服务器

Interface = *interface-name*, Policy = *policy-name*: Disconnected from the server

接口为*interface-name*，策略为*policy-name*：与服务器失去连接

Interface = *interface-name*, Policy = *policy-name*: The update timer timed out

接口为*interface-name*，策略为*policy-name*：更新定时器超时

Interface = *interface-name*, Policy = *policy-name*: Destroyed the update timer

接口为*interface-name*，策略为*policy-name*：销毁更新定时器

Interface = *interface-name*, Policy = *policy-name*: DDNS update failed

接口为*interface-name*，策略为*policy-name*：DDNS更新失败

Interface = *interface-name*, Policy = *policy-name*: Starting ODS update

接口为*interface-name*，策略为*policy-name*：开启ODS更新

Interface = *interface-name*, Policy = *policy-name*: Sent LOGIN request

接口为*interface-name*，策略为*policy-name*：发送LOGIN请求

Interface = *interface-name*, Policy = *policy-name*: Sent ADDRR request

接口为*interface-name*，策略为*policy-name*：发送ADDRR请求

Interface = *interface-name*, Policy = *policy-name*: Sent DELRR request

接口为*interface-name*，策略为*policy-name*：发送DELRR请求

Interface = *interface-name*, Policy = *policy-name*: Received response *response-code*

接口为*interface-name*，策略为*policy-name*：收到应答码*response-code*

Interface = *interface-name*, Policy = *policy-name*: Finished ODS update

接口为*interface-name*，策略为*policy-name*：完成ODS更新

Interface = *interface-name*, Policy = *policy-name*: Stopped ODS update

接口为*interface-name*，策略为*policy-name*：停止ODS更新

Interface = *interface-name*, Policy = *policy-name*: ODS update failed

接口为*interface-name*，策略为*policy-name*：ODS更新失败

Interface = *interface-name*, Policy = *policy-name*: Starting ORAY update

接口为*interface-name*，策略为*policy-name*：发起ORAY更新

Interface = *interface-name*, Policy = *policy-name*: Sent AUTH request

接口为*interface-name*，策略为*policy-name*：发送AUTH请求

Interface = *interface-name*, Policy = *policy-name*: Sent username and password

接口为*interface-name*，策略为*policy-name*：发送用户名和密码

Interface = *interface-name*, Policy = *policy-name*: Sent REGI request

接口为*interface-name*，策略为*policy-name*：发送REGI请求

Interface = *interface-name*, Policy = *policy-name*: Sent CNFM request

接口为*interface-name*，策略为*policy-name*：发送CNFM请求

Interface = *interface-name*, Policy = *policy-name*: Sent QUIT request

接口为*interface-name*，策略为*policy-name*：发送QUIT请求

Interface = *interface-name*, Policy = *policy-name*: Received response *reply-message*

接口为*interface-name*，策略为*policy-name*：收到ORAY应答消息*reply-message*

Interface = *interface-name*, Policy = *policy-name*: Sent a heartbeat to server, Chat ID = *chat-id*, OP Code = *op-code*, Start ID = *start-id*

接口为*interface-name*，策略为*policy-name*：发送心跳报文给服务器，会话ID为*chat-id*，操作码为*op-code*，启动ID为*start-id*

Interface = *interface-name*, Policy = *policy-name*: Received a heartbeat from server, Chat ID = *chat-id*, OP Code = *op-code*, Start ID = *start-id*, IP = *ip-address*

接口为*interface-name*，策略为*policy-name*：接收到服务器的心跳报文，会话ID为*chat-id*，操作码为*op-code*，启动ID为*start-id*，IP地址为*ip-address*

Interface = *interface-name*, Policy = *policy-name*: Stopped ORAY update

接口为*interface-name*，策略为*policy-name*：停止ORAY更新

Interface = *interface-name*, Policy = *policy-name*: Finished ORAY update, chat ID is *chat-id*, start ID is *start-id*

接口为*interface-name*，策略为*policy-name*：ORAY更新完成，chat ID为*chat-id*，start ID为*start-id*

Interface = *interface-name*, Policy = *policy-name*: ORAY update failed

接口为*interface-name*，策略为*policy-name*：ORAY更新失败

Interface = *interface-name*, Policy = *policy-name*: Starting GUNDIP update

接口为*interface-name*，策略为*policy-name*：发起GUNDIP更新

Interface = *interface-name*, Policy = *policy-name*: Stopped GUNDIP update

接口为*interface-name*，策略为*policy-name*：停止GUNDIP更新

Interface = *interface-name*, Policy = *policy-name*: Finished GUNDIP update

接口为*interface-name*，策略为*policy-name*：GUNDIP更新完成

Interface = *interface-name*, Policy = *policy-name*: GUNDIP update failed

接口为*interface-name*，策略为*policy-name*：GUNDIP更新失败

Interface = *interface-name*, Policy = *policy-name*: Sent GUNDIP update request

接口为*interface-name*，策略为*policy-name*：发送GUNDIP更新请求

Interface = *interface-name*, Policy = *policy-name*: Received response *packet*

接口为*interface-name*，策略为*policy-name*：收到GNUDIP应答*packet*

Interface = *interface-name*, Policy = *policy-name*: Starting HTTP/HTTPS update

接口为*interface-name*，策略为*policy-name*：发起HTTP/HTTPS更新

Interface = *interface-name*, Policy = *policy-name*: Stopped HTTP/HTTPS update

接口为*interface-name*，策略为*policy-name*：停止HTTP/HTTPS更新

Interface = *interface-name*, Policy = *policy-name*: Finished HTTP/HTTPS update

接口为*interface-name*，策略为*policy-name*：HTTP/HTTPS更新完成

Interface *interface-name* is activated

接口*interface-name*被激活

Interface *interface-name* is deactivated

接口*interface-name*去激活

Interface *interface-name* is up

接口*interface-name*变为UP状态

IP address of interface *interface-name* changed to *ip-address*

接口IP地址变为*ip-address*

表2-3 debugging ddns error命令输出信息描述表

字段

描述

Interface = *interface-name*, Policy = *policy-name*: The URL is invalid

接口为*interface-name*，策略为*policy-name*：无效的URL

Interface = *interface-name*, Policy = *policy-name*: Failed to lookup server IP address

接口为*interface-name*，策略为*policy-name*：查找服务器失败

Interface = *interface-name*, Policy = *policy-name*: The interface has no IP address

接口为*interface-name*，策略为*policy-name*：接口没有IP地址

Interface = *interface-name*, Policy = *policy-name*: Can't find the policy

接口为*interface-name*，策略为*policy-name*：找不到策略

Interface = *interface-name*, Policy = *policy-name*: The interface is not up

接口为*interface-name*，策略为*policy-name*：接口没有UP

Interface = *interface-name*, Policy = *policy-name*: Failed to connect to the server

接口为*interface-name*，策略为*policy-name*：连接服务器失败

Interface = *interface-name*, Policy = *policy-name*: Failed to create a socket

接口为*interface-name*，策略为*policy-name*：创建套接字失败

Interface = *interface-name*, Policy = *policy-name*: Failed to receive a packet

接口为*interface-name*，策略为*policy-name*：接收报文失败

Interface = *interface-name*, Policy = *policy-name*: Failed to send a packet

接口为*interface-name*，策略为*policy-name*：发送报文失败

Interface = *interface-name*, Policy = *policy-name*: Can't create SSL context by policy *ssl-policy*

接口为*interface-name*， 策略为*policy-name*： 通过策略*ssl-policy*创建SSL策略失败

【举例】

\# 打开DNS调试开关。

\<Sysname\> terminal monitor

Current terminal monitor is on.

\<Sysname\> terminal logging level 7

\<Sysname\> debugging ddns all

*// 配置DDNS policy。*

\<Sysname\> system-view

Sysname ddns policy oray

Sysname-ddns-policy-oray url oray://steven:nevets@phservice2.oray.net

Sysname-ddns-policy-oray quit

*// 接口引用DDNS policy。*

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ddns apply policy oray

Sysname-GigabitEthernet1/0/1

*// 开始DDNS更新。*

\*Nov 16 10:30:22:660 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Starting DDNS update

*// 启动周期更新定时器。*

\*Nov 16 10:30:22:660 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Create an update timer. The interval is 3720 seconds.

*// 解析服务器地址。*

\*Nov 16 10:30:22:660 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Resolving IP address for server phservice2.oray.net

\*Nov 16 10:30:22:661 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Server IP address is 202.105.21.217

*// 开始ORAY更新。*

\*Nov 16 10:30:22:661 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Starting ORAY update

*// 接收到服务器的欢迎信息。*

\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:

220 oray.cn DDNS ServerX6 Ready.

\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 220 oray.cn DDNS ServerX6 Ready.

*// 发送认证请求。*

\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent AUTH request

\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:

auth router6

*// 接收到服务器应答的挑战字。*

\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:

334 3vClhGrTEXdkTuvWsWghtQ==

\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 334 3vClhGrTEXdkTuvWsWghtQ==

*// 发送加密的用户名和密码。*

\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent username and password

\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:

aDNjZGRucyC/f8+6mZigJi6VWcZG9pw9zXBjqZf0t4E=

*// 接收到服务器应答的认证通过消息。*

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:

250 Auth passed at level \<1\>

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 250 Auth passed at level \<1\>

*// 接收到服务器应答的注册域名列表。*

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:

company.gicp.net

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response company.gicp.net

*// 发送更新注册动态域名请求。*

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent REGI request

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:

regi a company.gicp.net

*// 接收到服务器应答的注册域名列表结束标识。*

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:

.

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response .

*// 发送更新注册确认请求。*

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent CNFM request

\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:

cnfm

*// 接收到服务器应答的注册域名成功消息。*

\*Nov 16 10:30:22:667 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:

250 Register successfully

\*Nov 16 10:30:22:667 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 250 Register successfully

*// 接收到服务器应答的注册确认成功的消息。*

\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:

250 6319526 155100175

\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 250 6319526 155100175

*// 发送结束会话请求。*

\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent QUIT request

\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:

quit

*[// ORAY*]*会话结束，会话ID是6319526，心跳起始ID是155100175。*

\*Nov 16 10:30:22:771 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Finished ORAY update, chat ID is 6319526, start ID is 155100175

