
**以太网OAM \-- 以太网OAM配置命令 \-- display oam**

------------------------------------------------------------------------

**[display** **oam**]命令用来显示以太网OAM连接的信息，包括连接状态、以太网OAM报文头部信息和以太网OAM报文统计信息。

【命令】

**[display**[ **oam** { **local** \| **remote** } [ **interface** *interface-type interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[local**]：显示本端信息。

**[remote**]：显示远端信息。

**[interface** *interface-type interface-number*]：显示指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。

【举例】

\# 显示所有接口上以太网OAM连接的本端信息。

\<Sysname\> display oam local

\-\-\-\-\-\-\-\-\-\-- [GigabitEthernet1/0/1 \-\-\-\-\-\-\-\-\-\--]

 Enable status     : Enable

 Loopback status   : No loopback

 Link status       : UP

 OAM mode          : Active

 PDU               : ANY

 Mux action        : FWD

 Par action        : FWD

\# 显示接口GigabitEthernet1/0/1上以太网OAM连接的本端信息。

\<Sysname\> display oam local interface gigabitethernet 1/0/1

 Enable status     : Enable

 Loopback status   : No loopback

 Link status       : UP

 OAM mode          : Active

 PDU               : ANY

 Mux action        : FWD

 Par action        : FWD

 Flags

   Link fault        : Not occurred

   Dying gasp        : Not occurred

   Critical event    : Not occurred

   Local evaluating  : COMPLETE

   Remote evaluating : COMPLETE

 Packets statistics

   Packet type                      Sent                   Received

   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

   OAMPDU                           100                    80

   OAMInformation                   64                     60

   OAMEventNotification             36                     20

   OAMUniqueEventNotification       36                     10

   OAMDuplicateEventNotification    0                      10

表1-1 display oam local命令显示信息描述表

字段

描述

GigabitEthernet1/0/1

接口GigabitEthernet1/0/1上的信息

Enable status

本端的以太网OAM状态：

·Enable：表示已使能

·Disable：表示未使能

Loopback status

以太网OAM远端环回状态：

·No loopback：表示尚未建立远端环回

·Remote loopback：表示远端环回的主控端

·Local loopback：表示远端环回的被控端

Link status

链路状态：

·UP：表示链路up

·DOWN：表示链路down

OAM mode

本端以太网OAM的连接模式：

·Active：表示主动模式

·Passive：表示被动模式

PDU

本端对OAMPDU的处理方式：

·RX_INFO：表示只接收Information OAMPDU，不允许发送任何OAMPDU

·LF_INFO：表示只发送不带Information TLV且链路错误标志位已被置位的Information OAMPDU

·INFO：表示只收发Information OAMPDU

·ANY：表示可收发所有OAMPDU

Mux action

本端发送器的工作方式：

·FWD：表示发送方向为FORWARDING，允许发送任何报文

·DISCARD：表示发送方向为DISCARDING，只允许发送OAMPDU

Par action

本端接收器的工作方式：

·FWD：表示接收方向为FORWARDING，允许接收任何报文

·DISCARD：表示接收方向为DISCARDING，只允许接收OAMPDU

·LB：表示接收方向处于环回状态，收到的所有非OAMPDU都将按原路返回

Flags

以太网OAM报文中的本端标识域

Link fault

是否发生链路故障：

·Occurred：表示已发生

·Not occurred：表示未发生

Dying gasp

是否发生致命故障：

·Occurred：表示已发生

·Not occurred：表示未发生

Critical event

是否发生紧急事件：

·Occurred：表示已发生

·Not occurred：表示未发生

Local evaluating

本端对远端配置的协商过程：

·COMPLETE：表示协商已完成

·NOTCOMPLETE：表示协商未完成

Remote evaluating

远端对本端配置的协商过程：

·COMPLETE：表示协商已完成

·NOTCOMPLETE：表示协商未完成

·RESERVED：表示此字段为保留值，协商未完成

·UNSATISFIED：表示远端对本端的配置不满意，协商未完成

Packets statistics

各种以太网OAM报文的发送和接收数量

Packet type

报文类型

Sent

发送的报文数量

Received

收到的报文数量

OAMPDU

以太网OAM报文

OAMInformation

以太网OAM信息报文

OAMEventNotification

以太网OAM事件通知报文

OAMUniqueEventNotification

以太网OAM一次性发送或接收的事件报文

OAMDuplicateEventNotification

以太网OAM重复发送或接收的事件报文

\# 显示所有接口上以太网OAM连接的远端信息。

\<Sysname\> display oam remote

\-\-\-\-\-\-\-\-\-\-- [GigabitEthernet1/0/1 \-\-\-\-\-\-\-\-\-\--]

 OAM mode          : Active

 MAC address       : 3822-d6a2-a800

MTU size          : 1500

 Mux action        : FWD

 Par action        : FWD

\# 显示接口GigabitEthernet1/0/1上以太网OAM连接的远端信息。

\<Sysname\> display oam remote interface gigabitethernet 1/0/1

 OAM mode          : Active

MAC address       : 3822-d6a2-a800

MTU size          : 1500

 Mux action        : FWD

 Par action        : FWD

Configuration

   Unidirectional    : Not supported

   Remote loopback   : Supported

   Link events       : Supported

   MIB retrieval     : Not supported

 Flags

   Link fault        : Not occurred

   Dying gasp        : Not occurred

   Critical event    : Not occurred

   Local evaluating  : COMPLETE

   Remote evaluating : COMPLETE

表1-2 display oam remote命令显示信息描述表

字段

描述

GigabitEthernet1/0/1

接口GigabitEthernet1/0/1上的信息

OAM mode

远端的以太网OAM连接模式：

·Active：表示主动模式

·Passive：表示被动模式

MAC address

远端的MAC地址

MTU size

以太网OAM实体间传送的报文最大长度，单位为字节

Mux action

远端发送器的工作方式

·FWD：表示发送方向为FORWARDING，允许发送任何报文

·DISCARD：表示发送方向为DISCARDING，只允许发送OAMPDU

Par action

远端接收器的工作方式：

·FWD：表示接收方向为FORWARDING，允许接收任何报文

·DISCARD：表示接收方向为DISCARDING，只允许接收OAMPDU

·LB：表示接收方向处于环回状态，收到的所有非OAMPDU都将按原路返回

Configuration

远端以太网OAM实体的配置信息

Unidirectional

是否支持单向传输：

·Supported：表示支持

·Not supported：表示不支持

Remote loopback

是否支持远端环回：

·Supported：表示支持

·Not supported：表示不支持

Link events

是否支持一般链路事件：

·Supported：表示支持

·Not supported：表示不支持

MIB retrieval

是否支持获取MIB变量：

·Supported：表示支持

·Not supported：表示不支持

Flags

以太网OAM报文中的远端标识域

Link fault

是否发生链路故障：

·Occurred：表示已发生

·Not occurred：表示未发生

Dying gasp

是否发生致命故障：

·Occurred：表示已发生

·Not occurred：表示未发生

Critical event

是否发生紧急事件：

·Occurred：表示已发生

·Not occurred：表示未发生

Local evaluating

本端对远端配置的协商过程：

·COMPLETE：表示协商已完成

·NOTCOMPLETE：表示协商未完成

·RESERVED：表示此字段为保留值，协商未完成

·UNSATISFIED：表示本端对远端的配置不满意，协商未完成

Remote evaluating

远端对本端配置的协商过程：

·COMPLETE：表示协商已完成

·NOTCOMPLETE：表示协商未完成

·UNSATISFIED：表示本端对远端的配置不满意，协商未完成

【相关命令】

·**reset** **oam**

**以太网OAM \-- 以太网OAM配置命令 \-- display oam configuration**

------------------------------------------------------------------------

**[display** **oam** **configuration**]命令用来显示以太网OAM的配置信息，包括各一般链路事件的检测窗口和检测阈值。

【命令】

**[display** **oam** **configuration** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示全局以及未采用缺省配置的接口上的信息。

【举例】

\# 显示全局以及未采用缺省配置的接口上的以太网OAM配置信息。

\<Sysname\> display oam configuration

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- [Global \-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]

 OAM timers

   Hello timer        : 1000 milliseconds

   Keepalive timer    : 5000 milliseconds

 Link monitoring

   Errored symbol period

     Window           : 100 x 1000000 symbols

     Threshold        : 1 error symbols

   Errored frame

     Window           : 10 x 100 milliseconds

     Threshold        : 1 error frames

   Errored frame period

     Window           : 1000 x 10000 frames

     Threshold        : 1 error frames

   Errored frame seconds

     Window           : 600 x 100 milliseconds

     Threshold        : 1 error seconds

\-\-\-\-\-\-\-\-\-\-- [GigabitEthernet1/0/1 \-\-\-\-\-\-\-\-\-\--]

 OAM timers

   Hello timer        : 500 milliseconds

   Keepalive timer    : 5000 milliseconds

Link monitoring

   Errored symbol period

     Window           : 100 x 1000000 symbols

     Threshold        : 1 error symbols

   Errored frame

     Window           : 10 x 100 milliseconds

     Threshold        : 1 error frames

   Errored frame period

     Window           : 1000 x 10000 frames

     Threshold        : 1 error frames

   Errored frame seconds

     Window           : 600 x 100 milliseconds

     Threshold        : 1 error seconds

表1-3 display oam configuration命令显示信息描述表

字段

描述

Global

全局信息

GigabitEthernet1/0/1

接口GigabitEthernet1/0/1上的信息

OAM timers

以太网OAM连接检测定时器

Hello timer

以太网OAM握手报文的发送间隔

Keepalive timer

以太网OAM连接的超时时间

Link monitoring

一般链路事件的检测窗口和检测阈值

Errored symbol period

错误信号事件

Errored frame

错误帧事件

Errored frame period

错误帧周期事件

Errored frame seconds

错误帧秒事件

Window

检测窗口

Threshold

检测阈值

**以太网OAM \-- 以太网OAM配置命令 \-- display oam critical-event**

------------------------------------------------------------------------

**[display** **oam** **critical-event**]命令用来显示以太网OAM的紧急链路事件统计信息。

【命令】

**[display** **oam** **critical-event** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。

【举例】

\# 显示所有接口上以太网OAM紧急链路事件的统计信息。

\<Sysname\> display oam critical-event

\-\-\-\-\-\-\-\-\-\-- [GigabitEthernet1/0/1 \-\-\-\-\-\-\-\-\-\--]

 Local link status   : UP

 Event statistics

   Link fault        : Not occurred

   Dying gasp        : Not occurred

   Critical event    : Not occurred

表1-4 display oam critical-event命令显示信息描述表

字段

描述

GigabitEthernet1/0/1

接口GigabitEthernet1/0/1上的信息

Local link status

本端的链路状态：

·UP：表示链路up

·DOWN：表示链路down

Event statistics

紧急链路事件的统计信息

Link fault

是否发生链路故障：

·Occurred：表示已发生

·Not occurred：表示未发生

Dying gasp

是否发生致命故障：

·Occurred：表示已发生

·Not occurred：表示未发生

Critical event

是否发生紧急事件：

·Occurred：表示已发生

·Not occurred：表示未发生

**以太网OAM \-- 以太网OAM配置命令 \-- display oam link-event**

------------------------------------------------------------------------

**[display** **oam** **link-event**]命令用来显示以太网OAM的一般链路事件统计信息。

【命令】

**[display**[ **oam** **link-event** { **local** \| **remote** } [ **interface** *interface-type interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[local**]：显示本端统计信息。

**[remote**]：显示远端统计信息。

**[interface** *interface-type interface-number*]：显示指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。

【举例】

\# 显示所有接口上以太网OAM一般链路事件的本端统计信息。

\<Sysname\> display oam link-event local

\-\-\-\-\-\-\-\-\-\-- [GigabitEthernet1/0/1 \-\-\-\-\-\-\-\-\-\--]

 Link status: UP

 OAM local errored frame event

   Event time stamp        : 49582 x 100 milliseconds

   Errored frame window    : 10 x 100 milliseconds

   Errored frame threshold : 1 error frames

   Errored frame           : 1 error frames

   Error running total     : 6 error frames

   Event running total     : 6 events

 OAM local errored frame period event

   Event time stamp                : 16382 x 100 milliseconds

   Errored frame period window     : 10000000 frames

   Errored frame period threshold  : 1 error frames

   Errored frame period            : 1 error frames

   Error running total             : 5 error frames

   Event running total             : 5 events

 OAM local errored frame seconds summary event

   Event time stamp                : 50022 x 100 milliseconds

   Errored frame seconds window    : 600 x 100 milliseconds

   Errored frame seconds threshold : 1 error seconds

   Errored frame seconds           : 1 error seconds

   Error running total             : 1 error seconds

   Event running total             : 1 events

\# 显示所有接口上以太网OAM一般链路事件的远端统计信息。

\<Sysname\> display oam link-event remote

\-\-\-\-\-\-\-\-\-\-- [GigabitEthernet1/0/1 \-\-\-\-\-\-\-\-\-\--]

 Link status: UP

 OAM remote errored symbol event

   Event time stamp         : 35498 x 100 milliseconds

   Errored symbol window    : 100000000  symbols

   Errored symbol threshold : 1 error symbols

   Errored symbol           : 1 error symbols

   Error running total      : 4 error symbols

   Event running total      : 4 events

 OAM remote errored frame event

   Event time stamp        : 49582 x 100 milliseconds

   Errored frame window    : 10 x 100 milliseconds

   Errored frame threshold : 1 error frames

   Errored frame           : 1 error frames

   Error running total     : 6 error frames

   Event running total     : 6 events

 OAM remote errored frame period event

   Event time stamp                : 16382 x 100 milliseconds

   Errored frame period window     : 10000000 frames

   Errored frame period threshold  : 1 error frames

   Errored frame period            : 1 error frames

   Error running total             : 5 error frames

   Event running total             : 5 events

 OAM remote errored frame seconds summary event

   Event time stamp                : 50022 x 100 milliseconds

   Errored frame seconds window    : 600 x 100 milliseconds

   Errored frame seconds threshold : 1 error seconds

   Errored frame seconds           : 1 error seconds

   Error running total             : 1 error seconds

   Event running total             : 1 events

表1-5 display oam link-event命令显示信息描述表

字段

描述

GigabitEthernet1/0/1

接口GigabitEthernet1/0/1上的信息

Link status

链路状态：

·UP：表示链路up

·DOWN：表示链路down

OAM remote errored symbol event

远端产生的错误信号事件信息（只有产生了错误信号事件才会显示）：

·Event time stamp：表示错误信号事件的发生时间

·Errored symbol window：表示错误信号事件的检测窗口

·Errored symbol threshold：表示错误信号事件的检测阈值

·Errored symbol：表示最近一次错误信号事件中错误信号的数量

·Error running total：表示错误信号的总数量

·Event running total：表示错误信号事件的总数量

OAM local/remote errored frame event

本端/远端产生的错误帧事件信息（只有产生了错误帧事件才会显示）：

·Event time stamp：表示错误帧事件的发生时间

·Errored frame window：表示错误帧事件的检测窗口

·Errored frame threshold：表示错误帧事件的检测阈值

·Errored frame：表示最近一次错误帧事件中错误帧的数量

·Error running total：表示错误帧的总数量

·Event running total：表示错误帧事件的总数量

OAM local/remote errored frame period event

本端/远端产生的错误帧周期事件信息（只有产生了错误帧周期事件才会显示）：

·Event time stamp：表示错误帧周期事件的发生时间

·Errored frame period window：表示错误帧周期事件的检测窗口

·Errored frame period threshold：表示错误帧周期事件的检测阈值

·Errored frame period：表示最近一次错误帧周期事件中错误帧的数量

·Error running total：表示错误帧周期的总数量

·Event running total：表示错误帧周期事件的总数量

OAM local/remote errored frame seconds summary event

本端/远端产生的错误帧秒事件信息（只有产生了错误帧秒事件才会显示）：

·Event time stamp：表示错误帧秒事件的发生时间

·Errored frame seconds window：表示错误帧秒事件的检测窗口

·Errored frame seconds threshold：表示错误帧秒事件的检测阈值

·Errored frame seconds：表示最近一次错误帧秒事件中错误帧的数量

·Error running total：表示错误帧秒的总数量

·Event running total：表示错误帧秒事件的总数量

【相关命令】

·**reset** **oam**

**以太网OAM \-- 以太网OAM配置命令 \-- oam enable**

------------------------------------------------------------------------

**[oam** **enable**]命令用来使能以太网OAM功能。

**[undo** **oam** **enable**]命令用来关闭以太网OAM功能。

【命令】

**[oam** **enable**]

**[undo** **oam** **enable**]

【缺省情况】

以太网OAM功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在接口GigabitEthernet1/0/1上使能以太网OAM功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam enable

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame threshold**

------------------------------------------------------------------------

**[oam** **errored-frame** **threshold**]命令用来在接口上配置错误帧事件的检测阈值。

**[undo** **oam** **errored-frame** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-frame** **threshold** *threshold-value*]

**[undo** **oam** **errored-frame** **threshold**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误帧事件的检测阈值，取值范围为0～4294967295，单位为次。

【使用指导】

接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误帧事件的检测阈值为100次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-frame threshold 100

【相关命令】

·**display oam configuration**

·**display oam link-event**

·**oam** **global** **errored-frame** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame window**

------------------------------------------------------------------------

**[oam** **errored-frame** **window**]命令用来在接口上配置错误帧事件的检测窗口。

**[undo** **oam** **errored-frame** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-frame** **window** *window-value*]

**[undo** **oam** **errored-frame** **window**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误帧事件的检测窗口，取值范围为10～600，步长为10，单位为100毫秒。

【使用指导】

接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误帧事件的检测窗口为2000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-frame window 20

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **global** **errored-frame** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-period threshold**

------------------------------------------------------------------------

**[oam** **errored-frame-period** **threshold**]命令用来在接口上配置错误帧周期事件的检测阈值。

**[undo** **oam** **errored-frame-period** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-frame-period** **threshold** *threshold-value*]

**[undo** **oam** **errored-frame-period** **threshold**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误帧周期事件的检测阈值，取值范围为0～4294967295，单位为次。

【使用指导】

接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误帧周期事件的检测阈值为100次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-frame-period threshold 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **global** **errored-frame-period** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-period window**

------------------------------------------------------------------------

**[oam** **errored-frame-period** **window**]命令用来在接口上配置错误帧周期事件的检测窗口。

**[undo** **oam** **errored-frame-period** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-frame-period** **window** *window-value*]

**[undo** **oam** **errored-frame-period** **window**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误帧周期事件的检测窗口，取值范围为1～65535，单位为10000次。

【使用指导】

接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误帧周期事件的检测窗口为20000000次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-frame-period window 2000

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **global** **errored-frame-period** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-seconds threshold**

------------------------------------------------------------------------

**[oam** **errored-frame-seconds** **threshold**]命令用来在接口上配置错误帧秒事件的检测阈值。

**[undo** **oam** **errored-frame-seconds** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-frame-seconds** **threshold** *threshold-value*]

**[undo** **oam** **errored-frame-seconds** **threshold**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误帧秒事件的检测阈值，取值范围为0～900，单位为次。

【使用指导】

·在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。

·接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误帧秒事件的检测阈值为100次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-frame-seconds threshold 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame-seconds** **window**

·**oam** **global** **errored-frame-seconds** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-frame-seconds window**

------------------------------------------------------------------------

**[oam** **errored-frame-seconds** **window**]命令用来在接口上配置错误帧秒事件的检测窗口。

**[undo** **oam** **errored-frame-seconds** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-frame-seconds** **window** *window-value*]

**[undo** **oam** **errored-frame-seconds** **window**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误帧秒事件的检测窗口，取值范围为100～9000，步长为10，单位为100毫秒。

【使用指导】

·在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。

·接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误帧秒事件的检测窗口为10000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-frame-seconds window 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame-seconds** **threshold**

·**oam** **global** **errored-frame-seconds** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-symbol-period threshold**

------------------------------------------------------------------------

**[oam** **errored-symbol-period** **threshold**]命令用来在接口上配置错误信号事件的检测阈值。

**[undo** **oam** **errored-symbol-period** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-symbol-period** **threshold** *threshold-value*]

**[undo** **oam** **errored-symbol-period** **threshold**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误信号事件的检测阈值，取值范围为0～4294967295，单位为次。

【使用指导】

接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误信号事件的检测阈值为100次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-symbol-period threshold 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **global** **errored-symbol-period** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam errored-symbol-period window**

------------------------------------------------------------------------

**[oam** **errored-symbol-period** **window**]命令用来在接口上配置错误信号事件的检测窗口。

**[undo** **oam** **errored-symbol-period** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **errored-symbol-period** **window** *window-value*]

**[undo** **oam** **errored-symbol-period** **window**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误信号事件的检测窗口，取值范围为1～65535，单位为1000000次。

【使用指导】

接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置错误信号事件的检测值为200000000次。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam errored-symbol-period window 200

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **global** **errored-symbol-period** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame threshold**

------------------------------------------------------------------------

**[oam** **global** **errored-frame** **threshold**]命令用来全局配置错误帧事件的检测阈值。

**[undo** **oam** **global** **errored-frame** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-frame** **threshold** *threshold-value*]

**[undo** **oam** **global** **errored-frame** **threshold**]

【缺省情况】

错误帧事件检测阈值的全局值为1次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误帧事件的检测阈值，取值范围为0～4294967295，单位为次。

【使用指导】

全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误帧事件的检测阈值为100次。

\<Sysname\> system-view

Sysname oam global errored-frame threshold 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame window**

------------------------------------------------------------------------

**[oam** **global** **errored-frame** **window**]命令用来全局配置错误帧事件的检测窗口。

**[undo** **oam** **global** **errored-frame** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-frame** **window** *window-value*]

**[undo** **oam** **global** **errored-frame** **window**]

【缺省情况】

错误帧事件检测窗口的全局值为1000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误帧事件的检测窗口，取值范围为10～600，步长为10，单位为100毫秒。

【使用指导】

全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误帧事件的检测窗口配置为2000毫秒。

\<Sysname\> system-view

Sysname oam global errored-frame window 20

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-period threshold**

------------------------------------------------------------------------

**[oam** **global** **errored-frame-period** **threshold**]命令用来全局配置错误帧周期事件的检测阈值。

**[undo** **oam** **global** **errored-frame-period** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-frame-period** **threshold** *threshold-value*]

**[undo** **oam** **global** **errored-frame-period** **threshold**]

【缺省情况】

错误帧周期事件检测阈值的全局值为1次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误帧周期事件的检测阈值，取值范围为0～4294967295，单位为次。

【使用指导】

全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误帧周期事件的检测阈值为100次。

\<Sysname\> system-view

Sysname oam global errored-frame-period threshold 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame-period** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-period window**

------------------------------------------------------------------------

**[oam** **global** **errored-frame-period** **window**]命令用来全局配置错误帧周期事件的检测窗口。

**[undo** **oam** **global** **errored-frame-period** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-frame-period** **window** *window-value*]

**[undo** **oam** **global** **errored-frame-period** **window**]

【缺省情况】

错误帧周期事件检测窗口的全局值为10000000次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误帧周期事件的检测窗口，取值范围为1～65535，单位为10000次。

【使用指导】

全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误帧周期事件的检测窗口为20000000次。

\<Sysname\> system-view

Sysname oam global errored-frame-period window 2000

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame-period** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-seconds threshold**

------------------------------------------------------------------------

**[oam** **global** **errored-frame-seconds** **threshold**]命令用来全局配置错误帧秒事件的检测阈值。

**[undo** **oam** **global** **errored-frame-seconds** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-frame-seconds** **threshold** *threshold-value*]

**[undo** **oam** **global** **errored-frame-seconds** **threshold**]

【缺省情况】

错误帧秒事件检测阈值的全局值为1次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误帧秒事件的检测阈值，取值范围为0～900，单位为次。

【使用指导】

·在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。

·全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误帧秒事件的检测阈值配置为100次。

\<Sysname\> system-view

Sysname oam global errored-frame-seconds threshold 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame-seconds** **threshold**

·**oam** **global** **errored-frame-seconds** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-frame-seconds window**

------------------------------------------------------------------------

**[oam** **global** **errored-frame-seconds** **window**]命令用来全局配置错误帧秒事件的检测窗口。

**[undo** **oam** **global** **errored-frame-seconds** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-frame-seconds** **window** *window-value*]

**[undo** **oam** **global** **errored-frame-seconds** **window**]

【缺省情况】

错误帧秒事件检测窗口的全局值为60000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误帧秒事件的检测窗口，取值范围为100～9000，步长为10，单位为100毫秒。

【使用指导】

·在数量上，错误帧秒事件的检测阈值不应大于其检测窗口值（换算成秒），否则将不会产生错误帧秒事件。

·全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误帧秒事件的检测窗口为10000毫秒。

\<Sysname\> system-view

Sysname oam global errored-frame-seconds window 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-frame-seconds** **window**

·**oam** **global** **errored-frame-seconds** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-symbol-period threshold**

------------------------------------------------------------------------

**[oam** **global** **errored-symbol-period** **threshold**]命令用来全局配置错误信号事件的检测阈值。

**[undo** **oam** **global** **errored-symbol-period** **threshold**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-symbol-period** **threshold** *threshold-value*]

**[undo** **oam** **global** **errored-symbol-period** **threshold**]

【缺省情况】

错误信号事件检测阈值的全局值为1次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[threshold-value*]：表示错误信号事件的检测阈值，取值范围为0～4294967295，单位为次。

【使用指导】

全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误信号事件的检测阈值为100次。

\<Sysname\> system-view

Sysname oam global errored-symbol-period threshold 100

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-symbol-period** **threshold**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global errored-symbol-period window**

------------------------------------------------------------------------

**[oam** **global** **errored-symbol-period** **window**]命令用来全局配置错误信号事件的检测窗口。

**[undo** **oam** **global** **errored-symbol-period** **window**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **errored-symbol-period** **window** *window-value*]

**[undo** **oam** **global** **errored-symbol-period** **window**]

【缺省情况】

错误信号事件检测窗口的全局值为100000000。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[window-value*]：表示错误信号事件的检测窗口，取值范围为1～65535，单位为1000000次。

【使用指导】

全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置错误信号事件的检测窗口为200000000次。

\<Sysname\> system-view

Sysname oam global errored-symbol-period window 200

【相关命令】

·**display** **oam** **configuration**

·**display** **oam** **link-event**

·**oam** **errored-symbol-period** **window**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global timer hello**

------------------------------------------------------------------------

**[oam**]**global** **timer****hello**命令用来全局配置以太网OAM握手报文的发送间隔。

**[undo** **oam** **global** **timer** **hello**]命令用来恢复缺省情况。

【命令】

**[oam**] **global** **timer** **hello** *interval*

**[undo**] **oam** **global** **timer** **hello**

【缺省情况】

以太网OAM握手报文发送间隔的全局值为1000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示以太网OAM握手报文的发送间隔，单位为毫秒，步长为100，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·由于本端OAM实体在连接超时后将老化与远端OAM实体的连接关系，导致OAM连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网OAM连接不稳定。

·全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置以太网OAM握手报文的发送间隔为600毫秒。

\<Sysname\> system-view

Sysname oam global timer hello 600

【相关命令】

·**display** **oam** **configuration**

·**oam** **timer** **hello**

**以太网OAM \-- 以太网OAM配置命令 \-- oam global timer keepalive**

------------------------------------------------------------------------

**[oam** **global** **timer** **keepalive**]命令用来全局配置以太网OAM连接的超时时间。

**[undo** **oam** **global** **timer** **keepalive**]命令用来恢复缺省情况。

【命令】

**[oam** **global** **timer** **keepalive** *interval*]

**[undo** **oam** **global** **timer** **keepalive**]

【缺省情况】

以太网OAM连接超时时间的全局值为5000毫秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示以太网OAM连接的超时时间，单位为毫秒，步长为100，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·由于本端OAM实体在连接超时后将老化与远端OAM实体的连接关系，导致OAM连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网OAM连接不稳定。

·全局值对所有接口都有效，但配置优先级低于接口值。

【举例】

\# 全局配置以太网OAM连接的超时时间为6000毫秒。

\<Sysname\> system-view

Sysname oam globaltimer keepalive 6000

【相关命令】

·**display** **oam** **configuration**

·**oam** **timer** **keepalive**

**以太网OAM \-- 以太网OAM配置命令 \-- oam mode**

------------------------------------------------------------------------

**[oam** **mode**]命令用来配置以太网OAM的连接模式。

**[undo** **oam** **mode**]命令用来恢复缺省情况。

【命令】

**[oam**  **mode** { **active** \| **passive** }]

**[undo** **oam** **mode**]

【缺省情况】

以太网OAM连接模式为主动模式。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[active**]：表示主动模式。

**[passive**]：表示被动模式。

【使用指导】

不允许在已使能以太网OAM功能的接口上更改以太网OAM的连接模式。如需更改，请先关闭该接口上的以太网OAM功能。

【举例】

\# 在接口GigabitEthernet1/0/1上先关闭以太网OAM功能，再配置以太网OAM的连接模式为被动模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo oam enable

Sysname-GigabitEthernet1/0/1 oam mode passive

【相关命令】

·**oam** **enable**

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-failure action**

------------------------------------------------------------------------

**[oam** **remote-failure action**]命令用来配置接口收到远端以太网OAM事件时的响应动作。

**[undo oam** **remote-failure action**]命令用来恢复缺省情况。

【命令】

**[oam**[ **remote-failure** { **connection-expired** \| **critical-event** \| **dying-gasp** \| **link-fault** } **action** **error-link-down**]]

**[undo**[ **oam** **remote-failure** { **connection-expired** \| **critical-event** \| **dying-gasp** \| **link-fault** } **action** **error-link-down**]]

【缺省情况】

接口收到远端以太网OAM事件时仅记录日志。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[connection-expired**]：表示以太网OAM连接超时。

**[critical-event**]：表示紧急事件。

**[dying-gasp**]：表示致命故障。

**[link-fault**]：表示链路故障。

**[error-link-down**]：表示断开OAM连接，并设置接口的链路层状态为down。

【举例】

\# 配置接口GigabitEthernet1/0/1收到远端致命故障时的响应动作为断开OAM连接，并设置该接口的链路层状态为down。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam remote-failure dying-gasp action error-link-down

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-loopback**

------------------------------------------------------------------------

**[oam** **remote-loopback** **start**]命令用来使能当前接口的以太网OAM远端环回功能。

**[oam** **remote-loopback** **stop**]命令用来关闭当前接口的以太网OAM远端环回功能。

【命令】

**[oam** **remote-loopback** **start**]

**[oam** **remote-loopback** **stop**]

【缺省情况】

以太网OAM远端环回功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·只有当接口上的以太网OAM连接已建立完成，且以太网OAM的连接模式为主动模式时，才允许在该接口上使能以太网OAM远端环回功能。

·用户既可在用户视图或系统视图下使能指定接口的以太网OAM远端环回功能，也可在接口视图下使能当前接口的以太网OAM远端环回功能，三者的配置效果相同。

【举例】

\# 配置接口GigabitEthernet1/0/1的以太网OAM的连接模式为主动模式并使能其以太网OAM功能，然后在该接口视图下使能其以太网OAM远端环回功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam mode active

Sysname-GigabitEthernet1/0/1 oam enable

Sysname-GigabitEthernet1/0/1 oam remote-loopback start

【相关命令】

·**oam** **enable**

·**oam** **mode**

·**oam** **remote-loopback** **interface**

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-loopback interface**

------------------------------------------------------------------------

**[oam** **remote-loopback** **start** **interface**]命令用来使能指定接口的以太网OAM远端环回功能。

**[oam** **remote-loopback** **stop** **interface**]命令用来关闭指定接口的以太网OAM远端环回功能。

【命令】

**[oam** **remote-loopback** **start** **interface** *interface-type interface-number*]

**[oam** **remote-loopback** **stop** **interface** *interface-type interface-number*]

【缺省情况】

以太网OAM远端环回功能处于关闭状态。

【视图】

用户视图/系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：表示接口类型和接口编号。

【使用指导】

·只有当接口上的以太网OAM连接已建立完成，且以太网OAM的连接模式为主动模式时，才允许在该接口上使能以太网OAM远端环回功能。

·用户既可在用户视图或系统视图下使能指定接口的以太网OAM远端环回功能，也可在接口视图下使能当前接口的以太网OAM远端环回功能，三者的配置效果相同。

【举例】

\# 配置接口GigabitEthernet1/0/1的以太网OAM的连接模式为主动模式并使能其以太网OAM功能，然后在系统视图下使能该接口的以太网OAM远端环回功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam mode active

Sysname-GigabitEthernet1/0/1 oam enable

Sysname-GigabitEthernet1/0/1 quit

Sysname oam remote-loopback start interface gigabitethernet 1/0/1

【相关命令】

·**oam** **enable**

·**oam** **mode**

·**oam** **remote-loopback**

**以太网OAM \-- 以太网OAM配置命令 \-- oam remote-loopback reject-request**

------------------------------------------------------------------------

**[oam** **remote-loopback** **reject-request**]命令用来配置接口拒绝远端发起的以太网OAM远端环回。

**[undo** **oam** **remote-loopback** **reject-request**]命令用来恢复缺省情况。

【命令】

**[oam** **remote-loopback** **reject-request**]

**[undo** **oam** **remote-loopback** **reject-request**]

【缺省情况】

接口不拒绝远端发起的以太网OAM远端环回。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在执行**oam remote-loopback reject-request**命令时若接口已处于环回状态，则该配置将从下次环回开始时生效。

【举例】

\# 配置接口GigabitEthernet1/0/1拒绝远端发起的以太网OAM远端环回。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam remote-loopback reject-request

**以太网OAM \-- 以太网OAM配置命令 \-- oam timer hello**

------------------------------------------------------------------------

**[oam** **timer** **hello**]命令用来在接口上配置以太网OAM握手报文的发送间隔。

**[undo** **oam** **timer** **hello**]命令用来恢复缺省情况。

【命令】

**[oam**] **timer** **hello** *interval*

**[undo**] **oam** **timer** **hello**

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示以太网OAM握手报文的发送间隔，单位为毫秒，步长为100，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·由于本端OAM实体在连接超时后将老化与远端OAM实体的连接关系，导致OAM连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网OAM连接不稳定。

·接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置以太网OAM握手报文的发送间隔为600毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam timer hello 600

【相关命令】

·**display** **oam** **configuration**

·**oam** **global** **timer** **hello**

**以太网OAM \-- 以太网OAM配置命令 \-- oam timer keepalive**

------------------------------------------------------------------------

**[oam** **timer** **keepalive**]命令用来在接口上配置以太网OAM连接的超时时间。

**[undo** **oam** **timer** **keepalive**]命令用来恢复缺省情况。

【命令】

**[oam** **timer** **keepalive** *interval*]

**[undo** **oam** **timer** **keepalive**]

【缺省情况】

接口采用全局值。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示以太网OAM连接的超时时间，单位为毫秒，步长为100，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·由于本端OAM实体在连接超时后将老化与远端OAM实体的连接关系，导致OAM连接中断，因此连接超时时间必须大于握手报文发送间隔（建议为五倍或以上），否则将导致以太网OAM连接不稳定。

·接口值只对当前接口有效，但配置优先级高于全局值。

【举例】

\# 在接口GigabitEthernet1/0/1上配置以太网OAM连接的超时时间为6000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 oam timer keepalive 6000

【相关命令】

·**display** **oam** **configuration**

·**oam** **global** **timer** **keepalive**

**以太网OAM \-- 以太网OAM配置命令 \-- reset oam**

------------------------------------------------------------------------

**[reset** **oam**]命令用来清除以太网OAM的报文和一般链路事件统计信息。

【命令】

**[reset** **oam** [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：清除指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将清除所有接口上的信息。

【举例】

\# 清除所有接口上以太网OAM的报文和一般链路事件统计信息。

\<Sysname\> reset oam

【相关命令】

·**display** **oam**

·**display** **oam** **link-event**
