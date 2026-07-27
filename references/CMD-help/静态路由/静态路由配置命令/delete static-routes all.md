<!-- CMD-INDEX
  delete static-routes all            | 系统视图             | L11
  display route-static nib            | 任意视图             | L61
  display route-static routing-table  | 任意视图             | L319
  ip route-static                     | 系统视图             | L557
  ip route-static default-preference  | 系统视图             | L671
  ip route-static fast-reroute auto   | 系统视图             | L721
  ip route-static primary-path-detect bfd echo | 系统视图             | L757
-->

**静态路由 \-- 静态路由配置命令 \-- delete static-routes all**

------------------------------------------------------------------------

**[delete static-routes all**]命令用来删除所有静态路由。

【命令】

**[delete **[[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **static-routes all**]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：删除指定拓扑的所有静态路由。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则表示删除公网的所有静态路由。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance*** vpn-instance-name*]：删除指定VPN的所有静态路由。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示删除公网的所有静态路由。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·使用本命令删除静态路由时，系统会提示确认，确认后才会删除所配置的所有静态路由。

·使用**undo ip route-static**命令可以删除一条静态路由，而使用**delete static-routes all**命令可以删除包括缺省路由在内的所有静态路由。

【举例】

\# 删除所有静态路由。

\<Sysname\> system-view

Sysname delete static-routes all

This will erase all IPv4 static routes and their configurations, you must reconf

igure all static routes.

Are you sure?[Y/N:y]

【相关命令】

·**ip route-static**

**静态路由 \-- 静态路由配置命令 \-- display route-static nib**

------------------------------------------------------------------------

**[display route-static nib**]命令用来显示静态路由下一跳信息。

【命令】

**[display route-static nib ** *nib-id* ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[nib-id*]：路由邻居ID值，取值范围1～FFFFFFFF。

**[verbose**]：显示详细信息。如果未指定本参数，则显示概要信息。

【举例】

\# 显示静态路由下一跳信息。

\<Sysname\> display route-static nib

Total number of nexthop(s): 44

      NibID: 0x11000000        Sequence: 0

       Type: 0x21               Flushed: Yes

   UserKey0: 0x111              VrfNthp: 0

   UserKey1: 0x0                Nexthop: 0.0.0.0

    IFIndex: 0x111            LocalAddr: 0.0.0.0

   TopoNthp: 0

      NibID: 0x11000001        Sequence: 1

       Type: 0x41               Flushed: Yes

   UserKey0: 0x0                VrfNthp: 5

   UserKey1: 0x0                Nexthop: 2.2.2.2

    IFIndex: 0x0              LocalAddr: 0.0.0.0

   TopoNthp: 0

\...\...（省略部分显示信息）

表1-1 display route-static nib命令显示信息描述表

字段

描述

Total number of nexthop(s)

总的下一跳个数

NibID

NIB ID号

Sequence

NIB序列号

Type

NIB类型

Flushed

是否下刷FIB

UserKey0

NIB协议保留数据1

UserKey1

NIB协议保留数据2

VrfNthp

下一跳所在VPN

Nexthop

下一跳信息

IFIndex

接口索引

LocalAddr

本地接口地址

TopoNthp

下一跳所在拓扑，0为公网拓扑（目前IPv6不支持子拓扑，显示为Invalid）

\# 显示静态路由下一跳详细信息。

\<Sysname\> display route-static nib verbose

Total number of nexthop(s): 44

      NibID: 0x11000000        Sequence: 0

       Type: 0x21               Flushed: Yes

   UserKey0: 0x111              VrfNthp: 0

   UserKey1: 0x0                Nexthop: 0.0.0.0

    IFIndex: 0x111            LocalAddr: 0.0.0.0

   TopoNthp: 0

     RefCnt: 2              FlushRefCnt: 0

       Flag: 0x2                Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 0.0.0.0

  RelyDepth: 0              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

      NibID: 0x11000001        Sequence: 1

       Type: 0x41               Flushed: Yes

   UserKey0: 0x0                VrfNthp: 5

   UserKey1: 0x0                Nexthop: 2.2.2.2

    IFIndex: 0x0              LocalAddr: 0.0.0.0

   TopoNthp: 0

     RefCnt: 1              FlushRefCnt: 0

       Flag: 0x12               Version: 1

 2 nexthop(s):

PrefixIndex: 0              OrigNexthop: 2.2.2.2

  RelyDepth: 7              RealNexthop: 8.8.8.8

  Interface: Dia0             LocalAddr: 12.12.12.12

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

PrefixIndex: 0              OrigNexthop: 2.2.2.2

  RelyDepth: 9              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology: base

\...\...（省略部分显示信息）

表1-2 display route-static nib verbose命令显示信息描述表

字段

描述

*[x* nexthop (s)]

下一跳具体值（前面数值表示下一跳个数）

PrefixIndex

等价时下一跳序号

OrigNexthop

原始下一跳

RelyDepth

迭代深度

RealNexthop

真实下一跳

Interface

出接口

localAddr

本地接口地址

TunnelCnt

迭代到隧道的个数

Vrf

实例名

TunnelID

迭代到隧道的ID

Topology

拓扑名称，base为公网拓扑（目前IPv6不支持子拓扑，显示为空）

RefCnt

下一跳信息的引用计数

FlushRefCnt

下一跳信息的下刷引用计数

Flag

下一跳信息的标志位

Version

下一跳信息的版本号

**静态路由 \-- 静态路由配置命令 \-- display route-static routing-table**

------------------------------------------------------------------------

**[display route-static routing-table**]命令用来显示静态路由表信息。

【命令】

**[display route-static routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name*   *ip-address* { *mask-length* \| *mask* } ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ip-address*]：目的IP地址，点分十进制。

*[mask-length/mask*]：IP地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为0～32。

【举例】

\# 显示静态路由表信息。

\<Sysname\> display route-static routing-table

Total number of routes: 24

Status: \* - valid

\*Destination: 0.0.0.0/0

       NibID: 0x1100000a         NextHop: 2.2.2.10

   MainNibID: N/A              BkNextHop: N/A

     BkNibID: N/A              Interface: N/A

     TableID: 0x2            BkInterface: N/A

        Flag: 0x82d01           BfdSrcIp: N/A

     DbIndex: 0xd             BfdIfIndex: 0x0

        Type: Normal         BfdVrfIndex: 0

  TrackIndex: 0xffffffff           Label: NULL

  Preference: 60             vrfIndexDst: 0

     BfdMode: N/A             vrfIndexNH: 0

   Permanent: 0                      Tag: 0

 Destination: 0.0.0.0/0

       NibID: 0x1100000b         NextHop: 2.2.2.11

   MainNibID: N/A              BkNextHop: N/A

     BkNibID: N/A              Interface: N/A

     TableID: 0x2            BkInterface: N/A

        Flag: 0x82d01           BfdSrcIp: N/A

     DbIndex: 0xd             BfdIfIndex: 0x0

        Type: Normal         BfdVrfIndex: 0

  TrackIndex: 0xffffffff           Label: NULL

  Preference: 60             vrfIndexDst: 0

     BfdMode: N/A             vrfIndexNH: 0

   Permanent: 0                      Tag: 0

\...\...（省略部分显示信息）

\# 显示目的地址为1.2.3.4/32的静态路由信息。

\<Sysname\> display route-static routing-table 1.2.3.4 32

\*Destination: 1.2.3.4/32

       NibID: 0x11000017         NextHop: 4.4.4.4

   MainNibID: 0x11000015       BkNextHop: 5.5.5.5

     BkNibID: 0x11000016       Interface: GigabitEthernet1/0/1

     TableID: 0x2            BkInterface: GigabitEthernet1/0/2

        Flag: 0xa8d0b           BfdSrcIp: N/A

     DbIndex: 0x17            BfdIfIndex: 0x0

        Type: Normal         BfdVrfIndex: 0

  TrackIndex: 0xffffffff           Label: NULL

  Preference: 60             vrfIndexDst: 0

     BfdMode: N/A             vrfIndexNH: 0

   Permanent: 0                      Tag: 0

表1-3 display route-static routing-table命令显示信息描述表

字段

描述

Total number of routes

总的路由条数

Destination

目的地址/掩码

NibID

下一跳信息ID

MainNibID

FRR静态路由主下一跳信息ID

BkNibID

FRR静态路由备下一跳信息ID

NextHop

此路由的下一跳地址

BkNextHop

此路由的备份下一跳地址

Interface

出接口，即到该目的网段的数据包将从此接口发出

BkInterface

备份出接口

TableID

路由所在的表ID

Flag

路由标志位

DbIndex

路由所在DB的DB索引

Type

路由类型：

·Normal：普通类型的静态路由

·DHCP：DHCP类型的静态路由

·NAT：NAT类型的静态路由

·IPsec：IPsec类型的静态路由

BfdSrcIp

BFD非直连会话源地址

BfdIfIndex

BFD使用的接口索引

BfdVrfIndex

BFD所在VPN实例索引

BfdMode

BFD模式：

·N/A：未配置BFD会话

·Ctrl：控制报文方式的BFD会话

·Echo：echo报文方式的BFD会话

TrackIndex

NQA Track索引

Label

标签

Preference

路由优先级

vrfIndexDst

目的所在VPN索引

vrfIndexNH

下一跳所在VPN索引

Permanent

永久静态路由标志（1表示永久静态路由）

Tag

路由标记

**静态路由 \-- 静态路由配置命令 \-- ip route-static**

------------------------------------------------------------------------

**[ip route-static**]命令用来配置静态路由。

**[undo ip route-static**]命令用来删除已配置的静态路由。

【命令】

**[ip**[ **route-static** *dest-address* { *mask-length* \| *mask* } { *interface-type* *interface-number* [ *next-hop-address* ]  **backup-interface** *interface-type* *interface-number* [ **backup-nexthop** *backup-nexthop-address*   **permanent**  \| **bfd** { **control-packet** \| **echo-packet** } \| **permanent** ] \| *next-hop-address* [ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* ] \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* [ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* ] }  **preference** *preference-value*   **tag** *tag-value*   **description** *description-text* ]]

**[undo** **ip** **route-static**[ *dest-address* { *mask-length* \| *mask* } [ *interface-type* *interface-number* [ *next-hop-address* ] \| *next-hop-address* \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* ]  **preference** *preference-value* ]]

**[ip route-static**[ **vpn-instance** *s-vpn-instance-name* *dest-address* { *mask-length* \| *mask* } { *interface-type* *interface-number* [ *next-hop-address* ]  **backup-interface** *interface-type* *interface-number* [ **backup-nexthop** *backup-nexthop-address*   **permanent**  \| **bfd** { **control-packet** \| **echo-packet** } \| **permanent** ] \| *next-hop-address*  **public**  [ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* ] \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* [ **bfd** **control-packet** **bfd-source** *ip-address* \| **permanent** \| **track** *track-entry-number* ] }  **preference** *preference-value*   **tag** *tag-value*   **description** *description-text* ]]

**[undo** **ip** **route-static** **vpn-instance**[ *s-vpn-instance-name* *dest-address* { *mask-length* \| *mask* } [ *interface-type* *interface-number* [ *next-hop-address* ] \| *next-hop-address*  **public**  \| **vpn-instance** *d-vpn-instance-name* *next-hop-address* ]  **preference** *preference-value* ]]

**[ip route-static**[ **topology** *topo-name* *dest-address* { *mask* \| *mask-length* } { *next-hop-address* \| *interface-type* *interface-number* [ *next-hop-address* [ **backup-interface** *interface-type* *interface-number* **backup-nexthop** *backup-nexthop-address* ] ] }  **preference** *preference-value*   **tag** *tag-value*   **description** *description-text* ]]

**[undo** **ip** **route-static** **topology**[ *topo-name* *dest-address* { *mask* \| *mask-length* } [ *next-hop-address* \| *interface-type* *interface-number* [ *next-hop-address* ] ]  **preference** *preference-value* ]]

【缺省情况】

没有配置静态路由。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *s-vpn-instance-name*]：指定源VPN。*s-vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。每个VPN都有自己的路由表，配置的静态路由将被加入指定VPN的路由表。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[topology** *topo-name*]：指定拓扑。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。每个拓扑都有自己的路由表，配置的静态路由将被加入指定拓扑的路由表。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[dest-address*]：静态路由的目的IP地址，点分十进制格式。

*[mask-length/mask*]：IP地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为0～32。

**[vpn-instance**]* d-vpn-instance-name*：指定目的VPN。*d-vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果指定目的VPN，静态路由将根据配置的*next-hop-address*在目的VPN中查找出接口。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-type interface-number*]：指定静态路由的出接口类型和接口号。在指定静态路由的出接口类型和接口号时需要注意的事项，详见使用指导。

