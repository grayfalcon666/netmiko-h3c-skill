<!-- CMD-INDEX
  bandwidth                           | 以太网冗余接口视图        | L29
  default                             | 以太网冗余接口视图        | L75
  description                         | 以太网冗余接口视图        | L111
  display interface reth              | 任意视图             | L153
  display reth interface              | 任意视图             | L365
  interface reth                      | 系统视图             | L463
  member interface                    | 以太网冗余接口视图        | L509
  mtu                                 | 以太网冗余接口视图        | L577
  reset counters interface            | 用户视图             | L625
  shutdown                            | 以太网冗余接口视图        | L667
  bind chassis                        | 冗余组节点视图          | L707
  bind slot                           | 冗余组节点视图          | L763
  display redundancy group            | 任意视图             | L819
  hold-down-interval                  | 冗余组视图            | L1077
  member failover group               | 冗余组视图            | L1123
  member interface                    | 冗余组视图            | L1175
  node                                | 冗余组视图            | L1223
  node-member interface               | 冗余组节点视图          | L1271
  preempt-delay                       | 冗余组视图            | L1341
  priority                            | 冗余组节点视图          | L1387
  redundancy group                    | 系统视图             | L1435
  snmp-agent trap enable redundancy   | 系统视图             | L1483
  switchover request                  | 冗余组视图            | L1525
  switchover reset                    | 冗余组视图            | L1563
  track                               | 冗余组节点视图          | L1601
-->

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置以太网冗余接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth*** bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽为10000kbit/s。

【视图】

以太网冗余接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置以太网冗余接口Reth1的期望带宽为50kbit/s。

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1 bandwidth 50

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复以太网冗余接口的缺省配置。

【命令】

**[default**]

【视图】

以太网冗余接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将以太网冗余接口Reth1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1 default

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置以太网冗余接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Reth-redundancy1 Interface。

【视图】

以太网冗余接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：以太网冗余接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置以太网冗余接口Reth1的描述信息为master-interface。

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1 description master-interface

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- display interface reth**

------------------------------------------------------------------------

**[display interface reth**]命令用来显示以太网冗余接口的相关信息。

【命令】

