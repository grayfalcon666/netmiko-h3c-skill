<!-- CMD-INDEX
  debugging route-static nib          | 用户视图             | L6
  debugging route-static process      | 用户视图             | L266
-->

**静态路由 \-- 静态路由调试命令 \-- debugging route-static nib**

------------------------------------------------------------------------

【命令】

**[debugging route-static nib** [ *nib-id* ]]

**[undo debugging route-static nib**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，十六进制，取值范围为1～FFFFFFFF。

【描述】

**[debugging route-static nib**]命令用来打开IPv4单播静态路由下一跳信息的调试信息开关。**undo debugging route-static nib**用来关闭IPv4单播静态路由下一跳信息的调试信息开关。

缺省情况下，IPv4单播静态路由下一跳信息的调试信息开关处于关闭状态。

表1-1 debugging route-static nib命令输出信息描述表

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

Topology

拓扑名称，base为公网拓扑（目前IPv6不支持子拓扑，显示为空）

【举例】

\# 打开IPv4单播静态路由下一跳信息的调试信息开关。

\<Sysname\> debugging route-static nib

\*Aug 23 15:44:45:833 2012 Sysname NIB/7/DEBUG: -MDC=1; USR delete NIB 11000000 w

ith seq 2

*// 删除NIB*

\*Sep 19 09:16:18:606 2012 Sysname NIB/7/DEBUG: -MDC=1; USR add NIB 0001/0/2

/0/2/1.2.3.4, id 11000004 seq 4, errno 0

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.2.3.4

  RelyDepth: 0              RealNexthop: 1.2.3.4

  Interface: GE1/0/2           LocalAddr: 11.1.1.2

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

*// 添加基础NIB*

\*Sep 19 09:16:18:657 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR sync NIB 11000004 to RIB, msgtype ADD, bytes 200

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.2.3.4

  RelyDepth: 0              RealNexthop: 1.2.3.4

  Interface: GE1/0/2           LocalAddr: 11.1.1.2

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

*// 同步基础NIB给RIB*

\*Sep 19 09:16:18:708 2012 Sysname NIB/7/DEBUG: -MDC=1; USR add NIB 100011000004

/4/2/1/011000001/1/2/1/0, id 11000005 seq 5, errno 0

 1 Nexthop Value(s):

       PrefixIndex: 0

               Vrf: default-vrf

  Orig/RealNexthop: 1.2.3.4/1.2.3.4

         Interface: GE1/0/2

         LocalAddr: 11.1.1.2

         RelyDepth: 0

Backup Nexthop Value:

PrefixIndex: 0              OrigNexthop: 1.2.3.4

  RelyDepth: 0              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

*// 添加FRR的NIB*

\*Sep 19 09:16:18:761 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR sync NIB 11000005 to RIB, msgtype ADD, bytes 320

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 1.2.3.4

  RelyDepth: 0              RealNexthop: 1.2.3.4

  Interface: GE1/0/2           LocalAddr: 11.1.1.2

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

Backup Nexthop Value:

PrefixIndex: 0              OrigNexthop: 1.2.3.4

  RelyDepth: 0              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

*// 同步FRR的NIB*

\*Sep 19 09:15:23:313 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR modify NIB 11000000 with nexthop 2.2.2.2:

 Old value:

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 2.2.2.2

  RelyDepth: 1              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

 New value:

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 2.2.2.2

  RelyDepth: 1              RealNexthop: 1.2.3.4

  Interface: GE1/0/2           LocalAddr: 11.1.1.2

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

*// 修改NIB*

\*Sep 19 09:15:23:370 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR sync NIB 11000000 to RIB, msgtype MOD, bytes 192

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 2.2.2.2

  RelyDepth: 1              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

*// 修改NIB同步给RIB*

\*Sep 19 09:15:23:421 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR re-rely route under NIB 11000000

*// 处理一个NIB的重新迭代*

**静态路由 \-- 静态路由调试命令 \-- debugging route-static process**

------------------------------------------------------------------------

【命令】

**[debugging route-static process**]

**[undo debugging route-static process**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-static process**]命令用来打开IPv4单播静态路由的调试信息开关。**undo debugging route-static process**用来关闭IPv4单播静态路由的调试信息开关。

缺省情况下，IPv4单播静态路由的调试信息开关处于关闭状态。

表1-2 debugging route-static process命令输出信息描述表

字段

含义

Add/Delete/Modify route

添加/删除/修改路由

NibID

下一跳ID

【举例】

\# 打开IPv4单播静态路由的调试信息开关。

\<Sysname\> debugging route-static process

%May  9 10:41:38:990 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 Add static route 101.1.1.0/24

%May  9 10:41:38:991 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 USR: Add route 101.1.1.0/24 with NibID 0x11000003 to RIB

*// 添加目的地址为101.1.1.0/24的静态路由*

%May  9 10:42:13:279 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 Add static route 101.1.1.0/24

%May  9 10:42:13:279 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 USR: Modify route 101.1.1.0/24 with NibID 0x11000003

*// 修改目的地址为101.1.1.0/24的静态路由*

%May  9 10:40:58:530 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 USR: Delete route 101.1.1.0/24 with NibID 0x11000003

*// 删除目的地址为101.1.1.0/24的静态路由*
