
**TRILL \-- TRILL配置命令 \-- auto-cost enable**

------------------------------------------------------------------------

**[auto-cost** **enable**]命令用来开启TRILL端口链路开销值的自动计算功能。

**[undo** **auto-cost** **enable**]命令用来关闭TRILL端口链路开销值的自动计算功能。

【命令】

**[auto-cost** **enable**]

**[undo** **auto-cost** **enable**]

【缺省情况】

TRILL端口链路开销值的自动计算功能处于开启状态。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

TRILL端口的链路开销可以由系统自动计算或用户手工配置，其中手工配置优先，即：只要进行了手工配置，就取手工配置值；如果没有进行手工配置，若开启了自动计算功能则取自动计算值，若关闭了自动计算功能则取缺省值2000。

TRILL端口链路开销值自动计算的公式如下：链路开销值＝20000000000000÷端口波特率。

【举例】

\# 关闭TRILL端口链路开销值的自动计算功能。

\<Sysname\> system-view

Sysname trill

Sysname-trill undo auto-cost enable

【相关命令】

·**trill** **cost**

**TRILL \-- TRILL配置命令 \-- display trill adjacent-table**

------------------------------------------------------------------------

**[display** **trill** **adjacent-table**]命令用来显示TRILL邻接表信息。

【命令】

