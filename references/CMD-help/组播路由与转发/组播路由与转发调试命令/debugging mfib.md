
**组播路由与转发 \-- 组播路由与转发调试命令 \-- debugging mfib**

------------------------------------------------------------------------

【命令】

**[debugging mfib**[ [ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* ] { **all** \| **error** \| **mtunnel** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]]

**[undo debugging mfib**[ [ **multicast-vlan** \| **vpn-instance** *vpn-instance-name* ] { **all** \| **error** \| **mtunnel** \| **no-cache** \| **packet** \| **register** \| **route** \| **upcall** \| **wrong-iif** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[multicast-vlan**]：指定组播VLAN实例。

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

**[all**]：表示MFIB（Multicast Forwarding Information Base，组播转发信息库）的所有调试信息开关。

**[error**]**：**表示MFIB错误调试信息开关。

**[mtunnel**]：表示MFIB MTI（Multicast Tunnel Interface，组播隧道接口）接口调试信息开关。

**[no-cache**]：表示MFIB未匹配报文调试信息开关。

**[packet**]：表示MFIB报文调试信息开关。

**[register**]：表示MFIB注册报文调试信息开关。

**[route**]：表示MFIB路由调试信息开关。

**[upcall**]：表示MFIB上报MRIB相关报文调试信息开关。

**[wrong-iif**]：表示MFIB错误入接口的调试信息开关。

【描述】

**[debugging mfib**]命令用来打开MFIB调试信息开关。**undo debugging mfib**命令用来关闭MFIB调试信息开关。

缺省情况下，MFIB调试信息开关处于关闭状态。

需要注意的是，如果未指定**multicast-vlan**和**vpn-instance**参数，表示公网实例。

表1-1 debugging mfib error命令输出信息描述表

字段

描述

failed

失败

not found

没有查到

dummy entry

空转发表项

(*sadd, gadd*)

（S，G）表项

Memory allocation

内存分配

表1-2 debugging mfib mtunnel命令输出信息描述表

字段

描述

MTunnel create

通知驱动创建MTI接口

MTunnel delete

通知驱动删除MTI接口

MTunnel up

通知驱动MTI接口up

MTunnel down

通知驱动MTI接口down

source addr

封装的源地址

group addr

封装的目的地址

表1-3 debugging mfib no-cache命令输出信息描述表

字段

描述

NoCache packet

未匹配的组播数据报文

Report NoCache upcall

上报未知组播数据报文信息

(*sadd, gadd*)

（S，G）表项

表1-4 debugging mfib packet命令输出信息描述表

字段

描述

Dropping

丢弃组播数据报文

received

收到组播数据报文

(*sadd, gadd*)

（S，G）表项

TTL

报文的TTL值

表1-5 debugging mfib register命令输出信息描述表

字段

描述

Send

发送

Dropping

丢弃

register

注册报文

register-stop

注册停止报文

(*sadd, gadd*)

（S，G）表项

表1-6 debugging mfib route命令输出信息描述表

字段

描述

add-entry message

添加表项消息

delete-entry message

删除表项消息

set-IIF message

更改入接口消息

delete-OIF message

删除出接口消息

add-OIF message

添加出接口消息

(*sadd, gadd*)

（S，G）表项

表1-7 debugging mfib upcall命令输出信息描述表

字段

描述

Report NoCache upcall

上报未知组播报文信息

(*sadd, gadd*)

（S，G）表项

表1-8 debugging mfib wrong-iif命令输出信息描述表

字段

描述

WrongIF packet

从错误入接口收到组播数据报文

(*sadd, gadd*)

（S，G）表项

【举例】

\# 在接口上使能PIM-DM，打开公网实例MFIB错误调试信息开关。

\<Sysname\> debugging mfib error

\*Apr 26 12:53:18:967 2000 Sysname MFIB/7/ERROR: -MDC=1; Memory allocation is failed (A062115)

*// 分配内存失败*

\*Apr 26 12:53:18:979 2000 Sysname MFIB/7/DRIVER: -MDC=1; Failed to create entry （3.4.5.6，226.1.1.1）. (A062520)

*// 创建转发表项（3.4.5.6，226.1.1.1）失败*

\# 打开公网实例MFIB MTI接口调试信息开关。

\<Sysname\> debugging mfib mtunnel

\*Apr 26 12:53:18:967 2000 Sysname MFIB/7/MTUNNEL: -MDC=1; MTunnel create, ifindex=469. (A20732)

*// 通知驱动创建MTI接口*

\*Apr 26 12:53:18:967 2000 Sysname MFIB/7/MTUNNEL: -MDC=1; MTunnel up, ifindex=469, source addr=1.1.1.1, group addr=239.1.1.1. (A20788)

*// 通知驱动MTI接口up，封装的源地址为1.1.1.1，封装的目的地址为239.1.1.1*

\# 在接口上使能PIM-DM，打开公网实例MFIB未匹配报文调试信息开关。

\<Sysname\> debugging mfib no-cache

\*Apr 26 12:43:19:09 2000 Sysname MFIB/7/NO-CACHE: -MDC=1; Packet （3.4.5.6，226.1.1.1） matched nothing (A08303)

*// 收到无匹配转发表项的组播数据报文（3.4.5.6，226.1.1.1）*

Succeeded to send no-cache upcall (3.4.5.6，226.1.1.1) (A08453)

*// 向PIM上报没有转发表项（3.4.5.6，226.1.1.1）的信息*

\# 在接口上使能PIM-DM，打开公网实例MFIB报文调试信息开关。

\<Sysname\> debugging mfib packet

\*Apr 26 12:28:50:578 2000 Sysname MFIB/7/PACKET: -MDC=1; Receive packet (3.4.5.6，226.1.1.1) from interface Vlan-interface20, ttl is 128 (A012942)

*// 从接口Vlan-interface20收到TTL值为128的组播数据报文（3.4.5.6，226.1.1.1）*

\*Apr 26 12:28:50:625 2000 Sysname MFIB/7/PACKET: -MDC=1; Forward multicast packet (3.4.5.6, 226.1.1.1) on GigabitEthernet1/0/1 (A083551)

*// 将组播数据报文（3.4.5.6，226.1.1.1）通过端口GigabitEthernet1/0/1转发出去*

\# 分别在两台设备的接口上使能PIM-SM，并配置RP和BSR，打开公网实例MFIB注册报文调试信息开关。

\<Sysname\> debugging mfib register

\*Apr 26 13:29:33:753 2000 Sysname MFIB/7/REGISTER:-MDC=1; Received register packet from 22.1.1.1 to 10.1.1.1, with data packet: (22.1.1.10, 226.1.1.1)(A086218)

*// 收到由22.1.1.1发往10.1.1.1的、封装有组播数据报文（22.1.1.10，226.1.1.1）的注册报文*

\*Apr 26 13:29:33:763 2000 Sysname MFIB/7/REGISTER:-MDC=1; Send register-stop packet to 22.1.1.1 for (22.1.1.10, 226.1.1.1).(A085970)

*// 向22.1.1.1发送（22.1.1.10，226.1.1.1）的注册停止报文*

\# 在接口上使能PIM-DM，打开公网实例MFIB路由调试信息开关。

\<Sysname\> debugging mfib route

\*Apr 26 12:39:59:272 2000 Sysname MFIB/6/ROUTE: -MDC=1; Add dummy entry (3.4.5.6, 226.1.1.1)(A07120)

*// 收到无匹配转发表项的组播数据报文（3.4.5.6，226.1.1.1），为其创建临时转发表项*

\*Apr 26 12:39:59:297 2000 Sysname MFIB/6/ROUTE: -MDC=1; Receive add-entry message of entry (3.4.5.6, 226.1.1.1), oif num is 1.(A112030)

*// 收到MRIB通知添加（3.4.5.6，226.1.1.1）表项的消息，表项的出接口数目为1*

\*Apr 26 12:39:59:327 2000 Sysname MFIB/6/ROUTE: -MDC=1; Change dummy entry (3.4.5.6, 226.1.1.1) to normal (A07391)

*// 删除临时转发表项（3.4.5.6，226.1.1.1），并添加相应的正式转发表项*

\# 在接口上使能PIM-DM，打开公网实例MFIB上报MRIB相关报文调试信息开关。

\<Sysname\> debugging mfib upcall

\*Sep  7 21:10:08:130 2006 Sysname MFIB/7/UPCALL: -MDC=1; Succeeded to send no-cache upcall (3.4.5.6, 226.1.1.1) (A08453)

*// 向MRIB上报未匹配报文（3.4.5.6，226.1.1.1）的消息*

\# 在接口VLAN-interface40和VLAN-interface60上使能PIM-DM，发送相同源组的组播数据报文，打开公网实例MFIB错误入接口调试信息开关。

\<Sysname\> debugging mfib wrong-iif

\*Jan 24 04:36:52:990 2003 Sysname MFIB/7/WRONGIIF: -MDC=1; Slot=3; WRONG_IF packet (10.11.113.168, 226.1.1.1) received on Vlan-interface60, should from Vlan-interface40(A08734)

*// 从错误入接口Vlan-interface60收到组播数据报文（10.11.113.168，226.1.1.1），正确的入接口应为Vlan-interface40*

**组播路由与转发 \-- 组播路由与转发调试命令 \-- debugging mrib**

------------------------------------------------------------------------

【命令】

**[debugging mrib** [ **vpn-instance** *vpn-instance-name*  { **all** \| **error** \| **event** \| **interface**  *interface-type* *interface-number*  \| **proxy** [ **event** \| **routing-table** ] \| **route**  *advanced-acl-number*  }]]

**[undo debugging mrib** [ **vpn-instance** *vpn-instance-name*  { **all** \| **error** \| **event** \| **interface** \| **proxy** [ **event** \| **routing-table** ] \| **route** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

**[all**]：表示MRIB（Multicast Routing Information Base，组播路由信息库）的所有调试信息开关。

**[error**]：表示MRIB错误调试信息开关。

**[event**]：表示MRIB事件调试信息开关。

**[interface**]：表示MRIB接口管理调试信息开关。

*[interface-type*] *interface-number*：表示指定接口的MRIB接口管理调试信息开关。如果未指定本参数，表示所有接口的MRIB接口管理调试信息开关。

**[proxy**  [ **event** \| **routing-table** ]]：表示IGMP代理调试信息开关，包括事件（**event**）和路由表（**routing-table**）两种。如果未指定**event**和**routing-table**参数，表示同时包括这两种调试信息开关。

**[route**]：表示MRIB路由表项调试信息开关。

*[advanced-acl-number*]：表示IPv4高级ACL的编号，取值范围为3000～3999。

【描述】

**[debugging mrib**]命令用来打开MRIB调试信息开关。**undo debugging mfib**命令用来关闭MRIB调试信息开关。

缺省情况下，MRIB调试信息开关处于关闭状态。

表1-9 debugging mrib error命令输出信息描述表

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

表1-10 debugging mrib event命令输出信息描述表

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

表1-11 debugging mrib interface命令输出信息描述表

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

根据全局IP地址获取接口上的接口地址时，创建接口地址，引用计数为*cnt*

Destroy interface address for (*interface*, *address*) when deleting it, reference *cnt*

销毁接口地址，引用计数为*cnt*

Create interface address for (*interface*, *address*) at (*file*, *line*), reference *cnt*

在文件*file*的*line*引用行创建接口地址，引用计数为*cnt*

Failed to create interface

创建接口失败

Succeed in adding PIM interface *interface*

成功添加PIM接口*interface*

Remove PIM interface *interface*

删除PIM接口*interface*

Enable/Disable protocol packet deliver up on interface *interface*

使能/关闭接口*interface*的PIM协议功能

Succeed in enabling/disabling PIM packet to CPU for interface *interface*

使能/关闭接口*interface*的PIM协议功能成功

PIM interface *interface* is up/down

PIM接口*interface*生效/失效

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

表1-12 debugging mrib proxy命令输出信息描述表

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

Relate (*source*, *group*) to proxy interface: *interface*

将组*group*与代理接口*interface*相关联

Relate (*source*, *group*) to niif list

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

表1-13 debugging mrib route命令输出信息描述表

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

\# 在接口上使能PIM-SM，并打开公网实例MRIB事件调试信息开关。

\<Sysname\> debugging mrib event

\*Dec 10 17:15:08:494 2010 Sysname MRIB/7/EVENT: -MDC=1; Add msg(Type: add mfib, Len: 146) to ipc buffer(Count: 1) (M02333)

*// 向IPC缓冲区中添加一个消息（消息类型为：往MFIB添加表项，长度为146）*

\*Dec 10 17:15:08:502 2010 Sysname MRIB/7/EVENT: -MDC=1; Send msg to MFIB(Count 1, Len 158) success (M02258)

*// 成功向MFIB发送一个消息（数量为1，长度为158）*

\# 在接口上使能PIM-SM，并打开公网实例MRIB接口管理调试信息开关。

\<Sysname\> debugging mrib interface

\*Oct 30 06:16:27:689 2012 Sysname MRIB/7/IFM: -MDC=1; Try to enable protocol 0x2 on interface GigabitEthernet1/0/1. (PM055007)

*// 尝试在接口GigabitEthernet1/0/1上使能PIM-SM（protocol 0x2）协议*

\*Oct 30 06:16:27:689 2012 Sysname MRIB/7/IFM: -MDC=1; Create interface address for (GigabitEthernet1/0/1, 7.11.0.1) when sending message, reference 1. (PM052755)

*// 增加接口地址引用计数，用于发送接口变化消息*

\*Oct 30 06:16:27:695 2012 Sysname MRIB/7/IFM: -MDC=1; Succeed in adding PIM interface GigabitEthernet1/0/1. (PM052427)

*// 成功添加接口GigabitEthernet1/0/1的生效PIM接口*

\# 在接口上使能IGMP代理功能，并打开公网实例IGMP代理调试信息开关。

\<Sysname\> debugging mrib proxy

\*May 10 18:20:44:858 2013 Sysname MRIB/7/PRY_RT: -MDC=1; Relate group 225.0.0.1 to nonif list. (MP051207)

*// 将组225.0.0.1与空接口列表相关联*

\*May 10 18:20:44:858 2013 Sysname MRIB/7/PRY_EVT: -MDC=1; Delete proxy routing-table relate interface: Vlan-interface22. (MP05589)

*// 在接口Vlan-interface22上删除代理路由表*

\# 在接口上使能PIM-SM，并打开公网实例MRIB路由表项调试信息开关。

\<Sysname\> debugging mrib route

\*Dec 10 17:15:08:390 2010 Sysname MRIB/7/ROUTE: -MDC=1; Proc add entry (2.1.1.1,225.0.0.25) msg with iif GigabitEthernet1/0/1(Oifs 1,RP 2.1.1.5) (M032598)

*// 处理添加表项（2.1.1.1，225.0.0.25）消息，表项入接口为GigabitEthernet1/0/1（出接口数量为1，RP地址为2.1.1.5）*

\*Dec 10 17:15:08:413 2010 Sysname MRIB/7/ROUTE: -MDC=1; Add oif GigabitEthernet1/0/1(Status ADD) to entry (2.1.1.1,225.0.0.25) (M032440)

*// 将出接口GigabitEthernet1/0/1（状态为ADD）添加到表项（2.1.1.1，225.0.0.25）中*
