<!-- CMD-INDEX
  bandwidth                           | 二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图 | L36
  default                             | 二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图 | L92
  description                         | 二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图 | L128
  display interface                   | 任意视图             | L170
  display lacp system-id              | 任意视图             | L530
  display link-aggregation load-sharing mode | 任意视图             | L580
  display link-aggregation member-port | 任意视图             | L716
  display link-aggregation summary    | 任意视图             | L882
  display link-aggregation verbose    | 任意视图             | L998
  interface bridge-aggregation        | 系统视图             | L1206
  interface route-aggregation         | 系统视图             | L1254
  lacp edge-port                      | 二层聚合接口视图/三层聚合接口视图 | L1318
  lacp mode                           | 二层以太网接口视图/三层以太网接口视图 | L1366
  lacp period short                   | 二层以太网接口视图/三层以太网接口视图 | L1410
  lacp system-priority                | 系统视图             | L1452
  link-aggregation global load-sharing mode | 系统视图             | L1496
  link-aggregation ignore vlan        | 二层聚合接口视图         | L1576
  link-aggregation irf-enhanced       | 系统视图             | L1622
  link-aggregation lacp traffic-redirect-notification enable | 系统视图             | L1676
  link-aggregation load-sharing mode  | 二层聚合接口视图/三层聚合接口视图 | L1734
  link-aggregation load-sharing mode local-first | 系统视图             | L1820
  link-aggregation mode               | 二层聚合接口视图/三层聚合接口视图 | L1864
  link-aggregation port-priority      | 二层以太网接口视图/三层以太网接口视图 | L1902
  link-aggregation selected-port maximum | 二层聚合接口视图/三层聚合接口视图 | L1956
  link-aggregation selected-port minimum | 二层聚合接口视图/三层聚合接口视图 | L2018
  mac-address                         | 二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图 | L2074
  mtu                                 | 三层聚合接口视图/三层聚合子接口视图 | L2122
  port link-aggregation group         | 二层以太网接口视图/三层以太网接口视图 | L2172
  reset counters interface            | 用户视图             | L2230
  reset lacp statistics               | 用户视图             | L2276
  service                             |                  | L2310
  shutdown                            | 二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图 | L2382
-->

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- bandwidth**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[bandwidth**]命令用来配置当前接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会对下列内容有影响：

·CBQ队列带宽。具体介绍请参见"ACL和QoS配置指导"中的"拥塞管理"。

·链路开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置二层聚合接口1的期望带宽为10000kbit/s。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 bandwidth 10000

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前聚合接口的缺省配置。

【命令】

**[default**]

【视图】

二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·接口下的某些配置取消后，会对现有功能产生影响，建议您在执行该命令前，完全了解其对网络产生的影响。

·您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将二层聚合接口1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 default

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，比如接口Bridge-Aggregation1的缺省描述信息为：Bridge-Aggregation1 Interface。

【视图】

二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示接口的描述信息，为1～255个字符的字符串。

【举例】

\# 配置二层聚合接口1的描述信息为"connect to the lab"。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 description connect to the lab

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- display interface**

------------------------------------------------------------------------

**[display interface**]命令用来显示聚合接口的相关信息。

【命令】

