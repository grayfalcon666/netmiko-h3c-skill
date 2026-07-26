
**IP路由基础 \-- IP路由基础配置命令 \-- address-family ipv4**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[address-family ipv4**]命令用来创建RIB IPv4地址族，并进入RIB IPv4地址族视图。

**[undo address-family ipv4**]命令用来删除RIB IPv4地址族和RIB IPv4地址族视图下的所有配置。

【命令】

**[address-family ipv4**]

**[undo address-family ipv4**]

【缺省情况】

没有创建RIB IPv4地址族。

【视图】

RIB视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 创建RIB IPv4地址族，并进入RIB IPv4地址族视图。

\<Sysname\> system-view

Sysname rib

Sysname-rib address-family ipv4

Sysname-rib-ipv4

**IP路由基础 \-- IP路由基础配置命令 \-- address-family ipv6**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[address-family ipv6**]命令用来创建RIB IPv6地址族，并进入RIB IPv6地址族视图。

**[undo address-family**]命令用来删除RIB IPv6地址族和RIB IPv6地址族视图下的所有配置。

【命令】

**[address-family ipv6**]

**[undo address-family ipv6**]

【缺省情况】

没有创建RIB IPv6地址族。

【视图】

RIB视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 创建RIB IPv6地址族，并进入RIB IPv6地址族视图。

\<Sysname\> system-view

Sysname rib

Sysname-rib address-family ipv6

Sysname-rib-ipv6

**IP路由基础 \-- IP路由基础配置命令 \-- display ecmp mode**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ecmp mode**]命令用来显示IPv4等价路由模式信息。

【命令】

**[display ecmp mode**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IPv4等价路由模式信息。

\<Sysname\> display ecmp mode

  ECMP-mode in use: Default

  ECMP-mode at the next reboot: Enhanced

表1-1 display ecmp mode命令显示信息描述表

字段

描述

ECMP-mode in use

当前ECMP模式

ECMP-mode at the next reboot

下次启动后ECMP模式

**IP路由基础 \-- IP路由基础配置命令 \-- display ip routing-table**

------------------------------------------------------------------------

**[display ip routing-table**]命令用来显示路由表的信息。

【命令】

**[display ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ]  **verbose** ]]

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

**[verbose**]：显示全部路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。

【举例】

\# 显示路由表中当前激活路由的概要信息。

\<Sysname\> display ip routing-table

Destinations : 13        Routes : 13

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

0.0.0.0/32          Direct 0    0            127.0.0.1       InLoop0

1.1.1.0/24          Static 60   0            192.168.47.4    GE1/0/1

127.0.0.0/8         Direct 0    0            127.0.0.1       InLoop0

127.0.0.0/32        Direct 0    0            127.0.0.1       InLoop0

127.0.0.1/32        Direct 0    0            127.0.0.1       InLoop0

127.255.255.255/32  Direct 0    0            127.0.0.1       InLoop0

192.168.1.0/24      Direct 0    0            192.168.1.40    Vlan11

192.168.1.0/32      Direct 0    0            192.168.1.40    Vlan11

192.168.1.40/32     Direct 0    0            127.0.0.1       InLoop0

192.168.1.255/32    Direct 0    0            192.168.1.40    Vlan11

224.0.0.0/4         Direct 0    0            0.0.0.0         NULL0

224.0.0.0/24        Direct 0    0            0.0.0.0         NULL0

255.255.255.255/32  Direct 0    0            127.0.0.1       InLoop0

表1-1 display ip routing-table命令显示信息描述表

字段

描述

Destinations

目的地址个数

Routes

路由条数

Destination/Mask

目的地址/掩码长度

Proto

发现该路由的路由协议类型：

·O_INTRA：OSPF intra area

·O_INTER：OSPF inter area

·O_ASE1：OSPF external type 1

·O_ASE2：OSPF external type 2

·O_NSSA1：OSPF NSSA external type 1

·O_NSSA2：OSPF NSSA external type 2

·O_SUM：OSPF summary

·IS_L1：IS-IS level-1

·IS_L2：IS-IS level-2

·IS_SUM：IS-IS summary

Pre

路由的优先级

Cost

路由的度量值

NextHop

此路由的下一跳地址

Interface

出接口，即到该目的网段的数据包将从此接口发出

Summary Count

路由数目

\# 显示路由表的全部详细信息。

\<Sysname\> display ip routing-table verbose

Destinations : 13        Routes : 13

Destination: 0.0.0.0/32

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 08h34m37s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0x2                 OrigAs: 0

      NibID: 0x10000000          LastAs: 0

     AttrID: 0xffffffff        Neighbor: 0.0.0.0

      Flags: 0x1000c        OrigNextHop: 127.0.0.1

      Label: NULL           RealNextHop: 127.0.0.1

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: InLoopBack0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

Destination: 1.1.1.0/24

   Protocol: Static          Process ID: 0

  SubProtID: 0x0                    Age: 04h20m37s

       Cost: 0               Preference: 60

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active Adv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0x2                 OrigAs: 0

      NibID: 0x10000003          LastAs: 0

     AttrID: 0xffffffff        Neighbor: 0.0.0.0

      Flags: 0x1008c        OrigNextHop: 192.168.47.4

      Label: NULL           RealNextHop: 192.168.47.4

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: GigabitEthernet1/0/1

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

\...\...（省略部分显示信息）

表1-2 display ip routing-table verbose命令显示信息描述表

字段

描述

Destinations

目的地址个数

Routes

路由条数

Destination

目的地址/掩码

Protocol

发现该路由的路由协议类型

Process ID

进程号

SubProtID

路由子协议ID

Age

此路由在路由表中存在的时间

Cost

路由的度量值

Preference

路由的优先级

IpPre

IP优先级值

QosLocalID

QoS本地ID

Tag

路由标记

State

路由状态描述：

·Active：有效的单播路由

·Adv：允许对外发送的路由

·Inactive：非激活路由标志

·NoAdv：不允许发布的路由

·Vrrp：VRRP产生的路由

·Nat：NAT产生的路由

·TunE：Tunnel隧道的标志

OrigTblID

原始路由表ID

OrigVrf

路由所属的原始VPN

TableID

路由所在路由表的ID

OrigAs

初始AS号

NibID

下一跳ID

LastAs

最后AS号

AttrID

路由属性ID号

Neighbor

路由协议的邻居地址

Flags

路由标志位

OrigNextHop

此路由的下一跳地址

Label

标签

RealNextHop

路由真实下一跳

BkLabel

备份标签

BkNexthop

备份下一跳地址

Tunnel ID

隧道ID

Interface

出接口，即到该目的网段的数据包将从此接口发出

BkTunnel ID

备份隧道ID

BkInterface

备份出接口

FtnIndex

FTN表项索引

TrafficIndex

流量统计索引值，取值范围为1～64，N/A表示无效值

Connector

表示BGP为MD VPN特性所携带的Connector属性，具体取值为BGP对等体在交换VPN-IPv4路由时携带源PE的地址，N/A表示没有该属性

Summary Count

路由数目

**IP路由基础 \-- IP路由基础配置命令 \-- display ip routing-table acl**

------------------------------------------------------------------------

**[display ip routing-table acl**]命令用来显示通过指定ACL过滤的路由信息。

【命令】

