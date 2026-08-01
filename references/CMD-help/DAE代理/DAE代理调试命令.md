<!-- CMD-INDEX
  debugging radius dynamic-author proxy | 用户视图             | L5
-->

**DAE代理 \-- DAE代理调试命令 \-- debugging radius dynamic-author proxy**

------------------------------------------------------------------------

【命令】

**[debugging radius dynamic-author proxy **[{ **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging radius dynamic-author proxy **[{ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DAE代理的所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging radius dynamic-author proxy**]命令用来打开DAE代理的调试信息开关。**undo debugging radius dynamic-author proxy**命令用来关闭DAE代理的调试信息开关。

缺省情况下，DAE代理的所有调试信息开关均处于关闭状态。

表1-1 debugging radius dynamic-author proxy error命令输出信息描述表

字段

描述

Failed to bind port *port-num*.

绑定端口*port-num*失败

Failed to get DAE client\'s key by IP *IP-addr*.

通过IP地址*IP-addr*获取DAE客户端的密钥失败

Packet length is invalid.

报文长度非法.

Packet type is invalid.

报文类型非法.

Failed to authenticate packet.

校验报文失败

Failed to sent packet to DAE Client (IP *ip-addr*).

向IP地址为*ip-addr*的DAE客户端发送报文失败

Failed to get error code from packet.

从报文中获取错误码失败

The DAE packet code *code* is not support.

不支持的DAE报文类型*code*

Failed to receive packet from socket (ID *socket-ID*).

从Socket（ID为*socket-ID*）接收报文失败

Failed to get session for packet (ID *packet-ID*).

无法为报文（ID为*packet-ID*）找到会话上下文

Failed to send DAE request to NAS (IP *ip-addr*).

向IP地址为*ip-addr*的NAS发送DAE请求失败

Failed to get NAS.

找不到NAS（BAS AC）

Failed to send DAE request to NAS.

向NAS（BAS AC）发送DAE请求报文失败

表1-2 debugging radius dynamic-author proxy event命令输出信息描述表

字段

描述

Reset statistics of DAE packets.

清空DAE报文统计信息

Enable DAE proxy.

开启DAE代理功能

Disable DAE proxy.

关闭DAE代理功能

Got framed IP *ip-addr*.

获取到framed IP地址为*ip-addr*

DAE proxy received response with no request.

DAE代理收到没有请求的应答

DAE proxy received retransmit request pkt.

DAE代理收到重传请求报文

DAE proxy cached DAE response from NAS (IP *ip-addr*).

DAE代理缓存来自NAS（IP地址为*ip-addr*）的DAE应答

DAE proxy created tunnel DAE Client IP *ip-addr1*, Port *port-num*, Local IP *ip-addr2*.

DAE代理创建透传通道，DAE客户端IP地址为*ip-addr1*，端口号为*port-num*，本端IP地址为*ip-addr2*

DAE proxy deleted tunnel DAE Client IP *ip-addr1*, Port *port-num*, Local IP *ip-addr2*.

DAE代理删除透传通道，DAE客户端IP地址为*ip-addr1*，端口号为*port-num*，本端IP地址为*ip-addr2*

DAE proxy tunnel timed out.

DAE代理的透传通道超时（一个通道中有多个会话）

DAE proxy session timed out.

DAE代理的会话超时

DAE proxy created session with id *session-id*.

DAE代理创建session ID为*session-id*的会话

DAE proxy deleted session with id *session-id*.

DAE代理销毁session ID为*session-id*的会话

Start to connect WLAN.

开始与WLAN模块建立连接

Stop connecting to WLAN.

停止与WLAN模块建立连接

Set NAS port as *port-num*.

设置NAS端口为*port-num*

表1-3 debugging radius dynamic-author proxy packet命令输出信息描述表

字段

描述

Received DAE packet: SRC IP = *ip-addr*, Port = *port-num*, Type = *type*

收到DAE报文：源IP地址为*ip-addr*，端口号为*port-num*，报文类型为*type*

Sent DAE packet: DEST IP = *ip-addr*, Port = *port-num*, Type = *type*

发送DAE报文：目的IP地址为*ip-addr*，端口号为*port-num*，报文类型为*type*

【举例】

\# 在Master AC上开启DAE代理功能，并打开DAE代理的错误调试信息开关。若Master AC收到来自DAE Client的DAE请求报文，当校验Authenticator属性失败的时候，输出如下调试信息。

\<Sysname\> debugging radius dynamic-author proxy error

\*Aug  7 18:09:38:603 2012 Sysname RADIUS DYNAMIC-AUTHOR PROXY/7/ERROR: -MDC=1; Failed to authenticate packet.

*// 校验报文失败*

\# 在Master AC上打开DAE代理的事件调试信息开关，当Master AC上开启DAE代理功能时，输出如下调试信息。

\<Sysname\> debugging radius dynamic-author proxy event

\*Feb  1 16:54:50:621 2013 Sysname DAE PROXY/7/Event: -MDC=1; Enable DAE proxy.

*// 开启DAE代理功能*

\*Feb  1 16:54:50:621 2013 Sysname DAE PROXY/7/Event: -MDC=1; Start to connect WLAN.

*// 开始与WLAN模块建立连接*

\# 在Master AC上开启DAE代理功能，打开DAE代理的报文调试信息开关，当DAE代理收到DM_REQ报文时，输出如下调试信息。

\<Sysname\> debugging radius dynamic-author proxy packet

\*Feb  1 17:21:34:322 2013 Sysname DAE PROXY/7/Packet: -MDC=1; Received DAE packet: SRC IP = 6.6.6.6, Port = 1360, Type = disconnect request packet

28 00 00 19 4b f5 f0 07 0c 30 d9 6b f9 09 6d 68

95 29 97 b9 01 05 68 33 63

*// 收到DAE报文：源IP地址为6.6.6.6，端口号为1360，报文类型为disconnect request*

\*Feb  1 17:21:34:324 2013 Sysname DAE PROXY/7/Packet: -MDC=1; Sent DAE packet: DEST IP = 111.8.200.2, Port = 3799, Type = disconnect request packet

28 00 00 19 4b f5 f0 07 0c 30 d9 6b f9 09 6d 68

95 29 97 b9 01 05 68 33 63

*// 发送DAE报文：目的地址为111.8.200.2，端口为3799，报文类型为disconnect request*

**
