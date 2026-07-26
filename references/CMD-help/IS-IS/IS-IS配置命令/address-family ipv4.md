
**IS-IS \-- IS-IS配置命令 \-- address-family ipv4**

------------------------------------------------------------------------

**[address-family ipv4**]命令用来创建并进入IS-IS IPv4地址族视图。

**[undo address-family ipv4**]命令用来删除IS-IS IPv4地址族视图。

【命令】

**[address-family** **ipv4** [ **unicast** ]]

**[undo address-family** **ipv4** [ **unicast** ]]

【缺省情况】

没有创建IS-IS IPv4地址族视图。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[unicast**]：表示单播地址族。缺省为单播地址族。

【举例】

\# 创建并进入IS-IS IPv4单播地址族视图。

\<Sysname\> system-view

Sysname isis 100

Sysname-isis-100 address-family ipv4

Sysname-isis-100-ipv4

**IS-IS \-- IS-IS配置命令 \-- area-authentication send-only**

------------------------------------------------------------------------

**[area-authentication send-only**]命令用来配置对收到的Level-1报文（包括LSP、CSNP、PSNP）忽略认证信息检查。

**[undo area-authentication send-only**]命令用来取消该配置。

【命令】

**[area-authentication send-only**]

**[undo area-authentication send-only**]

【缺省情况】

如果配置了区域验证方式和验证密码，对收到的报文执行认证信息检查。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置区域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的Level-1报文（包括LSP、CSNP、PSNP）中，并对收到的Level-1报文进行验证密码的检查。当需要更改密码时由于密码不匹配可能导致业务发生中断。通过命令配置对收到的Level-1报文忽略认证信息检查可保证业务不中断，报文正常接收。

【举例】

\# 对收到报文忽略认证信息检查。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 area-authentication send-only

【相关命令】

·**area-authentication-mode**

·**domain-authentication send-only**

·**isis authentication send-only**

**IS-IS \-- IS-IS配置命令 \-- area-authentication-mode**

------------------------------------------------------------------------

**[area-authentication-mode**]命令用来配置区域验证方式和验证密码。

**[undo area-authentication-mode**]命令用来恢复缺省情况。

【命令】

**[area-authentication-mode **[{ **gca** *key-id* { **hmac-sha-1** \| **hmac-sha-224** \| **hmac-sha-256** \| **hmac-sha-384** \| **hmac-sha-512** } \| **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* } [ **ip** \| **osi** ]]]

**[undo** **area-authentication-mode**]

【缺省情况】

系统没有配置区域验证方式和验证密码。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gca**]：GCA验证模式（Generic Cryptographic Authentication）。

*[key-id*]：唯一标识一个认证项（SA），取值范围为1～65535。发送方将Key ID放入认证TLV中，接收方根据报文中提取的Key ID选择SA对报文进行认证。

**[hmac-sha-1**]：支持HMAC-SHA-1算法。

**[hmac-sha-224**]：支持HMAC-SHA-224算法。

**[hmac-sha-256**]：支持HMAC-SHA-256算法。

**[hmac-sha-384**]：支持HMAC-SHA-384算法。

**[hmac-sha-512**]：支持HMAC-SHA-512算法。

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，为33～53个字符的字符串，区分大小写。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，为1～16个字符的字符串，区分大小写。

**[ip**]：检查LSP中IP的相应字段的配置内容。

**[osi**]：检查LSP中OSI的相应字段的配置内容。

【使用指导】

配置区域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的Level-1报文（包括LSP、CSNP、PSNP）中，并对收到的Level-1报文进行验证密码的检查。

通过配置区域验证，可防止将从不可信任的路由器学习到的路由信息加入到本地LSDB中。

需要注意的是：

·同一区域内的路由器必须配置相同的验证方式和验证密码。

·如果没有指定**ip**或**osi**参数，将检查LSP中OSI的相应字段的配置内容。

·以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。

·认证密码选用**ip**或**osi**不受实际的网络环境影响。

【举例】

\# 在IS-IS进程1下配置区域采用简单明文验证模式，验证密码为123456。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 area-authentication-mode simple plain 123456

【相关命令】

·**area-authentication send-only**

·**domain-authentication-mode**

·**isis authentication-mode**

**IS-IS \-- IS-IS配置命令 \-- auto-cost enable**

------------------------------------------------------------------------

**[auto-cost enable**]命令用来使能自动计算接口链路开销值功能。

**[undo auto-cost enable**]命令用来关闭自动计算接口链路开销值功能。

【命令】

**[auto-cost enable**]

**[undo auto-cost enable**]

【缺省情况】

自动计算接口链路开销值功能处于关闭状态。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能自动计算接口链路开销值功能后，将根据带宽参考值自动计算接口的链路度量值。当开销值的类型为**wide**或**wide-compatible**时，可以根据公式"开销=（参考值÷带宽）×10"计算接口的链路度量值。当开销值类型为其他类型时，具体情况如下：接口带宽≤10Mbps时，值为60；接口带宽≤100Mbps时，值为50；接口带宽≤155Mbps时，值为40；接口带宽≤622Mbps时，值为30；接口带宽≤2500Mbps时，值为20；接口带宽\>2500Mbps时，值为10。

【举例】

\# 使能IS-IS进程1的自动计算接口链路开销值功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 auto-cost enable

【相关命令】

·**bandwidth-reference**

·**cost-style**

·**isis cost**

**IS-IS \-- IS-IS配置命令 \-- bandwidth-reference**

------------------------------------------------------------------------

**[bandwidth-reference**]命令用来配置IS-IS自动计算链路开销值时依据的带宽参考值。

**[undo** **bandwidth-reference**]命令用来恢复缺省情况。

【命令】

**[bandwidth-reference** *value*]

**[undo bandwidth-reference**]

【缺省情况】

IS-IS自动计算链路度量值时依据的带宽参考值为100Mbps。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：带宽参考值，取值范围为1～2147483648，单位为Mbps。

【举例】

\# 配置IS-IS进程1的带宽参考值为200Mbps。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 bandwidth-reference 200

【相关命令】

·**auto-cost enable**

·**isis cost**

**IS-IS \-- IS-IS配置命令 \-- circuit-cost**

------------------------------------------------------------------------

**[circuit-cost**]命令用来全局配置IS-IS的链路开销值。

**[undo circuit-cost**]命令用来取消该配置。

【命令】

**[circuit-cost**[ *value* [ **level-1** \| **level-2** ]]]

**[undo circuit-cost**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

没有全局配置IS-IS的链路开销值。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：链路开销值，当指定的路径开销值类型不同时，取值范围也不同：

·当指定的路径开销值类型为**narrow**、**narrow-compatibl**e或**compatible**时，取值范围为0～63。

·当指定的路径开销值类型为**wide**或**wide-compatible**时，取值范围为0～16777215。

**[level-1**]：配置在计算Level-1路由时使用的链路开销值。

**[level-2**]：配置在计算Level-2路由时使用的链路开销值。

【使用指导】

如果不指定级别，将同时配置计算Level-1和Level-2路由时使用的链路开销值。

【举例】

\# 全局配置IS-IS进程1下所有接口在计算Level-1路由时的链路开销值为11。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 circuit-cost 11 level-1

【相关命令】

·**cost-style**

·**isis cost**

**IS-IS \-- IS-IS配置命令 \-- cost-style**

------------------------------------------------------------------------

**[cost-style**]命令用来配置IS-IS开销值的类型，即IS-IS接收和发送的报文中到达目的地路径开销值的类型。

**[undo cost-style**]命令用来恢复缺省情况。

【命令】

**[cost-style**[ { **narrow** \| **wide** \| **wide-compatible** \| { **compatible** \| **narrow-compatible** } [ **relax-spf-limit** ] }]]

**[undo cost-style**]

【缺省情况】

只接收和发送采用**narrow**方式表示路径开销值的报文。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[narrow**]：表示只可以接收和发送采用**narrow**方式（取值范围为0～63）表示到达目的地路径开销的报文。

**[wide**]：表示只可以接收和发送采用**wide**方式（取值范围为0～16777215）表示到达目的地路径开销的报文。

**[compatible**]：表示可以接收和发送采用**narrow**和**wide**方式表示到达目的地路径开销的报文。

**[narrow-compatible**]：表示可以接收采用**narrow**和**wide**方式表示到达目的地路径开销的报文，却只能发送采用**narrow**方式表示到达目的地路径开销的报文。

**[wide-compatible**]：表示可以接收采用**narrow**和**wide**方式表示到达目的地路径开销的报文，却只能发送采用**wide**方式表示到达目的地路径开销的报文。

**[relax-spf-limit**]：表示允许接收到达目的地路径开销值大于1023的报文。如果不指定该参数，则在收到开销值大于1023的报文时，将丢弃。只有当指定了**compatible**或**narrow-compatible**时该参数可选。

【举例】

\# 配置路由器可以接收采用**narrow**或**wide**方式表示路由开销值的报文，却只能发送采用**narrow**方式表示路由开销值的报文。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 cost-style narrow-compatible

【相关命令】

·**circuit-cost**

·**isis cost**

**IS-IS \-- IS-IS配置命令 \-- default-route-advertise**

------------------------------------------------------------------------

**[default-route-advertise**]命令用来配置IS-IS发布Level-1或Level-2级别的缺省路由，即在指定级别的LSP中宣告目的地为0.0.0.0/0的路径信息。

**[undo default-route-advertise**]命令用来恢复缺省情况。

【命令】

**[default-route-advertise **[[ **avoid-learning** \| [ **level-1** \| **level-1-2** \| **level-2** ] \| **route-policy** *route-policy-name* \| **tag** *tag* ] \*]]

**[undo default-route-advertise**]

【缺省情况】

IS-IS不发布Level-1或Level-2级别的缺省路由。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[avoid-learning**]：禁止学习通过LSP发过来的缺省路由和ATT位产生的缺省路由，防止出现环路。

**[level-1**]：发布Level-1级别的缺省路由。

**[level-1-2**]：同时发布Level-1和Level-2级别的缺省路由。

**[level-2**]：发布Level-2级别的缺省路由。

**[route-policy*** route-policy-name*]：指定路由策略名。*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag ***tag*]：配置缺省路由Tag值，取值范围为1～4294967295。

【使用指导】

·如果不指定级别，则默认发布Level-2级别的缺省路由。

·Level-1缺省路由只发布给本区域的其他路由器，Level-2缺省路由发布给所有Level-2和Level-1-2路由器。

·如果在路由策略视图中**apply isis level-1**，则可以在L1 LSP中生成缺省路由；如果在路由策略视图中**apply isis level-2**，则可以在L2 LSP中生成缺省路由；如果在路由策略视图中**apply isis level-1-2**，可以在L1 LSP、L2 LSP中各自生成缺省路由。

·如果在路由策略中指定了Tag值，则本命令中的Tag值不生效。

【举例】

\# 配置IS-IS进程1发布Level-2级别缺省路由。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 default-route-advertise

**IS-IS \-- IS-IS配置命令 \-- display isis**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display isis**]命令用来显示IS-IS的进程信息。

【命令】

**[display isis ** *process-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的进程信息。如果未指定本参数，将显示所有IS-IS进程的进程信息。

【举例】

\# 显示IS-IS的进程信息。

\<Sysname\> display isis

          IS-IS(1) Protocol Information

Network-entity                 : 10.0000.0000.0001.00

IS-level                       : level-1-2

Cost-style                     : Wide

Fast reroute                   : Disabled

Preference                     : 15

LSP-length receive             : 1497

LSP-length originate

    level-1                    : 1497

    level-2                    : 1497

Maximum imported routes        : 1000

Timers

    LSP-max-age                : 1200

    LSP-refresh                : 900

    SPF intervals              : 5 50 200

IPv6 enabled

    Multi-topology             : Standard

    Preference                 : 15

    Maximum imported routes    : 1000

    SPF intervals              : 5 50 200

IPv4-Unicast                   :

  Topology red

    Topology ID                : 6

    Preference                 : 15

    Maximum imported routes    : 1000000

    SPF intervals              : 5 50 200

    Overload status            : Overloaded manually

表1-1 display isis显示信息描述表

字段

描述

Network-entity

网络实体名称

IS-level

路由器类型

Cost-style

开销类型

Fast reroute

是否使能快速重路由功能：

·Disabled：表示未使能

·Auto：表示自动选取备份下一跳

·Route-policy：表示通过路由策略来指定备份下一跳

Preference

路由优先级

LSP-length receive

可以接收LSP的最大长度

LSP-length originate

生成的LSP的最大长度

Maximum imported routes

引入Level1/Level2的IPv4路由/IPv6路由最大条数

Timers

LSP-max-age

LSP的最大生存时间

LSP-refresh

LSP的刷新周期

SPF intervals

SPF的计算时间间隔

IPv6 enabled

IS-IS进程支持IPv6功能

Multi-topology

IS-IS进程支持IPv6单播拓扑

·Standard：IPv6单播拓扑标准模式

·Compatible：IPv6单播拓扑兼容模式

IPv4-Unicast

IS-IS进程支持IPv4单播拓扑

Topology ID

IPv4单播拓扑ID

Topology

IPv4单播拓扑名称

Overload status

·Overloaded manually：手动设置过载标志位

·Overloaded on startup：系统启动时设置过载标志位

·Overloaded on startup waiting for nbr*system-id*up* timeout1*：系统启动后在*timeout1*时长内等待邻居up时设置过载标志位

·Overloaded on startup after nbr*system-id*up* timeout1*：系统启动邻居up后在*timeout1*时长内设置过载标志位

·Overloaded for memory shortage：在内存不足时设置过载标志位

·Overloaded for graceful starting：在GR starting阶段设置过载标志位

**IS-IS \-- IS-IS配置命令 \-- display isis graceful-restart event-log**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display isis graceful-restart event-log**]命令用来显示IS-IS GR日志信息。

【命令】

集中式设备：

**[display isis **]**graceful-restart event-log**

分布式设备－独立运行模式/集中式IRF设备：

**[display isis **]**graceful-restart event-log slot** *slot-number* [ **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display isis **]**graceful-restart event-log chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot**]* slot-number*：显示指定单板的IS-IS GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的IS-IS GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的IS-IS GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示0号板上GR的日志信息。

\<Sysname\> display isis graceful-restart event-log slot 0

IS-IS loginfo :

Jul 18 20:44:33 2012 -Slot=0 Enter HA Block status

Jul 18 10:44:33 2012 -Slot=0 Exit HA Block status

Jul 18 20:46:13 2012 -Slot=0 Process 1 enter GR restarting phase(Initialization).

Jul 18 20:46:13 2012 -Slot=0 Prcoess 1 enter GR phase (LSDB synchronization).

Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (First SPF computation).

Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (Redistribution).

Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (Second SPF computation).

Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (LSP stability).

Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (LSP generation).

Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (Finish).

Jul 18 20:46:40 2012 -Slot=0 Process 1 GR complete.

表1-2 display isis graceful-restart event-log显示信息描述表

字段

描述

GR phase

GR阶段：

·Initialization：初始化

·LSDB synchronization：LSDB同步

·First SPF computation：第一次路由计算

·Redistribution：引入路由

·Second SPF computation：第二次路由计算

·LSP stability：准备生成LSP

·LSP generation：LSP生成和泛洪

·Finish：完成

**IS-IS \-- IS-IS配置命令 \-- display isis graceful-restart status**

------------------------------------------------------------------------

**[display isis graceful-restart** **status**]命令用来显示IS-IS协议的GR状态。

【命令】

