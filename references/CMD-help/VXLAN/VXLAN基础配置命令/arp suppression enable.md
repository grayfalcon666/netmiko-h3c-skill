
**VXLAN \-- VXLAN基础配置命令 \-- arp suppression enable**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[arp suppression enable**]命令用来开启ARP泛洪抑制功能。

**[undo arp suppression enable**]命令用来恢复缺省情况。

【命令】

**[arp suppression enable**]

**[undo arp suppression enable**]

【缺省情况】

ARP泛洪抑制功能处于关闭状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了避免广播发送的ARP请求报文占用核心网络带宽，VTEP从本地站点、VXLAN隧道接收到ARP请求和ARP应答报文后，根据该报文在本地建立ARP泛洪抑制表项。后续当VTEP收到本站点内虚拟机请求其它虚拟机MAC地址的ARP请求时，优先根据ARP泛洪抑制表项进行代答。如果没有对应的表项，则将ARP请求泛洪到核心网。ARP泛洪抑制功能可以大大减少ARP泛洪的次数。

【举例】

\# 在VSI vsi1下开启ARP泛洪抑制功能。

\<Sysname\> system-view

Sysname vsi vsi1

Sysname-vsi-vsi1 arp suppression enable

【相关命令】

·**display arp suppression**** vsi**

·**reset arp suppression**** vsi**

**VXLAN \-- VXLAN基础配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置VSI的描述信息。

**[undo description**]命令用来删除VSI的描述信息。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

未配置VSI的描述信息。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：VSI的描述信息，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置名为vpn1的VSI的描述信息为"vsi for vpn1"。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 description vsi for vpn1

【相关命令】

·**display l2vpn vsi**

**VXLAN \-- VXLAN基础配置命令 \-- display arp suppression vsi**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display arp suppression vsi**]命令用来显示VSI的ARP泛洪抑制表项信息。

【命令】

集中式设备：

