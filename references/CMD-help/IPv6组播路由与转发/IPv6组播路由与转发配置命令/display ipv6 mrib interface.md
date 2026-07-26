
**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 mrib interface**

------------------------------------------------------------------------

**[display ipv6 mrib interface**]命令用来显示IPv6 MRIB（Multicast Routing Information Base，组播路由信息库）维护的接口信息，这些接口包括配置了IPv6 PIM、MLD等IPv6组播协议的接口以及注册接口、InLoopBack0接口、Null0接口等内部接口。

【命令】

**[display ipv6 mrib ** **vpn-instance** *vpn-instance-name* ] **interface**  *interface-type interface-number*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[interface-type* *interface-number*]：显示指定接口上IPv6 MRIB维护的接口信息。如果未指定本参数，将显示所有接口上IPv6 MRIB维护的接口信息。

【举例】

\# 显示公网实例所有接口上IPv6 MRIB维护的接口信息。

\<Sysname\> display ipv6 mrib interface

 Interface: GigabitEthernet1/0/1

     Index: 0x00000001

     Current state: up

     MTU: 1500

     Type: BROADCAST

     Protocol: PIM-DM

     PIM protocol state: Enabled

     Address list:

          1. Local address : FE80:7:11::1/10

             Remote address: ::

             Reference     : 1

             State         : NORMAL

表1-1 display ipv6 mrib interface命令显示信息描述表

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

接口的协议类型标记，包括PIM-DM、PIM-SM、MLD和PROXY

PIM protocol state

IPv6 PIM协议的使能状态，包括：

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

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 multicast boundary**

------------------------------------------------------------------------

**[display ipv6 multicast boundary**]命令用来显示IPv6组播边界的信息。

【命令】

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **boundary** { **group**  *ipv6-group-address* [ *prefix-length*  ] \| **scope**  *scope-id*  }  **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**[group**]：显示IPv6组播组的组播边界信息。

*[ipv6-group-address*]：指定IPv6组播组的地址，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的IPv6组播边界信息。

*[prefix-length*]：指定IPv6组播组地址的前缀长度，取值范围为8～128，缺省值为128。

**[scope**]：显示IPv6管理域的组播边界信息。

*[scope-id*]：指定IPv6管理域的编号，取值范围为3～15。如果未指定本参数，将显示所有IPv6管理域的IPv6组播边界信息。

**[interface ***interface-type interface-number*]：显示指定接口上的IPv6组播边界信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的IPv6组播边界信息。

【举例】

\# 显示公网实例所有接口上所有IPv6组播组的IPv6组播边界信息。

\<Sysname\> display ipv6 multicast boundary group

 Boundary                                                 Interface

 FF1E::/64                                                GE1/0/1

\# 显示公网实例所有接口上所有IPv6管理域的IPv6组播边界信息。

\<Sysname\> display ipv6 multicast boundary scope

 Boundary            Interface

        3            GigabitEthernet1/0/1

表1-2 display ipv6 multicast boundary命令显示信息描述表

字段

描述

Boundary

表示IPv6组播边界对应的IPv6组播组或IPv6管理域

Interface

表示IPv6组播边界对应的接口

【相关命令】

·**ipv6 multicast boundary**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 multicast forwarding df-info**

------------------------------------------------------------------------

**[display ipv6 multicast forwarding df-info**]命令用来显示IPv6组播转发的DF信息。

【命令】

集中式设备：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding** **df-info**  *ipv6-rp-address*   **verbose**   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding** **df-info**  *ipv6-rp-address*   **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding** **df-info**  *ipv6-rp-address*   **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-rp-address*]：指定IPv6双向PIM的RP地址。

**[verbose**]：显示IPv6组播转发的DF详细信息。如果未指定本参数，将显示IPv6组播转发的DF概要信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示公网实例IPv6组播转发的DF概要信息。

\<Sysname\> display ipv6 multicast forwarding df-info

