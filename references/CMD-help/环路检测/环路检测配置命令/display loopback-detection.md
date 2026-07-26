
**环路检测 \-- 环路检测配置命令 \-- display loopback-detection**

------------------------------------------------------------------------

**[display loopback-detection**]命令用来显示环路检测的配置和运行情况。

【命令】

**[display loopback-detection**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示环路检测的配置和运行情况。

\<Sysname\> display loopback-detection

Loopback detection is enabled.

Loopback detection interval is 30 second(s).

Loopback is detected on following interfaces:

 Interface                Action mode

 GigabitEthernet1/0/1     Block

 GigabitEthernet1/0/2     Shutdown

 GigabitEthernet1/0/3     None

 GigabitEthernet1/0/4     No-learning

表1-1 display loopback-detection命令显示信息描述表

字段

描述

Loopback detection is enabled

环路检测功能已使能

Loopback detection is disabled

环路检测功能已关闭

Loopback detection interval is 30 second(s)

环路检测的时间间隔为30秒

Loopback is detected on following interfaces

下列端口被检测到存在环路

Interface

端口名称

Action mode

环路检测的处理模式：

·Block：当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习MAC地址并将端口的入方向阻塞

·None：当系统检测到端口出现环路时，除了生成日志信息外不对该端口进行任何处理

·No-learning：当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习MAC地址

·Shutdown：当系统检测到端口出现环路时，除了生成日志信息外，还会自动关闭该端口，使其不能收发任何报文。端口被关闭后能够自动恢复，恢复时间由**shutdown-interval**命令（请参考"基础配置命令参考"中的"设备管理"）决定

No loopback is detected

未检测到环路

**环路检测 \-- 环路检测配置命令 \-- loopback-detection action**

------------------------------------------------------------------------

**[loopback-detection action**]命令用来在端口上配置环路检测的处理模式。

**[undo loopback-detection action**]命令用来恢复缺省情况。

【命令】

在二层以太网接口视图/S通道接口视图/S通道聚合接口视图下：

**[loopback-detection action**[ { **block** \| **no-learning** \| **shutdown** }]]

**[undo loopback-detection action**]

在二层聚合接口视图下：

**[loopback-detection action** **shutdown**]

**[undo loopback-detection action**]

【缺省情况】

当系统检测到端口出现环路时不对该端口进行任何处理，仅生成日志信息。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[block**]：表示Block模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习MAC地址并将端口的入方向阻塞。二层聚合接口不支持本模式。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[no-learning**]：表示No-learning模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会禁止端口学习MAC地址。二层聚合接口不支持本模式。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[shutdown**]：表示Shutdown模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会自动关闭该端口，使其不能收发任何报文。被关闭的端口将在**shutdown-interval**命令（请参考"基础配置命令参考"中的"设备管理"）所配置的时间之后自动恢复。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以使用**loopback-detection global action**命令在系统视图下全局配置环路检测的处理模式，也可以使用本命令在接口视图下配置当前端口的环路检测处理模式。系统视图下的配置对所有端口都有效，接口视图下的配置则只对当前端口有效，且接口视图下的配置优先级较高。

【举例】

\# 在端口GigabitEthernet1/0/1上配置环路检测的处理模式为Shutdown模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

System-GigabitEthernet1/0/1 loopback-detection action shutdown

【相关命令】

·**display loopback-detection**

·**loopback-detection global action**

**环路检测 \-- 环路检测配置命令 \-- loopback-detection enable**

------------------------------------------------------------------------

**[loopback-detection enable**]命令用来在端口上使能环路检测功能。

**[undo loopback-detection enable**]用来在端口上关闭环路检测功能。

【命令】

**[loopback-detection enable vlan**[ { *vlan-id-list* \| **all** }]]

**[undo loopback-detection enable vlan**[ { *vlan-id-list* \| **all** }]]

【缺省情况】

端口上的环路检测功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图/S通道接口视图/S通道聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表，表示多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

**[all**]：表示所有已创建的VLAN。

【使用指导】

用户可以使用**loopback-detection global enable**命令在系统视图下全局使能环路检测功能，也可以使用本命令在接口视图下使能当前端口的环路检测功能。系统视图下的配置对指定VLAN中的所有端口都有效，而接口视图下的配置则只对当前端口有效（该端口必须属于所指定的VLAN，否则配置无效），且接口视图下的配置优先级较高。

【举例】

\# 在端口GigabitEthernet1/0/1上使能VLAN 10～20内的环路检测功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

System-GigabitEthernet1/0/1 loopback-detection enable vlan 10 to 20

【相关命令】

·**display loopback-detection**

·**loopback-detection global enable**

**环路检测 \-- 环路检测配置命令 \-- loopback-detection global action**

------------------------------------------------------------------------

**[loopback-detection global action**]命令用来全局配置环路检测的处理模式。

**[undo loopback-detection global action**]命令用来恢复缺省情况。

【命令】

**[loopback-detection global action** **shutdown**]

**[undo loopback-detection global action**]

【缺省情况】

当系统检测到端口出现环路时不对该端口进行任何处理，仅生成日志信息。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[shutdown**]：表示Shutdown模式，即当系统检测到端口出现环路时，除了生成日志信息外，还会自动关闭该端口，使其不能收发任何报文。被关闭的端口将在**shutdown-interval**命令（请参考"基础配置命令参考"中的"设备管理"）所配置的时间之后自动恢复。

【使用指导】

用户可以使用本命令在系统视图下全局配置环路检测的处理模式，也可以使用**loopback-detection action**命令在接口视图下配置当前端口的环路检测处理模式。系统视图下的配置对所有端口都有效，接口视图下的配置则只对当前端口有效，且接口视图下的配置优先级较高。

【举例】

\# 全局配置环路检测的处理模式为Shutdown模式。

\<Sysname\> system-view

Sysname loopback-detection global action shutdown

【相关命令】

·**display loopback-detection**

·**loopback-detection action**

**环路检测 \-- 环路检测配置命令 \-- loopback-detection global enable**

------------------------------------------------------------------------

**[loopback-detection global enable**]命令用来全局使能环路检测功能。

**[undo loopback-detection global enable**]用来全局关闭环路检测功能。

【命令】

**[loopback-detection global enable vlan**[ { *vlan-list* \| **all** }]]

**[undo loopback-detection global enable vlan**[ { *vlan-list* \| **all** }]]

【缺省情况】

环路检测功能处于全局关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-list*]：VLAN列表，表示多个VLAN的编号。表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