*[next-hop-address*]：指定路由的下一跳的IP地址，点分十进制格式。在指定路由的下一跳的IP地址时需要注意的事项，详见使用指导。

**[backup-interface*** interface-type interface-number*]：备份出接口。对于备份出接口为非P2P类型的接口时（包括NBMA类型接口或广播类型接口，如以太网接口、VLAN接口等），必须同时指定其对应的备份下一跳地址。*interface-type interface-number*为指定的接口类型和编号。

**[backup-nexthop***backup-nexthop-address*]：备份下一跳地址。

**[bfd**]：使能BFD（Bidirectional Forwarding Detection，双向转发检测）功能，对静态路由下一跳的可达性进行快速检测，当下一跳不可达时可以快速切换到备份路由。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[control-packet**]：通过BFD控制报文方式实现BFD功能。

**[bfd-source** *ip-address*]：BFD源IP地址。建议配置为Loopback接口IP地址。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[permanent**]：指定为永久静态路由。即使在出接口down时，配置的永久静态路由仍然保持active状态。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[track **]*track-entry-number*：将静态路由与Track项相关联，*track-entry-number*为Track项的序号，取值范围为1～1024。关于Track的详细介绍，请参见"可靠性配置指导"中的"Track"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[echo-packet**]：通过BFD echo报文方式实现BFD功能。

