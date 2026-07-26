
**FC和FCoE \-- FCoE模式配置命令 \-- display fcoe-mode**

------------------------------------------------------------------------

**[display fcoe-mode**]命令用来显示交换机的FCoE模式。

【命令】

**[display fcoe-mode**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示交换机的FCoE模式。

\<Sysname\> display fcoe-mode

The FCoE mode is NONE.

表1-1 display fcoe-mode命令显示信息描述表

字段

描述

The FCoE mode is *mode*.

交换机的FCoE模式为*mode*，*mode*包括：

·FCF：FCF模式

·FCF-NPV：FCF-NPV模式

·NPV：NPV模式

·TRANSIT：Transit模式

·NONE：非FCoE模式

【相关命令】

·**fcoe-mode**

**FC和FCoE \-- FCoE模式配置命令 \-- fcoe-mode**

------------------------------------------------------------------------

**[fcoe-mode**]命令用来配置交换机的FCoE模式。

**[undo fcoe-mode**]命令用来恢复缺省情况。

【命令】

**[fcoe-mode**[ { **fcf** \| **fcf-npv** \| **npv** \| **transit** }]]

**[undo fcoe-mode**]

【缺省情况】

交换机工作在非FCoE模式下。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fcf**]：FCF模式。

**[fcf-npv**]：FCF-NPV模式。

**[npv**]：NPV模式。

**[transit**]：Transit模式。

【使用指导】

一台具备FC和FCoE能力的交换机，既可工作在非FCoE模式下，也可工作在FCoE模式下。其中，FCoE模式又分为以下四种：

·FCF模式：工作在本模式的交换机称为FCF交换机，其接口支持E模式和F模式，分别称为E_Port和F_Port。FCF交换机可通过E_Port连接其它交换机的E_Port，或者通过F_Port连接节点设备的N_Port或其它交换机的NP_Port。

·NPV模式：工作在本模式的交换机称为NPV交换机，其接口支持F模式和NP模式，分别称为F_Port和NP_Port。NPV交换机可通过F_Port连接节点设备的N_Port或其它交换机的NP_Port，或着通过NP_Port连接其它交换机的F_Port。

·FCF-NPV模式：工作在本模式的交换机称为FCF-NPV交换机。FCF-NPV交换机在VSAN中的工作模式又可分为两种：

¡FCF模式：在本模式下，FCF-NPV交换机的工作机制和连接方式与FCF交换机相同。

¡NPV模式：在本模式下，FCF-NPV交换机的工作机制和连接方式与NPV交换机相同。

·Transit模式：工作在本模式的交换机称为Transit交换机，其以太网接口可工作在ENode模式或FCF模式。Transit交换机可通过将以太网接口配置为ENode模式或FCF模式，以限制该接口只能接收来自ENode或FCF交换机的流量。

需要注意的是，交换机可以在非FCoE模式和FCoE模式之间直接切换，但不能在四种FCoE模式之间直接切换。当需要在四种FCoE模式之间切换时，必须先将交换机切换至非FCoE模式。当交换机从FCoE模式切换至非FCoE模式后，原FCoE模式下的所有FC和FCoE相关配置将被清空。

【举例】

\# 配置交换机工作在FCF模式。

\<Sysname\> system-view

Sysname fcoe-mode fcf

\# 当前交换机工作在FCF模式，修改其工作模式为NPV模式。

\<Sysname\> system-view

Sysname undo fcoe-mode

Sysname fcoe-mode npv

【相关命令】

·**display fcoe-mode**

**FC和FCoE \-- FC接口配置命令 \-- bandwidth (FC interface view)**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置当前接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

FC接口的期望带宽会影响FSPF的Cost值的计算，从而影响路由。

【举例】

\# 配置FC1/0/1接口的期望带宽为50kbit/s。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 bandwidth 50

**FC和FCoE \-- FC接口配置命令 \-- default (FC interface view)**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将FC1/0/1接口恢复为缺省配置。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 default

**FC和FCoE \-- FC接口配置命令 \-- description (FC interface view)**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，例如：Fc1/0/1 Interface。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置FC1/0/1接口的描述信息为FCport1。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 description FCport1

**FC和FCoE \-- FC接口配置命令 \-- display interface fc**

------------------------------------------------------------------------

**[display interface fc**]命令用来显示FC接口的相关信息。

【命令】

