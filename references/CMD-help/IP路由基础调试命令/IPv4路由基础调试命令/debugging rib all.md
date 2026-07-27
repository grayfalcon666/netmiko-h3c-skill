<!-- CMD-INDEX
  debugging rib all                   | 用户视图             | L19
  debugging rib ftn                   | 用户视图             | L55
  debugging rib nib                   | 用户视图             | L183
  debugging rib rcom                  | 用户视图             | L447
  debugging rib signal                | 用户视图             | L619
  debugging rib urt                   | 用户视图             | L691
  debugging route-direct nib          | 用户视图             | L861
  debugging route-direct process      | 用户视图             | L1001
  debugging ipv6 rib all              | 用户视图             | L1253
  debugging ipv6 rib nib              | 用户视图             | L1289
  debugging ipv6 rib rcom             | 用户视图             | L1465
  debugging ipv6 rib signal           | 用户视图             | L1523
  debugging ipv6 rib urt              | 用户视图             | L1569
  debugging ipv6 route-direct nib     | 用户视图             | L1667
  debugging ipv6 route-direct process | 用户视图             | L1809
-->

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging rib all**

------------------------------------------------------------------------

【命令】

**[debugging rib all**]

**[undo debugging rib all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging rib all**]命令用来打开IPv4路由管理所有的调试信息开关。**undo debugging rib all**命令用来关闭IPv4路由管理所有的调试信息开关。

缺省情况下，IPv4路由管理所有的调试信息开关处于关闭状态。

【举例】

\# 打开IPv4路由管理所有的调试信息开关。

\<Sysname\> debugging rib all

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging rib ftn**

------------------------------------------------------------------------

【命令】

**[debugging rib******ftn**]

**[undo debugging rib******ftn**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging rib******ftn**]命令用来打开IPv4路由FTN表的调试信息开关。**undo debugging rib******ftn**用来关闭IPv4路由FTN表的调试信息开关。

缺省情况下，IPv4路由FTN表的调试信息开关处于关闭状态。

表1-1 debugging rib ftn命令输出信息描述表

字段

含义

FtnIndex

FTN表项索引号

Route

路由前缀信息

NibID

下一跳ID

flags

路由标志信息

Label

出标签

Nexthop

下一跳信息

Ifindex

出接口索引

Protocol

打标签的协议号

StatDiscontinuityTime

统计计数翻转时间

FwOctets

转发字节数

FwPackets

转发包个数

type

FTN表项查询类型

length

返回包长度

error

错误码

【举例】

\# 打开IPv4路由管理FTN表的调试信息开关。

\<Sysname\> debugging rib ftn

\*Mar  2 14:51:44:057 2013 Sysname RM/7/DEBUG: -MDC=1;

  Add ftn success: FtnIndex 0x80000400, Route 199.1.1.1/32, NibID 0x15000003, fl

ags 0x900060

*// 添加目的地址为199.1.1.1/32的FTN表项*

\*Mar  2 14:50:19:062 2013 Sysname RM/7/DEBUG: -MDC=1;

 Delete ftn success, FtnIndex: 0x8000041d, NibID: 0x1500001e, Flags: 0x910060

*// 删除索引为0x8000041d的FTN表项*

\*Mar  2 12:05:27:484 2013 Sysname RM/7/DEBUG: -MDC=1;

 Ftn query success, type 0x200, length 92, error 0.

\*Mar  2 12:05:27:535 2013 Sysname RM/7/DEBUG: -MDC=1;

 Route: 2.2.2.2/32, Nexthop: 10.1.1.2, Ifindex: 467, Protocol: 2, FtnIndex: 0x80

000000, StatDiscontinuityTime: 0, FwOctets: 1157750, FwPackets: 17403.

\*Mar  2 12:05:27:586 2013 Sysname RM/7/DEBUG: -MDC=1;

 Ftn query success, type 0x300, length 16, error 1073807365.

*// 查询FTN表项信息*

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging rib nib**

------------------------------------------------------------------------

