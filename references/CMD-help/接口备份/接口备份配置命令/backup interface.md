
**接口备份 \-- 接口备份配置命令 \-- backup interface**

------------------------------------------------------------------------

**[backup interface**]命令用来配置主接口的备份接口。

**[undo backup interface**]命令用来删除备份接口。

【命令】

**[backup interface** *interface-type interface-number* [ *priority* ]]

**[undo backup interface ***interface-type interface-number*]

【缺省情况】

没有为主接口配置备份接口。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。

*[priority*]：指定备份接口的优先级，取值范围为0～255，缺省值为0。该数值越大表示优先级越高。

【使用指导】

通过为主接口配置备份接口，建立接口间的主备关系，命令所在视图的接口被指定为主接口，默认为主备方式备份，配置负载分担门限后可开启负载分担方式备份。

备份接口优先级仅在在用接口链路UP/DOWN（主备方式）和检测到流量变化（负载分担方式）时作为选取开启和关闭备份接口顺序的参考。备份接口被启用并up时，即使存在更高优先级的备份接口，都不再调整启用的备份接口。例如，备份接口GigabitEthernet1/0/1、GigabitEthernet1/0/2、GigabitEthernet1/0/3的优先级依此递减，当主接口down时先选取GigabitEthernet1/0/1，若GigabitEthernet1/0/1能够up，则GigabitEthernet1/0/1成为在用备份接口，否则继续选取GigabitEthernet1/0/2，直至所有备份接口都被选取；若备份接口全部被选取，GigabitEthernet1/0/2首先up，则GigabitEthernet1/0/2成为在用备份接口，GigabitEthernet1/0/1和GigabitEthernet1/0/3将被关闭，此时即使GigabitEthernet1/0/1已经可以up或配置了更高优先级的备份接口，都不再调整启用的备份接口；若GigabitEthernet1/0/2作为在用备份接口down时，则按照优先级首先选取GigabitEthernet1/0/1，若GigabitEthernet1/0/1不能up，继续选取GigabitEthernet1/0/3。备份接口的优先级相同时，先配置的备份接口将先启用。

需要注意的是：

·主备接口不可以嵌套配置，即一个主接口不能作为另外一个接口的备份接口。

·一个备份接口只能为1个主接口提供备份。

·一台设备上最多允许同时存在10个主接口。

·一个主接口最多允许有3个备份接口。

·子接口不能和其所对应的主接口建立备份关系。

·备份接口和主接口不能是逻辑链路成员接口，如三层聚合接口的成员接口。

·本命令与**backup track**命令互斥。也就是说，当在主接口上配置了**backup interface**后，在该主接口及其备份接口上都不能配置**backup track**；反之，当在某接口上配置了**backup track**后，也不能将该接口再配置为**backup interface**的主接口或备份接口。

【举例】

\# 指定接口GigabitEthernet1/0/2为接口GigabitEthernet1/0/1的备份接口，其优先级为50。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 backup interface gigabitethernet 1/0/2 50

【相关命令】

·**backup track**

**接口备份 \-- 接口备份配置命令 \-- backup threshold**

------------------------------------------------------------------------

**[backup threshold**]命令用来配置负载分担门限。

**[undo backup threshold**]命令用来取消负载分担门限的配置。

【命令】

**[backup threshold ***upper-threshold lower-threshold*]

**[undo backup threshold**]

【缺省情况】

没有配置负载分担门限。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[upper-threshold*]：指定负载分担门限的上限阈值，该参数表示数据流量占主接口带宽的百分比数值，取值范围为1～99。

*[lower-threshold*]：指定负载分担门限的下限阈值，该参数表示数据流量占主接口带宽的百分比数值，取值范围为1～99，且必须小于*upper-threshold*的配置值。

【使用指导】

为主接口配置备份接口后，通过配置负载分担门限开启负载分担方式。负载分担门限表示数据流量占主接口带宽的百分比数值，取值范围为1～99，用于计算负载分担上下限阈值。

当主接口上的数据流量超过了负载分担的上限阈值时，备份接口开始进行负载分担，若负载分担后主接口的流量又低于了下限阈值，备份接口将结束负载分担，导致备份接口不断地在up和down状态之间切换。为了避免这种情况的出现，配置时建议使下限阈值小于上限阈值的一半。

