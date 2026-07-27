<!-- CMD-INDEX
  debugging portal-proxy              | 用户视图             | L5
-->

**Portal代理 \-- Portal代理调试命令 \-- debugging portal-proxy**

------------------------------------------------------------------------

【命令】

**[debugging portal-proxy**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging portal-proxy **[ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示Portal代理的所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging portal-proxy**]命令用来打开Portal代理的调试信息开关。**undo debugging portal-proxy**命令用来关闭Portal代理的调试信息开关。

缺省情况下， Portal代理的所有调试信息开关均处于关闭状态。

表1-1 debugging portal-proxy error命令输出信息描述表

字段

描述

Cookie type *type* is not recognised.

不可识别的Cookie类型*type*

Failed to get cookie from packet.

从报文中获取cookie失败

Cookie is invalid, server-IP: *svr-ip*, local-IP: *local-ip*, server-port: *svr-port*.

非法的cookie：服务器IP为*svr-ip*，Master AC的IP为*local-ip*，服务器端口号为*svr-port*

Packet  is invalid.

报文非法

Failed to get IP address of MAC binding server.

获取MAC绑定服务器IP地址失败

Failed to get the IP address of BAS AC by user IP *user-ip.*

根据用户IP *user-ip*获取对应的BAS AC的IP地址失败

Failed to bind port *port-num*.

绑定端口*port-num*失败

Failed to receive packet from socket (ID *socket-id*)

从Socket（ID为*socket-id*）接收报文失败

Failed to send packet from Socket (ID *socket-id*).

通过Socket（ID为*socket-id*）发送报文失败

表1-2 debugging portal-proxy event命令输出信息描述表

字段

描述

Enable Portal proxy.

开启Portal代理功能

Disable Portal proxy.

关闭Portal代理功能

Reset statistics of packets.

清空报文统计信息

Fill cookie, server-IP: *svr-ip*, local-IP: *local-ip*, server-port: *svr-port*.

填充cookie属性，服务器IP为*svr-ip*，Master AC的IP为*local-ip*，服务器端口号为*svr-port*

Get cookie, server-IP: *svr-ip*, local-IP: *local-ip*, server-port:*svr-port.*

获取cookie属性，服务器IP为*svr-ip*，Master AC的IP为*local-ip，*服务器端口号为*svr-port*

Start to connect to WLAN.

开始与WLAN模块建立连接

Stop connecting to WLAN.

关闭与WLAN模块建立的连接

表1-3 debugging portal-proxy packet命令输出信息描述表

字段

描述

Received packet: Type = *type*, Length = *length*, Src IP= *ip-addr*, Port = *port-num*

收到Portal报文：报文类型为*type*，报文长度为*length*，源IP地址为*ip-addr*，源端口号为*port-num*

Sent packet: Type = *type*, Length = *length*, Dst IP= *ip-addr*, Port = *port-num*

发送Portal报文：报文类型为*type*，报文长度为*length*，目的IP地址为*ip-addr*，目的端口号为*port-num*

【举例】

\# 在Master AC上开启Portal代理功能，打开Portal代理的错误调试信息开关。若Master AC收到来自BAS AC的Portal报文，当报文中未携带Portal服务器IP地址的时候，输出如下调试信息。

\<Sysname\> debugging portal-proxy error

\*Aug  7 18:09:38:603 2012 Sysname PTPROXY/7/ERROR: -MDC=1; Failed to get cookie from packet.

*// 从报文中获取cookie失败*

\# 打开Portal代理的事件调试信息开关，当开启Portal代理功能的时候，输出如下调试信息。

\<Sysname\> debugging portal-proxy event

\<Sysname\> system-view

Sysname portal-proxy enable

\*Feb  1 22:02:40:913 2013 Sysname PTPROXY/7/Event: -MDC=1; Enable Portal proxy.

*// 开启Portal代理功能*

\*Feb  1 22:02:40:913 2013 Sysname PTPROXY/7/Event: -MDC=1; Start to connect to WLAN.

*// 开始与WLAN模块建立连接*

\*Feb  1 22:02:40:913 2013 Sysname PTPROXY/7/Event: Fill cookie, server-IP 111.8.12.300, local-IP 111.8.12.100, server-port 50100.

*[// Master AC*]*收到来自Portal服务器的报文后，首先向报文中填充cookie属性（服务器IP为111.8.12.300，Master AC的IP为111.8.12.100，服务器端口号为50100），然后发送给BAS AC*

\*Feb  1 22:02:40:913 2013 Sysname PTPROXY/7/Event: Get cookie, server-IP 111.8.12.300, local-IP 111.8.12.100, server-port 50100.

// *BAS AC**回复应答报文后，Master AC从回复报文中获取cookie属性（服务器IP为111.8.12.300，Master AC的IP为111.8.12.100，服务器端口号为50100）*

\# 在Master AC上开启Portal代理功能，打开Portal代理的事件调试信息开关，当Portal代理处理Portal报文时，输出如下调试信息。

\<Sysname\> debugging portal-proxy packet

\<Sysname\>\*Jan  2 22:29:41:966 2011 Sysname PORTALPR/7/Packet:

Received packet: Type = request info, Length = 16, Src IP= 111.8.24.1, Port = 50100

*// 收到Portal报文：报文长度为16，报文类型为request info，源IP地址为111.8.24.1，端口号为50100*

   01 09 00 00 00 00 00 00 6f 08 18 01 00 00 00 00

*// 报文前64字节信息*

\*Jan  2 22:29:41:969 2011 Sysname PTPROXY/7/Packet:

Sent packet: Type = request info, Length = 30, Dst IP = 111.8.24.55, Port = 2000

*// 发送Portal报文：报文长度为30，报文类型为request info，目的IP地址为111.8.24.55，端口号为2000*

   01 09 00 00 00 00 00 00 6f 08 18 01 00 00 00 01

   40 0e 01 04 6f 08 18 01 02 04 6f 08 18 58

*// 报文前64字节信息*