Total 1 RPs, 1 matched

00001. RP address: 7:11::1

     Flags: 0x0

     Uptime: 01:46:40

     RPF interface: GigabitEthernet1/0/1

     List of 1 DF interfaces:

       1: GigabitEthernet1/0/2

\# 显示公网实例IPv6组播转发的DF详细信息。

\<Sysname\> display ipv6 multicast forwarding df-info verbose

Total 1 RPs, 1 matched

00001. RP address: 7:11::1

     MID: 2, Flags: 0x0

     Uptime: 00:03:53

       Product information: 0x7a2f762f, 0x718fee9f, 0x4b82f137, 0x71c32184

     RPF interface: GigabitEthernet1/0/1

       Product information: 0xa567d6fc, 0xadeb03e3

       Tunnel  information: 0xdfb107d4, 0x7aa5d510

     List of 1 DF interfaces:

       1: GigabitEthernet1/0/2

          Product information: 0xa986152b, 0xb74a9a2f

          Tunnel  information: 0x297ca208, 0x76985b89

\# 显示ADVPN应用组网IPv6组播转发的DF概要信息。

\<Sysname\> display ipv6 multicast forwarding df-info

Total 1 RPs, 1 matched

00001. RP address: 2::2

     Flags: 0x0

     Uptime: 00:00:14

     RPF interface: LoopBack0

     List of 2 DF interfaces:

       1: Tunnel0, FE80::1

       2: Tunnel0, FE80::3

表1-3 display ipv6 multicast forwarding df-info命令显示信息描述表

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

Tunnel0, FE80::1

ADVPN隧道接口以及远端IPv6 link-local地址

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 multicast forwarding event**

------------------------------------------------------------------------

**[display ipv6 multicast forwarding event**]命令用来显示IPv6组播转发的事件统计信息。

【命令】

集中式设备：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding event**  **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding event**  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding event**  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示公网实例IPv6组播转发的事件统计信息。

\<Sysname\> display ipv6 multicast forwarding event

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

表1-4 display ipv6 multicast forwarding event命令显示信息描述表

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

NoCache事件的发送限速，单位为报文/秒

WrongIF rate limit

WrongIF事件的发送限速，单位为报文/10秒

Total timer of register suppress timeout

注册抑制超时的总次数

【相关命令】

·**reset ipv6 multicast forwarding event**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 multicast forwarding-table**

------------------------------------------------------------------------

**[display ipv6 multicast forwarding-table**]命令用来显示IPv6组播转发表的信息。

【命令】

集中式设备：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **cpu** *cpu-number* \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* \| **statistics** ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 multicast **[ **vpn-instance** *vpn-instance-name*  **forwarding-table**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* \| **slot** *slot-number*  **cpu** *cpu-number*  \| **statistics** ] \*]]

分布式设备－IRF模式：

**[display ipv6 multicast **[ **vpn-instance** *vpn-instance-name*  **forwarding-table**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* \| **statistics** ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-source-address*]：IPv6组播源地址，显示包含指定IPv6组播源的IPv6组播转发项。

*[ipv6-group-address*]：IPv6组播组地址，显示指定IPv6组播组的IPv6组播转发项，取值范围为FFxy::/16，其中x和y均表示0～F的任意一个十六进制数。

*[prefix-length*]：指定IPv6组播组或IPv6组播源地址的前缀长度。对于IPv6组播组地址，其取值范围为8～128，缺省值为128；对于IPv6组播源地址，其取值范围为0～128，缺省值为128。

**[incoming-interface**]：显示指定入接口的IPv6组播转发项。

*[interface-type* *interface-number*]：显示指定接口类型和接口编号的入接口的IPv6组播转发项。

**[outgoing-interface**]：显示指定出接口的IPv6组播转发项。

**[exclude**]：显示出接口列表中不包含指定接口的IPv6组播转发项。

**[include**]：显示出接口列表中包含指定接口的IPv6组播转发项。

**[match**]：显示出接口列表中包含且仅包含指定接口的IPv6组播转发项。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics**]：显示IPv6组播转发表的统计信息。

