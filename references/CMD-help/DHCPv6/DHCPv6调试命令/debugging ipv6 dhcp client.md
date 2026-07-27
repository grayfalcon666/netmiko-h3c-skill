<!-- CMD-INDEX
  debugging ipv6 dhcp client          | 用户视图             | L8
  debugging ipv6 dhcp relay           | 用户视图             | L478
  debugging ipv6 dhcp server          | 用户视图             | L818
  debugging ipv6 dhcp snooping        | 用户视图             | L1266
-->

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp client**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 dhcp client **[{ **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging ipv6 dhcp client **[{ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCPv6客户端所有调试信息开关。

**[error**]：表示DHCPv6客户端错误调试信息开关。

**[event**]：表示DHCPv6客户端事件调试信息开关。

**[packet**]：表示DHCPv6客户端报文调试信息开关。

【描述】

**[debugging ipv6 dhcp client**]命令用来打开DHCPv6客户端调试信息开关。**undo debugging ipv6 dhcp client**命令用来关闭DHCPv6客户端调试信息开关。

缺省情况下，DHCPv6客户端调试信息开关处于关闭状态。

表1-1 debugging ipv6 dhcp client error命令输出信息描述表

字段

描述

Failed to notify the client\'s information change.

通知其他模块失败，通知内容为客户端信息的变化

Failed to acquire IRT

不能获取IRT值

Failed to acquire interface control block.

不能获取接口控制块

Response without a server ID.

回应报文中没有server ID

Response without a client ID.

回应报文中没有client ID

Advertise message with matching transaction ID and mismatching client ID.

交互ID符合但client ID不符合的Advertise报文

Discarded invalid Advertise packet.

丢弃无效的Advertise报文。

Invalid DHCPv6 preference option length.

无效的DHCPv6优先级选项长度

Invalid server ID option information.

无效的serverID选项内容

Discarded invalid reply packet.

丢弃无效的Reply报文

Corrupt IAADDR options.

不完整的IA地址选项

Invalid IAADDR option.

无效的IA地址选项信息

Corrupt IA_NA options.

不完整的IA_NA选项

Invalid IA_NA option.

无效的IA_NA选项信息

Corrupt IAPREFIX options.

不完整的IA前缀选项

Invalid IAPREFIX option.

无效的IAPREFIX选项信息

Corrupt IA_PD options.

不完整的IA_PD选项

Invalid IA_PD option.

无效的IA_PD选项

Invalid status code length *length.*

无效的状态码选项长度

Wrong IA type in Advertise message

Advertise报文中IA类型错误

Wrong IA type in Reply message.

Reply报文中IA类型错误

Discarded reply without Rapid-Commit.

丢弃不包含Rapid-Commit选项的Reply报文

Can\'t renew without an active binding.

不存在有效的绑定无法启动renew操作

Malformed packet dhcp6:

option length does not equal its option buffer length.

非法的DHCP报文：服务器选项的实际长度和选项中"L"字段标识的长度不相等

Invalid unicast option length *length*.

无效的单播选项长度

IPv6 socket initilization failed.

IPv6 socket初始化发生错误

Invalid lifetime in the reply packet.

Reply报文中的生命期非法

Failed to send packet: only *send-length* of *total-length* bytes were sent.

发送报文失败，共* total-length*字节的报文仅发送出*send-length*字节

Failed to create max delay timer.

创建延迟发送定时器失败

Failed to create IPv6 socket, error: *error-number.*

创建IPv6 socket 失败，错误码*error-number.*

Failed to bind socket.

Socket ID: *socket-id*, error: *error-number*.

绑定socket失败，Socket ID *socket-id*，错误码 *error-number*

 Failed to set socket option.

 Socket ID: *socket-id*, error: *error-number*.

设置socket选项失败，Socket ID *socket-id*，错误码 *error-number*

Failed to receive packet from socket.

Socket ID: *socket-id*, error: *error-number*.

不能从socket接收报文，Socket ID *socket-id*，错误码 *error-number*

Discarded packet with no IA or address.

丢弃不含IA或地址的Advertise报文

Response with mismatching client ID

收到了应答报文，报文中的客户端ID和当前设备不匹配

Wrong length of option 52

Option 52长度错误

表1-2 debugging ipv6 dhcp client event命令输出信息描述表

字段

描述

Refresh event scheduled in *time* seconds.

在*time*秒后启动刷新事件日程表

Immediately selected the server that sent the Advertise message.

立即选择发出该Advertise报文的server

Recorded the server that sent the Advertise message.

记录发出该Advertise报文的server信息

Client information change notified successfully.

成功通知客户端信息变化

Address expired.

地址过期

Prefix expired.

前缀过期

Formed *msg-type*, *time* ms elapsed.

生成*msg-type*报文，其elapsed time选项为*time* ms

*[message-type* status code: *status code*.]

报文*message-type*的状态码为*status code*

*[Interface-name*: DHCPC6 *client-type* FSM state changed from *former-state* to *later-state* successfully. ]

接口*interface-name*上*client-type*类型的DHCPv6客户端从*former-state*状态转换到*later-state*状态

客户端类型的取值包括：

·PD：表示请求IPv6前缀的客户端

·ADDR：表示请求IPv6地址的客户端

·Stateless：表示DHCPv6无状态客户端

状态的取值包括：

·IDLE

·SOLICIT

·REQUEST

·OPEN

·RENEW

·REBIND

·RELEASE

·DECLINE

·INFO-REQUESTING

表1-3 debugging ipv6 dhcp client packet命令输出信息描述表

字段

描述

Packet sent

DHCPv6报文已发送

Packet received

DHCPv6报文已收到

Type *message-type*(*number*)

报文类型（报文类型号）

Transaction-ID *transaction-id*

DHCPv6客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程

Option

选项类型及类型号

Length

选项长度

Information

选项信息

【举例】

\# 在VLAN接口2上启动DHCPv6客户端的无状态配置，打开报文调试开关。

\<Sysname\> debugging ipv6 dhcp client packet

\*Feb 12 09:52:12:990 2013 Sysname DHCPC6/7/Packet: -MDC=1;

Vlan-interface2, Packet sent:

Type Information-request(11)

Transaction-id 0x07e0d3

Option               Length  Information

CLIENTID(1)          10      00030001000fe2ff0000

ORO(6)               12      DOMAIN_LIST(24)

                             DNS_SERVERS(23)

                             SIP_SERVER_A(22)

                             AC-LIST(52)

                             DS-LITE(64)

                             SIP_SERVER_D(21)

ELAPSED_TIME(8)      2       0

*[// DHCPv6*]*客户端发送INFORMATION-REQUEST报文*

\*Feb 12 10:00:45:696 2013 Sysname DHCPC6/7/Packet: -MDC=1;

Vlan-interface2, Packet received:

Type Reply(7)

Transaction-id 0x07e0d3

Option               Length  Information

CLIENTID(1)          10      00030001000fe2ff0000

SERVERID(2)          10      0003000100238963c4ba

DNS-SERVERS(23)      16      1:2:3::5

DOMAIN-LIST(24)      9       abc.com

*[// DHCPv6*]*客户端收到REPLY报文*

\# 在VLAN接口2上启动DHCPv6客户端的无状态配置，打开事件调试开关。

\<Sysname\> debugging ipv6 dhcp client event

\*Feb 20 17:37:26:502 2013 Sysname DHCPC6/7/Event: -MDC=1;

Client information change notified successfully.

*[//*]*成功通知客户端信息变化*

\# 在VLAN接口2上启动DHCPv6客户端的无状态配置，打开错误调试开关。

\<Sysname\> debugging ipv6 dhcp client error

\*Feb 25 09:05:19:102 2013 Sysname DHCPC6/7/Error: -MDC=1;

Failed to acquire IRT

*[//*]*不能获取IRT值*

\# 配置接口GigabitEthernet1/0/1作为DHCPv6客户端以二报文交互方式申请IPv6地址，打开DHCPv6客户端的所有调试开关。

\<Sysname\> debugging ipv6 dhcp client all

\*Feb  9 14:37:40:312 2013 Sysname DHCPC6/7/Event: -MDC=1;

GigabitEthernet1/0/1: DHCPC6 ADDR FSM state changed from IDLE to SOLICIT successfully.

*// 接口gigabitEthernet1/0/1上ADDR类型的DHCPv6客户端从IDLE状态转换到SOLICIT状态*

\*Feb  9 14:37:40:312 2013 Sysname DHCPC6/7/Packet: -MDC=1;

GigabitEthernet1/0/1, Packet sent:

Type Solicit(1)

Transaction-ID 0xd60e00

Option               Length  Information

RAPID_COMMIT(14)     0

CLIENTID(1)          10      00030001000fe2ff0000

IA_NA(3)             40      IAID: 0xf0019

                             T1: 0

                             T2: 0

IAADDR(5)            24      Address: ::

                             Preferred lifetime: 0

                             Valid lifetime: 0

ORO(6)               12      DOMAIN_LIST(24)

                             DNS_SERVERS(23)

                             SIP_SERVER_A(22)

                             AC-LIST(52)

                             DS-LITE(64)

                             SIP_SERVER_D(21)

ELAPSED_TIME(8)      2       0

*// 发送的报文内容*

\*Feb  9 14:37:40:468 2013 Sysname DHCPC6/7/Packet: -MDC=1;

GigabitEthernet1/0/1, Packet received:

Type Reply(7)

Transaction-ID 0xd60e00

Option               Length  Information

RAPID_COMMIT(14)     0

CLIENTID(1)          10      00030001000fe2ff0000

SERVERID(2)          14      0003000100238963c4ba

IA_NA(3)             74      IAID: 0xf0019

                             T1: 300

                             T2: 400

IAADDR(5)            24      Address: 100::9DD8:D090:A1A6:7858

                             Preferred lifetime: 500

                             Valid lifetime: 600

STATUS_CODE(13)      30      status-code: Success(0)

DNS_SERVERS(23)      32      2000::FF

                             2000::FE

DOMAIN_LIST(24)      32      example.com

                             example2.test.com

*// 收到应答报文，输出接收到的报文的内容*

\*Feb  9 14:37:40:488 2013 Sysname DHCPC6/7/Event: -MDC=1;

GigabitEthernet1/0/1: DHCPC6 ADDR FSM state changed from SOLICIT to OPEN successfully.

*// 接口GigabitEthernet1/0/1上ADDR类型的DHCPv6客户端从SOLICIT状态转换到OPEN状态*

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp relay**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 dhcp relay **[{ **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging ipv6 dhcp relay**[ { **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCPv6中继的所有调试信息开关。

**[error**]：表示DHCPv6中继的错误调试信息开关。

**[event**]：表示DHCPv6中继的事件调试信息开关。

**[packet**]：表示DHCPv6中继的报文调试信息开关。

【描述】

**[debugging ipv6 dhcp relay**]命令用来打开DHCPv6中继调试信息开关。**undo debugging ipv6 dhcp relay**命令用来关闭DHCPv6中继调试信息开关。

缺省情况下，DHCPv6中继调试信息开关处于关闭状态。

表1-4 debugging ipv6 dhcp relay packet命令输出信息描述表

字段

描述

From *ipv6-address* port *port*

接收报文时表示报文的源地址和端口号

To *ipv6-address* port *port*

发送报文时表示报文的目的地址和端口号

interface *interface-name*

接收或发送报文的接口名称

Message type: *message-type*

DHCPv6消息类型，包括：

·Solicit

·Advertise

·Request

·Confirm

·Renew

·Rebind

·Reply

·Release

·Decline

·Reconfigure

·Information-Request

·Relay-Forward

·Relay-Reply

Transaction ID: *transaction-id*

DHCPv6客户端发起申请时生成的一个随机数，用来唯一标示一次申请过程

Hop count: *hops*

DHCPv6报文经过的DHCPv6中继的数目，如果是Relay-Forward或者是Relay-Reply报文时输出

Link address: *ipv6-address*

链路地址，如果DHCPv6报文为Relay-Forward或Relay-Reply报文，则打印该字段

Peer address: *ipv6-address*

对端地址，如果DHCPv6报文为Relay-Forward或Relay-Reply报文，则打印该字段

表1-5 debugging ipv6 dhcp relay event命令输出信息描述表

字段

描述

Received a short packet from *ipv6-address* port *port-number*, length *length* bytes.

收到一个来自地址为*ipv6-address*端口号为*port-number*长度为*length*的短包

Can not find an interface to process the packet.

找不到处理报文的接口，一般为对应的接口没有启用DHCPv6功能

Discard the *message-type* message from *ipv6-address* port *port-number*.

丢弃从地址*ipv6-address*端口号*port-number*收到的类型为*message-type*的报文

Discard the *message-type* message to *ipv6-address* port *port-number*.

丢弃发送到地址*ipv6-address*端口号*port-number*的类型为*message-type*的报文

Interface *interface-name* is activated.

接口*interface-name*被激活

Add an IPv6 address *ipv6-address* to the interface *interface-name*.

接口*interface-name*添加IPv6地址*ipv6-address*

Interface *interface-name* is deactivated.

接口*interface-name*被去激活

Delete an IPv6 address *ipv6-address* from the interface *interface-name*.

接口*interface-name*删除IP地址*ipv6-address*

Interface *interface-name* is deleted.

接口*interface-name*被删除

The MAC address of interface *interface-name* is changed..

接口*interface-name*的MAC地址改变

Invalid packet length.

报文长度无效

Invalid relay message option.

报文中的relay message option选项无效

The length of relay-forward or relay-reply packet is invalid.

Relay-forward或Relay-reply报文长度无效

No relay message option.

报文中缺少relay message option选项

Relay the *message-type* message from *ipv6-address* port *port-number* to a DHCPv6 server.

将从地址*ipv6-address*端口号*port-number*收到的类型为*message-type*的上行报文转发给DHCPv6服务器

Relay the *message-type* message from *ipv6-address* port *port-number* to a DHCPv6 client.

将从地址*ipv6-address*端口号*port-number*收到的类型为*message-type*的上行报文转发给DHCPv6客户端

The hop count exceeds the limit.

报文中记录的跳数超过最大值

The relay-reply packet is a multicast packet.

收到的relay-reply报文是组播报文

Relay a message with unknown type *message-type-id* to *ipv6-address* port *port-number*.

转发报文类型为*message-type-id*的未知类型的下行报文到地址*ipv6-address*端口号*port-number*

Relay a message with unknown type *message-type-id* from *ipv6-address* port *port-number*.

转发从地址*ipv6-address*端口号*port-number*收到的类型ID为*message-type-id*的未知类型的上行报文

Unknown interface event *event* is detected on interface *interface-name*.

接口*interface-name*检测到不支持的接口事件*event*

Unknown IP address event *event* is detected on interface *interface-name*.

接口*interface-name*检测到不支持的IP地址事件*event*

表1-6 debugging ipv6 dhcp relay error命令输出信息描述表

字段

描述

Error occurs when calculation the value of option *option-code*.

计算选项编号为*option-code*的选项的值出错

Failed to get IPv6 address of interface *interface-name*.

获取接口*interface-name*的IPv6地址失败

Failed to send packet.

发送报文失败

Malformed packet dhcp6:

option length does not equal its option buffer length.

非法的DHCP报文：服务器选项的实际长度和选项中"L"字段标识的长度不相等

Not enough space for option *option-code.*

报文中没有空间存储选项编号为*option-code*的选项内容

Not enough space for more options.

报文中没有空间存储过多的选项

【举例】

\# 打开DHCPv6中继的报文调试信息开关。DHCPv6客户端通过DHCPv6中继从DHCPv6服务器获取IPv6地址时，将打印如下信息。

\<Sysname\> terminal monitor

\<Sysname\> terminal logging level 7

\<Sysname\>

\*Mar 25 11:51:01:194 2011 Sysname DHCPR6/7/PACKET:

From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Solicit (1)

Transaction ID: 0x00003889

*// 从接口GigabitEthernet1/0/1接收到Solicit报文，Transaction ID为0x00003889*

\*Mar 25 11:51:01:195 2011 Sysname DHCPR6/7/EVENT: Relay the Solicit message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 server.

\*Mar 25 11:51:01:196 2011 Sysname DHCPR6/7/PACKET:

To 2::2 port 547, interface is selected by routing table

Message type: Relay-Forward (12)

Hop count: 0

Link address: 1::1

Peer address: fe80::215:32ff:fe1b:8901

*// 将接收到的Solicit报文封装在Relay-Forward报文中，并转发给DHCPv6服务器2::2*

\*Mar 25 11:51:01:198 2011 Sysname DHCPR6/7/PACKET:

From 2::2 port 547, interface GigabitEthernet1/0/2

Message type: Relay-Reply (13)

Hop count: 0

Link address: 1::1

Peer address: fe80::215:32ff:fe1b:8901

*// 从接口GigabitEthernet1/0/2接收到Relay-Reply报文*

\*Mar 25 11:51:01:199 2011 Sysname DHCPR6/7/EVENT: Relay the Advertise message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 client.

\*Mar 25 11:51:01:200 2011 Sysname DHCPR6/7/PACKET:

To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Advertise (2)

Transaction ID: 0x00003889

*// 从Relay-reply报文中解析出Advertise报文，并转发给DHCPv6客户端fe80::215:32ff:fe1b:8901，Transaction ID为0x00003889*

\*Mar 25 11:51:02:121 2011 Sysname DHCPR6/7/PACKET:

From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Request (3)

Transaction ID: 0x0000388a

\*Mar 25 11:51:02:121 2011 Sysname DHCPR6/7/EVENT: Relay the Request message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 server.

*// 从接口GigabitEthernet1/0/1接收到Request报文，Transaction ID为0x0000388a*

\*Mar 25 11:51:02:121 2011 Sysname DHCPR6/7/PACKET:

To 2::2 port 547, interface is selected by routing table

Message type: Relay-Forward (12)

Hop count: 0

Link address: 1::1

Peer address: fe80::215:32ff:fe1b:8901

*// 将接收到的Request报文封装在Relay-Forward报文中，并转发给DHCPv6服务器2::2*

\*Mar 25 11:51:02:125 2011 Sysname DHCPR6/7/PACKET:

From 2::2 port 547, interface GigabitEthernet1/0/2

Message type: Relay-Reply (13)

Hop count: 0

Link address: 1::1

Peer address: fe80::215:32ff:fe1b:8901

*// 从接口GigabitEthernet1/0/2接收到Relay-Reply报文*

\*Mar 25 11:51:02:126 2011 Sysname DHCPR6/7/EVENT: Relay the Reply message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 client.

\*Mar 25 11:51:02:127 2011 Sysname DHCPR6/7/PACKET:

To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Reply (7)

Transaction ID: 0x0000388a

*// 从Relay-reply报文中解析出Reply报文，并转发给DHCPv6客户端fe80::215:32ff:fe1b:8901，Transaction ID为0x0000388a*

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp server**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 dhcp server **[{ **all** \| **error** \| **event** \| **packet** [ **verbose** ] }]]

**[undo debugging ipv6 dhcp server **[{ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCPv6服务器的所有调试信息开关

**[error**]：表示DHCPv6服务器的错误调试信息开关。

**[event**]：表示DHCPv6服务器的事件调试信息开关。

**[packet**]：表示DHCPv6服务器的报文调试信息开关。

**[verbose**]：表示DHCPv6报文的详细信息。

【描述】

**[debugging ipv6 dhcp server**]命令用来打开DHCPv6服务器的调试信息开关。**undo debugging ipv6 dhcp server**命令用来关闭DHCPv6服务器的调试信息开关。

缺省情况下，DHCPv6服务器的调试信息开关处于关闭状态。

表1-7 debugging ipv6 dhcp server packet命令输出信息描述表

字段

描述

From *ipv6-address* port *port*

接收报文时表示报文的源地址和端口号

To *ipv6-address* port *port*

发送报文时表示报文的目的地址和端口号

interface *interface-name*

接收或发送报文的接口名称

Message type: *message-type*

DHCPv6消息类型，包括：

·Solicit

·Advertise

·Request

·Confirm

·Renew

·Rebind

·Reply

·Release

·Decline

·Reconfigure

·Information-Request

·Relay-Forward

·Relay-Reply

Transaction ID: *transaction-id*

DHCPv6客户端发起申请时生成的一个随机数，用来唯一标示一次申请过程

Link address: *ipv6-address*

链路地址，如果DHCPv6报文为Relay-Forward或Relay-Reply报文，则打印该字段

Peer address: *ipv6-address*

对端地址，如果DHCPv6报文为Relay-Forward或Relay-Reply报文，则打印该字段

Options:

  option *option-name* *option-code*

    *option-value*

报文选项，显示详细报文信息时输出，*option-name*为报文选项对应的名字，*option-code*为选项的数值，*option-value*为报文选项的内容

表1-8 debugging ipv6 dhcp server event命令输出信息描述表

字段

描述

Received a short packet from *ipv6-address* port *port-number*, length *length* bytes.

收到一个来自地址为*ipv6-address*端口号为*port-number*长度为*length*的短包

Add a conflict IP *ipv6-address*.

添加冲突地址*ip-address*

Address *ipv6-address* is not bound to client.

地址*ipv6-address*没有和客户端绑定

Can not find an interface to process the packet.

找不到处理报文的接口，一般为对应的接口没有启用DHCPv6功能

Released prefix *ipv6-prefix* is not bound to the client.

客户端请求释放的前缀*ipv6-prefix*没有和客户端绑定

Client declines address *ipv6-address*.

客户端通过Decline报文报告地址*ipv6-address*冲突

Discard *message-type* from *ipv6-address*: Client identifier inexistent.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文中没有client identifier

Discard *message-type* from *ipv6-address*: Server identifier exists.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文中包含server identifier

Discard *message-type* from *ipv6-address*: Server identifier inexistent.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文中没有server identifier

Discard *message-type* from *ipv6-address*: Server identifier mismatched.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文中的server identifier不匹配

Discard *message-type* from *ipv6-address*: IA_NA option exists.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文中包含IA_NA选项

Discard *message-type* from *ipv6-address*: IA_TA option exists..

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文中包含IA_TA选项

Discard *message-type* from *ipv6-address*: IA_PD option exists.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文中包含IA_PD选项

Discard *message-type* from *ipv6-address*: unicast packet.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是报文是单播报文

Discard *message-type* from *ipv6-address*: Unsupported message type.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是不支持的消息类型

Discard *message-type* from *ipv6-address*: Unsupported message type for the stateless server.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是无状态配置服务器不支持的消息类型

Discard *message-type* from *ipv6-address*: Failed to find pool.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是找不到地址池。

Discard message-type from *ipv6-address*: can\'t find the pool.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是找不到地址池。

Discard message-type from *ipv6-address*: can\'t find the prefix pool.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是找不到前缀地址池。

Discard *message-type* from *ipv6-address*: can't find the network.

丢弃来自地址*ipv6-address*的消息类型为*message-type*的报文。原因是找不到network。

Discard unknown packet received from *ipv6-address*.

丢弃来自地址*ipv6-address*的未知报文

Interface *interface-name* is activated.

接口*interface-name*被激活

Add an IPv6 address *ipv6-address* to the interface *interface-name*.

接口*interface-name*添加IP地址*ipv6-address*

Interface *interface-name* is deactivated.

接口*interface-name*被去激活

Delete an IPv6 address *ipv6-address* from the interface *interface-name*.

接口*interface-name*删除IPv6地址*ipv6-address*

Interface *interface-name* is deleted.

接口*interface-name*被删除

The MAC address of interface *interface-name* is changed.

接口*interface-name*的MAC地址改变

No IA_NA or IA_TA option needs to be confirmed.

报文中没有需要确认的IA_NA或IA_TA选项

Relay-forward from *ipv6-address* with link address *link-address* and peer address *peer-address* misses the relay message option.

从地址*ipv6-address*收到的Relay-forward报文中没有relay message option选项，该报文中的link address字段为*link-address*和peer address字段为*peer-address*

Released address *ipv6-address*.

释放地址*ipv6-address*

Releases prefix *ipv6-prefix*.

释放地址前缀*ipv6-prefix*

Send *send-bytes* of *total-bytes* bytes.

发送了*total-bytes*字节报文中的*send-byte*字节数据

Send *message-type* to *ipv6-address*.

向地址*ipv6-address*发送消息类型为*message-type*的报文

Received *message-type* from *ipv6-address*

从地址*ipv6-address*接收到消息类型为*message-type*的报文

Unknown interface event *event* is detected on interface *interface-name*.

接口*interface-name*检测到不支持的接口事件*event*

Detect unknown IP address event *event* on interface *interface-name*.

接口*interface-name*检测到不支持的IP地址事件*event*

表1-9 debugging ipv6 dhcp server error命令输出信息描述表

字段

描述

Error occurs when calculation the value of option *option-code*.

计算选项编号为*option-code*的选项的值出错

Error occurs when parsing *option-type* option.

解析类型为*option-type*的选项失败

Error occurs when calculation the value of *option-type* option.

计算选项类型为*option-type*选项的值出错

Malformed packet dhcp6:

option length does not equal its option buffer length.

非法的DHCP报文：服务器选项的实际长度和选项中"L"字段标识的长度不相等

Failed to allocate a NA lease: Because the number of leases has reached the maximum.

分配NA租约失败，数量达到上限

Failed to allocate a prefix lease: Because the number of leases has reached the maximum.

分配前缀租约失败，数量达到上限

Failed to get interface address or link address.

获取接口地址或者报文链路地址失败

Failed to add *option-type* option to the packet.

向报文中保存*option-type*选项失败

Failed to send packet.

发送报文失败

Failed to set *status-code* status code in the reply packet.

在Reply报文中设置状态码*status-code*失败

No free IP in the address range of the pool..

address range中没有可分配的IP地址

No free IP in the network *network-address*.

网段*network-address*中没有可分配的IP地址

No free prefix in prefix pool *prefix-pool-index*.

前缀地址池*prefix-pool-index*中没有可分配的前缀

No enough space for option *option-code.*

报文中没有空间存储选项编号为*option-code*的选项内容

No enough space for more options.

报文中没有空间存储过多的选项

【举例】

\# 打开DHCPv6服务器的所有调试信息开关。DHCPv6客户端申请IPv6地址时，设备上将打印如下调试信息。

\<Sysname\> terminal monitor

\<Sysname\> terminal logging level 7

\<Sysname\> debugging ipv6 dhcp server all

\<Sysname\> debugging ipv6 dhcp server packet verbose

\<Sysname\>

\*Mar 25 11:45:06:338 2011 Sysname DHCPS6/7/PACKET:

From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Solicit (1)

Transaction ID: 0x00009c46

Options:

  option client-id 14

    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01

  option ia-na 40

    00:00:00:01:ff:ff:ff:ff:ff:ff:ff:ff:00:05:00:18:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:ff:ff:ff:ff:ff:ff:ff:ff

  option elapsed-time 2

    1

*// 服务器收到客户端fe80::215:32ff:fe1b:8901发送的SOLICIT消息，其中携带一个IA_NA选项*

\*Mar 25 11:45:06:339 2011 Sysname DHCPS6/7/EVENT: Send Advertise to fe80::215:32ff:fe1b:8901 port 546.

\*Mar 25 11:45:06:340 2011 Sysname DHCPS6/7/PACKET:

To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Advertise (2)

Transaction ID: 0x00009c46

Options:

  option client-id 14

    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01

  option server-id 10

    00:03:00:01:00:11:22:33:44:00

  option ia-na 40

    00:00:00:01:00:04:9d:40:00:07:62:00:00:05:00:18:00:01:00:00:00:00:00:00:00:00:00:00:00:00:00:10:00:09:3a:80:00:27:8d:00

\*Mar 25 11:45:06:340 2011 Sysname DHCPS6/7/EVENT: Send 80 of 80 bytes.

*// 服务器向客户端发送ADVERTISE消息，报文中包含为IA_NA选项拟分配的地址1::10 *

\*Mar 25 11:45:06:373 2011 Sysname DHCPS6/7/PACKET:

From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Request (3)

Transaction ID: 0x00009c47

Options:

  option client-id 14

    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01

  option server-id 10

    00:03:00:01:00:11:22:33:44:00

  option ia-na 40

    00:00:00:01:ff:ff:ff:ff:ff:ff:ff:ff:00:05:00:18:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:ff:ff:ff:ff:ff:ff:ff:ff

  option elapsed-time 2

    3

*// 服务器收到客户端发送的REQUEST消息*

%Mar 25 11:45:06:374 2011 Sysname DHCPS6/5/ALLOCATE_IP: Server IP = 1::1, DHCPv6 client IP = 1::10, DHCPv6 client DUID = 0001-0006-b794-1c15-0015-321b-8901, IAID = 00000001, DHCPv6 client lease = 2592000 seconds.

\*Mar 25 11:45:06:374 2011 Sysname DHCPS6/7/EVENT: Send Reply to fe80::215:32ff:fe1b:8901 port 546.

\*Mar 25 11:45:06:375 2011 Sysname DHCPS6/7/PACKET:

To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1

Message type: Reply (7)

Transaction ID: 0x00009c47

Options:

  option client-id 14

    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01

  option server-id 10

    00:03:00:01:00:11:22:33:44:00

  option ia-na 40

    00:00:00:01:00:04:9d:40:00:07:62:00:00:05:00:18:00:01:00:00:00:00:00:00:00:00:00:00:00:00:00:10:00:09:3a:80:00:27:8d:00

\*Mar 25 11:45:06:375 2011 Sysname DHCPS6/7/EVENT: Send 80 of 80 bytes.

*// 服务器向客户端发送REPLY消息，确认将地址1::10分配给客户端*

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp snooping**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 dhcp snooping **[{ **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging ipv6 dhcp snooping **[{ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DHCPv6 Snooping的所有调试信息开关。

**[error**]：表示DHCPv6 Snooping的错误调试信息开关。

**[event**]：表示DHCPv6 Snooping的事件调试信息开关。

**[packet**]：表示DHCPv6 Snooping的报文调试信息开关。

【描述】

**[debugging ipv6 dhcp snooping**]命令用来打开DHCPv6 Snooping调试信息开关。**undo debugging ipv6 dhcp snooping**命令用来关闭DHCPv6 Snooping调试信息开关。

缺省情况下，DHCPv6 Snooping调试信息开关处于关闭状态。

表1-10 debugging ipv6 dhcp snooping error命令输出信息描述表

字段

描述

Failed to delete IPCIM entries by VLAN *vlan-id*.

通知IPCIM删除VLAN *vlan-id*下的表项失败

Failed to delete IPCIM entries on interface *interface-name*

通知IPCIM删除接口*interface-name*下的表项失败

Failed to delete an IPCIM entry.

通知IPCIM删除一条IPCIM表项失败

Failed to synchronize IPCIM results.

同步IPCIM结果失败

Failed to synchronize IPCIM.

同步IPCIM失败

Insufficient storage space.

存储空间不足

表1-11 debugging ipv6 dhcp snooping event命令输出信息描述表

字段

描述

Number of DHCPv6 snooping entries has reached the maximum (interface is *interface-name*)

接口*interface-name*下的DHCPv6 Snooping表项个数达到最大值

Started to synchronize IPCIM.

开始同步IPCIM

Finished synchronizing IPCIM.

结束同步IPCIM

Finished recovering entries.

表项恢复完成

表1-12 debugging ipv6 dhcp snooping packet命令输出信息描述表

字段

描述

Received a DHCPv6 *type* packet.

收到类型为*type*的DHCPv6报文，DHCPv6报文类型为：

·SOLICIT

·REQUEST

·CONFIRM

·RENEW

·REBIND

·RELEASE

·DECLINE

·INFORMATION-REQUEST

·ADVERTISE

·RECONFIGURE

·REPLY

L3Output: Started to process DHCPv6 packets.

三层出方向开始处理报文

L3Output: Ignored request packets.

三层出方向请求报文不处理

Started to process DHCPv6 packets.

开始处理DHCPv6报文

DHCPv6 packet sent to slot *slot-number*

DHCP报文透传主用板*slot-number*

Processed a DHCPv6 RELAY-REPLY packet.

处理DHCPv6 RELAY-REPLY报文

Successfully sent packets in VLAN (interface is *interface-name*).

VLAN内的接口*interface-name*转发报文成功

Failed to send a DHCP packet.

发送DHCP报文失败

Sending the packet to all ports in VLAN *vlan-id*.

将DHCPv6报文发送到VLAN *vlan-id*内的所有端口

Sending the packet by interface *interface-name* of VLAN *vlan-id.*

设备通过VLAN *vlan-id*内接口*interface-name*转发报文

Started to check validity of the DHCP-request-packet.

开始请求方向报文有效性检查

Filled option 18 information: Length is *length*, PortIndex is *interface-name* Outer VLAN is *vlan-id,* Inner VLAN is *vlan-id*, DUID is *duid*.

填充Option 18：长度是*length*，接口索引是*interface-name*，外层VLAN *vlan-id*，内层VLAN *vlan-id*，DUID是*duid*

Successfully stripped Option *option-id*: Offset is *offset,* Stripped length is *length.*

剥离Option *option-id*，偏移量*offset*，剥离长度*length*

Padded option 18: Offset is *offset.*

在报文中填充Option18选项，偏移量*offset*

Failed to pad option 18.

在报文中填充Option18选项失败

Failed to strip option 18.

在报文中剥离Option18选项失败

Filled option 37 information: Length is *length* Enterprise number is *number*, PortIndex is *interface-name*, Outer VLAN is *vlan-id*, Inner VLAN is *vlan-id*, DUID is *duid.*

填充Option 37：长度是*length*，厂商标识是*number*，接口索引是*interface-name*，外层VLAN *vlan-id*，内层VLAN *vlan-id*，DUID是*duid*

Padded option 37: Offset is *offset.*

填充报文Option37，偏移量*offset*

Failed to pad option 37.

填充Option37失败

Failed to strip option 37.

剥离Option37失败

【举例】

\# 打开DHCPv6 Snooping的报文调试信息开关，并收到DHCPv6 Reply报文。

\<Sysname\> terminal debugging

\<Sysname\> debugging ipv6 dhcp snooping packet

\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1-Chassis=3-Slot=3; The DHCPv6

packet is sent to slot 58.

*[// DHCPv6*]*报文透传至58号单板*

\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1; Started to process DHCPv6 packets.

*[// DHCPv6 Snooping*]*预处理报文*

\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1; Received a DHCPv6 REPLY packet.

*// 接收到DHCPv6 Reply报文*

\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1; Sending the packet to all ports in VLAN 2.

*// 将DHCPv6报文在VLAN 2内转发*

