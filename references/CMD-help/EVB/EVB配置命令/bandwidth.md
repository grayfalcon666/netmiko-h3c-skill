
**EVB \-- EVB配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置当前接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽等于其所属物理端口的缺省最大带宽。

【视图】

S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【举例】

\# 配置S通道接口S-Channel1/0/1:10的期望带宽为2000000kbit/s。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname--S-Channel1/0/1:10bandwidth 2000000

\# 配置S通道聚合接口Schannel-Aggregation1:10的期望带宽为2000000kbit/s。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10bandwidth 2000000

\# 配置VSI接口S-Channel1/0/1:10.1的期望带宽为2000000kbit/s。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10.1

Sysname--S-Channel1/0/1:10.1bandwidth 2000000

\# 配置VSI聚合接口Schannel-Aggregation1:10.1的期望带宽为2000000kbit/s。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10.1

Sysname--Schannel-Aggregation1:10.1bandwidth 2000000

**EVB \-- EVB配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口上的某些配置被恢复为缺省情况后可能会对现有功能产生影响，请在执行本命令之前，完全了解其将对网络产生的影响。

执行本命令之后，可以通过**display** **this**命令来确认效果。对于未能成功恢复为缺省情况的配置，可以查阅相关的命令手册并进行手工恢复。如果手工恢复仍失败，可以通过设备给出的提示信息来定位原因。

【举例】

\# 将S通道接口S-Channel1/0/1:10恢复为缺省配置。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname--S-Channel1/0/1:10 default

\# 将S通道聚合接口Schannel-Aggregation1:10恢复为缺省配置。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10 default

\# 将VSI接口S-Channel1/0/1:10.1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10.1

Sysname--S-Channel1/0/1:10.1 default

\# 将VSI聚合接口Schannel-Aggregation1:10.1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10.1

Sysname--Schannel-Aggregation1:10.1 default

**EVB \-- EVB配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"。比如：S通道接口S-Channel1/0/1:10的缺省描述信息为S-Channel1/0/1:10 Interface，S通道聚合接口Schannel-Aggregation1:10的缺省描述信息为Schannel-Aggregation1:10 Interface，VSI接口S-Channel1/0/1:10.1的缺省描述信息为S-Channel1/0/1:10.1 Interface，VSI聚合接口Schannel-Aggregation1:10.1的缺省描述信息为Schannel-Aggregation1:10.1 Interface。

【视图】

S通道接口视图/S通道聚合接口视图/VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示接口的描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置S通道接口S-Channel1/0/1:10的描述信息为"S-Channel to lab"。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname--S-Channel1/0/1:10description S-Channel to lab

\# 配置S通道聚合接口Schannel-Aggregation1:10的描述信息为"Schannel-Aggregation to lab"。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10description Schannel-Aggregation to lab

\# 配置VSI接口S-Channel1/0/1:10.1的描述信息为"VSI to lab"。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10.1

Sysname--S-Channel1/0/1:10.1description VSI to lab

\# 配置VSI聚合接口Schannel-Aggregation1:10.1的描述信息为"VSI-Aggregation to lab"。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10.1

Sysname--Schannel-Aggregation1:10.1description VSI-Aggregation to lab

**EVB \-- EVB配置命令 \-- display evb cdcp**

------------------------------------------------------------------------

**[display evb cdcp**]命令用来显示CDCP协商信息。

【命令】

**[display evb cdcp** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**] *interface-type interface-number*：显示指定接口（二层以太网接口或二层聚合接口）上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有已使能EVB功能的接口上的信息。

【举例】

\# 显示所有已使能EVB功能的接口上的CDCP协商信息。

\<Sysname\> display evb cdcp

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--Bridge-Aggregation1\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

S-component capability               : Local-supported/Remote-not supported

Supported S-Channel numbers per-port : Local-167/Remote-0

SVID range                           : 2-4094

SCID requested from remote           :

SCID/SVID pair list allocated        :

 \<1, 1\>

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--GigabitEthernet1/0/1\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

S-component capability               : Local-supported/Remote-supported

Supported S-Channel numbers per-port : Local-167/Remote-167

SVID range                           : 2-4094

SCID requested from remote           :

 1, 2, 3, 4, 6, 10, 11, 12, 34, 35, 67

SCID/SVID pair list allocated        :

 \<1, 1\>,         \<2, 3\>,         \<3, 2\>,         \<4, 5\>,         \<6, 4\>,

 \<10, 9\>,        \<11, 6\>,        \<12, 7\>,        \<34, 23\>,       \<35, 35\>,

 \<67, 67\>

表1-1 display evb cdcp命令显示信息描述表

字段

描述

S-component capability

本端和对端对"端口映射的S-VLAN组件"技术的支持情况：

·supported：表示支持

·not supported：表示不支持

Supported S-Channel numbers per-port

本端和对端的接口下支持的S通道数目

SVID range

本端可分配的SVID范围

SCID requested from remote

对端请求的SCID（由小到大排序）

SCID/SVID pair list allocated

本端分配的\<SCID，SVID\>对

**EVB \-- EVB配置命令 \-- display evb evb-tlv**

------------------------------------------------------------------------

**[display evb evb-tlv**]命令用来显示S通道的EVB TLV协商信息。

【命令】

**[display evb evb-tlv ** **interface** *interface-type* ]*channel-id* }

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**]：显示指定接口上的信息。如果未指定本参数，将显示所有已使能EVB功能的接口上的信息。