**[display arp suppression vsi** [ **name** *vsi-name*   **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display arp suppression vsi** [ **name** *vsi-name*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display arp suppression vsi** [ **name** *vsi-name*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** vsi-name*]：显示指定VSI的ARP泛洪抑制表项。如果不指定本参数，则显示所有VSI的ARP泛洪抑制表项。

**[slot** *slot-number*]：显示指定单板的ARP泛洪抑制表项。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的ARP泛洪抑制表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的ARP泛洪抑制表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的ARP泛洪抑制表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的ARP泛洪抑制表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的ARP泛洪抑制表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的ARP泛洪抑制表项。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示ARP泛洪抑制表项的个数。

【举例】

\# 显示所有VSI的ARP泛洪抑制表项信息。（集中式设备）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示所有VSI的ARP泛洪抑制表项个数。（集中式设备）

\<Sysname\> display arp suppression vsi count

Total entries: 3

\# 显示主用主控板上的ARP泛洪抑制表项信息。（分布式设备－独立运行模式）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示主用主控板上的ARP泛洪抑制表项个数。（分布式设备－独立运行模式）

\<Sysname\> display arp suppression vsi count

Total entries: 3

\# 显示主设备上的ARP泛洪抑制表项信息。（集中式IRF设备）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示主设备上的ARP泛洪抑制表项个数。（集中式IRF设备）

\<Sysname\> display arp suppression vsi count

Total entries: 3

\# 显示全局主用主控板上的ARP泛洪抑制表项信息。（分布式设备－IRF模式）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示全局主用主控板上的ARP泛洪抑制表项个数。（分布式设备－IRF模式）

\<Sysname\> display arp suppression vsi count

Total entries: 3

表1-1 display arp suppression vsi命令显示信息描述表

字段

描述

IP address

ARP泛洪抑制表项的IP地址

MAC address

ARP泛洪抑制表项的MAC地址

Vsi Name

VSI名称

Link ID

MAC表项的出链路标识符，用来在VSI内唯一标识一条AC或一条VXLAN隧道

Aging

ARP泛洪抑制表项的老化时间，单位为分钟

Total entries

ARP泛洪抑制表项的数目

【相关命令】

·**arp suppression enable**

·**reset arp suppression**** vsi**

**VXLAN \-- VXLAN基础配置命令 \-- display igmp host group**

------------------------------------------------------------------------

**[display** **igmp** **host** **group**]命令用来显示IGMP执行主机行为的所有组播组信息。

【命令】

**[display**[ **igmp** **host** **group** [ *group-address* \| **interface** *interface-type* *interface-number* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-address*]：显示指定组播组的信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，则显示所有组播组的信息。

**[interface** *interface-type* *interface-number*]：显示指定接口上的信息。如果未指定本参数，则显示所有接口上的信息。

**[verbose**]：显示详细信息。如果未指定本参数，则显示简要信息。

【使用指导】

采用组播路由方式泛洪流量时，VXLAN组播报文源IP地址所在的接口需要作为IGMP主机加入VXLAN所在的组播组。通过本命令可以查看接口是否加入组播组，及该组播组的信息。

【举例】

\# 显示IGMP执行主机行为的所有组播组的简要信息。

\<Sysname\> display igmp host group

IGMP host groups in total: 2

 Vlan-interface10(1.1.1.20):

  IGMP host groups in total: 2

   Group address      Member state      Expires

   225.1.1.1          Idle              Off

   225.1.1.2          Idle              Off

\# 显示IGMP执行主机行为的所有组播组的详细信息。

\<Sysname\> display igmp host group verbose

 Vlan-interface10(1.1.1.20):

  IGMP host groups in total: 2

   Group: 225.1.1.1

     Group mode: Exclude

     Member state: Idle

     Expires: Off

     Source list (sources in total: 0):

   Group: 225.1.1.2

     Group mode: Exclude

     Member state: Idle

     Expires: Off

     Source list (sources in total: 0):

表1-2 display igmp host group命令显示信息描述表

字段

描述

IGMP host groups in total

IGMP执行主机行为的组播组总数

Vlan-interface10(1.1.1.20)

IGMP执行主机行为的接口的名称和IP地址

IGMP host groups in total

当前接口下IGMP执行主机行为的组播组数目

Group address/Group

组播组地址

Member state

组播组成员的状态，取值包括：

·Delay：表示加入了组播组，并对该组启动了延迟发送报告报文的定时器

·Idle：表示加入了组播组，但对该组尚未启动延迟发送报告报文的定时器

延迟发送报告报文定时器的值不可配置

Expires

组播组延迟发送报告报文的剩余时间，Off表示该定时器关闭

Group mode

对组播源的过滤模式，取值包括：

·Include：表示INCLUDE模式

·Exclude：表示EXCLUDE模式

Source list

IGMP执行主机行为的组播组所包含的组播源列表

sources in total

组播源的总数

![说明](VXLAN命令.files/image002.png)

对本命令的显示信息更加详细的介绍，请参见"IP组播配置指导"中的"IGMP"。

【相关命令】

·**igmp host enable**

**VXLAN \-- VXLAN基础配置命令 \-- display l2vpn mac-address**

------------------------------------------------------------------------

**[display l2vpn mac-address**]命令用来显示VSI的MAC地址表信息。

【命令】

**[display l2vpn mac-address ** **vsi** *vsi-name* ]  **dynamic**   **count**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi** *vsi-name*]：显示指定VSI的MAC地址表信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的MAC地址表信息。

**[dynamic**]：显示通过源MAC地址动态学习的MAC地址表项。如果不指定本参数，则显示所有类型的MAC地址表项，包括通过源MAC地址动态学习的本地和远端MAC地址表项、通过IS-IS协议学习的远端MAC地址表项、静态配置的远端MAC地址表项。VXLAN不支持静态配置本地MAC地址表项。

**[count**]：显示MAC地址表项的数目。如果不指定本参数，则显示MAC地址表项的具体信息。

【举例】

\# 显示所有VSI的MAC地址表信息。

\<Sysname\> display l2vpn mac-address

MAC Address      State    VSI Name                        Link ID/Name  Aging

0000-0000-000a   dynamic  vpn1                            1             Aging

0000-0000-000b   static   vpn1                            Tunnel10      NotAging

0000-0000-000c   dynamic  vpn1                            Tunnel60      Aging

0000-0000-000d   dynamic  vpn1                            Tunnel99      Aging

\-\-- 4 mac address(es) found  \-\--

\# 显示所有VSI的MAC地址表项总数。

\<Sysname\> display l2vpn mac-address count

4 mac address(es) found

表1-3 display l2vpn mac-address命令显示信息描述表

字段

描述

MAC Address

MAC地址

State

MAC地址的状态，取值包括：

·dynamic：表示通过源MAC地址动态学习的本地或远端MAC地址表项

·static：表示静态配置的远端MAC地址表项（Aging字段取值为NotAging）或通过IS-IS协议学习的远端MAC地址表项（Aging字段取值为Aging）

VSI Name

VSI名称

Link ID/Name

对于本端MAC地址，为MAC地址的出链路标识符，即AC在VSI内的链路标识符；对于远端MAC地址，为MAC地址对应的隧道名称

Aging

MAC地址表项是否老化，取值包括Aging和NotAging

XX mac address(es) found

VSI的MAC地址表项的总数

【相关命令】

·**reset l2vpn mac-address**

**VXLAN \-- VXLAN基础配置命令 \-- display l2vpn service-instance**

------------------------------------------------------------------------

**[display l2vpn service-instance**]命令用来显示以太网服务实例的信息。

【命令】

**[display l2vpn service-instance ** **interface**]* interface-type interface-number* [ **service-instance** *instance-id*  ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定二层以太网接口或二层聚合接口上的以太网服务实例信息。*interface-type interface-number*为接口类型和接口编号。如果没有指定本参数，则显示所有二层以太网接口和二层聚合接口上的以太网服务实例信息。

**[service-instance*** instance-id*]：显示指定以太网服务实例的信息。*instance-id*为以太网服务实例的ID，取值范围为1～4096。如果指定了**interface*** interface-type interface-number*参数，没有指定本参数，则显示指定二层以太网接口或二层聚合接口上所有以太网服务实例的信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【举例】

\# 显示所有以太网服务实例的简要信息。

\<Sysname\> display l2vpn service-instance

Total number of service-instances: 4, 4 up, 0 down

Total number of ACs: 4, 4 up, 0 down

Interface                SrvID Owner                           LinkID State Type

GE1/0/3                  1     vsi10                           1      Up    VSI

GE1/0/3                  2     vsi11                           1      Up    VSI

GE1/0/3                  3     vsi12                           1      Up    VSI

GE1/0/3                  4     vsi13                           1      Up    VSI

表1-4 display l2vpn service-instance命令显示信息描述表

字段

描述

Total number of service-instances

以太网服务实例的总数，及处于up和down状态的以太网服务实例数目

Total number of ACs

AC的总数，及处于up和down状态的AC数目

Interface

二层以太网接口或二层聚合接口名称

SrvID

以太网服务实例的ID

Owner

VSI名称，如果以太网服务实例上尚未关联VSI，则本字段显示为空

LinkID

以太网服务实例在VSI内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

Type

以太网服务实例所属的L2VPN类型，取值包括VSI和VPWS

\# 显示二层以太网接口GigabitEthernet1/0/3上所有以太网服务实例的详细信息。

\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/3 verbose

Interface: GE1/0/3

  Service Instance: 1

    Encapsulation : s-vid 1 to 16

    VSI Name      : vsi10

    Link ID       : 1

    State         : Up

  Service Instance: 2

    Encapsulation : s-vid 1001 to 1016

                    only-tagged

    VSI Name      : vsi11

    Link ID       : 1

    State         : Up

  Service Instance: 3

    Encapsulation : s-vid 2000

                    c-vid 1001 to 1002 1015 to 1016

    VSI Name      : vsi12

    Link ID       : 1

    State         : Up

表1-5 display l2vpn service-instance verbose命令显示信息描述表

字段

描述

Interface

二层以太网接口或二层聚合接口

Service Instance

以太网服务实例ID

Encapsulation

以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则不显示本字段

VSI Name

与以太网服务实例关联的VSI的名称

Link ID

以太网服务实例在VSI内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

【相关命令】

·**service-instance**

**VXLAN \-- VXLAN基础配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

**[display l2vpn vsi**]命令用来显示VSI的信息。

【命令】

**[display** **l2vpn** **vsi** [ **name** *vsi-name*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** vsi-name*]：显示指定VSI的信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的信息。

**[verbose**]：显示VSI的详细信息。如果不指定本参数，则显示VSI的简要信息。

【举例】

\# 显示所有VSI的简要信息。

\<Sysname\> display l2vpn vsi

Total number of VSIs: 1, 1 up, 0 down, 0 admin down

VSI Name                        VSI Index       MTU    State

vpna                            0               1500   Up

\# 显示所有VSI的详细信息。

\<Sysname\> display l2vpn vsi verbose

VSI Name: vpna

  VSI Index               : 0

  VSI State               : Up

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : -

  Drop Unknown            : Disabled

  Flooding                : Enabled

  Statistics              : Enabled

  Input statistics:

    Octets   : 0

    Packets  : 0

    Errors   : 0

    Discards : 0

  Output statistics:

    Octets   : 0

    Packets  : 0

    Errors   : 0

    Discards : 0

  Gateway Interface       : VSI-interface 100

  VXLAN ID                : 10

  Tunnels:

    Tunnel Name          Link ID    State  Type

    Tunnel1              0x5000001  Up     Manual

    Tunnel2              0x5000002  Up     Manual

    MTunnel0             0x6002710  Up     Auto

  ACs:

    AC                               Link ID    State

    GE1/0/1 srv1000                  0          Up

表1-6 display l2vpn vsi命令显示信息描述表

字段

描述

VSI Name

VSI名称

VSI Index

VSI索引

VSI Description

VSI的描述信息，如果不配置，则此行不显示

VSI State

VSI的状态，取值包括：

·Up：up状态。只有VXLAN关联了处于up状态的隧道和AC，VSI才会处于up状态

·Down：down状态

·Administratively down：通过**shutdown**命令手工关闭VSI

MTU

VSI上配置的最大传输单元

Bandwidth

VSI的带宽限制值，单位为kbps

Broadcast Restrain

VSI的广播抑制百分比

Multicast Restrain

VSI的组播抑制百分比

Unknown Unicast Restrain

VSI的未知单播抑制百分比

MAC Learning

是否使能了MAC地址学习功能

MAC Table Limit

VSI内MAC地址表项的最大数目

Drop Unknown

当VSI内学习到的MAC地址数达到最大值后，是否禁止转发源MAC地址不在MAC地址表里的报文

Hub-Spoke

是否使能了Hub-spoke能力

Flooding

是否使能VSI的泛洪功能，取值包括：

·Enabled：表示使能了VSI的泛洪功能，即VTEP会将目的MAC地址未知的单播数据帧发送给所有本地和远端站点

·Disabled：表示禁止VSI的泛洪功能，即VTEP只将目的MAC地址未知的单播数据帧发送给所有本地站点

Statistics

是否使能VSI的统计功能，取值包括：

·Enabled：使能了VSI的统计功能

·Disabled：禁止VSI的统计功能

Input statistics

入方向的VSI报文统计信息，包括入方向接收的字节数（Octets）、接收的报文数（Packets）、接收的错误报文数（Errors）和丢弃的报文数（Discards）

Output statistics

出方向的VSI报文统计信息，包括出方向发送的字节数（Octets）、发送的报文数（Packets）、错误报文数（Errors）和丢弃的报文数（Discards）

Gateway Interface

VSI网关虚接口编号

VXLAN ID

VXLAN编号

Tunnels

与VXLAN关联的隧道信息

Tunnel Name

隧道名称

Link ID

隧道在VSI内的链路标识符

State

隧道状态，取值包括Up和Down

Type

VXLAN和VXLAN隧道的关联方式，取值包括：

·Auto：表示自动关联，分为以下两种：

¡通过VXLAN ISIS协商VXLAN ID后，自动将VXLAN和VXLAN隧道关联；

¡在组播路由方式下，自动创建用于转发泛洪流量的组播VXLAN隧道（MTunnel），并将其与VXLAN关联

·Manual：表示手动关联VXLAN和VXLAN隧道

ACs

VSI的AC列表

AC

接入电路

Link ID

AC在VSI内的链路标识符

State

AC的状态，取值包括Up和Down

**VXLAN \-- VXLAN基础配置命令 \-- display vxlan tunnel**

------------------------------------------------------------------------

**[display vxlan tunnel**]命令用来显示与VXLAN关联的VXLAN隧道的信息。

【命令】

**[display** **vxlan tunnel** [ **vxlan-id** *vxlan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vxlan-id*]：显示与指定VXLAN关联的隧道的信息。*vxlan-id*为VXLAN的编号，取值范围为0～16777215。不指定此参数，则显示所有与VXLAN关联的隧道的信息。

【举例】

\# 显示所有与VXLAN关联的隧道的信息。

\<Sysname\> display vxlan tunnel

Total number of VXLANs: 1

VXLAN ID: 10, VSI name: vpna, Total tunnels: 4 (4 up, 0 down)

Tunnel name          Link ID    State  Type

Tunnel0              0x5000000  Up     Auto

Tunnel1              0x5000001  Up     Manual

Tunnel2              0x5000002  Up     Manual/Auto

MTunnel0             0x6002710  Up     Auto

\# 显示与编号为10的VXLAN关联的隧道的信息。

\<Sysname\> display vxlan tunnel vxlan-id 10

VXLAN ID: 10, VSI name: vpna, Total tunnels: 4 (4 up, 0 down)

Tunnel name          Link ID    State  Type

Tunnel0              0x5000000  Up     Auto

Tunnel1              0x5000001  Up     Manual

Tunnel2              0x5000002  Up     Manual/Auto

MTunnel0             0x6002710  Up     Auto

表1-7 display vxlan tunnel命令显示信息描述表

字段

描述

Total number of VXLANs

已创建的VXLAN的总数

VXLAN ID

VXLAN ID

VSI name

VXLAN所属的VSI名称

Total tunnels

与VXLAN关联的隧道的总数，包括处于Up和Down状态的隧道总数

Tunnel name

隧道名称

Link ID

隧道在VXLAN内的链路标识符

State

隧道的状态，取值包括Up、Down

Type

VXLAN和VXLAN隧道的关联方式，取值包括：

·Auto：表示自动关联，分为以下两种：

¡通过VXLAN ISIS协商VXLAN ID后，自动将VXLAN和VXLAN隧道关联；

¡在组播路由方式下，自动创建用于转发泛洪流量的组播VXLAN隧道（MTunnel），并将其与VXLAN关联

·Manual：表示手动关联VXLAN和VXLAN隧道

【相关命令】

·**tunnel**

·**vxlan**

·**negotiate-vni enable**

**VXLAN \-- VXLAN基础配置命令 \-- encapsulation**

------------------------------------------------------------------------

**[encapsulation**]命令用来配置以太网服务实例的报文匹配规则。

**[undo encapsulation**]命令用来删除以太网服务实例的报文匹配规则。

【命令】

**[encapsulation**[ **c-vid** { *vlan-id* \| *vlan-id-list* }]]

**[encapsulation**[ **s-vid** { *vlan-id* \| *vlan-id-list* } [ **only-tagged** ]]]

**[encapsulation**[ **s-vid** *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]]

**[encapsulation**[ { **default** \| **tagged** \| **untagged** }]]

**[undo encapsulation**]

【缺省情况】

未配置任何报文匹配规则。

【视图】

以太网服务实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[c-vid**[ { *vlan-id* \| *vlan-id-list* }]]：匹配内层VLAN标签（Customer VLAN ID）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ to *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[s-vid**[ { *vlan-id* \| *vlan-id-list* }]]：匹配外层VLAN标签（Service VLAN ID）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[only-tagged**]：表示只匹配携带VLAN标签的报文。当匹配的VLAN为缺省VLAN时，如果未指定本关键字，则会同时匹配所携带VLAN标签为缺省VLAN的报文和未携带VLAN标签的报文；如果指定了本参数，则只匹配所携带VLAN标签为缺省VLAN的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[s-vid**[ *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]]：匹配指定外层VLAN标签和内层VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·**al****l**表示所有VLAN。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[default**]：表示缺省的报文匹配规则。

**[tagged**]：表示匹配携带VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[untagged**]：表示匹配未携带VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

【使用指导】

当同一个接口下配置的不同以太网服务实例的报文匹配规则出现重叠时，如何匹配报文与设备的型号有关，请以设备的实际情况为准。

同一个以太网接口下可以创建多个服务实例，但是最多只能有一个服务实例采用缺省的报文匹配规则（**encapsulation default**）。如果接口下同时存在一个采用缺省报文匹配规则的服务实例和多个采用其他报文匹配规则的服务实例，则没有与任何其他报文匹配规则匹配的报文将匹配缺省报文匹配规则；如果接口下只存在一个采用缺省报文匹配规则的服务实例，则该接口上的所有报文都匹配缺省报文匹配规则。

需要注意的是：

·在同一个以太网服务实例视图下，不能重复执行本命令。

·删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例与VSI的关联。

·内层VLAN标签和外层VLAN标签的介绍请参见"二层技术-以太网交换配置指导"中的"QinQ"。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1的以太网服务实例1上配置如下报文匹配规则：匹配外层VLAN标签为111，内层VLAN标签为20、30～40的报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 1

Sysname-GigabitEthernet1/0/1-srv1 encapsulation s-vid 111 c-vid 20 30 to 40

【相关命令】

·**display l2vpn service-instance**

**VXLAN \-- VXLAN基础配置命令 \-- flooding disable**

------------------------------------------------------------------------

**[flooding disable**]命令用来关闭VSI的泛洪功能。

**[undo flooding disable**]命令用来恢复缺省情况。

【命令】

**[flooding disable**]

**[undo flooding disable**]

【缺省情况】

VSI的泛洪功能处于开启状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，VTEP从本地站点内接收到目的MAC地址未知的单播数据帧后，会在该VXLAN内除接收接口外的所有本地接口和VXLAN隧道上泛洪该数据帧，将该数据帧发送给VXLAN内的所有站点。如果用户希望把该类数据帧限制在本地站点内，不通过VXLAN隧道将其转发到远端站点，则可以通过本命令手工禁止VXLAN对应VSI的泛洪功能。

【举例】

\# 关闭名称为vsi1的VSI的泛洪功能。

\<Sysname\> system-view

Sysname vsi vsi1

Sysname-vsi-vsi1 flooding disable

**VXLAN \-- VXLAN基础配置命令 \-- group**

------------------------------------------------------------------------

**[group**]命令用来配置VXLAN泛洪的组播地址和组播报文的源IP地址。

**[undo group**]命令用来恢复缺省情况。

【命令】

**[group** *group-address* **source** *source-address*]

**[undo group** *group-address* **source** *source-address*]

【缺省情况】

未指定VXLAN泛洪的组播地址和组播报文的源IP地址，VXLAN采用单播路由方式泛洪。

【视图】

VXLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：VXLAN泛洪的组播地址，取值范围为224.0.1.0～239.255.255.255。

**[source** *source-address*]：指定VXLAN组播报文的源IP地址。

【使用指导】

泛洪流量包括组播、广播和未知单播流量。VXLAN流量泛洪可以采用如下两种方式：

·单播路由方式（头端复制）：VTEP接收到某个VXLAN的泛洪流量后，不仅通过本地接口在本地站点内泛洪，还会通过与该VXLAN关联的所有隧道、采用单播方式将其发送给VXLAN内的所有远端VTEP。

·组播路由方式（核心复制）：同一个VXLAN内的所有VTEP都加入同一个组播组，利用组播路由协议在IP核心网上为该组播组建立组播转发表项。VTEP接收到泛洪流量后，不仅在本地站点内泛洪，还会将本命令指定的组播地址作为目的IP地址、**source** *source-address*参数指定的地址作为源IP地址，对泛洪流量进行封装，封装后的报文根据已建立的组播转发表项转发到远端VTEP。

缺省情况下，VTEP采用单播路由方式泛洪流量。如果执行了本命令，则通过组播路由方式泛洪流量。

需要注意的是：

·对于某些产品，为确保组播报文转发正常，VXLAN组播报文的源IP地址（*source-address*）应指定为一个已创建且处于up状态的VXLAN隧道的源端地址。

·可以为不同的VXLAN指定相同的组播地址。例如，多个VXLAN共用相同的VTEP设备时，为这些VXLAN指定相同的组播地址，通过VXLAN ID来区分报文所属的VXLAN，可以减少IP核心网络中建立的组播转发表项数目。为不同VXLAN指定相同的组播地址时，要求为其指定的源IP地址也必须相同。

·在同一个VXLAN视图下重复执行本命令，则新的配置覆盖已有配置。

【举例】

\# 为VXLAN 100配置VXLAN泛洪的组播地址为233.1.1.1、VXLAN组播报文的源IP地址为2.1.1.1。

\<Sysname\> system-view

Sysname vsi aaa

Sysname-vsi-aaa vxlan 100

Sysname-vsi-aaa-vxlan-100 group 233.1.1.1 source 2.1.1.1

【相关命令】

·**igmp** **host** **enable**

**VXLAN \-- VXLAN基础配置命令 \-- igmp host enable**

------------------------------------------------------------------------

**[igmp** **host** **enable**]命令用来在接口上使能IGMP协议的主机功能。

**[undo** **igmp** **host** **enable**]命令用来关闭接口上IGMP协议的主机功能。

【命令】

**[igmp** **host** **enable**]

**[undo** **igmp** **host** **enable**]

【缺省情况】

接口上IGMP协议的主机功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

采用组播路由方式泛洪流量时，必须在VXLAN组播报文源IP地址所在的接口上执行本命令，使得当前接口作为IGMP主机，即从该接口收到IGMP查询报文后，通过该接口发送组播组的报告报文，以便接收该组播组的报文。

需要注意的是，只有通过**multicast routing**命令使能IP组播路由后，本命令才会生效。

【举例】

·路由应用

\# 使能公网实例中的IP组播路由，并在接口GigabitEthernet1/0/1上使能IGMP协议的主机功能。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 igmp host enable

·交换应用

\# 使能公网实例中的IP组播路由，并在接口Vlan-interface10上使能IGMP协议的主机功能。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 igmp host enable

【相关命令】

·**display** **igmp** **host** **group**

·**group**

·**multicast** **routing**（IP组播命令参考/组播路由与转发）

**VXLAN \-- VXLAN基础配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

**[l2vpn enable**]命令用来使能L2VPN功能。

**[undo l2vpn enable**]命令用来关闭L2VPN功能。

【命令】

**[l2vpn enable**]

**[undo l2vpn enable**]

【缺省情况】

L2VPN功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有使能L2VPN功能后，才能进行L2VPN的相关配置。

【举例】

\# 使能L2VPN功能。

\<Sysname\> system-view

Sysname l2vpn enable

**VXLAN \-- VXLAN基础配置命令 \-- mac-address static**

------------------------------------------------------------------------

**[mac-address static**]命令用来添加静态远端MAC地址表项。

**[undo mac-address static**]命令用来删除指定的静态远端MAC地址表项。

【命令】

**[mac-address static** *mac-address* **interface tunnel** *tunnel-number* **vsi** *vsi-name*]

**[undo mac-address static** [ *mac-address*   **interface tunnel** *tunnel-number*  **vsi** *vsi-name*]]

【缺省情况】

设备上不存在任何静态的远端MAC地址表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac*-]*address*：MAC地址，格式为H-H-H，不支持组播MAC地址和全0的MAC地址。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[interface tunnel ***tunnel-number*]：指定远端MAC地址对应的VXLAN隧道接口。*tunnel-number*为VXLAN隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[vsi*** vsi-name*]：指定远端MAC地址所属的VSI。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

远端MAC地址是指VTEP连接的远端站点内虚拟机的MAC地址。远端MAC地址既可以通过本命令静态配置，也可以通过报文中的源MAC地址动态学习、通过IS-IS协议学习。静态配置的远端MAC地址表项优先级高于源MAC地址动态学习和通过IS-IS协议学习的表项。源MAC地址动态学习和通过IS-IS协议学习的表项优先级相同，后生成的表项可以覆盖已经存在的表项。

【举例】

\# 添加一条静态远端MAC地址表项：MAC地址为000f-e201-0101，VXLAN隧道接口为Tunnel1，MAC地址所属的VSI为vsi1。

\<Sysname\> system-view

Sysname mac-address static 000f-e201-0101 interface tunnel 1 vsi vsi1

【相关命令】

·**vxlan tunnel mac-learning disable**

**VXLAN \-- VXLAN基础配置命令 \-- reset arp suppression vsi**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset arp suppression vsi**]命令用来清除VSI的ARP泛洪抑制表项。

【命令】

**[reset arp suppression vsi** [ **name** *vsi-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** vsi-name*]：清除指定VSI的ARP泛洪抑制表项。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除所有VSI的ARP泛洪抑制表项。

【举例】

\# 清除所有VSI的ARP泛洪抑制表项。

\<Sysname\> reset arp suppression vsi

This command will delete all entries. Continue? [Y/N:y]

【相关命令】

·**display arp suppression**** vsi**

·**arp suppression enable**

**VXLAN \-- VXLAN基础配置命令 \-- reset l2vpn mac-address**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[reset l2vpn mac-address**]命令用来清除通过源MAC地址动态学习的MAC地址表项。

【命令】

**[reset l2vpn mac-address ** **vsi**]* vsi-name *

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsi*** vsi-name*]：清除指定VSI动态学习的MAC地址表项。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除所有VSI动态学习的MAC地址表项。

【使用指导】

VSI通过源MAC地址学习到错误的MAC地址表项，或学习的MAC地址表项数目达到最大值时，可以执行本命令，以便重新学习MAC地址表项。

【举例】

\# 清除名为vpn1的VSI通过源MAC地址动态学习的MAC地址表项。

\<Sysname\> reset l2vpn mac-address vsi vpn1

【相关命令】

·**display l2vpn mac-address vsi**

**VXLAN \-- VXLAN基础配置命令 \-- reset l2vpn statistics vsi**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset l2vpn statistics vsi**]命令用来清除VSI的报文统计信息。

【命令】

**[reset l2vpn statistics vsi ** **name** *vsi-name* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** vsi-name*]：清除指定VSI的报文统计信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除所有VSI的信息。

【举例】

\# 清除本设备上所有VSI报文统计信息。

\<Sysname\> reset l2vpn statistics vsi

【相关命令】

·**statistics enable**

**VXLAN \-- VXLAN基础配置命令 \-- selective-flooding mac-address**

------------------------------------------------------------------------

**[selective-flooding mac-addres**]命令用来配置VSI选择性泛洪的MAC地址。

**[undo selective-flooding mac-addres**]命令用来删除VSI的选择性泛洪MAC地址。

【命令】

**[selective-flooding mac-addres** *mac-addres*]

**[undo selective-flooding mac-addres** *mac-addres*]

【缺省情况】

设备上不存在任何VSI选择性泛洪MAC地址。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：选择性泛洪的MAC地址。该MAC地址不能为全F。

【使用指导】

通过**flooding disable**命令关闭VSI的泛洪功能后，为了将某些MAC地址的数据帧泛洪到远端站点以保证某些业务的流量在站点间互通，可以配置选择性泛洪的MAC地址。当数据帧的目的MAC地址匹配选择性泛洪的MAC地址时，该数据帧可以泛洪到远端站点。

【举例】

\# 在VSI vsi1下配置选择性泛洪的MAC地址为000f-e201-0101。

\<Sysname\> system-view

Sysname vsi vsi1

Sysname-vsi-vsi1 selective-flooding mac-address 000f-e201-0101

【相关命令】

·**flooding disable**

**VXLAN \-- VXLAN基础配置命令 \-- service-instance**

------------------------------------------------------------------------

**[service-instance**]命令用来创建以太网服务实例，并进入以太网服务实例视图。

**[undo service-instance**]命令用来删除指定的以太网服务实例。

【命令】

**[service-instance ***instance-id*]

**[undo service-instance ***instance-id*]

【缺省情况】

接口上不存在任何以太网服务实例。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：以太网服务实例的编号，取值范围为1～4096。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1上创建以太网服务实例1，并进入以太网服务实例1的视图。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 1

Sysname-GigabitEthernet1/0/1-srv1

【相关命令】

·**display l2vpn service-instance**

**VXLAN \-- VXLAN基础配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前的VSI。

**[undo shutdown**]命令用来恢复缺省情况。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

VSI处于开启状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭VSI后，该VSI将不能提供二层交换服务。

关闭VSI功能通常用于暂时禁用二层交换服务，但还需要再次启用该服务的场景。关闭VSI后，该VSI所有已存在的配置保持不变。在关闭状态下还可以对VSI进行配置。VSI再次被开启后，基于最新的配置提供二层交换服务。

【举例】

\# 关闭名为vpn1的VSI。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 shutdown

【相关命令】

·**display l2vpn vsi**

**VXLAN \-- VXLAN基础配置命令 \-- statistics enable**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics enable**]命令用来开启指定VSI的报文统计功能。

**[undo statistics enable**]命令用来关闭指定VSI的报文统计功能。

【命令】

**[statistics enable**]

**[undo statistics enable**]

【缺省情况】

VSI的报文统计功能处于关闭状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启名为vpls1的VSI的报文统计功能。

\<Sysname\> system-view

Sysname vsi vpls1

Sysname-vsi-vpls1 statistics enable

【相关命令】

·**reset l2vpn statistics vsi**

**VXLAN \-- VXLAN基础配置命令 \-- tunnel**

------------------------------------------------------------------------

**[tunnel**]命令用来配置VXLAN与指定的隧道关联。

**[undo tunnel**]命令用来取消VXLAN与指定隧道的关联。

【命令】

**[tunnel ***tunnel-number*]

**[undo tunnel ***tunnel-number*]

【缺省情况】

VXLAN没有与任何VXLAN隧道关联。

【视图】

VXLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tunnel-numb*er]：隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在VXLAN组网中，用户可以手工将VXLAN与VXLAN隧道关联。VTEP接收到某个VXLAN的泛洪流量后，如果采用单播路由泛洪方式，则VTEP将在与该VXLAN关联的所有VXLAN隧道上发送该流量，以便将流量转发给所有的远端VTEP。

执行本命令时，需要注意的是：

·本命令指定的隧道必须是VXLAN模式的隧道。

·一个VXLAN可以关联多条VXLAN隧道；一条VXLAN隧道可以关联多个VXLAN。

【举例】

\# 配置VXLAN隧道Tunne0和Tunnel1与VXLAN 10000关联。

\<Sysname\> system

Sysname vsi vpna

Sysname-vsi-vpna vxlan 10000

Sysname-vsi-vpna-vxlan-10000 tunnel 0

Sysname-vsi-vpna-vxlan-10000 tunnel 1

【相关命令】

·**display vxlan tunnel**

**VXLAN \-- VXLAN基础配置命令 \-- tunnel bfd enable**

------------------------------------------------------------------------

**[tunnel bfd enable**]命令用来开启隧道的BFD检测功能。

**[undo tunnel bfd enable**]命令用来恢复缺省情况。

【命令】

**[tunnel bfd enable**]

**[undo tunnel bfd enable**]

【缺省情况】

隧道的BFD检测功能处于关闭状态。

【视图】

VXLAN模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

隧道的BFD检测功能用来避免VTEP设备无法及时感知隧道的故障，导致报文转发失败。

开启隧道的BFD检测功能后，VTEP将自动建立多跳控制报文方式的BFD会话，检测隧道源和目的端之间链路的可达性。BFD检测到链路不可达后，VTEP将Tunnel接口的状态置为down，不再通过该隧道转发报文。

【举例】

\# 开启VXLAN隧道Tunnel9的BFD检测功能。

\<Sysname\> system-view

Sysname interface tunnel 9 mode vxlan

Sysname-Tunnel9 tunnel bfd enable

**VXLAN \-- VXLAN基础配置命令 \-- vsi**

------------------------------------------------------------------------

**[vsi**]命令用来创建一个VSI（Virtual Switching Instance，虚拟交换实例），并进入VSI视图。

**[undo** **vsi**]命令用来删除指定的VSI。

【命令】

**[vsi**] *vsi-name*

**[undo**]**vsi** *vsi-name*

【缺省情况】

设备上不存在任何VSI。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

VSI是VTEP上为一个VXLAN提供二层交换服务的虚拟交换实例。VSI可以看做是VTEP上的一台基于VXLAN进行二层转发的虚拟交换机，它具有传统以太网交换机的所有功能，包括源MAC地址学习、MAC地址老化、泛洪等。VSI与VXLAN一一对应。

【举例】

\# 创建名为vxlan10的VSI，并进入VSI视图。

\<Sysname\> system-view

Sysname vsi vxlan10

Sysname-vsi-vxlan10

【相关命令】

·**display l2vpn vsi**

**VXLAN \-- VXLAN基础配置命令 \-- vxlan**

------------------------------------------------------------------------

**[vxlan**]命令用来创建VXLAN，并进入VXLAN视图。

**[undo vxlan**]命令用来删除指定的VXLAN。

【命令】

**[vxlan ***vxlan-id*]

**[undo vxlan**]

【缺省情况】

设备上不存在任何VXLAN。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vxlan-id*]：VXLAN ID，取值范围为0～16777215。

【使用指导】

在一个VSI下只能创建一个VXLAN。不同VSI下创建的VXLAN，其VXLAN ID不能相同。

【举例】

\# 在名称为vpna的VSI下创建编号为10000的VXLAN，并进入VXLAN视图。

\<Sysname\> system

Sysname vsi vpna

Sysname-vsi-vpna vxlan 10000

Sysname-vsi-vpna-vxlan-10000

【相关命令】

·**vsi**

**VXLAN \-- VXLAN基础配置命令 \-- vxlan invalid-udp-checksum discard**

------------------------------------------------------------------------

**[vxlan invalid-udp-checksum discard**]命令用来配置丢弃UDP校验和检查失败的VXLAN报文。

**[undo vxlan invalid-udp-checksum discard**]命令用来恢复缺省情况。

【命令】

**[vxlan invalid-udp-checksum discard**]

**[undo vxlan invalid-udp-checksum discard**]

【缺省情况】

不会检查VXLAN报文的UDP校验和。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

VTEP对二层数据帧进行封装时，将UDP校验和设置为0。缺省情况下，VTEP接收到VXLAN报文后，不会检查报文的UDP校验和。如果在VTEP上执行了本命令，则该VTEP会对接收的VXLAN报文的UDP校验和进行检查，校验和检查失败的报文将被丢弃。

为了兼容其他厂商的设备，UDP检验和为0和UDP检验和正确的报文均能通过VTEP的检查，被VTEP接收。

【举例】

\# 配置丢弃UDP校验和检查失败的VXLAN报文。

\<Sysname\> system-view

Sysname vxlan invalid-udp-checksum discard

【相关命令】

·**vxlan invalid-vlan-tag discard**

**VXLAN \-- VXLAN基础配置命令 \-- vxlan invalid-vlan-tag discard**

------------------------------------------------------------------------

**[vxlan invalid-vlan-tag discard**]命令用来配置丢弃内层数据帧含有VLAN tag的VXLAN报文。

**[undo vxlan invalid-vlan-tag discard**]命令用来恢复缺省情况。

【命令】

**[vxlan invalid-vlan-tag discard**]

**[undo vxlan invalid-vlan-tag discard**]

【缺省情况】

不会检查VXLAN报文内层封装的以太网数据帧是否携带VLAN tag。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果在VTEP上执行了本命令，则VTEP接收到VXLAN报文并对其解封装后，若内层以太网数据帧带有VLAN tag，则丢弃该VXLAN报文。

远端VTEP上通过**xconnect vsi**命令的**access-mode**参数配置接入模式为**ethernet**时，VXLAN报文可能携带VLAN tag。这种情况下建议不要在本端VTEP上执行**vxlan invalid-vlan-tag discard**命令，以免错误地丢弃报文。

【举例】

\# 配置丢弃内层数据帧含有VLAN tag的VXLAN报文。

\<Sysname\> system-view

Sysname vxlan invalid-vlan-tag discard

【相关命令】

·**vxlan invalid-udp-checksum discard**

·**xconnect vsi**

**VXLAN \-- VXLAN基础配置命令 \-- vxlan local-mac report**

------------------------------------------------------------------------

**[vxlan local-mac report**]命令用来开启VXLAN本地MAC地址添加/删除的日志功能。

**[undo vxlan local-mac report**]命令用来恢复缺省情况。

【命令】

**[vxlan local-mac report**]

**[undo vxlan local-mac report**]

【缺省情况】

VXLAN添加/删除本地MAC地址时不会记录日志。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行本配置后，VXLAN添加、删除本地MAC地址时，将产生日志信息。生成的日志信息将被发送到设备的信息中心，通过设置信息中心的参数，决定日志信息的输出规则（即是否允许输出以及输出方向）。

【举例】

\# 开启VXLAN本地MAC地址添加/删除的日志功能。

\<Sysname\> system-view

Sysname vxlan local-mac report

**VXLAN \-- VXLAN基础配置命令 \-- vxlan tunnel mac-learning disable**

------------------------------------------------------------------------

**[vxlan tunnel mac-learning disable**]命令用来关闭远端MAC地址自动学习功能。

**[undo vxlan tunnel mac-learning disable**]命令用来恢复缺省情况。

【命令】

**[vxlan tunnel mac-learning disable**]

**[undo vxlan tunnel mac-learning disable**]

【缺省情况】

远端MAC地址自动学习功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

远端MAC地址是指VTEP连接的远端站点内虚拟机的MAC地址。远端MAC地址可以通过报文中的源MAC地址动态学习。

缺省情况下，设备可以自动学习远端MAC地址。如果网络中存在攻击，为了避免学习到错误的远端MAC地址，可以通过本命令手工关闭远端MAC地址自动学习功能。

【举例】

\# 关闭远端MAC地址自动学习功能。

\<Sysname\> system-view

Sysname vxlan tunnel mac-learning disable

**VXLAN \-- VXLAN基础配置命令 \-- vxlan udp-port**

------------------------------------------------------------------------

**[vxlan udp-port**]命令用来配置VXLAN报文的目的UDP端口号。

**[undo vxlan udp-port**]命令用来恢复缺省情况。

【命令】

**[vxlan udp-port ***port-number*]

**[undo vxlan udp-port**]

【缺省情况】

VXLAN报文的目的UDP端口号为4789。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：VXLAN报文的目的UDP端口号，取值范围为1～65535。

【使用指导】

属于同一个VXLAN的VTEP设备上需要配置相同的UDP端口号。

建议不要将VXLAN报文的目的UDP端口号配置为知名端口，即1～1023之间的端口。

【举例】

\# 配置VXLAN报文的目的UDP端口号为6666。

\<Sysname\> system-view

Sysname vxlan udp-port 6666

**VXLAN \-- VXLAN基础配置命令 \-- xconnect vsi**

------------------------------------------------------------------------

**[xconnect vsi**]命令用来将AC与VSI关联。

**[undo** **xconnect vsi**]命令用来取消AC与VSI的关联。

【命令】

**[xconnect vsi ***vsi-name *[[ **access-mode** { **ethernet** \| **vlan** } ]]]

**[undo xconnect vsi**]

【缺省情况】

AC没有与VSI关联。

【视图】

接口视图/以太网服务实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

**[access-mode**]：指定接入模式。当关联VSI的AC为三层以太网子接口、VLAN接口、以太网服务实例时，接入模式缺省为VLAN；其他情况下，接入模式缺省为Ethernet。

**[ethernet**]：指定接入模式为Ethernet。

**[vlan**]：指定接入模式为VLAN。

【使用指导】

在接口视图下执行本命令后，从接口接收到的报文将通过查找关联VSI的MAC地址表进行转发；在某个接口的以太网服务实例视图下执行本命令后，从该接口接收到的、符合以太网服务实例报文匹配规则的报文，将通过查找关联VSI的MAC地址表进行转发。

接入模式分为以下两种：

·VLAN接入模式：从本地站点接收到的、发送给本地站点的以太网帧必须带有VLAN tag。VTEP从本地站点接收到以太网帧后，删除该帧的所有VLAN tag，再转发该数据帧；VTEP发送以太网帧到本地站点时，为其添加VLAN tag。采用该模式时，VTEP不会传递VLAN tag信息，不同站点可以独立地规划自己的VLAN，不同站点的不同VLAN之间可以互通。

·Ethernet接入模式：从本地站点接收到的、发送给本地站点的以太网帧可以携带VLAN tag，也可以不携带VLAN tag。VTEP从本地站点接收到以太网帧后，保持该帧的VLAN tag信息不变，转发该数据帧；VTEP发送以太网帧到本地站点时，不会为其添加VLAN tag。采用该模式时，VTEP会在不同站点间传递VLAN tag信息，不同站点的VLAN需要统一规划，否则无法互通。

需要注意的是，在以太网服务实例下配置该命令前，必须先配置**encapsulation**命令。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1下关联名为vpn1的VSI。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 xconnect vsi vpn1

·交换应用

\# 接口GigabitEthernet1/0/1下采用以太网服务实例200来匹配外层VLAN为200的报文，将该以太网服务实例与名为vpn1的VSI关联。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 200

Sysname-GigabitEthernet1/0/1-srv200 encapsulation s-vid 200

Sysname-GigabitEthernet1/0/1-srv200 xconnect vsi vpn1

【相关命令】

·**display l2vpn interface**

·**display l2vpn service-instance**

·**encapsulation**

·**vsi**

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery client member**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display vxlan neighbor-discovery client member**]命令用来在ENDC上显示ENDC学到的邻居信息。

