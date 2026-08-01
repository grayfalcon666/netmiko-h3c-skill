<!-- CMD-INDEX
  bandwidth                           | L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图 | L13
  default                             | L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图 | L75
  description                         | L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图 | L123
  display interface                   | 任意视图             | L179
  interface ve-l2vpn                  | 系统视图             | L467
  interface ve-l3vpn                  | 系统视图             | L537
  mtu                                 | L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图 | L603
  reset counters interface            | 用户视图             | L653
  shutdown                            | L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图 | L707
-->

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- bandwidth**

------------------------------------------------------------------------

![说明](L2VPN接入L3VPN或IP骨干网命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图

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

\# 配置接口VE-L2VPN100的期望带宽为10000kbps。

\<Sysname\> system-view

Sysname interface ve-l2vpn 100

Sysname-VE-L2VPN100 bandwidth 10000

\# 配置接口VE-L3VPN100的期望带宽为10000kbps。

\<Sysname\> system-view

Sysname interface ve-l3vpn 100

Sysname-VE-L3VPN100 bandwidth 10000

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将接口VE-L2VPN100恢复为缺省配置。

\<Sysname\> system-view

Sysname interface ve-l2vpn 100

Sysname-VE-L2VPN100 default

This command will restore the default settings. Continue? [Y/N:y]

\# 将接口VE-L3VPN100恢复为缺省配置。

\<Sysname\> system-view

Sysname interface ve-l3vpn 100

Sysname-VE-L3VPN100 default

This command will restore the default settings. Continue? [Y/N:y]

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，例如：VE-L2VPN100 Interface。

【视图】

L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述字符串，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。

本命令仅用于标识某接口，并无特别的功能。使用**display interface**等命令可以看到设置的描述信息。

【举例】

\# 配置接口VE-L2VPN100的描述信息为"L2VPN-Terminate"。

\<Sysname\> system-view

Sysname interface ve-l2vpn 100

Sysname-VE-L2VPN100 description L2VPN-Terminate

\# 配置接口VE-L3VPN100的描述信息为"L3VPN-Access"。

\<Sysname\> system-view

Sysname interface ve-l3vpn 100

Sysname-VE-L3VPN100 description L3VPN-Access

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- display interface**

------------------------------------------------------------------------

**[display interface**]命令用来显示接口的相关信息。

【命令】

**[display interface** **ve-l2vpn**[ [ *interface-number* *\| interface-number.subnumber* ] \| ]**ve-l3vpn**[ [ *interface-number \| interface-number.subnumber* ]   **brief** [ **description** \| **down** ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ve-l2vpn**]：显示L2VE接口或子接口的相关信息。

**[ve-l3vpn**]：显示L3VE接口或子接口的相关信息。

*[interface-number*]：L2VE接口或L3VE接口的接口编号，取值已创建的L2VE接口或L3VE接口的接口编号。

*[interface-number.subnumber*]：L2VE子接口或L3VE子接口的接口编号。其中*interface-number*为主接口编号，取值为已创建的L2VE接口或L3VE接口的接口编号；*subnumber*为子接口编号。该参数的支持情况[及子接口编号的取值范围与设备的型号有关，请以设备的实际情况为准。]

**[brief**]：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定接口类型（**ve-l2vpn**和**ve-l3vpn**），将显示设备支持的所有接口的相关信息。

·如果指定接口类型，不指定接口编号（*interface-number*和*interface-number.subnumber*），则显示所有指定类型接口的信息。

·如果同时指定接口类型和接口编号，则显示指定接口的信息。

【举例】

\# 显示接口VE-L2VPN100的相关信息。

\<Sysname\> display interface ve-l2vpn 100

VE-L2VPN100

Current state: UP

Line protocol state: UP

Description: VE-L2VPN100 Interface

Bandwidth: 100000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0202

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0202

Link service is PWE3 ethernet mode

Physical: L2VE

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

表1-1 display interface命令显示信息描述表

字段

描述

VE-L2VPN100

接口VE-L2VPN100的相关信息

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

Link service

链路业务模式，取值包括：

·VPLS mode：VPLS模式。接口上绑定VPLS实例时，接口的链路业务为该模式。VPLS实例的详细介绍，请参见"MPLS配置指导"中的"VPLS"

·PWE3 ethernet mode：PWE3的Ethernet模式。接口与PW关联，并且PW的封装方式为Ethernet模式时，接口的链路业务为该模式。PW的详细介绍，请参见"MPLS配置指导"中的"MPLS L2VPN"

·PWE3 vlan mode：PWE3的VLAN模式。接口与PW关联，并且PW的封装方式为VLAN模式时，接口的链路业务为该模式。PW的详细介绍，请参见"MPLS配置指导"中的"MPLS L2VPN"

Physical

接口的物理类型，取值包括：

·L2VE：表示该接口为用来终结MPLS L2VPN的L2VE接口或子接口

·L3VE：表示该接口为用来接入MPLS L3VPN或IP骨干网的L3VE接口或子接口

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

\# 显示所有L2VE类型接口的概要信息。

\<Sysname\> display interface ve-l2vpn brief

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

L2VE20                DOWN DOWN     \--

\# 显示接口L2VE2的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display interface ve-l2vpn 2 brief description

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

L2VE2                 UP    UP       1.1.1.1          L2VPN-Terminate

\# 显示当前状态为down的接口的信息以及DOWN的原因。

\<Sysname\> display interface brief down

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

L2VE20               DOWN Administratively

L3VE20               DOWN Administratively

表1-2 display interface brief命令显示信息描述表

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

·Not connected：表示未成功建立隧道

【相关命令】

·**reset counters interface**

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- interface ve-l2vpn**

------------------------------------------------------------------------

**[interface ve-l2vpn**]命令用来创建一个L2VE接口或子接口，并进入L2VE接口或子接口视图。

**[undo interface **]**ve-l2vpn**命令用来删除指定的L2VE接口或子接口。

【命令】

**[interface ve-l2vpn** { *interface-number \| interface-number.subnumber* }]

**[undo interface **]**ve-l2vpn **[{ *interface-number \| interface-number.subnumber* }]

【缺省情况】

设备上不存在任何L2VE接口和L2VE子接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：L2VE接口的编号，取值范围为1～8192。

*[interface-number.subnumber*]：L2VE子接口的接口编号。其中*interface-number*为主接口编号，取值范围为1～8192；*subnumber*为子接口编号。该参数的支持情况及子接口编号的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

L2VE接口（又称为VE-L2VPN接口）或子接口用于终结MPLS L2VPN报文。L2VE接口将还原的原始二层报文直接转交给与其相同接口编号的L3VE接口或子接口处理，但是L2VE子接口只能将还原的二层报文直接转交给与其相同接口编号的L3VE接口处理。

需要注意的是：

·当L2VE子接口收到的报文带有VLAN Tag时，需要在L2VE子接口上配置终结报文中的VLAN Tag。VLAN终结的详细介绍，请参见"二层技术-以太网交换配置指导"中的"VLAN终结"。

·删除L2VE接口，该接口上的子接口也将被删除。

·创建L2VE子接口之前，该子接口对应的主接口必须已经存在。

·在VPLS方式L2VPN接入L3VPN或IP骨干网的组网中，不支持创建L2VE子接口。

![说明](L2VPN接入L3VPN或IP骨干网命令.files/image001.png)

子接口的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建接口VE-L2VPN100，并进入L2VE接口视图。

\<Sysname\> system-view

Sysname interface ve-l2vpn 100

Sysname-VE-L2VPN100

\# 创建子接口VE-L2VPN100.10，并进入L2VE子接口视图。

\<Sysname\> system-view

Sysname interface ve-l2vpn 100.10

Sysname-VE-L2VPN100.10

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- interface ve-l3vpn**

------------------------------------------------------------------------

**[interface ve-l3vpn**]命令用来创建一个L3VE接口或子接口，并进入L3VE接口或子接口视图。

**[undo **]**interface ve-l3vpn**命令用来删除指定的L3VE接口或子接口。

【命令】

**[interface ve-l3vpn** { *interface-number \| interface-number.subnumber* }]

**[undo **]**interface ve-l3vpn **[{ *interface-number \| interface-number.subnumber* }]

【缺省情况】

设备上不存在任何L3VE接口和L3VE子接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：L3VE接口的接口编号，取值范围为1～8192。

*[interface-number.subnumber*]：L3VE子接口的接口编号。其中*interface-number*为主接口编号，取值范围为1～8192；*subnumber*为子接口编号。该参数的支持情况及子接口编号的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

L3VE接口（又称为VE-L3VPN接口）用来将报文接入MPLS L3VPN或IP骨干网。L3VE接口从骨干网侧接收到报文后，将报文转交给接口编号相同的L2VE接口进行MPLS L2VPN处理。

需要注意的是：

·当接入MPLS L3VPN或IP骨干网的报文带有VLAN Tag时，需要创建L3VE子接口，以便终结报文中的VLAN Tag。VLAN终结的详细介绍，请参见"二层技术-以太网交换配置指导"中的"VLAN终结"。

·删除L3VE接口，该接口上的子接口也将被删除。

·创建L3VE子接口之前，该子接口对应的主接口必须已经存在。

![说明](L2VPN接入L3VPN或IP骨干网命令.files/image001.png)

子接口的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建接口VE-L3VPN100，并进入L3VE接口视图。

\<Sysname\> system-view

Sysname interface ve-l3vpn 100

Sysname-VE-L3VPN100 quit

\# 创建子接口VE-L3VPN100.10，并进入L3VE子接口视图。

Sysname interface ve-l3vpn 100.10

Sysname-VE-L3VPN100.10

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，取值范围为46～1560，单位为字节。

【举例】

\# 配置接口VE-L2VPN100的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface ve-l2vpn 100

Sysname-VE-L2VPN100 mtu 1430

\# 配置接口VE-L3VPN100的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface ve-l3vpn 100

Sysname-VE-L3VPN100 mtu 1430

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除接口的统计信息。

【命令】

**[reset counters interface** **ve-l2vpn**[ [ *interface-number* \| *interface-number.subnumber* ] \| ]**ve-l3vpn**[[ *interface-number* \| *interface-number.subnumber* ] ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ve-l2vpn**]：清除L2VE接口或子接口的统计信息。

**[ve-l3vpn**]：清除L3VE接口或子接口的统计信息。

*[interface-number*]：L2VE接口或L3VE接口的接口编号，取值为已创建的L2VE接口或L3VE接口的接口编号。

*[interface-number.subnumber*]：L2VE子接口或L3VE子接口的接口编号。其中*interface-number*为主接口编号，取值为已创建的L2VE接口或L3VE接口的接口编号；*subnumber*为子接口编号。该参数的支持情况[及子接口编号的取值范围与设备的型号有关，请以设备的实际情况为准。]

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定接口类型（**ve-l2vpn**和**ve-l3vpn**），则清除所有接口的统计信息；

·如果指定接口类型，不指定接口编号（*interface-number*和*interface-number.subnumber*），则清除所有指定类型接口的统计信息；

·如果同时指定接口类型和接口编号，则清除指定接口的统计信息。

【举例】

\# 清除接口VE-L2VPN100的统计信息。

\<Sysname\> reset counters interface ve-l2vpn 100

\# 清除接口VE-L3VPN100的统计信息。

\<Sysname\> reset counters interface ve-l3vpn 100

【相关命令】

·**display interface**

**L2VPN接入L3VPN或IP骨干网 \-- L2VPN接入L3VPN或IP骨干网配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo** **shutdown**]命令用来开启当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

L2VE接口、L2VE子接口、L3VE接口和L3VE子接口均处于开启状态。

【视图】

L2VE接口视图/L2VE子接口视图/L3VE接口视图/L3VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭接口VE-L2VPN100。

\<Sysname\> system-view

Sysname interface ve-l2vpn 100

Sysname-VE-L2VPN100 shutdown

\# 关闭接口VE-L3VPN100。

\<Sysname\> system-view

Sysname interface ve-l3vpn 100

Sysname-VE-L3VPN100 shutdown
