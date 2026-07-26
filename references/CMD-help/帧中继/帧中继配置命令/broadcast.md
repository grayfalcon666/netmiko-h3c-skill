
**帧中继 \-- 帧中继配置命令 \-- broadcast**

------------------------------------------------------------------------

**[broadcast**]命令用来配置帧中继虚电路的广播属性。

**[undo broadcast**]命令用来关闭帧中继虚电路的广播属性。

【命令】

**[broadcast**]

**[undo broadcast**]

【缺省情况】

静态配置的帧中继虚电路不具备广播属性，动态学习的帧中继虚电路具备广播属性。

【视图】

帧中继DLCI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果帧中继虚电路具备了广播属性，则所属接口上的广播或组播报文都要在该虚电路上发送一份。如果需要在静态配置的虚电路上发送广播或者组播报文，务必配置本命令。

【举例】

\# 打开DLCI为200的虚电路的广播属性。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr dlci 200

Sysname-Serial2/1/0-fr-dlci-200 broadcast

**帧中继 \-- 帧中继配置命令 \-- display fr compression iphc**

------------------------------------------------------------------------

**[display fr compression iphc**]命令用来显示帧中继IPHC压缩的统计信息。

【命令】

**[display fr compression iphc**  { **rtp** \| **tcp** } [ **interface** *interface-type interface-number* ] **dlci** *number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[rtp**]：显示IPHC RTP头压缩的统计信息。

**[tcp**]：显示IPHC TCP头压缩的统计信息。

**[interface**] *interface-type interface-number*：指定接口的类型和编号，可以指定主接口，也可以指定子接口。指定主接口时，将显示该主接口及其子接口的IPHC压缩的统计信息。指定子接口时，将只显示该子接口的IPHC压缩的统计信息。不指定接口时，将显示所有接口的IPHC压缩的统计信息。

**[dlci** *dlci-number*]：虚电路DLCI编号，取值范围为16～1007。指定虚电路时，必须首先指定接口。指定主接口和虚电路时，无论指定的虚电路在主接口上还是在子接口上，都会显示这个虚电路的IPHC压缩的统计信息；指定子接口和虚电路时，如果指定的虚电路在子接口上，将显示这个虚电路的IPHC压缩的统计信息，如果指定的虚电路在子接口所对应的主接口上，将不显示统计信息。不指定虚电路时，将显示指定接口下的所有虚电路的IPHC压缩的统计信息。

【使用指导】

帧中继IPHC压缩的统计信息是基于虚电路的。每个接口下会存在一个或多个虚电路。

【举例】

\# 显示Serial2/1/0接口下DLCI为17的虚电路的IPHC RTP头压缩的统计信息。

\<Sysname\> display fr compression iphc rtp interface serial 2/1/0 dlci 17

DLCI: 17, Serial2/1/0

  Received:

    Compressed/Error/Total: 0/0/0 packets

  Sent:

    Compressed/Total: 0/0 packets

    Sent/Saved/Total: 0/0/0 bytes

    Packet-based compression ratio： 0%

    Byte-based compression ratio： 0%

  Connections:

    Rx/Tx: 16/16

    Five-Minute-Miss: 0 (Misses/5Mins)

    Max-Miss: 0

\# 显示Serial2/1/0接口的IPHC TCP头压缩的统计信息。

\<Sysname\> display fr compression iphc tcp interface serial 2/1/0

DLCI: 16, Serial2/1/0

  Received:

    Compressed/Error/Total: 0/0/0 packets

  Sent:

    Compressed/Total: 0/0 packets

    Sent/Saved/Total: 0/0/0 bytes

    Packet-based compression ratio: 0%

    Byte-based compression ratio: 0%

  Connections:

    Rx/Tx: 16/16

    Five-Minute-Miss: 0 (Misses/5Mins)

    Max-Miss: 0

DLCI: 17, Serial2/1/0

  Received:

    Compressed/Error/Total: 0/0/0 packets

  Sent:

    Compressed/Total: 0/0 packets

    Sent/Saved/Total: 0/0/0 bytes

    Packet-based compression ratio: 0%

    Byte-based compression ratio: 0%

  Connections:

    Rx/Tx: 16/16

    Five-Minute-Miss: 0 (Misses/5Mins)

    Max-Miss: 0

表1-1 display fr compression iphc命令显示信息描述表

字段

描述

DLCI: 17, Serial2/1/0

虚电路编号，虚电路所在的接口

Received:

  Compressed/Error/Total: 0/0/0 packets

收到报文的统计信息：

·Compressed：被压缩的报文数

·Error：错误报文数

·Total：总的报文数

Sent:

  Compressed/Total: 0/0 packets

  Sent/Saved/Total: 0/0/0 bytes

  Packet-based compression ratio: 0%

  Byte-based compression ratio: 0%

发送报文的统计信息：

·Compressed：被压缩的报文数

·Total：总的报文数

·Sent：实际发送的字节数

·Saved：节省的字节数

·Total：在不压缩的情况下，需要发送的字节数

·Packet-based compression ratio：基于报文的压缩率，表示压缩的报文在总发送报文中的比率，即（Compressed÷Total）×100%

·Byte-based compression ratio：基于字节的压缩率，表示压缩后带宽节省的百分比，即（Saved÷Total）×100%

Connections：

  Rx/Tx

  Five-Minute-Miss: x (Misses/5Mins)

  Max-Miss: x

连接信息：

·Rx：作为接收方，可解压缩的连接数

·Tx：作为发送方，可压缩的连接数

·Five-Minute-Miss：最后5分钟内，查找表项失败的次数（系统每5分钟统计一次查找表项失败的次数，本字段显示的是最新一次统计的结果）

·Max-Miss：查找表项失败的最大次数（将每次统计的查找表项失败的次数进行比较，得到最大值在这个字段显示）

【相关命令】

·**fr compression iphc enable**

·**reset fr compression iphc**

**帧中继 \-- 帧中继配置命令 \-- display fr inarp-info**

------------------------------------------------------------------------

**[display fr inarp-info**]命令用来显示帧中继InARP报文统计信息。

【命令】

**[display fr inarp-info** [ **interface** *interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**] *interface-type interface-number*：指定接口的类型和编号，可以指定主接口，也可以指定子接口。指定主接口时，显示该主接口及子接口的帧中继InARP报文统计信息。指定子接口时，显示该子接口的帧中继InARP报文统计信息。不指定接口时，显示所有接口的帧中继InARP报文统计信息。

【使用指导】

帧中继InARP报文分为两种：InARP请求报文和InARP应答报文。根据本命令的输出信息，可以诊断InARP协议是否正常工作。

【举例】

\# 显示帧中继InARP报文统计信息。

\<Sysname\> display fr inarp-info

Frame relay InARP statistics for interface Serial2/1/0 (DTE)

  Recvd InARP request  Sent InARP reply  Sent InARP request  Recvd InARP reply

  0                    0                 1                   1

表1-2 display fr inarp-info命令显示信息描述表

字段

描述

Frame relay InARP statistics for interface Serial2/1/0 (DTE)

DTE接口Serial2/1/0的帧中继InARP报文统计信息

Recvd InARP request

接收的InARP请求报文

Sent InARP reply

发送的InARP应答报文

Sent InARP request

发送的InARP请求报文

Recvd InARP reply

接收的InARP应答报文

【相关命令】

·**fr inarp**

**帧中继 \-- 帧中继配置命令 \-- display fr lmi-info**

------------------------------------------------------------------------

**[display fr lmi-info**]命令用来显示LMI信息。

【命令】

**[display fr lmi-info ** **interface** *interface-type* *interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：指定接口的类型和编号，只能指定主接口，不能指定子接口。指定主接口时，显示该主接口的LMI信息。不指定主接口时，显示所有主接口的LMI信息。

【使用指导】

LMI协议用于维护当前帧中继链路，LMI协议报文包括状态请求报文和状态报文。根据这些显示信息，可以进行故障的诊断。

【举例】

\# 显示所有接口的LMI信息。

\<Sysname\> display fr lmi-info

Frame relay LMI information for interface Serial2/1/1 (DTE, Q933)

  T391DTE: 10 seconds, N391DTE: 6, N392DTE: 3, N393DTE: 4

  Sent status enquiry: 96, Received status: 85

  Status timeout: 3, Discarded messages: 3

Frame relay LMI information for interface Serial2/1/0 (DCE, Q933)

  T392DCE: 15 seconds, N392DCE: 3, N393DCE: 4

  Received status enquiry: 0, Sent status: 0

  Status enquiry timeout: 0, Discarded messages: 0

表1-3 display fr lmi-info命令显示信息描述表

字段

描述

Frame relay LMI information for interface Serial2/1/1 (DTE, Q933)

帧中继接口Serial2/1/1的终端类型为DTE，LMI协议类型为Q.933附录A标准

T391DTE: 10 seconds, N391DTE: 6, N392DTE: 3, N393DTE: 4

DTE方的T391定时器的参数值（单位为秒，T391定时器的值通过**timer-hold**命令配置）、N391参数值、N392参数值以及N393参数值

Sent status enquiry: 96, Received status: 85

接口发出的状态请求报文数以及接口接收的状态报文数

Status timeout: 3, Discarded messages: 3

状态报文超时的数目以及丢弃报文的数目

Frame relay LMI information for interface Serial2/1/0 (DCE, Q933)

帧中继接口Serial2/1/0的终端类型为DCE，LMI协议类型为Q.933附录A标准

T392DCE: 15 seconds, N392DCE: 3, N393DCE: 4

DCE方的T392参数值、N392参数值以及N393参数值

Received status enquiry: 0, Sent status: 0

接口接收的状态请求报文数以及接口发送的状态报文数

Status enquiry timeout: 0, Discarded messages : 0

状态请求报文超时的数目以及丢弃报文的数目

【相关命令】

·**fr lmi n391dte**

·**fr lmi n392dce**

·**fr lmi n392dte**

·**fr lmi n393dce**

·**fr lmi n393dte**

·**fr lmi t392dce**

·**fr lmi type**

·**timer-hold**

**帧中继 \-- 帧中继配置命令 \-- display fr map-info**

------------------------------------------------------------------------

**[display fr map-info**]命令用来显示帧中继地址映射表。

【命令】

**[display fr map-info ** **interface** *interface-type* *interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**] *interface-type interface-number*：指定接口的类型和编号，可以指定主接口，也可以指定子接口。指定主接口时，显示该主接口及子接口的帧中继地址映射表。指定子接口时，显示该子接口的帧中继地址映射表。不指定接口时，显示所有接口的帧中继地址映射表。

【使用指导】

通过本命令的显示信息可以查看用户配置的静态地址映射是否正确、动态地址映射是否工作正常等。

【举例】

\# 显示所有接口的帧中继地址映射表。

\<Sysname\> display fr map-info

Map information for interface Serial2/1/0 (DTE)

  DLCI: 100, IP InARP 100.100.1.1, Serial2/1/0

    Creation time: 2012/10/21 14:48:44, Status: Active

  DLCI: 200, IP InARP 100.100.1.1, Serial2/1/0

    Creation time: 2012/10/21 14:34:42, Status: Active

  DLCI: 300, IP 1.1.1.1, Serial2/1/0

    Creation time: 2012/10/21 15:03:35, Status: Active

表1-4 display fr map-info命令显示信息描述表

字段

描述

Map information for interface Serial2/1/0 (DTE)

显示接口的帧中继地址映射表信息，该接口工作在DTE方式

DLCI: 100, IP InARP 100.100.1.1, Serial2/1/0

DLCI为100的虚电路和对端IP地址100.100.1.1通过InARP协议建立地址映射，该虚电路配置在接口Serial2/1/0上（如果没有InARP关键字，表示是通过手工配置建立的静态地址映射）

Creation time: 2012/10/21 14:48:44

该映射创建的时间

Status: Active

该映射的状态，与映射的虚电路状态保持一致，取值可能为：

·Active：激活状态

·Inactvie：非激活状态

【相关命令】

·**fr inarp**

·**fr map ip**

**帧中继 \-- 帧中继配置命令 \-- display fr pvc-info**

------------------------------------------------------------------------

**[display fr pvc-info**]命令用来显示帧中继的永久虚电路状态和该虚电路收发数据的统计信息。

【命令】

**[display fr pvc-info** [ **interface** *interface-type* *interface-number*   **dlci** *dlci-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**] *interface-type interface-number*：指定接口的类型和编号，可以指定主接口，也可以指定子接口。指定主接口时，显示该主接口及子接口的永久虚电路信息。指定子接口时，显示该子接口的永久虚电路信息。不指定接口时，显示所有接口的永久虚电路信息。

**[dlci** *dlci-number*]：虚电路DLCI编号，取值范围为16～1007。指定虚电路时，显示该永久虚电路的详细信息，不指定虚电路时，显示永久虚电路的概要信息。详细信息相比概要信息增加了帧中继流量管理等信息，例如流量整形信息。

【举例】

\# 显示帧中继所有永久虚电路的状态和收发数据的简要统计信息。

\<Sysname\> display fr pvc-info

PVC information for interface Serial2/1/0 (DTE, physical UP)

  DLCI: 100, Type: Dynamic, Serial2/1/0

    Encapsulation: ietf, Broadcast

    Creation time: 2012/04/01 23:55:39, Status: Active

    Input: 0 packets, 0 bytes, 0 dropped

    Output: 0 packets, 0 bytes, 0 dropped

  DLCI: 102, Type: Static, Serial2/1/0.1

    Encapsulation: nonstandard

    Creation time: 2012/04/01 23:56:14, Status: Active

    Input: 0 packets, 0 bytes, 0 dropped

    Output: 0 packets, 0 bytes, 0 dropped

\# 显示指定永久虚电路的状态和收发数据的详细统计信息。

\<Sysname\> display fr pvc-info dlci 100

PVC information for interface Serial2/1/0 (DTE, physical UP)

  DLCI: 100, Type: Dynamic, Serial2/1/0

    Encapsulation: ietf, Broadcast

    Creation time: 2012/04/01 23:55:39, Status: Active

    Input: 0 packets, 0 bytes, 0 dropped

    Output: 0 packets, 0 bytes, 0 dropped

    Traffic shaping: Inactive

      CIR allow: 56000 bps

      Output: 0 packets, 0 bytes, 0 dropped

表1-5 display fr pvc-info命令显示信息描述表

字段

描述

PVC information for interface Serial2/1/0 (DTE, physical UP)

显示帧中继接口Serial2/1/0的PVC信息，该接口工作在DTE方式，物理层状态为Up

DLCI: 100, Type: Dynamic, Serial2/1/0

DLCI=100的PVC的类型为Dynamic，配置在接口Serial2/1/0上，PVC类型的取值可能为：

·Dynamic：通过LMI动态学习的PVC

·Static：静态配置的PVC，包括通过**fr map ip**或**fr dlci**配置的PVC

Encapsulation: ietf, Broadcast

封装格式为IETF，允许发送广播报文

Creation time: 2012/04/01 23:55:39, Status: Active

该PVC的创建时间以及PVC状态

PVC状态取值可能为：

·Active：激活状态

·Inactvie：非激活状态

Input: 0 packets, 0 bytes, 0 dropped

接收的报文数、字节数和丢弃报文数

Output: 0 packets, 0 bytes, 0 dropped

发送的报文数、字节数和丢弃报文数

Traffic shaping: Inactive

流量整形状态，状态取值可能为：

·Active：激活状态

·Inactive：非激活状态

CIR allow: 56000 bps

允许的承诺信息速率

Output: 0 packets, 0 bytes, 0 dropped

使能流量整形功能后的发送报文数、字节数和丢弃报文数

【相关命令】

·**broadcast**

·**fr dlci**

·**fr encapsulation**

·**fr map ip**

**帧中继 \-- 帧中继配置命令 \-- fr compression iphc enable**

------------------------------------------------------------------------

**[fr compression iphc enable**]命令用来开启帧中继IPHC压缩功能。

**[undo fr compression iphc enable**]命令用来关闭帧中继IPHC压缩功能。

【命令】

**[fr compression iphc enable** [ **nonstandard** ]]

**[undo fr compression iphc enable**]

【缺省情况】

帧中继IPHC压缩功能处于关闭状态。

【视图】

接口视图/帧中继DLCI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[nonstandard**]：非标准的兼容的封装格式。不指定本参数时，则按照标准格式进行报文封装。与友商设备互通时需要配置本参数。配置本参数后，仅支持RTP头压缩，不支持TCP头压缩。

【使用指导】

帧中继IPHC压缩分为如下两种：

·RTP头压缩：对报文中的RTP/UDP/IP头进行压缩。

·TCP头压缩：对报文中的TCP/IP头进行压缩。

开启帧中继IPHC压缩功能后，上述两种压缩功能都将启动；关闭帧中继IPHC压缩功能后，上述两种压缩功能都将被禁止。

需要注意的是：

·用户必须在链路的两端同时开启帧中继IPHC压缩功能，该功能才生效。

·用户可以在接口视图下和DLCI视图下配置本命令，接口视图下的配置对该接口下的所有虚电路生效，DLCI视图下的配置只对本虚电路生效。如果接口视图的配置与DLCI视图的配置不同，则以DLCI视图下的配置为准。

·当帧中继的封装格式为**ietf**时（通过命令**fr encapsulation**配置），开启IPHC压缩功能后会触发IPHC协商，协商成功后压缩功能才生效；当帧中继的封装格式为**nonstandard**时，开启IPHC压缩功能后不会触发IPHC协商，压缩功能直接生效，而且仅支持RTP头压缩，不支持TCP头压缩。此时，需要链路两端的封装格式都配置为**nonstandard**才能正常通信。

·关闭IPHC压缩功能时，不会立即停止压缩，需要在接口下或者虚电路所在的接口下执行**shutdown**与**undo shutdown**操作后，才会关闭压缩功能。

【举例】

\# 开启帧中继接口Serial2/1/0的IPHC压缩功能。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr compression iphc enable

\# 开启DLCI为100的帧中继虚电路的IPHC压缩功能。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr dlci 100

Sysname-fr-dlci-Serial2/1/0-100 fr compression iphc enable

【相关命令】

·**fr encapsulation**

**帧中继 \-- 帧中继配置命令 \-- fr compression iphc rtp-connections**

------------------------------------------------------------------------

**[fr compression iphc rtp-connections**]命令用来配置接口或虚电路上允许进行RTP头压缩的最大连接数。

**[undo fr compression iphc rtp-connections**]命令用来恢复缺省情况。

【命令】

**[fr compression iphc rtp-connections ***number*]

**[undo fr compression iphc rtp-connections**]

【缺省情况】

接口或虚电路上允许进行RTP头压缩的最大连接数为16。

【视图】

接口视图/帧中继DLCI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：每条虚电路上允许进行RTP头压缩的最大连接数，取值范围为3～1000。当*number*≤256时，报文将被压缩成COMPRESSED_RTP_8格式，当*number*＞256时，报文将被压缩成COMPRESSED_RTP_16格式。

【使用指导】

RTP（Real-time Transport Protocol，实时传输协议）是面向连接的协议，一条链路上所能承载的RTP连接的数目是比较多的，但压缩算法压缩时需对每个连接维护一定的信息，从而占用一定的内存，因此可以用**fr compression iphc rtp-connections**命令来配置RTP头压缩的最大连接数。例如最大连接数配置为3时，第4条RTP连接上的报文就不会被压缩了。

需要注意的是：

·如果在接口视图下配置了RTP头压缩的最大连接数，那么该接口下的所有虚电路都会继承这个最大连接数；如果在该接口下的某DLCI视图下配置了不同的最大连接数，那么以这个DLCI视图下的配置为准。

·只有在开启IPHC压缩功能后，才能配置本命令。在关闭IPHC压缩功能后，本配置将被清除。

·配置本功能后，需要在接口下或者虚电路所在的接口下执行**shutdown**与**undo shutdown**操作后，配置才能生效。

【举例】

\# 配置帧中继接口Serial2/1/0上允许进行RTP头压缩的最大连接数为200。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr compression iphc enable

Sysname-Serial2/1/0 fr compression iphc rtp-connections 200

\# 配置DLCI为100的帧中继虚电路上允许进行RTP头压缩的最大连接数为200。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr dlci 100

Sysname-fr-dlci-Serial2/1/0-100 fr compression iphc enable

Sysname-fr-dlci-Serial2/1/0-100fr compression iphc rtp-connections 200

【相关命令】

·**fr compression iphc enable**

**帧中继 \-- 帧中继配置命令 \-- fr compression iphc tcp-connections**

------------------------------------------------------------------------

**[fr compression iphc tcp-connections**]命令用来配置接口或虚电路上允许进行TCP头压缩的最大连接数。

**[undo fr compression iphc tcp-connections**]命令用来恢复缺省情况。

【命令】

**[fr compression iphc tcp-connections ***number*]

**[undo fr compression iphc tcp-connections**]

【缺省情况】

接口或虚电路上允许进行TCP头压缩的最大连接数为16。

【视图】

接口视图/帧中继DLCI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：每条虚电路上允许进行TCP头压缩的最大连接数，取值范围为3～256。

【使用指导】

TCP是面向连接的协议，一条链路上所能承载的TCP连接的数目是比较多的，但压缩算法压缩时需对每个连接维护一定的信息，从而占用一定的内存，因此可以用**fr compression iphc tcp-connections**命令来配置TCP头压缩的最大连接数。例如最大连接数配置为3时，第4条TCP连接上的报文就不会被压缩了。

需要注意的是：

·如果在接口视图下配置了TCP头压缩的最大连接数，那么该接口下的所有虚电路都会继承这个最大连接数；如果在该接口下的某DLCI视图下配置了不同的最大连接数，那么以这个DLCI视图下的配置为准。

·只有在开启IPHC压缩功能，且不指定**nonstandard**参数时，才能配置本命令。在关闭IPHC压缩功能或者更改配置为**nonstandard**模式后，本配置将被清除。

·配置本功能后，需要在接口下或者虚电路所在的接口下执行**shutdown**与**undo shutdown**操作后，配置才能生效。

【举例】

\# 配置帧中继接口Serial2/1/0上允许进行TCP头压缩的最大连接数为200。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr compression iphc enable

Sysname-Serial2/1/0 fr compression iphc tcp-connections 200

\# 配置DLCI为100的帧中继虚电路上允许进行TCP头压缩的最大连接数为200。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr dlci 100

Sysname-fr-dlci-Serial2/1/0-100 fr compression iphc enable

Sysname-fr-dlci-Serial2/1/0-100fr compression iphc tcp-connections 200

【相关命令】

·**fr compression iphc enable**

**帧中继 \-- 帧中继配置命令 \-- fr dlci**

------------------------------------------------------------------------

**[fr dlci**]命令用来为帧中继接口创建虚电路，并进入相应的帧中继虚电路视图。

**[undo fr dlci**]命令用来删除帧中继接口的虚电路。

【命令】

**[fr dlci** *dlci-number*]

**[undo** **fr dlci** [ *dlci-number* ]]

【缺省情况】

接口下不存在虚电路。

【视图】

接口视图（包括主接口和子接口）

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dlci-number*]：虚电路DLCI编号，取值范围为16～1007。DLCI号0～15、1008～1023为帧中继协议保留，供特殊使用。

【使用指导】

当帧中继接口类型是DCE或NNI时，需要为接口（不论是主接口还是子接口）手动创建虚电路。当帧中继接口类型是DTE时，如果接口是主接口，则系统会根据对端设备自动确定虚电路，也可以手工配置虚电路；如果是子接口，则必须手动为接口指定虚电路。

需要注意的是：

·虚电路号在一个主接口及其所有子接口上是唯一的。

·在配置**undo**命令时，如果不指定*dlci-number*，则删除帧中继接口上的所有虚电路。

·DCE接口和NNI接口在LMI协商过程中需要传递虚电路信息，如果接口上配置的虚电路个数太多，协商报文长度超过了接口最大帧长度的限制，会导致LMI协商不通过。接口最大帧长度与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 为帧中继接口Serial2/1/0创建一条DLCI为100的虚电路。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr dlci 100

Sysname-Serial2/1/0-fr-dlci-100

**帧中继 \-- 帧中继配置命令 \-- fr encapsulation**

------------------------------------------------------------------------

**[fr encapsulation**]命令用来配置帧中继接口或者虚电路的封装格式。

**[undo** **fr** **encapsulation**]命令用来恢复缺省情况。

【命令】

**[fr encapsulation**[ { **ietf** \| **nonstandard** }]]

**[undo** **fr** **encapsulation**]

【缺省情况】

帧中继接口的封装格式为IETF，帧中继虚电路采用接口配置的封装格式。

【视图】

接口视图/帧中继DLCI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ietf**]：IETF标准封装。

**[nonstandard**]：非标准兼容的封装格式。

【使用指导】

当封装接口链路层协议为帧中继时，可以选择IETF标准（**ietf**），按照RFC 1490规定的格式进行封装；也可以选择非标准兼容（**nonstandard**）的封装格式，它与业界主流路由器的专用封装格式是兼容的。

当帧中继接口封装为以上任何一种帧中继格式后，接口将按该格式发送报文，但接口可以识别和接收这两种报文，也就是说，即使对端设备封装的帧中继格式和本地不同，只要对端设备也支持这两种格式的自动识别，两端设备一样可以通信。但在对端设备不支持对这两种格式的自动识别时，应将两端设备的帧中继格式设为一致。

虚电路的封装格式以虚电路配置的封装格式优先，缺省时采用接口配置的封装格式，当虚电路配置封装格式后，虚电路按照该格式发送报文。

【举例】

\# 在接口Serial2/1/0上封装帧中继，并选择非标准兼容封装格式。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr encapsulation nonstandard

\# 配置DLCI为200的帧中继虚电路的封装格式为IETF标准封装。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr dlci 200

Sysname-Serial2/1/0-fr-dlci-200 fr encapsulation ietf

**帧中继 \-- 帧中继配置命令 \-- fr inarp**

------------------------------------------------------------------------

**[fr inarp**]命令用来使能帧中继InARP功能。

**[undo fr inarp**]命令用来关闭帧中继InARP功能。

【命令】

**[fr inarp** **ip** [ *dlci-number*  ]]

**[undo** **fr inarp** **ip** [ *dlci-number* ]]

【缺省情况】

帧中继InARP功能处于使能状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip**]：表示对IP地址进行逆向地址解析。

*[dlci-number*]：虚电路DLCI编号，表示只对该虚电路号进行逆向地址解析，取值范围为16～1007。

【使用指导】

帧中继在接口上发送数据时，需要进行对端IP地址与本地DLCI的映射，该映射可以由手工配置来指定，也可以通过启用InARP功能来自动完成。

需要注意的是：

·如果要使能或关闭接口上所有虚电路的InARP功能，则使用不带任何参数的该命令。如果要使能或关闭指定虚电路上的InARP功能，则使用带*dlci-number*参数的该命令。

·如果接口上（包括子接口）使能InARP功能，则接口下所有虚电路也使能此功能，此时可以用**undo fr inarp ip ***dlci-number*命令单独关闭某条虚电路上的InARP功能；如果用**undo fr inarp**关闭了某个接口的InARP功能，则接口下所有虚电路也关闭了此功能，此时可以使用**fr inarp ip ***dlci-number*命令在某条虚电路上使能InARP功能。

·在主接口下启动InARP功能对该主接口下的子接口同样生效。

【举例】

\# 在帧中继接口Serial2/1/0上的所有虚电路上都允许进行逆向地址解析。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr inarp ip

【相关命令】

·**display fr inarp-info**

·**fr inarp** **interval**

**帧中继 \-- 帧中继配置命令 \-- fr inarp interval**

------------------------------------------------------------------------

**[fr inarp interval**]命令用来配置InARP学习时的请求报文发送间隔时间。

**[undo fr inarp interval**]命令用来恢复缺省情况。

【命令】

**[fr inarp** **interval** *seconds*]

**[undo** **fr inarp** **interval**]

【缺省情况】

InARP学习时的请求报文发送间隔时间为60秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：InARP学习时的请求报文发送间隔时间，取值范围为15～300，单位为秒。

【使用指导】

InARP功能使能后，InARP学习时的请求报文发送间隔时间才能生效。

【举例】

\# 配置帧中继接口InARP学习时的请求报文发送间隔时间为15秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr inarp interval 15

【相关命令】

·**display fr inarp-info**

·**fr inarp**

**帧中继 \-- 帧中继配置命令 \-- fr interface-type**

------------------------------------------------------------------------

**[fr interface-type**]命令用来配置帧中继接口类型。

**[undo fr interface-type**]命令用来恢复缺省情况。

【命令】

**[fr interface-type****nni** }

**[undo fr interface-type**]

【缺省情况】]