【命令】

**[display vxlan neighbor-discovery client member**[ [ **interface** **tunnel** *interface-number* \| **local** *local-ip* ]]｜ **remote**[ *client-ip* \| **server** *server-ip* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示通过指定NVE隧道接口学到的邻居信息。*interface-number*为Tunnel接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[local ***local-ip*]：显示通过源端地址为指定IPv4地址的NVE隧道接口学到的邻居信息。*local-ip*表示NVE隧道接口的源端地址，即本地ENDC的IPv4地址。

**[remote ***client-ip*]：显示设备学到的指定邻居ENDC的信息。*client-ip*表示邻居ENDC的IPv4地址。

**[server ***server-ip*]：显示通过指定ENDS学到的邻居信息。*server-ip*表示ENDS的IPv4地址。

【使用指导】

通过本命令可以查看ENDC学到的邻居信息，包括邻居的IPv4地址、桥MAC地址、创建时间、老化时间、邻居之间的VXLAN隧道状态等信息。

如果不指定任何参数，将显示ENDC学到的所有邻居信息。

【举例】

\# 显示ENDC学到的所有IPv4邻居信息。

\<Sysname\> display vxlan neighbor-discovery client member

Interface: Tunnel0    Network ID: 1

Local Address: 20.0.0.2

Server Address: 20.0.1.1

Neighbor        System ID         Created Time           Expire    Status

20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    13        Up

20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    12        Up

Interface: Tunnel0    Network ID: 1

Local Address: 20.0.0.2

Server Address: 20.0.1.2

Neighbor        System ID         Created Time           Expire    Status

20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up

20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Up

Interface: Tunnel1    Network ID: 2

Local Address: 21.0.0.1

Server Address: 21.0.1.2

Neighbor        System ID         Created Time           Expire    Status

21.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up

21.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Down

Interface: Tunnel2    Network ID: 3

Local Address: 21.0.0.2

Server Address: NA

Neighbor        System ID         Created Time           Expire    Status

21.0.2.1        NA                2011/01/01 12:12:12    25        Up

21.0.3.1        NA                2011/01/01 12:12:12    19        Up

表1-8 display vxlan neighbor-discovery client member命令显示信息描述表

字段

描述

Interface

启动ENDC功能的接口名称

Network ID

隧道的Network ID

Local Address

NVE隧道接口的源端地址

Server Address

ENDS的IPv4地址，NA表示ENDS未知

Neighbor

通过ENDS学到的邻居IPv4地址

System ID

邻居的桥MAC地址，NA表示桥MAC地址未知

Created Time

邻居创建的时间

Expire

邻居的老化时间，单位为秒

Status

与邻居之间VXLAN 隧道的状态：

·Up：表示可以通过VXLAN隧道进行传输

·Down：表示不可以通过VXLAN隧道进行传输

·NA：表示尚未创建VXLAN隧道

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery client statistics**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display vxlan neighbor-discovery client statistics**]命令用来在ENDC上显示ENDC的统计信息。

【命令】

**[display vxlan neighbor-discovery client statistics interface tunnel*** interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定NVE隧道接口对应的ENDC的统计信息。*interface-number*为Tunnel接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

通过本命令可以查看开启ENDC功能后，接口收到和发送ENDP报文的统计信息。

【举例】

\# 显示NVE隧道接口Tunnel0对应的ENDC的统计信息。

\<Sysname\> display vxlan neighbor-discovery client statistics interface tunnel 0

Server Address: 10.0.0.1

Received packets:

  Reply:        170              Error:      1

Sent packets:

  Register:     170              Purge:      0

Server Address: 10.0.0.2

Received packets:

  Reply:        99               Error:      1

Sent packets:

  Register:     100              Purge:      0

表1-9 display vxlan neighbor-discovery client statistics命令显示信息描述表

字段

描述

Server Address

ENDC对应的ENDS的IP地址

Received packets

ENDC收到的报文统计信息：

·Reply：表示注册应答报文

·Error：表示错误指示报文

Sent packets

ENDC发送的报文统计信息：

·Register：表示注册报文

·Purge：表示注销报文

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery client summary**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display vxlan neighbor-discovery client summary**]命令用来在ENDC上显示ENDC的运行信息。

【命令】

**[display vxlan neighbor-discovery client summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

通过本命令可以查看ENDC的运行信息，包括ENDC的配置信息、ENDC与ENDS的连接状态。

【举例】

\# 显示ENDC的运行信息。

\<Sysname\> display vxlan neighbor-discovery client summary

                         Status: I-Init  E-Establish  P-Probe

Interface    Local Address   Server Address  Network ID  Reg  Auth      Status

Tunnel0      20.0.0.2        20.0.0.1        1           15   enabled   E

Tunnel0      20.0.0.2        20.0.0.3        1           15   enabled   P

Tunnel1      21.0.0.2        21.0.0.1        2           15   disabled  P

表1-10 display vxlan neighbor-discovery client summary命令显示信息描述表

字段

描述

Interface

启动ENDC功能的接口名称

Local Address

本地NVE隧道接口的源端地址，NA表示未配置

Server Address

ENDS的IPv4地址

Network ID

隧道的Network ID，NA表示未配置

Reg

注册时间间隔，单位为秒

Auth

是否开启认证功能：

·enabled：表示已开启

·disabled：表示未开启

Status

ENDC与ENDS的连接状态：

·I：表示初始状态

·E：表示已建立连接

·P：表示未建立连接正在探测

【相关命令】

·**vxlan neighbor-discovery authentication**

·**vxlan neighbor-discovery client enable**

·**vxlan neighbor-discovery client register-interval**

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery server member**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display vxlan neighbor-discovery server member**]命令用来在ENDS上显示ENDS学到的成员信息。

【命令】

**[display vxlan neighbor-discovery server member**[ [ **interface** **tunnel** *interface-number* \| **local** *local-ip* \| **remote** *client-ip* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示通过指定NVE隧道接口学到的成员信息。*interface-number*为Tunnel接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[local ***local-ip*]：显示指定ENDS学到的成员信息。*local-ip*表示本地ENDS的IPv4地址。

**[remote ***client-ip*]：显示ENDS学到的指定IPv4地址的成员信息。*client-ip*表示ENDC的IPv4地址。

【使用指导】

通过本命令可以查看ENDS学到的成员信息，包括成员的IPv4地址、桥MAC地址、创建时间、老化时间等信息。

如果不指定任何参数，将显示ENDS学到的所有成员信息。

【举例】

\# 显示ENDS学到的所有IPv4成员信息。

\<Sysname\> display vxlan neighbor-discovery server member

Interface: Tunnel0    Network ID: 1

IP Address: 11.0.0.1

Client Address  System ID         Expire    Created Time

11.0.0.3        000F-0001-0001    25        2011/01/01 00:00:43

11.0.0.4        000F-0001-0002    15        2011/01/01 01:00:46

11.0.0.5        000F-0001-0003    20        2011/01/01 01:02:13

Interface: Tunnel1    Network ID: 2

IP Address: 11.0.1.2

Client Address  System ID         Expire    Created Time

11.0.1.3        000F-0001-0011    19        2011/01/01 00:19:31

11.0.1.4        000F-0001-0012    30        2011/01/01 02:00:43

11.0.1.5        000F-0001-0013    20        2011/01/01 01:02:13

Interface: Tunnel2    Network ID: 3

IP Address: 12.0.0.1

Client Address  System ID         Expire    Created Time

12.0.0.2        000F-0002-0001    30        2011/01/01 03:20:43

12.0.0.3        000F-0002-0002    37        2011/01/01 03:27:46

表1-11 display vxlan neighbor-discovery server member命令显示信息描述表

字段

描述

Interface

启动ENDS功能的接口名称

Network ID

隧道的Network ID

IP Address

ENDS的IPv4地址

Client Address

学到的成员的IPv4地址

System ID

学到的成员的桥MAC地址

Expire

成员的剩余老化时间，单位为秒

Created Time

成员的创建时间

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery server statistics**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display vxlan neighbor-discovery server statistics**]命令用来在ENDS上显示ENDS的统计信息。

【命令】

**[display vxlan neighbor-discovery server statistics interface tunnel*** interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定NVE隧道接口对应的ENDS的统计信息。*interface-number*为Tunnel接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

通过本命令可以查看开启ENDS功能后，接口收到和发送报文的统计信息。

【举例】

\# 显示NVE隧道接口Tunnel0对应的ENDS的统计信息。

\<Sysname\> display vxlan neighbor-discovery server statistics interface tunnel 0

Received packets:

  Register:     170              Purge:      13

Sent packets:

  Reply:        170              Error:      1

表1-12 display vxlan neighbor-discovery server statistics命令显示信息描述表

字段

描述

Received packets

ENDS收到的报文统计信息：

·Register：表示注册报文

·Purge：表示注销报文

Sent packets

ENDS发送的报文统计信息：

·Reply：表示注册应答报文

·Error：表示错误指示报文

**VXLAN \-- ENDP配置命令 \-- display vxlan neighbor-discovery server summary**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display vxlan neighbor-discovery server summary**]命令用来在ENDS上显示ENDS的运行信息。

【命令】

**[display vxlan neighbor-discovery server summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

通过本命令可以查看ENDS的运行信息，包括ENDS的配置信息、通过该ENDS学习到的ENDC个数。

【举例】

\# 显示ENDS的运行信息。

\<Sysname\> display vxlan neighbor-discovery server summary

Interface      Local Address   Network ID    Auth        Members

Tunnel0        20.0.0.1        1             enabled     10

Tunnel2        21.0.0.1        2             disabled    20

Tunnel3        22.0.0.1        NA            disabled    0

表1-13 display vxlan neighbor-discovery server summary命令显示信息描述表

字段

描述

Interface

启动ENDS功能的接口名称

Local Address

接口的源端地址，NA表示未配置

Network ID

隧道的Network ID，NA表示未配置

Auth

是否开启认证功能：

·enabled：表示已开启

·disabled：表示未开启

Members

通过该ENDS学习到的ENDC个数

【相关命令】

·**vxlan neighbor-discovery authentication**

·**vxlan neighbor-discovery server enable**

**VXLAN \-- ENDP配置命令 \-- network-id**

------------------------------------------------------------------------

**[network-id**]命令用来配置隧道的Network ID。

**[undo network-id**]命令用来删除隧道的Network ID。

【命令】

**[network-id** *network-id*]

**[undo network-id**]

【缺省情况】

没有配置隧道的Network ID。

【视图】

NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：Network ID值，取值范围为1～16777215。

【使用指导】

VXLAN通过ENDP来自动发现远端VTEP。ENDP可以划分为多个实例，通过Network ID来标识ENDP实例。只有属于同一个ENDP实例的VTEP之间可以互相发现。

需要注意的是，同一台设备的不同Tunnel接口下必须配置不同的Network ID。

【举例】

\# 配置NVE隧道Tunnel0的Network ID为123。

\<Sysname\> system-view

Sysname interface tunnel 0 mode nve

Sysname-Tunnel0 network-id 123

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery authentication**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vxlan neighbor-discovery authentication**]命令用来开启ENDP认证功能。

**[undo vxlan neighbor-discovery authentication**]命令用来关闭ENDP认证功能。

【命令】

**[vxlan neighbor-discovery authentication**[ { **cipher** \| **simple** } ]]*password*

**[undo vxlan neighbor-discovery authentication**]

【缺省情况】

ENDP认证功能处于关闭状态。

【视图】

NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置认证密码。

**[simple**]：表示以明文方式设置认证密码。

*[password*]：设置的明文认证密码或密文认证密码，区分大小写。明文认证密码为1～24个字符的字符串；密文认证密码为1～65个字符的字符串。

【使用指导】

为了安全起见，可以配置ENDP认证功能来防止恶意的节点注册到VXLAN网络。

开启ENDP认证功能后，发送ENDP报文的设备会使用配置的密码和MD5算法对报文进行摘要运算，然后把运算结果放到报文的认证字段。对端设备收到ENDP报文后，如果该设备未配置认证功能，则认为报文合法；如果设备配置了认证功能，则利用本端配置的密码和MD5算法对报文进行摘要运算，然后比较运算结果与报文认证字段携带的信息是否一致，如果一致则认为报文合法，如果不一致则认为报文非法。

只有本端与对端设备上都没有配置ENDP认证功能，或者都配置了认证功能且认证密码相同，才能在二者之间成功建立VXLAN隧道。

在一个安全的网络中，可以不配置ENDP认证功能。

需要注意的是：

·同一个VXLAN网络中所有的ENDS与ENDC必须配置相同的认证密码。

·以明文或密文方式设置的认证密码，均以密文的方式保存在配置文件中。

【举例】

\# 开启ENDP认证功能，并以明文方式设置认证密码为web-vxlan。

\<Sysname\> system

Sysname interface tunnel 0 mode nve

Sysname-Tunnel0 vxlan neighbor-discovery authentication simple web-vxlan

【相关命令】

·**display vxlan neighbor-discovery client summary**

·**display vxlan neighbor-discovery server summary**

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery client enable**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vxlan neighbor-discovery client enable**]命令用来开启接口的ENDC功能，并指定ENDS地址。

**[undo vxlan neighbor-discovery client enable**]命令用来关闭接口的ENDC功能。

【命令】

**[vxlan neighbor-discovery client enable ***server-ip*]

**[undo vxlan neighbor-discovery client enable** *server-ip*]

【缺省情况】

ENDC功能处于关闭状态。

【视图】

NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-ip*]：ENDC要连接的ENDS的IP地址。

【使用指导】

为了防止ENDS异常导致ENDC不能加入VXLAN网络，用户可以通过重复执行本命令为每个ENDC指定两个ENDS。ENDC同时向两个ENDS注册和获取ENDC信息。

需要注意的是，建议为地址相同、Network ID不同的ENDC指定不同的ENDS。

【举例】

\# 开启ENDC功能，并指定ENDS地址为11.0.0.1。

\<Sysname\> system

Sysname interface tunnel 0 mode nve

Sysname-Tunnel0 vxlan neighbor-discovery client enable 11.0.0.1

【相关命令】

·**display vxlan neighbor-discovery client summary**

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery client register-interval**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vxlan neighbor-discovery client register-interval**]命令用来配置ENDC向ENDS注册的时间间隔。

