<!-- CMD-INDEX
  delete ip rpf-route-static          | 系统视图             | L28
  display mac-address multicast       | 任意视图             | L72
  display mrib interface              | 任意视图             | L166
  display multicast boundary          | 任意视图             | L296
  display multicast forwarding df-info | 任意视图             | L362
  display multicast forwarding event  | 任意视图             | L546
  display multicast forwarding-table  | 任意视图             | L672
  display multicast forwarding-table df-list | 任意视图             | L898
  display multicast routing-table     | 任意视图             | L1012
  display multicast routing-table static | 任意视图             | L1140
  display multicast rpf-info          | 任意视图             | L1226
  ip rpf-route-static                 | 系统视图             | L1328
  load-splitting (MRIB view)          | MRIB视图           | L1396
  longest-match (MRIB view)           | MRIB视图           | L1444
  mac-address multicast               |                  | L1482
  multicast boundary                  | 接口视图             | L1558
  multicast forwarding supervlan community | VLAN接口视图         | L1632
  multicast routing                   | 系统视图             | L1684
  multicast rpf-fail-pkt bridging     | VLAN接口视图         | L1740
  multicast rpf-fail-pkt flooding     | 系统视图             | L1796
  multicast rpf-fail-pkt trap-to-cpu  | 系统视图             | L1846
  reset multicast forwarding event    | 用户视图             | L1896
  reset multicast forwarding-table    | 用户视图             | L1930
  reset multicast routing-table       | 用户视图             | L1982
-->

**组播路由与转发 \-- 组播路由与转发配置命令 \-- delete ip rpf-route-static**

------------------------------------------------------------------------

**[delete ip rpf-route-static**]命令用来删除所有组播静态路由。

【命令】