帧中继接口类型为DTE。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dce**]：配置帧中继接口类型为DCE（Data Circuit-terminating Equipment，数据电路终接设备）。

**[dte**]：配置帧中继接口类型为DTE（Data Terminal Equipment，数据终端设备）。

**[nni**]：配置帧中继接口类型为NNI（Network-to-Network Interface，网间网接口）。

【举例】

\# 配置帧中继接口Serial2/1/0类型为DCE。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr interface-type dce

**帧中继 \-- 帧中继配置命令 \-- fr lmi n391dte**

------------------------------------------------------------------------

**[fr lmi n391dte**]命令用来配置DTE侧N391参数的值。

**[undo fr lmi n391dte**]命令用来恢复缺省情况。

【命令】

**[fr lmi n391dte*** n391-value*]

**[undo fr lmi n391dte**]

【缺省情况】

DTE侧N391参数的值为6。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[n391-value*]：计数器N391的值，取值范围为1～255。

【使用指导】

DTE设备每隔一定的时间（时间间隔由T391决定）要发送一个状态请求报文。状态请求报文有两种类型：链路完整性请求报文和全状态请求报文。参数N391定义两种报文的发送比例，即（全状态请求报文数：链路完整性请求报文数）=（1：N391-1）。

需要注意的是，配置本命令时，要求接口类型是DTE或者NNI。