*[interface-type * { *interface-number* \| *interface-number*:*channel-id* }]：表示二层以太网接口、二层聚合接口、S通道接口或S通道聚合接口。其中，*interface-type*为接口类型，*interface-number*为接口编号，*channel-id*为S通道的编号。对于二层以太网接口和二层聚合接口，接口编号为*interface-number*的形式；对于S通道接口和S通道聚合接口，接口编号为*interface-number*:*channel-id*的形式。

【举例】

\# 显示端口GigabitEthernet1/0/1上S通道的EVB TLV协商信息。

\<Sysname\> display evb evb-tlv interface gigabitethernet 1/0/1

S-Channel1/0/1:1

EVB mode                       : Local-bridge/Remote-station

BGID status                    : Supported

Local RR capability            : Supported

Local RR status                : Disabled

Remote SGID status             : Not supported

Remote RR request status       : Not requested

Remote RR status               : Unknown

Max ECP retry time             : Local-3/Remote-NA/Operative-3

ULPDU retransmission exponent  : Local-16/Remote-NA/Operative-16

Resource wait-delay exponent   : Local-20/Remote-NA/Operative-20

Reinit Keep-alive exponent     : Local-25/Remote-NA/Operative-25

S-Channel1/0/1:100

EVB mode                       : Local-bridge/Remote-station

BGID status                    : Supported

Local RR capability            : Supported

Local RR status                : Disabled

Remote SGID status             : Not supported

Remote RR request status       : Not requested

Remote RR status               : Unknown

Max ECP retry time             : Local-3/Remote-NA/Operative-3

ULPDU retransmission exponent  : Local-16/Remote-NA/Operative-16

Resource wait-delay exponent   : Local-20/Remote-NA/Operative-20

Reinit keep-alive exponent     : Local-25/Remote-NA/Operative-25

表1-2 display evb evb-tlv命令显示信息描述表

字段

描述

EVB mode

本地和对端的EVB模式：

·bridge：表示EVB交换机

·station：表示EVB服务器

BGID status

本端是否支持Group ID：

·Supported：表示支持

·Not supported：表示不支持

Local RR capability

本端是否支持RR模式：

·Supported：表示支持

·Not supported：表示不支持

Local RR status

协商后本端的RR模式

Remote SGID status

对端是否支持Group ID：

·Supported：表示支持

·Not supported：表示不支持

Remote RR request status

对端是否申请了RR模式：

·Requested：表示已申请

·Not requested：表示未申请

Remote RR status

协商后对端是否启用了RR模式：

·Enabled：表示已启用

·Disabled：表示未启用

·Unknown：表示未知

Max ECP retry time

ECP最大重传次数，格式为：本端协商值/对端协商值/实际操作值，NA表示对端没有设置值

ULPDU retransmission Eexponent

ECP重传时间指数因子，格式为：本端协商值/对端协商值/实际操作值，NA表示对端没有设置值

Resource wait-delay exponent

VDP等待应答时间指数因子，格式为：本端协商值/对端协商值/实际操作值，NA表示对端没有设置值

Reinit keep-alive exponent

VDP保活时间指数因子，格式为：本端协商值/对端协商值/实际操作值，NA表示对端没有设置值

**EVB \-- EVB配置命令 \-- display evb s-channel**

------------------------------------------------------------------------

**[display evb s-channel**]命令用来显示S通道信息。

【命令】

**[display evb s-channel** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**]* interface-type interface-number*：显示指定接口（二层以太网接口或二层聚合接口）上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有已使能EVB功能的接口上的信息。

【举例】

\# 显示端口GigabitEthernet1/0/1上的S通道信息。

\<Sysname\> display evb s-channel interface gigabitethernet 1/0/1

RR status: D \-- Disabled, E \-- Enabled

MAC learning: A \-- Allowed, F \-- Forbidden

S-Channel           SVID    Uptime               RR      MAC       VSI

interface                   yyyy/mm/dd hh:mm:ss  status  learning  number

S-Ch1/0/1:1         1       2012/12/17 03:43:13  D       A         0

S-Ch1/0/1:100       100     2012/12/17 03:43:14  D       A         2

表1-3 display evb s-channel命令显示信息描述表

字段

描述

S-Channel interface

S通道接口的名称

SVID

S通道对应的S-VLAN编号

Uptime

S通道的创建时间

RR status

S通道反射式转发模式的状态：

·D：Disabled，表示关闭

·E：Enabled，表示开启

MAC learning

S通道的MAC地址学习能力：

·A：Allowed，表示允许学习

·F：Forbidden，表示禁止学习

VSI number

S通道上创建的VSI接口数量

**EVB \-- EVB配置命令 \-- display evb summary**

------------------------------------------------------------------------

**[display** **evb** **summary**]命令用来显示EVB概要信息。

【命令】

**[display**] **evb** **summary**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示EVB概要信息。

\<Sysname\>display evb summary

Default manager ID: 192.168.1.1

Port number: 80

Interface               S-Channel number        VSI number

GE1/0/1                 2                       2

表1-4 display evb summary命令显示信息描述表

字段

描述

Default manager ID

默认VSI管理服务器的地址或名称，Not configured表示没有配置

Port number

默认VSI管理服务器的端口编号，Not configured表示没有配置

Interface

使能了EVB功能的接口名称

