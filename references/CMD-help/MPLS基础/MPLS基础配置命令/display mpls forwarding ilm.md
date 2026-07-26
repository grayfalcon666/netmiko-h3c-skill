
**MPLS基础 \-- MPLS基础配置命令 \-- display mpls forwarding ilm**

------------------------------------------------------------------------

**[display** **mpls forwarding ilm**]命令用来显示ILM（Incoming Label Map，入标签映射）表项信息。

【命令】

集中式设备：

**[display mpls forwarding ilm **\*****[label *]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mpls forwarding ilm **\*****[label *  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mpls forwarding ilm** [ *label*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[label*]：显示指定入标签的ILM表项，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定本参数，则显示所有ILM表项信息。

**[slot**]* slot-number***：**显示指定单板上的ILM表项。*slot-number*为单板所在的槽位号。如果不指定本参数，则显示主用主控板上的ILM表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的ILM表项。*slot-number*为设备在IRF中的成员编号。如果不指定本参数，则显示Master设备上的ILM表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的ILM表项。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，则显示Master设备上的ILM表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的ILM表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示Master设备主用主控板上的ILM表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis **]*chassis-number* **slot** *slot-number*：显示指定单板的ILM表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，则显示Master设备主用主控板上的ILM表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ILM表项。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

ILM用于根据入标签查找对应的标签操作类型、出标签值等。LSR接收到带有标签的报文后，根据报文中的栈顶标签值查找对应的ILM表项，执行相应的标签操作，并转发该报文。

【举例】

\# 显示指定入标签的ILM表项。

\<Sysname\> display mpls forwarding ilm 30

Flags: T - Forwarded through a tunnel

       N - Forwarded through the outgoing interface to the nexthop IP address

       B - Backup forwarding information

       A - Active forwarding information

InLabel Oper    VRF   Flag SwapLabel Forwarding Info

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

30      SWAP    0     T    1300      1024

\# 显示所有ILM表项。

\<Sysname\> display mpls forwarding ilm

Total ILM entries: 3

Flags: T - Forwarded through a tunnel

       N - Forwarded through the outgoing interface to the nexthop IP address

       B - Backup forwarding information

       A - Active forwarding information

InLabel Oper    VRF   Flag SwapLabel Forwarding Info

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

30      SWAP    0     T    1300      1024

1279    POP     0     -    -         -

1407    SWAP    0     NA   1271      GE1/0/3                   50.2.0.2

                      NB   1270      Tun0                     0.0.0.0

表1-1 display mpls forwarding ilm命令显示信息描述表

字段

描述

Total ILM entries

ILM表项总数

InLabel

入标签

Oper

操作类型，取值包括：

·POP：弹出标签

·POPGO：弹出标签，并将报文转发到另一条隧道

·SWAP：交换标签

VRF

VPN实例的索引

Flag

转发标记，取值包括：

·T：隧道转发

·N：出接口/下一跳转发

·B：备份转发信息

·A：在用转发信息

SwapLabel

交换的标签值，即出标签值

Forwarding Info

转发信息

·转发标记为N时，转发信息为出接口和下一跳

·转发标记为T时，转发信息为NID

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls forwarding nhlfe**

------------------------------------------------------------------------

**[display** **mpls forwarding nhlfe**]命令用来显示NHLFE（Next Hop Label Forwarding Entry，下一跳标签转发项）表项信息。

【命令】

集中式设备：

**[display mpls forwarding nhlfe **\*****[nid* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mpls forwarding nhlfe **\*****[nid*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mpls forwarding nhlfe** [ *nid*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[nid*]：显示指定NHLFE表项的信息。*nid*为NHLFE表项索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果不指定本参数，则显示所有NHLFE表项信息。

**[slot*** slot-number*]：显示指定单板上的NHLFE表项。*slot-number*为单板所在的槽位号。如果不指定本参数，则显示主用主控板上的NHLFE表项。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的NHLFE表项。*slot-number*为设备在IRF中的成员编号。如果不指定本参数，则显示Master设备上的NHLFE表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的NHLFE表项。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，则显示Master设备上的NHLFE表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的NHLFE表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示Master设备主用主控板上的NHLFE表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板的NHLFE表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，则显示Master设备主用主控板上的NHLFE表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的NHLFE表项。*cpu-number*表示单板上CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

NHLFE表项描述了标签的转发信息（如出标签、出接口等），NHLFE表项主要用于为报文添加多层标签的情况。需要为报文添加多层标签时，LSR首先通过FIB表项或ILM表项获取最内层标签和对应的NHLFE表项索引，然后根据NHLFE表项索引查找NHLFE表项，从该表项中获取报文的外层标签。

【举例】

\# 显示索引号为2048的NHLFE表项。

\<Sysname\> display mpls forwarding nhlfe 2048

Flags: T - Forwarded through a tunnel

       N - Forwarded through the outgoing interface to the nexthop IP address

       B - Backup forwarding information

       A - Active forwarding information

NID        Tnl-Type Flag OutLabel Forwarding Info

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

2048       LSP      NA   2025     GE1/0/2                   10.11.112.26

\# 显示所有的NHLFE表项。

\<Sysname\> display mpls forwarding nhlfe

Total NHLFE entries: 5

Flags: T - Forwarded through a tunnel

       N - Forwarded through the outgoing interface to the nexthop IP address

       B - Backup forwarding information

       A - Active forwarding information

NID        Tnl-Type Flag OutLabel Forwarding Info

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

10         -        TA   -        2049

20         -        TA   -        2050

2048       LSP      NA   2025     GE1/0/2                   10.11.112.26

2049       LSP      NA   3024     GE1/0/2                   10.11.112.26

TB   3026     20

2050       LSP      NA   3025     GE1/0/1                   10.11.113.26

表1-2 display mpls forwarding nhlfe命令显示信息描述表

字段

描述

Total NHLFE entries

NHLFE表项总数

NID

NHLFE表项索引

Tnl-Type

隧道类型，取值包括：

·LOCAL：表示直连下一跳对应的LSP隧道

·LSP：表示静态LSP隧道、采用LDP或BGP协议建立的LSP隧道

·TE：表示MPLS TE隧道接口对应的隧道

·GRE：表示GRE隧道

·CRLSP：表示静态CRLSP隧道或采用RSVP协议建立的CR-LSP隧道

·-：表示隧道类型为无效值

Flag

转发标记，取值包括：

·T：隧道转发

·N：出接口/下一跳转发

·B：备份转发信息

·A：在用转发信息

OutLabel

出标签值

Forwarding Info

转发信息

·转发标记为N时，转发信息为出接口和下一跳

·转发标记为T时，转发信息为NID

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls interface**

------------------------------------------------------------------------

**[display mpls interface**]命令用来显示使能了MPLS能力接口的MPLS相关信息。

【命令】

**[display mpls interface** [ *interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：显示指定接口的MPLS相关信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则显示所有使能了MPLS能力接口的MPLS相关信息。

【举例】

\# 显示所有使能了MPLS能力接口的MPLS相关信息。

\<Sysname\> display mpls interface

Interface               Status       MPLS MTU

GE1/0/1                  Up           1514

GE1/0/2                  Up           1514

表1-3 display mpls interface命令显示信息描述表

字段

描述

Interface

接口名称

Status

接口状态

MPLS MTU

接口的MPLS MTU，单位为字节

【相关命令】

·**mpls enable**

·**mpls mtu**

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls label**

------------------------------------------------------------------------

**[display mpls label**]命令用来显示MPLS标签的使用状态。

【命令】

**[display mpls label** { *label-value1* [ **to** *label-value2*  \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[label-value1*]：显示指定标签的使用状态。*label-value1*为标签值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。当与*label-value2*一起使用时，*label-value1*表示标签范围的起始值。

**[to ***label-value2*]：标签范围的结束值。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果同时指定了*label-value1*和本参数，则显示*label-value1*到*label-value2*之间标签的使用状态。

**[all**]：显示所有标签的使用状态。

【举例】

\# 显示900～902之间标签的使用状态。

\<Sysname\> display mpls label 900 to 902

Label          Owner          State

900            -              Idle

901            -              Idle

902            LDP            Alloc

表1-4 display mpls label命令显示信息描述表

字段

描述

Label

标签值

Owner

标签使用者，即使用该标签的协议，取值包括：LDP、BGP、RSVP和L2VPN

State

标签的使用状态，取值包括：

·Idle：标签空闲

·Alloc：标签已被申请

·Pending：标签已释放，但仍被LSP表项使用

·Inuse：标签已被申请，同时被LSP表项使用

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls lsp**

------------------------------------------------------------------------

**[display mpls lsp**]命令用来显示LSP（Label Switched Path，标签交换路径）信息。

【命令】

**[display mpls lsp**[ [ **egress** \| **in-label** *label-value* \| **ingress** \| **outgoing-interface** *interface-type interface-number* \| **protocol** { **bgp** \| **ldp** *\|* **local** \| **rsvp-te** \| **static** \| **static-cr** } \| **transit**  ]  **vpn-instance** *vpn-instance-name*  [ *ipv4-dest mask-length* \| **ipv6** [ *ipv6-dest prefix-length* ] ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[egress**]：显示本设备作为出节点的LSP信息。

**[in-label*** label-value*]：显示以指定值为入标签的LSP信息。*label-value*为标签值，取值范围为0～1048575。

**[ingress**]：显示本设备作为入节点的LSP信息。

**[outgoing-interface ***interface-type interface-number*]：显示以指定接口为出接口的LSP信息。*interface-type interface-number*为接口类型和接口编号。

**[protocol**]：根据建立LSP的协议类型显示LSP信息。

**[bgp**]：显示BGP LSP信息。

**[ldp**]：显示LDP LSP信息。

**[local**]：显示直连下一跳、MPLS TE隧道接口、隧道捆绑接口对应的LSP信息。

**[rsvp-te**]：显示RSVP-TE建立的CR-LSP信息。

**[static**]：显示手工配置的静态LSP信息。

**[static-cr**]：显示手工配置的静态CR-LSP信息。

**[transit**]：显示本设备作为中间节点的LSP信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的LSP信息。*vpn-instance-name*表示VPN实例名称，为1～31字符的字符串，区分大小写。如果不指定本参数，则显示公网的LSP信息。

*[i*]*pv4-dest mask-length*：显示到达指定IPv4 FEC的LSP信息。*ipv4-dest*为FEC的目的IPv4地址；*mask-length*为FEC目的IPv4地址的掩码长度，取值范围为0～32。

**[ipv6**]：显示IPv6的LSP信息。如果不指定本参数，则显示IPv4的LSP信息。

*[i*]*pv6-dest prefix-length*：显示到达指定IPv6 FEC的LSP信息。*ipv6-dest*为FEC的目的IPv6地址；*prefix-length*为FEC目的IPv6地址的前缀长度，取值范围为0～128。

**[verbose**]：显示LSP的详细信息。如果不指定本参数，则显示LSP的简要信息。

【使用指导】

如果没有指定任何参数，则显示所有LSP的简要信息；如果只指定了**verbose**参数，则显示所有LSP的详细信息。

【举例】

\# 显示所有IPv4 LSP的简要信息。

\<Sysname\> display mpls lsp

FEC                         Proto    In/Out Label    Interface/Out NHLFE

100.100.100.100/24          LDP      -/1049          Vlan20

Backup                               -/1050          Vlan21

100.100.100.10/24           LDP      -/1051          Vlan22

Backup                               -/1050          Vlan21

100.100.100.10/24           LDP      -/1049          Vlan30

101.100.100.10/24           LDP      1026/1049       Vlan20

102.100.100.10/24           LDP      1027/-          -

103.100.100.10/24           LDP      1028/1049       Tunnel10

110.100.100.20/24           BGP      -/1049          Vlan20

111.100.100.10/24           BGP      2028/1049       Vlan20

112.100.100.10/24           BGP      2029/-          Vlan20

113.100.100.10/24           BGP      2030/1049       NHLFE1500

114.100.100.10/24           BGP      2031/1050       Tunnel100

100.100.100.100             Local    -/-             Vlan20

101.101.101.101/32          Static   -/100           Vlan20

-                           Static   100/200         Vlan20

-                           Static   101/-           Vlan20

200.200.200.200/64000/64000 RSVP     -/1030          Vlan10

201.200.200.200/64000/64000 RSVP     1024/1031       Vlan10

202.200.200.200/64000/64000 RSVP     1025/-          -

150.140.150.100/64001/0     StaticCR -/1000          Vlan10

-                           StaticCR 50/1001         Vlan10

-                           StaticCR 51/-            -

表1-5 display mpls lsp命令显示信息描述表

字段

描述

FEC

转发等价类，包括以下形式：

·IP地址/掩码：表示根据目的地址划分FEC

·IP地址：表示根据下一跳地址划分FEC

·IP地址/Out Label：表示根据下一跳地址和出标签划分FEC

·Ingress LSR ID/Tunnel ID/LSP ID：表示RSVP TE的FEC

·-：表示静态Transit LSP、静态Egress LSP、静态Transit CR-LSP或静态Egress CR-LSP

如果显示为"Backup"，则表示该LSP是前一条LSP的备份LSP

Proto

标签分发协议，取值包括：

·LDP：表示该LSP为采用LDP协议建立的LDP LSP

·BGP：表示该LSP为采用BGP协议建立的BGP LSP

·RSVP：表示该LSP为采用RSVP协议建立的CR-LSP

·Static：表示该LSP为手工配置的静态LSP

·StaticCR：表示该LSP为手工配置的静态CR-LSP

·Local：表示该LSP为直连下一跳、MPLS TE隧道接口、隧道捆绑接口对应的LSP

In/Out Label

入标签值/出标签值

Interface/Out NHLFE

出接口名称或NHLFE索引

取值为NHLFE*number*时，表示该LSP迭代到NID为*number*的NHLFE表项对应的Ingress LSP

\# 显示所有IPv6 LSP的简要信息。

\<Sysname\> display mpls lsp ipv6

FEC      : 100:100:100:100:100:100:100:100/128

Protocol : BGP      In-Label     : 2050

Out-Label: 10003    Out-Interface: Vlan10

BkLabel  : 10004    BkInterface  : Vlan20

表1-6 display mpls lsp ipv6命令显示信息描述表

字段

描述

FEC

转发等价类，包括以下形式：

·IP地址/掩码：表示根据目的地址划分FEC

·IP地址：表示根据下一跳地址划分FEC

·IP地址/Out Label：表示根据下一跳地址和出标签划分FEC

·Ingress LSR ID/Tunnel ID/LSP ID：表示RSVP TE的FEC

·-：表示静态Transit LSP、静态Egress LSP、静态Transit CR-LSP或静态Egress CR-LSP

Protocol

标签分发协议，取值包括：

·LDP：表示该LSP为采用LDP协议建立的LDP LSP

·BGP：表示该LSP为采用BGP协议建立的BGP LSP

·RSVP：表示该LSP为采用RSVP协议建立的CR-LSP

·Static：表示该LSP为手工配置的静态LSP

·StaticCR：表示该LSP为手工配置的静态CR-LSP

·Local：表示该LSP为直连下一跳、MPLS TE隧道接口、隧道捆绑接口对应的LSP

In-Label

入标签值

Out-Label

出标签值

Out-Interface

出接口

BkLabel

备份LSP的出标签值

BkInterface

备份LSP的出接口

\# 显示所有LSP的详细信息。

\<Sysname\> display mpls lsp verbose

Destination  : 56.10.10.2

FEC          : 56.10.10.2/32

Protocol     : LDP

LSR Type     : Egress

Service      : Statistics

In-Label     : 1024       

State        : Active

Inbound Statistics:

  Octets    : 13000

  Packets   : 100

  Errors    : 0

  Discards  : 0

Destination  : 56.10.10.4

FEC          : 56.10.10.2/32

Protocol     : LDP

LSR Type     : Transit

Service      : Statistics

In-Label     : 1026

Inbound Statistics:

  Octets    : 10600

  Packets   : 100

  Errors    : 0

  Discards  : 0

Path ID      : 0x40000000.1

State        : Active

Out-Label    : 1800

Nexthop      : 10.1.1.2

Out-Interface: Vlan10

BkLabel      : 1900

BkNexthop    : 20.1.1.2

BkInterface   : Vlan20

Outbound Statistics:

  Octets    : 12600

  Packets   : 100

  Errors    : 0

  Discards  : 0

Destination  : 56.10.10.4

FEC          : 56.10.10.2/32

Protocol     : LDP

LSR Type     : Ingress

Service      : -      

NHLFE ID     : 2000

State        : Active

Out-Label    : 1800

Nexthop      : 10.1.1.2

Out-Interface: Vlan10

表1-7 display mpls lsp verbose命令显示信息描述表

字段

描述

Destination

LSP的目的地址

FEC

转发等价类，包括以下形式：

·IP地址/掩码：表示根据目的地址划分FEC

·IP地址：表示根据下一跳地址划分FEC

·IP地址/Out Label：表示根据下一跳地址和出标签划分FEC

·Ingress LSR ID/Tunnel ID/LSP ID：表示RSVP TE的FEC

·-：表示静态Transit LSP、静态Egress LSP、静态Transit CR-LSP或静态Egress CR-LSP

Protocol

标签分发协议，取值包括：

·LDP：表示该LSP为采用LDP协议建立的LDP LSP

·BGP：表示该LSP为采用BGP协议建立的BGP LSP

·RSVP：表示该LSP为采用RSVP协议建立的CR-LSP

·Static：表示该LSP为手工配置的静态LSP

·StaticCR：表示该LSP为手工配置的静态CR-LSP

·Local：表示该LSP为直连下一跳、MPLS TE隧道接口、隧道捆绑接口对应的LSP

LSR Type

LSR类型，取值包括：

·Ingress：LSP的入节点

·Transit：LSP的中间节点

·Egress：LSP的出节点

Service

LSP上部署的业务，目前仅支持Statistics，表示MPLS转发统计功能

In-Label

入标签值

Path ID

转发路径，取值为0xnn.m，nn表示承载本层LSP的外层LSP的NHLFE组ID，m表示等价路径编号

NHLFE ID

NHLFE表项索引

State

LSP状态，取值包括：

·Active：LSP正在使用

·Inactive：LSP空闲未用

Inbound Statistics

入方向的MPLS转发统计信息，包括入方向接收的字节数（Octets）、接收的报文数（Packets）、接收的错误报文数（Errors）和丢弃的报文数（Discards）

Out-Label

出标签值

Nexthop

下一跳地址

Out-Interface

出接口

BkLabel

备份LSP的出标签值

BkNexthop

备份LSP的下一跳地址

BkInterface

备份LSP的出接口

Outbound Statistics

出方向的MPLS转发统计信息，包括出方向发送的字节数（Octets）、发送的报文数（Packets）、错误报文数（Errors）和丢弃的报文数（Discards）

【相关命令】

·**display mpls lsp statistics**

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls lsp statistics**

------------------------------------------------------------------------

**[display mpls lsp statistics**]命令用来显示LSP的统计信息。

【命令】

**[display mpls lsp statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示LSP的统计信息。

\<Sysname\> display mpls lsp statistics

LSP Type      Ingress/Transit/Egress  Active

Static LSP    0/0/0                   0/0/0

Static CRLSP  0/0/0                   0/0/0

LDP LSP       2/2/1                   2/2/1

RSVP CRLSP    0/0/0                   0/0/0

BGP LSP       0/0/0                   0/0/0

Local LSP     2/0/0                   2/0/0

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Total         4/2/1                   4/2/1

表1-8 display mpls lsp statistics命令显示信息描述表

字段

描述

LSP Type

LSP的类型，取值包括：

·Static LSP：静态LSP

·Static CRLSP：静态CR-LSP

·LDP LSP：通过LDP建立的LSP

·Local LSP：直连下一跳、MPLS TE隧道接口、隧道捆绑接口对应的LSP

·RSVP CRLSP：通过RSVP建立的CR-LSP

·BGP LSP：通过BGP建立的LSP

Total

各种类型LSP的总数

Ingress

本设备作为入节点的LSP数量

Transit

本设备作为中间节点的LSP数量

Egress

本设备作为出节点的LSP数量

Active

处于可用状态的各种类型LSP的数量

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls nib**

------------------------------------------------------------------------

**[display mpls nib**]命令用来显示MPLS的NIB（Nexthop Information Base，下一跳信息库）信息。

【命令】

**[display mpls nib ** *nib-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[nib-id*]：显示指定MPLS下一跳的信息。*nib-id*为MPLS下一跳的索引，取值范围为1～FFFFFFFFFFFFFFFE。如果不指定本参数，则显示所有MPLS下一跳的信息。

【举例】

\# 显示所有MPLS下一跳的信息。

\<Sysname\> display mpls nib

NIB ID: 0x40000000

  Users: 1

  Status: Active

  ECMP number: 1

      Outgoing NHLFE ID: 1024

      Backup outgoing NHLFE ID: 1027

表1-9 display mpls nib命令显示信息描述表

字段

描述

NIB ID

MPLS下一跳索引

Users

引用该MPLS下一跳的ILM表项数目

Status

MPLS下一跳的状态，取值包括：

·Active，激活表项

·Dummy，非激活表项

ECMP number

等价路径数目

Outgoing NHLFE ID

MPLS下一跳对应的NHLFE表项索引

Backup outgoing NHLFE ID

MPLS下一跳对应的备份NHLFE表项的索引

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls nid**

------------------------------------------------------------------------

**[display mpls nid**]命令用来显示NHLFE表项索引的使用状态。

【命令】

**[display mpls nid ** *nid-value1*  **to** *nid-value2*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[nid-value1*]：显示指定NHLFE表项索引的使用状态。*nid-value1*为NHLFE表项索引，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。当与*nid-value2*一起使用时，*nid-value1*表示索引范围的起始值。

**[to ***nid-value2*]：NHLFE表项索引，表示索引范围的结束值。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果同时指定了*nid-value1*和本参数，则显示*nid-value1*到*nid-value2*之间的NHLFE表项索引的使用状态。

【使用指导】

设备上的NHLFE表项索引（该索引为32位二进制数）分为两类：

·固定NHLFE表项索引：设备为隧道接口或隧道捆绑接口生成的NHLFE表项索引，该索引的高4位为非0值。

·动态NHLFE表项索引：设备为LDP LSP、静态LSP、CRLSP等协议生成的LSP分配的NHLFE表项索引，该索引的高4位为0。

本命令只能用来显示动态NHLFE表项索引的使用状态。

执行本命令时，如果不指定任何参数，则显示所有动态NHLFE表项索引的使用状态。

【举例】

\# 显示1028～1500之间的NHLFE表项索引的使用状态。

\<Sysname\> display mpls nid 1028 to 1500

NID alloc state: \'.\' means not used, \'\$\' means used

1028   :\...\$\.... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....

1092   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....

1156   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....

1220   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....

1284   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....

1348   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....

1412   :\...\..... \...\..... \...\..... \...\.....  \...\..... \...\..... \...\..... \...\.....

1476   :\...\..... \...\..... \...\..... .

表1-10 display mpls nid命令显示信息描述表

字段

描述

NID alloc state

NID使用状态

\'.\' means not used

"."表示没有使用

\'\$\' means used

"\$"表示已经使用

**MPLS基础 \-- MPLS基础配置命令 \-- display mpls summary**

------------------------------------------------------------------------

**[display mpls summary**]命令用来显示MPLS汇总信息。

【命令】

**[display mpls summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示MPLS汇总信息。

\<Sysname\> display mpls summary

MPLS LSR ID      : 2.2.2.2

Egress Label Type: Implicit-null

Labels:

  Range           Idle

  16-1023         1008

  1024-1000000    998849

Protocols:

  Type            State

  LDP             Normal

  Static          Normal

表1-11 display mpls summary命令显示信息描述表

字段

描述

MPLS LSR ID

MPLS LSR标识符

Egress Label Type

Egress向倒数第二跳通告的标签类型，取值包括：

·Implicit-null：隐式空标签

·Explicit-null：显式空标签

·Non-null：非空标签

Labels

标签相关信息

Range

标签范围

Idle

标签范围内空闲的标签数目

Protocols

生成LSP的标签分发协议及其运行状态

Type

协议类型，取值包括：LDP、BGP、RSVP、Static、StaticCR、TE、CCC

State

标签分发协议运行状态，取值包括：

·Normal：正常状态

·Recover：协议处于GR期间

**MPLS基础 \-- MPLS基础配置命令 \-- ftn enable**

------------------------------------------------------------------------

![说明](MPLS基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ftn enable**]命令用来开启RIB的FTN表项维护功能。

**[undo ftn enable**]命令用来恢复缺省情况。

【命令】

**[ftn enable**]

**[undo ftn enable**]

【缺省情况】

RIB的FTN表项维护功能处于关闭状态。

【视图】

RIB IPv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

FTN（FEC to NHLFE map，FEC到NHLFE表项的映射）表项是一类特殊的FIB表项，该类FIB表项中包含出标签值信息。如果报文的目的IP地址匹配FTN表项，则为报文添加该表项中的出标签值后，转发该报文。

只有执行本命令开启RIB的FTN表项维护功能后，设备才会将FTN表项学习到RIB中，才能进一步执行**mpls-forwarding statistics prefix-list**命令，使能指定目的网络的FTN转发统计功能。否则，不会对FTN转发进行统计。

【举例】

\# 开启RIB的FTN表项维护功能。

\<Sysname\> system-view

Sysname rib

system-rib address-family ipv4

system-rib-ipv4 ftn enable

【相关命令】

·**mpls-forwarding statistics prefix-list**

**MPLS基础 \-- MPLS基础配置命令 \-- mpls-forwarding statistics prefix-list**

------------------------------------------------------------------------

![说明](MPLS基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls-forwarding statistics prefix-list**]命令用来使能指定目的网络的FTN转发统计功能。

**[undo mpls-forwarding statistics prefix-list**]命令用来关闭指定目的网络的FTN转发统计功能。

【命令】

**[mpls-forwarding statistics prefix-list ***prefix-list-name*]

**[undo mpls-forwarding statistics prefix-list ***prefix-list-name*]

【缺省情况】

所有目的网络的FTN转发统计功能均处于关闭状态。

【视图】

RIB IPv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix-list-name*]：IPv4地址前缀列表，为1～63个字符的字符串，区分大小写。只有目的网络地址通过IPv4地址前缀列表的过滤，才会使能该目的网络的FTN转发统计功能。

【使用指导】

FTN转发是指接收到不带标签的报文，为其添加标签后转发该报文。本命令用来使能FTN转发的统计功能。

MPLS标签转发是指接收到带有标签的报文后，根据报文中的入标签转发该报文。MPLS标签转发的统计功能通过**mpls statistics**命令使能。

执行本命令前，必须先执行**ftn enable**命令开启RIB的FTN表项维护功能。

【举例】

\# 使能目的网络2.2.2.0/24的FTN转发统计功能。

\<Sysname\> system-view

Sysname ip prefix-list abc permit 2.2.2.0 24

Sysname rib

system-rib address-family ipv4

system-rib-ipv4 ftn enable

system-rib-ipv4 mpls-forwarding statistics prefix-list abc

【相关命令】

·**ftn enable**

·**mpls statistics**

·**mpls statistics interval**

**MPLS基础 \-- MPLS基础配置命令 \-- mpls enable**

------------------------------------------------------------------------

**[mpls enable**]命令用来使能接口的MPLS能力。

**[undo mpls enable**]命令用来关闭接口的MPLS能力。

【命令】

**[mpls enable**]

**[undo mpls enable**]

【缺省情况】

未使能接口的MPLS能力。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使能MPLS能力。

\<Sysname\> System-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls enable

·交换应用

\# 在接口Vlan-interface2上使能MPLS能力。

\<Sysname\> System-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mpls enable

【相关命令】

·**display mpls interface**

**MPLS基础 \-- MPLS基础配置命令 \-- mpls forwarding split-horizon**

------------------------------------------------------------------------

![说明](MPLS基础命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls forwarding split-horizon**]命令用来开启MPLS转发的水平分割功能。

**[undo mpls forwarding split-horizon**]命令用来恢复缺省情况。

【命令】

**[mpls forwarding split-horizon**]

**[undo mpls forwarding split-horizon**]

【缺省情况】

未开启MPLS转发的水平分割功能。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启MPLS转发的水平分割功能。

\<Sysname\> system-view

Sysname mpls forwarding split-horizon

**MPLS基础 \-- MPLS基础配置命令 \-- mpls label advertise**

------------------------------------------------------------------------

**[mpls label advertise**]命令用来配置设备作为Egress节点时分配的标签类型，即向倒数第二跳通告的标签类型。

**[undo mpls label advertise**]命令用来恢复缺省情况。

【命令】

**[mpls label advertise**[ { **explicit-null** \| **implicit-null** \| **non-null** }]]

**[undo mpls label advertise**]

【缺省情况】

设备作为Egress节点时，向倒数第二跳通告隐式空标签（**implicit-null**）。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[explicit-null**]：指定设备作为Egress节点时，向倒数第二跳通告显式空标签，标签值为0。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[implicit-null**]：指定设备作为Egress节点时，向倒数第二跳通告隐式空标签，标签值为3。

**[non-null**]：指定设备作为Egress节点时，向倒数第二跳通告非空标签。非空标签的支持情况和取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·请根据实际情况选择Egress节点分配的标签类型：如果倒数第二跳节点支持PHP（Penultimate Hop Popping，倒数第二跳弹出）功能，则建议采用隐式空标签；如果在简化Egress节点转发处理的同时，希望Egress节点能够根据标签中的TC等信息决定QoS策略，则建议采用显式空标签；非空标签只使用在一些比较特殊的场景，比如Egress节点上部署了OAM，只有根据标签才能对应到OAM功能实体的情况，通常情况下不建议使用非空标签。

·设备作为倒数第二跳节点时，允许Egress节点向其通告显式空标签、隐式空标签和非空标签。

·对于LDP LSP，执行**mpls label advertise**命令修改Egress分配的标签类型后，已经建立的LDP LSP会被拆除，并根据新的标签类型重新建立。

·对于BGP LSP，**mpls label advertise**命令只对新建立的BGP LSP生效，执行本命令前已经建立的BGP LSP不受影响。若要使本命令对已经建立的BGP LSP生效，则需要从BGP路由表中删除BGP LSP对应的路由，并重新引入该路由。

【举例】

\# 配置设备作为Egress节点时，向倒数第二跳通告显式空标签。

\<Sysname\> system-view

Sysname mpls label advertise explicit-null

【相关命令】

·**reset mpls ldp**（MPLS命令参考/LDP）

**MPLS基础 \-- MPLS基础配置命令 \-- mpls lsr-id**

------------------------------------------------------------------------

**[mpls lsr-id**]命令用来配置本节点的LSR ID。

**[undo mpls lsr-id**]命令用来删除LSR的ID。

【命令】

**[mpls lsr-id** *lsr-id*]

**[undo mpls lsr-id**]

【缺省情况】

未配置本节点的LSR ID。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsr-id*]：LSR的ID，点分十进制格式，用于标识一个LSR。

【使用指导】

推荐使用LSR上某个Loopback接口的地址作为LSR ID。

【举例】

\# 配置本节点的LSRID为3.3.3.3。

\<Sysname\> system-view

Sysname mpls lsr-id 3.3.3.3

【相关命令】

·**lsr-id**（MPLS命令参考/LDP）

**MPLS基础 \-- MPLS基础配置命令 \-- mpls mtu**

------------------------------------------------------------------------

**[mpls mtu**]命令用来配置接口的MPLS MTU值。

**[undo** **mpls mtu**]命令用来恢复缺省情况。

【命令】

**[mpls mtu ***value*]

**[undo mpls mtu**]

【缺省情况】

未配置接口的MPLS MTU值，此时根据接口的MTU值进行分片，分片的长度不包含MPLS标签栈的长度，为分片添加MPLS标签栈后MPLS报文的长度可能会大于接口MTU的值。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接口的MPLS MTU值，取值范围为46～65535，单位为字节。

【使用指导】

·只有在接口上使能MPLS功能后，该命令才会生效。

·配置的MPLS MTU值大于接口MTU时，有可能导致数据转发失败。

·MPLS TE隧道接口不支持本命令。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1的MPLS MTU值为1000。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls enable

Sysname-GigabitEthernet1/0/1 mpls mtu 1000

·交换应用

\# 配置接口Vlan-interface2的MPLS MTU值为1000。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mpls enable

Sysname-Vlan-interface2 mpls mtu 1000

【相关命令】

·**display mpls interface**

**MPLS基础 \-- MPLS基础配置命令 \-- mpls statistics**

------------------------------------------------------------------------

![说明](MPLS基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls statistics**]命令用来使能指定LSP的MPLS标签转发统计功能。

**[undo mpls statistics**]命令用来关闭指定LSP的MPLS标签转发统计功能。

【命令】

**[mpls statistics **[{ **all** \| [ **vpn-instance** *vpn-instance-name* ] { **ipv4** *ipv4-destination mask-length* \| **ipv6** *ipv6-destination prefix-length* } \| **static** \| **te** *ingress-lsr-id tunnel-id* }]]

**[undo mpls statistics **[{ **all** \| [ **vpn-instance** *vpn-instance-name* ] { **ipv4** *ipv4-destination mask-length* \| **ipv6** *ipv6-destination prefix-length* } \| **static** \| **te** *ingress-lsr-id tunnel-id* }]]

【缺省情况】

所有LSP的MPLS标签转发统计功能均处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：统计所有LSP的信息。

**[vpn-instance** *vpn-instance-name*]：统计指定VPN实例的LSP信息。*vpn-instance-name*表示VPN实例名称，为1～31字符的字符串，区分大小写。如果没有指定本参数，则统计公网的LSP信息。

**[ipv4 ***ipv4-destination mask-length*]：统计指定FEC对应IPv4 LSP的信息。*ipv4-destination*为FEC的IPv4目的地址，*mask-length*为FEC目的地址的掩码长度，取值范围为0～32。

**[ipv6** *ipv6-destination prefix-length*]：统计指定FEC对应BGP-IPv6 LSP的信息。*ipv6-destination*为FEC的IPv6目的地址，*prefix-length*为FEC目的地址的前缀长度，取值范围为0～128。

**[static**]：统计静态LSP和静态CR-LSP的信息。

**[te** *ingress-lsr-id tunnel-id*]：统计指定RSVP-TE隧道的信息。*ingress-lsr-id*为入节点的LSR ID，*tunnel-id*为隧道ID，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

MPLS标签转发是指接收到带有标签的报文后，根据报文中的入标签转发该报文。本命令用来使能MPLS标签转发的统计功能。

FTN转发是指接收到不带标签的报文，为其添加标签后转发该报文。FTN转发的统计功能需要通过RIB IPv4地址族视图下的**mpls-forwarding statistics prefix-list**命令来使能。

只有通过本命令使能MPLS标签转发统计功能，并通过**mpls statistics interval**命令使能统计信息收集功能，用户才能利用**display mpls lsp verbose**命令查看MPLS标签转发的统计信息。

【举例】

\# 使能目的地址为2.2.2.2/32的FEC对应LSP的MPLS标签转发统计功能。

\<Sysname\> system-view

Sysname mpls statistics ipv4 2.2.2.2 32

【相关命令】

·**display mpls lsp verbose**

·**mpls statistics**** interval**

·**reset mpls statistics**

**MPLS基础 \-- MPLS基础配置命令 \-- mpls statistics interval**

------------------------------------------------------------------------

![说明](MPLS基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls statistics interval**]命令用来使能MPLS标签转发统计信息的收集功能，并设置统计信息收集的时间间隔。

**[undo mpls statistics interval**]命令用来关闭MPLS标签转发统计信息的收集功能。

【命令】

**[mpls statistics interval ***interval*]

**[undo mpls statistics interval**]

【缺省情况】

MPLS标签转发统计信息收集功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：MPLS标签转发统计信息收集的时间间隔，取值范围为30～65535，单位为秒。

【使用指导】

只有通过**mpls statistics**命令使能MPLS标签转发统计功能，并通过本命令使能统计信息收集功能，用户才能利用**display mpls lsp verbose**命令查看MPLS标签转发统计信息。

【举例】

\# 使能MPLS标签转发统计信息收集功能，并将统计信息收集时间间隔设置为30秒。

\<Sysname\> system-view

Sysname mpls statistics interval 30

【相关命令】

·**display mpls lsp verbose**

·**mpls statistics**

·**reset mpls statistics**

**MPLS基础 \-- MPLS基础配置命令 \-- mpls ttl expiration enable**

------------------------------------------------------------------------

![说明](MPLS基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mpls ttl expiration enable**]命令用来使能MPLS的TTL超时消息发送功能。

**[undo mpls ttl expiration enable**]命令用来关闭MPLS的TTL超时消息发送功能。

【命令】

**[mpls ttl expiration enable**]

**[undo mpls ttl expiration enable**]

【缺省情况】

MPLS的TTL超时消息发送功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能MPLS的TTL超时消息发送功能后，当LSR收到TTL为1的MPLS报文时，LSR会生成ICMP的TTL超时消息。对于一层标签的MPLS报文，LSR沿着本地IP路由返回ICMP TTL超时消息；对于多层标签的MPLS报文，LSR沿着发送MPLS报文的LSP转发ICMP TTL超时消息，由Egress节点将该消息返回给发送者。

关闭MPLS的TTL超时消息发送功能后，当LSR收到TTL为1的MPLS报文时，LSR不会生成ICMP的TTL超时消息。

【举例】

\# 关闭MPLS的TTL超时消息发送功能。

\<Sysname\> system-view

Sysname undo mpls ttl expiration enable

**MPLS基础 \-- MPLS基础配置命令 \-- mpls ttl propagate**

------------------------------------------------------------------------

**[mpls ttl propagate**]命令用来使能TTL复制功能，即IP报文进入MPLS域时将IP TTL复制到标签的TTL域；报文离开MPLS域时将标签的TTL复制到IP的TTL域。

**[undo mpls ttl propagate**]命令用来禁止TTL复制功能，即IP报文进入MPLS域，为IP报文添加标签时，标签的TTL域取值为255；报文离开MPLS域时，直接弹出标签，不修改IP TTL的值。

【命令】

**[mpls ttl propagate**[ { **public** \| **vpn** }]]

**[undo mpls ttl propagate**[ { **public** \| **vpn** }]]

【缺省情况】

对于通过公网进行转发的报文使能了TTL复制功能，对于通过VPN进行转发的报文禁止TTL复制功能。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[public**]：对通过公网转发的报文进行设置。

**[vpn**]：对通过VPN转发的报文进行设置。

【使用指导】

在Ingress和Egress上都使能TTL复制功能后，Tracert的结果将反映报文实际经过的路径。MPLS骨干网的节点对用户网络的报文可见。

禁止TTL复制功能后，Tracert的结果不包括MPLS骨干网络中的每一跳。MPLS骨干网的节点对用户网络的报文不可见，从而隐藏MPLS骨干网络的结构。

需要注意的是：

·在MPLS域内部，MPLS报文多层标签之间的TTL值总是互相复制。**mpls ttl propagate**命令只决定是否将IP TTL复制到标签的TTL域、是否将标签的TTL复制到IP的TTL域。

·建议在LSP经过的LSR上配置相同的TTL域处理方式。

·如果配置**mpls ttl propagate vpn**命令使能对VPN报文的TTL复制功能，则建议在同一个VPN的所有PE上都使能此功能，以保证不同的PE上执行Tracert得到的跳数结果一致。

【举例】

\# 使能VPN报文的TTL复制功能。

\<Sysname\> system-view

Sysname mpls ttl propagate vpn

**MPLS基础 \-- MPLS基础配置命令 \-- reset mpls statistics**

------------------------------------------------------------------------

![说明](MPLS基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset mpls statistics**]命令用来清除指定LSP的MPLS转发统计信息。

【命令】

**[reset mpls statistics **[{ **all** \| [ **vpn-instance** *vpn-instance-name* ] { **ipv4** *ipv4-destination mask-length* \| **ipv6** *ipv6-destination prefix-length* } \| **static** \| **te** *ingress-lsr-id tunnel-id* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：清除所有LSP的统计信息。

**[vpn-instance** *vpn-instance-name*]：清除指定VPN实例的LSP统计信息。*vpn-instance-name*表示VPN实例名称，为1～31字符的字符串，区分大小写。如果没有指定本参数，则清除公网的LSP统计信息。

**[ipv4 ***ipv4-destination mask-length*]：清除指定FEC对应IPv4 LSP的统计信息。*ipv4-destination*为FEC的IPv4目的地址，*mask-length*为FEC目的地址的掩码长度，取值范围为0～32。

**[ipv6** *ipv6-destination prefix-length*]：清除指定FEC对应BGP-IPv6 LSP的统计信息。*ipv6-destination*为FEC的IPv6目的地址，*prefix-length*为FEC目的地址的前缀长度，取值范围为0～128。

**[static**]：清除静态LSP和静态CR-LSP的统计信息。

**[te** *ingress-lsr-id tunnel-id*]：清除指定RSVP-TE隧道的统计信息。*ingress-lsr-id*为入节点的LSR ID，*tunnel-id*为隧道ID，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 清除目的地址为2.2.2.2/32的FEC对应LSP的MPLS转发统计信息。

\<Sysname\> reset mpls statistics ipv4 2.2.2.2 32

【相关命令】

·**display mpls lsp verbose**

·**mpls statistics**

·**mpls statistics interval**

**MPLS基础 \-- MPLS基础配置命令 \-- snmp-agent trap enable mpls**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable mpls**]命令用来开启MPLS模块的告警功能。

**[undo** **snmp-agent** **trap** **enable mpls**]命令用来关闭MPLS模块的告警功能。

【命令】

**[snmp-agent** **trap** **enable** **mpls**]

**[undo** **snmp-agent** **trap** **enable** **mpls**]

【缺省情况】

MPLS模块的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启MPLS模块的告警功能后，该模块会生成告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启MPLS模块的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable mpls