【举例】

\# 配置帧中继接口Serial2/1/0工作在DTE方式，计数器N391的值为10。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr interface-type dte

Sysname-Serial2/1/0 fr lmi n391dte 10

**帧中继 \-- 帧中继配置命令 \-- fr lmi n392dce**

------------------------------------------------------------------------

**[fr** **lmi n392dce**]命令用来配置DCE侧N392参数的值。

**[undo fr lmi n392dce**]命令用来恢复缺省情况。

【命令】

**[fr lmi n392dce**] *n392-value*

**[undo fr lmi n392dce**]

【缺省情况】

DCE侧N392参数的值为3。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[n392-value*]：DCE侧N392参数的值，取值范围为1～10。

【使用指导】

DCE设备每隔一定的时间间隔（时间间隔由T392决定）要求DTE设备发送一个状态请求报文。在一定的时间内，如果DCE没有收到状态请求报文，DCE就记录该错误。如果错误次数超过门限，DCE设备就认为物理通路不可用，所有的虚电路都不可用。

N392和N393一起定义了"错误门限"。其中N393表示被观察的事件总数，N392表示在被观察的事件总数中发生错误的门限。也就是说，如果DCE设备在N393个事件中，发生错误次数达到N392，DCE设备就认为错误次数达到门限，由此认为物理通路不可用，所有的虚电路都不可用。

