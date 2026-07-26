
**IPv6组播路由与转发 \-- IPv6组播路由与转发调试命令 \-- debugging ipv6 mfib**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 mfib**[ [ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* ] { **all** \| **error** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]]

**[undo debugging ipv6****mfib**[ [ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* ] { **all** \| **error** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[multicast-vlan**]：指定组播VLAN实例。

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

**[all**]：表示IPv6 MFIB（Multicast Forwarding Information Base，组播转发信息库）的所有调试信息开关。

**[error**]：表示IPv6 MFIB错误调试信息开关。

**[no-cache**]：表示IPv6 MFIB未匹配报文调试信息开关。

**[packet**]：表示IPv6 MFIB报文调试信息开关。

**[register**]：表示IPv6 MFIB注册报文调试信息开关。

**[route**]：表示IPv6 MFIB路由调试信息开关。

**[upcall**]：表示IPv6 MFIB上报IPv6 MRIB相关报文调试信息开关。

**[wrong-iif**]：表示IPv6 MFIB错误入接口的调试信息开关。

【描述】

**[debugging ipv6 mfib**]命令用来打开IPv6 MFIB调试信息开关。**undo debugging ipv6 mfib**命令用来关闭IPv6 MFIB调试信息开关。

缺省情况下，IPv6 MFIB调试信息开关处于关闭状态。

需要注意的是，如果未指定**multicast-vlan**和**vpn-instance**参数，表示公网实例。

表1-1 debugging ipv6 mfib error命令输出信息描述表

字段

描述

Failed to allocate memory for add entry/add OIF/RP

添加表项/添加出接口/设置RP时分配内存失败

Failed to create entry (*src*, *dst*)

创建转发表项（*src*，*dst*）失败

Failed to allocate memory for outgoing interface list

创建出接口列表时分配内存失败

Failed to convert outgoing interface list

转换出接口列表失败

Failed to construct driver message

创建下驱动信息失败

Failed to flush entry (*src*, *dst*) to driver

表项（*src*，*dst*）下驱动失败

Failed to get entry (*src*, *dst*) driver statistic

表项（*src*，*dst*）下驱动获取统计信息失败

Failed to write forwarding message to queue

转发消息入队列失败

Multicast hasn\'t been enabled

组播没有使能

Entry (*src*, *dst*) does not found

找不到表项（*src*，*dst*）

(*src*, *dst*) is dummy entry

表项（*src*，*dst*）是临时表项

Entry (*src*, *dst*) does not exist

表项（*src*，*dst*）不存在

表1-2 debugging ipv6 mfib no-cache命令输出信息描述表

字段

描述

Packet (*src*, *dst*) matched nothing

报文（*src*，*dst*）无匹配的转发表项

dropped for invalid address

由于非法源地址而丢弃

dropped for rate limit

由于速率限制而丢弃

dropped for forward queue full

由于转发队列满而丢弃

dropped for total entry limit

由于表项总数限制而丢弃

Matched entry, no need to forward null-reg packet

匹配到表项，不需要转发空注册报文

Matched entry, forward packet

匹配到表项，转发报文

Matched dummy entry, no need to save null-reg packet

匹配临时表项，不需要缓存空注册报文

Matched dummy entry, save packet

匹配临时表项，缓存报文

Dummy limit specific is 0, don\'t create dummy entry

临时表项上限为0，不创建临时表项

No-cache packet is filtered, don\'t encap no-cache upcall

未匹配组播报文被过滤掉，不上报no-cache

表1-3 debugging ipv6 mfib packet命令输出信息描述表

字段

描述

Cache packet for dummy entry (*src*, *dst*)

缓存临时表项（*src*，*dst*）的数据报文

Free cached packet from dummy entry (*src*, *dst*)

释放临时表项（*src*，*dst*）缓存的数据报文

Dummy entry (*src*, *dst*) can\'t cache the packet, dropped it

临时表项（*src*，*dst*）不能缓存报文，将其丢弃

Sent PIM *type* packet (*src*, *dst*) to PIM

上送*type*类型的PIM报文到PIM模块，其中*type*包括：

·Hello

·Register

·RegisterStop

·Join-Prune

·BootStrap

·Assert

·Graft

·GraftAck

·CRP-Advertise

·StateRefresh

·Unknown

Hoplimit(*hoplimit*) of packet (*src*, *dst*) is less than hoplimit threshold(*hoplimit*) on *interface-name*, dropped it

报文（*src*，*dst*）的Hoplimit值小于接口*interface-name*上的Hoplimit阀值，将其丢弃

Forwarded packet (*src*, *dst*) to interface *interface-name*

向接口*interface-name*转发报文（*src*，*dst*）

Dropped packet (*src*, *dst*) for hoplimit is 1

报文（*src*，*dst*）的Hoplimit值为1，将其丢弃

Received packet (*src*, *dst*) from interface *interface-name*, hoplimit is *hoplimit*

在接口*interface-name*收到Hoplimit值为*hoplimit*的报文（*src*，*dst*）

Received a PIM *type* packet, then directly send to PIM module

收到*type*类型的报文直接上送PIM模块，其中*type*包括：

·Hello

·Register

·RegisterStop

·Join-Prune

·BootStrap

·Assert

·Graft

·GraftAck

·CRP-Advertise

·StateRefresh

·Unknow

Received a PIM packet with invalid type *type*

收到非法类型为*type*的PIM报文

Dropped the packet (*src*, *dst*)

丢弃报文（*src*，*dst*）

for hoplimit is 0

Hoplimit值为0

for entry hasn\'t any OIF

表项没有出接口

表1-4 debugging ipv6 mfib register命令输出信息描述表

字段

描述

No RP for (*src, dst*) to send register

（*src*，*dst*）没有RP用于发送注册报文

No local address for (*src, dst*) to send register

（*src*，*dst*）没有本地地址用于发送注册报文

Sent register for (*src, dst*) to RP *rp*

发送（*src*，*dst*）的注册报文到RP *rp*

Sent proxy register for (*src, dst*) to RP *rp*

发送（*src*，*dst*）的代理注册报文到RP *rp*

Sent register-stop packet for (*src, dst*)

发送（*src*，*dst*）的注册停止报文

Dropped register packet for length is 0 or larger than max length *maxlength*

丢弃报文长度为0或大于最大长度*maxlength*的注册报文

Dropped register packet for invalid source address *src*

丢弃非法源地址为*src*的注册报文

Dropped register packet from *src*, for length is wrong: data length is *dlen*(should be larger than *ldlen*), total length is *tlen*(should be *ltlen*)

丢弃从*src*收到的长度错误的注册报文，数据长度是*dlen*（应该大于*ldlen*），总长度是*tlen*（应该是*ltlen*）

Dropped register packet from *src* for checksum error

丢弃从*src*收到的校验和错误的注册报文

Received register packet from *src* to *dst*, with data packet: (*src1, dst2*)

收到从*src*到*dst*的注册报文，其中包含（*src1*，*dst2*）数据

Multicast hasn\'t been enabled, dropped the register packet

组播未使能，丢弃收到的注册报文

表1-5 debugging ipv6 mfib route命令输出信息描述表

字段

描述

Add/Remove OIF *interface-name* to (*src, dst*)

表项（*src*，*dst*）添加/删除出接口*interface-name*

Add/Delete entry (*src, dst*)

添加/删除表项（*src*，*dst*）

Add/Delete dummy entry (*src, dst*)

添加/删除临时表项（*src*，*dst*）

Set IIF *interface-name* to entry (*src, dst*)

设置表项（*src*，*dst*）的入接口为*interface-name*

Change dummy entry (*src, dst*) to normal

临时表项（*src*，*dst*）转换为正式表项

The dummy entry (*src, dst*)  is replaced for route limit(*limit*)

由于达到表项规格（*limit*），临时表项（*src*，*dst*）被正式表项替换

Set/Reset flag *flag* for entry (%s, %s)

设置/清除表项标记*flag*

Set RP (*rp*) for group *group*

设置组*group*的RP为*rp*

Flush entry (*src, dst*) to driver

下发表项（*src*，*dst*）到驱动

Get entry (*src, dst*) driver statistic, matched: *matched*, wrongif: *wrongif*

从驱动获取表项（*src*，*dst*）的统计信息：匹配数为*matched*，错误入接口数为*wrongif*

Reached dummy limit, don\'t create dummy entry

达到临时表项数目上限，不再创建临时表项

Re-add entry (*src, dst*) to driver

重新下刷表项（*src*，*dst*）到驱动

Re-add *num* OIF(s) of entry (*src, dst*) to driver

重新下刷表项（*src*，*dst*）添加*num*个出接口到驱动

Aged dummy entry (*src, dst*)

临时表项（*src*，*dst*）老化

Reached entry limit(*limit*), don\'t add entry (*src, dst*)

达到表项上限,不再添加表项（*src*，*dst*）

Received add-entry/delete-entry message of (*src, dst*)

收到添加/删除表项（*src*，*dst*）消息

OIF num is *num*

出接口数目为*num*

Received set-IIF message of (*src, dst*)

收到设置表项（*src*，*dst*）入接口消息

Received add-OIF/delete-OIF message of (*src, dst*)

收到添加/删除表项（*src*，*dst*）出接口消息

Received set-RP *rp* for group *group* message

收到设置组*group*的RP为*rp*消息

Received set-active/set-inactive message of (*src, dst*)

收到表项（*src*，*dst*）激活/非激活消息

Received set-multicast-enable/set-multicast-disable message on interface *interface-name*

收到接口*interface-name*上使能/去使能消息

Received multicast enable/disable message

收到组播使能/去使能消息

表1-6 debugging ipv6 mfib upcall命令输出信息描述表

字段

描述

Succeeded in sending *type* upcall (*src, dst*)

成功发送（*src*，*dst*）的*type*类型的upcall消息，其中*type*包括：

·no-cache

·wrong-IIF

·SPT-switchover

·source-active

·source-inactive

·reset

表1-7 debugging ipv6 mfib wrong-iif命令输出信息描述表

字段

描述

Packet (*src, dst*) should came from *interface-name*

报文的（*src*，*dst*）正确入接口应该是*interface-name*

dropped for rate limit

由于速率限制而丢弃

dropped for forward queue full

由于转发队列满而丢弃

【举例】

\# 在接口上使能IPv6 PIM-DM，打开公网实例IPv6 MFIB错误调试信息开关。

\<Sysname\> debugging ipv6 mfib error

\*Apr 26 12:53:18:979 2011 Sysname MFIB6/7/DRIVER: -MDC=1;IPv6: Failed to create entry (1::1, ff0e::1). (A062520)

*// 创建转发表项（1::1，FF0E::1）失败*

\# 在接口上使能IPv6 PIM-DM，打开公网实例IPv6 MFIB未匹配报文调试信息开关。

\<Sysname\> debugging ipv6 mfib no-cache

\*Apr 26 12:43:19:09 2011 Sysname MFIB6/7/NOCACHE: -MDC=1; IPv6: Packet (1::1, ff0e::1) matched nothing. (A08303)

*// 收到无匹配转发表项的IPv6组播数据报文（1::1，FF0E::1）*

\*Apr 26 12:43:19:15 2011 Sysname MFIB6/7/NOCACHE: -MDC=1; IPv6: Succeeded in sending no-cache upcall (1::1, ff0e::1). (A08453)

*// 成功发送没有转发表项（1::1，FF0E::1）的upcall消息*

\# 在接口上使能IPv6 PIM-DM，打开公网实例IPv6 MFIB报文调试信息开关。

\<Sysname\> debugging ipv6 mfib packet

\*Apr 26 12:28:50:578 2011 Sysname MFIB6/7/PACKET: -MDC=1; IPv6: Received packet (1::1, ff0e::1) from interface Vlan-interface20, hoplimit is 128. (A012942)

*// 从接口Vlan-interface20收到Hoplimit值为128的IPv6组播数据报文（1::1，FF0E::1）*

\*Apr 26 12:28:50:625 2011 Sysname MFIB6/7/PACKET: -MDC=1; IPv6: Forwarded packet (1::1, ff0e::1) to interface GigabitEthernet1/0/1. (A083551)

*// 将IPv6组播数据报文（1::1，FF0E::1）通过端口GigabitEthernet1/0/1转发出去*

\# 分别在两台设备的接口上使能IPv6 PIM-SM，并配置RP和BSR，打开公网实例IPv6 MFIB注册报文调试信息开关。

\<Sysname\> debugging ipv6 mfib register

\*Apr 26 13:29:33:753 2011 Sysname MFIB6/7/REGISTER: -MDC=1;IPv6: Received register packet from 2::1 to 1::1, with data packet: (2::10, ff0e::1). (A086218)

*// 收到由2::1发往1::1的、封装有IPv6组播数据报文（2::10，FF0E::1）的注册报文*

\*Apr 26 13:29:33:763 2011 Sysname MFIB6/7/REGISTER: -MDC=1;IPv6: Sent register-stop packet for (2::10, ff0e::1). (A085970)

*// 向2::1发送（2::10，FF0E::1）的注册停止报文*

\# 在接口上使能IPv6 PIM-DM，打开公网实例IPv6 MFIB路由调试信息开关。

\<Sysname\> debugging ipv6 mfib route

\*Apr 26 12:39:59:272 2011 Sysname MFIB6/6/ROUTE: -MDC=1; IPv6: Add dummy entry (1::1, ff0e::1). (A07120)

*// 收到无匹配转发表项的IPv6组播数据报文（1::1，FF0E::1），为其创建临时转发表项*

\*Apr 26 12:39:59:297 2011 Sysname MFIB6/6/ROUTE: -MDC=1; IPv6: Received add-entry message of (1::1, ff0e::1), OIF num is 1.(A112030)

*// 收到IPv6 MRIB通知添加（1::1，FF0E::1）表项的消息，表项的出接口数目为1*

\*Apr 26 12:39:59:327 2011 Sysname MFIB6/6/ROUTE: -MDC=1; IPv6: Change dummy entry (1::1, ff0e::1) to normal. (A07391)

*// 删除临时转发表项（1::1，FF0E::1），并添加相应的正式转发表项*

\# 在接口上使能IPv6 PIM-DM，打开公网实例IPv6 MFIB上报IPv6 MRIB相关报文调试信息开关。

\<Sysname\> debugging ipv6 mfib upcall

\*Sep  7 21:10:08:130 2011 Sysname MFIB6/7/UPCALL: -MDC=1; IPv6: Succeeded in sending no-cache upcall (1::1, ff0e::1). (A08453)

*// 向IPv6 MRIB上报未匹配报文（1::1，FF0E::1）的消息*

\# 在接口VLAN-interface40和VLAN-interface60上使能IPv6 PIM-DM，发送相同源组的IPv6组播数据报文，打开公网实例IPv6 MFIB错误入接口调试信息开关。

\<Sysname\> debugging ipv6 mfib wrong-iif

\*Jan 24 04:36:52:990 2011 Sysname MFIB6/7/WRONGIIF: -MDC=1; IPv6: -Slot=3; Packet (1::1, ff0e::1) should came from Vlan-interface40. (A08734)

*[// IPv6*]*组播数据报文（1::1，FF0E::1）正确的入接口应为Vlan-interface40*

**IPv6组播路由与转发 \-- IPv6组播路由与转发调试命令 \-- debugging ipv6 mrib**

------------------------------------------------------------------------

【命令】

**[debugging ipv6** **mrib** [ **vpn-instance** *vpn-instance-name*  { **all** \| **error** \| **event** \| **interface**  *interface-type* *interface-number*  \| **proxy** [ **event** \| **routing-table** ] \| **route**  *advanced-acl6-number*  }]]

**[undo debugging ipv6** **mrib** [ **vpn-instance** *vpn-instance-name*  { **all** \| **error** \| **event** \| **interface** \| **proxy** [ **event** \| **routing-table** ] \| **route** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

**[all**]：表示IPv6 MRIB（Multicast Routing Information Base，组播路由信息库）的所有调试信息开关。

**[error**]：表示IPv6 MRIB错误调试信息开关。

**[event**]：表示IPv6 MRIB事件调试信息开关。

**[interface**]：表示IPv6 MRIB接口管理调试信息开关。

*[interface-type*] *interface-number*：表示指定接口的IPv6 MRIB接口管理调试信息开关。如果未指定本参数，表示所有接口的IPv6 MRIB接口管理调试信息开关。

**[proxy**  [ **event** \| **routing-table** ]]：表示MLD代理调试信息开关，包括事件（**event**）和路由表（**routing-table**）两种。如果未指定**event**和**routing-table**参数，表示同时包括这两种调试信息开关。

**[route**]：表示IPv6 MRIB路由表项调试信息开关。

*[advanced-acl6-number*]：表示IPv6高级ACL的编号，取值范围为3000～3999。

【描述】

**[debugging ipv6 mrib**]命令用来打开IPv6 MRIB调试信息开关。**undo debugging ipv6 mfib**命令用来关闭IPv6 MRIB调试信息开关。

缺省情况下，IPv6 MRIB调试信息开关处于关闭状态。

表1-8 debugging ipv6 mrib error命令输出信息描述表

字段

描述

multicast routing

组播路由

MBoundary

组播边界

MFIB

组播转发信息库

iif

入接口

oif

出接口

spt thres

SPT切换阈值

reg suppress

注册抑制

flush mrt table

下刷路由表

表1-9 debugging ipv6 mrib event命令输出信息描述表

字段

描述

Multicast Boundary

组播边界

Multicast routing

组播路由

MFIB

组播转发信息库

spt thres

SPT切换阈值

reg suppress

注册抑制

Add msg to ipc buffer

向IPC缓冲区中添加一个消息

Send msg to MFIB success

成功向MFIB发送一个消息

Type

消息类型

Len

消息长度

Count

消息数量

表1-10 debugging ipv6 mrib interface命令输出信息描述表

字段

描述

Succeed in adding interface *interface*

成功添加接口*interface*

Remove interface *interface*

删除接口*interface*

Create interface address for (*interface*, *address*), reference *cnt*

创建接口*interface*的地址为*address*，引用计数为*cnt*

Remove interface address *address* of *interface*

删除接口*interface*的地址*address*

Create interface address for (*interface*, *address*) while exist, reference *cnt*

创建接口地址时，地址已经存在，增加它的引用计数为*cnt*

Create interface address for (*interface*, *address*) when sending message, reference *cnt*

发送接口变化消息时，创建接口地址，引用计数为*cnt*

Create interface address for (*interface*, *address*) when getting by index, reference *cnt*

根据接口索引获取接口上的接口地址时，创建接口地址，引用计数为*cnt*

Create interface address for (*interface*, *address*) when getting by address, reference *cnt*

根据全局IPv6地址获取接口上的接口地址时，创建接口地址，引用计数为*cnt*

Destroy interface address for (*interface*, *address*) when deleting it, reference *cnt*

销毁接口地址，引用计数为*cnt*

Create interface address for (*interface*, *address*) at (*file*, *line*), reference *cnt*

在文件*file*的*line*引用行创建接口地址，引用计数为*cnt*

Failed to create interface

创建接口失败

Succeed in adding PIM interface *interface*

成功添加IPv6 PIM接口*interface*

Remove PIM interface *interface*

删除IPv6 PIM接口*interface*

Enable/Disable protocol packet deliver up on interface *interface*

使能/关闭接口*interface*的IPv6 PIM协议功能

Succeed in enabling/disabling PIM packet to CPU for interface *interface*

使能/关闭接口*interface*的IPv6 PIM协议功能成功

PIM interface *interface* is up/down

IPv6 PIM接口*interface*生效/失效

No address or memory for PIM interface *interface*

接口*interface*没有配置地址或内存不足

Message to add(*type*) interface *interface*

收到接口*interface*添加消息，消息子类型为*type*

Message to up interface *interface*

收到接口*interface*生效消息

Message to down(*type*) interface *interface*

收到接口*interface*失效消息，消息子类型为*type*

Message to change configuration of interface *interface*

收到接口*interface*配置变化消息

Ignore non-primary or borrow address of *interface*, state *state*

忽略从地址和借用地址逻辑接口变化消息

Message to add/delete address *address*/*masklen* (*interface*)

接口*interface*添加/删除地址*address*/*masklen*消息

Message to up/down vlink interface *interface*

Vlink接口*interface *up/down消息

Vlink state of interface *interface* is not up, state *state*

Vlink接口*interface*状态不是up状态，状态为*state*

Succeed in creating basic interface *interface*

创建基本接口（注册口、Null0接口等）

Succeed in destroying basic interface *interface*

删除基本接口*interface*

Try to enable/disable protocol *pro* on interface *interface*

尝试在接口*interface*上使能/关闭协议*pro*

表1-11 debugging ipv6 mrib proxy命令输出信息描述表

字段

描述

Process gmp querier enable/disable for interface *interface*

为接口*interface*使能/关闭查询器

Notify proxy up/down message on interface *interface*

通报代理接口*interface*生效/失效消息

Add proxy interface for interface *interface*

在接口*interface*上添加代理功能

Process proxy enable/disable message on interface *interface*

在接口*interface*上处理代理功能使能/关闭消息

Delete proxy interface on interface *interface*

在接口*interface*上删除代理接口

Proxy interface logup/logdown for interface *interface*

代理接口*interface*逻辑up/逻辑down

Notify proxy enable/disable message

通报代理功能使能/关闭消息

Proxy routing-table adjust timer expired

代理路由表重整定时器超时

Create/Delete proxy routing-table relate interface: *interface*

在接口*interface*上创建/删除代理路由表

Create/Delete proxy routing-table adjust timer(*time*)

创建/删除代理路由表重整定时器（时间值为*time*）

Could not find (\*,*group*), ignore the prune message

没有找到（\*，*group*）表项，忽略剪枝报文

Receive gmp aux/ex join/prune for (*source*, *group*) on *interface*

在接口*interface*上收到（*source*，*group*）表项的加入/剪枝报文

Relate group *group* to proxy interface: *interface*

将组*group*与代理接口*interface*相关联

Relate group *group* to niif list

将组*group*与空接口列表相关联

Create/Delete proxy routing-table (*source*, *group*)

创建/删除代理路由表项（*source*，*group*）

Failed to create entry (*source*, *group*) for reaching route limit

由于超出规格，创建表项（*source*，*group*）创建失败

Add/Delete/Set iif: *interface* for (*source*, *group*)

为表项（*source*，*group*）添加/删除/更改入接口，并与该表项关联/解绑/重关联

Cannot add downstream *interface* for (*source*, *group*), since it is not in the immediate olist

由于表项（*source*，*group*）不在直接出接口列表中，因此不能为该表项添加下游接口*interface*

Cannot delete downstream *interface* for (*source*, *group*), since it is in the immediate olist

由于表项（*source*，*group*）在直接出接口列表中，因此不能为该表项删除下游接口*interface*

Add/Delete oif: *interface* for (*source*, *group*)

为表项（*source*，*group*）添加/删除出接口*interface*

Notify MRIB to add/delete oif *interface* before adding entry (*source*, *group*)

在添加表项（*source*，*group*）之前，就通知MRIB添加/删除出接口*interface*

Process multicast boundary message on proxy interface *interface*

在接口*interface*上处理组播边界消息

Create multicast boundary timer on proxy interface *interface*

在接口*interface*上创建组播边界定时器

Multicast boundary timer on interface *interface* expired

接口*interface*上的组播边界定时器超时

Process MFIB/MRIB reset entry message

处理MFIB/MRIB表项删除消息

Create flush entry timer

创建表项下刷定时器

Proxy flush entry timer expired

表项下刷定时器超时

Delete all expand oif from sg entry when delete (\*, *group*)

在删除（\*，*group*）表项时，同时删除对应（S，G）表项中的扩展出接口

表1-12 debugging ipv6 mrib route命令输出信息描述表

字段

描述

iif

入接口

oif

出接口

Merge state

抵消状态

spt thres

SPT切换阈值

reg suppress

注册抑制

【举例】

\# 在接口上使能IPv6 PIM-SM，并打开公网实例IPv6 MRIB事件调试信息开关。

\<Sysname\> debugging ipv6 mrib event

\*Sep  7 15:59:02:172 2011 Sysname MRIB6/7/EVENT: -MDC=1; IPv6: Add msg(Type: add mfib, Len: 146) to ipc buffer(Count: 1) (M02346)

*// 向IPC缓冲区中添加一个消息（消息类型为：往MFIB添加表项，长度为146）*

\*Sep  7 15:59:02:185 2011 Sysname MRIB6/7/EVENT: -MDC=1; IPv6: Send msg to MFIB(Count 1, Len 158) success (M02272)

*// 成功向MFIB发送一个消息（数量为1，长度为158）*

\# 在接口上使能IPv6 PIM-SM，并打开公网实例IPv6 MRIB接口管理调试信息开关。

\<Sysname\> debugging ipv6 mrib interface

\*Oct 30 06:16:27:689 2012 Sysname MRIB6/7/IFM: -MDC=1; IPv6: Try to enable protocol 0x2 on interface GigabitEthernet1/0/1. (PM055007)

*// 尝试在接口GigabitEthernet1/0/1上使能IPv6 PIM-SM（protocol 0x2）协议*

\*Oct 30 06:16:27:689 2012 Sysname MRIB6/7/IFM: -MDC=1; IPv6: Create interface address for (GigabitEthernet1/0/1, 7:11::1) when sending message, reference 1. (PM052755)

*// 增加接口地址引用计数，用于发送接口变化消息*

\*Oct 30 06:16:27:695 2012 Sysname MRIB6/7/IFM: -MDC=1; IPv6: Succeed in adding interface GigabitEthernet1/0/1. (PM052427)

*// 成功添加接口GigabitEthernet1/0/1的生效IPv6 PIM接口*

\# 在接口上使能MLD代理功能，并打开公网实例MLD代理调试信息开关。

\<Sysname\> debugging ipv6 mrib proxy

\*Jul  8 18:19:00:393 2013 Sysname MRIB6/7/PRY_RT: -MDC=1; IPv6: Relate group FF1E::1 to nonif list. (MP051207)

*// 将组FF1E::1与空接口列表相关联*

\*Jul  8 18:19:00:393 2013 Sysname MRIB6/7/PRY_EVT: -MDC=1; IPv6: Delete proxy routing-table relate interface: Vlan-interface33. (MP05821)

*// 在接口Vlan-interface33上删除代理路由表*

\# 在接口上使能IPv6 PIM-SM，并打开公网实例IPv6 MRIB路由表项调试信息开关。

\<Sysname\> debugging ipv6 mrib route

\*Sep  7 15:59:02:143 2011 Sysname MRIB6/7/ROUTE: -MDC=1; IPv6: Proc add entry (7:11::6,FFE3::101) msg with iif GigabitEthernet1/0/1(Oifs 1,RP 8:12::1) (M032579)

*// 处理添加表项（7:11::6，FFE3::101）消息，表项入接口为GigabitEthernet1/0/1（出接口数量为1，RP地址为8:12::1）*

\*Sep  7 15:59:02:169 2011 Sysname MRIB6/7/ROUTE: -MDC=1; IPv6: Add oif GigabitEthernet1/0/1(Status ADD) to entry (7:11::6,FFE3::101) (M032419)

*// 将出接口GigabitEthernet1/0/1（状态为ADD）添加到表项（7:11::6，FFE3::101）中*