**[undo vxlan neighbor-discovery client register-interval**]命令用来恢复缺省情况。

【命令】

**[vxlan neighbor-discovery client register-interval**]*time-value*

**[undo vxlan neighbor-discovery client register-interval**]

【缺省情况】

ENDC向ENDS注册的时间间隔为15秒。

【视图】

NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-value*]：注册时间间隔，取值范围为5～120，单位为秒。

【使用指导】

ENDP协议中定义了3个定时器：探测定时器、注册定时器、老化定时器。

·探测定时器

ENDC请求加入VXLAN网络时会启用探测定时器，该定时器以5秒的时间间隔定时向ENDS发送注册报文，收到ENDS应答报文后会停止探测定时器。

·注册定时器

ENDC加入VXLAN网络后，为了通告自己工作正常，会定时向ENDS发送注册报文，该定时器的默认时间间隔为15秒，用户可以通过配置**vxlan neighbor-discovery client register-interval**命令来调整该时间间隔。

如果ENDC连续发送5个注册报文，都未能收到ENDS的应答报文，则认为网络故障，此时需要清除之前学到的邻居信息，同时重新启用探测定时器。

·老化定时器

ENDC向ENDS发送的注册报文中携带注册时间间隔，ENDS会记录该时间间隔。

ENDC加入VXLAN网络后，如果ENDS在5倍的注册时间内未收到ENDC的注册报文则认为ENDC出现故障，此时需要把ENDC从VXLAN网络中删除。