S-Channel number

S通道的数量

VSI number

VSI接口的数量

**EVB \-- EVB配置命令 \-- display evb vsi**

------------------------------------------------------------------------

**[display evb vsi**]命令用来显示VSI接口信息。

【命令】

**[display evb vsi** [ **verbose**   **interface** *interface-type* *channel-id**[\| interface-number]*:*channel-id*.*vsi-local-id*} ]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

**[interface**]：显示指定接口上的信息。如果未指定本参数，将显示所有已使能EVB功能的接口上的信息。

*[interface-type * { *interface-number* \| *interface-number*:*channel-id* *\| interface-number*:*channel-id*.*vsi-local-id* }]：表示二层以太网接口、二层聚合接口、S通道接口、S通道聚合接口、VSI接口或VSI聚合接口。其中，*interface-type*为接口类型，*interface-number*为接口编号，*channel-id*为S通道的编号，*vsi-local-id*为VSI本地编号。对于二层以太网接口和二层聚合接口，接口编号为*interface-number*的形式；对于S通道接口和S通道聚合接口，接口编号为*interface-number*:*channel-id*的形式；对于VSI接口和VSI聚合接口，接口编号为*interface-number*:*channel-id*.*vsi-local-id*的形式。

【举例】

\# 显示端口GigabitEthernet1/0/1上的VSI接口概要信息。

\<Sysname\> display evb vsi interface gigabitethernet 1/0/1

Status: A \-- Association, P \-- Pre-association

VSI                     VTID     Type      Instance                Status

interface                        version   ID

S-Ch1/0/1:100.0         NA       NA        NA                      P

S-Ch1/0/1:100.1         NA       NA        NA                      A

\# 显示端口GigabitEthernet1/0/1上的VSI接口详细信息。

\<Sysname\> display evb vsi verbose interface gigabitethernet 1/0/1

S-Channel1/0/1:100

 S-Channel1/0/1:100.0

  VSI local-ID: 0           VSI type ID: NA         VSI type version: NA

  VSI instance ID: NA

  VSI manager ID: NA

  Current VDP status: Pre-association

  Filter type: VID

  Filter info:

  \<100\>

 S-Channel1/0/1:100.1

  VSI local-ID: 1           VSI type ID: 100        VSI type version: 0

  VSI instance ID: 11:2233:4455:6677:8899:1234:5678:9010

  VSI manager ID: NA

  Current VDP status: Association

  Filter type: MAC/VID

  Filter info:

  \<0011-2233-4455, 1000\>

表1-5 display evb vsi命令显示信息描述表

字段

描述

VSI interface

VSI接口的名称

VTID/VSI type ID

VSI类型编号，NA表示未指定

Type version/VSI type version

VSI类型版本号，NA表示未指定

Instance ID/VSI instance ID

VSI实例编号，NA表示未指定

Status

VSI接口的当前状态：

·A：即Association，表示关联属性

·P：即Pre-association，表示预关联属性

VSI local-ID

VSI本地编号

VSI manager ID

VSI管理服务器的地址，NA表示未指定

Current VDP status

VSI接口的当前状态：

·Association：表示关联属性

·Pre-association：表示预关联属性

Filter type

VSI过滤信息的类型：

·GroupID/VID：表示Group ID和VLAN ID的组合

·GroupID/MAC/VID：表示Group ID、MAC地址和VLAN ID的组合

·VID：表示VLAN ID

·MAC/VID：表示MAC地址和VLAN ID的组合

Filter info

VSI过滤信息的具体内容

**EVB \-- EVB配置命令 \-- display interface**

------------------------------------------------------------------------

**[display** **interface**]命令用来显示S通道接口/S通道聚合接口/VSI接口/VSI聚合接口的相关信息。

【命令】

**[display** **interface** \**[s-channel**[\| **schannel-aggregation** }   *interface-number*:*channel-id[ \| interface-number]*:*channel-id*.*vsi-local-id*    **brief** [ **description** \| **down** ] ]]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[s-channel**]：显示指定S通道接口或VSI接口的信息。

**[schannel-aggregation**]：显示指定S通道聚合接口或VSI聚合接口的信息。

*[interface-number*]:*channel-id*：表示S通道接口或S通道聚合接口的编号。其中，*interface-number*为S通道所在接口的编号，*channel-id*为S通道的编号。

*[interface-number*]:*channel-id*.*vsi-local-id*：表示VSI接口或VSI聚合接口的编号。其中，*interface-number*为S通道所在接口的编号，*channel-id*为S通道的编号，*vsi-local-id*为VSI本地编号。

**[brief**]：显示概要信息。如果未指定本参数，将显示详细信息。

**[description**]：当用户配置的接口描述信息超过27个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前27个字符，超出部分不会显示。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果未指定本参数，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果未指定接口类型，将显示设备支持的所有接口的信息。

·如果指定了接口类型而未指定接口编号，将显示所有已创建的S通道接口和VSI接口的信息。

【举例】

\# 显示S通道接口S-Channel1/0/1:10的详细信息。

\<Sysname\> display interface s-channel 1/0/1:10

S-Channel1/0/1:10

Current state: UP

IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 000c-29f9-366e

Description: S-Channel1/0/1:10 Interface

Bandwidth: 1000000kbps

Unknown-speed mode, unknown-duplex mode

Link speed type is autonegotiation, link duplex type is autonegotiation

