
**RRPP \-- RRPP配置命令 \-- control-vlan**

------------------------------------------------------------------------

**[control-vlan**]命令用来配置RRPP域的主控制VLAN。

**[undo** **control-vlan**]命令用来删除RRPP域的主控制VLAN。

【命令】

**[control-vlan*** vlan-id*]

**[undo** **control-vlan**]

【缺省情况】

RRPP域不存在任何控制VLAN。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：主控制VLAN的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·用户只需配置主控制VLAN，子控制VLAN由系统自动分配，其VLAN ID为主控制VLAN的VLAN ID＋1。因此，在配置控制VLAN时请选取两个连续的、尚未创建的VLAN，否则将导致配置失败。

·请勿将接入RRPP环的端口的缺省VLAN配置为控制VLAN，而且控制VLAN内不能运行QinQ和VLAN映射功能，否则RRPP协议报文将无法正常收发。

·配置好RRPP环之后不再允许用户删除或修改主控制VLAN。主控制VLAN只能通过**undo** **control-vlan**命令删除，不能通过**undo** **vlan**命令删除。

【举例】

\# 假设VLAN 100和VLAN 101都是尚未创建的VLAN，配置VLAN 100为RRPP域1的主控制VLAN。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 control-vlan 100

**RRPP \-- RRPP配置命令 \-- display rrpp brief**

------------------------------------------------------------------------

**[display** **rrpp** **brief**]命令用来显示RRPP的摘要信息。

【命令】

**[display**] **rrpp** **brief**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示RRPP的摘要信息。

\<Sysname\> display rrpp brief

 Flags for node mode: M --- Master, T \-- Transit, E \-- Edge, A \-- Assistant-edge

 RRPP protocol status: Enabled

 Domain ID     : 1

 Control VLAN  : Primary 5, Secondary 6

 Protected VLAN: Reference instance 0 to 2, 4

Hello timer   : 1 seconds, Fail timer: 3 seconds

Fast detection status: Disabled

 Fast-Hello timer: 20 ms, Fast-Fail timer: 60 ms

 Fast-Edge-Hello timer: 10 ms, Fast-Edge-Fail timer: 30 ms

Ring  Ring   Node  Primary/Common            Secondary/Edge            Enable

  ID    level  mode  port                      port                      status

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  1     1      M     GE1/0/1                   GE1/0/2                   Yes

 Domain ID     : 2

 Control VLAN  : Primary 10, Secondary 11

 Protected VLAN: Reference instance 0 to 2, 4

 Hello timer   : 1 seconds, Fail timer: 3 seconds

Fast detection status: Disabled

Fast-Hello timer: 10 ms, Fast-Fail timer: 30 ms

Ring  Ring   Node  Primary/Common            Secondary/Edge            Enable

  ID    level  mode  port                      port                      status

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\-\-\-\--

1     0      T     GE1/0/3                   GE1/0/4                   Yes

  2     1      E     GE1/0/3                   GE1/0/5                   Yes

                     GE1/0/4

表1-1 display rrpp brief命令显示信息描述表

字段

描述

Flags for node mode

RRPP的节点角色：

·M：代表主节点

·T：代表传输节点

·E：代表边缘节点

·A：代表辅助边缘节点

RRPP protocol status

RRPP协议的全局使能状态：

·Enabled：表示全局使能

·Disabled：表示全局未使能

Domain ID

RRPP域的ID

Control VLAN

RRPP域的控制VLAN：

·Primary：表示主控制VLAN

·Secondary：表示子控制VLAN

Protected VLAN

RRPP域的保护VLAN所对应的MSTI（Multiple Spanning Tree Instance，多生成树实例）。VLAN与MSTI的映射关系可通过命令**display** **stp** **region-configuration**（请参见"二层技术-以太网交换命令参考/生成树"）查看

Hello timer

Hello定时器的值，单位为秒

Fail timer

Fail定时器的值，单位为秒

Fast detection status

快速检测功能的使能状态：

·Enabled：表示使能

·Disabled：表示未使能

Fast-Hello timer

Fast-Hello定时器的值，单位为毫秒

Fast-Fail timer

Fast-Fail定时器的值，单位为毫秒

Fast-Edge-Hellotimer

Fast-Edge-Hello定时器的值，单位为毫秒

Fast-Edge-Fail timer

Fast-Edge-Fail定时器的值，单位为毫秒

Ring ID

