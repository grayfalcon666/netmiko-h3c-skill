
**L2TP \-- L2TP配置命令 \-- allow l2tp**

------------------------------------------------------------------------

**[allow l2tp**]命令用来配置LNS接受来自指定LAC的L2TP隧道建立请求，并指定建立L2TP隧道时使用的虚拟模板接口。

**[undo allow**]命令用来恢复缺省情况。

【命令】

**[allow l2tp virtual-template ***virtual-template-number* [ **remote** *remote-name*]**]

**[undo **]**allow**

【缺省情况】

LNS不接受任何LAC的L2TP隧道建立请求。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[virtual-template*** virtual-template-number*]：指定虚拟模板接口。其中，*virtual-template-number*为虚拟模板接口序号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。LNS根据虚拟模板接口下配置的参数，动态地创建VA（Virtual Access，虚拟访问）接口。不同的VA接口用来处理不同L2TP会话上的数据。

**[remote*** remote-name*]：指定发起L2TP隧道建立请求的对端（即LAC）。其中，*remote-name*表示隧道对端的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

本命令需要在LNS设备上执行，用来指定LNS可以接受来自哪些LAC的L2TP隧道建立请求。

在L2TP组1下，可以不指定隧道对端名称。即在L2TP组1下，本命令的格式为：**allow l2tp virtual-template** *virtual-template-number* [ **remote** *remote-name* ]。如果指定了隧道对端名称，则LNS只接受来自指定隧道对端的建立请求。如果不指定隧道对端名称，则LNS可以接受任何名称的隧道对端的建立请求，此时L2TP组1称为缺省L2TP组。

在其他L2TP组（非L2TP组1）下，必须指定隧道对端的名称。即在其他L2TP组下，本命令的格式为：**allow l2tp virtual-template ***virtual-template-number* **remote** *remote-name**。*

如果发起建立请求的隧道对端与某个L2TP组下配置的对端名称匹配，则LNS与该对端建立L2TP隧道时采用该L2TP组下配置的隧道参数（如隧道验证功能、流控功能等）。如果隧道对端不与任何L2TP组下配置的对端名称匹配，则存在缺省L2TP组时，LNS与该对端建立的L2TP隧道采用缺省L2TP组下配置的隧道参数，不存在缺省L2TP组时，LNS无法与该对端建立L2TP隧道。

如下情况下，建议用户在LNS上配置缺省L2TP组：

·某些LAC（如采用Windows 2000 beta 2版本的主机）发送的L2TP隧道建立请求中本端名称为空。为了接受这种不知名的对端发起的隧道建立请求，LNS上需要配置缺省L2TP组。

·LNS与多个LAC建立的L2TP隧道参数相同时，可以通过缺省L2TP组简化配置。

需要注意的是：

·只能在LNS模式的L2TP组下执行本命令。LAC模式的L2TP组下不支持本命令。

·执行本命令时要确保指定的隧道对端名称和LAC侧配置的隧道本端名称一致。

·如果在同一个L2TP组下重复执行本命令，则新的配置覆盖已有配置。

【举例】

\# 配置LNS接受名称为aaa的对端（LAC）发起的L2TP隧道建立请求，并指定建立L2TP隧道时使用的虚拟模板接口为Virtual-Template2。对于其他名称的对端，LNS接受L2TP隧道建立请求，L2TP隧道建立时使用的虚拟模板接口为Virtual-Template1。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lns

Sysname-l2tp1 allow l2tp virtual-template 1

Sysname-l2tp1 quit

Sysname l2tp-group 2 mode lns

Sysname-l2tp2 allow l2tp virtual-template 2 remote aaa

【相关命令】

·**tunnel name**

**L2TP \-- L2TP配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路的开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 设置虚拟PPP接口10的期望带宽为100kbit/s。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 bandwidth 100

**L2TP \-- L2TP配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将虚拟PPP接口10恢复为缺省配置。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 default

**L2TP \-- L2TP配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Virtual-PPP254 Interface。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置虚拟PPP接口10的描述信息为"virtual-interface"。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 description virtual-interface

**L2TP \-- L2TP配置命令 \-- display interface virtual-ppp**

------------------------------------------------------------------------

**[display interface virtual-ppp**]命令用来显示虚拟PPP接口的相关信息。

【命令】

