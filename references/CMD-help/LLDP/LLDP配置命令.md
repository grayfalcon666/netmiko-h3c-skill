<!-- CMD-INDEX
  cdp voice-vlan                      | 二层以太网接口视图        | L32
  dcbx version                        | 二层以太网接口视图        | L80
  display lldp local-information      | 任意视图             | L144
  display lldp neighbor-information   | 任意视图             | L1016
  display lldp statistics             | ]                | L2542
  display lldp status                 | 任意视图             | L2796
  display lldp tlv-config             | 任意视图             | L3044
  lldp admin-status                   | 二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图 | L3408
  lldp check-change-interval          | 二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图 | L3474
  lldp compliance admin-status cdp    | 二层以太网接口视图/三层以太网接口视图/管理以太网接口视图 | L3534
  lldp compliance cdp                 | 系统视图             | L3596
  lldp enable                         | 二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图 | L3646
  lldp encapsulation snap             | 二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图 | L3696
  lldp fast-count                     | 系统视图             | L3760
  lldp global enable                  | 系统视图             | L3800
  lldp hold-multiplier                | 系统视图             | L3844
  lldp management-address             | 三层以太网接口视图        | L3892
  lldp management-address-format string | 二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图 | L3946
  lldp max-credit                     | 系统视图             | L4008
  lldp mode                           | 系统视图             | L4048
  lldp notification med-topology-change enable | 二层以太网接口视图/三层以太网接口视图/管理以太网接口视图 | L4104
  lldp notification remote-change enable | 二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图 | L4146
  lldp source-mac vlan                | 三层以太网接口视图        | L4204
  lldp timer fast-interval            | 系统视图             | L4250
  lldp timer notification-interval    | 系统视图             | L4290
  lldp timer reinit-delay             | 系统视图             | L4330
  lldp timer tx-interval              | 系统视图             | L4370
  lldp tlv-enable                     |                  | L4410
-->

**LLDP \-- LLDP配置命令 \-- cdp voice-vlan**

------------------------------------------------------------------------

**[cdp voice-vlan**]命令用来配置CDP报文携带的Voice VLAN ID。

**[undo cdp voice-vlan**]命令用来恢复缺省情况。

【命令】

**[cdp voice-vlan ***vlan-id*]

**[undo cdp voice-vlan**]

【缺省情况】

未配置CDP报文携带的Voice VLAN ID。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：要发布的Voice VLAN ID，取值范围为1～4094。

【使用指导】

配置本命令后，设备当前接口向对端IP电话发送的CDP报文携带的Voice VLAN ID为本命令配置的VLAN ID。

对端IP电话收到本端发送的CDP报文后，会根据报文中携带的Voice VLAN ID发送语音数据。

【举例】

\# 配置CDP报文携带的Voice VLAN ID为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 cdp voice-vlan 100

**LLDP \-- LLDP配置命令 \-- dcbx version**

------------------------------------------------------------------------

![说明](LLDP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[dcbx version**]命令用来配置DCBX版本。

**[undo dcbx version**]命令用来恢复缺省情况。

【命令】

**[dcbx version **[{ **rev100** \| **rev101** \| **standard** }]]

**[undo dcbx version**]

【缺省情况】

未配置DCBX版本，此时DCBX版本由两端端口自协商决定。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rev100**]：表示采用预标准版1.00。

**[rev101**]：表示采用预标准版1.01。

**[standard**]：表示采用标准版。

【使用指导】

·配置本命令时，配置的DCBX版本需要视对端设备支持的版本而定，要求两端端口的DCBX版本配置一致，否则版本无法兼容，将会导致DCBX无法正常工作。建议配置两端设备都支持的最高版本（版本从高到低的顺序为：标准版-\>预标准版1.01-\>预标准版1.00）。

·配置本命令后，本端端口发送的LLDP报文中携带的DCBX版本为配置的版本，不再与对端端口进行DCBX版本协商。

·当端口的DCBX版本采用自协商决定，协商的初始版本为DCBX标准版，以保证优先协商到该版本。

【举例】

\# 配置接口GigabitEthernet1/0/1的DCBX版本为预标准版1.01。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dcbx version rev101

【相关命令】

·**lldp tlv-enable**

**LLDP \-- LLDP配置命令 \-- display lldp local-information**

------------------------------------------------------------------------

**[display lldp local-information**]命令用来显示LLDP本地信息，这些信息将根据端口TLV开启情况被组织成TLV发送给邻居设备。

【命令】

