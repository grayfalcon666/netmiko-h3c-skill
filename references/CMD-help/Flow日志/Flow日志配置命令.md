<!-- CMD-INDEX
  display userlog export              | 任意视图             | L11
  reset userlog flow export           | 用户视图             | L125
  userlog flow export host            | 系统视图             | L155
  userlog flow export load-balancing  | 系统视图             | L211
  userlog flow export source-ip       | 系统视图             | L261
  userlog flow export version         | 系统视图             | L305
  userlog flow syslog                 | 系统视图             | L353
-->

**Flow日志 \-- Flow日志配置命令 \-- display userlog export**

------------------------------------------------------------------------

**[display** **userlog** **export**]命令用来查看输出到日志主机的Flow日志的配置和统计信息。

【命令】

**[display** **userlog** **export**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看输出到日志主机的Flow日志的配置和统计信息。

\<Sysname\> display userlog export

Flow:

  Export flow log as UDP Packet.

  Version: 3.0

  Source address: 2.2.2.2

  Log load balance function: Disabled

  Log host numbers: 2

  Log host 1:

    IP address/Port: 1.2.3.6/2000

    Total logs/UDP packets exported: 112/87

  Log host 2:

    VPN instance:abc

    IP address/Port:1.1.1.1/2000

    Total logs/UDP packets exported: 6553665536/409597846

表1-1 display userlog export命令显示信息描述表

字段

描述

Flow

表示该段显示的是Flow日志的相关配置和统计信息

Export flow log as UDP Packet

表示Flow日志按照封装成UDP报文的方式发送

Version

Flow日志的版本号

Source address

Flow日志UDP报文的源IP地址

Log load balancing function

Flow日志UDP报文负载分担功能是否使能：

·Enabled：使能

·Disabled：未使能

Log hosts numbers

已配置的Flow日志主机数量

Log host 1

日志主机1的相关信息

VPN instance

Flow日志主机所属的VPN

IP address/port

Flow日志主机的IP地址和端口号

Total logs

Flow日志的总数

UDP packets exported

Flow日志的UDP报文总数，一条UDP报文中可能含有多条Flow日志

【相关命令】

·**userlog flow export**

**Flow日志 \-- Flow日志配置命令 \-- reset userlog flow export**

------------------------------------------------------------------------

**[reset**]**userlog****flow** **export**命令用来清除Flow日志的统计信息。

【命令】

**[r**]**eset****userlog****flow** **export**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除Flow日志的统计信息。

\<Sysname\> reset userlog flow export

【相关命令】

·**userlog flow export**

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export host**

------------------------------------------------------------------------

**[userlog**]**flow****export****host**命令用来配置Flow日志主机地址和UDP端口号。

**[undo userlog**]**flow****export****host**命令用来删除Flow日志主机配置。

【命令】

**[userlog**] **flow** **export**  **vpn-instance** *vpn-instance-name*  **host** *[ipv4-address*[ \| **ipv6** *ipv6-address* } **port** *udp-port*]

**[undo userlog** **flow** **export** [ **vpn-instance** *vpn-instance-name*  **host** { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* }]]

【缺省情况】]

没有配置Flow日志主机的IP地址和UDP端口号。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：指定Flow日志主机所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示Flow日志主机位于公网中。该参数的支持情况与设备型号有关，请以设备的实际情况为准。

*[hostname*]：指定Flow日志主机名，为1～253个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"-"、"\_"和"."。

*[ipv4-address*]：指定Flow日志主机的IPv4地址，取值范围是合法的单播IPv4地址，且不能是环回地址。

**[ipv6** *host-ipv6-address*]：指定Flow日志主机的IPv6地址。

**[port*** udp-port*]：指定Flow日志主机的UDP端口号，*udp-port*取值范围为1～65535。

【使用指导】

为了避免与通用的UDP端口号冲突，建议使用1025～65535的UDP端口号。

【举例】

\# 将Flow日志信息发送给Flow日志主机，Flow日志主机的地址为1.2.3.6，对应UDP端口号为2000。