**[display isis graceful-restart**[ **status** [ **level-1** \| **level-2** ]  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[level-1**]：表示Level-1级别的IS-IS GR状态。

**[level-2**]：表示Level-2级别的IS-IS GR状态。

*[process-id*]：IS-IS进程号，取值范围为1～65535。如果未指定本参数，将显示所有IS-IS进程的GR状态。

【举例】

\# 显示IS-IS协议的GR状态。

\<Sysname\> display isis graceful-restart status

                        Restart information for IS-IS(1)

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Restart status: COMPLETE

Restart phase: Finish

Restart t1: 3, count 10; Restart t2: 60; Restart t3: 300

SA Bit: supported

                          Level-1 restart information

                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Total number of interfaces: 1

Number of waiting LSPs: 0

                          Level-2 restart information

                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Total number of interfaces: 1

Number of waiting LSPs: 0

表1-3 display isis graceful-restart status命令显示信息描述表

字段

描述

Restart status

当前设备的Restarter状态：

·RESTARTING：保证能进行转发

·STARTING：不能保证转发

·COMPLETE：完成GR

Restart phase

当前设备的Restart阶段：

·Initialization：初始化

·LSDB synchronization：LSDB同步

·First SPF computation：第一次路由计算

·Redistribution：引入路由

·Second SPF computation：第二次路由计算

·LSP stability：准备生成LSP

·LSP generation：LSP生成和泛洪

·Finish：完成

Restart t1

T1定时器的超时值，单位为秒

count

T1定时器的超时次数

Restart t2

T2定时器的超时值，单位为秒

Restart t3

T3定时器的超时值，单位为秒

SA Bit

路由器是否支持SA：

·supported：支持

·Not supported：不支持

Total number of interfaces

当前Level使能的IS-IS接口数

Number of waiting LSPs

GR Restarter从GR Helper进行LSDB同步时，当前Level未完成同步的LSP数目

**IS-IS \-- IS-IS配置命令 \-- display isis interface**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display isis interface**]命令用来显示IS-IS的接口信息。

【命令】

**[display** **isis** **interface** [ [ *interface-type interface-number*   **verbose**  \| **statistics** ]  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。

**[verbose**]：显示接口的详细信息。如果未指定该参数，将显示接口的概要信息。

**[statistics**]：显示接口的统计信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示与指定IS-IS进程相关联接口的信息。如果未指定本参数，将显示所有IS-IS进程的接口信息。

【举例】

\# 显示使能IS-IS功能接口的概要信息。

\<Sysname\> display isis interface

                       Interface information for IS-IS(1)

                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Interface:  GigabitEthernet1/0/2

  Index     IPv4.State      IPv6.State     CircuitID   MTU   Type   DIS

  00001     Up              Down           1           1497  L1/L2  No/No

\# 显示使能IS-IS功能接口的详细信息。

\<Sysname\> display isis interface verbose

                       Interface information for IS-IS(1)

                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Interface:  GigabitEthernet1/0/2

  Index     IPv4.State      IPv6.State     CircuitID   MTU   Type   DIS

  00001     Up              Down           1           1497  L1/L2  No/No

  SNPA address                 : 000c-29e8-1bd5

  IP address                   : 192.168.220.10

  Secondary IP address(es)     :

  IPv6 link-local address      :

  Extended circuit ID          : 1

  CSNP timer value             : L1        10   L2        10

  Hello timer value            :           10

  Hello multiplier value       :            3

  LSP timer value              : L12       33

  LSP transmit-Throttle count  : L12        5

  Cost                         : L1       100   L2        100

  IPv6 cost                    : L1        10   L2        10

  Priority                     : L1        64   L2        64

  Retransmit timer value       : L12        5

  LDP state                    : L1      Init   L2      No-LDP

  LDP sync state               : L1      Init   L2    Achieved

MPLS TE status               : L1  Disabled   L2    Disabled

  IPv4 BFD                     : Disabled

  IPv6 BFD                     : Disabled

  FRR LFA backup               : Enabled

  IPv4 prefix-suppression      : Disabled

  IPv6 prefix-suppression      : Disabled

  IPv4 tag                     : 1

  IPv6 tag                     : 4294967295

  IPv4-Unicast                 :

    Topology ipv4_unicast_multopo

      Topology ID              : 6

      Cost                     : L1       444  L2       444

      FRR LFA backup           : Disabled

      Prefix-suppression       : Enabled

      Tag                      : 44444444

表1-4 display isis interface显示信息描述表

字段

描述

Interface

接口类型和接口编号

Index

接口索引

IPv4.State

IPv4状态：Up和Down

IPv6.State

IPv6状态：Up和Down

CircuitID

链路ID

MTU

接口MTU值

Type

接口的链路邻接关系类型

DIS

是否被选举为DIS，"\--"表示不进行DIS选举（P2P网络）

SNPA address

子网连接点地址

IP address

主IP地址

Secondary IP address(es)

从IP地址

IPv6 link-local address

IPv6链路本地地址

Extended circuit ID

扩展链路ID，点对点链路存在该项

CSNP timer value

CSNP报文发送时间间隔

Hello timer value

Hello报文发送时间间隔

Hello multiplier value

Hello报文失效数目

LSP timer value

发送LSP的最小时间间隔

LSP transmit-Throttle count

每次发送LSP的数目

Cost

接口的链路开销值

IPv6 cost

接口的IPv6链路开销值

Priority

DIS优先级

Retransmit timer value

LSP在点到点链路上的重传时间间隔

MPLS TE status

是否使能IS-IS的MPLS TE功能：

·Enabled：表示使能MPLS TE

·Disabled：表示未使能MPLS TE

LDP state

LDP状态：

·Init：表示处于初始化状态，LDP还没有上报状态

·No-LDP：表示未配置LDP

·Not ready：表示未建立LDP会话

·Ready：表示已建立LDP会话

LDP sync state

LDP同步状态：

·Init：表示初始化

·Achieved：表示已同步

·Max cost：表示保持最大开销值

IPv4 BFD

是否使能IS-IS的BFD功能：

·Disabled：表示未使能

·Enabled：表示使能

IPv6 BFD

是否使能IPv6 IS-IS的BFD功能：

·Disabled：表示未使能

·Enabled：表示使能

FRR LFA backup

是否使能LFA计算功能

·Disabled：表示未使能

·Enabled：表示使能

IPv4 prefix-suppression

是否使能IS-IS的前缀抑制功能

·Disabled：表示未使能

·Enabled：表示使能

IPv6 prefix-suppression

是否使能IPv6 IS-IS的前缀抑制功能

·Disabled：表示未使能

·Enabled：表示使能

IPv4 tag

接口IPv4 tag值

IPv6 tag

接口IPv6 tag值

IPv4-Unicast

接口支持的IPv4单播拓扑

Topology

IPv4单播拓扑名称

Topology ID

IPv4单播拓扑ID

\# 显示IS-IS接口的统计信息。

\<Sysname\> display isis interface statistics

                  Interface Statistics information for IS-IS(1)

                  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Type            IPv4 Up/Down           IPv6 Up/Down

  LAN                   1/0                    0/0

  P2P                   0/0                    0/0

表1-5 display isis interface statistics显示信息描述表

字段

描述

Type

接口类型，取值为：

·LAN：表示接口的网络类型为广播

·P2P：表示接口的网络类型为点对点

IPv4 Up

使能IS-IS功能且状态为up的接口数

IPv4 Down

使能IS-IS功能且状态为down的接口数

IPv6 Up

使能IPv6 IS-IS功能且状态为up的接口数

IPv6 Down

使能IPv6 IS-IS功能且状态为down的接口数

**IS-IS \-- IS-IS配置命令 \-- display isis lsdb**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display isis lsdb**]命令用来显示IS-IS的链路状态数据库信息。

【命令】

**[display isis lsdb**[ [ [ **level-1** \| **level-2** ] \| **local** \| [ **lsp-id** *lspid* \| **lsp-name** *lspname* ] \| **verbose** ] \*  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[level-1**]：显示Level-1链路状态数据库。

**[level-2**]：显示Level-2链路状态数据库。

**[local**]：显示当前路由器产生的LSP的信息。

**[lsp-id*** lspid*]：LSP标识，形式为SYSID*.*Pseudonode ID-fragment num，其中，SYSID是产生该LSP的节点或伪节点的SystemID，Pseudonode ID是伪节点ID，fragment num是该LSP的分片号。

**[lsp-name*** lspname*]：LSP名称，形式为Symbolic name.[Pseudo ID-fragment num]。

**[verbose**]：显示链路状态数据库中的LSP的详细信息。如果未指定该参数，将显示链路状态数据库中的LSP的概要信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的链路状态数据库信息。如果未指定本参数，将显示所有IS-IS进程的链路状态数据库信息。

【使用指导】

如果未指定级别，将同时显示Level-1和Level-2的链路状态数据库信息。

【举例】

\# 显示Level-1链路状态数据库的概要信息。

\<Sysname\> display isis lsdb level-1

                        Database information for IS-IS(1)

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                          Level-1 Link State Database

                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSPID                 Seq Num      Checksum      Holdtime      Length  ATT/P/OL

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0000.0000.0001.00-00\* 0x00000087   0xf846        1152          183     0/0/0

0000.0000.0003.00-00  0x00000005   0x4bee        520           177     0/0/0

0000.0000.0003.00-01  0x00000004   0x7245        520           45      0/0/0

0000.0000.0011.00-00  0x0000000b   0xcdf6        815           183     0/0/0

    \*-Self LSP, +-Self LSP(Extended), ATT-Attached, P-Partition, OL-Overload

\# 显示Level-1链路状态数据库的详细信息。

\<Sysname\> display isis lsdb level-1 verbose

                        Database information for IS-IS(1)

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                          Level-1 Link State Database

                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSPID                 Seq Num      Checksum      Holdtime      Length  ATT/P/OL

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0000.0000.0001.00-00\* 0x00000080   0x73f         1185          183     0/0/0

 Source       0000.0000.0001.00

 NLPID        IPv4

 Area address 10

 IPv4 address 192.168.220.10

 MT ID        0000   (-/-)

 MT ID        0002   (-/-)

 MT ID        0006   (-/-)

 +NBR  ID

     0000.0000.0011.00                Cost: 100

     Admin group: 0x00000000

     Physical bandwidth: 12500000 bytes/sec

     Reservable bandwidth: 0 bytes/sec

     Unreserved bandwidth for each TE class:

       TE class  0: 0 bytes/sec             TE class  1: 0 bytes/sec

       TE class  2: 0 bytes/sec             TE class  3: 0 bytes/sec

       TE class  4: 0 bytes/sec             TE class  5: 0 bytes/sec

       TE class  6: 0 bytes/sec             TE class  7: 0 bytes/sec

       TE class  8: 0 bytes/sec             TE class  9: 0 bytes/sec

       TE class 10: 0 bytes/sec             TE class 11: 0 bytes/sec

       TE class 12: 0 bytes/sec             TE class 13: 0 bytes/sec

       TE class 14: 0 bytes/sec             TE class 15: 0 bytes/sec

     TE cost: 10

     Bandwidth constraint model: Prestandard DS-TE RDM

     Bandwidth constraints:

       BC[0      : 0 bytes/sec             BC1      : 0 bytes/sec]

     Neighbor IP address: 192.168.220.30

     Interface IP address: 192.168.220.10

 IPv6 unicast NBR ID

     6464.6464.6464.01                Cost: 10         MT ID: 2

 MT NBR ID

     6464.6464.6464.01                Cost: 10         MT ID: 6

 +IP-Extended

     192.168.220.0   255.255.255.0    Cost: 100

 IPv4 unicast

     1.1.1.1         255.255.255.255  Cost: 0          MT ID: 6

 IPv4 unicast

     10.10.10.0      255.255.255.0    Cost: 10         MT ID: 6

 IPv6 unicast

     1:1:1::1/128                     Cost: 0          MT ID: 2

 IPv6 unicast

     10:10:10::/64                    Cost: 10         MT ID: 2

 Router ID    1.1.1.1

0000.0000.0003.00-00  0x00000005   0x4bee        887           177     0/0/0

 Source       0000.0000.0003.00

 NLPID        IPv4

 Area address 10

 IPv4 address 10.10.10.10

 IPv4 address 192.168.220.20

 +NBR  ID

     0000.0000.0001.00                Cost: 10

     Admin group: 0x00000000

     Physical bandwidth: 12500000 bytes/sec

     Reservable bandwidth: 0 bytes/sec

     Unreserved bandwidth for each TE class:

       TE class  0: 0 bytes/sec             TE class  1: 0 bytes/sec

       TE class  2: 0 bytes/sec             TE class  3: 0 bytes/sec

       TE class  4: 0 bytes/sec             TE class  5: 0 bytes/sec

       TE class  6: 0 bytes/sec             TE class  7: 0 bytes/sec

       TE class  8: 0 bytes/sec             TE class  9: 0 bytes/sec

       TE class 10: 0 bytes/sec             TE class 11: 0 bytes/sec

       TE class 12: 0 bytes/sec             TE class 13: 0 bytes/sec

       TE class 14: 0 bytes/sec             TE class 15: 0 bytes/sec

     TE cost: 10

     Bandwidth constraint model: Prestandard DS-TE RDM

     Bandwidth constraints:

       BC[0: 0 bytes/sec                   BC1: 0 bytes/sec]

     Interface IP address: 192.168.220.20

     Neighbor IP address: 192.168.220.10

 Router ID    3.3.3.3

0000.0000.0003.00-01  0x00000004   0x7245        887           45      0/0/0

 Source       0000.0000.0003.00

 +IP-Extended

         10.10.10.0      255.255.255.0    Cost: 10

 +IP-Extended

         192.168.220.0   255.255.255.0    Cost: 10

\*-Self LSP, +-Self LSP(Extended), ATT-Attached, P-Partition, OL-Overload

表1-6 display isis lsdb命令显示信息描述表

字段

描述

LSPID

链路状态报文ID

Seq Num

LSP序列号

Checksum

LSP校验和

Holdtime

LSP生存时间，随着时间推移递减

Length

LSP长度

ATT/P/OL

LSP中ATT（Attach bit）、P（Partition bit）、OL（Overload bit）的置位情况，1表示置位，0表示没有置位

Source

LSP生成路由器的System ID

HOST NAME

LSP生成路由器的动态主机名

ORG ID

LSP生成路由器配置的虚拟系统所对应的原始系统ID

NLPID

LSP生成路由器运行的网络层协议

Area address

LSP生成路由器的区域地址

IPv4 address

LSP生成路由器使能IS-IS功能接口的IP地址

IPv6 address

LSP生成路由器使能IPv6 IS-IS功能接口的IPv6地址

MT ID        0000     (-/-)

MT ID        0002     (-/-)

MT ID        0006     (-/-)

LSP生成路由器支持的拓扑信息

·0000表示标准拓扑，0002表示IPv6单播拓扑，0006表示IPv4单播拓扑

·(-/-)，即ATT/OL

NBR ID

LSP生成路由器邻居的System ID

MT NBR ID

LSP生成路由器的IPv4单播拓扑邻居信息

IPv6 unicast NBR ID

LSP生成路由器的IPv6单播邻居信息

Admin group

链路管理组属性

Interface IP address

与对端相连的本地接口IP地址

Neighbor IP address

邻居的接口IP地址

Physical bandwidth

物理带宽

Reservable bandwidth

预留带宽

Unreserved bandwidth for each TE class

每个TE class的可预留带宽

TE class

8个或16个TE class各自的可用带宽

TE cost

TE开销

Bandwidth constraint model

带宽约束模型，取值包括：

·Prestandard DS-TE RDM

·IETF DS-TE RDM

·IETF DS-TE MAM

BC

各个带宽约束值（Prestandard模式支持2个BC，IETF模式支持至多8个BC）

Router ID

路由器ID

IP-Internal

LSP生成路由器的IP内部可达地址和掩码信息

IP-External

LSP生成路由器的IP外部可达地址和掩码信息

IP-Extended

LSP生成路由器的扩展IP可达地址和掩码信息

Cost

开销值

Auth

LSP生成路由器的认证信息

IPV6

LSP生成路由器的IP内部可达IPv6地址和前缀信息

IPV6-Ext

LSP生成路由器的IP外部可达IPv6地址和前缀信息

IPv4 unicast

LSP生成路由器的IPv4单播可达信息

IPv6 unicast

LSP生成路由器的IPv6单播内部可达信息

IPv6 unicast-ext

LSP生成路由器的IPv6单播外部可达信息

**IS-IS \-- IS-IS配置命令 \-- display isis mesh-group**

------------------------------------------------------------------------

**[display isis mesh-group**]命令用来显示IS-IS Mesh-Group的配置信息。

【命令】

**[display**]**isis** **mesh-group** [ *process-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程Mesh-Group的配置信息。如果未指定本参数，将显示所有IS-IS进程Mesh-Group的配置信息。

【举例】

·路由应用

\# 配置路由器上运行IS-IS的Serial2/1/0接口和Serial2/1/1接口属于Mesh-Group 100。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 isis mesh-group 100

Sysname-Serial2/1/0 quit

Sysname interface serial 2/1/1

Sysname-Serial2/1/1 isis mesh-group 100

\# 显示配置的IS-IS Mesh-Group的信息。

Sysname-Serial2/1/1 display isis mesh-group

               Mesh Group information for IS-IS(1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Interface          Status

 Serial2/1/0         Blocked

 Serial2/1/1          100

·交换应用

\# 配置交换机上运行IS-IS的Vlan-interface10接口和Vlan-interface20接口属于Mesh-Group 100。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis mesh-group 100

Sysname-Vlan-interface10 interface vlan-interface 20

Sysname-Vlan-interface20 isis mesh-group 100

\# 显示配置的IS-IS Mesh-Group的信息。

Sysname-Vlan-interface20 display isis mesh-group

                       Mesh Group information for IS-IS(1)

                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Interface          Status

 Vlan10              Blocked

 Vlan20              100

表1-7 display isis mesh-group命令显示信息描述表

字段

描述

Interface

接口名称

Status

接口所属的Mesh-Group/是否配置了接口阻塞

**IS-IS \-- IS-IS配置命令 \-- display isis name-table**

------------------------------------------------------------------------

**[display isis name-table**]命令用来显示系统ID到主机名称的映射关系表。

【命令】

**[display **]**isis name-table ** *process-id*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程系统ID到主机名称的映射关系表。如果未指定本参数，将显示所有IS-IS进程系统ID到主机名称的映射关系表。

【举例】

\# 显示系统ID到主机名称的映射关系表。

\<Sysname\> display isis name-table

                      Name table information for IS-IS(1)

                      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 System ID           Hostname                            Type       Level

 6789.0000.0001      RUTA                                DYNAMIC    Level-1

 6789.0000.0001      RUTA                                DYNAMIC    Level-2

 0000.0000.0041      RUTB                                STATIC     Level-1

 0000.0000.0041      RUTB                                STATIC     Level-2

 6789.0000.0001.01   DIS-A                               DYNAMIC    Level-1

 0000.0000.0041.01   DIS-B                               DYNAMIC    Level-2

表1-8 display isis name-table命令显示信息描述表

字段

描述

System ID

系统ID

Hostname

主机名称

Type

系统ID与主机名称映射关系的生成方式，其中：

·DYNAMIC：表示映射关系是动态生成的

·STATIC：表示映射关系是通过静态配置的

Level

系统ID与主机名称映射关系生效的Level

·Level-1：表示该映射关系在Level-1生效

·Level-2：表示该映射关系在Level-2生效

**IS-IS \-- IS-IS配置命令 \-- display isis non-stop-routing event-log**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display isis non-stop-routing event-log**]命令用来显示IS-IS NSR日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display isis non-stop-routing event-log slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display isis non-stop-routing event-log chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot**]* slot-number*：显示指定单板的IS-IS NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的IS-IS NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的IS-IS NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示IS-IS NSR日志信息。

\<Sysname\> display isis non-stop-routing event-log slot 0

IS-IS loginfo :

Jul 20 08:34:05 2012 -Slot=0 Enter HA Block status

Jul 19 22:34:05 2012 -Slot=0 Exit HA Block status

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Initialization).

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Smooth).

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (First SPF computation).

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Redistribution).

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Second SPF computation).

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (LSP stability).

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (LSP generation).

Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Finish).

Jul 19 22:37:53 2012 -Slot=0 Process 1 NSR complete.

表1-9 display isis graceful-restart event-log显示信息描述表

字段

描述

NSR phase

NSR阶段：

·Initialization：初始化

·Smooth：平滑

·First SPF computation：第一次路由计算

·Redistribution：引入路由

·Second SPF computation：第二次路由计算

·LSP stability：准备生成LSP

·LSP generation：LSP生成和泛洪

·Finish：完成

**IS-IS \-- IS-IS配置命令 \-- display isis non-stop-routing status**

------------------------------------------------------------------------

**[display isis non-stop-routing status**]命令用来显示IS-IS的NSR状态。

【命令】

**[display isis non-stop-routing status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IS-IS的NSR状态。

\<Sysname\> display isis non-stop-routing status

                        Nonstop Routing information for IS-IS(1)

                    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

NSR phase: Finish

表1-10 display isis non-stop-routing status命令显示信息描述表

字段

描述

NSR phase

NSR阶段：

·Initialization：初始化

·Smooth：平滑

·First SPF computation：第一次路由计算

·Redistribution：引入路由

·Second SPF computation：第二次路由计算

·LSP stability：准备生成LSP

·LSP generation：LSP生成和泛洪

·Finish：完成

**IS-IS \-- IS-IS配置命令 \-- display isis peer**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display isis peer**]命令用来显示IS-IS的邻居信息。

【命令】

