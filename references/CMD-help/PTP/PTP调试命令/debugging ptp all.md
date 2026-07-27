<!-- CMD-INDEX
  debugging ptp all                   | 用户视图             | L10
  debugging ptp error                 | 用户视图             | L36
  debugging ptp event                 | 用户视图             | L368
  debugging ptp fsm                   | 用户视图             | L526
  debugging ptp packet                | 用户视图             | L576
  debugging ptp timer                 | 用户视图             | L1146
-->

**PTP \-- PTP调试命令 \-- debugging ptp all**

------------------------------------------------------------------------

【命令】

**[debugging ptp all**]

**[undo debugging ptp all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ptp all**]命令用于打开所有PTP的调试信息开关。**undo debugging ptp all**命令用于关闭所有PTP的调试信息开关。

缺省情况下，所有PTP的调试信息开关处于关闭状态。

**PTP \-- PTP调试命令 \-- debugging ptp error**

------------------------------------------------------------------------

【命令】

**[debugging ptp error**]

**[undo debugging ptp error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ptp error**]命令用来打开PTP错误调试信息开关。**undo debugging ptp error**命令用来关闭PTP错误调试信息开关。

缺省情况下，PTP错误调试信息开关处于关闭状态。

表1-1 debugging ptp error命令输出信息描述表

字段

描述

*[IfName *received a PTP packet from itself.]

接口*IfName*收到来自于自己的PTP报文

*[IfName *received a duplicate PTP packet.]

接口*IfName*收到重复的PTP报文

*[IfName* received a PTP packet with invalid length.]

接口*IfName*收到一个长度无效的PTP报文

*[IfName* received a PTP packet with invalid version.]

接口*IfName*收到一个版本无效的PTP报文

*[IfName *received a PTP packet with invalid domainNumber.]

接口*IfName*收到一个域值无效的PTP报文

*[IfName* received a PTP packet with invalid type.]

接口*IfName*收到一个类型无效的PTP报文

*[IfName *received a Signaling packet with *InvalidType*.]

接口*IfName*收到一个无效Signaling消息，无效类型*InvalidType*包括invalid TLV type、invalid TLV length field、invalid TLV organizationID、invalid targetPortID、unsupported TLV、invalid TLV organizationSubType

*[IfName* received an Announce packet with invalid stepsRemoved field.]

接口*IfName*收到的Announce报文的stepsRemoved字段错误

*[IfName* received an Announce packet with local clock ID in the PATH_TRACE TLV.]

接口*IfName*收到的Announce报文的PATH_TRACE TLV字段中包括本时钟ID

*[IfName* received an Announce packet from itself.]

接口*IfName*收到的Announce报文来自于自己

*[IfName*] received a Follow_Up packet with invalid sequenceID.

接口*IfName*收到一个序列号无效的Follow_Up报文

*[IfName*] received a Follow_Up packet with invalid sourcePortID.

接口*IfName*收到一个源端口ID无效的Follow_Up报文

*[IfName* received a Follow_Up packet with invalid TLV length field.]

接口*IfName*收到的Follow_Up报文携带的TLV中长度字段非法

*[IfName* received a Follow_Up packet without Follow_Up information TLV.]

接口*IfName*收到的Follow_Up报文没有携带Follow_Up information TLV

*[IfName* received a Follow_Up packet with invalid Follow_Up information TLV.]

接口*IfName*收到的Follow_Up报文的Follow_Up information TLV非法

*[IfName*] received a Delay_Resp packet with invalid sequenceID.

接口*IfName*收到一个序列号无效的Delay_Resp报文

*[IfName*] received a Delay_Resp packet with invalid sourcePortID.

接口*IfName*收到一个源端口ID无效的Delay_Resp报文

*[IfName*] received a Delay_Resp packet with invalid requestingPortID.

接口*IfName*收到一个请求端口ID无效的Delay_Resp报文

*[IfName*] received a Delay_Resp packet with no associated Delay_Req packet.

接口*IfName*收到一个Delay_Resp报文，该报文无对应的Delay_Req报文

*[IfName*] received a Pdelay_Resp packet with invalid sequenceID.

接口*IfName*收到一个序列号无效的Pdelay_Resp报文

