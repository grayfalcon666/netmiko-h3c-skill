<!-- CMD-INDEX
  debugging ipv6 pim                  | 用户视图             | L5
-->

**IPv6 PIM \-- IPv6 PIM调试命令 \-- debugging ipv6 pim**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 pim** [ **vpn-instance** *vpn-instance-name*  { **all** \| **df** \| **error** \| { **event** \| **register** \| **routing-table** }  *advanced-acl6-number*  \| { **assert** \| **join-prune** \| **rp** \| **state-refresh** }  *advanced-acl6-number*  [ **receive** \| **send** ] \| **neighbor**  *basic-acl6-number*  [ **receive** \| **send** ] }]]

**[undo debugging ipv6 pim** [ **vpn-instance** *vpn-instance-name*  { **all** \| **df** \| **error** \| **event** \| **register** \| **routing-table** \| { **assert** \| **join-prune** \| **neighbor** \| **rp** \| **state-refresh** } [ **receive** \| **send** ] }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

**[all**]：表示IPv6 PIM所有调试信息开关。

**[df**]：表示IPv6双向PIM DF选举调试信息开关。

**[error**]：表示IPv6 PIM错误调试信息开关。

**[event**]：表示IPv6 PIM事件调试信息开关。

**[register**]：表示IPv6 PIM注册报文调试信息开关。

**[routing-table**]：表示IPv6 PIM组播路由表状态改变调试信息开关。

*[advanced-acl6-number*]：表示IPv6高级ACL的编号，取值范围为3000～3999。

**[assert**]：表示IPv6 PIM断言报文调试信息开关。

**[join-prune**]：表示IPv6 PIM加入/剪枝报文调试信息开关。

**[rp**]：表示IPv6 PIM与RP相关报文的调试信息开关。

**[state-refresh**]：表示IPv6 PIM状态刷新报文调试信息开关。

**[receive**]：表示接收的IPv6 PIM报文调试信息开关。

**[send**]：表示发送的IPv6 PIM报文调试信息开关。

**[neighbor**]：表示IPv6 PIM与邻居信息相关的调试信息开关。

*[basic-acl6-number*]：表示IPv6基本ACL的编号，取值范围为2000～2999。

【描述】

**[debugging ipv6 pim**]命令用来打开IPv6 PIM调试信息开关。**undo debugging ipv6 pim**命令用来关闭IPv6 PIM调试信息开关。

缺省情况下，IPv6 PIM调试信息开关处于关闭状态。

表1-1 debugging ipv6 pim assert命令输出信息描述表

字段

描述

Assert FSM

断言状态机

*[state1*-\>*state2*]

断言状态机从*state1*转换到*state2*

loser/winner/noinfo

断言状态机处于Loser/Winner/Noinfo状态

timeout of the winner

Winner老化

Rbit

RPT标识位

Preference

优先级字段

Metric

Metric字段

assert timer expired

断言定时器超时

insufficient memory

内存不足

inferior assert

度量值比自身差的断言报文

acceptable assert

来自断言获胜路由器的度量值比自身好的断言报文

preferred assert

比当前断言获胜路由器具备更优开销的断言报文

NIIF

入接口为空

OIF

出接口

(\*,G) Entry is not exist

（\*，G）表项不存在

self metric

自身到源的路由度量值

unknown neighbor

未知邻居

wrong packet length

报文长度非法

bad group address

错误的组地址

invalid group address

非法的组地址

group boundary

组边界

bad source address

错误的源地址

invalid source address

非法的源地址

SSM group

SSM组

表1-2 debugging ipv6 pim df命令输出信息描述表

字段

描述

DF election/DF-Election

DF选举

DFT

DF选举定时器

WinTimer

Winner定时器

expire time

定时器的超时时间

MC

Offer或Winner报文的发送个数

robustness

DF选举健壮系数，缺省值为3

RPL

RPL链路

Offer

DF选举的初始状态

Lose

DF选举失败

Win

DF选举胜出

Backoff

处于Win状态的DF收到更优的Offer报文

DF FSM

DF选举状态

Receive better Backoff/Pass/Offer/Win

收到更优的Backoff/Pass/Offer/Win报文

Receive worse Backoff/Pass/Offer/Win

收到更差的Backoff/Pass/Offer/Win报文

Receive Backoff/Pass for us

收到通告自己的Backoff/Pass报文

表1-3 debugging ipv6 pim error命令输出信息描述表

字段

描述

IPC data

用于进程间通信的数据

Mfib

组播转发信息库

Reference

引用计数

config info

配置信息

insufficient memory

内存不足

secondary address node

二级地址节点

unsupported PIM packet type

不支持的PIM数据包类型

checksum error

检验和字段错误

invalid pim interface

非法的PIM接口

unknown neighbor

未知邻居

CRPT

C-RP发送定时器

Blank Group

不存在C-RP的组

Fail to get ifindex

获取接口索引失败

best route

最优路由

Assert_Timer

断言定时器

invalid event

非法事件

MRIB

组播路由信息库

valid RPF interface

合法的RPF邻居

Ifstate

接口状态

negotiation

协商

wrong flag

错误标识

表1-4 debugging ipv6 pim event命令输出信息描述表

字段

描述

PIM mrt

PIM组播路由表

No-Cache msg

未知组播消息

Wrong-If msg

从非入接口收到组播流消息

SPT msg

SPT切换消息

Active msg

MFIB上报新的组播流消息

Inactive msg

MFIB上报流老化消息

Reg-Timeout msg

注册定时器超时消息

reset forwarding-table msg

MIFB转发表重置消息

Received BFD event: *type*, *source* -\> *destination*, *interface*

收到BFD会话消息：类型为*type*，源地址为*source*，目的地址为*destination*，接口为*interface*

表1-5 debugging ipv6 pim join-prune命令输出信息描述表

字段

描述

JP

加入/剪枝报文

Upstream

报文中的上游邻居信息

Groups

报文中的组数目信息

Holdtime

加入/剪枝报文的保持时间字段

Group: *addr*/*mask* \-\-- *m* joins *n* prunes

报文中的组信息：组地址/掩码长度------*m*个加入*n*个剪枝

Join: *addr/mask* flag

加入：源地址/掩码，标志位

RP change

RP发生变化

the packet is received from interface *A*, but destination is *B*. Ignored.

从接口A上收到一个发给B的报文，将其丢弃

Message Truncated

报文长度非法

multicast boundary

组播边界

Join/Prune received from non-local neighbor

从不属于本接口网段的上游邻居收到一个加入/剪枝报文

*[Address *is not a valid multicast address]

*[Address*]是一个非法组播地址

Message from unknown neighbor

从未知邻居收到报文

表1-6 debugging ipv6 pim neighbor命令输出信息描述表

字段

描述

hello packet

PIM Hello报文

invalid secondary address

非法二级地址

Holdtime

PIM Hello报文的保持时间字段

Tbit

T位选项

Lan delay

剪枝延迟时间选项

Override interval

剪枝否决时间选项

DR priority

DR优先级选项

Genid

Generation ID选项

Discarding Hello packet from *address* without Generation ID.

丢弃没有Generation ID的Hello报文

the neighbor information being refreshed

更新邻居信息

Too many neighbors, ignoring new neighbor *address*.

邻居过多，忽略新的Hello报文

secondary address list

二级地址列表

bad secondary address

错误的二级地址

Received Hello packet from invalid source: *address*

收到来自非法源地址的Hello报文

Received Hello packet on *interface* from non-local source: *address*

收到非本地主机的Hello报文

Received Hello packet with short data from *address*

收到数据不完整的Hello报文

Received Hello packet from *address* with wrong Holdtime length:

收到Holdtime选项长度非法的Hello报文

Received Hello packet from *address* with invalid LAN Prune Delay length:

收到LAN Prune Delay选项长度非法的Hello报文

Received Hello packet from *address* with invalid DR Priority length:

收到DR优先级选项长度非法的Hello报文

Received Hello packet from *address* with invalid Generation ID length:

收到Generation ID选项长度非法的Hello报文

Received Hello packet from *address* with invalid State Refresh length:

收到状态更新选项长度非法的Hello报文

Received Hello packet from *address* with Bidir option

收到带有双向PIM选项的Hello报文

Received Hello packet from *address* with unsupported option:

收到带有错误选项的Hello报文

Received Hello packet from *address* with wrong data length

收到长度错误的Hello报文

Notify create/delete/disable BFD session *source* -\> *destination*, *interface*

通知创建/删除/关闭BFD会话，源地址为*source*，目的地址为*destination*，接口为*interface*

表1-7 debugging ipv6 pim register命令输出信息描述表

字段

描述

probe

探测报文

no route to RP

没有通往RP的路由

not knowing RP

未知RP

register packet

注册报文

Bbit

边界位

Nbit

空位

RST

注册停止定时器

register state

注册状态机状态

reg tunnel

注册通道

reg-stop packet

注册停止报文

invalid RPF interface

非法的RPF接口

RP changed

RP发生变化

Null-Register

空注册报文

register oif

注册出接口

the group address *address* is not valid.

组地址非法

Received register-stop message with bad group masks from *address* for *address/mask*.

收到组掩码错误的注册终止报文

the source address is not valid

源地址非法

RP for group *address* is unknown.

相关组的RP未知

RP dispute for *address*

RP映射错误

no matching entry for *(S,G)*

没有相关的（*S**，G*）表项

Anycast-RP timer

Anycast-RP定时器

the source address belongs to the Anycast-RP set

源地址在Anycast-RP集中

Notify MFIB not to suppress register packets

通知MFIB不要抑制注册报文

no active local RP exists

没有激活的本地RP存在

表1-8 debugging ipv6 pim rp命令输出信息描述表

字段

描述

auto-RP announce packet

自动RP宣告报文

Truncated bootstrap message

长度非法的自举报文

BSM packet

BSR自举报文

Nbit

BSR报文段禁止转发标志位

Fragment tag

用于BSR报文的分片

Hash mask len

哈希掩码长度

BSR Priority

BSR优先级

BSR address

BSR地址

Group

组地址

Zbit

BSR报文段自治域标志位

RP Count

BSR报文中表示服务这个组播组范围的RP个数

Frag RP Count

表示BSR分片报文中服务这个组播组范围的RP个数

RP: *address* \-\-- Holdtime *holdtime*, Priority *priority*

RP：地址为*address*------保持时间为*holdtime*，优先级为*priority*

Truncated crp packet

长度非法的C-RP宣告报文

C-RP-Adv

C-RP宣告报文

Prefix count

C-RP宣告报文中包含的组地址个数

Priority

C-RP宣告报文的优先级字段

Holdtime

C-RP宣告报文的保持时间字段

RP address

RP地址

Failed to build BSM pkt because MTU is too small

构造BSR自举报文失败，原因是MTU太小了

BSR boundary

BSR边界

multicast boundary

组播边界

EBSR

最优BSR

EBSR updates RPs by self in scope

最优BSR在域内自动更新了RP

Protocol conflict while updating group *address* for crp *address*.

更新C-RP地址时使用组地址，与协议冲突

Invalid group address

非法组地址

multicast boundary

组播边界

Received an invalid length C-RP-Adv packet

收到一个长度非法的C-RP的宣告报文

The length of C-RP-Adv packet is wrong

C-RP宣告报文长度出错

Received BSR packet with bad bsr address

收到BSR地址非法的BSR报文

Received BSR packet with non-unicast bsr address *address*

收到BSR地址不是单播地址的BSR报文

Received a BSM with bad first group address from BSR *address*

收到的BSR自举报文中第一个组地址错误

Unable to pass multicast boundary check for *address/mask*

由于组地址和掩码问题无法通过组播边界检查

no route to BSR *address*

没有通往BSR的路由信息

BSM from BSR *address* comes from wrong interface *interface*

收到来自错误接口的BSR报文

Source address *address1* is not next hop to BSR %A (next hop is*address2*)

源地址不是通往BSR的下一跳地址

Received a BSR packet from other PIM-SM domain from *address* on *interface*

收到来自其他PIM-SM域的BSR报文

Received a BSR packet from *address* with too short length

收到长度过短的BSR报文

Received BSR packet with bad hash mask length

收到哈希掩码长度错误的BSR报文

Received a BSR packet from unknown neighbor *address*

收到来自未知邻居的BSR报文

Scope

BSR域

Group: *address*/*mask* \-\-- RP Count: *m*, Frag RP Count: *n*

BSR自举报文中的组*address*/*length*对应的Frag字段的数目为*n*，C-RP的数目为*m*

RP count *m* differs from previous *n*,  or  accumulative frag count *k* is wrong

RP数量与之前不同，或者累计分片数量错误

表1-9 debugging ipv6 pim routing-table命令输出信息描述表

字段

描述

RPF Interface

RPF接口

multicast boundary

组播边界

Claim the route

组播表项声明使用某条单播路由

Unclaim the route

组播表项声明放弃使用某条单播路由

Wrong IIF

错误的入接口

Assert state machine

断言状态机

reg oif

注册出接口

ET

下游超时定时器

Downstream FSM

下游接口状态机

PPT

下游剪枝否决定时器

Upstream FSM

上游接口状态机

NotJoined

PIM-SM的（S，G，RPT）、（S，G）或（\*，G）上游状态机处于未加入状态

Joined

PIM-SM的（S，G）或（\*，G）上游状态机处于加入状态

Join

PIM-SM下游状态机处于加入状态

Prune-Pending

下游状态机处于剪枝未决状态

RPF\'(\*,G)

（\*，G）表项的上游邻居

RPF\'(S,G)

（S，G）表项的上游邻居

Join suppressed

从入接口收到给上游邻居的加入，抑制自己的加入

genid changed

Generation ID变化

override interval

剪枝否决时间

NoInfo

下游状态机处于Noinfo状态

NotPruned

PIM-SM的（S，G，RPT）上游状态机处于非剪枝状态

Pruned

PIM-SM的（S，G，RPT）上游状态机处于剪枝状态

override timer

剪枝覆盖定时器

PruneTmp

PIM-SM的（S，G，RPT）下游状态机处于Prune Tmp状态

PrunePendingTmp

PIM-SM的（S，G，RPT）下游状态机处于Prune Pending Tmp状态

RP changed, no RP is available for*(\*,G)* now

RP变化，没有当前（\*，G）表项可用的RP

RP changed, update the upstream state of *(\*,G)*

RP变化，更新（\*，G）表项的上游状态

SPT switch

SPT切换

表1-10 debugging ipv6 pim state-refresh命令输出信息描述表

字段

描述

SRM

状态刷新报文

Drop SRM for (S, G) because of rate limit

由于对状态刷新报文的接收进行限速，因此丢弃此期间收到的状态刷新报文

Drop SRM for (S, G) because of invalid hoplimit(0) or interval(0)

丢弃Hop Limit值为0或发送间隔为0的状态刷新报文

Originator address

产生状态刷新报文的地址

preference

报文的优先级字段

metric

报文的Metric字段

mask length

报文的掩码长度字段

hoplimit

报文的Hop Limit值

prune indicator

Prune Indicator标志位

prune now

Prune Now标志位

assert override

Assert Override标志位

Interval

状态刷新报文的发送间隔

【举例】

\# 接口上使能IPv6 PIM-SM，并打开公网实例IPv6 PIM断言报文的调试信息开关。

\<Sysname\> debugging ipv6 pim assert

%Sep  7 16:40:52:195 2011 Sysname PIM6/7/ASSERT: -MDC=1; IPv6: Received assert packet for (8:12::2, FFE3::101), FE80:8:12::2 -\> FF02::D on GigabitEthernet1/0/1, Rbit: 0, Preference: 100, Metric: 100. (SM141628)

*// 从接口GigabitEthernet1/0/1收到一个针对表项（8:12::2, FFE3::101）的断言报文，报文源地址为FE80:8:12::2，目的地址为FF02::D，RPT标志为0，优先级为100，花销为100*

\# 接口上使能IPv6 PIM-SM，并打开公网实例IPv6双向PIM DF选举的调试信息开关。

\<Sysname\> debugging ipv6 pim df

\*Dec 27 13:04:50:371 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Start DF election on interface GigabitEthernet1/0/1 of RP 1:1::1 (BD012845)

\*Dec 27 13:04:50:371 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Create DFT for RP: 1:1::1 on interface GigabitEthernet1/0/1, expire time is 1530 msec (BD012050)

\*Dec 27 13:04:50:371 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Set MC to 0 for RP (1:1::1) on interface GigabitEthernet1/0/1 (BD01523)

\*Dec 27 13:04:50:908 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Send bidir-pim offer packet for RP (1:1::1) on interface GigabitEthernet1/0/1. (BD01200)

\*Dec 27 13:04:51:907 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: DF FSM Offer-\>Offer for RP (1:1::1) on interface GigabitEthernet1/0/1, while DFT expires and MC is lessthan robustness (BD011974)

\*Dec 27 13:04:51:908 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Set MC to 1 for RP (1:1::1) on interface GigabitEthernet1/0/1 (BD01523)

\*Dec 27 13:04:51:908 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Create DFT for RP: 1:1::1 on interface GigabitEthernet1/0/1, expire time is 60 msec (BD012050)

*// 双向PIM的RP为1:1::1，在接口GigabitEthernet1/0/1上触发DF选举。启动DF选举定时器并设置Offer报文的发送个数为0，该定时器超时后发送Offer报文，并设置Offer报文的发送个数为1*

\*Dec 27 13:04:52:048 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Send bidir-pim offer packet for RP (1:1::1) on interface GigabitEthernet1/0/1. (BD01200)

\*Dec 27 13:04:52:117 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: DF FSM Offer-\>Win for RP (1:1::1) on interface GigabitEthernet1/0/1, while DFT expires and MC is equal to robustness and we have path to RPA (BD011974)

\*Dec 27 13:04:52:117 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Set DF to FE80:8:13::1 (pref: 0, metric: 0) for RP (1:1::1) on interface GigabitEthernet1/0/1 (BD01394)

\*Dec 27 13:04:52:118 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Send bidir-pim winner packet for RP (1:1::1) on interface GigabitEthernet1/0/1. (BD01200)

\*Dec 27 13:04:52:118 2012 Sysname PIM6/7/DF: -MDC=1; IPv6: Create WinTimer for RP:1:1::1 on interface GigabitEthernet1/0/1, expire time is 5000 msec (BD012275)

*// 定时器再次超时后发送Offer报文，Offer报文的发送个数等于健壮系数，接口的DF状态由Offer切换为Win。将DF设置为本接口的IPv6地址FE80:8:13::1，发送Winner报文并设置Winner定时器为5000毫秒*

\# 接口上使能IPv6 PIM-SM，并打开公网实例IPv6 PIM错误调试信息开关。

\<Sysname\> debugging ipv6 pim error

%Sep  7 16:40:01:700 2011 Sysname PIM6/7/ERROR: -MDC=1; IPv6: Dropping received pkt from FE80:8:12::2 to FF02::D with type 5, for checksum error (PM08321)

*// 从FE80:8:12::2收到一个IPv6 PIM报文，因为校验和错误，将其忽略*

\# 接口上使能IPv6 PIM-SM，并打开公网实例IPv6 PIM事件调试信息开关。

\<Sysname\> debugging ipv6 pim event

%Sep  7 16:36:06:845 2011 Sysname PIM6/7/EVENT: -MDC=1; IPv6: Recv Rt refresh msg with prefix: 8:12::/64, Nexthop: ::, OutIf: GigabitEthernet1/0/1, Pref: 0, Metric: 0, ProtoID: 1, Flags: 0x10800 (PR03338)

*// 收到前缀为8:12::/64、下一跳为::、出接口为GigabitEthernet1/0/1的路由刷新消息，该路由优先级为0，花销为0，协议号为1，标志0x10800*

\# 接口上使能IPv6 PIM-SM，并打开公网实例IPv6 PIM加入/剪枝报文的调试信息开关。

\<Sysname\> debugging ipv6 pim join-prune

Sep  7 16:38:24:393 2011 Sysname PIM6/7/JP: -MDC=1; IPv6: PIM ver 2 JP received FE80:8:12::4 -\> FF02::D on interface GigabitEthernet1/0/1 (SM141190)

*// 从接口GigabitEthernet1/0/1收到PIMv2的加入/剪枝报文，报文源地址为FE80:8:12::4，目的地址为FF02::D*

%Sep  7 16:38:24:395 2011 Sysname PIM6/7/JP: -MDC=1; IPv6:  Upstream: FE80:8:12::1, Number of groups: 1, Holdtime: 1800 (SM141192)

*// 上游邻居为8:12::1，组数目为1，保持时间为1800秒*

%Sep  7 16:38:24:395 2011 Sysname PIM6/7/JP: -MDC=1; IPv6:  Group: FFE3::101 \-\-- 1 joins 0 prunes (SM141198)

*[// IPv6*]*组播组FFE3::101的信息为：1个加入，0个剪枝*

%Sep  7 16:38:24:395 2011 Sysname PIM6/7/JP: -MDC=1; IPv6:   Join: 8:12::1 \-\-- Flags: SWR (SM141202)

*// 加入8:12::1，标志为SWR*

\# 接口上使能IPv6 PIM-SM，并打开公网实例接收IPv6 PIM Hello报文的调试信息开关。

\<Sysname\> debugging ipv6 pim neighbor receive

\* %Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Received Hello packet from neighbor FE80:7:12::1, incoming interface is Vlan-interface11. (PM073562)

*// 从接口Vlan-interface11上收到源地址为FE80:7:12::1的PIMv2的Hello报文*

%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Holdtime: 105 (PM073298)

%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Tbit: 0, Lan delay: 500, Override interval: 2500 (PM073340)

%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: DR priority: 1 (PM073365)

%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Genid: 0xDF424DC2 (PM073391)

%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Secondary address: 7:12::1 (PM073235)

*// 保持时间为105秒，T位没有设置，剪枝延迟时间为500毫秒，剪枝否决时间为2500毫秒，DR优先级为1，Generation ID为0xDF424DC2，二级地址7:12::1*

%Sep  7 16:59:05:820 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Received hello packet from neighbor FE80:7:12::1 and refreshed it. (PM072623)

*// 从邻居FE80:7:12::1收到Hello报文，并刷新*

\# 接口上使能IPv6 PIM-SM，并打开公网实例发送IPv6 PIM Hello报文的调试信息开关。

\<Sysname\> debugging ipv6 pim neighbor send

%Sep  7 16:59:13:914 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: PIM ver 2 Hello sending FE80:8:12::1 -\> FF02::D on GigabitEthernet1/0/1 (PM071570)

*// 从接口GigabitEthernet1/0/1上发送PIMv2的Hello报文，源地址为FE80:8:12::1，目的地址为FF02::D*

%Sep  7 16:59:13:917 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Holdtime: 105 s (PM071572)

%Sep  7 16:59:13:921 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Tbit: 0, Lan delay: 500 ms, Override interval: 2500 ms (PM071576)

%Sep  7 16:59:13:924 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: DR priority: 1 (PM071578)

%Sep  7 16:59:13:926 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Genid: 0xCEA8757C (PM071580)

%Sep  7 16:59:13:928 2011 Sysname PIM6/7/NBR: -MDC=1; IPv6: Secondary Address: 8:12::1 (PM071303)

*// 保持时间为105秒，T位没有设置，剪枝延迟时间为500毫秒，剪枝否决时间为2500毫秒，DR优先级为1，Generation ID为0xCEA8757C，二级地址为8:12::1*

\# 接口上使能IPv6 PIM-SM，并打开公网实例IPv6 PIM注册报文的调试信息开关。

\<Sysname\> debugging ipv6 pim register

%Sep  7 17:34:08:801 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: (7:11::8, FF1E::1) register state transited from NoInfo to Join due to CouldRegister(S,G) == True. Add reg tunnel. (SM06507)

*// 表项（7:11::8，FF1E::1）注册状态机从NoInfo跃迁到Join，添加注册口*

%Sep  7 17:34:08:804 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: Add register oif for (7:11::8, FF1E::1) (SM061560)

*// 为表项（7:11::8，FF1E::1）添加注册出接口*

%Sep  7 17:34:08:838 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: (7:11::8, FF1E::1) register state transited from Join to Prune due to received RegStop. Remove reg tunnel, set RST to 48s. (SM06690)

*// 收到注册停止报文，表项（7:11::8，FF1E::1）状态从Jolin跃迁到Prune，删除注册口，设置注册停止定时器为48秒*

%Sep  7 17:34:08:840 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: RST(48s) create successfully for (7:11::8, FF1E::1). (SM06384)

*// 成功为表项（7:11::8，FF1E::1）创建注册停住定时器为48秒*

%Sep  7 17:34:08:840 2011 Sysname PIM6/7/REG: -MDC=1; IPv6: Delete register oif for (7:11::8, FF1E::1) (SM061655)

*// 为表项（7:11::8，FF1E::1）删除注册出接口*

\*May  3 07:22:49:773 2013 Sysname PIM6/7/REG: -MDC=1; IPv6: Register packets of (7:11::123, FF1E::1) not forwarded because no active local RP exists. (SM06406)

*// 由于没有激活的本地Anycast-RP存在，不为（7:11::123，FF1E::1）转发注册报文*

\*May  3 07:22:49:773 2013 Sysname PIM6/7/REG: -MDC=1; IPv6: Register packets of (7:11::123, FF1E::1) not forwarded because the source address belongs to the Anycast-RP set. (SM061936)

*// 由于源地址在Anycast-RP集中，不为（7:11::123，FF1E::1）转发注册报文*

\# 接口上使能IPv6 PIM-SM，并打开公网实例接收IPv6 PIM与RP相关报文的调试信息开关。

\<Sysname\> debugging ipv6 pim rp receive

%Sep  7 17:09:12:835 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Received a msg (C-BSR enable). (RP08321)

*// 收到C-BSR使能的消息*

%Sep  7 17:09:12:835 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Scope \'Global\' receive an event of \'Router changes to C-BSR\' at state \'Accept Any\'. (RP042440)

%Sep  7 17:09:12:835 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Set BST of scope Global to 5. (RP041233)

*// 全局域收到在AA状态路由变成C-BSR事件，设置全局域的BST为5秒*

\# 接口上使能IPv6 PIM-SM，并打开公网实例发送IPv6 PIM与RP相关报文的调试信息开关。

\<Sysname\> debugging ipv6 pim rp send

%%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Send out BSM packet to interface Vlan-interface11. (PM09430)

*// 向接口Vlan-interface11发送BSM报文*

%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6:  Nbit: 0, Fragment tag: 0x6732, Hash mask len: 126, BSR Priority: 64, BSR address: 8:12::1. (PM09430)

*// 报文B标志位为0，分片标志0x6732，哈希长度126，优先级64，BSR地址8:12::1*

%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6:  Group: FF00::/8, Bbit: 0, Zbit: 0, RP Count: 1, Frag RP Count: 1 (PM09436)

%Sep  7 17:10:18:051 2011 Sysname PIM6/7/RP: -MDC=1; IPv6:   RP: 8:12::2 \-\-- Holdtime 180, Priority 192 (PM09440)

%Sep  7 17:10:18:052 2011 Sysname PIM6/7/RP: -MDC=1; IPv6: Set BST of scope Global to 60. (RP041233)

*// 组范围FF00::/8，B标志位为0，Z标志位为0，RP数量为1，分片中RP数为1，组下RP地址为8:12::2,保持时间180S，优先级192，设置全局域的BST为60秒*

\# 接口上使能IPv6 PIM-SM，并打开公网实例IPv6 PIM组播路由表状态改变调试信息开关。

\<Sysname\> debugging ipv6 pim routing-table

%Sep  7 17:23:53:839 2011 Sysname PIM6/7/ROUTE: -MDC=1; IPv6: Creating (7:11::8, FF1E::1), flags: 0x00000000, down if protocol: 0 (SM134265)

*// 创建表项（7:11::8，FF1E::1），标志为x00000000，下游接口协议号为0*

%Sep  7 17:23:53:839 2011 Sysname PIM6/7/ROUTE: -MDC=1; IPv6: Claim the IIF route for (7:11::8, FF1E::1) (SM151621)

*// 为表项（7:11::8，FF1E::1）声明路由*

%Sep  7 17:23:53:839 2011 Sysname PIM6/7/ROUTE: -MDC=1; IPv6: Add iif: Vlan-interface11 for (7:11::8, FF1E::1) (SM131961)

*// 为表项（7:11::8，FF1E::1）添加出接口Vlan-interface11*

\# 在接口上使能IPv6 PIM-DM，并打开公网实例接收IPv6 PIM状态刷新报文的调试信息开关。

\<Sysname\> debugging ipv6 pim state-refresh receive

\*Mar 16 08:36:12:644 2012 Sysname PIM6/7/SRM: -MDC=1; IPv6: PIM ver 2 SRM receiving FE80:8:12::1 -\> FF02::D for (7:11::100, FF0E::1) on GigabitEthernet1/0/1, Originator address: FE80:7:11::1, preference: 0, metric: 0, mask length: 64, hoplimit: 255, prune indicator: unset, prune now: unset, assert override: set, interval: 60s (DM141415)

*// 在接口GigabitEthernet1/0/1收到状态刷新报文，报文的源地址是FE80:8:12::1，目的地址是FF02::D；组播组为FF0E::1/128；组播源为7:11::100；产生状态刷新报文设备的地址为FE80:7:11::1；优先级和Metric值都是0；掩码长度为64；Hop Limit为255，没有设置Prune Indicator和Prune Now标志位，设置了Assert Override标志位；发送间隔为60秒*

\# 在接口上使能IPv6 PIM-DM，并打开公网实例发送IPv6 PIM状态刷新报文的调试信息开关。

\<Sysname\> debugging ipv6 pim state-refresh send

\*Mar 16 08:36:12:645 2012 Sysname PIM6/7/SRM: -MDC=1; IPv6: PIM ver 2 SRM sending FE80:8:24::2 -\> FF02::D for (7:11::100, FF0E::1) on GigabitEthernet1/0/1, Originator address: FE80:7:11::1, preference: 10, metric: 2, mask length: 64, hoplimit: 254, prune indicator: unset, prune now: unset, assert override: set, interval: 60s. (DM09330)

*// 在接口GigabitEthernet1/0/1发送状态刷新报文，报文的源地址是FE80:8:24::2，目的地址是FF02::D；组播组为FF0E::1/128；组播源为7:11::100；产生状态刷新报文设备的地址为FE80:7:11::1；优先级为10；Metric值为2；掩码长度都是64；Hop Limit为254，没有设置Prune Indicator和Prune Now标志位，设置了Assert Override标志位；发送间隔为60秒*