【举例】

\# 显示公网实例IPv6组播转发表的信息。

\<Sysname\> display ipv6 multicast forwarding-table

Total 1 entries, 1 matched

00001. (1::1, ff0e::1)

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

     Matched 19648 packets(20512512 bytes), Wrong If 0 packets

     Forwarded 19648 packets(20512512 bytes)

\# 显示ADVPN应用组网IPv6组播转发表的信息。

\<Sysname\> display ipv6 multicast forwarding-table

Total 1 entry, 1 matched

00001. (1::1, ff0e::1)

     Flags: 0x0

     Uptime: 00:08:32, Timeout in: 00:03:26

     Incoming interface: Tunnel1, FE80::20:11

     List of 1 outgoing interface:

           1:  Tunnel1, FE80::20:12

           2:  Tunnel1, FE80::20:13

     Matched 19648 packets(20512512 bytes), Wrong If 0 packet

     Forwarded 19648 packets(20512512 bytes)

表1-5 display ipv6 multicast forwarding-table命令显示信息描述表

字段

描述

Total 1 entries, 1 matched

IPv6组播转发表中（S，G）表项的总数和匹配数

00001

表示（S，G）表项的序号

(1::1, ff0e::1)

表示IPv6组播转发表的（S，G）表项

Flags

（S，G）表项的状态，通过将不同的比特位置位来表示不同的状态：

·0x0：表示正常表项

·0x1：表示表项处于Inactive状态

·0x2：表示空转发表项

·0x4：表示表项下刷失败

·0x8：表示有出接口下刷失败

·0x20：表示表项有注册出接口

·0x40：表示表项即将被删除

·0x80：表示表项处于注册抑制状态

·0x100：表示表项正在被删除

·0x200：表示表项处于平滑状态

·0x400：表示表项中存在Super VLAN对应的VLAN接口

·0x800：表示表项中存在到IPv6组播源地址的ND表项

·0x4000000：表示表项由MLD代理下发创建

·0x20000000：表示IPv6双向PIM的转发表项

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

Tunnel1, FE80::20:12

ADVPN隧道接口以及远端IPv6 link-local地址

Matched 19648 packets (20512512 bytes), Wrong If 0 packet

（S，G）表项匹配的报文数量（字节数），发生入接口错误的报文个数

Forwarded 19648 packets (20512512 bytes)

（S，G）表项已转发的IPv6组播报文数量（字节数）

【相关命令】

·**reset ipv6 multicast forwarding-table**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 multicast forwarding-table df-list**

------------------------------------------------------------------------

**[display ipv6 multicast forwarding-table df-list**]命令用来显示IPv6组播转发表的DF列表信息。

【命令】

集中式设备：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **df-list**  *ipv6-group-address*   **verbose**   **cpu** *cpu-number* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **df-list**  *ipv6-group-address*   **verbose**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding-table** **df-list**  *ipv6-group-address*   **verbose**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-group-address*]：IPv6组播组地址，显示指定IPv6组播组的IPv6组播转发表的DF列表信息，取值范围为FFxy::/16，其中x和y均表示0～F的任意一个十六进制数。

**[verbose**]：显示IPv6组播转发表的DF列表详细信息。如果未指定本参数，将显示IPv6组播转发表的DF列表概要信息。

**[slot** *slot-number*]：显示指定单板上的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示主设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示公网实例IPv6组播转发表的DF列表概要信息。

\<Sysname\> display ipv6 multicast forwarding-table df-list

Total 1 entries, 1 matched

00001. (::, FF1E::1)

     List of 1 DF interfaces:

       1: GigabitEthernet1/0/1

\# 显示公网实例IPv6组播转发表的DF列表详细信息。