*[IfName*] received a Pdelay_Resp packet with invalid requestingPortID.

接口*IfName*收到一个请求端口ID无效的Pdelay_Resp报文

*[IfName*] received a Pdelay_Resp packet with no associated Pdelay_Req packet.

接口*IfName*收到一个Pdelay_Resp报文，该报文无对应的Pdelay_Req报文

*[IfName*] received a Pdelay_Resp_Follow_Up packet with invalid sequenceID.

接口*IfName*收到一个序列号无效的Pdelay_Resp_Follow_Up报文

*[IfName*] received a Pdelay_Resp_Follow_Up packet with invalid sourcePortID.

接口*IfName*收到一个源端口ID无效的Pdelay_Resp_Follow_Up报文

*[IfName*] received a Pdelay_Resp_Follow_Up packet with invalid requestingPortID.

接口*IfName*收到一个请求端口ID无效的Pdelay_Resp_Follow_Up报文

*[IfName*] received a Pdelay_Resp_Follow_Up packet with no associated Pdelay_Req packet.

接口*IfName*收到一个Pdelay_Resp_Follow_Up报文，该报文无对应的Pdelay_Req报文

*[IfName*] received a Pdelay_Resp_Follow_Up packet with no associated Pdelay_Resp packet.

接口*IfName*收到一个Pdelay_Resp_Follow_Up报文，该报文无对应的Pdelay_Resp报文

*[IfName* detected link fault, the peer port is out of response.]

接口*IfName*检测到链路不通（链路两端配置不同的延时机制）

*[IfName* detected link fault, there may be more than one peer port.]

接口*IfName*检测到链路错误（多个延时机制为P2P的端口通过E2ETC相连）

*[IfName *received a PTP packet with incorrect encapsulation.]

接口*IfName*收到一个PTP报文，无效封装

*[IfName* discarded a PTP packet because the interface is operating in half-duplex mode.]

接口*IfName*丢弃PTP报文，接口工作在半双工模式

*[IfName *discarded a PTP packet because the PTP source IP address had not been configured.]

接口*IfName*丢弃PTP报文，PTP报文源IP地址未配置

*[IfName* discarded a PTP packet with an invalid destination IP address.]

接口*IfName*丢弃PTP报文，PTP报文目的IP地址非法

*[IfName* discarded a PTP packet with an invalid source IP address.]

接口*IfName*丢弃PTP报文，PTP报文源IP地址非法

*[IfName *failed to encapsulate packets because no IP address was configured for *IfName*.]

接口*IfName*封装报文失败，接口没有配置IP地址

*[IfName *received a PTP packet with an unsupported UTC offset value.]

接口*IfName*收到一个PTP报文，该报文携带的UTC offset字段值超出支持范围

【举例】

\# 在一台设备上启动PTP功能，打开PTP错误调试信息开关，配置设备的时钟节点类型。

\<Sysname\> debugging ptp error

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ptp clock-step one-step

Sysname-GigabitEthernet1/0/1 ptp enable

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a PTP packet from itself.

*// 接口GigabitEthernet1/0/1收到来自于自己的PTP报文*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a duplicate PTP packet.

*// 接口GigabitEthernet1/0/1收到重复的PTP报文*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a PTP packet with invalid length.

*// 接口GigabitEthernet1/0/1收到一个长度无效的PTP报文*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a PTP packet with invalid version.

*// 接口GigabitEthernet1/0/1收到一个版本无效的PTP报文*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a PTP packet with invalid domainNumber.

*// 接口GigabitEthernet1/0/1收到一个域值无效的PTP报文*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a PTP packet with invalid type.

*// 接口GigabitEthernet1/0/1收到一个类型无效的PTP报文*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Signaling packet with invalid TLV type.

*// 接口GigabitEthernet1/0/1收到的signaling报文TLV类型无效*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received an Announce packet with invalid stepsRemoved field.

*// 接口GigabitEthernet1/0/1，收到的Announce报文，报文的stepRemoved字段大于或等于255无效*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received an Announce packet with local clock ID in the PATH_TRACE TLV.

*// 接口GigabitEthernet1/0/1，收到的Announce报文的PATH_TRACE TLV中查找到本时钟ID*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received an Announce packet from itself.