需要注意的是：

·DCE侧的N392参数值应小于DCE侧N393参数的值。

·配置本命令时，要求接口类型是DCE或者NNI。

【举例】

\# 配置帧中继接口Serial2/1/0工作在DCE方式，并配置N392和N393分别为5和6。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr interface-type dce

Sysname-Serial2/1/0 fr lmi n392dce 5

Sysname-Serial2/1/0 fr lmi n393dce 6

**帧中继 \-- 帧中继配置命令 \-- fr lmi n392dte**

------------------------------------------------------------------------

**[fr lmi n392dte**]命令用来配置DTE侧N392参数的值。

**[undo fr lmi n392dte**]命令用来恢复缺省情况。

【命令】

**[fr lmi n392dte*** n392-value*]

**[undo fr lmi n392dte**]

【缺省情况】

DTE侧N392参数的值为3。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[n392-value*]：DTE侧N392参数的值，取值范围为1～10。

【使用指导】

DTE设备每隔一定的时间要发送一个状态请求报文去查询链路状态，DCE设备收到该报文后立即发送状态报文。如果DTE设备在规定的时间内没有收到响应，就记录该错误。如果错误次数超过门限，DTE设备就认为物理通路不可用，所有的虚电路都不可用。

N392和N393两个参数一起定义了"错误门限"。其中N393表示被观察的事件总数，N392表示在被观察的事件总数中发生的错误门限。也就是说，如果DTE设备发送N393个状态请求报文中，如果发生错误数达到N392，DTE设备就认为错误次数达到门限，由此认为物理通路不可用，所有的虚电路都不可用。