**[display lldp local-information**[ [ **global** \| **interface** *interface-type interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示全局LLDP本地信息。

**[interface** *interface-type interface-number*]：显示指定接口上的LLDP本地信息，*interface-type interface-number*表示接口类型和接口编号。

【使用指导】

如果未指定任何参数，将显示所有LLDP本地信息，包括全局LLDP信息以及所有开启了LLDP功能且状态为up的接口上的LLDP信息。

【举例】

\# 显示所有LLDP本地信息（假设DCBX的版本为标准版）。

\<Sysname\> display lldp local-information

Global LLDP local-information:

 Chassis ID          : 00e0-fc00-5600

 System name         : Sysname

 System description  : H3C Comware Platform Software

 System capabilities supported  : Bridge, Router, Customer Bridge, Service Bridge

 System capabilities enabled    : Bridge, Router, Service Bridge

 MED information:

 Device class               : Connectivity device

 MED inventory information of master board:

 HardwareRev                : REV.A

 FirmwareRev                : 109

 SoftwareRev                : 5.20 Alpha 2101

 SerialNum                  : NONE

 Manufacturer name          : H3C

 Model name                 : H3C Comware

 Asset tracking identifier  : Unknown

LLDP local-information of port 52[GigabitEthernet1/0/3:]

 Port ID type       : Interface name

 Port ID            : GigabitEthernet1/0/3

 Port description   : GigabitEthernet1/0/3 Interface

 LLDP agent nearest-bridge management address:

 Management address type           : IPv4

 Management address                : 192.168.80.60

 Management address interface type : IfIndex

 Management address interface ID   : Unknown

 Management address OID            : 0

 LLDP agent nearest-nontpmr management address:

 Management address type           : IPv4

 Management address                : 192.168.80.61

 Management address interface type : IfIndex

 Management address interface ID   : Unknown

 Management address OID            : 0

 LLDP agent nearest-customer management address:

 Management address type           : IPv4

 Management address                : 192.168.80.62

 Management address interface type : IfIndex

 Management address interface ID   : Unknown

 Management address OID            : 0

 DCBX Control info:

 Oper version       : Standard

 DCBX ETS configuration info:

  CBS                : False

  Max TCs            : 8

  CoS     Local Priority      Percentage        TSA

   0            0                 15            ETS

   1            1                 0             SP

   2            2                 15            ETS

   3            3                 14            ETS

   4            4                 14            ETS

   5            5                 14            ETS

   6            6                 14            ETS

   7            7                 14            ETS

 DCBX ETS recommendation info:

  CoS     Local Priority      Percentage        TSA

   0            0                 15            ETS

   1            1                 0             SP

   2            2                 15            ETS

   3            3                 14            ETS

   4            4                 14            ETS

   5            5                 14            ETS

   6            6                 14            ETS

   7            7                 14            ETS

 DCBX PFC info:

  P0-0     P1-1     P2-1     P3-1     P4-0     P5-0     P6-0     P7-0

  Number of traffic classes supported: 8

  Value of MBC: 0

 DCBX APP info:

  Selected Field  Protocol ID  Priority

  UDP/DCCP        100          0x3

  TCP/SCTP        200          0x3

  Ethertype       0x1234       0x3

  Ethertype       0x8906       0x3

 Port VLAN ID(PVID): 1

 Port and protocol VLAN ID(PPVID) : 12

 Port and protocol VLAN supported : Yes

 Port and protocol VLAN enabled   : Yes

 VLAN name of VLAN 12: VLAN 0012

 Management VLAN ID  : 5

 Auto-negotiation supported : Yes

 Auto-negotiation enabled   : Yes

 OperMau                    : Speed(1000)/Duplex(Full)

 Power port class           : PD

 PSE power supported        : Yes

 PSE power enabled          : Yes

 PSE pairs control ability  : Yes

 Power pairs                : Signal

 Port power classification  : Class 0

 Power type                 : Type 2 PSE

 Power source               : Primary

 Power priority             : High

 PD requested power value   : 21.1 w

 PSE allocated power value  : 15.3 w

 Link aggregation supported : Yes

 Link aggregation enabled   : Yes

 Aggregation port ID        : 52

 Congestion notification TLV info:

  Dot1p          CNPV         Ready

  0              Yes          Yes

  1              No           No

  2              No           No

  3              No           No

  4              Yes          No

  5              Yes          Yes

  6              No           No

  7              No           No

 Maximum frame size         : 1500

 Transmit Tw                : 100 us

 Receive Tw                 : 90 us

 Fallback Tw                : 90 us

 Echo Transmit Tw           : 0 us

 Echo Receive Tw            : 0 us

 Location format       : Civic Address LCI

 Location information  :

  What(1)  Country(CN)

  CA type  CA value

  0        Chinese

  1        Zhejiang

  2        Hangzhou

 MED port information:

  Media policy type        : Unknown

  Unknown policy           : Yes

  VLAN tagged              : No

  Media policy VLANID      : 0

  Media policy L2 priority : 0

  Media policy DSCP        : 0

 PoE PSE power source       : Primary

 Port PSE priority          : Critical

 Port available power value : 30.0 w

![说明](LLDP命令.files/image001.png)

本命令的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-1 display lldp local-information命令显示信息描述表

字段

描述

Global LLDP local-information

本设备的全局LLDP本地信息

Chassis ID

Chassis ID值，为本设备的桥MAC地址

System name

系统名称

System description

系统描述

System capabilities supported

系统所支持的功能：

·Bridge：表示支持交换功能

·Router：表示支持路由功能

·WlanAccessPoint：表示支持无线接入点功能

·Router：表示支持路由功能

·Telephone：表示支持电话功能

·DocsisCableDevice：表示支持电缆设备功能

·StationOnly：表示支持只作站点功能

·Customer Bridge：表示支持客户桥功能

·Service Bridge：表示支持服务桥功能

·TPMR：表示支持双端口MAC中继功能

·Other：表示支持不在上述列表的其它功能

System capabilities enabled

系统已开启的功能：

·Bridge：表示交换功能已开启

·Router：表示路由功能已开启

·WlanAccessPoint：表示无线接入点功能已开启

·Router：表示路由功能已开启

·Telephone：表示电话功能已开启

·DocsisCableDevice：表示电缆设备功能已开启

·StationOnly：表示只作站点功能已开启

·Customer Bridge：表示客户桥功能已开启

·Service Bridge：表示服务桥功能已开启

·TPMR：表示双端口MAC中继功能已开启

·Other：表示不在上述列表的其它功能已开启

MED information

MED设备相关信息

Device class

MED设备类型：

·Connectivity device：表示网络设备

·Class I：表示一般终端设备，即所有需要LLDP发现服务的终端设备

·Class II：表示媒体终端设备，即具备媒体能力的终端设备，其能力包含了一般终端设备的能力。该类设备支持媒体流

·Class III：表示通讯终端设备，即直接支持目标用户IP通讯系统的终端设备，其能力包含了一般终端设备和媒体终端设备的所有能力。该类设备直接被目标用户所使用

MED inventory information of master board

主控板MED资产信息

HardwareRev

产品的硬件版本

FirmwareRev

产品的固件版本

SoftwareRev

产品的软件版本

SerialNum

序列号

Manufacturer name

制造厂商

Model name

模块名称

Asset tracking identifier

资产跟踪ID

LLDP local-information of port 1

端口1上LLDP本地信息

Port ID type

端口ID类型：

·MAC address：表示MAC地址

·Interface name：表示接口名称

Port ID

端口ID值，根据本设备的Port ID type取相应类型的值

Port description

端口描述

LLDP agent nearest-bridge management address

LLDP缺省代理，即最近桥代理的管理地址

LLDP agent nearest-customer management address

LLDP最近客户桥代理的管理地址

LLDP agent nearest-nontpmr management address

LLDP最近非TPMR桥代理的管理地址

Management address type

管理地址类型

Management address

管理地址

Management address interface type

管理地址所在接口的编码方式

Management address interface ID

管理地址接口索引

Management address OID

管理地址对象标识符

DCBX control info

显示DCBX控制TLV的信息，在标准DCBX中显示版本信息

Oper version

DCBX版本号

Sequence number

DCBX TLV内容改变的次数

Acknowledge number

对端设备同步配置的次数

DCBX ETS info

CoS与本地优先级的映射关系及对应的带宽分配情况

CoS

CoS值

Local Priority

本地优先级

Percentage

对应的带宽分配

P0-     P1-     P2-     P3-     P4-     P5-     P6-     P7-

本端的no-drop标记值对应的支持的优先级数

Number of traffic classes supported

PFC支持的能力集，只在1.01版本中显示该项

DCBX APP info

显示APP TLV信息

Selected Field

选择域

Priority

优先级

Protocol ID

应用协议号

CoS map

应用协议与CoS的映射关系

DCBX ETS configuration info

显示ETS配置TLV信息

CBS

是否支持CBS，表示本端是否支持令牌桶限速算法：

·False：表示不支持令牌桶限速算法

·True：表示支持令牌桶限速算法

Max TCs

支持的最大优先级数目

TSA

传输选择算法

DCBX ETS recommendation info

显示ETS推荐TLV信息

DCBX PFC info

显示PFC TLV信息

Value of MBC

支持的MBC状态（MBC表示报文避开MACsec的能力，占1个bit，取值为0表示MACsec去开启时，报文可以避开MACsec，取值为1表示MACsec关闭时，报文不可以避开MACsec）

Port VLAN ID(PVID)

端口VLAN ID

Port and protocol VLAN ID(PPVID)

端口协议VLAN ID

Port and protocol VLAN supported

是否支持端口协议VLAN

Port and protocol VLAN enabled

是否已开启端口协议VLAN

VLAN name of VLAN 12

VLAN 12的名称

Management VLAN ID

管理VLAN ID

Auto-negotiation supported

端口是否支持自协商

Auto-negotiation enabled

端口是否已开启自协商

OperMau

端口自适应的速率和双工状态

Power port class

PoE类型：

·PSE（Power Sourcing Equipment,供电设备）

·PD（Powered Device，受电设备）

PSE power supported

是否支持PSE供电

PSE power enabled

是否已开启PSE供电

PSE pairs control ability

供电方式是否可控

Power pairs

PoE端口的远程供电模式：

·Signal：表示信号线供电模式

·Spare：表示空闲线供电模式

Port power classification

PD的端口控制级别：

·Class 0：表示级别0

·Class 1：表示级别1

·Class 2：表示级别2

·Class 3：表示级别3

·Class 4：表示级别4

Power type

供电类型：

·Type 1 PD：表示类型1 PD

·Type 2 PD：表示类型2 PD

·Type 1 PSE：表示类型1 PSE

·Type 2 PSE：表示类型2 PSE

Power source

功率来源（功率来源根据供电类型为PD类型或PSE类型，取值不同）：

PSE

·Unknown：表示采用的电源类型未知

·Primary：表示采用主用电源作为电源

·Backup：表示采用备用电源作为电源

·Reserved：保留

PD

·Unknown：表示采用的电源类型未知

·PSE：表示采用PSE作为电源

·Local：表示采用本地电源作为电源

·PSE and local：表示采用PSE和本地电源作为电源

Power priority

功率优先级：

·Unknown：表示优先级未知

·Critical：表示优先级为1级

·High：表示优先级为2级

·Low：表示优先级为3级

PD requested power value

PD请求功率值，单位为瓦特

PSE allocated power value

PSE分配功率值，单位为瓦特

Link aggregation supported

端口是否支持链路聚合

Link aggregation enabled

端口是否已开启链路聚合

Aggregation port ID

聚合组中该成员端口的编号，未开启链路聚合功能时为0

Congestion notification TLV info

拥塞通知TLV信息。本字段的支持情况与设备型号有关，请以设备的实际情况为准

Dot1p

802.1p优先级

CNPV

802.1p优先级是否被配置为CNPV（Congestion Notification Priority Value，拥塞通知优先级值），表明是否加入了对应CNPV域：

·Yes：表示802.1p优先级被配置为CNPV

·No：表示802.1p优先级未被配置为CNPV

Ready

表明设备接口是否已经关闭了802.1p优先级与隔离优先级的映射：

·Yes：表示关闭优先级映射

·No：表示未关闭优先级映射

Maximum frame size

端口支持的最大帧长度

Media policy type

媒体策略类型：

·Unknown：表示类型未知

·Voice：表示语音

·VoiceSignaling：表示语音信号

·GuestVoice：表示访客语音

·GuestVoiceSignaling：表示访客语音信号

·SoftPhoneVoice：表示软体电话语音

·Videoconferencing：表示视频会议

·StreamingVideo：表示流视频

·VideoSignaling：表示视频信号

Unknown policy

媒体策略类型是否未知：

·Yes：表示策略类型未知

·No：表示策略类型已知

VLAN tagged

媒体VLAN是否带Tag

Media policy VLANID

媒体VLAN的VLAN ID

Media policy L2 priority

二层优先级

Media policy DSCP

DSCP的值

Location format

位置信息格式：

·Invalid：表示无效位置数据类型

·Coordinate-based LCI：表示基于坐标的位置信息

·Civic Address LCI：表示普通地址信息

·ECS ELIN：表示紧急电话号码

Location information

位置信息

PoE PSE power source

PSE所采用的电源类型：

·Unknown：表示采用的电源类型未知

·Primary：表示采用主用电源作为电源

·Backup：表示采用备用电源作为电源

PoE PD power source

PD所采用的电源类型：

·Unknown：表示采用的电源类型未知

·PSE：表示采用PSE作为电源

·Local：表示采用本地电源作为电源

·PSE and local：表示采用PSE和本地电源作为电源

Port PSE priority

PSE上端口的供电优先级：

·Unknown：表示优先级未知

·Critical：表示优先级为1级

·High：表示优先级为2级

·Low：表示优先级为3级

Port PD priority

PD上端口的受电优先级：

·Unknown：表示优先级未知

·Critical：表示优先级为1级

·High：表示优先级为2级

·Low：表示优先级为3级

Port available power value

PSE上端口可提供的功率，或PD上端口所需的功率，单位为瓦特

Transmit Tw

本端发送的等待时间，单位为微秒

Receive Tw

本端向对端请求的等待时间，单位为微秒

Fallback Tw

本端向对端请求的候选等待时间，单位为微秒

Echo Transmit Tw

收到的对端发送的等待时间，单位为微秒

Echo Receive Tw

收到的对端请求的等待时间，单位为微秒

**LLDP \-- LLDP配置命令 \-- display lldp neighbor-information**

------------------------------------------------------------------------

**[display lldp neighbor-information**]命令用来显示由邻居设备发来的LLDP信息，这些信息是由邻居设备组织成TLV并发送给本设备的。

【命令】

**[display lldp neighbor-information** [ [ [ **interface** *interface-type interface-number*  [ **agent** { **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } ]  **verbose**  ] \| **list**  **system-name** *system-name*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示指定接口收到的由邻居设备发来的LLDP信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定该参数，将显示所有接口收到的由邻居设备发来的LLDP信息。

**[agent**]：显示指定类型LLDP代理收到的由邻居设备发来的LLDP信息。如果未指定该参数，将显示所有类型LLDP代理收到的由邻居设备发来的LLDP信息。

**[nearest-bridge**]：表示最近桥代理。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

**[verbose**]：显示由邻居设备发来的LLDP详细信息。如果未指定该参数，将显示由邻居设备发来的LLDP概要信息。

**[list**]：按列表显示由邻居设备发来的LLDP信息。

**[system-name** *system-name*]：按列表显示由指定邻居设备发来的LLDP信息。*system-name*表示邻居设备的系统名称，为1～255个字符的字符串。如果未指定该参数，将按列表显示由所有邻居设备发来的LLDP信息。

【举例】

\# 显示所有接口最近桥代理收到的由邻居设备发来的LLDP详细信息（假设DCBX的版本为标准版）。

\<Sysname\> display lldp neighbor-information agent nearest-bridge verbose

LLDP neighbor-information of port 1[GigabitEthernet1/0/1:]

LLDP agent nearest-bridge:

 LLDP Neighbor index : 1

 Update time         : 0 days, 0 hours, 1 minutes, 1 seconds

 LLDP mac type       : Nearest Bridge

 Chassis type        : MAC address

 Chassis ID          : 000f-0055-0002

 Port ID type        : Interface name

 Port ID             : GigabitEthernet1/0/1

 Time to live        : 121

 Port description    : GigabitEthernet1/0/1 Interface

 System name         : Sysname

 System description  : H3C Comware Platform Software

 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge

 System capabilities enabled   : Bridge, Router, Customer Bridge

 Management address type           : IPv4

 Management address                : 192.168.1.55

 Management address interface type : IfIndex

 Management address interface ID   : Unknown

 Management address OID            : 0

 DCBX Control info:

 Oper version       : Standard

 DCBX ETS configuration info:

  CBS                : False

  Max TCs            : 8

  CoS     Local priority      Percentage        TSA

   0            0                 15            ETS

   1            1                 0             SP

   2            2                 15            ETS

   3            3                 14            ETS

   4            4                 14            ETS

   5            5                 14            ETS

   6            6                 14            ETS

   7            7                 14            ETS

 DCBX ETS recommendation info:

  CoS     Local priority      Percentage        TSA

   0            0                 15            ETS

   1            1                 0             SP

   2            2                 15            ETS

   3            3                 14            ETS

   4            4                 14            ETS

   5            5                 14            ETS

   6            6                 14            ETS

   7            7                 14            ETS

 DCBX PFC info:

  P0-0     P1-1     P2-1     P3-1     P4-0     P5-0     P6-0     P7-0

  Number of traffic classes supported: 8

  Value of MBC: 0

 DCBX APP info:

  Selected Field              Protocol ID Priority

  UDP/ DCCP                   100         0x3

  TCP/SCTP                    200         0x3

  Ethertype                   0x1234      0x3

  Ethertype                   0x8906      0x3

 Port VLAN ID(PVID): 1

 Port and protocol VLAN ID(PPVID) : 12

 Port and protocol VLAN supported : Yes

 Port and protocol VLAN enabled   : Yes

 VLAN name of VLAN 12: VLAN 0012

 Management VLAN ID  : 5

 Auto-negotiation supported : Yes

 Auto-negotiation enabled   : Yes

 OperMau                    : Speed(1000)/Duplex(Full)

 Power port class           : PD

 PSE power supported        : Yes

 PSE power enabled          : Yes

 PSE pairs control ability  : Yes

 Power pairs                : Signal

 Port power classification  : Class 0

 Power type                 : Type 2 PD

 Power source               : PSE and local

 Power priority             : High

 PD requested power value   : 21.1 w

 PSE allocated power value  : 15.3 w

 Link aggregation supported : Yes

 Link aggregation enabled   : Yes

 Aggregation port ID        : 52

 Congestion notification TLV info:

  Dot1p          CNPV         Ready

  0              Yes          Yes

  1              No           No

  2              No           No

  3              No           No

  4              Yes          No

  5              Yes          Yes

  6              No           No

  7              No           No

 Maximum frame size         : 1500

 Transmit Tw                : 100 us

 Receive Tw                 : 90 us

 Fallback Tw                : 90 us

 Echo Transmit Tw           : 0 us

 Echo Receive Tw            : 0 us

 MED information：

 Device class               : Connectivity device

 Media policy type          : Unknown

 Unknown policy             : No

 VLAN tagged                : No

 Media policy VLAN ID       : 1000

 Media policy L2 priority   : 6

 Media policy DSCP          : 10

 Location format       : Civic Address LCI

 Location information  :

  What(1)  Country(CN)

  CA type  CA value

  0        Chinese

  1        Zhejiang

  2        Hangzhou

 MED port information:

  Media policy type          : Unknown

  Unknown policy             : No

  VLAN tagged                : No

  Media policy VLANID        : 1000

  Media policy L2 priority   : 6

  Media policy DSCP          : 10

 PoE PSE power source       : Primary

 Port PSE priority          : Low

 Port available power value : 2.2 w

 Unknown basic TLV:

  TLV type           : 23

  TLV information    : 0x00140014

 Unknown organizationally-defined TLV:

  TLV OUI            : 00-12-bb

  TLV subtype        : 21

  Index              : 1

  TLV information    : 0x556e6b6e 6f776e

CDP neighbor-information of port 1[GigabitEthernet1/0/1:]

LLDP agent nearest-bridge:

 CDP neighbor index  : 4

 Chassis ID          : SEP00260B5C0548

 Port ID             : Port 1

 Software version    : SCCP41.8-4-1S

 Platform version    : Cisco IP Phone 7941

 Duplex              : Full

 Time to live        : 180

\# 显示所有接口所有类型LLDP代理收到的由邻居设备发来的LLDP详细信息（假设DCBX的版本为标准版）。

\<Sysname\> display lldp neighbor-information verbose

LLDP neighbor-information of port 1[GigabitEthernet1/0/1:]

LLDP agent nearest-bridge:

 LLDP Neighbor index : 1

 Update time         : 0 days, 0 hours, 1 minutes, 1 seconds

 LLDP mac type       : Nearest Bridge

 Chassis type        : MAC address

 Chassis ID          : 000f-0055-0002

 Port ID type        : Interface name

 Port ID             : GigabitEthernet1/0/1

 Time to live        : 121

 Port description    : GigabitEthernet1/0/1 Interface

 System name         : Sysname

 System description  : H3C Comware Platform Software

 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge

 System capabilities enabled   : Bridge, Router, Customer Bridge

 Management address type           : IPv4

 Management address                : 192.168.1.55

 Management address interface type : IfIndex

 Management address interface ID   : Unknown

 Management address OID            : 0

 DCBX control info:

  Oper version       : Standard

 DCBX ETS configuration info:

  CBS                : False

  Max TCs            : 8

  CoS     Local Priority      Percentage        TSA

   0            0                 15            ETS

   1            1                 0             SP

   2            2                 15            ETS

   3            3                 14            ETS

   4            4                 14            ETS

   5            5                 14            ETS

   6            6                 14            ETS

   7            7                 14            ETS

 DCBX ETS recommendation info:

  CoS     Local Priority      Percentage        TSA

   0            0                 15            ETS

   1            1                 0             SP

   2            2                 15            ETS

   3            3                 14            ETS

   4            4                 14            ETS

   5            5                 14            ETS

   6            6                 14            ETS

   7            7                 14            ETS

 DCBX PFC info:

  P0-0     P1-1     P2-1     P3-1     P4-0     P5-0     P6-0     P7-0

  Number of traffic classes supported: 8

  Value of MBC: 0

 DCBX APP info:

  Selected Field  Protocol ID  Priority

  UDP/DCCP        100          0x3

  TCP/SCTP        200          0x3

  Ethertype       0x1234       0x3

  Ethertype       0x8906       0x3

 Port VLAN ID(PVID): 1

 Port and protocol VLAN ID(PPVID) : 12

 Port and protocol VLAN supported : Yes

 Port and protocol VLAN enabled   : Yes

 VLAN name of VLAN 12: VLAN 0012

 Management VLAN ID  : 5

 Auto-negotiation supported : Yes

 Auto-negotiation enabled   : Yes

 OperMau                    : Speed(1000)/Duplex(Full)

 Power port class           : PD

 PSE power supported        : Yes

 PSE power enabled          : Yes

 PSE pairs control ability  : Yes

 Power pairs                : Signal

 Port power classification  : Class 0

 Power type                 : Type 2 PD

 Power source               : PSE and local

 Power priority             : High

 PD requested power value   : 21.1 w

 PSE allocated power value  : 15.3 w

 Link aggregation supported : Yes

 Link aggregation enabled   : Yes

 Aggregation port ID        : 52

 Maximum frame size         : 1500

 Transmit Tw                : 100 us

 Receive Tw                 : 90 us

 Fallback Tw                : 90 us

 Echo Transmit Tw           : 0 us

 Echo Receive Tw            : 0 us

 Device class               : Connectivity device

 HardwareRev               : Unknown

 FirmwareRev               : Unknown

 SoftwareRev               : Unknown

 SerialNum                 : Unknown

 Manufacturer name         : Unknown

 Model name                : Unknown

 Asset tracking identifier : Unknown

 Location format       : Civic Address LCI

 Location information  :

  What(1)  Country(CN)

  CA type  CA value

  0        Chinese

  1        Zhejiang

  2        Hangzhou

 MED port information:

  Media policy type          : Unknown

  Unknown policy             : No

  VLAN tagged                : No

  Media policy VLANID        : 1000

  Media policy L2 priority   : 6

  Media policy DSCP          : 10

 PoE PSE power source       : Primary

 Port PSE priority          : Low

 Port available power value : 2.2 w

 Unknown basic TLV:

  TLV type           : 23

  TLV information    : 0x00140014

 Unknown organizationally-defined TLV:

  TLV OUI            : 00-12-bb

  TLV subtype        : 21

  Index              : 1

  TLV information    : 0x556e6b6e 6f776e

CDP neighbor-information of port 1[GigabitEthernet1/0/1:]

 LLDP agent nearest-bridge:

 CDP neighbor index  : 4

 Chassis ID          : SEP00260B5C0548

 Port ID             : Port 1

 Software version    : SCCP41.8-4-1S

 Platform version    : Cisco IP Phone 7941

 Duplex              : Full

 Time to live        : 180

LLDP neighbor-information of port 1[GigabitEthernet1/0/1:]

LLDP agent nearest-nontpmr:

 LLDP Neighbor index : 1

 Update time         : 0 days, 0 hours, 1 minutes, 1 seconds

 Chassis type        : MAC address

 Chassis ID          : 000f-0055-0002

 Port ID type        : Interface name

 Port ID             : GigabitEthernet1/0/1

 Time to live        : 121

 Port description    : GigabitEthernet1/0/1 Interface

 System name         : Sysname

 System description  : H3C Comware Platform Software

 System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge

 System capabilities enabled   : Bridge, Router, Customer Bridge

 Management address type           : IPv4

 Management address                : 192.168.1.55

 Management address interface type : IfIndex

 Management address interface ID   : Unknown

 Management address OID            : 0

 Port VLAN ID(PVID): 1

 Port and protocol VLAN ID(PPVID) : 12

 Port and protocol VLAN supported : Yes

 Port and protocol VLAN enabled   : Yes

 VLAN name of VLAN 12: VLAN 0012

 Auto-negotiation supported : Yes

 Auto-negotiation enabled   : Yes

 OperMau                    : Speed(1000)/Duplex(Full)

 Power port class           : PD

 PSE power supported        : Yes

 PSE power enabled          : Yes

 PSE pairs control ability  : Yes

 Power pairs                : Signal

 Port power classification  : Class 0

 Power type                 : Type 2 PD

 Power source               : PSE and local

 Power priority             : High

 PD requested power value   : 21.1 w

 PSE allocated power value  : 15.3 w

 Link aggregation supported : Yes

 Link aggregation enabled   : Yes

 Aggregation port ID        : 52

 Congestion notification TLV info:

  Dot1p          CNPV         Ready

  0              Yes          Yes

  1              No           No

  2              No           No

  3              No           No

  4              Yes          No

  5              Yes          Yes

  6              No           No

  7              No           No

 Maximum frame size         : 1500

 Transmit Tw                : 100 us

 Receive Tw                 : 90 us

 Fallback Tw                : 90 us

 Echo Transmit Tw           : 0 us

 Echo Receive Tw            : 0 us

 Device class              : Connectivity device

 HardwareRev               : Unknown

 FirmwareRev               : Unknown

 SoftwareRev               : Unknown

 SerialNum                 : Unknown

 Manufacturer name         : Unknown

 Model name                : Unknown

 Asset tracking identifier : Unknown

 Location format       : Civic Address LCI

 Location information  :

  What(1)  Country(CN)

  CA type  CA value

  0        Chinese

  1        Zhejiang

  2        Hangzhou

 MED port information:

  Media policy type          : Unknown

  Unknown policy             : No

  VLAN tagged                : No

  Media policy VLANID        : 1000

  Media policy L2 priority   : 6

  Media policy DSCP          : 10

PoE PSE power source      : Primary

Port PSE priority         : Low

Port available power value: 2.2 w

Unknown basic TLV:

  TLV type           : 23

  TLV information    : 0x00140014

 Unknown organizationally-defined TLV:

  TLV OUI            : 00-12-bb

  TLV subtype        : 21

  Index              : 1

  TLV information    : 0x556e6b6e 6f776e

\# 显示所有接口所有类型LLDP代理收到的由邻居设备发来的LLDP概要信息。

\<Sysname\> display lldp neighbor-information

LLDP neighbor-information of port 52[GigabitEthernet1/0/3:]

LLDP agent nearest-bridge:

 LLDP neighbor index : 3

 LLDP mac type       : Nearest Bridge

 ChassisID/subtype   : 0011-2233-4400/MAC address

 PortID/subtype      : 000c-29f5-c71f/MAC address

 Capabilities        : Bridge, Router, Customer Bridge

 LLDP neighbor index : 6

 LLDP mac type       : Nearest Bridge

 ChassisID/subtype   : 0011-2233-4400/MAC address

 PortID/subtype      : 000c-29f5-c715/MAC address

 Capabilities        : None

CDP neighbor-information of port 52[GigabitEthernet1/0/3:]

LLDP agent nearest-bridge：

 CDP neighbor index  : 4

 Chassis ID          : SEP00260B5C0548

 Port ID             : Port 1

 CDP neighbor index  : 5

 Chassis ID          : 0011-2233-4400

 Port ID             : GigabitEthernet1/0/4

LLDP neighbor-information of port 52[GigabitEthernet1/0/3:]

LLDP agent nearest-nontpmr:

 LLDP neighbor index : 6

 ChassisID/subtype   : 0011-2233-4400/MAC address

 PortID/subtype      : 000c-29f5-c715/MAC address

 Capabilities        : None

\# 按列表显示类型LLDP代理所有邻居设备发来的LLDP信息。

\<Sysname\> display lldp neighbor-information list

Chassis ID : \* \-- \--Nearest nontpmr bridge neighbor

             \# \-- \--Nearest customer bridge neighbor

             Default \-- \-- Nearest bridge neighbor

System Name          Local Interface   Chassis ID       Port ID

System1              GE1/0/1           000f-e25d-ee91   GigabitEthernet1/0/5

System2              GE1/0/2           000f-e25d-ee92\*  GigabitEthernet1/0/6

System3              GE1/0/3           000f-e25d-ee93#  GigabitEthernet1/0/7

表1-2 display lldp neighbor-information命令显示信息描述表

字段

描述

LLDP agent nearest-bridge

LLDP缺省代理，即最近桥代理

LLDP agent nearest-customer

LLDP最近客户桥代理

LLDP agent nearest-nontpmr

LLDP最近非TPMR桥代理

LLDP neighbor-information of port 1

端口1上收到的LLDP邻居信息

LLDP Neighbor index

邻居索引

Update time

邻居信息最新更新时间

LLDP mac type

邻居MAC地址类型：

·Nearest brige：最近桥代理

·Nearest customer bridge：最近客户桥代理

·Nearest non-tpmr bridge：最近非TPMR桥代理

Chassis type

Chassis ID类型：

·Chassis component：表示底架组件

·Interface alias：表示接口化名

·Port component：表示端口组件

·MAC address：表示MAC地址

·Network address(ipv4)：表示网络地址（括号里表示地址类型）

·Interface name：表示接口名称

·Locally assigned：表示邻居自定义

Chassis ID

Chassis ID值，根据邻居设备的Chassis type取相应类型的值

Port ID type

端口ID类型：

·Interface alias：表示接口化名

·Port component：表示端口组件

·MAC address：表示MAC地址

·Network Address(ipv4)：表示网络地址（括号里表示地址类型）

·Interface name：表示接口名称

·Agent circuit ID：表示代理巡回标识

·Locally assigned：表示邻居自定义

Port ID

端口ID值，根据邻居设备的Port ID type取相应类型的值

Time to live

邻居信息在本地的存活时间

Port description

端口描述

System name

系统名称

System description

系统描述

System capabilities supported

系统所支持的功能：

·Repeater：表示支持信号中继功能

·Bridge：表示支持交换功能

·WlanAccessPoint：表示支持无线接入点功能

·Router：表示支持路由功能

·Telephone：表示支持电话功能

·DocsisCableDevice：表示支持电缆设备功能

·StationOnly：表示支持只作站点功能

·Customer Bridge：表示支持客户桥功能

·Service Bridge：表示支持服务桥功能

·TPMR：表示支持双端口MAC中继功能

·Other：表示支持不在上述列表的其它功能

System capabilities enabled

系统已开启的功能：

·Repeater：表示信号中继功能已开启

·Bridge：表示交换功能已开启

·WlanAccessPoint：表示无线接入点功能已开启

·Router：表示路由功能已开启

·Telephone：表示电话功能已开启

·DocsisCableDevice：表示电缆设备功能已开启

·StationOnly：表示只作站点功能已开启

·Customer Bridge：表示支持客户桥功能

·Service Bridge：表示支持服务桥功能

·TPMR：表示支持双端口MAC中继功能

·Other：表示不在上述列表的其它功能已开启

Management address type

管理地址类型

Management address

管理地址

Management address interface type

管理地址接口类型

Management address interface ID

管理地址接口索引

Management address OID

管理地址对象标识符

DCBX control info:

显示DCBX控制TLV的信息，在标准DCBX中显示版本信息

Oper version

DCBX版本号

Sequence number

DCBX TLV内容改变的次数

Acknowledge number

对端设备同步配置的次数

DCBX ETS info

CoS与本地优先级的映射关系及对应的带宽分配情况

CoS

CoS值

Local Priority

本地优先级

Percentage

对应的带宽分配

P0-   P1-   P2-   P3-   P4-   P5-   P6-   P7-

本端的no-drop标记值对应的支持的优先级数

Number of traffic classes supported

PFC支持的能力集，在1.01版本和标准版本中显示该项

DCBX APP info

显示APP TLV信息

Protocol ID

应用协议号

CoS map

应用协议与CoS的映射关系

DCBX ETS configuration info

显示ETS配置TLV信息

CBS

是否支持CBS，表示本端是否支持令牌桶限速算法：

·False：表示不支持令牌桶限速算法

·True：表示支持令牌桶限速算法

Max TCs

显示支持的最大优先级数目

TSA

显示传输选择算法

DCBX ETS recommendation info

显示ETS推荐TLV信息

DCBX PFC info

显示PFC TLV信息

Value of MBC

支持的MBC状态

Selected Field

选择域

Port VLAN ID

端口VLAN ID

Port and protocol VLAN ID(PPVID)

端口协议VLAN ID

Port and protocol VLAN supported

是否支持端口协议VLAN

Port and protocol VLAN enabled

是否开启端口协议VLAN

VLAN name of VLAN 12

VLAN 12的名称

Management VLAN ID

管理VLAN ID

Auto-negotiation supported

端口是否支持自协商

Auto-negotiation enabled

端口是否已开启自协商

OperMau

端口自适应的速率和双工状态

Power port class

PoE类型：

·PSE：表示供电设备

·PD：表示受电设备

PSE power supported

是否支持PSE供电

PSE power enabled

是否已开启PSE供电

PSE pairs control ability

供电方式是否可控

Power pairs

PoE端口的远程供电模式：

·Signal：表示信号线供电模式

·Spare：表示空闲线供电模式

Port power classification

PD的端口控制级别：

·Class 0：表示级别0

·Class 1：表示级别1

·Class 2：表示级别2

·Class 3：表示级别3

·Class 4：表示级别4

Power type

供电类型：

·Type 1 PD：表示类型1 PD

·Type 2 PD：表示类型2 PD

·Type 1 PSE：表示类型1 PSE

·Type 2 PSE：表示类型2 PSE

Power source

功率来源（功率来源根据供电类型为PD类型或PSE类型，取值不同）：

PSE

·Unknown：表示采用的电源类型未知

·Primary：表示采用主用电源作为电源

·Backup：表示采用备用电源作为电源

·Reserved：保留

PD

·Unknown：表示采用的电源类型未知

·PSE：表示采用PSE作为电源

·Local：表示采用本地电源作为电源

·PSE and local：表示采用PSE和本地电源作为电源

Power priority

功率优先级：

·Unknown：表示优先级未知

·Critical：表示优先级为1级

·High：表示优先级为2级

·Low：表示优先级为3级

PD requested power value

PD请求功率值，单位为瓦特

PSE allocated power value

PSE分配功率值，单位为瓦特

Link aggregation supported

端口是否支持链路聚合

Link aggregation enabled

端口是否已开启链路聚合

Congestion notification TLV info

拥塞通知TLV信息。本字段的支持情况与设备型号有关，请以设备的实际情况为准

Dot1p

802.1p优先级

CNPV

802.1p优先级是否被配置为CNPV，即是否匹配该优先级的报文具有QCN功能：

·Yes：表示802.1p优先级被配置为CNPV

·No：表示802.1p优先级未被配置为CNPV

Ready

表明设备接口是否已经关闭了802.1p优先级与隔离优先级的映射：

·Yes：表示关闭优先级映射

·No：表示未关闭优先级映射

Maximum frame size

端口支持的最大帧长度

MED information

MED设备相关信息

Device class

MED设备类型：

·Connectivity device：表示网络设备

·Class I：表示一般终端设备，即所有需要LLDP发现服务的终端设备

·Class II：表示媒体终端设备，即具备媒体能力的终端设备，其能力包含了一般终端设备的能力。该类设备支持媒体流

·Class III：表示通讯终端设备，即直接支持目标用户IP通讯系统的终端设备，其能力包含了一般终端设备和媒体终端设备的所有能力。该类设备直接被目标用户所使用

Media policy type

媒体策略类型：

·Unknown：表示类型未知

·Voice：表示语音

·VoiceSignaling：表示语音信号

·GuestVoice：表示访客语音

·GuestVoiceSignaling：表示访客语音信号

·SoftPhoneVoice：表示软体电话语音

·Videoconferencing：表示视频会议

·StreamingVideo：表示流视频

·VideoSignaling：表示视频信号

Unknown policy

媒体策略类型是否未知：

·Yes：表示策略类型未知

·No：表示策略类型已知

VLAN tagged

媒体VLAN是否带Tag

Media policy VLAN ID

媒体VLAN的VLAN ID

Media policy L2 priority

二层优先级

Media policy DSCP

DSCP的值

Location format

位置信息格式：

·Invalid：表示无效位置数据类型

·Coordinate-based LCI：表示基于坐标的位置信息

·Civic Address LCI：表示普通地址信息

·ECS ELIN：表示紧急电话号码

Location information

位置信息

PoE PSE power source

PSE所采用的电源类型：

·Unknown：表示采用的电源类型未知

·Primary：表示采用主用电源作为电源

·Backup：表示采用备用电源作为电源

PoE PD power source

PD所采用的电源类型：

·Unknown：表示采用的电源类型未知

·PSE：表示采用PSE作为电源

·Local：表示采用本地电源作为电源

·PSE and local：表示采用PSE和本地电源作为电源

PoE service type

PoE服务类型

Port PSE priority

PSE上端口的供电优先级：

·Unknown：表示优先级未知

·Critical：表示优先级为1级

·High：表示优先级为2级

·Low：表示优先级为3级

Port PD priority

PD上端口的受电优先级：

·Unknown：表示优先级未知

·Critical：表示优先级为1级

·High：表示优先级为2级

·Low：表示优先级为3级

Port available power value

PSE上端口可提供的功率，或PD上端口所需的功率，单位为瓦特

HardwareRev

产品的硬件版本

FirmwareRev

产品的固件版本

SoftwareRev

产品的软件版本

SerialNum

序列号

Manufacturer name

制造厂商

Model name

模块名称

Asset tracking identifier

资产跟踪ID

Unknown basic TLV

未知的基本TLV

TLV type

未知的基本TLV类型

TLV information

未知的基本TLV的具体信息

Unknown organizationally-defined TLV

未知组织定义TLV

TLV OUI

未知组织定义TLV的对象唯一标识

TLV subtype

未知的组织定义TLV类型

Index

未知组织的索引

CDP neighbor-information of port 1

端口1的CDP邻居信息

CDP neighbor index

CDP邻居索引

Chassis ID/subtype

Chassis ID值及Chassis ID类型

Port ID/subtype

Port ID值及PortID类型

Software version

邻居软件版本

Platform version

邻居平台版本

Duplex

双工状态

Capabilities

系统已开启的功能：

·Repeater：表示开启信号中继功能

·Bridge：表示开启交换功能

·WlanAccessPoint：表示开启无线接入点功能

·Router：表示开启路由功能

·Telephone：表示开启电话功能

·DocsisCableDevice：表示开启电缆设备功能

·StationOnly：表示开启只作站点功能，与其他功能不能同时出现

·Other：表示开启不在上述列表的其他功能

·None：表示该邻居未发布该TLV

Local Interface

接收LLDP信息的本端端口

Chassis ID : \* \-- \-- Nearest nontpmr bridge neighbor                              

                    #\-- \-- Nearest customer bridge neighbor

·\*符号：表示该邻居是最近非TPMR桥代理类型邻居

·\#符号：表示该邻居是最近客户桥代理类型邻居

Transmit Tw

本端发送的等待时间，单位为微秒

Receive Tw

本端向对端请求的等待时间，单位为微秒

Fallback Tw

本端向对端请求的候选等待时间，单位为微秒

Echo Transmit Tw

收到的对端发送的等待时间，单位为微秒

Echo Receive Tw

收到的对端请求的等待时间，单位为微秒

**LLDP \-- LLDP配置命令 \-- display lldp statistics**

------------------------------------------------------------------------

**[display lldp statistics**]命令用来显示LLDP的统计信息。

【命令】

**[display lldp statistics**[ [ **global** \| [ **interface** *interface-type interface-number* ]  **agent**  [ **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } ] ]]

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[global**]：显示全局LLDP统计信息。

**[interface** *interface-type interface-number*]：显示指定接口上的LLDP统计信息，*interface-type interface-number*表示接口类型和接口编号。

**[agent**]：显示指定类型LLDP代理的统计信息。如果未指定该参数，将显示所有类型LLDP代理的统计信息。

**[nearest-bridge**]：表示最近桥代理。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

【使用指导】

如果未指定任何参数，将同时显示全局和接口上的LLDP统计信息。

【举例】

\# 显示全局和接口上的LLDP统计信息。

\<Sysname\> display lldp statistics

LLDP statistics global information:

LLDP neighbor information last change time:0 days, 0 hours, 4 minutes, 40 seconds

The number of LLDP neighbor information inserted : 1

The number of LLDP neighbor information deleted  : 1

The number of LLDP neighbor information dropped  : 0

The number of LLDP neighbor information aged out : 1

LLDP statistics information of port 1 [GigabitEthernet1/0/1:]

LLDP agent nearest-bridge:

The number of LLDP frames transmitted            : 0

The number of LLDP frames received               : 0

The number of LLDP frames discarded              : 0

The number of LLDP error frames                  : 0

The number of LLDP TLVs discarded                : 0

The number of LLDP TLVs unrecognized             : 0

The number of LLDP neighbor information aged out : 0

The number of CDP frames transmitted             : 0

The number of CDP frames received                : 0

The number of CDP frames discarded               : 0

The number of CDP error frames                   : 0

LLDP agent nearest-nontpmr:

The number of LLDP frames transmitted            : 0

The number of LLDP frames received               : 0

The number of LLDP frames discarded              : 0

The number of LLDP error frames                  : 0

The number of LLDP TLVs discarded                : 0

The number of LLDP TLVs unrecognized             : 0

The number of LLDP neighbor information aged out : 0

The number of CDP frames transmitted             : 0

The number of CDP frames received                : 0

The number of CDP frames discarded               : 0

The number of CDP error frames                   : 0

LLDP agent nearest-customer:

The number of LLDP frames transmitted            : 0

The number of LLDP frames received               : 0

The number of LLDP frames discarded              : 0

The number of LLDP error frames                  : 0

The number of LLDP TLVs discarded                : 0

The number of LLDP TLVs unrecognized             : 0

The number of LLDP neighbor information aged out : 0

The number of CDP frames transmitted             : 0

The number of CDP frames received                : 0

The number of CDP frames discarded               : 0

The number of CDP error frames                   : 0

\# 显示接口GigabitEthernet1/0/1的最近客户桥代理上的LLDP统计信息。

\<Sysname\> display lldp statistics interface gigabitethernet 1/0/1 agent nearest-customer

LLDP statistics information of port 1 [GigabitEthernet1/0/1:]

LLDP agent nearest-customer:

The number of LLDP frames transmitted            : 0

The number of LLDP frames received               : 0

The number of LLDP frames discarded              : 0

The number of LLDP error frames                  : 0

The number of LLDP TLVs discarded                : 0

The number of LLDP TLVs unrecognized             : 0

The number of LLDP neighbor information aged out : 0

The number of CDP frames transmitted             : 0

The number of CDP frames received                : 0

The number of CDP frames discarded               : 0

The number of CDP error frames                   : 0

表1-3 display lldp statistics命令显示信息描述表

字段

描述

LLDP agent nearest-bridge

LLDP缺省代理，即最近桥代理

LLDP agent nearest-customer

LLDP最近客户桥代理

LLDP agent nearest-nontpmr

LLDP最近非TPMR桥代理

LLDP statistics global information

全局LLDP统计信息

LLDP neighbor information last change time

邻居信息的最后更新时间

The number of LLDP neighbor information inserted

邻居信息的增加次数

The number of LLDP neighbor information deleted

邻居信息的删除次数

The number of LLDP neighbor information dropped

由于空间不足而导致丢弃邻居信息的次数

The number of LLDP neighbor information aged out

邻居信息的老化数量

LLDP statistics Information of port 1

端口1上的LLDP统计信息

The number of LLDP frames transmitted

发送的LLDP帧总数

The number of LLDP frames received

收到的LLDP帧总数

The number of LLDP frames discarded

丢弃的LLDP帧总数

The number of LLDP error frames

收到的错误LLDP帧总数

The number of LLDP TLVs discarded

丢弃的LLDP TLV总数

The number of LLDP TLVs unrecognized

不可识别的LLDP TLV总数

The number of LLDP neighbor information aged out

老化的LLDP邻居信息总数

The number of CDP frames transmitted

发送的CDP帧总数

The number of CDP frames received

收到的CDP帧总数

The number of CDP frames discarded

丢弃的CDP帧总数

The number of CDP error frames

收到的错误CDP帧总数

**LLDP \-- LLDP配置命令 \-- display lldp status**

------------------------------------------------------------------------

**[display lldp status**]命令用来显示LLDP的状态信息。

【命令】

**[display lldp status ** **interface** *interface-type interface-number* ]  **agent** [[ **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示指定接口上的LLDP状态信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定该参数，将显示所有开启了LLDP功能的接口上的LLDP状态信息。

**[agent**]：显示指定类型LLDP代理的状态信息。如果未指定该参数，将显示所有类型LLDP代理的状态信息。

**[nearest-bridge**]：表示最近桥代理。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

【举例】

\# 显示全局和所有接口上的LLDP状态信息。

\<Sysname\> display lldp status

Global status of LLDP: Enable

Bridge mode of LLDP: customer-bridge

The current number of LLDP neighbors: 0

The current number of CDP neighbors: 0

LLDP neighbor information last changed time: 0 days, 0 hours, 4 minutes, 40 seconds

Transmit interval              : 30s

Fast transmit interval         : 1s

Transmit max credit            : 5

Hold multiplier                : 4

Reinit delay                   : 2s

Trap interval                  : 5s

Fast start times               : 3

LLDP status information of port 1 [GigabitEthernet1/0/1:]

LLDP agent  nearest-bridge:

Port status of LLDP            : Enable

Admin status                   : Tx_Rx

Trap flag                      : No

MED trap flag                  : No

Polling interval               : 0s

Number of LLDP neighbors       : 5

Number of MED neighbors        : 2

Number of CDP neighbors        : 0

Number of sent optional TLV    : 12

Number of received unknown TLV : 5

LLDP agent nearest-nontpmr:

Port status of LLDP            : Enable

Admin status                   : Tx_Rx

Trap flag                      : No

Polling interval               : 0s

Number of LLDP neighbors       : 5

Number of MED neighbors        : 2

Number of CDP neighbors        : 0

Number of sent optional TLV    : 12

Number of received unknown TLV : 5

LLDP agent nearest-customer:

Port status of LLDP            : Enable

Admin status                   : Tx_Rx

Trap flag                      : No

Polling interval               : 0s

Number of LLDP neighbors       : 5

Number of MED neighbors        : 2

Number of CDP neighbors        : 0

Number of sent optional TLV    : 12

Number of received unknown TLV : 5

表1-4 display lldp status命令显示信息描述表

字段

描述

Bridge mode of LLDP

LLDP桥模式：

·service-bridge：表示服务桥模式

·customer-bridge：表示客户桥模式

LLDP agent nearest-bridge

LLDP缺省代理，即最近桥代理

LLDP agent nearest-customer

LLDP最近客户桥代理

LLDP agent nearest-nontpmr

LLDP最近非TPMR桥代理

Global status of LLDP

LLDP功能是否已全局开启

The current number of LLDP neighbors

当前设备的LLDP邻居总数

The current number of CDP neighbors

当前设备的CDP邻居总数

LLDP neighbor information last changed time

邻居信息的最后更新时间

Transmit interval

LLDP报文的发送间隔

Hold multiplier

TTL乘数

Reinit delay

端口初始化延迟时间

Transmit max credit

LLDP报文发包限速令牌桶的最大值

Trap interval

Trap信息的发送间隔

Fast start times

快速发送LLDP报文的个数

LLDP status infomation of port 1

端口1上的LLDP状态信息

Port status of LLDP

LLDP功能是否已在端口上开启

Admin status

端口LLDP工作模式：

·Tx_Rx：表示既发送也接收LLDP报文

·Rx_Only：表示只接收不发送LLDP报文

·Tx_Only：表示只发送不接收LLDP报文

·Disable：表示既不发送也不接收LLDP报文

Trap Flag

LLDP Trap功能是否已开启

MED trap flag

LLDP-MED Trap功能是否已开启

Polling interval

轮询间隔，0表示轮询功能处于关闭状态

Number of neighbors

端口LLDP邻居数量

Number of MED neighbors

端口MED邻居设备的数量

Number of CDP neighbors

端口CDP邻居设备的数量

Number of sent optional TLV

端口在一个LLDP报文中发送的可选TLV总数

Number of received unknown TLV

端口在所有LLDP报文中收到的不能识别的TLV总数

**LLDP \-- LLDP配置命令 \-- display lldp tlv-config**

------------------------------------------------------------------------

**[display lldp tlv-config**]命令用来显示接口上可发送的可选TLV信息。

【命令】

**[display lldp tlv-config **[ **interface** *interface-type interface-number*  [ **agent** { **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示指定接口上可发送的可选TLV信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定该参数，将显示所有接口上可发送的可选TLV信息。

**[agent**]：显示指定类型LLDP代理的可选TLV信息。如果未指定该参数，将显示所有类型LLDP代理的可选TLV信息。

**[nearest-bridge**]：表示最近桥代理。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

【举例】

\# 显示接口GigabitEthernet1/0/1上可发送的可选TLV信息。

\<Sysname\> display lldp tlv-config interface gigabitethernet 1/0/1

LLDP tlv-config of port 1[GigabitEthernet1/0/1:]

LLDP agent nearest-bridge:

NAME                              STATUS    DEFAULT

Basic optional TLV:

 Port Description TLV             YES       YES

 System Name TLV                  YES       YES

 System Description TLV           YES       YES

 System Capabilities TLV          YES       YES

 Management Address TLV           YES       YES

IEEE 802.1 extend TLV:

 Port VLAN ID TLV                 YES       YES

 Port And Protocol VLAN ID TLV    YES       YES

 VLAN Name TLV                    YES       YES

 DCBX TLV                         NO        NO

 EVB TLV                          NO        NO

 Link Aggregation TLV             YES       YES

 Management VID TLV               YES       YES

 Congestion notification TLV      NO        NO

IEEE 802.3 extend TLV:

 MAC-Physic TLV                   YES       YES

 Power via MDI TLV                YES       YES

 Maximum Frame Size TLV           YES       YES

 Energy-Efficient Ethernet TLV    NO        NO

LLDP-MED extend TLV:

 Capabilities TLV                 YES        YES

 Network Policy TLV               YES        YES

 Location Identification TLV      NO         NO

 Extended Power via MDI TLV       YES        YES

 Inventory TLV                    YES        YES

LLDP agent nearest-nontpmr:

NAME                              STATUS    DEFAULT

Basic optional TLV:

 Port Description TLV             YES       NO

 System Name TLV                  YES       NO

 System Description TLV           YES       NO

 System Capabilities TLV          YES       NO

 Management Address TLV           YES       NO

IEEE 802.1 extend TLV:

 Port VLAN ID TLV                 YES       NO

 Port And Protocol VLAN ID TLV    YES       NO

 VLAN Name TLV                    YES       NO

 DCBX TLV                         NO        NO

 EVB TLV                          YES       YES

 Link Aggregation TLV             YES       NO

 Management VID TLV               NO        NO

IEEE 802.3 extend TLV:

 MAC-Physic TLV                   YES       NO

 Power via MDI TLV                YES       NO

 Maximum Frame Size TLV           YES       NO

 Energy-Efficient Ethernet TLV    NO        NO

LLDP-MED extend TLV:

 Capabilities TLV                 YES        NO

 Network Policy TLV               YES        NO

 Location Identification TLV      NO         NO

 Extended Power via MDI TLV       YES        NO

 Inventory TLV                    YES        NO

LLDP agent nearest-customer:

NAME                              STATUS    DEFAULT

Basic optional TLV:

 Port Description TLV             YES       YES

 System Name TLV                  YES       YES

 System Description TLV           YES       YES

 System Capabilities TLV          YES       YES

 Management Address TLV           YES       YES

IEEE 802.1 extend TLV:

 Port VLAN ID TLV                 YES       YES

 Port And Protocol VLAN ID TLV    YES       YES

 VLAN Name TLV                    YES       YES

 DCBX TLV                         NO        NO

 EVB TLV                          NO        NO

 Link Aggregation TLV             YES       NO

 Management VID TLV               YES       YES

IEEE 802.3 extend TLV:

 MAC-Physic TLV                   YES       NO

 Power via MDI TLV                YES       NO

 Maximum Frame Size TLV           YES       NO

 Energy-Efficient Ethernet TLV    NO        NO

LLDP-MED extend TLV:

 Capabilities TLV                 YES        YES

 Network Policy TLV               YES        YES

 Location Identification TLV      NO         NO

 Extended Power via MDI TLV       YES        NO

 Inventory TLV                    YES        YES

![说明](LLDP命令.files/image001.png)

本命令的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-5 display lldp tlv-config命令显示信息描述表

字段

描述

LLDP agent nearest-bridge

LLDP 缺省代理，即最近桥代理

LLDP agent nearest-customer

LLDP最近客户桥代理

LLDP agent nearest-nontpmr

LLDP最近非TPMR桥代理

LLDP tlv-config of port 1

端口1上可发送的可选TLV类型

NAME

TLV类型

STATUS

端口是否配置发布指定类型TLV

DEFAULT

端口发布指定类型TLV的缺省情况

Basic optional TLV

端口可以发送的基本TLV类型

Port Description TLV

端口描述TLV

System Name TLV

系统名称TLV

System Description TLV

系统描述TLV

System Capabilities TLV

系统能力集TLV

Management Address TLV

管理地址TLV

Congestion notification TLV

拥塞通知TLV。本字段的支持情况与设备型号有关，请以设备的实际情况为准

IEEE 802.1 extended TLV

端口可发送的IEEE 802.1组织定义的TLV类型

Port VLAN ID TLV

端口VLAN ID TLV

Port And Protocol VLAN ID TLV

协议VLAN ID TLV

VLAN Name TLV

VLAN名称TLV

DCBX TLV

DCBX（Data Center Bridging Exchange Protocol，数据中心桥能力交换协议） TLV。本字段的支持情况与设备型号有关，请以设备的实际情况为准

EVB TLV

EVB（Edge Virtual Bridging，边缘虚拟桥接）模块TLV。本字段的支持情况与设备型号有关，请以设备的实际情况为准

Management VID TLV

管理VLAN TLV

IEEE 802.3 extended TLV

端口可发送的IEEE 802.3组织定义的TLV类型

MAC-Physic TLV

端口物理属性TLV

Power via MDI TLV

供电能力TLV

Link Aggregation TLV

链路聚合TLV

Maximum Frame Size TLV

最大帧长度TLV

LLDP-MED extend TLV

LLDP-MED TLV

Capabilities TLV

MED能力集TLV

Network Policy TLV

网络策略TLV

Location Identification TLV

位置标识TLV

Extended Power via MDI TLV

扩展供电能力TLV

Inventory TLV

资产信息TLV，包括以下几种：

·Hardware Revision TLV：终端设备硬件版本

·Firmware Revision TLV：终端设备固件版本

·Software Revision TLV：终端设备软件版本

·Serial Number TLV：终端设备序列号

·Manufacturer Name TLV：终端设备的制造厂商名称

·Model name TLV：终端设备的模块名称

·Asset ID TLV：终端设备的资产标识符，以便目录管理和资产跟踪

Energy-Efficient Ethernet TLV

节能以太网TLV。本字段的支持情况与设备型号有关，请以设备的实际情况为准

**LLDP \-- LLDP配置命令 \-- lldp admin-status**

------------------------------------------------------------------------

**[lldp admin-status**]命令用来配置LLDP的工作模式。

**[undo lldp admin-status**]命令用来恢复缺省情况。

【命令】

在二层以太网接口视图/三层以太网接口视图/管理以太网接口视图下：

**[lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **admin-status** { **disable** \| **rx** \| **tx** \| **txrx** }]]

**[undo lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **admin-status**]]

在二层聚合接口视图/三层聚合接口视图下：

**[lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **admin-status** { **disable** \| **rx** \| **tx** \| **txrx** }]]

**[undo lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **admin-status**]]

【缺省情况】

LLDP最近桥代理的工作模式为TxRx，既发送也接收LLDP报文。其他类型的LLDP代理的工作模式为Disable，即不发送也不接收LLDP报文。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[agent**]：配置指定类型LLDP代理的工作模式。在以太网接口视图/管理以太网接口视图下，未指定时表示配置最近桥代理的工作模式。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

**[disable**]：表示工作模式为Disable，既不发送也不接收LLDP报文。

**[rx**]：表示工作模式为Rx，只接收不发送LLDP报文。

**[tx**]：表示工作模式为Tx，只发送不接收LLDP报文。

**[txrx**]：表示工作模式为TxRx，既发送也接收LLDP报文。

【举例】

\# 配置接口GigabitEthernet1/0/1上最近客户桥代理LLDP的工作模式为Rx。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp agent nearest-customer admin-status rx

**LLDP \-- LLDP配置命令 \-- lldp check-change-interval**

------------------------------------------------------------------------

**[lldp check-change-interval**]命令用来开启轮询功能并配置轮询间隔。

**[undo lldp check-change-interval**]命令用来关闭轮询功能。

【命令】

在二层以太网接口视图/三层以太网接口视图/管理以太网接口视图下：

**[lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **check-change-interval** *interval*]]

**[undo lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **check-change-interval**]]

在二层聚合接口视图/三层聚合接口视图下：

**[lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **check-change-interval** *interval*]]

**[undo lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **check-change-interval**]]

【缺省情况】

轮询功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[agent**]：配置指定类型LLDP代理的轮询功能。在以太网接口视图/管理以太网接口视图下，未指定时表示配置最近桥代理的轮询功能。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

*[interval*]：表示轮询间隔，取值范围为1～30，单位为秒。

【举例】

\# 在接口GigabitEthernet1/0/1的最近客户桥代理上开启轮询功能，并配置轮询间隔为30秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp agent nearest-customer check-change-interval 30

**LLDP \-- LLDP配置命令 \-- lldp compliance admin-status cdp**

------------------------------------------------------------------------

![说明](LLDP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[lldp compliance admin-status cdp**]命令用来配置LLDP兼容CDP功能的工作模式。

**[undo lldp compliance admin-status cdp**]命令用来恢复缺省情况。

【命令】

**[lldp compliance admin-status cdp**[ { **disable** \| **txrx** }]]

**[undo lldp compliance admin-status cdp**]

【缺省情况】

LLDP兼容CDP功能的工作模式为Disable，既不发送也不接收CDP报文。

【视图】

二层以太网接口视图/三层以太网接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disable**]：表示工作模式为Disable，既不发送也不接收CDP报文。

**[txrx**]：表示工作模式为TxRx，既发送也接收CDP报文。

【使用指导】

欲使LLDP兼容CDP的功能生效，必须先开启LLDP兼容CDP功能，同时将LLDP兼容CDP功能的工作模式配置为TxRx。

【举例】

\# 开启LLDP兼容CDP功能，并在接口GigabitEthernet1/0/1上配置LLDP兼容CDP功能的工作模式为TxRx。

\<Sysname\> system-view

Sysname lldp compliance cdp

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp compliance admin-status cdp txrx

【相关命令】

·**lldp compliance cdp**

**LLDP \-- LLDP配置命令 \-- lldp compliance cdp**

------------------------------------------------------------------------

![说明](LLDP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[lldp compliance cdp**]命令用来开启LLDP兼容CDP功能。

**[undo lldp compliance cdp**]命令用来恢复缺省情况。

【命令】

**[lldp compliance cdp**]

**[undo lldp compliance cdp**]

【缺省情况】

LLDP兼容CDP功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

由于CDP报文所携Time To Live TLV中TTL的最大值为255，而CDP报文的发送间隔由LLDP报文的发送间隔控制，因此为保证LLDP兼容CDP功能的正常运行，建议配置LLDP报文的发送间隔值不大于实际TTL的1/3。

【举例】

\# 开启LLDP兼容CDP功能。

\<Sysname\> system-view

Sysname lldp compliance cdp

【相关命令】

·**lldp hold-multiplier**

·**lldp timer tx-interval**

**LLDP \-- LLDP配置命令 \-- lldp enable**

------------------------------------------------------------------------

**[lldp enable**]命令用来在接口上开启LLDP功能。

**[undo lldp enable**]命令用来在接口上关闭LLDP功能。

【命令】

**[lldp enable**]

**[undo lldp enable**]

【缺省情况】

接口上的LLDP功能处于开启状态。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有当全局和接口上都开启了LLDP功能后，该功能才会生效。

【举例】

\# 在接口GigabitEthernet1/0/1上关闭LLDP功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo lldp enable

【相关命令】

·**lldp global enable**

**LLDP \-- LLDP配置命令 \-- lldp encapsulation snap**

------------------------------------------------------------------------

**[lldp encapsulation snap**]命令用来配置LLDP报文的封装格式为SNAP格式。

**[undo lldp encapsulation**]命令用来恢复缺省情况。

【命令】

在二层以太网接口视图/三层以太网接口视图/管理以太网接口视图下：

**[lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **encapsulation snap**]]

**[undo lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **encapsulation**]]

在二层聚合接口视图/三层聚合接口视图下：

**[lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **encapsulation snap**]]

**[undo lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **encapsulation**]]

【缺省情况】

LLDP报文的封装格式为Ethernet II格式。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[agent**]：配置指定类型LLDP代理的封装格式。在以太网接口视图/管理以太网接口视图下，未指定时表示配置最近桥代理的封装格式。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

【使用指导】

·LLDP CDP报文的封装格式只能为SNAP格式，不能为Ethernet II格式。

·携带EVB模块TLV的LLDP报文不能通过SNAP格式封装和发送。

【举例】

\# 配置接口GigabitEthernet1/0/1上发送的LLDP报文的封装格式为SNAP格式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp encapsulation snap

**LLDP \-- LLDP配置命令 \-- lldp fast-count**

------------------------------------------------------------------------

**[lldp fast-count**]命令用来配置快速发送LLDP报文的个数。

**[undo lldp fast-count**]命令用来恢复缺省情况。

【命令】

**[lldp fast-count ***count*]

**[undo lldp fast-count**]

【缺省情况】

快速发送LLDP报文的个数为4个。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：表示快速发送LLDP报文的个数，取值范围为1～8，单位为个。

【举例】

\# 配置快速发送LLDP报文的个数为5个。

\<Sysname\> system-view

Sysname lldp fast-count 5

**LLDP \-- LLDP配置命令 \-- lldp global enable**

------------------------------------------------------------------------

**[lldp global enable**]命令用来全局开启LLDP功能。

**[undo lldp global enable**]命令用来全局关闭LLDP功能。

【命令】

**[lldp global enable**]

**[undo lldp global enable**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有当全局和接口上都开启了LLDP功能后，该功能才会生效。

【举例】

\# 全局关闭LLDP功能。

\<Sysname\> system-view

Sysname undo lldp global enable

【相关命令】

·**lldp enable**

**LLDP \-- LLDP配置命令 \-- lldp hold-multiplier**

------------------------------------------------------------------------

**[lldp hold-multiplier**]命令用来配置TTL乘数。

**[undo lldp hold-multiplier**]命令用来恢复缺省情况。

【命令】

**[lldp hold-multiplier ***value*]

**[undo lldp hold-multiplier**]

【缺省情况】

TTL乘数为4。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：表示TTL乘数，取值范围为2～10。

【使用指导】

LLDP报文所携Time To Live TLV中TTL的值用来设置邻居信息在本地设备上的老化时间，由于TTL＝Min（65535，（TTL乘数×LLDP报文的发送间隔＋1）），即取65535与（TTL乘数×LLDP报文的发送间隔＋1）中的最小值，因此通过调整TTL乘数可以控制本设备信息在邻居设备上的老化时间。

【举例】

\# 配置TTL乘数为6。

\<Sysname\> system-view

Sysname lldp hold-multiplier 6

【相关命令】

·**lldp timer tx-interval**

**LLDP \-- LLDP配置命令 \-- lldp management-address**

------------------------------------------------------------------------

**[lldp management-address**]命令用来配置接口收到LLDP报文后下发ARP表项或ND表项。

**[undo lldp management-address**]命令用来恢复缺省情况。

【命令】

**[lldp management-address**[ { **arp-learning** \| **nd-learning** } [ **vlan** *vlan-id* ]]]

**[undo lldp management-address**[ { **arp-learning** \| **nd-learning** }]]

【缺省情况】

接口收到LLDP报文后不下发ARP表项和ND表项。

【视图】

三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[arp-learning**]：表示接口收到携带IPv4格式Management Address TLV的LLDP报文后，会下发该报文携带的管理地址与报文源MAC地址组成的ARP表项。

**[nd-learning**]：表示接口收到携带IPv6格式Management Address TLV的LLDP报文后，会下发该报文携带的管理地址与报文源MAC地址组成的ND表项。

**[vlan** *vlan-id*]：指定Dot1q终结中三层以太网子接口关联的VLAN ID，取值范围为1\~4094。指定该参数后，下发ARP表项或ND表项到该VLAN ID关联的三层以太网子接口；如果该VLAN ID没有关联的三层以太网子接口，则将对应表项下发到当前接口。不指定该参数时表示将对应表项下发到当前接口。

【使用指导】

ARP表项和ND表项下发互不影响，可同时配置。

【举例】

\# 配置接口GigabitEthernet1/0/1收到携带IPv4格式Management Address TLV的LLDP报文后，下发ARP表项到Dot1q终结中VLAN 4094关联的三层以太网子接口上。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp management-address arp-learning vlan 4094

【相关命令】

·**lldp source-mac vlan**

**LLDP \-- LLDP配置命令 \-- lldp management-address-format string**

------------------------------------------------------------------------

**[lldp management-address-format string**]命令用来配置管理地址在TLV中的封装格式为字符串格式。

**[undo lldp management-address-format**]命令用来恢复缺省情况。

【命令】

在二层以太网接口视图/三层以太网接口视图/管理以太网接口视图下：

**[lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **management-address-format string**]]

**[undo lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **management-address-format**]]

