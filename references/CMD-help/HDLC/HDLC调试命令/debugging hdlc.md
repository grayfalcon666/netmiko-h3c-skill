
**HDLC \-- HDLC调试命令 \-- debugging hdlc**

------------------------------------------------------------------------

**[debugging hdlc**]命令用来打开HDLC调试信息开关。

**[undo debugging hdlc**]命令用来关闭HDLC调试信息开关。

【命令】

**[debugging hdlc **[{ **all** \| **event** \| { **ip** \| **ipv6** \| **isis** \| **keepalive** \| **mpls** } { **in** \| **in-out** \| **out** } } [ **interface** *interface-type interface-number* ]]]

**[undo debugging hdlc**[ { **all** \| **event** \| { **ip** \| **ipv6** \| **isis** \| **keepalive** \| **mpls** } { **in** \| **in-out** \| **out** } } [ **interface** *interface-type interface-number* ]]]

【缺省情况】

HDLC调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[event**]：表示事件调试信息开关。

**[ip**]：表示IP报文调试信息开关。

**[ipv6**]：表示IPv6报文调试信息开关。

**[isis**]：表示IS-IS报文调试信息开关。

**[keepalive**]：表示keepalive报文调试信息开关。

**[mpls**]：表示MPLS报文调试信息开关。

**[in**]：表示报文方向为入方向。

**[in-out**]：表示包括入/出两个方向的报文。

**[out**]：表示报文方向为出方向。

**[interface ***interface-type interface-number*]：表示指定接口的调试信息开关。

【使用指导】

表1-1 debugging hdlc event命令输出信息描述表

字段

描述

Interface *interface-name* keepalive timer started, timer ID = *id*.

接口的定时器启动

Interface *interface-name* keepalive timer stopped, timer ID = *id*.

接口的定时器停止

Interface *interface-name* keepalive timer reset, timer ID = *id*.

接口的定时器重置

Interface *interface-name* keepalive timer expired, timer ID = *id*.

接口的定时器超时

Interface *interface-name* keepalive function is disabled, and the frame is dropped.

关闭接口的keepalive机制，丢弃帧

Interface *interface-name* failed to send keepalive packets.

接口的keepalive报文发送失败

Loopback is detected on interface *interface-name*.

在接口上探测到环回

Interface *interface-name* added adjacency table.

添加接口的IPv4邻接表

Interface *interface-name* added IPv6 adjacency table.

添加接口的IPv6邻接表

Interface *interface-name* deleted adjacency table.

删除接口的IPv4邻接表

Interface *interface-name* deleted IPv6 adjacency table.

删除接口的IPv6邻接表

表1-2 debugging hdlc ip命令输出信息描述表

字段

描述

Interface *interface-name* received an IP packet.

接口收到一个IP报文

Interface *interface-name* sent an IP packet.

接口发送一个IP报文

Length

报文长度

Address

报文HDLC地址，IP报文的HDLC地址为单播地址0x0F

表1-3 debugging hdlc ipv6命令输出信息描述表

字段

描述

Interface *interface-name* received an IPv6 packet.

接口收到一个IPv6报文

Interface *interface-name* sent an IPv6 packet.

接口发送一个IPv6报文

Length

报文长度

Address

报文HDLC地址， IPv6报文的HDLC地址为单播地址0x0F

表1-4 debugging hdlc isis命令输出信息描述表

字段

描述

Interface *interface-name* received an ISIS packet.

接口收到一个ISIS报文

Interface *interface-name* sent an ISIS packet.

接口发送一个ISIS报文

Length

报文长度

Address

报文HDLC地址，ISIS报文的HDLC地址为组播地址0x8F

表1-5 debugging hdlc keepalive命令输出信息描述表

字段

描述

Interface *interface-name* received a KEEPALIVE packet.

接口收到一个keepalive报文

Interface *interface-name* sent a KEEPALIVE packet.

接口发送一个keepalive报文

Interface *interface-name* received a KEEPALIVE_REQ packet.

接口收到一个keepalive请求报文

Interface *interface-name* sent a KEEPALIVE_REQ packet.

接口发送一个keepalive请求报文

Interface *interface-name* received an ADDR_REQ packet.

接口收到一个地址请求报文

Interface *interface-name* received an ADDR_REPLY packet.

接口收到一个地址应答报文

Interface *interface-name* sent an ADDR_REPLY packet.

接口发送一个地址应答报文

Length

报文长度

Address

报文HDLC地址，keepalive报文的HDLC地址为组播地址0x8F

RemoteSeq

远端当前协议报文序号

AckedLocalSeq

远端保存的本地上次协议报文序号

LocalSeq