*// 接口GigabitEthernet1/0/1，收到的Announce报文来自于自己*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Follow_Up packet with invalid TLV length field.

*// 接口GigabitEthernet1/0/1收到一个序列号无效的Follow_Up报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Follow_Up packet with invalid sequenceID.

*// 接口GigabitEthernet1/0/1收到一个源端口ID无效的Follow_Up报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Follow_Up packet with invalid sourcePortID.

*// 接口GigabitEthernet1/0/1，收到的Follow_Up报文携带的TLV中长度字段非法*

\*Jan 24 15:17:20:518 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Follow_Up packet with no Follow_Up information TLV.

*// 接口GigabitEthernet1/0/1，收到的Follow_Up报文没有携带Follow_Up information TLV*

\*Jan 24 15:17:55:178 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Follow_Up packet with invalid Follow_Up information TLV.

*// 接口GigabitEthernet1/0/1，收到的Follow_Up报文的Follow_Up information TLV非法*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 detected link fault, the peer port is out of response.

*// 接口GigabitEthernet1/0/1收到一个序列号无效的Delay_Resp报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Delay_Resp packet with invalid sequenceID.

*// 接口GigabitEthernet1/0/1收到一个源端口ID无效的Delay_Resp报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Delay_Resp packet with invalid sourcePortID.

*// 接口GigabitEthernet1/0/1收到一个请求端口ID无效的Delay_Resp报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Delay_Resp packet with invalid requestingPortID.

*// 接口GigabitEthernet1/0/1收到一个 Delay_Resp报文，该报文无对应的Delay_Req报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Delay_Resp packet with no associated Delay_Req packet.

*// 接口GigabitEthernet1/0/1收到一个序列号无效的Pdelay_Resp报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp packet with invalid sequenceID.

*// 接口GigabitEthernet1/0/1收到一个请求端口ID无效的Pdelay_Resp报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp packet with invalid requestingPortID.

*// 接口GigabitEthernet1/0/1收到一个Pdelay_Resp报文，该报文无对应的Pdelay_Req报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp packet with no associated Pdelay_Req packet.

*// 接口GigabitEthernet1/0/1收到一个序列号无效的Pdelay_Resp_Follow_Up报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp_Follow_Up packet with invalid sequenceID.

*// 接口GigabitEthernet1/0/1收到一个源端口ID无效的Pdelay_Resp_Follow_Up报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp_Follow_Up packet with invalid sourcePortID.

*// 接口GigabitEthernet1/0/1收到一个请求端口ID无效的Pdelay_Resp_Follow_Up报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp_Follow_Up packet with invalid requestingPortID.

*// 接口GigabitEthernet1/0/1收到一个Pdelay_Resp_Follow_Up报文，该报文无对应的Pdelay_Req报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp_Follow_Up packet with no associated Pdelay_Req packet.

*// 接口GigabitEthernet1/0/1收到一个Pdelay_Resp_Follow_Up报文，该报文无对应的Pdelay_Resp报文*

\*Jan 24 15:16:28:781 2013 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a Pdelay_Resp_Follow_Up packet with no associated Pdelay_Resp packet.

*// 接口GigabitEthernet1/0/1检测到链路不通（链路两端配置不同的延时机制）*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 detected link fault, there may be more than one peer port.

*// 接口GigabitEthernet1/0/1检测到链路错误（多个延时机制为P2P的端口通过E2ETC相连）*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a PTP packet with incorrect encapsulation.

*// 接口GigabitEthernet1/0/1收到一个PTP报文，无效封装*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 discarded a PTP packet because the interface is operating in half-duplex mode.

*// 接口GigabitEthernet1/0/1丢弃PTP报文，接口工作在半双工模式*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 discarded a PTP packet because the PTP source IP address had not been configured.

*// 接口GigabitEthernet1/0/1丢弃PTP报文，PTP报文源IP地址未配置*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 discarded a PTP packet with an invalid destination IP address.

*// 接口GigabitEthernet1/0/1丢弃PTP报文，PTP报文目的IP地址非法*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 discarded a PTP packet with an invalid source IP address.

*// 接口GigabitEthernet1/0/1丢弃PTP报文，PTP报文源IP地址非法*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 failed to encapsulate packets because no IP address was configured for GigabitEthernet1/0/1.