PVID: 1

Port link-type: trunk

 VLAN Passing:   1(default vlan), 2

 VLAN permitted: 1(default vlan), 2

 Trunk port encapsulation: IEEE 802.1q

Last clearing of counters: Never

Input (total):  6 packets, 384 bytes

Output (total):  18 packets, 1152 bytes

\# 显示S通道接口S-Channel1/0/1:10的概要信息。

\<Sysname\> display interface s-channel 1/0/1:10 brief

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

S-Ch1/0/1:10         UP   10G(a)  F(a)   A    1

\# 显示VSI接口S-Channel1/0/1:10.1的详细信息。

\<Sysname\> display interface s-channel 1/0/1:10.1

S-Channel1/0/1:10.1

Current state: UP

IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 000c-29f9-366e

Description: S-Channel1/0/1:10.1 Interface

Bandwidth: 1000000kbps

Last clearing of counters: Never

\# 显示VSI接口S-Channel1/0/1:10.1的概要信息。

\<Sysname\> display interface s-channel 1/0/1:10.1 brief

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

S-Ch1/0/1:10.1       UP   \--      \--     \--   \--

\# 显示所有物理状态为down的S通道接口和VSI接口的概要信息。

\<Sysname\> display interface s-channel brief down

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

S-Ch1/0/1:11         DOWN Not connected

S-Ch1/0/1:11.1       DOWN Not connected

表1-6 display interface s-channel命令显示信息描述表

字段

描述

Current state

接口的状态：

·Administratively DOWN：表示管理状态为关闭

·DOWN：表示管理状态为开启，但物理状态为关闭

·UP：表示管理状态和物理状态均为开启

IP Packet Frame Type

IP报文的帧格式

Hardware Address

接口的硬件地址

Description

接口的描述信息

Bandwidth

接口的期望带宽

Unknown-speed mode, unknown-duplex mode

接口的速率和双工模式均未知

Link speed type is autonegotiation, link duplex type is autonegotiation

接口的速率和双工模式都是通过自协商确定的

PVID

接口缺省VLAN的编号

Port link-type

接口的链路类型

Trunk port encapsulation

Trunk端口的封装类型

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口统计信息的时间。Never表示设备启动后从未清除过

Input (total):  6 packets, 384 bytes

接口接收的报文总数和字节总数

Output (total):  18 packets, 1152 bytes

接口发送的报文总数和字节总数

Brief information on interface(s) under bridge mode

二层接口的概要信息

Interface

接口名称的缩写

Link

接口的物理连接状态：

·UP：表示接口在物理上连通

·DOWN：表示接口在物理上不通

·ADM：表示接口被手工关闭，需执行**undo** **shutdown**命令才能打开

·Stby：表示接口为备份接口，可使用**display** **interface-backup** **state**命令查看其主接口

Speed

接口的速率，单位为bps

Duplex

接口的双工模式：

·(a)/A：表示速率和双工模式都由自协商确定

·H：表示双工模式为半双工

·F：表示双工模式为全双工

Type

接口的链路类型：

·A：表示Access类型

·H：表示Hybrid类型

·T：表示Trunk类型

Cause

接口物理状态为down的原因：

·Administratively：表示链路被手工关闭（通过**shutdown**命令），需执行**undo** **shutdown**命令才能恢复其真实物理状态

·Not connected：表示没有物理连接（因未插网线或网线故障）

【相关命令】

·**reset counters interface**

**EVB \-- EVB配置命令 \-- evb default-manager**

------------------------------------------------------------------------

**[evb default-manager**]命令用来指定默认VSI管理服务器。

**[undo evb default-manager**]命令用来恢复缺省情况。

【命令】

**[evb default-manager**[ { { **ip** *ip-address* \| **ipv6** *ipv6-address* \| **name** *name* } [ **port** *port-number* ] \| **local-server** }]]

**[undo evb default-manager**]

【缺省情况】

未指定默认VSI管理服务器。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip**] *ip-address*：指定默认VSI管理服务器的IPv4地址。

**[ipv6**] *ipv6-address*：指定默认VSI管理服务器的IPv6地址。

**[name**] *name*：指定默认VSI管理服务器的名称，*name*为1～127个字符的字符串，不区分大小写。

**[port**] *port-number*：指定默认VSI管理服务器的端口，*port-number*为端口编号，取值范围为0～65535，缺省值为8080。

**[local-server**]：指定本设备为默认VSI管理服务器。

【使用指导】

当交换机收到服务器发来的VDP报文（不包括去关联请求报文）时，需要与VSI管理服务器进行通信以申请VSI接口的资源和策略。VDP报文中的VSI manager ID TLV用于携带VSI管理服务器的地址，如果交换机收到的VDP报文中此TLV为全0（即未携带VSI管理服务器的地址），则使用通过本命令指定的默认VSI管理服务器。

【举例】

\# 指定默认VSI管理服务器的IPv4地址为192.168.100.20。

\<Sysname\> system-view

Sysname evb default-manager ip 192.168.100.20

**EVB \-- EVB配置命令 \-- evb enable**

------------------------------------------------------------------------

**[evb enable**]命令用来在接口上使能EVB功能。

**[undo evb enabl**]**e**命令用来在接口上关闭EVB功能。

【命令】

**[evb enable**]

**[undo evb enable**]

【缺省情况】