**[delete ip rpf-route-static** [ **vpn-instance** *vpn-instance-name* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【使用指导】

本命令用来删除所有的组播静态路由，而**undo ip rpf-route-static**命令则用来删除指定的组播静态路由。

【举例】

\# 删除公网实例中的所有组播静态路由。

\<Sysname\> system-view

Sysname delete ip rpf-route-static

This will erase all multicast static routes and their configurations, you must reconfigure all static routes.

Are you sure?[Y/N:y]

【相关命令】

·**ip rpf-route-static**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display mac-address multicast**

------------------------------------------------------------------------

![说明](组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **mac-address** **multicast**]命令用来显示静态组播MAC地址表信息。

【命令】

**[display mac-address** [ *mac-address* [ **vlan** *vlan-id*  \|  **multicast**   **vlan** *vlan-id*   **count**  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[mac-address*]：显示指定MAC地址的静态组播MAC表项，取值范围为除0100-5Exx-xxxx和3333-xxxx-xxxx以外的任意合法的组播MAC地址，其中x代表0～F的任意一个十六进制数。

**[vlan** *vlan*-*id*]：显示指定VLAN的静态组播MAC地址表项。*vlan*-*id*的取值范围为1～4094。如果未指定本参数，将显示所有VLAN的静态组播MAC地址表项。

**[multicast**]：显示静态组播MAC地址表项。

**[count**]：显示静态组播MAC地址表项的数量。如果指定了本参数，将只显示表项数量而不显示表项内容；如果未指定本参数，将只显示表项内容而不显示表项数量。

【使用指导】

如果未指定任何参数，或仅指定了**vlan**和**count**两参数之一或其组合时，将显示包括静态组播MAC地址表项和单播MAC地址表项在内的所有MAC地址表项信息。

【举例】

\# 显示VLAN 2的静态组播MAC地址表信息。

\<Sysname\> display mac-address multicast vlan 2

MAC Address      VLAN ID    State            Port/NickName            Aging

0100-0001-0001   2          Multicast        GE1/0/1                  N

                                             GE1/0/2

\# 显示静态组播MAC表项的数量。

\<Sysname\> display mac-address multicast count

1 mac address(es) found.

表1-1 display mac-address multicast命令显示信息描述表

字段

描述

MAC Address

MAC地址

VLAN ID

MAC地址所在的VLAN

State

MAC地址表项的状态，Multicast表示该表项是用户手工配置的静态组播MAC地址表项

Port/NickName

MAC地址对应的接口名称或NickName。如果显示为接口名称，表示发往该MAC地址的报文将从此接口发出；如果显示为NickName，表示发往该MAC地址的报文进入TRILL网络后的Egress RB。有关NickName、TRILL和RB的详细介绍，请参见"TRILL配置指导"中的"TRILL"

Aging

老化状态，N表示该表项不会被老化

1 mac address(es) found

共有1个静态组播MAC地址表项

【相关命令】

·**mac-address multicast**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display mrib interface**

------------------------------------------------------------------------

**[display mrib interface**]命令用来显示MRIB（Multicast Routing Information Base，组播路由信息库）维护的接口信息，这些接口包括配置了PIM、IGMP等组播协议的接口以及注册接口、InLoopBack0接口、Null0接口等内部接口。

【命令】

**[display mrib ** **vpn-instance** *vpn-instance-name* ] **interface**  *interface-type interface-number*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[interface-type* *interface-number*]：显示指定接口上MRIB维护的接口信息。如果未指定本参数，将显示所有接口上MRIB维护的接口信息。

【举例】

\# 显示公网实例所有接口上MRIB维护的接口信息。

\<Sysname\> display mrib interface

 Interface: GigabitEthernet1/0/1

     Index: 0x00000001

     Current state: up

     MTU: 1500

     Type: BROADCAST

     Protocol: PIM-DM

     PIM protocol state: Enabled

     Address list:

          1. Local address : 8.12.0.2/16

             Remote address: 0.0.0.0

             Reference     : 1

             State         : NORMAL

表1-2 display mrib interface命令显示信息描述表

字段

描述

Interface

接口的名称

Index

接口的索引号

Current state

接口的状态，包括up和down

MTU

MTU（Maximum Transmission Unit，最大传输单元）值

Type

接口的类型，包括：

·BROADCAST：表示广播链路接口

·P2P：表示P2P接口

·LOOP：表示LoopBack接口

·REGISTER：表示注册接口

·NBMA：表示NBMA接口

·MTUNNEL：表示组播隧道接口

Protocol

接口的协议类型标记，包括PIM-DM、PIM-SM、IGMP、PROXY和MD

PIM protocol state

PIM协议的使能状态，包括：

·Enabled：表示使能

·Disabled：表示关闭

Address list

接口地址列表

Local address

本端的地址

Remote address

远端的地址（仅Vlink类型接口有效）

Reference

地址被引用的次数

State

接口地址的状态，包括NORMAL和DEL

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast boundary**

------------------------------------------------------------------------

**[display multicast boundary**]命令用来显示组播边界的信息。

【命令】

**[display multicast** [ **vpn-instance** *vpn-instance-name*  **boundary** \*group-address*[ [ *mask-length* \| *mask* ] ]  **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[group-address*]：显示指定组播组的组播边界信息，取值范围为224.0.0.0～239.255.255.255。如果未指定本参数，将显示所有组播组的组播边界信息。

*[mask-length*]：指定组播组地址的掩码长度，取值范围为4～32，缺省值为32。

*[mask*]：指定组播组地址的掩码，缺省值为255.255.255.255。

**[interface ***interface-type interface-number*]：显示指定接口上的组播边界信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的组播边界信息。

【举例】

\# 显示公网实例所有接口上所有组播组的组播边界信息。

\<Sysname\> display multicast boundary

 Boundary            Interface

 224.1.1.0/24        GE1/0/1

 239.2.2.0/24        GE1/0/2

表1-3 display multicast boundary命令显示信息描述表

字段

描述

Boundary

表示组播边界对应的组播组

Interface

表示组播边界对应的接口

【相关命令】

·**multicast boundary**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast forwarding df-info**

------------------------------------------------------------------------

**[display multicast forwarding df-info**]命令用来显示组播转发的DF信息。

【命令】

集中式设备：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding** **df-info**  *rp-address*   **verbose**   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding** **df-info**  *rp-address*   **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding** **df-info**  *rp-address*   **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[rp-address*]：指定双向PIM的RP地址。

**[verbose**]：显示组播转发的DF详细信息。如果未指定本参数，将显示组播转发的DF概要信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上]的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示公网实例组播转发的DF概要信息。

\<Sysname\> display multicast forwarding df-info

Total 1 RPs, 1 matched

00001. RP address: 7.11.0.2

     Flags: 0x0

     Uptime: 04:14:40

     RPF interface: GigabitEthernet1/0/1

     List of 1 DF interfaces:

       1: GigabitEthernet1/0/2

\# 显示公网实例组播转发的DF详细信息。

\<Sysname\> display multicast forwarding df-info verbose

Total 1 RPs, 1 matched

00001. RP address: 7.11.0.2

     MID: 2, Flags: 0x0

     Uptime: 03:37:22

       Product information: 0x7a2f762f, 0x718fee9f, 0x4b82f137, 0x71c32184

     RPF interface: GigabitEthernet1/0/1

       Product information: 0xa567d6fc, 0xadeb03e3

       Tunnel  information: 0xdfb107d4, 0x7aa5d510

     List of 1 DF interfaces:

       1: GigabitEthernet1/0/2

          Product information: 0xa986152b, 0xb74a9a2f

          Tunnel  information: 0x297ca208, 0x76985b89

\# 显示ADVPN应用组网组播转发的DF概要信息。

\<Sysname\> display multicast forwarding df-info

Total 1 RPs, 1 matched

00001. RP address: 1.1.1.1

     Flags: 0x0

     Uptime: 00:00:53

     RPF interface: Tunnel0, 192.168.0.1

     List of 2 DF interfaces:

       1: LoopBack0

       2: Tunnel0, 192.168.0.3

表1-4 display multicast forwarding df-info命令显示信息描述表

字段

描述

Total 1 RPs, 1 matched

RP的总数和匹配数

00001

RP表项的序号

RP address

RP的地址

MID

RP表项的标识，每个RP表项都有唯一的标识

Flags

RP表项的状态，通过将不同的比特位置位来表示不同的状态：

·0x0：表示正常表项

·0x4：表示表项下刷失败

·0x8：表示有DF接口下刷失败

·0x40：表示表项即将被删除

·0x100：表示表项正在被删除

·0x200：表示表项处于平滑状态

Uptime

RP表项已存在的时间

Product information

产品信息

Tunnel  information

隧道接口信息

RPF interface

到达RP的RPF接口

List of 1 DF interfaces

DF接口列表

Tunnel0, 192.168.0.3

ADVPN隧道接口以及远端IP地址

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast forwarding event**

------------------------------------------------------------------------

**[display multicast forwarding event**]命令用来显示组播转发的事件统计信息。

【命令】

集中式设备：

**[display multicast** **vpn-instance** *vpn-instance-name* ] **forwarding event**  **cpu** *cpu-number*

分布式设备－独立运行模式/集中式IRF设备：

**[display multicast** **vpn-instance** *vpn-instance-name* ] **forwarding event**  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display multicast** **vpn-instance** *vpn-instance-name* ] **forwarding event**  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示公网实例组播转发的事件统计信息。

\<Sysname\> display multicast forwarding event

Total entry active events sent: 0

Total entry inactive events sent: 0

Total NoCache events sent: 2

Total NoCache events dropped: 0

Total WrongIF events sent: 0

Total WrongIF events dropped: 0

Total SPT switch events sent: 0

NoCache rate limit: 1024 packets/s

WrongIF rate limit: 1 packets/10s

Total timer of register suppress timeout: 0

表1-5 display multicast forwarding event命令显示信息描述表

字段

描述

Total entry active events sent

表项活跃事件的发送次数

Total entry inactive events sent

表项不活跃事件的发送次数

Total NoCache events sent

NoCache事件的发送次数

Total NoCache events dropped

NoCache事件的丢弃次数

Total WrongIF events sent

WrongIF事件的发送次数

Total WrongIF events droppet

WrongIF事件的丢弃次数

Total SPT switch events sent

SPT切换事件的发送次数

NoCache rate limit

NoCache事件[的发送限速，单位为报文]/秒

WrongIF rate limit

WrongIF事件[的发送限速，单位为报文]/10秒

Total timer of register suppress timeout

注册抑制超时的总次数

【相关命令】

·**reset multicast forwarding event**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast forwarding-table**

------------------------------------------------------------------------

**[display multicast forwarding-table**]命令用来显示组播转发表的信息。

【命令】

集中式设备：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  ]**forwarding-table **[[ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **cpu** *cpu-number* \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* \| **statistics** ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  ]**forwarding-table **[[ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* \| **slot** *slot-number*  **cpu** *cpu-number*  \| **statistics** ] \*]]

分布式设备－IRF模式：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  ]**forwarding-table **[[ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* \| **statistics** ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[source-address*]：组播源地址，显示包含指定组播源的组播转发项。

*[group-address*]：组播组地址，显示指定组播组的组播转发项，取值范围为224.0.0.0～239.255.255.255。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为4～32，缺省值为32；对于组播源地址，其取值范围为0～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[incoming-interface**]：显示指定入接口的组播转发项。

*[interface-type* *interface-number*]：显示指定接口类型和接口编号的入接口的组播转发项。

**[outgoing-interface**]：显示指定出接口的组播转发项。

**[exclude**]：显示出接口列表中不包含指定接口的组播转发项。

**[include**]：显示出接口列表中包含指定接口的组播转发项。

**[match**]：显示出接口列表中包含且仅包含指定接口的组播转发项。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参[数，将显示主控板上的信息。（分布式设备－独立运行模式）]

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics**]：显示组播转发表的统计信息。

【举例】

\# 显示公网实例组播转发表的信息。

\<Sysname\> display multicast forwarding-table

Total 1 entries, 1 matched

00001. (172.168.0.2, 227.0.0.1)

     Flags: 0x0

     Uptime: 00:08:32, Timeout in: 00:03:26

     Incoming interface: Vlan-interface10

          Incoming sub-VLAN: VLAN 11

          Outgoing sub-VLAN: VLAN 12

                             VLAN 13

     List of 1 outgoing interfaces:

       1: Vlan-interface20

          Sub-VLAN: VLAN 21

                    VLAN 22

     Matched 19648 packets(20512512 bytes), Wrong If 0 packet

     Forwarded 19648 packets(20512512 bytes)

\# 显示ADVPN应用组网组播转发表的信息。

\<Sysname\> display multicast forwarding-table

Total 1 entry, 1 matched

00001. (172.168.0.2, 227.0.0.1)

     Flags: 0x0

     Uptime: 00:08:32, Timeout in: 00:03:26

     Incoming interface: Tunnel1, 12.1.1.3

     List of 2 outgoing interface:

           1:  Tunnel1, 12.1.1.1

           2:  Tunnel1, 12.1.1.2

     Matched 19648 packets(20512512 bytes), Wrong If 0 packet

     Forwarded 19648 packets(20512512 bytes)

表1-6 display multicast forwarding-table命令显示信息描述表

字段

描述

Total 1 entries, 1 matched

组播转发表中（S，G）表项的总数和匹配数

00001

表示（S，G）表项的序号

(172.168.0.2,227.0.0.1)

表示组播转发表的（S，G）表项

Flags

（S，G）表项的状态，通过将不同的比特位置位来表示不同的状态：

·0x0：表示正常表项

·0x1：表示表项处于Inactive状态

·0x2：表示空转发表项

·0x4：表示表项下刷失败

·0x8：表示有出接口下刷失败

·0x10：表示下刷Data-Group失败

·0x20：表示表项有注册出接口

·0x40：表示表项即将被删除

·0x80：表示表项处于注册抑制状态

·0x100：表示表项正在被删除

·0x200：表示表项处于平滑状态

·0x400：表示表项中存在Super VLAN对应的VLAN接口

·0x800：表示表项中存在到组播源地址的ARP表项

·0x4000000：表示表项由IGMP代理下发创建

·0x20000000：表示双向PIM的转发表项

Uptime

表示（S，G）表项已存在时间

Timeout in

表示（S，G）表项的超时剩余时间

Incoming interface

表示（S，G）表项的入接口

Incoming sub-VLAN

表示当（S，G）表项的入接口为Super VLAN对应的VLAN接口时，该Super VLAN的入Sub VLAN

Outgoing sub-VLAN

表示当（S，G）表项的入接口为Super VLAN对应的VLAN接口时，该Super VLAN的出Sub VLAN

List of 1 outgoing interfaces

表示（S，G）表项的出接口列表

Sub-VLAN

表示当（S，G）表项的出接口为Super VLAN对应的VLAN接口时，该Super VLAN的出Sub VLAN

Tunnel1, 12.1.1.1

ADVPN隧道接口以及远端IP地址

Matched 19648 packets (20512512 bytes), Wrong If 0 packet

（S，G）表项匹配的报文数量（字节数），发生入接口错误的报文个数

Forwarded 19648 packets (20512512 bytes)

（S，G）表项已转发的组播报文数量（字节数）

【相关命令】

·**reset multicast forwarding-table**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast forwarding-table df-list**

------------------------------------------------------------------------

**[display multicast forwarding-table df-list**]命令用来显示组播转发表的DF列表信息。

【命令】

集中式设备：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **df-list**  *group-address*   **verbose**   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **df-list**  *group-address*   **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **df-list**  *group-address*   **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网的信息。

*[group-address*]：指定组播组的地址，显示指定组播组的组播转发表的DF列表信息，取值范围为224.0.0.0～239.255.255.255。

**[verbose**]：显示组播转发表的DF列表详细信息。如果未指定本参数，将显示组播转发表的DF列[表概要信息。]

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示公网实例组播转发表的DF列表概要信息。

\<Sysname\> display multicast forwarding-table df-list

Total 1 entries, 1 matched

00001. (0.0.0.0, 225.0.0.1)

     List of 1 DF interfaces:

       1: GigabitEthernet1/0/1

\# 显示公网实例组播转发表的DF列表详细信息。

\<Sysname\>display multicast forwarding-table df-list verbose

Total 1 entries, 1 matched

00001. (0.0.0.0, 225.0.0.1)

       List of 1 DF interfaces:

         1: GigabitEthernet1/0/1

            Product information: 0x347849f6, 0x14bd6837

            Tunnel  information: 0xc4857986, 0x128a9c8f

表1-7 display multicast forwarding-table df-list命令显示信息描述表

字段

描述

Total 1 entries, 1 matched

表项总数和匹配数

00001

表项的序号

(0.0.0.0, 225.0.0.1)

组播转发表的（\*，G）表项

List of 1 DF interfaces

DF接口列表

Product information

产品信息

Tunnel  information

隧道接口信息

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast routing-table**

------------------------------------------------------------------------

**[display multicast routing-table**]命令用来显示组播路由表的信息。

【命令】

**[display multicast ** **vpn-instance** *vpn-instance-name* ] **routing-table **[[ *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* ] \*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[source-address*]：组播源地址，显示包含指定组播源的组播路由项。

*[group-address*]：组播组地址，显示指定组播组的组播路由项，取值范围为224.0.0.0～239.255.255.255。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为4～32，缺省值为32；对于组播源地址，其取值范围为0～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[incoming-interface**]：显示指定入接口的组播路由项。

*[interface-type interface-number*]：显示指定接口类型和接口编号的入接口的组播路由项。

**[outgoing-interface**]：显示指定出接口的组播路由项。

**[exclude**]：显示出接口列表中不包含指定接口的组播路由项。

**[include**]：显示出接口列表中包含指定接口的组播路由项。

**[match**]：显示出接口列表中包含且仅包含指定接口的组播路由项。

【使用指导】

组播路由表是进行组播数据转发的基础，通过查看该表可以了解（S，G）表项等的建立情况。

【举例】

\# 显示公网实例组播路由表的信息。

\<Sysname\> display multicast routing-table

 Total 1 entries

 00001. (172.168.0.2, 227.0.0.1)

       Uptime: 00:00:28

       Upstream Interface: GigabitEthernet1/0/1

       List of 2 downstream interfaces

           1:  GigabitEthernet1/0/2

           2:  GigabitEthernet1/0/3

\# 显示ADVPN应用组网组播路由表的信息。

\<Sysname\> display multicast routing-table

 Total 1 entries

 00001. (172.168.0.2, 227.0.0.1)

       Uptime: 00:00:28

       Upstream Interface: Tunnel1, 12.1.1.3

       List of 2 downstream interfaces

           1:  Tunnel1, 12.1.1.1

           2:  Tunnel1, 12.1.1.2

表1-8 display multicast routing-table命令显示信息描述表

字段

描述

Total 1 entries

组播路由表中（S，G）表项的总数

00001

表示（S，G）表项的序号

(172.168.0.2, 227.0.0.1)

表示组播路由表的（S，G）表项

Uptime

表示（S，G）表项已经存在的时间

Upstream Interface

表示（S，G）表项的上游接口，表示组播数据应该从此接口到达

List of 2 downstream interfaces

下游接口列表，表示哪些接口需要进行组播转发

Tunnel1, 12.1.1.1

ADVPN隧道接口以及远端IP地址

【相关命令】

·**reset multicast routing-table**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast routing-table static**

------------------------------------------------------------------------

**[display multicast routing-table static**]命令用来显示组播静态路由表的信息。

【命令】

**[display multicast ** **vpn-instance** *vpn-instance-name* ] **routing-table static**[ [ *source-address* { *mask-length* \| *mask* } ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[source-address*]：显示指定组播源的组播静态路由信息。

*[mask-length*]：指定组播源地址的掩码长度，取值范围为0～32。

*[mask*]：指定组播源地址的掩码。

【使用指导】

本命令只显示已生效的组播静态路由信息。

【举例】

\# 显示公网实例组播静态路由表的信息。

\<Sysname\> display multicast routing-table static

Destinations: 3        Routes: 4

Destination/Mask   Pre  RPF neighbor    Interface

1.1.0.0/16         10   7.12.0.1        Vlan12

                        7.11.0.1        Vlan11

2.2.2.0/24         20   7.11.0.1        Vlan11

3.3.3.3/32         50   7.12.0.1        Vlan12

表1-9 display multicast routing-table static命令显示信息描述表

字段

描述

Destinations

目的地址个数

Routes

路由条数

Destination/Mask

目的地址和掩码长度

Pre

路由优先级

RPF neighbor

可达目的地址的RPF邻居IP地址

Interface

可达目的地址的出接口

**组播路由与转发 \-- 组播路由与转发配置命令 \-- display multicast rpf-info**

------------------------------------------------------------------------

**[display multicast rpf-info**]命令用来显示组播源的RPF信息。

【命令】

**[display multicast** [ **vpn-instance** *vpn-instance-name*  ]**rpf-info** *source-address* [ *group-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[source-address*]：显示指定组播源的RPF信息。

*[group-address*]：显示指定组播组的RPF信息，取值范围为224.0.1.0～239.255.255.255。

【举例】

\# 显示公网组播源192.168.1.55的全部RPF信息。

\<Sysname\> display multicast rpf-info 192.168.1.55

 RPF information about source 192.168.1.55:

     RPF interface: GigabitEthernet1/0/1, RPF neighbor: 10.1.1.1

     Referenced route/mask: 192.168.1.0/24

     Referenced route type: igp

     Route selection rule: preference-preferred

     Load splitting rule: disable

表1-10 display multicast rpf-info命令显示信息描述表

字段

描述

RPF information about source 192.168.1.55

到组播源192.168.1.55的RPF路径信息

RPF interface

表示RPF接口名称

RPF neighbor

表示RPF邻居

Referenced route/mask

表示引用的路由及其掩码长度

Referenced route type

表示引用的路由类型，可以是下列类型之一：

·igp：单播路由（内部网关协议）

·egp：单播路由（外部网关协议）

·unicast (direct)：单播路由（直连）

·unicast：其它单播路由（如单播静态路由等）

·multicast static：组播静态路由

·mbgp：MBGP路由

Route selection rule

RPF路由选择规则，可以是根据路由协议的路由优先级进行选择，或者是按照目的地址对路由表进行最长匹配

Load splitting rule

是否使能了负载分担规则

【相关命令】

·**display multicast forwarding-table**

·**display multicast routing-table**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- ip rpf-route-static**

------------------------------------------------------------------------

**[ip rpf-route-static**]命令用来配置组播静态路由。

**[undo ip rpf-route-static**]命令用来删除指定的组播静态路由。

【命令】

**[ip rpf-route-static** [ **vpn-instance** *vpn-instance-name*  ]*source-address*[ { *mask-length* \| *mask* } { *rpf-nbr-address* \| *interface-type interface-number* } [ **preference** *preference* ]]]

**[undo ip rpf-route-static** [ **vpn-instance** *vpn-instance-name*  ]*source-address*[ { *mask-length* \| *mask* } { *rpf-nbr-address* \| *interface-type interface-number* }]]

【缺省情况】

不存在任何组播静态路由。

【视图】

系统视图

【缺省级别】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

*[source-address*]：指定组播源地址。

*[mask-length*]：指定组播源地址的掩码长度，取值范围为0～32。

*[mask*]：指定组播源地址的掩码。

*[rpf-nbr-address*]：指定RPF邻居的IP地址。

*[interface-type interface-number*]：指定与RPF邻居相连接口的接口类型和接口编号。

*[preference*]：指定路由优先级，取值范围为1～255，缺省值为1。

【使用指导】

·在相同的组播源地址范围下，最多允许配置16个RPF邻居。

·只有点到点类型的接口才能使用指定接口的方式来指定RPF邻居，非点到点类型的接口（包括三层以太网接口、三层聚合接口、Loopback接口或VLAN接口等）不能使用此方式，只能使用指定地址的方式。

·配置的组播静态路由并不一定会生效，因为可能出现指定的RPF邻居无法迭代出接口、指定的RPF接口不属于本实例、指定的RPF接口不是点到点类型或处于down状态等情况。此外，若在相同组播源地址范围下有多条配置，只有路由优先级最高的那条才能被激活。因此，配置完成后建议使用**display multicast routing-table static**命令显示该组播静态路由是否已生效。

·**undo ip rpf-route-static**命令用来删除指定的组播静态路由，而**delete ip rpf-route-static**命令则用来删除所有的组播静态路由。

【举例】

\# 在公网实例中配置到组播源10.1.1.1/24的组播静态路由，其RPF邻居的地址是192.168.1.23。

\<Sysname\> system-view

Sysname ip rpf-route-static 10.1.1.1 24 192.168.1.23

【相关命令】

·**delete ip rpf-route-static**

·**display multicast routing-table static**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- load-splitting (MRIB view)**

------------------------------------------------------------------------

**[load-splitting**]命令用来配置对组播流量进行负载分担。

**[undo load-splitting**]命令用来恢复缺省情况。

【命令】

**[load-splitting**[ { **source** \| **source-group** }]]

**[undo load-splitting**]

【缺省情况】

不对组播流量进行负载分担。

【视图】

MRIB视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[source**]：指定仅根据组播源对组播流量进行负载分担。

**[source-group**]：指定同时根据组播源与组播组对组播流量进行负载分担。

【使用指导】

本命令对双向PIM不生效。

【举例】

\# 在公网实例中配置仅根据组播源对组播流量进行负载分担。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib load-splitting source

**组播路由与转发 \-- 组播路由与转发配置命令 \-- longest-match (MRIB view)**

------------------------------------------------------------------------

**[longest-match**]命令用来配置按照最长匹配来选择RPF路由，即选择掩码最长的路由作为RPF路由。

**[undo longest-match**]命令用来恢复缺省情况。

【命令】

**[longest-match**]

**[undo longest-match**]

【缺省情况】

选择路由优先级最高的路由作为RPF路由。

【视图】

MRIB视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在公网实例中配置按照最长匹配原则选择RPF路由。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib longest-match

**组播路由与转发 \-- 组播路由与转发配置命令 \-- mac-address multicast**

------------------------------------------------------------------------

![说明](组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address** **multicast**]命令用来配置静态组播MAC地址表项。

**[undo** **mac-address** **multicast**]命令用来删除静态组播MAC地址表项。

【命令】

在系统视图下：

**[mac-address multicast ***mac-address*** interface***interface-list*** vlan ***vlan-id*]

**[undo mac-address** [ **multicast**   [ *mac-address* [ **interface** *interface-list*  ] **vlan** *vlan-id* ]]]

在二层以太网接口视图或二层聚合接口视图下：

**[mac-address** **multicast** *mac-address* **vlan** *vlan-id*]

**[undo** **mac-address** [ **multicast**  *mac-address* **vlan** *vlan-id*]]

【缺省情况】

没有配置任何静态组播MAC地址表项。

【视图】

系统视图/二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac*-*address*]：静态组播MAC地址，格式为H-H-H，必须是尚未使用的组播MAC地址（即最高字节的最低比特位为1的MAC地址）。

**[interface**] *interface-list*：接口列表，表示一个或多个接口。表示方式为*interface-list =* { *interface-type interface-number* [ **to** *interface-type interface-number*  }&\<1-4\>]。其中，*interface-type*为接口类型（目前只支持二层以太网接口和二层聚合接口），*interface-number*为接口编号。&\<1-4\>表示前面的参数最多可以输入4次。

**[vlan*** vlan*-*id*]：指定接口所属的VLAN，必须为已创建的VLAN，如果指定的接口不属于该VLAN，系统将提示出错。*vlan-id*为VLAN的编号，取值范围为1～4094。

【使用指导】

·执行本命令不需要使能IP组播路由。

·用户既可以在系统视图对指定接口进行配置，也可以在接口视图下只对当前接口进行配置。

·执行**undo** **mac-address** **multicast**命令时若未指定**multicast**参数，将删除包括静态组播MAC地址表项和单播MAC地址表项在内的所有MAC地址表项。

【举例】

\# 配置静态组播MAC地址表项0100-0001-0001，对应的端口为VLAN 2内的GigabitEthernet1/0/1～GigabitEthernet1/0/5。

\<Sysname\> system-view

Sysname mac-address multicast 0100-0001-0001 interface gigabitethernet 1/0/1 to gigabitethernet 1/0/5 vlan 2

\# 在端口GigabitEthernet1/0/1下配置静态组播MAC地址表项0100-0001-0001，该端口属于VLAN 2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address multicast 0100-0001-0001 vlan 2

【相关命令】

·**display** **mac-address** **multicast**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- multicast boundary**

------------------------------------------------------------------------

**[multicast boundary**]命令用来配置组播转发边界。

**[undo multicast boundary**]命令用来删除组播转发边界。

【命令】

**[multicast boundary ***group-address*[ { *mask-length* \| *mask* }]]

**[undo multicast boundary**[ { *group-address* { *mask-length* \| *mask* } \| **all** }]]

【缺省情况】

没有配置组播转发边界。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：指定组播组地址，取值范围为224.0.0.0～239.255.255.255。

*[mask-length*]：指定组播组地址的掩码长度，取值范围为4～32。

*[mask*]：指定组播组地址的掩码。

**[all**]：删除该接口上配置的所有组播转发边界。

【使用指导】

·执行本命令不需要使能IP组播路由。

·组播转发边界为指定地址范围的组播组划定了边界条件，如果组播报文的目的地址与边界条件匹配，就停止转发。

·一个接口可以作为不同地址范围的组播组的转发边界，即允许在同一接口上多次执行本命令为不同地址范围的组播组设定转发边界。

·假设A和B为不同地址范围的组播组的集合，且B是A的真子集：如果接口先配置为A的转发边界，再配置为B的转发边界，则该接口仍然为A的转发边界；如果接口先配置为B的转发边界，再配置为A的转发边界，则该接口将变为A的转发边界。

【举例】

·路由应用

\# 将接口GigabitEthernet1/0/1配置为地址范围为239.2.0.0/16的组播组的转发边界。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 multicast boundary 239.2.0.0 16

·交换应用

\# 将接口Vlan-interface100配置为地址范围为239.2.0.0/16的组播组的转发边界。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 multicast boundary 239.2.0.0 16

【相关命令】

·**display multicast boundary**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- multicast forwarding supervlan community**

------------------------------------------------------------------------

![说明](组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[multicast forwarding supervlan community**]命令用来配置组播数据在Super VLAN内的各Sub VLAN之间互通。

**[undo multicast forwarding supervlan community**]命令用来恢复缺省情况。

【命令】

**[multicast forwarding supervlan community**]

**[undo multicast forwarding supervlan community**]

【缺省情况】

组播数据在Super VLAN内的各Sub VLAN之间隔离。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行本命令后必须清除组播转发表中所有以该VLAN接口为入接口的转发项，否则本命令将不能生效。

【举例】

\# 配置组播数据在Super VLAN 2内的各Sub VLAN之间互通。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 multicast forwarding supervlan community

【相关命令】

·**reset multicast forwarding-table**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- multicast routing**

------------------------------------------------------------------------

**[multicast routing**]命令用来使能IP组播路由，并进入MRIB视图。

**[undo multicast routing**]命令用来关闭IP组播路由。

【命令】

**[multicast routing** [ **vpn-instance** *vpn-instance-name* ]]

**[undo multicast routing** [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

IP组播路由处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【使用指导】

·只有在公网实例或VPN实例中使能了IP组播路由，该实例中的其它三层组播功能才能生效；

·没有使能IP组播路由前，设备不转发任何组播报文。

【举例】

\# 使能公网实例中的IP组播路由，并进入公网实例的MRIB视图。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib

\# 使能VPN实例mvpn中的IP组播路由，并进入该VPN实例的MRIB视图。

\<Sysname\> system-view

Sysname multicast routing vpn-instance mvpn

Sysname-mrib-mvpn

**组播路由与转发 \-- 组播路由与转发配置命令 \-- multicast rpf-fail-pkt bridging**

------------------------------------------------------------------------

![说明](组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[multicast rpf-fail-pkt bridging**]命令用来配置在当前VLAN内组播RPF检查失败的组播数据报文。

**[undo multicast rpf-fail-pkt bridging**]命令用来恢复缺省情况。

【命令】

**[multicast rpf-fail-pkt bridging**]

**[undo multicast rpf-fail-pkt bridging**]

【缺省情况】

不在VLAN内组播RPF检查失败的组播数据报文。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·执行本命令不需要使能IP组播路由。

·执行本命令时，要先配置在所有VLAN内泛洪RPF检查失败的组播数据报文，并要求该VLAN内使能了IGMP Snooping且对应VLAN接口上配置有三层组播协议（IGMP或PIM），否则本命令将不能生效。

·执行本命令后必须清除该VLAN内所有动态组播组的IGMP Snooping转发表项，否则本命令将不能生效。

【举例】

\# 配置在VLAN 2内组播RPF检查失败的组播数据报文。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 multicast rpf-fail-pkt bridging

【相关命令】

·**multicast rpf-fail-pkt flooding**

·**reset ****igmp-snooping group**（IP组播命令参考/IGMP Snooping）

**组播路由与转发 \-- 组播路由与转发配置命令 \-- multicast rpf-fail-pkt flooding**

------------------------------------------------------------------------

![说明](组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[multicast rpf-fail-pkt flooding**]命令用来配置在所有VLAN内泛洪RPF检查失败的组播数据报文。

**[undo multicast rpf-fail-pkt flooding**]命令用来恢复缺省情况。

【命令】

**[multicast rpf-fail-pkt flooding**]

**[undo multicast rpf-fail-pkt flooding**]

【缺省情况】

不在VLAN内泛洪RPF检查失败的组播数据报文。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·执行本命令不需要使能IP组播路由。

·执行本命令后必须清除组播转发表中的所有转发项，否则本命令将不能生效。

【举例】

\# 配置在所有VLAN内泛洪RPF检查失败的组播数据报文。

\<Sysname\> system-view

Sysname multicast rpf-fail-pkt flooding

【相关命令】

·**reset multicast forwarding-table**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- multicast rpf-fail-pkt trap-to-cpu**

------------------------------------------------------------------------

![说明](组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[multicast rpf-fail-pkt trap-to-cpu**]命令用来配置把RPF检查失败的组播数据报文上送CPU处理。

**[undo multicast rpf-fail-pkt trap-to-cpu**]命令用来恢复缺省情况。

【命令】

**[multicast rpf-fail-pkt trap-to-cpu**]

**[undo multicast rpf-fail-pkt trap-to-cpu**]

【缺省情况】

不把RPF检查失败的组播数据报文上送CPU处理。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·执行本命令不需要使能IP组播路由。

·执行本命令后必须清除组播转发表中的所有转发项，否则本命令将不能生效。

【举例】

\# 配置把RPF检查失败的组播数据报文上送CPU处理。

\<Sysname\> system-view

Sysname multicast rpf-fail-pkt trap-to-cpu

【相关命令】

·**reset multicast forwarding-table**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- reset multicast forwarding event**

------------------------------------------------------------------------

**[reset multicast forwarding event**]命令用来清除组播转发的事件统计信息。

【命令】

**[reset multicast** **vpn-instance** *vpn-instance-name* ] **forwarding event**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

【举例】

\# 清除公网实例组播转发的事件统计信息。

\<Sysname\> reset multicast forwarding event

【相关命令】

·**display multicast forwarding**** event**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- reset multicast forwarding-table**

------------------------------------------------------------------------

**[reset multicast forwarding-table**]命令用来清除组播转发表中的转发项。

【命令】

**[reset multicast ** **vpn-instance** *vpn-instance-name* ] **forwarding-table**[ { { *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask-length* \| *mask* } ] \| **incoming-interface** { *interface-type interface-number* } } \* \| **all** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

*[source-address*]：组播源地址，清除包含指定组播源的组播转发项。

*[group-address*]：组播组地址，清除指定组播组的组播转发项，取值范围为224.0.0.0～239.255.255.255。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为4～32，缺省值为32；对于组播源地址，其取值范围为0～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[incoming-interface**]：清除指定入接口的组播转发项。

*[interface-type* *interface-number*]：清除指定接口类型和接口编号的入接口的组播转发项。

**[all**]：清除组播转发表中的所有组播转发项。

【使用指导】

清除组播转发表中的转发项后，组播路由表中的相应表项也将随之被删除。

【举例】

\# 从公网实例组播转发表中清除组播组225.5.4.3的相关转发表项。

\<Sysname\> reset multicast forwarding-table 225.5.4.3

【相关命令】

·**display multicast forwarding-table**

**组播路由与转发 \-- 组播路由与转发配置命令 \-- reset multicast routing-table**

------------------------------------------------------------------------

**[reset multicast routing-table**]命令用来清除组播路由表中的路由项。

【命令】

**[reset multicast ** **vpn-instance** *vpn-instance-name* ] **routing-table**[ { { *source-address* [ **mask** { *mask-length* \| *mask* } ] \| *group-address* [ **mask** { *mask* \| *mask-length* } ] \| **incoming-interface** *interface-type interface-number* } \* \| **all** }]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

*[source-address*]：组播源地址，清除包含指定组播源的组播路由项。

*[group-address*]：组播组地址，清除指定组播组的组播路由项，取值范围为224.0.0.0～239.255.255.255。

*[mask-length*]：指定组播组或组播源地址的掩码长度。对于组播组地址，其取值范围为4～32，缺省值为32；对于组播源地址，其取值范围为0～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[incoming-interface**]：清除指定入接口的组播路由项。

*[interface-type* *interface-number*]：清除指定接口类型和接口编号的入接口的组播路由项。

**[all**]：清除组播路由表中的所有组播路由项。

【使用指导】

清除组播路由表中的路由项后，组播转发表中的相应表项也将被随之删除。

【举例】

\# 从公网实例组播路由表中清除组播组225.5.4.3的相关路由项。

\<Sysname\> reset multicast routing-table 225.5.4.3

【相关命令】

·**display multicast routing-table**