RRPP环的ID

Ring level

RRPP环的级别：

·0：表示主环

·1：表示子环

Node mode

设备的节点角色

Primary/Common port

·当节点角色为主节点或传输节点时，该字段表示主端口

·当节点角色为边缘节点或辅助边缘节点时，该字段表示公共端口

·当环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口时，该字段显示为"-"

Secondary/Edge port

·当节点角色为主节点或传输节点时，该字段表示副端口

·当节点角色为边缘节点或辅助边缘节点时，该字段表示边缘端口

·当环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口时，该字段显示为"-"

Enable status

当前RRPP环的使能状态：

·Yes：表示使能

·No：表示未使能

**RRPP \-- RRPP配置命令 \-- display rrpp ring-group**

------------------------------------------------------------------------

**[display** **rrpp** **ring-group** ]命令用来显示RRPP环组的配置信息。

【命令】

**[display** **rrpp** **ring-group** [ *ring-group-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ring-group-id*]：显示指定RRPP环组的配置信息，*ring-group-id*为RRPP环组的ID，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，将显示所有RRPP环组的配置信息。

【使用指导】

如果是边缘节点的RRPP环组，还会显示当前发送Edge-Hello报文的环。

【举例】

\# 显示所有RRPP环组的配置信息。

\<Sysname\> display rrpp ring-group

 Ring group 1:

  Domain 1 ring 1 to 3, 5

  Domain 2 ring 1 to 3, 5

  Domain 1 ring 1 is the sending ring

 Ring group 2:

  Domain 1 ring 4, 6 to 7

  Domain 2 ring 4, 6 to 7

表1-2 display rrpp ring-group命令显示信息描述表

字段

描述

Ring group 1

RRPP环组1

Domain 1 ring 1 to 3, 5

该环组的子环成员有RRPP域1的环1、2、3和5

Domain 1 ring 1 is the sending ring

该环组的发送环为RRPP域1的环1

**RRPP \-- RRPP配置命令 \-- display rrpp statistics**

------------------------------------------------------------------------

**[display** **rrpp** **statistics**]命令用来显示RRPP报文的统计信息。

【命令】

**[display**] **rrpp** **statistics** **domain** *domain-id* [ **ring** *ring-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[domain**]*domain-id*：RRPP域的ID，取值范围为1～128。

**[ring**]*ring-id*：显示指定环的RRPP报文统计信息。*ring-id*为RRPP环的ID，取值范围为1～128。如果未指定本参数，将显示该域中所有环的RRPP报文统计信息。

【使用指导】

·如果某端口属于多个环，那么其报文将按环分别计数，用户看到的报文统计信息为该端口在当前环下的报文统计。

·当环由未激活状态进入激活状态时，报文统计将重新开始计数。

【举例】

\# 显示RRPP域2中所有环的RRPP报文统计信息。

\<Sysname\> display rrpp statistics domain 2

 Ring ID       : 1

 Ring level    : 0

 Node mode     : Master

 Active status : Yes

 Primary port  : GE1/0/3

 Fast-Hello packets: 0 Sent, 0 Received

 Fast-Edge-Hello packets: 0 Sent, 0 Received

  Direct Hello     Link     Common     Complete   Edge      Major     Total

                   down     flush FDB  flush FDB  hello     fault

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Out    16924     0        0          1          0         0         16925

  In     0         0        0          0          0         0         0

 Secondary port: GE1/0/4

 Fast-Hello packets: 0 Sent, 0 Received

 Fast-Edge-Hello packets: 0 Sent, 0 Received

  Direct Hello     Link     Common     Complete   Edge      Major     Total

                   down     flush FDB  flush FDB  hello     fault

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Out    0         0        0          0          0         0         0

  In     16878     0        0          1          0         0         16879

 Ring ID       : 2

 Ring level    : 1

 Node mode     : Edge

 Active status : No

 Common port   : GE1/0/3

 Fast-Hello packets: 0 Sent, 0 Received

 Fast-Edge-Hello packets: 0 Sent, 0 Received

  Direct Hello     Link     Common     Complete   Edge      Major     Total

                   down     flush FDB  flush FDB  hello     fault

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Out    0         0        0          0          0         0         0

  In     0         0        0          0          0         0         0

 Common port   : GE1/0/4

 Fast-Hello packets: 0 Sent, 0 Received

 Fast-Edge-Hello packets: 0 Sent, 0 Received

  Direct Hello     Link     Common     Complete   Edge      Major     Total

                   down     flush FDB  flush FDB  hello     fault

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Out    0         0        0          0          0         0         0

  In     0         0        0          0          0         0         0

 Edge port     : GE1/0/5

  Direct Hello     Link     Common     Complete   Edge      Major     Total

                   down     flush FDB  flush FDB  hello     fault

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\-\-\-\-\--

  Out    0         0        0          0          0         0         0

  In     0         0        0          0          0         0         0

表1-3 display rrpp statistics命令显示信息描述表

字段

描述

Ring ID

RRPP环的ID

Ring level

RRPP环的级别：

·0：表示主环

·1：表示子环

Node mode

设备的节点角色：

·Master：主节点

·Transit：传输节点

·Edge：边缘节点

·Assistant-edge：辅助边缘节点

Active status

RRPP环的激活状态：

·Yes：表示激活

·No：表示未激活

Primary port

主端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"，下面也不会有相应的报文统计信息

Secondary port

副端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"，下面也不会有相应的报文统计信息

Common port

公共端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"，下面也不会有相应的报文统计信息

Edge port

边缘端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"，下面也不会有相应的报文统计信息

Fast-Hello packets

端口上Fast-Hello报文的统计信息：

·Sent：表示发送报文的统计

·Received：表示接收报文的统计

Fast-Edge-Hello packets

端口上Fast-Edge-Hello报文的统计信息：

·Sent：表示发送报文的统计

·Received：表示接收报文的统计

Packet direct

端口上报文的传播方向：

·Out：表示发送

·In：表示接收

Hello

端口收发的Hello报文统计信息

Link down

端口收发的Link-Down报文统计信息

Common flush FDB

端口收发的Common-Flush-FDB报文统计信息

Complete flush FDB

端口收发的Complete-Flush-FDB报文统计信息

Edge hello

端口收发的Edge-Hello报文统计信息

Major fault

端口收发的Major-Fault报文统计信息

Total

端口收发的报文总数信息。这里只统计RRPP的Hello报文、Link-Down报文、Common-Flush-FDB报文、Complete-Flush-FDB报文、Edge-Hello报文和Major-Fault报文，其它种类的报文不统计

【相关命令】

·**reset** **rrpp** **statistics**

**RRPP \-- RRPP配置命令 \-- display rrpp verbose**

------------------------------------------------------------------------

**[display** **rrpp** **verbose**]命令用来显示RRPP的详细信息。

【命令】

**[display** **rrpp** **verbose** **domain** *domain-id* [ **ring** *ring-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[domain** *domain-id*]：RRPP域的ID，取值范围为1～128。

**[ring** *ring-id*]：显示指定环的RRPP详细信息。*ring-id*为RRPP环的ID，取值范围为1～128。如果未指定本参数，将显示该域中所有环的RRPP详细信息。

【举例】

\# 显示RRPP域2中所有环的RRPP详细信息。

\<Sysname\> display rrpp verbose domain 2

 Domain ID     : 2

 Control VLAN  : Primary 10, Secondary 11

 Protected VLAN: Reference instance 3, 5 to 7

Hello timer   : 1 seconds, Fail timer: 3 seconds

Fast detection status: Disabled

Fast-Hello timer: 20 ms, Fast-Fail timer: 60 ms

Fast-Edge-Hello timer: 10 ms, Fast-Edge-Fail timer: 30 ms

Ring ID       : 1

 Ring level    : 0

 Node mode     : Master

 Ring state    : Completed

 Enable status : Yes, Active status: Yes

 Primary port  : GE1/0/4                    Port status: UP

 Secondary port: GE1/0/5                    Port status: BLOCKED

 Ring ID       : 2

 Ring level    : 1

 Node mode     : Edge

 Ring state    : -

 Enable status : No, Active status: No

Common port   : GE1/0/4                    Port status: -

                 GE1/0/5                    Port status: -

Edge port     : GE1/0/3                    Port status: -

表1-4 display rrpp verbose命令显示信息描述表

字段

描述

Domain ID

RRPP域的ID

Control VLAN

RRPP域的控制VLAN：

·Primary：主控制VLAN

·Secondary：子控制VLAN

Protected VLAN

RRPP域的保护VLAN所对应的MSTI。VLAN与MSTI的映射关系可通过命令**display** **stp** **region-configuration**（请参见"二层技术-以太网交换命令参考/生成树"）查看

Hello timer

Hello定时器的值，单位为秒

Fail timer

Fail定时器的值，单位为秒

Fast detection status

快速检测功能的使能状态：

·Enabled：表示使能

·Disabled：表示未使能

Fast-Hello timer

Fast-Hello定时器的值，单位为毫秒

Fast-Fail timer

Fast-Fail定时器的值，单位为毫秒

Fast-Edge-Hello timer

Fast-Edge-Hello定时器的值，单位为毫秒

Fast-Edge-Fail timer

Fast-Edge-Fail定时器的值，单位为毫秒

Ring ID

RRPP环的ID

Ring level

RRPP环的级别：

·0：表示主环

·1：表示子环

Node mode

设备的节点角色：

·Master：主节点

·Transit：传输节点

·Edge：边缘节点

·Assistant-edge：辅助边缘节点

Ring state

当前RRPP环的状态：

·Completed：表示健康状态

·Failed：表示断裂状态

·在非主节点上，或当主节点上的环未使能时将显示为"-"

Enable status

当前RRPP环的使能状态：

·Yes：表示使能

·No：表示未使能

Active status

当前RRPP环的激活状态，可通过该字段状态了解RRPP协议和当前RRPP环的激活情况，必须同时使能RRPP协议和当前RRPP环，该环才能处于激活状态：

·Yes：表示激活

·No：表示未激活

Primary port

主端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"

Secondary port

副端口，说明此节点角色为主节点或传输节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"

Common port

公共端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"

Edge port

边缘端口，说明此节点角色为边缘节点或辅助边缘节点。如果环上未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"

Port status

端口状态，共有3种取值：DOWN、UP和BLOCKED；如果环处于未激活状态、未配置该端口、该端口所在单板未启动或该端口为聚合组成员端口，该字段显示为"-"

**RRPP \-- RRPP配置命令 \-- domain ring**

------------------------------------------------------------------------

**[domain** **ring**]命令用来配置RRPP环组内的子环。

**[undo** **domain** **ring**]命令用来删除RRPP环组内的子环。

【命令】

**[domain** *domain-id* **ring** *ring-id-list*]

**[undo**] **domain** *domain-id* [ **ring** *ring-id-list* ]

【缺省情况】

RRPP环组内不存在任何子环。

【视图】

RRPP环组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id*]：RRPP域的ID，取值范围为1～128。

**[ring*** ring-id-list*]：RRPP子环的ID列表。*ring-id-list* = { *ring-id* [ **to** *ring-id*  }&\<1-10\>]。其中，*ring-id*为RRPP子环的ID号，取值范围为1～128。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，将删除该域已加入环组的所有子环。

【使用指导】

进行下列操作时应按规定顺序进行，否则辅助边缘节点可能会因收不到Edge-Hello报文而误认为主环故障：

·将激活的环加入环组时，应先在辅助边缘节点将环加入环组，再在边缘节点将环加入环组。

·将激活的环从环组中删除时，应先在边缘节点将环从环组中删除，再在辅助边缘节点将环从环组中删除。

·将整个环组删除时，应先在边缘节点删除环组，再在辅助边缘节点删除环组。

·将环组中的环激活时，应先激活边缘节点环组中的环，再激活辅助边缘节点环组中的环。

·将环组中的环解除激活时，应先解除激活辅助边缘节点环组中的环，再解除激活边缘节点环组中的环。

【举例】

\# 创建RRPP环组1，并将子环1、2、3和5都加入到域1和域2中。

\<Sysname\> system-view

Sysname rrpp ring-group 1

Sysname-ring-group1 domain 1 ring 1 to 3 5

Sysname-ring-group1 domain 2 ring 1 to 3 5

【相关命令】

·**display** **rrpp** **ring-group**

·**rrpp** **ring-group**

**RRPP \-- RRPP配置命令 \-- fast-detection enable**

------------------------------------------------------------------------

**[fast-detection**] **enable**命令用来使能RRPP域的快速检测功能。

**[undo**]**fast-detection** **enable**命令用来关闭RRPP域的快速检测功能。

【命令】

**[fast-detection**] **enable**

**[undo**]**fast-detection****enable**

【缺省情况】

RRPP域的快速检测功能处于关闭状态。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·必须同时使能RRPP域的快速检测功能、RRPP协议和RRPP环，RRPP域的快速检测功能才会生效。

·使能RRPP域的快速检测功能时，请先在边缘节点上使能、再在辅助边缘节点上使能，否则辅助边缘节点可能会因收不到Fast-Edge-Hello报文而误认为主环故障。

【举例】

\# 使能RRPP域1的快速检测功能。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 fast-detection enable

【相关命令】

·**ring** **enable**

·**rrpp** **enable**

**RRPP \-- RRPP配置命令 \-- fast-edge-timer**

------------------------------------------------------------------------

**[fast-edge-timer**]命令用来配置Fast-Edge-Hello和Fast-Edge-Fail定时器。

**[undo** **fast-edge-timer**]命令用来恢复缺省情况。

【命令】

**[fast-edge-timer** **hello-timer** *hello-value* **fail-timer** *fail-value*]

**[undo** **fast-edge-timer**]

【缺省情况】

Fast-Edge-Hello定时器为10毫秒，Fast-Edge-Fail定时器为30毫秒。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hello-timer** *hello-value*]：Fast-Edge-Hello定时器的值，取值范围为5～100，单位为毫秒。

**[fail-timer*** fail-value*]：Fast-Edge-Fail定时器的值，取值范围为15～300，单位为毫秒。

【使用指导】

Fast-Edge-Fail定时器不得小于Fast-Edge-Hello定时器的3倍。

【举例】

\# 配置RRPP域1的Fast-Edge-Hello定时器为20毫秒，Fast-Edge-Fail定时器为70毫秒。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 fast-edge-timer hello-timer 20 fail-timer 70

**RRPP \-- RRPP配置命令 \-- fast-timer**

------------------------------------------------------------------------

**[fast-timer**]命令用来配置Fast-Hello和Fast-Fail定时器。

**[undo** **fast-timer**]命令用来恢复缺省情况。

【命令】

**[fast-timer** **hello-timer** *hello-value* **fail-timer** *fail-value*]

**[undo** **fast-timer**]

【缺省情况】

Fast-Hello定时器为20毫秒，Fast-Fail定时器为60毫秒。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hello-timer** *hello-value*]：Fast-Hello定时器的值，取值范围为10～500，单位为毫秒。

**[fail-timer*** fail-value*]：Fast-Fail定时器的值，取值范围为30～1500，单位为毫秒。

【使用指导】

Fast-Fail定时器不得小于Fast-Hello定时器的3倍。

【举例】

\# 配置RRPP域1的Fast-Hello定时器为20毫秒，Fast-Fail定时器为70毫秒。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 fast-timer hello-timer 20 fail-timer 70

**RRPP \-- RRPP配置命令 \-- protected-vlan**

------------------------------------------------------------------------

**[protected-vlan**]命令用来配置RRPP域的保护VLAN。

**[undo** **protected-vlan**]命令用来删除RRPP域的保护VLAN。

【命令】

**[protected-vlan** **reference-instance** *instance-id-list*]

**[undo** **protected-vlan** [ **reference-instance** *instance-id-list* ]]

【缺省情况】

RRPP域不保护任何VLAN。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reference-instance*** instance-id-list*]：RRPP域的保护VLAN对应的MSTI。*instance-id-list*为MSTI列表，表示方式为*instance-id-list *= { *instance-id* [ **to** *instance-id*  }&\<1-10\>]。其中，*instance-id*为MSTI的编号，取值范围为0～4094。&\<1-10\>表示前面的参数最多可以输入10次。VLAN与MSTI的映射关系可通过命令**display** **stp** **region-configuration**查看。如果未指定本参数，将删除RRPP域引用的所有MSTI。