主接口带宽可通过**bandwidth**命令配置。

需要注意的是：

·配置负载分担方式后，若主接口链路状态为DOWN，将仍按照主备方式备份。

·**backup threshold**命令只能在主接口上执行，且必须在指定了备份接口之后执行。

【举例】

\# 在接口GigabitEthernet1/0/1上配置负载分担门限的上限阈值为80，下限阈值为20。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 backup threshold 80 20

【相关命令】

·**backup interface**

·**backup timer flow-check**

**接口备份 \-- 接口备份配置命令 \-- backup timer delay**

------------------------------------------------------------------------

**[backup timer delay**]命令用来配置接口状态切换延时。

**[undo backup timer delay**]命令用来恢复缺省情况。

【命令】

**[backup timer delay ***up-delay down-delay *]

**[undo backup timer delay**]

【缺省情况】

接口状态切换延时均为5秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[up-delay*]：接口UP延时，即接口状态切换为UP前的延时时间，取值范围为1～65535，单位为秒。

*[down-delay*]：接口DOWN延时，即接口状态切换为DOWN前的延时时间，取值范围为1～65535，单位为秒。

【使用指导】

通常情况下，接口链路状态发生改变时，接口的状态切换应立即执行，但若接口链路状态不稳定则会引起接口状态的频繁切换，此现象可通过设置接口状态切换延迟时间来避免。若在用接口链路状态发生改变，系统将在该延迟时间后再做切换，若该延迟时间内在用接口链路状态恢复，则不进行切换。

需要注意的是，**backup timer delay**命令只能在主接口上执行，且必须在指定了备份接口之后执行。

【举例】

\# 指定接口GigabitEthernet1/0/2为接口GigabitEthernet1/0/1的备份接口，并设置接口状态切换延时均为10秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 backup interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/1 backup timer delay 10 10

【相关命令】

·**backup interface**

**接口备份 \-- 接口备份配置命令 \-- backup timer flow-check**

------------------------------------------------------------------------

**[backup timer flow-check**]命令用来配置检测主接口和备份接口流量的时间间隔。

**[undo backup timer flow-check**]命令用来恢复缺省情况。

【命令】

**[backup timer flow-check** *interval*]

**[undo backup timer flow-check**]

【缺省情况】

检测主接口和备份接口流量的时间间隔为30秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：检测主接口和备份接口流量的时间间隔，取值范围为30～600，单位为秒。

【使用指导】

负载分担备份情况下周期性进行流量监测，根据流量信息进行备份接口启动或关闭的操作。通过本命令配置检测流量的时间间隔来设定检测的周期。

需要注意的是，**backup timer flow-check**命令只能在主接口上执行，且必须在指定了备份接口之后执行。

【举例】

\# 在主接口GigabitEthernet1/0/1上配置检测主接口和备份接口流量的时间间隔为60秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 backup timer flow-check 60

【相关命令】

·**backup interface**

**接口备份 \-- 接口备份配置命令 \-- backup track**

------------------------------------------------------------------------

