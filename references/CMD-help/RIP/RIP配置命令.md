<!-- CMD-INDEX
  checkzero                           | RIP视图            | L56
  default cost                        | RIP视图            | L98
  default-route                       | RIP视图            | L148
  display rip                         | 任意视图             | L204
  display rip database                | 任意视图             | L420
  display rip graceful-restart        | 任意视图             | L506
  display rip interface               | 任意视图             | L584
  display rip neighbor                | 任意视图             | L710
  display rip non-stop-routing        | 任意视图             | L798
  display rip route                   | 任意视图             | L870
  fast-reroute                        | RIP视图            | L1058
  filter-policy export                | RIP视图            | L1144
  filter-policy import                | RIP视图            | L1242
  graceful-restart                    | RIP视图            | L1336
  graceful-restart interval           | RIP视图            | L1382
  host-route                          | RIP视图            | L1428
  import-route                        | RIP视图            | L1472
  maximum load-balancing              | RIP视图            | L1540
  network                             | RIP视图            | L1598
  non-stop-routing                    | RIP视图            | L1654
  output-delay                        | RIP视图            | L1700
  peer                                | RIP视图            | L1744
  preference                          | RIP视图            | L1796
  reset rip process                   | 用户视图             | L1848
  reset rip statistics                | 用户视图             | L1884
  rip                                 | 系统视图             | L1918
  rip authentication-mode             | ]                | L1968
  rip bfd enable                      | 接口视图             | L2054
  rip bfd enable destination          | 接口视图             | L2118
  rip default-route                   | 接口视图             | L2180
  rip enable                          | 接口视图             | L2266
  rip input                           | 接口视图             | L2330
  rip max-packet-length               | 接口视图             | L2380
  rip metricin                        | 接口视图             | L2448
  rip metricout                       | 接口视图             | L2538
  rip mib-binding                     | 系统视图             | L2628
  rip output                          | 接口视图             | L2674
  rip output-delay                    | 接口视图             | L2724
  rip poison-reverse                  | 接口视图             | L2784
  rip primary-path-detect bfd echo    | 接口视图             | L2834
  rip split-horizon                   | 接口视图             | L2910
  rip summary-address                 | 接口视图             | L2968
  rip triggered                       | 接口视图             | L3034
  rip version                         | 接口视图             | L3082
  silent-interface                    | RIP视图            | L3166
  summary                             | RIP视图            | L3230
  timer triggered                     | RIP视图            | L3278
  timers                              | RIP视图            | L3330
  trip retransmit count               | RIP视图            | L3398
  trip retransmit timer               | RIP视图            | L3446
  validate-source-address             | RIP视图            | L3494
  version                             | RIP视图            | L3532
-->

**RIP \-- RIP配置命令 \-- checkzero**

------------------------------------------------------------------------

**[checkzero**]命令用来使能RIP-1报文的零域检查功能。

**[undo checkzero**]命令用来关闭零域检查功能。

【命令】

**[checkzero**]

**[undo checkzero**]

【缺省情况】

RIP-1报文的零域检查功能处于使能状态。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能零域检查功能后，零域中包含非零位的RIP-1报文将被拒绝处理。如果用户能确保所有报文都是可信任的，则可以不进行该项检查，以节省CPU处理时间。

【举例】

\# 关闭进程号为1的RIP进程对RIP-1报文的零域检查功能。

\<Sysname\> system-view

Sysname rip

Sysname-rip-1 undo checkzero

**RIP \-- RIP配置命令 \-- default cost**

------------------------------------------------------------------------

**[default cost**]命令用来配置引入路由的缺省度量值。

**[undo default cost**]命令用来恢复缺省情况。

【命令】

**[default cost ***value*]

**[undo default cost**]

【缺省情况】

引入路由的缺省度量值为0。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：引入路由的缺省度量值，取值范围为0～16。

【使用指导】

当使用**import-route**命令从其它协议引入路由时，如果不指定具体的度量值，则引入路由的度量值为**default cost**所指定的值。

【举例】

\# 配置从其它路由协议引入路由的缺省度量值为3。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 default cost 3

【相关命令】

·**import-route**

**RIP \-- RIP配置命令 \-- default-route**

------------------------------------------------------------------------

**[default-route**]命令用来配置RIP进程下的所有接口以指定度量值向RIP邻居发布一条缺省路由。

**[undo default-route**]命令用来恢复缺省情况。

【命令】

**[default-route**[ { **only** \| **originate** } [ **cost** *cost* \| **route-policy** *route-policy-name* ] \*]]

**[undo default-route**]

【缺省情况】

不向RIP邻居发送缺省路由。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[only**]：配置只发送缺省路由，不发送普通路由。

**[originate**]：配置既发送普通路由，又发送缺省路由。

*[cost*]：缺省路由的度量值，取值范围为1～15，缺省值为1。

**[route-policy ***route-policy-name*]：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。只有当前路由器的路由表中有路由匹配*route-policy-name*指定的路由策略时，才发送缺省路由。

【使用指导】

配置了发布缺省路由的RIP路由器不接收来自RIP邻居的缺省路由。

【举例】

\# 配置RIP进程100的所有接口向RIP邻居发布一条度量值为2的缺省路由，而且只发送缺省路由，不发送普通路由。

\<Sysname\> system-view

Sysname rip 100

Sysname-rip-100 default-route only cost 2

【相关命令】

·**rip default-route**

**RIP \-- RIP配置命令 \-- display rip**

------------------------------------------------------------------------

**[display rip**]命令用来显示RIP的当前运行状态及配置信息。

【命令】