**[display interface** [ **reth** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reth**]：显示以太网冗余接口的相关信息.

*[interface-number*]：显示指定以太网冗余接口的信息。*interface-number*表示以太网冗余接口的编号，取值为已创建的以太网冗余接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

**[description**]：用来显示用户配置的接口的全部描述信息。

【使用指导】

·如果不指定**reth**参数，将显示设备支持的所有接口的相关信息；

·如果指定**reth**参数，不指定*interface-number*参数，将显示所有以太网冗余接口的相关信息。

·如果指定**reth**参数，同时指定了*interface-number*参数，将显示指定以太网冗余接口的相关信息。

【举例】

\# 显示以太网冗余接口Reth1的相关信息。

\<Sysname\> display interface reth 1

Reth1

Current state: UP

Line protocol state: UP

Description: Reth1 Interface

Bandwidth: 10000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0cda-41b5-cf30

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0cda-41b5-cf30

Physical: Reth, baudrate: 10000000 bps

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

\# 显示Reth1接口的概要信息。

\<Sysname\> display interface reth 1 brief

Brief information about interfaces in route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

RETH1                DOWN DOWN     \--

表1-3 display interface reth命令显示信息描述表{.TableDescriptionChar}

字段

描述

Current state

接口当前的物理状态和管理状态，可能的取值及含义如下：

·DOWN(Administratively)：表示该接口已经通过shutdown命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但没有成员接口或成员接口物理状态都为DOWN

·UP：表示该接口的管理状态为开启，且至少有一个成员接口物理状态为UP

Line protocol state

接口的链路协议状态，可能的状态及含义如下：

·UP：该接口的协议状态为开启

·DOWN：该接口的协议状态为关闭

Description

接口描述信息

Bandwidth

接口期望带宽，由接口下bandwidth命令配置

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing

网络层协议处理状况。disabled表示接口尚未配置IP地址，不能处理IP报文。当接口配置了IP地址之后，本字段将变为"Internet Address"，后面显示接口配置的IP地址

IP Packet Frame Type

以太网帧格式

Hardware Address

接口的MAC地址

IPv6 Packet Frame Type

IPv6报文发送帧格式

Physical

接口的类型为Reth

baudrate

接口的波特率为10000000bps

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Last 300 seconds input rate

最近300秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，packets/sec表示平均每秒输入的报文数

Last 300 seconds output rate

最近300秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数， packets/sec表示平均每秒输出的报文数

Input

该接口接收的数据报文个数、字节数，以及由于没有接收缓冲而被丢弃的报文个数

Output

该接口发送的数据报文个数、字节数，以及由于没有发送缓冲而被丢弃的报文个数

Brief information on interface(s) under route mode

三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的网络层协议状态显示是UP的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示本链路物理上是连通的

·DOWN：表示本链路物理上是不通的

Protocol

接口协议连接状态，取值可能为：

·DOWN：该接口的协议状态为关闭

·UP：该接口的协议状态为开启

Main IP

接口主IP地址

Description

接口的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- display reth interface**

------------------------------------------------------------------------

**[display reth**] **interface**命令用来显示以太网冗余接口的成员接口的信息。

【命令】

**[display reth interface reth***interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reth ***interface-number*]：表示接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 显示以太网冗余接口Reth1的信息。（集中式IRF设备）

\<Sysname\> display reth interface reth 1

Reth1 :

  Redundancy group  : aa

  Member         Physical status       Forwarding status      Presence status

  GE1/0/1      UP                    Active                 Normal

  GE1/0/2      UP                    Inactive               Normal

\# 显示以太网冗余接口Reth1的信息。（分布式设备－IRF模式）

\<Sysname\> display reth interface reth 1

Reth1 :

  Redundancy group  : aa

  Member         Physical status       Forwarding status      Presence status

  GE1/2/0/1      UP                    Active                 Normal

  GE1/2/0/2      UP                    Inactive               Normal

表1-1 display reth命令显示信息描述表

字段

描述

Reth1

以太网冗余接口Reth1的信息

Redundancy group

以太网冗余接口所在的冗余组，未加入冗余组时显示为N/A

Member

成员接口的名称

Physical status

成员接口的物理状态：

·Down(redundancy down)：表示该接口被Reth模块关闭，即接口状态为冗余关闭

·Down：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路关闭）

·Up：该接口的管理状态和物理状态均为开启

Forwarding status

成员接口的转发状态：

·Active：成员接口可以正常收发报文

·Inactive：成员接口不能收发报文

Presence status

成员接口的在位状态：

·Normal表示在位

·Absent表示不在位

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- interface reth**

------------------------------------------------------------------------

**[interface** **reth**]命令用来创建以太网冗余接口并进入该接口视图。

**[undo interface reth**]命令用来删除以太网冗余接口。

【命令】

**[interface** **reth** *interface-number*]

**[undo interface reth** *interface-number*]

【缺省情况】

未创建以太网冗余接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

删除以太网冗余接口时，如果该接口下存在成员接口，则不允许删除。

【举例】

\# 创建以太网冗余接口Reth1。

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- member interface**

------------------------------------------------------------------------

**[member interface**]命令用来给以太网冗余接口添加成员接口。

**[undo member interface**]命令用来将成员接口从以太网冗余接口中删除。

【命令】

**[member interface ***interface-type interface-number ***priority ***priority*]

**[undo member interface*** interface-type interface-number*]

【缺省情况】

以太网冗余接口下没有任何成员接口。

【视图】

以太网冗余接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：接口类型和接口编号。

*[priority*]：成员接口的优先级，取值范围为1～255。

【使用指导】

成员接口的优先级数值越大，优先级越高。当两成员接口的链路状态均为UP时，系统会让优先级高的成员接口处于激活状态，优先级低的处于非激活状态。激活接口可以收发报文，非激活接口不能收发报文。

以太网冗余接口的成员接口的类型可以为：三层以太网接口、三层GigabitEthernet接口、三层Ten-GigabitEthernet接口、三层TwentyGigE接口、三层FortyGigE接口、三层HundredGigE接口、三层聚合口、EFM接口及上述接口的子接口。

每个以太网冗余接口下最多可添加两个成员接口。同一以太网冗余接口的成员接口的类型和速率最好相同，例如均为100M三层以太网接口，从而能够保证成员接口切换后不因带宽过窄，影响正常的流量转发。

一个物理接口加入一个以太网冗余接口后，不能加入其它以太网冗余接口。

当以太网冗余接口的成员接口包含子接口时，不能指定该以太网冗余接口为IPv6静态邻居表项的出接口。关于IPv6静态邻居表项的详细描述请参见"三层技术-IP业务配置指导"中的"Ipv6基础"。

【举例】

\# 给以太网冗余接口Reth1中添加成员接口GigabitEthernet1/0/1，并指定优先级为100；添加成员接口GigabitEthernet1/0/2，并指定优先级为50。（集中式IRF设备）

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1 member interface gigabitethernet 1/0/1 priority 100

Sysname-Reth1 member interface gigabitethernet 1/0/2 priority 50

\# 给以太网冗余接口Reth1中添加成员接口GigabitEthernet1/1/0/1，并指定优先级为100；添加成员接口GigabitEthernet1/1/0/2，并指定优先级为50。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1 member interface gigabitethernet 1/2/0/1 priority 100

Sysname-Reth1 member interface gigabitethernet 1/2/0/2 priority 50

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置以太网冗余接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

接口的MTU值为1500字节。

【视图】

以太网冗余接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

需要注意的是，配置了**mtu**命令后需要执行命令**shutdown**和**undo shutdown**，这样该配置才能在接口上生效。

【举例】

\# 配置以太网冗余接口Reth1的MTU值为200字节。

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1 mtu 200

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除以太网冗余接口的统计信息。

【命令】

**[reset counters interface ** **reth**  *interface-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reth**]：清除以太网冗余接口的统计信息。

*[interface-number*]：以太网冗余接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

如果不指定**reth**参数，则清除所有接口的统计信息；

·如果指定了**reth**参数而不指定*interface-number*，则清除所有以太网冗余接口的统计信息；

·如果指定了**reth**参数，同时指定了*interface-number*参数，将清除指定以太网冗余接口的统计信息。

【举例】

\# 清除以太网冗余接口Reth1的统计信息。

\<Sysname\> reset counters interface reth 1

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭以太网冗余接口。

**[undo shutdown**]命令用来打开以太网冗余接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

以太网冗余接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭以太网冗余接口Reth1。

\<Sysname\> system-view

Sysname interface reth 1

Sysname-Reth1 shutdown

\

**冗余组 \-- 冗余组配置命令 \-- bind chassis**

------------------------------------------------------------------------

![说明](冗余备份命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bind chassis**]命令用来将冗余组节点和IRF成员设备绑定。

**[undo bind chassis**]命令用来取消冗余组节点和IRF成员设备的绑定。

【命令】

**[bind chassis ***chassis-number*]

**[undo bind chassis**]

【缺省情况】

冗余组节点未绑定任何成员设备。

【视图】

冗余组节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[chassis-number*]：设备在IRF中的成员编号。

【使用指导】

一个冗余组节点只能绑定一个成员设备。冗余组节点和成员设备绑定后，可以将这个成员设备上的部分接口添加到冗余组节点中作为冗余组节点的成员接口。这样，使用两个冗余组节点，就能实现一台成员设备上的部分接口和另一台成员设备上的部分接口互为备份。

一个成员设备只能和一个节点绑定。

冗余组节点下有成员接口时不能使用该命令修改绑定关系。

【举例】

\# 将冗余组aaa节点1与成员设备3绑定。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

Sysname-redundancy-group-aaa-node1 bind chassis 3

**冗余组 \-- 冗余组配置命令 \-- bind slot**

------------------------------------------------------------------------

![说明](冗余备份命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bind slot**]命令用来将冗余组节点和IRF成员设备绑定。

**[undo bind slot**]命令用来取消冗余组节点和IRF成员设备的绑定。

【命令】

**[bind slot ***slot-number*]

**[undo bind slot**]

【缺省情况】

冗余组节点未绑定任何成员设备。

【视图】

冗余组节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[slot-number*]：设备在IRF中的成员编号。

【使用指导】

一个冗余组节点只能绑定一个成员设备。冗余组节点和成员设备绑定后，可以将这个成员设备上的部分接口添加到冗余组节点中作为冗余组节点的成员接口。这样，使用两个冗余组节点，就能实现一台成员设备上的部分接口和另一台成员设备上的部分接口互为备份。

一个成员设备只能和一个节点绑定。

冗余组节点下有成员接口时不能使用该命令修改绑定关系。

【举例】

\# 将冗余组aaa节点1与成员设备1绑定。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

Sysname-redundancy-group-aaa-node1 bind slot 1

**冗余组 \-- 冗余组配置命令 \-- display redundancy group**

------------------------------------------------------------------------

**[display redundancy group**]命令用来显示冗余组的相关信息。

【命令】

**[display **]**redundancy group**** *group-name*

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：冗余组的名称，为1～15个字符的字符串，区分大小写。

【举例】

\# 显示冗余组aaa的相关信息。（集中式IRF设备）

\<Sysname\> display redundancy group aaa

Redundancy group aaa (ID 1):

  Node ID      Slot        Priority   Status           Track weight

  1            Slot1       100        Secondary        -255

  2            Slot2       99         Primary          255

Preempt delay time remained   : 0    min

Preempt delay timer setting   : 1    min

Remaining hold-down time      : 0    sec

Hold-down timer setting       : 300  sec

Manual switchover request     : No

Member interfaces:

    Reth1          Reth2

Member failover groups:

Node 1:

  Node member     Physical status

    GE1/0/2       DOWN

    GE1/0/4       DOWN(redundancy down)

  Track info:

    Track    Status       Reduced weight     Interface

    1        Negative     255                GE1/0/2(Fault)

    2        Negative     255                GE1/0/4

Node 2:

  Node member    Physical status

    GE2/0/2   UP

    GE2/0/4    UP

  Track info：

    Track    Status       Reduced weight     Interface

    3        Positive     55                 GE2/0/2

    4        Positive     55                 GE2/0/4

\# 显示冗余组aaa的相关信息。（分布式设备－IRF模式）

\<Sysname\> display redundancy group aaa

Redundancy group aaa (ID 1):

  Node ID      Chassis        Priority   Status           Track weight

  1            Chassis1       100        Secondary        -255

  2            Chassis2       99         Primary          255

Preempt delay time remained   : 0    min

Preempt delay timer setting   : 1    min

Remaining hold-down time      : 0    sec

Hold-down timer setting       : 300  sec

Manual switchover request     : No

Member interfaces:

    Reth1          Reth2

Member failover groups:

    groupa

    groupabc

Node 1:

  Node member     Physical status

    GE1/1/0/2     DOWN

    GE1/1/0/4     DOWN(redundancy down)

  Track info:

    Track    Status       Reduced weight     Interface

    1        Negative     255                GE1/1/0/2(Fault)

    2        Negative     255                GE1/1/0/4

Node 2:

  Node member    Physical status

    GE2/1/0/2    UP

    GE2/1/0/4    UP

  Track info：

    Track    Status       Reduced weight     Interface

    3        Positive     55                 GE2/1/0/2

    4        Positive     55                 GE2/1/0/4

表2-1 display redundancy group命令显示信息描述表

字段

描述

Redundancy group aaa (ID 1)

冗余组aaa（该冗余组的编号为1）

Node ID

冗余组节点的编号

Chassis

节点绑定的成员设备的编号（分布式设备－IRF模式）

Slot

节点绑定的成员设备的编号（集中式IRF设备）

Priority

节点的优先级

Status

对应节点当前所处的状态：

·Primary：当前节点为主节点，能够正常收发报文

·Secondary：当前节点为备节点；当优先级高的节点为备节点时，节点上的所有成员接口会被冗余组强制设置为Down状态，不能收发报文；当优先级低的节点为备节点时，节点的所有成员接口能够正常收发报文，为主节点分担流量

Track weight

节点的当前权重值

Preempt delay time remained

剩余的倒回延时，单位为分钟

Preempt delay timer setting

配置的倒回延时，单位为分钟

Remaining hold-down time

剩余的状态保持时间，单位为秒

Hold-down timer setting

配置的状态保持时间，单位为秒

Manual switchover request

手工倒换请求，取值为：

·Yes：表示存在手动倒换请求

·No：表示无倒换请求

Member interfaces

冗余组中添加的以太网冗余接口

Member failover groups

冗余组中添加的备份组

Node 1

冗余组节点的详细信息

Node member

冗余组节点的成员接口

Physical status

成员接口的物理状态：

·Down(redundancy down)：表示该接口被Reth模块关闭，即接口状态为冗余关闭

·Down：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路关闭）

·Up：该接口的管理状态和物理状态均为开启

Track info

冗余组节点关联的Track项的信息

Track

Track项的编号

Status

Track项的状态

Reduced weight

Track项的当前权重值

Interface

Track项的关联接口，如果显示为Fault，则表示该接口已故障；如果显示为Absent，则表示该接口当前不在位

**冗余组 \-- 冗余组配置命令 \-- hold-down-interval**

------------------------------------------------------------------------

**[hold-down-interval**]命令用来指定冗余组节点状态的保持时间，这段时间内不能发生主备倒换。

**[undo hold-down-interval**]命令用来恢复缺省情况。

【缺省情况】

保持时间为1秒。

【命令】

**[hold-down-interval**]*second*

**[undo hold-down-interval**]

【视图】

冗余组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[second*]：保持时间，取值范围为0～1800，单位为秒。

【使用指导】

当网络不稳定，监测接口/链路状态频繁改变，会导致Track项状态在短时间内频繁改变，连带导致冗余组需要不断的响应主备倒换事件，使用保持定时器可以避免这种情况的发生。当节点完成主备倒换后，系统启动保持定时器。在保持时间内，不允许再次发生主备倒换。

【举例】

\# 将冗余节点的状态保持时间配置为300秒。

\<Sysname\> system-view

Sysname redundancy group aa

Sysname-redundancy-group-aa hold-down-interval 300

**冗余组 \-- 冗余组配置命令 \-- member failover group**

------------------------------------------------------------------------

![说明](冗余备份命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[member failover group**]命令用来将备份组加入冗余组。

**[undo member failover group**]命令用来将备份组从冗余组下删除。

【命令】

**[member failover group** *group-name*]

**[undo member failover group ***group-name*]

【缺省情况】

冗余组下没有备份组。

【视图】

冗余组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：备份组名称，为1～63个字符的字符串，区分大小写。

【使用指导】

一个备份组只能加入一个冗余组。备份组加入冗余组后主备倒换受冗余组的影响。

一个冗余组下最多可以加入32个备份组，且必须是已经创建的备份组。否则，本命令将执行失败。

【举例】

\# 将备份组bb加入冗余组aaa中。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa member failover group bb

**冗余组 \-- 冗余组配置命令 \-- member interface**

------------------------------------------------------------------------

**[member interface**]命令用来将以太网冗余接口加入冗余组。

**[undo member interface**]命令用来将以太网冗余接口从冗余组下删除。

【命令】

**[member interface reth***interface-number*]

**[undo member interface reth ***interface-number*]

【缺省情况】

冗余组下没有添加以太网冗余接口。

【视图】

冗余组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reth ***interface-number*]：以太网冗余接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

一个以太网冗余接口只能加入一个冗余组。以太网冗余接口加入冗余组后主备倒换受冗余组的影响。

一个冗余组下最多可以加入32个以太网冗余接口，且必须是已经创建的以太网冗余接口。否则，本命令将执行失败。

【举例】

\# 将以太网冗余接口Reth1加到冗余组aaa中。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa member interface reth 1

**冗余组 \-- 冗余组配置命令 \-- node**

------------------------------------------------------------------------

**[node**]命令用来创建冗余组节点，并进入冗余组节点视图。

**[undo node**]命令用来删除冗余组节点。

【命令】

**[node ***node-id*]

**[undo node ***node-id*]

【缺省情况】

未创建任何冗余组节点。

【视图】

冗余组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

node-id：表示冗余组节点编号，取值范围为1～2。

【使用指导】

每个冗余组下最多可创建两个冗余组节点，这两个冗余组节点为主备关系。

当冗余组节点绑定了IRF成员设备时，不能删除该冗余组节点。

【举例】

\# 在冗余组aaa下，创建冗余组节点1。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

**冗余组 \-- 冗余组配置命令 \-- node-member interface**

------------------------------------------------------------------------

**[node-member interface**]命令用来为冗余组节点添加成员接口。

**[undo node-member interface**]命令用来将成员接口从冗余节点中删除。

【缺省情况】

冗余组节点下不存在任何成员接口。

【命令】

**[node-member interface ***interface-type interface-number*]

**[undo node-member interface ***interface-type interface-number*]

【视图】

冗余组节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：接口类型和编号。

【使用指导】

执行本命令前，请先执行**bind chassis**或**bind slot**命令。否则，本命令执行失败。

本命令中加入的成员接口必须是冗余组节点绑定的IRF成员设备上的接口。

一个冗余组节点下最多可添加32个成员接口，但是这些成员接口不能是聚合口和子接口，不能是以太网冗余接口的成员接口。

一个接口加入一个冗余组节点后，就不能再加入其它的冗余组节点。{.TableTextChar}

【举例】

\# 将接口GigabitEthernet1/0/1加到冗余组aaa的节点1中。（集中式IRF设备）

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

Sysname-redundancy-group-aaa-node1node-member interface gigabitethernet 1/0/1

\# 将接口GigabitEthernet1/2/0/1加到冗余组aaa的节点1中。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

Sysname-redundancy-group-aaa-node1node-member interface gigabitethernet 1/2/0/1

【相关命令】

·**bind chassis**

·**bind slot**

**冗余组 \-- 冗余组配置命令 \-- preempt-delay**

------------------------------------------------------------------------

**[preempt-delay**]命令用来指定冗余组节点的倒回延时。

**[undo preempt-delay**]命令用来恢复情况。

【命令】

**[preempt-delay**]*delay-time*

**[undo preempt-delay**]

【缺省情况】

倒回延时为1分钟。

【视图】

冗余组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay-time*]：冗余组将业务倒回到高优先级节点的等待时间，取值范围为0～12，单位为分钟，配置为0时表示不倒回。

