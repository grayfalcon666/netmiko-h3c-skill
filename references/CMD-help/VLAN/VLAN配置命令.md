<!-- CMD-INDEX
  bandwidth                           | VLAN接口视图         | L65
  default                             | VLAN接口视图         | L121
  description                         | VLAN视图/VLAN接口视图  | L155
  display interface vlan-interface    | 任意视图             | L219
  display vlan                        | 任意视图             | L453
  interface vlan-interface            | 系统视图             | L589
  mac-address                         | VLAN接口视图         | L645
  mtu                                 | VLAN接口视图         | L693
  name                                | VLAN视图           | L743
  reset counters interface vlan-interface | 用户视图             | L793
  shutdown                            | VLAN接口视图         | L835
  vlan                                | 系统视图             | L887
  display port                        | 任意视图             | L955
  port                                | VLAN视图           | L1037
  port access vlan                    | 二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1089
  port hybrid pvid                    | 二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1139
  port hybrid vlan                    | 二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1203
  port link-type                      | 二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1259
  port trunk permit vlan              | 二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1309
  port trunk pvid                     | 二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1365
  display mac-vlan                    | 任意视图             | L1425
  display mac-vlan interface          | 任意视图             | L1529
  mac-vlan enable                     | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1567
  mac-vlan mac-address                | 系统视图             | L1609
  mac-vlan trigger enable             | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1671
  port pvid forbidden                 | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1719
  vlan precedence                     | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L1765
  display ip-subnet-vlan interface    | 任意视图             | L1819
  display ip-subnet-vlan vlan         | ]                | L1905
  ip-subnet-vlan                      | VLAN视图           | L1979
  port hybrid ip-subnet-vlan          | 二层以太网接口视图/二层聚合接口视图 | L2039
  display protocol-vlan interface     | 任意视图             | L2123
  display protocol-vlan vlan          | ]                | L2205
  port hybrid protocol-vlan           | 二层以太网接口视图/二层聚合接口视图 | L2285
  protocol-vlan                       | VLAN视图           | L2371
  display vlan-group                  | 任意视图             | L2461
  vlan-group                          | 系统视图             | L2531
  vlan-list                           | VLAN组视图          | L2585
  display supervlan                   | 任意视图             | L2633
  subvlan                             | VLAN视图           | L2833
  supervlan                           | VLAN视图           | L2893
  display private-vlan                | 任意视图             | L2947
  port private-vlan host              | 二层以太网接口视图/二层聚合接口视图 | L3143
  port private-vlan promiscuous       | 二层以太网接口视图/二层聚合接口视图 | L3253
  port private-vlan trunk promiscuous | 二层以太网接口视图/二层聚合接口视图 | L3391
  port private-vlan trunk secondary   | 二层以太网接口视图/二层聚合接口视图 | L3527
  private-vlan （VLAN interface view）  | VLAN接口视图         | L3735
  private-vlan （VLAN view）            | VLAN视图           | L3837
  private-vlan community              | VLAN视图           | L3903
  private-vlan isolated               | VLAN视图           | L3987
  private-vlan primary                | VLAN视图           | L4087
  display voice-vlan mac-address      | 任意视图             | L4143
  display voice-vlan state            | 任意视图             | L4213
  voice-vlan aging                    | 系统视图             | L4319
  voice-vlan enable                   | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L4369
  voice-vlan mac-address              |                  | L4423
  voice-vlan mode auto                | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L4533
  voice-vlan qos                      | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L4579
  voice-vlan qos trust                | 二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图 | L4637
  voice-vlan security enable          | 系统视图             | L4689
  voice-vlan track lldp               | 系统视图             | L4733
-->

**VLAN \-- VLAN配置命令 \-- bandwidth**

------------------------------------------------------------------------

![说明](VLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[bandwidth**]命令用来配置VLAN接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbps）。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbps。

【使用指导】

接口的期望带宽会对下列内容有影响：

·CBQ队列带宽。具体介绍请参见"ACL和QoS配置指导"中的"拥塞管理"。

·链路开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置VLAN接口1的期望带宽为10000kbps。

\<Sysname\> system-view

Sysname interface vlan-interface 1

Sysname-Vlan-interface1 bandwidth 10000

**VLAN \-- VLAN配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前VLAN接口的缺省配置。

【命令】

**[default**]

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**default**命令并不能保证接口下的所有命令都能恢复到缺省情况，某些命令可能会由于不满足必备条件而恢复失败。因此，执行**default**命令后建议通过**display this**命令确认执行效果。

【举例】

\# 将VLAN接口1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface vlan-interface 1

Sysname-Vlan-interface1 default

**VLAN \-- VLAN配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前VLAN或VLAN接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description*** text*]

**[undo description**]

【缺省情况】

VLAN的描述信息为"VLAN *vlan-id*"，其中*vlan-id*为该VLAN的四位数编号，如果该VLAN的编号不足四位，则会在编号前增加0，补齐四位。例如，VLAN 100的描述信息为"VLAN 0100"；VLAN接口的描述信息为该VLAN接口的接口名，如"Vlan-interface1 Interface"。

【视图】

VLAN视图/VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：VLAN或VLAN接口的描述信息，为1～255个字符的字符串，可以包含字母（区分大小写）、数字、特殊字符（包括\~ ! @ \# \$ % \^ & \* ( ) - \_ + = { } [  \| \\ : ; \" \' \< \> , . /]）、空格以及符合unicode编码规范的其他文字和符号。

【使用指导】

当设备上配置的VLAN较多时，用户可以根据功能或者连接情况为VLAN或VLAN接口配置特定的描述信息，以便记忆和管理VLAN或VLAN接口。

【举例】

\# 将VLAN 2的描述信息配置为sales-private。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 description sales-private

\# 将VLAN接口2的描述信息配置为linktoPC56。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 quit

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 description linktoPC56

【相关命令】

·**display** **interface vlan-interface**

·**display** **vlan**

**VLAN \-- VLAN配置命令 \-- display interface vlan-interface**

------------------------------------------------------------------------

**[display** **interface vlan-interface**]命令用来显示VLAN接口的相关信息。

【命令】