【使用指导】

·配置RRPP环之前，可删除或修改已配置好的保护VLAN；配置RRPP环之后，也允许删除或修改已配置好的保护VLAN，但不允许将该域内所有保护VLAN的相关配置都删除。

·若VLAN与MSTI的映射关系发生变化，RRPP域实际保护的VLAN也会随之改变。

【举例】

\# 先将VLAN 1～30映射到MSTI 1上，并激活MST域的配置；然后配置RRPP域1的主控制VLAN为VLAN 100、保护VLAN为MSTI 1所映射的VLAN。

\<Sysname\> system-view

Sysname stp region-configuration

Sysname-mst-region instance 1 vlan 1 to 30

Sysname-mst-region active region-configuration

Sysname-mst-region quit

Sysname rrpp domain 1

Sysname-rrpp-domain1 control-vlan 100

Sysname-rrpp-domain1 protected-vlan reference-instance 1

【相关命令】

·**display** **stp** **region-configuration**（二层技术-以太网交换命令参考/生成树）

·**rrpp** **domain**

**RRPP \-- RRPP配置命令 \-- reset rrpp statistics**

------------------------------------------------------------------------

**[reset** **rrpp** **statistics**]命令用来清除RRPP报文的统计信息。

【命令】

**[reset**] **rrpp** **statistics** **domain** *domain-id* [ **ring** *ring-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain**]*domain-id*：RRPP域的ID，取值范围为1～128。

