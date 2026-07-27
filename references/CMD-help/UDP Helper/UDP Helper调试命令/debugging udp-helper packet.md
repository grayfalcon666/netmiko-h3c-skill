<!-- CMD-INDEX
  debugging udp-helper packet         | 任意视图             | L5
-->

**UDP Helper \-- UDP Helper调试命令 \-- debugging udp-helper packet**

------------------------------------------------------------------------

**[debugging udp-helper packet**]命令用来打开UDP Helper的报文调试信息开关。

**[undo debugging udp-helper packet**]命令用来关闭UDP Helper的报文调试信息开关。

【命令】

**[debugging udp-helper packet**]

**[undo debugging udp-helper packet**]

【缺省情况】

UDP Helper的报文调试信息开关处于关闭状态。

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

表1-1 debugging udp-helper packet命令输出信息描述表

字段

描述

Received a packet.

收到一个UDP报文

Sent a packet.

发送一个中继后的UDP报文

src_addr

UDP报文的源地址

dst_addr

UDP报文的目的地址

dst_port

UDP报文的目的端口号

dst_vrf

UDP报文的目的VRF索引

Failed to save packet header information to continuous storage space.

保存报文头在一块连续的空间里失败

Invalid UDP packet.

无效的UDP报文

Destination address (*address*, vrf:*vrf_index*) is not reachable.

目的地址*address*不可达

Failed to copy packet.

复制报文失败

Failed to put the message to the queue.

报文入队列失败

【举例】

\# 打开UDP Helper的收发报文调试信息开关，配置端口137收到的报文被转发到公网服务器192.168.3.252。

\<Sysname\> terminal logging level 7

\<Sysname\> terminal monitor

\<Sysname\> debugging udp-helper packet

\<Sysname\> system-view

Sysname udp-helper enable

Sysname udp-helper port 137

Sysname interface ethernet 1/1

Sysname-Ethernet1/1 udp-helper server 192.168.3.252 global

\*Sep  8 11:11:45:238 2011 Sysname UDPH/7/PACKET: -MDC=1; Received a packet.

src_addr: 192.168.3.251, dst_addr: 255.255.255.255, dst_port: 137

*// 收到一个UDP报文，源地址为192.168.3.251，目的地址为255.255.255.255，目的端口号为137*

\*Sep  8 11:11:45:239 2011 Sysname UDPH/7/PACKET: -MDC=1; Sent a packet. src_addr: 192.168.3.251, dst_addr: 192.168.3.252, dst_vrf: 0, dst_port: 137

*// 转发报文到公网服务器，被转发报文的源地址为192.168.3.251，目的地址被修改为192.168.3.252，目的端口号为137*

\# 打开UDP Helper的收发报文调试信息开关，配置端口137收到的报文被转发到VPN a内的服务器192.168.3.252。

\<Sysname\> terminal logging level 7

\<Sysname\> terminal monitor

\<Sysname\> debugging udp-helper packet

\<Sysname\> system-view

Sysname udp-helper enable

Sysname udp-helper port 137

Sysname interface ethernet 1/1

Sysname-Ethernet1/1 udp-helper server 192.168.3.252 vpn-instance a

\*Sep  8 11:11:45:238 2011 Sysname UDPH/7/PACKET: -MDC=1; Received a packet.

src_addr: 192.168.3.251, dst_addr: 255.255.255.255, dst_port: 137

*// 收到一个UDP报文，源地址为192.168.3.251，目的地址为255.255.255.255，目的端口号为137*

\*Sep  8 11:11:45:239 2011 Sysname UDPH/7/PACKET: -MDC=1; Sent a packet. src_addr: 192.168.3.251, dst_addr: 192.168.3.252, dst_vrf: 1, dst_port: 137

*// 转发报文到私网索引为1的服务器，被转发报文的源地址为192.168.3.251，目的地址被修改为192.168.3.252，目的端口号为137*

\*May  30 15:06:20:484 2013 Sysname UDPH/7/PACKET: -MDC=1; Destination address(192.168.3.252, vrf:0) is not reachable*.

*// 私网索引为0的目的地址192.168.3.252不可达*