需要注意的是：

·DTE侧的N392参数的值应小于DTE侧的N393参数的值。

·配置本命令时，要求接口类型是DTE或者NNI。

【举例】

\# 配置帧中继接口Serial2/1/0工作在DTE方式，并配置N392和N393为5和6。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr interface-type dte

Sysname-Serial2/1/0 fr lmi n392dte 5

Sysname-Serial2/1/0 fr lmi n393dte 6

**帧中继 \-- 帧中继配置命令 \-- fr lmi n393dce**

------------------------------------------------------------------------

**[fr lmi n393dce**]命令用来配置DCE侧N393参数的值。

**[undo fr lmi n393dce**]命令用来恢复缺省情况。

【命令】

**[fr lmi n393dce*** n393-value*]

**[undo fr lmi n393dce**]

【缺省情况】

DCE侧N393参数的值为4。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[n393-value*]：DCE侧N393参数的值，取值范围为1～10。

【使用指导】

DCE设备每隔一定的时间（时间间隔由T392决定）要求DTE设备发送一个状态请求报文。如果DCE在规定时间内没有收到状态请求报文，DCE就记录该错误。如果错误次数超过门限，DCE设备就认为物理通路不可用，所有的虚电路都不可用。

N392和N393一起定义了"错误门限"。其中N393表示被观察的总事件数，N392表示在被观察的总事件数中发生的错误门限。也就是说，如果DCE设备在N393个事件中，发生错误次数达到N392，DCE设备就认为错误次数达到门限，且认为物理通路不可用，所有的虚电路都不可用。

