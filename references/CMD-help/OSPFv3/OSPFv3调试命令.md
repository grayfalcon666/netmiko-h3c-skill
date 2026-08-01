<!-- CMD-INDEX
  debugging ospfv3 event              | 用户视图             | L11
  debugging ospfv3 lsa                | 用户视图             | L541
  debugging ospfv3 packet             | 用户视图             | L731
  debugging ospfv3 policy             | 用户视图             | L1075
  debugging ospfv3 redistribute       | 用户视图             | L1371
  debugging ospfv3 spf                | 用户视图             | L1707
  debugging ospfv3 timer              | 用户视图             | L2173
-->

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 event**

------------------------------------------------------------------------

【命令】

**[debugging ospfv3 **[ *process-id*  **event** [ **bfd** \| **error** \| **graceful-restart** \| **interface** \| **neighbor** ]]]

**[undo debugging ospfv3** [ *process-id*  **event** [ **bfd** \| **error** \| **graceful-restart** **interface** \| **neighbor** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[bfd**]：表示BFD事件调试信息开关。

**[error**]：表示错误事件调试信息开关。

**[graceful-restart**]：表示GR事件调试信息开关。

**[interface**]：表示接口事件调试信息开关。

**[neighbor**]：表示邻居事件调试信息开关。

【描述】

**[debugging ospfv3 event**]命令用来打开OSPFv3事件调试信息开关。**undo****debugging ospfv3 event**命令用来关闭OSPFv3事件调试信息开关。

缺省情况下，OSPFv3事件调试信息开关处于关闭状态。

如果未指定进程号，则打开所有OSPFv3进程的事件调试信息开关。

表1-1 debugging ospfv3 event bfd命令输出信息描述表

字段

描述

Receive bfd event (*number*)

接收到BFD事件

·*number*：BFD事件类型

*[Notify bfd smooth stop*]

通知BFD平滑停止

Bfd session create for process (*number1*), (*number2*), nbr (*x.x.x.x*), src (*address1*), dst (*address2*), RetVal: (*number3*).

创建BFD会话

·*number1*：指定进程ID

·*number2*：指定接口

·x.x.x.x：指定邻居的Router ID

·*address1*：BFD会话的源地址

·*address2*：BFD会话的目的地址

·*number3*：调用BFD接口的返回值

Bfd session delete for process (*number1*), (*number2*), nbr (*x.x.x.x*), src (*address1*), dst (*address2*), RetVal: (*number3*).

删除BFD会话

·*number1*：指定进程ID

·*number2*：指定接口

·*x.x.x.x*：邻居Router ID

·*address1*：BFD会话的源地址

·*address2*：BFD会话的目的地址

·*number3*：调用BFD接口的返回值

Bfd session disable for process (*number1*), (*number2*), nbr (*x.x.x.x*), src (*address1*), dst (*address2*), RetVal: (*number3*).

去使能BFD会话

·*number1*：指定进程ID

·*number2*：指定接口

·*x.x.x.x*：邻居Router ID

·*address1*：BFD会话的源地址

·*address2*：BFD会话的目的地址

·*number3*：调用BFD接口的返回值

Bfd smooth, collect Gr process (*number*).

BFD平滑，收集正在做GR的进程

·*number*：进程ID

Bfd smooth, no Gr process, Notify bfd smooth stop.

BFD平滑，没有处于GR的进程，通知BFD平滑停止

Bfd smooth, process (*number1*) Gr completed or deleted, bfd Gr Process list count: (*number2*).

BFD平滑，指定进程的GR过程完成或者删除

·*number1*：指定进程的ID

·*number2*：当前处于GR状态的进程计数

Bfd connected, process all session.

BFD连接成功，处理所有的会话

Bfd disconnect, clear all session.

BFD失去连接，清除所有的会话

Bfd session add radix nbr for process (*number1*), (*number2*), nbr (*x.x.x.x)*, instanceId (*number3*), Count: (*number4*), src (*address1*), dst (*address2*).

BFD会话添加新节点到Radix树中

·*number1*：指定进程ID

·*number2*：指定接口

·*x.x.x.x*：邻居Router ID

·*number3*：实例ID

·*number4*：当前节点个数

·*address1*：BFD会话的源地址

·*address2*：BFD会话的目的地址

Bfd session delete radix nbr for process (*number1*), (*number2*), nbr (*x.x.x.x*), instanceId (*number3*), Count: (*number4*), src (*address1*), dst (*address2*).

BFD会话删除Radix树中指定节点

·*number1*：指定进程ID

·*number2*：指定接口

·*x.x.x.x*：邻居Router ID

·*number3*：实例ID

·*number4*：当前节点个数

·*address1*：BFD会话的源地址

·*address2*：BFD会话的目的地址

表1-2 debugging ospfv3 event error命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

Neighbor *nbr-id*

邻居的Router ID

OSPFv3 *process-id* Gen Dbsummary list fail

生产DD summary列表失败

joining the multicastgroup *goupname*, Failed: *value*, IfNetIndex: *if-index(if-name)*.

加入组播组失败

·*goupname*：组播组名

·*value*：错误码

·*if-index*：接口索引

·*if-name*：接口名称

leaving the multicastgroup *goupname*, Failed: *value*, IfNetIndex: *if-index(if-name)*.

离开组播组失败

·*goupname*：组播组名

·*value*：错误码

·*if-index*：接口索引

·*if-name*：接口名称

表1-3 debugging ospfv3 event graceful-restart命令输出信息描述表

字段

描述

OSPFv3 *number*

OSPFv3进程号

create grace LSA send timer, timeout value is *number* (ms)

Restarter创建发送Grace LSA定时器

·*number*：表示定时器间隔

delete grace LSA send timer

Restarter端删除发送Grace LSA定时器

create GR waiting timer, timeout value is *number* (ms)

Restarter创建等待定时器，用来发现Helper

·*number*：表示定时器间隔

delete GR waiting timer

Restarter端删除等待定时器

GR waiting timer expired

Restarter端等待定时器超时

create GR period timer, timeout value is *number* (ms)

Restarter端创建平滑重启时间定时器

·*number*：表示定时器间隔

delete GR period timer

Restarter端删除平滑重启时间间隔定时器

GR period timer expired

Restarter端平滑重启时间间隔定时器超时

received newer grace LSA from neighbor *x.x.x.x*

Helper端从邻居收到新的Grace LSA

·*x.x.x.x*：表示邻居的Router ID

received maximum age grace LSA from neighbor *x.x.x.x*

Helper端从邻居收到新的Grace LSA并且LSA的age=3600

·*x.x.x.x*：表示邻居的Router ID

received maximum age grace LSA, no neighbor  *x.x.x.x*

Helper端收到新的age=3600的Grace LSA，发现发送该LSA的路由器不是自己的邻居

·*x.x.x.x*：Router ID

received grace LSA, GR helper is not enabled

Helper端收到Grace LSA，但是未使能GR Helper能力

not enter helper mode, support planned GR only

Helper端不进入helper模式，只支持计划性GR

received grace LSA, age *number1* larger than GR period *number2*

Helper端收到Grace LSA，但是收到的Grace LSA中age大于GR interval

·*number1*：LS age字段

·*number2*：GR interval字段

not enter helper mode, neighbor is neither full nor 2-way.

Helper端不进入Helper模式，因为邻居不是full状态或者2-way状态

already enter helper mode, neighbor is neither full nor 2-way.

Helper端已经进入Helper模式，邻居不是full或者2-way状态

not enter helper mode, LSA in retransmit-list content is changed

不进入Helper模式，因为重传链中的LSA发生变化

received invalid grace LSA

Helper端收到无效的Grace LSA

received grace LSA, but GR period *number* invalid.

Helper端收到Grace LSA，但是收到的Grace LSA中period字段无效

·*number*：Grace LSA中指定的period值

received grace LSA, but GR reason invalid

Helper端收到Grace LSA，但是收到的Grace LSA中GR reason字段无效

received grace LSA, but no neighbor *x.x.x.x*

Helper端收到Grace LSA，但是邻居列表中没有通告的邻居

·*x.x.x.x*：Grace LSA中通告的邻居Router ID

not enter helper mode, router is restarter.

Helper端不进入Helper模式，因为正在作为Restarter端平滑重启

create GR period timer *number1* for neighbor *x.x.x.x*, timeout interval is *number2*(s)

Helper端为指定的邻居创建平滑间隔定时器

·*number1*：定时器标编号

·*x.x.x.x*：指定的邻居Router ID

·*number2*：定时器间隔

delete GR period timer for neighbor *x.x.x.x*.

删除对指定邻居创建的平滑间隔定时器

·*x.x.x.x*：指定邻居的Router ID

restart GR period timer, return value: *number1* for neighbor *x.x.x.x*, timeout interval is *number2*(s).

Helper端为指定邻居重置平滑间隔定时器

·*number1*：重置平滑间隔定时器后返回值，查看是否重置成功，0表示成功。

·*x.x.x.x*：指定邻居的Router ID

·*number2*：定时器间隔设定值

enter helper mode for neighbor *x.x.x.x* of *interface*. Neighbor count in IETF GR restart is *number*.

Helper端为指定邻居进入Helper模式

·*x.x.x.x*：指定邻居的Router ID

·*interface*：邻居所在的接口

·*number*：此时本Helper端对应的Restarter个数

exit helper mode for neighbor *x.x.x.x* of *interface, exitreason*. Neighbor count in IETF GR restart is *number*.

Helper端为指定邻居离开Helper模式

·*x.x.x.x*：指定的邻居Router ID

·*interface*：邻居所在的接口

·*exitreason*：退出原因

·*number*：此时本Helper端对应的Restarter个数

received maximum age grace LSA from *x.x.x.x*, not helper mode for the neighbor.

Helper端接收到指定邻居发来的age为3600的Grace LSA，但本Helper端不作为指定邻居的Helper

process exit all helper mode.

Helper端不再做任何邻居的Helper

process exit helper mode abnormally, LSA check failed. LSA type: 0x*number1*, Lsid: *number2*, Adv: *x.x.x.x*.

Helper端退出Helper模式，因为LSA严格检查失败。

·*number1*：严格检查失败的LSA的类型

(1)0x2001表示Router -LSA

(2)0x2002表示Network-LSA

(3)0x2003表示Inter-Area-Prefix-LSA

(4)0x2004表示Inter-Area-Router-LSA

(5)0x4005表示AS-External-LSA

(6)0x0008表示Link-LSA

(7)0x2009表示Intra-Area-Prefix-LSA

(8)0x000b表示Grace-LSA

·*number2*：该LSA的Link State ID

·*x.x.x.x*：该LSA的通告路由器

DR/BDR is confilicting with helper.

当前DR/BDR与Helper端发来的Hello报文中通告的DR/BDR不一致

DR/BDR recovered from DBM: x.x.x.x/x.x.x.x, helper\'s DR/BDR: x.x.x.x/x.x.x.x.

从DBM里恢复的DR/BDR和helper带过来的DR/BDR。

·*x.x.x.x*：被选为DR或者BDR的Router ID

local DR/BDR: x.x.x.x/x.x.x.x, helper\'s DR/BDR: x.x.x.x/x.x.x.x.

本地的DR/BDR和helper带过来的DR/BDR。

·*x.x.x.x*：被选为DR或者BDR的Router ID

exit restarter mode for interface *interface*, *exitreason*.

Restarter端某个接口退出Restarter模式。

·*interface*：退出GR的接口

·*exitreason*：接口退出原因

process exit restarter mode, all neighbors have been done.

Restarter端的所有邻居都平滑重启完成

process exit restarter mode abnormally, interface changed.

Restarter端退出Restarter模式，因为接口发生改变

process exit restarter mode abnormally, neighbor changed.

Restarter端退出Restarter模式，因为邻居发生改变

process exit restarter mode abnormally, GR period timer expired.

Restarter端退出Restarter模式，因为超过了平滑重启时间

process exit restarter mode, no interface up.

Restarter端退出Restarter模式，因为没有接口up

graceful restart is finished

Restarter端完成了平滑重启

表1-4 debugging ospfv3 event interface命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

Interface *if-name* received *event* and its state from *pre-state* -\> *cur-state*.

接口状态变化

·*if-name*：接口名称

·*event*：接口状态机事件

·*pre-state/cur-state*：接口状态机状态

表1-5 debugging ospfv3 event neighbor命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

Neighbor *nbr-id* (*if-name*) received *event* and its state from *pre-state* -\> *cur-state*.

邻居状态变化

·*nbr-id*：邻居的Router ID

·*if-name*：接口名称

·*event*：邻居状态机事件

·*pre-state/cur-state*：邻居状态机状态

【举例】

\# Router A通过GigabitEthernet1/0/2（1001::1/64）与Router B的GigabitEthernet1/0/1（1001::2/64）相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域1，在GigabitEthernet1/0/2上使能OSPFv3功能并配置其属于区域1；在Router B上创建OSPFv3进程1，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域1。在Router A上打开邻居事件调试信息开关。

\<RouterA\> debugging ospfv3 event neighbor

\*Apr 20 15:44:55:319 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor 2.2.2.2(GigabitEthernet1/0/2) received HelloReceived and its state from Down -\> Init.

*// 邻居状态由Down变为Init*

\*Apr 20 15:44:55:319 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor 2.2.2.2(GigabitEthernet1/0/2) received 2WayReceived and its state from Init -\> ExStart.

*// 邻居状态由Init变为Exstart*

\*Apr 20 15:45:24:276 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor 2.2.2.2(GigabitEthernet1/0/2) received NegotiationDone and its state from ExStart -\> Exc

hange.

*// 邻居状态由Exstart变为Exchange*

\*Apr 20 15:45:24:286 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor 2.2.2.2(GigabitEthernet1/0/2) received ExchangeDone and its state from Exchange -\> Loadi

ng.

*// 邻居状态由Exchange变为Loading*

\*Apr 20 15:45:24:286 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor 2.2.2.2(GigabitEthernet1/0/2) received LoadingDone and its state from Loading -\> Full.

*// 邻居状态由Loading变为Full*

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 lsa**

------------------------------------------------------------------------

【命令】

**[debugging ospfv3** [ *process-id*  **lsa** { **generate** \| **install** \| **receive** }]]

**[undo debugging ospfv3** [ *process-id*  **lsa** { **generate** \| **install** \| **receive** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[generate**]：表示LSA生成调试信息开关。

**[install**]：表示将LSA导入到LSDB中的调试信息开关。

**[receive**]：表示LSA接收调试信息开关。

【描述】

**[debugging ospfv3 lsa**]命令用来打开LSA调试信息开关。**undo debugging ospfv3 lsa**命令用来关闭LSA调试信息开关。

缺省情况下，LSA调试信息开关处于关闭状态。

如果未指定进程号，则打开所有OSPFv3进程的LSA调试信息开关。

表1-6 debugging ospfv3 lsa命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

LS Age = *lsa-age*

LSA的生存时间

LS Type = *lsa-type*

*[lsa-type*]：LSA类型

·0x2001表示Router-LSA

·0x2002表示Network-LSA

·0x2003表示Inter-area-prefix-LSA

·0x2004表示Inter-area-router-LSA

·0x4005表示AS-External-LSA

·0x2007表示NSSA-LSA

·0x0008表示Link-LSA

·0x2009表示Intra-Area-Prefix-LSA

LS ID = *ls-id*

LSA的链路状态ID

Adv ID = *adv-id*

发布LSA的Router ID

Seq Number = *seqnum*

LSA序列号

Cksum = *chksum*

LSA校验和

Length = *length*

LSA长度

Generate LSA at *time-stamp* ms.

生成LSA的时间

Install LSA at *time-stamp* ms.

安装LSA的时间

Receive LSA at *time-stamp* ms.

接收LSA的时间

【举例】

\# Router A通过GigabitEthernet1/0/2（1001::1/64）与Router B的GigabitEthernet1/0/1（1001::2/64）相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域1，在GigabitEthernet1/0/2上使能OSPFv3功能并配置其属于区域1；在Router B上创建OSPFv3进程1，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域1。在Router A上打开LSA生成调试信息开关。

\<RouterA\> debugging ospfv3 lsa generate

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2402163 ms.

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x2001

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.0

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000001

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0x101e

\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 24

*// 生成Router LSA*

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2402164 ms.

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x0008

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.3

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000001

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0xfee

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 56

*// 生成Link LSA*

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2402164 ms.

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x2009

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.1

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000001

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0x4368

\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 44

*// 生成Intra-Area-Prefix-LSA*

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2410239 ms.

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x2001

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.0

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000007

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0x8c66

\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 40

*// 重新生成Router LSA*

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 packet**

------------------------------------------------------------------------

【命令】

**[debugging ospfv3 **[ *process-id*  **packet** [ **ack** \| **dd** \| **hello** \| **request** \| **update** ]]]

**[undo debugging ospfv3** [ *process-id*  **packet** [ **ack** \| **dd** \| **hello** \| **request** \| **update** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[ack**]：表示LSAck报文调试信息开关。

**[dd**]：表示DD报文调试信息开关。

**[hello**]：表示Hello报文调试信息开关。

**[request**]：表示LSR报文调试信息开关。

**[update**]：表示LSU报文调试信息开关。

【描述】

**[debugging ospfv3 packet**]命令用来打开OSPFv3报文调试信息开关。**undo debugging ospfv3 packet**命令用来关闭OSPFv3报文调试信息开关。

缺省情况下，OSPFv3报文调试信息开关处于关闭状态。

如果未指定进程号，则打开所有OSPFv3进程的报文调试信息开关。

表1-7 debugging ospfv3 packet命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

Interface id: *interface-id*

接口ID

Router Priority: *router-pri*

路由器优先级

Option: *option*

选项字段

Hello Interval: *interval*

Hello报文时间间隔

Dead Interval: *interval*

超时时长

DR: *router-id*

DR的Router ID

BDR: *router-id*

BDR的Router ID

MTU: *value*

MTU值

R_I_M_MS Bit: *value*

DD报文R_I_M_MS字段值

DD Sequence number: *seq-value*

DD报文序列号

LSA type: *lsa-type*

LSA类型

LinkStateId: *ls-id*

LSA的LS ID

Advertising Rtr: *router-id*

发布路由器ID

LSA age: *lsa-age*

LSA年龄

Length: *value*

长度

Checksum: *value*

校验和

LSA count: *value*

LSU报文保护的LSA数目

Version *value*

版本号

Source address: *src-addr*

源地址

Destination address: *dst-addr*

目的地址

Receiving packets

收到报文

OSPFv3 received packet having bad type :*value*

收到错误的类型报文

·*value*：报文类型

Sending packets

发送报文

OSPFv3 received packet with invalid destination

收到错误的目的地址报文

OSPFv3 received packet having conflicted Router ID :*router-id*

收到重复的Router-ID报文

·*router-id*：路由器ID

OSPFv3 received packet with mismatch AREA

收到区域不匹配的报文

Ignored the packet on interface *interface-type interface-number* due to IPsec profile mismatch.

IPsec安全框架不匹配，忽略该报文

·*interface-type interface-number*：接口类型和编号，从该接口收到OSPFv3报文

【举例】

\# Router A通过GigabitEthernet1/0/2（1001::1/64）与Router B的GigabitEthernet1/0/1（1001::2/64）相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域1，在GigabitEthernet1/0/2上使能OSPFv3功能并配置其属于区域1；在Router B上创建OSPFv3进程1，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域1。在Router A上打开DD报文调试信息开关。

\<RouterA\> debugging ospfv3 packet dd

\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.

\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205

\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100

\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.

\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|MS.]

\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00002368.

*// 发送DD报文*

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Receiving packets.

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::200:5eff:fe00:100

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::20c:29ff:fe85:9205

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 2.2.2.2, Area: 0.0.0.1, Checksum: 41302, Instance: 0.

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|MS.]

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003782.

*// 接收DD报文*

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 88.

\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|-.]

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003782.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 0008.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.3.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 1.1.1.1.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 6.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 56 Sequence number: 80000001 Checksum: 0fee.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2001.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.0.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 1.1.1.1.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 6.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 24 Sequence number: 80000001 Checksum: 101e.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2009.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.1.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 1.1.1.1.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 6.

\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 44 Sequence number: 80000001 Checksum: 4368.

*// 发送DD报文*

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Receiving packets.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::200:5eff:fe00:100

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::20c:29ff:fe85:9205

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 88.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 2.2.2.2, Area: 0.0.0.1, Checksum: 35496, Instance: 0.

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|MS.]

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003783.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 0008.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.15.0.8.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 2.2.2.2.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 214.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 56 Sequence number: 80000001 Checksum: 04d4.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2001.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.0.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 2.2.2.2.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 167.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 24 Sequence number: 80000003 Checksum: ed3a.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2009.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.1.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 2.2.2.2.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 166.

\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 44 Sequence number: 80000002 Checksum: 554d.

*// 接收DD报文*

\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.

\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205

\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100

\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.

\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.

[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|-.]

\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003783.

*// 发送DD报文*

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Receiving packets.

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::200:5eff:fe00:100

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::20c:29ff:fe85:9205

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 2.2.2.2, Area: 0.0.0.1, Checksum: 41306, Instance: 0.

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: -\|-\|MS.]

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003784.

*// 接收DD报文*

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: -\|-\|-.]

\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003784.

*// 发送DD报文*

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 policy**

------------------------------------------------------------------------

【命令】

**[debugging** **ospfv3** [ *process-id*  **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **export** \| **import** \| **preference** }]]

**[undo** **debugging** **ospfv3** [ *process-id*  **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **export** \| **import** \| **preference** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[abr-filter**]：打开3类LSA过策略调试开关。

**[all**]：打开所有路由过策略的调试开关。

**[default-route**]：打开默认路由过策略的调试开关。

**[event**]：打开策略事件的调试开关。

**[export**]：打开引入路由过策略的调试开关。

**[import**]：打开下路由过策略的调试开关。

**[preference**]：打开优先级过策略的调试开关。

【描述】

**[debugging** **ospfv3** **policy**]命令用来打开OSPFv3路由过策略调试信息开关。**undo****debugging** **ospfv3** **policy**命令用来关闭OSPFv3路由过策略调试信息开关。

缺省情况下，OSPFv3路由过策略调试信息开关处于关闭状态。

如果未指定进程号，则打开所有OSPFv3进程的路由过策略调试信息开关。

表1-8 debugging ospfv3 policy abr-filter命令输出信息描述表

字段

描述

OSPFv3 *process-id* checked abr-filter policy, area *area-id*, abr-filter type: *abr-filter-type,* flag: *flag*, policy type: *policy-type*, policy name: *name,* check address: *check-addr,* mask length: *length*

Type-3 LSA过策略相关信息

·*process-id*：OSPFv3进程ID

·*area-id*：区域ID

·*abr-filter-type*：ABR策略类型，取值为import表示对向本区域发布的Type-3 LSA进行过策略，export表示对向其它区域发布的Type-3 LSA进行过策略

·*flag*：标志位，取值为1表示对下一跳过策略，取值为2表示对前缀过策略

·*policy-type*：过策略类型，包括acl，prefix-list和route-policy三种类型

·*name*：策略名

·*check-addr*：过策略的前缀

·*len**gth*：前缀掩码长度

OSPFv3 *process-id*checked abr-filterpolicy result: *result,* cost: *cost*

Type-3 LSA过策略结果

·*process-id*：OSPFv3进程ID

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*cost*：过策略后的开销

表1-9 debugging ospfv3 policy default-route命令输出信息描述表

字段

描述

OSPFv3 *process-id* received default-route policy message, result: *result*, flag: *flag*, cost type: *type*, cost: *cost*

OSPFv3收到默认路由过策略消息

·*process-id*：OSPFv3进程ID

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*flag*：标志位，0x0表示无应用，0x1表示应用cost，0x2表示应用cost type，0x8表示应用tag，若存在多个应用，该标志位为或的关系

·*type*：默认路由类型，type-1表示一类外部路由，type-2表示二类外部路由，unknown表示未知类型

·*cost*：过策略后的开销

OSPFv3 *process-id* checked default-route policy permit, flag: *flag*, cost type: type, cost: *cost*

默认路由过策略通过后的结果

·*process-id*：OSPFv3进程ID

·*flag*：标志位，0x0表示无应用，0x1表示应用cost，0x2表示应用cost type，0x8表示应用tag，若存在多个应用，该标志位为或的关系

·*type*：默认路由类型，type-1表示一类外部路由，type-2表示二类外部路由，unknown表示未知类型

·*cost*：过策略后的开销

OSPFv3 *process-id* checked default-route policy deny.

默认路由过策略不通过

·*process-id*：OSPFv3进程ID

表1-10 debugging ospfv3 policy event命令输出信息描述表

字段

描述

OSPFv3 *process-id* received policy change event, import reference count: *number1*, calculate reference count: *number2*

OSPFv3进程过策略信息统计

·*process-id*：OSPFv3进程ID

·*number1*：本策略被进程引入过策略计数

·*number2*：本策略被路由计算引入计数

OSPFv3 *process-id* ignored policy change when process is under GR

OSPFv3进程处于GR状态而忽略策略变化

·*process-id*：OSPFv3进程ID

OSPFv3 received acl number *acl-number* change event

OSPFv3收到acl变化事件

·*acl-number*：访问控制列表号

OSPFv3 received prefix-list *name* change event

OSPFv3收到前缀列表变化事件

·*name*：前缀列表名

OSPFv3 received route-policy *name* change event

OSPFv3收到路由策略变化事件

·*name*：路由策略名

OSPFv3 received prefix-list batch end message

OSPFv3收到前缀列表批处理结束消息

OSPFv3 received route-policy batch end message

OSPFv3收到路由过策略批处理结束消息

表1-11 debugging ospfv3 export命令输出信息描述表

字段

描述

OSPFv3 *process-id* checked export policy, address: *addr,* mask length: *length*

引入路由过策略相关信息

·*process-id*：OSPFv3进程ID

·*addr*：过策略的前缀

·*length*：前缀掩码长度

OSPFv3 *process-id*checked exportpolicy result: *result*, cost: *cost*

引入路由过策略结果

·*process-id*：OSPFv3进程ID

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

·*cost*：表示过策略后的开销

表1-12 debugging ospfv3 import命令输出信息描述表

字段

描述

OSPFv3 *process-id* checked import policy, policy type: *type,* policy name: *name,* prefix: *prefix,* nexthop: *nexthop,* cost: *cost,* interface index: *if-index*

下路由过策略相关信息

·*process-id*：OSPFv3进程ID

·*type*：下路由过策略类型，包括acl，prefix-list和route-policy三种类型

·*name*：下路由过策略名

·*prefix*：路由前缀

·*nexthop*：下一跳地址

·*cost*：下一跳开销

·*if-index*：出接口索引

OSPFv3 *process-id* checked import policy result: *result*

下路由过策略结果

·*process-id*：OSPFv3进程ID

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

表1-13 debugging ospfv3 preference命令输出信息描述表

字段

描述

OSPFv3 *process-id* checked preference policy, preference: *pref,* policy name: *name,* prefix: *prefix,* nexthop: *nexthop,* cost: *cost,* interface index: *if-index*

路由优先级过策略相关信息

·*process-id*：OSPFv3进程ID

·*pref*：路由优先级

·*name*：路由优先级过策略名

·*prefix*：路由前缀

·*nexthop*：下一跳地址

·*cost*：下一跳开销

·*if-index*：出接口索引

OSPFv3 *process-id* checked preference policy result: *result*

路由优先级过策略的调试结果

·*process-id*：OSPFv3进程ID

·*result*：过策略结果，取值为permit表示通过，deny表示不通过

【举例】

\# Router A通过GigabitEthernet1/0/1（1::1/64）与Router B的GigabitEthernet1/0/1（1::2/64）相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域0；配置默认路由策略，在Router A上打开默认路由过策略的调试信息开关。

\<RouterA\> debugging ospfv3 policy default-route

\*Nov  5 17:11:49:217 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 received default-route policy message, result: permit, flag: 0x1,

cost type: 2, cost: 33.

*// 接收到默认路由过策略消息*

\*Nov  5 17:11:49:217 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 checked default-route policy permit, flag: 0x1, cost type: type-2,

cost: 33.

*// 默认路由过策略通过后的结果*

\# Router A通过GigabitEthernet1/0/1（1::1/64）与Router B的GigabitEthernet1/0/1（1::2/64）相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域0，配置静态路由1::8/128，引入静态路由；在Router B上创建OSPFv3进程1，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域0；配置策略，在Router A上打开引入路由过策略的调试信息开关。

\<RouterA\> debugging ospfv3 policy export

\*Nov  5 14:46:01:042 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

OSPFv3 1 checked export policy address: 1::8, mask Length: 128.

*// 引入路由过策略相关信息*

\*Nov  5 14:46:01:042 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 checked export policy result: permit, cost: 0.

*// 引入路由过策略结果*

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 redistribute**

------------------------------------------------------------------------

【命令】

**[debugging** **ospfv3** [ *process-id*  **redistribute**  **prefix** *ipv6-address prefix-length* ]]

**[undo** **debugging** **ospfv3** [ *process-id*  **redistribute**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[prefix** *ipv6-address prefix-length*]：表示指定IPv6地址的引入路由调试信息开关。*ipv6-address*表示IPv6地址前缀；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。

【描述】

**[debugging** **ospfv3** **redistribute**]命令用来打开OSPFv3引入路由调试信息开关。**undo****debugging** **ospfv3** **redistribute**命令用来关闭OSPFv3引入路由调试信息开关。

缺省情况下，OSPFv3引入路由调试信息开关处于关闭状态。

如果未指定进程号，则打开所有OSPFv3进程的引入路由调试信息开关。如果未指定IPv6地址前缀，则显示所有的引入路由调试信息。

表1-14 debugging ospfv3 redistribute命令输出信息描述表

字段

描述

OSPFv3 received rib batch start message, instance: *instance-id*, user data: *user-data*

OSPFv3实例收到批处理开始的消息

·*instance-id*：路由所在VPN

·*user-data*：消息中携带的用户数据值

OSPFv3 received rib batch end message, instance: *instance-id*, user data: *user-data*

OSPFv3实例收到批处理结束的消息

·*instance-id*：路由所在VPN

·*user-data*：消息中携带的用户数据值

OSPFv3 received rib smooth start message

OSPFv3收到平滑开始的消息

OSPFv3 received rib smooth end message

OSPFv3收到平滑结束的消息

 OSPFv3 *process-id* triggered redistributed type *type*

OSPFv3进程触发路由引入

·*process**-id*：OSPFv3进程ID

·*type*：引入类型，0x1表示从RIB表引入，0x2表示从自身的引入表引入

OSPFv3 received rib refresh message, instance: *instance-id*, address: *addr*,user data: *user-data*, metric: *metric*, protocol ID: *protocol-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*

OSPFv3实例收到普通路由刷新消息

·*instance-id*：路由所在VPN

·*addr*：该条路由的IPv6地址

·*user-data*：消息中携带的用户数据

·*metric*：该条路由的开销

·*protocol-id*：该条路由所属的协议ID，1表示直连路由，2表示静态路由，3表示ripng，4表示ospfv3，5表示isisv6，6表示bgp4+

·*subProtocol-id*：该条路由的子协议ID

·*count*：该条路由的下一跳个数

OSPFv3 received rib change message, instance: *instance-id*, address: *addr*, user data: *user-data*, table ID: *table-id*, last protocol ID: *protocol-id*

OSPFv3实例收到普通路由删除消息

·*instance-id*：路由所在VPN

·*addr*：该条路由的IPv6地址

·*user-data*：消息中携带的用户数据

·*table-id*：该条路由所在的路由表ID

·*protocol-id*：该条路由上次上报时所属协议类型

OSPFv3 *process-id* scanned redistributed route, nexthop: *nexthop*, interface index: *if-index*, vrfIndex: *vrfIndex*, process ID: *process-id2*, flag: *flag*

OSPFv3进程扫描特定进程的引入条目

·*process**-id*：OSPFv3进程ID

·*nexthop*：下一条地址

·*if-index*：出接口索引

·*vrfIndex*：转发表索引

·*process-id2*：引入条目所在的进程ID

·*flag*：路由标志

OSPFv3 *process-id* processed redistributed route, address: *addr*, type: *type*, metric: *metric*, protocol ID: *protoco-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*, option: *option*, last option: *last-option*

OSPFv3进程处理引入的路由

·*process**-id*：OSPFv3进程ID

·*addr*：路由IPv6地址

·*type*：引入类型

·*metric*：路由开销

·*protoco-id*：该路由所属协议ID

·*subProtocol-id*：该路由所属子协议ID

·*count*：下一跳个数

·*option*：当前可选项

·*last-option*：原来可选项

OSPFv3 *process-id* added type-5 LSA to LSDB, address: *addr*, option: *option*, metric: *metric*, EFTBits: *EFTBits*, LsID: *lsid*

OSPFv3进程为引入的路由添加5类LSA

·*process**-id*：OSPFv3进程ID

·*addr*：引入路由的IPv6地址

·*option*：可选项数值

·*metric*：路由开销

·*EFTBits*：EFT标志位数值

·*lsid*：产生的5类LSA的Link State ID

OSPFv3 *process-id* deleted type-5 LSA from LSDB, address: *addr*, option: *option*, EFTBits: *EFTBits*, LsID: *lsid*

OSPFv3进程删除由引入的路由生成的5类LSA

·*process**-id*：OSPFv3进程ID

·*addr*：引入路由的IPv6地址

·*option*：可选项数值

·*EFTBits*：EFT标志位数值

·*lsid*：产生的5类LSA的Link State ID

OSPFv3 *process-id* added default-route LSA, option: *option*, metric: *metric*, LsID: *lsid*

OSPFv3添加默认路由LSA

·*process-id*：OSPFv3进程ID

·*option*：OSPFv3前缀选项

·*metric*：默认路由开销

·*lsid*：链路状态ID

OSPFv3 *process-id* deleted default-route LSA, option: *option*, LsID: *lsid*

OSPFv3删除默认路由LSA

·*process-id*：OSPFv3进程ID

·*option*：OSPFv3前缀选项

·*lsid*：链路状态ID

OSPFv3 *process-id* added prefix to routing table, address: *addr*, metric: *metric*, option: *option*, version: *version*, protocol ID: *protocol-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*, result: *result*

OSPFv3进程添加引入的路由前缀到引入路由表

·*process**-id*：OSPFv3进程ID

·*addr*：引入路由地址

·*metric*：引入路由的度量值

·*option*：引入路由的可选项数值

·*version*：引入路由的版本号

·*protocol-id*：所属协议ID

·*subProtocol-id*：所属的子协议ID

·*count*：下一跳个数

·*result*：路由前缀添加结果，取值success表示添加成功，取值fail表示添加失败

OSPFv3 *process-id* deleted prefix from routing table, address: *addr*, metric: *metric*, option: *option*, version: *version*, protocol ID: *protocol-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*

OSPFv3进程从引入路由表中删除指定前缀

·*process**-id*：OSPFv3进程ID

·*addr*：引入路由地址

·*metric*：引入路由的度量值

·*option*：引入路由的可选项数值

·*version*：引入路由的版本号

·*protocol-id*：所属协议ID

·*subProtocol-id*：所属的子协议ID

·*count*：下一跳个数

OSPFv3 *process-id* queried rib route, instance: *instance-id*, protocol ID: *protocol-id*, synRt Fd: *fd*

OSPFv3进程向路由管理查询指定实例的路由

·*process**-id*：OSPFv3进程ID

·*instance-id*：进程所在的实例ID

·*protocol**-id*：需要查询的协议ID

·*fd*：路由管理进程的文件描述符

【举例】

\# Router A通过GigabitEthernet1/0/2（1::1/64）与Router B的GigabitEthernet1/0/1（1::2/64）相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域2，在GigabitEthernet1/0/2上使能OSPFv3功能并配置其属于区域2，；在Router B上创建OSPFv3进程1，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域2。在Router A上打开引入路由调试信息开关，配置静态路由1::9/128，并引入静态路由。

\<RouterA\> debugging ospfv3 redistribute

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 received rib batch start message, instance: 0, user data: 0x0.

*[// OSPFv3*]*实例收到批处理开始的消息*

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 received rib refresh message, instance: 0,address: 1::9/128,

user data: 0x0, metric: 0, protocol ID: 2, subProtocol ID: 0,

nexthop count: 1.

*[// OSPFv3*]*实例收到普通路由刷新消息*

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 scanned redistributed route, nexthop: ::, interface index: 273,

vrfIndex: 0, process 0, flag: 0x10000.

*[// OSPFv3*]*进程扫描特定进程的引入条目*

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 processed redistributed route, address: 1::9/128, type: 1,

metric: 0, protocol ID: 2, subProtocol ID: 0, nexthop count: 1,

option: 0x4, last option: 0x0.

*[// OSPFv3*]*进程处理引入的路由*

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 added type-5 LSA to LSDB, address: 1::9/128, option:0x0,

metric: 1, EFTBits: 0x4, LsID: 0.

*[// OSPFv3*]*进程为引入的路由添加5类LSA*

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 added prefixto routing table, address: 1::9/128, metric:0,

option: 0x4, version: 1, protocol ID: 2, subProtocol ID: 0,

nexthop count: 1, result: success.

*[// OSPFv3*]*进程添加引入的路由前缀到引入路由表*

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 received rib batch end message, instance: 0, user data: 0x0.

*[// OSPFv3*]*实例收到批处理结束的消息*

\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 triggered redistributed type 0x2.

*[// OSPFv3*]*进程触发路由引入*

\*Nov  5 16:21:07:573 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 scanned redistributed route, nexthop: ::, interface index: 273,

vrfIndex: 0, process Id: 0, flag: 0x10000.

*[// OSPFv3*]*进程扫描特定进程的引入条目*

\*Nov  5 16:21:07:573 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 processed redistributed route, address: 1::9/128,

redistribute type: 2, metric: 0, protocol ID: 2, subProtocol ID: 0,

nexthop count: 1, option: 0x4, last option: 0x4.

*[// OSPFv3*]*进程处理引入的路由*

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 spf**

------------------------------------------------------------------------

【命令】

**[debugging ospfv3 **[ *process-id*  **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **tree** }]]

**[undo debugging ospfv3** [ *process-id*  **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **tree** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[all**]：表示全部SPF路由计算调试信息开关。

**[asbr**]：表示ASBR的SPF路由计算调试信息开关。

**[brief**]：表示SPF路由计算概要调试信息开关。

**[external**]：表示AS外SPF路由计算的调试信息开关。

**[internal**]：表示AS内SPF路由计算调试信息开关。

**[tree**]：表示区域内SPF路由计算调试信息开关。

【描述】

**[debugging ospfv3 route**]命令用来打开SPF路由计算调试信息开关。**undo debugging ospfv3 route**命令用来关闭SPF路由计算调试信息开关。

缺省情况下，SPF路由计算调试信息开关处于关闭状态。

如果未指定进程号，则打开所有OSPFv3进程的SPF路由计算调试信息开关。

表1-15 debugging ospfv3 spf命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

Area *area-id*

区域ID

OSPFv3 *process-id* Schedule event: *sch-event* at *time-stamp* ms.

OSPFv3进程计算调度

·*sch-event*：调度类型

·*time-stamp*：时间戳

OSPFv3 *process-id* Schedule flag : *sch-flag* SPF is scheduled.

OSPFv3进程计算调度

·*sch-flag*：调度标记

OSPFv3 *process-id* Schedule event: *sch-event* SPF is stopped, at *time-stamp* ms

OSPFv3进程计算调度停止

·*sch-event*：调度类型

·*time-stamp*：时间戳

OSPFv3 *process-id* Pre flag : Schedule: *sch-flag*.

OSPFv3进程计算前次调度标记

·*sch-flag*：调度标记

OSPFv3 *process-id* Now flag : Running : *sch-flag*.

OSPFv3进程计算当前调度标记

·*sch-flag*：调度标记

OSPFv3 *process-id* \*\*\*\* Rebuilding Spf Tree for Area *area-id*, at *time-stamp* ms. \*\*\*\*

OSPFv3进程重新构造区域的SPF树

·*time-stamp*：时间戳

OSPFv3 *process-id* SPF Full Schedule

OSPFv3进程FULL计算调度

OSPFv3 *process-id* SPF route calculation is running, it have to be stopped

停止OSPFv3进程FULL路由计算

OSPFv3 *process-id* SPF running stop for inactive process state

停止OSPFv3进程SPF计算，进程状态无效

OSPFv3 *process-id* SPF Initial running flag

初始化OSPFv3进程运行标记

OSPFv3 *process-id* SPF Stop Schedule for process reset

停止OSPFv3进程SPF计算，进程重置

OSPFv3 *process-id* SPF building SPT begins at *time-stamp* ms

OSPFv3进程开始构造SPF树

·*time-stamp*：时间戳

OSPFv3 *process-id* SPF building SPT ends at *time-stamp* ms

OSPFv3进程结束构造SPF树

·*time-stamp*：时间戳

OSPFv3 *process-id* Router route calculation begins at *time-stamp* ms

OSPFv3进程开始路由计算

·*time-stamp*：时间戳

OSPFv3 *process-id* Router route calculation ends at *time-stamp* ms

OSPFv3进程结束路由计算

·*time-stamp*：时间戳

OSPFv3 *process-id* ASBR route calculation begins at *time-stamp* ms

OSPFv3进程开始ASBR计算

·*time-stamp*：时间戳

OSPFv3 *process-id* ASBR route calculation ends at *time-stamp* ms

OSPFv3进程结束ASBR计算

·*time-stamp*：时间戳

OSPFv3 *process-id* Internal route calculation begins at *time-stamp* ms

OSPFv3进程开始域内路由计算

·*time-stamp*：时间戳

OSPFv3 *process-id* Internal route calculation ends at *time-stamp* ms

OSPFv3进程结束域内路由计算

·*time-stamp*：时间戳

OSPFv3 *process-id* External route calculation begins at *time-stamp* ms

OSPFv3进程开始域外路由计算

·*time-stamp*：时间戳

OSPFv3 *process-id* External route calculation ends at *time-stamp* ms

OSPFv3进程结束域外路由计算

·*time-stamp*：时间戳

OSPFv3 *process-id* \*\*\*\* SPF starts(incremental internal routes)\*\*\*\*

OSPFv3进程开始域内增量路由计算

OSPFv3 *process-id* \*\*\*\* SPF ends(incremental internal routes)\*\*\*\*

OSPFv3进程结束域内增量路由计算

OSPFv3 *process-id* \*\*\*\* SPF starts(incremental external routes)\*\*\*\*

OSPFv3进程开始域外增量路由计算

OSPFv3 *process-id* \*\*\*\* SPF ends(incremental external routes)\*\*\*\*

OSPFv3进程结束域外增量路由计算

OSPFv3 *process-id* \*\*\*\* SPF starts(full internal routes)\*\*\*\*

OSPFv3进程开始域内完全路由计算

OSPFv3 *process-id* \*\*\*\* SPF ends(full internal routes)\*\*\*\*\*

OSPFv3进程结束域内完全路由计算

OSPFv3 *process-id* \*\*\*\* SPF starts(full external routes)\*\*\*\*

OSPFv3进程开始域外完全路由计算

OSPFv3 *process-id* \*\*\*\* SPF ends(full external routes)\*\*\*\*

OSPFv3进程结束域外完全路由计算

OSPFv3 *process-id* Add root to candidate list of area *area-id*

OSPFv3进程为区域候选列表添加根节点

OSPFv3 *process-id* Candidate list empty, SPF area *area-id* finished.

OSPFv3进程候选列表为空，SPF计算结束

OSPFv3 *process-id* SPF node *spf-node*, Type:*node-type*, Advertising source:*router-id*, LS ID:*ls-id*

OSPFv3进程添加SPF节点

·*spf-node*：SPF节点号

·*router-id*：发布源路由器ID

·*ls-id*：链路状态ID

OSPFv3 *process-id* SPF link *spf-link*, Type:*link-type*, Advertising source: *router-id*,, LS ID: *ls-id*

OSPFv3进程添加SPF Link

·*spf-link*：SPFLink号

·*router-id*：发布源路由器ID

·*ls-id*：链路状态ID

OSPFv3 *process-id* SPF calculating route to ASBR, Destination ID *router-id*

OSPFv3进程计算ASBR路由

·*router-id*：目的路由器ID

OSPFv3 *process-id* Del Asbr route,because *value*

OSPFv3进程删除ASBR路由

·*value*：原因码

OSPFv3 *process-id* Incremental ASBR routes calculation begins

OSPFv3进程开始增量ASBR路由计算

OSPFv3 *process-id* Incremental ASBR routes calculation ends

OSPFv3进程结束增量ASBR路由计算

OSPFv3 *process-id* Delete old route. Outgoing interface: *interface-id*, Nexthop: *next-hop*

OSPFv3进程删除路由

·*interface-id*：接口ID

·*next-hop*：下一跳

OSPFv3 *process-id* Cannot find valid nexthop for current advertising source.

OSPFv3进程找不到有效下一跳

OSPFv3 *process-id* No advertising sourc

OSPFv3进程无发布源

OSPFv3 *process-id* Don\'t calculate for active internal route.

OSPFv3进程不计算域内路由

OSPFv3 *process-id* Add new route. Outgoing interface:*interface-id*, Nexthop:*next-hop*

OSPFv3进程下发路由

·*interface-id*：接口ID

·*next-hop*：下一跳

OSPFv3 *process-id* Update old route. Outgoing interface: *interface-id*, Nexthop: *next-hop*

OSPFv3进程更新路由

·*interface-id*：接口ID

·*next-hop*：下一跳

OSPF *process-id* Fail to add route to RM rib

OSPFv3进程下发路由失败

【举例】

\# Router A通过GigabitEthernet1/0/2（1001::1/64）与Router B的GigabitEthernet1/0/1（1001::2/64）相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域1，在GigabitEthernet1/0/2上使能OSPFv3功能并配置其属于区域1；在Router B上创建OSPFv3进程1，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域1。在Router A上打开路由计算概要调试信息开关。

\<RouterA\> debugging ospfv3 spf brief

\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Schedule event: 0x00000001 at 69879924 ms.

\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Schedule flag : 0x00000001 SPF is scheduled.

\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 SPF Full Schedule

*[// OSPFv3*]*进程FULL计算调度*

\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 SPF route calculation is running, it have to be stopped

\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Schedule event: 0x00000000 SPF is stopped, at 69879924 ms

*// 停止OSPFv3进程FULL路由计算*

\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Schedule event: 0x00000020 at 69879924 ms.

\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Schedule flag : 0x00000020 SPF is scheduled.

\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Schedule event: 0x00000001 at 69879925 ms.

\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 SPF Full Schedule

*[// OSPFv3*]*进程FULL计算调度*

\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 SPF route calculation is running, it have to be stopped

\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Schedule event: 0x000000A7 SPF is stopped, at 69879925 ms

*// 停止OSPFv3进程FULL路由计算*

\...\...

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 SPF Initial running flag

*// 初始化OSPFv3进程运行标记*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Pre flag : Schedule: 0x00000000.

*[// OSPFv3*]*进程计算前次调度标记*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Now flag : Running : 0x000000A7.

*[// OSPFv3*]*进程计算当前调度标记*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 SPF building SPT begins at 69888240 ms

*[// OSPFv3*]*进程开始构造SPF树*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 \*\*\*\* Rebuilding Spf Tree for Area 0.0.0.1, at 69888240 ms. \*\*\*\*

*[// OSPFv3*]*进程重新构造区域的SPF树*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 SPF building SPT ends at 69888240 ms

*[// OSPFv3*]*进程结束构造SPF树*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Router route calculation begins at 69888240 ms

*[// OSPFv3*]*进程开始路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Router route calculation ends at 69888240 ms

*[// OSPFv3*]*进程结束路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 ASBR route calculation begins at 69888240 ms

*[// OSPFv3*]*进程开始ASBR计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 ASBR route calculation ends at 69888240 ms

*[// OSPFv3*]*进程结束ASBR计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Internal route calculation begins at 69888240 ms

*[// OSPFv3*]*进程开始域内路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 \*\*\*\* SPF starts(full internal routes)\*\*\*\*

*[// OSPFv3*]*进程开始域内完全路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 \*\*\*\* SPF ends(full internal routes)\*\*\*\*\*

*[// OSPFv3*]*进程结束域内完全路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 Internal route calculation ends at 69888240 ms

*[// OSPFv3*]*进程结束域内路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 External route calculation begins at 69888240 ms

*[// OSPFv3*]*进程开始域外路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 \*\*\*\* SPF starts(full external routes)\*\*\*\*

*[// OSPFv3*]*进程开始域外完全路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 \*\*\*\* SPF ends(full external routes)\*\*\*\*

*[// OSPFv3*]*进程结束域外完全路由计算*

\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

  OSPFv3 1 External route calculation ends at 69888240 ms

*[// OSPFv3*]*进程结束域外路由计算*

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 timer**

------------------------------------------------------------------------

【命令】

**[debugging** **ospfv3** [ *process-id*  **timer** [ **lsa-generate** \| **spf** ]]]

**[undo debugging ospfv3 **[ *process-id*  **timer** [ **lsa-generate** \| **spf** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[lsa-generate**]：表示LSA生成定时器调试信息开关。

**[spf**]：表示SPF计算定时器调试信息开关。

【描述】

**[debugging ospfv3 timer**]命令用来打开OSPFv3定时器调试信息开关。**undo debugging ospfv3 timer**命令用来关闭OSPFv3定时器调试信息开关。

缺省情况下，OSPFv3定时器调试信息开关处于关闭状态。

如果未指定进程号，则打开所有OSPFv3进程的定时器调试信息开关。

表1-16 debugging ospfv3 timer lsa-generate命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

Create LS timer, timeout value is *x* ms

创建LSA生成定时器，超时时间*x*毫秒

Delete LS timer

删除LSA生成定时器

Restart LS timer

启动LSA生成定时器

表1-17 debugging ospfv3 timer spf命令输出信息描述表

字段

描述

OSPFv3 *process-id*

OSPFv3进程号

Create SPF timer, timeout value is *x* ms

创建SPF计算定时器，超时时间*x*毫秒

Delete SPF timer

删除SPF计算定时器

Restart SPF timer

启动SPF计算定时器

【举例】

\# Router A通过GigabitEthernet1/0/1与Router B的GigabitEthernet1/0/1相连，网络类型为Broadcast，在Router A上创建OSPFv3进程1，在OSPFv3进程1中创建区域0，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域0；在Router B上创建OSPFv3进程1，在GigabitEthernet1/0/1上使能OSPFv3功能并配置其属于区域0；在Router A上打开OSPFv3定时器调试信息开关并重启OSPFv3进程1。

\<RouterA\> debugging ospfv3 timer

\*Sep  5 20:44:36:990 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

OSPFv3 1 Delete SPF timer

*// 删除SPF计算定时器*

\*Sep  5 20:44:36:991 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

OSPFv3 1 Create SPF timer,timeout value is 5000 ms

*// 创建SPF计算定时器*

\*Sep  6 20:33:42:647 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

OSPFv3 1 Restart SPF timer

*// 重置SPF计算定时器*

\*Sep  5 07:33:36:990 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

OSPFv3 1 Delete LS timer

*// 删除LSA生成定时器*

\*Sep  6 07:34:40:647 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

OSPFv3 1 Create LS timer,timeout value is 5000 ms

*// 创建LSA生成定时器，超时时间5000毫秒*

\*Sep  6 07:35:41:449 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;

OSPFv3 1 Restart LS timer

*// 重置LSA生成定时器*