【使用指导】

当冗余组内优先级高的节点倒回条件就绪时（譬如故障恢复），会触发倒回事件，但启动倒回定时器。由于需要整体倒回，在冗余组倒回的过程中会同时触发很多事件（比如接口状态变化等），这些事件的处理需要时间。倒回定时器能够为冗余组提供一段时间，让节点准备完毕后，再将业务从优先级低的节点倒换到优先级高的节点。

【举例】

\# 配置冗余组aaa的倒回等待时间为2分钟。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa preempt-delay 2

**冗余组 \-- 冗余组配置命令 \-- priority**

------------------------------------------------------------------------

**[priority**]命令用来配置冗余组节点的优先级。

**[undo priority**]命令用来恢复缺省情况。

【命令】

**[priority ***priority*]

**[undo priority**]

【缺省情况】

冗余组节点的优先级为1。

【视图】

冗余组节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：优先级的值，取值范围为1～255。

【使用指导】

冗余组节点的优先级数值越大，节点的优先级越高。缺省情况下，优先级高的冗余组节点为主节点，优先级低的为备节点。当冗余组下两个节点优先级相同时，编号小的为主节点，编号大的为备节点。

【举例】

\# 将冗余组aaa节点1的优先级设置为3。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

Sysname-redundancy-group-aaa-node1 priority 3

