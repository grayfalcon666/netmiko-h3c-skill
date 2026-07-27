<!-- CMD-INDEX
  bandwidth                           | Tunnel-Bundle接口视图 | L23
  default                             | Tunnel-Bundle接口视图 | L77
  description                         | Tunnel-Bundle接口视图 | L113
  destination                         | Tunnel-Bundle 接口视图 | L165
  display interface tunnel-bundle     | 任意视图             | L219
  display mpls forwarding protection  | 任意视图             | L485
  display mpls protection             | 任意视图             | L617
  display tunnel-bundle               | 任意视图             | L899
  interface tunnel-bundle protection  | 系统视图             | L1017
  member interface                    | Tunnel-Bundle接口视图 | L1089
  mpls protection                     | 系统视图             | L1145
  protection holdoff                  | Tunnel-Bundle接口视图 | L1191
  protection revertive                | Tunnel-Bundle接口视图 | L1243
  protection switch                   | Tunnel-Bundle接口视图 | L1305
  protection switching-mode bidirectional | Tunnel-Bundle接口视图 | L1379
  psc message-interval                | MPLS保护倒换视图       | L1443
  reset counters interface            | 用户视图             | L1499
  service                             |                  | L1547
  shutdown                            | Tunnel-Bundle接口视图 | L1629
-->

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会对下列内容有影响：

·CBQ队列带宽。具体介绍请参见"ACL和QoS配置指导"中的"[拥塞管理"。]

·链路开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置隧道捆绑接口Tunnel-Bundle2的期望带宽为1000kbit/s。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 bandwidth 1000

【相关命令】

·**display interface tunnel-bundle**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将隧道捆绑接口Tunnel-Bundle2恢复为缺省配置。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 default

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description**]*text*

