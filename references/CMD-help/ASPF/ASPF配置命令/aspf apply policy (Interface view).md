<!-- CMD-INDEX
  aspf apply policy (Interface view)  | 接口视图             | L15
  aspf apply policy (Zonepair view)   | 安全域间实例视图         | L75
  aspf policy                         | 系统视图             | L145
  detect                              | ASPF策略视图         | L193
  display aspf all                    | 任意视图             | L309
  display aspf interface              | 任意视图             | L415
  display aspf policy                 | 任意视图             | L477
  display aspf session                | 任意视图             | L567
  icmp-error drop                     | ASPF策略视图         | L1365
  reset aspf session                  | 用户视图             | L1417
  tcp syn-check                       | ASPF策略视图         | L1483
-->

**ASPF \-- ASPF配置命令 \-- aspf apply policy (Interface view)**

------------------------------------------------------------------------

**[aspf apply policy**]命令用来在接口上应用ASPF策略。

**[undo** **aspf apply policy**]命令用来删除接口上应用的ASPF策略。

【命令】

**[aspf**[ **apply policy** *aspf-policy-number* { **inbound** \| **outbound** }]]

**[undo aspf** **apply policy** *aspf*]*-policy-number*[ { **inbound** \| **outbound** }]

【缺省情况】

接口上没有应用ASPF策略。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aspf-policy-number*]：ASPF策略号，取值范围与设备的型号有关，请以设备的实际情况为准。

**[inbound**]：对接口入方向的报文应用ASPF策略。

**[outbound**]：对接口出方向的报文应用ASPF策略。

【使用指导】

只有将定义好的ASPF策略应用到接口上，才能对通过接口的流量进行检测。由于ASPF对于应用层协议状态的保存和维护都是基于接口的，因此在实际应用中，必须保证报文入口的一致性，即必须保证连接发起方发送的报文和响应端返回的报文经过同一接口。

可以同时在接口的出方向和入方向上都应用ASPF策略。

【举例】

\# 在接口GigabitEthernet1/0/1的出方向上应用ASPF策略。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 aspf apply policy 1 outbound

【相关命令】

·**aspf policy**

·**display aspf policy all**

·**display aspf policy interface**

**ASPF \-- ASPF配置命令 \-- aspf apply policy (Zonepair view)**

------------------------------------------------------------------------

![说明](ASPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[aspf apply policy**]命令用来在安全域间实例上应用ASPF策略。

**[undo** **aspf apply policy**]命令用来取消应用在安全域间实例上的指定ASPF策略。

【命令】

**[aspf apply policy** *aspf-policy-number*]

**[undo aspf apply policy** *aspf-policy-number*]

【缺省情况】

安全域间实例上应用了一个缺省的ASPF策略。

【视图】

安全域间实例视图

【支持的缺省用户角色】

network-admin

mdc-admin**

【参数】

*[aspf-policy-number*]：ASPF策略号，取值范围为1～*max_number*，其中*max_number*的取值与设备型号有关，请以设备的实际情况为准。

【使用指导】

创建安全域间实例时，系统默认为该实例应用一个缺省的ASPF策略，该策略支持对所有协议进行ASPF检测，但默认的策略不可改变，如果需要调整ASPF策略，需要自定义一个ASPF策略，并在安全域间实例上引用。

【举例】

\# 在安全域间实例上应用ASPF策略。

\<Sysname\> system-view

Sysname security-zone name trust

Sysname-security-zone-Trust import interface gigabitethernet 1/0/1

Sysname-security-zone-Trust quit

Sysname security-zone name untrust

Sysname-security-zone-Untrust import interface gigabitethernet 1/0/2

Sysname-security-zone-Untrust quit

Sysname zone-pair security source trust destination untrust

Sysname-zone-pair-security-Trust-Untrust aspf apply policy 1

【相关命令】

·**aspf policy**

·**display aspf policy all**

·**zone****-pair security**（基础命令参考/安全域）

**ASPF \-- ASPF配置命令 \-- aspf policy**

------------------------------------------------------------------------

**[aspf policy**]命令用来创建ASPF策略，并进入ASPF策略视图。

**[undo** **aspf policy**]命令用来删除指定的ASPF策略。

【命令】

**[aspf policy** *aspf-policy-number*]

**[undo** **aspf policy** *aspf-policy-number*]

【缺省情况】

不存在ASPF策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[aspf-policy-number*]：ASPF策略号，取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 创建ASPF策略1，并进入该ASPF策略视图。

\<Sysname\> system-view

Sysname aspf policy 1

Sysname-aspf-policy-1

【相关命令】

·**display aspf all**

·**display aspf policy**

**ASPF \-- ASPF配置命令 \-- detect**

------------------------------------------------------------------------

![说明](ASPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[detect**]命令用来为应用层协议或传输层协议配置ASPF检测。

**[undo** **detect**]命令用来恢复缺省情况。

【命令】

**[detect**]**[gtp**[\| **icmp** \| **icmpv6** \|]**ils **[\| **mgcp** \| **nbt** \| **pptp** \| **rawip** \| **rsh** \| ]**rtsp**[ \| ]**sctp **[\| ]**sqlnet**[ \| **tcp** \| ]**tftp**[\| **udp** \|]**udp-lite**[\| **xdmcp** ]}

**[undo** **detect** ]**[gtp**[\| **icmp** \| **icmpv6** \|]**ils **[\| **mgcp** \| **nbt** \| **pptp** \| **rawip** \|]**rsh**[ \| ]**rtsp**[ \|]**sctp **[\| **sqlnet** \| **tcp** \| ]**tftp**[\| **udp** \| ]**udp-lite **[\| **xdmcp**]}

**[detect**[ { **dns \| ftp** \| **h323** \| **http** \| **sccp** \| **sip** \| **smtp** } [ **action drop** ]]]

**[undo detect**[ { **dns** \| **ftp** \| **h323** \| **http** \| **sccp** \| **sip** \| **smtp** }]]

【缺省情况】]

未配置应用层和传输层协议]ASPF检测。