**[public**]：指定静态路由下一跳处于公网实例。

**preference** *preference-value*：指定静态路由的优先级，取值范围为1～255，缺省值为60。

**[tag ***tag-value*]：静态路由Tag值，用于标识该条静态路由，以便在路由策略中根据Tag对路由进行灵活的控制。*tag-value*的取值范围为1～4294967295，缺省值为0。关于路由策略的详细信息，请参见"三层技术-IP路由配置指导"中的"路由策略"。

**[description ***description-text*]：配置的静态路由描述信息，取值范围为1～60个字符。除"?"外，可以包含空格等特殊字符。

【使用指导】

如果目的IP地址和掩码都为0.0.0.0（或掩码为0），则配置的路由为缺省路由。当没有匹配的路由表项时，将使用缺省路由进行报文转发。

对不同的优先级配置，可采用不同的路由管理策略。例如，为同一目的地配置多条路由，如果指定相同的优先级，则实现路由负载分担；如果指定不同的优先级，则实现路由备份。

配置静态路由时，可根据实际需要指定出接口或下一跳地址。需要注意的是：

·对于Null0接口，配置了出接口就不需要配置下一跳地址。

·对于点到点接口（如封装PPP协议的串口），配置时可以只指定出接口，不指定下一跳地址。这样，即使对端地址发生了变化也无须改变配置。