**[undo description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，比如；"Tunnel-Bundle1 Interface"。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述字符串，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。

本命令仅用于标识某接口，并无特别的功能。使用**display interface**等命令可以看到设置的描述信息。

【举例】

\# 设置接口Tunnel-bundle2的描述信息为"tunnel-bundle2"。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 description tunnel-bundle2

【相关命令】

·**display interface tunnel-bundle**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- destination**

------------------------------------------------------------------------

**[destination**]命令用来配置Tunnel-Bundle接口的隧道目的端地址。

**[undo destination**]命令用来恢复缺省情况。

【命令】

**[destination** *ip-address*]

**[undo destination**]

【缺省情况】

未指定Tunnel-Bundle接口的隧道目的端地址。

【视图】

Tunnel-Bundle 接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：隧道的目的端IPv4地址。

【使用指导】

MPLS L3VPN、MPLS L2VPN和VPLS根据本命令配置的隧道目的端地址，判断捆绑隧道是否可以作为承载VPN业务的公网隧道。远端PE的地址与Tunnel-Bundle接口的隧道目的端地址相同时，该捆绑隧道可以作为MPLS L3VPN、MPLS L2VPN和VPLS的公网隧道。

建议为成员接口和Tunnel-Bundle接口配置相同的目的端地址。如果不同，则需要确保通过成员接口能够到达Tunnel-Bundle接口的目的端地址；否则，会导致流量转发不通。

【举例】

\# 设置隧道捆绑接口Tunnel-Bundle2的隧道目的端地址为2.2.2.2。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 destination 2.2.2.2

【相关命令】

·**display interface tunnel-bundle**

·**display tunnel-bundle**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display interface tunnel-bundle**

------------------------------------------------------------------------

**[display interface tunnel-bundle**]命令用来显示隧道捆绑接口的相关信息。

【命令】

**[display interface** **tunnel-bundle** \*[number * ] \**brief** \**[description**[ \| ]**down ** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number*]：显示指定Tunnel-Bundle接口的信息。*number*表示Tunnel-Bundle接口的编号，取值为已经创建的Tunnel-Bundle接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，则显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**tunnel-bundle**参数，则显示设备支持的所有接口的信息。

·如果指定**tunnel-bundle**参数，不指定*number*参数，则显示所有已创建的Tunnel-Bundle接口的信息。

【举例】

\# 显示接口Tunnel-Bundle100的详细信息。

\<Sysname\> display interface tunnel-bundle 100

Tunnel-Bundle100

Current state: UP

Line protocol state: UP

Description: Tunnel-Bundle100 Interface

Bandwidth: 64kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

Tunnel-Bundle destination unknown

Tunnel type: CRLSP

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

表1-1 display interface tunnel-bundle命令显示信息描述表

字段

描述

Tunnel-Bundle100

接口Tunnel-Bundle100的相关信息

Current state

Tunnel-Bundle接口的物理状态和管理状态，可能的取值及含义如下：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：该接口的管理状态为开启，但物理状态为关闭

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

Tunnel-Bundle接口的链路层协议状态。其值由链路层经过参数协商决定，取值为：

·UP：表示该接口的链路层协议状态为开启

·UP (spoofing)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示该接口的链路层协议状态为关闭

Description

Tunnel-Bundle接口的描述信息

Bandwidth

Tunnel-Bundle接口的期望带宽

Maximum Transmit Unit

Tunnel-Bundle接口的最大传输单元

Internet protocol processing

Tunnel-Bundle接口的IP地址。如果没有为Tunnel-Bundle接口配置IP地址，则该字段显示为Internet protocol processing: disabled，表示不能处理IP报文

Primary表示该IP地址为接口的主IP地址

Tunnel-Bundle destination

Tunnel-Bundle接口的隧道目的端地址，取值为unknown表示未指定Tunnel-Bundle接口的隧道目的端地址

Tunnel type

Tunnel-Bundle接口的隧道模式，目前取值只能为CRLSP

Last clearing of counters

最近一次清除计数时间

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输入速率：

·bytes/sec表示平均每秒输入的字节数

·bits/sec表示平均每秒输入的比特数

·packets/sec表示平均每秒输入的包数

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输出速率：

·bytes/sec表示平均每秒输出的字节数

·bits/sec表示平均每秒输出的比特数

·packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 drops

总计输入的报文数，总计输入的字节，总计丢弃的输入报文数

Output: 0 packets, 0 bytes, 0 drops

总计输出的报文数，总计输出的字节，总计丢弃的输出报文数

\# 显示接口Tunnel-Bundle100的概要信息

\<Sysname\> display interface tunnel-bundle 100 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Tunnel-B100          UP   UP       \--              aaaaaaaaaaaaaaaaaaaaaaaaaaa

\# 显示接口Tunnel-Bundle100的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display interface tunnel-bundle 100 brief  description

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Tunnel-B100          UP   UP       \--              aaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

\# 显示当前物理状态为down的接口的信息以及down的原因。

\<Sysname\> display interface tunnel-bundle brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Tunnel-B100          DOWN Not connected

Tunnel-B101          DOWN Not connected

表1-2 display interface tunnel-bundle brief命令显示信息描述表

字段

描述

Brief information on interface(s) under route mode

三层模式下（route）的接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复端口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"字符串，则表示该接口的链路层协议状态显示是UP的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示本链路物理上是连通的

·DOWN：表示本链路物理上是不通的

·ADM：表示本链路被手工关闭了，需要执行**undo shutdown**命令才能恢复真实的物理状态

Protocol

接口的链路层协议状态。其值由链路层经过参数协商决定，取值为：

·UP：表示该接口的链路层协议状态为开启

·UP (spoofing)：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示该接口的链路层协议状态为关闭

Main IP

接口主IP地址

Description

接口的描述信息

Cause

接口物理连接状态为down的原因，取值为：

·Administratively：表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

·Not connected：表示未成功建立捆绑隧道

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display mpls forwarding protection**

------------------------------------------------------------------------

**[display mpls forwarding protection**]命令用来显示MPLS保护组的转发状态信息。

【命令】

集中式设备：

**[display mpls forwarding protection** **tunnel-bundle** *number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display mpls forwarding protection** **tunnel-bundle** *number*  \**slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－IRF模式：

**[display mpls forwarding protection** **tunnel-bundle** *number*  \**chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[tunnel-bundle***number*]：显示指定Tunnel-Bundle接口对应MPLS保护组的转发状态信息。*number*为Tunnel-Bundle接口的编号，取值为已经创建的Tunnel-Bundle接口的编号。如果不指定本参数，则显示所有MPLS保护组的转发状态信息。

**[slot** *slot-number*]：显示指定单板上MPLS保护组的转发状态信息。*slot-number*为单板所在的槽位号。如果不指定本参数，则显示主用主控板上MPLS保护组的转发状态信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上MPLS保护组的转发状态信息。*slot-number*为设备在IRF中的成员编号。如果不指定本参数，则显示Master设备上MPLS保护组的转发状态信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上MPLS保护组的转发状态信息。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，则显示Master设备上MPLS保护组的转发状态信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* ]**slot** *slot-number*：显示指定成员设备上指定单板的MPLS保护组转发状态信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示Master设备主用主控板上MPLS保护组的转发状态信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* ]**slot** *slot-number*：显示指定单板的MPLS保护组转发状态信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，则显示Master设备主用主控板上MPLS保护组的转发状态信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的MPLS保护组转发状态信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有MPLS保护组的转发状态信息。

\<Sysname\> display mpls forwarding protection

Total number of protection groups: 1

State:

  N: Normal    UA: Unavailable    PA: Protecting administrative

  PF: Protecting failure    WTR: Wait-to-Restore    DNR: Do-not-Revert

  M: Manual switch    F: Forced switch   P: Protection tunnel failure

  W: Working tunnel failure    HO: Hold off    LO: Lockout of protection

  L: Local    R: Remote

Group ID    Working tunnel    Protection tunnel    State

2           100               200                  UA:LO:R

表1-3 display mpls forwarding protection命令显示信息描述表

字段

描述

Group ID

保护组ID

Working tunnel

工作隧道的编号

Protection tunnel

保护隧道的编号

State

本字段的取值由三部分组成：保护组的当前状态、进入该状态的原因及原因的来源

保护组的当前状态取值包括：

·N：表示Normal state，即工作隧道和保护隧道都正常工作，流量在工作隧道上传输

·UA：表示Unavailable state，即保护隧道不可用

·PA：表示Protecting administrative state，即执行外部倒换命令使得流量在保护隧道上传输

·PF：表示Protecting failure state，即工作隧道出现故障，流量倒换到保护隧道上传输

·WTR：表示Wait-to-Restore state，即工作隧道故障恢复后，等待WTR时间将流量从保护隧道回切到工作隧道

·DNR：表示Do-not-Revert state，即工作隧道故障恢复后，不将流量从保护隧道回切到工作隧道

保护组进入某个状态的原因包括：

·LO：表示Lockout of protection，即执行锁定倒换命令

·P：表示通过信令协议检测到保护隧道出现故障

·W：表示通过信令协议检测到工作隧道出现故障

·F：表示Forced switch，即执行强制倒换命令

·M：表示Manual switch，即执行手工倒换命令

·HO：表示Hold off，即工作隧道出现故障后，等待倒换延迟时间，再将流量切换到保护隧道上传输

原因的来源包括：

·L：表示来自于本地

·R：表示来自于远端

例如，UA:LO:L表示由于本地执行锁定倒换命令，导致保护组进入保护隧道不可用状态

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display mpls protection**

------------------------------------------------------------------------

**[display mpls protection**]命令用来显示MPLS保护组的当前运行状态和相关信息。

【命令】

**[display mpls protection ****tunnel-bundle***number***** \**verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[tunnel-bundle*** number*]：显示指定Tunnel-Bundle接口对应MPLS保护组的当前运行状态和相关信息。*number*为Tunnel-Bundle接口的编号，取值为已经创建的Tunnel-Bundle接口的编号。如果不指定本参数，则显示所有MPLS保护组的当前运行状态和相关信息。

**[verbose**]：显示MPLS保护组的详细信息。如果不指定本参数，则显示MPLS保护组的简要信息。

【举例】

\# 显示所有MPLS保护组的当前运行状态和相关信息。

\<Sysname\> display mpls protection

Total number of protection groups: 1

State:

  N: Normal    UA: Unavailable    PA: Protecting administrative

  PF: Protecting failure    WTR: Wait-to-Restore    DNR: Do-not-Revert

  M: Manual switch    F: Forced switch   P: Protection tunnel failure

  W: Working tunnel failure    HO: Hold off    LO: Lockout of protection

  L: Local    R: Remote

Group ID   Type            Working tunnel    Protection tunnel    State

2          Tunnel bundle   100               200                  UA:LO:R

表1-4 display mpls protection命令显示信息描述表

字段

描述

Group ID

保护组ID

Type

保护组的隧道类型，目前取值只能是Tunnel bundle，表示隧道捆绑接口类型

Working tunnel

工作隧道的编号

Protection tunnel

保护隧道的编号

State

本字段的取值由三部分组成：保护组的当前状态、进入该状态的原因及原因的来源

保护组的当前状态取值包括：

·N：表示Normal state，即工作隧道和保护隧道都正常工作，流量在工作隧道上传输

·UA：表示Unavailable state，即保护隧道不可用

·PA：表示Protecting administrative state，即执行外部倒换命令使得流量在保护隧道上传输

·PF：表示Protecting failure state，即工作隧道出现故障，流量倒换到保护隧道上传输

·WTR：表示Wait-to-Restore state，即工作隧道故障恢复后，等待WTR时间将流量从保护隧道回切到工作隧道

·DNR：表示Do-not-Revert state，即工作隧道故障恢复后，不将流量从保护隧道回切到工作隧道

保护组进入某个状态的原因包括：

·LO：表示Lockout of protection，即执行锁定倒换命令

·P：表示通过信令协议检测到保护隧道出现故障

·W：表示通过信令协议检测到工作隧道出现故障

·F：表示Forced switch，即执行强制倒换命令

·M：表示Manual switch，即执行手工倒换命令

·HO：表示Hold off，即工作隧道出现故障后，等待倒换延迟时间，再将流量切换到保护隧道上传输

原因的来源包括：

·L：表示来自于本地

·R：表示来自于远端

例如，UA:LO:L表示由于本地执行锁定倒换命令，导致保护组进入保护隧道不可用状态

\# 显示MPLS保护组的详细信息。

\<Sysname\> display mpls protection verbose

Protection group ID         : 2

   Protection group type    : Tunnel bundle

   Tunnel bundle name       : Tunnel-Bundle200

   Working tunnel           : Tunnel100

   Protection tunnel        : Tunnel200

   Protection mode          : 1:1

   Switching mode           : Bidirectional

   Tunnel in use            : Working-path

   Working tunnel state     : No defect

   Protection tunnel state  : Signal failure

   Holdoff time             : 5s (Remaining: 3s)

   Wait to restore time     : 30s (Remaining: 10s)

   Message interval          : 5s

   Revertive mode           : Revertive

   State                    : Unavailable (UA),

                              Protection tunnel failure (P),

                              Local (L)

表1-5 display mpls protection verbose命令显示信息描述表

字段

描述

Protection group ID

保护组ID

Protection group type

保护组的隧道类型，目前取值只能是Tunnel bundle，表示隧道捆绑接口类型

Tunnel bundle name

保护组关联的隧道捆绑接口名称

Working tunnel

工作隧道的接口名称

Protection tunnel

保护隧道的接口名称

Protection mode

保护模式，取值包括1+1和1:1

Switching mode

切换模式，取值包括：

·Bidirectional：双向切换

·Unidirectional：单向切换

Tunnel in use

当前转发流量使用的隧道，取值包括：

·Working-path：表示当前使用的隧道是工作隧道

·Protection-path：表示当前使用的隧道是保护隧道

Working tunnel state

工作隧道的状态，取值包括：

·No defect：表示没有缺陷

·Signal failure：表示通过信令协议检测出缺陷

·OAM defect：表示通过OAM机制检测出缺陷

·Remote defect：表示从远端接收到的缺陷

Protection tunnel state

保护隧道的状态，取值包括：

·No defect：表示没有缺陷

·Signal failure：表示通过信令协议检测出缺陷

·OAM defect：表示通过OAM机制检测出缺陷

·Remote defect：表示从远端接收到的缺陷

Holdoff time

倒换延迟时间，及当前的倒换延迟剩余时间，单位为秒

Wait to testore time

回切时间，及当前的回切剩余时间，单位为秒

Message interval

PSC控制报文的发送时间间隔，单位为秒

Revertive mode

回切模式，取值包括：

·Revertive：支持回切

·Non-revertive：不支持回切

State

本字段的取值由三部分组成：保护组的当前状态、进入该状态的原因及原因的来源

保护组的当前状态取值包括：

·Normal (N)：表示工作隧道和保护隧道都正常工作，流量在工作隧道上传输

·Unavailable (UA)：表示保护隧道不可用

·Protecting administrative (PA)：表示执行外部倒换命令使得流量在保护隧道上传输

·Protecting failure(PF)：表示工作隧道出现故障，流量倒换到保护隧道上传输

·Wait-to-Restore (WTR)：表示工作隧道故障恢复后，等待WTR时间将流量从保护隧道回切到工作隧道

·Do-not-Revert (DNR)：表示工作隧道故障恢复后，不将流量从保护隧道回切到工作隧道

保护组进入某个状态的原因包括：

·Lockout of protection(LO)：表示执行锁定倒换命令

·Protection tunnel failure(P)：表示通过信令协议检测到保护隧道出现故障

·Working tunnel failure(W)：表示通过信令协议检测到工作隧道出现故障

·Forced switch(F)：表示执行强制倒换命令

·Manual switch(M)：表示执行手工倒换命令

·Hold off(HO)：表示工作隧道出现故障后，等待倒换延迟时间，再将流量切换到保护隧道上传输

原因的来源包括：

·Local(L)：表示来自于本地

·Remote(R)：表示来自于远端

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- display tunnel-bundle**

------------------------------------------------------------------------

**[display tunnel-bundle**]命令用来显示Tunnel-Bundle接口及其成员接口的信息。

【命令】

**[display tunnel-bundle ** *number*]****

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number*]：显示指定Tunnel-Bundle接口及其成员接口的信息。*number*为Tunnel-Bundle接口的编号，取值为已经创建的Tunnel-Bundle接口的编号。如果不指定本参数，则显示所有Tunnel-Bundle接口及其成员接口的信息。

【举例】

\# 显示所有Tunnel-Bundle接口及其成员口的信息。

\<Sysname\> display tunnel-bundle

Total number of tunnel bundles: 1, 1 up, 0 down

Tunnel bundle name: Tunnel-Bundle 2

Bundle state           : Up

Bundle attributes      :

  Working mode         : 1:1

  Tunnel type          : CR-LSP

  Tunnel destination   : 3.3.3.3

Bundle members:

  Member         State        Role

  Tunnel4        Up           Working

  Tunnel5        Up           Protection

表1-6 display tunnel-bundle命令显示信息描述表

字段

描述

Total number of tunnel bundles

Tunnel-Bundle接口的总数，以及处于up、down状态的Tunnel-Bundle接口数目

Tunnel bundle name

Tunnel-Bundle接口的名称

Bundle state

Tunnel-Bundle接口的状态，取值包括up、down

Bundle attributes

Tunnel-Bundle接口的属性

Working mode

Tunnel-Bundle接口的模式，取值包括：

·Load Balancing：表示负载分担模式

·1+1：表示1+1保护倒换模式

·1:1：表示1:1保护倒换模式

Load Balancing模式的详细介绍，请参见"MPLS配置指导"中的"MPLS TE"

Tunnel type

隧道类型，目前取值仅支持CR-LSP

Tunnel destination

Tunnel-Bundle接口的隧道目的端地址

Bundle members

Tunnel-Bundle接口中的成员接口信息

Member

成员接口的名称

State

成员接口的状态

Role

成员接口的角色，取值包括：

·Working：表示成员接口对应的隧道为工作隧道

·Protection：表示成员接口对应的隧道为保护隧道

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- interface tunnel-bundle protection**

------------------------------------------------------------------------

**interface tunnel-bundle protection**命令用来创建保护倒换模式的隧道捆绑接口（Tunnel-Bundle接口），并进入Tunnel-Bundle接口视图。

**[undo interface tunnel-bundle**]命令用来删除指定的Tunnel-Bundle接口。

【命令】

**[interface tunnel-bundle** *number*]****\**[protection ****[ oneplusone**[ \|]** onetoone }** ]

**[undo interface tunnel-bundle** *number*]

【缺省情况】]

设备上不存在任何Tunnel-Bundle接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：Tunnel-Bundle接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[oneplusone**]：指定为1+1保护倒换方式。

**[onetoone**]：指定为1:1保护倒换方式。

【使用指导】

创建保护倒换模式的Tunnel-Bundle接口后，还需要在Tunnel-Bundle接口视图下通过**member interface**命令为Tunnel-Bundle接口指定两个成员接口：一个作为工作隧道，一个作为保护隧道。两条隧道形成一条具有保护作用的MPLS TE捆绑隧道，构成一个MPLS保护组。在MPLS TE保护组内，设备根据外部倒换命令、信令倒换，决定转发流量使用的隧道。

MPLS的保护倒换方式分为如下两种：

·1:1保护倒换：正常情况下，流量在工作隧道上传输；当隧道的头节点或尾节点通过检测机制（如MPLS BFD）发现工作隧道发生故障、或执行外部倒换命令时，通知头节点根据保护倒换状态决定流量在工作隧道或保护隧道上传输。

·1+1保护倒换：在正常情况下，流量在工作隧道、保护隧道上都传输，隧道的尾节点选择从工作隧道上接收流量；当隧道的头节点或尾节点通过检测机制（如MPLS BFD）发现工作隧道发生故障、或执行外部倒换命令时，通知隧道的尾节点根据保护倒换状态决定从工作隧道或保护隧道上接收流量。

需要注意的是：

·创建保护倒换模式的Tunnel-Bundle接口时，必须指定**protection **[{ **oneplusone** \| **onetoone** }]参数；进入已经创建的Tunnel-Bundle接口时，可以不指定该参数。

·不能通过重复执行本命令，修改Tunnel-Bundle接口的保护倒换方式。

【举例】

\# 创建1:1保护倒换方式的隧道捆绑接口Tunnel-Bundle2，并进入Tunnel-Bundle接口视图。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2 protection onetoone

Sysname-tunnel-bundle2

【相关命令】

·**destination**

·**display tunnel bundle**

·**member interface**

·**mpls protection**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- member interface**

------------------------------------------------------------------------

**[member interface**]命令用来为Tunnel-Bundle接口指定成员接口。

**[undo member interface**]命令用来从Tunnel-Bundle接口中删除指定的成员接口。

【命令】

**[member interface tunnel **]*tunnel-number* \**[protection** ]

**[undo member interface tunnel **]*tunnel-number*

【缺省情况】

Tunnel-Bundle接口下不存在任何成员接口。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tunnel-number*]：指定成员接口。*tunnel-number*为Tunnel接口的编号，本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[protection**]：指定该成员接口为备用成员Tunnel接口，即该成员接口对应的MPLS TE隧道为保护隧道。如果不指定本参数，则成员接口为主用成员接口，即该成员接口对应的MPLS TE隧道为工作隧道。