【举例】

\# 配置ENDC向ENDS注册的时间间隔为30秒。

\<Sysname\> system

Sysname interface tunnel 0 mode nve

Sysname-Tunnel0 vxlan neighbor-discovery client register-interval 30

【相关命令】

·**display vxlan neighbor-discovery client summary**

**VXLAN \-- ENDP配置命令 \-- vxlan neighbor-discovery server enable**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vxlan neighbor-discovery server enable**]命令用来开启接口的ENDS功能。

**[undo vxlan neighbor-discovery server enable**]命令用来关闭接口的ENDS功能。

【命令】

**[vxlan neighbor-discovery server enable**]

**[undo vxlan neighbor-discovery server enable**]

【缺省情况】

ENDS功能处于关闭状态。

【视图】

NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启接口的ENDS功能时，会同时开启该接口的ENDC功能（该ENDC对应的ENDS地址为该接口的源地址）。

【举例】

\# 开启ENDS功能。

\<Sysname\> system

Sysname interface tunnel 0 mode nve

Sysname-Tunnel0 vxlan neighbor-discovery server enable

【相关命令】

·**display vxlan neighbor-discovery server summary**

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis brief**

------------------------------------------------------------------------

**[display vxlan isis brief**]命令用来显示VXLAN IS-IS进程的摘要信息。

【命令】

