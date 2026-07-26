
**IGMP \-- IGMP配置命令 \-- display igmp group**

------------------------------------------------------------------------

**[display** **igmp** **group**]命令用来显示IGMP组播组（即通过IGMP加入的组播组）的信息。

【命令】

**[display** **igmp** [ **vpn-instance** *vpn-instance-name*  **group** [ *group-address* \| **interface** *interface-type interface-number*   **static** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[group-address*]：显示指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

**[interface** *interface-type interface-number*]：显示指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。

**[static**]：显示静态加入的组播组信息。如果未指定本参数，将只显示动态加入的组播组信息。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例中动态加入的所有IGMP组播组信息。

\<Sysname\> display igmp group

IGMP groups in total: 3

 GigabitEthernet1/0/1(10.10.1.20):

  IGMP groups reported in total: 3

   Group address   Last reporter   Uptime      Expires

   225.1.1.1       10.10.1.10      00:02:04    00:01:15

   225.1.1.2       10.10.1.10      00:02:04    00:01:15

   225.1.1.3       10.10.1.10      00:02:04    00:01:15

表1-1 display igmp group命令显示信息描述表

字段

描述

IGMP groups in total

IGMP组播组的总数

IGMP groups reported in total

当前接口上动态加入的IGMP组播组总数

Group address

组播组地址

Last reporter

最后发送报告报文的主机地址

Uptime

组播组的运行时间

Expires

组播组的超时时间，Off表示该定时器关闭

\# 显示公网实例中动态加入的IGMP组播组232.1.1.1的详细信息（假设当前运行IGMP SSM Mapping）。

\<Sysname\> display igmp group 232.1.1.1 verbose

 GigabitEthernet1/0/1(10.10.1.20):

  IGMP groups reported in total: 3

   Group: 232.1.1.1

     Uptime: 00:00:34

     Exclude expires: 00:04:16

     Mapping expires: 00:02:16

     Last reporter: 10.10.1.10

     Last-member-query-counter: 0

     Last-member-query-timer-expiry: Off

     Mapping last-member-query-counter: 0

     Mapping last-member-query-timer-expiry: Off

     Group mode: Exclude

     Version1-host-present-timer-expiry: Off

     Version2-host-present-timer-expiry: 00:02:11

     Mapping version1-host-present-timer-expiry: Off

     Source list (sources in total: 1):

       Source: 10.1.1.1

          Uptime: 00:00:03

          V3 expires: 00:04:16

          Mapping expires: 00:02:16

          Last-member-query-counter: 0

          Last-member-query-timer-expiry: Off

表1-2 display igmp group verbose命令显示信息描述表

字段

描述

IGMP groups reported in total

当前接口上动态加入的IGMP组播组总数

Group

组播组地址

Uptime

组播组的运行时间

Exclude expires

EXCLUDE模式下组播组的超时时间，Off表示该定时器关闭

 

Mapping expires

IGMP SSM Mapping规则所生成组播组的超时时间。只有运行IGMP SSM Mapping时才会显示本字段

Last reporter

最后发送报告报文的主机地址

Last-member-query-counter

最后组成员查询次数

Last-member-query-timer-expiry

最后组成员查询定时器的超时时间，Off表示该定时器关闭

Mapping last-member-query-counter

IGMP SSM Mapping规则所生成组播组的最后组成员查询次数。只有运行IGMP SSM Mapping时才会显示本字段

Mapping last-member-query-timer-expiry

IGMP SSM Mapping规则所生成组播组的最后组成员查询定时器的超时时间，Off表示该定时器关闭。只有运行IGMP SSM Mapping时才会显示本字段

Group mode

对组播源的过滤模式：

·Include：表示INCLUDE模式

·Exclude：表示EXCLUDE模式

IGMPv1/v2本身并不区分过滤模式，但当运行IGMP SSM Mapping时，会根据具体配置以及加入的组播组来显示相应的模式；而当未运行IGMP SSM Mapping时，则固定显示为Exclude

Version1-host-present-timer-expiry

IGMPv1主机超时时间，Off表示该定时器关闭。只有运行IGMPv2或IGMPv3时才会显示本字段

Version2-host-present-timer-expiry

IGMPv2主机超时时间，Off表示该定时器关闭。只有运行IGMPv3时才会显示本字段

Mapping version1-host-present-timer-expiry

运行IGMP SSM Mapping时IGMPv1主机的超时时间，Off表示该定时器关闭。只有运行IGMP SSM Mapping时才会显示本字段

Source list (sources in total: 1)

组播源列表及总数。只有运行IGMPv3或IGMP SSM Mapping时才会显示本字段

Source

组播源地址。只有运行IGMPv3或IGMP SSM Mapping时才会显示本字段

Uptime

组播源的运行时间。只有运行IGMPv3或IGMP SSM Mapping时才会显示本字段

V3 expires

IGMPv3组播源的超时时间，Off表示该定时器关闭，"\-\--"表示该组播源由IGMP SSM Mapping规则生成。只有运行IGMPv3或IGMP SSM Mapping时才会显示本字段

Mapping expires

IGMP SSM Mapping规则所生成组播源的超时时间。只有运行IGMP SSM Mapping时才会显示本字段

Last-member-query-counter

最后源组成员查询次数。只有运行IGMPv3或IGMP SSM Mapping时才会显示本字段

Last-member-query-timer-expiry

最后源组成员查询定时器的超时时间，Off表示该定时器关闭。只有运行IGMPv3或IGMP SSM Mapping时才会显示本字段

\# 显示公网实例中静态加入的IGMP组播组信息。

\<Sysname\> display igmp group static

 Entries in total: 2

   Group address   Source address  Interface           Expires

   225.1.1.1       0.0.0.0         GE1/0/1             Never

   225.2.2.2       1.1.1.1         GE1/0/1             Never

表1-3 display igmp group static命令显示信息描述表

字段

描述

Entries in total

IGMP组播组的总数

Group address

组播组地址

Source address

组播源地址

Interface

接口名称

Expires

组播组的超时时间，固定显示为Never，表示永不超时

【相关命令】

·**reset** **igmp** **group**

**IGMP \-- IGMP配置命令 \-- display igmp interface**

------------------------------------------------------------------------

**[display** **igmp** **interface**]命令用来显示接口上IGMP配置和运行的信息。

【命令】

**[display** **igmp** [ **vpn-instance** *vpn-instance-name*  **interface**  *interface-type interface-number*  [ **host** \| **proxy** ]  **verbose** ]]

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

**[host**]：显示主机接口（即使能了IGMP主机行为的接口）的信息。如果未指定本参数，将显示所有接口的信息。有关IGMP主机行为的详细介绍，请参见"VXLAN配置指导"中的"VXLAN"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[proxy**]：显示代理接口的信息。如果未指定本参数，将显示所有接口的信息。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例接口GigabitEthernet1/0/1（非代理接口）上IGMP配置和运行的详细信息。

\<Sysname\> display igmp interface gigabitethernet 1/0/1 verbose

 GigabitEthernet1/0/1(10.10.1.20):

   IGMP is enabled.

   IGMP version: 2

   Query interval for IGMP: 125s

   Other querier present time for IGMP: 255s

   Maximum query response time for IGMP: 10s

   Last member query interval: 1s

   Last member query count: 2

   Startup query interval: 31s

   Startup query count: 2

   General query timer expiry (hh:mm:ss): 00:00:54

   Querier for IGMP: 10.10.1.20 (This router)

   IGMP activity: 1 join(s), 0 leave(s)

   Multicast routing on this interface: Enabled

   Robustness: 2

   Require-router-alert: Disabled

   Fast-leave: Disabled

   Startup-query: Off

   Other-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--

   Authorization: Disabled

   Join-by-session: Disabled

   User-VLAN-aggregation: Disabled

  IGMP groups reported in total: 1

\# 显示公网实例所有代理接口上IGMP配置和运行的详细信息。

\<Sysname\> display igmp interface proxy verbose

 GigabitEthernet1/0/2(20.10.1.20):

   IGMP proxy is enabled.

   IGMP version: 2

   Multicast routing on this interface: Enabled

   Require-router-alert: Disabled

   Version1-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--

\# 显示公网实例所有主机接口上IGMP配置和运行的详细信息。

\<Sysname\> display igmp interface host verbose

 GigabitEthernet1/0/3(30.10.1.20):

   IGMP host is enabled.

   IGMP version: 2

   Multicast routing on this interface: Enabled

   Require-router-alert: Disabled

   Version1-querier-present-timer-expiry (hh:mm:ss): \--:\--:\--

表1-4 display igmp interface命令显示信息描述表

字段

描述

GigabitEthernet1/0/1(10.10.1.20)

接口的名称和IP地址

IGMP is enabled

IGMP已使能

IGMP version

此接口运行的IGMP版本

Query interval for IGMP

IGMP普遍组查询报文的发送间隔（秒）

Other querier present time for IGMP

IGMP其它查询器的存在时间（秒）

Maximum query response time for IGMP

IGMP普遍组查询报文的最大响应时间（秒）

Last member query interval

最后组成员查询间隔（秒）

Last member query count

最后组成员查询次数

Startup query interval

IGMP查询器启动查询间隔（秒）

Startup query count

IGMP查询器启动查询次数

General query timer expiry

IGMP普遍组查询的超时时间，Off表示该定时器关闭

Querier for IGMP

IGMP查询器的IP地址。当本设备运行IGMPv1且不是IGMPv1查询器时，将不会显示本字段

IGMPv1查询器由PIM DR来担任，可通过**display pim interface**命令查看

No querier elected

没有进行IGMP查询器选举。只有本设备运行IGMPv1且不是IGMPv1查询器时才会显示本字段

IGMPv1查询器由PIM DR来担任，可通过**display pim interface**命令查看

IGMP activity: 1 join(s), 0 leave(s)

IGMP的活动统计：

·join(s)：表示加入过的组播组总数

·leave(s)：表示离开过的组播组总数

Multicast routing on this interface

是否使能IP组播路由功能：

·Enabled：表示已使能

·Disabled：表示未使能

Robustness

IGMP查询器的健壮系数

Require-router-alert

是否使能丢弃未携带Router-Alert选项的IGMP报文功能：

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

IGMP其它查询器的存在超时时间，Off表示该定时器关闭

Authorization

是否使能可控组播功能：

·Enabled：表示已使能

·Disabled：表示未使能

本字段的支持情况与设备的型号有关，请以设备的实际情况为准

Join-by-session

是否使能按会话记录加入组播组的用户功能：

·Enabled：表示已使能

·Disabled：表示未使能

本字段的支持情况与设备的型号有关，请以设备的实际情况为准

User-VLAN-aggregation

是否使能边缘复制时封装VLAN Tag功能：

·Enabled：表示已使能

·Disabled：表示未使能

本字段的支持情况与设备的型号有关，请以设备的实际情况为准

IGMP groups reported in total

此接口上动态加入的组播组数量。没有加入组时不显示本字段

IGMP proxy is enabled

IGMP代理功能已使能

IGMP host is enabled

IGMP主机行为功能已使能。本字段的支持情况与设备的型号有关，请以设备的实际情况为准

Version1-querier-present-timer-expiry

IGMPv1查询器的存在超时时间

Version2-querier-present-timer-expiry

IGMPv2查询器的存在超时时间

**IGMP \-- IGMP配置命令 \-- display igmp proxy group**

------------------------------------------------------------------------

**[display** **igmp** **proxy** **group**]命令用来显示IGMP代理记录的组播组信息。

【命令】

**[display** **igmp** [ **vpn-instance** *vpn-instance-name*  **proxy** **group** [ *group-address* \| **interface** *interface-type* *interface-number* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[group-address*]：显示指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

**[interface** *interface-type* *interface-number*]：显示指定接口上的信息。如果未指定本参数，将显示所有接口上的信息。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例中IGMP代理记录的所有组播组信息。

\<Sysname\> display igmp proxy group

IGMP proxy group records in total: 2

 GigabitEthernet1/0/1(1.1.1.20):

  IGMP proxy group records in total: 2

   Group address      Member state      Expires

   225.1.1.1          Delay             00:00:02

   225.1.1.2          Idle              Off

\# 显示公网实例中IGMP代理记录的组播组225.1.1.1的详细信息。

\<Sysname\> display igmp proxy group 225.1.1.1 verbose

 GigabitEthernet1/0/1(1.1.1.20):

  IGMP proxy group records in total: 2

   Group: 225.1.1.1

     Group mode: Include

     Member state: Delay

     Expires: 00:00:02

     Source list (sources in total: 1):

       1.1.1.1

表1-5 display igmp proxy group命令显示信息描述表

字段

描述

IGMP proxy group records in total

IGMP代理记录的组播组总数

GigabitEthernet1/0/1(1.1.1.20)

IGMP代理接口的名称和IP地址

Pending proxy group

等待生效的代理组

Group address/Group

组播组地址

Member state

组播组成员的状态，其中：

·Delay：表示加入了一个组，并对该组启动了延迟发送报告报文的定时器

·Idle：表示加入了一个组，但对该组尚未启动延迟发送报告报文的定时器

Expires

组播组延迟发送报告报文的时间，Off表示该定时器关闭

Group mode

对组播源的过滤模式，其中：

·Include：表示INCLUDE模式

·Exclude：表示EXCLUDE模式

Source list

IGMP代理的组播组所包含的组播源列表

sources in total

组播源的总数

**IGMP \-- IGMP配置命令 \-- display igmp proxy routing-table**

------------------------------------------------------------------------

**[display** **igmp** **proxy** **routing-table**]命令用来显示IGMP代理路由表的信息。

【命令】

**[display** **igmp** [ **vpn-instance** *vpn-instance-name*  **proxy** **routing-table** [ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] ] \*  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[source-address*]：显示指定组播源的信息。如果未指定本参数，将显示所有组播源的信息。

*[group-address*]：显示指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将显示所有组播组的信息。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播源地址，其取值范围为0～32，缺省值为32；对于组播组地址，其取值范围为4～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[verbose**]：显示详细信息。

【举例】

\# 显示公网实例IGMP代理路由表的信息。

\<Sysname\> display igmp proxy routing-table

 Total 1 (\*, G) entries, 2 (S, G) entries.

(172.168.0.12, 227.0.0.1)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: IGMP

 (\*, 225.1.1.1)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: STATIC

 (2.2.2.2, 225.1.1.1)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (2 in total):

         1: LoopBack1

             Protocol: STATIC

         2: Vlan-interface2

             Protocol: PROXY

\# 显示公网实例IGMP代理路由表的详细信息。

\<Sysname\> display igmp proxy routing-table verbose

 Total 1 (\*, G) entries, 2 (S, G) entries.

 (172.168.0.12, 227.0.0.1)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: IGMP

             Querier state: Querier

             Join/Prune state：Join

     Non-downstream interfaces: None

 (\*, 225.1.1.1)

     Upstream interface: GigabitEthernet1/0/1

     Downstream interfaces (1 in total):

         1: Vlan-interface2

             Protocol: STATIC

             Querier state: Querier

             Join/Prune state：Join

     Non-downstream interfaces (1 in total):

         1: Vlan-interface3

             Protocol: IGMP

             Querier state: Non-querier

             Join/Prune state：Join

 (2.2.2.2, 225.1.1.1)

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

表1-6 display igmp proxy routing-table命令显示信息描述表

字段

描述

Total 1 (\*, G) entries, 2 (S, G) entries

（S，G）表项和（\*，G）表项的总数

(172.168.0.12, 227.0.0.1)

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

·IGMP：表示动态IGMP

·PROXY：表示IGMP代理

·STATIC：表示静态IGMP

Querier state

接口的查询器状态：

·Querier：表示接口为IGMP查询器

·Non-querier：表示接口不是IGMP查询器

Join/Prune state

接口的加入/剪枝状态：

·NI：表示默认状态

·Join：表示处于IGMP加入的状态

·Prune：表示处于IGMP剪枝的状态

**IGMP \-- IGMP配置命令 \-- display igmp ssm-mapping**

------------------------------------------------------------------------

**[display** **igmp** **ssm-mapping**]命令用来显示IGMP SSM Mapping规则。

【命令】

**[display** **igmp** [ **vpn-instance** *vpn-instance-name*  **ssm-mapping** *group-address*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[group-address*]：显示指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。

【举例】

\# 显示公网实例中组播组232.1.1.1对应的IGMP SSM Mapping规则。

\<Sysname\> display igmp ssm-mapping 232.1.1.1

 Group: 232.1.1.1

 Source list:

        1.2.3.4

        5.5.5.5

        10.1.1.1

        100.1.1.10

表1-7 display igmp ssm-mapping命令显示信息描述表

字段

描述

Group

组播组地址

Source list

组播源地址列表

**IGMP \-- IGMP配置命令 \-- display igmp user-authorization**

------------------------------------------------------------------------

![说明](IGMP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **igmp** **user-authorization**]命令用来显示IGMP用户的授权信息。

【命令】

**[display** **igmp** **user-authorization** [ **interface** *interface-type* *interface-number* ]]

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

\# 显示所有IGMP用户的授权信息。

\<Sysname\> display igmp user-authorization

 Authorized users in total: 3

   User name: user1@isp1

   Access type: PPP

   Interface: Virtual-Access0

   Access interface: Virtual-Access0

   Maximum programs for order: 4

   User profile: profile1

   Authorized programs list:

     225.0.0.1

   User name: user2

   Access type: IPoE

   Interface: Multicast-UA0

   Access interface: GigabitEthernet1/0/1.1

   VLAN ID: 100

   Second VLAN ID: 10

   Maximum programs for order: 4

   User profile: profile1

   Authorized programs list:

     225.0.0.1

     225.0.0.2

     225.0.0.3

   User name: user3

   Access type: Portal

   Interface: Multicast-UA1

   Access interface: GigabitEthernet1/0/2

   Maximum programs for order: 4

   User profile: profile1

   Authorized programs list:

     225.0.0.1

     225.0.0.2

表1-8 display igmp user-authorization命令显示信息描述表

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

允许用户加入组播组的最大数量

User profile

用户授权的User Profile名称，用户可加入该User Profile下通过**igmp** **access-policy**命令所配置接入策略中的组播组

Authorized programs list

用户授权加入的组播组列表

**IGMP \-- IGMP配置命令 \-- igmp**

------------------------------------------------------------------------

**[igmp**]命令用来进入IGMP视图。

**[undo** **igmp**]命令用来清除IGMP视图下的所有配置。

【命令】

**[igmp** [ **vpn-instance** *vpn-instance-name* ]]

**[undo** **igmp** [ **vpn-instance** *vpn-instance-name* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【举例】

\# 进入公网实例的IGMP视图。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp

\# 进入VPN实例mvpn的IGMP视图。

\<Sysname\> system-view

Sysname igmp vpn-instance mvpn

Sysname-igmp-mvpn

**IGMP \-- IGMP配置命令 \-- igmp access-policy**

------------------------------------------------------------------------

![说明](IGMP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[igmp** **access-policy**]命令用来配置IGMP用户的接入策略。

**[undo** **igmp** **access-policy**]命令用来删除IGMP用户的接入策略。

【命令】

**[igmp** **access-policy** *acl-number*]

**[undo** **igmp** **access-policy** *acl-number*]

【缺省情况】

没有配置IGMP用户的接入策略，即IGMP用户未被授权加入组播组。

【视图】

User-Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本或高级ACL的编号，取值范围为2000～3999。IGMP用户只能加入该ACL规则所允许的组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有组播组。

【使用指导】

·对于IPv4基本ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv4高级ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播源地址（对于IGMPv1/v2报文和未携带组播源地址的IS_EX/TO_EX类型的IGMPv3报文，视其组播源地址为0.0.0.0）范围，**destination**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·通过多次执行本命令可以配置多条IGMP用户接入策略，用户发送的IGMP成员关系报告报文只需匹配其中一条就允许通过。

【举例】

\#在名为abc的User Profile下配置只允许IGMP用户加入组播组225.1.1.2。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 225.1.1.2 0

Sysname-acl-ipv4-basic-2000 quit

Sysname user-profile abc

Sysname-user-profile-abc igmp access-policy 2000

**IGMP \-- IGMP配置命令 \-- igmp authorization-enable**

------------------------------------------------------------------------

![说明](IGMP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[igmp** **authorization-enable**]命令用来使能可控组播功能。

**[undo** **igmp** **authorization-enable**]命令用来关闭可控组播功能。

【命令】

**[igmp** **authorization-enable**]

**[undo** **igmp** **authorization-enable**]

【缺省情况】

可控组播功能处于关闭状态。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/VT接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在接口GigabitEthernet1/0/1上使能可控组播功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp authorization-enable

**IGMP \-- IGMP配置命令 \-- igmp enable**

------------------------------------------------------------------------

**[igmp** **enable**]命令用来在接口上使能IGMP。

**[undo** **igmp** **enable**]命令用来在接口上关闭IGMP。

【命令】

**igmp** **enable**

**[undo** **igmp** **enable**]

【缺省情况】

接口上的IGMP处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·只有在相应实例中先使能了IP组播路由，本命令才能生效。

·只有在接口上使能了IGMP，在该接口上所做的IGMP配置才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IP组播路由，并在接口GigabitEthernet1/0/1上使能IGMP。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp enable

·交换应用：

\# 使能公网实例中的IP组播路由，并在接口Vlan-interface100上使能IGMP。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp enable

【相关命令】

·**multicast** **routing**（IP组播命令参考/组播路由与转发）

**IGMP \-- IGMP配置命令 \-- igmp fast-leave**

------------------------------------------------------------------------

**[igmp** **fast-leave**]命令用来在接口上使能组播组成员快速离开功能。

**[undo** **igmp** **fast-leave**]命令用来在接口上关闭组播组成员快速离开功能。

【命令】

**[igmp** **fast-leave** [ **group-policy** *acl-number* ]]

**[undo** **igmp** **fast-leave**]

【缺省情况】

组播组成员快速离开功能处于关闭状态，即IGMP查询器在收到主机发送的IGMP离开组报文后将发送IGMP特定组查询报文或IGMP特定源组查询报文，而不会直接向上游发送离开通告。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本ACL的编号，取值范围为2000～2999。如果指定了本参数，快速离开功能将只为该ACL规则所允许的组播组服务；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则快速离开功能将为所有组播组服务。

【使用指导】

ACL规则中的**source**参数用来指定组播组的范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上使能组播组成员快速离开功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp fast-leave

·交换应用：

\# 在接口Vlan-interface100上使能组播组成员快速离开功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp fast-leave

**IGMP \-- IGMP配置命令 \-- igmp group-policy**

------------------------------------------------------------------------

**[igmp** **group-policy**]命令用来在接口上配置组播组过滤器，以限定该接口下的主机所能加入的组播组。

**[undo** **igmp** **group-policy**]命令用来在接口上删除组播组过滤器。

【命令】

**[igmp** **group-policy** *acl-number* [ *version-number* ]]

**[undo** **igmp** **group-policy**]

【缺省情况】

接口上没有配置组播组过滤器，即该接口下的主机可以加入任意组播组。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本或高级ACL的编号，取值范围为2000～3999。主机只能加入该ACL规则所允许的组播组。当指定的ACL不存在或ACL中未配置有效规则，将过滤掉所有组播组。

*[version-number*]：指定IGMP的版本号，取值范围为1～3。缺省情况下，系统同时支持对IGMPv1、IGMPv2和IGMPv3报告报文的过滤。

【使用指导】

·对于IPv4基本ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·对于IPv4高级ACL，该ACL规则中的**source**参数用来指定IGMP报文中的组播源地址（对于IGMPv1/v2报文和未携带组播源地址的IS_EX/TO_EX类型的IGMPv3报文，视其组播源地址为0.0.0.0）范围，**destination**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·由于本命令只能过滤IGMP报文，因此无法对接口静态加入组播组或组播源组进行限制。

【举例】

·路由应用：

\# 限定接口GigabitEthernet1/0/1下的主机只能加入组播组225.1.1.1。

\<Sysname\> system-view

Sysname acl basic 2005

Sysname-acl-ipv4-basic-2005 rule permit source 225.1.1.1 0

Sysname-acl-ipv4-basic-2005 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp group-policy 2005

·交换应用：

\# 限定接口Vlan-interface100下的主机只能加入组播组225.1.1.1。

\<Sysname\> system-view

Sysname acl basic 2005

Sysname-acl-ipv4-basic-2005 rule permit source 225.1.1.1 0

Sysname-acl-ipv4-basic-2005 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp group-policy 2005

**IGMP \-- IGMP配置命令 \-- igmp join-by-session**

------------------------------------------------------------------------

![说明](IGMP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[igmp** **join-by-session**]命令用来配置按会话记录用户加入的组播组。

**[undo** **igmp** **join-by-session**]命令用来恢复缺省情况。

【命令】

**[igmp** **join-by-session**]

**[undo** **igmp** **join-by-session**]

【缺省情况】

按接口记录用户加入的组播组。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当按接口记录用户加入的组播组时，设备只会向物理接口发送一份组播报文；当按会话记录用户加入的组播组时，设备会向接口下的每位用户分别发送一份组播报文。

·**igmp** **join-by-session**命令与**igmp** **user-vlan-aggregation** **dot1q**命令互斥，不允许同时配置。

【举例】

\# 在接口GigabitEthernet1/0/1上配置按会话记录用户加入的组播组。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp join-by-session

**IGMP \-- IGMP配置命令 \-- igmp last-member-query-count**

------------------------------------------------------------------------

**[igmp last-member-query-count**]命令用来在接口上配置IGMP最后组成员查询次数。

**[undo igmp last-member-query-count**]命令用来恢复缺省情况。

【命令】

**[igmp last-member-query-count ***count*]

**[undo igmp last-member-query-count**]

【缺省情况】

IGMP最后组成员查询次数等于IGMP查询器的健壮系数。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定IGMP最后组成员查询次数，取值范围为1～255。

【使用指导】

本命令与**last-member-query-count**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP最后组成员查询次数为6次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp last-member-query-count 6

·交换应用：

\# 在接口Vlan-interface100上配置IGMP最后组成员查询次数为6次。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp last-member-query-count 6

【相关命令】

·**last-member-query-count** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp last-member-query-interval**

------------------------------------------------------------------------

**[igmp last-member-query-interval**]命令用来在接口上配置IGMP最后组成员查询间隔。

**[undo igmp last-member-query-interval**]命令用来恢复缺省情况。

【命令】

**[igmp last-member-query-interval*** interval*]

**[undo igmp last-member-query-interval**]

【缺省情况】

IGMP最后组成员查询间隔为1秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP最后组成员查询间隔，取值范围为1～25，单位为秒。

【使用指导】

本命令与**last-member-query-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP最后组成员查询间隔为6秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp last-member-query-interval 6

·交换应用：

\# 在接口Vlan-interface100上配置IGMP最后组成员查询间隔为6秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp last-member-query-interval 6

【相关命令】

·**last-member-query-interval** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp max-response-time**

------------------------------------------------------------------------

**[igmp max-response-time**]命令用来在接口上配置IGMP普遍组查询报文的最大响应时间。

**[undo igmp max-response-time**]命令用来恢复缺省情况。

【命令】

**[igmp max-response-time*** time*]

**[undo igmp max-response-time**]

【缺省情况】

IGMP普遍组查询报文的最大响应时间为10秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定IGMP普遍组查询报文的最大响应时间，取值范围为1～3174，单位为秒。

【使用指导】

本命令与**max-response-time**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP普遍组查询报文的最大响应时间为25秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp max-response-time 25

·交换应用：

\# 在接口Vlan-interface100上配置IGMP普遍组查询报文的最大响应时间为25秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp max-response-time 25

【相关命令】

·**max-response-time** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp other-querier-present-interval**

------------------------------------------------------------------------

**[igmp** **other-querier-present-interval**]命令用来在接口上配置IGMP其它查询器的存在时间。

**[undo** **igmp other-querier-present-interval**]命令用来恢复缺省情况。

【命令】

**[igmp** **other-querier-present-interval** *interval*]

**[undo** **igmp** **other-querier-present-interval**]

【缺省情况】

IGMP其它查询器的存在时间＝IGMP普遍组查询报文的发送间隔×IGMP查询器的健壮系数＋IGMP普遍组查询的最大响应时间÷2。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP其它查询器的存在时间，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**other-querier-present-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP其它查询器的存在时间为125秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp other-querier-present-interval 125

·交换应用：

\# 在接口Vlan-interface100上配置IGMP其它查询器的存在时间为125秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp other-querier-present-interval 125

【相关命令】

·**other-querier-present-interval** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp proxy enable**

------------------------------------------------------------------------

**[igmp** **proxy** **enable**]命令用来在接口上使能IGMP代理功能。

**[undo** **igmp** **proxy** **enable**]命令用来关闭接口上的IGMP代理功能。

【命令】

**[igmp** **proxy** **enable**]

**[undo** **igmp** **proxy** **enable**]

【缺省情况】

接口上的IGMP代理功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IP组播路由，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IP组播路由，并在接口GigabitEthernet1/0/1上使能IGMP代理功能。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp proxy enable

·交换应用：

\# 使能公网实例中的IP组播路由，并在接口Vlan-interface100上使能IGMP代理功能。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp proxy enable

【相关命令】

·**multicast** **routing**（IP组播命令参考/组播路由与转发）

**IGMP \-- IGMP配置命令 \-- igmp proxy forwarding**

------------------------------------------------------------------------

**[igmp** **proxy** **forwarding**]命令用来使能非查询器转发功能。

**[undo** **igmp** **proxy** **forwarding**]命令用来关闭非查询器转发功能。

【命令】

**[igmp** **proxy** **forwarding**]

**[undo** **igmp** **proxy** **forwarding**]

【缺省情况】

非查询器转发功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

组播数据通常只被查询器转发，非查询器不具备组播转发能力，这样可避免组播数据被重复转发。但如果IGMP代理设备的路由器接口未能当选查询器，应在该接口上使能非查询器转发功能，否则下游主机将无法收到组播数据。

【举例】

·路由应用：

\# 在IGMP代理设备的路由器接口GigabitEthernet1/0/1上使能非查询器转发功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp proxy forwarding

·交换应用：

\# 在IGMP代理设备的路由器接口Vlan-interface100上使能非查询器转发功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp proxy forwarding

**IGMP \-- IGMP配置命令 \-- igmp query-interval**

------------------------------------------------------------------------

**[igmp** **query-interval**]命令用来在接口上配置IGMP普遍组查询报文的发送间隔。

**[undo** **igmp** **query-interval**]命令用来恢复缺省情况。

【命令】

**[igmp** **query-interval** *interval*]

**[undo** **igmp** **query-interval**]

【缺省情况】

IGMP普遍组查询报文的发送间隔为125秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP普遍组查询报文的发送间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**query-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP普遍组查询报文的发送间隔为60秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp query-interval 60

·交换应用：

\# 在接口Vlan-interface100上配置IGMP普遍组查询报文的发送间隔为60秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp query-interval 60

【相关命令】

·**query-interval** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp robust-count**

------------------------------------------------------------------------

**[igmp robust-count**]命令用来在接口上配置IGMP查询器的健壮系数。

**[undo igmp robust-count**]命令用来恢复缺省情况。

【命令】

**[igmp robust-count*** count*]

**[undo igmp robust-count**]

【缺省情况】

IGMP查询器的健壮系数为2。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定IGMP查询器的健壮系数，取值范围为1～255。

【使用指导】

·IGMP查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，IGMP查询器就越"健壮"，但是组播组超时所需的时间也就越长。

·本命令与**robust-count**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP查询器的健壮系数为5。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp robust-count 5

·交换应用：

\# 在接口Vlan-interface100上配置IGMP查询器的健壮系数为5。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp robust-count 5

【相关命令】

·**robust-count** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp startup-query-count**

------------------------------------------------------------------------

**[igmp startup-query-count**]命令用来在接口上配置IGMP查询器的启动查询次数。

**[undo igmp startup-query-count**]命令用来恢复缺省情况。

【命令】

**[igmp startup-query-count*** count*]

**[undo igmp startup-query-count**]

【缺省情况】

IGMP查询器的启动查询次数等于IGMP查询器的健壮系数。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定IGMP查询器的启动查询次数，取值范围为1～255。

【使用指导】

本命令与**startup-query-count**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP查询器的启动查询次数为5次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp startup-query-count 5

·交换应用：

\# 在接口Vlan-interface100上配置IGMP查询器的启动查询次数为5次。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp startup-query-count 5

【相关命令】

·**startup-query-count** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp startup-query-interval**

------------------------------------------------------------------------

**[igmp startup-query-interval**]命令用来在接口上配置IGMP查询器的启动查询间隔。

**[undo igmp startup-query-interval**]命令用来恢复缺省情况。

【命令】

**[igmp startup-query-interval*** interval*]

**[undo igmp startup-query-interval**]

【缺省情况】

IGMP查询器的启动查询间隔为IGMP普遍组查询报文发送间隔的1/4。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP查询器的启动查询间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**startup-query-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IGMP查询器的启动查询间隔为100秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp startup-query-interval 100

·交换应用：

\# 在接口Vlan-interface100上配置IGMP查询器的启动查询间隔为100秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp startup-query-interval 100

【相关命令】

·**startup-query-interval** (IGMP view)

**IGMP \-- IGMP配置命令 \-- igmp static-group**

------------------------------------------------------------------------

**[igmp** **static-group**]命令用来配置接口静态加入组播组或组播源组。

**[undo** **igmp** **static-group**]命令用来恢复缺省情况。

【命令】

**[igmp** **static-group** *group-address* [ **source** *source-address*  [ **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* ]]]

**[undo**[ **igmp** **static-group** { **all** \| *group-address* [ **source** *source-address*   **dot1q** **vid** *vlan-list* \| **dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list* ] }]]

【缺省情况】

接口没有以静态方式加入任何组播组或组播源组。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：指定组播组地址，取值范围为224.0.1.0～239.255.255.255。

*[source-address*]：指定组播源的地址。如果未指定本参数，表示针对所有组播源。

**[dot1q** **vid** *vlan-list*]：指定封装的第一层VLAN Tag。*vlan-list*为VLAN列表，表示一或多个第一层VLAN Tag，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dot1q** **vid** *vlan-id* **second-dot1q** *vlan-list*]：指定封装的第一层和第二层VLAN Tag。*vlan-id*表示第一层VLAN Tag，取值范围为1～4094；*vlan-list*为VLAN列表，表示一或多个第二层VLAN Tag，表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。本参数只在三层以太网子接口视图和三层聚合子接口视图下支持。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[all**]：删除此接口加入的所有静态组播组。

【使用指导】

·如果指定的组播组地址在SSM组地址范围内，则必须同时指定组播源的地址，否则将不会生成组播路由表项用于指导组播转发；如果指定的组播组地址不在SSM组地址范围内，则无此限制。

·对于同一个组播组或组播源组，不带VLAN封装、带一层VLAN封装和带两层VLAN封装的静态加入配置两两互斥，不允许同时配置。

·配置不带VLAN封装的静态加入时，如果子接口上没有配置**igmp** **join-by-session**命令和**igmp** **user-vlan-aggregation** **dot1q**命令，才生成静态组播表项。

·配置带VLAN封装的静态加入时，如果子接口上配置了**igmp** **join-by-session**命令，那么当相应VLAN内的用户上线时才生成静态组播表项；如果子接口上配置了**igmp** **user-vlan-aggregation** **dot1q**命令，那么只有二者的VLAN封装相同，才生成静态组播表项。

【举例】

·路由应用：

\# 配置接口GigabitEthernet1/0/1静态加入组播组224.1.1.1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp static-group 224.1.1.1

\# 配置接口GigabitEthernet1/0/1静态加入组播源组（192.168.1.1，232.1.1.1）。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp static-group 232.1.1.1 source 192.168.1.1

\# 配置子接口GigabitEthernet1/0/1.1按会话记录用户加入的组播组，并静态加入组播组224.1.1.1：当第一层VLAN Tag为10、第二层VLAN Tag范围为10～20的用户上线时才生成静态组播表项。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 igmp join-by-session

Sysname-GigabitEthernet1/0/1.1 igmp static-group 224.1.1.1 dot1q vid 10 second-dot1q 10 to 20

·交换应用：

\# 配置接口Vlan-interface100静态加入组播组224.1.1.1。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp static-group 224.1.1.1

\# 配置接口Vlan-interface100静态加入组播源组（192.168.1.1，232.1.1.1）。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp static-group 232.1.1.1 source 192.168.1.1

**IGMP \-- IGMP配置命令 \-- igmp user-vlan-aggregation dot1q**

------------------------------------------------------------------------

![说明](IGMP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[igmp** **user-vlan-aggregation** **dot1q**]命令用来配置为组播报文封装的VLAN Tag。

**[undo** **igmp** **user-vlan-aggregation** **dot1q**]命令用来恢复缺省情况。

【命令】

**[igmp** **user-vlan-aggregation** **dot1q** **vid** *vlan-id* [ **second-dot1q** *vlan-id* ]]

**[undo** **igmp** **user-vlan-aggregation** **dot1q**]

【缺省情况】

不为组播报文封装VLAN Tag。

【视图】

三层以太网子接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vid** *vlan-id*]：指定封装的第一层VLAN Tag，*vlan-id*的取值范围为1～4094。

**[second-dot1q** *vlan-id*]：指定封装的第二层VLAN Tag，*vlan-id*的取值范围为1～4094。

【使用指导】

**[igmp** **join-by-session**]命令与**igmp** **user-vlan-aggregation** **dot1q**命令互斥，不允许同时配置。

【举例】

\# 在子接口GigabitEthernet1/0/1.1上配置为组播报文封装的第一层VLAN Tag为10，第二层VLAN Tag为20。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 igmp user-vlan-aggregation dot1q vid 10 second-dot1q 20

**IGMP \-- IGMP配置命令 \-- igmp version**

------------------------------------------------------------------------

**[igmp** **version**]命令用来在接口上配置IGMP的版本。

**[undo** **igmp** **version**]命令用来恢复缺省情况。

【命令】

**[igmp** **version** *version-number*]

**[undo** **igmp** **version**]

【缺省情况】

IGMP的版本为IGMPv2。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：表示IGMP的版本号，取值范围为1～3。

【举例】

·路由应用：

\# 指定接口GigabitEthernet1/0/1使用IGMPv1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp version 1

·交换应用：

\# 指定接口Vlan-interface100使用IGMPv1。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 igmp version 1

**IGMP \-- IGMP配置命令 \-- last-member-query-count (IGMP view)**

------------------------------------------------------------------------

**[last-member-query-count**]命令用来全局配置IGMP最后组成员查询次数。

**[undo last-member-query-count**]命令用来恢复缺省情况。

【命令】

**[last-member-query-count ***count*]

**[undo last-member-query-count**]

【缺省情况】

IGMP最后组成员查询次数等于IGMP查询器的健壮系数。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定IGMP最后组成员查询次数，取值范围为1～255。

【使用指导】

本命令与**igmp last-member-query-count**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP最后组成员查询次数为6次。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp last-member-query-count 6

【相关命令】

·**igmp last-member-query-count**

**IGMP \-- IGMP配置命令 \-- last-member-query-interval (IGMP view)**

------------------------------------------------------------------------

**[last-member-query-interval**]命令用来全局配置IGMP最后组成员查询间隔。

**[undo last-member-query-interval**]命令用来恢复缺省情况。

【命令】

**[last-member-query-interval*** interval*]

**[undo last-member-query-interval**]

【缺省情况】

IGMP最后组成员查询间隔为1秒。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP最后组成员查询间隔，取值范围为1～25，单位为秒。

【使用指导】

本命令与**igmp last-member-query-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP最后组成员查询间隔为6秒。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp last-member-query-interval 6

【相关命令】

·**igmp last-member-query-interval**

**IGMP \-- IGMP配置命令 \-- max-response-time (IGMP view)**

------------------------------------------------------------------------

**[max-response-time**]命令用来全局配置IGMP普遍组查询报文的最大响应时间。

**[undo max-response-time**]命令用来恢复缺省情况。

【命令】

**[max-response-time*** time*]

**[undo max-response-time**]

【缺省情况】

IGMP普遍组查询报文的最大响应时间为10秒。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定IGMP普遍组查询报文的最大响应时间，取值范围为1～3174，单位为秒。

【使用指导】

本命令与**igmp max-response-time**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP普遍组查询报文的最大响应时间为25秒。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp max-response-time 25

【相关命令】

·**igmp max-response-time**

**IGMP \-- IGMP配置命令 \-- other-querier-present-interval (IGMP view)**

------------------------------------------------------------------------

**[other-querier-present-interval**]命令用来全局配置IGMP其它查询器的存在时间。

**[undo other-querier-present-interval**]命令用来恢复缺省情况。

【命令】

**[other-querier-present-interval*** interval*]

**[undo other-querier-present-interval**]

【缺省情况】

IGMP其它查询器的存在时间＝IGMP普遍组查询报文的发送间隔×IGMP查询器的健壮系数＋IGMP普遍组查询的最大响应时间÷2。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP其它查询器的存在时间，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**igmp** **other-querier-present-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP其它查询器的存在时间为125秒。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp other-querier-present-interval 125

【相关命令】

·**igmp****other-querier-present-interval**

**IGMP \-- IGMP配置命令 \-- proxy multipath (IGMP view)**

------------------------------------------------------------------------

**[proxy** **multipath**]命令用来使能IGMP代理的负载分担功能。

**[undo** **proxy** **multipath**]命令用来关闭IGMP代理的负载分担功能。

【命令】

**[proxy** **multipath**]

**[undo** **proxy** **multipath**]

【缺省情况】

IGMP代理的负载分担功能处于关闭状态。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当在IGMP代理设备的多个接口上使能了IGMP代理功能时：

·如果关闭了IGMP代理的负载分担功能，则只有IP地址最大的接口会转发组播流量。

·如果使能了IGMP代理的负载分担功能，则可通过这些接口对组播流量按组进行负载分担。

【举例】

\# 在公网实例中使能IGMP代理的负载分担功能。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp proxy multipath

**IGMP \-- IGMP配置命令 \-- query-interval (IGMP view)**

------------------------------------------------------------------------

**[query-interval**]命令用来全局配置IGMP普遍组查询报文的发送间隔。

**[undo query-interval**]命令用来恢复缺省情况。

【命令】

**[query-interval ***interval*]

**[undo query-interval**]

【缺省情况】

IGMP普遍组查询报文的发送间隔为125秒。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP普遍组查询报文的发送间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**igmp** **query-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP普遍组查询报文的时间间隔为60秒。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp query-interval 60

【相关命令】

·**igmp****query-interval**

**IGMP \-- IGMP配置命令 \-- reset igmp group**

------------------------------------------------------------------------

**[reset** **igmp** **group**]命令用来清除IGMP组播组的动态加入记录。

【命令】

**[reset** **igmp** [ **vpn-instance** *vpn-instance-name*  **group** { **all** \| **interface** *interface-type interface-number* { **all** \| *group-address* [ **mask** { *mask* \| *mask-length* }   *source-address* [ **mask** { *mask* \| *mask-length* } ] ] } }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的记录，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的记录。

**[all**]：前一个**all**表示清除所有接口上的记录，后一个**all**表示清除所有组播组的记录。

*[interface-type interface-number*]：清除指定接口上的记录。

*[group-address*]：清除指定组播组的记录，取值范围为224.0.0.0～239.255.255.255。

*[source-address*]：清除指定组播源的记录。如果未指定本参数，将清除所有组播源的记录。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为4～32，缺省值为32；对于组播源地址，其取值范围为0～32，缺省值为32。

【使用指导】

执行本命令可能导致接收者中断组播信息的接收。

【举例】

·路由应用：

\# 清除公网实例所有接口上IGMP组播组的动态加入记录。

\<Sysname\> reset igmp group all

\# 清除公网实例接口GigabitEthernet1/0/1上所有IGMP组播组的动态加入记录。

\<Sysname\> reset igmp group interface gigabitethernet 1/0/1 all

\# 清除公网实例接口GigabitEthernet1/0/1上IGMP组播组225.0.0.1的动态加入记录。

\<Sysname\> reset igmp group interface gigabitethernet 1/0/1 225.0.0.1

·交换应用：

\# 清除公网实例所有接口上IGMP组播组的动态加入记录。

\<Sysname\> reset igmp group all

\# 清除公网实例接口Vlan-interface100上所有IGMP组播组的动态加入记录。

\<Sysname\> reset igmp group interface vlan-interface 100 all

\# 清除公网实例接口Vlan-interface100上IGMP组播组225.0.0.1的动态加入记录。

\<Sysname\> reset igmp group interface vlan-interface 100 225.0.0.1

【相关命令】

·**display** **igmp** **group**

**IGMP \-- IGMP配置命令 \-- robust-count (IGMP view)**

------------------------------------------------------------------------

**[robust-count**]命令用来全局配置IGMP查询器的健壮系数。

**[undo robust-count**]命令用来恢复缺省情况。

【命令】

**[robust-count*** count*]

**[undo robust-count**]

【缺省情况】

IGMP查询器的健壮系数为2。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定IGMP查询器的健壮系数，取值范围为1～255。

【使用指导】

·IGMP查询器的健壮系数是为了弥补可能发生的网络丢包而设置的报文重传次数，健壮系数越大，IGMP查询器就越"健壮"，但是组播组超时所需的时间也就越长。

·本命令与**igmp robust-count**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP查询器的健壮系数为5。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp robust-count 5

【相关命令】

·**igmp robust-count**

**IGMP \-- IGMP配置命令 \-- ssm-mapping (IGMP view)**

------------------------------------------------------------------------

**[ssm-mapping**]命令用来配置IGMP SSM Mapping规则。

**[undo** **ssm-mapping**]命令用来删除IGMP SSM Mapping规则。

【命令】

**[ssm-mapping** *source-address* *acl-number*]

**[undo ssm-mapping**[ { *source-address* \| **all** }]]

【缺省情况】

未配置IGMP SSM Mapping规则。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-address*]：指定组播源地址。

*[acl-number*]：指定IPv4基本ACL的编号，取值范围为2000～2999。通过该ACL规则中的**permit**语句指定组播组的范围。当指定的ACL不存在或ACL中未配置有效规则，则表示未指定任何组播组。

**[all**]：删除所有的IGMP SSM Mapping规则。

【使用指导】

ACL规则中的**source**参数用来指定组播组的范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

\# 在公网实例中添加如下一条IGMP SSM Mapping规则：组地址范围为232.1.1.0/24，对应的源地址为125.1.1.1。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 232.1.1.1 0.0.0.255

Sysname-acl-ipv4-basic-2001 quit

Sysname igmp

Sysname-igmp ssm-mapping 125.1.1.1 2001

【相关命令】

·**display ****igmp ssm-mapping**

**IGMP \-- IGMP配置命令 \-- startup-query-count (IGMP view)**

------------------------------------------------------------------------

**[startup-query-count**]命令用来全局配置IGMP查询器的启动查询次数。

**[undo startup-query-count**]命令用来恢复缺省情况。

【命令】

**[startup-query-count*** count*]

**[undo startup-query-count**]

【缺省情况】

IGMP查询器的启动查询次数等于IGMP查询器的健壮系数。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：指定IGMP查询器的启动查询次数，取值范围为1～255。

【使用指导】

本命令与**igmp startup-query-count**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP查询器的启动查询次数为5次。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp startup-query-count 5

【相关命令】

·**igmp startup-query-count**

**IGMP \-- IGMP配置命令 \-- startup-query-interval (IGMP view)**

------------------------------------------------------------------------

**[startup-query-interval**]命令用来全局配置IGMP查询器的启动查询间隔。

**[undo startup-query-interval**]命令用来恢复缺省情况。

【命令】

**[startup-query-interval*** interval*]

**[undo startup-query-interval**]

【缺省情况】

IGMP查询器的启动查询间隔为IGMP普遍组查询报文发送间隔的1/4。

【视图】

IGMP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定IGMP查询器的启动查询间隔，取值范围为1～31744，单位为秒。

【使用指导】

本命令与**igmp** **startup-query-interval**命令的功能相同，只是作用范围不同：IGMP视图下的全局配置对所有接口都有效，接口视图下的配置只对当前接口有效，后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IGMP查询器的启动查询间隔为100秒。

\<Sysname\> system-view

Sysname igmp

Sysname-igmp startup-query-interval 100

【相关命令】

·**igmp****startup-query-interval**