**[display interface**[ [ { **bridge-aggregation** \| **route-aggregation** } [ *interface-number* ]   **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[bridge-aggregation**]：显示二层聚合接口的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[route-aggregation**]：显示三层聚合接口的相关信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-number*]：显示指定聚合接口的相关信息，*interface-number*表示聚合接口的编号，取值范围为已创建的聚合接口的编号。

**[brief**]：显示接口的概要信息。如果未指定该参数，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果未指定**bridge-aggregation**和**route-aggregation**参数，将显示设备支持的所有接口的相关信息。

·如果指定了**bridge-aggregation**或**route-aggregation**参数而未指定*interface-number*参数，将显示所有已创建的该类型聚合接口的相关信息。

·如果指定了**bridge-aggregation**或**route-aggregation**参数，同时指定了*interface-number*参数，将显示指定聚合接口的相关信息。

【举例】

\# 显示二层聚合接口1的详细信息。

\<Sysname\> display interface bridge-aggregation 1

Bridge-Aggregation1

Current state: UP

IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 000f-e207-f2e0

Description: Bridge-Aggregation1 Interface

Bandwidth: 1000kbps

2Gbps-speed mode, full-duplex mode

Link speed type is autonegotiation, link duplex type is autonegotiation

PVID: 1

Port link-type: access

 Tagged Vlan:   none

 UnTagged Vlan: 1

Last clearing of counters:  Never

Last 300 seconds input:  6900 packets/sec 885160 bytes/sec    0%

Last 300 seconds output:  3150 packets/sec 404430 bytes/sec    0%

Input (total):  5364747 packets, 686688416 bytes

         2682273 unicasts, 1341137 broadcasts, 1341337 multicasts, 0 pauses

Input (normal):  5364747 packets, 686688416 bytes

         2682273 unicasts, 1341137 broadcasts, 1341337 multicasts, 0 pauses

Input:  0 input errors, 0 runts, 0 giants, 0 throttles

         0 CRC, 0 frame, 0 overruns, - aborts

         - ignored, - parity errors

Output (total): 1042508 packets, 133441832 bytes

         1042306 unicasts, 0 broadcasts, 202 multicasts, - pauses

Output (normal): 1042508 packets, 133441832 bytes

         1042306 unicasts, 0 broadcasts, 202 multicasts, 0 pauses

Output: 0 output errors, - underruns, - buffer failures

         0 aborts, 0 deferred, 0 collisions, 0 late collisions

         - lost carrier, - no carrier

\# 显示三层聚合接口1的详细信息。

\<Sysname\> display interface route-aggregation 1

Route-Aggregation1

Current state: UP

Line protocol state: UP

Description: Route-Aggregation1 Interface

Bandwidth: 1000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0000-0000-0000

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0000-0000-0000

Last clearing of counters: Never

    Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

    Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

    0 packets input, 0 bytes, 0 drops

    0 packets output, 0 bytes, 0 drops

\# 显示二层聚合接口1的概要信息。

\<Sysname\> display interface bridge-aggregation 1 brief

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

BAGG1                UP   auto    A      A    1

\# 显示三层聚合接口1的概要信息。

\<Sysname\> display interface route-aggregation 1 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

RAGG1                UP   UP       \--

![说明](以太网链路聚合命令.files/image001.png)

本命令的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-1 display interface命令显示信息描述表

字段

描述

Bridge-Aggregation1

二层聚合接口名

Route-Aggregation1

三层聚合接口名

Current state

接口的状态：

·DOWN ( Administratively down)：表示该接口已被**shutdown**命令关闭，其管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但其物理状态为关闭（可能由于没有物理连线或线路故障）

·UP：表示该接口的管理状态和物理状态均为开启

IP Packet Frame Type

IPv4报文帧格式，取值为PKTFMT_ETHNT_2表示报文以Ethernet II型帧格式封装

IPv6 Packet Frame Type

IPv6报文帧格式

Hardware Address

接口的MAC地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Bandwidth

接口的期望带宽值，当该参数的取值为0时，不显示该参数

Unknown-speed mode, unknown-duplex mode

接口的速率和双工模式均未知

Link speed type is autonegotiation, link duplex type is autonegotiation

接口的速率和双工模式都是通过自协商确定的

PVID

接口缺省VLAN的编号

Port link-type

接口的链路类型，取值可能为access、trunk或hybrid

Tagged Vlan

通过该接口后携带Tag的VLAN

Untagged Vlan

通过该接口后不再携带Tag的VLAN

Last clearing of counters

最后一次使用**reset counters interface**命令清除接口统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Last 300 seconds input/output rate

接口在最近300秒接收/发送报文的平均速率

Input/Output (total)

接口接收/发送的全部报文的统计值

Input/Output (normal)

接口接收/发送的正常报文的统计值

Line protocol state

接口数据链路层协议状态

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing

对IP报文的处理能力，disabled表示尚未配置IP地址，不能处理IP报文。当接口下配置了IP地址之后，该字段将变为"Internet Address is"

Brief information on interface(s) under route mode

三层接口的概要信息

Brief information on interface(s) under bridge mode

二层接口的概要信息

Link: ADM - administratively down; Stby - standby

接口的物理连接状态：

·ADM：表示该接口已被管理员手工关闭，在该接口下执行**undo shutdown**命令才能恢复其物理状态

·Stby：表示该接口是一个备份接口

Speed or Duplex: (a)/A - auto; H - half; F - full

接口的速率和双工模式：

·(a)/A：表示速率和双工模式都是通过自协商确定的

·H：表示双工模式为半双工

·F：表示双工模式为全双工

Type: A - access; T - trunk; H - hybrid

接口的链路类型：

·A：表示Access类型

·H：表示Hybrid类型

·T：表示Trunk类型

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称的缩写

Link

接口物理连接状态，取值为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上是不通的

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Speed

接口的速率（单位为bps）

Duplex

接口的双工模式

Type

接口的链路类型

Protocol

接口数据链路层连通状态，取值为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口的主IP地址

Cause

接口物理连接状态为down的原因

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- display lacp system-id**

------------------------------------------------------------------------

**[display lacp system-id**]命令用来显示本端系统的设备ID。

【命令】

**[display lacp system-id**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

使用**lacp** **system-priority**命令可以改变系统的LACP优先级，但通过该命令输入的是十进制的优先级数值。而当使用**display lacp system-id**命令显示时，系统会自动将其转换为十六进制的优先级数值。

【举例】

\# 显示本端系统的设备ID。

\<Sysname\> display lacp system-id

Actor System ID: 0x8000, 0000-fc00-6504

表1-2 display lacp system-id命令显示信息描述表

字段

描述

Actor System ID: 0x8000, 0000-fc00-6504

本端系统的设备ID（由系统的LACP优先级和系统的MAC地址共同构成）：系统的LACP优先级为0x8000，系统的MAC地址为0000-FC00-6504

【相关命令】

·**lacp system-priority**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- display link-aggregation load-sharing mode**

------------------------------------------------------------------------

**[display link-aggregation load-sharing mode**]命令用来显示全局或聚合组内采用的聚合负载分担类型。

【命令】

**[display link-aggregation load-sharing mode**[ [ **interface** [ { **bridge-aggregation** \| **route-aggregation** } *interface-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[bridge-aggregation**]：显示二层聚合接口所对应聚合组内采用的聚合负载分担类型。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[route-aggregation**]：显示三层聚合接口所对应聚合组内采用的聚合负载分担类型。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-number*]：聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。必须是当前已经创建的聚合接口编号。

【使用指导】

·如果未指定参数**interface**，则显示全局采用的聚合负载分担类型。

·如果仅指定参数**interface**而未指定具体的聚合接口类型，则显示所有聚合接口所对应聚合组内采用的聚合负载分担类型。

·只有在设备上创建了二层或三层聚合接口之后，才能指定**bridge-aggregation**或**route-aggregation**参数。

【举例】

\# 显示全局采用的聚合负载分担类型（缺省情况）。

\<Sysname\> display link-aggregation load-sharing mode

Link-aggregation load-sharing mode:

Layer 2 traffic: packet type-based sharing

Layer 3 traffic: packet type-based sharing

\# 显示全局采用的聚合负载分担类型（非缺省情况）。

\<Sysname\> display link-aggregation load-sharing mode

Link-aggregation load-sharing mode:

destination-mac address, source-mac address

\# 显示二层聚合接口10所对应聚合组内采用的聚合负载分担类型（缺省情况）。

\<Sysname\> display link-aggregation load-sharing mode interface bridge-aggregation 10

Bridge-Aggregation10 load-sharing mode:

Layer 2 traffic: packet type-based sharing

Layer 3 traffic: packet type-based sharing

\# 显示二层聚合接口10所对应聚合组内采用的聚合负载分担类型（非缺省情况）。

\<Sysname\> display link-aggregation load-sharing mode interface bridge-aggregation 10

Bridge-Aggregation10 load-sharing mode:

destination-mac address, source-mac address

表1-3 display link-aggregation load-sharing mode命令显示信息描述表

字段

描述

Link-aggregation load-sharing mode

全局采用的聚合负载分担类型：

·缺省情况下显示：二层报文、三层报文、四层报文、MPLS报文采用的聚合负载分担类型（各设备支持的报文类型不同，请以设备的实际情况为准）

·非缺省情况下显示：用户配置后采用的聚合负载分担类型

Bridge-Aggregation10 load-sharing mode

二层聚合接口10所对应聚合组内采用的聚合负载分担类型：

·缺省情况下显示：全局采用的聚合负载分担类型

·非缺省情况下显示：用户配置后采用的聚合负载分担类型

Route-Aggregation10 load-sharing mode

三层聚合接口10所对应聚合组内采用的聚合负载分担类型：

·缺省情况下显示：全局采用的聚合负载分担类型

·非缺省情况下显示：用户配置后采用的聚合负载分担类型

Layer 2 traffic: destination-mac address, source-mac address

二层报文缺省采用的聚合负载分担类型：按照源MAC地址和目的MAC地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 2 traffic: packet type-based sharing

二层报文缺省采用的聚合负载分担类型：按照产品自定义方式进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 3 traffic: destination-ip address,  source-ip address

三层报文缺省采用的聚合负载分担类型：按照源IP地址和目的IP地址进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 3 traffic: packet type-based sharing

三层报文缺省采用的聚合负载分担类型：按照产品自定义方式进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

Layer 4 traffic: destination-port,        source-port

四层报文缺省采用的聚合负载分担类型：按照源服务端口和目的服务端口进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

MPLS traffic   : mpls-label1,             mpls-label2,                 mpls-label3

MPLS报文缺省采用的聚合负载分担类型：按照第1～3层的MPLS标签进行负载分担（此字段的显示内容与设备的型号有关，请以设备的实际情况为准）

destination-mac address, source-mac address

用户配置后采用的聚合负载分担类型：按照源MAC地址和目的MAC地址进行负载分担（此字段的显示内容与用户的配置相关）

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- display link-aggregation member-port**

------------------------------------------------------------------------

**[display link-aggregation member-port**]命令用来显示成员端口上链路聚合的详细信息。

【命令】

**[display link-aggregation member-port ** *interface-list* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-list*]：成员端口列表，表示一个或多个成员端口。表示方式为*interface-list *= *interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type*为接口类型，*interface-number*为接口编号。

【使用指导】

由于静态聚合组无法获知对端信息，因此静态聚合组只显示本端的端口编号、端口优先级和操作Key的值。

【举例】

\# 显示静态聚合组内成员端口GigabitEthernet1/0/1上链路聚合的详细信息。

\<Sysname\> display link-aggregation member-port gigabitethernet 1/0/1

Flags: A \-- LACP_Activity, B \-- LACP_Timeout, C \-- Aggregation,

       D \-- Synchronization, E \-- Collecting, F \-- Distributing,

       G \-- Defaulted, H \-- Expired

GigabitEthernet1/0/1:

Aggregate Interface: Bridge-Aggregation1

Port Number: 1

Port Priority: 32768

Oper-Key: 1

\# 显示动态聚合组内成员端口GigabitEthernet1/0/2上链路聚合的详细信息。

\<Sysname\> display link-aggregation member-port gigabitethernet 1/0/2

Flags: A \-- LACP_Activity, B \-- LACP_Timeout, C \-- Aggregation,

       D \-- Synchronization, E \-- Collecting, F \-- Distributing,

       G \-- Defaulted, H \-- Expired

GigabitEthernet1/0/2:

Aggregate Interface: Bridge-Aggregation10

Local:

    Port Number: 2

    Port Priority: 32768

    Oper-Key: 2

    Flag: {ACDEF}

Remote:

    System ID: 0x8000, 000f-e267-6c6a

    Port Number: 26

    Port Priority: 32768

    Oper-Key: 2

    Flag: {ACDEF}

Received LACP Packets: 5 packet(s)

Illegal: 0 packet(s)

Sent LACP Packets: 7 packet(s)

表1-4 display link-aggregation member-port命令显示信息描述表

字段

描述

Flags

LACP协议的状态标识，长度为1字节，该字节自低位至高位分别以英文字母A～H表示，某一位为1时打印出对应的英文字母，为0时不打印对应的英文字母。各标志位的含义如下：

·A：LACP是否使能标志。1表示使能；0表示未使能

·B：LACP长/短超时标志。1表示短超时；0表示长超时

·C：发送端认为本成员端口所在链路是否可聚合。1表示是；0表示否

·D：发送端认为本成员端口所在链路是否处于同步状态。1表示是；0表示否

·E：发送端认为本成员端口所在链路是否处于收集状态。1表示是；0表示否

·F：发送端认为本成员端口所在链路是否处于分发状态。1表示是；0表示否

·G：发送端的接收状态机是否处于默认状态。1表示是；0表示否

·H：发送端的接收状态机是否处于超时状态。1表示是；0表示否

Aggregate Interface

本成员端口所属的聚合接口

Local

本端信息

Port Number

端口的编号

Port Priority

端口优先级

Oper-key

操作Key的值

Flag

LACP协议的状态标志值

Remote

对端信息

System ID

设备ID（由系统的LACP优先级和系统的MAC地址共同构成）

Received LACP Packets

收到的LACP报文总数

Illegal

非法报文的总数

Sent LACP Packets

发出的LACP报文总数

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- display link-aggregation summary**

------------------------------------------------------------------------

**[display link-aggregation summary**]命令用来显示所有聚合组的摘要信息。

【命令】

**[display link-aggregation summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

由于静态聚合组无法获知对端信息，因此静态聚合组的对端信息无显示或显示为None，并不代表对端系统的实际信息。

【举例】

\# 显示所有聚合组的摘要信息。

\<Sysname\> display link-aggregation summary

Aggregate Interface Type:

BAGG \-- Bridge-Aggregation, RAGG \-- Route-Aggregation

Aggregation Mode: S \-- Static, D \-- Dynamic

Loadsharing Type: Shar \-- Loadsharing, NonS \-- Non-Loadsharing

Actor System ID: 0x8000, 000f-e267-6c6a

AGG        AGG   Partner ID              Selected  Unselected  Individual  Share

Interface  Mode                          Ports     Ports       Ports       Type

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RAGG10     S     None                    1         0           0           NonS

BAGG20     D     0x8000,00e0-fcff-ff01   2         0           0           Shar

表1-5 display link-aggregation summary命令显示信息描述表

字段

描述

Aggregate Interface Type

聚合接口类型：

·BAGG：表示二层聚合接口

·RAGG：表示三层聚合接口

Aggregation Mode

聚合组类型：

·S：表示静态聚合

·D：表示动态聚合

Loadsharing Type

负载分担类型：

·Shar：表示负载分担类型

·NonS：表示非负载分担类型

Actor System ID

本端的设备ID（由系统的LACP优先级和系统的MAC地址共同构成）

AGG Interface

聚合接口的类型和编号

AGG Mode

聚合组的类型

Partner ID

对端的设备ID（由系统的LACP优先级和系统的MAC地址共同构成）

Selected Ports

处于选中状态的成员端口数量

Unselected Ports

处于非选中状态的成员端口数量

Individual Ports

处于独立状态的成员端口数量

Share Type

负载分担类型

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- display link-aggregation verbose**

------------------------------------------------------------------------

**[display link-aggregation verbose**]命令用来显示已有聚合接口所对应聚合组的详细信息。

【命令】

**[display link-aggregation**[ **verbose** [ { **bridge-aggregation** \| **route-aggregation** } [ *interface-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[bridge-aggregation**]：显示二层聚合接口所对应聚合组的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[route-aggregation**]：显示三层聚合接口所对应聚合组的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-number*]：聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。必须是当前已经创建的聚合接口编号。

【使用指导】

·如果未指定聚合接口类型，则显示所有聚合接口所对应聚合组的详细信息。

·如果仅指定聚合接口类型而未指定具体的聚合接口编号，则显示所有该类型聚合接口所对应聚合组的详细信息。

·只有在设备上创建了二层或三层聚合接口之后，才能指定**bridge-aggregation**或**route-aggregation**参数。

【举例】

\# 二层聚合接口10所对应的聚合组是动态聚合组，显示该聚合组的详细信息。

\<Sysname\> display link-aggregation verbose bridge-aggregation 10

Loadsharing Type: Shar \-- Loadsharing, NonS \-- Non-Loadsharing

Port Status: S \-- Selected, U \-- Unselected, I \-- Individual

Flags:  A \-- LACP_Activity, B \-- LACP_Timeout, C \-- Aggregation,

        D \-- Synchronization, E \-- Collecting, F \-- Distributing,

        G \-- Defaulted, H \-- Expired

Aggregate Interface: Bridge-Aggregation10

Aggregation Mode: Dynamic

Loadsharing Type: Shar

System ID: 0x8000, 000f-e267-6c6a

Local:

  Port             Status  Priority Oper-Key  Flag

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  GE1/0/1          S       32768    2         {ACDEF}

  GE1/0/2          S       32768    2         {ACDEF}

  GE1/0/3          S       32768    2         {AG}

Remote:

  Actor            Partner Priority Oper-Key  SystemID               Flag

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  GE1/0/1          1       32768    2         0x8000, 000f-e267-57ad {ACDEF}

  GE1/0/2          2       32768    2         0x8000, 000f-e267-57ad {ACDEF}

  GE1/0/3          0       32768    0         0x8000, 0000-0000-0000 {DEF}

\# 二层聚合接口20所对应的聚合组是静态聚合组，显示该聚合组的详细信息。

\<Sysname\> display link-aggregation verbose bridge-aggregation 20

Loadsharing Type: Shar \-- Loadsharing, NonS \-- Non-Loadsharing

Port Status: S \-- Selected, U \-- Unselected, I \-- Individual

Flags:  A \-- LACP_Activity, B \-- LACP_Timeout, C \-- Aggregation,

        D \-- Synchronization, E \-- Collecting, F \-- Distributing,

        G \-- Defaulted, H \-- Expired

Aggregate Interface: Bridge-Aggregation20

Aggregation Mode: Static

Loadsharing Type: Shar

  Port             Status  Priority Oper-Key

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  GE1/0/1          U       32768    1

  GE1/0/2          U       32768    1

  GE1/0/3          U       32768    1

表1-6 display link-aggregation verbose命令显示信息描述表

字段

描述

Loadsharing Type

负载分担类型：

·Shar：表示负载分担类型

·NonS：表示非负载分担类型

Port Status

端口的选中/非选中/独立状态：

·Selected：表示处于选中状态

·Unselected：表示处于非选中状态

·Individual：表示处于独立状态

Flags

LACP协议的状态标志，长度为1字节，该字节自低位至高位分别以英文字母A～H表示，某一位为1时打印出对应的英文字母，为0时不打印对应的英文字母。各标志位的含义如下：

·A：LACP是否使能标志。1表示使能；0表示未使能

·B：LACP长/短超时标志。1表示短超时；0表示长超时

·C：发送端认为本成员端口所在链路是否可聚合。1表示是；0表示否

·D：发送端认为本成员端口所在链路是否处于同步状态。1表示是；0表示否

·E：发送端认为本成员端口所在链路是否处于收集状态。1表示是；0表示否

·F：发送端认为本成员端口所在链路是否处于分发状态。1表示是；0表示否

·G：发送端的接收状态机是否处于默认状态。1表示是；0表示否

·H：发送端的接收状态机是否处于超时状态。1表示是；0表示否

Aggregate Interface

聚合接口的名称

Aggregation Mode

聚合组的工作模式：

·Static：表示静态聚合

·Dynamic：表示动态聚合

System ID

设备ID（由系统的LACP优先级和系统的MAC地址共同构成）

Local

本端信息（静态聚合组只显示本端信息，显示信息中不包括Flag字段）：

·Port：端口的类型和编号

·Status：端口的选中/非选中状态

·Priority：端口优先级

·Oper-Key：操作Key的值

·Flag：LACP协议的状态标志值

Remote

对端信息：

·Actor：本端的端口类型和编号

·Partner：对端端口的端口索引

·Priority：对端端口的端口优先级

·Oper-Key：对端端口的操作Key的值

·System ID：对端的设备ID

·Flag：对端的LACP协议的状态标志值

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- interface bridge-aggregation**

------------------------------------------------------------------------

**[interface bridge-aggregation**]命令用来创建二层聚合接口，并进入二层聚合接口视图。

**[undo interface bridge-aggregation**]命令用来删除二层聚合接口。

【命令】

**[interface bridge-aggregation ***interface-number*]

**[undo interface bridge-aggregation ***interface-number*]

【缺省情况】

未创建任何二层聚合接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：指定二层聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·创建二层聚合接口后，系统将自动生成同编号的二层聚合组，且该聚合组缺省工作在静态聚合模式下。

·删除二层聚合接口的同时会删除其对应的二层聚合组，如果该聚合组内有成员端口，那么这些成员端口将自动从该聚合组中退出。

【举例】

\# 创建二层聚合接口1，并进入二层聚合接口1的视图。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- interface route-aggregation**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[interface route-aggregation**]命令用来创建三层聚合接口/子接口，并进入三层聚合接口/子接口视图。

**[undo interface route-aggregation**]命令用来删除三层聚合接口/子接口。

【命令】

**[interface route-aggregation **[{ *interface-number* \| *interface-number.subnumber* }]]

**[undo interface route-aggregation **[{ *interface-number* \| *interface-number.subnumber* }]]

【缺省情况】

未创建任何三层聚合接口/子接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：指定三层聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[interface-number.subnumber*]：指定三层聚合子接口。其中*interface-number*为主接口编号；*subnumber*为子接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·创建三层聚合接口后，系统将自动生成同编号的三层聚合组，且该聚合组缺省工作在静态聚合模式下。

·删除三层聚合接口的同时会删除其对应的三层聚合组以及该接口下的所有聚合子接口，如果该聚合组内有成员端口，那么这些成员端口将自动从该聚合组中退出。

·如果删除三层聚合子接口，则不会影响其主接口以及主接口对应的聚合组状态。

【举例】

\# 创建三层聚合接口1，并进入三层聚合接口1的视图。

\<Sysname\> system-view

Sysname interface route-aggregation 1

Sysname-Route-Aggregation1

\# 创建三层聚合子接口1.1，并进入三层聚合子接口1.1的视图。

\<Sysname\> system-view

Sysname interface route-aggregation 1.1

Sysname-Route-Aggregation1.1

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- lacp edge-port**

------------------------------------------------------------------------

**[lacp edge-port**]命令用来配置聚合接口为聚合边缘接口。

**[undo lacp edge-port**]命令用来恢复缺省情况。

【命令】

**[lacp edge-port**]

**[undo lacp edge-port**]

【缺省情况】

聚合接口不为聚合边缘接口。

【视图】

二层聚合接口视图/三层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令主要用于在网络设备与服务器等终端设备相连的场景中，当网络设备配置了动态聚合模式，而终端设备未配置动态聚合模式时，网络设备的聚合成员端口都可以作为普通物理口转发报文，从而保证终端设备与网络设备间的多条链路可以相互备份，增加可靠性。

需要注意的是：

·该配置仅在聚合接口对应的聚合组为动态聚合组时生效。

·当聚合接口配置为聚合边缘接口后，聚合流量重定向功能将不能正常使用。

【举例】

\# 配置二层聚合接口1为聚合边缘接口。

\<Sysname\> System-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 lacp edge-port

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- lacp mode**

------------------------------------------------------------------------

**[lacp mode passive**]命令用来配置当前端口的LACP工作模式为PASSIVE。

**[undo lacp mode**]命令用来恢复缺省情况。

【命令】

**[lacp mode passive**]

**[undo lacp mode**]

【缺省情况】

端口的LACP工作模式为ACTIVE。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·{.ItemListCharChar}如果动态聚合组内成员端口的LACP工作模式为PASSIVE，且对端的LACP工作模式也为PASSIVE时，两端将不能发送LACPDU。如果两端中任何一端的LACP工作模式为ACTIVE时，两端将可以发送LACPDU。

·{.ItemListCharChar}执行本命令后，只有在当前端口为动态聚合组成员端口时，配置才生效。

【举例】

\# 配置端口GigabitEthernet1/0/1的LACP工作模式为PASSIVE。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lacp mode passive

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- lacp period short**

------------------------------------------------------------------------

**[lacp period short**]命令用来配置当前端口的LACP超时时间为短超时（3秒），并使对端快速发送LACPDU。

**[undo lacp period**]命令用来恢复缺省情况。

【命令】

**[lacp period short**]

**[undo lacp period**]

【缺省情况】

端口的LACP超时时间为长超时（90秒），对端慢速发送LACPDU。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

请不要在ISSU升级前配置LACP超时时间为短超时，否则在ISSU升级期间会出现网络流量中断，导致流量转发不通。有关ISSU升级的详细介绍请参见"基础配置指导"中的"ISSU配置"。

【举例】

\# 配置端口GigabitEthernet1/0/1的LACP超时时间为短超时（3秒），并使对端快速发送LACPDU。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lacp period short

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- lacp system-priority**

------------------------------------------------------------------------

**[lacp** **system-priority**]命令用来配置系统的LACP优先级。

**[undo** **lacp** **system-priority**]命令用来恢复缺省情况。

【命令】

**[lacp** **system-priority** *system-priority*]

**[undo** **lacp** **system-priority**]

【缺省情况】

系统的LACP优先级为32768。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[system-priority*]：系统的LACP优先级，取值范围为0～65535。该数值越小，优先级越高。

【举例】

\# 配置系统的LACP优先级为64。

\<Sysname\> system-view

Sysname lacp system-priority 64

【相关命令】

·**link-aggregation** **port-priority**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation global load-sharing mode**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-aggregation global load-sharing mode**]命令用来配置全局采用的聚合负载分担类型。

**[undo link-aggregation global load-sharing mode**]命令用来恢复缺省情况。

【命令】

**[link-aggregation global load-sharing mode**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-ip** \| **source-mac** \| **source-port** \| **vlan-id** } \* \| **flexible** \| **per-packet** }]]

**[undo link-aggregation global load-sharing mode**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination-ip**]：表示按报文的目的IP地址进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-mac**]：表示按报文的目的MAC地址进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[destination-port**]：表示按报文的目的服务端口进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ingress-port**]：表示按报文的入端口进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip-protocol**]：表示按报文的IP协议类型进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label1**]：表示按MPLS报文第一层标签进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label2**]：表示按MPLS报文第二层标签进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-label3**]：表示按MPLS报文第三层标签进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-ip**]：表示按报文的源IP地址进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-mac**]：表示按报文的源MAC地址进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[source-port**]：表示按报文的源服务端口进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan-id**]：表示按报文所属的VLAN进行聚合负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flexible**]：表示按报文类型（如二层协议报文、IPv4报文、IPv6报文、MPLS报文等）自动选择聚合负载分担的类型。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[per-packet**]：表示对每个报文逐包进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