接口上的EVB功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·不允许在聚合组的成员端口上使能EVB功能或将已使能EVB功能的端口加入聚合组，否则系统将提示出错。

·在接口上使能EVB功能之前，建议先将该接口上的所有配置都恢复为缺省情况。

·在接口上使能EVB功能之后，该接口上将自动创建默认S通道（SCID和SVID均为1，对应S通道接口/S通道聚合接口的链路类型为Access类型）。

·在已使能EVB功能的接口上，不建议进行VLAN配置或运行其它二层协议。

·在接口上关闭EVB功能之前，请先删除该接口上的所有非默认S通道，默认S通道将在关闭EVB功能时被自动删除。

·不要在同一接口上同时使能EVB功能和QinQ功能，否则二者均将无法正常工作。

·不要在同一接口上同时创建以太网服务实例和使能EVB功能，否则二者均将无法正常工作。

【举例】

\# 在端口GigabitEthernet1/0/1上使能EVB功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 evb enable

\# 在二层聚合接口Bridge-Aggregation1上使能EVB功能。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 evb enable

【相关命令】

·**evb s-channel**

·**qinq enable**（二层技术-以太网交换命令参考/QinQ）

·**service-instance**（MPLS命令参考/VPLS）

**EVB \-- EVB配置命令 \-- evb mac-learning forbidden**

------------------------------------------------------------------------

**[evb mac-learning forbidden**]命令用来关闭S通道的MAC地址学习能力。

**[undo evb mac-learning forbidden**]命令用来开启S通道的MAC地址学习能力。

【命令】

**[evb mac-learning forbidden**]

**[undo evb mac-learning forbidden**]

【缺省情况】

S通道的MAC地址学习能力处于开启状态。

【视图】

S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·对于已关闭RR模式的S通道，请勿再关闭其MAC地址学习能力，否则可能导致相应的虚拟机流量不通。

·关闭了S通道的MAC地址学习能力之后，源MAC地址未知的报文将被丢弃。

·当使用**undo evb mac-learning forbidden**命令开启S通道的MAC地址学习能力时，请确保该S通道的MAC地址学习功能也处于开启状态（即**mac-address** **mac-learning** **enable**），否则可能导致该S通道内的流量不通。

【举例】

\# 在S通道接口S-Channel1/0/1:10上关闭MAC地址学习能力。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname-S-Channel1/0/1:10 evb mac-learning forbidden

\# 在S通道聚合接口Schannel-Aggregation1:10上关闭MAC地址学习能力。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10 evb mac-learning forbidden

【相关命令】

·**evb reflective-relay**

·**mac-address** **mac-learning** **enable**（二层技术-以太网交换命令参考/MAC地址表）

**EVB \-- EVB配置命令 \-- evb reflective-relay**

------------------------------------------------------------------------

**[evb reflective-relay**]命令用来开启S通道的RR模式。

**[undo evb reflective-relay**]命令用来关闭S通道的RR模式。

【命令】

**[evb reflective-relay**]

**[undo evb reflective-relay**]

【缺省情况】

S通道的RR模式处于关闭状态。

【视图】

S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通常，服务器和交换机之间通过EVB TLV协商是否开启S通道的RR模式。当服务器在EVB TLV中申请开启RR模式、且交换机也支持该模式时，系统将自动为S通道开启RR模式，并转化为交换机上相应的命令行；用户也可通过本命令进行手工配置。

【举例】

\# 在S通道接口S-Channel1/0/1:10上开启RR模式。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname-S-Channel1/0/1:10 evb reflective-relay

\# 在S通道聚合接口Schannel-Aggregation1:10上开启RR模式。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10 evb reflective-relay

**EVB \-- EVB配置命令 \-- evb s-channel**

------------------------------------------------------------------------

**[evb s-channel**]命令用来在接口上创建S通道。

**[undo evb s-channel**]命令用来在接口上删除S通道。

【命令】

**[evb s-channel**]* channel-id* [ **service-vlan** *svlan-id* ]

**[undo evb s-channel** *channel-id*]

【缺省情况】

已使能EVB功能的接口上只存在自动创建的默认S通道（SCID和SVID均为1）。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[channel-id*]：表示S通道的编号，即SCID，取值范围为2～167（0为保留的SCID，1为默认的SCID，均不可配）。

*[svlan-id*]：表示S-VLAN的编号，即SVID，取值范围为2～4094（1为默认S通道所使用的SVID，不可配）。如果未指定本参数，系统将自动分配一个尚未被其它S通道使用的最小SVID。

【使用指导】

S通道通常由服务器和交换机之间通过CDCP协议协商自动创建，系统会将自动创建的结果转化为交换机上相应的命令行；用户也可以通过本命令手工创建S通道。当自动创建和手工创建的S通道的\<SCID，SVID\>对冲突时，系统将优先采用自动创建的配置。

S通道创建成功后，系统将自动创建对应的S通道接口/S通道聚合接口；删除S通道的同时也将自动删除对应的S通道接口/S通道聚合接口。手工创建的S通道接口/S通道聚合接口的链路类型为Access类型，而自动创建的S通道接口/S通道聚合接口的链路类型则为Trunk类型。

S通道如果创建在二层以太网接口上，则其对应的接口称为S通道接口；S通道如果创建在二层聚合接口上，则其对应的接口称为S通道聚合接口。

需要注意的是：

·必须在已使能EVB功能的接口上创建S通道，否则系统将提示出错。