**[display**[ **trill** **adjacent-table** [ **count** \| **nickname** *nickname* **interface** *interface-type* *interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[count**]：显示表项的数量。

**[nickname** *nickname* **interface** *interface-type* *interface-number*]：显示指定RB指定端口上的信息。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数；*interface-type* *interface-number*为端口类型和端口编号。如果未指定本参数，将显示所有RB所有端口上的信息。

【举例】

\# 显示TRILL邻接表所有表项的信息。

\<Sysname\> display trill adjacent-table

NextHop     MAC address       Interface

0x899b      00e0-fc58-123a    GE1/0/1

\# 显示TRILL邻接表的表项数量。

\<Sysname\> display trill adjacent-table count

Total number of TRILL ADJ entries: 1

表1-1 display trill adjacent-table命令显示信息描述表

字段

描述

NextHop

报文转发的下一跳RB的Nickname

MAC address

报文转发的下一跳RB的MAC地址

Interface

报文的出端口

Total number of TRILL ADJ entries

TRILL邻接表的表项数量

**TRILL \-- TRILL配置命令 \-- display trill brief**

------------------------------------------------------------------------

**[display** **trill** **brief**]命令用来显示TRILL摘要信息。

【命令】

**[display** **trill** **brief**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示TRILL摘要信息。

\<Sysname\> display trill brief

Network entity: 00.00a0.fc00.5806.00

Nickname: 0xfa1b

Nickname priority: 64

Tree-root priority: 32768

Cost style: Wide

Maximum allowed LSP received: 1492

Maximum allowed LSP originated: 1458

Maximum unicast load-balancing: 8

Overload status: None

Overload remaining time: N/A

Device role: Normal

Timers:

  LSP-max-age: 1200s

  LSP-refresh: 900s

  Interval between SPFs: 10s  10ms  20ms

表1-2 display trill brief命令显示信息描述表

字段

描述

Network entity

网络实体的名称

Nickname

RB的Nickname

Nickname priority

RB拥有Nickname的优先级

Tree-root priority

设备作为TRILL分发树根桥的优先级

Cost style

开销类型，仅支持Wide类型

Maximum allowed LSP received

可接收的LSP最大长度

Maximum allowed LSP originated

可生成的LSP最大长度

Maximum unicast load-balancing

TRILL单播等价多路径的最大路径数

Overload status

过载标志位的置位原因：

·Config：表示配置过载标志位置位

·GR：表示在平滑重启中过载标志位置位

·GR/Config：表示在Start类型的平滑重启中配置过载标志位置位

·None：表示未配置过载标志位置位

Device role

设备角色：

·Normal：表示普通RB

·Access：表示二层接入设备

·Gateway：表示网关设备

Overload remaining time

过载标志位保持置位状态的时间，单位为秒。N/A表示未配置此时间或此时间已超时

Timers

TRILL定时器

LSP-max-age

LSP的最大生存时间，单位为秒

LSP-refresh

LSP的刷新周期，单位为秒

Interval between SPFs

依次为使用SPF（Shortest Path First，最短路径优先）算法进行路由计算的最大时间间隔（单位为秒）、最小时间间隔（单位为毫秒）和时间间隔惩罚增量（单位为毫秒）

**TRILL \-- TRILL配置命令 \-- display trill fib**

------------------------------------------------------------------------

**[display** **trill** **fib**]命令用来显示TRILL单播转发表信息。

【命令】

**[display**[ **trill** **fib** [ **count** \| **nickname** *nickname* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[count**]：显示表项的数量。

**[nickname** *nickname*]：显示指定RB的信息。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数。如果未指定本参数，将显示所有RB的信息。

【举例】

\# 显示TRILL单播转发表所有表项的信息。

\<Sysname\> display trill fib

Flags: T-Transit, E-Egress

Destination   HopCount   NextHop   Interface                Flags

0xfa1b        63         N/A   N/A                      E

0x899b        63         0x2a5c    GE1/0/1                  T

\# 显示TRILL单播转发表的表项数量。

\<Sysname\> display trill fib count

Total number of TRILL FIB destinations: 1

Total number of TRILL FIB entries: 2

表1-3 display trill fib命令显示信息描述表

字段

描述

Destination

目的RB的Nickname

HopCount

到达目的RB的跳数

NextHop

下一跳RB的Nickname

Interface

报文的出端口

Flags

标志：

·T：表示转发

·E：表示出隧道

Total number of TRILL FIB destinations

TRILL单播转发表中目的RB的数量

Total number of TRILL FIB entries

TRILL单播转发表的表项数量

**TRILL \-- TRILL配置命令 \-- display trill graceful-restart status**

------------------------------------------------------------------------

**[display**] **tril**l **graceful-restart** **status**命令用来显示TRILL的GR（Graceful Restart，平滑重启）状态信息。

【命令】

**[display**] **trill** **graceful-restart** **status**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示TRILL的GR状态信息。

\<Sysname\> display trill graceful-restart status

Restart status: RESTARTING

Restart phase: LSDB synchronization

Restart interval: 300s

T3 remaining time: 140s

Total number of interfaces: 1

Number of waiting LSPs: 3

T2 remaining time: 55s

  Interface: GigabitEthernet1/0/1

    T1 remaining time: 2s

    RA received: Y

    CSNP received: N

    T1 expiration number: 1

表1-4 display trill graceful-restart status显示信息描述表

字段

描述

Restart status

重启状态：

·COMPLETE：表示平滑重启已完成

·RESTARTING：表示正进行Restart类型的平滑重启

·STARTING：表示正进行Start类型的平滑重启

Restart phase

重启阶段：

·Finish：表示平滑重启已完成

·LSDB synchronization：表示T2同步阶段

·LSP generation：表示LSP生成阶段

·MCS synchronization：表示二层组播数据同步阶段

·SPF：表示路由计算阶段

Restart interval

重启间隔，单位为秒

T3 remaining time

T3定时器的超时剩余时间，单位为秒。初始值为65535秒，后续会根据RA报文中的剩余时间来更新

Total number of interfaces

进程下的所有端口数

Number of waiting LSPs

等待的LSP数量

T2 remaining time

T2定时器的超时剩余时间，单位为秒。对于Restart类型的GR，初始值固定为60秒；对于Start类型的GR，初始值为**graceful-restart interval**命令的配置值（缺省为300秒）

Interface

端口名称

T1 remaining time

T1定时器的超时剩余时间，单位为秒。初始值为3秒

RA received

RA接收标记位：

·Y：表示置位

·N：表示未置位

CSNP received

CSNP接收标记位：

·Y：表示置位

·N：表示未置位

T1 expiration number

T1定时器的超时次数。最大值为10次

**TRILL \-- TRILL配置命令 \-- display trill ingress-route**

------------------------------------------------------------------------

**[display** **trill** **ingress-route**]命令用来显示TRILL入流量的转发信息。

【命令】

**[display** **trill** **ingress-route** [ **vlan** *vlan-list* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan** *vlan-list*]：显示指定VLAN的信息。v*lan-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，将显示所有VLAN的信息。

【使用指导】

通过本命令可以显示流量进入TRILL网络的本地入端口，以及流量转发所使用的树根和出端口信息。

【举例】

\# 显示所有VLAN的TRILL入流量的转发信息。

\<Sysname\> display trill ingress-route

Total number of VLANs: 1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

VLAN ID:

  1

List of local ports:

  GE1/0/1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

VLAN ID:

  1

Tree root:

  0x1111

List of remote ports:

  GE1/0/2

表1-5 display trill ingress-route命令显示信息描述表

字段

描述

Total number of VLANs

VLAN总数

VLAN ID

VLAN的编号

List of local ports

流量进入TRILL网络的本地入端口

Tree root

本VLAN转发组播流量所使用的TRILL分发树树根的Nickname

List of remote ports

报文经TRILL封装后的转发出端口

**TRILL \-- TRILL配置命令 \-- display trill interface**

------------------------------------------------------------------------

**[display** **trill** **interface**]命令用来显示TRILL端口信息。

【命令】

**[display**[ **trill** **interface** [ *interface-type* *interface-number* \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type* *interface-number*]：显示指定端口的信息，*interface-type* *interface-number*为端口类型和端口编号。如果未指定本参数，将显示所有端口的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示摘要信息。

【举例】

\# 显示所有TRILL端口的摘要信息。

\<Sysname\> display trill interface

Interface                   Protocol state   DRB  Cost      Link type

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

GigabitEthernet1/0/1        UP               Yes  2000      Access

\# 显示所有TRILL端口的详细信息。

\<Sysname\> display trill interface verbose

Interface: GigabitEthernet1/0/1

Protocol state: UP

Nickname: 0xfa1b

MTU: 1470

DRB: Yes

Designated VLAN: 1

Link type: Access

CSNP timer: 10s

Hello timer: 10s

Hello multiplier: 3

LSP timer: 10ms

LSP transmit-throttle count: 5

Cost: 2000

AVF inhibited timer: 30s

Priority: 64

Track index: None

Track state: NotReady

Active AVF:

  1-3, 5, 58

Inhibited AVF: None

表1-6 display trill interface命令显示信息描述表

字段

描述

Interface

端口名称

Protocol state

TRILL协议的状态，包括UP和DOWN

Nickname

RB的Nickname

MTU

链路的MTU值，单位为字节

DRB

是否被选举为DRB：

·Yes：表示已被选举为DRB

·No：表示未被选举为DRB

·Down：表示端口状态为down，不参与DRB的选举

Designated VLAN

当前生效的指定VLAN。如果显示为65535，表示端口down或端口下没有使能VLAN

Link type

TRILL端口的类型：

·Access：表示Access类型

·Hybrid：表示Hybrid类型

·Trunk：表示Trunk类型

·VR：表示VR类型

CSNP timer

CSNP报文的发送间隔，单位为秒

Hello timer

Hello报文发送间隔，单位为秒

Hello multiplier

Hello报文的失效数目

LSP timer

LSP的最小发送间隔，单位为毫秒

LSP transmit-throttle count

一次发送LSP的最大数目

Cost

端口的链路开销值

AVF inhibited timer

环路避免的抑制时间，单位为秒

Priority

DRB优先级

Track index

TRILL监测的Track项，None表示没有

Track state

TRILL监测的Track项状态：

·NotReady：表示没有监测任何Track项或未连接Track模块

·Positive：表示状态正常

·Negative：表示状态异常

Active AVF

当前端口上被DRB分配为AVF的VLAN，None表示没有

Inhibited AVF

当前端口上暂时被抑制的AVF的VLAN，None表示没有

**TRILL \-- TRILL配置命令 \-- display trill lsdb**

------------------------------------------------------------------------

**[display** **trill** **lsdb**]命令用来显示TRILL链路状态数据库信息。

【命令】

**[display**[ **trill** **lsdb** [ **local** \| **lsp-id** *lsp-id* \| **verbose** ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[local**]：显示本地生成的LSP的信息。

**[lsp-id** *lsp-id*]：显示指定LSP的信息。*lsp-id*为LSP标识，形式为SYSID*.*Pseudonode ID-fragment num，其中，SYSID是产生该LSP的结点或伪结点的System ID，fragment num是该LSP的分片号。如果未指定本参数，将显示所有LSP的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示摘要信息。

【举例】

\# 显示TRILL链路状态数据库的摘要信息。

\<Sysname\> display trill lsdb

Flags: \* - Self LSP

LSP ID                 Seq num     Checksum  Holdtime  Length    Overload

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

00a0.fc00.5806.00-00\*  0x00000005  0xd315    361       78        0

\# 显示TRILL链路状态数据库的详细信息。

\<Sysname\> display trill lsdb verbose

LSP ID: 00a0.fc00.5806.00-00\*

Sequence number: 0x00000005

Checksum: 0xd315

Holdtime: 1145s

Length: 78

Overload: 0

Source: 00a0.fc00.5806.00

TRILL version: 0x00

Nickname:

  Nickname: 0xfa1b

  Priority: 64

  Tree-root priority: 32768

Trees:

  Compute trees number: 1

  Max compute trees number: 15

  Used trees number: 1

Tree identifiers:

  0x899b

Trees used identifiers:

  0x899b

Interested VLANs:

  Start: 4, End: 4, M4: 0, M6: 0

  Start: 5, End: 6, M4: 1, M6: 0

Neighbor:

  ID: 00e0.fc58.123a.01, Cost: 2000

Group address:

  VLAN ID: 2

  Group MAC address: 0100-5e01-0101

Gateway information:

  MAC address: 0100-5e01-0001

   VR type: IPv4, VR ID: 2, VR priority: 64

Gateway router capability:

  VR type: IPv4, VR ID: 2

   VLAN ID: 2

    Virtual address:

     192.168.1.1

     192.168.1.2

表1-7 display trill lsdb命令显示信息描述表

字段

描述

LSP ID

LSP标识，\*表示是本地生成的LSP

Seq num/Sequence number

LSP的序列号

Checksum

LSP的校验和

Holdtime

LSP的生存剩余时间，单位为秒

Length

LSP的长度

Overload

LSP中Overload位的置位情况：

·0：表示未置位

·1：表示已置位

Source

生成此LSP的RB的编号

TRILL version

生成此LSP的RB支持的最高版本

Nickname

生成此LSP的RB的Nickname信息：

·Nickname：RB的Nickname

·Priority：占有Nickname的优先级

·Tree-root priority：作为TRILL分发树根桥的优先级

Trees

生成此LSP的RB的TRILL分发树计算信息：

·Compute trees number：希望整网计算的TRILL分发树数量

·Max compute trees number：最多可计算的TRILL分发树数量

·Used trees number：作为Ingress RB时使用的TRILL分发树数量

Tree identifiers

生成此LSP的RB作为根桥优先级最高的RB时，要求其它RB计算的TRILL分发树

Trees used identifiers

生成此LSP的RB作为Ingress RB时使用的TRILL分发树

Interested VLANs

以生成此LSP的RB为AVF的VLAN信息：

·Start：起始VLAN的编号

·End：结束VLAN的编号

·M4：在此VLAN范围内是否存在IPv4组播路由器。0表示存在，1表示不存在

·M6：在此VLAN范围内是否存在IPv6组播路由器。0表示存在，1表示不存在

Neighbor

生成此LSP的RB的邻居信息：

·ID：邻居的编号

·Cost：到达此邻居的开销值

Group address

生成此LSP的RB的组播MAC地址信息：

·VLAN ID：组播MAC地址所属VLAN

·Group MAC address：关注的组播MAC地址

Gateway information

生成此LSP的RB的网关信息：

·MAC address：封装的三层协议报文的实际MAC地址

·VR type：网络类型，IPv4或IPv6

·VR ID：VR的编号

·VR priority：竞选主成员RB的优先级

Gateway router capability

生成此LSP的RB的网关路由能力：

·VR type：网络类型，IPv4或IPv6

·VR ID：VR的编号

·VLAN ID：虚拟IP地址所属的VLAN

·Virtual address：虚拟IP地址列表

**TRILL \-- TRILL配置命令 \-- display trill mfib ingress**

------------------------------------------------------------------------

![说明](TRILL命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **trill** **mfib** **ingress**]命令用来显示TRILL组播转发表的入表项信息。

【命令】

**[display**[ **trill** **mfib** **ingress** [ **vlan** *vlan-id* [ **local-entry** \| **remote-entry** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vlan***vlan-id*]：显示指定VLAN内的信息，*vlan-id*的取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[local-entry**]：显示本地的入表项信息。本地入表项是指从该表项中的端口发出的报文无需进行TRILL封装。

**[remote-entry**]：显示远端的入表项信息。远端入表项是指从该表项中的端口发出的报文需要进行TRILL封装。

【使用指南】

如果未指定**local-entry**和**remote-entry**参数，将同时显示本地和远端的入表项信息。

【举例】

\# 显示TRILL组播转发表所有入表项的信息。

\<Sysname\> display trill mfib ingress

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Ingress type: Local entry

  VLAN ID: 1

  Ports:

    GE1/0/1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Ingress type: Remote entry

  VLAN ID: 1

  RootNickName: 0x5092

  Ports:

    GE1/0/2

表1-8 display trill mfib ingress命令显示信息描述表

字段

描述

Ingress type

入表项的类型：

·Local entry：表示本地入表项

·Remote entry：表示远端入表项

VLAN ID

表项对应VLAN的编号

RootNickName

表项对应RB的Nickname

Ports

表项对应的端口

**TRILL \-- TRILL配置命令 \-- display trill mfib transit**

------------------------------------------------------------------------

![说明](TRILL命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **trill** **mfib** **transit**]命令用来显示TRILL组播转发表的出表项信息。

【命令】

**[display**[ **trill** **mfib** **transit** [ **nickname** *nickname* [ **prune-entry** \| **rpf-entry** \| **vlan** *vlan-id* [ **mac** *mac-address* ] ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[nickname** *nickname*]：显示指定RB的信息。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数。如果未指定本参数，将显示所有RB的信息。

**[prune-entry**]：显示被剪枝掉的表项的信息。如果未指定本参数，将显示所有表项的信息。

**[rpf-entry**]：显示RPF表项的信息。如果未指定本参数，将显示所有表项的信息。

**[vlan** *vlan-id*]：显示指定VLAN内的信息，*vlan-id*的取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[mac** *mac-address*]**：**显示指定MAC地址的信息，*mac-address*为MAC地址。如果未指定本参数，将显示所有MAC地址的信息。

【举例】

\# 显示TRILL组播转发表所有出表项的信息。

\<Sysname\> display trill mfib transit

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Transit type: RPF entry

  RootNickName: 0x5092

  InNickName: 0x5092

  Port:GE1/0/1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Transit type: RB entry

  RootNickName: 0x5092

  Flag: Egress/Transit

  Ports:

    GE1/0/1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Transit type: VLAN RB entry

  RootNickName: 0x5092

  VLAN ID: 1

  Flag: Egress/Transit

  Ports:

    GE1/0/1

表1-9 display trill mfib transit命令显示信息描述表

字段

描述

Transit type

出表项的类型：

·RB entry：表示RB表项

·RPF entry：表示RPF表项

·VLAN RB entry：表示指定VLAN的RB表项

·MAC VLAN RB entry：表示指定MAC地址和VLAN的RB表项

RootNickName

表项对应RB的Nickname

InNickName

表项入口RB的Nickname

VLAN ID

表项对应VLAN的编号

MAC address

表项对应的MAC地址

Flag

表项的类型：

·Egress：表示Egress表项

·Transit：表示Transit表项

·Egress/Transit：表示既是Egress表项又是Transit表项

Port/Ports

表项对应的端口

**TRILL \-- TRILL配置命令 \-- display trill multicast-route**

------------------------------------------------------------------------

**[display** **trill** **multicast-route**]命令用来显示TRILL组播路由表信息，即基于组播分发树的组播报文的下一跳出端口列表。

【命令】

**[display** **trill** **multicast-route** [ **tree-root** *nickname* [ **vlan** *vlan-list* [ **mac-address** *mac-address*  ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[tree-root** *nickname*]：显示以指定RB为TRILL分发树根桥的TRILL组播路由表信息。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数。如果未指定本参数，将显示所有TRILL组播路由表信息。

**[vlan** *vlan-list*]：显示指定VLAN内的信息。v*lan-list*为VLAN列表，表示多个VLAN。表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。如果未指定本参数，将显示所有VLAN内的信息。

**[mac-address** *mac-address*]：显示指定MAC地址的信息，*mac-address*为MAC地址。如果未指定本参数，将显示所有MAC地址的信息。

【举例】

\# 显示TRILL组播路由表所有表项的信息。

\<Sysname\> display trill multicast-route

Root                          Flag

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0x899b                        Valid

\# 显示以指定RB（Nickname为0x899B）为TRILL分发树根桥的TRILL组播路由表信息。

\<Sysname\> display trill multicast-route tree-root 899b

Root: 0x899b

LocalRcvFlag: True

List of VLANs:

  1 to 10, 13, 40, 60 to 85, 200, 1001

List of outgoing ports (4 in total):

  GE1/0/1

  GE1/0/2

  GE1/0/3

  GE1/0/4

\# 显示VLAN 1内以指定RB（Nickname为0x899B）为TRILL分发树根桥的TRILL组播路由表信息。

\<Sysname\> display trill multicast-route tree-root 899b vlan 1

Root: 0x899b

VLAN: 1

LocalRcvFlag: False

List of outgoing ports (3 in total):

  GE1/0/1

  GE1/0/2

  GE1/0/3

List of IPv4 multicast-router ports (2 in total):

  GE1/0/1

  GE1/0/2

List of IPv6 multicast-router ports (2 in total):

  GE1/0/2

  GE1/0/3

List of MAC addresses (4 in total):

  0000-1111-00ee

  00ff-1111-00ff

  00ef-1111-00ef

  0000-111f-00ff

\# 显示VLAN 1内以指定RB（Nickname为0x899B）为TRILL分发树根桥的、指定MAC地址（0011-11FF-0022）上的TRILL组播路由表信息。

\<Sysname\> display trill multicast-route tree-root 899b vlan 1 mac-address 0011-11ff-0022

Root: 0x899b

VLAN: 1

MAC address: 0011-11ff-0022

LocalRcvFlag: True

List of outgoing ports (2 in total):

  GE1/0/3

  GE1/0/4

表1-10 display trill multicast-route命令显示信息描述表

字段

描述

Root

作为TRILL分发树根桥的RB的Nickname

VLAN

VLAN的编号

MAC address

MAC地址

Flag

根桥是否有效：

·Invalid：表示无效

·Valid：表示有效

LocalRcvFlag

本地接收标识，即是否需要进行本地转发：

·False：表示不需要进行本地转发

·True：表示需要进行本地转发

List of outgoing ports (4 in total)

出端口列表及其总数，None表示没有

List of VLANs (2 in total)

VLAN列表及其总数，None表示没有

List of IPv4 multicast-router ports (2 in total)

IPv4组播路由器的端口列表及其总数

List of IPv6 multicast-router ports (2 in total)

IPv6组播路由器的端口列表及其总数

List of MAC addresses (4 in total)

MAC地址列表及其总数

**TRILL \-- TRILL配置命令 \-- display trill neighbor-table**

------------------------------------------------------------------------

**[display** **trill** **neighbor-table**]命令用来显示TRILL邻居表信息。

【命令】

**[display** **trill** **neighbor-table**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示TRILL邻居表信息。

\<Sysname\> display trill neighbor-table

Total number of nexthops: 3

NextHop   MAC address       Interface

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0x899b    00e0-fc58-123a    GE1/0/1

表1-11 display trill neighbor-table命令显示信息描述表

字段

描述

Total number of nexthops

下一跳的总数

NextHop

下一跳的Nickname

MAC address

下一跳的MAC地址

Interface

出端口

**TRILL \-- TRILL配置命令 \-- display trill peer**

------------------------------------------------------------------------

**[display** **trill** **peer**]命令用来显示TRILL邻居统计信息。

【命令】

**[display** **trill** **peer** [ **interface** *interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type* *interface-number*]：显示指定端口上的信息，*interface-type* *interface-number*为端口类型和端口编号。如果未指定本参数，将显示所有端口上的信息。

【举例】

\# 显示端口GigabitEthernet1/0/1上的TRILL邻居统计信息。

\<Sysname\> display trill peer interface gigabitethernet 1/0/1

System ID: 00e0.fc58.123a

Interface: GigabitEthernet1/0/1

Circuit ID: 00e0.fc58.123a.01

State: Up

Holdtime: 8s

DRB priority: 64

Nickname: 0x899b

Uptime: 00:38:15

表1-12 display trill peer命令显示信息描述表

字段

描述

System ID

邻居的System ID

Interface

与邻居直连的本地TRILL端口

Circuit ID

伪节点的LSP编号

State

邻居状态，包括Up和Down

Holdtime

邻接关系保持时间，单位为秒。如果在该时间内未收到邻居发来的Hello报文，则认为与该邻居的邻接关系已失效；如果收到了，则重置此时间

DRB priority

邻居端口的DRB优先级

Nickname

邻居的Nickname

Uptime

与该邻居的邻接关系已保持的时间

**TRILL \-- TRILL配置命令 \-- display trill rpf-table**

------------------------------------------------------------------------

**[display** **trill** **rpf-table**]命令用来显示TRILL RPF检查表信息。

【命令】

**[display** **trill** **rpf-table** **tree-root** *nickname*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[tree-root***nickname*]：显示以指定RB为TRILL分发树根桥的信息。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数。

【使用指导】

TRILL RPF（Reverse Path Forwarding，逆向路径转发）检查表用来检查组播报文的入端口是否合法。即根据报文中Egress RB（即该报文所属TRILL分发树的根桥）和Ingress RB的Nickname，检查报文的实际入端口与RPF表项中的入端口是否一致，如不一致则认为该报文非法并将其丢弃。

【举例】

\# 显示以指定RB（Nickname为0x899B）为TRILL分发树根桥的TRILL RPF检查表信息。

\<Sysname\> display trill rpf-table tree-root 899b

Ingress-nickname           Expected-rcv-ports

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0x1fff                     GE1/0/1

0x1ff0                     GE1/0/2

0x0ffe                     GE1/0/3

表1-13 display trill rpf-table命令显示信息描述表

字段

描述

Ingress-nickname

Ingress RB的Nickname

Expected-rcv-ports

期望的入端口

**TRILL \-- TRILL配置命令 \-- display trill topology**

------------------------------------------------------------------------

**[display** **trill** **topology**]命令用来显示TRILL网络的拓扑信息。

【命令】

**[display** **trill** **topology** [ **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[verbose**]：显示详细信息。如果未指定本参数，将显示摘要信息。

【举例】

\# 显示TRILL网络拓扑的摘要信息。

\<Sysname\> display trill topology

                         TRILL topology information

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Flags: O-Node is overloaded          R-Node is directly reachable

           D-Node or link is to be deleted

SPF node          Node flag    SPF link               Link cost  Link flag

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0011.2200.0201.00 -/-/-

                               \--\>0011.2200.0301.01   20000      -

0011.2200.0301.01 -/R/-

                               \--\>0011.2200.0201.00   0          -

                               \--\>0011.2200.0301.00   0          -

0011.2200.0301.00 -/-/-

                               \--\>0011.2200.0301.01   20000      -

\# 显示TRILL网络拓扑的详细信息。

\<Sysname\> display trill topology verbose

                         TRILL topology information

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Flags: O-Node is overloaded          R-Node is directly reachable

           D-Node or link is to be deleted

SPF node: 0011.2200.0201.00

  Node flag: -/-/-

  SPF links count: 1

  \--\>0011.2200.0301.01

    Link cost: 20000

    Link flag: -

    Link sources: 1

     Link source 1

       Type: Adjacent       Interface: N/A

       Cost: 20000          NextHop: N/A

SPF node: 0011.2200.0301.01

  Node flag: -/R/-

  SPF links: 2

  \--\>0011.2200.0201.00

    Link cost: 0

    Link flag: -

    Link sources count: 1

     Link source 1

       Type: Remote         Interface: N/A

       Cost: 0              NextHop: N/A

  \--\>0011.2200.0301.00

    Link cost: 0

    Link flag: -

    Link sources: 1

     Link source 1

       Type: Remote         Interface: GE1/0/1

       Cost: 0              NextHop: 0x0002

SPF node: 0011.2200.0301.00

  Node flag: -/-/-

  SPF links: 1

  \--\>0011.2200.0301.01

    Link cost: 20000

    Link flag: -

    Link sources: 1

     Link source 1

       Type: Remote         Interface: N/A

       Cost: 20000          NextHop: N/A

表1-14 display trill topology命令显示信息描述表

字段

描述

SPF node

拓扑节点的编号

Node flag

节点的状态标记：

·O：OverLoad状态，表示节点当前不可用

·R：表示节点是直连节点

·D：表示节点待删除

SPF link

拓扑链路

SPF links

拓扑链路的个数

Link cost

拓扑链路的开销

Link flag

链路状态标记，D表示链路待删除

Link sources

链路发布源的个数

Link source 1

链路发布源的相关信息

Type

链路发布源的类型：

·Adjacent：表示由本地邻居维护产生

·Remote：表示由其它节点的LSP产生

Cost

链路发布源的开销

**TRILL \-- TRILL配置命令 \-- display trill unicast-route**

------------------------------------------------------------------------

**[display** **trill** **unicast-route**]命令用来显示TRILL单播路由表信息。

【命令】

**[display** **trill** **unicast-route** [ **nickname** *nickname*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[nickname** *nickname*]：显示指定RB的信息。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数。如果未指定本参数，将显示所有RB的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示摘要信息。

【举例】

\# 显示TRILL单播路由表所有表项的摘要信息。

\<Sysname\> display trill unicast-route

Destinations: 2        Unicast routes: 2

Destination    Interface                NextHop

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0xfa1b         N/A                      N/A

0x899b         GE1/0/1                  Direct

\# 显示TRILL单播路由表所有表项的详细信息。

\<Sysname\> display trill unicast-route verbose

Destinations: 2        Unicast routes: 2

Destination: 0xfa1b

NextHop count: 0             Neighbor ID: 0x0000

Destination: 0x899b

NextHop count: 1             Neighbor ID: 0x0101

Interface: GE1/0/1           NextHop: Direct

表1-15 display trill unicast-route命令显示信息描述表

字段

描述

Destinations

目的RB的数量

Unicast routes

单播路由的条数

Destination

目的RB的Nickname

Interface

出端口

NextHop

下一跳的Nickname

NextHop count

下一跳的数量

Neighbor ID

下一跳关联的邻居编号

**TRILL \-- TRILL配置命令 \-- display trill vr**

------------------------------------------------------------------------

**[display** **trill** **vr**]命令用来显示TRILL VR（Virtual Router，虚拟路由器）的信息。

【命令】

**[display** **trill** **vr** [ **ipv6**   **verbose** [ **vrid** *vr-id* [ **interface** *interface-type interface-number*  ] \| **vrid** *vr-id* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6**]：显示IPv6 TRILL VR的信息。如果未指定本参数，将显示IPv4 TRILL VR的信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示摘要信息。

**[vrid** *vr-id*]：显示指定VR的信息。*vr-id*表示VR的编号，取值范围为1～255。如果未指定本参数，将显示所有VR的信息。

**[interface** *interface-type* *interface-number*]：显示指定端口上的信息，*interface-type* *interface-number*为端口类型和端口编号。如果未指定本参数，将显示所有端口上的信息。

【举例】

\# 显示所有IPv4 TRILL VR的摘要信息。

\<Sysname\> display trill vr

VRID    Partner RB         State       Local

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1       0606.0606.0606     Backup      Y

        0808.0808.0808     Master      N

2       0606.0606.0606     Backup      Y

        0808.0808.0808     Master      N

3       0606.0606.0606     Backup      Y

        0808.0808.0808     Master      N

\# 显示所有IPv4 TRILL VR的详细信息。

\<Sysname\> display trill vr verbose

IPv4 virtual router information:

  VRID: 1     Virtual MAC: 0cda-41ed-be01

    Partner RB information:

      System ID: 0606.0606.0606

        State: Backup

        Local: Y

      System ID: 0808.0808.0808

        State: Master

        Local: N

    Interface information:

      Interface: Vlan-interface10

        Virtual IP: 193.1.1.1

        Track index: 11     State: Positive

表1-16 display trill vr命令显示信息描述表

字段

描述

VRID

VR的编号

Partner RB

VR中成员RB的System ID

State

该成员RB在VR中的状态，包括Master、Backup和Inactive三种

Local

该成员RB是否为当前设备：

·Y：表示是当前设备

·N：表示不是当前设备

IPv4 virtual router information

IPv4 TRILL VR的信息

IPv6 virtual router information

IPv6 TRILL VR的信息

Virtual MAC

VR的虚拟MAC地址

Partner RB information

VR中成员RB的信息

System ID

该成员RB的System ID

Interface information

VR所在接口的信息

Interface

接口的名称

Virtual IP

VR的虚拟IP地址

Track index

VR监测的Track项（配置了**trill** **vr** **vrid** **track**命令后，才会显示此项）

State

Track项的状态（配置了**trill** **vr** **vrid** **track**命令后，才会显示此项）：

·Negative：表示无效状态

·Positive：表示有效状态

·NotReady：表示尚未就绪状态

**TRILL \-- TRILL配置命令 \-- display trill vr-adjacent-table**

------------------------------------------------------------------------

**[display**]**trill** **vr-****adjacent-table**命令用来显示TRILL VR邻接表信息。

【命令】

**[display**]**trill** **vr-****adjacent-table**\**[count**[ \| ]**nickname** *nickname* **interface** *interface-type* *interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[count**]：显示表项的数量。

**[nickname** *nickname* **interface** *interface-type* *interface-number*]：显示指定RB指定端口上的信息。*nickname*表示RB的Nickname，为0x1～0xFFFE的十六进制数；*interface-type interface-number*为端口类型和端口编号。如果未指定本参数，将显示所有RB所有端口上的信息。

【举例】

\# 显示TRILL VR邻接表所有表项的信息。

\<Sysname\> display trill vr-adjacent-table

NextHop     MAC address       Interface

0x899b      00e0-fc58-123a    GE1/0/1

\# 显示TRILL VR邻接表的表项数量。

\<Sysname\> display trill vr-adjacent-table count

Total number of TRILL VR ADJ entries: 3

表1-17 display trill vr-adjacent-table命令显示信息描述表

字段

描述

NextHop

报文转发下一跳RB的Nickname

MAC address

报文转发下一跳RB的MAC地址

Interface

报文的出端口

Total number of TRILL VR ADJ entries

TRILL VR邻接表的表项数量

**TRILL \-- TRILL配置命令 \-- display trill vr-fib**

------------------------------------------------------------------------

**[display**]**trill** **vr-fib**命令用来显示TRILL VR单播转发表信息。

【命令】

**[display**]**trill** **vr-fib** \**[count**[ \| ]**mac** *mac-address* **vlan** *vlan-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[count**]：显示表项的数量。

**[mac**] *mac-address* **vlan** *vlan-id*：显示指定MAC地址在指定VLAN内的信息。*mac-address*为MAC地址；*vlan-id*的取值范围为1～4094。如果未指定本参数，将显示所有MAC地址在所有VLAN内的信息。

【举例】

\# 显示TRILL VR单播转发表所有表项的信息。

\<Sysname\> display trill vr-fib

MAC address    VLAN NextHop   Interface

0cad-41ed-be01 1    0x2a5c    GE1/0/1

0cad-41ed-bf01 2    0x2a5c    GE1/0/2

\# 显示TRILL VR单播转发表的表项数量。

\<Sysname\> display trill vr-fib count

Total number of TRILL VR FIB destinations: 2

Total number of TRILL VR FIB entries: 2

表1-18 display trill vr-fib命令显示信息描述表

字段

描述

MAC address

目的MAC地址

VLAN

转发的VLAN编号

NextHop

下一跳RB的Nickname

Interface

报文的出端口

Total number of TRILL VR FIB destinations

TRILL VR单播转发表中目的MAC地址的数量

Total number of TRILL VR FIB entries

TRILL VR单播转发表的表项数量

**TRILL \-- TRILL配置命令 \-- display trill vr-route**

------------------------------------------------------------------------

**[display** **trill** **vr-route**]命令用来显示TRILL VR多端口单播MAC地址表信息。

【命令】

**[display** **trill** **vr-route** [ **vrid** *vrid*   **vlan** *vlan-id*   **mac-address** *mac-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vrid** *vr-id*]：显示指定VR的信息。*vr-id*表示VR的编号，取值范围为1～255。如果未指定本参数，将显示所有VR的信息。

**[vlan***vlan-id*]：显示指定VLAN内的信息，*vlan-id*的取值范围为1～4094。如果未指定本参数，将显示所有VLAN内的信息。

**[mac-address** *mac-address*]：显示指定MAC地址的信息，*mac-address*为MAC地址。如果未指定本参数，将显示所有MAC地址的信息。

【举例】

\# 显示TRILL VR多端口单播MAC地址表所有表项的信息。

\<Sysname\> display trill vr-route

VRID    MAC address     VLAN    Port

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

1       0cda-41ed-be01  1       GE1/0/1

                        2       GE1/0/3

                        3       GE1/0/4

2       0cda-41ed-be02  1       GE1/0/2

                        3       GE1/0/5

表1-19 display trill vr-route命令显示信息描述表

字段

描述

VRID

VR的编号

MAC address

VR的虚拟MAC地址

VLAN

VLAN的编号

Port

出端口

**TRILL \-- TRILL配置命令 \-- flash-flood**

------------------------------------------------------------------------

**[flash-flood**]命令用来开启LSP快速扩散功能。

**[undo** **flash-flood**]命令用来关闭LSP快速扩散功能。

【命令】

**[flash-flood**[[ **flood-count** *flooding-count* \| **max-timer-interval** *flooding-interval* ] \*]]

**[undo** **flash-flood**]

【缺省情况】

LSP快速扩散功能处于关闭状态。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[flood-count** *flooding-count*]：表示扩散次数，取值范围为1～15，缺省值为5。

**[max-timer-interval** *flooding-interval*]：表示开始进行扩散的延迟时间，取值范围为0～50000，单位为毫秒，缺省值为0毫秒（表示立即扩散）。

【使用指导】

LSP的变化会导致重新计算SPF。开启本功能后，设备会将导致SPF重新计算的LSP快速扩散出去，从而有效缩短拓扑变化时全网设备上LSDB不一致的时间，提高全网的快速收敛性能。

【举例】

\# 开启LSP快速扩散功能，并配置LSP快速扩散的个数为10个、延迟时间为10毫秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill flash-flood flood-count 10 max-timer-interval 10

**TRILL \-- TRILL配置命令 \-- flush-policy difference**

------------------------------------------------------------------------

**[flush-policy** **difference**]命令用来配置TRILL组播路由采用差异化下刷策略。

**[undo** **flush-policy** **difference**]命令用来恢复缺省情况。

【命令】

**[flush-policy** **difference**]

**[undo** **flush-policy** **difference**]

【缺省情况】

TRILL组播路由未采用差异化下刷策略。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

TRILL组播路由表项分为RB表项、RB＋VLAN表项和RB＋VLAN＋MAC表项三级。在特定的组网和配置下，如果TRILL组播路由相关的下级表项与上一级表项完全相同，此时只需下刷上一级表项便可正确指导转发，这便是差异化下刷策略，即仅当下级表项与上一级表项不同时才下刷。

例如：若一棵TRILL分发树的RB表项、RB＋VLAN 1表项和RB＋VLAN 1＋MAC表项均相同，则只需下刷RB表项即可，VLAN 1中的TRILL数据报文可以直接查找RB表项进行转发。

需要注意的是，本命令只能应用在RB表项、RB＋VLAN表项和RB＋VLAN＋MAC表项的出端口和本地标识都相同的特殊组网中，否则将导致大量表项同一时间集中下刷而使性能下降。

【举例】

\# 配置TRILL组播路由采用差异化下刷策略。

\<Sysname\> system-view

Sysname trill

Sysname-trill flush-policy difference

**TRILL \-- TRILL配置命令 \-- graceful-restart**

------------------------------------------------------------------------

**[graceful-restart**]命令用来使能TRILL的GR能力。

**[undo graceful-restart**]命令用来关闭TRILL的GR能力。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

TRILL的GR能力处于关闭状态。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能TRILL的GR能力。

\<Sysname\> system-view

Sysname trill

Sysname-trill graceful-restart

**TRILL \-- TRILL配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

**[graceful-restart interval**]命令用来配置TRILL的GR重启间隔。

**[undo graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[graceful-restart interval **]*interval*

**[undo graceful-restart interval**]

【缺省情况】

TRILL的GR重启间隔为300秒。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示TRILL的GR重启间隔，取值范围为30～1800，单位为秒。

【举例】

\# 配置TRILL的GR重启间隔为120秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill graceful-restart interval 120

**TRILL \-- TRILL配置命令 \-- graceful-restart suppress-sa**

------------------------------------------------------------------------

**[graceful-restart** **suppress-sa**]命令用来配置TRILL GR重启时抑制SA（Suppress-Advertisement）位置位。

**[undo** **graceful-restart** **suppress-sa**]命令用来恢复缺省情况。

【命令】

**[graceful-restart** **suppress-sa**]

**[undo** **graceful-restart** **suppress-sa**]

【缺省情况】

TRILL GR重启时SA位将被置位。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

SA表示抑制邻接标志位，将其置位的主要目的是避免出现路由黑洞，例如在启动或重启时没有保留本地转发表，此时如果GR Helper将报文送到设备来进行转发将造成严重的丢包现象。在这种情况下，GR Restarter发送的Hello报文中必须将SA位置位，而GR Helper收到这种SA位被置位的Hello报文后，将不会把发送该Hello报文的GR Restarter放入LSP中扩散出去。而对于启动速度要求较高的场景，则可以不配置TRILL GR重启时抑制SA位置位。

【举例】

\# 配置TRILL GR重启时抑制SA位置位。

\<Sysname\> system-view

Sysname trill

Sysname-trill graceful-restart suppress-sa

**TRILL \-- TRILL配置命令 \-- ingress assign-delay**

------------------------------------------------------------------------

**[ingress** **assign-delay**]命令用来配置入流量分配给新TRILL分发树的延时时间。

**[undo** **ingress** **assign-delay**]命令用来恢复缺省情况。

【命令】

**[ingress** **assign-delay** *delay*]

**[undo** **ingress** **assign-delay**]

【缺省情况】

入流量分配给新TRILL分发树的延时时间为300秒。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：入流量分配给新TRILL分发树的延时时间，取值范围为1～3600，单位为秒。

【使用指导】

当入流量选择TRILL分发树的策略为负载均衡优先时，当新增一棵TRILL分发树时，为了让所有TRILL分发树来进行流量分担，Ingress RB需要将部分已分配给其它树的AVF VLAN重新分配给新树，以使新树分担本地流量的转发。但在其他RB尚未声明使用新树前，本地流量是无法使用新树进行转发的。因此，可以通过本命令来设置新树生效后，入流量分配给该树的延时时间。

【举例】

\# 配置入流量分配给新TRILL分发树的延时时间为600秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill ingress assign-delay 600

【相关命令】

·**ingress** **assign-rule** **load-balancing**

**TRILL \-- TRILL配置命令 \-- ingress assign-rule load-balancing**

------------------------------------------------------------------------

**[ingress** **assign-rule** **load-balancing**]命令用来配置入流量选择TRILL分发树的策略为负载均衡优先。

**[undo** **ingress** **assign-rule**]命令用来恢复缺省情况。

【命令】

**[ingress** **assign-rule** **load-balancing**]

**[undo** **ingress** **assign-rule**]

【缺省情况】

入流量选择TRILL分发树的策略为稳定优先。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当新增或删除TRILL分发树时，入流量选择TRILL分发树的策略缺省为稳定优先，即尽量保持原分发树不变；如果想让全部分发树都对入流量进行负载分担，则可将策略配置为负载均衡优先。

需要注意的是，本命令只影响减少AVF VLAN时对剩余AVF VLAN选择TRILL分发树的策略。

【举例】

\# 配置入表项选择TRILL分发树的策略为负载均衡优先。

\<Sysname\> system-view

Sysname trill

Sysname-trill ingress assign-rule load-balancing

**TRILL \-- TRILL配置命令 \-- log-peer-change enable**

------------------------------------------------------------------------

**[log-peer-change** **enable**]命令用来开启TRILL邻接状态输出开关。

**[undo** **log-peer-change** **enable**]命令用来关闭TRILL邻接状态输出开关。

【命令】

**[log-peer-change** **enable**]

**[undo** **log-peer-change** **enable**]

【缺省情况】

邻接状态输出开关处于开启状态。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启邻接状态输出开关后，TRILL邻接状态的变化会输出到配置终端上。

【举例】

\# 关闭TRILL邻接状态输出开关。

\<Sysname\> system-view

Sysname trill

Sysname-trill undo log-peer-change enable

**TRILL \-- TRILL配置命令 \-- lsp-length originate**

------------------------------------------------------------------------

**[lsp-length** **originate**]命令用来配置RB可生成的LSP最大长度。

**[undo** **lsp-length** **originate**]命令用来恢复缺省情况。

【命令】

**[lsp-length** **originate** *size*]

**[undo** **lsp-length** **originate**]

【缺省情况】

RB可生成的LSP最大长度为1458字节。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：表示RB可生成的LSP最大长度，取值范围为512～16384，单位为字节。

【使用指导】

LSP的实际最大长度将由本配置值、端口的MTU值和所有其它RB在LSP中携带的自身能生成的LSP最大长度这三者中的最小值来决定。

需要注意的是，RB可生成的LSP最大长度不得大于RB可接收的LSP最大长度，否则系统将提示出错。

【举例】

\# 配置RB可生成的LSP最大长度为1024字节。

\<Sysname\> system-view

Sysname trill

Sysname-trill lsp-length originate 1024

【命令】

·**lsp-length** **receive**

**TRILL \-- TRILL配置命令 \-- lsp-length receive**

------------------------------------------------------------------------

**[lsp-length** **receive**]命令用来配置RB可接收的LSP最大长度。

**[undo** **lsp-length** **receive**]命令用来恢复缺省情况。

【命令】

**[lsp-length** **receive** *size*]

**[undo** **lsp-length** **receive**]

【缺省情况】

RB可接收的LSP最大长度为1492字节。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：表示RB可接收的LSP最大长度，取值范围为512～16384，单位为字节。

【使用指导】

需要注意的是，RB可接收的LSP最大长度不得小于RB可生成的LSP最大长度，否则系统将提示出错。

【举例】

\# 配置RB可接收的LSP最大长度为1024字节。

\<Sysname\> system-view

Sysname trill

Sysname-trill lsp-length receive 1024

【命令】

·**lsp-length originate**

**TRILL \-- TRILL配置命令 \-- max-unicast-load-balancing**

------------------------------------------------------------------------

**[max-unicast-load-balancing**]命令用来配置TRILL单播等价多路径的最大路径数。

**[undo** **max-unicast-load-balancing**]命令用来恢复缺省情况。

【命令】

**[max-unicast-load-balancing** *number*]

**[undo** **max-unicast-load-balancing**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：表示TRILL单播等价多路径的最大路径数，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。取值为1表示不进行负载分担。

【举例】

\# 配置TRILL单播等价多路径的最大路径数为3条。

\<Sysname\> system-view

Sysname trill

Sysname-trill max-unicast-load-balancing 3

**TRILL \-- TRILL配置命令 \-- multicast multi-thread enable**

------------------------------------------------------------------------

**[multicast** **multi-thread** **enable**]命令用来开启TRILL分发树计算支持多线程功能。

**[undo** **multicast** **multi-thread** **enable**]命令用来关闭TRILL分发树计算支持多线程功能。

【命令】

**[multicast** **multi-thread** **enable**]

**[undo** **multicast** **multi-thread** **enable**]

【缺省情况】

TRILL分发树计算支持多线程功能处于关闭状态。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在多核CPU设备上，可以开启TRILL分发树计算支持多线程功能，以提升TRILL分发树的计算效率。开启本功能后，每棵TRILL分发树将分别使用一个线程进行计算。

需要注意的是：

·在单核CPU设备上开启本功能后，并不一定会带来效率的提升。

·开启或关闭本功能，将会清除TRILL进程当前的动态运行数据。

【举例】

\# 开启TRILL分发树计算支持多线程功能。

\<Sysname\> system-view

Sysname trill

Sysname-trill multicast multi-thread enable

【相关命令】

·**reset** **trill**

**TRILL \-- TRILL配置命令 \-- multicast-ecmp enable**

------------------------------------------------------------------------

**[multicast-ecmp** **enable**]命令用来开启TRILL组播等价多路径功能。

**[undo** **multicast-ecmp** **enable**]命令用来关闭TRILL组播等价多路径功能。

【命令】

**[multicast-ecmp** **enable**  **p2p-ignore** ]

**[undo** **multicast-ecmp** **enable**]

【缺省情况】

TRILL组播等价多路径功能处于关闭状态。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[p2p-ignore**]：表示在伪节点被旁路的等价路径上，只使用一条路径转发组播报文。如果未指定本参数，表示在伪节点被旁路的等价路径上，使用全部等价路径转发组播报文，这样可在最大程度上实现组播流量的负载分担。但当与第三方厂商的设备互通时，可能需要指定本参数以保证互通成功。

【使用指导】

·当TRILL组播等价多路径功能关闭时，由于根桥不同而使各分发树拓扑不同，从而可在一定程度上实现组播流量的负载分担，但并未利用开销相同的等价路径来分担流量；当开启该功能后，TRILL可将这些等价路径分给不同的分发树，从而实现更好的负载分担效果。

·本功能的配置在TRILL网络中所有RB上应完全一致，否则可能导致组播流量不通。

【举例】

\# 开启TRILL组播等价多路径功能。

\<Sysname\> system-view

Sysname trill

Sysname-trill multicast-ecmp enable

**TRILL \-- TRILL配置命令 \-- nickname**

------------------------------------------------------------------------

**[nickname**]命令用来配置RB的Nickname。

**[undo** **nickname**]命令用来恢复缺省情况。

【命令】

**[nickname** *nickname* [ **priority** *priority* ]]

**[undo** **nickname** *nickname*]

【缺省情况】

RB的Nickname由系统自动分配，其持有Nickname的优先级为64。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nickname*]：表示RB的Nickname，为0x1～0xFFBF的十六进制数。

**[priority** *priority*]：表示RB持有Nickname的优先级，取值范围为129～255，缺省值为192。

【使用指导】

Nickname是RB在TRILL网络中的地址。如果TRILL网络中不同RB拥有相同的Nickname，则优先级较高者保留此Nickname；如果优先级也相同，则System ID较大者保留此Nickname，其余RB再由系统为其自动分配一个新的Nickname。

【举例】

\# 配置RB的Nickname为0x0001，其持有Nickname的优先级为198。

\<Sysname\> system-view

Sysname trill

Sysname-trill nickname 0001 priority 198

**TRILL \-- TRILL配置命令 \-- reset trill**

------------------------------------------------------------------------

**[reset** **trill**]命令用来清除TRILL进程当前的动态运行数据。

【命令】

**[reset** **trill**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除TRILL进程当前的动态运行数据。

\<Sysname\> reset trill

**TRILL \-- TRILL配置命令 \-- set ingress-load-balancing**

------------------------------------------------------------------------

**[set** **ingress-load-balancing**]命令用来对TRILL分发树转发的流量进行手工均衡。

【命令】

**[set** **ingress-load-balancing**]

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当入流量选择TRILL分发树的策略为稳定优先时，当VLAN在各TRILL分发树上分布不均衡时，可使用本命令对TRILL分发树转发的流量进行手工均衡。

需要注意的是，执行本命令可能影响当前某些报文的转发。

【举例】

\# 对TRILL分发树转发的流量进行手工均衡。

\<Sysname\> system-view

Sysname trill

Sysname-trill set ingress-load-balancing

【相关命令】

·**ingress** **assign-rule** **load-balancing**

**TRILL \-- TRILL配置命令 \-- set overload**

------------------------------------------------------------------------

**[set** **overload**]命令用来将LSP的过载标志位置位并配置保持置位状态的时间。

**[undo** **set** **overload**]命令用来清除过载标志位。

【命令】

**[set** **overload** [ *timeout* ]]

**[undo** **set** **overload**]

【缺省情况】

LSP的过载标志位未置位。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timeout*]：表示过载标志位保持置位状态的时间，取值范围为5～3600，单位为秒。缺省值为无穷大，即一直保持置位状态直至被清除。

【使用指导】

需要注意的是，请不要在作为TRILL分发树根桥的RB上配置本命令，否则将导致使用该根桥的流量转发不通。

【举例】

\# 将LSP的过载标志位置位，并配置保持置位状态的时间为1200秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill set overload 1200

**TRILL \-- TRILL配置命令 \-- snmp context-name**

------------------------------------------------------------------------

**[snmp**] **context-name**命令用来配置管理TRILL的SNMP实体所使用的上下文名称。

**[undo** **snmp** ]**context-name**命令用来恢复缺省情况。

【命令】

**[snmp**] **context-name** *context-name*

**[undo** **snmp** ]**context-name**

【缺省情况】

没有配置管理TRILL的SNMP实体所使用的上下文名称。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：上下文的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

TRILL使用IS-IS的MIB（Management Information Base，管理信息库）对NMS（Network Management System，网络管理系统）提供TRILL对象的管理，但标准IS-IS MIB中定义的MIB为单实例管理对象，无法同时对IS-IS和TRILL进行管理。因此，参考RFC 4750中对OSPF多实例的管理方法，为管理TRILL定义一个上下文名称，以区分来自NMS的SNMP请求是要对IS-IS还是TRILL进行管理。需要注意的是，由于上下文名称只是SNMPv3独有的概念，因此对于SNMPv1/v2c，会将团体名映射为上下文名称以对不同协议进行区分。

【举例】

\# 配置管理TRILL的SNMP实体所使用的上下文名称为trill。

\<Sysname\> system-view

Sysname trill

Sysname-trill snmp context-name trill

**TRILL \-- TRILL配置命令 \-- snmp-agent trap enable trill**

------------------------------------------------------------------------

**[snmp-agent**] **trap** **enable** **trill**命令用来开启TRILL的告警功能。

**[undo**] **snmp-agent** **trap** **enable** **trill**命令用来关闭TRILL的告警功能。

【命令】

**[snmp-agent**] **trap** **enable** **trill**[[ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]**maxarea-mismatch**[ \| **new-drb** \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** ] \*]

**[undo**]**snmp-agent** **trap** **enable** **trill**[[ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]**maxarea-mismatch**[ \| **new-drb** \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** ] \*]

【缺省情况】

TRILL的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adjacency-state-change**]：表示TRILL邻接状态变化的告警信息。

**[area-mismatch**]：表示Hello报文区域地址不匹配的告警信息。

**[buffsize-mismatch**]：表示LSP长度与产生缓冲区大小不匹配的告警信息。

**[id-length-mismatch**]：表示TRILL报文中System ID长度不匹配的告警信息。

**[lsdboverload-state-change**]：表示LSDB过载状态变化的告警信息。

**[lsp-parse-error**]：表示LSP解析错误的告警信息。

**[lsp-size-exceeded**]：表示超大LSP导致泛洪失败的告警信息。

**[max-seq-exceeded**]：表示LSP序列号超过最大序列号的告警信息。

**[maxarea-mismatch**]：表示Hello报文最大区域地址不匹配的告警信息。

**[new-drb**]：表示成为新DRB的告警信息。

**[own-lsp-purge**]：表示尝试清除本地LSP的告警信息。

**[protocol-support**]：表示报文协议支持类型不匹配的告警信息。

**[rejected-adjacency**]：表示Hello报文邻接不匹配丢弃的告警信息。

**[skip-sequence-number**]：表示跳过已产生过的LSP序列号的告警信息。

**[topology-change**]：表示AVF状态变化的告警信息。

**[version-skew**]：表示Hello报文版本号不匹配的告警信息。

【使用指导】

如果未指定任何可选参数，表示开启或关闭TRILL的全部告警功能。

开启了TRILL的告警功能之后，TRILL会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 关闭TRILL的全部告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable trill

**TRILL \-- TRILL配置命令 \-- system-id**

------------------------------------------------------------------------

**[system-id**]命令用来配置RB的System ID。

**[undo** **system-id**]命令用来恢复缺省情况。

【命令】

**[system-id** *system-id*]

**[undo** **system-id**]

【缺省情况】

RB启动后会根据自己的MAC地址自动生成一个System ID。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[system-id*]：表示RB的System ID，格式为xxxx.xxxx.xxxx，x代表十六进制数。

【使用指导】

需要注意的是，如果用户为RB新配置的System ID与原有的不同，系统将重置TRILL进程。

【举例】

\# 配置RB的System ID为1010.1020.1030。

\<Sysname\> system-view

Sysname trill

Sysname-trill system-id 1010.1020.1030

**TRILL \-- TRILL配置命令 \-- timer lsp-generation**

------------------------------------------------------------------------

**[timer** **lsp-generation**]命令用来配置LSP重新生成的时间间隔。

**[undo** **timer** **lsp-generation**]命令用来恢复缺省情况。

【命令】

**[timer** **lsp-generation** *maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo** **timer** **lsp-generation**]

【缺省情况】

LSP重新生成的最大时间间隔为2秒，最小时间间隔为10毫秒，时间间隔惩罚增量为20毫秒。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：表示LSP重新生成的最大时间间隔，取值范围为1～120，单位为秒。

*[minimum-interval*]：表示LSP重新生成的最小时间间隔，取值范围为10～60000，单位为毫秒，必须为10的整数倍。最小时间间隔必须小于最大时间间隔。

*[incremental-interval*]：表示LSP重新生成的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒，必须为10的整数倍。时间间隔惩罚增量必须小于最大时间间隔。

【使用指导】

网络拓扑的变化会导致重新生成LSP，通过调节LSP重新生成的时间间隔，可以抑制网络频繁变化可能导致的对带宽资源和设备资源的过多占用。在网络变化不频繁的情况下，将LSP重新生成的时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

【举例】

\# 配置LSP重新生成的最大时间间隔为10秒，最小时间间隔为100毫秒，时间间隔惩罚增量为200毫秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill timer lsp-generation 10 100 200

**TRILL \-- TRILL配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

**[timer** **lsp-max-age**]命令用来配置LSP的最大生存时间。

**[undo** **timer** **lsp-max-age**]命令用来恢复缺省情况。

【命令】

**[timer** **lsp-max-age** *time*]

**[undo** **timer** **lsp-max-age**]

【缺省情况】

LSP的最大生存时间为1200秒。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：表示LSP的最大生存时间，取值范围为3～65535，单位为秒。

【使用指导】

当RB生成一个LSP时，会将该LSP的最大生存时间作为LSP中的剩余生存时间告知其他RB。当LSDB中一个LSP的剩余生存时间为0时，说明该LSP已失效，RB将从LSDB中删除该LSP的内容，只保留其摘要，并将该LSP的剩余生存时间置0后泛洪给其他RB以清除此LSP。

需要注意的是，由于LSP的实际刷新时间会受LSP的最小发送间隔和一次发送LSP的最大数目的影响，因此请合理配置LSP的最大生存时间和刷新周期，以免LSP被意外老化。

【举例】

\# 配置LSP的最大生存时间为1500秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill timer lsp-max-age 1500

【相关命令】

·**timer** **lsp-refresh**

·**trill** **timer** **lsp**

**TRILL \-- TRILL配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

**[timer** **lsp-refresh**]命令用来配置LSP的刷新周期。

**[undo** **timer** **lsp-refresh**]命令用来恢复缺省情况。

【命令】

**[timer**] **lsp-refresh** *time*

**[undo**] **timer** **lsp-refresh**

【缺省情况】

LSP的刷新周期为900秒。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：表示LSP的刷新周期，取值范围为1～65534，单位为秒。

【使用指导】

对于一个本地生成的LSP，当其剩余生存时间≤（最大生存时间－刷新周期）时，即使该LSP中的内容没有任何改变，也要重新更新此LSP，这样可避免网络中的LSP老化太频繁，保证网络稳定性。

需要注意的是，由于LSP的实际刷新时间会受LSP的最小发送间隔和一次发送LSP的最大数目的影响，因此请合理配置LSP的最大生存时间和刷新周期，以免LSP被意外老化。

【举例】

\# 配置LSP的刷新周期为1000秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill timer lsp-refresh 1000

【相关命令】

·**timer** **lsp-max-age**

·**trill** **timer** **lsp**

**TRILL \-- TRILL配置命令 \-- timer spf**

------------------------------------------------------------------------

**[timer** **spf**]命令用来配置TRILL使用SPF算法进行路由计算的时间间隔。

**[undo** **timer** **spf**]命令用来恢复缺省情况。

【命令】

**[timer** **spf** *maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo** **timer** **spf**]

【缺省情况】

TRILL使用SPF算法进行路由计算的最大时间间隔为10秒，最小时间间隔为10毫秒，时间间隔惩罚增量为20毫秒。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：表示最大时间间隔，取值范围为1～120，单位为秒。

*[minimum-interval*]：表示最小时间间隔，取值范围为10～60000，单位为毫秒，必须为10的整数倍。最小时间间隔必须小于最大时间间隔。

*[incremental-interval*]：表示时间间隔惩罚增量，取值范围为10～60000，单位为毫秒，必须为10的整数倍。时间间隔惩罚增量必须小于最大时间间隔。

【使用指导】

根据本地维护的LSDB，RB通过SPF算法算出以自己为根的最短路径树，并根据此树决定到达目的网络的下一跳。通过调节SPF算法的时间间隔，可抑制由于网络频繁变化而导致的带宽资源和设备资源的过多占用。

系统在网络变化不频繁时将连续路由计算的时间间隔缩小至*minimum-interval*，而在网络变化频繁时进行相应的惩罚，即增加*incremental-interval*×2^n-2^（n为连续触发路由计算的次数），但最大不超过*maximum-interval*。

【举例】

\# 配置TRILL使用SPF算法进行路由计算的最大时间间隔为15秒，最小时间间隔为100毫秒，时间间隔惩罚增量为200毫秒。

\<Sysname\> system-view

Sysname trill

Sysname-trill timer spf 15 100 200

**TRILL \-- TRILL配置命令 \-- tree-root priority**

------------------------------------------------------------------------

**[tree-root** **priority**]命令用来配置RB作为TRILL分发树根桥的优先级。

**[undo** **tree-root** **priority**]命令用来恢复缺省情况。

【命令】

**[tree-root** **priority** *priority*]

**[undo** **tree-root** **priority**]

【缺省情况】

RB作为TRILL分发树的根桥优先级为32768。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：表示RB作为TRILL分发树根桥的优先级，取值范围为1～65535，数值越大优先级越高。

【举例】

\# 配置RB作为TRILL分发树根桥的优先级为65535。

\<Sysname\> system-view

Sysname trill

Sysname-trill tree-root priority 65535

**TRILL \-- TRILL配置命令 \-- trees calculate**

------------------------------------------------------------------------

**[trees** **calculate**]命令用来配置RB希望整网计算的TRILL分发树数量。

**[undo** **trees** **calculate**]命令用来恢复缺省情况。

【命令】

**[trees** **calculate** *count*]

**[undo** **trees** **calculate**]

【缺省情况】

RB希望整网计算的TRILL分发树数量为1棵。

【视图】

TRILL视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：表示RB希望整网计算的TRILL分发树数量，取值范围为1～15。

【举例】

\# 配置RB希望整网计算的TRILL分发树数量为2棵。

\<Sysname\> system-view

Sysname trill

Sysname-trill trees calculate 2

**TRILL \-- TRILL配置命令 \-- trill**

------------------------------------------------------------------------

**[trill**]命令用来全局使能TRILL协议，并进入TRILL视图。

**[undo** **trill**]命令用来全局关闭TRILL协议。

【命令】

**[trill**]

**[undo** **trill**]

【缺省情况】

TRILL协议处于全局关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 全局使能TRILL协议，并进入TRILL视图。

\<Sysname\> system-view

Sysname trill

Sysname-trill

**TRILL \-- TRILL配置命令 \-- trill announcing-vlan**

------------------------------------------------------------------------

**[trill** **announcing-vlan**]命令用来配置通告VLAN。

**[undo** **trill** **announcing-vlan**]命令用来恢复缺省情况。

【命令】

**[trill**[ **announcing-vlan** { *vlan-list* \| **null** }]]

**[undo**[ **trill** **announcing-vlan** { *vlan-list* \| **null** }]]

【缺省情况】

没有配置通告VLAN，此时通告VLAN与使能VLAN的范围相同。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-list*]：通告VLAN的列表，表示多个通告VLAN。表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]。其中，*vlan-id*为VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

**[null**]：表示通告VLAN为空集，即不包含任何VLAN。

【使用指导】

RB之间的Hello报文，是通过一个VLAN集合来交互的，具体来说：

·DRB在以下VLAN集合中发送Hello报文：使能VLAN ∩（指定VLAN ∪通告VLAN）。

·非DRB在以下VLAN集合中发送Hello报文：使能VLAN ∩（指定VLAN ∪（通告VLAN ∩ AVF VLAN））。

由于TRILL端口会在上述VLAN集合的每个VLAN内都发送Hello报文，这样当VLAN集合较大时，设备会因发送大量Hello报文而占用过多CPU资源，从而无法及时处理其它协议的报文。为了避免这种情况，可以通过减少通告VLAN的范围来缩小VLAN集合的范围。

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置通告VLAN为VLAN 10～20。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill announcing-vlan 10 to 20

\# 配置通告VLAN为空集。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill announcing-vlan null

【相关命令】

·**trill** **designated-vlan**

**TRILL \-- TRILL配置命令 \-- trill bypass-pseudonode enable**

------------------------------------------------------------------------

**[trill** **bypass-pseudonode** **enable**]命令用来开启旁路伪节点功能。

**[undo** **trill** **bypass-pseudonode** **enable**]命令用来关闭旁路伪节点功能。

【命令】

**[trill** **bypass-pseudonode** **enable**]

**[undo** **trill** **bypass-pseudonode** **enable**]

【缺省情况】

旁路伪节点功能处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启本功能后，如果当前端口为DRB且只有一个邻居，则不再生成伪节点的LSP，以减少网络中LSP的数量。

【举例】

\# 在端口GigabitEthernet1/0/1上开启旁路伪节点功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill bypass-pseudonode enable

**TRILL \-- TRILL配置命令 \-- trill cost**

------------------------------------------------------------------------

**[trill** **cost**]命令用来配置TRILL端口的链路开销值。

**[undo** **trill** **cost**]命令用来恢复缺省情况。

【命令】

**[trill** **cost** *value*]

**[undo** **trill** **cost**]

【缺省情况】

TRILL端口的链路开销值为2000。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：表示链路开销值，取值范围为1～16777214。

【使用指导】

对于TRILL端口的链路开销值来说：如果进行了手工配置，则取配置值；如果没有手工配置且自动计算功能处于开启状态，则取自动计算值；如果没有手工配置且自动计算功能处于关闭状态，则取缺省值2000。

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置TRILL端口GigabitEthernet1/0/1的链路开销值为20000。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill cost 20000

【相关命令】

·**auto-cost** **enable**

**TRILL \-- TRILL配置命令 \-- trill designated-vlan**

------------------------------------------------------------------------

**[trill** **designated-vlan**]命令用来配置指定VLAN。

**[undo** **trill** **designated-vlan**]命令用来恢复缺省情况。

【命令】

**[trill** **designated-vlan** *vlan-id*]

**[undo** **trill** **designated-vlan**]

【缺省情况】

没有配置指定VLAN，此时指定VLAN由系统从使能VLAN中自动选出。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：表示指定VLAN，取值范围为1～4094。

【使用指导】

RB之间的Hello报文，是通过一个VLAN集合来交互的，具体来说：

·DRB在以下VLAN集合中发送Hello报文：使能VLAN ∩（指定VLAN ∪通告VLAN）。

·非DRB在以下VLAN集合中发送Hello报文：使能VLAN ∩（指定VLAN ∪（通告VLAN ∩ AVF VLAN））。

而除Hello报文外的其它TRILL协议报文和本地数据报文，则全部通过指定VLAN来交互。因此，请确保所配置的指定VLAN处于使能VLAN的范围内，否则可能导致TRILL邻居无法建立或TRILL数据报文无法转发。

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置指定VLAN为VLAN 2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill designated-vlan 2

【相关命令】

·**trill** **announcing-vlan**

**TRILL \-- TRILL配置命令 \-- trill drb-priority**

------------------------------------------------------------------------

**[trill** **drb-priority**]命令用来配置TRILL端口的DRB优先级。

**[undo** **trill** **drb-priority**]命令用来恢复缺省情况。

【命令】

**[trill** **drb-priority** *priority*]

**[undo** **trill** **drb-priority**]

【缺省情况】

TRILL端口的DRB优先级为64。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：表示TRILL端口的DRB优先级，取值范围为0～127，数值越大优先级越高。

【使用指导】

当网络类型为广播网时，TRILL需要选举DRB：DRB优先级较高的RB优先被选中为DRB；若两个RB的DRB优先级相同，则MAC地址最大者会被选为DRB。

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置TRILL端口GigabitEthernet1/0/1的DRB优先级为2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill drb-priority 2

**TRILL \-- TRILL配置命令 \-- trill enable**

------------------------------------------------------------------------

**[trill** **enable**]命令用来在端口上使能TRILL协议。

**[undo** **trill** **enable**]命令用来在端口上关闭TRILL协议。

【命令】

**[trill** **enable**]

**[undo** **trill** **enable**]

【缺省情况】

端口上的TRILL协议处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

需要注意的是：

·在端口上使能TRILL协议之前，必须先全局使能TRILL协议。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 全局使能TRILL协议，并在端口GigabitEthernet1/0/1上使能TRILL协议。

\<Sysname\> system-view

Sysname trill

Sysname-trill quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill enable

【相关命令】

·**trill**

**TRILL \-- TRILL配置命令 \-- trill link-type**

------------------------------------------------------------------------

**[trill** **link-type**]命令用来配置TRILL端口的类型。

**[undo** **trill** **link-type**]命令用来恢复缺省情况。

【命令】

**[trill** **link-type** { **access** [ **alone**  \| **hybrid** \| **trunk** \| **vr** }]]

**[undo** **trill** **link-type**]

【缺省情况】

TRILL端口的类型为Access类型（非Alone属性）。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[access** [ **alone** ]]：表示Access类型。如果未指定**alone**参数，表示非Alone属性的Access端口，此类端口只能处理本地数据报文和Hello报文；如果指定了**alone**参数，表示Alone属性的Access端口，此类端口不会收、发Hello报文，不参与DRB选举和AVF协商。

**[hybrid**]：表示Hybrid类型。该类型的端口同时具有Access和Trunk的属性，能够处理本地数据报文和过路数据报文。

**[trunk**]：表示Trunk类型。该类型的端口能够处理过路数据报文和部分二层协议报文（如LLDP报文），不能处理本地数据报文。

**[vr**]：表示VR类型。该类型的端口是一种特殊的虚拟路由端口，除了可以和Trunk类型端口一样转发TRILL数据报文外，还可以转发非TRILL封装的三层单播数据报文和非TRILL封装的二、三层组播数据报文。

【使用指导】

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 配置TRILL端口GigabitEthernet1/0/1的类型为Trunk类型。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill link-type trunk

**TRILL \-- TRILL配置命令 \-- trill timer avf-inhibited**

------------------------------------------------------------------------

**[trill** **timer** **avf-inhibited**]命令用来配置环路避免的抑制时间。

**[undo** **trill** **timer** **avf-inhibited**]命令用来恢复缺省情况。

【命令】

**[trill** **timer** **avf-inhibited** *time*]

**[undo** **trill** **timer** **avf-inhibited**]

【缺省情况】

环路避免的抑制时间为30秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：表示环路避免的抑制时间，取值范围为0～30，单位为秒。

【使用指导】

AVF的存在保证了在一条链路上与一个VLAN相关的报文，只会有唯一的出口或入口，其他RB收到与该VLAN相关的报文时将不做任何处理。然而，当RB发现链路上的根桥发生了变化，或其他RB宣称的AVF与本RB的AVF发生冲突时，会将相关的AVF抑制一段时间以避免环路的产生。抑制时间超时后，如果本RB仍是该VLAN的AVF，则重新履行AVF的职能。

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\#在端口GigabitEthernet1/0/1上配置环路避免的抑制时间为20秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill timer avf-inhibited 20

**TRILL \-- TRILL配置命令 \-- trill timer csnp**

------------------------------------------------------------------------

**[trill** **timer** **csnp**]命令用来配置CSNP报文的发送间隔。

**[undo** **trill** **timer** **csnp**]命令用来恢复缺省情况。

【命令】

**[trill** **timer** **csnp** *interval*]

**[undo** **trill** **timer** **csnp**]

【缺省情况】

CSNP报文的发送间隔为10秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示CSNP报文的发送间隔，取值范围为1～600，单位为秒。

【使用指导】

当网络类型为广播网时，DRB定期发送CSNP报文进行全网的LSDB同步。CSNP报文记录了本地LSDB中的所有LSP摘要，当一个RB收到一个CSNP报文时，就会与本地的LSDB进行比较，检查其中的LSP是否有老化和缺失。如果CSNP报文中有某个LSP摘要而本地LSDB中没有，RB将发送PSNP报文以请求获取该LSP的信息。

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上配置CSNP报文的发送间隔为15秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill timer csnp 15

**TRILL \-- TRILL配置命令 \-- trill timer hello**

------------------------------------------------------------------------

**[trill** **timer** **hello**]命令用来配置Hello报文的发送间隔。

**[undo** **trill** **timer** **hello**]命令用来恢复缺省情况。

【命令】

**[trill** **timer** **hello** *interval*]

**[undo** **trill** **timer** **hello**]

【缺省情况】

Hello报文的发送间隔为10秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示Hello报文的发送间隔，取值范围为1～255，单位为秒。

【使用指导】

RB定期发送Hello报文以维持邻接关系。Hello报文的发送间隔越短，网络收敛越快，但也会占用更多的系统资源。

Hello报文的发送间隔与失效数目的乘积为邻接关系保持时间，即RB监测到链路失效并进行路由重计算的时间。RB通过Hello报文将邻接关系保持时间通知给其邻居，若该邻居在邻接关系保持时间内未收到此报文，便宣告邻接关系失效。

本命令用来配置RB发送Hello报文的时间间隔，而DRB发送Hello报文的时间间隔则为RB的1/3，以保证DRB失效后可被快速检测到。

需要注意的是：

·Hello报文的发送间隔与失效数目的乘积不允许超过65535。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上配置Hello报文的发送间隔为20秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill timer hello 20

【相关命令】

·**trill** **timer** **holding-multiplier**

**TRILL \-- TRILL配置命令 \-- trill timer holding-multiplier**

------------------------------------------------------------------------

**[trill** **timer** **holding-multiplier**]命令用来配置Hello报文的失效数目。

**[undo** **trill** **timer** **holding-multiplier**]命令用来恢复缺省情况。

【命令】

**[trill** **timer** **holding-multiplier** *count*]

**[undo** **trill** **holding-multiplier**]

【缺省情况】

Hello报文的失效数目为3个。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：表示Hello报文的失效数目，取值范围为2～1000。

【使用指导】

Hello报文的发送间隔与失效数目的乘积为邻接关系保持时间，即RB监测到链路失效并进行路由重计算的时间。RB通过Hello报文将邻接关系保持时间通知给其邻居，若该邻居在邻接关系保持时间内未收到此报文，便宣告邻接关系失效。

需要注意的是：

·Hello报文的发送间隔与失效数目的乘积不允许超过65535。

·二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上配置Hello报文的失效数目为6。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill timer holding-multiplier 6

【相关命令】

·**trill** **timer** **hello**

**TRILL \-- TRILL配置命令 \-- trill timer lsp**

------------------------------------------------------------------------

**[trill** **timer** **lsp**]命令用来配置LSP的最小发送间隔和一次发送的最大数目。

**[undo** **trill** **timer** **lsp**]命令用来恢复缺省情况。

【命令】

**[trill** **timer** **lsp** *interval* [ **count** *count* ]]

**[undo** **trill** **timer** **lsp**]

【缺省情况】

LSP的最小发送间隔为10毫秒，一次发送LSP的最大数目为5个。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：表示LSP的最小发送间隔，取值范围为10～1000，步长为10，单位为毫秒。

*[count*]：表示一次发送LSP的最大数目，取值范围为1～1000。

【使用指导】

为了避免网络中的LSP老化太频繁，RB需要定期发送LSP，以使全网RB上的LSDB和路由计算保持稳定有效。

需要注意的是，二层以太网接口视图下的配置只对当前端口生效；二层聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上配置LSP的最小发送间隔为500毫秒，一次发送LSP的最大数目为10个。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill timer lsp 500 count 10

**TRILL \-- TRILL配置命令 \-- trill track**

------------------------------------------------------------------------

**[trill** **track**]命令用来配置TRILL监测的Track项。

**[undo** **trill** **track**]命令用来取消TRILL监测的Track项。

【命令】

**[trill** **track** *track-entry-number*]

**[undo** **trill** **track**]

【缺省情况】

TRILL未监测任何Track项。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：表示Track项的序号，取值范围为1～1024。

【举例】

\# 在端口GigabitEthernet1/0/1上配置TRILL监测Track项10。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 trill track 10

**TRILL \-- TRILL配置命令 \-- trill vr ipv6 vrid**

------------------------------------------------------------------------

**[trill** **vr** **ipv6** ]**vrid**命令用来创建IPv6 TRILL VR并为其配置虚拟IPv6地址。

**[undo** **trill** **vr** **ipv6** ]**vrid**命令用来删除指定的IPv6 TRILL VR，或为其删除一个虚拟IPv6地址。

【命令】

**[trill** **vr** **ipv6** **vrid** *vr-id* **virtual-ip** *virtual-address* [ **link-local** ]]

**[undo** **trill** **vr** **ipv6** **vrid** *vr-id* **virtual-ip** [ *virtual-address* [ **link-local**  ]]]

【缺省情况】

不存在任何IPv6 TRILL VR。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vr-id*]：表示VR的编号，取值范围为1～255。

*[virtual-address*]：表示VR的虚拟IPv6地址，必须为IPv6链路本地地址或IPv6全球单播地址。如果未指定本参数，表示删除该VR中的所有虚拟IPv6地址。

**[link-local**]：表示IPv6链路本地地址。当虚拟IPv6地址为IPv6链路本地地址时，必须指定本参数；当虚拟IPv6地址为IPv6全球单播地址，则不得指定本参数，否则系统都将提示出错。

【使用指导】

需要注意的是：

·使用**trill** **vr** **ipv6** **vrid**命令时，如果指定编号的IPv6 TRILL VR不存在，则创建一个新的IPv6 TRILL VR；如果指定编号的IPv6 TRILL VR已存在，则为其更新或添加一个虚拟IPv6地址（对于IPv6链路本地地址是更新，对于IPv6全球单播地址是添加）。

·在一个VLAN接口上必须且只能为一个VR配置一个IPv6链路本地地址；为VR配置的第一个虚拟IPv6地址必须为IPv6链路本地地址，且IPv6链路本地地址必须被最后一个删除。否则，系统都将提示出错。

·在一个VLAN接口上最多可配置4个IPv6 TRILL VR，且所有IPv6 TRILL VR的虚拟IPv6地址总数不得超过16个。

【举例】

\# 在接口Vlan-interface2上先创建IPv6 TRILL VR 2并为其配置虚拟IPv6地址FE80::1，然后再为其添加一个虚拟IPv6地址1::1。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 trill vr ipv6 vrid 2 virtual-ip fe80::1 link-local

Sysname-Vlan-interface2 trill vr ipv6 vrid 2 virtual-ip 1::1

**TRILL \-- TRILL配置命令 \-- trill vr vrid**

------------------------------------------------------------------------

**[trill** **vr** ]**vrid**命令用来创建IPv4 TRILL VR并为其配置虚拟IPv4地址。

**[undo** **trill** **vr** **vrid**]命令用来删除指定的IPv4 TRILL VR，或为其删除一个虚拟IPv4地址。

【命令】

**[trill** **vr** **vrid** *vr-id* **virtual-ip** *virtual-address*]

**[undo** **trill** **vr** **vrid** *vr-id* **virtual-ip** [ *virtual-address* ]]

【缺省情况】

不存在任何IPv4 TRILL VR。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vr-id*]：表示VR的编号，取值范围为1～255。

*[virtual-address*]：表示VR的虚拟IPv4地址，必须为合法的IPv4地址（A、B、C类地址，不包括全零、广播和环回地址）。如果未指定本参数，表示删除该VR中的所有虚拟IPv4地址。

【使用指导】

需要注意的是：

·使用**trill** **vr** **vrid**命令时，如果指定编号的IPv4 TRILL VR不存在，则创建一个新的IPv4 TRILL VR；如果指定编号的IPv4 TRILL VR已存在，则为其添加一个虚拟IPv4地址。

·一个VLAN接口上最多可配置4个IPv4 TRILL VR，且所有IPv4 TRILL VR的虚拟IPv4地址总数不得超过16个。

【举例】

\# 在接口Vlan-interface2上先创建IPv4 TRILLVR 1并为其配置虚拟IPv4地址10.1.1.1，然后再为其添加一个虚拟IPv4地址10.1.1.2。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 trill vr vrid 1 virtual-ip 10.1.1.1

Sysname-Vlan-interface2 trill vr vrid 1 virtual-ip 10.1.1.2

**TRILL \-- TRILL配置命令 \-- trill vr vrid track**

------------------------------------------------------------------------

**[trill** **vr** **vrid** **track**]命令用来配置TRILL VR监测的Track项。

**[undo** **trill** **vr** **vrid** **track**]命令用来取消TRILL VR监测的Track项。

【命令】

**[trill** **vr** [ **ipv6**  **vrid**] *vr-id* **track** *track-entry-number*]

**[undo** **trill** **vr** [ **ipv6**  **vrid**] *vr-id* **track** [ *track-entry-number* ]]

【缺省情况】

TRILL VR未监测任何Track项。

【视图】

VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：表示IPv6 TRILL VR。如果未指定本参数，表示IPv4 TRILL VR。

*[vr-id*]：表示VR的编号，取值范围为1～255。

*[track-entry-number*]：表示Track项的编号，取值范围为1～1024。如果未指定本参数，表示取消监测所有Track项。

【使用指导】

需要注意的是，如果当前接口下不存在指定的TRILL VR，或一个VR监测了超过8个Track项，均将导致配置失败。

【举例】

\# 在接口Vlan-interface2上配置IPv4 TRILL VR 1监测Track项8。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 trill vr vrid 1 track 8

\# 在接口Vlan-interface2上配置IPv6 TRILL VR 2监测Track项9。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 trill vr ipv6 vrid 2 track 9