*// 接口GigabitEthernet1/0/1接口IfName封装报文失败，接口没有配置IP地址*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/ERROR: GigabitEthernet1/0/1 received a PTP packet with an unsupported UTC offset value.

*// 接口GigabitEthernet1/0/1收到一个PTP报文，该报文携带的UTC offset字段值超出支持范围*

**PTP \-- PTP调试命令 \-- debugging ptp event**

------------------------------------------------------------------------

【命令】

**[debugging ptp event**]

**[undo debugging ptp event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ptp event**]命令用来打开PTP事件调试信息开关。**undo debugging ptp event**命令用来关闭PTP事件调试信息开关。

缺省情况下，**PTP**事件调试信息开关处于关闭状态。

表1-2 debugging ptp event命令输出信息描述表

字段

描述

Received *IF_event_name* event for *IfName.*

收到接口*IfName*的*IF_event_name*事件，*IF_event_name*包括IF_DELETE、IF_UP、IF_DOWN、IF_ACTIVE、IF_DEACTIVE、IF_HALFDUPLEX、IF_FULLDUPLEX

Received SLOT_INSERT event for slot *slot_id.*（分布式设备－独立运行模式、集中式IRF设备）

Received SLOT_INSERT event for chassis *chassis_id* slot *slot_id.*（分布式设备－IRF模式）

收到板*slot_id*的SLOT_INSERT事件（分布式设备－独立运行模式/集中式IRF设备）

收到成员设备*chassis_id*上板*slot_id*的SLOT_INSERT事件（分布式设备－IRF模式）

Received SLOT_REMOVE event for slot *slot_id.*（分布式设备－独立运行模式、集中式IRF设备）

Received SLOT_REMOVE event for chassis *chassis_id* slot *slot_id.*（分布式设备－IRF模式）

收到板*slot_id*的SLOT_REMOVE事件（分布式设备－独立运行模式/集中式IRF设备）

收到成员设备*chassis_id*上板*slot_id*的SLOT_REMOVE事件（分布式设备－IRF模式）

Received *CHANNEL_event* event for slot *slot_id.*（分布式设备－独立运行模式/集中式IRF设备）

Received *CHANNEL_event* event for chassis *chassis_id* slot *slot_id*.（分布式设备－IRF模式）

收到板*slot_id*的*CHANNEL_event*事件，*CHANNEL_event*事件包括CHANNEL_ESTABLIST、CHANNEL_DISCONNECT（分布式设备－独立运行模式/集中式IRF设备）

收到成员设备*chassis_id*上板*slot_id*的*CHANNEL_event*事件，*CHANNEL*\_event事件包括CHANNEL_ESTABLIST、CHANNEL_DISCONNECT（分布式设备－独立运行模式/集中式IRF设备）

Received BRIDGEMAC_CHANGE event.

收到桥MAC变化事件

Received SYSTIME_CHANGE event.

收到系统时间变化事件

Set *PacketType* packet sending interval for *IfName* to the configured value.

Signaling消息设置接口*IfName PacketType*消息的时间间隔为用户配置值，*PacketType*包括Announce、Sync、Pdelay_Req

Set *PacketType* packet sending interval for *IfName* to signaling packet value.

Signaling消息设置接口*IfName PacketType*消息的时间间隔为Signaling报文携带值，*PacketType*包括Announce、Sync、Pdelay_Req

*[IfName* stopped sending *PacketType packet*.]

Signaling消息设置接口*IfName*停止发送*PacketType*消息，*PacketType*包括Announce、Sync、Pdelay_Req

The *PacketType* packet sending interval for *IfName* is not changed.

Signaling消息设置接口*IfName PacketType*消息发送间隔不变，*PacketType*包括Announce、Sync、Pdelay_Req

*[IfName* started computing NeighberRateRatio.]

Signaling消息使接口*IfName*开始计算邻居频率比

*[IfName* stopped computing NeighberRateRatio.]

Signaling消息使接口*IfName*停止计算邻居频率比

*[IfName* started computing NeighberPropDelay.]

Signaling消息使接口*IfName*开始计算路径延时