**[display interface **** virtual-ppp** [ *interface-number*    **brief** [ **description** \| **down** ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定虚拟PPP接口的信息。*interface-number*表示虚拟PPP接口的编号，取值范围为0～255。

**[brief**]：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。

**[description**]：显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。

【使用指导】

执行本命令时，如果不指定**virtual-ppp**参数，则显示设备支持的所有接口的相关信息；如果指定**virtual-ppp**参数，不指定*interface-number*参数，则显示所有已创建的虚拟PPP接口的相关信息。

【举例】

\# 显示虚拟PPP接口10的详细信息。

\<Sysname\> display interface virtual-ppp 10

Virtual-PPP10

Current state: Administratively DOWN

Line protocol state: DOWN

Description: Virtual-PPP10 Interface

Bandwidth: 100000kbps

Maximum Transmit Unit: 1500

Hold timer: 10 seconds, retry times: 5

Internet Address is 10.0.0.1/24 Primary

Link layer protocol: PPP

LCP: initial

Physical: L2TP, baudrate: 100000000 bps

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 154 packets, 1880 bytes, 0 drops

Output: 155 packets, 1875 bytes, 0 drops

表1-1 display interface virtual-ppp命令显示信息描述表

字段

描述

Current state

接口当前的物理状态和管理状态，可能的取值及含义如下：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态，可能的状态及含义如下：

·UP：表示该接口的链路层协议状态为开启

·DOWN：表示该接口的链路层协议状态为关闭

·UP (spoofing)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立

Description

接口描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口的最大传输单元

Hold timer

当前接口发送keepalive报文的周期，单位为秒

retry times

在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路

Internet Address

虚拟PPP接口的IP地址。如果没有为虚拟PPP接口配置IP地址，则该字段显示为Internet protocol processing: disabled，表示不能处理IP报文

Primary表示该IP地址为接口的主IP地址

Link layer protocol

链路层封装的协议，取值为PPP

LCP

LCP（Link Control Protocol，链路控制协议）状态

Physical

接口的物理类型，取值为L2TP

baudrate

接口的波特率

Last clearing of counters: Never

最后一次清除接口统计信息的时间（Never表示未清除过接口的统计信息）

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

当前接口最近300秒内输入报文的平均速率

·bytes/sec表示平均每秒输入的字节数

·bits/sec表示平均每秒输入的比特数

·packets/sec表示平均每秒输入的包数

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

当前接口最近300秒内输出报文的平均速率

·bytes/sec表示平均每秒输出的字节数

·bits/sec表示平均每秒输出的比特数

·packets/sec表示平均每秒输出的包数

Input: 154 packets, 1880 bytes, 0 drops

总计输入的报文数，总计输入的字节，总计丢弃的输入报文数

Output: 155 packets, 1875 bytes, 0 drops

总计输出的报文数, 总计输出的字节，总计丢弃的输出报文数

\# 显示虚拟PPP接口10的概要信息。

\<Sysname\> display interface virtual-ppp 10 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

VPPP10               ADM  DOWN     10.0.0.1        Virtual-PPP10 Interface

\# 显示所有当前物理状态为down的虚拟PPP接口的信息以及down的原因。

\<Sysname\> display interface virtual-ppp brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

VPPP9                ADM  Administratively

VPPP10               ADM  Administratively

VPPP12               ADM  Administratively

\# 显示虚拟PPP接口10的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display inter Virtual-PPP 10 brief description

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

VPPP10               ADM  DOWN     10.0.0.1        Virtual-PPP10 Interface

表1-2 display interface virtual-ppp brief命令显示信息描述表

字段

描述

The brief information of interface(s) under route mode/Brief information on interface(s) under route mode

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack等接口会具有该属性

Interface

接口名称缩写

Link

接口物理连接状态，取值为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行{.TableTextChar}**undo shutdown**命令才能打开接口{.TableTextChar}

·Stby：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准

Protocol

接口数据链路层协议状态，取值为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack等接口会取该值

Main IP

接口主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为：

·Administratively：表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

·Not connected：表示没有物理连接，一般是因为L2TP协商失败，或者配置不充分未能触发L2TP协商

**L2TP \-- L2TP配置命令 \-- display l2tp session**

------------------------------------------------------------------------

**[display l2tp session**]命令用来显示L2TP会话的信息。

【命令】

**[display l2tp session** [ **statistics** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[statistics**]：显示L2TP会话的统计信息。

【举例】

\# 显示L2TP会话的统计信息。

\<Sysname\> display l2tp session statistics

Total number of sessions: 1

\# 显示L2TP会话的信息。

\<Sysname\> display l2tp session

LocalSID      RemoteSID      LocalTID      State

89            36245          10878         Established

表1-3 display l2tp session命令显示信息描述表

字段

描述

Total number of sessions

会话的数目

LocalSID

本端的会话ID

RemoteSID

对端的会话ID

LocalTID

本端的隧道ID

State

会话的状态，取值包括：

·Idle：空闲状态

·Wait-tunnel：等待建立隧道

·Wait-reply：等待ICRP报文

·Wait-connect：等待ICCN报文

·Established：会话成功建立

**L2TP \-- L2TP配置命令 \-- display l2tp tunnel**

------------------------------------------------------------------------

**[display l2tp tunnel**]命令用来显示L2TP隧道的信息。

【命令】

**[display l2tp tunnel** [ **statistics** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[statistics**]：显示L2TP隧道的统计信息。

【举例】

\# 显示L2TP隧道的统计信息。

\<Sysname\> display l2tp tunnel statistics

Total number of tunnels: 1

\# 显示L2TP隧道的信息。

\<Sysname\> display l2tp tunnel

LocalTID RemoteTID State         Sessions RemoteAddress    RemotePort RemoteName

10878    21        Established   1        20.1.1.2         1701       lns

表1-4 display l2tp tunnel命令显示信息描述表

字段

描述

Total number of tunnels

隧道的数目

LocalTID

本端的隧道ID

RemoteTID

对端的隧道ID

State

隧道的状态，取值包括：

·{.TableTextChar}Idle：空闲状态

·{.TableTextChar}Wait-reply：等待SCCRP报文

·{.TableTextChar}Wait-connect：等待SCCCN报文

·{.TableTextChar}Established：隧道成功建立

·Stopping：正在下线

Sessions

此隧道上的会话数目

RemoteAddress

对端的IP地址

RemotePort

对端L2TP使用的UDP端口号

RemoteName

隧道对端的名称

【相关命令】

·**reset l2tp tunnel**

**L2TP \-- L2TP配置命令 \-- display l2tp va-pool**

------------------------------------------------------------------------

**[display l2tp va-pool**]命令用来显示L2TP的VA池信息。

【命令】

**[display l2tp va-pool**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示L2TP的VA池信息。

\<Sysname\> display l2tp va-pool

VT interface          Size      Unused      State

Virtual-Template1     1000      900         Normal

表1-5 display l2tp va-pool命令显示信息描述表

字段

描述

VT interface

使用VA池的虚拟模板接口

Size

用户申请的VA池容量

Unused

VA池中可用的VA接口数量

State

VA池当前的状态，取值包括：

·Creating：表示正在创建VA池

·Destroying：表示正在删除VA池

·Normal：表示VA池已经创建完成

【相关命令】

·**l2tp virtual-template va-pool**

**L2TP \-- L2TP配置命令 \-- interface virtual-ppp**

------------------------------------------------------------------------

**[interface virtual-ppp**]命令用来创建虚拟PPP接口，并进入指定的虚拟PPP接口视图。如果指定的虚拟PPP接口已经创建，则该命令用来直接进入虚拟PPP接口视图。

**[undo interface virtual-ppp**]命令用来删除指定的虚拟PPP接口。

【命令】

**[interface virtual-ppp** *interface-number*]

**[undo interface virtual-ppp** *interface-number*]

【缺省情况】

设备上不存在任何虚拟PPP接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：虚拟PPP接口的编号，取值范围为0～255。

【使用指导】

配置LAC-Auto-Initiated模式的L2TP隧道时，需要在LAC端创建虚拟PPP接口。

【举例】

\# 创建虚拟PPP接口10，并进入虚拟PPP接口视图。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10

**L2TP \-- L2TP配置命令 \-- l2tp enable**

------------------------------------------------------------------------

**[l2tp enable**]命令用来开启L2TP功能。

**[undo l2tp enable**]命令用来关闭L2TP功能。

【命令】

**[l2tp enable**]

**[undo l2tp enable**]

【缺省情况】

L2TP功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有开启该功能后其他L2TP相关配置才能生效。

【举例】

\# 开启L2TP功能。

\<Sysname\> system-view

Sysname l2tp enable

**L2TP \-- L2TP配置命令 \-- l2tp tsa-id**

------------------------------------------------------------------------

**[l2tp tsa-id**]命令用来配置LTS设备的TSA ID，并开启LTS设备的L2TP环路检测功能。

**[undo l2tp tsa-id**]命令用来恢复缺省情况。

【命令】

**[l2tp tsa-id ***tsa-id*]

**[undo l2tp tsa-id**]

【缺省情况】

未指定LTS设备的TSA ID，且LTS设备的L2TP环路检测功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tsa-id*]：LTS设备的唯一标识，为1～64个字符的字符串，区分大小写。

【使用指导】

在L2TP隧道交换组网中，LTS通过ICRQ（Incoming Call Request，入呼叫请求）报文中的TSA（Tunnel Switching Aggregator，隧道交换聚合） ID AVP来避免环路。

LTS接收到ICRQ报文后，将报文中携带的所有TSA ID AVP中的TSA ID逐一与本地配置的TSA ID进行比较。如果TSA ID AVP中存在与本地相同的TSA ID，则表示存在环路，LTS立即拆除会话。否则，LTS将自己的TSA ID封装到新的TSA ID AVP中，LTS向它的下一跳LTS发送ICRQ报文时携带接收到的所有TSA ID AVP及本地封装的TSA ID AVP。

为不同LTS设备配置的TSA ID不能相同，否则会导致环路检测错误。

【举例】

\# 配置LTS设备的TSA ID为lts0，并开启LTS设备的L2TP环路检测功能。

\<Sysname\> system-view

Sysname l2tp tsa-id lts0

**L2TP \-- L2TP配置命令 \-- l2tp virtual-template va-pool**

------------------------------------------------------------------------

**[l2tp virtual-template va-pool**]命令用来配置VA池。

**[undo l2tp virtual-template va-pool**]命令用来删除VA池。

【命令】

**[l2tp virtual-template** *template-number* **va-pool** *va-volume*]

**[undo l2tp virtual-template** *template-number* **va-pool**]

【缺省情况】

设备上不存在任何VA池。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[virtual-template ***template-number*]：指定需要使用VA池的虚拟模板接口。该接口必须已经存在。

**[va-pool ***va-volume*]：指定需要创建的VA池的大小，取值范围为1～65534。

【使用指导】

LNS设备在用户上线创建会话时需要创建VA接口，用于和LAC交换数据。在用户下线后需要删除VA接口。由于创建/删除VA接口需要一定的时间，所以如果有大量用户上线/下线，L2TP连接的建立和拆除性能会受到影响。

VA池可以用来解决上述问题。VA池是在建立L2TP连接前事先创建的VA接口的集合。创建VA池后，当需要创建VA接口时，直接从VA池中获取一个VA接口，加快了L2TP连接的建立速度。当用户下线后，直接把VA接口放入VA池中，不需要删除VA接口，加快了L2TP连接的拆除速度。当VA池中的VA接口耗光后，仍需在建立L2TP连接时再创建VA接口，在用户下线后删除VA接口。

需要注意的是：

·每个虚拟模板接口只能关联一个VA池。如果想要修改使用的VA池的大小，只能先删除原来的配置，然后重新配置VA池。

·创建/删除VA池需要花费一定的时间，请用户耐心等待。在VA池创建/删除过程中（还没创建/删除完成）允许用户上线/下线，但正在创建/删除的VA池不生效。

·系统可能由于资源不足不能创建用户指定容量的VA池，用户可以通过**display l2tp va-pool**命令查看实际可用的VA池的容量以及VA池的状态。

·VA池会占用较多的系统内存，请用户根据实际情况创建大小合适的VA池。

·删除VA池时，如果已有在线用户使用该VA池中的VA接口，不会导致这些用户下线。

【举例】

\# 为虚拟模板2创建容量为1000的VA池。

\<Sysname\> system-view

Sysname l2tp virtual-template 2 va-pool 1000

【相关命令】

·**display l2tp va-pool**

**L2TP \-- L2TP配置命令 \-- l2tp-auto-client**

------------------------------------------------------------------------

**[l2tp-auto-client**]命令用来触发LAC自动建立L2TP隧道。

**[undo l2tp-auto-client**]命令用来拆除LAC自动建立的L2TP隧道。

【命令】

**[l2tp-auto-client l2tp-group ***group-number*]

**[undo l2tp-auto-client**]

【缺省情况】

LAC不会自动建立L2TP隧道。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[l2tp-group*** group-number*]：指定LAC采用特定L2TP组下配置的隧道参数建立L2TP隧道。*group-number*为L2TP组号，取值范围为1～65535。

【使用指导】

配置本命令时指定的L2TP组必须已经创建，并且L2TP组的模式必须是LAC。

触发LAC建立L2TP隧道后，该隧道将始终存在，直到通过**undo** **l2tp-auto-client**或**undo l2tp-group*** group-number*命令拆除该隧道。

【举例】

\# 触发LAC自动建立L2TP隧道，建立隧道时采用L2TP组10下配置的隧道参数。

\<Sysname\> system-view

Sysname interface virtual-ppp 1

Sysname-Virtual-PPP1 l2tp-auto-client l2tp-group 10

【相关命令】

·**l2tp-group**

**L2TP \-- L2TP配置命令 \-- l2tp-group**

------------------------------------------------------------------------

**[l2tp-group**]命令用来创建L2TP组，指定L2TP组的模式，并进入L2TP组视图。

**[undo l2tp-group**]命令用来删除L2TP组。

【命令】

**[l2tp-group**[ *group-number* [ **mode** { **lac** \| **lns** } ]]]

**[undo l2tp-group** *group-number*]

【缺省情况】

设备上不存在任何L2TP组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：L2TP组号，取值范围为1～65535。

**[mode**]：指定L2TP组的模式。

**[lac**]：LAC模式，表示设备可以作为L2TP隧道的LAC端向LNS发起隧道建立请求。

**[lns**]：LNS模式，表示设备可以作为L2TP隧道的LNS端接受来自LAC的隧道建立请求。

【使用指导】

通过本命令创建L2TP组时，必须携带**mode**关键字，指定L2TP组的模式。通过本命令进入已经创建的L2TP组视图时，不需要携带**mode**关键字。

在L2TP组视图下，可以配置L2TP隧道的参数，如隧道验证功能、流控功能等。

一台设备上可以同时存在LAC模式和LNS模式的L2TP组，且最多能够创建1000个L2TP组。

【举例】

\# 创建L2TP组2，指定L2TP组模式为LAC，并进入L2TP组视图。

\<Sysname\> system-view

Sysname l2tp-group 2 mode lac

Sysname-l2tp2

【相关命令】

·**allow l2tp**

·**lns-ip**

·**user**

**L2TP \-- L2TP配置命令 \-- lns-ip**

------------------------------------------------------------------------

**[lns-ip**]命令用来在LAC端配置LNS的IP地址。

**[undo** **lns-ip**]命令用来在LAC端删除LNS的IP地址。

【命令】

**[lns-ip **{ *ip-address* }&\<1-5\>]

**[undo lns-ip**]

【缺省情况】

没有在LAC端指定LNS的IP地址。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

{ *ip-address* }*&*\<1-5\>：LNS的IP地址，&\<1-5\>表示前面的参数最多可以输入5次。

【使用指导】

在建立L2TP隧道时，LAC将按照LNS的IP地址配置的先后顺序依次向每个LNS发送建立L2TP隧道的请求。LAC接收到某个LNS的接受应答后，该LNS就作为隧道的对端；否则，LAC向下一个LNS发起隧道建立请求。

需要注意的是：

·只能在LAC模式的L2TP组下执行本命令。LNS模式的L2TP组下不支持本命令。

·如果在同一个L2TP组下重复执行本命令，则新的配置覆盖已有配置。

【举例】

\# 在LAC端配置LNS的IP地址为202.1.1.1。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 lns-ip 202.1.1.1

**L2TP \-- L2TP配置命令 \-- mandatory-chap**

------------------------------------------------------------------------

**[mandatory-chap**]命令用来强制LNS重新对用户进行CHAP验证。

**[undo mandatory-chap**]命令用来恢复缺省情况。

【命令】

**[mandatory-chap**]

**[undo mandatory-chap**]

【缺省情况】

LNS不会重新对用户进行CHAP验证。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，LAC代替LNS对用户进行验证，并将用户的所有验证信息及LAC端本身配置的验证方式发送给LNS。LNS根据接收到的信息及LNS端配置的验证方式，判断用户是否合法。

为了增加安全性，可以执行**mandatory-chap**命令，强制在LAC代理验证成功后，LNS再次对用户进行CHAP验证。

执行**mandatory-chap**命令配置强制CHAP验证后，对于NAS-Initiated模式L2TP隧道的用户来说，会经过两次验证：一次是在NAS端的验证，另一次是在LNS端的验证。一些用户可能不支持进行第二次验证，这时，LNS端的CHAP重新验证会失败。在这种情况下，建议不要开启LNS的强制CHAP验证功能。

需要注意的是：

·只能在LNS模式的L2TP组下执行本命令。LAC模式的L2TP组下不支持本命令。

·本命令只对NAS-Initiated模式的L2TP隧道有效，对Client-Initiated模式和LAC-Auto-Initiated模式的L2TP隧道无效。

·**mandatory-lcp**命令的优先级高于本命令，即如果在L2TP组下同时执行了**mandatory-chap**命令和**mandatory-lcp**命令，则LNS与用户重新进行LCP协商。

【举例】

\# 强制LNS重新对用户进行CHAP验证。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lns

Sysname-l2tp1 mandatory-chap

【相关命令】

·**mandatory-lcp**

**L2TP \-- L2TP配置命令 \-- mandatory-lcp**

------------------------------------------------------------------------

**[mandatory-lcp**]命令用来强制LNS与用户重新进行LCP（Link Control Protocol，链路控制协议）协商。

**[undo mandatory-lcp**]命令用来恢复缺省情况。

【命令】

**[mandatory-lcp**]

**[undo mandatory-lcp**]

【缺省情况】

LNS不会与用户重新进行LCP协商。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，对于NAS-Initialized模式的L2TP隧道，用户先和LAC进行LCP协商。如果协商通过，则由LAC发起L2TP隧道建立请求，并把与用户协商时收集到的信息（包括验证信息）发送给LNS。LNS根据接收到的信息判断用户是否合法。LNS不会与用户重新进行LCP协商。

LAC与用户协商出来的LCP参数可能不是LNS期望的参数。此时，需要在LNS上执行**mandatory-lcp**命令，强制LNS与用户重新进行LCP协商，忽略LAC发送的信息。

如果一些PPP用户不支持LCP重新协商，则LCP重新协商过程会失败。在这种情况下，建议不要开启LNS的强制LCP重协商功能。

需要注意的是：

·只能在LNS模式的L2TP组下执行本命令。LAC模式的L2TP组下不支持本命令。

·本命令只对NAS-Initiated模式的L2TP隧道有效，对Client-Initiated模式和LAC-Auto-Initiated模式的隧道无效。

·本命令的优先级高于**mandatory-chap**命令，即如果在L2TP组下同时执行了**mandatory-chap**命令和**mandatory-lcp**命令，则LNS与用户重新进行LCP协商。

【举例】

\# 强制LNS与用户重新进行LCP协商。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lns

Sysname-l2tp1 mandatory-lcp

【相关命令】

·**mandatory-chap**

**L2TP \-- L2TP配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

虚拟PPP接口的MTU值为1500字节。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

需要注意的是，配置了**mtu**命令后需要执行命令**shutdown**和**undo shutdown**，这样该配置才能在接口上生效。

【举例】

\# 配置虚拟PPP接口10的MTU值为1400字节。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 mtu 1400

**L2TP \-- L2TP配置命令 \-- reset counters interface virtual-ppp**

------------------------------------------------------------------------

**[reset counters interface virtual-ppp**]命令用来清除虚拟PPP接口的统计信息。

【命令】

**[reset counters interface** [ **virtual-ppp** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：虚拟PPP接口的编号，取值范围为0～255。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**virtual-ppp**和*interface-number*，则清除所有接口的统计信息；

·如果指定**virtual-ppp**而不指定*interface-number*，则清除所有虚拟PPP接口的统计信息；

·如果同时指定**virtual-ppp**和*interface-number*，则清除指定虚拟PPP接口的统计信息。

【举例】

\# 清除虚拟PPP接口10的统计信息。

\<Sysname\> reset counters interface virtual-ppp 10

**L2TP \-- L2TP配置命令 \-- reset l2tp tunnel**

------------------------------------------------------------------------

**[reset l2tp tunnel**]命令用来断开指定的L2TP隧道，同时断开该隧道内的所有会话。

【命令】

**[reset l2tp tunnel**[ { **id** *tunnel-id* \| **name** *remote-name* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[id **]*tunnel-id*：断开隧道ID为指定值的L2TP隧道。*tunnel-id*为隧道ID，取值范围为1～65535。

**[name**]*remote-name*：断开与指定隧道对端之间的L2TP隧道。*remote-name*表示隧道对端的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

在用户数为零、网络发生故障等情况下，可以通过本命令强制断开指定的L2TP隧道。LAC和LNS任何一端都可主动发起断开L2TP隧道的请求。隧道断开后，该隧道上的所有L2TP会话也将被清除。

需要注意的是：

·强制断开一个L2TP隧道后，当对端用户再次呼入时，隧道可以重新建立。

·通过指定隧道的对端名称来确定需要断开的L2TP隧道时，如果没有符合条件的L2TP隧道存在，则对当前的L2TP隧道没有影响；如果有多个符合条件的L2TP隧道存在（同一个名称，不同IP地址），则断开所有符合条件的L2TP隧道。

【举例】

\# 断开对端名称为aaa的L2TP隧道，并断开该隧道内的所有会话。

\<Sysname\> reset l2tp tunnel name aaa

【相关命令】

·**display l2tp tunnel**

**L2TP \-- L2TP配置命令 \-- service**

------------------------------------------------------------------------

![说明](L2TP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[service**]命令用来指定虚拟PPP接口下流量的业务处理板。

**[undo service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[service slot*** slot-number*]

**[undo service slot**]

分布式设备－IRF模式：

**[service chassis ***chassis-number*** slot*** slot-number*]

**[undo service chassis**]

【缺省情况】

没有指定虚拟PPP接口下流量的业务处理板。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：指定单板所在的槽位号。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：指定设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

**[service**]命令仅对L2TP数据报文的处理产生影响，L2TP控制报文始终在主用主控板上处理，不受本命令的控制。

如果通过本命令指定了虚拟PPP接口下流量的业务处理板，则通过该接口转发的报文均在指定的单板/成员设备上进行封装和解封装处理。否则，由系统自动选择处理L2TP数据报文的单板/成员设备。

需要注意的是：

·通过**tunnel flow-control**命令为L2TP数据报文开启了流控功能时，需要在虚拟PPP接口下配置**service**命令。

·如果指定的业务处理板被拔出，则即使接口UP，流量也转发不通。重新插入该业务处理板后，流量可以恢复在指定板上进行封装和解封装处理。

【举例】

\# 指定在2号单板集中处理虚拟PPP接口10的流量。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 service slot 2

\# 指定在2号成员设备集中处理虚拟PPP接口的流量。（集中式IRF设备）

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 service slot 2

\# 指定在2号成员设备的2号单板集中处理虚拟PPP接口10的流量。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10service chassis2 slot 2

**L2TP \-- L2TP配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo** **shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于打开状态。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭虚拟PPP接口10。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 shutdown

**L2TP \-- L2TP配置命令 \-- source-ip**

------------------------------------------------------------------------

**[source-ip**]命令用来设置L2TP隧道的源端地址，即封装后L2TP隧道报文的源地址。

**[undo source-ip**]命令用来恢复缺省情况。

【命令】

**[source-ip** *ip-address*]

**[undo source-ip**]

【缺省情况】

L2TP隧道的源端地址为本端隧道出接口的IP地址。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[ip-address*]：L2TP隧道的源端IP地址。

【使用指导】

建议将L2TP隧道的源端地址配置为设备上某LoopBack接口的IP地址，以减小物理接口故障对L2TP业务造成的影响。

需要注意的是：

·只能在LAC模式的L2TP组下执行本命令。LNS模式的L2TP组下不支持本命令。

·在L2TP多机备份的情况下，如果L2TP组视图下同时配置了**tunnel vsrp source-ip**和**source-ip**命令，将使用**tunnel vsrp source-ip**命令指定的地址作为L2TP隧道的源端地址；如果L2TP组视图下配置了**source-ip**命令，没有配置**tunnel vsrp source-ip**命令，将会导致L2TP多机备份故障。关于L2TP多机备份的详细介绍请参见"可靠性配置指导"中的"多机备份"。

【举例】

\# 设置L2TP隧道的源端地址为2.2.2.2。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 source-ip 2.2.2.2

【相关命令】

·**tunnel vsrp source-ip**（可靠性命令参考/多机备份）

**L2TP \-- L2TP配置命令 \-- tunnel authentication**

------------------------------------------------------------------------

**[tunnel authentication**]命令用来开启L2TP隧道验证功能。

**[undo tunnel authentication**]命令用来关闭L2TP隧道验证功能。

【命令】

**[tunnel authentication**]

**[undo tunnel authentication**]

【缺省情况】

L2TP隧道验证功能处于开启状态。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

L2TP隧道验证功能用来防止本端设备与非法的对端设备建立L2TP隧道，提高网络的安全性。

如果LAC和LNS两端都开启了隧道验证功能，则两端密钥（通过**tunnel password**命令配置）不为空并且完全一致的情况下，二者之间才能成功建立L2TP隧道。

如果LAC和LNS中的一端开启了隧道验证功能，则另一端可不开启隧道验证功能，但需要两端密钥（通过**tunnel password**命令配置）不为空并且完全一致，二者之间才能成功建立L2TP隧道。

如果LAC和LNS两端都禁用隧道验证功能，则无论两端是否配置密钥、密钥是否相同，都不影响隧道建立。

需要注意的是：

·为了保证隧道安全，建议用户不要禁用隧道验证功能。

·如果用户需要修改隧道验证的密钥，请在隧道开始协商前进行，否则修改的密钥不生效。

【举例】

\# 开启L2TP隧道验证功能。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lns

Sysname-l2tp1 tunnel authentication

【相关命令】

·**tunnel password**

**L2TP \-- L2TP配置命令 \-- tunnel avp-hidden**

------------------------------------------------------------------------

**[tunnel avp-hidden**]命令用来配置隧道采用隐藏方式（即密文方式）传输AVP数据。

**[undo** **tunnel avp-hidden**]命令用来恢复缺省情况。

【命令】

**[tunnel avp-hidden**]

**[undo tunnel avp-hidden**]

【缺省情况】

隧道采用明文方式传输AVP数据。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

L2TP协议通过AVP（Attribute Value Pair，属性值对）来传输隧道协商参数、会话协商参数和用户认证信息等。如果用户不希望这些信息（如用户密码）被窃取，则可以使用本配置将AVP数据的传输方式配置为隐藏传输，即利用隧道验证密钥（通过**tunnel password**命令配置）对AVP数据进行加密传输。

需要注意的是：

·LAC和LNS模式的L2TP组下都可以执行本命令。但是，目前LNS模式的L2TP组下本命令不会生效。

·只有通过**tunnel authentication**命令开启隧道验证功能后，本命令才会生效。

【举例】

\# 配置AVP数据采用隐藏方式传输。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 tunnel avp-hidden

【相关命令】

·**tunnel authentication**

·**tunnel password**

**L2TP \-- L2TP配置命令 \-- tunnel flow-control**

------------------------------------------------------------------------

**[tunnel flow-control**]命令用来开启L2TP会话的流控功能。

**[undo tunnel flow-control**]命令用来关闭L2TP会话的流控功能。

【命令】

**[tunnel flow-control**]

**[undo tunnel flow-control**]

【缺省情况】

L2TP会话的流控功能处于关闭状态。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

L2TP会话的流控功能是指在L2TP会话上传递的报文中携带序列号，通过序列号检测是否存在丢包，并根据序列号对乱序报文进行排序。

L2TP会话的流控功能应用在L2TP数据报文的接收与发送过程中。

只要LAC和LNS中的一端开启了流控功能，二者之间建立的L2TP会话就支持流控功能。设备作为LAC时，L2TP会话建立后如果LNS上改变了流控功能的状态，则L2TP会话的流控功能状态随之改变。设备作为LNS时，L2TP会话建立后如果LAC上改变了流控功能的状态，则L2TP会话的流控功能状态不会随之改变。

【举例】

\# 开启L2TP会话的流控功能。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 tunnel flow-control

**L2TP \-- L2TP配置命令 \-- tunnel name**

------------------------------------------------------------------------

**[tunnel name**]命令用来配置隧道本端的名称。

**[undo tunnel name**]命令用来恢复缺省情况。

【命令】

**[tunnel name** *name*]

**[undo tunnel name**]

【缺省情况】

隧道本端的名称为设备的名称。设备名称的详细介绍，请参见"基础配置指导"中的"设备管理"。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[name*]：隧道本端的名称，为1～31个字符的字符串，区分大小写。

【举例】

\# 配置隧道本端的名称为itsme。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lns

Sysname-l2tp1 tunnel name itsme

【相关命令】

·**sysname**（基础配置命令参考/设备管理）

**L2TP \-- L2TP配置命令 \-- tunnel password**

------------------------------------------------------------------------

**[tunnel password**]命令用来配置隧道验证密钥。

**[undo tunnel password**]命令用来删除隧道验证密钥。

【命令】

**[tunnel password**[ { **cipher** \| **simple** } *password*]]

**[undo tunnel password**]

【缺省情况】

没有配置隧道验证密钥。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：以密文方式设置密钥。

**[simple**]：以明文方式设置密钥。

*[password*]：隧道验证密钥，区分大小写。如果是**cipher**方式，则*password*为1～53个字符的密文字符串；如果是**simple**方式，则*password*为1～16个字符的明文字符串。

【使用指导】

只有通过**tunnel authentication**命令开启隧道验证功能后，本命令才会生效。

以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。

【举例】

\# 以明文方式配置隧道验证密钥为yougotit。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 tunnel password simple yougotit

【相关命令】

·**tunnel authentication**

**L2TP \-- L2TP配置命令 \-- tunnel timer hello**

------------------------------------------------------------------------

**[tunnel timer hello**]命令用来配置隧道中Hello报文的发送时间间隔。

**[undo tunnel timer hello**]命令用来恢复缺省情况。

【命令】

**[tunnel timer hello** *hello-interval*]

**[undo tunnel timer hello**]

【缺省情况】

隧道中Hello报文的发送时间间隔为60秒。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hello-interval*]：Hello报文的发送时间间隔，取值范围为60～1000，单位为秒。

【使用指导】

LAC和LNS在没有L2TP报文发送时，按照本命令配置的时间间隔周期性发送Hello报文，以免LAC和LNS之间的L2TP隧道和会话在超时后被删除。

在LNS和LAC上，可以配置不同的Hello报文发送时间间隔。

【举例】

\# 配置隧道中Hello报文的发送时间间隔为90秒。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 tunnel timer hello 90

**L2TP \-- L2TP配置命令 \-- ip dscp**

------------------------------------------------------------------------

**[ip dscp**]命令用来配置隧道报文的DSCP（Differentiated Services Code Point，区分服务编码点）优先级。

**[undo ip dscp**]命令用来恢复缺省情况。

【命令】

**[ip dscp** *dscp-value*]

**[undo ip dscp**]

【缺省情况】

隧道报文的DSCP优先级为0。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：隧道报文的DSCP优先级，取值范围为0～63。

【使用指导】

DSCP携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定发送的L2TP隧道报文中携带的DSCP优先级的取值。

【举例】

\# 配置隧道报文的DSCP优先级为50。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 ip dscp 50

**L2TP \-- L2TP配置命令 \-- timer-hold**

------------------------------------------------------------------------

**[timer-hold**]命令用来配置接口发送keepalive报文的周期。

**[undo timer-hold**]命令用来恢复缺省情况。

【命令】

**[timer-hold** *seconds*]

**[undo timer-hold**]

【缺省情况】

接口发送keepalive报文的周期为10秒。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口发送keepalive报文的周期，取值范围为0～32767，单位为秒。

【使用指导】

虚拟PPP接口定期向对端发送keepalive报文。如果在一段时间内无法收到对端发来的keepalive报文，虚拟PPP接口的链路层会认为对端故障，上报链路层Down。可以通过**timer-hold**命令修改发送keepalive报文的时间间隔。

在速率非常低的链路上，参数*seconds*不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟keepalive报文的发送与接收。而接口如果在retry个（可以通过**timer-hold retry**命令修改该个数）keepalive周期之后仍然无法收到对端的keepalive报文，它就会认为链路发生故障。如果keepalive报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。

【举例】

\# 配置虚拟PPP接口10发送keepalive报文的周期为20秒。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 timer-hold 20

【相关命令】

·**timer-hold retry**

**L2TP \-- L2TP配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

**[timer-hold** **retry**]命令用来配置接口在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路。

**[undo timer-hold retry**]命令用来恢复缺省情况。

【命令】

**[timer-hold** **retry** *retry*]

**[undo timer-hold retry**]

【缺省情况】

接口在5个keepalive周期内没有收到keepalive报文的应答就拆除链路。

【视图】

虚拟PPP接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retry*]：接口在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路，取值范围为1～255。

【使用指导】

虚拟PPP接口定期向对端发送keepalive报文。如果在一段时间内无法收到对端发来的keepalive报文，虚拟PPP接口的链路层会认为对端故障，上报链路层Down。可以通过**timer-hold**命令修改发送keepalive报文的时间间隔。

在速率非常低的链路上，参数*seconds*不能配置过小。因为在低速链路上，大报文可能会需要很长的时间才能传送完毕，这样就会延迟keepalive报文的发送与接收。而接口如果在*retry*个（可以通过**timer-hold retry**命令修改该个数）keepalive周期之后仍然无法收到对端的keepalive报文，它就会认为链路发生故障。如果keepalive报文被延迟的时间超过接口的这个限制，链路就会被认为发生故障而被关闭。

【举例】

\# 配置虚拟PPP接口10在10个keepalive周期内没有收到keepalive报文的应答就拆除链路。

\<Sysname\> system-view

Sysname interface virtual-ppp 10

Sysname-Virtual-PPP10 timer-hold retry 10

【相关命令】

·**timer-hold**

**L2TP \-- L2TP配置命令 \-- user**

------------------------------------------------------------------------

**[user**]命令用来配置本端作为LAC端时向LNS发起隧道建立请求的触发条件。

**[undo** **user**]命令用来删除配置的触发条件。

【命令】

**[user**[ { **domain** *domain-name* \| **fullusername** *user-name* }]]

**[undo user**]

【缺省情况】

没有指定本端作为LAC端时向LNS发起隧道建立请求的触发条件。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain** *domain-name*]：指定接入用户的域名与配置的域名匹配时，LAC向LNS发起L2TP隧道建立请求。*domain-name*表示用户域名，为1～24个字符的字符串，不区分大小写。

**[fullusername** *user-name*]：指定接入用户的用户名与配置的完整用户名匹配时，LAC向LNS发起L2TP隧道建立请求。*user-name*表示完整的用户名，为1～255个字符的字符串，区分大小写。

【使用指导】

只有接入用户的域名或完整用户名符合本命令配置的触发条件时，LAC才会向对端LNS发送建立L2TP隧道的请求。

需要注意的是：

·只能在LAC模式的L2TP组下执行本命令。LNS模式的L2TP组下不支持本命令。

·如果在同一个L2TP组下重复执行本命令，则新的配置覆盖已有配置。

【举例】

\# 配置接入用户的完整用户名为test@aabbcc.net时，触发LAC向LNS发送L2TP隧道建立请求。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 user fullusername test@aabbcc.net

**L2TP \-- L2TP配置命令 \-- vpn-instance**

------------------------------------------------------------------------

**[vpn-instance**]命令用来配置隧道对端所属的VPN。

**[undo vpn-instance**]命令用来恢复缺省情况。

【命令】

**[vpn-instance** *vpn-instance-name*]

**[undo vpn-instance**]

【缺省情况】

隧道对端属于公网。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

通过本命令指定隧道对端所属的VPN后，设备将在指定的VPN内发送L2TP控制消息和数据消息，即在指定VPN内查找到达控制消息和数据消息目的地址的路由，根据指定VPN的路由转发控制消息和数据消息。

当L2TP隧道的一个端点位于某个VPN中时，需要在L2TP隧道的另一个端点上通过本命令指定隧道对端属于该VPN，以便正确地在L2TP隧道端点之间转发报文。

执行本命令时需要注意：

·隧道对端所属的VPN应该与本端设备连接L2TP隧道对端的物理接口所属的VPN（通过**ip binding vpn-instance**命令配置）相同。

·本命令中指定的VPN实例必须已经创建。

【举例】

\# 配置隧道对端所属的VPN为vpn1。

\<Sysname\>system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 vpn-instance vpn1

【相关命令】

·**ip vpn-instance**（MPLS命令参考/MPLS L3VPN）

·**ip binding vpn-instance**（MPLS命令参考/MPLS L3VPN）