**[display rip** [ *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。如果未指定本参数，则显示所有RIP进程的当前运行状态及配置信息。

【举例】

\# 显示所有RIP进程的当前运行状态及配置信息。

\<Sysname\> display rip

  Public VPN-instance name:

    RIP process: 1

       RIP version: 1

       Preference: 100

           Routing policy: abc

       Fast-reroute:

           Routing policy: frr

       Checkzero: Enabled

       Default cost: 0

       Summary: Enabled

       Host routes: Enabled

       Maximum number of load balanced routes: 8

       Update time   :   30 secs  Timeout time         :  180 secs

       Suppress time :  120 secs  Garbage-collect time :  120 secs

       Update output delay:   20(ms)  Output count:    3

       Silent interfaces: None

       Default routes: Originate  Default routes cost: 3

       Verify-source: Enabled

       Networks:

           1.0.0.0

       Configured peers:

           197.168.6.2

       Triggered updates sent: 0

       Number of routes changes: 1

       Number of replies to queries: 0

表1-1 display rip命令显示信息描述表

字段

描述

Public VPN-instance name/Private VPN-instance name

RIP进程运行在公网实例下/RIP进程应用于指定VPN实例

RIP process

RIP进程号

RIP version

RIP版本

Preference

RIP路由优先级

Fast-reroute

RIP快速重路由

Routing policy

路由策略

Checkzero

是否使能对RIP-1报文的零域进行检查的功能

·Enable表示已使能

·Disabled表示关闭

Default cost

引入路由的缺省度量值

Summary

路由聚合功能是否使能

·Enabled表示已使能

·Disabled表示关闭

Host routes

是否允许接收主机路由

·Enabled表示允许

·Disabled表示不允许

Maximum number of load balanced routes

等价路由的最大数目

Update time

Update定时器的值，单位为秒

Timeout time

Timeout定时器的值，单位为秒

Suppress time

Suppress定时器的值，单位为秒

Update output delay

接口发送RIP报文的时间间隔

Output count

接口一次发送RIP报文的最大个数

Garbage-collect time

Garbage-Collect定时器的值，单位为秒

Silent interfaces

工作在抑制状态的接口（这些接口不发送周期更新报文）

Default routes

是否向RIP邻居发布一条缺省路由

·Only：表示只发布缺省路由

·Originate：表示同时发布缺省路由和普通路由

·Disabled：表示不发布缺省路由

Default routes cost

RIP进程下发布缺省路由的度量值

Verify-source

是否使能对接收到的RIP路由更新报文进行源IP地址检查的功能

·Enable表示已使能

·Disabled表示关闭

Networks

使能RIP的网段地址

Configured peers

配置的邻居

Triggered updates sent

发送的触发更新报文数

Number of routes changes

RIP进程改变路由数据库的统计数据

Number of replies to queries

RIP请求的响应报文数

**RIP \-- RIP配置命令 \-- display rip database**

------------------------------------------------------------------------

**[display rip** **database**]命令用来显示RIP数据库的激活路由，这些路由以常规RIP更新报文的形式发送。

【命令】

**[display rip**[ *process-id* **database** [ *ip-address* { *mask-length* \| *mask* } ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[ip-address*[ { *mask-length* \| *mask* }]]：显示指定目的地址和掩码的激活路由信息。如果未指定本参数，将显示RIP的所有激活路由信息。

【举例】

\# 显示RIP进程100数据库的所有激活路由。

\<Sysname\> display rip 100 database

   1.0.0.0/8, auto-summary

       1.1.1.0/24, cost 16, interface summary

       1.1.1.0/24, cost 0, nexthop 1.1.1.1, RIP-interface

       1.1.2.0/24, cost 0, imported

   2.0.0.0/8, auto-summary

   2.0.0.0/8, cost 1, nexthop 1.1.1.2

\# 显示RIP进程100数据库中指定地址和掩码为1.1.1.0/24的激活路由。

\<Sysname\> display rip 100 database 1.1.1.0 24

   1.1.1.0/24, cost 16, interface summary

   1.1.1.0/24, cost 0, nexthop 1.1.1.1, RIP-interface

表1-2 display rip database命令显示信息描述表

字段

描述

cost

度量值

auto-summary

表示该条路由是RIP的自动聚合路由

interface summary

表示该条路由是RIP的接口聚合路由

nexthop

下一跳地址

RIP-interface

使能RIP协议的接口的直连路由

imported

表示该条路由是从其它路由协议引入的

**RIP \-- RIP配置命令 \-- display rip graceful-restart**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display rip graceful-restart**]命令用来显示RIP进程的GR状态信息。

【命令】

**[display rip** [ *process-id*  **graceful-restart**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。如果未指定本参数，则显示所有RIP进程的GR状态信息。

【举例】

\# 显示RIP 1进程的GR状态信息。

\<Sysname\> display rip 1 graceful-restart

 RIP process: 1

 Graceful Restart capability     : Enabled

 Current GR state                : Normal

 Graceful Restart period         : 60  seconds

 Graceful Restart remaining time : 0   seconds

表1-3 display rip graceful-restart命令显示信息描述表

字段

描述

Graceful Restart capability

GR使能状态

·Enabled：使能了GR能力

·Disabled：关闭了GR能力

Current GR state

当前GR所处状态

·Under GR：进程正在GR

·Normal：普通状态

Graceful Restart period

GR重启间隔时间

Graceful Restart remaining time

GR结束剩余时间

**RIP \-- RIP配置命令 \-- display rip interface**

------------------------------------------------------------------------

**[display rip interface**]命令用来显示RIP的接口信息。

【命令】

**[display rip ***process-id*** interface ** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示RIP的所有接口信息。

【举例】

\# 显示RIP进程1的接口信息。

\<Sysname\> display rip 1 interface

 Interface: GigabitEthernet1/0/2

    Address/Mask: 1.1.1.1/24          Version: RIPv1

    MetricIn: 0                       MetricIn route policy: Not designated

    MetricOut: 1                      MetricOut route policy: Not designated

    Split-horizon/Poison-reverse: On/Off  Input/Output: On/On

    Default route: Off

    Update output delay:  20(ms)      Output count: 3

    Current number of packets/Maximum number of packets: 0/2000

表1-4 display rip interface命令显示信息描述表

字段

描述

Interface

运行RIP协议的接口的名称

Address/Mask

运行RIP协议的接口的IP地址/掩码

Version

接口上运行的RIP协议的版本

MetricIn

接收路由的附加度量值

MetricIn route policy

接收路由的附加度量值应用的路由策略，取值为Not designated表示没有对接收路由的附加度量值使用路由策略，如果对接收路由的附加度量值使用了路由策略，取值为使用的路由策略名称

MetricOut

发送路由的附加度量值

MetricOut route policy

发送路由的附加度量值应用的路由策略，取值为Not designated表示没有对发送路由的附加度量值使用路由策略，如果对发送路由的附加度量值使用了路由策略，取值为使用的路由策略名称

Split-horizon

是否使能了水平分割（On表示使能，Off表示关闭）

Poison-reverse

是否使能了毒性逆转（On表示使能，Off表示关闭）

Input/Output

是否允许接口接收（Input）/发送（Output）RIP报文（On表示允许，Off表示不允许）

Default route

是否允许向RIP邻居发送缺省路由

·Only：表示只发布缺省路由

·Originate：表示同时发布缺省路由和普通路由

·No-originate：表示只发布普通路由

·Off：表示不发布缺省路由

Default route cost

RIP接口下配置发布缺省路由的度量值

Update output delay

接口发送RIP报文的时间间隔

Output count

接口一次发送RIP报文的最大个数

Current number of packets /Maximum number of packets

显示当前接口待发送的报文数量和最多可以发送的报文数量

**RIP \-- RIP配置命令 \-- display rip neighbor**

------------------------------------------------------------------------

**[display rip neighbor**]命令用来显示RIP进程的邻居信息。

【命令】

**[display rip ***process-id*** neighbor ** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示RIP的所有邻居信息。

【举例】

\# 显示RIP进程1的邻居信息。

\<Sysname\> display rip 1 neighbor

 Neighbor address: 197.168.2.3 (TRIP)

     Interface  : Serial3/0/3

     Version    : RIPv2     Last update: 00h00m02s

     Relay nbr  : N/A       BFD session: N/A

     Bad packets: 0         Bad routes : 0

表1-5 display rip neighbor命令显示信息描述表

字段

描述

Neighbor address

邻居地址

Interface

出接口

Version

收到邻居RIP报文的版本

Last update

上次收到邻居更新报文距离现在时间

Relay nbr

是否是非直连邻居

BFD session

BFD会话类型

Bad packets

接口收到的错误报文数目

Bad routes

接口收到的错误路由数目

TRIP

TRIP邻居

**RIP \-- RIP配置命令 \-- display rip non-stop-routing**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display rip** **non-stop-routing**]命令用来显示RIP进程的NSR状态信息。

【命令】

**[display rip** [ *process-id*  **non-stop-routing**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。如果未指定本参数，则显示所有RIP进程的NSR状态信息。

【举例】

\# 显示RIP 1进程的NSR状态信息。

\<Sysname\> display rip 1 non-stop-routing

RIP process: 1

 Nonstop Routing capability: Enabled

 Current NSR state         : Finish

表1-6 display rip non-stop-routing命令显示信息描述表

字段

描述

Nonstop Routing capability

NSR使能状态

·Enabled：使能NSR

·Disabled：不使能NSR

Current NSR state

当前NSR所处状态

·Initialization：初始准备

·Smooth：数据平滑

·Advertising：发布路由

·Redistribution：路由引入处理

·Finish：完成

**RIP \-- RIP配置命令 \-- display rip route**

------------------------------------------------------------------------

**[display rip route**]命令用来显示RIP的路由信息。

【命令】

**[display rip ***process-id*** route **[[ *ip-address* { *mask-length* \| *mask* } [ **verbose** ] \| **peer** *ip-address* \| **statistics** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

*[ip-address*[ { *mask-length* \| *mask* }]]：显示指定目的地址和掩码的路由信息。

**[verbose**]：显示当前RIP路由表中指定目的地址和掩码的所有路由信息。如果未指定本参数，则只显示指定目的地址和掩码的最优RIP路由。

**[peer ***ip-address*]：显示从指定邻居学到的所有路由信息。

**[statistics**]：显示路由的统计信息。路由的统计信息包括路由总数目，各个邻居的路由数目。

【使用指导】

如果未指定任何参数，将显示RIP的所有路由信息。

【举例】

\# 显示进程号为1的RIP进程所有的路由信息。

\<Sysname\> display rip 1 route

 Route Flags: R -- RIP

              A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct

              O - Optimal, F - Flush to RIB

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Peer 1.1.1.1 on GigabitEthernet1/0/2

      Destination/Mask        Nexthop           Cost    Tag     Flags   Sec

      3.0.0.0/8               1.1.1.1           1       0       RAOF    24

 Local route

      Destination/Mask        Nexthop           Cost    Tag     Flags   Sec

      4.4.4.4/32              0.0.0.0           0       0       RDOF    -

      1.1.1.0/24              0.0.0.0           0       0       RDOF    -

\# 显示进程号为1的RIP进程指定路由的全部路由信息。

\<Sysname\> display rip 1 route 3.0.0.0 8 verbose

 Route Flags: R -- RIP

              A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct

              O - Optimal, F - Flush to RIB

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Peer 1.1.1.1 on GigabitEthernet1/0/2

  Destination/Mask    OrigNexthop/RealNexthop          Cost  Tag   Flags Sec

  3.0.0.0/8           1.1.1.1/1.1.1.1                  1     0     RAOF  16

表1-7 display rip route命令显示信息描述表

字段

描述

Route Flags

路由标志：

·R：RIP生成的路由

·A：该路由处于老化时期

·S：该路由处于抑制时期

·G：该路由处于Garbage-collect时期

·D：RIP生成的直连路由

·O：该路由处于最优路由状态

·F：该路由已经被下刷到RIB

Peer *X.X.X.X* on *interface-type interface-number*

在RIP接口上从指定邻居学到的路由信息

Local route

RIP本地生成的直连路由

Destination/Mask

目的IP地址/掩码

Nexthop

路由的下一跳地址

OrigNexthop/RealNexthop

如果路由来自直连邻居，那么路由的真实下一跳就是原始下一跳；如果路由来自非直连邻居，对于成功迭代的路由RealNexthop则显示迭代出来的下一跳，否则不显示

Cost

度量值

Tag

路由标记

Flags

路由信息所处状态

Sec

路由信息所处状态对应的定时器时间

\# 显示进程号为1的RIP进程的路由统计信息。

\<Sysname\> display rip 1 route statistics

 Peer              Optimal/Aging        Garbage

 1.1.1.1           1/1                  0

 Local             2/0                  0

 Total             3/1                  0

表1-8 display rip route statistics命令显示信息描述表

字段

描述

Peer

RIP邻居IP地址

Optimal

路由信息中处于最优路由状态的路由条数

Aging

路由信息中处于老化状态的路由条数

Garbage

路由信息中处于Garbage-collection状态的路由条数

Local

RIP本地生成的直连路由条数的总和

Total

从所有RIP邻居学习到的路由条数的总和

**RIP \-- RIP配置命令 \-- fast-reroute**

------------------------------------------------------------------------

![说明](RIP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[fast-reroute**]命令用来配置RIP快速重路由功能。

**[undo fast-reroute**]命令用来关闭RIP快速重路由功能。

【命令】

**[fast-reroute route-policy ***route-policy-name*]

**[undo fast-reroute**]

【缺省情况】

RIP快速重路由功能处于关闭状态。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-policy*** route-policy-name*]：为通过策略的路由指定备份下一跳。*route-policy-name*为路由策略名，为1～63个字符的字符串，区分大小写。

【使用指导】

·RIP快速重路由功能只适合在主链路三层接口up，主链路由双通变为单通或者不通的情况下使用。在主链路三层接口down的情况下，本功能不可用。单通现象，即一条链路上的两端，有且只有一端可以收到另一端发来的报文，此链路称为单向链路。

·RIP快速重路由功能仅对非迭代RIP路由（即从直连邻居学到RIP路由）有效。

·RIP快速重路由功能不能与RIP支持BFD检测功能同时使用，否则可能导致快速重路由功能失效。

·等价路由不支持快速重路由功能，当备份信息与主路由信息相同时该功能不生效。

【举例】

\# 配置对通过策略frr的路由指定备份下一跳信息。

·路由应用

\<Sysname\> system-view

Sysname ip prefix-list abc index 10 permit 100.1.1.0 24

Sysname route-policy frr permit node 10

Sysname-route-policy-frr-10 if-match ip address prefix-list abc

Sysname-route-policy-frr-10 apply fast-reroute backup-interface gigabitethernet 1/0/1 backup-nexthop 193.1.1.8

Sysname-route-policy-frr-10 quit

Sysname rip 100

Sysname-rip-100 fast-reroute route-policy frr

·交换应用

\<Sysname\> system-view

Sysname ip prefix-list abc index 10 permit 100.1.1.0 24

Sysname route-policy frr permit node 10

Sysname-route-policy-frr-10 if-match ip address prefix-list abc

Sysname-route-policy-frr-10 apply fast-reroute backup-interface vlan-interface 1 backup-nexthop 193.1.1.8

Sysname-route-policy-frr-10 quit

Sysname rip 100

Sysname-rip-100 fast-reroute route-policy frr

**RIP \-- RIP配置命令 \-- filter-policy export**

------------------------------------------------------------------------

**[filter-policy export**]命令用来配置RIP对发布的路由信息进行过滤。

**[undo filter-policy export**]命令用来取消对发布路由信息的过滤。

【命令】

**[filter-policy**[ { *acl-number* \| **prefix-list** *prefix-list-name* } **export** [ *protocol* [ *process-id* ] \| *interface-type* *interface-number* ]]]

**[undo filter-policy** **export** [ *protocol* [ *process-id*  \| *interface-type interface-number* ]]]

【缺省情况】

RIP不对发布的路由信息进行过滤。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：用于过滤发布的路由信息的访问控制列表号，取值范围为2000～3999。

**[prefix-list** *prefix-list-name*]：指定用于过滤发布路由信息的IP地址前缀列表名称。*prefix-list-name*为IP地址前缀列表名称，为1～63个字符的字符串，区分大小写。

*[protocol*]：过滤指定路由协议发布的路由信息，*protocol*可以选择**bgp**、**direct**、**isis**、**ospf**、**rip**和**static**。

*[process-id*]：被过滤路由信息的路由协议的进程号，取值范围为1～65535。仅当路由协议为**rip**、**ospf**、**isis**时需要指定进程号，若未指定，缺省进程号为1。

*[interface-type* *interface-number*]：过滤指定接口发布的路由信息，*interface-type* *interface-number*为接口类型和编号。

【使用指导】

·一个协议或接口只能配置一个过滤策略。如果未指定协议或接口，就认为是配置全局过滤策略，同样每次只能配置一个。如果重复配置，新的策略将覆盖之前的策略。

·如果已经配置了基于协议或接口的过滤策略，删除时必须指定*protocol*或*[interface-type*]{.varname} [*interface-number*{.varname}]。{.varname}

l当配置的是高级ACL（3000～3999）时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]来过滤指定目的地址和掩码的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。

【举例】

\# 配置使用编号为2000的基本ACL来对发布的路由信息进行过滤。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule deny source 192.168.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname rip 1

Sysname-rip-1 filter-policy 2000 export

\# 配置按照地址前缀列表来过滤发布的路由信息。

\<Sysname\> system-view

Sysname ip prefix-list abc index 10 permit 11.0.0.0 8

Sysname rip 1

Sysname-rip-1 filter-policy prefix-list abc export

\# 使用编号为3000的高级ACL对发布的路由进行过滤，只允许113.0.0.0/16通过。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0

Sysname-acl-ipv4-adv-3000 rule 100 deny ip

Sysname-acl-ipv4-adv-3000 quit

Sysname rip 1

Sysname-rip 1 filter-policy 3000 export

【命令参考】

·**acl**（ACL和QoS命令参考/ACL）

·**import-route**

·**ip prefix****-list**（三层技术-IP路由命令参考/路由策略）

**RIP \-- RIP配置命令 \-- filter-policy import**

------------------------------------------------------------------------

**[filter-policy import**]命令用来配置RIP对接收的路由信息进行过滤。

**[undo filter-policy import**]命令用来取消该配置。

【命令】

**[filter-policy**[ { *acl-number* \| **gateway** *prefix-list-name* \| **prefix-list** *prefix-list-name* [ **gateway** *prefix-list-name* ] } **import**  *interface-type* *interface-number* ]]

**[undo filter-policy** **import** [ *interface-type* *interface-number* ]]

【缺省情况】

RIP不对接收的路由信息进行过滤。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：用于过滤发布的路由信息的访问控制列表号，取值范围为2000～3999。

**[prefix-list ***prefix-list-name*]：指定用于过滤接收路由信息的IP地址前缀列表名称。*prefix-list-name*为IP地址前缀列表名称，为1～63个字符的字符串，区分大小写。

**[gateway** *prefix-list-name*]：基于要加入到路由表的路由信息的下一跳进行过滤。*prefix-list-name*为IP地址前缀列表名称，为1～63个字符的字符串，区分大小写。

*[interface-type interface-number*]：过滤指定接口接收的路由信息，*interface-type* *interface-number*为接口类型和编号。

【使用指导】

·一个接口只能配置一个过滤策略。如果未指定接口，就认为是配置全局过滤策略，同样每次只能配置一个。如果重复配置，新的策略将覆盖之前的策略。

·如果已经配置了基于接口的过滤策略，删除时必须指定*[interface-type*]{.varname} [*interface-number*{.varname}]。{.varname}

·当配置的是高级ACL（3000～3999）时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]来过滤指定目的地址和掩码的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。

【举例】

\# 配置使用编号为2000的基本ACL来对接收的路由信息进行过滤。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule deny source 192.168.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname rip 1

Sysname-rip-1 filter-policy 2000 import

\# 配置按照地址前缀列表来过滤接收的路由信息。

\<Sysname\> system-view

Sysname ip prefix-list abc index 10 permit 11.0.0.0 8

Sysname rip 1

Sysname-rip-1 filter-policy prefix-list abc import

\# 使用编号为3000的高级ACL对接收的路由进行过滤，只允许113.0.0.0/16通过。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0

Sysname-acl-ipv4-adv-3000 rule 100 deny ip

Sysname-acl-ipv4-adv-3000 quit

Sysname rip 1

Sysname-rip-1 filter-policy 3000 import

【命令参考】

·**acl**（ACL和QoS命令参考/ACL）

·**ip prefix****-list**（三层技术-IP路由命令参考/路由策略）

**RIP \-- RIP配置命令 \-- graceful-restart**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart**]命令用来使能RIP协议的GR能力。

**[undo graceful-restart**]命令用来关闭RIP协议的GR能力。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

RIP协议的GR能力处于关闭状态。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RIP GR特性与RIP NSR特性互斥，即**graceful-restart**和**non-stop-routing**命令互斥，不能同时配置。

【举例】

\# 使能RIP进程1的GR能力。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 graceful-restart

**RIP \-- RIP配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart interval**]命令用来配置RIP协议的GR重启间隔时间。

**[undo graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[graceful-restart interval ***interval-value*]

**[undo graceful-restart interval**]

【缺省情况】

RIP协议的GR重启间隔时间为60秒。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：GR重启间隔时间，取值范围是5～360，单位是秒。

【举例】

\# 配置RIP进程1的GR重启间隔时间为200秒。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 graceful-restart interval 200

**RIP \-- RIP配置命令 \-- host-route**

------------------------------------------------------------------------

**[host-route**]命令用来允许RIP接收主机路由。

**[undo host-route**]命令用来禁止RIP接收主机路由。

【命令】

**[host-route**]

**[undo host-route**]

【缺省情况】

允许RIP接收主机路由。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

l在某些特殊情况下，路由器会收到大量来自同一网段的主机路由。这些路由对于路由寻址没有多少作用，却占用了大量的资源；此时可以使用**undo host-route**命令禁止接收主机路由，以节省网络资源。

l该命令仅对RIPv2报文携带的路由有效，对RIPv1报文携带的路由无效。

【举例】

\# 禁止RIP接收主机路由。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 undo host-route

**RIP \-- RIP配置命令 \-- import-route**

------------------------------------------------------------------------

**[import-route**]命令用来从其它路由协议引入路由。

**[undo import-route**]命令用来取消引入外部路由信息。

【命令】

**[import-route ***protocol*[ [ *process-id* \| **all-processes** \| **allow-ibgp**   **allow-direct** \| **cost** *cost* \| **route-policy** *route-policy-name* ] [\| **tag** *tag* ]]] \*

**[undo import-route **]*protocol* [ *process-id* [\| **all-processes** ]]

【缺省情况】

RIP不引入其它路由。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：指定引入的路由协议，可以是**bgp**、**direct**、**isis**、**ospf**、**rip**或**static**。

*[proces*s-*id*]：路由协议进程号，取值范围为1～65535，缺省值为1。只有当*protocol*是**isis**、**ospf**或**rip**时该参数可选。

**[all-processes**]：引入指定路由协议所有进程的路由，只有当*protocol*是**rip**、**ospf**或**isis**时可以指定该参数。

**[allow-ibgp**]：当*protocol*为**bgp**时，**allow-ibgp**为可选关键字。

**[allow-direct**]：在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入协议路由时不会包含使能了该协议的接口网段路由。当**allow-direct**与**route-policy** *route-policy-name*参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致**allow-direct**配置失效。例如，当配置**allow-direct**参数引入OSPF直连时，在路由策略中不要配置**if-match** **route-type**匹配条件，否则，**allow-direct**参数失效。

**[cost*** cost*]：所要引入路由的度量值，取值范围为0～16，缺省值为0。

**[route-policy **]*route-policy-name*：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag*** tag*]：所要引入路由的标记值，取值范围为0～65535，缺省值为0。

【使用指导】

l**import-route***bgp*表示只引入EBGP路由；**import-route ***bgp*** allow-ibgp**表示将IBGP路由也引入，容易引起路由环路，请慎用。

l只能引入路由表中状态为active的路由，是否为active状态可以通过**displayiprouting-table protocol**命令来查看。

·**undo import-route** *protocol* **all-processes**命令只能取消**import-route** *protocol* **all-processes**命令的配置，不能取消**import-route** *protocol* *process-id*命令的配置。

【举例】

\# 引入静态路由，并将其度量值设置为4。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 import-route static cost 4

【命令参考】

·**default cost**

**RIP \-- RIP配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

![说明](RIP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[maximum load-balancing**]命令用来配置RIP最大等价路由条数。

**[undo maximum load-balancing**]命令用来恢复缺省情况。

【命令】

**[maximum load-balancing** *number*]

**[undo maximum load-balancing**]

【缺省情况】

RIP支持的等价路由的最大条数与系统支持最大等价路由的条数相同。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：等价路由的最大条数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

如果通过**max-ecmp-num**命令配置系统支持最大等价路由的条数为m，则本命令的缺省值为m，取值范围为1～m。

**[max-ecmp-num**]命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置RIP最大等价路由条数为2。

\<Sysname\> system-view

Sysname rip

Sysname-rip-1 maximum load-balancing 2

【相关命令】

·**max-ecmp-num**（三层技术-IP路由命令参考/IP路由基础）

**RIP \-- RIP配置命令 \-- network**

------------------------------------------------------------------------

**[network**]命令用来在指定网段上使能RIP。

**[undo network**]命令用来在指定网段上禁用RIP。

【命令】

**[network ***network-address * *wildcard-mask* ]

**[undo** **network** *network-address*]

【缺省情况】

没有网段使能RIP。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[network-address*]：指定网段的地址，其取值可以为各个接口的IP网络地址。

*[wildcard-mask*]：IP地址掩码的反码，相当于将IP地址的掩码取反（0变1，1变0）。其中，"1"表示忽略IP地址中对应的位，"0"表示必须保留此位。（例如：子网掩码255.0.0.0，该掩码的反码为0.255.255.255）。如果未指定本参数，将按照自然网段进行。

【使用指导】

RIP只在指定网段的接口上运行，指定网段可以配置掩码；对于不在指定网段上的接口，RIP既不在它上面接收和发送路由，也不将它的接口路由发布出去。因此，RIP启动后必须指定其工作网段。

·在单进程情况下，可以使用**network **0.0.0.0命令在所有接口上使能RIP；在多进程情况下，无法使用**network **0.0.0.0命令。

·RIP不支持将同一物理接口下的不同网段使能到不同的RIP进程中。

【举例】

\# 在指定网段129.102.0.0上使能RIP进程100。

\<Sysname\> system-view

Sysname rip 100

Sysname-rip-100 network 129.102.0.0

【相关命令】

·**rip enable**

**RIP \-- RIP配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[non-stop-routing**]命令用来使能RIP协议的NSR功能。

**[undo non-stop-routing**]命令用来关闭RIP协议的NSR功能。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【缺省情况】

RIP协议的NSR功能处于关闭状态。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RIP NSR特性与RIP GR特性互斥，即**non-stop-routing**和**graceful-restart**命令互斥，不能同时配置。

【举例】

\# 配置RIP进程1使能NSR功能。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 non-stop-routing

**RIP \-- RIP配置命令 \-- output-delay**

------------------------------------------------------------------------

**[output-delay**]用来配置RIP报文的发送速率。

**[undo output-delay**]命令用来恢复缺省情况。

【命令】

**[output-delay*** time ***count ***count*]

**[undo output-delay**]

【缺省情况】

接口发送RIP报文的时间间隔为20毫秒，一次最多发送3个RIP报文。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：接口发送RIP报文的时间间隔，取值范围为10～100，单位为毫秒。

*[count*]：接口一次发送RIP报文的最大个数，取值范围为1～30。

【举例】

\# 配置RIP进程1的所有接口发送RIP报文的时间间隔为60毫秒，一次最多发送10个RIP报文。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 output-delay 60 count 10

**RIP \-- RIP配置命令 \-- peer**

------------------------------------------------------------------------

**[peer**]命令用来配置NBMA（Non-Broadcast Multi-Access，非广播多路访问）网络中RIP邻居的IP地址，并使更新报文以单播形式发送到对端，而不采用正常的组播或广播的形式。

**[undo peer**]命令用来取消指定邻居IP地址。

【命令】

**[peer*** ip-address*]

**[undo peer ***ip-address*]

【缺省情况】

RIP不向任何定点地址发送单播更新报文。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：RIP邻居IP地址，用点分十进制格式表示。

【使用指导】

当RIP邻居与当前设备直连时不推荐使用该命令，因为这样可能会造成对端同时收到同一路由信息的组播（或广播）和单播两种形式的报文。

配置本命令时，必须同时配置**undo** **validate-source-address**命令，即取消对接收到的RIP路由更新报文进行源IP地址检查。

【举例】

\# 配置RIP邻居的IP地址为202.38.165.1。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 peer 202.38.165.1

【相关命令】

·**validate-source-address**

**RIP \-- RIP配置命令 \-- preference**

------------------------------------------------------------------------

**[preference**]命令用来配置RIP路由的优先级。

**[undo preference**]命令用来恢复缺省情况。

【命令】

**[preference****[{ *preference* \| **route-policy** *route-policy-name* } \*]]

**[undo preference**]

【缺省情况】

RIP路由的优先级为100。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference*]：RIP路由优先级的值，取值范围为1～255，取值越小，优先级越高。

**[route-policy **]*route-policy-name*：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。对满足特定条件的路由设置优先级。

【使用指导】

通过指定**route-policy**参数，可应用路由策略对特定的路由设置优先级：

·如果在路由策略中已经设置了匹配路由的优先级，则匹配路由取路由策略设置的优先级，其它路由取**preference**命令所设优先级。

·如果在路由策略中没有设置匹配路由的优先级，则所有路由都取**preference**命令所设优先级。

【举例】

\# 配置RIP路由的优先级为120。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 preference 120

**RIP \-- RIP配置命令 \-- reset rip process**

------------------------------------------------------------------------

**[reset rip process**]命令用来重启指定RIP进程。

【命令】

**[reset rip **]*process-id***process**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

【使用指导】

执行该命令后，系统提示用户确认是否重启RIP协议。

【举例】

\# 重启进程号为100的RIP进程。

\<Sysname\> reset rip 100 process  

Reset RIP process? [Y/N:y]

**RIP \-- RIP配置命令 \-- reset rip statistics**

------------------------------------------------------------------------

**[reset rip statistics**]命令用来清除指定RIP进程的统计信息，便于在调试时重新记录统计数据。

【命令】

**[reset rip **]*process-id* **statistics**

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

【举例】

\# 清除进程号为100的RIP进程的统计信息。

\<Sysname\> reset rip 100 statistics

**RIP \-- RIP配置命令 \-- rip**

------------------------------------------------------------------------

**[rip**]命令用来启动RIP，并进入RIP视图。

**[undo rip**]命令用来关闭RIP。

【命令】

**[rip** [ *process-id*   **vpn-instance** *vpn-instance-name* ]]

**[undo rip** [ *process-id* ]]

【缺省情况】

系统没有运行RIP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535，缺省值为1。

**[vpn-instance*** vpn-instance-name*]：指定RIP所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示RIP位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·必须先启动RIP进程，才能配置RIP的各种全局性参数，而配置与接口相关的参数时，可以不受这个限制。

·关闭RIP进程后，原来配置的接口参数也同时失效。

【举例】

\# 启动RIP进程1，并进入RIP视图。

\<Sysname\> system-view

Sysname rip

Sysname-rip-1

**RIP \-- RIP配置命令 \-- rip authentication-mode**

------------------------------------------------------------------------

**[rip authentication-mode**]命令用来配置RIP-2的验证方式及验证参数。

**[undo rip authentication-mode**]命令用来取消所有验证。

【命令】

**[rip authentication-mode**]**[md5** [**[cipher***cipher-string*****[\| **plain** *plain-string* ]}[ *key-id* \| **rfc2453** ]**[cipher***cipher-string*****[\| **plain** *plain-string* ]}[ } \| ]**simple ****[cipher***cipher-string*****[\| **plain** *plain-string* ]}****}

**[undo rip authentication-mode**]

【缺省情况】]

接口没有配置]RIP-2的认证方式。

【视图】]

接口视图]

【缺省用户角色】]

network-admin

mdc-admin

【参数】

**[md5**]：MD5验证方式。

**[rfc2082**]：指定MD5验证报文使用RFC 2082规定的报文格式。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，为33～53个字符的字符串，区分大小写。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，为1～16个字符的字符串，区分大小写。

*[key-id*]：MD5 **rfc2082**验证标识符，取值范围为1～255。

**[rfc2453**]：指定MD5验证报文使用RFC 2453规定的报文格式（IETF标准）。

**[simple**]：简单验证方式。

【使用指导】

·每次验证只支持一个验证字，新输入的验证字将覆盖旧验证字。

·当RIP的版本为RIP-1时，虽然在接口视图下仍然可以配置验证方式，但由于RIP-1不支持认证，因此该配置不会生效。

·以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置RFC 2453格式的MD5明文验证，验证字为rose。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip version 2

Sysname-GigabitEthernet1/0/1 rip authentication-mode md5 rfc2453 plain rose

·交换应用

\# 在接口Vlan-interface10上配置RFC 2453格式的MD5明文验证，验证字为rose。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip version 2

Sysname-Vlan-interface10 rip authentication-mode md5 rfc2453 plain rose

【命令参考】

·**rip version**

**RIP \-- RIP配置命令 \-- rip bfd enable**

------------------------------------------------------------------------

![说明](RIP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rip bfd enable**]命令用来使能RIP的BFD功能。

**[undo rip bfd enable**]命令用来关闭RIP的BFD功能。

【命令】

**[rip bfd enable**]

**[undo rip bfd enable**]

【缺省情况】

RIP的BFD功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RIP支持采用BFD的直连echo检测方式和非直连control检测方式。

RIP的邻居是单跳的概念，适合采用BFD的echo单向检测方式，但是，经过多跳到达邻居时echo方式则会失效。

由于**peer**命令与邻居之间没有对应关系，**undo peer**操作并不能立刻删除邻居，因此不能立刻删除BFD会话。

本命令与**rip bfd enable**** destination**命令互斥，不能同时使用。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1使能RIP的BFD功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip bfd enable

·交换应用

\# 在接口Vlan-interface11使能RIP的BFD功能。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 rip bfd enable

**RIP \-- RIP配置命令 \-- rip bfd enable destination**

------------------------------------------------------------------------

![说明](RIP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rip bfd enable destination**]命令用来使能RIP指定目的地址的BFD功能。

**[undo rip bfd enable**]命令用来关闭RIP的BFD功能。

【命令】

**[rip bfd enable destination ***ip-address*]

**[undo rip bfd enable**]

【缺省情况】

RIP的BFD功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·该命令只支持采用BFD的直连echo检测方式。

·该命令与**rip bfd enable**命令互斥，不能同时使用。

·该命令指定了链路检测的目的地址，当到该目的地址的链路出现故障时，便不再从该接口收发任何RIP报文。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1使能RIP指定目的地址202.38.165.1的BFD功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip bfd enable destination 202.38.165.1

·交换应用

\# 在接口Vlan-interface10使能RIP指定目的地址202.38.165.1的BFD功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip bfd enable destination 202.38.165.1

**RIP \-- RIP配置命令 \-- rip default-route**

------------------------------------------------------------------------

**[rip default-route**]命令用来配置RIP接口以指定度量值向RIP邻居发布一条缺省路由。

**[undo rip default-route**]命令用来取消配置RIP接口向RIP邻居发布缺省路由。

【命令】

**[rip default-route**[ { { **only** \| **originate** } [ **cost** *cost* \| **route-policy** *route-policy-name* ] \* \| **no-originate** }]]

**[undo rip default-route**]

【缺省情况】

RIP接口是否发布缺省路由以RIP进程配置为准。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[only**]：配置只发送缺省路由，不发送普通路由。

**[originate**]：配置既发送普通路由，又发送缺省路由。

*[cost*]：缺省路由的度量值，取值范围为1～15，缺省值为1。

**[route-policy ***route-policy-name*]：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。只有当前路由器的路由表中有路由匹配*route-policy-name*指定的路由策略时，才发送缺省路由。

**[no-originate**]：配置只发送普通路由，不发布缺省路由。

【使用指导】

配置了发布缺省路由的RIP路由器不接收来自RIP邻居的缺省路由。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1以指定度量值2向RIP邻居发布一条缺省路由，而且只发送缺省路由，不发送普通路由。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip default-route only cost 2

\# 指定接口GigabitEthernet1/0/1以指定度量值4向RIP邻居既发布缺省路由，而且发送普通路由。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip default-route originate cost 4

·交换应用

\# 配置接口Vlan-interface10以指定度量值2向RIP邻居发布一条缺省路由，而且只发送缺省路由，不发送普通路由。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip default-route only cost 2

\# 指定接口Vlan-interface10以指定度量值2向RIP邻居既发布缺省路由，而且发送普通路由。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip default-route originate cost 2

【相关命令】

·**default-route**

**RIP \-- RIP配置命令 \-- rip enable**

------------------------------------------------------------------------

**[rip** **enable**]命令用来在接口上使能RIP。

**[undo rip enable**]命令用来在接口上关闭RIP。

【命令】

**[rip** *process-id* **enable** [ **exclude-subip** ]]

**[undo rip enable**]

【缺省情况】

接口上没有使能RIP。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

**[exclude-subip**]：不包括接口的从IP地址。如果未指定本参数，将包括接口的从IP地址。

【使用指导】

本命令的优先级高于**network**命令。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使能RIP进程100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip 100 enable

·交换应用

\# 在接口Vlan-interface10上使能RIP进程100。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip 100 enable

【相关命令】

·**network**

**RIP \-- RIP配置命令 \-- rip input**

------------------------------------------------------------------------

**[rip input**]命令用来允许接口接收RIP报文。

**[undo rip input**]命令用来禁止接口接收RIP报文。

【命令】

**[rip input**]

**[undo **]**rip input**

【缺省情况】

允许接口接收RIP报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 禁止接口GigabitEthernet1/0/1接收RIP报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo rip input

·交换应用

\# 禁止接口Vlan-interface10接收RIP报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 undo rip input

**RIP \-- RIP配置命令 \-- rip max-packet-length**

------------------------------------------------------------------------

**[rip max-packet-length**]命令用来配置RIP报文的最大长度。

**[undo rip max-packet-length**]命令用来恢复缺省情况。

【命令】

**[rip max-packet-length ***value*]

**[undo rip max-packet-length**]

【缺省情况】

RIP报文的最大长度为512字节。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：指定RIP报文的最大长度，取值范围为32～65535，单位为字节。

【使用指导】

如果配置值大于接口MTU，则报文的最大长度为接口MTU。

由于不同厂商对RIP报文最大长度的支持情况不同，要谨慎使用本特性，以免出现不兼容的情况。

在配置认证的情况下，如果配置不当可能会造成报文无法发送，建议用户按照下面进行配置：

·简单验证方式时，RIP报文的最大长度不小于52字节；

·MD5验证方式（使用RFC 2453规定的报文格式）时，RIP报文的最大长度不小于56字节；

·MD5验证方式（使用RFC 2082规定的报文格式）时，RIP报文的最大长度不小于72字节。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1配置RIP报文的最大长度为1024字节。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip max-packet-length 1024

·交换应用

\# 在接口Vlan-interface10配置RIP报文的最大长度为1024字节。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip max-packet-length 1024

**RIP \-- RIP配置命令 \-- rip metricin**

------------------------------------------------------------------------

**[rip metricin**]命令用来配置接口接收RIP路由时的附加度量值。

**[undo rip metricin**]命令用来恢复缺省情况。

【命令】

**[rip metricin **] **route-policy** *route-policy-name*  *value*

**[undo **]**rip metricin**

【缺省情况】

接口接收RIP路由时的附加度量值为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-policy **]*route-policy-name*：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。对满足特定条件的路由设置附加度量值。

*[value*]：接收附加度量值，取值范围为0～16。

【使用指导】

当接口收到一条合法的RIP路由，在将其加入路由表前，附加度量值会被加到该路由上。因此，增加接口的接收附加度量值，该接口收到的RIP路由的度量值也会相应增加，当附加度量值与原路由度量值之和大于16，该条路由的度量值取16。

通过指定**route-policy**参数，可应用路由策略对接口接收的特定路由设置附加度量值：

·如果通过**apply cost**命令设置了匹配路由的附加度量值，则匹配路由的附加度量值取**apply cost**命令*value*参数设置的值，不匹配路由的附加度量值取本命令*value*参数所设的值。需要注意的是，本命令不支持通过**apply cost**命令中的**+**、**-**关键字对接口接收RIP路由的附加度量值进行增加、减少的设置。

·如果没有通过**apply cost**命令设置路由的附加度量值，则所有接收路由的附加度量值都取本命令*value*参数所设的值。

【举例】

·路由应用

\# 对接口GigabitEthernet1/0/1接收的RIP路由附加度量值进行设置。其中，1.0.0.0/8网段路由的附加度量值设置为6，其它网段路由的附加度量值设置为2。

\<Sysname\> system-view

Sysname ip prefix-list 123 permit 1.0.0.0 8

Sysname route-policy abc permit node 0

Sysname-route-policy-abc-10 if-match ip address prefix-list 123

Sysname-route-policy-abc-10 apply cost 6

Sysname-route-policy-abc-10 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip metricin route-policy abc 2

·交换应用

\# 对接口Vlan-interface10接收的RIP路由附加度量值进行设置。其中，1.0.0.0/8网段路由的附加度量值设置为6，其它网段路由的附加度量值设置为2。

\<Sysname\> system-view

Sysname ip prefix-list 123 permit 1.0.0.0 8

Sysname route-policy abc permit node 0

Sysname-route-policy-abc-10 if-match ip address prefix-list 123

Sysname-route-policy-abc-10 apply cost 6

Sysname-route-policy-abc-10 quit

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip metricin route-policy abc 2

【相关命令】

·**apply cost**（三层技术-IP路由命令参考/路由策略）

**RIP \-- RIP配置命令 \-- rip metricout**

------------------------------------------------------------------------

**[rip metricout**]命令用来配置接口发送RIP路由时的附加度量值。

**[undo rip metricout**]命令用来恢复缺省情况。

【命令】

**[rip metricout **] **route-policy** *route-policy-name*  *value*

**[undo **]**rip metricout**

【缺省情况】

接口发送RIP路由时的附加度量值为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-policy **]*route-policy-name*：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。对满足特定条件的路由设置附加度量值。

*[value*]：发送附加度量值，取值范围为1～16。

【使用指导】

当发布一条RIP路由时，附加度量值会在发布该路由之前附加在这条路由上。因此，增加一个接口的发送附加度量值，该接口发送的RIP路由的度量值也会相应增加。

通过指定**route-policy**参数，可应用路由策略对接口发布的特定路由设置附加度量值：

·如果通过**apply cost**命令设置了匹配路由的附加度量值，则匹配路由的附加度量值取**apply cost**命令*value*参数设置的值，不匹配路由的附加度量值取本命令*value*参数所设的值。需要注意的是，本命令不支持通过**apply cost**命令中的**+**、**-**关键字对接口发布RIP路由的附加度量值进行增加、减少的设置。

·如果没有通过**apply cost**命令设置路由的附加度量值，则所有发布路由的附加度量值都取本命令*value*参数所设的值。

【举例】

·路由应用

\# 对接口GigabitEthernet1/0/1发送的RIP路由附加度量值进行设置。其中，1.0.0.0/8网段路由的附加度量值设置为6，其它网段路由的附加度量值设置为2。

\<Sysname\> system-view

Sysname ip prefix-list 123 permit 1.0.0.0 8

Sysname route-policy abc permit node 0

Sysname-route-policy-abc-10 if-match ip address prefix-list 123

Sysname-route-policy-abc-10 apply cost 6

Sysname-route-policy-abc-10 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip metricout route-policy abc 2

·交换应用

\# 对接口Vlan-interface10发送的RIP路由附加度量值进行设置。其中，1.0.0.0/8网段路由的附加度量值设置为6，其它网段路由的附加度量值设置为2。

\<Sysname\> system-view

Sysname ip prefix-list 123 permit 1.0.0.0 8

Sysname route-policy abc permit node 0

Sysname-route-policy-abc-10 if-match ip address prefix-list 123

Sysname-route-policy-abc-10 apply cost 6

Sysname-route-policy-abc-10 quit

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip metricout route-policy abc 2

【相关命令】

·**apply cost**（三层技术-IP路由命令参考/路由策略）

**RIP \-- RIP配置命令 \-- rip mib-binding**

------------------------------------------------------------------------

**[rip mib-binding**]命令用来配置RIP进程绑定MIB。

**[undo rip mib-binding**]命令用来恢复缺省情况。

【命令】

**[rip mib-binding** *process-id*]

**[undo rip mib-binding**]

【缺省情况】

MIB绑定在进程号最小的RIP进程上。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIP进程号，取值范围为1～65535。

【使用指导】

·如果指定的*process-id*不存在，配置RIP进程绑定命令时将会提示RIP进程不存在，无法完成配置。

·如果配置了RIP进程绑定MIB，若删除*process-id*对应的RIP进程，则同时删除RIP进程绑定MIB配置，MIB绑定到进程号最小的RIP进程上。

【举例】

\# 配置RIP进程100绑定MIB。

\<Sysname\> system-view

Sysname rip mib-binding 100

**RIP \-- RIP配置命令 \-- rip output**

------------------------------------------------------------------------

**[rip output**]命令用来允许接口发送RIP报文。

**[undo rip output**]命令用来禁止接口发送RIP报文。

【命令】

**[rip output**]

**[undo rip output**]

【缺省情况】

允许接口发送RIP报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 禁止接口GigabitEthernet1/0/1发送RIP报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo rip output

·交换应用

\# 禁止接口Vlan-interface10发送RIP报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 undo rip output

**RIP \-- RIP配置命令 \-- rip output-delay**

------------------------------------------------------------------------

**[rip output-delay**]命令用来配置接口下RIP报文的发送速率。

**[undo rip output-delay**]命令用来恢复缺省情况。

【命令】

**[rip output-delay*** time*** count*** count*]

**[undo rip output-delay**]

【缺省情况】

RIP报文的发包速率由进程全局的配置决定。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：接口发送RIP报文的时间间隔，取值范围为10～100，单位为毫秒。

*[count*]：接口一次发送RIP报文的最大个数，取值范围为1～30。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1配置发送RIP报文的时间间隔为30毫秒，一次最多发送6个RIP报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip output-delay 30 count 6

·交换应用

\# 在接口Vlan-interface10配置发送RIP报文的时间间隔为30毫秒，一次最多发送6个RIP报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip output-delay 30 count 6

【相关命令】

·**output-delay**

**RIP \-- RIP配置命令 \-- rip poison-reverse**

------------------------------------------------------------------------

**[rip poison-reverse**]命令用来使能毒性逆转功能。

**[undo rip poison-reverse**]命令用来关闭毒性逆转功能。

【命令】

**[rip poison-reverse**]

**[undo rip poison-reverse**]

【缺省情况】

毒性逆转功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置对RIP更新报文进行毒性逆转。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip poison-reverse

·交换应用

\# 在接口Vlan-interface10上配置对RIP更新报文进行毒性逆转。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip poison-reverse

**RIP \-- RIP配置命令 \-- rip primary-path-detect bfd echo**

------------------------------------------------------------------------

![说明](RIP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[rip primary-path-detect bfd echo**]命令用来使能RIP协议中主用链路使能BFD（Echo方式）检测功能。

**[undo rip primary-path-detect bfd**]命令用来恢复缺省情况。

【命令】

**[rip primary-path-detect bfd echo**]

**[undo rip primary-path-detect bfd**]

【缺省情况】

RIP协议中主用链路的BFD Echo检测功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置本功能后，RIP协议的快速重路由特性中的主用链路将使用BFD（Echo方式）进行检测。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置RIP协议快速重路由特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 fast-reroute route-policy frr

Sysname-rip-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip primary-path-detect bfd echo

·交换应用

\# 在接口Vlan-interface10上配置RIP协议快速重路由特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 fast-reroute route-policy frr

Sysname-rip-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip primary-path-detect bfd echo

**RIP \-- RIP配置命令 \-- rip split-horizon**

------------------------------------------------------------------------

**[rip split-horizon**]命令用来使能水平分割功能。

**[undo rip split-horizon**]命令用来关闭水平分割功能。

【命令】

**[rip split-horizon**]

**[undo rip split-horizon**]

【缺省情况】

水平分割功能处于使能状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·通常情况下，为了防止路由环路的出现，水平分割是必要的，因此，建议不要关闭水平分割。当因为特殊需要，如为保证协议的正确执行，需要关闭水平分割时，请一定要确认是否必要。

·在帧中继和X.25等NBMA（Non-Broadcast Multi-Access，非广播多路访问）网络中，当主接口和点到多点子接口配置了多条虚电路时，为了保证路由信息的正确传播，需要关闭水平分割功能。关于帧中继和X.25的详细信息，请参见"二层技术-广域网接入配置指导"中的"帧中继"和"LAPB和X.25"。

·如果同时使能了水平分割和毒性逆转，则只有毒性逆转功能生效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置水平分割。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip split-horizon

·交换应用

\# 在接口Vlan-interface10上配置水平分割。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip split-horizon

**RIP \-- RIP配置命令 \-- rip summary-address**

------------------------------------------------------------------------

**[rip summary-address**]命令用来配置发布一条聚合路由。

**[undo rip summary-address**]命令用来取消该配置。

【命令】

**[rip summary-address**[ *ip-address* { *mask-length* \| *mask* }]]

**[undo rip summary-address**[ *ip-address* { *mask-length* \| *mask* }]]

【缺省情况】

没有配置发布一条聚合路由。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：聚合路由的目的IP地址。

*[mask-length*]：聚合路由的网络掩码长度，取值范围为0～32。

*[mask*]：聚合路由的网络掩码，点分十进制格式。

【使用指导】

该功能仅在自动路由聚合功能被关闭时才能生效。

【举例】

·路由应用

\# 配置RIP在接口GigabitEthernet1/0/1发布一个聚合本地IP地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip summary-address 10.0.0.0 255.255.255.0

·交换应用

\# 配置RIP在接口Vlan-interface10发布一个聚合本地IP地址。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip summary-address 10.0.0.0 255.255.255.0

【相关命令】

·**summary**

**RIP \-- RIP配置命令 \-- rip triggered**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[rip triggered**]命令用来使能TRIP功能。

**[undo rip triggered**]命令用来关闭TRIP功能。

【命令】

**[rip triggered**]

**[undo rip triggered**]

【缺省情况】

TRIP功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

TRIP功能只能运行在PPP、帧中继、X.25链路层协议上。

【举例】

\# 使能TRIP功能。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 rip triggered

**RIP \-- RIP配置命令 \-- rip version**

------------------------------------------------------------------------

**[rip version**]命令用来配置接口运行的RIP版本。

**[undo rip version**]命令用来恢复缺省情况。

【命令】

**[rip version **[{ **1** \| **2** [ **broadcast** \| **multicast** ] }]]

**[undo rip version**]

【缺省情况】

没有配置接口运行的RIP版本。接口只能发送RIP-1广播报文，可以接收RIP-1广播/单播报文、RIP-2广播/组播/单播报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1**]：接口运行RIP协议的版本为RIP-1。

**[2**]：接口运行RIP协议的版本为RIP-2。

[[[ **broadcast** \| **multicast** ]]]：RIP-2报文的发送方式为广播方式（**broadcast**）还是组播方式（**multicast**），缺省为组播方式（**multicast**）。

【使用指导】

如果接口上配置了RIP版本，以接口配置的为准；如果接口上没有配置RIP版本，接口运行的RIP版本以全局配置的为准。

当接口运行的RIP版本为RIP-1时：

·发送RIP-1广播报文

·接收RIP-1广播/单播报文

当接口运行在RIP-2广播方式时：

·发送RIP-2广播报文

·接收RIP-1广播/单播报文、RIP-2广播/组播/单播报文

当接口运行在RIP-2组播方式时：

·发送RIP-2组播报文

·接收RIP-2广播/组播/单播报文

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1以广播方式发送RIP-2报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rip version 2 broadcast

·交换应用

\# 配置接口Vlan-interface10以广播方式发送RIP-2报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rip version 2 broadcast

【相关命令】

·**version**

**RIP \-- RIP配置命令 \-- silent-interface**

------------------------------------------------------------------------

**[silent-interface**]命令用来配置接口工作在抑制状态，即接口只接收RIP报文而不发送RIP报文。

**[undo silent-interface**]命令用来恢复缺省情况。

【命令】

**[silent-interface**  { *interface-type interface-number* \| **all** }]

**[undo silent-interface**  { *interface-type interface-number* \| **all** }]

【缺省情况】

允许所有接口发送RIP报文。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：接口类型和编号。

**[all**]：抑制所有接口。

【举例】

·路由应用

\# 将所有接口设置为抑制状态，随后激活指定接口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname rip 100

Sysname-rip-100 silent-interface all

Sysname-rip-100 undo silent-interface gigabitethernet 1/0/1

Sysname-rip-100 network 131.108.0.0

·交换应用

\# 将所有接口设置为抑制状态，随后激活指定接口Vlan-interface10。

\<Sysname\> system-view

Sysname rip 100

Sysname-rip-100 silent-interface all

Sysname-rip-100 undo silent-interface vlan-interface 10

Sysname-rip-100 network 131.108.0.0

**RIP \-- RIP配置命令 \-- summary**

------------------------------------------------------------------------

**[summary**]命令用来使能RIP-2自动路由聚合功能，聚合后的路由以使用自然掩码的路由形式发布，减小了路由表的规模。

**[undo summary**]命令用来关闭自动路由聚合功能，以便将所有子网路由广播出去。

【命令】

**[summary**]

**[undo summary**]

【缺省情况】

RIP-2自动路由聚合功能处于使能状态。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能RIP-2自动路由聚合功能可以减小路由表规模，提高大型网络的可扩展性和效率。

【举例】

\# 关闭RIP-2自动路由聚合功能。

\<Sysname\> system-view

Sysname rip

Sysname-rip-1 undo summary

【相关命令】

·**rip summary-address**

·**rip version**

**RIP \-- RIP配置命令 \-- timer triggered**

------------------------------------------------------------------------

**[timer triggered**]命令用来配置触发更新的时间间隔。

**[undo timer triggered**]命令用来恢复缺省情况。

【命令】

**[timer triggered ***maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo timer triggered**]

【缺省情况】

发送触发更新的最大时间间隔为5秒，最小间隔为50毫秒，增量惩罚间隔为200毫秒。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：触发更新的最大间隔时间。取值范围是1{.varname}～5{.varname}，单位是秒。{.varname}

*[minimum-interval*]：触发更新的最小间隔时间。取值范围是10{.varname}～5000{.varname}，单位是毫秒。{.varname}

*incremental-interval*{.varname}：触发更新间隔的增加时间。取值范围是100{.varname}～1000{.varname}，单位是毫秒。{.varname}

【使用指导】

本命令在网络变化不频繁的情况下将触发更新的时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将时间间隔按照配置的惩罚增量延长，最大不超过*maximum-interval*。

*[minimum-interval*]和*incremental-interval*配置值不允许大于*maximum-interval*配置值。

【举例】

\# 配置发送触发更新的最大时间间隔为2秒，最小时间间隔为100毫秒，惩罚增量为100毫秒。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 timer triggered 2 100 100

**RIP \-- RIP配置命令 \-- timers**

------------------------------------------------------------------------

**[timers**]命令用来配置RIP各个定时器的值，可通过调节RIP定时器来调整路由协议的性能，以满足网络需要。

**[undo timers**]命令用来恢复缺省情况。

【命令】

**[timers **[{ **garbage-collect** *garbage-collect-value* \| **suppress** *suppress-value* \| **timeout** *timeout-value* \| **update** *update-value* } \*]]

**[undo timers **[{ **garbage-collect** \| **suppress** \| **timeout** \| **update** } \*]]

【缺省情况】

Garbage-collect定时器的值为120秒，Suppress定时器的值为120秒，Timeout定时器的值为180秒，Update定时器的值为30秒。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[garbage-collect-value*]：Garbage-collect定时器的值，取值范围为1～3600，单位为秒。

*[suppress-value*]：Suppress定时器的值，取值范围为0～3600，单位为秒。

*[timeout-value*]：Timeout定时器的值，取值范围为1～3600，单位为秒。

*[update-value*]：Update定时器的值，取值范围为1～3600，单位为秒。

【使用指导】

RIP受四个定时器的控制，分别是Update、Timeout、Suppress和Garbage-Collect，其中：

·Update定时器，定义了发送更新报文的时间间隔。

·Timeout定时器，定义了路由老化时间。如果在老化时间内没有收到关于某条路由的更新报文，则该条路由在路由表中的度量值将会被设置为16。

·Suppress定时器，定义了RIP路由处于抑制状态的时间段长度。当一条路由的度量值变为16时，该路由将进入被抑制状态。在被抑制状态，只有来自同一邻居，且度量值小于16的路由更新才会被路由器接收，取代不可达路由。

·Garbage-Collect定时器，定义了一条路由从度量值变为16开始，直到它从路由表里被删除所经过的时间。在Garbage-Collect时间内，RIP以16作为度量值向外发送这条路由的更新，如果Garbage-Collect超时，该路由仍没有得到更新，则该路由将从路由表中被彻底删除。

需要注意的是：

·通常情况下，无需改变各定时器的缺省值，该命令须谨慎使用。

·各个定时器的值在网络中所有的路由器上必须保持一致。

·Timeout定时器的值要大于Update定时器的值。

【举例】

\# 分别设置RIP各定时器的值：其中，Update定时器的值为5秒、Timeout定时器的值为15秒、Suppress定时器的值为15秒、Garbage-Collect定时器的值为30秒。

\<Sysname\> system-view

Sysname rip 100

Sysname-rip-100 timers update 5 timeout 15 suppress 15 garbage-collect 30

**RIP \-- RIP配置命令 \-- trip retransmit count**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[trip retransmit count**]命令用来配置TRIP中Update Response报文的最大重传次数。

**[undo trip retransmit count**]命令用来恢复缺省情况。

【命令】

**[trip retransmit count ***retransmit-count-value*]

**[undo trip retransmit count**]

【缺省情况】

TRIP中Update Response报文的最大重传次数为36。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retransmit-count-value*]：TRIP中Update Response报文的最大重传次数，取值范围为1～3600。