【使用指导】

保护倒换模式的Tunnel-Bundle接口下只能指定两个成员接口：一个主用成员接口和一个备用成员接口。设备根据外部倒换命令、信令倒换，决定转发流量使用的成员接口。

【举例】

\# 配置接口Tunnel-Bundle2的主用成员接口为Tunnel1接口，备用成员接口为Tunnel2接口。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2 protection onetoone

Sysname-tunnel-bundle2 member interface tunnel 1

Sysname-tunnel-bundle2 member interface tunnel 2 protection

【相关命令】

·**display mpls protection**

·**display tunnel-bundle**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- mpls protection**

------------------------------------------------------------------------

**[mpls protection**]命令用来开启MPLS保护倒换功能，并进入MPLS保护倒换视图。

**[undo mpls protection**]命令用来关闭MPLS保护倒换功能。

【命令】

**[mpls protection**]

**[undo mpls protection**]

【缺省情况】

MPLS保护倒换功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有执行本命令开启MPLS保护倒换功能后，才能执行MPLS保护倒换的其他命令。

如果没有开启MPLS保护倒换功能，则保护倒换模式的隧道捆绑接口仅能按照指定的保护倒换方式进行流量转发。只有开启MPLS保护倒换功能后，才能进行MPLS保护倒换操作，如执行外部倒换命令、在隧道的两端协调保护倒换状态等。