**[display**]**isis**[ **peer** [ **statistics** \| **verbose** ]  *process-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[statistics**]：显示IS-IS邻居的统计信息。

**[verbose**]：显示IS-IS邻居的详细信息。如果未指定该参数，将显示IS-IS邻居的概要信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的邻居信息。如果未指定本参数，将显示所有IS-IS进程的邻居信息。

【举例】

\# 显示IS-IS邻居的概要信息。

\<Sysname\> display isis peer

                         Peer information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 System Id: 0000.0000.0001

 Interface: GE1/0/2                  Circuit Id:  0000.0000.0001.01

 State: Up     HoldTime:  27s       Type: L1(L1L2)     PRI: 64

 System Id: 0000.0000.0001

 Interface: GE1/0/2                  Circuit Id:  0000.0000.0001.01

 State: Up     HoldTime:  27s       Type: L2(L1L2)     PRI: 64

\# 显示IS-IS邻居的详细信息。

\<Sysname\> display isis peer verbose

                         Peer information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 System ID: 0000.1111.2222

 Interface: GE1/0/2                  Circuit Id:  0000.1111.2222.01

 State: Up     Holdtime:   6s       Type: L1(L1L2)     PRI: 64

 Area address(es): 49

 Peer IP address(es): 12.0.0.2

 Peer local circuit ID: 1

 Peer circuit SNPA address: 000c-293b-c4be

 Uptime: 00:05:07

 Adj protocol:  IPv4

 Adj P2P three-way handshake: No

Graceful Restart capable

   Restarting signal: No

   Suppress adjacency advertisement: No

 Local topology:

   0    2

 Remote topology:

   0    2

 System ID: 0000.0000.0002

 Interface: GE1/0/3                  Circuit Id:  001

 State: Up     HoldTime: 27s        Type: L1L2         PRI: \--

 Area address(es): 49

 Peer IP address(es): 192.168.220.30

 Peer local circuit ID: 1

 Peer circuit SNPA address: 000c-29fd-ed69

 Uptime: 00:05:07

 Adj protocol:  IPv4

 Adj P2P three-way handshake: Yes

   Peer extended circuit ID: 2

Graceful Restart capable

   Restarting signal: No

   Suppress adjacency advertisement: No

表1-11 display isis peer命令显示信息描述表

字段

描述

System Id

邻居的System ID

Interface

与对端相连的本地IS-IS接口

Circuit Id

链路ID

State

链路状态

HoldTime

抑制时间，随着时间推移递减，如果在抑制时间内还没有收到邻居发送的Hello报文，则认为邻居已经失效，如果收到了Hello报文，则抑制时间将重置为初始值

Type

链路关系类型，其中：

·L1：表示与邻居建立的链路类型为Level-1，邻居路由器类型为Level-1

·L2：表示与邻居建立的链路类型为Level-2，邻居路由器类型为Level-2

·L1(L1L2)：表示与邻居建立的链路类型为Level-1，邻居路由器类型为Level-1-2

·L2(L1L2)：表示与邻居建立的链路类型为Level-2，邻居路由器类型为Level-1-2

PRI

邻居接口DIS优先级

Area Address(es)

邻居所在区域地址

Peer IP Address(es)

邻居接口的IP地址

Uptime

邻居关系保持时间

Adj Protocol

邻接协议：IPv4或IPv6

Peer local circuit ID

邻居链路ID

Peer circuit SNPA address

邻居子网连接点地址

Adj P2P three-way handshake

邻居是否支持P2P三次握手

Peer extended circuit ID

邻居接口的扩展链路ID，邻居支持三次握手时存在该项

Graceful Restart capable

GR Helper能力

Restarting signal

RR标记

Suppress adjacency advertisement

SA标记

Local topology

本端接口支持的拓扑列表

Remote topology

邻居接口支持的拓扑列表

\# 显示IS-IS邻居的统计信息。

\<Sysname\> display isis peer statistics

                    Peer Statistics information for IS-IS(1)

                    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Type              IPv4 Up/Init              IPv6 Up/Init

  LAN Level-1             1/0                       0/0

  LAN Level-2             1/0                       0/0

  P2P                     0/0                       0/0

表1-12 display isis peer statistics命令显示信息描述表

字段

描述

Type

邻居类型，取值为：

·LAN Level-1：表示网络类型为广播的Level-1邻居个数

·LAN Level-2：表示网络类型为广播的Level-2邻居个数

·P2P：表示网络类型为点对点的邻居个数

IPv4 Up

状态为up的IPv4邻居个数

IPv4 Init

状态为init的IPv4邻居个数

IPv6 Up

状态为up的IPv6邻居个数

IPv6 Init

状态为init的IPv6邻居个数

**IS-IS \-- IS-IS配置命令 \-- display isis redistribute**

------------------------------------------------------------------------

**[display isis redistribute**]命令用来显示IS-IS引入路由的信息。

【命令】

**[display isis redistribute **[ **ipv4** [ **topology** *topo-name*   *ip-address mask-lengh*    **level-1** \| **level-2** ]  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：显示IS-IS的IPv4引入路由信息。缺省情况下，显示IPv4引入路由信息。

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ip-address mask-lengh*]：显示指定目的IP地址和掩码长度的引入路由。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的IPv4路由信息。

**[level-1**]：显示Level-1的IS-IS路由信息。

**[level-2**]：显示Level-2的IS-IS路由信息。

【使用指导】

如果不指定级别，将同时显示Level-1和Level-2的路由信息。

【举例】

\# 显示IS-IS的IPv4引入路由信息。

\<Sysname\> display isis redistribute 1

                         Route information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                        Level-1 IPv4 Redistribute Table

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Type IPv4 Destination     IntCost    ExtCost    Tag        State

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 D    192.168.30.0/24      0          0                     Active

 D    11.11.11.11/32       0          0

 D    10.10.10.0/24        0          0

 Type: D -Direct, I -ISIS, S -Static, O -OSPF, B -BGP, R --RIP

表1-1 display isis redistribute命令显示信息描述表

字段

描述

Route information for IS-IS(1)

指定IS-IS进程引入路由信息

Level-1 IPv4 Redistribute Table

Level-1的IS-IS IPv4引入路由信息

Level-2  IPv4 Redistribute  Table

Level-2的IS-IS IPv4引入路由信息

Type

引入的路由类型，包括直连、IS-IS、静态、OSPF、BGP、RIP

IPV4 Destination

IPv4目的地址

IntCost

路由内部Cost

ExtCost

路由外部Cost

Tag

引入路由发布时的Tag值

State

引入路由是否为最终生效路由

**IS-IS \-- IS-IS配置命令 \-- display isis route**

------------------------------------------------------------------------

**[display isis route**]命令用来显示IS-IS的IPv4路由信息。

【命令】

**[display isis route** [ **ipv4** [ **topology** *topo-name*  \*ip-address mask-length*    [ **level-1** \| **level-2** ] \| **verbose** ] \*  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：显示IS-IS的IPv4路由信息。缺省情况下，显示IPv4路由信息。

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ip-address mask-length*]：显示指定目的IP地址和掩码长度的路由。*mask-length*取值范围为0～32。

**[verbose**]：显示IS-IS详细的IPv4路由信息。如果未指定该参数，将显示路由信息的概要信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的IPv4路由信息。

**[level-1**]：显示Level-1的IS-IS路由信息。

**[level-2**]：显示Level-2的IS-IS路由信息。

【使用指导】

·如果未指定级别，将同时显示Level-1和Level-2的路由信息。

·如果未指定IS-IS进程号，将显示所有IS-IS进程的路由信息。

【举例】

\# 显示IS-IS的IPv4路由信息。

\<Sysname\> display isis route

                         Route information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                         Level-1 IPv4 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPv4 Destination     IntCost    ExtCost ExitInterface   NextHop         Flags

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 8.8.8.0/24           10         NULL    GE1/0/2         Direct          D/L/-

 9.9.9.0/24           20         NULL    GE1/0/2         8.8.8.5         R/L/-

      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

                         Level-2 IPv4 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPv4 Destination     IntCost    ExtCost ExitInterface   NextHop         Flags

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 8.8.8.0/24           10         NULL                                    D/L/-

      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

表1-13 display isis route命令显示信息描述表

字段

描述

Route information for IS-IS(1)

指定IS-IS进程路由信息

Level-1 IPv4 Forwarding Table

Level-1的IS-IS IPv4路由信息

Level-2 IPv4 Forwarding Table

Level-2的IS-IS IPv4路由信息

IPv4 Destination

IPv4目的地址

IntCost

路由内部Cost

ExtCost

路由外部Cost

ExitInterface

出接口

NextHop

下一跳

Flags

路由状态标志

·D：直连路由

·R：该路由是否已放到路由表中

·L：是否已经通过LSP发布

·U：路由渗透状态标识。设置为"Up"表示可以避免由L2发送到L1的LSP又返回给L2，设置为"Down"表示不可以

\# 显示IS-IS的IPv4路由详细信息。

\<Sysname\> display isis route verbose

                         Route information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                         Level-1 IPv4 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPV4 Dest : 8.8.8.0/24          Int. Cost : 10               Ext. Cost : NULL

 Admin Tag : -                   Src Count : 2                Flag      : D/L/-

 NextHop   :                     Interface :                  ExitIndex :

    Direct                             GE1/0/2                     0x00000000

 Nib ID    : 0x0

 IPV4 Dest : 9.9.9.0/24          Int. Cost : 20               Ext. Cost : NULL

 Admin Tag : -                   Src Count : 1                Flag      : R/L/-

 NextHop   :                     Interface :                  ExitIndex :

    8.8.8.5                            GE1/0/2                     0x00000003

 Nib ID    : 0x0

      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

                         Level-2 IPv4 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPV4 Dest : 8.8.8.0/24          Int. Cost : 10               Ext. Cost : NULL

 Admin Tag : -                   Src Count : 2                Flag      : D/L/-

      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

表1-14 display isis route verbose命令显示信息描述表

字段

描述

Route information for IS-IS(1)

指定IS-IS进程的IPv4路由信息

Level-1 IPv4 Forwarding Table

Level-1的IS-IS IPv4路由信息

Level-2 IPv4 Forwarding Table

Level-2的IS-IS IPv4路由信息

IPV4 Dest

IPv4目的地址

Int. Cost

路由内部Cost

Ext. Cost

路由外部Cost

Admin Tag

Tag值

Src Count

发布源个数

Flag

路由状态标志

·R：该路由是否已放到路由表中

·L：是否已经通过LSP发布

·U：路由渗透状态标识。设置为"Up"表示可以避免由L2发送到L1的LSP又返回给L2，设置为"Down"表示不可以

Next Hop

下一跳

Interface

出接口

ExitIndex

出接口索引

Nib ID

路由管理分配的ID，即下一跳索引

**IS-IS \-- IS-IS配置命令 \-- display isis spf-tree**

------------------------------------------------------------------------

**[display isis spf-tree**]命令用来显示IS-IS的IPv4拓扑信息。

【命令】

**[display isis spf-tree **[ **ipv4** [ **topology** *topo-name*    [ **level-1** \| **level-2** ] \| **verbose** ] \*  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：显示IS-IS的IPv4拓扑信息。如果未指定该参数，显示IPv4拓扑信息。

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[level-1**]：显示Level-1的IS-IS拓扑信息。如果未指定级别，将同时显示Level-1和Level-2的拓扑信息。

**[level-2**]：显示Level-2的IS-IS拓扑信息。如果未指定级别，将同时显示Level-1和Level-2的拓扑信息。

**[verbose**]：显示IS-IS的详细拓扑信息。如果未指定该参数，显示概要拓扑信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的拓扑信息。如果未指定IS-IS进程号，将显示所有IS-IS进程的拓扑信息。

【举例】

\# 显示IS-IS的IPv4拓扑信息。

\<Sysname\> display isis spf-tree

                        Shortest Path Tree for IS-IS(1)

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      Flags: S-Node is on SPF tree       T-Node is on tent list

             O-Node is overload          R-Node is directly reachable

             I-Node or Link is isolated  D-Node or Link is to be deleted

             C-Neighbor is child         P-Neighbor is parent

             V-Link is involved          N-Link is a new path

             L-Link is on change list    U-Protocol usage is changed

             H-Nexthop is changed

                           Level-1 Shortest Path Tree

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SpfNode            NodeFlag       SpfLink            LinkCost LinkFlag

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0000.0000.0032.00  S/-/-/-/-/-

                               \--\>0000.0000.0032.01  10       -/-/C/-/-/-/-/-/-

                               \--\>0000.0000.0064.00  10       -/-/C/-/-/-/-/-/-

0000.0000.0032.01  S/-/-/R/-/-

                               \--\>0000.0000.0064.00  0        -/-/C/-/-/-/-/-/-

                               \--\>0000.0000.0032.00  0        -/-/-/P/-/-/-/-/-

0000.0000.0064.00  S/-/-/R/-/-

                               \--\>0000.0000.0032.00  10       -/-/-/P/-/-/-/-/-

                               \--\>0000.0000.0032.01  10       -/-/-/P/-/-/-/-/-

                           Level-2 Shortest Path Tree

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SpfNode            NodeFlag       SpfLink            LinkCost LinkFlag

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0000.0000.0032.00  S/-/-/-/-/-

                               \--\>0000.0000.0032.01  10       -/-/C/-/-/-/-/-/-

                               \--\>0000.0000.0064.00  10       -/-/C/-/-/-/-/-/-

0000.0000.0032.01  S/-/-/R/-/-

                               \--\>0000.0000.0064.00  0        -/-/C/-/-/-/-/-/-

                               \--\>0000.0000.0032.00  0        -/-/-/P/-/-/-/-/-

0000.0000.0064.00  S/-/-/R/-/-

                               \--\>0000.0000.0032.00  10       -/-/-/P/-/-/-/-/-

                               \--\>0000.0000.0032.01  10       -/-/-/P/-/-/-/-/-

\# 显示IS-IS的IPv4详细拓扑信息。

\<Sysname\> display isis spf-tree verbose

                        Shortest Path Tree for IS-IS(1)

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

      Flags: S-Node is on SPF tree       T-Node is on tent list

             O-Node is overload          R-Node is directly reachable

             I-Node or Link is isolated  D-Node or Link is to be deleted

             C-Neighbor is child         P-Neighbor is parent

             V-Link is involved          N-Link is a new path

             L-Link is on change list    U-Protocol usage is changed

             H-Nexthop is changed

                           Level-1 Shortest Path Tree

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 SpfNode        : 0000.0000.0001.00

 Distance       : 0

 TE distance    : 0

 NodeFlag       : S/-/-/-/-/-

 RelayNibID     : 0x0

 TE tunnel count: 0

 Nexthop count  : 0

 SpfLink count  : 1

 \--\>0000.0000.0004.04

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Adjacent       Interface: N/A

        Cost: 10             Nexthop  : N/A

 SpfNode        : 0000.0000.0004.00

 Distance       : 10

 Te Distance    : 10

 NodeFlag       : S/-/-/-/-/-

 RelayNibID     : 0x14000000

 TE tunnel count: 1

     Destination: 4.4.4.4                  Interface  : Tun0

     TE cost    : 10                       Final cost : 10

     Add nexthop: YES                      Add TLV    : YES

 Nexthop count  : 2

     Neighbor   : 0000.0000.0004.00        Interface  : Tun0

     Nexthop    : 4.4.4.4

     BkNeighbor : N/A                      BkInterface: N/A

     BkNexthop  : N/A

     Neighbor   : 0000.0000.0004.00        Interface  : Vlan50

     Nexthop    : 1.1.1.3

     BkNeighbor : N/A                      BkInterface: N/A

     BkNexthop  : N/A

 SpfLink count  : 1

 \--\>0000.0000.0004.04

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/-/P/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Remote         Interface: N/A

        Cost: 10             Nexthop  : N/A

        AdvMtID: 0

 SpfNode        : 0000.0000.0004.04

 Distance       : 10

 TE distance    : 10

 NodeFlag       : S/-/-/R/-/-

 RelayNibID     : 0x14000001

 TE tunnel count: 0

 Nexthop count  : 0

 SpfLink count  : 2

 \--\>0000.0000.0001.00

    LinkCost    : 0

    LinkNewCost : 0

    LinkFlag    : -/-/-/P/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Remote         Interface: N/A

        Cost: 0              Nexthop  : N/A

 \--\>0000.0000.0004.00

    LinkCost    : 0

    LinkNewCost : 0

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Remote         Interface: Vlan50

        Cost: 0              Nexthop  : 1.1.1.3

                           Level-2 Shortest Path Tree

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 SpfNode        : 0000.0000.0001.00

 Distance       : 0

 TE distance    : 0

 NodeFlag       : S/-/-/-/-/-

 RelayNibID     : 0x0

 TE tunnel count: 0

 Nexthop count  : 0

 SpfLink count  : 1

 \--\>0000.0000.0004.04

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Adjacent       Interface: N/A

        Cost: 10             Nexthop  : N/A

 SpfNode        : 0000.0000.0004.00

 Distance       : 10

 TE distance    : 10

 NodeFlag       : S/-/-/-/-/-

 RelayNibID     : 0x0

 TE tunnel count: 1

     Destination: 4.4.4.4                  Interface  : Tun0

     TE cost    : 10                       Final cost : 10

     Add nexthop: YES                      Add TLV    : YES

 Nexthop count  : 2

     Neighbor   : 0000.0000.0004.00        Interface  : Tun0

     Nexthop    : 4.4.4.4

     BkNeighbor : N/A                      BkInterface: N/A

     BkNexthop  : N/A

     Neighbor   : 0000.0000.0004.00        Interface  : Vlan50

     Nexthop    : 1.1.1.3

     BkNeighbor : N/A                      BkInterface: N/A

     BkNexthop  : N/A

 SpfLink count  : 1

 \--\>0000.0000.0004.04

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/-/P/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Remote         Interface: N/A

        Cost: 10             Nexthop  : N/A

        AdvMtID: 0

 SpfNode        : 0000.0000.0004.04

 Distance       : 10

 TE distance    : 10

 NodeFlag       : S/-/-/R/-/-

 RelayNibID     : 0x0

 TE tunnel count: 0

 Nexthop count  : 0

 SpfLink count  : 2

 \--\>0000.0000.0001.00

    LinkCost    : 0

    LinkNewCost : 0

    LinkFlag    : -/-/-/P/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Remote         Interface: N/A

        Cost: 0              Nexthop  : N/A

 \--\>0000.0000.0004.00

    LinkCost    : 0

    LinkNewCost : 0

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type: Remote         Interface: Vlan50

        Cost: 0              Nexthop  : 1.1.1.3

表1-15 display isis spf-tree命令显示信息描述表

字段

描述

SpfNode

拓扑节点ID

Distance

根节点到该节点的最短距离

TE distance

根节点到该节点的最短距离（包含隧道Link），如果未配置隧道，则与Distance值相等

NodeFlag

节点状态标记：

·S：节点在SPF树上

·T：节点在候选列表上

·O：节点处于OverLoad

·R：节点是直连的

·I：孤立节点

·D：节点待删除

RelayNibID

节点的迭代下一跳ID

TE tunnel count

Destination为该节点的隧道条数

Destination

目的路由器

TE cost

TE隧道配置的IGP开销值

Final cost

TE隧道的最终生效开销值

Nexthop count

节点的下一跳个数

Nexthop

节点的主用下一跳地址/链路发布源下一跳地址

AdvMtID

从哪个拓扑学到的路由：

·0：标准拓扑ID

·6-4094：其它拓扑ID

Interface

节点的主用下一跳出接口/链路发布源下一跳出接口

BkNexthop

节点的备份下一跳地址

BkInterface

节点的备份下一跳出接口

Neighbor

节点主用下一跳邻居节点ID

BkNeighbor

节点备份下一跳邻居节点ID

SpfLink

拓扑链路

SpfLink count

拓扑链路个数

LinkCost

链路开销

LinkNewCost

链路新开销

LinkFlag

链路状态标记：

·I：孤立链路

·D：链路待删除

·C：目的节点是源节点的子节点

·P：目的节点是源节点的父节点

·V：链路受到影响

·N：新增链路

·L：链路在变化链表上

·U：链路协议类型发生变化

·H：链表下一跳发生变化

LinkSrcCnt

链路发布源个数

Type

链路发布源类型：

·Adjacent：本地邻居维护产生

·Remote：其它节点LSP产生

Cost

链路发布源开销

**IS-IS \-- IS-IS配置命令 \-- display isis statistics**

------------------------------------------------------------------------

**[display isis statistics**]命令用来显示IS-IS的统计信息。

【命令】

**[display **]**isis statistics **[ **ipv4** [ **topology** *topo-name*    **level-1** \| **level-1-2** \| **level-2** ]  *process-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：显示IS-IS的IPv4统计信息。如果未指定该参数，显示IPv4拓扑信息。

**[topology** *topo-name*]：显示指定拓扑的信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；**base**为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[level-1**]：显示IS-IS Level-1的统计信息。

**[level-1-2**]：显示IS-IS Level-1-2的统计信息。

**[level-2**]：显示IS-IS Level-2的统计信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的统计信息。

【使用指导】

·如果未指定级别，将同时显示Level-1和Level-2的统计信息。

·如果未指定IS-IS进程号，将显示所有IS-IS进程的统计信息。

【举例】

\# 显示IS-IS的统计信息。

\<Sysname\> display isis statistics

                       Statistics information for IS-IS(1)

                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                               Level-1 Statistics

                               \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

MTR(base)

Learnt routes information:

         Total IPv4 Learnt Routes in IPv4 Routing Table: 1

Imported routes information:

         IPv4 Imported Routes:

                         Static: 0       Direct: 0

                         ISIS:   0       BGP:    0

                         RIP:    0       OSPF:   0

                         Total Number:   0

MTR(base)

Learnt routes information:

         Total IPv6 Learnt Routes in IPv6 Routing Table: 0

Imported routes information:

         IPv6 Imported Routes:

                         Static: 0       Direct: 0

                         ISISv6: 0       BGP4+:  0

                         RIPng:  0       OSPFv3: 0

                         Total Number:   0

Lsp information:

                  LSP Source ID:          No. of used LSPs

                  7777.8888.1111                  001

                               Level-2 Statistics

                               \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

MTR(base)

Learnt routes information:

         Total IPv4 Learnt Routes in IPv4 Routing Table: 0

Imported routes information:

         IPv4 Imported Routes:

                         Static: 0       Direct: 0

                         ISIS:   0       BGP:    0

                         RIP:    0       OSPF:   0

                         Total Number:   0

MTR(base)

Learnt routes information:

         Total IPv6 Learnt Routes in IPv6 Routing Table: 0

Imported routes information:

         IPv6 Imported Routes:

                         Static: 0       Direct: 0

                         ISISv6: 0       BGP4+:  0

                         RIPng:  0       OSPFv3: 0

                         Total Number:   0

Lsp information:

                  LSP Source ID:          No. of used LSPs

                  7777.8888.1111                  001

表1-16 display isis statistics命令显示信息描述表

字段

描述

Statistics information for IS-IS(*processid*)

指定IS-IS进程的统计信息

Level-1 Statistics

Level-1路由统计信息

Level-2 Statistics

Level-2路由统计信息

MTR(*topo-name*)

指定某个拓扑，拓扑名为base则为公网拓扑

Learnt routes information

学习到的路由信息：

Total IPv4 Learnt Routes in IPv4 Routing Table：学习到的IPv4路由信息的总数

Total IPv6 Learnt Routes in IPv6 Routing Table：学习到的IPv6路由信息的总数

Imported routes information

IPv4 Imported Routes

引入IPv4路由数量：

·Static：引入的IPv4静态路由数量

·Direct：引入的IPv4直连路由数量

·ISIS：从其它IS-IS进程引入的路由数量

·BGP：从BGP引入的路由数量

·RIP：从RIP引入的路由数量

·OSPF：从OSPF引入的路由数量

IPv6 Imported Routes

引入IPv6路由数量：

·Static：引入的IPv6静态路由数量

·Direct：引入的IPv6直连路由数量

·ISISv6：从其它IS-ISv6进程引入的路由数量

·BGP4+：从BGP4+引入的路由数量

·RIPng：从RIPng引入的路由数量

·OSPFv3：从OSPFv3引入的路由数量

Lsp information

LSP信息：

·LSP Source ID：本地生成的LSP的System ID

·No. of used LSPs：本地生成的LSP已使用的分片数量

**IS-IS \-- IS-IS配置命令 \-- display osi**

------------------------------------------------------------------------

**[display osi**]命令用来显示OSI连接的信息，包括socket的状态、选项等，以及接收报文时需要匹配的入接口和组播MAC地址信息。

【命令】

集中式设备：

display osi

分布式设备－独立运行模式/集中式IRF设备：

display osi slot slot-number{.commandparameterChar} [cpu *cpu-number*  ]

分布式设备－IRF模式：

**[display osi ** **chassis** ]chassis-number{.commandparameterChar}** slot**slot-number{.commandparameterChar} [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的OSI连接的信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号[，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的连接信息。（分布式－独立运行模式）]

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备的OSI连接的信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备的连接信息。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备的OSI连接的信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX的连接信息。（集中式设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备上指定单板的OSI连接的信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有成员设备所有单板的连接信息。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的OSI连接的信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有OSI连接的信息。

\<Sysname\> display osi

Total OSI socket number: 2

 Location: chassis 1 slot 0 cpu 0

 Creator: isisd[1539]

 State: N/A

 Options: SO_FILTER

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 1048576 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 262144 / 512 / N/A

 Type: 2

 Enabled interfaces:

  GigabitEthernet0/0

   MAC address: 0180-c200-0014

 Location: chassis 1 slot 0 cpu 0

 Creator: isisd[1539]

 State: N/A

 Options: SO_FILTER

 Error: 0

 Receiving buffer(cc/hiwat/lowat/state): 0 / 1048576 / 1 / N/A

 Sending buffer(cc/hiwat/lowat/state): 0 / 262144 / 512 / N/A

 Type: 2

 Enabled interfaces:

  GigabitEthernet0/0

   MAC address: 0180-c200-0014

表1-17 display osi命令显示信息描述表

字段

描述

Total OSI socket number

OSI socket的总数

Chassis

设备在IRF中的成员编号

Slot

单板的槽位号

Cpu

CPU编号

Creator

创建socket的任务名称，括号中为创建者的进程号

State

OSI socket无状态，始终显示为N/A

Options

socket的选项，OSI socket支持以下两种：

·SO_FILTER：设置了过滤选项

·N/A：没有设置选项

Error

影响socket连接的错误

Receiving buffer(cc/hiwat/lowat/state)

接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态

Sending buffer(cc/hiwat/lowat/state)

发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态

Type

IS-IS使用的socket类型为2，对应无连接的、不可靠的运输层数据包协议

Enabled interfaces

接收报文时需要匹配的入接口和组播MAC地址信息，仅以太链路层接口上收到的报文需要匹配组播MAC地址

**IS-IS \-- IS-IS配置命令 \-- display osi statistics**

------------------------------------------------------------------------

**[display osi statistics**]命令用来显示OSI连接的报文统计信息，包括接收报文、中继转发报文、丢弃报文和发送报文等统计信息。

【命令】

集中式设备：

**[display osi statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display osi statistics** [ **slot** ]slot-number]{.commandparameterChar} [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display osi statistics** [ **chassis** ]chassis-number]{.commandparameterChar} **slot** slot-number{.commandparameterChar} [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的OSI连接的报文统计信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号[，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的报文统计信息之和。（分布式－独立运行模式）]

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备的OSI连接的报文统计信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备的报文统计信息之和。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备/PEX的OSI连接的报文统计信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX的报文统计信息之和。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备上指定单板的OSI连接的报文统计信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有成员设备所有单板的报文统计信息之和。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的OSI连接的报文统计信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的报文统计信息之和。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示OSI连接的报文统计信息。

\<Sysname\> display osi statistics

Received packets:

     Total: 35

     Relay received: 35

     Relay forwarded: 35

     Invalid service slot: 0

     No matched socket: 0

     Not delivered, input socket full: 0

Sent packets:

     Total: 19

     Relay forwarded: 19

     Relay received: 19

     Failed: 0

表1-18 display osi statistics命令显示信息描述表

字段

描述

Received packets

Total

从链路层接收的报文总数

Relay received

业务板从其他板中继接收的入方向报文总数，该计数不计入Total中

Relay forwarded

中继转发给业务板的入方向报文数

Invalid service slot

因为业务板不可用而被丢弃的报文数

No matched socket

因为未匹配报文入接口、或者未匹配MAC地址、或者不满足连接的过滤条件而被丢弃的报文数

Not delivered, input socket full

因为socket接收缓冲区已满而没有向上层传送的报文数

Sent packets

Total

IS-IS通过OSI连接发送的报文总数

Relay forwarded

中继转发给出接口所在板的出方向报文数，该计数不计入Total中

Relay received

出接口所在板从其他板中继接收的出方向报文总数

Failed

发送失败的报文个数

【相关命令】

·**reset osi statistics**

**IS-IS \-- IS-IS配置命令 \-- domain-authentication send-only**

------------------------------------------------------------------------

**[domain-authentication send-only**]命令用来配置对收到的Level-2报文（包括LSP、CSNP、PSNP）忽略认证信息检查。

**[undo domain-authentication send-only**]命令用来取消该配置。

【命令】

**[domain-authentication send-only**]

**[undo domain-authentication send-only**]

【缺省情况】

如果配置了路由域验证方式和验证密码，对收到的报文执行认证信息检查。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置路由域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的Level-2报文（包括LSP、CSNP、PSNP）中，并对收到的Level-2报文进行验证密码的检查。当需要更改密码时由于密码不匹配可能导致业务发生中断。通过命令配置对收到的Level-2报文忽略认证信息检查可保证业务不中断，报文正常接收。

【举例】

\# 对收到报文忽略认证信息检查。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 domain-authentication send-only

【相关命令】

·**area-authentication**** send-only**

·**domain-authentication-mode**

·**isis authentication send-only**

**IS-IS \-- IS-IS配置命令 \-- domain-authentication-mode**

------------------------------------------------------------------------

**[domain-authentication-mode**]命令用来配置路由域验证方式和验证密码。

**[undo** **domain-authentication-mode**]命令用来恢复缺省情况。

【命令】

**[domain-authentication-mode **[{ **gca** *key-id* { **hmac-sha-1** \| **hmac-sha-224** \| **hmac-sha-256** \| **hmac-sha-384** \| **hmac-sha-512** } \| **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* } [ **ip** \| **osi** ]]]

**[undo**] **domain-authentication-mode**

【缺省情况】

系统没有配置路由域验证方式和验证密码。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gca**]：GCA验证模式（Generic Cryptographic Authentication）。

*[key-id*]：唯一标识一个认证项（SA），取值范围为1～65535。发送方将Key ID放入认证TLV中，接收方根据报文中提取的Key ID选择SA对报文进行认证。

**[hmac-sha-1**]：支持HMAC-SHA-1算法。

**[hmac-sha-224**]：支持HMAC-SHA-224算法。

**[hmac-sha-256**]：支持HMAC-SHA-256算法。

**[hmac-sha-384**]：支持HMAC-SHA-384算法。

**[hmac-sha-512**]：支持HMAC-SHA-512算法。

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，为33～53个字符的字符串。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，为1～16个字符的字符串。

**[ip**]：检查LSP中IP的相应字段的配置内容。

**[osi**]：检查LSP中OSI的相应字段的配置内容。

【使用指导】

配置路由域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的Level-2报文（包括LSP、CSNP、PSNP）中并对收到的Level-2报文进行验证密码的检查。

需要注意的是：

·所有骨干层（Level-2）路由器必须配置相同的验证方式和验证密码。

·如果没有指定**ip**或**osi**参数，将检查LSP中OSI的相应字段的配置内容。

·以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。

·认证密码选用**ip**或**osi**不受实际的网络环境影响。

【举例】

\# 配置路由域采用简单明文验证模式，认证密码为123456。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 domain-authentication-mode simple plain 123456

【相关命令】

·**area-authentication-mode**

·**domain-authentication send-only**

·**isis authentication-mode**

**IS-IS \-- IS-IS配置命令 \-- fast-reroute**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[fast-reroute**]命令用来配置IS-IS支持快速重路由功能。

**[undo fast-reroute**]命令用来恢复缺省情况。

【命令】

**[fast-reroute**[ { **lfa** \| **route-policy** *route-policy-name* }]]

**[undo fast-reroute**]

【缺省情况】

IS-IS支持快速重路由功能处于关闭状态。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lfa**]：为所有路由通过LFA（Loop Free Alternate）算法选取备份下一跳信息。

**[route-policy**] *route-policy-name*：指定路由策略名，*route-policy-name*为1～63个字符的字符串，区分大小写。为通过策略的路由指定备份下一跳信息。

【使用指导】

IS-IS支持快速重路由功能不能与IS-IS的BFD功能同时使用，否则可能导致快速重路由功能失效。

【举例】

\# 为所有路由通过LFA算法选取备份下一跳信息。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 fast-reroute lfa

**IS-IS \-- IS-IS配置命令 \-- filter-policy export**

------------------------------------------------------------------------

**[filter-policy export**]命令用来配置IS-IS对引入的路由信息进行过滤。

**[undo filter-policy export**]命令用来取消该配置。

【命令】

**[filter-policy**[ { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **export** [ *protocol* [ *process-id* ] ]]]

**[undo** **filter-policy** **export** [ *protocol* [ *process-id*  ]]]

【缺省情况】

没有配置该过滤功能。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定访问控制列表序号，取值范围为2000～3999，基于ACL对引入的路由信息进行过滤。

**[prefix-list**] *prefix-list-name*：指定IPv4地址前缀列表名，基于目的地址对引入的路由信息进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy** *route-policy-name*]：指定路由策略名，基于路由策略对引入的路由信息进行过滤。*route-policy-name*为1～63个字符的字符串，区分大小写。

*[protocol*]：路由协议名称，指定过滤从哪种路由协议引入的路由信息。目前可包括：**bgp、direct、isis、ospf**、**rip**和**static**。如果不指定该参数，将对所有引入的路由进行过滤。

*[process-id*]：路由协议进程号，取值范围为1～65535。只有当*protocol*为**isis**、**ospf**、**rip**时，该参数可选，若未指定，缺省进程号为1。

【使用指导】

当配置的是高级ACL（3000～3999）或者指定的路由策略中配置的是高级ACL时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]来过滤指定目的地址和掩码的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。

【举例】

\# 使用编号为2000的基本ACL对引入的路由进行过滤。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule deny source 192.168.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 filter-policy 2000 export

\# 使用编号为3000的高级ACL对引入的路由进行过滤，只允许113.0.0.0/16通过。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0

Sysname-acl-ipv4-adv-3000 rule 100 deny ip

Sysname-acl-ipv4-adv-3000 quit

Sysname isis 1

Sysname-isis 1 address-family ipv4

Sysname-isis-1-ipv4 filter-policy 3000 export

【相关命令】

·**display isis route**

**IS-IS \-- IS-IS配置命令 \-- filter-policy import**

------------------------------------------------------------------------

**[filter-policy import**]命令用来配置IS-IS对接收的路由是否加入IP路由表进行过滤。

**[undo filter-policy import**]命令用来恢复缺省情况。

【命令】

**[filter-policy**[ { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **import**]]

**[undo filter-policy import**]

【缺省情况】

没有配置该过滤功能。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定访问控制列表序号，取值范围为2000～3999，基于ACL对接收的路由是否加入IP路由表进行过滤。

**[prefix-list** *prefix-list-name*]：指定IPv4地址前缀列表名，基于目的地址对接收的路由是否加入IP路由表进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy** *route-policy-name*]：指定路由策略名，基于路由策略对接收的路由是否加入IP路由表进行过滤。*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

当配置的是高级ACL（3000～3999）或者指定的路由策略中配置的是高级ACL时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]来过滤指定目的地址和掩码的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。

【举例】

\# 基于编号为2000的基本ACL对接收的路由是否加入IP路由表进行过滤。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule deny source 192.168.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 filter-policy 2000 import

\# 基于编号为3000的高级ACL对接收的路由是否加入IP路由表进行过滤，只允许113.0.0.0/16加入IP路由表。

\<Sysname\> system-view

Sysname acl number 3000

Sysname-acl-ipv4-adv-3000 rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0

Sysname-acl-ipv4-adv-3000 rule 100 deny ip

Sysname-acl-ipv4-adv-3000 quit

Sysname isis 1

Sysname-isis 1 address-family ipv4

Sysname-isis-1-ipv4 filter-policy 3000 import

【相关命令】

·**display ip routing-table**（三层技术-IP路由命令参考/IP路由基础）

**IS-IS \-- IS-IS配置命令 \-- flash-flood**

------------------------------------------------------------------------

**[flash-flood**]命令用来使能LSP快速扩散功能。

**[undo flash-flood**]命令用来关闭LSP快速扩散功能。

【命令】

**[flash-flood**[ [ **flood-count** *flooding-count* \| **max-timer-interval** *flooding-interval* \| [ **level-1** \| **level-2** ] ] \*]]

**[undo flash-flood**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

LSP快速扩散功能处于关闭状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[flood-count*** flooding-count*]：在SPF重新计算前快速扩散LSP的个数，取值范围为1～15，缺省值为5。

**[max-timer-interval*** flooding-interval*]：在LSP快速扩散之前的等待时间，取值范围为10～50000，单位为毫秒，缺省值为10毫秒。

**[level-1**]：使能在**level-1**级别的快速扩散功能。

**[level-2**]：使能在**level-2**级别的快速扩散功能。

【使用指导】

如果不指定级别，将同时使能**level-1**和**level-2**级别的快速扩散功能。

【举例】

\# 使能LSP快速扩散功能，配置发送个数10个，发送延时100毫秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 flash-flood flood-count 10 max-timer-interval 100

**IS-IS \-- IS-IS配置命令 \-- graceful-restart**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart**]命令用来使能IS-IS协议的GR能力。

**[undo graceful-restart**]命令用来关闭IS-IS协议的GR能力。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

IS-IS协议的GR能力处于关闭状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

IS-IS GR特性与IS-IS NSR特性互斥，即**graceful-restart**和**non-stop-routing**命令互斥，不能同时配置。

【举例】

\# 使能IS-IS进程1的GR能力。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 graceful-restart

【相关命令】

·**graceful-restart suppress-sa**

**IS-IS \-- IS-IS配置命令 \-- graceful-restart suppress-sa**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart suppress-sa**]命令用来配置重启时抑制SA（Suppress-Advertisement）位置位。**undo graceful-restart suppress-sa**命令用来取消重启时抑制SA位置位。

【命令】

**[graceful-restart suppress-sa**]

**[undo graceful-restart suppress-sa**]

【缺省情况】

SA位处于置位状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

SA表示抑制邻接标志位，其主要目的是为了避免出现路由黑洞，例如在启动或者重启时没有保留本地转发表，此时如果GR Helper将报文送到设备来进行转发将会造成严重的丢包现象，在这种情况下GR Restarter发送的Hello报文中必须将SA位置1，而GR Helper接收到这种SA位被置1的Hello报文后就不会将发送该Hello报文的GR Restarter放入LSP扩散出去。

【举例】

\# 配置重启时对SA位进行抑制。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 graceful-restart suppress-sa

【相关命令】

·**graceful-restart**

**IS-IS \-- IS-IS配置命令 \-- graceful-restart t1**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart t1**]命令用来配置T1定时器。

**[undo graceful-restart t1**]命令用来恢复缺省情况。

【命令】

**[graceful-restart t1** *seconds* **count** *count*]

**[undo graceful-restart t1**]

【缺省情况】

T1定时器的超时值为3秒，超时次数为10次。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：T1定时器的超时值，取值范围为3～10，单位为秒。

*[count*]：T1定时器超时次数，取值范围为1～20。

【使用指导】

T1定时器用来控制发送带有RR标志位的Restart TLV的次数。重启路由器发送带有RR标志位的Restart TLV，如果在超时时间内收到对端回复的带有RA标志的Restart TLV，才能正常进入GR流程；否则GR流程失败。

【举例】

\# 配置IS-IS进程1的T1定时器超时值为5秒，超时次数为5。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 graceful-restart t1 5 count 5

【相关命令】

·**graceful-restart**

·**graceful-restart**** t2**

·**graceful-restart ****t3**

**IS-IS \-- IS-IS配置命令 \-- graceful-restart t2**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart t2**]命令用来配置T2定时器。

**[undo graceful-restart t2**]命令用来恢复缺省情况。

【命令】

**[graceful-restart t2** *seconds*]

**[undo graceful-restart t2**]

【缺省情况】

T2定时器的超时值为60秒。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：T2定时器的超时值，取值范围为30～65535，单位为秒。

【使用指导】

T2定时器用来控制LSDB同步时间。每个LSDB都有一个T2定时器，对于Level-1-2路由器来说，就需要有两个T2定时器，一个为Level-1的T2定时器，另外一个为Level-2的T2定时器。如果Level-1和Level-2的T2定时器都超时后，LSDB同步还没有完成，则GR失败。

【举例】

\# 配置IS-IS进程1的T2定时器超时值为50秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 graceful-restart t2 50

【相关命令】

·**graceful-restart**

·**graceful-restart**** t1**

·**graceful-restart ****t3**

**IS-IS \-- IS-IS配置命令 \-- graceful-restart t3**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart t3**]命令用来配置T3定时器。