·手工创建S通道时，不允许使用已被其它S通道占用的SCID或SVID，否则系统将提示出错。

·请避免自动创建/删除S通道与手工创建/删除S通道同时进行，否则可能造成S通道创建/删除结果异常。

【举例】

\# 在端口GigabitEthernet1/0/1上创建SCID为10的S通道，其对应的SVID为5。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 evb s-channel 10 service-vlan 5

\# 在二层聚合接口Bridge-Aggregation1上创建SCID为10的S通道，其对应的SVID为5。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 evb s-channel 10 service-vlan 5

【相关命令】

·**evb enable**

·**interface**

**EVB \-- EVB配置命令 \-- evb vdp timer keepalive exponent**

------------------------------------------------------------------------

**[evb vdp timer keepalive exponent**]命令用来配置VDP保活时间指数因子。

**[undo evb vdp timer keepalive exponent**]命令用来恢复缺省情况。

【命令】

**[evb vdp timer keepalive exponent ***value*]

**[undo evb vdp timer keepalive exponent**]

【缺省情况】

VDP保活时间指数因子为20。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：表示VDP保活时间指数因子，取值范围为14～31。

【使用指导】

VDP保活时间＝1.5× [ 2^VDP^^保活时间指数因子^＋（2×ECP最大重传次数＋1）×2^ECP^^重传时间指数因子^  ]×10^---5^（秒），用户在配置时可参考[表]1-7(?-620347954#_Ref319417533)中的实际取值。

!(EVB命令.files/image001.png)

[表]1-7(?-620347954#_Ref319417533)在计算时分别采用3和14作为"ECP最大重传次数"和"ECP重传时间指数因子"的取值。但这两个值仅仅是未与服务器协商时，交换机上的缺省值。在实际应用中，这两个参数将取交换机与服务器通过EVB TLV协商后的较大值，此时[表]1-7(?-620347954#_Ref319417533)可能失去参考价值。

表1-7 VDP保活时间取值对照表

VDP保活时间指数因子

计算值（秒）

实际取值（秒）

14

1.96608

2

15

2.21184

3

16

2.70336

3

17

3.68640

4

18

5.65248

6

19

9.58464

10

20

17.44896

18

21

33.17760

34

22

64.63488

65

23

127.54944

128

24

253.37856

254

25

505.03680

506

26

1008.35328

1009

27

2014.98624

2015

28

4028.25216

4029

29

8054.78400

8055

30

16107.84768

16108

31

32213.97504

32214

【举例】

\# 在端口GigabitEthernet1/0/1上配置VDP保活时间指数因子为23。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 evb vdp timer keepalive exponent 23

\# 在二层聚合接口Bridge-Aggregation1上配置VDP保活时间指数因子为23。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 evb vdp timer keepalive exponent 23

**EVB \-- EVB配置命令 \-- evb vdp timer resource-wait-delay exponent**

------------------------------------------------------------------------

**[evb vdp timer resource-wait-delay exponent**]命令用来配置VDP等待应答时间指数因子。

**[undo evb vdp timer resource-wait-delay exponent**]命令用来恢复缺省情况。

【命令】

**[evb vdp timer resource-wait-delay exponent*** value*]

**[undo evb vdp timer resource-wait-delay exponent**]

【缺省情况】

VDP等待应答时间指数因子为20。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：表示VDP等待应答时间指数因子，取值范围为15～31。

【使用指导】

VDP等待应答时间＝2^VDP^^等待应答时间指数因子^×10^---5^（秒），用户在配置时可参考[表]1-8(?388226591#_Ref319417523)中的实际取值。

表1-8 VDP等待应答时间取值对照表

VDP等待应答时间指数因子

计算值（秒）

实际取值（秒）

15

0.32768

1

16

0.65536

1

17

1.31072

2

18

2.62144

3

19

5.24288

6

20

10.48576

11

21

20.97152

21

22

41.94304

42

23

83.88608

84

24

167.77216

168

25

335.54432

336

26

671.08864

672

27

1342.17728

1343

28

2684.35456

2685

29

5368.70912

5369

30

10737.41824

10738

31

21474.83648

21475

【举例】

\# 在端口GigabitEthernet1/0/1上配置VDP等待应答时间指数因子为23。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 evb vdp timer resource-wait-delay exponent 23{.TerminalDisplayChar}

\# 在二层聚合接口Bridge-Aggregation1上配置VDP等待应答时间指数因子为23。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 evb vdp timer resource-wait-delay exponent 23{.TerminalDisplayChar}

**EVB \-- EVB配置命令 \-- evb vsi**

------------------------------------------------------------------------

**[evb vsi**]命令用来创建VSI接口/VSI聚合接口。

**[undo evb vsi**]命令用来删除VSI接口/VSI聚合接口。

【命令】

**[evb vsi**[ *vsi-local-id* { **association** \| **pre-association** }]]

**[undo evb vsi** *vsi-local-id*]

【缺省情况】

S通道中不存在任何VSI接口/VSI聚合接口。

【视图】

S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-local-id*]：表示VSI本地编号，用于VSI接口名，取值范围为0～1023。

**[association**]：表示关联属性。关联属性VSI接口下的过滤信息会立即生效。

**[pre-association**]：表示预关联属性。预关联属性VSI接口下的过滤信息中，VLAN信息会立即生效，而\<VLAN，MAC\>信息只有当该接口转换为关联属性时才会生效。

【使用指导】

·通过本命令在S通道接口上创建的接口称为VSI接口，在S通道聚合接口上创建的接口称为VSI聚合接口。

·通常，VSI接口/VSI聚合接口由VSI管理服务器下发创建或删除；用户也可通过本命令手工创建或删除VSI接口，或者修改其关联/预关联属性。

·VSI接口/VSI聚合接口为S通道接口/S通道聚合接口的子接口，删除S通道的同时也将删除其下的所有VSI接口/VSI聚合接口。

·当手工将VSI接口/VSI聚合接口由关联属性改为预关联属性时，如果虚拟机的流量特征中有MAC地址信息，则此MAC地址将从交换机的驱动中删除，虚拟机的流量可能中断。当手工将VSI接口由预关联属性改为关联属性时，交换机将设置该虚拟机的MAC地址，如果该虚拟机尚未就绪，可能会出错。

·VSI接口/VSI聚合接口创建成功后，用户可通过**interface**命令进入其视图。

【举例】

\# 在S通道接口S-Channel1/0/1:10上创建VSI本地编号为1、属性为关联属性的VSI接口。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname-S-Channel1/0/1:10 evb vsi 1 association

\# 在S通道聚合接口Schannel-Aggregation1:10上创建VSI本地编号为1、属性为关联属性的VSI聚合接口。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10 evb vsi 1 association

【相关命令】

·**evb s-channel**

·**evb vsi filter**

·**interface**

**EVB \-- EVB配置命令 \-- evb vsi active**

------------------------------------------------------------------------

**[evb vsi active**]命令用来激活VSI接口/VSI聚合接口。

**[undo evb vsi active**]命令用来取消激活VSI接口/VSI聚合接口。

【命令】

**[evb vsi** **active**]

**[undo evb vsi** **active**]

【缺省情况】

VSI接口/VSI聚合接口未激活。

【视图】

VSI接口视图/VSI聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当VSI接口/VSI聚合接口激活后，流量监管（请参见"ACL和QoS配置指导"中的"QoS"）等配置才会生效；而当VSI接口/VSI聚合接口未激活时，流量监管等配置不会生效，此时不建议对该接口进行除VSI过滤信息以外的其它配置。

需要注意的是，在配置了VSI过滤信息之后，才允许激活VSI接口/VSI聚合接口；而在删除VSI过滤信息之前，必须先将已激活的VSI接口/VSI聚合接口取消激活。

【举例】

\# 激活VSI接口S-Channel1/0/1:10.1。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10.1

Sysname--S-Channel1/0/1:10.1 evb vsi active

\# 激活VSI聚合接口Schannel-Aggregation1:10.1。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10.1

Sysname--Schannel-Aggregation1:10.1 evb vsi active

【相关命令】

·**evb vsi filter**

**EVB \-- EVB配置命令 \-- evb vsi filter**

------------------------------------------------------------------------

**[evb vsi filter**]命令用来配置VSI过滤信息。

**[undo evb vsi filter**]命令用来删除VSI过滤信息。

【命令】

**[evb vsi filter ** **group** *group-id* ] **vlan** *vlan-id*  **mac** *mac-address*

**[undo evb vsi filter** [ **group** *group-id*   **vlan** *vlan-id* [ **mac** *mac-address*  ]]]

【缺省情况】

不存在任何VSI过滤信息。

【视图】

VSI接口视图/VSI聚合接口

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group**] *group-id*：表示组编号，取值范围为1～4094。本参数用于为VLAN分组，即当要使用的VLAN数量超过4094个时，可通过由Group ID和VLAN ID共同标识一个VLAN的方式来扩充VLAN的可用数量。

**[vlan**] *vlan-id*：表示VLAN的编号，取值范围为1～4094，该VLAN必须存在。

**[mac**] *mac-address*：表示MAC地址，必须为有效的单播MAC地址。

【使用指导】

VSI过滤信息是用来标识虚拟机上VSI流量特征的信息，EVB交换机通过该信息来识别虚拟机上VSI的流量。VSI过滤信息通常由VSI管理服务器下发，用户也可以通过本命令手工创建或删除。VSI过滤信息分为两种：流量所属的VLAN，或者流量的目的MAC地址及其所属VLAN的组合。

VSI过滤信息中有三个参数：流量所属的VLAN，流量所属VLAN所在的组，以及流量的目的MAC地址。由这三个参数形成了以下四种VSI过滤信息的组合：

·VLAN ID

·VLAN ID + MAC

·Group ID + VLAN ID

·Group ID + VLAN ID + MAC

需要注意的是：

·在VSI接口/VSI聚合接口上配置VSI过滤信息之前，必须将该VSI接口/VSI聚合接口所属S通道接口/S通道聚合接口的链路类型配置为Trunk类型，否则VSI过滤信息的配置将失败。

·当在某VSI接口/VSI聚合接口上配置VSI过滤信息时，如果该VSI接口/VSI聚合接口所属S通道接口/S通道聚合接口（或此S通道所属接口）尚未允许VSI过滤信息中所包含的VLAN通过，则该S通道接口/S通道聚合接口（或此S通道所属接口）将自动允许此VLAN通过；当在某VSI接口/VSI聚合接口上删除包含某VLAN的VSI过滤信息时，如果该VSI接口/VSI聚合接口所属S通道接口/S通道聚合接口（或此S通道所属接口）下所有VSI接口/VSI聚合接口上的其它VSI过滤信息中都不包含此VLAN，则该S通道接口/S通道聚合接口（或此S通道所属接口）将自动禁止此VLAN通过。

·当一个VSI接口/VSI聚合接口上配置的VSI过滤信息中已包含某VLAN时，不允许在该VSI接口/VSI聚合接口或其所属S通道接口/S通道聚合接口下的其它VSI接口/VSI聚合接口上再配置包含该VLAN的VSI过滤信息，否则系统将提示出错。

·如果VSI过滤信息为流量所属的VLAN，但用户手工关闭了相应S通道的MAC地址学习能力，将导致VSI流量无法转发。

·在配置了VSI过滤信息之后，才允许激活VSI接口/VSI聚合接口；而在删除VSI过滤信息之前，必须先取消激活VSI接口/VSI聚合接口。

【举例】

\# 在VSI接口S-Channel1/0/1:10.1上配置VLAN 1的过滤信息。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10.1

Sysname--S-Channel1/0/1:10.1 evb vsi filter vlan 1

\# 在VSI聚合接口Schannel-Aggregation1:10.1上配置VLAN 1的过滤信息。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10.1

Sysname--Schannel-Aggregation1:10.1 evb vsi filter vlan 1

【相关命令】

·**evb mac-learning forbidden**

·**evb vsi ****active**

**EVB \-- EVB配置命令 \-- interface**

------------------------------------------------------------------------

**[interface**]命令用来进入S通道接口/S通道聚合接口/VSI接口/VSI聚合接口视图。

【命令】

**[interface ****s-channel**[\| **schannel-aggregation** } ]*[channel-id[ \| interface-number]*:*channel-id*.*vsi-local-id* }

【视图】]