·对于NBMA、P2MP等接口（如封装X.25或者帧中继的接口），需要进行IP地址到链路层地址的映射，建议同时配置出接口和下一跳IP地址。

·对于广播类型接口（如以太网接口、VLAN接口），因为可能有多个下一跳，配置时必须同时指定出接口和下一跳IP地址。

配置静态路由时需要注意的是：

·路由振荡时，使能BFD检测功能可能会加剧振荡，需谨慎使用。关于BFD的详细介绍，请参考"可靠性配置指导"中的"BFD"。

·如果Track模块通过NQA探测私网静态路由中下一跳的可达性，静态路由下一跳的VPN实例号与NQA测试组配置的实例号必须相同，才能进行正常的探测。

·在静态路由进行迭代时，Track项监测的应该是静态路由真正的下一跳，而不是配置的下一跳。否则，可能导致错误地将有效路由判断为无效路由。

·参数**permanent**不能和**bfd**、**track**一起进行配置。

【**举例】**

\# 配置静态路由，其目的地址为1.1.1.1/24，指定下一跳为2.2.2.2，Tag值为45，描述信息为"for internet"。

\<Sysname\> system-view

Sysname ip route-static 1.1.1.1 24 2.2.2.2 tag 45 description for internet

【相关命令】

·**display ip routing-table protocol**（三层技术-IP路由命令参考/IP路由基础）

