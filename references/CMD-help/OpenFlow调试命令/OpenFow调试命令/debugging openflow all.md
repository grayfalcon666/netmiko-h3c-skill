<!-- CMD-INDEX
  debugging openflow all              | 用户视图             | L8
  debugging openflow error            | 用户视图             | L44
  debugging openflow event            | 用户视图             | L106
  debugging openflow packet           | 用户视图             | L184
-->

**OpenFlow调试命令 \-- OpenFow调试命令 \-- debugging openflow all**

------------------------------------------------------------------------

【命令】

**[debugging openflow all**]

**[undo debugging openflow all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging openflow all**]命令用来打开OpenFlow所有调试信息开关。**undo debugging openflow all**命令用来关闭OpenFlow所有调试信息开关。

缺省情况下，OpenFlow所有调试信息开关处于关闭状态。

【举例】

\# 打开OpenFlow所有调试信息开关。

\<Sysname\> debugging openflow all

**OpenFlow调试命令 \-- OpenFow调试命令 \-- debugging openflow error**

------------------------------------------------------------------------

【命令】

**[debugging openflow error**]

**[undo debugging openflow error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging openflow error**]命令用来打开OpenFlow错误调试信息开关。**undo debugging openflow error**命令用来关闭OpenFlow错误调试信息开关。

缺省情况下，OpenFlow错误调试信息开关处于关闭状态。

表1-1 debugging openflow error命令输出信息描述表

字段

描述

Instance *instance-id* Controller *controller-id* send a illegal packet.

实例下的控制器发送一个非法报文

Instance *instance-id* Controller *controller-id* receive a illegal packet.

实例下的控制器收到一个非法报文

Set mac-learning failed under vlan *vlan-id* in instance *instance-id*

设置实例下VLAN的动态MAC学习失败

Set mac-learning forbidden failed under vlan vlan-id in instance *instance-id*

禁止实例下VLAN的动态MAC学习失败

【举例】

\# 打开OpenFlow错误调试信息开关。

\<Sysname\> debugging openflow error

\<Sysname\> \*Jan 17 21:59:49:951 2011 Sysname OFP/7/ERROR: Instance 1 Controller 0 receive a illegal packet.

*// 实例1控制器0接收到一个OpenFlow协议报文，消息格式错误*

**OpenFlow调试命令 \-- OpenFow调试命令 \-- debugging openflow event**

------------------------------------------------------------------------

【命令】

**[debugging openflow event**]

**[undo debugging openflow event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging openflow event**]命令用来打开OpenFlow事件调试信息开关。**undo debugging openflow event**命令用来关闭OpenFlow事件调试信息开关。

缺省情况下，OpenFlow事件调试信息开关处于关闭状态。

表1-2 debugging openflow event命令输出信息描述表

字段

描述

Openflow instance *instance-id* table *table-id* add flow entry *rule-id*.

成功添加一条流表项

Openflow instance *instance-id* table *table-id* add table miss flow entry.

成功添加一条Table Miss表项

Openflow instance *instance-id* add meter entry *meter-id*.

成功添加一条Meter表项

Openflow instance *instance-id* add group entry *group-id.*

成功添加一条Group表项

【举例】

\# 打开OpenFlow事件调试信息开关。

\<Sysname\> debugging openflow event

\<Sysname\> \*Sep  5 11:06:02:834 2013 Sysname OFP/7/EVENT: -MDC=1; Openflow instance 1 table 0 add table miss flow entry.

*// 实例1的表0成功添加一条Table Miss表项*

\<Sysname\> \*Sep  5 11:08:15:455 2013 Sysname OFP/7/EVENT: -MDC=1; Openflow instance 1 table 0 add flow entry 1.

*// 实例1的表0成功添加一条流表项*

\<Sysname\> \*Sep  5 11:12:10:934 2013 Sysname OFP/7/EVENT: -MDC=1; Openflow instance 1 add meter

 entry 1.

*// 实例1的表0成功添加一条Meter表项*

\<Sysname\> \*Sep  5 11:11:05:489 2013 Sysname OFP/7/EVENT: -MDC=1; Openflow instance 1 add group

 entry 1.

*// 实例1的表0成功添加一条Group表项*

**OpenFlow调试命令 \-- OpenFow调试命令 \-- debugging openflow packet**

------------------------------------------------------------------------

【命令】

**[debugging openflow packet instance ***instance-id ***controller*** controller-id*]