**[display vxlan isis brief**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示VXLAN IS-IS进程的摘要信息。

\<Sysname\> display vxlan isis brief

Network-entity: 00.0011.2200.0001.00

LSP-length receive: 16384

LSP-length originate: 1400

Timers:

  LSP-max-age: 1200s

  LSP-refresh: 900s

State: Enabled

表1-14 display vxlan isis brief命令显示信息描述表

字段

描述

Network-entity

网络实体名称

LSP-length receive

可以接收LSP的最大长度

LSP-length originate

生成的LSP的最大长度

Timers

LSP-max-age

LSP的最大生存时间，单位为秒

LSP-refresh

LSP的刷新周期，单位为秒

State

VXLAN IS-IS进程的运行状态，取值包括：

·Enabled：表示VXLAN IS-IS进程处于开启状态，即已经开启VXLAN IS-IS的MAC地址同步功能或VXLAN自动协商功能

·Disabled：表示VXLAN IS-IS进程处于关闭状态，即尚未开启VXLAN IS-IS的MAC地址同步功能和VXLAN自动协商功能

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis graceful-restart status**

------------------------------------------------------------------------

**[display vxlan isis graceful-restart status**]命令用来显示VXLAN IS-IS协议的GR状态。

【命令】

**[display vxlan isis graceful-restart status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示VXLAN IS-IS协议的GR状态。

\<Sysname\> display vxlan isis graceful-restart status

Restart status: RESTARTING

Restart phase: LSDB synchronization

Restart interval: 300s

T3 remaining time: 65531s

Total number of interfaces: 1

Number of waiting LSPs: 0

T2 remaining time: 56s

  Interface: Tunnel0

    T1 remaining time: 2

    RA received: N

    CSNP received: N

    T1 expired number: 3

表1-15 display vxlan isis graceful-restart status命令显示信息描述表

字段

描述

Restart status

重启状态，取值包括：

·COMPLETE：重启完成{.TableTextChar}

·{.TableTextChar}STARTING：重启开始{.TableTextChar}

·{.TableTextChar}RESTARTING：重启中{.TableTextChar}

·UNKNOWN：未知状态{.TableTextChar}

Restart phase

重启阶段，取值包括：

·Initialization：初始阶段

·LSDB synchronization：LSDB同步阶段

·MAC receiving：接收本地MAC地址上报的阶段

·LSP stable：LSP生成的阶段

·LSP generation：LSP刷新和泛洪的阶段

·Finish：GR完成的阶段

·Unknown：未知阶段

Restart interval

重启间隔时间，单位为秒

重启间隔时间即T2定时器的值，用来控制LSDB同步时间。如果在GR重启间隔时间内没有完成LSDB同步，则GR失败，退出GR过程

该值可以通过**graceful-restart interval**命令设置

T3 remaining time

定时器T3的剩余时间，单位为秒

在T3定时器内邻居不会断掉与重启设备的邻接关系。如果T3定时器超时后GR还没有完成，则GR失败

T3定时器的值不可配置

Total number of interfaces

VXLAN IS-IS进程下的接口数

Number of waiting LSPs

GR Restarter与GR Helper进行LSDB同步时，未完成同步的LSP数目

T2 remaining time

定时器T2的剩余时间，单位为秒

T2定时器用来控制LSDB的同步时间

Interface

指定接口下VXLAN IS-IS协议的GR状态

T1 remaining time

定时器T1的剩余时间，单位为秒

T1定时器用来控制带RR（Restart Request，Restart请求）标志位的Hello报文的重传时间。如果在T1定时器内没有接收到对端回复的带有RA（Restart Acknowledgement，Restart应答）标志的Hello报文，则重传带RR标志位的Hello报文

T1定时器的值不可配置

RA received

接口上是否收到邻居发送的带RA标志位的Hello报文

CSNP received

接口上是否收到完整的CSNP报文，即是否完成与GR Helper的LSDB同步

T1 expired number

定时器T1的超时次数，超时达到10次后，不会再进行带RR标志位的Hello报文的重传

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis local-mac**

------------------------------------------------------------------------

**[display vxlan isis local-mac**]命令用来显示VXLAN IS-IS的本地MAC地址信息。

【命令】

**[display vxlan isis local-mac dynamic** [ [ **vxlan-id** *vxlan-id*   **count**  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dynamic**]：显示本地动态MAC地址信息。

**[vxlan-id ***vxlan-id*]：显示指定VXLAN的本地MAC地址信息。*vxlan-id*表示VXLAN编号，取值范围为0～16777215。如果不指定本参数，将显示所有VXLAN的本地MAC地址信息。

**[count**]：显示本地MAC地址的数目。

【举例】

\# 显示所有VXLAN IS-IS的本地动态MAC地址信息。

\<Sysname\> display vxlan isis local-mac dynamic

  VXLAN ID: 100

    MAC address: 00aa-00bb-00cc

    MAC address: 00aa-00cc-00bb

    MAC address: 00cc-00aa-00bb

  VXLAN ID: 50

    MAC address: 00bb-00aa-00cc

    MAC address: 00bb-00cc-00aa

\# 显示VXLAN IS-IS的本地动态MAC地址的数目。

\<Sysname\> display vxlan isis local-mac dynamic count

5 MAC addresses found.

表1-16 display vxlan isis local-mac命令显示信息描述表

字段

描述

VXLAN ID

VXLAN编号

MAC address

MAC地址

5 MAC addresses found

本地MAC地址的数目，本例中本地MAC地址的数目为5

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis lsdb**

------------------------------------------------------------------------

**[display vxlan isis lsdb**]命令用来显示VXLAN IS-IS的链路状态数据库。

【命令】

**[display vxlan isis lsdb**[ [ **local** \| **lsp-id** *lsp-id* \| **verbose** ] \*  **tunnel** *tunnel-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[local**]：显示当前设备产生的LSP的信息。

**[lsp-id** *lsp-id*]：显示指定LSP的信息。*lsp-id*为LSP标识，形式为SYSID*.*Pseudonode ID-fragment num，其中，SYSID是产生该LSP的节点或伪节点的System ID，Pseudonode ID是伪节点ID，fragment num是该LSP的分片号。

**[verbose**]：显示链路状态数据库中的LSP的详细信息。如果不指定本参数，将显示链路状态数据库中的LSP的摘要信息。

**[tunnel** *tunnel-number*]：显示指定Tunnel接口下的LSP信息。*tunnel-number*为隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 显示VXLAN IS-IS链路状态数据库的摘要信息。

\<Sysname\> display vxlan isis lsdb

          Link state database information for VXLAN ISIS (Tunnel 0)

LSP ID                   Seq num     Checksum  Holdtime  Length    Overload

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0011.2200.0201.0000-00   0x00000063  0x1bc2    1104      74        0

0011.2200.0401.0000-00\*  0x00000060  0x7f76    1089      55        0

0011.2200.0401.0001-00\*  0x0000005f  0xf77     1175      57        0

Flags: \*-Self LSP, +-Self LSP(Extended)

\# 显示VXLAN IS-IS链路状态数据库的详细信息。

\<Sysname\> display vxlan isis lsdb verbose

          Link state database information for VXLAN ISIS (Tunnel 0)

LSP ID: 0011.2200.0201.0000-00

Sequence number: 0x00000063

Checksum: 0x1bc2

Holdtime: 745s

Length: 74

Overload: 0

Source: 0011.2200.0201.0000

Neighbour

    ID: 0011.2200.0401.0001, Cost: 10

VXLANs:

    VXLAN ID: 100

    VXLAN ID: 10

MAC addresses:

  VXLAN ID: 10   Confidence: 1

    0001-0001-0001

LSP ID: 0011.2200.0401.0000-00\*

Sequence number: 0x00000060

Checksum: 0x7f76

Holdtime: 730s

Length: 55

Overload: 0

Source: 0011.2200.0401.0000

Neighbour

    ID: 0011.2200.0401.0001, Cost: 10

VXLANs:

    VXLAN ID: 10

LSP ID: 0011.2200.0401.0001-00\*

Sequence number: 0x0000005f

Checksum: 0xf77

Holdtime: 816s

Length: 57

Overload: 0

Source: 0011.2200.0401.0001

Neighbour

    ID: 0011.2200.0201.0000, Cost: 0

    ID: 0011.2200.0401.0000, Cost: 0

Flags: \*-Self LSP, +-Self LSP(Extended)

表1-17 display vxlan isis lsdb命令显示信息描述表

字段

描述

Link state database information for VXLAN IS-IS (Tunnel 1)

Tunnel1上VXLAN IS-IS的链路状态数据库信息

LSP ID

链路状态报文ID

·带\*号表示是本地生成的、原始系统LSP

·带+号表示是本地生成的、虚拟系统LSP（LSP扩展分片）

Sequence number

LSP序列号

Checksum

LSP校验和

Holdtime

LSP生存时间，随着时间推移递减，单位为秒

Length

LSP长度

Overload

LSP中Overload bit的置位情况。1表示置位，0表示没有置位

Source

LSP生成路由器的System ID

Neighbour

LSP生成路由器的邻居信息

ID

邻居的System ID

Cost

LSP生成路由器和邻居之间链路的开销值

VXLANs

LSP中包含的VXLAN信息

VXLAN ID

通过LSP发布的VXLAN的编号

MAC addresses

LSP中包含的MAC地址信息

VXLAN ID

MAC地址所属的VXLAN的编号

Confidence

可信度，取值为0表示可信，取值为1表示不可信。当MAC地址出现冲突时，优选可信度为0的MAC地址

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis peer**

------------------------------------------------------------------------

**[display vxlan isis peer**]命令用来显示VXLAN IS-IS的邻居信息。

【命令】

**[display vxlan isis peer**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示VXLAN IS-IS的邻居信息。

\<Sysname\> display vxlan isis peer

System ID: 0011.2200.0201

Link interface: Tunnel1

Circuit ID: 0011.2200.0401.0001

State: Up

Hold time: 26s

Neighbour DED priority: 64

Uptime: 00:01:24

表1-18 display vxlan isis peer命令显示信息描述表

字段

描述

System ID

邻居的系统ID

Link interface

与对端相连的本地Tunnel接口

Circuit ID

链路ID

State

邻居状态，取值包括：

·Init：邻居初始化

·Up：邻接关系建立

·Down：邻接关系断开

Hold time

存活时间，随着时间推移递减，单位为秒

如果在存活时间内还没有收到邻居发送的Hello报文，则认为邻居已经失效，如果收到了Hello报文，则存活时间将重置为初始值

Neighbour DED Priority

邻居接口DED优先级，DED优先级数值高的设备被选为DED

Uptime

邻居关系保持的时间

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis remote-mac**

------------------------------------------------------------------------

**[display vxlan isis remote-mac**]命令用来显示通过VXLAN IS-IS学习到的远端MAC地址信息。

【命令】

**[display vxlan isis remote-mac** [ [ **vxlan-id** *vxlan-id*   **count**  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vxlan-id ***vxlan-id*]：显示指定VXLAN的远端MAC地址信息。*vxlan-id*表示VXLAN编号，取值范围为0～16777215。如果不指定本参数，将显示所有VXLAN的远端MAC地址信息。

**[count**]：显示远端MAC地址的数目。

【举例】

\# 显示通过VXLAN IS-IS学习到的所有远端MAC地址信息。

\<Sysname\> display vxlan isis remote-mac

MAC Flags: A-MAC received on an active tunnel interface.

           C-MAC conflict with local dynamic MAC.

           F-MAC has been flushed to the remote MAC address table.

  VXLAN ID: 10

    MAC address: 0001-0001-0001

      Interface: Tunnel1

          Flags: AF

\# 显示通过VXLAN IS-IS学习到的所有远端MAC地址的数目。

\<Sysname\> display vxlan isis remote-mac count

1 MAC addresses found.

表1-19 display vxlan isis remote-mac命令显示信息描述表

字段

描述

VXLAN ID

VXLAN的编号

MAC address

通过VXLAN IS-IS学习到的远端MAC地址

Interface

远端MAC地址对应的Tunnel接口

Flags

VXLAN IS-IS远端MAC地址标记，取值包括：

·A：该MAC地址从有效的Tunnel接口接收到

·C：该MAC地址与VXLAN IS-IS本地动态MAC地址冲突

·F：该MAC地址已经下发到远端MAC地址表

1 MAC address(es) found

远端MAC地址的数目，本例中远端MAC地址的数目为1

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis remote-vxlan**

------------------------------------------------------------------------

**[display vxlan isis remote-vxlan**]命令用来显示通过VXLAN IS-IS学习到的远端VXLAN信息。

【命令】

**[display vxlan isis remote-vxlan**[ [ *vxlan-id* \| **count** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vxlan-id*]：显示指定远端VXLAN的信息。*vxlan-id*表示VXLAN编号，取值范围为0～16777215。如果不指定本参数，将显示所有VXLAN的信息。

**[count**]：显示远端VXLAN的数目。

【举例】

\# 显示通过VXLAN IS-IS学习到的所有远端VXLAN的信息。

\<Sysname\> display vxlan isis remote-vxlan

VXLAN Flags: S-VXLAN supported at the local end.

             F-The association between VXLAN and Tunnels has been flushed to L2VPN.

      VXLAN ID: 10

      Tunnels: 1, 3-5

      Flags: SF

\<Sysname\> display vxlan isis remote-vxlan count

1 remote VXLANs found.

表1-20 display vxlan isis remote-mac命令显示信息描述表

字段

描述

VXLAN ID

VXLAN IS-IS学习到的远端VXLAN

Tunnels

远端VXLAN关联的VXLAN隧道

Flags

远端VXLAN标记，取值包括：

·S：本地支持该远端VXLAN

·F：该VXLAN与隧道的关联关系已经通知给L2VPN

·N/A：本地不支持该远端VXLAN

1 remote VXLANs found

远端VXLAN的数目

**VXLAN \-- VXLAN IS-IS配置命令 \-- display vxlan isis tunnel**

------------------------------------------------------------------------

**[display vxlan isis tunnel**]命令用来显示Tunnel接口的VXLAN IS-IS信息。

【命令】

**[display vxlan isis tunnel** [ *tunnel-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[tunnel-number*]：显示指定Tunnel接口的VXLAN IS-IS信息。如果不指定本参数，将显示所有Tunnel接口上的VXLAN IS-IS信息。

【举例】

\# 显示Tunnel接口101的VXLAN IS-IS信息。

\<Sysname\> display vxlan isis tunnel 101

Tunnel101

MTU: 1400

DED: Yes

DED priority: 80

Hello timer: 10s

Hello multiplier: 3

CSNP timer: 10s

LSP timer: 100ms

Max LSP transmit number: 5

VXLANs:

  1,50,100

表1-21 display vxlan isis tunnel命令显示信息描述表

字段

描述

Tunnel

VXLAN隧道接口编号

MTU

链路MTU值

DED

是否被选举为DED：Yes表示是；No表示否

DED priority

DED优先级

Hello timer

Hello报文发送时间间隔，单位为秒

Hello multiplier

Hello报文失效数目

CSNP timer

CSNP报文发送时间间隔，单位为秒

LSP timer

LSP的最小发送时间间隔，单位为毫秒

Max LSP transmit number

一次最多可以发送的LSP数目

VXLANs

与Tunnel接口关联的VXLAN

**VXLAN \-- VXLAN IS-IS配置命令 \-- graceful-restart**

------------------------------------------------------------------------

**[graceful-restart**]命令用来使能VXLAN IS-IS的GR能力。

**[undo graceful-restart**]命令用来关闭VXLAN IS-IS的GR能力。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

VXLAN IS-IS的GR能力处于关闭状态。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

GR（Graceful Restart，平滑重启）是一种在协议重启或主备倒换时保证转发业务不中断的机制。需要协议重启或主备倒换的设备将重启状态通知给邻居，允许邻居重新建立邻接关系而不终止连接。

GR有两个角色：

·GR Restarter：发生协议重启或主备倒换事件且具有GR能力的设备。

·GR Helper：和GR Restarter具有邻居关系，协助完成GR流程的设备。

GR Restarter和GR Helper上都需要使能VXLAN IS-IS的GR能力。

【举例】

\# 使能VXLAN IS-IS的GR能力。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis graceful-restart

【相关命令】

·**display vxlan isis graceful-restart status**

**VXLAN \-- VXLAN IS-IS配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

**[graceful-restart interval**]命令用来配置VXLAN IS-IS协议的GR重启间隔时间。

**[undo graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[graceful-restart interval** *interval-value*]

**[undo graceful-restart interval**]

【缺省情况】

VXLAN IS-IS协议的GR重启间隔时间为300秒。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：VXLAN IS-IS协议的GR重启间隔时间，取值范围为30～1800，单位为秒。

【使用指导】

本命令配置的GR重启间隔时间作为T2定时器的值，用来控制LSDB同步时间。如果在GR重启间隔时间内没有完成LSDB同步，则GR失败，退出GR过程。

【举例】

\# 配置VXLAN IS-IS的GR重启间隔时间为120秒。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis graceful-restart interval 120

【相关命令】

·**display vxlan isis graceful-restart status**

**VXLAN \-- VXLAN IS-IS配置命令 \-- log-peer-change enable**

------------------------------------------------------------------------

**[log-peer-change enable**]命令用来打开邻接状态变化的输出开关。

**[undo log-peer-change enable**]命令用来关闭邻接状态变化的输出开关。

【命令】

**[log-peer-change enable**]

**[undo log-peer-change enable**]

【缺省情况】

邻接状态变化的输出开关处于打开状态。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

打开邻接状态变化的输出开关后，VXLAN IS-IS邻接状态变化时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。

【举例】

\# 打开邻接状态变化的输出开关。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis log-peer-change enable

**VXLAN \-- VXLAN IS-IS配置命令 \-- mac-synchronization enable**

------------------------------------------------------------------------

**[mac-synchronization enable**]命令用来开启VXLAN IS-IS的MAC地址同步功能。

**[undo mac-synchronization enable**]命令用来恢复缺省情况。

【命令】

**[mac-synchronization enable**]

**[undo mac-synchronization enable**]

【缺省情况】

VXLAN IS-IS不会在VTEP之间同步MAC地址信息。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admim

【使用指导】

开启本功能后，VTEP可以通过VXLAN IS-IS协议发布本地的MAC地址信息，并能够接收其他VTEP发布的远端MAC地址信息。

【举例】

\# 开启VXLAN IS-IS的MAC地址同步功能。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis mac-synchronization enable

**VXLAN \-- VXLAN IS-IS配置命令 \-- negotiate-vni enable**

------------------------------------------------------------------------

**[negotiate-vni enable**]命令用来开启VXLAN IS-IS的VXLAN自动协商功能。

**[undo negotiate-vni enable**]命令用来恢复缺省情况。

【命令】

**[negotiate-vni enable**]

**[undo negotiate-vni enable**]

【缺省情况】

VXLAN IS-IS不会在VTEP之间交互VXLAN ID。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admim

【使用指导】

本功能用来实现VXLAN隧道与VXLAN的自动关联。

开启本功能后，VTEP在所有VXLAN隧道上通过VXLAN IS-IS将本地存在的VXLAN的ID通告给远端VTEP。远端VTEP将其与本地的VXLAN进行比较，如果存在相同的VXLAN，则将该VXLAN与接收该信息的VXLAN隧道关联。

【举例】

\# 开启VXLAN IS-IS的VXLAN隧道自动协商功能。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis negotiate-vni enable

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis ded-priority**

------------------------------------------------------------------------

**[overlay isis ded-priority**]命令用来配置Tunnel接口的DED（Designated Edge Device，指定边缘设备）优先级。

**[undo overlay isis ded-priority**]命令用来恢复缺省情况。

【命令】

**[overlay isis ded-priority** *value*]

**[undo overlay isis ded-priority**]

【缺省情况】

Tunnel接口的DED优先级为64。

【视图】

VXLAN模式Tunnel接口视图/NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：Tunnel接口的DED优先级，取值范围为0～127。

【使用指导】

每个VXLAN隧道两端的VTEP设备通过交互VXLAN IS-IS Hello报文选举出一个DED。选举出的DED周期性发布CSNP报文来进行LSDB同步。

DED优先级数值高的设备被选为DED；如果两台设备的DED优先级相同，则MAC地址较大的设备会被选中。

【举例】

\# 配置Tunnel接口101的DED优先级为2。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 overlay isis ded-priority 2

【相关命令】

·**display ****vxlan isis tunnel**

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer csnp**

------------------------------------------------------------------------

**[overlay isis timer csnp**]命令用来配置DED发送CSNP报文的时间间隔。

**[undo overlay isis timer csnp**]命令用来恢复缺省情况。

【命令】

**[overlay isis timer csnp** *seconds*]

**[undo overlay isis timer csnp**]

【缺省情况】

DED发送CSNP报文的时间间隔为10秒。

【视图】

VXLAN模式Tunnel接口视图/NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：DED发送CSNP报文的时间间隔，取值范围为1～600，单位为秒。

【使用指导】

DED使用CSNP报文来进行LSDB同步。因此，只有在被选举为DED的设备上进行该项配置才有效。

【举例】

\# 配置Tunnel接口101上CSNP报文的发送时间间隔为15秒。

\<Sysname\> system-view

Sysname interface  tunnel 101

Sysname-tunnel101 overlay isis timer csnp 15

【相关命令】

·**display ****vxlan isis tunnel**

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer hello**

------------------------------------------------------------------------

**[overlay isis timer hello**]命令用来配置VXLAN IS-IS Hello报文的发送时间间隔。

**[undo overlay isis timer hello**]命令用来恢复缺省情况。

【命令】

**[overlay isis timer hello** *seconds*]

**[undo overlay isis timer hello**]

【缺省情况】

VXLAN IS-IS Hello报文的发送时间间隔为10秒。

【视图】

VXLAN模式Tunnel接口视图/NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：VXLAN IS-IS Hello报文的发送时间间隔，取值范围为3～255，单位为秒。

【使用指导】

发送时间间隔越短，网络收敛越快，但也需要占用更多的系统资源。因此，需要根据实际情况合理配置VXLAN IS-IS Hello报文的发送时间间隔。

DED发送VXLAN IS-IS Hello报文的时间间隔是本命令设置的时间间隔的1/3。

【举例】

\# 配置Tunnel接口101上VXLAN IS-IS Hello报文的发送时间间隔为6秒。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 overlay isis timer hello 6

【相关命令】

·**display ****vxlan isis tunnel**

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer holding-multiplier**

------------------------------------------------------------------------

**[overlay isis timer holding-multiplier**]命令用来配置VXLAN IS-IS Hello报文失效数目。

**[undo overlay isis timer holding-multiplier**]命令用来恢复缺省情况。

【命令】

**[overlay isis timer holding-multiplier** *value*]

**[undo overlay isis timer holding-multiplier**]

【缺省情况】

VXLAN IS-IS Hello报文失效数目为3。

【视图】

VXLAN模式Tunnel接口视图/NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：VXLAN IS-IS Hello报文失效数目，取值范围为3～1000。

【使用指导】

当前VTEP可以将邻接关系保持时间（即VXLAN IS-IS Hello报文失效数目与VXLAN IS-IS Hello报文发送时间间隔的乘积）通过VXLAN IS-IS Hello报文通知远端VTEP。如果远端VTEP在邻接关系保持时间内没有收到来自当前VTEP的VXLAN IS-IS Hello报文，将宣告邻接关系失效。通过设置VXLAN IS-IS Hello报文失效数目和VXLAN IS-IS Hello报文的发送时间间隔，可以调整邻接关系保持时间。

需要注意的是，邻接关系保持时间最大不能超过65535秒，超过65535秒时，算作65535秒。

【举例】

\# 配置Tunnel接口101上VXLAN IS-IS Hello报文失效数目为6。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 overlay isis timer holding-multiplier 6

【相关命令】

·**overlay isis timer hello**

**VXLAN \-- VXLAN IS-IS配置命令 \-- overlay isis timer lsp**

------------------------------------------------------------------------

**[overlay isis timer lsp**]命令用来配置VXLAN IS-IS在接口上发送LSP的最小时间间隔以及一次可以最多发送的LSP的数目。

**[undo overlay isis timer lsp**]命令用来恢复缺省情况。

【命令】

**[overlay isis timer lsp***time * **count** *count* ]

**[undo overlay isis timer lsp**]

【缺省情况】

发送LSP的最小时间间隔为100毫秒，一次最多可以发送的LSP数目为5。

【视图】

VXLAN模式Tunnel接口视图/NVE模式Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：发送LSP的最小时间间隔，取值范围为100～1000，为100的整数倍，单位为毫秒。

**[count***count*]：一次最多可以发送的LSP数目，取值范围为1～1000，缺省值为5。

【使用指导】

当LSDB的内容发生变化时，VXLAN IS-IS将把发生变化的LSP扩散出去。用户可以通过本命令对LSP的最小发送时间间隔进行调节。

【举例】

\# 配置发送LSP的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 overlay isis timer lsp 500

【相关命令】

·**display ****vxlan isis brief**

**VXLAN \-- VXLAN IS-IS配置命令 \-- reserved vxlan**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reserved vxlan**]命令用来配置IS-IS协议使用的保留VXLAN。

**[undo reserved vxlan**]命令用来恢复缺省情况。

【命令】

**[reserved vxlan** *vxlan-id*]

**[undo reserved vxlan**]

【缺省情况】

没有指定IS-IS协议使用的保留VXLAN。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vxlan-id*]：保留VXLAN的ID，取值范围为0～16777215。

【使用指导】

保留VXLAN用来接收和发送VXLAN IS-IS报文。属于同一个VXLAN的VTEP上只有配置了相同的保留VXLAN，VTEP之间才能够正常收发VXLAN IS-IS报文。

只能在系统视图下配置一个全局保留VXLAN，该VXLAN不能与VSI下创建的VXLAN相同。

【举例】

\# 配置IS-IS协议使用的保留VXLAN为VXLAN 10000。

\<Sysname\> system

Sysname reserved vxlan 10000

**VXLAN \-- VXLAN IS-IS配置命令 \-- reset vxlan isis**

------------------------------------------------------------------------

**[reset vxlan isis**]命令用来清除VXLAN IS-IS进程下所有的动态数据，包括VXLAN IS-IS的邻居、本地MAC地址、远端MAC地址、VXLAN ID、链路状态数据库等信息。

【命令】

**[reset vxlan isis**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除VXLAN IS-IS进程下所有的动态数据。

\<Sysname\> reset vxlan isis

**VXLAN \-- VXLAN IS-IS配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

**[timer lsp-max-age**]命令用来配置当前VTEP生成的LSP在LSDB里的最大生存时间。

**[undo timer lsp-max-age**]命令用来恢复缺省情况。

【命令】

**[timer lsp-max-age ***second*s]

**[undo timer lsp-max-age**]

【缺省情况】

当前VTEP生成的LSP在LSDB里的最大生存时间为1200秒。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：LSP在LSDB里的最大生存时间，取值范围是3～65535，单位为秒。

【使用指导】

每个LSP都有一个最大生存时间，随着时间的推移LSP的生存时间将逐渐减小，当LSP的生存时间为0时，VXLAN IS-IS将清除该LSP。用户可根据网络的实际情况调整LSP的最大生存时间。

【举例】

\# 配置生成的LSP的最大生存时间为25分钟，即1500秒。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis timer lsp-max-age 1500

【相关命令】

·**display vxlan isis brief**

**VXLAN \-- VXLAN IS-IS配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

**[timer lsp-refresh**]命令用来配置LSP刷新周期。

**[undo timer lsp-refresh**]命令用来恢复缺省情况。

【命令】

**[timer lsp-refresh ***second*s]

**[undo timer lsp-refresh**]

【缺省情况】

LSP刷新周期为900秒。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[second*s]：LSP刷新周期，取值范围为1～65534，单位为秒。

【使用指导】

**[timer lsp-refresh**]命令配置的时间必须小于**timer lsp-max-age**命令配置的时间，以保证在LSP失效前进行刷新。

【举例】

\# 配置LSP刷新周期为1500秒。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis timer lsp-refresh 1500

【相关命令】

·**display vxlan isis brief**

·**timer lsp-max-age**

**VXLAN \-- VXLAN IS-IS配置命令 \-- virtual-system**

------------------------------------------------------------------------

**[virtual-system**]命令用来创建一个VXLAN IS-IS虚拟系统。

**[undo virtual-system**]命令用来删除一个已经存在的VXLAN IS-IS虚拟系统。

【命令】

**[virtual-system** *system-id*]

**[undo virtual-system ***system-id*]

【缺省情况】

不存在任何VXLAN IS-IS虚拟系统。

【视图】

VXLAN IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[system-id*]：虚拟系统的系统ID，用来标识虚拟系统，格式为XXXX.XXXX.XXXX，X表示十六进制数字。

【使用指导】

当本地MAC地址数超过系统的LSP分片集所能携带的MAC地址数时，可以配置VXLAN IS-IS虚拟系统来扩展LSP的分片数量，以增加系统所能发布的MAC地址数量。

创建虚拟系统前，系统最多可以发送约55×2^10^的MAC地址信息，每创建一个虚拟系统，最多可以多发送55×2^10^的MAC地址信息。用户可以根据本地MAC地址表的规模，来决定创建的虚拟系统的个数。

创建虚拟系统时，用户需要保证所配置的虚拟系统的系统ID在网络中是唯一的。

【举例】

\# 创建一个系统ID为0001.0001.0001的虚拟系统。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis virtual-system 0001.0001.0001

【相关命令】

·**display vxlan isis brief**

**VXLAN \-- VXLAN IS-IS配置命令 \-- vxlan-isis**

------------------------------------------------------------------------

**[vxlan-isis**]命令用来创建VXLAN IS-IS进程，并进入VXLAN IS-IS视图。

**[undo vxlan-isis**]命令用来删除VXLAN IS-IS进程，并清除VXLAN IS-IS进程下的配置数据。

【命令】

**[vxlan-isis**]

**[undo vxlan-isis**]

【缺省情况】

未创建VXLAN IS-IS进程。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admim

【举例】

\# 创建VXLAN IS-IS进程，并进入VXLAN IS-IS视图。

\<Sysname\> system-view

Sysname vxlan-isis

Sysname-vxlan-isis

【相关命令】

·**display ****vxlan isis brief**

**VXLAN \-- VXLAN IP网关配置命令 \-- bandwidth**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的最大速率÷1000（kbit/s）。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：接口的期望带宽，取值范围为1～400000000，单位为kbps。

【使用指导】

接口的期望带宽会对下列内容有影响：

·CBQ队列带宽。具体介绍请参见"ACL和QoS配置指导"中的"[拥塞管理"。]

·链路开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置接口VSI-interface100的期望带宽为10000kbps。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 bandwidth 10000

**VXLAN \-- VXLAN IP网关配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将接口VSI-interface100恢复为缺省配置。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 default

This command will restore the default settings. Continue? [Y/N:y]

**VXLAN \-- VXLAN IP网关配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，例如：Vsi-interface100 Interface。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述字符串，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。

本命令仅用于标识某接口，并无特别的功能。使用**display interface**等命令可以看到设置的描述信息。

【举例】

\# 配置接口VSI-interface100的描述信息为"gateway for VXLAN 10"。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 description gateway for VXLAN 10

**VXLAN \-- VXLAN IP网关配置命令 \-- display interface vsi-interface**

------------------------------------------------------------------------

**[display interface **]**vsi-interface**命令用来显示VSI虚接口的相关信息。

【命令】

**[display interface** **vsi-interface** [ *vsi-interface-id*    **brief** [ **description** \| **down** ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsi-nterface-id*]：VSI虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[brief**]：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定接口类型（**vsi-interface**），将显示设备支持的所有接口的相关信息。

·如果指定接口类型，不指定接口编号（*vsi-interface-id*），则显示所有VSI虚接口的信息。

·如果同时指定接口类型和接口编号，则显示指定VSI虚接口的信息。

【举例】

\# 显示接口VSI-interface100的相关信息。

\<Sysname\> display interface vsi-interface 100

Vsi-interface100

Current state: UP

Line protocol state: UP

Description: Vsi-interface100 Interface

Bandwidth: 1000000kbps

Maximum Transmit Unit: 1500

Internet Address is 10.1.1.1/24 Primary

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102

Physical: Unknown, baudrate: 1000000 kbps

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

表1-22 display interface vsi-interface命令显示信息描述表

字段

描述

Vsi-interface100

接口VSI-interface100的相关信息

Current state

接口的物理状态和管理状态，取值包括：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：

·UP：表示该接口的链路层协议状态为开启

·UP (spoofing)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示该接口的链路层协议状态为关闭

Description

接口的描述信息

Bandwidth

接口的期望带宽，单位为kbps

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing

Tunnel接口的IP地址。如果没有为Tunnel接口配置IP地址，则该字段显示为Internet protocol processing: disabled，表示不能处理IP报文

Primary表示该IP地址为接口的主IP地址

IP Packet Frame Type，Hardware Address

IP报文发送帧格式，硬件地址

IPv6 Packet Frame Type，Hardware Address

IPv6报文发送帧格式，硬件地址

Physical

接口的物理类型，取值为Unknown

baudrate

接口的波特率，单位为kbps

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间（如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never）

Last 300 seconds input rate

最近300秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，bits/sec表示平均每秒输入的比特数，packets/sec表示平均每秒输入的包数

Last 300 seconds output rate

最近300秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数，bits/sec表示平均每秒输出的比特数，packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 drops

总计输入的报文数, 总计输入的字节，总计丢弃的输入报文数

Output: 0 packets, 0 bytes, 0 drops

总计输出的报文数, 总计输出的字节，总计丢弃的输出报文数

\# 显示所有VSI虚接口的概要信息。

\<Sysname\> display interface vsi-interface brief

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Vsi100               DOWN DOWN     \--

\# 显示接口VSI-interface100的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display interface vsi-interface 100 brief description

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Vsi100               UP    UP      1.1.1.1         VSI-interface100

\# 显示当前状态为down的接口的信息以及DOWN的原因。

\<Sysname\> display interface brief down

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Vsi100               DOWN Administratively

Vsi200               DOWN Administratively

表1-23 display interface vsi-interface brief命令显示信息描述表

字段

描述

Brief information of interface(s) under route mode:

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的网络层协议状态显示是UP的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立

Interface

接口名称缩写

Link

接口物理连接状态，取值包括：

·UP：表示本链路物理上是连通的

·DOWN：表示本链路物理上是不通的

·ADM：表示本链路被手工关闭了，需要执行**undo shutdown**命令才能恢复真实的物理状态

·Stby：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准

Protocol

接口的链路层协议状态。其值由链路层经过参数协商决定，取值包括：

·UP：表示该接口的链路层协议状态为开启

·UP (s)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示该接口的链路层协议状态为关闭

Main IP

接口主IP地址

Description

接口的描述信息

Cause

接口物理连接状态为down的原因，取值为：

·Administratively：表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

·Not connected：表示没有VSI关联该接口，或者关联该接口的VSI内没有AC或PW.

【相关命令】

·**reset counters interface**

**VXLAN \-- VXLAN IP网关配置命令 \-- distributed-gateway local**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[distributed-gateway local**]命令用来配置VSI虚接口为分布式网关接口。

**[undo** **distributed-gateway local**]命令用来恢复缺省情况。

【命令】

**[distributed-gateway local**]

**[undo distributed-gateway local**]

【缺省情况】

VSI虚接口不是分布式本地网关接口。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在分布式VXLAN IP网关组网中，多个网关上的VSI虚接口需要配置相同的IP地址。为了避免IP地址冲突，需要在VSI虚接口上执行本命令，以防止VSI虚接口上报地址冲突，导致VSI虚接口不可用。

【举例】

\# 配置接口Vsi-interface100为分布式网关接口。

\<Sysname\> system

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 distributed-gateway local

**VXLAN \-- VXLAN IP网关配置命令 \-- gateway subnet**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[gateway subnet**]命令用来配置VSI所属的子网网段。

**[undo gateway subnet**]命令用来恢复缺省情况。

【命令】

**[gateway subnet **[{ *ip-address wildcard-mask* \| *ipv6-address prefix-length* } ]]

**[undo gateway subnet**[ { *ip-address wildcard-mask* \| *ipv6-address prefix-length* }]]

【缺省情况】

没有指定VSI所属的子网网段。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：子网网段地址，为点分十进制格式。

*[wildcard-mask*]：IP地址掩码的反码，即将IP地址的掩码取反（0变1，1变0）。例如：子网掩码255.0.0.0的反码为0.255.255.255。其中，反码中的"1"表示忽略IP地址中对应的位，"0"表示必须保留此位。

*[ipv6-address prefix-length*]：IPv6地址及前缀长度。*prefix-length*为IPv6前缀长度，取值范围为1～128。

【使用指导】

为了节省分布式VXLAN IP网关设备上的三层接口资源，在网关设备上多个VXLAN可以共用一个VSI虚接口，为VSI虚接口配置一个主IP地址和多个从IP地址（IPv4网络）、或多个IPv6地址（IPv6网络），分别作为不同VXLAN内虚拟机的网关地址。

多个VXLAN共用一个VSI虚接口时，网关设备无法判断从VSI虚接口接收到的报文属于哪个VXLAN。为了解决该问题，需要在VSI视图下通过本命令指定VSI所属的子网网段，通过子网网段判断报文所属的VSI，并在该VSI内转发报文，从而限制广播报文范围，有效地节省带宽资源。但是每个VXLAN都有各自的IP地址子网网段以及网关IP，因此需要VSI虚接口支持按VXLAN设置Subnet IP。

需要注意的是：

·一个VSI视图下最多可以配置8个子网网段，包括IPv4子网和IPv6子网。

·在VSI视图下配置子网网段前，必须先为该VSI指定网关接口。取消为VSI指定网关接口时，会自动删除为该VSI指定的子网网段。

·不能为指定了相同网关接口的不同VSI配置相同的子网网段。

【举例】

\# 配置名称为vxlan的VSI所属的子网网段为100.0.10.0/24。

\<Sysname\> system-view

Sysname vsi vxlan

Sysname-vsi-vxlan gateway subnet 100.0.10.0 0.0.0.255

**VXLAN \-- VXLAN IP网关配置命令 \-- gateway vsi-interface**

------------------------------------------------------------------------

**[gateway vsi-interface**]命令用来为VSI指定网关接口。

**[undo gateway vsi-interface**]命令用来恢复缺省情况。

【命令】

**[gateway vsi-interface ***vsi-interface-id*]

**[undo gateway vsi-interface**]

【缺省情况】

没有为VSI指定网关接口。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-interface-id*]：VSI网关虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·一个VSI只能指定一个网关接口。

·不同的VSI可以指定相同的网关接口。

【举例】

\# 为VSI指定网关接口为Vsi-interface100。

\<Sysname\> system

Sysname vsi vpna

Sysname-vsi-vpna gateway vsi-interface 100

【相关命令】

·**interface vsi-interface**

**VXLAN \-- VXLAN IP网关配置命令 \-- interface vsi-interface**

------------------------------------------------------------------------

**[interface vsi-interface**]命令用来创建VSI虚接口，并进入VSI虚接口视图。

**[undo interface vsi-interface**]命令用来删除VSI虚接口。

【命令】

**[interface vsi-interface ***vsi-interface-id*]

**[undo interface vsi-interface ***vsi-interface-id*]

【缺省情况】

设备上不存在任何VSI虚接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-nterface-id*]：VSI虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 创建VSI虚接口100，并进入VSI虚接口视图。

\<Sysname\> system

Sysname interface vsi-interface 100

Sysname-Vsi-interface100

【相关命令】

·**gateway vsi-interface**

**VXLAN \-- VXLAN IP网关配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，取值范围为46～1560，单位为字节。

【举例】

\# 配置接口VSI-interface100的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 mtu 1430

**VXLAN \-- VXLAN IP网关配置命令 \-- reset counters interface vsi-interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除接口的统计信息。

【命令】

**[reset counters interface** **vsi-interface** [ *vsi-interface-id*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-nterface-id*]：VSI虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定接口类型（**vsi-interface**），则清除所有接口的统计信息；

·如果指定接口类型，不指定接口编号（*vsi-interface-id*），则清除所有VSI虚接口的统计信息；

·如果同时指定接口类型和接口编号，则清除指定VSI虚接口的统计信息。

【举例】

\# 清除接口VSI-interface100的统计信息。

\<Sysname\> reset counters interface vsi-interface 100

【相关命令】

·**display interface**

**VXLAN \-- VXLAN IP网关配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo** **shutdown**]命令用来开启当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

VSI虚接口均处于开启状态。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭接口VSI-interface100。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 shutdown

**VXLAN \-- VXLAN IP网关配置命令 \-- vxlan ip-forwarding**

------------------------------------------------------------------------

![说明](VXLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vxlan ip-forwarding**]命令用来配置VXLAN采用三层转发模式。

**[undo vxlan ip-forwarding**]命令用来配置VXLAN采用二层转发模式。

【命令】

**[vxlan ip-forwarding**]

**[undo vxlan ip-forwarding**]

【缺省情况】

VXLAN采用三层转发模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

三层转发模式是指VTEP设备通过查找ARP表项（IPv4网络）或ND表项（IPv6网络）对流量进行转发。二层转发模式是指VTEP通过查找MAC地址表项对流量进行转发。

采用分布式VXLAN IP网关组网方案时，VXLAN需要采用三层转发模式；其他情况下，VXLAN采用二层转发模式。

需要注意的是，修改本配置前，必须先删除设备上的所有VSI、VSI虚接口和VXLAN隧道，否则配置将失败。

【举例】

\# 配置VXLAN采用三层转发模式。

\<Sysname\> system-view

Sysname vxlan ip-forwarding