如果不开启MPLS保护倒换功能，则创建保护倒换模式的隧道捆绑接口，并为其添加成员接口后，执行**display mpls protection**命令不会显示该接口对应的保护组信息。

【举例】

\# 开启MPLS保护倒换功能，并进入MPLS保护倒换视图。

\<Sysname\> system-view

Sysname mpls protection

Sysname-mpls-protection

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection holdoff**

------------------------------------------------------------------------

**[protection holdoff**]命令用来配置检测到工作隧道发生故障后的倒换延迟时间。

**[undo protection holdoff**]命令用来恢复缺省情况。

【命令】

**[protection holdoff ***holdoff-time*]

**[undo protection holdoff**]

【缺省情况】

倒换延迟时间为0，即检测到工作隧道故障后立即将流量倒换到保护隧道传输。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[holdoff-time*]：倒换延迟时间，取值范围为0～10，单位为秒。

【使用指导】

工作隧道出现故障时，等待倒换延迟时间超时后，再将流量切换到保护隧道上传输。若在倒换延迟时间内，工作隧道恢复正常，则不会进行倒换，避免因网络抖动而引起重复倒换。

只有执行**mpls protection**命令开启MPLS保护倒换功能后，才能执行本命令。

【举例】

\# 配置接口Tunnel-Bundle2的倒换延迟时间为3秒。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2 protection onetoone

