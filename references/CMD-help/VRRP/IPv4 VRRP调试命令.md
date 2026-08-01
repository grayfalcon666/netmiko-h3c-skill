<!-- CMD-INDEX
  debugging vrrp error                | 用户视图             | L12
  debugging vrrp event                | 用户视图             | L68
  debugging vrrp packet               | 用户视图             | L298
  debugging vrrp fsm                  | 用户视图             | L454
  debugging vrrp ipv6 error           | 用户视图             | L630
  debugging vrrp ipv6 event           | 用户视图             | L704
  debugging vrrp ipv6 packet          | 用户视图             | L944
  debugging vrrp ipv6 fsm             | 用户视图             | L1100
-->

**VRRP \-- IPv4 VRRP调试命令 \-- debugging vrrp error**

------------------------------------------------------------------------

【命令】

**[debugging vrrp error**]

**[undo debugging vrrp error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging vrrp error**]命令用来打开IPv4 VRRP的错误调试信息开关。**undo debugging vrrp error**命令用来关闭IPv4 VRRP的错误调试信息开关。

缺省情况下，IPv4 VRRP的错误调试信息开关处于关闭状态。

表1-1 debugging vrrp error命令输出信息描述表

字段

描述

The VRID *vrid* in the packet from *ip-address* does not exist on interface *interface-name*

收到报文中的VRID对应备份组在本地不存在

The VRRP packet is illegal

VRRP报文为非法报文

The VF ID is illegal

非法VFID号

【举例】

\# 打开IPv4 VRRP的错误调试信息开关。

\<Sysname\> debugging vrrp error

\*Apr 27 21:55:24:781 2010 Sysname VRRP4/7/Error:

The VRRP packet is illegal

*// 收到非法的VRRP报文*

**VRRP \-- IPv4 VRRP调试命令 \-- debugging vrrp event**

------------------------------------------------------------------------

【命令】

**[debugging vrrp event**]

**[undo debugging vrrp event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging vrrp event**]命令用来打开IPv4 VRRP的事件调试信息开关。**undo debugging vrrp event**命令用来关闭IPv4 VRRP的事件调试信息开关。

缺省情况下，IPv4 VRRP的事件调试信息开关处于关闭状态。

表1-2 debugging vrrp event命令输出信息描述表

字段

描述

Created track object *track-entry-number*

创建Track对象，*track-entry-number*为Track项序号

Deleted track object *track-entry-number*

删除Track对象，*track-entry-number*为Track项序号

Status of track object *track-entry-number* changed to *state*

IPv4 VRRP的备份组监视的Track对象状态转为*state*，状态取值包括：

·positive

·negative

·notready

[[IPv4 *interface-name* \| Forwarder *vrid*.*vfid*  : *event*]]

接口*interface-name*下，IPv4 VRRP的备份组*vrid*中的虚拟转发器*vfid*发生事件*event*，事件包括：

·Active timer created：创建Active定时器

·VF instance created：创建VF实例

·VF instance deleted：删除VF实例

·Active timer deleted：删除Active定时器

·Offer timer created：创建Offer定时器

·Offer timer deleted：删除Offer定时器

·Offer timer expired：Offer定时器超时

·Redirect timer expired：Redirect定时器超时

·Time-out timer expired：Time-out定时器超时

·Forward information updated：更新转发信息

·Forward information deleted：删除转发信息

·Virtual MAC *mac-address* added：添加虚拟MAC地址*mac-address*

·Virtual MAC *mac-address* deleted：删除虚拟MAC地址*mac-address*

No virtual MAC address available

已经没有可用的虚拟MAC地址

[[IPv4 *interface-name* \| Virtual Router *vrid* : *event*]]

接口*interface-name*下，IPv4 VRRP的备份组*vrid*发生事件*event*，事件包括：

·Adver timer created：创建Adver定时器

·Adver timer deleted：删除Adver定时器

·Hold timer created：创建Hold定时器

·Hold timer deleted：删除Hold定时器

·Hold timer expired：Hold定时器超时

·VF-learning timer created：创建VF-learning定时器

·VF-learning timer deleted：删除VF-learning定时器

·VF-learning timer expired：VF-learning定时器超时