在二层聚合接口视图/三层聚合接口视图下：

**[lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **management-address-format string**]]

**[undo lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **management-address-format**]]

【缺省情况】

管理地址在TLV中的封装格式为数字格式。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[agent**]：配置指定LLDP代理类型管理地址在TLV中的封装格式。在以太网接口视图/管理以太网接口视图下，未指定时表示配置最近桥代理的管理地址在TLV中的封装格式。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

【使用指导】

如果邻居将管理地址以字符串格式封装在TLV中，用户可在本地设备上也将封装格式改为字符串，以保证与邻居设备的正常通信。

【举例】

\# 在接口GigabitEthernet1/0/1的最近客户桥代理上配置管理地址在TLV中的封装格式为字符串格式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp agent nearest-customer management-address-format string

**LLDP \-- LLDP配置命令 \-- lldp max-credit**

------------------------------------------------------------------------

**[lldp max-credit**]命令用来配置限制发送报文速率的令牌桶大小。

**[undo lldp max-credit**]命令用来恢复缺省情况。

【命令】

**[lldp max-credit ***credit-value*]

**[undo lldp max-credit**]

【缺省情况】

限制发送报文速率的令牌桶大小为5。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[credit-value*]：表示LLDP发包限速的令牌桶大小，取值范围1～100。

