<!-- CMD-INDEX
  debugging pbb                       | 用户视图             | L5
-->

**PBB \-- PBB调试命令 \-- debugging pbb**

------------------------------------------------------------------------

【命令】

**[debugging pbb **[{ **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging pbb **[{ **all** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示PBB所有调试信息开关。

**[error**]：表示PBB错误调试信息开关。

**[event**]：表示PBB事件调试信息开关。

**[packet**]：表示PBB报文调试信息开关。

【描述】

**[debugging pbb**]命令用来打开PBB调试信息开关。**undo debugging pbb**命令用来关闭PBB调试信息开关。

缺省情况下，PBB的所有调试信息开关处于关闭状态。

表1-1 debugging pbb error命令输出信息描述表

字段

描述

Failed to get VSI block.

获取VSI控制块失败

The interface *interface-name* isn\'t enabled to receive PBB packet.

该VSI的接口*interface-name*没有使能接收PBB报文

The Unicast Pseudo Wire entry has already been learned.

已经学习该单播表项

The number of Unicast Pseudo Wire entries in this VSI (VsiIndex *n*) has reached the upper limit.

已达到VSI索引为*n*的单播PW表项个数的上限

The total number of Unicast Pseudo Wire entries has reached the upper limit.

已达到设备可以学习的最大的单播PW表项个数上限

Failed to learn the Unicast Pseudo Wire entry.

学习单播PW表项失败

The STG state of interface *interface-name* is not forwarding.

接口*interface-name*的STG状态为非转发状态

Failed to add Multicast Pseudo Wire entries to driver.

添加组播PW表项到驱动失败

Failed to add Multicast Pseudo Wire port to driver.

添加组播PW表项中的出端口到驱动失败

Failed to delete Multicast Pseudo Wire entries from driver.

从驱动删除组播PW表项失败

Failed to delete Multicast Pseudo Wire port from driver.

从驱动删除组播PW表项中的出端口失败

Failed to add Unicast Pseudo Wire entries to driver.

添加单播PW表项到驱动失败

Failed to delete Unicast Pseudo Wire entries from driver.

从驱动删除单播PW表项失败

Failed to enable the interface PBB mode.

使能接口PBB模式失败

Failed to disable the interface PBB mode.

关闭接口PBB模式失败

The I-SID of this PBB packet is not the same as configured.

PBB报文的I-SID和配置值不符

The B-VLAN of this PBB packet is not the same as configured.

PBB报文的B-VLAN和配置值不符

Failed to learn PBB packet because the VSI is administratively down.

由于VSI被手工关闭导致学习PBB报文失败

Failed to allocate memory for VLAN map on interface *interface-name.*

为接口*interface-name*上的VLAN位图分配内存失败

Failed to allocate memory for control block on interface *interface-name.*

为接口*interface-name*上的控制块分配内存失败

Failed to set private data on interface *interface-name.*

设置接口*interface-name*上的控制块失败

Failed to allocate memory for Multicast Pseudo Wire entry with VsiIndex *vsi-index*, I-SID *i-sid*, B-VLAN *vlan-id*.

为VSI索引为*vsi-index*，I-SID为*i-sid*，B-VLAN为*vlan-id*的组播表项分配内存失败

Failed to allocate memory for Unicast Pseudo Wire interface control block on interface *interface-name.*

为接口*interface-name*上的单播表项接口控制块分配内存失败

Failed to allocate memory for Unicast Pseudo Wire entry with VsiIndex *vsi-index,* I-SID *i-sid,* B-VLAN *vlan-id*, B-MAC *mac-address* on interface *interface-name.*

为接口*interface-name*上的VSI索引为*vsi-index*，I-SID为*i-sid*，B-VLAN为*vlan-id*，B-MAC为*mac-address*的单播表项分配内存失败

Failed to recognize an invalid TLV. Keep on processing the next one.

识别无效的TLV失败。继续处理下一个TLV

Failed to allocate memory for control block on VSI (VsiIndex *vsi-index*).

为VSI（VSI索引为*vsi-index*）的控制块分配内存失败

Failed to allocate memory for uplink node for VSI (VsiIndex *vsi-index*).

为VSI（VSI索引为*vsi-index*）的上行口节点分配内存失败

Failed to allocate memory for hash node for VSI (VsiIndex *vsi-index*).

为VSI（VSI索引为*vsi-index*）的hash节点分配内存失败

Failed to set ethernet type.

设置报文封装模式失败

表1-2 debugging pbb event命令输出信息描述表

字段

描述

Receive event: *event* on the interface *interface-name*.

接口*interface-name*收到事件*event*。*interface-name*为接口名，*event*为事件类型，取值包括：

·interface\_active：接口激活事件

·interface\_deactive：接口去激活事件

·interface\_delete：接口删除事件

·interface\_up：接口链路UP事件

·interface\_down：接口链路DOWN事件

Receive the event that interface *interface-name1* *event* the aggregate interface *interface-name2*.

收到接口*interface-name1*加入/退出聚合接口*interface-name*2事件。*interface-name1*为接口名，*interface-name2*为聚合接口名，*event*为事件类型，取值包括：

·joinin：接口加入聚合

·leavefrom：接口离开聚合

Receive vsi_add event: VsiIndex *vsiindex*, VsiName *vsiname*, PBB I-SID *pbbisid*, ShutdownFlag *flag*.

收到VSI添加事件，其中：

·*vsiindex*：VSI索引

·*vsiname*：VSI名字

·*pbbisid*：PBB I-SID

·*flag*：VSI是否Down

Receive *event* event: VsiIndex *vsiindex*, VsiName *vsiname*.

收到VSI UP/DOWN/Delete事件，其中：

·*event*：vsi\_up、vsi\_down或vsi\_del

·*vsiindex*：VSI索引

·*vsiname*：VSI名字

Receive vsi_modify_pbb_i-sid event: VsiIndex *vsiindex*, VsiName *vsiname*, PBB I-SID *pbbisid.*

收到VSI PBB模式改变事件，其中：

·*vsiindex*：VSI索引

·*vsiname*：VSI名字

·*pbbisid*：PBB I-SID

Receive *event* event.

收到*event*事件，*event*为事件类型，取值包括：

·l2vpn\_disable：L2VPN功能关闭

·l2vpn\_batch\_begin：批备开始

·l2vpn\_batch\_end：批备结束事件

Receive slot *slot-id* insert event.

收到单板*slot-id*插入事件。*slot-id*为单板所在的槽位号

Receive slot *slot-id* remove event.

收到单板*slot-id*拔出事件。*slot-id*为单板所在的槽位号

Slot *slot-id* does not support PBB.

单板*slot-id*不支持PBB。*slot-id*为单板所在的槽位号

Receive event: interface *interface-name* *event* VLAN *vlan-id.*

收到事件：接口*interface-name*加入/退出VLAN *vlan-id*（单个VLAN）。*interface-name*为端口名，*vlan-id*为VLAN-ID，*event*为事件类型，取值包括：

·added to：端口加入VLAN

·deleted from：端口退出VLAN

Receive event: interface *interface-name* *event* VLAN

VLANs number: *vlan-number*

VLANs:*start* to *end.*

收到事件：端口*interface-name*加入/退出VLAN（批量VLAN）。*interface-name*为端口名，*vlan-number*为VLAN个数，*start*为开始的VLAN值，*end*为结束的VLAN值，*event*为事件类型，取值包括：

·addedto：端口加入VLAN

·deletedfrom：端口退出VLAN

Receive NoHardResource event with Unicast Pseudo Wire number *n*.

No.   SlotId   VSIIndex  I-SID   B-MAC    B-VLAN

*[number  SlotId  VsiIndex I-sid* * mac-address    vlan-id*]

收到硬件资源不足消息，*n*为单播PW表项个数

Receive *event* event from slot *slot-id* with VsiIndex *vsiindex*, I-SID *i-sid*, Unicast Pseudo Wire number *n.*

No.              B-MAC                B-VLAN

*[number      mac-address        vlan-id*]

收到老化事件。*slot-id*为板号，*vsiindex*为*VSI*索引，*i-sid*为I-SID，*n*为单播表项个数，*event*为事件类型，取值包括：

·aged：老化

·cancelled_aged：不老化

Receive TC event with all interfaces and all VLANs.

收到所有接口和所有VLAN的TC（Topology Change）事件

Receive TC event

Interfaces number: *interface-number*

Interfaces:

*[interface-name*]

VLANs number: *vlan-number*

VLANs:

*[start *to *end*]

收到指定接口和指定VLAN的TC事件，其中：

·interface-number：为接口个数

·interface-name：接口名字

·vlan-number：VLAN个数

·start：开始的VLAN值

·end：结束的VLAN值

表1-3 debugging pbb packet命令输出信息描述表

字段

描述

Receive PBB frame from *interface-name*

从端口*interface-name*收到PBB报文

B-DA

目的B-MAC地址

B-SA

源B-MAC地址

B-Tag TPID

B-Tag类型

B-VLAN

B-VLAN值

I-Tag TPID

I-Tag类型

I-SID

I-SID值

C-DA

目的C-MAC地址

C-SA

源C-MAC地址

【举例】

\# 配置好PBB功能，并打开PBB错误调试信息开关。

\<Sysname\> debugging pbb error

\*Oct 24 14:23:58:531 2012 Sysname PBB/7/Error: The B-VLAN of this PBB packet is not the same as configured.

*[// PBB*]*报文所携带的B-VLAN与配置不相符，单播表项学习失败*

\*Oct 24 14:27:16:968 2012 Sysname PBB/7/Error: The I-SID of this PBB packet is not the same as configured.

*[// PBB*]*报文所携带的I-SID与配置不相符，单播表项学习失败*

\# 配置好PBB功能，并打开PBB事件调试信息开关。

\<Sysname\> debugging pbb event

\*Oct 24 14:36:35:312 2012 Sysname PBB/7/Event: Receive vsi_add event: VsiIndex 0, VsiName aaa, PBB I-SID 1, ShutdownFlag 0.

*// 处理VSI添加事件成功（即创建VSI）*

\*Oct 24 14:36:35:312 2009 Sysname PBB/7/Event: Receive slot 9 insert event.

*// 处理板插入事件*

\# 配置好PBB功能，并打开PBB报文调试信息开关。

\<Sysname\> debugging pbb packet

\*Oct 24 11:20:41:453 2012 Sysname PBB/7/Packet:

 Receive PBB frame from GigabitEthernet1/0/1

 B-DA: 0102-0304-0506

 B-SA: 0605-0403-0206

 B-Tag TPID: 0x8100

 B-VLAN: 20

 I-Tag TPID: 0x88e7

 I-SID: 111

 C-DA: 0101-0101-0101

 C-SA: 0202-0202-0202

*// 从上行口GigabitEthernet1/0/1收到的PBB报文头的具体内容*