*[IfName* stopped computing NeighberPropDelay.]

Signaling消息使接口*Ifname*停止计算路径延时

【举例】

\# 在一台设备上启动PTP功能，打开PTP事件调试信息开关，进行如下操作：拔去某一接口板，然后插入，配置设备的时钟节点类型，并在接口上使能PTP功能。

\<Sysname\> debugging ptp event{.TerminalDisplayChar}

\*Jun 13 09:59:53 672 2011 Sysname PTP/7/EVENT: Received IF_DEACTIVE event for GigabitEthernet1/0/1.{.TerminalDisplayChar}

*// 拔去某一接口板，收到接口去激活事件* *，接口为GigabitEthernet1/0/1*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: Received SLOT_INSERTED event for slot 2.{.TerminalDisplayChar}

*// 接口板插入，收到板插入事件，槽号为2（分布式设备－独立运行模式/集中式-IRF设备）*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: Received CHANNEL_ESTABLIST event for slot 2.{.TerminalDisplayChar}

*// 接口板插入，收到通道建立事件* *，槽号为2（分布式设备－独立运行模式/集中式-IRF设备）*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: Received BRIDGEMAC_CHANGE event.{.TerminalDisplayChar}

*// 收到桥MAC变化事件*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: Received SYSTIME_CHANGE event.{.TerminalDisplayChar}

*// 收到系统时间变化事件*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: Set Announce packet sending interval for GigabitEthernet1/0/1 to the configured value.{.TerminalDisplayChar}

