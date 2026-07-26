
**L2PT \-- L2PT配置命令 \-- display l2protocol statistics**

------------------------------------------------------------------------

**[display l2protocol statistics**]命令用来显示L2PT报文统计信息。

【命令】

**[display l2protocol statistics ** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**] *interface-type* *interface-number*：显示指定二层以太网接口或二层聚合接口上的L2PT报文统计信息。*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，将显示所有二层以太网接和二层聚合接口的L2PT报文统计信息。

【举例】

\# 显示所有二层以太网接口和二层聚合接口的L2PT报文统计信息。

\<Sysname\> display l2protocol statistics

L2PT statistics information on interface Bridge-Aggregation1:

Protocol  Encapsulated      Decapsulated      Forwarded         Dropped

CDP       0                 0                 0                 0

DLDP      0                 3                 0                 0

EOAM      0                 2                 0                 0

GVRP      8                 4                 9                 2

LACP      0                 0                 0                 0

LLDP      0                 3                 0                 0

MVRP      0                 0                 0                 0

PAGP      0                 1                 0                 0

PVST      0                 0                 0                 0

STP       5                 5                 5                 0

Tunnel    N/A               N/A               100               10

VTP       0                 6                 0                 0

L2PT statistics information on interface GigabitEthernet1/0/1:

Protocol  Encapsulated      Decapsulated      Forwarded         Dropped

CDP       0                 0                 0                 0

DLDP      2                 3                 3                 0

EOAM      5                 2                 9                 0

GVRP      8                 4                 9                 2

LACP      0                 0                 0                 0

LLDP      3                 3                 3                 3

MVRP      0                 0                 0                 0

PAGP      5                 1                 7                 3

PVST      0                 0                 0                 0

STP       5                 5                 5                 0

Tunnel    N/A               N/A               100               10

VTP       0                 6                 0                 0

表1-1 display l2protocol statistics命令显示信息描述表

字段

描述

Protocol

协议类型

Encapsulated

封装统计计数

用户侧收到协议报文后封装成BPDU Tunnel报文，对应的协议封装统计计数加1

对于Tunnel（表示BPDU Tunnel报文），对应值显示为N/A，为无效统计计数

Decapsulated

解封装统计计数

网络侧收到BPDU Tunnel报文后解封装成协议报文，对应的协议解封装统计计数加1

对于Tunnel，对应值显示为N/A，为无效统计计数

Forwarded

转发统计计数

·用户侧或网络侧收到协议报文后转发，对应的协议转发统计计数加1

·网络侧收到BPDU Tunnel报文后转发，对应的Tunnel转发统计计数加1（如果网络侧收到BPDU Tunnel报文时，设备没有任何用户侧端口，则Tunnel转发统计计数不会增加）

Dropped

丢弃统计计数

·接口收到协议报文后丢弃，对应的协议丢弃统计计数加1（如果协议报文被硬件丢弃，则协议丢弃统计计数不会增加）

·接口收到BPDU Tunnel报文后丢弃，对应的Tunnel丢弃统计计数加1

**L2PT \-- L2PT配置命令 \-- l2protocol drop**

------------------------------------------------------------------------

**[l2protocol drop**]命令用来使能指定协议的L2PT Drop功能，即强制丢弃指定的协议报文。

**[undo l2protocol drop**]命令用来关闭指定协议的L2PT Drop功能。

【命令】

在二层以太网接口视图下：

