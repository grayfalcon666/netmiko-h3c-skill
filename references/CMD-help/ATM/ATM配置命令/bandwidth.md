
**ATM \-- ATM配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth*** bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

VE接口视图/VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置VE接口Virtual-Ethernet2/4/1的期望带宽为50kbit/s。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1

Sysname-Virtual-Ethernet2/4/1 bandwidth 50

**ATM \-- ATM配置命令 \-- broadcast**

------------------------------------------------------------------------

**[broadcast**]命令用来打开当前PVC或PVC-group的广播属性。

**[undo broadcast**]命令用来恢复缺省情况。

【命令】

**[broadcast**]

**[undo broadcast**]

【缺省情况】

广播属性处于关闭状态。

【视图】

PVC视图/PVC-group视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果某PVC或PVC-group配置了广播属性，则PVC或PVC-group所属接口上的广播或组播报文都要在该PVC或PVC-group上发送一份。

如果在PVC或PVC-group上需要发送广播或者组播报文，请务必配置此关键字。例如：PIM组播如果要想在以ATM链路相连的路由器间建立PIM邻居，则链路两端的ATM接口下的PVC必须配置广播属性，因为建立PIM邻居时需要通过ATM接口来发送IP组播报文。

本命令不能在PVC-group下的PVC下配置。

【举例】

\# 打开PVC 0/100的广播属性。

\<Sysname\> system-view

Sysname interface atm 2/4/1.1

Sysname-ATM2/4/1.1 pvc 0/100

Sysname-ATM2/4/1.1-pvc-0/100 broadcast

**ATM \-- ATM配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

VE接口视图/VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将VE接口Virtual-Ethernet2/4/1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1

Sysname-Virtual-Ethernet2/4/1 default

**ATM \-- ATM配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Virtual-Ethernet2/4/1 Interface。

【视图】

VE接口视图/VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置VE接口Virtual-Ethernet2/4/1的描述信息为"Virtual-Ethernet"。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1

Sysname-Virtual-Ethernet2/4/1 description Virtual-Ethernet

**ATM \-- ATM配置命令 \-- display atm map-info**

------------------------------------------------------------------------

**[display atm map-info**]命令用来显示PVC或PVC-group的映射信息。

【命令】

