<!-- CMD-INDEX
  display mld group                   | 任意视图             | L41
  display mld interface               | 任意视图             | L307
  display mld proxy group             | 任意视图             | L551
  display mld proxy routing-table     | 任意视图             | L679
  display mld ssm-mapping             | 任意视图             | L885
  display mld user-authorization      | 任意视图             | L947
  last-listener-query-count (MLD view) | MLD视图            | L1097
  last-listener-query-interval (MLD view) | MLD视图            | L1147
  max-response-time (MLD view)        | MLD视图            | L1197
  mld                                 | 系统视图             | L1247
  mld access-policy                   | User-Profile视图   | L1293
  mld authorization-enable            | 三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/VT接口视图 | L1353
  mld enable                          | 接口视图             | L1395
  mld fast-leave                      | 接口视图             | L1463
  mld group-policy                    | 接口视图             | L1521
  mld join-by-session                 | 三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图 | L1597
  mld last-listener-query-count       | 接口视图             | L1645
  mld last-listener-query-interval    | 接口视图             | L1707
  mld max-response-time               | 接口视图             | L1769
  mld other-querier-present-timeout   | 接口视图             | L1831
  mld proxy enable                    | 接口视图             | L1893
  mld proxy forwarding                | 接口视图             | L1959
  mld query-interval                  | 接口视图             | L2013
  mld robust-count                    | 接口视图             | L2075
  mld startup-query-count             | 接口视图             | L2139
  mld startup-query-interval          | 接口视图             | L2201
  mld static-group                    | 接口视图             | L2263
  mld user-vlan-aggregation dot1q     | 三层以太网子接口视图/三层聚合子接口视图 | L2361
  mld version                         | 接口视图             | L2413
  other-querier-present-timeout (MLD view) | MLD视图            | L2467
  proxy multipath (MLD view)          | MLD视图            | L2517
  query-interval (MLD view)           | MLD视图            | L2563
  reset mld group                     | 用户视图             | L2613
  robust-count (MLD view)             | MLD视图            | L2685
  ssm-mapping (MLD view)              | MLD视图            | L2737
  startup-query-count (MLD view)      | MLD视图            | L2797
  startup-query-interval (MLD view)   | MLD视图            | L2847
-->

**MLD \-- MLD配置命令 \-- display mld group**

------------------------------------------------------------------------

**[display** **mld** **group**]命令用来显示MLD组播组（即通过MLD加入的IPv6组播组）的信息。

【命令】