**[ring**]*ring-id*：清除指定环的RRPP报文统计信息。*ring-id*为RRPP环的ID，取值范围为1～128。如果未指定本参数，将清除该域中所有环的RRPP报文统计信息。

【举例】

\# 清除RRPP域1中环10的RRPP报文统计信息。

\<Sysname\> reset rrpp statistics domain 1 ring 10

【相关命令】

·**display** **rrpp** **statistics**

**RRPP \-- RRPP配置命令 \-- ring**

------------------------------------------------------------------------

**[ring**]命令用来配置当前设备的节点角色、RRPP端口以及环的级别。

**[undo** **ring**]命令用来删除RRPP环。

【命令】

**[ring**[ *ring-id* **node-mode** { { **master** \| **transit** } [ **primary-port** *interface-type interface-number* ]  **secondary-port** *interface-type interface-number*  **level** *level-value \|* { **assistant-edge** \| **edge** }  **edge-port** *interface-type interface-number*  }]]

**[undo** **ring** *ring-id*]

【缺省情况】

设备不是RRPP环的节点。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ring-id*]：RRPP环的ID，取值范围为1～128。

**[master**]：指定当前设备为RRPP环的主节点。

**[transit**]：指定当前设备为RRPP环的传输节点。

**[primary-port**]：指定本节点的主端口。

