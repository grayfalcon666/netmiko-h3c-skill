<!-- CMD-INDEX
  debugging mpls lsm                  | 用户视图             | L6
  debugging mpls packet               | 用户视图             | L452
-->

**MPLS基础 \-- MPLS基础调试命令 \-- debugging mpls lsm**

------------------------------------------------------------------------

【命令】

**[debugging mpls lsm **[{ **all** \| **error** \| **event** \| **fec** [ **asbr** \| **vpn-instance** *vpn-instance-name* ] { **ipv4** *destination mask* \| **ipv6** *destination mask* } \| **hsb** \| **label** \| **process** \| **tunnel** }]]

**[undo debugging mpls lsm**[ { **all** \| **error** \| **event** \| **fec** { **ipv4** \| **ipv6** } \| **hsb** \| **label** \| **process** \| **tunnel** }]]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[all**]：表示MPLS LSM所有调试信息开关。

**[error**]：表示MPLS LSM的错误调试信息开关。

**[event**]：表示MPLS LSM的事件调试信息开关。

**[fec**]：表示指定LSP的MPLS LSM调试信息开关。

**[asbr**]：表示指定ASBR LSP的MPLS LSM调试信息开关。

**[vpn-instance** *vpn-instance-name*]：表示指定VPN实例内LSP的MPLS LSM调试信息开关。*vpn-instance-name*表示VPN实例名称，为1～31字符的字符串，区分大小写。

**[ipv4 ***destination mask*]：表示指定FEC对应IPv4 LSP的MPLS LSM调试信息开关信息。*destination*为FEC的目的IPv4地址，*mask*为FEC目的IPv4地址的掩码，取值范围为0～32。

**[ipv6** *destination mask*]：表示指定FEC对应BGP-IPv6 LSP的MPLS LSM调试信息开关。*destination*为FEC的目的IPv6地址，*mask*为FEC目的IPv6地址的掩码，取值范围为0～128。

**[hsb**]：表示MPLS LSM热备份事件的调试信息开关。

**[label**]：表示MPLS LSM标签分配管理的调试信息开关。

**[tunnel**]：表示MPLS LSM隧道管理的调试信息开关。

**[process**]：表示MPLS LSM处理过程的调试信息开关。

【描述】

**[debugging mpls lsm**]命令用来打开MPLS LSM（Label Switch Management，标签交换管理）的调试信息开关。**undo debugging mpls lsm**命令用来关闭MPLS LSM的调试信息开关。

缺省情况下，所有MPLS LSM的调试信息开关均处于关闭状态。

需要注意的是：

·当LSM运行出现问题时，可以通过**debugging mpls lsm**命令进行故障定位。但这条命令的执行会影响系统性能，因此建议谨慎使用。

·执行**debugging mpls lsm all**命令可以打开除**fec**外所有的MPLS LSM调试信息开关；执行**undo debugging mpls lsm all**命令可以关闭包括**fec**在内的所有MPLS LSM调试开关。

表1-1 debugging mpls lsm error命令输出信息描述表

字段

描述

Failed to open the file

打开文件失败

Failed to write the file

写文件失败

Failed to download a configuration command

配置下发驱动失败

Failed to recover from binary configurations

二进制配置信息恢复失败

Failed to backup configurations in batches

配置批量备份失败

Invalid TLV

接收消息中存在无效TLV

Unknown signalling

非法信令类型

Unknown signalling message type

非法的信令消息类型

Failed to analyze the signalling message

解析信令消息失败

Received an invalid HA message

收到一个无效的HA消息

Invalid LSP index

无效的LSP索引值

Failed to allocate a NID

申请NID失败

Failed to set the NID

设置NID失败

Failed to free the NID

释放NID失败

Failed to update the LSP

更新LSP失败

Failed to add an FTN entry

添加FTN表项失败

Failed to add a cross-connected entry

添加XC表项失败

Failed to add all the LSPs

添加FEC下的所有等价LSP失败

Failed to send an LSP entry to TNLC when creating the LSP

向隧道管理通告LSP隧道表项失败

Failed to send an LSP entry to LFIB when creating the LSP

向LFIB下发LSP表项失败

Failed to send an LSP entry to HA when creating the LSP

LSP创建时向HA发送LSP表项失败

Failed to release the label

释放标签失败

Label *label* is in bad status, and a notification was sent to signaling *signal*

标签状态错误，发送通知信息给信令协议*signal*

**

表1-2 debugging mpls lsm event命令输出信息描述表

字段

描述

Received and processed an interface event. Interface index: *ifIndex*; event: *event*; result: *result*

