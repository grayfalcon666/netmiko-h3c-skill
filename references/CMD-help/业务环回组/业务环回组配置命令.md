<!-- CMD-INDEX
  display service-loopback group      | 任意视图             | L7
  port service-loopback group         | 二层以太网接口视图        | L71
  service-loopback group              | 系统视图             | L125
-->

**业务环回组 \-- 业务环回组配置命令 \-- display service-loopback group**

------------------------------------------------------------------------

**[display service-loopback group**]命令用来显示业务环回组的信息。

【命令】

**[display service-loopback group ** *number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number*]：显示指定业务环回组的信息。*number*为业务环回组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，将显示所有业务环回组的信息。

【举例】

\# 显示业务环回组5的信息。

\<Sysname\> display service-loopback group 5

Service Group ID: 5       Service Type: Tunnel

Member:

 GigabitEthernet1/0/1

 GigabitEthernet1/0/2

表1-1 display service-loopback group命令显示信息描述表

字段

描述

Service Group ID

业务环回组的编号

Service Type

业务环回组的业务类型：

·Multicast-tunnel：表示组播隧道业务类型

·Tunnel：表示单播隧道业务类型

Member

业务环回组的成员端口

**业务环回组 \-- 业务环回组配置命令 \-- port service-loopback group**

------------------------------------------------------------------------

**[port service-loopback group**]命令用来将端口加入指定的业务环回组。

**[undo port service-loopback group**]命令用来将端口从业务环回组中删除。

【命令】

**[port service-loopback group*** number*]

**[undo** **port** **service-loopback group**]

【缺省情况】

端口不属于任何业务环回组。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：指定业务环回组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·在将端口加入业务环回组时，该端口上已存在的所有配置都将被清除。

·一个端口只允许加入一个业务环回组，且必须支持该业务环回组的业务类型。

·通过在不同端口上执行本命令，可以将多个端口加入到业务环回组中。

·如果端口是一个已被引用的业务环回组中唯一的成员端口，那么该端口退出该业务环回组将导致单播隧道或组播隧道尚未down时就发生流量中断。

·如果端口不属于任何业务环回组，则在该端口上不能执行**undo port service-loopback group**命令。

【举例】

\# 将端口GigabitEthernet1/0/1加入业务环回组5中。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port service-loopback group 5

**业务环回组 \-- 业务环回组配置命令 \-- service-loopback group**

------------------------------------------------------------------------

**[service-loopback group**]命令用来创建业务环回组，并指定其业务类型。

**[undo** **service-loopback group**]命令用来删除业务环回组。

【命令】

**[service-loopback group**[ *number* **type** { **multicast-tunnel** \| **tunnel** } \*]]

**[undo service-loopback group ***number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：指定业务环回组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[type**]：指定业务环回组的业务类型。

**[multicast-tunnel**]：指定业务类型为Multicast tunnel（组播隧道）类型。

**[tunnel**]：指定业务类型为Tunnel（单播隧道）类型。

【使用指导】

·业务环回组只有在被其他特性引用后才能处理业务。业务环回组一旦创建即可被引用，且一个业务环回组可以同时被多个特性引用。

·每种业务类型的业务环回组在全局只能有一个。

·业务环回组创建后不允许再更改其业务类型。

·不建议删除已被其他特性引用的业务环回组。

【举例】

\# 创建业务环回组5，并指定其业务类型为Tunnel类型。

\<Sysname\> system-view

Sysname service-loopback group 5 type tunnel