【举例】

\# 配置LLDP发包限速的令牌桶大小为10。

\<Sysname\> system-view

Sysname lldp max-credit 10

**LLDP \-- LLDP配置命令 \-- lldp mode**

------------------------------------------------------------------------

**[lldp mode**]命令用来配置LLDP桥模式。

**[undo lldp mode**]命令用来恢复缺省情况。

【命令】

**[lldp mode service-bridge**]

**[undo lldp mode**]

【缺省情况】

LLDP桥模式为客户桥模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-bridge**]：表示服务桥模式。

【使用指导】

LLDP桥模式命令用于控制设备支持不同的LLDP代理。

·工作于服务桥模式时，设备可支持最近桥代理和最近非TPMR桥代理，即对上述类型的代理MAC的LLDP报文进行处理，其他目的MAC的LLDP报文进行VLAN内透传。

·工作于客户桥模式时，设备可支持最近桥代理、最近非TPMR桥代理及最近客户桥代理，即对上述类型的代理MAC的LLDP报文进行处理，其他目的MAC的LLDP报文进行VLAN内透传。

![说明](LLDP命令.files/image001.png)

桥模式配置只在LLDP全局开启后才能生效，LLDP全局关闭时，只能作为客户桥对三种类型代理MAC的LLDP报文进行拦截。