本地协议报文序号

AckedRemoteSeq

本地保存的远端协议报文序号

line UP

链路UP

line DOWN

链路DOWN

表1-6 debugging hdlc mpls命令输出信息描述表

字段

描述

Interface *interface-name* received an MPLS packet.

接口收到一个MPLS报文

Interface *interface-name* sent an MPLS packet.

接口发送一个MPLS报文

Length

报文长度

Address

报文HDLC地址，MPLS报文的HDLC地址为单播地址0x0F

【举例】

Router A的接口和Router B的接口上均封装HDLC协议，且Router A和Router B链路UP。

\# 打开Router B上HDLC的事件调试信息开关，可查看到如下调试信息：

\<RouterB\> debugging hdlc event

\*Jan 30 17:12:27:141 2012 RouterB HDLC/7/EVENT: -MDC=1; Interface Serial2/1/0 keepalive timer expired, timer ID = 354.

*// 接口Serial2/1/0的keepalive定时器超时*

\# 打开Router B上HDLC的IP报文调试信息开关，在接口下配置IP地址，并从Router A ping Router B，可查看到如下调试信息：

\<RouterB\> debugging hdlc ip in

\*Jan 31 09:20:56:093 2012 RouterB HDLC/7/IP: -MDC=1; Interface Serial2/1/0 received an IP packet. Length: 88, Address: 0x0F

*// 接口Serial2/1/0收到IP报文*

\# 打开Router B上HDLC的IPv6报文调试信息开关，在接口下配置IPv6地址，并从Router A ping Router B，可查看到如下调试信息：

\<RouterB\> debugging hdlc ipv6 in

\*Jan 31 09:28:23:552 2012 RouterB HDLC/7/IPv6: -MDC=1; Interface Serial2/1/0 received an IPv6 packet. Length: 68, Address: 0x0F

*// 接口Serial2/1/0收到IPv6报文*

\# 打开Router B上HDLC的ISIS报文调试信息开关，Router A和Router B两端都配置ISIS功能后，可查看到如下调试信息：

\<RouterB\> debugging hdlc isis in-out

\*Jan 31 09:55:49:015 2012 RouterB HDLC/7/ISIS: -MDC=1; Interface Serial2/1/0 received an ISIS packet. Length: 46, Address: 0x8F

*// 接口Serial2/1/0收到ISIS报文*

\*Jan 31 09:55:49:843 2012 RouterB HDLC/7/ISIS: -MDC=1; Interface Serial2/1/0 sent an ISIS packet. Length: 40, Address: 0x8F

*// 接口Serial2/1/0发送ISIS报文*

\# 打开Router B上HDLC的keepalive报文调试信息开关，由于当前链路UP，keepalive机制已启动，可查看到如下调试信息：

\<RouterB\> debugging hdlc keepalive in-out

\*Jan 30 17:18:42:328 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 received a KEEPALIVE packet. Length: 22, Address: 0x8F

*// 接口Serial2/1/0收到keepalive报文*

\*Jan 30 17:18:42:328 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 received a KEEPALIVE_REQ packet. Length: 18, RemoteSeq: 830, AckedLocalSeq: 804

*// 接口Serial2/1/0收到keepalive请求报文*

\*Jan 30 17:18:48:610 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 sent

a KEEPALIVE_REQ packet. Length: 18, LocalSeq: 804, AckedRemoteSeq: 830, line UP

*// 接口Serial2/1/0发送keepalive请求报文*

\*Jan 30 17:18:48:610 2012 RouterB HDLC/7/KEEPALIVE: -MDC=1; Interface Serial2/1/0 sent a

KEEPALIVE packet. Length: 22, Address: 0x8F

*// 接口Serial2/1/0发送keepalive报文*

\# 打开Router B上HDLC的MPLS报文调试信息开关，Router A和Router B两端都配置MPLS功能后，可查看到如下调试信息：

\<RouterB\> debugging hdlc mpls in

\*Jan 31 10:02:31:432 2012 RouterB HDLC/7/MPLS: -MDC=1; Interface Serial2/1/0 received an MPLS packet. Length: 92, Address: 0x0F

*// 接口Serial2/1/0收到MPLS报文*

**HDLC \-- HDLC链路捆绑调试命令 \-- debugging bundle**

------------------------------------------------------------------------

**[debugging bundle**]命令用来打开HDLC捆绑接口调试信息开关。

**[undo debugging bundle**]命令用来关闭HDLC捆绑接口调试信息开关。

【命令】

**[debugging bundle**  { **all** \| **error** \| **event** \| **packet** } [ **hdlc-bundle** *bundle-id* ]]