Sysname-tunnel-bundle2 protection holdoff 3

【相关命令】

·**mpls protection**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection revertive**

------------------------------------------------------------------------

**[protection revertive**]命令用来配置保护组的回切模式和回切等待时间。

**[undo protection revertive**]命令用来恢复缺省情况。

【命令】

**[protection revertive ****never**[ \| ]**wtr** [ *wtr-time*  }]

**[undo protection revertive**]

【缺省情况】]

工作隧道故障恢复后，流量会立即从保护隧道回切到工作隧道。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[never**]：指定为不回切模式，即工作隧道故障恢复后，流量继续在保护隧道上传输，如果保护隧道未出现故障，则流量不会回切到工作隧道。

**[wtr**]：指定为可回切模式，即工作隧道故障恢复后，流量从保护隧道回切到工作隧道。

*[wtr-time*]：指定回切时间，取值范围为0～3600，单位为秒，缺省值为600秒。工作隧道故障恢复后，如果在回切时间超时时，工作隧道仍然处于正常状态，则将流量从保护隧道回切到工作隧道。

【使用指导】

通常情况下，工作隧道优于保护隧道，两条隧道都正常工作时，应优先使用工作隧道转发流量。工作隧道故障恢复后，流量立即从保护隧道回切到工作隧道，可以确保流量优先使用工作隧道转发。但是在网络抖动的情况下，立即回切可能会导致流量频繁在工作隧道和保护隧道之间倒换，影响流量的正常转发，并增加了设备的负担。通过配置不回切模式或指定回切时间，可以解决上述问题。