\<Sysname\> display ipv6 multicast forwarding-table df-list verbose

Total 1 entries, 1 matched

00001. (::, FF1E::1)

       List of 1 DF interfaces:

         1: GigabitEthernet1/0/1

            Product information: 0x347849f6, 0x14bd6837

            Tunnel  information: 0xc4857986, 0x128a9c8f

表1-6 display ipv6 multicast forwarding-table df-list命令显示信息描述表

字段

描述

Total 1 entries, 1 matched

表项总数和匹配数

00001

表项的序号

(::, FF1E::1)

组播转发表的（\*，G）表项

List of 1 DF interfaces

DF接口列表

Product information

产品信息

Tunnel  information

隧道接口信息

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 multicast routing-table**

------------------------------------------------------------------------

**[display ipv6 multicast routing-table**]命令用来显示IPv6组播路由表的信息。

【命令】

**[display ipv6 multicast **[ **vpn-instance** *vpn-instance-name*  **routing-table**  *ipv6-source-address* [ *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **incoming-interface** *interface-type interface-number* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type interface-number* ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-source-address*]：IPv6组播源地址，显示包含指定IPv6组播源的IPv6组播路由项。

*[ipv6-group-address*]：IPv6组播组地址，显示指定IPv6组播组的IPv6组播路由项，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。

*[prefix-length*]：指定IPv6组播组或IPv6组播源地址的前缀长度。对于IPv6组播组地址，其取值范围为8～128，缺省值为128；对于IPv6组播源地址，其取值范围为0～128，缺省值为128。

**[incoming-interface**]：显示指定入接口的IPv6组播路由项。

*[interface-type* *interface-number*]：显示指定接口类型和接口编号的入接口的IPv6组播路由项。

**[outgoing-interface**]：显示指定出接口的IPv6组播路由项。

**[exclude**]：显示出接口列表中不包含指定接口的IPv6组播路由项。

**[include**]：显示出接口列表中包含指定接口的IPv6组播路由项。

**[match**]：显示出接口列表中包含且仅包含指定接口的IPv6组播路由项。

【使用指导】

IPv6组播路由表是进行IPv6组播数据转发的基础，通过查看该表可以了解（S，G）表项等的建立情况。

【举例】

\# 显示公网实例IPv6组播路由表的信息。

\<Sysname\> display ipv6 multicast routing-table

 Total 1 entries

 00001. (2001::2, FFE3::101)

       Uptime: 00:00:14

       Upstream Interface: GigabitEthernet1/0/1

       List of 2 downstream interfaces

           1:  GigabitEthernet1/0/2

           2:  GigabitEthernet1/0/3

\# 显示ADVPN应用组网IPv6组播路由表的信息。

\<Sysname\> display ipv6 multicast routing-table

 Total 1 entries

00001. (2001::2, FFE3::101)

       Uptime: 00:00:14

       Upstream Interface: Tunnel1, FE80::20:11

       List of 2 downstream interfaces

           1:  Tunnel1, FE80::20:12

           2:  Tunnel1, FE80::20:13

表1-7 display ipv6 multicast routing-table命令显示信息描述表

字段

描述

Total 1 entries

IPv6组播路由表中（S，G）表项的总数

00001

表示（S，G）表项的序号

(2001::2, FFE3::101)

表示IPv6组播路由表的（S，G）表项

Uptime

表示（S，G）表项已经存在的时间

Upstream Interface

表示（S，G）表项的上游接口，表示IPv6组播数据应该从此接口到达

List of 2 downstream interfaces

下游接口列表，表示哪些接口需要进行组播转发

Tunnel11, FE80::20:12

ADVPN隧道接口以及远端IPv6 link-local地址

【相关命令】

·**reset ipv6 multicast****routing-table**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- display ipv6 multicast rpf-info**

------------------------------------------------------------------------

**[display ipv6 multicast rpf-info**]命令用来显示IPv6组播源的RPF信息。

【命令】

**[display ipv6 multicast ** **vpn-instance** *vpn-instance-name* ] **rpf-info** *ipv6-source-address*  *ipv6-group-address*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。

*[ipv6-source-address*]：显示指定IPv6组播源的RPF信息。

*[ipv6-group-address*]：显示指定IPv6组播组的RPF信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。

【举例】

\# 显示公网IPv6组播源2001::101的全部RPF信息。

\<Sysname\> display ipv6 multicast rpf-info 2001::101

 RPF information about source 2001::101:

     RPF interface: GigabitEthernet1/0/1, RPF neighbor: FE80::A01:101:1

     Referenced prefix/prefix length: 2001::/64

     Referenced route type: igp

     Route selection rule: preference-preferred

     Load splitting rule: disable

表1-8 display ipv6 multicast rpf-info命令显示信息描述表

字段

描述

RPF information about source 2001::101

到IPv6组播源2001::101的RPF路径信息

RPF interface

表示RPF接口名称

RPF neighbor

表示RPF邻居的IPv6地址（链路本地地址）

Referenced prefix/prefix length

表示引用的路由及其前缀长度

Referenced route type

表示引用的路由类型，可以是下列类型之一：

·igp：IPv6单播路由（内部网关协议）

·egp：IPv6单播路由（外部网关协议）

·unicast (direct)：IPv6单播路由（直连）

·unicast：其它IPv6单播路由（如IPv6单播静态路由等）

·mbgp：IPv6 MBGP路由

Route selection rule

RPF路由选择规则，可以是根据路由协议的路由优先级进行选择，或者是按照目的地址对路由表进行最长匹配

Load splitting rule

是否使能了负载分担规则

【相关命令】

·**display ipv6 multicast forwarding-table**

·**display ipv6 multicast routing-table**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- ipv6 multicast boundary**

------------------------------------------------------------------------

**[ipv6 multicast boundary**]命令用来配置IPv6组播转发边界。

**[undo ipv6 multicast boundary**]命令用来删除IPv6组播转发边界。

【命令】

**[ipv6 multicast boundary**[ { *ipv6-group-address prefix-length* \| **scope** { *scope-id* \| **admin-local** \| **global** \| **organization-local** \| **site-local** } }]]

**[undo ipv6 multicast boundary**[ { *ipv6-group-address prefix-length* \| **all** \| **scope** { *scope-id* \| **admin-local** \| **global** \| **organization-local** \| **site-local** } }]]

【缺省情况】

没有配置IPv6组播转发边界。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-group-address*]：指定IPv6组播组地址，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。

*[prefix-length*]：指定IPv6组播组地址的前缀长度，取值范围为8～128。

**[all**]：删除该接口上配置所有IPv6组播转发边界。

*[scope-id*]：指定Scope字段的值，取值范围为3～15。

**[admin-local**]：指定Scope字段为管理本地范围，对应的Scope值为4。

**[global**]：指定Scope字段为全局范围，对应的Scope值为14。

**[organization-local**]：指定Scope字段为机构本地范围，对应的Scope值为8。

**[site-local**]：指定Scope字段为站点本地范围，对应的Scope值为5。

【使用指导】

·执行本命令不需要使能IPv6组播路由。

·IPv6组播转发边界为指定地址范围或Scope值的IPv6组播组划定了边界条件，如果IPv6组播报文的目的地址与边界条件匹配，就停止转发。

·一个接口可以作为不同地址范围的IPv6组播组的转发边界，即允许在同一接口上多次执行本命令为不同地址范围的IPv6组播组设定转发边界；但一个接口只能作为特定Scope值的IPv6组播组的转发边界，若在同一接口上多次执行本命令为不同Scope值的IPv6组播组设定转发边界，则只有最后一次的配置生效。

·假设A和B为不同地址范围的IPv6组播组的集合，且B是A的真子集：如果接口先配置为A的转发边界，再配置为B的转发边界，则该接口仍然为A的转发边界；如果接口先配置为B的转发边界，再配置为A的转发边界，则该接口将变为A的转发边界。

【举例】

·路由应用

\# 将接口GigabitEthernet1/0/1配置为地址范围为FF03::/16的IPv6组播组的转发边界。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 multicast boundary ff03:: 16

\# 将接口GigabitEthernet1/0/1配置为Scope值为4的IPv6组播组的转发边界。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 multicast boundary scope 4

·交换应用

\# 将接口Vlan-interface100配置为地址范围为FF03::/16的IPv6组播组的转发边界。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 multicast boundary ff03:: 16

\# 将接口Vlan-interface100配置为Scope值为4的IPv6组播组的转发边界。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 multicast boundary scope 4

【相关命令】

·**display ipv6 multicast boundary**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- ipv6 multicast forwarding supervlan community**

------------------------------------------------------------------------

![说明](IPv6组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 multicast forwarding supervlan community**]命令用来配置IPv6组播数据在Super VLAN内的各Sub VLAN之间互通。

**[undo ipv6 multicast forwarding supervlan community**]命令用来恢复缺省情况。

【命令】

**[ipv6 multicast forwarding supervlan community**]

**[undo ipv6 multicast forwarding supervlan community**]

【缺省情况】

IPv6组播数据在Super VLAN内的各Sub VLAN之间隔离。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行本命令后必须清除IPv6组播转发表中所有以该VLAN接口为入接口的转发项，否则本命令将不能生效。

【举例】

\# 配置IPv6组播数据在Super VLAN 2内的各Sub VLAN之间互通。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 ipv6 multicast forwarding supervlan community

【相关命令】

·**reset ****ipv6 multicast forwarding-table**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- ipv6 multicast routing**

------------------------------------------------------------------------

**[ipv6 multicast routing**]命令用来使能IPv6组播路由，并进入IPv6 MRIB视图。

**[undo ipv6 multicast routing**]命令用来关闭IPv6组播路由。

【命令】

**[ipv6 multicast routing** [ **vpn-instance** *vpn-instance-name* ]]

**[undo ipv6 multicast routing** [ **vpn-instance** *vpn-instance-name* ]]

【缺省情况】

IPv6组播路由处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【使用指导】

·只有在公网实例或VPN实例中使能了IPv6组播路由，该实例中的其它三层IPv6组播功能才能生效；

·没有使能IPv6组播路由前，设备不转发任何IPv6组播报文。

【举例】

\# 使能公网实例中的IPv6组播路由，并进入公网实例的IPv6 MRIB视图。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6

\# 使能VPN实例mvpn中的IPv6组播路由，并进入该VPN实例的IPv6 MRIB视图。

\<Sysname\> system-view

Sysname ipv6 multicast routing vpn-instance mvpn

Sysname-mrib6-mvpn

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- ipv6 multicast rpf-fail-pkt bridging**

------------------------------------------------------------------------

![说明](IPv6组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 multicast rpf-fail-pkt bridging**]命令用来配置在当前VLAN内组播RPF检查失败的IPv6组播数据报文。

**[undo ipv6 multicast rpf-fail-pkt bridging**]命令用来恢复缺省情况。

【命令】

**[ipv6 multicast rpf-fail-pkt bridging**]

**[undo ipv6 multicast rpf-fail-pkt bridging**]

【缺省情况】

不在VLAN内组播RPF检查失败的IPv6组播数据报文。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·执行本命令不需要使能IPv6组播路由。

·执行本命令时，要先配置在所有VLAN内泛洪RPF检查失败的IPv6组播数据报文，并要求该VLAN内使能了MLD Snooping且对应VLAN接口上配置有IPv6三层组播协议（MLD或IPv6 PIM），否则本命令将不能生效。

·执行本命令后必须清除该VLAN内所有IPv6动态组播组的MLD Snooping转发表项，否则本命令将不能生效。

【举例】

\# 配置在VLAN 2内组播RPF检查失败的IPv6组播数据报文。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 ipv6 multicast rpf-fail-pkt bridging

【相关命令】

·**ipv6 multicast rpf-fail-pkt flooding**

·**reset mld-snooping group**（IP组播命令参考/MLD Snooping）

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- ipv6 multicast rpf-fail-pkt flooding**

------------------------------------------------------------------------

![说明](IPv6组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 multicast rpf-fail-pkt flooding**]命令用来配置在所有VLAN内泛洪RPF检查失败的IPv6组播数据报文。

**[undo ipv6 multicast rpf-fail-pkt flooding**]命令用来恢复缺省情况。

【命令】

**[ipv6 multicast rpf-fail-pkt flooding**]

**[undo ipv6 multicast rpf-fail-pkt flooding**]

【缺省情况】

不在VLAN内泛洪RPF检查失败的IPv6组播数据报文。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·执行本命令不需要使能IPv6组播路由。

·执行本命令后必须清除IPv6组播转发表中的所有转发项，否则本命令将不能生效。

【举例】

\# 配置在所有VLAN内泛洪RPF检查失败的IPv6组播数据报文。

\<Sysname\> system-view

Sysname ipv6 multicast rpf-fail-pkt flooding

【相关命令】

·**reset ipv6 multicast forwarding-table**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- ipv6 multicast rpf-fail-pkt trap-to-cpu**

------------------------------------------------------------------------

![说明](IPv6组播路由与转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 multicast rpf-fail-pkt trap-to-cpu**]命令用来配置把RPF检查失败的IPv6组播数据报文上送CPU处理。

**[undo ipv6 multicast rpf-fail-pkt trap-to-cpu**]命令用来恢复缺省情况。

【命令】

**[ipv6 multicast rpf-fail-pkt trap-to-cpu**]

**[undo ipv6 multicast rpf-fail-pkt trap-to-cpu**]

【缺省情况】

不把RPF检查失败的IPv6组播数据报文上送CPU处理。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·执行本命令不需要使能IPv6组播路由。

·执行本命令后必须清除IPv6组播转发表中的所有转发项，否则本命令将不能生效。

【举例】

\# 配置把RPF检查失败的IPv6组播数据报文上送CPU处理。

\<Sysname\> system-view

Sysname ipv6 multicast rpf-fail-pkt trap-to-cpu

【相关命令】

·**reset ipv6 multicast forwarding-table**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- load-splitting (IPv6 MRIB view)**

------------------------------------------------------------------------

**[load-splitting**]命令用来配置对IPv6组播流量进行负载分担。

**[undo load-splitting**]命令用来恢复缺省情况。

【命令】

**[load-splitting**[ { **source** \| **source-group** }]]

**[undo load-splitting**]

【缺省情况】

不对IPv6组播流量进行负载分担。

【视图】

IPv6 MRIB视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[source**]：指定仅根据IPv6组播源对IPv6组播流量进行负载分担。

**[source-group**]：指定同时根据IPv6组播源与IPv6组播组对IPv6组播流量进行负载分担。

【使用指导】

本命令对IPv6双向PIM不生效。

【举例】

\# 在公网实例中配置仅根据IPv6组播源对IPv6组播流量进行负载分担。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 load-splitting source

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- longest-match (IPv6 MRIB view)**

------------------------------------------------------------------------

**[longest-match**]命令用来配置按照最长匹配来选择RPF路由，即选择掩码最长的路由作为RPF路由。

**[undo longest-match**]命令用来恢复缺省情况。

【命令】

**[longest-match**]

**[undo longest-match**]

【缺省情况】

选择路由优先级最高的路由作为RPF路由。

【视图】

IPv6 MRIB视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在公网实例中配置按照最长匹配原则选择RPF路由。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 longest-match

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- reset ipv6 multicast forwarding event**

------------------------------------------------------------------------

**[reset ipv6 multicast forwarding event**]命令用来清除IPv6组播转发的事件统计信息。

【命令】

**[reset ipv6 multicast** [ **vpn-instance** *vpn-instance-name*  **forwarding event**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

【举例】

\# 清除公网实例IPv6组播转发的事件统计信息。

\<Sysname\> reset ipv6 multicast forwarding event

【相关命令】

·**display ipv6 multicast forwarding event**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- reset ipv6 multicast forwarding-table**

------------------------------------------------------------------------

**[reset ipv6 multicast forwarding-table**]命令用来清除IPv6组播转发表中的转发项。

【命令】

**[reset ipv6 multicast **[ **vpn-instance** *vpn-instance-name*  **forwarding-table** { { *ipv6-source-address*  *prefix*-*length*  \| *ipv6-group-address*  *prefix*-*length*  \| **incoming-interface** { *interface-type interface-number* } } \* \| **all** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

*[ipv6-source-address*]：IPv6组播源地址，显示包含指定组播源的IPv6组播转发项。

*[ipv6-group-address*]：IPv6组播组地址，显示指定组播组的IPv6组播转发项，取值范围为FFxy::/16，其中x和y均表示0～F的任意一个十六进制数。

*[prefix-length*]：指定IPv6组播组或IPv6组播源地址的前缀长度。对于IPv6组播组地址，其取值范围为8～128，缺省值为128；对于IPv6组播源地址，其取值范围为0～128，缺省值为128。

**[incoming-interface**]：清除指定入接口的IPv6组播转发项。

*[interface-type* *interface-number*]：清除指定接口类型和接口编号的入接口的IPv6组播转发项。

**[all**]：清除组播转发表中的所有IPv6组播转发项。

【使用指导】

清除IPv6组播转发表中的转发项后，IPv6组播路由表中的相应表项也将随之被删除。

【举例】

\# 从公网实例IPv6组播转发表中清除组播组FF0E::1的相关转发表项。

\<Sysname\> reset ipv6 multicast forwarding-table ff0e::1

【相关命令】

·**display ipv6 multicast forwarding-table**

**IPv6组播路由与转发 \-- IPv6组播路由与转发配置命令 \-- reset ipv6 multicast routing-table**

------------------------------------------------------------------------

**[reset ipv6 multicast routing-table**]命令用来清除IPv6组播路由表中的路由项。

【命令】

**[reset ipv6 multicast **[ **vpn-instance** *vpn-instance-name*  **routing-table** { { *ipv6-source-address*  *prefix-length*  \| *ipv6-group-address*  *prefix-length*  \| **incoming-interface** *interface-type interface-number* } \* \| **all** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：清除指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。

*[ipv6-source-address*]：IPv6组播源地址，清除包含指定IPv6组播源的IPv6组播路由项。

*[ipv6-group-address*]：IPv6组播组地址，清除指定IPv6组播组的IPv6组播路由项，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。

*[prefix-length*]：指定IPv6组播组或IPv6组播源地址的前缀长度。对于IPv6组播组地址，其取值范围为8～128，缺省值为128；对于IPv6组播源地址，其取值范围为0～128，缺省值为128。

**[incoming-interface**]：清除指定入接口的IPv6组播路由项。

*[interface-type interface-number*]：清除指定接口类型和接口编号的入接口的IPv6组播路由项。

**[all**]：清除IPv6组播路由表中的所有IPv6组播路由项。

【使用指导】

清除IPv6组播路由表中的路由项后，IPv6组播转发表中的相应表项也将被随之删除。

【举例】

\# 从公网实例IPv6组播路由表中清除组播组FF03::101的相关路由项。

\<Sysname\> reset ipv6 multicast routing-table ff03::101

【相关命令】

·**display ipv6 multicast routing-table**
