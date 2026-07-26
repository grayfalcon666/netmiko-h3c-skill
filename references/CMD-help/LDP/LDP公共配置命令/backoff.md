
**LDP \-- LDP公共配置命令 \-- backoff**

------------------------------------------------------------------------

**[backoff**]命令用来配置LDP倒退机制的初始延迟和最大延迟。

**[undo backoff**]命令用来恢复缺省情况。

【命令】

**[backoff** **initial** *initial-time* **maximum** *maximum-time*]

**[undo backoff**]

【缺省情况】

LDP倒退机制的初始延迟为15秒，最大延迟为120秒。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[initial*** initial-time*]：指定LDP倒退机制的初始延迟。*initial-time*表示LDP倒退机制的初始延迟，取值范围15～50331，单位为秒。

**[maximum** *maximum-time*]：指定LDP倒退机制的最大延迟。*maximum-time*表示LDP倒退机制的最大延迟，取值范围120～50331，单位为秒。

【使用指导】

如果LDP对等体上配置的LDP会话参数不兼容，则可能导致会话参数协商失败、LDP对等体无休止地反复尝试建立会话。

LDP倒退机制用来抑制尝试建立会话的频率。如果会话因为参数不兼容而建立失败，LSR将等待初始延迟时间再尝试建立会话；如果会话再次因为参数不兼容而建立失败，则再次尝试建立会话的延迟时间为上一次延迟时间的二倍；延迟时间达到配置的最大值后，尝试建立会话的等待时间将保持为配置的最大延迟。

需要注意的是，如果配置的LDP倒退机制的初始延迟大于最大延迟，则初始延迟采用所配置的最大延迟的值。

【举例】

\# 配置公网LDP实例LDP倒退机制的初始延迟时间为100秒，最大延迟时间为300秒。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp backoff initial 100 maximum 300

**LDP \-- LDP公共配置命令 \-- display mpls ldp discovery**

------------------------------------------------------------------------

**[display mpls ldp discovery**]命令用来显示LDP发现过程相关信息。

【命令】

集中式设备：