**[l2protocol ** { **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **drop**]

**[undo l2protocol ** { **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **drop**]

在二层聚合接口视图下：

**[l2protocol** { **gvrp** \| **lldp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **drop**]

**[undo l2protocol** { **gvrp** \| **lldp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **drop**]

【缺省情况】

各协议的L2PT Drop功能均处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cdp**]：表示CDP协议。

**[dldp**]：表示DLDP协议。

**[eoam**]：表示EOAM协议。

**[gvrp**]：表示GVRP协议。

**[mvrp**]：表示MVRP协议。

**[lacp**]：表示LACP协议。

**[lldp**]：表示LLDP协议。

**[pagp**]：表示PAGP协议。

**[pvst**]：表示PVST协议。

**[stp**]：表示STP协议。

**[vtp**]：表示VTP协议。

【使用指导】

·允许在二层聚合组的成员端口上使能GVRP、MVRP、PVST、STP和VTP协议的L2PT Drop功能，但配置不生效。在二层聚合组的成员端口上使能CDP、DLDP、EOAM、LACP、LLDP和PAGP协议的L2PT Drop功能会生效。

·L2PT Drop功能的优先级高于协议报文的处理优先级，因此，在接口上使能指定协议的L2PT Drop功能时，不需要在当前接口关闭该协议。

·对于LLDP协议，L2PT Drop功能支持所有的LLDP报文，包括Nearest Bridge（最近桥代理）、Nearest Customer Bridge（最近客户桥代理）、Nearest non-TPMR Bridge（最近非TPMR桥代理）类型的LLDP报文。

·**l2protocol drop**与**l2protocol tunnel dot1q**命令会相互覆盖。

【举例】

\# 在接口GigabitEthernet1/0/1上使能STP协议的L2PT Drop功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 l2protocol stp drop

\# 在二层聚合接口Bridge-Aggregation1上使能STP协议的L2PT Drop功能。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 l2protocol stp drop

【相关命令】

·**l2protocol tunnel dot1q**

**L2PT \-- L2PT配置命令 \-- l2protocol tunnel dot1q**

------------------------------------------------------------------------

**[l2protocol**]** tunnel dot1q**命令用来使能指定协议的L2PT功能。

**[undo **]**l2protocol tunnel dot1q**命令用来关闭指定协议的L2PT功能。

【命令】

在二层以太网接口视图下：

**[l2protocol ** { **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]

**[undo l2protocol ** { **cdp** \| **dldp** \| **eoam** \| **gvrp** \| **lacp** \| **lldp** \| **mvrp** \| **pagp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]

在二层聚合接口视图下：

**[l2protocol ** { **gvrp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]

**[undo l2protocol**]****[{ **gvrp** \| **mvrp** \| **pvst** \| **stp** \| **vtp** } **tunnel dot1q**]

【缺省情况】

各协议的L2PT功能均处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cdp**]：表示CDP协议。

**[dldp**]：表示DLDP协议。

**[eoam**]：表示EOAM协议。

**[gvrp**]：表示GVRP协议。

**[lacp**]：表示LACP协议。

**[lldp**]：表示LLDP协议。

**[mvrp**]：表示MVRP协议。

**[pagp**]：表示PAGP协议。

**[pvst**]：表示PVST协议。

**[stp**]：表示STP协议。

**[vtp**]：表示VTP协议。

【使用指导】

·不支持在二层聚合接口上使能CDP、DLDP、EOAM、LACP、LLDP、PAGP协议的L2PT功能。

·在接口上使能某协议的L2PT功能时，对应的CE上应启用该协议，同时当前接口必须关闭该协议。

·允许在二层聚合组的成员端口上使能L2PT功能，但配置不生效。

·不能在业务环回组的成员端口上使能L2PT功能。

·对于LLDP协议，L2PT功能只支持Nearest Bridge（最近桥代理）类型的LLDP报文。

·**l2protocol tunnel dot1q**与**l2protocol drop**命令会相互覆盖。

【举例】

\# 在接口GigabitEthernet1/0/1上关闭STP协议，并使能STP协议的L2PT功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo stp enable

Sysname-GigabitEthernet1/0/1 l2protocol stp tunnel dot1q

\# 在二层聚合接口Bridge-Aggregation1上关闭STP协议，并使能STP协议的L2PT功能。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 undo stp enable

Sysname-Bridge-Aggregation1 l2protocol stp tunnel dot1q

【相关命令】

·**l2protocol drop**

**L2PT \-- L2PT配置命令 \-- l2protocol tunnel-dmac**

------------------------------------------------------------------------

**[l2protocol tunnel-dmac**]命令用来配置BPDU Tunnel报文的组播目的MAC地址。

**[undo l2protocol tunnel-dmac**]命令用来恢复缺省情况。

【命令】

**[l2protocol tunnel-dmac ***mac-address*]

**[undo l2protocol tunnel-dmac**]

【缺省情况】

BPDU Tunnel报文的组播目的MAC地址为010F-E200-0003。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac*]-*address*：BPDU Tunnel报文的组播目的MAC地址。取值可以为下列MAC地址之一：0100-0CCD-CDD0、0100-0CCD-CDD1、0100-0CCD-CDD2或010F-E200-0003。

【举例】

\# 配置BPDU Tunnel报文的组播目的MAC地址为0100-0CCD-CDD0。

\<Sysname\> system-view

Sysname l2protocol tunnel-dmac 0100-0ccd-cdd0

**L2PT \-- L2PT配置命令 \-- reset l2protocol statistics**

------------------------------------------------------------------------

**[reset l2protocol statistics**]命令用来清除L2PT报文的统计信息。

【命令】

**[reset l2protocol statistics ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**] *interface-type* *interface-number*：清除指定二层以太网接口或二层聚合接口上的L2PT报文统计信息。*interface-type* *interface-number*表示接口类型和接口编号。如未指定本参数，将清除所有二层以太网接口和二层聚合接口的L2PT报文统计信息。

【举例】

\# 清除所有二层以太网接口和二层聚合接口的L2PT报文统计信息。

\<Sysname\> reset l2protocol statistics

