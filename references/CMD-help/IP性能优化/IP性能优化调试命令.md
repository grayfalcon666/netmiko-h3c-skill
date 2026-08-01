<!-- CMD-INDEX
  debugging ip error                  | 用户视图             | L14
  debugging ip icmp                   | 用户视图             | L90
  debugging ip packet                 | 用户视图             | L200
  debugging ip virtual-reassembly     | 用户视图             | L362
  debugging rawip packet              | 用户视图             | L490
  debugging tcp-proxy                 | 用户视图             | L654
  debugging tcp event                 | 用户视图             | L1076
  debugging tcp nsr                   | 用户视图             | L1218
  debugging tcp packet                | 用户视图             | L1602
  debugging udp packet                | 用户视图             | L1758
-->

**IP性能优化 \-- IP性能优化调试命令 \-- debugging ip error**

------------------------------------------------------------------------

【命令】

**[debugging ip error**]

**[undo debugging ip error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging** **ip error**]命令用来打开IP转发错误调试信息开关。**undo debugging** **ip error**命令用来关闭IP转发错误调试信息开关。

缺省情况下，IP转发错误调试信息开关处于关闭状态。

表1-1 debugging ip error命令输出信息描述表

字段

描述

The number of queues of reassemble is MAX!

重组队列数目超过了总的重组队列数目

The queue of reassemble is full!

重组队列中分片数目超过了最大值

Reassemble Failed!

重组失败

Get Interface CB failed!

从接口管理获取转发控制块失败

Release MBUF! Phase Num is *num*, Service ID is *id*, Bitmap is *%#lx*!

业务释放报文，业务阶段、顺序号、以及当前业务掩码位

MPLS Ping/Trrt: Can\'t get the route!

LSP Ping/Traceroute等操作查询转发表失败

Broadcast NOT allowed to be forwarded!

不允许出接口子网广播报文转发

Error interface is assigned!

上层指定了错误的发送接口

【举例】

\# 打开IP转发错误调试信息开关。

\<Sysname\> debugging ip error

%Jun 29 11:48:17:939 2011 Sysname IPFW/3/IPFW_ERROR: -MDC=1;

Broadcast NOT allowed to be forwarded!

*// 出接口没有使能子网广播转发，转发报文被丢弃*

**IP性能优化 \-- IP性能优化调试命令 \-- debugging ip icmp**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging ip icmp**]