【使用指导】

·如果多次执行本命令，新配置将覆盖原有配置。

·对于设备不支持的聚合负载分担类型，系统将提示用户不支持。

【举例】

\# 配置全局按照报文目的MAC地址进行聚合负载分担。

\<Sysname\> system-view

Sysname link-aggregation global load-sharing mode destination-mac

【相关命令】

·**link-aggregation load-sharing mode**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation ignore vlan**

------------------------------------------------------------------------

**[link-aggregation ignore vlan**]命令用来配置二层聚合接口的忽略VLAN。

**[undo link-aggregation ignore vlan**]命令用来恢复缺省情况。

【命令】

**[link-aggregation ignore vlan ***vlan-id-list*]

**[undo link-aggregation ignore vlan** *vlan-id-list*]

【缺省情况】

二层聚合接口未配置忽略VLAN。

【视图】

二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：忽略VLAN列表。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

【使用指导】

通过本命令配置二层聚合接口的忽略VLAN后，二层聚合接口在确定其成员端口的选中状态时忽略这些VLAN允许通过的配置（包括是否允许VLAN通过，以及通过的方式），也就是说即使二层聚合接口及其成员端口关于这些VLAN的允许通过的配置不一致，也不影响成员端口的选中状态。

【举例】

\# 在二层聚合接口 1上配置忽略VLAN 50，这时该聚合接口在确定其成员端口的选中状态时，不考虑VLAN 50允许通过的配置是否一致。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 link-aggregation ignore vlan 50

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation irf-enhanced**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-aggregation** **irf-enhanced**]命令用来使能IRF模式下聚合选中能力增强功能。

