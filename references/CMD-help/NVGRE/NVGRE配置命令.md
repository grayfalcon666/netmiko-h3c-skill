<!-- CMD-INDEX
  arp suppression enable              | VSI视图            | L35
  bandwidth                           | VSI虚接口视图         | L87
  default                             | VSI虚接口视图         | L141
  description (VSI view)              | VSI视图            | L179
  description (VSI interface view)    | VSI虚接口视图         | L225
  display arp suppression vsi         | 任意视图             | L273
  display interface vsi-interface     | 任意视图             | L439
  display l2vpn mac-address           | 任意视图             | L709
  display l2vpn service-instance      | 任意视图             | L803
  display l2vpn vsi                   | 任意视图             | L967
  display nvgre tunnel                | 任意视图             | L1269
  encapsulation                       | 以太网服务实例视图        | L1359
  flooding disable                    | VSI视图            | L1453
  gateway vsi-interface               | VSI视图            | L1495
  interface vsi-interface             | 系统视图             | L1547
  l2vpn enable                        | 系统视图             | L1593
  mac-address static                  | 系统视图             | L1633
  mtu                                 | VSI虚接口视图         | L1681
  nvgre                               | VSI视图            | L1723
  reset arp suppression vsi           | 用户视图             | L1775
  reset counters interface vsi-interface | 用户视图             | L1817
  reset l2vpn mac-address             | 用户视图             | L1861
  reset l2vpn statistics vsi          | 用户视图             | L1905
  selective-flooding mac-address      | VSI视图            | L1943
  service-instance                    | 二层以太网接口视图/二层聚合接口视图 | L1993
  shutdown (VSI view)                 | VSI视图            | L2041
  shutdown (VSI interface view)       | VSI虚接口视图         | L2089
  statistics enable                   | VSI视图            | L2127
  tunnel                              | NVGRE网络视图        | L2173
  vsi                                 | 系统视图             | L2233
  xconnect vsi                        | 接口视图/以太网服务实例视图   | L2283
-->

**NVGRE \-- NVGRE配置命令 \-- arp suppression enable**

------------------------------------------------------------------------