![说明](接口备份命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[backup track**]命令用来配置接口与Track项关联。

**[undo backup track**]命令用来取消接口与Track项的关联。

【命令】

**[backup track ***track-entry-number*]

**[undo backup track**]

【缺省情况】

接口没有与Track项关联。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：指定Track项序号，取值范围为1～1024。

【使用指导】

通过配置接口与Track项关联，使该接口作为备份接口，通过Track项来监测主链路的状态，从而可以根据网络环境的变化来改变备份接口的状态。当Track项为Negative状态时，备份接口被启用，当Track项为Positive状态时，备份接口被停用。

需要注意的是：

·本命令与**backup interface**命令互斥。也就是说，当在主接口上配置了**backup interface**后，在该主接口及其备份接口上都不能配置**backup track**；反之，当在某接口上配置了**backup track**后，也不能将该接口再配置为**backup interface**的主接口或备份接口。

·一个接口只能关联一个Track项。如果在同一接口上多次执行本命令，则新的配置将覆盖旧的配置。

·接口上所关联的Track项可以是尚未创建的Track项。但是，只有当该Track项创建后，联动功能才开始生效。

·通过Track联动方式配置的备份接口的数量建议不要超过64个，否则可能影响设备的正常运行。

【举例】

\# 配置接口GigabitEthernet1/0/1与Track项1关联。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 backup track 1

【相关命令】

·**backup interface**

**接口备份 \-- 接口备份配置命令 \-- display interface-backup state**

------------------------------------------------------------------------

**[display interface-backup state**]命令用来查看主接口与备份接口的状态。

【命令】

**[display interface-backup state**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看主接口与备份接口的状态。

\<Sysname\> display interface-backup state

Interface: GE1/0/1

  UpDelay: 10 s

  DownDelay: 5 s

  State: UP

  Backup interfaces:

    GE1/0/2             Priority: 30   State: STANDBY

    GE1/0/3             Priority: 20   State: STANDBY

Interface: GE1/0/5

  UpDelay: 10 s

  DownDelay: 5 s

  Upper threshold: 80

  Lower threshold: 20

State: DOWN

  Backup interfaces:

    GE1/0/6             Priority: 30   State: UP_DELAY

    GE1/0/7             Priority: 20   State: STANDBY

IB Track Information:

  GE1/0/4              Track: 1  State: STANDBY

  GE1/0/8              Track: 2  State: UP

表1-1 display interface-backup state命令显示信息描述表

字段

描述

Interface

主接口名称

UpDelay

接口延时UP超时时间，单位为秒

DownDelay

接口延时DOWN超时时间，单位为秒

Upper threshold

负载分担门限的上限阈值

Lower threshold

负载分担门限的下限阈值

State

主接口状态：

·UP：UP状态

·DOWN：DOWN状态

·UP_DELAY：延时UP状态

·DOWN_DELAY：延时DOWN状态

Backup interfaces

主接口关联的所有备份接口

Priority

备份接口优先级

State

备份接口状态：

·UP：UP状态

·DOWN：DOWN状态

·UP_DELAY：延时UP状态

·DOWN_DELAY：延时DOWN状态

·STANDBY：备用状态

IB Track Information

与Track项关联的备份接口信息

GE1/0/4

备份接口

Track

备份接口关联的Track项

State

关联了Track项的备份接口状态：

·INVALID：接口角色未生效（比如Track项未创建）

·UP：UP状态

·DOWN：DOWN状态

·STANDBY：备用状态

**接口备份 \-- 接口备份配置命令 \-- display interface-backup statistics**

------------------------------------------------------------------------

**[display interface-backup statistics**]命令用来查看参与负载分担的接口的流量统计信息。

【命令】

**[display interface-backup statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 查看参与负载分担的接口的流量统计信息。

\<Sysname\> display interface-backup statistics

Interface: GigabitEthernet1/0/2

  Statistics interval: 30 s

  Bandwidth: 100000000 bps

  PrimaryTotalIn: 102 bytes

  PrimaryTotalOut: 108 bytes

  PrimaryIntervalIn: 102 bytes

  PrimaryIntervalOut: 108 bytes

  Primary used bandwidth: 28 bps

  TotalIn: 102 bytes

  TotalOut: 108 bytes

  TotalIntervalIn: 102 bytes

  TotalIntervalOut: 108 bytes

  Total used bandwidth: 28 bps

表1-2 display interface-backup statistics命令显示信息描述表

字段

描述

Interface

主接口名称

Statistics interval

检测主接口和备份接口流量的时间间隔，单位为秒

Bandwidth

主接口带宽，单位为比特每秒

PrimaryTotalIn

上一次检测时主接口累计的接收字节数，单位为字节

PrimaryTotalOut

上一次检测时主接口累计的发送字节数，单位为字节

PrimaryIntervalIn

上一个时间间隔内主接口的接收字节数，单位为字节

PrimaryIntervalOut

上一个时间间隔内主接口的发送字节数，单位为字节

Primary used bandwidth

上一个时间间隔内主接口参与负载分担的实际带宽，单位为比特每秒

TotalIn

上一次检测时主接口与在用备份接口累计的接收总字节数，单位为字节

TotalOut

上一次检测时主接口与在用备份接口累计的发送总字节数，单位为字节

TotalIntervalIn

上一个时间间隔内主接口与在用备份接口的接收总字节数，单位为字节

TotalIntervalOut

上一个时间间隔内主接口与在用备份接口的发送总字节数，单位为字节

Total used bandwidth

上一个时间间隔内主接口与在用备份接口的实际总带宽，单位为比特每秒

