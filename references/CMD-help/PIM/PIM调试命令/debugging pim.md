
**PIM \-- PIM调试命令 \-- debugging pim**

------------------------------------------------------------------------

【命令】

**[debugging pim** [ **vpn-instance** *vpn-instance-name*  { **all** \| **df** \| **error** \| { **event** \| **register** \| **routing-table** }  *advanced-acl-number*  \| { **assert** \| **join-prune** \| **rp** \| **state-refresh** }  *advanced-acl-number*  [ **receive** \| **send** ] \| **neighbor**  *basic-acl-number*  [ **receive** \| **send** ] }]]

**[undo debugging pim** [ **vpn-instance** *vpn-instance-name*  { **all** \| **df** \| **error** \| **event** \| **register** \| **routing-table** \| { **assert** \| **join-prune** \| **neighbor** \| **rp** \| **state-refresh** } [ **receive** \| **send** ] }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

**[all**]：表示PIM所有调试信息开关。

**[df**]：表示双向PIM DF选举调试信息开关。

**[error**]：表示PIM错误调试信息开关。

**[event**]：表示PIM事件调试信息开关。

**[register**]：表示PIM注册报文调试信息开关。

**[routing-table**]：表示PIM组播路由表状态改变调试信息开关。

*[advanced-acl-number*]：表示IPv4高级ACL的编号，取值范围为3000～3999。

**[assert**]：表示PIM断言报文调试信息开关。

**[join-prune**]：表示PIM加入/剪枝报文调试信息开关。

**[rp**]：表示PIM与RP相关报文的调试信息开关。

**[state-refresh**]：表示PIM状态刷新报文调试信息开关。

**[receive**]：表示接收的PIM报文调试信息开关。

**[send**]：表示发送的PIM报文调试信息开关。

**[neighbor**]：表示PIM与邻居信息相关的调试信息开关。

*[basic-acl-number*]：表示IPv4基本ACL的编号，取值范围为2000～2999。

【描述】

**[debugging pim**]命令用来打开PIM调试信息开关。**undo debugging pim**命令用来关闭PIM调试信息开关。

缺省情况下，PIM调试信息开关处于关闭状态。

表1-1 debugging pim assert命令输出信息描述表

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

表1-2 debugging pim df命令输出信息描述表

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

表1-3 debugging pim error命令输出信息描述表

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

表1-4 debugging pim event命令输出信息描述表

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

表1-5 debugging pim join-prune命令输出信息描述表

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

表1-6 debugging pim neighbor命令输出信息描述表

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

表1-7 debugging pim register命令输出信息描述表

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

表1-8 debugging pim rp命令输出信息描述表

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

表1-9 debugging pim routing-table命令输出信息描述表

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

表1-10 debugging pim state-refresh命令输出信息描述表

字段

描述

SRM

状态刷新报文

Drop SRM for (S, G) because of rate limit

由于对状态刷新报文的接收进行限速，因此丢弃此期间收到的状态刷新报文

Drop SRM for (S, G) because of invalid ttl(0) or interval(0)

丢弃TTL值为0或发送间隔为0的状态刷新报文

Originator address

产生状态刷新报文的地址

preference

报文的优先级字段

metric

报文的Metric字段

mask length

报文的掩码长度字段

ttl

报文的TTL值

prune indicator

Prune Indicator标志位

prune now

Prune Now标志位

assert override

Assert Override标志位

Interval

状态刷新报文的发送间隔

【举例】

\# 接口上使能PIM-SM，并打开公网实例接收PIM断言报文的调试信息开关。

\<Sysname\> debugging pim assert received

\*Dec 10 13:53:28:147 2010 Sysname PIM/7/ASSERT: -MDC=1; Received assert packet for (2.1.1.1, 225.0.0.25), 5.1.1.10 -\> 224.0.0.13 on GigabitEthernet1/0/1, Rbit: 0, Preference: 10, Metric: 2. (SM141564)

*// 从接口GigabitEthernet1/0/1收到一个针对表项（2.1.1.1，225.0.0.25）的断言报文，报文源地址为5.1.1.10，目的地址为224.0.0.13，RPT标志为0，优先级为10，度量值为2*

\*Dec 10 13:53:28:190 2010 Sysname PIM/7/ASSERT: -MDC=1; Assert (2.1.1.1, 225.0.0.25) GigabitEthernet1/0/1 FSM Loser-\>Loser, acceptable assert received from current Winner. (SM041341)

*// 接口GigabitEthernet1/0/1上的表项（2.1.1.1，225.0.0.25）的断言状态机保持Loser状态，此时从当前的Winner收到一个可接受的断言报文*

\# 接口上使能PIM-SM，并打开公网实例发送PIM断言报文的调试信息开关。

\<Sysname\> debugging pim assert send

\*Dec 10 13:54:04:921 2010 Sysname PIM/7/ASSERT: -MDC=1; PIM ver 2 assert packet sending 5.1.1.10 -\> 224.0.0.13 for (2.1.1.1, 225.0.0.25) through interface GigabitEthernet1/0/1, Rbit: 0, Preference: 10, Metric: 2. (SM04155)

*// 从接口GigabitEthernet1/0/1发送一个针对表项（2.1.1.1，225.0.0.25）的断言报文，报文源地址为5.1.1.10，目的地址为224.0.0.13，RPT标志为0，优先级为10，度量值为2*

\# 接口上使能PIM-SM，并打开公网实例双向PIM DF选举的调试信息开关。

\<Sysname\> debugging pim df

\*Dec 27 12:02:01:846 2012 Sysname PIM/7/DF: -MDC=1; Start DF election on interface GigabitEthernet1/0/1 of RP 1.1.0.1 (BD012845)

\*Dec 27 12:02:01:846 2012 Sysname PIM/7/DF: -MDC=1; Create DFT for RP: 1.1.0.1 on interface GigabitEthernet1/0/1, expire time is 1880 msec (BD012050)

\*Dec 27 12:02:01:846 2012 Sysname PIM/7/DF: -MDC=1; Set MC to 0 for RP (1.1.0.1) on interface GigabitEthernet1/0/1 (BD01523)

\*Dec 27 12:02:02:803 2012 Sysname PIM/7/DF: -MDC=1; Send bidir-pim offer packet for RP (1.1.0.1) on interface GigabitEthernet1/0/1. (BD01200)

\*Dec 27 12:02:02:803 2012 Sysname PIM/7/DF: -MDC=1; DF FSM Offer-\>Offer for RP (1.1.0.1) on interface GigabitEthernet1/0/1, while DFT expires and MC is less than robustness (BD011974)

\*Dec 27 12:02:02:803 2012 Sysname PIM/7/DF: -MDC=1; Set MC to 1 for RP (1.1.0.1) on interface GigabitEthernet1/0/1 (BD01523)

*// 双向PIM的RP为1.1.0.1，在接口GigabitEthernet1/0/1上触发DF选举。启动DF选举定时器并设置Offer报文的发送个数为0，该定时器超时后发送Offer报文，并设置Offer报文的发送个数为1*

\*Dec 27 12:02:03:882 2012 Sysname PIM/7/DF: -MDC=1; Send bidir-pim offer packet for RP (1.1.0.1) on interface GigabitEthernet1/0/1. (BD01200)

\*Dec 27 12:02:03:952 2012 Sysname PIM/7/DF: -MDC=1; DF FSM Offer-\>Win for RP (1.1.0.1) on interface GigabitEthernet1/0/1, while DFT expires and MC is equal to robustness and we have path to RPA (BD011974)

\*Dec 27 12:02:03:952 2012 Sysname PIM/7/DF: -MDC=1; Set DF to 8.13.0.1 (pref: 0, metric: 0) for RP (1.1.0.1) on interface GigabitEthernet1/0/1 (BD01394)

\*Dec 27 12:02:03:952 2012 Sysname PIM/7/DF: -MDC=1; Send bidir-pim winner packet for RP (1.1.0.1) on interface GigabitEthernet1/0/1. (BD01200)

\*Dec 27 12:02:03:953 2012 Sysname PIM/7/DF: -MDC=1; Create WinTimer for RP: 1.1.0.1 on interface GigabitEthernet1/0/1, expire time is 5000 msec (BD012275)

*// 定时器再次超时后发送Offer报文，Offer报文的发送个数等于健壮系数，接口的DF状态由Offer切换为Win。将DF设置为本接口的IP地址8.13.0.1，发送Winner报文并设置Winner定时器为5000毫秒*

\# 接口上使能PIM-SM，并打开公网实例PIM错误调试信息开关。

\<Sysname\> debugging pim error

\*Dec 10 13:57:31:714 2010 Sysname PIM/7/ERROR: -MDC=1; Received a PIM packet from unknown neighbor 6.1.1.3. Ignored. (PM08341)

*// 从未知邻居6.1.1.3收到一个PIM报文，将其忽略*

\# 接口上使能PIM-SM，并打开公网实例PIM事件调试信息开关。

\<Sysname\> debugging pim event

\*Dec 14 18:24:27:191 2010 Sysname PIM/7/EVENT: -MDC=1; Receive No-Cache msg for (1.0.0.7,/225.0.0.25) with IIF GigabitEthernet1/0/1. (SM161073)

*// 收到一个未知组播流消息，组播流源地址为1.0.0.7，目的地址为225.0.0.25，入接口为GigabitEthernet1/0/1*

\# 接口上使能PIM-SM，并打开公网实例接收PIM加入/剪枝报文的调试信息开关。

\<Sysname\> debugging pim join-prune received

\*Dec 10 10:43:05:326 2010 Sysname PIM/7/JP: -MDC=1; PIM ver 2 JP received 6.1.1.5 -\> 224.0.0.13 on interface GigabitEthernet1/0/1 (SM141126)

\*Dec 10 10:43:05:331 2010 Sysname PIM/7/JP: -MDC=1;  Upstream: 6.0.0.10, Number of groups: 1, Holdtime: 210 (SM141128)

\*Dec 10 10:43:05:339 2010 Sysname PIM/7/JP: -MDC=1;  Group: 225.0.0.25 \-\-- 1 joins 0 prunes (SM141134)

\*Dec 10 10:43:05:349 2010 Sysname PIM/7/JP: -MDC=1;   Join: 3.0.0.5 \-\-- Flags: S (SM141138)

*// 从接口GigabitEthernet1/0/1收到PIMv2的加入/剪枝报文，报文源地址为6.1.1.5，目的地址为224.0.0.13，上游邻居为6.0.0.10，组数目为1，保持时间为210秒，组播组225.0.0.25的信息为：1个加入，0个剪枝；加入3.0.0.5，S标志位为1*

\# 接口上使能PIM-SM，并打开公网实例发送PIM加入/剪枝报文的调试信息开关。

\<Sysname\> debugging pim join-prune send

\*Dec 10 10:43:06:415 2010 Sysname PIM/7/JP: -MDC=1; Send a JP packet to interface GigabitEthernet1/0/1. (PM09198)

\*Dec 10 10:43:06:416 2010 Sysname PIM/7/JP: -MDC=1;  Upstream: 5.0.0.10, Groups: 1, Holdtime: 210 (PM09200)

\*Dec 10 10:43:06:416 2010 Sysname PIM/7/JP: -MDC=1;  Group: 225.0.0.25 \-\-- 1 joins 0 prunes (PM09206)

\*Dec 10 10:43:06:417 2010 Sysname PIM/7/JP: -MDC=1;   Join: 3.0.0.5 \-\-- Flags: S (PM09210) 

*// 向接口GigabitEthernet1/0/1发送加入/剪枝报文，上游邻居为5.0.0.10，组数目为1，保持时间为210秒，组播组225.0.0.25的信息为：1个加入，0个剪枝；加入3.0.0.5，S标志位为1*

\# 接口上使能PIM-SM，并打开公网实例接收PIM Hello报文的调试信息开关。

\<Sysname\> debugging pim neighbor receive

\*Dec 10 10:31:45:76 2010 Sysname PIM/7/NBR: -MDC=1; Received Hello packet from neighbor 3.0.0.5, incoming interface is GigabitEthernet1/0/1. (PM073099)

\*Dec 10 10:31:45:89 2010 Sysname PIM/7/NBR: -MDC=1; Holdtime: 105 (PM073147)

\*Dec 10 10:31:45:98 2010 Sysname PIM/7/NBR: -MDC=1; Tbit: 0, Lan delay: 500, Override interval: 2500 (PM073184)

\*Dec 10 10:31:45:101 2010 Sysname PIM/7/NBR: -MDC=1; DR priority: 1 (PM073207)

\*Dec 10 10:31:45:119 2010 Sysname PIM/7/NBR: -MDC=1; Genid: 0xB3DC0254 (PM073231)

*// 从接口GigabitEthernet1/0/1上收到源地址为3.0.0.5的PIMv2的Hello报文，保持时间为105秒，T位没有设置，剪枝延迟时间为500毫秒，剪枝否决时间为2500毫秒，DR优先级为1，Generation ID为0xB3DC0254*

\# 接口上使能PIM-SM，并打开公网实例发送PIM Hello报文的调试信息开关。

\<Sysname\> debugging pim neighbor send

\*Dec 10 10:31:31:241 2010 Sysname PIM/7/NBR: -MDC=1; PIM ver 2 Hello sending 3.0.0.10 -\> 224.0.0.13 on GigabitEthernet1/0/1 (PM071410)

\*Dec 10 10:31:31:244 2010 Sysname PIM/7/NBR: -MDC=1; Holdtime: 105 s (PM071412)

\*Dec 10 10:31:31:247 2010 Sysname PIM/7/NBR: -MDC=1; Tbit: 0, Lan delay: 500 ms, Override interval: 2500 ms (PM071416)

\*Dec 10 10:31:31:249 2010 Sysname PIM/7/NBR: -MDC=1; DR priority: 1 (PM071418)

\*Dec 10 10:31:31:251 2010 Sysname PIM/7/NBR: -MDC=1; Genid: 0x7EF237CB (PM071420)

*// 从接口GigabitEthernet1/0/1上发送PIMv2的Hello报文，源地址为3.0.0.10，目的地址为224.0.0.13，保持时间为105秒，T位没有设置，剪枝延迟时间为500毫秒，剪枝否决时间为2500毫秒，DR优先级为1，Generation ID为07EF237CB*

\# 接口上使能PIM-SM，并打开公网实例PIM注册报文的调试信息开关。

\<Sysname\> debugging pim register

\*Dec 10 10:51:15:332 2010 Sysname PIM/7/REG: -MDC=1; (1.0.0.5, 225.0.0.25) register state transited from NoInfo to Join due to CouldRegister(S,G) == True. Add reg tunnel. (SM06512)

\*Dec 10 10:51:15:340 2010 Sysname PIM/7/REG: -MDC=1; Add register oiffor (1.0.0.5, 225.0.0.25) (SM061336)

*// 表项（1.0.0.5，225.0.0.25）的注册状态机由NoInfo状态变为加入状态。添加注册通道，并为该表项添加注册出接口*

\*Dec 10 10:51:25:382 2010 Sysname PIM/7/REG: -MDC=1; PIM ver 2 Reg-Stop received 5.0.0.10 -\> 1.0.0.10 for (1.0.0.5, 225.0.0.25) (SM061767)

\*Dec 10 10:51:25:391 2010 Sysname PIM/7/REG: -MDC=1; Received register-stop message for (1.0.0.5, 225.0.0.25). (SM061834)

\*Dec 10 10:51:25:399 2010 Sysname PIM/7/REG: -MDC=1; (1.0.0.5, 225.0.0.25) register state transited from Join to Prune due to received RegStop. Remove reg tunnel, set RST to 61s. (SM06695)

\*Dec 10 10:51:25:404 2010 Sysname PIM/7/REG: -MDC=1; RST(61s) create successfully for (1.0.0.5, 225.0.0.25). (SM06388)

\*Dec 10 10:51:25:425 2010 Sysname PIM/7/REG: -MDC=1; Delete register oif for (1.0.0.5, 225.0.0.25) (SM061428)

*// 从接口收到PIMv2的表项（1.0.0.5，225.0.0.25）的注册终止报文，源地址为5.0.0.10，目的地址为1.0.0.10。该表项的注册状态机由加入状态变为剪枝状态，删除注册通道。设置注册停止定时器时间为61秒，注册停止定时器被成功地创建。删除该表项的注册出接口*

\*May  3 07:09:25:137 2013 Sysname PIM/7/REG: -MDC=1; Register packets of (7.11.0.123, 225.1.1.1) not forwarded because no active local RP exists. (SM06406)

*// 由于没有激活的本地Anycast-RP存在，不为（7.11.0.123，225.1.1.1）转发注册报文*

\*May  3 07:09:25:137 2013 Sysname PIM/7/REG: -MDC=1; Register packets of (7.11.0.123, 225.1.1.1) not forwarded because the source address belongs to the Anycast-RP set. (SM061936)

*// 由于源地址在Anycast-RP集中，不为（7.11.0.123，225.1.1.1）转发注册报文*

\# 接口上使能PIM-SM，并打开公网实例接收PIM与RP相关报文的调试信息开关。

\<Sysname\> debugging pim rp receive

\*Dec 10 10:55:41:438 2010 Sysname PIM/7/RP: -MDC=1; Received a C-RP-Adv Packet from self, prefix count 1, priority 192, holdtime 150, RP address 5.0.0.10. (RP03676)

\*Dec 10 10:55:41:438 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4, Bbit: 0, Zbit: 0 (RP03681)

*[// RP*]*收到一个自已发送的RP宣告报文，前缀数目为1，优先级为192，保持时间为150秒，RP地址为5.0.0.10。组播组224.0.0.0/4的信息为：B位没有设置，Z位没有设置*

\*Dec 10 10:54:55:54 2010 Sysname PIM/7/RP: -MDC=1; Received BSM packet on GigabitEthernet1/0/1 from 3.0.0.10. Scope Global, Nbit: 0, Fragment tag: 0x5e67, Hash mask len: 30, BSR Priority: 64, BSR address: 4.0.0.10. (RP04760)

*// 在接口GigabitEthernet1/0/1收到一个BSR自举报文，源地址为3.0.0.10，属全局域，N位没有设置，分片信息为0x5e67，哈希掩码长度为30，BSR优先级为64，BSR地址为4.0.0.10*

\*Dec 10 10:54:55:55 2010 Sysname PIM/7/RP: -MDC=1; Scope \'Global\' receive an event of \'Receive Preferred BSM\' at state \'Accept Preferred\'. (RP042346)

*// 全局域内在Accept Preferred状态下收到一个更优BSR的自举报文*

\*Dec 10 10:54:55:56 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4 \-\-- RPCount: 1, Frag RP Count: 1 (RP05535)

\*Dec 10 10:54:55:56 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (RP05539)

*// 组播组224.0.0.0/4的信息为：C-RP个数为1，分片信息为1。RP地址为5.0.0.10，保持时间为180秒，优先级为192*

\# 接口上使能PIM-SM，并打开公网实例发送PIM与RP相关报文的调试信息开关。

\<Sysname\> debugging pim rp send

\*Dec 10 10:54:55:56 2010 Sysname PIM/7/RP: -MDC=1; Send out BSM packet to interface GigabitEthernet1/0/1. (PM09364)

\*Dec 10 10:54:55:57 2010 Sysname PIM/7/RP: -MDC=1;  Nbit: 0, Fragment tag: 0x5e67, Hash mask len: 30, BSR Priority: 64, BSR address: 4.0.0.10. (PM09368)

*// 向接口GigabitEthernet1/0/1发送BSR自举报文。N位没有设置，分片信息为0x5E67，哈希掩码长度为30，BSR优先级为64，BSR地址为4.0.0.10*

\*Dec 10 10:54:55:57 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4, Bbit:0, Zbit: 0, RP Count: 1, Frag RP Count: 1 (PM09378)

\*Dec 10 10:54:55:57 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (PM09382)

\*Dec 10 10:54:55:105 2010 Sysname PIM/7/RP: -MDC=1; Set BST of scope Global to 130. (RP041140)

*// 组播组224.0.0.0/4的信息为：B位没有设置，Z位没有设置，C-RP个数为1，分片信息为1。C-RP地址为5.0.0.10，保持时间为180秒，优先级为192。设置全局域自举定时器为130秒*

\*Dec 10 10:55:57:439 2010 Sysname PIM/7/RP: -MDC=1; Send BSM packet to all neighbor in scope Global. (RP011260)

*// 自举路由器向全局域内的所有邻居发送自举报文*

\*Dec 10 10:55:57:443 2010 Sysname PIM/7/RP: -MDC=1; EBSR updates RPs by self in scope Global. (RP01984)

\*Dec 10 10:55:57:443 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4 \-\-- RP Count: 1, Frag RP Count: 1 (RP05535)

\*Dec 10 10:55:57:444 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (RP05539)

*// 被选中的自举路由器在全局域内更新RP，组播组224.0.0.0/4的信息为：C-RP个数为1，分片信息为1。C-RP地址为5.0.0.10，保持时间为180秒，优先级为192*

\*Dec 10 10:55:57:448 2010 Sysname PIM/7/RP: -MDC=1; Send out BSM packet to interface GigabitEthernet1/0/1. (PM09364)

\*Dec 10 10:55:57:448 2010 Sysname PIM/7/RP: -MDC=1;  Nbit: 0, Fragment tag: 0x5e67, Hash mask len: 30, BSR Priority: 64, BSR address: 4.0.0.10. (PM09368)

*// 向接口GigabitEthernet1/0/1发送BSR自举报文，N位没有设置，分片信息为0x5e67，哈希掩码长度为30，BSR优先级为64，BSR地址为4.0.0.10*

\*Dec 10 10:55:57:452 2010 Sysname PIM/7/RP: -MDC=1;  Group: 224.0.0.0/4, Bbit: 0, Zbit: 0, RP Count: 1, Frag RP Count: 1 (PM09378)

\*Dec 10 10:55:57:453 2010 Sysname PIM/7/RP: -MDC=1;   RP: 5.0.0.10 \-\-- Holdtime 180, Priority 192 (PM09382)

\*Dec 10 10:55:57:503 2010 Sysname PIM/7/RP: -MDC=1; Set BST of scope Global to 60. (RP041140)

*// 组播组224.0.0.0/4的信息为：B位没有设置，Z位没有设置，C-RP个数为1，分片信息为1。RP地址为5.0.0.10，保持时间为180秒，优先级为192。设置全局域自举定时器为60秒*

\# 接口上使能PIM-SM，并打开公网实例PIM组播路由表状态改变调试信息开关。

\<Sysname\> debugging pim routing-table

\*Dec 10 10:46:32:258 2010 Sysname PIM/7/ROUTE: -MDC=1; Creating (4.0.0.5, 225.0.0.25), flags: 0x00000004, down if protocol: 0 (SM134084)

*// 创建表项（4.0.0.5，225.0.0.25），标志为0x00000004，下游接口协议号为0（表示PIM-SM）*

\*Dec 10 10:46:32:272 2010 Sysname PIM/7/ROUTE: -MDC=1; ET(210s) create successfully for downstream (4.0.0.5, 225.0.0.25) on interface GigabitEthernet1/0/1 (6.0.0.10) (SM07344)

*// 为表项（4.0.0.5，225.0.0.25）的出接口GigabitEthernet1/0/1（IP地址为6.0.0.10）创建超时定时器（210秒）成功*

\*Dec 10 10:46:32:273 2010 Sysname PIM/7/ROUTE: -MDC=1; Downstream (4.0.0.5, 225.0.0.25) FSM on interface GigabitEthernet1/0/1 (6.0.0.10) transited from NoInfo to Join. Join Received (SM071418)

*// 接口GigabitEthernet1/0/1上的表项（4.0.0.5，225.0.0.25）的下游状态机从NoInfo状态越迁到加入状态，原因是收到加入报文*

\*Dec 10 10:46:46:515 2010 Sysname PIM/7/ROUTE: -MDC=1; Delete (3.0.0.5, 225.0.0.25) for inactive (SM12343)

*// 删除老化的表项（3.0.0.5，225.0.0.25）*

\# 在接口上使能PIM-DM，并打开公网实例接收PIM状态刷新报文的调试信息开关。

\<Sysname\> debugging pim state-refresh receive

\*Mar 16 05:50:15:086 2012 Sysname PIM/7/SRM: -MDC=1; PIM ver 2 SRM receiving 8.12.0.1 -\> 224.0.0.13 for (7.11.0.100, 225.0.0.1) on GigabitEthernet1/0/1, Originator address: 7.11.0.1, preference: 0, metric: 0, mask length: 16, ttl: 255, prune indicator: unset, prune now: unset, assert override: set, interval: 60s (DM141415)

*// 在接口GigabitEthernet1/0/1收到状态刷新报文，报文的源地址是8.12.0.1，目的地址是224.0.0.13；组播组为225.0.0.1/32；组播源为7.11.0.100；产生状态刷新报文设备的地址为7.11.0.1；优先级和Metric值都是0；掩码长度为16；TTL为255，没有设置Prune Indicator和Prune Now标志位，设置了Assert Override标志位；发送间隔为60秒*

\# 在接口上使能PIM-DM，并打开公网实例发送PIM状态刷新报文的调试信息开关。

\<Sysname\> debugging pim state-refresh send

\*Mar 16 05:50:15:086 2012 Sysname PIM/7/SRM: -MDC=1; PIM ver 2 SRM sending 8.24.0.2 -\> 224.0.0.13 for (7.11.0.100, 225.0.0.1) on GigabitEthernet1/0/1, Originator address: 7.11.0.1, preference: 10, metric: 2, mask length: 16, ttl: 254, prune indicator: unset, prune now: unset, assert override: set, interval: 60s. (DM09330)

*// 在接口GigabitEthernet1/0/1发送状态刷新报文，报文的源地址是8.24.0.2，目的地址是224.0.0.13；组播组为225.0.0.1/32；组播源为7.11.0.100；产生状态刷新报文设备的地址为7.11.0.1；优先级为10；Metric值为2；掩码长度都是16；TTL为254，没有设置Prune Indicator和Prune Now标志位，设置了Assert Override标志位；发送间隔为60秒*