需要注意的是：

·隧道两端配置的回切模式和回切时间必须相同。

·只有执行**mpls protection**命令开启MPLS保护倒换功能后，才能执行本命令。

【举例】

\# 配置接口Tunnel-Bundle2对应的保护组工作在可回切模式，并指定回切时间为10秒。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2 protection onetoone

Sysname-tunnel-bundle2 protection revertive wtr 10

【相关命令】

·**mpls protection**

·**protection switching-mode bidirectional**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection switch**

------------------------------------------------------------------------

**[protection switch**]命令用来在指定Tunnel-Bundle接口上执行外部倒换命令。

【命令】

**[protection switch****clear**[ \| ]**force**[ \| ]**lock**[ \| ]**manual** }

【缺省情况】]

未配置外部倒换命令。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[clear**]：表示清除倒换，即清除所有已执行的外部倒换命令。

**[force**]：表示强制倒换，即强制流量在保护隧道上传输。

**[lock**]：表示锁定倒换，即将流量锁定在工作隧道上传输。

**[manual**]：表示手工倒换，即手动将流量从工作隧道倒换到保护隧道上传输，如果保护隧道存在故障，则不进行流量倒换。

【使用指导】

触发流量在工作隧道和保护隧道之间倒换的方式分为外部倒换和信令倒换两类。优先级从高到低依次为：