·Request timer created：创建Request定时器

·Request timer deleted：删除Request定时器

·Request timer expired Request定时器超时

【举例】

\# 打开IPv4 VRRP的事件调试信息开关。

\<Sysname\> debugging vrrp event

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IP地址为3.1.1.3。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 3.1.1.3

\*Oct 15 11:48:43:969 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer created

*// 创建Hold定时器*

\*Oct 15 11:48:46:219 2010 Sysname VRRP4/7/Event:

 IPv4 Ethernet1/1 \| Virtual Router 1 : Hold timer expired

*[// Hold*]*定时器超时*

\*Oct 15 11:48:46:219 2010 Sysname VRRP4/7/Event:

 IPv4 Ethernet1/1 \| Virtual Router 1 : Hold timer deleted

*// 删除Hold定时器*

\*Oct 15 11:48:46:235 2010 Sysname VRRP4/7/Event:

 IPv4 Ethernet1/1 \| Virtual Router 1 : Adver timer created

*// 创建Adver定时器*

\# VRRP工作在负载均衡模式，打开事件调试信息开关，对设备上所有虚拟备份组的事件进行调试。

\<Sysname\> debugging vrrp event

\# 配置设备工作在VRRP负载均衡模式。

\<Sysname\> system-view

Sysname vrrp mode load-balance

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IP地址为3.1.1.3。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 3.1.1.3

\*Oct 15 13:28:04:797 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer created

*// 创建Hold定时器*

\*Oct 15 13:28:04:813 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Adver timer created

*// 创建Adver定时器*

\*Oct 15 13:28:04:813 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : VF-learning timer created

*// 创建VF-learning定时器*

\*Oct 15 13:28:04:828 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Request timer created

*// 创建Request定时器*

\*Oct 15 13:28:06:313 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : VF-learning timer expired

*[// VF-learning*]*定时器超时*

\*Oct 15 13:28:06:313 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : VF-learning timer deleted

*// 删除VF-learning定时器*

\*Oct 15 13:28:07:78 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer expired

*[// Hold*]*定时器超时*

\*Oct 15 13:28:07:94 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer deleted

*// 删除Hold定时器*

\*Oct 15 13:28:07:110 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Request timer deleted

*// 删除Request定时器*

\*Oct 15 13:28:07:110 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Forwarder 1.1 : VF instance created

*// 创建VF实例*

\*Oct 15 13:28:07:110 2010 Sysname VRRP4/7/Event:

 IPv4 GigabitEthernet1/0/1 \| Forwarder 1.1 : Forward information updated

*// 更新备份组转发信息*

**VRRP \-- IPv4 VRRP调试命令 \-- debugging vrrp packet**

------------------------------------------------------------------------

【命令】

**[debugging vrrp packet** [ **interface** *interface-type interface-number* [ **vrid** *virtual-router-id*  ]]]

**[undo debugging vrrp packet** [ **interface** *interface-type interface-number* [ **vrid** *virtual-router-id*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：表示指定接口的报文调试信息开关。其中，*interface-type interface-number*分别为接口类型和接口编号。

**[vrid** *virtual-router-id*]：表示接口下指定备份组的报文调试信息开关。*virtual-router-id*为备份组号，取值范围1～255。

【描述】

**[debugging vrrp packet**]命令用来打开IPv4 VRRP的报文调试信息开关。**undo debugging vrrp packet**命令用来关闭IPv4 VRRP的报文调试信息开关。

缺省情况下，IPv4 VRRP的报文调试信息开关处于关闭状态。

关闭全局报文调试信息开关并不会关闭具体接口或备份组的报文调试信息开关。当全局报文调试开关、接口下报文调试开关或备份组报文调试开关中有一个处于开启状态，接口或者备份组就会输出调试信息。

表1-3 debugging vrrp packet命令输出信息描述表

字段

描述

Sent *message-type* message from *interface-number*

从接口*interface-number*发送*message-type*类型的报文，报文类型包括Advertisement、Request、Reply和Release

Received *message-type* message from *ip-address* on *interface-number*

在接口*interface-number*上接收到来自*ip-address*的报文，报文类型为*message-type*，取值包括Advertisement、Request、Reply和Release

VRID

备份组号

Pri

发送VRRP报文的路由器在备份组中的优先级或虚拟转发器的优先级

Adver timer

VRRP备份组通告VRRP报文的时间间隔，单位为厘秒

Weight

备份组中虚拟转发器的权重

VMAC

由VRRP备份组中Master分配的虚拟MAC

Forwarder *number*

虚拟转发器*number*的信息

Owner ID

虚拟转发器拥有者的接口MAC地址

MAC

发送VRRP报文的接口MAC地址

Timer

VRRP备份组中Redirect timer/Timeout timer的剩余时间，单位为秒

IP

发送VRRP报文的接口IP地址

【举例】

\# VRRP工作在标准协议模式，打开报文调试信息开关，输出设备上所有备份组的报文收发信息。

\<Sysname\> debugging vrrp packet

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IP地址为3.1.1.3，路由器的优先级为缺省值100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 3.1.1.3

\*Oct 15 11:24:00:172 2010 Sysname VRRP4/7/Packet:

 Sent Advertisement message from Ethernet1/1

 VRID: 1  Pri: 100  Adver timer: 100 centisecs

*// 从接口GigabitEthernet1/0/1发送Advertisement报文，VRID为1，路由器在备份组中的优先级为100，通告VRRP报文的发送时间间隔为1秒*

\# VRRP工作在负载均衡模式，打开报文调试信息开关，输出设备上所有备份组的报文收发信息。

\<Sysname\> debugging vrrp packet

\# 配置VRRP工作在负载均衡模式。

\<Sysname\> system-view

Sysname vrrp mode load-balance

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IP地址为3.1.1.3。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 3.1.1.3

\*Oct 15 13:15:28:906 2010 Sysname VRRP4/7/Packet:

 Sent Request message from GigabitEthernet1/0/1

 VRID: 1  MAC: 0000-5e01-1101  IP: 3.1.1.1

*// 从接口GigabitEthernet1/0/1发送Request报文，接口MAC地址为0000-5e01-1101，接口IP地址为3.1.1.1*

\*Oct 15 13:15:31:188 2010 Sysname VRRP4/7/Packet:

 Sent Advertisement message from GigabitEthernet1/0/1

 VRID: 1  Pri: 100  Adver timer: 100 centisecs

*// 从接口GigabitEthernet1/0/1发送Advertisement报文，VRID为1，路由器在备份组中的优先级为100，通告VRRP报文的发送时间间隔为1秒*

\*Oct 15 13:15:31:188 2010 Sysname VRRP4/7/Packet:

 Sent Advertisement message from GigabitEthernet1/0/1

 VRID: 1  Pri: 100  Adver timer: 100 centisecs

 Weight: 255

 Forwarder 1:

 Pri: 255  Timer: 600/1800 secs  Owner ID: 0000-5e01-1101

*// 从接口GigabitEthernet1/0/1发送Advertisement报文，VRID为1，路由器在备份组中的优先级为100，通告VRRP报文的发送时间间隔为1秒；虚拟转发器的权重为255，路由器上存在一个虚拟转发器，转发器优先级为255，Redirect timer为600秒，Time-out timer为1800秒，虚拟转发器拥有者的接口MAC地址为0000-5e01-1101*

**VRRP \-- IPv4 VRRP调试命令 \-- debugging vrrp fsm**

------------------------------------------------------------------------

【命令】

**[debugging vrrp fsm**]

**[undo debugging vrrp fsm**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging** **vrrp fsm**]命令用来打开IPv4的VRRP状态调试信息开关。**undo** **debugging** **vrrp fsm**命令用来关闭IPv4 VRRP的状态调试信息开关。

缺省情况下，IPv4 VRRP的状态调试信息开关处于关闭状态。

表1-4 debugging vrrp fsm命令输出信息描述表

字段

描述

[[IPv4 *interface-name* \| Virtual Router *vrid* : *state1* \--\> *state2*]]

接口*interface-name*下，IPv4 VRRP的备份组*vrid*从状态*state1*转换到状态*state2*，备份组的状态包括：

·Inactive

·Initialize

·Backup

·Master

[[IPv4 *interface-name* \| Virtual Router *vrid* : *state1* \--\> *state2     * reason: *reason*]]

接口*interface-name*下，IPv4 VRRP的备份组*vrid*从状态*state1*转换到状态*state2*，状态转化原因为*reason*

备份组的状态包括：

·Backup

·Master

状态变化原因包括：

·Master-down-timer expired：定时器超时

·VRRP packet received：收到VRRP报文

·The status of the tracked object changed：监视的Track对象状态改变

·Current device has changed to IP address owner：成为IP地址拥有者

·Zero priority packet received：收到优先级为0的通告报文

·Preempt：抢占成为Master

[[IPv4 *interface-name* ]{.TableTextChar}[\| Forwarder [*vrid*]{.TableTextChar}.*vfid* : *state1 \--\> state2  *    reason: *reason*{.TableTextChar}]]

接口*interface-name*下，IPv4 VRRP的备份组*[vrid*]{.TableTextChar}中的虚拟转发器*vfid*从状态*state1*转换到状态*state2*，状态转化原因为*reason*

虚拟转发器的状态包括：

·Initialize

·Listening

·Active

状态转换原因包括：

·Weight changed：权重改变

·Adding virtual MAC address failed：添加虚拟MAC地址失败

·Conceded：AVF主动放弃转发权限，即接收到虚拟转发器优先级为0的报文

·Learnt from Advertisement：从Advertisement报文中学习

·Reply received：收到reply报文

·Release received：收到release报文

·Active timer expired：Active定时器超时

·Time-out timer expired：Time-out定时器超时

·Self-allocated：master为自己分配虚拟MAC地址

·VRRP down：VRRP协议down

·Take over：3倍的Adver timer时间内没有接收到Advertisement报文，接管AVF的工作

【举例】

\# VRRP工作在标准协议模式，打开IPv4的状态调试信息开关。

\<Sysname\> debugging vrrp fsm

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IP地址为3.1.1.3。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 3.1.1.3

\*Oct 15 11:26:36:891 2010 Sysname VRRP4/7/FSM:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Inactive \--\> Initialize

*// 创建VRRP备份组1后，备份组从Inactive状态转换到Initialize状态*

\*Oct 15 11:26:36:891 2010 Sysname VRRP4/7/FSM:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Initialize \--\> Backup

*[// VRRP*]*备份组1从Initialize状态转换到Backup状态*

\*Oct 15 11:26:39:156 2010 Sysname VRRP4/7/FSM:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Backup \--\> Master   reason: Master-down-timer expired

*[// 3*]*倍的通告报文时间间隔内没有收到Advertisement报文，备份组1从Backup状态转换到 Master状态*

\# VRRP工作在负载均衡模式，打开状态调试信息开关，对设备上所有虚拟备份组的状态进行调试。

\<Sysname\> debugging vrrp fsm

\# 配置VRRP工作在负载均衡模式。

\<Sysname\> system-view

Sysname vrrp mode load-balance

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IP地址为3.1.1.3

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 3.1.1.3

\*Oct 15 13:22:54:141 2010 Sysname VRRP4/7/FSM :

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Inactive \--\> Initialize

*// 创建VRRP备份组1后，备份组从Inactive状态转换到Initialize状态*

\*Oct 15 13:22:54:141 2010 Sysname VRRP4/7/FSM:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Initialize \--\> Backup

*[// VRRP*]*备份组1从Initialize状态转换到Backup状态*

\*Oct 15 13:22:56:360 2010 Sysname VRRP4/7/FSM:

 IPv4 GigabitEthernet1/0/1 \| Virtual Router 1 : Backup \--\> Master   reason: Master-down-timer expired

*[// 3*]*倍的通告报文时间间隔内没有收到Advertisement报文，备份组1从Backup状态转换到 Master状态*

\*Oct 15 13:22:56:375 2010 Sysname VRRP4/7/FSM:

 IPv4 GigabitEthernet1/0/1 \| Forwarder 1.1 : Initialize \--\> Active  reason: Self-allocated

*// 路由器作为备份组1的Master为自己分配虚拟MAC地址，路由器上创建虚拟转发器1，该虚拟转发器从Initialize状态转换为Active状态*

**VRRP \-- IPv6 VRRP调试命令 \-- debugging vrrp ipv6 error**

------------------------------------------------------------------------

【命令】

**[debugging vrrp ipv6 error**]

**[undo debugging vrrp ipv6 error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging vrrp ipv6 error**]命令用来打开IPv6 VRRP的错误调试信息开关。**undo debugging vrrp ipv6 error**命令用来关闭IPv6 VRRP的错误调试信息开关。

缺省情况下，IPv6 VRRP的错误调试信息开关处于关闭状态。

表1-5 debugging vrrp ipv6 error命令输出信息描述表

字段

描述

The VRID *vrid* in the packet from *ipv6-address* does not exist on interface *interface-name*

收到报文中的VRID对应备份组在本地不存在

The VRRP packet is illegal

VRRP报文为非法报文

The VF ID is illegal

非法VFID号

【举例】

\# VRRP工作在标准模式，打开VRRP的错误调试信息开关。

\<Sysname\> debugging vrrp ipv6 error

\*Apr 27 21:56:57:300 2010 Sysname VRRP6/7/Error:

The VRRP Packet is illegal

*// 收到非法的VRRP报文*

\# VRRP工作在负载均衡模式，打开错误调试信息开关，对设备上所有虚拟备份组的错误进行调试。

\<Sysname\> terminal monitor

\<Sysname\> debugging vrrp ipv6 error

\# 配置设备工作在VRRP负载均衡模式。

\<Sysname\> system－view

Sysname vrrp mode load-balance

\*Apr 27 21:56:57:300 2010 Sysname VRRP6/7/Error:

The VRRP Packet is illegal

*// 收到非法的VRRP报文*

**VRRP \-- IPv6 VRRP调试命令 \-- debugging vrrp ipv6 event**

------------------------------------------------------------------------

【命令】

**[debugging vrrp ipv6 event**]

**[undo debugging vrrp ipv6 event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging vrrp ipv6 event**]命令用来打开IPv6 VRRP的事件调试信息开关。**undo debugging vrrp ipv6 event**命令用来关闭IPv6 VRRP的事件调试信息开关。

缺省情况下，IPv6 VRRP的事件调试信息开关处于关闭状态。

表1-6 debugging vrrp ipv6 event命令输出信息描述表

字段

描述

Created track object *track-entry-number*

创建Track对象，*track-entry-number*为Track项序号

Deleted track object *track-entry-number*

删除Track对象，*track-entry-number*为Track项序号

Status of VRRP IPv6 track object *track-entry-number* changed to *state*

IPv6 VRRP的备份组监视的Track对象的状态转为*state*，状态取值包括：

·positive

·negative

·notready

[[IPv6 *interface-name* \| Forwarder *vrid.vfid*  : *event*]]

接口*interface-name*下，IPv6 VRRP的备份组*vrid*中的虚拟转发器*vfid*发生事件*event*，事件包括：

·Active timer created：创建Active定时器

·VF instance created：创建VF实例

·VF instance deleted：删除VF实例

·Active timer deleted：删除Active定时器

·Offer timer created：创建Offer定时器

·Offer timer deleted：删除Offer定时器

·Offer timer expired：Offer定时器超时

·Redirect timer expired：Redirect定时器超时

·Time-out timer expired：Time-out定时器超时

·Forward information updated：更新转发信息

·Forward information deleted：删除转发信息

·Virtual MAC *mac-address* added：添加虚拟MAC地址*mac-address*

·Virtual MAC *mac-address* deleted：删除虚拟MAC地址*mac-address*

[[IPv6 *interface-name* \| Virtual Router *vrid* : *event*]]

接口*interface-name*下，IPv6 VRRP的备份组*vrid*发生事件*event*，事件包括：

·Adver timer created：创建Adver定时器

·Adver timer deleted：删除Adver定时器

·Hold timer created：创建Hold定时器

·Hold timer deleted：删除Hold定时器

·Hold timer expired：Hold定时器超时

·VF-learning timer created：创建VF-learning定时器

·VF-learning timer deleted：删除VF-learning定时器

·VF-learning timer expired：VF-learning定时器超时

·Request timer created：创建Request定时器

·Request timer deleted：删除Request定时器

·Request timer expired：Request定时器超时

Send unsolicited ND

IPv6发送无请求ND报文

No virtual MAC address available

没有可用的虚拟MAC地址

【举例】

\# VRRP工作在标准模式，打开基于IPv6的事件调试信息开关。

\<Sysname\> debugging vrrp ipv6 event

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IPv6地址为fe80::10。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local

\*Oct 15 13:12:08:94 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer created

*// 创建Hold定时器*

\*Oct 15 13:12:10:313 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer expired

*[// Hold*]*定时器超时*

\*Oct 15 13:12:10:313 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer deleted

*// 删除Hold定时器*

\*Oct 15 13:12:10:313 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Adver timer created

*// 创建Adver定时器*

\*Oct 15 13:12:10:328 2010 Sysname VRRP6/7/Event:

 Send unsolicited ND.

*[// IPv6*]*发送无请求ND报文*

\# VRRP工作在负载均衡模式，打开状态调试信息开关，对设备上所有虚拟备份组的状态进行调试

\<Sysname\> debugging vrrp ipv6 event

\# 配置VRRP工作在负载均衡模式。

\<Sysname\> system-view

Sysname vrrp mode load-balance

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IPv6地址为fe80::10

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local

\*Oct 15 13:43:40:719 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer created

*// 创建Hold定时器*

\*Oct 15 13:43:40:719 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Adver timer created

*// 创建Adver定时器*

\*Oct 15 13:43:40:735 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : VF-learning timer created

*// 创建VF-learning定时器*

\*Oct 15 13:43:40:735 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Request timer created

*// 创建Request定时器*

\*Oct 15 13:43:42:188 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : VF-learning timer expired

*[// VF-learning*]*定时器超时*

\*Oct 15 13:43:42:203 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : VF-learning timer deleted

*// 删除VF-learning定时器*

\*Oct 15 13:43:42:985 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer expired

*[// Hold*]*定时器超时*

\*Oct 15 13:43:42:985 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Hold timer deleted

*// 删除Hold定时器*

\*Oct 15 13:43:43:00 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Request timer deleted

*// 删除Request定时器*

\*Oct 15 13:43:43:00 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Forwarder 1.1 : VF instance created

*// 创建VF实例*

\*Oct 15 13:43:43:16 2010 Sysname VRRP6/7/Event:

 IPv6 GigabitEthernet1/0/1 \| Forwarder 1.1 : Forward information updated

*// 更新备份组转发信息*

**VRRP \-- IPv6 VRRP调试命令 \-- debugging vrrp ipv6 packet**

------------------------------------------------------------------------

【命令】

**[debugging vrrp ipv6 packet** [ **interface** *interface-type interface-number* [ **vrid** *virtual-router-id*  ]]]

**[undo debugging vrrp ipv6 packet** [ **interface** *interface-type interface-number* [ **vrid** *virtual-router-id*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：表示指定接口的报文调试信息开关。其中，*interface-type interface-number*为接口类型和接口编号。

**[vrid** *virtual-router-id*]：表示接口下指定备份组的报文调试信息开关。*virtual-router-id*为备份组号，取值范围1～255。

【描述】

**[debugging vrrp ipv6 packet**]命令用来打开IPv6 VRRP的报文调试信息开关。**undo debugging vrrp ipv6 packet**命令用来关闭IPv6 VRRP的报文调试信息开关。

缺省情况下，IPv6 VRRP的报文调试信息开关处于关闭状态。

关闭全局报文调试信息开关并不会关闭具体接口或备份组的报文调试信息开关。当全局报文调试开关、接口下报文调试开关或备份组报文调试开关中有一个处于开启状态，接口或者备份组就会输出调试信息。

表1-7 debugging vrrp ipv6 packet命令输出信息描述表

字段

描述

Sent *message-type* message from *interface-number*

从接口*interface-number*发送*message-type*类型的报文，报文类型包括Advertisement、Request、Reply和Release

Received *message-type* message from *ip-address* on *interface-number*

在接口*interface-number*上接收到来自*ip-address*的报文，报文类型为*message-type*，取值包括Advertisement、Request、Reply和Release

VRID

备份组号

Pri

发送VRRP报文的路由器在虚拟备份组中的优先级或虚拟转发器的优先级

Adver timer

VRRP备份组通告VRRP报文的定时器间隔，单位为厘秒

Weight

VRRP备份组中活动路由器的权重

VMAC

由VRRP备份组中Master分配的虚拟MAC

Forwarder

VRRP备份组中虚拟转发器的信息

Owner ID

虚拟转发器拥有者的接口MAC地址

Timer

VRRP备份组中Redirect timer/Timeout timer的剩余时间，单位为秒

MAC

发送VRRP报文的接口MAC地址

IP

发送VRRP报文的接口IP地址

【举例】

\# VRRP工作在标准协议模式，打开基于IPv6的报文调试信息开关，输出设备上所有虚拟备份组的报文收发信息。

\<Sysname\> debugging vrrp ipv6 packet

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IPv6地址为FE80::1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip fe80::1 link-local

\*Oct 15 11:54:08:828 2010 Sysname VRRP6/7/Packet:

 Sent Advertisement message from Ethernet1/1

 VRID: 1  Pri: 255  Adver timer: 100 centisecs

*// 从接口GigabitEthernet1/0/1发送Advertisement报文，VRID为1，路由器在备份组中的优先级为255，Advertisement报文的发送时间间隔为1*秒*

\# VRRP工作在负载均衡模式，打开基于IPv6的报文调试信息开关，输出设备上所有虚拟备份组的报文收发信息。

\<Sysname\> debugging vrrp ipv6 packet

\# 配置VRRP工作在负载均衡模式。

\<Sysname\> system-view

Sysname vrrp mode load-balance

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IPv6地址为fe80::10。

Sysname interface GigabitEthernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local

\*Oct 15 13:35:38:344 2010 Sysname VRRP6/7/Packet:

 Sent Request message from Ethernet1/1

 VRID: 1  MAC: 0000-5e01-1101  IP: FE80::1

*// 从接口GigabitEthernet1/0/1发送Request报文，接口MAC地址为0000-5e01-1101，接口IP地址为FE80::1*

\*Oct 15 13:35:40:719 2010 Sysname VRRP6/7/Packet:

 Sent Advertisement message from GigabitEthernet1/0/1

 VRID: 1  Pri: 100  Adver timer: 100 centisecs

*// 从接口GigabitEthernet1/0/1发送Advertisement报文，VRID为1，路由器在备份组中的优先级为100，Advertisement报文的发送时间间隔为1秒*

\*Oct 15 13:35:40:719 2010 Sysname VRRP6/7/Packet:

 Sent Advertisement message from GigabitEthernet1/0/1

 VRID: 1  Pri: 100  Adver timer: 100 centisecs

 Weight: 255

 Forwarder 1:

 Pri: 255  Timer: 600/1800 secs  Owner ID: 0000-5e01-1101

*// 从接口GigabitEthernet1/0/1发送Advertisement报文，VRID为1，路由器在备份组中的优先级为100，Advertisement报文的发送时间间隔为1秒；虚拟转发器的权重为255，路由器上存在一个虚拟转发器，转发器优先级为255，Redirect timer为600秒，Time-out timer为1800秒，虚拟转发器拥有者的接口MAC地址为0000-5e01-1101*

**VRRP \-- IPv6 VRRP调试命令 \-- debugging vrrp ipv6 fsm**

------------------------------------------------------------------------

【命令】

**[debugging vrrp ipv6 fsm**]

**[undo debugging vrrp ipv6 fsm**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging vrrp ipv6 fsm**]命令用来打开IPv6 VRRP的状态调试信息开关。**undo debugging vrrp ipv6 fsm**命令用来关闭IPv6 VRRP的状态调试信息开关。

缺省情况下，IPv6 VRRP的状态调试信息开关处于关闭状态。

表1-8 debugging vrrp ipv6 fsm命令输出信息描述表

字段

描述

[[IPv6 *interface-name* \| Virtual Router *vrid* : *state1* \--\> *state2*]]

接口*interface-name*下，IPv6 VRRP的备份组*vrid*从状态*state1*转换到状态*state2*，备份组的状态包括：

·Inactive

·Initialize

·Backup

·Master

[[IPv6 *interface-name* \| Virtual Router *vrid* : *state1* \--\> *state2     * reason: *reason*]]

接口*interface-name*下，IPv6 VRRP的备份组*vrid*从状态*state1*转换到状态*state2*，状态转化原因为*reason*

备份组的状态包括：

·Backup

·Master

状态变化原因包括：

·Master-down-timer expired：定时器超时

·VRRP packet received：收到VRRP报文

·The status of the tracked object changed：监视的Track对象状态改变

·Current device has changed to IP address owner：成为IP地址拥有者

·Zero priority packet received：收到优先级为0的通告报文

·Preempt：抢占成为Master

[[IPv6 *interface-name* ]{.TableTextChar}[\| Forwarder [*vrid*]{.TableTextChar}.*vfid* : *state1 \--\> state2  *    reason: *reason*{.TableTextChar}]]

接口*interface-name*下，IPv6 VRRP的备份组*[vrid*]{.TableTextChar}中的虚拟转发器*vfid*从状态*state1*转换到状态*state2*，状态转化原因为*reason*

虚拟转发器的状态包括：

·Initialize

·Listening

·Active

状态转换原因包括：

·Weight changed：权重改变

·Adding virtual MAC address failed：添加虚拟MAC地址失败

·Conceded：AVF主动放弃转发权限，即接收到虚拟转发器优先级为0的报文

·Learnt from Advertisement：从Advertisement报文中学习

·Reply received：收到reply报文

·Release received：收到release报文

·Active timer expired：Active定时器超时

·Time-out timer expired：Time-out定时器超时

·Self-allocated：master为自己分配虚拟MAC地址

·VRRP down：VRRP协议down

·Take over：3倍的Adver timer时间内没有接收到Advertisement报文，接管AVF的工作

【举例】

\# 设备工作在VRRP标准协议模式，打开基于IPV6 VRRP协议的状态调试信息开关。

\<Sysname\> debugging vrrp ipv6 fsm

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IPv6地址为FE80::10。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local

\*Oct 15 13:09:19:781 2010 Sysname VRRP6/7/FSM:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Inactive \--\> Initialize

*// 创建VRRP备份组1后，备份组从Created状态转换到Initialize状态*

\*Oct 15 13:09:19:781 2010 Sysname VRRP6/7/FSM:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Initialize \--\> Backup

*[// VRRP*]*备份组1从Initialize状态转换到Backup状态*

\*Oct 15 13:09:22:16 2010 Sysname VRRP6/7/FSM:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Backup \--\> Master   reason: Master-down-timer expired

*[// 3*]*倍的通告报文时间间隔内没有收到Advertisement报文，备份组1从Backup状态转换到 Master状态*

\# VRRP工作在负载均衡模式，打开基于IPv6的状态调试信息开关，对设备上所有虚拟备份组的状态进行调试。

\<Sysname\> debugging vrrp ipv6 fsm

\# 配置VRRP工作在负载均衡模式。

\<Sysname\> system-view

Sysname vrrp mode load-balance

\# 在接口GigabitEthernet1/0/1下配置虚拟备份组1，虚拟IPv6地址为FE80::10。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local

\*Oct 15 13:40:40:125 2010 Sysname VRRP6/7/FSM:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Created \--\> Initialize

*// 创建VRRP备份组1后，备份组从Created状态转换到Initialize状态*

\*Oct 15 13:40:40:141 2010 Sysname VRRP6/7/FSM:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Initialize \--\> Backup

*[// VRRP*]*备份组1从Initialize状态转换到Backup状态*

\*Oct 15 13:40:42:375 2010 Sysname VRRP6/7/FSM:

 IPv6 GigabitEthernet1/0/1 \| Virtual Router 1 : Backup \--\> Master   reason: Master-down-timer expired

*[// 3*]*倍的通告报文时间间隔内没有收到Advertisement报文，备份组1从Backup状态转换到 Master状态*

\*Oct 15 13:40:42:375 2010 Sysname VRRP6/7/FSM:

 IPv6 GigabitEthernet1/0/1 \| Forwarder 1.1 : Initialize \--\> Active  reason: Self-allocated

*// 路由器作为备份组1的Master为自己分配虚拟MAC地址，路由器上创建虚拟转发器1，该虚拟转发器从Initialize状态转换为Active状态*