**[undo** **link-aggregation** **irf-enhanced**]命令用来恢复缺省情况。

【命令】

**[link-aggregation** **irf-enhanced**]

**[undo** **link-aggregation** **irf-enhanced**]

【缺省情况】

IRF模式下聚合选中能力增强功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·设备只有在IRF模式下，才可以配置该命令。

·聚合组中的最大选中端口数为其聚合选中能力及**link-aggregation selected-port maximum**命令配置值中的较小值。

·设备配置本功能后，建议用户同时在对端设备上也配置本功能，否则当本端单个成员设备聚合组中可选中的端口数大于成员设备的聚合选中能力时，聚合功能可能无法正常使用。最终生效的聚合选中能力为本端和对端的聚合选中能力较小者。

·建议用户不要在设备上同时配置该命令和两端口间的冗余备份功能，配置该命令后，两端口间的冗余备份功能无法正常使用。

·设备配置该命令后，每个成员设备的聚合选中能力不变，但整个IRF的聚合选中能力则成倍增长（IRF的聚合选中能力=成员设备的聚合选中能力×成员设备个数）。

·设备若取消该命令配置，整个IRF的聚合选中能力则为成员设备的聚合选中能力。

【举例】

\# 使能IRF模式下聚合选中能力增强功能。

\<Sysname\> system-view