收到并处理接口事件。接口索引为*ifIndex*；接口事件为*event*；处理结果为*result*

Notify interface management that the process of the event completed

通知接口管理事件处理完成

VRF added successfully

添加VRF成功

VRF deleted successfully

删除VRF成功

Application *applicationID* session event: Received an init message

应用*applicationID*的会话事件：收到初始化消息

Application *applicationID* session event: Recovery completed

应用*applicationID*的会话事件：恢复完成

Application session event: LIPC down

应用会话事件：进程间通信连接断开

表1-3 debugging mpls lsm hsb命令输出信息描述表

字段

描述

Sent an HA message. Message type: *messageType*, length: *length*

发送备份消息，消息类型为*messageType*，消息长度为*length*

Received an HA message. Message type: *messageType*, length: *length*

收到备份消息，消息类型为*messageType*，消息长度为*length*

表1-4 debugging mpls lsm label命令输出信息描述表

字段

描述

Label *label* released successfully

成功释放标签

Label segment is available

标签段可用

Claim label *label*

申请指定标签

Refresh label *label*, signalling *signal*

刷新标签*label*，信令协议为*signal*

表1-5 debugging mpls lsm tunnel命令输出信息描述表

字段

描述

Fetch the tunnels. Destination: *destAddr*, ECMP number: *number*

获取到目的地址*destAddr*的隧道，等价隧道数目为*number*

Notify the status event (*event*) of tunnel with destination *destAddr* to application *applicationID*

向应用*applicationID*通告隧道状态变化事件，隧道目的地址为*destAddr，*隧道状态变化事件包括：

·1：隧道增加

·2：隧道删除

·3：隧道更新

Notify the status event (*event*) of tunnel policy (*policyName*) to application *applicationID*

向应用*applicationID*通告隧道策略变化事件。隧道策略名称为*policyName*，隧道策略变化事件包括：

·1：策略增加

·2：策略删除

·3：策略更新

Process LSP message. Destination: *destAddr*, Tunnel ifindex:*interfaceIndex*, event type: *event*, result: *result*.

处理LSP隧道消息。隧道目的地址为*destAddr*，隧道接口索引为*interfaceIndex*，事件类型为*event*，处理结果为*result*

TNLC received an LSP message. Destination: *destAddr*, event type: *event*, ECMP number: *number*.

隧道控制模块收到LSP隧道消息，隧道目的地址为*destAddr*，事件类型为*event*，等价隧道数目为*number*

表1-6 debugging mpls lsm process命令输出信息描述表

字段

描述

Configuration commands applied to drive successfully

成功下发配置命令到驱动

Allocate a NID successfully

成功申请NID

Set the NID successfully

成功设置NID

Release the NID successfully

成功释放NID

LSP updated successfully. XC index: *XcIndex*, Inseg index: *InSegmentIndex*, Outseg index: *OutSegmentIndex*, FTN index: *FtnIndex*, Serve FLag: *ServeFlag*.

成功更新LSP信息。XC索引为*XcIndex*，入方向索引为*InSegmentIndex*，出方向索引为*OutSegmentIndex*，FTN索引为*FtnIndex*，统计使能标记为*ServeFlag*

LSP added successfully. XC index: *XcIndex*, Inseg index: *InSegmentIndex*, Outseg index: *OutSegmentIndex*, FTN index: *FtnIndex*, Serve FLag: *ServeFlag*.

成功添加LSP信息。XC索引为*XcIndex*，入方向索引为*InSegmentIndex*，出方向索引为*OutSegmentIndex*，FTN索引为*FtnIndex*，统计使能标记为*ServeFlag*

LSP deleted successfully. XC index: *XcIndex*, Inseg index: *InSegmentIndex*, Outseg index: *OutSegmentIndex*, FTN index: *FtnIndex*

成功删除LSP信息。XC索引为*XcIndex*，入方向索引为*InSegmentIndex*，出方向索引为*OutSegmentIndex*，FTN索引为*FtnIndex*

Slave: Fill the LSP table. Version: *EntryVersion*, Flag: *LspFlag*, SigID: *LsmSig*, FEC info: type *type*, ip address *address*, mask length *length*, vrf index *index*, Inseg: in-label *InLabel*, in-ifindex *ifIndex*, ECMP: *OutSegNum*

备进程填充LSP表项。版本号为*EntryVersion*，LSP操作标记为*LspFlag*，信令协议类型为*LsmSig*

FEC信息：FEC类型为*type*，FEC目的地址为*address*，目的地址掩码为*length*，FEC所属VPN的索引为*index*