【举例】

\# 配置TRIP中Update Response报文的最大重传次数为20。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 trip retransmit count 20

**RIP \-- RIP配置命令 \-- trip retransmit timer**

------------------------------------------------------------------------

![说明](RIP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[trip retransmit timer**]命令用来配置TRIP重传Update Request、Update Response报文的时间间隔。

**[undo trip retransmit timer**]命令用来恢复缺省情况。

【命令】

**[trip retransmit timer ***retransmit-time-value*]

**[undo trip retransmit timer**]

【缺省情况】

TRIP重传Update Request报文、Update Response报文的时间间隔为5秒。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retransmit-time-value*]：TRIP重传Update Request、Update Response报文的时间间隔，取值范围为1～3600，单位为秒。

【举例】

\# 配置TRIP重传Update Request、Update Response报文的时间间隔为80秒。

\<Sysname\> system-view

Sysname rip 1

Sysname-rip-1 trip retransmit timer 80

**RIP \-- RIP配置命令 \-- validate-source-address**

------------------------------------------------------------------------

**[validate-source-address**]命令用来使能对接收到的RIP路由更新报文进行源IP地址检查的功能。

**[undo validate-source-address**]命令用来关闭该项功能。

【命令】

**[validate-source-address**]

**[undo validate-source-address**]

