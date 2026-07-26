
**IPv6静态路由 \-- IPv6静态路由配置命令 \-- delete ipv6 static-routes all**

------------------------------------------------------------------------

**[delete ipv6 static-routes all**]命令用来删除所有IPv6静态路由。

【命令】

**[delete ipv6 ** **vpn-instance** *vpn-instance-name* ] **static-routes all**

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：删除指定VPN的所有IPv6静态路由。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则删除公网实例下的所有IPv6静态路由。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

使用本命令删除IPv6静态路由时，系统会提示确认，确认后才会删除所配置的所有IPv6静态路由。

【举例】

\# 删除所有IPv6静态路由。

\<Sysname\> system-view

Sysname delete ipv6 static-routes all

This will erase all IPv6 static routes and their configurations, you must reconf

igure all static routes.

Are you sure?[Y/N:y]

【相关命令】

·**ipv6 route-static**

**IPv6静态路由 \-- IPv6静态路由配置命令 \-- display ipv6 route-static nib**

------------------------------------------------------------------------

**[display ipv6 route-static nib**]命令用来显示IPv6静态路由下一跳信息。

【命令】

**[display ipv6 route-static nib ** *nib-id* ]  **verbose**

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

\# 显示IPv6静态路由邻居信息与下一跳信息。

\<Sysname\> display ipv6 route-static nib

Total number of nexthop(s): 35

      NibID: 0x21000000        Sequence: 0

       Type: 0x41               Flushed: Yes

   UserKey0: 0x0                VrfNthp: 0

   UserKey1: 0x0                Nexthop: 2::3

    IFIndex: 0x0              LocalAddr: ::

   TopoNthp: Invalid

      NibID: 0x21000001        Sequence: 1

       Type: 0x41               Flushed: Yes

   UserKey0: 0x0                VrfNthp: 0

   UserKey1: 0x0                Nexthop: 3::4

    IFIndex: 0x0              LocalAddr: ::

   TopoNthp: Invalid

\...\...（省略部分显示信息）

表1-1 display ipv6 route-static nib命令显示信息描述表

字段

描述

Total number of nexthop(s)

总的NIB个数

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

\# 显示IPv6静态路由邻居与下一跳的详细信息。

\<Sysname\> display ipv6 route-static nib verbose

Total number of nexthop(s): 35

      NibID: 0x21000000        Sequence: 0

       Type: 0x41               Flushed: Yes

   UserKey0: 0x0                VrfNthp: 0

   UserKey1: 0x0                Nexthop: 2::3

    IFIndex: 0x0              LocalAddr: ::

   TopoNthp: Invalid

     RefCnt: 1              FlushRefCnt: 0

       Flag: 0x12               Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 2::3

  RelyDepth: 2              RealNexthop: ::

  Interface: NULL0            LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

      NibID: 0x21000001        Sequence: 1

       Type: 0x41               Flushed: Yes

   UserKey0: 0x0                VrfNthp: 0

   UserKey1: 0x0                Nexthop: 3::4

    IFIndex: 0x0              LocalAddr: ::

   TopoNthp: Invalid

     RefCnt: 1              FlushRefCnt: 0

       Flag: 0x12               Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 3::4

  RelyDepth: 1              RealNexthop: ::

  Interface: NULL0            LocalAddr: ::

  TunnelCnt: 0                      Vrf: default-vrf

   TunnelID: N/A               Topology:

\...\...（省略部分显示信息）

表1-2 display ipv6 route-static nib verbose命令显示信息描述表

字段

描述

*[x* nexthop(s)]

下一跳具体值（前面数值表示下一跳个数）

Tnl-Policy

隧道策略

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

TunnelCnt

迭代到隧道的个数

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

**IPv6静态路由 \-- IPv6静态路由配置命令 \-- display ipv6 route-static routing-table**

------------------------------------------------------------------------

**[display ipv6 route-static routing-table**]命令用来显示IPv6静态路由表信息。

【命令】