【举例】

\# 配置LLDP桥模式为服务桥模式。

\<Sysname\> system-view

Sysname lldp mode service-bridge

【相关命令】

·**lldp global enable**

**LLDP \-- LLDP配置命令 \-- lldp notification med-topology-change enable**

------------------------------------------------------------------------

**[lldp notification med-topology-change enable**]命令用来开启LLDP-MED Trap功能。

**[undo lldp notification med-topology-change enable**]命令用来关闭LLDP-MED Trap功能。

【命令】

**[lldp notification med-topology-change enable**]

**[undo lldp notification med-topology-change enable**]

【缺省情况】

LLDP-MED Trap功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在接口GigabitEthernet1/0/1上开启LLDP-MED Trap功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp notification med-topology-change enable

**LLDP \-- LLDP配置命令 \-- lldp notification remote-change enable**

------------------------------------------------------------------------

**[lldp notification remote-change enable**]命令用来开启LLDP Trap功能。

**[undo lldp notification remote-change enable**]命令用来关闭LLDP Trap功能。

【命令】

在二层以太网接口视图/三层以太网接口视图/管理以太网接口视图下：

**[lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **notification remote-change enable**]]

**[undo lldp **[[ **agent** { **nearest-customer** \| **nearest-nontpmr** } ] **notification remote-change enable**]]

