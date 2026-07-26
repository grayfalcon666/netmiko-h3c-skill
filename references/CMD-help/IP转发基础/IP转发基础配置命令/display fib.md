
**IP转发基础 \-- IP转发基础配置命令 \-- display fib**

------------------------------------------------------------------------

**[display fib**]命令用来显示FIB表项的信息。

【命令】

**[display**[ **fib** [ **topology** *topo-name* \| **vpn-instance** *vpn-instance-name*   *ip-address* [ *mask \| mask-length* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[topology** *topo-name*]：显示指定拓扑的FIB表项的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；取值为**base**时表示公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的FIB表项的信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定VPN实例，则显示公网的FIB表项的信息。

*[ip-address*]：显示与指定目的IP地址匹配的FIB表项的信息。

*[mask*]：IP地址掩码。

*[mask-length*]：IP地址掩码长度，即掩码中连续"1"的个数，取值范围为0～32。

【使用指导】

**[display fib**]命令用来显示FIB表项的信息，包括目的地址/掩码长度、转发的下一跳地址、转发接口等内容。

需要注意的是：

·如果配置*ip-address*时不指定掩码和掩码长度，则显示与指定目的IP地址最长匹配的FIB表项的信息；

·如果配置*ip-address*时指定了掩码或掩码长度，则显示与指定目的IP地址和掩码精确匹配的FIB表项的信息。

【举例】

\# 显示指定拓扑的FIB表项的信息。

\<Sysname\>display fib topology mt

Destination count: 8 FIB entry count: 8

Flag:

  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static

  R:Relay     F:FRR

Destination/Mask   Nexthop         Flag     OutInterface/Token       Label

0.0.0.0/32         127.0.0.1       UH       InLoop0                  Null

127.0.0.0/8        127.0.0.1       U        InLoop0                  Null

127.0.0.0/32       127.0.0.1       UH       InLoop0                  Null

127.0.0.1/32       127.0.0.1       UH       InLoop0                  Null

127.255.255.255/32 127.0.0.1       UH       InLoop0                  Null

224.0.0.0/4        0.0.0.0         UB       NULL0                    Null

224.0.0.0/24       0.0.0.0         UB       NULL0                    Null

255.255.255.255/32 127.0.0.1       UH       InLoop0                  Null

\# 显示公网的所有FIB表项的信息。

\<Sysname\> display fib

Destination count: 5 FIB entry count: 6

Flag:

  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static

  R:Relay     F:FRR

Destination/Mask   Nexthop         Flag     OutInterface/Token       Label

0.0.0.0/32         127.0.0.1       UH       InLoop0                  Null

1.1.1.0/24         192.168.126.1   USGF     M-GE0/0/0                Null

                   20.20.20.25     SGF      GE2/0/1                  Null

127.0.0.0/8        127.0.0.1       U        InLoop0                  Null

127.0.0.0/32       127.0.0.1       UH       InLoop0                  Null

127.0.0.1/32       127.0.0.1       UH       InLoop0                  Null

\#显示私网的FIB表项的信息

\<Sysname\> display fib vpn-instance vpn1

Destination count: 8 FIB entry count: 8

Flag:

  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static

  R:Relay     F:FRR

Destination/Mask   Nexthop         Flag     OutInterface/Token       Label

0.0.0.0/32         127.0.0.1       UH       InLoop0                  Null

20.20.20.0/24      20.20.20.25     U        GE2/0/1                  Null

20.20.20.0/32      20.20.20.25     UBH      GE2/0/1                  Null

20.20.20.25/32     127.0.0.1       UH       InLoop0                  Null

20.20.20.25/32     20.20.20.25     H        GE2/0/1                  Null

20.20.20.255/32    20.20.20.25     UBH      GE2/0/1                  Null

30.30.30.0/24      30.30.30.30     U        GE2/0/2                  Null

30.30.30.0/32      30.30.30.30     UBH      GE2/0/2                  Null

\# 显示目的地址为10.2.1.1的FIB表项的信息。

\<Sysname\> display fib 10.2.1.1

Destination count: 1 FIB entry count: 1

Flag:

  U:Useable   G:Gateway   H:Host   B:Blackhole   D:Dynamic   S:Static

  R:Relay     F:FRR

Destination/Mask   Nexthop         Flag     OutInterface/Token       Label

10.2.1.1/32        127.0.0.1       UH       InLoop0                  Null

表1-1 display fib命令显示信息描述表

字段

描述

Destination count

目的地址的个数

FIB entry count

FIB表项数目

Destination/Mask

目的地址/掩码长度

Nexthop

转发的下一跳地址

Flag

路由的标志：

·U：表示可用路由

·G：表示网关路由

·H：表示主机路由

·B：表示黑洞路由

·D：表示动态路由

·S：表示静态路由

·R：表示迭代路由

·F：表示快速重路由

OutInterface/Token

转发接口/LSP索引号

Label

内层标签值

**IP转发基础 \-- IP转发基础配置命令 \-- ip last-hop hold**

------------------------------------------------------------------------

![说明](IP转发基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip last-hop hold **]命令用来开启转发保持上一跳功能。

**[undo ip last-hop hold **]命令用来关闭转发保持上一跳功能。

【命令】

**[ip last-hop hold**]

**[undo ip last-hop hold**]

【缺省情况】

转发保持上一跳功能处于关闭状态。

【视图】

三层以太网接口视图/三层以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口上开启保持上一跳功能后，当正向流量的第一个IP报文从该接口发出，在高速缓存中会记录相应的流量特征以及上一跳信息，反向流量报文到达设备上进行转发时可以直接通过该上一跳信息指导报文进行转发。

保持上一跳功能依赖于快速转发表项的建立，如果上一跳的MAC地址发生变化，对应的快速转发表项需要重建才能使保持上一跳功能正常工作。

【举例】

\# 开启转发保持上一跳功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 2/0/0

Sysname-GigabitEthernet2/0/0 ip last-hop hold

**负载分担 \-- 负载分担配置命令 \-- bandwidth-based-sharing**

------------------------------------------------------------------------

![说明](IP转发基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bandwidth-based-sharing**]命令用来开启IPv4基于带宽的负载分担功能。

**[undo **]**bandwidth-based-sharing**命令用来关闭IPv4基于带宽的负载分担功能。

【命令】

**[bandwidth-based-sharing**]

**[undo **]**bandwidth-based-sharing**

【缺省情况】

IPv4基于带宽的负载分担功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启IPv4基于带宽的负载分担功能情况下，如果转发时查到多个出接口/下一跳，则按照接口的带宽值计算出各个接口应该分配的报文比例，然后按照带宽比例对报文进行转发。

支持负载分担的协议（如LISP）的设备，无论是否配置**bandwidth-based-sharing**，负载分担比例以协议定义的负载分担比例为准。

【举例】

\# 开启IPv4基于带宽的负载分担功能。

\<Sysname\> system-view

Sysname bandwidth-based-sharing

**负载分担 \-- 负载分担配置命令 \-- ip load-sharing local-first enable**

------------------------------------------------------------------------

![说明](IP转发基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip load-sharing local-first enable**]命令用来开启等价路由负载分担本地优先功能。

**[undo ip load-sharing local-first enable**]命令用来关闭等价路由负载分担本地优先功能。

【命令】

**[ip load-sharing local-first enable**]

**[undo ip load-sharing local-first enable**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启等价路由负载分担本地优先功能。

\<Sysname\> system-view

Sysname ip load-sharing local-first enable

**负载分担 \-- 负载分担配置命令 \-- ip load-sharing mode**

------------------------------------------------------------------------

![说明](IP转发基础命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ip load-sharing mode**]命令用来配置负载分担方式。

**[undo ip load-sharing mode**]命令用来恢复缺省的负载分担方式。

【命令】

集中式设备：

**[ip load-sharing mode **]*[algorithm-number*****[\|  [ **dest-ip** \| **dest-port** \| **ip-pro** \| **src-ip** \| **src-port** ] \* ] \| **per-packet** }]

**[undo ip load-sharing mode**]

分布式设备－独立运行模式/集中式IRF设备：

**[ip load-sharing mode **]*[algorithm-number*****[\|  [ **dest-ip** \| **dest-port** \| **ip-pro** \| **src-ip** \| **src-port** ] \* ] \| **per-packet** }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]

**[undo ip load-sharing mode**]**** **slot** *slot-number* \**cpu** *cpu-number*

分布式设备－IRF模式：

**[ip load-sharing mode ***algorithm-number*****[\|  [ **dest-ip** \| **dest-port** \| **ip-pro** \| **src-ip** \| **src-port** ] \* ] \| **per-packet** }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

**[undo ip load-sharing mode** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[per-flow**]：基于报文逐流进行负载分担。

**[dest-ip**]：基于报文的目的IP地址逐流进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[dest-port**]：基于报文的目的端口逐流进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ip-pro**]：基于报文的IP协议号逐流进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[src-ip**]：基于报文的源IP地址逐流进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[src-port**]：基于报文的源端口逐流进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[algorithm**]* algorithm-number*：基于报文逐流进行负载分担的算法切换。*algorithm-number*指定要进行算法切换的算法编号。范围为0\~7，当编号为0时，表示设备内的缺省算法。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[per-packet**]：基于报文逐包进行负载分担。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot**]* slot-number*：在指定单板上配置负载分担方式。*slot-number*表示单板所在的槽位号。如果未指定本参数，则在所有单板上配置负载分担方式。（分布式设备－独立运行模式）

**[slot*** slot-number*]：在指定成员设备上配置负载分担方式。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则在所有成员设备上配置负载分担方式。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：在指定成员设备/PEX上配置负载分担方式。slot-number表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则在所有成员设备/PEX上配置负载分担方式。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：在指定成员设备上指定单板上配置负载分担方式。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则在所有单板上配置负载分担方式。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：在指定单板上配置负载分担方式。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则在所有单板上配置负载分担方式。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：在指定CPU上配置负载分担方式。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 配置基于报文逐包进行负载分担。（集中式设备）

\<Sysname\> system-view

Sysname ip load-sharing mode per-packet

\# 配置2号单板基于报文逐包进行负载分担。（分布式设备－独立运行模式）

\<Sysname\> system-view

Sysname ip load-sharing mode per-packet slot 2

\# 配置2号成员设备基于报文逐包进行负载分担。（集中式IRF设备）

\<Sysname\> system-view

Sysname ip load-sharing mode per-packet slot 2

\# 配置1号成员设备2号单板基于报文逐包进行负载分担。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname ip load-sharing mode per-packet chassis 1 slot 2