系统视图]

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[s-channel**]：进入S通道接口或VSI接口。

**[schannel-aggregation**]：进入S通道聚合接口或VSI聚合接口。

*[interface-number*]:*channel-id*：表示S通道接口或S通道聚合接口的编号。其中，*interface-number*为S通道所在接口的编号，*channel-id*为S通道的编号。

*[interface-number*]:*channel-id.vsi-local-id*：表示VSI接口或VSI聚合接口的编号。其中，*interface-number*为S通道所在接口的编号，*channel-id*为S通道的编号，*vsi-local-id*为VSI本地编号。

【举例】

\# 进入S通道接口S-Channel1/0/1:10的视图。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname--S-Channel1/0/1:10

\# 进入S通道聚合接口Schannel-Aggregation1:10的视图。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10

\# 进入VSI接口S-Channel1/0/1:10.1的视图。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10.1

Sysname--S-Channel1/0/1:10.1

\# 进入VSI聚合接口Schannel-Aggregation1:10.1的视图。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10.1

Sysname--Schannel-Aggregation1:10.1

**EVB \-- EVB配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除S通道接口/S通道聚合接口/VSI接口/VSI聚合接口上的统计信息。

【命令】

**[reset counters interface** \**[s-channel**[\| **schannel-aggregation** }   *interface-number*:*channel-id[ \| interface-number]*:*channel-id*.*vsi-local-id*  ]]