在二层聚合接口视图/三层聚合接口视图下：

**[lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **notification remote-change enable**]]

**[undo lldp agent **[{ **nearest-customer** \| **nearest-nontpmr** } **notification remote-change enable**]]

【缺省情况】

LLDP Trap功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[agent**]：开启指定类型LLDP代理的LLDP Trap功能。在以太网接口视图/管理以太网接口视图下，未指定时表示开启最近桥代理类型LLDP代理的LLDP Trap功能。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

【举例】

\# 在接口GigabitEthernet1/0/1最近客户桥代理上开启LLDP Trap功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp agent nearest-customer notification remote-change enable

**LLDP \-- LLDP配置命令 \-- lldp source-mac vlan**

------------------------------------------------------------------------

**[lldp source-mac vlan**]命令用来配置LLDP报文源MAC地址为指定VLAN关联三层以太网子接口的MAC地址。

**[undo lldp source-mac vlan**]命令用来恢复缺省情况。

【命令】

**[lldp source-mac vlan ***vlan-id*]

**[undo lldp source-mac vlan**]

【缺省情况】

LLDP报文源MAC地址为当前接口的MAC地址。

【视图】

三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定Dot1q终结中三层以太网子接口关联的VLAN ID，取值范围为1\~4094。指定该参数后，LLDP报文源MAC地址为该VLAN ID关联的三层以太网子接口；如果该VLAN ID没有关联的三层以太网子接口，则LLDP报文源MAC地址为当前接口的MAC地址。