Sysname link-aggregation irf-enhanced

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation lacp traffic-redirect-notification enable**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-aggregation lacp traffic-redirect-notification enable**]命令用来使能聚合流量重定向功能。

**[undo link-aggregation lacp traffic-redirect-notification enable**]命令用来关闭聚合流量重定向功能。

【命令】

**[link-aggregation lacp traffic-redirect-notification enable**]

**[undo link-aggregation lacp traffic-redirect-notification enable**]

【缺省情况】

聚合流量重定向功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在使能了聚合流量重定向功能后，当关闭聚合组内某选中端口时，系统可以将该端口上的流量重定向到其他选中端口上，从而实现聚合链路上流量的不中断。其中，已知单播报文可以实现零丢包，非已知单播报文不保证不丢包。（集中式设备）

·在使能了聚合流量重定向功能后，当重启设备上某块有聚合组选中端口的单板时，系统可以将该单板上的流量重定向到其他单板上，从而实现聚合链路上流量的不中断。其中，已知单播报文可以实现零丢包，非已知单播报文不保证不丢包。（分布式设备－独立运行模式）

·在使能了聚合流量重定向功能后，当重启IRF中某台有聚合组选中端口的成员设备时，系统可以将该设备上的流量重定向到其他成员设备上，从而实现聚合链路上流量的不中断。其中，已知单播报文可以实现零丢包，非已知单播报文不保证不丢包。（集中式IRF设备）