![说明](IP路由基础Debug.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

【命令】

**[debugging rib nib ** *nib-id* ]

**[undo debugging rib nib**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，十六进制，取值范围为1～FFFFFFFF。

【描述】

**[debugging rib nib**]命令用来打开IPv4 RIB下一跳信息的调试信息开关。**undo debugging rib nib**用来关闭IPv4 RIB下一跳信息的调试信息开关。

缺省情况下，IPv4 RIB下一跳信息的调试信息开关处于关闭状态。

表1-2 debugging rib nib命令输出信息描述表

字段

含义

id

 Nexthop ID

fd

与该协议连接的句柄

TempID

申请ID时协议建议值

seq

序列号

errno

错误码

PrefixIndex

等价时下一跳序号

Vrf

实例名

OrigNexthop

原始下一跳

RealNexthop

真实下一跳

Interface

出接口

localAddr

本地接口地址

RelyDepth

迭代深度

msgtype

消息类型，包括ADD/DEL

【举例】

\# 打开IPv4 RIB 下一跳信息的调试信息开关。

\<Sysname\> debugging rib nib

\*Aug 22 19:30:08:536 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB reply id request to USR, id 11000000, fd 23, TempID 0

*// 响应协议的NIB ID申请*

\*Aug 22 19:30:08:485 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB add NIB 0041/0/0/0/0/2.2.2.2, id 11000000 seq 15, errno 0

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3.3.4.5

  RelyDepth: 0              RealNexthop: 3.3.4.5

  Interface: GE1/0/2          LocalAddr: 11.1.1.2

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 添加Nexthop信息*

\*Aug 22 22:48:58:433 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB delete NIB 11000000 with seq 15

*// 删除Nexthop信息*

\*Aug 22 19:30:08:485 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB modify NIB 11000000 with nexthop 1.1.1.1

Old Value:

1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.1.1.1

  RelyDepth: 1              RealNexthop: 2.2.2.2

  Interface: GE1/0/2          LocalAddr: 3.3.3.3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

New value:

1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.1.1.1

  RelyDepth: 1              RealNexthop: 4.4.4.4

  Interface: GE1/0/2          LocalAddr: 3.3.3.3

  TunnelCnt: 1                      Vrf: default-vrf

   TunnelID: 1024

*// 修改Nexthop信息*

\*Aug 22 19:30:08:537 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB sync NIB 11000000 to backup, msgtype ADD, errno 0

1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3.3.4.5

  RelyDepth: 0              RealNexthop: 3.3.4.5

  Interface: GE1/0/2          LocalAddr: 11.1.1.2

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 同步nexthop增、删消息给备进程（保证主备NIB ID一致）*

\*Aug 22 19:30:08:537 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB nexthop 2.2.2.2 for NIB 11000000 is deleted for validation check.

*// 下一跳有效性检查, 剔除多余部分*

\*Aug 22 19:30:08:537 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB recv tnlchg for NIB 1100000, tunnels: [11024]

*// 处理解析后的Nexthop消息\--隧道变化消息*

\*Aug 22 19:30:08:537 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB flush NIB with ID 1100000 and seq 15 to FIB, bytes 36, value:

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.1.1.1

  RelyDepth: 1              RealNexthop: 2.2.2.2

  Interface: GE1/0/2          LocalAddr: 3.3.3.3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

    Backup Nexthop Value:

PrefixIndex: 0              OrigNexthop: 1.1.1.1

  RelyDepth: 1              RealNexthop: 5.5.5.5

  Interface: GE1/0/4          LocalAddr: 4.4.4.4

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 下刷FIB添加消息*

\*Aug 22 19:30:08:537 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB deflush NIB with ID 1100000  and seq 15 to FIB, bytes 36

*// 下刷FIB删除消息*

\*Aug 22 19:30:08:537 2012 Sysname NIB/7/DEBUG: -MDC=1;

RIB refresh NIB 1100000

Old Value:

1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.1.1.1

  RelyDepth: 1              RealNexthop: 2.2.2.2

  Interface: GE1/0/2          LocalAddr: 3.3.3.3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

New value:

1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.1.1.1

  RelyDepth: 1              RealNexthop: 2.2.2.2

  Interface: GE1/0/2          LocalAddr: 3.3.3.3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 更新NIB的值*

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging rib rcom**

------------------------------------------------------------------------

【命令】

**[debugging rib rcom** [ **prefix-list** *prefix-list-name* ]]

**[undo debugging rib rcom**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[prefix-list*** prefix-list-name*]：打开指定前缀列表的IPv4路由下刷的调试信息开关。*prefix-list-name*为前缀列表名称，为1～63个字符的字符串，区分大小写。

【描述】

**[debugging rib rcom**]用来打开IPv4路由下刷的调试信息开关。**undo debugging rib rcom**命令用来关闭IPv4路由下刷的调试信息开关。

缺省情况下，IPv4路由下刷的调试信息开关处于关闭状态。

表1-3 debugging rib rcom命令输出信息描述表

字段

描述

prefix

目的地址/掩码

VrfIndex

VPN索引

OrigAs

初始自治域

LasAs

邻接自治域

CurProto

路由协议类型

OldProto

上次上报的协议类型

SubProto

子协议类型号

Pref

路由优先级

Metric

路由的度量值

VNID

虚拟下一跳索引

Flag

路由标志位

Label

标签

BkLabel

备份标签

DrvContext

预留字段

NibID

下一跳ID

IF

接口索引

RtIndex

路由索引

Tunnel

隧道ID

Pri/ private(s)

等价路由的私有部分编号

AttrID

路由属性ID

ProcessID

进程号

IpPrec

IP优先级

QosLocalID

QoS本地ID

【举例】

\# 打开IPv4路由下刷的调试信息开关。

\<Sysname\> debugging rib rcom

\*May  9 10:00:09:614 2012 Sysname RM/7/DEBUG: -MDC=1;

 Flush IPv4 Delete Msg for default-vrf. 1 prefix(s):

    2.2.2.0/24 VrfIndex=0 OrigAs=0 LasAs=0 with 0 private(s)

\*May  9 10:00:09:716 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify IPv4 delete(comm) for default-vrf. CurProto: UnSpec OldProto: STATIC

    Prefix: 2.2.2.0/24 SubProto: 0 Pref: 0 Metric: 0

*// 路由删除的下刷*

\*May  9 09:42:51:937 2012 Sysname RM/7/DEBUG: -MDC=1;

 Flush IPv4 Refresh Msg for default-vrf. VNID: 0x111000001, 1 prefix(s):

    3.3.3.0/24 VrfIndex=0 OrigAs=0 LasAs=0 with 1 private(s)

    1 Flag=10020000 Label=-1 BkLabel=-1 DrvContext=(ffffffff/ffffffff) AttrId=

-1 IpPrec=7 QosLocalID=1

\*May  9 09:42:52:039 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify IPv4 refresh(comm) for default-vrf. CurProto: STATIC OldProto: UnSpec

    01VrfIndex: 0, OrigNH: 0.0.0.0, RealNH: 0.0.0.0

        NibID: 0x11000001 IF: NULL0(32), RtIndex: 0, Tunnel: -1

    Prefix: 3.3.3.0/24 SubProto: 0 Pref: 60 Metric: 0

    01Pri: AttrID: 0xffffffff Flag: 10000 Label: -1 Tag: 0 ProcessID: 0

*// 路由添加的下刷*

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging rib signal**

------------------------------------------------------------------------

【命令】

**[debugging rib******signal**]

**[undo debugging rib******signal**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging rib******signal**]命令用来打开IPv4线程间信号传递的调试信息开关。**undo debugging rib******signal**用来关闭IPv4线程间信号传递的调试信息开关。

缺省情况下，IPv4线程间信号传递的调试信息开关处于关闭状态。

表1-4 debugging rib signal命令输出信息描述表

字段

含义

Notify Thread Type

通知的消息类型

【举例】

\# 打开IPv4线程间信号传递的调试信息开关。

\<Sysname\> debugging rib signal

\*May  9 10:18:25:359 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

\*May  9 10:18:25:410 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

\*May  9 10:18:25:462 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

\*May  9 10:18:25:513 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

\*May  9 10:18:25:564 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

\*May  9 10:18:25:615 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

*[// IPv4*]*线程间有信息传递，信息类型为0x621f*

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging rib urt**

------------------------------------------------------------------------

【命令】

**[debugging rib******urt ** **prefix-list** *prefix-list-name* ]

**[undo debugging rib******urt**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[prefix-list*** prefix-list-name*]：打开指定前缀列表的IPv4路由表的调试信息开关。*prefix-list-name*为前缀列表名称，为1～63个字符的字符串，区分大小写。

【描述】

**[debugging rib******urt**]命令用来打开IPv4路由表的调试信息开关。**undo debugging rib******urt**用来关闭IPv4路由表的调试信息开关。

缺省情况下，IPv4路由表的调试信息开关处于关闭状态。

表1-5 debugging rib urt命令输出信息描述表

字段

含义

added/deleted/modified

添加/删除/修改路由

Flags

路由属性标志位

Process

协议进程ID

SubProto

子协议号

Label

出标签

NibID

下一跳ID

Metric

度量值

Pref

优先级

(B)Label

备份出标签

AttrID

属性ID

ErrCode

错误码

PubFlags

路由操作标志位

Priority

路由优先级

IDNtfy

上报路由协议的Neighbor ID

OldProto

上次上报的协议类型

ActiveCnt

相同前缀激活路由条数

IDFlush

下刷FIB的Neighbor ID

【举例】

\# 打开IPv4路由管理路由表的调试信息开关。

\<Sysname\> debugging rib urt

\*May  9 10:29:58:618 2012 Sysname RM/7/DEBUG: -MDC=1;

 STATIC route 101.1.1.0/24 was added in vpn default-vrf.

      Flags: 0x0         Process: 0     SubProto: 0       Label: -1

      NibID: 0x11000003   Metric: 0         Pref: 60   (B)Label: -1

     AttrID: 0xffffffff Priority: 3

\*May  9 10:29:58:669 2012 Sysname RM/7/DEBUG: -MDC=1;

 route 101.1.1.0/24 in default-vrf was calculated, ErrCode: 0.

      PubFlags: 0x0000(0x22)  Priority: LOW       IDNtfy: 0x11000003

      OldProto: UnSpec       ActiveCnt: 1        IDFlush: 0x11000003

*// 添加目的地址为101.1.1.0/24的静态路由*

\*May  9 10:33:31:125 2012 Sysname RM/7/DEBUG: -MDC=1;

 STATIC route 101.1.1.0/24 was modified in vpn default-vrf.

      Flags: 0x0         Process: 0     SubProto: 0       Label: 0

      NibID: 0x11000003   Metric: 0         Pref: 10   (B)Label: 0

     AttrID: 0x0        Priority: 3

\*May  9 10:33:31:176 2012 Sysname RM/7/DEBUG: -MDC=1;

 route 101.1.1.0/24 in default-vrf was calculated, ErrCode: 0.

      PubFlags: 0x0c00(0x12)  Priority: LOW       IDNtfy: 0x11000003

      OldProto: STATIC       ActiveCnt: 1        IDFlush: 0x11000003

*// 修改目的地址为101.1.1.0/24的静态路由*

\*May  9 10:33:08:551 2012 Sysname RM/7/DEBUG: -MDC=1;

 STATIC route 101.1.1.0/24 was deleted in vpn default-vrf.

      Flags: 0x0         Process: 0     SubProto: 0       Label: 0

      NibID: 0x11000003   Metric: 0         Pref: 0    (B)Label: 0

     AttrID: 0x0        Priority: 3

\*May  9 10:33:08:603 2012 Sysname RM/7/DEBUG: -MDC=1;

 route 101.1.1.0/24 in default-vrf was calculated, ErrCode: 0.

      PubFlags: 0x0c00(0x12)  Priority: LOW       IDNtfy: 0x00000000

      OldProto: STATIC       ActiveCnt: 0        IDFlush: 0x00000000

*// 删除目的地址为101.1.1.0/24的静态路由*

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging route-direct nib**

------------------------------------------------------------------------

【命令】

**[debugging route-direct nib** [ *nib-id* ]]

**[undo debugging route-direct nib**]

【视图】

用户视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，十六进制，取值范围为1～FFFFFFFF。

【描述】

**[debugging route-direct nib**]命令用来打IPv4直连路由下一跳信息的调试信息开关。**undo debugging route-direct nib**用来关闭IPv4直连路由下一跳信息的调试信息开关。

缺省情况下，IPv4直连路由下一跳信息的调试信息开关处于关闭状态。

表1-6 debugging route-direct nib命令输出信息描述表

字段

含义

Add/Delete/Modify NIB

添加/删除/修改下一跳信息

Seq

序号

Errno

错误码

PrefixIndex

前缀编号

Vrf

实例名

OrigNexthop

原始下一跳

RealNexthop

真实下一跳

Interface

出接口名

Localaddr

本地接口地址

RelyDepth

迭代深度

Msgtype

消息类型

TunnelCnt

隧道个数

TunnelID

隧道号

【举例】

\# 打开IPv4直连路由下一跳信息的调试信息开关。

\<Sysname\> debugging route-direct nib

\*Sep 19 09:00:52:251 2012 Sysname NIB/7/DEBUG: -MDC=1; IFM add NIB 0005/0/0/0/1d

4/3.2.3.4, id 10000010 seq 17, errno 0

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3.2.3.4

  RelyDepth: 0              RealNexthop: 3.2.3.4

  Interface: Vlan400          LocalAddr: 3.2.3.4

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 添加NIB*

%Sep 19 09:00:52:252 2012 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on

the interface Vlan-interface400 is UP.

\*Sep 19 09:00:52:302 2012 Sysname NIB/7/DEBUG: -MDC=1;

 IFM sync NIB 10000010 to RIB, msgtype ADD, bytes 200

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3.2.3.4

  RelyDepth: 0              RealNexthop: 3.2.3.4

  Interface: Vlan400          LocalAddr: 3.2.3.4

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 把NIB同步给RIB*

\*Aug 23 15:44:45:833 2012 Sysname NIB/7/DEBUG: -MDC=1; IFM delete NIB 10000010 w

ith seq 17

*// 删除NIB*

**IP路由基础调试命令 \-- IPv4路由基础调试命令 \-- debugging route-direct process**

------------------------------------------------------------------------

【命令】

**[debugging route-direct process**]

**[undo debugging route-direct process**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-direct process**]命令用来打开IPv4直连路由的调试信息开关。**undo debugging route-direct process**用来关闭IPv4直连路由的调试信息开关。

缺省情况下，IPv4直连路由的调试信息开关处于关闭状态。

表1-7 debugging route-direct process命令输出信息描述表

字段

含义

ifIndex

接口索引

Ifstate

接口状态标志

Slot

板号

IfName

接口名

ifType

接口类型

EventType

事件类型

Inst

实例号

Band

带宽

Baud

波特率

MTU

最大传输单元

MAC

MAC地址

LINKDOWN2UP

链路层UP消息

PhyName

物理口名

PhyIndex

物理口DB索引

IP4PriLogiIndex

IPv4主逻辑口索引

字段

含义

IP6FirstLogiIndex

IPv6主逻辑口索引

State

接口状态

DOWN2UP

逻辑口UP消息

LogiIndex

逻辑口索引

RefCount

引用计数

ExitIf

出接口索引

ProtoID

协议号

Pref

优先级

AddrType

地址类型

HColor

主机地址冲突类型

NColor

网段地址冲突类型

【举例】

\# 打开IPv4直连路由的调试信息开关。

\<Sysname\> debugging route-direct process

\*Sep 14 19:02:00:548 2012 Sysname IFM/7/DEBUG: -MDC=1;

IFNET Message: ifIndex=0x2, IfState=0x88400, Slot=0, IfName=, IfType=0, EventTyp

e=0x40000001, Inst=0, Band=0, Baud=0x0, MTU=0, MAC=0000-0000-0000.

*// 收到接口消息*

\*Sep 14 19:02:00:548 2012 Sysname IFM/7/DEBUG: -MDC=1;

Packed phyical LINKDOWN2UP message: phyName=GigabitEthernet1/0/2, ifIndex=0x2, PhyInde

x=3, IP4PriLogiIndex=3, IP6FirstLogiIndex=0, State=0x88400.

*// 打包通知各协议的物理口消息（链路UP）*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Packed Logical DOWN2UP message(11.1.1.2/24): LogiIndex=3, PhyIndex=3, PriL

ogiIndex=3, State=0x201.

*// 打包通知各协议的逻辑口消息（IPv4逻辑口UP）*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Increase extnode(11.1.1.2/32) refcount: 1.

*// 加radix树外节点引用计数*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Add Interface route: NibID=0x10000009, Dest/Mask(11.1.1.2/32), ExitIf=112,

 Nexthop=127.0.0.1, ProtoID=1, Pref=0, Flag=4.

*// 添加接口主机路由*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Add subnet(or NAT) route: NibID=0x1000000d, Dest/Mask(11.1.1.0/24), ExitIf

=2, Nexthop=11.1.1.2, ProtoID=1, Pref=0, Flag=128.

*// 添加网段路由*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Add 1st SubBroadcast route: NibID=0x1000000d, Dest/Mask(11.1.1.255/32), Ex

itIf=2, Nexthop=201010b, ProtoID=1, Pref=0, Flag=140.

*// 添加.255的子网广播路由*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Add 2nd SubBroadcast route: NibID=0x1000000d, Dest/Mask(11.1.1.0/32), Exit

If=2, Nexthop=201010b, ProtoID=1, Pref=0,Flag=140.

*// 添加.0的子网广播路由*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Add 1st Global Multicast route: NibID=0x1000000d, Dest/Mask(224.0.0.0/4),

ExitIf=2, Nexthop=201010b, ProtoID=1, Pref=0, Flag=140.

*// 添加224.0.0.0/4组播路由*

\*Sep 14 19:02:00:550 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Add 2nd Global Multicast route: NibID=0x1000000d, Dest/Mask(224.0.0.0/24)

, ExitIf=2, Nexthop=201010b, ProtoID=1, Pref=0,Flag=140.

*// 添加224.0.0.0/24组播路由*

\*Sep 15 19:47:02:717 2012 Sysname IFM/7/DEBUG: -MDC=1;

 IP4 Packed Logical DEL message(30.1.1.1/24): LogiIndex=12, PhyIndex=11, PriLo

giIndex=12, State=0x200.

*// 打包通知IPv4删除消息*

\*Sep 15 19:47:02:717 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP4 Logical DEL message: Inst=0, ifIndex=0x1d4, IP/Mask=30.1.1.1/24, AddrType

=1, HColor=0, NColor=0, IpFlag=0.

*// 处理IPv4删除逻辑口消息*

\*Sep 15 19:47:02:721 2012 Sysname IFM/7/DEBUG: -MDC=1;

Packed phyiscal DEL message: phyName=Vlan-interface300, ifIndex=0x1d4, PhyIndex

=11, IP4PriLogiIndex=0, IP6FirstLogiIndex=0, State=0x8400.

*// 处理IPv4删除物理口消息*

**IP路由基础调试命令 \-- IPv6路由基础调试命令 \-- debugging ipv6 rib all**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 rib all**]

**[undo debugging ipv6 rib all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging ipv6 rib all**]命令用来打开IPv6路由管理所有的调试信息开关。**undo debugging ipv6 rib all**命令用来关闭IPv6路由管理所有的调试信息开关。

缺省情况下，IPv6路由管理所有的调试信息开关处于关闭状态。

【举例】

\# 打开IPv6路由管理所有的调试信息开关。

\<Sysname\> debugging ipv6 rib all

**IP路由基础调试命令 \-- IPv6路由基础调试命令 \-- debugging ipv6 rib nib**

------------------------------------------------------------------------

![说明](IP路由基础Debug.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

【命令】

**[debugging ipv6 rib nib ** *nib-id* ]

**[undo debugging ipv6 rib nib**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，十六进制，取值范围为1～FFFFFFFF。

【描述】

**[debugging ipv6 rib nib**]命令用来打开IPv6 RIB下一跳信息的调试信息开关。**undo debugging ipv6 rib nib**用来关闭IPv6 RIB下一跳信息的调试信息开关。

缺省情况下，IPv6 RIB下一跳信息的调试信息开关处于关闭状态。

输出信息描述参考 表1-2(?139547675#_Ref343604621)。

【举例】

\# 打开IPv6 RIB下一跳信息的调试信息开关。

\<Sysname\> debugging ipv6 rib nib

\*Sep 20 09:59:09:333 2012 Sysname NIB/7/DEBUG: -MDC=1; RIB add NIB 0005/0/0/0/2/

::, id 2000000c seq 12, errno 0

*// 添加NIB*

Sep 20 09:59:09:384 2012 Sysname NIB/7/DEBUG: -MDC=1; RIB reply id request to IF

M, id 2000000c, fd 24, TempID 0

*// 响应申请NIB ID*

\*Sep 20 09:59:09:443 2012 Sysname NIB/7/DEBUG: -MDC=1; RIB sync NIB 2000000c to

backup, msgtype ADD, errno 0

*// 同步添加消息到备板*

\*Sep 20 09:59:09:799 2012 Sysname NIB/7/DEBUG: -MDC=1;

 RIB modify NIB 21000002 with nexthop 3::3:

 Old value:

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3::3

  RelyDepth: 1              RealNexthop: ::

  Interface: NULL0            LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

 New value:

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3::3

  RelyDepth: 1              RealNexthop: 1:1::2

  Interface: GE1/0/2           LocalAddr: FE80::20C:29FF:FE1A:4DF7

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 修改NIB的下一跳信息*

\*Sep 20 09:59:09:850 2012 Sysname NIB/7/DEBUG: -MDC=1; RIB sync NIB 21000002 to

backup, msgtype MOD, errno 0

*// 同步modify消息*

\*Sep 20 09:59:10:786 2012 Sysname NIB/7/DEBUG: -MDC=1;

 RIB deflush NIB with ID 21000003 and seq 3 to FIB, bytes 20

*// 给FIB表下删除消息*

\*Sep 20 09:59:10:837 2012 Sysname NIB/7/DEBUG: -MDC=1; RIB delete NIB 21000003 w

ith seq 3

*// 删除指定的NIB*

\*Sep 20 09:59:10:888 2012 Sysname NIB/7/DEBUG: -MDC=1; RIB sync NIB 21000003 to

backup, msgtype DEL, errno 0

*// 同步删除消息到备板*

\*Sep 20 10:07:50:212 2012 Sysname NIB/7/DEBUG: -MDC=1; RIB add NIB 200021000002

/2/2/1/021000000/0/2/1/0, id 26000000 seq 0, errno 0

 2 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3::3

  RelyDepth: 1              RealNexthop: 1:1::2

  Interface: GE1/0/2           LocalAddr: 1:1::3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

PrefixIndex: 1              OrigNexthop: 3::3

  RelyDepth: 1              RealNexthop: ::

  Interface: NULL0            LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 添加组合NIB*

\*Sep 20 10:07:50:314 2012 Sysname NIB/7/DEBUG: -MDC=1;

 RIB flush NIB with ID 26000000 and seq 0 to FIB, bytes 244, value:

 2 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3::3

  RelyDepth: 1              RealNexthop: 1:1::2

  Interface: GE1/0/2           LocalAddr: 1:1::3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

PrefixIndex: 1              OrigNexthop: 3::3

  RelyDepth: 0              RealNexthop: ::

  Interface: NULL0            LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 下刷有两个下一跳的NIB*

**IP路由基础调试命令 \-- IPv6路由基础调试命令 \-- debugging ipv6 rib rcom**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 rib rcom ** **prefix-list** *prefix-list-name* ]

**[undo debugging ipv6 rib rcom**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[prefix-list*** prefix-list-name*]：打开指定前缀列表的IPv6路由下刷的调试信息开关。*prefix-list-name*为前缀列表名称，为1～63个字符的字符串，区分大小写。

【描述】

**[debugging ipv6 rib rcom**]用来打开IPv6路由下刷的调试信息开关。**undo debugging ipv6 rib rcom**命令用来关闭IPv6路由下刷的调试信息开关。

缺省情况下，IPv6路由下刷的调试信息开关处于关闭状态。

输出信息描述参考 表1-3(?195461564#_Ref291765971)。

【举例】

\# 打开IPv6路由下刷的调试信息开关。

\<Sysname\> debugging ipv6 rib rcom

\*May  9 10:44:38:273 2012 Sysname RM/7/DEBUG: -MDC=1;

 Flush IPv6 Delete Msg for default-vrf. 1 prefix(s):

    1::1/128 VrfIndex=0 OrigAs=0 LasAs=0 with 0 private(s)

*// 路由删除的下刷*

\*May  9 10:44:02:024 2012 Sysname RM/7/DEBUG: -MDC=1;

 Flush IPv6 Refresh Msg for default-vrf. VNID: 0x21000000, 1 prefix(s):

    1::1/128 VrfIndex=0 OrigAs=0 LasAs=0 with 1 private(s)

    1 Flag=10020000 Label=-1 BkLabel=-1 DrvContext=(ffffffff/ffffffff) AttrId=

-1 IpPrec=7 QosLocalID=1

*// 路由添加的下刷*

**IP路由基础调试命令 \-- IPv6路由基础调试命令 \-- debugging ipv6 rib signal**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 rib signal**]

**[undo debugging ipv6 rib signal**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging ipv6 rib signal**]命令用来打开IPv6线程间信号传递的调试信息开关。**undo debugging ipv6 rib signal**用来关闭IPv6线程间信号传递的调试信息开关。

缺省情况下，IPv6线程间信号传递的调试信息开关处于关闭状态。

输出信息描述参考 表1-4(?-796800424#_Ref291766015)。

【举例】

\# 打开IPv6线程间信号传递的调试信息开关。

\*May  9 10:47:54:683 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

\*May  9 10:47:54:734 2012 Sysname RM/7/DEBUG: -MDC=1;

 Notify Thread Type: 0x621f

*[// IPv6*]*线程间有信息传递，信息类型为0x621f*

**IP路由基础调试命令 \-- IPv6路由基础调试命令 \-- debugging ipv6 rib urt**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 rib urt** [ **prefix-list** *prefix-list-name* ]]

**[undo debugging ipv6 rib urt**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[prefix-list*** prefix-list-name*]：打开指定前缀列表的IPv6路由表的调试信息开关。*prefix-list-name*为前缀列表名称，为1～63个字符的字符串，区分大小写。

【描述】

**[debugging ipv6 rib urt**]命令用来打开IPv6路由表的调试信息开关。**undo debugging ipv6 rib urt**用来关闭IPv6路由表的调试信息开关。

缺省情况下，IPv6路由表的调试信息开关处于关闭状态。

输出信息描述参考 表1-5(?-1811608310#_Ref291766120)。

【举例】

\# 打开IPv6路由管理路由表的调试信息开关。

\<Sysname\> debugging ipv6 rib urt

\*May  9 10:51:49:094 2012 Sysname RM/7/DEBUG: -MDC=1;

 STATIC6 route 1::/96 was added in vpn default-vrf.

      Flags: 0x40        Process: 0     SubProto: 0       Label: -1

      NibID: 0x21000000   Metric: 0         Pref: 60   (B)Label: -1

     AttrID: 0xffffffff Priority: 3

\*May  9 10:51:49:146 2012 Sysname RM/7/DEBUG: -MDC=1;

 route 1::/96 in default-vrf was calculated, ErrCode: 0.

      PubFlags: 0x0000(0x22)  Priority: LOW       IDNtfy: 0x21000000

      OldProto: UnSpec       ActiveCnt: 1        IDFlush: 0x21000000

*// 添加目的地址为1::/96的IPv6静态路由*

\*May  9 10:51:03:796 2012 Sysname RM/7/DEBUG: -MDC=1;

 STATIC6 route 1::/96 was modified in vpn default-vrf.

      Flags: 0x0         Process: 0     SubProto: 0       Label: 0

      NibID: 0x21000000   Metric: 0         Pref: 10   (B)Label: 0

     AttrID: 0x0        Priority: 3

\*May  9 10:51:03:847 2012 Sysname RM/7/DEBUG: -MDC=1;

 route 1::/96 in default-vrf was calculated, ErrCode: 0.

      PubFlags: 0x0400(0x22)  Priority: LOW       IDNtfy: 0x21000000

      OldProto: UnSpec       ActiveCnt: 1        IDFlush: 0x21000000

*// 修改目的地址为1::/96的IPv6静态路由*

\*May  9 10:51:27:368 2012 Sysname RM/7/DEBUG: -MDC=1;

 STATIC6 route 1::/96 was deleted in vpn default-vrf.

      Flags: 0x0         Process: 0     SubProto: 0       Label: 0

      NibID: 0x21000000   Metric: 0         Pref: 0    (B)Label: 0

     AttrID: 0x0        Priority: 3

\*May  9 10:51:27:419 2012 Sysname RM/7/DEBUG: -MDC=1;

 route 1::/96 in default-vrf was calculated, ErrCode: 0.

      PubFlags: 0x0400(0x12)  Priority: LOW       IDNtfy: 0x00000000

      OldProto: UnSpec       ActiveCnt: 0        IDFlush: 0x00000000

*// 删除目的地址为1::/96的IPv6静态路由*

**IP路由基础调试命令 \-- IPv6路由基础调试命令 \-- debugging ipv6 route-direct nib**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 route-direct nib** [ *nib-id* ]]

**[undo debugging ipv6 route-direct nib**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，十六进制，取值范围为1～FFFFFFFF。

【描述】

**[debugging ipv6 route-direct nib**]命令用来打开IPv6直连路由下一条信息的调试信息开关。**undo debugging ipv6 route-direct nib**用来关闭IPv6直连路由下一条信息的调试信息开关。

缺省情况下，IPv6直连路由下一条信息的调试信息开关处于关闭状态。

表1-8 debugging ipv6 route-direct nib命令输出信息描述表

字段

含义

Add/Delete/Modify NIB

添加/删除/修改NIB邻居信息

Seq

序号

errno

错误码

PrefixIndex

前缀编号

Vrf

实例名

OrigNexthop

原始下一跳

RealNexthop

真实下一跳

Interface

出接口名

Localaddr

本地接口地址

RelyDepth

迭代深度

Msgtype

消息类型

TunnelCnt

隧道个数

TunnelID

隧道号

【举例】

\# 打开IPv6直连路由下一跳信息的调试信息开关。

\<Sysname\> debugging ipv6 route-direct nib

\*Sep 20 12:39:22:869 2012 Sysname NIB/7/DEBUG: -MDC=1; IFM add NIB 0005/0/0/0/1d

2/::, id 2000000d seq 15, errno 0

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: ::

  RelyDepth: 0              RealNexthop: ::

  Interface: Vlan200          LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 添加NIB*

\*Sep 20 12:39:22:920 2012 Syaname NIB/7/DEBUG: -MDC=1;

 IFM sync NIB 2000000d to RIB, msgtype ADD, bytes 200

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: ::

  RelyDepth: 0              RealNexthop: ::

  Interface: Vlan200          LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A

*// 把NIB添加同步给RIB*

\*Sep 20 12:40:50:636 2012 Sysname NIB/7/DEBUG: -MDC=1; IFM delete NIB 2000000d w

ith seq 16

*// 删除NIB*

\*Sep 20 12:40:50:687 2012 Sysname NIB/7/DEBUG: -MDC=1;

 IFM sync NIB 2000000d to RIB, msgtype DEL, bytes 36

*// 把NIB删除同步给RIB*

**IP路由基础调试命令 \-- IPv6路由基础调试命令 \-- debugging ipv6 route-direct process**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 route-direct process**]

**[undo debugging ipv6 route-direct process**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging ipv6 route-direct process**]命令用来打开IPv6直连路由的调试信息开关。**undo debugging ipv6 route-driect process**用来关闭IPv6直连路由的调试信息开关。

缺省情况下，IPv6直连路由的调试信息开关处于关闭状态。

表1-9 debugging ipv6 route-direct process命令输出信息描述表

字段

含义

ifIndex

接口索引

Ifstate

接口状态标志

Slot

板号

IfName

接口名

ifType

接口类型

EventType

事件类型

Inst

实例号

Band

带宽

Baud

波特率

MTU

最大传输单元

MAC

MAC地址

LINKDOWN2UP

链路层UP消息

PhyName

物理口名

PhyIndex

物理口DB索引

IP4PriLogiIndex

IPv4主逻辑口索引

IP6FirstLogiIndex

IPv6主逻辑口索引

State

接口状态

DOWN2UP

逻辑口UP消息

LogiIndex

逻辑口索引

RefCount

引用计数

ExitIf

出接口索引

ProtoID

协议号

Pref

优先级

AddrType

地址类型

HColor

主机地址冲突类型

NColor

网段地址冲突类型

【举例】

\# 打开IPv6直连路由的调试信息开关。

\<Sysname\> debugging ipv6 route-direct process

\*Sep 20 11:55:23:779 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Message: MsgType=0x10008, vrfIndex=0, IP/MaskLen:1:1::3/104, AddrType=4, I

fIndex=0x2, HColor=0, NColor=0.

*[// IFM*]*收到事件*

\*Sep 20 11:55:23:779 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Packed logical DEL message(1:1::3/104): LogiIndex=13, PhyIndex=3, PriLogiI

ndex=0, State=0x10000282.

*// 打包IPv6逻辑口删除事件通知协议*

\*Sep 20 11:55:23:779 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Logical DEL message: Inst=0, ifIndex=0x2, IP/Mask=1:1::3/104, AddrType=4,

HColor=0, NColor=0, IpFlag=0.

*// 处理IPv6逻辑口删除事件*

\*Sep 20 11:55:23:779 2012 Sysname IFM/7/DEBUG: -MDC=1;

IFNET Message: ifIndex=0x2, ifState=0x8, Slot=0, IfName=, IfType=0, EventType=0x

80000002, Inst=0, Band=0, Baud=0x0, MTU=0, MAC=0000-0000-0000.

*// 收到Ifnet消息*

\*Sep 20 11:55:23:780 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Packed logical UP2DOWN message(FE80::20C:29FF:FE1A:4DF7/10): LogiIndex=12,

 PhyIndex=3, PriLogiIndex=0, State=0x10800080.

*// 打包IPv6逻辑口DOWN事件通知协议*

\*Sep 20 11:55:23:780 2012 Sysname IFM/7/DEBUG: -MDC=1;

Packed physical IP6UP2DOWN message: phyName=GigabitEthernet1/0/2, ifIndex=0x2, PhyIndex

=3, IP4PriLogiIndex=0, IP6FirstLogiIndex=0, State=0x88480.

*// 打包物理口IPv6 DOWN事件通知协议*

\*Sep 20 11:55:39:208 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Logical ADD message: Inst=0, ifIndex=0x2, IP/Mask=1:1::/104, AddrType=2, H

Color=0, NColor=0, IpFlag=0.

*// 处理IPv6逻辑口添加事件*

\*Sep 20 11:55:40:461 2012 Sysname IFM/7/DEBUG: -MDC=1;

Packed physical CFGCHG message: phyName=GigabitEthernet1/0/2, ifIndex=0x2, PhyIndex=3,

IP4PriLogiIndex=0, IP6FirstLogiIndex=0, State=0x88480.

*// 打包物理口配置变化事件通知协议*

\*Sep 20 11:55:40:461 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Add subnet(or NAT) route: NibID=0x2000000c, Dest/Mask(1:1::/104), ExitIf=2

, Nexthop=::, ProtoID=1, Pref=0, Flag=128.

*[// IPv6*]*添加网段路由*

\*Sep 20 11:55:40:461 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Increase extnode(1:1::/104) refcount: 1.

*// 增加外节点引用计数*

\*Sep 20 11:55:40:461 2012 Sysname IFM/7/DEBUG: -MDC=1;

Packed physical IP6DOWN2UP message: phyName=GigabitEthernet1/0/2, ifIndex=0x2, PhyIndex

=3, IP4PriLogiIndex=0, IP6FirstLogiIndex=0, State=0x88482.

*// 打包物理口IPv6 UP事件通知协议*

\*Sep 20 11:55:40:462 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Packed logical ADD message(FE80::20C:29FF:FE1A:4DF7/10): LogiIndex=15, Phy

Index=3, PriLogiIndex=0, State=0x10800082.

*// 打包IPv6逻辑口UP事件通知协议*

\*Sep 20 11:55:40:462 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Logical ADD message: Inst=0, ifIndex=0x2, IP/Mask=FE80::20C:29FF:FE1A:4DF7

/10, AddrType=1, HColor=0, NColor=0, IpFlag=0.

*// 处理IPv6逻辑口UP事件通知协议*

\*Sep 20 11:55:41:472 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Add Interface route: NibID=0x20000009, Dest/Mask(1:1::3/128), ExitIf=112,

Nexthop=::1, ProtoID=1, Pref=0, Flag=4.

*[// IPv6*]*添加接口主机路由*

\*Sep 20 11:55:41:472 2012 Sysname IFM/7/DEBUG: -MDC=1;

IP6 Packed logical ADD message(1:1::3/104): LogiIndex=16, PhyIndex=3, PriLogiI

ndex=16, State=0x10000282.

*// 打包IPv6逻辑口UP事件通知协议*

\*Sep 20 12:33:18:039 2012 Sysname IFM/7/DEBUG: -MDC=1;

A pseudo logical interface delete: LogiIndex=20.

*// 删除伪逻辑口*

