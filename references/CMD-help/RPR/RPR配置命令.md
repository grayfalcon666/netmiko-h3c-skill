<!-- CMD-INDEX
  alarm-detect                        | RPRPOS接口视图       | L56
  bandwidth                           | 二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图 | L122
  clock                               | RPRPOS接口视图       | L204
  crc                                 | RPRPOS接口视图       | L256
  dampening                           | RPRPOS接口视图       | L310
  default                             | 二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图 | L392
  description                         | 二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图 | L464
  display interface                   | 任意视图             | L546
  display rpr bind-info               | 任意视图             | L1030
  display rpr defect                  | 任意视图             | L1142
  display rpr fairness                | 任意视图             | L1254
  display rpr mac-address             | 任意视图             | L1402
  display rpr mac-address aging-time  | 任意视图             | L1578
  display rpr protection              | 任意视图             | L1624
  display rpr rs-table                | 任意视图             | L1776
  display rpr statistics              | 任意视图             | L1944
  display rpr timers                  | 任意视图             | L2018
  display rpr topology                | 任意视图             | L2142
  flag c2                             | RPRPOS接口视图       | L3052
  flag j0                             | RPRPOS接口视图       | L3108
  flag j1                             | RPRPOS接口视图       | L3170
  flag j1 ignore                      | RPRPOS接口视图       | L3234
  flow-interval                       | 系统视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图 | L3280
  frame-format                        | RPRPOS接口视图       | L3356
  interface                           | 系统视图             | L3414
  link-delay                          | RPRPOS接口视图       | L3502
  mtu                                 | 三层RPR逻辑接口视图      | L3562
  reset counters interface            | 用户视图             | L3612
  reset rpr protection statistics     | 用户视图             | L3682
  rpr admin-request                   | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L3712
  rpr bind                            | 二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图 | L3780
  rpr default-rs ringlet1             | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L3874
  rpr echo mac                        | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L3930
  rpr mac-address                     | 二层RPR逻辑接口视图      | L4034
  rpr mac-address timer               | 系统视图             | L4096
  rpr mate smart-connect              | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4148
  rpr port-type                       | RPRXGE接口视图/RPRPOS接口视图 | L4206
  rpr protect-mode wrap               | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4270
  rpr rate-limit                      | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4324
  rpr reversion-mode non-revertive    | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4398
  rpr static-rs                       | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4446
  rpr station-name                    | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4506
  rpr timer                           | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4560
  rpr weight                          | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4634
  scramble                            | RPRPOS接口视图       | L4692
  service                             | 二层RPR逻辑接口视图/三层RPR逻辑接口视图 | L4738
  shutdown                            | 二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图 | L4852
  snmp-agent trap enable { b1-tca \| b2-tca \| b3-tca } | RPRPOS接口视图       | L4926
  threshold                           | RPRPOS接口视图       | L4986
  threshold { b1-tca \| b2-tca \| b3-tca } | RPRPOS接口视图       | L5042
  timer-hold                          | RPRPOS接口视图       | L5110
  timer-hold retry                    | RPRPOS接口视图       | L5166
-->

**RPR \-- RPR配置命令 \-- alarm-detect**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[alarm-detect**]命令用来配置当前接口的告警联动动作。

**[undo** **alarm-detect**]命令用来取消告警联动动作。

【命令】

**[alarm-detect**[ { **rdi** \| **sd** \| **sf** } **action** **link-down**]]

**[undo**[ **alarm-detect** { **rdi** \| **sd** \| **sf** }]]

【缺省情况】

接口不执行任何告警联动动作。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rdi**]：表示RDI（Remote Defect Indication，远端失效指示）告警。

**[sd**]：表示SD（Signal Degrade，信号衰减）告警。

**[sf**]：表示SF（Signal Fail，信号失败）告警。

**[action**]：配置当接口检测到告警时的联动动作。

**[link-down**]：表示自动将接口的物理状态设置为down。

【使用指导】

当设备收到对端发送的MS-RDI信号时，则认为发生了RDI告警。当设备收到的报文的误码率超过配置的门限时，则生成SD告警或SF告警。SD告警和SF告警的门限可通过**threshold**命令配置。

配置本命令后，当设备检测到告警时，会自动将接口的物理状态设置为down。

【举例】

\# 配置当接口RPRPOS2/4/0检测到SD告警时，自动将接口的物理状态设置为down。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 alarm-detect sd action link-down

【相关命令】

·**threshold**

**RPR \-- RPR配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置当前接口的期望带宽。

**[undo** **bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo** **bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置二层RPR逻辑接口RPR-Bridge1的期望带宽为10000kbit/s。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} bandwidth 10000

\# 配置三层RPR逻辑接口RPR-Router1的期望带宽为10000kbit/s。

\<Sysname\> system-view

Sysname interface rpr--router 1

Sysname-RPR-Router1 bandwidth 10000

\# 配置RPR物理接口RPRGE2/2/0的期望带宽为10000kbit/s。

\<Sysname\> system-view

Sysname interface rprge 2/2/0

Sysname-RPRGE2/2/0 bandwidth 10000

\# 配置RPR物理接口RPRXGE2/3/0的期望带宽为10000kbit/s。

\<Sysname\> system-view

Sysname interface rprxge 2/3/0

Sysname-RPRXGE2/3/0 bandwidth 10000

\# 配置RPR物理接口RPRPOS2/4/0的期望带宽为10000kbit/s。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 bandwidth 10000

**RPR \-- RPR配置命令 \-- clock**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[clock**]命令用来配置当前接口的时钟模式。

**[undo** **clock**]命令用来恢复缺省情况。

【命令】

**[clock**[ { **master** \| **slave** }]]

**[undo** **clock**]

【缺省情况】

接口的时钟模式为从时钟模式。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[master**]：表示主时钟模式，使用内部时钟信号。

**[slave**]：表示从时钟模式，使用线路提供的时钟信号。

【使用指导】

与同步串口有DTE和DCE两种工作方式相仿，RPRPOS也需要选择时钟模式。当两台设备的RPRPOS接口直接相连时，应配置一端使用主时钟模式，另一端使用从时钟模式；当与SONET/SDH设备相连时，由于SONET/SDH网络的时钟精度高于RPRPOS本身内部时钟源的精度，应配置RPRPOS接口使用从时钟模式。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0使用主时钟模式。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 clock master

**RPR \-- RPR配置命令 \-- crc**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[crc**]命令用来配置当前接口的CRC校验字长度。

**[undo** **crc**]命令用来恢复缺省情况。

【命令】

**[crc**[ { **16** \| **32** }]]

**[undo** **crc**]

【缺省情况】

接口的CRC校验字长度为32比特。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[16**]：表示CRC校验字长度为16比特。

**[32**]：表示CRC校验字长度为32比特。

【使用指导】

需要注意的是，两端设备接口的CRC校验字长度应保持一致。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0的CRC校验字长度为16比特。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 crc 16

**RPR \-- RPR配置命令 \-- dampening**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dampening**]命令用来开启当前接口的Dampening功能。

**[undo** **dampening**]命令用来关闭当前接口的Dampening功能。

【命令】

**[dampening** [ *half-life* *reuse* *suppress* *max-suppress-time* ]]

**[undo** **dampening**]

【缺省情况】

接口的Dampening功能处于关闭状态。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[half-life*]：表示半衰期，取值范围为1～120，单位为秒，缺省值为54秒。

*[reuse*]：表示启用门限，取值范围为200～20000，缺省值为750，*reuse*的值必须小于*suppress*的值。

*[suppress*]：表示抑制门限，取值范围为200～20000，缺省值为2000。

*[max-suppress-time*]：表示最大抑制时间，取值范围为1～255，单位为秒，缺省值为半衰期的3倍，即162秒。

【使用指导】

接口有两种物理连接状态：up和down。由于线缆故障、接口连接或链路层配置错误等问题，可能会导致设备接口的状态频繁的在down和up之间切换，这种现象称为接口震荡。随着接口状态的频繁改变，设备会不停的刷新相关表项（比如路由表），消耗大量的系统资源。通过在接口上配置Dampening功能，可以在一定条件下，屏蔽该接口的震荡对路由等上层业务的影响。此时若出现接口震荡，将不上送CPU处理，仅产生对应的Trap和Log信息，从而节省系统资源的消耗。

Dampening功能的工作原理如下：

·开启Dampening功能后，接口将关联一个惩罚值，初始值是0。接口状态每次从up变到down时，惩罚值会增加1000（接口状态从down变到up时，惩罚值不变）。同时，惩罚值随着时间的推移自动减少，满足半衰期衰减规律：完全衰减时（即假如在此期间没有再发生接口震荡），经过一个半衰期，惩罚值将减少为原来值的一半。

·当惩罚值大于或等于抑制门限时，开始抑制接口：不上送CPU处理接口状态变化，仅产生对应的Trap和Log信息。当惩罚值小于或等于启用门限时，不抑制接口：上送CPU处理接口状态变化，同时发送对应的Trap和Log信息。

·当惩罚值达到最大惩罚值后，惩罚值将不再增加。最大惩罚值不可配，其值与最大抑制时间、半衰期、启用门限之间的关系遵循如下公式：最大惩罚值＝2^(^^最大抑制时间/半衰期)^×启用值。

·每次接口进入抑制状态后，当接口持续抑制的时间超过最大抑制时间时，且此时惩罚值大于启用门限时，惩罚值将不再增加，此时惩罚值进入完全半衰期（此阶段接口状态变化不会增加惩罚值），直到惩罚值小于启用门限，不再抑制接口（完全半衰期中，接口仍然处于抑制状态，但完全半衰阶段时间不算入持续抑制时间）。

·如果接口抑制时间不到最大抑制时间，惩罚值就小于启用门限，那么不存在完全半衰过程（持续抑制时间超过最大抑制时间才会进入）。

需要注意的是：

·本命令和**link-delay**命令不能同时使用。

·本命令对使用**shutdown**命令手工关闭的接口无效。接口被关闭时，惩罚值恢复为初始值0。

·处于抑制期时产生的接口up事件，通过**display** **interface**命令、MIB网管或Web网管等方式查看到时，接口状态仍然为down。

【举例】

\# 开启RPR物理接口RPRPOS2/4/0的Dampening功能，配置半衰期为2秒，启用门限为800，抑制门限为3000，最大抑制时间为5秒。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 dampening 2 800 3000 5

【相关命令】

·**display** **interface**

·**link-delay**

**RPR \-- RPR配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display** **this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将二层RPR逻辑接口RPR-Bridge1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} default

\# 将三层RPR逻辑接口RPR-Router1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 default

\# 将RPR物理接口RPRGE2/2/0恢复为缺省配置。

\<Sysname\> system-view

Sysname interface rprge 2/2/0

Sysname-RPRGE2/2/0 default

\# 将RPR物理接口RPRXGE2/3/0恢复为缺省配置。

\<Sysname\> system-view

Sysname interface rprxge 2/3/0

Sysname-RPRXGE2/3/0 default

\# 将RPR物理接口RPRPOS2/4/0恢复为缺省配置。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 default

**RPR \-- RPR配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo** **description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，比如二层RPR逻辑接口RPR-Bridge1的缺省描述信息为"RPR-Bridge1 Interface"。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：表示接口的描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置二层RPR逻辑接口RPR-Bridge1的描述信息为"RPR-Bridge-1"。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} description RPR-Bridge-1

\# 配置三层RPR逻辑接口RPR-Router1的描述信息为"RPR-Router-1"。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 description RPR-Router-1

\# 配置RPR物理接口RPRGE2/2/0的描述信息为"RPRGE-1"。

\<Sysname\> system-view

Sysname interface rprge 2/2/0

Sysname-RPRGE2/2/0 description RPRGE-1

\# 配置RPR物理接口RPRXGE2/3/0的描述信息为"RPRXGE-1"。

\<Sysname\> system-view

Sysname interface rprxge 2/3/0

Sysname-RPRXGE2/3/0 description RPRXGE-1

\# 配置RPR物理接口RPRPOS2/4/0的描述信息为"RPRPOS-1"。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 description RPRPOS-1

【相关命令】

·**display** **interface**

**RPR \-- RPR配置命令 \-- display interface**

------------------------------------------------------------------------

**[display** **interface**]命令用来显示RPR接口的相关信息。

【命令】

**[display** **interface**[ [ { **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } [ *interface-number* ]   **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[rpr-bridge**]：显示二层RPR逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rpr-router**]：显示三层RPR逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprge**]：显示RPRGE接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprpos**]：显示RPRPOS接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprxge**]：显示RPRXGE接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

*[interface-number*]：表示RPR接口的编号。

**[brief**]：显示概要信息。如果未指定本参数，将显示详细信息。

**[description**]：当用户配置的接口描述信息超过27个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前27个字符，超出部分不会显示。

