<!-- CMD-INDEX
  debugging ripng                     | 用户视图             | L11
  debugging ripng brief               | 用户视图             | L47
  debugging ripng event               | 用户视图             | L139
  debugging ripng packet              | 用户视图             | L247
  debugging ripng receive             | 用户视图             | L503
  debugging ripng send                | 用户视图             | L715
  debugging ripng timer               | 用户视图             | L843
-->

**RIPng \-- RIPng调试命令 \-- debugging ripng**

------------------------------------------------------------------------

【命令】

**[debugging ripng**] *process-id*

**[undo debugging ripng**] *process-id*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【描述】

**[debugging ripng**]命令用来打开RIPng所有的调试信息开关。**undo debugging ripng**命令用来关闭RIPng所有的调试信息开关。

缺省情况下，RIPng所有的调试信息开关处于关闭状态。

【举例】

\# 打开RIPng进程1所有的调试信息开关。

\<Sysname\> debugging ripng 1

**RIPng \-- RIPng调试命令 \-- debugging ripng brief**

------------------------------------------------------------------------

【命令】

**[debugging ripng** *process-id* **brief**]

**[undo debugging ripng** *process-id* **brief**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【描述】

**[debugging ripng brief**]命令用来打开RIPng摘要调试信息开关。**undo debugging ripng brief**命令用来关闭RIPng摘要调试信息开关。

缺省情况下，RIPng摘要调试信息开关处于关闭状态。

表1-1 debugging ripng brief命令输出信息描述表

字段

描述

RIPng *process-id*

RIPng进程号

Sending *packet-version packet-type* on *interface-type interface-number* to *dest-ipv6* with *number* route enties

发送RIPng报文

·*packet-version*：RIPng报文的版本，取值为v1

·*packet-type*：RIPng报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口发送RIPng报文

·*dest-ipv6*：RIPng报文的目的IPv6地址

·*number*：该报文携带的路由表项数目

Receiving *packet-version packet-type* on *interface-type interface-number* from *source-ipv6* with *number* route enties

接收RIPng报文

·*packet-version*：RIPng报文的版本，取值为v1

·*packet-type*：RIPng报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口接收RIPng报文

·*source-ipv6*：RIPng报文的源IPv6地址

·*number*：该报文携带的路由表项数目

Packets to be sent on interface *interface-type interface-number* have exceeded the limit, possibly causing packet loss

接口下缓存报文数过大

·*interface-type interface-number*：接口类型和编号，从该接口发送RIPng报文

【举例】

\# Router A的GigabitEthernet1/0/1接口和Router B的GigabitEthernet1/0/1接口相连，在Router A的GigabitEthernet1/0/1接口和Router B的GigabitEthernet1/0/1接口上使能RIPng功能，在Router A上打开RIPng摘要调试信息开关。

\<RouterA\> debugging ripng 1 brief

\*Nov 22 21:17:37:662 2010 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Sending v1 response on GigabitEthernet1/0/1 to FF02::9 with 2 route enties.

*[// RIPng*]*进程1发送版本1的应答报文，发送接口为GigabitEthernet1/0/1，目的地址为FF02::9，且该报文包括2个路由表项*

\*Nov 22 21:17:40:390 2010 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Receiving v1 response on GigabitEthernet1/0/1 from FE80::200:5EFF:FE71:A706 with 2 route enties.

*[// RIPng*]*进程1接收版本1的应答报文，接收接口为GigabitEthernet1/0/1，报文源地址为FE80::200:5EFF:FE71:A706，且该报文包括2个路由表项*

\*July 18 15:47:40:160 2012 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Packets to be sent on interface *logic-interface ipv6-address* have exceeded the limit, possibly causing packet loss

*[// RIPng*]*进程1从接口GigabitEthernet1/0/1发送报文，缓存报文长度超过接口允许最大报文长度*

**RIPng \-- RIPng调试命令 \-- debugging ripng event**

------------------------------------------------------------------------

【命令】

**[debugging ripng** *process-id* **event**]

**[undo debugging ripng** *process-id* **event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【描述】

**[debugging ripng event**]命令用来打开RIPng事件调试信息开关。**undo debugging ripng event**命令用来关闭RIPng事件调试信息开关。

缺省情况下，RIPng事件调试信息开关处于关闭状态。

表1-2 debugging ripng event命令输出信息描述表

字段

描述

RIPng *process-id*

RIPng进程号

Enabled RIPng on *interface-type interface-number*

在接口上使能RIPng功能

·*interface-type interface-number*：接口类型和编号

Disabled RIPng on *interface-type interface-number*

在接口上关闭RIPng功能

·*interface-type interface-number*：接口类型和编号

Failed to add RIPng route

添加IPv6路由表失败

Triggered update sent

路由表发生变化，发送触发更新报文

Prefix list used in filter-policy import has changed

用于过滤接收路由信息的IPv6地址前缀列表发生变化

Prefix list used in filter-policy export has changed

用于过滤发布路由信息的IPv6地址前缀列表发生变化

The ACL used in filter-policy import has changed

用于过滤接收路由信息的访问控制列表发生变化

The ACL used in filter-policy export has changed

用于过滤发布路由信息的访问控制列表发生变化

Received default-route result of route-policy

收到缺省路由的路由策略上报结果

【举例】

\# 在Router A上创建RIPng进程1，并在GigabitEthernet1/0/1接口上使能RIPng功能；在Router A上打开RIPng事件调试信息开关。

\<RouterA\> debugging ripng 1 event

\<RouterA\> system-view

RouterA interface gigabitethernet 1/0/1

RouterA-GigabitEthernet1/0/1 ripng 1 enable

\*Nov 22 21:48:54:988 2010 RouterA RIPNG/7/RIPNGDEBUG:RIPng 1 : Enabled RIPng on GigabitEthernet1/0/1.

*// 在GigabitEthernet1/0/1接口上使能RIPng进程1*

\*Nov 22 21:47:25:836 2010 RouterA RIPNG/7/RIPNGDEBUG:RIPng 1 : Triggered update sent{.TerminalDisplayChar}

*[// RIPng*]*进程1发送触发更新*

\# 在Router A的GigabitEthernet1/0/1接口上关闭RIPng功能。

RouterA-GigabitEthernet1/0/1 undo ripng enable

\*Nov 22 21:50:46:270 2010 RouterA RIPNG/7/RIPNGDEBUG:RIPng 1 : Disabled RIPng on GigabitEthernet1/0/1.

*// 在GigabitEthernet1/0/1接口上去使能RIPng进程1*

**RIPng \-- RIPng调试命令 \-- debugging ripng packet**

------------------------------------------------------------------------

【命令】

**[debugging ripng** *process-id* **packet** [ **interface** *interface-type interface-number* ]]

**[undo debugging ripng** *process-id* **packet** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

**[interface***interface-type interface-number*]：接口类型和接口编号，打开指定接口的RIPng报文调试信息开关。如果未指定本参数，将打开所有接口的RIPng报文调试信息开关。

【描述】

**[debugging ripng** **packet**]命令用来打开RIPng报文调试信息开关。**undo debugging ripng packet**命令用来关闭RIPng报文调试信息开关。

缺省情况下， RIPng报文调试信息开关处于关闭状态。

表1-3 debugging ripng packet命令输出信息描述表

字段

描述

RIPng *process-id*

RIPng进程号

Suppressed update on *sour-ipv6* of *interface-type interface-number*

接口无路由可发

·*sour-ipv6*：RIPng报文的源地址

·*interface-type interface-number*：接口类型和编号，从该接口发送RIPng报文

Failed to send socket, return value *error-number*

Socket报文发送失败

·*error-number*：发送失败返回值

Receiving *packet-type* message from *source-ipv6* on *interface-type interface-number*

接收RIPng报文

·*packet-type*：RIPng报文类型，取值为request或response

·*source-ipv6*：RIPng报文的源IPv6地址

·*interface-type interface-number*：接口类型和编号，从该接口接收RIPng报文

Sending *packet-type* message on *interface-type interface-number* to *dest-ipv6*

发送RIPng报文

·*packet-type*：RIPng报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口发送RIPng报文

·*dest-ipv6*：RIPng报文的目的IPv6地址

Packet: version *packet-version*, command *cmd-value*, length *length*

RIPng报文头信息

·*packet-version*：RIPng报文的版本，取值为1或2

·*cmd-value*：报文类型，取值为request或response

·*length*：报文长度

Destination *prefix/number*, cost *cost*, tag *tag*

路由表项信息

·*prefix/number*：目的网段前缀

·*cost*：此路由的度量值

·*tag*：此路由的标签值

Must-Be-Zero fields are not zero in header

RIPng报文头Must-Be-Zero字段不等于零

Request for all route entries

请求全部路由

Nexthop *ipv6-address*

路由的下一跳地址

·*ipv6-address*：IPv6地址

Destination *prefix*/*number*

路由项的目的网段前缀

·*prefix/number*：目的网段前缀

Ignored this packet. Failed to get the hop limit

获取报文hoplimit失败，忽略接收的报文

Ignored this packet. Packet originated by itself

接收到自身产生的RIPng报文，忽略接收的报文

Invalid destination address *ipv6-address* in the received RTE

目的地址不正确

·*ipv6-address*：此条路由的目的地址

Invalid prefix length *prefix-length* in the received RTE

前缀长度不正确

·*prefix-length*：此条路由的前缀长度

Invalid cost *cost* in the received RTE

cost字段无效

·*cost*：此条路由的度量值

Ignored route *ipv6-address/ prefix-length*. Policy prohibits

路由未通过路由策略，忽略此路由

·*ipv6-address/prefix-length*：此条路由的目的地址和前缀长度

Ignored route *ipv6-address/ prefix-length*. Nexthop is this interface\'s link-local.

路由的下一跳是本接口的链路本地地址，忽略此路由

·*ipv6-address/prefix-length*：此条路由的目的地址和前缀长度

Ignored route *ipv6-address/ prefix-length*.. Default route configured is advertised.

正在发布缺省路由，忽略路由

·*ipv6-address/prefix-length*：此条路由的目的地址和前缀长度

Unrecognized command received from *interface-type interface-number*

无法识别收到RIPng报文的命令字段

·*interface-type interface-number*：接口类型和编号，从该接口收到RIPng报文

Error occurred while processing received packet

处理接收报文时出错

Received packet with invalid length from *ipv6-address*

接收的RIPng报文长度无效

·*ipv6-address*：RIPng报文的源地址

Received packet with invalid version from *ipv6-address*

接收的RIPng报文版本无效

·*ipv6-address*：RIPng报文的源地址

Response received from *ipv6-address* on invalid UDP port

收到来自无效UDP端口的应答报文

·*ipv6-address*：RIPng报文的源地址

Response received from *ipv6-address* has invalid hop limit

接收的应答报文hoplimit无效

·*ipv6-address*：RIPng报文的源地址

Response received from invalid peer *ipv6-address*

收到来自无效peer的应答报文

·*ipv6-address*：邻居IPv6地址

Ignored this response packet. BFD session was not up.

BFD会话没有up，不接收响应报文

Ignored the packet on interface *interface-type interface-number*  due to IPsec profile mismatch

IPsec安全框架不匹配，忽略该报文

·*interface-type interface-number*：接口类型和编号，从该接口收到RIPng报文

Must-Be-Zero fields are not zero in header

必为零域不为0

【举例】

\# Router A通过GigabitEthernet1/0/1接口与Router B的GigabitEthernet1/0/1接口相连，在Router A上创建RIPng进程1，并在GigabitEthernet1/0/1接口上使能RIPng功能；在Router B上创建RIPng进程，并在GigabitEthernet1/0/1接口上使能RIPng；在Router A上打开RIPng报文调试信息开关。

\<RouterA\> debugging ripng 1 packet

\*Nov 24 13:49:27:98 2010 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Receiving response message from FE80::200:5EFF:FE71:A700 on GigabitEthernet1/0/1

*[// RIPng*]*进程1从接口GigabitEthernet1/0/1接收应答报文。收接口IPv6地址为FE80::200:5EFF:FE71:A700*

\*Nov 24 13:49:27:98 2010 RouterA RIPNG/7/RIPNGDEBUG:  Packet : version 1, command response, length 64

*// 接收的应答报文版本1，长度64字节*

\*Nov 24 13:49:27:98 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 22::/64, cost 16, tag 0

*// 第一个路由表项：目的网段22::/64，cost为16，tag为0*

\*Nov 24 13:49:27:98 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 50::/64, cost 1, tag 0

*// 第二个路由表项：目的网段50::/64，cost为1，tag为0*

\*Nov 24 13:49:27:98 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 1001::1/128, cost 1, tag 0

*// 第三个路由表项：目的网段1001::1/128，cost为1，tag为0*

\*Nov 24 13:49:51:130 2010 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Sending response message on GigabitEthernet1/0/1 to FF02::9

*[// RIPng*]*进程1从接口GigabitEthernet1/0/1发送应答报文。发送报文的目的地址为IPv6组播地址FF02::9*

\*Nov 24 13:49:52:302 2010 RouterA RIPNG/7/RIPNGDEBUG:  Packet : version 1, command response, length 44

*// 发送的应答报文版本1，长度44字节*

\*Nov 24 13:49:52:317 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 22::/64, cost 16, tag 0

*// 第一个路由表项：目的网段22::/64，cost为16，tag为0*

\*Nov 24 13:49:52:317 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 2000::1/128, cost 1, tag 0

*// 第二个路由表项：目的网段2000::1/128，cost为1，tag为0*

**RIPng \-- RIPng调试命令 \-- debugging ripng receive**

------------------------------------------------------------------------

【命令】

**[debugging ripng** *process-id* **receive** [ **interface** *interface-type interface-number* ]]

**[undo debugging ripng** *process-id* **receive** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

**[interface***interface-type interface-number*]：接口类型和编号，打开指定接口的RIPng接收报文调试信息开关。如果未指定本参数，将打开所有接口的RIPng接收报文调试信息开关。

【描述】

**[debugging ripng receive**]命令用来打开RIPng接收报文调试信息开关。**undo debugging ripng receive**命令用来关闭RIPng接收报文调试信息开关。

缺省情况下，RIPng接收报文调试信息开关处于关闭状态。

表1-4 debugging ripng receive命令输出信息描述表

字段

描述

RIPng *process-id*

RIPng进程号

Ignored this packet. Failed to get the hoplimit

获取报文hoplimit失败，忽略接收的报文

Ignored this packet. Packet originated by the local router

接收到自身产生的RIPng报文，忽略接收的报文

Ignored this packet. Failed to add neighbor

添加邻居失败，忽略接收的报文

Invalid destination address *ipv6-address* in the received RTE

目的地址不正确

·*ipv6-address*：此条路由的目的地址

Invalid prefix length *prefix-length* in the received RTE

前缀长度不正确

·*prefix-length*：此条路由的前缀长度

Invalid cost *cost* in the received RTE

cost字段无效

·*cost*：此条路由的度量值

Ignored route *ipv6-address/ prefix-length*. Policy prohibits

路由未通过路由策略，忽略此路由

·*ipv6-address/prefix-length*：此条路由的目的地址和前缀长度

Ignored route *ipv6-address/ prefix-length*. Nexthop is this interface\'s link-local.

路由的下一跳是本接口的链路本地地址，忽略此路由

·*ipv6-address/prefix-length*：此条路由的目的地址和前缀长度

Ignored route *ipv6-address/ prefix-length*.. Default route configured is advertised.

正在发布缺省路由，忽略路由

*[ipv6-address/prefix-length*]：此条路由的目的地址和前缀长度

Unrecognized command received from *interface-type interface-number*

无法识别收到RIPng报文的命令字段

·*interface-type interface-number*：接口类型和编号，从该接口收到RIPng报文

Error occurred while processing received packet

处理接收报文时出错

Must-Be-Zero fields are not zero in header

RIPng报文头Must-Be-Zero字段不等于零

Received packet with invalid length from *ipv6-address*

接收的RIPng报文长度无效

·*ipv6-address*：RIPng报文的源地址

Received packet with invalid version from *ipv6-address*

接收的RIPng报文版本无效

·*ipv6-address*：RIPng报文的源地址

Receiving *packet-type* from *source-ipv6* on *interface-type interface-number*

接收RIPng报文

·*packet-type*：RIPng报文类型，取值为request或response

·*source-ipv6*：接收RIPng报文的源IPv6地址

·*interface-type interface-number*：接口类型和编号，从该接口接收RIPng报文

Response received from *ipv6-address* on invalid UDP port

到来自无效UDP端口的应答报文

·*ipv6-address*：RIPng报文的源地址

Response received from *ipv6-address* has invalid hoplimit

接收的应答报文hoplimit无效

·*ipv6-address*：RIPng报文的源地址

Response received from invalid peer *ipv6-address*

收到来自无效peer的应答报文

·*ipv6-address*：邻居IPv6地址

Request for all route entries

请求全部路由

Next hop *ipv6-address*

路由的下一跳地址

·*ipv6-address*：IPv6地址

Destination *prefix*/*number*

路由项的目的网段前缀

·*prefix/number*：目的网段前缀

Packet: version *packet-version*, command *cmd-value*, length *length*

RIPng报文头信息

·*packet-version*：RIPng报文的版本，取值为1或2

·*cmd-value*：报文类型，取值为request或response

·*length*：报文长度

Dest *prefix/number*, cost *cost*, tag *tag*

路由表项信息

·*prefix/number*：目的网段前缀

·*cost*：此路由的度量值

·*tag*：此路由的标签值

Ignored this response packet. BFD session was not up.

BFD会话没有up，不接收响应报文

Ignored the packet on interface *interface-type interface-number*  due to IPsec profile mismatch

IPsec安全框架不匹配，忽略该报文

·*interface-type interface-number*：接口类型和编号，从该接口收到RIPng报文

【举例】

\# Router A通过GigabitEthernet1/0/1接口与Router B的GigabitEthernet1/0/1接口相连，在Router A上创建RIPng进程1，并在GigabitEthernet1/0/1接口上使能RIPng功能；在Router B上创建RIPng进程，并在GigabitEthernet1/0/1接口上使能RIPng；在Router A上打开RIPng接收报文调试信息开关。

\<RouterA\> debugging ripng 1 receive

\*Nov 22 21:41:02:00 2010 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Receiving response from FE80::200:5EFF:FE71:A706 on GigabitEthernet1/0/1

*[// RIPng*]*进程1从FE80::200:5EFF:FE71:A706收到应答报文，收接口为GigabitEthernet1/0/1*

\*Nov 22 21:41:02:00 2010 RouterA RIPNG/7/RIPNGDEBUG:  Packet : version 1, command response, length 44

*// 接收的应答报文版本1，长度44字节*

\*Nov 22 21:41:02:00 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 22::/64, cost 1, tag 0

*// 第一个路由表项：目的网段22::/64，cost为1，tag为0*

\*Nov 22 21:41:02:00 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 50::/64, cost 1, tag 0

*// 第二个路由表项：目的网段50::/64，cost为1，tag为0*

**RIPng \-- RIPng调试命令 \-- debugging ripng send**

------------------------------------------------------------------------

【命令】

**[debugging ripng** *process-id* **send** [ **interface** *interface-type interface-number* ]]

**[undo debugging ripng** *process-id* **send** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

**[interface***interface-type interface-number*]：接口类型和编号，打开指定接口的RIPng发送报文调试信息开关。如果未指定本参数，将打开所有接口的RIPng发送报文调试信息开关。

【描述】

**[debugging ripng send**]命令用来打开RIPng发送报文调试信息开关。**undo debugging ripng send**命令用来关闭发送报文调试信息开关。

缺省情况下，RIPng发送报文调试信息开关处于关闭状态。

表1-5 debugging ripng send命令输出信息描述表

字段

描述

RIPng *process-id*

RIPng 进程号

Failed to send socket, return value *error-number*

Socket报文发送失败

·*error-number*：发送失败返回值

Sending *packet-type* on *interface-type interface-number* to *dest-ipv6*

发送RIPng报文

·*packet-type*：RIPng报文类型，取值为request或response

·*interface-type interface-number*：接口类型和编号，从该接口发送RIPng报文

·*dest-ipv6*：RIPng报文的目的IPv6地址

Packet: version *packet-version*, command *cmd-value*, length *length*

RIPng报文头信息

·*packet-version*：RIPng报文的版本，取值为1或2

·*cmd-value*：报文类型，取值为request或response

·*length*：报文长度

Destination *prefix/number*, cost *cost*, tag *tag*

路由表项信息

·*prefix/number*：目的网段前缀

·*cost*：此路由的度量值

·*tag*：此路由的标签值

Packets to be sent on interface *interface-type interface-number* have exceeded the limit, possibly causing packet loss

接口下缓存报文数过大

·*interface-type interface-number*：接口类型和编号，从该接口发送RIPng报文

Suppressed update on *sour-ipv6* of *interface-type interface-number*

接口无路由可发

·*sour-ipv6*：RIPng报文的源IPv6地址

·*interface-type interface-number*：接口类型和编号，从该接口发送RIPng报文

Request for all route entries

请求全部路由

Nexthop *ipv6-address*

路由的下一跳地址

·*ipv6-address*：IPv6地址

Must-Be-Zero fields are not zero in header

必为零域不为0

【举例】

\# Router A通过GigabitEthernet1/0/1接口与Router B的GigabitEthernet1/0/1接口相连，在Router A上创建RIPng进程1，并在GigabitEthernet1/0/1接口上使能RIPng功能；在Router B上创建RIPng进程，并在GigabitEthernet1/0/1接口上使能RIPng；在Router A上打开RIPng发送报文调试信息开关。

\<RouterA\> debugging ripng 1 send

\*Nov 22 21:35:29:86 2010 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Sending response on GigabitEthernet1/0/1 to FF02::9

*[// RIPng*]*进程1从接口GigabitEthernet1/0/1向IPv6组播地址FF02::9发送RIPng应答报文*

\*Nov 22 21:35:29:86 2010 RouterA RIPNG/7/RIPNGDEBUG:  Packet : version 1, command response, length 44

*// 应答报文版本1，长度44字节*

\*Nov 22 21:35:29:86 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 22::/64, cost 1, tag 0

*// 第一个路由表项：目的网段22::/64，cost为1，tag为0*

\*Nov 22 21:35:29:86 2010 RouterA RIPNG/7/RIPNGDEBUG:  Destination 33::/64, cost 1, tag 0

*// 第二个路由表项：目的网段33::/64，cost为1，tag为0*

**RIPng \-- RIPng调试命令 \-- debugging ripng timer**

------------------------------------------------------------------------

【命令】

**[debugging ripng** *process-id* **timer**]

**[undo debugging ripng** *process-id* **timer**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【描述】

**[debugging ripng timer**]命令用来打开RIPng定时器调试信息开关。**undo debugging ripng timer**命令用来关闭RIPng定时器调试信息开关。

缺省情况下，RIPng定时器调试信息开关处于关闭状态。

表1-6 debugging ripng timer命令输出信息描述表

字段

描述

RIPng *process-id*

RIPng进程号

Update timer expired

定时更新定时器超时

【举例】

\# 在一台启动了RIPng功能的设备上打开RIPng定时器调试信息开关。

\<RouterA\> debugging ripng 1 timer

\*Oct 18 13:38:32:406 2010 RouterA RIPNG/7/RIPNGDEBUG: RIPng 1 : Update timer expired

*[// RIPng*]*进程1的定时更新定时器超时*