·在使能了聚合流量重定向功能后，当重启IRF中某台有聚合组选中端口的成员设备或成员设备上某块有聚合组选中端口的单板时，系统可以将该设备或单板上的流量重定向到其他成员设备或单板上，从而实现聚合链路上流量的不中断。其中，已知单播报文可以实现零丢包，非已知单播报文不保证不丢包。（分布式设备－IRF模式）

·只有动态聚合组支持聚合流量重定向功能。

·必须在聚合链路两端都使能聚合流量重定向功能才能实现聚合链路上流量的不中断。

·如果同时使能聚合流量重定向功能和生成树功能，在重启单板/设备时会出现少量的丢包，因此不建议同时使能上述两个功能。

·当聚合接口配置为聚合边缘接口后，聚合流量重定向功能将不能正常使用。

【举例】

\# 使能聚合流量重定向功能。

\<Sysname\> system-view

Sysname link-aggregation lacp traffic-redirect-notification enable

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation load-sharing mode**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-aggregation load-sharing mode**]命令用来配置聚合组内采用的聚合负载分担类型。

**[undo link-aggregation load-sharing mode**]命令用来恢复缺省情况。

【命令】

**[link-aggregation load-sharing mode**[ { { **destination-ip** \| **destination-mac** \| **destination-port** \| **ingress-port** \| **ip-protocol** \| **mpls-label1** \| **mpls-label2** \| **mpls-label3** \| **source-ip** \| **source-mac** \| **source-port** \| **vlan-id** } \* \| **flexible** \| **per-packet** }]]