**[down**]：显示当前状态为down的接口的信息以及down的原因。如果未指定本参数，将不会根据接口接口状态来过滤显示信息。

【使用指导】

需要注意的是：

·如果未指定接口类型，将显示设备支持的所有接口的信息。

·如果指定了接口类型而未指定接口编号，将显示所有已创建的指定类型接口的信息。

【举例】

\# 显示二层RPR逻辑接口RPR-Bridge1的详细信息。

\<Sysname\> display interface rpr-bridge 1

RPR-Bridge1

Current state: DOWN

Description: RPR-Bridge1 Interface

Bandwidth: 0kbps

IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 34b9-854b-0102

Unknown-speed mode, full-duplex mode

Link speed type is autonegotiation, link duplex type is force link

PVID: 1

Port link-type: access

 Tagged Vlan:   none

 UnTagged Vlan: 1

Last clearing of counters: Never

\# 显示三层RPR逻辑接口RPR-Router1的详细信息。

\<Sysname\> display interface rpr-router 1

RPR-Router1

Current state: DOWN

Line protocol state: DOWN

Description: RPR-Router1 Interface

Bandwidth: 0kbps

Maximum Transmit Unit: 1500

Internet protocol processing : disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 34b9-854b-0102

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 34b9-854b-0102

Last clearing of counters:  Never

\# 显示二层RPR逻辑接口RPR-Bridge1的概要信息。

\<Sysname\> display interface rpr-bridge 1 brief

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

RPR-B1               DOWN auto    A      A    1

\# 显示三层RPR逻辑接口RPR-Router1的概要信息。

\<Sysname\> display interface rpr-router 1 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

RPR-R1               DOWN DOWN     \--

表1-1 display interface命令显示信息描述表

字段

描述

Current state

接口当前的物理状态和管理状态，可能的状态及含义如下：

·DOWN（Administratively）：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态，可能的状态及含义如下：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Description

接口的描述信息

Bandwidth

接口的期望带宽

Unknown-speed mode, unknown-duplex mode

接口速率未知，双工模式未知

Link speed type is autonegotiation

接口速率通过自协商确定

link duplex type is autonegotiation

链路双工类型通过自协商确定

PVID

接口的缺省VLAN ID

Port link-type

接口链路类型（有access、trunk和hybrid三种类型）

Tagged Vlan

标识在该端口有哪些VLAN的报文需要打Tag标记

UnTagged Vlan

标识在该端口有哪些VLAN的报文不需要打Tag标记

VLAN Passing

Trunk口实际可以通过的VLAN（该VLAN已经创建，并且接口允许其通过）

VLAN permitted

Trunk口允许通过的VLAN（该VLAN不一定存在，可能没有创建）

Trunk port encapsulation

Trunk口上封装的协议类型

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing

对IP报文的处理能力，disabled表示没有配置IP地址，不能处理IP报文。当接口下配置了IP地址之后，该字段将变为"Internet Address is"

Internet Address is 192.168.2.1/24 Primary

RPR接口配置的IP地址

IP Packet Frame Type

IPv4报文帧格式

IPv6 Packet Frame Type

IPv6报文帧格式

Hardware Address

接口的硬件地址

Last link flapping

接口最近一次物理状态改变到现在的时长。Never表示接口从设备启动后一直处于down状态（没有改变过）

Last clearing of counters

最后一次使用**reset** **counts** **interface**命令清除接口统计信息的时间，Never表示未清除过

Brief information on interface(s) under bridge mode

二层接口的概要信息

Brief information on interface(s) under route mode

三层接口的概要信息

Dampening enabled:

 Penalty: 0 (not suppressed)

 Ceiling: 4525

 Reuse: 800

 Suppress: 3000

 Half-life: 2 seconds

 Max-suppress-time: 5 seconds

 Flap count: 0

接口的dampening抑制信息，该显示信息的支持情况与用户的配置以及设备型号有关，请以设备的实际情况为准（若未使能dampening功能，则不会显示该段信息）：

·Dampening enabled：已使能dampening功能

·Penalty：惩罚值（若接口处于抑制期，则在惩罚值后标识suppressed；反之，在惩罚值后标识not suppressed）

·Ceiling：最大惩罚值

·Reuse：启用门限

·Suppress：抑制门限

·Half-life：半衰期

·Max-suppress-time：最大抑制时间

·Flap count：接口震荡发生的次数

 

Hold timer

Keepalive报文的发送周期

retry times

在多少个Keepalive报文发送周期内未收到应答就拆除链路

Internet Address

接口的网络地址

Link layer protocol

接口的链路层封装的协议

LCP: opened, IPCP: opened

表示LCP和IPCP都协商成功

Physical layer

物理接口

Baudrate

接口的波特率

Scramble

接口是否开启对载荷数据的加扰功能

crc

接口的CRC校验字长度

clock

接口的时钟模式

loopback

接口是否开启环回功能

SONET alarm

SONET告警信息

SONET error

SONET错误信息

Last link flapping

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

Speed or Duplex: (a)/A - auto; H - half; F - full

Speed属性值为(a)表示该接口的速率通过自动协商获取；Duplex属性值为(a)或A表示该接口的Duplex属性通过自动协商获取，为H表示半双工，为F则表示全双工

Type: A - access; T - trunk; H - hybrid

接口的链路类型：

·A：表示Access链路类型

·H：表示Hybrid链路类型

·T：表示Trunk链路类型

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称的缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Speed

接口的速率，单位为bps

Duplex

接口的双工模式：

·A：表示双工模式由自动协商结果决定

·F：表示全双工

·F(a)：表示自由协商的结果为全双工

·H：表示半双工

·H(a)：表示自由协商的结果为半双工

Type

接口的链路类型：

·A：表示Access链路类型

·H：表示Hybrid链路类型

·T：表示Trunk链路类型

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口的主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

【相关命令】

·**reset** **counters** **interface**

**RPR \-- RPR配置命令 \-- display rpr bind-info**

------------------------------------------------------------------------

**[display** **rpr** **bind-info**]命令用来显示RPR逻辑接口与RPR物理接口的绑定信息。

【命令】

