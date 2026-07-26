
**QinQ \-- QinQ配置命令 \-- display qinq**

------------------------------------------------------------------------

**[display qinq**]命令用来显示使能了QinQ功能的端口。

【命令】

**[display qinq** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定端口是否使能了QinQ功能。*interface-type interface-number*为端口类型和端口编号；如果未指定该参数，则显示所有使能QinQ功能的端口。

【使用指导】

如果端口都没有使能QinQ功能，则执行该命令后无显示内容。

【举例】

\# 在端口GigabitEthernet1/0/1上使能QinQ功能，然后显示该端口是否使能了QinQ功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qinq enable

Sysname-GigabitEthernet1/0/1 display qinq interface gigabitethernet 1/0/1

Interface

 GigabitEthernet1/0/1

\# 在端口GigabitEthernet1/0/1和GigabitEthernet1/0/3上使能QinQ功能，然后显示所有使能了QinQ功能的端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qinq enable

Sysname-GigabitEthernet1/0/1 quit

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 qinq enable

Sysname-GigabitEthernet1/0/3 display qinq

Interface

 GigabitEthernet1/0/1

 GigabitEthernet1/0/3

表1-1 display qinq命令显示信息描述表

字段

描述

Interface

接口名称

GigabitEthernet1/0/1

使能了QinQ功能的端口

【相关命令】

·**qinq enable**

**QinQ \-- QinQ配置命令 \-- qinq enable**

------------------------------------------------------------------------

**[qinq enable**]命令用来使能端口的QinQ功能。

**[undo qinq enable**]命令用来恢复缺省情况。

【命令】

**[qinq enable**]

**[undo qinq enable**]

【缺省情况】

端口的QinQ功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在端口GigabitEthernet1/0/1上使能QinQ功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qinq enable

【相关命令】

·**display qinq**

**QinQ \-- QinQ配置命令 \-- qinq ethernet-type**

------------------------------------------------------------------------

![说明](QinQ命令.files/image001.png)

本命令的视图支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[qinq ethernet-type**]命令用来配置内层或外层VLAN Tag的TPID值。

**[undo qinq ethernet-type**]命令用来恢复内层或外层VLAN Tag的TPID值为缺省值。

【命令】

**[qinq ethernet-type**[ { **customer-tag** \| **service-tag** } *hex-value*]]

**[undo qinq ethernet-type **[{ **customer-tag** \| **service-tag** }]]

【缺省情况】

内、外层VLAN Tag的TPID值的全局配置都为0x8100，端口配置等于全局配置（若支持全局配置）或都为0x8100（若不支持全局配置）。

【视图】

系统视图/二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[customer-tag**]：表示配置内层VLAN Tag的TPID值。本参数及视图的支持情况与设备的型号有关，请以设备的实际情况为准。

**[service-tag**]：表示配置外层VLAN Tag的TPID值。本参数及视图的支持情况与设备的型号有关，请以设备的实际情况为准。

*[hex-value*]：表示十六进制格式的协议类型值，取值范围为0x0001～0xFFFF，但不允许配置为[表]1-2(?-1936232445#_Ref154730745)中列举的常用协议类型值。

表1-2 常用协议类型值

协议类型

协议类型值

ARP

0x0806

PUP

0x0200

RARP

0x8035

IP

0x0800

IPv6

0x86DD

PPPoE

0x8863/0x8864

MPLS

0x8847/0x8848

IPX/SPX

0x8137

IS-IS

0x8000

LACP

0x8809

LLDP

0x88CC

802.1X

0x888E

802.1ag

0x8902

集群

0x88A7

设备保留

0xFFFD/0xFFFE/0xFFFF

【使用指导】

对于某个端口来说，优先采用端口上的配置，最后才采用全局配置。

【举例】

\# 全局配置内层VLAN Tag的TPID值为0x8200。

\<Sysname\> system-view

Sysname qinq ethernet-type customer-tag 8200

\# 全局配置外层VLAN Tag的TPID值为0x8200。

\<Sysname\> system-view

Sysname qinq ethernet-type service-tag 8200

\# 在端口GigabitEthernet1/0/1上配置内层VLAN Tag的TPID值为0x9100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qinq ethernet-type customer-tag 9100

\# 在端口GigabitEthernet1/0/1上配置外层VLAN Tag的TPID值为0x9100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qinq ethernet-type service-tag 9100

**QinQ \-- QinQ配置命令 \-- qinq transparent-vlan**

------------------------------------------------------------------------

**[qinq transparent-vlan**]命令用来配置端口的VLAN透传功能，使端口对指定VLAN的报文进行透传。

**[undo** **qinq transparent-vlan**]命令用来取消端口对指定VLAN的报文进行透传的配置。

【命令】

**[qinq transparent-vlan ***vlan-id-list*]

**[undo qinq transparent-vlan**[ { *vlan-id-list* \| **all** }]]

【缺省情况】

端口没有配置VLAN透传功能。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，表示一个或多个VLAN，且这些VLAN必须是本地已创建好的。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中，*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094，*vlan-id2*的值要大于或等于*vlan-id1*的值。&\<1-10\>表示前面的参数最多可以输入10次。

**[all**]：表示所有已创建的VLAN。

【举例】

\# 在端口GigabitEthernet1/0/1上使能QinQ功能，配置端口为Trunk类型，允许VLAN 2、3、50～100的报文通过，并对VLAN 2的报文进行透传。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type trunk

Sysname-GigabitEthernet1/0/1 port trunk permit vlan 2 3 50 to 100

Sysname-GigabitEthernet1/0/1 qinq enable

Sysname-GigabitEthernet1/0/1 qinq transparent-vlan 2