【缺省情况】

对接收到的RIP路由更新报文进行源IP地址检查的功能处于使能状态。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭对接收到的RIP路由更新报文进行源IP地址检查的功能。

\<Sysname\> system-view

Sysname-rip rip 100

Sysname-rip-100 undo validate-source-address

**RIP \-- RIP配置命令 \-- version**

------------------------------------------------------------------------

**[version**]命令用来配置全局RIP版本。

**[undo version**]命令用来恢复缺省情况。

【命令】

**[version**[ { **1** \| **2** }]]

**[undo version**]

【缺省情况】

没有配置全局RIP版本。接口只能发送RIP-1广播报文，可以接收RIP-1广播/单播报文、RIP-2广播/组播/单播报文。

【视图】

RIP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1**]：指定为RIP-1版本。

**[2**]：指定为RIP-2版本，RIP-2报文的发送方式为组播方式。

【使用指导】

·如果接口上配置了RIP版本，以接口配置的为准。

·如果接口没有配置RIP版本，将全局RIP版本配置为1时，接口运行的RIP版本为RIP-1，发送RIP-1广播报文，可以接收RIP-1广播/单播报文。

·如果接口没有配置RIP版本，将全局RIP版本配置为2时，接口运行的RIP版本为RIP-2且工作在组播方式，发送RIP-2组播报文，可以接收RIP-2广播/组播/单播。

【举例】

\# 指定全局RIP版本为RIP-2。

\<Sysname\> system-view

Sysname rip 100

Sysname-rip-100 version 2

【相关命令】

·**rip version**

