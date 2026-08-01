<!-- CMD-INDEX
  alarm-detect                        | POS接口视图          | L34
  bandwidth                           | POS接口视图/POS子接口视图/POS通道接口视图 | L100
  clock                               | POS接口视图          | L146
  crc                                 | POS接口视图/POS通道接口视图 | L200
  dampening                           | POS接口视图          | L248
  default                             | POS接口视图/POS子接口视图/POS通道接口视图 | L326
  description                         | POS接口视图/POS子接口视图/POS通道接口视图 | L362
  display interface pos               | 任意视图             | L404
  flag c2                             | POS接口视图/POS通道接口视图 | L802
  flag j0                             | POS接口视图          | L854
  flag j1                             | POS接口视图/POS通道接口视图 | L912
  flag j1 ignore                      | POS接口视图/POS通道接口视图 | L972
  flow-interval                       | 系统视图/POS接口视图/POS子接口视图/POS通道接口视图 | L1018
  frame-format                        | POS接口视图          | L1076
  interface pos                       | 系统视图             | L1130
  link-delay                          | POS接口视图/POS通道接口视图 | L1186
  link-protocol                       | POS接口视图/POS通道接口视图 | L1246
  loopback                            | POS接口视图          | L1288
  mtu                                 | POS接口视图/POS子接口视图/POS通道接口视图 | L1344
  port-type switch                    | POS接口视图/三层GE接口视图 | L1392
  reset counters interface            | 用户视图             | L1448
  scramble                            | POS接口视图/POS通道接口视图 | L1496
  shutdown                            | POS接口视图/POS子接口视图/POS通道接口视图 | L1538
  snmp-agent trap enable { b1-tca \| b2-tca \| b3-tca } | POS接口视图          | L1576
  speed                               | POS接口视图          | L1636
  sub-interface rate-statistic        | POS接口视图/POS通道接口视图 | L1678
  threshold                           | POS接口视图          | L1730
  threshold { b1-tca \| b2-tca \| b3-tca } | POS接口视图          | L1786
  timer-hold                          | POS接口视图/POS通道接口视图 | L1854
  timer-hold retry                    | POS接口视图/POS通道接口视图 | L1906
-->

**POS接口 \-- POS接口配置命令 \-- alarm-detect**

------------------------------------------------------------------------

![说明](POS接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[alarm-detect**]命令用来设置当前接口的告警联动动作。

**[undo alarm-detect**]命令用来取消告警联动动作。

【命令】

**[alarm-detect**[ { **rdi** \| **sd** \| **sf** } **action** **link-down**]]

**[undo alarm-detect**[ { **rdi** \| **sd** \| **sf** }]]

【缺省情况】

接口不执行任何告警联动动作。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rdi**]：表示RDI（Remote Defect Indication，远端失效指示）告警。

**[sd**]：表示SD（Signal Degrade，信号衰减）告警。

**[sf**]：表示SF（Signal Fail，信号失败）告警。

**[action**]：设置当接口检测到告警时的联动动作。

**[link-down**]：表示自动将接口的物理状态设置为down。

【使用指导】

当设备收到对端发送的MS-RDI信号时，则认为发生了RDI告警。当设备收到的报文的误码率达到或超过设置的门限时，则生成SD告警或SF告警。SD告警和SF告警的门限可通过**threshold**命令设置。

配置本命令后，当设备检测到告警时，会自动将接口的物理状态设置为down。

【举例】

\# 配置当POS接口2/2/0检测到SD告警时，自动将接口的物理状态设置为down。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 alarm-detect sd action link-down

【相关命令】

·**threshold**

**POS接口 \-- POS接口配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

POS接口视图/POS子接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 设置POS接口2/2/0的期望带宽为50kbit/s。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 bandwidth 50

**POS接口 \-- POS接口配置命令 \-- clock**

------------------------------------------------------------------------

**[clock**]命令用来设置POS接口的时钟模式。

**[undo clock**]命令用来恢复缺省情况。

【命令】

**[clock**[ { **master** \| **slave** }]]

**[undo clock**]

【缺省情况】

POS接口的时钟模式为从时钟模式（**slave**）。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：设置POS接口的时钟模式为主时钟模式。

**[slave**]：设置POS接口的时钟模式为从时钟模式。

【使用指导】

POS接口支持两种时钟模式：

·**master**：主时钟模式，使用内部时钟信号；

·**slave**：从时钟模式，使用线路提供的时钟信号。