*[interface-type interface-number*]：指定端口类型和端口编号。

**[secondary-port**]：指定本节点的副端口。

**[level***level-value*]：RRPP环的级别，取值为0或1，0表示主环，1表示子环。

**[assistant-edge**]：指定当前设备为RRPP环的辅助边缘节点。

**[edge**]：指定当前设备为RRPP环的边缘节点。

**[edge-port**]：指定本节点的边缘端口。

【使用指导】

·同一RRPP域中不同的RRPP环不能使用相同的环ID。

·当RRPP环处于激活状态时不能配置RRPP端口。

·在配置边缘节点和辅助边缘节点时，必须先配置主环再配置子环。

·RRPP环的节点角色、RRPP端口以及环的级别一经配置就不能修改，若要改变这些配置，必须先删除原有配置。

·删除边缘节点或辅助边缘节点的主环配置之前，必须先删除所有的子环配置。但是，处于激活状态的RRPP环不能被删除。

·当设备上的RRPP协议已使能时，必须先关闭RRPP环才能删除该环；当设备上的RRPP协议未使能时，可以直接删除RRPP环，且该环的使能配置将被一并清除。

【举例】

\# 配置当前设备为RRPP域1中主环10的主节点，主端口为GigabitEthernet1/0/1，副端口为GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 control-vlan 100