**[undo graceful-restart t3**]命令用来恢复缺省情况。

【命令】

**[graceful-restart t3 ***seconds*]

**[undo graceful-restart t3**]

【缺省情况】

T3定时器的超时值为300秒。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：T3定时器的超时值，取值范围为300～65535，单位为秒。

【使用指导】

T3定时器用来控制路由器的重启时间间隔。重启时间间隔在IS-IS的Hello PDU中设置为保持时间，这样在该路由器重启的时间内邻居不会断掉与其的邻接关系。如果T3定时器超时后GR还没有完成，则GR失败。

【举例】

\# 配置IS-IS进程1的T3定时器超时值为500秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 graceful-restart t3 500

【相关命令】

·**graceful-restart**

·**graceful-restart**** t1**

·**graceful-restart ****t2**

**IS-IS \-- IS-IS配置命令 \-- ignore-att**

------------------------------------------------------------------------

**[ignore-att**]命令用来配置IS-IS不采用ATT位计算缺省路由。

**[undo ignore-att**]命令用来取消该配置。

【命令】

**[ignore-att**]

**[undo ignore-att**]

【缺省情况】

IS-IS采用ATT位计算缺省路由。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置不采用ATT位计算缺省路由。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 ignore-att

**IS-IS \-- IS-IS配置命令 \-- import-route**