【视图】

ASPF策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dccp**]：表示DCCP（Datagram Congestion Control Protocol，数据报拥塞控制协议）协议，属于传输层协议；

**[dns**]：表示DNS协议，属于应用层协议。

**[ftp**]：表示FTP协议，属于应用层协议；

**[gtp**]：表示GTP（GPRS Tunneling Protocol，GPRS隧道协议）协议，属于应用层协议；

**[h323**]：表示H.323协议族，属于应用层协议；

**[http**]：表示HTTP协议，属于应用层协议。

**[icmp**]：表示ICMP协议，属于传输层协议；

**[icmpv6**]：表示ICMPv6协议，属于传输层协议；

**[ils**]：表示ILS（Internet Locator Service，互联网定位服务）协议，属于应用层协议；

**[mgcp**]：表示MGCP（Media Gateway Control Protocol，媒体网关控制协议）协议，属于应用层协议；

**[nbt**]：表示NBT（NetBIOS over TCP/IP，基于TCP/IP的网络基本输入输出系统）协议，属于应用层协议；

**[pptp**]：表示PPTP（Point-to-Point Tunneling Protocol，点到点隧道协议）协议，属于应用层协议；

**[rawip**]：表示Raw IP协议，属于传输层协议；

**[rsh**]：表示RSH（Remote Shell，远程外壳）协议，属于应用层协议；

**[rtsp**]：表示RTSP（Real Time Streaming Protocol，实时流协议）协议，属于应用层协议；

**[sccp**]：表示SCCP（Skinny Client Control Protocol，瘦小客户端控制协议）协议，属于应用层协议；

**[sctp**]：表示SCTP（Stream Control Transmission Protocol，流控制传输协议）协议，属于传输层协议；

**[sip**]：表示SIP（Session Iniation Protocol，会话初始化协议）协议，属于应用层协议；

**[smtp**]：表示SMTP协议，属于应用层协议。

**[sqlnet**]：表示SQLNET协议，属于应用层协议；

**[tcp**]：表示TCP协议，属于传输层协议；

**[tftp**]：表示TFTP协议，属于应用层协议；

**[udp**]：表示UDP协议，属于传输层协议；

**[udp-lite**]：表示UDP-Lite协议，属于传输层协议；

**[xdmcp**]：表示XDMCP（X Display Manager Control Protocol，X显示监控）协议，属于应用层协议。

