
**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

LoopBack接口的期望带宽为0kbit/s。

【视图】

LoopBack接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会对下列内容有影响：

·CBQ队列带宽。具体介绍请参见"ACL和QoS配置指导"中的"[拥塞管理"。]

·链路开销值。具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置LoopBack1的期望带宽为1000kbit/s。

\<Sysname\> system-view

Sysname interface loopback 1

Sysname-LoopBack1 bandwidth 1000

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

LoopBack接口视图/NULL接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将LoopBack1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface loopback 1

Sysname-LoopBack1 default

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，比如：LoopBack1 Interface。

【视图】

LoopBack接口视图/NULL接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述信息，为1～255个字符的字符串，区分大小写。

【使用指导】

当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。

配置的描述信息可通过命令行**display interface**查看。

【举例】

\# 设置LoopBack1的描述信息为"for RouterID"。

\<Sysname\> system-view

Sysname interface loopback 1

Sysname-LoopBack1 description for RouterID

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- display interface inloopback**

------------------------------------------------------------------------

![说明](LoopBack接口、NULL接口和InLoopBack接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display interface inloopback**]命令用来显示InLoopBack接口的相关信息。

【命令】

**[display interface ** **inloopback**  **0**  ]  **brief** [ **description**  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[0**]：InLoopBack接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。对于InLoopBack接口，因为其描述信息只能为InLoopBack0 Interface，不能配置，所以，该参数对InLoopBack接口无意义。

【使用指导】

查看InLoopBack接口的相关信息时：

·如果不指定**inloopback**参数，将显示设备支持的所有接口的相关信息。

·因为设备只支持一个InLoopBack接口InLoopBack0，所以，只要指定**inloopback**参数，不管是否指定**0**参数，显示的都是InLoopBack0的相关信息。

【举例】

\# 显示指定接口InLoopBack0的相关信息。

\<Sysname\> display interface inloopback

InLoopBack0

Current state: UP

Line protocol state: UP(spoofing)

Description: InLoopBack0 Interface

Maximum Transmit Unit: 1536

Physical: InLoopBack

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

表1-1 display interface inloopback命令显示信息描述表

字段

描述

Current state

接口当前的物理层状态。始终为UP，表示接口能收发报文

Line protocol state

链路层协议状态。始终为UP(spoofing)，表示接口的链路层协议状态为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在，而是按需建立的

Description

接口的描述字符串。只能为InLoopBack0 Interface，不可配置

Maximum Transmit Unit

接口的最大传输单元。只能为1536，不可配置

Physical: InLoopBack

接口的物理类型是InLoopBack

Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输入速率（只有接口支持统计功能时才显示该信息）：

·bytes/sec表示平均每秒输入的字节数

·bits/sec表示平均每秒输入的比特数

·packets/sec表示平均每秒输入的包数

Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输出速率（只有接口支持统计功能时才显示该信息）：

·bytes/sec表示平均每秒输出的字节数

·bits/sec表示平均每秒输出的比特数

·packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 drops

接口输入的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）

Onput: 0 packets, 0 bytes, 0 drops

接口输出的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）

\# 显示InLoopBack接口的概要信息。

\<Sysname\> display interface inloopback 0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

InLoop0              UP   UP(s)    \--

表1-2  display interface inloopback brie{.FigureDescriptionChar}f命令显示信息描述表

字段

描述

Brief information on interface(s) under route mode:

InLoopBack接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有(s)，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack、InLoopBack等接口会具有该属性

Interface

接口名称缩写

Link

接口物理连接状态。取值为UP，表示本链路物理上是连通的

Protocol

接口数据链路层协议状态，取值为UP(s)

Main IP

接口IP地址

因为InLoopBack接口下不能配置命令行，所以该项对InLoopBack接口无意义

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

因为InLoopBack接口下不能配置命令行，所以该项对InLoopBack接口无意义

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- display interface loopback**

------------------------------------------------------------------------

**[display interface loopback**]命令用来显示LoopBack接口的相关信息。

【命令】

**[display interface **[ **loopback** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：LoopBack接口的编号，取值范围为已创建的LoopBack接口的编号。如果不指定接口编号，将显示所有已创建的LoopBack接口的相关信息。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

**[display interface loopback**]命令用来显示Loopback接口的相关信息。只有创建LoopBack接口后，才支持该命令。

·如果不指定**loopback**参数，将显示设备支持的所有接口的相关信息。

·如果指定**loopback**参数，不指定*interface-number*参数，将显示所有已创建的Loopback接口的相关信息。

【举例】

\# 显示LoopBack0接口的相关信息。（支持统计功能的LoopBack接口的显示信息）

\<Sysname\> display interface loopback 0

LoopBack0

Current state: UP

Line protocol state: UP(spoofing)

Description: LoopBack0 Interface

Bandwidth: 1000kbps

Maximum Transmit Unit: 1536

Internet protocol processing: disabled

Physical: Loopback

Last clearing of counters:  Never

Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

\# 显示LoopBack0接口的相关信息。（不支持统计功能的LoopBack0接口的显示信息）

\<Sysname\> display interface loopback 0

LoopBack0

Current state: UP

Line protocol state: UP(spoofing)

Description: LoopBack0 Interface

Maximum Transmit Unit: 1536

Internet protocol processing : disabled

Physical: Loopback

Last clearing of counters:  Never

表1-3 display interface loopback命令显示信息描述表

字段

描述

Current state

接口当前的物理层状态

·UP：表示接口能收发报文

·Administratively DOWN：表示接口被手工关闭了，即在接口下配置了**shutdown**命令

Line protocol state

链路层协议状态：UP(spoofing)，表示接口的链路层协议状态为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在，而是按需建立的

Description

接口的描述字符串

Bandwidth

接口的期望带宽，只有当取值不为0时，才显示该字段

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing: disabled

表示不能处理三层报文（接口没有配置IP地址时，显示该信息）

Internet Address is 1.1.1.1/32 Primary

接口的主IP地址（接口配置了主IP地址时显示该信息）

Physical: Loopback

接口的物理类型是Loopback

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间（如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never）

Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输入速率（只有接口支持统计功能时才显示该信息）：

·bytes/sec表示平均每秒输入的字节数

·bits/sec表示平均每秒输入的比特数

·packets/sec表示平均每秒输入的包数

Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec

最近300秒钟的平均输出速率（只有接口支持统计功能时才显示该信息）：

·bytes/sec表示平均每秒输出的字节数

·bits/sec表示平均每秒输出的比特数

·packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 drops

接口输入的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）

Onput: 0 packets, 0 bytes, 0 drops

接口输出的报文数，输入的字节数，输入报文中丢弃的报文数（只有接口支持统计功能时才显示这些信息）

\# 显示LoopBack接口的概要信息。

\<Sysname\> display interface loopback brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

Loop1                UP   UP(s)    \--              forLAN1

\# 显示当前物理状态为down的LoopBack接口的信息以及down的原因。

\<Sysname\> display interface loopback brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Loop1                ADM  Administratively

表1-4 display interface loopback brief命令显示信息描述表

字段

描述

Brief information on interface(s) under route mode:

LoopBack接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有(s)，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack等接口会具有该属性

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Protocol

接口数据链路层协议状态，取值为UP(s)

Main IP

接口主IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时，表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

【相关命令】

·**interface loopback**

·**reset counters interface loopback**

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- display interface null**

------------------------------------------------------------------------

**[display interface null**]命令用来显示NULL接口的相关信息。

【命令】

**[display interface ** **null**  **0**  ]  **brief** [ **description**  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[0**]：NULL接口的编号。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

【使用指导】

查看Null接口的相关信息时：

·如果不指定**null**参数，将显示设备支持的所有接口的相关信息。

·因为设备只支持一个Null接口Null0，所以，只要指定**null**参数，不管是否指定**0**参数，显示的都是Null0的相关信息。

【举例】

\# 显示指定接口NULL0的相关信息。（支持统计功能的NULL接口的显示信息）

\<Sysname\> display interface null 0

NULL0

Current state: UP

Line protocol state: UP(spoofing)

Description: NULL0 Interface

Bandwidth: 1000000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

Physical: NULL DEV

Last clearing of counters: Never

Last 300 seconds input:  0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output:  0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

\# 显示指定接口NULL0的相关信息。（不支持统计功能的NULL接口的显示信息）

\<Sysname\> display interface null 0

NULL0

Current state: UP

Line protocol state: UP(spoofing)

Description:  NULL0 Interface

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

Physical: NULL DEV

Last clearing of counters: Never

\# 显示NULL接口的概要信息。

\<Sysname\> display interface null 0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

NULL0                UP   UP(s)    \--             

**[display interface null**]命令显示信息描述请参见[表]1-3(?-2004230743#_Ref137377196)和[表]1-4(?-2004230743#_Ref328495828)。

【相关命令】

·**interface null**

·**reset counters interface null**

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- interface loopback**

------------------------------------------------------------------------

**[interface loopback**]命令用来创建LoopBack接口，并进入LoopBack接口视图。

**[undo interface loopback**]命令用来删除指定的LoopBack接口。

【命令】

**[interface loopback**]*interface-number*

**[undo interface loopback** *interface-number*]

【缺省情况】

设备上没有LoopBack接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：LoopBack接口的编号。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

LoopBack接口创建后，物理层和链路层永远处于up状态，除非手工关闭该接口。因此，使用LoopBack接口建立连接，能够避免连接受接口物理状态的影响，从而提高连接的可靠性。比如，将LoopBack接口作为建立FTP连接时的源接口，将LoopBack接口的地址作为BGP协议中的Router ID。

【举例】

\# 创建接口LoopBack1。

\<Sysname\> system-view

Sysname interface loopback 1

Sysname-LoopBack1

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- interface null**

------------------------------------------------------------------------

**[interface null**]命令用来进入NULL接口的视图。

【命令】

**[interface null 0**]

【缺省情况】

设备只支持一个NULL接口------NULL0，用户不能创建也不能删除。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[0**]：NULL接口的编号。

【举例】

\# 进入接口NULL0的视图。

\<Sysname\> system-view

Sysname interface null 0

Sysname-NULL0

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- reset counters interface loopback**

------------------------------------------------------------------------

![说明](LoopBack接口、NULL接口和InLoopBack接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset counters interface loopback**]命令用来清除LoopBack接口的统计信息。

【命令】

**[reset counters interface** [ **loopback** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：逻辑接口编号。如果不指定该参数，则清除所有LoopBack接口的统计信息。

【使用指导】

如果要统计一定时间内接口的流量来判断接口和链路工作是否正常，可以使用该命令先清除接口原有的统计信息，然后让接口自动重新统计。

只有创建LoopBack接口后，才支持该命令。

【举例】

\# 清除接口LoopBack1的统计信息。

\<Sysname\> reset counters interface loopback 1

【相关命令】

·**display interface loopback**

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- reset counters interface null**

------------------------------------------------------------------------

![说明](LoopBack接口、NULL接口和InLoopBack接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset counters interface null**]命令用来清除NULL接口的统计信息。

【命令】

**[reset counters interface** [ **null** [ **0**  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[0**]：NULL接口的编号。

【使用指导】

如果要统计一定时间内接口的流量来判断接口工作是否正常，可以使用该命令先清除接口原有的统计信息，然后让接口自动重新统计。

【举例】

\# 清除接口NULL0的统计信息。

\<Sysname\> reset counters interface null 0

【相关命令】

·**display interface null**

**LoopBack接口、NULL接口和InLoopBack接口 \-- LoopBack接口、NULL接口和InLoopBack接口配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭LoopBack接口。

**[undo** **shutdown**]命令用来开启LoopBack接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

LoopBack接口处于开启状态。

【视图】

LoopBack接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**shutdown**命令会导致使用该接口建立的链路中断，不能通信，请谨慎使用。

【举例】

\# 关闭接口LoopBack1。

\<Sysname\> system-view

Sysname interface loopback 1

Sysname-LoopBack1 shutdown
