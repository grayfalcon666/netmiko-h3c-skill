
**EVB \-- EVB调试命令 \-- debugging evb**

------------------------------------------------------------------------

【命令】

**[debugging evb** **[all**[ \| **error**]****[\| ]**event**[ \| **packet** [ **verbose** ]  **interface** *interface-type* *channel-id* }  }]

**[undo debugging evb** **[all**[ \| **error**]****[\| ]**event**[ \| **packet** [ **verbose** ]  **interface** *interface-type* *channel-id* } }]

【视图】]

用户视图]

【缺省用户角色】]

network-admin]

mdc-admin

【参数】

**[all**]：表示EVB所有调试信息开关。

**[error**]：表示EVB错误调试信息开关。

**[event**]：表示EVB事件调试信息开关。

**[packet**]：表示EVB协议报文调试信息开关。

**[verbose**]：表示EVB协议报文详细信息调试开关。若未指定本参数，表示EVB协议报文摘要信息调试开关。

**[interface*** interface-type *]*[interface-number*[ \| *interface-number*:*channel-id* }]：指定二层以太网接口、二层聚合接口、S通道接口或S通道聚合接口。其中，*interface-type*为接口类型，*interface-number*为接口编号，*channel-id*为S通道的编号。对于二层以太网接口和二层聚合接口，接口编号为*interface-number*的形式；对于S通道接口和S通道聚合接口，接口编号为*interface-number*:*channel-id*的形式。如果未指定本参数，表示所有接口。

【描述】]

**[debugging evb**]命令用来打开EVB调试信息开关。**undo debugging evb**命令用来关闭EVB调试信息开关。

缺省情况下，EVB调试信息开关处于关闭状态。

表1-1 debugging evb error命令输出信息描述表

字段

描述

The role value of received CDCP packet on phyport *IfName* is illegal.

接口*IfName*收到的远端CDCP报文的角色值非法

The channel capability value of received CDCP packet on phyport *IfName* is illegal.

接口*IfName*收到的远端CDCP报文的能力值非法

The SCID *SCID* SVID *SVID* in received CDCP packet is illegal.

接口*IfName*收到的远端CDCP报文的SCID和SVID非法

The first SCID/SVID info is not the default S-Channel.

第一个SCID/SVID对不是默认的S通道

The length of received CDCP packet on phyport *IfName* is less than 7 bytes.

接口*IfName*收到的CDCP报文长度小于7字节

Phyport *IfName* found that EVB is disabled after analyzing a received CDCP packet.

接口*IfName*在解析收到的CDCP报文后，发现EVB未使能

EVB is disabled on phyport *IfName* that received a CDCP packet.

接收CDCP报文的接口*IfName*未使能EVB

The port *IfName* that received a CDCP packet is not a L2-phyport.

接收CDCP报文的接口*IfName*不是二层物理接口

The length of EVB TLV received on S-Channel port *IfName* is illegal.

接口*IfName*收到的EVB TLV的长度非法

The *IfName* of EVB TLV received on S-Channel port *IfName* is illegal.

接收EVB TLV的S通道接口*IfName*非法

The MODE value of EVB TLV received on S-Channel port *IfName* is illegal.

接口*IfName*收到的EVB TLV的模式非法

Failed to negotiate according to EVB TLV packet received on S-Channel port *IfName*.

根据S通道接口*IfName*收到的EVB TLV协商运行值失败

Failed to send EVB message to LLDP.

向LLDP进程发送EVB消息失败

Invalid VDP packet on interface *IfName* with invalid filter format or instanceId format.

接口*IfName*收到的VDP报文中，过滤信息格式或实例ID格式非法

Process an invalid packet on interface *IfName* without filter info.

接口*IfName*处理没有过滤信息的非法报文

VDP packet on interface *IfName*, length of filter information is inconsistent with filter format and number.

接口*IfName*收到的VDP报文中，过滤信息长度与过滤的格式与个数冲突

Received a VDP packet on interface *IfName* with VLAN 0 in filter, but number of filters is not 1.

接口*ifName*收到VDP报文中，过滤信息VLAN为0，但过滤信息的个数不为1

The new VDP request packet not consistent with the last one.

新的VDP请求报文与上一次的冲突

Received a packet on interface *IfName* with invalid VDP TLV type.

接口*IfName*接收的报文的TLV类型非法

Received a VDP packet on interface *IfName* with invalid length *length*.

接口*IfName*接收的VDP报文长度非法

Failed to process de-association packet on interface *IfName*, because managerid is different from associate request.

接口*IfName*处理去关联报文失败，因为管理地址与关联请求时不同

Failed to process VDP packet on interface *IfName* for invlaid managerID TLV.

处理接口*IfName*收到的VDP报文失败，管理地址TLV非法

Received a VDP packet with invalid MAC in filter information.

接收的VDP报文，过滤信息中MAC非法

Received a VDP packet with invalid instance ID of MAC format.

接收的VDP报文中MAC格式的实例ID非法

No manager address to use.

无管理地址可以使用

Req/Ack bit is not 0 in VDP request packet on interface *IfName*.

接口*IfName*接收的VDP请求报文的请求/应答位不是0

There are not enough resources to create S-Channel with SCID *SCID* on phyport *IfName*.

在物理口*IfName*上没有足够资源创建S通道接口，其SCID为*SCID*

表1-2 debugging evb event命令输出信息描述表

字段

描述

The server port connected to phyport *IfName* that received a CDCP packet does not support s-component.

与收到CDCP报文的物理口*IfName*相连的服务器的接口不支持S组件

CDCP packet received on phyport *IfName* has only default S-Channel.

接口*IfName*收到的CDCP报文中只有缺省S通道

CDCP packet received on phyport *IfName* has a remaining length less than the SCID/SVID pair.