Sysname-rrpp-domain1 protected-vlan reference-instance 0 1 2

Sysname-rrpp-domain1 ring 10 node-mode master primary-port gigabitethernet 1/0/1 secondary-port gigabitethernet 1/0/2 level 0

\# 先配置当前设备为RRPP域1中主环10的传输节点，主端口为GigabitEthernet1/0/1，副端口为GigabitEthernet1/0/2；再配置当前设备为RRPP域1中子环20的边缘节点，边缘端口为GigabitEthernet1/0/3。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 control-vlan 100

Sysname-rrpp-domain1 protected-vlan reference-instance 0 1 2

Sysname-rrpp-domain1 ring 10 node-mode transit primary-port gigabitethernet 1/0/1 secondary-port gigabitethernet 1/0/2 level 0

Sysname-rrpp-domain1 ring 20 node-mode edge edge-port gigabitethernet 1/0/3

【相关命令】

·**ring** **enable**

**RRPP \-- RRPP配置命令 \-- ring enable**

------------------------------------------------------------------------

**[ring**] **enable**命令用来使能RRPP环。

**[undo**] **ring** **enable**命令用来关闭RRPP环。

【命令】

**[ring**] *ring-id* **enable**

**[undo**] **ring** *ring-id* **enable**

【缺省情况】

