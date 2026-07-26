
**加密口 \-- 加密口配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

加密口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

加密口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 配置加密口Encrypt2/4/0的期望带宽为50kbit/s。

\<Sysname\> system-view

Sysname interface encrypt 2/4/0

Sysname-Encrypt2/4/0 bandwidth 50

**加密口 \-- 加密口配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：Encrypt2/4/0 Interface。

【视图】

加密口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 设置加密口Encrypt2/4/0的描述信息为"encrypt-intf"。

\<Sysname\> system-view

Sysname interface encrypt 2/4/0

Sysname-Encrypt2/4/0 description encrypt-intf

**加密口 \-- 加密口配置命令 \-- display interface encrypt**

------------------------------------------------------------------------

**[display interface encrypt**]命令用来显示加密口的相关信息。

【命令】

**[display interface **[ **encrypt** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定加密口的信息。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**encrypt**参数，将显示设备支持的所有接口的相关信息；

·如果指定**encrypt**参数，不指定*interface-number*参数，将显示所有已创建的加密口的相关信息。

【举例】

\# 显示加密口Encrypt2/4/0的详细信息。

\<Sysname\> display interface encrypt 2/4/0

Encrypt2/4/0

Current state: DOWN

Line protocol state: DOWN

Description: Encrypt2/4/0 Interface

Bandwidth: 64kbps

Maximum Transmit Unit: 64000

Internet protocol processing: disabled

Physical: Encrypt2/4/0, baudrate: 64000 bps

Last 5 seconds input: 0 bytes/sec, 0 packets/sec

Last 5 seconds output: 0 bytes/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 droped

Output: 0 packets, 0 bytes, 0 droped

\# 显示加密口Encrypt2/4/0的概要信息。

\<Sysname\> display interface encrypt 2/4/0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

En2/4/0              DOWN DOWN      \--

\# 显示当前物理状态为down的加密口的信息以及down的原因。

\<Sysname\> display interface encrypt brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

En2/4/0              ADM   Administratively

En2/4/1              DOWN  Not connected

En2/4/2              DOWN  Not connected

En2/4/3              DOWN  Not connected

En2/4/4              DOWN  Not connected

En2/4/5              DOWN  Not connected

En2/4/6              DOWN  Not connected

En2/4/7              DOWN  Not connected

表1-1 display interface encrypt命令显示信息描述表

字段

描述

Encrypt2/4/0

Current state

接口当前的物理状态和管理状态，可能的取值及含义如下：

·DOWN（Administratively）：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该接口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态，可能的状态及含义如下：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口的最大传输单元（MTU）。缺省值为64000字节。表示长度大于MTU的报文，将会被分片后再发送。如果设置了不准分片，报文会被丢弃

Physical

物理层链路信息

baudrate

接口的带宽

Last 5 seconds input: 0 bytes/sec, 0 packets/sec

最近5秒钟的平均输入速率：bytes/sec表示平均每秒输入的字节数，packets/sec表示平均每秒输入的包数

Last 5 seconds output:  0 bytes/sec, 0 packets/sec

最近5秒钟的平均输出速率：bytes/sec表示平均每秒输出的字节数，packets/sec表示平均每秒输出的包数

Input: 0 packets, 0 bytes, 0 droped

该接口接收的数据报文个数、字节数，以及由于没有接收缓冲而被丢弃的报文个数

Output: 0 packets, 0 bytes, 0 droped

该接口发送的数据报文个数、字节数，以及由于没有发送缓冲而被丢弃的报文个数

Brief information on interface(s) under route mode:

三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

【相关命令】

·**interface encrypt**

·**reset counters interface**

**加密口 \-- 加密口配置命令 \-- interface encrypt**

------------------------------------------------------------------------

**[interface encrypt**]命令用来进入加密口视图。

【命令】

**[interface encrypt** *number*]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：加密口的编号。

【举例】

\# 进入加密口Encrypt2/4/0的接口视图。

\<Sysname\> system-view

Sysname interface encrypt 2/4/0

Sysname-Encrypt2/4/0

**加密口 \-- 加密口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除加密口的统计信息。

【命令】

**[reset counters interface** [ **encrypt** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[encrypt**]：清除加密口的统计信息。

*[interface-number*]：加密口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**encrypt**和*interface-number*，则清除所有接口的统计信息；

·如果指定**encrypt**而不指定*interface-number*，则清除所有加密口的统计信息；

·如果同时指定**encrypt**和*interface-number*，则清除指定加密口的统计信息。

【举例】

\# 清除加密口Encrypt2/4/0上的统计信息。

\<Sysname\> reset counters interface encrypt 2/4/0

【相关命令】

·**display interface encrypt**

**加密口 \-- 加密口配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo** **shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于打开状态。

【视图】

加密口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭加密口Encrypt2/4/0。

\<Sysname\> system-view

Sysname interface encrypt 2/4/0

Sysname-Encrypt2/4/0 shutdown