**[display mpls ldp discovery** [ **vpn-instance** *vpn-instance-name*  [ [ **interface** *interface-type interface-number* \| **peer** *peer-lsr-id* ]  **ipv6**  \| [ **targeted-peer** { *ip-address* \| *ipv6-address* } ] ]  **verbose**  ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mpls ldp discovery** [ **vpn-instance** *vpn-instance-name*  [ [ **interface** *interface-type interface-number* \| **peer** *peer-lsr-id* ]  **ipv6**  \| [ **targeted-peer** { *ip-address* \| *ipv6-address* } ] ]  **verbose**   **standby** **slot** *slot-number*] **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display mpls ldp discovery** [ **vpn-instance** *vpn-instance-name*  [ [ **interface** *interface-type interface-number* \| **peer** *peer-lsr-id* ]  **ipv6**  \| [ **targeted-peer** { *ip-address* \| *ipv6-address* } ] ]  **verbose**   **standby chassis** *chassis-number* **slot** *slot-number*] **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定LDP实例的发现过程相关信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网LDP实例的发现过程相关信息。

**[interface** *interface-type interface-number*]：显示通过指定接口发送Link hello消息的LDP发现过程相关信息，即基本发现机制相关信息。*interface-type interface-number*为接口类型和接口编号。

**[peer ***peer-lsr-id*]：显示发现指定对等体的LDP发现过程相关信息，既可以是通过基本发现机制发现对等体的信息，也可以是通过扩展发现机制发现对等体的信息。*peer-lsr-id*为LDP对等体的LSR ID。

**[ipv6**]**：**显示IPv6 Link hello和IPv6 Targeted hello消息发现过程的相关信息。如果不指定本参数，则显示IPv4 Link hello和IPv4 Targeted hello消息发现过程的相关信息。

**[targeted-peer**[ { *ip-address* \| *ipv6-address* }]]：显示向指定对等体发送Targeted hello消息的LDP发现过程相关信息，即扩展发现机制相关信息。*ip-address*为LDP对等体的IPv4地址，*ipv6-address*为LDP对等体的IPv6地址。

**[verbose**]**：**显示LDP发现过程的详细信息。如果不指定本参数，则显示LDP发现过程的简要信息。

**[standby**]**：**显示指定LDP备进程的信息。如果不指定本参数，则显示LDP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的主控板。*slot-number*为主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和主控板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的LDP发现过程相关信息。*cpu-number*表示单板上CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果没有指定**interface**、**peer**、**targeted-peer**和**ipv6**中的任何一个参数，则显示所有LDP IPv4发现过程相关信息，包括基本发现机制相关信息和扩展发现机制相关信息。

【举例】

\# 显示所有公网LDP IPv4 hello消息发现过程的简要信息。

\<Sysname\> display mpls ldp discovery

     Type: L - Link Hello, T - Targeted Hello

Discovery Source              Hello Sent/Rcvd       Peer LDP ID

(L) GE1/0/2                   83/80                 100.100.100.18:0

                                                    200.100.100.18:0

(T) 100.100.100.18            23/20                 100.100.100.18:0

表1-1 display mpls ldp discovery命令显示信息描述表

字段

描述

Type

LDP发现过程类型，取值包括：

·L：表示通过发送Link hello消息发现对等体的基本发现机制

·T：表示通过发送Targeted hello消息发现对等体的扩展发现机制

Discovery Source

LDP对等体的发现源：

·LDP发现过程类型为L时，显示为发现该对等体的接口

·LDP发现过程类型为T时，显示为对等体的IPv4地址

Hello Sent/Rcvd

接口上发送和接收的Hello报文数目

Peer LDP ID

LDP对等体的LDP ID

\# 显示所有公网LDP IPv6 hello消息发现过程的简要信息。

\<Sysname\> display mpls ldp discovery ipv6

Interface: GigabitEthernet1/0/2

  Hello Sent/Rcvd: 12/12

    Peer LDP ID: 100.100.100.18:0

    Peer LDP ID: 200.200.200.28:0

Targeted Hellos: 2001:0000:130F::09C0:876A:130B -\>

                 2005:130F::09C0:876A:130B

  Hello Sent/Rcvd: 93/80

    Peer LDP ID: 100.100.100.180:0

表1-2 display mpls ldp discovery命令显示信息描述表

字段

描述

Interface

采用基本发现机制发现的对等体的接口

Hello Sent/Rcvd

向该对等体发送和从该对等体接收的Hello报文数目

Peer LDP ID

LDP对等体的LDP ID

Targeted Hellos

采用扩展发现机制发现的对等体。其中，"-\>"前面的地址为本地地址；"-\>"后面的地址为对等体地址

\# 显示所有公网LDP IPv4 hello消息发现过程的详细信息。

\<Sysname\> display mpls ldp discovery verbose

Link Hellos:

  Interface GigabitEthernet1/0/2

    Hello Interval   : 5000 ms            Hello Sent/Rcvd  : 83/160

    Transport Address: 100.100.100.17

    Peer LDP ID      : 100.100.100.18:0

      Source Address : 202.118.224.18     Transport Address: 100.100.100.18

      Hello Hold Time: 15 sec (Local: 15 sec, Peer: 15 sec)

    Peer LDP ID      : 100.100.100.20:0

      Source Address : 202.118.224.20     Transport Address: 100.100.100.20

      Hello Hold Time: 15 sec (Local: 15 sec, Peer: 15 sec)

Targeted Hellos:

  100.100.100.17 -\> 100.100.100.18 (Active, Passive)

    Hello Interval   : 15000 ms           Hello Sent/Rcvd  : 23/20

    Transport Address: 100.100.100.17

    Peer LDP ID      : 100.100.100.18:0

      Source Address : 100.100.100.18     Transport Address: 100.100.100.18

      Hello Hold Time: 45 sec (Local: 45 sec, Peer: 45 sec)

  100.100.100.17 -\> 100.100.100.20 (Active, Passive)

    Hello Interval   : 15000 ms           Hello Sent/Rcvd  : 23/22

    Transport Address: 100.100.100.17

    Peer LDP ID      : 100.100.100.20:0

      Source Address : 100.100.100.20     Transport Address: 100.100.100.20

      Hello Hold Time: 45 sec (Local: 45 sec, Peer: 45 sec)

\# 显示所有公网LDP IPv6 hello消息发现过程的详细信息。

\<Sysname\> display mpls ldp discovery ipv6 verbose

Link Hellos:

  Interface GigabitEthernet1/0/2

    Hello Interval   : 5000 ms            Hello Sent/Rcvd  : 83/160

    Transport Address: 2001::2

    Peer LDP ID      : 100.100.100.18:0

      Source Address : FE80:130F:20C0:29FF:FEED:9E60:876A:130B

      Transport Address: 2001::1

      Hello Hold Time: 15 sec (Local: 15 sec, Peer: 15 sec)

Targeted Hellos:

  2001:0000:130F::09C0:876A:130B -\>

        2005:130F::09C0:876A:130B(Active, Passive)

    Hello Interval   : 15000 ms           Hello Sent/Rcvd  : 23/22

    Transport Address: 2001:0000:130F::09C0:876A:130B

    Peer LDP ID      : 100.100.100.18:0

      Source Address : 2005:130F::09C0:876A:130B

      Destination Address : 2001:0000:130F::09C0:876A:130B

      Transport Address   : 2005:130F::09C0:876A:130B

      Hello Hold Time: 45 sec (Local: 45 sec, Peer: 45 sec)

表1-3 display mpls ldp discovery verbose命令显示信息描述表

字段

描述

Link Hellos

发送Link hello消息的LDP发现过程相关信息，即基本发现机制相关信息，按接口显示

多播类型接口下，可能发现多个对等体

Interface

运行LDP基本发现机制的接口

Hello Interval

hello报文发送时间间隔，单位为毫秒

Hello Sent/Rcvd

接口上发送和接收的hello报文数

Transport Address

本地传输地址

Peer LDP ID

LDP对等体的LDP ID

Source Address

收到hello报文的源IP地址

Destination Address

收到hello报文的目的IP地址

Transport Address

收到的hello报文中指定的传输地址，即LDP对等体的传输地址

Hello Hold Time

协商出来的Hello保持时间，单位为秒

Local：本地配置的Hello保持时间，单位为秒；Peer：收到的hello报文中指定的Hello保持时间，即LDP对等体的Hello保持时间，单位为秒

协商出来的Hello保持时间为Local和Peer值中的较小者

Targeted Hellos

发送Targeted hello消息的LDP发现过程相关信息，即扩展发现机制相关信息，按对等体LSR ID显示

100.100.100.17 -\> 100.100.100.18 (Active, Passive)

·100.100.100.17（"-\>"前面的地址）为本地的地址

·100.100.100.18（"-\>"后面的地址）为对等体的地址

·(Active)：本地LSR为主动方，即主动向对等体发送Targeted hello消息

·(Passive)：本地LSR为被动方，被动应答对等体发送的Targeted hello消息

·(Active, Passive)：本地LSR既作为主动方，又作为被动方

**LDP \-- LDP公共配置命令 \-- display mpls ldp fec**

------------------------------------------------------------------------

**[display mpls ldp fec**]命令用来显示通过LDP学习到的FEC---标签映射信息。

【命令】

集中式设备：

**[display mpls ldp fec **[ **vpn-instance** *vpn-instance-name*  [ *ip-address mask-length* \| *ipv6-address prefix-length* \| [ i**pv6** ]  **summary**  ] ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mpls ldp fec **[ **vpn-instance** *vpn-instance-name*  [ *ip-address mask-length* \| *ipv6-address prefix-length* \| [ i**pv6** ]  **summary**  ]  **standby slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mpls ldp fec **[ **vpn-instance** *vpn-instance-name*  [ *ip-address mask-length* \| *ipv6-address prefix-length* \| [ i**pv6** ]  **summary**  ]  **standby chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定LDP实例的FEC---标签映射信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网LDP实例的FEC---标签映射信息。

*[ip-address mask-length*]：显示指定IPv4 FEC的标签映射详细信息。*ip-address*为FEC的目的IPv4地址前缀，*mask-length*为FEC目的IPv4地址前缀的掩码长度，取值范围为0～32。

*[ipv6-address* *prefix-length*]：显示指定IPv6 FEC的标签映射详细信息。*ipv6-address*为FEC的目的IPv6地址前缀，*prefix-length*为FEC目的IPv6地址前缀的掩码长度，取值范围为0～128。

**[ipv6**]**：**显示IPv6的FEC标签映射相关信息。如果仅指定**ipv6**参数，则显示所有IPv6 FEC---标签映射的详细信息。

**[summary**]：显示LDP学习到的所有FEC---标签映射的概要信息，如果仅指定**summary**参数，则显示显示IPv4 FEC---标签映射的概要信息。

**[standby**]**：**显示指定LDP备进程的信息。如果不指定本参数，则显示LDP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的主控板。*slot-number*为主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和主控板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的FEC信息。*cpu-number*表示单板上CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果同时指定**summary**参数和**ipv6**参数，则显示所有IPv6 FEC---标签映射的概要信息

·如果不指定ip-address mask-length**、**ipv6-address mask-length、**ipv6**和**summary**参数，则显示IPv4 FEC---标签映射详细信息

【举例】

\# 显示公网LDP学习到的所有IPv4 FEC---标签映射详细信息。

\<Sysname\> display mpls ldp fec

 FEC: 100.100.100.18/32

   Flags: 0x02

   In Label: 1531

   Label Advertisement Policy:

     FEC Prefix-list: Fec-prefix-list

     Peer Prefix-list: Peer-prefix-list

   Upstream Info:

     Peer: 100.100.100.18:0        State: Established (stale)

   Downstream Info:

     Peer: 100.100.100.18:0

       Out Label: 3                State: Established (stale)

       Next Hops: 202.118.224.18          GE1/0/2

                  100.19.100.18           GE1/0/6

 FEC: 200.100.100.18/32 (No route)

   Flags: 0x0

   In Label: 1532

   Upstream Info:

     Peer: 200.200.200.28:0        State: Established

   Downstream Info:

     Peer: 120.100.100.18:0

       Out Label: 3                State: Idle

\# 显示公网LDP学习到的IPv6 FEC---标签映射详细信息。

\<Sysname\> display mpls ldp fec ipv6

 FEC: 2005:130F::09C0/128

   Flags: 0x02

   In Label: 1026

   Label Advertisement Policy:

     FEC Prefix-list: Fec-ipv6-prefix-list

     Peer Prefix-list: Peer-ipv6-prefix-list

   Upstream Info:

     Peer: 100.100.100.18:0        State: Established (stale)

   Downstream Info:

     Peer: 100.100.100.18:0

       Out Label: 3                State: Established (stale)

       Next Hops:

       FE80:130F:20C0:29FF:FEED:9E60:876A:130B          GE1/0/2

表1-4 display mpls ldp fec命令显示信息描述表

字段

描述

FEC

转发等价类，即IP地址前缀和前缀长度

Flags

FEC标志位，包含如下标志位：

·0x01：表示Egress LSP

·0x02：表示Ingress LSP

·0x04：表示等待向RIB添加出标签

·0x08：表示等待向LSM添加LSP

·0x10：表示GR恢复期间，非Egress LSP等待恢复

·0x20：表示满足发送标签通告的条件

FEC标志位的实际显示值可能为多种取值的组合，如显示为0x21表示0x01和0x20的组合

In Label

入标签值，即本地LSR为此FEC分配的标签

Label Advertisement Policy

标签通告控制策略信息

FEC Prefix-list

用于检查FEC目的地址的IP地址前缀列表

Peer Prefix-list

用于检查LDP对等体LSR ID的IP地址前缀列表

Upstream Info

上游信息，即向哪些对等体通告FEC---标签映射信息及与上游对等体建立的LSP的当前状态

Peer

上游对等体的LDP ID

State

与上游对等体建立的LSP的当前状态，取值包括：

·Established：激活状态

·Idle：初始状态

·Release Awaited：等待Release消息状态

·Resource Awaited：等待标签资源分配状态

如果状态后带有stale标记，则表示对应的FEC---标签映射处于GR期间

Downstream Info

下游信息，即从哪些对等体接收到FEC---标签映射信息及与下游对等体建立的LSP的当前状态

Peer

下游对等体的LDP ID

Out Label

出标签值，即下游对等体为此FEC分配的标签

State

与下游对等体建立的LSP的当前状态，取值包括：

·Established：激活状态

·Idle：未激活状态

如果状态后带有stale标记，则表示对应的FEC---标签映射处于GR期间

Next Hops

出接口和下一跳信息

\# 显示公网LDP学习到的所有IPv4 FEC---标签映射的概要信息。

\<Sysname\> display mpls ldp fec summary

FECs         : 3

Implicit Null: 1

Explicit Null: 0

Non-Null     : 2

No Label     : 0

No Route     : 0

Sent         : 3

Received     : 3

\# 显示公网LDP学习到的IPv6 FEC---标签映射的概要信息。

\<Sysname\> display mpls ldp fec ipv6 summary

FECs         : 4

Implicit Null: 0

Explicit Null: 0

Non-Null     : 4

No Label     : 0

No Route     : 0

Sent         : 3

Received     : 3

表1-5 display mpls ldp fec summary命令显示汇总信息描述表

字段

描述

FECs

LDP发现的转发等价类个数，FEC来自路由协议或者LDP对等体通告的标签映射

Implicit Null

绑定隐式空标签的FEC个数

Explicit Null

绑定显式空标签的FEC个数

Non-Null

绑定非空标签的FEC个数

No Label

未分配到标签的FEC个数

No Route

LDP没有对应路由的FEC个数，包含几种情况：

·路由表中没有对应路由信息

·路由表中有对应路由信息，但是没有将路由引入到LDP

·对于IPv6路由，如果路由表中有对应路由信息，并已引入LDP，但是当前设备上没有配置**mpls ldp ipv6 enable**或者没有配置**targeted-peer ***ipv6-address*，FEC也会视为没有对应路由

Sent

已经发送和正在发送的标签映射个数

Received

已经收到并接受的标签映射个数

**LDP \-- LDP公共配置命令 \-- display mpls ldp interface**

------------------------------------------------------------------------

**[display mpls ldp interface**]命令用来显示使能了LDP能力的接口的LDP相关信息。

【命令】

**[display mpls ldp interface** [ **vpn-instance** *vpn-instance-name*   *interface-type interface-number*   **ipv6**  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定LDP实例的接口的LDP相关信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网LDP实例下所有使能接口LDP能力的接口的LDP相关信息。

*[interface-type interface-number*]：显示指定接口的LDP相关信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则显示所有使能LDP能力的接口的LDP相关信息。

**[ipv6**]**：**显示使能了LDP支持IPv6能力的接口的相关信息。如果不指定本参数，则显示使能LDP支持IPv4的能力的接口的相关信息。

【举例】

\# 显示公网LDP实例下所有使能了LDP支持IPv4能力的接口的LDP相关信息。

\<Sysname\> display mpls ldp interface

Interface                 MPLS         LDP             Auto-config

GE1/0/2                    Enabled      Configured      -

GE1/0/6                    Enabled      Configured      -

\# 显示公网LDP实例下所有使能了LDP支持IPv6能力的接口的LDP相关信息。

\<Sysname\> display mpls ldp interface ipv6

Interface                 MPLS         LDP             Auto-config

GE1/0/2                   Enabled      Not Configured  -

GE1/0/3                   Enabled      Not Configured  -

表1-6 display mpls ldp interface命令显示信息描述表

字段

描述

Interface

使能了LDP能力的接口名称

MPLS

接口上MPLS是否使能，取值包括：

·Enabled：使能了{.TableTextChar}MPLS

·Disabled：未使能MPLS

LDP

接口上是否配置了**mpls ldp enable**命令或**mpls ldp ipv6 enable**命令，取值包括：

·Configured：配置了该命令

·Not Configured：未配置该命令

Auto-config

通过IGP自动使能接口上LDP能力的相关信息：

· 如果{.TableTextChar}通过IGP自动使能了接口的LDP能力，则显示对应的IGP实例参数，如OSPF的实例号和区域标识

· 如果没有通过{.TableTextChar}IGP自动使能接口的LDP能力，则显示为"-"

【相关命令】

·**mpls ldp**

·**mpls ldp enable**

·**mpls ldp ipv6 enable**

**LDP \-- LDP公共配置命令 \-- display mpls ldp lsp**

------------------------------------------------------------------------

**[display mpls ldp lsp**]命令用来显示LDP协议生成的LSP信息，即LDP LSP信息。

【命令】

**[display mpls ldp lsp** [ **vpn-instance** *vpn-instance-name*  [*ip-address mask-length* \| *ipv6-address prefix-length \|* **ipv6** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的LDP LSP信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网LDP实例的LDP LSP信息。

*[ip-address* *mask-length*]：显示到达指定IPv4 FEC的LDP LSP信息。*ip-address*为FEC的目的IPv4地址前缀；*mask-length*为FEC目的IPv4地址前缀的掩码长度，取值范围为0～32。

*[ipv6-address prefix-length*]：显示到达指定IPv6 FEC的LDP LSP信息。*ipv6-address*为FEC的目的IPv6地址前缀；*prefix-length*为FEC目的IPv6地址前缀的掩码长度，取值范围为0～128。

**[ipv6**]：显示IPv6 FEC的LDP LSP信息。

【使用指导】

如果不指定参数*ip-address mask-length***、***ipv6-address prefix-length*和**ipv6**，则显示所有IPv4 FEC的LDP LSP信息**。**

【举例】

\# 显示公网LDP实例的IPv4 FEC的LDP LSP信息。

\<Sysname\> display mpls ldp lsp

Status Flags: \* - stale, L - liberal, B - backup

FECs: 4            Ingress: 1          Transit: 1      Egress: 3

FEC                In/Out Label        Nexthop         OutInterface

1.1.1.1/32         -/3                 10.1.1.1        GE1/0/2

                   1151/3              10.1.1.1        GE1/0/2

                   -/1025(B)           30.1.1.1        GE1/0/3

                   1151/1025(B)        30.1.1.1        GE1/0/3

2.2.2.2/32         3/-

                   -/1151(L)

10.1.1.0/24        1149/-

                   -/1149(L)

192.168.1.0/24     1150/-

                   -/1150(L)

\# 显示公网LDP实例的IPv6 FEC的LDP LSP信息。

\<Sysname\> display mpls ldp lsp ipv6

Status Flags: \* - stale, L - liberal, B - backup

FECs: 2            Ingress: 1          Transit: 1      Egress: 1

FEC: 2080::29FF:FEED:9E60:876A:130B/128      

In/Out Label: -/3                                OutInterface : GE1/0/2

Nexthop     : FE80:12F:C0::130B    

In/Out Label: 1151/3                             OutInterface : GE1/0/2    

Nexthop     : FE80:12F:C0::130B    

In/Out Label: -/1026(L)                          OutInterface : -

Nexthop     : -                                          

FEC: 2001::1/128      

In/Out Label: 3/-                               OutInterface : -

Nexthop     : -

表1-7 display mpls ldp lsp命令显示信息描述表

字段

描述

Status Flags

LSP状态，取值包括：

·\*：即stale，表示LSP处于GR过程中

·L：即liberal，表示LSP不可用

·B：即backup，表示备份LSP

FECs

FEC的总数

Ingress

本地设备作为入节点的LSP数

Transit

本地设备作为中间节点的LSP数

Egress

本地设备作为出节点的LSP数

FEC

转发等价类，即IP地址前缀和前缀长度

In/Out Label

入标签值/出标签值

Nexthop

下一跳地址

OutInterface

出接口

【相关命令】

·**display mpls lsp**（MPLS命令参考/MPLS基础）

**LDP \-- LDP公共配置命令 \-- display mpls ldp parameter**

------------------------------------------------------------------------

**[display mpls ldp parameter**]命令用来显示LDP的运行参数。

【命令】

**[display mpls ldp parameter ** **vpn-instance** *vpn-instance-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定LDP实例的运行参数。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网LDP实例的运行参数。

【使用指导】

本命令的显示信息内容包括适用于所有LDP实例的全局运行参数和适用于特定LDP实例的运行参数。

【举例】

\# 显示公网LDP实例的运行参数。

\<Sysname\> display mpls ldp parameter

 Global Parameters:

   Protocol Version    : V1         IGP Sync Delay on Restart : 90 sec

   Nonstop Routing     : Off        Graceful Restart          : Off

   Reconnect Time      : 120 sec    Forwarding State Hold Time: 360 sec

   DSCP Value          : 48

 Instance Parameters:

   Instance ID         : 0

   LSR ID              : 0.0.0.0

   Loop Detection      : Off

   Hop Count Limit     : 32         Path Vector Limit              : 32

   Label Retention Mode: Liberal    Label Distribution Control Mode: Ordered

   IGP Sync Delay      : 0 sec

表1-8 display mpls ldp parameter命令显示信息描述表

字段

描述

Global Parameters

适用于所有LDP实例的全局运行参数

Protocol Version

LDP的协议版本

IGP Sync Delay on Restart

LDP重启时IGP同步延迟时间，单位为秒

Nonstop Routing

是否使能不间断路由功能，取值包括：

·On：使能了不间断路由功能

·Off：未使能不间断路由功能

Graceful Restart

是否使能Graceful Restart功能，取值包括：

·On：使能了GR功能

·Off：未使能GR功能

Reconnect Time

GR重连定时器间的值，单位为秒

Forwarding State Hold Time

GR转发状态保持定时器的值，单位为秒

DSCP Value

发送的LDP报文的DSCP优先级

Instance Parameters

适用于特定LDP实例的运行参数

Instance ID

VPN实例索引，取值为0时表示公网

LSR ID

本地设备的LSR ID

Loop Detection

是否使能环路检测功能，取值包括：

·On：使能了环路检测功能

·Off：未使能环路检测功能

Hop Count Limit

环路检测的最大跳数

Path Vector Limit

路径向量方式下LSP的最大跳数

Label Retention Mode

使用的标签保持方式，目前取值只能是Liberal，表示自由标签保持方式

Label Distribution Control Mode

使用的标签分发控制方式，取值包括：

·Ordered：有序方式

·Independent：独立方式

IGP Sync Delay

IGP同步延迟时间，单位为秒

**LDP \-- LDP公共配置命令 \-- display mpls ldp peer**

------------------------------------------------------------------------

**[display mpls ldp peer**]命令用来显示LDP对等体和LDP会话信息。

【命令】

集中式设备：

**[display mpls ldp peer** [ **vpn-instance** *vpn-instance-name*   *peer-lsr-id*   **verbose**  ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mpls ldp peer** [ **vpn-instance** *vpn-instance-name*   *peer-lsr-id*   **verbose**   **standby slot** *slot-number*] **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display mpls ldp peer** [ **vpn-instance** *vpn-instance-name*   *peer-lsr-id*   **verbose**   **standby chassis** *chassis-number* **slot** *slot-number*] **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定LDP实例的LDP对等体和LDP会话信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网LDP实例的LDP对等体和会话信息。

**[peer ***peer-lsr-id*]：显示与指定LDP对等体之间LDP会话的信息。*peer-lsr-id*为LDP对等体的LSR ID。如果不指定本参数，则显示所有LDP对等体和LDP会话的信息。

**[verbose**]**：**显示LDP对等体和LDP会话的详细信息。如果不指定本参数，则显示LDP对等体和LDP会话的简要信息。

**[standby**]**：**显示指定LDP备进程的信息。如果不指定本参数，则显示LDP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的主控板。*slot-number*为主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和主控板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的peer信息。*cpu-number*表示单板上CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

本命令的显示信息内容包括LDP对等体参数和LDP会话状态等。

【举例】

\# 显示公网LDP实例中所有LDP对等体和LDP会话的简要信息。

\<Sysname\> display mpls ldp peer

Total number of peers: 1

Peer LDP ID             State         Role     GR   MD5  KA Sent/Rcvd

2.2.2.9:0               Operational   Passive  Off  Off  39/39

表1-9 display mpls ldp peer命令显示信息描述表

字段

描述

Total number of peers

LDP对等体的总数

Peer LDP ID

对等体的LDP ID

State

本地LSR与LDP对等体之间的LDP会话的状态，取值包括：

·Non Existent：尚未建立TCP连接

·Initialized：TCP连接已经建立

·OpenRecv：本地LSR接收到可接受的初始化消息

·OpenSent：本地LSR已经发送初始化消息

·Operational：成功建立会话

Role

本地LSR在会话中的角色，取值包括Active（主动方）和Passive（被动方），IP地址大的LSR为主动方，IP地址小的LSR为被动方，由主动方发起建立TCP连接

GR

对等体上是否使能了GR功能，取值包括

·On：使能了GR功能

·Off：未使能GR功能

MD5

本地是否使能了与该对等体之间LDP会话的MD5认证功能，取值包括：

·On：使能了MD5认证功能

·Off：未使能MD5认证功能

KA Sent/Rcvd

本地LSR发送和接收的Keepalive消息数

\# 显示公网LDP实例中所有LDP对等体和LDP会话的详细信息。

\<Sysname\> display mpls ldp peer verbose

 Peer LDP ID      : 100.100.100.20:0

 Local LDP ID     : 100.100.100.17:0

 TCP Connection   : 100.100.100.20:47515 -\> 100.100.100.17:646

 Session State    : Operational        Session Role     : Passive

 Session Up Time  : 0000:00:03 (DD:HH:MM)

 Max PDU Length   : 4096 bytes (Local: 4096 bytes, Peer: 4096 bytes)

 Keepalive Time     : 45 sec (Local: 45 sec, Peer: 45 sec)

 Keepalive Interval : 15 sec

 Msgs Sent/Rcvd   : 288/426

 KA Sent/Rcvd     : 13/13

Label Adv Mode   : DU                 Graceful Restart : On

Reconnect Time   : 120 sec            Recovery Time    : 360 sec

 Loop Detection   : On                 Path Vector Limit: 32

 Discovery Sources:

   Targeted Hello 100.100.100.17 -\> 100.100.100.20 (Active, Passive)

     Hello Hold Time: 45 sec           Hello Interval   : 15000 ms

   Targeted Hello 2005:130F::09C0:876A:130B -\>

                  2001:0000:130F:0000:0000:09C0:876A:130B (Active, Passive)

     Hello Hold Time: 45 sec           Hello Interval   : 15000 ms

   GigabitEthernet1/0/2

     Hello Hold Time: 15 sec           Hello Interval   : 5000 ms

   GigabitEthernet1/0/2 (v6)

     Hello Hold Time: 15 sec           Hello Interval   : 5000 ms

 Label Acceptance Policy :

   prefix-from-20

   prefix-from-30(v6)

 Session Protection      : On

   State            : Ready            Duration         : 120 sec

 Addresses received from peer:

   202.118.224.20   100.100.100.20   11.22.33.44      1.2.3.10

   1.2.3.4

   2005:130F::09C0:876A:130B

表1-10 display mpls ldp peer verbose命令显示信息描述表

字段

描述

Peer LDP ID

对等体的LDP标识符

Local LDP ID

本地的LDP标识符

TCP connection

该会话的TCP连接信息，即TCP连接两端的IP地址和端口号、是否使能了TCP连接的MD5验证（如果使能了MD5验证，则显示MD5 On；如果未使能MD5验证，则不显示任何信息）

Session State

本地LSR与对等体之间的LDP会话的状态，取值包括：

·Non Existent：尚未建立TCP连接

·Initialized：TCP连接已经建立

·OpenRecv：本地LSR接收到可接受的初始化消息

·OpenSent：本地LSR已经发送初始化消息

·Operational：成功建立会话

Session Role

本地LSR在会话中的角色，取值包括：

·Active：主动方

·Passive：被动方

Session Up time

会话处于Operational状态的持续时间

Max PDU Length

协商出来的最大PDU长度值，单位为字节

Local：本地LSR允许的最大PDU长度值，单位为字节

Peer：对等体发送的报文中携带的最大PDU长度值，单位为字节

Keepalive Time

协商出来的Keepalive时间值，单位为秒

Local：本地配置的Keepalive保持时间值，单位为秒

Peer：对等体发送的报文中携带的Keepalive时间值，单位为秒

Keepalive Interval

当前在用的Keepalive报文发送时间间隔，单位为秒

Msgs Sent/Rcvd

本地发送和接收的各种LDP消息的总数

KA Sent/Rcvd

本地发送和接收的Keepalive消息的总数

Label Adv Mode

协商后的标签通告方式，目前取值只能为DU，表示下游自主通告方式

Graceful Restart

对等体上是否使能了Graceful Restart功能，取值包括：

·On：使能了GR功能

·Off：未使能GR功能

Reconnect Time

协商出来的GR重连时间，单位为秒

Recovery Time

对等体发送的报文中携带的GR恢复时间，单位为秒

Loop Detection

对等体是否使能了环路检测功能，取值包括

·On：使能了环路检测功能

·Off：未使能环路检测功能

Path Vector Limit

对等体发送的报文中携带的路径向量最大长度值

Discovery Sources

对等体的发现源

Targeted Hello

通过扩展发现机制发现的LDP对等体

·100.100.100.17（"-\>"前面的地址）为本地的地址

·100.100.100.20（"-\>"后面的地址）为对等体的地址

·(Active)：本地LSR为主动方，即主动向对等体发送Targeted hello消息

·(Passive)：本地LSR为被动方，被动应答对等体发送的Targeted hello消息

·(Active, Passive)：本地LSR既作为主动方，又作为被动方

GigabitEthernet1/0/2

运行LDP基本发现机制的接口，通过从该接口发送Link hello消息发现了LDP对等体

(v6)：表示通过IPv6 Link hello消息发现对等体

Hello Hold Time

协商出来的Hello保持时间，单位为秒

Hello Interval

当前在用的Hello报文发送时间间隔，单位为毫秒

Label Acceptance Policy

对从对等体接收的标签映射进行过滤时使用的标签接受控制策略

(v6)：表示通过IPv6地址前缀列表进行过滤的标签接受控制策略

Session Protection

是否使能了会话保护功能，取值包括：

·On：使能了会话保护功能

·Off：未使能会话保护功能

State

会话保护状态，取值包括：

·Incomplete：会话保护未准备好

·Ready：会话保护准备就绪

·Protecting：会话处于保护中

Duration

本地配置的会话保护持续时间，单位为秒

取值为Infinite时，表示永久保护

Holdup time remaining

会话保持剩余时间，单位为秒

取值为Infinite时，表示永久保护

会话保护处于Protecting状态时，才会显示此字段

Addresses received from peer

对等体发送的地址列表

**LDP \-- LDP公共配置命令 \-- display mpls ldp summary**

------------------------------------------------------------------------

**[display mpls ldp summary**]命令用来显示LDP运行数据汇总信息。

【命令】

集中式设备：

**[display mpls ldp summary** \**[all**[ \| ]**vpn-instance** *vpn-instance-name*  ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mpls ldp summary** \**[all**[ \| ]**vpn-instance** *vpn-instance-name*   **standby slot** *slot-number*] **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display mpls ldp summary** \**[all**[ \| ]**vpn-instance** *vpn-instance-name*   **standby chassis** *chassis-number* **slot** *slot-number*] **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示公网和所有VPN实例的LDP汇总信息。

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的LDP汇总信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

**[standby**]**：**显示指定LDP备进程的信息。如果不指定本参数，则显示LDP主进程的信息。

**[slot**]* slot-number*：指定备进程所在的主控板。*slot-number*为主控板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：指定备进程所在的成员设备。*slot-number*为设备在IRF中的成员编号。（集中式IRF设备）

**[chassis **]*chassis-number* **slot** *slot-number*：指定备进程所在的成员设备和主控板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的汇总信息。*cpu-number*表示单板上CPU的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

执行本命令时，如果没有指定任何参数，则显示公网LDP汇总信息。

【举例】

\# 显示公网LDP运行数据的汇总信息。

\<Sysname\> display mpls ldp summary

VPN Instance Name    : Public

  Instance ID        : 0

  Instance State     : Active

  Interfaces         : 1 (1 active)

  Targeted Peers     : 0

  Targeted Peers(v6) : 0

  Adjacencies        : 1

  Adjacencies(v6)    : 1

  Peers              : 1

    Operational : 1 (0 GR)

    OpenSent    : 0

    OpenRecv    : 0

    Initialized : 0

    Non-Existent: 0

表1-11 display mpls ldp summary命令显示信息描述表

字段

描述

VPN Instance Name

VPN实例名称

Instance ID

VPN实例标识，取值为0表示公网

Instance State

LDP实例的状态，取值包括：

·Active：LDP实例已激活

·Inactive：LDP实例未激活

Interfaces

使能了LDP能力的接口数

active：表示已经正常运行LDP协议的接口数

Targeted Peers

通过扩展发现机制发现的LDP IPv4对等体数目，包括手工指定和自动生成的对等体

Targeted Peers(v6)

通过扩展发现机制发现的LDP IPv6对等体数目，包括手工指定和自动生成的对等体

Adjacencies

IPv4 Hello邻接体的数目

Adjacencies(v6)

IPv6 Hello邻接体的数目

Peers

对等体总数

Operational

处于Operational状态下的对等体数

GR：表示使能了GR功能的对等体数

OpenSent

处于OpenSent状态下的对等体数

OpenRecv

处于OpenRecv状态下的对等体数

Initialized

处于Initialized状态下的对等体数

Non-Existent

处于Non-Existent状态下的对等体数

**LDP \-- LDP公共配置命令 \-- dscp**

------------------------------------------------------------------------

**[dscp**]命令用来配置发送的LDP报文的DSCP优先级。

**[undo dscp**]命令用来恢复缺省情况。

【命令】

**[dscp ***dscp-value*]

**[undo dscp**]

【缺省情况】

发送的LDP报文的DSCP优先级为48。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：发送的LDP报文的DSCP优先级，取值范围为0～63。

【使用指导】

DSCP（Differentiated Services Code point，差分服务编码点）携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定发送的LDP报文中携带的DSCP优先级的取值。

【举例】

\# 配置发送的LDP报文的DSCP优先级为56。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp dscp 56

【相关命令】

·**display mpls ldp parameter**

**LDP \-- LDP公共配置命令 \-- graceful-restart**

------------------------------------------------------------------------

**[graceful-restart**]命令用来使能LDP协议的GR功能。

**[undo graceful-restart**]命令用来关闭LDP协议的GR功能。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

LDP协议的GR功能处于关闭状态。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

LDP GR（Graceful Restart，平滑重启）在LDP协议重启时，保持标签转发表项，LSR依然根据该表项转发报文，从而保证数据转发不中断。

通过**graceful-restart**命令使能GR功能后，不会对已建立的LDP会话生效。如果要求对已建立的会话生效，则需要执行**reset mpls ldp**命令重新建立LDP会话。

【举例】

\# 使能LDP协议的GR能力。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp graceful-restart

【相关命令】

·**display mpls ldp parameter**

·**reset mpls ldp**

**LDP \-- LDP公共配置命令 \-- graceful-restart timer**

------------------------------------------------------------------------

**[graceful-restart timer**]命令用来配置GR转发状态保持定时器的值和GR重连超时时间。

**[undo graceful-restart timer**]命令用来恢复缺省情况。

【命令】

**[graceful-restart timer **[{ **forwarding-hold** *hold-time* \| **reconnect** *reconnect-time* }]]

**[undo graceful-restart timer **[{ **forwarding-hold** \| **reconnect** }]]

【缺省情况】

GR转发状态保持定时器的值为180秒，GR重连超时时间为120秒。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[forwarding-hold ***hold-time*]：指定GR转发状态保持定时器的值，即本地LSR控制平面重启后，本地LSR转发状态的保持时间。*hold-time*取值范围为60～600，单位为秒。

**[reconnect*** timeout*]：指定GR重连超时时间。GR重连超时时间由本地LSR发送给对等体，该值表示本地LSR期望对等体在检测到LDP会话失效后等待重建LDP会话的时间。*timeout*取值范围为60～300，单位为秒。

【使用指导】

LSR在控制平面重启后，启动GR转发状态保持定时器，并将标签转发信息标记为stale状态。LSR与对等体重新建立LDP会话，并交互标签映射，更新标签转发信息。如果从对等体接收到与标签转发信息匹配的标签映射，则删除该信息的stale标记。GR转发状态保持定时器超时后，LSR删除仍标记为stale的标签转发信息。

当控制平面重启的LSR向对等体发送Initialization消息进行会话协商时，LSR将转发状态保持定时器的剩余时间作为Recovery Time发送给它的对等体。

如果具有GR能力的对端LSR发生控制平面重启，则本端LSR启动GR helper过程，继续保持从重启的LSR接收的FEC---标签映射，并将这些FEC---标签映射标记为stale。如果在重连超时时间内，本端LSR和重启的对端LSR建立LDP会话失败，则本端LSR将删除标记为stale的FEC---标签映射。如果LDP会话建立成功，则本端LSR启动恢复定时器，并与对端LSR交互标签映射，更新本地保存的FEC---标签映射。恢复定时器的值为对端LSR发送的Initialization消息中携带的Recovery Time。恢复定时器超时后，本端LSR删除仍标记为stale的标签转发信息。

需要注意的是，配置的GR转发状态保持定时器的值必须大于GR重连超时时间。

【举例】

\# 配置转发状态保持定时器的值为200秒，GR重连超时时间为100秒。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp graceful-restart timer forwarding-hold 200

Sysname-ldp graceful-restart timer reconnect 100

【相关命令】

·**display mpls ldp parameter**

·**graceful-restart**

**LDP \-- LDP公共配置命令 \-- label-distribution**

------------------------------------------------------------------------

**[label-distribution**]命令用来配置标签分发控制方式。

**[undo label-distribution**]命令用来恢复缺省情况。

【命令】

**[label-distribution**[ { **independent** \| **ordered** }]]

**[undo label-distribution**]

【缺省情况】

标签分发控制方式为有序方式（**ordered**）。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[independent**]：独立方式，即LSR可以在任意时间向与它连接的LSR通告标签映射。

**[ordered**]：有序方式，即LSR只有收到它的下游LSR通告来的特定FEC的标签映射，或该LSR是特定FEC的出口节点时，才会向它的上游LSR通告该FEC的标签映射。

【使用指导】

有序方式的优点是，收到标签时可以确认下游的LSP已经成功建立。

独立方式的优点是，LSP收敛快，因为每个LSR都独立通告标签，不需要等待下游通告标签。

【举例】

\# 配置公网LDP的标签分发控制方式为独立方式。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp label-distribution independent

【相关命令】

·**display mpls ldp parameter**

**LDP \-- LDP公共配置命令 \-- loop-detect**

------------------------------------------------------------------------

**[loop-detect**]命令用来开启环路检测功能。

**[undo** **loop-detect** ]命令用来关闭环路检测功能。

【命令】

**[loop-detect**]

**[undo loop-detect**]

【缺省情况】

环路检测功能处于关闭状态。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

LDP环路检测机制用来检测并避免LSP环路。LDP环路检测有以下几种方式：

·最大跳数方式，详细介绍请参见"1.1.15  (?1376703629#_Ref325015332)maxhops(?1376703629#_Ref325015338)"。

·路径向量方式，详细介绍请参见"1.1.20  (?-1984842639#_Ref286323500)pv-limit(?-1984842639#_Ref286323507)"。

环路检测机制用于非TTL递减设备（如标签控制的ATM交换机）组成的网络。支持TTL递减的设备上启动LDP环路检测功能没有实际用途，还会因为频繁发送标签映射消息来更新环路检测的路径向量或跳数，而产生额外处理开销。因此，不推荐用户使用环路检测功能。

通过**loop-detect**命令开启环路检测功能后，不会对已建立的LDP会话生效。如果要求对已建立的会话生效，则需执行**reset mpls ldp**命令重新建立LDP会话。

【举例】

\# 开启公网LDP的环路检测功能。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp loop-detect

【相关命令】

·**display mpls ldp parameter**

·**maxhops**

·**pv-limit**

**LDP \-- LDP公共配置命令 \-- lsr-id**

------------------------------------------------------------------------

**[lsr-id**]命令用来配置LDP的LSR ID。

**[undo lsr-id**]命令用来删除配置的LDP LSR ID。

【命令】

**[lsr-id*** lsr-id*]

**[undo lsr-id**]

【缺省情况】

未配置LDP LSR ID，公网LDP和VPN实例LDP的LSR ID均为**mpls lsr-id**命令配置的LSR ID。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsr-id*]：LDP的LSR ID，点分十进制格式。

【使用指导】

公网LDP和VPN实例LDP的LSR ID选择方式为：

(1)如果在LDP视图或LDP-VPN实例视图下通过**lsr-id**命令配置了LDP LSR ID，则LDP的LSR ID为此命令配置的值。

(2)否则，LDP的LSR ID为**mpls lsr-id**命令配置的MPLS LSR ID。

同一个LDP实例内所有会话的LSR ID都相同。修改LSR ID配置后，LDP实例使用的LSR ID保持不变。要使用新配置的LSR ID，必须执行**reset mpls ldp**命令重建LDP实例内的所有会话。

公网LDP推荐使用**mpls lsr-id**命令配置的LSR ID。如果要使用**lsr-id**命令配置的LSR ID，推荐使用本地loopback接口的IP地址，以避免非loopback接口的状态down导致LSR ID对应的IP地址未被路由协议通告带来的影响。

【举例】

\# 配置公网LDP的LSR ID为2.2.2.2。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp lsr-id 2.2.2.2

【相关命令】

·**display mpls ldp parameter**

·**mpls lsr-id**（MPLS命令参考/MPLS基础）

**LDP \-- LDP公共配置命令 \-- maxhops**

------------------------------------------------------------------------

**[maxhops**]命令用来配置最大跳数环路检测方式下LSP的最大跳数。

**[undo maxhops**]命令用来恢复缺省情况。

【命令】

**[maxhops** *hop-number*]

**[undo maxhops**]

【缺省情况】

最大跳数环路检测方式下LSP的最大跳数为32。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hop-number*]：最大跳数环路检测方式下LSP的最大跳数值，取值范围为1～32。

【使用指导】

最大跳数环路检测方式的工作机制为：在传递的标签映射（或者标签请求）消息中携带跳数信息，每经过一跳该值就加一。当该值达到本命令配置的最大跳数值时即认为出现环路，终止LSP的建立过程。

请根据网络中LSR的数目和连接方式，合理选择LSP最大跳数。配置的LSP最大跳数较小时，能够快速检测并避免环路，但是要求网络中不能存在经过跳数较多的LSP；配置的LSP最大跳数较大时，允许建立经过跳数较多的LSP，但是环路检测速度较慢。

通过**maxhops**命令配置最大跳数环路检测方式下LSP的最大跳数后，不会对已建立的LDP会话生效。如果要求对已建立的会话生效，则需执行**reset mpls ldp**命令重新建立LDP会话。

【举例】

\# 配置公网LDP的LSP最大跳数为25。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp maxhops 25

【相关命令】

·**display mpls ldp parameter**

·**loop-detect**

·**pv-limit**

**LDP \-- LDP公共配置命令 \-- md5-authentication**

------------------------------------------------------------------------

**[md5-authentication**]命令用来使能LDP的MD5认证功能。

**[undo md5- authentication**]命令用来恢复缺省情况。

【命令】

**[md5-authentication**[ *peer-lsr-id* { **cipher** \| **plain** } *password*]]

**[undo md5-authentication** *peer-lsr-id*]

【缺省情况】

未使能LDP的MD5认证功能。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-lsr-id*]：对等体的LSR ID。

**[cipher**]：表示以密文形式设置密钥。

**[plain**]：表示以明文形式设置密钥。

*[password*]：与指定对等体之间的LDP会话使用的认证密钥值，区分大小写。如果采用**plain**形式，则*password*为1～16个字符的明文字符串；如果采用**cipher**形式，则*password*为1～53个字符的密文字符串。

【使用指导】

为了提高LDP会话的安全性，可以配置在LDP会话使用的TCP连接上采用MD5认证，来验证LDP消息的完整性。

需要注意的是：

·本地配置的密钥必须与对等体上配置的密钥相同。否则，本地LSR和对等体之间无法建立TCP连接。

·指定或改变对等体之间的LDP会话使用的认证密钥值后，不会对已建立的LDP会话生效。如果要求对已建立的会话生效，则需要执行**reset mpls ldp**命令重新建立会话。

·以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。

【举例】

\# 配置公网LDP的MD5认证功能：与对等体3.3.3.3建立的LDP会话上采用MD5认证，以明文形式设置密码，密钥值为pass。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp md5-authentication 3.3.3.3 plain pass

【相关命令】

·**display mpls ldp peer**

**LDP \-- LDP公共配置命令 \-- mpls ldp**

------------------------------------------------------------------------

**[mpls ldp**]命令用来全局使能LSR的LDP能力，并进入LDP视图。

**[undo mpls ldp**]命令用来全局关闭LSR的LDP能力，并删除所有LDP实例。

【命令】

**[mpls ldp**]

**[undo mpls ldp**]

【缺省情况】

未全局使能LSR的LDP能力。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有全局使能LSR的LDP能力后，LSR上才可能正常运行LDP协议。

除了LDP的NSR、GR、会话保护功能相关命令和**targeted-peer**命令外，LDP视图下的命令都可以在LDP-VPN实例视图下使用。其中：

·NSR、GR功能相关命令是全局命令，对所有LDP实例生效。

·会话保护功能相关命令和**targeted-peer**命令只对公网LDP实例生效。

·LDP视图下的命令对公网LDP实例生效。

·LDP-VPN实例视图下的命令对指定VPN的LDP实例生效。

【举例】

\# 全局使能本节点的LDP能力，并进入LDP视图。

\<Sysname\> System-view

Sysname mpls ldp

Sysname-ldp

【相关命令】

·**mpls ldp enable**

·**vpn-instance**

**LDP \-- LDP公共配置命令 \-- mpls ldp timer**

------------------------------------------------------------------------

**[mpls ldp timer**]命令用来配置Hello保持时间、Hello报文发送时间间隔、Keepalive保持时间和Keepalive报文发送时间间隔。

**[undo mpls ldp timer**]命令用来恢复缺省情况。

【命令】

**[mpls ldp timer**[ { **hello-hold** *timeout \|* **hello-interval** *interval* \| **keepalive-hold** *timeout \|* **keepalive-interval** *interval* } ]]

**[undo mpls ldp timer **[{ **hello-hold** \| **hello-interval** \| **keepalive-hold** \| **keepalive-interval** } ]]

【缺省情况】

Link hello保持时间为15秒、Link hello报文发送时间间隔为5秒、Targeted hello保持时间为45秒、Targeted hello报文发送时间间隔为15秒、Keepalive保持时间为45秒、Keepalive报文发送时间间隔为15秒。

【视图】

接口视图/LDP对等体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hello-hold*** timeout*]：指定Hello保持时间。Hello保持时间用来控制LSR保持与对端的Hello邻接关系的时间。LSR将本端和对端的Hello保持时间中的较小者，作为Hello保持定时器的值。如果在Hello保持定时器超时时，仍没有收到来自对端的Hello消息，则删除与对端的Hello邻接关系。*timeout*取值范围为1～65535，单位为秒。取值为65535表示无穷大，即永远保持与对端的Hello邻接关系。

**[hello-interval ***interval*]：指定Hello报文发送时间间隔。*interval*取值范围为1～65535，单位为秒。

**[keepalive-hold*** timeout*]：指定Keepalive保持时间。Keepalive保持时间用来控制LSR保持与对等体的LDP会话的时间。LSR将本端和对端的Keepalive保持时间中的较小者，作为Keepalive保持定时器的值。如果在Keepalive保持定时器超时时，仍没有收到来自对等体的任何LDP消息，则删除与该对等体的LDP会话。*timeout*取值范围为15～65535，单位为秒。

**[keepalive-interval*** interval*]：指定Keepalive报文发送时间间隔。*interval*取值范围为1～65535，单位为秒。

【使用指导】

接口视图下配置的是Link hello保持时间和Link hello报文发送时间间隔；LDP对等体视图下配置的是Targeted hello保持时间和Targeted hello报文发送时间间隔。

如果设置的Hello保持时间和Keepalive保持时间过大，则可能会导致LDP不能快速发现链路故障；如果设置的值过小，则可能会导致LDP错误地将未故障链路判断为故障链路。建议使用缺省值。

需要注意的是：

·如果两个LSR之间存在多个邻接关系，如通过多条直连链路相连时存在多个Link hello邻接关系或同时存在Link hello和Targeted hello邻接关系时，则两个LSR之间的所有链路和LDP对等体视图下配置的KeepAlive保持时间必须相同。

·配置了LDP会话保护、LDP over MPLS TE、MPLS L2VPN LDP PW或VPLS LDP PW后，LDP自动向指定对等体发送Targeted hello消息来建立LDP会话，如果要修改Targeted hello或KeepAlive的保持时间及发送时间间隔，必须使用**targeted-peer**命令创建对等体，并在LDP对等体视图下进行配置。

·LDP邻居发现时，LSR比较本地配置的Hello保持时间与Hello消息中携带的对端LSR上配置的Hello保持时间，从中选择较小者作为协商后的Hello保持时间。如果协商后的Hello保持时间大于本地配置的Hello报文发送时间间隔的三倍，则Hello报文的实际发送时间间隔为本地配置的值；否则，为协商后Hello保持时间的1/3。

·LDP会话协商时，通过交换会话初始化消息，LSR比较本地配置的Keepalive保持时间与对端LSR上配置的Keepalive保持时间，从中选择较小者作为协商后的Keepalive保持时间。如果协商后的Keepalive保持时间大于本地配置的Keepalive报文发送时间间隔的三倍，则Keepalive报文的实际发送时间间隔为本地配置的值；否则，为协商后Keepalive保持时间的1/3。

·通过**mpls ldp timer**命令配置Keepalive保持时间和Keepalive报文发送时间间隔后，不会对已建立的LDP会话生效。如果要求对已建立的会话生效，则需执行**reset mpls ldp**命令重新建立LDP会话。

【举例】

\# 为对等体3.3.3.3配置Targeted hello保持时间为1000秒、Targeted hello报文的发送时间间隔为50秒、Keepalive保持时间为1000秒、Keepalive报文发送时间间隔为50秒。

\<Sysname\> System-view

Sysname mpls ldp

Sysname-ldp targeted-peer 3.3.3.3

Sysname-ldp-peer-3.3.3.3 mpls ldp timer hello-hold 1000

Sysname-ldp-peer-3.3.3.3 mpls ldp timer hello-interval 50

Sysname-ldp-peer-3.3.3.3 mpls ldp timer keepalive-hold 1000

Sysname-ldp-peer-3.3.3.3 mpls ldp timer keepalive-interval 50

·路由应用

\# 在接口GigabitEthernet1/0/1上配置Link hello保持时间为100秒、Link hello报文的发送时间间隔为20秒、Keepalive保持时间为50秒、Keepalive报文发送时间间隔为10秒。

\<Sysname\> System-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls ldp timer hello-hold 100

Sysname-GigabitEthernet1/0/1 mpls ldp timer hello-interval 20

Sysname-GigabitEthernet1/0/1 mpls ldp timer keepalive-hold 50

Sysname-GigabitEthernet1/0/1 mpls ldp timer keepalive-interval 10

·交换应用

\# 在接口Vlan-interface2上配置Link hello保持时间为100秒、Link hello报文的发送时间间隔为20秒、Keepalive保持时间为50秒、Keepalive报文发送时间间隔为10秒。

\<Sysname\> System-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mpls ldp timer hello-hold 100

Sysname-Vlan-interface2 mpls ldp timer hello-interval 20

Sysname-Vlan-interface2 mpls ldp timer keepalive-hold 50

Sysname-Vlan-interface2 mpls ldp timer keepalive-interval 10

【相关命令】

·**display mpls ldp discovery**

·**display mpls ldp peer**

**LDP \-- LDP公共配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

![说明](LDP命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[non-stop-routing**]命令用来使能LDP NSR功能。

**[undo non-stop-routing**]命令用来关闭LDP NSR功能。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【缺省情况】

LDP NSR功能处于关闭状态。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

LDP NSR（Nonstop Routing，不间断路由）是一种通过在LDP协议主备进程之间备份必要的协议状态和数据（如LDP会话信息和LSP信息），使得LDP协议的主进程中断时，备份进程能够无缝地接管主进程的工作，从而确保对等体感知不到LDP协议中断，保证LDP会话保持Operational状态，并保证转发不会中断的技术。

导致LDP主进程中断的事件包括以下几种：

·LDP主进程重启

·LDP主进程所在的主控板发生故障导致

·LDP主进程所在的主控板进行ISSU（In-Service Software Upgrade，不中断业务升级）

·进程分布优化为LDP进程决策出的位置不同于当前运行的位置而进行进程主备倒换

LDP NSR与LDP GR具有如下区别，请根据实际情况选择合适的方式确保数据转发不中断：

·对设备要求不同：LDP协议的主进程和备进程运行在不同的主控板上，因此要运行LDP NSR功能，设备上必须有两个或两个以上的主控板。要运行LDP GR功能，设备上可以只有一个主控板。

·对LDP对等体的要求不同：使用LDP NSR功能时，LDP对等体不会感知本地设备发生了LDP进程的异常重启或主备倒换等故障，不需要LDP对等体协助恢复MPLS转发信息。LDP GR要求LDP对等体能够识别本地设备的GR能力标识（即能处理Initialization消息中的GR相关扩展），并且在LDP会话中断恢复时，LDP对等体能够作为GR helper协助本地设备恢复MPLS转发信息。

【举例】

\# 使能LDP NSR功能。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp non-stop-routing

【相关命令】

·**display mpls ldp ****discovery**

·**display mpls ldp ****fec**

·**display mpls ldp ****peer**

·**display mpls ldp**** summary**

**LDP \-- LDP公共配置命令 \-- pv-limit**

------------------------------------------------------------------------

**[pv-limit**]命令用来配置路径向量环路检测方式下LSP的最大跳数。

**[undo pv-limit**]命令用来恢复缺省情况。

【命令】

**[pv-limit** *pv-number*]

**[undo pv-limit**]

【缺省情况】

路径向量环路检测方式下LSP的最大跳数为32。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[pv-number*]：路径向量环路检测方式下LSP的最大跳数，取值范围为1～32。

【使用指导】

路径向量环路检测方式的工作机制为：

·在传递的标签映射（或者标签请求）消息中记录路径信息，即记录经过的每一跳LSR的LSR ID。每个LSR接收到标签映射（或者标签请求）消息后，都会检查自己的LSR ID是否在记录的路径信息中。如果路径信息中没有本LSR的LSR ID，LSR就会将自己的LSR ID添加到其中；如果已存在本LSR的LSR ID，则认为出现环路，终止LSP的建立过程。

·采用路径向量方式进行环路检测时，也需要规定LSP的最大跳数。当路径信息中的LSR ID数目达到本命令配置的最大跳数值时，也会认为出现环路，终止LSP的建立过程。

通过**pv-limit**命令配置路径向量环路检测方式下LSP的最大跳数后，不会对已建立的LDP会话生效。如果要求对已建立的会话生效，则需执行**reset mpls ldp**命令重新建立LDP会话。

【举例】

\# 设置公网LDP路径向量环路检测方式下LSP的最大跳数为3。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp pv-limit 3

【相关命令】

·**display mpls ldp parameter**

·**loop-detect**

·**maxhops**

**LDP \-- LDP公共配置命令 \-- reset mpls ldp**

------------------------------------------------------------------------

**[reset mpls ldp**]命令用来重启LDP会话。

【命令】

**[reset mpls ldp ** **vpn-instance** *vpn-instance-name* ]  **peer** *peer-id*

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：重启指定LDP实例的会话。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则重启公网LDP实例的会话。

**[peer** *peer-id*]：重启与指定对等体之间的LDP会话。*peer-id*为对等体的LSR ID。如果不指定本参数，则重启公网或指定LDP实例中的所有会话。

【使用指导】

重启LDP会话后，指定的LDP会话将会被删除并重新建立，基于该LDP会话建立的LSP也将删除并重新建立。

修改LDP会话参数后，可以通过配置**reset mpls ldp**命令重启公网或指定LDP实例中的所有会话，使新配置的LDP参数生效。如果指定**peer**参数，则仅重启与指定对等体之间的LDP会话，新配置的LDP参数不会生效。

【举例】

\# 重启公网LDP实例的所有会话。

\<Sysname\> reset mpls ldp

\# 重启VPN实例vpn1的所有LDP会话。

\<Sysname\> reset mpls ldp vpn-instance vpn1

**LDP \-- LDP公共配置命令 \-- snmp-agent trap enable ldp**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable ldp**]命令用来开启LDP模块的告警功能。

**[undo** **snmp-agent** **trap** **enable ldp**]命令用来关闭LDP模块的告警功能。

【命令】

**[snmp-agent** **trap** **enable** **ldp**]

**[undo** **snmp-agent** **trap** **enable** **ldp**]

【缺省情况】

LDP模块的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启LDP模块的告警功能后，当LDP会话状态发生变化时会产生RFC 3815中规定的告警信息。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启LDP模块的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable ldp

**LDP \-- LDP公共配置命令 \-- vpn-instance**

------------------------------------------------------------------------

**[vpn-instance**]命令用来使能指定VPN实例的LDP能力，为该VPN创建LDP实例，并进入LDP-VPN实例视图。

**[undo vpn-instance**]命令用来删除指定VPN的LDP实例。

【命令】

**[vpn-instance** *vpn-instance-name*]

**[undo vpn-instance** *vpn-instance-name*]

【缺省情况】

没有为任何VPN创建LDP实例。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

为VPN创建LDP实例主要用于一级运营商PE与二级运营商PE之间采用LDP协议的"运营商的运营商"组网环境。在此组网中，一级运营商PE上需要为每个VPN配置相应的LDP实例。

除了LDP的DSCP、NSR、GR、IGP同步功能相关命令、会话保护功能相关命令和**targeted-peer**命令外，LDP视图下的命令都可以在LDP-VPN实例视图下使用。其中：

·DSCP、NSR、GR功能相关命令是全局命令，对所有LDP实例生效。

·IGP同步功能相关命令、会话保护功能相关命令和**targeted-peer**命令只对公网LDP实例生效。

·LDP视图下的命令对公网LDP实例生效。

·LDP-VPN实例视图下的命令对指定VPN的LDP实例生效。

需要注意的是，本命令中指定的VPN实例必须已经通过系统视图下的**ip vpn-instance**命令创建。

【举例】

\# 使能VPN实例vpn1的LDP能力，建立LDP实例，并进入LDP-VPN实例视图。

\<Sysname\> System-view

Sysname mpls ldp

Sysname-ldp vpn-instance vpn1

Sysname-ldp-vpn-instance-vpn1

【相关命令】

·**ip vpn-instance**（MPLS命令参考/MPLS L3VPN）

·**mpls ldp**

**LDP \-- LDP IPv4配置命令 \-- accept-label**

------------------------------------------------------------------------

**[accept-label**]命令用来配置标签接受控制策略。

**[undo accept-label**]命令用来取消标签接受控制策略。

【命令】

**[accept-label peer** *peer-lsr-id* **prefix-list** *prefix-list-name*]

**[undo accept-label peer ***peer-lsr-id*]

【缺省情况】

未配置标签接受控制策略，接受来自所有对等体的所有IPv4地址前缀的标签映射。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer ***peer-lsr-id*]：指定LDP对等体。*peer-lsr-id*为LDP对等体的LSR ID。

**[prefix-list*** prefix-list-name*]：指定用来对收到的IPv4地址前缀标签映射进行过滤的IPv4地址前缀列表。*prefix-list-name*表示IPv4地址前缀列表名，为1～63个字符的字符串，区分大小写。

【使用指导】

标签接受控制策略用来对来自特定对等体的标签映射进行过滤。对于来自指定对等体的标签映射，只有标签映射中FEC的IPv4地址前缀通过指定IPv4地址前缀列表的过滤时，LSR才接受该标签映射，否则LSR不会接受且不会保存该标签映射。

当LSR接收到的标签映射数量较大时，可以配置标签接受控制策略，有选择地接受来自特定对等体的标签映射，减少LSR接受的标签映射数量，降低设备内存等资源的消耗。

需要注意的是：

·当LSR上配置的标签接受控制策略发生变化，使得LSR可以接受来自特定对等体的、以前被拒绝的标签映射时（如执行**undo accept-label**命令删除标签接受控制策略，或者将IPv4地址前缀列表的过滤条件修改得更宽松时），只有执行**reset mpls ldp**命令重建与特定对等体的LDP会话，触发指定对等体重新通告标签映射，LSR才能获取之前拒绝的标签映射。

·在下游LSR上配置标签通告控制策略与在上游LSR上配置标签接受控制策略具有相同的效果。如果下游LSR支持配置标签通告控制策略，则推荐使用标签通告控制策略，以减轻网络负担。

【举例】

\# 对于LSR ID为1.1.1.9的LDP对等体通告的标签映射，只接受IPv4地址前缀属于10.1.1.0/24和10.2.1.0/24网段的标签映射。

\<Sysname\> system-view

Sysname ip prefix-list prefix-from-RTA index 1 permit 10.1.1.0 24

Sysname ip prefix-list prefix-from-RTA index 2 permit 10.2.1.0 24

Sysname mpls ldp

Sysname-ldp accept-label peer 1.1.1.9 prefix-list prefix-from-RTA

【相关命令】

·**display mpls ldp peer verbose**

·**ip prefix-list**（三层技术-IP路由命令参考/路由策略）

**LDP \-- LDP IPv4配置命令 \-- advertise-label**

------------------------------------------------------------------------

**[advertise-label**]命令用来配置标签通告控制策略。

**[undo advertise-label**]命令用来取消标签通告控制策略。

【命令】

**[advertise-label prefix-list ***prefix-list-name* [ **peer** *peer-prefix-list-name* ]]

**[undo advertise-label prefix-list ***prefix-list-name*]

【缺省情况】

未配置标签通告控制策略，即向所有对等体通告满足LSP触发策略的所有IPv4地址前缀的标签映射。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[prefix-list*** prefix-list-name*]：指定用来对将要通告的标签映射进行过滤的IPv4地址前缀列表。*prefix-list-name*表示IPv4地址前缀列表名，为1～63个字符的字符串，区分大小写。

**[peer ***peer-prefix-list-name*]：指定用来对LDP对等体进行过滤的IPv4地址前缀列表。*peer-prefix-list-name*表示IPv4地址前缀列表名，为1～63个字符的字符串，区分大小写。如果不指定本参数，则表示向所有对等体通告标签映射。

【使用指导】

标签通告控制策略用来实现对本地LSR向对等体通告的标签映射进行过滤。

多次执行本命令，可以配置多条标签通告控制策略。

LSR按照下面的规则来判断是否向特定对等体通告标签：

·如果待通告的标签映射的IPv4地址前缀没有通过IPv4地址前缀列表的检查（没有匹配任何一条**permit**规则或匹配了**deny**规则），则不向任何对等体通告该标签映射。

·如果待通告的标签映射的IPv4地址前缀通过某个IPv4地址前缀列表的检查，且对应标签通告控制策略中的对等体IPv4地址前缀列表为空（只配置**advertise-label prefix-list ***prefix-list-name，*没有指定**peer ***peer-prefix-list-name*），则向所有对等体通告该标签映射。

·如果待通告的标签映射的IPv4地址前缀通过某个IPv4地址前缀列表的检查，且对应标签通告控制策略中指定了对等体IPv4地址前缀列表，则只向通过对等体IPv4地址前缀列表检查的对等体通告该标签映射。

·如果待通告的标签映射的IPv4地址前缀通过多于一个IPv4地址前缀列表的检查（多次执行**advertise-label**命令配置多条标签通告控制策略），则以配置的第一条命令为准。

在下游LSR上配置标签通告控制策略与在上游LSR上配置标签接受控制策略具有相同的效果。如果下游LSR支持配置标签通告控制策略，则推荐使用标签通告控制策略，以减轻网络负担。

【举例】

\# 配置标签通告控制策略：向LSR ID为3.3.3.9的对等体通告网段地址10.1.1.0/24对应的标签映射；向LSR ID为4.4.4.9的对等体通告网段地址10.2.1.0/24对应的标签映射；不通告其他网段地址对应的标签映射。

\<Sysname\> system-view

Sysname ip prefix-list prefix-to-C permit 10.1.1.0 24

Sysname ip prefix-list prefix-to-D permit 10.2.1.0 24

Sysname ip prefix-list peer-C permit 3.3.3.9 32

Sysname ip prefix-list peer-D permit 4.4.4.9 32

Sysname mpls ldp

Sysname-ldp advertise-label prefix-list prefix-to-C peer peer-C

Sysname-ldp advertise-label prefix-list prefix-to-D peer peer-D

【相关命令】

·**display mpls ldp fec**

·**ip prefix-list**（三层技术-IP路由命令参考/路由策略）

·**lsp-trigger**

**LDP \-- LDP IPv4配置命令 \-- display mpls ldp igp sync**

------------------------------------------------------------------------

**[display mpls ldp igp sync**]命令用来显示LDP IGP同步信息。

【命令】

**[display mpls ldp igp sync ** **interface**] *interface-type interface-number*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的LDP IGP同步信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则显示所有接口的LDP IGP同步信息。

【举例】

\# 显示所有接口的LDP IGP同步信息。

\<Sysname\> display mpls ldp igp sync

GigabitEthernet1/0/2:

  IGP protocols: OSPF

  Sync status: Ready

  Peers:

    10.1.1.2:0

GigabitEthernet1/0/6:

  IGP protocols: OSPF, IS-IS

  Sync status: Delayed (24 sec remaining)

  Peers:

    20.1.1.2:0

GigabitEthernet1/0/8:

  LDP-IGP synchronization is disabled on the interface

表1-12 display mpls ldp igp sync命令显示信息描述表

字段

描述

IGP protocols

要求LDP IGP同步的IGP协议，取值包括OSPF、IS-IS

Sync status

接口上的LDP IGP同步状态，取值包括：

·Ready：LDP已收敛，可以被IGP使用

·Delayed：满足LDP收敛条件，但处于IGP延迟等待期间，remaining为延迟剩余时间，单位为秒

·Not ready：LDP未收敛，不可以被IGP使用

·LDP not enabled：接口上没有使能LDP

Peers

接口上已收敛的LDP对等体

LDP-IGP synchronization is disabled on the interface

接口上禁止LDP IGP同步功能

**LDP \-- LDP IPv4配置命令 \-- igp sync delay**

------------------------------------------------------------------------

**[igp sync delay**]命令用来配置向IGP通知LDP已收敛的延迟时间。

**[undo igp sync delay**]命令用来恢复缺省情况。

【命令】

**[igp sync delay*** time*]

**[undo igp sync delay**]

【缺省情况】

LDP收敛后立即通知IGP。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：向IGP通知LDP收敛的延迟时间，取值范围为5～300，单位为秒。

【使用指导】

同时满足如下条件时，设备认为LDP在某条链路上已收敛：

·在该链路上本地设备至少与一个对等体建立了LDP会话，且该LDP会话已进入operational状态。

·在该链路上本地设备至少向一个对等体发送完标签映射。

缺省情况下，LDP在某条链路上收敛后立即通知IGP，以便IGP发布该链路的正常开销值。但是，在某些情况下，LDP收敛后立即通知IGP，可能会导致MPLS流量转发中断，例如：

·对等体的标签分发控制方式为有序方式时，LDP会话进入operational状态后，设备需要等待下游的标签映射。如果尚未收到下游的标签映射就向IGP通知LDP收敛，则可能导致MPLS流量转发中断。

·下游的标签映射比较多时，如果LDP收敛后立即通知IGP，则下游的标签映射可能尚未通告完成，导致MPLS流量转发中断。

在这些情况下，需要通过本命令配置恰当的延迟通知时间，即LDP在某条链路上收敛后，等待延迟时间再通知IGP，以最大限度地缩短MPLS流量中断的时间。

【举例】

\# 配置LDP收敛后延迟通知IGP的时间为30秒。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp igp sync delay 30

【相关命令】

·**igp****sync delay on-restart**

·**mpls ldp igp sync disable**

·**mpls ldp sync** (IS-IS view)

·**mpls ldp sync** (OSPF view/OSPF area view)

**LDP \-- LDP IPv4配置命令 \-- igp sync delay on-restart**

------------------------------------------------------------------------

**[igp sync delay on-restart**]命令用来配置在LDP协议重启或倒换后，向IGP通告LDP IGP同步状态的最大延迟时间。

**[undo igp sync delay on-restart**]命令用来恢复缺省情况。

【命令】

**[igp sync delay******on-restart ***time*]

**[undo igp sync delay on-restart**]

【缺省情况】

在LDP协议重启或倒换后，向IGP通告LDP IGP同步状态的最大延迟时间为90秒。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：在LDP协议重启或倒换后，向IGP通告LDP IGP同步状态的最大延迟时间，取值范围为60～600，单位为秒。

【使用指导】

LDP协议重启或倒换后，需要等待一段时间LDP才会收敛。如果在协议重启或倒换后，LDP立即将当前所有的LDP IGP同步状态通知给IGP，在LDP收敛后再更新这些状态，则可能会导致IGP频繁地根据不同的同步状态进行处理，增加了IGP的处理开销。

LDP协议重启或倒换后的延迟通知机制可以用来解决上述问题。该机制提供了LDP进程级别的延迟通知时间，即在LDP协议重启或倒换的情况下，等待LDP恢复到重启或倒换前的收敛状态后，再批量通知LDP IGP同步状态，以减少IGP的处理开销。如果到达本命令指定的最大延迟时间时，仍未恢复之前的收敛状态，则立即向IGP批量通告当前的LDP IGP同步状态。

【举例】

\# 配置LDP协议重启或倒换后，向IGP通告LDP IGP同步状态的最大延迟时间为300秒。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp igp sync delay on-restart 300

【相关命令】

·**igp****sync delay**

·**mpls ldp igp sync disable**

·**mpls ldp sync** (IS-IS view)

·**mpls ldp sync** (OSPF view/OSPF area view)

**LDP \-- LDP IPv4配置命令 \-- import bgp**

------------------------------------------------------------------------

**[import bgp**]命令用来配置LDP引入BGP IPv4单播路由。

**[undo import bgp**]命令用来恢复缺省情况。

【命令】

**[import bgp**]

**[undo import bgp**]

【缺省情况】

LDP不主动引入BGP IPv4单播路由。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，LDP自动引入IPv4 IGP路由（包括已引入到IGP的BGP IPv4单播路由），并为通过LSP触发策略的IGP路由和通过LSP触发策略的带标签BGP路由分配标签，但不自动引入未被引入到IGP的BGP IPv4单播路由。这就导致了在一些特殊的组网环境下，如在运营商的运营商组网中，如果一级运营商的PE与二级运营商CE之间未配置OSPF、IS-IS等IGP协议，则无法通过LDP为BGP IPv4单播路由分配标签，因而无法建立LDP LSP。有关运营商的运营商组网的详细信息，请参见"MPLS配置指导"中的"MPLS L3VPN"。

通过配置LDP引入BGP IPv4单播路由，可将BGP IPv4单播路由强制引入至LDP，如果该路由通过LSP触发策略，则为其分配标签建立LSP。

配置此命令后，可能会导致LDP引入大量的BGP IPv4单播路由，占用设备的标签、内存资源等问题，建议仅在必要时使用此命令。

【举例】

\# 在公网LDP实例下，配置LDP主动引入BGP IPv4单播路由。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp import bgp

【相关命令】

·**lsp-trigger**

**LDP \-- LDP IPv4配置命令 \-- lsp-trigger**

------------------------------------------------------------------------

**[lsp-trigger**]命令用来配置IPv4 FEC的LSP的触发策略。

**[undo lsp-trigger**]命令用来恢复缺省情况。

【命令】

**[lsp-trigger **[[ **all** \| **prefix-list** *prefix-list-name* }]]

**[undo lsp-trigger**]

【缺省情况】]

只有引入到LDP的32位掩码的IPv4主机路由能够触发建立LSP。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有引入到LDP的路由表项都会触发LDP建立LSP。

**[prefix-list*** prefix-list-name*]：利用IPv4地址前缀列表对引入到LDP的路由表项进行过滤，通过IPv4地址前缀列表过滤的路由表项可以触发建立LSP，被IPv4地址前缀列表拒绝的路由表项不触发建立LSP。*prefix-list-name*表示IPv4地址前缀列表名，为1～63个字符的字符串，区分大小写。

【使用指导】

LSP触发策略用来控制引入到LDP的路由中的哪些路由可以建立LDP LSP。

缺省情况下，LSP的触发策略与标签分发控制方式有关：

·有序方式下：只有32位掩码的本地Loopback接口地址路由和已经收到下游通告的标签映射且掩码为32位的路由可以触发建立LDP LSP。

·独立方式下：只要是32位掩码的路由都会触发建立LDP LSP。

配置触发策略后，引入到LDP中的所有路由或通过IPv4地址前缀列表的路由都会触发建立LDP LSP，独立和有序标签分发控制方式的处理没有差别。

建议用户使用缺省的LSP触发策略。

【举例】

\# 配置公网LDP实例中只有引入到LDP中的网段路由10.10.1.0/24和10.20.1.0/24能够触发建立LDP LSP。

\<Sysname\> system-view

Sysname ip prefix-list egress-fec-list index 1 permit 10.10.1.0 24

Sysname ip prefix-list egress-fec-list index 2 permit 10.20.1.0 24

Sysname mpls ldp

Sysname-ldp lsp-trigger prefix-list egress-fec-list

【相关命令】

·**import bgp**

·**ip prefix-list**（三层技术-IP路由命令参考/路由策略）

**LDP \-- LDP IPv4配置命令 \-- mpls ldp enable**

------------------------------------------------------------------------

**[mpls ldp enable**]命令用来使能接口的LDP支持IPv4能力。

**[undo mpls ldp enable**]命令用来关闭接口的LDP支持IPv4能力。

【命令】

**[mpls ldp enable**]

**[undo mpls ldp enable**]

【缺省情况】

未使能接口的LDP支持IPv4能力。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果在接口上通过**mpls enable**命令使能了MPLS能力和LDP支持IPv4能力，且该接口处于up状态，则LDP会在该接口上启动基本发现机制，通过该接口发送IPv4 Link hello消息。

在LDP over MPLS TE组网环境下，如果在MPLS TE隧道接口上使能了LDP能力，且MPLS TE隧道接口处于up状态，则LDP将启动扩展发现机制，向隧道目的地址发送Targeted hello消息，尝试建立跨越MPLS TE隧道的LDP会话，以建立承载在MPLS TE隧道之上的LDP LSP。

需要注意的是：

·执行本命令前，需要先在系统视图下执行**mpls ldp**命令全局使能LSR的LDP能力。

·如果接口已与某个VPN实例绑定，则需要通过**vpn-instance**命令使能此VPN实例的LDP能力。

·取消接口的LDP能力将会导致接口下的所有LDP会话中断，基于这些会话的所有LSP也将被删除。

·同一接口上既可以通过配置**mpls ldp enable**使能LDP支持IPv4能力，也可以通过配置**mpls ldp ipv6 enable**使能LDP支持IPv6能力。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使能LDP支持IPv4能力。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls ldp enable

·交换应用

\# 在接口Vlan-interface2上使能LDP支持IPv4能力。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp quit

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mpls ldp enable

【相关命令】

·**display mpls ldp interface**

·**mpls enable**（MPLS命令参考/MPLS基本配置）

·**mpls ldp**

·**mpls ldp**** ipv6 enable**

**LDP \-- LDP IPv4配置命令 \-- mpls ldp sync (IS-IS view)**

------------------------------------------------------------------------

**[mpls ldp sync**]命令用来使能LDP IS-IS同步功能。

**[undo mpls ldp sync**]命令用来关闭LDP IS-IS同步功能。

【命令】

**[mpls ldp sync**[ [ **level-1** \| **level-2** ]]]

**[undo****mpls ldp sync**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

LDP IS-IS同步功能处于关闭状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：在Level-1使能LDP IS-IS同步功能。

**[level-2**]：在Level-2使能LDP IS-IS同步功能。

【使用指导】

LDP基于IGP最优路由建立LSP，LDP和IGP不同步可能导致MPLS流量转发中断。LDP IGP同步功能用来解决上述问题。

启用LDP IGP同步功能后，只有LDP在某条链路上收敛，IGP才会为这条链路通告正常的开销值，否则通告链路开销的最大值，使得这条链路在IGP拓扑中可见，但是在其它链路可用的情况下，IGP不会将该链路选为最优路由，从而确保设备收到MPLS报文时，不会因为最优路由上的LDP LSP没有建立而丢弃MPLS报文。

执行本命令时，需要注意的是：

·如果不指定级别，则同时使能Level-1和Level-2的LDP IS-IS同步功能。

·执行**isis**命令时，如果通过**vpn-instance** *vpn-instance-name*参数指定了IS-IS进程所属的VPN实例，则该IS-IS进程下不能通过本命令使能LDP IGP同步功能。

·在同一个IS-IS进程下，如果重复执行本命令，则新的配置覆盖原有配置。例如，执行**mpls ldp sync**命令同时使能Level-1和Level-2的LDP IS-IS同步功能后，如果再执行**mpls ldp sync level-1**命令，则使能Level-1的LDP IS-IS同步功能，关闭Level-2的LDP IS-IS同步功能。

【举例】

\# 在IS-IS进程1的Level-2上使能LDP IS-IS同步功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 mpls ldp sync level-2

【相关命令】

·**display mpls ldp igp sync**

·**igp sync delay**

·**igp sync delay on-restart**

·**mpls ldp igp sync disable**

**LDP \-- LDP IPv4配置命令 \-- mpls ldp sync (OSPF view/OSPF area view)**

------------------------------------------------------------------------

**[mpls ldp sync**]命令用来使能LDP OSPF同步功能。

**[undo mpls ldp sync**]命令用来关闭LDP OSPF同步功能。

【命令】

**[mpls ldp sync**]

**[undo mpls ldp sync**]

【缺省情况】

LDP OSPF同步功能处于关闭状态。

【视图】

OSPF视图/OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

LDP基于IGP最优路由建立LSP，LDP和IGP不同步可能导致MPLS流量转发中断。LDP IGP同步功能用来解决上述问题。

启用LDP IGP同步功能后，只有LDP在某条链路上收敛，IGP才会为这条链路通告正常的开销值，否则通告链路开销的最大值，使得这条链路在IGP拓扑中可见，但是在其它链路可用的情况下，IGP不会将该链路选为最优路由，从而确保设备收到MPLS报文时，不会因为最优路由上的LDP LSP没有建立而丢弃MPLS报文。

执行本命令时，需要注意的是：

·执行**ospf**命令时，如果通过**vpn-instance** *vpn-instance-name*参数指定了OSPF进程所属的VPN实例，则该OSPF进程下、该进程的OSPF区域下不能配置LDP IGP同步功能。

·如果在OSPF进程下执行本命令，则该OSPF进程下的所有区域都使能LDP OSPF同步功能；如果在OSPF区域下执行本命令，则只在该区域下使能LDP OSPF同步功能。

【举例】

\# 在OSPF进程1上使能LDP OSPF同步功能。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 mpls ldp sync

【相关命令】

·**display mpls ldp igp sync**

·**igp sync delay**

·**igp sync delay on-restart**

·**mpls ldp igp sync disable**

**LDP \-- LDP IPv4配置命令 \-- mpls ldp igp sync disable**

------------------------------------------------------------------------

**[mpls ldp igp sync disable**]命令用来在接口上禁止LDP IGP同步功能。

**[undo mpls ldp igp sync disable**]命令用来恢复缺省情况。

【命令】

**[mpls ldp igp sync disable**]

**[undo mpls ldp igp sync disable**]

【缺省情况】

接口上未禁止LDP IGP同步功能。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在IGP协议（如OSPF区域、IS-IS进程）下使能LDP IGP同步功能后，与该IGP实例相关的接口上将使能LDP IGP同步功能。如果某个接口不希望使能LDP IGP同步功能，则可以通过在该接口上执行**mpls ldp igp sync diasable**命令禁止接口上的LDP IGP同步功能。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上禁止LDP IGP同步功能。

\<Sysname\> System-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls ldp igp sync disable

·交换应用

\# 在接口Vlan-interface2上禁止LDP IGP同步功能。

\<Sysname\> System-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mpls ldp igp sync disable

【相关命令】

·**mpls ldp sync** (IS-IS view)

·**mpls ldp sync** (OSPF view/OSPF area view)

**LDP \-- LDP IPv4配置命令 \-- mpls ldp transport-address**

------------------------------------------------------------------------

**[mpls ldp transport-address**]命令用来配置LDP传输地址。

**[undo mpls ldp transport-address**]命令用来恢复缺省情况。

【命令】

接口视图下：

**[mpls ldp transport-address**[ { *ip-address* \| **interface** }]]

**[undo mpls ldp transport-address **[{ *ip-address* \| **interface** }]]

LDP对等体视图下：

**[mpls ldp transport-address** *ip-address*]

**[undo mpls ldp transport-address**]

【缺省情况】

接口视图下：

接口属于公网，则传输地址是本LSR的LSR ID；

接口属于某个VPN，则传输地址是本接口的主IPv4地址。

对等体视图下：

传输地址为LSR的LSR ID。

【视图】

接口视图/LDP对等体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：LDP使用此地址作为LDP传输地址。

**[interface**]：LDP使用当前接口的IPv4地址作为LDP传输地址。

【使用指导】

在两个LSR之间建立LDP会话之前，需要先建立TCP连接。本命令配置的LDP传输地址就是LSR建立用于LDP会话的TCP连接时使用的地址。

建议用户不要修改LDP传输地址，采用传输地址的缺省值。

需要注意的是，当两个LSR之间存在多条链路时，如果要在这多条链路上都建立LDP会话，则所有链路上配置的传输地址必须相同。

【举例】

\# 配置与对等体3.3.3.3建立TCP连接时采用的LDP传输地址为2.2.2.2，即向对等体3.3.3.3发送的Targeted hello消息中携带的传输地址为2.2.2.2。

\<Sysname\> System-view

Sysname mpls ldp

Sysname-ldp targeted-peer 3.3.3.3

Sysname-ldp-peer-3.3.3.3 mpls ldp transport-address 2.2.2.2

·路由应用

\# 在接口GigabitEthernet1/0/1上配置Link hello消息中携带的传输地址为本接口的IP地址。

\<Sysname\> System-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls ldp transport-address interface

·交换应用

\# 在接口Vlan-interface2上配置Link hello消息中携带的传输地址为本接口的IP地址。

\<Sysname\> System-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mpls ldp transport-address interface

【相关命令】

·**display mpls ldp discovery**

·**targeted-peer**

**LDP \-- LDP IPv4配置命令 \-- session protection**

------------------------------------------------------------------------

**[session protection**]命令用来使能会话保护功能。

**[undo session protection**]命令用来关闭会话保护功能。

【命令】

**[session protection ** **duration** *time* ]  **peer** *peer-prefix-list-name *

**[undo session protection**]

【缺省情况】

未使能会话保护功能。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[duration*** time*]：会话保护持续时间，取值范围为30～2147483，单位为秒。如果不指定本参数，则会话保护永久持续。

**[peer ***peer-prefix-list-name*]：指定被保护的LDP会话。只有对等体的LSR ID通过IP地址前缀列表过滤时，才会保护本端与该对等体之间的会话。*peer-prefix-list-name*表示IP地址前缀列表名，为1～63个字符的字符串，区分大小写。如果不指定本参数，则表示保护所有通过基本发现机制建立的LDP会话。

【使用指导】

会话保护功能实现了基本发现机制失效时，利用扩展发现机制来保持与对等体的会话，确保基本发现机制恢复时，LDP协议能够快速收敛。会话保护功能主要应用在LDP对等体之间存在直连（只有一跳）和非直连（多于一跳）多条路径的组网环境中。

使能与指定对等体的会话保护功能后，如果通过Link hello消息发现了该直连的LDP对等体，则本地LSR不仅与其建立Link hello邻接关系，还会向该对等体发送Targeted hello消息，与其建立Targeted hello邻接关系。当直连链路出现故障时，Link hello邻接关系将被删除。如果此时非直连链路正常工作，则Targeted hello邻接关系依然存在，因此，LDP会话不会被删除，基于该会话的FEC---标签映射等信息也不会删除。直连链路恢复后，不需要重新建立LDP会话、重新学习FEC---标签映射等信息，从而加快了LDP收敛速度。

使能会话保护功能时，还可以指定会话保护持续时间，即Link hello邻接关系被删除后，保留Targeted hello邻接关系的时间。如果在会话保护持续时间内，Link hello邻接关系没有恢复，则删除Targeted hello邻接关系，对应的LDP会话也将被删除。如果未指定会话保护持续时间，则永远不会删除Targeted hello邻接关系。

【举例】

\# 配置保护本端与LSR ID为3.3.3.3的对等体之间的LDP会话，会话保护持续时间为120秒。

\<Sysname\> system-view

Sysname ip prefix-list protected-peer-list index 1 permit 3.3.3.3 32

Sysname mpls ldp

Sysname-ldp session protection duration 120 peer protected-peer-list

【相关命令】

·**display mpls ldp peer**

**LDP \-- LDP IPv4配置命令 \-- targeted-peer**

------------------------------------------------------------------------

**[targeted-peer**]命令用来配置主动向指定对等体发送IPv4 Targeted hello消息来建立LDP会话，允许应答指定对等体的Targeted hello消息，并进入LDP对等体视图。

**[undo targeted-peer**]命令用来取消向指定对等体发送IPv4 Targeted hello消息。

【命令】

**[targeted-peer** *ip-address*]

**[undo targeted-peer** *ip-address*]

【缺省情况】

设备不会主动向对等体发送IPv4 Targeted hello消息，也不会应答对等体的IPv4 Targeted hello消息。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：对等体的IPv4地址。

【使用指导】

·使用**targeted-peer** *ip-address*命令配置指定目的IPv4地址的对等体时，如果不配置传输地址，LDP默认会使用LSR ID作为传输地址，发送IPv4 Targeted hello消息。

·若要成功建立IPv4 Targeted hello邻接关系，需保证对等体两端配置的一致性，即在本端使用**targeted-peer** *ip-address*命令配置的目的地址需为对端在对等体视图下配置的传输地址，并保证本端传输地址与目的地址之间路由可达。

·配置了LDP会话保护、LDP over MPLS TE、MPLS L2VPN LDP PW或VPLS LDP PW后，LDP自动向指定对等体发送Targeted hello消息来建立LDP会话，如果要修改Targeted hello或KeepAlive的保持时间及发送时间间隔，必须使用**targeted-peer**命令创建对等体，并在LDP对等体视图下进行配置。

【举例】

\# 配置向对等体3.3.3.3发送IPv4 Targeted hello消息，并进入LDP对等体视图。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp targeted-peer 3.3.3.3

Sysname-ldp-peer-3.3.3.3

【相关命令】

·**display mpls ldp discovery**

·**display mpls ldp peer**

**LDP \-- LDP IPv6配置命令 \-- ipv6 accept-label**

------------------------------------------------------------------------

**[ipv6 accept-label**]命令用来配置标签接受控制策略。

**[undo ipv6 accept-label**]命令用来取消标签接受控制策略。

【命令】

**[ipv6 accept-label peer** *peer-lsr-id* **prefix-list** *prefix-list-name*]

**[undo ipv6 accept-label peer ***peer-lsr-id*]

【缺省情况】

未配置标签接受控制策略，接受来自所有对等体的所有IPv6地址前缀的标签映射。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer ***peer-lsr-id*]：指定LDP对等体。*peer-lsr-id*为LDP对等体的LSR ID。

**[prefix-list*** prefix-list-name*]：指定用来对收到的IPv6地址前缀标签映射进行过滤的IPv6地址前缀列表。*prefix-list-name*表示IPv6地址前缀列表名，为1～63个字符的字符串，区分大小写。

【使用指导】

标签接受控制策略用来对来自特定对等体的标签映射进行过滤。对于来自指定对等体的标签映射，只有标签映射中FEC的IPv6地址前缀通过指定IPv6地址前缀列表的过滤时，LSR才接受该标签映射，否则LSR不会接受且不会保存该标签映射。

当LSR接收到的标签映射数量较大时，可以配置标签接受控制策略，有选择地接受来自特定对等体的标签映射，减少LSR接受的标签映射数量，降低设备内存等资源的消耗。

需要注意的是：

·当LSR上配置的标签接受控制策略发生变化，使得LSR可以接受来自特定对等体的、以前被拒绝的标签映射时（如执行**undo ipv6 accept-label**命令删除标签接受控制策略，或者将IPv6地址前缀列表的过滤条件修改得更宽松时），只有执行**reset mpls ldp**命令重建与特定对等体的LDP会话，触发指定对等体重新通告标签映射，LSR才能获取之前拒绝的标签映射。

·在下游LSR上配置标签通告控制策略与在上游LSR上配置标签接受控制策略具有相同的效果。如果下游LSR支持配置标签通告控制策略，则推荐使用标签通告控制策略，以减轻网络负担。

【举例】

\# 对于LSR ID为1.1.1.9的LDP对等体通告的标签映射，允许地址前缀为2001:D00::/32，前缀长度大于等于32位的IPv6地址的标签映射。

\<Sysname\> system-view

Sysname ipv6 prefix-list prefix-from-RTA permit 2001:D00:: 32 less-equal 128

Sysname mpls ldp

Sysname-ldp ipv6 accept-label peer 1.1.1.9 prefix-list prefix-from-RTA

【相关命令】

·**display mpls ldp peer verbose**

·**ip****v6 prefix-list**（三层技术-IP路由命令参考/路由策略）

**LDP \-- LDP IPv6配置命令 \-- ipv6 advertise-label**

------------------------------------------------------------------------

**[ipv6 advertise-label**]命令用来配置标签通告控制策略。

**[undo ipv6 advertise-label**]命令用来取消标签通告控制策略。

【命令】

**[ipv6 advertise-label prefix-list ***prefix-list-name* [ **peer** *peer-prefix-list-name* ]]

**[undo ipv6 advertise-label prefix-list ***prefix-list-name*]

【缺省情况】

未配置标签通告控制策略，即向所有对等体通告满足LSP触发策略的所有IPv6地址前缀的标签映射。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[prefix-list*** prefix-list-name*]：指定用来对将要通告的标签映射进行过滤的IPv6地址前缀列表。*prefix-list-name*表示IPv6地址前缀列表名，为1～63个字符的字符串，区分大小写。

**[peer ***peer-prefix-list-name*]：指定用来对LDP对等体进行过滤的IPv6地址前缀列表。*peer-prefix-list-name*表示IPv6地址前缀列表名，为1～63个字符的字符串，区分大小写。如果不指定本参数，则表示向所有对等体通告标签映射。

【使用指导】

标签通告控制策略用来实现对本地LSR向对等体通告的标签映射进行过滤。

多次执行本命令，可以配置多条标签通告控制策略。

LSR按照下面的规则来判断是否向特定对等体通告标签：

·如果待通告的标签映射的IPv6地址前缀没有通过IPv6地址前缀列表的检查（没有匹配任何一条**permit**规则或匹配了**deny**规则），则不向任何对等体通告该标签映射。

·如果待通告的标签映射的IPv6地址前缀通过某个IPv6地址前缀列表的检查，且对应标签通告控制策略中的对等体IPv6地址前缀列表为空（只配置**ipv6 advertise-labelprefix-list ***prefix-list-name，*没有指定**peer ***peer-prefix-list-name*），则向所有对等体通告该标签映射。

·如果待通告的标签映射的IPv6地址前缀通过某个IPv6地址前缀列表的检查，且对应标签通告控制策略中指定了对等体IPv6地址前缀列表，则只向通过对等体IPv6地址前缀列表检查的对等体通告该标签映射。

·如果待通告的标签映射的IPv6地址前缀通过多于一个IPv6地址前缀列表的检查（多次执行**ipv6advertise-label**命令配置多条标签通告控制策略），则以配置的第一条命令为准。

在下游LSR上配置标签通告控制策略与在上游LSR上配置标签接受控制策略具有相同的效果。如果下游LSR支持配置标签通告控制策略，则推荐使用标签通告控制策略，以减轻网络负担。

【举例】

\# 配置标签通告控制策略：向LSR ID为3.3.3.9的对等体通告网段地址2001::1/64对应的标签映射；向LSR ID为4.4.4.9的对等体通告网段地址3001::1/64对应的标签映射；不通告其他网段地址对应的标签映射。

\<Sysname\> system-view

Sysname ipv6 prefix-list prefix-to-C permit 2001::1 64

Sysname ipv6 prefix-list prefix-to-D permit 3001::1 64

Sysname ip prefix-list peer-C permit 3.3.3.9 32

Sysname ip prefix-list peer-D permit 4.4.4.9 32

Sysname mpls ldp

Sysname-ldp ipv6 advertise-label prefix-list prefix-to-C peer peer-C

Sysname-ldp ipv6 advertise-label prefix-list prefix-to-D peer peer-D

【相关命令】

·**display mpls ldp fec**

·**ip****v6 prefix-list**（三层技术-IP路由命令参考/路由策略）

·**ipv6 lsp-trigger**

**LDP \-- LDP IPv6配置命令 \-- ipv6 lsp-trigger**

------------------------------------------------------------------------

**[ipv6 lsp-trigger**]命令用来配置IPv6 FEC的LSP触发策略。

**[undo ipv6 lsp-trigger**]命令用来恢复缺省情况。

【命令】

**[ipv6 lsp-trigger **[[ **all** \| **prefix-list** *prefix-list-name* }]]

**[undo ipv6 lsp-trigger **]

【缺省情况】]

只有引入到LDP的128位掩码的IPv6主机路由能够触发建立LSP。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有引入到LDP的IPv6路由表项都会触发LDP建立LSP。

**[prefix-list*** prefix-list-name*]：利用IPv6地址前缀列表对引入到LDP的路由表项进行过滤，通过IPv6地址前缀列表过滤的路由表项可以触发建立LSP，被IPv6地址前缀列表拒绝的路由表项不触发建立LSP。*prefix-list-name*表示IPv6地址前缀列表名，为1～63个字符的字符串，区分大小写。

【使用指导】

LSP触发策略用来控制引入到LDP中的哪些路由可以建立LDP LSP。

缺省情况下，LSP的触发策略与标签分发控制方式有关：

·有序方式下：只有128位掩码的本地Loopback接口IPv6地址路由和已经收到下游通告的标签映射且掩码为128位的路由可以触发建立LDP LSP。

·独立方式下：只要是128位掩码的路由都会触发建立LDP LSP。

配置触发策略后，引入到LDP中的所有路由或通过IPv6地址前缀列表的路由都会触发建立LDP LSP，独立和有序标签分发控制方式的处理没有差别。

建议用户使用缺省的LSP触发策略。

【举例】

\# 配置公网LDP实例中只有路由2001::1/ 64能够触发建立LDP LSP。

\<Sysname\> system-view

Sysname ipv6 prefix-list egress-fec-list permit 2001::1 64

Sysname mpls ldp

Sysname-ldp ipv6 lsp-trigger prefix-list egress-fec-list

【相关命令】

·**ipv6 import bgp**

·**ip****v6prefix-list**（三层技术-IP路由命令参考/路由策略）

**LDP \-- LDP IPv6配置命令 \-- ipv6 import bgp**

------------------------------------------------------------------------

**[ipv6 import bgp**]命令用来配置LDP引入BGP IPv6单播路由。

**[undo ipv6 import bgp**]命令用来恢复缺省情况。

【命令】

**[ipv6 import bgp**]

**[undo ipv6 import bgp**]

【缺省情况】

LDP 不主动引入BGP IPv6单播路由。

【视图】

LDP视图/LDP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，LDP自动引入IPv6 IGP路由（包括已引入到IGP的BGP IPv6单播路由），并为通过LSP触发策略的IGP路由和通过LSP触发策略的带标签BGP路由分配标签，但不自动引入未被引入到IGP的BGP IPv6单播路由。这就导致了在一些特殊的组网环境下，如在运营商的运营商组网中，如果一级运营商的PE与二级运营商CE之间未配置OSPF、IS-IS等IGP协议，则无法通过LDP为BGP IPv6单播路由分配标签，因而无法建立LDP LSP。有关运营商的运营商组网的详细信息，请参见"MPLS配置指导"中的"MPLS L3VPN"。

通过配置LDP引入BGP IPv6单播路由，可将BGP IPv6单播路由强制引入至LDP，如果该路由通过LSP触发策略，则为其分配标签建立LSP。

配置此命令后，可能会导致LDP引入大量的BGP IPv6单播路由，占用设备的标签、内存资源等问题，建议仅在必要时使用此命令。

【举例】

\# 配置公网LDP实例中，强制引入BGP IPv6单播路由，触发建立LDP LSP。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp ipv6 import bgp

【相关命令】

·**ipv6 lsp-trigger**

**LDP \-- LDP IPv6配置命令 \-- mpls ldp ipv6 enable**

------------------------------------------------------------------------

**[mpls ldp ipv6** **enable**]命令用来使能接口的LDP支持IPv6能力。

**[undo mpls ldp ipv6 enable**]命令用来关闭接口的LDP支持IPv6能力。

【命令】

**[mpls ldp ipv6** **enable**]

**[undo mpls ldp ipv6** **enable**]

【缺省情况】

未使能接口的LDP支持IPv6能力。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果在接口上使能了MPLS能力和LDP支持IPv6能力，且该接口处于up状态，则LDP会在该接口上启动基本发现机制，通过该接口发送Link hello消息，hello消息源地址以及携带的TCP传输地址的地址类型为IPv6地址。

需要注意的是：

·如果接口上仅使能了LDP支持IPv6能力，则必须使用**mpls ldp transport-address**命令配置LDP传输地址后，才会发送IPv6 hello消息。

·执行本命令前，需要先在系统视图下执行**mpls ldp**命令全局使能LSR的LDP能力。

·如果接口已与某个VPN实例绑定，则需要通过**vpn-instance**命令使能此VPN实例的LDP能力。

·同一接口上既可以通过配置**mpls ldp enable**使能LDP支持IPv4能力，也可以通过配置**mpls ldp ipv6 enable**使能LDP支持IPv6能力。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使能LDP支持IPv6能力。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls ldp ipv6 enable

·交换应用

\# 在接口Vlan-interface2上使能支持IPv6能力。

\<Sysname\> system-view

Sysname mpls ldp

Sysname-ldp quit

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 mpls ldp ipv6 enable

【相关命令】

·**display mpls ldp interface**

·**mpls enable**（MPLS命令参考/MPLS基本配置）

·**mpls ldp**

·**mpls ldp**** enable**

**LDP \-- LDP IPv6配置命令 \-- mpls ldp transport-address**

------------------------------------------------------------------------

**[mpls ldp transport-address**]命令用来配置LDP传输地址。

**[undo mpls ldp transport-address**]命令用来恢复缺省情况。

【命令】

接口视图下：

**[mpls ldp transport-address** *ipv6-address*]

**[undo mpls ldp transport-address ***ipv6-address*]

LDP对等体视图下：

**[mpls ldp transport-address** *ipv6-address* ]

**[undo mpls ldp transport-address**]

【缺省情况】

未配置LDP IPv6传输地址。

【视图】

接口视图/LDP对等体视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：LDP使用此地址作为LDP传输地址。

【使用指导】

LSR在Link hello消息或Targeted hello消息中携带传输地址，将本端的传输地址通知给对端。

【举例】

\# 配置与对等体建立TCP连接时采用的LDP传输地址为2002：：1。

\<Sysname\> System-view

Sysname mpls ldp

Sysname-ldp targeted-peer 2001::1

Sysname-ldp-peer-2001::1 mpls ldp transport-address 2002::1

【相关命令】

·**display mpls ldp discovery**

·**targeted-peer**

**LDP \-- LDP IPv6配置命令 \-- targeted-peer**

------------------------------------------------------------------------

**[targeted-peer**]命令用来配置主动向指定对等体的IPv6地址发送Targeted hello消息来建立LDP会话，允许应答指定对等体的Targeted hello消息，并进入LDP对等体视图。

**[undo targeted-peer**]命令用来取消向指定对等体的IPv6地址发送Targeted hello消息。

【命令】

**[targeted-peer** *ipv6-address*]

**[undo targeted-peer*** ipv6-address*]

【缺省情况】

设备不会主动向对等体发送Targeted hello消息，也不会应答对等体的Targeted hello消息。

【视图】

LDP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定对等体的IPv6地址。

【使用指导】

·通过**targeted-peer*** ipv6-address*命令指定LDP IPv6对等体，并进入对等体视图后，必须在该视图下配置IPv6传输地址，LDP才会发送IPv6 Targeted hello消息。

·若要保证建立IPv6 Targeted hello邻接关系，需保证对等体两端配置的一致性，即在本端使用**targeted-peer*** ipv6-address*命令配置的目的地址需为对端在对等体视图下配置的传输地址，并保证本端传输地址与目的地址之间路由可达。

【举例】

\# 配置向对等体的指定地址2001::1发送Targeted hello消息，并进入LDP对等体视图*。*

*[\<*Sysname\> system-view]

Sysname mpls ldp

Sysname-ldp targeted-peer 2001::1

Sysname-ldp-peer-2001::1

【相关命令】

·**display mpls ldp discovery**

·**display mpls ldp peer**