与同步串口有DTE和DCE两种工作方式相仿，POS也需要选择时钟模式。当两台路由器的POS接口直接相连时，应配置一端使用主时钟模式，另一端使用从时钟模式；当与SONET/SDH设备相连时，由于SONET/SDH网络的时钟精度高于POS本身内部时钟源的精度，应配置POS接口使用从时钟模式。

【举例】

\# 设置POS接口2/2/0使用主时钟模式。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 clock master

**POS接口 \-- POS接口配置命令 \-- crc**

------------------------------------------------------------------------

**[crc**]命令用来设定接口的CRC校验字长度。

**[undo crc**]命令用来恢复缺省情况。

【命令】

**[crc**[ { **16** \| **32** }]]

**[undo** **crc**]

【缺省情况】

CRC校验字长度为32比特。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[16**]：CRC校验字长度为16比特。

**[32**]：CRC校验字长度为32比特。

【使用指导】

设置接口的CRC校验字长度时，注意两端设备应保持一致。

【举例】

\# 设置POS接口2/2/0的CRC校验字长度为16比特。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 crc 16

**POS接口 \-- POS接口配置命令 \-- dampening**

------------------------------------------------------------------------

**[dampening**]命令用来开启接口的dampening功能。

**[undo dampening**]命令用来关闭接口的dampening功能。

【命令】

**[dampening** [ *half-life* *reuse suppress max-suppress-time* ]]

**[undo dampening**]

【缺省情况】

接口的dampening功能处于关闭状态。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[half-life*]：半衰期，取值范围为1～120，单位为秒，缺省值为54秒。

*[reuse*]：启用门限，取值范围为200～20000，缺省值为750，*reuse*的值必须小于*suppress*的值。

*[suppress*]：抑制门限，取值范围为200～20000，缺省值为2000。

*[max-suppress-time*]：最大抑制时间，取值范围为1～255，单位为秒，缺省值为半衰期的3倍，即162秒。

【使用指导】

接口有两种物理连接状态：up和down。由于线缆故障、接口连接或链路层配置错误等问题，可能会导致设备接口的状态频繁的在down和up之间切换，这种现象称为接口震荡。随着接口状态的频繁改变，设备会不停的刷新相关表项（比如路由表），消耗大量的系统资源。通过在接口上配置dampening功能，可以在一定条件下，屏蔽该接口的震荡对路由等上层业务的影响。此时若出现接口震荡，将不上送CPU处理，仅产生对应的Trap和Log信息，从而节省系统资源的消耗。

dampening功能的工作原理如下：

·开启dampening功能后，接口将关联一个惩罚值，初始值是0。接口状态每次从up变到down时，惩罚值会增加1000（接口状态从down变到up时，惩罚值不变）。同时，惩罚值随着时间的推移自动减少，满足半衰期衰减规律：完全衰减时（即假如在此期间没有再发生接口震荡），经过一个半衰期，惩罚值将减少为原来值的一半。

·当惩罚值大于或等于抑制门限时，开始抑制接口：不上送CPU处理接口状态变化，仅产生对应的Trap和Log信息。当惩罚值小于或等于启用门限时，不抑制接口：上送CPU处理接口状态变化，同时发送对应的Trap和Log信息。

·当惩罚值达到最大惩罚值后，惩罚值将不再增加。最大惩罚值不可配，其值与最大抑制时间、半衰期、启用门限之间的关系遵循如下公式：最大惩罚值＝2^(^^最大抑制时间/半衰期)^×启用值。

·每次接口进入抑制状态后，当接口持续抑制的时间超过最大抑制时间时，且此时惩罚值大于启用门限时，惩罚值将不再增加，此时惩罚值进入完全半衰期（此阶段接口状态变化不会增加惩罚值），直到惩罚值小于启用门限，不再抑制接口（完全半衰期中，接口仍然处于抑制状态，但完全半衰阶段时间不算入持续抑制时间）。

·如果接口抑制时间不到最大抑制时间，惩罚值就小于启用门限，那么不存在完全半衰过程（持续抑制时间超过最大抑制时间才会进入）

需要注意的是：

·本命令和**link-delay**命令不能同时使用。

·本命令对使用**shutdown**命令手工关闭的接口无效。接口被关闭时，惩罚值恢复为初始值0。

·处于抑制期时产生的接口up事件，通过**display interface pos**命令、MIB网管或Web网管等方式查看到时，接口状态仍然为down。