**[display interface** [ **fc** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[fc**]：显示FC接口的信息。如果未指定本参数，将显示设备支持的所有接口的信息。

*[interface-number*]：显示指定FC接口的信息。如果未指定本参数，将显示所有FC接口的信息。

**[brief**]：显示概要信息。如果未指定本参数，将显示详细信息。

**[description**]：当用户配置的接口描述信息超过27个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前27个字符，超出部分不会显示。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果未指定本参数，将不会根据接口物理状态来过滤显示信息。

【举例】

\# 显示FC1/0/1接口的详细信息。

\<Sysname\> display interface fc 1/0/1

Fc1/0/1

Current state: UP

Line protocol state: UP

Description: Fc1/0/1 Interface

Bandwidth: 4000000kbps

Maximum Transmit Unit: 2112

4000Mbps-speed mode

Internet protocol processing: disabled

Link layer protocol is FC

Fill word is idle-idle

Port WWN is 66:66:66:62:65:34:30:39

FC mode is Auto, state is E

Transmit B2B Credit is 64

Receive B2B Credit is 64

Support the VSAN protocol

VSAN tagging mode is Non tagging

EVFP common VSAN : 1

Last link flapping: 1 hours 12 minutes 25 seconds

Last clearing of counters: Never

表1-2 display interface fc命令显示信息描述表

字段

描述

Current state

FC接口的物理层状态和管理状态，包括：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

FC接口的链路层协议状态，可能的状态及含义如下：

·DOWN：表示数据链路层协议状态为关闭

·UP：表示数据链路层协议状态为开启

Description

FC接口的描述信息

Bandwidth

FC接口的期望带宽

Maximum Transmit Unit

FC接口的MTU值

4000Mbps-speed mode

FC接口的速率

Internet protocol processing

对IP报文的处理能力，disabled表示没有为该接口配置IP地址

Link layer protocol

FC接口的链路层协议类型

Fill word

FC接口的Fill Word模式，包括：

·idle-idle：idle-idle模式

·idle-arbff：idle-arbff模式

Port WWN

接口WWN

FC mode

FC接口的配置模式

state

FC接口的协商运行状态

Transmit B2B Credit

FC接口本端的BB_Credit值，此信息只有接口链路up后才显示

Receive B2B Credit

FC接口对端的BB_Credit值，此信息只有接口链路up后才显示

Support the VSAN protocol

FC接口支持VSAN协议，经过协商后确定接口支持VSAN协议且接口链路up后才显示该信息

VSAN tagging mode

经过EVFP协商后确定端口的连接方式是Trunk（Tagging）或Access（Non tagging），此信息只有接口链路up后才显示

EVFP common VSAN

经过协商后确定端口连接并up的公共VSAN，此信息只有接口链路up后才显示

Last link flapping

接口最近一次物理状态改变到现在的时长。Never表示接口从设备启动后一直处于down状态（没有改变过）

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

\# 显示FC1/0/1接口的概要信息。

\<Sysname\> display interface fc 1/0/1 brief

Brief information on FC interface(s):

Admin Mode: auto - auto; E - e port; F - f port; NP - n port proxy

Oper Mode: E - e port; F - f port; NP - n port proxy;

           TE - trunking e port; TF - trunking f port;

           TNP - trunking n port proxy

Interface  VSAN Admin Admin Oper Oper   Status SAN-Aggregation

                Mode  Trunk Mode Speed

                      Mode

Fc1/0/1    2    auto  off   E    4G     UP     SAGG23

表1-3 display interface fc brief命令显示信息描述表

字段

描述

Brief information on FC interface(s)

FC接口的概要信息

Interface

FC接口的名称

VSAN

FC接口的Access VSAN

Admin Mode

配置的FC接口的模式：

·auto：表示Auto模式

·E：表示E模式

·F：表示F模式

·NP：表示NP模式

Admin Trunk Mode

配置的FC接口的Trunk模式：

·auto：表示Auto模式

·on：表示On模式

·off：表示Off模式

Oper Mode

链路层协商后，FC接口的运行模式：

·E：表示工作在Access VSAN方式下的E_Port

·F：表示工作在Access VSAN方式下的F_Port

·NP：表示工作在Access VSAN方式下的NP_Port

·TE：表示工作在Trunk VSAN方式下的E_Port

·TF：表示工作在Trunk VSAN方式下的F_Port

·TNP：表示工作在Trunk VSAN方式下的NP_Port

·\--：表示未发起协商或协商失败

Oper Speed

物理层协商后，FC接口的速率，单位为bps。未发起协商或协商失败时，将显示为"\--"

Status

链路层协商后，FC接口的状态：UP或DOWN

SAN-Aggregation

FC接口所属的FC聚合组，当FC接口没有加入任何FC聚合组时，将显示为空

\# 显示FC接口的描述信息。

\<sysname\> display interface fc brief description

Brief information on FC interface(s):

Interface    Description

Fc1/0/2      Fc1/0/2 Interface

Fc1/0/3      Fc1/0/3 Interface

表1-4 display interface fc brief description命令显示信息描述表

字段

描述

Brief information on FC interface(s)

FC接口的概要信息

Interface

FC接口的名称

Description

FC接口的描述信息

\# 显示当前物理状态为down的FC接口的概要信息。

\<Sysname\> display interface fc brief down

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Fc1/0/1              ADM  Administratively

表1-5 display interface fc brief down命令显示信息描述表

字段

描述

Brief information on interface(s) under bridge mode

二层模式下（bridge）的接口概要信息，即二层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能打开接口

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口

Interface

接口名称

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

【相关命令】

·**reset counters interface**** fc**

**FC和FCoE \-- FC接口配置命令 \-- fc mode (FC interface view)**

------------------------------------------------------------------------

**[fc mode**]命令用来配置FC接口的模式。

**[undo fc mode**]命令用来恢复缺省情况。

【命令】

**[fc mode**  [\| **np**] }

**[undo fc mode**]

【缺省情况】]

FCF交换机缺省为Auto模式，NPV交换机和FCF-NPV交换机缺省为F模式。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：Auto模式，可以通过动态协商转化为F模式或E模式。

**[e**]：E模式。

**[f**]：F模式。

**[np**]：NP模式。

【使用指导】

需要注意的是：

·FCF交换机只支持Auto模式、E模式和F模式；NPV交换机只支持F模式和NP模式；FCF-NPV交换机只支持E模式、F模式和NP模式。

·在FCF-NPV交换机上，如果用户配置的FC接口模式与该接口所属的某个VSAN的工作模式不匹配，则FC接口模式的配置在该VSAN下将不会生效。

【举例】

\# 配置FC1/0/1接口工作在E模式。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fc mode e

【相关命令】

·**working-mode**

**FC和FCoE \-- FC接口配置命令 \-- fcb2bcredit**

------------------------------------------------------------------------

**[fcb2bcredit**]命令用来配置FC接口的BB_Credit（Buffer-to-Buffer Credit，缓冲区到缓冲区信用数）值。

**[undo **]**fcb2bcredit**命令用来恢复缺省情况。

【命令】

**[fcb2bcredit**]*****credit-value*

**[undo **]**fcb2bcredit**

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[credit-value*]：表示接口连续接收报文的个数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

BB_Credit是一种流量控制机制，用来保证FC接口不丢弃报文。通常情况下，用户不需要修改FC接口的BB_Credit值，采用缺省值即可。

【举例】

\# 配置FC1/0/1接口的BB_Credit值为10。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fcb2bcredit 10

**FC和FCoE \-- FC接口配置命令 \-- fill-word**

------------------------------------------------------------------------

**[fill-word**]命令用来配置8Gbps速率的FC接口的Fill Word模式。

**[undo fill-word**]命令用来恢复缺省情况。

【命令】

**[fill-word**[ { **idle-arbff** *\|* **idle-idle** }]]

**[undo fill-word**]

【缺省情况】

8Gbps速率的FC接口的Fill Word模式为idle-arbff模式。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[idle-arbff**]：idle-arbff模式，表示接口链路初始化阶段用idle原语信号，并且将ARBff原语信号作为Fill Word。

**[idle-idle**]：idle-idle模式，表示接口链路初始化阶段用idle原语信号，并且idle原语信号作为Fill Word。

【使用指导】

本命令只用于8Gbps速率的FC接口。2Gbps或4Gbps速率的FC接口仅支持idle-idle模式，即使配置了本命令也不生效。

当8Gbps速率的FC接口出现互通问题时，可以使用本命令调整Fill Word模式。

配置本命令后，需要执行**shutdown**/**undo shutdown**命令重启该FC接口后才能生效。

【举例】

\# 配置8Gbps速率的FC1/0/1接口的Fill Word模式为idle-idle模式。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 speed 8000

Sysname-Fc1/0/1 fill-word idle-idle

【相关命令】

·**speed**

**FC和FCoE \-- FC接口配置命令 \-- interface fc**

------------------------------------------------------------------------

**[interface fc**]命令用来进入FC接口视图。

【命令】

**[interface fc ***interface-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：表示FC接口的编号。

【举例】

\# 进入FC1/0/1接口的视图。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1

**FC和FCoE \-- FC接口配置命令 \-- port-type**

------------------------------------------------------------------------

![说明](FC和FCoE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[port-type**]命令用来在二层以太网接口和FC接口间进行类型切换。

【命令】

在二层以太网接口视图下：

**[port-type** **fc**]

在FC接口视图下：

**[port-type** **ethernet**]

【缺省情况】

接口为二层以太网接口类型。

【视图】

二层以太网接口视图/FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ethernet**]：将当前接口切换到二层以太网类型，切换后的接口速率与设备型号有关，请以设备的实际情况为准。

**[fc**]：将当前接口切换到FC接口类型。

【使用指导】

某些二层以太网接口支持切换到FC接口。

如果要将二层以太网接口切换为FC接口，则需要进入对应的二层以太网接口视图执行**port-type** **fc**命令；如果要将FC接口切换回二层以太网接口，则需要进入对应的FC接口视图执行**port-type** **ethernet**命令。

接口类型切换后，原接口删除并创建新的接口，切换后的接口编号与切换前保持一致。

【举例】

\# 把二层以太网接口Ten-GigabitEthernet1/0/1切换为FC接口。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/0/1

Sysname-Ten-GigabitEthernet1/0/1 port-type fc

Sysname-Fc1/0/1

**FC和FCoE \-- FC接口配置命令 \-- reset counters interface fc**

------------------------------------------------------------------------

**[reset counters interface fc**]命令用来清除FC接口的统计信息。

【命令】

**[reset counters interface** [ **fc** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fc**]：清除指定FC接口的信息。

*[interface-number*]：表示FC接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某FC接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。

·如果不指定**fc**和*interface-number*，则清除所有接口的统计信息；

·如果指定**fc**而不指定*interface-number*，则清除所有FC接口的统计信息；

·如果同时指定**fc**和*interface-number*，则清除指定FC接口的统计信息。

【举例】

\# 清除FC1/0/1接口的统计信息。

\<Sysname\> reset counters interface fc 1/0/1

【相关命令】

·**display interface ****fc**

**FC和FCoE \-- FC接口配置命令 \-- shutdown (FC interface view)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo shutdown**]命令用来打开当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于开启状态。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭FC1/0/1接口。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 shutdown

**FC和FCoE \-- FC接口配置命令 \-- speed**

------------------------------------------------------------------------

**[speed**]命令用来配置FC接口的速率。

**[undo speed**]命令用来恢复缺省情况。

【命令】

**[speed **[{**1000** \| **2000** \| **4000** \| **8000** \| **16000** \| **auto**}]]

**[undo speed**]

【缺省情况】

FC接口的速率和FC接口的物理特性有关。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1000**]：配置接口的速率为1000Mbps。

**[2000**]：配置接口的速率为2000Mbps。

**[4000**]：配置接口的速率为4000Mbps。

**[8000**]：配置接口的速率为8000Mbps。

**[16000**]：配置接口的速率为16000Mbps。

**[auto**]：配置接口自协商速率，通过两端的协商来选择可以接受的接口速率。具体协商机制与设备的型号有关，请以设备实际情况为准。

【举例】

\# 配置FC1/0/1接口的速率为1000Mbps。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 speed 1000

**FC和FCoE \-- VFC接口配置命令 \-- bandwidth (VFC interface view)**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置当前接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

VFC接口的期望带宽会影响FSPF的Cost值的计算，从而影响路由。

VFC接口的缺省波特率为10Gbit/s，各产品可以修改其缺省波特率，请以设备的实际情况为准。

【举例】

\# 配置VFC接口1的期望带宽为50kbit/s。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 bandwidth 50

**FC和FCoE \-- VFC接口配置命令 \-- bind interface**

------------------------------------------------------------------------

**[bind interface**]命令用来将VFC接口绑定到以太网接口（这里泛指二层以太网接口、二层聚合接口、S通道接口和S通道聚合接口）。

**[undo bind interface**]命令用来删除VFC接口和以太网接口的绑定关系。

【命令】

**[bind interface ***interface-type******interface-number* [ **mac** *mac-address* ]]

**[undo bind interface**]

【缺省情况】

VFC接口没有与以太网接口绑定。

【视图】

VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-numbe*r]：指定接口类型和接口编号。接口类型包括二层以太网接口、二层聚合接口、S通道接口和S通道聚合接口，不同型号的设备支持的接口类型不同，请以设备的实际情况为准。

**[mac*** mac-address*]：绑定的对端FCoE MAC地址，形式为XXXX-XXXX-XXXX，是6字节地址。

【使用指导】

VFC接口是一种虚拟接口，只有在绑定了以太网接口之后才可以使用、链路才能up，VFC接口通过与其绑定的以太网接口收发报文。

VFC接口绑定对端FCoE MAC地址，可以使多个虚拟接口使用同一个物理链路。多个VFC接口可以绑定同一个以太网接口，但必须绑定不同的对端FCoE MAC地址，通过该FCoE MAC地址来区分VFC接口是和哪个对端设备进行通信。如果是点到多点的网络，必须要绑定FCoE MAC地址；如果是点到点的网络，则可以不绑定FCoE MAC地址。

交换机的FCoE MAC地址可以通过**display fcoe**命令查看。ENode的FCoE MAC地址可以通过其它软件、网管等途径获取。

需要注意的是：

·一个VFC接口只能绑定一个以太网接口，也只能绑定一个FCoE MAC地址。

·一个以太网接口可以被多个VFC接口绑定，但是一个FCoE MAC地址仅能被一个VFC接口绑定。

·交换机只有工作在专家模式下，才支持FCoE over S-Channel能力，因此在绑定S通道接口或S通道聚合接口前，应先将系统的工作模式切换为专家模式，否则会绑定失败。有关系统工作模式的介绍，请参见"基础配置指导"中的"设备管理"；有关S通道接口和S通道聚合接口的介绍，请参见"EVB配置指导"中的"EVB"。

·绑定二层以太网接口时，该接口需具备FCoE能力，否则会绑定失败。绑定二层聚合接口时，其所有成员端口都需具备FCoE能力，否则会绑定失败；向已绑定的二层聚合接口中添加新的成员端口时，需确保新加入的成员端口具备FCoE能力，否则可能导致FCoE流量转发不通。绑定S通道接口时，其对应的二层以太网接口需具备FCoE over S-Channel能力，否则会绑定失败。绑定S通道聚合接口时，其对应二层聚合接口内的所有成员端口都需具备FCoE over S-Channel能力，否则会绑定失败；向已绑定的S通道聚合接口对应的二层聚合接口中添加新的成员端口时，需确保新加入的成员端口具备FCoE over S-Channel能力，否则可能导致FCoE流量转发不通。具体哪些单板具备FCoE能力和FCoE over S-Channel能力，请参考产品手册的介绍。

·如果将二层聚合接口和该二层聚合接口的成员端口分别与不同的VFC接口绑定，则二层聚合接口的绑定配置将不会生效；如果将S通道聚合接口和该S通道聚合接口所对应二层聚合接口的成员端口分别与不同的VFC接口绑定，则S通道聚合接口的绑定配置将不会生效。

·在二层以太网接口或二层聚合接口上开启EVB功能后，这些接口上的FCoE流量将断流，只有在这些接口上创建S通道接口或S通道聚合接口并与VFC接口绑定后，才能恢复FCoE流量。

·FCoE over S-Channel只能应用于支持EVB功能的设备与服务器接口之间。

【举例】

\# 将VFC接口4绑定到二层以太网接口Ten-GigabitEthernet1/0/1，并绑定FCoE MAC地址000c-2999-eacd。

\<Sysname\> system-view

sysname interface vfc 4

sysname-Vfc4 bind interface ten-gigabitethernet 1/0/1 mac 000c-2999-eacd

\# 将VFC接口5绑定到二层聚合接口Bridge-aggregation1，并绑定FCoE MAC地址000c-2888-eacd。

\<Sysname\> system-view

sysname interface vfc 5

sysname-Vfc5 bind interface bridge-aggregation 1 mac 000c-2888-eacd

\# 将VFC接口6绑定到S通道接口S-Channe1/0/1:10，并绑定FCoE MAC地址000c-2777-eacd。

\<Sysname\> system-view

sysname interface vfc 6

sysname-Vfc6 bind interface s-channel 1/0/1:10 mac 000c-2777-eacd

\# 将VFC接口7绑定到S通道聚合接口Schannel-Aggregation1:10，并绑定FCoE MAC地址000c-2666-eacd。

\<Sysname\> system-view

sysname interface vfc 7

sysname-Vfc7 bind interface schannel-aggregation 1:10 mac 000c-2666-eacd

【相关命令】

·**display fcoe**

·**display interface vfc**

**FC和FCoE \-- VFC接口配置命令 \-- default (VFC interface view)**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将VFC接口1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 default

**FC和FCoE \-- VFC接口配置命令 \-- description (VFC interface view)**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo descripition**]命令用来恢复缺省情况。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*接口名* interface"，例如：Vfc1 Interface。

【视图】

VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【使用指导】

接口的描述信息可以帮助用户标记接口的作用。

【举例】

\# 配置VFC接口1的描述信息为VFCport1。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 description VFCport1

**FC和FCoE \-- VFC接口配置命令 \-- display interface vfc**

------------------------------------------------------------------------

**[display interface vfc**]命令用来显示VFC接口的相关信息。

【命令】

**[display interface** [ **vfc** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vfc**]：显示VFC接口的信息。如果未指定本参数，将显示设备支持的所有接口的信息。

*[interface-numbe*r]：显示指定VFC接口的信息，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，将显示所有VFC接口的信息。

**[brief**]：显示概要信息。如果未指定本参数，将显示详细信息。

**[description**]：当用户配置的接口描述信息超过27个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前27个字符，超出部分不会显示。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果未指定本参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**vfc**参数，将显示设备支持的所有接口的相关信息。

·如果指定**vfc**参数，不指定*interface-number*参数，将显示所有VFC接口的相关信息。

【举例】

\# 显示VFC接口1的详细信息。

\<Sysname\> display interface vfc 1

Vfc1

Current state: UP

Line protocol state: UP

Description: Vfc1 Interface

Bandwidth: 10000000kbps

Maximum Transmit Unit: 2112

Internet protocol processing: disabled

Link layer protocol is FC

Port WWN is 66:66:66:63:66:64:61:30

FC mode is E, state is E

Support the VSAN protocol

VSAN tagging mode is Tagging

EVFP common VSAN: 1

Bound interface is Ten-GigabitEthernet1/0/1, Bound MAC is 000c-2933-eacd

VSAN of physical-UP state: 1

Last clearing of counters: Never

表1-6 display interface vfc命令显示信息描述表

字段

描述

Current state

VFC接口的物理状态和管理状态，包括：

·DOWN ( Administratively )：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

VFC接口的链路层协议状态，可能的状态及含义如下：

·DOWN：表示数据链路层协议状态为关闭

·UP：表示数据链路层协议状态为开启

Description

VFC接口的描述信息

Bandwidth

VFC接口的期望带宽

Maximum Transmit Unit

VFC接口的MTU值

Internet protocol processing

对IP报文的处理能力，disabled表示没有为该接口配置IP地址

Link layer protocol

VFC接口的链路层协议类型

Port WWN

端口WWN

FC mode

VFC接口的配置模式

state

VFC接口的协商运行状态

Support the VSAN protocol

VFC接口支持VSAN协议

VSAN tagging mode

端口的连接方式是Trunk（Tagging）或Access（Non tagging），VFC接口只支持Tagging

EVFP common VSAN

经过协商后确定端口连接并up的公共VSAN，此信息只有接口链路up后才显示

Bound interface

VFC接口绑定的物理接口

Bound MAC

VFC接口绑定的FCoE MAC地址

VSAN of physical-UP state

处于物理up状态的VSAN列表

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

\# 显示VFC接口1的概要信息。

\<Sysname\> display interface vfc 1 brief

Brief information on VFC interface(s):

Admin Mode: auto - auto; E - e port; F - f port; NP - n port proxy

Oper Mode: E - e port; F - f port; NP - n port proxy;

           TE - trunking e port; TF - trunking f port;

           TNP - trunking n port proxy

Interface  Admin Admin Oper Status Bind

           Mode  Trunk Mode        Interface

                 Mode

Vfc1       F     on    TF   UP     XGE1/0/1 01:02:03:04:05:06

表1-7 display interface vfc brief命令显示信息描述表

字段

描述

Brief information on VFC interface(s)

VFC接口的概要信息

Interface

VFC接口的名称

Admin Mode

配置的VFC接口的模式：

·auto：表示Auto模式（VFC接口不支持本模式）

·E：表示E模式

·F：表示F模式

·NP：表示NP模式

Admin Trunk Mode

配置的VFC接口的Trunk模式：

·auto：表示Auto模式

·on：表示On模式（VFC接口仅支持本模式）

·off：表示Off模式

Oper Mode

链路层协商后，VFC接口的运行模式：

·E：表示工作在Access VSAN方式下的E_Port

·F：表示工作在Access VSAN方式下的F_Port

·NP：表示工作在Access VSAN方式下的NP_Port

·TE：表示工作在Trunk VSAN方式下的E_Port

·TF：表示工作在Trunk VSAN方式下的F_Port

·TNP：表示工作在Trunk VSAN方式下的NP_Port

·\--：表示未发起协商或协商失败

Status

链路层协商后，FC接口的状态：UP或DOWN

Bind Interface

VFC接口的绑定信息，包括：绑定的以太网接口和FCoE MAC地址。如果没有配置绑定信息，则显示为空

\# 显示VFC接口的描述信息。

\<sysname\> display interface vfc brief description

Brief information on VFC interface(s):

Interface    Description

Vfc1         Vfc1 Interface

Vfc2         Vfc2 Interface

表1-8 display interface vfc brief description命令显示信息描述表

字段

描述

Brief information on VFC interface(s)

VFC接口的概要信息

Interface

VFC接口的名称

Description

VFC接口的描述信息

\# 显示当前物理状态为down的VFC接口的概要信息。

\<Sysname\> display interface vfc brief down

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Vfc1                 ADM  Administratively

表1-9 display interface vfc brief down命令显示信息描述表

字段

描述

Brief information on interface(s) under bridge mode

二层模式下（bridge）的接口概要信息，即二层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能打开接口

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口

Interface

接口名称

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

【相关命令】

·**reset counters interface**** vfc**

**FC和FCoE \-- VFC接口配置命令 \-- fc mode (VFC interface view)**

------------------------------------------------------------------------

**[fc mode**]命令用来配置VFC接口的模式。

**[undo fc mode**]命令用来恢复缺省情况。

【命令】

**[fc mode**  { **e** \| **f** \| **np** }]

**[undo fc mode**]

【缺省情况】

VFC接口的模式为F模式。

【视图】

VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[e**]：E模式。

**[f**]：F模式。

**[np**]：NP模式。

【使用指导】

需要注意的是：

·FCF交换机只支持E模式和F模式；NPV交换机只支持F模式和NP模式；FCF-NPV交换机支持E模式、F模式和NP模式。

·在FCF-NPV交换机上，如果用户配置的VFC接口模式与该接口所属的某个VSAN的工作模式不匹配，则VFC接口模式的配置在该VSAN下将不会生效。

【举例】

\# 配置VFC接口1工作在E模式。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fc mode e

【相关命令】

·**working-mode**

**FC和FCoE \-- VFC接口配置命令 \-- interface vfc**

------------------------------------------------------------------------

**[interface vfc**]命令用来创建VFC接口并进入VFC接口视图。如果该VFC接口已经存在，则直接进入VFC接口视图。

**[undo interface vfc**]命令用来删除VFC接口。

【命令】

**[interface vfc ***interface-number*]

**[undo interface vfc ***interface-number*]

【缺省情况】

不存在VFC接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-numbe*r]：表示VFC接口的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

VFC接口是手工创建的虚拟逻辑口，它虚拟实现物理FC接口的功能。

【举例】

\# 创建VFC接口1，并进入VFC接口1的视图。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1

【相关命令】

·**display interface vfc**

**FC和FCoE \-- VFC接口配置命令 \-- reset counters interface vfc**

------------------------------------------------------------------------

**[reset counters interface vfc**]命令用来清除VFC接口的统计信息。

【命令】

**[reset counters interface** [ **vfc** [ *number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vfc**]：清除指定VFC接口的信息。

*[number*]：表示VFC接口编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在某些情况下，需要统计一定时间内某FC接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。

·如果不指定**vfc**和*number*，则清除所有接口的统计信息；

·如果指定**vfc**而不指定*number*，则清除所有VFC接口的统计信息；

·如果同时指定**vfc**和*number*，则清除指定VFC接口的统计信息。

【举例】

\# 清除VFC接口1的统计信息。

\<Sysname\> reset counters interface vfc 1

【相关命令】

·**display interface ****vfc**

**FC和FCoE \-- VFC接口配置命令 \-- shutdown (VFC interface view)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo shutdown**]命令用来打开当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于开启状态。

【视图】

VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭VFC接口1。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 shutdown

**FC和FCoE \-- FC链路聚合配置命令 \-- bandwidth (FC aggregate interface view)**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置当前接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

FC聚合接口的波特率＝FC聚合接口的速率。

FC聚合接口的期望带宽会影响FSPF的Cost值的计算，从而影响路由。

【举例】

\# 配置FC聚合接口3的期望带宽为1000kbit/s。

\<Sysname\> system-view

Sysname interface san-aggregation 3

Sysname-SAN-Aggregation3 bandwidth 1000

**FC和FCoE \-- FC链路聚合配置命令 \-- default (FC aggregate interface view)**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将FC聚合接口3恢复为缺省配置。

\<Sysname\> system-view

Sysname interface san-aggregation 3

Sysname-SAN-Aggregation3 default

**FC和FCoE \-- FC链路聚合配置命令 \-- description (FC aggregate interface view)**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo descripition**]命令用来恢复缺省情况。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*接口名* interface"，例如：SAN-Aggregation3 Interface。

【视图】

FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置FC聚合接口3的描述信息为SAGG-interface。

\<Sysname\> system-view

Sysname interface san-aggregation 3

Sysname-SAN-Aggregation3 description SAGG-interface

**FC和FCoE \-- FC链路聚合配置命令 \-- display interface san-aggregation**

------------------------------------------------------------------------

**[display interface san-aggregation**]命令用来显示FC聚合接口的相关信息。

【命令】

**[display interface** [ **san-aggregation** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[san-aggregation**]：显示FC聚合接口的信息。如果未指定本参数，将显示设备支持的所有接口的信息。

*[interface-numbe*r]：显示指定FC聚合接口的信息，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，将显示所有FC聚合接口的信息。

**[brief**]：显示概要信息。如果未指定本参数，将显示详细信息。

**[description**]：当用户配置的接口描述信息超过27个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前27个字符，超出部分不会显示。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**san-aggregation**参数，将显示设备支持的所有接口的相关信息。

·如果指定**san-aggregation**参数，不指定*interface-number*参数，将显示所有FC聚合接口的相关信息。

【举例】

\# 显示FC聚合接口3的详细信息。

\<Sysname\> display interface san-aggregation 3

SAN-Aggregation3

Current state: UP

Line protocol state: UP

Description: SAN-Aggregation3 Interface

Bandwidth: 1000kbps

Maximum Transmit Unit: 2112

Internet protocol processing: disabled

Link layer protocol is FC

Port WWN is 00:00:00:00:00:00:00:00

FC mode is Auto, state is Init

Last clearing of counters: Never

表1-10 display interface san-aggregation命令显示信息描述表

字段

描述

Current state

FC聚合接口的物理状态和管理状态，包括：

·DOWN ( Administratively )：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

FC聚合接口的链路层协议状态，可能的状态及含义如下：

·DOWN：表示数据链路层协议状态为关闭

·UP：表示数据链路层协议状态为开启

Description

FC聚合接口的描述信息

Bandwidth

FC聚合接口的期望带宽，只有取值不为0时才会显示本字段

Maximum Transmit Unit

FC聚合接口的MTU值

Internet protocol processing

对IP报文的处理能力，disabled表示没有为该接口配置IP地址

Link layer protocol

FC聚合接口的链路层协议类型

Port WWN

端口WWN

FC mode

FC聚合接口的配置模式

state

FC聚合接口的协商运行状态

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

\# 显示FC聚合接口3的概要信息。

\<Sysname\> display interface san-aggregation 3 brief

Brief information on SAN-Aggregation interface(s):

Admin Mode: auto - auto; E - e port; F - f port; NP - n port proxy

Oper Mode: E - e port; F - f port; NP - n port proxy;

           TE - trunking e port; TF - trunking f port;

           TNP - trunking n port proxy

Interface  VSAN Admin Admin Oper Oper   Status

                Mode  Trunk Mode Speed

                      Mode

SAGG3      37   NP    auto  NP   4G     UP

表1-11 display interface san-aggregation brief命令显示信息描述表

字段

描述

Brief information on SAN-Aggregation interface(s)

FC聚合接口的概要信息

Interface

FC聚合接口的名称

VSAN

FC聚合接口的Access VSAN

Admin Mode

配置的FC聚合接口的模式：

·auto：表示Auto模式

·E：表示E模式

·F：表示F模式

·NP：表示NP模式

Admin Trunk Mode

配置的FC聚合接口的Trunk模式：

·auto：表示Auto模式

·on：表示On模式

·off：表示Off模式

Oper Mode

链路层协商后，FC聚合接口的运行模式：

·E：表示工作在Access VSAN方式下的E_Port

·F：表示工作在Access VSAN方式下的F_Port

·NP：表示工作在Access VSAN方式下的NP_Port

·TE：表示工作在Trunk VSAN方式下的E_Port

·TF：表示工作在Trunk VSAN方式下的F_Port

·TNP：表示工作在Trunk VSAN方式下的NP_Port

·\--：表示未发起协商或协商失败

Oper Speed

物理层协商后，FC聚合接口的速率，单位为bps。未发起协商或协商失败时，将显示为"\--"

Status

链路层协商后，FC聚合接口的状态：UP或DOWN

\# 显示FC聚合接口的描述信息。

\<sysname\> display interface san-aggregation brief description

Brief information on SAN-Aggregation interface(s):

Interface    Description

SAGG1        SAGG1 Interface

SAGG2        SAGG2 Interface

表1-12 display interface san-aggregation brief description命令显示信息描述表

字段

描述

Brief information on SAN-Aggregation interface(s)

FC聚合接口的概要信息

Interface

FC聚合接口的名称

Description

FC聚合接口的描述信息

\# 显示当前物理状态为down的FC聚合接口的概要信息。

\<Sysname\> display interface san-aggregation brief down

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

SAGG3                ADM  Administratively

表1-13 display interface san-aggregation brief down命令显示信息描述表

字段

描述

Brief information on interface(s) under bridge mode

二层模式下（bridge）的接口概要信息，即二层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能打开接口

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口

Interface

接口名称

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

【相关命令】

·**reset counters interface****san-aggregation**

**FC和FCoE \-- FC链路聚合配置命令 \-- display san-aggregation**

------------------------------------------------------------------------

**[display san-aggregation**]命令用来显示已有FC聚合接口所对应FC聚合组的信息。

【命令】

**[display san-aggregation** [ **verbose**   **interface** **san-aggregation** *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：显示FC聚合接口所对应FC聚合组的详细信息。不指定本参数时，将显示FC聚合接口所对应FC聚合组的简要信息。

**[interface** **san-aggregation** *interface-number*]：显示指定FC聚合接口所对应FC聚合组的信息。*interface-number*表示FC聚合接口的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。不指定本参数时，将显示所有FC聚合接口所对应FC聚合组的信息。

【举例】

\# 显示所有FC聚合接口所对应FC聚合组的简要信息。

\<Sysname\> display san-aggregation

\* indicates the member port is selected.

Interface        State   Mode   Speed     Member port

SAGG1            UP      E      8Gbps    \*Fc1/0/1

                                          Fc1/0/2

SAGG2            DOWN    -      -         -

表1-14 display san-aggregation命令显示信息描述表

字段

描述

Interface

FC聚合接口的简写名称

State

FC聚合接口的物理状态，包括：

·DOWN：该接口的物理状态为关闭，表示对应FC聚合组内没有选中成员接口

·UP：该接口的物理状态为开启，表示对应FC聚合组内有选中成员接口

Mode

FC聚合接口的运行模式，包括：

·E：E模式

·F：F模式

·NP：NP模式

（FC聚合接口物理状态为DOWN时显示为"-"）

Speed

FC聚合接口的速率，为所有选中成员接口的速率之和（FC聚合接口物理状态为DOWN时显示为"-"）

Member port

FC聚合接口所对应FC聚合组的成员接口（带\*表示为选中成员接口，没有成员接口时显示为"-"）

\# 显示所有FC聚合接口所对应FC聚合组的详细信息。

\<Sysname\> display san-aggregation verbose

Interface SAN-Aggregation1：

State                : UP

Mode                 : E

Speed                : 2Gbps

Member port number   : 2

Selected port number : 1

  Member port        State   Mode   Speed   Selected

  Fc1/0/1            UP      E      2Gbps   Y

  Fc1/0/2            UP      E      1Gbps   N

Interface SAN-Aggregation2:

State                : DOWN

Mode                 : N/A

Speed                : N/A

Member port number   : 2

Selected port number : 0

  Member port         State   Mode   Speed   Selected

  Fc1/0/3             DOWN    -      -       N

  Fc1/0/4             DOWN    -      -       N

表1-15 display san-aggregation verbose命令显示信息描述表

字段

描述

Interface

FC聚合接口的名称

State

FC聚合接口的物理层状态，包括：

·DOWN：该接口的物理状态为关闭，表示对应FC聚合组内没有选中成员接口

·UP：该接口的物理状态为开启，表示对应FC聚合组内有选中成员接口

Mode

FC聚合接口的运行模式，包括：

·E：E模式

·F：F模式

·NP：NP模式

（FC聚合接口物理状态为DOWN时显示为"N/A"）

Speed

FC聚合接口的速率，为所有选中成员接口的速率之和（FC聚合接口物理状态为DOWN时显示为"N/A"）

Member port number

FC聚合接口所对应FC聚合组的成员接口的数量

Selected port number

FC聚合接口所对应FC聚合组的选中成员接口的数量

Member port

FC聚合接口所对应FC聚合组的成员接口名称，没有成员接口时不显示

State

成员接口的链路协议状态，包括：

·DOWN：该接口的链路协议状态为关闭

·UP：该接口的链路协议状态为开启

Mode

成员接口的运行模式，包括：

·E：E模式

·F：F模式

·NP：NP模式

（成员接口的链路协议状态为DOWN时显示为"-"）

Speed

成员接口的速率（成员接口的链路协议状态为DOWN时显示为"-"）

Selected

成员接口的选中状态，包括：

·N：该接口未被选中

·Y：该接口被选中

**FC和FCoE \-- FC链路聚合配置命令 \-- fc mode (FC aggregate interface view)**

------------------------------------------------------------------------

**[fc mode**]命令用来配置FC聚合接口的模式。

**[undo fc mode**]命令用来恢复缺省情况。

【命令】

**[fc mode**  [\| **np**] }

**[undo fc mode**]

【缺省情况】]

FCF交换机缺省为Auto模式，NPV交换机和FCF-NPV交换机缺省为F模式。

【视图】

FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：Auto模式，可以通过动态协商转化为F模式或E模式。

**[e**]：E模式。

**[f**]：F模式。

**[np**]：NP模式。

【使用指导】

需要注意的是：

·FCF交换机只支持Auto模式、E模式和F模式；NPV交换机只支持F模式和NP模式；FCF-NPV交换机只支持E模式、F模式和NP模式。

·在FCF-NPV交换机上，如果用户配置的FC聚合接口模式与该接口所属的某个VSAN的工作模式不匹配，则FC聚合接口模式的配置在该VSAN下将不会生效。

【举例】

\# 配置FC聚合接口3工作在E模式。

\<Sysname\> system-view

Sysname interface san-aggregation 3

Sysname-SAN-Aggregation3 fc mode e

【相关命令】

·**working-mode**

**FC和FCoE \-- FC链路聚合配置命令 \-- interface san-aggregation**

------------------------------------------------------------------------

**[interface san-aggregation**]命令用来创建FC聚合接口并进入FC聚合接口视图。如果该FC聚合接口已经存在，则直接进入FC聚合接口视图。

**[undo interface san-aggregation**]命令用来删除FC聚合接口。

【命令】

**[interface san-aggregation ***interface-number*]

**[undo interface san-aggregation ***interface-number*]

【缺省情况】

不存在FC聚合接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-numbe*r]：表示FC聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 创建FC聚合接口3，并进入FC聚合接口3的视图。

\<Sysname\> system-view

Sysname interface san-aggregation 3

Sysname-SAN-Aggregation3

【相关命令】

·**display interface san-aggregation**

**FC和FCoE \-- FC链路聚合配置命令 \-- reset counters interface san-aggregation**

------------------------------------------------------------------------

**[reset counters interface san-aggregation**]命令用来清除FC聚合接口的统计信息。

【命令】

**[reset counters interface** [ **san-aggregation** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[san-aggregation**]：清除指定FC聚合接口的信息。

*[interface-number*]：表示FC聚合接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在某些情况下，需要统计一定时间内某FC接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。

·如果不指定**san-aggregation**和*number*，则清除所有接口的统计信息；

·如果指定**san-aggregation**而不指定*number*，则清除所有FC聚合接口的统计信息；

·如果同时指定**san-aggregation**和*number*，则清除指定FC聚合接口的统计信息。

【举例】

\# 清除FC聚合接口3的统计信息。

\<Sysname\> reset counters interface san-aggregation 3

【相关命令】

·**display interface san-aggregation**

**FC和FCoE \-- FC链路聚合配置命令 \-- san-aggregation group**

------------------------------------------------------------------------

**[san-aggregation group**]命令用来将FC接口加入指定的FC聚合组。

**[undo san-aggregation group**]命令用来将FC接口从已加入的FC聚合组中删除。

【命令】

**[san-aggregation group ***group-number*]

**[undo san-aggregation group**]

【缺省情况】

FC接口未加入任何FC聚合组。

【视图】

FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：指定已经存在的FC聚合组所对应FC聚合接口的编号。FC聚合组和FC聚合接口一一对应、编号相同。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

需要注意到是：

·一个FC接口只能加入一个FC聚合组。

·FC接口加入FC聚合组后，会删除FC接口下原有的接口模式、Trunk模式、Trunk VSAN、 Access VSAN配置，也不允许对成员接口做以上配置。FC接口离开FC聚合组后，这些配置也不会恢复，均为缺省配置。

·一个FC聚合组中可以加入的成员接口数量与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 将FC1/0/1接口加入FC聚合组2。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 san-aggregation group 2

【相关命令】

·**display san-aggregation**

**FC和FCoE \-- FC链路聚合配置命令 \-- san-aggregation load-sharing mode local-first**

------------------------------------------------------------------------

**[san-aggregation load-sharing mode local-first**]命令用来开启本地转发优先功能。

**[undo san-aggregation load-sharing mode local-first**]命令用来关闭本地转发优先功能。

【命令】

**[san-aggregation load-sharing mode local-first**]

**[undo san-aggregation load-sharing mode local-first**]

【缺省情况】

本地转发优先功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

采用聚合负载分担的本地转发优先机制可以降低数据流量对IRF物理端口之间链路的冲击。在IRF中，如果某成员设备转发报文的出接口为FC聚合接口，且对应FC聚合组的选中口分布在多个成员设备上，则系统根据该成员设备上的配置进行如下处理：

·当该成员设备开启了本地转发优先功能时，如果该成员设备上存在选中口，则只在该成员设备上的各选中口间进行负载分担；如果该成员设备上不存在选中口，则在所有成员设备上的所有选中口间进行负载分担。

·当该成员设备关闭了本地转发优先功能时，将在所有成员设备上的所有选中口间进行负载分担。

有关IRF的详细介绍，请参见"虚拟化技术配置指导"中的"IRF"。

需要注意的是，本地转发优选功能配置后会立即生效，可能造成转发流量丢失。

【举例】

\# 开启本地转发优先功能。

\<Sysname\> system-view

Sysname san-aggregation load-sharing mode local-first

**FC和FCoE \-- FC链路聚合配置命令 \-- shutdown (FC aggregate interface view)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo shutdown**]命令用来打开当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于开启状态。

【视图】

FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭FC聚合接口3。

\<Sysname\> system-view

Sysname interface san-aggregation 3

Sysname-SAN-Aggregation3 shutdown

**FC和FCoE \-- FCoE功能配置命令 \-- display fcoe**

------------------------------------------------------------------------

**[display fcoe**]命令用来显示全局的FCoE配置信息。

【命令】

**[display fcoe**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

只有FCF交换机和NPV交换机支持本命令。

【举例】

\# 显示全局的FCoE配置信息。（FCF交换机和NPV交换机）

\<Sysname\> display fcoe

Global FCoE information:

  FCoE MAC    : 0000-1234-0202

  FC-MAP      : 0x0efc25

  FCF Priority: 128

  FKA period  : 8 seconds

表1-16 display fcoe命令显示信息描述表

字段

描述

Global FCoE information

全局的FCoE配置信息

FCoE MAC

交换机的FCoE MAC地址

FC-MAP

FC-MAP值

FCF Priority

系统的FCF优先级

FKA period

VFC接口周期性发送发现请求报文和非请求发现通告报文的时间间隔

【相关命令】

·**fcoe fcmap**

·**fcoe fka-adv-period**

·**fcoe global fcf-priority**

**FC和FCoE \-- FCoE功能配置命令 \-- display fcoe vlan**

------------------------------------------------------------------------

**[display fcoe vlan**]命令用来显示指定VLAN中的FCoE配置信息。

【命令】

**[display fcoe vlan ***vlan-id*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan ***vlan-id*]：指定VLAN，*vlan-id*的取值范围为1～4094。

【使用指导】

只有FCF-NPV交换机支持本命令。

【举例】

\# 显示VLAN 1中的FCoE配置信息。（FCF-NPV交换机）

\<Sysname\> display fcoe

FCoE information of VLAN 10:

  FCoE MAC    : 0000-2345-0202

  FC-MAP      : 0x0efc01

  FCF Priority: 128

  FKA period  : 8 seconds

表1-17 display fcoe vlan命令显示信息描述表

字段

描述

FCoE information of VLAN 10

VLAN 10中的FCoE配置信息

FCoE MAC

交换机的FCoE MAC地址

FC-MAP

FC-MAP值

FCF Priority

系统的FCF优先级

FKA period

VFC接口周期性发送发现请求报文和非请求发现通告报文的时间间隔

【相关命令】

·**fcoe fcmap**

·**fcoe fka-adv-period**

·**fcoe global fcf-priority**

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe enable**

------------------------------------------------------------------------

**[fcoe enable**]命令用来开启FCoE功能并指定映射VSAN。

**[undo fcoe enable**]命令用来关闭FCoE功能。

【命令】

**[fcoe enable** [ **vsan** *vsan-id* ]]

**[undo fcoe enable**]

【缺省情况】

VLAN内的FCoE功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan*** vsan-id*]：当前VLAN映射的VSAN，*vsan-id*为VSAN的编号，取值范围为1～3839。如果未指定本参数，则当前VLAN将与同编号的VSAN相映射。在编号为3840～4094的VLAN内则必须指定本参数，否则系统将提示出错。

【使用指导】

通过FC接口或VFC接口发送报文时，都需要配置本功能：

·通过FC接口发送报文时，用到的VSAN都要与某个VLAN映射，并在该VLAN内开启FCoE功能，目的是让设备可以正常运行FC和FCoE相关特性。

·通过VFC接口发送报文时，由于其绑定的以太网接口可能同时允许多个VLAN通过，因此需要在其中某个VLAN内开启FCoE功能，并将该VLAN与某VSAN映射，这样该VSAN内的报文就会被打上该VLAN的Tag，并在此VLAN内发送。

需要注意的是：

·不允许在VLAN 1内开启FCoE功能。

·VLAN与VSAN是一一对应的，一个VLAN只能映射一个VSAN，反之亦然。

·链路两端的设备必须通过相同的VSAN通信：使用FC接口时，两端的VSAN可以与不同的VLAN映射；使用VFC接口时，两端的VSAN必须与相同的VLAN映射。

·在某个VLAN内开启了FCoE功能后：

¡该VLAN内仅转发FCoE流量，不转发其它业务流量（如IP流量）。

¡该VLAN内的成员端口之间被设置为二层隔离，不会形成广播环路，因此，FCoE VLAN内不需要运行生成树协议或其它环路检测协议，否则可能会导致FCoE转发链路被阻塞。

¡该VLAN内可以运行二层协议，但由于成员端口之间被设置为二层隔离，因此二层协议将按照端口隔离的拓扑运行。

【举例】

\# 在VLAN 4内开启FCoE功能，并将该VLAN与VSAN 6相映射。

\<Sysname\> system-view

Sysname vlan 4

Sysname-vlan4 fcoe enable vsan 6

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe fcf-priority**

------------------------------------------------------------------------

**[fcoe fcf-priority**]命令用来配置VFC接口的FCF优先级。

**[undo fcoe fcf-priority**]命令用来恢复缺省情况。

【命令】

**[fcoe fcf-priority** *priority*]

**[undo fcoe fcf-priority**]

【缺省情况】

VFC接口的FCF优先级为128。

【视图】

VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：FCF优先级，取值范围为0～255，数值越小，优先级越高。

【使用指导】

发送请求发现通告报文时，报文中的fcf priority字段将填写VFC接口的FCF优先级的值。

ENode在收到多个FCF发送的发现通告报文的情况下，将从这些发现通告报文中选择fcf priority优先级最高的FCF，并向其发送FLOGI报文，进行注册。

本配置仅在VFC接口为F模式时生效，在E模式下可以配置，但不生效。

【举例】

\# 配置VFC接口的FCF优先级为12。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fcoe fcf-priority 12

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe fcmap**

------------------------------------------------------------------------

**[fcoe fcmap**]命令用来配置FC-MAP值。

**[undo fcoe fcmap**]命令用来恢复缺省情况。

【命令】

**[fcoe fcmap** *fc-map*]

**[undo fcoe fcmap**]

【缺省情况】

FC-MAP值为0x0EFC00。

【视图】

系统视图/VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fc-map*]：FC-MAP值，取值范围为0x0EFC00～0x0EFCFF。

【使用指导】

本命令可以在系统视图或VLAN视图下配置，FCF交换机和NPV交换机只支持系统视图下的配置，FCF-NPV交换机只支持VLAN视图下的配置。

FC-MAP值用来标识一个FCoE网络，所有的交换机必须具有相同的FC-MAP值。

需要注意的是，配置FC-MAP值后，VFC接口会重新进行FIP协商。

【举例】

\# 配置FC-MAP值为0x0EFCFF。（FCF交换机和NPV交换机）

\<Sysname\> system-view

Sysname fcoe fcmap 0efcff

\# 在VLAN 2中，配置FC-MAP值为0x0EFCFF。（FCF-NPV交换机）

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 fcoe fcmap 0efcff

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe fka-adv-period**

------------------------------------------------------------------------

**[fcoe fka-adv-period**]命令用来配置fka-adv-period值。

**[undo fcoe fka-adv-period**]命令用来恢复缺省情况。

【命令】

**[fcoe fka-adv-period** *fka-adv-period*]

**[undo fcoe fka-adv-period**]

【缺省情况】

fka-adv-period值为8秒。

【视图】

系统视图/VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fka-adv-period*]：fka-adv-period值，取值范围为4～600，单位为秒。

【使用指导】

本命令可以在系统视图或VLAN视图下配置，FCF交换机和NPV交换机只支持系统视图下的配置，FCF-NPV交换机只支持VLAN视图下的配置。

fka-adv-period值的作用如下：

·虚链路建立以后，在E模式VFC接口上，交换机以fka-adv-period为间隔周期性向外发送非请求发现通告报文来维护建立的虚链路，非请求发现通告报文中携带fka-adv-period值。对端交换机收到非请求发现通告报文后，维持虚链路的状态，并记录fka-adv-period值。如果交换机在2.5倍的fka-adv-period间隔（收到的非请求发现通告报文中携带的值，非本机配置的值）内没有收到非请求发现通告报文，则删除该虚链路。

·虚链路建立以后，在F模式VFC接口上，交换机以fka-adv-period为间隔周期性向外发送非请求发现通告报文来维护建立的虚链路，非请求发现通告报文中携带fka-adv-period值。对端ENode收到非请求发现通告报文后，维持虚链路的状态，并记录fka-adv-period值。如果ENode在2.5倍的fka-adv-period间隔内没有收到非请求发现通告报文，则删除该虚链路。同时ENode使用记录的fka-adv-period间隔周期性发送保活报文，交换机收到保活报文后，维持虚链路的状态。如果交换机在2.5倍的fka-adv-period间隔内没有收到保活报文，则删除该虚链路。

·NP模式的VFC接口与ENode的行为相同，不受本交换机配置的fka-adv-period值的影响，使用从对端交换机学习到的fka-adv-period值。

配置fka-adv-period值时，需要注意：

·FC-BB-5标准中规定，fka-adv-period取值上限为90秒，H3C交换机的fka-adv-period配置上限为600秒，超出了协议规定的取值范围。因此，当H3C交换机与服务器、存储设备或其他厂商交换机互通时，配置的fka-adv-period值不能超出90秒。

·通常情况下，使用fka-adv-period的缺省值（8秒）即可。在交换机进行主备倒换或者有备用主控板的ISSU软重启升级时，为了保证业务不中断，如果FCoE配置较多，则需要适当调大fka-adv-period值，建议配置为60～90秒之间。关于ISSU的详细介绍，请参见"基础配置指导"中的"ISSU"。

·超出90秒的配置，建议用户在无备用主控板的ISSU软重启升级时使用。当交换机进行无备用主控板ISSU软重启升级时，由于没有备用主控板的存在，会有较长一段时间无法发送非请求发现通告报文或保活报文，为了使对端设备不会在此期间因超时而删除虚链路，从而保证业务不中断，建议调整fka-adv-period值到300～600秒之间，使得ISSU软重启升级能够完成。

·NPV交换机进行主备倒换或者ISSU软重启升级时，为了保证业务不中断，除了要调整本交换机的fka-adv-period值，还要调整上游FCF交换机的fka-adv-period值。这是因为，NPV交换机上的fka-adv-period值，仅影响本机F模式VFC接口和其连接的下游Enode的行为。NP模式VFC接口使用的是从上游FCF交换机学习到的fka-adv-period值。因此，NPV交换机进行主备倒换或者ISSU软重启升级时，需要同时调整本交换机和上游FCF交换机的fka-adv-period值。

由于上述配置限制，当无备用主控板的接入FCF交换机或NPV交换机进行ISSU软重启升级时，FCoE流量会中断。这是因为接入FCF交换机或NPV交换机连接服务器、存储设备或者其他厂商NPV设备，由于互通限制，fka-adv-period值不能超过90秒。由于没有备用主控板存在，ISSU软重启升级需要的时间较长，超过了2.5×90秒的超时间隔，ISSU软重启升级期间虚链路会超时删除，所以，FCoE流量会中断。

【举例】

\# 配置fka-adv-period值为20秒。（FCF交换机和NPV交换机）

\<Sysname\> system-view

Sysname fcoe fka-adv-period 20

\# 在VLAN 2中，配置fka-adv-period值为20秒。（FCF-NPV交换机）

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 fcoe fka-adv-period 20

**FC和FCoE \-- FCoE功能配置命令 \-- fcoe global fcf-priority**

------------------------------------------------------------------------

**[fcoe global fcf-priority**]命令用来配置系统的FCF优先级。

**[undo fcoe global fcf-priority**]命令用来恢复缺省情况。

【命令】

**[fcoe global fcf-priority ***priority*]

**[undo fcoe global fcf-priority**]

【缺省情况】

系统的FCF优先级为128。

【视图】

系统视图/VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：FCF优先级，取值范围为0～255，数值越小，优先级越高。

【使用指导】

本命令可以在系统视图或VLAN视图下配置，FCF交换机和NPV交换机只支持系统视图下的配置，FCF-NPV交换机只支持VLAN视图下的配置。

发送非请求发现通告报文时，报文中的fcf priority字段将填写系统的FCF优先级的值。

ENode在收到多个FCF发送的发现通告报文的情况下，将从这些发现通告报文中选择fcf priority优先级最高的FCF，并向其发送FLOGI报文，进行注册。

本配置对所有F模式的VFC接口生效。

【举例】

\# 配置系统的FCF优先级为12。（FCF交换机和NPV交换机）

\<Sysname\> system-view

Sysname fcoe global fcf-priority 12

\# 在VLAN 2中，配置系统的FCF优先级为12。（FCF-NPV交换机）

\<Sysname\> system-view

Sysname vlan 2

Sysname-vlan2 fcoe global fcf-priority 12

**FC和FCoE \-- VSAN配置命令 \-- display vsan port-member**

------------------------------------------------------------------------

**[display vsan port-member**]命令用来显示VSAN配置的接口成员。

【命令】

**[display vsan** [ *vsan-id*  **port-member**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsan-id*]：显示指定VSAN配置的接口成员，取值范围为1～3839。不指定该参数时，显示所有VSAN配置的接口成员。

【举例】

\# 显示所有VSAN配置的接口成员。

\<Sysname\> display vsan port-member

VSAN 1:

  Access Ports:

    Fc1/0/1              Fc1/0/2           Fc1/0/3

    Fc1/0/4              Fc1/0/5           Fc1/0/6

  Trunk Ports:

    Fc1/0/4              Fc1/0/5           Fc1/0/6

    Vfc2

VSAN 2:

  Access Ports:

  Trunk Ports:

    Fc1/0/4

VSAN 10:

  Access Ports:

  Trunk Ports:

VSAN 100:

  Access Ports:

  Trunk Ports:

    Fc1/0/4              Fc1/0/5           Fc1/0/6

表1-18 display vsan port-member命令显示信息描述表

字段

描述

VSAN

VSAN编号

Access Ports

Access接口

Trunk Ports

Trunk接口

**FC和FCoE \-- VSAN配置命令 \-- display vsan status**

------------------------------------------------------------------------

**[display vsan** **status**]命令用来显示VSAN的状态信息。

【命令】

**[display vsan** [ *vsan-id*  **status**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsan-id*]：显示指定VSAN的状态信息，取值范围为1～3839。不指定该参数时，显示所有VSAN的状态信息。

【使用指导】

只有FCF-NPV交换机支持本命令。

【举例】

\# 显示所有VSAN的状态信息。

\<Sysname\> display vsan status

VSAN 1:

  Name: VSAN0001

  Working mode: NPV

VSAN 10:

  Name: VSAN0010

  Working mode: NPV

表1-19 display vsan status命令显示信息描述表

字段

描述

VSAN 1

VSAN 1的状态信息

Name

VSAN的名称

Working mode

VSAN的工作模式，包括：

·FCF：FCF模式

·NPV：NPV模式

【相关命令】

·**vsan**

·**working-mode**

**FC和FCoE \-- VSAN配置命令 \-- port**

------------------------------------------------------------------------

**[port**]命令用来将接口以Access方式批量加入当前VSAN。

**[undo port**]命令用来将多个从当前VSAN中批量删除接口。

【命令】

**[port** *interface-list*]

**[undo port** *interface-list*]

【缺省情况】

接口以Access方式属于VSAN 1。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-list*]：接口列表，表示方式为*interface-list* = { *interface-type interface-number1* [ **to** *interface-type interface-number2*  }&\<1-10\>]。其中，*interface-type*为接口类型，*interface-number*为接口编号。接口类型可以是FC接口或FC聚合接口。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

用户既可使用本命令在VSAN视图下将FC接口或FC聚合接口以Access方式批量加入当前VSAN，也可使用**port** **access vsan**命令在FC接口或FC聚合接口视图下将当前接口以Access方式加入指定VSAN。二者的配置优先级相同。

【举例】

\# 将接口FC1/0/1～FC1/0/10以Access方式批量加入VSAN 10。

\<Sysname\> system-view

Sysname vsan 10

Sysname-vsan10 port fc 1/0/1 to fc 1/0/10

【相关命令】

·**port** **access vsan**

**FC和FCoE \-- VSAN配置命令 \-- port access vsan**

------------------------------------------------------------------------

**[port** **access vsan**]命令用来将当前接口以Access方式加入指定VSAN。

**[undo port access vsan**]命令用来恢复缺省情况。

【命令】

**[port access vsan** *vsan-id*]

**[undo port access vsan**]

【缺省情况】

接口以Access方式属于VSAN 1。

【视图】

FC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsan-id*]：VSAN的编号，取值范围为1～3839。该VSAN必须是设备上已经创建的VSAN，否则，该命令将执行失败。

【使用指导】

用户既可使用本命令在FC接口或FC聚合接口视图下将当前接口以Access方式加入指定VSAN，也可使用**port**命令在VSAN视图下将FC接口或FC聚合接口以Access方式批量加入当前VSAN。二者的配置优先级相同。

【举例】

\# 创建VSAN 10，并将接口FC1/0/1以Access方式加入该VSAN。

\<Sysname\> system-view

Sysname vsan 10

Sysname-vsan10 quit

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 port access vsan 10

【相关命令】

·**port**

**FC和FCoE \-- VSAN配置命令 \-- port trunk mode**

------------------------------------------------------------------------

**[port** **trunk mode**]命令用来配置当前接口的Trunk模式。

**[undo port trunk mode**]命令用来恢复缺省情况。

【命令】

**[port trunk mode**  { **auto** \| **off** \| **on** }]

**[undo port trunk mode**]

【缺省情况】

接口的Trunk模式为Auto模式。

【视图】

FC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示Auto模式。

**[off**]：表示Off模式。

**[on**]：表示On模式。

【使用指导】

互连的两个接口通过EVFP协议，根据本命令所配置的Trunk模式来协商接口是否支持VSAN Tag。

【举例】

\# 配置接口FC1/0/1的Trunk模式为On模式。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 port trunk mode on

**FC和FCoE \-- VSAN配置命令 \-- port trunk vsan**

------------------------------------------------------------------------

**[port** **trunk vsan**]命令用来将当前接口以Trunk方式加入VSAN。

**[undo port trunk vsan**]命令用来取消将当前接口以Trunk方式加入VSAN的配置。

【命令】

**[port** **trunk vsan** *vsan-id-list*]

**[undo port** **trunk vsan** *vsan-id-list*]

【缺省情况】

接口不以Trunk方式属于任何VSAN。

【视图】

FC接口视图/VFC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsan-id-list*]：VSAN列表，为Trunk接口加入的VSAN的范围，表示方式为*vsan-id-list = *{ *vsan-id1* [ **to** *vsan-id2*  }&\<1-10\>]，*vsan-id*取值范围为1～3839，&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

在FCF-NPV交换机上配置本命令时，在指定的VSAN列表中不建议同时包含FCF模式和NPV模式的VSAN。否则，E_Port将只选择FCF模式的VSAN生效，NP_Port将只选择NPV模式的VSAN生效。

【举例】

\# 配置接口FC1/0/1允许VSAN 1～2、10、20～100通过。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 port trunk vsan 1 to 2 10 20 to 100

\# 配置接口VFC1允许VSAN 1～2、10、20～100通过。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 port trunk vsan 1 to 2 10 20 to 100

【相关命令】

·**working-mode**

**FC和FCoE \-- VSAN配置命令 \-- vsan**

------------------------------------------------------------------------

**[vsan**]命令用来创建VSAN并进入VSAN视图。如果指定的VSAN已创建，则该命令直接用来进入该VSAN的视图。

**[undo vsan**]命令用来删除VSAN。

【命令】

**[vsan** *vsan-id* [ **name** *vsan-name* ]]

**[undo vsan** *vsan-id* [ **name** ]]

【缺省情况】

只存在默认VSAN（VSAN 1）。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsan-id*]：VSAN的编号，取值范围为1～3839。

**[name** *vsan-name*]：VSAN的名称，为1～32个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$ - \^ \_，并且名称的起始字符只能为大小写英文字母。如果创建VSAN时没有指定名称，则VSAN的默认名称由字符串"VSAN"和4位数字的*vsan-id*组合而成。例如，VSAN 10的默认名称为"VSAN0010"。

【使用指导】

需要注意的是：

·初始情况下，只存在默认VSAN（VSAN 1），用户不能创建或删除默认VSAN。用户可以创建的VSAN范围是2～3839。

·每台设备上包括默认VSAN在内，最多可以配置的VSAN数目与设备的型号相关，请以设备的实际情况为准。

·使用**undo vsan**命令时，如果指定了**name**参数，则将VSAN的名称恢复为缺省名称，如果未指定**name**参数，则删除该VSAN。

【举例】

\# 创建VSAN 10，并进入VSAN 10的视图。

\<Sysname\> system-view

Sysname vsan 10

Sysname-vsan10

\# 修改已创建VSAN 10的名称为FCF-VSAN。

\<Sysname\> system-view

Sysname vsan 10 name FCF-VSAN

Sysname-vsan10

\# 创建VSAN 11，为其配置名称为FCF-VSAN，并进入VSAN 11的视图。

\<Sysname\> system-view

Sysname vsan 11 name FCF-VSAN

Sysname-vsan11

\# 将VSAN 11的名称恢复为缺省名称。

\<Sysname\> system-view

Sysname undo vsan 11 name

\# 删除VSAN 11。

\<Sysname\> system-view

Sysname undo vsan 11

【相关命令】

·**display vsan status**

**FC和FCoE \-- VSAN配置命令 \-- working-mode**

------------------------------------------------------------------------

**[working-mode**]命令用来配置VSAN的工作模式。

**[undo working-mode**]命令用来恢复缺省情况。

【命令】

**[working-mode **[{ **fcf** \| **npv** }]]

**[undo working-mode**]

【缺省情况】

VSAN的工作模式为NPV模式。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fcf**]：表示FCF模式。

**[npv**]：表示NPV模式。

【使用指导】

只有FCF-NPV交换机支持本命令。

FCF-NPV交换机在VSAN中的工作模式又可分为以下两种：

·FCF模式：工作在本模式下的VSAN，相当于一台独立的FCF交换机。

·NPV模式：工作在本模式下的VSAN，相当于一台独立的NPV交换机。

需要注意的是，在FCF-NPV交换机上，如果用户配置的接口模式与该接口所属的某个VSAN的工作模式不匹配，则FC接口模式的配置在该VSAN下将不会生效。

【举例】

\# 配置VSAN 10的工作模式为FCF模式。

\<Sysname\> system-view

Sysname vsan 10

Sysname-vsan10 working-mode fcf

【相关命令】

·**display vsan status**

·**fc mode**

**FC和FCoE \-- Fabric网络命令 \-- allowed-domain-id**

------------------------------------------------------------------------

**[allowed-domain-id**]命令用来配置交换机允许的域ID范围。

**[undo** **allowed-domain-id**]命令用来恢复缺省情况。

【命令】

**[allowed-domain-id** *domain-id-list*]

**[undo allowed-domain-id ***domain-id-list*]

【缺省情况】

交换机允许的域ID范围为1～239。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id-list*]：域ID列表，表示允许的域ID范围。表示方式为*domain-id-list* = { *domain-id1* [ **to** *domain-id2*  }&\<1-8\>]。其中，*domain-id1*、*domain-id2*为域ID的值，取值范围为1～239，*domain-id2*必须大于等于*domain-id1*。&\<1-8\>表示前面的参数最多可以输入8次。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

在网络地址分配时，每个FC交换机都会分配到一个域ID，域ID的默认有效范围是1～239，可以通过配置，指定FC交换机允许的域ID范围。

配置允许的域ID范围对交换机的影响如下：

·主交换机：只能从允许的域ID范围内分配域ID。如果配置的允许域ID范围不包含已分配的域ID和本地配置的域ID，配置均会失败。

·非主交换机：手工配置的域ID必须在允许的域ID范围内，否则会配置失败。主交换机为本交换机分配的域ID必须在允许的域ID范围内，否则不接受所分配的域ID，并隔离连接主交换机的接口。如果交换机当前运行时域ID（动态分配或者手工指定域ID后，交换机实际使用的域ID）不在新配置的允许的域ID范围内时，将导致配置失败。

建议为一个VSAN内的所有交换机都配置相同的允许域ID范围。

【举例】

\# 在VSAN 1内配置交换机允许的域ID范围为3～10。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 allowed-domain-id 3 to 10

**FC和FCoE \-- Fabric网络命令 \-- display fc domain**

------------------------------------------------------------------------

**[display fc domain**]命令用来显示VSAN内的域信息。

【命令】

**[display fc domain** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的域信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的域信息。在FCF-NPV交换机上，只能显示FCF模式VSAN内的域信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看VSAN下的域信息，主要包含以下内容：本交换机运行时信息、本交换机配置信息以及主交换机运行时信息。

【举例】

\# 显示VSAN 1内的域信息。

\<Sysname\> display fc domain vsan 1

Domain Information of VSAN 1:

    Running time information:

        State: Stable

        Switch WWN: 41:6e:64:69:61:6d:6f:21

        Fabric name: 41:6e:64:69:61:6d:6f:21

        Priority: 2

        Domain ID: 100

    Configuration information:

        Domain configure: Enabled

        Domain auto-reconfigure: Disabled

        Fabric name: 41:6e:64:69:61:6d:6f:21

        Priority: 128

        Domain ID: 100 (static)

    Principal switch running time information:

        Priority: 2

    Path               Interface

    Downstream         Fc1/0/1

    Downstream         Fc1/0/2

    Downstream         Fc1/0/4

表1-20 display fc domain命令显示信息描述表

字段

描述

Domain Information of VSAN 1

VSAN 1内的域信息

Running time information

本交换机运行时信息

State

本交换机运行状态，包括：

·Stable：表示配置结束

·Unstable：表示配置还未结束

Switch WWN

本交换机的WWN

Fabric name

Fabric网络的名称

Priority

本交换机的运行优先级

Domain ID

本交换机的运行域ID

Configuration information

本交换机配置信息

Domain configure

Fabric配置功能开启情况，包括：

·Enabled：表示开启Fabric配置功能

·Disabled：表示关闭Fabric配置功能

Domain auto-reconfigure

自动重配置功能开启情况，包括：

·Enabled：表示交换机开启自动重配置功能

·Disabled：表示交换机关闭自动重配置功能

Fabric name

本交换机上配置的Fabric网络的名称

Priority

本交换机上配置的优先级

Domain ID

本交换机上配置的域ID。括号中内容的含义：

·static：表示该域ID是静态模式的

·preferred：表示该域ID是可选模式的

Principal switch running time information

主交换机运行时信息

Priority

主交换机的运行优先级

Path

接口路径类型，包括：

·Upstream：表示上游主链路

·Downstream：表示下游主链路

Interface

本地的FC接口

**FC和FCoE \-- Fabric网络命令 \-- display fc domain-list**

------------------------------------------------------------------------

**[display fc domain-list**]命令用来显示VSAN内动态分配的域列表。

【命令】

**[display fc domain-list** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内动态分配的域列表，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内动态分配的域列表。在FCF-NPV交换机上，只能显示FCF模式VSAN内动态分配的域列表。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

在开启Fabric配置功能、动态建立Fabric网络时，使用本命令可以查看VSAN内动态分配的域列表信息，包括域的总数目、域ID和交换机WWN的对应关系。

【举例】

\# 显示VSAN 1内动态分配的域列表。

\<Sysname\> display fc domain-list vsan 1

Domain list of VSAN 1:

  Number of domains: 3

  Domain ID    WWN

  0xc8(200)    20:01:00:05:30:00:47:df [Principal]

  0x63(99)     20:01:00:0d:ec:08:60:c1 [Local]

  0x61(97)     50:00:53:0f:ff:f0:10:06

表1-21 display fc domain-list命令显示信息描述表

字段

描述

Domain list of VSAN

VSAN内的域列表

Number of domains

域的总数目

Domain ID

域ID

WWN

交换机的WWN。Principal表示主交换机，Local表示本地交换机

【相关命令】

·**domain configure enable**

**FC和FCoE \-- Fabric网络命令 \-- display fc ess**

------------------------------------------------------------------------

**[display fc ess**]命令用来显示ESS（Exchange Switch Support，交换机能力协商）协商结果。

【命令】

**[display fc ess** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的ESS协商结果，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的ESS协商结果。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看ESS协商结果，包括本交换机的能力和完成ESS协商的远端交换机的能力。

关于各种交换机能力的详细介绍请查看相关的协议文档。

【举例】

\# 显示VSAN 2内的ESS协商结果。

\<Sysname\> display fc ess vsan 2

ESS info of VSAN 2:

  Domain: 210

    Directory Server Capability:

      Accept large name server objects: Yes

      Accept small name server objects: No

      Accept large + FC-4 Features name server objects: No

      Accept small + FC-4 Features name server objects: No

      Support receiving ACCept with 0 length: Yes

    Fabric Controller Capability:

     Support receiving the SW_RSCN Request: Yes

    Fabric Configuration Server Capability:

      Support basic configuration services: Yes

      Support platform configuration services: No

      Support topology discovery configuration services: Yes

      Support enhanced configuration services: Yes

    Enhanced Zone Server Capability:

      Support enhanced zoning management: Yes

表1-22 display fc ess命令显示信息描述表

字段

描述

ESS info of VSAN

指定VSAN内的ESS信息

Domain

交换机的域ID

Directory Server Capability

目录服务器能力列表

Accept large name server objects

交换机是否支持接收大模式的名称服务对象：yes表示支持，no表示不支持

（大模式下，除了包含小模式的信息之外，还包括N端口符号名称和N节点符号名称信息）

Accept small name server objects

交换机是否支持接收小模式的名称服务对象：Yes表示支持，No表示不支持

（小模式下，只有基本信息，不包括N端口符号名称、N节点符号名称以及所支持的FC-4特性信息）

Accept large + FC-4 Features name server objects

交换机是否支持接收大模式+FC-4特性的名称服务对象：Yes表示支持，No表示不支持

Acceptsmall + FC-4 Features name server objects

交换机是否支持接收小模式+FC-4特性的名称服务对象：Yes表示支持，No表示不支持

Support receiving ACCept with 0 length

交换机是否支持接收负载为0的名称服务ACC回应报文：Yes表示支持，No表示不支持

Fabric Controller Capability

网络控制器能力列表

Support receiving the SW_RSCN Request

交换机是否支持接收SW_RSCN请求报文：Yes表示支持，No表示不支持

Fabric Configuration Server Capability

网络配置服务能力列表

Support basic configuration services

交换机是否支持基本配置服务：Yes表示支持，No表示不支持

Support platform configuration services

交换机是否支持平台配置服务：Yes表示支持，No表示不支持

Support topology discovery configuration services

交换机是否支持拓扑发现配置服务：Yes表示支持，No表示不支持

Support enhanced configuration services

交换机是否支持增强配置服务：Yes表示支持，No表示不支持

Enhanced Zone Server Capability

增强Zone能力列表

Support enhanced zoning management

交换机是否支持增强Zone模式：Yes表示支持，No表示不支持

**FC和FCoE \-- Fabric网络命令 \-- display fc login**

------------------------------------------------------------------------

**[display fc login**]命令用来显示节点注册的相关信息。

【命令】

**[display fc login** [ **vsan** *vsan-id*   **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：指定所属VSAN，取值范围为1～3839。不指定该参数，将显示所有VSAN的信息。在FCF-NPV交换机上，只能显示FCF模式VSAN的信息。

**[count**]：显示登录节点的数目。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示VSAN 1的节点注册的相关信息。

\<Sysname\> display fc login vsan 1

Interface VSAN FCID     Node WWN                Port WWN

Fc1/0/1   1    0x010000 21:01:00:1b:32:a0:fa:18 21:01:00:1b:32:a0:fa:17

\# 显示VSAN 1的登录节点的数目。

\<Sysname\> display fc login vsan 1 count

Total entries: 1

\# 显示所有VSAN的登录节点的数目。

\<Sysname\> display fc login count

VSAN        Entries

1           1

2           1

Total entries: 2

表1-23 display fc login命令显示信息描述表

字段

描述

Interface

交换机上和节点相连的接口

VSAN

VSAN ID

FCID

交换机为节点分配的FC地址

Node WWN

节点WWN

Port WWN

节点上和交换机相连的端口的WWN

Entries

某VSAN内登录节点的数目

Total entries

登录节点的总数目

**FC和FCoE \-- Fabric网络命令 \-- display fc name-service database**

------------------------------------------------------------------------

**[display fc name-service database**]命令用来显示名称服务数据库信息。

【命令】

**[display fc name-service database ** **vsan** *vsan-id*  **fcid** *fcid*  ]  **verbose**

**[display fc name-service database** [ **vsan** *vsan-id*  **count**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的名称服务数据库信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的名称服务数据库信息。

**[fcid** *fcid*]：显示FC地址为*fcid*的名称服务数据库表项。*fcid*的取值范围为0x010000～0xEFFFFF（十六进制）。不指定该参数时，将显示所有FC地址的表项。

**[verbose**]：显示名称服务数据库的详细信息。不指定该参数时，将显示名称服务数据库的简要信息。

**[count**]：显示名称服务数据库表项的数目。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示VSAN 1内的名称服务数据库的简要信息。

\<Sysname\> display fc name-service database vsan 1

VSAN 1:

  FCID     Type               PWWN(vendor)                      FC4-type:feature

  0x030001 0x01(N)            20:00:00:05:30:00:25:a3           SCSI-FCP

  0x030200 0x01(N)            20:00:00:49:c9:28:c7:01           NPV

\# 显示名称服务数据库的详细信息。

\<Sysname\> display fc name-service database verbose

VSAN:1     FCID:0x030001

  Port-WWN(vendor): 20:00:00:05:30:00:25:a3

  Node-WWN: 20:00:00:05:30:00:25:9e

Class: 2,3

  Node-IP-addr: 192.168.0.52

  FC4-types(FC4_features): SCSI-FCP

  Symbolic-port-name:

  Symbolic-node-name:

  Port-type: 0x01(N)

  Fabric-port-WWN: 30:30:30:30:65:33:64:6

  Hard-addr: 0x000000

VSAN:1     FCID:0x030200

  Port-WWN(vendor): 20:00:00:5a:c9:28:c7:01

  Node-WWN: 10:00:00:5a:c9:28:c7:01

  Class: 3

  Node-IP-addr: 192.168.6.171

  FC4-types(FC4_features): NPV

  Symbolic-port-name: NPV-Sysname:Vfc1

  Symbolic-node-name: NPV-Sysname

  Port-type: 0x01(N)

  Fabric-port-WWN: 22:0a:00:05:30:00:26:1e

  Hard-addr: 0x000000

\-\-- Total 2 entries \-\--

\# 显示VSAN 1内的名称服务数据库表项的数目。

\<Sysname\> display fc name-service database vsan 1 count

Total entries: 2

表1-24 display fc name-service database命令显示信息描述表

字段

描述

VSAN

指定VSAN内的信息

FCID

N端口的FC地址

Type

节点向交换机注册的端口类型，包括：

·0x00(Unidentified)：表示未注册端口类型

·0x01(N)：表示N端口。N端口通过直连方式连接到Fabric

·0x02(NL)：表示NL端口。NL端口通过仲裁环连接到Fabric

·0x03(F/NL)：表示F端口或者NL端口

·0x7f(Nx)：表示N端口、NL端口、F/NL端口

·0x81(F)：表示F端口。F端口与N端口相连

·0x82(FL)：表示FL端口。FL端口与NL端口相连

·0x84(E)：表示E端口。E端口与E端口或B端口相连

·0x85(B)：表示B端口。如果两个E端口之间通过桥设备连接，那么桥设备上连接E端口的端口就是B端口

·0xXX(Unknown)：表示以上取值以外的其它端口类型

![说明](FC和FCoE命令.files/image002.png)

正常情况下节点只会注册两种端口类型：N端口、NL端口。

PWWN(vendor)

N端口的WWN（制造厂商名称）

FC4-type:feature

FC4类型：属性（显示简要信息时，最多显示两条FC4类型：属性）

·FC4类型包括：SCSI-FCP、LLC/SNAP、SW_ILS、SNMP、GS3、VI、NPV

·属性包括：支持Initiator、支持Target、两者都支持Initiator/Target

表1-25 display fc name-service database verbose命令显示信息描述表

字段

描述

VSAN

指定VSAN内的信息

FCID

N端口的FC地址

Port-WWN(vendor)

N端口的WWN（制造厂商名称）

Node-WWN

N节点的WWN

Class

CLASS服务级别

Node-IP-addr

N节点的IP地址

FC4-types(FC4 features)

FC4类型（属性）

·FC4类型包括：SCSI-FCP、LLC/SNAP、SW_ILS、SNMP、GS3、VI、NPV

·属性包括：支持Initiator、支持Target、两者都支持Initiator/Target

Symbolic-port-name

N端口的符号名称，用于描述此端口。H3C的NPV交换机会携带本机系统名和端口名，注册形如*system-name*:*port-name*的字符串作为端口描述名

Symbolic-node-name

N节点的符号名称，用于描述此节点。H3C的NPV交换机会携带本机系统名，注册形如*system-name*的字符串作为节点描述名

Port-type

节点向交换机注册的端口类型，包括：

·0x00(Unidentified)：表示未注册端口类型

·0x01(N)：表示N端口。N端口通过直连方式连接到Fabric

·0x02(NL)：表示NL端口。NL端口通过仲裁环连接到Fabric

·0x03(F/NL)：表示F端口或者NL端口

·0x7f(Nx)：表示N端口、NL端口、F/NL端口

·0x81(F)：表示F端口。F端口与N端口相连

·0x82(FL)：表示FL端口。FL端口与NL端口相连

·0x84(E)：表示E端口。E端口与E端口或B端口相连

·0x85(B)：表示B端口。如果两个E端口之间通过桥设备连接，那么桥设备上连接E端口的端口就是B端口

·0xXX(Unknown)：表示以上取值以外的其它端口类型

![说明](FC和FCoE命令.files/image002.png)

正常情况下节点只会注册两种端口类型：N端口、NL端口。

Fabric-port-WWN

F端口的WWN

Hard-addr

N端口的硬件地址

Total entries

此VSAN内的表项数目

**FC和FCoE \-- Fabric网络命令 \-- display fc scr-table**

------------------------------------------------------------------------

**[display fc scr-table**]命令用来显示N端口注册的SCR（State Change Registration，状态变化注册）列表。

【命令】

**[display fc scr-table** [ **vsan** *vsan-id*   **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的SCR列表，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的SCR列表。

**[count**]：显示SCR表项的数目。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示SCR列表。

\<Sysname\> display fc scr-table

SCR table for VSAN 1:

FCID         REGISTERED FOR

0x1b0300     fabric detected rscns

0x010121     nx_port detected rscns

\-\-- Total 2 entries \-\--

\# 显示SCR表项数目。

\<Sysname\> display fc scr-table vsan 1 count

Total entries: 2

表1-26 display fc scr-table命令显示信息描述表

字段

描述

SCR table for VSAN

指定VSAN内的SCR列表

FCID

N端口的FC地址

REGISTERED FOR

注册接收RSCN（Registered State Change Notification，注册状态变化通知）报文的种类：

·fabric detected rscns：表示注册接收所有由Fabric中的交换机感知到状态变化而发送的RSCN报文

·nx_port detected rscns：表示注册接收所有由N端口感知到状态变化而发送的RSCN报文

·full detected rscns：表示注册接收所有的RSCN报文

Total entries

此VSAN内的表项数目

**FC和FCoE \-- Fabric网络命令 \-- display fc switch-wwn**

------------------------------------------------------------------------

**[display fc switch-wwn**]命令用来显示本交换机的WWN。

【命令】

**[display fc switch-wwn**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示本交换机的WWN。

\<Sysname\> display fc switch-wwn

Switch WWN is 10:00:00:0d:ec:ff:a3:25

**FC和FCoE \-- Fabric网络命令 \-- display fc timer**

------------------------------------------------------------------------

**[display fc timer**]命令用来显示Fabric定时器信息。

【命令】

**[display fc timer**[ [ **distributed-services** \| **error-detect** \| **resource-allocation** ]  **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[distributed-services**]：显示分布式服务超时时间。

**[error-detect**]：显示错误检测超时时间。

**[resource-allocation**]：显示资源分配超时时间。

**[vsan** *vsan-id*]：显示指定VSAN内的Fabric定时器信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示全局Fabric定时器信息。

【使用指导】

如果配置命令时不指定**distributed-services**、**error-detect**、**resource-allocation**参数，将显示所有Fabric定时器的信息。

【举例】

\# 显示VSAN 1内的所有Fabric定时器信息。

\<Sysname\> display fc timer vsan 1

Timer of VSAN 1:

  Distributed-services timer: 5000 ms

  Error-detect timer:         2000 ms

  Resource-allocation timer:  10000 ms

表1-27 display fc timer命令显示信息描述表

字段

描述

Timer of VSAN

指定VSAN内的Fabric定时器信息

Distributed-services timer

分布式服务超时时间，单位为毫秒

Error-detect timer

错误检测超时时间，单位为毫秒

Resource-allocation timer

资源分配超时时间，单位为毫秒

**FC和FCoE \-- Fabric网络命令 \-- display fcid allocation**

------------------------------------------------------------------------

**[display** **fcid** **allocation**]命令用来显示FCID的分配情况。

【命令】

**[display** **fcid** **allocation** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的信息，*vsan-id*的取值范围为1～3839。如果未指定本参数，将显示所有VSAN内的信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示VSAN 1内的FCID分配情况。

\<Sysname\> display fcid allocation vsan 1

VSAN 1:

Free FCIDs: 0xef0000 to 0xef06ff

            0xef0701 to 0xef08ff

            0xef0901 to 0xefffff

Assigned FCIDs: 0xef0700

                0xef0900

Number of free FCIDs: 65534

Number of assigned FCIDs: 2

表1-28 display fcid allocation命令显示信息描述表

字段

描述

VSAN 1

VSAN ID

Free FCIDs

未分配的FCID

Assigned FCIDs

已分配的FCID

Number of free FCIDs

未分配的FCID数量

Number of assigned FCIDs

已分配的FCID数量

**FC和FCoE \-- Fabric网络命令 \-- display fcid persistent**

------------------------------------------------------------------------

**[display** **fcid** **persistent**]命令用来显示FCID持久化表项信息。

【命令】

**[display** **fcid** **persistent** [ **unused**   **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[unused**]：显示当前尚未使用（即对应节点未登录）的FCID持久化表项。如果未指定本参数，将显示所有的FCID持久化表项。

**[vsan** *vsan-id*]：显示指定VSAN内的信息，*vsan-id*的取值范围为1～3839。如果未指定本参数，将显示所有VSAN内的信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示所有VSAN内的FCID持久化表项信息。

\<Sysname\> display fcid persistent

VSAN 1:

FCID persistence: Enabled

Total entries: 3

WWN                      FCID       Used   Assignment

10:00:00:00:c9:ef:39:5f  0x1e0002   Yes    Dynamic

10:00:00:00:c9:ef:39:60  0x1e1000   Yes    Static

10:00:00:00:c9:ef:39:68  0x1e000a   Yes    Dynamic

VSAN 2:

FCID persistence: Disabled

Total entries: 0

表1-29 display fcid allocation命令显示信息描述表

字段

描述

VSAN

VSAN ID

FCID persistence

FCID持久化功能的开启状态，包括：

·{.TableTextChar}[Enabled]{.TableTextChar}：{.TableTextChar}表示{.TableTextChar}已{.TableTextChar}开启{.TableTextChar}

·Disabled：表示已关闭

WWN

节点的WWN

FCID

交换机为节点分配的FC地址

Used

分配的FCID的使用情况，包括：

·Yes：表示节点在线，正在使用

·No：表示节点不在线，未使用

Assignment

分配的FCID类型，包括：

·Dynamic：表示动态

·Static：表示静态

Total entries

FCID持久化表项的总数

**FC和FCoE \-- Fabric网络命令 \-- domain auto-reconfigure enable**

------------------------------------------------------------------------

**[domain auto-reconfigure enable**]命令用来开启自动Fabric重配置功能。

**[undo domain auto-reconfigure enable**]命令用来恢复缺省情况。

【命令】

**[domain auto-reconfigure enable**]

**[undo domain auto-reconfigure enable**]

【缺省情况】

自动Fabric重配置功能处于关闭状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

Fabric重配置将触发整个网络重新开始主交换机选举、域ID分配和FC地址分配。

自动Fabric重配置功能一般在网络出现故障或者合并时发生：

·两个Fabric网络合并时，如果域ID列表重叠，交换机会自动进行中断重配置。

·两个Fabric网络合并时，如果两个Fabric网络的主交换机信息不同，而且域ID列表非空且不重叠，系统会自动进行非中断重配置。

·主交换机宕机时，系统会自动进行非中断重配置。

需要注意的是，只有开启了Fabric配置功能后，本命令才会生效。

【举例】

\# 在VSAN 1内开启自动Fabric重配置功能。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 domain auto-reconfigure enable

【相关命令】

·**domain configure enable**

**FC和FCoE \-- Fabric网络命令 \-- domain configure enable**

------------------------------------------------------------------------

**[domain configure enable**]命令用来开启Fabric配置功能。

**[undo** **domain** **configure** **enable**]命令用来关闭Fabric配置功能。

【命令】

**[domain configure enable**]

**[undo domain configure enable**]

【缺省情况】

VSAN内的Fabric配置功能处于开启状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

开启了Fabric配置功能后，FC交换机会通过消息交互选举主交换机，并由选举出来的主交换机为网络中的所有交换机动态分配域ID。因此，在动态建立Fabric网络时，必须在VSAN内的所有交换机上都开启Fabric配置功能；而在静态建立Fabric网络时，则必须在VSAN内的所有交换机上都关闭Fabric配置功能，需要手工配置各交换机的域ID。

【举例】

\# 在VSAN 1内开启Fabric配置功能。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 domain configure enable

**FC和FCoE \-- Fabric网络命令 \-- domain restart**

------------------------------------------------------------------------

**[domain restart**]命令用来手工发起Fabric重配置。

【命令】

**[domain restart** [ **disruptive** ]]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disruptive**]：表示发起中断重配置。如果未指定本参数，表示发起非中断重配置。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

Fabric重配置一般在网络改造（比如两个Fabric网络合并等）或外部干预（比如管理员通过命令行发起重配置）时发生。Fabric重配置将触发整个网络重新开始主交换机选举、域ID分配和FC地址分配。

根据重配置过程中对Fabric网络的影响程度不同，可将Fabric重配置分为以下两种：

·中断重配置：在整个Fabric中洪泛RCF（Reconfigure Fabric，重配置Fabric）报文，通知所有交换机进行中断重配置。重配置过程中，会清除所有运行数据重新进行协商，因此整个Fabric网络的数据传输都会中断。

·非中断重配置：在整个Fabric中洪泛BF（Build Fabric，建立Fabric）报文，通知所有交换机进行非中断重配置。重配置过程中，会尽量保留上一次的运行数据，以保证交换机的域ID尽量不发生变化，从而不影响Fabric网络的数据传输。

对于配置之后不会立即生效的Fabric配置（比如修改了交换机的优先级），需要执行中断重配置使其生效。

需要注意的是，只有开启了Fabric配置功能后，本命令才生效。

【举例】

\# 手工在VSAN 1内发起中断重配置。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 domain restart disruptive

【相关命令】

·**domain configure enable**

**FC和FCoE \-- Fabric网络命令 \-- domain-id**

------------------------------------------------------------------------

**[domain-id**]命令用来配置交换机的域ID。

**[undo** **domain-id**]命令用来恢复缺省情况。

【命令】

**[domain-id**[ *domain-id* { **preferred** \| **static** }]]

**[undo domain-id**]

【缺省情况】

交换机的域ID为0，采用preferred模式。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id*]：域ID，取值范围为1～239。

**[preferred**]：preferred模式。

**[static**]：static模式。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

虽然上层协议只能识别WWN，但实际报文传输时，在FC交换机之间的路由和转发使用的都是域ID。域ID是8位的地址，域ID是按每个VSAN进行分配的，也存在默认值。因为域ID的默认值都为0，无法区分不同的设备，所以在使用前必须分配域ID，可以通过静态配置，也可以动态分配。

需要注意的是：

·如果通过静态配置指定域ID，则需要为Fabric网络中的每台交换机都指定域ID，且每台交换机的域ID必须是唯一的。在静态配置域ID情况下，preferred模式和static模式没有区别。

·如果动态分配域ID，则由主交换机负责为网络中的每台交换机分配域ID。在动态获取域ID情况下，当非主交换机向主交换机请求分配配置的域ID失败时，preferred模式下，非主交换机可以使用主交换机分配的其它域ID；static模式下，非主交换机将隔离上游主链路。

·建议为一个VSAN内的所有交换机都配置相同模式的域ID。

【举例】

\# 在VSAN 1内配置交换机的域ID为55，采用static模式。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 domain-id 55 static

**FC和FCoE \-- Fabric网络命令 \-- fabric-name**

------------------------------------------------------------------------

**[fabric-name**]命令用来配置Fabric网络的名称。

**[undo** **fabric-name**]命令用来恢复缺省情况。

【命令】

**[fabric-name** *name*]

**[undo fabric-name**]

【缺省情况】

使用WWN作为Fabric网络的名称。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：表示Fabric网络的名称，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

FC交换机支持为每个VSAN分配一个Fabric网络名称，其格式与WWN格式相同，是一个64位的地址。当VSAN创建后，如果用户未配置Fabric网络的名称，则使用本交换机的WWN作为Fabric网络的名称。

需要注意的是，仅在静态建立Fabric网络时才需要配置Fabric网络的名称，并且同一VSAN内所有交换机的Fabric网络名称必须一样。动态建立Fabric网络时并不需要配置Fabric网络的名称，系统将使用主交换机的WWN作为Fabric网络的名称。

【举例】

\# 在VSAN 1内配置Fabric网络的名称为10:11:12:13:14:15:16:17。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 fabric-name 10:11:12:13:14:15:16:17

**FC和FCoE \-- Fabric网络命令 \-- fc domain rcf-reject**

------------------------------------------------------------------------

**[fc** **domain** **rcf-reject**]命令用来配置接口拒绝收到的指定VSAN内的RCF请求报文。

**[undo** **fc** **domain** **rcf-reject**]命令用来恢复缺省情况。

【命令】

**[fc domain rcf-reject vsan** *vsan-id*]

**[undo fc domain rcf-reject vsan** *vsan-id*]

【缺省情况】

接口不拒绝收到的RCF请求报文。

【视图】

FC接口视图/FC聚合接口视图/VFC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan** *vsan-id*]：指定所属VSAN，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

在一个稳定的网络中，可以配置接口拒绝收到的特定VSAN内的RCF请求报文，以防止设备进行不必要的中断重配置。配置该功能后，如果接口收到该VSAN内的RCF请求报文，设备会回应拒绝报文，并将该接口隔离。

【举例】

\# 配置接口FC1/0/1拒绝收到的VSAN 1内的RCF请求报文。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fc domain rcf-reject vsan 1

\# 配置接口VFC1拒绝收到的VSAN 1内的RCF请求报文。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fc domain rcf-reject vsan 1

**FC和FCoE \-- Fabric网络命令 \-- fc login-limit**

------------------------------------------------------------------------

**[fc login-limit**]命令用来配置VSAN下的最大登录节点数。

**[undo fc login-limit**]命令用来恢复缺省情况。

【命令】

**[fc login-limit** *max-number*]

**[undo fc login-limit**]

【缺省情况】

不限制VSAN下的最大登录节点数。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-number*]：VSAN下的最大登录节点数目，取值范围为1～65535。

【使用指导】

只有FCF交换机支持本命令。

本命令用于配置VSAN下的最大登录节点数，以防止某VSAN下的登录节点过多，占用大量的ACL资源。这里的登录节点数＝交换机直连的NPV交换机的数＋登录到本交换机上的服务器和磁盘数。

如果已登录节点数大于配置的最大登录节点数，不会将已登录节点强制下线，但后续任何新节点均无法登陆。用户可以通过手工关闭接口等方式将不需要的节点下线。

需要注意的是，登录节点数即受本命令、也受硬件ACL资源的限制，当硬件ACL资源耗尽时，新节点也无法登录。

【举例】

\# 配置VSAN 2下最多登录256个节点。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fc login-limit 256

**FC和FCoE \-- Fabric网络命令 \-- fc name-service auto-discovery**

------------------------------------------------------------------------

**[fc name-service auto-discovery**]命令用来开启Fabric自动发现SCSI-FCP信息功能。

**[undo fc name-service auto-discovery**]命令用来关闭Fabric自动发现SCSI-FCP信息功能。

【命令】

**[fc name-service auto-discovery**]

**[undo fc name-service auto-discovery**]

【缺省情况】

Fabric自动发现SCSI-FCP信息功能处于开启状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

某些节点设备有时不会主动注册支持SCSI-FCP协议（比如节点设备离线又重新上线后，不再主动注册FC4-Type或Feature），也因此没有SCSI-FCP协议对应的Feature值，对节点设备间的互通可能产生影响。

Fabric自动发现SCSI-FCP信息功能可以主动获取节点设备的SCSI-FCP协议及其对应的Feature值，开启该功能后，FCF交换机在节点设备登录后，会主动向节点设备发送PRLI报文，询问节点设备是否支持SCSI-FCP协议，同时获取节点设备支持SCSI-FCP协议对应的Feature信息，并将此信息保存在名称服务数据库中。

需要注意的是，开启Fabric自动发现SCSI-FCP信息功能后，某些较老型号的网卡可能不会再向交换机自动注册节点设备信息。请用户根据实际情况选择是否开启本功能。

【举例】

\# 在VSAN 2内开启Fabric自动发现SCSI-FCP信息功能。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fc name-server auto-discovery

**FC和FCoE \-- Fabric网络命令 \-- fc timer distributed-services**

------------------------------------------------------------------------

**[fc timer** **distributed-services**]命令用来全局配置分布式服务超时时间。

**[undo fc timer** **distributed-services**]命令用来恢复缺省情况。

【命令】

**[fc timer distributed-services** *value*]

**[undo fc timer distributed-services**]

【缺省情况】

分布式服务超时时间为5000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：分布式服务超时时间，取值范围为5000～10000，单位为毫秒。

【使用指导】

本命令与**timer distributed-services**命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有VSAN都有效，VSAN视图下的配置只对当前VSAN有效，后者的配置优先级较高。

【举例】

\# 全局配置分布式服务超时时间为6000毫秒。

\<Sysname\> system-view

Sysname fc timer distributed-services 6000

【相关命令】

·**timer distributed-services**

**FC和FCoE \-- Fabric网络命令 \-- fc timer error-detect**

------------------------------------------------------------------------

**[fc timer** **error-detect**]命令用来全局配置错误检测超时时间。

**[undo fc timer** **error-detect**]命令用来恢复缺省情况。

【命令】

**[fc timer error-detect** *value*]

**[undo fc timer error-detect**]

【缺省情况】

错误检测超时时间为2000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：错误检测超时时间，取值范围为1000～10000，单位为毫秒。

【使用指导】

本命令与**timer error-detect**命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有VSAN都有效，VSAN视图下的配置只对当前VSAN有效，后者的配置优先级较高。

【举例】

\# 全局配置错误检测超时时间为6000毫秒。

\<Sysname\> system-view

Sysname fc timer error-detect 6000

【相关命令】

·**timer** **error-detect**

**FC和FCoE \-- Fabric网络命令 \-- fc timer resource-allocation**

------------------------------------------------------------------------

**[fc timer** **resource-allocation**]命令用来全局配置资源分配超时时间。

**[undo fc timer** **resource-allocation**]命令用来恢复缺省情况。

【命令】

**[fc timer resource-allocation** *value*]

**[undo fc timer resource-allocation**]

【缺省情况】

资源分配超时时间为10000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：资源分配超时时间，取值范围为5000～10000，单位为毫秒。

【使用指导】

本命令与**timer resource-allocation**命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有VSAN都有效，VSAN视图下的配置只对当前VSAN有效，后者的配置优先级较高。

【举例】

\# 全局配置资源分配超时时间为6000毫秒。

\<Sysname\> system-view

Sysname fc timer resource-allocation 6000

【相关命令】

·**timer resource-allocation**

**FC和FCoE \-- Fabric网络命令 \-- fc wwn default-fc4-type**

------------------------------------------------------------------------

**[fc wwn default-fc4-type**]命令用来配置节点设备的默认FC4信息。

**[undo fc wwn default-fc4-type**]命令用来删除配置的节点设备的默认FC4信息。

【命令】

**[fc wwn ***wwn-value ***default-fc4-type**[ { *type-value* **feature** *feature-map \|* **scsi-fcp** **feature** { *feature-map \|* **both** *\|* **initiator** *\|* **target** } }]]

**[undo fc wwn ***wwn-value ***default-fc4-type**[ { *type-value \|* **scsi-fcp** }]]

【缺省情况】

没有配置节点设备的默认FC4信息。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[wwn-value*]：N_Port的WWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

*[type-value*]：表示支持的FC4-Type。FC4-Type由256比特构成，每个比特位表示一种类型，某位比特的值为1，则表示支持该比特位对应的类型。*type-value*值表示置位所支持的FC4-Type的对应比特位，取值范围为0～255。

**[scsi-fcp**]：表示支持的FC4-Type为SCSI-FCP，对应的*type-value*值为8。

**[feature ***feature-map*]：表示支持FC4-Type的Feature值。每种协议共有四种属性，Feature值由4个比特组成，每个比特位表示一种属性，取值范围为0～15。某位比特的值为1，则表示支持该比特位对应的属性。[例如，]Feature值配置为15，表示节点设备对于该FC4-Type对应的四种属性全部都支持。Feature值为0表示不支持任何属性。当FC4-Type为SCSI-FCP时，用户还可配置如下参数：

·**target**：表示支持target属性，对应的*feature-map*值为1。

·**initiator**：表示支持initiator属性，对应的*feature-map*值为2。

·**both**：表示同时支持initiator和target属性，对应的*feature-map*值为3。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

为了不影响节点设备之间的互通，用户可以手工配置节点设备的默认FC4信息（FC4-Type和Feature）。当节点设备不注册FC4信息并且交换机主动探测SCSI-FCP信息也不成功时，名称服务数据库中记录的将是该默认FC4信息。此后，如果节点设备又主动注册了FC4信息或交换机又探测到了SCSI-FCP信息，则名称服务数据库中将保存节点设备注册或交换机探测到的FC4信息。

配置本命令时，每条配置命令只能表示某个N_Port支持的一种FC4-Type及其Feature，如果该N_Port还支持其它FC4-Type及其Feature，则需要再配置一条命令。

【举例】

\# 配置节点设备（其WWN为00:00:00:11:22:33:44:55）的默认FC4信息。

\<Sysname\> system-view

Sysname fc wwn 00:00:00:11:22:33:44:55 default-fc4-type scsi-fcp feature target

Sysname fc wwn 00:00:00:11:22:33:44:55 default-fc4-type 9 feature 7

**FC和FCoE \-- Fabric网络命令 \-- fcid persistent enable**

------------------------------------------------------------------------

**[fcid** **persistent** **enable**]命令用来开启FCID持久化功能。

**[undo** **fcid** **persistent** **enable**]命令用来关闭FCID持久化功能。

【命令】

**[fcid** **persistent** **enable**]

**[undo** **fcid** **persistent** **enable**]

【缺省情况】

FCID持久化功能处于开启状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

需要注意的是：

·开启本功能后，手工配置的FCID持久化表项才能生效。

·关闭本功能时，会删除所有静态和动态的FCID持久化表项。

·关闭本功能后，曾登录过的节点的WWN与FCID的对应关系也会被记录下来，在重新开启FCID持久化功能时，系统会尝试将其恢复为动态的FCID持久化表项。在此恢复过程中，如果FCID持久化表项的总数达到了系统上限（40000条），系统会删除当前所有离线节点的动态表项后，再继续恢复。

【举例】

\# 在VSAN 1内关闭FCID持久化功能。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 undo fcid persistent enable

【举例】

·**wwn** **fcid**

**FC和FCoE \-- Fabric网络命令 \-- priority**

------------------------------------------------------------------------

**[priority**]命令用来配置交换机的优先级。

**[undo** **priority**]命令用来恢复缺省情况。

【命令】

**[priority** *value*]

**[undo priority**]

【缺省情况】

交换机的优先级为128。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：交换机的优先级，取值范围为1～254。优先级值越小，优先级越高。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

在一个VSAN中，优先级高的交换机将优先被选为主交换机。同一台FC交换机在不同VSAN中的优先级可以不同。

需要注意的是，交换机优先级的配置不能立即生效，需通过命令**domain restart** **disruptive**进行一次中断重配置后才能生效。

【举例】

\# 在VSAN 1内配置交换机的优先级为64。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 priority 64

【相关命令】

·**domain restart**

**FC和FCoE \-- Fabric网络命令 \-- reset fcid persistent**

------------------------------------------------------------------------

**[reset** **fcid** **persistent**]命令用来清除FCID持久化表项信息。

【命令】

**[reset** **fcid** **persistent** [ **static**   **vsan** *vsan-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[static**]：表示清除静态表项。如果未指定本参数，表示清除动态表项。

**[vsan** *vsan-id*]：清除指定VSAN内的信息，*vsan-id*的取值范围为1～3839。如果未指定本参数，将清除所有VSAN内的信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

需要注意的是，本命令不会清除在线节点的FCID持久化表项。

【举例】

\# 清除VSAN 1下的所有动态FCID持久化表项。

\<Sysname\> reset fcid persistent vsan 1

**FC和FCoE \-- Fabric网络命令 \-- rscn aggregation enable**

------------------------------------------------------------------------

**[rscn aggregation enable**]命令用来开启RSCN聚合功能。

**[undo rscn aggregation enable**]命令用来关闭RSCN聚合功能。

【命令】

**[rscn aggregation enable**]

**[undo rscn aggregation enable**]

【缺省情况】

RSCN聚合功能处于关闭状态。

【视图】

VSAN视图

【缺省级别】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

开启RSCN聚合功能后，如果在RSCN聚合等待时间内，有多个节点设备产生变化事件，则使用携带了多个变化FC地址的一个ELS_RSCN报文，来代替以前只携带一个变化FC地址的多个ELS_RSCN报文，以此减少向关心该变化的节点设备发送ELS_RSCN报文的数量，减少变化通知次数。

建议一个VSAN内的所有交换机同时开启RSCN聚合功能，并配置相同的RSCN聚合等待时间，以避免可能产生的设备互通问题。

【举例】

\# 在VSAN 1内开启RSCN聚合功能。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 rscn aggregation enable

【相关命令】

·**rscn aggregation timer**

**FC和FCoE \-- Fabric网络命令 \-- rscn aggregation timer**

------------------------------------------------------------------------

**[rscn aggregation timer**]命令用来配置RSCN聚合等待时间。

**[undo rscn aggregation timer**]命令用来恢复缺省情况。

【命令】

**[rscn aggregation timer** *time*]

**[undo rscn aggregation timer**]

【缺省情况】

RSCN聚合等待时间为2000毫秒。

【视图】

VSAN视图

【缺省级别】

network-admin

mdc-admin

【参数】

*[time*]：RSCN聚合等待时间，取值范围为100～2000，单位为毫秒。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

只有开启RSCN聚合功能后，RSCN聚合等待时间才会生效。

建议一个VSAN内的所有交换机同时开启RSCN聚合功能，并配置相同的RSCN聚合等待时间，以避免可能产生的设备互通问题。

【举例】

\# 配置RSCN聚合等待时间为1500毫秒。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 rscn aggregation timer 1500

【相关命令】

·**rscn aggregation enable**

**FC和FCoE \-- Fabric网络命令 \-- snmp-agent trap enable fc-fabric**

------------------------------------------------------------------------

**[snmp-agent trap enable fc-fabric**]命令用来开启Fabric的告警功能。

**[undo snmp-agent trap enable fc-fabric**]命令用来关闭Fabric的告警功能。

【命令】

**[snmp-agent trap enable fc-fabric**[ [ **domain-id-change** \| **fabric-change** ] \*]]

**[undo snmp-agent trap enable fc-fabric**[ [ **domain-id-change** \| **fabric-change** ] \*]]

【缺省情况】

Fabric的告警功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain-id-change**]：表示域ID变化的告警功能。开启本告警功能后，当本地交换机在所在VSAN内的域ID发生变化时会生成告警信息，其中携带发生变化的VSAN ID、本地交换机的WWN以及变化后的域ID。

**[fabric-change**]：表示Fabric变化的告警功能。开启了本告警功能后，当Fabric进行重配置，即交换机收到或发送BF或RCF报文时（包括配置了拒绝收到的RCF请求报文的接口收到了RCF请求报文）会生成告警信息，其中携带进行Fabric重配置的VSAN ID。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

如果未指定任何参数，则表示开启或关闭Fabric的全部告警功能。

开启了Fabric的告警功能之后，Fabric会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启Fabric的全部告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable fc-fabric

**FC和FCoE \-- Fabric网络命令 \-- snmp-agent trap enable fc-name-service**

------------------------------------------------------------------------

**[snmp-agent trap enable fc-name-service**]命令用来开启名称服务的告警功能。

**[undo snmp-agent trap enable fc-name-service**]命令用来关闭名称服务的告警功能。

【命令】

**[snmp-agent trap enable fc-name-service**[ [ **login** \| **logout** ] \*]]

**[undo snmp-agent trap enable fc-name-service**[ [ **login** \| **logout** ] \*]]

【缺省情况】

名称服务的告警功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[login**]：表示节点向交换机注册名称服务信息的告警功能。开启本告警功能后，当本地交换机发生节点注册名称服务信息事件时会生成告警信息，其中携带VSAN ID、本地交换机的WWN以及节点上N_Port的WWN。

**[logout**]：表示节点向交换机注销名称服务信息的告警功能。开启本告警功能后，当本地交换机发生节点注销名称服务信息事件时会生成告警信息，其中携带VSAN ID、本地交换机的WWN以及节点上N_Port的WWN。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

如果未指定任何参数，则表示开启或关闭名称服务的全部告警功能。

开启了名称服务的告警功能之后，名称服务会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启名称服务的全部告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable fc-name-service

**FC和FCoE \-- Fabric网络命令 \-- timer distributed-services**

------------------------------------------------------------------------

**[timer** **distributed-services**]命令用来在VSAN内配置分布式服务超时时间。

**[undo** **timer** **distributed-services**]命令用来恢复缺省情况。

【命令】

**[timer distributed-services** *value*]

**[undo timer distributed-services**]

【缺省情况】

分布式服务超时时间为5000毫秒。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：分布式服务超时时间，取值范围为5000～10000，单位为毫秒。

【使用指导】

本命令与**fc timer** **distributed-services**命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有VSAN都有效，VSAN视图下的配置只对当前VSAN有效，后者的配置优先级较高。

【举例】

\# 在VSAN 1内配置分布式服务超时时间为6000毫秒。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 timer distributed-services 6000

【相关命令】

·**fc timer** **distributed-services**

**FC和FCoE \-- Fabric网络命令 \-- timer error-detect**

------------------------------------------------------------------------

**[timer** **error-detect**]命令用来在VSAN内配置错误检测超时时间。

**[undo** **timer** **error-detect**]命令用来恢复缺省情况。

【命令】

**[timer error-detect** *value*]

**[undo timer error-detect**]

【缺省情况】

错误检测超时时间为2000毫秒。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：错误检测超时时间，取值范围为1000～10000，单位为毫秒。

【使用指导】

本命令与**fc timer** **error-detect**命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有VSAN都有效，VSAN视图下的配置只对当前VSAN有效，后者的配置优先级较高。

【举例】

\# 在VSAN 1内配置错误检测超时时间为6000毫秒。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 timer error-detect 6000

【相关命令】

·**fc timer** **error-detect**

**FC和FCoE \-- Fabric网络命令 \-- timer resource-allocation**

------------------------------------------------------------------------

**[timer** **resource-allocation**]命令用来在VSAN内配置资源分配超时时间。

**[undo** **timer** **resource-allocation**]命令用来恢复缺省情况。

【命令】

**[timer resource-allocation** *value*]

**[undo timer resource-allocation**]

【缺省情况】

资源分配超时时间为10000毫秒。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：资源分配超时时间，取值范围为5000～10000，单位为毫秒。

【使用指导】

本命令与**fc timer** **resource-allocation**命令的功能相同，只是作用范围不同：系统视图下的全局配置对所有VSAN都有效，VSAN视图下的配置只对当前VSAN有效，后者的配置优先级较高。

【举例】

\# 在VSAN 1内配置资源分配超时时间为6000毫秒。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 timer resource-allocation 6000

【相关命令】

·**fc timer** **resource-allocation**

**FC和FCoE \-- Fabric网络命令 \-- wwn fcid**

------------------------------------------------------------------------

**[wwn** **fcid**]命令用来配置FCID持久化表项。

**[undo** **wwn** **fcid**]命令用来删除FCID持久化表项。

【命令】

**[wwn** *wwn-value* **fcid** *fcid-value* [ **dynamic** ]]

**[undo** **wwn** *wwn-value* **fcid**]

【缺省情况】

不存在手工配置的FCID持久化表项。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[wwn-value*]：N_Port/NP_Port的WWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

*[fcid-value*]：FCID的值，格式为xxxxxx，其中x为16进制数字，前两位表示Domain_ID，中间两位表示Area_ID，后两位表示Port_ID。其中，Domain_ID必须是本VSAN内正在运行的Domain_ID。

**[dynamic**]：表示动态的FCID持久化表项。如果未指定本参数，表示静态的FCID持久化表项。尽管节点上线时会自动生成动态的FCID持久化表项，但用户也可根据实际需要自行配置动态的FCID持久化表项。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

需要注意的是：

·只有开启了FCID持久化功能后，手工配置的FCID持久化表项才能生效。

·每个N_Port/NP_Port只能绑定一个FCID，一个FCID也只能与一个N_Port/NP_Port绑定。

·要绑定的N_Port/NP_Port如果已Login并分配了其它FCID，或者要绑定的FCID已被分配给其它N_Port/NP_Port，则不允许将二者绑定。

·当FCID持久化表项总数达到系统上限（40000条）后仍继续添加表项，系统会先删除当前所有离线节点的动态表项，如果所有表项均为静态表项，或对应节点均在线，则系统对此后收到的所有FLOGI请求均回应拒绝报文。

【举例】

\# 在VSAN 1内配置如下静态FCID持久化表项：为N_Port（WWN为33:e8:00:05:30:00:16:df）绑定Area_ID为03、Port_ID为12的FCID，当前VSAN内运行的Domain_ID为01。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 wwn 33:e8:00:05:30:00:16:df fcid 010312

【相关命令】

·**fcid** **persistent** **enable**

**FC和FCoE \-- FC路由与转发配置命令 \-- display fc exchange**

------------------------------------------------------------------------

**[display fc exchange**]命令用来显示FC Exchange表项信息。

【命令】

集中式设备：

**[display fc exchange**[ { **link** \| **protocol** }]]

**[display fc exchange link verbose** [ **exid** *exid* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display fc exchange**[ { **link** \| **protocol** } [ **slot** *slot-number* ]]]

**[display fc exchange link verbose** [ **slot** *slot-number* [ **exid** *exid*  ]]]

分布式设备－IRF模式：

**[display fc exchange**[ { **link** \| **protocol** } [ **chassis** *chassis-number* **slot** *slot-number* ]]]

**[display fc exchange link verbose** [ **chassis** *chassis-number* **slot** *slot-number* [ **exid** *exid*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[link**]：显示连接Exchange表项信息。

**[protocol**]：显示协议Exchange表项信息。

**[verbose**]：显示连接Exchange表项的详细信息。

**[exid**]exid{.commandparameterChar}：显示指定Exchange ID的连接Exchange表项信息。exid{.commandparameterChar}的取值范围为0～65534。如果不指定本参数，则显示所有连接Exchange表项信息。

**[slot**]slot-number{.commandparameterChar}：显示指定单板上的信息。slot-number{.commandparameterChar}表示单板所在的槽位号。如果未指定本参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot**]slot-number{.commandparameterChar}：显示指定成员设备上的信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：显示指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示Master设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]chassis-number{.commandparameterChar} **slot** slot-number{.commandparameterChar}：显示指定成员设备指定单板上的信息。chassis-number{.commandparameterChar}表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]chassis-number{.commandparameterChar} **slot** slot-number{.commandparameterChar}：显示指定单板上的信息。chassis-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。如果未指定本参数，将显示全局主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

Exchange是FC协议的基本概念，所有数据帧和控制帧的传输都要基于Exchange完成。

一个Exchange表示两个通讯实体间的一次数据交换，可以包含多次双向的报文交互。

FC协议中的任意一次数据交互或协议报文交互都要创建一对Exchange结构（发起端Exchange和回应端Exchange），基于这一对Exchange来完成报文的发送和接收，对于提供可靠传输服务的服务级别（Class 1、2、6），基于这对Exchange来完成报文的确认、错误检测、报文重传。

Exchange分为两种：

·协议Exchange：只存在于服务器端，基于协议号和VSAN ID创建，用于监听连接建立。

·连接Exchange：同时存在于数据交互的两端，基于Exchange ID创建，用于报文交互。

【举例】

\# 显示协议Exchange表项信息。（集中式设备）

\<Sysname\> display fc exchange protocol

 Local_ID:EXID     Remote_ID:EXID     State       Protocol

 0x000000:65535    0x000000:65535     LISTEN      5

\# 显示协议Exchange表项信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display fc exchange protocol slot 1

 Local_ID:EXID     Remote_ID:EXID     State       Slot  Protocol

 0x000000:65535    0x000000:65535     LISTEN      1     6

\# 显示协议Exchange表项信息。（分布式设备－IRF模式）

\<Sysname\> display fc exchange protocol chassis 1 slot 2

 Local_ID:EXID     Remote_ID:EXID     State       Chassis Slot  Protocol

 0x000000:65535    0x000000:65535     LISTEN      1       2     13

\# 显示连接Exchange表项信息。（集中式设备）

\<Sysname\> display fc exchange link

 Local_ID:EXID     Remote_ID:EXID     State       Protocol

 0x060501:1024     0x010001:1025      ESTABLISHED 7

\# 显示连接Exchange表项信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display fc exchange link slot 2

 Local_ID:EXID     Remote_ID:EXID     State       Slot  Protocol

 0x060501:1024     0x010001:1025      ESTABLISHED 2     8

\# 显示连接Exchange表项信息。（分布式设备－IRF模式）

\<Sysname\> display fc exchange link chassis 3 slot 5

 Local_ID:EXID     Remote_ID:EXID     State       Chassis Slot  Protocol

 0x060501:1024     0x010001:1025      ESTABLISHED 3       5     11

\# 显示连接Exchange表项详细信息。

\<Sysname\> display fc exchange link verbose slot 1

 slot: 1

 protocol: 8

 connection info: Local = 0x090801:1155 ,  Remote = 0x050001:1089

 PCB flags: 0x2

 FC Class: FC_CLASS_F

 connection state: ESTABLISHED

 VSAN ID: 25

表1-30 display fc exchange命令显示信息描述表

字段

描述

Local_ID:EXID/Local

本端FC地址及Exchange ID（对于协议Exchange来说，此值没有意义）

Remote_ID:EXID/Remote

对端FC地址及Exchange ID（对于协议Exchange来说，此值没有意义）

State/connection state

FC Exchange的连接状态，包括：

·PREPARE：表示协议Exchange绑定成功/连接Exchange等待回应报文

·LISTEN：表示协议Exchange监听连接

·ESTABLISHED：表示连接建立

·ABTS：表示连接超时或出错后发送了ABTS，正在等待ABTS ACK

·BA_ACC：表示收到了ABTS并回应了BA_ACC，正在等待ACC ACK

·ABTS_ACK：表示收到了ABTS ACK，正在等待BA_ACC

·CLOSED：表示连接关闭

Slot/slot

FC Exchange建立所在的单板

Protocol/protocol

FC协议号，标识协议类型

PCB flags

FC Exchange状态控制标志位（一共4位）：

·0x1：该位取值为0标识发送端，取值为1标识回应端

·0x2：该位取值为0标识无主动权，取值为1标识有主动权

·0x4：该位取值为1标识Exchange连接的第一个报文

·0x8：该位取值为1标识Exchange正在等待老化

FC Class

FC连接服务级别，包含如下几种（其中FC_CLASS_3不需要回应ACK）：

FC_CLASS_1、FC_CLASS_2、FC_CLASS_3、FC_CLASS_F、FC_CLASS_6

VSAN ID

虚拟存储局域网索引

**FC和FCoE \-- FC路由与转发配置命令 \-- display fc fib**

------------------------------------------------------------------------

**[display fc fib**]命令用来显示FC FIB表项信息。

【命令】

**[display fc fib** [ *fcid* [ *mask-length*  ] **vsan** *vsan-id*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

fcid{.commandparameterChar}：显示指定目的FC地址的FC FIB表项信息，取值范围为0x000000～0xFFFFFF（十六进制）。

*[mask-length*]：目的FC地址掩码长度，取值范围为0～24。

**[vsan**]vsan-id{.commandparameterChar}：显示指定VSAN内的FC FIB表项信息，vsan-id的取值范围为1～4095。

【使用指导】

FC FIB提供以VSAN ID和目的FC地址为索引的表项查询，为转发报文和本机发送报文提供出接口信息。

需要注意的是：

·如果同时指定*fcid*和*mask-length*，则显示指定目的FC地址和掩码长度的FC FIB表项信息。

·如果仅指定*fcid*，不指定*mask-length*，则按照最长匹配原则显示指定目的FC地址的FC FIB表项信息。

·如果不指定*fcid*和*mask-length*，则显示指定VSAN内所有的FC FIB表项信息。

【举例】

\# 显示VSAN 18内所有的FC FIB表项信息。

\<Sysname\> display fc fib vsan 18

FC FIB information in VSAN 18:

  Destination count: 6

  FIB entry count: 7

  Destination/Mask              Interface

  0x030100/16                   Fc1/0/1

  0x030100/16                   Fc1/0/2

  0x030100/24                   Fc1/0/3

  0xfffc01/24                   InLoop0

  0xfffffa/24                   InLoop0

  0xfffffc/24                   InLoop0

  0xfffffd/24                   InLoop0

\# 按照最长匹配原则显示指定目的FC地址的FC FIB表项信息。

\<Sysname\> display fc fib 030100 vsan 18

FC FIB information in VSAN 18:

  Destination count: 1

  FIB entry count: 1

  Destination/Mask              Interface

  0x030100/24                   Fc1/0/3

\# 显示指定目的FC地址和掩码长度的FC FIB表项信息。

\<Sysname\> display fc fib 030100 16 vsan 18

FC FIB information in VSAN 18:

  Destination count: 1

  FIB entry count: 2

  Destination/Mask              Interface

  0x030100/16                   Fc1/0/1

  0x030100/16                   Fc1/0/2

表1-31 display fc fib命令显示信息描述表

字段

描述

Destination count

显示表项中目的FC地址个数

FIB entry count

显示表项中实际表项个数，包含等价路由

Destination/Mask

目的FC地址/掩码长度

Interface

出接口

**FC和FCoE \-- FC路由与转发配置命令 \-- display fc routing-table**

------------------------------------------------------------------------

**[display fc routing-table**]命令用来显示FC路由表信息。

【命令】

**[display fc routing-table** [ **vsan** *vsan-id*  [ **statistics** \| **verbose** ]]]

**[display fc routing-table**[ **vsan** *vsan-id* *fcid* [ *mask* \| *mask-length* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan*** vsan-id*]：显示指定VSAN内的路由信息。*vsan-id*的取值范围为1～4095。不指定该参数时，显示所有VSAN的路由信息。

*[fcid*]：指定FC静态路由的目的FC地址，取值范围为0x010000～0xEFFFFF（十六进制）。

*[mask*]：FC地址的十六进制掩码，与*fcid*配合使用。取值为0xFF0000、0xFFFF00、0xFFFFFF。不指定该参数时，将显示FC路由表内所有FC地址是*fcid*，且掩码是0xFF0000、0xFFFF00和0xFFFFFF的路由。

*[mask-length*]：FC地址的十进制掩码，与*fcid*配合使用。取值为8、16、24。不指定该参数时，将显示FC路由表内所有FC地址是*fcid*，且掩码是8、16和24的路由。

**[statistics**]：显示FC路由表的统计信息。

**[verbose**]：显示FC路由表的详细信息。

【使用指导】

路由表中保存了各种路由协议发现的路由。通过本命令可以查看路由表的概要信息、详细信息以及统计信息。

需要注意的是：

·如果不指定**statistics**和**verbose**，将显示FC路由表的概要信息。

·在显示FC路由表的概要信息时，将只显示激活的路由；在显示FC路由表的详细信息时，将显示所有激活和非激活的路由。

【举例】

\# 显示VSAN 5内所有路由的概要信息。

\<Sysname\> display fc routing-table vsan 5

Routing Table: VSAN 5

  Destinations : 5          Routes : 8

  Destination/mask   Protocol   Preference   Cost     Interface

  0x040000/8         FSPF       20           100      Vfc10

  0x040000/8         FSPF       20           100      Vfc20

  0x040000/8         FSPF       20           100      Vfc30

  0x040000/8         FSPF       20           100      Vfc40

  0xfffc01/24        DIRECT     0            0        InLoop0

  0xfffffa/24        DIRECT     0            0        InLoop0

  0xfffffc/24        DIRECT     0            0        InLoop0

  0xfffffd/24        DIRECT     0            0        InLoop0

\# 显示VSAN 5内所有路由的的详细信息。

\<Sysname\> display fc routing-table vsan 5 verbose

Routing Table: VSAN 5

  Destinations : 5          Routes : 5

  Destination/mask: 0x120000/8

          Protocol: STATIC

        Preference: 10

              Cost: 0

         Interface: Fc1/0/1

             State: Active

               Age: 0h21m36s

  Destination/mask: 0xfffc01/24

          Protocol: DIRECT

        Preference: 0

              Cost: 0

         Interface: InLoop0

             State: Active

               Age: 0h21m36s

  Destination/mask: 0xfffffa/24

          Protocol: DIRECT

        Preference: 0

              Cost: 0

         Interface: InLoop0

             State: Active

               Age: 0h21m36s

  Destination/mask: 0xfffffc/24

          Protocol: DIRECT

        Preference: 0

              Cost: 0

         Interface: InLoop0

             State: Active

               Age: 0h21m36s

  Destination/mask: 0xfffffd/24

          Protocol: DIRECT

        Preference: 0

              Cost: 0

         Interface: InLoop0

             State: Active

               Age: 0h21m36s

表1-32 display fc routing-table命令显示信息描述表

字段

描述

VSAN

VSAN编号

Destinations

不同目的地址的个数

Routes

路由条数

Destination/mask

FC地址/掩码

Protocol

协议类型，包括：

·DIRECT：表示直连路由

·STATIC：表示静态路由

·FSPF：表示FSPF路由

Preference

路由的优先级

Cost

路由的度量值

Interface

出接口

State

路由状态，包括：

·Active：表示激活

·Inactive：表示非激活

Age

路由在路由表中存在的时间，格式为：XXhXXmXXs（XX小时XX分钟XX秒）

\# 显示VSAN 5内所有路由的统计信息。

\<Sysname\> display fc routing-table vsan 5 statistics

Routing Table: VSAN 5

  Protocol  route       active      added       deleted

  DIRECT    4           4           4           0

  STATIC    1           1           1           0

  FSPF      0           0           0           0

  Total     5           5           5           0

表1-33 display fc routing-table statistics命令显示信息描述表

字段

描述

VSAN

VSAN编号

Protocol

协议类型，包括：

·DIRECT：表示直连路由

·STATIC：表示静态路由

·FSPF：表示FSPF路由

route

协议类型Protocol下的路由数

active

协议类型Protocol下的激活路由数

added

协议类型Protocol下添加的路由数

deleted

协议类型Protocol下删除的路由数

Total

总计

【相关命令】

·**fc route-static**

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf graceful-restart**

------------------------------------------------------------------------

**[display fspf graceful-restart**]命令用来显示FSPF GR状态信息。

【命令】

**[display fspf graceful-restart** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的FSPF GR状态信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的FSPF GR状态信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看FSPF GR状态信息，包括是否开启GR Restarter、GR Helper以及正在重启的GR Restarter数量、正在协助本机重启的GR Helper数量等信息。

【举例】

\# 显示FSPF GR状态信息。

\<Sysname\> display fspf graceful-restart

Graceful-restart capability      : Disable

Helper capability                : Enable

Graceful-restart period          : 120 seconds

FSPF graceful restart information of VSAN 1:

  Number of neighbors under helper : 0

  Number of restarting neighbors   : 0

FSPF graceful restart information of VSAN 2:

  Number of neighbors under helper : 0

  Number of restarting neighbors   : 0

表1-34 display fspf graceful-restart命令显示信息描述表

字段

描述

Graceful-restart capability

是否开启GR能力，包括：

·Enable：表示开启

·Disable：表示未开启

Helper capability

是否开启GR Helper能力，包括：

·Enable：表示开启

·Disable：表示未开启

Graceful-restart period

GR最大间隔时间

Number of neighbors under helper

处于helper状态邻居的数量

Number of restarting neighbors

处于restarter状态邻居的数量

【相关命令】

·**fspf graceful-restart**

·**fspf graceful-restart helper**

·**fspf graceful-restart interval**

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf lsdb**

------------------------------------------------------------------------

**[display fspf lsdb**]命令用来显示FSPF链路状态数据库信息。

【命令】

**[display fspf lsdb** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的FSPF链路状态数据库信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的FSPF链路状态数据库信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看FSPF链路状态数据库信息，包括VSAN下LSR的总数和各LSR的具体信息。

【举例】

\# 显示FSPF链路状态数据库信息。

\<Sysname\> display fspf lsdb

FSPF LSDB information of VSAN 1(01):

  Total LSR count: 2

    FSPF Link State Database for Domain 01

      LSR Type                  : 1

      LSR Age                   : 0

      LSR Incarnation number    : 0x80000008

      LSR Checksum              : 0x7deb

      Number of links           : 1

      NbrDomainID    IfIndex    NbrIfIndex    LinkType    Cost

      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      2              0x68       0x68          1           265

    FSPF Link State Database for Domain 02

      LSR Type                  : 1

      LSR Age                   : 6

      LSR Incarnation number    : 0x80000008

      LSR Checksum              : 0x7dea

      Number of links           : 1

      NbrDomainID    IfIndex    NbrIfIndex    LinkType    Cost

      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      1              0x68       0x68          1           265

表1-35 display fspf lsdb命令显示信息描述表

字段

描述

FSPF LSDB information of VSAN

指定VSAN的链路状态数据库信息，括号中为本机域ID的十进制显示

Total LSR count

LSR数量

FSPF Link State Database for Domain

指定域ID交换机的链路状态数据库信息

LSR Type

LSR类型，只支持Switch Link Record（0x01）类型

LSR Age

LSR生存时间

LSR Incarnation number

LSR实例号

LSR Checksum

LSR校验和

Number of links

链路数量

NbrDomainID

邻居域ID

IfIndex

本交换机出接口索引

NbrIfIndex

邻居接口索引

Link Type

链路类型，包括：

·0x01：表示点到点类型

·0xF0-FF：表示厂商自定义类型

Cost

链路开销

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf neighbor**

------------------------------------------------------------------------

**[display fspf neighbor**]命令用来显示FSPF邻居信息。

【命令】

**[display fspf neighbor** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的FSPF邻居信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的FSPF邻居信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看FSPF邻居信息，包括邻居的域ID、邻居接口索引及本机出接口索引、邻居剩余Dead时间、邻居状态。

【举例】

\# 显示FSPF邻居信息。

\<Sysname\> display fspf neighbor

FSPF neighbor information of VSAN 1(01):

  Interface   NbrDomain   IfIndex   NbrIfIndex   Dead Time   State

  Fc1/0/1     2           0x68      0x68         00:01:06    Full

表1-36 display fspf neighbor命令显示信息描述表

字段

描述

FSPF neighbor information of VSAN

指定VSAN的FSPF邻居信息，括号中为本机域ID的十进制显示

Interface

本机接口名称

NbrDomain

邻居域ID，十进制显示

IfIndex

本机出接口索引

NbrIfIndex

邻居接口索引

Dead Time

邻居所剩Dead间隔（如果这个间隔后还未收到邻居的Hello报文，邻居状态变迁至Init）

State

邻居状态，包括：

·Down：表示邻居还未开始协商

·Init：表示开始协商

·DB_Exchange：表示已经发现邻居

·DB_Wait：表示本端已发送完LSR

·DB_Ack_Wait：表示对端已发送完LSR

·Full：表示同步完成

**FC和FCoE \-- FC路由与转发配置命令 \-- display fspf statistics**

------------------------------------------------------------------------

**[display fspf statistics**]命令用来显示FSPF统计信息。

【命令】

**[display fspf statistics** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的FSPF统计信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的FSPF统计信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看FSPF所有统计信息，包括全局统计信息和接口统计信息。全局统计信息包括当前路由计算次数、错误报文计数、及报文收发总数；接口统计信息包括各接口下报文收发数目。

【举例】

\# 显示FSPF统计信息。

\<Sysname\> display fspf statistics

FSPF statistics of VSAN 1(01):

  SPF computing count: 6

  Statistics counters:

    Bad packet       : 0      Neighbor unknown   : 0

    Timer mismatch   : 0      Neighbor state low : 0

    Bad LSR          : 0

  Packet statistics:

    Type          Input        Output

    HELLO         50           50

    LSU           5            5

    LSA           4            4

  Interface Fc1/0/1 statistics:

    Type          Input        Output

    HELLO         50           50

    LSU           5            5

    LSA           4            4

表1-37 display fspf statistics命令显示信息描述表

字段

描述

FSPF statistics of VSAN

指定VSAN的FSPF统计信息，括号中为本机域ID的十进制显示

SPF computing count

路由计算次数

Statistics counters

统计计数

Packet statistics

报文统计

Interface statistics

端口下报文统计

Bad packet

错误报文

Timer mismatch

和邻居Hello或Dead间隔值不匹配的报文

Bad LSR

错误LSR

Neighbor unknown

未知邻居发来的报文

Neighbor state low

Init状态收到LSU、LSA报文的统计

Type

报文类型，包括：

·Hello：Hello报文

·LSU：LSU报文

·LSA：LSA报文

Input

接收的报文数目

Output

发送的报文数目

【相关命令】

·**reset fspf counters**

**FC和FCoE \-- FC路由与转发配置命令 \-- fc route-static**

------------------------------------------------------------------------

**[fc route-static**]命令用来配置FC静态路由。

**[undo fc route-static**]命令用来删除FC静态路由。

【命令】

**[fc route-static*** fcid *[{ *mask* \| *mask-length* } *interface-type interface-number* [ **cost** *cost-value* ]]]

**[undo fc route-static*** fcid *[{ *mask* \| *mask-length* } *interface-type interface-number*]]

【缺省情况】

不存在FC静态路由。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fcid*]：指定FC静态路由的目的FC地址，取值范围为0x010000～0xEFFFFF（十六进制）。

*[mask*]：FC地址的十六进制掩码，与*fcid*配合使用。取值为0xFF0000、0xFFFF00、0xFFFFFF。

*[mask-length*]：FC地址的十进制掩码，与*fcid*配合使用。取值为8、16、24。

*[interface-type interface-number*]：指定FC静态路由的出接口，出接口必须为FC交换机上存在的FC接口或者VFC接口。

**[cost*** cost-value*]：指定路由的度量值，取值范围为0～65535，缺省值为0。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

静态路由是由管理员手工配置的。配置静态路由后，去往指定目的地的FC报文将按照管理员指定的路径进行转发。

在组网结构比较简单的网络中，只需配置静态路由就可以实现网络互通。但是静态路由不能自动适应网络拓扑结构的变化，当网络发生故障或者拓扑发生变化后，需要管理员手工修改静态路由的配置。

静态路由支持等价路由，如果先后配置多条目的地址相同、出接口不同的静态路由且度量值相同，则生成等价路由。

【举例】

\# 添加一条目的FC地址为0x010000、掩码为8、出接口为FC1/0/1、路由度量值为20的FC静态路由。

\<Sysname\> system-view

Sysname vsan 5

Sysname-vsan5 fc route-static 010000 8 fc 1/0/1 cost 20

\# 添加一条目的FC地址为0x010000、掩码为8、出接口为VFC4、路由度量值为20的FC静态路由。

\<Sysname\> system-view

Sysname vsan 5

Sysname-vsan5 fc route-static 010000 8 vfc 4 cost 20

【相关命令】

·**display fc routing-table**

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf cost**

------------------------------------------------------------------------

**[fspf cost**]命令用来配置指定VSAN内接口的FSPF开销。

**[undo fspf cost**]命令用来恢复缺省情况。

【命令】

**[fspf cost** *value* **vsan** *vsan-id*]

**[undo fspf cost vsan** *vsan-id*]

【缺省情况】

FC接口的缺省FSPF开销根据接口波特率计算得到，计算公式为（1.0\*1.062e12/波特率）。

VFC接口、FC聚合接口的缺省FSPF开销为100。

【视图】

FC接口视图/VFC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接口的FSPF开销，取值范围为1～65535。

**[vsan** *vsan-id*]：所属VSAN，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

网络中，每一条链路会有不同的开销，在路由优选算法中将使用开销值来确定最有效的路由，接口的FSPF开销越小说明链路的开销越小。

【举例】

\# 配置接口FC1/0/1在VSAN 4内的FSPF开销为1000。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1fspf cost 1000 vsan 4

\# 配置接口VFC1在VSAN 4内的FSPF开销为1000。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fspf cost 1000 vsan 4

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf dead-interval**

------------------------------------------------------------------------

**[fspf dead-interval**]命令用来配置指定VSAN内接口的Dead间隔值。

**[undo fspf dead-interval**]命令用来恢复缺省情况。

【命令】

**[fspf dead-interval** *value* **vsan** *vsan-id*]

**[undo fspf dead**]**-interval** **vsan** *vsan-id*

【缺省情况】

接口的Dead间隔值为80秒。

【视图】

FC接口视图/VFC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接口的Dead间隔值，取值范围为2～65535，单位为秒。

**[vsan** *vsan-id*]：所属VSAN，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

两台交换机之间建立起邻居关系后，需要以Hello间隔值为周期向对方发送Hello报文来维护邻居关系。若在Dead间隔内仍未收到对方的Hello报文，则认为邻居不存在，需要删除该邻居。

需要注意的是，配置的Dead间隔值必须大于Hello间隔值，且邻居双方配置的Dead间隔值必须一致。

【举例】

\# 配置接口FC1/0/1在VSAN 4内的Dead间隔值为100秒。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fspf dead-interval 100 vsan 4

\# 配置接口VFC1在VSAN 4内的Dead间隔值为100秒。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fspf dead-interval 100 vsan 4

【相关命令】

·**fspf hello-interval**

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf enable**

------------------------------------------------------------------------

**[fspf enable**]命令用来开启指定VSAN的FSPF功能。

**[undo fspf enable**]命令用来关闭指定VSAN的FSPF功能。

【命令】

**[fspf enable**]

**[undo fspf enable**]

【缺省情况】

VSAN创建后，FSPF功能处于开启状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

开启了指定VSAN的FSPF功能后，该VSAN才可以运行FSPF相关的功能。

【举例】

\# 开启VSAN 4的FSPF功能。

\<Sysname\> system-view

Sysname vsan 4

Sysname-vsan4 fspf enable

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf graceful-restart**

------------------------------------------------------------------------

**[fspf graceful-restart**]命令用来开启FSPF的GR能力。

**[undo fspf graceful-restart**]命令用来关闭FSPF的GR能力。

【命令】

**[fspf graceful-restart**]

**[undo fspf graceful-restart**]

【缺省情况】

FSPF的GR能力处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

GR（Graceful Restart，平滑重启）是一种通过备份FSPF配置信息，在协议重启或主备倒换时FSPF进行平滑重启，从邻居那里获得邻居关系，并对LSDB进行同步，从而保证转发业务不中断的机制。

GR有两个角色：

·GR Restarter：发生协议重启或主备倒换事件且具有GR能力的设备。

·GR Helper：和GR Restarter具有邻居关系，协助完成GR流程的设备。

【举例】

\# 开启FSPF的GR能力。

\<Sysname\> system-view

Sysname fspf graceful-restart

【相关命令】

·**display fspf graceful-restart**

·**fspf graceful-restart helper**

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf graceful-restart helper**

------------------------------------------------------------------------

**[fspf graceful-restart helper**]命令用来开启FSPF的GR Helper能力。

**[undo fspf graceful-restart helper**]命令用来关闭FSPF的GR Helper能力。

【命令】

**[fspf graceful-restart helper**]

**[undo fspf graceful-restart helper**]

【缺省情况】

FSPF的GR Helper能力处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

开启了FSPF的GR Helper能力后，该交换机才可以协助GR Restarter完成GR功能。

【举例】

\# 开启FSPF的GR Helper能力。

\<Sysname\> system-view

Sysname fspf graceful-restart helper

【相关命令】

·**display fspf graceful-restart**

·**fspf graceful-restart**

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf graceful-restart interval**

------------------------------------------------------------------------

**[fspf graceful-restart interval**]命令用来配置FSPF的GR最大间隔时间。

**[undo fspf graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[fspf graceful-restart interval ***interval-value*]

**[undo fspf graceful-restart interval**]

【缺省情况】

FSPF的GR最大间隔时间为120秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：指定FSPF的GR最大间隔时间，取值范围为40～1800，单位为秒。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

对于GR Restarter来说，如果在GR最大间隔时间内没有完成GR过程，则立即退出GR过程。

【举例】

\# 配置FSPF的GR最大间隔时间为100秒。

\<Sysname\> system-view

Sysname fspf graceful-restart interval 100

【相关命令】

·**display fspf graceful-restart**

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf hello-interval**

------------------------------------------------------------------------

**[fspf hello-interval**]命令用来配置指定VSAN内接口的Hello间隔值。

**[undo fspf hello-interval**]命令用来恢复缺省情况。

【命令】

**[fspf hello-interval** *value* **vsan** *vsan-id*]

**[undo fspf hello-interval**]**vsan** *vsan-id*

【缺省情况】

接口的Hello间隔值为20秒。

【视图】

FC接口视图/VFC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接口的Hello间隔值，取值范围为1～65534，单位为秒。

**[vsan** *vsan-id*]：所属VSAN，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

交换机通过周期性向外发送Hello报文，来发现和维护邻居关系。Hello间隔值决定了接口在指定VSAN内发送Hello报文的时间间隔。

需要注意的是，配置的Hello间隔值必须小于Dead间隔值，且邻居双方配置的Hello间隔值必须一致。

【举例】

\# 配置接口FC1/0/1在VSAN 4内的Hello间隔值为10秒。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fspf hello-interval 10 vsan 4

\# 配置接口VFC1在VSAN 4内的Hello间隔值为10秒。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fspf hello-interval 10 vsan 4

【相关命令】

·**fspf dead-interval**

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf min-ls-arrival**

------------------------------------------------------------------------

**[fspf min-ls-arrival**]命令用来配置指定VSAN内LSR最小接收间隔。

**[undo fspf min-ls-arrival**]命令用来恢复缺省情况。

【命令】

**[fspf min-ls-arrival** *value*]

**[undo fspf min-ls-arrival**]

【缺省情况】

LSR最小接收间隔为1秒。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：LSR最小接收间隔，取值范围为0～60，单位为秒。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

LSR最小接收间隔决定了指定VSAN内接收LSR的间隔。为了避免过于频繁的从邻居接收到同一个LSR的新实例、更新本地LSDB而频繁触发路由计算。在LSR最小接收间隔时间内，如果又一次接收到了这个LSR的新实例，则直接丢弃，不做处理。

【举例】

\# 配置VSAN 2内LSR最小接收间隔为10秒。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fspf min-ls-arrival 10

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf min-ls-interval**

------------------------------------------------------------------------

**[fspf min-ls-interval**]命令用来配置指定VSAN内LSR最小刷新间隔。

**[undo fspf min-ls-interval**]命令用来恢复缺省情况。

【命令】

**[fspf min-ls-interval** *value*]

**[undo fspf min-ls-interval**]

【缺省情况】

LSR最小刷新间隔为5秒。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：最小LSR刷新间隔值，取值范围为1～60，单位为秒。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

LSR最小刷新间隔决定了指定VSAN内LSR刷新间隔。为了避免本机LSR被频繁的刷新，从而降低路由计算的频率和减少Fabric中LSR的泛洪，在LSR最小刷新间隔内，交换机不能再次刷新本机LSR。

【举例】

\# 配置VSAN 2内最小LSR刷新间隔值为10秒。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fspf min-ls-interval 10

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf retransmit-interval**

------------------------------------------------------------------------

**[fspf retransmit-interval**]命令用来配置指定VSAN内接口的LSR重传间隔。

**[undo fspf retransmit-interval**]命令用来恢复缺省情况。

【命令】

**[fspf retransmit-interval** *value* **vsan** *vsan-id*]

**[undo fspf retransmit**]**-interval vsan** *vsan-id*

【缺省情况】

接口的LSR重传间隔为5秒。

【视图】

FC接口视图/VFC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接口的LSR重传间隔，取值范围为1～65535，单位为秒。

**[vsan** *vsan-id*]：所属VSAN，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

LSDB的同步需要交互LSR。在发送LSR后，等待邻居回应报文确认，如果过了LSR重传间隔还没有接收到邻居的确认，那么需要再次发送该LSR。

【举例】

\# 配置接口FC1/0/1在VSAN 4内的LSR重传间隔为10秒。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fspf retransmit-interval 10 vsan 4

\# 配置接口VFC1在VSAN 4内的LSR重传间隔为10秒。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fspf retransmit-interval 10 vsan 4

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf silent**

------------------------------------------------------------------------

**[fspf silent**]命令用来关闭指定VSAN内接口的FSPF功能。

**[undo fspf silent**]命令用来开启指定VSAN内接口的FSPF功能。

【命令】

**[fspf silent vsan** *vsan-id*]

**[undo fspf silent vsan** *vsan-id*]

【缺省情况】

所有接口的FSPF功能均处于开启状态。

【视图】

FC接口视图/VFC接口视图/FC聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan** *vsan-id*]：所属VSAN，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

开启接口的FSPF功能后，接口才可以参与FSPF路由运算，如果某接口不参与FSPF路由运算，则需关闭该接口的FSPF功能。

【举例】

\# 关闭VSAN 4内接口FC1/0/1的FSPF功能。

\<Sysname\> system-view

Sysname interface fc 1/0/1

Sysname-Fc1/0/1 fspf silent vsan 4

\# 关闭VSAN 4内接口VFC1的FSPF功能。

\<Sysname\> system-view

Sysname interface vfc 1

Sysname-Vfc1 fspf silent vsan 4

**FC和FCoE \-- FC路由与转发配置命令 \-- fspf spf-hold-time**

------------------------------------------------------------------------

**[fspf spf-hold-time**]命令用来配置指定VSAN内最短SPF计算间隔。

**[undo fspf spf-hold-time**]命令用来恢复缺省情况。

【命令】

**[fspf spf-hold-time** *value*]

**[undo fspf spf-hold-time**]

【缺省情况】

最短SPF计算间隔为0秒。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：最短SPF计算间隔，取值范围为0～60，单位为秒。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

当LSDB发生改变时，需要进行SPF计算。SPF计算需要耗费一定的CPU，如果网络频繁变化，且每次变化都立即进行SPF计算，将会占用大量的CPU。为了避免交换机过于频繁的进行路由计算而浪费CPU，用户可以配置最短的SPF计算间隔。

最短SPF计算间隔决定了指定VSAN内两次连续的SPF计算之间的最小时间间隔。最短SPF计算间隔配置的小，意味着FSPF对于Fabric的变化可以快速反应，重新计算VSAN内的路由。一个更小的SPF计算间隔会耗费更多的CPU。

【举例】

\# 配置VSAN 2内最短SPF计算间隔为10秒。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fspf spf-hold-time 10

**FC和FCoE \-- FC路由与转发配置命令 \-- reset fspf counters**

------------------------------------------------------------------------

**[reset fspf counters**]命令用来清除FSPF统计信息。

【命令】

**[reset fspf counters** [ **vsan** *vsan-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan**] *vsan-id*：清除指定VSAN内的FSPF统计信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将清除所有VSAN内的FSPF统计信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 清除VSAN 2内的FSPF统计信息。

\<Sysname\> reset fspf counters vsan 2

【相关命令】

·**display fspf statistics**

**FC和FCoE \-- FC Zone配置命令 \-- delete zone database all**

------------------------------------------------------------------------

**[delete zone database all**]命令用来清除Zone数据库信息。

【命令】

**[delete zone database all**]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

通过本命令可以删除指定VSAN内的Zone数据库信息，包括所有Zone set、Zone以及Zone别名，但是Active Zone set不会被删除。

【举例】

\# 清除VSAN 1内的Zone数据库信息。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 delete zone database all

**FC和FCoE \-- FC Zone配置命令 \-- display zone**

------------------------------------------------------------------------

**[display** **zone**]命令用来显示Zone的相关信息。

【命令】

**[display** **zone** [ [ **name** *zone-name*  **vsan** *vsan-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***zone-name*]：显示指定名称的Zone的相关信息。*zone-name*表示Zone的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

**[vsan*** vsan-id*]：显示指定VSAN内的Zone相关信息。*vsan-id*表示Zone所属的VSAN编号，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

根据用户的配置可以显示不同Zone的信息：

·如果同时指定**name**和**vsan**参数，则显示指定VSAN内指定名称的单个Zone的信息；

·如果仅指定**vsan**参数，则显示指定VSAN内所有Zone的信息；

·如果不指定任何参数，则显示所有VSAN内所有Zone的信息。

【举例】

\# 显示所有VSAN内所有Zone的相关信息。

\<Sysname\> display zone

VSAN 1:

  zone name z1

    fcid 0x111111 initiator

    fcid 0x222222 target

    pwwn 11:11:11:11:22:22:22:22

    fwwn 02:0e:30:30:33:33:32:35

  zone name z2

    fcid 0x111111

    zone-alias name za1

    fcid 0x333333 initiator

VSAN 2:

VSAN 3:

表1-38 display zone命令显示信息描述表

字段

描述

VSAN

VSAN编号

zone name

Zone的名称

fcid

Zone成员的FC地址信息

pwwn

Zone成员的PWWN信息

fwwn

Zone成员的FWWN信息

initiator、target

Zone成员的角色，包括：

·initiator：表示成员角色为发起端

·target：表示成员角色为目的端

如果没有标出initiator或target，则表示同时兼具这两种角色

zone-alias name

Zone别名的名称

【相关命令】

·**member (zone view)**

·**zone clone**

·**zone name**

·**zone rename**

**FC和FCoE \-- FC Zone配置命令 \-- display zone member**

------------------------------------------------------------------------

**[display** **zone member**]命令用来显示指定Zone成员所属的父亲信息。

【命令】

**[display**[ **zone member** { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* \| **zone-alias** *zone-alias-name* } [ **vsan** *vsan-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[fcid ***fcid*]：显示指定的FC地址成员所属的父亲信息。*fcid*表示成员的FC地址，格式为xxxxxx，其中x为16进制数字。

**[fwwn ***fwwn*]：显示指定的FWWN成员所属的父亲信息。*fwwn*表示成员的FWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[pwwn ***pwwn*]：显示指定的PWWN成员所属的父亲信息。*pwwn*表示成员的PWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[zone-alias ***zone-alias-name*]：显示指定的Zone别名成员所属的父亲信息。*zone-alias-name*：表示成员的Zone别名，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

**[vsan ***vsan-id*]：显示指定VSAN内的Zone成员所属的父亲信息。*vsan-id*表示VSAN编号，取值范围为1～3839。不指定本参数，将显示所有VSAN内的Zone成员所属的父亲信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

根据用户的配置，本命令可以显示FC地址类型、PWWN类型、FWWN类型、Zone别名类型的成员所属的父亲信息。父亲信息包括：成员所属的Zone和Zone别名，Zone别名所属的Zone，以及Zone和Zone别名所属的VSAN。当Zone别名没有被加入任何Zone时，其父亲信息将只显示Zone别名所属的VSAN。

【举例】

\# 显示VSAN 1中FC地址为010000的Zone成员所属的父亲信息。

\<Sysname\> display zone member fcid 010000 vsan 1

fcid 0x010000

  VSAN 1:

    zone z1

    zone z2

    zone z3

    zone-alias a1

      zone z2

      zone z3

\# 显示所有VSAN中PWWN为11:22:33:44:55:66:77:88的Zone成员所属的父亲信息。

\<Sysname\> display zone member pwwn 11:22:33:44:55:66:77:88

pwwn 11:22:33:44:55:66:77:88

  VSAN 1:

    zone z1

    zone z2

    zone z3

    zone-alias a1

      zone z2

      zone z3

  VSAN 3:

    zone z1

\# 显示所有VSAN中FWWN为12:22:33:44:55:66:77:88的Zone成员所属的父亲信息。

\<Sysname\> display zone member fwwn 12:22:33:44:55:66:77:88

fwwn 12:22:33:44:55:66:77:88

  VSAN 1:

    zone z1

    zone z2

    zone z3

    zone-alias a1

      zone z2

      zone z3

  VSAN 3:

    zone z1

\# 显示VSAN 1中Zone别名为za1的Zone成员所属的父亲信息。

\<Sysname\> display zone member zone-alias za1 vsan 1

zone-alias za1

  VSAN 1：

    zone z1

    zone z2

表1-39 display zone member命令显示信息描述表

字段

描述

VSAN

VSAN编号

fcid

指定显示的Zone成员的FC地址信息

pwwn

指定显示的Zone成员的PWWN信息

fwwn

指定显示的Zone成员的FWWN信息

zone-alias

Zone别名的名称

zone

Zone的名称

【相关命令】

·**member (zone view)**

·**member (zone-alias view)**

**FC和FCoE \-- FC Zone配置命令 \-- display zone statistics**

------------------------------------------------------------------------

**[display zone statistics**]命令用来显示Zone报文统计信息。

【命令】

**[display zone statistics** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan ***vsan-id*]：显示指定VSAN内的Zone报文统计信息。*vsan-id*表示VSAN编号，取值范围为1～3839。不指定本参数，将显示所有VSAN内的Zone报文统计信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示VSAN 2内的Zone报文统计信息。

\<Sysname\> display zone statistics vsan 2

VSAN 2:

  Message type      Sent          Received

  Merge Request     19            23

  Merge Accept      17            18

  Merge Reject      6             1

  Change Request    144           18

  Change Accept     0             0

  Change Reject     0             0

表1-40 display zone statistics命令显示信息描述表

字段

描述

Message type

报文类型

Sent

发送报文的统计信息

Received

接收报文的统计信息

Merge Request

合并过程中的请求报文

Merge Accept

合并过程中的应答报文

Merge Reject

合并过程中的拒绝报文

Change Request

扩散过程中的请求报文

Change Accept

扩散过程中的应答报文

Change Reject

扩散过程中的拒绝报文

【相关命令】

·**reset zone statistics**

**FC和FCoE \-- FC Zone配置命令 \-- display zone status**

------------------------------------------------------------------------

**[display** **zone status**]命令用来显示FC Zone的配置信息以及运行状态。

【命令】

**[display** **zone status** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan ***vsan-id*]：显示指定VSAN内的FC Zone配置信息以及运行状态。*vsan-id*表示VSAN编号，取值范围为1～3839。不指定本参数，将显示所有VSAN内的FC Zone配置信息以及运行状态。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

通过本命令可以查看当前FC Zone的配置信息以及运行状态，包括：Zone的模式、默认Zone策略、扩散和合并类型、Zone数据库信息（创建的Zone set、Zone、Zone别名的个数）、Zone的状态（如，正在进行扩散、合并等）。

需要注意的是，增强Zone模式的合并和扩散不受合并和扩散类型影响，所以在增强Zone模式下，不显示合并和扩散类型信息。

【举例】

\# 显示所有VSAN中FC Zone的配置信息以及运行状态。

\<Sysname\> display zone status

VSAN 1:

  Mode: basic

  Default zone: deny

  Distribute: active only

  Hard-zoning: enabled

  Full zoning database:

    Zonesets: 10, Zones: 20, Zone-aliases: 0

  Status: merging

VSAN 2:

  Mode: enhanced

  Default zone: permit

  Hard-zoning: enabled

  Full zoning database:

    Zonesets: 10, Zones: 20, Zone-aliases: 0

  Status: distributing

表1-41 display zone status命令显示信息描述表

字段

描述

VSAN

VSAN编号

Mode

Zone的模式，包括：

·basic：基本Zone

·enhanced：增强Zone

Default zone

默认Zone策略，包括：

·deny：默认Zone内成员禁止互访

·permit：默认Zone内成员允许互访

Distribute

扩散和合并类型，包括：

·active only：非完全扩散和合并

·full：完全扩散和合并

因为增强Zone不受扩散和合并类型影响，所以在增强Zone模式下不显示Distribute信息

Hard-zoning

硬件Zone的生效状态，包括（不同VSAN下状态可能不同）：

·enabled：硬件Zone处于生效状态

·disabled (Administratively)：用户通过命令手工关闭了硬件Zone

·disabled (No enough hardware resource)：由于底层资源不足，硬件Zone处于未生效状态

Full Zoning Database

Zone数据库信息，将显示指定VSAN下Zone set、Zone、Zone别名的个数

Status

Zone的状态，包括：

·merging：正在进行合并

·distributing：正在进行扩散

·free：空闲状态，表示未处于扩散或合并的过程中

在合并或扩散的过程中，不允许在此VSAN中进行Zone相关的配置

【相关命令】

·**zone default-zone permit**

·**zoneset distribute full**

**FC和FCoE \-- FC Zone配置命令 \-- display zone-alias**

------------------------------------------------------------------------

**[display zone-alias**]命令用来显示Zone别名的相关信息。

【命令】

**[display** **zone-alias** [ [ **name** *zone-alias-name*  **vsan** *vsan-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***zone-alias-name*]：显示指定名称的Zone别名的相关信息。*zone-alias-name*表示Zone别名的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

**[vsan*** vsan-id*]：显示指定VSAN内的Zone别名相关信息。*vsan-id*表示Zone别名所属的VSAN编号，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

根据用户的配置可以显示不同Zone别名的信息：

·如果同时指定**name**和**vsan**参数，则显示指定VSAN内指定名称的单个Zone别名的信息；

·如果仅指定**vsan**参数，则显示指定VSAN内所有Zone别名的信息；

·如果不指定任何参数，则显示所有VSAN内所有Zone别名的信息。

【举例】

\# 显示所有VSAN内所有Zone别名的相关信息。

\<Sysname\> display zone-alias

VSAN 1：

  zone-alias name za1

    fcid 0x111111 initiator

    fcid 0x222222 target

    pwwn 11:11:11:11:22:22:22:22

  zone-alias name za2

    fcid 0x111111

    fwwn 12:11:11:11:22:22:22:22

VSAN 2：

  zone-alias name za1

表1-42 display zone-alias命令显示信息描述表

字段

描述

VSAN

VSAN编号

zone-alias name

Zone别名的名称

fcid

Zone别名成员的FC地址信息

pwwn

Zone别名成员的PWWN信息

fwwn

Zone别名成员的FWWN信息

initiator、target

Zone成员的角色，包括：

·initiator：表示成员角色为发起端

·target：表示成员角色为目的端

如果没有标出initiator或target，则表示同时兼具这两种角色

【相关命令】

·**member (zone-alias view)**

·**zone-alias clone**

·**zone-alias name**

·**zone-alias rename**

**FC和FCoE \-- FC Zone配置命令 \-- display zoneset**

------------------------------------------------------------------------

**[display zoneset**]命令用来显示Zone set的相关信息。

【命令】

**[display** **zoneset** [ [ **name** *zoneset-name* **vsan** *vsan-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name ***zoneset-name*]：显示指定名称的Zone set的相关信息。*zoneset-name*表示Zone set的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

**[vsan*** vsan-id*]：显示指定VSAN内的Zone set相关信息。*vsan-id*表示Zone set所属的VSAN编号，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

根据用户的配置可以显示不同Zone set的信息：

·如果同时指定**name**和**vsan**参数，则显示指定VSAN内指定名称的单个Zone set的信息；

·如果仅指定**vsan**参数，则显示指定VSAN内所有Zone set的信息；

·如果不指定任何参数，则显示所有VSAN内所有Zone set的信息。

【举例】

\# 显示所有VSAN内所有Zone set的相关信息。

\<Sysname\> display zoneset

VSAN 1:

  zoneset name zs1

    zone name z1

      fcid 0x111111

      fcid 0x222222

      pwwn 11:11:11:11:22:22:22:22

    zone name z2

      fcid 0x111111

      zone-alias name za1

        fcid 0x111112

  zoneset name zs2

    zone name z1

VSAN 2:

VSAN 3:

  zoneset name zs1

    zone name z1

表1-43 display zoneset命令显示信息描述表

字段

描述

VSAN

VSAN编号

zoneset name

Zone set的名称

zone name

Zone的名称

fcid

Zone或者Zone别名成员的FC地址信息

pwwn

Zone或者Zone别名成员的PWWN信息

zone-alias name

Zone 别名的名称

【相关命令】

·**member (zoneset view)**

·**zoneset clone**

·**zoneset name**

·**zoneset rename**

**FC和FCoE \-- FC Zone配置命令 \-- display zoneset active**

------------------------------------------------------------------------

**[display zoneset active**]命令用来显示Active Zone set的相关信息。

【命令】

**[display** **zoneset active** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan*** vsan-id*]：显示指定VSAN内Active Zone set的相关信息。*vsan-id*表示Active Zone set所属的VSAN编号，取值范围为1～3839。如果不指定本参数，则显示所有VSAN内Active Zone set相关信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

同一VSAN内只会存在一个Active Zone set。

显示信息的格式遵循下列规则：

·根据用户所配置的成员类型，按照FC地址、PWWN和FWWN的顺序依次分类显示，同种类型的成员按照各自配置值所对应ASCII码升序排列。

·对于在本地名称服务数据库中能够查找到的成员，即实际存在的成员，在显示结果的对应条目前面加上"\*"。如果用户配置的是成员的PWWN，那么交换机会在名称服务数据库中查找对应的FC地址并显示出来，并将配置的PWWN用" "标注在FC地址后面。如果用户配置的是成员的FWWN，那么交换机会在名称服务数据库中查找从该FWWN成员登录的所有N_Port的FC地址并显示出来，并将配置的FWWN用" "标注在FC地址后面。

·对于在本地名称服务数据库中不存在的成员，则显示为用户的配置内容。

·不支持在Active Zone set信息中以Zone别名显示成员。配置激活Zone set后，如果该Zone set中的Zone存在Zone别名类型成员，会直接将Zone别名中的非重复N_Port成员添加进入Zone。

·如果配置了允许默认Zone成员互相访问策略，则会显示默认Zone内的有效成员。即在本地名称服务数据库中存在的，并且不属于Active Zone set的成员，都进行显示。显示信息中将显示这些有效成员的FC地址。

【举例】

\# 显示所有VSAN内的Active Zone set的相关信息。

\<Sysname\> display zoneset active

VSAN 1:

zoneset name zs1

zone name z1

\*fcid 0x222222

\*fcid 0x111111 [pwwn 11:11:11:11:11:11:11:11]

zone name z2

        fcid 0x123456

\*fcid 0x111111 [pwwn 11:11:11:11:11:11:11:11]

        pwwn 11:11:11:11:11:11:11:12

\*fcid 0x333333 [pwwn 33:33:33:33:33:33:33:33]

      zone name #default-zone#

        \*fcid 0x20abcd

        \*fcid 0xabcdef

  VSAN 2:

  VSAN 3:

    zoneset name zs1

zone name z1

         fcid 0x123456

\*fcid 0x111111 [pwwn 11:11:11:11:11:11:11:11]

        pwwn 11:11:11:11:11:11:11:12

        \*fcid 0x333333 [pwwn 33:33:33:33:33:33:33:33]

        \*fcid 0x222221 [fwwn 22:22:22:22:22:22:22:22]

\*fcid 0x222222 [fwwn 22:22:22:22:22:22:22:22]

        \*fcid 0x222223 [fwwn 22:22:22:22:22:22:22:22]

        fwwn aa:bb:cc:dd:ee:ff:00:11

\# 显示VSAN 1内的Active Zone set的相关信息。

\<Sysname\> display zoneset active vsan 1

  VSAN 1:

    zoneset name zs1

      zone name z1

\*fcid 0x222222

\*fcid 0x111111 [pwwn 11:11:11:11:11:11:11:11]

zone name z2

        fcid 0x123456

        \*fcid 0x111111 [pwwn 11:11:11:11:11:11:11:11]

        pwwn 11:11:11:11:11:11:11:12

        \*fcid 0x333333 [pwwn 33:33:33:33:33:33:33:33]

zone name #default_zone#

        \*fcid 0x20abcd

        \*fcid 0xabcdef

表1-44 display zoneset active命令显示信息描述表

字段

描述

VSAN

VSAN编号

zoneset name

Zone set的名称

zone name

Zone的名称

\*fcid

本地名称服务数据库中存在的Zone成员的FC地址信息

fcid

本地名称服务数据库中不存在的Zone成员的FC地址信息

pwwn

用户配置的Zone成员的PWWN信息

fwwn

用户配置的Zone成员的FWWN信息

#default_zone#

默认Zone

【相关命令】

·**zoneset activate name**

**FC和FCoE \-- FC Zone配置命令 \-- member (zone view)**

------------------------------------------------------------------------

**[member**]命令用来在Zone内添加成员。

**[undo member**]命令用来在Zone内删除成员。

【命令】

**[member**[ { { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* } [ **initiator** \| **target** ] \| **zone-alias** *zone-alias-name* }]]

**[undo member**[ { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* \| **zone-alias** *zone-alias-name* }]]

【缺省情况】

新建的Zone内不存在任何成员。

【视图】

Zone视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fcid ***fcid*]：所配置成员的FC地址，格式为xxxxxx，其中x为16进制数字。

**[fwwn ***fwwn*]：所配成员的FWWN，*fwwn*是交换机上某F_Port的fwwn，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。配置本参数后，从该F_Port登录的所有N_Port都添加到该Zone内。

**[pwwn ***pwwn*]：所配置成员的PWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[initiator**]：表示成员角色为发起端。

**[target**]：表示成员角色为目的端。不指定**initiator**和**target**参数时，表示同时兼具这两种角色。

**[zone-alias ***zone-alias-name*]：指定Zone别名的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。指定的Zone别名必须已经存在。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

需要注意的是：

·本命令用于向当前Zone添加或删除成员，为成员指定或更改角色。

·当同一个成员以相同的配置方式（FC地址、PWWN、FWWN或Zone别名）多次指定角色时，该成员的角色为最后一次指定的值。例如：两次均以FC地址方式指定成员角色，第一次指定为**initiator**，第二次指定为**target**，则该成员的角色为**target**。

·当同一个成员以不同的配置方式多次指定角色时，该成员的角色为多次指定的并集。例如：第一次以FC地址方式指定成员角色为**initiator**，第二次以PWWN方式指定成员角色为**target**，则该成员将同时兼具这两种角色。

·成员角色在开启Pairwise特性时才生效。

【举例】

\# 创建Zone z1并进入其视图。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone name z1

Sysname-vsan1-zone-z1

\# 添加FC地址为010000的N_Port为z1的成员，并指明成员角色为发起端。

Sysname-vsan1-zone-z1 member fcid 010000 initiator

\# 添加PWWN为01:02:03:04:05:06:07:08的N_Port为z1的成员，并指明成员角色为目的端。

Sysname-vsan1-zone-z1 member pwwn 01:02:03:04:05:06:07:08 target

\# 恢复PWWN为01:02:03:04:05:06:07:08的N_Port的角色为兼具两种角色。

Sysname-vsan1-zone-z1 member pwwn 01:02:03:04:05:06:07:08

\# 添加FWWN为08:07:06:05:04:03:02:01的F_Port为z1的成员，并指明成员同时兼具两种角色。

Sysname-vsan2-zone-z1 member fwwn 08:07:06:05:04:03:02:01

\# 添加Zone别名za1为z1的成员，其中Zone别名za1已经存在。

Sysname-vsan1-zone-z1 member zone-alias za1

【相关命令】

·**display zone**

·**display zone member**

·**pairwise-zoning enable**

·**zone name**

·**zone-alias name**

**FC和FCoE \-- FC Zone配置命令 \-- member (zone alias view)**

------------------------------------------------------------------------

**[member**]命令用来在Zone别名内添加成员。

**[undo member**]命令用来在Zone别名内删除成员。

【命令】

**[member**[ { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* } [ **initiator** \| **target** ]]]

**[undo member**[ { **fcid** *fcid* \| **fwwn** *fwwn* \| **pwwn** *pwwn* }]]

【缺省情况】

新建的Zone别名内不存在任何成员。

【视图】

Zone别名视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fcid ***fcid*]：所配置成员的FC地址，格式为xxxxxx，其中x为16进制数字。

**[fwwn ***fwwn*]：所配成员的FWWN，*pwwn*是交换机上某F_Port的FWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。配置本参数后，从该F_Port登录的所有N_Port都添加到该Zone别名内。

**[pwwn ***pwwn*]：所配置成员的PWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[initiator**]：表示成员角色为发起端。

**[target**]：表示成员角色为目的端。不指定**initiator**和**target**参数时，表示同时兼具这两种角色。

【使用指导】

只有FCF交换机支持本命令。

需要注意的是：

·本命令用于向当前Zone别名添加或删除成员，为成员指定或更改角色。

·当同一个成员以相同的配置方式（FC地址、PWWN、FWWN或Zone别名）多次指定角色时，该成员的角色为最后一次指定的值。例如：两次均以FC地址方式指定成员角色，第一次指定为**initiator**，第二次指定为**target**，则该成员的角色为**target**。

·当同一个成员以不同的配置方式多次指定角色时，该成员的角色为多次指定的并集。例如：第一次以FC地址方式指定成员角色为**initiator**，第二次以PWWN方式指定成员角色为**target**，则该成员将同时兼具这两种角色。

·成员角色在开启Pairwise特性时才生效。

【举例】

\# 创建Zone别名za1并进入其视图。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone-alias name za1

Sysname-vsan1-zone-alias-za1

\# 添加FC地址为010000的N_Port为za1的成员，并指明成员角色为发起端。

Sysname-vsan1-zone-alias-za1 member fcid 010000 initiator

\# 添加PWWN为01:02:03:04:05:06:07:08的N_Port为za1的成员，并指明成员角色为目的端。

Sysname-vsan1-zone-alias-za1 member pwwn 01:02:03:04:05:06:07:08 target

\# 添加FWWN为08:07:06:05:04:03:02:01的F_Port为za1的成员，并指明成员同时兼具两种角色。

Sysname-vsan2-zone-alias-za1 member fwwn 08:07:06:05:04:03:02:01

【相关命令】

·**display zone-alias**

·**zone-alias name**

**FC和FCoE \-- FC Zone配置命令 \-- member (zone set view)**

------------------------------------------------------------------------

**[member**]命令用来在Zone set内添加Zone。

**[undo member**]命令用来在Zone set内删除Zone。

【命令】

**[member** *zone-**name*]

**[undo** **member** *zone-name*]

【缺省情况】

Zone set内不存在任何Zone。

【视图】

Zone set视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[zone-name*]：Zone的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。指定的Zone必须已经存在。

【使用指导】

只有FCF交换机支持本命令。

【举例】

\# 创建Zone z1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone name z1

Sysname-vsan1-zone-z1 quit

\# 创建Zone set zs1并进入其视图。

Sysname zoneset name zs1

Sysname-vsan1-zoneset-zs1

\# 添加z1为zs1的成员。

Sysname-vsan1-zoneset-zs1 member z1

【相关命令】

·**display zoneset**

·**zone name**

·**zoneset name**

**FC和FCoE \-- FC Zone配置命令 \-- pairwise-zoning enable**

------------------------------------------------------------------------

**[pairwise-zoning enable**]命令用来开启当前Zone的Pairwise特性。

**[undo pairwise-zoning enable**]命令用来关闭当前Zone的Pairwise特性。

【命令】

**[pairwise-zoning enable**]

**[undo pairwise-zoning enable**]

【缺省情况】

Zone的Pairwise特性处于关闭状态。

【视图】

Zone视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机支持本命令。

Zone成员的角色有两种：Initiator和Target，分别表示发起端和目的端。一个Zone成员可以同时兼具这两种角色。

在Zone中开启Pairwise特性后，该Zone内节点间的访问会受到成员角色的影响，即同一Zone内具有不同角色的成员可以互相访问，角色相同的成员间不允许互相访问，兼具两种角色的成员可以和任意角色的成员互相访问。

在Zone中关闭Pairwise特性后，该Zone内节点间的访问不会受到成员角色的影响，即同一Zone内的所有成员之间都可以互相访问。

Pairwise特性开启后不会立即生效，需要重新激活Zone set才能生效。

本配置会在激活Zone set或配置扩散命令后，与Zone信息一起在Fabric中扩散。

【举例】

\# 开启z1的Pairwise特性。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 zone name z1

Sysname-vsan2-zone-z1 pairwise-zoning enable

【相关命令】

·**member (zone view)**

·**member (zone-alias view)**

·**zoneset activate**

·**zoneset distribute**

**FC和FCoE \-- FC Zone配置命令 \-- reset zone statistics**

------------------------------------------------------------------------

**[reset zone statistics**]命令用来清除Zone报文统计信息。

【命令】

**[reset zone statistics** [ **vsan** *vsan-id* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan ***vsan-id*]：清除指定VSAN内的Zone报文统计信息。*vsan-id*表示VSAN编号，取值范围为1～3839。不指定本参数，将清除所有VSAN内的Zone报文统计信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 清除VSAN 2内的Zone报文统计信息。

\<Sysname\> reset zone statistics vsan 2

【相关命令】

·**display zone statistics**

**FC和FCoE \-- FC Zone配置命令 \-- snmp-agent trap enable fc-zone**

------------------------------------------------------------------------

**[snmp-agent trap enable fc-zone**]命令用来开启Zone的告警功能。

**[undo snmp-agent trap enable fc-zone**]命令用来关闭Zone的告警功能。

【命令】

**[snmp-agent trap enable fc-zone**[ [ **activation-completed** \| **defaultzone-change** \| **hardzone-change** \| **merge-failed** \| **merge-succeeded** ] \*]]

**[undo snmp-agent trap enable fc-zone**[ [ **activation-completed** \| **defaultzone-change** \| **hardzone-change** \| **merge-failed** \| **merge-succeeded** ] \*]]

【缺省情况】

Zone的告警功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[activation-completed**]：表示已完成激活/取消激活Zone set的告警信息。

**[defaultzone-change**]：表示默认Zone策略发生变化的告警信息。

**[hardzone-change**]：表示硬Zone功能已关闭的告警信息。

**[merge-failed**]：表示合并失败的告警信息。

**[merge-succeeded**]：表示合并成功的告警信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

如果未指定任何参数，则表示开启或关闭Zone的全部告警功能。

开启了Zone的告警功能之后，Zone会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启Zone的全部告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable fc-zone

**FC和FCoE \-- FC Zone配置命令 \-- zone clone**

------------------------------------------------------------------------

**[zone clone**]命令用来复制Zone。

【命令】

**[zone clone ***src-name dest-name*]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[src-name*]：被复制的源Zone的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

*[dest-name*]：复制后的目的Zone的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone z1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone name z1

Sysname-vsan1-zone-z1 quit

\# 复制z1到z2。

Sysname-vsan1 zone clone z1 z2

【相关命令】

·**display zone**

·**zone name**

**FC和FCoE \-- FC Zone配置命令 \-- zone default-zone permit**

------------------------------------------------------------------------

**[zone default-zone permit**]命令用来配置允许默认Zone内的成员互相访问。

**[undo zone default-zone permit**]命令用来配置禁止默认Zone内的成员互相访问。

【命令】

**[zone default-zone permit**]

**[undo zone default-zone permit**]

【缺省情况】

默认Zone内的成员禁止互相访问。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

在增强Zone模式下，需要通过激活Zone set或扩散命令显式地触发扩散，使默认Zone策略随同其它数据一同向全网扩散。但是在基本Zone模式下，必须手动配置全网默认Zone策略一致。

在Zone模式切换时，为保证切换后全网默认Zone策略的一致性，无论是基本Zone向增强Zone切换，还是增强Zone向基本Zone扩散，默认Zone策略也会随同其它数据一同向全网扩散。

在增强Zone模式下，VSAN内交换机发生合并时，要求发生合并的交换机必须具有相同的默认Zone策略，否则合并失败，链路将被隔离。

【举例】

\# 配置允许默认Zone内的成员互相访问。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone default-zone permit

【相关命令】

·**display** **zone status**

·**zone mode enhanced**

·**zoneset acti****vate**

·**zoneset distribute**

**FC和FCoE \-- FC Zone配置命令 \-- zone hard-zoning enable**

------------------------------------------------------------------------

**[zone hard-zoning enable**]命令用来开启VSAN下的硬件Zone。

**[undo zone hard-zoning enable**]命令用来关闭VSAN下硬件Zone。

【命令】

**[zone hard-zoning enable**]

**[undo zone hard-zoning enable**]

【缺省情况】

VSAN下的硬件Zone处于开启状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

当底层资源足够下发Zone规则时，硬件Zone才能生效，而软件Zone一直处于生效状态。当底层资源足够下发当前VSAN的硬件Zone规则时，该VSAN的软件Zone和硬件Zone一起生效；当底层资源不够下发当前VSAN的硬件Zone规则时，为了保证规则的完整性，系统会清空该VSAN已下发的硬件Zone规则，自动切换为硬件Zone未生效状态，此时该VSAN下只有软件Zone继续生效。

当用户希望增强某VSAN的安全性时，可以开启该VSAN的硬件Zone。当用户认为软件Zone能够满足某VSAN的节点访问控制要求时，可以关闭该VSAN的硬件Zone，节约硬件表项资源供其它重要VSAN使用。

开启某VSAN的硬件Zone后，系统将触发一次下发该VSAN的所有Zone规则的操作；关闭某VSAN的硬件Zone后，系统会清空该VSAN当前已经下发的硬件Zone规则，并且后续不会下发任何新的硬件Zone规则。

在增强Zone模式下，需要通过激活Zone set或扩散命令显式地触发扩散，使硬件Zone配置随同其它数据一同向全网扩散。但是在基本Zone模式下，必须手动配置保证全网硬件Zone配置的一致性。

用户可以通过**display zone status**命令查询当前硬件Zone的生效状态。

需要注意的是，当交换机处于合并或扩散状态时，不能配置本命令。

【举例】

\# 关闭VSAN 2下硬件Zone。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 undo zone hard-zoning enable

【相关命令】

·**display zone status**

**FC和FCoE \-- FC Zone配置命令 \-- zone merge-control restrict**

------------------------------------------------------------------------

**[zone merge-control restrict**]命令用来在增强Zone模式下，配置当前VSAN的合并控制模式为Restrict。

**[undo zone merge-control restrict**]命令用来恢复缺省情况。

【命令】

**[zone merge-control restrict**]

**[undo zone merge-control restrict**]

【缺省情况】

合并控制模式为Allow。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

合并控制模式分为两种：Restrict和Allow。在增强Zone模式下，当VSAN内的两台交换机发生合并时，合并操作的结果受其所配置的合并控制模式的影响。并且，只有当发生合并的交换机具有相同的合并控制模式时才允许进行合并，否则合并失败，链路将被隔离。

需要注意到是，本命令仅支持在增强Zone模式下配置，该配置需要通过激活Zone set或扩散命令显式地触发扩散，保证全网一致性。

【举例】

\# 配置VSAN 2的合并控制模式为Restrict。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 zone merge-control restrict

\# 配置VSAN 2的合并控制模式为Allow。

Sysname-vsan2 undo zone merge-control restrict

【相关命令】

·**zone mode enhanced**

·**zoneset activate**

·**zoneset distribute**

**FC和FCoE \-- FC Zone配置命令 \-- zone mode enhanced**

------------------------------------------------------------------------

**[zone mode enhanced**]命令用来配置当前VSAN工作在增强Zone模式。

**[undo zone mode enhanced**]命令用来恢复缺省情况。

【命令】

**[zone mode enhanced**]

**[undo zone mode enhanced**]

【缺省情况】

当前VSAN工作在基本Zone模式。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

Zone有两种工作模式：基本Zone模式和增强Zone模式。当进行Zone模式切换时，将进行Fabric内的扩散操作，以保证Fabric内的所有交换机的Zone模式的一致性。因此，只有当Fabric中的所有交换机都支持增强Zone模式时，才允许配置为增强Zone模式。

如果Zone模式切换时未能成功在Fabric内完成扩散，可能造成本交换机Zone模式切换成功但Fabric内其它交换机Zone模式切换失败的情况。如果扩散失败，系统将打印日志信息，告知用户扩散失败。此时，需要用户主动激发一次完全扩散过程，以保证Fabric内所有交换机的Zone模式的一致性。

当从增强Zone模式切换为基本Zone模式时，若存在激活Zone set，且激活Zone set大小超过了基本Zone模式下激活Zone set的最大规格，则切换失败，本交换机的Zone模式不变。

【举例】

\# 配置VSAN 2工作在增强Zone模式。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 zone mode enhanced

【相关命令】

·**display zone status**

·**zoneset distribute**

**FC和FCoE \-- FC Zone配置命令 \-- zone name**

------------------------------------------------------------------------

**[zone name**]命令用来创建Zone，并进入其视图。如果指定的Zone已经创建，则该命令直接用来进入该Zone的视图。

**[undo zone name**]命令用来删除指定名称的Zone。

【命令】

**[zone name** *zone-name*]

**[undo zone name** *zone-name*]

【缺省情况】

不存在任何Zone。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[zone-name*]：Zone的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone z1，并进入其视图。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone name z1

Sysname-vsan1-zone-z1

【相关命令】

·**display zone**

**FC和FCoE \-- FC Zone配置命令 \-- zone rename**

------------------------------------------------------------------------

**[zone rename**]命令用来修改Zone的名称。

【命令】

**[zone rename***old-name new-name*]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[old-name*]：待重命名的Zone名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

*[new-name*]：新的Zone名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone z1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone name z1

Sysname-vsan1-zone-z1 quit

\# 将z1重命名为z2。

Sysname-vsan1 zone rename z1 z2

【相关命令】

·**display zone**

·**zone name**

**FC和FCoE \-- FC Zone配置命令 \-- zone-alias clone**

------------------------------------------------------------------------

**[zone-alias clone**]命令用来复制Zone别名。

【命令】

**[zone-alias clone ***src-name dest-name*]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[src-name*:]被复制的源Zone别名的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

*[dest-name*:]复制后的目的Zone别名的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone别名za1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone-alias name za1

Sysname-vsan1-zone-alias-za1 quit

\# 复制za1到za2。

Sysname-vsan1 zone-alias clone za1 za2

【相关命令】

·**display zone-alias**

·**zone-alias name**

**FC和FCoE \-- FC Zone配置命令 \-- zone-alias name**

------------------------------------------------------------------------

**[zone-alias name**]命令用来创建Zone别名，并进入其视图。如果指定的Zone别名已经创建，则该命令直接用来进入该Zone别名的视图。

**[undo zone-alias name**]命令用来删除指定名称的Zone别名。

【命令】

**[zone-alias name **]*zone-alias-name*

**[undo zone-alias name**]*zone-alias-name*

【缺省情况】

不存在任何Zone别名。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[zone-alias-name*]：Zone别名的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone别名za1，并进入其视图。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone-alias name za1

Sysname-vsan1-zone-alias-za1

【相关命令】

·**display zone-alias**

**FC和FCoE \-- FC Zone配置命令 \-- zone-alias rename**

------------------------------------------------------------------------

**[zone-alias rename**]命令用来修改Zone别名的名称。

【命令】

**[zone-alias rename***old-name new-name*]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[old-name*]：待重命名的Zone别名的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

*[new-name*]：新的Zone别名的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone别名za1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone-alias name za1

Sysname-vsan1-zone-alias-za1 quit

\# 将za1重命名为za2。

Sysname-vsan1 zone-alias rename za1 za2

【相关命令】

·**display zone-alias**

·**zone-alias name**

**FC和FCoE \-- FC Zone配置命令 \-- zoneset activate**

------------------------------------------------------------------------

**[zoneset activate**]命令用来激活指定Zone set生成Active Zone set，并发起向全网的扩散过程。

**[undo zoneset activate**]命令用来删除Active Zone set，并发起向全网的扩散过程。

【命令】

**[zoneset activate name ***zoneset-name*]

**[undo zoneset activate**]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name **]*zoneset-name*：被激活的Zone set的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。指定的Zone set必须已经存在。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

虽然每个VSAN内可以配置多个Zone set，但只有一个可以生效，称为Active Zone set。最终N_Port成员的访问控制都在Active Zone set内进行匹配。

Active Zone set需要通过命令显式地在本地交换机上激活，并向整个Fabric进行同步，使其在全网范围内保持一致。如果扩散失败，系统将打印日志信息，告知用户扩散失败。此时需要用户重新激活该Zone set，以保证Fabric内所有交换机的Active Zone set数据的一致性。

在将Active Zone set进行全网扩散时，交换机会根据**zoneset distribute full**命令配置的扩散类型来决定扩散时是否携带数据库信息。

被激活的Zone set中至少要包含一个N_Port成员。

同一VSAN内只能够存在一个Active Zone set。

在基本Zone模式下，若Active Zone set超过了最大规格，则激活失败。

【举例】

\# 创建Zone z1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zone name z1

\# 添加FC地址为010000的N_Port为z1成员。

Sysname-vsan1-zone-z1 member fcid 010000

Sysname-vsan1-zone-z1 quit

\# 创建Zone set zs1。

Sysname-vsan1 zoneset name zs1

\# 添加z1为zs1的成员。

Sysname-vsan1-zoneset-zs1 member z1

Sysname-vsan1-zoneset-zs1 quit

\# 激活zs1。

Sysname-vsan1 zoneset activate name zs1

【相关命令】

·**display zoneset active**

·**zoneset distribute full**

**FC和FCoE \-- FC Zone配置命令 \-- zoneset clone**

------------------------------------------------------------------------

**[zoneset clone**]命令用来复制Zone set。

【命令】

**[zoneset clone ***src-name dest-name*]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[src-name*]：被复制的源Zone set的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

*[dest-name*]：复制后的目的Zone set的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone set zs1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zoneset name zs1

Sysname-vsan1-zoneset-zs1 quit

\# 复制zs1到zs2。

Sysname-vsan1 zoneset clone zs1 zs2

【相关命令】

·**display zoneset**

·**zoneset name**

**FC和FCoE \-- FC Zone配置命令 \-- zoneset distribute**

------------------------------------------------------------------------

**[zoneset distribute**]命令用来激发完全扩散过程，扩散的内容包括Active Zone set以及数据库。

【命令】

**[zoneset distribute**]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

配置该命令会触发一次Zone数据扩散流程，且为完全扩散，即将Active Zone set和数据库均携带在报文中进行扩散。

使用激活命令**zoneset activate**激活一个Zone set成为Active Zone set后，用户可以继续修改数据库的配置，本命令可以在不改变Active Zone set的同时将Active Zone set以及修改后的数据库向全网扩散。

如果扩散失败，系统将打印日志信息，告知用户扩散失败。此时需要用户重新激发一次完全扩散，以保证Fabric内所有交换机的Zone数据的一致性。

【举例】

\# 激发完全扩散过程。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zoneset distribute

**FC和FCoE \-- FC Zone配置命令 \-- zoneset distribute full**

------------------------------------------------------------------------

**[zoneset distribute full**]命令用来配置扩散和合并类型为完全扩散和完全合并。

**[undo zoneset distribute full**]命令用来恢复扩散和合并类型为非完全扩散和非完全合并。

【命令】

**[zoneset distribute full**]

**[undo zoneset distribute full**]

【缺省情况】

基本Zone模式下，扩散和合并类型为非完全扩散和非完全合并。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

完全扩散和完全合并会将Active Zone set以及数据库都进行扩散和合并；非完全扩散和非完全合并仅将Active Zone set进行扩散和合并。

需要注意的是：

·本命令只允许在基本Zone模式下配置。在增强Zone模式下，扩散和合并类型固定为完全扩散和完全合并，因此不支持本命令。

·基本Zone模式下，扩散类型仅会对使用**zoneset activate**命令激发的扩散过程产生影响，对使用**zoneset distrbute**命令激发的扩散不会产生影响。

·基本Zone模式下，合并类型会对所有合并过程产生影响。

【举例】

\# 配置扩散和合并类型为完全扩散和完全合并。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zoneset distribute full

【相关命令】

·**display zone status**

·**zoneset activate**

**FC和FCoE \-- FC Zone配置命令 \-- zoneset name**

------------------------------------------------------------------------

**[zoneset name**]命令用来创建Zone set，并进入其视图。如果指定的Zone set已经创建，则该命令直接用来进入该Zone set的视图。

**[undo zoneset name**]命令用来删除指定名称的Zone set。

【命令】

**[zoneset name ***zoneset-name*]

**[undo zoneset name ***zoneset-name*]

【缺省情况】

不存在任何Zone set。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[zoneset-name*:Zone set]的名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone set zs1并进入其视图。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zoneset name zs1

Sysname-vsan1-zoneset-zs1

【相关命令】

·**display zoneset**

**FC和FCoE \-- FC Zone配置命令 \-- zoneset rename**

------------------------------------------------------------------------

 **zoneset rename**命令用来修改Zone set的名称。

【命令】

**[zoneset rename***old-name new-name*]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[old-name*]：待重命名的Zone set名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

*[new-name*]：新的Zone set名称，为1～64个字符的字符串，区分大小写，只能包含大小写英文字母、数字以及下列特殊符号：\$-\^\_，并且名称的起始字符只能为大小写英文字母。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

【举例】

\# 创建Zone set zs1。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 zoneset name zs1

Sysname-vsan1-zoneset-zs1 quit

\# 将zs1重命名为zs2。

Sysname-vsan1 zoneset rename zs1 zs2

【相关命令】

·**display zoneset**

·**zoneset name**

**FC和FCoE \-- NPV配置命令 \-- display fc nport**

------------------------------------------------------------------------

**[display** **fc** **nport**]命令用来显示NPV交换机向FCF交换机进行注册的信息以及获取到的管理地址。

【命令】

**[display** **fc** **nport** [ **interface** *interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type* *interface-number*]：显示从指定接口获取到的FCF交换机管理地址，*interface*-*type*只能是FC接口、VFC接口或FC聚合接口，且只能指定NP模式的接口。如果未指定本参数，将显示从所有FC接口、VFC接口和FC聚合接口获取到的FCF交换机管理地址。

【使用指导】

只有NPV交换机和FCF-NPV交换机支持本命令。

本命令可以显示NPV交换机通过up的NP模式接口，向FCF交换机发送的注册信息，以及从FCF交换机获取到的管理地址。

需要注意的是，只有NPV交换机向FCF交换机成功注册后，才能显示相关信息。

【举例】

\# 显示NPV交换机向FCF交换机进行注册的信息以及获取到的管理地址。

\<Sysname\> display fc nport

NP port: FC1/0/5

  Port-WWN: 20:00:00:41:22:a8:00:05

  FC4-types(FC4_features): NPV

  Symbolic-node-name: NPV-Sysname

  Symbolic-port-name: NPV-Sysname:FC1/0/5

  Node-IP-addr: 192.168.0.153

  Peer management address: snmp://192.168.0.151

                           snmp://192.168.0.152

NP port: Vfc2

  Port-WWN: 20:00:00:49:c9:28:c7:01

  FC4-types(FC4_features): NPV

  Symbolic-node-name: NPV-Sysname

  Symbolic-port-name: NPV-Sysname:Vfc2

  Node-IP-addr: 192.168.0.153

  Peer management address: snmp://192.168.0.151

                           snmp://192.168.0.152

表1-45 display fc nport命令显示信息描述表

字段

描述

NP port

NP模式接口的名称

Port-WWN

NP模式接口的WWN

FC4-types(FC4 features)

NP模式接口固定注册FC4类型为NPV，无FC4属性

Symbolic-node-name

NPV节点的符号名称，用于描述此节点。NP模式接口会携带本机系统名，注册形如*system-name*的字符串作为节点描述名

Symbolic-port-name

NP模式接口的符号名称，用于描述此端口。NP模式接口会携带本机系统名和端口名，注册形如*system-name*:*port-name*的字符串作为端口描述名

Node-IP-addr

NPV交换机的IP地址

Peer management address

NP模式接口获取到的FCF交换机管理地址列表。例如：snmp://192.168.6.151，表示管理协议为SNMP，管理地址为192.168.6.151。显示为空表示FCF交换机上未配置管理地址

**FC和FCoE \-- NPV配置命令 \-- display npv login**

------------------------------------------------------------------------

**[display npv login**]命令用来显示NPV交换机的下行口上相连的节点设备的注册信息和映射的上行口。

【命令】

**[display npv login** [ **vsan** *vsan-id*   **interface** *interface-type* *interface-number* ]]

**[display npv login** [ **vsan** *vsan-id*  **count**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的下行口上相连的节点设备的注册信息和映射的上行口，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的信息。在FCF-NPV交换机上，只能显示NPV模式VSAN内的信息。

**[interface** *interface-type* *interface-number*]：显示指定下行口上相连的节点设备的注册信息和映射的上行口。不指定该参数时，将显示所有下行口的信息。

**[count**]：显示登录节点的数目。

【使用指导】

只有NPV交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示NPV交换机的下行口上相连的节点设备的注册信息和映射的上行口。

\<Sysname\> display npv login

Server                                                                  External

Interface VSAN FCID     Node WWN                Port WWN                Interface

Fc1/0/2   1    0xae0002 20:00:00:23:89:c9:fc:05 20:00:00:23:89:c9:fc:05 Fc1/0/1

Vfc3      1    0xae0003 10:00:00:00:c9:66:6b:60 20:00:00:00:c9:66:6b:60 Fc1/0/1

\# 显示NPV交换机上VSAN 1的登录节点的数目。

\<Sysname\> display npv login vsan 1 count

Total entries: 2

\# 显示NPV交换机上所有VSAN的登录节点的数目。

\<Sysname\> display npv login count

VSAN        Entries

1           2

2           1

Total entries: 3

表1-46 display npv login命令显示信息描述表

字段

描述

Server Interface

下行口的接口名

External interface

下行口映射的上行口的接口名

VSAN

VSAN编号

FCID

节点的FC地址

Node WWN

节点的WWN

Port WWN

节点端口的WWN

Entries

某VSAN内登录节点的数目

Total entries

登录节点的总数目

**FC和FCoE \-- NPV配置命令 \-- display npv status**

------------------------------------------------------------------------

**[display npv status**]命令用来显示NPV交换机的状态信息。

【命令】

**[display npv status** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan***vsan-id*]：显示指定VSAN内的状态信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的状态信息。在FCF-NPV交换机上，只能显示NPV模式VSAN内的状态信息。

【使用指导】

使用本命令可以查询到NPV交换机上各个接口在VSAN内的状态信息，包括接口VSAN Tag模式、接口在VSAN内的状态、FC地址等。

只有NPV交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示VSAN 1的NPV交换机的状态信息。

\<Sysname\> display npv status vsan 1

External Interfaces:

  Interface: Fc1/0/2  VSAN tagging mode: Tagging

    VSAN  State  FCID

    1     Up     0x010002

  Interface: Fc1/0/3  VSAN tagging mode: Non tagging

    VSAN  State  FCID

    1     Up     0x010001

  Number of External Interfaces: 2

Server Interfaces:

  Interface: Fc1/0/5  VSAN tagging mode: Tagging

    VSAN  State

    1     Down

  Number of Server Interfaces: 1

\# 显示所有VSAN的NPV交换机的状态信息。

\<Sysname\> display npv status

External Interfaces:

  Interface: Fc1/0/1  VSAN tagging mode: Non tagging

    VSAN  State  FCID

    2     Up     0x010003

  Interface: Fc1/0/2  VSAN tagging mode: Tagging

    VSAN  State  FCID

    1     Up     0x010002

    2     Up     0x010003(Unavailable)

    5     Down

  Interface: Fc1/0/3  VSAN tagging mode: Non tagging

    VSAN  State  FCID

    1     Up     0x010001

  Number of External Interfaces: 3

Server Interfaces:

  Interface: Fc1/0/4  VSAN tagging mode: Non tagging

    VSAN  State

    2     Up

  Interface: Fc1/0/5  VSAN tagging mode: Tagging

    VSAN  State

    1     Down

    2     Up

    3     Down

  Number of Server Interfaces: 2

表1-47 display npv status命令显示信息描述表

字段

描述

External Interfaces

上行口列表

Server Interfaces

下行口列表

Interface

接口名

VSAN tagging mode

VSAN Tag模式

VSAN

VSAN ID

State

当前接口的Up/Down状态

FCID

上行口Up后，会显示核心交换机为之分配的FC地址；下行口没有FC地址

（在一个VSAN内，如果NPV交换机同时接入两个Fabric网络，并且这两个Fabric网络为上行口分配了相同的FCID，那么其中一个上行口虽然可以Up，但并不能作为上行口工作，此时会在括号中显示Unavailable）

![说明](FC和FCoE命令.files/image002.png)

FC SAN中可能存在多个Fabric网络，比如FC SAN中有两台FC交换机，但这两台FC交换机之间并没有连接，那么每台FC交换机都自成一个Fabric网络。

Number of External Interfaces

上行口的数量

Number of Server Interfaces

下行口的数量

**FC和FCoE \-- NPV配置命令 \-- display npv traffic-map**

------------------------------------------------------------------------

**[display npv traffic-map**]命令用来显示NPV交换机上的流量映射信息。

【命令】

**[display** **npv** **traffic-map** [ **vsan** *vsan-id*   **interface** *interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的流量映射信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的流量映射信息。在FCF-NPV交换机上，只能显示NPV模式VSAN内的流量映射信息。

**[interface** *interface-type* *interface-number*]：显示NPV交换机上指定下行口的流量映射信息。不指定该参数时，将显示NPV交换机上所有下行口的流量映射信息。

【使用指导】

使用本命令可以查询到NPV交换机上的流量映射信息，即下行口到上行口的映射关系。

只有NPV交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示流量映射信息。

\<Sysname\> display npv traffic-map

NPV traffic map information of VSAN 1:

Server interface       External interface

Fc1/0/1                Fc1/0/3

Fc1/0/2                Fc1/0/3

Vfc1                   Fc1/0/4

表1-48 display npv traffic-map命令显示信息描述表

字段

描述

NPV traffic map information of VSAN 1

VSAN 1内上下行口映射信息

Server interface

下行口

External interface

上行口

**FC和FCoE \-- NPV配置命令 \-- npv auto-load-balance enable**

------------------------------------------------------------------------

**[npv auto-load-balance enable**]命令用来开启自动负载均衡功能。

**[undo npv auto-load-balance enable**]命令用来关闭自动负载均衡功能。

【命令】

**[npv auto-load-balance enable**]

**[undo npv auto-load-balance enable**]

【缺省情况】

自动负载均衡功能处于关闭状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有NPV交换机和FCF-NPV交换机（NPV模式）支持本命令。

自动负载均衡的过程如下：当系统在VSAN内检测到up的上行口时，会自动创建一个延迟定时器（可通过**npv auto-load-balance-interval**命令配置），待定时器超时后，系统将自动进行一次负载均衡。如果在定时器超时前又有新的上行口up，则重置该定时器。

需要注意的是：

·开启了自动负载均衡功能后，上行口的up可能引起负载均衡的发生，从而可能导致流量中断。

·关闭了自动负载均衡功能后，不会影响现有的上下行口映射关系。

【举例】

\# 配置VSAN 1内开启自动负载均衡功能。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 npv auto-load-balance enable

**FC和FCoE \-- NPV配置命令 \-- npv auto-load-balance-interval**

------------------------------------------------------------------------

**[npv auto-load-balance-interval**]命令用来配置自动负载均衡的延迟时间。

**[undo auto-load-balance-interval**]命令用来恢复缺省情况。

【命令】

**[npv auto-load-balance-interval ***interval*]

**[undo auto-load-balance-interval**]

【缺省情况】

自动负载均衡的延迟时间为30秒。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：自动负载均衡的延迟时间，单位为秒，取值范围为1～300。

【使用指导】

只有NPV交换机和FCF-NPV交换机（NPV模式）支持本命令。

自动负载均衡的延迟时间主要用来缓冲上行口的up、down而引起震荡，以减少对自动负载均衡的影响。如果上行口的链路状况良好，可适当将减小延迟时间；否则，需增大延迟时间。

【举例】

\# 在VSAN 1内配置自动负载均衡的延迟时间为20秒。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 npv auto-load-balance-interval 20

**FC和FCoE \-- NPV配置命令 \-- npv load-balance disruptive**

------------------------------------------------------------------------

**[npv load-balance disruptive**]命令用来发起一次中断负载均衡过程。

【命令】

**[npv load-balance disruptive**]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有NPV交换机和FCF-NPV交换机（NPV模式）支持本命令。

当某VSAN内各个接口负载不均衡时，可以使用本命令在VSAN内发起一次中断负载均衡过程，强制该VSAN内的所有下行节点重新登录。发起中断负载均衡过程后，系统会重新进行上下行口的负载均衡分配，以达到更好的负载均衡效果，但会破坏已经稳定的上下行口的映射关系，从而导致流量中断。

【举例】

\# 在VSAN 1内发起一次中断负载均衡过程。

\<Sysname\> system-view

Sysname vsan 1

Sysname-vsan1 npv load-balance disruptive

**FC和FCoE \-- NPV配置命令 \-- npv traffic-map**

------------------------------------------------------------------------

**[npv traffic-map**]命令用来配置上下行口的映射关系。

**[undo npv traffic-map**]命令用来删除配置的上下行口的映射关系。

【命令】

**[npv** **traffic-map** **server-interface** *interface-type* *interface-number* **external-interface** *interface-type* *interface-number*]

**[undo** **npv** **traffic-map** **server-interface** *interface-type* *interface-number* **external-interface** *interface-type* *interface-number*]

【缺省情况】

上下行口之间不存在映射关系。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[server-interface** *interface-type* *interface-number*]：指定下行口。可以是FC接口或者VFC接口。

**[external-interface** *interface-type* *interface-number*]：指定上行口。可以是FC接口或者VFC接口。

【使用指导】

只有NPV交换机和FCF-NPV交换机（NPV模式）支持本命令。

在进行下行口到上行口的映射时，如果该下行口有配置到上行口的映射关系，则该下行口只能从配置的上行口中选择一个有效接口进行映射，如果没有配置映射关系则可以从属于同一VSAN的所有上行口中选择一个有效接口进行映射。

【举例】

\# 在VSAN10内配置接口FC1/0/1到FC1/0/2的映射关系，其中FC1/0/1作为下行口，FC1/0/2作为上行口。

\<Sysname\> system-view

Sysname vsan 10

Sysname-vsan10 npv traffic-map server-interface fc 1/0/1 external-interface fc 1/0/2

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping enode**

------------------------------------------------------------------------

**[display fip-snooping enode**]命令用来显示Transit交换机获取到的ENode信息。

【命令】

**[display fip-snooping enode** [ **vlan** *vlan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN的ENode信息。*vlan-id*的取值范围为1～4094。不指定本参数，将显示所有VLAN的ENode信息。

【举例】

\# 显示Transit交换机获取到的ENode信息。

\<Sysname\> display fip-snooping enode

VLAN 2:

Interface   ENode WWN                ENode MAC

XGE1/0/1    21:01:00:1b:32:a0:fa:18  000c-2999-eacd

表1-49 display fip-snooping enode命令显示信息描述表

字段

描述

VLAN 2

显示VLAN 2的信息

Interface

Transit交换机上连接ENode的以太网接口

ENode WWN

ENode的WWN

ENode MAC

ENode的FCoE MAC地址

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping fcf**

------------------------------------------------------------------------

**[display fip-snooping fcf**]命令用来显示Transit交换机获取到的FCF交换机信息。

【命令】

**[display fip-snooping fcf** [ **vlan** *vlan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN的FCF交换机信息。*vlan-id*的取值范围为1～4094。不指定本参数，将显示所有VLAN的FCF交换机信息。

【举例】

\# 显示Transit交换机获取到的FCF交换机信息。

\<Sysname\> display fip-snooping fcf

VLAN 3:

Interface   FCF MAC        FCF WWN                 Fabric Name             ENode

XGE1/0/1    000c-2999-eacd 66:66:66:63:66:64:61:30 41:6e:64:69:61:6d:6f:21 1

XGE1/0/2    000c-2999-eaad 66:66:66:63:66:64:61:31 41:6e:64:69:61:6d:6f:22 2

表1-50 display fip-snooping fcf命令显示信息描述表

字段

描述

VLAN 3

显示VLAN 3的信息

Interface

Transit交换机上连接FCF交换机的以太网接口

FCF MAC

FCF交换机的FCoE MAC地址

FCF WWN

FCF交换机的WWN地址

Fabric Name

Fabric网络的名称

ENode

该FCF交换机下存在的ENode的个数

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping flushing-rules**

------------------------------------------------------------------------

**[display fip-snooping flushing-rules**]命令用来显示正在下刷的FIP Snooping规则。

【命令】

**[display fip-snooping flushing-rules**[ [ **enode** \| **fcf** ]  **vlan** *vlan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[enode**]：显示正在下刷的ENode FIP Snooping规则。

**[fcf**]：显示正在下刷的FCF FIP Snooping规则。

**[vlan** *vlan-id*]：显示指定VLAN的正在下刷的FIP Snooping规则。*vlan-id*的取值范围为1～4094。不指定本参数，将显示所有VLAN的正在下刷的FIP Snooping规则。

【使用指导】

只有已经下刷的FIP Snooping规则可以用来过滤FCoE报文，正在下刷的FIP Snooping规则不能用来过滤FCoE报文。

需要注意的是，如果不指定**enode**和**fcf**参数，则显示正在下刷的所有FIP Snooping规则，包括ENode FIP Snooping规则和FCF FIP Snooping规则。

【举例】

\# 显示正在下刷的所有FIP Snooping规则。

\<Sysname\> display fip-snooping flushing-rules

VLAN 2:

  FCF flushing-rules information:

    Interface   Source MAC/Mask      Destination MAC/Mask

    XGE1/0/1    0000-1234-0212/48    0efc-0034-0111/24

  ENode flushing-rules information:

    Interface   Source MAC/Mask      Destination MAC/Mask

    XGE1/0/2    0efc-0034-0202/48    0000-1234-0101/48

VLAN 5:

  FCF flushing-rules information:

    Interface   Source MAC/Mask      Destination MAC/Mask

    XGE1/0/3    0000-1234-2212/48    0efc-0034-2111/24

表1-51 display fip-snooping flushing-rules命令显示信息描述表

字段

描述

VLAN 2

显示VLAN 2的信息

FCF flushing-rules information

正在下刷的FCF FIP Snooping规则

ENode flushing-rules information

正在下刷的ENode FIP Snooping规则

Interface

Transit交换机上的以太网接口

Source MAC/Mask

源MAC地址和掩码

Destination MAC/Mask

目的MAC地址和掩码

【相关命令】

·**display fip-snooping rules**

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping rules**

------------------------------------------------------------------------

**[display fip-snooping rules**]命令用来显示已经下刷的FIP Snooping规则。

【命令】

集中式设备：

**[display fip-snooping rules**[ [ **enode** \| **fcf** ]  **vlan** *vlan-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display fip-snooping rules**[ [ **enode** \| **fcf** ]  **vlan** *vlan-id*   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display fip-snooping rules**[ [ **enode** \| **fcf** ]  **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[enode**]：显示已经下刷的ENode FIP Snooping规则。

**[fcf**]：显示已经下刷的FCF FIP Snooping规则。

**[vlan** *vlan-id*]：显示指定VLAN的已经下刷的FIP Snooping规则。*vlan-id*的取值范围为1～4094。不指定本参数，将显示所有VLAN的已经下刷的FIP Snooping规则。

**[slot**]slot-number{.commandparameterChar}：显示指定单板上的信息。slot-number{.commandparameterChar}表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]slot-number{.commandparameterChar}：显示指定成员设备上的信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]slot-number{.commandparameterChar}：显示指定成员设备/PEX上的信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示所有成员设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]chassis-number{.commandparameterChar} **slot** slot-number{.commandparameterChar}：显示指定成员设备指定单板上的信息。chassis-number{.commandparameterChar}表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number* **slot** *slot-number*：显示指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

只有已经下刷的FIP Snooping规则可以用来过滤FCoE报文，正在下刷的FIP Snooping规则不能用来过滤FCoE报文。

需要注意的是，如果不指定**enode**和**fcf**参数，则显示已经下刷的所有FIP Snooping规则，包括ENode FIP Snooping规则和FCF FIP Snooping规则。

【举例】

\# 显示已经下刷的所有FIP Snooping规则。

\<Sysname\> display fip-snooping rules slot 1

Slot 1:

  VLAN 2：

    FCF rules information:

      Interface   Source MAC/Mask     Destination MAC/Mask   DriverContext

      XGE1/0/1    0000-1234-0202/48   0efc-0034-0101/24      ffffffff

    ENode rules information:

      Interface   Source MAC/Mask     Destination MAC/Mask   DriverContext

      XGE1/0/2    0efc-0034-0102/48   0000-1234-0201/48      ffffffff

  VLAN 4：

    FCF rules information:

      Interface  Source MAC/Mask      Destination MAC/Mask   DriverContext

      XGE1/0/3   0000-1234-1202/48    0efc-0034-1101/24      ffffffff

表1-52 display fip-snooping rules命令显示信息描述表

字段

描述

VLAN 2

显示VLAN 2的信息

FCF rules information

已经下刷的FCF FIP Snooping规则

ENode rules information

已经下刷的ENode FIP Snooping规则

Interface

Transit交换机上的以太网接口

Source MAC/Mask

源MAC地址和掩码

Destination MAC/Mask

目的MAC地址和掩码

DriverContext

驱动上下文

【相关命令】

·**display fip-snooping flushing-rules**

**FC和FCoE \-- FIP Snooping配置命令 \-- display fip-snooping sessions**

------------------------------------------------------------------------

**[display fip-snooping sessions**]命令用来显示FIP Snooping的会话信息，即ENode和FCF交换机的连接信息。

【命令】

**[display fip-snooping sessions** [ **vlan** *vlan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-id*]：显示指定VLAN的FIP Snooping会话信息。*vlan-id*的取值范围为1～4094。不指定本参数，将显示所有VLAN的FIP Snooping会话信息。

【举例】

\# 显示FIP Snooping的会话信息。

\<Sysname\> display fip-snooping sessions

VLAN 2:

FCF MAC         ENode MAC       VN_Port MAC     VN_Port WWN

0000-1234-0202  0000-1234-0100  0efc-00ae-0002  41:6e:64:69:61:6d:6f:21

表1-53 display fip-snooping sessions命令显示信息描述表

字段

描述

VLAN 2

VLAN 2中的FIP Snooping会话信息

FCF MAC

FCF的FCoE MAC地址

ENode MAC

ENode的FCoE MAC地址

VN_Port MAC

VN_Port的MAC地址

VN_Port WWN

VN_Port的WWN

**FC和FCoE \-- FIP Snooping配置命令 \-- fip-snooping enable**

------------------------------------------------------------------------

**[fip-snooping enable**]命令用来开启FIP Snooping功能。

**[undo fip-snooping enable**]命令用来恢复缺省情况。

【命令】

**[fip-snooping enable**]

**[undo fip-snooping enable**]

【缺省情况】

FIP Snooping功能处于关闭状态。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在Transit交换机上，没有开启FIP Snooping功能的VLAN不能处理FCoE报文和FIP报文。

当需要某VLAN具有处理FCoE报文以及FIP报文的能力时，开启该VLAN的FIP Snooping功能。

【举例】

\# 开启VLAN 10的FIP Snooping功能。

\<Sysname\> system-view

Sysname vlan 10

Sysname-vlan10 fip-snooping enable

**FC和FCoE \-- FIP Snooping配置命令 \-- fip-snooping fc-map**

------------------------------------------------------------------------

**[fip-snooping fc-map**]命令用来配置VLAN下的FC-MAP值。

**[undo fip-snooping fc-map**]命令用来恢复缺省情况。

【命令】

**[fip-snooping fc-map** *fc-map*]

**[undo fip-snooping fc-map**]

【缺省情况】

每个VLAN下的FC-MAP值均为0x0EFC00。

【视图】

VLAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[fc-map*]：FC-MAP值，取值范围为0x0EFC00～0x0EFCFF。

【使用指导】

Transit交换机上某VLAN中的以太网接口从FCF交换机接收到报文后，会检查接收报文的FC-MAP值和Transit交换机上该VLAN下的FC-MAP值是否一致：如果一致，则转发报文；如果不一致，则丢弃报文。

【举例】

\# 配置VLAN 10的FC-MAP值为0x0EFCFF。

\<Sysname\> system-view

Sysname vlan 10

Sysname-vlan 10 fip-snooping fc-map 0efcff

【相关命令】

·**fcoe fcmap**

**FC和FCoE \-- FIP Snooping配置命令 \-- fip-snooping port-mode**

------------------------------------------------------------------------

**[fip-snooping port-mode**]命令用来配置Transit交换机上以太网接口的模式。

**[undo fip-snooping port-mode**]命令用来恢复缺省情况。

【命令】

**[fip-snooping port-mode**[ { **enode** \| **fcf** }]]

**[undo fip-snooping port-mode**]

【缺省情况】

以太网接口为ENode模式。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[enode**]：ENode模式。

**[fcf**]：FCF模式。

【使用指导】

Transit交换机上的以太网接口有两种模式：FCF模式和ENode模式。

·与ENode相连的以太网接口需要配置为ENode模式。

·与FCF交换机相连的以太网接口需要配置为FCF模式。

【举例】

\# 将接口Ten-GigabitEthernet1/0/2配置为FCF模式。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/0/2

Sysname-Ten-GigabitEthernet1/0/2 fip-snooping port-mode fcf

**FC和FCoE \-- FC端口安全配置命令 \-- any-wwn**

------------------------------------------------------------------------

**[any-wwn**]命令用来配置允许任意设备在指定接口登录。

**[undo** **any-wwn**]命令用来恢复缺省情况。

【命令】

**[any-wwn** **interface** *interface-list*]

**[undo** **any-wwn** **interface** *interface-list*]

【缺省情况】

未配置接口允许任意设备登录。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-list*]：表示允许登录的接口，表示方式为*interface-list* = { *interface-type* *interface-number1* [ **to** *interface-type* *interface-number2*  }&\<1-10\>]。其中，*interface-type*为接口类型，*interface-number*为接口编号。&\<1-10\>表示前面的参数最多可以输入10次。支持FC接口（不能是FC聚合的成员接口）、VFC接口、FC聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该接口上已登录设备的登录状态。该接口上已登录的设备是否会下线，取决于配置安全策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线。

需要注意的是，开启FC端口安全功能后才能配置本命令。

【举例】

\# 在VSAN 2中配置允许任意设备在FC1/0/1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 any-wwn interface fc 1/0/1

\# 在VSAN 2中配置允许任意设备在VFC1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 any-wwn interface vfc 1

【相关命令】

·**display** **fc-port-security** **database**

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security database**

------------------------------------------------------------------------

**[display** **fc-port-security** **database**]命令用来显示FC端口安全策略数据库中的表项。

【命令】

**[display**[ **fc-port-security** **database** { **all** \| **auto-learn** \| **static** } [ **interface** *interface-type* *interface-number* ]  **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示FC端口安全策略数据库中的所有表项，包括static表项、learned表项、learning表项。

**[auto-learn**]：显示FC端口安全策略数据库中的learned表项和learning表项。

**[static**]：显示FC端口安全策略数据库中的static表项。

**[interface** *interface-type*  *interface-number*]：显示FC端口安全策略数据库中指定接口相关的表项。如果不指定接口，则显示FC端口安全策略数据库中所有接口的表项。

**[vsan** *vsan-id*]：显示FC端口安全策略数据库中指定VSAN内的表项，*vsan-id*的取值范围为1～3839。如果不指定VSAN，则显示FC端口安全策略数据库中所有VSAN内的表项。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示FC端口安全策略数据库中VSAN 2内的所有表项。

\<Sysname\> display fc-port-security database all vsan 2

Total entries: 7

Database for VSAN 2:

  Logging-in entity                Interface              Type

  Any WWN                          Fc1/0/7                Static

  20:33:44:78:66:77:ab:97(pWWN)    Any interface          Static

  20:36:44:78:66:77:ab:97(pWWN)    Fc1/0/6                Static

  20:36:44:78:66:77:ab:9e(pWWN)    Fc1/0/9                Learned

  20:86:44:65:90:2a:ab:3a(pWWN)    Fc1/0/5                Learning

  10:83:45:78:66:77:ab:93(nWWN)    Fc1/0/7                Static

  10:36:44:78:66:77:ab:96(sWWN)    Fc1/0/8                Static

表1-54 display fc-port-security database命令显示信息描述表

字段

描述

Total entries

表项的数目

Database for VSAN

指定VSAN内的表项

Logging-in entity

允许登录设备的WWN（Any WWN表示允许任意设备登录），括号中显示的是WWN类型，包括：

·pWWN：表示N_Port或NP_Port的WWN

·sWWN：表示FCF交换机的WWN

·nWWN：表示节点设备或NPV交换机的WWN

Interface

设备允许登录的接口，Any interface表示允许在任意接口登录

Type

表项的类型，包括：

·static：表示手工配置的表项

·learned：表示关闭自动学习功能后，由learning表项转化为的learned表项，不随设备的下线而删除

·learning：表示通过自动学习功能动态学习的临时表项，将随设备的下线而删除

【相关命令】

·**reset** **fc-port-security** **database**

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security statistics**

------------------------------------------------------------------------

**[display** **fc-port-security** **statistics**]命令用来显示FC端口安全的统计信息。

【命令】

**[display** **fc-port-security** **statistics** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的FC端口安全的统计信息，*vsan-id*的取值范围为1～3839。如果不指定VSAN，则显示所有VSAN内的FC端口安全的统计信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示VSAN 2的FC端口安全的统计信息。

\<Sysname\> display fc-port-security statistics vsan 2

Statistics for VSAN 2:

  Number of permitted pWWN logins: 2

  Number of permitted nWWN logins: 2

  Number of permitted sWWN logins: 2

  Number of denied pWWN logins   : 0

  Number of denied nWWN logins   : 0

  Number of denied sWWN logins   : 0

  Total logins permitted  : 6

  Total logins denied     : 0

表1-55 display fc-port-security statistics命令显示信息描述表

字段

描述

Statistics for VSAN

指定VSAN内的统计信息

Number of permitted pWWN logins

允许PWWN登录的次数

Number of permitted nWWN logins

允许NWWN登录的次数

Number of permitted sWWN logins

允许SWWN登录的次数

Number of denied pWWN logins

拒绝PWWN登录的次数

Number of denied nWWN logins

拒绝NWWN登录的次数

Number of denied sWWN logins

拒绝SWWN登录的次数

Total logins permitted

总共允许登录的次数

Total logins denied

总共拒绝登录的次数

【相关命令】

·**reset** **fc-port-security** **statistics**

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security status**

------------------------------------------------------------------------

**[display** **fc-port-security** **status**]命令用来显示是否开启FC端口安全功能和自动学习功能。

【命令】

**[display** **fc-port-security** **status** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN的FC端口安全功能和自动学习功能开启情况，*vsan-id*的取值范围为1～3839。如果不指定VSAN，则显示所有VSAN的FC端口安全功能和自动学习功能开启情况。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

本命令查看是否开启FC端口安全功能和自动学习功能，包括由命令**fc-port-security** **enable**和**fc-port-security** **auto-learn**引起的状态变化。

【举例】

\# 显示所有VSAN的FC端口安全功能和自动学习功能开启情况。

\<Sysname\> display fc-port-security status

Status for VSAN 1:

  FC port security: Disabled

  Auto learn: Disabled

Status for VSAN 2:

  FC port security: Enabled

  Auto learn: Enabled

表1-56 display fc-port-security status命令显示信息描述表

字段

描述

Status for VSAN

指定VSAN内FC端口安全功能和自动学习功能开启情况

FC port security

FC端口安全功能的开启状态，包括：

·Enabled：表示开启

·Disabled：表示关闭

Auto learn

自动学习功能的开启状态，包括：

·Enabled：表示开启

·Disabled：表示关闭

开启FC端口安全功能时是否开启自动学习功能同样会影响该状态

【相关命令】

·**fc-port-security** **auto-learn**

·**fc-port-security** **enable**

**FC和FCoE \-- FC端口安全配置命令 \-- display fc-port-security violation**

------------------------------------------------------------------------

**[display** **fc-port-security** **violation**]命令用来显示非法登录的信息。

【命令】

**[display** **fc-port-security** **violation** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的非法登录信息，*vsan-id*的取值范围为1～3839。如果不指定VSAN，则显示所有VSAN内的非法登录信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示VSAN 2内的非法登录信息。

\<Sysname\> display fc-port-security violation vsan 2

Total entries: 3

Violations for VSAN 2:

  Interface   Logging-in entity               Last time             Repeat count

  Fc1/0/7     20:36:44:78:66:77:ab:97(pWWN)   2013/10/30 12:59:23   2

              20:00:00:e0:8b:06:d9:1d(nWWN)

  Fc1/0/8     20:45:78:66:77:ab:98:12(pWWN)   2013/10/29 17:59:23   3

              20:00:00:e0:8b:06:d9:1d(nWWN)

  Fc1/0/9     10:36:44:78:66:77:ab:96(sWWN)   2013/10/28 11:30:23   12

表1-57 display fc-port-security violation命令显示信息描述表

字段

描述

Total entries

非法登录信息总条数

Violations for VSAN

指定VSAN的非法登录信息

Interface

交换机的接口

Logging-in entity

非法登录设备的WWN，括号中显示的是WWN类型，包括：

·pWWN：表示N_Port或NP_Port的WWN

·sWWN：表示FCF交换机的WWN

·nWWN：表示节点设备或NPV交换机的WWN

Last time

该WWN最后一次非法登录的时间

Repeat count

该WWN在此接口重复非法登录的次数

**FC和FCoE \-- FC端口安全配置命令 \-- fc-port-security auto-learn**

------------------------------------------------------------------------

**[fc-port-security** **auto-learn**]命令用来开启自动学习功能。

**[undo** **fc-port-security** **auto-learn**]命令用来恢复缺省情况。

【命令】

**[fc-port-security** **auto-learn**]

**[undo** **fc-port-security** **auto-learn**]

【缺省情况】

自动学习功能处于关闭状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

开启自动学习功能后，后续登录的设备将以learning表项学习到策略数据库中。learning表项不对其它设备的登录产生影响，并将随设备下线而删除。关闭自动学习功能后，当前的learning表项将转化为learned表项，对后续设备的登录产生影响，此后该表项不再随设备下线而删除。

需要注意的是，开启FC端口安全功能后才能配置本命令。

【举例】

\# 在VSAN 2中开启自动学习功能。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fc-port-security enable

Sysname-vsan2 fc-port-security auto-learn

\# 学习完成后关闭自动学习功能，可以将learning表项转换为learned表项。

Sysname-vsan2 undo fc-port-security auto-learn

【相关命令】

·**display** **fc-port-security** **status**

**FC和FCoE \-- FC端口安全配置命令 \-- fc-port-security database copy**

------------------------------------------------------------------------

**[fc-port-security** **database** **copy**]命令用来将策略数据库中的learned表项转化为static表项。

【命令】

**[fc-port-security** **database** **copy**]

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

设备重启后，learned表项将会丢失。如果用户需要保留动态学习的learned表项，可以使用本命令将learned表项转化为static表项。

需要注意的是，开启FC端口安全功能后才能执行本命令。

【举例】

\# 在VSAN 2中将自动学习的learned表项转化为static表项。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fc-port-security database copy

【相关命令】

·**display** **fc-port-security** **database**

**FC和FCoE \-- FC端口安全配置命令 \-- fc-port-security enable**

------------------------------------------------------------------------

**[fc-port-security** **enable**]命令用来开启FC端口安全功能。

**[undo** **fc-port-security** **enable**]命令用来关闭FC端口安全功能。

【命令】

**[fc-port-security** **enable** [ **auto-learn** ]]

**[undo** **fc-port-security** **enable**]

【缺省情况】

FC端口安全功能处于关闭状态。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto-learn**]：开启自动学习功能。如果不指定本参数，则不开启自动学习功能。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

开启了FC端口安全功能后，将根据授权登录条件对当前已登录和后续登录交换机的设备进行检查，不符合授权登录条件的设备将不允许登录交换机。

开启FC端口安全功能时可选择是否同时开启自动学习功能：如果开启自动学习功能，交换机将对当前已登录和后续登录的设备进行学习，并以learning表项添加到策略数据库中；如果不开启自动学习功能，将导致当前已登录的设备下线。

需要注意的是，开启FC端口安全功能后才能进行FC端口安全相关的其它配置。

【举例】

\# 在VSAN 2中开启FC端口安全功能，并同时开启自动学习功能。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 fc-port-security enable auto-learn

【相关命令】

·**display** **fc-port-security** **status**

**FC和FCoE \-- FC端口安全配置命令 \-- nwwn**

------------------------------------------------------------------------

**[nwwn**]命令用来配置允许指定节点设备或NPV交换机在指定接口登录。

**[undo** **nwwn**]命令用来恢复缺省情况。

【命令】

**[nwwn** *nwwn* [ **interface** *interface-list* ]]

**[undo** **nwwn** *nwwn* [ **interface** *interface-list* ]]

【缺省情况】

未配置节点设备或NPV交换机与登录接口的绑定关系。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nwwn*]：节点设备或NPV交换机的NWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[interface** *interface-list*]：表示允许登录的接口，表示方式为*interface-list* = { *interface-type* *interface-number1* [ **to** *interface-type* *interface-number2*  }&\<1-10\>]。其中，*interface-type*为接口类型，*interface-number*为接口编号。&\<1-10\>表示前面的参数最多可以输入10次。支持FC接口（不能是FC聚合的成员接口）、VFC接口、FC聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。如果不指定接口，则表示允许在任意接口登录。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该节点设备或NPV交换机在已登录接口上的登录状态。如果命令中指定了允许登录的接口，则可能会影响该接口上已登录设备的登录状态。该节点设备或NPV交换机是否会在已登录接口下线，取决于配置安全策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线；该接口上已登录设备是否会下线，也是同理。

需要注意的是，开启FC端口安全功能后才能配置本命令。

【举例】

\# 在VSAN 2中配置允许NWWN为20:36:44:78:66:77:ab:9e的节点设备在FC1/0/1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 nwwn 20:36:44:78:66:77:ab:9e interface fc 1/0/1

\# 在VSAN 2中配置允许NWWN为20:36:44:78:66:77:ab:9e的节点设备在VFC1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 nwwn 20:36:44:78:66:77:ab:9e interface vfc 1

【相关命令】

·**display** **fc-port-security** **database**

**FC和FCoE \-- FC端口安全配置命令 \-- pwwn**

------------------------------------------------------------------------

**[pwwn**]命令用来配置允许指定N_Port或NP_Port在指定接口登录。

**[undo** **pwwn**]命令用来恢复缺省情况。

【命令】

**[pwwn** *pwwn* [ **interface** *interface-list* ]]

**[undo** **pwwn** *pwwn* [ **interface** *interface-list* ]]

【缺省情况】

未配置N_Port或NP_Port与登录接口的绑定关系。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pwwn*]：N_Port或NP_Port的PWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[interface** *interface-list*]：表示允许登录的接口，表示方式为*interface-list* = { *interface-type* *interface-number1* [ **to** *interface-type* *interface-number2*  }&\<1-10\>]。其中，*interface-type*为接口类型，*interface-number*为接口编号。&\<1-10\>表示前面的参数最多可以输入10次。支持FC接口（不能是FC聚合的成员接口）、VFC接口、FC聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。如果不指定接口，则表示允许在任意接口登录。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该N_Port或NP_Port在已登录接口上的登录状态。如果命令中指定了允许登录的接口，则可能会影响该接口上其它已登录设备的登录状态。该N_Port或NP_Port是否会在已登录接口下线，取决于配置策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线；该接口上已登录设备是否会下线，也是同理。

需要注意的是，开启FC端口安全功能后才能配置本命令。

【举例】

\# 在VSAN 2中配置允许PWWN为20:36:44:78:66:77:ab:9e的N_Port在FC1/0/1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 pwwn 20:36:44:78:66:77:ab:9e interface fc 1/0/1

\# 在VSAN 2中配置允许PWWN为20:36:44:78:66:77:ab:9e的N_Port在VFC1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 pwwn 20:36:44:78:66:77:ab:9e interface vfc 1

【相关命令】

·**display** **fc-port-security** **database**

**FC和FCoE \-- FC端口安全配置命令 \-- reset fc-port-security database**

------------------------------------------------------------------------

**[reset** **fc-port-security** **database**]命令用来清除FC端口安全策略数据库中的表项。

【命令】

**[reset**[ **fc-port-security** **database** { **all** \| **auto-learn** \| **static** } [ **interface** *interface-type* *interface-number* ] **vsan** *vsan-id*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：清除FC端口安全策略数据库中的static表项和learned表项。

**[auto-learn**]：清除FC端口安全策略数据库中的learned表项。

**[static**]：清除FC端口安全策略数据库中的static表项。

**[interface** *interface-type* *interface-number*]：清除FC端口安全策略数据库中指定接口相关的表项。如果不指定接口，则清除FC端口安全策略数据库中所有接口的表项。

**[vsan** *vsan-id*]：清除FC端口安全策略数据库中指定VSAN内的表项，*vsan-id*的取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

清除FC端口安全策略数据库中的表项后，将对已登录的设备重新根据授权登录条件进行检查，因此可能会导致当前已登录的设备下线。

【举例】

\# 清除FC端口安全策略数据库中VSAN 2内的所有static表项和learned表项。

\<Sysname\> reset fc-port-security database all vsan 2

【相关命令】

·**display** **fc-port-security** **database**

**FC和FCoE \-- FC端口安全配置命令 \-- reset fc-port-security statistics**

------------------------------------------------------------------------

**[reset** **fc-port-security** **statistics**]命令用来清除FC端口安全的统计信息。

【命令】

**[reset** **fc-port-security** **statistics** **vsan** *vsan-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan** *vsan-id*]：清除指定VSAN的FC端口安全统计信息，*vsan-id*的取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 清除VSAN 2的FC端口安全统计信息。

\<Sysname\> reset fc-port-security statistics vsan 2

【相关命令】

·**display** **fc-port-security** **statistics**

**FC和FCoE \-- FC端口安全配置命令 \-- snmp-agent trap enable fc-port-security**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable** **fc-port-security**]命令用来开启FC端口安全的告警功能。

**[undo** **snmp-agent** **trap** **enable** **fc-port-security**]命令用来关闭FC端口安全的告警功能。

【命令】

**[snmp-agent** **trap** **enable** **fc-port-security** [ **violation-happen** ]]

**[undo** **snmp-agent** **trap** **enable** **fc-port-security** [ **violation-happen** ]]

【缺省情况】

FC端口安全的告警功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[violation-happen**]：表示非法登录的告警功能。开启本告警功能后，当发生非法登录时会生成告警信息，其中携带非法登录设备的WWN、非法登录的接口以及非法登录的时间。如果未指定本参数，表示开启或关闭FC端口安全的全部告警功能。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

开启了FC端口安全的告警功能之后，FC端口安全会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启FC端口安全的全部告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable fc-port-security

**FC和FCoE \-- FC端口安全配置命令 \-- swwn**

------------------------------------------------------------------------

**[swwn**]命令用来配置允许指定FCF交换机在指定接口登录。

**[undo** **swwn**]命令用来恢复缺省情况。

【命令】

**[swwn** *swwn* [ **interface** *interface-list* ]]

**[undo** **swwn** *swwn* [ **interface** *interface-list* ]]

【缺省情况】

未配置FCF交换机与登录接口的绑定关系。

【视图】

VSAN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[swwn*]：FCF交换机的sWWN，格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[interface** *interface-list*]：表示允许登录的接口，表示方式为*interface-list* = { *interface-type* *interface-number1* [ **to** *interface-type* *interface-number2*  }&\<1-10\>]。其中，*interface-type*为接口类型，*interface-number*为接口编号。&\<1-10\>表示前面的参数最多可以输入10次。支持FC接口（不能是FC聚合的成员接口）、VFC接口、FC聚合接口。起始接口和终止接口必须具有相同的类型、属于相同的接口板，并且终止接口编号必须大于等于起始接口编号。如果不指定接口，则表示允许在任意接口登录。

【使用指导】

只有FCF交换机和FCF-NPV交换机（FCF模式）支持本命令。

由于安全策略变化后，将对已登录的设备重新根据授权登录条件进行检查。因此，本命令可能会影响该FCF交换机在已登录接口上的登录状态。如果命令中指定了允许登录的接口，则可能会影响该接口上其它已登录设备的登录状态。该FCF交换机是否会在已登录接口下线，取决于配置策略后是否仍满足授权登录条件：如满足则保持登录状态，否则会被下线；该接口上已登录设备是否会下线，也是同理。

需要注意的是，开启FC端口安全功能后才能配置本命令。

【举例】

\# VSAN 2中配置允许SWWN为20:36:44:78:66:77:ab:9e的FCF交换机在FC1/0/1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 swwn 20:36:44:78:66:77:ab:9e interface fc 1/0/1

\# VSAN 2中配置允许SWWN为20:36:44:78:66:77:ab:9e的FCF交换机在VFC1接口登录。

\<Sysname\> system-view

Sysname vsan 2

Sysname-vsan2 swwn 20:36:44:78:66:77:ab:9e interface vfc 1

【相关命令】

·**display** **fc-port-security** **database**

**FC和FCoE \-- FCS配置命令 \-- fcs discovery start**

------------------------------------------------------------------------

**[fcs discovery start**]命令用来发起拓扑发现。

【命令】

**[fcs discovery start ** **age** *interval* ] **vsan** *vsan-list*

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[age ***interval*]：拓扑发现数据的老化时间。*interval*的取值范围为300～86400，单位为秒，缺省值为900秒。

**[vsan** *vsan-list*]：VSAN列表，表示发起拓扑发现的VSAN范围。表示方式为*vsan-list* = *vsan-id* [ **to** *vsan-id* ]，*vsan-id*为VSAN的编号，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 在VSAN 1～VSAN 100内发起拓扑发现。

\<Sysname\> system-view

Sysname fcs discovery start vsan 1 to 100

【相关命令】

·**display fcs discovery status**

·**display fcs database**

·**display fcs ie**

·**display fcs port**

**FC和FCoE \-- FCS配置命令 \-- fcs discovery stop**

------------------------------------------------------------------------

**[fcs discovery stop**]命令用来取消拓扑发现。

【命令】

**[fcs discovery stop vsan ***vsan-list*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsan** *vsan-list*]：VSAN列表，表示取消拓扑发现的VSAN范围。表示方式为*vsan-list* = *vsan-id* [ **to** *vsan-id* ]，*vsan-id*为VSAN的编号，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 在VSAN 1～VSAN 100内取消拓扑发现。

\<Sysname\> system-view

Sysname fcs discovery stop vsan 1 to 100

【相关命令】

·**fcs discovery start**

**FC和FCoE \-- FCS配置命令 \-- display fcs discovery status**

------------------------------------------------------------------------

**[display fcs discovery status**]命令用来显示当前的拓扑发现状态。

【命令】

**[display fcs discovery status** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的拓扑发现状态，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的拓扑发现状态。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示所有VSAN 内的拓扑发现状态。

\<Sysname\> display fcs discovery status

VSAN    Discovery Status

1       inProgress

2       completed

3       localOnly

表1-58 display fcs discovery status命令显示信息描述表

字段

描述

VSAN

VSAN编号

Discovery Status

VSAN内的拓扑发现状态，包括：

·localOnly：表示未进行拓扑发现

·inProgress：表示正在进行拓扑发现

·completed：表示已完成拓扑发现

【相关命令】

·**fcs discovery start**

·**fcs discovery stop**

**FC和FCoE \-- FCS配置命令 \-- display fcs database**

------------------------------------------------------------------------

**[display fcs database**]命令用来显示FCS数据库信息。

【命令】

**[display fcs database** [ **vsan** *vsan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的FCS数据库信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的FCS数据库信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看本地FCS数据库信息，包括IE信息和端口信息。

【举例】

\# 显示所有VSAN内的FCS数据库信息。

\<Sysname\> display fcs database

FCS Local Database in VSAN 1:

  IE WWN                   : 10:00:00:11:22:00:01:01

  Domain ID                : 0x01

  Management address list  : snmp://192.168.6.100

                             snmp://192.168.0.100

  Fabric name              : 10:00:00:11:22:00:01:01

  Logical name             : IE-Sysname1

  Information list         : xxx, Inc.#DS-A8263-M5#1.3(2a)

  IE ports:

    Interface   Port WWN                  Port type  Attached port WWNs

    Fc1/0/2     2f:15:01:11:22:00:01:01   F_Port       2f:15:01:11:22:00:01:02

                                                     2f:15:01:11:22:00:01:03

                                                     2f:15:01:11:22:00:01:04

    Fc1/0/1     38:00:00:11:22:00:01:01   E_Port     38:00:00:11:22:00:01:02

  IE WWN                   : 10:00:00:11:22:00:01:02

  Domain ID                : 0x02

  Management address list  : snmp://192.168.6.101

  Fabric name              : 10:00:00:11:22:00:01:01

  Logical name             : IE-Sysname2

  Information list         : xxx, Inc.#DS-A8263-M5#1.3(2a)

  IE ports:

    Interface   Port WWN                  Port type  Attached port WWNs

    -           2f:15:01:11:22:00:01:01   F_Port       2f:15:01:11:22:00:01:02

    -           38:00:00:11:22:00:01:01   E_Port       38:00:00:11:22:00:01:02

FCS Local Database in VSAN 2:

  IE WWN                   : 10:00:00:11:22:00:01:01

  Domain ID                : 0x01

  Management address list  : snmp://192.168.6.100

                             snmp://192.168.0.100

  Fabric name              : 10:00:00:11:22:00:01:01

  Logical name             : IE-Sysname

  Information list         : xxx, Inc.#DS-A8263-M5#1.3(2a)

  IE ports:

    Interface    Port WWN                  Port type  Attached port WWNs

表1-59 display fcs database命令显示信息描述表

字段

描述

FCS Local Database in VSAN

指定VSAN内的FCS数据库信息

IE WWN

IE的WWN

Domain ID

IE的域ID

Management addresss list

IE的管理地址列表，其中snmp://192.168.6.100，表示支持SNMP管理协议，管理IP地址为192.168.6.100。Unknown表示未从对应IE获取管理地址，NA表示未配置管理地址

Fabric name

VSAN内IE所在Fabric网络的名称，Unknown表示未从对应IE获取Fabric网络名称

Logical name

IE的设备名称，Unknown表示未从对应IE获取设备名称

Information list

IE的信息列表：厂商名称\#产品名称/编号\#发布编码。Unknown表示未从对应IE获取信息列表

IE ports

IE上的端口信息

Interface

接口名称（只有本地交换机对应IE下的接口显示实际接口名称，其它IE下的接口显示为"-"）

Port WWN

端口的WWN

Port type

端口的模式，包括：

·E_Port：表示E端口

·F_Port：表示F端口

·Unknown：表示非以上模式

Attached port WWNs

端口所连接的端口的WWN，NA表示端口未与其它端口连接

【相关命令】

·**fcs discovery start**

**FC和FCoE \-- FCS配置命令 \-- display fcs ie**

------------------------------------------------------------------------

**[display fcs ie**]命令用来显示FCS的IE信息。

【命令】

**[display fcs ie** [ **vsan** *vsan-id* [ **nwwn** *wwn*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的IE信息。*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的IE信息。

**[nwwn ***wwn*]：显示指定WWN的IE信息。*wwn*格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。不指定该参数时，将显示指定VSAN内所有IE的信息。

**[verbose**]：显示IE的详细信息。不指定该参数时，将显示IE的简要信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示所有VSAN内的IE信息。

\<Sysname\> display fcs ie

IE List for VSAN 1:

  IE WWN                   Domain ID   Mgmt addr list           Logical name

  10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100     Sysname

                                       snmp://192.168.0.100

  10:00:00:11:22:00:01:02  0x02        snmp://192.168.6.101     Sysname

  Total 2 IEs in Fabric.

IE List for VSAN 2:

  IE WWN                   Domain ID   Mgmt addr list           Logical name

  10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100     Sysname

  Total 1 IEs in Fabric.

\# 显示VSAN 1内的IE信息。

\<Sysname\> display fcs ie vsan 1

IE List for VSAN 1:

  IE WWN                   Domain ID   Mgmt addr list           Logical name

  10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100     Sysname

                                       snmp://192.168.0.100

  10:00:00:11:22:00:01:02  0x02        snmp://192.168.6.101     Sysname

  Total 2 IEs in Fabric.

\# 显示VSAN 1内的NWWN为10:00:00:11:22:00:01:01的IE的简要信息。

\<Sysname\> display fcs ie vsan 1 nwwn 10:00:00:11:22:00:01:01

IE WWN                   Domain ID   Mgmt addr list            Logical name

10:00:00:11:22:00:01:01  0x01        snmp://192.168.6.100      Sysname

                                     snmp://192.168.0.100

\# 显示VSAN 1内的NWWN为10:00:00:11:22:00:01:01的IE的详细信息。

\<Sysname\> display fcs ie vsan 1 nwwn 10:00:00:11:22:00:01:01 verbose

IE Attributes:

  IE WWN                 : 10:00:00:11:22:00:01:01

  IE type                : Switch

  Domain ID              : 0x01

  Fabric name            : 10:00:00:11:22:00:01:01

  Logical name           : Sysname

  Management address list: snmp://192.168.6.100

                           snmp://192.168.0.100

  Information list       :

    Vendor name      : abc, Inc.

    Model name/number: DS-A8263-M5

    Release code     : 1.3(2a)

\# 显示所有VSAN内的IE的详细信息。

\<Sysname\> display fcs ie verbose

IE List for VSAN 1:

  IE Attributes:

    IE WWN                 : 10:00:00:11:22:00:01:01

    IE type                : Switch

    Domain ID              : 0x01

    Fabric name            : 10:00:00:11:22:00:01:01

    Logical name           : Sysname

    Management address list: snmp://192.168.6.100

                             snmp://192.168.0.100

    Information list       :

      Vendor name      : abc, Inc.

      Model name/number: DS-A8263-M5

      Release code     : 1.3(2a)

  Total 1 IEs in Fabric.

IE List for VSAN 2:

  IE Attributes:

    IE WWN                 : 10:00:00:11:22:00:01:01

    IE type                : Switch

    Domain ID              : 0x01

    Fabric name            : 10:00:00:11:22:00:01:01

    Logical name           : Sysname

    Management address list: snmp://192.168.6.100

                             snmp://192.168.0.100

    Information list       :

      Vendor name      : abc, Inc.

      Model name/number: DS-A8263-M5

      Release code     : 1.3(2a)

  Total 1 IEs in Fabric.

表1-60 display fcs ie命令显示信息描述表

字段

描述

IE List for VSAN

指定VSAN内的IE信息

IE Attributes

IE的属性

IE WWN

IE的WWN

IE type

IE的类型，包括：

·Switch：表示交换机

·Unknown：表示非交换机

Domain ID

IE的域ID

Fabric name

IE所在Fabric网络的名称，Unknown表示未从对应IE获取Fabric网络名称

Logical name

IE的设备名称，Unknown表示未从对应IE获取设备名称

Mgmt addr list

Management address list

IE的管理服务地址列表，其中snmp://192.168.6.100，表示支持SNMP管理协议，管理地址为192.168.6.100。Unknown表示未从对应IE获取管理地址，NA表示未配置管理地址

Information list

IE信息列表，Unknown表示未从对应IE获取信息列表

Vendor name

厂商名称

Model name/number

产品名称/编号

Release code

发布编码

Total 2 IEs in Fabric

显示Fabric中IE的个数

【相关命令】

·**fcs discovery start**

**FC和FCoE \-- FCS配置命令 \-- display fcs port**

------------------------------------------------------------------------

**[display fcs port**]命令用来显示FCS的端口信息。

【命令】

**[display fcs port**  **vsan** *vsan-id* [ **pwwn** *wwn*  ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan ***vsan-id*]：显示指定VSAN内的端口信息。*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的端口信息。

**[pwwn ***wwn*]：显示指定WWN的端口信息。*wwn*格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。不指定该参数时，将显示指定VSAN内所有端口的信息。

**[verbose**]：显示端口的详细信息。不指定该参数时，将显示端口的简要信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 显示所有VSAN内的端口信息。

\<Sysname\> display fcs port

Port List for VSAN 1:

  IE WWN: 10:00:00:11:22:00:01:01

    Port WWN                  Port type    Tx type             Module type

    2f:15:01:11:22:00:01:01   Unknown      Shortwave Laser     SFP with Serial ID

    38:00:00:11:22:00:01:01   E_Port       Shortwave Laser     SFP with Serial ID

    Total 2 switch-ports in IE.

  IE WWN: 10:00:00:11:22:00:01:02

    Port WWN                  Port type    Tx type             Module type

    38:00:00:11:22:00:01:02   E_Port       Shortwave Laser     SFP with Serial ID

    Total 1 switch-ports in IE.

Port List for VSAN 2:

  IE WWN: 10:00:00:11:22:00:01:01

    Port WWN                  Port type    Tx type             Module type

    2f:15:01:11:22:00:01:01   Unknown      Shortwave Laser     SFP with Serial ID

    38:00:00:11:22:00:01:01   E_Port       Shortwave Laser     SFP with Serial ID

    Total 2 switch-ports in IE.

\# 显示VSAN 1内的WWN为38:00:00:11:22:00:01:01的端口的简要信息。

\<Sysname\> display fcs port vsan 1 pwwn 38:00:00:11:22:00:01:01

Port WWN                  Port type    Tx type             Module type

38:00:00:11:22:00:01:01   E_Port       Shortwave Laser     SFP with Serial ID

\# 显示VSAN 1内的WWN为38:00:00:11:22:00:01:01的端口的详细信息。

\<Sysname\> display fcs port vsan 1 pwwn 38:00:00:11:22:00:01:01 verbose

Port Attributes:

  Port WWN                         : 38:00:00:11:22:00:01:01

  Port type                        : E_Port

  Tx type                          : Shortwave Laser

  Module type                      : SFP with Serial ID

  Port number                      : 465

  Attached port WWNs               : 2f:15:01:11:22:00:01:02

  Port state                       : Offline

  Port speed capability            : 10Gbps, 16Gbps

  Port speed operation             : 10Gbps

  Port zoning enforcement status   : Soft, Hard

表1-61 display fcs port命令显示信息描述表

字段

描述

Port List for VSAN

指定VSAN内的端口信息

IE WWN

IE的WWN

Port Attributes

端口的属性

Port WWN

端口的WWN

Port type

端口的模式，包括：

·E_Port：表示E端口

·F_Port：表示F端口

·Unknown：表示非以上模式

Tx type

端口的传输类型，包括：Long wave laser-LL(1550nm)、Short wave laser-SN(850nm)、Long wave laser cost reduced-LC(1310nm)、Electrical-EL、10GBASE-SR 850nm laser、10GBASE-LR 1310nm laser、10GBASE-ER 1550nm laser、10GBASE-LX4 WWDM 1300nm laser、10GBASE-SW 850nm laser、10GBASE-LW 1310nm laser、10GBASE-EW 1550nm laser和10GBASE-CX4。非以上类型则显示Unknown

Module type

端口采用的光模块类型，包括：GLM、GBIC with serial ID、GBIC without serial ID、SFP with serial ID、SFP without serial ID、XFP、X2 short、X2 Medium、X2 Tall、XPAX short、XPAX Medium、XPAX Tall、XENPAK、SFP-DWDM、QSFP和X2-DWDM。非以上类型则显示Other，获取不到光模块的类型则显示Unknown

Port number

端口的索引值

Attached port WWNs

所连接的端口的WWN。当不存在连接的端口WWN时，显示NA

Port state

端口当前状态，包括：

·Online：表示端口链路已连接

·Offline：表示端口链路未连接

·Unknown：表示非以上类型

Port speed capability

端口支持的所有速率，速率包括：1Gbps、2Gbps、4Gbps、8Gbps、10Gbps、16Gbps和20Gbps（可包含其中一项或多项）。非以上速率则显示Unknown

Port speed operation

端口当前的运行速率，运行速率包括：1Gbps、2Gbps、4Gbps、8Gbps、10Gbps、16Gbps和20Gbps（只可包含其中一项）。非以上速率则显示Unknown

端口当前状态为Offline时，端口运行速率显示为Speed not established

Port zoning enforcement status

端口当前支持的Zone类型：Soft表示软件Zone；Hard表示硬件Zone。可以同时支持两种，以上两种均不支持则显示NA

Total xx switch-ports in IE

IE的端口个数

【相关命令】

·**fcs discovery start**

**FC和FCoE \-- FDMI配置命令 \-- display fdmi database**

------------------------------------------------------------------------

**[display fdmi database**]命令用来显示FDMI数据库信息。

【命令】

**[display** **fdmi** **database** [ **vsan** *vsan-id* [ **hba-id** *hba-id*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsan** *vsan-id*]：显示指定VSAN内的FDMI数据库信息，*vsan-id*的取值范围为1～3839。不指定该参数时，将显示所有VSAN内的FDMI数据库信息。

**[hba-id** *hba-id*]：显示指定HBA ID的FDMI数据库信息。*hba-id*的格式为xx:xx:xx:xx:xx:xx:xx:xx，其中x为16进制数字。

**[verbose**]：显示FDMI数据库的详细信息。不指定该参数时，将显示FDMI数据库的简要信息。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

使用本命令可以查看FDMI数据库信息，包括整个Fabric网络中所有已经注册节点设备上的HBA信息。

【举例】

\# 显示所有VSAN内的FDMI数据库的简要信息。

\<Sysname\> display fdmi database

Registered HBA List for VSAN 1:

  HBA ID                        Port WWNs

  21:00:00:11:22:00:01:02       21:00:00:11:22:00:01:02

                                21:00:00:c0:dd:13:cc:d6

                                21:00:00:c0:dd:13:cc:d7

  38:00:00:11:22:00:01:01       21:00:00:c0:dd:13:cc:d4

                                21:00:00:c0:dd:13:cc:d5

                                38:00:00:11:22:00:01:01

Registered HBA List for VSAN 2:

  HBA ID                        Port WWNs

  38:00:00:11:22:00:01:01       21:00:00:c0:dd:13:cc:d4

                                21:00:00:c0:dd:13:cc:d5

                                38:00:00:11:22:00:01:01

\# 显示VSAN 1内的FDMI数据库内指定HBA的简要信息。

\<Sysname\> display fdmi database vsan 1 hba-id 38:00:00:11:22:00:01:01

  HBA ID                        Port WWNs

  38:00:00:11:22:00:01:01       21:00:00:c0:dd:13:cc:d4

                                21:00:00:c0:dd:13:cc:d5

                                38:00:00:11:22:00:01:01

\# 显示VSAN 1内的FDMI数据库的详细信息。

\<Sysname\> display fdmi database vsan 1 verbose

Registered HBA List for VSAN 1:

  HBA ID: 38:00:00:11:22:00:01:01

    Node WWN: 20:00:00:c0:dd:13:cc:d5

    Manufacturer: QLogic Corporation

    Serial num: RFC1001S63347

    Model: QLE8152

    Model description: QLogic QLE8152 Fibre Channel Adapter

    Hardware version: 2.1

    Driver version: 9.1.9.17

    ROM version: 3.00

    Firmware version: 5.04.01

    OS name/version: Microsoft Windows Server 2003 R2 for x86

    CT payload len: 2112

      Port WWN: 21:00:00:c0:dd:13:cc:d5

        Supported FC4 types: FCP

        Supported speed: 10Gbps

        Current speed: 10Gbps

        Maximum frame size: 2048

        OS device name: S05131F

        Host name: S05131F

表1-62 display fdmi database命令显示信息描述表

字段

描述

Registered HBA List for VSAN

VSAN内的HBA列表

HBA ID

HBA的编号

Port WWNs

HBA上的端口的WWN

表1-63 display fdmi database verbose命令显示信息描述表

字段

描述

Registered HBA List for VSAN

VSAN内的HBA列表

HBA ID

HBA的编号

Node WWN

HBA所属N节点的WWN

Manufacturer

HBA制造商信息

Serial num

HBA序列号

Model

HBA型号

Model description

HBA型号描述

Hardware version

HBA的硬件版本号

Driver version

HBA的驱动程序版本号

ROM version

HBA的ROM版本号

Firmware version

HBA的固件版本号

OS name/version

HBA所在操作系统名称和版本号

CT payload len

HBA允许的CT负载的最大长度，包括CT类型报文的基本头和扩展头，但不包括FC头

Port WWN

HBA上的端口的WWN

Supported FC4 types

端口支持的FC4类型，包括：

·FCP：表示光纤通道协议

·IP：表示互联网协议

·LLC/SNAP：表示链路控制/子网访问协议

·SW_ILS：表示交换机Fabric网内部链接服务

·SNMP：表示简单网络管理协议

·GS3：表示通用服务3

·VI：表示接口虚拟化

·NPV：表示N端口虚拟化

Supported speed

端口支持的速率，包括：1Gbps、2Gbps、4Gbps、8Gbps、10Gbps、16Gbps、20Gbps、32Gbps、40Gbps（可包含其中一项或多项）。非以上速率则显示Unknown

如果不能确定端口支持的速率，则显示为Speed not established

Current speed

端口当前的速率，包括：1Gbps、2Gbps、4Gbps、8Gbps、10Gbps、16Gbps、20Gbps、32Gbps、40Gbps（只可包含其中一项）。非以上速率则显示Unknown

如果不能确定端口当前的速率，则显示为Speed not established

Maximum frame size

端口支持的最大帧大小

OS device name

端口所在操作系统的名称

Host name

端口所在N节点设备的名称

**FC和FCoE \-- FC Ping配置命令 \-- fcping**

------------------------------------------------------------------------

**[fcping**]命令用来检查指定目的地址是否可达，并输出相应的统计信息。

在执行命令过程中，键入\<Ctrl+C\>可终止FC Ping操作。

【命令】

**[fcping**[ [ **-c** *count* \| **-t** *timeout* ] \* **fcid** *fcid* **vsan** *vsan-id*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-c** *count*]：指定发送ECHO请求报文的个数，取值范围为0～2147483647，缺省值为5。其中，0表示连续发送直到用户手动停止。

**[-t** *timeout*]：指定ECHO回应报文的超时时间。发送ECHO请求报文*timeout*后还没有收到ECHO回应报文，源端则认为ECHO回应报文超时。*timeout*的取值范围为1～10，单位为秒，缺省值为5秒。

**[fcid*** fcid*]：目的地址。当目的端为N节点时，*fcid*的值就是该节点的FC地址。当目的端为交换机时，*fcid*为该交换机的域控制器地址FFFCxx，xx为目的交换机的域ID。例如：目的交换机的域ID为3，则域控制器地址为FFFC03。

**[vsan*** vsan-id*]：VSAN ID，取值范围为1～3839。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

【举例】

\# 检查VSAN 1内目的地址为FFFC02的设备是否可达。

\<Sysname\> fcping fcid fffc02 vsan 1

FCPING fcid 0xfffc02: 128 data bytes, press CTRL_C to break.

Reply from 0xfffc02: bytes = 128 time = 1.281 ms

Reply from 0xfffc02: bytes = 128 time = 0.890 ms

Reply from 0xfffc02: bytes = 128 time = 0.889 ms

Reply from 0xfffc02: bytes = 128 time = 0.892 ms

Reply from 0xfffc02: bytes = 128 time = 0.894 ms

\-\-- 0xfffc02 fcping statistics \-\--

5 packet(s) transmitted

5 packet(s) received

0.00% packet loss

round-trip min/avg/max = 0.889/0.969/1.281 ms

\# FC Ping时报文发送失败。

\<Sysname\> fcping fcid fffc01 vsan 1

FCPING fcid 0xfffc01: 128 data bytes, press CTRL_C to break.

fcping: sendto: No route to host

fcping: sendto: No route to host

fcping: sendto: \^C

\-\-- 0xfffc01 fcping statistics \-\--

3 packet(s) transmitted

0 packet(s) received

100.00% packet loss

表1-64 fcping命令显示信息描述表

字段

描述

FCPING fcid 0xfffc02

检查目的地址为FFFC02的设备是否可达

128 data bytes

每个ECHO请求报文中的数据字节数

press CTRL_C to break

在执行命令过程中，键入\<Ctrl+C\>可终止FC Ping操作

Reply from 0xfffc02: bytes = 128 time = 0.892 ms

收到目的地址为0xfffc02的设备回复的ECHO回应报文：

·bytes表示ECHO回应报文中的数据字节数

·time表示响应时间

Request time out

ECHO请求报文发送成功，超时时间内未收到ECHO回应报文

fcping: sendto: No route to host

ECHO请求报文发送失败

\-\-- 0xfffc02 fcping statistics \-\--

FC Ping操作中收发报文的统计结果

5 packet(s) transmitted

发送的ECHO请求报文数

5 packet(s) received

收到的ECHO回应报文数

0.00% packet loss

未收到ECHO回应报文的ECHO请求报文占发送的总ECHO请求报文的百分比

round-trip min/avg/max = 0.889/0.969/1.281 ms

响应时间的最小值、平均值和最大值，单位为毫秒

**FC和FCoE \-- FC Tracert配置命令 \-- fctracert**

------------------------------------------------------------------------

**[fctracert**]命令用来探测本端到目的端的双向路由信息，目的端可以为N节点或交换机。

【命令】

**[fctracert** [ **-t** *timeout*  **fcid** *fcid* **vsan** *vsan-id*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-t*** timeout*]：整个探测过程的超时时间，取值范围为1～10，单位为秒，缺省值为5秒。

**[fcid** *fcid*]：目的地址。当目的端为N节点时，*fcid*的值就是该节点的FC地址。当目的端为交换机时，*fcid*为该交换机的域控制器地址FFFCxx，xx为目的交换机的域ID。例如：目的交换机的域ID为3，则域控制器地址为FFFC03。

**[vsan** *vsan-id*]：指定所属VSAN，取值范围为1～3839。该VSAN必须已经存在。

【使用指导】

只有FCF交换机和FCF-NPV交换机支持本命令。

通过本命令可以获取本端到目的端的双向路由信息，包括从本端到目的端往返所经过的所有交换机的WWN和域控制器地址。设备支持往返两端双向的最大跳数为255。

在执行命令过程中，键入\<Ctrl+C\>可终止此次fctracert操作。

【举例】

\# 探测在VSAN 1内本端到FC地址为0xd70000的节点的双向路由信息。

\<Sysname\> fctracert fcid d70000 vsan 1

Route present for: 0xd70000, press CTRL_C to break.

20:00:00:0b:46:00:02:82(0xfffcd5)

20:00:00:05:30:00:18:db(0xfffcd7)

20:00:00:05:30:00:18:db(0xfffcd7)

20:00:00:0b:46:00:02:82(0xfffcd5)

Fctracert completed.

表1-65 fctracert命令显示信息描述表

字段

描述

Route present for

查看从当前设备到目的地址设备所经过的路径

press CTRL_C to break

在执行命令过程中，键入\<Ctrl+C\>可终止操作

20:00:00:0b:46:00:02:82

设备的WWN值

0xfffcd5

设备的域控制器地址FFFCxx，xx为交换机的域ID

Fctracert completed.

FC Tracert命令执行完成

Fctracert uncompleted.

FC Tracert命令执行未完成，原因如下：

·resource is not enough：资源不足

·max hops reached：已达到最大跳数

·fabric is being built：Fabric网络正在建立

·no route to destination port：没有到目的端的路由

·destination port is not in fabric：目的端不在该Fabric网络

·destination port and source port are not in the same zone：目的端与源端不在同一个Zone

Fctracert timeout.

探测超时

Service is unavailable.

FC Tracert服务未启动或者内部处理失败

