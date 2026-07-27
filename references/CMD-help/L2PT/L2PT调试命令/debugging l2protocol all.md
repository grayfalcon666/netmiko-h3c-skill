<!-- CMD-INDEX
  debugging l2protocol all            | 用户视图             | L8
  debugging l2protocol error          | 用户视图             | L38
  debugging l2protocol event          | 用户视图             | L108
  debugging l2protocol packet         | 用户视图             | L222
-->

**L2PT \-- L2PT调试命令 \-- debugging l2protocol all**

------------------------------------------------------------------------

【命令】

**[debugging l2protocol all**]

**[undo debugging l2protocol all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging l2protocol all**]命令用于打开L2PT的所有调试信息开关。**undo debugging l2protocol all**命令用于关闭L2PT的所有调试信息开关。

缺省情况下，L2PT的所有调试信息开关均处于关闭状态。

**L2PT \-- L2PT调试命令 \-- debugging l2protocol error**

------------------------------------------------------------------------

【命令】

**[debugging l2protocol error**]

**[undo debugging l2protocol error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging l2protocol error**]命令用来打开L2PT错误调试信息开关。**undo debugging l2protocol error**命令用来关闭L2PT错误调试信息开关。

缺省情况下，L2PT错误调试信息开关处于关闭状态。

表1-1 debugging l2protocol error命令输出信息描述表

字段

描述

Failed to multicast a *Protocol_Type* packet to the *Network_Type*.

向*Network_Type*网络发送*Protocol_Type*报文失败，*Protocol_Type*包括CDP、DLDP、GVRP、PAGP、PVST、VTP、tunnel，*Network_Type*包括customer network、service provider network

Failed to multicast an *Protocol_Type* packet to the *Network_Type*.

向*Network_Type*网络发送*Protocol_Type*报文失败，*Protocol_Type*包括EOAM、LACP、LLDP、MVRP、STP，*Network_Type*包括customer network、service provider network

Failed to broadcast a *PacketType* packet in VLAN *vlan-id*.

在VLAN *vlan-id*内广播*PacketType*报文失败。*PacketType*包括CDP、DLDP、GVRP、PAGP、PVST、VTP、tunnel

Failed to broadcast an *PacketType* packet in VLAN *vlan-id*.

在VLAN *vlan-id*内广播*PacketType*报文失败。*PacketType*包括unrecognized tunnel、LLDP、MVRP、STP

【举例】

\# 在设备上使能CDP协议的L2PT Tunnel功能后，打开L2PT调试信息开关。

\<Sysname\> debugging l2protocol error

%Jun 13 09:50:53 672 2014 Sysname L2PT/7/ERROR:

Failed to multicast a CDP packet to the customer network.

*// 向用户网络发送一个CDP报文失败。*

%Jun 13 09:50:53 672 2014 Sysname L2PT/7/ERROR:

Failed to broadcast an unrecognized tunnel packet in VLAN 3.

*// 向VLAN 3内广播一个不识别的tunnel报文失败*

**L2PT \-- L2PT调试命令 \-- debugging l2protocol event**

------------------------------------------------------------------------

【命令】

**[debugging l2protocol event**]

**[undo debugging l2protocol event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging l2protocol event**]命令用来打开L2PT事件调试信息开关。**undo debugging l2protocol event**命令用来关闭L2PT事件调试信息开关。

缺省情况下，L2PT事件调试信息开关处于关闭状态。

表1-2 debugging l2protocol event命令输出信息描述表

字段

描述

Received *IF_event_name* event for *IfName.*

收到接口*IfName*的*IF_event_name*事件，IF\_*event_name*包括IF_DELETE、IF_ACTIVE、IF_DEACTIVE

*[IfName *joined the ]aggregation group that corresponds to aggregate interface *IfAggName.*

接口*IfName*加入聚合组，该聚合组对应的聚合口为*IfAggName*

*[IfName *leaved the aggregation group that corresponds to aggregate interface *IfAggName.*]

接口*IfName*退出聚合组，该聚合组对应的聚合口为*IfAggName*

Received SLOT_INSERT event for slot *slot_id.*（分布式设备－独立运行模式、集中式IRF设备）

Received SLOT_INSERT event for chassis *chassis_id* slot *slot_id.*（分布式设备－IRF模式）

收到板*slot_id*的SLOT_INSERT事件（分布式设备－独立运行模式/集中式IRF设备）

收到成员设备*chassis_id*上板*slot_id*的SLOT_INSERT事件（分布式设备－IRF模式）

Received ISSU PRESOFTREBOOT event for slot *slot_id*.（分布式设备－独立运行模式/集中式IRF设备）

Received ISSU PRESOFTREBOOT event for chassis *chassis_id* slot *slot_id*.（分布式设备－IRF模式）