【举例】

\# 配置LLDP报文源MAC地址为Dot1q终结中VLAN 4094关联的三层以太网子接口的MAC地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp source-mac vlan 4094

【相关命令】

·**lldp management-address arp-learning**

**LLDP \-- LLDP配置命令 \-- lldp timer fast-interval**

------------------------------------------------------------------------

**[lldp timer fast-interval**]命令用来配置LLDP快速发送报文的时间间隔。

**[undo lldp timer fast-interval**]命令用来恢复缺省情况。

【命令】

**[lldp timer fast-interval ***interval*]

**[undo lldp timer fast-interval**]

【缺省情况】

LLDP快速发送报文的时间间隔为1秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示LLDP快速发送报文的时间间隔，取值范围为1～3600，单位为秒。

【举例】

\# 配置LLDP快速发送报文的时间间隔为2秒。

\<Sysname\> system-view

Sysname lldp timer fast-interval 2

**LLDP \-- LLDP配置命令 \-- lldp timer notification-interval**

------------------------------------------------------------------------

**[lldp timer notification-interval**]命令用来配置LLDP Trap和LLDP-MED Trap信息的发送间隔。

**[undo lldp timer notification-interval**]命令用来恢复缺省情况。

【命令】

**[lldp timer notification-interval ***interval*]

**[undo lldp timer notification-interval**]

【缺省情况】

LLDP Trap和LLDP-MED Trap信息的发送间隔均为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示LLDP Trap和LLDP-MED Trap信息的发送间隔，取值范围为5～3600，单位为秒。

【举例】

\# 配置LLDP Trap和LLDP-MED Trap信息的发送间隔为8秒。

\<Sysname\> system-view

Sysname lldp timer notification-interval 8

**LLDP \-- LLDP配置命令 \-- lldp timer reinit-delay**

------------------------------------------------------------------------

**[lldp timer reinit-delay**]命令用来配置接口初始化的延迟时间。

**[undo lldp timer reinit-delay**]命令用来恢复缺省情况。

【命令】

**[lldp timer reinit-delay ***delay*]

**[undo lldp timer reinit-delay**]

【缺省情况】

接口初始化的延迟时间为2秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：接口初始化的延迟时间，取值范围为1～10，单位为秒。

【举例】

\# 配置接口初始化的延迟时间为4秒。

\<Sysname\> system-view

Sysname lldp timer reinit-delay 4

**LLDP \-- LLDP配置命令 \-- lldp timer tx-interval**

------------------------------------------------------------------------

**[lldp timer tx-interval**]命令用来配置LLDP报文的发送间隔。

**[undo lldp timer tx-interval**]命令用来恢复缺省情况。

【命令】

**[lldp timer tx-interval ***interval*]

**[undo lldp timer tx-interval**]

【缺省情况】

LLDP报文的发送间隔为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示LLDP报文的发送间隔，取值范围为5～32768，单位为秒。

【举例】

\# 配置LLDP报文的发送间隔为20秒。

\<Sysname\> system-view

Sysname lldp timer tx-interval 20

**LLDP \-- LLDP配置命令 \-- lldp tlv-enable**

------------------------------------------------------------------------

**[lldp tlv-enable**]命令用来配置接口上允许发布的TLV类型。

**[undo lldp tlv-enable**]命令用来配置接口上禁止发布的TLV类型。

【命令】

在二层以太网接口视图下：

·配置最近桥代理LLDP接口上允许发布的TLV类型

**[lldp**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** \| **dcbx** \| **protocol-vlan-id**  *vlan-id*  \| **vlan-name**  *vlan-id*  \| **management-vid**  *mvlan-id*  } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **network-policy**  *vlan-id*  \| **power-over-ethernet** \| **location-id** { **civic-address** *device-type country-code* { *ca-type ca-value* }&\<1-10\> \| **elin-address** *tel-number* } } }]]

**[undo lldp**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** \| **dcbx** \| **protocol-vlan-id** \| **vlan-name** \| **management-vid** } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **network-policy**  *vlan-id*  \| **power-over-ethernet** \| **location-id** } }]]

·配置最近非TPMR代理LLDP接口上允许发布的TLV类型

