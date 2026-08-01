<!-- CMD-INDEX
  debugging igmp-snooping             | 用户视图             | L6
  debugging l2mf                      | 用户视图             | L1054
-->

**IGMP Snooping \-- IGMP Snooping调试命令 \-- debugging igmp-snooping**

------------------------------------------------------------------------

【命令】

**[debugging igmp-snooping **[{ **all** \| **entry** \| **error** \| **event** \| **fsm** \| **group** \| **packet** [ **vlan** *vlan-id* [ **port** *interface-type interface-number* ] \| **vsi** *vsi-name* ] \| **sync** \| **timer** }]]

**[undo debugging igmp-snooping **[{ **all** \| **entry** \| **error** \| **event** \| **fsm** \| **group** \| **packet** \| **sync** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IGMP Snooping所有调试信息开关。

**[entry**]：表示IGMP Snooping表项调试信息开关。

**[error**]：表示IGMP Snooping错误调试信息开关。

**[event**]：表示IGMP Snooping事件调试信息开关。

**[fsm**]：表示IGMP Snooping状态机调试信息开关。

**[group**]：表示IGMP Snooping组播组调试信息开关。

**[packet**]：表示IGMP Snooping报文调试信息开关。

**[vlan** *vlan-id*]：指定VLAN。*vlan-id*为VLAN的编号，取值范围为1～4094。如果未指定本参数，表示所有VLAN。

**[port** *interface-type interface-number*]：指定端口，*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，表示所有端口。

**[vsi** *vsi-name*]：指定VSI。*vsi-name*为VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示所有VSI。

**[sync**]：表示IGMP Snooping板间消息同步调试信息开关。

**[timer**]：表示IGMP Snooping定时器调试信息开关。

【描述】

**[debugging igmp-snooping**]命令用来打开IGMP Snooping调试信息开关。**undo debugging igmp-snooping**命令用来关闭IGMP Snooping调试信息开关。

缺省情况下，IGMP Snooping调试信息开关处于关闭状态。

表1-1 debugging igmp-snooping entry命令输出信息描述表

字段

描述

Create IP entry (*source*, *group*) on *vlan*

在VLAN *vlan*上创建IP表项（*source*，*group*）

Create router entry on *vlan*

在VLAN *vlan*上创建路由器表项

Create MAC entry *mac* on *vlan*

在VLAN *vlan*上创建MAC表项

Delete IP entry (*source*, *group*) from *vlan*

从VLAN *vlan*中删除IP表项（*source*，*group*）

Delete router entry from *vlan*

从VLAN *vlan*中删除路由器表项

Delete port *port* from MAC entry *mac*

从MAC表项*mac*中删除端口*port*

Delete (*source*, *group*) from driver

从驱动中删除表项（*source*，*group*）

Delete (*source*, *group*) ports from driver

从驱动中删除端口（*source*，*group*）

Delete (*source*, *group*) slot from driver

从驱动中删除板（*source*，*group*）

Delete MAC entry *mac* from driver

从驱动中删除MAC表项*mac*

Delete *mac* ports from driver

从驱动中删除端口*mac*

Delete *mac* slot from driver

从驱动中删除板*mac*

Delete IP entry (*source*, *group*) from the noresource list

从无资源列表中删除IP表项（*source*，*group*）

Delete IP entry (*source*, *group*) from IP fail list

从IP失败列表中删除IP表项（*source*，*group*）

Add port *port* to (*source*, *group*) on *vlan*

添加端口*port*到VLAN *vlan*中的表项（*source*，*group*）

Add port *port* to MAC *mac*

添加端口*port*到MAC表项*mac*

Add IP ports from (*source*, *group*) to driver

通知驱动添加端口到IP表项（*source*，*group*）

Add IP slot from (*source*, *group*) to driver

通知驱动添加板到IP表项（*source*，*group*）

Add MAC ports from *mac* to driver

通知驱动添加端口到MAC地址*mac*

Add *mac* slot to driver

通知驱动添加板到MAC地址*mac*

Add IP entry (*source*, *group*) to IP fail list

添加IP表项（*source*，*group*）到IP失败列表

Add *mac* to MAC fail list

添加MAC地址*mac*到MAC失败列表

Add IP entry (*source*, *group*) to driver

通知驱动添加IP表项（*source*，*group*）

Add MAC *mac* to driver

通知驱动添加MAC地址*mac*

Add IP entry (*source*, *group*) for the first time

第一时间添加IP表项（*source*，*group*）

Copy router resource to (*source*, *group*)

复制路由器资源到表项（*source*，*group*）

Copy router resource to *mac*

复制路由器资源到*mac*

Copy (\*,G) protocol resource to (*source*, *group*)

复制（\*，G）协议资源到表项（*source*，*group*）

Copy (\*,G) info to All (S,G) on *vlan*

复制（\*，G）信息到VLAN *vlan*上所有（S，G）

Copy (\*,G) protocol slot to All (S,G) on *vlan*

复制（\*，G）协议板到VLAN *vlan*上所有（S，G）

Copy router ports to all entry on *vlan*

复制路由器端口到VLAN *vlan*上所有表项

Copy router slot to all entry on *vlan*

复制路由器板到VLAN *vlan*上所有表项

Remove (\*,G) info from All (S,G) on *vlan*

在VLAN *vlan*上从所有（S，G）表项中删除（\*，G）信息

Remove (\*,G) protocol ports from All (S,G) on *vlan*

在VLAN *vlan*上从所有（S，G）表项中删除（\*，G）协议端口

Remove (\*,G) protocol slot from All (S,G) on *vlan*

在VLAN *vlan*上从所有（S，G）表项中删除（\*，G）协议板

Remove router ports from all entry on *vlan*

在VLAN *vlan*上从所有表项中删除路由器端口

Remove router slot from all entry on *vlan*

在VLAN *vlan*上从所有表项中删除路由器板

Driver hasn\'t enough resource for (*source*, *group*)

存储表项（*source*，*group*）的驱动资源不足

Notify kernel *version* enable/disable

通知内核版本*version*使能/关闭

Insert port *port* to tree

将端口*port*插入树

Can\'t find port *port*

无法找到端口*port*

connect group *group* with MAC entry *mac*

关联组地址*group*和MAC表项*mac*

表1-2 debugging igmp-snooping error命令输出信息描述表

字段

描述

Multicast address is invalid

组播地址非法

Wrong IGMPv*n* report packet which receive from port *port* on *vlan*

在VLAN *vlan*的端口*port*上收到错误的版本为*n*的IGMP加入报文

Failed to create Dynamic group (*source*, *group*) on *vlan*

在VLAN *vlan*上创建动态表项（*source*，*group*）失败

Failed to create host response timer on group *group* of port *port* in *vlan*.

在VLAN *vlan*的端口*port*上为组*group*创建查询响应定时器失败

Failed to add host port *port* to (*source*, *group*) on *vlan*

在VLAN *vlan*上添加端口*port*到动态表项（*source*，*group*）失败

Failed to notify add host slot slot of (*source*, *group*) to other on *vlan*

在VLAN *vlan*上通知其它板添加表项（*source*，*group*）的成员板失败

Failed to add entry (*source*, *group*) to MSIB on *vlan*

在VLAN *vlan*上添加MSIB表项（*source*，*group*）失败

Failed to update dbm data

更新DBM数据失败

Failed to recover global *config* snooping disable

全局配置*config*恢复时失败

Failed to parse message

解析消息失败

Failed to get port type

获取接口类型失败

表1-3 debugging igmp-snooping event命令输出信息描述表

字段

描述

Successfully enable/disable IGMP snooping on *vlan*

在VLAN *vlan*上使能/关闭IGMP Snooping成功

Received get level2 multicast IP/mac group message

收到获取二层组播IP/MAC组信息

Received IGMP snooping debug message

收到IGMP Snooping调试信息

Received IGMP snooping group message

收到IGMP Snooping组信息

Received IGMP snooping router port message

收到IGMP Snooping路由器端口信息

Received ha-upgrade event

收到HA升级事件

Received interface/slot/vlan event (Event:*event,* Sequence*=sequence*)

收到接口/板/VLAN事件（事件为*event*，序列号为*sequence*）

Global IGMP snooping is enabled

IGMP Snooping已全局使能

IGMP snooping is disabling globally

IGMP Snooping正在全局关闭

IGMP snooping is enabled/disabled on *vlan*

IGMP Snooping在VLAN *vlan*上已使能/关闭

Successfully enable multicast globally in driver

在驱动上全局使能组播成功

Successfully call driver enable multicast on *vlan*

在VLAN *vlan*上调用驱动使能组播成功

Port *port* is down or not belong the vlan *vlan*

端口*port* down或不属于VLAN *vlan*

Delete all host response timers on port *port*

删除端口*port*上的所有查询响应定时器

表1-4 debugging igmp-snooping fsm命令输出信息描述表

字段

描述

(*source*, *group*) state changes from *state1* to *state2* on *vlan*

VLAN *vlan*上表项（*source*，*group*）的状态由*state1*迁移到*state2*

(*source*, *group*) state changes to *state* on *vlan*

VLAN *vlan*上表项（*source*，*group*）的状态迁移到*state*

Notified add/delete host port *port* of (*source*, *group*) to main on *vlan*

VLAN *vlan*上通知主板添加/删除（*source*，*group*）的成员端口*port*

Notified add/delete host slot *slot* of (*source*, *group*) to other on *vlan*

VLAN *vlan*上通知其它板添加/删除（*source*，*group*）的成员板*slot*

Notified add/delete host slot *slot* of (*source*, *group*) to main on *vlan*

VLAN *vlan*上通知主板添加/删除（*source*，*group*）的成员板*slot*

Notified add/delete router port *port* to main on *vlan*

VLAN *vlan*上通知主板添加/删除路由器端口*port*

Notified add/delete router slot *slot* to other on *vlan*

VLAN *vlan*上通知其它板添加/删除路由器板*slot*

Notified add/delete router slot *slot* to main on *vlan*

VLAN *vlan*上通知主板添加/删除路由器板*slot*

Notified add/delete global router port *port* to other on *vlan*

VLAN *vlan*上通知其它板添加/删除全局路由器端口*slot*

Notified add/delete global host port *port* of (*source*, *group*) to other on *vlan*

VLAN *vlan*上通知其它板添加/删除（*source*，*group*）的全局成员端口*port*

Notified delete entry (*source*, *group*) to other on *vlan*

VLAN *vlan*上通知其它板删除表项（*source*，*group*）

Global host attribute is set to (*source*, *group*)on *vlan*

对VLAN *vlan*表项（*source*，*group*）设置全局成员特征

Global host attribute is cleared from (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）删除全局成员特征

Global host port *port* is successfully added to (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）添加全局成员端口

Global host port *port* is successfully deleted from (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）删除全局成员端口

Global router port *port* is successfully added on *vlan*

对VLAN *vlan*表项（*source*，*group*）添加全局路由器端口

Global router port *port* is successfully deleted from *vlan*

对VLAN *vlan*表项（*source*，*group*）删除全局路由器端口

Host slot attribute is set to (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）设置成员板特征

Host slot attribute is cleared from (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）删除成员板特征

Host slot *slot* is successfully added to (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）添加成员板*slot*

Host slot *slot* is successfully deleted from (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）删除成员板*slot*

Local host attribute is set to (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）添加本地成员特征

Local host attribute is cleared from (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）删除本地成员特征

Local host port *port* is successfully added to (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）添加本地成员端口

Local host port *port* is successfully deleted from (*source*, *group*) on *vlan*

对VLAN *vlan*表项（*source*，*group*）删除本地成员端口

Local router port *port* is successfully added on *vlan*

对VLAN *vlan*表项（*source*，*group*）添加本地路由器端口

Local router port *port* is successfully deleted from *vlan*

对VLAN *vlan*表项（*source*，*group*）删除本地路由器端口

表1-5 debugging igmp-snooping group命令输出信息描述表

字段

描述

Add v*n* host port *port*

在端口*port*上添加版本*n*的成员端口

Create Dynamic group (*source*, *group*) on *vlan*, add host port *port*

VLAN *vlan*上创建动态组（*source*，*group*），并添加成员端口*port*

Succeed in sending special group query packet for group *group* on host port *port* on *vlan*

对VLAN *vlan*上端口*port*特定组*group*成功发送特定源组查询报文

Router port *port* times out on *vlan*, delete router port

VLAN *vlan*上路由器端口*port*超时，删除路由器端口

Delete host port *port* for dynamic group (*source*, *group*) on *vlan*

删除VLAN *vlan*上对动态组（*source*，*group*）路由器端口*port*

Delete dynamic group (*source*, *group*) on *vlan*

删除VLAN *vlan*上的动态组（*source*，*group*）

Update v*n* host port *port* for dynamic group: (*source*, *group*) on *vlan*

VLAN *vlan*上更新动态组（*source*，*group*）的版本*n*成员端口*port*

The v1/v2 host is present, ignore the IGMPv3 BLOCK report packet

版本1/版本2的主机存在，不处理收到的版本3的BLOCK报文

Delete the port *port* from all dynamic group

将成员端口*port*从所有动态组表项中删除

Delete all host port that on the slot *slot* and delete the slot *slot* from host slot bitmap

将属于板*slot*的所有成员端口删除，若该板是成员板，删除该板

Clear all dynamic group on *vlan*

清除VLAN *vlan*内所有动态组表项

Send group specific query packet for group *group* on host port *port* on *vlan*

VLAN *vlan*上成员端口*port*的组*group*发送特定组查询报文

Create static group (*source*, *group*) on *vlan*, add host port *port*

VLAN *vlan*上创建静态组（*source*，*group*），并添加成员端口*port*

The host port *port* does not exist in static group (*source*, *group*) on *vlan*, add it

VLAN *vlan*上的静态组（*source*，*group*）不存在成员端口*port*，添加成员端口

Delete host port *port* for static group (*source*, *group*)**on *vlan*

删除VLAN *vlan*上对静态组（*source*，*group*）路由器端口*port*

Delete static group (*source*, *group*) on *vlan*

删除VLAN *vlan*上的静态组（*source*，*group*）

The port *port* is not router port, add it

端口*port*不是路由器端口，添加

Delete the port *port* from router port list

从路由器端口列表中删除路由器端口*port*

Delete the port *port* from all static group

将成员端口*port*从所有静态组表项中删除

Clear all Static group on *vlan*

清除VLAN内所有静态组表项

表1-6 debugging igmp-snooping packet命令输出信息描述表

字段

描述

Succeed in forwarding IGMP packet to port *port* on *vlan*

成功发送IGMP报文到VLAN *vlan*上的端口*port*

Succeed in broadcasting the packet on *vlan*

在VLAN *vlan*内成功广播报文

Succeed in delivering up packet to IP

将报文上送IP层成功

Receive IGMPv*n* version general query packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取版本*n*的IGMP通用查询报文

Receive IGMP group specific query packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取版本*n*的IGMP特定组查询报文

Receive IGMPv3 group specific query packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取IGMPv3特定组查询报文

Receive IGMPv*n* report packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取版本*n*的IGMP报告报文

Receive IGMP leave packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取IGMP离开报文

Receive PIMv1 or DVMRP packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取PIMv1或DVMRP报文

The version of IGMP packet that receive from port *port* on *vlan* is higher than the version on *vlan*

从VLAN *vlan*上获取的报文版本高于VLAN *vlan*版本

The PIM packet which receive from port *port* on *vlan* is not hello report or is fragment

从VLAN *vlan*的端口*port*上获取的PIM报文不是Hello报文或PIM分片报文

Receive PIMv2 Hello packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取到PIMv2 Hello报文

Receive CBT packet from port *port* on *vlan*

从VLAN *vlan*的端口*port*上获取到CBT报文

Deal with the IGMP/PIMv2/CBT packet which receive from port *port* on *vlan*

处理从VLAN *vlan*的端口*port*上获取到的IGMP/PIMv2/CBT报文

Forward the group and source specific query packet on port which receive from port *port* on *vlan*, (*source*, *group*)

转发从VLAN *vlan*的端口*port*表项（*source*，*group*）上获取到的特定源组查询报文

Main slot broadcast the general query packet which receive from port *port* on *vlan*

主板广播从VLAN *vlan*的端口*port*上获取到通用查询报文

Forward the group specific query packet on port which receive from port *port* on *vlan*, the group address is *group*

转发从VLAN *vlan*的端口*port*上获取的组地址为*group*的特定组查询报文

Forward the IGMP report packet on router port which destination IP address is *group* and source IP address is *source* that receive from port *port* on *vlan*

从路由器端口上转发从VLAN *vlan*的端口*port*上获取的（*source*，*group*）的IGMP报告报文

Broadcast PIMv1 or DVMRP packet which receive from port *port* on *vlan*

广播从VLAN *vlan*的端口*port*上获取的PIMv1或DVMRP报文

Send PIMv1 or DVMRP packet to IP

将PIMv1/DVMRP报文上送IP层成功

The version of IGMP packet is lower than version on *vlan*, the main slot broadcast it on *vlan*

报文版本低于端口版本，主板在VLAN *vlan*内广播

The IGMP packet which receive from port *port* on *vlan* on Main slot, forward it locally

从主板VLAN *vlan*的端口*port*上获取报文，本地转发

The IGMP packet version which receive from IGMP is higher than the version on *vlan*, broadcast it on *vlan*

报文版本高于端口版本，VLAN *vlan*内广播

Receive Query packet from *vlan*, it needn\'t to maintain router port, only main slot deal with it

从VLAN *vlan*上获取查询报文，无需维护路由器端口，只有主板处理

The IGMP packet which receive from IGMP on *vlan* on main slot, forward it locally

从主板VLAN *vlan*上获取的报文，本地转发

Forward the IGMP packet locally

本地转发IGMP报文

Send the IGMP packet up to IP

上送报文至IP层

Receive Query packet from main slot

从主板收到查询报文

Host send IGMPv3(*mode*) packet to *port* with *group* and 0 source(s) on *vlan*.

VLAN *vlan*内的模拟主机向端口*port*发送模式为*mode*的IGMPv3报告报文

表1-7 debugging igmp-snooping sync命令输出信息描述表

字段

描述

Received a configuration message

接收到配置信息

Received a message to add/delete/cancel host slot

添加/删除/取消成员板

Received a message to add/delete host ports

添加/删除成员接口

Received a message to add/delete router slot

添加/删除路由板

Received a message to add/delete router ports

添加/删除路由接口

Received a message to delete entry

删除表项

Receive message from master

接口板收到主板发的消息

Main slot forward the IGMP packet to other IO slot

主板发送IGMP报文至接口板

The IGMP packet which receive from port *port* on *vlan* on IO slot, send it to the main slot

发送来自于VLAN *vlan*上端口*port*的接口板上的消息至主板

Send the IGMP packet to IO slots

发送IGMP报文至接口板

Receive IGMP packet from another slot

从其它板收到IGMP报文

Synchronize vlan or vsi IGMP snooping disable message to other slots

同步VLAN的IGMP Snooping去使能信息到其它板

Successfully set version on *vlan* and synchronize to other slots

设置VLAN *vlan*的版本并同步到其它板

Successfully set drop-unknown on *vlan* and synchronize to other slots

设置VLAN *vlan*的未知报文丢弃并同步到其它板

Successfully set host-aging-time on *vlan* and synchronize to other slots

设置VLAN *vlan*的成员端口定时器并同步到其它板

Successfully set router-aging-time on *vlan* and synchronize to other slots

设置VLAN *vlan*的路由端口定时器并同步到其它板

Successfully set *n* on *vlan* and synchronize to other slots

设置VLAN *vlan*的特定组查询时间间隔*n*并同步到其它板

Successfully set max-response-time on *vlan* and synchronize to other slots

设置VLAN *vlan*的最大响应时间并同步到其它板

Successfully recover global IGMP snooping disabled and synchronize message to other slots

设置全局IGMP去使能并同步到其它板

Successfully recover default entry limit globally

恢复全局表项数目限制

Successfully recover default drop-unknown globally and synchronize message to other slots

恢复默认的全局未知组播丢弃并同步到其它板

Successfully recover default host-aging-time globally and synchronize message to other slots

恢复默认的全局成员端口定时器并同步到其它板

Successfully recover default router-aging-time globally and synchronize message to other slots

恢复默认的全局路由端口定时器并同步到其它板

Successfully recover default *n* globally and synchronize message to other slots

恢复默认的全局查询时间*n*并同步到其它板

Successfully recover default max-response-time globally and synchronize message to other slots

恢复默认的全局最大查询时间并同步到其它板

Successfully recover default fast-leave globally and synchronize message to other slots

恢复默认的全局快速离开并同步到其它板

Successfully recover default group-policy globally and synchronize message to other slots

恢复默认的全局组过滤并同步到其它板

Successfully recover default overflow-replace globally and synchronize message to other slots

恢复默认的全局组替换并同步到其它板

Successfully recover IGMP snooping disable on *vlan* and send message to other slots synchronize configuration

恢复VLAN *vlan*上去使能并同步到其它板

Successfully recover IGMP snooping drop-unknown disable on *vlan* and send message to other slots synchronize configuration

恢复VLAN *vlan*上未知组播丢弃并同步到其它板

Successfully recover IGMP snooping Version on *vlan* and send message to other slots synchronize configuration

恢复VLAN *vlan*上版本并同步到其它板

Successfully recover IGMP snooping router-aging-time on *vlan* and send message to other slots synchronize configuration

恢复VLAN *vlan*上路由端口定时器并同步到其它板

Successfully recover IGMP snooping max-response-time on *vlan* and send message to other slots synchronize configuration

恢复VLAN *vlan*上最大响应时间并同步到其它板

Successfully set *n* on *vlan* and synchronize to other slots

恢复VLAN *vlan*上特定组查询时间间隔*n*并同步到其它板

Successfully process Port fast-leave message and sync to other slots

恢复端口快速离开并同步到其它板

Successfully process Port group-policy message and sync to other slots

恢复端口组过滤并同步到其它板

Successfully process Port group-limit message and sync to other slots

恢复端口组数目限制并同步到其它板

Successfully process Port overflow-replace message and sync to other slots

恢复端口组替换并同步到其它板

Synchronize enable or disable IGMP snooping globally message to other slots

同步IGMP的使能或去使能到其它板

Successfully process global entry limit message and sync to other slots

处理全局表项数目并同步到其它板

Synchronize drop-unknown globally message to other slots

处理全局未知报文丢弃并同步到其它板

Successfully process global host-aging-time message and sync to other slots

处理全局成员端口定时器并同步到其它板

Successfully process global router-aging-time message and sync to other slots

处理全局路由器端口定时器并同步到其它板

Successfully set *n* and synchronize to other slots

处理全局查询时间间隔*n*并同步到其它板

Successfully process global max-response-time message and sync to other slots

处理全局最大响应时间并同步到其它板

Successfully process global fast-leave message and sync to other slots

处理全局快速离开并同步到其它板

Successfully process global group-policy message and sync to other slots

处理全局组过滤并同步到其它板

Successfully process global overflow-replace message and sync to other slots

处理全局组替换并同步到其它板

synchronize configure debug message to other slots

同步配置debug信息到其它板

Successfully process Port fast-leave message and sync to other slots

处理端口快速离开并同步到其它板

Successfully process Port group-limit message and sync to other slots

处理全局组数目并同步到其它板

Successfully process Port group-policy message and sync to other slots

处理全局组过滤并同步到其它板

Successfully process Port overflow-replace message and sync to other slots

处理全局快速离开并同步到其它板

Successfully process static host port message and sync to other slots

处理静态成员端口的状态配置信息并同步到其它板

Successfully process static router port message and sync to other slots

处理静态路由器端口的状态配置信息并同步到其它板

Synchronize configure resetting statistics message to other slots

同步清空统计信息配置并同步到其它板

Synchronize configure resetting groups message to other slots

同步清空组信息配置并同步到其它板

表1-8 debugging igmp-snooping timer命令输出信息描述表

字段

描述

Succeed in creating router port timer, *n* seconds for port *port* on *vlan*

为VLAN *vlan*上端口*port*创建路由器端口定时器，时间为*n*秒

Succeed in resizing router port timer, *n* seconds, for port *port* on *vlan*

为VLAN *vlan*上端口*port*调整路由器端口定时器，时间为*n*秒

Create host port timer, *n* seconds, for port:*port,* dynamic group: (*source*, *group*) on *vlan*

为VLAN *vlan*上端口*port*动态组（*source*，*group*）创建成员端口定时器，时间为*n*秒

Resize host port timer, *n* seconds, for port:*port*, dynamic group: (*source*, *group*) on *vlan*

为VLAN *vlan*上端口*port*动态组（*source*，*group*）调整成员端口定时器，时间为*n*秒

Succeed in creating v*n*host port timer, *m* seconds, for port *port*

为端口*port*创建版本为*n*的成员端口定时器，时间为*m*秒

Succeed in resizing v*n* host port timer, *m* seconds, for port *port*

为端口*port*调整版本为*n*的成员端口定时器，时间为*m*秒

Down host port timer, *n* seconds, for port *port*

对端口*port*关掉成员端口定时器，时间为*n*秒

Update v*n* host port timer

更新版本*n*的成员端口定时器

The host port *port* times out for dynamic group (*source*, *group*) on *vlan*

VLAN *vlan*上对动态组（*source*，*group*）的端口*port*超时

Successfully create query information record timer

成功创建查询信息记录定时器

Successfully resize query information record timer

成功调整查询信息记录定时器

Created resend timer, *n* ms

创建重传定时器，时间为*n*毫秒

Create timer to IP fail list, *n* seconds

对IP下驱动失败创建定时器，时间为*n*秒

Create timer to MAC fail list, *n* seconds.

对MAC下驱动失败创建定时器，时间为*n*秒

Successfully create IGMPv1 query present timer on *vlan*, *n* seconds.

在VLAN *vlan*内将IGMPv1查询存在定时器创建为*n*秒

Successfully resize IGMPv1 query present timer on *vlan*, *n* seconds.

在VLAN *vlan*内将IGMPv1查询存在定时器调整为*n*秒

The IGMPv1 query present times out on *vlan*.

VLAN *vlan*内的IGMPv1查询存在定时器超时

Successfully create host response timer, 10 seconds on group *group* of port *port* in *vlan*.

在VLAN *vlan*内的端口*port*上为组*group*将查询响应定时器创建为10秒

Successfully update host response timer, 10 seconds on group *group* of port *port* in *vlan*.

在VLAN *vlan*内的端口*port*上为组*group*将查询响应定时器更新为10秒

Host response times out on group *group* of port *port* in *vlan*.

VLAN *vlan*内的端口*port*上组*group*的查询响应定时器超时

【举例】

\# 在设备上使能IGMP Snooping，打开IGMP Snooping接口驱动调试信息开关。

\<Sysname\> debugging igmp-snooping entry

\*Sep 15 11:43:28:565 2011 Sysname MCS/7/ENTRY: -MDC=1; Delete MAC entry 0100-5e01-0101 from driver. (G156098)

*// 在VLAN 2内从驱动中删除二层MAC表项*

\# 在设备上使能IGMP Snooping，打开IGMP Snooping事件调试信息开关。

\<Sysname\> debugging igmp-snooping event

\*Sep 15 11:46:06:924 2011 Sysname MCS/7/EVENT: -MDC=1; Successfully enable IGMP snooping on VLAN 4. (G174304)

*// 在VLAN 4上使能IGMP Snooping*

\# 在设备上使能IGMP Snooping，打开IGMP Snooping组播组调试信息开关。

\<Sysname\> debugging igmp-snooping group

\*Sep 15 11:47:41:455 2011 Sysname MCS/7/GROUP: -MDC=1; Create Dynamic group (0.0.0.0, 225.1.1.1) on VLAN 2, add host port GE1/0/1. (G091840)

*// 在VLAN 2内创建动态表项（0.0.0.0，225.1.1.1），添加主机端口GigabitEthernet1/0/1*

\# 在设备上使能IGMP Snooping，打开IGMP Snooping报文调试信息开关。

\<Sysname\> debugging igmp-snooping packet

\*Sep 15 11:47:41:455 2011 Sysname MCS/7/PACKET: -MDC=1; Receive IGMPv2 report packet from port GE1/0/1 on VLAN 2. (G162625)

*// 在VLAN 2内的端口GigabitEthernet1/0/1上收到IGMPv2成员关系报告报文*

\*Sep 15 13:35:00:846 2011 Sysname MCS/7/PACKET: -MDC=1; Forward the IGMP membership packet on router port which destination IP address is 224.0.0.1 and source IP address is 0.0.0.0 that receive from port GE1/0/1 on VLAN 2. (G163447)

*// 通过VLAN 2内的端口GigabitEthernet1/0/1发送源地址为0.0.0.0、目的地址为224.0.0.1的IGMP报文*

\# 在设备上使能IGMP Snooping，打开IGMP Snooping板间同步调试信息开关。

\<Sysname\> debugging igmp-snooping sync

\*Sep 15 13:40:04:692 2011 Sysname MCS/7/SYNC: -MDC=1; synchronize configure debug message to other board. (G1710245)

*// 通知其它板打开调试信息*

\# 在设备上使能IGMP Snooping，打开IGMP Snooping定时器调试信息开关。

\<Sysname\> debugging igmp-snooping timer

\*Sep 15 13:42:03:448 2011 Sysname MCS/7/TIMER: -MDC=1; Successfully create query information record timer. (G092699)

\*Sep 15 13:42:03:449 2011 Sysname MCS/7/TIMER: -MDC=1; Succeed in creating router port timer, 105 seconds, for port GE1/0/1 on VLAN 1. (G091031)

*// 创建路由器端口，并将其老化时间设置为105秒*

\*Sep 15 13:35:00:845 2011 Sysname MCS/7/TIMER: -MDC=1; Down host port timer, 2 seconds, for port GE1/0/1. (G091336)

*// 收到离开报文，并将端口老化时间设置为2秒*

\# 在设备上使能IGMP Snooping，打开IGMP Snooping状态机调试信息开关。

\<Sysname\> debugging igmp -snooping fsm

\*Sep 15 13:42:10:403 2011 Sysname MCS/7/FSM: -MDC=1; Notified add host self slot 0 of (0.0.0.0,239.255.255.250) to other on VLAN 2. (G061062)

*// 在VLAN 2上通知其它板添加成员板*

**IGMP Snooping \-- IGMP Snooping调试命令 \-- debugging l2mf**

------------------------------------------------------------------------

【命令】

**[debugging l2mf **[{ **all** \| **error** \| **event** \| **group** \| **msg** }]]

**[undo debugging l2mf **[{ **all** \| **error** \| **event** \| **group** \| **msg** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示L2MF（Layer-2 Multicast Forwarding，二层组播转发）所有调试信息开关。

**[error**]：表示L2MF错误调试信息开关。

**[event**]：表示L2MF事件调试信息开关。

**[group**]：表示L2MF组播组调试信息开关。

**[msg**]：表示L2MF消息调试信息开关。

【描述】

**[debugging l2mf**]命令用来打开L2MF调试信息开关。**undo debugging l2mf**命令用来关闭L2MF调试信息开关。

缺省情况下，L2MF调试信息开关处于关闭状态。

表1-9 debugging l2mf error命令输出信息描述表

字段

描述

Failed flush set router port message (*source, group*) to driver in VLAN *vlan*

在VLAN *vlan*中下刷路由器端口信息（*source*，*group*）到驱动失败

The port extend information is invalid when add port

在添加端口时端口的扩展信息无效

(*source, group*) has been existent in VLAN *vlan*

在VLAN *vlan*中（*source*，*group*）已存在

Can\'t find (*source, group*) in VLAN *vlan*

在VLAN *vlan*中未能找到（*source*，*group*）

MAC entry *mac* has been existent in VLAN *vlan*

在VLAN *vlan*中MAC表项*mac*已存在

MAC entry *mac* can\'t be found in VLAN *vlan*

在VLAN *vlan*中未能找到MAC表项*mac*

Failed to parse received message

解析收到的消息失败

表1-10 debugging l2mf event命令输出信息描述表

字段

描述

Port is exisit when add port for entry (0.0.0.0, 0.0.0.0) in VLAN *vlan*

在VLAN *vlan*中为表项（0.0.0.0，0.0.0.0）添加端口时，该端口已存在

Add port for entry (0.0.0.0, 0.0.0.0) inVLAN *vlan*

在VLAN *vlan*中为表项（0.0.0.0，0.0.0.0）添加端口

Delete port for entry (0.0.0.0, 0.0.0.0) in VLAN *vlan*

在VLAN *vlan*中为表项（0.0.0.0，0.0.0.0）删除端口

Add slot *slot* for entry (0.0.0.0, 0.0.0.0) in VLAN*vlan*

在VLAN *vlan*中为表项（0.0.0.0，0.0.0.0）添加板*slot*

表1-11 debugging l2mf group命令输出信息描述表

字段

描述

The *number* ports are added/deleted to the entry (*source, group*) of interface *interface*, and it return *value*

在表项（*source*，*group*）的接口*interface*中添加/删除了*number*个端口，并返回值*value*

Add entry (*source, group*) in VLAN*vlan*

在VLAN *vlan*中添加表项（*source*，*group*）

Add MAC entry *mac* in VLAN *vlan*

在VLAN *vlan*中添加MAC表项*mac*

Delete entry (*source, group*) in VLAN*vlan*

在VLAN *vlan*中删除表项（*source*，*group*）

Add slot for (*source, group*) in VLAN*vlan*

在VLAN *vlan*中为表项（*source*，*group*）添加板

Add port for MAC entry *mac* in VLAN*vlan*

在VLAN *vlan*中为MAC表项*mac*添加端口

表1-12 debugging l2mf msg命令输出信息描述表

字段

描述

Flush set router port message (*source*, *group*) to driver in VLAN*vlan* with port

在VLAN *vlan*中拷贝路由器端口信息（*source*，*group*）并下刷驱动

Flush add entry message (*source*, *group*) to driver in VLAN*vlan*

在VLAN *vlan*中将表项（*source*，*group*）的信息下刷驱动

Flush add entry Mac message (*mac*) to driver in VLAN*vlan*

在VLAN *vlan*中将MAC表项*mac*的信息下刷驱动

Flush L2 multicast configuration message to driver with command

将二层组播配置信息下刷驱动

Save message to Kernel

保存信息到内核

Cache message to fail list

写队列失败

Process add entry message for entry (*source*, *group*)

处理添加IP表项（*source*，*group*）的消息

Process add entry message for MAC entry *mac*

处理添加MAC表项*mac*的消息

Send finish packet message to MCS

完成向MCS进程打包发送消息

Send L3 multicast enable message to MCS in VLAN*vlan*

在VLAN *vlan*中向MCS进程发送三层组播使能的消息

【举例】

\# 打开L2MF事件调试信息开关。

\<Sysname\> debugging l2mf event

\*Jun  4 12:55:19:912 2012 Sysname L2MF/7/EVENT: -MDC=1; Delete port for entry (0.0.0.0, 0.0.0.0) in VLAN 2. (A171255)

*// 在VLAN 2中为表项（0.0.0.0，0.0.0.0）删除端口*

\# 打开L2MF组播组调试信息开关。

\<Sysname\> debugging l2mf group

\*Jun  4 12:50:41:191 2012 Sysname L2MF/7/GROUP: -MDC=1; Add MAC entry 0100-5e01-0101 in VLAN 1. (A151783)

*// 在VLAN 1中添加MAC表项0100-5E01-0101*

\*Jun  4 12:50:41:191 2012 Sysname L2MF/7/GROUP: -MDC=1; Add entry (0.0.0.0, 225.1.1.1) in VLAN 1. (A151071)

*// 在VLAN 1中添加表项（0.0.0.0，225.1.1.1）*

\# 打开L2MF消息调试信息开关。

\<Sysname\> debugging l2mf msg

\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Flush add entry Mac message (0100-5e01-0101) to driver in VLAN 1. (A141939)

*// 在VLAN 1中将MAC表项0100-5E01-0101的信息下刷驱动*

\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Save message to Kernel. (A131801)

*// 保存信息到内核*

\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Process add entry message for MAC entry 0100-5e01-0101  (A18873)

*// 处理添加MAC表项0100-5E01-0101的消息*

\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Flush add entry message (0.0.0.0, 225.1.1.1) to driver in VLAN 1. (A141815)

*// 在VLAN 1中将表项（0.0.0.0，225.1.1.1）的信息下刷驱动*

\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Process add entry message for entry (0.0.0.0, 225.1.1.1). (A18815)

*// 处理添加IP表项（0.0.0.0，225.1.1.1）的消息*