·清除倒换

·锁定倒换

·强制倒换

·保护隧道的信令倒换，即通过信令协议检测到保护隧道发生故障

·工作隧道的信令倒换，即通过信令协议检测到工作隧道发生故障

·信令清除倒换，即通过信令协议检测到工作隧道或保护隧道故障恢复

·手工倒换

如果同时存在多种触发方式，则由优先级高的触发方式决定当前传输流量的隧道。

需要注意的是：

·只有执行**mpls protection**命令开启MPLS保护倒换功能后，才能执行本命令。

·重复执行本命令指定不同的外部倒换命令时，优先级高的倒换命令覆盖优先级低的倒换命令。设备上已经执行了外部倒换命令时，若要将其修改为低优先级的外部倒换命令，则需要先配置清除倒换（**clear**）命令，再配置低优先级的外部倒换命令。

【举例】

\# 配置接口Tunnel-Bundle2上执行强制倒换。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2 protection oneplusone

Sysname-tunnel-bundle2 protection switch force

【相关命令】

·**mpls protection**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- protection switching-mode bidirectional**

------------------------------------------------------------------------

**[protection **]**switching-mode bidirectional**命令用来配置保护组采用双向路径切换方式。

**[undo protection switching-mode bidirectional**]命令用来恢复缺省情况。

【命令】

**[protection switching-mode bidirectional**]

**[undo protection switching-mode bidirectional**]

【缺省情况】

保护组采用单向路径切换方式。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

MPLS TE隧道为双向隧道时，该隧道可以采用如下方式切换流量转发路径：

·单向路径切换：外部倒换命令或信令倒换触发一个方向的流量进行保护倒换时，只切换该方向流量的转发隧道，另一个方向的转发隧道不受影响。

