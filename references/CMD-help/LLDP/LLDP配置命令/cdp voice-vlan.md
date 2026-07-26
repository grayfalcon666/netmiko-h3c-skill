::: {#-1204032224 .myid}
[]{#_Toc404784690}[]{#struct_0_x1289_x1771_1326472709}[]{#_Toc352678892}[]{#_Toc352661499}

**LLDP \-- LLDP配置命令 \-- cdp voice-vlan**

------------------------------------------------------------------------

[**[cdp voice-vlan]{lang="EN-US"}**]{#struct_0_x1289_x1771_x26076014}[命令用来配置]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文携带的]{style="font-family:宋体"}[Voice VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cdp voice-vlan]{lang="EN-US"}**]{#struct_0_x1289_x1771_796008803}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1442540181}

[**[cdp voice-vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1289_x1771_775300821}

[**[undo cdp voice-vlan]{lang="EN-US"}**]{#struct_0_x1289_x1771_578400355}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2017332785}

[[未配置]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1378197591}[报文携带的]{style="font-family:宋体"}[Voice VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1948947754}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1525643953}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_218378237}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1326407173}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x766984514}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x76090349}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x1289_x1771_1093435264}[：要发布的]{style="font-family:宋体"}[Voice VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x722160136}

[[配置本命令后，设备当前接口向对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1289_x1771_1120993493}[电话发送的]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文携带的]{style="font-family:宋体"}[Voice VLAN ID]{lang="EN-US"}[为本命令配置的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1289_x1771_2065862803}[电话收到本端发送的]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文后，会根据报文中携带的]{style="font-family:宋体"}[Voice VLAN ID]{lang="EN-US"}[发送语音数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x452317319}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_972341740}[配置]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文携带的]{style="font-family:宋体"}[Voice VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_1911479400}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] cdp voice-vlan 100]{lang="EN-US"}
:::

::::: {#-1868338396 .myid}
[]{#_Toc404784691}[]{#struct_0_x1289_x1771_499737374}[]{#_Toc362275727}

**LLDP \-- LLDP配置命令 \-- dcbx version**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_2100028854}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x1924285370}
:::

**[ ]{lang="EN-US"}**

[**[dcbx version]{lang="EN-US"}**]{#struct_0_x1289_x1771_x148118017}[命令用来配置]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[undo dcbx version]{lang="EN-US"}**]{#struct_0_x1289_x1771_431732132}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_830962534}

[**[dcbx version ]{lang="EN-US"}**[{ **rev100** \| **rev101** \| **standard** }]{lang="EN-US"}]{#struct_0_x1289_x1771_83199036}

[**[undo dcbx version]{lang="EN-US"}**]{#struct_0_x1289_x1771_499671838}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1822449873}

[[未配置]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1289_x1771_x96854600}[版本，此时]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[版本由两端端口自协商决定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x517415737}

[[二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x2044907408}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_114901871}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1504515923}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_58218497}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x67158774}

[**[rev100]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1714599574}[：表示采用预标准版]{style="font-family:宋体"}[1.00]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rev101]{lang="EN-US"}**]{#struct_0_x1289_x1771_962888876}[：表示采用预标准版]{style="font-family:宋体"}[1.01]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[standard]{lang="EN-US"}**]{#struct_0_x1289_x1771_1672869709}[：表示采用标准版。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_499606302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，配置的]{style="font-family:宋体"}]{#struct_0_x1289_x1771_508880343}[DCBX]{lang="EN-US"}[版本需要视对端设备支持的版本而定，要求两端端口的]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[版本配置一致，否则版本无法兼容，将会导致]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[无法正常工作。建议配置两端设备都支持的最高版本（版本从高到低的顺序为：标准版]{style="font-family:宋体"}[-\>]{lang="EN-US"}[预标准版]{style="font-family:宋体"}[1.01-\>]{lang="EN-US"}[预标准版]{style="font-family:宋体"}[1.00]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令后，本端端口发送的]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x86511508}[LLDP]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[版本为配置的版本，不再与对端端口进行]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[版本协商。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当端口的]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1187407808}[DCBX]{lang="EN-US"}[版本采用自协商决定，协商的初始版本为]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[标准版，以保证优先协商到该版本。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_216913087}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_2111588067}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[版本为预标准版]{style="font-family:宋体"}[1.01]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_1671863713}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dcbx version rev101]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_288008346}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp tlv-enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_x968886692}
:::::

::::: {#491889923 .myid}
[]{#_Toc404784692}[]{#struct_0_x1289_x1771_x1516057613}[]{#_Toc144347671}[]{#_Toc378693091}[]{#_Toc379979755}

**LLDP \-- LLDP配置命令 \-- display lldp local-information**

------------------------------------------------------------------------

[**[display lldp local-information]{lang="EN-US"}**]{#struct_0_x1289_x1771_x973311939}[命令用来显示]{style="font-family:
宋体"}[LLDP]{lang="EN-US"}[本地信息，这些信息将根据端口]{style="font-family:宋体"}[TLV]{lang="EN-US"}[开启情况被组织成]{style="font-family:宋体"}[TLV]{lang="EN-US"}[发送给邻居设备。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1050440314}

[**[display lldp local-information]{lang="EN-US"}**[ \[]{lang="EN-US"}[ **global** \| **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1289_x1771_401343651}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1393809885}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x602128838}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1874160201}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1719172343}

[[network-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_796263318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1101698793}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_1935394951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x973901762}

[**[global]{lang="EN-US"}**]{#struct_0_x1289_x1771_858623555}[：显示全局]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[本地信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1289_x1771_1883756614}[：显示指定接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[本地信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_804151368}

[[如果未指定任何参数，将显示所有]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_856680567}[本地信息，包括全局]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息以及所有开启了]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能且状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[的接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_819049832}

[]{#struct_0_x1289_x1771_385469688}[]{#_Toc135620324}[]{#_Toc135620327}[]{#_Toc135620328}[]{#_Toc135620329}[]{#_Toc135620330}[]{#_Toc135620331}[]{#_Toc135620332}[]{#_Toc135620333}[]{#_Toc135620334}[]{#_Toc135620335}[]{#_Toc135620336}[]{#_Toc135620337}[]{#_Toc135620338}[]{#_Toc135620339}[]{#_Toc135620340}[]{#_Toc135620341}[]{#_Toc135620342}[]{#_Toc135620343}[]{#_Toc135620345}[]{#_Toc135620346}[]{#_Toc135620347}[]{#_Toc135620348}[]{#_Toc135620349}[]{#_Toc135620350}[]{#_Toc135620351}[]{#_Toc135620352}[]{#_Toc135620354}[]{#_Toc135620355}[]{#_Toc135620356}[]{#_Toc135620357}[]{#_Toc135620358}[]{#_Toc135620359}[]{#_Hlt5077351}[]{#_Toc135620360}[]{#_Toc135620361}[]{#_Toc135620362}[]{#_Toc135620363}[]{#_Toc135620364}[]{#_Toc135620365}[]{#_Toc135620366}[]{#_Toc135620367}[]{#_Toc135620368}[]{#_Toc135620369}[\# ]{lang="EN-US"}[显示所有]{style="font-family:
宋体"}[LLDP]{lang="EN-US"}[本地信息（假设]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[的版本为标准版）。]{style="font-family:宋体"}

[[\<Sysname\> display lldp local-information]{lang="EN-US"}]{#struct_0_x1289_x1771_x973639618}

[Global LLDP local-information:]{lang="EN-US"}

[ Chassis ID          : 00e0-fc00-5600]{lang="EN-US"}

[ System name         : Sysname]{lang="EN-US"}

[ System description  : H3C Comware Platform Software]{lang="EN-US"}

[ System capabilities supported  : Bridge, Router, Customer Bridge, Service Bridge]{lang="EN-US"}

[ System capabilities enabled    : Bridge, Router, Service Bridge]{lang="EN-US"}

[ ]{lang="EN-US"}

[ MED information:]{lang="EN-US"}

[ Device class               : Connectivity device]{lang="EN-US"}

[ MED inventory information of master board:]{lang="EN-US"}

[ HardwareRev                : REV.A]{lang="EN-US"}

[ FirmwareRev                : 109]{lang="EN-US"}

[ SoftwareRev                : 5.20 Alpha 2101]{lang="EN-US"}

[ SerialNum                  : NONE]{lang="EN-US"}

[ Manufacturer name          : H3C]{lang="EN-US"}

[ Model name                 : H3C Comware]{lang="EN-US"}

[ Asset tracking identifier  : Unknown]{lang="EN-US"}

[LLDP local-information of port 52\[GigabitEthernet1/0/3\]:]{lang="EN-US"}

[ Port ID type       : Interface name]{lang="EN-US"}

[ Port ID            : GigabitEthernet1/0/3]{lang="EN-US"}

[ Port description   : GigabitEthernet1/0/3 Interface]{lang="EN-US"}

[ LLDP agent nearest-bridge management address:]{lang="EN-US"}

[ Management address type           : IPv4]{lang="EN-US"}

[ Management address                : 192.168.80.60]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ LLDP agent nearest-nontpmr management address:]{lang="EN-US"}

[ Management address type           : IPv4]{lang="EN-US"}

[ Management address                : 192.168.80.61]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ LLDP agent nearest-customer management address:]{lang="EN-US"}

[ Management address type           : IPv4]{lang="EN-US"}

[ Management address                : 192.168.80.62]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ DCBX Control info:]{lang="EN-US"}

[ Oper version       : Standard]{lang="EN-US"}

[ DCBX ETS configuration info:]{lang="EN-US"}

[  CBS                : False]{lang="EN-US"}

[  Max TCs            : 8]{lang="EN-US"}

[  CoS     Local Priority      Percentage        TSA]{lang="EN-US"}

[   0            0                 15            ETS]{lang="EN-US"}

[   1            1                 0             SP]{lang="EN-US"}

[   2            2                 15            ETS]{lang="EN-US"}

[   3            3                 14            ETS]{lang="EN-US"}

[   4            4                 14            ETS]{lang="EN-US"}

[   5            5                 14            ETS]{lang="EN-US"}

[   6            6                 14            ETS]{lang="EN-US"}

[   7            7                 14            ETS]{lang="EN-US"}

[ DCBX ETS recommendation info:]{lang="EN-US"}

[  CoS     Local Priority      Percentage        TSA]{lang="EN-US"}

[   0            0                 15            ETS]{lang="EN-US"}

[   1            1                 0             SP]{lang="EN-US"}

[   2            2                 15            ETS]{lang="EN-US"}

[   3            3                 14            ETS]{lang="EN-US"}

[   4            4                 14            ETS]{lang="EN-US"}

[   5            5                 14            ETS]{lang="EN-US"}

[   6            6                 14            ETS]{lang="EN-US"}

[   7            7                 14            ETS]{lang="EN-US"}

[ DCBX PFC info:]{lang="EN-US"}

[  P0-0     P1-1     P2-1     P3-1     P4-0     P5-0     P6-0     P7-0]{lang="EN-US"}

[  Number of traffic classes supported: 8]{lang="EN-US"}

[  Value of MBC: 0]{lang="EN-US"}

[ DCBX APP info:]{lang="EN-US"}

[  Selected Field  Protocol ID  Priority]{lang="EN-US"}

[  UDP/DCCP        100          0x3]{lang="EN-US"}

[  TCP/SCTP        200          0x3]{lang="EN-US"}

[  Ethertype       0x1234       0x3]{lang="EN-US"}

[  Ethertype       0x8906       0x3]{lang="EN-US"}

[ Port VLAN ID(PVID): 1]{lang="EN-US"}

[ Port and protocol VLAN ID(PPVID) : 12]{lang="EN-US"}

[ Port and protocol VLAN supported : Yes]{lang="EN-US"}

[ Port and protocol VLAN enabled   : Yes]{lang="EN-US"}

[ VLAN name of VLAN 12: VLAN 0012]{lang="EN-US"}

[ Management VLAN ID  : 5]{lang="EN-US"}

[ Auto-negotiation supported : Yes]{lang="EN-US"}

[ Auto-negotiation enabled   : Yes]{lang="EN-US"}

[ OperMau                    : Speed(1000)/Duplex(Full)]{lang="EN-US"}

[ Power port class           : PD]{lang="EN-US"}

[ PSE power supported        : Yes]{lang="EN-US"}

[ PSE power enabled          : Yes]{lang="EN-US"}

[ PSE pairs control ability  : Yes]{lang="EN-US"}

[ Power pairs                : Signal]{lang="EN-US"}

[ Port power classification  : Class 0]{lang="EN-US"}

[ Power type                 : Type 2 PSE]{lang="EN-US"}

[ Power source               : Primary]{lang="EN-US"}

[ Power priority             : High]{lang="EN-US"}

[ PD requested power value   : 21.1 w]{lang="EN-US"}

[ PSE allocated power value  : 15.3 w]{lang="EN-US"}

[ Link aggregation supported : Yes]{lang="EN-US"}

[ Link aggregation enabled   : Yes]{lang="EN-US"}

[ Aggregation port ID        : 52]{lang="EN-US"}

[ Congestion notification TLV info:]{lang="EN-US"}

[  Dot1p          CNPV         Ready]{lang="EN-US"}

[  0              Yes          Yes]{lang="EN-US"}

[  1              No           No]{lang="EN-US"}

[  2              No           No]{lang="EN-US"}

[  3              No           No]{lang="EN-US"}

[  4              Yes          No]{lang="EN-US"}

[  5              Yes          Yes]{lang="EN-US"}

[  6              No           No]{lang="EN-US"}

[  7              No           No]{lang="EN-US"}

[ Maximum frame size         : 1500]{lang="EN-US"}

[ Transmit Tw                : 100 us]{lang="EN-US"}

[ Receive Tw                 : 90 us]{lang="EN-US"}

[ Fallback Tw                : 90 us]{lang="EN-US"}

[ Echo Transmit Tw           : 0 us]{lang="EN-US"}

[ Echo Receive Tw            : 0 us]{lang="EN-US"}

[ Location format       : Civic Address LCI]{lang="EN-US"}

[ Location information  :]{lang="EN-US"}

[  What(1)  Country(CN)]{lang="EN-US"}

[  CA type  CA value]{lang="EN-US"}

[  0        Chinese]{lang="EN-US"}

[  1        Zhejiang]{lang="EN-US"}

[  2        Hangzhou]{lang="EN-US"}

[ MED port information:]{lang="EN-US"}

[  Media policy type        : Unknown]{lang="EN-US"}

[  Unknown policy           : Yes]{lang="EN-US"}

[  VLAN tagged              : No]{lang="EN-US"}

[  Media policy VLANID      : 0]{lang="EN-US"}

[  Media policy L2 priority : 0]{lang="EN-US"}

[  Media policy DSCP        : 0]{lang="EN-US"}

[ PoE PSE power source       : Primary]{lang="EN-US"}

[ Port PSE priority          : Critical]{lang="EN-US"}

[ Port available power value : 30.0 w]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x1446909619}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_782410448}
:::

[ ]{lang="EN-US"}