收到板*slot_id*的ISSU PRESOFTREBOOT事件（分布式设备－独立运行模式/集中式IRF设备）

收到成员设备*chassis_id*上板*slot_id*的ISSU PRESOFTREBOOT事件（分布式设备－独立运行模式/集中式IRF设备）

Received ISSU SOFTREBOOTOK event for slot *slot_id.*（分布式设备－独立运行模式/集中式IRF设备）

Received ISSU SOFTREBOOT_OK event for chassis *chassis_id* slot *slot_id*.（分布式设备－IRF模式）

收到板*slot_id*的ISSU SOFTREBOOTOK事件（分布式设备－独立运行模式/集中式IRF设备）

收到成员设备*chassis_id*上板*slot_id*的ISSU SOFTREBOOT_OK事件（分布式设备－独立运行模式/集中式IRF设备）

【举例】

\# 在设备上使能STP协议 tunneling功能后，打开L2PT调试信息开关，进行如下操作：拔去某一接口板，然后插入。

\<Sysname\> debugging l2protocol event{.TerminalDisplayChar}

%Jun 13 09:59:53 672 2014 Sysname L2PT/7/EVENT:{.TerminalDisplayChar}

Received IF_DEACTIVE event for GigabitEthernet1/0/1.{.TerminalDisplayChar}

*// 拔去某一接口板，收到接口去激活事件* *，接口为GigabitEthernet1/0/1*

%Jun 13 10:04:53 674 2014 Sysname L2PT/7/EVENT:{.TerminalDisplayChar}

GigabitEthernet1/0/1 joined the aggregation group that corresponds to aggregate interface BAGG1.{.TerminalDisplayChar}

*// 接口GigabitEthernet1/0/1加入聚合组，该聚合组对应的聚合接口为BAGG1*

%Jun 13 10:04:53 674 2014 Sysname L2PT/7/EVENT:{.TerminalDisplayChar}

GigabitEthernet1/0/1 leaved the aggregation group that corresponds to aggregate interface BAGG1.{.TerminalDisplayChar}

*// 接口GigabitEthernet1/0/1退出聚合组，该聚合组对应的聚合接口为BAGG1*

%Jun 13 10:04:53 674 2014 Sysname L2PT/7/EVENT:{.TerminalDisplayChar}

Received SLOT_INSERT event for slot 2.{.TerminalDisplayChar}

*// 插入接口板，收到板插入事件，槽号为2（分布式设备－独立运行模式/集中式-IRF设备）*

%Jun 13 10:04:53 674 2014 Sysname L2PT/7/EVENT:{.TerminalDisplayChar}

Received ISSU PRESOFTREBOOT event for slot 2.{.TerminalDisplayChar}

*// 收到板ISSU*{.TerminalDisplayChar}*PRESOFTREBOOT事件，槽号为2（分布式设备－独立运行模式/集中式-IRF设备）*

%Jun 13 10:04:53 674 2014 Sysname L2PT/7/EVENT:{.TerminalDisplayChar}

Received ISSU SOFTREBOOT_OK event for slot 2.{.TerminalDisplayChar}

*// 收到板ISSU SOFTREBOOT_OK事件，槽号为2（分布式设备－独立运行模式/集中式-IRF设备）*

**L2PT \-- L2PT调试命令 \-- debugging l2protocol packet**

------------------------------------------------------------------------

【命令】

**[debugging l2protocol packet**[ [ **drop** \| **receive** \| **send** ]  **interface** *interface-type* *interface-number* ]]