需要注意的是：

·DCE侧的N392参数的值应小于DCE侧的N393参数的值。

·配置本命令时，要求接口类型是DCE或者NNI。

【举例】

\# 配置帧中继接口Serial2/1/0工作在DCE方式，并配置N392和N393为5和6。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr interface-type dce

Sysname-Serial2/1/0 fr lmi n392dce 5

Sysname-Serial2/1/0 fr lmi n393dce 6

**帧中继 \-- 帧中继配置命令 \-- fr lmi n393dte**

------------------------------------------------------------------------

**[fr** **lmi n393dte**]命令用来配置DTE侧N393参数的值。

**[undo fr** **lmi n393dte**]命令用来恢复缺省情况。

【命令】

**[fr lmi n393dte** *n393-value*]

**[undo fr lmi n393dte**]

【缺省情况】

DTE侧N393参数的值为4。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[n393-value*]：DTE侧N393参数的值，取值范围为1～10。

【使用指导】

DTE设备每隔一定的时间要发送一个状态请求报文去查询链路状态，DCE设备收到该报文后立即发送状态报文。如果DTE设备在规定的时间内没有收到响应，就记录该错误。如果错误次数超过门限，DTE设备就认为物理通路不可用，所有的虚电路都不可用。

N392和N393一起定义了"错误门限"。其中N393表示被观察的总事件数，N392表示在被观察的总事件数中发生的错误门限。也就是说，如果DCE设备在N393个事件中，发生错误次数达到N392，DCE设备就认为错误次数达到门限，且认为物理通路不可用，所有的虚电路都不可用。