**[undo debugging bundle**  { **all** \| **error** \| **event** \| **packet** } [ **hdlc-bundle** *bundle-id* ]]

【缺省情况】

HDLC捆绑接口调试信息开关处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

**[hdlc-bundle**] *bundle-id*：显示指定HDLC捆绑接口的调试信息。*bundle-id*表示HDLC捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定本参数，将显示所有HDLC捆绑接口的调试信息。

【使用指导】

表1-7 debugging bundle error命令输出信息描述表

字段

描述

Failed to execute the *operation* on interface *interface-name*.

接口*interface-name*上执行*operation*操作失败，*operation*的取值及其含义如下：

·active：接口激活

·deactive：接口去激活

·create：接口创建

·delete：接口删除

·link_up：接口链路up

·link_down：接口链路down

·shutdown：接口shutdown

·undo_shutdown：接口undo shutdown

·speed_change：接口速率变化

Failed to block member *interface-name.*

阻塞成员接口*interface-name*失败

Failed to unblock member *interface-name.*

去阻塞成员接口*interface-name*失败

表1-8 debugging bundle event命令输出信息描述表

字段

描述

Received event *event* on interface *interface-name*.

接口*interface-name*收到*event*事件，*event*包括以下几种：

·active：接口激活事件

·deactive：接口去激活事件

·create：接口创建事件

·delete：接口删除事件

·link_up：接口链路up事件

·link_down：接口链路down事件

·shutdown：接口shutdown事件

·undo_shutdown：接口undo shutdown事件

Received a speed-change event on interface *interface-name* (new speed: *speed*).

接口*interface-name*速率变化，新速率为*speed*

Interface *interface-name* started rechoosing Selected interfaces.

HDLC捆绑接口*interface-name*开始重新选择选中接口

Interface *interface-name* succeeded in rechoosing Selected interfaces and sent the rechoosing result to the kernel.

HDLC捆绑接口*interface-name*重新选择选中接口成功，开始把重选结果下内核

Succeeded in blocking member *interface-name*.

阻塞成员接口*interface-name*成功

Succeeded in unblocking member *interface-name*.

去阻塞成员接口*interface-name*成功

表1-9 debugging bundle packet命令输出信息描述表

字段

描述

*[bundle-name* sent a packet out of member *interface-name* (packet length: *length*). *packet context*]

HDLC捆绑接口*bundle-name*从成员接口*interface-name*发送报文，报文长度为*length*。报文内容为*packet context*

*[bundle-name* received a packet on member *interface-name* (packet length: *length*). *packet context*]

HDLC捆绑接口*bundle-name*从成员接口*interface-name*接收报文，报文长度为*length*。报文内容为*packet context*

Sent a packet to slot *slot-num* cpu *cpu-id*.

发送一个报文到指定板的指定CPU，目的板号为*slot-num*，目的CPU编号为*cpu-id*

【举例】

\# 打开HDLC捆绑接口错误调试信息开关。当接口POS2/2/1变为选中成员接口下驱动去阻塞失败时会输出下列调试信息。

\<Sysname\> debugging bundle error

\*Jan 30 17:18:48:610 2012 Sysname BUNDLE/7/ERROR: -MDC=1; Failed to unblock member POS2/2/1.

*// 去阻塞成员接口POS2/2/1失败*

\# 打开HDLC捆绑接口1的事件调试信息开关。将HDLC捆绑接口1 **shutdown**时会输出下列调试信息。

\<Sysname\> debugging bundle event hdlc-bundle 1

\*Jan 30 18:18:48:610 2012 Sysname BUNDLE/7/EVENT: -MDC=1; Received event shutdown on interface HDLC-bundle1.

*[// HDLC*]*捆绑接口1发生shutdown事件*

\# 设备上配置了HDLC捆绑1，HDLC捆绑1中有选中成员接口POS2/2/1。打开HDLC捆绑接口报文调试信息开关。当在设备上ping其他设备时会输出下列调试信息。

\<Sysname\> debugging bundle packet hdlc-bundle 1

\*Jan 30 19:18:48:610 2012 Sysname BUNDLE/7/PACKET: -MDC=1; HDLC-bundle1 sent a packet out of member POS2/2/1 (packet length: 88).

    0f 00 08 00 45 00 00 54 00 20 00 00 ff 01 b7 84

    01 01 01 01 01 01 01 02 08 00 74 35 08 00 01 00

    da 87 76 00 00 00 00 00 00 01 02 03 04 05 06 07

    08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17

    18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25 26 27

    28 29 2a 2b 2c 2d 2e 2f

*[// HDLC*]*捆绑接口1发送报文，报文的长度为88，发送报文的成员接口为POS2/2/1*