接口*IfName*收到的CDCP报文中剩余长度小于SCID/SVID长度

Number of S-Channels supported by the remote end is less than that in the CDCP packet received on phyport *IfName*.

远端支持的S通道个数少于接口*IfName*收到的CDCP报文中S通道个数

The request url of online is: *string.*

向iMC发送的VSI上线URL信息

The request url of offline is: *string.*

向iMC发送的VSI下线URL信息

Received a de-association packet on interface *IfName* but the VSI does not exist.

在接口*IfName*上收到去关联报文，但VSI接口不存在

Successfully get the managerid TLV on interface *IfName*.

接口*IfName*解析到合法的管理地址TLV

Received a VDP packet on interface *IfName* with type *type*.

接口*IfName*收到*type*类型的VDP报文

Received an ACK or invalid packet through by ECP on interface *IfName*.

接口*IfName*通过ECP收到ACK或者非法报文

Received a VDP packet with VLAN 0 in filter information.

收到的VDP报文中，过滤信息中VLAN为0

Create VSI by local server manager.

本地创建VSI

Delete VSI by local server manager.

本地删除VSI

Current VSI status is waiting; delete VSI for reason *reason*.

VSI当前状态为waiting，删除VSI的原因为*reason*

VSI *IfName* status changed into *Pre-Association/ Association.*

VSI关联状态切换

Current VSI status is pre-association; delete VSI for reason *reason.*

VSI当前状态为预关联，删除VSI的原因为*reason*

VSI successfully sent a request to and received a response from iMC to get online.

VSI上线，向iMC发送请求并接收回应成功

VSI successfully sent a request to and received a response from iMC to get offline.

VSI下线，向iMC发送请求并接收回应成功

表1-3 debugging evb packet命令输出信息描述表

字段

描述

*[PacketType* packet received on interface *IfName* with length *length*]

接口*IfName*收到类型为*PacketType*、长度为*length*的报文

*[PacketType*]的取值为：

·CDCP：表示CDCP协议报文

·EVB TLV：表示EVB TLV协议报文

·VDP：表示VDP协议报文

*[PacketType* packet sent on interface *IfName* with *length*]

接口*IfName*发送类型为*PacketType*、长度为*length*的报文

*[PacketType*]的取值为：

·CDCP：表示CDCP协议报文

·EVB TLV：表示EVB TLV协议报文

·VDP：表示VDP协议报文

【举例】

\# 打开EVB事件调试信息开关。

\<Sysname\> debugging evb event

\*Mar  6 22:33:50:188 2012 Sysname EVB/7/Event: -MDC=1; The request url of online is:http://[1122:3344:5566:7788:9900:AABB:CCDD:EEFF:8080/evb/vdp/profile?vsi_inst=11:2233:4455:6677:8899:1234:5678:9010&vsi_type=100&vsi_ver=0&vlan_mac=1000_0022-3344-5566&schannel=S-Channel1/0/1/3:2&vsi_local_id=0&pre-associate=0.]

*// 向VSI管理服务器发送上线请求的URL信息*

\*Mar  6 22:33:50:187 2012 Sysname EVB/7/Event: -MDC=1; Received a VDP packet on interface S-Channe1/0/1:10 with type 3.

*// 在S通道接口S-Channel1*/0*/1:10**上收到类型为3的VDP报文*

\# 在端口GigabitEthernet1/0/1上使能EVB功能，创建S通道，并打开EVB协议报文详细调试信息开关。

\<Sysname\> debugging evb packet verbose

Dec 19 05:31:38:033 2011 Sysname EVB/7/Packet: -MDC=1; VDP packet received on interface S-Channe1/0/1:10 with length 57:

10 01 00 02 0a 10 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 04 21 04 00 00 64 00 02 00 11

22 33 44 55 66 77 88 99 12 34 56 78 90 10 02 00

01 00 11 22 33 44 55 03 e8

*// 在S通道接口S-Channel1*/0*/1:10**上收到长度为57的VDP报文*

\*Dec 19 05:31:38:048 2011 Sysname EVB/7/Packet: -MDC=1; VDP packet sent on interface S-Channe1/0/1:10 with length 53:

0a 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 04 21 00 00 00 64 00 02 00 11 22 33 44 55

66 77 88 99 12 34 56 78 90 10 02 00 01 00 11 22

33 44 55 03 e8

*// 通过S通道接口S-Channel1*/0*/1:10**发送长度为53的VDP报文*

\*Dec 19 05:35:53:692 2011 Sysname EVB/7/Packet: -MDC=1; CDCP packet received on interface GigabitEthernet1/0/1 with length 25:

98 00 00 a7 00 10 01 00 20 02 00 30 00 00 40 04

00 60 00 00 a0 0a 00 b0 00

\*Dec 19 05:38:20:119 2011 Sysname EVB/7/Packet: -MDC=1; CDCP packet sent on interface GigabitEthernet1/0/1 with length 19:

18 00 00 a7 00 10 01 00 20 02 00 30 03 00 a0 0a

00 b0 06

*// 本地物理端口GigabitEthernet1/0/1上的信息变化时，向LLDP进程同步信息*

\*Dec 19 05:39:02:788 2011 Sysname EVB/7/Packet: -MDC=1; EVB TLV packet received on interface S-Channe1/0/1:10 with length 5:

00 07 b4 91 17

*// 在S通道接口S-Channel1*/0*/1:10**上收到长度为5的EVB TLV*

\*Dec 19 05:45:33:257 2011 Sysname EVB/7/Packet: -MDC=1; EVB TLV packet sent on interface S-Channe1/0/1:10 with length 5:

03 07 b4 54 14

*// 通过S通道接口S-Channel1*/0*/1:10**发送长度为5的EVB TLV给LLDP*