[]{#_Toc144347672}[[表1-1 ]{lang="EN-US"}[display lldp local-information]{lang="EN-US"}]{#struct_0_x1289_x1771_x1354545193}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x157647143}[[字段]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x973574082}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x720710444}

[[Global LLDP local-information]{lang="EN-US"}]{#struct_0_x1289_x1771_2058420606}

[[本设备的全局]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_444340500}[本地信息]{style="font-family:宋体"}

[[Chassis ID]{lang="EN-US"}]{#struct_0_x1289_x1771_56349062}

[[Chassis ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x948823139}[值，为本设备的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[System name]{lang="EN-US"}]{#struct_0_x1289_x1771_x973770690}

[[系统名称]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1631126187}

[[System description]{lang="EN-US"}]{#struct_0_x1289_x1771_1629367229}

[[系统描述]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1404715163}

[[System capabilities supported]{lang="EN-US"}]{#struct_0_x1289_x1771_x1464175074}

[[系统所支持的功能：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x2105647865}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x973705154}[：表示支持交换功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x1289_x1771_x1492688784}[：表示支持路由功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WlanAccessPoint]{lang="EN-US"}]{#struct_0_x1289_x1771_1665238970}[：表示支持无线接入点功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x1289_x1771_x428036296}[：表示支持路由功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Telephone]{lang="EN-US"}]{#struct_0_x1289_x1771_x1263724747}[：表示支持电话功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DocsisCableDevice]{lang="EN-US"}]{#struct_0_x1289_x1771_x973377474}[：表示支持电缆设备功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StationOnly]{lang="EN-US"}]{#struct_0_x1289_x1771_x1522251476}[：表示支持只作站点功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Customer Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_756537751}[：表示支持客户桥功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x212112864}[：表示支持服务桥功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TPMR]{lang="EN-US"}]{#struct_0_x1289_x1771_x1810372386}[：表示支持双端口]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[中继功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_x1289_x1771_905983435}[：表示支持不在上述列表的其它功能]{lang="EN-US" style="font-family:宋体"}

[[System capabilities enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_x973311938}

[[系统已开启的功能：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1050374778}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_181578784}[：表示交换功能已开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x1289_x1771_x501450397}[：表示路由功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WlanAccessPoint]{lang="EN-US"}]{#struct_0_x1289_x1771_2084565354}[：表示无线接入点功能已开启]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x1289_x1771_x973901765}[：表示路由功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Telephone]{lang="EN-US"}]{#struct_0_x1289_x1771_859082307}[：表示电话功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DocsisCableDevice]{lang="EN-US"}]{#struct_0_x1289_x1771_x1073015439}[：表示电缆设备功能已开启]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StationOnly]{lang="EN-US"}]{#struct_0_x1289_x1771_x98799159}[：表示只作站点功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Customer Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x973836229}[：表示客户桥功能已开启]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_66895527}[：表示服务桥功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TPMR]{lang="EN-US"}]{#struct_0_x1289_x1771_x104694379}[：表示双端口]{style="font-family:宋体"}[MAC]{lang="EN-US"}[中继功能已开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_x1289_x1771_x255933423}[：表示不在上述列表的其它功能已开启]{lang="EN-US" style="font-family:宋体"}

[[MED information]{lang="EN-US"}]{#struct_0_x1289_x1771_x974032837}

[[MED]{lang="EN-US"}]{#struct_0_x1289_x1771_372632274}[设备相关信息]{style="font-family:宋体"}

[[Device class]{lang="EN-US"}]{#struct_0_x1289_x1771_x316402642}

[[MED]{lang="EN-US"}]{#struct_0_x1289_x1771_1193666923}[设备类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connectivity device]{lang="EN-US"}]{#struct_0_x1289_x1771_x973967301}[：表示网络设备]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class I]{lang="EN-US"}]{#struct_0_x1289_x1771_x716748309}[：表示一般终端设备，即所有需要]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[发现服务的终端设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class II]{lang="EN-US"}]{#struct_0_x1289_x1771_x301959273}[：表示媒体终端设备，即具备媒体能力的终端设备，其能力包含了一般终端设备的能力。]{style="font-family:宋体"}[该类设备支持媒体流]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class III]{lang="EN-US"}]{#struct_0_x1289_x1771_x939390155}[：表示通讯终端设备，即直接支持目标用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[通讯系统的终端设备，其能力包含了一般终端设备和媒体终端设备的所有能力。]{style="font-family:宋体"}[该类设备直接被目标用户所使用]{lang="EN-US" style="font-family:宋体"}

[[MED inventory information of master board]{lang="EN-US"}]{#struct_0_x1289_x1771_x973639621}

[[主控板]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_x1289_x1771_x1447499444}[资产信息]{style="font-family:宋体"}

[[HardwareRev]{lang="EN-US"}]{#struct_0_x1289_x1771_2067425725}

[[产品的硬件版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1759612632}

[[FirmwareRev]{lang="EN-US"}]{#struct_0_x1289_x1771_x973574085}

[[产品的固件版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x720907052}

[[SoftwareRev]{lang="EN-US"}]{#struct_0_x1289_x1771_100437276}

[[产品的软件版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1534343893}

[[SerialNum]{lang="EN-US"}]{#struct_0_x1289_x1771_x973770693}

[[序列号]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1630929579}

[[Manufacturer name]{lang="EN-US"}]{#struct_0_x1289_x1771_x745913291}

[[制造厂商]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x973705157}

[[Model name]{lang="EN-US"}]{#struct_0_x1289_x1771_x1492754320}

[[模块名称]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1068223017}

[[Asset tracking identifier]{lang="EN-US"}]{#struct_0_x1289_x1771_x398282274}

[[资产跟踪]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x973377477}

[[LLDP local-information of port 1]{lang="EN-US"}]{#struct_0_x1289_x1771_x1522448084}

[[端口]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1289_x1771_2090324384}[上]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[本地信息]{style="font-family:宋体"}

[[Port ID type]{lang="EN-US"}]{#struct_0_x1289_x1771_x973311941}

[[端口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x1050964601}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC address]{lang="EN-US"}]{#struct_0_x1289_x1771_536319705}[：表示]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface name]{lang="EN-US"}]{#struct_0_x1289_x1771_x973901764}[：表示接口名称]{lang="EN-US" style="font-family:宋体"}

[[Port ID]{lang="EN-US"}]{#struct_0_x1289_x1771_859016771}

[[端口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x1842092304}[值，根据本设备的]{style="font-family:宋体"}[Port ID type]{lang="EN-US"}[取相应类型的值]{style="font-family:宋体"}

[[Port description]{lang="EN-US"}]{#struct_0_x1289_x1771_x973836228}

[[端口描述]{style="font-family:宋体"}]{#struct_0_x1289_x1771_66961063}

[[LLDP agent nearest-bridge management address]{lang="EN-US"}]{#struct_0_x1289_x1771_x974032836}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_372697810}[缺省代理，即最近桥代理的管理地址]{style="font-family:宋体"}

[[LLDP agent nearest-customer management address]{lang="EN-US"}]{#struct_0_x1289_x1771_2014170926}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x973967300}[最近客户桥代理的管理地址]{style="font-family:宋体"}

[[LLDP agent nearest-nontpmr management address]{lang="EN-US"}]{#struct_0_x1289_x1771_x716813845}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x208374453}[最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理的管理地址]{style="font-family:宋体"}

[[Management address type]{lang="EN-US"}]{#struct_0_x1289_x1771_x973639620}

[[管理地址类型]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1447433908}

[[Management address]{lang="EN-US"}]{#struct_0_x1289_x1771_1419064856}

[[管理地址]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x973574084}

[[Management address interface type]{lang="EN-US"}]{#struct_0_x1289_x1771_x720841516}

[[管理地址所在接口的编码方式]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x973770692}

[[Management address interface ID]{lang="EN-US"}]{#struct_0_x1289_x1771_1630995115}

[[管理地址接口索引]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1609682155}

[[Management address OID]{lang="EN-US"}]{#struct_0_x1289_x1771_x973705156}

[[管理地址对象标识符]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1492819856}

[[DCBX control info]{lang="EN-US"}]{#struct_0_x1289_x1771_x973377476}

[[显示]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1289_x1771_x1522382548}[控制]{style="font-family:宋体"}[TLV]{lang="EN-US"}[的信息，在标准]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[中显示版本信息]{style="font-family:宋体"}

[[Oper version]{lang="EN-US"}]{#struct_0_x1289_x1771_1725457091}

[[DCBX]{lang="EN-US"}]{#struct_0_x1289_x1771_x973311940}[版本号]{style="font-family:宋体"}

[[Sequence number]{lang="EN-US"}]{#struct_0_x1289_x1771_x1050899065}

[[DCBX TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_592182180}[内容改变的次数]{style="font-family:宋体"}

[[Acknowledge number]{lang="EN-US"}]{#struct_0_x1289_x1771_1448908303}

[[对端设备同步配置的次数]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1976768633}

[[DCBX ETS info]{lang="EN-US"}]{#struct_0_x1289_x1771_592247716}

[[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_x667898165}[与本地优先级的映射关系及对应的带宽分配情况]{style="font-family:宋体"}

[[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_592051108}

[[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_x2107205676}[值]{style="font-family:宋体"}

[[Local Priority]{lang="EN-US"}]{#struct_0_x1289_x1771_979757997}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592116644}

[[Percentage]{lang="EN-US"}]{#struct_0_x1289_x1771_x1686750845}

[[对应的带宽分配]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592444324}

[[P0-     P1-     P2-     P3-     P4-     P5-     P6-     P7-]{lang="EN-US"}]{#struct_0_x1289_x1771_x797671115}

[[本端的]{style="font-family:宋体"}[no-drop]{lang="EN-US"}]{#struct_0_x1289_x1771_592509860}[标记值对应的支持的优先级数]{style="font-family:宋体"}

[[Number of traffic classes supported]{lang="EN-US"}]{#struct_0_x1289_x1771_x1995978828}

[[PFC]{lang="EN-US"}]{#struct_0_x1289_x1771_1322607138}[支持的能力集，只在]{style="font-family:宋体"}[1.01]{lang="EN-US"}[版本中显示该项]{style="font-family:宋体"}

[[DCBX APP info]{lang="EN-US"}]{#struct_0_x1289_x1771_592313252}

[[显示]{style="font-family:宋体"}[APP TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_103812081}[信息]{style="font-family:宋体"}

[[Selected Field]{lang="EN-US"}]{#struct_0_x1289_x1771_592378788}

[[选择域]{style="font-family:宋体"}]{#struct_0_x1289_x1771_566865632}

[[Priority]{lang="EN-US"}]{#struct_0_x1289_x1771_592706468}

[[优先级]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1866420344}

[[Protocol ID]{lang="EN-US"}]{#struct_0_x1289_x1771_592772004}

[[应用协议号]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1052713855}

[[CoS map]{lang="EN-US"}]{#struct_0_x1289_x1771_592182181}

[[应用协议与]{style="font-family:宋体"}[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_1448908302}[的映射关系]{style="font-family:宋体"}

[[DCBX ETS configuration info]{lang="EN-US"}]{#struct_0_x1289_x1771_592247717}

[[显示]{style="font-family:宋体"}[ETS]{lang="EN-US"}]{#struct_0_x1289_x1771_x667898166}[配置]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[CBS]{lang="EN-US"}]{#struct_0_x1289_x1771_1349156077}

[[是否支持]{style="font-family:宋体"}[CBS]{lang="EN-US"}]{#struct_0_x1289_x1771_592051109}[，表示本端是否支持令牌桶限速算法：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_x1289_x1771_x2107205675}[：表示不支持令牌桶限速算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[True]{lang="EN-US"}]{#struct_0_x1289_x1771_592116645}[：表示支持令牌桶限速算法]{lang="EN-US" style="font-family:宋体"}

[[Max TCs]{lang="EN-US"}]{#struct_0_x1289_x1771_x1686750844}

[[支持的最大优先级数目]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592444325}

[[TSA]{lang="EN-US"}]{#struct_0_x1289_x1771_592509861}

[[传输选择算法]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1995978829}

[[DCBX ETS recommendation info]{lang="EN-US"}]{#struct_0_x1289_x1771_592313253}

[[显示]{style="font-family:宋体"}[ETS]{lang="EN-US"}]{#struct_0_x1289_x1771_103812082}[推荐]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[DCBX PFC info]{lang="EN-US"}]{#struct_0_x1289_x1771_592378789}

[[显示]{style="font-family:宋体"}[PFC TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_566865633}[信息]{style="font-family:宋体"}

[[Value of MBC]{lang="EN-US"}]{#struct_0_x1289_x1771_592706469}

[[支持的]{style="font-family:宋体"}[MBC]{lang="EN-US"}]{#struct_0_x1289_x1771_1866420343}[状态（]{style="font-family:宋体"}[MBC]{lang="EN-US"}[表示报文避开]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[的能力，占]{style="font-family:宋体"}[1]{lang="EN-US"}[个]{style="font-family:宋体"}[bit]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[去开启时，报文可以避开]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[关闭时，报文不可以避开]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Port VLAN ID(PVID)]{lang="EN-US"}]{#struct_0_x1289_x1771_592772005}

[[端口]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_1052713856}

[[Port and protocol VLAN ID(PPVID)]{lang="EN-US"}]{#struct_0_x1289_x1771_592182178}

[[端口协议]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_257267207}

[[Port and protocol VLAN supported]{lang="EN-US"}]{#struct_0_x1289_x1771_592247714}

[[是否支持端口协议]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_x667898167}

[[Port and protocol VLAN enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_592051106}

[[是否已开启端口协议]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_x2107205666}

[[VLAN name of VLAN 12]{lang="EN-US"}]{#struct_0_x1289_x1771_592116642}

[[VLAN 12]{lang="EN-US"}]{#struct_0_x1289_x1771_x1686750843}[的名称]{style="font-family:宋体"}

[[Management VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_592444322}

[[管理]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_592509858}

[[Auto-negotiation supported]{lang="EN-US"}]{#struct_0_x1289_x1771_x422000708}

[[端口是否支持自协商]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592313250}

[[Auto-negotiation enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_103812083}

[[端口是否已开启自协商]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592378786}

[[OperMau]{lang="EN-US"}]{#struct_0_x1289_x1771_566865638}

[[端口自适应的速率和双工状态]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592706466}

[[Power port class]{lang="EN-US"}]{#struct_0_x1289_x1771_592772002}

[[PoE]{lang="EN-US"}]{#struct_0_x1289_x1771_1052713861}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_592182179}[（]{lang="EN-US" style="font-family:宋体"}[Power Sourcing Equipment]{lang="EN-US"}[,]{lang="EN-US"}[供电设备）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_257267206}[（]{lang="EN-US" style="font-family:宋体"}[Powered Device]{lang="EN-US"}[，受电设备）]{lang="EN-US" style="font-family:宋体"}

[[PSE power supported]{lang="EN-US"}]{#struct_0_x1289_x1771_592247715}

[[是否支持]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_592051107}[供电]{style="font-family:宋体"}

[[PSE power enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_x2107205665}

[[是否已开启]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_592116643}[供电]{style="font-family:宋体"}

[[PSE pairs control ability]{lang="EN-US"}]{#struct_0_x1289_x1771_x1686750842}

[[供电方式是否可控]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592444323}

[[Power pairs]{lang="EN-US"}]{#struct_0_x1289_x1771_x797671118}

[[PoE]{lang="EN-US"}]{#struct_0_x1289_x1771_592509859}[端口的远程供电模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Signal]{lang="EN-US"}]{#struct_0_x1289_x1771_592313251}[：表示信号线供电模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spare]{lang="EN-US"}]{#struct_0_x1289_x1771_103812084}[：表示空闲线供电模式]{lang="EN-US" style="font-family:宋体"}

[[Port power classification]{lang="EN-US"}]{#struct_0_x1289_x1771_592378787}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_566865639}[的端口控制级别：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 0]{lang="EN-US"}]{#struct_0_x1289_x1771_592706467}[：表示级别]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 1]{lang="EN-US"}]{#struct_0_x1289_x1771_592772003}[：表示级别]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 2]{lang="EN-US"}]{#struct_0_x1289_x1771_1052713862}[：表示级别]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 3]{lang="EN-US"}]{#struct_0_x1289_x1771_592182176}[：表示级别]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 4]{lang="EN-US"}]{#struct_0_x1289_x1771_592247712}[：表示级别]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}

[[Power type]{lang="EN-US"}]{#struct_0_x1289_x1771_2065952382}

[[供电类型：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x876925136}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 1 PD]{lang="EN-US"}]{#struct_0_x1289_x1771_2065886846}[：表示类型]{lang="EN-US" style="font-family:宋体"}[1 PD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 2 PD]{lang="EN-US"}]{#struct_0_x1289_x1771_1869021673}[：表示类型]{lang="EN-US" style="font-family:宋体"}[2 PD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 1 PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_2065821310}[：表示类型]{lang="EN-US" style="font-family:宋体"}[1 PSE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 2 PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_695384799}[：表示类型]{lang="EN-US" style="font-family:宋体"}[2 PSE]{lang="EN-US"}

[[Power source]{lang="EN-US"}]{#struct_0_x1289_x1771_30464080}

[[功率来源（功率来源根据供电类型为]{style="font-family:宋体"}[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_2065755774}[类型或]{style="font-family:宋体"}[PSE]{lang="EN-US"}[类型，取值不同）：]{style="font-family:宋体"}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x515404232}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_2065690238}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_x1289_x1771_290670476}[：表示采用主用电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x1289_x1771_2065624702}[：表示采用备用电源作为电源]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reserved]{lang="EN-US"}]{#struct_0_x1289_x1771_1056905721}[：保留]{lang="EN-US" style="font-family:宋体"}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_2065559166}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x49146061}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x864868828}[：表示采用]{style="font-family:宋体"}[PSE]{lang="EN-US"}[作为电源]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_x1289_x1771_2065493630}[：表示采用本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE and local]{lang="EN-US"}]{#struct_0_x1289_x1771_651535779}[：表示采用]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[和本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[Power priority]{lang="EN-US"}]{#struct_0_x1289_x1771_2066476670}

[[功率优先级：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x263650448}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_2066411134}[：表示优先级未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x1289_x1771_181189741}[：表示优先级为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x1289_x1771_2065952385}[：表示优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low]{lang="EN-US"}]{#struct_0_x1289_x1771_x876728528}[：表示优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[级]{style="font-family:宋体"}

[[PD requested power value]{lang="EN-US"}]{#struct_0_x1289_x1771_x341353012}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_2065886849}[请求功率值，单位为瓦特]{style="font-family:宋体"}

[[PSE allocated power value]{lang="EN-US"}]{#struct_0_x1289_x1771_1869349353}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_2065821313}[分配功率值，单位为瓦特]{style="font-family:宋体"}

[[Link aggregation supported]{lang="EN-US"}]{#struct_0_x1289_x1771_x667898169}

[[端口是否支持链路聚合]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592051104}

[[Link aggregation enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_592116640}

[[端口是否已开启链路聚合]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1686750841}

[[Aggregation port ID]{lang="EN-US"}]{#struct_0_x1289_x1771_592444320}

[[聚合组中该成员端口的编号，未开启链路聚合功能时为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1289_x1771_x797671119}

[[Congestion notification TLV info]{lang="EN-US"}]{#struct_0_x1289_x1771_x393804802}

[[拥塞通知]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x393935874}[信息。本字段的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Dot1p]{lang="EN-US"}]{#struct_0_x1289_x1771_x394001410}

[[802.1p]{lang="EN-US"}]{#struct_0_x1289_x1771_1531556005}[优先级]{style="font-family:宋体"}

[[CNPV]{lang="EN-US"}]{#struct_0_x1289_x1771_x395367615}

[[802.1p]{lang="EN-US"}]{#struct_0_x1289_x1771_x393542658}[优先级是否被配置为]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[（]{style="font-family:宋体"}[Congestion Notification Priority Value]{lang="EN-US"}[，拥塞通知优先级值），表明是否加入了对应]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[域：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x1289_x1771_x1055310635}[：表示]{lang="EN-US" style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级被配置为]{lang="EN-US" style="font-family:宋体"}[CNPV]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x1289_x1771_x393608194}[：表示]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级未被配置为]{style="font-family:宋体"}[CNPV]{lang="EN-US"}

[[Ready]{lang="EN-US"}]{#struct_0_x1289_x1771_1317372310}

[[表明设备接口是否已经关闭了]{style="font-family:宋体"}[802.1p]{lang="EN-US"}]{#struct_0_x1289_x1771_x393673730}[优先级与隔离优先级的映射：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x1289_x1771_x1838036845}[：表示关闭优先级映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x1289_x1771_60068155}[：表示未关闭优先级映射]{style="font-family:宋体"}

[[Maximum frame size]{lang="EN-US"}]{#struct_0_x1289_x1771_592509856}

[[端口支持的最大帧长度]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592313248}

[[Media policy type]{lang="EN-US"}]{#struct_0_x1289_x1771_592378784}

[[媒体策略类型：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_566865636}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_592706464}[：表示类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Voice]{lang="EN-US"}]{#struct_0_x1289_x1771_592772000}[：表示语音]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VoiceSignaling]{lang="EN-US"}]{#struct_0_x1289_x1771_1052713859}[：表示语音信号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GuestVoice]{lang="EN-US"}]{#struct_0_x1289_x1771_592182177}[：表示访客语音]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GuestVoiceSignaling]{lang="EN-US"}]{#struct_0_x1289_x1771_592247713}[：表示访客语音信号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SoftPhoneVoice]{lang="EN-US"}]{#struct_0_x1289_x1771_x667898170}[：表示软体电话语音]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Videoconferencing]{lang="EN-US"}]{#struct_0_x1289_x1771_592051105}[：表示视频会议]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StreamingVideo]{lang="EN-US"}]{#struct_0_x1289_x1771_592116641}[：表示流视频]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VideoSignaling]{lang="EN-US"}]{#struct_0_x1289_x1771_x1686750840}[：表示视频信号]{lang="EN-US" style="font-family:宋体"}

[[Unknown policy]{lang="EN-US"}]{#struct_0_x1289_x1771_592444321}

[[媒体策略类型是否未知：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_592509857}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x1289_x1771_x422000719}[：表示策略类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x1289_x1771_592313249}[：表示策略类型已知]{style="font-family:宋体"}

[[VLAN tagged]{lang="EN-US"}]{#struct_0_x1289_x1771_592378785}

[[媒体]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_592706465}[是否带]{style="font-family:宋体"}[Tag]{lang="EN-US"}

[[Media policy VLANID]{lang="EN-US"}]{#struct_0_x1289_x1771_1866420331}

[[媒体]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_592772001}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Media policy L2 priority]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136701175}

[[二层优先级]{style="font-family:宋体"}]{#struct_0_x1289_x1771_647645598}

[[Media policy DSCP]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136635639}

[[DSCP]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136832247}[的值]{style="font-family:宋体"}

[[Location format]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136766711}

[[位置信息格式：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x2006111230}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136439031}[：表示无效位置数据类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Coordinate-based LCI]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136373495}[：表示基于坐标的位置信息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Civic Address LCI]{lang="EN-US"}]{#struct_0_x1289_x1771_x1825927384}[：表示普通地址信息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ECS ELIN]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136570103}[：表示紧急电话号码]{style="font-family:宋体"}

[[Location information]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136504567}

[[位置信息]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x2136176887}

[[PoE PSE power source]{lang="EN-US"}]{#struct_0_x1289_x1771_632399350}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136111351}[所采用的电源类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136701174}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136635638}[：表示采用主用电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136832246}[：表示采用备用电源作为电源]{style="font-family:宋体"}

[[PoE PD power source]{lang="EN-US"}]{#struct_0_x1289_x1771_508272499}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136766710}[所采用的电源类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136439030}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136373494}[：表示采用]{style="font-family:宋体"}[PSE]{lang="EN-US"}[作为电源]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_x1289_x1771_902955971}[：表示采用本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE and local]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136570102}[：表示采用]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[和本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[Port PSE priority]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136504566}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136176886}[上端口的供电优先级：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136111350}[：表示优先级未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x1289_x1771_x1055406542}[：表示优先级为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136701177}[：表示优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136635641}[：表示优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[级]{style="font-family:宋体"}

[[Port PD priority]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136832249}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136766713}[上端口的受电优先级：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136439033}[：表示优先级未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136373497}[：表示优先级为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136570105}[：表示优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low]{lang="EN-US"}]{#struct_0_x1289_x1771_2054852387}[：表示优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[级]{style="font-family:宋体"}

[[Port available power value]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136504569}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136176889}[上端口可提供的功率，或]{style="font-family:宋体"}[PD]{lang="EN-US"}[上端口所需的功率，单位为瓦特]{style="font-family:宋体"}

[[Transmit Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_1869498170}

[[本端发送的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1869563706}

[[Receive Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_1870153530}

[[本端向对端请求的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_412592514}

[[Fallback Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_1870219066}

[[本端向对端请求的候选等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1869629245}

[[Echo Transmit Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_1869694781}

[[收到的对端发送的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1869760317}

[[Echo Receive Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_1869825853}

[[收到的对端请求的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x721905202}

[ ]{lang="EN-US"}

::: {#2060811889 .myid}
[]{#_Toc404784693}[]{#struct_0_x1289_x1771_182060656}

**LLDP \-- LLDP配置命令 \-- display lldp neighbor-information**

------------------------------------------------------------------------

[**[display lldp neighbor-information]{lang="EN-US"}**]{#struct_0_x1289_x1771_82004578}[命令用来显示由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息，这些信息是由邻居设备组织成]{style="font-family:宋体"}[TLV]{lang="EN-US"}[并发送给本设备的。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1409905347}

[**[display lldp neighbor-information]{lang="EN-US"}**[ \[ \[ \[ **interface** *interface-type interface-number* \] \[ **agent** { **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } \] \[ **verbose** \] \] \| **list** \[ **system-name** *system-name* \] \]]{lang="EN-US"}]{#struct_0_x1289_x1771_157247950}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2136111353}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1673476813}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1789661147}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x591455351}

[[network-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_1244103674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1231408927}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_1900984689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_935654711}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1289_x1771_1066537562}[：显示指定接口收到的由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定该参数，将显示所有接口收到的由邻居设备发来的]{style="font-family:
宋体"}[LLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_x2136701176}[：显示指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理收到的由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息。如果未指定该参数，将显示所有类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理收到的由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[nearest-bridge]{lang="EN-US"}**]{#struct_0_x1289_x1771_1050930125}[：表示最近桥代理。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1768479768}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1302419317}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1289_x1771_970630087}[：显示由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[详细信息。如果未指定该参数，将显示由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[概要信息。]{style="font-family:宋体"}

[**[list]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1912585707}[：按列表显示由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[system-name]{lang="EN-US"}**[ *system-name*]{lang="EN-US"}]{#struct_0_x1289_x1771_x803496370}[：按列表显示由指定邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[system-name]{lang="EN-US"}*[表示邻居设备的系统名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。如果未指定该参数，将按列表显示由所有邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x532751715}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x521376231}[显示所有接口最近桥代理收到的由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[详细信息（假设]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[的版本为标准版）。]{style="font-family:宋体"}

[[\<Sysname\> display lldp neighbor-information agent nearest-bridge verbose]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136373496}

[LLDP neighbor-information of port 1\[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent nearest-bridge:]{lang="EN-US"}

[ LLDP Neighbor index : 1]{lang="EN-US"}

[ Update time         : 0 days, 0 hours, 1 minutes, 1 seconds ]{lang="EN-US"}

[ LLDP mac type       : Nearest Bridge]{lang="EN-US"}

[ Chassis type        : MAC address]{lang="EN-US"}

[ Chassis ID          : 000f-0055-0002]{lang="EN-US"}

[ Port ID type        : Interface name]{lang="EN-US"}

[ Port ID             : GigabitEthernet1/0/1]{lang="EN-US"}

[ Time to live        : 121]{lang="EN-US"}

[ Port description    : GigabitEthernet1/0/1 Interface]{lang="EN-US"}

[ System name         : Sysname]{lang="EN-US"}

[ System description  : H3C Comware Platform Software]{lang="EN-US"}

[ System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge]{lang="EN-US"}

[ System capabilities enabled   : Bridge, Router, Customer Bridge]{lang="EN-US"}

[ Management address type           : IPv4]{lang="EN-US"}

[ Management address                : 192.168.1.55]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ DCBX Control info:]{lang="EN-US"}

[ Oper version       : Standard]{lang="EN-US"}

[ DCBX ETS configuration info:]{lang="EN-US"}

[  CBS                : False]{lang="EN-US"}

[  Max TCs            : 8]{lang="EN-US"}

[  CoS     Local priority      Percentage        TSA]{lang="EN-US"}

[   0            0                 15            ETS]{lang="EN-US"}

[   1            1                 0             SP]{lang="EN-US"}

[   2            2                 15            ETS]{lang="EN-US"}

[   3            3                 14            ETS]{lang="EN-US"}

[   4            4                 14            ETS]{lang="EN-US"}

[   5            5                 14            ETS]{lang="EN-US"}

[   6            6                 14            ETS]{lang="EN-US"}

[   7            7                 14            ETS]{lang="EN-US"}

[ DCBX ETS recommendation info:]{lang="EN-US"}

[  CoS     Local priority      Percentage        TSA]{lang="EN-US"}

[   0            0                 15            ETS]{lang="EN-US"}

[   1            1                 0             SP]{lang="EN-US"}

[   2            2                 15            ETS]{lang="EN-US"}

[   3            3                 14            ETS]{lang="EN-US"}

[   4            4                 14            ETS]{lang="EN-US"}

[   5            5                 14            ETS]{lang="EN-US"}

[   6            6                 14            ETS]{lang="EN-US"}

[   7            7                 14            ETS]{lang="EN-US"}

[ DCBX PFC info:]{lang="EN-US"}

[  P0-0     P1-1     P2-1     P3-1     P4-0     P5-0     P6-0     P7-0]{lang="EN-US"}

[  Number of traffic classes supported: 8]{lang="EN-US"}

[  Value of MBC: 0]{lang="EN-US"}

[ DCBX APP info:]{lang="EN-US"}

[  Selected Field              Protocol ID Priority]{lang="EN-US"}

[  UDP/ DCCP                   100         0x3]{lang="EN-US"}

[  TCP/SCTP                    200         0x3]{lang="EN-US"}

[  Ethertype                   0x1234      0x3]{lang="EN-US"}

[  Ethertype                   0x8906      0x3 ]{lang="EN-US"}

[ Port VLAN ID(PVID): 1]{lang="EN-US"}

[ Port and protocol VLAN ID(PPVID) : 12]{lang="EN-US"}

[ Port and protocol VLAN supported : Yes]{lang="EN-US"}

[ Port and protocol VLAN enabled   : Yes]{lang="EN-US"}

[ VLAN name of VLAN 12: VLAN 0012]{lang="EN-US"}

[ Management VLAN ID  : 5]{lang="EN-US"}

[ Auto-negotiation supported : Yes]{lang="EN-US"}

[ Auto-negotiation enabled   : Yes]{lang="EN-US"}

[ OperMau                    : Speed(1000)/Duplex(Full)]{lang="EN-US"}

[ Power port class           : PD]{lang="EN-US"}

[ PSE power supported        : Yes]{lang="EN-US"}

[ PSE power enabled          : Yes]{lang="EN-US"}

[ PSE pairs control ability  : Yes]{lang="EN-US"}

[ Power pairs                : Signal]{lang="EN-US"}

[ Port power classification  : Class 0]{lang="EN-US"}

[ Power type                 : Type 2 PD]{lang="EN-US"}

[ Power source               : PSE and local]{lang="EN-US"}

[ Power priority             : High]{lang="EN-US"}

[ PD requested power value   : 21.1 w]{lang="EN-US"}

[ PSE allocated power value  : 15.3 w]{lang="EN-US"}

[ Link aggregation supported : Yes]{lang="EN-US"}

[ Link aggregation enabled   : Yes]{lang="EN-US"}

[ Aggregation port ID        : 52]{lang="EN-US"}

[ Congestion notification TLV info:]{lang="EN-US"}

[  Dot1p          CNPV         Ready]{lang="EN-US"}

[  0              Yes          Yes]{lang="EN-US"}

[  1              No           No]{lang="EN-US"}

[  2              No           No]{lang="EN-US"}

[  3              No           No]{lang="EN-US"}

[  4              Yes          No]{lang="EN-US"}

[  5              Yes          Yes]{lang="EN-US"}

[  6              No           No]{lang="EN-US"}

[  7              No           No]{lang="EN-US"}

[ Maximum frame size         : 1500]{lang="EN-US"}

[ Transmit Tw                : 100 us]{lang="EN-US"}

[ Receive Tw                 : 90 us]{lang="EN-US"}

[ Fallback Tw                : 90 us]{lang="EN-US"}

[ Echo Transmit Tw           : 0 us]{lang="EN-US"}

[ Echo Receive Tw            : 0 us]{lang="EN-US"}

[ MED information]{lang="EN-US"}[：]{style="font-family:宋体"}

[ Device class               : Connectivity device]{lang="EN-US"}

[ Media policy type          : Unknown]{lang="EN-US"}

[ Unknown policy             : No]{lang="EN-US"}

[ VLAN tagged                : No]{lang="EN-US"}

[ Media policy VLAN ID       : 1000]{lang="EN-US"}

[ Media policy L2 priority   : 6]{lang="EN-US"}

[ Media policy DSCP          : 10]{lang="EN-US"}

[ Location format       : Civic Address LCI]{lang="EN-US"}

[ Location information  :]{lang="EN-US"}

[  What(1)  Country(CN)]{lang="EN-US"}

[  CA type  CA value]{lang="EN-US"}

[  0        Chinese]{lang="EN-US"}

[  1        Zhejiang]{lang="EN-US"}

[  2        Hangzhou]{lang="EN-US"}

[ MED port information:]{lang="EN-US"}

[  Media policy type          : Unknown]{lang="EN-US"}

[  Unknown policy             : No]{lang="EN-US"}

[  VLAN tagged                : No]{lang="EN-US"}

[  Media policy VLANID        : 1000]{lang="EN-US"}

[  Media policy L2 priority   : 6]{lang="EN-US"}

[  Media policy DSCP          : 10]{lang="EN-US"}

[ PoE PSE power source       : Primary]{lang="EN-US"}

[ Port PSE priority          : Low]{lang="EN-US"}

[ Port available power value : 2.2 w]{lang="EN-US"}

[ Unknown basic TLV:]{lang="EN-US"}

[  TLV type           : 23]{lang="EN-US"}

[  TLV information    : 0x00140014]{lang="EN-US"}

[ Unknown organizationally-defined TLV:]{lang="EN-US"}

[  TLV OUI            : 00-12-bb]{lang="EN-US"}

[  TLV subtype        : 21]{lang="EN-US"}

[  Index              : 1]{lang="EN-US"}

[  TLV information    : 0x556e6b6e 6f776e]{lang="EN-US"}

[ ]{lang="EN-US"}

[CDP neighbor-information of port 1\[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent nearest-bridge:]{lang="EN-US"}

[ CDP neighbor index  : 4]{lang="EN-US"}

[ Chassis ID          : SEP00260B5C0548]{lang="EN-US"}

[ Port ID             : Port 1]{lang="EN-US"}

[ Software version    : SCCP41.8-4-1S]{lang="EN-US"}

[ Platform version    : Cisco IP Phone 7941]{lang="EN-US"}

[ Duplex              : Full]{lang="EN-US"}

[ Time to live        : 180]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x259843443}[显示所有接口所有类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理收到的由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[详细信息（假设]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[的版本为标准版）。]{style="font-family:宋体"}

[[\<Sysname\> display lldp neighbor-information verbose]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136766715}

[LLDP neighbor-information of port 1\[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent nearest-bridge:]{lang="EN-US"}

[ LLDP Neighbor index : 1]{lang="EN-US"}

[ Update time         : 0 days, 0 hours, 1 minutes, 1 seconds]{lang="EN-US"}

[ LLDP mac type       : Nearest Bridge]{lang="EN-US"}

[ Chassis type        : MAC address]{lang="EN-US"}

[ Chassis ID          : 000f-0055-0002]{lang="EN-US"}

[ Port ID type        : Interface name]{lang="EN-US"}

[ Port ID             : GigabitEthernet1/0/1]{lang="EN-US"}

[ Time to live        : 121]{lang="EN-US"}

[ Port description    : GigabitEthernet1/0/1 Interface]{lang="EN-US"}

[ System name         : Sysname]{lang="EN-US"}

[ System description  : H3C Comware Platform Software]{lang="EN-US"}

[ System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge]{lang="EN-US"}

[ System capabilities enabled   : Bridge, Router, Customer Bridge]{lang="EN-US"}

[ Management address type           : IPv4]{lang="EN-US"}

[ Management address                : 192.168.1.55]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ DCBX control info:]{lang="EN-US"}

[  Oper version       : Standard]{lang="EN-US"}

[ DCBX ETS configuration info:]{lang="EN-US"}

[  CBS                : False]{lang="EN-US"}

[  Max TCs            : 8]{lang="EN-US"}

[  CoS     Local Priority      Percentage        TSA]{lang="EN-US"}

[   0            0                 15            ETS]{lang="EN-US"}

[   1            1                 0             SP]{lang="EN-US"}

[   2            2                 15            ETS]{lang="EN-US"}

[   3            3                 14            ETS]{lang="EN-US"}

[   4            4                 14            ETS]{lang="EN-US"}

[   5            5                 14            ETS]{lang="EN-US"}

[   6            6                 14            ETS]{lang="EN-US"}

[   7            7                 14            ETS]{lang="EN-US"}

[ DCBX ETS recommendation info:]{lang="EN-US"}

[  CoS     Local Priority      Percentage        TSA]{lang="EN-US"}

[   0            0                 15            ETS]{lang="EN-US"}

[   1            1                 0             SP]{lang="EN-US"}

[   2            2                 15            ETS]{lang="EN-US"}

[   3            3                 14            ETS]{lang="EN-US"}

[   4            4                 14            ETS]{lang="EN-US"}

[   5            5                 14            ETS]{lang="EN-US"}

[   6            6                 14            ETS]{lang="EN-US"}

[   7            7                 14            ETS]{lang="EN-US"}

[ DCBX PFC info:]{lang="EN-US"}

[  P0-0     P1-1     P2-1     P3-1     P4-0     P5-0     P6-0     P7-0]{lang="EN-US"}

[  Number of traffic classes supported: 8]{lang="EN-US"}

[  Value of MBC: 0]{lang="EN-US"}

[ DCBX APP info:]{lang="EN-US"}

[  Selected Field  Protocol ID  Priority]{lang="EN-US"}

[  UDP/DCCP        100          0x3]{lang="EN-US"}

[  TCP/SCTP        200          0x3]{lang="EN-US"}

[  Ethertype       0x1234       0x3]{lang="EN-US"}

[  Ethertype       0x8906       0x3]{lang="EN-US"}

[ Port VLAN ID(PVID): 1]{lang="EN-US"}

[ Port and protocol VLAN ID(PPVID) : 12]{lang="EN-US"}

[ Port and protocol VLAN supported : Yes]{lang="EN-US"}

[ Port and protocol VLAN enabled   : Yes]{lang="EN-US"}

[ VLAN name of VLAN 12: VLAN 0012]{lang="EN-US"}

[ Management VLAN ID  : 5]{lang="EN-US"}

[ Auto-negotiation supported : Yes]{lang="EN-US"}

[ Auto-negotiation enabled   : Yes]{lang="EN-US"}

[ OperMau                    : Speed(1000)/Duplex(Full)]{lang="EN-US"}

[ Power port class           : PD]{lang="EN-US"}

[ PSE power supported        : Yes]{lang="EN-US"}

[ PSE power enabled          : Yes]{lang="EN-US"}

[ PSE pairs control ability  : Yes]{lang="EN-US"}

[ Power pairs                : Signal]{lang="EN-US"}

[ Port power classification  : Class 0]{lang="EN-US"}

[ Power type                 : Type 2 PD]{lang="EN-US"}

[ Power source               : PSE and local]{lang="EN-US"}

[ Power priority             : High]{lang="EN-US"}

[ PD requested power value   : 21.1 w]{lang="EN-US"}

[ PSE allocated power value  : 15.3 w]{lang="EN-US"}

[ Link aggregation supported : Yes]{lang="EN-US"}

[ Link aggregation enabled   : Yes]{lang="EN-US"}

[ Aggregation port ID        : 52]{lang="EN-US"}

[ Maximum frame size         : 1500]{lang="EN-US"}

[ Transmit Tw                : 100 us]{lang="EN-US"}

[ Receive Tw                 : 90 us]{lang="EN-US"}

[ Fallback Tw                : 90 us]{lang="EN-US"}

[ Echo Transmit Tw           : 0 us]{lang="EN-US"}

[ Echo Receive Tw            : 0 us]{lang="EN-US"}

[ Device class               : Connectivity device]{lang="EN-US"}

[ HardwareRev               : Unknown]{lang="EN-US"}

[ FirmwareRev               : Unknown]{lang="EN-US"}

[ SoftwareRev               : Unknown]{lang="EN-US"}

[ SerialNum                 : Unknown]{lang="EN-US"}

[ Manufacturer name         : Unknown]{lang="EN-US"}

[ Model name                : Unknown]{lang="EN-US"}

[ Asset tracking identifier : Unknown]{lang="EN-US"}

[ Location format       : Civic Address LCI]{lang="EN-US"}

[ Location information  :]{lang="EN-US"}

[  What(1)  Country(CN)]{lang="EN-US"}

[  CA type  CA value]{lang="EN-US"}

[  0        Chinese]{lang="EN-US"}

[  1        Zhejiang]{lang="EN-US"}

[  2        Hangzhou]{lang="EN-US"}

[ MED port information:]{lang="EN-US"}

[  Media policy type          : Unknown]{lang="EN-US"}

[  Unknown policy             : No]{lang="EN-US"}

[  VLAN tagged                : No]{lang="EN-US"}

[  Media policy VLANID        : 1000]{lang="EN-US"}

[  Media policy L2 priority   : 6]{lang="EN-US"}

[  Media policy DSCP          : 10]{lang="EN-US"}

[ PoE PSE power source       : Primary]{lang="EN-US"}

[ Port PSE priority          : Low]{lang="EN-US"}

[ Port available power value : 2.2 w]{lang="EN-US"}

[ Unknown basic TLV:]{lang="EN-US"}

[  TLV type           : 23]{lang="EN-US"}

[  TLV information    : 0x00140014]{lang="EN-US"}

[ Unknown organizationally-defined TLV:]{lang="EN-US"}

[  TLV OUI            : 00-12-bb]{lang="EN-US"}

[  TLV subtype        : 21]{lang="EN-US"}

[  Index              : 1]{lang="EN-US"}

[  TLV information    : 0x556e6b6e 6f776e]{lang="EN-US"}

[ ]{lang="EN-US"}

[CDP neighbor-information of port 1\[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[ LLDP agent nearest-bridge:]{lang="EN-US"}

[ CDP neighbor index  : 4]{lang="EN-US"}

[ Chassis ID          : SEP00260B5C0548]{lang="EN-US"}

[ Port ID             : Port 1]{lang="EN-US"}

[ Software version    : SCCP41.8-4-1S]{lang="EN-US"}

[ Platform version    : Cisco IP Phone 7941]{lang="EN-US"}

[ Duplex              : Full]{lang="EN-US"}

[ Time to live        : 180]{lang="EN-US"}

[LLDP neighbor-information of port 1\[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent nearest-nontpmr:]{lang="EN-US"}

[ LLDP Neighbor index : 1]{lang="EN-US"}

[ Update time         : 0 days, 0 hours, 1 minutes, 1 seconds]{lang="EN-US"}

[ Chassis type        : MAC address]{lang="EN-US"}

[ Chassis ID          : 000f-0055-0002]{lang="EN-US"}

[ Port ID type        : Interface name]{lang="EN-US"}

[ Port ID             : GigabitEthernet1/0/1]{lang="EN-US"}

[ Time to live        : 121]{lang="EN-US"}

[ Port description    : GigabitEthernet1/0/1 Interface]{lang="EN-US"}

[ System name         : Sysname]{lang="EN-US"}

[ System description  : H3C Comware Platform Software]{lang="EN-US"}

[ System capabilities supported : Bridge, Router, Customer Bridge, Service Bridge]{lang="EN-US"}

[ System capabilities enabled   : Bridge, Router, Customer Bridge]{lang="EN-US"}

[ Management address type           : IPv4]{lang="EN-US"}

[ Management address                : 192.168.1.55]{lang="EN-US"}

[ Management address interface type : IfIndex]{lang="EN-US"}

[ Management address interface ID   : Unknown]{lang="EN-US"}

[ Management address OID            : 0]{lang="EN-US"}

[ Port VLAN ID(PVID): 1]{lang="EN-US"}

[ Port and protocol VLAN ID(PPVID) : 12]{lang="EN-US"}

[ Port and protocol VLAN supported : Yes]{lang="EN-US"}

[ Port and protocol VLAN enabled   : Yes]{lang="EN-US"}

[ VLAN name of VLAN 12: VLAN 0012 ]{lang="EN-US"}

[ Auto-negotiation supported : Yes]{lang="EN-US"}

[ Auto-negotiation enabled   : Yes]{lang="EN-US"}

[ OperMau                    : Speed(1000)/Duplex(Full)]{lang="EN-US"}

[ Power port class           : PD]{lang="EN-US"}

[ PSE power supported        : Yes]{lang="EN-US"}

[ PSE power enabled          : Yes]{lang="EN-US"}

[ PSE pairs control ability  : Yes]{lang="EN-US"}

[ Power pairs                : Signal]{lang="EN-US"}

[ Port power classification  : Class 0]{lang="EN-US"}

[ Power type                 : Type 2 PD]{lang="EN-US"}

[ Power source               : PSE and local]{lang="EN-US"}

[ Power priority             : High]{lang="EN-US"}

[ PD requested power value   : 21.1 w]{lang="EN-US"}

[ PSE allocated power value  : 15.3 w]{lang="EN-US"}

[ Link aggregation supported : Yes]{lang="EN-US"}

[ Link aggregation enabled   : Yes]{lang="EN-US"}

[ Aggregation port ID        : 52]{lang="EN-US"}

[ Congestion notification TLV info:]{lang="EN-US"}

[  Dot1p          CNPV         Ready]{lang="EN-US"}

[  0              Yes          Yes]{lang="EN-US"}

[  1              No           No]{lang="EN-US"}

[  2              No           No]{lang="EN-US"}

[  3              No           No]{lang="EN-US"}

[  4              Yes          No]{lang="EN-US"}

[  5              Yes          Yes]{lang="EN-US"}

[  6              No           No]{lang="EN-US"}

[  7              No           No]{lang="EN-US"}

[ Maximum frame size         : 1500]{lang="EN-US"}

[ Transmit Tw                : 100 us]{lang="EN-US"}

[ Receive Tw                 : 90 us]{lang="EN-US"}

[ Fallback Tw                : 90 us]{lang="EN-US"}

[ Echo Transmit Tw           : 0 us]{lang="EN-US"}

[ Echo Receive Tw            : 0 us]{lang="EN-US"}

[ Device class              : Connectivity device]{lang="EN-US"}

[ HardwareRev               : Unknown]{lang="EN-US"}

[ FirmwareRev               : Unknown]{lang="EN-US"}

[ SoftwareRev               : Unknown]{lang="EN-US"}

[ SerialNum                 : Unknown]{lang="EN-US"}

[ Manufacturer name         : Unknown]{lang="EN-US"}

[ Model name                : Unknown]{lang="EN-US"}

[ Asset tracking identifier : Unknown]{lang="EN-US"}

[ Location format       : Civic Address LCI]{lang="EN-US"}

[ Location information  :]{lang="EN-US"}

[  What(1)  Country(CN)]{lang="EN-US"}

[  CA type  CA value]{lang="EN-US"}

[  0        Chinese]{lang="EN-US"}

[  1        Zhejiang]{lang="EN-US"}

[  2        Hangzhou]{lang="EN-US"}

[ MED port information:]{lang="EN-US"}

[  Media policy type          : Unknown]{lang="EN-US"}

[  Unknown policy             : No]{lang="EN-US"}

[  VLAN tagged                : No]{lang="EN-US"}

[  Media policy VLANID        : 1000]{lang="EN-US"}

[  Media policy L2 priority   : 6]{lang="EN-US"}

[  Media policy DSCP          : 10]{lang="EN-US"}

[PoE PSE power source      : Primary]{lang="EN-US"}

[Port PSE priority         : Low]{lang="EN-US"}

[Port available power value: 2.2 w]{lang="EN-US"}

[Unknown basic TLV:]{lang="EN-US"}

[  TLV type           : 23]{lang="EN-US"}

[  TLV information    : 0x00140014]{lang="EN-US"}

[ Unknown organizationally-defined TLV:]{lang="EN-US"}

[  TLV OUI            : 00-12-bb]{lang="EN-US"}

[  TLV subtype        : 21]{lang="EN-US"}

[  Index              : 1]{lang="EN-US"}

[  TLV information    : 0x556e6b6e 6f776e]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_319487598}[显示所有接口所有类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理收到的由邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display lldp neighbor-information]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136439035}

[LLDP neighbor-information of port 52\[GigabitEthernet1/0/3\]:]{lang="EN-US"}

[LLDP agent nearest-bridge:]{lang="EN-US"}

[ LLDP neighbor index : 3]{lang="EN-US"}

[ LLDP mac type       : Nearest Bridge]{lang="EN-US"}

[ ChassisID/subtype   : 0011-2233-4400/MAC address]{lang="EN-US"}

[ PortID/subtype      : 000c-29f5-c71f/MAC address]{lang="EN-US"}

[ Capabilities        : Bridge, Router, Customer Bridge]{lang="EN-US"}

[ ]{lang="EN-US"}

[ LLDP neighbor index : 6]{lang="EN-US"}

[ LLDP mac type       : Nearest Bridge]{lang="EN-US"}

[ ChassisID/subtype   : 0011-2233-4400/MAC address]{lang="EN-US"}

[ PortID/subtype      : 000c-29f5-c715/MAC address]{lang="EN-US"}

[ Capabilities        : None]{lang="EN-US"}

[ ]{lang="EN-US"}

[CDP neighbor-information of port 52\[GigabitEthernet1/0/3\]:]{lang="EN-US"}

[LLDP agent nearest-bridge]{lang="EN-US"}[：]{style="font-family:宋体"}

[ CDP neighbor index  : 4]{lang="EN-US"}

[ Chassis ID          : SEP00260B5C0548]{lang="EN-US"}

[ Port ID             : Port 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ CDP neighbor index  : 5]{lang="EN-US"}

[ Chassis ID          : 0011-2233-4400]{lang="EN-US"}

[ Port ID             : GigabitEthernet1/0/4]{lang="EN-US"}

[ ]{lang="EN-US"}

[LLDP neighbor-information of port 52\[GigabitEthernet1/0/3\]:]{lang="EN-US"}

[LLDP agent nearest-nontpmr:]{lang="EN-US"}

[ LLDP neighbor index : 6]{lang="EN-US"}

[ ChassisID/subtype   : 0011-2233-4400/MAC address]{lang="EN-US"}

[ PortID/subtype      : 000c-29f5-c715/MAC address]{lang="EN-US"}

[ Capabilities        : None]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136373499}[按列表显示类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理所有邻居设备发来的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display lldp neighbor-information list]{lang="EN-US"}]{#struct_0_x1289_x1771_855901804}

[Chassis ID : \* \-- \--Nearest nontpmr bridge neighbor]{lang="EN-US"}

[             \# \-- \--Nearest customer bridge neighbor]{lang="EN-US"}

[             Default \-- \-- Nearest bridge neighbor]{lang="EN-US"}

[System Name          Local Interface   Chassis ID       Port ID]{lang="EN-US"}

[System1              GE1/0/1           000f-e25d-ee91   GigabitEthernet1/0/5]{lang="EN-US"}

[System2              GE1/0/2           000f-e25d-ee92\*  GigabitEthernet1/0/6]{lang="EN-US"}

[System3              GE1/0/3           000f-e25d-ee93#  GigabitEthernet1/0/7]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display lldp neighbor-information]{lang="EN-US"}]{#struct_0_x1289_x1771_x2060000395}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x149285769}[[字段]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x736906118}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2136570107}

[[LLDP agent nearest-bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_892052973}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x552835432}[缺省代理，即最近桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-customer]{lang="EN-US"}]{#struct_0_x1289_x1771_x1559974904}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1770367462}[最近客户桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-nontpmr]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136504571}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1996284914}[最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理]{style="font-family:宋体"}

[[LLDP neighbor-information of port 1]{lang="EN-US"}]{#struct_0_x1289_x1771_813175771}

[[端口]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1289_x1771_x1281240881}[上收到的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}

[[LLDP Neighbor index]{lang="EN-US"}]{#struct_0_x1289_x1771_29038647}

[[邻居索引]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x2136176891}

[[Update time]{lang="EN-US"}]{#struct_0_x1289_x1771_x174104168}

[[邻居信息最新更新时间]{style="font-family:宋体"}]{#struct_0_x1289_x1771_606065762}

[[LLDP mac type ]{lang="EN-US"}]{#struct_0_x1289_x1771_x626760356}

[[邻居]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1289_x1771_x2013527683}[地址类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nearest brige]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136111355}[：最近桥代理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nearest customer bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x1814921429}[：最近客户桥代理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nearest non-tpmr bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x306252842}[：最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理]{style="font-family:宋体"}

[[Chassis type]{lang="EN-US"}]{#struct_0_x1289_x1771_1510344582}

[[Chassis ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136701178}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Chassis component]{lang="EN-US"}]{#struct_0_x1289_x1771_600591431}[：表示底架组件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface alias]{lang="EN-US"}]{#struct_0_x1289_x1771_1142413687}[：表示接口化名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port component]{lang="EN-US"}]{#struct_0_x1289_x1771_125619903}[：表示端口组件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC address]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136635642}[：表示]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Network address(ipv4)]{lang="EN-US"}]{#struct_0_x1289_x1771_1820642571}[：表示网络地址（括号里表示地址类型）]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface name]{lang="EN-US"}]{#struct_0_x1289_x1771_x1897128755}[：表示接口名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Locally assigned]{lang="EN-US"}]{#struct_0_x1289_x1771_190212920}[：表示]{lang="EN-US" style="font-family:
  宋体"}[邻居自定义]{style="font-family:宋体"}

[[Chassis ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136832250}

[[Chassis ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x654592451}[值，根据邻居设备的]{style="font-family:宋体"}[Chassis type]{lang="EN-US"}[取相应类型的值]{style="font-family:宋体"}

[[Port ID type]{lang="EN-US"}]{#struct_0_x1289_x1771_x114095818}

[[端口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x871485559}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface alias]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136766714}[：表示接口化名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port component]{lang="EN-US"}]{#struct_0_x1289_x1771_1885571539}[：表示端口组件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC address]{lang="EN-US"}]{#struct_0_x1289_x1771_678751081}[：表示]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Network Address(ipv4)]{lang="EN-US"}]{#struct_0_x1289_x1771_187193640}[：表示网络地址（括号里表示地址类型）]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface name]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136439034}[：表示接口名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Agent circuit ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x1678210901}[：表示代理巡回标识]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Locally assigned]{lang="EN-US"}]{#struct_0_x1289_x1771_994507259}[：表示]{lang="EN-US" style="font-family:
  宋体"}[邻居自定义]{style="font-family:宋体"}

[[Port ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136373498}

[[端口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x710182137}[值，根据邻居设备的]{style="font-family:宋体"}[Port ID type]{lang="EN-US"}[取相应类型的值]{style="font-family:宋体"}

[[Time to live]{lang="EN-US"}]{#struct_0_x1289_x1771_1313597668}

[[邻居信息在本地的存活时间]{style="font-family:宋体"}]{#struct_0_x1289_x1771_251951383}

[[Port description]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136570106}

[[端口描述]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x674030968}

[[System name]{lang="EN-US"}]{#struct_0_x1289_x1771_829948312}

[[系统名称]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x2136504570}

[[System description]{lang="EN-US"}]{#struct_0_x1289_x1771_x430200973}

[[系统描述]{style="font-family:宋体"}]{#struct_0_x1289_x1771_999809514}

[[System capabilities supported]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136176890}

[[系统所支持的功能：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1740188109}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Repeater]{lang="EN-US"}]{#struct_0_x1289_x1771_x1002460154}[：表示支持信号中继功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x2136111354}[：表示支持交换功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WlanAccessPoint]{lang="EN-US"}]{#struct_0_x1289_x1771_913961926}[：表示支持无线接入点功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x1289_x1771_456221368}[：表示支持路由功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Telephone]{lang="EN-US"}]{#struct_0_x1289_x1771_x214386874}[：表示支持电话功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DocsisCableDevice]{lang="EN-US"}]{#struct_0_x1289_x1771_767736697}[：表示支持电缆设备功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StationOnly]{lang="EN-US"}]{#struct_0_x1289_x1771_x535374138}[：表示支持只作站点功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Customer Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x214321338}[：表示支持客户桥功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_382557604}[：表示支持服务桥功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TPMR]{lang="EN-US"}]{#struct_0_x1289_x1771_x183221623}[：表示支持双端口]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[中继功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_x1289_x1771_x214517946}[：表示支持不在上述列表的其它功能]{lang="EN-US" style="font-family:宋体"}

[[System capabilities enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_392644381}

[[系统已开启的功能：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1676899918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Repeater]{lang="EN-US"}]{#struct_0_x1289_x1771_x214452410}[：表示信号中继功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_742517094}[：表示交换功能已开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WlanAccessPoint]{lang="EN-US"}]{#struct_0_x1289_x1771_636623415}[：表示无线接入点功能已开启]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x1289_x1771_x214124730}[：表示路由功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Telephone]{lang="EN-US"}]{#struct_0_x1289_x1771_1907270789}[：表示电话功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DocsisCableDevice]{lang="EN-US"}]{#struct_0_x1289_x1771_x214059194}[：表示电缆设备功能已开启]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StationOnly]{lang="EN-US"}]{#struct_0_x1289_x1771_1106379245}[：表示只作站点功能已开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Customer Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x790413956}[：表示支持客户桥功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x214255802}[：表示支持服务桥功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TPMR]{lang="EN-US"}]{#struct_0_x1289_x1771_x792121396}[：表示支持双端口]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[中继功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_x1289_x1771_x1364545283}[：表示不在上述列表的其它功能已开启]{lang="EN-US" style="font-family:宋体"}

[[Management address type]{lang="EN-US"}]{#struct_0_x1289_x1771_x214190266}

[[管理地址类型]{style="font-family:宋体"}]{#struct_0_x1289_x1771_749785620}

[[Management address]{lang="EN-US"}]{#struct_0_x1289_x1771_x213862586}

[[管理地址]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1073944077}

[[Management address interface type]{lang="EN-US"}]{#struct_0_x1289_x1771_x1559916406}

[[管理地址接口类型]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x213797050}

[[Management address interface ID]{lang="EN-US"}]{#struct_0_x1289_x1771_82134872}

[[管理地址接口索引]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x214386873}

[[Management address OID]{lang="EN-US"}]{#struct_0_x1289_x1771_767540089}

[[管理地址对象标识符]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x214321337}

[[DCBX control info:]{lang="EN-US"}]{#struct_0_x1289_x1771_383147428}

[[显示]{style="font-family:宋体"}[DCBX]{lang="EN-US"}]{#struct_0_x1289_x1771_x214517945}[控制]{style="font-family:宋体"}[TLV]{lang="EN-US"}[的信息，在标准]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[中显示版本信息]{style="font-family:宋体"}

[[Oper version]{lang="EN-US"}]{#struct_0_x1289_x1771_392840989}

[[DCBX]{lang="EN-US"}]{#struct_0_x1289_x1771_1181959500}[版本号]{style="font-family:宋体"}

[[Sequence number]{lang="EN-US"}]{#struct_0_x1289_x1771_x214452409}

[[DCBX TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_743106919}[内容改变的次数]{style="font-family:宋体"}

[[Acknowledge number]{lang="EN-US"}]{#struct_0_x1289_x1771_x214124729}

[[对端设备同步配置的次数]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1906680964}

[[DCBX ETS info]{lang="EN-US"}]{#struct_0_x1289_x1771_x214059193}

[[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_1106575853}[与本地优先级的映射关系及对应的带宽分配情况]{style="font-family:宋体"}

[[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_x214255801}

[[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_x791924788}[值]{style="font-family:宋体"}

[[Local Priority]{lang="EN-US"}]{#struct_0_x1289_x1771_x214190265}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_x1289_x1771_749982228}

[[Percentage]{lang="EN-US"}]{#struct_0_x1289_x1771_129783537}

[[对应的带宽分配]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x213862585}

[[P0-   P1-   P2-   P3-   P4-   P5-   P6-   P7-]{lang="EN-US"}]{#struct_0_x1289_x1771_x1073878541}

[[本端的]{style="font-family:宋体"}[no-drop]{lang="EN-US"}]{#struct_0_x1289_x1771_x213797049}[标记值对应的支持的优先级数]{style="font-family:宋体"}

[[Number of traffic classes supported]{lang="EN-US"}]{#struct_0_x1289_x1771_82724695}

[[PFC]{lang="EN-US"}]{#struct_0_x1289_x1771_x214386876}[支持的能力集，在]{style="font-family:宋体"}[1.01]{lang="EN-US"}[版本和标准版本中显示该项]{style="font-family:宋体"}

[[DCBX APP info]{lang="EN-US"}]{#struct_0_x1289_x1771_767867769}

[[显示]{style="font-family:宋体"}[APP TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x214321340}[信息]{style="font-family:宋体"}

[[Protocol ID]{lang="EN-US"}]{#struct_0_x1289_x1771_383081893}

[[应用协议号]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x214517948}

[[CoS map]{lang="EN-US"}]{#struct_0_x1289_x1771_391989021}

[[应用协议与]{style="font-family:宋体"}[CoS]{lang="EN-US"}]{#struct_0_x1289_x1771_x214452412}[的映射关系]{style="font-family:宋体"}

[[DCBX ETS configuration info]{lang="EN-US"}]{#struct_0_x1289_x1771_742386022}

[[显示]{style="font-family:宋体"}[ETS]{lang="EN-US"}]{#struct_0_x1289_x1771_x214124732}[配置]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[CBS]{lang="EN-US"}]{#struct_0_x1289_x1771_1907139717}

[[是否支持]{style="font-family:宋体"}[CBS]{lang="EN-US"}]{#struct_0_x1289_x1771_x214059196}[，表示本端是否支持令牌桶限速算法：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[False]{lang="EN-US"}]{#struct_0_x1289_x1771_1106248173}[：表示不支持令牌桶限速算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[True]{lang="EN-US"}]{#struct_0_x1289_x1771_x214255804}[：表示支持令牌桶限速算法]{lang="EN-US" style="font-family:宋体"}

[[Max TCs]{lang="EN-US"}]{#struct_0_x1289_x1771_x792252468}

[[显示支持的最大优先级数目]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x214190268}

[[TSA]{lang="EN-US"}]{#struct_0_x1289_x1771_750178836}

[[显示传输选择算法]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x213862588}

[[DCBX ETS recommendation info]{lang="EN-US"}]{#struct_0_x1289_x1771_x1073026573}

[[显示]{style="font-family:宋体"}[ETS]{lang="EN-US"}]{#struct_0_x1289_x1771_x213797052}[推荐]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[DCBX PFC info]{lang="EN-US"}]{#struct_0_x1289_x1771_x214386875}

[[显示]{style="font-family:宋体"}[PFC TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_767671161}[信息]{style="font-family:宋体"}

[[Value of MBC]{lang="EN-US"}]{#struct_0_x1289_x1771_x214321339}

[[支持的]{style="font-family:宋体"}[MBC]{lang="EN-US"}]{#struct_0_x1289_x1771_382492068}[状态]{style="font-family:宋体"}

[[Selected Field]{lang="EN-US"}]{#struct_0_x1289_x1771_x214517947}

[[选择域]{style="font-family:宋体"}]{#struct_0_x1289_x1771_392709917}

[[Port VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x214452411}

[[端口]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_742582630}

[[Port and protocol VLAN ID(PPVID)]{lang="EN-US"}]{#struct_0_x1289_x1771_x214124731}

[[端口协议]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x214059195}

[[Port and protocol VLAN supported]{lang="EN-US"}]{#struct_0_x1289_x1771_1106444781}

[[是否支持端口协议]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_x214255803}

[[Port and protocol VLAN enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_x792055860}

[[是否开启端口协议]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_x214190267}

[[VLAN name of VLAN 12]{lang="EN-US"}]{#struct_0_x1289_x1771_749851156}

[[VLAN 12]{lang="EN-US"}]{#struct_0_x1289_x1771_x213862587}[的名称]{style="font-family:宋体"}

[[Management VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x213797051}

[[管理]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_82200408}

[[Auto-negotiation supported]{lang="EN-US"}]{#struct_0_x1289_x1771_x214386878}

[[端口是否支持自协商]{style="font-family:宋体"}]{#struct_0_x1289_x1771_767998841}

[[Auto-negotiation enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_x214321342}

[[端口是否已开启自协商]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x214517950}

[[OperMau]{lang="EN-US"}]{#struct_0_x1289_x1771_392513310}

[[端口自适应的速率和双工状态]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x214452414}

[[Power port class]{lang="EN-US"}]{#struct_0_x1289_x1771_x214124734}

[[PoE]{lang="EN-US"}]{#struct_0_x1289_x1771_1907532933}[类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x214059198}[：表示供电设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_1107165677}[：表示受电设备]{lang="EN-US" style="font-family:宋体"}

[[PSE power supported]{lang="EN-US"}]{#struct_0_x1289_x1771_x214255806}

[[是否支持]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x214190270}[供电]{style="font-family:宋体"}

[[PSE power enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_749654549}

[[是否已开启]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x213862590}[供电]{style="font-family:宋体"}

[[PSE pairs control ability]{lang="EN-US"}]{#struct_0_x1289_x1771_x213797054}

[[供电方式是否可控]{style="font-family:宋体"}]{#struct_0_x1289_x1771_82397016}

[[Power pairs]{lang="EN-US"}]{#struct_0_x1289_x1771_x214386877}

[[PoE]{lang="EN-US"}]{#struct_0_x1289_x1771_x214321341}[端口的远程供电模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Signal]{lang="EN-US"}]{#struct_0_x1289_x1771_383016357}[：表示信号线供电模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spare]{lang="EN-US"}]{#struct_0_x1289_x1771_x214517949}[：表示空闲线供电模式]{lang="EN-US" style="font-family:宋体"}

[[Port power classification]{lang="EN-US"}]{#struct_0_x1289_x1771_x214452413}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_742451558}[的端口控制级别：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 0]{lang="EN-US"}]{#struct_0_x1289_x1771_x214124733}[：表示级别]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 1]{lang="EN-US"}]{#struct_0_x1289_x1771_x214059197}[：表示级别]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 2]{lang="EN-US"}]{#struct_0_x1289_x1771_1106313709}[：表示级别]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 3]{lang="EN-US"}]{#struct_0_x1289_x1771_x214255805}[：表示级别]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class 4]{lang="EN-US"}]{#struct_0_x1289_x1771_x214190269}[：表示级别]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}

[[Power type]{lang="EN-US"}]{#struct_0_x1289_x1771_2066411138}

[[供电类型：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_180927597}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 1 PD]{lang="EN-US"}]{#struct_0_x1289_x1771_x662930972}[：表示类型]{lang="EN-US" style="font-family:宋体"}[1 PD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 2 PD]{lang="EN-US"}]{#struct_0_x1289_x1771_x662996508}[：表示类型]{lang="EN-US" style="font-family:宋体"}[2 PD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 1 PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x663062044}[：表示类型]{lang="EN-US" style="font-family:宋体"}[1 PSE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type 2 PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_407177617}[：表示类型]{lang="EN-US" style="font-family:宋体"}[2 PSE]{lang="EN-US"}

[[Power source]{lang="EN-US"}]{#struct_0_x1289_x1771_x663127580}

[[功率来源（功率来源根据供电类型为]{style="font-family:宋体"}[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_x663193116}[类型或]{style="font-family:宋体"}[PSE]{lang="EN-US"}[类型，取值不同）：]{style="font-family:宋体"}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x663258652}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x663324188}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_x1289_x1771_x777063578}[：表示采用主用电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x1289_x1771_x663389724}[：表示采用备用电源作为电源]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reserved]{lang="EN-US"}]{#struct_0_x1289_x1771_x662406684}[：保留]{lang="EN-US" style="font-family:宋体"}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_x662472220}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x662930973}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x741072475}[：表示采用]{style="font-family:宋体"}[PSE]{lang="EN-US"}[作为电源]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_x1289_x1771_x662996509}[：表示采用本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE and local]{lang="EN-US"}]{#struct_0_x1289_x1771_x663062045}[：表示采用]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[和本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[Power priority]{lang="EN-US"}]{#struct_0_x1289_x1771_x663127581}

[[功率优先级：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x416263947}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_x663193117}[：表示优先级未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x1289_x1771_x663258653}[：表示优先级为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x1289_x1771_x663324189}[：表示优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low]{lang="EN-US"}]{#struct_0_x1289_x1771_x663389725}[：表示优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[级]{style="font-family:宋体"}

[[PD requested power value]{lang="EN-US"}]{#struct_0_x1289_x1771_x376442685}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_x662406685}[请求功率值，单位为瓦特]{style="font-family:宋体"}

[[PSE allocated power value]{lang="EN-US"}]{#struct_0_x1289_x1771_x662472221}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_x662930970}[分配功率值，单位为瓦特]{style="font-family:宋体"}

[[Link aggregation supported]{lang="EN-US"}]{#struct_0_x1289_x1771_750244372}

[[端口是否支持链路聚合]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x213862589}

[[Link aggregation enabled]{lang="EN-US"}]{#struct_0_x1289_x1771_x213797053}

[[端口是否已开启链路聚合]{style="font-family:宋体"}]{#struct_0_x1289_x1771_82069336}

[[Congestion notification TLV info]{lang="EN-US"}]{#struct_0_x1289_x1771_x393739264}

[[拥塞通知]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x394329088}[信息。本字段的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Dot1p]{lang="EN-US"}]{#struct_0_x1289_x1771_406850649}

[[802.1p]{lang="EN-US"}]{#struct_0_x1289_x1771_x394394624}[优先级]{style="font-family:宋体"}

[[CNPV]{lang="EN-US"}]{#struct_0_x1289_x1771_1172279138}

[[802.1p]{lang="EN-US"}]{#struct_0_x1289_x1771_1172213602}[优先级是否被配置为]{style="font-family:宋体"}[CNPV]{lang="EN-US"}[，即是否匹配该优先级的报文具有]{style="font-family:宋体"}[QCN]{lang="EN-US"}[功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x1289_x1771_x1985107484}[：表示]{lang="EN-US" style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级被配置为]{lang="EN-US" style="font-family:宋体"}[CNPV]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x1289_x1771_1172148066}[：表示]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级未被配置为]{style="font-family:宋体"}[CNPV]{lang="EN-US"}

[[Ready]{lang="EN-US"}]{#struct_0_x1289_x1771_1172082530}

[[表明设备接口是否已经关闭了]{style="font-family:宋体"}[802.1p]{lang="EN-US"}]{#struct_0_x1289_x1771_1172541282}[优先级与隔离优先级的映射：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x1289_x1771_1909178321}[：表示关闭优先级映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x1289_x1771_1172475746}[：表示未关闭优先级映射]{style="font-family:宋体"}

[[Maximum frame size]{lang="EN-US"}]{#struct_0_x1289_x1771_1351697067}

[[端口支持的最大帧长度]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1351762603}

[[MED information]{lang="EN-US"}]{#struct_0_x1289_x1771_1351565995}

[[MED]{lang="EN-US"}]{#struct_0_x1289_x1771_297459056}[设备相关信息]{style="font-family:宋体"}

[[Device class]{lang="EN-US"}]{#struct_0_x1289_x1771_1351631531}

[[MED]{lang="EN-US"}]{#struct_0_x1289_x1771_1351959211}[设备类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connectivity device]{lang="EN-US"}]{#struct_0_x1289_x1771_x1362734040}[：表示网络设备]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class I]{lang="EN-US"}]{#struct_0_x1289_x1771_1352024747}[：表示一般终端设备，即所有需要]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[发现服务的终端设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class II]{lang="EN-US"}]{#struct_0_x1289_x1771_1351828139}[：表示媒体终端设备，即具备媒体能力的终端设备，其能力包含了一般终端设备的能力。]{style="font-family:宋体"}[该类设备支持媒体流]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class III]{lang="EN-US"}]{#struct_0_x1289_x1771_1351893675}[：表示通讯终端设备，即直接支持目标用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[通讯系统的终端设备，其能力包含了一般终端设备和媒体终端设备的所有能力。]{style="font-family:宋体"}[该类设备直接被目标用户所使用]{lang="EN-US" style="font-family:宋体"}

[[Media policy type]{lang="EN-US"}]{#struct_0_x1289_x1771_624412221}

[[媒体策略类型：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1352221355}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_1352286891}[：表示类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Voice]{lang="EN-US"}]{#struct_0_x1289_x1771_x630888024}[：表示语音]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VoiceSignaling]{lang="EN-US"}]{#struct_0_x1289_x1771_1351697068}[：表示语音信号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GuestVoice]{lang="EN-US"}]{#struct_0_x1289_x1771_1351762604}[：表示访客语音]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GuestVoiceSignaling]{lang="EN-US"}]{#struct_0_x1289_x1771_1351565996}[：表示访客语音信号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SoftPhoneVoice]{lang="EN-US"}]{#struct_0_x1289_x1771_297262448}[：表示软体电话语音]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Videoconferencing]{lang="EN-US"}]{#struct_0_x1289_x1771_1351631532}[：表示视频会议]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StreamingVideo]{lang="EN-US"}]{#struct_0_x1289_x1771_1351959212}[：表示流视频]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VideoSignaling]{lang="EN-US"}]{#struct_0_x1289_x1771_1352024748}[：表示视频信号]{lang="EN-US" style="font-family:宋体"}

[[Unknown policy]{lang="EN-US"}]{#struct_0_x1289_x1771_x263957847}

[[媒体策略类型是否未知：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1351828140}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x1289_x1771_1351893676}[：表示策略类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x1289_x1771_1352221356}[：表示策略类型已知]{style="font-family:宋体"}

[[VLAN tagged]{lang="EN-US"}]{#struct_0_x1289_x1771_96514235}

[[媒体]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_1352286892}[是否带]{style="font-family:宋体"}[Tag]{lang="EN-US"}

[[Media policy VLAN ID]{lang="EN-US"}]{#struct_0_x1289_x1771_1351697065}

[[媒体]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_1351762601}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Media policy L2 priority]{lang="EN-US"}]{#struct_0_x1289_x1771_1351565993}

[[二层优先级]{style="font-family:宋体"}]{#struct_0_x1289_x1771_297065840}

[[Media policy DSCP]{lang="EN-US"}]{#struct_0_x1289_x1771_1351631529}

[[DSCP]{lang="EN-US"}]{#struct_0_x1289_x1771_1351959209}[的值]{style="font-family:宋体"}

[[Location format]{lang="EN-US"}]{#struct_0_x1289_x1771_1352024745}

[[位置信息格式：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1351828137}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_x1289_x1771_x1361721118}[：表示无效位置数据类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Coordinate-based LCI]{lang="EN-US"}]{#struct_0_x1289_x1771_1351893673}[：表示基于坐标的位置信息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Civic Address LCI]{lang="EN-US"}]{#struct_0_x1289_x1771_1352221353}[：表示普通地址信息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ECS ELIN]{lang="EN-US"}]{#struct_0_x1289_x1771_1352286889}[：表示紧急电话号码]{style="font-family:宋体"}

[[Location information]{lang="EN-US"}]{#struct_0_x1289_x1771_1351697066}

[[位置信息]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1318914932}

[[PoE PSE power source]{lang="EN-US"}]{#struct_0_x1289_x1771_1351762602}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_1351565994}[所采用的电源类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_1351631530}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_x1289_x1771_1351959210}[：表示采用主用电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x1289_x1771_x1362668504}[：表示采用备用电源作为电源]{style="font-family:宋体"}

[[PoE PD power source]{lang="EN-US"}]{#struct_0_x1289_x1771_1352024746}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_1351828138}[所采用的电源类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_1351893674}[：表示采用的电源类型未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_1352221354}[：表示采用]{style="font-family:宋体"}[PSE]{lang="EN-US"}[作为电源]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_x1289_x1771_1352286890}[：表示采用本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE and local]{lang="EN-US"}]{#struct_0_x1289_x1771_x630953560}[：表示采用]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[和本地电源作为电源]{lang="EN-US" style="font-family:宋体"}

[[PoE service type]{lang="EN-US"}]{#struct_0_x1289_x1771_1351697063}

[[PoE]{lang="EN-US"}]{#struct_0_x1289_x1771_1351762599}[服务类型]{style="font-family:宋体"}

[[Port PSE priority]{lang="EN-US"}]{#struct_0_x1289_x1771_1351565991}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_1351631527}[上端口的供电优先级：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_1351959207}[：表示优先级未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x1289_x1771_x1362602969}[：表示优先级为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x1289_x1771_1352024743}[：表示优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low]{lang="EN-US"}]{#struct_0_x1289_x1771_1351828135}[：表示优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[级]{style="font-family:宋体"}

[[Port PD priority]{lang="EN-US"}]{#struct_0_x1289_x1771_1351893671}

[[PD]{lang="EN-US"}]{#struct_0_x1289_x1771_1352221351}[上端口的受电优先级：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x1289_x1771_1352286887}[：表示优先级未知]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x1289_x1771_x630494807}[：表示优先级为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x1289_x1771_1351697064}[：表示优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low]{lang="EN-US"}]{#struct_0_x1289_x1771_1351762600}[：表示优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[级]{style="font-family:宋体"}

[[Port available power value]{lang="EN-US"}]{#struct_0_x1289_x1771_1351565992}

[[PSE]{lang="EN-US"}]{#struct_0_x1289_x1771_1351631528}[上端口可提供的功率，或]{style="font-family:宋体"}[PD]{lang="EN-US"}[上端口所需的功率，单位为瓦特]{style="font-family:宋体"}

[[HardwareRev]{lang="EN-US"}]{#struct_0_x1289_x1771_1351959208}

[[产品的硬件版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1363192793}

[[FirmwareRev]{lang="EN-US"}]{#struct_0_x1289_x1771_1352024744}

[[产品的固件版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1351828136}

[[SoftwareRev]{lang="EN-US"}]{#struct_0_x1289_x1771_1351893672}

[[产品的软件版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1352221352}

[[SerialNum]{lang="EN-US"}]{#struct_0_x1289_x1771_1352286888}

[[序列号]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1377186288}

[[Manufacturer name]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377120752}

[[制造厂商]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1377317360}

[[Model name]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377251824}

[[模块名称]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1376924144}

[[Asset tracking identifier]{lang="EN-US"}]{#struct_0_x1289_x1771_805506338}

[[资产跟踪]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376858608}

[[Unknown basic TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377055216}

[[未知的基本]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376989680}

[[TLV type]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376662000}

[[未知的基本]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376596464}[类型]{style="font-family:宋体"}

[[TLV information]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377186287}

[[未知的基本]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377120751}[的具体信息]{style="font-family:宋体"}

[[Unknown organizationally-defined TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377317359}

[[未知组织定义]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377251823}

[[TLV OUI]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376924143}

[[未知组织定义]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376858607}[的对象唯一标识]{style="font-family:宋体"}

[[TLV subtype]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377055215}

[[未知的组织定义]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376989679}[类型]{style="font-family:宋体"}

[[Index]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376661999}

[[未知组织的索引]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1376596463}

[[CDP neighbor-information of port 1]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377186290}

[[端口]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377120754}[的]{style="font-family:宋体"}[CDP]{lang="EN-US"}[邻居信息]{style="font-family:宋体"}

[[CDP neighbor index]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377317362}

[[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377251826}[邻居索引]{style="font-family:宋体"}

[[Chassis ID/subtype]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376924146}

[[Chassis ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376858610}[值及]{style="font-family:宋体"}[Chassis ID]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Port ID/subtype]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377055218}

[[Port ID]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376989682}[值及]{style="font-family:宋体"}[PortID]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Software version]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376662002}

[[邻居软件版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1376596466}

[[Platform version]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377186289}

[[邻居平台版本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1377120753}

[[Duplex]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377317361}

[[双工状态]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1377251825}

[[Capabilities]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376924145}

[[系统已开启的功能：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1376858609}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Repeater]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377055217}[：表示开启信号中继功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376989681}[：表示开启交换功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WlanAccessPoint]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376662001}[：表示开启无线接入点功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376596465}[：表示开启路由功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Telephone]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377186292}[：表示开启电话功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DocsisCableDevice]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377120756}[：表示开启电缆设备功能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StationOnly]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377317364}[：表示开启只作站点功能，与其他功能不能同时出现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377251828}[：表示开启不在上述列表的其他功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376924148}[：表示该邻居未发布该]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Local Interface]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376858612}

[[接收]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377055220}[信息的本端端口]{style="font-family:宋体"}

[[Chassis ID : \* \-- \-- Nearest nontpmr bridge neighbor                               ]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376989684}

[[                    #\-- \-- Nearest customer bridge neighbor]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376662004}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\*]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376596468}[符号：表示该邻居是最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理类型邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\#]{lang="EN-US"}]{#struct_0_x1289_x1771_x1377120755}[符号：表示该邻居是最近客户桥代理类型邻居]{style="font-family:宋体"}

[[Transmit Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_x859516257}

[[本端发送的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x859450721}

[[Receive Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_x859319649}

[[本端向对端请求的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x858729825}

[[Fallback Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_x859254110}

[[本端向对端请求的候选等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x859188574}

[[Echo Transmit Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_x859123038}

[[收到的对端发送的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x859516254}

[[Echo Receive Tw]{lang="EN-US"}]{#struct_0_x1289_x1771_x859450718}

[[收到的对端请求的等待时间，单位为微秒]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x859385182}

[ ]{lang="EN-US"}

::: {#-1172730649 .myid}
[]{#_Toc404784694}[]{#struct_0_x1289_x1771_x848716233}[]{#_Toc144347673}[]{#_Toc287965202}[]{#_Toc295980444}[]{#_Toc287965410}[]{#_Toc295980652}

**LLDP \-- LLDP配置命令 \-- display lldp statistics**

------------------------------------------------------------------------

[**[display lldp statistics]{lang="EN-US"}**]{#struct_0_x1289_x1771_1217549778}[命令用来显示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_631649466}

[**[display lldp statistics]{lang="EN-US"}**[ \[ **global** \| \[ **interface** *interface-type interface-number* \] \[ **agent** ]{lang="EN-US"}]{#struct_0_x1289_x1771_364362126}[{]{lang="EN-US"}[ **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1861201974}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1251817302}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1377055219}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1265386224}

[[network-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_x656863341}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x588802761}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_x1351132107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_34518665}

[**[global]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1729865368}[：显示全局]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1289_x1771_1935041166}[：显示指定接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[统计信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1376989683}[：显示指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的统计信息。如果未指定该参数，将显示所有类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的统计信息。]{style="font-family:宋体"}

[**[nearest-bridge]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1130915498}[：表示最近桥代理。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1323275805}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_2139913555}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2071231463}

[[如果未指定任何参数，将同时显示全局和接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1490531235}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x90512530}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x129550362}[显示全局和接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display lldp statistics]{lang="EN-US"}]{#struct_0_x1289_x1771_x1376596467}

[LLDP statistics global information:]{lang="EN-US"}

[LLDP neighbor information last change time:0 days, 0 hours, 4 minutes, 40 seconds]{lang="EN-US"}

[The number of LLDP neighbor information inserted : 1]{lang="EN-US"}

[The number of LLDP neighbor information deleted  : 1]{lang="EN-US"}

[The number of LLDP neighbor information dropped  : 0]{lang="EN-US"}

[The number of LLDP neighbor information aged out : 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[LLDP statistics information of port 1 \[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent nearest-bridge:]{lang="EN-US"}

[The number of LLDP frames transmitted            : 0]{lang="EN-US"}

[The number of LLDP frames received               : 0]{lang="EN-US"}

[The number of LLDP frames discarded              : 0]{lang="EN-US"}

[The number of LLDP error frames                  : 0]{lang="EN-US"}

[The number of LLDP TLVs discarded                : 0]{lang="EN-US"}

[The number of LLDP TLVs unrecognized             : 0]{lang="EN-US"}

[The number of LLDP neighbor information aged out : 0]{lang="EN-US"}

[The number of CDP frames transmitted             : 0]{lang="EN-US"}

[The number of CDP frames received                : 0]{lang="EN-US"}

[The number of CDP frames discarded               : 0]{lang="EN-US"}

[The number of CDP error frames                   : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[LLDP agent nearest-nontpmr:]{lang="EN-US"}

[The number of LLDP frames transmitted            : 0]{lang="EN-US"}

[The number of LLDP frames received               : 0]{lang="EN-US"}

[The number of LLDP frames discarded              : 0]{lang="EN-US"}

[The number of LLDP error frames                  : 0]{lang="EN-US"}

[The number of LLDP TLVs discarded                : 0]{lang="EN-US"}

[The number of LLDP TLVs unrecognized             : 0]{lang="EN-US"}

[The number of LLDP neighbor information aged out : 0]{lang="EN-US"}

[The number of CDP frames transmitted             : 0]{lang="EN-US"}

[The number of CDP frames received                : 0]{lang="EN-US"}

[The number of CDP frames discarded               : 0]{lang="EN-US"}

[The number of CDP error frames                   : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[LLDP agent nearest-customer:]{lang="EN-US"}

[The number of LLDP frames transmitted            : 0]{lang="EN-US"}

[The number of LLDP frames received               : 0]{lang="EN-US"}

[The number of LLDP frames discarded              : 0]{lang="EN-US"}

[The number of LLDP error frames                  : 0]{lang="EN-US"}

[The number of LLDP TLVs discarded                : 0]{lang="EN-US"}

[The number of LLDP TLVs unrecognized             : 0]{lang="EN-US"}

[The number of LLDP neighbor information aged out : 0]{lang="EN-US"}

[The number of CDP frames transmitted             : 0]{lang="EN-US"}

[The number of CDP frames received                : 0]{lang="EN-US"}

[The number of CDP frames discarded               : 0]{lang="EN-US"}

[The number of CDP error frames                   : 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_1397368383}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的最近客户桥代理上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display lldp statistics interface gigabitethernet 1/0/1 agent nearest-customer]{lang="EN-US"}]{#struct_0_x1289_x1771_188897653}

[LLDP statistics information of port 1 \[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent nearest-customer:]{lang="EN-US"}

[The number of LLDP frames transmitted            : 0]{lang="EN-US"}

[The number of LLDP frames received               : 0]{lang="EN-US"}

[The number of LLDP frames discarded              : 0]{lang="EN-US"}

[The number of LLDP error frames                  : 0]{lang="EN-US"}

[The number of LLDP TLVs discarded                : 0]{lang="EN-US"}

[The number of LLDP TLVs unrecognized             : 0]{lang="EN-US"}

[The number of LLDP neighbor information aged out : 0]{lang="EN-US"}

[The number of CDP frames transmitted             : 0]{lang="EN-US"}

[The number of CDP frames received                : 0]{lang="EN-US"}

[The number of CDP frames discarded               : 0]{lang="EN-US"}

[The number of CDP error frames                   : 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display lldp statistics]{lang="EN-US"}]{#struct_0_x1289_x1771_x1955176576}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_155439350}[[字段]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x342121516}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1191672473}

[[LLDP agent nearest-bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_1645115281}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_188963189}[缺省代理，即最近桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-customer]{lang="EN-US"}]{#struct_0_x1289_x1771_358935506}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_166835603}[最近客户桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-nontpmr]{lang="EN-US"}]{#struct_0_x1289_x1771_x1218113651}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x2797279}[最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理]{style="font-family:宋体"}

[[LLDP statistics global information]{lang="EN-US"}]{#struct_0_x1289_x1771_1640524492}

[[全局]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_188766581}[统计信息]{style="font-family:宋体"}

[[LLDP neighbor information last change time]{lang="EN-US"}]{#struct_0_x1289_x1771_2075639350}

[[邻居信息的最后更新时间]{style="font-family:宋体"}]{#struct_0_x1289_x1771_478285658}

[[The number of LLDP neighbor information inserted]{lang="EN-US"}]{#struct_0_x1289_x1771_66406964}

[[邻居信息的增加次数]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1484097652}

[[The number of LLDP neighbor information deleted]{lang="EN-US"}]{#struct_0_x1289_x1771_188832117}

[[邻居信息的删除次数]{style="font-family:宋体"}]{#struct_0_x1289_x1771_382069807}

[[The number of LLDP neighbor information dropped]{lang="EN-US"}]{#struct_0_x1289_x1771_46518397}

[[由于空间不足而导致丢弃邻居信息的次数]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x236043034}

[[The number of LLDP neighbor information aged out]{lang="EN-US"}]{#struct_0_x1289_x1771_x438217141}

[[邻居信息的老化数量]{style="font-family:宋体"}]{#struct_0_x1289_x1771_189159797}

[[LLDP statistics Information of port 1]{lang="EN-US"}]{#struct_0_x1289_x1771_x819278688}

[[端口]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1289_x1771_x886737205}[上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[统计信息]{style="font-family:宋体"}

[[The number of LLDP frames transmitted]{lang="EN-US"}]{#struct_0_x1289_x1771_x1006001442}

[[发送的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_648185871}[帧总数]{style="font-family:宋体"}

[[The number of LLDP frames received]{lang="EN-US"}]{#struct_0_x1289_x1771_189225333}

[[收到的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1393034469}[帧总数]{style="font-family:宋体"}

[[The number of LLDP frames discarded]{lang="EN-US"}]{#struct_0_x1289_x1771_x1762735409}

[[丢弃的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1095255491}[帧总数]{style="font-family:宋体"}

[[The number of LLDP error frames]{lang="EN-US"}]{#struct_0_x1289_x1771_189028725}

[[收到的错误]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1880214925}[帧总数]{style="font-family:宋体"}

[[The number of LLDP TLVs discarded]{lang="EN-US"}]{#struct_0_x1289_x1771_1350322718}

[[丢弃的]{style="font-family:宋体"}[LLDP TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x133612545}[总数]{style="font-family:宋体"}

[[The number of LLDP TLVs unrecognized]{lang="EN-US"}]{#struct_0_x1289_x1771_189094261}

[[不可识别的]{style="font-family:宋体"}[LLDP TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1492872785}[总数]{style="font-family:宋体"}

[[The number of LLDP neighbor information aged out]{lang="EN-US"}]{#struct_0_x1289_x1771_x203788681}

[[老化的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1084790373}[邻居信息总数]{style="font-family:宋体"}

[[The number of CDP frames transmitted]{lang="EN-US"}]{#struct_0_x1289_x1771_189421941}

[[发送的]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_2028617595}[帧总数]{style="font-family:宋体"}

[[The number of CDP frames received]{lang="EN-US"}]{#struct_0_x1289_x1771_x583486721}

[[收到的]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1748250145}[帧总数]{style="font-family:宋体"}

[[The number of CDP frames discarded]{lang="EN-US"}]{#struct_0_x1289_x1771_189487477}

[[丢弃的]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_792734230}[帧总数]{style="font-family:宋体"}

[[The number of CDP error frames]{lang="EN-US"}]{#struct_0_x1289_x1771_x518454481}

[[收到的错误]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1067145968}[帧总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#61811945 .myid}
[]{#_Toc404784695}[]{#struct_0_x1289_x1771_188897654}[]{#_Toc144347674}

**LLDP \-- LLDP配置命令 \-- display lldp status**

------------------------------------------------------------------------

[**[display lldp status]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1955176571}[命令用来显示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1101636403}

[**[display lldp status ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \] \[ **agent** ]{lang="EN-US"}]{#struct_0_x1289_x1771_x119253083}[{]{lang="EN-US"}[ **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1172474846}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1405617532}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1490517642}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x797572962}

[[network-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_x2022097707}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_188963190}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_x1979716661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1840914256}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1289_x1771_33898994}[：显示指定接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[状态信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定该参数，将显示所有开启了]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能的接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_1093482286}[：显示指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的状态信息。如果未指定该参数，将显示所有类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的状态信息。]{style="font-family:宋体"}

[**[nearest-bridge]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1492750597}[：表示最近桥代理。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_x226262240}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_1373628904}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_676958189}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_188766582}[显示全局和所有接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display lldp status]{lang="EN-US"}]{#struct_0_x1289_x1771_188832118}

[Global status of LLDP: Enable]{lang="EN-US"}

[Bridge mode of LLDP: customer-bridge]{lang="EN-US"}

[The current number of LLDP neighbors: 0]{lang="EN-US"}

[The current number of CDP neighbors: 0]{lang="EN-US"}

[LLDP neighbor information last changed time: 0 days, 0 hours, 4 minutes, 40 seconds]{lang="EN-US"}

[Transmit interval              : 30s]{lang="EN-US"}

[Fast transmit interval         : 1s]{lang="EN-US"}

[Transmit max credit            : 5]{lang="EN-US"}

[Hold multiplier                : 4]{lang="EN-US"}

[Reinit delay                   : 2s]{lang="EN-US"}

[Trap interval                  : 5s]{lang="EN-US"}

[Fast start times               : 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[LLDP status information of port 1 \[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent  nearest-bridge:]{lang="EN-US"}

[Port status of LLDP            : Enable]{lang="EN-US"}

[Admin status                   : Tx_Rx]{lang="EN-US"}

[Trap flag                      : No]{lang="EN-US"}

[MED trap flag                  : No]{lang="EN-US"}

[Polling interval               : 0s]{lang="EN-US"}

[Number of LLDP neighbors       : 5]{lang="EN-US"}

[Number of MED neighbors        : 2]{lang="EN-US"}

[Number of CDP neighbors        : 0]{lang="EN-US"}

[Number of sent optional TLV    : 12]{lang="EN-US"}

[Number of received unknown TLV : 5]{lang="EN-US"}

[LLDP agent nearest-nontpmr:]{lang="EN-US"}

[Port status of LLDP            : Enable]{lang="EN-US"}

[Admin status                   : Tx_Rx]{lang="EN-US"}

[Trap flag                      : No]{lang="EN-US"}

[Polling interval               : 0s]{lang="EN-US"}

[Number of LLDP neighbors       : 5]{lang="EN-US"}

[Number of MED neighbors        : 2]{lang="EN-US"}

[Number of CDP neighbors        : 0]{lang="EN-US"}

[Number of sent optional TLV    : 12]{lang="EN-US"}

[Number of received unknown TLV : 5]{lang="EN-US"}

[ ]{lang="EN-US"}

[LLDP agent nearest-customer:]{lang="EN-US"}

[Port status of LLDP            : Enable]{lang="EN-US"}

[Admin status                   : Tx_Rx]{lang="EN-US"}

[Trap flag                      : No]{lang="EN-US"}

[Polling interval               : 0s]{lang="EN-US"}

[Number of LLDP neighbors       : 5]{lang="EN-US"}

[Number of MED neighbors        : 2]{lang="EN-US"}

[Number of CDP neighbors        : 0]{lang="EN-US"}

[Number of sent optional TLV    : 12]{lang="EN-US"}

[Number of received unknown TLV : 5]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display lldp status]{lang="EN-US"}]{#struct_0_x1289_x1771_382069800}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_153632314}[[字段]{style="font-family:黑体"}]{#struct_0_x1289_x1771_189159798}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x819278675}

[[Bridge mode of LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x886409524}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_193860783}[桥模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[service-bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x195905787}[：表示服务桥模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[customer-bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_x1467186077}[：表示客户桥模式]{lang="EN-US" style="font-family:
  宋体"}

[[LLDP agent nearest-bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_189225334}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1393034462}[缺省代理，即最近桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-customer]{lang="EN-US"}]{#struct_0_x1289_x1771_x1809789576}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1118636913}[最近客户桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-nontpmr]{lang="EN-US"}]{#struct_0_x1289_x1771_x552314697}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1546854354}[最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理]{style="font-family:宋体"}

[[Global status of LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_189028726}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1880214924}[功能是否已全局开启]{style="font-family:宋体"}

[[The current number of LLDP neighbors]{lang="EN-US"}]{#struct_0_x1289_x1771_1350257182}

[[当前设备的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_259847438}[邻居总数]{style="font-family:宋体"}

[[The current number of CDP neighbors]{lang="EN-US"}]{#struct_0_x1289_x1771_x81453293}

[[当前设备的]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_189094262}[邻居总数]{style="font-family:宋体"}

[[LLDP neighbor information last changed time]{lang="EN-US"}]{#struct_0_x1289_x1771_1492872782}

[[邻居信息的最后更新时间]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x204247433}

[[Transmit interval]{lang="EN-US"}]{#struct_0_x1289_x1771_200167054}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_189421942}[报文的发送间隔]{style="font-family:宋体"}

[[Hold multiplier]{lang="EN-US"}]{#struct_0_x1289_x1771_2028617594}

[[TTL]{lang="EN-US"}]{#struct_0_x1289_x1771_x583552257}[乘数]{style="font-family:宋体"}

[[Reinit delay]{lang="EN-US"}]{#struct_0_x1289_x1771_1022778263}

[[端口初始化延迟时间]{style="font-family:宋体"}]{#struct_0_x1289_x1771_163502173}

[[Transmit max credit]{lang="EN-US"}]{#struct_0_x1289_x1771_189487478}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_792734233}[报文发包限速令牌桶的最大值]{style="font-family:宋体"}

[[Trap interval]{lang="EN-US"}]{#struct_0_x1289_x1771_x518454482}

[[Trap]{lang="EN-US"}]{#struct_0_x1289_x1771_x1066949360}[信息的发送间隔]{style="font-family:宋体"}

[[Fast start times]{lang="EN-US"}]{#struct_0_x1289_x1771_188897651}

[[快速发送]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1955176574}[报文的个数]{style="font-family:宋体"}

[[LLDP status infomation of port 1]{lang="EN-US"}]{#struct_0_x1289_x1771_x1504920930}

[[端口]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1289_x1771_x1494764373}[上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[状态信息]{style="font-family:宋体"}

[[Port status of LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_188963187}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_358935492}[功能是否已在端口上开启]{style="font-family:宋体"}

[[Admin status]{lang="EN-US"}]{#struct_0_x1289_x1771_923615484}

[[端口]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1567187100}[工作模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tx_Rx]{lang="EN-US"}]{#struct_0_x1289_x1771_188766579}[：表示既发送也接收]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Rx_Only]{lang="EN-US"}]{#struct_0_x1289_x1771_1355595326}[：表示只接收不发送]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tx_Only]{lang="EN-US"}]{#struct_0_x1289_x1771_x1576870555}[：表示只发送不接收]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x1289_x1771_1747569292}[：表示既不发送也不接收]{lang="EN-US" style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Trap Flag]{lang="EN-US"}]{#struct_0_x1289_x1771_188832115}

[[LLDP Trap]{lang="EN-US"}]{#struct_0_x1289_x1771_382069805}[功能是否已开启]{style="font-family:宋体"}

[[MED trap flag]{lang="EN-US"}]{#struct_0_x1289_x1771_46518395}

[[LLDP-MED Trap]{lang="EN-US"}]{#struct_0_x1289_x1771_189159795}[功能是否已开启]{style="font-family:宋体"}

[[Polling interval]{lang="EN-US"}]{#struct_0_x1289_x1771_x819278686}

[[轮询间隔，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1289_x1771_x886606133}[表示轮询功能处于关闭状态]{style="font-family:宋体"}

[[Number of neighbors]{lang="EN-US"}]{#struct_0_x1289_x1771_x1781125537}

[[端口]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_189225331}[邻居数量]{style="font-family:宋体"}

[[Number of MED neighbors]{lang="EN-US"}]{#struct_0_x1289_x1771_x1393034467}

[[端口]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_x1289_x1771_2081893193}[邻居设备的数量]{style="font-family:宋体"}

[[Number of CDP neighbors]{lang="EN-US"}]{#struct_0_x1289_x1771_189028723}

[[端口]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1880214919}[邻居设备的数量]{style="font-family:宋体"}

[[Number of sent optional TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1351109151}

[[端口在一个]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_189094259}[报文中发送的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[总数]{style="font-family:宋体"}

[[Number of received unknown TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x81105319}

[[端口在所有]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_99251167}[报文中收到的不能识别的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1411816975 .myid}
[]{#_Toc404784696}[]{#struct_0_x1289_x1771_2038643670}[]{#_Toc144347675}

**LLDP \-- LLDP配置命令 \-- display lldp tlv-config**

------------------------------------------------------------------------

[**[display lldp tlv-config]{lang="EN-US"}**]{#struct_0_x1289_x1771_x844137094}[命令用来显示接口上可发送的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_189421939}

[**[display lldp tlv-config ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \] \[ **agent** { **nearest-bridge** \| **nearest-customer** \| **nearest-nontpmr** } \]]{lang="EN-US"}]{#struct_0_x1289_x1771_x1074708621}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_542738383}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1579712723}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_37232089}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_585418935}

[[network-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_828982312}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1014882970}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1289_x1771_x1692737934}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_189487475}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1289_x1771_792734228}[：显示指定接口上可发送的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定该参数，将显示所有接口上可发送的可选]{style="font-family:
宋体"}[TLV]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_1820197687}[：显示指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息。如果未指定该参数，将显示所有类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[nearest-bridge]{lang="EN-US"}**]{#struct_0_x1289_x1771_110346014}[：表示最近桥代理。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_x2049563806}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_827126612}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1695091318}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_188897652}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上可发送的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display lldp tlv-config interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1289_x1771_188766580}

[LLDP tlv-config of port 1\[GigabitEthernet1/0/1\]:]{lang="EN-US"}

[LLDP agent nearest-bridge:]{lang="EN-US"}

[NAME                              STATUS    DEFAULT]{lang="EN-US"}

[Basic optional TLV:]{lang="EN-US"}

[ Port Description TLV             YES       YES]{lang="EN-US"}

[ System Name TLV                  YES       YES]{lang="EN-US"}

[ System Description TLV           YES       YES]{lang="EN-US"}

[ System Capabilities TLV          YES       YES]{lang="EN-US"}

[ Management Address TLV           YES       YES]{lang="EN-US"}

[IEEE 802.1 extend TLV:]{lang="EN-US"}

[ Port VLAN ID TLV                 YES       YES]{lang="EN-US"}

[ Port And Protocol VLAN ID TLV    YES       YES]{lang="EN-US"}

[ VLAN Name TLV                    YES       YES]{lang="EN-US"}

[ DCBX TLV                         NO        NO]{lang="EN-US"}

[ EVB TLV                          NO        NO]{lang="EN-US"}

[ Link Aggregation TLV             YES       YES]{lang="EN-US"}

[ Management VID TLV               YES       YES]{lang="EN-US"}

[ Congestion notification TLV      NO        NO]{lang="EN-US"}

[IEEE 802.3 extend TLV:]{lang="EN-US"}

[ MAC-Physic TLV                   YES       YES]{lang="EN-US"}

[ Power via MDI TLV                YES       YES]{lang="EN-US"}

[ Maximum Frame Size TLV           YES       YES]{lang="EN-US"}

[ Energy-Efficient Ethernet TLV    NO        NO]{lang="EN-US"}

[LLDP-MED extend TLV:]{lang="EN-US"}

[ Capabilities TLV                 YES        YES]{lang="EN-US"}

[ Network Policy TLV               YES        YES]{lang="EN-US"}

[ Location Identification TLV      NO         NO]{lang="EN-US"}

[ Extended Power via MDI TLV       YES        YES]{lang="EN-US"}

[ Inventory TLV                    YES        YES]{lang="EN-US"}

[LLDP agent nearest-nontpmr:]{lang="EN-US"}

[NAME                              STATUS    DEFAULT]{lang="EN-US"}

[Basic optional TLV:]{lang="EN-US"}

[ Port Description TLV             YES       NO]{lang="EN-US"}

[ System Name TLV                  YES       NO]{lang="EN-US"}

[ System Description TLV           YES       NO]{lang="EN-US"}

[ System Capabilities TLV          YES       NO]{lang="EN-US"}

[ Management Address TLV           YES       NO]{lang="EN-US"}

[IEEE 802.1 extend TLV:]{lang="EN-US"}

[ Port VLAN ID TLV                 YES       NO]{lang="EN-US"}

[ Port And Protocol VLAN ID TLV    YES       NO]{lang="EN-US"}

[ VLAN Name TLV                    YES       NO]{lang="EN-US"}

[ DCBX TLV                         NO        NO]{lang="EN-US"}

[ EVB TLV                          YES       YES]{lang="EN-US"}

[ Link Aggregation TLV             YES       NO]{lang="EN-US"}

[ Management VID TLV               NO        NO]{lang="EN-US"}

[IEEE 802.3 extend TLV:]{lang="EN-US"}

[ MAC-Physic TLV                   YES       NO]{lang="EN-US"}

[ Power via MDI TLV                YES       NO]{lang="EN-US"}

[ Maximum Frame Size TLV           YES       NO]{lang="EN-US"}

[ Energy-Efficient Ethernet TLV    NO        NO]{lang="EN-US"}

[LLDP-MED extend TLV:]{lang="EN-US"}

[ Capabilities TLV                 YES        NO]{lang="EN-US"}

[ Network Policy TLV               YES        NO]{lang="EN-US"}

[ Location Identification TLV      NO         NO]{lang="EN-US"}

[ Extended Power via MDI TLV       YES        NO]{lang="EN-US"}

[ Inventory TLV                    YES        NO]{lang="EN-US"}

[ ]{lang="EN-US"}

[LLDP agent nearest-customer:]{lang="EN-US"}

[NAME                              STATUS    DEFAULT]{lang="EN-US"}

[Basic optional TLV:]{lang="EN-US"}

[ Port Description TLV             YES       YES]{lang="EN-US"}

[ System Name TLV                  YES       YES]{lang="EN-US"}

[ System Description TLV           YES       YES]{lang="EN-US"}

[ System Capabilities TLV          YES       YES]{lang="EN-US"}

[ Management Address TLV           YES       YES]{lang="EN-US"}

[IEEE 802.1 extend TLV:]{lang="EN-US"}

[ Port VLAN ID TLV                 YES       YES]{lang="EN-US"}

[ Port And Protocol VLAN ID TLV    YES       YES]{lang="EN-US"}

[ VLAN Name TLV                    YES       YES]{lang="EN-US"}

[ DCBX TLV                         NO        NO]{lang="EN-US"}

[ EVB TLV                          NO        NO]{lang="EN-US"}

[ Link Aggregation TLV             YES       NO]{lang="EN-US"}

[ Management VID TLV               YES       YES]{lang="EN-US"}

[IEEE 802.3 extend TLV:]{lang="EN-US"}

[ MAC-Physic TLV                   YES       NO]{lang="EN-US"}

[ Power via MDI TLV                YES       NO]{lang="EN-US"}

[ Maximum Frame Size TLV           YES       NO]{lang="EN-US"}

[ Energy-Efficient Ethernet TLV    NO        NO]{lang="EN-US"}

[LLDP-MED extend TLV:]{lang="EN-US"}

[ Capabilities TLV                 YES        YES]{lang="EN-US"}

[ Network Policy TLV               YES        YES]{lang="EN-US"}

[ Location Identification TLV      NO         NO]{lang="EN-US"}

[ Extended Power via MDI TLV       YES        NO]{lang="EN-US"}

[ Inventory TLV                    YES        YES]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x859254117}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x1791352966}
:::

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display lldp tlv-config]{lang="EN-US"}]{#struct_0_x1289_x1771_188832116}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_180291758}[[字段]{style="font-family:黑体"}]{#struct_0_x1289_x1771_382069806}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1289_x1771_46518398}

[[LLDP agent nearest-bridge]{lang="EN-US"}]{#struct_0_x1289_x1771_955598054}

[[LLDP ]{lang="EN-US"}]{#struct_0_x1289_x1771_x576240635}[缺省代理，即最近桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-customer]{lang="EN-US"}]{#struct_0_x1289_x1771_1375601115}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_189159796}[最近客户桥代理]{style="font-family:宋体"}

[[LLDP agent nearest-nontpmr]{lang="EN-US"}]{#struct_0_x1289_x1771_x819278689}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x886671669}[最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理]{style="font-family:宋体"}

[[LLDP tlv-config of port 1]{lang="EN-US"}]{#struct_0_x1289_x1771_x1411466807}

[[端口]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1289_x1771_2102853677}[上可发送的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[NAME]{lang="EN-US"}]{#struct_0_x1289_x1771_681091533}

[[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189225332}[类型]{style="font-family:宋体"}

[[STATUS]{lang="EN-US"}]{#struct_0_x1289_x1771_x1393034468}

[[端口是否配置发布指定类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_966147946}

[[DEFAULT]{lang="EN-US"}]{#struct_0_x1289_x1771_583352496}

[[端口发布指定类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_123613714}[的缺省情况]{style="font-family:宋体"}

[[Basic optional TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189028724}

[[端口可以发送的基本]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1880214926}[类型]{style="font-family:宋体"}

[[Port Description TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1350388254}

[[端口描述]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x201799159}

[[System Name TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189094260}

[[系统名称]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1492872784}

[[System Description TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x203854217}

[[系统描述]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1999125423}

[[System Capabilities TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_2011788306}

[[系统能力集]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189421940}

[[Management Address TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_2028617596}

[[管理地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x583421185}

[[Congestion notification TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1172213604}

[[拥塞通知]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1172148068}[。本字段的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[IEEE 802.1 extended TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1334789748}

[[端口可发送的]{style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}]{#struct_0_x1289_x1771_189487476}[组织定义的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Port VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_792734231}

[[端口]{style="font-family:宋体"}[VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x518454480}

[[Port And Protocol VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1067080432}

[[协议]{style="font-family:宋体"}[VLAN ID TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_188897649}

[[VLAN Name TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1138570}

[[VLAN]{lang="EN-US"}]{#struct_0_x1289_x1771_x1590098597}[名称]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[DCBX TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1770903029}

[[DCBX]{lang="EN-US"}]{#struct_0_x1289_x1771_188963185}[（]{style="font-family:宋体"}[Data Center Bridging Exchange Protocol]{lang="EN-US"}[，数据中心桥能力交换协议）]{style="font-family:宋体"}[ TLV]{lang="EN-US"}[。本字段的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[EVB TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_358935494}

[[EVB]{lang="EN-US"}]{#struct_0_x1289_x1771_923615478}[（]{style="font-family:宋体"}[Edge Virtual Bridging]{lang="EN-US"}[，边缘虚拟桥接）模块]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。本字段的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Management VID TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x2007736160}

[[管理]{style="font-family:宋体"}[VLAN TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_188766577}

[[IEEE 802.3 extended TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1355595312}

[[端口可发送的]{style="font-family:宋体"}[IEEE 802.3]{lang="EN-US"}]{#struct_0_x1289_x1771_x1576608408}[组织定义的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[MAC-Physic TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_188832113}

[[端口物理属性]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_382069811}

[[Power via MDI TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1909796745}

[[供电能力]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_818311324}

[[Link Aggregation TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189159793}

[[链路聚合]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x819278684}

[[Maximum Frame Size TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x886475061}

[[最大帧长度]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189225329}

[[LLDP-MED extend TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_563280661}

[[LLDP-MED TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1232529031}

[[Capabilities TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1715292162}

[[MED]{lang="EN-US"}]{#struct_0_x1289_x1771_189028721}[能力集]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Network Policy TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1880214921}

[[网络策略]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1350584862}

[[Location Identification TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189094257}

[[位置标识]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x81105325}

[[Extended Power via MDI TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1474726941}

[[扩展供电能力]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189421937}

[[Inventory TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1074708611}

[[资产信息]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_542803919}[，包括以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware Revision TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_189487473}[：终端设备硬件版本]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Firmware Revision TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_792734226}[：终端设备固件版本]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Software Revision TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1820197681}[：终端设备软件版本]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Serial Number TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_188897650}[：终端设备序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Manufacturer Name TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1955176575}[：终端设备的制造厂商名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Model name TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_1223962425}[：终端设备的模块名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Asset ID TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_188963186}[：终端设备的资产标识符，以便目录管理和资产跟踪]{style="font-family:宋体"}

[[Energy-Efficient Ethernet TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x858664293}

[[节能以太网]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x628023194}[。本字段的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-71100106 .myid}
[]{#_Toc404784697}[]{#struct_0_x1289_x1771_358935493}[]{#_Toc144347676}

**LLDP \-- LLDP配置命令 \-- lldp admin-status**

------------------------------------------------------------------------

[**[lldp admin-status]{lang="EN-US"}**]{#struct_0_x1289_x1771_923615483}[命令用来配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[的工作模式。]{style="font-family:宋体"}

[**[undo lldp admin-status]{lang="EN-US"}**]{#struct_0_x1289_x1771_1567187095}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1598194656}

[[在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_1080830716}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下：]{style="font-family:宋体"}

[**[lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **admin-status** { **disable** \| **rx** \| **tx** \| **txrx** }]{lang="EN-US"}]{#struct_0_x1289_x1771_x1100777879}

[**[undo lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **admin-status**]{lang="EN-US"}]{#struct_0_x1289_x1771_188766578}

[[在二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_1355595327}[三层聚合接口视图下：]{style="font-family:宋体"}

[**[lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **admin-status** { **disable** \| **rx** \| **tx** \| **txrx** }]{lang="EN-US"}]{#struct_0_x1289_x1771_x1576936091}

[**[undo lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **admin-status**]{lang="EN-US"}]{#struct_0_x1289_x1771_10665185}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1755619124}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_453006601}[最近桥代理的工作模式为]{style="font-family:宋体"}[TxRx]{lang="EN-US"}[，既发送也接收]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文。其他类型的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的工作模式为]{style="font-family:宋体"}[Disable]{lang="EN-US"}[，即不发送也不接收]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1172039968}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_1669320389}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x1586736154}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_188832114}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_382069804}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_46518396}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_2102609126}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_641478940}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_x619833642}[：配置指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的工作模式。在以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下，未指定时表示配置最近桥代理的工作模式。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1755876021}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_x823101522}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[**[disable]{lang="EN-US"}**]{#struct_0_x1289_x1771_189159794}[：表示工作模式为]{style="font-family:宋体"}[Disable]{lang="EN-US"}[，既不发送也不接收]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[rx]{lang="EN-US"}**]{#struct_0_x1289_x1771_x819278687}[：表示工作模式为]{style="font-family:宋体"}[Rx]{lang="EN-US"}[，只接收不发送]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[tx]{lang="EN-US"}**]{#struct_0_x1289_x1771_x886540597}[：表示工作模式为]{style="font-family:宋体"}[Tx]{lang="EN-US"}[，只发送不接收]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[txrx]{lang="EN-US"}**]{#struct_0_x1289_x1771_2108900564}[：表示工作模式为]{style="font-family:宋体"}[TxRx]{lang="EN-US"}[，既发送也接收]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2074536422}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x385803475}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上最近客户桥代理]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[的工作模式为]{style="font-family:宋体"}[Rx]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_1011929296}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp agent nearest-customer admin-status rx]{lang="EN-US"}
:::::

::::: {#1145925097 .myid}
[]{#_Toc404784698}[]{#struct_0_x1289_x1771_189225330}[]{#_Toc144347677}[]{#_Toc345180593}[]{#_Toc345180594}[]{#_Toc345180595}[]{#_Toc345180596}[]{#_Toc345180597}[]{#_Toc345180598}[]{#_Toc345180599}[]{#_Toc345180600}[]{#_Toc345180601}[]{#_Toc345180602}[]{#_Toc345180603}[]{#_Toc345180604}[]{#_Toc345180605}[]{#_Toc345180606}[]{#_Toc345180607}[]{#_Toc345180608}[]{#_Toc345180609}[]{#_Toc345180610}[]{#_Toc345180611}[]{#_Toc345180612}[]{#_Toc345180613}[]{#_Toc345180614}[]{#_Toc345180615}

**LLDP \-- LLDP配置命令 \-- lldp check-change-interval**

------------------------------------------------------------------------

[**[lldp check-change-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1393034466}[命令用来开启轮询功能并配置轮询间隔。]{style="font-family:
宋体"}

[**[undo lldp check-change-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_515809252}[命令用来关闭轮询功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1774070489}

[[在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_555955454}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下：]{style="font-family:宋体"}

[**[lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **check-change-interval** *interval*]{lang="EN-US"}]{#struct_0_x1289_x1771_753418761}

[**[undo lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **check-change-interval**]{lang="EN-US"}]{#struct_0_x1289_x1771_1281662371}

[[在二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x473461261}[三层聚合接口视图下：]{style="font-family:宋体"}

[**[lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **check-change-interval** *interval*]{lang="EN-US"}]{#struct_0_x1289_x1771_1865846250}

[**[undo lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **check-change-interval**]{lang="EN-US"}]{#struct_0_x1289_x1771_189028722}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1880214920}

[[轮询功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1350519326}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x581741399}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x1216693842}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_173961724}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x1491028221}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1952696599}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_189094258}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x81105320}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1474726936}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_2005392461}[：配置指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的轮询功能。在以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下，未指定时表示配置最近桥代理的轮询功能。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_356724110}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_95403938}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[*[interval]{lang="EN-US"}*]{#struct_0_x1289_x1771_x1491419031}[：表示轮询间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1761763026}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_189421938}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的最近客户桥代理上开启轮询功能，并配置轮询间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x1074708620}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp agent nearest-customer check-change-interval 30]{lang="EN-US"}
:::::

::::::: {#-738009646 .myid}
[]{#_Toc144347678}[]{#_Toc404784699}[]{#struct_0_x1289_x1771_2108822324}

**LLDP \-- LLDP配置命令 \-- lldp compliance admin-status cdp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_1443769645}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x1166779156}
:::

[ ]{lang="EN-US"}

[**[lldp compliance admin-status cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_1702757991}[命令用来配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能的工作模式。]{style="font-family:宋体"}

[**[undo lldp compliance admin-status cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_x522616480}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1305876587}

[**[lldp compliance admin-status cdp]{lang="EN-US"}**[ { **disable** \| **txrx** }]{lang="EN-US"}]{#struct_0_x1289_x1771_189487474}

[**[undo lldp compliance admin-status cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_792734229}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1820197688}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_109887262}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能的工作模式为]{style="font-family:宋体"}[Disable]{lang="EN-US"}[，既不发送也不接收]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1904578959}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_1639443877}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x2089318096}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_1134301713}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111211954}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x975273020}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x49514890}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_128090314}

[**[disable]{lang="EN-US"}**]{#struct_0_x1289_x1771_1472659892}[：表示工作模式为]{style="font-family:宋体"}[Disable]{lang="EN-US"}[，既不发送也不接收]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[txrx]{lang="EN-US"}**]{#struct_0_x1289_x1771_x418899111}[：表示工作模式为]{style="font-family:宋体"}[TxRx]{lang="EN-US"}[，既发送也接收]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1821180765}

[[欲使]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_2043163587}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[的功能生效，必须先开启]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能，同时将]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能的工作模式配置为]{style="font-family:宋体"}[TxRx]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x79379871}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_2111277490}[开启]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能的工作模式为]{style="font-family:宋体"}[TxRx]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x1008702202}

[\[Sysname\] lldp compliance cdp]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp compliance admin-status cdp txrx]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1038911567}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp compliance cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_720609115}
:::::::

::::: {#1415279429 .myid}
[]{#_Toc404784700}[]{#struct_0_x1289_x1771_869433090}

**LLDP \-- LLDP配置命令 \-- lldp compliance cdp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x62229866}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x1032608377}
:::

[ ]{lang="EN-US"}

[**[lldp compliance cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111080882}[命令用来开启]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo lldp compliance cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_x214042468}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_745072769}

[**[lldp compliance cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_1126554242}

[**[undo lldp compliance cdp]{lang="EN-US"}**]{#struct_0_x1289_x1771_2102616269}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1050738915}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1353369993}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1048291990}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_2111146418}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1722737016}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_357809890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_11896748}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x949798369}

[[由于]{style="font-family:宋体"}[CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x220350905}[报文所携]{style="font-family:宋体"}[Time To Live TLV]{lang="EN-US"}[中]{style="font-family:宋体"}[TTL]{lang="EN-US"}[的最大值为]{style="font-family:宋体"}[255]{lang="EN-US"}[，而]{style="font-family:宋体"}[CDP]{lang="EN-US"}[报文的发送间隔由]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的发送间隔控制，因此为保证]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能的正常运行，建议配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的发送间隔值不大于实际]{style="font-family:宋体"}[TTL]{lang="EN-US"}[的]{style="font-family:宋体"}[1/3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x172097289}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_1088178330}[开启]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[兼容]{style="font-family:宋体"}[CDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_2111474098}

[\[Sysname\] lldp compliance cdp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x646788211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp hold-multiplier]{lang="EN-US"}**]{#struct_0_x1289_x1771_x20072889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp timer tx-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1860135322}
:::::

::::: {#-928948148 .myid}
[]{#_Toc404784701}[]{#struct_0_x1289_x1771_x763475090}

**LLDP \-- LLDP配置命令 \-- lldp enable**

------------------------------------------------------------------------

[**[lldp enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_x236361645}[命令用来在接口上开启]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo lldp enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_x449745509}[命令用来在接口上关闭]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1902136416}

[**[lldp enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_1898172341}

[**[undo lldp enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111539634}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1424021247}

[[接口上的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_933592014}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x902876144}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x785982696}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 7 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x1603249121}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x618236506}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_176208688}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_2111343026}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1726978610}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_823580559}

[[只有当全局和接口上都开启了]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x683612002}[功能后，该功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1467374581}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x865917357}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上关闭]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_394875363}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#_Toc144348964}

[\[Sysname-GigabitEthernet1/0/1\] undo lldp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_988399323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp global enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111408562}
:::::

::::: {#1250753595 .myid}
[]{#_Toc404784702}[]{#struct_0_x1289_x1771_x1414488578}

**LLDP \-- LLDP配置命令 \-- lldp encapsulation snap**

------------------------------------------------------------------------

[**[lldp encapsulation snap]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1463264558}[命令用来配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的封装格式为]{style="font-family:宋体"}[SNAP]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[**[undo lldp encapsulation]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1988451020}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_821134379}

[[在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x929709755}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下：]{style="font-family:宋体"}

[**[lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **encapsulation snap**]{lang="EN-US"}]{#struct_0_x1289_x1771_2007767787}

[**[undo lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **encapsulation**]{lang="EN-US"}]{#struct_0_x1289_x1771_1434744083}

[[在二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_2111736242}[三层聚合接口视图下：]{style="font-family:宋体"}

[**[lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **encapsulation snap**]{lang="EN-US"}]{#struct_0_x1289_x1771_x1419255361}

[**[undo lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **encapsulation**]{lang="EN-US"}]{#struct_0_x1289_x1771_648757197}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_938593724}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1349716936}[报文的封装格式为]{style="font-family:宋体"}[Ethernet II]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1309140619}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x1678331958}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 8 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x1082402380}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_2111801778}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_177308424}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x2012215434}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_845150780}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1532562968}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_x2061697621}[：配置指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的封装格式。在以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下，未指定时表示配置最近桥代理的封装格式。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_1064176797}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_1042222920}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1200137504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LLDP CDP]{lang="EN-US"}]{#struct_0_x1289_x1771_2111211955}[报文的封装格式只能为]{lang="EN-US" style="font-family:宋体"}[SNAP]{lang="EN-US"}[格式，不能为]{lang="EN-US" style="font-family:宋体"}[Ethernet II]{lang="EN-US"}[格式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[携带]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x975338556}[EVB]{lang="EN-US"}[模块]{style="font-family:宋体"}[TLV]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文不能通过]{style="font-family:宋体"}[SNAP]{lang="EN-US"}[格式封装和发送。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x406954677}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x843398098}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发送的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的封装格式为]{style="font-family:宋体"}[SNAP]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_816494030}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp encapsulation snap]{lang="EN-US"}
:::::

::: {#1385165723 .myid}
[]{#_Toc404784703}[]{#struct_0_x1289_x1771_877883004}

**LLDP \-- LLDP配置命令 \-- lldp fast-count**

------------------------------------------------------------------------

[**[lldp fast-count]{lang="EN-US"}**]{#struct_0_x1289_x1771_665341851}[命令用来配置快速发送]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的个数。]{style="font-family:宋体"}

[**[undo lldp fast-count]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111277491}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1008767738}

[**[lldp fast-count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_x1289_x1771_351491042}

[**[undo lldp fast-count]{lang="EN-US"}**]{#struct_0_x1289_x1771_1558182809}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1442528187}

[[快速发送]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1562568723}[报文的个数为]{style="font-family:宋体"}[4]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x6640046}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1435636975}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_767896476}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_2111080883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x213976932}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1043874761}

[*[count]{lang="EN-US"}*]{#struct_0_x1289_x1771_420172165}[：表示快速发送]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[，单位为个。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1851423766}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_290297890}[配置快速发送]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_1170193144}

[\[Sysname\] lldp fast-count 5]{lang="EN-US"}
:::

::: {#1075645974 .myid}
[]{#_Toc144363257}[]{#_Toc144348965}[]{#_Toc404784704}[]{#struct_0_x1289_x1771_450931079}

**LLDP \-- LLDP配置命令 \-- lldp global enable**

------------------------------------------------------------------------

[**[lldp global enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111146419}[命令用来全局开启]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo lldp global enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_1722802552}[命令用来全局关闭]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1538923538}

[**[lldp global enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_1394051215}

[**[undo lldp global enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_387048465}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1606025080}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1289_x1771_593521384}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1013024528}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_895431449}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111474099}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x646853747}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_28613938}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1367253372}

[[只有当全局和接口上都开启了]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1015263712}[功能后，该功能才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1276880789}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x254004217}[全局关闭]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x2120933576}

[\[Sysname\] undo lldp global enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111539635}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1424086783}
:::

::: {#1701684818 .myid}
[]{#_Toc404784705}[]{#struct_0_x1289_x1771_258878103}

**LLDP \-- LLDP配置命令 \-- lldp hold-multiplier**

------------------------------------------------------------------------

[**[lldp hold-multiplier]{lang="EN-US"}**]{#struct_0_x1289_x1771_1328406383}[命令用来配置]{style="font-family:宋体"}[TTL]{lang="EN-US"}[乘数。]{style="font-family:宋体"}

[**[undo lldp hold-multiplier]{lang="EN-US"}**]{#struct_0_x1289_x1771_1014843950}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1796954545}

[**[lldp hold-multiplier ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1289_x1771_x1196569793}

[**[undo lldp hold-multiplier]{lang="EN-US"}**]{#struct_0_x1289_x1771_1462375736}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111343027}

[[TTL]{lang="EN-US"}]{#struct_0_x1289_x1771_1727044146}[乘数为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x255958665}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1431922752}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2121481653}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_307851746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1306817519}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1695448910}

[*[value]{lang="EN-US"}*]{#struct_0_x1289_x1771_x806032757}[：表示]{style="font-family:宋体"}[TTL]{lang="EN-US"}[乘数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111408563}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_2111736243}[报文所携]{style="font-family:宋体"}[Time To Live TLV]{lang="EN-US"}[中]{style="font-family:宋体"}[TTL]{lang="EN-US"}[的值用来设置邻居信息在本地设备上的老化时间，由于]{style="font-family:宋体"}[TTL]{lang="EN-US"}[＝]{style="font-family:宋体"}[Min]{lang="EN-US"}[（]{style="font-family:宋体"}[65535]{lang="EN-US"}[，（]{style="font-family:宋体"}[TTL]{lang="EN-US"}[乘数×]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的发送间隔＋]{style="font-family:宋体"}[1]{lang="EN-US"}[）），即取]{style="font-family:宋体"}[65535]{lang="EN-US"}[与（]{style="font-family:宋体"}[TTL]{lang="EN-US"}[乘数×]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的发送间隔＋]{style="font-family:宋体"}[1]{lang="EN-US"}[）中的最小值，因此通过调整]{style="font-family:宋体"}[TTL]{lang="EN-US"}[乘数可以控制本设备信息在邻居设备上的老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1419320897}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_2111801779}[配置]{style="font-family:宋体"}[TTL]{lang="EN-US"}[乘数为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_177373960}

[\[Sysname\] lldp hold-multiplier 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1907890994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp timer tx-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_537862889}
:::

::: {#346521027 .myid}
[]{#_Toc404784706}[]{#struct_0_x1289_x1771_x1402803866}[]{#_Toc385951286}[]{#_Toc385238235}

**LLDP \-- LLDP配置命令 \-- lldp management-address**

------------------------------------------------------------------------

[**[lldp management-address]{lang="EN-US"}**]{#struct_0_x1289_x1771_1770551031}[命令用来配置接口收到]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文后下发]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项或]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[undo lldp management-address]{lang="EN-US"}**]{#struct_0_x1289_x1771_826654665}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x403167059}

[**[lldp management-address]{lang="EN-US"}**[ { **arp-learning** \| **nd-learning** } \[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1289_x1771_2124719149}

[**[undo lldp ]{lang="EN-US"}[management-address]{lang="EN-US"}**[ { **arp-learning** \| **nd-learning** }]{lang="EN-US"}]{#struct_0_x1289_x1771_619856055}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2135215666}

[[接口收到]{style="font-family:宋体"}[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_1967505739}[报文后不下发]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项和]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2050005551}

[[三层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1008259470}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1402869402}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1230462399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1705823405}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1832079802}

[**[arp-learning]{lang="EN-US"}**]{#struct_0_x1289_x1771_1775909470}[：表示接口收到携带]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[格式]{style="font-family:宋体"}[Management Address TLV]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文后，会下发该报文携带的管理地址与报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址组成的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[nd-learning]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1727325583}[：表示接口收到携带]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[格式]{style="font-family:宋体"}[Management Address TLV]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文后，会下发该报文携带的管理地址与报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址组成的]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x1289_x1771_302539672}[：指定]{style="font-family:宋体"}[Dot1q]{lang="EN-US"}[终结中三层以太网子接口关联的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1\~4094]{lang="EN-US"}[。指定该参数后，下发]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项或]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项到该]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[关联的三层以太网子接口；如果该]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[没有关联的三层以太网子接口，则将对应表项下发到当前接口。不指定该参数时表示将对应表项下发到当前接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1880931899}

[[ARP]{lang="EN-US"}]{#struct_0_x1289_x1771_792902999}[表项和]{style="font-family:宋体"}[ND]{lang="EN-US"}[表项下发互不影响，可同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x368364588}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x735120553}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到携带]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[格式]{style="font-family:宋体"}[Management Address TLV]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文后，下发]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项到]{style="font-family:宋体"}[Dot1q]{lang="EN-US"}[终结中]{style="font-family:宋体"}[VLAN 4094]{lang="EN-US"}[关联的三层以太网子接口上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x420617718}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp management-address arp-learning vlan 4094]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1641909502}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp source-mac vlan]{lang="EN-US"}**]{#struct_0_x1289_x1771_x772383711}
:::

::::: {#1441681564 .myid}
[]{#_Toc144363258}[]{#_Toc144348966}[]{#_Toc404784707}[]{#struct_0_x1289_x1771_2126086120}

**LLDP \-- LLDP配置命令 \-- lldp management-address-format string**

------------------------------------------------------------------------

[**[lldp management-address-format string]{lang="EN-US"}**]{#struct_0_x1289_x1771_924335659}[命令用来配置管理地址在]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中的封装格式为字符串格式。]{style="font-family:宋体"}

[**[undo lldp management-address-format]{lang="EN-US"}**]{#struct_0_x1289_x1771_x978082200}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1898583343}

[[在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_2111211952}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下：]{style="font-family:宋体"}

[**[lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **management-address-format string**]{lang="EN-US"}]{#struct_0_x1289_x1771_x975404092}

[**[undo lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **management-address-format**]{lang="EN-US"}]{#struct_0_x1289_x1771_x452733710}

[[在二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x1765567268}[三层聚合接口视图下：]{style="font-family:宋体"}

[**[lldp]{lang="EN-US"}[ agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **management-address-format string**]{lang="EN-US"}]{#struct_0_x1289_x1771_x474294620}

[**[undo lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **management-address-format**]{lang="EN-US"}]{#struct_0_x1289_x1771_x1444752313}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x539470284}

[[管理地址在]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1739398502}[中的封装格式为数字格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111277488}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x1008177915}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x827054890}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_456470015}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_983383858}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_806672507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_162968658}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_937839215}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111080880}[：配置指定]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理类型管理地址在]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中的封装格式。在以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下，未指定时表示配置最近桥代理的管理地址在]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中的封装格式。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_x213911396}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_510746224}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x720491976}

[[如果邻居将管理地址以字符串格式封装在]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_2083485177}[中，用户可在本地设备上也将封装格式改为字符串，以保证与邻居设备的正常通信。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1464185467}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_357800630}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的最近客户桥代理上配置管理地址在]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中的封装格式为字符串格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_1964304422}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="EN-US"}[lldp agent nearest-customer management-address-format string]{lang="EN-US"}
:::::

::: {#1929990489 .myid}
[]{#struct_0_x1289_x1771_2111146416}[]{#_Toc404784708}[]{#_Toc340510137}[]{#_Toc333218581}

**LLDP \-- LLDP配置命令 \-- lldp max-credit**

------------------------------------------------------------------------

[**[lldp max-credit]{lang="EN-US"}**]{#struct_0_x1289_x1771_1721819512}[命令用来配置限制发送报文速率的令牌桶大小。]{style="font-family:宋体"}

[**[undo lldp max-credit]{lang="EN-US"}**]{#struct_0_x1289_x1771_x706458549}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1229023683}

[**[lldp max-credit ]{lang="EN-US"}***[credit-value]{lang="EN-US"}*]{#struct_0_x1289_x1771_1183396409}

[**[undo lldp max-credit]{lang="EN-US"}**]{#struct_0_x1289_x1771_460087499}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2121736223}

[[限制发送报文速率的令牌桶大小为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x1289_x1771_x342861913}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1947367828}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_2111474096}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x647705715}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1261286302}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_763760560}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x274353305}

[*[credit-value]{lang="EN-US"}*]{#struct_0_x1289_x1771_683701945}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[发包限速的令牌桶大小，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x573036592}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x1914651339}[配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[发包限速的令牌桶大小为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_2111539632}

[\[Sysname\] lldp max-credit 10]{lang="EN-US"}
:::

::::: {#686093785 .myid}
[]{#_Toc404784709}[]{#struct_0_x1289_x1771_x1424414463}[]{#_Toc340510134}[]{#_Toc333218578}

**LLDP \-- LLDP配置命令 \-- lldp mode**

------------------------------------------------------------------------

[**[lldp mode]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1081444829}[命令用来配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[桥模式。]{style="font-family:宋体"}

[**[undo lldp mode]{lang="EN-US"}**]{#struct_0_x1289_x1771_x206723967}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1800045336}

[**[lldp mode service-bridge]{lang="EN-US"}**]{#struct_0_x1289_x1771_x110795642}

[**[undo lldp mode]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1025101683}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1841032431}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_2111343024}[桥模式为客户桥模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1727109682}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_2059816235}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x728998935}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x123951467}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x802392494}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1686304812}

[**[service-bridge]{lang="EN-US"}**]{#struct_0_x1289_x1771_106553801}[：表示服务桥模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x434393518}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_2111408560}[桥模式命令用于控制设备支持不同的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[工作于服务桥模式时，设备可支持最近桥代理和最近非]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1414357506}[TPMR]{lang="EN-US"}[桥代理，即对上述类型的代理]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文进行处理，其他目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文进行]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内透传。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[工作于客户桥模式时，设备可支持最近桥代理、最近非]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1547563217}[TPMR]{lang="EN-US"}[桥代理及最近客户桥代理，即对上述类型的代理]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文进行处理，其他目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[的]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文进行]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内透传。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 9 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_1271996482}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[桥模式配置只在]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x1037897846}[LLDP]{lang="EN-US"}[全局开启后才能生效，]{style="font-family:KaiTi_GB2312"}[LLDP]{lang="EN-US"}[全局关闭时，只能作为客户桥对三种类型代理]{style="font-family:KaiTi_GB2312"}[MAC]{lang="EN-US"}[的]{style="font-family:KaiTi_GB2312"}[LLDP]{lang="EN-US"}[报文进行拦截。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2091691601}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x1066368712}[配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[桥模式为服务桥模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_2111736240}

[\[Sysname\] lldp mode service-bridge]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1419124289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp global enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_1001184425}
:::::

::::: {#-186219939 .myid}
[]{#_Toc144363259}[]{#_Toc144348967}[]{#_Toc404784710}[]{#struct_0_x1289_x1771_1782380085}[]{#_Toc298833923}[]{#_Toc287965425}[]{#_Toc295980667}[]{#_Toc287965426}[]{#_Toc295980668}[]{#_Toc287965427}[]{#_Toc295980669}[]{#_Toc287965428}[]{#_Toc295980670}[]{#_Toc287965429}[]{#_Toc295980671}[]{#_Toc287965430}[]{#_Toc295980672}[]{#_Toc287965431}[]{#_Toc295980673}[]{#_Toc287965432}[]{#_Toc295980674}[]{#_Toc287965433}[]{#_Toc295980675}[]{#_Toc287965434}[]{#_Toc295980676}[]{#_Toc287965435}[]{#_Toc295980677}[]{#_Toc287965436}[]{#_Toc295980678}[]{#_Toc287965437}[]{#_Toc295980679}[]{#_Toc287965438}[]{#_Toc295980680}[]{#_Toc287965439}[]{#_Toc295980681}[]{#_Toc287965440}[]{#_Toc295980682}[]{#_Toc287965441}[]{#_Toc295980683}[]{#_Toc287965442}[]{#_Toc295980684}[]{#_Toc287965443}[]{#_Toc295980685}[]{#_Toc287965444}[]{#_Toc295980686}[]{#_Toc287965445}[]{#_Toc295980687}[]{#_Toc287965446}[]{#_Toc295980688}[]{#_Toc287965447}[]{#_Toc295980689}[]{#_Toc287965448}[]{#_Toc295980690}[]{#_Toc287965450}[]{#_Toc295980692}

**LLDP \-- LLDP配置命令 \-- lldp notification med-topology-change enable**

------------------------------------------------------------------------

[**[lldp notification med-topology-change enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_1655666572}[命令用来开启]{style="font-family:宋体"}[LLDP-MED Trap]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo lldp notification med-topology-change enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_330656039}[命令用来关闭]{style="font-family:宋体"}[LLDP-MED Trap]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1667425338}

[**[lldp notification med-topology-change enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_x408769900}

[**[undo lldp notification med-topology-change enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1062008072}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111801776}

[[LLDP-MED Trap]{lang="EN-US"}]{#struct_0_x1289_x1771_177963784}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x556762169}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_1690306935}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 10 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_561332738}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_1391159526}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1853177625}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_196408499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_2111211953}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x975469628}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x425137906}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[LLDP-MED Trap]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x2102358982}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp notification med-topology-change enable]{lang="EN-US"}
:::::

::::: {#-1639006138 .myid}
[]{#_Toc404784711}[]{#struct_0_x1289_x1771_134205034}

**LLDP \-- LLDP配置命令 \-- lldp notification remote-change enable**

------------------------------------------------------------------------

[**[lldp notification remote-change enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_1529496538}[命令用来开启]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo lldp notification remote-change enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_869157416}[命令用来关闭]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111277489}

[[在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x1008243451}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下：]{style="font-family:宋体"}

[**[lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **notification remote-change enable**]{lang="EN-US"}]{#struct_0_x1289_x1771_758467172}

[**[undo lldp ]{lang="EN-US"}**[\[ **agent** { **nearest-customer** \| **nearest-nontpmr** } \] **notification remote-change enable**]{lang="EN-US"}]{#struct_0_x1289_x1771_x1083322014}

[[在二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_1494900904}[三层聚合接口视图下：]{style="font-family:宋体"}

[**[lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **notification remote-change enable**]{lang="EN-US"}]{#struct_0_x1289_x1771_76896134}

[**[undo lldp agent ]{lang="EN-US"}**[{ **nearest-customer** \| **nearest-nontpmr** } **notification remote-change enable**]{lang="EN-US"}]{#struct_0_x1289_x1771_285274702}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x970725322}

[[LLDP Trap]{lang="EN-US"}]{#struct_0_x1289_x1771_1754685557}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111080881}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x213845860}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 11 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_x273731344}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_x332296701}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1163327675}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1758364715}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x196128058}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x741113657}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111146417}[：开启指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[功能。在以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下，未指定时表示开启最近桥代理类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理的]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_1721885048}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_x261696246}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1194599124}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_1683764062}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[最近客户桥代理上开启]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_675826038}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp agent nearest-customer notification remote-change enable]{lang="EN-US"}
:::::

::: {#-343440181 .myid}
[]{#_Toc404784712}[]{#struct_0_x1289_x1771_x1806088390}[]{#_Toc385951292}

**LLDP \-- LLDP配置命令 \-- lldp source-mac vlan**

------------------------------------------------------------------------

[**[lldp source-mac vlan]{lang="EN-US"}**]{#struct_0_x1289_x1771_188734882}[命令用来配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[关联三层以太网子接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo lldp source-mac vlan]{lang="EN-US"}**]{#struct_0_x1289_x1771_964219583}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1880097774}

[**[lldp source-mac vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1289_x1771_x978987704}

[**[undo ]{lang="EN-US"}[lldp source-mac vlan]{lang="EN-US"}**]{#struct_0_x1289_x1771_x727627285}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1301318918}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_663406822}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为当前接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_567254123}

[[三层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1705029581}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1643003220}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_697225020}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_839653184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1806153926}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x1289_x1771_x1406372735}[：指定]{style="font-family:宋体"}[Dot1q]{lang="EN-US"}[终结中三层以太网子接口关联的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1\~4094]{lang="EN-US"}[。指定该参数后，]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为该]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[关联的三层以太网子接口；如果该]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[没有关联的三层以太网子接口，则]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为当前接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1905042102}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x519780082}[配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[Dot1q]{lang="EN-US"}[终结中]{style="font-family:宋体"}[VLAN 4094]{lang="EN-US"}[关联的三层以太网子接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x1870015801}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp source-mac vlan 4094]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_805043594}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lldp management-address arp-learning]{lang="EN-US"}**]{#struct_0_x1289_x1771_238352171}
:::

::: {#-1759646567 .myid}
[]{#_Toc404784713}[]{#struct_0_x1289_x1771_x1397487791}[]{#_Toc340510140}[]{#_Toc333218616}

**LLDP \-- LLDP配置命令 \-- lldp timer fast-interval**

------------------------------------------------------------------------

[**[lldp timer fast-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_50996377}[命令用来配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[快速发送报文的时间间隔。]{style="font-family:宋体"}

[**[undo lldp timer fast-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111474097}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x647771251}

[**[lldp timer fast-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1289_x1771_x1888385522}

[**[undo lldp timer fast-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_x317339880}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1139344001}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_117654226}[快速发送报文的时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2038439316}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1455044956}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x661892440}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_2111539633}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1424479999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1687213138}

[*[interval]{lang="EN-US"}*]{#struct_0_x1289_x1771_x1901133033}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[快速发送报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_469338321}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x358160966}[配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[快速发送报文的时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_820244992}

[\[Sysname\] lldp timer fast-interval 2]{lang="EN-US"}
:::

::: {#232210342 .myid}
[]{#_Toc404784714}[]{#struct_0_x1289_x1771_x832743808}[]{#_Toc144363261}[]{#_Toc144348969}

**LLDP \-- LLDP配置命令 \-- lldp timer notification-interval**

------------------------------------------------------------------------

[**[lldp timer notification-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111343025}[命令用来配置]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[LLDP-MED Trap]{lang="EN-US"}[信息的发送间隔。]{style="font-family:宋体"}

[**[undo lldp timer notification-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_1727175218}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_124769774}

[**[lldp timer notification-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1289_x1771_366017673}

[**[undo lldp timer notification-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1423571255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x2073011032}

[[LLDP Trap]{lang="EN-US"}]{#struct_0_x1289_x1771_642668626}[和]{style="font-family:宋体"}[LLDP-MED Trap]{lang="EN-US"}[信息的发送间隔均为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1110823943}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x469371876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111408561}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1414291970}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1439525063}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1216524643}

[*[interval]{lang="EN-US"}*]{#struct_0_x1289_x1771_1961505310}[：表示]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[LLDP-MED Trap]{lang="EN-US"}[信息的发送间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1519543759}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_1849474689}[配置]{style="font-family:宋体"}[LLDP Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[LLDP-MED Trap]{lang="EN-US"}[信息的发送间隔为]{style="font-family:宋体"}[8]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x1142132498}

[\[Sysname\] lldp timer notification-interval 8]{lang="EN-US"}
:::

::: {#571325864 .myid}
[]{#_Toc404784715}[]{#struct_0_x1289_x1771_2111736241}[]{#_Toc144363262}[]{#_Toc144348970}

**LLDP \-- LLDP配置命令 \-- lldp timer reinit-delay**

------------------------------------------------------------------------

[**[lldp timer reinit-delay]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1419189825}[命令用来配置接口初始化的延迟时间。]{style="font-family:宋体"}

[**[undo lldp timer reinit-delay]{lang="EN-US"}**]{#struct_0_x1289_x1771_x2086136779}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1270994702}

[**[lldp timer reinit-delay ]{lang="EN-US"}***[delay]{lang="EN-US"}*]{#struct_0_x1289_x1771_x1028389300}

[**[undo lldp timer reinit-delay]{lang="EN-US"}**]{#struct_0_x1289_x1771_x328278288}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_192456070}

[[接口初始化的延迟时间为]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1289_x1771_x1581698243}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x660732947}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_2111801777}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_178029320}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1728445672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_x1262840044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_583544554}

[*[delay]{lang="EN-US"}*]{#struct_0_x1289_x1771_x47792744}[：接口初始化的延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1200769511}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x328450819}[配置接口初始化的延迟时间为]{style="font-family:宋体"}[4]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_2111211950}

[\[Sysname\] lldp timer reinit-delay 4]{lang="EN-US"}
:::

::: {#1016981977 .myid}
[]{#_Toc404784716}[]{#struct_0_x1289_x1771_x975535164}[]{#_Toc144363264}[]{#_Toc144348972}[]{#_Toc345180632}[]{#_Toc345180633}[]{#_Toc345180634}[]{#_Toc345180635}[]{#_Toc345180636}[]{#_Toc345180637}[]{#_Toc345180638}[]{#_Toc345180639}[]{#_Toc345180640}[]{#_Toc345180641}[]{#_Toc345180642}[]{#_Toc345180643}[]{#_Toc345180644}[]{#_Toc345180645}[]{#_Toc345180646}[]{#_Toc345180647}[]{#_Toc345180648}[]{#_Toc345180649}[]{#_Toc345180650}[]{#_Toc345180651}[]{#_Toc345180652}[]{#_Toc345180653}[]{#_Toc345180654}[]{#_Toc345180655}

**LLDP \-- LLDP配置命令 \-- lldp timer tx-interval**

------------------------------------------------------------------------

[**[lldp timer tx-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1218551757}[命令用来配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的发送间隔。]{style="font-family:宋体"}

[**[undo lldp timer tx-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_x342341634}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1160086923}

[**[lldp timer tx-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1289_x1771_x1616834704}

[**[undo lldp timer tx-interval]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1839909059}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_729416749}

[[LLDP]{lang="EN-US"}]{#struct_0_x1289_x1771_x1398295636}[报文的发送间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_2111277486}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1009095419}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x322183862}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1432641184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_77176902}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1542190236}

[*[interval]{lang="EN-US"}*]{#struct_0_x1289_x1771_x976927817}[：表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的发送间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[32768]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_234965484}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_2111080878}[配置]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文的发送间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x213387093}

[\[Sysname\] lldp timer tx-interval 20]{lang="EN-US"}
:::

::::: {#97394087 .myid}
[]{#_Toc404784717}[]{#struct_0_x1289_x1771_84231904}[]{#_Toc144363265}[]{#_Toc144348973}[]{#_Toc345180657}[]{#_Toc345180658}

**LLDP \-- LLDP配置命令 \-- lldp tlv-enable**

------------------------------------------------------------------------

[**[lldp tlv-enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_577119467}[命令用来配置接口上允许发布的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[undo lldp tlv-enable]{lang="EN-US"}**]{#struct_0_x1289_x1771_2012804684}[命令用来配置接口上禁止发布的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1325151728}

[[在二层以太网接口视图下：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1303094919}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置最近桥代理]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1714488650}[LLDP]{lang="EN-US"}[接口上允许发布的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[**[lldp]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** \| **dcbx** \| **protocol-vlan-id** \[ *vlan-id* \] \| **vlan-name** \[ *vlan-id* \] \| **management-vid** \[ *mvlan-id* \] } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **network-policy** \[ *vlan-id* \] \| **power-over-ethernet** \| **location-id** { **civic-address** *device-type country-code* { *ca-type ca-value* }&\<1-10\> \| **elin-address** *tel-number* } } }]{lang="EN-US"}]{#struct_0_x1289_x1771_2111146414}

[**[undo lldp]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** \| **dcbx** \| **protocol-vlan-id** \| **vlan-name** \| **management-vid** } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **network-policy** \[ *vlan-id* \] \| **power-over-ethernet** \| **location-id** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_1721950584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置最近非]{style="font-family:宋体"}]{#struct_0_x1289_x1771_496710336}[TPMR]{lang="EN-US"}[代理]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[接口上允许发布的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[**[lldp agent nearest-nontpmr tlv-enable]{lang="EN-US"}**[ { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **congestion-notification** \| **evb** \| **port-vlan-id** \| **link-aggregation** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_1654430775}

[**[undo lldp agent nearest-nontpmr tlv-enable]{lang="EN-US"}**[ { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **congestion-notification** \| **evb** \| **port-vlan-id** \| **link-aggregation** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_x1270143861}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置最近客户桥代理]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1858237863}[LLDP]{lang="EN-US"}[接口上允许发布的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型]{style="font-family:宋体"}

[**[lldp agent nearest-customer]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_1699738904}

[**[undo lldp agent nearest-customer]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **congestion-notification** \| **port-vlan-id** \| **link-aggregation** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_2111474094}

[[在三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x647574643}[管理以太网接口视图下：]{style="font-family:宋体"}

[**[lldp]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \| **interface** **loopback** *interface-number* \] } \| **dot1-tlv** { **all** \| **link-aggregation** } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **power-over-ethernet** \| **location-id** { **civic-address** *device-type country-code* { *ca-type ca-value* }&\<1-10\> \| **elin-address** *tel-number* } } }]{lang="EN-US"}]{#struct_0_x1289_x1771_882523846}

[**[lldp agent]{lang="EN-US"}**[ { **nearest-nontpmr** \| **nearest-customer** } **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **link-aggregation** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_2109141633}

[**[undo lldp]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \| **interface** **loopback** *interface-number* \] } \| **dot1-tlv** { **all** \| **link-aggregation** } \| **dot3-tlv** { **all** \| **mac-physic** \| **max-frame-size** \| **power** \| **eee** } \| **med-tlv** { **all** \| **capability** \| **inventory** \| **power-over-ethernet** \| **location-id** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_x526939232}

[**[undo lldp agent]{lang="EN-US"}**[ { **nearest-nontpmr** \| **nearest-customer** } **tlv-enable** { **basic-tlv** { **all** \| **port-description** \| **system-capability** \| **system-description** \| **system-name** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] } \| **dot1-tlv** { **all** \| **link-aggregation** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_x1349379280}

[[在二层聚合接口视图下：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x620051178}

[**[lldp agent nearest-nontpmr tlv-enable]{lang="EN-US"}**[ { **basic-tlv** { **all** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **evb** \| **port-vlan-id** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_2111539630}

[**[lldp agent nearest-customer]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **port-vlan-id** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_x1424283391}

[**[lldp tlv-enable]{lang="EN-US"}**[ **dot1-tlv** { **protocol-vlan-id** \[ *vlan-id* \] \| **vlan-name** \[ *vlan-id* \] \| **management-vid** \[ *mvlan-id* \] }]{lang="EN-US"}]{#struct_0_x1289_x1771_x1568980643}

[**[undo lldp agent nearest-nontpmr tlv-enable]{lang="EN-US"}**[ { **basic-tlv** { **all** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **evb** \| **port-vlan-id** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_946197982}

[**[undo lldp agent nearest-customer]{lang="EN-US"}**[ **tlv-enable** { **basic-tlv** { **all** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] \| **port-description** \| **system-capability** \| **system-description** \| **system-name** } \| **dot1-tlv** { **all** \| **port-vlan-id** } }]{lang="EN-US"}]{#struct_0_x1289_x1771_x47234434}

[**[undo lldp tlv-enable]{lang="EN-US"}**[ **dot1-tlv** { **protocol-vlan-id** \| **vlan-name** \| **management-vid** } ]{lang="EN-US"}]{#struct_0_x1289_x1771_650957966}

[[在三层聚合接口视图下：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x439804148}

[**[lldp agent]{lang="EN-US"}**[ { **nearest-customer** \| **nearest-nontpmr** } **tlv-enable basic-tlv** { **all** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] \| **port-description** \| **system-capability** \| **system-description** \| **system-name** }]{lang="EN-US"}]{#struct_0_x1289_x1771_2007371943}

[**[undo lldp agent]{lang="EN-US"}**[ { **nearest-customer** \| **nearest-nontpmr** } **tlv-enable** **basic-tlv** { **all** \| **management-address-tlv** \[ **ipv6** \] \[ *ip-address* \] \| **port-description** \| **system-capability** \| **system-description** \| **system-name** }]{lang="EN-US"}]{#struct_0_x1289_x1771_2111343022}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1727240754}

[[二层以太网接口上：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_922498086}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近桥代理允许发布除]{lang="EN-US" style="font-family:宋体"}[DCBX TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1984736557}[、]{lang="EN-US" style="font-family:宋体"}[Location-id TLV]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Port And Protocol VLAN ID TLV]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VLAN Name TLV]{lang="EN-US"}[、]{style="font-family:宋体"}[Management VLAN ID TLV]{lang="EN-US"}[和]{style="font-family:宋体"}[EEE TLV]{lang="EN-US"}[之外所有类型的]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近非]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1833018429}[TPMR]{lang="EN-US"}[桥代理只允许发布]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近客户桥代理允许发布基本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1209348644}[TLV]{lang="EN-US"}[和]{style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[[三层以太网接口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x1443143640}[管理以太网接口上：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近桥代理允许发布除]{lang="EN-US" style="font-family:宋体"}[Network Policy TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x648504392}[和]{style="font-family:宋体"}[EEE TLV]{lang="EN-US"}[之外所有类型的]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[，其中]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义的]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[只支持]{lang="EN-US" style="font-family:宋体"}[Link Aggregation TLV]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近非]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x506052919}[TPMR]{lang="EN-US"}[桥代理不发布任何]{style="font-family:宋体"}[TLV]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近客户桥代理允许发布基本]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_2111408558}[和]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[，其中]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义的]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[只支持]{lang="EN-US" style="font-family:宋体"}[Link Aggregation TLV]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[二层聚合接口上：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1414881795}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不存在最近桥代理；]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1289_x1771_1127224269}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近非]{style="font-family:宋体"}]{#struct_0_x1289_x1771_2140692920}[TPMR]{lang="EN-US"}[桥代理只允许发布]{style="font-family:宋体"}[EVB TLV]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近客户桥代理允许发布基本]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x1289_x1771_x1697034657}[和]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[，其中]{lang="EN-US" style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义的]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[只支持]{lang="EN-US" style="font-family:宋体"}[Port And Protocol VLAN ID TLV]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VLAN Name TLV]{lang="EN-US"}[及]{lang="EN-US" style="font-family:宋体"}[Management VLAN ID TLV]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[三层聚合接口上：]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1253916032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不存在最近桥代理；]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1289_x1771_966736244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近非]{style="font-family:宋体"}]{#struct_0_x1289_x1771_174676784}[TPMR]{lang="EN-US"}[桥代理不发布任何]{style="font-family:宋体"}[TLV]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最近客户桥代理只允许发布基本]{style="font-family:宋体"}]{#struct_0_x1289_x1771_2111736238}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x1419648580}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1289_x1771_x101213067}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](LLDP命令.files/image001.png){#图片 12 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1289_x1771_1588821023}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1289_x1771_1353378566}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x326252022}

[[network-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_787999210}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1289_x1771_1439172000}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x753729998}

[**[agent]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111801774}[：配置指定类型]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[代理允许发布的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型。在以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下，未指定时表示配置最近桥代理允许发布的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[nearest-customer]{lang="EN-US"}**]{#struct_0_x1289_x1771_178094856}[：表示最近客户桥代理。]{style="font-family:宋体"}

[**[nearest-nontpmr]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1718234760}[：表示最近非]{style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x1289_x1771_2125177908}[：在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下指定]{style="font-family:宋体"}**[basic-tlv]{lang="EN-US"}**[、]{style="font-family:宋体"}**[dot1-tlv]{lang="EN-US"}**[或]{style="font-family:宋体"}**[dot3-tlv]{lang="EN-US"}**[，或者在三层聚合接口视图下指定]{style="font-family:宋体"}**[basic-tlv]{lang="EN-US"}**[时，本参数表示该类型下所有的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[；而在二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下指定]{style="font-family:宋体"}**[med-tlv]{lang="EN-US"}**[时，本参数都表示该类型下除]{style="font-family:宋体"}**[location-id]{lang="EN-US"}**[以外所有的可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[basic-tlv]{lang="EN-US"}**]{#struct_0_x1289_x1771_x2030063005}[：表示基本类型]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[management-address-tlv]{lang="EN-US"}**[ \[ **ipv6** \] \[ *ip-address* \| **interface** **loopback** *interface-number* \]]{lang="EN-US"}]{#struct_0_x1289_x1771_x604871010}[：表示]{style="font-family:宋体"}[Management Address TLV]{lang="EN-US"}[。其中，]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文中所要发布的管理地址为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[格式的地址，当未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[时，表示]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文中所要发布的管理地址为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[格式的地址。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示在]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文中发布的管理地址为指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[ **loopback** *interface-number*]{lang="EN-US"}[表示在]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[报文中发布的管理地址为指定的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。其缺省值根据当前接口视图确定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x1993251199}[/]{lang="EN-US"}[二层聚合接口视图下：]{style="font-family:宋体"}

[[当未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1168657532}[参数时，若未指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，则发布的管理地址为当前接口允许通过的、对应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口上配置有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址且处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的最小]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的主]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址（如果当前接口允许通过的所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口上都未配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或均处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，则发布当前接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）；]{style="font-family:宋体"}

[[当指定了]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x1289_x1771_2125243444}[参数时，若未指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，则发布的管理地址为当前接口允许通过的、对应]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口上配置有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址且处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的最小]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的主]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（如果当前接口允许通过的所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[所对应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口上都未配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或均处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，则发布当前接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在三层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_634488042}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下：]{style="font-family:宋体"}

[[当未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x1289_x1771_x182835365}[参数时，若未指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}[、]{style="font-family:宋体"}*[指定的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口不存在或]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口没有配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，则发布的管理地址为当前接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址（如果当前接口未配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，则发布当前接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）；]{style="font-family:宋体"}

[[当指定了]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x1289_x1771_1250462835}[参数时，若未指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[、指定的]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口不存在或]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，则发布的管理地址为当前接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（如果当前接口未配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，则发布当前接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在二层以太网接口视图]{style="font-family:宋体"}]{#struct_0_x1289_x1771_1649294168}[/]{lang="EN-US"}[二层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理以太网接口视图下：]{style="font-family:宋体"}

[[执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x1289_x1771_260075949}[命令时，如果不带]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[和]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[ **loopback** *interface-number*]{lang="EN-US"}[参数表示不发布该]{style="font-family:宋体"}[TLV]{lang="EN-US"}[；如果带]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[或]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[ **loopback** *interface-number*]{lang="EN-US"}[参数表示按缺省值发布该]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[port-description]{lang="EN-US"}**]{#struct_0_x1289_x1771_x700877023}[：表示]{style="font-family:宋体"}[Port Description TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[system-capability]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1603907656}[：表示]{style="font-family:宋体"}[System Capabilities TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[system-description]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111211951}[：表示]{style="font-family:宋体"}[System Description TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[system-name]{lang="EN-US"}**]{#struct_0_x1289_x1771_x975600700}[：表示]{style="font-family:宋体"}[System Name TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot1-tlv]{lang="EN-US"}**]{#struct_0_x1289_x1771_325124801}[：表示]{style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[congestion-notification]{lang="EN-US"}**]{#struct_0_x1289_x1771_1172410213}[：表示]{style="font-family:宋体"}[QCN]{lang="EN-US"}[（]{style="font-family:宋体"}[Quantized Congestion Notification]{lang="EN-US"}[，量化拥塞通知）模块]{style="font-family:宋体"}[TLV]{lang="EN-US"}[，目前]{style="font-family:宋体"}[QCN]{lang="EN-US"}[模块只支持]{style="font-family:宋体"}[LLDP]{lang="EN-US"}[中三种代理类型中的最近桥代理类型。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[dcbx]{lang="EN-US"}**]{#struct_0_x1289_x1771_1179566372}[：表示]{style="font-family:宋体"}[Data Center Bridging Exchange Protocol TLV]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[evb]{lang="EN-US"}**]{#struct_0_x1289_x1771_x879890431}[：表示]{style="font-family:宋体"}[EVB]{lang="EN-US"}[（]{style="font-family:宋体"}[Edge Virtual Bridging]{lang="EN-US"}[，边缘虚拟桥接）模块]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[port-vlan-id]{lang="EN-US"}**]{#struct_0_x1289_x1771_1851458308}[：表示]{style="font-family:宋体"}[Port VLAN ID TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[protocol-vlan-id]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1289_x1771_x128530075}[：表示]{style="font-family:宋体"}[Port And Protocol VLAN ID TLV]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为所要发布]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，缺省值为该端口所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中最小的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan-name]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1289_x1771_362021180}[：表示]{style="font-family:宋体"}[VLAN Name TLV]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为所要发布]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，缺省值为该端口所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中最小的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[management-vid]{lang="EN-US"}**[ \[ *mvlan-id* \]]{lang="EN-US"}]{#struct_0_x1289_x1771_x57434186}[：表示]{style="font-family:宋体"}[Management VLAN ID TLV]{lang="EN-US"}[。]{style="font-family:宋体"}*[mvlan-id]{lang="EN-US"}*[指定要发布管理]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定该参数，则表示发布]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示当前]{style="font-family:宋体"}[LLDP agent]{lang="EN-US"}[未配置管理]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[link-aggregation]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111277487}[：表示]{style="font-family:宋体"}[Link Aggregation TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot3-tlv]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1009160955}[：表示]{style="font-family:宋体"}[IEEE 802.3]{lang="EN-US"}[组织定义的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[link-aggregation]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1428985872}[：表示]{style="font-family:宋体"}[Link Aggregation TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac-physic]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1196122183}[：表示]{style="font-family:宋体"}[MAC/PHY Configuration/Status TLV]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[max-frame-size]{lang="EN-US"}**]{#struct_0_x1289_x1771_x1590823606}[：表示]{style="font-family:宋体"}[Maximum Frame Size TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[power]{lang="EN-US"}**]{#struct_0_x1289_x1771_970747744}[：表示]{style="font-family:宋体"}[Power Via MDI TLV]{lang="EN-US"}[和]{style="font-family:宋体"}[Power Stateful Control TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[eee]{lang="EN-US"}**]{#struct_0_x1289_x1771_1515364958}[：表示]{style="font-family:宋体"}[Energy-Efficient Ethernet TLV]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[med-tlv]{lang="EN-US"}**]{#struct_0_x1289_x1771_x782328102}[：表示]{style="font-family:宋体"}[LLDP-MED TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[capability]{lang="EN-US"}**]{#struct_0_x1289_x1771_x678453296}[：表示]{style="font-family:宋体"}[LLDP-MED Capabilities TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[inventory]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111080879}[：表示]{style="font-family:宋体"}[Hardware Revision TLV]{lang="EN-US"}[、]{style="font-family:宋体"}[Firmware Revision TLV]{lang="EN-US"}[、]{style="font-family:宋体"}[Software Revision TLV]{lang="EN-US"}[、]{style="font-family:宋体"}[Serial Number TLV]{lang="EN-US"}[、]{style="font-family:宋体"}[Manufacturer Name TLV]{lang="EN-US"}[、]{style="font-family:宋体"}[Model Name TLV]{lang="EN-US"}[和]{style="font-family:宋体"}[Asset ID TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[location-id]{lang="EN-US"}**]{#struct_0_x1289_x1771_x213321557}[：表示]{style="font-family:宋体"}[Location Identification TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[civic-address]{lang="EN-US"}**]{#struct_0_x1289_x1771_1664048550}[：表示]{style="font-family:宋体"}[Location Identification TLV]{lang="EN-US"}[封装网络设备的普通地址信息。]{style="font-family:宋体"}

[*[device-type]{lang="EN-US"}*]{#struct_0_x1289_x1771_1470672632}[：表示设备类型，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示设备类型为]{style="font-family:
宋体"}[DHCP server]{lang="EN-US"}[，]{style="font-family:
宋体"}[1]{lang="EN-US"}[表示设备类型为]{style="font-family:宋体"}[Network device]{lang="EN-US"}[，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示设备类型为]{style="font-family:宋体"}[LLDP-MED Endpoint]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[country-code]{lang="EN-US"}*]{#struct_0_x1289_x1771_x355983880}[：表示国家编码，取值范围请参考]{style="font-family:宋体"}[ISO 3166]{lang="EN-US"}[。]{style="font-family:宋体"}

[[{ *ca-type ca-value* }&\<1-10\>]{lang="EN-US"}]{#struct_0_x1289_x1771_17536293}[：地址信息。]{style="font-family:
宋体"}*[ca-type]{lang="EN-US"}*[表示地址信息类型，取值范围为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[ca-value]{lang="EN-US"}*[表示地址信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[250]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[elin-address]{lang="EN-US"}**]{#struct_0_x1289_x1771_25052559}[：]{style="font-family:宋体"}[Location Identification TLV]{lang="EN-US"}[封装紧急电话号码。]{style="font-family:宋体"}

[*[tel-number]{lang="EN-US"}*]{#struct_0_x1289_x1771_1543330513}[：表示紧急电话号码，为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[个字符的字符串，只能包含数字。]{style="font-family:宋体"}

[**[network-policy]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_x1289_x1771_x2129771529}[：表示]{style="font-family:宋体"}[Network Policy TLV]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为要发布的]{style="font-family:宋体"}[Voice VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[power-over-ethernet]{lang="EN-US"}**]{#struct_0_x1289_x1771_2111146415}[：表示]{style="font-family:宋体"}[Extended Power-via-MDI TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_1722016120}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使用本命令时若不指定]{style="font-family:宋体"}]{#struct_0_x1289_x1771_x28489045}**[all]{lang="EN-US"}**[参数，每次只能配置某类型下的一种可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[，此时可通过多次使用该命令来配置各类型下的多种可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果禁止发布]{lang="EN-US" style="font-family:宋体"}[802.3]{lang="EN-US"}]{#struct_0_x1289_x1771_x1146993303}[的组织定义的]{lang="EN-US" style="font-family:宋体"}[MAC/PHY Configuration/Status TLV]{lang="EN-US"}[，则]{lang="EN-US" style="font-family:宋体"}[LLDP-MED TLV]{lang="EN-US"}[将不会被发布，不论其是否被允许发布；如果禁止发布]{lang="EN-US" style="font-family:宋体"}[LLDP-MED Capabilities TLV]{lang="EN-US"}[，则其它]{lang="EN-US" style="font-family:
宋体"}[LLDP-MED TLV]{lang="EN-US"}[将不会被发布，不论其是否被允许发布。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IEEE 802.1]{lang="EN-US"}]{#struct_0_x1289_x1771_599554725}[组织定义的]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Port And Protocol VLAN ID TLV]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[VLAN Name TLV]{lang="EN-US"}[及]{lang="EN-US" style="font-family:宋体"}[Management VLAN ID TLV]{lang="EN-US"}[只能基于最近桥代理配置，但是其配置会被最近非]{lang="EN-US" style="font-family:宋体"}[TPMR]{lang="EN-US"}[桥代理和最近客户桥代理继承。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1289_x1771_x566248274}

[[\# ]{lang="EN-US"}]{#struct_0_x1289_x1771_x1049330748}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上最近客户桥代理允许发布]{style="font-family:宋体"}[IEEE 802.1]{lang="EN-US"}[组织定义的]{style="font-family:宋体"}[Link Aggregation]{lang="EN-US"}[可选]{style="font-family:宋体"}[TLV]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1289_x1771_x836869488}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] lldp agent nearest-customer tlv-enable dot1-tlv link-aggregation]{lang="EN-US"}
:::::