**[display ipv6 route-static routing-table** [ **vpn-instance** *vpn-instance-name*   *ipv6-address prefix-length* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ipv6-address*]：目的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。

【举例】

\# 显示IPv6静态路由表信息。

\<Sysname\> display ipv6 route-static routing-table

Total number of routes: 5

Status: \* - valid

\*Destination: 1::1/128

       NibID: 0x21000000        NextHop: 2::2

   MainNibID: N/A             BkNextHop: N/A

     BkNibID: N/A             Interface: GigabitEthernet1/0/1

     TableID: 0xa           BkInterface: N/A

        Flag: 0x80d0a          BfdSrcIp: N/A

     DbIndex: 0x3            BfdIfIndex: 0x0

        Type: Normal        BfdVrfIndex: 0

  TrackIndex: 0xffffffff          Label: NULL

  Preference: 60            vrfIndexDst: 0

     BfdMode: N/A            vrfIndexNH: 0

   Permanent: 0                     Tag: 0

\*Destination: 1::1234/128

      NibID: 0x21000000        NextHop: 2::2

   MainNibID: N/A             BkNextHop: N/A

     BkNibID: N/A             Interface: NULL0

     TableID: 0xa           BkInterface: N/A

        Flag: 0x80d0a          BfdSrcIp: N/A

     DbIndex: 0x1            BfdIfIndex: 0x0

        Type: Normal        BfdVrfIndex: 0

  TrackIndex: 0xffffffff          Label: NULL

  Preference: 60            vrfIndexDst: 0

     BfdMode: N/A            vrfIndexNH: 0

   Permanent: 0                     Tag: 0

\...\...（省略部分显示信息）

\# 显示目的IPv6地址为1::1/128的IPv6静态路由信息。

\<Sysname\> display ipv6 route-static routing-table 1::1 128

\*Destination: 1::1/128

       NibID: 0x21000001        NextHop: 2::2

   MainNibID: N/A             BkNextHop: N/A

     BkNibID: N/A             Interface: GigabitEthernet1/0/1

     TableID: 0xa           BkInterface: N/A

        Flag: 0x80d0b          BfdSrcIp: N/A

     DbIndex: 0x2            BfdIfIndex: 0x0

        Type: Normal        BfdVrfIndex: 0

  TrackIndex: 0xffffffff          Label: NULL

  Preference: 60            vrfIndexDst: 0

     BfdMode: N/A            vrfIndexNH: 0

   Permanent: 0                     Tag: 429496729

表1-3 display ipv6 route-static routing-table命令显示信息描述表

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

目的所在VPN

vrfIndexNH

下一跳所在VPN

Permanent

永久静态路由标志（1表示永久静态路由）

Tag

路由标记

**IPv6静态路由 \-- IPv6静态路由配置命令 \-- ipv6 route-static**

------------------------------------------------------------------------

**[ipv6 route-static**]命令用来配置IPv6静态路由。

**[undo ipv6 route-static**]命令用来删除已配置的IPv6静态路由。

【命令】

**[ipv6 route-static** *ipv6-address prefix-length* { *interface-type* *interface-number* [ *next-hop-address*  [ **bfd** { **control-packet** \| **echo-packet** } [ **bfd-source** *ipv6-address* ] \| **permanent** ] \|  **vpn-instance** *d-vpn-instance-name*  *next-hop-address* [ **bfd** **control-packet** **bfd-source** *ipv6-address* \| **permanent** ] }  **preference** *preference-value*   **tag** *tag-value*   **description** *description-text* ]]

**[undo ipv6 route-static***ipv6-address prefix-length* [ *interface-type* *interface-number* [ *next-hop-address*  \|  **vpn-instance** *d-vpn-instance-name*  *next-hop-address* ]  **preference** *preference-value* ]]

**[ipv6 route-static** **vpn-instance** *s-vpn-instance-name* *ipv6-address prefix-length* { *interface-type interface-number* [ *next-hop-address*  [ **bfd** { **control-packet** \| **echo-packet** } [ **bfd-source** *ipv6-address* ] \| **permanent** ] \| *next-hop-address*  **public**  [ **bfd** **control-packet** **bfd-source** *ipv6-address* \| **permanent** ] \| **vpn-instance** *d-vpn-instance-name next-hop-address* [ **bfd** **control-packet** **bfd-source** *ipv6-address* \| **permanent** ] }  **preference** *preference-value*   **tag** *tag-value*   **description** *description-text* ]]

**[undo ipv6 route-static****vpn-instance** *s-vpn-instance-name* *ipv6-address* *prefix-length* [ *interface-type interface-number* [ *next-hop-address*  \| *next-hop-address*  **public**  \| **vpn-instance** *d-vpn-instance-name next-hop-address* ]  **preference** *preference-value* ]]

【缺省情况】

没有配置IPv6静态路由。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address prefix-length*]：IPv6地址及前缀长度。

*[interface-type interface-number*]：路由出接口的类型和编号。对于接口类型为非P2P接口（包括NBMA类型接口或广播类型接口，如以太网接口、VLAN接口等），必须指定下一跳地址。

*[next-hop-address*]：下一跳IPv6地址。

**[bfd**]：使能BFD（Bidirectional Forwarding Detection，双向转发检测）功能，对静态路由下一跳的可达性进行快速检测。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[control-packet**]：通过BFD控制报文方式实现BFD功能。

