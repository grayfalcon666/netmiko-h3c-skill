
**环路检测 \-- 环路检测调试命令 \-- debugging loopback-detection**

------------------------------------------------------------------------

【命令】

**[debugging loopback-detection**[ { **all** \| **error** \| **event** \| **packet** [ **vlan** *vlan-list* ] }]]

**[undo debugging loopback-detection**[ { **all** \| **error** \| **event** \| **packet** [ **vlan** *vlan-list* ] }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示环路检测所有调试信息开关。

**[error**]：表示环路检测错误调试信息开关。

**[event**]：表示环路检测事件调试信息开关。

**[packet**]：表示环路检测报文调试信息开关。

**[vlan ***vlan-list*]：表示指定VLAN内环路检测报文的调试信息开关。*vlan-list*为VLAN列表，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果不指定该参数，表示所有VLAN内环路检测报文的调试信息开关。

【描述】

**[debugging loopback-detection**]命令用来打开环路检测调试信息开关。**undo debugging loopback-detection**命令用来关闭环路检测调试信息开关。

缺省情况下，环路检测调试信息开关处于关闭状态。

表1-1 debugging loopback-detection error命令输出信息描述表

字段

描述

Dropped a length-invalid packet on interface *interface-name*

在接口*interface-name*上丢弃一个长度无效的报文

Received a TLV-invalid message packet

收到一个带有无效TLV消息的报文

表1-2 debugging loopback-detection event命令输出信息描述表

字段

描述

Dropped a packet because loopback-detection is disabled

由于环路检测未使能，因此丢弃报文

Succeeded to process an packet, it's device MAC is *mac-address*

成功处理了一个报文，其设备MAC为*mac-address*

Loop occurred on interface *interface-name*

接口*interface-name*上出现环路

Loop recovered on interface *interface-name*

接口*interface-name*上的环路恢复

表1-3 debugging loopback-detection packet命令输出信息描述表

字段

描述

Succeeded to send a packet on interface *interface-name* in VLAN *vlan-id*

在VLAN *vlan-id*的端口*interface-name*上成功发送了一个报文

Failed to send a packet on interface *interface-name* in VLAN *vlan-id*

在VLAN *vlan-id*的端口*interface-name*上发送报文失败

Succeeded to send a packet in VLAN *vlan-id*

在VLAN *vlan-id*中成功发送了一个报文

Failed to send a packet in VLAN *vlan-id*

在VLAN *vlan-id*中发送报文失败

Received a packet on interface *interface-name* in VLAN *vlan-id*

在VLAN *vlan-id*的端口*interface-name*上收到了一个报文

Succeeded to process a packet on interface *interface-name* in VLAN *vlan-id*

在VLAN *vlan-id*的端口*interface-name*上成功处理了一个报文

【举例】

\# 打开环路检测错误调试信息开关。

\<Sysname\> debugging loopback-detection error

\*Dec 22 14:09:53:859 2011 Sysname LPDT/7/Error: -MDC=1; Received a TLV-invalid message packet.

*// 收到一个带有无效TLV消息的报文*

\# 打开环路检测事件调试信息开关。

\<Sysname\> debugging loopback-detection event

\*Dec 22 11:59:33:391 2011 Sysname LPDT/7/Event: -MDC=1;Dropped a packet because loopback-detection is disabled.

*// 由于环路检测未使能，因此丢弃报文*

\# 打开环路检测报文调试信息开关。

\<Sysname\> debugging loopback-detection packet

\*Dec 22 11:57:31:453 2011 Sysname LPDT/7/Packet: -MDC=1; Succeeded to send a packet in VLAN 6.

*// 在VLAN 6中成功发送了一个报文*