*[// Signaling*]*消息设置接口GigabitEthernet1/0/1上Announce消息的时间间隔为用户配置值*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: Set Announce packet sending interval for GigabitEthernet1/0/1 to signaling packet value.{.TerminalDisplayChar}

*[// Signaling*]*消息设置接口GigabitEthernet1/0/1上Announce消息的时间间隔为Signaling报文携带值*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: GigabitEthernet1/0/1 stop sending Announce packet.{.TerminalDisplayChar}

*[// Signaling*]*消息设置接口GigabitEthernet1/0/1停止发送Announce消息*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: The Announce packet sending interval for GigabitEthernet1/0/1 is not changed.{.TerminalDisplayChar}

*[// Signaling*]*消息设置接口GigabitEthernet1/0/1上PacketType消息发送间隔不变*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: GigabitEthernet1/0/1 started computing NeighberRateRatio.{.TerminalDisplayChar}

*[// Signaling*]*消息使接口GigabitEthernet1/0/1上开始计算邻居频率比*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: GigabitEthernet1/0/1 stopped computing NeighberRateRatio.{.TerminalDisplayChar}

*[// Signaling*]*消息使接口GigabitEthernet1/0/1上停止计算邻居频率比*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: GigabitEthernet1/0/1 started computing NeighberPropDelay.{.TerminalDisplayChar}

*[// Signaling*]*消息使接口GigabitEthernet1/0/1开始计算路径延时*

\*Jun 13 10:04:53 674 2011 Sysname PTP/7/EVENT: GigabitEthernet1/0/1 stopped computing NeighberPropDelay.{.TerminalDisplayChar}

*[// Signaling*]*消息使接口GigabitEthernet1/0/1停止计算路径延时*

**PTP \-- PTP调试命令 \-- debugging ptp fsm**

------------------------------------------------------------------------

【命令】

**[debugging ptp fsm ** **interface** *interface-type* *interface-number* ]

**[undo debugging ptp fsm ** **interface** *interface-type* *interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：指定接口上的调试信息开关。*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，表示所有端口上的调试信息开关。

【描述】

**[debugging ptp fsm**]命令用来打开PTP状态机调试信息开关。**undo debugging ptp fsm**命令用来关闭PTP状态机调试信息开关。

缺省情况下，PTP状态机调试信息开关处于关闭状态。

表1-3 debugging ptp fsm命令输出信息描述表

字段

描述

*[IfName* state changed to *portstate*.]

接口*IfName*的状态迁移到*portstate*，*portstate*包括：Faulty、Disabled、Listening、Premaster、Master、Passive、Uncalibrated、Slave

【举例】

\# 在一台设备上启动PTP功能，打开PTP状态机调试信息开关，配置设备的时钟节点类型，并在接口上使能PTP功能。

\<Sysname\> debugging ptp fsm

\*{.TerminalDisplayChar}Jun 13 09:50:53 672 2011 Sysname PTP/7/FSM: GigabitEthernet1/0/1 state changed to Master.

*// 接口GigabitEthernet1/0/1状态迁移到Master状态*

**PTP \-- PTP调试命令 \-- debugging ptp packet**

------------------------------------------------------------------------

【命令】

**[debugging ptp packet**[ [ **send** \| **receive** ]  **interface** *interface-type* *interface-number* ]]

**[undo ptp debugging packet**[ [ **send** \| **receive** ]  **interface** *interface-type* *interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[send**]：表示发送报文调试信息开关。

**[receive**]：表示接收报文调试信息开关。

**[interface** *interface-type* *interface-number*]：指定接口上的调试信息开关。*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，表示所有接口上的调试信息开关。

【描述】

**[debugging ptp packet**]命令用来打开PTP报文调试信息开关，当报文类型不一样时，报文的具体字段不同。**undo debugging packet**命令用来关闭PTP报文调试信息开关。

缺省情况下，PTP报文调试信息开关处于关闭状态。

表1-4 debugging ptp packet命令输出信息描述表

字段

描述

*[IfName* received a *PacketType* packet with length *ulMsgTotal*.]

接口*IfName*收到*PacketType*报文，报文长度为*ulMsgTotal*。*PacketType*包括Sync、Delay_Req、Pdelay_Req、Pdelay_Resp、Follow_Up、Delay_Resp、Pdelay_Resp_Follow_Up、Announce、Signaling

*[IfName* sent a *PacketType* packet with length *ulMsgTotal*.]

接口*IfName*发送*PacketType*报文，报文长度为*ulMsgTotal*。*PacketType*包括Sync、Delay_Req、Pdelay_Req、Pdelay_Resp、Follow_Up、Delay_Resp、Pdelay_Resp_Follow_Up、Announce、Signaling

Transport specific

传输说明

Message type

报文类型

PTP version

PTP版本号

Message length

PTP报文长度

Domain number

PTP域号

Flag field

标志域

Correction field

校正域

Source clock ID

PTP报文源时钟节点编号

Source port number

PTP报文源端口号

Sequence number

序列号

Control field

控制域

Log message interval

报文发送间隔

Origin timestamp

报文发送时刻的原始时间戳

Current UTC offset

最优时钟的UTC时间相对于TAI时间的累计偏移量（单位为秒）

Grandmaster clock quality

最优时钟节点品质特性

Class

最优时钟的时间等级值

Accuracy

最优时钟的时间精度值

Offset (log variance)

最优时钟的偏差度量

Grandmaster priority1

最优时钟优先级一的值

Grandmaster priority2

最优时钟优先级二的值

Grandmaster ID

最优时钟节点编号

StepsRemoved

最优时钟到本时钟节点的跳数

Time source

最优时钟的属性值

Origin timestamp

报文发送时间戳

Precise origin timestamp

精准原始时间戳，为双步Sync报文发送时间

Receive timestamp

Delay_Req报文的接收时间

Requesting clock ID

请求发送方时钟节点编号

Requesting port number

请求的发送端口

Request receipt timestamp

Pdelay_Req报文的接收时间

Response origin timestamp

Pdelay_Resp报文的发送时间

Target clock ID

目的时钟节点编号

Target port number

目的端口号

TLV length field

TLV中长度字段的值

Interval request TLV

消息发送间隔请求TLV

Organization ID

组织ID

Organization subtype

组织自定义子类型

Link delay interval

请求Pdelay_Req报文的发送间隔

Time sync interval

请求Sync报文的发送间隔

Announce interval

请求Announce报文的发送间隔

Flags

附带标记位，包括是否需要计算链路延时和邻居频比

Follow_Up information TLV

Follow_Up 信息TLV

Cumulative scaled rate offset

与最优时钟的累计频率比偏差

GM timebase indicator

指示最优时钟时间基准是否发生变化

Last GM phase change

最优时钟最近一次相位变化值

Last GM frequency change

最优时钟最近一次频率变化值

【举例】

\# 在一台设备上启动PTP功能，打开PTP packet调试信息开关，配置设备的时钟节点类型，并在接口上使能PTP功能。

\<Sysname\> debugging ptp packet

\*{.TerminalDisplayChar}Jun 13 09:50:53 672 2011 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 sent an Announce packet with length 76.

Transport specific        : 0x1

Message type              : Announce

PTP version               : 2

Message length            : 76

Domain number             : 0

Flag field                : 0x0030

Correction field          : 0

Source clock ID           : 001122-FFFE-000001

Source port number        : 3

Sequence number           : 81

Control field             : 5

Log message interval      : 4

Origin timestamp          : 0

Current UTC offset        : 0

Grandmaster clock quality :

 Class                    : 248

 Accuracy                 : 254

 Offset (log variance)    : 16640

Grandmaster priority1     : 246

Grandmaster priority2     : 248

Grandmaster ID            : 001122-FFFE-000001

StepsRemoved              : 0

Time source               : 0xA0

*// 接口GigabitEthernet1/0/1发送Announce报文的具体内容，长度为76*

\*Jan 15 10:29:00:394 2013 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 sent a Sync packet with length 44.

Transport specific        : 0x0

Message type              : Sync

PTP version               : 2

Message length            : 44

Domain number             : 0

Flag field                : 0x0200

Correction field          : 0

Source clock ID           : 001122-FFFE-000001

Source port number        : 2

Sequence number           : 26888

Control field             : 0

Log message interval      : 1

Origin timestamp          : 0

*// 接口GigabitEthernet1/0/1发送Sync报文，长度为44*

\*Jan 10 16:34:49:973 2013 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 sent a Follow_Up packet with length 76.

Transport specific        : 0x1

Message type              : Follow_Up

PTP version               : 2

Message length            : 76

Domain number             : 0

Flag field                : 0x0000

Correction field          : 0

Source clock ID           : 001122-FFFE-000001

Source port number        : 2

Sequence number           : 26888

Control field             : 0

Log message interval      : 127

Precise origin timestamp  : 0

Follow_Up information TLV :

 TLV length field                : 28

 Organization ID                 : 00-80-C2

 Organization subtype            : 0x000001

 Cumulative scaled rate offset   : 0

 GM timebase indicator           : 0

 Last GM phase change            : 0x000000000000000000000000

 Last GM frequency change        : 0

*// 接口GigabitEthernet1/0/1发送到携带有Follow_Up Information TLV的Follow_Up报文，长度为76*

\*Jan 15 10:27:06:446 2013 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 received a Delay_Req packet with length 44.

Transport specific        : 0x0

Message type              : Delay_Req

PTP version               : 2

Message length            : 44

Domain number             : 0

Flag field                : 0x0000

Correction field          : 0

Source clock ID           : 001122-FFFE-000101

Source port number        : 2

Sequence number           : 6739

Control field             : 1

Log message interval      : 127

Origin timestamp          : 0

*// 接口GigabitEthernet1/0/1接收Delay_Req报文，长度为44*

\*Jan 15 10:27:06:449 2013 H3C PTP/7/PACKET: GigabitEthernet1/0/1 sent a Delay_Resp packet with length 54.

Transport specific        : 0x0

Message type              : Delay_Resp

PTP version               : 2

Message length            : 54

Domain number             : 0

Flag field                : 0x0000

Correction field          : 0

Source clock ID           : 001122-FFFE-000001

Source port number        : 2

Sequence number           : 6739

Control field             : 3

Log message interval      : 0

Receive timestamp         : 1358245669431425000

Requesting clock ID       : 001122-FFFE-000101

Requesting port number    : 2

*// 接口GigabitEthernet1/0/1发送Delay_Resp报文，长度为54*

\*Jan 15 10:32:58:485 2013 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 received a Pdelay_Req packet with length 54.

Transport specific        : 0x0

Message type              : Pdelay_Req

PTP version               : 2

Message length            : 54

Domain number             : 0

Flag field                : 0x0000

Correction field          : 0

Source clock ID           : 001122-FFFE-000001

Source port number        : 2

Sequence number           : 35181

Control field             : 5

Log message interval      : 127

Origin timestamp          : 0

*// 接口GigabitEthernet1/0/1接收Pdelay_Req报文，长度为54*

\*Jan 15 10:32:58:485 2013 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 sent a Pdelay_Resp packet with length 54.

Transport specific        : 0x0

Message type              : Pdelay_Resp

PTP version               : 2

Message length            : 54

Domain number             : 0

Flag field                : 0x0200

Correction field          : 0

Source clock ID           : 001122-FFFE-000101

Source port number        : 2

Sequence number           : 35181

Control field             : 5

Log message interval      : 127

Request receipt timestamp : 1358245978484598000

Requesting clock ID       : 001122-FFFE-000001

Requesting port number    : 2

*// 接口GigabitEthernet1/0/1发送Pdelay_Resp报文，长度为54*

\*Jan 15 10:32:58:486 2013 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 sent a Pdelay_Resp_Follow_Up packet with length 54.

Transport specific        : 0x0

Message type              : Pdelay_Resp_Follow_Up

PTP version               : 2

Message length            : 54

Domain number             : 0

Flag field                : 0x0000

Correction field          : 0

Source clock ID           : 001122-FFFE-000101

Source port number        : 2

Sequence number           : 35181

Control field             : 5

Log message interval      : 127

Response origin timestamp : 1358245978484598000

Requesting clock ID       : 001122-FFFE-000001

Requesting port number    : 2

*// 接口GigabitEthernet1/0/1发送Pdelay_Resp_Follow_Up报文，长度为54*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/PACKET: GigabitEthernet1/0/1 received a Signaling packet with length 60.

Transport specific        : 0x1

Message type              : Signaling

PTP version               : 2

Message length            : 60

Domain number             : 0

Flag field                : 0x0000

Correction field          : 0

Source clock ID           : 001122-FFFE-000101

Source port number        : 2

Sequence number           : 3

Control field             : 5

Log message interval      : 127

Target clock ID           : 000000-0000-000000

Target port number        : 255

Interval request TLV :

 TLV length field      : 12

 Organization ID       : 00-80-C2

 Organization subtype  : 0x000002

 Link delay interval   : -3

 Time sync interval    : -1

 Announce interval     : 0

 Flags                 : 0x0

*// 接口GigabitEthernet1/0/1接收携带有消息发送间隔请求TLV的Signaling报文，长度为60*

**PTP \-- PTP调试命令 \-- debugging ptp timer**

------------------------------------------------------------------------

【命令】

**[debugging ptp timer ** **interface** *interface-type* *interface-number* ]

**[undo debugging ptp timer ** **interface** *interface-type* *interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type* *interface-number*]：指定接口上的调试信息开关。*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，表示所有端口上的调试信息开关。

【描述】

**[debugging ptp timer**]命令用来打开PTP定时器调试信息开关。**undo debugging ptp timer**命令用来关闭PTP定时器调试信息开关。

缺省情况下，PTP定时器调试信息开关处于关闭状态。

表1-5 debugging ptp timer命令输出信息描述表

字段

描述

Timer for periodically sending *PacketType* packet was successfully created on *IfName,* timer ID was *TimerID.*

接口*IfName*创建*PacketType*报文发送定时器成功，*PacketType*包括Announce、PDelay_Req、Sync，timer ID 为*TimerID*

Timer destroyed for sending *PacketType* packet on *IfName*, timer ID was *TimerID*.

接口*IfName*删除*PacketType*报文发送定时器，*PacketType*包括Announce、PDelay_Req、Sync，timer ID 为*TimerID*

【举例】

\# 在一台设备上启动PTP功能，打开PTP定时器调试信息开关，配置设备的时钟节点类型，并在接口上使能PTP功能。

\<Sysname\> debugging ptp timer

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/TIMER: Timer for periodically sending Announce packet was successfully created on GigabitEthernet1/0/1，timer ID was 3.

*// 接口GigabitEthernet1/0/1创建Announce报文发送定时器*，*timer ID为3*

\*Jun 13 09:50:53 672 2011 Sysname PTP/7/TIMER: Timer destroyed for sending Announce packet on GigabitEthernet1/0/1, timer ID was 3.

*// 接口GigabitEthernet1/0/1删除Announce报文发送定时器，timer ID为3*