**[action**]：设置对检测到的非法报文的处理行为。若不指定该参数，则表示放行报文。

**[drop**]：表示丢弃报文。

【使用指导】

可通过多次执行本命令配置多种协议类型的ASPF检测。

在未配置应用层协议检测，直接配置TCP或UDP检测的情况下，可能会产生接收不到应答报文的情况，故建议应用层协议检测和TCP/UDP检测配合使用。

对于Telnet应用，直接配置通用TCP检测即可实现ASPF功能。

需要注意的是，目前，设备对支持**action**参数的应用层协议才支持进行协议状态合法性检查，对不符合协议状态的报文可根据配置进行丢弃。对于其它应用层协议，仅进行连接状态信息的维护，不做协议状态合法性检查。

【举例】

\# 配置对FTP协议报文进行ASPF检测。

\<Sysname\> system-view

Sysname aspf policy 1

Sysname-aspf-policy-1 detect ftp

【相关命令】

·**display** **aspf** **policy**

**ASPF \-- ASPF配置命令 \-- display aspf all**

------------------------------------------------------------------------

**[display** **aspf** **all**]命令用来查看ASPF策略配置信息及接口应用ASPF策略的信息。

【命令】

**[display aspf all**]

【视图】

任意视图

【缺省用户角色】

network-admin

netword-operator

mdc-admin

mdc-operator

【举例】

\# 查看所有的ASPF策略配置信息。

\<Sysname\> display aspf all

ASPF policy configuration:

  Policy number: 1

    Enable ICMP error message check

    Disable TCP SYN packet check

    Detect these protocols:

      FTP

      TCP

Interface configuration:

  GigabitEthernet1/0/1

    Inbound policy : 1

    Outbound policy: none

表1-1 display aspf all命令显示信息描述表

字段

描述

ASPF policy configuration

ASPF策略的配置信息

Policy number

ASPF策略号

Enable ICMP error message check

使能ICMP差错报文检测功能

Enable TCP SYN packet check

丢弃非SYN的TCP首报文

Disable ICMP error message check

去使能ICMP差错报文检测功能

Disable TCP SYN packet check

不丢弃非SYN的TCP首报文

Detect these protocols

需要检测的协议

Interface configuration

接口下应用ASPF策略的配置信息

Inbound policy

接口入方向上应用的ASPF策略编号

Outbound policy

接口出方向上应用的ASPF策略编号

【相关命令】

·**aspf**** apply policy**

·**aspf policy**

·**display aspf policy**

**ASPF \-- ASPF配置命令 \-- display aspf interface**

------------------------------------------------------------------------

**[display** **aspf** **interface**]命令用来查看接口上的ASPF策略配置信息。

【命令】

**[display aspf interface**]

【视图】

任意视图

【缺省用户角色】

network-admin

netword-operator

mdc-admin

mdc-operator

【举例】

\# 查看接口上的ASPF策略信息。

\<Sysname\> display aspf interface

Interface configuration:

  GigabitEthernet1/0/1

    Inbound policy : 1

    Outbound policy: none

表1-2 display aspf interface命令显示信息描述表

字段

描述

Interface configuration

接口上应用ASPF策略的配置信息

Inbound policy

接口入方向上应用的ASPF策略编号

Outbound policy

接口出方向上应用的ASPF策略编号

【相关命令】

·**aspf**** apply policy**

·**aspf policy**

**ASPF \-- ASPF配置命令 \-- display aspf policy**

------------------------------------------------------------------------

**[display** **aspf** **policy**]命令用来查看ASPF策略的配置信息。

【命令】