**冗余组 \-- 冗余组配置命令 \-- redundancy group**

------------------------------------------------------------------------

**[redundancy group**]命令用来创建冗余组并进入该冗余组视图。

**[undo redundancy group**]命令用来删除冗余组。

【命令】

**[redundancy group ***group-name*]

**[undo redundancy group ***group-name*]

【缺省情况】

设备上不存在任何冗余组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

group-name：冗余组的名称，为1～15个字符的字符串，区分大小写。

【使用指导】

如果冗余组不存在，则先创建该冗余组，再进入该冗余组视图。如果冗余组已经创建，则直接进入该冗余组视图。

多次执行该命令可创建多个冗余组，最多可创建255个。

当冗余组中还有冗余接口或者冗余组节点时，不能删除该冗余组。

【举例】

\# 创建名称为aaa的冗余组。

\<Sysname\> system-view

Sysname redundancy group aaa

**冗余组 \-- 冗余组配置命令 \-- snmp-agent trap enable redundancy**

------------------------------------------------------------------------

**[snmp-agent trap enable rddc**]命令用来开启冗余组告警功能。

**[undo snmp-agent trap enable rddc**]命令用来关闭冗余组告警功能。

【命令】

**[snmp-agent trap enable rddc**]

**[undo snmp-agent trap enable rddc**]

