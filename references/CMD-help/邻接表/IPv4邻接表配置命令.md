<!-- CMD-INDEX
  display adjacent-table              | 任意视图             | L6
  display ipv6 adjacent-table         | 任意视图             | L176
-->

**邻接表 \-- IPv4邻接表配置命令 \-- display adjacent-table**

------------------------------------------------------------------------

**[display adjacent-table**]命令用来显示IPv4邻接表项的信息。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[display adjacent-table **[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **slot** *slot-number* [ **cpu** *cpu-number* ] } [ **count** \| **verbose** ]]]

分布式设备－IRF模式：

**[display adjacent-table **[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] } [ **count** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有的IPv4邻接表项的信息。

**[physical-interface** *interface-type interface-number*]：显示指定物理接口上的IPv4邻接表项的信息。

**[routing-interface** *interface-type interface-number*]：显示指定路由接口上的IPv4邻接表项的信息。

**[slot** *slot-number*]：显示指定单板的IPv4邻接表项的信息。*slot-number*表示单板所在的槽位号，只能为0。（集中式设备）

**[slot ***slot-number*]：显示指定单板的IPv4邻接表项的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv4邻接表项的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的IPv4邻接表项的信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv4邻接表项的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的IPv4邻接表项的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv4邻接表项的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv4邻接表项的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv4邻接表项的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv4邻接表项的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv4邻接表项的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的IPv4邻接表项的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[count**]：显示IPv4邻接表项的数目。

**[verbose**]：显示IPv4邻接表项的详细信息。

【举例】

\# 显示所有IPv4邻接表项的详细信息。

\<Sysname\> display adjacent-table all verbose

 IP address                     : 0.0.0.0

 Routing interface             : Pos2/2/0

Physical interface            : Pos2/2/0

 Logical interface             : N/A

Service type                   : PPP

 Action type                    : Forwarding

Link media type                : P2P

 Slot                             : 1

 Cpu                              : 0

VPN index                       : 0

Virtual circuit information : N/A

 Link head information(IP)    : ff030021

 Link head information(MPLS) : ff030281

\# 显示1号单板的IPv4邻接表项的信息。

\<Sysname\> display adjacent-table slot 1

IP address       Routing interface     Physical interface    Type

0.0.0.0          Pos2/2/0                 Pos2/2/0                PPP

\# 显示1号单板的IPv4邻接表项的数目。

\<Sysname\> display adjacent-table slot 1 count

 Total entries on slot 1: 1

以上显示信息表示1号单板的IPv4邻接表项的数目为1。

表1-1 display adjacent-table命令显示信息描述表

字段

描述

IP address

报文转发下一跳的IP地址（对于P2P链路，不需要下一跳IP地址信息，本字段的值填为0.0.0.0；对于NBMA链路，取值0.0.0.0表示缺省邻接表，从缺省虚链路转发）

Routing interface

路由出接口

Physical interface

路由出接口对应的实际发送报文的物理接口

Logical interface

发送报文的逻辑接口（如果没有此信息，则显示为N/A）

Service type/Type

链路层协议类型，如PPP、HDLC、Tunnel、MTunnel等

Action type

报文处理类型：

·Forwarding：表示转发

·Drop：表示丢弃

Link media type

链路介质类型：

·P2P：表示点到点链路

·NBMA：表示点对多点链路

Slot

单板所在的槽位号

Cpu

CPU编号

VPN index

VPN索引

Virtual circuit information

虚链路信息，如PVC、DLCI等（如果没有此信息，则显示为N/A）

Link head information(IP)

IPv4协议对应的链路层头信息

Link head information(MPLS)

MPLS协议对应的链路层头信息

**邻接表 \-- IPv6邻接表配置命令 \-- display ipv6 adjacent-table**

------------------------------------------------------------------------

![说明](邻接表命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ipv6 adjacent-table**]命令用来显示IPv6邻接表项的信息。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[display ipv6 adjacent-table **[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **slot** *slot-number* [ **cpu** *cpu-number* ] } [ **count** \| **verbose** ]]]

分布式设备－IRF模式：

**[display ipv6 adjacent-table **[{ **all** \| **physical-interface** *interface-type interface-number* \| **routing-interface** *interface-type interface-number* \| **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] } [ **count** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有的IPv6邻接表项的信息。

**[physical-interface** *interface-type interface-number*]：显示指定物理接口上的IPv6邻接表项的信息。

**[routing-interface** *interface-type interface-number*]：显示指定路由接口上的IPv6邻接表项的信息。

**[slot** *slot-number*]：显示指定单板的IPv6邻接表项的信息。*slot-number*表示单板所在的槽位号，只能为0。（集中式设备）

**[slot ***slot-number*]：显示指定单板的IPv6邻接表项的信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6邻接表项的信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的IPv6邻接表项的信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6邻接表项的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的IPv6邻接表项的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6邻接表项的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6邻接表项的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6邻接表项的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6邻接表项的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6邻接表项的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的IPv6邻接表项的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[count**]：显示IPv6邻接表项的数目。

**[verbose**]：显示IPv6邻接表项的详细信息。

【举例】

\# 显示所有IPv6邻接表项的详细信息。

\<Sysname\> display ipv6 adjacent-table all verbose

 IPv6 address                    : N/A

 Routing interface              : Pos2/2/0

 Physical interface             : Pos2/2/0

 Logical interface              : N/A

 Service type                    : PPP

 Action type                     : Forwarding

 Link media type                : P2P

 Slot                             : 0

 VPN index                       : 0

 Virtual circuit information : N/A

 Link head information(IPv6) : ff030057

\# 显示1号单板的IPv6邻接表项的信息。

\<Sysname\> display ipv6 adjacent-table slot 1

IPv6 address          Routing interface     Physical interface    Type

N/A                     Pos2/2/0                Pos2/2/0                PPP

\# 显示1号单板的IPv6邻接表项的数目。

\<Sysname\> display ipv6 adjacent-table slot 1 count

 Total entries on slot 1: 1

以上显示信息表示1号单板的IPv6邻接表项的数目为1。

表1-2 display ipv6 adjacent-table命令显示信息描述表

字段

描述

IPv6 address

报文转发下一跳的IPv6地址（对于P2P链路，不需要下一跳IPv6地址信息，本字段的值填为0::0，显示为N/A；对于NBMA链路，取值0::0表示缺省邻接表，从缺省虚链路转发）

Routing interface

路由出接口

Physical interface

路由出接口对应的实际发送报文的物理接口

Logical interface

发送报文的逻辑接口（如果没有此信息，则显示为N/A）

Service type/Type

链路层协议类型，如PPP、HDLC、Tunnel、MTunnel等

Action type

报文处理类型：

·Forwarding：表示转发

·Drop：表示丢弃

Link media type

链路介质类型：

·P2P：表示点到点链路

·NBMA：表示点对多点链路

Slot

单板所在的槽位号

Cpu

CPU编号

VPN index

VPN索引

Virtual circuit information

虚链路信息，如PVC、DLCI等（如果没有此信息，则显示为N/A）

Link head information(IPv6)

IPv6协议对应的链路层头信息