**[display** **aspf** **policy** *aspf-policy-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

netword-operator

mdc-admin

mdc-operator

【参数】

*[aspf-policy-number*]：ASPF策略号，取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 查看策略号为1的ASPF策略的配置信息。

\<Sysname\> display aspf policy 1

ASPF policy configuration:

  Policy number: 1

    ICMP error message check: Disabled

    TCP SYN packet check: Enabled

    Inspected protocol   Action

     FTP                  Drop

     TCP                  -

     HTTP                 None

表1-3 display aspf policy命令显示信息描述表

字段

描述

ASPF policy configuration

ASPF策略的配置信息

Policy number

ASPF策略号

ICMP error message check

ICMP差错报文检测功能的开启状态

TCP SYN packet check

非SYN的TCP首报文丢弃功能是否开启

Inspected protocol

待检测的协议

Action

对检测到的非法报文的处理行为

·Drop：丢弃

·None：不做处理，放行

"-"表示该协议不支持此配置项

【相关命令】

·**aspf policy**

**ASPF \-- ASPF配置命令 \-- display aspf session**

------------------------------------------------------------------------

![说明](ASPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display aspf session**]命令用来查看ASPF的会话表信息。

【命令】

集中式设备：

**[display aspf session**[ [ **ipv4** \| **ipv6** ]  **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display aspf session**[ [ **ipv4** \| **ipv6** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

分布式设备－IRF模式：

**[display aspf session**[ [ **ipv4** \| **ipv6** ] ]**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

netword-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：查看ASPF创建的IPv4会话表。

**[ipv6**]：查看ASPF创建的IPv6会话表。

**[slot**] *slot-number*：显示指定单板上的ASPF会话表，*slot-number*表示单板所在槽位号。不指定该参数时，显示所有单板上的ASPF会话表。（分布式设备－独立运行模式）

**[slot**] *slot-number*：显示指定成员设备上的ASPF会话表，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上的ASPF会话表。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的ASPF会话表，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的ASPF会话表。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备的指定单板上的ASPF会话表，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的ASPF会话表。（分布式IRF设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的ASPF会话表，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的ASPF会话表。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：显示指定CPU上的ASPF会话表，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[verbose**]：查看ASPF会话表的详细信息。若不指定该参数，则表示查看ASPF会话表的概要信息。

【使用指导】

不指定**ipv4**和**ipv6**参数时，表示查看所有的ASPF会话表信息。

【举例】

\# 显示ASPF创建的IPv4会话表的概要信息。（集中式设备）

\<Sysname\> display aspf session ipv4

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Total sessions found: 2

\# 显示ASPF创建的IPv4会话表的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display aspf session ipv4

Slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Total sessions found: 2

\# 显示ASPF创建的IPv4会话表的概要信息。（分布式设备－IRF模式）

\<Sysname\> display aspf session ipv4

Slot 1 in chassis 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Total sessions found: 2

\# 显示IPv4 ASPF会话的详细信息。（集中式设备）

\<Sysname\> display aspf session ipv4 verbose

Initiator:

Source       IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source       IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:          1 packets         60 bytes

Responder-\>Initiator:          0 packets          0 bytes

Total sessions found: 2

\# 显示IPv4 ASPF会话的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display aspf session ipv4 verbose

Slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:         1 packets         6048 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 2

\# 显示IPv4 ASPF会话的详细信息。（分布式设备－IRF模式）

\<Sysname\> display aspf session ipv4 verbose

Slot 1 in chassis 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:         1 packets         6048 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 2

\# 显示ASPF创建的IPv4会话表的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display aspf session ipv4

CPU 0 on slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Total sessions found: 2

\# 显示ASPF创建的IPv4会话表的概要信息。（分布式设备－IRF模式）

\<Sysname\> display aspf session ipv4

CPU 0 on slot 1 in chassis 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Total sessions found: 2

\# 显示IPv4 ASPF会话的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display aspf session ipv4 verbose

CPU 0 on slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:         1 packets         6048 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 2

\# 显示IPv4 ASPF会话的详细信息。（分布式设备－IRF模式）

\<Sysname\> display aspf session ipv4 verbose

CPU 0 on slot 1 in chassis 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: SrcZone

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: DestZone

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:         1 packets         6048 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 2

表1-4 display aspf session命令显示信息描述表

字段

描述

Initiator

发起方到响应方的连接对应的会话信息

Responder

响应方到发起方的连接对应的会话信息

Source IP/port

源IP地址/端口号

Dest IP/port

目的IP地址/端口号

DS-Lite tunnel peer

DS-Lite隧道对端地址。会话不属于任何DS-Lite隧道时，本字段显示为"-"

VPN-instance/VLAN ID/VLL ID

会话所属的MPLS L3VPN/二层转发时会话所属的VLAN ID/二层转发时会话所属的INLINE。未指定的参数则显示为"-"

Protocol

传输层协议类型，取值包括：DCCP、ICMP、ICMPv6、Raw IP 、SCTP、TCP、UDP、UDP-Lite

括号中的数字表示协议号

Inbound interface

报文的入接口

Source security zone

源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"-"

该参数的支持情况与设备的型号有关，请以设备的实际情况为准

State

会话的协议状态

Application

应用层协议类型，取值包括：FTP、DNS等，OTHER表示未知协议类型，其对应的端口为非知名端口

Start time

会话的创建时间

TTL

会话剩余存活时间，单位为秒

Initiator-\>Responder

发起方到响应方的报文数、报文字节数

Responder-\>Initiator

响应方到发起方的报文数、报文字节数

Total sessions found

当前查找到的会话总数

【相关命令】

·**reset aspf session**

**ASPF \-- ASPF配置命令 \-- icmp-error drop**

------------------------------------------------------------------------

![说明](ASPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[icmp**-**error drop**]命令用来开启ICMP差错报文检测功能。

**[undo** **icmp**-**error drop**]命令用来恢复缺省情况。

【命令】

**[icmp**-**error drop**]

**[undo** **icmp**-**error drop**]

【缺省情况】

ICMP差错报文检测功能处于关闭状态。

【视图】

ASPF策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

正常ICMP差错报文中均携带有本报文对应连接的相关信息，根据这些信息可以匹配到相应的连接。如果匹配失败，则根据当前配置决定是否丢弃该ICMP报文。

【举例】

\# 设置ASPF策略1丢弃非法的ICMP差错报文。

\<Sysname\> system-view

Sysname aspf policy 1

Sysname-aspf-policy-1 icmp-error drop

【相关命令】

·**aspf policy**

·**display** **aspf** **policy**

**ASPF \-- ASPF配置命令 \-- reset aspf session**

------------------------------------------------------------------------

![说明](ASPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset aspf session**]命令用来删除ASPF的会话表项。

【命令】

集中式设备：

**[reset aspf session **[[ **ipv4 \| ipv6** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset aspf session **[[ **ipv4 \| ipv6** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset aspf session **[[ **ipv4 \| ipv6** ] ]**chassis** *chassis-number***slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：删除ASPF创建的IPv4会话表项。

**[ipv6**]：删除ASPF创建的IPv6会话表项。

**[slot**] *slot-number*：删除指定单板上的所有ASPF创建的会话表项，*slot-number*表示单板所在槽位号。不指定该参数时，删除所有单板上的所有ASPF创建的会话表项。（分布式设备－独立运行模式）

**[slot**] *slot-number*：删除指定成员设备上的所有ASPF创建的会话表项，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，删除所有成员设备上的所有ASPF创建的会话表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：删除指定成员设备/PEX上的所有ASPF创建的会话表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则删除所有成员设备/PEX上的所有ASPF创建的会话表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：删除指定成员设备的指定单板上的所有ASPF创建的会话表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的所有ASPF创建的会话表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定单板上的所有ASPF创建的会话表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则删除所有单板上的所有ASPF创建的会话表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：删除指定CPU上的所有ASPF创建的会话表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

如果不指定**ipv4**和**ipv6**参数，则表示删除ASPF创建的所有会话表项。

【举例】

\# 清除ASPF创建的所有会话表项。

\<Sysname\> reset aspf session

【相关命令】

·**display aspf session**

**ASPF \-- ASPF配置命令 \-- tcp syn-check**

------------------------------------------------------------------------

![说明](ASPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tcp syn-check**]命令用来开启非SYN的TCP首报文丢弃功能。

**[undo** **tcp syn-check**]命令用来恢复缺省情况。

【命令】

**[tcp syn-check**]

**[undo** **tcp syn-check**]

【缺省情况】

不丢弃非SYN的TCP首报文。

【视图】

ASPF策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

ASPF对TCP连接的首报文进行检测，查看是否为SYN报文，如果不是SYN报文则根据当前配置决定是否丢弃该报文。

【举例】

\# 设置ASPF策略1丢弃非SYN的TCP首报文。

\<Sysname\> system-view

Sysname aspf policy 1

Sysname-aspf-policy-1 tcp syn-check

【相关命令】

·**aspf policy**