------------------------------------------------------------------------

**[import-route**]命令用来从其它路由协议或其它IS-IS进程引入路由信息。

**[undo import-route**]命令用来取消从其它路由协议或其它IS-IS进程引入路由信息。

【命令】

**[import-route**[ *protocol* [ *process-id* \| **all-processes** \| **allow-ibgp**   **allow-direct** \| **cost** *cost* \| **cost-type** { **external** \| **internal** } \| [ **level-1** \| **level-1-2** \| **level-2** ] \| **route-policy** *route-policy-name* \| **tag** *tag* ] \*]]

**[undo import-route**[ *protocol* [ *process-id* \| **all-processes** ]]]

【缺省情况】

IS-IS不引入其它协议的路由信息。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：指定引入的路由协议，可以是**bgp**、**direct**、**isis**、**ospf**、**rip**或**static**。

*[process-id*]：路由协议进程号，取值范围为1～65535，缺省值为1。只有当*protocol*是**isis**、**ospf**或**rip**时该参数可选。

**[all-processes**]：引入指定路由协议所有进程的路由，只有当*protocol*是**rip**、**ospf**或**isis**时可以指定该参数。

**[allow-ibgp**]：允许引入IBGP路由。只有当*protocol*是**bgp**时该参数可选。

**[allow-direct**]：在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入协议路由时不会包含使能了该协议的接口网段路由。当**allow-direct**与**route-policy** *route-policy-name*参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致**allow-direct**配置失效。例如，当配置**allow-direct**参数引入OSPF直连时，在路由策略中不要配置**if-match** **route-type**匹配条件，否则，**allow-direct**参数失效。

**[cost** *cost*]：引入的路由的路径开销，取值范围为0～4261412864。

·当路径开销值类型为**narrow**、**narrow-compatible**或**compatible**时，取值范围为0～63。

·当路径开销值类型为**wide**或**wide-compatible**时，取值范围为0～4261412864。

**[cost-type **[{ **external** \| **internal** }]]：表示路径开销类型：**internal**表示内部路由；**external**表示外部路由，配置路径开销类型为**external**后，通过LSP发布路由时路径开销会在配置的cost值的基础上加上64，从而保证内部路由优于外部路由。缺省情况下为**external**类型。只有当开销类型为**narrow**、**narrow-compatible**或者**compatible**时，该参数有效。

**[level-1**]：引入路由到Level-1的路由表中。

**[level-1-2**]：同时引入路由到Level-1和Level-2的路由表中。

**[level-2**]：引入路由到Level-2的路由表中。如果不指定引入的级别，默认为引入路由到Level-2路由表中。

**[route-policy** *route-policy-name*]：路由策略名称，只有满足指定路由策略匹配条件的路由才被引入。*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag ***tag*]：为引入路由配置Tag值，取值范围为1～4294967295。

【使用指导】

IS-IS将所有引入路由域中的路由当作外部路由，它们描述了应该如何选择到路由域以外目的地的路由。

真正生效的开销值受当前开销类型的影响。当路径开销值类型为**narrow**、**narrow-compatible**或**compatible**时，生效的开销值范围为0～63，超过63的也取值为63；当路径开销值类型为**wide**或**wide-compatible**时，配置值即为生效值。

需要注意的是：

·该命令不能引入缺省路由。

·**import-route bgp**表示只引入EBGP路由；**import-route bgp allow-ibgp**表示将IBGP路由也引入，容易引起路由环路，请慎用。

·只能引入路由表中状态为active的路由，是否为active状态可以通过**display ip routing-table** **protocol**命令来查看。

·**undo import-route** *protocol* **all-processes**命令只能取消**import-route** *protocol* **all-processes**命令的配置，不能取消**import-route** *protocol* *process-id*命令的配置。

【举例】

\# 引入静态路由，cost值为15。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 import-route static cost 15

【相关命令】

·**import-route limit**

**IS-IS \-- IS-IS配置命令 \-- import-route isis level-1 into level-2**

------------------------------------------------------------------------

**[import-route isis level-1 into level-2**]命令用来配置将Level-1区域的路由信息引入到Level-2区域。

**[undo import-route isis level-1 into level-2**]命令用来取消此功能。

【命令】

**[import-route isis level-1 into level-2**[ [ **filter-policy** { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } \| **tag** *tag* ] \*]]

**[undo import-route isis level-1 into level-2**]

【缺省情况】

Level-1区域的路由信息向Level-2区域发布。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[filter-policy**]：过滤策略。

*[acl-number*]：指定访问控制列表序号，取值范围为2000～3999，过滤从Level-1区域引入到Level-2区域的路由信息。

**[prefix-list** *prefix-list-name*]：指定IPv4地址前缀列表名，基于目的地址对从Level-1区域引入到Level-2区域的路由信息进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy** *route-policy-name*]：指定路由策略名，基于路由策略从Level-1区域引入到Level-2区域的路由信息进行过滤。*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag ***tag*]：为引入路由配置Tag值，取值范围为1～4294967295。

【使用指导】

·如果要通过路由策略对从Level-1区域引入到Level-2区域的路由信息进行过滤，必须在**import-route isis level-1 into level-2**命令中同时指定要应用的路由策略，否则路由过滤将不会生效；其它路由策略，如在接收或引入路由时指定的路由策略对路由渗透无效。

·如果指定了过滤策略，则只有通过过滤的路由才能够被发布到Level-2区域中。

【举例】

\# 配置路由器从Level-1向Level-2进行路由渗透。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 import-route isis level-1 into level-2

【相关命令】

·**import-route**

·**import-route isis level-1 into level-2**

**IS-IS \-- IS-IS配置命令 \-- import-route isis level-2 into level-1**

------------------------------------------------------------------------

**[import-route isis level-2 into level-1**]命令用来配置将Level-2区域的路由信息引入到Level-1区域。

**[undo import-route isis level-2 into level-1**]命令用来取消此功能。

【命令】

**[import-route isis level-2 into level-1 **[ **filter-policy** *[acl-number*****[\| **prefix-list** ]*prefix-list-name *[\| **route-policy** *route-policy-name* } \| **tag** ]*tag***** \*]]

**[undo import-route **]**isis level-2 into level-1**

【缺省情况】]

Level-2区域的路由信息不向Level-1区域发布。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[filter-policy**]：过滤策略。

*[acl-number*]：指定访问控制列表序号，取值范围为2000～3999，过滤从Level-2区域引入到Level-1区域的路由信息。

**[prefix-list** *prefix-list-name*]：指定IPv4地址前缀列表名，基于目的地址对从Level-2区域引入到Level-1区域的路由信息进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy** *route-policy-name*]：指定路由策略名，基于路由策略从Level-2区域引入到Level-1区域的路由信息进行过滤。*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag ***tag*]：为引入路由配置Tag值，取值范围为1～4294967295。

【使用指导】

·如果要通过路由策略对从Level-2区域引入到Level-1区域的路由信息进行过滤，必须在**import-route isis level-2 into level-1**命令中同时指定要应用的路由策略，否则路由过滤将不会生效；其它路由策略，如在接收或引入路由时指定的路由策略对路由渗透无效。

·如果指定了过滤策略，则只有通过过滤的路由才能够被发布到Level-1区域中。

【举例】

\# 配置路由器从Level-2向Level-1进行路由渗透。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 import-route isis level-2 into level-1

【相关命令】

·**import-route**

·**import-route isis level-1 into level-2**

**IS-IS \-- IS-IS配置命令 \-- import-route limit**

------------------------------------------------------------------------

**[import-route limit**]命令用来配置引入Level1/Level2的IPv4路由最大条数。

**[undo import-route limit**]命令用来恢复缺省情况。

【命令】

**[import-route limit ***number*]

**[undo import-route limit**]

【缺省情况】

本命令的缺省情况和设备的型号有关，请以设备的实际情况为准。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：引入Level1/Level2的IPv4路由最大条数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 配置IS-IS进程1引入Level1/Level2的IPv4路由最大条数为1000。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 import-route limit 1000

【相关命令】

·**import-route**

**IS-IS \-- IS-IS配置命令 \-- isis**

------------------------------------------------------------------------

**[isis**]命令用来创建一个IS-IS进程，并进入IS-IS视图。

**[undo isis**]命令用来删除IS-IS进程。

【命令】

**[isis** [ *process-id*   **vpn-instance** *vpn-instance-name* ]]

**[undo **]**isis** *process-id*

【缺省情况】

系统没有运行任何IS-IS进程。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535，缺省值为1。

**[vpn-instance*** vpn-instance-name*]：指定IS-IS所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示IS-IS位于公网中。

【举例】

\# 创建IS-IS进程1，配置网络实体名称，其中系统ID为0000.0000.0002，区域ID为01.0001。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 01.0001.0000.0000.0002.00

【相关命令】

·**isis enable**

·**network-entity**

**IS-IS \-- IS-IS配置命令 \-- isis authentication send-only**

------------------------------------------------------------------------

**[isis authentication send-only**]命令用来配置对收到的Hello报文忽略认证信息检查。

**[undo isis authentication send-only**]命令用来取消该配置。

【命令】

**[isis authentication send-only**[ [ **level-1** \| **level-2** ]]]