需要注意的是：

·DTE侧的N392参数的值应小于DTE侧的N393参数的值。

·配置本命令时，要求接口类型是DTE或者NNI。

【举例】

\# 配置帧中继接口Serial2/1/0工作在DTE方式，并配置N392和N393为5和6。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr interface-type dte

Sysname-Serial2/1/0 fr lmi n392dte 5

Sysname-Serial2/1/0 fr lmi n393dte 6

**帧中继 \-- 帧中继配置命令 \-- fr lmi t392dce**

------------------------------------------------------------------------

**[fr** **lmi t392dce**]命令用来配置DCE侧T392参数的值。

**[undo fr** **lmi t392dce**]命令用来恢复缺省情况。

【命令】

**[fr lmi t392dce** *t392-value*]

**[undo fr lmi t392dce**]

【缺省情况】

DCE侧T392参数的值为15秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t392-value*]：DCE侧T392参数的值，取值范围为5～30，单位为秒。

【使用指导】

DCE侧T392参数定义了DCE设备等待一个状态请求报文的最大时间。

需要注意的是：

·DCE侧的T392参数的值应大于DTE侧的T391参数的值（该参数的值通过**timer-hold**命令配置）。

·配置本命令时，要求接口类型是DCE或者NNI。

【举例】

\# 配置帧中继接口Serial2/1/0工作在DCE方式，并配置T392为10秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr interface-type dce

Sysname-Serial2/1/0 fr lmi t392dce 10

**帧中继 \-- 帧中继配置命令 \-- fr lmi type**

------------------------------------------------------------------------

**[fr lmi type**]命令用来配置帧中继LMI协议类型。

**[undo fr lmi type**]命令用来恢复缺省情况。

【命令】

**[fr lmi type**  { **ansi** \| **nonstandard** \| **q933a** }]

**[undo fr lmi type**]

【缺省情况】

接口的LMI协议类型为q933a。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ansi**]：ANSI T1.617附录D标准的LMI协议类型。

**[nonstandard**]：非标准兼容的LMI协议类型。

**[q933a**]：ITU-T Q.933附录A标准的LMI协议类型。

【使用指导】

LMI协议用于维护帧中继协议的PVC表，包括：通知PVC的增加、探测PVC的删除、监控PVC状态的变更、验证链路的完整性。

系统支持三种LMI协议类型：ITU-T的Q.933附录A、ANSI的T1.617附录D、非标准兼容协议。

【举例】

\# 配置接口Serial2/1/0的帧中继LMI协议类型为非标准兼容协议。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr lmi type nonstandard

**帧中继 \-- 帧中继配置命令 \-- fr map ip**

------------------------------------------------------------------------

**[fr** **map** **ip**]命令用来增加一条帧中继的地址映射。

**[undo fr** **map** **ip**]命令用来删除一条帧中继的地址映射。

【命令】

**[fr**[ **map** **ip** { *ip-address* \| **default** } *dlci-number*]]

**[undo**[ **fr** **map ip** { *ip-address* \| **default** }]] *dlci-number*

【缺省情况】

系统没有静态地址映射。

【视图】

接口视图（包括主接口和P2MP子接口）

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：对端的IP地址。

**[default**]：表示创建一条缺省地址映射。