【缺省情况】

冗余组告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启冗余组告警功能后，在冗余组人工倒换、故障接口恢复、故障接口生成时，会生成告警信息，并将该信息发送到设备的SNMP模块。通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关特性。

有关告警信息的详细描述，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启冗余组告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable rddc

**冗余组 \-- 冗余组配置命令 \-- switchover request**

------------------------------------------------------------------------

**[switchover request**]命令用来手工触发指定冗余组进行主备倒换，让冗余组工作在优先级低的节点。

【命令】

**[switchover request**]

【视图】

冗余组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当冗余组主备结点无故障，业务运行在优先级高的节点时，用户可通过此命令触发冗余组主备倒换，让业务运行到备结点，以便用户可更换主节点上的部件。

【举例】

\# 手工触发指定冗余组的主备倒换。

\<Sysname\> system-view

Sysname redundancy group aa

Sysname-redundancy-group-aa switchover request

【相关命令】

·**switchover reset**

**冗余组 \-- 冗余组配置命令 \-- switchover reset**

------------------------------------------------------------------------

**[switchover reset**]命令用来手工触发一次冗余组倒回，让冗余组工作在优先级高的节点。

【命令】

**[switchover reset**]

【视图】

冗余组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当冗余组主备结点无故障，业务运行在优先级低的节点时，用户可通过此命令手工触发冗余组进行倒回。