【举例】

\# 开启POS接口2/2/0的dampening功能，配置半衰期为2秒，启用门限为800，抑制门限为3000，最大抑制时间为5秒。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 dampening 2 800 3000 5

【相关命令】

·**display interface pos**

·**link-delay**

**POS接口 \-- POS接口配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

POS接口视图/POS子接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将POS接口2/2/0恢复为缺省配置。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 default

**POS接口 \-- POS接口配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Pos2/2/0 Interface。

【视图】

POS接口视图/POS子接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置接口POS2/2/0的描述信息为"pos-interface"。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 description pos-interface

**POS接口 \-- POS接口配置命令 \-- display interface pos**

------------------------------------------------------------------------

**[display interface pos**]命令用来显示POS接口、POS子接口、POS通道接口的相关信息。

【命令】

**[display interface**[ [ **pos** [ *interface-number* \| *interface-number.subnumber* ]   **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定POS接口、POS通道接口的信息。*interface-number*表示POS接口、POS通道接口的编号。

*[interface-number.subnumber*]：显示指定POS子接口的信息。*interface-number.subnumber*表示POS子接口编号，其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为0～1023。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**pos**参数，将显示设备支持的所有接口的相关信息。

·如果指定**pos**参数，不指定接口编号，将显示所有已创建的POS接口、POS子接口、POS通道接口的相关信息。

【举例】

\# 显示POS接口2/2/0的详细信息。

\<Sysname\> display interface pos 2/2/0

Pos2/2/0

Current state: DOWN

Line protocol state: DOWN

Description: Pos5/1 Interface

Bandwidth: 50kbps

Maximum Transmit Unit: 1500

Dampening enabled:

 Penalty: 0 (not suppressed)

 Ceiling: 4525

 Reuse: 800

 Suppress: 3000

 Half-life: 2 seconds

 Max-suppress-time: 5 seconds

 Flap count: 0

Hold timer: 10 seconds, retry times: 5

Internet Address: 5.5.5.2/24 Primary

Link layer protocol: PPP

LCP: opened, IPCP: opened

Physical layer: Packet Over SONET, Baudrate: 155520000 bps

Scramble: enabled, crc: 32, clock: slave, loopback: not set

SONET alarm:

  section layer: OOF LOF LOS

  line    layer: AIS

  path    layer: AIS RDI

  C2(Rx): 0xff, C2(Tx): 0x16

  J0(Rx): unknown

  J0(Tx): \"\"

  J1(Rx): unknown

  J1(Tx): \"\"

SONET error:

  section layer: B1 65535

  line    layer: B2 0 M1 0

  path    layer: B3 0 G1 0

Last link flapping: 6 hours 39 minutes 25 seconds

Last clearing of counters: Never

Last 300 seconds input rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec

Last 300 seconds output rate: 0.00 bytes/sec, 0 bits/sec, 0.00 packets/sec

Input:

  0 packets, 0 bytes

  0 errors, 0 runts, 0 giants, 0 CRC

  0 overruns, 0 aborts, 0 no buffers

Output:

  0 packets, 0 bytes

  0 errors, 0 underruns, 0 aborts

\# 显示POS接口2/2/0的概要信息。

\<Sysname\> display interface pos 2/2/0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Pos2/2/0             UP   UP(s)    \--

\# 显示当前物理状态为down的POS接口、POS子接口、POS通道接口的信息以及down的原因。

\<Sysname\> display interface pos brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Pos2/2/0             ADM  Administratively

表1-1 display interface pos命令显示信息描述表

字段

描述

Pos2/2/0

Current state

该接口当前的物理状态和管理状态，可能的状态及含义如下：

·DOWN（Administratively）：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

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

Dampening enabled:

 Penalty: 0 (not suppressed)

 Ceiling: 4525

 Reuse: 800

 Suppress: 3000

 Half-life: 2 seconds

 Max-suppress-time: 5 seconds

 Flap count: 0

该接口的dampening抑制信息，该显示信息的支持情况与用户的配置以及设备型号有关，请以设备的实际情况为准（若未使能dampening功能，则不会显示该段信息）：

·Dampening enabled：已使能dampening功能

·Penalty：惩罚值（若接口处于抑制期，则在惩罚值后标识suppressed；反之，在惩罚值后标识not suppressed）

·Ceiling：最大惩罚值

·Reuse：启用门限

·Suppress：抑制门限

·Half-life：半衰期

·Max-suppress-time：最大抑制时间

·Flap count：接口震荡发生的次数

 

Hold timer

该接口发送keepalive报文的周期

retry times

在多少个keepalive周期内没有收到keepalive报文的应答就拆除链路

Internet Address

该接口网络地址

Link layer protocol

该接口的链路层封装的协议

LCP: opened, IPCP: opened

表示LCP和IPCP都协商成功

Physical layer

物理接口

Baudrate

接口的波特率

Scramble

该接口是否开启对载荷数据的加扰功能

crc

该接口的CRC校验字长度

clock

该接口的时钟模式

loopback

该接口是否开启环回功能

SONET alarm

SONET告警信息

SONET error

SONET错误信息

Last link flapping

接口最近一次物理状态改变到现在的时长。Never表示接口从设备启动后一直处于down状态（没有改变过）

Last clearing of counters

最近一次清除计数的时间

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，bits/sec表示平均每秒输入的比特数，packets/sec表示平均每秒输入的报文数

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数，bits/sec表示平均每秒输出的比特数，packets/sec表示平均每秒输出的报文数

Input:

  0 packets, 0 bytes

  0 errors, 0 runts, 0 giants, 0 CRC

  0 overruns, 0 aborts, 0 no buffers

接口收到的总报文数和总字节数：

·errors：在物理层检测时发现的错误报文数目

·runts：接口接收到小于规定的最小报文长度报文数

·giants：接收到长度大于规定长度的报文数目

·CRC：接收长度正常但CRC校验错误的报文数目

·overruns：接收的报文速度大于转发处理能力导致无法处理的报文

·aborts：接收报文的异常错误

·no buffers：在接收报文时由于内部缓存满，导致帧丢弃

Output:

  0 packets, 0 bytes

  0 errors, 0 underruns, 0 aborts

接口发送的报文数和总字节数

·errors：在物理层检测时发现的错误报文数目

·underruns：因为接口读取内存的速度小于转发的速度而无法发送报文数目

·aborts：发送报文的异常错误

Brief information on interface(s) under route mode:

三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

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

【相关命令】

·**reset counters interface**

**POS接口 \-- POS接口配置命令 \-- flag c2**

------------------------------------------------------------------------

**[flag**]**c2**命令用来配置信号标记字节C2。

**[undo flag**]**c2**命令用来恢复缺省情况。

【命令】

**[flag**] **c2** *flag-value*

**[undo flag c2**]

【缺省情况】

信号标记字节C2的值为0x16。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[flag-value*]：信号标记字节C2，取值范围为0x00～0xFF。

【使用指导】

信号标记字节C2属于高阶通道开销字节，用于指示虚拟容器VC（Virtual Container）帧的复接结构和信息净负荷的性质。

C2字节的设置一定要使收/发两端相匹配，否则会产生告警。

【举例】

\# 配置POS接口2/2/0的信号标记字节C2为0x01。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 flag c2 01

【相关命令】

·**display interface pos**

**POS接口 \-- POS接口配置命令 \-- flag j0**

------------------------------------------------------------------------

**[flag**]**j0**命令用来配置SONET/SDH帧的再生段踪迹字节J0。

**[undo flag**]**j0**命令用来恢复缺省情况。

【命令】

**[flag**  **j0** { **sdh** \| **sonet** } *flag-value*]

**[undo flag j0**  { **sdh** \| **sonet** }]

【缺省情况】

系统使用SDH帧格式的缺省值，SDH帧格式下再生段踪迹字节J0的缺省值为空。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[flag-value*]：再生段踪迹字节J0。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为0x00～0xFF。

**[sdh**]：帧格式为SDH（Synchronous Digital Hierarchy，同步数字系列）。

**[sonet**]：帧格式为SONET（Synchronous Optical Network，同步光网络）。

【使用指导】

再生段踪迹字节J0属于段开销字节（Section Overhead），用于检测两个接口之间的连接在段层次上的连续性。

在同一个运营者的网络内J0字节可为任意字符，而在两个不同运营者的网络边界处要使设备收、发两端的J0字节相匹配。

【举例】

\# 配置POS接口2/2/0的SDH帧的再生段踪迹字节J0为0xFF。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 flag j0 sdh ff

【相关命令】

·**display interface pos**

·**frame-format**

**POS接口 \-- POS接口配置命令 \-- flag j1**

------------------------------------------------------------------------

**[flag**]**j1**命令用来配置SONET/SDH帧的通道踪迹字节J1。

**[undo flag**]**j1**命令用来恢复缺省情况。

【命令】

**[flag**  **j1** { **sdh** \| **sonet** } *flag-value*]

**[undo flag**  **j1** { **sdh** \| **sonet** }]

【缺省情况】

系统使用SDH帧格式的缺省值，SDH帧格式下通道踪迹字节J1的缺省值为空。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[flag-value*]：通道踪迹字节J1。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为1～62个字符的字符串。

**[sdh**]：帧格式为SDH。

**[sonet**]：帧格式为SONET。

【使用指导】

通道踪迹字节J1属于高阶通道开销字节，用于检测两个接口之间的连接在通道层次上的连续性。

J1字节的设置一定要使收/发两端相匹配，否则会产生告警。

【举例】

\# 配置POS接口2/2/0的SDH帧的通道踪迹字节J1为aabbcc。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 flag j1 sdh aabbcc

【相关命令】

·**display interface pos**

·**flag j1 ignore**

·**frame-format**

**POS接口 \-- POS接口配置命令 \-- flag j1 ignore**

------------------------------------------------------------------------

![说明](POS接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flag j1 ignore**]命令用来配置忽略对通道踪迹字节J1的检查。

**[undo flag j1 ignore**]命令用来恢复缺省情况。

【命令】

**[flag j1 ignore**]

**[undo flag j1 ignore**]

【缺省情况】

需要对通道踪迹字节J1进行检查。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置POS接口2/2/0忽略对通道踪迹字节J1的检查。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 flag j1 ignore

【相关命令】

·**flag**** j1**

**POS接口 \-- POS接口配置命令 \-- flow-interval**

------------------------------------------------------------------------

![说明](POS接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flow-interval**]命令用来配置接口统计报文信息的时间间隔。

**[undo flow-interval**]命令用来恢复缺省情况。

【命令】

**[flow-interval ***interval*]

**[undo flow-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图/POS接口视图/POS子接口视图/POS通道接口视图

![说明](POS接口命令.files/image002.png)

不同设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：接口统计信息的时间间隔值，取值范围为5～300，单位为秒，步长为5（即取值必须为5的整数倍）。

【使用指导】

用户可以配置接口统计报文信息的时间间隔：

·系统视图下的配置对所有接口生效；

·接口视图下的配置只对当前接口生效。

【举例】

\# 配置POS接口2/2/0的统计信息时间间隔为180秒。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 flow-interval 180

**POS接口 \-- POS接口配置命令 \-- frame-format**

------------------------------------------------------------------------

**[frame-format**]命令用来设定POS接口的帧格式。

**[undo frame-format**]命令用来恢复缺省情况。

【命令】

**[frame-format**  { **sdh** \| **sonet** }]

**[undo**] **frame-format**

【缺省情况】

帧格式为SDH。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sdh**]：帧格式为SDH。

**[sonet**]：帧格式为SONET。

【使用指导】

通过**flag j0**和**flag****j1**命令设置开销字节时，需要与帧格式匹配。

【举例】

\# 设置POS接口2/2/0的帧格式为SONET。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 frame-format sonet

【相关命令】

·**flag****j0**

·**flag****j1**

**POS接口 \-- POS接口配置命令 \-- interface pos**

------------------------------------------------------------------------

**[interface pos**]命令用来进入POS接口、POS子接口、POS通道接口视图。在进入POS子接口视图之前，如果指定的POS子接口不存在，则先创建POS子接口，再进入该POS子接口的视图。

**[undo interface pos**]命令用来删除POS子接口。

【命令】

**[interface pos**[ { *interface-number* \| *interface-number.subnumber* [ **p2mp** \| **p2p** ] }]]

**[undo interface pos** *interface-number.subnumber*]

【缺省情况】

不存在POS子接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：POS接口、POS通道接口的编号。

*[interface-number.subnumber*]：POS子接口编号，其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为0～1023。

**[p2mp**]：点到多点子接口。子接口缺省为**p2mp**类型。

**[p2p**]：点到点子接口。

【使用指导】

只有POS主接口上封装的链路层协议为FR时，才能创建子接口。

【举例】

\# 创建POS子接口POS2/2/0.1。

\<Sysname\> system-view

Sysname interface pos 2/2/0.1

Sysname-Pos2/2/0.1

【相关命令】

·**link-protocol**

**POS接口 \-- POS接口配置命令 \-- link-delay**

------------------------------------------------------------------------

![说明](POS接口命令.files/image003.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-delay**]命令用来设置接口物理连接状态抑制时间，即在接口发生up或down的时候，需要经过连接状态抑制时间后，接口状态才能变为up或down。

**[undo link-delay**]命令用来恢复缺省情况。

【命令】

**[link-delay msec ***milliseconds*]

**[undo link-delay**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[msec ***milliseconds*]：接口物理连接状态抑制时间，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

使用该命令可以防止短时间内的接口物理连接状态变化对正常业务的影响。

需要注意的是，本命令和**dampening**命令不能同时使用。

![说明](POS接口命令.files/image003.jpg)

本命令对up或down抑制的支持情况与设备的型号有关，请以设备的实际情况为准。即有些设备对up进行抑制，有些设备对down进行抑制，有些设备同时对up/down进行抑制。

【举例】

\# 设置POS接口物理连接状态抑制时间为100毫秒，即在POS接口发生up或down的时候，需要经过100毫秒后，接口状态才能变为up或down。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 link-delay msec 100

【相关命令】

·**dampening**

**POS接口 \-- POS接口配置命令 \-- link-protocol**

------------------------------------------------------------------------

**[link-protocol**]命令用来配置接口的链路协议。

【命令】

**[link-protocol**[ { **fr** \| **hdlc** \| **ppp** }]]

【缺省情况】

接口的链路协议为PPP。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fr**]：使用帧中继作为接口的链路层协议。

**[hdlc**]：使用HDLC作为接口的链路层协议。

**[ppp**]：使用PPP作为接口的链路层协议。

【举例】

\# 设置POS接口2/2/0的链路层协议为HDLC。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 link-protocol hdlc

**POS接口 \-- POS接口配置命令 \-- loopback**

------------------------------------------------------------------------

**[loopback**]命令用来开启POS接口的环回功能。

**[undo loopback**]命令用来关闭POS接口的环回功能。

【命令】

**[loopback**[ { **local** \| **remote** }]]

**[undo** **loopback**]

【缺省情况】

POS接口的环回功能处于关闭状态。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local**]：开启POS接口对内环回。

**[remote**]：开启POS接口对外环回。

【使用指导】

只有在进行某些特殊功能测试的时候，才对接口设置环回功能。

如果对POS接口封装PPP协议，设置环回后，物理层的状态会上报为up。

环回功能和**clock slave**不能同时设置，否则POS接口会无法对接成功。

【举例】

\# 开启POS接口2/2/0对内环回。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 loopback local

【相关命令】

·**clock**

**POS接口 \-- POS接口配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来设置接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

POS接口视图/POS子接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：MTU的大小，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

需要注意的是，配置了**mtu**命令后需要执行命令**shutdown**和**undo shutdown**，这样该配置才能在接口上生效。

【举例】

\# 设置POS接口2/2/0的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 mtu 1430

**POS接口 \-- POS接口配置命令 \-- port-type switch**

------------------------------------------------------------------------

![说明](POS接口命令.files/image003.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[port-type switch**]命令用来在POS接口和三层GE接口间进行类型切换。

【命令】

在POS接口视图下：

**[port-type switch gigabitethernet**]

在三层GE接口视图下：

**[port-type switch pos**]

【视图】

POS接口视图/三层GE接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gigabitethernet**]：将当前POS接口切换为三层GE接口。

**[pos**]：将当前三层GE接口切换为POS接口。

【使用指导】

接口类型切换后，原接口删除并创建新的接口，切换后的接口编号与切换前保持一致。

命令执行成功后会切换到新接口的接口视图下。

【举例】

\# 将POS接口2/2/0切换为GigabitEthernet2/2/0接口。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 port-type switch gigabitethernet

Changing port type can result in loss of port configuration. Are you sure to continue? [Y/N:y]

Sysname-GigabitEthernet2/2/0

**POS接口 \-- POS接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除POS接口、POS子接口、POS通道接口的统计信息。

【命令】

**[reset counters interface** [ **pos** [ *interface-number* [\| *interface-number.subnumber* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pos**]：清除POS接口、POS子接口、POS通道接口的统计信息。

*[interface-number*]：POS接口、POS通道接口的编号。

*[interface-number.subnumber*]：POS子接口编号，其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为0～1023。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**pos**参数，则清除所有接口的统计信息；

·如果指定**pos**参数而不指定接口编号，则清除所有POS接口、POS子接口、POS通道接口的统计信息；

·如果同时指定**pos**和接口编号，则清除指定POS接口、POS子接口、POS通道接口的统计信息。

【举例】

\# 清除POS接口2/2/0的统计信息。

\<Sysname\> reset counters interface pos 2/2/0

【相关命令】

·**display interface ****pos**

**POS接口 \-- POS接口配置命令 \-- scramble**

------------------------------------------------------------------------

**[scramble**]命令用来打开接口对载荷的加扰功能。

**[undo scramble**]命令用来关闭加扰功能。

【命令】

**[scramble**]

**[undo** **scramble**]

【缺省情况】

接口对载荷的加扰功能处于打开状态。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的1或0，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端接口都打开或关闭对载荷的加扰功能，才能对接成功。

【举例】

\# 打开POS接口2/2/0对载荷的加扰功能。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 scramble

**POS接口 \-- POS接口配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo** **shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于打开状态。

【视图】

POS接口视图/POS子接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭POS接口2/2/0。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 shutdown

**POS接口 \-- POS接口配置命令 \-- snmp-agent trap enable { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

![说明](POS接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[snmp-agent trap enable**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来开启POS接口的B1/B2/B3告警功能。

**[undo snmp-agent trap enable**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来关闭POS接口的B1/B2/B3告警功能。

【命令】

**[snmp-agent trap enable**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

**[undo snmp-agent trap enable**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

【缺省情况】

POS接口的B1/B2/B3告警功能处于开启状态。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

B1/B2/B3告警都是用于指示SDH体制线路的当前信号传输性能的，只是三者关注的信号层次不一样：

·B1检验的是当前传输信号STM-N帧的整体误码情况。

·B2检验的是传输信号基本组成单元STM-1帧的误码情况。

·B3检验的是STM-1帧封装的复用信号（VC3或VC4帧）的误码情况。

当开启了POS接口的B1/B2/B3告警功能后，设备将在POS接口的误码超过B1/B2/B3告警门限时生成告警信息。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 关闭POS2/2/0接口的B1告警功能。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 undo snmp-agent trap enable b1-tca

【相关命令】

[·**threshold**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

**POS接口 \-- POS接口配置命令 \-- speed**

------------------------------------------------------------------------

**[speed**]命令用来设置POS接口的速率。

**[undo speed**]命令用来恢复缺省情况。

【命令】

**[speed ***speed-value*]

**[undo speed**]

【缺省情况】

POS接口的速率为155Mbps。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[speed-value*]：设置的速率值，单位为Mbps。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 设置POS接口2/2/0的速率为2.5G。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 speed 2500

**POS接口 \-- POS接口配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

![说明](POS接口命令.files/image003.jpg)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·开启本功能后可能需要耗费大量系统资源，请谨慎使用。

****

**[sub-interface rate-statistic**]命令用来开启子接口的速率统计功能。

**[undo sub-interface rate-statistic**]命令用来关闭子接口的速率统计功能。

【命令】

**[sub-interface rate-statistic**]

**[undo sub-interface rate-statistic**]

【缺省情况】

子接口的速率统计功能处于关闭状态。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启POS接口2/2/0的子接口速率统计功能。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 sub-interface rate-statistic

【相关命令】

·**reset counters interface**

·**display interface pos**

**POS接口 \-- POS接口配置命令 \-- threshold**

------------------------------------------------------------------------

![说明](POS接口命令.files/image003.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[threshold**]命令用来设置接口的SD告警门限和（或）SF告警门限。

**[undo threshold**]命令用来恢复缺省情况。

【命令】

**[threshold** { **sd** *sdvalue* \| **sf** *sfvalue* } \*]

**[undo threshold** [ **sd** \| **sf** ]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sd**]：表示配置SD（Signal Degrade，信号衰减）告警门限。

*[sdvalue*]：以10e-sd*value*的形式表示的SD告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。*sdvalue*值越大表示SD告警门限越小。

**[sf**]：表示配置SF（Signal Fail，信号失败）告警门限。

*[sfvalue*]：以10e-sf*value*的形式表示的SF告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。*sfvalue*值越大表示SF告警门限越小。

【使用指导】

SD告警和SF告警都是用于指示当前线路性能的，相比较而言，SF告警比SD告警更为严重，SF的误码率门限一般会比SD的误码率门限高，也就是说，当出现少量误码时，设备产生SD告警，当误码率增大到一定程度时，说明线路质量严重下降，此时设备才产生SF告警。因此，应使SD的告警门限小于SF的告警门限，*sdvalue*的值应大于*sfvalue*。

【举例】

\# 设置POS接口2/2/0的SD告警门限为10e-4。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 threshold sd 4

**POS接口 \-- POS接口配置命令 \-- threshold { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

![说明](POS接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[threshold**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来设置POS接口的B1/B2/B3告警门限。

**[undo threshold**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来恢复缺省情况。

【命令】

**[threshold**[ { **b1-tca** *b1value* \| **b2-tca** *b2value* \| **b3-tca** *b3value* }]]

**[undo threshold**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

POS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[b1value*]：以10e-*b1value*的形式表示的B1告警门限值，*b1value*的取值范围为3～9，值越大表示B1告警门限越小。

*[b2value*]：以10e-*b2value*的形式表示的B2告警门限值，*b2value*的取值范围为3～9，值越大表示B2告警门限越小。

*[b3value*]：以10e-*b3value*的形式表示的B3告警门限值，*b3value*的取值范围为3～9，值越大表示B3告警门限越小。

【使用指导】

B1/B2/B3告警都是用于指示SDH体制线路的当前信号传输性能的，只是三者关注的信号层次不一样：

·B1检验的是当前传输信号\--STM-N帧的整体误码情况。

·B2检验的是传输信号基本组成单元STM-1帧的误码情况。

·B3检验的是STM-1帧封装的复用信号（VC3或VC4帧）的误码情况。

当开启了POS接口的B1/B2/B3告警功能后，设备将在POS接口的误码超过B1/B2/B3告警门限时生成告警信息。

【举例】

\# 配置POS2/2/0接口的B1告警门限为10e-4。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 threshold b1-tca 4

【相关命令】

[·**snmp-agent trap enable**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

**POS接口 \-- POS接口配置命令 \-- timer-hold**

------------------------------------------------------------------------

**[timer-hold**]命令用来配置Keepalive报文的发送周期。

**[undo timer-hold**]命令用来恢复缺省情况。

【命令】

**[timer-hold** *seconds*]

**[undo timer-hold**]

【缺省情况】

Keepalive报文的发送周期为10秒。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：Keepalive报文的发送周期，取值范围为0～32767，单位为秒。

【使用指导】

当接口上封装的链路层协议为PPP、FR或HDLC时，链路层会定期（可通过本命令修改）向对端发送Keepalive报文。如果在一段时间内无法收到对端发来的Keepalive报文，链路层会认为对端故障，从而上报链路层down。

在速率非常低的链路上，Keepalive报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟Keepalive报文的收发。而接口在若干个（可通过**timer-hold retry**命令修改）Keepalive报文发送周期后仍未收到对端发来的Keepalive报文，就认为链路发生故障，从而拆除链路。

【举例】

\# 在POS接口2/2/0上配置Keepalive报文的发送周期为15秒。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 timer-hold 15

【相关命令】

·**timer-hold retry**

**POS接口 \-- POS接口配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

**[timer-hold** **retry**]命令用来配置在多少个Keepalive报文发送周期内未收到应答就拆除链路。

**[undo timer-hold retry**]命令用来恢复缺省情况。

【命令】

**[timer-hold** **retry** *retry*]

**[undo timer-hold retry**]

【缺省情况】

在5个Keepalive报文发送周期内未收到应答就拆除链路。

【视图】

POS接口视图/POS通道接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retry*]：在多少个Keepalive报文发送周期内未收到应答就拆除链路，取值范围为1～255。

【使用指导】

当接口上封装的链路层协议为PPP、FR或HDLC时，链路层会定期（可通过**timer-hold**命令修改）向对端发送Keepalive报文。如果在一段时间内无法收到对端发来的Keepalive报文，链路层会认为对端故障，上报链路层Down。

在速率非常低的链路上，Keepalive报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟Keepalive报文的收发。而接口在若干个（可通过本命令修改）Keepalive报文发送周期后仍未收到对端发来的Keepalive报文，就认为链路发生故障，从而拆除链路。

【举例】

\# 在POS接口2/2/0上，配置在10个Keepalive报文发送周期内未收到应答就拆除链路。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 timer-hold retry 10

【相关命令】

·**timer-hold**

