
**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging attack-defense**

------------------------------------------------------------------------

【命令】

**[debugging attack-defense ** { **all** \| **error** \| **event** }]

**[undo debugging attack-defense ** { **all** \| **error** \| **event** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示攻击检测与防范所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging attack-defense**]命令用来打开攻击检测与防范调试信息开关。**undo debugging attack-defense**命令用来关闭攻击检测与防范调试信息开关。

缺省情况下，攻击检测与防范调试信息开关处于关闭状态。

表1-1 debugging attack-defense error命令输出信息描述表

字段

描述

Failed to add a dynamic blacklist entry for IP *ip-address*.

添加动态黑名单失败，IP地址为*ip-address*

Failed to add a dynamic protected IP entry (*ip-address*: *port*) for TCP client verification.

添加动态TCP客户端验证保护IP表项失败，IP地址为*ip-address*、端口号为*port*

Failed to add a dynamic protected IP entry (*ip-address*: *port*) for DNS client verification.

添加动态DNS客户端验证保护IP表项失败，IP地址为*ip-address*、端口号为*port*

Failed to add a dynamic protected IP entry (*ip-address*: *port*) for HTTP client verification.

添加动态HTTP客户端验证保护IP表项失败，IP地址为*ip-address*、端口号为*port*

表1-2 debugging attack-defense event命令输出信息描述表

字段

描述

Detected an attack occurred.

Attack type: *type*

Detected on: *interface-type interface-number / local*

Action: *action*

IP address: *ip-address*

Protocol: *protocol*

设备检测到一个攻击发生

·Attack type：攻击类型，包括scan、syn-flood、syn-ack-flood、ack-flood 、rst-flood、fin-flood、icmp-flood、icmpv6-flood、udp-flood等

·Detected on：进行攻击防范的位置，包括接口或本机

·Action：攻击防范的处理行为，包括以下动作的组合：

¡none：不作任何处理

¡drop：丢弃报文

¡logging：发送日志

¡block-source：将攻击源的主机IP地址加入黑名单，并阻断和丢弃来自该地址的后续报文

¡client-verify：将攻击目标的主机IP地址加入到客户端验证的受保护IP列表中

·IP address：Scan攻击的攻击源IP地址或Flood攻击的攻击目标IP地址

·Protocol：Scan攻击使用的协议（Scan攻击才显示此字段）

Detected an attack ended.

Attack type: *type*

Detected on: *interface-type interface-number / local*

Action: *action*

IP address: *ip-address*

设备检测到一个攻击结束

·Attack type：攻击类型，包括syn-flood、syn-ack-flood、ack-flood 、rst-flood、fin-flood、icmp-flood、icmpv6-flood、udp-flood等

·Detected on：进行攻击防范的位置，包括接口或本机

·Action：攻击防范的处理行为，包括：

¡none：不作任何处理

·IP address：Scan攻击的攻击源IP地址或Flood攻击的攻击目标IP地址

Added a dynamic protected IP entry (*ip-address*: *port*) for TCP client verification.

添加一个动态TCP客户端验证保护IP表项，IP地址为*ip-address*、端口号为*port*

Removed an expired dynamic protected IP entry (*ip-address*: *port*) for TCP client verification.

动态的TCP客户端验证保护IP表项被删除，IP地址为*ip-address*、端口号为*port*

Added a dynamic protected IP entry (*ip-address*: *port*) for DNS client verification.

添加一个动态DNS客户端验证保护IP表项，IP地址为*ip-address*、端口号为*port*

Removed an expired dynamic protected IP entry (*ip-address*: *port*) for DNS client verification.

动态的DNS客户端验证保护IP表项被删除，IP地址为*ip-address*、端口号为*port*

Added a dynamic protected IP entry (*ip-address*: *port*) for HTTP client verification.

添加一个动态HTTP客户端验证保护IP表项，IP地址为*ip-address*、端口号为*port*

Removed an expired dynamic protected IP entry (*ip-address*: *port*) for HTTP client verification.

动态的HTTP客户端验证保护IP表项被删除，IP地址为*ip-address*、端口号为*port*

Added a dynamic blacklist entry IP (*ip-address*), aging time *aging-time*(s).

添加一个动态黑名单表项，IP地址*ip-address*，老化时间为*aging-time*秒

【举例】

\# 创建一个攻击防范策略，在策略中使能对本机IP地址1.1.1.1进行SYN flood攻击防范检测，触发阈值为10，防范动作为输出日志和加入TCP客户端验证保护IP表项。在本机应用该策略。打开攻击防范报文调试信息开关后，当设备检测到发送速率超过阈值且目的地址为本机地址1.1.1.1的SYN报文时，输出如下调试信息。

\<Sysname\> debugging attack-defense event

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/EVENT: -MDC=1; Detected an attack occurred.

Attack type: syn-flood

Detected on: local

Action: logging, client-verify

IP address: 1.1.1.1

*// 检测到一个攻击发生：*

*[攻击类型为*]*syn-flood*

*[进行*]*攻击防范的位置为本机*

*[攻击防范的处理行为*]*包括：发送日志、将攻击目标的主机IP地址加入到客户端验证的受保护IP列表中*

*[Flood*]*攻击的攻击目标IP地址为1.1.1.1*

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/ EVENT: -MDC=1; Added a dynamic protected IP entry (1.1.1.1: 2003) of TCP client verify.

*// 添加一个动态TCP客户端验证保护IP表项，IP地址为1.1.1.1、端口号为2003*

\# 创建一个攻击防范策略，在策略中使能对本机IP地址1.1.1.1进行扫描攻击防范检测，攻击方防范的级别为**low**，防范动作为输出日志和阻断并丢弃来自该IP地址的后续报文。在本机应用该策略。打开攻击防范错误调试信息开关后，当设备检测到源地址为2.2.2.2，目的地址为1.1.1.1的报文端口变化数超过**low**级别的阈值，且此时设备资源不足时，输出如下调试信息。

\<Sysname\> debugging attack-defense error

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/ERROR: -MDC=1; Failed to add a dynamic blacklist entry for IP 2.2.2.2.

*// 添加一个动态黑名单表项失败*

**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging client-verify tcp**

------------------------------------------------------------------------

【命令】

**[debugging client-verify tcp ** { **all** \| **error** \| **event** \| **packet** }]

**[undo debugging client-verify tcp ** { **all** \| **error** \| **event** \| **packet** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示TCP客户端验证功能的所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging client-verify tcp**]命令用来打开TCP客户端验证功能的调试信息开关。**undo debugging client-verify tcp**命令用来关闭TCP客户端验证功能的调试信息开关。

缺省情况下，TCP客户端验证功能的调试信息开关处于关闭状态。

表1-3 debugging client-verify tcp error命令输出信息描述表

字段

描述

Failed to send a reply packet to client. Reason: No route is found.

向客户端回复报文失败，原因：找不到匹配的路由

Cookie is equal to correct ACK. Changed the cookie.

Cookie和正确的ACK序号相同，修改Cookie

Failed to copy data from mbuf.

拷贝mbuf中的报文失败

表1-4 debugging client-verify tcp event命令输出信息描述表

字段

描述

Added a trusted node: Type TCP, Source IP *src-ip-address*, VPN instance *vpn-instance-**name.*

添加一个信任{.TableTextChar}IP{.TableTextChar}地址：{.TableTextChar}类型为TCP，源IP地址为*src-ip-address*，所属的VPN实例名称为*vpn-instance-name*

Removed expired trusted node: Type = TCP,

Source IP = *src-ip-address*,

VPN instance = *vpn-instance-name.*

删除一个信任{.TableTextChar}IP{.TableTextChar}地址{.TableTextChar}：类型为TCP，源IP地址为*src-ip-address*，所属的VPN实例名称为*vpn-instance-name*

New cookie created, cookie ID is* cookie-id，*value is *cookie-value*

产生新{.TableTextChar}cookie，ID是*cookie-id*，cookie值是*cookie-value*

Cookie timed out.

Cookie超时

表1-5 debugging client-verify tcp packet命令输出信息描述表

字段

描述

The SYN packet sourced from *src-ip-address* is untrusted, and it will be verified by TCP client-verify.

源地址为*src-ip-address*的报文不可信，需要对其进行TCP客户端验证

The SYN ACK packet sourced from server is trusted.

来自服务器的SYN ACK报文可信

The RST packet is invalid and dropped.

该RST报文已被验证不合法，被丢弃

The ACK packet is invalid and dropped.

该ACK报文已被验证不合法，被丢弃

Dropped SYN, and replied with SYN ACK.

丢弃SYN报文，回复代理SYN ACK报文

Replied with ACK to server.

向服务器回复ACK报文

Sent ACK to client.

向客户端回复ACK报文

ACK cookie valid. Sent SYN to server.

ACK报文的cookie有效，向服务器发送SYN报文

Adjusted the ACK sequence number, and then forwarded the ACK.

调整报文响应序号，继续转发

Adjusted the sequence number, and then forwarded the packet.

调整报文序号，继续转发

Protocol(*pro-type*) ,FLAG(*flags*)

SrcIP(*src-ip-address*:*src-port*), DstIP(*dest-ip-address*: *dest-port*)

Seq(*seqSeqNumber*), AckSeq(*seqAckNumber*)

WinSize(*WinSize*)

MSS(*MssSize*)

设备向服务器或客户端发送的报文信息：

·*pro-type*：协议类型，包括TCP、UDP、Other，其中，Other表示除TCP和UDP以外的其它协议类型

·*flags*：报文标识

·*src-ip-address*：源IP地址

·*src-port*：源端口号

·*dest-ip-address*：目的IP地址

·*dest-port*：目的端口号

·*seqSeqNumber*：报文序列号

·*seqAckNumber*：确认序列号

·*WinSize*：窗口大小

·*MssSize*：MSS大小

【举例】

\# 配置TCP客户端验证受保护IP 9.1.1.1，并在入接口上使能TCP客户端验证单向代理功能。打开TCP客户端验证报文调试信息开关后，当设备接收到客户端首次发送的目的主机存在且目的IP为受保护IP的SYN报文时，输出如下调试信息。

\<Sysname\> debugging client-verify tcp packet

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The SYN packet 9.1.1.1 is untrusted, and will be verified by TCP client-verify.

*// 源地址为6.1.1.2的报文不可信，需要对其进行TCP客户端验证*

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Dropped SYN, and replied with SYN ACK:

      Protocol(TCP), FLAG(SYNACK)

      SrcIP(9.1.1.1: 2200), DstIP(6.1.1.2: 1)

      Seq(0), AckSeq(369121992)

      WinSize(0)

*// 丢弃SYN报文，设备代替服务器端向客户端回复SYN ACK报文*

\# 在入接口上使能TCP客户端验证单向代理功能。打开TCP客户端验证事件调试信息开关后，当设备对来自客户端的源地址为1.1.1.1，VPN名为kkk且目的地址为受保护IP的TCP连接请求验证通过时，输出如下调试信息。

\<Sysname\> debugging client-verify tcp event

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Added a trusted node: Type TCP, Source IP 1.1.1.1, VPN instance kkk.

*// 添加一个信任IP地址：类型为TCP，源IP地址为[1.1.1.1，所]属的VPN实例名称为kkk*

\# 在入接口上使能TCP客户端验证双向代理功能。打开TCP客户端验证错误调试信息开关后，当设备接收到服务端首次发送的可信SYNACK报文，且设备资源不足时，输出如下调试信息。

\<Sysname\> debugging client-verify tcp error

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Failed to copy data from mbuf.

*// 拷贝mbuf中的报文失败*

**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging client-verify dns**

------------------------------------------------------------------------

【命令】

**[debugging client-verify dns ** { **all** \| **error** \| **event** \| **packet** }]

**[undo debugging client-verify dns ** { **all** \| **error** \| **event** \| **packet** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示DNS客户端验证功能的所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging client-verify dns**]命令用来打开DNS客户端验证功能的调试信息开关。**undo debugging client-verify dns**命令用来关闭DNS客户端验证功能的调试信息开关。

缺省情况下，DNS客户端验证功能的调试信息开关处于关闭状态。

表1-6 debugging client-verify dns error命令输出信息描述表

字段

描述

Failed to send a reply packet to client. Reason: No route is found.

向客户端回复报文失败，原因：找不到匹配的路由

Cookie is equal to correct ACK. Changed cookie.

cookie序号正确，将其修改为计算得到的序号

表1-7 debugging client-verify dns event命令输出信息描述表

字段

描述

Added a trusted node: Type DNS, Source IP *src-ip-address*, VPN instance *vpn-instance-**name.*

添加一个信任{.TableTextChar}IP{.TableTextChar}地址：{.TableTextChar}类型为DNS，源IP地址为*src-ip-address*，所属的VPN实例名称为*vpn-instance-name*

Removed expired trusted node: Type =DNS,

Source IP = *src-ip-address*,

VPN instance = *vpn-instance-name.*

删除一个信任{.TableTextChar}IP{.TableTextChar}地址{.TableTextChar}：类型为DNS，源IP地址为*src-ip-address*，所属的VPN实例名称为*vpn-instance-name*

New cookie created, cookie ID is* cookie-id，*value is *cookie-value*

产生新{.TableTextChar}cookie，ID是*cookie-id*，cookie值是*cookie-value*

Cookie timed out.

Cookie超时

表1-8 debugging client-verify dns packet命令输出信息描述表

字段

描述

The SYN packet sourced from *src-ip-address* is untrusted, and it will be verified by DNS client-verify.

源地址为*src-ip-address*的报文不可信，需要对其进行DNS客户端验证

The UDP DNS query packet sourced from *src-ip-address* is untrusted, dropped it and then replied with TC packet.

源地址为*src-ip-address*的UDP DNS 查询请求报文不可信，丢弃该报文并向客户端回复TC报文

The RST packet is invalid and dropped.

该RST报文已被验证不合法，被丢弃

The ACK packet is invalid and dropped.

该ACK报文已被验证不合法，被丢弃

Dropped SYN, and replied with SYN ACK.

丢弃SYN报文，回复代理SYN ACK报文

Protocol(*pro-type*) ,FLAG(*flags*)

SrcIP(*src-ip-address*:*src-port*), DstIP(*dest-ip-address*: *dest-port*)

Seq(*seqSeqNumber*), AckSeq(*seqAckNumber*)

WinSize(*WinSize*)

MSS(*MssSize*)

设备向服务器或客户端发送的报文信息：

·*pro-type*：协议类型，包括TCP、UDP、Other，其中，Other表示除TCP和UDP以外的其它协议类型

·*flags*：报文标识

·*src-ip-address*：源IP地址

·*src-port*：源端口号

·*dest-ip-address*：目的IP地址

·*dest-port*：目的端口号

·*seqSeqNumber*：报文序列号

·*seqAckNumber*：确认序列号

·*WinSize*：窗口大小

·*MssSize*：MSS大小

【举例】

\# 在入接口上使能DNS客户端验证功能。打开DNS客户端验证错误调试信息开关后，设备收到DNS客户端发送的目的IP为受保护IP的首个DNS查询请求报文（UDP报文），且查找路由失败时，输出如下调试信息。

\<Sysname\> debugging client-verify tcp error

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/ERROR: -MDC=1; Failed to send a reply packet to client. Reason: No route is found.

*// 向客户端回复报文失败，原因：找不到匹配的路由*

\# 在入接口上使能DNS客户端验证功能。打开DNS客户端验证事件调试信息开关后，当设备对来自客户端的源地址为1.1.1.1，VPN名为KKK且目的地址为受保护IP的DNS请求验证通过时，输出如下调试信息。

\<Sysname\> debugging client-verify dns event

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/EVENT: -MDC=1; Added a trusted node: Type DNS, Source IP 1.1.1.1, VPN instance kkk.

*// 添加了一个信任IP地址：类型为DNS，源IP地址为1.1.1.1，所属的VPN实例名称为kkk*

\# 配置DNS客户端验证受保护IP 6.1.1.2，并在入接口上使能DNS 客户端验证功能，打开DNS客户端验证报文调试信息开关。

(1)设备收到DNS客户端发送的目的IP为受保护IP的首个DNS查询请求报文（UDP报文）时，输出如下调试信息。

\<Sysname\> debugging client-verify dns packet

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The UDP DNS query packet 2.2.2.2 is untrusted, drop it and then reply with TC packet.

*// 源地址为2.2.2.2的UDP DNS 查询请求报文不可信，丢弃该报文并向客户端回复TC报文*

(2) DNS{.ItemListCharChar}客户端收到TC报文后，按照TCP方式再次向服务器发起DNS请求。当设备收到DNS客户端发送目的IP为受保护IP的SYN报文时，输出如下调试信息。

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The SYN packet 2.2.2.2 is untrusted, and will be verified by DNS client-verify.

*// 源地址为2.2.2.2的报文不可信，需要对其进行DNS客户端验证*

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Dropped SYN, and replied with SYN ACK:

      Protocol(TCP), FLAG(SYNACK)

      SrcIP(6.1.1.2: 2200), DstIP(2.2.2.2)

      Seq(0),AckSeq(369121992)

      WinSize(0)

*// 丢弃客户端的SYN报文，设备代替服务器端向客户端回复SYN ACK报文*

\# 在入接口上使能DNS客户端验功能。打开DNS客户端验证事件调试信息开关60秒后，输出如下调试信息。

\<Sysname\> debugging client-verify dns event

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; New cookie created, cookie ID is*1，*value is 517312006.

*[//*]*产生新cookie，ID是1，cookie值是517312006*

\# 在入接口上使能DNS客户端验证功能。打开HTTP客户端验证错误调试信息开关后，当设备接收到客户端首次发送的SYN报文*SeqNumber*为517312000，且设备此时创建的cookie值也为517312001时，输出如下调试信息。

\<Sysname\> debugging client-verify dns error

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Cookie is equal to correct ACK. Changed cookie.

*[// cookie*]*序号正确，将其修改为计算得到的序号*

**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging client-verify http**

------------------------------------------------------------------------

【命令】

**[debugging client-verify http ** { **all** \| **error** \| **event** \| **packet** }]

**[undo debugging client-verify http ** { **all** \| **error** \| **event** \| **packet** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示HTTP客户端验证功能的所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【描述】

**[debugging client-verify http**]命令用来打开HTTP客户端验证功能的调试信息开关。**undo debugging client-verify http**命令用来关闭HTTP客户端验证功能的调试信息开关。

缺省情况下，HTTP客户端验证功能的调试信息开关处于关闭状态。

表1-9 debugging client-verify dns error命令输出信息描述表

字段

描述

Failed to send a reply packet to client. Reason: No route is found.

向客户端回复报文失败，原因：找不到匹配的路由

Cookie is equal to correct ACK. Changed cookie.

cookie序号正确，将其修改为计算得到的序号

表1-10 debugging client-verify dns event命令输出信息描述表

字段

描述

Added a trusted node: Type HTTP, Source IP *src-ip-address*, VPN instance *vpn-instance* *name.*

添加一个信任{.TableTextChar}IP{.TableTextChar}地址：{.TableTextChar}类型为HTTP，源IP地址为*src-ip-address*，所属的VPN实例名称为*vpn-instance-name*

Removed expired trusted node: Type = HTTP,

Source IP = *src-ip-address*,

VPN instance = *vpn-instance-name.*

删除一个信任{.TableTextChar}IP{.TableTextChar}地址{.TableTextChar}：类型为HTTP，源IP地址为*src-ip-address*，所属的VPN实例名称为*vpn-instance-name*

New cookie created, cookie ID is* cookie-id，*value is *cookie-value*

产生新{.TableTextChar}cookie，ID是*cookie-id*，cookie值是*cookie-value*

Cookie timed out.

Cookie超时

表1-11 debugging client-verify dns packet命令输出信息描述表

字段

描述

The SYN packet soured from *src-ip-address* is untrusted, and it will be verified by HTTP client-verify.

源地址为*src-ip-address*的报文不可信，需要对其进行HTTP客户端验证

The RST packet is invalid and dropped.

该RST报文已被验证不合法，被丢弃

The ACK packet is invalid and dropped.

该ACK报文已被验证不合法，被丢弃

Received HTTP GET query packet from *src-ip-address* ,and will begin first redirect.

收到HTTP GET请求报文，即将进行第一次重定向

Received HTTP GET query packet from *src-ip-address ,* and will begin second redirect.

收到HTTP GET请求报文，即将进行第二次重定向

Sent the redirect packet to client.

向HTTP客户端发送重定向报文

Dropped SYN, and replied with SYN ACK.

丢弃SYN报文，回复代理的SYN ACK报文

Protocol(*pro-type*) ,FLAG(*flags*)

SrcIP(*src-ip-address*:*src-port*), DstIP(*dest-ip-address*: *dest-port*),

Seq(*seqSeqNumber*), AckSeq(*seqAckNumber*)

WinSize(*WinSize*)

MSS(*MssSize*)

设备向服务器或客户端发送的报文信息：

·*pro-type*：协议类型，包括TCP、UDP、Other，其中，Other表示除TCP和UDP以外的其它协议类型

·*flags*：报文标识

·*src-ip-address*：源IP地址

·*src-port*：源端口号

·*dest-ip-address*：目的IP地址

·*dest-port*：目的端口号

·*seqSeqNumber*：报文序列号

·*seqAckNumber*：确认序列号

·*WinSize*：窗口大小

·*MssSize*：MSS大小

【举例】

\# 配置HTTP客户端验证受保护IP 6.1.1.2，在入接口上使能HTTP客户端验证功能，并打开HTTP客户端验证报文调试信息开关。

(1)设备收到HTTP客户端发送的目的IP为受保护IP的首个SYN报文时，输出如下调试信息。

\<Sysname\> debugging client-verify http packet

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The SYN packet 9.1.1.1 is untrusted, and will be verified by HTTP client-verify.

*// 源地址为9.1.1.1的报文不可信，需要对其进行HTTP客户端验证*

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Dropped SYN, and replied with SYN ACK:

      Protocol(TCP), FLAG(SYNACK)

      SrcIP(6.1.1.2: 2200), DstIP(9.1.1.1: 1)

      Seq(0),AckSeq(369121992)

      WinSize(0)

*// 丢弃SYN报文，设备代替服务器向客户端回复SYN ACK报文*

(2)HTTP客户端与设备之间的TCP连接建立后，HTTP客户端首次发送HTTP GET请求报文时，设备上输出如下调试信息。

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Receive HTTP GET query packet 9.1.1.1, and will begin first redirect.

*// 收到HTTP GET请求报文，即将进行第一次重定向验证处理*

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Sent the redirect packet to client.

*// 向HTTP客户端发送重定向报文*

(3)HTTP客户端根据第一次的重定向结果，再次发送HTTP GET请求报文时，设备上输出如下调试信息。

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Receive HTTP GET query packet 9.1.1.1, and will begin second redirect.

*// 收到HTTP GET请求报文，即将进行第二次重定向验证处理*

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Sent the redirect packet to client.

*// 向HTTP客户端发送从定向报文*

(4)HTTP客户端根据第二次的重定向结果，再次发送HTTP GET请求报文时，设备上输出如下调试信息。

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Added a trusted node: Type HTTP, Source IP 9.1.1.1, VPN instance \--.

*// 添加一个信任IP地址：类型为HTTP，源IP地址为9.1.1.1，属于公网*

\# 在入接口上使能HTTP客户端验功能。打开HTTP客户端验证事件调试信息开关后，当设备对来自客户端的源地址为1.1.1.1，VPN名为kkk且目的地址为受保护IP的HTTP连接请求验证通过时，输出如下调试信息。

\<Sysname\> debugging client-verify http event

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Added a trusted node: Type HTTP, Source IP 1.1.1.1, VPN instance kkk.

*// 添加一个信任IP地址：类型为*HTTP*，源IP地址为[1.1.1.1，所]属的VPN实例名称为kkk*

\# 在入接口上使能HTTP客户端验证功能。打开HTTP客户端验证错误调试信息开关后，当设备接收到客户端首次发送的SYN报文*SeqNumber*为517312000，且设备此时创建的cookie值也为517312001时，输出如下调试信息。

\<Sysname\> debugging client-verify http error

\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Cookie is equal to correct ACK. Changed cookie.

*[// cookie*]*序号正确，将其修改为计算得到的序号*