**[display interface** **vlan-interface** [ *interface-number*  [ **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan-interface**]：显示VLAN接口的相关信息。

*[interface-number*]：VLAN接口的编号，显示指定VLAN接口的信息。不指定该参数时，将显示已创建的所有VLAN接口的信息。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，指定**brief**参数而不指定**description**参数时，只显示描述信息中的前27个字符，超出部分不显示；指定**description**参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示VLAN-interface 2的相关信息。（支持统计功能的VLAN接口的显示信息）

\<Sysname\> display interface vlan-interface 2

Vlan-interface2

Current state: DOWN

Line protocol state: DOWN

Description: Vlan-interface2 Interface

Bandwidth: 100000kbps

Maximum Transmit Unit: 1500

Internet protocol processing : disabled

IP Packet Frame Type:PKTFMT_ETHNT_2,  Hardware Address: 000f-e249-8050

IPv6 Packet Frame Type:PKTFMT_ETHNT_2,  Hardware Address: 000f-e249-8050

Last clearing of counters: Never

     Last 300 seconds input:  0 bytes/sec 0 packets/sec

     Last 300 seconds output:  0 bytes/sec 0 packets/sec

     0 packets input, 0 bytes, 0 drops

     0 packets output, 0 bytes, 0 drops

\# 显示VLAN-interface 10的相关信息。（不支持统计功能的VLAN接口的显示信息）

\<Sysname\> display interface vlan-interface 10

Vlan-interface10

Current state: UP

Line protocol state: UP

Description: Vlan-interface10 Interface

Bandwidth: 100000kbps

Maximum Transmit Unit: 1500

Internet Address is 192.168.1.54/24 Primary

IP Packet Frame Type:PKTFMT_ETHNT_2,  Hardware Address: 0023-89b6-d613

IPv6 Packet Frame Type:PKTFMT_ETHNT_2,  Hardware Address: 0023-89b6-d613

Last clearing of counters: Never

\# 显示VLAN-interface 2的概要信息。

\<Sysname\> display interface vlan-interface 2 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Vlan2                DOWN DOWN     \--

表1-1 display interface vlan-interface命令显示信息描述表

字段

描述

Vlan-interface2

VLAN接口名

Current state

VLAN接口的物理状态，状态可能为：

·DOWN ( Administratively )：表示该VLAN接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该VLAN接口的管理状态为开启，但物理状态为关闭，即该接口对应的VLAN内没有处于UP状态的物理端口（可能因为没有物理连线或者线路故障）

·UP：该端口的管理状态和物理状态均为开启

Line protocol state

VLAN接口的链路层协议状态，状态可能为：

·DOWN：该VLAN接口的协议状态为关闭

·UP：该VLAN接口的协议状态为开启

Description

用户通过**description**命令给VLAN接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Bandwidth

VLAN接口的期望带宽

Maximum Transmit Unit

VLAN接口允许通过的最大传输单元

Internet protocol processing : disabled

该接口还不具有处理IP报文的能力（当没有为该接口配置IP地址时会显示该信息）

Internet Address is 192.168.1.54/24 Primary

该接口的主IP地址为192.168.1.54/24（只有为该接口配置主IP地址后才会显示该信息）

IP Packet Frame Type

IPv4发送帧格式

Hardware Address

VLAN接口对应的MAC地址

IPv6 Packet Frame Type

IPv6发送帧格式

Last clearing of counters

最近一次使用**reset counters interface vlan-interface**命令清除接口下的统计信息的时间（如果从设备启动一直没有执行**reset counters interface vlan-interface**命令清除过该接口下的统计信息，则显示Never）

Last 300 seconds input:  0 bytes/sec 0 packets/sec

Last 300 seconds output:  0 bytes/sec 0 packets/sec

当前接口最近300秒内输入（input）和输出（output）报文的平均速率（单位为bps和pps）（只有支持统计功能的VLAN接口才显示该信息）

0 packets input, 0 bytes, 0 drops

接口输入的报文总数（分别以包和字节为单位进行了统计），输入报文中丢弃的报文数（只有支持统计功能的VLAN接口才显示该信息）

0 packets output, 0 bytes, 0 drops

接口输出的报文总数（分别以包和字节为单位进行了统计），输出报文中丢弃的报文数（只有支持统计功能的VLAN接口才显示该信息）

Brief information on interface(s) under route mode

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上是不通的

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Protocol

接口数据链路层协议状态，取值为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址

【相关命令】

·**reset counters interface vlan-interface**

**VLAN \-- VLAN配置命令 \-- display vlan**

------------------------------------------------------------------------

**[display** **vlan**]命令用来显示VLAN的相关信息。

【命令】

**[display** **vlan** [ *vlan-id1* [ **to** *vlan-id2*  \| **all** \| **dynamic** \| **reserved** \| **static** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vlan-id1*]：显示指定VLAN的信息。*vlan-id1*为VLAN的编号，取值范围为1～4094。

*[vlan-id1* **to** *vlan-id2*]：显示ID在指定范围内的VLAN的信息。*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094。*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值。

**[all**]：显示除保留VLAN外的其他VLAN的信息。

**[dynamic**]：显示系统动态创建的VLAN的数量和编号。动态VLAN是指通过MVRP协议生成或通过RADIUS服务器下发的VLAN。

**[reserved**]：显示系统保留VLAN的信息。保留VLAN是设备根据功能实现的需要预留的VLAN。保留VLAN由协议模块来指定，为协议模块服务，用户不能对保留VLAN进行任何操作。

**[static**]：显示系统静态创建的VLAN的数量和VLAN编号。静态VLAN是指通过命令行手工创建的VLAN。

【举例】

\# 显示VLAN 2的信息。

\<Sysname\> display vlan 2

 VLAN ID: 2

 VLAN type: Static

 Route interface: Not configured

 Description: VLAN 0002

 Name: VLAN 0002

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/1  GigabitEthernet1/0/2  GigabitEthernet1/0/3

\# 显示VLAN 3的信息。

\<Sysname\> display vlan 3

 VLAN ID: 3

 VLAN type: static

 Route interface: Configured

 IPv4 address: 1.1.1.1

 IPv4 subnet mask: 255.255.255.0

 Description: VLAN 0003

 Name: VLAN 0003

 Tagged ports:   None

 Untagged ports: None

表1-2 display vlan命令显示信息描述表

字段

解释

VLAN ID

VLAN的编号

VLAN type

VLAN的类型：

·Static：静态VLAN

·Dynamic：动态VLAN

Route interface

设备上是否创建了对应的VLAN接口：

·Not configured：未创建

·Configured：已创建

Description

VLAN的描述信息

Name

VLAN的名称

IP address

VLAN接口的主用IP地址（如果VLAN接口没有配置IP地址，则不显示该字段），如果VLAN接口上还配置了从IP地址，可以使用**display interface vlan-interface**或者在VLAN接口视图下使用**display this**命令查看

Subnet mask

VLAN接口的主用IP地址的子网掩码（如果VLAN接口没有配置IP地址，则不显示该字段）

Tagged ports

该VLAN报文从哪些端口发送时需要携带Tag标记

Untagged ports

该VLAN报文从哪些端口发送时不需要携带Tag标记

【相关命令】

·**vlan**

**VLAN \-- VLAN配置命令 \-- interface vlan-interface**

------------------------------------------------------------------------

**[interface vlan-interface**]命令用来创建VLAN接口并进入VLAN接口视图。如果该VLAN接口已经存在，则直接进入VLAN接口视图。

**[undo interface vlan-interface**]命令用来删除指定的VLAN接口。

【命令】

**[interface vlan-interface ***interface-number*]

**[undo interface vlan-interface** *interface-number*]

【缺省情况】

未创建VLAN接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：VLAN接口的编号，取值范围为1～4094。

【使用指导】

·在创建VLAN接口之前，对应的VLAN必须已经存在，否则将不能创建指定的VLAN接口。

·Sub VLAN及在Primary VLAN interface下配置了三层互通的Secondary VLAN不能创建对应的VLAN接口。有关Sub VLAN的详细介绍，请参见"二层技术-以太网交换配置指导"中的"Super VLAN"；有关Secondary VLAN的详细介绍，请参见"二层技术-以太网交换配置指导"中的"Private VLAN"。

【举例】

\# 创建VLAN接口2并进入视图。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 quit

Sysname interface vlan-interface 2

Sysname-Vlan-interface2

【相关命令】

·**display interface vlan-interface**

**VLAN \-- VLAN配置命令 \-- mac-address**

------------------------------------------------------------------------

![说明](VLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address**]命令用来配置VLAN接口的MAC地址。

**[undo mac-address**]命令用来恢复缺省情况。

【命令】

**[mac-address** *mac-address*]

**[undo mac-address**]

【缺省情况】

本命令的缺省情况与设备型号有关，请以设备的实际情况为准。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：MAC地址，形式为H-H-H。

【举例】

\# 配置VLAN接口2的MAC地址为0001-0001-0001。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mac-address 1-1-1

**VLAN \-- VLAN配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置VLAN接口的MTU值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

本命令的缺省情况与设备型号有关，请以设备的实际情况为准。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：表示接口允许通过的MTU（Maximum Transmission Unit，最大传输单元）值的大小，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

如果当前接口同时配置**mtu**和**ip mtu**命令，则设备会以**ip mtu**命令配置的接口MTU值对报文进行分片，不会再按照**mtu**命令配置的MTU值对报文进行分片。有关**ip mtu**命令的详细介绍，请参见"三层技术-IP业务命令参考"中的"IP性能优化"。

【举例】

\# 配置VLAN接口1的MTU值为1492字节。

\<Sysname\> system-view

Sysname interface vlan-interface 1

Sysname-Vlan-interface1 mtu 1492

【相关命令】

·**display** **interface vlan-interface**

**VLAN \-- VLAN配置命令 \-- name**

------------------------------------------------------------------------

**[name**]命令用来指定当前VLAN的名称。

**[undo name**]命令用来恢复缺省情况。

【命令】

**[name ***text*]

**[undo name**]

【缺省情况】

VLAN的名称为"VLAN *vlan-id*"，其中*vlan-id*为该VLAN的四位数编号，如果该VLAN的编号不足四位，则会在编号前增加0，补齐四位。例如，VLAN 100的名称为"VLAN 0100"。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：VLAN名称，为1～32个字符的描述信息，可以包含字母（区分大小写）、数字、特殊字符（包括\~ ! @ \# \$ % \^ & \* ( ) - \_ + = { } [  \| \\ : ; \" \' \< \> , . /]）、空格以及符合unicode编码规范的其他文字和符号。

【使用指导】

当设备上配置了802.1X或MAC地址认证功能后，可以通过RADIUS服务器来对认证通过的端口下发VLAN。某些RADIUS服务器可以向设备发送需要下发的VLAN编号或者VLAN名称，当VLAN数量很多的时候，使用名称可以更明确的定位VLAN。

【举例】

\# 指定VLAN 2的名称为"test vlan"。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 name test vlan

【相关命令】

·**display vlan**

**VLAN \-- VLAN配置命令 \-- reset counters interface vlan-interface**

------------------------------------------------------------------------

**[reset counters interface vlan-interface**]命令用来清除VLAN接口的统计信息。

【命令】

**[reset counters interface** **vlan-interface** [ *interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：VLAN接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定*interface-number*，则清除所有VLAN接口的统计信息；

·如果指定*interface-number*，则清除指定VLAN接口的统计信息。

【举例】

\# 清除VLAN接口2的统计信息。

\<Sysname\> reset counters interface vlan-interface 2

【相关命令】

·**display interface vlan-interface**

**VLAN \-- VLAN配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来手工关闭VLAN接口。

**[undo shutdown**]命令用来取消手工关闭VLAN接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

本命令的缺省情况与设备型号有关，请以设备的实际情况为准。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·如果未手工关闭VLAN接口，此时VLAN接口状态受VLAN中端口状态的影响，即：当VLAN中所有以太网端口状态均为down时，VLAN接口为down状态，即关闭状态；当VLAN中有一个或一个以上的以太网端口处于up状态时，则VLAN接口处于up状态。

·如果手工关闭VLAN接口，则VLAN接口的状态始终为down（Administratively），不受VLAN中端口状态的影响。

·配置VLAN接口参数前，为了避免配置过程中对网络造成影响，建议先使用**shutdown**命令手工关闭接口，之后再配置参数。配置完成后，使用**undo shutdown**命令取消手工关闭接口，使配置的参数生效。

·当VLAN接口出现故障时，可以使用**shutdown**命令手工关闭接口，然后再使用**undo shutdown**命令取消手工关闭接口，这样有可能使接口恢复正常。

·关闭和打开VLAN接口对于属于这个VLAN的任何一个以太网端口本身都不起作用，以太网端口的状态不随VLAN接口状态的改变而改变。

【举例】

\# 将VLAN接口2关闭后再重新打开。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 shutdown

Sysname-Vlan-interface2 undo shutdown

**VLAN \-- VLAN配置命令 \-- vlan**

------------------------------------------------------------------------

**[vlan** *vlan-id*]命令用来创建VLAN并进入VLAN视图。如果指定的VLAN已创建，则直接进入该VLAN的视图。

**[vlan** *vlan-id1*** to*** vlan-id2*]命令用来批量创建*vlan-id1*～*vlan-id2*之间的所有VLAN，保留VLAN除外。

**[vlan all**]命令用来批量创建VLAN 1～4094。

**[undo vlan**]命令用来删除VLAN。

【命令】

**[vlan** { *vlan-id1* [ **to** *vlan-id2*  *\|* **all** }]]

**[undo vlan****[ **to** *vlan-id2*  *\|* **all** }]]

【缺省情况】

系统只有一个缺省VLAN（VLAN 1）。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id1*]：VLAN的编号，取值范围为1～4094。

*[vlan-id1* **to** *vlan-id2*]：指定VLAN的编号范围。*vlan-id1*和*vlan-id2*为VLAN的编号，取值范围为1～4094。*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值。

**[all**]：除保留VLAN外的其他VLAN，当设备允许创建的最大VLAN数小于4094时，不支持该参数。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

【使用指导】

·VLAN 1为系统缺省VLAN，用户不能创建和删除。

·保留VLAN是系统为实现特定功能预留的VLAN，用户也不能手工创建和删除。

·动态学习到的VLAN，以及被其他应用锁定不让删除的VLAN，都不能使用**undo vlan**命令直接删除。只有将相关配置删除之后，才能删除相应的VLAN。

【举例】

\# 创建VLAN 2，并进入该VLAN视图。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2

\# 批量创建VLAN 4～100。

\<Sysname\> system-view

Sysname vlan 4 to 100

【相关命令】

·**display vlan**

**VLAN \-- 基于端口的VLAN配置命令 \-- display port**

------------------------------------------------------------------------

**[display port**]命令用来显示设备上当前存在的Hybrid或Trunk端口。显示的信息包括端口对应的端口名、缺省VLAN ID和允许通过的VLAN ID。

【命令】

**[display** **port**[ { **hybrid** \| **trunk** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[hybrid**]：显示系统当前存在的Hybrid端口。

**[trunk**]：显示系统当前存在的Trunk端口。

【举例】

\# 显示当前系统存在的Hybrid端口。

\<Sysname\> display port hybrid

Interface            PVID  VLAN Passing

GE1/0/4              100   Tagged:  1000, 1002, 1500, 1600-1611, 2000,

                                    2555-2558, 3000, 4000

                           Untagged:1, 10, 15, 18, 20-30, 44, 55, 67, 100,

                                    150-160, 200, 255, 286, 300-302

\# 显示当前系统存在的Trunk端口。

\<Sysname\> display port trunk

Interface            PVID  VLAN Passing

GE1/0/8              2     1-4, 6-100, 145, 177, 189-200, 244, 289, 400,

                           555, 600-611, 1000, 2006-2008

表1-3 display port命令显示信息描述表

字段

描述

Interface

接口名称

PVID

该端口的缺省VLAN ID

VLAN Passing

表示该端口实际通过的VLAN（该VLAN已经创建，并且接口允许其通过）

Tagged

表示哪些VLAN的报文通过该端口时必须携带VLAN Tag

Untagged

表示哪些VLAN的报文通过该端口时必须去掉VLAN Tag

**VLAN \-- 基于端口的VLAN配置命令 \-- port**

------------------------------------------------------------------------

**[port**]命令用来向当前VLAN中添加一个或一组Access端口。

**[undo port**]命令用来从当前VLAN中删除一个或一组Access端口。

【命令】

**[port ***interface-list*]

**[undo port ***interface-list*]

【缺省情况】

系统将所有端口都加入到VLAN 1。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-list*]：以太网接口列表。表示方式为*interface-list *= { *interface-type interface-number1* [ **to** *interface-type interface-number2*  }&\<1-10\>]，其中*interface-type interface-number*为端口类型和端口编号，*interface-number2*的值要大于或等于*interface-number1*的值，&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·通过本命令只能将Access端口加入到VLAN中，不能将Trunk和Hybrid端口加入到VLAN中。

·设备上的所有端口的缺省链路类型都是Access类型，但用户可以自行切换端口类型，具体配置可参考命令**port link-type**。

【举例】

\# 向VLAN2中添加端口GigabitEthernet1/0/1～GigabitEthernet1/0/3。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 port gigabitethernet 1/0/1 to gigabitethernet 1/0/3

【相关命令】

·**display vlan**

**VLAN \-- 基于端口的VLAN配置命令 \-- port access vlan**

------------------------------------------------------------------------

**[port access vlan**]命令用来将当前Access端口加入到指定的VLAN中。

**[undo port access vlan**]命令用来恢复缺省情况。

【命令】

**[port access vlan ***vlan-id*]

**[undo** **port** **access vlan**]

【缺省情况】

所有Access端口都属于VLAN 1。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定的VLAN编号，取值范围为1～4094。该VLAN必须是设备上已创建的VLAN，否则，该命令执行失败。

【使用指导】

在将Access端口加入到指定VLAN之前，该VLAN必须已经存在。

【举例】

\# 将GigabitEthernet1/0/1端口加入到VLAN 3中。

\<Sysname\> system-view

Sysname vlan 3

Sysname-vlan3 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port access vlan 3

**VLAN \-- 基于端口的VLAN配置命令 \-- port hybrid pvid**

------------------------------------------------------------------------

**[port hybrid pvid**]命令用来配置Hybrid端口的缺省VLAN。

**[undo port hybrid pvid**]命令用来配置Hybrid端口的缺省VLAN为1。

【命令】

**[port hybrid pvid vlan*** vlan-id*]

**[undo port hybrid pvid**]

【缺省情况】

Hybrid端口的缺省VLAN为该端口在链路类型为Access时的所属VLAN。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定接口的缺省的VLAN ID，取值范围为1～4094。

【使用指导】

·对Hybrid端口，执行**undo vlan**命令删除端口的缺省VLAN后，端口的缺省VLAN配置不会改变，即可以使用已经不存在的VLAN作为缺省VLAN。

·建议本机Hybrid端口的缺省VLAN和相连的对端交换机的Hybrid端口的缺省VLAN保持一致。

·配置缺省VLAN后，必须使用**port hybrid** **vlan**命令配置允许缺省VLAN的报文通过，出接口才能转发缺省VLAN的报文。

【举例】

\# 配置端口GigabitEthernet1/0/1（Hybrid类型）的缺省VLAN为100，并允许VLAN 100通过。

\<Sysname\> system-view

Sysname vlan 100

Sysname-vlan100 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type hybrid

Sysname-GigabitEthernet1/0/1 port hybrid pvid vlan 100

Sysname-GigabitEthernet1/0/1 port hybrid vlan 100 untagged

【相关命令】

·**port hybrid vlan**

·**port link-type**

**VLAN \-- 基于端口的VLAN配置命令 \-- port hybrid vlan**

------------------------------------------------------------------------

**[port hybrid vlan**]命令用来允许指定的VLAN通过当前Hybrid端口。

**[undo port hybrid vlan**]命令用来禁止指定的VLAN通过当前Hybrid端口。

【命令】

**[port hybrid vlan**[ *vlan-id-list* { **tagged** \| **untagged** }]]

**[undo port hybrid vlan** *vlan-id-list*]

【缺省情况】

Hybrid端口只允许该端口在链路类型为Access时的所属VLAN的报文以Untagged方式通过。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，Hybrid端口允许通过的VLAN范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。该VLAN必须是设备上已创建的VLAN，否则，该命令执行失败。

**[tagged**]：该端口在转发指定的VLAN报文时将携带VLAN Tag。

**[untagged**]：该端口在转发指定的VLAN报文时将去掉VLAN Tag。

【使用指导】

Hybrid端口允许多个VLAN通过。如果多次使用**port hybrid** **vlan**命令，那么Hybrid端口上允许通过的VLAN是这些*vlan-id-list*的合集。

【举例】

\# 配置端口GigabitEthernet1/0/1为Hybrid端口，允许VLAN 2、4、50～VLAN 100通过，并且发送这些VLAN的报文时携带VLAN Tag。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type hybrid

Sysname-GigabitEthernet1/0/1 port hybrid vlan 2 4 50 to 100 tagged

【相关命令】

·**port link-type**

**VLAN \-- 基于端口的VLAN配置命令 \-- port link-type**

------------------------------------------------------------------------

**[port link-type**]命令用来配置当前端口的链路类型。

**[undo port link-type**]命令用来恢复缺省情况。

【命令】

**[port link-type**[ { **access** \| **hybrid** \| **trunk** }]]

**[undo port link-type**]

【缺省情况】

所有端口的链路类型均为Access类型。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[access**]：配置端口的链路类型为Access类型。

**[hybrid**]：配置端口的链路类型为Hybrid类型。

**[trunk**]：配置端口的链路类型为Trunk类型。

【使用指导】

Trunk端口和Hybrid端口之间不能直接切换，只能先设为Access端口，再配置为其他类型端口。

【举例】

\# 配置端口GigabitEthernet1/0/1配置为Trunk端口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type trunk

**VLAN \-- 基于端口的VLAN配置命令 \-- port trunk permit vlan**

------------------------------------------------------------------------

**[port trunk permit vlan**]命令用来允许指定的VLAN通过当前Trunk端口。

**[undo port trunk permit vlan**]命令用来禁止指定的VLAN通过当前Trunk端口。

【命令】

**[port trunk permit vlan**[ { *vlan-id-list* \| **all** }]]

**[undo port trunk permit vlan**[ { *vlan-id-list* \| **all** }]]

【缺省情况】

Trunk端口只允许VLAN 1的报文通过。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，Trunk端口允许通过的VLAN范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

**[all**]：表示允许所有VLAN通过该Trunk端口。建议用户谨慎使用**port trunk permit vlan all**命令，以防止未授权VLAN的用户通过该端口访问受限资源。

【使用指导】

·Trunk端口可以允许多个VLAN通过。如果多次执行**port trunk permit vlan**命令，那么Trunk端口上允许通过的VLAN是这些*vlan-id-list*的集合。

·Trunk端口发送出去的报文，只有缺省VLAN的报文不带VLAN Tag，其他VLAN的报文均会保留VLAN Tag。

【举例】

\# 配置端口GigabitEthernet1/0/1为Trunk端口，允许VLAN 2、4、50～100通过。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type trunk

Sysname-GigabitEthernet1/0/1 port trunk permit vlan 2 4 50 to 100

【相关命令】

·**port link-type**

**VLAN \-- 基于端口的VLAN配置命令 \-- port trunk pvid**

------------------------------------------------------------------------

**[port trunk pvid**]命令用来配置Trunk端口的缺省VLAN。

**[undo **]**port trunk pvid**命令用来恢复缺省情况。

【命令】

**[port trunk pvid vlan*** vlan-id*]

**[undo **]**port trunk pvid**

【缺省情况】

Trunk端口的缺省VLAN为VLAN 1。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定接口的缺省VLAN ID，取值范围为1～4094。

【使用指导】

·对Trunk端口，执行**undo vlan**命令删除端口的缺省VLAN后，端口的缺省VLAN配置不会改变，即使用已经不存在的VLAN作为缺省VLAN。

·本端设备Trunk端口的缺省VLAN ID和相连的对端设备的Trunk端口的缺省VLAN ID必须一致，否则报文将不能正确传输。

·配置缺省VLAN后，必须使用**port trunk permit vlan**命令配置允许缺省VLAN的报文通过，出接口才能转发缺省VLAN的报文。

【举例】

\# 配置端口GigabitEthernet1/0/1（Trunk类型）的缺省VLAN为VLAN 100，并允许VLAN 100通过。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type trunk

Sysname-GigabitEthernet1/0/1 port trunk pvid vlan 100

Sysname-GigabitEthernet1/0/1 port trunk permit vlan 100

【相关命令】

·**port link-type**

·**port trunk permit vlan**

**VLAN \-- 基于MAC的VLAN配置命令 \-- display mac-vlan**

------------------------------------------------------------------------

**[display mac-vlan**]命令用来显示MAC VLAN表项。

【命令】

**[display mac-vlan**[ { **all** \| **dynamic** \| **mac-address** *mac-address* [ **mask** *mac-mask* ] \| **static** \| **vlan** *vlan-id* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有MAC VLAN表项。

**[dynamic**]：显示动态配置的MAC VLAN表项。

**[mac-address ***mac-address*]：显示指定MAC地址对应的MAC VLAN表项，*mac-address*格式为H-H-H。

**[mask** *mac-mask*]：显示指定范围的MAC VLAN表项。*mac-mask*为二进制时高位必须为连续1，为十六进制时高位必须为连续F。缺省十六进制值为全F。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[static**]：显示静态配置的MAC VLAN表项。

**[vlan** *vlan-id*]：显示指定VLAN对应的MAC VLAN表项。*vlan-id*取值范围为1～4094。

【举例】

\# 显示所有MAC VLAN表项。

\<Sysname\> display mac-vlan all

The following MAC VLAN entries exist:

State: S - Static, D - Dynamic

MAC address        Mask                VLAN ID   Dot1q      State

0008-0001-0000     FFFF-FF00-0000      5         3          S

0002-0001-0000     FFFF-FFFF-FFFF      5         3          S&D

Total MAC VLAN entries count: 2

表1-4 display mac-vlan命令显示信息描述表

字段

描述

The following MAC VLAN entries exist

目前设备上存在以下MAC VLAN表项

S - Static

以下显示信息中，S表示静态配置的MAC VLAN

D - Dynamic

以下显示信息中，D表示动态配置的MAC VLAN

MAC address

MAC地址

Mask

MAC地址对应的掩码

VLAN ID

MAC地址对应的VLAN ID

Dot1q

MAC地址对应的802.1p优先级

State

MAC VLAN表项属性：

·S：表示该表项是用户静态配置的

·D：表示该表项是接入认证功能动态下发的

·S&D：表示该表项既是静态配置的也是动态下发的

【相关命令】

·**mac-vlan mac-address**

**VLAN \-- 基于MAC的VLAN配置命令 \-- display mac-vlan interface**

------------------------------------------------------------------------

**[display mac-vlan interface**]命令用来显示所有使能了MAC VLAN功能的接口。

【命令】

**[display mac-vlan interface**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有使能了MAC VLAN功能的接口。

\<Sysname\> display mac-vlan interface

MAC VLAN is enabled on following ports:

GigabitEthernet1/0/1  GigabitEthernet1/0/2  GigabitEthernet1/0/3

【相关命令】

·**mac-vlan enable**

**VLAN \-- 基于MAC的VLAN配置命令 \-- mac-vlan enable**

------------------------------------------------------------------------

**[mac-vlan enable**]命令用来使能MAC VLAN功能。

**[undo mac-vlan enable**]命令用来恢复缺省情况。

【命令】

**[mac-vlan enable**]

**[undo mac-vlan enable**]

【缺省情况】

MAC VLAN功能处于关闭状态。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在接口GigabitEthernet1/0/1上使能MAC VLAN功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname--GigabitEthernet1/0/1 mac-vlan enable

【相关命令】

·**display mac-vlan interface**

**VLAN \-- 基于MAC的VLAN配置命令 \-- mac-vlan mac-address**

------------------------------------------------------------------------

**[mac-vlan mac-address**]命令用来配置MAC VLAN表项，即配置MAC地址与VLAN的关联。

**[undo mac-vlan**]命令用来删除指定的MAC VLAN表项。

【命令】

**[mac-vlan mac-address*** mac-address* [ **mask** *mac-mask*  **vlan** *vlan-id*  **dot1q** *priority* ]]

**[undo mac-vlan**[ { **all** \| **mac-address** *mac-address* [ **mask** *mac-mask* ] \| **vlan** *vlan-id* }]]

【缺省情况】

不存在MAC VLAN表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mac-address **]*mac-address*：MAC地址，*mac-address*格式为H-H-H，不支持组播MAC地址和全0的MAC地址。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[mask**]* mac-mask*：MAC地址的掩码，*mac-mask*为二进制时高位必须为连续1，为十六进制时高位必须为连续F。缺省十六进制值为全F。该参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[vlan ***vlan-id*]：VLAN的编号，取值范围为1～4094。

**[dot1q***priority*]：802.1p优先级，取值为0～7，缺省值为0。取值越大，802.1p优先级越高。

**[all**]：表示删除所有的静态MAC VLAN表项。

【使用指导】

设备维护两张MAC VLAN表，一张是通过指定**mask**参数配置的MAC VLAN表，该表里的表项描述的是一类MAC地址和VLAN、802.1p优先级之间的关系；一张是不指定**mask**参数配置的MAC VLAN表，该表里的表项描述的是单个MAC地址和VLAN、优先级之间的关系。根据用户的配置，系统将自动在这两张MAC VLAN表里添加/删除MAC VLAN表项。

【举例】

\# 配置MAC地址0000-0001-0001与VLAN 100关联，并指定该表项中VLAN 100的802.1p优先级为7。

\<Sysname\> system-view

Sysname mac-vlan mac-address 0-1-1 vlan 100 dot1q 7

\# 配置十六进制前6位为1211-22的MAC地址与VLAN 100关联，并指定该表项中VLAN 100的802.1p优先级为4。

\<Sysname\> system-view

Sysname mac-vlan mac-address 1211-2222-3333 mask ffff-ff00-0000 vlan 100 dot1q 4

【相关命令】

·**display mac-vlan**

**VLAN \-- 基于MAC的VLAN配置命令 \-- mac-vlan trigger enable**

------------------------------------------------------------------------

**[mac-vlan trigger enable**]命令用来使能MAC VLAN的动态触发功能。

**[undo mac-vlan trigger enable**]命令用来恢复缺省情况。

【命令】

**[mac-vlan trigger enable**]

**[undo mac-vlan trigger enable**]

【缺省情况】

MAC VLAN的动态触发功能处于关闭状态。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能MAC VLAN的动态触发功能后，只有端口接收的报文的源MAC地址精确匹配了MAC VLAN表项，才会动态触发该端口加入相应VLAN。

【举例】

\# 在接口GigabitEthernet1/0/1上使能MAC VLAN的动态触发功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-vlan trigger enable

【相关命令】

·**mac-vlan mac-address**

·**port pvid forbidden**

**VLAN \-- 基于MAC的VLAN配置命令 \-- port pvid forbidden**

------------------------------------------------------------------------

**[port pvid forbidden**]命令用来配置当报文源MAC地址与MAC VLAN表项的MAC地址未精确匹配时，禁止该报文在PVID内转发。

**[undo port pvid forbidden**]命令用来恢复缺省情况。

【命令】

**[port pvid forbidden**]

**[undo port pvid forbidden**]

【缺省情况】

当报文源MAC地址与MAC VLAN表项的MAC地址未精确匹配时，允许该报文在PVID内转发。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该功能仅适用于和MAC VLAN的动态触发功能配合使用。

【举例】

\# 在接口GigabitEthernet1/0/1上配置当报文源MAC地址不匹配MAC VLAN表项时，禁止该报文在PVID内转发。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port pvid forbidden

【相关命令】

·**mac-vlan trigger enable**

**VLAN \-- 基于MAC的VLAN配置命令 \-- vlan precedence**

------------------------------------------------------------------------

**[vlan precedence**]命令用来配置当前接口的VLAN优先匹配方式。

**[undo vlan precedence**]命令用来恢复缺省情况。

【命令】

**[vlan precedence**[ { **mac-vlan** \| **ip-subnet-vlan** }]]

**[undo vlan precedence**]

【缺省情况】

对于基于MAC的VLAN和基于IP子网的VLAN，优先根据MAC地址来匹配VLAN。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mac-vlan**]：表示优先根据MAC地址来匹配VLAN。

**[ip-subnet-vlan**]：表示优先根据IP子网来匹配VLAN。

【使用指导】

·本命令只对基于MAC的VLAN和基于IP子网的VLAN有效。

·当使用**mac-vlan trigger enable**命令使能MAC VLAN的动态触发功能后，建议用户在配置VLAN匹配优先级时，使用**vlan precedence mac-vlan**命令，使报文优先根据MAC地址来匹配VLAN，此时**vlan precedence ip-subnet-vlan**命令不能生效。

【举例】

\# 配置接口GigabitEthernt1/0/1优先根据MAC地址来匹配VLAN。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vlan precedence mac-vlan

【相关命令】

·**mac-vlan trigger enable**

**VLAN \-- 基于IP子网的VLAN配置命令 \-- display ip-subnet-vlan interface**

------------------------------------------------------------------------

**[display ip-subnet-vlan interface**]命令用于显示端口关联的子网VLAN的信息。

【命令】

**[display ip-subnet-vlan interface** { *interface-type interface-number1* [ **to** *interface-type interface-number2*  \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number1*]：端口的类型和编号。

*[interface-type interface-number1* **to** *interface-type interface-number2*]：端口的类型和范围。

**[all**]：显示所有端口关联的子网VLAN的信息。

【举例】

\# 显示端口GigabitEthernet1/0/1关联的子网VLAN的信息。

\<Sysname\> display ip-subnet-vlan interface gigabitethernet1/0/1

 Interface: GigabitEthernet1/0/1

  VLAN ID   Subnet index    IP address       Subnet mask       Status

  3         0               192.168.1.0      255.255.255.0     Active

  4         N/A             N/A              N/A               Inactive

  4094      65535           172.16.1.1       255.255.0.0       Inactive

表1-5 display ip-subnet-vlan interface命令显示信息描述表

字段

描述

VLAN ID

子网VLAN的编号

Subnet index

IP子网的索引，N/A表示该VLAN下未配置任何子网VLAN

IP address

IP子网的地址，N/A表示该VLAN下未配置子网地址

Subnet mask

IP子网的掩码，N/A表示该VLAN下未配置子网掩码

Status

该子网VLAN在端口的生效情况：

·Active：表示生效

·Inactive：表示未生效（如子网VLAN配置未完成或端口未允许子网VLAN通过）

【相关命令】

·**display ip-subnet-vlan vlan**

·**ip-subnet-vlan**

·**port hybrid ip-subnet-vlan**

**VLAN \-- 基于IP子网的VLAN配置命令 \-- display ip-subnet-vlan vlan**

------------------------------------------------------------------------

**[display ip-subnet-vlan vlan**]命令用于显示指定的或所有子网VLAN的信息。

【命令】

**[display ip-subnet-vlan vlan****[-*id1* [ **to** *vlan*-*id2*  *\|* **all** }]]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vlan*-*id1*]：显示指定的子网VLAN的信息，*vlan*-*id1*表示VLAN的编号，取值范围为1～4094。

*[vlan*-*id1* **to** *vlan*-*id2*]：显示指定VLAN范围内的子网VLAN的信息。*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值。

**[all**]：显示所有子网VLAN的信息。

【举例】

\# 显示所有子网VLAN的信息。

\<Sysname\> display ip-subnet-vlan vlan all

 VLAN ID: 3

  Subnet index      IP address      Subnet mask

  0                 192.168.1.0     255.255.255.0

表1-6 display ip-subnet-vlan vlan命令显示信息描述表

字段

描述

VLAN ID

子网VLAN的编号

Subnet index

IP子网的索引

IP address

IP子网的地址（可以是IP地址或网络地址）

Subnet mask

IP子网的掩码

【相关命令】

·**display ip-subnet-vlan interface**

·**ip-subnet-vlan**

·**port hybrid ip-subnet-vlan**

**VLAN \-- 基于IP子网的VLAN配置命令 \-- ip-subnet-vlan**

------------------------------------------------------------------------

**[ip-subnet-vlan**]命令用来配置当前VLAN与指定的IP子网或IP地址关联。

**[undo ip-subnet-vlan**]命令用于取消当前VLAN与IP子网或IP地址的关联。

【命令】

**[ip-subnet-vlan** [ *ip-subnet-index*  **ip** *ip-address*  *mask* ]]

**[undo ip-subnet-vlan** { *ip-subnet-index* [ **to** *ip-subnet-end*  \| **all** }]]

【缺省情况】

VLAN没有与任何IP子网或IP地址关联。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-subnet-index*]：IP子网索引值，取值范围为0～65535。子网索引可以由用户指定，也可由系统根据IP子网或IP地址与VLAN关联的先后顺序自动编号产生。

**[ip ***ip-address * *mask* ]：作为子网VLAN划分依据的源IP地址或网络地址，*ip-address*表示源IP地址或网络地址，采用点分十进制格式；*mask*表示子网掩码，采用点分十进制格式，缺省值为255.255.255.0。

**[to*** ip-subnet-end*]：用来确定IP子网索引的范围。其中*ip-subnet-end*表示IP子网索引的终止值，取值范围为0～65535，其值必须大于或等于*ip-subnet-index*的值。

**[all**]：取消VLAN与所有IP子网或IP地址的关联。

【使用指导】

VLAN关联的IP网段或IP地址不允许是组播网段或组播地址。

【举例】

\# 将VLAN 3配置为基于IP子网的VLAN，与192.168.1.0/24网段进行关联，使得源地址为该网段的报文可以在VLAN 3中传送。

\<Sysname\> system-view

Sysname vlan 3

Sysname-vlan3 ip-subnet-vlan ip 192.168.1.0 255.255.255.0

【相关命令】

·**display protocol-vlan interface**

·**display protocol-vlan vlan**

·**port hybrid protocol-vlan**

**VLAN \-- 基于IP子网的VLAN配置命令 \-- port hybrid ip-subnet-vlan**

------------------------------------------------------------------------

**[port hybrid ip-subnet-vlan**]命令用来配置当前端口与子网VLAN关联。

**[undo** **port hybrid ip-subnet-vlan**]命令用于取消当前端口与子网VLAN的关联。

【命令】

**[port hybrid ip-subnet-vlan** **vlan** *vlan-id*]

**[undo**[ **port hybrid ip-subnet-vlan** { **vlan** *vlan-id* \| **all** }]]

【缺省情况】

端口没有与任何子网VLAN关联。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan*** vlan*-*id*]：VLAN的编号，取值范围为1～4094。

**[all**]：所有VLAN。

【使用指导】

执行本命令时，需保证当前端口的链路类型为Hybrid，并允许子网VLAN通过，且子网VLAN下存在与IP子网或IP地址关联的配置，该命令才实际生效。

【举例】

\# 将端口GigabitEthernet1/0/1与子网VLAN 3关联。

\<Sysname\> system-view

Sysname vlan 3

Sysname-vlan3 ip-subnet-vlan ip 192.168.1.0 255.255.255.0

Sysname-vlan3 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type hybrid

Sysname-GigabitEthernet1/0/1 port hybrid vlan 3 untagged

Sysname-GigabitEthernet1/0/1 port hybrid ip-subnet-vlan vlan 3

\# 将二层聚合接口1与子网VLAN 3关联。

\<Sysname\> system-view

Sysname vlan 3

Sysname-vlan3 ip-subnet-vlan ip 192.168.1.0 255.255.255.0

Sysname-vlan3 quit

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 port link-type hybrid

Sysname-Bridge-Aggregation1 port hybrid vlan 3 untagged

Sysname-Bridge-Aggregation1 port hybrid ip-subnet-vlan vlan 3

【相关命令】

·**display ip-subnet-vlan interface**

·**display ip-subnet-vlan vlan**

·**ip-subnet-vlan**

**VLAN \-- 基于协议的VLAN配置命令 \-- display protocol-vlan interface**

------------------------------------------------------------------------

**[display protocol-vlan interface**]命令用于显示端口关联的协议VLAN的信息。

【命令】

**[display protocol-vlan interface** { *interface-type interface-number1* [ **to** *interface-type interface-number2*  \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number1*]：端口的类型和编号。

*[interface-type interface-number1* **to** *interface-type interface-number2*]：端口的类型和范围。

**[all**]：显示所有端口关联的协议VLAN的信息。

【举例】

\# 显示端口GigabitEthernet1/0/1关联的协议VLAN的信息。

\<Sysname\> display protocol-vlan interface gigabitethernet 1/0/1

 Interface: GigabitEthernet1/0/1

  VLAN ID  Protocol index  Protocol type             Status

  2        0               IPv6                      Active

  2        1               N/A                       Inactive

  4094     65535           IPv4                      Inactive

表1-7 display protocol-vlan interface命令显示信息描述表

字段

描述

VLAN ID

协议VLAN的编号

Protocol index

协议模板索引号

Protocol type

该协议模板指定的协议类型，N/A表示该协议模板未指定协议类型

Status

该协议VLAN在端口的生效情况：

·Active：表示生效

·Inactive：表示未生效

【相关命令】

·**display protocol-vlan vlan**

·**port hybrid protocol-vlan**

·**protocol-vlan**

**VLAN \-- 基于协议的VLAN配置命令 \-- display protocol-vlan vlan**

------------------------------------------------------------------------

**[display protocol-vlan vlan**]命令用于显示指定的或所有协议VLAN的信息。

【命令】

**[display protocol-vlan vlan****[-*id1* [ **to** *vlan*-*id2*  *\|* **all** }]]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vlan*-*id1*]：显示指定的协议VLAN的信息，*vlan*-*id1*表示VLAN的编号，取值范围为1～4094。

*[vlan*-*id1* **to** *vlan*-*id2*]：显示指定VLAN范围内的协议VLAN的信息。*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值。

**[all**]：显示所有协议VLAN的信息。

【举例】

\# 显示所有协议VLAN的信息。

\<Sysname\> display protocol-vlan vlan all

 VLAN ID: 2

  Protocol index  Protocol type

  0               IPv4

  65535           IPv6

 VLAN ID: 3

  Protocol index  Protocol type

  0               IPv4

  65535           LLC DSAP 0x11 SSAP 0x22

表1-8 display protocol-vlan vlan命令显示信息描述表

字段

描述

VLAN ID

协议VLAN的编号

Protocol index

协议模板索引号

Protocol type

该协议模板所指定的协议类型或封装格式

【相关命令】

·**display protocol-vlan interface**

·**port hybrid protocol-vlan**

·**protocol-vlan**

**VLAN \-- 基于协议的VLAN配置命令 \-- port hybrid protocol-vlan**

------------------------------------------------------------------------

**[port hybrid protocol-vlan**]命令用来配置当前端口与协议VLAN关联。

**[undo** **port hybrid protocol-vlan**]命令用于取消当前端口与协议VLAN的关联。

【命令】

**[port hybrid protocol-vlan** **vlan** *vlan-id* { *protocol-index* [ **to** *protocol-end*  \| **all** }]]

**[undo hybrid protocol-vlan** { **vlan** *vlan-id* { *protocol-index* [ **to** *protocol-end*  \| **all** } \| **all** }]]

【缺省情况】

端口没有与任何协议VLAN关联。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan** *vlan*-*id*]：VLAN的编号，取值范围为1～4094。

*[protocol-index*]：协议模板索引，取值范围为0～65535

**[to**]：协议模板索引的范围。

*[protocol-end*]：协议模板索引终止值，取值范围为0～65535，其值必须大于或等于*protocol-index*的值。

**[all**]：所有协议模板。

【使用指导】

需要注意的是：

·执行本命令时，需确保当前端口的链路类型为Hybrid，并允许协议VLAN通过，且协议VLAN下存在与协议模板关联的配置，本命令才实际生效。

·在执行**undo** **port hybrid protocol-vlan**命令时，如果同时指定*vlan-id*和**all**，则表示取消当前端口与指定VLAN下绑定的所有协议模板的关联；如果仅指定**all**，则表示取消当前端口与所有VLAN下绑定的所有协议模板的关联。

【举例】

\# 配置端口GigabitEthernet1/0/1与协议VLAN 2中的协议模板1关联。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 protocol-vlan 1 ipv4

Sysname-vlan2 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-type hybrid

Sysname-GigabitEthernet1/0/1 port hybrid vlan 2 untagged

Sysname-GigabitEthernet1/0/1 port hybrid protocol-vlan vlan 2 1

\# 配置二层聚合接口1与协议VLAN 2中的协议模板1关联。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 protocol-vlan 1 ipv4

Sysname-vlan2 quit

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 port link-type hybrid

Sysname-Bridge-Aggregation1 port hybrid vlan 2 untagged

Sysname-Bridge-Aggregation1 port hybrid protocol-vlan vlan 2 1

**VLAN \-- 基于协议的VLAN配置命令 \-- protocol-vlan**

------------------------------------------------------------------------

**[protocol-vlan**]命令用来配置当前VLAN与指定的协议模板关联。

**[undo protocol-vlan**]命令用于取消当前VLAN与协议模板的关联。

【命令】

**[protocol-vlan** [ *protocol-index*  { **at** \| **ipv4** \| **ipv6** \| **ipx** { **ethernetii** *\|* **llc** \| **raw** *\|* **snap** } \| **mode** { **ethernetii** **etype** *etype-id* \| **llc** { **dsap** *dsap-id*  **ssap** *ssap-id*  \| **ssap** *ssap-id* } \| **snap** **etype** *etype-id* } }]]

**[undo protocol-vlan** { *protocol-index* [ **to** *protocol-end*  \| **all** }]]

【缺省情况】

VLAN没有与任何协议模板关联。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[at**]：基于AT（AppleTalk，Apple计算机网络协议）协议的VLAN。

**[ipv4**]：基于IPv4协议的VLAN。

**[ipv6**]：基于IPv6协议的VLAN。

**[ipx**]：基于IPX协议的VLAN，可包括**ethernetii**、**llc**、**raw**和**snap**四种封装类型。

**[mode**]：配置自定义协议模板，可包括**ethernetii**、**llc**和**snap**三种封装类型。

**[ethernetii** **etype** *etype-id*]：匹配Ethernet II封装格式及相应的协议类型值。其中，*etype-id*表示入报文的协议类型值，取值范围为0x0600～0xFFFF（不包括0x0800、0x809B、0x8137和0x86DD）。

**[llc**]：匹配LLC封装格式。

**[dsap ***dsap-id*]：目的服务接入点，取值范围为0x00～0xFF。

**[ssap ***ssap-id*]：源服务接入点，取值范围为0x00～0xFF。

**[snap** **etype** *etype-id*]：匹配SNAP封装格式及相应的协议类型值。其中，*etype-id*表示入报文的以太网类型，取值范围为0x0600～0xFFFF（不包括0x8137）。

*[protocol-index*]：协议索引，用来标识与当前VLAN绑定的协议模版，取值范围为0～65535。如果不指定该参数，则系统会自动分配一个索引值。

**[to*** protocol-end*]：用来确定协议索引的范围。其中*protocol-end*表示协议索引终止值，取值范围为0～65535，其值必须大于或等于*protocol-index*的值。

*[protocol-end*]：协议索引终止值，取值范围为0～65535，必须大于等于*protocol-index*。

**[all**]：与当前VLAN绑定的所有协议。

【使用指导】

需要注意的是：

·由于IPv4协议与ARP协议关系密切，建议用户将IPv4协议和ARP协议绑定到同一VLAN，并且关联到相同的端口，避免因ARP报文与IPv4报文未划分到同一VLAN，而造成无法正常通信的情况。

·使用**mode ethernetii etype**关键字进行配置时，不允许将*etype-id*的值配置为0x0800、0x809B、0x8137或0x86DD，因为上述取值分别与IPv4、AppleTalk、IPX和IPv6协议模板相同。

·使用**mode llc**关键字进行配置时，*dsap-id*和*ssap-id*的值不允许同时为0xE0（代表IPX报文的LLC封装格式）、0xFF（代表IPX报文的raw封装格式）、0xAA（代表SNAP封装格式）；如果只配置了*dsap-id*和*ssap-id*中的一个，系统会将另一参数的值自动配置为0xAA。

·使用**mode snap etype**关键字进行配置时，不允许将*etype-id*的值配置为0x8137，因为该值与IPX协议协议模板相同。当*etype-id*的值取0x0800、0x809B或0x86DD时，其对应的协议模板分别为IPv4、AppleTalk和IPv6。

【举例】

\# 将IPv4报文和采用Ethernet II封装格式的ARP报文（ARP协议的协议代码为0x0806）划分到VLAN 3中传输。

\<Sysname\> system-view

Sysname vlan 3

Sysname-vlan3 protocol-vlan 1 ipv4

Sysname-vlan3 protocol-vlan 2 mode ethernetii etype 0806

【相关命令】

·**display protocol-vlan interface**

·**display protocol-vlan vlan**

·**port protocol-vlan**

**VLAN \-- VLAN组配置命令 \-- display vlan-group**

------------------------------------------------------------------------

**[display vlan-group**]命令用来显示创建的VLAN组及其VLAN成员列表。

【命令】

**[display vlan-group ** *group-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-name*]：VLAN组的名称，为1～31个字符的字符串，区分大小写，首字符必须为字母。若不指定该参数，则表示显示所有VLAN组的信息。

【举例】

\# 显示指定VLAN组test001的信息。

\<Sysname\> display vlan-group test001

VLAN group: test001

     VLAN list: 2-4 100 200

\# 显示所有VLAN组的信息。

\<Sysname\> display vlan-group

VLAN group: test001

     VLAN list: 2-4 100 200

VLAN group: rnd

     VLAN list: Null

表1-9 display vlan-group命令显示信息描述表

字段

描述

VLAN group

VLAN组名称

VLAN list

对应的该VLAN组内的VLAN列表

【相关命令】

·**vlan-group**

·**vlan-list**

**VLAN \-- VLAN组配置命令 \-- vlan-group**

------------------------------------------------------------------------

**[vlan-group**]命令用来创建一个VLAN组，并进入VLAN组视图。

**[undo vlan-group**]命令用来删除指定的VLAN组。

【命令】

**[vlan-group** *group-name*]

**[undo** **vlan-group** *group-name*]

【缺省情况】

不存在任何VLAN组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：VLAN组的名称，为1～31个字符的字符串，区分大小写，首字符必须为字母。

【使用指导】

·VLAN组是一组VLAN的集合。VLAN组内可以添加多个VLAN列表。

·认证服务器可以通过下发VLAN组名的方式为通过认证的802.1X用户下发一组授权VLAN。

·无线AC可以通过使用VLAN组，依次将其VLAN成员分配给上线的各客户端，使各客户端均匀分布在各VLAN。有关该配置的详细介绍，请参见"WLAN配置指导"中的"WLAN接入"。

【举例】

\# 创建一个VLAN组，名称为test001，并进入VLAN组视图。

\<Sysname\> system-view

Sysname vlan-group test001

Sysname-vlan-group-test001

【相关命令】

·**vlan-list**

**VLAN \-- VLAN组配置命令 \-- vlan-list**

------------------------------------------------------------------------

**[vlan-list**]命令用来在当前VLAN组内添加VLAN成员。

**[undo vlan-list**]命令用来从当前VLAN组内删除VLAN成员。

【命令】

**[vlan-list ***vlan-id-list*]

**[undo vlan-list ***vlan-id-list*]

【缺省情况】

当前VLAN组中不存在任何VLAN列表。

【视图】

VLAN组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094（取值范围与设备的型号有关，请以设备的实际情况为准），*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

【举例】

\# 向VLAN组test001内添加VLAN成员：VLAN 2～VLAN 4、VLAN 100、VLAN 200。

\<Sysname\> system-view

Sysname vlan-group test001

Sysname-vlan-group-test001 vlan-list 2 to 4 100 200

【相关命令】

·**vlan-group**

\

**Super VLAN \-- Super VLAN配置命令 \-- display supervlan**

------------------------------------------------------------------------

**[display supervlan**]命令用来显示Super VLAN及其关联的Sub VLAN的信息。

【命令】

**[display supervlan ** *supervlan-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[supervlan-id*]：Super VLAN的编号，取值范围为1～4094。如果未指定该参数，则显示设备上所有的Super VLAN及其关联的Sub VLAN的信息。

【举例】

\# 显示Super VLAN 2及其关联的Sub VLAN的信息。

\<Sysname\> display supervlan 2

 Super VLAN ID: 2

 Sub-VLAN ID: 3-5

 VLAN ID: 2

 VLAN type: Static

 It is a super VLAN.

 Route interface: Configured

 IPv4 address: 10.153.17.41

 IPv4 subnet mask: 255.255.252.0

 IPv6 global unicast addresses:

   2001::1, subnet is 2001::/64 [TENTATIVE]

 Description: VLAN 0002

 Name: VLAN 0002

 Tagged ports:   None

 Untagged ports: None

 VLAN ID: 3

 VLAN type: Static

 It is a sub-VLAN.

 Route interface: Configured

 IPv4 address: 10.153.17.41

 IPv4 subnet mask: 255.255.252.0

 IPv6 global unicast addresses:

   2001::1, subnet is 2001::/64 [TENTATIVE]

 Description: VLAN 0003

 Name: VLAN 0003

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/3

 VLAN ID: 4

 VLAN type: Static

 It is a sub-VLAN.

 Route interface: Configured

 IPv4 address: 10.153.17.41

 IPv4 subnet mask: 255.255.252.0

 IPv6 global unicast addresses:

   2001::1, subnet is 2001::/64 [TENTATIVE]

 Description: VLAN 0004

 Name: VLAN 0004

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/4

表2-1 display supervlan命令显示信息描述表

字段

描述

Super VLAN ID

Super VLAN的编号

Sub-VLAN ID

Sub VLAN的编号

VLAN ID

VLAN编号

VLAN type

VLAN类型：

·Dynamic：动态VLAN

·Static：静态VLAN

It is a super VLAN

当前VLAN是Super VLAN

It is a sub-VLAN

当前VLAN是Sub VLAN

Route interface

设备上是否创建了对应的VLAN接口：

·Configured：已创建

·Not configured：未创建

IPv4 address

VLAN接口的主用IPv4地址（如果VLAN接口没有配置IPv4地址，则不显示该字段），如果VLAN接口上还配置了从IPv4地址，可以使用**display interface vlan-interface**或者在VLAN接口视图下使用**display this**命令查看

IPv4 subnet mask

VLAN接口的主用IPv4地址的子网掩码（如果VLAN接口没有配置IPv4地址，则不显示该字段）

IPv6 global unicast addresses

VLAN接口上配置的全球单播IPv6地址（如果VLAN接口没有配置IPv6地址，则不显示该字段）

可能的IPv6地址状态及含义如下：

· TENTATIVE：该状态为地址初始化状态，此时该地址可能正在进行DAD检测或准备进行DAD检测，处于该状态的地址不能作为报文的源地址或者目的地址

· DUPLICATE：该状态表明地址DAD检测已经结束，由于该地址在链路上不唯一，因此不能使用

· PREFERRED：该状态表明地址处于首选生命期以内。该状态的地址可以作为报文的源地址或者目的地址。为该状态时，不显示地址的状态标识

· DEPRECATED：该状态表明地址超过首选生命期，但是在有效生命期以内。该状态地址有效，但不应作为新建连接报文的源地址，目的地址是该地址的报文还可以被正常处理

Description

VLAN的描述信息

Name

VLAN的名称

Tagged ports

该VLAN报文从哪些端口发送需要携带VLAN Tag

Untagged ports

该VLAN报文从哪些端口发送时不需要携带VLAN Tag

【相关命令】

·**subvlan**

·**supervlan**

**Super VLAN \-- Super VLAN配置命令 \-- subvlan**

------------------------------------------------------------------------

**[subvlan**]命令用来建立Super VLAN和Sub VLAN的映射关系。

**[undo subvlan**]命令用来解除Super VLAN和Sub VLAN的映射关系。

【命令】

**[subvlan ***vlan-id-list*]

**[undo subvlan ** *vlan-id-list* ]

【缺省情况】

未建立Super VLAN和Sub VLAN的映射关系。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：Sub VLAN列表，表示方式为*vlan-id-list* *=* { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中，*vlan-id*表示Sub VLAN的VLAN ID，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以重复输入10次。

【使用指导】

·建立Super VLAN和Sub VLAN的映射关系前，指定的Sub VLAN必须已经创建。

·在建立了Super VLAN和Sub VLAN的映射关系后，仍可以向Sub VLAN中添加和删除接口。

·使用**undo subvlan**命令时，如果不指定*vlan-id-list*，则解除当前Super VLAN与所有Sub VLAN的映射关系；如果指定*vlan-id-list*，则解除当前Super VLAN与指定Sub VLAN的映射关系。

【举例】

\# 建立Super VLAN 10和Sub VLAN 3、4、5的映射关系。

\<Sysname\> system-view

Sysname vlan 3 to 5

Sysname vlan 10

Sysname-vlan10 supervlan

Sysname-vlan10 subvlan 3 to 5

【相关命令】

·**display supervlan**

·**supervlan**

**Super VLAN \-- Super VLAN配置命令 \-- supervlan**

------------------------------------------------------------------------

**[supervlan**]命令用来配置当前VLAN的类型为Super VLAN。

**[undo supervlan**]命令用来恢复缺省情况。

【命令】

**[supervlan**]

**[undo supervlan**]

【缺省情况】

VLAN类型不为Super VLAN。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·如果某个VLAN被指定为Super VLAN，则该VLAN不建议被指定为某个端口的Guest VLAN/Auth-Fail VLAN/Critical VLAN；同样，如果某个VLAN被指定为某个端口的Guest VLAN/Auth-Fail VLAN/Critical VLAN，则该VLAN不建议被指定为Super VLAN。Guest VLAN/Auth-Fail VLAN/Critical VLAN的相关内容请参见"安全配置指导"中的"802.1X"。

·在Super VLAN对应的VLAN接口下配置VRRP功能后，会对网络性能造成影响，建议不要这样配置。

·在Super VLAN下可以配置二层组播功能，但是由于Super VLAN中没有物理端口，该配置将不会生效。

【举例】

\# 配置VLAN 2为Super VLAN。

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 supervlan

【相关命令】

·**display supervlan**

·**subvlan**

\

**Private VLAN \-- Private VLAN配置命令 \-- display private-vlan**

------------------------------------------------------------------------

**[display private-vlan**]命令用来显示Primary VLAN和其包含的Secondary VLAN的信息。

【命令】

**[display private-vlan ** *primary-vlan-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[primary-vlan-id*]：Primary VLAN的编号，取值范围为1～4094。如果未指定该参数，则显示所有Primary VLAN和其对应的Secondary VLAN的映射信息。

【举例】

\# 显示所有Primary VLAN和其包含的Secondary VLAN的信息。

\<Sysname\> display private-vlan

 Primary VLAN ID: 2

 Secondary VLAN ID: 3-4

 VLAN ID: 2

 VLAN type: Static

 Private VLAN type: Primary

 Route interface: Configured

 IPv4 address: 1.1.1.1

 IPv4 subnet mask: 255.255.255.0

 IPv6 global unicast addresses:

   2001::1, subnet is 2001::/64 [TENTATIVE]

 Description: VLAN 0002

 Name: VLAN 0002

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/2

    GigabitEthernet1/0/3

    GigabitEthernet1/0/4

 VLAN ID: 3

 VLAN type: Static

 Private VLAN type: Secondary

 Route interface: Not configured

 Description: VLAN 0003

 Name: VLAN 0003

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/2

    GigabitEthernet1/0/3

 VLAN ID: 4

 VLAN type: Static

 Private VLAN type: Secondary

 Route interface: Not configured

 Description: VLAN 0004

 Name: VLAN 0004

 Tagged ports:   None

 Untagged ports:

    GigabitEthernet1/0/2

    GigabitEthernet1/0/4

表3-1 display private-vlan命令显示信息描述表

字段

描述

Primary VLAN ID

Primary VLAN的编号

Secondary VLAN ID

Secondary VLAN的编号

VLAN ID

VLAN编号

VLAN type

VLAN类型：

·Dynamic：动态VLAN

·Static：静态VLAN

Private VLAN type

Private VLAN类型：

·Primary：表示Primary VLAN

·Secondary：表示Secondary VLAN

·Isolated secondary：表示配置了各端口二层隔离的Secondary VLAN

Route interface

设备上是否创建了对应的VLAN接口：

·Configured：已创建

·Not configured：未创建

IPv4 address

VLAN接口的主用IPv4地址（如果VLAN接口没有配置IPv4地址，则不显示该字段），如果VLAN接口上还配置了从IPv4地址，可以使用**display interface vlan-interface**或者在VLAN接口视图下使用**display this**命令查看

IPv4 subnet mask

VLAN接口的主用IPv4地址的子网掩码（如果VLAN接口没有配置IPv4地址，则不显示该字段）

IPv6 global unicast addresses

VLAN接口上配置的全球单播IPv6地址（如果VLAN接口没有配置IPv6地址，则不显示该字段）

可能的IPv6地址状态及含义如下：

· TENTATIVE：该状态为地址初始化状态，此时该地址可能正在进行DAD检测或准备进行DAD检测，处于该状态的地址不能作为报文的源地址或者目的地址

· DUPLICATE：该状态表明地址DAD检测已经结束，由于该地址在链路上不唯一，因此不能使用

· PREFERRED：该状态表明地址处于首选生命期以内。该状态的地址可以作为报文的源地址或者目的地址。为该状态时，不显示地址的状态标识

· DEPRECATED：该状态表明地址超过首选生命期，但是在有效生命期以内。该状态地址有效，但不应作为新建连接报文的源地址，目的地址是该地址的报文还可以被正常处理

Description

VLAN的描述信息

Name

VLAN的名称

Tagged ports

该VLAN报文从哪些端口发送需要携带VLAN Tag

Untagged ports

该VLAN报文从哪些端口发送时不需要携带VLAN Tag

【相关命令】

·**private-vla****n **（VLAN view）

·**private-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- port private-vlan host**

------------------------------------------------------------------------

**[port private-vlan host**]命令用来配置端口工作在host模式。

**[undo port private-vlan**]命令用来恢复缺省情况。

【命令】

**[port private-vlan host**]

**[undo port private-vlan**]

【缺省情况】

端口不工作在host模式。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

端口工作在host模式时，若端口已经加入了Secondary VLAN，则端口也会同步加入和Secondary VLAN有映射关系的Primary VLAN。

**[undo port private-vlan**]命令恢复缺省情况时，端口的VLAN属性（包括端口加入VLAN以及端口的链路类型、端口缺省VLAN）不做改变。

需要注意的是：

·在执行**port private-vlan host**命令时，当端口同步加入Primary VLAN，若此前端口的链路类型为Access类型，则会配置端口的链路类型为Hybrid类型，缺省VLAN为端口加入的Secondary VLAN；若此前端口的链路类型为Trunk/Hybrid类型，则端口的链路类型及缺省VLAN不做改变。

·在执行**port private-vlan host**命令时，当端口的链路类型最终为Hybrid类型，端口同步加入Primary VLAN时，若此前端口有以Tagged/Untagged方式加入Primary VLAN的配置，则保持原有配置；否则端口会以Untagged方式加入Primary VLAN。

·可以在执行完**port private-vlan host**命令后，再配置端口加入Secondary VLAN，此时，该命令的功能依然生效。

·**port private-vlan host**命令与**port private-vlan** **trunk promiscuous**及**port private-vlan trunk secondary**命令互斥。

【举例】

VLAN 20的类型为Secondary VLAN，且VLAN 20和Primary VLAN 2关联。配置链路类型为Access的端口GigabitEthernet1/0/1工作在host模式，将端口GigabitEthernet1/0/1加入VLAN 20。

\# 配置链路类型为Access的端口GigabitEthernet1/0/1工作在host模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port private-vlan host

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port private-vlan host

\#

return

\# 将端口GigabitEthernet1/0/1加入VLAN 20。

Sysname-GigabitEthernet1/0/1 port access vlan 20

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出当端口GigabitEthernet1/0/1工作在host模式，且加入Secondary VLAN 20时，该端口会同步加入关联的Primary VLAN 2，同时修改链路类型及缺省VLAN。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port private-vlan host

 port link-type hybrid

 undo port hybrid vlan 1

 port hybrid vlan 2 20 untagged

 port hybrid pvid vlan 20

\#

return

【相关命令】

·**port private-vlan promiscuous**

·**port private-vlan trunk promiscuous**

·**port private-vlan trunk secondary**

·**private-vlan******（VLAN view）

·**private-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- port private-vlan promiscuous**

------------------------------------------------------------------------

**[port private-vlan** **promiscuous**]命令用来配置端口在指定VLAN中工作在promiscuous模式。

**[undo port private-vlan**]命令用来恢复缺省情况。

【命令】

**[port private-vlan** *vlan-id* **promiscuous**]

**[undo port private-vlan**]

【缺省情况】

端口在指定VLAN中不工作在promiscuous模式。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：VLAN的编号，取值范围为1～4094。其中，VLAN 1虽然在取值范围中，但不能配置。

【使用指导】

**[port private-vlan** **promiscuous**]命令同时会将端口加入指定VLAN。此时若指定VLAN的类型为Primary VLAN，且存在和指定VLAN有映射关系的Secondary VLAN，则端口也会同步加入这些Secondary VLAN。

**[undo port private-vlan**]命令恢复缺省情况时，端口的VLAN属性（包括端口加入Secondary VLAN以及端口的链路类型、缺省VLAN的配置）不做改变。

需要注意的是：

·在执行**port private-vlan** **promiscuous**命令时，若此前端口的链路类型为Access类型，则会配置端口的链路类型为Hybrid类型，缺省VLAN为指定VLAN；若此前端口的链路类型为Trunk/Hybrid类型，则端口的链路类型及缺省VLAN不做改变。

·在执行**port private-vlan** **promiscuous**命令时，当端口的链路类型最终为Hybrid类型，端口加入对应VLAN（包括指定VLAN及同步加入的Secondary VLAN）时，若端口此前存在以Tagged/Untagged方式加入某些对应VLAN的配置，则在保持原有配置的基础上，端口会以Untagged方式加入其他对应VLAN；否则端口会以Untagged方式加入所有对应VLAN。即自动产生的以Untagged方式加入VLAN的配置不会覆盖原有以Tagged/Untagged加入VLAN的配置。

·在执行**port private-vlan** **promiscuous**命令时，若端口已配置promiscuous模式，则系统会自动先执行**undo port private-vlan**命令，再执行**port private-vlan** **promiscuous**命令。

·在执行**undo port private-vlan**命令时，若端口已配置在某VLAN中工作在promiscuous模式，则取消端口加入该VLAN的配置。

·可以在执行完**port private-vlan** **promiscuous**命令后，再配置指定VLAN的类型为Primary VLAN，此时，该命令的功能依然生效。

·**port private-vlan promiscuous**命令与**port private-vlan trunk promiscuous**及**port private-vlan trunk secondary**命令互斥。

【举例】

VLAN 2的类型为Primary VLAN，且VLAN 2和Secondary VLAN 20关联。配置链路类型为Access的端口GigabitEthernet1/0/1在VLAN 2中工作在promiscuous模式，然后取消该配置。

\# 配置链路类型为Access的端口GigabitEthernet1/0/1在VLAN 2中工作在promiscuous模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

\#

return

Sysname-GigabitEthernet1/0/1 port private-vlan 2 promiscuous

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出当该端口在VLAN 2中工作在promiscuous模式时，该端口会加入Primary VLAN 2及关联的Secondary VLAN 20，同时修改端口的链路类型及缺省VLAN。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 port private-vlan 2 promiscuous

 undo port hybrid vlan 1

 port hybrid vlan 2 20 untagged

 port hybrid pvid vlan 2

\#

return

\# 取消端口GigabitEthernet1/0/1的promiscuous模式配置。

Sysname-GigabitEthernet1/0/1 undo port private-vlan

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出该端口退出Primary VLAN 2，但该端口的VLAN属性（包括端口加入Secondary VLAN以及端口的链路类型、缺省VLAN的配置）不做改变。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 undo port hybrid vlan 1

 port hybrid vlan 20 untagged

 port hybrid pvid vlan 2

\#

return

【相关命令】

·**port private-vlan host**

·**port private-vlan trunk promiscuous**

·**port private-vlan trunk secondary**

·**private-vlan******（VLAN view）

·**private-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- port private-vlan trunk promiscuous**

------------------------------------------------------------------------

**[port private-vlan trunk promiscuous**]命令用来配置端口在指定VLAN中工作在trunk promiscuous模式。

**[undo port private-vlan trunk promiscuous**]命令用来配置端口在指定VLAN退出trunk promiscuous模式。

【命令】

**[port private-vlan ***vlan-id-list* **trunk promiscuous**]

**[undo port private-vlan** *vlan-id-list* **trunk promiscuous**]

【缺省情况】

端口在指定VLAN中不工作在trunk promiscuous模式。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，Primary VLAN的范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。其中，系统缺省VLAN（VLAN 1）虽然在取值范围中，但不能配置。

【使用指导】

**[port private-vlan** **trunk promiscuous**]命令同时会将端口加入指定VLAN。此时若指定VLAN的类型为Primary VLAN，且存在和指定VLAN有映射关系的Secondary VLAN，则端口也会同步加入这些Secondary VLAN。

**[undo port private-vlan****trunk promiscuous**]命令用来配置端口在指定VLAN中退出trunk promiscuous模式，但端口的VLAN属性（包括端口加入Secondary VLAN以及端口的链路类型、缺省VLAN的配置）不做改变。

需要注意的是：

·在执行**port private-vlan** **trunk promiscuous**命令时，若此前端口的链路类型为Access类型，则会配置端口的链路类型为Hybrid类型，缺省VLAN不做改变；若此前端口的链路类型为Trunk/Hybrid类型，则端口的链路类型及缺省VLAN不做改变。

·在执行**port private-vlan** **trunk promiscuous**命令时，当端口的链路类型最终为Hybrid类型，端口加入对应VLAN（包括指定VLAN及同步加入的Secondary VLAN）时，若端口此前存在以Tagged/Untagged方式加入某些对应VLAN的配置，则在保持原有配置的基础上，端口会以Tagged方式加入其他对应VLAN；否则端口会以Tagged方式加入所有对应VLAN。即自动产生的以Tagged方式加入VLAN的配置不会覆盖原有以Tagged/Untagged加入VLAN的配置。

·在执行**undo port private-vlan** **trunk promiscuous**命令时，若已配置端口在*vlan-id-list*中工作在trunk promiscuous模式，则取消端口加入*vlan-id-list*的配置。

·可以在执行完**port private-vlan** **trunk promiscuous**命令后，再配置指定VLAN的类型为Primary VLAN，此时，该命令的功能依然生效。

·**port private-vlan trunk promiscuous**命令与**port private-vlan******promiscuous**、**port private-vlan trunk secondary**及**port private-vlan host**命令互斥。

![说明](VLAN命令.files/image002.png)

**[port private-vlan trunk promiscuous**]命令适用于需要多个Primary VLAN通过上行端口的情况，配置该命令后多个Primary VLAN携带Tag通过上行端口。**port private-vlan******promiscuous**适用于只有一个Primary VLAN通过上行端口的情况，配置该命令后Primary VLAN不带Tag通过上行端口。

【举例】

VLAN 2、3的类型为Primary VLAN，且VLAN 2和Secondary VLAN 20关联，VLAN 3和Secondary VLAN 30关联。配置链路类型为Access的端口GigabitEthernet1/0/1在VLAN 2、3中工作在trunk promiscuous模式，然后取消该配置。

\# 配置链路类型为Access的端口GigabitEthernet1/0/1在VLAN 2、3中工作在trunk promiscuous模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

\#

return

Sysname-GigabitEthernet1/0/1 port private-vlan 2 3 trunk promiscuous

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出当该端口在VLAN 2、3中工作在trunk promiscuous模式时，该端口会加入Primary VLAN 2、3及关联的Secondary VLAN 20、30，同时修改端口的链路类型。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 port private-vlan 2 3 trunk promiscuous

 port hybrid vlan 2 3 20 30 tagged

 port hybrid vlan 1 untagged

\#

return

\# 取消端口GigabitEthernet1/0/1在VLAN 2、3中的trunk promiscuous模式配置。

Sysname-GigabitEthernet1/0/1 undo port private-vlan 2 3 trunk promiscuous

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出该端口退出Primary VLAN 2、3，但该端口的VLAN属性（包括端口加入Secondary VLAN以及端口的链路类型、缺省VLAN的配置）不做改变。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 port hybrid vlan 20 30 tagged

 port hybrid vlan 1 untagged

\#

return

【相关命令】

·**port private-vlan host**

·**port private-vlan promiscuous**

·**port private-vlan trunk secondary**

·**private-vlan******（VLAN view）

·**private-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- port private-vlan trunk secondary**

------------------------------------------------------------------------

**[port private-vlan trunk secondary**]命令用来配置端口在指定VLAN中工作在trunk secondary模式。

**[undo port private-vlan trunk secondary**]命令用来配置端口在指定VLAN退出trunk secondary模式。

【命令】

**[port private-vlan** *vlan-id-list* **trunk secondary**]

**[undo port private-vlan** *vlan-id-list* **trunk secondary**]

【缺省情况】

端口在指定VLAN中不工作在trunk secondary模式。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，Secondary VLAN的范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。其中，系统缺省VLAN（VLAN 1）虽然在取值范围中，但不能配置。

【使用指导】

**[port private-vlan** **trunk secondary**]命令同时会将端口加入指定VLAN。此时若指定VLAN的类型为Secondary VLAN，且存在和指定VLAN有映射关系的Primary VLAN，则端口也会同步加入这些Primary VLAN。

**[undo port private-vlan****trunk secondary**]命令将指定VLAN退出trunk secondary模式，但端口的VLAN关系（包括端口加入Primary VLAN以及端口的链路类型、缺省VLAN的配置）不做改变。

需要注意的是：

·工作在trunk secondary模式的端口，对于一个Primary VLAN对应的Secondary VLAN，只能加入其中的一个，但可以分别加入多个Primary VLAN对应的多个Secondary VLAN。

·在执行**port private-vlan trunk secondary**命令时，当端口同步加入Primary VLAN，若此前端口的链路类型为Access类型，则会配置端口的链路类型为Hybrid类型，缺省VLAN不做改变；若此前端口的链路类型为Trunk/Hybrid类型，则端口的链路类型及缺省VLAN不做改变。

·在执行**port private-vlan trunk secondary**命令时，当端口的链路类型最终为Hybrid类型，端口加入对应VLAN（包括指定VLAN及同步加入的Primary VLAN）时，若端口此前存在以Tagged/Untagged方式加入某些对应VLAN的配置，则在保持原有配置的基础上，端口会以Tagged方式加入其他对应VLAN；否则端口会以Tagged方式加入所有对应VLAN。即自动产生的以Tagged方式加入VLAN的配置不会覆盖原有以Tagged/Untagged加入VLAN的配置。

·在执行完**port private-vlan trunk secondary**命令后，再执行**undo port private-vlan trunk secondary**命令时，若端口的链路类型为Access类型，则端口加入指定VLAN的配置不做改变；若端口的链路类型为Trunk/Hybrid类型，则取消端口加入指定VLAN的配置。

·可以在执行完**port private-vlan trunk secondary**命令后，再建立指定VLAN与Primary VLAN的映射关系，此时，该命令的功能依然生效。

·在执行**port private-vlan trunk secondary**命令时，若其中*vlan-id-list*中部分VLAN不满足要求（比如指定VLAN不存在，指定VLAN的类型为除Secondary VLAN外的其他特殊类型VLAN，本端口已经在指定VLAN对应Primary VLAN下的其他Secondary VLAN中工作在trunk secondary模式等），则本命令只在其他满足要求的VLAN中生效。

·**port private-vlan trunk secondary**命令与**port private-vlan host**、**port private-vlan promiscuous**及**port private-vlan trunk promiscuous**命令互斥。

![说明](VLAN命令.files/image003.png)

**[port private-vlan trunk secondary**]命令适用于需要多个Secondary VLAN（分别对应不同的Primary VLAN）通过下行端口的情况，配置该命令后多个Secondary VLAN携带Tag通过下行端口。**port private-vlan host**命令适用于只有一个Secondary VLAN通过下行端口的情况，配置该命令后Secondary VLAN不带Tag通过下行端口。

【举例】

VLAN 2、3的类型为Primary VLAN，且VLAN 2和Secondary VLAN 20关联，VLAN 3和Secondary VLAN 30关联，配置VLAN 20、30在链路类型为Access的端口GigabitEthernet1/0/1工作在trunk secondary模式，然后取消该配置。

\# 配置链路类型为Access的端口GigabitEthernet1/0/1在VLAN 20、30中工作在trunk secondary模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

\#

return

Sysname-GigabitEthernet1/0/1 port private-vlan 20 30 trunk secondary

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出当该端口在VLAN 20、30中工作在trunk secondary模式时，该端口会加入Secondary VLAN 20、30及关联的Primary VLAN 2、3，同时修改链路类型。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 port hybrid vlan 2 3 20 30 tagged

 port hybrid vlan 1 untagged

 port private-vlan 20 30 trunk secondary

\#

return

\# 取消端口GigabitEthernet1/0/1在VLAN 20、30中的trunk secondary模式配置。

Sysname-GigabitEthernet1/0/1 undo port private-vlan 20 30 trunk secondary

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出该端口退出Secondary VLAN 20、30，但该端口的VLAN属性（包括端口加入Primary VLAN以及端口的链路类型、缺省VLAN的配置）不做改变。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 port hybrid vlan 2 3 tagged

 port hybrid vlan 1 untagged

\#

return

VLAN 10的类型不为Secondary VLAN。配置链路类型为Access的端口GigabitEthernet1/0/1在VLAN 10中工作在trunk secondary模式，然后取消该配置。

\# 配置链路类型为Access的端口GigabitEthernet1/0/1在VLAN 10中工作在trunk secondary模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

\#

return

Sysname-GigabitEthernet1/0/1 port private-vlan 10 trunk secondary

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出该端口在VLAN 10中工作在trunk secondary模式时，该端口会加入Secondary VLAN 10，同时修改链路类型。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 port hybrid vlan 10 tagged

 port hybrid vlan 1 untagged

 port private-vlan 10 trunk secondary

\#

return

\# 取消端口GigabitEthernet1/0/1在VLAN 10中的trunk secondary模式配置。

Sysname-GigabitEthernet1/0/1 undo port private-vlan 10 trunk secondary

\# 显示端口GigabitEthernet1/0/1当前配置，可以看出该端口退出VLAN 10，但该端口的VLAN属性（包括端口的链路类型、缺省VLAN的配置）不做改变。

Sysname-GigabitEthernet1/0/1 display this

\#

interface GigabitEthernet1/0/1

 port link-mode bridge

 port link-type hybrid

 port hybrid vlan 1 untagged

\#

return

【相关命令】

·**port private-vlan host**

·**port private-vlan promiscuous**

·**port private-vlan trunk promiscuous**

·**private-vlan******（VLAN view）

·**private-vlan isolated**

·**private-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- private-vlan （VLAN interface view）**

------------------------------------------------------------------------

**[private-vlan secondary**]命令用来配置当前Primary VLAN下指定的Secondary VLAN间三层互通。

**[undo private-vlan**]用来取消当前Primary VLAN下指定的或所有的Secondary VLAN间三层互通。

【命令】

**[private-vlan secondary ***vlan-id-list*]

**[undo private-vlan ** **secondary** *vlan-id-list* ]

【缺省情况】

Secondary VLAN间三层不互通。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，Secondary VLAN的范围。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

【使用指导】

·该命令只能在Primary VLAN对应的VLAN接口（Primary VLAN interface）视图下执行，且Secondary VLAN必须已经与该对应的Primary VLAN建立了映射关系，同时要求Secondary VLAN不能建立对应的VLAN接口。要使功能生效，还需要在该三层虚接口上配置IP地址和本地代理ARP/ND功能。

·没有配置三层互通的Secondary VLAN可以创建对应的VLAN接口，配置了三层互通的Secondary VLAN不能创建对应的VLAN接口。

·在同一Primary VLAN interface下多次执行本命令时，最终生效结果是多次配置的集合。

·在执行**undo private-vlan**命令时，如果不带参数**secondary** *vlan-id-list*，就解除所有Secondary VLAN间的三层互通；如果带有该参数，就解除指定的Secondary VLAN间的三层互通。

【举例】

配置Primary VLAN 2下的Secondary VLAN 3、4三层互通（GigabitEthernet1/0/2为上行端口，GigabitEthernet1/0/3、GigabitEthernet1/0/4为下行端口）。

\# 建立Primary VLAN 2和Secondary VLAN 3、4的映射关系。

\<Sysname\> system-view

Sysname vlan 3 to 4

Sysname vlan 2

Sysname-vlan2 private-vlan primary

Sysname-vlan2 private-vlan secondary 3 to 4

Sysname-vlan2 quit

\# 配置端口GigabitEthernet1/0/2在VLAN 2中工作在promiscuous模式。

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port private-vlan 2 promiscuous

Sysname-GigabitEthernet1/0/2 quit

\# 配置链路类型为Access的端口GigabitEthernet1/0/3在VLAN 3中工作在host模式，链路类型为Access的端口GigabitEthernet1/0/4在VLAN 4中工作在host模式。

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 port access vlan 3

Sysname-GigabitEthernet1/0/3 port private-vlan host

Sysname-GigabitEthernet1/0/3 quit

Sysname interface gigabitethernet 1/0/4

Sysname-GigabitEthernet1/0/4 port access vlan 4

Sysname-GigabitEthernet1/0/4 port private-vlan host

Sysname-GigabitEthernet1/0/4 quit

\# 配置Primary VLAN 2下的Secondary VLAN 3、4三层互通，同时配置Primary VLAN接口的IP地址及开启本地代理ARP功能。

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 private-vlan secondary 3 to 4

Sysname-Vlan-interface2 ip address 192.168.1.1 255.255.255.0

Sysname-Vlan-interface2 local-proxy-arp enable

【相关命令】

·**private-vlan******（VLAN view）

·**private-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- private-vlan （VLAN view）**

------------------------------------------------------------------------

**[private-vlan**]命令用来建立Primary VLAN和Secondary VLAN的映射关系。

**[undo private-vlan**]用来解除Primary VLAN和Secondary VLAN的映射关系。

【命令】

**[private-vlan secondary** *vlan-id-list*]

**[undo private-vlan ** **secondary** *vlan-id-list* ]

【缺省情况】

未建立Primary VLAN和Secondary VLAN的映射关系。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[secondary** *vlan-id-list*]：表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。其中，系统缺省VLAN（VLAN 1）虽然在取值范围中，但不能配置。

【使用指导】

·Primary VLAN可以与多个Secondary VLAN建立映射关系。在同一VLAN视图下多次执行**private-vlan**命令时，Primary VLAN对应的Secondary VLAN是多次配置的集合。

·在执行**private-vlan**命令时，若已经配置Primary VLAN，且设备上有端口工作在promiscuous模式、trunk promiscuous模式或host模式，则依据接口配置会触发配置同步。

·在执行**undo private-vlan**命令时，如果不带参数**secondary ***vlan-id-list*，就解除所有Secondary VLAN和对应Primary VLAN的映射关系；如果带有该参数，就解除参数指定的Secondary VLAN和对应Primary VLAN的映射关系。

【举例】

\# 建立Primary VLAN 2和Secondary VLAN 3、4的映射关系。

\<Sysname\> system-view

Sysname vlan 3 to 4

Sysname vlan 2

Sysname-vlan2 private-vlan primary

Sysname-vlan2 private-vlan secondary 3 to 4

【相关命令】

·**port private-vlan host**

·**port private-vlan promiscuous**

·**port private-vlan trunk promiscuous**

·**port private-vlan trunk secondary**

·**primary-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- private-vlan community**

------------------------------------------------------------------------

**[private-vlan community**]命令用来配置同一Secondary VLAN内各端口二层互通。

【命令】

**[private-vlan community**]

【缺省情况】

同一Secondary VLAN内的端口二层互通。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[private-vlan community**]命令实现的功能与**undo private-vlan isolated**命令相同。当用户通过**save**命令保存配置时，**private-vlan community**命令的配置不会被存入配置文件。

【举例】

配置Secondary VLAN 4内各端口二层互通（GigabitEthernet1/0/1工作为promiscuous模式，GigabitEthernet1/0/2和GigabitEthernet1/0/3工作在host模式）。完成下述配置后，Secondary VLAN 4内端口GigabitEthernet1/0/2和GigabitEthernet1/0/3二层互通。

\# 建立Primary VLAN 2和Secondary VLAN 4的映射关系。

\<Sysname\> system-view

Sysname vlan 4

Sysname-vlan4 quit

Sysname vlan 2

Sysname-vlan2 private-vlan primary

Sysname-vlan2 private-vlan secondary 4

Sysname-vlan2 quit

\# 配置端口GigabitEthernet1/0/1在VLAN 2中工作在promiscuous模式。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port private-vlan 2 promiscuous

Sysname-GigabitEthernet1/0/1 quit

\# 配置链路类型为Access的端口GigabitEthernet1/0/2和GigabitEthernet1/0/3在VLAN 4中工作在host模式。

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port access vlan 4

Sysname-GigabitEthernet1/0/2 port private-vlan host

Sysname-GigabitEthernet1/0/2 quit

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 port access vlan 4

Sysname-GigabitEthernet1/0/3 port private-vlan host

Sysname-GigabitEthernet1/0/3 quit

\# 配置Secondary VLAN 4内各端口二层互通。

Sysname vlan 4

Sysname-vlan4 private-vlan community

【相关命令】

·**private-vlan isolated**

**Private VLAN \-- Private VLAN配置命令 \-- private-vlan isolated**

------------------------------------------------------------------------

![说明](VLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[private-vlan isolated**]命令用来配置同一Secondary VLAN内各端口二层隔离，即配置该Secondary VLAN为隔离Secondary VLAN。

**[undo private-vlan isolated**]命令用来恢复缺省情况。

【命令】

**[private-vlan isolated**]

**[undo private-vlan isolated**]

【缺省情况】

同一Secondary VLAN内的端口能够二层互通。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·添加到该隔离Secondary VLAN的各下行端口二层隔离。

·当Primary VLAN与Secondary VLAN建立映射关系，并且下行端口配置为trunk secondary模式或host模式后，**private-vlan isolated**命令才生效。

·Secondary VLAN隔离与Primary VLAN、Super VLAN和Sub VLAN配置互斥。

【举例】

配置Secondary VLAN 4内各端口二层隔离（GigabitEthernet1/0/1工作在promiscuous模式，GigabitEthernet1/0/2及GigabitEthernet1/0/3工作在host模式）。完成下述配置后，Secondary VLAN 4内端口GigabitEthernet1/0/2和GigabitEthernet1/0/3二层隔离。

\# 建立Primary VLAN 2和Secondary VLAN 4的映射关系。

\<Sysname\> system-view

Sysname vlan 4

Sysname-vlan4 quit

Sysname vlan 2

Sysname-vlan2 private-vlan primary

Sysname-vlan2 private-vlan secondary 4

Sysname-vlan2 quit

\# 配置端口GigabitEthernet1/0/1在VLAN 2中工作在promiscuous模式。

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port private-vlan 2 promiscuous

Sysname-GigabitEthernet1/0/1 quit

\# 配置链路类型为Access的端口GigabitEthernet1/0/2和GigabitEthernet1/0/3在VLAN 4中工作在host模式。

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port access vlan 4

Sysname-GigabitEthernet1/0/2 port private-vlan host

Sysname-GigabitEthernet1/0/2 quit

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 port access vlan 4

Sysname-GigabitEthernet1/0/3 port private-vlan host

Sysname-GigabitEthernet1/0/3 quit

\# 配置Secondary VLAN 4内各端口二层隔离。

Sysname vlan 4

Sysname-vlan4 private-vlan isolated

【相关命令】

·**private-vla****n **（VLAN view）

·**private-vlan community**

·**private-vlan primary**

**Private VLAN \-- Private VLAN配置命令 \-- private-vlan primary**

------------------------------------------------------------------------

**[private-vlan primary**]命令用来配置VLAN的类型为Primary VLAN。

**[undo private-vlan primary**]命令用来恢复缺省情况。

【命令】

**[private-vlan primary**]

**[undo private-vlan primary**]

【缺省情况】

VLAN的类型不是Primary VLAN。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置该命令时，若已经配置Primary VLAN和Secondary VLAN的映射关系，且设备上有端口工作在promiscuous模式、trunk promiscuous模式、trunk secondary模式或host模式，则依据接口配置会触发配置同步。

【举例】

\# 配置VLAN 5为Primary VLAN。

\<Sysname\> system-view

Sysname vlan 5

Sysname-vlan5 private-vlan primary

【相关命令】

·**port private-vlan host**

·**port private-vlan promiscuous**

·**port private-vlan trunk promiscuous**

·**port private-vlan trunk secondary**

·**private-vlan primary**

\

**Voice VLAN \-- Voice VLAN配置命令 \-- display voice-vlan mac-address**

------------------------------------------------------------------------

**[display voice-vlan mac-address**]命令用来显示Voice VLAN当前支持的OUI地址、OUI地址掩码和描述信息。

【命令】

**[display voice-vlan mac-address**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示Voice VLAN的OUI地址、OUI地址掩码和描述信息。

\<Sysname\> display voice-vlan mac-address

OUI Address     Mask            Description

0001-e300-0000  ffff-ff00-0000  Siemens phone

0003-6b00-0000  ffff-ff00-0000  Cisco phone

0004-0d00-0000  ffff-ff00-0000  Avaya phone

000f-e200-0000  ffff-ff00-0000  H3C Aolynk phone

0060-b900-0000  ffff-ff00-0000  Philips/NEC phone

00d0-1e00-0000  ffff-ff00-0000  Pingtel phone

00e0-7500-0000  ffff-ff00-0000  Polycom phone

00e0-bb00-0000  ffff-ff00-0000  3Com phone

表4-1 display voice-vlan mac-address命令显示信息描述表

字段

描述

OUI Address

设备当前允许通过的OUI地址

Mask

设备当前允许通过的OUI地址的掩码

Description

设备当前允许通过的OUI地址的描述

【相关命令】

·**voice-vlan mac-****address**

**Voice VLAN \-- Voice VLAN配置命令 \-- display voice-vlan state**

------------------------------------------------------------------------

**[display voice-vlan state**]命令用来显示Voice VLAN的配置信息。

【命令】

**[display voice-vlan state**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示Voice VLAN的配置信息。

\<Sysname\> display voice-vlan state

 Current voice VLANs: 1

 Voice VLAN security mode: Security

 Voice VLAN aging time: 1440 minutes

 Voice VLAN enabled ports and their modes:

 Port                        VLAN        Mode        CoS        DSCP

 GigabitEthernet1/0/1        111         Auto        6          46

![说明](VLAN命令.files/image004.png)

具体显示内容与设备的型号有关，请以设备的实际情况为准。

表4-2 display voice-vlan state命令显示信息描述表

字段

描述

Current Voice VLANs

已创建的Voice VLAN数量

Voice VLAN security mode

Voice VLAN的安全模式的开启状态：

·Security：表示当前使用的是安全模式

·Normal：表示当前使用的是普通模式

Voice VLAN aging time

Voice VLAN的老化时间

Voice VLAN enabled ports and their modes

当前使能了Voice VLAN的端口及其工作模式

Port

当前使能了Voice VLAN的端口编号

VLAN

端口使能的Voice VLAN ID

Mode

端口Voice VLAN的工作模式：

·Auto：表示自动模式

·Manual：表示手工模式

CoS

服务级别

DSCP

差分服务编码点优先级

【相关命令】

·**voice-vlan aging**

·**voice-vlan enable**

·**voice-vlan mode auto**

·**voice-vlan security enable**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan aging**

------------------------------------------------------------------------

**[voice-vlan aging**]命令用来设置Voice VLAN的老化时间。

**[undo voice-vlan aging**]命令用来恢复缺省情况。

【命令】

**[voice-vlan aging**] *minutes*

**[undo voice-vlan aging**]

【缺省情况】

Voice VLAN的老化时间为1440分钟。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[minutes*]：Voice VLAN的老化时间，取值范围为5～43200，单位为分钟。

【使用指导】

·在自动模式下，系统会根据收到的语音报文的源MAC地址，来决定是否把该报文的入端口加入Voice VLAN。在将入端口加入Voice VLAN后，系统会同时启动老化定时器。经过老化时间后，如果设备没有从该端口收到任何语音报文，老化时间到达后系统会自动把该端口从Voice VLAN中删除。

·老化时间只对Voice VLAN工作在自动模式的端口有效，对Voice VLAN工作在手工模式的端口无效。

【举例】

\# 将Voice VLAN的老化时间配置为100分钟。

\<Sysname\> system-view

Sysname voice-vlan aging 100

【相关命令】

·**display voice-vlan state**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan enable**

------------------------------------------------------------------------

**[voice-vlan ***vlan-id***enable**]命令用来使能端口的Voice VLAN功能。

**[undo voice-vlan enable**]命令用来关闭端口的Voice VLAN功能。

【命令】

**[voice-vlan** *vlan-id* **enable**]

**[undo voice-vlan** [ *vlan-id*  **enable**]]

【缺省情况】

端口的Voice VLAN功能处于关闭状态。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：Voice VLAN编号，取值范围为2～4094。

【使用指导】

·当端口的Voice VLAN工作在自动模式时，只有Trunk或者Hybrid类型端口支持使能Voice VLAN功能。

·使能端口的Voice VLAN功能之前，须确保对应的VLAN已存在。

【举例】

\# 使能端口GigabitEthernet1/0/1的Voice VLAN功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 voice-vlan 2 enable

【相关命令】

·**display voice-vlan state**

·**voice-vlan mode auto**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan mac-address**

------------------------------------------------------------------------

**[voice-vlan mac-address**]命令用来配置允许指定OUI地址的报文通过Voice VLAN。

**[undo voice-vlan mac-address**]命令用来取消指定OUI地址的报文通过Voice VLAN。

【命令】

**[voice-vlan mac-address** *mac-address* **mask** *oui-mask* [ **description** *text* ]]

**[undo voice-vlan mac-address** *oui*]

【缺省情况】

系统已配置有如下表所示的OUI地址。

表4-3 设备缺省的OUI地址

序号

OUI地址

生产厂商

1

0001-E300-0000

Siemens phone

2

0003-6B00-0000

Cisco phone

3

0004-0D00-0000

Avaya phone

4

000F-E200-0000

H3C Aolynk phone

5

0060-B900-0000

Philips/NEC phone

6

00D0-1E00-0000

Pingtel phone

7

00E0-7500-0000

Polycom phone

8

00E0-BB00-0000

3Com phone

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：语音报文的源MAC地址，格式为H-H-H，如：1234-1234-1234。

**[mask ***oui-mask*]：OUI地址的有效长度，用掩码表示，格式为H-H-H。由连续的1和连续的0组成，表示OUI地址的匹配长度。如：FFFF-0000-0000，如果要匹配某个设备厂商的语音设备，可以设置为FFFF-FF00-0000。

**[description*** text*]：OUI地址的描述字符串，长度为1～30，区分大小写。

*[oui*]：指定要删除的OUI地址，格式为H-H-H，如1234-1200-0000。OUI地址不能是广播地址或者组播地址，也不能是全0的地址。OUI地址是*mac-address*和*oui-mask*参数相与的结果。可以通过**display voice-vlan mac-address**命令查看当前系统支持的OUI地址的信息。

【使用指导】

系统最多支持配置OUI地址个数以具体产品实际规格为准。

【举例】

\# 配置允许来自IP电话PhoneA（MAC地址为1234-1234-1234）的语音流通过Voice VLAN。

\<Sysname\> system-view

Sysname voice-vlan mac-address 1234-1234-1234 mask ffff-ff00-0000 description PhoneA

【相关命令】

·**display voice-vlan ****mac-address**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan mode auto**

------------------------------------------------------------------------

**[voice-vlan mode auto**]命令用来配置端口的Voice VLAN工作模式为自动模式。

**[undo voice-vlan mode auto**]命令用来配置端口的Voice VLAN工作模式为手工模式。

【命令】

**[voice-vlan mode auto**]

**[undo voice-vlan mode auto**]

【缺省情况】

端口的Voice VLAN工作模式为自动模式。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当端口使能了Voice VLAN并工作在手工模式时，必须手工将端口加入Voice VLAN，才能保证Voice VLAN功能生效。

【举例】

\# 将端口GigabitEthernet1/0/1的Voice VLAN的工作模式设置为手工模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo voice-vlan mode auto

【相关命令】

·**display voice-vlan state**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan qos**

------------------------------------------------------------------------

![说明](VLAN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[voice-vlan qos**]命令用来配置端口将Voice VLAN内语音报文的CoS和DSCP值修改为指定值。

**[undo voice-vlan qos**]命令用来恢复缺省情况。

【命令】

**[voice-vlan qos ***cos-value dscp-value*]

**[undo voice-vlan qos**]

【缺省情况】

端口将Voice VLAN内语音报文的CoS值修改为6，DSCP值修改为46。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cos-value*]：语音报文CoS值，取值范围为0～7。

*[dscp-value*]：语音报文DSCP值，取值范围为0～63。

【使用指导】

·在Voice VLAN使能的情况下，不允许配置本命令。必须关闭Voice VLAN功能后，才能配置本命令。

·如果对于同一端口多次执行**voice-vlan qos**和**voice-vlan qos trust**命令，以最后配置的命令为准。

【举例】

\# 配置端口GigabitEthernet1/0/1收到Voice VLAN内的语音报文时，将报文的CoS值修改为5，DSCP值修改为45。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 voice-vlan qos 5 45

【相关命令】

·**voice-vlan qos trust**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan qos trust**

------------------------------------------------------------------------

![说明](VLAN命令.files/image005.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[voice-vlan qos trust**]命令用来配置端口信任Voice VLAN内语音报文的优先级，即端口不会修改Voice VLAN内语音报文自带的CoS和DSCP值。

**[undo voice-vlan qos**]命令用来恢复缺省情况。

【命令】

**[voice-vlan qos trust**]

**[undo voice-vlan qos**]

【缺省情况】

端口将Voice VLAN内语音报文的CoS值修改为6，DSCP值修改为46。

【视图】

二层以太网接口视图/S通道接口视图/S通道聚合接口视图/二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在Voice VLAN使能的情况下，不允许配置本命令。必须关闭Voice VLAN功能后，才能配置本命令。

·如果对于同一端口多次执行**voice-vlan qos**和**voice-vlan qos trust**命令，以最后配置的命令为准。

【举例】

\# 配置端口GigabitEthernet1/0/1信任语音报文的优先级。端口收到Voice VLAN内语音报文后，报文自带的CoS和DSCP值保持不变。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 voice-vlan qos trust

【相关命令】

·**voice-vlan qos**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan security enable**

------------------------------------------------------------------------

**[voice-vlan security enable**]命令用来使能Voice VLAN的安全模式。

**[undo voice-vlan security enable**]命令用来关闭Voice VLAN的安全模式。

【命令】

**[voice-vlan security enable**]

**[undo voice-vlan security enable**]

【缺省情况】

Voice VLAN工作在安全模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在安全模式下，Voice VLAN中只能有语音流量。用户使能Voice VLAN的安全模式以后，该VLAN的报文都经过过滤，设备会根据报文的源MAC地址是否匹配OUI地址来过滤所有非语音流量，增加安全性保证语音流的优先级，保证通话质量。在普通模式下，Voice VLAN中允许有业务流量和语音流量并存。

【举例】

\# 关闭Voice VLAN的安全模式。

\<Sysname\> system-view

Sysname undo voice-vlan security enable

【相关命令】

·**display voice-vlan state**

**Voice VLAN \-- Voice VLAN配置命令 \-- voice-vlan track lldp**

------------------------------------------------------------------------

**[voice-vlan track lldp**]命令用来使能通过LLDP自动发现IP电话功能。

**[undo voice-vlan track lldp**]命令用来恢复缺省情况。

【命令】

**[voice-vlan track lldp**]

**[undo voice-vlan track lldp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过LLDP自动发现IP电话功能处于关闭状态。

【举例】

\# 在设备上使能通过LLDP自动发现IP电话功能。

\<Sysname\> system-view

Sysname voice-vlan track lldp

