<!-- CMD-INDEX
  display smart-link flush            | 任意视图             | L16
  display smart-link group            | 任意视图             | L86
  flush enable                        | Smart Link组视图    | L210
  port                                | Smart Link组视图    | L264
  port smart-link group               | 二层以太网接口视图/二层聚合接口视图 | L330
  port smart-link group track         | 二层以太网接口视图/二层聚合接口视图 | L412
  preemption delay                    | Smart Link组视图    | L502
  preemption mode                     | Smart Link组视图    | L556
  protected-vlan                      | Smart Link组视图    | L614
  reset smart-link statistics         | 用户视图             | L684
  smart-link flush enable             | 二层以太网接口视图/二层聚合接口视图 | L714
  smart-link group                    | 系统视图             | L768
-->

**Smart Link \-- Smart Link配置命令 \-- display smart-link flush**

------------------------------------------------------------------------

**[display smart-link flush**]命令用来显示设备收到的Flush报文信息。

【命令】

**[display smart-link flush**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示设备收到的Flush报文信息。

\<Sysname\> display smart-link flush

 Received flush packets                             : 10

 Receiving interface of the last flush packet       : GigabitEthernet1/0/1

 Receiving time of the last flush packet            : 19:19:03 2012/04/21

 Device ID of the last flush packet                 : 000f-e200-8500

 Control VLAN of the last flush packet              : 1

表1-1 display smart-link flush命令显示信息描述表

字段

描述

Received flush packets

接收的Flush报文总数

Receiving interface of the last flush packet

接收最后一个Flush报文的端口

Receiving time of the last flush packet

接收最后一个Flush报文的时间

Device ID of the last flush packet

接收的最后一个Flush报文中携带的设备标识

Control VLAN of the last flush packet

接收的最后一个Flush报文中携带的控制VLAN

【相关命令】

·**reset smart-link statistics**

**Smart Link \-- Smart Link配置命令 \-- display smart-link group**

------------------------------------------------------------------------

**[display smart-link group**]命令用来显示Smart Link组的信息。

【命令】

**[display smart-link group**[ { *group-id* \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-id*]：显示指定Smart Link组的信息。*group-id*表示Smart Link组的编号，最小取值为1，不同型号的设备支持的最大值不同，请以设备的实际情况为准。

**[all**]：显示所有Smart Link组的信息。

【使用指导】

请勿将一个端口同时加入聚合组和Smart Link组，否则该端口在Smart Link组中将不会生效，也无法使用本命令查看到。

【举例】

\# 显示Smart Link组1的信息。

\<Sysname\> display smart-link group 1

Smart link group 1 information:

  Device ID       : 0011-2200-0001

  Preemption mode : NONE

  Preemption delay: 1(s)

  Control VLAN    : 1

  Protected VLAN  : Reference Instance 2, 4

  Member                  Role      State   Flush-count     Last-flush-time

  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  GE1/0/1                 PRIMARY   ACTIVE  1               16:45:20 2012/04/21

  GE1/0/2                 SECONDARY STANDBY 2               16:37:20 2012/04/21

表1-2 display smart-link group命令显示信息描述表

字段

描述

Smart link group 1 information

Smart Link组的信息

Device ID

设备标识

Preemption mode

抢占模式：

·NONE：非抢占模式

·ROLE：角色抢占模式

Preemption delay

抢占延时，单位为秒

Control-VLAN

控制VLAN

Protected VLAN

Smart Link组保护的VLAN列表。此处显示的是引用的MSTI（Multiple Spanning Tree Instance，多生成树实例），所引用的MSTI与VLAN间的映射关系可通过命令**display stp region-configuration**查看

Member

Smart Link组的成员端口

Role

端口角色：

·PRIMARY：主端口

·SECONDARY：从端口

State

端口状态：

·ACTIVE：转发

·DOWN：故障

·STANDBY：待命

Flush-count

发送的Flush报文数

Last-flush-time

最后一次发送Flush报文的时间，NA表示没有发送过Flush报文

**Smart Link \-- Smart Link配置命令 \-- flush enable**

------------------------------------------------------------------------

**[flush enable**]命令用来使能发送Flush报文的功能。

**[undo flush enable**]命令用来关闭发送Flush报文的功能。

【命令】

**[flush enable** [ **control-vlan** *vlan-id* ]]

**[undo flush enable**]

【缺省情况】

发送Flush报文的功能处于开启状态，且控制VLAN为VLAN 1。

【视图】

Smart Link组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[control-vlan*** vlan-id*]：表示发送Flush报文的控制VLAN。*vlan-id*为控制VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·需要为不同的Smart Link组配置不同的控制VLAN。

·请确保控制VLAN存在，且Smart Link组的端口要允许控制VLAN的报文通过。

·某Smart Link组的控制VLAN应同时为该Smart Link组的保护VLAN，且不要将已配置为控制VLAN的VLAN删除，否则会影响Flush报文的发送。

【举例】

\# 在Smart Link组1中关闭发送Flush报文的功能。

\<Sysname\> system-view

Sysname smart-link group 1

Sysname-smlk-group1 undo flush enable

【相关命令】

·**smart-link flush enable**

**Smart Link \-- Smart Link配置命令 \-- port**

------------------------------------------------------------------------

**[port**]命令用来配置Smart Link组的成员端口。

**[undo port**]命令用来取消Smart Link组成员端口的配置。

【命令】

**[port**[ *interface-type interface-number* { **primary** \| **secondary** }]]

**[undo port** *interface-type interface-number*]

【缺省情况】

Smart Link组中没有成员端口。

【视图】

Smart Link组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type* *interface-number*]：表示端口类型和端口编号，包括二层以太网接口和二层聚合接口。

**[primary**]：表示主端口。

**[secondary**]：表示从端口。

【使用指导】

·在配置Smart Link组的成员端口之前，请确认端口未启用生成树协议或者RRPP功能；端口配置为Smart Link组成员后，不能在该端口上开启生成树协议或者RRPP功能。

·请勿将一个端口同时加入聚合组和Smart Link组，否则该端口在Smart Link组中将不会生效，也无法使用**display smart-link group**命令查看到。

·配置Smart Link组的成员端口也可在接口视图下进行。

【举例】

\# 配置Smart Link组1的从端口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo stp enable

Sysname-GigabitEthernet1/0/1 quit

Sysname smart-link group 1

Sysname-smlk-group1 protected-vlan reference-instance 0

Sysname-smlk-group1 port gigabitethernet 1/0/1 secondary

【相关命令】

·**port smart-link group**

**Smart Link \-- Smart Link配置命令 \-- port smart-link group**

------------------------------------------------------------------------

**[port smart-link group**]命令用来配置Smart Link组的成员端口。

**[undo port smart-link group**]命令用来取消Smart Link组成员端口的配置。

【命令】

**[port smart-link group ***group-id*[ { **primary** \| **secondary** }]]

**[undo port smart-link group ***group-id*]

【缺省情况】

接口不是Smart Link组的成员端口。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：Smart Link组的编号。最小取值为1，不同型号的设备支持的最大值不同，请以设备的实际情况为准。

**[primary**]：表示主端口。

**[secondary**]：表示从端口。

【使用指导】

·在配置Smart Link组的成员端口之前，请确认端口未启用生成树协议或者RRPP功能；端口配置为Smart Link组的成员端口后，不能在该端口上开启生成树协议或者RRPP功能。

·请勿将一个端口同时加入聚合组和Smart Link组，否则该端口在Smart Link组中将不会生效，也无法使用**display smart-link group**命令查看到。

·配置Smart Link组的成员端口也可在Smart Link组视图下进行。

【举例】

\# 将端口GigabitEthernet1/0/1配置为Smart Link组1的主端口。

\<Sysname\> system-view

Sysname smart-link group 1

Sysname-smlk-group1 protected-vlan reference-instance 0

Sysname-smlk-group1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo stp enable

Sysname-GigabitEthernet1/0/1 port smart-link group 1 primary

\# 将二层聚合接口1配置为Smart Link组1的主端口。

\<Sysname\> system-view

Sysname smart-link group 1

Sysname-smlk-group1 protected-vlan reference-instance 0

Sysname-smlk-group1 quit

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 undo stp enable

Sysname-Bridge-Aggregation1 port smart-link group 1 primary

【相关命令】

·**port**

**Smart Link \-- Smart Link配置命令 \-- port smart-link group track**

------------------------------------------------------------------------

![说明](Smart%20Link命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[port smart-link group track**]命令用来配置Smart Link组的成员端口与Track项联动。

**[undo port smart-link group track**]命令用来取消Smart Link组的成员端口与Track项联动。

【命令】

**[port smart-link group ***group-id*** track ***track-entry-number*]

**[undo port smart-link group ***group-id* **track** *track-entry-number*]

【缺省情况】

Smart Link组的成员端口未与任何Track项联动。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示Smart Link组的编号。最小取值为1，不同型号的设备支持的最大值不同，请以设备的实际情况为准。

*[track-entry-number*]：表示Track项的序号，必须是与CFD连续性检测功能关联的Track项。

【使用指导】

·Smart Link组的成员端口通过Track项与链路检测协议进行联动，目前仅支持与CFD的连续性检测功能联动，请通过**track cfd**命令创建与CFD连续性检测功能关联的Track项。

·在配置端口与Track项联动之前，必须保证该端口已加入相应的Smart Link组。

【举例】

\# 配置Smart Link组1的主端口GigabitEthernet1/0/1通过Track项1与CFD的连续性检测功能联动，以检测其链路状态。

\<Sysname\> system-view

Sysname track 1 cfd cc service-instance 100 mep 2

Sysname smart-link group 1

Sysname-smlk-group1 protected-vlan reference-instance 0

Sysname-smlk-group1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo stp enable

Sysname-GigabitEthernet1/0/1 port smart-link group 1 primary

Sysname-GigabitEthernet1/0/1 port smart-link group 1 track 1

\# 配置Smart Link组1的主端口二层聚合接口1通过Track项1与CFD的连续性检测功能联动，以检测其链路状态。

\<Sysname\> system-view

Sysname track 1 cfd cc service-instance 100 mep 2

Sysname smart-link group 1

Sysname-smlk-group1 protected-vlan reference-instance 0

Sysname-smlk-group1 quit

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 undo stp enable

Sysname-Bridge-Aggregation1 port smart-link group 1 primary

Sysname-Bridge-Aggregation1 port smart-link group 1 track 1

【相关命令】

·**track cfd**（可靠性命令参考/Track）

**Smart Link \-- Smart Link配置命令 \-- preemption delay**

------------------------------------------------------------------------

**[preemption delay**]命令用来配置抢占延时。

**[undo preemption delay**]命令用来恢复缺省情况。

【命令】

**[preemption delay*** delay*]

**[undo preemption delay**]

【缺省情况】

抢占延时为1秒。

【视图】

Smart Link组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：表示抢占延时，取值范围为0～300，单位为秒。

【使用指导】

·抢占延时在配置了抢占模式之后才会生效。

·在角色抢占模式下，在主端口抢占为转发状态之前，先延迟一段时间以配合上游设备的切换，这段延迟时间就叫做抢占延时。

【举例】

\# 配置抢占模式为角色抢占模式，并配置抢占延时为10秒。

\<Sysname\> system-view

Sysname smart-link group 1

Sysname-smlk-group1 preemption mode role

Sysname-smlk-group1 preemption delay 10

【相关命令】

·**preemption mode**

**Smart Link \-- Smart Link配置命令 \-- preemption mode**

------------------------------------------------------------------------

**[preemption mode**]命令用来配置Smart Link组的抢占模式。

**[undo preemption mode**]命令用来恢复缺省情况。

【命令】

**[preemption mode **[{ **role** \| **speed** [ **threshold** *threshold-value* ] }]]

**[undo preemption mode**]

【缺省情况】

Smart Link组为非抢占模式。

【视图】

Smart Link组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[role**]：配置Smart Link组的抢占模式为角色抢占模式，即当主链路恢复后，主端口切换回转发状态。

**[speed**]：配置Smart Link组的抢占模式为速率抢占模式。

**[threshold** *threshold-value*]：速率抢占阈值，取值范围为1～10000。在Smart Link组的抢占模式为速率抢占模式时，如果配置了本参数，当主链路恢复后，如果主端口的速率大于等于从端口速率的*threshold-value*%，主端口切换回转发状态；如果未配置本参数，当主链路恢复后，只要主端口的速率大于从端口的速率，主端口就切换回转发状态。

【使用指导】

抢占延时在配置了Smart Link组的抢占模式之后才会生效。

【举例】

\# 配置Smart Link组的抢占模式为角色抢占模式。

\<Sysname\> system-view

Sysname smart-link group 1

Sysname-smlk-group1 preemption mode role

\# 配置Smart Link组的抢占模式为速率抢占模式，速率抢占阈值为1000。

\<Sysname\> system-view

Sysname smart-link group 1

Sysname-smlk-group1 preemption mode speed threshold 1000

**Smart Link \-- Smart Link配置命令 \-- protected-vlan**

------------------------------------------------------------------------

**[protected-vlan**]命令用来配置Smart Link组的保护VLAN。

**[undo protected-vlan**]命令用来删除Smart Link组中保护VLAN的相关配置。

【命令】

**[protected-vlan reference-instance** *instance-id-list*]

**[undo protected-vlan** [ **reference-instance** *instance-id-list* ]]

【缺省情况】

Smart Link组不保护任何VLAN。

【视图】

Smart Link组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reference-instance ***instance-id-list*]：通过引用MSTI的方式来配置Smart Link组的保护VLAN。*instance-id-list*为MSTI列表，表示方式为*instance-id-list *= { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0到4094，0表示CIST。&\<1-10\>表示前面的参数最多可以输入10次。MSTI所映射的VLAN可通过命令**display stp region-configuration**查看。

【使用指导】

·在使用**undo protected-vlan**命令时若指定了**reference-instance*** instance-id-list*参数，将删除Smart Link组中指定MSTI所映射VLAN的相关配置；否则，将删除Smart Link组中所有MSTI所映射VLAN的相关配置。

·在配置Smart Link组的成员端口之前必须配置保护VLAN。

·在删除保护VLAN的相关配置时，如果Smart Link组中已经配置了成员端口，则不允许删除所有保护VLAN的相关配置；如果Smart Link组中没有配置成员端口，则可以删除所有保护VLAN的相关配置。

·在删除Smart Link组时会同时删除其所保护VLAN的相关配置。

·若VLAN与MSTI的映射关系发生变化，Smart Link组实际所保护的VLAN也会根据Smart Link组的保护VLAN所引用的MSTI而变化。

·Smart Link端口允许通过的VLAN都应该被Smart Link组保护。

【举例】

\# 先将VLAN 1～30映射到MSTI 1上，并激活MST域的配置；然后配置Smart Link 组1的保护VLAN为MSTI 1所映射的VLAN。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region instance 1 vlan 1 to 30

Sysname-mst-region active region-configuration

Sysname-mst-region quit

Sysname smart-link group 1

Sysname-smlk-group1 protected-vlan reference-instance 1

【相关命令】

·**display stp region-configuration**（二层技术-以太网交换命令参考/生成树）

·**smart-link group**

**Smart Link \-- Smart Link配置命令 \-- reset smart-link statistics**

------------------------------------------------------------------------

**[reset smart-link statistics**]命令用来清除Flush报文的统计信息。

【命令】

**[reset smart-link statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除Flush报文的统计信息。

\<Sysname\> reset smart-link statistics

【相关命令】

·**display smart-link flush**

**Smart Link \-- Smart Link配置命令 \-- smart-link flush enable**

------------------------------------------------------------------------

**[smart-link flush enable**]命令用来使能接收Flush报文的功能。

**[undo smart-link flush enable**]命令用来取消相关配置。

【命令】

**[smart-link flush enable** [ **control-vlan** *vlan-id-list* ]]

**[undo smart-link flush enable ** **control-vlan** *vlan-id-list* ]

【缺省情况】

接收Flush报文的功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[control-vlan*** vlan-id-list*]：表示接收Flush报文的控制VLAN，缺省值为1。*vlan-id-list*为控制VLAN列表，*vlan-id-list*＝{ *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。&\<1-10\>表示前面的参数最多可以输入10次。

【举例】

\# 在端口GigabitEthernet1/0/1上使能接收Flush报文的功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 smart-link flush enable

\# 在二层聚合接口1上使能接收Flush报文的功能。

\<Sysname\> system-view

Sysname interface bridge-aggregation 1

Sysname-Bridge-Aggregation1 smart-link flush enable

【相关命令】

·**flush enable**

**Smart Link \-- Smart Link配置命令 \-- smart-link group**

------------------------------------------------------------------------

**[smart-link group**]命令用来创建Smart Link组，并进入Smart Link组视图。

**[undo smart-link group**]命令用来删除Smart Link组。

【命令】

**[smart-link group ***group-id*]

**[undo smart-link group ***group-id*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：表示Smart Link组的编号。最小取值为1，不同型号的设备支持的最大值不同，请以设备的实际情况为准。

【使用指导】

当Smart Link组内有成员端口时不允许删除。

【举例】

\# 创建Smart Link组1，并进入Smart Link组1的视图。

\<Sysname\> system-view

Sysname smart-link group 1

Sysname-smlk-group1
