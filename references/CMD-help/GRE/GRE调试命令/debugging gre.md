
**GRE \-- GRE调试命令 \-- debugging gre**

------------------------------------------------------------------------

【命令】

**[debugging gre**[ { **all** \| **error** \| **packet** } [ **interface** { **evi-link** \| **tunnel** } *interface-number* ]]]

**[undo debugging gre**[ { **all** \| **error** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示GRE所有调试信息开关。

**[error**]：表示GRE错误调试信息开关。

**[packet**]：表示GRE报文调试信息开关。

**[interface evi-link** *interface-number*]：表示指定EVI-Link接口进行调试。

**[interface tunnel** *interface-number*]：表示指定Tunnel接口进行调试。

【描述】

**[debugging gre**]命令用来打开GRE的调试信息开关。**undo debugging gre**命令用来关闭GRE的调试信息开关。

缺省情况下，GRE的调试信息开关处于关闭状态。

表1-1 debugging gre error命令输出信息描述表

字段

描述

Tunnel*num* status check: Source address is not set.

隧道Tunnel*num*状态检查：源地址没有配置

Tunnel*num* status check: Destination address is not set.

隧道Tunnel*num*状态检查：目的地址没有配置

Tunnel*num* status check: Source address is not the address of a local interface.

隧道Tunnel*num*状态检查：源地址不是本设备接口的地址

Tunnel*num* status check: Failed to get FIB information of the source address.

隧道Tunnel*num*状态检查：获取源地址FIB信息失败

Tunnel*num* status check: Destination address should not be the address of a local interface.

隧道Tunnel*num*状态检查：目的地址不能是本设备接口的地址

Tunnel*num* status check: Failed to get FIB information of the destination address.

隧道Tunnel*num*状态检查：获取目的地址FIB信息失败

GRE version error.

GRE报文版本号错误

GRE routing is not supported.

不支持GRE Routing域

Invalid GRE packet.

非法的GRE报文

The local and peer GRE keys do not match.

本地和对端的GRE key不相同

GRE key at the local end of the tunnel is not set.

本地隧道没有配置GRE key

GRE key at the peer end of the tunnel is not set.

对端隧道没有配置GRE key

The protocol state of Tunnel*num* is not up. Dropped the packet.

待解封装报文出隧道时发现相应隧道接口协议状态不是up的，报文被丢弃

Tunnel*num*: The information obtained from the adjacency table is invalid.

隧道Tunnel*num*：邻接表信息非法

Tunnel*num*: The passenger protocol number *number* is not supported.

隧道Tunnel*num*：不支持乘客协议*number*

Failed to forward the IPv4 packet.

加封装后的IPv4报文发送失败

Failed to forward the IPv6 packet.

加封装后的IPv6报文发送失败

No tunnel in the physical state of up was found for the packet. Dropped the packet.

对出隧道报文进行解封装时，找不到对应的隧道接口，报文被丢弃

表1-2 debugging gre packet命令输出信息描述表

字段

描述

Successfully added a GRE header.

添加GRE头成功

The checksum flag of the packet is set.

此报文含有checksum标志

Tunnel*num*: Send a keepalive packet.

隧道Tunnel*num*：发送keepalive报文

Tunnel*num* packet: After de-encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*报文处理：解封装后，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: After encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*报文处理：加封装后，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Fast forwarded the encapsulated packet.

快速转发加封装后的报文

Failed to fast forward the encapsulated packet.

快速转发加封装后的报文失败

Tunnel*num* packet: Before encapsulation according to fast-forwarding table,

*[source*-\>*destination* (length = *length*)]

隧道Tunnel*num*报文处理：根据快转表加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before de-encapsulation according to fast-forwarding table, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*报文处理：根据快转表解封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num* packet: Before encapsulation, *source*-\>*destination* (length = *length*)

隧道Tunnel*num*报文处理：加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Before de-encapsulation, *source*-\>*destination* (length = *length*)

解封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Tunnel*num*: Received a keepalive packet.

隧道Tunnel*num*：收到keepalive回应报文，说明对端可达

Tunnel*num* packet: Before encapsulation according to adjacency table,

*[source*-\>*destination* (length = *length*)]

隧道Tunnel*num*报文处理：根据邻接表加封装前，报文头源地址为*source*，目的地址为*destination*，报文长度为*length*

Discarded compatible address packet.

丢弃含有IPv4兼容IPv6地址的IPv6报文

【举例】

\# 打开本端的GRE错误调试信息开关。创建隧道接口，没有配置源地址时，出现如下调试信息。

\<Sysname\> debugging gre error

\*Nov 17 09:16:07:928 2010 Sysname GRE/7/error: -MDC=1;

 Tunnel1 status check: Source address is not set.

*// 隧道Tunnel1状态检查：没有配置源地址*

\# 打开本端的GRE报文调试信息开关。在两台设备之间建立GRE over IPv4隧道，并分别配置参数使隧道接口up。在本端设备上ping对端设备，本端设备上将打印如下调试信息。

\<Sysname\> debugging gre packet

\<Sysname\> ping -c 1 -a 10.1.1.1 10.1.3.1

PING 10.1.3.1 (10.1.3.1) from 10.1.1.1: 56 data bytes

56 bytes from 10.1.3.1: icmp_seq=0 ttl=255 time=1.000 ms

\-\-- 10.1.3.1 ping statistics \-\--

1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss

round-trip min/avg/max/stddev = 1.000/1.000/1.000/0.000 ms

\<Sysname\>

\*Sep  6 11:49:46:052 2011 Sysname GRE/7/packet: -MDC=1;

 Tunnel0 packet: Before encapsulation according to adjacency table,

   10.1.1.1-\>10.1.3.1 (length = 84)

*// 根据邻接表加封装前，报文的源IP地址为10.1.1.1，目的IP地址为10.1.3.1，报文长度为84字节*

\*Sep  6 11:49:46:052 2011 Sysname GRE/7/packet: -MDC=1;

 Tunnel0 packet: After encapsulation,

   1.1.1.1-\>1.1.1.2 (length = 108)

*// 加封装后，报文的源IP地址为1.1.1.1，目的IP地址为1.1.1.2，报文长度为108字节*

\*Sep  6 11:49:46:052 2011 Sysname GRE/7/packet: -MDC=1;

 Tunnel0 packet: Failed to fast forward the encapsulated packet.

*// 没有找到封装后报文对应的快速转发表项，快速转发失败*

\*Sep  6 11:49:46:053 2011 Sysname GRE/7/packet: -MDC=1;

 Before de-encapsulation,

   1.1.1.2-\>1.1.1.1 (length = 108)

*// 接收到的报文解封装前，源IP地址为1.1.1.2，目的IP地址为1.1.1.1，报文长度为108字节*

\*Sep  6 11:49:46:053 2011 Sysname GRE/7/packet: -MDC=1;

 Tunnel0 packet: After de-encapsulation,

   10.1.3.1-\>10.1.1.1 (length = 84)

*// 接收到的报文解封装后，源IP地址为10.1.3.1，目的IP地址为10.1.1.1，报文长度为84字节*
