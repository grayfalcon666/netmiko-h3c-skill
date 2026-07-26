
**Monitor Link \-- Monitor Link配置命令 \-- display monitor-link group**

------------------------------------------------------------------------

**[display monitor-link group**]命令用来显示Monitor Link组的信息。

【命令】

**[display monitor-link group**[ { *group-id* \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-id*]：显示指定Monitor Link组的信息。*group-id*表示Monitor Link组的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[all**]：显示所有Monitor Link组的信息。

【使用指导】

使用本命令不会显示Monitor Link组中聚合成员端口的信息。

【举例】

\# 显示Monitor Link组1的信息。

\<Sysname\> display monitor-link group 1

Monitor link group 1 information:

  Group status     : UP

  Downlink up-delay: 0(s)

  Last-up-time     : 16:38:26 2012/4/21

  Last-down-time   : 16:37:20 2012/4/21

  Member                    Role       Status

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  GE1/0/1                   UPLINK     UP

  GE1/0/2                   DOWNLINK   UP

表1-1 display monitor-link group命令显示信息描述表

字段

描述

Monitor link group 1 information

Monitor Link组1的信息

Group status

Monitor Link组的状态：

·DOWN：故障

·UP：正常

Downlink up-delay

Monitor Link组下行接口的回切延时，单位为秒

Last-up-time

Monitor Link组最近一次up的时间

Last-down-time

Monitor Link组最近一次down的时间

Member

Monitor Link组的成员接口

Role

成员接口的角色：

·DOWNLINK：下行接口

·UPLINK：上行接口

Status

成员接口的状态：

·DOWN：故障

·UP：正常

**Monitor Link \-- Monitor Link配置命令 \-- downlink up-delay**

------------------------------------------------------------------------

**[downlink up-delay**]命令用来配置Monitor Link组下行接口的回切延时。

**[undo downlink up-delay**]命令用来恢复缺省情况。

【命令】

**[downlink up-delay ***delay*]

**[undo downlink up-delay**]

【缺省情况】

Monitor Link组下行接口的回切延时为0秒，即上行接口up后，下行接口立刻恢复为up状态。

【视图】

Monitor Link组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：表示延时时间，取值范围为1～300，单位为秒。

【使用指导】

通过延时回切机制可以避免由于Monitor Link组上行链路震荡而导致的下行链路频繁切换。其原理为：当Monitor Link组的上行接口恢复为up状态并维持了一段时间之后，下行接口才恢复为up状态，这段时间就称为Monitor Link组下行接口的回切延时。

【举例】

\# 配置Monitor Link组1下行接口的回切延时为50秒。

\<Sysname\> system-view

Sysname monitor-link group 1

Sysname-mtlk-group1 downlink up-delay 50

**Monitor Link \-- Monitor Link配置命令 \-- monitor-link group**

------------------------------------------------------------------------

**[monitor-link group**]命令用来创建Monitor Link组，并进入Monitor Link组视图。

**[undo monitor-link group**]命令用来删除Monitor Link组。

【命令】

**[monitor-link group ***group-id*]

**[undo monitor-link group ***group-id*]

【缺省情况】

不存在任何Monitor Link组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示Monitor Link组的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 创建Monitor Link组1，并进入Monitor Link组1的视图。

\<Sysname\> system-view

Sysname monitor-link group 1

Sysname-mtlk-group1

**Monitor Link \-- Monitor Link配置命令 \-- port**

------------------------------------------------------------------------

**[port**]命令用来配置Monitor Link组的成员接口。

**[undo port**]命令用来取消Monitor Link组成员接口的配置。

【命令】

**[port ***interface-type*[ { *interface-number* \| *interface-number*.*subnumber* } { **downlink** \| **uplink** }]]

**[undo port ***interface-type interface-number*]

【缺省情况】

Monitor Link组中没有成员接口。

【视图】

Monitor Link组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type*]：表示接口类型，包括二层以太网接口、三层以太网接口、三层以太网子接口、二层聚合接口、三层聚合接口、三层聚合子接口、S通道接口和S通道聚合接口。

*[interface-number*]：表示接口编号。

*[interface-number*.*subnumber*]：表示子接口的编号。其中，*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为1～4094。

**[downlink**]：表示下行接口。

**[uplink**]：表示上行接口。

【使用指导】

·如果已将一个接口的主接口配置为Monitor Link组的下行接口，请勿再将该接口的子接口配置为任何Monitor Link组的上行接口，否则将影响Monitor Link协议的正常运行。

·不允许将一个聚合接口及其所对应聚合组的成员端口加入同一个Monitor Link组中，否则将影响Monitor Link协议的正常运行。

·由于同一接口的主接口和子接口的up/down状态本身是联动的，因此请勿将它们加入同一个Monitor Link组中，否则将影响该Monitor Link组的性能。

·一个接口只能属于一个Monitor Link组。

·配置Monitor Link组的成员接口也可在接口视图下进行。

【举例】

\# 配置Monitor Link组1的上行接口为GigabitEthernet1/0/1，下行接口为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname monitor-link group 1

Sysname-mtlk-group1 port gigabitethernet 1/0/1 uplink

Sysname-mtlk-group1 port gigabitethernet 1/0/2 downlink

【相关命令】

·**port monitor-link group**

**Monitor Link \-- Monitor Link配置命令 \-- port monitor-link group**

------------------------------------------------------------------------

**[port monitor-link group**]命令用来配置Monitor Link组的成员接口。

**[undo port monitor-link group**]命令用来取消Monitor Link组成员接口的配置。

【命令】

**[port monitor-link group ***group-id*[ { **downlink** \| **uplink** }]]

**[undo port monitor-link group ***group-id*]

【缺省情况】

接口/子接口不是Monitor Link组的成员接口。

【视图】

二层以太网接口视图/三层以太网接口视图/三层以太网子接口视图/二层聚合接口视图/三层聚合接口视图/三层聚合子接口视图/S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示Monitor Link组的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[downlink**]：表示下行接口。

**[uplink**]：表示上行接口。

【使用指导】

·如果已将一个接口的主接口配置为Monitor Link组的下行接口，请勿再将该接口的子接口配置为任何Monitor Link组的上行接口，否则将影响Monitor Link协议的正常运行。

·不允许将一个聚合接口及其所对应聚合组的成员端口加入同一个Monitor Link组中，否则将影响Monitor Link协议的正常运行。

·由于同一接口的主接口和子接口的up/down状态本身是联动的，因此请勿将它们加入同一个Monitor Link组中，否则将影响该Monitor Link组的性能。

·一个接口只能属于一个Monitor Link组。

·配置Monitor Link组的成员接口也可在Monitor Link组视图下进行。

【举例】

\# 将GigabitEthernet1/0/1和GigabitEthernet1/0/2分别配置为Monitor Link组1的上行接口和下行接口。

\<Sysname\> system-view

Sysname monitor-link group 1

Sysname-mtlk-group1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port monitor-link group 1 uplink

Sysname-GigabitEthernet1/0/1 quit

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 port monitor-link group 1 downlink

【相关命令】

·**port**