*[dlci-number*]：虚电路DLCI编号，取值范围为16～1007。DLCI号0～15、1008～1023为帧中继协议保留，供特殊使用。

【使用指导】

地址映射可以通过手工配置建立，也可以通过InARP协议来自动完成。当对端主机较少或有缺省路由的情况下采用手工配置静态地址映射；当对端路由器也支持InARP协议而且网络较复杂的情况下，采用InARP协议建立动态地址映射。

需要注意的是：

·配置地址映射中的地址要求是有效的单播地址。

·配置本命令时，如果指定的虚电路不存在，则会创建此虚电路。

·同一个接口最多只能配置一条缺省地址映射。

·同一个接口到同一个IP地址只能配置一条地址映射。

【举例】

\# 接口Serial2/1/0连接的对端路由器的IP地址为202.38.163.252，在本地Serial2/1/0接口上有一条DLCI为50的虚电路连接到该路由器，配置静态地址映射如下：

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 fr map ip 202.38.163.252 50

【相关命令】

·**display fr map-info**

**帧中继 \-- 帧中继配置命令 \-- link-protocol fr**

------------------------------------------------------------------------

**[link-protocol fr**]命令用来配置接口封装的链路层协议为帧中继。

【命令】

**[link-protocol fr**]

【缺省情况】

除以太网接口、VLAN接口外，其它接口封装的链路层协议均为PPP。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置接口Serial2/1/0封装的链路层协议为帧中继。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

**帧中继 \-- 帧中继配置命令 \-- reset fr compression iphc**

------------------------------------------------------------------------

**[reset fr compression iphc**]命令用来清除帧中继IPHC压缩的统计信息。

【命令】

**[reset fr compression iphc**[ [ **rtp** \| **tcp** ]  **interface** *interface-type interface-number* [ **dlci** *number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rtp**]：清除IPHC RTP头压缩的统计信息。

**[tcp**]：清除IPHC TCP头压缩的统计信息。不指定**rtp**和**tcp**参数时，将同时清除RTP头压缩和TCP头压缩的统计信息。

**[interface** *interface-type interface-number*]：清除指定接口的IPHC压缩的统计信息。不指定本参数时，将清除所有接口的IPHC压缩的统计信息。

**[dlci** *number*]：清除指定接口、指定虚电路的IPHC压缩的统计信息。*number*表示虚电路DLCI编号，取值范围为16～1007。不指定本参数时，将清除指定接口下的所有虚电路的IPHC压缩的统计信息。

【举例】

\# 清除所有接口的IPHC压缩的统计信息。

\<Sysname\> reset fr compression iphc

【相关命令】

·**display fr compression iphc**

**帧中继 \-- 帧中继配置命令 \-- reset fr inarp**

------------------------------------------------------------------------

**[reset fr inarp**]命令用来清除InARP协议建立的动态地址映射。

【命令】

**[reset fr inarp ** **interface** *interface-type* *interface-number*  **dlci** *dlci-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**] *interface-type interface-number*：指定接口的类型和编号，可以指定主接口，也可以指定子接口。指定主接口时，清除该主接口及子接口的动态地址映射。指定子接口时，清除该子接口的动态地址映射。不指定接口时，清除所有接口的动态地址映射。

**[dlci*** dlci-number*]：虚电路DLCI编号，取值范围为16～1007。范围0～15、1008～1023的虚电路为帧中继协议保留，供特殊使用。指定虚电路时，清除该虚电路对应的动态地址映射。

【使用指导】

在某些特殊情况下，如网络结构修改导致原来建立的动态地址映射失效，需要重新建立新的地址映射，此时可以用该命令清除动态地址映射。

【举例】

\# 清除InARP协议建立的全部动态地址映射。

\<Sysname\> reset fr inarp

【相关命令】

·**fr inarp**

**帧中继 \-- 帧中继配置命令 \-- reset fr pvc**

------------------------------------------------------------------------

**[reset fr pvc**]命令用来清除帧中继的PVC统计信息。

【命令】

**[reset fr pvc** [ **interface** *interface-type* *interface-number* [ **dlci** *dlci-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**] *interface-type interface-number*：指定接口的类型和编号，可以指定主接口，也可以指定子接口。指定主接口时，清除该主接口及子接口的PVC统计信息。指定子接口时，清除该子接口的PVC统计信息。不指定接口时，清除所有接口的PVC统计信息。

**[dlci*** dlci-number*]：虚电路DLCI编号，取值范围为16～1007。范围0～15、1008～1023的虚电路为帧中继协议保留，供特殊使用。指定虚电路时，清除该虚电路对应的PVC统计信息。

【举例】

\# 清除接口Serial2/1/0下所有PVC的统计信息。

\<Sysname\> reset fr pvc interface serial 2/1/0

**帧中继 \-- 帧中继配置命令 \-- timer-hold**

------------------------------------------------------------------------

**[timer-hold**]命令用来配置DTE侧T391参数的值。

**[undo timer-hold**]命令用来恢复缺省情况。

【命令】

**[timer-hold*** seconds*]

**[undo timer-hold**]

【缺省情况】

DTE侧T391参数的值为10秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：DTE侧T391参数的值，取值范围为0～32767，单位为秒。当*seconds*取值为0时，表示禁止LMI协议。

【使用指导】

T391参数是一个时间变量，它定义了DTE设备发送状态请求报文的时间间隔。

需要注意的是：

·DTE侧的T391参数的值应小于DCE侧的T392参数的值。

·配置本命令时，要求接口类型是DTE或者NNI。

【举例】

\# 配置帧中继接口Serial2/1/0工作在DTE方式，并配置DTE侧T391参数的值为15秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol fr

Sysname-Serial2/1/0 fr interface-type dte

Sysname-Serial2/1/0 timer-hold 15
