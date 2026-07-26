
**OSPFv3 \-- OSPFv3配置命令 \-- abr-summary (OSPFv3 area view)**

------------------------------------------------------------------------

**[abr-summary**]命令用来配置ABR路由聚合。

**[undo** **abr-summary**]命令用来取消该配置。

【命令】

**[abr-summary** *ipv6-address prefix-length* [ **not-advertise**   **cost** value ]]

**[undo abr-summary** *ipv6-address prefix-length*]

【缺省情况】

ABR不对路由进行聚合。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：聚合路由的目的IPv6地址。

*[prefix-length*]：聚合路由的目的IPv6地址前缀长度，取值范围为0～128。它指定地址中有多少连续的位组成IPv6网络前缀，即IPv6地址中的网络地址部分。

**[not-advertise**]：不通告聚合的IPv6路由。如果未指定本参数，则通告聚合的IPv6路由。

**[cost** *value*]：聚合路由的开销，取值范围为1～16777215，缺省值为所有被聚合的路由中最大的开销值。

【使用指导】

本命令只适用于ABR，用来对当前区域进行路由聚合。对于落入该聚合网段的路由，ABR向其它区域只发送一条聚合后的路由。一个区域可配置多条聚合网段，这样OSPFv3可对多个网段进行聚合。

当配置了**undo abr-summary**命令后，原来被聚合的路由将重新被发布。

【举例】

\# 将OSPFv3区域1中两条路由2000:1:1:1::/64、2000:1:1:2::/64的路由聚合成一条前缀2000:1:1::/48向其它区域发送。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 area 1

Sysname-ospfv3-1-area-0.0.0.1 abr-summary 2000:1:1:: 48

**OSPFv3 \-- OSPFv3配置命令 \-- area**

------------------------------------------------------------------------

**[area**]命令用来创建OSPFv3区域，并进入区域视图。

**[undo** **area**]命令用来删除指定的OSPFv3区域。

【命令】

**[area** *area-id*]

**[undo area ***area-id*]

【缺省情况】

没有创建OSPFv3区域。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[area-id*]：区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

【举例】

\# 进入OSPFv3区域0视图。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 area 0

Sysname-ospfv3-1-area-0.0.0.0

**OSPFv3 \-- OSPFv3配置命令 \-- asbr-summary (OSPFv3 view)**

------------------------------------------------------------------------

**[asbr-summary**]命令用来配置ASBR路由聚合。

**[undo** **asbr-summary**]命令用来取消该配置。

【命令】

**[asbr-summary**[ *ipv6-address prefix-length* [ **cost** *cost* \| **not-advertise \|** **nssa-only** \| **tag** *tag* ] \*]]

**[undo asbr-summary** *ipv6-address prefix-length*]

【缺省情况】

ASBR不对路由进行聚合。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：聚合路由的目的IPv6地址。

*[prefix-length*]：聚合路由的目的IPv6地址前缀长度，取值范围为0～128。它指定地址中有多少连续的位组成IPv6网络前缀，即IPv6地址中的网络地址部分。

**[cost** *cost*]：聚合路由的开销，取值范围为1～16777214。如果未指定本参数，*cost*取所有被聚合的路由中最大的开销值作为聚合路由的开销；如果是Type-7 LSA转化成的Type-5 LSA描述的路由匹配聚合、且是Type2外部路由，则*cost*取所有被聚合的路由中最大的开销值加1作为聚合路由的开销。

**[not-advertise**]：不通告聚合路由。如果未指定本参数，将通告聚合路由。

**[nssa-only**]**：**设置Type-7 LSA的P比特位为不置位，即在对端路由器上不能转为Type-5 LSA。缺省时，Type-7 LSA的P比特位被置位，即在对端路由器上可以转为Type-5 LSA（如果本地路由器是ABR，则会检查骨干区域是否存在FULL状态的邻居，当FULL状态的邻居存在时，产生的Type-7 LSA中P比特位不置位）。

**[tag*** tag*]：聚合路由的标记，取值范围为0～4294967295。

【使用指导】

如果本地路由器是ASBR，对引入的聚合地址范围内的Type-5 LSA描述的路由进行聚合；当配置了NSSA区域时，对引入的聚合地址范围内的Type-7 LSA描述的路由进行聚合。

如果本地路由器同时是ASBR和ABR，并且是NSSA区域的转换路由器，则对由Type-7 LSA转化成的Type-5 LSA描述的路由进行聚合处理；如果不是NSSA区域的转换路由器，则不进行聚合处理。

配置**asbr-summary**命令后，对处于聚合地址范围内的外部路由，本地路由器只向邻居路由器发布一条聚合后的路由；配置**undo asbr-summary**命令后，原来被聚合的外部路由将重新被发布。

【举例】

\# 配置OSPFv3进程1对引入的路由进行聚合，聚合路由为2000::/16，开销值为100，标记为2。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 asbr-summary 2000:: 16 cost 100 tag 2

**OSPFv3 \-- OSPFv3配置命令 \-- bandwidth-reference (OSPFv3 view)**

------------------------------------------------------------------------

**[bandwidth-reference**]命令用来配置计算链路开销时所依据的带宽参考值。

**[undo bandwidth-reference**]命令用来恢复缺省情况。

【命令】

**[bandwidth-reference** *value*]

**[undo bandwidth-reference**]

【缺省情况】

计算链路开销时所依据的带宽参考值为100Mbps。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：计算链路开销时所依据的带宽参考值，取值范围为1～4294967，单位为Mbps。

【使用指导】

OSPFv3有两种方式来配置接口的开销值，第一种方法是在接口视图下直接配置开销值；第二种方法是配置接口的带宽参考值，OSPFv3根据带宽参考值自动计算接口的开销值，计算公式为：接口开销＝带宽参考值÷接口带宽，当计算出来的开销值大于65535，开销取最大值65535；当计算出来的开销值小于1时，开销取最小值1。

如果没有在接口视图下显式的配置此接口的开销值，OSPFv3会根据该接口的带宽自动计算其开销值[.]

【举例】

\# 配置计算链路开销时所依据的带宽参考值为1000Mbps。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 bandwidth-reference 1000

**OSPFv3 \-- OSPFv3配置命令 \-- default tag**

------------------------------------------------------------------------

**[default tag**]命令用来配置引入外部路由的全局标记。

**[undo default tag**]命令用来恢复缺省情况。

【命令】

**[default tag ***tag*]

**[undo default tag**]

【缺省情况】

引入外部路由的全局标记为1。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag*]：外部路由的全局标记，取值范围为0～4294967295。

【使用指导】

如果在配置相关命令时没有指定标记，则缺省使用本命令配置的全局标记。

【举例】

\# 配置OSPFv3引入外部路由的标记为2。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 default tag 2

【相关命令】

·**default-route-advertise** (OSPFv3 view)

l**import-route**

l**route-tag**（MPLS命令参考/MPLS L3VPN）

**OSPFv3 \-- OSPFv3配置命令 \-- default-cost (OSPFv3 area view)**

------------------------------------------------------------------------

**[default-cost**]命令用来配置发送到Stub区域或NSSA区域的缺省路由的开销。

**[undo default-cost**]命令用来恢复缺省情况。

【命令】

**[default-cost ***cost*]

**[undo default-cost**]

【缺省情况】

发送到Stub区域或NSSA区域的缺省路由的开销为1。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cost*]：发送到Stub区域或NSSA区域的缺省路由的开销，取值范围为0～16777214。

【使用指导】

该命令只有在Stub区域的ABR或NSSA区域的ABR/ASBR上配置才能生效。

【举例】

\# 将OSPFv3区域1设置为Stub区域，使发送到该Stub区域的缺省路由开销为60。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 area 1

Sysname-ospfv3-1-area-0.0.0.1 stub

Sysname-ospfv3-1-area-0.0.0.1 default-cost 60

【相关命令】

l**nssa **(OSPFv3 area view)

l**stub******(OSPFv3 area view)

**OSPFv3 \-- OSPFv3配置命令 \-- default-route-advertise (OSPFv3 view)**

------------------------------------------------------------------------

**[default-route-advertise**]命令用来将缺省路由引入到OSPFv3路由区域。

**[undo default-route-advertise**]命令用来恢复缺省情况。

【命令】

**[default-route-advertise **[[ [ **always** \| **permit-calculate-other** ] \| **cost** *cost* \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* ] \*]]

**[undo default-route-advertise**]

【缺省情况】

没有引入缺省路由。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[always**]：如果当前路由器的路由表中没有缺省路由，使用此参数可产生一个描述缺省路由的AS-external-LSA发布出去。如果没有指定该关键字，仅当本地路由器的路由表中存在缺省路由时，才可以产生一个描述缺省路由的AS-external-LSA发布出去。

**[permit-calculate-other**]：当路由器产生并发布了一个描述缺省路由的AS-external-LSA时，指定此参数的路由器仍然会计算来自于其他路由器的缺省路由，未指定此参数的路由器不再计算来自其他路由器的缺省路由。当路由器没有产生一个描述缺省路由的AS-external-LSA时，无论是否指定此参数，路由器都会计算来自其他路由器的缺省路由。

**[cost** *cost*]：该缺省路由的度量值，取值范围为0～16777214，缺省值为1。

**[route-policy** *route-policy-name*]：路由策略名，为1～63个字符的字符串，区分大小写。只有当前路由器的路由表中存在缺省路由，并且有路由匹配*route-policy-name*指定的路由策略，才可以产生一个描述缺省路由的AS-external-LSA发布出去，指定的路由策略会影响AS-external-LSA中的值。如果同时指定**always**参数，不论当前路由器的路由表中是否有缺省路由，只要有路由匹配指定的路由策略，就将产生一个描述缺省路由的AS-external-LSA发布出去，指定的路由策略会影响AS-external-LSA中的值。

**[tag** *tag*]：外部路由的标记，取值范围为0～4294967295。如果未指定本参数，将根据**default tag**命令的配置进行取值。

**[type** *type*]：该AS-external-LSA的类型，取值范围为1～2，缺省值为2。

【使用指导】

使用**import-route**命令不能引入缺省路由，如果要引入缺省路由，必须使用本命令。当本地路由器的路由表中没有缺省路由时，要产生一个描述缺省路由的AS-external-LSA应使用**always**关键字。

【举例】

\# 将产生的缺省路由引入到OSPFv3自治系统中（本地路由器没有缺省路由）。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 default-route-advertise always

【相关命令】

l**import-route******(OSPFv3 area view)

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3**

------------------------------------------------------------------------

**[display ospfv3**]命令用来显示OSPFv3的进程信息。

【命令】