**[bfd-source** *ipv6-address*]：BFD源IPv6地址。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[echo-packet**]：通过BFD echo报文方式实现BFD功能。

**[permanent**]：指定为永久IPv6静态路由。即使在出接口down时，配置的永久IPv6静态路由仍然保持active状态。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[public**]：指定静态路由下一跳处于公网实例。

**[vpn-instance**] *d-vpn-instance-name*：指定目的VPN。*d-vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果指定目的VPN，IPv6静态路由将根据配置的下一跳IPv6地址在目的VPN中查找出接口。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[preference*** preference-value*]：路由的优先级，取值范围为1～255，缺省值为60。

**[tag ***tag-value*]：静态路由Tag值，用于标识该条静态路由，以便在路由策略中根据Tag对路由进行灵活的控制。*tag-value*的取值范围为1～4294967295，缺省值为0。关于路由策略的详细信息，请参见"三层技术-IP路由配置指导"中的"路由策略"。

**[description ***description-text*]：静态路由描述信息。*description-text*为1～60个字符的字符串，除"?"外，可以包含空格等特殊字符。

**[vpn-instance** *s-vpn-instance-name*]：指定源VPN。*s-vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。每个VPN都有自己的路由表，配置的IPv6静态路由将被加入指定VPN的路由表。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果配置的IPv6静态路由指定目的地址为::/0（前缀长度为0），则表示配置了一条IPv6缺省路由。如果报文的目的地址无法匹配路由表中的任何一项，设备将选择IPv6缺省路由来转发IPv6报文。

在配置静态路由时，可以指定出接口（*interface-type interface-number*），也可指定下一跳地址（*next-hop-address*），具体采用哪种方法，需要根据实际情况而定：

·如果出接口类型为广播（如以太网接口、VLAN接口等）或者NBMA类型（如封装X.25或者帧中继的接口等），必须指定下一跳地址。

·如果出接口类型为点到点类型（如串口等），配置时可以只指定出接口，不指定下一跳地址。这样，即使对端地址发生了变化也无须改变配置。

配置IPv6静态路由与BFD联动时，需要注意的是：

·对于直连下一跳，当指定的出接口类型为非P2P接口时，建议用户通过**bfd-source**命令指定BFD源IPv6地址，该地址必须为出接口的IPv6地址，且与下一跳IPv6地址处在同一网段。如果下一跳IPv6地址指定的是链路本地地址，本参数也必须是链路本地地址。

·对于直连下一跳或者非直连下一跳，如果要指定BFD源IPv6地址，那么下一跳IPv6地址和BFD源IPv6地址必须成对配置，即本端指定的下一跳IPv6地址是对端的BFD源IPv6地址，本端指定的BFD源IPv6地址是对端的下一跳IPv6地址。

配置IPv6静态路由时需要注意的是：

·路由振荡时，使能BFD检测功能可能会加剧振荡，需谨慎使用。关于BFD的详细介绍，请参考"可靠性配置指导"中的"BFD"。

·配置BFD echo报文方式时，下一跳IPv6地址必须为全球单播地址。

·参数**permanent**不能和**bfd**、**track**一起进行配置。

【**举例】**

\# 配置IPv6静态路由，该路由的目的地址为1:1:2::/64，下一跳地址为1:1:3::1。

\<Sysname\> system-view

Sysname ipv6 route-static 1:1:2:: 64 1:1:3::1

【相关命令】

·**display ipv6 routing-table protocol**（三层技术-IP路由命令参考/IP路由基础）

**IPv6静态路由 \-- IPv6静态路由配置命令 \-- ipv6 route-static default-preference**

------------------------------------------------------------------------

**[ipv6 route-static default-preference**]命令用来配置IPv6静态路由的缺省优先级。

**[undo ipv6 route-static default-preference**]命令用来恢复缺省情况。

【命令】

**[ipv6 route-static default-preference ***default-preference-value*]

**[undo ipv6 route-static default-preference**]

【缺省情况】

IPv6静态路由的缺省优先级为60。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[default-preference-value*]：IPv6静态路由缺省优先级的值，取值范围为1～255。

【使用指导】

·如果在配置IPv6静态路由时没有指定优先级，就会使用缺省优先级。

·重新配置缺省优先级后，新设置的缺省优先级仅对新增的IPv6静态路由有效。

【举例】

\# 配置IPv6静态路由的缺省优先级为120。

\<Sysname\> system-view

Sysname ipv6 route-static default-preference 120

【相关命令】

·**display ip****v6 routing-table protocol**（三层技术-IP路由命令参考/IP路由基础）