**[undo link-aggregation load-sharing mode**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

二层聚合接口视图/三层聚合接口视图

![说明](以太网链路聚合命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[destination-ip**]：表示按报文的目的IP地址进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[destination-mac**]：表示按报文的目的MAC地址进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[destination-port**]：表示按报文的目的服务端口进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[ingress-port**]：表示按报文的入端口进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[ip-protocol**]：表示按报文的IP协议类型进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[mpls-label1**]：表示按MPLS报文第一层标签进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[mpls-label2**]：表示按MPLS报文第二层标签进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[mpls-label3**]：表示按MPLS报文第三层标签进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[source-ip**]：表示按报文的源IP地址进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[source-mac**]：表示按报文的源MAC地址进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[source-port**]：表示按报文的源服务端口进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[vlan-id**]：表示按报文所属的VLAN进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[flexible**]：表示按报文类型（如二层协议报文、IPv4报文、IPv6报文、MPLS报文等）自动选择聚合负载分担的类型。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

**[per-packet**]：表示对每个报文逐包进行聚合负载分担。本参数的支持情况与设备的型号和当前的视图有关，请以设备的实际情况为准。

【使用指导】

·如果多次执行本命令，新的配置将覆盖旧的配置。

·对于设备不支持的聚合负载分担类型，系统将提示用户不支持。

【举例】

\# 配置二层聚合接口1对应的聚合组内按照报文目的MAC地址进行聚合负载分担。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 link-aggregation load-sharing mode destination-mac

【相关命令】

·**link-aggregation ****global load-sharing mode**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation load-sharing mode local-first**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-aggregation load-sharing mode** **local-first**]命令用来配置聚合负载分担采用本地转发优先。

**[undo link-aggregation load-sharing mode** **local-first**]命令用来取消聚合负载分担采用本地转发优先。

【命令】

**[link-aggregation load-sharing mode** **local-first**]

**[undo link-aggregation load-sharing mode local-first**]

【缺省情况】

聚合负载分担采用本地转发优先。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

取消聚合负载分担采用本地转发优先后，从聚合接口转发的报文将在IRF所有成员设备的所有选中端口间进行负载分担。

【举例】

\# 取消聚合负载分担采用本地转发优先。

\<Sysname\> system-view

Sysname undo link-aggregation load-sharing mode local-first

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation mode**

------------------------------------------------------------------------

**[link-aggregation mode dynamic**]命令用来配置聚合组工作在动态聚合模式下，同时使能了LACP协议。

**[undo link-aggregation mode**]命令用来恢复缺省情况。

【命令】

**[link-aggregation mode dynamic**]

**[undo link-aggregation mode**]

【缺省情况】

聚合组工作在静态聚合模式下。

【视图】

二层聚合接口视图/三层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置二层聚合接口1对应的聚合组工作在动态聚合模式下。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 link-aggregation mode dynamic

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation port-priority**

------------------------------------------------------------------------

**[link-aggregation** **port-priority**]命令用来配置端口优先级。

**[undo** **link-aggregation** **port-priority**]命令用来恢复缺省情况。

【命令】

**[link-aggregation** **port-priority** *port-priority*]

**[undo** **link-aggregation** **port-priority**]

【缺省情况】

端口优先级为32768。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-priority*]：端口优先级，取值范围为0～65535。该数值越小，优先级越高。

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1的端口优先级为64。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 link-aggregation port-priority 64

\# 配置三层以太网接口GigabitEthernet1/0/2的端口优先级为64。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 link-aggregation port-priority 64

【相关命令】

·**lacp** **system-priority**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation selected-port maximum**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-aggregation selected-port maximum**]命令用来配置聚合组中的最大选中端口数。

**[undo link-aggregation selected-port maximum**]命令用来恢复缺省情况。

【命令】

**[link-aggregation selected-port maximum ***number*]

**[undo link-aggregation selected-port maximum**]

【缺省情况】

聚合组中的最大选中端口数仅受设备硬件能力的限制。

【视图】

二层聚合接口视图/三层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：聚合组中的最大选中端口数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·执行本命令可能导致聚合组内部分成员端口变为非选中状态。

·本端和对端配置的聚合组中的最大选中端口数必须一致。

·当配置了聚合组中的最大选中端口数之后，最大选中端口数将同时受配置值和设备硬件能力的限制，即取二者的较小值作为限制值。用户借此可实现两端口间的冗余备份：在一个聚合组中只添加两个成员端口，并配置该聚合组中的最大选中端口数为1，这样这两个成员端口在同一时刻就只能有一个成为选中端口，而另一个将作为备份端口。

·对于IRF，当配置的聚合组中的最大选中端口数大于设备硬件能力时，可通过使能IRF模式下聚合选中能力增强功能，成倍提高IRF的设备硬件能力，相关配置请参见**link-aggregation** **irf-enhanced**命令。

【举例】

\# 配置二层聚合接口1对应的聚合组中的最大选中端口数为5。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 link-aggregation selected-port maximum 5

【相关命令】

·**link-aggregation** **irf-enhanced**

·**link-aggregation selected-port minimum**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- link-aggregation selected-port minimum**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-aggregation selected-port minimum**]命令用来配置聚合组中的最小选中端口数。

**[undo link-aggregation selected-port minimum**]命令用来恢复缺省情况。