**[undo debugging ip icmp**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging ip icmp** \****[slot ***slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging ip icmp** \****[slot ***slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging ip icmp** \****[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging ip icmp** \****[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ICMP调试信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的ICMP调试信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ICMP调试信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备的ICMP调试信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ICMP调试信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX的ICMP调试信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的ICMP调试信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的ICMP调试信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ICMP调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的ICMP调试信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的ICMP调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【描述】

**[debugging** **ip icmp**]命令用来打开ICMP调试信息开关。**undo debugging** **ip icmp**命令用来关闭ICMP调试信息开关。

缺省情况下，ICMP调试信息开关处于关闭状态。

表1-2 debugging ip icmp命令输出信息描述表

字段

描述

ICMP Output

发送报文的操作

ICMP Input

接收报文的操作

type

ICMP报文类型

code

ICMP报文代码

src

报文源地址

dst

报文目的地址

【举例】

\# 打开ICMP的调试信息开关。对端ping本设备时，本设备会输出下列调试信息。

\<Sysname\> debugging ip icmp

\*Feb  8 18:28:47:417 2011 Sysname SOCKET/7/ICMP:

ICMP Input:

 ICMP Packet: src = 192.168.20.14, dst = 192.168.20.13

              type = 8, code = 0 (echo)

*// 接收ICMP请求报文，报文源IP地址为192.168.20.14，报文目的IP地址为192.168.20.13*

\*Feb  8 18:28:47:451 2011 Sysname SOCKET/7/ICMP:

ICMP Output:

 ICMP Packet: src = 192.168.20.13, dst = 192.168.20.14

              type = 0, code = 0 (echo-reply)

*// 发送ICMP应答报文，报文源IP地址为192.168.20.13，报文目的IP地址为192.168.20.14*

**IP性能优化 \-- IP性能优化调试命令 \-- debugging ip packet**

------------------------------------------------------------------------

【命令】

**[debugging ip packet ** **acl** *acl-number* ]

**[undo debugging ip packet**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl **]*acl-number*：输出通过指定访问控制列表过滤的IP报文调试信息，取值范围为2000～3999。

【描述】

**[debugging** **ip packet**]命令用来打开IP报文调试信息开关。**undo debugging** **ip packet**命令用来关闭IP报文调试信息开关。

缺省情况下，IP报文调试信息开关处于关闭状态。

表1-3 debugging ip packet命令输出信息描述表

字段

描述

Sending

发送报文的操作

Receiving

接收报文的操作

Delivering

IP层将报文送到上层

interface

接收/发送报文的接口

version

IP协议版本号

headlen

报文首部长度

tos

服务类型

pktlen

报文总长度

pktid

标识

offset

片偏移

ttl

生存时间

protocol

协议域

checksum

首部校验和

s

报文源地址

d

报文目的地址

Sending the packet from local at *interface-type interface-number*

从本地接口发送报文

Receiving IP packet from *interface-type interface-number*

从接口接收到报文

IP packet is delivering up!

将接收的报文送到上层处理

【举例】

\# 打开IP报文的调试信息开关，并执行ping操作。

\<Sysname\> debugging ip packet

\<Sysname\> ping --c 1 10.1.1.2

Ping 10.1.1.2: 56  data bytes, press CTRL_C to break

\*Aug  3 05:12:33:619 2011 Sysname IPFWD/7/IPFW_PACKET:

Sending, interface = GigabitEthernet1/0/1, version = 4, headlen = 20, tos = 0,

pktlen = 84, pktid = 36756, offset = 0, ttl = 255, protocol = 1,

checksum = 5648, s = 10.1.1.1, d = 10.1.1.2

prompt: Sending the packet from local at GigabitEthernet1/0/1

*// 从本地接口GigabitEthernet1/0/1发送报文*

\*Aug  3 05:12:33:621 2011 Sysname IPFWD/7/IPFW_PACKET:

Receiving, interface = GigabitEthernet1/0/1, version = 4, headlen = 20, tos = 0,

pktlen = 84, pktid = 7751, offset = 0, ttl = 255, protocol = 1,

checksum = 34653, s = 10.1.1.2, d = 10.1.1.1

prompt: Receiving IP packet from GigabitEthernet1/0/1

*// 从接口GigabitEthernet1/0/1接收到报文*

\*Aug  3 05:12:33:622 2011 Sysname IPDBG/7/IPFW_PACKET:

Delivering, interface = GigabitEthernet1/0/1, version = 4, headlen = 20, tos = 0,

pktlen = 84, pktid = 7751, offset = 0, ttl = 255, protocol = 1,

checksum = 34653, s = 10.1.1.2, d = 10.1.1.1

prompt: IP packet is delivering up!

*// 将接收的报文送到上层处理*

Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=5.000 ms

\-\-- Ping statistics for 10.1.1.2 \-\--

1 packet(s) transmitted, 1 packet(s) received, 0.00% packet loss

round-trip min/avg/max/std-dev = 5.000/5.000/5.000/5.000 ms   

**IP性能优化 \-- IP性能优化调试命令 \-- debugging ip virtual-reassembly**

------------------------------------------------------------------------

【命令】

**[debugging ip virtual-reassembly**]

**[undo debugging ip virtual-reassembly**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ip virtual-reassembly**]命令用来打开IP虚拟分片重组调试信息开关。**undo debugging ip virtual-reassembly**命令用来关闭IP虚拟分片重组调试信息开关。

缺省情况下，IP虚拟分片重组调试信息开关处于关闭状态。

表1-4 debugging ip virtual-reassembly命令输出信息描述表

字段

描述

VFR_rcv: Fragment

收到VFR分片报文

target_ip_addr

目的IP地址

sender_ip_addr

源IP地址

ID

数据报文标识字段

offset

偏移量

len

分片报文长度

VFR_operation

VFR操作

Created frag queue (success)

创建分片队列（成功）

Created frag queue (failure).

创建分片队列（失败）

Packet reassembly incompleted (Offset: *offset*). Waiting to receive the rest fragments.

报文未完成，偏移量为*offset*，等待接收

Packet reassembly completed.

报文重组完成

Frag queue deleted. Drop this fragment.

分片队列已删除，丢弃此分片报文

【举例】

\# 在报文的入接口配置IP虚拟分片重组功能，并打开IP虚拟分片重组调试信息开关，当接口收到分片报文时，打印如下调试信息。

\<Sysname\> debugging ip virtual-reassembly

\<Sysname\> ping --c 1 --s 3000 10.1.1.1

\*Jun 25 14:49:32:851 2012 Sysname IPVFR/7/IPVFR_DEBUG_COMMON:

VFR_rcv: Fragment, target_ip_addr: 10.1.1.1, sender_ip_addr: 10.1.1.2, ID: 54, offset: 0, len: 1500.

*// 收到一个VFR分片请求报文，目的IP地址为10.1.1.1，源IP地址为10.1.1.2，标识为54，偏移量为0，报文长度为1500*

\*Jun 25 14:49:32:851 2012 Sysname{.TerminalDisplayChar} IPVFR/7/IPVFR_DEBUG_COMMON:

VFR_operation: Created frag queue (success).

*[// VFR*]*操作，创建一个分片队列（成功）*

\*Jun 25 14:49:32:851 2012 Sysname{.TerminalDisplayChar} IPVFR/7/IPVFR_DEBUG_COMMON:

VFR_operation: Packet reassembly incompleted (Offset: 0). Waiting to receive the rest fragments.

*[// VFR*]*操作，报文未完成，偏移量为0，等待接收其他分片报文*

\*Jun 25 14:49:32:851 2012 Sysname{.TerminalDisplayChar} IPVFR/7/IPVFR_DEBUG_COMMON:

VFR_rcv: Fragment, target_ip_addr: 10.1.1.1, sender_ip_addr: 10.1.1.2, ID: 54, offset: 1480, len: 548.

*// 收到一个VFR分片报文，目的IP地址为10.1.1.1，源IP地址为10.1.1.2，标识为54，偏移量为1480，报文长度为548*

\*Jun 25 14:49:32:852 2012 Sysname{.TerminalDisplayChar} IPVFR/7/IPVFR_DEBUG_COMMON:

VFR_operation: Packet reassembly completed.

*[// VFR*]*操作，报文重组完成*

Ping 10.1.1.1 (10.1.1.1): 3000 data bytes, press CTRL_C to break

3000 bytes from 10.1.1.1: icmp_seq=0 ttl=255 time=3.000 ms

\-\-- Ping statistics for 10.1.1.1 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 1.000/2.400/4.000/1.200 ms

**IP性能优化 \-- IP性能优化调试命令 \-- debugging rawip packet**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging** **rawip packet** [ **acl** *acl-number* ]]

**[undo debugging** **rawip packet**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging** **rawip packet** [ **acl** *acl-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging** **rawip packet** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging** **rawip packet** [ **acl** *acl-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging** **rawip packet** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl** *acl-number*]：输出通过指定访问控制列表过滤的IP报文调试信息，取值范围为[2000～3999。]

**[slot ***slot-number*]：显示指定单板的RawIP报文调试信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的RawIP报文调试信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的RawIP报文调试信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的RawIP报文调试信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的RawIP报文调试信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的RawIP报文调试信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的RawIP报文调试信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的RawIP报文调试信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的RawIP报文调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的RawIP报文调试信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的RawIP报文调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【描述】

**[debugging** **rawip packet**]命令用来打开RawIP报文调试信息开关。**undo debugging** **rawip packet**命令用来关闭RawIP报文调试信息开关。

缺省情况下，RawIP报文调试信息开关处于关闭状态。

表1-5 debugging rawip packet命令输出信息描述表

字段

描述

RawIP Input

接收报文

RawIP Output

发送报文

IN VRF

报文入VRF

OUT VRF

报文出VRF

IN IF

报文入接口

src

报文源地址

dst

报文目的地址

headlen

IP头部长度

tos

服务类型

ttl

生存时间

proto

协议类型

len

RawIP报文长度

id

报文序号

offset

偏移

【举例】

\# 打开RawIP报文调试信息开关，ping对端设备时打印如下调试信息。

\<Sysname\> debugging rawip packet

\<Sysname\> ping -c 1 192.168.20.14

Ping 192.168.20.14 (192.168.20.14): 56 data bytes, press CTRL_C to break

\*Feb  8 23:42:42:161 2011 Sysname SOCKET/7/RAWIP:

RawIP Output:

 OUT VRF = 0

 IP Packet: src = 0.0.0.0, dst = 192.168.20.14

            headlen = 1, tos = 0, ttl = 255, proto = 1

            len = 84, id = 65535, offset = 0

*// 发送RawIP报文*

\*Feb  8 23:42:42:161 2011 Sysname SOCKET/7/RAWIP:

RawIP Input:

 IN VRF = 0, IN IF = GigabitEthernet1/0/1

 IP Packet: src = 192.168.20.14, dst = 192.168.20.13

            headlen = 5, tos = 0, ttl = 128, proto = 1

            len = 64, id = 30752, offset = 0

*// 接收RawIP报文*

64 bytes from 192.168.20.14: icmp_seq=0 ttl=128 time=0.188 ms

\-\-- Ping statistics for 192.168.20.14 \-\--

1 packets transmitted, 1 packets received, 0.0% packet loss

round-trip min/avg/max/std-dev = 0.188/0.188/0.188/0.000 ms

**IP性能优化 \-- IP性能优化调试命令 \-- debugging tcp-proxy**

------------------------------------------------------------------------

【命令】

**[debugging**[ **tcp-proxy** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

**[undo**[ **debugging** **tcp-proxy** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示TCP代理的所有调试信息开关。

**[error**]：表示TCP代理的错误调试信息开关。

**[event**]：表示TCP代理的事件调试信息开关。

**[fsm**]：表示TCP代理的状态机调试信息开关。

**[packet**]：表示TCP代理的报文调试信息开关。

【描述】

**[debugging** **tcp-proxy**]命令用来打开TCP代理的调试信息开关。**undo** **debugging** **tcp-proxy**命令用来关闭TCP代理的调试信息开关。

缺省情况下，TCP代理的调试信息开关处于关闭状态。

本命令用来打开IPv4 TCP和IPv6 TCP代理的调试信息开关。

表1-6 debugging tcp-proxy error命令输出信息描述表

字段

描述

*addressport*

地址端口信息：

·*sip*/*sport* \--\> *dip*/*dport*：发起方IPv4/IPv6地址/端口号*sip*/*sport*，响应方IPv4/IPv6地址/端口号*dip*/*dport*

·*sip*/*sport -*-\> None：发起方IPv4/IPv6地址/端口号*sip*/*sport*，无响应方

·initial：未指定地址和端口号

 

Failed to connect to IPv4/IPv6* sip*/*sport* on handle \*[addressport*.]

应用程序用句柄（地址端口信息为*addressport*）向IPv4/IPv6的源IP*sip*/源端口*sport*发起连接失败

 

Failed to create new packet for data of *datalen* bytes due to insufficient memory.

由于内存不足，导致创建*datalen*字节的报文失败

 

Failed to erase *overlaplen* bytes of overlapping data from packet

从报文中擦除*overlaplen*字节的重叠数据失败

 

Failed to create TCP proxy data block due to insufficient memory.

由于内存不足，导致创建TCP代理数据信息失败

 

Failed to send SYN ACK packet.

发送SYN ACK报文失败

 

Can\'t find listening TCP proxy data block for server/client *addressport*.

无法找到服务器/客户端（地址端口信息为*addressport*）的TCP代理监听数据信息

 

Server/Client *addressport* is unable to process *event* event in *state* state.

服务器/客户端（地址端口信息为*addressport*）的不能在状态*state*下处理*event*事件

 

Failed to create data packet on server/client*addressport*.

服务器/客户端（地址端口信息为*addressport*）创建报文失败

 

Failed to send packet.

发送报文失败

 

 TCP packet: src=*sip*/*sport*, dst=*dip*/*dport*

             seq=*seqnum*, ack=*acknum*, flag=*flag*

             win=*winsize*, checksum=*checksum*, datalen=*datalen*, headlen=*headlen*.

TCP报文的信息：源IPv4/IPv6地址/端口号*sip*/*sport*，目的IPv4/IPv6地址/端口号*dip*/*dport*，序号*seqnum*，确认序号*acknum*，标志*flag*，窗口大小*winsize*，检验和*checksum*，数据长度*datalen*，首部长度*headlen*

 

表1-7 debugging tcp-proxy event命令输出信息描述表

字段

描述

*addressport*

地址端口信息：

·*sip*/*sport* \--\> *dip*/*dport*：发起方IPv4/IPv6地址/端口号*sip*/*sport*，响应方IPv4/IPv6地址/端口号*dip*/*dport*

·*sip*/*sport -*-\> None：发起方IPv4/IPv6地址/端口号*sip*/*sport*，无响应方

·initial：未指定地址和端口号

 

Application has created a new handle.

应用程序已创建一个新句柄

 

Application is closing server/client *addressport*.

应用程序正在关闭一个服务器/客户端（地址端口信息为*addressport*）

 

Application is binding handle *addressport* to IPv4/IPv6* sip*/*sport*.

应用程序正在绑定句柄（地址端口信息为*addressport*）到IPv4/IPv6*sip*/*sport*

 

Application is connecting to IPv4/IPv6* sip*/*sport* on handle \*[addressport*.]

应用程序正在用句柄（地址端口信息为*addressport*）向IPv4/IPv6 *sip*/*sport*发起连接

 

Application set handle *addressport* to listening state.

应用程序设置句柄（地址端口信息为*addressport*）进入监听状态

 

Application accepted a new connection on handle *addressport*.

应用程序在句柄（地址端口信息为*addressport*）上获取了一个新连接

 

Application registered notification event on handle *addressport*.

应用程序在句柄（地址端口信息为*addressport*）上注册了通告事件

 

Application wanted *datalen* bytes of data, actually received *receivelen* bytes on handle *addressport*.

应用程序期望通过句柄（地址端口信息为*addressport*）接收*datalen*字节数据，实际接收*receivelen*字节

 

Foreign window on server/client *addressport* is not enough, declined to send 0 byte.

服务器/客户端（地址端口信息为*addressport*）的外部窗口大小不够，拒绝发送0字节数据

 

Application is sending *count* packets on server/client *addressport*.

应用程序正在通过客户端/服务器（地址端口信息为*addressport*）发送*count*个报文

 

Application received *count* packets on server/client *addressport*.

应用程序通过客户端/服务器（地址端口信息为*addressport*）接收*count*个报文

 

Server/Client *addressport* received a retransmitted packet and ignored it.

服务器/客户端（地址端口信息为*addressport*）收到重传报文，忽略此报文

 

*[Datalen *bytes of overlapping data has been erased from packet*t*]

应用程序已经从报文中擦除*datalen*字节重叠数据

 

Server/Client *addressport* submitted a pipe writable event to application.

服务器/客户端（地址端口信息为*addressport*）提交一个管道可写事件给应用程序

 

Application ignored a pipe writable event on server/client *addressport*.

应用程序忽略了句柄服务器/客户端（地址端口信息为*addressport*）上的一个管道可写事件

 

Server/Client *addressport* submitted *datalen* bytes of data to application.

服务器/客户端（地址端口信息为*addressport*）提交*datalen*字节数据给应用程序

 

Application ignored *datalen* bytes of data on server/client *addressport*.

应用程序忽略了句柄服务器/客户端（地址端口信息为*addressport*）上的*datalen*字节数据

 

Server/Client *addressport* state migrated: *state1* -\> *state2*.

服务器/客户端（地址端口信息为*addressport*）状态迁移：*state1*-\> *state2*

 

Server/Client *addressport* submitted a new connection to application.

服务器/客户端（地址端口信息为*addressport*）向应用程序提交一个新连接

 

Application ignored a new connection on server/client *addressport*.

应用程序忽略了句柄服务器/客户端（地址端口信息为*addressport*）上的一个新连接

 

Server/Client *addressport* submitted a disconnection event to application.

服务器/客户端（地址端口信息为*addressport*）向应用程序提交一个连接关闭事件

 

Application ignored a disconnection event on server/client *addressport*.

应用程序忽略一个来自服务器/客户端（地址端口信息为*addressport*）的连接关闭事件

 

Server/Client *addressport* window size is not enough. Stopped sending packet.

服务器/客户端（地址端口信息为*addressport*）的窗口尺寸不足，停止发送报文

 

表1-8 debugging tcp-proxy fsm命令输出信息描述表

字段

描述

*addressport*

地址和端口的信息：

·*sip*/*sport* \--\> *dip*/*dport*：发起方IPv4/IPv6地址/端口号*sip*/*sport*，响应方IPv4/IPv6地址/端口号*dip*/*dport*

·*sip*/*sport -*-\> None：发起方IPv4/IPv6地址/端口号*sip*/*sport*，无响应方

·initial：未指定地址和端口号

 

Server/Client *addressport* before/after FSM processed *event*

 Info: seq=*expectsendseq*, ack=*expectsendack*, sent ack=*alreadysendack*, received ack=*foreignack*, lwin=*localwin*, fwin=*foreignwin*

 State: *state*.

服务器/客户端（地址端口信息为*addressport*）在状态机处理*event*事件前/后的信息：

本端下次发送的起始序号*expectsendseq*，本端期待发送的确认号*expectsendack*，本端已发出的确认号*alreadysendack*，对端已确认的数据*foreignack*，本端当前窗口大小*localwin*，对端最后一次有效报文通告的窗口大小*foreignwin*，状态*state*。其中：

*[event*]包括：

·SYN

·SYNACK

·FIN

·ACK

·RST

·NONE

·TIMEOUT

*[state*]包括：

·CLSD

·LSTN

·SYNSND

·SYNRCV

·EST

·CLSWT

·FINWT1

·CLSNG

·LSTACK

·FINWT2

·TMWT

 

表1-9 debugging tcp-proxy packet命令输出信息描述表

字段

描述

Received a disordered packet, expected seq=*expectseq*, packet seq=*packetseq*.

收到一个乱序报文，期待的序号*expectseq*，报文实际的序号*packetseq*

Input packet: Time=*time*, total length=*len*

接收报文的时间*time*，报文总长度*len*

Output packet: Time=*time*, total length=*len*

发送报文的时间*time*，报文总长度*len*

Processing disordered packet *packet*

处理乱序报文，报文信息为*packet*

 TCP packet: src=*sip*/*sport*, dst=*dip*/*dport*

             seq=*seqnum*, ack=*acknum*, flag=*flag*

             win=*winsize*, checksum=*checksum*, datalen=*datalen*, headlen=*headlen*

TCP报文的信息：源IPv4/IPv6地址/端口号*sip*/*sport*，目的IPv4/IPv6地址/端口号*dip*/*dport*，序号*seqnum*，确认序号*acknum*，标志*flag*，窗口大小*winsize*，检验和*checksum*，数据长度*datalen*，首部长度*headlen*

【举例】

\# 打开TCP代理错误调试信息开关。

\<Sysname\> debugging tcp-proxy error

\*Jan 16 09:29:23:045 2014 Sysname TCPP/7/FSM: Failed to send packet.

*// 发送报文失败*

\# 打开TCP代理事件调试信息开关。

\<Sysname\> debugging tcp-proxy event

\*Jan 16 09:29:23:075 2014 Sysname TCPP/7/EVENT: -MDC=1; Application is closing client [192.168.1.10/80\--\>192.168.1.11/45457.]

*// 应用程序正在关闭一个客户端（源IP地址/端口号192.168.1.10/80\--\>目的IP地址/端口号192.168.1.11/45457）*

\# 打开TCP代理状态机调试信息开关。

\<Sysname\> debugging tcp-proxy fsm

\*Jan 16 09:29:23:076 2014 Sysname TCPP/7/FSM: -MDC=1; Server [192.168.1.10:80\--\>192.168.1.11:45457 before FSM processed ACK]

 Info: seq=0x00b4cc08, ack=0x0e4cbe56, sent ack=0x0e4cbe56, received ack=0x00b4cc07, lwin=65535, fwin=64800

 State: FINWAIT1.

*// 服务器（本端IP地址/端口号192.168.1.10/80\--\>对端IP地址/端口号192.168.1.11/45457）在状态机处理ACK事件前的信息：本端下次发送的起始序号0x00b4cc08，本端期待发送的确认号0x0e4cbe56，本端已发出的确认号0x0e4cbe56，对端已确认的数据0x00b4cc07，本端当前窗口大小65535，对端最后一次有效报文通告的窗口大小64800，状态FINWAIT1*

\# 打开TCP代理报文调试信息开关。

\<Sysname\> debugging tcp-proxy packet

\*Jan 16 09:29:25:089 2014 Sysname TCPP/7/PACKET: -MDC=1; Input packet: Time=4350167781, total length=572

 TCP packet: src=192.168.1.11/45457, dst=192.168.1.10/80

             seq=0x0e4cbe56, ack=0x00b4cc08, flag=0x18

             win=64800, checksum=0x9cc8, datalen=512, headlen=20

*// 接收报文的时间为4350167781，报文总长度为572。TCP报文的信息：源IP地址/端口号192.168.1.11/45457，目的IP地址/端口号192.168.1.10/80，序号0x0e4cbe56，确认序号0x00b4cc08，标志0x18，窗口大小64800，检验和0x9cc8，数据长度512，首部长度20*

**IP性能优化 \-- IP性能优化调试命令 \-- debugging tcp event**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging tcp event**]

**[undo debugging tcp event**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging tcp event** \****[slot ***slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging tcp event** \****[slot ***slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging tcp event** \****[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging tcp event** \****[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的TCP事件调试信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的TCP事件调试信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的TCP事件调试信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的TCP事件调试信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的TCP事件调试信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的TCP事件调试信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的TCP事件调试信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的TCP事件调试信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的TCP事件调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的TCP事件调试信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的TCP事件调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【描述】

**[debugging tcp event**]命令用来打开TCP事件调试信息开关。**undo debugging tcp event**命令用来关闭TCP事件调试信息开关。

缺省情况下，TCP事件调试信息开关处于关闭状态。

表1-10 debugging tcp event命令输出信息描述表

字段

描述

TCP timer(type = *timer*) restart, timeout = *time*.

TCP定时器启动事件信息

TCP timer(type = *timer*) now processing.

TCP定时器处理事件信息

TCP timer(type = *timer*) stop.

TCP定时器删除事件信息

TCP state change: *state1* \--\> *state2*.

TCP连接状态迁移信息

TCP received XXX packet.

TCP连接接收到FIN/RST报文

TCP send XXX packet.

TCP发送FIN/RST报文

Connect Info

连接信息

local

本地地址和端口信息

foreign

对端地址和端口信息

【举例】

\# 使能Telnet服务器功能。打开TCP事件调试信息开关。从其他设备使用Telnet功能登录到本设备，经过三次握手，建立连接。本设备的调试信息如下。

\<Sysname\> debugging tcp event

\*Feb  8 21:50:44:622 2011 Sysname SOCKET/7/TCP:

TCP state change: SYN_RCVD \--\> ESTABLISHED.

 Connect Info: local = 192.168.20.13:23, foreign = 192.168.20.14:4796.

*[// TCP*]*连接状态从SYN_RCVD*迁移到*ESTABLISHED。连接信息：本地地址为192.168.20.13，端口号为23；対端地址为192.168.20.14，端口号为4796*

\*Feb  8 21:50:44:623 2011 Sysname SOCKET/7/TCP:

TCP timer(type = KEEP) restart, timeout = 7200000.

 Connect Info: local = 192.168.20.13:23, foreign = 192.168.20.14:4796.

*// 启动Keep定时器*

\*Feb  8 21:50:45:223 2011 Sysname SOCKET/7/TCP:

TCP state change: ESTABLISHED \--\> FIN_WAIT_1.

 Connect Info: local = 192.168.20.13:23, foreign = 192.168.20.14:4796.

*[// TCP*]*连接关闭时，TCP连接状态从ESTABLISHED迁移到FIN_WAIT_1*

\*Feb  8 21:50:45:223 2011 Sysname SOCKET/7/TCP:

TCP Output: TCP send FIN packet.

 Connect Info: local = 192.168.20.13:23, foreign = 192.168.20.14:4796.

*[// TCP*]*发送FIN报文*

\*Feb  8 21:50:45:932 2011 Sysname SOCKET/7/TCP:

TCP state change: FIN_WAIT_1 \--\> FIN_WAIT_2.

 Connect Info: local = 192.168.20.13:23, foreign = 192.168.20.14:4796.

*// 接收到对端的应答后，TCP连接状态从FIN_WAIT_1迁移到FIN_WAIT_2*

**IP性能优化 \-- IP性能优化调试命令 \-- debugging tcp nsr**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging tcp nsr **[{ **all \| event *[\|]{.underline}* fsm \| msg** }]]

**[undo debugging tcp nsr **[{ **all** \| **event** \| **fsm** \| **msg** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging**[ **tcp nsr** { **all** \| **event** \| **fsm** \| **msg** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[undo debugging tcp nsr **[{ **all** \| **event** \| **fsm** \| **msg** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[debugging tcp nsr**[ { **all** \| **event** \| **fsm** \| **msg** } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

**[undo debugging tcp nsr **[{ **all** \| **event** \| **fsm** \| **msg** } [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：打开TCP NSR所有调试开关。

**[event**]：打开TCP NSR事件调试开关。

**[fsm**]：打开TCP NSR状态机运行调试开关。

**[msg**]：打开TCP NSR消息调试开关。

**[slot ***slot-number*]：显示指定单板的TCP NSR消息调试信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板的TCP NSR消息调试信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的TCP NSR消息调试信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的TCP NSR消息调试信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的TCP NSR消息调试信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的TCP NSR消息调试信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板TCP NSR消息调试信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的TCP NSR消息调试信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板TCP NSR消息调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的TCP NSR消息调试信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的TCP NSR消息调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【描述】

**[debugging** **tcp nsr**]命令用来打开TCP NSR消息调试信息开关。**undo debugging** **tcp nsr**命令用来关闭TCP NSR关闭消息调试信息开关。

缺省情况下，TCP NSR消息调试开关处于关闭状态。

表1-11 debugging tcp nsr msg命令输出信息描述表

字段

描述

Connection info

收发消息的连接信息

src

连接源地址和端口

dst

连接目的地址和端口

Sent an NSR enable message

发送nsr使能消息

Received an NSR enable message

收到nsr使能消息

Sent an NSR disable message

发送nsr去使能消息

Received an NSR disable message

收到nsr去使能消息

Sent an NSR inpcb slot change message

发送inpcb槽号切换消息

Received an NSR inpcb slot change message

收到inpcb槽号切换消息

Sent a pull message

发送数据请求

Received a pull message

接收到数据请求

Sent a ready message

TCP备份连接发送READY消息给TCP主连接

Received a ready message

TCP主连接收到TCP备份连接的READY消息

Sent brief data

发送TCP连接的简要数据信息

Received brief data

收到TCP连接的简要数据信息

rcvbuf

接收缓冲区大小

rcvcc

已接收数据字节数

initrcvseq

初始接收序号

undeliver

待上送给应用的第一个未读字节序号

rcvnext

待接收下一个字节序号

rcvwnd

接收窗口大小

sndbuf

发送缓冲区大小

sndcc

待发送数据字节数

initsndseq

初始发送序号

sndunack

已发送但未被对端确认的数据序号

sndmax

已发送数据的最大序号

sndnext

待发送下一个字节序号

sndwnd

发送窗口大小

congwnd

拥塞窗口大小

congthresh

慢启动门限

Sent packet

通过内部通道发送TCP报文数据

Received packet

通过内部通道接收TCP报文数据

Dropped packet

丢弃从内部通道收到的TCP报文数据

Packet info

报文内容片断

The connection was closed for FIN

连接被FIN报文丢弃

The packet was sent directly without any processing

报文被直接发送，没有其他任何处理方式

The packet was dropped because it was an ACK

纯ACK报文被直接丢弃

Appended data to sending buffer

向发送缓冲区增加数据

Dropped data from receiving buffer

从接收缓冲区重丢弃数据

Sent a command message

发送控制消息

Received a command message

接收控制消息

表1-12 debugging tcp nsr fsm命令输出信息描述表

字段

描述

Connection info

状态变化的连接信息

src

连接源地址和端口

dst

连接目的地址和端口

NSR state

TCP连接当前的NSR状态

Event

触发NSR状态变化的事件

表1-13 debugging tcp nsr event命令输出信息描述表

字段

描述

Connect Info

发生事件的连接信息

src

连接源地址和端口

dst

连接目的地址和端口

User set NSR

用户态进程设置连接的NSR开关

User set NSR standby slot

用户态进程设置连接的NSR备份板板号

User activated NSR connection

用户态进程激活NSR备份连接

【举例】

\# 打开TCP NSR消息调试开关。

\<Sysname\> debugging tcp nsr msg

*// 备份连接收到连接信息。*

\*Jan  3 04:42:03:434 2011 H3C SOCKET/7/TCP_NSR_MSG: -Slot=1;

Received brief data.

 Connection info: src = 13::2:20821, dst = 13::1:179.

*// 连接信息详情。*

\*Jan  3 04:42:03:436 2011 H3C SOCKET/7/TCP_NSR_MSG: -Slot=1;

Verbose info:

rcvbuf = 32844, rcvcc = 0, initrcvseq = 4144334050,

undeliver = 4145053342(719292), rcvnext = 4145053342(719292), rcvwnd = 32844

sndbuf = 32844, sndcc = 0, initsndseq = 418927020,sndunack = 419290042(363022),

sndmax = 419290042(363022), sndnext = 419290042(363022), sndwnd = 8192

congwnd = 2856, congthresh = 2856.

*// 连接发送数据报文。*

\*Jan  3 04:42:10:296 2011 H3C SOCKET/7/TCP_NSR_MSG: -Slot=1;

Sent packet, total length = 91.

 TCP packet: src = d::1/179, dst = d::2/20839

             seq = 3796013817, ack = 3594596379, flag =  PSH ACK

             window = 1024, checksum = 0x4e65, datalen = 19, headlen = 32

Packet info:

01 01 08 0a 10 52 d0 18 00 1d 71 d2 ff ff ff ff

ff ff ff ff ff ff ff ff ff ff ff ff 00 13 04

*// 连接接收数据报文。*

\*Jan  3 04:42:10:296 2011 H3C SOCKET/7/TCP_NSR_MSG: -Slot=2;

Received packet, total length = 91.

 TCP packet: src = 1::1/179, dst = 1::2/20833

             seq = 3304791859, ack = 1836562985, flag =  PSH ACK

             window = 1024, checksum = 0xe283, datalen = 19, headlen = 32

Packet info:

01 01 08 0a 10 52 d0 18 00 1d 4d 9b ff ff ff ff

ff ff ff ff ff ff ff ff ff ff ff ff 00 13 04

*[// NSR*]*主连接发送ENABLE消息。*

\*Jan  3 04:42:03:436 2011 H3C SOCKET/7/TCP_NSR_MSG: -Slot=2;

Sent NSR enable.

 Connection info: src = 12::2:20834, dst = 12::1:179.

\# 打开TCP NSR的事件调试开关。

\<Sysname\> debugging tcp nsr event

*// 用户态进程设置连接NSR使能。*

\*Jan  3 04:42:03:435 2011 H3C SOCKET/7/TCP_NSR_EVENT: -Slot=2; User set NSR enable. Connection info: src = 12::2:20834, dst = 12::1:179.

\# 打开TCP NSR的状态机运行调试开关。

\<Sysname\> debugging tcp nsr fsm

*[// NSR*]*主连接在NSR CLOSE状态时发生SET事件。*

\*Jan  3 04:42:03:436 2011 H3C SOCKET/7/TCP_NSR_FSM: -Slot=2; NSR state: CLOSED(M), event: SET. Connection info: src = 12::2:20834, dst = 1

2::1:179.

*// 主连接进入ENABLED状态。*

\*Jan  3 04:42:03:437 2011 H3C SOCKET/7/TCP_NSR_FSM: -Slot=2; NSR state: ENABLED(M). Connection info: src = 12::2:20834, dst = 12::1:179.

**IP性能优化 \-- IP性能优化调试命令 \-- debugging tcp packet**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging** **tcp packet** [ **acl** *acl-number* ]]

**[undo debugging** **tcp packet**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging** **tcp packet** [ **acl** *acl-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging** **tcp packet** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging** **tcp packet** [ **acl** *acl-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging** **tcp packet** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl** *acl-number*]：输出通过指定访问控制列表过滤的IP报文调试信息，取值范围为2000～3999。

**[slot ***slot-number*]：显示指定单板的TCP报文调试信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的TCP报文调试信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的TCP报文调试信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的TCP报文调试信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的TCP报文调试信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备上的TCP报文调试信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的TCP报文调试信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的TCP报文调试信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的TCP报文调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的TCP报文调试信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的TCP报文调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【描述】

**[debugging** **tcp packet**]命令用来打开TCP报文调试信息开关。**undo debugging** **tcp packet**命令用来关闭TCP报文调试信息开关。

缺省情况下，TCP报文调试信息开关处于关闭状态。

表1-14 debugging tcp packet命令输出信息描述表

字段

描述

TCP Input

接收报文

TCP Synrespond

对SYN报文的回复报文

TCP Output

发送报文

state

TCP连接的当前状态

src

报文源地址

dst

报文目的地址

seq

报文序号

ack

报文确认序号

flag

标志位

window

接收和发送缓冲区大小

checksum

校验和

datalen

数据长度

headlen

TCP报文头部长度

【举例】

\# 使能Telnet服务器功能。打开TCP报文调试信息开关。从其他设备使用Telnet功能登录到本设备，本设备的调试信息如下。

\<Sysname\> debugging tcp packet

\*Feb  8 21:50:45:223 2011 Sysname SOCKET/7/TCP:

TCP Input(state = LISTEN):

 TCP Packet: src = 192.168.20.14:4796, dst = 192.168.20.13:23

             seq = 4162171040, ack = 0, flag =  SYN

             window = 65535, checksum = 0x0, datalen = 0, headlen = 28

*// 收到SYN报文，TCP连接的当前状态为LISTEN*

\*Feb  8 21:50:45:224 2011 Sysname SOCKET/7/TCP:

TCP Synrespond(state = SYN_RCVD):

 TCP Packet: src = 192.168.20.13:23, dst = 192.168.20.14:4796

             seq = 427493480, ack = 4162171041, flag =  SYN ACK

             window = 65535, checksum = 0xffd4, datalen = 0, headlen = 28

*// 发送SYN ACK报文，TCP连接的当前状态为SYN_RCVD*

\*Feb  8 21:50:45:324 2011 Sysname SOCKET/7/TCP:

TCP Input(state = LISTEN):

 TCP Packet: src = 192.168.20.14:4796, dst = 192.168.20.13:23

             seq = 4162171041, ack = 427493481, flag =  ACK

             window = 65535, checksum = 0x0, datalen = 0, headlen = 20

*// 收到ACK报文，TCP连接的当前状态为LISTEN*

**IP性能优化 \-- IP性能优化调试命令 \-- debugging udp packet**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging** **udp packet** [ **acl** *acl-number* ]]

**[undo debugging** **udp packet**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging** **udp packet** [ **acl** *acl-number*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging** **udp packet** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging** **udp packet** [ **acl** *acl-number*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo debugging** **udp packet** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[acl** *acl-number*]：输出通过指定访问控制列表过滤的IP报文调试信息，取值范围为2000～3999。

**[slot ***slot-number*]：显示指定单板的UDP报文调试信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的UDP报文调试信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的UDP报文调试信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的UDP报文调试信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备PEX的UDP报文调试信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备上的UDP报文调试信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的UDP报文调试信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的UDP报文调试信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的UDP报文调试信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的UDP报文调试信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU的UDP报文调试信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【描述】

**[debugging** **udp packet**]命令用来打开UDP报文调试信息开关。**undo debugging** **udp packet**命令用来关闭UDP报文调试信息开关。

缺省情况下，UDP报文调试信息开关处于关闭状态。

表1-15 debugging udp packet命令输出信息描述表

字段

描述

UDP Input

接收报文

UDP Output

发送报文

IN VRF

报文入VRF

OUT VRF

报文出VRF

IN IF

报文入接口

src

报文源地址和UDP源端口号

dst

报文目的地址和UDP目的端口号

len

UDP报文长度

checksum

校验和

【举例】

\# 不使能TFTP服务，打开UDP报文调试信息开关。对端使用TFTP客户端获取文件，因为服务器没有开启，拒绝服务。

\<Sysname\> debugging udp packet

\*Feb  8 23:33:10:534 2011 Sysname SOCKET/7/UDP:

UDP Input:

 IN VRF = 0, IN IF = GigabitEthernet1/0/1

 UDP Packet: src = 192.168.20.14:4849, dst = 192.168.20.13:69

             len = 26, checksum = 0x175f

*// 接收UDP报文*

\*Feb  8 23:33:10:534 2011 Sysname SOCKET/7/INET:

UDP Input: No PCB found, drop the packet.

*// 没有发现对应的五元组（因为没有启用TFTP服务），丢弃收到的UDP报文*