**[undo isis authentication send-only**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

如果配置了接口验证方式和验证密码，对收到的报文执行认证信息检查。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：对收到的Level-1 Hello报文忽略认证信息检查。

**[level-2**]：对收到的Level-2 Hello报文忽略认证信息检查。

【使用指导】

配置邻居关系验证方式和验证密码后，验证密码将会按照设定的方式封装到Hello报文中，并对接收到的Hello报文进行验证密码的检查，通过检查才会形成邻居关系。当需要更改密码时由于密码不匹配可能导致邻居关系中断。通过命令配置对收到的Hello报文忽略认证信息检查可保证邻居关系不中断，报文正常接收。

【举例】

\# 为接口GigabitEthernet1/0/1配置对收到Level-1 Hello报文忽略认证信息检查。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis authentication send-only level-1

【相关命令】

·**area-authentication send-only**

·**domain-authentication**** send-only**

·**isis authentication****-mode**

**IS-IS \-- IS-IS配置命令 \-- isis authentication-mode**

------------------------------------------------------------------------

**[isis authentication-mode**]命令用来配置邻居关系验证方式和验证密码。

**[undo isis authentication-mode**]命令用来取消该配置。

【命令】

**[isis authentication-mode**[ { **gca** *key-id* { **hmac-sha-1** \| **hmac-sha-224** \| **hmac-sha-256** \| **hmac-sha-384** \| **hmac-sha-512** } \| **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* } [ **level-1** \| **level-2**   **ip** \| **osi** ]]]

**[undo isis authentication-mode**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

接口没有配置邻居关系验证方式和验证密码。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gca**]：GCA验证模式（Generic Cryptographic Authentication）。

*[key-id*]：唯一标识一个认证项（SA），取值范围为1～65535。发送方将Key ID放入认证TLV中，接收方根据报文中提取的Key ID选择SA对报文进行认证。

**[hmac-sha-1**]：支持HMAC-SHA-1算法。

**[hmac-sha-224**]：支持HMAC-SHA-224算法。

**[hmac-sha-256**]：支持HMAC-SHA-256算法。

**[hmac-sha-384**]：支持HMAC-SHA-384算法。

**[hmac-sha-512**]：支持HMAC-SHA-512算法。

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，为33～53个字符的字符串，区分大小写。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，为1～16个字符的字符串，区分大小写。

**[level-1**]：为Level-1配置认证密码。

**[level-2**]：为Level-2配置认证密码。

**[ip**]：检查SNP、LSP中IP的相应字段的配置内容。

**[osi**]：检查SNP、LSP中OSI的相应字段的配置内容。

【使用指导】

配置邻居关系验证方式和验证密码后，验证密码将会按照设定的方式封装到Hello报文中，并对接收到的Hello报文进行验证密码的检查，通过检查才会形成邻居关系，否则将不会形成邻居关系。

需要注意的是：

·两台路由器要形成邻居关系必须配置相同的验证方式和验证密码。

·以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。

·如果没有指定**level-1**或**level-2**参数，将同时为**level-1**和**level-2**的Hello报文配置验证方式及验证密码。

·如果没有指定**ip**或**osi**参数，将检查Hello报文中OSI的相应字段的配置内容。

·认证密码选用**ip**或**osi**不受实际的网络环境影响。

·参数**level-1**和**level-2**的支持情况和产品相关，具体请以设备的实际情况为准。

·必须先使用**isis enable**命令在接口上使能IS-IS功能才能进行参数**level-1**和**level-2**的配置。

【举例】

·路由应用

\# 为接口GigabitEthernet1/0/1配置邻居关系采用简单明文验证模式，验证密码为123456。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis authentication-mode simple plain 123456

·交换应用

\# 为Vlan-interface10接口配置邻居关系采用简单明文验证模式，验证密码为123456。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis authentication-mode simple plain 123456

【相关命令】

·**area-authentication-mode**

·**domain-authentication-mode**

·**isis authentication send-only**

**IS-IS \-- IS-IS配置命令 \-- isis bfd enable**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[isis bfd enable**]命令用来使能IS-IS的BFD功能。

**[undo** **isis** **bfd enable**]命令用来关闭IS-IS的BFD功能。

【命令】

**[isis bfd enable**]

**[undo**]**isis bfd enable**

【缺省情况】

IS-IS的BFD功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 使能接口GigabitEthernet1/0/1的IS-IS BFD功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis enable

Sysname-GigabitEthernet1/0/1 isis bfd enable

·交换应用

\# 使能接口Vlan-interface11的IS-IS BFD功能。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 isis enable

Sysname-Vlan-interface11 isis bfd enable

**IS-IS \-- IS-IS配置命令 \-- isis circuit-level**

------------------------------------------------------------------------

**[isis circuit-level**]命令用来配置接口的链路邻接关系类型。

**[undo isis circuit-level**]命令用来恢复缺省情况。

【命令】

**[isis circuit-level**[ [ **level-1** \| **level-1-2** \| **level-2** ]]]

**[undo**]**isis circuit-level**

【缺省情况】

接口既可以建立Level-1的邻接关系，也可以建立Level-2的邻接关系。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：配置本接口链路邻接关系类型为Level-1。

**[level-1-2**]：配置本接口链路邻接关系类型为Level-1-2。

**[level-2**]：配置本接口链路邻接关系类型为Level-2。

【使用指导】

如果路由器类型是Level-1（Level-2），接口的链路类型只能为Level-1（Level-2），因此仅当路由器类型是Level-1-2时，才需要通过配置接口的链路邻接关系类型来限制接口上所能建立的邻接关系，让接口只发送和接收Level-1（Level-2）类型的Hello报文。

【举例】

·路由应用

\# 接口GigabitEthernet1/0/1和同一区域内的非骨干路由器相连，配置接口的链路邻接关系类型为Level-1，禁止发送和接收Level-2 Hello报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis enable

Sysname-GigabitEthernet1/0/1 isis circuit-level level-1

·交换应用

\# 接口Vlan-interface10和同一区域内的非骨干路由器相连，配置接口的链路邻接关系类型为Level-1，禁止发送和接收Level-2 Hello报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis enable

Sysname-Vlan-interface10 isis circuit-level level-1

【相关命令】

·**is-level**

**IS-IS \-- IS-IS配置命令 \-- isis circuit-type p2p**

------------------------------------------------------------------------

**[isis circuit-type p2p**]命令用来配置接口的网络类型为P2P。

**[undo isis circuit-type**]命令用来取消配置接口的网络类型为P2P。

【命令】

**[isis circuit-type p2p**]

**[undo**]**isis circuit-type**

【缺省情况】

接口网络类型根据物理接口决定。（VLAN接口网络类型为Broadcast。）

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口网络类型不同，其工作机制也略微不同，如：当网络类型为广播网时，需要选举DIS、通过泛洪CSNP报文来实现LSDB同步，当网络类型为P2P时不需要选举DIS，LSDB同步机制也不同。

当只有两台路由器接入到同一个广播网时，通过将接口网络类型配置为P2P可以使IS-IS按照P2P而不是广播网的工作机制运行，避免DIS选举以及CSNP的泛洪，既可以节省网络带宽，又可以加快网络的收敛速度。

需要注意的是，仅当接口的网络类型为广播网且只有两台路由器接入该广播网时才需要进行该项配置且两台路由器都要进行此项配置。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1为P2P类型。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis enable

Sysname-GigabitEthernet1/0/1 isis circuit-type p2p

·交换应用

\# 配置接口Vlan-interface10为P2P类型。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis enable

Sysname-Vlan-interface10 isis circuit-type p2p

**IS-IS \-- IS-IS配置命令 \-- isis cost**

------------------------------------------------------------------------

**[isis cost**]命令用来配置IS-IS接口的链路开销值。

**[undo isis cost**]命令用来取消该配置。

【命令】

**[isis cost**[ *value* [ **level-1** \| **level-2** ]]]

**[undo**]**isis cost**[ [ **level-1** \| **level-2** ]]

【缺省情况】

没有配置IS-IS接口的链路开销值。

【视图】

接口视图/接口IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：链路开销值，取值范围为1～16777215。

**[level-1**]：配置在计算Level-1路由时使用的链路开销值。

**[level-2**]：配置在计算Level-2路由时使用的链路开销值。

【使用指导】

如果没有指定**level-1**或者**level-2**，将同时配置计算Level-1和Level-2路由时使用的链路开销值。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1上Level-2的链路开销值为5。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis cost 5 level-2

·交换应用

\# 配置接口Vlan-interface10上Level-2的链路开销值为5。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis cost 5 level-2

【相关命令】

·**auto-cost enable**

·**bandwidth-reference**

**IS-IS \-- IS-IS配置命令 \-- isis dis-name**

------------------------------------------------------------------------

**[isis dis-name**]命令用来在DIS上配置局域网名称来代表这个广播网中的伪节点。

**[undo isis dis-name**]命令用来恢复缺省情况。

【命令】

**[isis dis-name** *symbolic-name*]

**[undo **]**isis dis-name**

【缺省情况】

没有配置本地局域网名称。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[symbolic-name*]：本地局域网的名称，为1～64个字符的字符串，不区分大小写。

【使用指导】

该命令只有在使能了动态主机名映射功能的路由器上配置才能有效，在点到点链路的接口上配置无效。

【举例】

·路由应用

\# 配置本地局域网的名称为"LOCALAREA"。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis dis-name LOCALAREA

·交换应用

\# 配置本地局域网的名称为"LOCALAREA"。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis dis-name LOCALAREA

【相关命令】

·**display ****isis name-table**

·**is-name**

**IS-IS \-- IS-IS配置命令 \-- isis dis-priority**

------------------------------------------------------------------------

**[isis dis-priority**]命令用来配置接口在不同层次的DIS优先级。

**[undo isis dis-priority**]命令用来取消该配置。

【命令】

**[isis dis-priority**[ *value* [ **level-1** \| **level-2** ]]]

**[undo**]**isis dis-priority**[ [ **level-1** \| **level-2** ]]

【缺省情况】

接口Level-1和Level-2级别DIS优先级为64。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：配置接口DIS优先级，取值范围为0～127。

**[level-1**]：配置Level-1级别DIS选举优先级。

**[level-2**]：配置Level-2级别DIS选举优先级。

【使用指导】

如果不指定级别，将同时配置Level-1和Level-2级别DIS选举优先级。

当网络类型为广播网时，IS-IS需要选举DIS，Level-1和Level-2的DIS是分别选举的，用户可以为不同级别的DIS选举配置不同的优先级，DIS优先级数值越高，被选中的可能性就越大；如果两台路由器DIS优先级相同，则SNPA（Subnetwork Point of Attachment，子网连接点）地址（广播网络中的SNPA地址是MAC地址）最大的路由器会被选中。

在IS-IS中并没有备份DIS的概念，优先级为0的路由器也可以参与选举DIS。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1的Level-2 DIS优先级为127。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis dis-priority 127 level-2

·交换应用

\# 配置接口Vlan-interface10的Level-2 DIS优先级为127。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis dis-priority 127 level-2

**IS-IS \-- IS-IS配置命令 \-- isis enable**

------------------------------------------------------------------------

**[isis enable**]命令用来在指定接口上使能IS-IS功能，并配置与该接口关联的IS-IS进程。

**[undo isis enable**]命令用来在指定接口上关闭IS-IS功能。

【命令】

**[isis enable** [ *process-id* ]]

**[undo**]**isis enable**

【缺省情况】

IS-IS功能在接口上处于关闭状态，且没有任何IS-IS进程与其关联。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：指定与该接口关联的IS-IS进程，*process-id*为IS-IS进程号，取值范围为1～65535，缺省值为1。

【举例】

·路由应用

\# 创建IS-IS路由进程1，并在接口GigabitEthernet1/0/1上使能IS-IS功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 10.0001.1010.1020.1030.00

Sysname-isis-1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis enable 1

·交换应用

\# 创建IS-IS路由进程1，并在接口Vlan-interface10上使能IS-IS功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 10.0001.1010.1020.1030.00

Sysname-isis-1 quit

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis enable 1

【相关命令】

·**isis**

·**network-entity**

**IS-IS \-- IS-IS配置命令 \-- isis fast-reroute lfa-backup exclude**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[isis fast-reroute lfa-backup exclude**]命令用来去使能接口LFA计算功能。

**[undo isis fast-reroute lfa-backup exclude**]命令用来恢复缺省情况。

【命令】

**[isis fast-reroute lfa-backup exclude**]

**[undo isis fast-reroute lfa-backup exclude**]

【缺省情况】

接口参与LFA计算。

【视图】

接口视图/接口IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口缺省参与LFA计算，有资格成为备份接口。配置本功能后，接口不会被选为备份接口。

【举例】

·路由应用

\# 去使能接口GigabitEthernet1/0/1的LFA计算功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 10.0001.1010.1020.1030.00

Sysname-isis-1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis enable 1

Sysname-GigabitEthernet1/0/1 isis fast-reroute lfa-backup exclude

·交换应用

\#去使能接口Vlan-interface10的LFA计算功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 10.0001.1010.1020.1030.00

Sysname-isis-1 quit

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis enable 1

Sysname-Vlan-interface10 isis fast-reroute lfa-backup exclude

【相关命令】

·**fast-reroute**

**IS-IS \-- IS-IS配置命令 \-- isis mesh-group**

------------------------------------------------------------------------

**[isis mesh-group**]命令用来配置接口属于Mesh group或配置接口阻塞。

**[undo isis mesh-group**]命令用来恢复缺省情况。

【命令】

**[isis mesh-group **[{ *mesh-group-number* \| **mesh-blocked** }]]

**[undo **]**isis mesh-group**

【缺省情况】

接口不属于任何Mesh-Group且接口不阻塞。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mesh-group-number*]：Mesh-Group号，取值范围为1～4294967295。

**[mesh-blocked**]：配置接口阻塞，接口只有在收到邻居路由器要求发送LSP的请求时才会发送LSP，否则不会主动向外发送LSP。

【使用指导】

对于不属于Mesh-Group的接口，当收到LSP时，接口将按照正常流程将LSP扩散到所有其它接口。对于连通程度比较高，有多条点到点链路的NBMA网络，这种处理会造成LSP的重复扩散，浪费带宽。

把接口配置属于一个Mesh-Group后，当接收到一个新的LSP时，只把LSP扩散到其它Mesh-Group的接口以及没有配置Mesh group的接口，而不会扩散到到同Mesh-Group中的其它接口。

若配置某个接口阻塞，则该接口只有在收到邻居路由器要求发送LSP的请求时才会发送LSP，否则不会主动向外发送LSP。

需要注意的是，Mesh-Group只对点到点类型链路的接口起作用。

【举例】

\# 将帧中继子接口Serial2/1/1.1加入组号为3的Mesh-Group中。

\<Sysname\> system-view

Sysname interface serial 2/1/1

Sysname-Serial2/1/1 link-protocol fr

Sysname-Serial2/1/1 quit

Sysname interface serial 2/1/1.1

Sysname-Serial2/1/1.1 isis mesh-group 3

**IS-IS \-- IS-IS配置命令 \-- isis mib-binding**

------------------------------------------------------------------------

**[isis mib-binding**]命令用来配置IS-IS进程绑定MIB。

**[undo isis mib-binding**]命令用来恢复缺省情况。

【命令】

**[isis mib-binding*** process-id*]

**[undo isis mib-binding**]

【缺省情况】

MIB绑定在进程号最小的IS-IS进程上。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535。

【使用指导】

·如果指定的*process-id*不存在，配置IS-IS进程绑定命令时将会提示IS-IS进程不存在，无法完成配置。

·如果配置了IS-IS进程绑定MIB，若删除*process-id*对应的IS-IS进程，则同时删除IS-IS进程绑定MIB配置，MIB绑定到进程号最小的IS-IS进程上。

【举例】

\# 配置IS-IS进程100绑定MIB。

\<Sysname\> system-view

Sysname isis mib-binding 100

**IS-IS \-- IS-IS配置命令 \-- isis peer-ip-check**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[isis peer-ip-check**]命令用来配置在PPP接口上建立邻接关系必须在同一网段的检查功能，即在接收Hello报文时，对端的IP地址与当前接口必须在同一网段。

**[undo isis peer-ip-check**]命令用来恢复缺省情况。

【命令】

**[isis peer-ip-check**]

**[undo isis peer-ip-check**]

【缺省情况】

协议类型为PPP的接口要与对端路由器建立邻接关系，双方可以不在同一网段。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置在Serial2/1/0接口上与对端路由器建立邻接关系必须在同一网段的检查功能，即在Serial2/1/0上接收IS-IS Hello报文时，对端的IP地址与当前接口必须在同一网段才可以建立邻接关系。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 isis peer-ip-check

**IS-IS \-- IS-IS配置命令 \-- isis prefix-suppression**

------------------------------------------------------------------------

**[isis prefix-suppression**]命令用来配置接口的前缀抑制功能。

**[undo isis prefix-suppression**]命令用来恢复缺省情况。

【命令】

**[isis prefix-suppression**]

**[undo isis prefix-suppression**]

【缺省情况】

未配置接口的前缀抑制功能。

【视图】

接口视图/接口IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口使能IS-IS时，有时候不希望在LSP中发布此接口的前缀，可以通过在接口上配置本命令，减少此接口的前缀在LSP中携带，屏蔽内部节点被发布，提高安全性，加快路由收敛。

本命令对接口从地址同样生效。

【举例】

·路由应用

\# 接口GigabitEthernet1/0/1使能前缀抑制功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis prefix-suppression

·交换应用

\# 接口Vlan-interface10使能前缀抑制功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis prefix-suppression

**IS-IS \-- IS-IS配置命令 \-- isis primary-path-detect bfd echo**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[isis primary-path-detect bfd echo**]命令用来使能IS-IS协议中主用链路的BFD（Echo方式）检测功能。

**[undo isis primary-path-detect bfd**]命令用来恢复缺省情况。

【命令】

**[isis primary-path-detect bfd echo**]

**[undo isis primary-path-detect bfd**]

【缺省情况】

IS-IS协议中主用链路的BFD（Echo方式）检测功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置本功能后，IS-IS协议的快速重路由特性和PIC特性中的主用链路将使用BFD（Echo方式）进行检测。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置IS-IS协议快速重路由特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 fast-reroute lfa

Sysname-isis-1-ipv4 quit

Sysname-isis-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis primary-path-detect bfd echo

\# 在接口GigabitEthernet1/0/2上配置IS-IS协议PIC特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 pic additional-path-always

Sysname-isis-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 isis primary-path-detect bfd echo

·交换应用

\# 在接口Vlan-interface10上配置IS-IS协议快速重路由特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 fast-reroute lfa

Sysname-isis-1-ipv4 quit

Sysname-isis-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis primary-path-detect bfd echo

\# 在接口Vlan-interface11上配置IS-IS协议PIC特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 pic additional-path-always

Sysname-isis-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 isis primary-path-detect bfd echo

**IS-IS \-- IS-IS配置命令 \-- isis silent**

------------------------------------------------------------------------

**[isis silent**]命令用来禁止接口发送和接收IS-IS报文。

**[undo isis silent**]命令用来恢复缺省情况。

【命令】

**[isis silent**]

**[undo **]**isis silent**

【缺省情况】

接口既发送也接收IS-IS报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

Loopback接口视图下不支持此命令。

【举例】

·路由应用

\# 禁止接口GigabitEthernet1/0/1发送和接收IS-IS报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis silent

·交换应用

\# 禁止接口Vlan-interface10发送和接收IS-IS报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis silent

**IS-IS \-- IS-IS配置命令 \-- isis small-hello**

------------------------------------------------------------------------

**[isis small-hello**]命令用来配置接口发送不加入填充CLV的小型Hello报文。

**[undo isis small-hello**]命令用来恢复缺省情况。

【命令】

**[isis small-hello**]

**[undo **]**isis small-hello**

【缺省情况】

接口发送标准Hello报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

Loopback接口视图下不支持此命令。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1发送小型Hello报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis small-hello

·交换应用

\# 指定接口Vlan-interface10发送小型Hello报文。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis small-hello

**IS-IS \-- IS-IS配置命令 \-- isis tag**

------------------------------------------------------------------------

**[isis tag**]命令用来配置接口的Tag值。

**[undo isis tag**]命令用来恢复缺省情况。

【命令】

**[isis tag ***tag*]

**[undo isis tag**]

【缺省情况】

没有配置接口的Tag值。

【视图】

接口视图/接口IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag*]：管理标记值，取值范围为1～4294967295。

【使用指导】

当cost-sytle为wide、wide-compatible 或compatible时，如果发布可达的IP地址前缀具有Tag属性，IS-IS会将Tag加入到该前缀的IP可达信息TLV中。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1的Tag值。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis tag 4294967295

·交换应用

\# 配置接口Vlan-interface10的Tag值。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis tag 4294967295

**IS-IS \-- IS-IS配置命令 \-- isis timer csnp**

------------------------------------------------------------------------

**[isis timer csnp**]命令用来配置DIS在广播网络上发送CSNP报文的时间间隔。

**[undo isis timer csnp**]命令用来取消该配置。

【命令】

**[isis timer csnp**[ *seconds* [ **level-1** \| **level-2** ]]]

**[undo**]**isis timer csnp**[ [ **level-1** \| **level-2** ]]

【缺省情况】

DIS在广播网络上发送CSNP报文的时间间隔为10秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：DIS在广播网络上发送CSNP报文的时间间隔，取值范围为1～600，单位为秒。

**[level-1**]：配置DIS在Level-1发送CSNP报文的时间间隔。

**[level-2**]：配置DIS在Level-2发送CSNP报文的时间间隔。

【使用指导】

如果不指定级别，将同时配置DIS在Level-1和Level-2发送CSNP报文的时间间隔。

当网络类型为广播网时，DIS使用CSNP报文来进行LSDB同步，因此只有在被选举为DIS的路由器上进行该项配置才有效。

【举例】

·路由应用

\# 配置Level-2的CSNP报文在接口GigabitEthernet1/0/1上的发送时间间隔为15秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis timer csnp 15 level-2

·交换应用

\# 配置Level-2的CSNP报文在Vlan-interface10接口上的发送时间间隔为15秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis timer csnp 15 level-2

**IS-IS \-- IS-IS配置命令 \-- isis timer hello**

------------------------------------------------------------------------

**[isis timer hello**]命令用来配置Hello报文的发送时间间隔。

**[undo isis timer hello**]命令用来取消该配置。

【命令】

**[isis timer hello**[ *seconds* [ **level-1** \| **level-2** ]]]

**[undo**]**isis timer hello**[ [ **level-1** \| **level-2** ]]

【缺省情况】

Hello报文的发送时间间隔为10秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：配置Hello报文的发送时间间隔，取值范围为3～255，单位为秒。

**[level-1**]：配置Level-1 Hello报文的发送时间间隔。

**[level-2**]：配置Level-2 Hello报文的发送时间间隔。

【使用指导】

如果路由器在邻居关系保持时间内（即Hello报文失效数目与Hello报文发送时间间隔的乘积）没有收到来自邻居路由器的Hello报文时将宣告邻居关系失效。通过设置Hello报文失效数目和Hello报文的发送时间间隔，可以调整邻居关系保持时间，即邻居路由器要花多长时间能够监测到链路已经失效并重新进行路由计算。