**[undo debugging openflow packet instance ***instance-id ***controller*** controller-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：OpenFlow实例号，取值范围为1～4097。

*[controller-id*]：控制器的ID号，取值范围为0～63。

【描述】

**[debugging openflow packet**]命令用来打开OpenFlow报文调试信息开关。**undo debugging openflow packet**命令用来关闭OpenFlow报文调试信息开关。

缺省情况下，OpenFlow报文调试信息开关处于关闭状态。

表1-3 debugging openflow packet命令输出信息描述表

字段

描述

instance-id

实例ID

controller-id

控制器ID

Version

协议版本

Type

报文类型：

·*hello*：表示OFPT_HELLO

·*error*：表示OFPT_ERROR

·*echo req*：表示OFPT_ECHO_REQUEST

·*echo rep*：表示OFPT_ECHO_REPLY

·*feature req*：表示OFPT_FEATURE_REQUEST

·*feature rep*：表示OFPT_FEATURE_REPLY

·*get cfg req*：表示OFPT_GET_CONFIG\_ reqUEST

·*get cfg rep*：表示OFPT_GET_CONFIG_REPLY

·*set cfg*：表示OFPT_SET_CONFIG

·*pktin*：表示OFPT_PAKCET_IN

·*flow rmv*：表示OFPT_FLOW_REMOVED

·*port stat*：表示OFPT_PORT_STATUS

·*pktout*：表示OFPT_PACKET_OUT

·*flow mod*：表示OFPT_FLOW_MOD

·*group mod*：表示OFPT_GROUP_MOD

·*port mod*：表示OFPT_PORT_MOD

·*table mod*：表示OFPT_TABLE_MOD

·*multi req*：表示OFPT_MULTIPART_REQUEST

·*multi rep*：表示OFPT_MULTIPART_REPLY

·*barrier req*：表示OFPT_BARRIER_REQUEST

·*barrier rep*：表示OFPT_BARRIER_REPLY

·*queue get cfg req*：表示OFPT_QUEUE_GET_CONFIG_REQUEST

·*queue get cfg rep*：表示OFPT_QUEUE_GET_CONFIG_REPLY

·*role req*：表示OFPT_ROLE_REQUEST

·*role rep*：表示OFPT_ROLE_REPLY

·*get async req*：表示OFPT_GET_ASYNC_REQUEST

·*get async rep*：表示OFPT_GET_ASYNC_REPLY

·*set async req*：表示OFPT_SET_ASYNC

·*mete rmod*：表示OFPT_METER_MOD

Length

报文长度

Xid

分配给该报文的处理ID

Hello

Hello报文中携带的信息：

·Element Type：Element的类型

·Version：Element为bitmap时表示的版本ID

Error

Error报文中携带的信息：

·Type：错误报文的类型

·Code：错误码

·Extra Data：错误报文附带的信息

Features Reply

Features Reply报文中携带的信息：

·Datapath ID：设备的Datapath ID

·Buffers：实例下可缓存的报文数目

·Auxiliary ID：辅助连接ID

·Capabilities：设备能力集

Config Reply

Get Confing Reply报文中携带的信息：

·flags：设备属性

·Miss Send Length：packet in上送的报文最大长度

Set Config Reply

Set Confing Reply报文中携带的信息：

·flags：设备属性

·Miss Send Length：packet in上送的报文最大长度

Packet in

Packet in报文中携带的信息：

·Reason： packet in的原因

·table id：匹配packet in报文的table

·bufid：缓存packet in报文的buffer ID

·cookie：流表项的cookie

·Match Type：Match的类型

·Match Length：Match域的长度

·Match Field：Match域

·Packet Data：packet in的报文内容

Flow Mod

Flow Mod报文中携带的信息：

·Cookie：流表项cookie

·CookieMask：流表项cookie mask

·TableId：流表项属于的table ID

·Command：flow mod类型

·IdleTime：流表项的idle time超时时间，单位为秒，0代表永不超时。如果idle time超时时间内没有数据流匹配到该流表项，该流表项被清除

·HardTime：流表项的hard time超时时间，单位为秒，0代表永不超时。当定时器超时后就清除该流表项，无论该流表项是否匹配到数据流

·Priority：优先级

·BufferId：流表项对应buffer ID

·Outport：流表项匹配出端口

·Outgroup：流表项匹配group

·Match Type：match域类型

·Match Length：match域长度

·Match Field：match域

·Instruction Type：Instruction类型

·Action：Action内容

Group Mod

Group Mod报文中携带的信息：

·Group id：group标识

·command：group mod的类型

·type：group类型

·Bucket：group中的动作集

Port Mod

Port Mod报文中携带的信息：

·Port：端口索引

·Config：端口配置

·Adv：端口建议配置

·Mac addr：端口MAC地址

Table Mod

Table Mod报文中携带的信息：

·Table id：表ID

·Config：表配置

Multipart Description Request

Multipart Description Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

Multipart Flow Request

Multipart Flow Request报文中携带的信息：

· Type：Multipart报文类型

·Flags：Multipart报文标记

·Cookie：流表项cookie

·CookieMask：流表项cookie mask

·TableId：流表项属于的table ID

·Outport：流表项匹配出端口

·Outgroup：流表项匹配group

·Match Type：match域类型

·Match Length：match域长度

·Match Field：match域

Multipart Agg Request

Multipart Agg Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Cookie：流表项cookie

·CookieMask：流表项cookie mask

·TableId：流表项属于的table ID

·Outport：流表项匹配出端口

·Outgroup：流表项匹配group

·Match Type：match域类型

·Match Length：match域长度

·Match Field：match域

Multipart Table Request

Multipart Table Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

Multipart Port Stats Request

Multipart Port Stats Request报文中携带的信息：

· Type：Multipart报文类型

· Flags：Multipart报文标记

· Port no：端口索引

Multipart Queue Request

Multipart Queue Request报文中携带的信息：

· Type：Multipart报文类型

· Flags：Multipart报文标记

· Port no：端口索引

·Queue id：队列索引

Multipart Group Request

Multipart Group Request报文中携带的信息：

· Type：Multipart报文类型

· Flags：Multipart报文标记

Multipart Group Description Request

Multipart Group Description Request报文中携带的信息：

· Type：Multipart报文类型

· Flags：Multipart报文标记

Multipart Group Features Request

Multipart Group Features Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

Multipart Meter Request

Multipart Meter Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

Multipart Meter Config Request

Multipart Meter Config Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

Multipart Meter Features Request

Multipart Meter Features Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

Multipart Table Features Request

Multipart Table Features Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Table ID：表ID

·Config：表的配置

·Max Entries：流表项最大数目

·Name：表名字

·MetaDataMatch：匹配的metadata取值范围

·MetaDataWrite：写入的metadata取值范围

·Prop type：Property类型

Multipart Port Description Request

Multipart Port Description Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

Multipart Description Reply

Multipart Description Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·DpDesc：连接描述信息

·HWDesc：设备硬件描述信息

·SWDesc：设备软件描述信息

·MFRDesc：生产商描述信息

·SerialNum：序列号描述信息

Multipart Flow Reply

Multipart Flow Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Cookie：流表项cookie

·TableId：流表项属于的table ID

·DurSec：流表项持续秒数

·DurnSec：流表项持续微秒数

·Packet count：流表项匹配报文计数

·Byte count：流表项匹配字节计数

·Match Type：match域类型

·Match Length：match域长度

·Match Field：match域

Multipart Agg Reply

Multipart Agg Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Packet count：流表项匹配报文计数

·Byte count：流表项匹配字节计数

·Flow count：流表项个数

Multipart Table Reply

Multipart Table Reply报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Table ID：表ID

·Active Count：当前处于激活状态的表个数

·LookUp Count：流表查询次数

·Matched Count：流表匹配次数

Multipart Port Stats Reply

Multipart Port Stats Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Port no：端口索引

·Dur Sec：持续时间秒数

·DurnSec：持续时间微秒数

·RecvPkt：端口接收到的报文计数

·SendPkt：端口发送的报文计数

·RecvByte：端口接收的报文字节数

·SendByte：端口发送的报文字节数

·RecvDrop：端口丢弃的接收报文数目

·SendDrop：端口丢弃的发送报文数目

·RecvErr：接受错误的报文数目

·FrameErr：帧错误计数

·RunOver：越界计数

·CRCErr：CRC效验错误计数

·uiCollision：冲突错误计数

Multipart Queue Reply

Multipart Queue Reply报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Port no：端口索引

·Queue id：队列索引

·Send Bytes：队列发送字节数

·Send Packets：队列发送报文计数

·Err Packets：队列错误报文计数

·DurSec：队列持续时间秒数

·DurnSec：队列持续时间微秒数

Multipart Group Reply

Multipart Group Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Group ID：group ID

·RefCount：关联表项个数

·DurSec：group持续时间秒数

·DurnSec：group持续时间微秒数

Multipart Group Description Reply

Multipart Group Description Reply报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Group ID：group ID

·Type：group类型

·Bucket：group动作集

Multipart Group Features Reply

Multipart Group Features Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Type：group类型

·Capabilities：group支持的能力集

·Select Weight：Support weight for select groups

·Select Liveness：Support liveness for select groups

·Chaining：Support chaining groups

·Chaining Checks：Check chaining for loops and delete

Multipart Meter Reply

Multipart Meter Reply报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Meter ID：meter ID

·Flow Count：meter关联流表项个数

·Dur Sec：meter持续时间秒数

·Dur nSec：meter持续时间微秒数

·Pkt Count：meter匹配报文个数

·Byte Count：meter匹配报文字节数

·Band Counter：每个band的统计计数

Multipart Meter Config Reply

Multipart Meter Config Reply报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Meter ID：meter ID

·Flags：meter标识

·Band：meter内band信息

Multipart Meter Features Reply

Multipart Meter Features Reply报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·MaxMeter：meter最大数目

·BandTypes：支持的band类型

·Capabilities：能力集

·MaxBands：支持最大band数目

·MaxColor：支持最大报文颜色数目

Multipart Table Features Reply

Multipart Table Features Reply报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Table ID：表ID

·Config：表的配置

·Max Entries：流表项最大数目

·Name：表名字

·MetaDataMatch：匹配的metadata取值范围

·MetaDataWrite：写入的metadata取值范围

·Prop type：Property类型

Multipart Port Description Request

Multipart Port Description Request报文中携带的信息：

·Type：Multipart报文类型

·Flags：Multipart报文标记

·Port：端口索引

·Mac addr：端口MAC地址

·Port Name：端口名

·Config：端口配置

·State：端口状态

·Curr：端口当前状态

·Adv：端口建议状态

·Support：端口支持状态

·Peer：端口对端状态

·Curr speed：端口当前速率

·Max speed：端口最大速率

Role Request

Role Request报文中携带的信息：

·Role：角色

·Gener ID：generation ID

Role Reply

Role Reply报文中携带的信息：

·Role：角色

·Gener ID：generation ID

Queue Get Config Request

Queue Get Config Request报文中携带的信息：

·Port：端口索引

Queue Get Config Reply

Queue Get Config Reply报文中携带的信息：

·Port：端口索引

·Queue ID：队列ID

·Port：队列所属端口索引

·Prop：队列的性质

Get Async Reply

Get Async Reply报文中携带的信息：

·packetin：Controller各个角色是否上送packet in报文

·flow rmv：Controller各个角色是否上送flow rmv报文

·port status：Controller各个角色是否上送port status报文

Set Async Reply

Set Async Reply报文中携带的信息：

·packetin：Controller各个角色是否上送packet in报文

·flow rmv：Controller各个角色是否上送flow rmv报文

·port status：Controller各个角色是否上送port status报文

Meter Mod

Meter Mod报文中携带的信息：

·Meter id：meter ID

·Command：Meter Mod类型

·Flags：meter标记

·Band：meter中的band信息

【举例】

\# 打开OpenFlow报文调试信息开关。

\<Sysname\> debugging openflow packet

\*Apr  9 09:56:09:475 2013 Sysname OFP/7/PACKET: -MDC=1;

Instance ID: 0x1, Controller ID: 0x0 send

Version: 0x4, Type: hello, Length: 0x10, Xid: 0x0

Element Type: Bitmap

Version: 0x4

*// 实例1控制器0发送一个Hello报文*

\<Sysname\>

\*Apr  9 09:56:09:475 2013 Sysname OFP/7/PACKET: -MDC=1;

Instance ID: 0x1, Controller ID: 0x0 receive

Version: 0x4, Type: hello, Length: 0x10, Xid: 0x0

Element Type: Bitmap

Version: 0x4

*// 实例1控制器0接收一个Hello报文*

\<Sysname\>

\*Jan  1 21:38:28:070 2011 Sysname OFP/7/PACKET:

Instance ID: 0x1, Controller ID: 0x0 send

Version: 0x4, Type: pkt in, Length: 0x86, Xid: 0x0

Reason: 0x0, table id: 0x0, bufid: 0x0, cookie: 0x0

Match Type: 0x1, Match Length: 0x2c

Match Field

Class: 0x8000, Type: in port, value: 0x1

Class: 0x8000, Type: in phy port, value: 0x1

Class: 0x8000, Type: metadata

value: 0x0000000000000000

Class: 0x8000, Type: tunnel_id, value: 0x0

Packet Data:

ff ff ff ff ff ff 00 00 00 00 00 09 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00

*// 实例1控制器0发送一个packet in报文*

\<Sysname\>

\*Jan  1 22:06:07:289 2011 Sysname OFP/7/PACKET:

Instance ID: 0x1, Controller ID: 0x0 receive

Version: 0x4, Type: pkt out, Length: 0x5d, Xid: 0x14

bufid: 0x1, in port: 0x1

Action: output, port: 0x1, maxlen: 0x80

Action: set field

Class: 0x8000, Type: ipv4_dst, value: 1.1.1.1

Action: set field

Class: 0x8000, Type: vlan_vid, value: 0x64

Packet Data:

00 11 22 33 44 55 66 77 88 99 00 11 22 33 44 55

66 77 88 99 00

*// 实例1控制器0接收一个packet out报文*

\<Sysname\>

\*Apr  9 16:10:22:962 2013 Sysname OFP/7/PACKET: -MDC=1;

Instance ID: 0x1, Controller ID: 0x0 receive

Version: 0x4, Type: flow mod, Length: 0x120, Xid: 0x3b

Cookie: 0x457, CookieMask: 0x0, TableId: 0x0,

Command: 0x0, IdleTime: 0x0, HardTime: 0x0,

Priority: 0x68, BufferId: 0xffffffff,

OutPort: 0xffffffff, OutGroup: 0xffffffff, Flag: 0x7

Match Type: 0x1, Match Length: 0x7a

Match Field

Class: 0x8000, Type: in port, value: 0x4

Class: 0x8000, Type: in phy port, value: 0x4

Class: 0x8000, Type: ethdst, value: 0012-3456-789a ,mask: ffff-ffff-0000

Class: 0x8000, Type: ethsrc, value: 0011-1111-1111 ,mask: ffff-ff00-0000

Class: 0x8000, Type: ethtype, value: 0x0800

Class: 0x8000, Type: vlan_vid, value: 0x64 ,mask: 0x64

Class: 0x8000, Type: vlan_pcp, value: 0x5

Class: 0x8000, Type: ip_dscp, value: 0x7

Class: 0x8000, Type: ip_ecn, value: 0x3

Class: 0x8000, Type: ip_pro, value: 0x6

Class: 0x8000, Type: ipv4_src, value: 1.1.1.1 ,mask

\*Apr  9 16:10:22:962 2013 Sysname OFP/7/PACKET: -MDC=1;

: 255.0.0.0

Class: 0x8000, Type: ipv4_dst, value: 1.1.1.2 ,mask: 255.0.0.0

Class: 0x8000, Type: tcp_src, value: 0x15af

Class: 0x8000, Type: tcp_dst, value: 0x1a05

Instruction Type: clear actions

Instruction Type: meter

meter id: 0x1

Instruction Type: go to table

table id: 0x1

Instruction Type: apply actions

Action: output, port: 0xfffffffe, maxlen: 0x80

Instruction Type: write actions

Action: output, port: 0xfffffffd, maxlen: 0x80

Action: group, group: 0x1

Action: set field

Class: 0x8000, Type: ipv4_src, value: 2.2.2.2

Action: set field

Class: 0x8000, Type: vlan_vid, value: 0x64

*// 实例1控制器0接收一个flow mod报文*

\<Sysname\>

\*Apr  9 16:26:55:493 2013 Sysname OFP/7/PACKET: -MDC=1;

Instance ID: 0x1, Controller ID: 0x0 receive

Version: 0x4, Type: group mod, Length: 0xa8, Xid: 0x3e

Group id: 0x1, command: 0x0, type: 0x1

Bucket

Weight: 0x64, watch group: 0x66, watch port: 0x65

Action: set field

Class: 0x8000, Type: ipv4_dst, value: 1.1.1.1

Action: set field

Class: 0x8000, Type: vlan_vid, value: 0x64

Action: output, port: 0xfffffffd, maxlen: 0x80

Bucket

Weight: 0x64, watch group: 0x66, watch port: 0x65

Action: set field

Class: 0x8000, Type: ipv6_src

value: 11:2233:4455:6677:8899:AABB:CCDD:EEFF

mask: FFFF:FFFF:FFFF:FFFF::

Action: set field

Class: 0x8000, Type: vlan_vid, value: 0x64

Action: output, port: 0x4, maxlen: 0x80

*// 实例1控制器0接收一个group mod报文*

\<Sysname\>

\*Apr 10 11:19:55:498 2013 Sysname OFP/7/PACKET: -MDC=1;

Instance ID: 0x1, Controller ID: 0x0 receive

Version: 0x4, Type: meter mod, Length: 0x30, Xid: 0x18

Meter id: 0x1, command: 0x0, flags: 0x1

Band type: drop, rate: 0x3e8, burst size: 0x7d0

Band type: dscp remark, rate: 0xbb8, burst size: 0xfa0, preclevel: 0x1

*// 实例1控制器0接收一个meter mod报文*