**[display ospfv3** [ *process-id*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的概要信息。

**[verbose**]：显示OSPFv3进程的详细信息。如果未指定本参数，将显示OSPFv3进程的概要信息。

【举例】

\# 显示所有OSPFv3进程的详细信息。

\<Sysname\> display ospfv3 verbose

               OSPFv3 Process 1 with Router ID 1.1.1.1

 RouterID: 1.1.1.1          Router type:  ABR  ASBR  NSSA

 Route tag: 0

 Route tag check: Disabled

 Multi-VPN-Instance: Disabled

 Type value of extended community attributes:

    Domain ID : 0x0005

    Route type: 0x0306

    Router ID : 0x0107

 Domain-id: 0.0.0.0

 DN-bit check: Enabled

 DN-bit set: Enabled

 Originating router-LSAs with maximum metric

    Condition: On startup while BGP is converging for 600 seconds, State: Inactive

    Advertise summary-LSAs with metric 16711680

    Advertise external-LSAs with metric 16711680

    Advertise intra-area-prefix-LSAs with maximum metric

 SPF-schedule-interval: 5 50 200

 LSA generation interval: 5

 LSA arrival interval: 1000

 Transmit pacing: Interval: 20 Count: 3

 Default ASE parameters: Tag: 1

 Route preference: 10

 ASE route preference: 150

 SPF calculation count: 0

 External LSA count: 0

 LSA originated count: 0

 LSA received count: 0

 Area count: 2  Stub area Count: 0  NSSA area Count: 1

 ExChange/Loading neighbors: 0

 Max equal cost paths: 32

 Up interfaces: 1

 Full neighbors: 1

 Normal areas with up interfaces: 1

 Calculation trigger type: Full

 Current calculation type: SPF calculation

 Current calculation phase: Calculation area topology

 Redistribute timer: Off

 Redistribute schedule type: RIB

 Redistribute route count: 0

 Process reset state: N/A

 Current reset type: N/A

 Next reset type: N/A

 Reset prepare message replied: -/-/-/-

 Reset process message replied: -/-/-/-

 Reset phase of module:

   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A

 Area: 0.0.0.0

 Area flag: Normal

 SPF scheduled count: 0

 ExChange/Loading neighbors: 0

 LSA count: 0

 IPsec profile name: Profile000

 Up interfaces: 0

 MTU: 1440

 Default cost: 1

 Created by Vlink

 Process reset state: N/A

 Current reset type: N/A

 Reset prepare message replied: -/-/-/-

 Reset process message replied: -/-/-/-

 Reset phase of module:

   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A

 Area: 0.0.0.2

 Area flag: Normal

 SPF scheduled count: 0

 ExChange/Loading neighbors: 0

 LSA count: 0

 Up interfaces: 1

 MTU: 1500

 Default cost: 1

 Process reset state: N/A

 Current reset type: N/A

 Reset prepare message replied: -/-/-/-

 Reset process message replied: -/-/-/-

 Reset phase of module:

   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A

 Area: 0.0.0.3

 Area flag: NSSA

 7/5 translator state: Disabled

 7/5 translate stability timer interval: 0

 SPF Scheduled Count: 0

 ExChange/Loading neighbors: 0

 LSA Count: 0

 Up interfaces: 0

 MTU: 1440

 Default cost: 1

 Process reset flag: N/A

 Current reset type: N/A

 Reset prepare message replied: -/-/-/-

 Reset process message replied: -/-/-/-

 Reset phase of module:

   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A

表1-1 display ospfv3 verbose命令显示信息描述表

字段

描述

OSPFv3 Process 1 with Router ID 1.1.1.1

OSPFv3进程是1，Router ID是1.1.1.1

RouterID

本路由器的Router ID

Router type

路由器类型，取值为：

·ABR表示区域边界路由器

·ASBR表示自治系统边界路由器

·NSSA表示支持NSSA区域

为空表示非上面三种情况

Route tag

当前进程引入外部路由的缺省标记

Route tag check

当前进程是否使能检查OSPFv3 LSA的标记

Multi-VPN-Instance

当前进程对PE、多VPN实例的支持情况：

·Multi-VPN-Instance：Disabled表示不支持多VPN实例

·Multi-VPN-instance：Enabled表示支持多VPN实例

·PE Router, Multi-VPN-Instance：Enabled表示为PE

Type value of extended community attributes

OSPFv3扩展团体属性的类型编码

Domain-id

OSPFv3域标识符

DN-bit check

当前进程是否使能检查OSPFv3 LSA的DN位

DN-bit set

当前进程是否使能设置OSPFv3 LSA的DN位

Originating router-LSAs with maximum metric/Originating router-LSAs with R-bit clear

Router LSA中使用最大开销值发布/Router LSA中清除R-bit

Condition

Stub路由器的状态：

·Always代表始终生效

·On startup while BGP is converging for XXX seconds代表BGP收敛超时时间

·On startup for XXX seconds代表重启后生效时间

State

Stub路由器是否生效：

·Active表示生效

·Inactive表示不生效

Advertise summary-LSAs with metric

Summary LSA发布使用的开销值

Advertise external-LSAs with metric

外部LSA发布使用的开销值

Advertise intra-area-prefix-LSAs with maximum metric

Intra-area-prefix-LSA发布使用的开销值

SPF-schedule-interval

进行SPF计算的时间间隔

LSA generation interval

LSA生成时间间隔

LSA arrival interval

LSA重复到达的最小时间间隔

Transmit pacing

接口发送LSU报文的速率，其中：

·Interval表示接口发送LSU报文的时间间隔

·Count表示接口一次发送LSU报文的最大个数

Default ASE parameters

引入外部路由的缺省参数值，其中Tag代表路由标记

Route preference

内部路由优先级

ASE route preference

外部路由优先级

SPF calculation count

OSPFv3进程的路由计算总数

External LSA count

外部LSA数目，其中：

·Count：LSA数目

·checksum Sum：校验和

LSA originated count

产生的LSA数目

LSA received count

接收的LSA数目

Area count

区域总数目

Stub area Count

Stub区域数目

NSSA area Count

NSSA区域数目

ExChange/Loading neighbors

处于ExChange/Loading状态的邻居数

Calculation trigger type

触发路由计算的类型，具体如下：

·Full：触发全部路由计算

·Area topology change：区域拓扑改变触发路由计算

·Intra router change：增量的区域内路由器路由变化

·ASBR change：增量的ASBR路由变化

·Full IP prefix：触发全部IP前缀计算

·Full intra AS：触发全部AS内部前缀计算

·Inc intra AS：触发增量AS内部前缀计算

·Full inter AS：触发全部AS外部前缀计算

·Inc inter AS：触发增量AS外部前缀计算

·Nexthop calculation：触发下一跳计算

·N/A：未触发计算

Current calculation type

当前路由计算的类型，具体如下：

·SPF calculation：进行区域SPF计算

·Intra router calculation：区域内路由器路由计算

·ASBR calculation：区域间ASBR路由计算

·Inc intra router：增量区域内路由器路由计算

·Inc ASBR calculation：增量区域间ASBR路由计算

·Full intra AS：进行全部AS内部前缀计算

·Inc intra AS：进行增量AS内部前缀计算

·Full inter AS：进行全部AS外部前缀计算

·Inc inter AS：进行增量AS外部前缀计算

·N/A：未触发计算

Current calculation phase

当前路由计算调度运行到的阶段，具体如下：

·Calculation area topology：计算区域拓扑

·Calculation router：计算路由器路由

·Calculation intra AS：计算AS内部路由

·Calculation ASBR：计算ASBR路由

·Calculation inter AS：计算AS外部路由

·Calculation end：计算收尾阶段

·N/A：未触发计算

Redistribute timer

引入路由定时器，其中：

·Off： 关闭

·On：开启

Redistribute schedule type

引入路由调度类型，其中：

·RIB： 触发遍历RIB表进行引入

·Self： 触发遍历自身引入表进行引入

·N/A：未触发引入

Redistribute route count

引入路由计数

Process reset state

进程重启状态标志，具体如下：

·N/A：进程未重启

·Under reset：进程正在重启

·Under RIB smooth：进程正在同步RIB路由

Current reset type

当前进程重启类型，具体如下：

·N/A：进程未重启

·GR quit：GR异常退出进行普通重启

·Delete：删除OSPFv3进程

·Undo router-id：删除Router-id

·Set router-id：设置Router-id

Next reset type

即将调度进程重启类型，具体如下：

·N/A：进程未重启

·GR quit：GR异常退出进行普通重启

·Delete：删除OSPFv3进程

·Undo router-id：删除Router-id

·Set router-id：设置Router-id

Reset prepare message replied

响应准备重启消息的模块，具体如下：

·P代表邻居维护模块

·S代表LSDB同步模块

·C代表路由计算模块

·R代表路由引入模块

Reset process message replied

响应进程重启消息的模块，具体如下：

·P代表邻居维护模块

·S代表LSDB同步模块

·C代表路由计算模块

·R代表路由引入模块

Reset phase of module

各模块所处重启阶段。其中M代表主控制模块，P代表邻居维护模块，S代表LSDB同步模块，其阶段有：

·N/A：未重启

·Delete ASE：删除所有ASE LSA

·Delete area LSA：删除区域相关LSA

·Delete area IF：删除区域下接口

C代表路由计算模块，其阶段有：

·N/A：未重启

·Delete topology：删除区域拓扑

·Delete router：删除路由器路由

·Delete intra AS：删除AS内部路由

·Delete inter AS：删除AS外部路由

·Delete ASBR：删除ASBR路由

R代表路由引入模块，其阶段有：

·N/A：未重启

·Delete import：删除引入路由

Area

区域信息

Area flag

区域类型

SPF scheduled count

OSPF区域的路由计算总数

LSA count

LSA数目，其中：

·Count：LSA数目

·checksum Sum：校验和

IPsec profile name

IPsec安全框架名

MTU

区域的MTU值

Default cost

路由的缺省开销值

Created by Vlink

区域由Vlink创建

7/5 translator state

Type-7 LSA转换为Type-5 LSA的转换者状态，取值为：

·Enabled：表示本设备是通过命令指定的Type-7 LSA转换为Type-5 LSA的转换者

·Elected：表示本设备是通过选举指定的Type-7 LSA转换为Type-5 LSA的转换者

·Disabled：表示本设备不是Type-7 LSA转换为Type-5 LSA的转换者

7/5 translate stability timer interval

Type-7 LSA转换为Type-5 LSA转换稳定定时器的超时时间间隔，单位为秒

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 abr-asbr**

------------------------------------------------------------------------

**[display ospfv3 abr-asbr**]命令用来显示到OSPFv3的区域边界路由器和自治系统边界路由器的路由信息。

【命令】

**[display ospfv3** [ *process-id*  **abr-asbr**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程下到区域边界路由器和自治系统边界路由器的路由信息。

【举例】

\# 显示所有OSPFv3进程的ABR和ASBR路由。

\<Sysname\> display ospfv3 abr-asbr

               OSPFv3 Process 1 with Router ID 1.1.1.1

Destination :1.1.1.2                                   Rtr Type : ABR

 Area        :0.0.0.0                                   Path Type: Intra

 NextHop     :FE80:1:1::1                               Cost     : 1

 Destination :1.1.1.3                                   Rtr Type : ASBR

 Area        :0.0.0.0                                   Path Type: Intra

 NextHop     :FE80:2:1::1                               Cost     : 1

表1-2 display ospfv3 abr-asbr命令显示信息描述表

字段

描述

OSPFv3 Process 1 with Router ID 1.1.1.1

OSPFv3进程是1，Router ID是1.1.1.1

Destination

ABR或ASBR的路由器ID

Rtr Type

路由器类型，包括ABR和ASBR

Area

下一跳地址所在的区域ID

Path Type

到ABR或ASBR的路由类型，取值为：

·Intra表示区域内路由

·Inter表示区域间路由

NextHop

下一跳地址

Cost

从本路由器到达ABR或ASBR的开销

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 abr-summary**

------------------------------------------------------------------------

**[display** **ospfv3** **abr-summary**]命令用来显示OSPFv3的ABR聚合信息。

【命令】

**[display** **ospfv3** [ *process-id*   **area** *area-id*  **abr-summary**  *ipv6-address* *prefix-length*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：当前的聚合配置所在进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的ABR聚合信息。

**[area** *area-id*]：显示位于指定区域的ABR聚合信息。如果未指定本参数，将显示所有区域的ABR聚合信息。*area-id*为区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

*[ipv6-address* *prefix-length*]：显示指定IPv6地址的ABR聚合信息。*ipv6-address*表示IPv6地址前缀；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。如果未指定本参数，将显示所有ABR聚合信息。

**[verbose**]：显示ABR聚合详细信息。如果未指定本参数，将显示ABR聚合的概要信息。

【举例】

\# 显示OSPFv3进程1的ABR聚合信息。

\<Sysname\> display ospfv3 1 abr-summary

             OSPFv3 Process 1 with Router ID 2.2.2.2

                     Area: 1.1.1.1

 Total summary addresses: 1

 Prefix      : 1000:4::/32

 Status      : Advertise

 NULL0       : Active

 Cost        : 1 (Configured)

 Routes count: 2

表1-1 display ospfv3 abr-summary命令显示信息描述表

字段

描述

Total summary addresses

聚合路由的路由数

Area

聚合路由所在的区域

Prefix

聚合路由的地址前缀

Status

聚合路由的状态：

·Advertise：已发布

·Not-advertise：未发布

NULL0

NULL0路由：

·Active：激活

·Inactive：未激活

Cost

聚合路由的开销

·Configured：配置的聚合开销

·Not Configured：未配置聚合开销

Routes count

被聚合的路由数

\# 显示OSPFv3进程1的ABR聚合详细信息。

\<Sysname\> display ospfv3 1 abr-summary verbose

             OSPFv3 Process 1 with Router ID 2.2.2.2

                        Area: 1.1.1.1

Total summary addresses: 1

 Prefix      : 1000:4::/32

 Status      : Advertise

 NULL0       : Active

 Cost        : 1 (Configured)

 Routes count: 2

   Destination                                        Metric

   1000:4:10:3::/96                                   1

   1000:4:11:3::/96                                   1

表1-2 display ospfv3 abr-summary verbose命令显示信息描述表

字段

描述

Destination

被聚合路由的目的地址

Metric

路由的开销值

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 asbr-summary**

------------------------------------------------------------------------

**[display** **ospfv3** **asbr-summary**]命令用来显示OSPFv3的ASBR聚合信息。

【命令】

**[display** **ospfv3** [ *process-id*  **asbr-summary**  *ipv6-address* *prefix-length*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：当前的聚合配置所在进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的ASBR聚合信息。

*[ipv6-address* *prefix-length*]：显示指定IPv6地址的ASBR聚合信息。*ipv6-address*表示IPv6地址前缀；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。如果未指定本参数，将显示所有ASBR聚合信息。

**[verbose**]：显示ASBR聚合详细信息。如果未指定本参数，将显示ASBR聚合的概要信息。

【举例】

\# 显示OSPFv3进程1的ASBR聚合信息。

\<Sysname\> display ospfv3 1 asbr-summary

               OSPFv3 Process 1 with Router ID 2.2.2.2

 Total summary addresses: 1

 Prefix      : 1000:4::/32

 Status      : Advertise

 NULL0       : Active

 Cost        : 1 (Configured)

 Tag         : (Not configured)

 Nssa-only   : (Not configured)

 Routes count: 2

表1-3 display ospfv3 asbr-summary命令显示信息描述表

字段

描述

Total summary addresses

聚合路由的路由数

Prefix

聚合路由的地址前缀和前缀长度

Status

聚合路由的状态：

·Advertise：已发布

·Not-advertise：未发布

NULL0

NULL0路由：

·Active：激活

·Inactive：未激活

Cost

聚合路由的开销：

·Configured：配置的聚合开销

·Not configured：未配置聚合开销

Tag

聚合路由的标记：

·Configured：配置的聚合标记

·Not configured：未配置聚合标记

Nssa-only

是否配置Nssa-only：

·Configured：配置了Nssa-only

·Not configured：未配置Nssa-only

Routes count

被聚合的路由数

\# 显示OSPFv3进程1的ASBR聚合详细信息。

\<Sysname\> display ospfv3 1 asbr-summary verbose

               OSPFv3 Process 1 with Router ID 2.2.2.2

 Total summary addresses: 1

 Prefix      : 1000:4::/32

 Status      : Advertise

 NULL0       : Active

 Cost        : 1 (Configured)

 Tag         : (Not configured)

 Nssa-only   : (Not configured)

 Routes count: 2

  Destination                                 Protocol Process Type Metric

  1000:4:10:3::/96                            Static   0       2    1

  1000:4:11:3::/96                            Static   0       2    1

表1-4 display ospfv3 asbr-summary verbose命令显示信息描述表

字段

描述

Destination

被聚合路由的前缀和前缀长度

Protocol

被聚合路由的协议类型

Process

被聚合路由的协议进程ID

Type

被聚合路由的类型

Metric

被聚合路由的开销

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 graceful-restart**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ospfv3 graceful-restart**]命令用来显示OSPFv3进程的GR状态信息。

【命令】

**[display ospfv3** [ *process-id*  **graceful-restart**  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的GR状态信息。

**[verbose**]：显示GR详细状态信息。如果未指定本参数，将显示OSPFv3进程的GR状态概要信息。

【举例】

\# 显示所有OSPFv3进程的GR状态信息（Restarter）。

\<Sysname\> display ospfv3 graceful-restart

               OSPFv3 Process 1 with Router ID 3.3.3.3

 Graceful-restart capability     : Enable

 Graceful-restart support        : Planned and un-planned, Partial

 Helper capability               : Enable

 Helper support                  : Planned and un-planned

 Current GR state                : Normal

 Graceful-restart period         : 120 seconds

 Number of neighbors under helper: 0

 Number of restarting neighbors  : 0

 Last exit reason:

   Restarter: None

   Helper   : None

表1-5 display ospfv3 graceful-restart命令显示信息描述表

字段

描述

OSPFv3 Process 1 with Router ID 3.3.3.3

OSPFv3进程是1，Router ID是3.3.3.3的GR状态信息

Graceful-restart capability

是否使能OSPFv3协议的GR能力

·Enable：使能

·Disable：未使能

Graceful-restart support

进程GR支持模式（GR使能时才显示）：

·Planned and un-planned：支持计划和非计划GR

·Planned only：只支持计划性GR

·Partial：支持接口级GR

·Global：不支持接口级GR，支持全局GR

Helper capability

是否使能OSPFv3协议的GR Helper能力

·Enable：使能

·Disable：未使能

Helper support

显示Helper的支持模式（Helper使能时才显示）：

·Strict LSA check：Helper端支持严格的LSA检查

·Planned and un-planned：支持作为计划和非计划GR的Helper

·Planned only：只支持作为计划GR的Helper

Current GR state

当前GR的状态，其状态有如下几种：

·Normal：表示正处在非GR的正常状态

·Under GR：表示正在GR过程中，自身作为Restarter

·Under Helper：表示正在GR过程中，自身作为Helper

Graceful-restart period

GR重启间隔时间

Number of neighbors under helper

处于GR Helper模式的邻居个数

Number of restarting neighbors

处于GR Restarter模式的邻居个数

Last exit reason

上次退出原因，其中：

·Restarter：表示退出Restarter的原因

¡None：无

¡Completed：GR完成

¡Intervaltimerisfired：GR定时器超时

¡Interfacestatechange：接口状态变化

¡Received1-wayhello：收到邻居的1-way Hello报文

¡Resetneighbor：邻居发生Reset操作

¡DRorBDRchange：DR或BDR发生变化

·Helper：表示退出Helper的原因

¡None：无

¡Completed：GR完成

¡Received1-wayhello：收到邻居的1-way Hello报文

¡GracePeriodtimerisfired：GR定时器超时

¡Lsacheckfailed：LSA检查未通过

¡Resetneighbor：邻居发生Reset操作

¡ReceivedMAXAGEgracelsabutneighborisnotfull：收到到达老化时间的Grace LSA，但邻居状态未达到FULL状态

\# 显示OSPFv3进程的GR详细状态信息（Restarter）。

\<Sysname\> display ospfv3 graceful-restart verbose

               OSPFv3 Process 1 with Router ID 3.3.3.3

 Graceful-restart capability     : Enable

 Graceful-restart support        : Planned and un-planned, Partial

 Helper capability               : Enable

 Helper support                  : Planned and un-planned

 Current GR state                : Normal

 Graceful-restart period         : 120 seconds

 Number of neighbors under helper: 0

 Number of restarting neighbors  : 0

 Last exit reason:

   Restarter: None

   Helper   : None

 Area: 0.0.0.0

 Area flag: Normal

 Area up interface count: 1

 Virtual-link Neighbor-ID: 100.1.1.1, Neighbor-state: Full

 Restarter state: Normal   State: P-2-P    Type: Virtual

 Interface: 6696 (Vlan-interface200), Instance-ID: 0

 Local  IPv6 address: 200:1:FFFF::1

 Remote IPv6 address: 201:FFFF::2

 Transit area: 0.0.0.1

 Last exit reason:

   Restarter: None

   Helper   : None

 Neighbor       GR state       Last helper exit reason

 100.1.1.1      Normal         None

 Area: 0.0.0.1

 Area flag: Transit

 Area up interface count: 3

 Interface: 5506 (Vlan-interface3), Instance-ID: 0

 Restarter state: Normal   State: DR       Type: Broadcast

 Last exit reason:

   Restarter: None

   Helper   : None

 Neighbor count of this interface: 0

 Number of neighbors under helper: 0

 Interface: 6696 (Vlan-interface200), Instance-ID: 0

 Restarter state: Normal   State: DR       Type: Broadcast

 Last exit reason:

   Restarter: None

   Helper   : None

 Neighbor count of this interface: 1

 Number of neighbors under helper: 0

 Neighbor       GR state       Last helper exit reason

 100.1.1.1      Normal         None

 Sham-link Neighbor-ID: 100.1.1.1, Neighbor-state: Full

 Restarter state: Normal   State: P-2-P    Type: Sham

 Interface-ID: 2147483649, Instance-ID: 0

 Source      : 8000:88::FFFF

 Destination : 7000:77::FFFF

 Last exit reason:

   Restarter: None

   Helper   : None

 Neighbor       GR state       Last helper exit reason

 100.1.1.1      Normal         None

 Area: 0.0.0.5

 Area flag: NSSANoSummaryNoImportRoute

 7/5 translator state: Disabled

 7/5 translate stability timer interval: 0

 Area up interface count: 0

表1-6 display ospfv3 graceful-restart命令显示信息描述表

字段

描述

Area

区域信息

Area flag

区域类型：

·Normal：普通区域

·Transit：传输区

·Stub：Stub区域

·StubNoSummary：完全Stub区域

·NSSA：NSSA区域

·NSSANoSummary：完全NSSA区域

·NSSANoSummaryNoImportRoute：完全NSSA区域，配置了no-import-route参数

7/5 translator state

Type-7 LSA转换为Type-5 LSA的转换者状态，取值为：

·Enabled：表示通过命令指定Type-7 LSA转换为Type-5 LSA的转换者

·Elected：表示通过选举指定Type-7 LSA转换为Type-5 LSA的转换者

·Disabled：表示不是Type-7 LSA转换为Type-5 LSA的转换者

7/5 translate stability timer interval

Type-7 LSA转换为Type-5 LSA转换稳定定时器的超时时间，单位为秒

Area up interface count

区域下up的接口计数

Interface

区域内的普通接口，以及虚连接所属的出接口

Instance-ID

接口实例ID

Restarter state

作为Restarter的状态

State

接口状态

Type

接口的网络类型

Neighbor count of this interface

接口下的邻居个数

Neighbor

邻居Router ID

GR state

邻居的GR状态：

·Normal：普通状态

·Under GR：进程正在GR

·Under Helper：进程正在作为GR Helper

Last helper exit reason

上一次作为该邻居Helper退出的原因

Virtual-link Neighbor-ID

虚连接的邻居Router ID

Neighbor-State

虚连接和邻居的状态，包括Down、Init、2-Way、ExStart、Exchange、Loading和Full

Local  IPv6 address

本地IPv6地址

Remote IPv6 address

对端IPv6地址

Transit area

传输区域ID

Sham-link Neighbor-ID

Shamlink的邻居Router ID

Source

Shamlink源地址

Destination

Shamlink目的地址

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 interface**

------------------------------------------------------------------------

**[display ospfv3 interface**]命令用来显示OSPFv3的接口信息。

【命令】

**[display ospfv3 **[ *process-id*  **interface** [ *interface-type interface-number* \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和接口编号。显示指定接口的详细信息。

**[verbose**]：显示所有接口的详细信息。

【使用指导】

·如果未指定OSPFv3进程号，将显示所有OSPFv3进程的接口概要信息。

·如果未指定接口或参数**verbose**，将显示所有接口的概要信息。

【举例】

·路由应用

\# 显示运行OSPFv3的接口GigabitEthernet1/0/1的信息。

\<Sysname\> display ospfv3 interface gigabitethernet 1/0/1

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Area: 0.0.0.0

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 GigabitEthernet1/0/1 is up, line protocol is up

  Interface ID 3        Instance ID 0

  IPv6 prefixes

    fe80::200:12ff:fe34:1  (Link-Local address)

    2001::1

  Cost: 1       State: BDR       Type: Broadcast    MTU: 1500

  Priority: 1

  Designated router: 2.2.2.2

  Backup designated router: 1.1.1.1

  Timers: Hello 10, Dead 40, Poll 40, Retransmit 5, Transmit delay 1

  Neighbor count is 1, Adjacent neighbor count is 1

  IPsec profile name: profile001

  Exchanging/Loading neighbors: 0

  Wait timer: Off,  LsAck timer: Off

  Prefix-suppression is enabled

·交换应用

\# 显示运行OSPFv3的接口Vlan-interface1的信息。

\<Sysname\> display ospfv3 interface vlan-interface 1

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Area: 0.0.0.0

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Vlan-interface1 is up, line protocol is up

  Interface ID 65697        Instance ID 0

  IPv6 prefixes

    fe80::200:12ff:fe34:1  (Link-Local address)

    2001::1

  Cost: 1       State: BDR       Type: Broadcast    MTU: 1500

  Priority: 1

  Designated router: 2.2.2.2

  Backup designated router: 1.1.1.1

  Timers: Hello 10, Dead 40, Poll 40, Retransmit 5, Transmit delay 1

  Neighbor count is 1, Adjacent neighbor count is 1

  IPsec profile name: profile001

  Exchanging/Loading neighbors: 0

  Wait timer: Off,  LsAck timer: Off

  Prefix-suppression is enabled

表1-7 display ospfv3 interface命令显示信息描述表

字段

描述

Area

接口所属的区域ID

Interface ID

接口ID

Instance ID

实例ID

IPv6 prefixes

IPv6前缀

Cost

接口开销

State

根据OSPFv3接口状态机确定的当前接口状态，取值为：

·Down表示在接口上没有发送和接收任何路由协议的报文

·Waiting表示接口开始发送和接收Hello报文，并试图去识别网络上的DR和BDR

·P-2-P表示接口将每隔HelloInterval的时间间隔发送Hello报文，并尝试和接口链路另一端相连的路由器建立邻接关系

·DR表示路由器是所连网络的指定路由器

·BDR表示路由器是所连网络的备份指定路由器

·DROther表示路由器既不是所连网络的指定路由器，也不是所连网络的备份指定路由器

Type

接口的网络类型，取值为：

·PTP表示网络类型为点对点

·PTMP表示网络类型为点对多点

·Broadcast表示网络类型为广播

·NBMA表示网络类型为NBMA

MTU

接口MTU的值

Priority

接口的DR优先级

Designated router

本链路上的DR

Backup designated router

本链路上的BDR

Timer interval configured

配置的OSPFv3定时器，分别定义如下：

·Hello：接口发送Hello报文的时间间隔

·Dead：邻居的失效时间

·Poll：NBMA网络上发送轮询Hello报文的时间间隔

·Retransmit：接口重传LSA的时间间隔

·Transmit delay：接口对LSA的传输延迟时间

Neighbor count

接口的邻居数目

Adjacent neighbor count

接口的邻接数目

IPsec profile name

IPsec安全框架名

Exchanging/Loading neighbors

处于Exchanging或Loading状态的邻居个数

Wait timer

等待定时器，其中：

·Off： 关闭

·On： 开启

LsAck timer

报文确认定时器，其中：

·Off： 关闭

·On： 开启

Prefix-suppression is enabled

接口处于前缀抑制

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 lsdb**

------------------------------------------------------------------------

**[display ospfv3 lsdb**]命令用来显示OSPFv3的链路状态数据库信息。

【命令】

**[display ospfv3 **[ *process-id*  **lsdb** [ { **external** \| **grace** \| **inter-prefix** \| **inter-router** \| **intra-prefix** \| **link** \| **network** \| **nssa** \| **router** \| **unknown** [ *type* ] }  *link-state-id*  [ **originate-router** *router-id* \| **self-originate** ] \| **statistics** \| **total** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的链路状态数据库信息。

**[external**]：显示链路状态数据库中Type-5 LSA（AS External LSA）的信息。

**[grace**]：显示链路状态数据库中Type-11 LSA（Grace LSA）的信息。

**[inter-prefix**]：显示链路状态数据库中Type-3 LSA（Inter-Area-Prefix LSA）的信息。

**[inter-router**]：显示链路状态数据库中Type-4 LSA（Inter-Area-Router LSA）的信息。

**[intra-prefix**]：显示链路状态数据库中Type-9 LSA（Intra-Area-Prefix LSA）的信息。

**[link**]：显示链路状态数据库中Type-8 LSA（Link LSA）的信息。

**[network**]：显示链路状态数据库中Type-2 LSA（Network LSA）的信息。

**[nssa**]：显示链路状态数据库中Type-7 LSA（NSSA LSA）的信息。

**[router**]：显示链路状态数据库中Type-1 LSA（Router LSA）的信息。

**[unknown**]：显示链路状态数据库中未知类型LSA的信息。

*[type*]：LSA类型，取值范围十六进制0～FFFF。如果未指定本参数，将显示所有未知类型LSA的信息。

*[link-state-id*]：链路状态ID，IPv4地址形式。

**[originate-router** *router-id*]：发布该LSA的路由器的Router ID。

**[self-originate**]：显示本地路由器自己产生的LSA的链路状态数据库信息。

**[statistics**]：显示链路状态数据库中LSA的统计信息。

**[total**]：显示链路状态数据库中各种LSA的总数。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

【举例】

\# 显示OSPFv3的链路状态数据库信息。

\<Sysname\> display ospfv3 lsdb

               OSPFv3 Process 1 with Router ID 1.1.1.1

                  Link-LSA (Interface GigabitEthernet1/0/1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix

 0.15.0.8        2.2.2.2          0691  0x80000041 0x8315      1

 0.0.0.3         1.1.1.1          0623  0x80000001 0x0fee      1

                  Router-LSA (Area 0.0.0.1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum    Link

 0.0.0.0         1.1.1.1          0013  0x80000068 0x5d5f      2

 0.0.0.0         2.2.2.2          0024  0x800000ea 0x1e22      0

                  Network-LSA (Area 0.0.0.1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum

 0.15.0.8        2.2.2.2          0019  0x80000007 0x599e

                  Intra-Area-Prefix-LSA (Area 0.0.0.1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix  Reference

 0.0.0.2         2.2.2.2          3600  0x80000002 0x2eed      2 Network-LSA

 0.0.0.1         2.2.2.2          0018  0x80000001 0x1478      1 Network-LSA

表1-8 display ospfv3 lsdb命令显示信息描述表

字段

描述

Link State ID

链路状态ID

Origin Router

产生LSA的路由器

Age

LSA老化时间

SeqNum

LSA序列号

CkSum

LSA校验和

Prefix

前缀数目

Link

链路数目

Reference

引用的LSA类型

\# 显示OSPFv3链路状态数据库中Link-LSA的信息。

\<Sysname\> display ospfv3 lsdb link

               OSPFv3 Process 1 with Router ID 1.1.1.1

                  Link-LSA (Interface GigabitEthernet1/0/1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  LS age            : 833

  LS Type           : Link-LSA

  Link State ID     : 0.15.0.8

  Originating Router: 2.2.2.2

  LS Seq Number     : 0x80000041

  Checksum          : 0x8315

  Length            : 56

  Priority          : 1

[  Options           : 0x000013 (-\|R\|-\|-\|E\|V6)]

  Link-Local Address: fe80::200:5eff:fe00:100

  Number of Prefixes: 1

      Prefix        : 1001::/64

[      Prefix Options: 0 (-\|-\|-\|-)]

表1-9 display ospfv3 lsdb link命令显示信息描述表

字段

描述

LS age

LSA老化时间

LS Type

LSA类型

Link State ID

链路状态ID

Originating Router

产生LSA的路由器

LS Seq Number

LSA序列号

Checksum

LSA校验和

Length

LSA长度

Priority

路由器优先级

Options

选项

Link-Local Address

链路本地地址

Number of Prefixes

前缀的数目

Prefix

地址前缀

Prefix Options

前缀选项

\# 显示OSPFv3链路状态数据库中LSA的统计信息。

\<System\> display ospfv3 lsdb statistics

               OSPFv3 Process 1 with Router ID 1.1.1.1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Area ID         Router Network IntePre  InteRou IntraPre NSSA

 0.0.0.1         2      0       0        0       2        0

 0.0.0.3         1      0       0        0       1        1

 Total           2      0       0        0       3        1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                 Link   Grace   ASE

 Total           4      0       0

表1-10 display ospfv3 lsdb statistics命令显示信息描述表

字段

描述

Area ID

区域ID，显示该区域各类LSA的总数

Router

Type-1 LSA的数目

Network

Type-2 LSA的数目

IntePre

Type-3 LSA的数目

InteRou

Type-4 LSA的数目

IntraPre

Type-9 LSA的数目

NSSA

Type-7 LSA的数目

Link

Type-8 LSA的数目（只显示总数）

Grace

Type-11 LSA的数目

ASE

Type-5 LSA的数目（只显示总数）

Total

不同区域相同类型LSA的总数

\# 显示OSPFv3的链路状态数据库的详细信息。

\<Sysname\> display ospfv3 lsdb verbose

               OSPFv3 Process 1 with Router ID 1.1.1.1

                  Link-LSA (Interface GigabitEthernet1/0/1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix

 0.15.0.8        2.2.2.2          0691  0x80000041 0x8315      1

                 SendCnt: 0       RxmtCnt: 0       Status: Stale

 0.0.0.3         1.1.1.1          0623  0x80000001 0x0fee      1

                 SendCnt: 0       RxmtCnt: 0       Status: Stale

                  Router-LSA (Area 0.0.0.1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum    Link

 0.0.0.0         1.1.1.1          0013  0x80000068 0x5d5f      2

                 SendCnt: 0       RxmtCnt: 0       Status: Stale

 0.0.0.0         2.2.2.2          0024  0x800000ea 0x1e22      0

                 SendCnt: 0       RxmtCnt: 0       Status: Stale

                  Network-LSA (Area 0.0.0.1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum

 0.15.0.8        2.2.2.2          0019  0x80000007 0x599e

                 SendCnt: 0       RxmtCnt: 0       Status: Stale

                  Intra-Area-Prefix-LSA (Area 0.0.0.1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix  Reference

 0.0.0.2         2.2.2.2          3600  0x80000002 0x2eed      2 Network-LSA

                 SendCnt: 0       RxmtCnt: 0       Status: Stale

 0.0.0.1         2.2.2.2          0018  0x80000001 0x1478      1 Network-LSA

                 SendCnt: 0       RxmtCnt: 0       Status: Stale

表1-11 display ospfv3 lsdb verbose命令显示信息描述表

字段

描述

SendCnt

待发送该LSA的接口数目

RxmtCnt

该LSA在重传列表中的数目

Status

LSA所处的状态：

·Normal：正常状态

·Delayed：延迟生成的LSA

·Maxage routed：Maxage的LSA且已经经过拓扑前缀处理

·Self originated：收到自己产生的LSA

·Stale：GR过程中收到自己产生的LSA

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 nexthop**

------------------------------------------------------------------------

**[display ospfv3 nexthop**]命令用来显示OSPFv3的路由下一跳信息。

【命令】

**[display** **ospfv3** [ *process-id*  **nexthop**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的下一跳信息。

【举例】

\# 显示OSPFv3进程1的路由下一跳信息。

\<Sysname\>****display ospfv3 1 nexthop

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Nexthop : FE80::20C:29FF:FED7:F308                Interface: GE1/0/2

 RefCount: 4                                       Status   : Valid

 NbrID   : 1.1.1.1                                 NbrIntID : 21

 Nexthop : FE80::20C:29FF:FED7:F312                Interface: GE1/0/3

 RefCount: 3                                       Status   : Valid

 NbrID   : 1.1.1.1                                 NbrIntID : 38

表1-12 display ospfv3 nexthop命令显示信息描述表

字段

描述

Nexthop

下一跳地址

Interface

出接口名

RefCount

下一跳引用计数

Status

该下一跳的状态：

·Valid：有效

·Invalid：无效

NbrID

邻居路由器ID

NbrIntID

邻居的接口ID

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 non-stop-routing**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ospfv3 non-stop-routing**]命令用来显示OSPFv3进程的NSR状态信息。

【命令】

**[display ospfv3** [ *process-id*  **non-stop-routing**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的NSR状态信息。

【举例】

\# 显示所有OSPFv3进程的NSR状态信息。

\<Sysname\> display ospfv3 non-stop-routing

               OSPFv3 Process 1 with Router ID 3.3.3.3

 Nonstop Routing capability: Enabled

 Upgrade phase             : Normal

表1-13 display ospfv3 non-stop-routing命令显示信息描述表

字段

描述

Nonstop Routing capability

是否使能OSPFv3协议的NSR能力

·Enabled：使能

·Disabled：未使能

Upgrade phase

NSR的各个阶段，有如下几种：

·Normal：普通状态

·Preparation：准备阶段

·Smooth：数据平滑阶段

·Precalculation：路由计算预处理阶段

·Calculation：路由计算阶段

·Redistribution：路由引入阶段

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 peer**

------------------------------------------------------------------------

**[display ospfv3 peer**]命令用来显示OSPFv3的邻居信息。

【命令】

**[display ospfv3 **[ *process-id*   **area** *area-id*  **peer**  [ *interface-type interface-number*   **verbose**  \| *peer-router-id* \| **statistics** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[area*** area-id*]：显示位于指定区域的邻居信息。*area-id*为区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

*[interface-type interface-number*]：接口类型和接口编号。

**[verbose**]：显示邻居的详细信息。

*[peer-router-id*]：显示指定邻居的信息。

**[statistics**]：显示OSPFv3邻居的统计信息。

【使用指导】

·如果未指定OSPFv3进程号，将显示所有OSPFv3进程的邻居信息。

·如果未指定区域，将显示所有区域的邻居信息。

·如果接口参数、邻居Router ID参数都不输入，则显示所有接口的邻居信息。

【举例】

\# 显示OSPFv3进程1的邻居信息。

·路由应用

\<Sysname\> display ospfv3 1 peer gigabitethernet 1/0/1

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Area: 0.0.0.1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Router ID       Pri State             Dead-Time InstID Interface

 2.2.2.2         1   Full/DR           00:00:33  0      GE1/0/1

·交换应用

\<Sysname\> display ospfv3 1 peer vlan-interface 1

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Area: 0.0.0.1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Router ID       Pri State             Dead-Time InstID Interface

 2.2.2.2         1   Init/ -           00:00:36  0      Vlan1

表1-14 display ospfv3 peer命令显示信息描述表

字段

描述

Router ID

邻居ID

Pri

邻居路由器优先级

State

邻居状态

Dead-Time

邻居路由器的失效时间

Inst ID

实例ID

Interface

和邻居相连的接口

\# 显示接口上的OSPFv3进程1的邻居详细信息。

·路由应用

\<Sysname\> display ospfv3 1 peer gigabitethernet 1/0/2 verbose

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Area 0.0.0.1 interface GE1/0/2\'s neighbors

 Router ID: 2.2.2.2          Address: fe80::200:5eff:fe00:100

   State: Full  Mode: Nbr is master  Priority: 1

   DR: 2.2.2.2  BDR: None   MTU: 1500

[   Options is 0x000013 (-\|R\|-\|x\|E\|V6)]

   Dead timer due in 00:00:38

   Neighbor is up for 00:19:07

   Neighbor state change count: 120

   Database Summary List 0

   Link State Request List 0

   Link State Retransmission List 3

   Neighbor interface ID: 8037

   GR state: Normal

   Grace period: 0           Grace period timer: Off

   DD Rxmt timer: Off        LS Rxmt timer: On

·交换应用

\<Sysname\> display ospfv3 1 peer vlan-interface 1 verbose

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Area 0.0.0.1 interface Vlan1\'s neighbors

 Router ID: 2.2.2.2          Address: fe80::200:5eff:fe00:100

   State: ExStart  Mode: None  Priority: 1

   DR: 2.2.2.2  BDR: None   MTU: 1500

[   Options is 0x000013 (-\|R\|-\|x\|E\|V6)]

   Dead timer due in 00:00:33

   Neighbor is up for 00:24:19

   Neighbor state change count: 205

   Database Summary List 0

   Link State Request List 0

   Link State Retransmission List 0

   Neighbor interface ID: 8037

   GR state: Normal

   Grace period: 0           Grace period timer: Off

   DD Rxmt timer: Off        LS Rxmt timer: On

表1-15 display ospfv3 peer verbose命令显示信息描述表

字段

描述

Router ID

邻居的Router ID

Address

接口链路本地地址

State

邻居状态

Mode

路由器在数据库同步阶段，路由器与邻居协商的主从关系，取值为：

·Nbr is master：邻居路由器为主路由器

·Nbr is slave：邻居路由器为从路由器

Priority

邻居路由器优先级

DR

接口所属网段的DR

BDR

接口所属网段的BDR

MTU

接口MTU的值

Options

邻居的LSA选项，各选项含义如下：

·DC：支持按需链路

·R：是否为活跃路由器

·N：是否支持NSSA外部LSA

·x：保留

·E：AS外部LSA的接受能力

·V6：是否参与IPv6路由计算

Dead timer due in 33  sec

邻居将在33秒后被认为不可达

Neighbor is up for 00:24:19

与邻居建立的时长00:24:19

Neighbor state change count

邻居状态发生改变的次数

Database Summary List

需要DD报文发送的LSA个数

Link State Request List

链路状态请求列表中LSA个数

Link State Retransmission List

链路状态重传列表中LSA个数

Neighbor interface ID

邻居的接口ID

GR state

GR状态，取值为：

·Normal：普通状态

·Doing GR：正在作为GR Restarter

·Complete GR：GR完成

·Helper：正在作为GR Helper

Grace period

发送Grace LSA的间隔

Grace period timer

发送Grace LSA的间隔定时器，其中：

·Off： 关闭

·On：开启

DD Rxmt timer

DD报文重传定时器，其中：

·Off： 关闭

·On：开启

LS Rxmt timer

LSU报文重传定时器，其中：

·Off： 关闭

·On：开启

\# 显示所有OSPFv3邻居的统计信息。

\<Sysname\> display ospfv3 peer statistics

               OSPFv3 Process 1 with Router ID 1.1.1.1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Area ID         Down Attempt Init 2-Way ExStart Exchange Loading Full Total

 0.0.0.0         0    0       0    0     0       0        0       1    1

 Total           0    0       0    0     0       0        0       1    1

表1-16 display ospfv3 peer statistics命令显示信息描述表

字段

描述

Area ID

区域标识

Down

该状态为OSPFv3建立邻居关系的初始化状态，表示OSPFv3路由器在一定时间之内没有收到从某一邻居路由器发送来的信息

Attempt

该状态仅对NBMA网络上的邻居有效，表示最近没有从邻居收到信息，但仍需作出进一步的尝试，用以与邻居联系

Init

此状态表示OSPFv3路由器已经接收到邻居路由器发送来的Hello数据包，但该Hello数据包内没有包含自己的Router ID，还没有建立起双方的双向通信

2-Way

此状态表示OSPFv3路由器与邻居路由器的双向通信已经建立。DR及BDR的选择是在这个状态（或更高的状态）完成的

ExStart

在此状态，路由器要确定邻居双方的主从关系并决定初始的DD报文的序列号

Exchange

在此状态，OSPFv3路由器向其邻居路由器发送DD报文来交换链路状态信息

Loading

在此状态，OSPFv3路由器向邻居路由器发送LSR报文，请求最新的链路状态信息

Full

在此状态，建立起邻居关系的路由器之间已经完成了数据库同步的工作，它们的链路状态数据库已经一致

Total

所有区域中处于相同状态的邻居数目的总和

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 request-queue**

------------------------------------------------------------------------

**[display ospfv3 request-queue**]命令用来显示OSPFv3请求列表的信息。

【命令】

**[display ospfv3 ** *process-id* ]  **area** *area-id*  **request-queue**  *interface-type interface-number*   *neighbor-id*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[area*** area-id*]：显示位于指定区域的信息。*area-id*为区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

*[interface-type interface-number*]：接口类型和编号。

*[neighbor-id*]：邻居路由器的Router ID。

【使用指导】

l如果未指定OSPFv3进程号，将显示所有OSPFv3进程的请求列表信息。

l如果未指定OSPFv3区域号，将显示所有OSPFv3区域的请求列表信息。

l如果未指定接口，将显示所有接口的请求列表信息。

l如果未指定邻居路由器，将显示所有邻居路由器的请求列表信息。

【举例】

\# 显示OSPFv3请求列表的信息。

\<Sysname\> display ospfv3 request-queue

               OSPFv3 Process 1 with Router ID 1.1.1.1

                   Area: 0.0.0.0

                   Interface GigabitEthernet1/0/1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                   Nbr-ID 1.3.3.3 Request List

 Type    LinkState ID    AdvRouter       SeqNum       Age   CkSum

 0x4005  0.0.34.127      1.3.3.3         0x80000001   0027  0x274d

 0x4005  0.0.34.128      1.3.3.3         0x80000001   0027  0x2d45

 0x4005  0.0.34.129      1.3.3.3         0x80000001   0027  0x333d

 0x4005  0.0.34.130      1.3.3.3         0x80000001   0027  0x3935

表1-3 display ospfv3 request-queue命令显示信息描述表

字段

描述

Area

区域ID

Interface

接口类型和序号

Nbr-ID

邻居ID

Request List

请求列表信息

Type

LSA类型

LinkState ID

链路状态标示符

AdvRouter

通告路由器

SeqNum

LSA序列号

Age

LSA老化时间

CkSum

校验和

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 retrans-queue**

------------------------------------------------------------------------

**[display ospfv3 retrans-queue**]命令用来显示OSPFv3重传列表的信息。

【命令】

**[display ospfv3 ** *process-id* ]  **area** *area-id*  **retrans-queue**  *interface-type interface-number*   *neighbor-id*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[area*** area-id*]：显示位于指定区域的信息。*area-id*为区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

*[interface-type interface-number*]：接口类型和编号。

*[neighbor-id*]：邻居路由器的Router ID。

【使用指导】

l如果未指定OSPFv3进程号，将显示所有OSPFv3进程的重传列表信息。

l如果未指定OSPFv3区域号，将显示所有OSPFv3区域的重传列表信息。

l如果未指定接口，将显示所有接口的重传列表信息。

l如果未指定邻居路由器，将显示所有邻居路由器的重传列表信息。

【举例】

\# 显示OSPFv3重传列表的信息。

\<Sysname\> display ospfv3 retrans-queue

               OSPFv3 Process 1 with Router ID 1.1.1.1

                   Area: 0.0.0.0

                   Interface GigabitEthernet1/0/1

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                   Nbr-ID 1.2.2.2 Retransmit List

 Type    LinkState ID    AdvRouter       SeqNum       Age   CkSum

 0x2009  0.0.0.0         1.3.3.3         0x80000001   3600  0x49fb

表1-4 display ospfv3 retrans-queue命令显示信息描述表

字段

描述

Area

区域ID

Interface

接口类型和序号

Nbr-ID

邻居ID

Retransmit List

重传列表信息

Type

LSA类型

LinkState ID

链路状态标示符

AdvRouter

通告路由器

SeqNum

LSA序列号

Age

LSA老化时间

CkSum

校验和

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 routing**

------------------------------------------------------------------------

**[display ospfv3 routing**]命令用来显示OSPFv3路由表的信息。

【命令】

**[display ospfv3 ** *process-id* ] **routing**  *ipv6-address* *prefix-length*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的路由表信息。

*[ipv6-address prefix-length*]：显示指定IPv6地址的OSPFv3路由表的信息。*ipv6-address*表示IPv6地址前缀；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。

【举例】

\# 显示OSPFv3路由表的信息。

\<Sysname\> display ospfv3 routing

               OSPFv3 Process 1 with Router ID 9.9.9.9

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 I  - Intra area route,  E1 - Type 1 external route,  N1 - Type 1 NSSA route

 IA - Inter area route,  E2 - Type 2 external route,  N2 - Type 2 NSSA route

 \*  - Selected route

 \*Destination: 3::3/128

  Type       : I                                         Cost     : 0

  Nexthop    : ::                                        Interface: Loop1

  AdvRouter  : 9.9.9.9                                   Area     : 0.0.0.0

  Preference : 10

 \*Destination: 4::4/128

  Type       : I                                         Cost     : 1

  Nexthop    : FE80::20C:29FF:FED4:7171                  Interface: GE1/0/2

  AdvRouter  : 8.8.8.8                                   Area     : 0.0.0.0

  Preference : 10

 \*Destination: 6::/64

  Type       : I                                         Cost     : 1

  Nexthop    : ::                                        Interface: GE1/0/2

  AdvRouter  : 9.9.9.9                                   Area     : 0.0.0.0

  Preference : 10

 Total: 3

 Intra area: 3         Inter area: 0         ASE: 0         NSSA: 0

表1-17 display ospfv3 routing命令显示信息描述表

字段

描述

Destination

目的网段

Type

路由类型

Cost

路由开销值

Nexthop

下一跳地址

Interface

出接口

AdvRouter

发布路由器

Area

区域ID

Tag

外部路由标记

Preference

路由优先级

Total

路由总数目

Intra area

区域内路由数目

Inter area

区域间路由数目

ASE

5类外部路由数目

NSSA

7类外部路由数目

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 spf-tree**

------------------------------------------------------------------------

**[display ospfv3 spf-tree**]命令用来显示OSPFv3区域的拓扑信息。

【命令】

**[display** **ospfv3** [ *process-id*   **area** *area-id*  **spf-tree**  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的区域拓扑信息。

**[area*** area-id*]：显示位于指定区域的信息。如果未指定本参数，将显示所有区域的拓扑信息。*area-id*为区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

【举例】

\# 显示OSPFv3进程1下区域0的最短路径树信息。

\<Sysname\> display ospfv3 1 area 0 spf-tree

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Flags: S-Node is on SPF tree       R-Node is directly reachable

        I-Node or Link is init      D-Node or Link is to be deleted

        P-Neighbor is parent        A-Node is in candidate list

        C-Neighbor is child         H-Nexthop changed

        N-Link is a new path        V-Link is involved

                 Area: 0.0.0.0  Shortest Path Tree

 SPFNode         Type   Flag         SPFLink         Type   Cost  Flag

\>1.1.1.1         Router S R

                                  \--\>2.2.2.2         RT2RT  1     C

                                  \--\>2.2.2.2         RT2RT  1     P

表1-18 display ospfv3 spf-tree命令显示信息描述表

字段

描述

SPFNode

SPF节点，以宣告路由器ID作为标识，其中，Type为节点类型：

·Network：网络节点

·Router：路由器节点

Flag为节点标志：

·I：节点处于初始化状态

·T：节点在候选列表上

·S：节点在SPF树上

·R：该节点与根节点直连

·D：该节点将被删除

SPFLink

SPF链路，以宣告路由器ID作为标识，其中，Type为链路类型：

·RT2RT：表示路由器到路由器链路

·NET2RT：表示网络到路由器链路

·RT2NET：表示路由器到网络链路

Cost为链路花费，Flag为链路标志：

·I：链路处于初始化状态

·P：目的节点是父节点

·C：目的节点是子节点

·D：链路将要被删除

·H：下一跳发生改变

·V：目的节点删除或者是新增节点时，链路的目的节点不在SPF树上或处于删除状态

·N：新增链路，并且源节点和目的节点都在SPF树上

·L：链路在区域变化列表中

\# 显示OSPFv3进程1下区域0的最短路径树详细信息。

\<Sysname\> display ospfv3 1 area 0 spf-tree verbose

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Flags: S-Node is on SPF tree       R-Node is directly reachable

        I-Node or Link is init      D-Node or Link is to be deleted

        P-Neighbor is parent        A-Node is in candidate list

        C-Neighbor is child         H-Nexthop changed

        N-Link is a new path        V-Link is involved

           Area: 0.0.0.0  Shortest Path Tree

\>SPFNode[0]

  AdvID        : 1.1.1.1                  LsID       : 0.0.0.0

  NodeType     : Router                   Distance   : 1

  NodeFlag     : S R

  Nexthop count: 1

 \--\>NbrID      : 1.1.1.1                  NbrIntID   : 21

    Interface  : GE1/0/2                  NhFlag     : Valid

    Nexthop    : FE80::20C:29FF:FED7:F308

    RefCount   : 4

  SPFLink count: 1

 \--\>AdvID      : 1.1.1.1                  LsID       : 0.0.0.0

    IntID      : 232                      NbrIntID   : 465

    NbrID      : 2.2.2.2                  LinkType   : RT2RT

    LinkCost   : 1                        LinkNewCost: 1

    LinkFlag   : C                        NexthopCnt : 0

  ParentLink count: 1

 \--\>AdvID      : 1.1.1.1                  LsID       : 0.0.0.0

    IntID      : 215                      NbrIntID   : 466

    NbrID      : 2.2.2.2                  LinkType   : RT2RT

    LinkCost   : 1                        LinkNewCost: 1

    LinkFlag   : P                        NexthopCnt : 0

表1-19 display ospfv3 spf-tree verbose命令显示信息描述表

字段

描述

SPFNode

SPF节点

AdvID

通告路由器ID

LsID

链路状态ID

NodeType

节点类型

Distance

到根节点的开销

NodeFlag

节点标志

Nexthop count

下一跳计数

NbrID

邻居路由器ID

NbrIntID

邻居的接口ID

Interface

出接口

NhFlag

下一跳标志：

·Valid：有效

·Invalid：无效

Nexthop

下一跳地址

RefCount

下一跳的引用计数

SPFLink count

SPF链路计数

IntID

接口ID

LinkType

链路类型：

·RT2RT：表示路由器到路由器链路

·NET2RT：表示网络到路由器链路

·RT2NET：表示路由器到网络链路

LinkCost

当前链路花费

LinkNewCost

新的链路花费

LinkFlag

链路标志：

·I：链路处于初始化状态

·P：目的节点是父节点

·C：目的节点是子节点

·D：链路将要被删除

·H：下一跳发生改变

·V：目的节点删除或者是新增节点时，链路的目的节点不在SPF树上或处于删除状态

·N：新增链路，并且源节点和目的节点都在SPF树上

·L：链路在区域变化列表中

NexthopCnt

下一跳个数

ParentLink count

父链路计数

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 statistics**

------------------------------------------------------------------------

**[display ospfv3 statistics**]命令用来显示OSPFv3的统计信息。

【命令】

**[display ospfv3 ** *process-id* ] **statistics**  **error**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的统计信息。

**[error**]：显示错误统计信息。如果未指定本参数，将显示OSPFv3进程的报文、LSA和路由的统计信息。

【举例】

\# 显示OSPFv3的统计信息。

\<Sysname\> display ospfv3 statistics

               OSPFv3 Process 1 with Router ID 1.1.1.1

                   Packet Statistics

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Type                         Recv                Send

 Hello                        1746                1284

DB Description               505                 941

 Ls Req                       252                 136

 Ls Upd                       851                 1553

Ls Ack                       416                 450

             Local Originated LSAs Statistics

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Type                                             Count

 Router-LSA                                       192

 Network-LSA                                      0

Inter-Area-Prefix-LSA                            0

 Inter-Area-Router-LSA                            0

 AS-external-LSA                                  0

 NSSA-LSA                                         0

 Link-LSA                                         10

 Intra-Area-Prefix-LSA                            112

 Grace-LSA                                        0

 Unknown-LSA                                      0

 Total                                            314

                   Routes Statistics

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Type                                             Count

 Intra Area                                       0

 Inter Area                                       0

 ASE                                              0

 NSSA                                             0

表1-20 display ospfv3 statistics命令显示信息描述表

字段

描述

Packet Statistics

收发报文统计

Hello

Hello报文

DB Description

数据库描述报文

Ls Req

链路状态请求报文

Ls Upd

链路状态更新报文

Ls Ack

链路状态确认报文

Local Originated LSAs Statistics

生成的LSA统计

Router-LSA

Type-1 LSA的数目

Network-LSA

Type-2 LSA的数目

Inter-Area-Prefix-LSA

Type-3 LSA的数目

Inter-Area-Router-LSA

Type-4 LSA的数目

AS-external-LSA

Type-5 LSA的数目

NSSA-LSA

Type-7 LSA的数目

Link-LSA

Type-8 LSA的数目

Intra-Area-Prefix-LSA

Type-9 LSA的数目

Grace-LSA

Type-11 LSA的数目

Unknown-LSA

Unknown-LSA数目

Total

总数目

Routes Statistics

路由计数

Intra Area

区域内路由

Inter Area

区域间路由

ASE

5类外部路由

NSSA

7类外部路由

\# 显示OSPFv3进程的错误统计信息。

\<sysname\> display ospfv3 statistics error

               OSPFv3 Process 1 with Router ID 1.1.1.1

 0         : Transmit error               0         : Neighbor state low

 0         : Packet too small             0         : Bad version

 0         : Bad checksum                 0         : Unknown neighbor

 0         : Bad area ID                  0         : Bad packet

 0         : Packet dest error            0         : Inactive area packet

 0         : Router ID confusion          0         : Bad virtual link

 0         : HELLO: Hello-time mismatch   0         : HELLO: Dead-time mismatch

 0         : HELLO: Ebit option mismatch  0         : DD: Ebit option mismatch

 0         : DD: Unknown LSA type         0         : DD: MTU option mismatch

 0         : REQ: Empty request           0         : REQ: Bad request

 0         : UPD: LSA checksum bad        0         : UPD: Unknown LSA type

 0         : UPD: Less recent LSA         0         : UPD: LSA length bad

 0         : UPD: LSA AdvRtr id bad       0         : ACK: Bad ack packet

 0         : ACK: Invalid ack             0         : Interface down

 0         : Multicast incapable

表1-21 display ospfv3 statistics error命令显示信息描述表

字段

描述

Transmit error

发送出错的OSPFv3报文数

Neighbor state low

在低邻居状态收到的OSPFv3报文数

Packet too small

报文长度太小的OSPFv3报文数

Bad version

错误版本号的OSPFv3报文数

Bad checksum

校验和出错的OSPFv3报文数

Unknown neighbor

未知的邻居发来的OSPFv3报文数

Bad area ID

非法的区域ID的OSPFv3报文数

Bad packet

非法的OSPFv3报文数

Packet dest error

目的地址错误的OSPFv3报文数

Inactive area packet

非活动区域中接收到的报文数

Router ID confusion

含有重复路由器ID的OSPFv3报文数

Bad virtual link

错误的虚链路的OSPFv3报文数

HELLO: Hello-time mismatch

Hello定时器不匹配的Hello报文数

HELLO: Dead-time mismatch

Dead定时器不匹配的Hello报文数

HELLO: Ebit option mismatch

Option字段E位不匹配的Hello报文数

DD: Ebit option mismatch

Option字段E位不匹配的DD报文数

DD: Unknown LSA type

DD报文中含有未知类型LSA的数目

DD: MTU option mismatch

MTU不匹配的DD报文数

REQ: Empty request

不含有任何请求信息的LSR报文数

REQ: Bad request

请求错误LSA的LSR报文数

UPD: LSA checksum bad

LSU报文中含有错误校验和LSA的数目

UPD: Unknown LSA type

LSU报文中含有未知类型LSA的数目

UPD: Less recent LSA

LSU报文中含有不是最新LSA的数目

UPD: LSA length bad

LSU报文中含有错误长度LSA的数目

UPD: LSA AdvRtr id bad

LSU报文中含有错误宣告路由器LSA的数目

ACK: Bad ack packet

对LSU报文错误确认的ack报文数

ACK: Invalid ack

LSAck报文中无效确认ack的数目

Interface down

接口down计数

Multicast incapable

加入组播组出错计数

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 vlink**

------------------------------------------------------------------------

**[display ospfv3 vlink**]命令用来显示OSPFv3的虚连接信息。

【命令】

**[display ospfv3 ** *process-id* ] **vlink**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的虚连接信息。

【举例】

\# 显示OSPFv3的虚连接信息。

\<Sysname\> display ospfv3 vlink

               OSPFv3 Process 1 with Router ID 1.1.1.1

 Virtual-link Neighbor-id: 12.2.2.2, Neighbor-state: Full

 Interface: 2348 (Vlan-interface12), Instance-ID: 0

 Local  IPv6 address: 3:3333::12

 Remote IPv6 address: 2:2222::12

 Cost: 1  State: P-2-P  Type: Virtual

 Transit area: 0.0.0.1

 Timers: Hello 10, Dead 40, Retransmit 5, Transmit Delay 1

 IPsec profile name: profile001

表1-5 display ospfv3 vlink命令显示信息描述表

字段

描述

Virtual-link Neighbor-ID

通过虚连接相连的邻居路由器的Router ID

Neighbor-state

邻居状态，包括Down、Init、2-Way、ExStart、Exchange、Loading和Full

Interface

此虚连接的本端接口的端口号和名称

Instance-ID

实例ID

Local IPv6 address

本地IPv6地址

Remote IPv6 address

对端IPv6地址

Cost

接口的路由开销

State

接口状态

Type

类型：虚连接

Transit area

传输区域ID（如果当前接口为虚连接，则显示）

Timers

OSPFv3定时器，分别定义如下：

·Hello：接口发送Hello报文的时间间隔，单位为秒

·Dead：邻居的失效时间，单位为秒

·Retransmit：接口重传LSA时间间隔，单位为秒

Transmit Delay

接口对LSA的传输延迟时间，单位为秒

IPsec profile name

IPsec安全框架名

**OSPFv3 \-- OSPFv3配置命令 \-- enable ipsec-profile**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[enable ipsec-profile**]命令用来在OSPFv3区域应用IPsec安全框架。

**[undo enable ipsec-profile**]命令用来取消在OSPFv3区域应用的IPsec安全框架。

【命令】

**[enable ipsec-profile** *profile-name*]

**[undo enable ipsec-profile**]

【缺省情况】

OSPFv3区域没有应用IPsec安全框架。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：IPsec安全框架名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

本命令应结合IPsec安全框架使用，IPsec安全框架的具体情况请参见"安全配置指导"中的"IPsec"。

【举例】

\# 配置OSPFv3进程1区域0的安全框架为profile001。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 area 0

Sysname-ospfv3-1-area-0.0.0.0 enable ipsec-profile profile001

**OSPFv3 \-- OSPFv3配置命令 \-- filter (OSPFv3 area view)**

------------------------------------------------------------------------

**[filter**]命令用来配置对Inter-Area-Prefix-LSA进行过滤。

**[undo filter**]命令用来取消该配置。

【命令】

**[filter**[ { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } { **export** \| **import** }]]

**[undo**[ **filter** { **export** \| **import** }]]

【缺省情况】

没有配置对Inter-Area-Prefix-LSA进行过滤。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定的IPv6基本或高级访问控制列表，对进出本区域的Inter-Area-Prefix-LSA进行过滤，取值范围为2000～3999。

*[prefix-list-name*]：指定的IPv6地址前缀列表，对进出本区域的Inter-Area-Prefix-LSA进行过滤，为1～63个字符的字符串，区分大小写。

*[route-policy-name*]：指定的路由策略，对进出本区域的Inter-Area-Prefix-LSA进行过滤，为1～63个字符的字符串，区分大小写。

**[export**]：对ABR向其它区域发布的Inter-Area-Prefix-LSA进行过滤。

**[import**]：对ABR向本区域发布的Inter-Area-Prefix-LSA进行过滤。

【使用指导】

此命令只在ABR路由器上有效，对区域内部路由器无效。

【举例】

\# 根据IPv6地址前缀列表my-prefix-list和编号为2000的IPv6基本ACL分别对进出OSPFv3区域1的Inter-Area-Prefix-LSA进行过滤。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 area 1

Sysname-ospfv3-1-area-0.0.0.1 filter prefix-list my-prefix-list import

Sysname-ospfv3-1-area-0.0.0.1 filter 2000 export

**OSPFv3 \-- OSPFv3配置命令 \-- filter-policy export (OSPFv3 View)**

------------------------------------------------------------------------

**[filter-policy export**]命令用来配置对引入的路由信息进行过滤。

**[undo filter-policy export**]命令用来取消该配置。

【命令】

**[filter-policy**  { *acl6-number* \| **prefix-list** *prefix-list-name* } **export** [ *protocol* [ *process-id* ] ]]

**[undo filter-policy export** *protocol* \*[process-id*  ]]

【缺省情况】

没有对引入的路由信息进行过滤。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：用于过滤路由信息目的地址的IPv6基本或高级访问控制列表编号，取值范围为2000～3999。

*[prefix-list-name*]：用于过滤路由信息目的地址的IPv6地址前缀列表的名称，为1～63个字符的字符串，区分大小写。

*[protocol*]：路由协议名称，指定何种路由协议的路由信息将被过滤。目前可包括：**bgp4+、direct、isisv6、ospfv3**、**ripng**和**static**。如果没有指定*protocol*参数，对引入的任何一个协议产生的路由都要进行过滤。

*[process-id*]：路由协议进程号，取值范围为1～65535。只有当*protocol*为**isisv6**、**ospfv3**、**ripng**时，支持该参数。

【使用指导】

当配置的是高级ACL（3000～3999）时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour-addr sour-prefix*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour-addr sour-prefix* **destination** *dest-addr dest-prefix*]来过滤指定目的地址和掩码的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。

**[filter-policy export**]命令只对本设备使用**import-route**引入的路由起作用。如果没有配置**import-route**命令来引入其它外部路由（包括不同进程的[OSPFv3路由），则]**filter-policy export**命令无效。

【举例】

\# 根据IPv6地址前缀列表abc对引入的路由信息进行过滤。

\<Sysname\> system-view

Sysname ipv6 prefix-list abc permit 2002:1:: 64

Sysname ospfv3

Sysname-ospfv3-1 filter-policy prefix-list abc export

\# 使用编号为3000的IPv6高级ACL对引入的路由进行过滤，只允许2001::1/128通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128

Sysname-acl-ipv6-adv-3000 rule 100 deny ipv6

Sysname-acl-ipv6-adv-3000 quit

Sysname ospfv3

Sysname-ospfv3-1 filter-policy 3000 export

**OSPFv3 \-- OSPFv3配置命令 \-- filter-policy import (OSPFv3 View)**

------------------------------------------------------------------------

**[filter-policy import**]命令用来过滤通过接收到的LSA计算出来的路由信息。

**[undo filter-policy import**]命令用来恢复缺省情况。

【命令】

**[filter-policy**] { *acl6-number* [ **gateway** *prefix-list-name*  \| **prefix-list** *prefix-list-name*  **gateway** *prefix-list-name*  \| **gateway** *prefix-list-name* \| **route-policy** *route-policy-name* } **import**]

**[undo filter-policy import**]

【缺省情况】

不对通过接收到的LSA计算出来的路由信息进行过滤。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：用于过滤路由信息目的地址的IPv6基本或高级访问控制列表编号，取值范围为2000～3999。

**[gateway **]*prefix-list-name*：指定的IPv6地址前缀列表，基于要加入到路由表的路由信息的下一跳进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。如果未指定本参数，则不会基于要加入到路由表的路由信息的下一跳进行过滤。

**[prefix-list**] *prefix-list-name*：指定的地址前缀列表，基于目的地址对接收的路由信息进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy**] *route-policy-name*：指定路由策略名，基于路由策略对接收的路由信息进行过滤。*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

当配置的是高级ACL（3000～3999）或者指定的路由策略中配置的是高级ACL时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-prefix*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-prefix* **destination** *dest-addr dest-prefix*]来过滤指定目的地址和前缀的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。

**[filter-policy import**]命令只对OSPFv3计算出来的路由进行过滤，没有通过过滤的路由将不被加入路由表中，从而不能指导报文转发。

【举例】

\# 根据IPv6地址前缀列表abc对接收的路由信息进行过滤。

\<Sysname\> system-view

Sysname ipv6 prefix-list abc permit 2002:1:: 64

Sysname ospfv3

Sysname-ospfv3-1 filter-policy prefix-list abc import

\# 使用编号为3000的IPv6高级ACL对接收的路由进行过滤，只允许2001::1/128通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128

Sysname-acl-ipv6-adv-3000 rule 100 deny ipv6

Sysname-acl-ipv6-adv-3000 quit

Sysname ospfv3

Sysname-ospfv3-1 filter-policy 3000 import

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart enable**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart enable**]命令用来使能OSPFv3协议的GR能力。

**[undo graceful-restart enable**]命令用来关闭OSPFv3协议的GR能力。

【命令】

**[graceful-restart enable **[[ **global** \| **planned-only** ] \*]]

**[undo graceful-restart enable**]

【缺省情况】

OSPFv3的GR能力处于关闭状态。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[global**]：全局GR，必须保证所有的GR Helper都存在，整个GR才会完成，如果有一个GR Helper失效（比如，接口down），则整个GR失败。如果未指定本参数，表示支持接口级GR，即只要有一个GR Helper存在，则整个GR会完成。

**[planned-only**]：表示只支持计划重启。如果未指定本参数，表示计划重启和非计划重启都支持。计划重启指的是手动通过命令执行重启或主备倒换，在进行重启或主备倒换前GR Restarter会先发送Grace-LSA；非计划GR指的是由于设备故障等原因进行重启或主备倒换，在进行重启或主备倒换前GR Restarter不会事先发送Grace-LSA。

【使用指导】

**[graceful-restart enable**]和**non-stop-routing**命令互斥，不能同时配置。

支持OSPFv3的GR Restarter能力的设备主备倒换后，为了实现设备转发业务的不中断，它必须完成下列两项任务：

·重启过程GR Restarter转发表项保持稳定；

·重启流程结束后重建所有邻居关系，重新获取完整的网络拓扑信息；

【举例】

\# 使能OSPFv3进程1的GR能力。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 graceful-restart enable

【相关命令】

l**graceful-restart helper enable**

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart helper enable**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart helper enable**]命令用来使能OSPFv3的GR Helper能力。

**[undo graceful-restart helper enable**]命令用来关闭OSPFv3的GR Helper能力。

【命令】

**[graceful-restart helper enable ** **planned-only** ]

**[undo graceful-restart helper enable**]

【缺省情况】

OSPFv3的GR Helper能力处于开启状态。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[planned-only**]：表示只支持计划重启。如果未指定本参数，表示计划重启和非计划重启（即异常重启）都支持。

【使用指导】

收到Grace-LSA后，如果支持GR Helper能力则进入Helper模式（此时该邻居称为GR Helper）。在GR Restarter重新建立邻居的时候，GR Helper帮助GR Restarter进行LSDB的同步

【举例】

\# 使能OSPFv3进程1的GR Helper能力。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 graceful-restart helper enable

【相关命令】

·**graceful-restart enable**

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart helper strict-lsa-checking**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart helper strict-lsa-checking**]命令用来使能GR Helper严格LSA检查能力。

**[undo graceful-restart helper strict-lsa-checking**]命令用来关闭GR Helper严格LSA检查能力。

【命令】

**[graceful-restart helper strict-lsa-checking**]

**[undo graceful-restart helper strict-lsa-checking**]

【缺省情况】

GR Helper严格LSA检查能力处于关闭状态。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能GR Helper严格LSA检查能力，当检查到GR Helper设备的LSA发生变化时候，Helper设备退出GR Helper模式。

【举例】

\# 使能OSPFv3进程1的GR Helper严格LSA检查能力。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 graceful-restart helper strict-lsa-checking

【相关命令】

·**graceful-restart helper enable**

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart interval ***interval-value*]命令用来配置OSPFv3协议的GR重启间隔时间。

**[undo graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[graceful-restart interval ***interval-value*]

**[undo graceful-restart interval**]

【缺省情况】

OSPFv3协议的GR重启间隔时间为120秒。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：指定OSPFv3协议的GR重启间隔时间，取值范围为40～1800，单位为秒。

【使用指导】

配置此命令的用户需要确保配置的GR重启间隔不小于OSPFv3所有接口的邻居失效时间的最大值，否则可能造成GR重启失败。

【举例】

\# 配置OSPFv3进程1的GR重启间隔时间为100秒。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 graceful-restart interval 100

【相关命令】

·**ospfv3 timer dead**

**OSPFv3 \-- OSPFv3配置命令 \-- import-route (OSPFv3 view)**

------------------------------------------------------------------------

**[import-route**]命令用来配置引入外部路由信息。

**[undo import-route**]命令用来取消引入外部路由信息。

【命令】

**[import-route**[ *protocol* [ *process-id* \| **all-processes** \| **allow-ibgp**   **allow-direct** \| **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* ] \*]]

**[undo import-route**[ *protocol* [ *process-id* \| **all-processes** ]]]

【缺省情况】

没有引入外部路由信息。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：指定引入的路由协议，可以是**bgp4+**、**direct**、**isisv6**、**ospfv3**、**ripng**或**static**。

*[process-id*]：路由协议进程号，取值范围为1～65535，缺省值为1。只有当*protocol*是**isisv6**、**ospfv3**或**ripng**时该参数可选。

**[all-processes**]：引入指定路由协议所有进程的路由，只有当*protocol*是**ripng**、**ospfv3**或**isisv6**时可以指定该参数。

**[allow-ibgp**]：允许引入IBGP路由。只有当*protocol*是**bgp4+**时该参数可选。

**[allow-direct**]：在引入的路由中包含使能了该协议的接口网段路由。如果未指定本参数，在引入协议路由时不会包含使能了该协议的接口网段路由。当**allow-direct**与**route-policy** *route-policy-name*参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致**allow-direct**配置失效。例如，当配置**allow-direct**参数引入OSPFv3直连时，在路由策略中不要配置**if-match** **route-type**匹配条件，否则，**allow-direct**参数失效。

**[cost ***cost*]：路由开销值，取值范围为0～16777214，缺省值为1。

**[nssa-only**]：设置Type-7 LSA的P比特位不置位，即在对端路由器上不能转为Type-5 LSA。如果未指定本参数，Type-7 LSA的P比特位被置位，即在对端路由器上可以转为Type-5 LSA（如果本地路由器是ABR，则会检查骨干区域是否存在FULL状态的邻居，当FULL状态的邻居存在时，产生的Type-7 LSA中P比特位不置位）。

**[route-policy** *route-policy-name*]：配置只能引入符合指定路由策略的路由。*route-policy-name*为路由策略名称，为1～63个字符的字符串，区分大小写。

**[tag** *tag*]：外部LSA中的标记，取值范围为0～4294967295。如果未指定本参数，将根据**default tag**命令的配置进行取值。

**[type** *type*]：度量值类型，取值范围为1～2，缺省值为2。

【使用指导】

外部路由是指到达自治系统外部的路由，有两类：

l第一类外部路由（Type1 External）：这类路由的可信程度较高，并且和OSPFv3自身路由的开销具有可比性，所以到第一类外部路由的开销等于本路由器到相应的ASBR的开销与ASBR到该路由目的地址的开销之和。

l第二类外部路由（Type2 External）：这类路由的可信度比较低，所以OSPFv3协议认为从ASBR到自治系统之外的开销远远大于在自治系统之内到达ASBR的开销。所以计算路由开销时将主要考虑前者，即到第二类外部路由的开销等于ASBR到该路由目的地址的开销。如果计算出开销值相等的两条路由，再考虑本路由器到相应的ASBR的开销。

需要注意的是：

·该命令不能引入缺省路由。

·**import-route bgp4+**表示只引入EBGP路由；**import-route bgp4+ allow-ibgp**表示将IBGP路由也引入，容易引起路由环路，请慎用。

·**import-route ****nssa-only**命令配置后，引入的路由只在NSSA区域产生Type-7 LSA，不会在非NSSA区域产生Type-5 LSA。

【举例】

\# 指定引入进程号为10的RIPng路由为第二类路由，路由开销值为50。

\<Sysname\> system-view

Sysname ospfv3

Sysname-ospfv3-1 import-route ripng 10 type 2 cost 50

\# OSPFv3进程100引入OSPFv3进程160发现的路由。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 import-route ospfv3 160

【相关命令】

·**default-route-advertise******(OSPFv3 view)

**OSPFv3 \-- OSPFv3配置命令 \-- log-peer-change**

------------------------------------------------------------------------

**[log-peer-change**]命令用来打开邻居状态变化的输出开关。

**[undo log-peer-change**]命令用来关闭邻居状态变化的输出开关。

【命令】

**[log-peer-change**]

**[undo log-peer-change**]

【缺省情况】

邻居状态变化的输出开关处于打开状态。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

打开邻居状态输出开关后，OSPFv3邻居状态变化时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）

【举例】

\# 关闭OSPFv3进程100的邻居状态变化的输出开关。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 undo log-peer-change

**OSPFv3 \-- OSPFv3配置命令 \-- lsa-generation-interval**

------------------------------------------------------------------------

**[lsa-generation-interval**]命令用来配置OSPFv3 LSA重新生成的时间间隔。

**[undo lsa-generation-interval**]命令用来恢复缺省情况。

【命令】

**[lsa-generation-interval ***maximum-interval * *minimum-interval*  *incremental-interval*  ]

**[undo lsa-generation-interval**]

【缺省情况】

OSPFv3 LSA重新生成的最大时间间隔为5秒，最小时间间隔为0毫秒，时间间隔惩罚增量为0毫秒。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：OSPFv3 LSA重新生成的最大时间间隔，取值范围为1～60，单位为秒。

*[minimum-interval*]：OSPFv3 LSA重新生成的最小时间间隔，取值范围为10～60000，单位为毫秒。取值为0毫秒时表示不对OSPFv3 LSA重新生成的最小时间间隔进行限制。

*[incremental-interval*]：OSPFv3 LSA重新生成的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

通过调节LSA重新生成的时间间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。在网络变化不频繁的情况下，将LSA重新生成时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

需要注意的是，*minimum-interval*和*incremental-interval*配置值不允许大于*maximum-interval*配置值。

【举例】

\# 设置LSA重新生成的最大时间间隔为2秒，最小时间间隔为100毫秒，惩罚增量为100毫秒。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 lsa-generation-interval 2 100 100

【相关命令】

·**lsa-arrival-interval**

**OSPFv3 \-- OSPFv3配置命令 \-- maximum load-balancing (OSPFv3 view)**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[maximum load-balancing**]命令用来配置OSPFv3支持的等价路由的最大条数。

**[undo maximum load-balancing**]命令用来恢复缺省情况。

【命令】

**[maximum load-balancing** *maximum*]

**[undo maximum load-balancing**]

【缺省情况】

OSPFv3支持的等价路由的最大条数与系统支持最大等价路由的条数相同。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum*]：等价路由的最大条数，当*maximum*取值为1时，相当于不进行负载分担。不同型号的设备支持的取值范围与缺省值不同，请以设备的实际情况为准。

【使用指导】

如果通过**max-ecmp-num**命令配置系统支持最大等价路由的条数为m，则本命令的缺省值为m，取值范围为1～m。

**[max-ecmp-num**]命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置OSPFv3支持的等价路由的最大条数为2。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 maximum load-balancing 2

【相关命令】

·**max-ecmp-num**（三层技术-IP路由命令参考/IP路由基础）

**OSPFv3 \-- OSPFv3配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[non-stop-routing**]命令用来使能OSPFv3协议的NSR能力。

**[undo non-stop-routing**]命令用来关闭OSPFv3协议的NSR能力。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【缺省情况】

OSPFv3的NSR能力处于关闭状态。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[non-stop-routing**]和**graceful-restart enable**命令互斥，不能同时配置。

【举例】

\# 使能OSPFv3进程100的NSR能力。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 non-stop-routing

**OSPFv3 \-- OSPFv3配置命令 \-- nssa (OSPFv3 area view)**

------------------------------------------------------------------------

**[nssa**]命令用来配置一个区域为NSSA区域。

**[undo nssa**]命令用来恢复缺省情况。

【命令】

**[nssa **[ **default-route-advertise**[ [ **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* ] \* \| **no-import-route** \| **no-summary** \| [ **translate-always** \| **translate-never** ] \| **suppress-fa** \| **translator-stability-interval** *value* ] \*]]

**[undo nssa**]

【缺省情况】

没有区域被配置为NSSA区域。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[default-route-advertise**]：该参数只用于NSSA区域的ABR或ASBR，配置后，对于ABR，不论本地是否存在缺省路由，都将生成一条Type-7 LSA向区域内发布缺省路由；对于ASBR，只有当本地存在缺省路由时，才产生Type-7 LSA向区域内发布缺省路由。

**[cost** *cost*]：该缺省路由的度量值，取值范围为0～16777214。如果未指定本参数，缺省路由的度量值将取**default-cost**命令配置的值。

**[nssa-only**]：设置Type-7 LSA的P比特位不置位，即在对端路由器上不能转为Type-5 LSA，对端路由器不能引入Type-7 LSA产生的外部路由。如果未指定本参数，Type-7 LSA的P比特位被置位，即在对端路由器上可以转为Type-5 LSA，对端路由器可以引入Type-7 LSA产生的外部路由（如果本地路由器是ABR，则会检查骨干区域是否存在FULL状态的邻居，当FULL状态的邻居存在时，产生的Type-7 LSA中P比特位不置位）。

**[route-policy** *route-policy-name*]：路由策略名，为1～63个字符的字符串，区分大小写。只有*route-policy-name*指定的路由策略匹配时，才可以产生一个描述缺省路由的Type-7 LSA发布出去，指定的路由策略会影响Type-7 LSA中的属性。

**[tag** *tag*]：缺省路由的标识，取值范围为0～4294967295。

**[type** *type*]：该NSSA LSA的类型，取值范围为1～2，缺省类型为2。

**[no-import-route**]：该参数用于禁止将AS外部路由以Type-7 LSA的形式引入到NSSA区域中，这个参数通常只用在既是NSSA区域的ABR，也是OSPFv3自治系统的ASBR的路由器上，以保证所有外部路由信息能正确地进入OSPFv3路由域。

**[no-summary**]：该参数只用于NSSA区域的ABR，配置后，NSSA ABR只通过Type-3 LSA向区域内发布一条缺省路由，不再向区域内发布任何其它Type-3 LSA（这种区域又称为Totally NSSA区域）。

**[translate-always**]：指定ABR为NSSA区域的Type-7 LSA转换为Type-5 LSA的转换路由器。

**[translate-never**]：指定ABR不能将NSSA区域的Type-7 LSA转换为Type-5 LSA。

**[suppress-fa**]：指定当Type-7 LSA转换为Type-5 LSA时，生成的Type-5 LSA不携带Forwarding Address。

**[translator-stability-interval** *value*]：当有新的设备成为NSSA区域的Type-7 LSA转换为Type-5 LSA的转换路由器后，原Type-7 LSA转换为Type-5 LSA的转换路由器保持转换能力的时间。*value*为保持时间，取值范围为0～900，单位为秒。缺省值为0秒，即不保持。

【使用指导】

如果要将一个区域配置成NSSA区域，则该区域中的所有路由器都必须配置本命令。

【举例】

\# 将区域1配置成NSSA区域。

\<Sysname\> system-view

Sysname ospfv3 120

Sysname-ospfv3-120 area 1

Sysname-ospfv3-120-area-0.0.0.1 nssa

【相关命令】

·**default-cost **(OSPFv3 area view)

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3**

------------------------------------------------------------------------

**[ospfv3**]命令用来启动OSPFv3进程，并进入OSPFv3视图。

**[undo ospfv3**]命令用来关闭OSPFv3进程。

【命令】

**[ospfv3 **  *process-id* [\| **vpn-instance** *vpn-instance-name* ] \*]

**[undo ospfv3 **] *process-id*

【缺省情况】

系统没有运行OSPFv3进程。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535，缺省值为1。

**[vpn-instance*** vpn-instance-name*]：指定OSPFv3进程所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示OSPFv3位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

只有在OSPFv3视图下配置了Router ID，OSPFv3进程才能正常运行，否则只能看到该进程，但无法生成LSA。

【举例】

\# 启动进程号为120的OSPFv3进程并配置路由器的Router ID为1.1.1.1。

\<Sysname\> system-view

Sysname ospfv3 120

Sysname-ospfv3-120 router-id 1.1.1.1

【相关命令】

·**router-id**

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 area**

------------------------------------------------------------------------

**[ospfv3 area**]命令用来在接口上使能OSPFv3协议，并指定所属区域。

**[undo ospfv3 area**]命令用来在接口上关闭OSPFv3协议。

【命令】

**[ospfv3 ***process-id* **area** *area-id* [ **instance** *instance-id* ]]

**[undo ospfv3 ***process-id*** area** *area-id* [ **instance** *instance-id* ]]

【缺省情况】

接口上没有使能OSPFv3协议。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

*[area-id*]：区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上启动OSPFv3实例1的运行，并使能到Area 1中。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 1 area 1 instance 1

·交换应用

\# 在接口Vlan-interface10上启动OSPFv3实例1的运行，并使能到Area 1中。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 1 area 1 instance 1

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 bfd enable**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ospfv3 bfd enable**]命令用来在运行OSPFv3的接口下使能BFD功能。

**[undo ospfv3 bfd enable**]命令用来在运行OSPFv3的接口下关闭BFD功能。

【命令】

**[ospfv3 bfd enable** [ **instance** *instance-id* ]]

**[undo ospfv3 bfd enable ** **instance** *instance-id* ]

【缺省情况】

运行OSPFv3的接口未使能BFD功能。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

BFD（Bidirectional Forwarding Detection，双向转发检测）能够为OSPFv3邻居之间的链路提供快速检测功能。当邻居之间的链路出现故障时，加快OSPFv3协议的收敛速度。

OSPFv3通过BFD控制报文实现BFD功能。

【举例】

·路由应用

\# 使能接口GigabitEthernet1/0/1的OSPFv3实例1的BFD功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 bfd enable instance 1

·交换应用

\# 使能接口Vlan-interface11的OSPFv3实例1的BFD功能。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 ospfv3 bfd enable instance 1

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 cost**

------------------------------------------------------------------------

**[ospfv3 cost**]命令用来配置运行不同OSPFv3实例的接口的开销值。

**[undo ospfv3 cost**]命令用来恢复缺省情况。

【命令】

**[ospfv3 cost** *value* [ **instance** *instance-id* ]]

**[undo ospfv3 cost** [ **instance** *instance-id* ]]

【缺省情况】

路由器接口按照带宽自动计算运行OSPFv3协议所需的开销；对于VLAN接口，缺省值为1；对于Loopback接口，缺省值为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接口运行OSPFv3协议的路由开销，Loopback接口的取值范围为0～65535，其他接口的取值范围为1～65535。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【举例】

·路由应用

\# 指定运行OSPFv3实例1的接口GigabitEthernet1/0/1的开销为33。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 cost 33 instance 1

·交换应用

\# 指定运行OSPFv3实例1的接口Vlan-interface10的开销为33。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 cost 33 instance 1

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 dr-priority**

------------------------------------------------------------------------

**[ospfv3 dr-priority**]命令用来配置运行不同OSPFv3实例的接口的DR优先级。

**[undo ospfv3 dr-priority**]命令用来恢复缺省情况。

【命令】

**[ospfv3 dr-priority*** priority* [ **instance** *instance-id* ]]

**[undo ospfv3 dr-priority** [ **instance** *instance-id* ]]

【缺省情况】

接口的DR优先级为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：接口的DR优先级，取值范围为0～255。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

接口的DR优先级决定了该接口在选举DR/BDR时所具有的资格，优先级高的在选举时被首先考虑。

【举例】

·路由应用

\# 设置运行OSPFv3实例1的接口GigabitEthernet1/0/1在选举DR/BDR时的优先级为8。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 dr-priority 8 instance 1

·交换应用

\# 设置运行OSPFv3实例1的接口Vlan-interface10在选举DR/BDR时的优先级为8。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 dr-priority 8 instance 1

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 ipsec-profile**

------------------------------------------------------------------------

![说明](OSPFv3命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ospfv3 ipsec-profile**]命令用来在OSPFv3接口上应用IPsec安全框架。

**[undo ospfv3 ipsec-profile**]命令用来取消OSPFv3接口上应用的IPsec安全框架。

【命令】

**[ospfv3 ipsec-profile***profile-name* [ **instance** **** *instance-id* ]]

**[undo ospfv3 ipsec-profile** [ **instance** **** *instance-id* ]]

【缺省情况】

OSPFv3接口没有应用IPsec安全框架。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：IPsec安全框架名称，为1～63个字符的字符串，不区分大小写。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

本命令应结合IPsec安全框架使用，IPsec安全框架的具体情况请参见"安全配置指导"中的"IPsec"。

【举例】

l路由应用

\# 配置OSPFv3接口GigabitEthernet1/0/1上应用的IPsec安全框架为profile001。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 ipsec-profile profile001

l交换应用

\# 配置OSPFv3接口Vlan-interface10上应用的IPsec安全框架为profile001。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 ipsec-profile profile001

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 mib-binding**

------------------------------------------------------------------------

**[ospfv3 mib-binding**]命令用来配置OSPFv3进程绑定MIB。

**[undo ospfv3 mib-binding**]命令用来恢复缺省情况。

【命令】

**[ospfv3 mib-binding** *process-id*]

**[undo ospfv3 mib-binding**]

【缺省情况】

MIB绑定在进程号最小的OSPFv3进程上。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

【使用指导】

·如果指定的*process-id*不存在，配置OSPFv3进程绑定命令时将会提示OSPFv3进程不存在，无法完成配置。

·如果配置了OSPFv3进程绑定MIB，若删除*process-id*对应的OSPFv3进程，则同时删除OSPFv3进程绑定MIB配置，MIB绑定到进程号最小的OSPFv3进程上。

【举例】

\#配置OSPFv3进程100绑定MIB。

\<Sysname\> system-view

Sysname ospfv3 mib-binding 100

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 mtu-ignore**

------------------------------------------------------------------------

**[ospfv3 mtu-ignore**]命令用来配置接口在进行DD报文交换时忽略MTU检查。

**[undo ospfv3 mtu-ignore**]命令用来恢复缺省情况。

【命令】

**[ospfv3 mtu-ignore**** **instance** *instance-id* ]

**[undo ospfv3 mtu-ignore**** **instance** *instance-id* ]

【缺省情况】

接口在进行DD报文交换时执行MTU检查。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

双方的接口MTU必须相同才能建立邻居关系。

【举例】

l路由应用

\# 配置运行OSPFv3实例1的接口GigabitEthernet1/0/1在进行DD报文交换时忽略MTU检查。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 mtu-ignore instance 1

l交换应用

\# 配置运行OSPFv3实例1的接口Vlan-interface10在进行DD报文交换时忽略MTU检查。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 mtu-ignore instance 1

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 network-type**

------------------------------------------------------------------------

**[ospfv3 network-type**]命令用来配置OSPFv3接口的网络类型。

**[undo ospfv3 network-type**]命令用来恢复缺省情况。

【命令】

**[ospfv3 network-type ****[ broadcast**[ \| **nbma** \| **p2mp** [ **unicast** ] \| **p2p** }  **instance** *instance-id* ]]

**[undo ospfv3 network-type** [ **instance** *instance-id* ]]

【缺省情况】]

当接口封装的链路层协议不同时，OSPFv3接口网络类型的缺省值也不同：

l当接口封装的链路层协议是Ethernet、FDDI时，OSPFv3接口网络类型的缺省值为广播类型；

l当接口封装的链路层协议是ATM、帧中继或X.25时，OSPFv3接口网络类型的缺省值为NBMA；

l当接口封装的链路层协议是PPP、LAPB、HDLC或POS时，OSPFv3接口网络类型的缺省值为P2P。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[broadcast**]：配置接口的网络类型为广播类型。

**[nbma**]：配置接口的网络类型为NBMA类型。

**[p2mp**]：配置接口的网络类型为点到多点类型。

**[unicast**]：P2MP类型支持单播发送报文，缺省情况下是组播方式发送报文。

**[p2p**]：配置接口的网络类型为点到点类型。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

l如果在广播网络上有不支持组播地址的路由器，可以将接口的网络类型改为NBMA。

l在NBMA网络中，如果任意两台路由器之间都有一条虚电路直接可达，或者说，这个网络是全连通的，那么可以把OSPFv3接口的网路类型配置为NBMA；否则，需要把OSPFv3接口的网络类型配置为点到多点，这样，两台不能直接可达的路由器之间可以通过一台与两者都直接可达的路由器来交换路由信息。

l接口的网络类型为NBMA或P2MP（unicast）时，必须使用peer命令来配置邻接点。

l接口的网络类型为P2MP（unicast）时，OSPFv3协议在该接口上发送的报文均为单播报文。

【举例】

l路由应用

\# 设置运行OSPFv3的接口GigabitEthernet1/0/1网络类型为NBMA。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 network-type nbma

l交换应用

\# 设置运行OSPFv3的接口Vlan-interface20网络类型为NBMA。

\<Sysname\> system-view

Sysname interface vlan-interface 20

Sysname-Vlan-interface20 ospfv3 network-type nbma

【相关命令】

l**ospfv3 dr-priority**

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 peer**

------------------------------------------------------------------------

**[ospfv3 peer**]命令用来指定邻居接口的链路本地地址，并指定该邻居是否有选举权。

**[undo ospfv3 peer**]命令用来取消该操作。

【命令】

**[ospfv3 peer**[ *ipv6-address* [ **cost** *value* \| **dr-priority** *dr-priority* ]  **instance** *instance-id* ]]

**[undo ospfv3 peer** *ipv6-address* [ **instance** *instance-id* ]]

【缺省情况】

没有指定邻居接口的链路本地地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：邻居的链路本地地址。

**[cost*** value*]：表示网络邻居的开销，取值范围为1～65535。

**[dr-priority*** dr-priority*]：表示网络邻居的优先级，取值范围为0～255，缺省值为1。

**[instance*** instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

当路由器的接口类型为如下网络类型时，需要为其指定相邻路由器IP地址：

·NBMA网络

·P2MP网络（仅当接口选择单播形式发送报文时，需要此配置）

由于无法通过广播Hello报文的形式发现相邻路由器，必须手工指定相邻路由器的本地链路地址。对于NBMA网络，可以指定该相邻路由器是否有选举权等。

【举例】

l路由应用

\# 在运行OSPFv3协议的接口GigabitEthernet1/0/1上指定邻居的链路本地地址为FE80::1111。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 peer fe80::1111

l交换应用

\# 在运行OSPFv3协议的接口Vlan-interface10上指定邻居的链路本地地址为FE80::1111。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 peer fe80::1111

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 prefix-suppression**

------------------------------------------------------------------------

**[ospfv3 prefix-suppression**]命令用来抑制接口进行前缀发布。

**[undo ospfv3 prefix-suppression**]命令用来取消该配置。

【命令】

**[ospfv3 prefix-suppression** [ **disable**   **instance** *instance-id* ]]

**[undo ospfv3 prefix-suppression ** **instance** *instance-id* ]

【缺省情况】

不抑制接口进行前缀发布。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disable**]：不抑制接口进行前缀发布。

**[instance** *instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

如果OSPFv3进程配置了抑制前缀发布，但某个接口不想进行抑制，此时可以配置本命令并指定**disable**参数。

【举例】

l路由应用

\# 抑制接口GigabitEthernet1/0/1进行前缀发布。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 prefix-suppression

l交换应用

\# 抑制接口Vlan-interface10进行前缀发布。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 prefix-suppression

【相关命令】

l**prefix-suppression**

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer dead**

------------------------------------------------------------------------

**[ospfv3 timer dead**]命令用来设置OSPFv3的邻居失效时间。

**[undo ospfv3 timer dead**]命令用来恢复缺省情况。

【命令】

**[ospfv3 timer dead ***seconds * **instance** *instance-id* ]

**[undo ospfv3 timer dead ** **instance** *instance-id* ]

【缺省情况】

P2P、Broadcast类型接口的OSPFv3邻居失效的时间为40秒；P2MP、NBMA类型接口的OSPFv3邻居失效的时间为120秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：OSPFv3邻居失效的时间，取值范围为1～65535，单位为秒。

【使用指导】

OSPFv3邻居的失效时间是指：在该时间间隔内，若未收到邻居的Hello报文，就认为该邻居已失效。**dead** *seconds*值至少应为**hello** *seconds*值的4倍，同一网段上的接口的**dead ***seconds*也必须相同。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1上的邻居失效时间为60秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 timer dead 60

·交换应用

\# 配置接口Vlan-interface10上的邻居失效时间为60秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 timer dead 60

【相关命令】

·**ospfv3 timer hello**

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer hello**

------------------------------------------------------------------------

**[ospfv3 timer hello**]命令用来配置接口发送Hello报文的时间间隔。

**[undo ospfv3 timer hello**]命令用来恢复缺省情况。

【命令】

**[ospfv3 timer hello ***seconds * **instance** *instance-id* ]

**[undo ospfv3 timer hello ** **instance** *instance-id* ]

【缺省情况】

P2P、Broadcast类型接口发送Hello报文的时间间隔为10秒；P2MP、NBMA类型接口发送Hello报文的时间间隔为30秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口发送Hello报文的时间间隔，取值范围为1～65535，单位为秒。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

*[seconds*]的值越小，发现网络拓扑改变的速度越快，对系统资源的开销也就越大。同一网段上的接口的*seconds*必须相同。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1发送Hello报文的时间间隔为20秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 timer hello 20

·交换应用

\# 配置接口Vlan-interface10发送Hello报文的时间间隔为20秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 timer hello 20

【相关命令】

·**ospfv3 timer dead**

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer poll**

------------------------------------------------------------------------

**[ospfv3 timer poll**]命令用来配置在NBMA接口上向状态为down的邻居路由器发送轮询Hello报文的时间间隔。

**[undo ospfv3 timer poll**]命令用来恢复缺省情况。

【命令】

**[ospfv3 timer poll ***seconds * **instance** *instance-id* ]

**[undo ospfv3 timer poll** [ **instance** *instance-id* ]]

【缺省情况】

在NBMA接口上向状态为down的邻居路由器发送轮询Hello报文的时间间隔为120秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：向状态为down的邻居路由器发送轮询Hello报文的时间间隔，取值范围为1～65535，单位为秒。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

在NBMA的网络上，当邻居失效后，将按轮询时间间隔定期地发送Hello报文。用户可配置轮询时间间隔以指定该接口在与相邻路由器构成邻居关系之前发送Hello报文的时间间隔。

发送轮询Hello报文的时间间隔至少应为发送Hello报文时间间隔的4倍。

【举例】

l路由应用

\# 配置接口GigabitEthernet1/0/1发送轮询Hello报文的时间间隔为120秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 timer poll 120

l交换应用

\# 配置接口Vlan-interface10发送轮询Hello报文的时间间隔为120秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 timer poll 120

【相关命令】

l**ospfv3 timer hello**

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer retransmit**

------------------------------------------------------------------------

**[ospfv3 timer retransmit**]命令用来配置接口重传LSA的时间间隔。

**[undo ospfv3 timer retransmit**]命令用来恢复缺省情况。

【命令】

**[ospfv3 timer retransmit ***seconds * **instance** *instance-id* ]

**[undo ospfv3 timer retransmit ** **instance** *instance-id* ]

【缺省情况】

接口重传LSA的时间间隔为5秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口重传LSA的时间间隔，取值范围为1～3600，单位为秒。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

当一台路由器向它的邻居发送一条LSA后，需要等到对方的确认报文。若在该重传LSA的时间间隔内未收到对方的确认报文，就会重传这条LSA。

相邻路由器重传LSA时间间隔的值不要设置得太小，否则将会引起不必要的重传。

【举例】

l路由应用

\# 指定运行OSPFv3实例1的接口GigabitEthernet1/0/1重传LSA的时间间隔为12秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 timer retransmit 12 instance 1

l交换应用

\# 指定运行OSPFv3实例1的接口Vlan-interface10重传LSA的时间间隔为12秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 timer retransmit 12 instance 1

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 trans-delay**

------------------------------------------------------------------------

**[ospfv3 trans-delay**]命令用来配置接口对LSA的传输延迟时间。

**[undo ospfv3 trans-delay**]命令用来恢复缺省情况。

【命令】

**[ospfv3 trans-delay ***seconds * **instance** *instance-id* ]

**[undo ospfv3 trans-delay ** **instance** *instance-id* ]

【缺省情况】

接口对LSA的传输延迟时间为1秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口对LSA的传输延迟时间，取值范围为1～3600，单位为秒。

*[instance-id*]：接口所属的实例ID，取值范围为0～255，缺省值为0。

【使用指导】

LSA在本路由器的LSDB中会随时间老化（LSA的老化时间每秒钟加1），但在网络的传输过程中却不会，所以有必要在发送之前在LSA的老化时间上增加一定的延迟时间。此配置对低速率的网络尤其重要。

【举例】

l路由应用

\# 指定运行OSPFv3实例1的接口GigabitEthernet1/0/1洪泛LSA的时延值为3秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospfv3 trans-delay 3 instance 1

l交换应用

\# 指定运行OSPFv3实例1的接口Vlan-interface10洪泛LSA的时延值为3秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospfv3 trans-delay 3 instance 1

**OSPFv3 \-- OSPFv3配置命令 \-- preference**

------------------------------------------------------------------------

**[preference**]命令用来配置OSPFv3协议路由的优先级。

**[undo preference**]命令用来恢复缺省情况。

【命令】

**[preference** [ **ase**  { *preference* \| **route-policy** *route-policy-name* } \*]]

**[undo preference** [ **ase** ]]

【缺省情况】

OSPFv3内部路由的优先级为10，OSPFv3外部路由的优先级为150。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ase**]：配置外部路由的优先级。如果未指定该参数，配置内部路由优先级。

*[preference*]：OSPFv3路由的优先级，取值范围为1～255。优先级的值越小，其实际的优先程度越高。

**[route-policy*** route-policy-name*]：应用路由策略，对特定的路由设置优先级。*route-policy-name*是路由策略名称，为1～63个字符的字符串，区分大小写。

【使用指导】

由于路由器上可能同时运行多个动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题，所以为每一种路由协议指定了一个缺省的优先级。在不同的路由协议发现去往同一目的地的多条路由时，优先级高的协议发现的路由将被选中以转发IPv6报文。

【举例】

\# 配置OSPFv3协议路由的优先级为150。

\<Sysname\> system-view

Sysname ospfv3

Sysname-ospfv3-1 preference 150

**OSPFv3 \-- OSPFv3配置命令 \-- prefix-suppression**

------------------------------------------------------------------------

**[prefix-suppression**]命令用来抑制OSPFv3进程进行前缀发布。

**[undo prefix-suppression**]命令用来恢复缺省情况。

【命令】

**[prefix-suppression**]

**[undo prefix-suppression**]

【缺省情况】

不抑制OSPFv3进程进行前缀发布。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口使能OSPFv3后，会将接口下的所有网段路由都通过LSA发布，但有时候网段路由是不希望被发布的。通过前缀抑制配置，可以减少LSA中携带不需要的前缀，即不发布某些网段路由，从而提高网络安全性，加快路由收敛。

全局配置前缀抑制不能抑制LoopBack接口和处于silent-interface状态接口对应的前缀。如果想对Loopback接口或处于silent-interface状态接口进行抑制，可以通过接口下配置前缀抑制（**ospfv3 prefix-suppression**命令）来实现。

当使能前缀抑制时，具体处理如下：

lType-8 LSA中不发布处于抑制的接口前缀信息。

l对于广播网/NBMA网络，DR在生成Type-9 LSA引用Type-2 LSA时，不发布处于抑制的接口前缀信息。

l对于P2P/P2MP网络，生成Type-9 LSA引用Type-1 LSA时，不发布处于抑制的接口前缀信息。

【举例】

\# 抑制OSPFv3进程100的前缀发布。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 prefix-suppression

【相关命令】

l**ospfv3 prefix-suppression**

**OSPFv3 \-- OSPFv3配置命令 \-- reset ospfv3 process**

------------------------------------------------------------------------

**[reset ospfv3 process**]命令用来重启OSPFv3进程。

【命令】

**[reset** **ospfv3** [ *process-id*  **process**  **graceful-restart** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，则重启所有OSPFv3进程。

**[graceful-restart**]：以GR方式重启OSPFv3进程。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

使用**reset ospfv3 process**命令重启OSPFv3，可以获得如下结果：

l可以立即清除无效的LSA，而不必等到LSA超时。

l方便重新选举DR、BDR。

l重启前的OSPFv3配置不会丢失。

执行该命令后，系统提示用户确认是否重启OSPFv3协议。

【举例】

\# 重启所有OSPFv3进程。

\<Sysname\> reset ospfv3 process

Reset OSPFv3 process? [Y/N:y]

**OSPFv3 \-- OSPFv3配置命令 \-- reset ospfv3 redistribution**

------------------------------------------------------------------------

**[reset ospfv3 redistribution**]命令用来重新向OSPFv3引入外部路由。

【命令】

**[reset** **ospfv3** [ *process-id*  **redistribution**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，所有OSPFv3进程都将重新引入外部路由。

【举例】

\# 重新向OSPFv3引入外部路由。

\<Sysname\> reset ospfv3 redistribution

**OSPFv3 \-- OSPFv3配置命令 \-- reset ospfv3 statistics**

------------------------------------------------------------------------

**[reset ospfv3 statistics**]命令用来清除OSPFv3的统计信息。

【命令】

**[reset** **ospfv3** [ *process-id*  **statistics**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，则清除所有OSPFv3进程的统计信息。

【举例】

\# 清除所有OSPFv3进程的统计信息。

\<Sysname\> reset ospfv3 statistics

**OSPFv3 \-- OSPFv3配置命令 \-- router-id**

------------------------------------------------------------------------

**[router-id**]命令用来配置运行OSPFv3协议的路由器的Router ID。

**[undo router-id**]命令用来删除已配置的路由器的Router ID。

【命令】

**[router-id**] *router-id*

**[undo router-id**]

【缺省情况】

运行OSPFv3协议的路由器没有Router ID。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[router-id*]：路由器标识符，IPv4地址格式。

【使用指导】

Router ID是一台运行OSPFv3协议的路由器在自治系统中的唯一标识。如果用户没有指定路由器的Router ID，则OSPFv3进程无法运行。

设置路由器的Router ID时，必须保证自治系统中任意两个进程的Router ID都不相同。

通过指定不同的进程号，可以在一台路由器上运行多个OSPFv3进程，在这种情况下，必须为不同进程指定不同的Router ID。

【举例】

\# 设置OSPFv3进程1的Router ID为10.1.1.3。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 router-id 10.1.1.3

【相关命令】

·**ospfv3**

**OSPFv3 \-- OSPFv3配置命令 \-- silent-interface (OSPFv3 view)**

------------------------------------------------------------------------

**[silent-interface**]命令用来禁止接口收发OSPFv3报文。

**[undo silent-interface**]命令用来恢复缺省情况。

【命令】

**[silent-interface**[ { *interface-type interface-number* \| **all** }]]

**[undo silent-interface**[ { *interface-type interface-number* \| **all** }]]

【缺省情况】

允许接口收发OSPFv3报文。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：接口类型和接口号，禁止指定OSPFv3接口收发OSPFv3报文。

**[all**]：禁止所有OSPFv3接口收发OSPFv3报文。

【使用指导】

不同的进程可以对同一接口禁止收发OSPFv3报文，但**silent-interface**命令只对本进程已经使能的OSPFv3接口起作用，对其它进程的接口不起作用。

【举例】

l路由应用

\#禁止接口GigabitEthernet1/0/1在OSPFv3进程100和200中收发OSPFv3报文。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 router-id 10.100.1.9

Sysname-ospfv3-100 silent-interface gigabitethernet 1/0/1

Sysname-ospfv3-100 quit

Sysname ospfv3 200

Sysname-ospfv3-200 router-id 20.100.1.9

Sysname-ospfv3-200 silent-interface gigabitethernet 1/0/1

l交换应用

\# 禁止接口Vlan-interface10在OSPFv3进程100和200中收发OSPFv3报文。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 router-id 10.100.1.9

Sysname-ospfv3-100 silent-interface vlan-interface 10

Sysname-ospfv3-100 quit

Sysname ospfv3 200

Sysname-ospfv3-200 router-id 20.100.1.9

Sysname-ospfv3-200 silent-interface vlan-interface 10

**OSPFv3 \-- OSPFv3配置命令 \-- snmp-agent trap enable ospfv3**

------------------------------------------------------------------------

**[snmp-agent trap enable ospfv3**]命令用来开启OSPFv3的告警功能。

**[undo** **snmp-agent** **trap** **enable ospfv3**]命令用来关闭OSPFv3的告警功能。

【命令】

**[snmp-agent**[ **trap** **enable ospfv3** [ **grrestarter-status-change** \| **grhelper-status-change** \| **if-state-change** \| **if-cfg-error** \| **if-bad-pkt** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **virtif-bad-pkt** \| **virtif-cfg-error** \|**virtif-state-change** \| **virtgrhelper-status-change** \| **virtneighbor-state-chang** ] \*]]

**[undo snmp-agent**[ **trap** **enable ospfv3** [ **grrestarter-status-change** \| **grhelper-status-change** \| **if-state-change** \| **if-cfg-error** \| **if-bad-pkt** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **virtif-bad-pkt** \| **virtif-cfg-error** \|**virtif-state-change** \| **virtgrhelper-status-change** \| **virtneighbor-state-change**] \*]]

【缺省情况】

OSPFv3的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[grrestarter-status-change**]：GR Restarter状态变化。

**[grhelper-status-change**]：邻居GR Helper状态变化。

**[if-state-change**]：接口状态变化。

**[if-cfg-error**]：接口配置错误。

**[if-bad-pkt**]：接口接收了错误报文。

**[neighbor-state-change**]**：**邻居状态变化。

**[nssatranslator-status-change**]：NSSA转换路由器状态变化。

**[virtif-bad-pkt**]：虚接口接收错误报文。

**[virt-config-error**]：虚接口配置错误。

**[virtif-state-change**]：虚接口状态变化。

**[virtgrhelper-status-change**]：虚接口邻居GR Helper状态变化。

**[virtneighbor-state-change**]：虚接口邻居状态变化。

【举例】

\# 关闭OSPFv3的告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable ospfv3

**OSPFv3 \-- OSPFv3配置命令 \-- snmp context-name**

------------------------------------------------------------------------

**[snmp** **context-name**]命令用来创建一个管理OSPFv3的SNMP实体所使用的上下文名称。

**[undo** **snmp** **context-name**]命令用来恢复缺省情况。

【命令】

**[snmp** **context-name** *context-name*]

**[undo** **snmp** **context-name**]

【缺省情况】

没有配置管理OSPFv3的SNMP实体所使用的上下文名称。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：上下文的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

OSPFv3使用MIB（Management Information Base，管理信息库）为NMS（Network Management System，网络管理系统）提供对OSPFv3实例的管理，但标准OSPFv3 MIB中定义的MIB为单实例管理对象，无法对多个OSPFv3实例进行管理。因此，参考RFC 4750中对OSPF多实例的管理方法，为管理OSPFv3的SNMP实体定义一个上下文名称，以此来区分不同的OSPFv3实例，实现对多个OSPFv3实例进行管理。需要注意的是，由于上下文名称只是SNMPv3独有的概念，对于SNMPv1/v2c，会将团体名映射为上下文名称以对不同协议进行区分。

【举例】

\# 配置管理OSPFv3进程1的SNMP实体所使用的上下文名称为mib。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 snmp context-name mib

**OSPFv3 \-- OSPFv3配置命令 \-- snmp trap rate-limit**

------------------------------------------------------------------------

**[snmp trap rate-limit**]命令用来配置OSPFv3在指定时间间隔内允许输出的告警信息条数。

**[undo snmp trap rate-limit**]命令用来恢复缺省情况。

【命令】

**[snmp trap rate-limit interval*** trap-interval ***count** *trap-number*]

**[undo snmp trap rate-limit**]

【缺省情况】

OSPFv3在10内秒允许输出7条告警信息。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[trap-interval*]：指定时间间隔，取值范围为2～60，单位为秒。

*[trap-number*]：在指定时间间隔内允许输出的告警信息条数，取值范围为0～300，为0时表示不输出告警信息。

【举例】

\# 配置OSPFv3在5秒内允许输出10条告警信息。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 snmp trap rate-limit interval 5 count 10

**OSPFv3 \-- OSPFv3配置命令 \-- spf-schedule-interval**

------------------------------------------------------------------------

**[spf-schedule-interval**]命令用来配置OSPFv3路由计算的时间间隔。

**[undo spf-schedule-interval**]命令用来恢复缺省情况。

【命令】

**[spf-schedule-interval** *maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo spf-schedule-interval**]

【缺省情况】

OSPFv3路由计算的最大时间间隔为5秒，最小时间间隔为50毫秒，时间间隔惩罚增量为200毫秒。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：OSPFv3路由计算的最大时间间隔，取值范围为1～60，单位为秒。

*[minimum-interval*]：OSPFv3路由计算的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：OSPFv3路由计算的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

根据本地维护的LSDB，运行OSPFv3协议的路由器通过SPF算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。

本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

需要注意的是，*minimum-interval*和*incremental-interval*配置值不允许大于*maximum-interval*配置值。

【举例】

\# 设置OSPFv3路由计算最大时间间隔为10秒，最小时间间隔为500毫秒，惩罚增量为300毫秒。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 spf-schedule-interval 10 500 300

**OSPFv3 \-- OSPFv3配置命令 \-- stub (OSPFv3 area view)**

------------------------------------------------------------------------

**[stub**]命令用来配置一个区域为Stub区域。

**[undo stub**]命令用来恢复缺省情况。

【命令】

**[stub**[ [ **default-route-advertise-always** \| **no-summary** ] \*]]

**[undo stub**]

【缺省情况】

没有区域被设置为Stub区域。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[default-route-advertise-always**]：该参数用于设置总是通告默认路由。

**[no-summary**]：该参数只用于Stub区域的ABR，配置后ABR只向区域内发布一条缺省路由的Inter-Area-Prefix-LSA。这种既没有AS-external-LSA，也没有其它Inter-Area-Prefix-LSA、Inter-Area-Router-LSA的Stub区域，又称为Totally Stub区域。

【使用指导】

如果需要在ABR上取消配置no-summary参数，可以通过重新执行stub命令覆盖之前配置即可。

如果要将一个区域配置成Stub区域，则该区域中的所有路由器都必须配置此属性。

【举例】

\# 将OSPFv3区域1设置为Stub区域。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 area 1

Sysname-ospfv3-1-area-0.0.0.1 stub

【相关命令】

l**default****-cost**(OSPFv3 area view)

**OSPFv3 \-- OSPFv3配置命令 \-- stub-router**

------------------------------------------------------------------------

**[stub-router**]命令用来配置当前路由器为Stub路由器。

**[undo stub-router**]命令用来恢复缺省情况。

【命令】

**[stub-router**[ **r-bit** [ **include-stub** \| **on-startup** { *seconds* \| **wait-for-bgp** [ *seconds* ] } ] \*]]

**[stub-router** **max-metric** [ **external-lsa** [ *max-metric-value*  \| **summary-lsa**  *max-metric-value*  \| **include-stub** \| **on-startup** { *seconds* \| **wait-for-bgp**  *seconds*  } ] \*]]

**[undo stub-router**]

【缺省情况】

当前路由器没有被配置为Stub路由器。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[r-bit**]：路由器发布的Type-1 LSA中，options域的R-bit将清除。

**[max-metric**]：路由器发布的Type-1 LSA的链路度量值将设置为最大值65535。

**[external-lsa ***max-metric-value*]：路由器发布的外部LSA链路度量值。*max-metric-value*表示链路度量值，取值范围为1～16777215，缺省值为16711680。

**[summary-lsa*** max-metric-value*]：路由器发布的Type-3 LSA和Type-4 LSA链路度量值。*max-metric-value*表示链路度量值，取值范围为1～16777215，缺省值为16711680。

**[include-stub**]：路由器发布的引用Type-1 LSA的Type-9 LSA中，链路度量值将设置为最大值65535。

**[on-startup*** seconds*]：在路由器重启期间，路由器做为Stub路由器。*seconds*表示超时时间，取值范围为5～86400，单位为秒。

**[wait-for-bgp*** seconds*]：在路由器重启后，等待BGP路由收敛期间，路由器做为Stub路由器。*seconds*表示超时时间，取值范围为5～86400，单位为秒，缺省值为600秒。

【使用指导】

将当前路由器配置为Stub路由器的功能，可通过R-bit和max-metric两种模式来实现：

·R-bit模式：通过清除该路由器发布Type-1 LSA中options域的R-bit，使其他路由器只能计算到该路由器但是不会通过该路由器来转发数据。

·max-metric模式：该路由器发布的Type-1 LSA的链路度量值将设为最大值65535，这样其邻居计算出这条路由的开销就会很大，如果邻居上有到这个目的地址开销更小的路由，则数据不会通过这个Stub路由器转发。

【举例】

\# 配置当前路由器为Stub路由器。

\<Sysname\> system-view

Sysname ospfv3 100

Sysname-ospfv3-100 stub-router r-bit

**OSPFv3 \-- OSPFv3配置命令 \-- transmit-pacing**

------------------------------------------------------------------------

**[transmit-pacing**]用来配置接口发送LSU报文的时间间隔和一次发送LSU报文的最大个数。

**[undo transmit-pacing**]命令用来恢复缺省情况。

【命令】

**[transmit-pacing** **interval** *interval* **count** *count*]

**[undo** **transmit-pacing**]

【缺省情况】

接口发送LSU报文的时间间隔为20毫秒，一次最多发送3个LSU报文。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval** *interval*]：接口发送LSU报文的时间间隔，*interval*的取值范围为10～1000，单位为毫秒。当路由器上使能OSPFv3功能的接口数比较多时，建议增大该值，以控制路由器每秒钟发送LSU报文的总数。

**[count** *count*]：接口一次发送LSU报文的最大个数，*count*的取值范围为1～200。当路由器上使能OSPFv3功能的接口数比较多时，建议减小该值，以控制路由器每秒钟发送LSU报文的总数。

【举例】

\# 配置OSPFv3进程1的所有接口发送LSU报文的时间间隔为30毫秒，一次最多发送10个LSU报文。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 transmit-pacing interval 30 count 10

**OSPFv3 \-- OSPFv3配置命令 \-- vlink-peer (OSPFv3 area view)**

------------------------------------------------------------------------

**[vlink-peer**]命令用来创建并配置一条虚连接。

**[undo vlink-peer**]命令用来删除一条已有的虚连接。

【命令】

**[vlink-peer ***router-id*[ [ **dead** *seconds* \| **hello** *seconds* \| **instance** *instance-id* \| **ipsec-profile** *profile-name* \| **retransmit** *seconds* \| **trans-delay** *seconds* ] \*]]

**[undo vlink-peer ***router-id*[ [ **dead** \| **hello** \| **ipsec-profile** \| **retransmit** \| **trans-delay** ] \*]]

【缺省情况】

没有虚连接。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[router-id*]：虚连接邻居的路由器ID。

**[dead ***seconds*]：失效时间间隔，取值范围为1～32768，单位为秒，缺省值为40秒。该值必须和与其建立虚连接路由器的**dead** *seconds*值相等，并至少为**hello** *seconds*值的4倍。

**[hello ***seconds*]：接口发送Hello报文的时间间隔，取值范围为1～8192，单位为秒，缺省值为10秒。该值必须和与其建立虚连接路由器上的hello seconds值相等。

**[instance*** instance-id*]：设置虚连接的实例ID，取值范围为0～255，缺省值为0。

**[ipsec-profile*** profile-name*]：应用IPsec安全框架。*profile-name*为IPsec安全框架名称，为1～63个字符的字符串，不区分大小写。

**[retransmit ***seconds*]：接口重传LSA报文的时间间隔，取值范围为1～3600，单位为秒，缺省值为5秒。

**[trans-delay*** seconds*]：接口延迟发送LSA报文的时间间隔，取值范围为1～3600，单位为秒，缺省值为1秒。

【使用指导】

对于没有和骨干区域直接相连的非骨干区域，或者不连续的骨干区域来说，可以使用**vlink-pee**r命令建立逻辑上的连通性。在某种程度上，可以将虚连接看作一个普通的使能了OSPFv3的接口，因为在其上配置的**hello**、**dead**、**retransmit**和**trans-delay**等参数的原理是类似的。

各参数取值规则如下：

l**hello**值越小，发现网络变化的速度越快，消耗的网络资源也就越多**。**

l不能将**retransmit**值设置的太小，否则将会引起不必要的重传。网络速度相对较慢的时候应把该值设的更大一些。

l设置**trans-delay**值时必须考虑接口的发送延迟。

虚连接的两端必须是ABR，**vlink-peer**命令必须在两端同时配置才可生效。

IPsec安全框架的具体情况请参见"安全配置指导"中的"IPsec"。

【举例】

\# 创建一条到10.10.0.3的虚连接。

\<Sysname\> system-view

Sysname ospfv3 1

Sysname-ospfv3-1 area 1

Sysname-ospfv3-1-area-0.0.0.1 vlink-peer 10.10.0.3

【相关命令】

l**display ospfv3 vlink**