**[undo debugging l2protocol packet**[ [ **drop** \| **receive** \| **send** ]  **interface** *interface-type* *interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[drop**]：表示丢弃报文调试信息开关。

**[receive**]：表示接收报文调试信息开关。

**[send**]：表示发送报文调试信息开关。

**[interface** *interface-type* *interface-number*]：表示指定接口上的调试信息开关。*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，表示所有接口上的调试信息开关。

【描述】

**[debugging l2protocol packet**]命令用来打开L2PT报文调试信息开关，当报文类型不一样时，报文的具体字段不同。**undo debugging l2protocol packet**命令用来关闭L2PT 报文调试信息开关。

缺省情况下，L2PT报文调试信息开关处于关闭状态。

需要注意的是，在指定本命令时，如果未指定**receive**、**send**和**drop**，则表示L2PT的所有报文调试信息开关。

表1-3 debugging l2protocol packet命令输出信息描述表

字段

描述

*[IfName* received a *PacketType* packet with PDU length *ulMsgTotal*.]

接口*IfName*收到*PacketType*报文，PDU长度为*ulMsgTotal*。*PacketType*包括CDP、DLDP、GVRP、PAGP、PVST、VTP、tunnel

*[IfName* received an *PacketType* packet with PDU length *ulMsgTotal*.]

接口*IfName*收到*PacketType*报文，PDU长度为*ulMsgTotal*。*PacketType*包括EOAM 、LACP 、LLDP、MVRP、STP

*[IfName* multicast a *PacketType* packet to the *Network_Type*.]

接口*IfName*组播发送*PacketType*报文到*Network_Type*网络。*PacketType*包括CDP、DLDP、GVRP、PAGP、PVST、VTP、tunnel；*Network_Type*包括customer network、service provider network

*[IfName* multicast an *PacketType* packet to the *Network_Type*.]

接口*IfName*组播发送*PacketType*报文到*Network_Type*网络。*PacketType*包括EOAM、LACP、LLDP、MVRP、STP；*Network_Type*包括customer network、service provider network

*[IfName* broadcast a *PacketType* packet in VLAN *vlan-id*.]

接口*IfName*在VLAN *vlan-id*内广播*PacketType*报文。*PacketType*包括CDP、DLDP、GVRP、PAGP、PVST、VTP、tunnel

*[IfName* broadcast an *PacketType* packet in VLAN *vlan-id*.]

接口*IfName*在VLAN *vlan-id*内广播*PacketType*报文。*PacketType*包括unrecognized tunnel、LLDP、MVRP、STP

*[IfName* dropped a *PacketType* packet.]

接口*IfName*丢弃*PacketType*报文。*PacketType*包括CDP、DLDP、GVRP、PAGP、PVST、VTP、tunnel

*[IfName* dropped an *PacketType* packet.]

接口*IfName*丢弃PacketType报文。*PacketType*包括EOAM 、LACP、LLDP、MVRP、STP

*[IfName* dropped a tunnel packet because the interface has been enabled with l2protocol tunneling.]

接口*IfName*丢弃tunnel报文，因为接口使能了tunneling功能

Destination MAC address

报文目的MAC地址

Source MAC address

报文源MAC地址

Outer VLAN ID

报文外层VLAN  ID

Inner VLAN ID

报文内层VLAN ID

DSAP

报文目的服务访问点信息

SSAP

报文源服务访问点信息

Control

报文control字段信息

OUI

报文OUI字段信息

SNAP type

报文SNAP封装协议类型信息

Protocol type

报文ETH II封装协议类型信息

****

【举例】

\# 在设备上使能PVST和EOAM协议的L2PT Tunnel功能以及DLDP协议的L2PT Drop功能，打开L2PT报文调试信息开关。

\<Sysname\> debugging l2protocol packet

%Jun 13 09:50:53 672 2014 Sysname L2PT/7/PKT_RECV:

GigabitEthernet1/0/1 received a PVST packet with PDU length 150.

Destination MAC address   : 0100-0CCC-CCCD

Source MAC address        : 0011-FFFE-0001

Outer VLAN ID             : 50

Inner VLAN ID             : 20

DSAP                      : 0x42

SSAP                      : 0x42

Control                   : 0x03

OUI                       : 0x00000C

SNAP type                 : 0x010B

*// 接口GigabitEthernet1/0/1接收到一个PVST报文，报文PDU长度为150*

%Jun 13 09:50:53 672 2014 Sysname L2PT/7/PKT_SEND:

GigabitEthernet1/0/1 multicast an EOAM packet to customer networks.

Destination MAC address   : 0180-C200-0002

Source MAC address        : 0011-FFFE-0001

Outer vlan ID             : 50

Inner vlan ID             : 20

Protocol type             : 0x8809

*// 接口GigabitEthernet1/0/1向用户网络组播发送一个EOAM报文*

%Jun 13 09:50:53 672 2014 Sysname L2PT/7/PKT_SEND:

GigabitEthernet1/0/1 broadcast an EOAM packet in VLAN 5.

Destination MAC address   : 0180-C200-0002

Source MAC address        : 0011-FFFE-0001

Outer VLAN ID             : 50

Inner VLAN ID             : 20

Protocol type             : 0x8809

*// 接口GigabitEthernet1/0/1在VLAN 5内广播一个EOAM报文*

%Jun 13 09:50:53 672 2014 Sysname L2PT/7/PACKET_DROP:

GigabitEthernet1/0/1 dropped a DLDP packet.

*// 接口GigabitEthernet1/0/1丢弃一个DLDP报文*

%Jun 13 09:50:53 672 2014 Sysname L2PT/7/PACKET_DROP:

GigabitEthernet1/0/1 dropped a tunnel packet because the interface has been enabled with l2protocol tunneling.

*// 接口GigabitEthernet1/0/1丢弃一个tunnel报文，因为该接口使能了tunneling功能*