**[display ip routing-table **[[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **acl** *acl-number*  **verbose** ]]

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

*[acl-number*]：基本ACL的编号，取值范围为2000～2999。

**[verbose**]：显示通过指定ACL过滤的所有路由的详细信息。如果未指定本参数，将只显示通过指定ACL过滤的激活路由的概要信息。

【使用指导】

如果用户指定的ACL不存在或者ACL中没有任何规则，将显示所有的路由信息。

【举例】

\# 配置ACL 2000，并设置路由过滤规则。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 192.168.1.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 rule deny source any

\# 显示通过ACL 2000过滤的激活路由的概要信息。

Sysname-acl-basic-2000 display ip routing-table acl 2000

Routes Matched by Access control list : 2000

Summary Count : 4

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

192.168.1.0/24      Direct 0    0            192.168.1.111   GE1/0/1

192.168.1.0/32      Direct 0    0            192.168.1.111   GE1/0/1

192.168.1.111/32    Direct 0    0            127.0.0.1       InLoop0

192.168.1.255/32    Direct 0    0            192.168.1.111   GE1/0/1

以上显示信息解释请参见 表1-1(?-935850768#_Ref167867063)。

\# 显示通过ACL 2000过滤的所有路由的详细信息。

\<Sysname\> display ip routing-table acl 2000 verbose

Routes Matched by Access control list : 2000

Summary Count : 4

Destination: 192.168.1.0/24

   Protocol: Direct          Process ID: 0

  SubProtID: 0x1                    Age: 04h20m37s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active Adv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0x2                 OrigAs: 0

      NibID: 0x10000003          LastAs: 0

     AttrID: 0xffffffff        Neighbor: 0.0.0.0

      Flags: 0x10080        OrigNextHop: 192.168.1.111

      Label: NULL           RealNextHop: 192.168.1.111

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: GigabitEthernet1/0/1

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

Destination: 192.168.1.0/32

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 04h20m37s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0x2                 OrigAs: 0

      NibID: 0x10000003          LastAs: 0

     AttrID: 0xffffffff        Neighbor: 0.0.0.0

      Flags: 0x1008c        OrigNextHop: 192.168.1.111

      Label: NULL           RealNextHop: 192.168.1.111

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: GigabitEthernet1/0/1

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

Destination: 192.168.1.111/32

   Protocol: Direct          Process ID: 0

  SubProtID: 0x1                    Age: 04h20m37s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0x2                 OrigAs: 0

      NibID: 0x10000000          LastAs: 0

     AttrID: 0xffffffff        Neighbor: 0.0.0.0

      Flags: 0x10004        OrigNextHop: 127.0.0.1

      Label: NULL           RealNextHop: 127.0.0.1

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: InLoopBack0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

Destination: 192.168.1.255/32

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 04h20m37s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0x2                 OrigAs: 0

      NibID: 0x10000003          LastAs: 0

     AttrID: 0xffffffff        Neighbor: 0.0.0.0

      Flags: 0x1008c        OrigNextHop: 192.168.1.111

      Label: NULL           RealNextHop: 192.168.1.111

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: GigabitEthernet1/0/1

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

以上显示信息解释请参见 表1-2(?-935850768#_Ref166916179)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ip routing-table ip-address**

------------------------------------------------------------------------

**[display ip routing-table ***ip-address*]命令用来显示指定目的地址的路由信息。

**[display ip routing-table ***ip-address1 ***to*** ip-address2*]命令用来显示指定目的地址范围内的路由信息。

【命令】

**[display ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] *ip-address* [ *mask* \| *mask-length* ]  **longer-match**   **verbose** ]]

**[display ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] *ip-address1* **to** *ip-address2*  **verbose** ]]

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

*[ip-address*]：目的IP地址，点分十进制格式。

*[mask/mask-length*]：IP地址掩码，点分十进制格式或以整数形式表示的长度，当用整数时，取值范围为0～32。

**[longer-match**]：匹配掩码更长的路由。

*[ip-address1* **to** *ip-address2*]：IP地址范围。*ip-address1*和*ip-address2*共同决定一个地址范围，只有地址在此范围内的路由才会被显示。

**[verbose**]：显示全部路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。

【使用指导】

使用不同的可选参数，命令的输出也不相同，以下是对该命令不同形式的输出说明：

(1)**display ip routing-table** *ip-address*

显示满足如下条件的所有激活路由：

·用户输入的目的IP地址同路由表中各条路由的子网掩码值进行与运算；

·路由表中各条路由的目的IP地址同其自身子网掩码值进行与运算；

·两次运算结果相同的路由条目将被显示出来。

(2)**display ip routing-table** *ip-address* *mask*

显示满足如下条件的所有激活路由：

·用户输入的目的IP地址同用户输入的子网掩码值进行与运算；

·路由表中各条路由的目的IP地址同用户输入的子网掩码值进行与运算；

·两次运算结果相同，并且掩码小于等于用户输入的子网掩码的路由条目将被显示出来。

(3)**display ip routing-table** *ip-address* **longer-match**

显示满足如下条件的所有激活路由：

·用户输入的目的IP地址同路由表中各条路由的子网掩码值进行与运算；

·路由表中各条路由的目的IP地址同其自身子网掩码值进行与运算；

·两次运算结果相同，并且子网掩码最长匹配的路由条目将被显示出来。

(4)**display ip routing-table** *ip-address mask* **longer-match**

显示满足如下条件的所有激活路由：

·用户输入的目的IP地址同用户输入的子网掩码值进行与运算；

·路由表中各条路由的目的IP地址同用户输入的子网掩码值进行与运算；

·两次运算结果相同，掩码小于等于用户输入的子网掩码，同时子网掩码最长匹配的路由条目将被显示出来。

(5)**display ip routing-table** *ip-address1* **to** *ip-address2*

显示*ip-address1*/32到*ip-address2*/32之间的激活路由，目的地址与掩码（32位）同时在指定范围内才会显示。

【举例】

\# 显示目的地址为11.0.0.1的路由信息。

\<Sysname\> display ip routing-table 11.0.0.1

Summary Count : 3

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

11.0.0.0/8          Static 60   0            0.0.0.0         NULL0

11.0.0.0/16         Static 60   0            0.0.0.0         NULL0

11.0.0.0/24         Static 60   0            0.0.0.0         NULL0

\# 显示目的地址/掩码为11.0.0.1/20的路由信息。

\<Sysname\> display ip routing-table 11.0.0.1 20

Summary Count : 2

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

11.0.0.0/8          Static 60   0            0.0.0.0         NULL0

11.0.0.0/16         Static 60   0            0.0.0.0         NULL0

\# 显示目的地址为11.0.0.1并且掩码最长匹配的路由信息。

\<Sysname\> display ip routing-table 11.0.0.1 longer-match

Summary Count : 1

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

11.0.0.0/24         Static 60   0            0.0.0.0         NULL0

\# 显示目的地址/掩码为11.0.0.1/20并且掩码最长匹配的路由信息。

\<Sysname\> display ip routing-table 11.0.0.1 20 longer-match

Summary Count : 1

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

11.0.0.0/16         Static 60   0            0.0.0.0         NULL0

\# 显示目的地址从1.1.1.0到5.5.5.0范围内的路由信息。

\<Sysname\> display ip routing-table 1.1.1.0 to 5.5.5.0

Summary Count : 6

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

1.1.1.1/32          Direct 0    0            127.0.0.1       InLoop0

2.2.2.0/24          Direct 0    0            2.2.2.1         Vlan2

3.3.3.0/24          Direct 0    0            3.3.3.1         GE1/0/2

3.3.3.1/32          Direct 0    0            127.0.0.1       InLoop0

4.4.4.0/24          Direct 0    0            4.4.4.1         GE1/0/1

4.4.4.1/32          Direct 0    0            127.0.0.1       InLoop0