**[display**[ **rpr** **bind-info** [ { **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

[[{ **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } *interface-number*]]：显示指定RPR接口的绑定信息。如果未指定本参数，将显示所有RPR逻辑接口对应的绑定信息。不同型号的设备支持的接口类型不同，请以设备的实际情况为准。

【举例】

\# 显示所有RPR逻辑接口的绑定信息。

\<Sysname\> display rpr bind-info

Bind information on interface RPR-Bridge1:

 Smart connection: Enabled/Disconnected

 PHY interface    Ringlet ID    Role       Mate port

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 None             N/A           N/A        N/A

 None             N/A           N/A        N/A

Bind information on interface RPR-Router1:

 Smart connection: Enabled/Connected

 PHY interface    Ringlet ID    Role       Mate port

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 RPRPOS2/4/0      0             Primary    Up

 RPRPOS2/4/1      1             Secondary  Up

表1-2 display rpr bind-info命令显示信息描述表

字段

描述

Bind information on interface

RPR{.ItemListinTableCharChar}逻辑接口的绑定信息{.ItemListinTableCharChar}

Smart connection

MATE口的智能连接功能是否使能以及{.ItemListinTableCharChar}MATE口的连接情况：{.ItemListinTableCharChar}

·Enabled/Connected：表示智能连接功能处于使能状态，MATE口已在内部自动连接

·Enabled/Disconnected：表示智能连接功能处于使能状态，但MATE口在内部并未自动连接

·Disabled：表示智能连接功能处于关闭状态

PHY interface

绑定到RPR逻辑接口的RPR物理接口

Ringlet ID

RPR{.ItemListinTableCharChar}物理接口绑定到{.ItemListinTableCharChar}RPR逻辑接口上的绑定方向：{.ItemListinTableCharChar}

·0：表示RPR{.ItemListinTableCharChar}物理接口绑定为RPR逻辑接口的西向接口

·1：表示RPR{.ItemListinTableCharChar}物理接口绑定为RPR逻辑接口的东向接口

·N/A：表示没有绑定

Role

RPR物理接口的角色：

·Primary：表示该RPR物理接口为主接口

·Secondary：表示该RPR物理接口为从接口

·N/A：表示没有绑定

Mate port

RPR物理接口对应{.ItemListinTableCharChar}MATE口的状态：{.ItemListinTableCharChar}

·Up：表示MATE口处于up状态

·Down：表示MATE口处于down状态

·N/A：表示没有绑定

**RPR \-- RPR配置命令 \-- display rpr defect**

------------------------------------------------------------------------

**[display** **rpr** **defect**]命令用来显示RPR的缺陷信息。

【命令】

**[display**[ **rpr** **defect** [ { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：显示指定RPR逻辑接口对应RPR站点所在RPR环的缺陷信息。如果未指定本参数，将显示所有RPR逻辑接口对应的RPR站点所在RPR环的缺陷信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【举例】

\# 显示三层RPR逻辑接口RPR-Router1所在RPR环的缺陷信息。

\<Sysname\> display rpr defect rpr-router 1

RPR defects on interface RPR-Router1:

  Reserved rate exceeded                            : Ringlet0：0; Ringlet1: 0

  Jumbo configuration defect                        : 0

  Maximum number of stations exceeded               : 0

  Miscabling                                        : Ringlet0: 0; Ringlet1: 0

  Protection mode configuration defect              : 0

  Inconsistent topology                             : 0

  Unstable topology                                 : 0

  Invalid topology entry                            : 0

  Duplicate IP address                              : 0

  Duplicate secondary MAC address                   : 0

  Maximum number of secondary MAC addresses exceeded: 0

表1-3 display rpr defect命令显示信息描述表

字段

描述

RPR defects on interface RPR-Router1

RPR-Router1接口对应站点所在{.ItemListinTableCharChar}RPR环的缺陷信息{.ItemListinTableCharChar}

Reserved rate exceeded

超过预留带宽缺陷，分别对{.ItemListinTableCharChar}0环和{.ItemListinTableCharChar}1环说明：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

Jumbo configuration defect

Jumbo帧配置缺陷：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

Maximum number of stations exceeded

超过最大站点数限制缺陷：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

Miscabling

光纤错接缺陷，分别对{.ItemListinTableCharChar}0环和{.ItemListinTableCharChar}1环说明：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

Protection mode configuration defect

保护倒换模式配置缺陷：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

Inconsistent topology

拓扑不一致缺陷：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

Unstable topology

拓扑不稳定缺陷：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

Invalid topology entry

拓扑实体无效缺陷：0表示没有缺陷，1表示存在缺陷

Duplicate IP address

IP地址重复缺陷：0表示没有缺陷，1表示存在缺陷

Duplicate secondary MAC address

次级{.ItemListinTableCharChar}MAC地址重复缺陷：{.ItemListinTableCharChar}0{.ItemListinTableCharChar}表示没有缺陷，{.ItemListinTableCharChar}1{.ItemListinTableCharChar}表示存在缺陷{.ItemListinTableCharChar}

Maximum number of secondary MAC addresses exceeded

超过最大次级MAC地址数缺陷：{.ItemListinTableCharChar}0表示没有缺陷，{.ItemListinTableCharChar}1表示存在缺陷{.ItemListinTableCharChar}

**RPR \-- RPR配置命令 \-- display rpr fairness**

------------------------------------------------------------------------

**[display** **rpr** **fairness**]命令用来显示RPR的公平性参数信息。

【命令】

**[display**[ **rpr** **fairness** [ { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：显示指定RPR逻辑接口对应RPR站点的公平性参数信息。如果未指定本参数，将显示所有RPR逻辑接口对应RPR站点的公平性参数信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【举例】

\# 三层RPR逻辑接口RPR-Router1已绑定两个2.5GPOS物理接口，显示该接口的RPR公平性参数信息。

\<Sysname\> display rpr fairness rpr-router 1

RPR fairness parameters on interface RPR-Router1:

  Fairness weight on Ringlet0: 1

  Fairness weight on Ringlet1: 1

  Local reserved bandwidth for class A0 service on Ringlet0: 0 Mbps

  Local reserved bandwidth for class A0 service on Ringlet1: 0 Mbps

  Local rate limit for subclass A1 service on Ringlet0: 5 Mbps

  Local rate limit for subclass A1 service on Ringlet1: 5 Mbps

  Local rate limit for class B CIR service on Ringlet0: 0 Mbps

  Local rate limit for class B CIR service on Ringlet1: 0 Mbps

  Local rate limit for class B EIR and class C service on Ringlet0: 2500 Mbps

  Local rate limit for class B EIR and class C service on Ringlet1: 2500 Mbps

  Total reserved bandwidth for class A0 service on Ringlet0: 0 Mbps

  Total reserved bandwidth for class A0 service on Ringlet1: 0 Mbps

\# 三层RPR逻辑接口RPR-Router2没有绑定任何RPR物理接口，显示该接口的RPR公平性参数信息。

\<Sysname\> display rpr fairness rpr-router 2

RPR fairness parameters on interface RPR-Router2:

  Fairness weight on Ringlet0: 1

  Fairness weight on Ringlet1: 1

  Local reserved bandwidth for class A0 service on Ringlet0: 0 in permillage

  Local reserved bandwidth for class A0 service on Ringlet1: 0 in permillage

  Local rate limit for subclass A1 service on Ringlet0: 2 in permillage

  Local rate limit for subclass A1 service on Ringlet1: 2 in permillage

  Local rate limit for class B CIR service on Ringlet0: 0 in permillage

  Local rate limit for class B CIR service on Ringlet1: 0 in permillage

  Local rate limit for class B EIR and class C service on Ringlet0: 1000 in permillage

  Local rate limit for class B EIR and class C service on Ringlet1: 1000 in permillage

![说明](RPR命令.files/image002.png)

当RPR逻辑接口没有与RPR物理接口进行绑定时，站点在0环和1环上为各类业务配置的预留带宽显示的是该类业务预留带宽占总带宽的千分比。

表1-4 display rpr fairness命令显示信息描述表

字段

描述

RPR fairness parameters on interface RPR-Router1

RPR-Router1接口对应站点公平性参数信息{.ItemListinTableCharChar}

Fairness weight on Ringlet0

本站点在{.ItemListinTableCharChar}0环上公平权重{.ItemListinTableCharChar}

Fairness weight on Ringlet1

本站点在{.ItemListinTableCharChar}1环上公平权重{.ItemListinTableCharChar}

Local reserved bandwidth for class A0 service on Ringlet0

本站点在{.ItemListinTableCharChar}0环上为{.ItemListinTableCharChar}A0类业务预留的带宽{.ItemListinTableCharChar}

Local reserved bandwidth for class A0 service on Ringlet1

本站点在{.ItemListinTableCharChar}1环上为{.ItemListinTableCharChar}A0类业务预留的带宽{.ItemListinTableCharChar}

Local rate limit for subclass A1 service on Ringlet0

本站点在{.ItemListinTableCharChar}0环上为{.ItemListinTableCharChar}A1类业务配置的预留带宽{.ItemListinTableCharChar}

Local rate limit for subclass A1 service on Ringlet1

本站点在{.ItemListinTableCharChar}1环上为{.ItemListinTableCharChar}A1类业务配置的预留带宽{.ItemListinTableCharChar}

Local rate limit for class B CIR service on Ringlet0

本站点在0环上为B-CIR类业务配置的预留带宽

Local rate limit for class B CIR service on Ringlet1

本站点在1环上为B-CIR类业务配置的预留带宽

Local rate limit for class B EIR and class C service on Ringlet0

本站点在0环上为B-EIR和C类业务配置的预留带宽

Local rate limit for class B EIR and class C service on Ringlet1

本站点在1环上为B-EIR和C类业务配置的预留带宽

Total reserved bandwidth for class A0 service on Ringlet0

本站点所在RPR环上的所有站点在0环上为A0类业务预留带宽之和

Total reserved bandwidth for class A0 service on Ringlet1

本站点所在RPR环上的所有站点在1环上为A0类业务预留带宽之和

**RPR \-- RPR配置命令 \-- display rpr mac-address**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **rpr** **mac-address**]命令用来显示RPR MAC地址表的信息。

【命令】

**[display**[ **rpr** **mac-address** [ **dynamic** \| **static** ]  **destination** *mac-address1*   **vlan** *vlan-id*   **ring** *mac-address2*   **rpr-bridge** *interface-number*   **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dynamic**]：显示RPR动态MAC地址表信息。

**[static**]：显示RPR静态MAC地址表信息。

**[destination** *mac-address1*]：显示指定目的MAC地址的表项信息。

**[vlan** *vlan-id*]：显示指定VLAN的RPR MAC地址表信息。*vlan-id*为VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[ring** *mac-address2*]：显示指定下环站点MAC地址的表项信息。

**[rpr-bridge** *interface-number*]：显示指定二层RPR逻辑接口对应站点的RPR MAC地址表信息。如果未指定本参数，将显示所有二层RPR逻辑接口对应站点的RPR MAC地址表信息。

**[count**]：显示指定RPR MAC地址表的表项条数。

【举例】

\# 显示RPR静态MAC地址表的信息。

\<Sysname\> display rpr mac-address static

Static MAC address table on interface RPR-Bridge1:

 MAC address     VLAN ID   Next hop          Status    Ringlet ID   TTL

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 0001-0001-0001  1         00e0-fc01-6503    Valid     1            1

 0001-0001-0001  2         00e0-fc01-6503    Valid     1            1

 0002-0002-0002  2         00e0-fc01-6503    Invalid   N/A          N/A

 0002-0002-0002  1000      00e0-fc01-6503    Valid     1            244

 \-\--   Total entrie(s): 4   \-\--

\# 显示RPR动态MAC地址表的信息。

\<Sysname\> display rpr mac-address dynamic

Dynamic MAC address table on interface RPR-Bridge1:

 MAC address     VLAN ID   Next hop          Status    Ringlet ID   TTL

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 0001-0001-0001  2         00e0-fc01-6503    Valid     1            1

 \-\--   Total entrie(s): 1   \-\--

![说明](RPR命令.files/image002.png)

RPR动态MAC地址表的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-5 display rpr mac-address命令显示信息描述表

字段

描述

Static MAC address table on interface RPR-Bridge1

RPR-Bridge1接口对应站点的RPR静态MAC地址表信息

Dynamic MAC address table on interface RPR-Bridge1

RPR-Bridge1接口对应站点的RPR动态MAC地址表信息

MAC address

目的MAC地址

VLAN ID

目的MAC地址所在的VLAN编号

Next hop

下一跳的MAC地址

Status

是否有效：

·Valid：表示有效

·Invalid：表示无效

Ringlet ID

子环号

TTL

生存时间

Total entrie(s)

指定RPR MAC地址表表项条数

\# 显示RPR静态MAC地址表的表项条数。

\<Sysname\> display rpr mac-address static count

Static MAC address table on interface RPR-Bridge1:

  5 entries found.

Static MAC address table on interface RPR-Bridge2:

  No entry found.

\# 显示RPR动态MAC地址表的表项条数。

\<Sysname\> display rpr mac-address dynamic count

Dynamic MAC address table on interface RPR-Bridge1:

  No entry found.

Dynamic MAC address table on interface RPR-Bridge2:

  No entry found.

![说明](RPR命令.files/image002.png)

RPR动态MAC地址表表项条数的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-6 display rpr mac-address count命令显示信息描述表

字段

描述

Static MAC address table on interface RPR-Bridge1

RPR-Bridge1接口对应站点的RPR静态MAC地址表信息

Dynamic MAC address table on interface RPR-Bridge1

RPR-Bridge1接口对应站点的RPR动态MAC地址表信息

5 entries found

指定RPR MAC地址表表项条数

**RPR \-- RPR配置命令 \-- display rpr mac-address aging-time**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **rpr** **mac-address** **aging-time**]命令用来显示RPR动态MAC地址表表项的老化时间。

【命令】

**[display** **rpr** **mac-address** **aging-time**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示RPR动态MAC地址表表项的老化时间。

\<Sysname\> display rpr mac-address aging-time

  Dynamic MAC-Learning aging time : 100 s

表1-7 display rpr mac-address aging-time命令显示信息描述表

字段

描述

Dynamic MAC-Learning aging time

RPR动态MAC地址表表项的老化时间

**RPR \-- RPR配置命令 \-- display rpr protection**

------------------------------------------------------------------------

**[display** **rpr** **protection**]命令用来显示RPR的保护信息。

【命令】

**[display**[ **rpr** **protection** [ { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：显示指定RPR逻辑接口对应的RPR站点的保护信息。如果未指定本参数，将显示所有RPR逻辑接口对应的RPR站点的保护信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【使用指导】

需要注意的是，保护倒换模式分为配置的保护倒换模式和生效的保护倒换模式，前者由用户手工配置，但并不一定生效，协议自动检查环上所有站点的保护倒换模式，尽量保证生效的保护倒换模式的一致性。

【举例】

\# 三层RPR逻辑接口RPR-Router1已绑定两个RPR物理接口，显示该接口的RPR保护信息。

\<Sysname\> display rpr protection rpr-router 1

Protection information on interface RPR-Router1:

  Configured protection mode: Steer

  Active protection mode: Steer

  Protection reversion mode: Revertible

  Context containment: Disabled

                                    West span              East span

  Protection state                  IDLE                   FS

  Edge state                        Unedged                Edged

  Last known neighbour              00e0-0100-0002         00e0-0300-0002

  The number of protection states   1                      4

  The number of local edges         0                      2

  Last local edge time              -                      2014.04.08 05:47:31

  Local edge start time             -                      2014.04.08 05:48:07

\# 三层RPR逻辑接口RPR-Router2没有绑定任何RPR物理接口，显示该接口的RPR保护信息。

\<Sysname\> display rpr protection rpr-router 2

Protection information on interface RPR-Router2:

  Configured protection mode: Steer

  Protection reversion mode: Revertible

![说明](RPR命令.files/image002.png)

当RPR逻辑接口未与任何RPR物理接口进行绑定时，将只显示该RPR逻辑接口配置的保护倒换模式和保护倒换恢复模式。

表1-8 display rpr protection命令显示信息描述表

字段

描述

Protection information on interface RPR-Router1

RPR-Router1接口对应站点的{.ItemListinTableCharChar}RPR{.ItemListinTableCharChar}保护信息{.ItemListinTableCharChar}

Configured protection mode

配置的保护倒换模式{.ItemListinTableCharChar}

Active protection mode

生效的保护倒换模式{.ItemListinTableCharChar}

Protection reversion mode

保护倒换恢复模式{.ItemListinTableCharChar}

Context containment

上下文抑制是否生效：{.ItemListinTableCharChar}

·Enabled：表示生效

·Disabled：表示无效

Protection state

东西向{.ItemListinTableCharChar}Span上的保护状态：{.ItemListinTableCharChar}

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

Edge state

东西向{.ItemListinTableCharChar}Span上的{.ItemListinTableCharChar}Edge状态：{.ItemListinTableCharChar}

·Edged：表示发生Edge

·Unedged：表示没有发生{.ItemListinTableCharChar}E{.ItemListinTableCharChar}dge

Last known neighbour

东西向邻站点{.ItemListinTableCharChar}MAC地址{.ItemListinTableCharChar}

The number of protection states

本站点东西向{.ItemListinTableCharChar}Span上保护状态变化次数{.ItemListinTableCharChar}

The number of local edges

本站点东西向{.ItemListinTableCharChar}Span上出现{.ItemListinTableCharChar}Edge的次数{.ItemListinTableCharChar}

Last local edge time

本站点东西向{.ItemListinTableCharChar}Span上上一次出现{.ItemListinTableCharChar}Edge的时间{.ItemListinTableCharChar}

Local edge start time

本站点东西向{.ItemListinTableCharChar}Span上当前{.ItemListinTableCharChar}Edge的开始时间{.ItemListinTableCharChar}

**RPR \-- RPR配置命令 \-- display rpr rs-table**

------------------------------------------------------------------------

**[display** **rpr** **rs-table**]命令用来显示RPR选环表的信息。

【命令】

**[display**[ **rpr** **rs-table** { **default** \| **dynamic** \| **overall** \| **static** } [ { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[default**]：显示默认选环表信息。

**[dynamic**]：显示动态选环表信息。

**[overall**]：显示综合选环表信息。

**[static**]：显示静态选环表信息。

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：显示指定RPR逻辑接口对应RPR站点选环表的信息。如果未指定本参数，将显示所有RPR逻辑接口对应的RPR站点选环表的信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【举例】

\# 显示RPR动态选环表的信息。

\<Sysname\> display rpr rs-table dynamic

Dynamic ringlet selection table on interface RPR-Router1:

 MAC address     Ringlet ID  TTL  IP address       Station name

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 00e0-fc00-1a01  0           1    -

 \-\--   Entries in total: 1    \-\--

\# 显示RPR静态选环表的信息。

\<Sysname\> display rpr rs-table static

Static ringlet selection table on interface RPR-Router1:

 MAC address    Ringlet ID   Status

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 0003-0002-0002 0            Invalid

 \-\--   Entries in total: 1    \-\--

\# 显示RPR默认选环表的信息。

\<Sysname\>display rpr rs-table default

Default ringlet selection table on interface RPR-Router1:

  Configured default ringlet: Ringlet0

  Active default ringlet: Ringlet0

\# 显示RPR综合选环表的信息。

\<Sysname\> display rpr rs-table overall

Overall ringlet selection table on interface RPR-Router2:

 MAC address     Ringlet ID  TTL  Type      IP address       Station name

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 00e0-fe10-0001  0           1    Dynamic   -

 \-\--   Entries in total: 1    \-\--

表1-9 display rpr rs-table命令显示信息描述表

字段

描述

Dynamic ringlet selection table on interface RPR-Router1

RPR-Router1接口对应站点动态选环表的信息{.ItemListinTableCharChar}

Static ringlet selection table on interface RPR-Router1

RPR-Router1接口对应站点静态选环表的信息{.ItemListinTableCharChar}

Default ringlet selection table on interface RPR-Router1

RPR-Router1接口对应站点默认选环表的信息{.ItemListinTableCharChar}

Overall ringlet selection table on interface RPR-Router2

RPR-Router2接口对应站点综合选环表的信息{.ItemListinTableCharChar}

MAC address

目的站点{.ItemListinTableCharChar}MAC地址{.ItemListinTableCharChar}

Ringlet ID

发送子环：

·0：表示0环

·1：表示1环

TTL

生存时间，到目的站点经过的跳数

Type

生成综合选环表的选环表类型：

·Static：表示静态选环

·Dynamic：表示动态选环

IP address

目的站点{.ItemListinTableCharChar}IP地址，目的站点未配置{.ItemListinTableCharChar}IP地址时显示为{.ItemListinTableCharChar}-

Station name

目的站点名称

Status

表项状态：

·Valid：表示有效

·Invalid：表示无效

Configured default ringlet

配置的默认选环：

·Ringlet0：表示0环

·Ringlet1：表示1环

Active default ringlet

实际生效的默认选环：

·Ringlet0：表示0环

·Ringlet1：表示1环

**RPR \-- RPR配置命令 \-- display rpr statistics**

------------------------------------------------------------------------

**[display** **rpr** **statistics**]命令用来显示RPR环上流量统计的信息。

【命令】

**[display**[ **rpr** **statistics** { **dmac** \| **smac** } [ *mac-address*   { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dmac**]：显示发送到指定目的站点的流量统计信息。

**[smac**]：显示从指定源站点收到的流量统计信息。

*[mac-address*]：显示发送到环上指定MAC地址的目的站点或从环上指定MAC地址的源站点收到的流量统计信息。如果未指定本参数，将显示发送到环上所有站点或从环上所有站点收到的流量统计信息。

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：显示指定RPR逻辑接口对应RPR站点的流量统计信息。如果未指定本参数，将显示所有RPR逻辑接口对应的RPR站点的流量统计信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【举例】

\# 显示从MAC地址为00E0-FC00-1A01的环上站点发送过来的流量统计信息。

\<Sysname\> display rpr statistics smac 00e0-fc00-1a01

Statistics for traffic from the source station on interface RPR-Router1:

 MAC address      Packets              Bytes

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 00e0-fc00-1a01   1844                 1844

表1-10 display rpr statistics命令显示信息描述表

字段

描述

Statistics for traffic from the source station on interface RPR-Router1

RPR-Router1接口对应站点基于源{.ItemListinTableCharChar}MAC地址统计的流量信息{.ItemListinTableCharChar}

Statistics for traffic to the destination station on interface RPR-Router1

RPR-Router1接口对应站点基于目的{.ItemListinTableCharChar}MAC地址统计的流量信息{.ItemListinTableCharChar}

MAC address

源或目的站点的{.ItemListinTableCharChar}MAC地址{.ItemListinTableCharChar}

Packets

发送或接收的报文数

Bytes

发送或接收的字节数

**RPR \-- RPR配置命令 \-- display rpr timers**

------------------------------------------------------------------------

**[display** **rpr** **timers**]命令用来显示RPR可配定时器的值。

【命令】

**[display**[ **rpr** **timers** [ { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：显示指定RPR逻辑接口对应的RPR站点的定时器信息。如果未指定本参数，将显示所有RPR逻辑接口对应的RPR站点的定时器信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【举例】

\# 显示所有RPR可配定时器的值。

\<Sysname\> display rpr timers

RPR timers on interface RPR-Bridge1:

  Fast TP timer: 10 ms

  Slow TP timer: 100 ms

  Fast TC timer: 10 ms

  Slow TC timer: 100 ms

  ATD timer: 1 s

  WTR timer: 10 s

  Holdoff timer: 0 ms

  Keepalive timer: 3 ms

  Topology stability timer: 40 ms

RPR timers on interface RPR-Router1:

  Fast TP timer: 10 ms

  Slow TP timer: 100 ms

  Fast TC timer: 10 ms

  Slow TC timer: 100 ms

  ATD timer: 1 s

  WTR timer: 10 s

  Holdoff timer: 0 ms

  Keepalive timer: 3 ms

  Topology stability timer: 40 ms

![说明](RPR命令.files/image002.png)

本命令的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-11 display rpr timers命令显示信息描述表

字段

描述

RPR timers on interface RPR-Router1

RPR-Router1接口对应站点所有定时器的值

Fast TP timer

TP帧快发定时器的值

Slow TP timer

TP帧慢发定时器的值

Fast TC timer

TC帧快发定时器的值

Slow TC timer

TC帧慢发定时器的值

ATD timer

ATD帧定时器的值

WTR timer

WTR定时器的值

Holdoff timer

Hold Off定时器的值

Keepalive timer

Keepalive定时器的值

Topology stability timer

拓扑稳定定时器的值

**RPR \-- RPR配置命令 \-- display rpr topology**

------------------------------------------------------------------------

**[display** **rpr** **topology**]命令用来显示RPR的拓扑信息。

【命令】

**[display**[ **rpr** **topology** { **all** \| **local** \| **ring** \| **stations** } [ **brief**   { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示拓扑数据库所有信息。

**[local**]：显示本站点拓扑信息。

**[ring**]：显示环路级的拓扑信息。

**[stations**]：显示环上所有站点拓扑信息。

**[brief**]：显示RPR拓扑摘要信息。

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：显示指定RPR逻辑接口对应RPR站点的相关拓扑信息。如果未指定本参数，将显示所有RPR逻辑接口对应的RPR站点的相关拓扑信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【举例】

\# 三层RPR逻辑接口RPR-Router1已绑定两个RPR物理接口，显示该接口对应RPR站点的所有拓扑数据库信息。

\<Sysname\> display rpr topology all rpr-router 1

Ring-level topology information on interface RPR-Router1:

  Number of stations on Ringlet0: 1

  Number of stations on Ringlet1: 1

  Total number of stations on the ring: 2

  Jumbo preference: Regular

  Ring topology type: Closed ring

Local station topology information on interface RPR-Router1:

  Station name:

  MAC address: 00e0-fc00-1001

  IP address: -

  Jumbo preference: Regular

  Active protection mode: Steer

  Protection state on the west span: IDLE

  Protection state on the east span: IDLE

  Edge state on the west span: Unedged

  Edge state on the east span: Unedged

  Sequence number: 10

  Last known neighbour on the west span: 00e0-fc00-1a01

  Last known neighbour on the east span: 00e0-fc00-1a01

  Local topology state: Valid

Station topology information on interface RPR-Router1:

 Station entry on Ringlet0:

  MAC address: 00e0-fc00-1a01

  Station name:

  IP address: -

  Hops: 1

  Jumbo preference: Regular

  Protection mode: Steer

  Protection state on the west span: IDLE

  Protection state on the east span: IDLE

  Edge state on the west span: Unedged

  Edge state on the east span: Unedged

  Sequence number: 9

  Reachability: Reachable

  Valid: 1

 Station entry on Ringlet1:

  MAC address: 00e0-fc00-1a01

  Station name:

  IP address:  -

  Hops: 1

  Jumbo preference: Regular

  Protection mode: Steer

  Protection state on the west span: IDLE

  Protection state on the east span: IDLE

  Edge state on the west span: Unedged

  Edge state on the east span: Unedged

  Sequence number: 9

  Reachability: Reachable

  Valid: 1

\# 三层RPR逻辑接口RPR-Router2没有绑定任何RPR物理接口，显示该接口对应RPR站点的所有拓扑数据库信息。

\<Sysname\> display rpr topology all rpr-router 2

Ring-level topology information on interface RPR-Router2:

  Number of stations on Ringlet0: 0

  Number of stations on Ringlet1: 0

  Total number of stations on the ring: 1

  Jumbo preference: Regular

  Ring topology type: Open ring

Local station topology information on interface RPR-Router2:

  Station name:

  IP address: -

Station topology information on interface RPR-Router2:

 Station entry on Ringlet0:

  No station entry.

 Station entry on Ringlet1:

  No station entry.

表1-12 display rpr topology all命令显示信息描述表

字段

描述

Ring-level topology information on interface RPR-Router1

RPR-Router1接口对应的{.ItemListinTableCharChar}RPR站点所在{.ItemListinTableCharChar}RPR环的环路拓扑信息{.ItemListinTableCharChar}

Number of stations on Ringlet0

站点在西向{.ItemListinTableCharChar}Span上的站点数{.ItemListinTableCharChar}

Number of stations on Ringlet1

站点在东向{.ItemListinTableCharChar}Span上的站点数{.ItemListinTableCharChar}

Total number of stations on the ring

站点所在环上总站点数

Jumbo preference

是否支持{.ItemListinTableCharChar}Jumbo帧：{.ItemListinTableCharChar}

·Regular：表示不支持

·Jumbo：表示支持

Ring topology type

环状态：

·Open ring：表示开环

·Closed ring：表示闭环

Local station topology information on interface RPR-Router1

RPR-Router1接口对应的{.ItemListinTableCharChar}RPR站点的本地拓扑数据库信息{.ItemListinTableCharChar}

Station name

站点名称

MAC address

站点{.ItemListinTableCharChar}MAC地址{.ItemListinTableCharChar}

IP address

站点{.ItemListinTableCharChar}IP地址，未配置{.ItemListinTableCharChar}IP地址时显示为{.ItemListinTableCharChar}-

Active protection mode

站点生效保护倒换模式：

·Wrap：表示wrap模式

·Steer：表示steer模式

Protection state on the west span

站点西向{.ItemListinTableCharChar}Span的保护状态：{.ItemListinTableCharChar}

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

Protection state on the east span

站点东向{.ItemListinTableCharChar}Span的保护状态：{.ItemListinTableCharChar}

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

Edge state on the west span

站点西向{.ItemListinTableCharChar}Span是否出现{.ItemListinTableCharChar}Edge状态：{.ItemListinTableCharChar}

·Edged：表示发生edge

·Unedged：表示没有发生{.ItemListinTableCharChar}edge

Edge state on the east span

站点东向{.ItemListinTableCharChar}Span是否出现{.ItemListinTableCharChar}Edge状态：{.ItemListinTableCharChar}

·Edged表示发生edge

·Unedged表示没有发生{.ItemListinTableCharChar}edge

Sequence number

TP帧序列号{.ItemListinTableCharChar}

Last known neighbour on the west span

西向最后学习到的邻站点的{.ItemListinTableCharChar}MAC地址{.ItemListinTableCharChar}

Last known neighbour on the east span

东向最后学习到的邻站点的{.ItemListinTableCharChar}MAC地址{.ItemListinTableCharChar}

Local topology state

本站点拓扑状态：

·Start：表示拓扑初始化

·Stable：表示拓扑稳定

·Unstable：表示拓扑不稳定

·Valid：表示拓扑有效

·Invalid：表示拓扑无效{.ItemListinTableCharChar}

Station topology information on interface RPR-Router1

RPR-Router1接口对应的{.ItemListinTableCharChar}RPR站点的拓扑数据库信息{.ItemListinTableCharChar}

Station entry on Ringlet0

站点西向Span上邻站点的拓扑信息

Station entry on Ringlet1

站点东向Span上邻站点的拓扑信息

Hops

该站点到本地站点的跳数

Protection mode

站点的保护倒换模式：

·Wrap：表示Wrapping模式

·Steer：表示Steering模式

Sequence number

TP帧序列号

Reachability

站点是否可达：

·Reachable：表示可达

·Unreachable：表示不可达

Valid

表项是否有效：

·1：表示有效

·0：表示无效

\# 显示拓扑数据库所有信息的摘要信息。

\<Sysname\> display rpr topology all brief

Topology information items:

PSW: Protection State, West       PSE: Protection State, East

ESW: Edge State, West             ESE: Edge State, East

WC: Wrap protection Configured    JP: Jumbo frame Preferred

Ring-level topology information on interface RPR-Router1:

 Ringlet0  Ringlet1  Ring  Jumbo prefer  Topology type

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 1         1         2     Regular       Closed ring

Local station topology information on interface RPR-Router1:

 MAC address    PSW  PSE  ESW  ESE  WC  JP  IP address       Station name

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 00e0-fc00-1001 IDLE IDLE 0    0    0   0   -                StationA

Station topology information on interface RPR-Router1:

 Station entry on Ringlet0:

 MAC address    PSW  PSE  ESW  ESE  WC  JP  IP address       Station name

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 00e0-fc00-1a01 IDLE IDLE 0    0    0   0   -                StationB

 Station entry on Ringlet1:

 MAC address    PSW  PSE  ESW  ESE  WC  JP  IP address       Station name

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 00e0-fc00-1a01 IDLE IDLE 0    0    0   0   -                StationB

表1-13 display rpr topology all brief命令显示信息描述表

字段

描述

Topology information items

拓扑信息条目

PSE

站点东向Span保护状态：

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

PSW

站点西向Span保护状态：

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

ESE

站点东向Span Edge状态：

·1：表示发生edge

·0：表示没有发生edge

ESW

站点西向Span Edge状态：

·1：表示发生edge

·0：表示没有发生edge

WC

Wrap保护设置：

·1：表示Wrapping模式

·0：表示Steering模式

JP:Jumbo frame preferred

Jumbo帧设置：

·1：表示支持Jumbo帧

·0：表示不支持Jumbo帧

Ring-level topology information on interface RPR-Router1

RPR-Router1接口对应的RPR站点所在RPR环的拓扑信息

Ringlet0

站点在西向Span上的站点数

Ringlet1

站点在东向Span上的站点数

Ring

站点所在环上总站点数

Jumbo prefer

是否支持Jumbo帧：

·Regular：表示不支持

·Jumbo：表示支持

Topology type

环状态：

·Open ring：表示开环

·Closed ring：表示闭环

Local station topology information on interface RPR-Router1

RPR-Router1接口对应的RPR站点的本地拓扑数据库摘要信息

MAC address

站点MAC地址

IP address

站点IP地址

Station name

站点名称

Station topology information on interface RPR-Router1

RPR-Router1接口对应的RPR站点所在RPR环的其它站点的拓扑摘要信息

Station entry on ringlet0

该接口对应的RPR站点在RPR环的西向Span上邻站点的拓扑摘要信息

Station entry on ringlet1

该接口对应的RPR站点在RPR环的东向Span上邻站点的拓扑摘要信息

\# 显示本站点的拓扑信息。

\<Sysname\>display rpr topology local

Local station topology information on interface RPR-Router1:

  Station name: StationA

  MAC address: 00e0-fc00-1001

  IP address: -

  Jumbo preference: Regular

  Active protection mode: Steer

  Protection state on the west span: IDLE

  Protection state on the east span: IDLE

  Edge state on the west span: Unedged

  Edge state on the east span: Unedged

  Sequence number: 10

  Last known neighbour on the west span: 00e0-fc00-1a01

  Last known neighbour on the east span: 00e0-fc00-1a01

  Local topology state: Valid

表1-14 display rpr topology local命令显示信息描述表

字段

描述

Local station topology information on interface RPR-Router1

RPR-Router1接口对应的RPR站点的本地拓扑数据库信息

MAC address

站点MAC地址

Station name

站点名称

IP address

站点IP地址

Jumbo preference

是否支持Jumbo帧：

·Regular：表示不支持

·Jumbo：表示支持

Active protection mode

站点的保护倒换模式

Protection state on the west span

站点东向Span保护状态：

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

Protection state on the east span

站点西向Span保护状态：

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

Edge state on the west span

站点西向Span的Edge状态：

·Edged：表示发生edge

·Unedged：表示没有发生edge

Edge state on the east span

站点东向Span的Edge状态：

·Edged：表示发生edge

·Unedged：表示没有发生edge

Sequence number

TP帧序列号

Last known neighbour on the west span

西向最后学习到的邻站点

Last known neighbour on the east span

东向最后学习到的邻站点

Local topology state

本站点拓扑状态：

·Start：表示拓扑初始化

·Stable：表示拓扑稳定

·Unstable：表示拓扑不稳定

·Valid：表示拓扑有效

·Invalid：表示拓扑无效

\# 显示环路级的拓扑信息。

\<Sysname\>display rpr topology ring

Ring-level topology information on interface RPR-Router1:

  Number of stations on Ringlet0: 1

  Number of stations on Ringlet1: 1

  Total number of stations on the ring: 2

  Jumbo preference: Regular

  Ring topology type: Closed ring

表1-15 display rpr topology ring命令显示信息描述表

字段

描述

Ring-level topology information on interface RPR-Router1

RPR-Router1接口对应的RPR站点所在RPR环的环路拓扑信息

Number of stations on Ringlet0

站点在西向Span上的站点数

Number of stations on Ringlet1

站点在东向Span上的站点数

Total number of stations on the ring

站点所在环上总站点数

Jumbo preference

是否支持Jumbo帧：

·Regular：表示不支持

·Jumbo：表示支持

Ring topology type

环状态：

·Open ring：表示开环

·Closed ring：表示闭环

\# 显示环上所有站点拓扑信息。

\<Sysname\>display rpr topology stations

Station topology information on interface RPR-Router1:

 Station entry on Ringlet0:

  MAC address: 00e0-fc00-1a01

  Station name: StationA

  IP address: -

Hops: 1

  Jumbo preference: Regular

  Protection mode: Steer

  Protection state on the west span: IDLE

  Protection state on the east span: IDLE

  Edge state on the west span: Unedged

  Edge state on the east span: Unedged

  Sequence number: 9

  Reachability: Reachable

  Valid: 1

 Station entry on Ringlet1:

  MAC address: 00e0-fc00-1a01

  Station name: StationB

  IP address: -

 Hops: 1

  Jumbo preference: Regular

  Protection mode: Steer

  Protection state on the west span: IDLE

  Protection state on the east span: IDLE

  Edge state on the west span: Unedged

  Edge state on the east span: Unedged

  Sequence number: 9

  Reachability: Reachable

  Valid: 1

表1-16 display rpr topology stations命令显示信息描述表

字段

描述

Station topology information on interface RPR-Router1

RPR-Router1接口对应的RPR站点所在RPR环的其它站点的拓扑信息

Station entry on Ringlet0

西向Span上邻站点的拓扑信息

Station entry on Ringlet1

东向Span上邻站点的拓扑信息

MAC address

站点MAC地址

Station name

站点名称

IP address

站点IP地址

Hops

该站点到本地站点的跳数

Jumbo preference

是否支持Jumbo帧：

·Regular：表示不支持

·Jumbo：表示支持

Protection mode

站点的保护倒换模式

Protection state on the west span

站点西向Span的保护状态：

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

Protection state on the east span

站点东向Span的保护状态：

·FS：强制倒换状态

·SF：信号失效状态

·SD：信号衰减状态

·MS：手工倒换状态

·WTR：等待恢复状态

·IDLE：空闲状态

Edge state on the west span

站点西向Span是否出现Edge：

·Edged：表示发生edge

·Unedged：表示没有发生edge

Edge state on the east span

站点东向Span是否出现Edge：

·Edged：表示发生edge

·Unedged：表示没有发生edge

Sequence number

TP帧序列号

Reachability

站点是否可达：

·Reachable：表示可达

·Unreachable：表示不可达

Valid

表项是否有效：

·1：表示有效

·0：表示无效

![说明](RPR命令.files/image002.png)

·当RPR逻辑接口没有与RPR物理接口绑定时，显示本站点拓扑信息时只显示站点名和站点IP。

·当RPR逻辑接口没有与RPR物理接口绑定时，站点拓扑信息将无信息显示。

**RPR \-- RPR配置命令 \-- flag c2**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flag**]**c2**命令用来配置信号标记字节C2。

**[undo** **flag**]**c2**命令用来恢复缺省情况。

【命令】

**[flag**] **c2** *flag-value*

**[undo**] **flag** **c2**

【缺省情况】

信号标记字节C2的值为0x16。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[flag-value*]：表示信号标记字节C2，取值范围为0x00～0xFF。

【使用指导】

信号标记字节C2属于高阶通道开销字节，用于指示虚拟容器VC（Virtual Container）帧的复接结构和信息净负荷的性质。

需要注意的是，C2字节的配置一定要使收、发两端相匹配，否则会产生告警。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0的信号标记字节C2为0x01。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 flag c2 01

【相关命令】

·**display** **interface**

**RPR \-- RPR配置命令 \-- flag j0**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flag**]**j0**命令用来配置SONET/SDH帧的再生段踪迹字节J0。

**[undo** **flag**]**j0**命令用来恢复缺省情况。

【命令】

**[flag**  **j0** { **sdh** \| **sonet** } *flag-value*]

**[undo**  **flag** **j0** { **sdh** \| **sonet** }]

【缺省情况】

系统使用SDH帧格式的缺省值，SDH帧格式下再生段踪迹字节J0的缺省值为空。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[flag-value*]：表示再生段踪迹字节J0。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为0x00～0xFF。

**[sdh**]：表示帧格式为SDH（Synchronous Digital Hierarchy，同步数字系列）。

**[sonet**]：表示帧格式为SONET（Synchronous Optical Network，同步光网络）。

【使用指导】

再生段踪迹字节J0属于段开销字节（Section Overhead），用于检测两个接口之间的连接在段层次上的连续性。

需要注意的是，在同一个运营者的网络内J0字节可为任意字符，而在两个不同运营者的网络边界处要使设备收、发两端的J0字节相匹配。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0的SDH帧的再生段踪迹字节J0为0xFF。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 flag j0 sdh ff

【相关命令】

·**display** **interface**

·**frame-format**

**RPR \-- RPR配置命令 \-- flag j1**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flag**]**j1**命令用来配置SONET/SDH帧的通道踪迹字节J1。

**[undo** **flag**]**j1**命令用来恢复缺省情况。

【命令】

**[flag**  **j1** { **sdh** \| **sonet** } *flag-value*]

**[undo**  **flag** **j1** { **sdh** \| **sonet** }]

【缺省情况】

系统使用SDH帧格式的缺省值，SDH帧格式下通道踪迹字节J1的缺省值为空。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[flag-value*]：表示通道踪迹字节J1。SDH帧格式下*flag-value*的取值范围为1～15个字符的字符串；SONET帧格式下*flag-value*的取值范围为1～62个字符的字符串。

**[sdh**]：表示帧格式为SDH。

**[sonet**]：表示帧格式为SONET。

【使用指导】

通道踪迹字节J1属于高阶通道开销字节，用于检测两个接口之间的连接在通道层次上的连续性。

需要注意的是，J1字节的配置一定要使收、发两端相匹配，否则会产生告警。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0的SDH帧的通道踪迹字节J1为aabbcc。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 flag j1 sdh aabbcc

【相关命令】

·**display** **interface**

·**flag** **j1** **ignore**

·**frame-format**

**RPR \-- RPR配置命令 \-- flag j1 ignore**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flag** **j1** **ignore**]命令用来配置忽略对通道踪迹字节J1的检查。

**[undo** **flag** **j1** **ignore**]命令用来恢复缺省情况。

【命令】

**[flag** **j1** **ignore**]

**[undo** **flag** **j1** **ignore**]

【缺省情况】

需要对通道踪迹字节J1进行检查。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置RPR物理接口RPRPOS2/4/0忽略对通道踪迹字节J1的检查。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 flag j1 ignore

【相关命令】

·**flag** **j1**

**RPR \-- RPR配置命令 \-- flow-interval**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flow-interval**]命令用来配置接口统计报文信息的时间间隔。

**[undo** **flow-interval**]命令用来恢复缺省情况。

【命令】

**[flow-interval***interval*]

**[undo** **flow-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图

![说明](RPR命令.files/image003.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示接口统计信息的时间间隔，取值范围为5～300，单位为秒，步长为5。

【使用指导】

需要注意的是，系统视图下的全局配置对所有接口都生效，接口视图下的配置只对当前接口生效，如果设备同时支持这两种配置，则全局配置优先生效。

【举例】

\# 全局配置接口统计报文信息的时间间隔为100秒。

\<Sysname\> system-view

Sysname flow-interval 100

\# 配置RPR物理接口RPRGE2/2/0统计报文信息的时间间隔为100秒。

\<Sysname\> system-view

Sysname interface rprge 2/2/0

Sysname-RPRGE2/2/0 flow-interval 100

\# 配置RPR物理接口RPRXGE2/3/0统计报文信息的时间间隔为100秒。

\<Sysname\> system-view

Sysname interface rprxge 2/3/0

Sysname-RPRXGE2/3/0 flow-interval 100

\# 配置RPR物理接口RPRPOS2/4/0统计报文信息的时间间隔为100秒。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 flow-interval 100

**RPR \-- RPR配置命令 \-- frame-format**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[frame-format**]命令用来配置当前接口的帧格式。

**[undo**] **frame-format**命令用来恢复缺省情况。

【命令】

**[frame-format**  { **sdh** \| **sonet** }]

**[undo**] **frame-format**

【缺省情况】

接口的帧格式为SDH。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sdh**]：表示帧格式为SDH。

**[sonet**]：表示帧格式为SONET。

【使用指导】

通过**flag****j0**和**flag****j1**命令配置开销字节时，需要与帧格式匹配。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0的帧格式为SONET。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 frame-format sonet

【相关命令】

·**flag****j0**

·**flag****j1**

**RPR \-- RPR配置命令 \-- interface**

------------------------------------------------------------------------

**[interface**[ { **rprge** \| **rprpos** \| **rprxge** }]]命令用来进入RPR物理接口视图。

**[interface**[ { **rpr-bridge** \| **rpr-router** }]]命令用来创建RPR逻辑接口，并进入RPR逻辑接口视图。

**[undo**[ **interface** { **rpr-bridge** \| **rpr-router** }]]用来删除已创建的RPR逻辑接口。

【命令】

**[interface**[ { **rprge** \| **rprpos** \| **rprxge** } *interface-number*]]

**[interface**[ { **rpr-bridge** \| **rpr-router** } *interface-number*]]

**[undo**[ **interface** { **rpr-bridge** \| **rpr-router** } *interface-number*]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rprge**]：表示RPRGE接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprpos**]：表示RPRPOS接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprxge**]：表示RPRXGE接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rpr-bridge**]：表示二层RPR逻辑接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rpr-router**]：表示三层RPR逻辑接口。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

*[interface-number*]：表示RPR接口的编号。

【使用指导】

如果指定的RPR逻辑接口不存在，则**interface**[ { **rpr-bridge** \| **rpr-router** }]命令先完成RPR逻辑接口的创建，然后再进入该逻辑接口的视图。

【举例】

\# 创建二层RPR逻辑接口RPR-Bridge1，并进入其视图。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname- RPR-Bridge1{.TerminalDisplayChar}

\# 创建三层RPR逻辑接口RPR-Router1，并进入其视图。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1

\# 进入RPR物理接口RPRGE2/3/0的视图。

\<Sysname\> system-view

Sysname interface rprge 2/3/0

Sysname-RPRGE2/3/0

\# 进入RPR物理接口RPRXGE2/3/0的视图。

\<Sysname\> system-view

Sysname interface rprxge 2/3/0

Sysname-RPRXGE2/3/0

\# 进入RPR物理接口RPRPOS2/4/0的视图。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0

**RPR \-- RPR配置命令 \-- link-delay**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[link-delay**]命令用来配置当前接口的物理连接状态抑制时间。

**[undo** **link-delay**]命令用来恢复缺省情况。

【命令】

**[link-delay** **msec** *milliseconds*]

**[undo** **link-delay**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[msec** *milliseconds*]：表示接口物理连接状态的抑制时间，单位为毫秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

物理连接状态的抑制时间是指在接口发生up或down的时候，需要经过连接状态抑制时间后，接口状态才能变为up或down。使用本命令可以防止短时间内的接口物理连接状态变化对正常业务的影响。

需要注意的是，本命令和**dampening**命令不能同时使用。

![说明](RPR命令.files/image004.jpg)

本命令对up或down抑制的支持情况与设备的型号有关，请以设备的实际情况为准。即有些设备对up进行抑制，有些设备对down进行抑制，有些设备同时对up/down进行抑制。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0的物理连接状态抑制时间为100毫秒。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 link-delay msec 100

【相关命令】

·**dampening**

**RPR \-- RPR配置命令 \-- mtu**

------------------------------------------------------------------------

![说明](RPR命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mtu**]命令用来配置当前接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo** **mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo** **mtu**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：表示MTU值的大小，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

【举例】

\# 配置三层RPR逻辑接口RPR-Router1的MTU值为1492字节。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 mtu 1492

**RPR \-- RPR配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset** **counters** **interface**]命令用来清除RPR接口上的统计信息。

【命令】

**[reset**[ **counters** **interface** [ { **rpr-bridge** \| **rpr-router** \| **rprge** \| **rprpos** \| **rprxge** } [ *interface-number* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rpr-bridge**]：清除二层RPR逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rpr-router**]：清除三层RPR逻辑接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprge**]：清除RPRGE接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprpos**]：清除RPRPOS接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[rprxge**]：清除RPRXGE接口的信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

*[interface-number*]：表示RPR接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口上原有的统计信息，以便重新进行统计。

需要注意的是：

·如果未指定接口类型和接口编号，将清除所有接口上的统计信息。

·如果指定了接口类型而未指定接口编号，将清除所有已创建的指定类型接口的统计信息。

【举例】

\# 清除二层RPR逻辑接口RPR-Bridge1上的统计信息。

\<Sysname\> reset counters interface rpr-bridge 1

\# 清除三层RPR逻辑接口RPR-Router1上的统计信息。

\<Sysname\> reset counters interface rpr-router 1

\# 清除RPR物理接口RPRGE2/2/0上的统计信息。

\<Sysname\> reset counters interface rprge 2/2/0

\# 清除RPR物理接口RPRXGE2/3/0上的统计信息。

\<Sysname\> reset counters interface rprxge 2/3/0

\# 清除RPR物理接口RPRPOS2/4/0上的统计信息。

\<Sysname\> reset counters interface rprpos 2/4/0

【相关命令】

·**display** **interface**

**RPR \-- RPR配置命令 \-- reset rpr protection statistics**

------------------------------------------------------------------------

**[reset** **rpr** **protection** **statistics**]命令用来清除RPR站点的保护事件统计信息。

【命令】

**[reset**[ **rpr** **protection** **statistics** [ { **rpr-bridge** \| **rpr-router** } *interface-number* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：清除指定RPR逻辑接口对应的RPR站点的保护事件统计信息。如果未指定本参数，将清除所有RPR逻辑接口对应的RPR站点的保护事件统计信息。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

【举例】

\# 清除RPR站点的保护事件统计信息。

\<Sysname\> reset rpr protection statistics

**RPR \-- RPR配置命令 \-- rpr admin-request**

------------------------------------------------------------------------

**[rpr** **admin-request**]命令用来在指定子环上配置RPR保护请求。

【命令】

**[rpr**[ **admin-request** { **fs** \| **idle** \| **ms** } { **ringlet0** \| **ringlet1** }]]

【缺省情况】

子环上没有配置RPR保护请求。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fs**]：配置FS保护请求。

**[ms**]：配置MS保护请求。

**[idle**]：配置IDLE保护请求。

**[ringlet0**]：在0环上配置保护请求。

**[ringlet1**]：在1环上配置保护请求。

【使用指导】

保护请求包括FS（Forced Switch，强制倒换）、MS（Manual Switch，手工倒换）和IDLE（空闲），优先级从高到低，其中FS和MS是需要手工配置的。

·**rpr** **admin-request** **fs**命令用来产生FS保护请求。

·**rpr** **admin-request** **ms**命令用来产生MS保护请求。当站点发出MS保护请求时，若环上存在优先级更高的保护请求，MS保护请求将不被处理。需要指出的是，本地站点物理端口上的FS保护请求可以被本地站点相同物理端口上发出的MS保护请求抢占。

·**rpr** **admin-request** **idle**命令用来清除FS或者MS保护请求。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置0环的FS保护请求。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr admin-request fs ringlet0

\# 在三层RPR逻辑接口RPR-Router1上配置0环的FS保护请求。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr admin-request fs ringlet0

**RPR \-- RPR配置命令 \-- rpr bind**

------------------------------------------------------------------------

**[rpr** **bind**]命令用来配置RPR逻辑接口与RPR物理接口的绑定关系。

**[undo** **rpr** **bind**]命令用来取消RPR逻辑接口与RPR物理接口的绑定关系。

【命令】

在二层RPR逻辑接口视图或三层RPR逻辑接口视图下：

**[rpr**[ **bind** { { **rprge** \| **rprpos** \| **rprxge** } *interface-number* } { **ringlet0** \| **ringlet1** }]]

**[undo**[ **rpr** **bind** { { **rprge** \| **rprpos** \| **rprxge** } *interface-number* }]]

在RPRGE接口视图、RPRXGE接口视图或RPRPOS接口视图下：

**[rpr**[ **bind** { { **rpr-bridge** \| **rpr-router** } *interface-number* } { **ringlet0** \| **ringlet1** }]]

**[undo** **rpr** **bind**]

【缺省情况】

RPR逻辑接口与RPR物理接口未绑定。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

[[{ **rprge** \| **rprpos** \| **rprxge** } *interface-number*]]：指定RPR物理接口的接口类型和编号。不同型号的设备支持的RPR物理接口类型不同，请以设备的实际情况为准。

[[{ **rpr-bridge** \| **rpr-router** } *interface-number*]]：指定RPR逻辑接口的接口类型和编号。不同型号的设备支持的RPR逻辑接口类型不同，请以设备的实际情况为准。

**[ringlet0**]：把在0环上接收数据帧、在1环上发送数据帧的RPR物理接口绑定为RPR逻辑接口的西向接口。

**[ringlet1**]：把在0环上发送数据帧、在1环上接收数据帧的RPR物理接口绑定为RPR逻辑接口的东向接口。

【使用指导】

需要注意的是：

·一个RPR逻辑接口可以绑定两个RPR物理接口，一个RPR物理接口只能绑定一个RPR逻辑接口。

·RPR站点要正常工作，RPR逻辑接口至少要与一个RPR物理接口进行绑定。

·每一个RPR物理接口都有一MATE口，如果两个RPR物理接口绑定到了同一RPR逻辑接口，那么它们的MATE口必须连接起来。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上，将RPR物理接口RPRPOS2/4/0绑定为当前接口的西向接口。

\<Sysname\> system-view

sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr bind rprpos 2/4/0 ringlet0

\# 在三层RPR逻辑接口RPR-Router1上，将RPR物理接口RPRPOS2/4/0绑定为当前接口的西向接口。

\<Sysname\> system-view

sysname interface rpr-router 1

sysname-RPR-Router1 rpr bind rprpos 2/4/0 ringlet0

\# 在RPR物理接口RPRPOS2/4/0上，将当前接口绑定为二层RPR逻辑接口RPR-Bridge1的东向接口。

\<Sysname\> system-view

sysname interface rprpos 2/4/0

sysname-RPRPOS2/4/0 rpr bind rpr-bridge 1 ringlet1

\# 在RPR物理接口RPRPOS2/4/0上，将当前接口绑定为三层RPR逻辑接口RPR-Router1的东向接口。

\<Sysname\> system-view

sysname interface rprpos 2/4/0

sysname-RPRPOS2/4/0 rpr bind rpr-router 1 ringlet1

**RPR \-- RPR配置命令 \-- rpr default-rs ringlet1**

------------------------------------------------------------------------

**[rpr** **default-rs** **ringlet1**]命令用来配置RPR的默认选环为1环。

**[undo** **rpr** **default-rs**]命令用来恢复缺省情况。

【命令】

**[rpr** **default-rs** **ringlet1**]

**[undo** **rpr** **default-rs**]

【缺省情况】

RPR的默认选环为0环。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

默认选环就是指数据帧的缺省发送子环。

需要注意的是，当配置的默认选环因故障而不具备数据转发能力时，未发送故障的另一子环将成为生效的默认选还；而当两个子环都发生故障时，系统仍会把配置的默认选环视为生效的默认选环。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置RPR的默认选环为1环。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr default-rs ringlet1

\# 在三层RPR逻辑接口RPR-Router1上配置RPR的默认选环为1环。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr default-rs ringlet1

**RPR \-- RPR配置命令 \-- rpr echo mac**

------------------------------------------------------------------------

**[rpr** **echo** **mac**]命令用来检测当前站点与目的站点之间的连通性。

【命令】

**[rpr**[ **echo** **mac** *mac-address* [ **-c** *c-value* \| **-r** { **reverse** \| **ringlet0** \| **ringlet1** } \| **-s** { **ringlet0** \| **ringlet1** } \| **-t** *t-value* ] \*]]

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：检测到达该MAC地址的目的站点的连通性。

**[-c** *c-value*]：指定发送的Echo Request报文的数量，*c-value*的取值范围为1～1000，缺省值为5个。

**[-r**]：指定目点站点发送Echo Response报文的发送子环，取值为**reverse**、**ringlet0**和**ringlet1**。**reverse**表示目的站点将从与接收Echo Request报文子环的反方向子环发送Echo Response报文，缺省的发送环为实际生效的默认子环。例如，当目的站点从0环接收Echo Request报文时，则会从1环发送Echo Response报文。

**[-s**]：指定发送Echo Request报文的子环，取值为**ringlet0**和**ringlet1**，缺省的发送环为实际生效的默认子环。

**[-t** *t-value*]：指定站点等待目的站点应答的超时时间，*t-value*的取值范围为10～65535，单位为毫秒，缺省值为10毫秒。

【使用指导】

如果当前站点在指定子环上发送的Echo Request报文目的站点可以接收到，且目的站点在指定子环上发送的Echo Response报文当前站点也可以接收到，即只有当前站点和目的站点同时在指定发送子环和指定接收子环上连接正常时，则认为当前站点与目的站点之间连通，否则认为出现故障。

需要注意的是，如果没有指定发送子环和接收子环，源站点将根据综合选环表选择相应的子环发送Echo Request报文，目的站点也将根据综合选环表选择相应的子环发送Echo Response报文。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上检测到MAC地址为0012-3F83-A1E3的目的站点的连通性，指定的发送子环为0环、接收子环为1环。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr echo mac 0012-3F83-A1E3 -s ringlet0 -r ringlet1

Ping 0012-3F83-A1E3: press CTRL+C to break

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=2 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=3 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=4 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=5 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=6 time=1 ms

\-\-- Ping statistics for 0012-3F83-A1E3 \-\--

    5 packet(s) transmitted

    5 packet(s) received

    0.0% packet loss

    Round-trip min/avg/max = 1/1/1 ms

\# 在三层RPR逻辑接口RPR-Router1上检测到MAC地址为0012-3F83-A1E3的目的站点的连通性，指定的发送子环为0环、接收子环为1环。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr echo mac 0012-3F83-A1E3 -s ringlet0 -r ringlet1

Ping 0012-3F83-A1E3: press CTRL+C to break

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=2 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=3 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=4 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=5 time=1 ms

   Reply from 0012-3F83-A1E3: ringlet=1 hops=1 seq=6 time=1 ms

\-\-- Ping statistics for 0012-3F83-A1E3 \-\--

    5 packet(s) transmitted

    5 packet(s) received

    0.0% packet loss

    Round-trip min/avg/max = 1/1/1 ms

**RPR \-- RPR配置命令 \-- rpr mac-address**

------------------------------------------------------------------------

![说明](RPR命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rpr** **mac-address**]命令用来向RPR MAC地址表中添加表项，使到达指定VLAN目的站点的数据帧被单播到指定环上站点下环。

**[undo** **rpr** **mac-address**]命令用来删除指定的MAC地址表项。

【命令】

**[rpr**[ **mac-address** { **dynamic** \| **static** } **destination** *mac-address1* **vlan** *vlan-id* **ring** *mac-address2*]]

**[undo**[ **rpr** **mac-address** [ **dynamic** \| **static** ]  **destination** *mac-address1*   **vlan** *vlan-id*   **ring** *mac-address2* ]]

【缺省情况】

没有配置RPR MAC地址表项。

【视图】

二层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dynamic**]：添加RPR动态MAC地址表项。

**[static**]：添加RPR静态MAC地址表项。

*[mac-address1*]：目的以太网MAC地址。

*[mac-address2*]：下环站点MAC地址。

*[vlan-id*]：目的以太网MAC地址所属VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

需要注意的是，下环站点MAC地址必须为环上站点MAC地址，才能新增一条有效的MAC地址表项。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上添加如下RPR静态MAC地址表项：目的MAC地址为0011-43CA-7D45，属于VLAN 5，下环站点的MAC地址为2256-38B8-D92C。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1 rpr mac-address static destination 0011-43ca-7d45 vlan 5 ring 2256-38b8-d92c

【相关命令】

·**display** **rpr** **mac-address**

**RPR \-- RPR配置命令 \-- rpr mac-address timer**

------------------------------------------------------------------------

![说明](RPR命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[rpr** **mac-address** **timer**]命令用来配置RPR动态MAC地址表表项是否老化及老化时间。

**[undo** **rpr** **mac-address** **timer**]命令用来恢复缺省情况。

【命令】

**[rpr**[ **mac-address** **timer** { **aging** *seconds* \| **no-aging** }]]

**[undo** **rpr** **mac-address** **timer** **aging**]

【缺省情况】

RPR动态MAC地址表表项的老化时间为300秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aging** *seconds*]：RPR动态MAC地址表表项的老化定时器的值，*seconds*的取值范围为0～85899，单位为秒。

**[no-aging**]：配置RPR动态MAC地址表表项不老化。

【举例】

\# 配置RPR动态MAC地址表表项的老化时间为600秒。

\<Sysname\> system-view

Sysname rpr mac-address timer aging 600

【相关命令】

·**display** **rpr** **mac-address** **aging-time**

**RPR \-- RPR配置命令 \-- rpr mate smart-connect**

------------------------------------------------------------------------

![说明](RPR命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rpr** **mate** **smart-connect**]命令用来使能RPR MATE口的智能连接功能。

**[undo** **rpr** **mate** **smart-connect**]用来关闭RPR MATE口的智能连接功能。

【命令】

**[rpr** **mate** **smart-connect**]

**[undo** **rpr** **mate** **smart-connect**]

【缺省情况】

RPR MATE口的智能连接功能处于关闭状态。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过使能RPR MATE口的智能连接功能，当两个RPR物理接口在同一个子卡上时，RPR会自动把两个RPR物理接口的MATE口通过内部部件连接起来，不再需要将这两个RPR物理接口的MATE口用光纤在外部连接起来。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上使能RPR MATE口的智能连接功能。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr mate smart-connect

\# 在三层RPR逻辑接口RPR-Router1上使能RPR MATE口的智能连接功能。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr mate smart-connect

**RPR \-- RPR配置命令 \-- rpr port-type**

------------------------------------------------------------------------

![说明](RPR命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[rpr** **port-type**]命令用来改变RPR物理接口的类型。

【命令】

**[rpr**  **port-type** { **10ge** \| **10gpos** }]

【缺省情况】

RPR物理接口的类型与设备的型号有关，请以设备的实际情况为准。

【视图】

RPRXGE接口视图/RPRPOS接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[10ge**]：表示10GE类型。

**[10gpos**]：表示10GPOS类型。

【使用指导】

需要注意的是：

·改变RPR物理接口的类型后接口板会自动重启并切换到新类型，该接口上的原有配置将丢失；如果该接口原先被分配给非缺省MDC，在接口类型切换后该接口会被归还给缺省MDC，请重新进行配置。

·本命令仅对10GE和10GPOS的RPR物理接口起作用，若对GE或2.5GPOS的RPR物理接口执行本命令将返回错误提示信息。

【举例】

\# 改变RPR物理接口RPRXGE2/3/0的类型为10GPOS。

\<Sysname\> system-view

Sysname interface rprxge 2/3/0

Sysname-RPRXGE2/3/0 rpr port-type 10gpos

\# 改变RPR物理接口RPRPOS2/4/0的类型为10GE。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 rpr port-type 10ge

**RPR \-- RPR配置命令 \-- rpr protect-mode wrap**

------------------------------------------------------------------------

**[rpr** **protect-mode** **wrap**]命令用来配置站点的保护倒换模式为Wrapping模式。

**[undo** **rpr** **protect-mode**]命令用来恢复缺省情况。

【命令】

**[rpr**] **protect-mode** **wrap**

**[undo** **rpr** **protect-mode**]

【缺省情况】

站点的保护倒换模式为Steering模式。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置本站点的保护倒换模式为Wrapping模式。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr protect-mode wrap

\# 在三层RPR逻辑接口RPR-Router1上配置本站点的保护倒换模式为Wrapping模式。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysnamey-RPR-Router1 rpr protect-mode wrap

【相关命令】

·**display** **rpr** **protection**

**RPR \-- RPR配置命令 \-- rpr rate-limit**

------------------------------------------------------------------------

**[rpr** **rate-limit**]命令用来配置站点各类业务在指定子环上的预留带宽或速率限制。

**[undo** **rpr** **rate-limit**]命令用来恢复缺省情况。

【命令】

**[rpr**[ **rate-limit** { **high** \| **low** \| **medium** \| **reserved** } { **ringlet0** \| **ringlet1** } *value*]]

**[undo**[ **rpr** **rate-limit** { **high** \| **low** \| **medium** \| **reserved** } { **ringlet0** \| **ringlet1** }]]

【缺省情况】

A0类业务的预留带宽占总带宽的0‰，A1类业务的速率限制值为2‰，B-CIR类业务的速率限制值为0‰，B-EIR类业务和C类业务的速率限制值为1000‰。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[high**]：表示A1类业务。

**[low**]：表示B-EIR和C类业务。

**[medium**]：表示B-CIR类业务。

**[reserved**]：表示A0类业务。

**[ringlet0**]：表示各类业务在0环上的预留带宽或速率限制。

**[ringlet1**]：表示各类业务在1环上的预留带宽或速率限制。

*[value*]：A0类业务预留带宽占总带宽的千分比或B、C类业务的速率限制值，取值范围为0～1000，单位为千分之一。

【使用指导】

需要注意的是：

·配置了A0类业务的站点，为A0类业务预留的带宽总和不能超过环路带宽（即RPR逻辑口的带宽）。

·这里的0环、1环都是指发送子环。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置站点A0类业务在0环上的预留带宽占总带宽的5‰。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr rate-limit reserved ringlet0 5

\# 在三层RPR逻辑接口RPR-Router1上配置站点A0类业务在0环上的预留带宽占总带宽的5‰。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr rate-limit reserved ringlet0 5

**RPR \-- RPR配置命令 \-- rpr reversion-mode non-revertive**

------------------------------------------------------------------------

**[rpr**] **reversion-mode** **non-revertive**命令用来配置站点上保护倒换的恢复模式为不可恢复模式。**undo** **rpr** **reversion-mode**命令用来恢复缺省情况。

【命令】

**[rpr**] **reversion-mode** **non-revertive**

**[undo**] **rpr** **reversion-mode**

【缺省情况】

站点上保护倒换的恢复模式为可恢复模式。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上，将站点上保护倒换的恢复模式配置为不可恢复模式。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr reversion-mode non-revertive

\# 在三层RPR逻辑接口RPR-Router1上，将站点上保护倒换的恢复模式配置为不可恢复模式。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr reversion-mode non-revertive

**RPR \-- RPR配置命令 \-- rpr static-rs**

------------------------------------------------------------------------

**[rpr** **static-rs**]命令用来添加静态选环表项信息，使到达指定目的站点的数据帧通过指定子环发送。**undo** **rpr** **static-rs**命令用来删除到指定目的站点的静态选环表项信息。

【命令】

**[rpr**[ **static-rs** *mac-address* { **ringlet0** \| **ringlet1** }]]

**[undo** **rpr** **static-rs** *mac-address*]

【缺省情况】

不存在静态选环表项信息。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ringlet0**]：到指定目的站点的数据帧通过0环发送。

**[ringlet1**]：到指定目的站点的数据帧通过1环发送。

*[mac-address*]：目的站点MAC地址。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置到MAC地址为0001-0002-0003的目的站点的数据帧走0环，到MAC地址为0001-0002-0004的目的站点的数据帧走1环。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1 rpr static-rs 0001-0002-0003 ringlet0

Sysname-RPR-Bridge1 rpr static-rs 0001-0002-0004 ringlet1

\# 在三层RPR逻辑接口RPR-Router1上配置到MAC地址为0001-0002-0003的目的站点的数据帧走0环，到MAC地址为0001-0002-0004的目的站点的数据帧走1环。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr static-rs 0001-0002-0003 ringlet0

Sysname-RPR-Router1 rpr static-rs 0001-0002-0004 ringlet1

**RPR \-- RPR配置命令 \-- rpr station-name**

------------------------------------------------------------------------

**[rpr** **station-name**]命令用来配置RPR站点的名称。

**[undo** **rpr** **station-name**]命令用来删除已存在的RPR站点名称。

【命令】

**[rpr** **station-name** *station-name*]

**[undo** **rpr** **station-name**]

【缺省情况】

RPR站点没有配置任何名称。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[station-name*]：表示RPR站点的名称，取值范围为1～127个字符。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置本站点的名称为ABC。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr station-name ABC

\# 在三层RPR逻辑接口RPR-Router1上配置本站点的名称为ABC。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr station-name ABC

**RPR \-- RPR配置命令 \-- rpr timer**

------------------------------------------------------------------------

**[rpr** **timer**]命令用来配置各类RPR定时器。

**[undo** **rpr** **timer**]命令用来恢复缺省情况。

【命令】

**[rpr**[ **timer** { **atd** *atd-value* \| **holdoff** *holdoff-value* \| **keepalive** *keepalive-value* \| **stability** *stability-value* \| **tc-fast** *tc-fast-value* \| **tc-slow** *tc-slow-value* \| **tp-fast** *tp-fast-value* \| **tp-slow** *tp-slow-value* \| **wtr** *wtr-value* }]]

**[undo**[ **rpr** **timer** { **atd** \| **holdoff** \| **keepalive** \| **stability** \| **tc-fast** \| **tc-slow** \| **tp-fast** \| **tp-slow** \| **wtr** }]]

【缺省情况】

ATD帧定时器的值为1秒，Hold Off定时器的值为0毫秒，Keepalive定时器的值为3毫秒，拓扑稳定定时器的值为40毫秒，TC帧快发定时器的值为10毫秒，TC帧慢发定时器的值为100毫秒，TP帧快发定时器的值为10毫秒，TP帧慢发定时器的值为100毫秒，WTR定时器的值为10秒。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[atd** *atd-value*]：ATD帧定时器的值，*atd-value*的取值范围为1～10，单位为秒。

**[holdoff** *holdoff-value*]：Hold Off定时器的值，*holdoff-value*的取值范围为0～200，单位为毫秒，步长为10毫秒。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[keepalive** *keepalive-value*]：Keepalive定时器的值，*keepalive-value*的取值范围为2～200，单位为毫秒。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[stability** *stability-value*]：拓扑稳定定时器的值，*stability-value*的取值范围为10～100，单位为毫秒。

**[tc-fast** *tc-fast-value*]：TC帧快发定时器的值，*tc-fast-value*的取值范围为1～20，单位为毫秒。

**[tc-slow** *tc-slow-value*]：TC帧慢发定时器的值，*tc-slow-value*的取值范围为50～10000，单位为毫秒，步长为50毫秒。

**[tp-fast** *tp-fast-value*]：TP帧快发定时器的值，*tp-fast-value*的取值范围为1～20，单位为毫秒。

**[tp-slow** *tp-slow-value*]：TP帧慢发定时器的值，*tp-slow-value*的取值范围为50～10000，单位为毫秒，步长为50毫秒。

**[wtr** *wtr-value*]：WTR定时器的值，*wtr-value*的取值范围为0～1440，单位为秒。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置ATD帧定时器的值为3秒。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr timer atd 3

\# 在三层RPR逻辑接口RPR-Router1上配置ATD帧定时器的值为3秒。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr timer atd 3

【相关命令】

·**display** **rpr** **timers**

**RPR \-- RPR配置命令 \-- rpr weight**

------------------------------------------------------------------------

**[rpr** **weight**]命令用来配置站点的链路权重。

**[undo** **rpr** **weight**]命令用来恢复缺省情况。

【命令】

**[rpr**[ **weight** { **ringlet0** \| **ringlet1** } *value*]]

**[undo**[ **rpr** **weight** { **ringlet0** \| **ringlet1** }]]

【缺省情况】

站点在0环和1环上的链路权重均为1。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ringlet0**]：配置站点在0环上的链路权重。

**[ringlet1**]：配置站点在1环上的链路权重。

*[value*]：链路权重值，取值范围为1～255，必须是2的指数幂。

【举例】

\# 在二层RPR逻辑接口RPR-Bridge1上配置站点在0环上的链路权重为2。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} rpr weight ringlet0 2

\# 在三层RPR逻辑接口RPR-Router1上配置站点在0环上的链路权重为2。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 rpr weight ringlet0 2

**RPR \-- RPR配置命令 \-- scramble**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[scramble**]命令用来开启当前接口对载荷的加扰功能。

**[undo** **scramble**]命令用来关闭该功能。

【命令】

**[scramble**]

**[undo** **scramble**]

【缺省情况】

接口对载荷的加扰功能处于开启状态。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启加扰功能后，发送数据时采用加扰传输，接收数据时进行解扰，可避免出现过多连续的1或0，便于接收端提取线路时钟信号；关闭加扰功能后，发送数据时不采用加扰传输，接收数据时也不进行解扰。两端接口都打开或关闭对载荷的加扰功能，才能对接成功。

【举例】

\# 开启RPR物理接口RPRPOS2/4/0对载荷的加扰功能。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 scramble

**RPR \-- RPR配置命令 \-- service**

------------------------------------------------------------------------

**[service**]命令用来指定转发当前接口流量的业务处理板。

**[undo** **service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[service** **slot** *slot-number*]

**[undo** **service** **slot**]

分布式设备－IRF模式：

**[service** **chassis** *chassis-number* **slot** *slot-number*]

**[undo** **service** **chassis**]

【缺省情况】

流量会被接收该流量的RPR物理端口所在的单板直接进行处理。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：将指定单板作为处理当前接口流量的业务处理板。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：将指定该成员设备作为处理当前接口流量的业务处理板。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：将指定该成员设备/PEX作为处理当前接口流量的业务处理板。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：将指定成员设备上的指定单板作为处理当前接口流量的业务处理板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：将指定单板作为处理当前接口流量的业务处理板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

缺省情况下，流量会被接收该流量的RPR物理端口所在的单板直接进行处理。而某些业务（如IPsec抗重放检测）要求同一个RPR逻辑接口的流量必须在同一个单板/成员设备上进行处理，此时可以通过本命令指定转发当前接口流量的业务处理板。

需要注意的是，如果把本配置所指定的业务处理板拔出，将导致流量转发不通；重新插入该板后，流量可以恢复在该板的正常转发。

【举例】

·分布式设备－独立运行模式应用

\# 指定2号单板作为处理二层RPR逻辑接口RPR-Bridge1流量的业务处理板。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} service slot 2

\# 指定2号单板作为处理三层RPR逻辑接口RPR-Router1流量的业务处理板。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 service slot 2

·集中式IRF设备应用

\# 指定2号成员设备作为处理二层RPR逻辑接口RPR-Bridge1流量的业务处理板。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} service slot 2

\# 指定2号成员设备作为处理三层RPR逻辑接口RPR-Router1流量的业务处理板。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 service slot 2

·分布式设备－IRF模式应用

\# 指定2号成员设备的2号单板处理二层RPR逻辑接口RPR-Bridge1流量的业务处理板。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} service chassis 2 slot 2

\# 指定2号成员设备的2号单板处理三层RPR逻辑接口RPR-Router1流量的业务处理板。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 service chassis 2 slot 2

**RPR \-- RPR配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo** **shutdown**]命令用来打开当前接口。

【命令】

**[shutdown**]

**[undo** **shutdown**]

【缺省情况】

接口处于开启状态。

【视图】

二层RPR逻辑接口视图/三层RPR逻辑接口视图/RPRGE接口视图/RPRXGE接口视图/RPRPOS接口视图

![说明](RPR命令.files/image002.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭二层RPR逻辑接口RPR-Bridge1。

\<Sysname\> system-view

Sysname interface rpr-bridge 1

Sysname-RPR-Bridge1{.TerminalDisplayChar} shutdown

\# 关闭三层RPR逻辑接口RPR-Router1。

\<Sysname\> system-view

Sysname interface rpr-router 1

Sysname-RPR-Router1 shutdown

\# 关闭RPR物理接口RPRGE2/2/0。

\<Sysname\> system-view

Sysname interface rprge 2/2/0

Sysname-RPRGE2/2/0 shutdown

\# 关闭RPR物理接口RPRXGE2/3/0。

\<Sysname\> system-view

Sysname interface rprxge 2/3/0

Sysname-RPRXGE2/3/0 shutdown

\# 关闭RPR物理接口RPRPOS2/4/0。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 shutdown

**RPR \-- RPR配置命令 \-- snmp-agent trap enable { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[snmp-agent**[ **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来开启当前接口的B1/B2/B3告警功能。

**[undo**[ **snmp-agent** **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来关闭当前接口的B1/B2/B3告警功能。

【命令】

**[snmp-agent**[ **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

**[undo**[ **snmp-agent** **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

【缺省情况】

RPRPOS接口的B1/B2/B3告警功能处于开启状态。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

B1/B2/B3告警都是用于指示SDH体制线路的当前信号传输性能的，只是三者关注的信号层次不一样：

·B1检验的是当前传输信号STM-N帧的整体误码情况。

·B2检验的是传输信号基本组成单元STM-1帧的误码情况。

·B3检验的是STM-1帧封装的复用信号（VC3或VC4帧）的误码情况。

当开启了RPRPOS接口的B1/B2/B3告警功能后，设备将在RPRPOS接口的误码超过B1/B2/B3告警门限时生成告警信息。生成的告警信息将发送到设备的SNMP模块，通过配置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 关闭RPR物理接口RPRPOS2/4/0的B1告警功能。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 undo snmp-agent trap enable b1-tca

【相关命令】

[·**threshold**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

**RPR \-- RPR配置命令 \-- threshold**

------------------------------------------------------------------------

![说明](RPR命令.files/image004.jpg)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[threshold**]命令用来配置当前接口的SD告警门限和（或）SF告警门限。

**[undo** **threshold**]命令用来恢复缺省情况。

【命令】

**[threshold** { **sd** *sdvalue* \| **sf** *sfvalue* } \*]

**[undo** **threshold**  [ **sd** \| **sf** ]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

RPRPOS接口视图

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

\# 配置RPR物理接口RPRPOS2/4/0的SD告警门限为10e-4。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 threshold sd 4

**RPR \-- RPR配置命令 \-- threshold { b1-tca \| b2-tca \| b3-tca }**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[threshold**[ { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来配置当前接口的B1/B2/B3告警门限。

**[undo**[ **threshold** { **b1-tca** \| **b2-tca** \| **b3-tca** }]]命令用来恢复缺省情况。

【命令】

**[threshold**[ { **b1-tca** *b1value* \| **b2-tca** *b2value* \| **b3-tca** *b3value* }]]

**[undo**[ **threshold** { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

RPRPOS接口视图

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

当开启了RPRPOS接口的B1/B2/B3告警功能后，设备将在RPRPOS接口的误码超过B1/B2/B3告警门限时生成告警信息。

【举例】

\# 配置RPR物理接口RPRPOS2/4/0的B1告警门限为10e-4。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 threshold b1-tca 4

【相关命令】

[·**snmp-agent**[ **trap** **enable** { **b1-tca** \| **b2-tca** \| **b3-tca** }]]

**RPR \-- RPR配置命令 \-- timer-hold**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[timer-hold**]命令用来配置Keepalive报文的发送周期。

**[undo** **timer-hold**]命令用来恢复缺省情况。

【命令】

**[timer-hold** *seconds*]

**[undo** **timer-hold**]

【缺省情况】

Keepalive报文的发送周期为10秒。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：Keepalive报文的发送周期，取值范围为0～32767，单位为秒。

【使用指导】

当接口上封装的链路层协议为PPP、FR或HDLC时，链路层会定期（可通过本命令修改）向对端发送Keepalive报文。如果在一段时间内无法收到对端发来的Keepalive报文，链路层会认为对端故障，从而上报链路层down。

在速率非常低的链路上，Keepalive报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟Keepalive报文的收发。而接口在若干个（可通过**timer-hold retry**命令修改）Keepalive报文发送周期后仍未收到对端发来的Keepalive报文，就认为链路发生故障，从而拆除链路。

【举例】

\# 在RPR物理接口RPRPOS2/4/0上配置Keepalive报文的发送周期为15秒。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 timer-hold 15

【相关命令】

·**timer-hold retry**

**RPR \-- RPR配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

![说明](RPR命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[timer-hold retry**]命令用来配置在多少个Keepalive报文发送周期内未收到应答就拆除链路。

**[undo** **timer-hold retry**]命令用来恢复缺省情况。

【命令】

**[timer-hold retry** *retry*]

**[undo** **timer-hold retry**]

【缺省情况】

在5个Keepalive报文发送周期内未收到应答就拆除链路。

【视图】

RPRPOS接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retry*]：在多少个Keepalive报文发送周期内未收到应答就拆除链路，取值范围为1～255，单位为秒。

【使用指导】

当接口上封装的链路层协议为PPP、FR或HDLC时，链路层会定期（可通过**timer-hold**命令修改）向对端发送Keepalive报文。如果在一段时间内无法收到对端发来的Keepalive报文，链路层会认为对端故障，上报链路层Down。

在速率非常低的链路上，Keepalive报文的发送周期不能过小，因为大报文在低速链路上可能需要很长时间才能传送完毕，这样就会延迟Keepalive报文的收发。而接口在若干个（可通过本命令修改）Keepalive报文发送周期后仍未收到对端发来的Keepalive报文，就认为链路发生故障，从而拆除链路。

【举例】

\# 在RPR物理接口RPRPOS2/4/0上，配置在10个Keepalive报文发送周期内未收到应答就拆除链路。

\<Sysname\> system-view

Sysname interface rprpos 2/4/0

Sysname-RPRPOS2/4/0 timer-hold retry 10

【相关命令】

·**timer-hold**