**[display atm map-info**[ [ **interface** *interface-type* { *interface-number* \| *interface-number.subnumber* } [ **pvc** { *pvc-name* \| *vpi/vci* } \| **pvc-group** *group-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**[ *interface-type* { *interface-number* \| *interface-number.subnumber* }]]：显示指定接口的映射信息。支持ATM接口、ATM子接口。

**[pvc**]：显示指定PVC的映射信息。

*[pvc-name*]：PVC名，长度为1～15个字符的字符串，区分大小写，PVC名中不允许使用"/"和"-"，如"1/20"、"a-b"就不允许作为PVC名。

*[vpi/vci*]：*vpi*为VPI值，取值范围为0～255；*vci*为VCI值，取值范围与接口类型相关，请参见"[表]1-8(?-1864992396#_Ref337389143)"。*vpi*与*vci*不能同时为0。通常，*vci*取值0到31保留用于特定用途，建议用户不要使用。

**[pvc-group** *group-number*]：显示指定PVC-group的映射信息。*group-number*表示PVC-group编号，取值范围为1～128。

【使用指导】

·如果不指定接口，则显示所有接口下所有PVC和PVC-group的映射信息。

·如果指定接口而不指定PVC或PVC-group，则显示指定接口下所有PVC和PVC-group的映射信息。

·如果指定接口并且指定PVC或PVC-group，则显示指定接口下指定PVC或PVC-group的映射信息。

【举例】

\# 显示所有接口下所有PVC和PVC-group的映射信息。

\<Sysname\> display atm map-info

ATM2/4/0

  PVC 1/32:

    Protocol: PPP, Interface: Virtual-Template10, State: UP

    Protocol: IP, IP address: 100.11.1.1, State: UP

  PVC-group 1:

    Protocol: IP InARP, IP address: 100.22.22.2, Interval: 2 minutes, State: UP

    Protocol: ETH, Interface: Virtual-Ethernet2, State: UP

ATM2/4/1

  PVC 2/32:

    Protocol: IP InARP, IP address: no IP address, Interval: 3 minutes, State: UP

表1-1 display atm map-info命令显示信息描述表

字段

描述

ATM2/4/0

接口名称

PVC 1/32

PVC的VPI/VCI值对

PVC-group 1

PVC-group名称

Protocol

PVC或PVC-group支持的上层协议的类型，可能的取值及含义如下：

·PPP：PPP协议

·IP：IP协议

·IP InARP ：IP InARP协议

·ETH：以太网协议

State

对应映射的状态，可能的取值及含义如下：

·UP：对于PPP、IP（包括InARP）映射，表示其PVC或PVC-group状态为UP；对于ETH映射，表示其PVC或PVC-group状态和VE口状态均为UP

·DOWN：对于PPP、IP（包括InARP）映射，表示其PVC或PVC-group状态为DOWN；对于ETH映射，表示其PVC或PVC-group状态和VE口状态至少一个为DOWN

IP address

IP地址

Interval

发送InARP报文的间隔时间，单位为分钟

Interface

承载PPPoA或EoA的虚拟接口

**ATM \-- ATM配置命令 \-- display atm pvc-group**

------------------------------------------------------------------------

**[display atm pvc-group**]命令用来显示PVC-group的信息。

【命令】

**[display atm pvc-group**[ [ **interface** *interface-type* { *interface-number* \| *interface-number.subnumber* } [ **pvc-group** *group-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**[ *interface-type* { *interface-number* \| *interface-number.subnumber* }]]：显示指定接口的PVC-group信息。支持ATM接口、ATM子接口。

**[pvc-group** *group-number*]：显示指定PVC-group的信息。*group-number*表示PVC-group编号，取值范围为1～128。

【使用指导】

·如果不指定接口，则显示所有接口的PVC-group的简要信息。

·如果指定接口而不指定PVC-group，则显示指定接口的所有PVC-group的简要信息。

·如果指定接口并且指定PVC-group，则显示指定接口的指定PVC-group的详细信息。

【举例】

\# 显示所有接口的PVC-group的简要信息。

\<Sysname\> display atm pvc-group

ATM2/4/0, State UP

  PVC-group: 1

    Encapsulation: SNAP, Protocol: IP

    VPI/VCI  PVC name   Precedence        State

    1/32     aa         Default           UP

    2/32     N/A        2-3               UP

    3/32     N/A        5                 UP

  PVC-group: 3

    Encapsulation: SNAP, Protocol: IP

    VPI/VCI  PVC name   Precedence        State

    3/64     bb         4                 UP

    4/64     N/A        Default           UP

ATM2/4/1, State UP

  PVC-group: 1

    Encapsulation: SNAP, Protocol: IP

    VPI/VCI  PVC name   Precedence        State

    1/32     aa         Default           UP

表1-2 display atm pvc-group命令显示信息描述表

字段

描述

ATM2/4/0, State UP

PVC-group所属的接口名及接口物理状态和管理状态

如果不是子接口，可能的状态及含义如下：

·UP：该接口的管理状态和物理状态均为开启

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）或者该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

如果是子接口，可能的状态及含义如下：

·UP：该接口的管理状态和其父接口的物理状态和管理状态均为开启

·DOWN：表示该接口或其父接口已经通过shutdown命令被关闭或者其父接口物理状态为关闭

PVC-group：1

PVC-group对应的PVC-group编号

Encapsulation

PVC-group的AAL5封装类型，目前只可能取值SNAP，表示LLC（Logical Link Control，逻辑链接控制）/SNAP（Subnet Access Protocol，子网访问协议）封装类型

Protocol

PVC-group支持的上层协议的类型，可能的取值及含义如下：

·PPP：PPP协议

·IP：IP协议

·ETH：以太协议

·None：未配置任何协议

VPI/VCI

PVC的VPI/VCI值对

PVC name

PVC名称，N/A表示没有PVC名称

Precedence

PVC-group下PVC承载的IP包的优先级，可能的取值及含义如下：

·Default：表示该PVC为缺省PVC，则没有指定PVC承载的优先级别的IP包将从缺省PVC进行传输

·a-b：表示该PVC承载的IP包的最小优先级到最大优先级（a，b表示数字0\~7，a\<b）

·c：表示该PVC承载的IP包的优先级（c表示数字0\~7）

·-：表示该PVC下没有配置承载IP包优先级

State

PVC的状态，可能的取值及含义如下：

·UP：该PVC所属ATM接口的状态、shutdown状态和OAM状态均为UP状态

·DOWN：PVC所属ATM接口的状态、shutdown状态和OAM状态中至少其中一个为DOWN状态

\# 显示指定PVC-group的详细信息。

\<Sysname\> display atm pvc-group interface atm 2/4/0 pvc-group 1

ATM2/4/0, PVC-group: 1

  Encapsulation: SNAP, Protocol: None

  PVC VPI/VCI: 0/34

    Precedence: default

    Service-type: CBR, Output-pcr: 200 kbps, CDVT: 500 us

    Transmit-Priority: 0

    OAM loopback interval: 0 sec(disabled), OAM loopback retry interval: 1 sec

    OAM loopback retry count (up/down): 3/5

    OAM AIS-RDI count (up/down): 3/1          

    Interface State: UP, OAM State: UP, PVC State: UP

    Input: 0 packets, 0 bytes, 0 errors

    Output: 0 packets, 0 bytes, 0 errors

    Output queue: (Urgent queuing : Size/Length/Discards)  0/100/0

    Output queue: (Protocol queuing : Size/Length/Discards)  0/500/0

    Output queue: (FIFO queuing : Size/Length/Discards)  0/75/0

    OAM cells received: 42

      F5 Loopback: 0, F5 AIS: 42, F5 RDI: 0

    OAM cells sent: 0

      F5 Loopback: 0

    OAM cell drops: 0

    OAM AIS State: No AIS Alarm

    OAM RDI State: No RDI Alarm

    OAM CC State: No CC Alarm

  PVC VPI/VCI: 0/35

    Precedence: -

    Service-type: UBR, Output-pcr: 200 kbps

    Transmit-Priority: 0

    OAM loopback interval: 0 sec(disabled), OAM loopback retry interval: 1 sec

    OAM loopback retry count (up/down): 3/5

    OAM AIS-RDI count (up/down): 3/1

    Interface State: UP, OAM State: UP, PVC State: UP

    Input: 0 packets, 0 bytes, 0 errors

    Output: 0 packets, 0 bytes, 0 errors

    Output queue: (Urgent queuing : Size/Length/Discards)  0/100/0

    Output queue: (Protocol queuing : Size/Length/Discards)  0/500/0

    Output queue: (FIFO queuing : Size/Length/Discards)  0/75/0

    OAM cells received: 42

      F5 Loopback: 0, F5 AIS: 42, F5 RDI: 0

    OAM cells sent: 0

      F5 Loopback: 0

    OAM cell drops: 0

    OAM AIS State: No AIS Alarm

    OAM RDI State: No RDI Alarm

    OAM CC State: No CC Alarm

表1-3 display atm pvc-group命令指定PVC-group显示信息描述表

字段

描述

ATM2/4/0,PVC-group： 1

表示PVC-group所在接口及对应的PVC-group编号

Encapsulation

PVC-group的AAL5封装类型，目前只可能取值SNAP，表示LLC（Logical Link Control，逻辑链接控制）/SNAP（Subnet Access Protocol，子网访问协议）封装类型

Protocol

PVC-group支持的上层协议的类型，可能的取值及含义如下：

·PPP：PPP协议

·IP：IP协议

·ETH：以太协议

·None：未配置任何协议

PVC VPI/ VCI

PVC的VPI/VCI值对

Precedence

PVC-group下PVC承载的IP包的优先级，可能的取值及含义如下：

·Default：表示该PVC为缺省PVC，则没有指定PVC承载的优先级别的IP包将从缺省PVC进行传输

·a-b：表示该PVC承载的IP包的最小优先级到最大优先级（a，b表示数字0\~7，a\<b）

· c：表示该PVC承载的IP包的优先级（c表示数字0\~7）

·- ：表示该PVC下没有配置承载IP包优先级

Service-type

服务类型，可能的类型如下：

·CBR：恒定速率

·UBR：非确定速率

·VBR-NRT：非实时可变速率

·VBR-RT：实时可变速率

Output-pcr

输出ATM信元的峰值速率

CDVT

信元时延变化容限（Cell Delay Variation Tolerance），单位为微秒

Transmit-Priority

传输优先级

OAM loopback interval

发送OAM F5 Loopback信元的间隔时间，单位为秒

OAM loopback retry interval

OAM F5 Loopback重传验证的间隔时间，单位为秒

OAM loopback retry count (up/down)

OAM验证UP和DOWN的信元数量

OAM AIS-RDI count (up/down)

OAM AIS-RDI验证UP的秒数、OAM AIS-RDI验证DOWN的信元数量

Interface State

该PVC所属的接口名及接口物理状态和管理状态

如果不是子接口，可能的状态及含义如下：

·UP：该接口的管理状态和物理状态均为开启

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）或者该接口已经通过shutdown命令被关闭，即管理状态为关闭

如果是子接口，可能的状态及含义如下：

·UP：该接口的管理状态和其父接口的物理状态和管理状态均为开启

·DOWN：表示该接口或其父接口已经通过shutdown命令被关闭或者其父接口物理状态关闭

OAM State

OAM协议状态，可能的取值及含义如下：

·UP：协议状态开启

·DOWN：协议状态关闭

PVC State

PVC的状态，可能的取值及含义如下：

·UP：该PVC所属ATM接口的状态、shutdown状态和OAM状态均为UP状态

·DOWN：PVC所属ATM接口的状态、shutdown状态和OAM状态中至少其中一个为DOWN状态

Input: 0 packets, 0 bytes, 0 errors

接收的报文数、字节数以及接收报文的错误数

Output: 0 packets, 0 bytes, 0 errors

发送的报文数、字节数以及发送报文的错误数

Output queue

PVC的QoS发送报文队列信息

OAM cells received

收到的OAM信元个数

F5 Loopback

收到的F5 Loopback信元个数

F5 AIS

收到的AIS信元个数。如果不支持AIS告警状态，则只显示信元个数，不显示告警状态（即OAM AIS State字段）

F5 RDI

收到的RDI信元个数。如果不支持RDI告警状态，则只显示信元个数，不显示告警状态（即OAM RDI State字段）

OAM cells sent

发送的OAM信元个数

F5 Loopback

发送的F5 Loopback信元个数

OAM cell drops

OAM信元丢弃的个数

OAM AIS State

AIS告警状态，可能的取值及含义如下：

·No AIS Alarm：无OAM AIS告警

·E2E AIS Alarm：端到端OAM AIS告警

如果支持告警状态，则只显示告警状态，不显示信元个数（即F5 AIS字段）

OAM RDI State

RDI告警状态，可能的取值及含义如下：

·No RDI Alarm：无OAM RDI告警

·E2E RDI Alarm：端到端OAM RDI告警

如果支持告警状态，则只显示告警状态，不显示信元个数（即F5 RDI字段）

OAM CC State

CC告警状态，可能的取值及含义如下：

·No CC Alarm：无OAM CC告警

·E2E CC Alarm：端到端OAM CC告警

**ATM \-- ATM配置命令 \-- display atm pvc-info**

------------------------------------------------------------------------

**[display atm pvc-info**]命令用来显示PVC的信息。

【命令】

**[display atm pvc-info**[ [ **interface** *interface-type* { *interface-number* \| *interface-number.subnumber* } [ **pvc** { *pvc-name* \| *vpi/vci* } ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**[ *interface-type* { *interface-number* \| *interface-number.subnumber* }]]：显示指定接口的PVC信息。支持ATM接口、ATM子接口。

**[pvc**]：显示指定PVC的信息。

*[pvc-name*]：PVC名，长度为1～15个字符的字符串，区分大小写，PVC名中不允许使用"/"和"-"，如"1/20"、"a-b"就不允许作为PVC名。

*[vpi/vci*]：*vpi*为VPI值，取值范围为0～255；*vci*为VCI值，取值范围与接口类型相关，请参见"[表]1-8(?-1864992396#_Ref337389143)"。*vpi*与*vci*不能同时为0。通常，*vci*取值0到31保留用于特定用途，建议用户不要使用。

【使用指导】

·如果不指定接口，则显示所有接口的PVC的简要信息。

·如果指定接口而不指定PVC，则显示指定接口的所有PVC的简要信息。

·如果指定接口并且指定PVC，则显示指定接口的指定PVC的详细信息。

【举例】

\# 显示所有接口的PVC的简要信息。

\<Sysname\> display atm pvc-info

VPI/VCI   State    PVC name    Encap    Protocol   Interface

1/32      UP       aa          SNAP     IP         ATM2/4/0

1/33      UP       Sysname     MUX      None       ATM2/4/0

1/55      UP       datacomm    SNAP     PPP        ATM2/4/0.1

2/66      UP       N/A         SNAP     IP         ATM2/4/0.4

2/101     UP       beijing     SNAP     ETH        ATM2/4/0.2

表1-4 display atm pvc-info命令显示信息描述表

字段

描述

VPI/VCI

PVC的VPI/VCI值对

State

PVC的状态，可能的取值及含义如下：

·UP：该PVC所属ATM接口的状态、shutdown状态和OAM状态均为UP状态

·DOWN： PVC所属ATM接口的状态、shutdown状态和OAM状态中至少其中一个为DOWN状态

PVC name

PVC名称，N/A表示没有PVC名称

Encap

PVC的AAL5封装类型，可能的取值及含义如下：

·SNAP：表示LLC（Logical Link Control，逻辑链接控制）/SNAP（Subnet Access Protocol，子网访问协议）封装类型

·NLPID：表示RFC1490封装类型

·MUX：表示MUX复用封装类型

Protocol

PVC支持的上层协议的类型，可能的取值及含义如下：

·PPP：PPP协议

·IP：IP协议

·ETH：以太协议

·None：未配置任何协议

Interface

PVC所属的接口

\# 显示指定PVC的详细信息。

\<Sysname\> display atm pvc-info interface atm 2/4/1 pvc 1/100

ATM2/4/1, VPI: 1, VCI: 100

  Encapsulation: SNAP, Protocol: IP

  Service-type: UBR, Output-pcr: 200 kbps

  Transmit-Priority: 0

  OAM loopback interval: 0 sec(disabled), OAM loopback retry interval: 1 sec

  OAM loopback retry count (up/down): 3/5

  OAM AIS-RDI count (up/down): 3/1

  Interface State: UP, OAM State: UP, PVC State: UP

  Input: 0 packets, 0 bytes, 0 errors

  Output: 0 packets, 0 bytes, 0 errors

  Output queue: (Urgent queuing : Size/Length/Discards)  0/100/0

  Output queue: (Protocol queuing : Size/Length/Discards)  0/500/0

  Output queue: (FIFO queuing : Size/Length/Discards)  0/75/0

  OAM cells received: 42

    F5 Loopback: 0, F5 AIS: 42, F5 RDI: 0

  OAM cells sent: 0

    F5 Loopback: 0

  OAM cell drops: 0

  OAM AIS State: No AIS Alarm

  OAM RDI State: No RDI Alarm

  OAM CC State: No CC Alarm

表1-5 display atm pvc-info命令指定PVC显示信息描述表

字段

描述

ATM2/4/1

PVC所属的接口名

VPI

虚路径标识符

VCI

虚通道标识符

Encapsulation

PVC的AAL5封装类型，可能的取值及含义如下：

·SNAP：表示LLC（Logical Link Control，逻辑链接控制）/SNAP（Subnet Access Protocol，子网访问协议）封装类型

·NLPID：表示RFC1490封装类型

·MUX：表示MUX复用封装类型

Protocol

PVC支持的上层协议的类型，可能的取值及含义如下：

·PPP：PPP协议

·IP：IP协议

·ETH：以太协议

·None：未配置任何协议

Service-type

服务类型，可能的类型如下：

·CBR：恒定速率

·UBR：非确定速率

·VBR-NRT：非实时可变速率

·VBR-RT：实时可变速率

Output-pcr

输出ATM信元的峰值速率

Transmit-Priority

传输优先级

OAM loopback interval

发送OAM F5 Loopback信元的间隔时间

OAM loopback retry interval

OAM F5 Loopback重传验证的间隔时间

OAM loopback retry count (up/down)

OAM验证UP和DOWN的信元数量

OAM AIS-RDI count (up/down)

OAM AIS-RDI验证UP的秒数、OAM AIS-RDI验证DOWN的信元数量

Interface State

该PVC所属的接口名及接口物理状态和管理状态

如果不是子接口，可能的状态及含义如下：

·UP：该接口的管理状态和物理状态均为开启

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）或者该接口已经通过shutdown命令被关闭，即管理状态为关闭

如果是子接口，可能的状态及含义如下：

·UP：该接口的管理状态和其父接口的物理状态和管理状态均为开启

·DOWN：表示该接口或其父接口已经通过shutdown命令被关闭或者其父接口物理状态关闭

OAM State

OAM协议状态，可能的取值及含义如下：

·UP：协议状态开启

·DOWN：协议状态关闭

PVC State

PVC的状态，可能的取值及含义如下：

·UP：该PVC所属ATM接口的状态、shutdown状态和OAM状态均为UP状态

·DOWN：PVC所属ATM接口的状态、shutdown状态和OAM状态中至少其中一个为DOWN状态

Input: 0 packets, 0 bytes, 0 errors

接收的报文数、字节数以及接收报文的错误数

Output: 0 packets, 0 bytes, 0 errors

发送的报文数、字节数以及发送报文的错误数

Output queue

PVC的QoS发送报文队列信息

OAM cells received

收到的OAM信元个数

F5 Loopback

收到的F5 Loopback信元个数

F5 AIS

收到的AIS信元个数。如果不支持AIS告警状态，则只显示信元个数，不显示告警状态（即OAM AIS State字段）

F5 RDI

收到的RDI信元个数。如果不支持RDI告警状态，则只显示信元个数，不显示告警状态（即OAM RDI State字段）

OAM cells sent

发送的OAM信元个数

F5 Loopback

发送的F5 Loopback信元个数

OAM cell drops

OAM信元丢弃的个数

OAM AIS State

AIS告警状态，可能的取值及含义如下：

·No AIS Alarm：无OAM AIS告警

·E2E AIS Alarm：端到端OAM AIS告警

如果支持告警状态，则只显示告警状态，不显示信元个数（即F5 AIS字段）

OAM RDI State

RDI告警状态，可能的取值及含义如下：

·No RDI Alarm：无OAM RDI告警

·E2E RDI Alarm：端到端OAM RDI告警

如果支持告警状态，则只显示告警状态，不显示信元个数（即F5 RDI字段）

OAM CC State

CC告警状态，可能的取值及含义如下：

·No CC Alarm：无OAM CC告警

·E2E CC Alarm：端到端OAM CC告警

**ATM \-- ATM配置命令 \-- display interface virtual-ethernet**

------------------------------------------------------------------------

**[display interface virtual-ethernet**]命令用来显示VE接口的相关信息。

【命令】

**[display interface** [ **virtual-ethernet** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定VE接口的信息。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**virtual-ethernet**参数，将显示设备支持的所有接口的相关信息。

·如果指定**virtual-ethernet**参数，不指定*interface-number*参数，将显示所有已创建的VE接口的相关信息。

【举例】

\# 显示VE接口Virtual-Ethernet2/4/1的详细信息。

\<Sysname\> display interface virtual-ethernet 2/4/1

Virtual-Ethernet2/4/1

Current state: UP

Line protocol state: UP

Description: Virtual-Ethernet2/4/1 Interface

Bandwidth: 20000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 00e0-fc0d-9485

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 00e0-fc0d-9485

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

\# 显示VE接口Virtual-Ethernet2/4/1的概要信息。

\<Sysname\> display interface virtual-ethernet 2/4/1 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

VE1                  DOWN DOWN     \--

\# 显示当前物理状态为down的VE接口的信息以及down的原因。

\<Sysname\> display interface virtual-ethernet brief down

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

VE2/4/1              DOWN Not connected

表1-6 display interface virtual-ethernet命令显示信息描述表

字段

描述

Current state

该接口的物理状态，状态可能为：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该端口的管理状态和物理状态均为开启

Line protocol state

该接口的链路层协议状态，可能的状态及含义如下：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Description

该接口的描述信息

Bandwidth

该接口的期望带宽

Maximum Transmit Unit

该接口的最大传输单元

Internet protocol processing

该接口网络层协议处理状况

IP Packet Frame Type

该接口IPv4报文帧格式，取值为PKTFMT_ETHNT_2表示报文以Ethernet II型帧格式封装

IPv6 Packet Frame Type

该接口IPv6报文帧格式

Hardware Address

该接口的MAC地址

Last clearing of counters: Never

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Last 300 seconds input rate

该接口在最近300秒接收报文的平均速率

Last 300 seconds output rate

该接口在最近300秒发送报文的平均速率

Input

输入报文统计信息：

·packets：数据包的个数

·bytes：总字节数

·drops：丢弃的报文个数

Output

输出报文统计信息：

·packets：数据包的个数

·bytes：总字节数

·drops：丢弃的报文个数

Brief information on interface(s) under route mode

三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

**ATM \-- ATM配置命令 \-- encapsulation**

------------------------------------------------------------------------

**[encapsulation**]命令用来配置PVC或PVC-group的ATM AAL5封装类型。

**[undo encapsulation**]命令用来恢复缺省情况。

【命令】

**[encapsulation**[ { **aal5mux** *\|* **aal5nlpid** *\|* **aal5snap** }]]

**[undo encapsulation**]

【缺省情况】

ATM AAL5封装类型为**aal5snap**。

【视图】

PVC视图/PVC-group视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aal5mux**]：MUX复用封装类型。

**[aal5nlpid**]：RFC1490封装类型。

**[aal5snap**]：LLC（Logical Link Control，逻辑链接控制）/SNAP（Subnet Access Protocol，子网访问协议）封装类型。

【使用指导】

不同的ATM AAL5封装类型支持的映射类型如下：

·**aal5snap**封装支持IPoA、IPoEoA、PPPoA、PPPoEoA映射。

·**aal5mux**封装支持IPoA、IPoEoA、PPPoA、PPPoEoA映射，但不支持同时承载多种协议。

·**aal5nlpid**封装只支持IPoA映射。

需要注意的是：

·相互通信的两端设备上配置的ATM AAL5封装类型要保持一致。

·只有**aal5snap**封装支持InARP协议，当采用**aal5mux**和**aal5nlpid**封装时不能配置InARP。

·PVC/PVC-group支持同时承载多种协议，但某些类型的封装可能并不支持部分应用方式（即IPoA、IPoEoA、PPPoA、PPPoEoA中的一种或几种）。当出现不能支持的情况时，系统会给出错误提示。

·在PVC/PVC-group切换封装时，如果已经配置了与切换后封装类型冲突的映射，切换封装后的PVC/PVC-group将会删除所有冲突的映射对应的配置。

·本命令不能在PVC-group下的PVC下配置。

【举例】

\# 指定ATM接口2/4/0的PVC 1/32的AAL5封装类型为**aal5snap**。

\<Sysname\>system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/32

Sysname-ATM2/4/0-pvc-1/32 encapsulation aal5snap

**ATM \-- ATM配置命令 \-- interface virtual-ethernet**

------------------------------------------------------------------------

**[interface virtual-ethernet**]命令用来创建VE（Virtual Ethernet，三层虚拟以太网）接口或子接口，并进入VE接口或子接口视图。如果该VE接口或子接口已经存在，则直接进入VE接口或子接口视图。

**[undo interface virtual-ethernet**]命令用来删除VE接口或子接口。

【命令】

**[interface virtual-ethernet****[{ *interface-number* \| *interface-number.subnumber* }]]

**[undo interface virtual-ethernet**[ { *interface-number* \| *interface-number.subnumber* }]]

【缺省情况】

不存在VE接口和子接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：VE接口编号。

*[interface-number.subnumber*]：VE子接口编号，其中*interface-number*为主接口编号；*subnumber*为子接口编号。

【使用指导】

VE接口的波特率为10000000bit/s。

【举例】

\# 创建VE接口并进入VE接口视图。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1

Sysname-Virtual-Ethernet2/4/1

\# 创建VE子接口并进入VE子接口视图。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1.1

Sysname-Virtual-Ethernet2/4/1.1

**ATM \-- ATM配置命令 \-- mac-address**

------------------------------------------------------------------------

**[mac-address**]命令用来配置VE接口的MAC地址。

**[undo mac-address**]命令用来恢复缺省情况。

【命令】

**[mac-address** *mac-address*]

**[undo mac-address**]

【缺省情况】

VE接口在创建时会使用设备的桥MAC地址作为自己的MAC地址。

【视图】

VE接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：MAC地址，形式为H-H-H。

【使用指导】

VE接口在创建时会使用设备的桥MAC地址作为自己的MAC地址，这样，所有的VE接口都共用一个MAC地址。如果同一设备的多个VE接口通过不同的PVC连接到同一个DHCP服务器，而DHCP服务器上采用静态绑定方式给VE接口进行IP地址分配，则需要使用**mac-address**命令为不同的VE接口配置不同的MAC地址。

【举例】

\# 配置VE接口Virtual-Ethernet2/4/1的MAC地址为0001-0001-0001。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1

Sysname-Virtual-Ethernet2/4/1 mac-address 1-1-1

**ATM \-- ATM配置命令 \-- map bridge**

------------------------------------------------------------------------

**[map bridge**]命令用来为PVC或PVC-group创建IPoEoA映射、PPPoEoA映射。

**[undo map bridge**]命令用来删除该映射。

【命令】

**[map bridge virtual-ethernet** *interface-number*]

**[undo map bridge**]

【缺省情况】

没有配置任何映射。

【视图】

PVC视图/PVC-group视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[virtual-ethernet*** interface-number*]：VE接口。*interface-number*表示VE接口编号。该接口必须已经创建。

【使用指导】

·**aal5snap**和**aal5mux**封装支持IPoEoA映射、PPPoEoA映射。

·每个VE接口上最多允许创建512条映射。

·每个PVC或PVC-group只能映射到一个VE接口。

·本板VE接口只能绑定到本板PVC或PVC-group，使用前可以看VE接口的接口编号中对应的板号和PVC或PVC-group所在ATM接口对应板号是否一致。

·本命令不能在PVC-group下的PVC下配置。

·配置IPoEoA、PPPoEoA应用时，必须指定一个VE接口与之对应。

【举例】

下面这个例子展示了一个完整的IPoEoA配置过程。

\# 创建VE接口Virtual-Ethernet2/4/1。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1

\# 为该VE接口配置IP地址10.1.1.1/16。

Sysname-Virtual-Ethernet2/4/1 ip address 10.1.1.1 255.255.0.0

Sysname-Virtual-Ethernet2/4/1 quit

\# 在ATM接口ATM2/4/0下创建VPI/VCI为1/102的PVC。

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/102

\# 在PVC视图下使用已经创建的VE接口来创建IPoEoA映射。

Sysname-ATM2/4/0-pvc-1/102 map bridge virtual-ethernet 2/4/1

【相关命令】

·**encapsulation**

**ATM \-- ATM配置命令 \-- map ip**

------------------------------------------------------------------------

**[map ip**]命令用来为PVC或PVC-group创建IPoA映射，使PVC或PVC-group承载IP协议报文。

**[undo map ip**]命令用来删除该映射。

【命令】

**[map ip**[ { *ip-address* \| **default** \| **inarp** [ *minutes* ] }]]

**[undo map ip**[ [ *ip-address* \| **default** \| **inarp** ]]]

【缺省情况】

没有配置任何映射。

【视图】

PVC视图/PVC-group视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：映射到PVC或PVC-group的对端接口的IP地址。

**[default**]：配置一个具有缺省路由属性的映射。若某个报文在接口上找不到下一跳地址和*ip-address*相同的映射，但某条PVC或PVC-group配置了default映射，则报文将从该PVC或PVC-group上发送。

**[inarp**]：使能反向地址解析InARP。

*[minutes*]：发送InARP报文的间隔时间，取值范围为1～600，单位为分钟，缺省值为15分钟。

【使用指导】

·所有的封装类型都支持IPoA映射。但只有**aal5snap**封装支持配置InARP映射，当采用**aal5mux**和**aal5nlpid**封装时不能配置InARP映射。

·相同PVC或PVC-group下可以映射多个IP地址，且静态IP地址映射、default映射和InARP映射三者可以同时配置。

·相同接口下不同的PVC或PVC-group不能映射到同一个IP地址。

·同一个接口下的PVC和PVC-group最多只能配置一个default映射。

·执行**undo**命令时，如果不指定任何参数，则删除该PVC或PVC-group下所有的静态IP地址映射、default映射和InARP映射。

·本命令不能在PVC-group下的PVC下配置。

【举例】

\# 在PVC 1/32上创建一个静态IP地址映射，指定对端IP地址为61.123.30.169。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/32

Sysname-ATM2/4/0-pvc-1/32 map ip 61.123.30.169

\# 在PVC 1/33上使能InARP映射，每10分钟发送一次InARP报文。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/33

Sysname-ATM2/4/0-pvc-1/33 map ip inarp 10

\# 在PVC 1/33上删除所有类型的IP地址映射。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/33

Sysname-ATM2/4/0-pvc-1/33 undo map ip

【相关命令】

·**encapsulation**

**ATM \-- ATM配置命令 \-- map ppp**

------------------------------------------------------------------------

**[map ppp**]命令用来为PVC或PVC-group创建PPPoA映射。

**[undo map ppp**]命令用来删除该映射。

【命令】

**[map ppp virtual-template** *vt-number*]

**[undo map ppp**]

【缺省情况】

没有配置任何映射。

【视图】

PVC视图/PVC-group视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vt-number*]：PPPoA对应的虚拟模板接口编号。该虚拟模板接口必须已经创建。

【使用指导】

·**aal5snap**和**aal5mux**封装支持PPPoA映射。

·每个PVC或PVC-group只能映射到一个虚拟模板接口。

·本命令不能在PVC-group下的PVC下配置。

【举例】

下面这个例子展示了一个完整的PPPoA配置过程。

\# 创建虚拟模板接口10并为该接口配置IP地址。

\<Sysname\> system-view

Sysname interface virtual-template 10

Sysname-Virtual-Template10 ip address 202.38.160.1 255.255.255.0

Sysname-Virtual-Template10 quit

\# 在ATM接口ATM2/4/0下创建VPI/VCI为1/101的PVC。

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/101

\# 使用已经创建的虚拟模板接口来创建PPPoA映射。

Sysname-ATM2/4/0-pvc-1/101 map ppp virtual-template 10

【相关命令】

·**encapsulation**

**ATM \-- ATM配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

接口的MTU值为1500字节。

【视图】

VE接口视图/VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

需要注意的是，配置了**mtu**命令后需要执行命令**shutdown**和**undo shutdown**，这样该配置才能在接口上生效。

【举例】

\# 配置接口VE2/4/0的MTU值为200字节。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/0

Sysname- Virtual-Ethernet2/4/0 mtu 200

**ATM \-- ATM配置命令 \-- oam ais-rdi**

------------------------------------------------------------------------

**[oam ais-rdi**]命令用来修改AIS/RDI（Alarm Indication Signal/Remote Defect Indication，告警指示信号/远程故障指示）告警信元检测的相关参数。

**[undo oam ais-rdi**]命令用来恢复缺省情况。

【命令】

**[oam ais-rdi** **up** *up-seconds* **down** *down-seconds*]

**[undo oam ais-rdi**]

【缺省情况】

参数*up-seconds*为3秒，参数*down-seconds*为1秒。即当系统连续1秒收到AIS/RDI告警信元后，PVC状态转变为DOWN，当连续3秒没有收到AIS/RDI告警信元后，PVC状态转变为UP。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[up*** up-seconds*]：连续*up-seconds*秒没有收到AIS/RDI告警信元，PVC状态转变为UP。*up-seconds*的取值范围为3～60，单位为秒。

**[down*** down-seconds*]：连续*down-seconds*秒收到AIS/RDI告警信元后，PVC状态转变为DOWN。*down-seconds*的取值范围为1～60，单位为秒。

【使用指导】

系统使用一个超时时间为1秒的定时器来检测每秒内是否收到了AIS/RDI告警信元。当连续*down-seconds*秒收到AIS/RDI告警信元后，PVC状态转变为DOWN，当连续*up-seconds*秒没有收到AIS/RDI告警信元后，PVC状态转变为UP。

【举例】

\# 在ATM接口下的PVC1/32上修改AIS-RDI告警检测参数，*up-seconds*为5，*down-seconds*为5。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/32

Sysname-ATM2/4/0-pvc-1/32 oam ais-rdi up 5 down 5

\# 在PVC-group2下的PVC1/33上修改AIS-RDI告警检测参数，*up-seconds*为5，*down-secondst*为5。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 2

Sysname-ATM2/4/0-pvc-group-2 pvc 1/33

Sysname-ATM2/4/0-pvc-group-2-pvc-1/33 oam ais-rdi up 5 down 5

**ATM \-- ATM配置命令 \-- oam cc**

------------------------------------------------------------------------

**[oam cc**]命令用来启动OAM CC（Continuity Check，连续性检测）功能。

**[undo oam cc**]命令用来恢复缺省情况。

【命令】

**[oam cc**[ { **both** \| **sink** \| **source** }]]

**[undo oam cc**]

【缺省情况】

OAM CC功能处于关闭状态。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[both**]：PVC作为接收端时启动CC信元的检测功能，以及作为发送端时启动CC信元的发送功能。

**[sink**]：PVC作为接收端时启动CC信元的检测功能。

**[source**]：PVC作为发送端时启动CC信元的发送功能。

【使用指导】

·在配置OAM CC功能时，一端配置为**source**，另一端配置为**sink**。

·启动OAM CC功能后，一端作为接收端启动CC信元的检测功能，一端作为发送端启动CC信元的发送功能。如果检测端3秒内收不到CC信元，PVC状态变为DOWN。当再收到CC信元后，PVC状态变为UP。

【举例】

\# 在ATM接口下的PVC1/32上启动OAM CC功能。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/32

Sysname-ATM2/4/0-pvc-1/32 oam cc sink

\# 在PVC-group2下的PVC1/33上启动OAM CC功能。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 2

Sysname-ATM2/4/0-pvc-group-2 pvc 1/33

Sysname-ATM2/4/0-pvc-group-2-pvc-1/33 oam cc both

**ATM \-- ATM配置命令 \-- oam loopback**

------------------------------------------------------------------------

**[oam loopback**]命令用来启动OAM F5 Loopback信元的发送以及重传检测，同时修改相关参数。**undo oam loopback**命令用来停止OAM F5 Loopback信元的发送以及重传检测。

【命令】

**[oam loopback** *interval* [ **up** *up-count* **down** *down-count* **retry** *retry-interval* ]]

**[undo oam loopback**]

【缺省情况】

不启动OAM F5 Loopback信元的发送，但如果收到OAM F5 Loopback信元，则要进行应答。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：发送OAM F5 Loopback信元的间隔时间，取值范围为1～600，单位为秒。

**[up*** up-count*]：PVC状态转变为UP之前，必须连续正确收到OAM F5 Loopback信元的数量，取值范围为1～600，缺省值为3个。

**[down*** down-count*]：PVC状态转变为DOWN之前，连续未收到的OAM F5 Loopback 信元的数量，取值范围为1～600，缺省值为5个。

**[retry*** retry-interval*]：PVC状态改变前，OAM F5 Loopback在进行重传验证时的信元发送间隔时间，取值范围为1～1000，单位为秒，缺省值为1秒。

【使用指导】

启动OAM F5 Loopback信元的发送以及重传检测功能后，每隔*interval*秒发送OAM F5 Loopback信元。如果发出OAM F5 Loopback信元后在*retry-interval*秒内未正确收到回应信元，则会立即重发OAM F5 Loopback信元。

在OAM F5 Loopback信元的发送以及重传检测过程中根据收发信元情况更新PVC状态：

·如果PVC状态为DOWN，当连续正确收到*up-count*个OAM F5 Loopback信元后，PVC状态转变为UP；

·如果PVC状态为UP，当连续未收到*down-count*个OAM F5 Loopback信元后，PVC状态转变为DOWN。

【举例】

\# 在ATM接口下的PVC1/32上启动OAM F5 Loopback检测，周期为12秒，*up-count*为4，*down-count*为4，重传验证周期为1秒。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/32

Sysname-ATM2/4/0-pvc-1/32 oam loopback 12 up 4 down 4 retry 1

\# 在PVC-group2下的PVC1/33上启动OAM F5 Loopback检测，周期为12秒，*up-count*为4，*down-count*为3，重传验证周期为2秒。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 2

Sysname-ATM2/4/0-pvc-group-2 pvc 1/33

Sysname-ATM2/4/0-pvc-group-2-pvc-1/33 oam loopback 12 up 4 down 3 retry 2

**ATM \-- ATM配置命令 \-- oam ping**

------------------------------------------------------------------------

**[oam ping**]命令用来在指定接口的特定PVC上发送OAM F5 end-to-end信元，检测链路的连接情况。

【命令】

**[oam ping interface ***interface-type*****[{ *interface-number* \| *interface-number.subnumber* } **pvc** { *pvc-name* \| *vpi/vci* } [ *number* *timeout* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-type*[ { *interface-number* \| *interface-number.subnumber* }]]：在指定接口上发送OAM F5 end-to-end信元。支持ATM接口、ATM子接口。

**[pvc**]：在指定PVC上发送OAM F5 end-to-end信元。

*[pvc-name*]：PVC名，长度为1～15个字符的字符串，区分大小写，PVC名中不允许使用"/"和"-"，如"1/20"、"a-b"就不允许作为PVC名。

*[vpi/vci*]：*vpi*为VPI值，取值范围为0～255；*vci*为VCI值，取值范围与接口类型相关，请参见"[表]1-8(?-1864992396#_Ref337389143)"。*vpi*与*vci*不能同时为0。通常，*vci*取值0到31保留用于特定用途，建议用户不要使用。

*[number*]：发送的OAM F5 end-to-end信元的个数，取值范围为1～1000，缺省值为5个。

*[timeout*]：接收OAM F5 end-to-end信元应答的超时时间，取值范围为1～30，单位为秒，缺省值为2秒。

【使用指导】

本命令用来在指定ATM接口的特定PVC上发送OAM F5 end-to-end信元，根据在设定的时间内是否收到应答来判断链路的连接情况。

配置**oam ping**命令后，系统先发送一个OAM F5 end-to-end信元，如果在*timeout*超时前收到应答，则收到应答后系统马上再发送一个OAM F5 end-to-end信元，如果在*timeout*超时时还没有收到应答，则在*timeout*超时后再发送一个OAM F5 end-to-end信元。一次**oam ping**过程中一共发送*number*个OAM F5 end-to-end信元。如果没有收到应答，可能是链路不通，也可能是链路太忙而发生丢包。

【举例】

\# 检测ATM接口2/4/0下PVC1/32的链路状况，发送3个信元，超时时间为1秒。

\<Sysname\> oam ping interface atm 2/4/0 pvc 1/32 3 1

PING interface ATM2/4/0 pvc 1/32 with 3 of 53 bytes of oam F5 end-to-end cell(s),

timeout is 1 second(s), press CTRL_C to break

Receive reply from pvc 1/32: time=1 ms

Receive reply from pvc 1/32: time=1 ms

Receive reply from pvc 1/32: time=1 ms

oam ping statistics:

Cells: Sent = 3, Received = 3, Lost = 0 (0.00% loss)

\# 检测ATM接口2/4/0下PVC 5/100的链路状况，发送3个信元，超时时间为1秒。

\<Sysname\> oam ping interface atm 2/4/0 pvc 5/100 3 1

PING interface ATM2/4/0 pvc 5/100 with 3 of 53 bytes of oam F5 end-to-end cell(s),

timeout is 1 second(s), press CTRL_C to break

Request time out!

Request time out!

Request time out!

oam ping statistics:

Cells: Sent = 3, Received = 0, Lost = 3 (100.00% loss)

表1-7 oam ping命令显示信息描述表

字段

描述

PING interface ATM2/4/0 pvc 1/32

检测ATM2/4/0 pvc 1/32链路是否可达

53 bytes

每个信元的字节数

timeout is 1 second(s)

允许PVC的回应时间为1秒

Receive reply from pvc 1/32: time=1 ms

收到PVC的应答，time表示响应时间

Request time out

在允许的时间内未收到PVC的应答

Sent = 3

发送的信元数

Received = 0

收到的应答数

Lost = 3(100.00% loss)

未响应请求信元数及其占发送的总请求信元数的百分比

**ATM \-- ATM配置命令 \-- precedence**

------------------------------------------------------------------------

**[precedence**]命令用来设置PVC-group中的PVC承载的IP包的优先级。

**[undo precedence**]命令用来删除PVC承载的IP包的优先级设置。

【命令】

**[precedence** { *min* [ **to** *max*  *\|* **default** }]]

**[undo precedence**]

【缺省情况】

不设置优先级。

【视图】

PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[min*]：该PVC承载的IP包的最小优先级，取值范围为0～7。

*[max*]：该PVC承载的IP包的最大优先级，取值范围为0～7。*max*值必须大于等于*min*值。

**[default**]：指定该PVC为缺省PVC。没有指定PVC承载的优先级别的IP包将从缺省PVC进行传输。

【使用指导】

本命令只能对该PVC-group内的PVC进行设置。

·如果没有PVC被**precedence**命令指定**default**参数，则没有指定PVC承载的优先级别的IP包将从未设置优先级的所有PVC轮询地进行传输。

·如果未找到IP包对应优先级别的PVC，而且既没有PVC被**precedence**命令指定**default**参数，也没有未设置优先级的PVC，则该包将做丢弃处理。

需要注意的是，本命令并不能改变IP包的优先级。

【举例】

\# 设置名为"aa"、VPI/VCI为1/32的PVC承载优先级为0～3的IP包。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc aa 1/32

Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/32 precedence 0 to 3

**ATM \-- ATM配置命令 \-- pvc**

------------------------------------------------------------------------

在ATM接口视图、ATM子接口视图下：

**[pvc**]命令用来创建一条PVC并进入PVC视图。如果指定的PVC已创建，则直接进入该PVC的视图。

**[undo pvc**]命令用来删除指定的PVC。

在PVC-group视图下：

**[pvc**]命令用来创建一条属于该PVC-group的PVC并进入PVC视图。如果指定的PVC在PVC-group已经存在，则直接进入该PVC的视图。

**[undo pvc**]命令用来将指定的PVC从PVC-group中退出，并删除该PVC。

【命令】

**[pvc** { *pvc-name* [ *vpi/vci*  \| *vpi/vci* }]]

**[undo pvc**[ { *pvc-name* \| *vpi/vci* }]]

【缺省情况】

没有创建PVC。

【视图】

ATM接口视图/ATM子接口视图/PVC-group视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pvc-name*]：PVC名，长度为1～15个字符的字符串，区分大小写，PVC名中不允许使用"/"和"-"，如"1/20"、"a-b"就不允许作为PVC名。

*[vpi/vci*]：*vpi*为VPI值，取值范围为0～255；*vci*为VCI值，取值范围与接口类型相关，请参见"[表]1-8(?-1864992396#_Ref337389143)"。*vpi*与*vci*不能同时为0。通常，*vci*取值0到31保留用于特定用途，建议用户不要使用。

表1-8 不同接口对应的VCI取值范围

接口类型

VCI取值范围

ATM ADSL

\<0-255\>

ATM ADSL2+

\<0-255\>

ATM G.SHDSL

\<0-255\>

ATM SHDSL_4WIRE

\<0-255\>

ATM SHDSL_4WIRE_BIS

\<0-255\>

ATM SHDSL_8WIRE_BIS

\<0-255\>

ATM E1

\<0-511\>

ATM T1

\<0-511\>

ATM E3

\<0-1023\>

ATM T3

\<0-1023\>

ATM OC-3c/STM-1

\<0-1023\>

ATM OC-12c/STM-4

\<0-1023\>

ATM 25M

\<0-1023\>

ATM子接口

与ATM子接口所属ATM接口的取值范围相同

PVC-group

与PVC-group所属ATM接口的取值范围相同

【使用指导】

·创建PVC时必须指定*vpi/vci*。每条PVC的VPI/VCI值对在一个接口范围内（包括接口和子接口以及它们的PVC-group）唯一。

·如果创建PVC时指定了*pvc-name*，则可以通过命令**pvc** *pvc-name* [ *vpi/vci* ]进入该PVC视图。在删除该PVC时，既可以通过命令**undo pvc** *pvc-name* [ *vpi/vci* ]，也可以通过命令**undo pvc** *vpi/vci*来完成。

·ATM P2P子接口只允许配置一个PVC。

·一个PVC-group下最多允许创建8个PVC。

·在ATM接口/ATM子接口下不能删除PVC-group内的PVC。

·实际可以创建的PVC数量与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 在ATM接口下创建一条名为"aa"、VPI/VCI为1/101的PVC。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc aa 1/101

Sysname-ATM2/4/0-pvc-aa-1/101

\# 在PVC-group下创建一条名为"bb"、VPI/VCI为1/102的PVC。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc bb 1/102

Sysname-ATM2/4/0-pvc-group-1-pvc-bb-1/102

【相关命令】

·**display atm pvc-info**

·**pvc-group**

**ATM \-- ATM配置命令 \-- pvc-group**

------------------------------------------------------------------------

**[pvc-group**]命令用来创建一个PVC-group或进入已经创建的PVC-group视图。

**[undo pvc-group**]命令用来删除指定的PVC-group。

【命令】

**[pvc-group** *group-number*]

**[undo** **pvc-group** *group-number*]

【缺省情况】

没有创建PVC-group。

【视图】

ATM接口视图/ATM子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-number*]：PVC-group编号，取值范围为1～128。

【使用指导】

使用PVC-group后，可以在PVC-group下的各PVC上进行流量的负载分担，将不同优先级的IP包通过不同的PVC进行传输。用户可以配置每条PVC承载的IP包的优先级。

当收到IP包后，根据IP包的优先级来找到对应的PVC进行传输，如果没有找到对应的PVC，则从缺省PVC（**precedence**命令中使用了**default**参数）进行传输，如果没有配置缺省PVC，则从未设置优先级的所有PVC轮询地进行传输。如果没有未设置优先级的PVC，则将该IP包丢弃。

如果收到的不是IP包，则从该PVC-group下所有PVC轮询地进行传输。

PVC-group下的PVC的封装类型、承载的协议类型直接从PVC-group获取。

需要注意的是：

·一个PVC只能属于一个PVC-group。

·本命令可以在ATM P2MP子接口下配置，不能在ATM P2P子接口下配置。

·PVC-group的编号在一个接口范围内（包括接口和子接口）唯一。

【举例】

\# 创建一个编号为1的PVC-group。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1

【相关命令】

·**display atm pvc-group**

·**precedence**

**ATM \-- ATM配置命令 \-- remark atm-clp**

------------------------------------------------------------------------

**[remark atm-clp**]命令用来重新标记ATM信元的CLP标志位的值。

**[undo remark atm-clp**]命令用来取消重新标记ATM信元的CLP标志位的值。

【命令】

**[remark**[ [ **green** \| **red** \| **yellow** ] **atm-clp** *atm-clp-value*]]

**[undo remark**[ [ **green** \| **red** \| **yellow** ] **atm-clp**]]

【缺省情况】

没有配置重新标记ATM信元的CLP标志位的值。

【视图】

流行为视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[green**]：对绿色报文进行重新标记。

**[red**]：对红色报文进行重新标记。

**[yellow**]：对黄色报文进行重新标记。

*[atm-clp-value*]：ATM信元CLP（Cell Loss Priority，信元丢失优先级）标志位的值，取值为0或1。发生拥塞时优先丢弃CLP为1的信元。

【使用指导】

配置了该特性的策略只能应用在ATM PVC出方向上。

【举例】

\# 重新标记ATM信元的CLP标志位的值为1。

\<Sysname\> system-view

Sysname traffic behavior database

Sysname-behavior-database remark atm-clp 1

**ATM \-- ATM配置命令 \-- reset atm interface**

------------------------------------------------------------------------

**[reset atm interface**]命令用来清除PVC的统计信息。

【命令】

**[reset atm interface**[ [ *interface-type* { *interface-number* \| *interface-number.subnumber* } ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type *[{ *interface-number* \| *interface-number.subnumber* }]]：清除指定接口下的所有PVC（包括接口下的PVC和PVC-group下的PVC）的统计信息。支持ATM接口、ATM子接口。不指定本参数时，将清除所有接口下的所有PVC的统计信息。

【使用指导】

本命令只能清除PVC的统计信息，不能清除接口的统计信息，接口的统计信息可以通过**reset counters interface**命令来清除。

【举例】

\# 清除接口ATM2/4/0下的所有PVC的统计信息。

\<Sysname\> reset atm interface atm 2/4/0

**ATM \-- ATM配置命令 \-- reset counters interface virtual-ethernet**

------------------------------------------------------------------------

**[reset counters interface virtual-ethernet**]命令用来清除VE接口的统计信息。

【命令】

**[reset counters interface** [ **virtual-ethernet** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[virtual-ethernet**]：清除VE接口的统计信息。

*[interface-number*]：VE接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**virtual-ethernet**参数，则清除所有接口的统计信息；

·如果指定**virtual-ethernet**参数而不指定*interface-number*，则清除所有VE接口的统计信息；

·如果同时指定**virtual-ethernet**和*interface-number*，则清除指定VE接口的统计信息。

【举例】

\# 清除VE接口Virtual-Ethernet2/4/2的统计信息。

\<Sysname\> reset counters interface virtual-ethernet 2/4/2

**ATM \-- ATM配置命令 \-- service cbr**

------------------------------------------------------------------------

**[service** **cbr**]命令用来指定PVC的服务类型为CBR（Constant Bit Rate，恒定速率），并指定相关的服务参数。

**[undo service**]命令用来恢复缺省情况。

【命令】

**[service** **cbr** *output-pcr* [ **cdvt** *cdvt_value* ]]

**[undo service**]

【缺省情况】

创建一个PVC后，该PVC的服务类型为UBR，输出ATM信元的峰值速率为PVC所在接口的最大带宽。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[output-pcr*]：输出ATM信元的峰值速率，不同接口的*output-pcr*取值范围请参见[表]1-9(?1437517977#_Ref57606154)，单位为Kbit/s。

表1-9 *output-pcr*的取值范围

接口类型

output-pcr取值范围

ATM ADSL

\<64-640\>

ATM ADSL2+

\<64-640\>

ATM G.SHDSL

\<64-2312\>

ATM SHDSL_4WIRE

\<128-4624\>

ATM SHDSL_4WIRE_BIS

\<128-11392\>

ATM SHDSL_8WIRE_BIS

\<256-22784\>

ATM E1

\<64-1920\>

ATM T1

\<64-1536\>

ATM E3

\<64-34000\>

ATM T3

\<64-44000\>

ATM OC-3c/STM-1

\<64-155000\>

ATM OC-12c/STM-4

不支持

ATM 25M

不支持

ATM子接口

与ATM子接口所属ATM接口的取值范围相同

PVC-group

与PVC-group所属ATM接口的取值范围相同

**[cdvt ***cdvt_value*]：信元时延变化容限（Cell Delay Variation Tolerance），取值范围为0～10000，单位为μs，缺省值为500μs，表示信元的最大时延是500μs。设置该参数后，当超出峰值速率后，会根据该参数分配缓存，保证业务的稳定。该参数的值配置的越小，要求的硬件资源越多，越不容易配置成功。若配置不成功，可将*cdvt_value*的值调大，再试着配置，此情况会在命令行中给出提示（Failed to set service parameter. Please adjust cdvt value.）

【使用指导】

可以使用本命令以及**service ubr**、**service** **vbr-nrt**，**service** **vbr-rt**命令来设置PVC的服务类型和服务参数。新指定的PVC服务类型将会覆盖已有的服务类型。

因为每个PVC的带宽是独占的，所以建议在设置CBR带宽时先设置需要大带宽的PVC，再设置需要小带宽的PVC。

本命令不支持ATM E1接口和ATM E3接口。

【举例】

\# 在ATM接口下创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为CBR，ATM信元峰值发送速率为50,000Kbit/s，信元时延变化容限为1000μs。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc aa 1/101

Sysname-ATM2/4/0-pvc-aa-1/101 service cbr 50000 cdvt 1000

\# 在PVC-group1下创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为CBR，ATM信元峰值发送速率为50,000Kbit/s，信元时延变化容限为1000μs。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc aa 1/101

Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101 service cbr 50000 cdvt 1000

【相关命令】

·**service ubr**

·**service vbr-nrt**

·**service vbr-rt**

**ATM \-- ATM配置命令 \-- service ubr**

------------------------------------------------------------------------

**[service** **ubr**]命令用来指定PVC的服务类型为UBR（Unspecified Bit Rate，非确定速率），并指定相关的服务参数。

**[undo service**]命令用来恢复缺省情况。

【命令】

**[service** **ubr** *output-pcr*]

**[undo service**]

【缺省情况】

创建一个PVC后，该PVC的服务类型为UBR，输出ATM信元的峰值速率为PVC所在接口的最大带宽。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[output-pcr*]：输出ATM信元的峰值速率，取值范围请参见[表]1-9(?1437517977#_Ref57606154)，单位为Kbit/s。

【使用指导】

可以使用本命令以及**service** **cbr**、**service** **vbr-nrt**、**service** **vbr-rt**命令来设置PVC的服务类型和服务参数。新指定的PVC服务类型将会覆盖已有的服务类型。

【举例】

\# 在ATM接口下创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为UBR，ATM信元峰值发送速率为100,000Kbit/s。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc aa 1/101

Sysname-ATM2/4/0-pvc-aa-1/101 service ubr 100000

\# 在PVC-group1下创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为UBR，ATM信元峰值发送速率为100,000Kbit/s。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc aa 1/101

Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101 service ubr 100000

【相关命令】

·**service** **cbr**

·**service vbr-nrt**

·**service vbr-rt**

**ATM \-- ATM配置命令 \-- service vbr-nrt**

------------------------------------------------------------------------

**[service** **vbr-nrt**]命令用来指定PVC的服务类型为VBR-NRT（Variable Bit Rate-Non Real Time，非实时可变速率），并指定相关的服务参数。

**[undo service**]命令用来恢复缺省情况。

【命令】

**[service** **vbr-nrt** *output-pcr output-scr output-mbs*]

**[undo service**]

【缺省情况】

创建一个PVC后，该PVC的服务类型为UBR，输出ATM信元的峰值速率为PVC所在接口的最大带宽。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[output-pcr*]：输出ATM信元的峰值速率，取值范围请参见[表]1-9(?1437517977#_Ref57606154)，单位为Kbit/s。

*[output-scr*]：输出ATM信元的可承受速率，取值范围与*output-pcr*相同，并且*output-scr*小于等于*output-pcr*，单位为Kbit/s。

*[output-mbs*]：输出ATM信元的最大突发长度，即接口输出ATM信元的最大缓冲数量，取值范围为1～512，单位为信元数。

【使用指导】

可以使用本命令以及**service** **cbr**、**service** **ubr**、**service** **vbr-rt**命令来设置PVC的服务类型和服务参数。新指定的PVC服务类型将会覆盖已有的服务类型。

【举例】

\# 在ATM接口下创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为VBR-NRT，且ATM信元峰值发送速率为100,000Kbit/s、可承受发送速率为50,000Kbit/s、最大突发长度为320个信元。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc aa 1/101

Sysname-ATM2/4/0-pvc-aa-1/101 service vbr-nrt 100000 50000 320

\# 在PVC-group  1下 创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为VBR-NRT，且ATM信元峰值发送速率为100,000Kbit/s、可承受发送速率为50,000Kbit/s、最大突发长度为320个信元。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc aa 1/101

Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101 service vbr-nrt 100000 50000 320

【相关命令】

·**service** **cbr**

·**service** **ubr**

·**service** **vbr-rt**

**ATM \-- ATM配置命令 \-- service vbr-rt**

------------------------------------------------------------------------

**[service** **vbr-rt**]命令用来指定PVC的服务类型为VBR-RT（Variable Bit Rate-Real Time，实时可变速率），并指定相关的服务参数。

**[undo service**]命令用来恢复缺省情况。

【命令】

**[service** **vbr-rt** *output-pcr output-scr output-mbs*]

**[undo service**]

【缺省情况】

创建一个PVC后，该PVC的服务类型为UBR，输出ATM信元的峰值速率为PVC所在接口的最大带宽。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[output-pcr*]：输出ATM信元的峰值速率，取值范围请参见[表]1-9(?1437517977#_Ref57606154)，单位为Kbit/s。

*[output-scr*]：输出ATM信元的可承受速率，取值范围与*output-pcr*相同，并且*output-scr*小于等于*output-pcr*，单位为Kbit/s。

*[output-mbs*]：输出ATM信元的最大突发长度，即接口输出ATM信元的最大缓冲数量，取值范围为1～512，单位为信元数。用于ATM E3接口时，该参数的取值范围也为1～512。

【使用指导】

可以使用本命令以及**service** **cbr**、**service** **ubr**、**service** **vbr-nrt**命令来设置PVC的服务类型和服务参数。新指定的PVC服务类型将会覆盖已有的服务类型。

本命令不支持ATM E1接口。

【举例】

\# 在ATM接口下创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为VBR-RT，且ATM信元峰值发送速率为100,000Kbit/s、可承受发送速率为50,000Kbit/s、最大突发长度为320个信元。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc aa 1/101

Sysname-ATM2/4/0-pvc-aa-1/101 service vbr-rt 100000 50000 320

\# 在PVC-group1下创建一条名为"aa"、VPI/VCI为1/101的PVC，并指定该PVC的服务类型为VBR-RT，且ATM信元峰值发送速率为100,000Kbit/s、可承受发送速率为50,000Kbit/s、最大突发长度为320个信元。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc aa 1/101

Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101 service vbr-rt 100000 50000 320

【相关命令】

·**service cbr**

·**service ubr**

·**service vbr-nrt**

**ATM \-- ATM配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于打开状态。

【视图】

VE接口视图/VE子接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭VE接口Virtual-Ethernet2/4/1。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/1

Sysname-Virtual-Ethernet2/4/1 shutdown

**ATM \-- ATM配置命令 \-- shutdown**

------------------------------------------------------------------------

![说明](ATM命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[shutdown**]命令用来关闭当前PVC。

**[undo shutdown**]命令用来打开当前PVC。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

PVC处于打开状态。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 打开ATM接口下PVC0/100。

\<Sysname\> system-view

Sysname interface atm 2/4/0.1

Sysname-ATM2/4/0.1 pvc 0/100

Sysname-ATM2/4/0.1-pvc-0/100 undo shutdown

\# 打开PVC-group1下PVC1/101。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc aa 1/101

Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101 undo shutdown

**ATM \-- ATM配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

![说明](ATM命令.files/image002.jpg)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·开启本功能后可能需要耗费大量系统资源，请谨慎使用。

****

**[sub-interface rate-statistic**]命令用来开启VE子接口的速率统计功能。

**[undo sub-interface rate-statistic**]命令用来关闭VE子接口的速率统计功能。

【命令】

**[sub-interface rate-statistic**]

**[undo sub-interface rate-statistic**]

【缺省情况】

VE子接口的速率统计功能处于关闭状态。

【视图】

VE接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启接口VE2/4/0的子接口速率统计功能。

\<Sysname\> system-view

Sysname interface virtual-ethernet 2/4/0

Sysname-Virtual-Ethernet2/4/0 sub-interface rate-statistic

**ATM \-- ATM配置命令 \-- transmit-priority**

------------------------------------------------------------------------

**[transmit-priority**]命令用来配置UBR、VBR-NRT、VBR-RT服务下的PVC的传输优先级。

**[undo transmit-priority**]命令用来按照PVC服务类型恢复对应的缺省传输优先级。

【命令】

**[transmit-priority** *value*]

**[undo** **transmit-priority**]

【缺省情况】

UBR服务的传输优先级为0；VBR-NRT服务的传输优先级为5；VBR-RT服务的传输优先级为8。

【视图】

PVC视图/PVC-group下PVC视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：传输优先级，取值范围为0～9，数值大的优先级高。UBR服务的传输优先级取值范围是0～4；VBR-NRT服务的传输优先级取值范围是5～7；VBR-RT服务的传输优先级取值范围是8～9。

【使用指导】

传输优先级高的PVC优先占有带宽，相同传输优先级的PVC占有相同的带宽。

当改变PVC的服务类型时，传输优先级变为当前服务的缺省值。

【举例】

\# 配置ATM接口下PVC1/32的传输优先级为3。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc 1/32

Sysname-ATM2/4/0-pvc-1/32 transmit-priority 3

\# 配置PVC-group1下PVC1/101的传输优先级为4。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 pvc-group 1

Sysname-ATM2/4/0-pvc-group-1 pvc aa 1/101

Sysname-ATM2/4/0-pvc-group-1-pvc-aa-1/101 transmit-priority 4

**ATM \-- ATM配置命令 \-- vp limit**

------------------------------------------------------------------------

**[vp limit**]命令用来配置VP监管的参数。

**[undo vp limit**]命令用来取消VP监管。

【命令】

**[vp limit** *vpi* *scr*]

**[undo vp limit** *vpi*]

【缺省情况】

不进行VP监管。

【视图】

ATM接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpi*]：VPI值，取值范围为0～255。

*[scr*]：可承受速率，取值范围请参见[表]1-9(?1437517977#_Ref57606154)，单位为Kbit/s。

【使用指导】

VP是具有相同VPI的所有PVC的集合，VP监管用来管理VP的最大带宽，对一个物理接口下的虚通道（VP）流量进行入方向、出方向的监管，即保证VP的最大传输速率不能超过设定值，超出的流量将被丢弃。在应用VP监管时，PVC的参数仍然有效，只有满足PVC的参数与VP监管的参数时，分组才会被接收或发送。在计算流量时，已经包括了LLC/SNAP、MUX和NLPID封装头部，但不包括ATM信元头。

【举例】

\# 配置VPI为1的VP的流量为2Mbit/s。

\<Sysname\> system-view

Sysname interface atm 2/4/0

Sysname-ATM2/4/0 vp limit 1 2000

【相关命令】

·**service cbr**

·**service ubr**

·**service vbr-nrt**

·**service vbr-rt**