RRPP环处于关闭状态。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ring-id*]：RRPP环的ID，取值范围为1～128。

【使用指导】

只有当RRPP协议和RRPP环都使能后，当前设备的RRPP环才能激活。

在一台设备上使能子环之前必须先使能主环，而关闭主环之前也必须先关闭所有子环，否则系统将提示出错。

【举例】

\# 使能RRPP域1的RRPP环10。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 control-vlan 100

Sysname-rrpp-domain1 protected-vlan reference-instance 0 1 2

Sysname-rrpp-domain1 ring 10 node-mode master primary-port gigabitethernet 1/0/1 secondary-port gigabitethernet 1/0/2 level 0

Sysname-rrpp-domain1 ring 10 enable

【相关命令】

·**rrpp** **enable**

**RRPP \-- RRPP配置命令 \-- rrpp domain**

------------------------------------------------------------------------

**[rrpp** **domain**]命令用来创建RRPP域，并进入RRPP域视图。

**[undo** **rrpp** **domain**]命令用来删除RRPP域。

【命令】

**[rrpp** **domain** *domain-id*]

**[undo** **rrpp** **domain** *domain-id*]

【缺省情况】

不存在任何RRPP域。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id*]：RRPP域的ID，取值范围为1～128。

【使用指导】

·删除RRPP域时，将同时删除该域所有控制VLAN和保护VLAN的相关配置。

·删除RRPP域时，必须保证该RRPP域内尚未配置RRPP环，否则将导致删除失败。

【举例】

\# 创建RRPP域1，并进入RRPP域1的视图。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1

【相关命令】

·**control-vlan**

·**protected-vlan**

**RRPP \-- RRPP配置命令 \-- rrpp enable**

------------------------------------------------------------------------

**[rrpp** **enable**]命令用来使能RRPP协议。

**[undo** **rrpp** **enable**]命令用来关闭RRPP协议。

【命令】

**[rrpp**] **enable**

**[undo** **rrpp** **enable**]

【缺省情况】

RRPP协议处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有当RRPP协议和RRPP环都使能后，当前设备的RRPP域才能激活。

【举例】

\# 使能RRPP协议。

\<Sysname\> system-view

Sysname rrpp enable

【相关命令】

·**ring** **enable**

**RRPP \-- RRPP配置命令 \-- rrpp ring-group**

------------------------------------------------------------------------

**[rrpp** **ring-group**]命令用来创建RRPP环组，并进入RRPP环组视图。

**[undo** **rrpp** **ring-group**]命令用来删除RRPP环组。

【命令】

**[rrpp** **ring-group** *ring-group-id*]

**[undo** **rrpp** **ring-group** *ring-group-id*]

【缺省情况】

不存在任何RRPP环组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ring-group-id*]：RRPP环组的ID，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·删除环组时，应先删除边缘节点环组，再删除辅助边缘节点环组，否则辅助边缘节点可能会因收不到Edge-Hello报文而误认为主环故障。

·删除环组后，原环组内的所有子环不再属于任何环组。

【举例】

\# 创建RRPP环组1，并进入RRPP环组1的视图。

\<Sysname\> system-view

Sysname rrpp ring-group 1

Sysname-ring-group1

【相关命令】

·**display** **rrpp** **ring-group**

·**domain** **ring**

**RRPP \-- RRPP配置命令 \-- timer**

------------------------------------------------------------------------

**[timer**]命令用来配置Hello和Fail定时器。

**[undo** **timer**]命令用来恢复缺省情况。

【命令】

**[timer** **hello-timer** *hello-value* **fail-timer** *fail-value*]

**[undo** **timer**]

【缺省情况】

Hello定时器为1秒，Fail定时器为3秒。

【视图】

RRPP域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hello-timer** *hello-value*]：Hello定时器的值，取值范围为1～10，单位为秒。

**[fail-timer*** fail-value*]：Fail定时器的值，取值范围为3～30，单位为秒。

【使用指导】

Fail定时器不得小于Hello定时器的3倍。

【举例】

\# 配置RRPP域1的Hello定时器为2秒，Fail定时器为7秒。

\<Sysname\> system-view

Sysname rrpp domain 1

Sysname-rrpp-domain1 timer hello-timer 2 fail-timer 7