【命令】

**[link-aggregation selected-port minimum ***number*]

**[undo link-aggregation selected-port minimum**]

【缺省情况】

聚合组中的最小选中端口数不受限制。

【视图】

二层聚合接口视图/三层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：聚合组中的最小选中端口数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·执行本命令可能导致聚合组内所有成员端口都变为非选中状态。

·本端和对端配置的聚合组中的最小选中端口数必须一致。

【举例】

\# 配置二层聚合接口1对应的聚合组中的最小选中端口数为3。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 link-aggregation selected-port minimum 3

【相关命令】

·**link-aggregation selected-port maximum**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- mac-address**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

本命令的视图支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address**]命令用来配置聚合接口的MAC地址。

**[undo mac-address**]命令用来恢复缺省情况。

【命令】

**[mac-address** *mac-address*]

**[undo mac-address**]

【缺省情况】

同一设备上所有聚合接口的MAC地址都相同，不同设备上聚合接口的MAC地址不同，具体的MAC地址请以设备实际情况为准。

【视图】

二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：MAC地址，形式为H-H-H。

【举例】

\# 配置二层聚合接口1的MAC地址为0001-0001-0001。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 mac-address 1-1-1

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- mtu**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mtu**]命令用来配置三层聚合接口/子接口的MTU值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

三层聚合接口/子接口的MTU值为1500字节。

【视图】

三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：表示接口允许通过的MTU（Maximum Transmission Unit，最大传输单元）值的大小，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置三层聚合接口1的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface route-aggregation 1

Sysname-Route-Aggregation1 mtu 1430

【相关命令】

·**display interface**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- port link-aggregation group**

------------------------------------------------------------------------

**[port link-aggregation group**]命令用来将以太网接口加入指定的聚合组。

**[undo port link-aggregation group**]命令用来将以太网接口从已加入的聚合组中删除。

【命令】

**[port link-aggregation group ***number*]

**[undo port link-aggregation group**]

【缺省情况】

以太网接口未加入任何聚合组。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：指定聚合组所对应聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·二层以太网接口只能加入二层聚合组，三层以太网接口只能加入三层聚合组。

·一个以太网接口只能加入一个聚合组。

·以太网冗余接口的成员接口和冗余组节点的成员接口不能再加入聚合组。有关以太网冗余接口和冗余组节点的详细介绍，请参见"可靠性配置指导"中的"冗余备份"。

【举例】

\# 将二层以太网接口GigabitEthernet1/0/1加入二层聚合组1中。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-aggregation group 1

\# 将三层以太网接口GigabitEthernet1/0/2加入三层聚合组2中。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port link-aggregation group 2

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除聚合接口上的统计信息。

【命令】

**[reset counters interface**[ [ { **bridge-aggregation** \| **route-aggregation** } [ *interface-number* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bridge-aggregation**]：清除二层聚合接口上的统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[route-aggregation**]：清除三层聚合接口上的统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-number*]：聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。若未指定该参数，将清除所有该类型聚合接口上的统计信息。

【使用指导】

·在某些情况下，需要统计一定时间内某二层聚合接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。

·如果未指定**bridge-aggregation**和**route-aggregation**参数以及*interface-number*参数，将清除所有接口上的统计信息。

·如果指定了**bridge-aggregation**或**route-aggregation**参数而未指定*interface-number*参数，将清除所有二层聚合接口或三层聚合接口上的统计信息。

·如果指定了**bridge-aggregation**或**route-aggregation**参数，同时指定了*interface-number*参数，将清除指定二层聚合接口或三层聚合接口上的统计信息。

·只有在设备上创建了二层或三层聚合接口之后，才能指定**bridge-aggregation**或**route-aggregation**参数。

【举例】

\# 清除二层聚合接口1上的统计信息。

\<Sysname\> reset counters interface bridge-aggregation 1

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- reset lacp statistics**

------------------------------------------------------------------------

**[reset lacp statistics**]命令用来清除成员端口上的LACP统计信息。

【命令】

**[reset lacp statistics** [ **interface** *interface-list* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-list*]：表示清除指定成员端口上的LACP统计信息。*interface-list*为成员端口列表，表示一个或多个成员端口。表示方式为*interface-list *= *interface-type interface-number* [ **to** *interface-type interface-number* ]。其中，*interface-type*为接口类型，*interface-number*为接口编号。若未指定本参数，则清除所有成员端口上的LACP统计信息。

【举例】

\# 清除所有成员端口上的LACP统计信息。

\<Sysname\> reset lacp statistics

【相关命令】

·**display link-aggregation member-port**

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- service**

------------------------------------------------------------------------

![说明](以太网链路聚合命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[service**]命令用来配置转发当前接口流量的单板/成员设备。

**[undo service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[service slot** *slot-number*]

**[undo service slot**]

分布式设备－IRF模式：

**[service chassis** *chassis-number* **slot** *slot-number*]

**[undo service chassis**]

【缺省情况】

没有配置转发当前接口流量的单板/成员设备。

【视图】

三层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：指定单板所在的槽位号。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：指定设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：指定成员编号或PEX虚拟槽位号。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

未配置本命令时，流量直接在接收报文的单板/成员设备上进行业务处理。当要求同一个三层聚合接口的流量必须在同一个单板/成员设备上进行处理，此时可以在三层聚合接口下通过**service**命令配置转发当前接口流量的单板/成员设备。

需要注意：

·配置本命令后，该三层聚合接口的子接口也会通过指定的单板/成员设备转发流量。

·如果拔出指定的转发流量单板，流量不会被转发；如果重新插入指定的转发流量的单板，则流量可以恢复在指定板正常转发。

【举例】

\# 配置2号单板转发三层聚合口1的流量。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname interface route-aggregation 1

Sysname-Route-Aggregation1 service slot 2

**以太网链路聚合 \-- 以太网链路聚合配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo shutdown**]命令用来打开当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当打开/关闭三层聚合接口时，会同时打开/关闭其下的所有子接口，而打开/关闭三层聚合子接口则不会对其主接口有影响。

【举例】

\# 开启二层聚合接口1。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 undo shutdown