![说明](NVGRE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[arp suppression enable**]命令用来开启ARP泛洪抑制功能。

**[undo arp suppression enable**]命令用来恢复缺省情况。

【命令】

**[arp suppression enable**]

**[undo arp suppression enable**]

【缺省情况】

ARP泛洪抑制功能处于关闭状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了避免广播发送的ARP请求报文占用核心网络带宽，NVE从本地站点、NVGRE隧道接收到ARP请求和ARP应答报文后，根据该报文在本地建立ARP泛洪抑制表项。后续当NVE收到本站点内虚拟机请求其它虚拟机MAC地址的ARP请求时，优先根据ARP泛洪抑制表项进行代答。如果没有对应的表项，则将ARP请求泛洪到核心网。ARP泛洪抑制功能可以大大减少ARP泛洪的次数。

【举例】

\# 在VSI vsi1下开启ARP泛洪抑制功能。

\<Sysname\> system-view

Sysname vsi vsi1

Sysname-vsi-vsi1 arp suppression enable

【相关命令】

·**display arp suppression**** vsi**

·**reset arp suppression**** vsi**

**NVGRE \-- NVGRE配置命令 \-- bandwidth**

------------------------------------------------------------------------

![说明](NVGRE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的最大速率÷1000（kbit/s）。

【视图】

VSI虚接口视图

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

\# 配置接口VSI-interface100的期望带宽为10000kbps。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 bandwidth 10000

**NVGRE \-- NVGRE配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将接口VSI-interface100恢复为缺省配置。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 default

This command will restore the default settings. Continue? [Y/N:y]

**NVGRE \-- NVGRE配置命令 \-- description (VSI view)**

------------------------------------------------------------------------

**[description**]命令用来设置VSI的描述信息。

**[undo description**]命令用来删除VSI的描述信息。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

未配置VSI的描述信息。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：VSI的描述信息，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置名为vpn1的VSI的描述信息为"vsi for vpn1"。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 description vsi for vpn1

【相关命令】

·**display l2vpn vsi**

**NVGRE \-- NVGRE配置命令 \-- description (VSI interface view)**

------------------------------------------------------------------------

**[description**]命令用来配置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，例如：Vsi-interface100 Interface。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述字符串，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。

本命令仅用于标识某接口，并无特别的功能。使用**display interface**等命令可以看到设置的描述信息。

【举例】

\# 配置接口VSI-interface100的描述信息为"gateway for NVGRE 5000"。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 description gateway for NVGRE 5000

**NVGRE \-- NVGRE配置命令 \-- display arp suppression vsi**

------------------------------------------------------------------------

![说明](NVGRE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display arp suppression vsi**]命令用来显示VSI的ARP泛洪抑制表项信息。

【命令】

集中式设备：

**[display arp suppression vsi** [ **name** *vsi-name*   **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display arp suppression vsi** [ **name** *vsi-name*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display arp suppression vsi** [ **name** *vsi-name*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** vsi-name*]：显示指定VSI的ARP泛洪抑制表项。如果不指定本参数，则显示所有VSI的ARP泛洪抑制表项。

**[slot** *slot-number*]：显示指定单板的ARP泛洪抑制表项。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的ARP泛洪抑制表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示主设备上的ARP泛洪抑制表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示主设备上的ARP泛洪抑制表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的ARP泛洪抑制表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的ARP泛洪抑制表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的ARP泛洪抑制表项。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示ARP泛洪抑制表项的个数。

【举例】

\# 显示所有VSI的ARP泛洪抑制表项信息。（集中式设备）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示所有VSI的ARP泛洪抑制表项个数。（集中式设备）

\<Sysname\> display arp suppression vsi count

Total entries: 3

\# 显示主用主控板上的ARP泛洪抑制表项信息。（分布式设备－独立运行模式）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示主用主控板上的ARP泛洪抑制表项个数。（分布式设备－独立运行模式）

\<Sysname\> display arp suppression vsi count

Total entries: 3

\# 显示主设备上的ARP泛洪抑制表项信息。（集中式IRF设备）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示主设备上的ARP泛洪抑制表项个数。（集中式IRF设备）

\<Sysname\> display arp suppression vsi count

Total entries: 3

\# 显示全局主用主控板上的ARP泛洪抑制表项信息。（分布式设备－IRF模式）

\<Sysname\> display arp suppression vsi

IP address      MAC address    Vsi Name                        Link ID    Aging

1.1.1.2         000f-e201-0101 vsi1                            0x70000    14

1.1.1.3         000f-e201-0202 vsi1                            0x80000    18

1.1.1.4         000f-e201-0203 vsi2                            0x90000    10

\# 显示全局主用主控板上的ARP泛洪抑制表项个数。（分布式设备－IRF模式）

\<Sysname\> display arp suppression vsi count

Total entries: 3

表1-1 display arp suppression vsi命令显示信息描述表

字段

描述

IP Address

ARP泛洪抑制表项的IP地址

MAC Address

ARP泛洪抑制表项的MAC地址

Vsi Name

VSI名称

Link ID

MAC表项的出链路标识符，用来在VSI内唯一标识一条AC或一条NVGRE隧道

Aging

ARP泛洪抑制表项的老化时间，单位为分钟

Total entries

ARP泛洪抑制表项的数目

【相关命令】

·**arp suppression enable**

·**reset arp suppression**** vsi**

**NVGRE \-- NVGRE配置命令 \-- display interface vsi-interface**

------------------------------------------------------------------------

**[display interface **]**vsi-interface**命令用来显示VSI虚接口的相关信息。

【命令】

**[display interface** **vsi-interface** [ *vsi-interface-id*    **brief** [ **description** \| **down** ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsi-nterface-id*]：VSI虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[brief**]：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定接口类型（**vsi-interface**），将显示设备支持的所有接口的相关信息。

·如果指定接口类型，不指定接口编号（*vsi-interface-id*），则显示所有VSI虚接口的信息。

·如果同时指定接口类型和接口编号，则显示指定VSI虚接口的信息。

【举例】

\# 显示接口VSI-interface100的相关信息。

\<Sysname\> display interface vsi-interface 100

Vsi-interface100

Current state: UP

Line protocol state: UP

Description: Vsi-interface100 Interface

Bandwidth: 1000000kbps

Maximum Transmit Unit: 1500

Internet Address is 10.1.1.1/24 Primary

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0011-2200-0102

Physical: Unknown, baudrate: 1000000 kbps

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

表1-2 display interface vsi-interface命令显示信息描述表

字段

描述

Vsi-interface100

接口VSI-interface100的相关信息

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

Physical

接口的物理类型，取值为Unknown

baudrate

接口的波特率，单位为kbps

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

\# 显示所有VSI虚接口的概要信息。

\<Sysname\> display interface vsi-interface brief

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Vsi100               DOWN DOWN     \--

\# 显示接口VSI-interface100的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display interface vsi-interface 100 brief description

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Vsi100               UP    UP      1.1.1.1         VSI-interface100

\# 显示当前状态为down的接口的信息以及DOWN的原因。

\<Sysname\> display interface brief down

Brief information of interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Vsi100               DOWN Administratively

Vsi200               DOWN Administratively

表1-3 display interface vsi-interface brief命令显示信息描述表

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

·Not connected：表示没有VSI关联该接口，或者关联该接口的VSI内没有AC或PW.

【相关命令】

·**reset counters interface**

**NVGRE \-- NVGRE配置命令 \-- display l2vpn mac-address**

------------------------------------------------------------------------

**[display l2vpn mac-address**]命令用来显示VSI的MAC地址表信息。

【命令】

**[display l2vpn mac-address ** **vsi** *vsi-name* ]  **dynamic**   **count**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi** *vsi-name*]：显示指定VSI的MAC地址表信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的MAC地址表信息。

**[dynamic**]：显示通过源MAC地址动态学习到的MAC地址表项。如果不指定本参数，则显示所有类型的MAC地址表项，包括通过源MAC地址动态学习的本地和远端MAC地址表项、静态配置的远端MAC地址表项。NVGRE不支持静态配置本地MAC地址表项。

**[count**]：显示MAC地址表项的数目。如果不指定本参数，则显示MAC地址表项的具体信息。

【举例】

\# 显示所有VSI的MAC地址表信息。

\<Sysname\> display l2vpn mac-address

MAC Address      State    VSI Name                        Link ID/Name  Aging

0000-0000-000a   dynamic  vpn1                            1             Aging

0000-0000-000b   static   vpn1                            Tunnel10      NotAging

0000-0000-000c   dynamic  vpn1                            Tunnel65535   Aging

0000-0000-000d   dynamic  vpn1                            Tunnel9999999 Aging

\-\-- 4 mac address(es) found  \-\--

\# 显示所有VSI的MAC地址表项总数。

\<Sysname\> display l2vpn mac-address count

4 mac address(es) found

表1-4 display l2vpn mac-address命令显示信息描述表

字段

描述

MAC Address

MAC地址

State

MAC地址的状态，取值包括：

·dynamic：表示通过源MAC地址动态学习的本地或远端MAC地址表项

·static：表示静态配置的远端MAC地址表项

VSI Name

VSI名称

Link ID/Name

对于本端MAC地址，为MAC地址的出链路标识符，即AC在VSI内的链路标识符；对于远端MAC地址，为MAC地址对应的隧道名称

Aging

MAC地址表项是否老化，取值包括Aging和NotAging

XX mac address(es) found

VSI的MAC地址表项的总数

【相关命令】

·**reset l2vpn mac-address**

**NVGRE \-- NVGRE配置命令 \-- display l2vpn service-instance**

------------------------------------------------------------------------

**[display l2vpn service-instance**]命令用来显示以太网服务实例的信息。

【命令】

**[display l2vpn service-instance ** **interface**]* interface-type interface-number* [ **service-instance** *instance-id*  ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定二层以太网接口或二层聚合接口上的以太网服务实例信息。*interface-type interface-number*为接口类型和接口编号。如果没有指定本参数，则显示所有二层以太网接口和二层聚合接口上的以太网服务实例信息。

**[service-instance*** instance-id*]：显示指定以太网服务实例的信息。*instance-id*为以太网服务实例的ID，取值范围为1～4096。如果指定了**interface*** interface-type interface-number*参数，没有指定本参数，则显示指定二层以太网接口或二层聚合接口上所有以太网服务实例的信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【举例】

\# 显示所有以太网服务实例的简要信息。

\<Sysname\> display l2vpn service-instance

Total number of service-instances: 4, 4 up, 0 down

Total number of ACs: 4, 4 up, 0 down

Interface                SrvID Owner                           LinkID State Type

GE1/0/3                  1     vsi10                           1      Up    VSI

GE1/0/3                  2     vsi11                           1      Up    VSI

GE1/0/3                  3     vsi12                           1      Up    VSI

GE1/0/3                  4     vsi13                           1      Up    VSI

表1-5 display l2vpn service-instance命令显示信息描述表

字段

描述

Total number of service-instances

以太网服务实例的总数，及处于up和down状态的以太网服务实例数目

Total number of ACs

AC的总数，及处于up和down状态的AC数目

Interface

二层以太网接口或二层聚合接口名称

SrvID

以太网服务实例的ID

Owner

VSI名称，如果以太网服务实例上尚未关联VSI，则本字段显示为空

LinkID

以太网服务实例在VSI内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

Type

以太网服务实例所属的L2VPN类型，取值包括VSI和VPWS

\# 显示二层以太网接口GigabitEthernet1/0/3上所有以太网服务实例的详细信息。

\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/3 verbose

Interface: GE1/0/3

  Service Instance: 1

    Encapsulation : s-vid 1 to 16

    VSI Name      : vsi10

    Link ID       : 1

    State         : Up

  Service Instance: 2

    Encapsulation : s-vid 1001 to 1016

                    only-tagged

    VSI Name      : vsi11

    Link ID       : 1

    State         : Up

  Service Instance: 3

    Encapsulation : s-vid 2000

                    c-vid 1001 to 1002 1015 to 1016

    VSI Name      : vsi12

    Link ID       : 1

    State         : Up

表1-6 display l2vpn service-instance verbose命令显示信息描述表

字段

描述

Interface

二层以太网接口或二层聚合接口

Service Instance

以太网服务实例ID

Encapsulation

以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则不显示本字段

VSI Name

与以太网服务实例关联的VSI的名称

Link ID

以太网服务实例在VSI内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

【相关命令】

·**service-instance**

**NVGRE \-- NVGRE配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

**[display l2vpn vsi**]命令用来显示VSI的信息。

【命令】

**[display** **l2vpn** **vsi** [ **name** *vsi-name*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** vsi-name*]：显示指定VSI的信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的信息。

**[verbose**]：显示VSI的详细信息。如果不指定本参数，则显示VSI的简要信息。

【举例】

\# 显示所有VSI的简要信息。

\<Sysname\> display l2vpn vsi

Total number of VSIs: 1, 1 up, 0 down, 0 admin down

VSI Name                        VSI Index       MTU    State

vpna                            0               1500   Up

\# 显示所有VSI的详细信息。

\<Sysname\> display l2vpn vsi verbose

VSI Name: 0

  VSI Index               : 0

  VSI State               : Down

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : Unlimited

  Drop Unknown            : Disabled

  Flooding                : Enabled

  Statistics              : Enabled

  Input statistics:

    Octets   : 0

    Packets  : 0

    Errors   : 0

    Discards : 0

  Output statistics:

    Octets   : 0

    Packets  : 0

    Errors   : 0

    Discards : 0

  Gateway Interface       : VSI-interface 100

  NVGRE VSID              : 4096

VSI Name: 1

  VSI Index               : 1

  VSI State               : Down

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : Unlimited

  Drop Unknown            : Disabled

  Flooding                : Enabled

  Statistics              : Enabled

  Input Statistics:

    Octets   : 0

    Packets  : 0

    Errors   : 0

    Drops : 0

  Output Statistics:

    Octets   : 0

    Packets  : 0

    Errors   : 0

    Discards : 0

  Gateway Interface       : VSI-interface 101

  NVGRE VSID              : 4097

  Tunnels:

    Tunnel Name          Link ID    State  Type

Tunnel1              0x7000001  Up     Manual

Tunnel2              0x7000002  Up     Manual

  ACs:

    AC                               Link ID    State

    BAGG1 srv1                       0          Down

表1-7 display l2vpn vsi命令显示信息描述表

字段

描述

VSI Name

VSI名称

VSI Index

VSI索引

VSI Description

VSI的描述信息，如果不配置，则此行不显示

VSI State

VSI的状态，取值包括：

·Up：up状态。只有NVGRE关联了处于up状态的隧道和AC，VSI才会处于up状态

·Down：down状态

·Administratively down：通过**shutdown**命令手工关闭VSI

MTU

VSI上配置的最大传输单元

Bandwidth

VSI的带宽限制值，单位为kbps

Broadcast Restrain

VSI的广播抑制百分比

Multicast Restrain

VSI的组播抑制百分比

Unknown Unicast Restrain

VSI的未知单播抑制百分比

MAC Learning

是否使能了MAC地址学习功能，取值包括：

·Enabled：使能了MAC地址学习功能

·Disabled：未使能MAC地址学习功能

MAC Table Limit

VSI内MAC地址表项的最大数目

取值为Unlimited，表示不限制VSI内MAC地址表项的最大数目

Drop Unknown

当VSI内学习到的MAC地址数达到最大值后，是否禁止转发源MAC地址不在MAC地址表里的报文

·Enabled：表示禁止转发

·Disabled：表示允许转发

Hub-Spoke

是否使能了Hub-spoke能力。未使能Hub-spoke能力，则不显示此字段

Flooding

VSI是否使能泛洪功能

·Enabled：表示使能了VSI的泛洪功能，即NVE会将目的MAC地址未知的单播数据帧发送给所有本地和远端站点

·Disabled：表示禁止VSI的泛洪功能，即NVE只将目的MAC地址未知的单播数据帧发送给所有本地站点

Statistics

是否使能VSI的统计功能，取值包括：

·Enabled：使能了VSI的统计功能

·Disabled：禁止VSI的统计功能

Input statistics

入方向的VSI报文统计信息，包括入方向接收的字节数（Octets）、接收的报文数（Packets）、接收的错误报文数（Errors）和丢弃的报文数（Discards）

Output statistics

出方向的VSI报文统计信息，包括出方向发送的字节数（Octets）、发送的报文数（Packets）、错误报文数（Errors）和丢弃的报文数（Discards）

Gateway Interface

VSI网关虚接口编号

NVGRE VSID

NVGRE虚拟子网编号

Tunnels

与NVGRE网络关联的隧道信息

Tunnel Name

隧道名字

Link ID

隧道在VSI内的链路标识符

State

隧道状态，取值包括Up和Down

Type

NVGRE和NVGRE隧道的关联方式，取值为Manual，表示手动关联NVGRE和NVGRE隧道

ACs

VSI的AC列表

AC

接入电路

Link ID

AC在VSI内的链路标识符

State

AC的状态，取值包括Up和Down

**NVGRE \-- NVGRE配置命令 \-- display nvgre tunnel**

------------------------------------------------------------------------

**[display nvgre tunnel**]命令用来显示与NVGRE网络关联的NVGRE隧道的信息。

【命令】

**[display** **nvgre tunnel** [ **vsid** *vsid* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsid*]：显示与指定NVGRE网络关联的隧道的信息。*vsid*为NVGRE虚拟子网标识符，取值范围为4096～16777214。不指定此参数，则显示所有与NVGRE网络关联的隧道的信息。

【举例】

\# 显示所有与NVGRE网络关联的隧道的信息。

\<Sysname\> display nvgre tunnel

Total number of NVGREs: 2

NVGRE VSID: 4096; VSI name: 1

NVGRE VSID: 4097; VSI name: 2; Total tunnels: 2 (1 up, 1 down)

Tunnel name          Link ID    State  Type

Tunnel1              0x7000001  Up     Manual

Tunnel3              0x7000002  Down   Manual

表1-8 display nvgre tunnel命令显示信息描述表

字段

描述

Total number of NVGREs

已创建的NVGRE网络的总数

NVGRE VSID

NVGRE虚拟子网编号

VSI name

NVGRE网络所属的VSI名称

Total tunnels

与NVGRE网络关联的隧道的总数，包括处于Up和Down状态的隧道总数

Tunnel name

隧道名称

Link ID

隧道在NVGRE网络内的链路标识符

State

隧道的状态，取值包括Up、Down

Type

NVGRE和NVGRE隧道的关联方式，取值为Manual，表示手动关联NVGRE和NVGRE隧道

【相关命令】

·**nvgre**

·**tunnel**

**NVGRE \-- NVGRE配置命令 \-- encapsulation**

------------------------------------------------------------------------

**[encapsulation**]命令用来配置以太网服务实例的报文匹配规则。

**[undo encapsulation**]命令用来删除以太网服务实例的报文匹配规则。

【命令】

**[encapsulation**[ **c-vid** { *vlan-id* \| *vlan-id-list* }]]

**[encapsulation**[ **s-vid** { *vlan-id* \| *vlan-id-list* } [ **only-tagged** ]]]

**[encapsulation**[ **s-vid** *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]]

**[encapsulation**[ { **default** \| **tagged** \| **untagged** }]]

**[undo encapsulation**]

【缺省情况】

未配置任何报文匹配规则。

【视图】

以太网服务实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[c-vid**[ { *vlan-id* \| *vlan-id-list* }]]：匹配内层VLAN标签（Customer VLAN ID）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ to *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[s-vid**[ { *vlan-id* \| *vlan-id-list* }]]：匹配外层VLAN标签（Service VLAN ID）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[only-tagged**]：表示只匹配携带VLAN标签的报文。当匹配的VLAN为缺省VLAN时，如果未指定本关键字，则会同时匹配所携带VLAN标签为缺省VLAN的报文和未携带VLAN标签的报文；如果指定了本参数，则只匹配所携带VLAN标签为缺省VLAN的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[s-vid**[ *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]]：匹配指定外层VLAN标签和内层VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·**al****l**表示所有VLAN。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[default**]：表示缺省的报文匹配规则。

**[tagged**]：表示匹配携带VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[untagged**]：表示匹配未携带VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

【使用指导】

当同一个接口下配置的不同以太网服务实例的报文匹配规则出现重叠时，如何匹配报文与设备的型号有关，请以设备的实际情况为准。

同一个以太网接口下可以创建多个服务实例，但是最多只能有一个服务实例采用缺省的报文匹配规则（**encapsulation default**）。如果接口下同时存在一个采用缺省报文匹配规则的服务实例和多个采用其他报文匹配规则的服务实例，则没有与任何其他报文匹配规则匹配的报文将匹配缺省报文匹配规则；如果接口下只存在一个采用缺省报文匹配规则的服务实例，则该接口上的所有报文都匹配缺省报文匹配规则。

需要注意的是：

·在同一个以太网服务实例视图下，不能重复执行本命令。

·删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例与VSI的关联。

·内层VLAN标签和外层VLAN标签的介绍请参见"二层技术-以太网交换配置指导"中的"QinQ"。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1的以太网服务实例1上配置如下报文匹配规则：匹配外层VLAN标签为111，内层VLAN标签为20、30～40的报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 1

Sysname-GigabitEthernet1/0/1-srv1 encapsulation s-vid 111 c-vid 20 30 to 40

【相关命令】

·**display l2vpn service-instance**

**NVGRE \-- NVGRE配置命令 \-- flooding disable**

------------------------------------------------------------------------

**[flooding disable**]命令用来关闭VSI的泛洪功能。

**[undo flooding disable**]命令用来恢复缺省情况。

【命令】

**[flooding disable**]

**[undo flooding disable**]

【缺省情况】

VSI的泛洪功能处于开启状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，NVE从本地站点内接收到目的MAC地址未知的单播数据帧后，会在该NVGRE网络内除接收接口外的所有本地接口和NVGRE隧道上泛洪该数据帧，将该数据帧发送给NVGRE网络内的所有站点。如果用户希望把该类数据帧限制在本地站点内，不通过NVGRE隧道将其转发到远端站点，则可以通过本命令手工禁止NVGRE网络对应VSI的泛洪功能。

【举例】

\# 关闭名称为vsi1的VSI的泛洪功能。

\<Sysname\> system-view

Sysname vsi vsi1

Sysname-vsi-vsi1 flooding disable

**NVGRE \-- NVGRE配置命令 \-- gateway vsi-interface**

------------------------------------------------------------------------

**[gateway vsi-interface**]命令用来为VSI指定网关接口。

**[undo gateway vsi-interface **]命令用来恢复缺省情况。

【命令】

**[gateway vsi-interface ***vsi-interface-id*]

**[undo gateway vsi-interface**]

【缺省情况】

没有为VSI指定网关接口。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-interface-id*]：VSI网关虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·一个VSI只能指定一个网关接口。

·不同的VSI可以指定相同的网关接口。

【举例】

\# 为VSI指定网关接口为Vsi-interface100。

\<Sysname\> system

Sysname vsi vpna

Sysname-vsi-vpna gateway vsi-interface 100

【相关命令】

·**interface vsi-interface**

**NVGRE \-- NVGRE配置命令 \-- interface vsi-interface**

------------------------------------------------------------------------

**[interface vsi-interface**]命令用来创建VSI虚接口，并进入VSI虚接口视图。

**[undo interface vsi-interface**]命令用来删除VSI虚接口。

【命令】

**[interface vsi-interface ***vsi-interface-id*]

**[undo interface vsi-interface ***vsi-interface-id*]

【缺省情况】

设备上不存在任何VSI虚接口。

【视图】

系统视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-nterface-id*]：VSI虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 创建VSI虚接口100，并进入VSI虚接口视图。

\<Sysname\> system

Sysname interface vsi-interface 100

Sysname-Vsi-interface100

【相关命令】

·**gateway vsi-interface**

**NVGRE \-- NVGRE配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

**[l2vpn enable**]命令用来使能L2VPN功能。

**[undo l2vpn enable**]命令用来关闭L2VPN功能。

【命令】

**[l2vpn enable**]

**[undo l2vpn enable**]

【缺省情况】

L2VPN功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有使能L2VPN功能后，才能进行L2VPN的相关配置。

【举例】

\# 使能L2VPN功能。

\<Sysname\> system-view

Sysname l2vpn enable

**NVGRE \-- NVGRE配置命令 \-- mac-address static**

------------------------------------------------------------------------

**[mac-address static**]命令用来添加静态远端MAC地址表项。

**[undo mac-address static**]命令用来删除指定的静态远端MAC地址表项。

【命令】

**[mac-address static** *mac-address* **interface tunnel** *tunnel-number* **vsi** *vsi-name*]

**[undo mac-address static** [ *mac-address*   **interface tunnel** *tunnel-number*  **vsi** *vsi-name*]]

【缺省情况】

设备上不存在任何静态的远端MAC地址表项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac*-]*address*：MAC地址，格式为H-H-H，不支持组播MAC地址和全0的MAC地址。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。

**[interface tunnel ***tunnel-number*]：指定远端MAC地址对应的NVGRE隧道接口。*tunnel-number*为NVGRE隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[vsi*** vsi-name*]：指定远端MAC地址所属的VSI。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

远端MAC地址是指NVE连接的远端站点内虚拟机的MAC地址。远端MAC地址既可以通过本命令静态配置，也可以通过报文中的源MAC地址动态学习。静态配置的远端MAC地址表项优先级高于源MAC地址动态学习的表项。

【举例】

\# 添加一条静态远端MAC地址表项：MAC地址为000f-e201-0101，NVGRE隧道接口为Tunnel1，MAC地址所属的VSI为vsi1。

\<Sysname\> system-view

Sysname mac-address static 000f-e201-0101 interface tunnel 1 vsi vsi1

**NVGRE \-- NVGRE配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置接口的MTU值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，取值范围为46～1560，单位为字节。

【举例】

\# 配置接口VSI-interface100的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 mtu 1430

**NVGRE \-- NVGRE配置命令 \-- nvgre**

------------------------------------------------------------------------

**[nvgre**]命令用来创建NVGRE网络，并进入NVGRE网络视图。

**[undo nvgre**]命令用来删除指定的NVGRE网络。

【命令】

**[nvgre ***vsid*]

**[undo nvgre**]

【缺省情况】

设备上不存在任何NVGRE网络。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsid*]：NVGRE虚拟子网标识符，取值范围为4096～16777214。

【使用指导】

在一个VSI下只能创建一个NVGRE网络。不同VSI下创建的NVGRE网络，其VSID不能相同。

【举例】

\# 在名称为vpna的VSI下创建编号为10000的NVGRE网络，并进入NVGRE网络视图。

\<Sysname\> system

Sysname vsi vpna

Sysname-vsi-vpna nvgre 10000

Sysname-vsi-vpna-nvgre-10000

【相关命令】

·**vsi**

**NVGRE \-- NVGRE配置命令 \-- reset arp suppression vsi**

------------------------------------------------------------------------

![说明](NVGRE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset arp suppression vsi**]命令用来清除VSI的ARP泛洪抑制表项。

【命令】

**[reset arp suppression vsi** [ **name** *vsi-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** vsi-name*]：清除指定VSI的ARP泛洪抑制表项。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除所有VSI的ARP泛洪抑制表项。

【举例】

\# 清除所有VSI的ARP泛洪抑制表项。

\<Sysname\> reset arp suppression vsi

This command will delete all entries. Continue? [Y/N:y]

【相关命令】

·**display arp suppression**** vsi**

·**arp suppression enable**

**NVGRE \-- NVGRE配置命令 \-- reset counters interface vsi-interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除接口的统计信息。

【命令】

**[reset counters interface** **vsi-interface** [ *vsi-interface-id*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-nterface-id*]：VSI虚接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定接口类型（**vsi-interface**），则清除所有接口的统计信息；

·如果指定接口类型，不指定接口编号（*vsi-interface-id*），则清除所有VSI虚接口的统计信息；

·如果同时指定接口类型和接口编号，则清除指定VSI虚接口的统计信息。

【举例】

\# 清除接口VSI-interface100的统计信息。

\<Sysname\> reset counters interface vsi-interface 100

【相关命令】

·**display interface**

**NVGRE \-- NVGRE配置命令 \-- reset l2vpn mac-address**

------------------------------------------------------------------------

![说明](NVGRE命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[reset l2vpn mac-address**]命令用来清除通过源MAC地址动态学习的MAC地址表项。

【命令】

**[reset l2vpn mac-address ** **vsi**]* vsi-name *

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsi*** vsi-name*]：清除指定VSI动态学习的MAC地址表项。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除所有VSI动态学习的MAC地址表项。

【使用指导】

VSI通过源MAC地址学习到错误的MAC地址表项，或学习的MAC地址表项数目达到最大值时，可以执行本命令，以便重新学习MAC地址表项。

【举例】

\# 清除名为vpn1的VSI通过源MAC地址动态学习的MAC地址表项。

\<Sysname\> reset l2vpn mac-address vsi vpn1

【相关命令】

·**display l2vpn mac-address vsi**

**NVGRE \-- NVGRE配置命令 \-- reset l2vpn statistics vsi**

------------------------------------------------------------------------

![说明](NVGRE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset l2vpn statistics vsi**]命令用来清除VSI的报文统计信息。

【命令】

**[reset l2vpn statistics vsi ** **name** *vsi-name* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[name*** vsi-name*]：清除指定VSI的报文统计信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除所有VSI的信息。

【举例】

\# 清除本设备上所有VSI报文统计信息。

\<Sysname\> reset l2vpn statistics vsi

【相关命令】

·**statistics enable**

**NVGRE \-- NVGRE配置命令 \-- selective-flooding mac-address**

------------------------------------------------------------------------

**[selective-flooding mac-addres**]命令用来配置VSI选择性泛洪的MAC地址。

**[undo selective-flooding mac-addres**]命令用来删除VSI的选择性泛洪MAC地址。

【命令】

**[selective-flooding mac-addres** *mac-addres*]

**[undo selective-flooding mac-addres** *mac-addres*]

【缺省情况】

设备上不存在任何VSI选择性泛洪MAC地址。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：选择性泛洪的MAC地址。该MAC地址不能为全F。

【使用指导】

通过**flooding disable**命令关闭VSI的泛洪功能后，为了将某些MAC地址的数据帧泛洪到远端站点以保证某些业务的流量在站点间互通，可以配置选择性泛洪的MAC地址。当数据帧的目的MAC地址匹配选择性泛洪的MAC地址时，该数据帧可以泛洪到远端站点。

【举例】

\# 在VSI vsi1下配置选择性泛洪的MAC地址为000f-e201-0101。

\<Sysname\> system-view

Sysname VSI vsi1

Sysname-vsi-vsi1 selective-flooding mac-address 000f-e201-0101

【相关命令】

·**flooding disable**

**NVGRE \-- NVGRE配置命令 \-- service-instance**

------------------------------------------------------------------------

**[service-instance**]命令用来创建以太网服务实例，并进入以太网服务实例视图。

**[undo service-instance**]命令用来删除指定的以太网服务实例。

【命令】

**[service-instance ***instance-id*]

**[undo service-instance ***instance-id*]

【缺省情况】

接口上不存在任何以太网服务实例。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：以太网服务实例的编号，取值范围为1～4096。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1上创建以太网服务实例1，并进入以太网服务实例1的视图。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 1

Sysname-GigabitEthernet1/0/1-srv1

【相关命令】

·**display l2vpn service-instance**

**NVGRE \-- NVGRE配置命令 \-- shutdown (VSI view)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前的VSI。

**[undo shutdown**]命令用来恢复缺省情况。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

VSI处于开启状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭VSI后，该VSI将不能提供二层交换服务。

关闭VSI功能通常用于暂时禁用二层交换服务，但还需要再次启用该服务的场景。关闭VSI后，该VSI所有已存在的配置保持不变。在关闭状态下还可以对VSI进行配置。VSI再次被开启后，基于最新的配置提供二层交换服务。

【举例】

\# 关闭名为vpn1的VSI。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 shutdown

【相关命令】

·**display l2vpn vsi**

**NVGRE \-- NVGRE配置命令 \-- shutdown (VSI interface view)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前接口。

**[undo** **shutdown**]命令用来开启当前接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

VSI虚接口均处于开启状态。

【视图】

VSI虚接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭接口VSI-interface100。

\<Sysname\> system-view

Sysname interface vsi-interface 100

Sysname-Vsi-interface100 shutdown

**NVGRE \-- NVGRE配置命令 \-- statistics enable**

------------------------------------------------------------------------

![说明](NVGRE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics enable**]命令用来开启指定VSI的报文统计功能。

**[undo statistics enable**]命令用来关闭指定VSI的报文统计功能。

【命令】

**[statistics enable**]

**[undo statistics enable**]

【缺省情况】

VSI的报文统计功能处于关闭状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启名为vpls1的VSI的报文统计功能。

\<Sysname\> system-view

Sysname vsi vpls1

Sysname-vsi-vpls1 statistics enable

【相关命令】

·**reset l2vpn statistics vsi**

**NVGRE \-- NVGRE配置命令 \-- tunnel**

------------------------------------------------------------------------

**[tunnel**]命令用来配置NVGRE网络与指定的NVGRE隧道关联。

**[undo tunnel**]命令用来取消NVGRE网络与NVGRE隧道的关联。

【命令】

**[tunnel ***tunnel-number*]

**[undo tunnel ***tunnel-number*]

【缺省情况】

NVGRE网络没有与任何NVGRE隧道关联。

【视图】

NVGRE网络视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tunnel-numb*er]：隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在NVGRE组网中，用户需要手工将NVGRE网络与NVGRE隧道关联。NVE接收到某个NVGRE网络的泛洪流量后，将在与该NVGRE网络关联的所有NVGRE隧道上发送该流量，以便将流量转发给所有的远端NVE。

执行本命令时，需要注意的是：

·本命令指定的隧道必须是NVGRE模式的隧道。

·一个NVGRE网络可以关联多条NVGRE隧道；一条NVGRE隧道可以关联多个NVGRE网络。

【举例】

\# 配置NVGRE隧道Tunne0和Tunnel1与NVGRE 10000关联。

\<Sysname\> system

Sysname vsi vpna

Sysname-vsi-vpna nvgre 10000

Sysname-vsi-vpna-nvgre-10000 tunnel 0

Sysname-vsi-vpna-nvgre-10000 tunnel 1

【相关命令】

·**display nvgre tunnel**

**NVGRE \-- NVGRE配置命令 \-- vsi**

------------------------------------------------------------------------

**[vsi**]命令用来创建一个VSI（Virtual Switching Instance，虚拟交换实例），并进入VSI视图。

**[undo** **vsi**]命令用来删除指定的VSI。

【命令】

**[vsi**] *vsi-name*

**[undo**]**vsi** *vsi-name*

【缺省情况】

设备上不存在任何VSI。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

VSI是NVE上为一个NVGRE网络提供二层交换服务的虚拟交换实例。VSI可以看做是NVE上的一台基于NVGRE网络进行二层转发的虚拟交换机，它具有传统以太网交换机的所有功能，包括源MAC地址学习、MAC地址老化、泛洪等。VSI与NVGRE网络一一对应。

【举例】

\# 创建名为nvgre5000的VSI，并进入VSI视图。

\<Sysname\> system-view

Sysname vsi nvgre5000

Sysname-vsi-nvgre5000

【相关命令】

·**display l2vpn vsi**

**NVGRE \-- NVGRE配置命令 \-- xconnect vsi**

------------------------------------------------------------------------

**[xconnect vsi**]命令用来将AC与VSI关联。

**[undo** **xconnect vsi**]命令用来取消AC与VSI的关联。

【命令】

**[xconnect vsi ***vsi-name *[[ **access-mode** { **ethernet** \| **vlan** } ]]]

**[undo xconnect vsi**]

【缺省情况】

AC没有与VSI关联。

【视图】

接口视图/以太网服务实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

**[access-mode**]：指定接入模式。当关联VSI的AC为三层以太网子接口、VLAN接口、以太网服务实例时，接入模式缺省为VLAN；其他情况下，接入模式缺省为Ethernet。

**[ethernet**]：指定接入模式为Ethernet。

**[vlan**]：指定接入模式为VLAN。

【使用指导】

在接口视图下执行本命令后，从接口接收到的报文将通过查找关联VSI的MAC地址表进行转发；在某个接口的以太网服务实例视图下执行本命令后，从该接口接收到的、符合以太网服务实例报文匹配规则的报文，将通过查找关联VSI的MAC地址表进行转发。

接入模式分为以下两种：

·VLAN接入模式：从本地站点接收到的、发送给本地站点的以太网帧必须带有VLAN tag。NVE从本地站点接收到以太网帧后，删除该帧的所有VLAN tag，再转发该数据帧；NVE发送以太网帧到本地站点时，为其添加VLAN tag。采用该模式时，NVE不会传递VLAN tag信息，不同站点可以独立地规划自己的VLAN，不同站点的不同VLAN之间可以互通。

·Ethernet接入模式：从本地站点接收到的、发送给本地站点的以太网帧可以携带VLAN tag，也可以不携带VLAN tag。NVE从本地站点接收到以太网帧后，保持该帧的VLAN tag信息不变，转发该数据帧；NVE发送以太网帧到本地站点时，不会为其添加VLAN tag。采用该模式时，NVE会在不同站点间传递VLAN tag信息，不同站点的VLAN需要统一规划，否则无法互通。

需要注意的是，在以太网服务实例下配置该命令前，必须先配置**encapsulation**命令。

【举例】

\# 接口GigabitEthernet1/0/1下采用以太网服务实例200来匹配外层VLAN为200的报文，将该以太网服务实例与名为vpn1的VSI关联。

\<Sysname\> system-view

Sysname vsi vpn1 hub-spoke

Sysname-vsi-vpn1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 200

Sysname-GigabitEthernet1/0/1-srv200 encapsulation s-vid 200

Sysname-GigabitEthernet1/0/1-srv200 xconnect vsi vpn1

【相关命令】

·**display l2vpn interface**

·**display l2vpn service-instance**

·**encapsulation**

·**vsi**