以上显示信息的解释请参见 表1-1(?-935850768#_Ref167867063)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ip routing-table prefix-list**

------------------------------------------------------------------------

**[display ip routing-table prefix-list**]命令用来显示通过指定前缀列表过滤的路由信息。

【命令】

**[display ip routing-table **[[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **prefix-list** *prefix-list-name*  **verbose** ]]

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

*[prefix-list-name*]：前缀列表名称，为1～63个字符的字符串，区分大小写。

**[verbose**]：当使用该参数时，显示通过过滤规则的所有路由的详细信息。如果未指定本参数，将只显示通过过滤规则的激活路由的概要信息。

【使用指导】

如果指定的前缀列表不存在，将显示所有的路由信息。

【举例】

\# 配置地址前缀列表test允许前缀为1.1.1.0，掩码长度为24的路由通过。

\<Sysname\> system-view

Sysname ip prefix-list test permit 1.1.1.0 24

\# 显示通过前缀列表test过滤的激活路由的概要信息。

Sysname display ip routing-table prefix-list test

Routes Matched by Prefix list : test

Summary Count : 1

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

1.1.1.0/24          Direct 0    0            1.1.1.2         GE1/0/2

以上显示信息的解释请参见 表1-1(?-935850768#_Ref167867063)。

\# 显示通过前缀列表test过滤的所有路由的详细信息。

Sysname display ip routing-table prefix-list test verbose

Routes Matched by Prefix list : test

Summary Count : 1

Destination: 1.1.1.0/24

   Protocol: Direct          Process ID: 0

  SubProtID: 0x1                    Age: 04h20m37s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active Adv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0x2                 OrigAs: 0

      NibID: 0x10000003          LastAs: 0

     AttrID: 0xffffffff        Neighbor: 0.0.0.0

      Flags: 0x1008c        OrigNextHop: 1.1.1.2

      Label: NULL           RealNextHop: 1.1.1.2

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: GigabitEthernet1/0/2

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

以上显示信息的解释请参见 表1-2(?-935850768#_Ref166916179)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ip routing-table protocol**

------------------------------------------------------------------------

**[display ip routing-table** **protocol**]命令用来显示指定协议生成或发现的路由信息。

【命令】

**[display ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **protocol** *protocol* [ **inactive** \| **verbose** ]]]

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

*[protocol*]：显示指定路由协议的信息，包括**bgp**、**direct**、**isis**、**ospf**、**rip**和**static**。

**[inactive**]：显示未激活路由的信息。如果未指定本参数，则显示激活路由和未激活路由的信息。

**[verbose**]：当使用该参数时，显示路由的详细信息。如果未指定本参数，将显示路由的概要信息。

【举例】

\# 显示所有直连路由的概要信息。

\<Sysname\> display ip routing-table protocol direct

Summary Count : 13

Direct Routing Table Status : \<Active\>

Summary Count : 13

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

0.0.0.0/32          Direct 0    0            127.0.0.1       InLoop0

2.2.2.0/24          Direct 0    0            2.2.2.1         Vlan2

2.2.2.0/32          Direct 0    0            2.2.2.1         Vlan2

2.2.2.2/32          Direct 0    0            127.0.0.1       InLoop0

2.2.2.255/32        Direct 0    0            2.2.2.1         Vlan2

127.0.0.0/8         Direct 0    0            127.0.0.1       InLoop0

127.0.0.0/32        Direct 0    0            127.0.0.1       InLoop0

127.0.0.1/32        Direct 0    0            127.0.0.1       InLoop0

127.255.255.255/32  Direct 0    0            127.0.0.1       InLoop0

192.168.80.0/24     Direct 0    0            192.168.80.10   GE1/0/1

192.168.80.0/32     Direct 0    0            192.168.80.10   GE1/0/1

192.168.80.10/32    Direct 0    0            127.0.0.1       InLoop0

192.168.80.255/32   Direct 0    0            192.168.80.10   GE1/0/1

Direct Routing Table Status : \<Inactive\>

Summary Count : 0

\# 显示静态路由表。

\<Sysname\> display ip routing-table protocol static

Summary Count : 2

Static Routing Table Status : \<Active\>

Summary Count : 0

Static Routing Table Status : \<Inactive\>

Summary Count : 2

Destination/Mask    Proto  Pre  Cost         NextHop        Interface

1.2.3.0/24          Static 60   0            1.2.4.5        Vlan10

3.0.0.0/8           Static 60   0            2.2.2.2        GE1/0/1

以上显示信息的解释请参见 表1-1(?-935850768#_Ref167867063)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ip routing-table statistics**

------------------------------------------------------------------------

**[display ip routing-table statistics**]命令用来显示路由表中的综合路由统计信息。综合路由统计信息包括路由总数目、路由协议添加/删除路由数目、激活路由数目。

【命令】

**[display ip routing-table**[ [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] **statistics**]]

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

【举例】

\# 显示路由表中的综合路由统计信息。

\<Sysname\> display ip routing-table statistics

Proto      route       active      added       deleted

DIRECT     12          12          30          18

STATIC     3           3           5           2

RIP        0           0           0           0

OSPF       0           0           0           0

ISIS       0           0           0           0

BGP        0           0           0           0

Total      15          15          35          20

表1-3 display ip routing-table statistics命令显示信息描述表

字段

描述

Proto

路由协议

route

总的路由数目

active

活跃的、正在使用的路由数目

added

路由器启动后或在上一次清除路由表后，路由表中添加的路由数目

deleted

标记为删除的路由数目（此类路由在等待一段时间后会被释放）

Total

各种类型路由数目的总和

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 ecmp mode**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ipv6 ecmp-mode**]命令用来显示IPv6等价路由模式信息。

【命令】

**[display ipv6 ecmp mode**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IPv6等价路由模式信息。

\<Sysname\> display ipv6 ecmp mode

  IPv6 ECMP-mode in use: Default

  IPv6 ECMP-mode at the next reboot: Enhanced

表1-2 display ipv6 ecmp mode命令显示信息描述表

字段

描述

IPv6 ECMP-mode in use

当前IPv6 ECMP模式

IPv6 ECMP-mode at the next reboot

下次启动后IPv6 ECMP模式

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 rib attribute**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display ipv6 rib attribute**]命令用来显示IPv6 RIB的路由属性信息。

【命令】

**[display ipv6 rib attribute** [ *attribute-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[attribute-id*]：路由属性ID值，取值范围0～FFFFFFFF。

【举例】

\# 显示IPv6 RIB的路由属性信息。

\<Sysname\> display ipv6 rib attribute

Total number of attribute(s): 1

Detailed information of attribute 0x9:

                  Flag: 0x0

              Protocol: BGP4+

        Address family: IPv6

       Reference count: 0

      Local preference: 0

Ext-communities number: 0

 Ext-communities value: N/A

    Communities number: 0

     Communities value: N/A

        AS-path number: 0

         AS-path value: N/A

以上显示信息的解释请参见 表1-10(?172263077#_Ref343540137)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 rib graceful-restart**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display ipv6 rib graceful-restart**]命令用来显示IPv6 RIB的GR状态信息。

【命令】

**[display ipv6 rib graceful-restart**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IPv6 RIB的GR状态信息。

\<Sysname\> display ipv6 rib graceful-restart

RIB GR state     : Phase2-calculation end

RCOM GR State    : Flush end

Protocol GR state:

 No.  Protocol   Lifetime FD   State    Start/End

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 1    DIRECT6    480      29   End      No/No

 2    STATIC6    480      32   End      No/No

 3    ISISV6     480      30   End      No/No

 4    BGP4+      480      31   End      No/No

以上显示信息的解释请参见 表1-11(?-1663174259#_Ref335659994)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 rib nib**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display ipv6 rib nib**]命令用来显示IPv6 RIB的下一跳信息。

【命令】

**[display ipv6 rib nib ** **self-originated** ]  *nib-id*   **verbose**

**[display ipv6 rib nib protocol ***protocol-name* [ **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[self-originated**]：路由管理自己生成的下一跳。

*[nib-id*]：路由下一跳ID值，取值范围1～FFFFFFFF。

**[verbose**]：显示详细信息。如果未指定本参数，则显示概要信息。

**[protocol ***protocol-name*]：显示指定路由协议的下一跳信息，包括**bgp4+**、**direct6**、**isisv6**、**ospfv3**、**ripng**和**static6**。

【举例】

\# 显示IPv6 RIB的下一跳信息。

\<Sysname\> display ipv6 rib nib

Total number of nexthop(s): 151

      NibID: 0x20000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::

    IFIndex: 0x111            LocalAddr: ::

   TopoNthp: Invalid

      NibID: 0x20000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::1

    IFIndex: 0x112            LocalAddr: ::1

   TopoNthp: Invalid

\...\...（省略部分显示信息）

\# 显示IPv6 RIB下一跳的详细信息。

\<Sysname\> display ipv6 rib nib verbose

Total number of nexthop(s): 151

      NibID: 0x20000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::

    IFIndex: 0x111            LocalAddr: ::

   TopoNthp: Invalid

     RefCnt: 4              FlushRefCnt: 1

       Flag: 0x84               Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: ::

  RelyDepth: 0              RealNexthop: ::

  Interface: NULL0            LocalAddr: ::

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology:

      NibID: 0x20000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::1

    IFIndex: 0x112            LocalAddr: ::1

   TopoNthp: Invalid

     RefCnt: 4              FlushRefCnt: 1

       Flag: 0x84               Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: ::1

  RelyDepth: 0              RealNexthop: ::1

  Interface: InLoop0          LocalAddr: ::1

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology:

\...\...（省略部分显示信息）

以上显示信息的解释请参见表 1-12(?-577285439#_Ref335989228)和表 1-13(?-577285439#_Ref335989205)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 route-direct nib**

------------------------------------------------------------------------

**[display ipv6 route-direct nib**]命令用来显示IPv6直连路由下一跳信息。

【命令】

**[display ipv6 route-direct nib ** *nib-id* ]  **verbose**

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

\# 显示IPv6直连路由下一跳信息。

\<Sysname\> display ipv6 route-direct nib

Total number of nexthop(s): 115

      NibID: 0x20000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::

    IFIndex: 0x111            LocalAddr: ::

   TopoNthp: Invalid

      NibID: 0x20000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::1

    IFIndex: 0x112            LocalAddr: ::1

   TopoNthp: Invalid

\...\...（省略部分显示信息）

表1-4 display ipv6 route-direct nib命令显示信息描述表

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

\#显示IPv6直连路由下一跳详细信息。

\<Sysname\> display ipv6 route-direct nib verbose

Total number of nexthop(s): 115

      NibID: 0x20000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::

    IFIndex: 0x111            LocalAddr: ::

     RefCnt: 1              FlushRefCnt: 0

       Flag: 0x2                Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: ::

  RelyDepth: 0              RealNexthop: ::

  Interface: NULL0            LocalAddr: ::

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology:

      NibID: 0x20000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: ::1

    IFIndex: 0x112            LocalAddr: ::1

     RefCnt: 1              FlushRefCnt: 0

       Flag: 0x2                Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: ::1

  RelyDepth: 0              RealNexthop: ::1

  Interface: InLoop0          LocalAddr: ::1

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology:

\...\...（省略部分显示信息）

表1-5 display ipv6 route-direct nib verbose命令显示信息描述表

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

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 routing-table**

------------------------------------------------------------------------

**[display ipv6 routing-table**]命令用来显示IPv6路由表的信息。

【命令】

**[display ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示IPv6路由表的详细信息，包括激活路由和未激活路由。如果未指定本参数，将显示激活路由的概要信息。

【举例】

\# 显示当前路由表的概要信息。

\<Sysname\> display ipv6 routing-table

Destinations : 3 Routes : 3

Destination: ::1/128                                     Protocol  : Direct

NextHop    : ::1                                         Preference: 0

Interface  : InLoop0                                     Cost      : 0

Destination: FE80::/10                                   Protocol  : Direct

NextHop    : ::                                          Preference: 0

Interface  : InLoop0                                     Cost      : 0

Destination: FF00::/8                                    Protocol  : Direct

NextHop    : ::                                          Preference: 0

Interface  : NULL0                                       Cost      : 0

表1-6 display ipv6 routing-table命令显示信息描述表

字段

描述

Destinations

目的地址个数

Routes

路由条数

Destination

目的网络/主机的IPv6地址和前缀

NextHop

下一跳地址

Preference

路由优先级

Interface

出接口，即到该目的地址的数据包将从此接口发出

Protocol

发现该路由的路由协议类型：

·O_INTRA：OSPF intra area

·O_INTER：OSPF inter area

·O_ASE1：OSPF external type 1

·O_ASE2：OSPF external type 2

·O_NSSA1：OSPF NSSA external type 1

·O_NSSA2：OSPF NSSA external type 2

·O_SUM：OSPF summary

·IS_L1：IS-IS level-1

·IS_L2：IS-IS level-2

·IS_SUM：IS-IS summary

Cost

路由的开销值

Summary Count

路由数目

\# 显示路由表的详细路由信息。

\<Sysname\> display ipv6 routing-table verbose

Destinations : 3 Routes : 3

Destination: ::1/128

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 00h53m50s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0xa                 OrigAs: 0

      NibID: 0x20000000          LastAs: 0

     AttrID: 0xffffffff        Neighbor: ::

      Flags: 0x10004        OrigNextHop: ::1

      Label: NULL           RealNextHop: ::1

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: InLoopBack0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

Destination: FE80::/10

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 00h53m50s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0xa                 OrigAs: 0

      NibID: 0x20000003          LastAs: 0

     AttrID: 0xffffffff        Neighbor: ::

      Flags: 0x10084        OrigNextHop: ::

      Label: NULL           RealNextHop: ::

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: InLoop0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

Destination: FF00::/8

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 00h53m50s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0xa                 OrigAs: 0

      NibID: 0x20000001          LastAs: 0

     AttrID: 0xffffffff        Neighbor: ::

      Flags: 0x10014        OrigNextHop: ::

      Label: NULL           RealNextHop: ::

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: NULL0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

表1-7 display ipv6 routing-table verbose命令显示信息描述表

字段

描述

Destination

目的网络/主机的IPv6地址和前缀

Protocol

发现该路由的路由协议类型

Process ID

进程号

SubProtID

路由子协议ID

Age

此路由在路由表中存在的时间

Cost

路由的度量值

Preference

路由的优先级

IpPre

IP优先级值

QosLocalID

QoS本地ID

Tag

路由标记

State

路由状态描述：

·Active：有效的单播路由

·Adv：允许对外发送的路由

·Inactive：非激活路由标志

·NoAdv：不允许发布的路由

·Vrrp：VRRP产生的路由

·Nat：NAT产生的路由

·TunE：Tunnel隧道的标志

OrigTblID

原始路由表ID

OrigVrf

路由所属的原始VPN

TableID

路由所在路由表的ID

OrigAs

初始AS号

NibID

下一跳ID

LastAs

最后AS号

AttrID

路由属性ID号

Neighbor

路由协议的邻居地址

Flags

路由标志位

OrigNextHop

此路由的下一跳地址

Label

标签

RealNextHop

路由真实下一跳

BkLabel

备份标签

BkNexthop

备份下一跳地址

Tunnel ID

隧道ID

Interface

出接口，即到该目的网段的数据包将从此接口发出

BkTunnel ID

备份隧道ID

BkInterface

备份出接口

FtnIndex

FTN表项索引

TrafficIndex

流量统计索引值，取值范围为1～64，N/A表示无效值

Connector

表示BGP为MD VPN特性所携带的Connector属性，具体取值为BGP对等体在交换VPN-IPv4路由时携带源PE的地址，N/A表示没有该属性

Summary Count

路由数目

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 routing-table acl**

------------------------------------------------------------------------

**[display ipv6 routing-table acl**]命令用来显示通过指定IPv6 ACL过滤的IPv6路由信息。

【命令】

**[display ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] **acl** *acl-number*  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[acl6-number*]：基本IPv6 ACL编号，取值范围为2000～2999。

**[verbose**]：显示通过指定IPv6 ACL过滤的所有路由的详细信息。如果未指定本参数，只显示通过IPv6 ACL过滤的激活路由的概要信息。

【使用指导】

如果指定的IPv6 ACL不存在或者IPv6 ACL中没有任何规则，将显示所有的IPv6路由信息。

【举例】

\# 显示通过IPv6 ACL 2000过滤的激活路由的概要信息。

\<Sysname\> display ipv6 routing-table acl 2000

Routes Matched by Access control list : 2000

Summary Count : 3

Destination : ::1/128                                    Protocol  : Direct

NextHop     : ::1                                        Preference: 0

Interface   : InLoop0                                    Cost      : 0

Destination : 1:1::/64                                   Protocol  : Static

NextHop     : ::                                         Preference: 60

Interface   : NULL0                                      Cost      : 0

以上显示信息的解释请参见 表1-6(?1738996239#_Ref167867634)。

\# 显示通过IPv6 ACL 2000过滤的所有路由的详细信息。

\<Sysname\> display ipv6 routing-table acl 2000 verbose

Routes Matched by Access control list : 2000

Summary Count : 3

Destination: ::1/128

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 08h57m19s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0xa                 OrigAs: 0

      NibID: 0x20000000          LastAs: 0

     AttrID: 0xffffffff        Neighbor: ::

      Flags: 0x10004        OrigNextHop: ::1

      Label: NULL           RealNextHop: ::1

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: InLoopBack0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

Destination: 1:1::/64

   Protocol: Static          Process ID: 0

  SubProtID: 0x2                    Age: 08h57m19s

       Cost: 0               Preference: 60

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active Adv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0xa                 OrigAs: 0

      NibID: 0x20000002          LastAs: 0

     AttrID: 0xffffffff        Neighbor: ::

      Flags: 0x10084        OrigNextHop: ::

      Label: NULL           RealNextHop: ::

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: NULL0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

以上显示信息的解释请参见 表1-7(?1738996239#_Ref318297176)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 routing-table ipv6-address**

------------------------------------------------------------------------

**[display ipv6 routing-table ***ipv6-address*]命令用来显示指定目的地址的IPv6路由信息。

**[display ipv6 routing-table ***ipv6-address1 ***to*** ipv6-address2*]命令用来显示指定目的地址范围内的IPv6路由信息。

【命令】

**[display ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  *ipv6-address*  *prefix-length*   **longer-match**   **verbose** ]]

**[display ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] *ipv6-address1* **to** *ipv6-address2*  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ipv6-address*]：IPv6目的地址。

*[prefix-length*]：前缀长度，取值范围为0～128。

**[longer-match**]：匹配并显示前缀最长的路由条目。

*[ipv6-address1* **to** *ipv6-address2*]：IPv6地址范围。*ipv6-address1*和*ipv6-address2*共同决定一个地址范围，只有地址在此范围内的路由才会被显示。

**[verbose**]：显示激活和未激活路由的详细信息。如果未指定本参数，将显示激活路由的概要信息。

【使用指导】

使用不同的可选参数，命令的输出也不相同，以下是对该命令不同形式的输出说明：

(1)**display ipv6 routing-table** *ipv6-address*

显示满足如下条件的所有激活路由：

·用户输入的目的IPv6地址同路由表中各条路由的前缀长度值进行与运算；

·路由表中各条路由的目的IPv6地址同其自身前缀长度值进行与运算；

·两次运算结果相同的路由条目将被显示出来。

(2)**display ipv6 routing-table** *ipv6-address* *prefix-length*

显示满足如下条件的所有激活路由：

·用户输入的目的IPv6地址同用户输入的前缀长度值进行与运算；

·路由表中各条路由的目的IPv6地址同用户输入的前缀长度值进行与运算；

·两次运算结果相同，并且路由表中前缀长度小于等于用户输入的前缀长度的路由条目将被显示出来。

(3)**display ipv6 routing-table** *ipv6-address* **longer-match**

显示满足如下条件的所有激活路由：

·用户输入的目的IPv6地址同路由表中各条路由的前缀长度值进行与运算；

·路由表中各条路由的目的IPv6地址同其自身前缀长度值进行与运算；

·两次运算结果相同，同时前缀长度最长匹配的路由条目将被显示出来。

(4)**display ipv6 routing-table** *ipv6-address prefix-length* **longer-match**

显示满足如下条件的所有激活路由：

·用户输入的目的IPv6地址同用户输入的前缀长度值进行与运算；

·路由表中各条路由的目的IPv6地址同用户输入的前缀长度值进行与运算；

·两次运算结果相同，路由表中前缀长度小于等于用户输入的前缀长度，同时前缀长度最长匹配的路由条目将被显示出来。

(5)**display ipv6 routing-table ***ipv6-address1 ***to*** ipv6-address2*

显示*ipv6-address1*/128到*ipv6-address2*/128之间的路由，目的IPv6地址与前缀长度（128位）同时在指定范围内才会显示。

【举例】

\# 显示目的IPv6地址/前缀为10::1/127的IPv6路由信息。

\<Sysname\> display ipv6 routing-table 10::1 127

Summary Count: 3

Destination: 10::/64                                     Protocol  : Static

NextHop    : ::                                          Preference: 60

Interface  : NULL0                                       Cost      : 0

Destination: 10::/68                                     Protocol  : Static

NextHop    : ::                                          Preference: 60

Interface  : NULL0                                       Cost      : 0

Destination: 10::/120                                    Protocol  : Static

NextHop    : ::                                          Preference: 60

Interface  : NULL0                                       Cost      : 0

\# 显示目的IPv6地址/前缀为10::1/127并且掩码最长匹配的IPv6路由信息。

\<Sysname\> display ipv6 routing-table 10::1 127 longer-match

Summary Count : 1

Destination: 10::/120                                    Protocol  : Static

NextHop    : ::                                          Preference: 60

Interface  : NULL0                                       Cost      : 0

\# 显示目的IPv6地址从100::到300::范围内的IPv6路由信息。

\<Sysname\> display ipv6 routing-table 100:: to 300::

Summary Count : 3

Destination: 100::/64                                    Protocol  : Static

NextHop    : ::                                          Preference: 60

Interface  : NULL0                                       Cost      : 0

Destination: 200::/64                                    Protocol  : Static

NextHop    : ::                                          Preference: 60

Interface  : NULL0                                       Cost      : 0

Destination: 300::/64                                    Protocol  : Static

NextHop    : ::                                          Preference: 60

Interface  : NULL0                                       Cost      : 0

以上显示信息的解释请参见 表1-6(?1738996239#_Ref167867634)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 routing-table prefix-list**

------------------------------------------------------------------------

**[display ipv6 routing-table prefix-list**]命令用来显示通过指定前缀列表过滤的IPv6路由信息。

【命令】

**[display ipv6 routing-table ** **vpn-instance** *vpn-instance-name* ] **prefix-list** *prefix-list-name*  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[prefix-list-name*]：IPv6前缀列表的名称，为1～63个字符的字符串，区分大小写。

**[verbose**]：显示所有路由的详细信息。如果未指定本参数，只显示激活路由的概要信息。

【使用指导】

如果指定的前缀列表不存在，将显示所有的路由信息。

【举例】

\# 配置地址前缀列表test允许前缀为::1，前缀长度为128的IPv6路由通过。

\<Sysname\> system-view

Sysname ipv6 prefix-list test permit ::1 128

\# 显示通过前缀列表test过滤的IPv6激活路由的概要信息。

Sysname display ipv6 routing-table prefix-list test

Routes Matched by Prefix list : test

Summary Count : 1

Destination: ::1/128                                     Protocol  : Direct

NextHop    : ::1                                         Preference: 0

Interface  : InLoop0                                     Cost      : 0

以上显示信息的解释请参见 表1-6(?1738996239#_Ref167867634)。

\# 显示通过前缀列表test过滤的所有IPv6路由的详细信息。

Sysname display ipv6 routing-table prefix-list test verbose

Routes Matched by Prefix list : test

Summary Count : 1

Destination: ::1/128

   Protocol: Direct          Process ID: 0

  SubProtID: 0x0                    Age: 08h57m19s

       Cost: 0               Preference: 0

      IpPre: N/A             QosLocalID: N/A

        Tag: 0                    State: Active NoAdv

  OrigTblID: 0x0                OrigVrf: default-vrf

    TableID: 0xa                 OrigAs: 0

      NibID: 0x20000000          LastAs: 0

     AttrID: 0xffffffff        Neighbor: ::

      Flags: 0x10004        OrigNextHop: ::1

      Label: NULL           RealNextHop: ::1

    BkLabel: NULL             BkNextHop: N/A

  Tunnel ID: Invalid          Interface: InLoopBack0

BkTunnel ID: Invalid        BkInterface: N/A

   FtnIndex: 0x0           TrafficIndex: N/A

  Connector: N/A

以上显示信息的解释请参见 表1-7(?1738996239#_Ref318297176)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 routing-table protocol**

------------------------------------------------------------------------

**[display ipv6 routing-table protocol**]命令用来显示指定协议生成或发现的IPv6路由信息。

【命令】

**[display ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  **protocol** *protocol* [ **inactive** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[protocol*]：显示指定路由协议的信息，包括**bgp4+**、**direct**、**isisv6**、**ospfv3**、**ripng**和**static**。

**[inactive**]：如果配置了该参数，此命令只显示未激活路由信息。如果未指定本参数，将显示所有激活和未激活路由信息。

**[verbose**]：显示激活和未激活路由的详细信息。如果未指定本参数，将显示路由的概要信息。

【举例】

\# 显示所有IPv6直连路由的概要信息。

\<Sysname\> display ipv6 routing-table protocol direct

Summary Count : 3

Direct Routing Table Status : \<Active\>

Summary Count : 3

Destination: ::1/128                                     Protocol  : Direct

NextHop    : ::1                                         Preference: 0

Interface  : InLoop0                                     Cost      : 0

Destination: FE80::/10                                   Protocol  : Direct

NextHop    : ::                                          Preference: 0

Interface  : InLoop0                                     Cost      : 0

Destination: FF00::/8                                    Protocol  : Direct

NextHop    : ::                                          Preference: 0

Interface  : NULL0                                       Cost      : 0

Direct Routing Table Status : \<Inactive\>

Summary Count : 0

\# 显示IPv6静态路由表。

\<Sysname\> display ipv6 routing-table protocol static

Summary Count : 3

Static Routing table Status : \<Active\>

Summary Count : 3

Destination: 2::2/128                                    Protocol  : Static

NextHop    : fe80::2                                     Preference: 60

Interface  : GE1/0/2                                     Cost      : 0

Destination: 2::2/128                                    Protocol  : Static

NextHop    : fe80::3                                     Preference: 60

Interface  : GE1/0/2                                     Cost      : 0

Destination: 3::3/128                                    Protocol  : Static

NextHop    : 2::2                                        Preference: 60

Interface  : GE1/0/2                                     Cost      : 0

Static Routing table Status : \<Inactive\>

Summary Count : 0

以上显示信息的解释请参见 表1-6(?1738996239#_Ref167867634)。

**IP路由基础 \-- IP路由基础配置命令 \-- display ipv6 routing-table statistics**

------------------------------------------------------------------------

**[display ipv6 routing-table statistics**]命令用来显示IPv6路由表中的综合路由统计信息。综合路由统计信息包括路由总数、增加的路由数、删除的路由数等。

【命令】

**[display ipv6 routing-table** [ **vpn-instance** *vpn-instance-name*  **statistics**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示综合路由统计信息。

\<Sysname\> display ipv6 routing-table statistics

Proto      route       active      added       deleted

DIRECT     5           5           5           0

STATIC     3           3           3           0

RIPng      0           0           0           0

OSPFv3     0           0           0           0

IS-ISv6    0           0           0           0

BGP4+      0           0           0           0

Total      8           8           8           0

表1-8 display ipv6 routing-table statistics命令显示信息描述表

字段

描述

Proto

路由协议

route

总的路由数目

active

激活的、正在使用的路由数目

added

路由器启动后或在上一次清除路由表后，路由表中添加的路由数目

deleted

标记为删除的路由数目（此类路由在等待一段时间后会被释放）

Total

各种类型路由数目的总和

**IP路由基础 \-- IP路由基础配置命令 \-- display max-ecmp-num**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display max-ecmp-num**]命令用来显示系统支持最大等价路由的条数。

【命令】

**[display max-ecmp-num**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示系统支持最大等价路由的条数。

\<Sysname\> display max-ecmp-num

  Max-ECMP-Num in use: 6

  Max-ECMP-Num at the next reboot: 10

表1-9 display max-ecmp-num命令显示信息描述表

字段

描述

Max-ECMP-Num in use

当前使用的最大等价路由的条数

Max-ECMP-Num at the next reboot

下次启动后的最大等价路由的条数

**IP路由基础 \-- IP路由基础配置命令 \-- display rib attribute**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display rib attribute**]命令用来显示RIB的路由属性信息。

【命令】

**[display rib attribute** [ *attribute-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[attribute-id*]：路由属性ID值，取值范围0～FFFFFFFF。

【举例】

\# 显示RIB的路由属性信息。

\<Sysname\> display rib attribute

Total number of attribute(s): 10

Detailed information of attribute 0x0:

                  Flag: 0x0

              Protocol: BGP

        Address family: IPv4

       Reference count: 0

      Local preference: 0

Ext-communities number: 26

 Ext-communities value: \<RT: 1:1\> \<RT: 2:2\> \<RT: 3:3\> \<RT: 123.123.123.123:65535

                        \> \<RT: 1234567890:65535\> \<RT: 123.123.123.123:65534\> \<RT

                        : 4:4\> \<RT: 5:5\> \<RT: 6:6\> \<RT: 7:7\> \<RT: 8:8\> \<RT: 9:9\>

                         \<RT: 10:10\> \<RT: 10:1\> \<RT: 10:11\> \<RT: 10:12\> \<RT: 10:

                        13\> \<RT: 10:14\> \<RT: 10:15\> \<RT: 10:16\> \...

    Communities number: 0

     Communities value: N/A

        AS-path number: 0

         AS-path value: N/A

Detailed information of attribute 0x1:

                  Flag: 0x0

              Protocol: BGP

        Address family: IPv4

       Reference count: 0

       Local prefrence: 0

Ext-communities number: 1

 Ext-communities value: \<RT: 1:2\>

    Communities number: 0

     Communities value: N/A

        AS-path number: 0

         AS-path value: N/A

表1-10 display rib attribute命令显示信息描述表

字段

描述

Total number of attribute(s):

attribute的总个数

Flag

标志位

Protocol

产生该属性的协议

Address family

地址簇类型

Reference count

引用计数

Local prefrence

本地优先级

Ext-communities number

扩展团体属性个数

Ext-communities value

扩展团体属性值（个数为0显示N/A，最多显示20个，超出部分用...表示）

Communities number

团体属性个数

Communities value

团体属性值（个数为0显示N/A，最多显示20个，超出部分用...表示）

AS-path number

AS-path个数（AS-patch个数为所有AS号之和）

AS-path value

AS-path值（AS-path值不区分AS-set、AS-sequence、联盟AS-set、联盟AS-sequence；个数为0显示N/A，最多显示20个，超出部分用...表示）

**IP路由基础 \-- IP路由基础配置命令 \-- display rib graceful-restart**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display rib graceful-restart**]命令用来显示RIB的GR状态信息。

【命令】

**[display rib graceful-restart**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示RIB的GR状态信息。

\<Sysname\> display rib graceful-restart

RIB GR state     : Phase2-calculation end

RCOM GR State    : Flush end

Protocol GR state:

 No.  Protocol   Lifetime FD   State    Start/End

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 1    DIRECT     100      30   End      No/No

 2    STATIC     480      34   End      No/No

 3    OSPF       480      36   End      No/No

 4    ISIS       480      32   End      No/No

 5    BGP        480      31   End      No/No

 6    LDP        480      35   End      No/No

 7    SLSP       480      29   End      No/No

表1-11 display rib graceful-restart命令显示信息描述表

字段

描述

RIB GR state

RIB GR状态：

·Start：协议GR开始

·IGP end：所有IGP协议GR结束

·VPN-triggering end：VPN路由触发优选结束

·VPN-calculation end：VPN路由优选结束

·Routing protocol end：所有路由协议GR结束

·NSR-calculation unfinished：NSR优选未完成状态

·Triggering start：所有路由触发优选开始

·Triggering end：所有路由触发优选结束

·Phase1-calculation end：第一阶段优选结束

·All end：所有协议GR结束

·Phase2-calculation end：第二阶段优选结束

RCOM GR state

RCOM GR状态：

·Start：协议GR开始

·VPN-calculation end：VPN路由优选结束

·VPN-notification end：VPN路由上报结束

·Routing protocol end：所有路由协议GR结束

·NSR-calculation unfinished：NSR优选未完成状态

·Phase1-calculation end：第一阶段优选结束

·Notification end：所有路由上报结束

·Phase2-calculation end：第二阶段优选结束

·Flush start：开始下刷FIB

·Flush end：下刷FIB结束

Protocol GR state

协议GR状态

No.

编号

Protocol

协议名称

Lifetime

倒换过程中协议的路由信息/标签信息在RIB中的存活时间，单位为秒

FD

协议进程与RIB连接的句柄

State

协议GR状态：

·Init：协议GR初始化状态

·Listen：协议GR监听状态

·Idle：协议GR空闲状态

·Active：协议GR激活状态

·Start：协议GR开始状态

·End：协议GR结束状态

Start/End

·No：表示该消息未发送

·Yes：表示该消息已发送

**IP路由基础 \-- IP路由基础配置命令 \-- display rib nib**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display rib nib**]命令用来显示RIB的下一跳信息。

【命令】

**[display rib nib ** **self-originated** ]  *nib-id*   **verbose**

**[display rib nib protocol ***protocol-name* [ **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[self-originated**]：路由管理自己生成的下一跳信息。

*[nib-id*]：路由下一跳信息的ID值，取值范围1～FFFFFFFF。

**[verbose**]：显示详细信息。如果未指定本参数，则显示概要信息。

**[protocol ***protocol-name*]：显示指定路由协议生成的下一跳信息，包括**bgp**、**direct**、**isis**、**ospf**、**rip**和**static**。

【举例】

\# 显示RIB的下一跳信息。

\<Sysname\> display rib nib

Total number of nexthop(s): 176

      NibID: 0x10000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 0.0.0.0

    IFIndex: 0x111            LocalAddr: 0.0.0.0

   TopoNthp: 0

      NibID: 0x10000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 127.0.0.1

    IFIndex: 0x112            LocalAddr: 127.0.0.1

   TopoNthp: 0

      NibID: 0x10000002        Sequence: 2

       Type: 0x5                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 127.0.0.1

    IFIndex: 0x112            LocalAddr: 127.0.0.1

   TopoNthp: 0

\...\...（省略部分显示信息）

表1-12 display rib nib命令显示信息描述表

字段

描述

Total number of Nexthop(s)

总的下一跳个数

NibID

下一跳ID

Sequence

下一跳序列号

Type

下一跳类型

Flushed

是否下刷

UserKey0

第一个协议保留数据

UserKey1

第二个协议保留数据

VrfNthp

下一跳所在VPN

Nexthop

下一跳地址

IFIndex

接口索引

LocalAddr

本地接口地址

TopoNthp

下一跳所在拓扑，0为公网拓扑（目前IPv6不支持子拓扑，显示为Invalid）

SubNibID

子下一跳的ID

SubSeq

子下一跳的序列号

NthpCnt

子下一跳的下一跳计数

Samed

子下一跳中相同下一跳计数

NthpType

子下一跳类型：

·IP：下一跳是IP转发类型

·MPLS：下一跳是MPLS转发类型

\# 显示RIB下一跳详细信息。

\<Sysname\> display rib nib verbose

Total number of nexthop(s): 176

      NibID: 0x10000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 0.0.0.0

    IFIndex: 0x111            LocalAddr: 0.0.0.0

   TopoNthp: 0

     RefCnt: 6              FlushRefCnt: 2

       Flag: 0x84               Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 0.0.0.0

  RelyDepth: 0              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology: base

      NibID: 0x10000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 127.0.0.1

    IFIndex: 0x112            LocalAddr: 127.0.0.1

   TopoNthp: 0

     RefCnt: 13             FlushRefCnt: 5

       Flag: 0x84               Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 127.0.0.1

  RelyDepth: 0              RealNexthop: 127.0.0.1

  Interface: InLoop0          LocalAddr: 127.0.0.1

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology: base

      NibID: 0x15000003        Sequence: 3

       Type: 0x43               Flushed: Yes

   UserKey0: 0x100010000        VrfNthp: 0

   UserKey1: 0x0                Nexthop: 22.22.22.22

    IFIndex: 0x0              LocalAddr: 0.0.0.0

   TopoNthp: 0

     RefCnt: 9              FlushRefCnt: 3

       Flag: 0x84               Version: 1

     Policy: tnl-policy1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 22.22.22.22

  RelyDepth: 1              RealNexthop: 13.1.1.2

  Interface: GE0/1/3          LocalAddr: 13.1.1.1

  TunnelCnt: 1                      Vrf: default-vrf

   TunnelID: 1025               Topology: base

\...\...（省略部分显示信息）

表1-13 display rib nib verbose命令显示信息描述表

字段

描述

Policy

隧道策略名

*[x *nexthop (s)]

下一跳具体值（前面数值表示下一跳个数）

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

LocalAddr

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

**IP路由基础 \-- IP路由基础配置命令 \-- display route-direct nib**

------------------------------------------------------------------------

**[display route-direct nib**]命令用来显示直连路由下一跳信息。

【命令】

**[display route-direct nib ** *nib-id* ]  **verbose**

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

\# 显示直连路由下一跳信息。

\<Sysname\> display route-direct nib

Total number of nexthop(s): 116

      NibID: 0x10000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 0.0.0.0

    IFIndex: 0x111            LocalAddr: 0.0.0.0

   TopoNthp: 0

      NibID: 0x10000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 127.0.0.1

    IFIndex: 0x112            LocalAddr: 127.0.0.1

   TopoNthp: 0

\...\...（省略部分显示信息）

表1-14 display route-direct nib命令显示信息描述表

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

\# 显示直连路由下一跳详细信息。

\<Sysname\> display route-direct nib verbose

Total number of nexthop(s): 116

      NibID: 0x10000000        Sequence: 0

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 0.0.0.0

    IFIndex: 0x111            LocalAddr: 0.0.0.0

     RefCnt: 2              FlushRefCnt: 0

       Flag: 0x2                Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 0.0.0.0

  RelyDepth: 0              RealNexthop: 0.0.0.0

  Interface: NULL0            LocalAddr: 0.0.0.0

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology: base

      NibID: 0x10000001        Sequence: 1

       Type: 0x1                Flushed: Yes

   UserKey0: 0x0                VrfNthp: 1

   UserKey1: 0x0                Nexthop: 127.0.0.1

    IFIndex: 0x112            LocalAddr: 127.0.0.1

     RefCnt: 5              FlushRefCnt: 0

       Flag: 0x2                Version: 1

 1 nexthop(s):

PrefixIndex: 0              OrigNexthop: 127.0.0.1

  RelyDepth: 0              RealNexthop: 127.0.0.1

  Interface: InLoop0          LocalAddr: 127.0.0.1

  TunnelCnt: 0                      Vrf: vpn1

   TunnelID: N/A               Topology: base

\...\...（省略部分显示信息）

表1-15 display route-direct nib verbose命令显示信息描述表

字段

描述

*[x* nexthop (s)]

下一跳具体值（前面数值表示下一跳个数）

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

**IP路由基础 \-- IP路由基础配置命令 \-- ecmp mode enhanced**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ecmp mode enhanced**]命令用来使能IPv4等价路由增强模式功能。

**[undo ecmp mode**]命令用来恢复缺省情况。

【命令】

**[ecmp mode enhanced**]

**[undo ecmp mode**]

【缺省情况】

IPv4等价路由增强模式功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当去往同一目的地址存在多条等价路由时，设备在转发去往该目的地址的报文时，会在各条路径间实现负载分担；如果其中一条或者多条路径失效，所有业务流量会在剩余的可用路径间重新进行一次分配，实现新的负载均衡。

如果为了保持业务的连续性，需要保持在可用路径上转发的业务流量不改变转发路径，仅将故障路径上的原业务流量在可用路径上进行平均分配，可以配置等价路由增强模式功能。

【举例】

\# 使能IPv4等价路由增强模式功能。

\<Sysname\> system-view

Sysname ecmp mode enhanced

The configuration will take effect at the next reboot. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

**IP路由基础 \-- IP路由基础配置命令 \-- fib lifetime**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[fib lifetime**]命令用来配置IPv4/IPv6路由在FIB中的最大存活时间。

**[undo fib lifetime**]命令用来恢复缺省情况。

【命令】

**[fib******lifetime** *seconds*]

**[undo fib lifetime**]

【缺省情况】

IPv4/IPv6路由在FIB中的最大存活时间为600秒。

【视图】

RIB IPv4地址族视图/RIB IPv6地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：FIB中路由的最大存活时间，取值范围为0～6000，单位为秒。取值为0时表示，协议或RIB进程倒换并重新恢复后，会立即通知FIB老化表项。

【使用指导】

如果配置了该命令，协议在不配置GR或NSR的情况下，协议或RIB倒换重新恢复后，会延迟上述配置时间间隔，再通知FIB老化表项，当配置为0时，会立刻通知FIB老化表项。

【举例】

\# 配置FIB中IPv4路由的最大存活时间为60秒。

\<Sysname\> system-view

Sysname rib

Sysname-rib address-family ipv4

Sysname-rib-ipv4 fib lifetime 60

**IP路由基础 \-- IP路由基础配置命令 \-- ipv6 ecmp mode enhanced**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ipv6 ecmp mode enhanced**]命令用来使能IPv6等价路由增强模式功能。

**[undo ipv6 ecmp mode**]命令用来恢复缺省情况。

【命令】

**[ipv6 ecmp mode enhanced**]

**[undo ipv6 ecmp mode**]

【缺省情况】

IPv6等价路由增强模式功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当去往同一目的地址存在多条等价路由时，设备在转发去往该目的地址的报文时，会在各条路径间实现负载分担；如果其中一条或者多条路径失效，所有业务流量会在剩余的可用路径间重新进行一次分配，实现新的负载均衡。

如果为了保持业务的连续性，需要保持在可用路径上转发的业务流量不改变转发路径，仅将故障路径上的原业务流量在可用路径上进行平均分配，可以配置等价路由增强模式功能。

【举例】

\# 使能IPv6等价路由增强模式功能。

\<Sysname\> system-view

Sysname ipv6 ecmp mode enhanced

The configuration will take effect at the next reboot. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

**IP路由基础 \-- IP路由基础配置命令 \-- max-ecmp-num**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[max-ecmp-num**]命令用来配置系统支持最大等价路由的条数。

【命令】

**[max-ecmp-num** *number*]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：最大等价路由的条数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置系统支持最大等价路由的条数为10。

\<Sysname\> system-view

Sysname max-ecmp-num 10

The configuration will take effect at the next reboot. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

重启后，系统支持最大等价路由的条数为10。

**IP路由基础 \-- IP路由基础配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[non-stop-routing**]命令用来配置RIB IPv4/IPv6地址族使能NSR功能。

**[undo non-stop-routing**]命令用来恢复缺省情况。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【缺省情况】

未使能NSR功能。

【视图】

RIB IPv4地址族视图/RIB IPv6地址族视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置RIB IPv4地址族使能NSR功能。

\<Sysname\> system-view

Sysname rib

Sysname-rib address-family ipv4

Sysname-rib-ipv4 non-stop-routing

**IP路由基础 \-- IP路由基础配置命令 \-- protocol lifetime**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[protocol lifetime**]命令用来配置IPv4/IPv6路由和标签在RIB中的最大存活时间。

**[undo protocol lifetime**]命令用来恢复缺省情况。

【命令】

**[protocol ***protocol ***lifetime ***seconds*]

**[undo protocol**]*[protocol *]**lifetime**

【缺省情况】

IPv4/IPv6路由和标签在RIB中的最大存活时间为480秒。

【视图】

RIB IPv4地址族视图/RIB IPv6地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：路由协议，可以是**bgp**、**direct**、**isis**、**ldp**、**ospf**、**rip**、**static**或**static-lsp**。

*[seconds*]：最大存活时间，取值范围为1～6000，单位为秒。

【使用指导】

如果配置了该命令，且协议配置GR的情况下，需要注意该时间不要与GR时间冲突，即必须要保证协议能够在该时间内完成GR并将全部表项下发RIB，否则会导致GR失败并断流。

【举例】

\# 配置RIB中OSPF路由和标签的最大存活时间为60秒。

\<Sysname\> system-view

Sysname rib

Sysname-rib address-family ipv4

Sysname-rib-ipv4 protocol ospf lifetime 60

**IP路由基础 \-- IP路由基础配置命令 \-- reset ip routing-table statistics protocol**

------------------------------------------------------------------------

**[reset ip routing-table statistics protocol**]命令用来清除路由表中的路由统计信息。

【命令】

**[reset ip routing-table statistics protocol **[[ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name* ] { *protocol* \| **all** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：清除指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则清除公网的路由统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：清除指定VPN的路由统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则清除公网的路由统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[protocol*]：清除IPv4路由表中指定路由协议的统计信息。目前可选择**bgp**、**direct**、**isis**、**ospf**、**rip**、**static**。

**[all**]：清除IPv4路由表中所有路由协议的统计信息。

【举例】

\# 清除路由表中的路由统计信息。

\<Sysname\> reset ip routing-table statistics protocol all

**IP路由基础 \-- IP路由基础配置命令 \-- reset ipv6 routing-table statistics protocol**

------------------------------------------------------------------------

**[reset ipv6 routing-table statistics protocol**]命令用来清除IPv6路由表中的综合路由统计信息。

【命令】

**[reset ipv6 routing-table statistics protocol** [ **vpn-instance** *vpn-instance-name*  { *protocol* \| **all** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：清除指定VPN的路由统计信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则清除公网的路由统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[protocol*]：清除IPv6路由表中指定路由协议的统计信息。目前可选择**bgp4+**、**direct**、**isisv6**、**ospfv3**、**ripng**、**static**。

**[all**]：清除IPv6路由表中所有路由协议的统计信息。

【举例】

\# 清除IPv6路由表中所有路由协议的综合路由统计信息。

\<Sysname\> reset ipv6 routing-table statistics protocol all

**IP路由基础 \-- IP路由基础配置命令 \-- rib**

------------------------------------------------------------------------

![说明](IP路由基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rib**]命令用来进入RIB视图。

**[undo rib**]命令用来删除RIB视图下的所有配置。

【命令】

**[rib**]

**[undo rib**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入RIB视图。

\<Sysname\> system-view

Sysname rib

Sysname-rib