入方向信息：入标签为*InLabel*，入接口为*ifIndex*

等价数目为*OutSegNum*

Master: Fill the LSP table. Version: *EntryVersion*, Flag: *LspFlag*, SigID: *LsmSig*, FEC info: type *type*, ip address *address*, mask length *length*, vrf index *index*, Inseg: in-label *InLabel*, in-ifindex *ifIndex*, ECMP: *OutSegNum*

主进程填充LSP表项。版本号为*EntryVersion*，LSP操作标记为*LspFlag*，信令协议类型为*LsmSig*

FEC信息：FEC类型为*type*，FEC目的地址为*address*，目的地址掩码为*length*，FEC所属VPN的索引为*index*

入方向信息：入标签为*InLabel*，入接口为*ifIndex*

等价数目为*OutSegNum*

Outseg info: type *OutType*, out-ifindex *ifIndex*, next-hop *IpAddr*, out-label *OutLabel*, outgoing NID *OutgoingNid*, TPID *TPID*, backup out-ifindex *ifIndexFrr*

处理的LSP表项的出方向信息。类型为*OutType，*出接口为*ifIndex，*下一跳为*IpAddr*，出标签为*OutLabel*，出方向NID为*OutgoingNid*，策略ID为*TPID*，备份出接口为*ifIndexFrr*

ILM downloading. Operation: *OperType*, in-label: *InLabel*, length: *length*

下发ILM表项：操作类型为*OperType*，入标签为*InLabel*，长度为*length*

NHLFE downloading. Operation: *OperType*, NID: *nid*, length: *length*

下发NHLFE表项：操作类型为*OperType*，NID为*nid*，长度为*length*

【举例】

\# 打开MPLS LSM的事件调试信息开关。断开L3VPN应用与LSM的连接，并重建该连接时，打印如下信息。

\<Sysname\> debugging mpls lsm event

\*May 12 06:34:53:514 2010 Sysname LSM/7/EVENT:

Application session event: LIPC down.

*// 应用连接断开*

\*May 12 06:35:00:116 2010 Sysname LSM/7/EVENT:

Application 2 session event: Received an init message.

*// 收到连接初始化消息*

\*May 12 06:35:00:117 2010 Sysname LSM/7/EVENT:

Application 2 session event: Recover completed.

