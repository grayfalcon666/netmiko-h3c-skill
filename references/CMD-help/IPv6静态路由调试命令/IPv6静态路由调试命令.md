<!-- CMD-INDEX
  debugging ipv6 route-static nib     | 用户视图             | L6
  debugging ipv6 route-static process | 用户视图             | L254
-->

**IPv6静态路由调试命令 \-- IPv6静态路由调试命令 \-- debugging ipv6 route-static nib**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 route-static nib** [ *nib-id* ]]

**[undo debugging ipv6 route-static nib**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：下一跳ID，十六进制，取值范围为1～FFFFFFFF。

【描述】

**[debugging ipv6 route-static nib**]命令用来打开IPv6单播静态路由下一跳信息的调试信息开关。**undo debugging ipv6 route-static nib **用来关闭IPv6 单播静态路由下一跳信息的调试信息开关。

缺省情况下，IPv6单播静态路由下一跳信息的调试信息开关处于关闭状态。

表1-1 debugging ipv6 route-static nib命令输出信息描述表

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

Topology

拓扑名称，目前IPv6不支持子拓扑，显示为空

【举例】

\# 打开IPv6单播静态路由邻居的调试信息开关。

\<Sysname\> debugging ipv6 route-static nib

\*Sep 20 10:51:41:770 2012 Sysname NIB/7/DEBUG: -MDC=1; USR add NIB 0041/0/0/0/0

/3::3, id 21000002 seq 5, errno 0

*// 添加NIB*

\*Sep 20 10:51:41:822 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR sync NIB 21000002 to RIB, msgtype ADD, bytes 104

*// 将NIB添加消息同步到RIB*

\*Sep 20 10:51:41:924 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR sync NIB 21000002 to RIB, msgtype MOD, bytes 192

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 3::3

  RelyDepth: 1              RealNexthop: 1:1::2

  Interface: GE1/0/2          LocalAddr: 1:1::3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

*// 将NIB修改消息同步到RIB*

\*Sep 20 10:51:41:975 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR re-rely route under NIB 21000002

*[// NIB*]*进行重新迭代*

\*Sep 20 10:51:42:127 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR modify NIB 21000001 with nexthop 2::2:

 Old value:

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 2::2

  RelyDepth: 1              RealNexthop: ::

  Interface: NULLL0           LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

 New value:

PrefixIndex: 0              OrigNexthop: 2::2

  RelyDepth: 2              RealNexthop: 1:1::2

  Interface: GE1/0/2          LocalAddr: 1:1::3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

*// 修改NIB*

\*Sep 20 10:51:52:670 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR modify NIB 21000001 with nexthop 2::2:

 Old value:

 1 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 2::2

  RelyDepth: 2              RealNexthop: 1:1::2

  Interface: GE1/0/2          LocalAddr: 1:1::3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

 New value:

 2 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 2::2

  RelyDepth: 2              RealNexthop: 1:1::2

  Interface: GE1/0/2          LocalAddr: 1:1::3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

PrefixIndex: 0              OrigNexthop: 2::2

  RelyDepth: 1              RealNexthop: ::

  Interface: NULLL0           LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

\*Sep 20 10:51:52:721 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR sync NIB 21000001 to RIB, msgtype MOD, bytes 400

 2 Nexthop Value(s):

PrefixIndex: 0              OrigNexthop: 2::2

  RelyDepth: 2              RealNexthop: 1:1::2

  Interface: GE1/0/2          LocalAddr: 1:1::3

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

PrefixIndex: 0              OrigNexthop: 2::2

  RelyDepth: 1              RealNexthop: ::

  Interface: NULLL0           LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

*// 修改NIB的内容*

\*Sep 20 10:52:00:745 2012 Sysname NIB/7/DEBUG: -MDC=1; USR delete NIB 21000002

with seq 5

*// 删除指定NIB*

\*Sep 20 10:52:00:796 2012 Sysname NIB/7/DEBUG: -MDC=1;

 USR sync NIB 21000002 to RIB, msgtype DEL, bytes 36

*// 同步删除消息到RIB*

**IPv6静态路由调试命令 \-- IPv6静态路由调试命令 \-- debugging ipv6 route-static process**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 route-static process**]

**[undo debugging ipv6 route-static process**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging ipv6 route-static process**]命令用来打开IPv6单播静态路由的调试信息开关。**undo debugging ipv6 route-static process**用来关闭IPv6单播静态路由的调试信息开关。

缺省情况下，IPv6单播静态路由的调试信息开关处于关闭状态。

表1-2 debugging ipv6 route-static process命令输出信息描述表

字段

含义

Add/Delete/Modify route

添加/删除/修改路由

NibID

邻居ID

【举例】

\# 打开IPv6单播静态路由的调试信息开关。

\<Sysname\> debugging ipv6 route-static process

%May  9 10:52:33:645 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 Add static route 1::/96

%May  9 11:13:24:652 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 USR: Add route 3::3/128 with NibID 0x21000000 to RIB

*// 添加目的地址为1::/96的IPv6静态路由*

%May  9 10:52:50:764 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 Add static route 1::/96

%May  9 10:52:50:764 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 USR: Modify route 1::/96 with NibID 0x21000000

*// 修改目的地址为1::/96的IPv6静态路由*

%May  9 10:53:25:398 2012 Sysname STATICRT/7/DEBUG: -MDC=1;

 USR: Delete route 1::/96 with NibID 0x21000000

*// 删除目的地址为1::/96的IPv6静态路由*