·双向路径切换：外部倒换命令或信令倒换触发一个方向的流量进行保护倒换时，不仅切换该方向流量的转发隧道，还通过PSC（Protection State Coordination，保护状态协调）控制报文通知远端切换另一个方向流量的转发隧道。

1:1保护倒换支持单向路径切换和双向路径切换；1+1保护倒换只支持双向路径切换。

需要注意的是：

·只有执行**mpls protection**命令开启MPLS保护倒换功能后，才能执行本命令。

·双向路径切换方式要求工作隧道和保护隧道都是双向隧道，且两端保护组都采用双向路径切换方式，否则双向切换功能无法正常运行。

·1+1保护倒换方式只支持双向路径切换方式。

【举例】

\# 配置接口Tunnel-Bundle2对应的保护组采用双向路径切换方式。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2 protection onetoone

Sysname-tunnel-bundle2 protection switching-mode bidirectional

【相关命令】

·**mpls protection**

·**protection holdoff**

·**psc message-interval**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- psc message-interval**

------------------------------------------------------------------------

**[psc message-interval**]命令用来配置PSC控制报文的发送时间间隔。

**[undo psc message-interval**]命令用来恢复缺省情况。

【命令】

**[psc message-interval** *interval*]

**[undo psc message-interval**]

【缺省情况】

PSC控制报文的发送时间间隔为5秒。

【视图】

MPLS保护倒换视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：PSC控制报文的发送时间间隔，取值范围为1～65535，单位为秒。

【使用指导】

采用双向路径切换时，两个方向的隧道需要同时进行切换，因此隧道两端的设备需要周期性发送PSC控制报文来协调隧道两端的保护状态，以达到双向隧道同时切换的目的。

可以根据需要修改PSC控制报文的发送时间间隔，避免协议报文占用过多的带宽和设备资源。

只有执行**mpls protection**命令开启MPLS保护倒换功能后，才能执行本命令。

【举例】

\# 配置PSC控制报文的发送时间间隔为10秒。

\<Sysname\> system-view

Sysname mpls protection

sys-mpls-protection psc message-interval 10

【相关命令】

·**mpls protection**

·**protection switching-mode bidirectional**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除接口的统计信息。

【命令】

**[reset counters interface**] \**[tunnel-bundle** [ *number*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tunnel-bundle**]：指定接口类型为隧道捆绑接口。

*[number*]：隧道捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**tunnel-bundle**，则清除所有接口的统计信息；

·如果指定**tunnel-bundle**而不指定*number*，则清除所有隧道捆绑接口的统计信息；

·如果同时指定**tunnel-bundle**和*number*，则清除指定隧道捆绑接口的统计信息。

【举例】

\# 清除接口Tunnel-Bundle2的统计信息。

\<Sysname\> reset counters tunnel-bundle 2

【相关命令】

·**display interface tunnel-bundle**

·**interface tunnel-bundle**

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- service**

------------------------------------------------------------------------

![说明](MPLS保护倒换命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[service**]命令用来指定转发当前接口流量的业务处理板。

**[undo service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[service slot*** slot-number*]

**[undo service slot**]

分布式设备－IRF模式：

**[service chassis ***chassis-number*]** slot*** slot-number*

**[undo service chassis**]

【缺省情况】

没有指定转发当前接口流量的业务处理板。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：指定转发当前接口流量的单板所在的槽位号。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：指定转发当前接口流量的设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：指定转发当前接口流量的设备/PEX在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* ]**slot** *slot-number*：指定转发当前接口流量的成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* ]**slot** *slot-number*：指定转发当前接口流量的指定单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

如果拔出指定的转发流量业务板，即使Tunnel-Bundle接口UP，流量也转发不通；如果重新插入指定的转发流量业务板，则流量可以恢复在指定板正常转发。

【举例】

\# 指定在2号单板转发接口Tunnel-Bundle2的流量。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 service slot 2

\# 指定在2号成员设备转发接口Tunnel-Bundle2的流量。（集中式IRF设备）

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 service slot 2

\# 指定在2号成员设备的2号板转发接口Tunnel-Bundle2的流量。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2service chassis2 slot 2

**MPLS保护倒换 \-- MPLS保护倒换配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭隧道捆绑接口。

**[undo shutdown**]命令用来打开隧道捆绑接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**shutdown**命令不仅关闭隧道捆绑接口，还会关闭该隧道捆绑接口的成员接口。

【举例】

\# 关闭接口Tunnel-Bundle2。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 shutdown