**静态路由 \-- 静态路由配置命令 \-- ip route-static default-preference**

------------------------------------------------------------------------

**[ip route-static default-preference**]命令用来配置静态路由的缺省优先级。

**[undo ip route-static default-preference**]命令用来恢复缺省情况。

【命令】

**[ip route-static default-preference ***default-preference-value*]

**[undo ip route-static default-preference**]

【缺省情况】

静态路由的缺省优先级为60。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[default-preference-value*]：静态路由缺省优先级的值，取值范围为1～255。

【使用指导】

·如果在配置静态路由时没有指定优先级，就会使用缺省优先级。

·重新配置缺省优先级后，新设置的缺省优先级仅对新增的静态路由有效。

【举例】

\# 配置静态路由的缺省优先级为120。

\<Sysname\> system-view

Sysname ip route-static default-preference 120

【相关命令】

·**display ip routing-table protocol**（三层技术-IP路由命令参考/IP路由基础）

**静态路由 \-- 静态路由配置命令 \-- ip route-static fast-reroute auto**

------------------------------------------------------------------------

**[ip route-static fast-reroute auto**]命令用来配置静态路由自动快速重路由功能。

**[undo ip route-static fast-reroute auto**]命令用来关闭静态路由自动快速重路由功能。

【命令】

**[ip route-static fast-reroute auto**]

**[undo ip route-static fast-reroute auto**]

【缺省情况】

静态路由自动快速重路由功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置静态路由自动快速重路由功能。

\<Sysname\> system-view

Sysname ip route-static fast-reroute auto

**静态路由 \-- 静态路由配置命令 \-- ip route-static primary-path-detect bfd echo**

------------------------------------------------------------------------

![说明](静态路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ip route-static primary-path-detect bfd echo**]命令用来使能静态路由中主用链路的BFD（Echo方式）检测功能。

**[undo ip route-static primary-path-detect bfd**]命令用来恢复缺省情况。

【命令】

**[ip route-static primary-path-detect bfd echo**]

**[undo ip route-static primary-path-detect bfd**]

【缺省情况】

静态路由中主用链路的BFD（Echo方式）检测功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置本功能后，静态路由的快速重路由特性中的主用链路将使用BFD（Echo方式）进行检测。

【举例】

\# 配置静态路由快速重路由特性中主用链路使能BFD（Echo方式）功能。

\<Sysname\> system-view

Sysname ip route-static 1.1.1.1 32 gigabitethernet 1/0/1 2.2.2.2 backup-interface gigabitethernet 1/0/2 backup-nexthop 3.3.3.3

Sysname ip route-static primary-path-detect bfd echo

