<!-- CMD-INDEX
  dot1q ethernet-type                 | 三层以太网接口视图/三层聚合接口视图/三层虚拟以太网接口视图/L3VE接口视图/VLAN接口视图 | L11
  second-dot1q                        | 三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图/VLAN接口视图 | L137
  vlan-termination broadcast enable   | 三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图/VLAN接口视图 | L321
  vlan-type dot1q default             | 三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图 | L411
  vlan-type dot1q untagged            | 三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图 | L461
  vlan-type dot1q vid                 | 三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图 | L511
  vlan-type dot1q vid second-dot1q    | 三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图 | L609
-->

**VLAN终结 \-- VLAN终结配置命令 \-- dot1q ethernet-type**

------------------------------------------------------------------------

![说明](VLAN终结命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[dot1q ethernet-type**]命令用来配置当前接口接收和发送的报文最外层VLAN Tag的TPID值。

**[undo dot1q ethernet-type**]命令用来恢复缺省情况。

【命令】

**[dot1q ethernet-type** *hex-value*]

**[undo dot1q ethernet-type**]

【缺省情况】

当前接口接收或发送的报文最外层VLAN Tag的TPID值为0x8100。

【视图】

三层以太网接口视图/三层聚合接口视图/三层虚拟以太网接口视图/L3VE接口视图/VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hex-value*]：指定VLAN报文中的TPID（Tag Protocol Identifier，标签协议标识符）值，为4个字符长度的十六进制数字，取值范围为0x1～0xFFFF，但不允许配置为[表]1-1(?1352125841#_Ref154730745)中列举的常用协议类型值。

表1-1 常用协议类型值

协议

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

配置**dot1q ethernet-type**命令后，当接收报文时，只有报文最外层VLAN Tag的TPID值为0x8100或者指定值的报文才会作为VLAN报文来处理；发送报文时，会给报文最外层VLAN Tag的TPID值填入指定值，如果报文带有两层及以上VLAN Tag，则给报文其他层VLAN Tag的TPID值都填入0x8100。

需要注意的是：

·该命令只能在三层以太网主接口、三层聚合主接口、三层虚拟以太网主接口、L3VE主接口和VLAN接口下配置，不能在子接口上配置。

·在三层以太网接口、三层聚合接口、三层虚拟以太网接口或L3VE视图下配置，会对相应接口的所有子接口生效；在VLAN接口视图下配置，会对该VLAN接口生效。

【举例】

\# 设置接口GigabitEthernet1/0/1下所有子接口能够接收和发送外层TPID值为0x9100的VLAN报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dot1q ethernet-type 9100

**VLAN终结 \-- VLAN终结配置命令 \-- second-dot1q**

------------------------------------------------------------------------

![说明](VLAN终结命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[second-dot1q**]命令用来使能当前接口的QinQ终结功能，并指定当前接口可以终结的VLAN报文的第二层VLAN ID（第一层VLAN ID等于当前接口的编号，不能配置）。

**[undo second-dot1q**]用来恢复缺省情况。

【命令】

**[second-dot1q **[{ *vlan-id-list* \| **any** } [ **loose** ]]]

**[undo second-dot1q**[ { *vlan-id-list* \| **any** } [ **loose** ]]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图/VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：当前接口能够终结的VLAN报文的第二层VLAN ID范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中，*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

**[any**]：表示当前接口可以终结第一层VLAN ID为接口编号，第二层VLAN ID为1～4094中任意值的VLAN报文。

**[loose**]：表示当前接口支持接收并终结携带两层或两层以上VLAN Tag的报文。

【举例】

\# 配置子接口GigabitEthernet1/0/1.10能够终结的VLAN报文的第二层VLAN ID范围为10～20；配置子接口GigabitEthernet1/0/1.12能够终结的VLAN报文的第二层VLAN ID为100；配置子接口GigabitEthernet1/0/1.100能够终结的VLAN报文的第二层VLAN ID为1～4094中任意值。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.10

Sysname-GigabitEthernet1/0/1.10 second-dot1q 10 to 20

Sysname-GigabitEthernet1/0/1.10 quit

Sysname interface gigabitethernet 1/0/1.12

Sysname-GigabitEthernet1/0/1.12 second-dot1q 100

Sysname-GigabitEthernet1/0/1.12 quit

Sysname interface gigabitethernet 1/0/1.100

Sysname-GigabitEthernet1/0/1.100 second-dot1q any

通过以上配置，子接口GigabitEthernet1/0/1.10、GigabitEthernet1/0/1.12和GigabitEthernet1/0/1.100能够终结的VLAN报文规格如下：

子接口

允许终结的VLAN报文的第一层VLAN ID

允许终结的VLAN报文的第二层VLAN ID

GigabitEthernet1/0/1.10

10

10～20

GigabitEthernet1/0/1.12

12

100

GigabitEthernet1/0/1.100

100

1～4094

\# 配置Vlan-interface10能够终结的VLAN报文的第二层VLAN ID范围为10～20；配置Vlan-interface12能够终结的VLAN报文的第二层VLAN ID为100；配置Vlan-interface100能够终结的VLAN报文的第二层VLAN ID为1～4094中任意值。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 second-dot1q 10 to 20

Sysname-Vlan-interface10 quit

Sysname interface vlan-interface 12

Sysname-Vlan-interface12 second-dot1q 100

Sysname-Vlan-interface12 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 second-dot1q any

通过以上配置，Vlan-interface10、Vlan-interface12和Vlan-interface100能够终结的VLAN报文规格如下：

接口

允许终结的VLAN报文的第一层VLAN ID

允许终结的VLAN报文的第二层VLAN ID

Vlan-interface10

10

10～20

Vlan-interface12

12

100

Vlan-interface100

100

1～4094

\# 配置Virtual-Ethernet1.10能够终结的VLAN报文的第二层VLAN ID范围为10～20；配置Virtual-Ethernet1.20能够终结的VLAN报文的第二层VLAN ID为100；配置Virtual-Ethernet1.100能够终结的VLAN报文的第二层VLAN ID为1～4094中任意值。

\<Sysname\> system-view

Sysname interface virtual-ethernet 1.10

Sysname-Virtual-Ethernet1.10 second-dot1q 10 to 20

Sysname-Virtual-Ethernet1.10 quit

Sysname interface virtual-ethernet 1.20

Sysname-Virtual-Ethernet1.20 second-dot1q 100

Sysname-Virtual-Ethernet1.20 quit

Sysname interface virtual-ethernet 1.100

Sysname-Virtual-Ethernet1.100 second-dot1q any

通过以上配置，Virtual-Ethernet1.10、Virtual-Ethernet1.20和Virtual-Ethernet1.100能够终结的VLAN报文规格如下：

子接口

允许终结的VLAN报文的第一层VLAN ID

允许终结的VLAN报文的第二层VLAN ID

Virtual-Ethernet 1.10

10

10～20

Virtual-Ethernet 1.20

20

100

Virtual-Ethernet 1.100

100

1～4094

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-termination broadcast enable**

------------------------------------------------------------------------

 ![说明](VLAN终结命令.files/image001.png)

·本特性的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[vlan-termination broadcast enable**]命令用来配置允许当前接口发送广播和组播报文，即允许当前接口遍历模糊终结的范围发送报文，具体为当前接口遍历模糊终结范围内的VLAN ID，给报文分别添加这些VLAN ID对应的VLAN Tag后发送（比如，对于配置了模糊的QinQ终结的接口，报文添加VLAN Tag后，最外两层VLAN ID分别对应各自模糊终结范围内的VLAN ID）。

**[undo vlan-termination broadcast enable**]命令用来恢复缺省情况。

【命令】

**[vlan-termination broadcast enable**]

**[undo vlan-termination broadcast enable**]

【缺省情况】

当前接口配置了模糊的Dot1q终结或者模糊的QinQ终结功能后，不允许发送广播、组播报文。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图/VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在接口配置了模糊终结功能时，建议用户同时配置该命令，以允许接口遍历模糊终结的范围发送报文。如果出于系统性能考虑，不允许接口遍历模糊终结的范围发送报文，则不要配置该命令。

【举例】

\# 配置允许子接口GigabitEthernet1/0/1.10遍历模糊Dot1q终结范围发送广播、组播报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.10

Sysname-GigabitEthernet1/0/1.10 vlan-type dot1q vid 10 to 20

Sysname-GigabitEthernet1/0/1.10 vlan-termination broadcast enable

通过以上配置，当子接口GigabitEthernet1/0/1.10发送广播、组播报文的时候，给报文封装VLAN Tag（遍历范围10～20）后发送。

\# 配置允许子接口GigabitEthernet1/0/1.10遍历模糊QinQ终结范围发送广播、组播报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.10

Sysname-GigabitEthernet1/0/1.10 vlan-type dot1q vid 300 to 400 second-dot1q 500 to 600

Sysname-GigabitEthernet1/0/1.10 vlan-termination broadcast enable

通过以上配置，当子接口GigabitEthernet1/0/1.10发送广播、组播报文的时候，给报文封装VLAN Tag（内层VLAN Tag遍历范围500～600，外层VLAN Tag遍历范围300～400）后发送。

\# 配置允许接口Vlan-interface 10遍历终结范围发送广播、组播报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 second-dot1q 10 to 20

Sysname-Vlan-interface10 vlan-termination broadcast enable

通过以上配置，当接口Vlan-interface 10发送广播、组播报文的时候，给报文封装两层VLAN Tag（内层VLAN Tag遍历范围10～20，外层VLAN Tag对应VLAN 10）后发送。

\# 配置允许子接口Virtual-Ethernet1.10遍历终结范围发送广播、组播报文。

\<Sysname\> system-view

Sysname interface virual-ethernet 1.10

Sysname-Virtual-Ethernet1.10 vlan-type dot1q vid 10 to 20

Sysname-Virtual-Ethernet1.10 vlan-termination broadcast enable

通过以上配置，当子接口Virtual-Ethernet1.10发送广播、组播报文的时候，给报文封装VLAN Tag（遍历范围10～20）后发送。

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q default**

------------------------------------------------------------------------

![说明](VLAN终结命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[vlan-type dot1q default**]命令用来使能当前接口的Default终结功能，使当前接口可以处理其他子接口都无法处理的报文。

**[undo vlan-type dot1q default**]命令用来恢复缺省情况。

【命令】

**[vlan-type dot1q default**]

**[undo vlan-type dot1q default**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置子接口GigabitEthernet1/0/1.1的Default终结功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q default

Sysname-GigabitEthernet1/0/1.1 quit

通过以上配置，子接口GigabitEthernet1/0/1.1能够处理其他子接口都无法处理的报文。

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q untagged**

------------------------------------------------------------------------

![说明](VLAN终结命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[vlan-type dot1q untagged**]命令用来使能当前接口的Untagged终结功能，使当前接口可以处理不带VLAN Tag的报文。

**[undo vlan-type dot1q untagged**]命令用来恢复缺省情况。

【命令】

**[vlan-type dot1q untagged**]

**[undo vlan-type dot1q untagged**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置子接口GigabitEthernet1/0/1.1的Untagged终结功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q untagged

Sysname-GigabitEthernet1/0/1.1 quit

通过以上配置，子接口GigabitEthernet1/0/1.1能够接收不带VLAN Tag的报文。

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q vid**

------------------------------------------------------------------------

![说明](VLAN终结命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[vlan-type dot1q vid**]命令用来使能当前接口的Dot1q终结功能，并指定当前接口能够终结的VLAN报文的最外层VLAN ID范围。

**[undo vlan-type dot1q vid**]命令用来取消当前接口的Dot1q终结功能。

【命令】

**[vlan-type dot1q vid ***vlan-id-list * **loose** ]

**[undo vlan-type dot1q vid ***vlan-id-list * **loose** ]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：当前接口能够终结的VLAN报文的最外层VLAN ID范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中，*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

**[loose**]：表示当前接口支持接收携带一层或一层以上VLAN Tag的报文。本参数的支持情况与设备型号有关，请以设备的实际型号为准。

【使用指导】

同一以太网主接口下的不同子接口不能终结同一种VLAN报文，即同一主接口下各子接口指定的*vlan-id-list*不能存在交集。

【举例】

\# 配置子接口GigabitEthernet1/0/1.1能够终结最外层VLAN ID在范围2～100内的VLAN报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 2 to 100

通过以上配置，当子接口GigabitEthernet1/0/1.1收到的报文的最外层VLAN ID在范围2～100内时，就会对该报文进行终结处理。

\# 配置子接口Virtual-Ethernet1.1能够终结最外层VLAN ID在范围2～100内的VLAN报文。

\<Sysname\> system-view

Sysname interface virtual-ethernet 1.1

Sysname-Virtual-Ethernet1.1 vlan-type dot1q vid 2 to 100

通过以上配置，当子接口Virtual-Ethernet1.1收到的报文的最外层VLAN ID在范围2～100内时，就会对该报文进行终结处理。

\# 配置子接口GigabitEthernet1/0/1.1能够终结最外层VLAN ID为2的带有一层或一层以上VLAN Tag的VLAN报文。配置子接口GigabitEthernet1/0/1.2能够终结最外层VLAN ID为3的VLAN报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 2 loose

Sysname interface gigabitethernet 1/0/1.2

Sysname-GigabitEthernet1/0/1.2 vlan-type dot1q vid 3

子接口

允许终结的最外层VLAN ID

是否允许终结携带一层以上VLAN Tag的报文

GigabitEthernet1/0/1.1

2

是

GigabitEthernet1/0/1.2

3

否

**VLAN终结 \-- VLAN终结配置命令 \-- vlan-type dot1q vid second-dot1q**

------------------------------------------------------------------------

![说明](VLAN终结命令.files/image001.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[vlan-type dot1q vid second-dot1q**]命令用来使能子接口的QinQ终结功能，并指定当前接口可以终结的VLAN报文的最外两层VLAN ID。

**[undo vlan-type dot1q vid second-dot1q**]命令用来恢复缺省情况。

【命令】

**[vlan-type dot1q vid**[ *vlan-id-list* **second-dot1q** { *vlan-id-list* \| **any** } [ **loose** ]]]

**[undo vlan-type dot1q vid ***vlan-id-list*[ **second-dot1q** { *vlan-id-list* \| **any** } [ **loose** ]]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层虚拟以太网子接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN ID范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中，*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

**[any**]：表示当前接口可以终结第一层VLAN ID为指定值，第二层VLAN ID为1～4094中任意值的VLAN报文。

**[loose**]：表示当前接口支持接收携带两层或两层以上VLAN Tag的报文。

【使用指导】

同一以太网主接口下的不同子接口不能终结同一种VLAN报文，如果为两个子接口配置了相同的第一层VLAN ID，则第二层VLAN ID范围不能有交叉。需要注意的是，如果这两个子接口的第二层VLAN ID各配置为*vlan-id-list1*和**any**，**any**表示1～4094范围内除*vlan-id-list1*的其他任意VLAN ID。

【举例】

\# 使能三层以太网子接口的QinQ终结功能，并指定子接口可以终结的VLAN报文的最外两层VLAN ID。

·配置子接口GigabitEthernet1/0/1.1能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 100 second-dot1q 100

Sysname-GigabitEthernet1/0/1.1 quit

·配置子接口GigabitEthernet1/0/1.2能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID范围为200～300。

Sysname interface gigabitethernet 1/0/1.2

Sysname-GigabitEthernet1/0/1.2 vlan-type dot1q vid 100 second-dot1q 200 to 300

Sysname-GigabitEthernet1/0/1.2 quit

·配置子接口GigabitEthernet1/0/1.3能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID为any。

Sysname interface gigabitethernet 1/0/1.3

Sysname-GigabitEthernet1/0/1.3 vlan-type dot1q vid 100 second-dot1q any

Sysname-GigabitEthernet1/0/1.3 quit

·配置子接口GigabitEthernet1/0/1.4能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID范围为500～600。

Sysname interface gigabitethernet 1/0/1.4

Sysname-GigabitEthernet1/0/1.4 vlan-type dot1q vid 100 second-dot1q 500 to 600

Sysname-GigabitEthernet1/0/1.4 quit

·配置子接口GigabitEthernet1/0/1.5能够终结的VLAN报文的第一层VLAN ID为200、第二层VLAN ID范围为500～600。

Sysname interface gigabitethernet 1/0/1.5

Sysname-GigabitEthernet1/0/1.5 vlan-type dot1q vid 200 second-dot1q 500 to 600

Sysname-GigabitEthernet1/0/1.5 quit

·配置子接口GigabitEthernet1/0/1.6能够终结的VLAN报文的第一层VLAN ID为300～400、第二层VLAN ID范围为100。

Sysname interface gigabitethernet 1/0/1.6

Sysname-GigabitEthernet1/0/1.6 vlan-type dot1q vid 300 to 400 second-dot1q 100

Sysname-GigabitEthernet1/0/1.6 quit

·配置子接口GigabitEthernet1/0/1.7能够终结的VLAN报文的第一层VLAN ID为300～400、第二层VLAN ID范围为500～600。

Sysname interface gigabitethernet 1/0/1.7

Sysname-GigabitEthernet1/0/1.7 vlan-type dot1q vid 300 to 400 second-dot1q 500 to 600

Sysname-GigabitEthernet1/0/1.7 quit

·配置子接口GigabitEthernet1/0/1.8能够终结的VLAN报文的第一层VLAN ID为300～400、第二层VLAN ID范围为any。

Sysname interface gigabitethernet 1/0/1.8

Sysname-GigabitEthernet1/0/1.8 vlan-type dot1q vid 300 to 400 second-dot1q any

通过以上配置，子接口GigabitEthernet1/0/1.1～GigabitEthernet1/0/1.8能够终结的VLAN报文规格如下：

子接口

允许终结的VLAN报文的第一层VLAN ID

允许终结的VLAN报文的第二层VLAN ID

GigabitEthernet1/0/1.1

100

100

GigabitEthernet1/0/1.2

100

200～300

GigabitEthernet1/0/1.3

100

1～99、101～199、301～499、601～4094（即1～4094范围内除100、200～300和500～600的值）

GigabitEthernet1/0/1.4

100

500～600

GigabitEthernet1/0/1.5

200

500～600

GigabitEthernet1/0/1.6

300～400

100

GigabitEthernet1/0/1.7

300～400

500～600

GigabitEthernet1/0/1.8

300～400

1～99、101～499、601～4094（即1～4094范围内除100和500～600的值）

\# 使能三层虚拟以太网子接口的QinQ终结功能，并指定子接口可以终结的VLAN报文的最外两层VLAN ID。

·配置子接口Virtual-Ethernet1.1能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID为100。

\<Sysname\> system-view

Sysname interface virtual-ethernet 1.1

Sysname-Virtual-Ethernet1.1 vlan-type dot1q vid 100 second-dot1q 100

Sysname-Virtual-Ethernet1.1 quit

·配置子接口Virtual-Ethernet1.2能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID范围为200～300。

Sysname interface virtual-ethernet 1.2

Sysname-Virtual-Ethernet1.2 vlan-type dot1q vid 100 second-dot1q 200 to 300

Sysname-Virtual-Ethernet1.2 quit

·配置子接口Virtual-Ethernet1.3能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID为any。

Sysname interface virtual-ethernet 1.3

Sysname-Virtual-Ethernet1.3 vlan-type dot1q vid 100 second-dot1q any

Sysname-Virtual-Ethernet1.3 quit

·配置子接口Virtual-Ethernet1.4能够终结的VLAN报文的第一层VLAN ID为100、第二层VLAN ID为500～600。

Sysname interface virtual-ethernet 1.4

Sysname-Virtual-Ethernet1.4 vlan-type dot1q vid 100 second-dot1q 500 to 600

Sysname-Virtual-Ethernet1.4 quit

·配置子接口Virtual-Ethernet1.5能够终结的VLAN报文的第一层VLAN ID为200、第二层VLAN ID为500～600。

Sysname interface virtual-ethernet 1.5

Sysname-Virtual-Ethernet1.5 vlan-type dot1q vid 200 second-dot1q 500 to 600

Sysname-Virtual-Ethernet1.5 quit

·配置子接口Virtual-Ethernet1.6能够终结的VLAN报文的第一层VLAN ID为300～400、第二层VLAN ID范围为100。

Sysname interface virtual-ethernet 1.6

Sysname-Virtual-Ethernet1.6 vlan-type dot1q vid 300 to 400 second-dot1q 100

Sysname-Virtual-Ethernet1.6 quit

·配置子接口GigabitEthernet1/0/1.7能够终结的VLAN报文的第一层VLAN ID为300～400、第二层VLAN ID范围为500～600。

Sysname interface virtual-ethernet 1.7

Sysname-Virtual-Ethernet1.7 vlan-type dot1q vid 300 to 400 second-dot1q 500 to 600

Sysname-Virtual-Ethernet1.7 quit

·配置子接口GigabitEthernet1/0/1.8能够终结的VLAN报文的第一层VLAN ID为300～400、第二层VLAN ID范围为any。

Sysname interface virtual-ethernet 1.8

Sysname-Virtual-Ethernet1.8 vlan-type dot1q vid 300 to 400 second-dot1q any

通过以上配置，子接口Virtual-Ethernet1.1～Virtual-Ethernet1.8能够终结的VLAN报文规格如下：

子接口

允许终结的VLAN报文的第一层VLAN ID

允许终结的VLAN报文的第二层VLAN ID

Virtual-Ethernet1.1

100

100

Virtual-Ethernet1.2

100

200～300

Virtual-Ethernet1.3

100

1～99、101～199、301～499、601～4094（即1～4094范围内除100、200～300和500～600的值）

Virtual-Ethernet1.4

100

500～600

Virtual-Ethernet1.5

200

500～600

Virtual-Ethernet1.6

300～400

100

Virtual-Ethernet1.7

300～400

500～600

Virtual-Ethernet1.8

300～400

1～99、101～499、601～4094（即1～4094范围内除100和500～600的值）

\# 配置子接口GigabitEthernet1/0/1.1能够终结的第一层VLAN ID为10、第二层VLAN ID为100的带有两层或两层以上VLAN Tag的VLAN报文；配置子接口GigabitEthernet1/0/1.2能够终结的VLAN报文的第一层VLAN ID为20、第二层VLAN ID为20。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 10 second-dot1q 100 loose

Sysname-GigabitEthernet1/0/1.1 quit

Sysname interface gigabitethernet 1/0/1.2

Sysname-GigabitEthernet1/0/1.2 vlan-type dot1q vid 20 second-dot1q 20

Sysname-GigabitEthernet1/0/1.2 quit

通过以上配置，GigabitEthernet1/0/1.1、GigabitEthernet1/0/1.2能够终结的报文规格如下：

子接口

允许终结的第一层VLAN ID

允许终结的第二层VLAN ID

是否允许终结携带两层以上VLAN Tag的报文

GigabitEthernet1/0/1.1

10

100

是

GigabitEthernet1/0/1.2

20

20

否