【视图】]

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[s-channel**]：清除指定S通道接口或VSI接口的信息。

**[schannel-aggregation**]：清除指定S通道聚合接口或VSI聚合接口的信息。

*[interface-number*]:*channel-id*：表示S通道接口或S通道聚合接口的编号。其中，*interface-number*为S通道所在接口的编号，*channel-id*为S通道的编号。

*[interface-number*]:*channel-id*.*vsi-local-id*：表示VSI接口或VSI聚合接口的编号。其中，*interface-number*为S通道所在接口的编号，*channel-id*为S通道的编号，*vsi-local-id*为VSI本地编号。

【使用指导】

·在某些情况下，需要统计一定时间内某S通道接口/S通道聚合接口/VSI接口/VSI聚合接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。

·如果未指定接口类型和接口编号，将清除所有接口上的统计信息。

·如果指定了接口类型而未指定接口编号，将清除所有已创建的S通道/S通道聚合接口/VSI接口/VSI聚合接口的相关信息。

【举例】

\# 清除S通道接口S-Channel1/0/1:10上的统计信息。

\<Sysname\> reset counters interface s-channel 1/0/1:10

\# 清除S通道聚合接口Schannel-Aggregation1:10上的统计信息。

\<Sysname\> reset counters interface schannel-aggregation 1:10

\# 清除VSI接口S-Channel1/0/1:10.1上的统计信息。

\<Sysname\> reset counters interface s-channel 1/0/1:10.1

\# 清除VSI聚合接口Schannel-Aggregation1:10.1上的统计信息。

\<Sysname\> reset counters interface schannel-aggregation 1:10.1

【相关命令】

·**display** **interface**

**EVB \-- EVB配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo shutdown**]命令用来打开当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于开启状态。

【视图】

S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭S通道接口S-Channel1/0/1:10。

\<Sysname\> system-view

Sysname interface s-channel 1/0/1:10

Sysname--S-Channel1/0/1:10shutdown

\# 关闭S通道聚合接口Schannel-Aggregation1:10。

\<Sysname\> system-view

Sysname interface schannel-aggregation 1:10

Sysname--Schannel-Aggregation1:10 shutdown