【举例】

\# 在冗余组aaa内手动触发一次倒回。

\<Sysname\> system-view

Sysname redundancy group aaa

Sysname-redundancy-group-aaa switchover reset

【相关命令】

·**switchover request**

**冗余组 \-- 冗余组配置命令 \-- track**

------------------------------------------------------------------------

**[track**]命令用来关联Track项。

**[undo track**]命令用来取消关联。

【命令】

**[track***track-entry-number***** **reduced** *weight-reduced* ]  **interface** *interface-type interface-number*

**[undo track***track-entry-number*]

【缺省情况】

冗余组节点下没有关联任何Track项。

【视图】

冗余组节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：Track项的序号，取值范围为1～1024。

**[reduced** *weight-reduced*]：权重的变化值，取值范围为1～255，缺省值为255。

**[interface**]*interface-type interface-number*：Track项关联接口的类型和编号。当影响Track项状态改变的接口是以太网冗余接口的成员接口或是冗余组节点的成员接口时，建议配置该参数，并将该参数配置成与Track项接口一致。

【使用指导】

一个节点最多能够配置64个Track项。

建议先创建Track项，再将该Track项和冗余组关联。否则，可能会导致冗余组没有有效的Track项而触发倒换。

当已将某物理接口配置为某冗余组内高优先级冗余组节点的成员接口，或者为某冗余组内以太网冗余接口的高优先级成员接口时，请不要将该物理接口的子接口配置为该冗余组内高优先级冗余组节点的Track项关联接口。因为物理接口被协议关闭时，会导致其子接口状态为Down，该子接口将无法触发自动倒回，此时，需要手工倒回。

【举例】

\# 将冗余组aaa和track 1、track 2关联。（集中式IRF设备）

\<Sysname\> system-view

Sysname track 1 interface gigabitethernet 1/0/1

Sysname track 2 interface gigabitethernet 2/0/1

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

Sysname-redundancy-group-aaa-node1 track 1 reduced 50 interface gigabitethernet 1/0/1

Sysname-redundancy-group-aaa-node1 track 2 reduced 50 interface gigabitethernet 2/0/1

\# 将冗余组aaa和track 1、track 2关联。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname track 1 interface gigabitethernet 1/2/0/1

Sysname track 2 interface gigabitethernet 2/2/0/1

Sysname redundancy group aaa

Sysname-redundancy-group-aaa node 1

Sysname-redundancy-group-aaa-node1 track 1 reduced 50 interface gigabitethernet 1/2/0/1

Sysname-redundancy-group-aaa-node1 track 2 reduced 50 interface gigabitethernet 2/2/0/1