**[lldp agent nearest-nontpmr tlv-enable**[ { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **congestion-notification** \| **evb** \| **port-vlan-id** \| **link-aggregation** } }]]

**[undo lldp agent nearest-nontpmr tlv-enable**[ { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **congestion-notification** \| **evb** \| **port-vlan-id** \| **link-aggregation** } }]]

·配置最近客户桥代理LLDP接口上允许发布的TLV类型

**[lldp agent nearest-customer**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** } }]]

**[undo lldp agent nearest-customer**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** } }]]

在三层以太网接口视图/管理以太网接口视图下：

**[lldp**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6**   *ip-address* \| **interface** **loopback** *interface-number* ] } \| **dot1-tlv** { **all** \| **link-aggregation** } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **power-over-ethernet** \| **location-id** { **civic-address** *device-type country-code* { *ca-type ca-value* }&\<1-10\> \| **elin-address** *tel-number* } } }]]

**[lldp agent**[ { **nearest-nontpmr** \| **nearest-customer** } **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **link-aggregation** } }]]

**[undo lldp**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6**   *ip-address* \| **interface** **loopback** *interface-number* ] } \| **dot1-tlv** { **all** \| **link-aggregation** } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **power-over-ethernet** \| **location-id** } }]]

**[undo lldp agent**[ { **nearest-nontpmr** \| **nearest-customer** } **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  } \| **dot1-tlv** { **all** \| **link-aggregation** } }]]

在二层聚合接口视图下：

**[lldp agent nearest-nontpmr tlv-enable**[ { **basic-tlv** { **all** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **evb** \| **port-vlan-id** } }]]

**[lldp agent nearest-customer**[ **tlv-enable** { **basic-tlv** { **all** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **port-vlan-id** } }]]

**[lldp tlv-enable** **dot1-tlv** { **protocol-vlan-id** [ *vlan-id*  \| **vlan-name**  *vlan-id*  \| **management-vid**  *mvlan-id*  }]]

**[undo lldp agent nearest-nontpmr tlv-enable**[ { **basic-tlv** { **all** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **evb** \| **port-vlan-id** } }]]

**[undo lldp agent nearest-customer**[ **tlv-enable** { **basic-tlv** { **all** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **port-vlan-id** } }]]

**[undo lldp tlv-enable**[ **dot1-tlv** { **protocol-vlan-id** \| **vlan-name** \| **management-vid** } ]]

在三层聚合接口视图下：

**[lldp agent**[ { **nearest-customer** \| **nearest-nontpmr** } **tlv-enable basic-tlv** { **all** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  \| **port-description** \| **system-capability** \| **system-description** \| **system-name** }]]

**[undo lldp agent**[ { **nearest-customer** \| **nearest-nontpmr** } **tlv-enable** **basic-tlv** { **all** \| **management-address-tlv** [ **ipv6** ]  *ip-address*  \| **port-description** \| **system-capability** \| **system-description** \| **system-name** }]]

【缺省情况】

二层以太网接口上：

·最近桥代理允许发布除DCBX TLV、Location-id TLV、Port And Protocol VLAN ID TLV、VLAN Name TLV、Management VLAN ID TLV和EEE TLV之外所有类型的TLV；

·最近非TPMR桥代理只允许发布EVB TLV；

·最近客户桥代理允许发布基本TLV和IEEE 802.1组织定义TLV。

三层以太网接口/管理以太网接口上：

·最近桥代理允许发布除Network Policy TLV和EEE TLV之外所有类型的TLV，其中IEEE 802.1组织定义的TLV只支持Link Aggregation TLV；

·最近非TPMR桥代理不发布任何TLV；

·最近客户桥代理允许发布基本TLV和IEEE 802.1组织定义TLV，其中IEEE 802.1组织定义的TLV只支持Link Aggregation TLV。

二层聚合接口上：

·不存在最近桥代理；

·最近非TPMR桥代理只允许发布EVB TLV；

·最近客户桥代理允许发布基本TLV和IEEE 802.1组织定义TLV，其中IEEE 802.1组织定义的TLV只支持Port And Protocol VLAN ID TLV、VLAN Name TLV及Management VLAN ID TLV。

三层聚合接口上：

·不存在最近桥代理；

·最近非TPMR桥代理不发布任何TLV；

·最近客户桥代理只允许发布基本TLV。

【视图】

二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图

![说明](LLDP命令.files/image001.png)

不同型号的设备支持的视图不同，请以设备的实际情况为准。

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[agent**]：配置指定类型LLDP代理允许发布的TLV类型。在以太网接口视图/管理以太网接口视图下，未指定时表示配置最近桥代理允许发布的TLV类型。

**[nearest-customer**]：表示最近客户桥代理。

**[nearest-nontpmr**]：表示最近非TPMR桥代理。

**[all**]：在二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/管理以太网接口视图下指定**basic-tlv**、**dot1-tlv**或**dot3-tlv**，或者在三层聚合接口视图下指定**basic-tlv**时，本参数表示该类型下所有的可选TLV；而在二层以太网接口视图/三层以太网接口视图/管理以太网接口视图下指定**med-tlv**时，本参数都表示该类型下除**location-id**以外所有的可选TLV。

**[basic-tlv**]：表示基本类型TLV。

**[management-address-tlv** [ **ipv6**  [ *ip-address* \| **interface** **loopback** *interface-number* ]]]：表示Management Address TLV。其中，**ipv6**表示LLDP报文中所要发布的管理地址为IPv6格式的地址，当未指定**ipv6**时，表示LLDP报文中所要发布的管理地址为IPv4格式的地址。*ip-address*表示在LLDP报文中发布的管理地址为指定的IP地址，**interface** **loopback** *interface-number*表示在LLDP报文中发布的管理地址为指定的LoopBack接口的IP地址。其缺省值根据当前接口视图确定：

·在二层以太网接口视图/二层聚合接口视图下：

当未指定**ipv6**参数时，若未指定*ip-address*，则发布的管理地址为当前接口允许通过的、对应VLAN接口上配置有IPv4地址且处于up状态的最小VLAN的主IPv4地址（如果当前接口允许通过的所有VLAN所对应的VLAN接口上都未配置IPv4地址或均处于down状态，则发布当前接口的MAC地址）；

当指定了**ipv6**参数时，若未指定*ip-address*，则发布的管理地址为当前接口允许通过的、对应VLAN接口上配置有IPv6地址且处于up状态的最小VLAN的主IPv6地址（如果当前接口允许通过的所有VLAN所对应的VLAN接口上都未配置IPv6地址或均处于down状态，则发布当前接口的MAC地址）。

·在三层以太网接口视图/三层聚合接口视图/管理以太网接口视图下：

当未指定**ipv6**参数时，若未指定*ip-address、*指定的LoopBack接口不存在或LoopBack接口没有配置IPv4地址，则发布的管理地址为当前接口的IPv4地址（如果当前接口未配置IPv4地址，则发布当前接口的MAC地址）；

当指定了**ipv6**参数时，若未指定*ip-address*、指定的LoopBack接口不存在或LoopBack接口没有配置IPv6地址，则发布的管理地址为当前接口的IPv6地址（如果当前接口未配置IPv6地址，则发布当前接口的MAC地址）。

·在二层以太网接口视图/二层聚合接口视图/三层以太网接口视图/三层聚合接口视图/管理以太网接口视图下：

执行**undo**命令时，如果不带**ipv6**、*ip-address*和**interface** **loopback** *interface-number*参数表示不发布该TLV；如果带**ipv6**、*ip-address*或**interface** **loopback** *interface-number*参数表示按缺省值发布该TLV。

**[port-description**]：表示Port Description TLV。

**[system-capability**]：表示System Capabilities TLV。

**[system-description**]：表示System Description TLV。

**[system-name**]：表示System Name TLV。

**[dot1-tlv**]：表示IEEE 802.1组织定义的TLV。

**[congestion-notification**]：表示QCN（Quantized Congestion Notification，量化拥塞通知）模块TLV，目前QCN模块只支持LLDP中三种代理类型中的最近桥代理类型。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[dcbx**]：表示Data Center Bridging Exchange Protocol TLV。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[evb**]：表示EVB（Edge Virtual Bridging，边缘虚拟桥接）模块TLV。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[port-vlan-id**]：表示Port VLAN ID TLV。

**[protocol-vlan-id** [ *vlan-id* ]]：表示Port And Protocol VLAN ID TLV，*vlan-id*为所要发布VLAN的VLAN ID，取值范围为1～4094，缺省值为该端口所属VLAN中最小的VLAN ID。

**[vlan-name** [ *vlan-id* ]]：表示VLAN Name TLV，*vlan-id*为所要发布VLAN的VLAN ID，取值范围为1～4094，缺省值为该端口所属VLAN中最小的VLAN ID。

**[management-vid** [ *mvlan-id* ]]：表示Management VLAN ID TLV。*mvlan-id*指定要发布管理VLAN的VLAN ID，取值范围为1～4094。如果未指定该参数，则表示发布0，表示当前LLDP agent未配置管理VLAN。

**[link-aggregation**]：表示Link Aggregation TLV。

**[dot3-tlv**]：表示IEEE 802.3组织定义的TLV。

**[link-aggregation**]：表示Link Aggregation TLV。

**[mac-physic**]：表示MAC/PHY Configuration/Status TLV。

**[max-frame-size**]：表示Maximum Frame Size TLV。

**[power**]：表示Power Via MDI TLV和Power Stateful Control TLV。

**[eee**]：表示Energy-Efficient Ethernet TLV。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[med-tlv**]：表示LLDP-MED TLV。

**[capability**]：表示LLDP-MED Capabilities TLV。

**[inventory**]：表示Hardware Revision TLV、Firmware Revision TLV、Software Revision TLV、Serial Number TLV、Manufacturer Name TLV、Model Name TLV和Asset ID TLV。

**[location-id**]：表示Location Identification TLV。

**[civic-address**]：表示Location Identification TLV封装网络设备的普通地址信息。

*[device-type*]：表示设备类型，取值范围为0～2。0表示设备类型为DHCP server，1表示设备类型为Network device，2表示设备类型为LLDP-MED Endpoint。

*[country-code*]：表示国家编码，取值范围请参考ISO 3166。

{ *ca-type ca-value* }&\<1-10\>：地址信息。*ca-type*表示地址信息类型，取值范围为0～255；*ca-value*表示地址信息，为1～250个字符的字符串。&\<1-10\>表示前面的参数最多可以输入10次。

**[elin-address**]：Location Identification TLV封装紧急电话号码。

*[tel-number*]：表示紧急电话号码，为10～25个字符的字符串，只能包含数字。

**[network-policy** [ *vlan-id* ]]：表示Network Policy TLV，*vlan-id*为要发布的Voice VLAN ID，取值范围为1～4094。

**[power-over-ethernet**]：表示Extended Power-via-MDI TLV。

【使用指导】

·在使用本命令时若不指定**all**参数，每次只能配置某类型下的一种可选TLV，此时可通过多次使用该命令来配置各类型下的多种可选TLV。

·如果禁止发布802.3的组织定义的MAC/PHY Configuration/Status TLV，则LLDP-MED TLV将不会被发布，不论其是否被允许发布；如果禁止发布LLDP-MED Capabilities TLV，则其它LLDP-MED TLV将不会被发布，不论其是否被允许发布。

·IEEE 802.1组织定义的TLV的Port And Protocol VLAN ID TLV、VLAN Name TLV及Management VLAN ID TLV只能基于最近桥代理配置，但是其配置会被最近非TPMR桥代理和最近客户桥代理继承。

【举例】

\# 配置接口GigabitEthernet1/0/1上最近客户桥代理允许发布IEEE 802.1组织定义的Link Aggregation可选TLV。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 lldp agent nearest-customer tlv-enable dot1-tlv link-aggregation