**[display** **mld** [ **vpn-instance** *vpn-instance-name*  **group** [ *ipv6-group-address* \| **interface** *interface-type interface-number*   **static** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

**[interface** *interface-type interface-number*]：显示指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。

**[static**]：显示静态加入的IPv6组播组信息。如果未指定本参数，将只显示动态加入的IPv6组播组信息。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例中动态加入的所有MLD组播组信息。

\<Sysname\> display mld group

MLD groups in total: 1

 GigabitEthernet1/0/1(FE80::101):

  MLD groups reported in total: 1

   Group address: FF03::101

    Last reporter: FE80::10

    Uptime: 00:02:04

    Expires: 00:01:15

表1-1 display mld group命令显示信息描述表

字段

描述

MLD groups in total

MLD组播组的总数

MLD groups reported in total

当前接口上动态加入的MLD组播组总数

Group address

IPv6组播组地址

Last reporter

最后发送报告报文的主机地址

Uptime

IPv6组播组的运行时间

Expires

IPv6组播组的超时时间，Off表示该定时器关闭

 # 显示公网实例中动态加入的MLD组播组FF3E::101的详细信息（假设当前运行MLD SSM Mapping）。

\<Sysname\> display mld group ff3e::101 verbose

 GigabitEthernet1/0/1(FE80::101):

  MLD groups reported in total: 1

   Group: FF3E::101

     Uptime: 00:01:46

     Exclude expires: 00:04:16

     Mapping expires: 00:02:16

     Last reporter: FE80::10

     Last-listener-query-counter: 0

     Last-listener-query-timer-expiry: Off

     Mapping last-listener-query-counter: 0

     Mapping last-listener-query-timer-expiry: Off

     Group mode: Exclude

     Version1-host-present-timer-expiry: Off

     Source list (sources in total: 1):

       Source: 10::10

          Uptime: 00:00:09

          V2 expires: 00:04:11

          Mapping expires: 00:02:16

          Last-listener-query-counter: 0

          Last-listener-query-timer-expiry: Off

表1-2 display mld group verbose命令显示信息描述表

字段

描述

MLD groups reported in total

当前接口上动态加入的MLD组播组总数

Group

IPv6组播组地址

Uptime

IPv6组播组的运行时间

Exclude expires

EXCLUDE模式下IPv6组播组的超时时间，Off表示该定时器关闭

Mapping expires

MLD SSM Mapping规则所生成IPv6组播组的超时时间。只有运行MLD SSM Mapping时才会显示本字段

Last reporter

最后发送报告报文的主机地址

Last-listener-query-counter

最后组成员查询次数

Last-listener-query-timer-expiry

最后组成员查询定时器的超时时间，Off表示该定时器关闭

Mapping last-listener-query-counter

MLD SSM Mapping规则所生成IPv6组播组的最后组成员查询次数。只有运行MLD SSM Mapping时才会显示本字段

Mapping last-listener-query-timer-expiry

MLD SSM Mapping规则所生成IPv6组播组的最后组成员查询定时器的超时时间，Off表示该定时器关闭。只有运行MLD SSM Mapping时才会显示本字段

Group mode

对IPv6组播源的过滤模式：

·Include：表示INCLUDE模式

·Exclude：表示EXCLUDE模式，对于未运行MLD SSM Mapping的MLDv1，也显示为本模式

MLDv1本身并不区分过滤模式，但当运行MLD SSM Mapping时，会根据具体配置以及加入的IPv6组播组来显示相应的模式；而当未运行MLD SSM Mapping时，则固定显示为Exclude

Version1-host-present-timer-expiry

MLDv1主机超时时间，Off表示该定时器关闭。只有运行MLDv2时才会显示本字段

Source list (sources in total: 1)

IPv6组播源列表及总数。只有运行MLDv2或MLD SSM Mapping时才会显示本字段

Source

IPv6组播源地址。只有运行MLDv2或MLD SSM Mapping时才会显示本字段

Uptime

IPv6组播源的运行时间。只有运行MLDv2或MLD SSM Mapping时才会显示本字段

V2 expires

MLDv2组播源的超时时间，Off表示该定时器关闭，"\-\--"表示该组播源由MLD SSM Mapping规则生成。只有运行MLDv2或MLD SSM Mapping时才会显示本字段

Mapping expires

MLD SSM Mapping规则所生成IPv6组播源的超时时间。只有运行MLD SSM Mapping时才会显示本字段

Last-listener-query-counter

最后源组成员查询次数。只有运行MLDv2或MLD SSM Mapping时才会显示本字段

Last-listener-query-timer-expiry

最后源组成员查询定时器的超时时间，Off表示该定时器关闭。只有运行MLDv2或MLD SSM Mapping时才会显示本字段

\# 显示公网实例中静态加入的MLD组播组信息。

\<Sysname\> display mld group static

 Entries in total: 2

  (\*, FF03::101)

   Interface: GE1/0/1

   Expires: Never

  (2001::101, FF3E::202)

   Interface: GE1/0/1

   Expires: Never

表1-3 display mld group static命令显示信息描述表

字段

描述

Entries in total

MLD组播组的总数

(\*, FF03::101)

（\*，G）表项

(2001::101, FF3E::202)

（S，G）表项

Interface

接口名称

Expires

IPv6组播组的超时时间，固定显示为Never，表示永不超时

【相关命令】

·**reset****mld** **group**

**MLD \-- MLD配置命令 \-- display mld interface**

------------------------------------------------------------------------

**[display** **mld** **interface**]命令用来显示接口上MLD配置和运行的信息。

【命令】

**[display** **mld** [ **vpn-instance** *vpn-instance-name*  **interface**  *interface-type interface-number*   **proxy**   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[interface-type interface-number*]：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。

**[proxy**]：显示代理接口的信息。如果未指定本参数，将显示所有接口的信息。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例接口GigabitEthernet1/0/1（非代理接口）上MLD配置和运行的详细信息。

\<Sysname\> display mld interface gigabitethernet 1/0/1 verbose

 GigabitEthernet1/0/1(FE80::200:AFF:FE01:101):

   MLD is enabled.

   MLD version: 1

   Query interval for MLD: 125s

   Other querier present time for MLD: 255s

   Maximum query response time for MLD: 10s

   Last listener query interval: 1s

   Last listener query count: 2

   Startup query interval: 31s

   Startup query count: 2

   General query timer expiry (hh:mm:ss): 00:00:23

   Querier for MLD: FE80::200:AFF:FE01:101 (This router)

   MLD activity: 1 join(s), 0 done(s)

   IPv6 multicast routing on this interface: Enabled

   Robustness: 2

   Require-router-alert: Disabled

   Fast-leave: Disabled

   Startup-query: Off

   Other-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--

   Authorization: Disabled

   Join-by-session: Disabled

   User-VLAN-aggregation: Disabled

  MLD groups reported in total: 1

\# 显示公网实例所有代理接口上MLD配置和运行的详细信息。

\<Sysname\> display mld interface proxy verbose

 GigabitEthernet1/0/2(FE80::100:CEF:FE01:101):

   MLD proxy is enabled.

   MLD version: 1

   IPv6 multicast routing on this interface: Enabled

   Require-router-alert: Disabled

表1-4 display mld interface命令显示信息描述表

字段

描述

GigabitEthernet1/0/1(FE80::200:AFF:FE01:101)

接口的名称和IPv6链路本地地址

MLD is enabled

MLD已使能

MLD version

此接口运行的MLD版本

Query interval for MLD

MLD普遍组查询报文的发送间隔（秒）

Other querier present time for MLD

MLD其它查询器的存在时间（秒）

Maximum query response time for MLD

MLD普遍组查询报文的最大响应时间（秒）

Last listener query interval

最后组成员查询间隔（秒）

Last listener query count

最后组成员查询次数

Startup query interval

MLD查询器启动查询间隔（秒）

Startup query count

MLD查询器启动查询次数

General query timer expiry

MLD普遍组查询的超时时间，off表示该定时器关闭

Querier for MLD

MLD查询器的IPv6链路本地地址

MLD activity: 1 join(s), 0 done(s)

MLD的活动统计：

·join(s)：表示加入过的IPv6组播组总数

·done(s)：表示离开过的IPv6组播组总数

IPv6 multicast routing on this interface

是否使能IPv6组播路由功能：

·Enabled：表示已使能

·Disabled：表示未使能

Robustness

MLD查询器的健壮系数

Require-router-alert

是否使能丢弃未携带Router-Alert选项的MLD报文功能：

·Enabled：表示已使能

·Disabled：表示未使能

Fast-leave

是否使能快速离开功能：

·Enabled：表示已使能

·Disabled：表示未使能

Startup-query

是否处于启动查询状态：

·On：表示处于启动查询状态

·Off：表示未处于启动查询状态

Other-querier-present-timer-expiry

MLD其它查询器的存在超时时间，Off表示该定时器关闭

Authorization

是否使能IPv6可控组播功能：

·Enabled：表示已使能

·Disabled：表示未使能

本字段的支持情况与设备的型号有关，请以设备的实际情况为准

Join-by-session

是否使能按会话记录用户加入的IPv6组播组：

·Enabled：表示已使能

·Disabled：表示未使能

本字段的支持情况与设备的型号有关，请以设备的实际情况为准

User-VLAN-aggregation

是否使能为IPv6组播报文封装VLAN Tag：

·Enabled：表示已使能

·Disabled：表示未使能

本字段的支持情况与设备的型号有关，请以设备的实际情况为准

MLD groups reported in total

此接口上动态加入的IPv6组播组数量。没有加入组时不显示本字段

MLD proxy is enabled

MLD代理功能已使能

Version1-querier-present-timer-expiry

MLDv1查询器的存在超时时间

**MLD \-- MLD配置命令 \-- display mld proxy group**

------------------------------------------------------------------------

**[display** **mld** **proxy** **group**]命令用来显示MLD代理记录的IPv6组播组信息。

【命令】

**[display** **mld** [ **vpn-instance** *vpn-instance-name*  **proxy** **group**  *ipv6-group-address*[ \| **interface** *interface-type* *interface-number* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

**[interface** *interface-type* *interface-number*]：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例中MLD代理记录的所有IPv6组播组信息。

\<Sysname\> display mld proxy group

MLD proxy group records in total: 2

 GigabitEthernet1/0/1(FE80::16:1):

  MLD proxy group records in total: 2

   Group address: FF1E::1

    Member state: Idle

    Expires: Off

   Group address: FF1E::2

    Member state: Idle

    Expires: Off

\# 显示公网实例中MLD代理记录的IPv6组播组FF1E::1的详细信息。

\<Sysname\> display mld proxy group ff1e::1 verbose

 GigabitEthernet1/0/1(FE80::16:1):

  MLD proxy group records in total: 2

   Group: FF1E::1

     Group mode: Include

     Member state: Idle

     Expires: Off

     Source list (sources in total: 1):

       100::1

表1-5 display mld proxy group命令显示信息描述表

字段

描述

MLD proxy group records in total

MLD代理记录的IPv6组播组总数

GigabitEthernet1/0/1(FE80::16:1)

MLD代理接口的名称和IPv6地址

Pending proxy group

等待生效的代理组

Group address/Group

IPv6组播组地址

Member state

IPv6组播组成员的状态，其中：

·Delay：表示加入了一个组，并对该组启动了延迟发送报告报文的定时器

·Idle：表示加入了一个组，但对该组尚未启动延迟发送报告报文的定时器

Expires

IPv6组播组延迟发送报告报文的时间，Off表示该定时器关闭

Group mode

对IPv6组播源的过滤模式，其中：

·Include：表示INCLUDE模式

·Exclude：表示EXCLUDE模式

Source list

MLD代理的IPv6组播组所包含的IPv6组播源列表

sources in total

IPv6组播源的总数

**MLD \-- MLD配置命令 \-- display mld proxy routing-table**

------------------------------------------------------------------------

**[display** **mld** **proxy** **routing-table**]命令用来显示MLD代理路由表的信息。

【命令】

**[display** **mld** [ **vpn-instance** *vpn-instance-name*  **proxy** **routing-table**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  ] \*  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-source-address*]：显示指定IPv6组播源的信息。如果未指定本参数，将显示所有IPv6组播源的信息。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的信息。

*[prefix-length*]：指定IPv6组播组或IPv6组播源地址的前缀长度。对于IPv6组播源地址，其取值范围为0～128，缺省值为128；对于IPv6组播组地址，其取值范围为8～128，缺省值为128。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例MLD代理路由表的信息。

\<Sysname\> display mld proxy routing-table

 Total 1 (\*, G) entries, 2 (S, G) entries.

 (100::1, FF1E::1)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: MLD

 (\*, FF1E::2)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: STATIC

 (2::2, FF1E::2)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (2 in total):

         1: LoopBack1

             Protocol: STATIC

         2: Vlan-interface2

             Protocol: PROXY

\# 显示公网实例MLD代理路由表的详细信息。

\<Sysname\> display mld proxy routing-table verbose

 Total 1 (\*, G) entries, 2 (S, G) entries.

 (100::1, FF1E::1)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: MLD

             Querier state: Querier

             Join/Prune state：Join

     Non-downstream interfaces: None

 (\*, FF1E::2)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: STATIC

             Querier state: Querier

             Join/Prune state：Join

     Non-downstream interfaces (1 in total):

         1: Vlan-interface3

             Protocol: MLD

             Querier state: Non-querier

             Join/Prune state：Join

 (2::2, FF1E::2)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (2 in total):

         1: LoopBack1

             Protocol: STATIC

             Querier state: Querier

             Join/Prune state: Join

         2: Vlan-interface2

             Protocol: PROXY

             Querier state: Querier

             Join/Prune state: Join

     Non-downstream interfaces: None

表1-6 display mld proxy routing-table命令显示信息描述表

字段

描述

Total 1 (\*, G) entries, 2 (S, G) entries

（S，G）表项和（\*，G）表项的总数

(100::1, FF1E::1)

（S，G）表项

Upstream interface

表项的入接口

Downstream interfaces (1 in total)

下游的出接口信息及总数

Non-downstream interfaces (1 in total)

下游的非出接口信息及总数

1: Vlan-interface2

索引号为1的接口Vlan-interface2

Protocol

接口使用的协议类型：

·MLD：表示动态MLD

·PROXY：表示MLD代理

·STATIC：表示静态MLD

Querier state

接口的查询器状态：

·Querier：表示接口为MLD查询器

·Non-querier：表示接口不是MLD查询器

Join/Prune state

接口的加入/剪枝状态：

·NI：表示默认状态

·Join：表示处于MLD加入的状态

·Prune：表示处于MLD剪枝的状态

**MLD \-- MLD配置命令 \-- display mld ssm-mapping**

------------------------------------------------------------------------

**[display** **mld** **ssm-mapping**]命令用来显示MLD SSM Mapping规则。

【命令】

**[display** **mld** [ **vpn-instance** *vpn-instance-name*  **ssm-mapping** *ipv6-group-address*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-group-address*]：显示指定IPv6组播组的信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。

【举例】

\# 显示公网实例中IPv6组播组FF3E::101对应的MLD SSM Mapping规则。

\<Sysname\> display mld ssm-mapping ff3e::101

 Group: FF3E::101

 Source list:

        1::1

        1::2

        10::1

        100::10

表1-7 display mld ssm-mapping命令显示信息描述表

字段

描述

Group

IPv6组播组地址

Source list

IPv6组播源地址列表

**MLD \-- MLD配置命令 \-- display mld user-authorization**

------------------------------------------------------------------------

![说明](MLD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display****mld****user-authorization**]命令用来显示MLD用户的授权信息。

【命令】

**[display****mld****user-authorization** [ **interface** *interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type* *interface-number*]：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。

【举例】

\# 显示所有MLD用户的授权信息。

\<Sysname\> display mld user-authorization

 Authorized users in total: 3

   User name: user1@isp1

   Access type: PPP

   Interface: Virtual-Access0

   Access interface: Virtual-Access0

   Maximum programs for order: 10

   User profile: profile1

   Authorized programs list:

     FF03::101

   User name: user2

   Access type: IPoE

   Interface: Multicast-UA0

   Access interface: GigabitEthernet1/0/1.1

   VLAN ID: 100

   Second VLAN ID: 10

   Maximum programs for order: 10

   User profile: profile1

   Authorized programs list:

     FF03::101

     FF03::102

     FF03::103

   User name: user3

   Access type: Portal

   Interface: Multicast-UA1

   Access interface: GigabitEthernet1/0/2

   Maximum programs for order: 10

   User profile: profile1

   Authorized programs list:

     FF03::101

     FF03::103

表1-8 display mld user-authorization命令显示信息描述表

字段

描述

Authorized users in total

接入用户总数

User name

用户名

Access type

用户接入的方式：

·IPoE：表示IPoE方式

·Portal：表示Portal方式

·PPP：表示PPP方式

Interface

用户接口

Access interface

用户接入的实际接口

VLAN ID

用户带VLAN Tag接入时所携带的第一层（或唯一一层）VLAN编号

Second VLAN ID

用户带VLAN Tag接入时所携带的第二层VLAN编号

Maximum programs for order

允许用户加入IPv6组播组的最大数量

User profile

用户授权的User Profile名称，用户可加入该User Profile下通过**mld** **access-policy**命令所配置接入策略中的IPv6组播组

Authorized programs list

用户授权加入的IPv6组播组列表

**MLD \-- MLD配置命令 \-- last-listener-query-count (MLD view)**

------------------------------------------------------------------------

**[last-listener-query-count**]命令用来全局配置MLD最后组成员查询次数。

**[undo last-listener-query-count**]命令用来恢复缺省情况。

【命令】

**[last-listener-query-count ***count*]

**[undo last-listener-query-count**]

【缺省情况】

MLD最后组成员查询次数等于MLD查询器的健壮系数。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定MLD最后组成员查询次数，取值范围为1～255。

【使用指导】

本命令与**mld last-listener-query-count**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD最后组成员查询次数为6次。

\<Sysname\> system-view

Sysname mld

Sysname-mld last-listener-query-count 6

【相关命令】

·**mld last-listener-query-count**

**MLD \-- MLD配置命令 \-- last-listener-query-interval (MLD view)**

------------------------------------------------------------------------

**[last-listener-query-interval**]命令用来全局配置MLD最后组成员查询间隔。

**[undo last-listener-query-interval**]命令用来恢复缺省情况。

【命令】

**[last-listener-query-interval***interval*]

**[undo last-listener-query-interval**]

【缺省情况】

MLD最后组成员查询间隔为1秒。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定MLD最后组成员查询间隔，取值范围为1～25，单位为秒。

【使用指导】

本命令与**mld last-listener-query-interval**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD最后组成员查询间隔为6秒。

\<Sysname\> system-view

Sysname mld

Sysname-mld last-listener-query-interval 6

【相关命令】

·**mld last-listener-query-interval**

**MLD \-- MLD配置命令 \-- max-response-time (MLD view)**

------------------------------------------------------------------------

**[max-response-time**]命令用来全局配置MLD普遍组查询报文的最大响应时间。

**[undo max-response-time**]命令用来恢复缺省情况。

【命令】

**[max-response-time*** time*]

**[undo max-response-time**]

【缺省情况】

MLD普遍组查询报文的最大响应时间为10秒。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定MLD普遍组查询报文的最大响应时间，取值范围为1～3174，单位为秒。

【使用指导】

本命令与**mld max-response-time**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD普遍组查询报文的最大响应时间为25秒。

\<Sysname\> system-view

Sysname mld

Sysname-mld max-response-time 25

【相关命令】

·**mld****max-response-time**

**MLD \-- MLD配置命令 \-- mld**

------------------------------------------------------------------------

**[mld**]命令用来进入MLD视图。

**[undo** **mld**]命令用来清除MLD视图下的所有配置。

【命令】

**[mld** [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **mld** [ **vpn-instance** *vpn-instance-name* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【举例】

\# 进入公网实例的MLD视图。

\<Sysname\> system-view

Sysname mld

Sysname-mld

\# 进入VPN实例mvpn的MLD视图。

\<Sysname\> system-view

Sysname mld vpn-instance mvpn

Sysname-mld-mvpn

**MLD \-- MLD配置命令 \-- mld access-policy**

------------------------------------------------------------------------

![说明](MLD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mld** **access-policy**]命令用来配置MLD用户的接入策略。

**[undo****mld** **access-policy**]命令用来删除MLD用户的接入策略。

【命令】

**[mld** **access-policy** *acl6-number*]

**[undo****mld** **access-policy** *acl6-number*]

【缺省情况】

没有配置MLD用户的接入策略，即MLD用户未被授权加入IPv6组播组。

【视图】

User-Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本或高级ACL的编号，取值范围为2000～3999。MLD用户只能加入该ACL规则所允许的IPv6组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有IPv6组播组。

【使用指导】

·对于IPv6基本ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv6高级ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播源地址（对于MLDv1报文和未携带IPv6组播源地址的IS_EX/TO_EX类型的MLDv2报文，视其IPv6组播源地址为0::0）范围，**destination**参数用来指定IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·通过多次执行本命令可以配置多条MLD用户接入策略，用户发送的MLD成员关系报告报文只需匹配其中一条就允许通过。

【举例】

\#在名为abc的User Profile下配置只允许MLD用户加入IPv6组播组FF03::101。

\<Sysname\> system-view

Sysname acl ipv6 basic 2000

Sysname-acl-ipv6-basic-2000 rule permit source ff03::101 0

Sysname-acl-ipv6-basic-2000 quit

Sysname user-profile abc

Sysname-user-profile-abc mld access-policy 2000

**MLD \-- MLD配置命令 \-- mld authorization-enable**

------------------------------------------------------------------------

![说明](MLD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mld** **authorization-enable**]命令用来使能IPv6可控组播功能。

**[undo** **mld** **authorization-enable**]命令用来关闭IPv6可控组播功能。

【命令】

**[mld** **authorization-enable**]

**[undo** **mld** **authorization-enable**]

【缺省情况】

IPv6可控组播功能处于关闭状态。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/VT接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在接口GigabitEthernet1/0/1上使能IPv6可控组播功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld authorization-enable

**MLD \-- MLD配置命令 \-- mld enable**

------------------------------------------------------------------------

**[mld** **enable**]命令用来在接口上使能MLD。

**[undo** **mld** **enable**]命令用来在接口上关闭MLD。

【命令】

**mld** **enable**

**[undo** **mld** **enable**]

【缺省情况】

接口上的MLD处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·只有在相应实例中先使能了IPv6组播路由，本命令才能生效。

·只有在接口上使能了MLD，在该接口上所做的MLD配置才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IPv6组播路由，并在接口GigabitEthernet1/0/1上使能MLD。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld enable

·交换应用：

\# 使能公网实例中的IPv6组播路由，并在接口Vlan-interface100上使能MLD。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld enable

【相关命令】

·**ipv6 multicast** **routing**（IP组播命令参考/IPv6组播路由与转发）

**MLD \-- MLD配置命令 \-- mld fast-leave**

------------------------------------------------------------------------

**[mld** **fast-leave**]命令用来在接口上使能IPv6组播组成员快速离开功能。

**[undo** **mld** **fast-leave**]命令用来在接口上关闭IPv6组播组成员快速离开功能。

【命令】

**[mld** **fast-leave** \**[group-policy*** acl6-number *]]

**[undo** **mld** **fast-leave**]

【缺省情况】

IPv6组播组成员快速离开功能处于关闭状态，即MLD查询器在收到主机发送的MLD离开组报文后将发送MLD特定组查询报文或MLD特定源组查询报文，而不会直接向上游发送离开通告。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本ACL的编号，取值范围为2000～2999。如果指定了本参数，快速离开功能将只为该ACL规则所允许的IPv6组播组服务；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则快速离开功能将为所有IPv6组播组服务。

【使用指导】

ACL规则中的**source**参数用来指定IPv6组播组的范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上使能IPv6组播组成员快速离开功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld fast-leave

·交换应用：

\# 在接口Vlan-interface100上使能IPv6组播组成员快速离开功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld fast-leave

**MLD \-- MLD配置命令 \-- mld group-policy**

------------------------------------------------------------------------

**[mld** **group-policy**]命令用来在接口上配置IPv6组播组过滤器，以限定该接口下的主机所能加入的IPv6组播组。

**[undo** **mld** **group-policy**]命令用来在接口上删除IPv6组播组过滤器。

【命令】

**[mld** **group-policy** *acl6-number* [ *version-number* ]]

**[undo** **mld** **group-policy**]

【缺省情况】

接口上没有配置IPv6组播组过滤器，即该接口下的主机可以加入任意IPv6组播组。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本或高级ACL的编号，取值范围为2000～3999。主机只能加入该ACL规则所允许的IPv6组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有IPv6组播组。

*[version-number*]：指定MLD的版本号，取值范围为1～2。缺省情况下，系统同时支持对MLDv1和MLDv2报告报文的过滤。

【使用指导】

·对于IPv6基本ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv6高级ACL，该ACL规则中的**source**参数用来指定MLD报文中的IPv6组播源地址（对于MLDv1报文和未携带IPv6组播源地址的IS_EX/TO_EX类型的MLDv2报文，视其IPv6组播源地址为0::0）范围，**destination**参数用来指定IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·由于本命令只能过滤MLD报文，因此无法对接口静态加入IPv6组播组或组播源组进行限制。

【举例】

·路由应用：

\# 限定接口GigabitEthernet1/0/1下的主机只能加入IPv6组播组FF03::101。

\<Sysname\> system-view

Sysname acl ipv6 basic 2005

Sysname-acl-ipv6-basic-2005 rule permit source ff03::101 128

Sysname-acl-ipv6-basic-2005 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld group-policy 2005

·交换应用：

\# 限定接口Vlan-interface100下的主机只能加入IPv6组播组FF03::101。

\<Sysname\> system-view

Sysname acl ipv6 basic 2005

Sysname\--acl-ipv6-basic-2005 rule permit source ff03::101 128

Sysname\--acl-ipv6-basic-2005 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld group-policy 2005

**MLD \-- MLD配置命令 \-- mld join-by-session**

------------------------------------------------------------------------

![说明](MLD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mld** **join-by-session**]命令用来配置按会话记录用户加入的IPv6组播组。

**[undo****mld** **join-by-session**]命令用来恢复缺省情况。

【命令】

**[mld** **join-by-session**]

**[undo** **mld** **join-by-session**]

【缺省情况】

按接口记录用户加入的IPv6组播组。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当按接口记录用户加入的IPv6组播组时，设备只会向物理接口发送一份IPv6组播报文；当按会话记录用户加入的IPv6组播组时，设备会向接口下的每位用户分别发送一份IPv6组播报文。

·**mld** **join-by-session**命令与**mld** **user-vlan-aggregation** **dot1q**命令互斥，不允许同时配置。

【举例】

\# 在接口GigabitEthernet1/0/1上配置按会话记录用户加入的IPv6组播组。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld join-by-session

**MLD \-- MLD配置命令 \-- mld last-listener-query-count**

------------------------------------------------------------------------

**[mld last-listener-query-count**]命令用来在接口上配置MLD最后组成员查询次数。

**[undo mld last-listener-query-count**]命令用来恢复缺省情况。

【命令】

**[mld last-listener-query-count ***count*]

**[undo mld last-listener-query-count**]

【缺省情况】

MLD最后组成员查询次数等于MLD查询器的健壮系数。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定MLD最后组成员查询次数，取值范围为1～255。

【使用指导】

本命令与**last-listener-query-count**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD最后组成员查询次数为6次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld last-listener-query-count 6

·交换应用：

\# 在接口Vlan-interface100上配置MLD最后组成员查询次数为6次。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld last-listener-query-count 6

【相关命令】

·**last-listener-query-count** (MLD view)

**MLD \-- MLD配置命令 \-- mld last-listener-query-interval**

------------------------------------------------------------------------

**[mld last-listener-query-interval**]命令用来在接口上配置MLD最后组成员查询间隔。

**[undo mld last-listener-query-interval**]命令用来恢复缺省情况。

【命令】

**[mld last-listener-query-interval***interval*]

**[undo mld last-listener-query-interval**]

【缺省情况】

MLD最后组成员查询间隔为1秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定MLD最后组成员查询间隔，取值范围为1～25，单位为秒。

【使用指导】

本命令与**last-listener-query-interval**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD最后组成员查询间隔为6秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld last-listener-query-interval 6

·交换应用：

\# 在接口Vlan-interface100上配置MLD最后组成员查询间隔为6秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld last-listener-query-interval 6

【相关命令】

·**last-listener-query-interval** (MLD view)

**MLD \-- MLD配置命令 \-- mld max-response-time**

------------------------------------------------------------------------

**[mld max-response-time**]命令用来在接口上配置MLD普遍组查询报文的最大响应时间。

**[undo mld max-response-time**]命令用来恢复缺省情况。

【命令】

**[mld max-response-time*** time*]

**[undo mld max-response-time**]

【缺省情况】

MLD普遍组查询报文的最大响应时间为10秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定MLD普遍组查询报文的最大响应时间，取值范围为1～3174，单位为秒。

【使用指导】

本命令与**max-response-time**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD普遍组查询报文的最大响应时间为25秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld max-response-time 25

·交换应用：

\# 在接口Vlan-interface100上配置MLD普遍组查询报文的最大响应时间为25秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld max-response-time 25

【相关命令】

·**max-response-time** (MLD view)

**MLD \-- MLD配置命令 \-- mld other-querier-present-timeout**

------------------------------------------------------------------------

**[mld** **other-querier-present-timeout**]命令用来在接口上配置MLD其它查询器的存在时间。

**[undo** **mld other-querier-present-timeout**]命令用来恢复缺省情况。

【命令】

**[mld** **other-querier-present-timeout** *time*]

**[undo** **mld** **other-querier-present-timeout**]

【缺省情况】

MLD其它查询器的存在时间＝MLD普遍组查询报文的发送间隔×MLD查询器的健壮系数＋MLD普遍组查询的最大响应时间÷2。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定MLD其它查询器的存在时间，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**other-querier-present-timeout**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD其它查询器的存在时间为125秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld other-querier-present-timeout 125

·交换应用：

\# 在接口Vlan-interface100上配置MLD其它查询器的存在时间为125秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld other-querier-present-timeout 125

【相关命令】

·**other-querier-present-****timeout** (MLD view)

**MLD \-- MLD配置命令 \-- mld proxy enable**

------------------------------------------------------------------------

**[mld** **proxy** **enable**]命令用来在接口上使能MLD代理功能。

**[undo** **mld** **proxy** **enable**]命令用来关闭接口上的MLD代理功能。

【命令】

**[mld** **proxy** **enable**]

**[undo** **mld** **proxy** **enable**]

【缺省情况】

接口上的MLD代理功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IPv6组播路由，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的Ipv6组播路由，并在接口GigabitEthernet1/0/1上使能MLD代理功能。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld proxy enable

·交换应用：

\# 使能公网实例中的IPv6组播路由，并在接口Vlan-interface100上使能MLD代理功能。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld proxy enable

【相关命令】

·**ipv6****multicast** **routing**（IP组播命令参考/IPv6组播路由与转发）

**MLD \-- MLD配置命令 \-- mld proxy forwarding**

------------------------------------------------------------------------

**[mld** **proxy** **forwarding**]命令用来使能非查询器转发功能。

**[undo** **mld** **proxy** **forwarding**]命令用来关闭非查询器转发功能。

【命令】

**[mld** **proxy** **forwarding**]

**[undo** **mld** **proxy** **forwarding**]

【缺省情况】

非查询器转发功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

IPv6组播数据通常只被查询器转发，非查询器不具备IPv6组播转发能力，这样可避免IPv6组播数据被重复转发。但如果MLD代理设备的路由器接口未能当选查询器，应在该接口上使能非查询器转发功能，否则下游主机将无法收到IPv6组播数据。

【举例】

·路由应用：

\# 在MLD代理设备的路由器接口GigabitEthernet1/0/1上使能非查询器转发功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld proxy forwarding

·交换应用：

\# 在MLD代理设备的路由器接口Vlan-interface100上使能非查询器转发功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld proxy forwarding

**MLD \-- MLD配置命令 \-- mld query-interval**

------------------------------------------------------------------------

**[mld** **query-interval**]命令用来在接口上配置MLD普遍组查询报文的发送间隔。

**[undo** **mld** **query-interval**]命令用来恢复缺省情况。

【命令】

**[mld** **query-interval** *interval*]

**[undo** **mld** **query-interval**]

【缺省情况】

MLD普遍组查询报文的发送间隔为125秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定MLD普遍组查询报文的发送间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**query-interval**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD普遍组查询报文的发送间隔为60秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld query-interval 60

·交换应用：

\# 在接口Vlan-interface100上配置MLD普遍组查询报文的发送间隔为60秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld query-interval 60

【相关命令】

·**query-interval** (MLD view)

**MLD \-- MLD配置命令 \-- mld robust-count**

------------------------------------------------------------------------

**[mld robust-count**]命令用来在接口上配置MLD查询器的健壮系数。

**[undo mld robust-count**]命令用来恢复缺省情况。

【命令】

**[mld robust-count*** count*]

**[undo mld robust-count**]

【缺省情况】

MLD查询器的健壮系数为2。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定MLD查询器的健壮系数，取值范围为1～255。

【使用指导】

·MLD查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，MLD查询器就越"健壮"，但是组播组超时所需的时间也就越长。

·本命令与**robust-count**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD查询器的健壮系数为5。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld robust-count 5

·交换应用：

\# 在接口Vlan-interface100上配置MLD查询器的健壮系数为5。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld robust-count 5

【相关命令】

·**robust-count** (MLD view)

**MLD \-- MLD配置命令 \-- mld startup-query-count**

------------------------------------------------------------------------

**[mld startup-query-count**]命令用来在接口上配置MLD查询器的启动查询次数。

**[undo mld startup-query-count**]命令用来恢复缺省情况。

【命令】

**[mld startup-query-count*** count*]

**[undo mld startup-query-count**]

【缺省情况】

MLD查询器的启动查询次数等于MLD查询器的健壮系数。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定MLD查询器的启动查询次数，取值范围为1～255。

【使用指导】

本命令与**startup-query-count**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD查询器的启动查询次数为5次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld startup-query-count 5

·交换应用：

\# 在接口Vlan-interface100上配置MLD查询器的启动查询次数为5次。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld startup-query-count 5

【相关命令】

·**startup-query-count** (MLD view)

**MLD \-- MLD配置命令 \-- mld startup-query-interval**

------------------------------------------------------------------------

**[mld startup-query-interval**]命令用来在接口上配置MLD查询器的启动查询间隔。

**[undo mld startup-query-interval**]命令用来恢复缺省情况。

【命令】

**[mld startup-query-interval***interval*]

**[undo mld startup-query-interval**]

【缺省情况】

MLD查询器的启动查询间隔为MLD普遍组查询报文发送间隔的1/4。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定MLD查询器的启动查询间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**startup-query-interval**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置MLD查询器的启动查询间隔为100秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld startup-query-interval 100

·交换应用：

\# 在接口Vlan-interface100上配置MLD查询器的启动查询间隔为100秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld startup-query-interval 100

【相关命令】

·**startup-query-interval** (MLD view)

**MLD \-- MLD配置命令 \-- mld static-group**

------------------------------------------------------------------------

**[mld** **static-group**]命令用来配置接口静态加入IPv6组播组或组播源组。

**[undo** **mld** **static-group**]命令用来恢复缺省情况。

【命令】

**[mld** **static-group** *ipv6-group-address* [ **source** *ipv6-source-address*  [ **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* ]]]

**[undo**[ **mld** **static-group** { **all** \| *ipv6-group-address* [ **source** *ipv6-source-address*   **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* ] }]]

【缺省情况】

接口没有以静态方式加入任何IPv6组播组或组播源组。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-group-address*]：指定IPv6组播组地址，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。

*[ipv6-source-address*]：指定组播源的IPv6地址。如果未指定本参数，表示针对所有组播源。

**[dot1q** **vid** *vlan-list*]：指定封装的第一层VLAN Tag。*vlan-list*为VLAN列表，表示一或多个第一层VLAN Tag，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list*]：指定封装的第一层和第二层VLAN Tag。*vlan-id*表示第一层VLAN Tag，取值范围为1～4094；*vlan-list*为VLAN列表，表示一或多个第二层VLAN Tag，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：删除此接口加入的所有静态IPv6组播组。

【使用指导】

·如果指定的IPv6组播组地址在SSM组地址范围内，则必须同时指定IPv6组播源的地址，否则将不会生成IPv6组播路由表项用于指导组播转发；如果指定的IPv6组播组地址不在SSM组地址范围内，则无此限制。

·对于同一个IPv6组播组或IPv6组播源组，不带VLAN封装、带一层VLAN封装和带两层VLAN封装的静态加入配置两两互斥，不允许同时配置。

·配置不带VLAN封装的静态加入时，如果子接口上没有配置**mld** **join-by-session**命令和**mld** **user-vlan-aggregation** **dot1q**命令，才生成IPv6静态组播表项。

·配置带VLAN封装的静态加入时，如果子接口上配置了**mld** **join-by-session**命令，那么当相应VLAN内的用户上线时才生成IPv6静态组播表项；如果子接口上配置了**mld** **user-vlan-aggregation** **dot1q**命令，那么只有二者的VLAN封装相同，才生成IPv6静态组播表项。

【举例】

·路由应用：

\# 配置接口GigabitEthernet1/0/1静态加入IPv6组播组FF03::101。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld static-group ff03::101

\# 配置接口GigabitEthernet1/0/1静态加入IPv6组播源组（2001::101，FF3E::202）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld static-group ff3e::202 source 2001::101

\# 配置子接口GigabitEthernet1/0/1.1按会话记录用户加入的IPv6组播组，并静态加入IPv6组播组FF03::101：当第一层VLAN Tag为10、第二层VLAN Tag范围为10～20的用户上线时才生成IPv6静态组播表项。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 mld join-by-session

Sysname-GigabitEthernet1/0/1.1 mld static-group ff03::101 dot1q vid 10 second-dot1q 10 to 20

·交换应用：

\# 配置接口Vlan-interface100静态加入IPv6组播组FF03::101。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld static-group ff03::101

\# 配置接口Vlan-interface100静态加入IPv6组播源组（2001::101，FF3E::202）。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld static-group ff3e::202 source 2001::101

**MLD \-- MLD配置命令 \-- mld user-vlan-aggregation dot1q**

------------------------------------------------------------------------

![说明](MLD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mld** **user-vlan-aggregation** **dot1q**]命令用来配置为IPv6组播报文封装的VLAN Tag。

**[undo** **mld** **user-vlan-aggregation** **dot1q**]命令用来恢复缺省情况。

【命令】

**[mld** **user-vlan-aggregation** **dot1q** **vid** *vlan-id* [ **second-dot1q** *vlan-id* ]]

**[undo** **mld** **user-vlan-aggregation** **dot1q**]

【缺省情况】

不为IPv6组播报文封装VLAN Tag。

【视图】

三层以太网子接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vid** *vlan-id*]：指定封装的第一层VLAN Tag，*vlan-id*的取值范围为1～4094。

**[second-dot1q** *vlan-id*]：指定封装的第二层VLAN Tag，*vlan-id*的取值范围为1～4094。

【使用指导】

**[mld** **join-by-session**]命令与**mld** **user-vlan-aggregation** **dot1q**命令互斥，不允许同时配置。

【举例】

\# 在子接口GigabitEthernet1/0/1.1上配置为IPv6组播报文封装的第一层VLAN Tag为10，第二层VLAN Tag为20。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 mld user-vlan-aggregation dot1q vid 10 second-dot1q 20

**MLD \-- MLD配置命令 \-- mld version**

------------------------------------------------------------------------

**[mld** **version**]命令用来在接口上配置MLD的版本。

**[undo** **mld** **version**]命令用来恢复缺省情况。

【命令】

**[mld** **version** *version-number*]

**[undo** **mld** **version**]

【缺省情况】

MLD的版本为MLDv1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：表示MLD的版本号，取值范围为1～2。

【举例】

·路由应用：

\# 指定接口GigabitEthernet1/0/1使用MLDv2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mld version 2

·交换应用：

\# 指定接口Vlan-interface100使用MLDv2。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 mld version 2

**MLD \-- MLD配置命令 \-- other-querier-present-timeout (MLD view)**

------------------------------------------------------------------------

**[other-querier-present-timeout**]命令用来全局配置MLD其它查询器的存在时间。

**[undo other-querier-present-timeout**]命令用来恢复缺省情况。

【命令】

**[other-querier-present-timeout***time*]

**[undo other-querier-present-timeout**]

【缺省情况】

MLD其它查询器的存在时间＝MLD普遍组查询报文的发送间隔×MLD查询器的健壮系数＋MLD普遍组查询的最大响应时间÷2。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定MLD其它查询器的存在时间，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**mld other-querier-present-timeout**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD其它查询器的存在时间为125秒。

\<Sysname\> system-view

Sysname mld

Sysname-mld other-querier-present-timeout 125

【相关命令】

·**mld other-querier-present-timeout**

**MLD \-- MLD配置命令 \-- proxy multipath (MLD view)**

------------------------------------------------------------------------

**[proxy** **multipath**]命令用来使能MLD代理的负载分担功能。

**[undo** **proxy** **multipath**]命令用来关闭MLD代理的负载分担功能。

【命令】

**[proxy** **multipath**]

**[undo** **proxy** **multipath**]

【缺省情况】

MLD代理的负载分担功能处于关闭状态。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当在MLD代理设备的多个接口上使能了MLD代理功能时：

·如果关闭了MLD代理的负载分担功能，则只有IPv6地址最大的接口会转发IPv6组播流量。

·如果使能了MLD代理的负载分担功能，则可通过这些接口对IPv6组播流量按组进行负载分担。

【举例】

\# 在公网实例中使能MLD代理的负载分担功能。

\<Sysname\> system-view

Sysname mld

Sysname-mld proxy multipath

**MLD \-- MLD配置命令 \-- query-interval (MLD view)**

------------------------------------------------------------------------

**[query-interval**]命令用来全局配置MLD普遍组查询报文的发送间隔。

**[undo query-interval**]命令用来恢复缺省情况。

【命令】

**[query-interval ***interval*]

**[undo query-interval**]

【缺省情况】

MLD普遍组查询报文的发送间隔为125秒。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定MLD普遍组查询报文的发送间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**mld query-interval**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD普遍组查询报文的时间间隔为60秒。

\<Sysname\> system-view

Sysname mld

Sysname-mld query-interval 60

【相关命令】

·**mld query-interval**

**MLD \-- MLD配置命令 \-- reset mld group**

------------------------------------------------------------------------

**[reset** **mld** **group**]命令用来清除MLD组播组的动态加入记录。

【命令】

**[reset** **mld** [ **vpn-instance** *vpn-instance-name*  **group**  { **all** \| **interface** *interface-type interface-number* { **all** \| *ipv6-group-address* [ *prefix-length* ]  *ipv6-source-address* [ *prefix-length*  ] } }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的记录，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的记录。

**[all**]：前一个**all**表示清除所有接口上的记录，后一个**all**表示清除所有组播组的记录。

*[interface-type* *interface-number*]：清除指定接口上的记录。

*[ipv6-group-address*]：清除指定IPv6组播组的记录，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。

*[ipv6-source-address*]：清除指定组播源的记录。如果未指定本参数，将清除所有组播源的记录。

*[prefix-length*]：指定组播源或组播组地址的前缀长度。对于组播源地址，其取值范围为0～128，缺省值为128；对于组播组地址，其取值范围为8～128，缺省值为128。

【使用指导】

执行本命令可能导致接收者中断IPv6组播信息的接收。

【举例】

·路由应用：

\# 清除公网实例所有接口上MLD组播组的动态加入记录。

\<Sysname\> reset mld group all

\# 清除公网实例接口GigabitEthernet1/0/1上所有MLD组播组的动态加入记录。

\<Sysname\> reset mld group interface gigabitethernet 1/0/1 all

\# 清除公网实例接口GigabitEthernet1/0/1上MLD组播组FF03::101:10的动态加入记录。

\<Sysname\> reset mld group interface gigabitethernet 1/0/1 ff03::101:10

·交换应用：

\# 清除公网实例所有接口上MLD组播组的动态加入记录。

\<Sysname\> reset mld group all

\# 清除公网实例接口Vlan-interface100上所有MLD组播组的动态加入记录。

\<Sysname\> reset mld group interface vlan-interface 100 all

\# 清除公网实例接口Vlan-interface100上MLD组播组FF03::101:10的动态加入记录。

\<Sysname\> reset mld group interface vlan-interface 100 ff03::101:10

【相关命令】

·**display** **mld** **group**

**MLD \-- MLD配置命令 \-- robust-count (MLD view)**

------------------------------------------------------------------------

**[robust-count**]命令用来全局配置MLD查询器的健壮系数。

**[undo robust-count**]命令用来恢复缺省情况。

【命令】

**[robust-count*** count*]

**[undo robust-count**]

【缺省情况】

MLD查询器的健壮系数为2。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定MLD查询器的健壮系数，取值范围为1～255。

【使用指导】

·MLD查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，MLD查询器就越"健壮"，但是组播组超时所需的时间也就越长。

·本命令与**mld robust-count**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD查询器的健壮系数为5。

\<Sysname\> system-view

Sysname mld

Sysname-mld robust-count 5

【相关命令】

·**mld robust-count**

**MLD \-- MLD配置命令 \-- ssm-mapping (MLD view)**

------------------------------------------------------------------------

**[ssm-mapping**]命令用来配置MLD SSM Mapping规则。

**[undo** **ssm-mapping**]命令用来删除MLD SSM Mapping规则。

【命令】

**[ssm-mapping** *ipv6-source-address* *acl6-number*]

**[undo ssm-mapping**[ { *ipv6-source-address* \| **all** }]]

【缺省情况】

未配置MLD SSM Mapping规则。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-source-address*]：指定IPv6组播源地址。

*[acl6-number*]：指定IPv6基本ACL的编号，取值范围为2000～2999。通过该ACL规则中的**permit**语句指定IPv6组播组的范围。当指定的ACL不存在或ACL中未配置有效规则，则表示未指定任何IPv6组播组。

**[all**]：删除所有的MLD SSM Mapping规则。

【使用指导】

ACL规则中的**source**参数用来指定IPv6组播组的范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

\# 在公网实例中添加如下一条MLD SSM Mapping规则：组地址范围为FF3E::/64，对应的源地址为1::1。

\<Sysname\> system-view

Sysname acl ipv6 basic 2001

Sysname-acl-ipv6-basic-2001 rule permit source ff3e:: 64

Sysname-acl-ipv6-basic-2001 quit

Sysname mld

Sysname-mld ssm-mapping 1::1 2001

【相关命令】

·**display mld ssm-mapping**

**MLD \-- MLD配置命令 \-- startup-query-count (MLD view)**

------------------------------------------------------------------------

**[startup-query-count**]命令用来全局配置MLD查询器的启动查询次数。

**[undo startup-query-count**]命令用来恢复缺省情况。

【命令】

**[startup-query-count*** count*]

**[undo startup-query-count**]

【缺省情况】

MLD查询器的启动查询次数等于MLD查询器的健壮系数。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定MLD查询器的启动查询次数，取值范围为1～255。

【使用指导】

本命令与**mld startup-query-count**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD查询器的启动查询次数为5次。

\<Sysname\> system-view

Sysname mld

Sysname-mld startup-query-count 5

【相关命令】

·**mld startup-query-count**

**MLD \-- MLD配置命令 \-- startup-query-interval (MLD view)**

------------------------------------------------------------------------

**[startup-query-interval**]命令用来全局配置MLD查询器的启动查询间隔。

**[undo startup-query-interval**]命令用来恢复缺省情况。

【命令】

**[startup-query-interval***interval*]

**[undo startup-query-interval**]

【缺省情况】

MLD查询器的启动查询间隔为MLD普遍组查询报文发送间隔的1/4。

【视图】

MLD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定MLD查询器的启动查询间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**mld startup-query-interval**命令的功能相同，只是作用范围不同：MLD视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置MLD查询器的启动查询间隔为100秒。

\<Sysname\> system-view

Sysname mld

Sysname-mld startup-query-interval 100

【相关命令】

·**mld startup-query-interval**