需要注意的是：

·在广播链路上，Level-1和Level-2 Hello报文会分别发送，其时间间隔也要分别配置；在点到点链路中，Level-1和Level-2的Hello报文是在同一个点到点Hello报文中发送，不需要分别配置发送时间间隔。

·参数level-1和level-2仅在广播接口上是可配置的，而且必须先在接口上使能IS-IS功能。

·发送时间间隔越短，网络收敛更快，但也需要占用更多的系统资源；因此，需要根据实际情况指定。

·如果不指定级别，将同时配置Level-1和Level-2的Hello报文发送时间间隔。

【举例】

·路由应用

\# 配置Level-2的Hello报文在接口GigabitEthernet1/0/1上的发送时间间隔为20秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis timer hello 20 level-2

·交换应用

\# 配置Level-2的Hello报文在Vlan-interface10接口上的发送时间间隔为20秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis timer hello 20 level-2

【相关命令】

·**isis timer holding-multiplier**

**IS-IS \-- IS-IS配置命令 \-- isis timer holding-multiplier**

------------------------------------------------------------------------

**[isis timer holding-multiplier**]命令用来配置Hello报文失效数目。

**[undo isis timer holding-multiplier**]命令用来取消该配置。

【命令】

**[isis timer holding-multiplier**[ *value* [ **level-1** \| **level-2** ]]]

**[undo **]**isis timer holding-multiplier**[ [ **level-1** \| **level-2** ]]

【缺省情况】

Hello报文失效数目为3。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：IS-IS邻居的Hello报文失效数目，取值范围为3～1000。

**[level-1**]：Level-1的IS-IS邻居Hello报文失效数目。

**[level-2**]：Level-2的IS-IS邻居Hello报文失效数目。

【使用指导】

Hello报文失效数目，即宣告邻居失效前IS-IS没有收到的邻居Hello报文的数目。

如果路由器在邻居关系保持时间内（即Hello报文失效数目与Hello报文发送时间间隔的乘积）没有收到来自邻居路由器的Hello报文时将宣告邻居关系失效。通过设置Hello报文失效数目和Hello报文的发送时间间隔，可以调整邻居关系保持时间，即邻居路由器要花多长时间能够监测到链路已经失效并重新进行路由计算。

需要注意的是：

·在广播链路上，Level-1和Level-2 Hello报文会分别发送，Hello报文失效数目需要分别设置；在点到点链路中，Level-1和Level-2的Hello报文是在同一个点到点Hello报文中发送，因此不需要指定Level-1或Level-2。

·参数level-1和level-2仅在广播接口上是可配置的，而且必须先在接口上使能IS-IS功能。

·如果不指定级别，将同时配置Level-1和Level-2的Hello报文失效数目。

·Hello报文失效数目与Hello报文发送时间间隔的乘积不能超过65535。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1上标志邻居失效的Level-2 Hello报文数目为6。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis timer holding-multiplier 6 level-2

·交换应用

\# 指定接口Vlan-interface10上标志邻居失效的Level-2 Hello报文数目为6。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis timer holding-multiplier 6

【相关命令】

·**isis timer hello**

**IS-IS \-- IS-IS配置命令 \-- isis timer lsp**

------------------------------------------------------------------------

**[isis timer lsp**]命令用来配置IS-IS在接口上发送LSP的最小时间间隔以及一次最多可以发送的LSP报文数目。

**[undo isis timer lsp**]命令用来恢复缺省情况。

【命令】

**[isis timer lsp ***time * **count** *count* ]

**[undo**]**isis timer lsp**

【缺省情况】

发送LSP的最小时间间隔为33毫秒，一次最多可以发送5个LSP报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：发送链路状态报文的最小时间间隔，取值范围为1～1000，单位为毫秒。

*[count*]：一次最多发送的链路状态报文的数目，取值范围为1～1000。

【使用指导】

当LSDB的内容发生变化时，IS-IS将把发生变化的LSP扩散出去，用户可以对LSP的最小发送时间间隔进行调节。

请合理配置LSP发送时间间隔，当存在大量IS-IS接口或大量路由时，会发送大量的LSP报文，导致LSP风暴的出现。

【举例】

·路由应用

\# 配置在GigabitEthernet1/0/1接口LSP的发送时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis timer lsp 500

·交换应用

\# 配置在Vlan-interface10接口LSP的发送时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis timer lsp 500

【相关命令】

·**isis timer retransmit**

**IS-IS \-- IS-IS配置命令 \-- isis timer retransmit**

------------------------------------------------------------------------

**[isis timer retransmit**]命令用来配置LSP在点到点链路上的重传时间间隔。

**[undo isis timer retransmit**]命令用来恢复缺省情况。

【命令】

**[isis timer retransmit ***seconds*]

**[undo isis timer retransmit**]

【缺省情况】

LSP在点到点链路上的重传时间间隔为5秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：表示LSP报文的重传时间间隔，取值范围1～300，单位为秒。

【使用指导】

在点到点链路上，发送的LSP需要得到对端的应答，否则将在重传时间间隔内重新发送该LSP；在广播链路上，DIS周期性广播CSNP来实现LSDB的同步，不需要进行此项配置。

【举例】

·路由应用

\# 在接口Serial2/1/1上配置LSP在点到点链路上的重传时间间隔为50秒。

\<Sysname\> system-view

Sysname interface serial 2/1/1

Sysname-Serial2/1/1 isis timer retransmit 50

·交换应用

\# 在接口Vlan-interface10上配置LSP在点到点链路上的重传时间间隔为50秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis circuit-type p2p

Sysname-Vlan-interface10 isis timer retransmit 50

【相关命令】

·**isis circuit-type p2p**

·**isis timer ****lsp**

**IS-IS \-- IS-IS配置命令 \-- isis topology enable**

------------------------------------------------------------------------

**[isis topology enable**]命令用来在接口使能拓扑的IS-IS功能。

**[undo isis topology enable**]命令用来关闭此拓扑的IS-IS功能。

【命令】

**[isis topology enable**]

**[undo isis topology enable**]

【缺省情况】

没有使能拓扑的IS-IS功能。

【视图】

接口IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令必须满足下面条件才能进行配置：

·接口使能了IS-IS；

·创建了IS-IS IPv4单播拓扑。

【举例】

\# 在接口上IS-IS IPv4单播拓扑voice中使能IS-IS功能。

\<Sysname\> system-view

Sysname isis 100

Sysname-isis-100 address-family ipv4

Sysname-isis-100-ipv4 topology voice tid 4000

Sysname-isis-100-ipv4-topo-voice quit

Sysname-isis-100-ipv4 quit

Sysname-isis-100 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis enable 100

Sysname-GigabitEthernet1/0/1 topology ipv4 voice

Sysname-GigabitEthernet1/0/1-topo-voice isis topology enable

**IS-IS \-- IS-IS配置命令 \-- ispf enable**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ispf enable**]命令用来使能IS-IS ISPF功能，即增量SPF计算功能。

**[undo ispf enable**]命令用来关闭IS-IS ISPF功能。

【命令】

**[ispf enable**]

**[undo ispf enable**]

【缺省情况】

使能IS-IS ISPF功能。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能增量SPF计算功能后，当网络的拓扑结构发生变化影响到最短路径树的结构时，只将受影响的部分节点进行修正，而不重建整棵最短路径树。

【举例】

\# 使能增量SPF计算功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 ispf enable

**IS-IS \-- IS-IS配置命令 \-- is-level**

------------------------------------------------------------------------

**[is-level**]命令用来配置路由器的Level级别。

**[undo is-level**]命令用来恢复缺省情况。

【命令】

**[is-level**[ { **level-1** \| **level-1-2** \| **level-2** }]]

**[undo** **is-level**]

【缺省情况】

路由器的的Level级别为Level-1-2。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：配置路由器工作在Level-1，它只计算区域内路由，维护L1的LSDB。

**[level-1-2**]：配置路由器工作在Level-1-2，同时参与L1和L2的路由计算，维护L1和L2两个LSDB。

**[level-2**]：配置路由器工作在Level-2，只参加L2的LSP交换和L2的路由计算，维护L2的LSDB。

【使用指导】

如果只有一个区域，建议用户将所有路由器的Level配置为Level-1或者Level-2，因为没有必要让所有路由器同时维护两个完全相同的数据库。

在IP网络中使用时，建议将所有的路由器都配置为Level-2，这样有利于以后的扩展。

【举例】

\# 配置路由器的Level级别为Level-1。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 is-level level-1

**IS-IS \-- IS-IS配置命令 \-- is-name**

------------------------------------------------------------------------

**[is-name**]命令用来使能动态主机名映射功能并为当前路由器配置主机名称。

**[undo is-name**]命令用来关闭动态主机名映射功能。

【命令】

**[is-name ***sys-name*]

**[undo is-name**]

【缺省情况】

动态主机名映射功能处于关闭状态且没有为当前路由器配置主机名称。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sys-name*]：为本地IS配置的主机名称，为1～64个字符的字符串，不区分大小写。

【使用指导】

只有使能动态主机名映射功能后，使用**display isis lsdb**等命令才可以看到路由器的主机名而不是System ID。

【举例】

\# 为本地IS配置主机名称。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 is-name RUTA

【相关命令】

·**display isis name-table**

**IS-IS \-- IS-IS配置命令 \-- is-name map**

------------------------------------------------------------------------

**[is-name map**]命令用来为远端IS配置System ID与主机名称的映射关系。

**[undo is-name map**]命令用来取消此配置。

【命令】

**[is-name map** *sys-id* *map-sys-name*]

**[undo** **is-name map** *sys-id*]

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sys-id*]：远端IS的系统ID或伪系统ID。

*[map-sys-name*]：为远端IS配置的主机名称，为1～64个字符的字符串，不区分大小写。

【使用指导】

每个System ID只能对应一个主机名称。

【举例】

\# 为远端IS配置静态主机名映射，远端IS的System ID为"0000.0000.0041"，为其配置的主机名称为"RUTB"。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 is-name map 0000.0000.0041 RUTB

【相关命令】

·**display isis name-table**

**IS-IS \-- IS-IS配置命令 \-- log-peer-change**

------------------------------------------------------------------------

**[log-peer-change**]命令用来打开邻接状态变化的输出开关。

**[undo log-peer-change**]命令用来关闭邻接状态变化的输出开关。

【命令】

**[log-peer-change**]

**[undo log-peer-change**]

【缺省情况】

邻接状态变化的输出开关处于打开状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

打开邻接状态输出开关后，IS-IS邻接状态变化时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）

【举例】

\# 关闭IS-IS邻接状态变化的输出开关。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 undo log-peer-change

**IS-IS \-- IS-IS配置命令 \-- lsp-fragments-extend**

------------------------------------------------------------------------

**[lsp-fragments--extend**]命令用来在指定Level上使能IS-IS进程的LSP分片扩展功能。

**[undo lsp-fragments--extend**]命令用来关闭该功能。

【命令】

**[lsp-fragments-extend**[ [ **level-1** \| **level-1-2** \| **level-2** ]]]

**[undo lsp-fragments-extend**]

【缺省情况】

LSP分片扩展功能处于关闭状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：只对Level-1 LSP进行分片扩展。

**[level-1-2**]：对Level-1 LSP和Level-2 LSP都进行分片扩展。

**[level-2**]：只对Level-2 LSP进行分片扩展。

【使用指导】

如果配置时没有指定**level-1**、**level-2**或**level-1-2**参数，IS-IS进程运行LSP分片扩展功能时，将同时对Level-1 LSP和Level-2 LSP都进行分片扩展。

【举例】

\# 使能Level-2的LSP分片扩展功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 lsp-fragments-extend level-2

**IS-IS \-- IS-IS配置命令 \-- lsp-length originate**

------------------------------------------------------------------------

**[lsp-length originate**]命令用来配置当前路由器生成的Level-1 LSP和Level-2 LSP的最大长度。

**[undo lsp-length originate**]命令用来取消该配置。

【命令】

**[lsp-length originate ***size*****[[ **level-1** \| **level-2** ]]]

**[undo lsp-length originate**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

生成的Level-1 LSP和Level-2 LSP的最大长度均为1497个字节。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：LSP的最大长度，取值范围为512～16384，单位为字节。

**[level-1**]：配置Level-1 LSP长度。

**[level-2**]：配置Level-2 LSP长度。

【使用指导】

如果命令中没有指定Level-1或Level-2，则默认为对当前IS-IS系统进行配置。

【举例】

\# 配置生成的Level-2 LSP最大长度为1024字节。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 lsp-length originate 1024 level-2

**IS-IS \-- IS-IS配置命令 \-- lsp-length receive**

------------------------------------------------------------------------

**[lsp-length receive**]命令用来配置当前路由器可以接收的LSP的最大长度。

**[undo lsp-length receive**]命令用来恢复缺省情况。

【命令】

**[lsp-length receive ***size*]

**[undo lsp-length receive**]

【缺省情况】

可以接收的LSP的最大长度为1497个字节。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：LSP的最大长度，取值范围为512～16384，单位为字节。

【举例】

\# 配置接收LSP报文最大长度为1024字节。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 lsp-length receive 1024

**IS-IS \-- IS-IS配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[maximum load**-**balancing**]命令用来配置IS-IS支持的等价路由的最大条数。

**[undo maximum load-balancing**]命令用来恢复缺省情况。

【命令】

**[maximum load-balancing ***number*]

**[undo** **maximum load-balancing**]

【缺省情况】

IS-IS支持的等价路由的最大条数与系统支持最大等价路由的条数相同。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：等价路由的最大条数。不同设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【使用指导】

如果通过**max-ecmp-num**命令配置系统支持最大等价路由的条数为m，则本命令的缺省值为m，取值范围为1～m。

**[max-ecmp-num**]命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置IS-IS支持的等价路由的最大条数为2。

\<Sysname\> system-view

Sysname isis 100

Sysname-isis-100 address-family ipv4

Sysname-isis-1-ipv4 maximum load-balancing 2

【相关命令】

·**max-ecmp-num**（三层技术-IP路由命令参考/IP路由基础）

**IS-IS \-- IS-IS配置命令 \-- network-entity**

------------------------------------------------------------------------

**[network-entity**]命令用来配置IS-IS进程的网络实体名称（Network Entity Title，简称NET）。

**[undo network-entity**]命令用来删除网络实体名称。

【命令】

**[network-entity** *net*]

**[undo** **network-entity** *net*]

【缺省情况】

没有配置NET。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[net*]：格式为X...X.XXXX\....XXXX.00，为十六进制数。前面的"X...X"是区域地址，中间的12个"X"是路由器的System ID，最后的"00"是SEL。

【使用指导】

NET可以看作是一类特殊的NSAP，即SEL为0的NSAP地址，长度为8～20个字节。

NET由三部分组成：

·区域ID：它的长度可变的，为1～13个字节。

·System ID：用来在区域内唯一标识主机或路由器，它的长度固定为6个字节。

·SEL：为0，它的长度固定为1个字节。

例如NET为：ab.cdef.1234.5678.9abc.00，则其中区域ID为ab.cdef，System ID为1234.5678.9abc，SEL为00。

【举例】

\# 指定NET为10.0001.1010.1020.1030.00。其中区域ID是10.0001，System ID是1010.1020.1030。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 10.0001.1010.1020.1030.00

【相关命令】

·**isis**

·**isis enable**

**IS-IS \-- IS-IS配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[non-stop-routing**]命令用来使能IS-IS协议的NSR功能。

**[undo **]**non-stop-routing**命令用来关闭IS-IS协议的NSR功能。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

IS-IS NSR特性与IS-IS GR特性互斥，即**non-stop-routing**和**graceful-restart**命令互斥，不能同时配置。

【举例】

\#在IS-IS进程1中使能NSR功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 non-stop-routing

**IS-IS \-- IS-IS配置命令 \-- pic**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[pic**]命令用来使能前缀无关收敛功能。

**[undo pic**]命令用来关闭前缀无关收敛功能。

【命令】

**[pic** [ **[additional-path-always** ]]]

**[undo pic**]

【缺省情况】

前缀无关收敛功能处于开启状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[additional-path-always**]：支持非直连的次优路由作为备份。

【使用指导】

PIC（Prefix Independent Convergence，前缀无关收敛），即收敛时间与前缀数量无关，加快收敛速度。传统的路由计算快速收敛都与前缀数量相关，收敛时间与前缀数量成正比。只有邻居发送的LSP才会进行PIC。

IS-IS快速重路由功能和PIC同时配置时，IS-IS快速重路由功能生效。

【举例】

\# 使能IS-IS协议的PIC支持非直连次优路由做备份功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 pic additional-path-always

**IS-IS \-- IS-IS配置命令 \-- preference**

------------------------------------------------------------------------

**[preference**]命令用来配置IS-IS路由优先级。

**[undo preference**]命令用来恢复缺省情况。

【命令】

**[preference**[ { *preference* \| **route-policy** *route-policy-name* } \*]]

**[undo preference**]

【缺省情况】

IS-IS路由的优先级为15。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference*]：IS-IS路由优先级，取值范围为1～255。

**[route-policy*** route-policy-name*]：指定路由策略，对通过该路由策略过滤的路由指定优先级。*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

配置了**route-policy**参数后，如果**route-policy**中对某些匹配的路由优先级进行了修改，则这些匹配的路由取**route-policy**修改的优先级，其它路由的优先级均取**preference**命令所设的值。

由于在一台路由器上可能同时运行多种动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题。系统为每一种路由协议配置一个优先级，当不同协议都发现了到同一目的地的路由时，优先级高的协议将起决定作用。

【举例】

\# 配置IS-IS协议的优先级为25。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 preference 25

**IS-IS \-- IS-IS配置命令 \-- prefix-priority**

------------------------------------------------------------------------

**[prefix-priority**]命令用来配置指定IS-IS路由收敛的优先级。

**[undo prefix-priority**]命令用来取消该配置。

【命令】

**[prefix-priority**[ { **critical** \| **high** \| **medium** } { **prefix-list** *prefix-list-name* \| **tag** *tag-value* }]]

**[prefix-priority** **route-policy** *route-policy-name*]

**[undo prefix-priority**[ { **critical** \| **high** \| **medium** } [ **prefix-list** \| **tag** ]]]

**[undo prefix-priority** **route-policy**]

【缺省情况】

IS-IS路由收敛的优先级为低优先级。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[critical**]：最高优先级。

**[high**]：高优先级。

**[medium**]：中优先级。

**[prefix-list ***prefix-list-name*]：指定IPv4地址前缀列表名，唯一标识一个IPv4地址前缀列表。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[tag*** tag-value*]：指定要求的标记值，取值范围为1～4294967295。