**[all**]：表示所有已创建的VLAN。

【使用指导】

用户可以使用本命令在系统视图下全局使能环路检测功能，也可以使用**loopback-detection enable**命令在接口视图下使能当前端口的环路检测功能。系统视图下的配置对指定VLAN中的所有端口都有效，而接口视图下的配置则只对当前端口有效（该端口必须属于所指定的VLAN，否则配置无效），且接口视图下的配置优先级较高。

【举例】

\# 全局使能VLAN 10～20内的环路检测功能。

\<Sysname\> system-view

Sysname loopback-detection global enable vlan 10 to 20

【相关命令】

·**display loopback-detection**

·**loopback-detection enable**

**环路检测 \-- 环路检测配置命令 \-- loopback-detection interval-time**

------------------------------------------------------------------------

**[loopback-detection interval-time**]命令用来配置环路检测的时间间隔。

**[undo loopback-detection interval-time**]命令用来恢复缺省情况。

【命令】

**[loopback-detection interval-time ***interval*]

**[undo loopback-detection interval-time**]

【缺省情况】

环路检测的时间间隔为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：环路检测的时间间隔，取值范围为1～300，单位为秒。

【使用指导】

当使能了环路检测功能后，系统开始以一定的时间间隔发送环路检测报文，该间隔越长耗费的系统性能越少，该间隔越短环路检测的灵敏度越高。用户可以通过本命令调整发送环路检测报文的时间间隔，以在系统性能和环路检测的灵敏度之间进行平衡。

【举例】

\# 配置环路检测的时间间隔为10秒。

\<Sysname\> system-view

Sysname loopback-detection interval-time 10

【相关命令】

·**display loopback-detection**