\<Sysname\> system-view

Sysname userlog flow export host 1.2.3.6 port 2000

【相关命令】

·**display userlog export**

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export load-balancing**

------------------------------------------------------------------------

**[userlog flow export load-balancing**]命令用来配置Flow日志按照负载分担方式输出到日志主机。

**[undo userlog flow export load-balancing**]命令用来恢复缺省情况。

【命令】

**[userlog** **flow** ]**export load-balancing**

**[undo userlog** **flow** ]**export load-balancing**

【缺省情况】

每一条Flow日志复制发送给所有已配置的Flow日志主机。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置Flow日志按照负载分担方式输出到日志主机时：

·配置了Flow日志负载分担功能以后，一条Flow日志仅仅会发送到用户配置的所有日志主机中的某一台特定的日志主机。

·Flow日志按照会话源IP进行负载分担。在不改变配置的前提下，源IP固定的会话对应的Flow日志始终发送到固定的一台日志主机。

·如果配置的日志主机不可达时，日志主机仍会参与Flow日志的负载分担，但负载分担到不可达的日志主机的Flow日志会直接被丢弃。

【举例】

\# 设置Flow日志负载分担发送。

\<Sysname\> system-view

Sysname userlog flow export load-balancing

【相关命令】

·**userlog flow export host**

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export source-ip**

------------------------------------------------------------------------

**[userlog** **flow** **export** **source-ip**]命令用来配置Flow日志报文的源地址。

**[undo** **userlog** **flow export** **source-ip**]命令用来恢复缺省情况。

【命令】

**[userlog** **flow** **export** **source-ip** *ip-address*]

**[undo** **userlog** **flow** **export** **source-ip**]

【缺省情况】

Flow日志报文的源地址为发送该报文的接口的IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：Flow日志报文的源IP地址。

【举例】

\# 将1.2.1.2配置为Flow日志报文的源地址。

\<Sysname\> system-view

Sysname userlog flow export source-ip 1.2.1.2

【相关命令】

·**userlog flow export host**

**Flow日志 \-- Flow日志配置命令 \-- userlog flow export version**

------------------------------------------------------------------------

**[userlog** **flow** **export** **version**]命令用来配置Flow日志报文的版本号。

**[undo** **userlog** **flow export** **version**]命令用来恢复缺省情况。

【命令】

**[userlog** **flow** **export** **version** *version-number*]

**[undo userlog**] **flow** **export****version**

【缺省情况】

Flow日志报文的版本号为1.0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：Flow日志报文的版本号，取值为1或3，分别对应Flow1.0和Flow3.0。

【使用指导】

同一时刻只能使用一个版本，如果多次使用该命令配置版本，则最新的配置生效。

【举例】

\# 将Flow日志报文版本号设为3.0。

\<Sysname\> system-view

Sysname userlog flow export version 3

【相关命令】

·**userlog flow export host**

**Flow日志 \-- Flow日志配置命令 \-- userlog flow syslog**

------------------------------------------------------------------------

**[userlog**]**flow****syslog**命令用来配置Flow日志输出到信息中心。

**[undo userlog**]**flow****syslog**命令用来恢复缺省情况。

【命令】

**[userlog** **flow** **syslog**]

**[undo userlog** **flow** **syslog**]

【缺省情况】

Flow日志输出到Flow日志主机。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置Flow日志输出到信息中心时，需要注意：

·日志主机和信息中心两种输出方向互斥，默认输出方向为日志主机。如果配置了信息中心方向，则会忽略日志主机方向。

·通常情况下，用户访问网络会在短时间内产生大量NAT会话日志。系统日志传输格式为ASCII码，相比Flow日志的二进制格式传输效率低。所以，建议在日志量较小的情况下，使用输出到信心中心的方式。

·日志输出至信息中心时，日志信息的优先级为informational，即作为设备的一般提示信息。

【举例】

\# 设置Flow日志输出到信息中心。

\<Sysname\> system-view

Sysname userlog flow syslog

【相关命令】

·**userlog** **flow** **export** **host**
