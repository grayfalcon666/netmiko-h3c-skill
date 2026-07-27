<!-- CMD-INDEX
  debugging mld                       | 用户视图             | L5
-->

**MLD \-- MLD调试命令 \-- debugging mld**

------------------------------------------------------------------------

【命令】

**[debugging** **mld** [ **vpn-instance** *vpn-instance-name*   { **all** \| **done** \| **event** \| **query** [ **receive** \| **send** ] \| **report** \| \| **timer** }]]

**[undo** **debugging** **mld** [ **vpn-instance** *vpn-instance-name*  { **all** \| **done** \| **event** \| **query** [ **receive** \| **send** ] \| **report** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

**[all**]：表示MLD所有调试信息开关。

**[done**]：表示MLD离开组报文调试信息开关。

**[event**]：表示MLD事件调试信息开关。

**[query**]：表示MLD查询报文调试信息开关。

**[receive**]：表示接收的MLD查询报文调试信息开关。

**[send**]：表示发送的MLD查询报文调试信息开关。

**[report**]：表示MLD成员关系报告报文调试信息开关。

**[timer**]：表示MLD定时器调试信息开关。

【描述】

**[debugging** **mld**]命令用来打开MLD调试信息开关。**undo** **debugging** **mld**命令用来关闭MLD调试信息开关。

缺省情况下，MLD调试信息开关处于关闭状态。

表1-1 debugging mld done命令输出信息描述表

字段

描述

Ignore MLD packet from *src* to *dest*

忽略源地址为*src*、目的地址为*dest*的MLD报文

TTL is 0

TTL值为0

length *length* is too short

报文长度*length*太短

Router-Alert option

IPv6选项Router-Alert

interface *interfacename*(*address*)

接口*interfacename*的地址为*address*

done

MLD离开组报文

group address *gaddr* is not in multicast range

组播组g*addr*不是组播地址

group address *gaddr* is reserved

组地址g*addr*为保留地址

group address g*addr* is node-local

组地址g*addr*为节点本地地址

group address g*addr* is link-local

组地址g*addr*为链路本地地址

scope of group address g*addr* is zero

组地址g*addr*的Scope为0

group(*gaddr)*

组播组*gaddr*

this group does not exist

组播组不存在

this group has v1 host

存在MLDv1的主机

fast-leave is off and interface is non-querier

组播组成员快速离开功能处于关闭状态，接口也不是查询器

this group is leaving

组播组正在离开

表1-2 debugging mld event命令输出信息描述表

字段

描述

Create/Add/Remove/Delete MLD configuration interface *interfacename*

创建/添加/移动/删除MLD配置接口*interfacename*

Create /Delete MLD interface *interfacename*(*address*)

创建/删除MLD接口*interfacename*，其地址为*address*

interface *interfacename*(*address*)

接口*interfacename*的地址为*address*

Send/Notify/Receive/Ignore

发送/通知/接收/忽略

*[message-type* message]

*[message-type*]类型的消息，*message-type*包括：

·join-prune：表示加入/剪枝消息

·querier：表示查询器消息

·smooth：表示平滑消息

·smooth over：表示平滑结束消息

·HA：表示高可靠性相关的消息

·MLD enable：表示协议使能消息

·MRIB connection up：表示与MRIB建立连接成功消息

·MRIB connection down：表示与MRIB连接中断消息

·MRIB smooth：表示与MRIB进行平滑消息

·multicast boundary message：表示组播边界消息

·multicast routing-enable：表示三层组播使能消息

·multicast routing-disable：表示三层组播关闭消息

·PIM DR：表示PIM指定路由器消息

MRIB

组播路由信息库

set binary data

设置二进制数据

static-group

添加静态组

open DBM

打开DBM

batch backup data on interface(*interfacename*) configuration

关于接口*interfacename*配置的批量备份数据

batch backup data on global configuration

关于全局配置的批量备份数据

Add/Delete address  *address* for interface *interfacename*

为接口*interfacename*添加/删除地址*address*

(*saddr, gaddr*)

（S，G）表项，*saddr*为源地址，*gaddr*为组地址

group(*gaddr*)

组播组*gaddr*

Change mode from *mode1* to *mode2*

组播组的模式由*mode1*变更为*mode2*，具体模式包括INCLUDE和EXCLUDE

Create group (*gaddr*)

创建组播组*gaddr*

Becomes querier/non-querier

成为查询器/非查询器

Stop event thread

终止事件处理线程

real time backup data

实时备份数据

batch backup data

批量备份数据

HA batch backup event

高可靠性的批量备份事件

HA degrade/stop/upgrade event

高可靠性的降级/停止/升级事件

*[event* event on interface *interfacename*]

接口*interfacename*上发生事件*event*，*event*包括：

·0x1：表示添加接口

·0x2：表示删除接口

·0x3：表示接口down

·0x4：表示接口up

·0x6：表示接口配置变化

·0x9：表示接口解除绑定

·0xa：表示拔出接口

·0xb：表示插入接口

address event *event* on interface *interfacename* (*address*), state is *state*

接口*interfacename*（地址为*address*）上发生地址事件。事件类型为*event*，状态为*state*。

*[event*]包括：

·0x1：表示添加地址

·0x2：表示删除地址

*[state*]包括：

·0x200：表示主地址

·0x400：表示链路本地地址

ifnet connection down event

与接口管理的连接中断事件

Process interface *interfacename* *event*

处理接口*interfacename*上发生的事件*event*，*event*包括：

·add：表示添加

·delete：表示删除

·plugout：表示拔出

·up：表示连接成功

·down：表示连接中断

·attribute changed：表示属性变化

MLD proxy

MLD代理

proxy database

代理成员关系数据库

proxy cache

代理缓存

Create/Delete MLD proxy interface *interfacename*

创建/删除MLD代理接口*interfacename*

Send MLD proxy enable/disable on interface *interfacename* to MRIB

通过接口*interfacename*向MRIB通知使能/关闭MLD代理功能

Add/Remove source(*saddr*) to proxy cache on interface *interfacename* for group(*gaddr*)

在接口*interfacename*上为组节点*gaddr*添加/删除源节点*saddr*到代理缓存

Add/Remove/Update group(*gaddr*) to proxy cache on interface *interfacename*

在接口*interfacename*上添加/删除/更新组节点*gaddr*到代理缓存

Add/Remove source(*saddr*) to proxy database for group(*gaddr*)

在代理成员关系数据库的组节点*gaddr*下添加/删除源*saddr*

Add INCLUDE/EXCLUDE group(*gaddr*) to proxy database

在代理成员关系数据库中添加INCLUDE/EXCLUDE模式的组播组*gaddr*

表1-3 debugging mld query命令输出信息描述表

字段

描述

Ignore MLD packet from *src* to *dest*

忽略源地址为*src*、目的地址为*dest*的MLD报文

TTL is 0

TTL值为0

length *length* is too short

报文长度*length*太短

Router-Alert option

IPv6选项Router-Alert

interface *interfacename*(*address*)

接口*interfacename*的地址为*address*

query

MLD查询报文

length is invalid

报文长度非法

group address is invalid

组地址非法

group address *gaddr* is reserved

组地址*gaddr*为保留地址

group address *gaddr* is node-local

组地址*gaddr*为节点本地地址

group address *gaddr* is link-local

组地址*gaddr*为链路本地地址

general query

MLD普遍组查询

group specific query

MLD特定组查询

group-source specific query

MLD特定源组查询

group *gaddr*

查询的组地址为*gaddr*

source count *num*

源数目为*num*

S flag

查询报文的S标记

表1-4 debugging mld report命令输出信息描述表

字段

描述

Ignore MLD packet from *src* to *dest*

忽略源地址为*src*、目的地址为*dest*的MLD报文

TTL is 0

TTL值为0

length *length* is too short

报文长度*length*太短

Router-Alert option

IPv6选项Router-Alert

interface *interfacename*(*address*)

接口*interfacename*的地址为*address*

group address *gaddr* is not in multicast range

组地址*gaddr*不是组播地址

group address *gaddr* is reserved

组地址*gaddr*为保留地址

group address *gaddr* is node-local

组地址*gaddr*为节点本地地址

group address *gaddr* is link-local

组地址*gaddr*为链路本地地址

scope of group address *gaddr* is scope-none

组地址*gaddr*的Scope为scope-none

group(*gaddr)*

组播组*gaddr*

report

MLD成员关系报告报文

group record

组播组记录

IS_IN/IS_EX/TO_IN/TO_EX/ALLOW/BLOCK

MLDv2报告报文中组记录的类型

number of sources is zero

组播源的数目为0

this group does not exist

组播组不存在

old version host exists

存在低版本主机

fast-leave is off and interface is non-querier

组播组成员快速离开功能处于关闭状态，接口也不是查询器

v1 host exists

存在MLDv1的主机

can\'t pass multicast boundary

不能通过组播边界

can\'t pass group policy

不能通过组播组策略

group address is in SSM range

组地址属于SSM组范围

destination address *addr* is invalid

目的地址*addr*非法

Proxy send

代理发送

Failed to send packet

发送报文失败

表1-5 debugging mld timer命令输出信息描述表

字段

描述

Static group activation timer

静态组激活定时器

Group reset timer

表项清除定时器

Multicast boundary timer

组播边界定时器

Multicast routing enable timer

组播使能定时器

v1/v2 host timer

v1/v2主机存在定时器

Source aging timer

源老化定时器

Group aging timer

组老化定时器

Group retransmit timer

组重传定时器

General query timer

普遍组查询定时器

Source retransmit timer

源重传定时器

Delay timer

延迟发送报告报文定时器

Other/other querier present timer

其它查询器存在时间定时器

Create/Delete/Set/expired

创建/删除/设置/超时

Smooth timer

平滑定时器

Smooth over timer

平滑结束定时器

Proxy database adjust timer

代理成员关系数据库调整定时器

old querier present timer

旧版本查询器的存在时间定时器

【举例】

\# 在接口上使能MLD，并打开公网实例MLD离开组报文调试信息开关。

\<Sysname\> debugging mld done

\*Jun 23 15:01:00:288 2011 Sysname MLD/7/DONE: -MDC=1; Received MLDv1 done for group FF0E::101:101 on interface GigabitEthernet1/0/1(FE80::1:101) (G19849)

*// 接口GigabitEthernet1/0/1收到离开组FF0E::101:101的报文*

\# 在接口上使能MLD，并打开公网实例MLD事件调试信息开关。

\<Sysname\> debugging mld event

\*Jun 23 15:06:16:139 2011 Sysname MLD/7/EVENT: -MDC=1; Create group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) (G102769)

*// 接口GigabitEthernet1/0/2上创建组播组FF0E::101:101*

\*Jun 23 15:06:16:152 2011 Sysname MLD/7/EVENT: -MDC=1; Change mode from INCLUDE to EXCLUDE for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) (G101882)

*// 接口GigabitEthernet1/0/1上组播组FF0E::101:101的模式由INCLUDE变为EXCLUDE*

\*Jun 23 15:06:16:153 2011 Sysname MLD/7/EVENT: -MDC=1; Send JOIN for (::,FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to MRIB (G10105)

*// 通知MRIB接口GigabitEthernet1/0/1上有（::，FF0E::101:101）加入*

\*Jun 23 15:06:39:766 2011 Sysname MLD/7/EVENT: -MDC=1; Change mode from EXCLUDE to INCLUDE for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) (G101789)

*// 接口GigabitEthernet1/0/1上组播组FF0E::101:101的模式由EXCLUDE变为INCLUDE*

\*Jun 23 15:06:39:767 2011 Sysname MLD/7/EVENT: -MDC=1; Send PRUNE for (::,FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to MRIB (G10105)

*// 通知MRIB接口GigabitEthernet1/0/1上有（::，FF0E::101:101）离开*

\# 在接口上使能MLD，并打开公网实例接收MLD查询报文调试信息开关。

\<Sysname\> debugging mld query receive

\*Jun 22 18:31:11:221 2011 Sysname MLD/7/QUERY SEND: -MDC=1; Received MLD  v1 query on GigabitEthernet1/0/1(FE80::1:101) from FE80::1:102 (G10308)

*// 接口GigabitEthernet1/0/1收到MLDv1普遍组查询报文*

\# 在接口上使能MLD，并打开公网实例发送MLD查询报文调试信息开关。

\<Sysname\> debugging mld query send

Jun 23 15:16:32:744 2011 Sysname MLD/7/QUERY SEND: -MDC=1; Send MLD version 1 general query on GigabitEthernet1/0/1(FE80::1:101) to destination FF02::1 (G10308)

*// 接口GigabitEthernet1/0/1发送MLDv1普遍组查询报文*

\# 在接口上使能MLD，并打开公网实例MLD成员关系报告报文调试信息开关。

\<Sysname\> debugging mld report

\*Jun 23 15:55:25:514 2011 Sysname MLD/7/REPORT: -MDC=1; Received MLDv1 report for group FF0E::101:101 on interface GigabitEthernet1/0/1(FE80::1:101) (G19849)

*[//*]*接口GigabitEthernet1/0/1上收到加入组FF0E::101:101的成员关系报告报文*

\# 在接口上使能MLD，并打开公网实例MLD定时器调试信息开关。

\<Sysname\> debugging mld timer

\*Jun 22 18:53:49:129 2011 Sysname MLD/7/TIMER: -MDC=1; Setting v1 host timer for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to 260s (G102089)

*// 接口GigabitEthernet1/0/1设置组FF0E::101:101的MLDv1主机存在定时器*

\*Jun 22 18:55:58:012 2011 Sysname MLD/7/TIMER: -MDC=1;Setting group aging timer for group(FF0E::101:101) on interface GigabitEthernet1/0/1(FE80::1:101) to 260s (G102379)

*// 设置组FF0E::101:101的老化定时器超时*

\*Jun 22 18:56:33:261 2011 Sysname MLD/7/TIMER: -MDC=1; Setting general query timer on interface GigabitEthernet1/0/1(FE80::1:101) to 125s (G10338)

*// 设置接口GigabitEthernet1/0/1的普遍组查询定时器*