*[//*]*连接恢复完成*

\# 打开MPLS LSM的错误调试信息开关。当标签1024已经被使用的情况下，新创建LSP重复使用1024标签时，打印如下信息。

\<Sysname\> debugging mpls lsm error

\*May 12 09:02:25:795 2010 Sysname LSM/7/ERROR:

Label 1024 is in bad status, and a notification was sent to signaling 3.

*// 标签冲突，通知信令LSP处理失败。*

\# 打开MPLS LSM的热备份事件调试信息开关。发送一条实时备份消息时，打印如下信息。

\<Sysname\> debugging mpls lsm hsb

\*May 7 17:33:22:796 2010 Sysname LSM/7/HSB:

Sent an HA message. Message type: 1, length: 80. 

*// 发送备份消息*

\# 打开MPLS LSM的标签分配管理调试信息开关。申请指定标签时，打印如下信息。

\<Sysname\> debugging mpls lsm label

\*May 12 09:11:17:560 2010 Sysname LSM/7/LABEL:

Claim label 1025, result 0.

*// 成功申请标签1025*

\# 打开MPLS LSM的隧道管理调试信息开关。处理并生成一条LSP隧道时，打印如下信息。

\<Sysname\> debugging mpls lsm tunnel

\*May 7 14:51:51:08 2010 Sysname LSM/7/TUNNEL:

TNLC received an LSP message. Destination: 0xdedee9e9, event type: 1, ECMP number:

1.

*// 隧道控制模块收到LSP隧道消息*

\*May 7 14:51:51:13 2010 Sysname LSM/7/TUNNEL:

Notify the status event (1) of tunnel with destination dedee9e9 to application 1

*// 通告隧道状态变化事件*

\*May  7 14:51:51:15 2010 Sysname LSM/7/TUNNEL:

Process LSP message. Destination: 0xdedee9e9, Tunnel ifindex :0, event type: 1,

result: 0. 

*// 处理LSP隧道消息的结果*

\# 打开MPLS LSM的处理过程调试信息开关。处理并生成一条LSP表项时，打印如下信息。

\<Sysname\> debugging mpls lsm process

\*May 12 09:20:58:749 2010 Sysname LSM/7/PROCESS:

Master: Fill the LSP table. Version: 0, Flag: 0x18, SigID: 3, FEC info: type 17, ip address 1.1.1.1, mask length 32, vrf index 0, Inseg: in-label 1028, in-ifindex

 136479, ECMP: 1.

*// 处理的LSP消息的FEC和入方向信息*

\*May 12 09:20:58:752 2010 Sysname LSM/7/PROCESS:

Outseg info: type 65, out-ifindex 136479, next-hop 12.12.12.2, out-label 1025, outgoing NID 4294967295, TPID 65535, backup out-ifindex 0.

*// 处理的LSP消息出方向信息*

\*May 12 09:20:58:754 2010 Sysname LSM/7/PROCESS:

LSP updated successfully. XC index: 2, Inseg index: 3, Outseg index: 2, FTN index: 2, Serve FLag:0x1.

*[// LSP*]*表项更新成功*

\*May 12 09:20:58:765 2010 Sysname LSM/7/PROCESS:

NHLFE downloading. Operation: 5, NID: 2049, result: 0.

*// 下发NHLFE表项*

\*May 12 09:20:58:765 2010 Sysname LSM/7/PROCESS:

ILM downloading. Operation: 1, in-label: 1025, result: 0.

*// 下发ILM表项*

**MPLS基础 \-- MPLS基础调试命令 \-- debugging mpls packet**

------------------------------------------------------------------------

【命令】

**[debugging mpls packet**[ [ **acl** *acl-number* \| **acl6** *acl6-number* ]  **inlabel** *outer-in-label* [ *inner-in-label*  ] ]]

**[undo debugging mpls packet**]

【视图】

用户视图

【缺省级别】

1：监控级

【参数】

**[acl*** acl-number*]：输出符合ACL匹配条件的MPLS报文的调试信息, *acl-number*为高级访问控制列表号，取值范围为3000～3999。

**[acl6 ***acl6-number*]：输出符合IPv6 ACL匹配条件的MPLS报文的调试信息，*acl6-number*为高级访问控制列表号，取值范围为3000～3999。

**[inlabel**]：输出具有指定入标签值的MPLS报文的调试信息。

*[outer-in-label*]：外层入标签，取值范围为0～1048575。

*[inner-in-label*]：内层入标签，取值范围为0～1048575。

【描述】

**[debugging mpls packet**]命令用来打开MPLS报文转发调试信息开关。**undo debugging mpls packet**命令用来关闭MPLS报文转发调试信息开关。

缺省情况下，MPLS报文转发调试信息开关处于关闭状态。

表1-7 {.TableTextChar}[debugging mpls packet]{.TableTextChar}命令输出信息描述表{.TableTextChar}

字段

描述

MPLS Input

收到MPLS报文

MPLS Forward

转发MPLS报文

MPLS Output

发送MPLS报文

Receiving from interface *interface-name*

从接口*interface-name*收到数据包

Sending to interface *interface-name*

发送数据包到接口*interface-name*

Label(s)

标签（包括私网内层标签和公网外层标签）

EXP

MPLS报文的EXP值

TTL

MPLS报文的TTL值

*[Operation* Label]

标签操作（如POP、PUSH、SWAP等）

PktLen

数据包的长度

MPLS send result *result*

MPLS报文发送结果，0表示发送成功，其它表示失败

AF

地址族类型

{.TableTextChar}

【举例】

\# 在设备上打开MPLS的报文调试信息开关，当网络中存在MPLS流量时，设备上将打印如下调试信息。

\<PE1\> debugging mpls packet

\*Oct 19 09:13:03:979 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;

MPLS Input: Receiving from interface GE1/0/1, PktLen=70, Label(s)=1025, EXP=4, TTL=3.

*// 接收到MPLS报文：接收报文的接口为GE1/0/1，报文长度为70字节，入标签为1025，EXP为4，TTL为3*

\*Oct 19 09:13:03:980 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;

POP Label=1025, EXP=4, TTL=3

*// 弹出标签，标签为1025，EXP为4，TTL为3*

\*Oct 19 09:13:03:980 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;

PUSH Label=2025, EXP=4, TTL=2

*// 压入标签，标签为2025，EXP为4，TTL为2*

\*Oct 19 09:13:03:980 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;

MPLS Output: Sending to interface GE1/0/2, PktLen=70, Label(s)=2025, EXP=4, TTL=2.

*// 发送MPLS报文：发送报文的接口为GE1/0/2，报文的出标签为2025，EXP为4，TTL为2*

\*Oct 19 09:13:03:981 2010 PE1 MPLSFW/7/MPLSFW:Slot=2;

MPLS send result 0.

*[// MPLS*]*报文发送成功*