**[route-policy** *route-policy-name*]：指定路由策略名，配置路由收敛的优先级。*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

IS-IS路由的优先级越高收敛的速度越快。

需要注意的是，IS-IS主机路由的优先级为中优先级。

【举例】

\# 配置前缀列表standtest的IS-IS路由收敛的优先级为高优先级。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 prefix-priority high prefix-list standtest

**IS-IS \-- IS-IS配置命令 \-- reset isis all**

------------------------------------------------------------------------

**[reset isis all**]命令用来清除IS-IS进程所有的数据结构信息。

【命令】

**[reset isis all **\*[process-id*****  **graceful-restart** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围为1～65535，清除该IS-IS进程所有的数据结构信息。

**[graceful-restart**]：清除IS-IS数据之后，通过GR方式来恢复。

【使用指导】

如果未指定IS-IS进程号，将清除所有IS-IS进程的数据结构信息。

本命令用在某些需要立即刷新LSP的情况下。

【举例】

\# 清除所有IS-IS进程的数据结构信息。

\<Sysname\> reset isis all

**IS-IS \-- IS-IS配置命令 \-- reset isis graceful-restart event-log**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset isis graceful-restart event-log**]命令用来清除IS-ISGR的日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset isis **]**graceful-restart event-log slot** *slot-number* [ **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[reset isis **]**graceful-restart event-log chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：清除指定单板的IS-IS GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：清除指定成员设备的IS-IS GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**] *chassis-number* **slot** *slot-number*：清除指定成员设备上指定单板的IS-IS GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 清除1号板上GR的日志信息。

\<Sysname\> reset isis graceful-restart event-log slot 1

**IS-IS \-- IS-IS配置命令 \-- reset isis non-stop-routing event-log**

------------------------------------------------------------------------

![说明](IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset isis non-stop-routing event-log**]命令用来清除IS-ISNSR的日志信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[reset isis non-stop-routing event-log slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset isis non-stop-routing event-log chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：清除指定单板的IS-IS NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：清除指定成员设备的IS-IS NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**] *chassis-number* **slot** *slot-number*：清除指定成员设备上指定单板的IS-IS NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：清除指定CPU的信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 清除1号板上NSR的日志信息。

\<Sysname\> reset isis non-stop-routing event-log slot 1

**IS-IS \-- IS-IS配置命令 \-- reset isis peer**

------------------------------------------------------------------------

**[reset isis peer**]命令用来清除IS-IS指定邻居的数据结构信息。

【命令】

**[reset **]**isis peer** *system-id* [ *process-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[system-id*]：IS-IS邻居的System ID。

*[process-id*]：IS-IS进程号，取值范围为1～65535，清除指定IS-IS进程邻居的数据结构信息。

【使用指导】

本命令用在需要重建某个特定邻居的情况下使用。

【举例】

\# 清除系统ID为0000.0c11.1111的IS-IS邻居的数据结构信息。

\<Sysname\> reset isis peer 0000.0c11.1111

**IS-IS \-- IS-IS配置命令 \-- reset osi statistics**

------------------------------------------------------------------------

**[reset osi statistics**]命令用来清除OSI连接的报文统计信息。

【命令】

**[reset osi statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在某些情况下，需要统计从某个时刻开始的报文统计信息，这时必须在统计开始前清除原有的统计信息，重新进行统计。

【举例】

\# 清除OSI连接的报文统计信息。

\<Sysname\> reset osi statistics

【相关命令】

·**display osi statistics**

**IS-IS \-- IS-IS配置命令 \-- set-att**

------------------------------------------------------------------------

**[set-att**]命令用来设置系统自身发布的Level-1 LSP的ATT位。

**[undo set-att**]命令用来取消该配置。

【命令】

**[set-att**[ { **always** \| **never** }]]

**[undo set-att**]

【缺省情况】

没有设置系统自身发布的Level-1 LSP的ATT位。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[always**]：保持对Level-1 LSP的ATT位置位。

**[never**]：保持对Level-1 LSP的ATT位不置位。

【举例】

\# 设置ATT位置位。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 set-att always

**IS-IS \-- IS-IS配置命令 \-- set-overload**

------------------------------------------------------------------------

**[set-overload**]命令用来为当前路由器配置过载标志位。

**[undo set-overload**]命令用来清除过载标志位。

【命令】

**[set-overload** [ **on-startup** [ [ **start-from-nbr** *system-id* [ *timeout1* [ *nbr-timeout*  ] ] \| *timeout2* \| **wait-for-bgp**  *timeout3* ]] ]  [ **allow** { **external** \| **interlevel** } \* ]]

**[undo** **set-overload**]

【缺省情况】

不配置过载标志位。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[on-startup**]：系统启动时将过载标志位置位。

**[start-from-nbr** *system-id* [ *timeout1* [ *nbr-timeout*  ]]]：从系统启动时开始计算，如果在*nbr-timeout*参数指定的时长内仍未与指定邻居建立邻接关系完毕，过载标志位将结束置位状态；如果在*nbr-timeout*参数指定的时长内与指定邻居建立邻接关系完毕，过载标志位将继续保持置位状态，且从与指定邻居建立邻接关系时重新计时，在*timeout1*参数配置的时长内保持置位状态。

·*system-id*：指定邻居的System ID。

·*timeout1*：取值范围为5～86400秒，缺省值为600秒（10分钟）。

·*nbr-timeout*：取值范围为5～86400秒，缺省值为1200秒（20分钟）。

*[timeout2*]：从系统启动时开始计算，过载标志位保持置位状态的时间长度，取值范围为5～86400秒。缺省值为600秒（10分钟）。

**[wait-for-bgp** [ *timeout3* ]]：从系统启动时开始计算，如果在*timeout3*参数指定的时长内BGP仍未收敛，过载标志位将结束置位状态。*timeout3*取值范围为5～86400秒，缺省值为600秒（10分钟）。

**[allow**]：允许发布地址前缀。缺省情况下，当系统进入过载状态时不允许发布地址前缀。

**[external**]：当配置**allow**时，允许发布从其它协议学来的IP地址前缀。

**[interlevel**]：当配置**allow**时，允许发布从不同层次学来的IP地址前缀。

【使用指导】

·如果没有指定**on-startup**参数，IS-IS将立即把过载标志位置位且一直保持置位状态直到用户通过**undo** **set-overload**清除过载标志位。

·如果只指定**on-startup**参数，过载标志位将在系统启动时开始置位，并且在*timeout2*参数指定的时长内保持置位状态。

【举例】

\# 在当前路由器上配置过载标志位。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 set-overload

**IS-IS \-- IS-IS配置命令 \-- snmp context-name**

------------------------------------------------------------------------

**[snmp**] **context-name**命令用来配置管理IS-IS的SNMP实体所使用的上下文名称。

**[undo** **snmp** ]**context-name**命令用来恢复缺省情况。

【命令】

**[snmp**] **context-name** *context-name*

**[undo** **snmp** ]**context-name**

【缺省情况】

没有配置管理IS-IS的SNMP实体所使用的上下文名称。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：上下文的名称，为1～32个字符的字符串，区分大小写。

【使用指导】

TRILL使用IS-IS的MIB（Management Information Base，管理信息库）对NMS（Network Management System，网络管理系统）提供TRILL对象的管理，但标准IS-IS MIB中定义的MIB为单实例管理对象，无法同时对IS-IS和TRILL进行管理。因此，参考RFC 4750中对OSPF多实例的管理方法，为管理TRILL定义一个上下文名称，以区分来自NMS的SNMP请求是要对IS-IS还是TRILL进行管理。需要注意的是，由于上下文名称只是SNMPv3独有的概念，因此对于SNMPv1/v2c，会将团体名映射为上下文名称以对不同协议进行区分。

【举例】

\# 配置管理IS-IS进程1的SNMP实体所使用的上下文名称为isis。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 snmp context-name isis

**IS-IS \-- IS-IS配置命令 \-- snmp-agent trap enable isis**

------------------------------------------------------------------------

**[snmp-agent trap enable isis**]命令用来开启IS-IS的告警功能。

**[undo snmp-agent trap enable isis**]命令用来关闭IS-IS的告警功能。

【命令】

**[snmp-agent trap enable isis**[ [ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-corrupt** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **manual-address-drop** \| **max-seq-exceeded** \| **maxarea-mismatch** \| **own-lsp-purge** \| **protocol-support**  \| **rejected-adjacency** \| **skip-sequence-number** \| **version-skew** ] \*]]

**[undo snmp-agent trap enable isis**[ [ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-corrupt** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **manual-address-drop** \| **max-seq-exceeded** \| **maxarea-mismatch** \| **own-lsp-purge** \| **protocol-support**  \| **rejected-adjacency** \| **skip-sequence-number** \| **version-skew** ] \*]]

【缺省情况】

IS-IS的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adjacency-state-change**]：IS-IS邻居状态变化。

**[area-mismatch**]：Hello报文区域地址不匹配。

**[authentication**]：IS-IS报文认证失败。

**[authentication-type**]：IS-IS报文认证类型错误。

**[buffsize-mismatch**]：LSP报文长度和产生缓冲区大小不匹配。

**[id-length-mismatch**]：IS-IS报文中System ID长度不匹配。

**[lsdboverload-state-change**]：LSDB过载状态变化。

**[lsp-corrupt**]：LSP在LSDB中校验和错误。

**[lsp-parse-error**]：LSP报文解析错误。

**[lsp-size-exceeded**]：超大的LSP报文导致泛洪失败。

**[manual-address-drop**]：手动配置区域地址丢弃。

**[max-seq-exceeded**]：LSP序列号超过最大序列号。

**[maxarea-mismatch**]：最大配置区域地址数不匹配。

**[own-lsp-purge**]：尝试清除本地LSP。

**[protocol-support**]：报文协议支持类型不匹配。

**[rejected-adjacency**]：Hello报文邻接不匹配丢弃。

**[skip-sequence-number**]：跳过已经产生过的LSP序列号。

**[version-skew**]：Hello报文版本号不匹配。

【使用指导】

·如果未指定任何参数，将开启IS-IS所有类型的告警功能。

·如果配置时不存在任何IS-IS进程，将会提示无IS-IS进程，并不允许配置。

·如果删除了所有配置的IS-IS进程，则本功能不生效。

【举例】

\# 关闭IS-IS的告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable isis

**IS-IS \-- IS-IS配置命令 \-- summary**

------------------------------------------------------------------------

**[summary**]命令用来配置一条聚合路由。

**[undo summary**]命令用来删除指定的聚合路由。

【命令】

**[summary ***ip-address *[{ *mask-length* \| *mask* } [ **avoid-feedback** \| **generate_null0_route** \| [ **level-1** \| **level-1-2** \| **level-2** ] \| **tag** *tag* ] \*]]

**[undo summary ***ip-address *[{ *mask-length* \| *mask* } [ **level-1** \| **level-1-2** \| **level-2** ]]]

【缺省情况】

没有对路由进行聚合。

【视图】

IS-IS IPv4单播地址族视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：聚合路由的目的IP地址。

*[mask-length*]：聚合路由的网络掩码长度，取值范围为0～32。

*[mask*]：聚合路由的网络掩码，点分十进制格式。

**[avoid-feedback**]：避免通过路由计算学习到聚合路由。

**[generate_null0_route**]：为防止路由循环而生成NULL0路由。

**[level-1**]：只对引入到Level-1区域的路由进行聚合。

**[level-1-2**]：对引入到Level-1和Level-2区域的路由都进行聚合。

**[level-2**]：只对引入到Level-2区域的路由进行聚合。

**[tag ***tag*]：管理标记，取值范围为1～4294967295。

【使用指导】

如果不输入**level**参数，则默认只对**level-2**的路由进行聚合。

如果没有指定拓扑名，则只对标准拓扑的路由进行聚合。

通过路由聚合，一方面可以减小路由表规模，还可以减少本路由器生成的LSP报文大小和LSDB的规模。其中，被聚合的路由可以是IS-IS协议发现的路由，也可以是引入的外部路由。另外，聚合后路由的开销值取所有被聚合路由中最小的开销值。

需要注意的是，路由器只对本地生成的LSP中的路由进行聚合。

【举例】

\# 配置一条202.0.0.0/8的聚合路由。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv4

Sysname-isis-1-ipv4 summary 202.0.0.0 255.0.0.0

**IS-IS \-- IS-IS配置命令 \-- timer lsp-generation**

------------------------------------------------------------------------

**[timer lsp-generation**]命令用来配置LSP重新生成的时间间隔。

**[undo timer lsp-generation**]命令用来取消该配置。

【命令】

**[timer lsp-generation ***maximum-interval* [ *minimum-interval* [ *incremental-interval*    **level-1** \| **level-2** ]]]

**[undo timer lsp-generation**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

LSP重新生成的最大时间间隔为5秒，最小时间间隔为50毫秒，时间间隔惩罚增量为200毫秒。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：网络拓扑变化导致LSP重新生成时，LSP生成的最大时间间隔，取值范围为1～120，单位为秒。

*[minimum-interval*]：网络拓扑变化导致LSP重新生成时，LSP生成的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：网络拓扑变化导致LSP重新生成时，LSP生成的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

**[level-1**]：配置Level-1 LSP生成时间间隔。

**[level-2**]：配置Level-2的LSP生成时间间隔，默认不配置级别时对Level-1和Level-2同时起作用。

【使用指导】

通过调节LSP重新生成的时间间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。在网络变化不频繁的情况下，将LSA重新生成时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

需要注意的是，*minimum-interval*和*incremental-interva*l配置值不允许大于*maximum-interval*配置值。

【举例】

\# 配置IS-IS LSP重新生成的最大时间间隔为10秒，最小时间间隔为100毫秒，时间间隔惩罚增量为200毫秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 timer lsp-generation 10 100 200

**IS-IS \-- IS-IS配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

**[timer lsp-max-age**]命令用来配置当前路由器生成的LSP在LSDB里的最大生存时间。

**[undo timer lsp-max-age**]命令用来恢复缺省情况。

【命令】

**[timer lsp-max-age ***second*s]

**[undo timer lsp-max-age**]

【缺省情况】

当前路由器生成的LSP在LSDB里的最大生存时间为1200秒。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：LSP在LSDB里的最大生存时间，取值范围是1～65535，单位为秒。

【使用指导】

每个LSP都有一个最大生存时间，随着时间的推移最大生存时间将逐渐减小，当LSP的最大生存时间为0时，IS-IS将启动清除过期LSP的过程。用户可根据网络规模对LSP的最大生存时间进行调整。

【举例】

\# 配置当前路由器生成的LSP在LSDB里的最大生存时间为25分钟，即1500秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 timer lsp-max-age 1500

【相关命令】

·**timer lsp-refresh**

**IS-IS \-- IS-IS配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

**[timer lsp-refresh**]命令用来配置LSP刷新周期。

**[undo timer lsp-refresh**]命令用来恢复缺省情况。

【命令】

**[timer lsp-refresh ***second*s]

**[undo** **timer lsp-refresh**]

【缺省情况】

LSP刷新周期为900秒。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[second*s]：LSP刷新周期，取值范围为1～65534，单位为秒。

【使用指导】

路由器必须定时刷新自己生成的LSP，防止LSP的最大生存时间减小为0。另外，通过定时刷新LSP可以使整个区域中的LSP保持同步。用户可对LSP的刷新周期进行配置，提高LSP的刷新频率可以加快网络收敛速度，但是将占用更多的带宽。

**[timer lsp-refresh**]命令配置的时间必须小于**timer lsp-max-age**命令配置的时间，以保证在LSP失效前进行刷新。

【举例】

\# 配置当前系统的LSP刷新周期为1500秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 timer lsp-refresh 1500

【相关命令】

·**timer lsp-max-age**

**IS-IS \-- IS-IS配置命令 \-- timer spf**

------------------------------------------------------------------------

**[timer spf**]命令用来配置IS-IS路由计算[的时间间隔。]

**[undo timer spf**]命令用来恢复缺省情况。

【命令】

**[timer spf ***maximum-interval***** *minimum-interval*  *incremental-interval*  ]

**[undo timer spf**]

【缺省情况】

IS-IS路由计算的最大时间间隔为5秒，最小时间间隔为50毫秒，时间间隔惩罚增量为200毫秒。

【视图】

IS-IS视图/IS-IS IPv4单播拓扑视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：IS-IS路由计算的最大时间间隔，取值范围为1～120，单位为秒。

*[minimum-interval*]：IS-IS路由计算的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：IS-IS路由计算的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

根据本地维护的LSDB，运行IS-IS协议的路由器通过SPF算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。

本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

需要注意的是，*minimum-interval*和*incremental-interval*配置值不允许大于*maximum-interval*配置值。

【举例】

\# 配置路由器Sysname的IS-IS路由计算的最大时间间隔为10秒，最小时间间隔为100毫秒，惩罚增量为300毫秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 timer spf 10 100 300

**IS-IS \-- IS-IS配置命令 \-- topology**

------------------------------------------------------------------------

**[topology**]命令用来创建并进入IS-IS IPv4单播拓扑视图。

**[undo topology**]命令用来删除该视图下的所有配置。

【命令】

**[topology ***topo-name***** **tid** *tid* ]

**[undo topology ***topo-name*]

【缺省情况】

没有创建IS-IS IPv4单播拓扑视图。

【视图】

IS-IS IPv4单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[topo-name*]：拓扑名，为1～31个字符的字符串，区分大小写。

*[tid*]：拓扑号，取值范围为6～4095。

【使用指导】

拓扑名**base**已经为标准拓扑保留，在此处不能配置。

本命令必须在配置了对应的IPv4子拓扑后才能生效。

本命令必须在链路开销值类型为**wide****、compatible**或**wide-compatible**时才能配置。

【举例】

\# 创建并进入IS-IS IPv4单播拓扑voice（4000）视图。

\<Sysname\> system-view

Sysname isis 100

Sysname-isis-100 address-family ipv4

Sysname-isis-100-ipv4 topology voice tid 4000

Sysname-isis-100-ipv4-topo-voice

【相关命令】

·**cost-style**

**IS-IS \-- IS-IS配置命令 \-- virtual-system**

------------------------------------------------------------------------

**[virtual-system**]命令用来配置IS-IS进程的虚拟系统ID。

**[undo virtual-system**]命令用来删除虚拟系统ID。

【命令】

**[virtual-system** *virtual-system-id*]

**[undo virtual-system** *virtual-system-id*]

【缺省情况】

没有配置IS-IS进程的虚拟系统ID。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-system-id*]：IS-IS进程的虚拟系统ID。

【举例】

\# 配置IS-IS进程1的虚拟系统ID为2222.2222.2222。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 virtual-system 2222.2222.2222

