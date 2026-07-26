
**以太网接口 \-- 以太网接口通用配置命令 \-- alarm-detect**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[alarm-detect**]命令用来配置10GE接口工作在WAN模式下时，接口的告警联动动作。

**[undo alarm-detect**]命令用来取消告警联动动作。

【命令】

**[alarm-detect**[ { **rdi** \| **sd** \| **sf** } **action link-down**]]

**[undo alarm-detect**[ { **rdi** \| **sd** \| **sf** }]]

【缺省情况】

接口不执行任何告警联动动作。

【视图】

Ten-GigabitEthernet接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rdi**]：表示RDI（Remote Defect Indication，远端失效指示）告警。

**[sd**]：表示SD（Signal Degrade，信号衰减）告警。

**[sf**]：表示SF（Signal Fail，信号失败）告警。

**[action link-down**]：表示当接口检测到告警时，会自动将接口的物理状态设置为down。

【使用指导】

当设备收到对端发送的MS-RDI信号时，则认为发生了RDI（Remote Defect Indication，远端失效指示）告警。当设备收到的报文的误码率超过设置的门限时，则生成SD告警或SF告警。SD告警和SF告警的门限可通过**threshold**命令设置。

配置本命令后，当设备检测到SD告警/SF告警/RDI告警时，会自动将接口的物理状态设置为down。

【举例】

\# 配置当Ten-GigabitEthernet1/1/1接口检测到SD告警时，自动将接口的物理状态设置为down。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/1/1

Sysname-Ten-GigabitEthernet1/1/1 port-mode wan

Sysname-Ten-GigabitEthernet1/1/1 alarm-detect sd action link-down

【相关命令】

·**port-mode**

·**threshold**

**以太网接口 \-- 以太网接口通用配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth** *bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的最大速率÷1000（kbit/s）。

【视图】

以太网接口视图/以太网子接口视图

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

\# 配置接口GigabitEthernet1/0/1的期望带宽为1000kbit/s。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 bandwidth 1000

\# 设置以太网子接口GigabitEthernet1/0/1.1的期望带宽为1000kbit/s。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 bandwidth 1000

【相关命令】

·**speed**

**以太网接口 \-- 以太网接口通用配置命令 \-- combo enable**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[combo** **enable**]命令用来激活Combo接口中的电口或者光口。

【命令】

**[combo**[ **enable** { **copper** \| **fiber** }]]

【缺省情况】

电口被激活。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[copper**]：表示该Combo接口的电口被激活，请使用双绞线连接。

**[fiber**]：表示该Combo接口的光口被激活，请使用光纤连接。

【使用指导】

Combo接口是一个逻辑接口，一个Combo接口物理上对应设备面板上一个电口和一个光口。电口与其对应的光口是光电复用关系，两者不能同时工作（当激活其中的一个接口时，另一个接口就自动处于关闭状态），用户可根据组网需求选择使用电口或光口。

请根据设备面板上的标识了解设备上有哪些Combo接口以及每个Combo接口的编号。

【举例】

\# 指定GigabitEthernet1/0/1端口的电口被激活。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 combo enable copper

\# 指定GigabitEthernet1/0/1端口的光口被激活。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 combo enable fiber

**以太网接口 \-- 以太网接口通用配置命令 \-- dampening**

------------------------------------------------------------------------

**[dampening**]命令用来开启接口的dampening功能。

**[undo dampening**]命令用来恢复缺省情况。

【命令】

**[dampening ** *half-life* *reuse suppress max-suppress-time* ]

**[undo dampening**]

【缺省情况】

接口的dampening功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[half-life*]：半衰期，取值范围为1～120，单位为秒，缺省值为54秒。

*[reuse*]：启用值，取值范围为200～20000，缺省值为750，必须要小于*suppress*的值。

*[suppress*]：抑制门限，取值范围为200～20000，缺省值为2000。

*[max-suppress-time*]：最大抑制时间，取值范围为1～255，单位为秒，缺省值为半衰期的3倍，即162秒。

【使用指导】

接口有两种物理连接状态：up和down。由于线缆故障、接口连接或链路层配置错误等问题，可能会导致设备接口的状态频繁的在down和up之间切换，这种现象称为接口震荡。随着接口状态的频繁改变，设备会不停的刷新相关表项（比如路由表），消耗大量的系统资源。通过在接口上配置dampening功能，可以在一定条件下，屏蔽该接口的震荡对路由等上层业务的影响。此时若出现接口震荡，将不上送CPU处理，仅产生对应的Trap和Log信息，从而节省系统资源的消耗。

最大惩罚值与最大抑制时间、半衰期、启用值之间遵循公式：最大惩罚值＝2^(^^最大抑制时间/半衰期)^×启用值，其中最大惩罚值不可配。

开启dampening功能后，各参数运行情况：

·接口将对应一个惩罚值，初始值是0。接口状态每次从up变到down时，惩罚值会增加1000（接口状态从down变到up时，惩罚值不变）。同时，惩罚值随时间推移自动减少，满足半衰期衰减规律：完全衰减时（假如没有接口震荡），经过一个半衰周期，惩罚值减少为原来值的一半（软件模拟的半衰期，取样时间是1秒，惩罚值的递减在每个取样定时器中操作。开启dampening的同时会创建并激活取样定时器，只有执行**undo dampening**命令才会删除定时器）。

·当惩罚值大于或等于抑制门限时，开始抑制接口：不上送CPU处理接口状态变化，仅产生对应的Trap和Log信息。当惩罚值小于或等于启用门限时，不抑制接口：上送CPU处理接口状态变化，同时发送对应的Trap和Log信息。

·当惩罚值达到最大惩罚值后，惩罚值将不再增加。每次接口进入抑制状态后，持续抑制的时间超过最大抑制时间时，惩罚值不再增加，此时惩罚值进入完全半衰期（此阶段接口状态变化不会增加惩罚值），直到惩罚值小于启用值，不再抑制接口（完全半衰时，接口仍然处于抑制状态，但完全半衰阶段时间不算入持续抑制时间）。

·如果接口抑制时间不到最大抑制时间，惩罚值就小于启用值，那么不存在完全半衰过程（持续抑制时间超过最大抑制时间才会进入）。

需要注意的是：

·以太网接口上不能同时配置本命令和**link-delay**命令。

·本命令对使用**shutdown**命令手动关闭的接口无效。

·手工**shutdown**接口时，dampening的惩罚值恢复为初始值0。

·对于使能了RRPP、MSTP或Smart Link的接口不建议使用该命令。

·配置该命令时，如果不指定任何参数，开启的dampening功能将采用缺省值。

【举例】

\# 按照缺省值开启接口GigabitEthernet1/0/1的dampening功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dampening

\# 开启接口GigabitEthernet1/0/1的dampening功能，配置半衰期为2秒，启用值为800，抑制门限为3000，最大抑制时间为5秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dampening 2 800 3000 5

【相关命令】

·**display interface**

·**link-delay**

**以太网接口 \-- 以太网接口通用配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前接口的缺省配置。

【命令】

**[default**]

【视图】

以太网接口视图/以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将以太网接口GigabitEthernet1/0/1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 default

\# 将以太网子接口GigabitEthernet1/0/1.1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 default

**以太网接口 \-- 以太网接口通用配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，例如：GigabitEthernet1/0/1 Interface。

【视图】

以太网接口视图/以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口的描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 设置以太网接口GigabitEthernet1/0/1的描述信息为"lan-interface"。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 description lan-interface

\# 设置以太网子接口GigabitEthernet1/0/1.1的描述信息为"subinterface1/0/1.1"。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 description subinterface1/0/1.1

**以太网接口 \-- 以太网接口通用配置命令 \-- display counters**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display counters**]命令用来显示接口的流量统计信息。

【命令】

**[display counters **[{ **inbound** \| **outbound** } **interface** [ *interface-type* [ *interface-number* \| *interface-number.subnumber* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]：显示输入报文的流量统计信息。

**[outbound**]：显示输出报文的流量统计信息。

*[interface-type*]：指定接口类型。

*[interface-number*]：指定接口编号。

*[interface-number.subnumber*]：指定子接口。其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为1～4094。

【使用指导】

·本命令显示的是统计周期内报文的数量，统计周期可以通过**flow-interval**命令进行设置。

·可通过命令**reset counters interface**清除以太网接口的统计信息，具体指导请参见**reset counters interface**命令描述。

·如果不指定*interface-type*，则显示所有可统计的接口的流量统计信息。

·如果指定*interface-type*而不指定*interface-number*/*interface-number.subnumber*，则显示该类型下所有接口的流量统计信息。

·如果同时指定*interface-type*和*interface-number*/*interface-number.subnumber*，则显示指定接口/子接口的报文流量统计信息。

【举例】

\# 显示Ethernet类型接口的报文输入流量统计信息。

\<Sysname\> display counters inbound interface gigabitethernet

Interface            Total (pkts)    Broadcast (pkts)    Multicast (pkts)  Err (pkts)

GE1/0/1                       100                 100                   0           0

GE1/0/2                         0                   0                   0           0

GE1/0/3                  Overflow            Overflow            Overflow    Overflow

GE1/0/4                         0                   0                   0           0

 Overflow: More than 14 digits (7 digits for column \"Err\").

       \--: Not supported.

表1-1 display counters命令显示信息描述表

字段

描述

Interface

接口名称缩写

Total (pkts)

接口接收或发送报文的总数（单位为包）

Broadcast (pkts)

接口接收或发送广播报文的总数（单位为包）。RPR物理端口不对广播报文单独进行统计，而是将广播报文视为组播报文来统计

Multicast (pkts)

接口接收或发送组播报文的总数（单位为包）。RPR物理端口不对广播报文单独进行统计，而是将广播报文视为组播报文来统计

Err (pkts)

接口接收或发送错误报文的总数（单位为包）

Overflow: More than 14 digits (7 digits for column \"Err\").

当某个统计信息的值为Overflow时，表示该项数据的长度超过了显示范围：

·对于Err项，Overflow表示数据的长度超过了7位十进制数

·对于其它项，Overflow表示数据的长度超过了14位十进制数

\--: Not supported.

当某个统计信息的值为"\--"时，表示设备不支持该项数据的统计

【相关命令】

·**flow-interval**

·**reset counters interface**

**以太网接口 \-- 以太网接口通用配置命令 \-- display counters rate**

------------------------------------------------------------------------

**[display counters rate**]命令用来显示最近一个统计周期内处于up状态的接口的报文速率统计信息。

【命令】

**[display counters rate **[{ **inbound** \| **outbound** } **interface** [ *interface-type* [ *interface-number* \| *interface-number.subnumber* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[inbound**]**：**显示报文接收速率统计信息。

**[outbound**]**：**显示报文发送速率统计信息。

*[interface-type*]：指定接口类型。

*[interface-number*]：指定接口编号。

*[interface-number.subnumber*]：指定子接口编号。其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为1～4094。

【使用指导】

·如果不指定*interface-type*和*interface-number*，则显示所有可统计的接口类型中最近一个统计周期内处于up状态的接口的报文速率统计信息。

·如果指定*interface-type*而不指定*interface-number*，则显示该类型下最近一个统计周期内处于up状态接口的报文速率统计信息。

·如果同时指定*interface-type*和*interface-number*，则显示指定接口在最近一个统计周期内报文速率统计信息。如果该接口在最近一个统计周期内一直处于down状态，则提示接口不支持该操作。

关于统计周期的值，分为以下几种情况：

·不支持**flow-interval**命令的设备，统计周期固定为5分钟。

·对于支持**flow-interval**命令的设备，统计周期可以通过**flow-interval**命令来配置。

【举例】

\# 显示GigabitEthernet类型接口的报文接收速率统计信息。

\<Sysname\> display counters rate inbound interface gigabitethernet

Interface               Total (pps)       Broadcast (pps)       Multicast (pps)

GE1/0/1                         200                   100                   100

GE1/0/2                         300                   200                   100

GE1/0/3                         300                   200                   100

 Overflow: More than 14 digits.

       \--: Not supported.

表1-2 display counters rate命令显示信息描述表

字段

描述

Interface

接口名称缩写

Total (pps)

在最近一个统计周期内，接口接收或发送所有类型报文的平均速率（单位为包/秒）

Broadcast (pps)

在最近一个统计周期内，接口接收或发送广播报文的平均速率（单位为包/秒）。RPR物理端口不对广播报文单独进行统计，而是与组播报文一起都按照组播报文进行统计

Multicast (pps)

在最近一个统计周期内，接口接收或发送组播报文的平均速率（单位为包/秒）。RPR物理端口不对广播报文单独进行统计，而是与组播报文一起都按照组播报文进行统计

Overflow: More than 14 digits.

当某个统计信息的值为Overflow时，表示该项数据的长度超过了14位十进制数

\--: Not supported.

当某个统计信息的值为"\--"时，则表示设备不支持该项数据的统计

【相关命令】

·**flow-interval**

·**reset counters interface**

**以太网接口 \-- 以太网接口通用配置命令 \-- display ethernet statistics**

------------------------------------------------------------------------

**[display ethernet statistics**]命令用来显示以太网软件模块收发报文的统计信息。

【命令】

集中式设备：

**[display ethernet statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ethernet statistics** **slot** *slot-number* [ **cpu** v*cpu-numbe* ]]

分布式设备－IRF模式：

**[display ethernet statistics chassis ***chassis-number ***slot*** slot-number * **cpu** v*cpu-numbe* ]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot ***slot-number*]：显示指定单板的统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备或者PEX的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板/PEX的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟槽位号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的统计信息，*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示以太网软件模块收发报文的统计信息。（集中式设备）

\<Sysname\> display ethernet statistics

ETH receive packet statistics:

    Totalnum        : 10447          ETHIINum     : 4459

    SNAPNum         : 0              RAWNum       : 0

    LLCNum          : 0              UnknownNum   : 0

    ForwardNum      : 4459           ARP          : 0

    MPLS            : 0              ISIS         : 0

    ISIS2           : 0              IP           : 0

    IPV6            : 0

ETH receive error statistics:

    NullPoint       : 0              ErrIfindex   : 0

    ErrIfcb         : 0              IfShut       : 0

    ErrAnalyse      : 5988           ErrSrcMAC    : 5988

    ErrHdrLen       : 0

ETH send packet statistics:

    L3OutNum        : 211            VLANOutNum   : 0

    FastOutNum      : 155            L2OutNum     : 0

ETH send error statistics:

    MbufRelayNum    : 0              NullMbuf     : 0

    ErrAdjFwd       : 0              ErrPrepend   : 0

    ErrHdrLen       : 0              ErrPad       : 0

    ErrQoSTrs       : 0              ErrVLANTrs   : 0

    ErrEncap        : 0              ErrTagVLAN   : 0

    IfShut          : 0              IfErr        : 0

\# 显示以太网软件模块关于2号单板收发报文的统计信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display ethernet statistics slot 2

ETH receive packet statistics:

    Totalnum        : 10447          ETHIINum     : 4459

    SNAPNum         : 0              RAWNum       : 0

    LLCNum          : 0              UnknownNum   : 0

    ForwardNum      : 4459           ARP          : 0

    MPLS            : 0              ISIS         : 0

    ISIS2           : 0              IP           : 0

    IPV6            : 0

ETH receive error statistics:

    NullPoint       : 0              ErrIfindex   : 0

    ErrIfcb         : 0              IfShut       : 0

    ErrAnalyse      : 5988           ErrSrcMAC    : 5988

    ErrHdrLen       : 0

ETH send packet statistics:

    L3OutNum        : 211            VLANOutNum   : 0

    FastOutNum      : 155            L2OutNum     : 0

ETH send error statistics:

    MbufRelayNum    : 0              NullMbuf     : 0

    ErrAdjFwd       : 0              ErrPrepend   : 0

    ErrHdrLen       : 0              ErrPad       : 0

    ErrQoSTrs       : 0              ErrVLANTrs   : 0

    ErrEncap        : 0              ErrTagVLAN   : 0

    IfShut          : 0              IfErr        : 0

\# 显示以太网软件模块关于成员设备1上1号单板收发报文的统计信息。（分布式设备－IRF模式）

\<Sysname\> display ethernet statistics chassis 1 slot 1

ETH receive packet statistics:

    Totalnum        : 10447          ETHIINum     : 4459

    SNAPNum         : 0              RAWNum       : 0

    LLCNum          : 0              UnknownNum   : 0

    ForwardNum      : 4459           ARP          : 0

    MPLS            : 0              ISIS         : 0

    ISIS2           : 0              IP           : 0

    IPV6            : 0

ETH receive error statistics:

    NullPoint       : 0              ErrIfindex   : 0

    ErrIfcb         : 0              IfShut       : 0

    ErrAnalyse      : 5988           ErrSrcMAC    : 5988

    ErrHdrLen       : 0

ETH send packet statistics:

    L3OutNum        : 211            VLANOutNum   : 0

    FastOutNum      : 155            L2OutNum     : 0

ETH send error statistics:

    MbufRelayNum    : 0              NullMbuf     : 0

    ErrAdjFwd       : 0              ErrPrepend   : 0

    ErrHdrLen       : 0              ErrPad       : 0

    ErrQoSTrs       : 0              ErrVLANTrs   : 0

    ErrEncap        : 0              ErrTagVLAN   : 0

    IfShut          : 0              IfErr        : 0

表1-3 display ethernet statistics命令显示信息描述表

字段

描述

ETH receive packet statistics

以太网软件模块接收到的以太网报文的统计信息

Totalnum

接收报文的总个数

ETHIINum

接收的ETHII封装格式报文个数

SNAPNum

接收的SNAP封装格式报文个数

RAWNum

接收的RAW封装格式报文个数

ISISNum

接收的ISIS封装格式报文个数

LLCNum

接收的LLC封装格式报文个数

UnknowNum

接收的未知封装格式报文个数

ForwardNum

二层转发或上送CPU的报文个数

ARP

接收的ARP报文个数

MPLS

接收的MPLS报文个数

ISIS

接收的ISIS报文个数

ISIS2

接收的ISIS2报文个数

IP

接收的IP报文个数

IPv6

接收的IPv6报文个数

ETH receive error statistics

以太网软件模块接收错误的以太网报文的统计信息（可能是包本身包含错误或者是接收动作出错了）

NullPoint

接收报文时指针为空的报文的个数

ErrIfindex

接收报文时接口索引错误的报文个数

ErrIfcb

接收报文时接口控制块错误的报文个数

IfShut

接收报文时接口shutdown的报文个数

ErrAnalyse

接收报文时报文解析错误的报文个数

ErrSrcMAC

接收的包含源MAC地址错误的报文个数

ErrHdrLen

接收的包含报文头长度错误的报文个数

ETH send packet statistics

以太网软件模块发送的以太网报文的统计信息

L3OutNum

通过三层以太网接口发送的报文总个数

VLANOutNum

通过VLAN接口发送的报文总个数

FastOutNum

快速发送的报文总个数

L2OutNum

通过二层以太网接口发送的报文总个数

MbufRelayNum

透传发送的报文总个数

ETH send error statistics

以太网软件模块发送的错误以太网报文的统计信息

NullMbuf

发送报文时空指针错误的报文个数

ErrAdjFwd

发送报文时邻接表错误的报文个数

ErrPrepend

发送报文时扩展错误的报文个数

ErrHdrLen

发送的包含报文头长度错误的报文个数

ErrPad

发送报文时填充错误的报文个数

ErrQoSTrs

发送报文时QoS发送失败的报文个数

ErrVLANTrs

发送报文时VLAN发送失败的报文个数

ErrEncap

发送报文时封装链路头失败的报文个数

ErrTagVLAN

发送报文时封装VLAN TAG失败的报文个数

IfShut

发送报文时端口shutdown的报文个数

IfErr

发送报文时出接口错误的报文个数

【相关命令】

·**reset ethernet statistics**

**以太网接口 \-- 以太网接口通用配置命令 \-- display interface**

------------------------------------------------------------------------

**[display interface**]命令用来显示指定接口当前的运行状态和相关信息。

【命令】

**[display interface**[ [ *interface-type* [ *interface-number \| interface-number.subnumber* ]   **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type*]：指定接口类型。

*[interface-number*]：指定接口编号。

*[interface-number.subnumber*]：指定子接口编号。其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为1～4094。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定接口类型和接口编号，则显示所有接口的信息；

·如果仅指定接口类型，则显示所有该类型接口的信息；

·如果同时指定接口类型和接口编号，则显示指定接口的信息。

【举例】

\# 查看三层以太网接口GigabitEthernet1/0/1的运行状态和相关信息。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display interface gigabitethernet1/0/1

GigabitEthernet1/0/1

Current state: Administratively DOWN

Line protocol state: DOWN

Description: GigabitEthernet1/0/1 Interface

Bandwidth: 1000000kbps

Maximum Transmit Unit: 1500

Internet protocol processing: disabled

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 3822-d666-bd0c

IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 3822-d666-bd0c

Media type is twisted pair, Port hardware type is 1000_BASE_T

Port priority: 2

Loopback is not set

Unknown-speed mode, Unknown-duplex mode

Last link flapping: 6 hours 39 minutes 28 seconds

Last clearing of counters: Never

 Last 300 seconds input:  0 packets/sec 0 bytes/sec  0%

 Last 300 seconds output: 0 packets/sec 0 bytes/sec  0%

 Input  (total): 0 packets, 0 bytes

          0 broadcasts, 0 multicasts, - pauses

 Input  (normal): 0 packets, 0 bytes

          0 broadcasts, 0 multicasts, 0 pauses

 Input: 0 input errors, 0 runts, 0 giants, 0 throttles

          0 CRC, 0 frame, 0 overruns, - aborts

          - ignored, - parity errors

 Output  (total): 0 packets, 0 bytes

          0 broadcasts, 0 multicasts, - pauses

 Output  (normal): 0 packets, 0 bytes

          0 broadcasts, 0 multicasts, 0 pauses

 Output: 0 output errors, - underruns, - buffer failures

          0 aborts, 0 deferred, 0 collisions, 0 late collisions

          - lost carrier, - no carrier

 Peak value of input: 0 bytes/sec, at 2013-07-07 16:07:11

 Peak value of output: 0 bytes/sec, at 2013-07-07 16:07:11

\# 查看二层以太网接口GigabitEthernet1/0/1的运行状态和相关信息。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display interface gigabitethernet 1/0/1

GigabitEthernet1/0/1

Current state: DOWN

Line protocol state: DOWN

IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: 000c-2963-b767

Description: GigabitEthernet1/0/1 Interface

Bandwidth: 100000kbps

Loopback is not set

Media type is twisted pair,Port hardware type is 1000_BASE_T_AN_SFP

Unknown-speed mode, unknown-duplex mode

Link speed type is autonegotiation, link duplex type is autonegotiation

Flow-control is not enabled

The Maximum Frame Length is 9216

Allow jumbo frame to pass

Broadcast MAX-ratio: 100%

Multicast MAX-ratio: 100%

Unicast MAX-ratio: 100%

PVID: 1

Mdi type: automdix

Port link-type: access

 Tagged Vlan:   none

 UnTagged Vlan: 1

Port priority: 2

Last link flapping: 6 hours 39 minutes 25 seconds

Last clearing of counters:  14:34:09 Tue 11/01/2011

 Peak value of input: 0 bytes/sec, at 2013-07-17 22:06:19

 Peak value of output: 0 bytes/sec, at 2013-07-17 22:06:19

 Last 300 seconds input:  0 packets/sec 0 bytes/sec -%

 Last 300 seconds output:  0 packets/sec 0 bytes/sec -%

 Input (total):  0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

 Input (normal):  0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

 Input:  0 input errors, 0 runts, 0 giants, 0 throttles

          0 CRC, 0 frame, 0 overruns, 0 aborts

          0 ignored, 0 parity errors

 Output (total): 0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

 Output (normal): 0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

 Output: 0 output errors, 0 underruns, 0 buffer failures

          0 aborts, 0 deferred, 0 collisions, 0 late collisions

          0 lost carrier, 0 no carrier

表1-4 display interface命令显示信息描述表

字段

描述

GigabitEthernet1/0/1

接口GigabitEthernet1/0/1的相关信息

Current state

接口的物理状态，状态可能为：

·Administratively DOWN：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该端口的管理状态和物理状态均为开启

Line protocol state

接口的链路层协议状态。其值由链路层经过参数协商决定，取值为：

·UP：表示数据链路层协议状态为开启

·UP(spoofing)：表示该接口的数据链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常NULL、LoopBack等接口会具有该属性

·DOWN：表示数据链路层协议状态为关闭

·DOWN(*protocol*)：表示接口的数据链路层被一个或者多个协议模块关闭。*protocol*为DLDP、OAM、LAGG、BFD和MACSEC的任意组合，例如，DOWN(DLDP)、DOWN(DLDP, OAM)、DOWN(DLDP, OAM, LAGG)等：

¡当*protocol*中包含DLDP时，表示由于DLDP模块检测到单通而关闭接口的数据链路层

¡当*protocol*中包含OAM时，表示由于以太网OAM模块检测到远端链路故障而关闭接口的数据链路层

¡当*protocol*中包含LAGG时，表示聚合接口中没有选中的成员端口而关闭接口的数据链路层

¡当*protocol*中包含BFD时，表示由于BFD模块检测到链路故障而关闭接口的数据链路层

¡当*protocol*中包含MACSEC时，表示由于MACSEC模块还未协商成功接口的通信加密参数而关闭接口的数据链路层

Description

接口的描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口的MTU

Internet protocol processing: disabled

接口当前不能处理IP报文

Internet Address is 192.168.1.200/24 Primary

接口的主IP地址

IP Packet Frame Type

以太网帧格式，取值为PKTFMT_ETHNT_2表示报文以Ethernet II型帧格式封装

Hardware address

接口的MAC地址

IPv6 Packet Frame Type

IPv6报文发送帧格式

Media type is

接口的介质类型

Port hardware type is

接口的硬件类型

Port priority

接口优先级

Loopback is set internal

以太网接口正在进行对内环回测试，该显示信息的支持情况与用户的配置以及设备型号有关，请以设备的实际情况为准

Loopback is set external

对以太网接口进行对外环回测试，该显示信息的支持情况与用户的配置以及设备型号有关，请以设备的实际情况为准

Loopback is not set

接口上没有配置环回测试，该显示信息的支持情况与用户的配置有关，请以设备的实际情况为准

10Mbps-speed mode

接口速率为10Mbps，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

100Mbps-speed mode

接口速率为100Mbps，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

1000Mbps-speed mode

接口速率为1000Mbps，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

10Gbps-speed mode

接口速率为10Gbps，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

40Gbps-speed mode

接口速率为40Gbps，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

100Gbps-speed mode

接口速率为100Gbps，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

Unknown-speed mode

速率未知，可能因为速率协商失败或者接口物理未连通

half-duplex mode

接口工作在半双工模式，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

full-duplex mode

接口工作在全双工模式，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

unknown-duplex mode

未知双工模式，可能因为双工模式协商失败或者接口物理未连通

Link speed type is autonegotiation

当用户配置了**speed auto**时显示该信息

Link speed type is force link

当用户使用**speed**命令配置了具体的速率时显示该信息，例如10M或者100M等

link duplex type is autonegotiation

当用户配置了**duplex** **auto**时显示该信息

link duplex type is force link

当用户使用**duplex**命令配置了具体的双工模式时显示该信息，例如half或者full

Flow-control is not enabled

没有配置流量控制功能，该显示信息的支持情况与用户的配置以及链路参数的协商结果有关，请以设备的实际情况为准

The Maximum Frame Length

接口允许通过的最大以太网帧长度

Allow jumbo frame to pass

允许长帧通过

Broadcast MAX-

广播风暴抑制阈值，可能为ratio（百分比）、pps或者kbps，与用户的配置有关

Multicast MAX-

组播风暴抑制阈值，可能为ratio（百分比）、pps或者kbps，与用户的配置有关

Unicast MAX-

未知单播风暴抑制阈值，可能为ratio（百分比）、pps或者kbps，与用户的配置有关

PVID

接口所在的缺省VLAN ID

Mdi type

网线类型，取值为automdix、mdi或mdix，与用户的配置有关

Port link-type

链路类型，取值为access、trunk或hybrid，与用户的配置有关

Tagged Vlan

通过该接口后携带Tag的VLAN

UnTagged Vlan

通过该接口后不再携带Tag的VLAN

Port priority

接口优先级，该信息的支持情况与设备的型号有关，请以设备的实际情况为准

Last link flapping

接口最近一次物理状态改变到现在的时长。Never表示接口从设备启动后一直处于down状态（没有改变过）

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间（如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never）

Last 300 seconds input:  0 packets/sec 0 bytes/sec 0%

Last 300 seconds output:  0 packets/sec 0 bytes/sec 0%

端口在最近300秒接收和发送报文的平均速率，单位分别为数据包/秒和字节/秒，以及实际速率和接口带宽的百分比

如果值显示为"-"，则表示不支持该统计项。"-"的支持情况与设备的型号有关，请以设备的实际情况为准

Input(total):  0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

端口接收报文的统计值，包括正常报文、异常报文和正常PAUSE帧的报文数、字节数

端口接收的单播报文、广播报文、组播报文和PAUSE帧的数量

如果值显示为"-"，则表示不支持该统计项

Input(normal):  0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

端口接收的正常报文的统计值，包括正常报文和正常PAUSE帧的报文数、字节数

端口接收的正常单播报文、广播报文、组播报文和PAUSE帧的数量

如果值显示为"-"，则表示不支持该统计项

input errors

端口接收的错误报文的统计值

runts

接收到的超小帧的数量

超小帧是指长度小于64字节、格式正确且包含有效的CRC字段的帧

giants

接收到的超大帧的数量

超大帧是指有效长度大于端口允许通过最大报文长度的帧：

·对于禁止长帧通过的以太网端口，超大帧是指有效长度大于1518字节（不带VLAN Tag）或大于1522字节（带VLAN Tag报文）的帧

·对于允许长帧通过的以太网端口，超大帧是指有效长度大于指定最大长帧长度的帧

throttles

接收到的长度为非整数字节的帧的个数

CRC

接收到的CRC校验错误、长度正常的帧的数量

frame

接收到的CRC校验错误、且长度不是整字节数的帧的数量

overruns

当端口的接收速率超过接收队列的处理能力时，导致报文被丢弃

aborts

接收到的非法报文总数，非法报文包括：

·报文碎片：长度小于64字节（长度可以为整数或非整数）且CRC校验错误的帧

·jabber帧：有效长度大于端口允许通过的最大报文长度，且CRC校验错误的帧（长度可以为整字节数或非整字节数）。如对于禁止长帧通过的以太网端口，jabber帧是指大于1518（不带VLAN Tag）或1522（带VLAN Tag）字节，且CRC校验错误的帧；对于允许长帧通过的以太网端口，jabber帧是指有效长度大于指定最大长帧长度，且CRC校验错误的帧

·符号错误帧：报文中至少包含1个错误的符号

·操作码未知帧：报文是MAC控制帧，但不是Pause帧

·长度错误帧：报文中802.3长度字段与报文实际长度（46～1500字节）不匹配

ignored

由于端口接收缓冲区不足等原因而丢弃的报文数量

parity errors

接收到的奇偶校验错误的帧的数量

Output(total): 0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

端口发送报文的统计值，包括正常报文、异常报文和正常PAUSE帧的报文数、字节数

端口发送的单播报文、广播报文、组播报文和PAUSE帧的数量

如果值显示为"-"，则表示不支持该统计项

Output(normal): 0 packets, 0 bytes

          0 unicasts, 0 broadcasts, 0 multicasts, 0 pauses

端口发送的正常报文的统计值，包括正常报文和正常PAUSE帧的报文数、字节数

端口发送的正常单播报文、广播报文、组播报文和PAUSE帧的数量

如果值显示为"-"，则表示不支持该统计项

output errors

各种发送错误的报文总数

underruns

当端口的发送速率超过了发送队列的处理能力，导致报文被丢弃，是一种非常少见的硬件异常

buffer failures

由于端口发送缓冲区不足而丢弃的报文数量

aborts

发送失败的报文总数，即报文已经开始发送，但由于各种原因（如冲突）而导致发送失败

deferred

延迟报文的数量，延迟报文是指发送前检测到冲突而被延迟发送的报文

collisions

冲突帧的数量，冲突帧是指在发送过程中检测到冲突的而停止发送的报文

late collisions

延迟冲突帧的数量，延迟冲突帧是指帧的前512 bits已经被发送，由于检测到冲突，该帧被延迟发送

lost carrier

载波丢失，一般适用于串行WAN接口，发送过程中，每丢失一个载波，此计数器加一

no carrier

无载波，一般适用于串行WAN接口，当试图发送帧时，如果没有载波出现，此计数器加一

Peak value of input

接口输入流量的峰值速率大小（单位为bytes/sec）以及峰值产生的时间

Peak value of output

接口输出流量的峰值速率大小（单位为bytes/sec）以及峰值产生的时间

\# 显示所有接口的概要信息。

\<Sysname\> display interface brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) -- spoofing

Interface            Link Protocol Main IP         Description

GE1/0/0              UP   UP       10.1.1.2        Link to CoreRouter

GE1/0/1              DOWN DOWN     \--

Loop0                UP   UP(s)    2.2.2.9

NULL0                UP   UP(s)    \--

Vlan1                UP   DOWN     \--

Vlan999              UP   UP       192.168.1.42

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

GE1/0/2              DOWN auto    A      A    1

GE1/0/3              UP   100M(a) F(a)   A    1    aaaaaaaaaaaaaaaaaaaaaaaaaaa

GE1/0/4              DOWN auto    A      A    1

GE1/0/5              DOWN auto    A      A    1

GE1/0/6              UP   100M(a) F(a)   A    1

GE1/0/7              DOWN auto    A      A    1

GE1/0/8              UP   100M(a) F(a)   A    1

GE1/0/9              UP   100M(a) F(a)   A    999

\# 显示接口GigabitEthernet1/0/3的概要信息，包括用户配置的全部描述信息。

\<Sysname\> display interface gigabitethernet 1/0/3 brief description

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

GE1/0/3              UP   100M(a) F(a)   A    1    aaaaaaaaaaaaaaaaaaaaaaaaaaaaa

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

\# 显示当前物理状态为down的接口的信息以及down的原因。

\<Sysname\> display interface brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

GE1/0/1              DOWN Not connected

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

GE1/0/2              DOWN Not connected

GE1/0/4              DOWN Not connected

GE1/0/5              DOWN Not connected

GE1/0/7              DOWN Not connected

表1-5 display interface brief命令显示信息描述表

字段

描述

Brief information on interface(s) under route mode:

三层模式下（route）接口的概要信息，即三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack等接口会具有该属性

Interface

接口名称缩写

Link

接口物理连接状态，取值为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Protocol

接口数据链路层协议状态，取值为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack等接口会取该值

Main IP

接口主IP地址。当显示"\--"时，表示接口下还没有配置IP地址

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

The brief information of interface(s) under bridge mode:

二层模式下（bridge）的接口概要信息，即二层接口的概要信息

Speed or Duplex: (a)/A - auto; H - half; F - full

如果某接口的Speed属性值为"(a)"，则表示该接口的速率是通过自动协商获取的

如果某接口的Duplex属性值为"(a)"或者"A"，则表示该接口的Duplex属性是通过自动协商获取的；取值为"H"则表示为半双工；取值为"F"则表示为全双工

Type: A - access; T - trunk; H - hybrid

接口的链路类型，

·A：表示Access链路类型

·H：表示Hybrid链路类型

·T：表示Trunk链路类型

Speed

接口的速率，单位为bps

Duplex

接口的双工模式，取值为：

·A：表示双工模式由自动协商结果决定

·F：表示全双工

·F(a)：表示自由协商的结果为全双工

·H：表示半双工

·H(a)：表示自由协商的结果为半双工

Type

链路类型，取值为：

·A：表示Access链路类型

·H：表示Hybrid链路类型

·T：表示Trunk链路类型

PVID

接口所在的缺省VLAN ID

Cause

接口物理连接状态为down的原因，取值为（不同型号的设备支持的取值不同，请以设备的实际情况为准）：

·Administratively：表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

·DOWN ( Link-Aggregation interface down )：聚合接口被关闭后，该聚合接口的所有成员端口的状态会显示为DOWN，down的原因会显示为DOWN ( Link-Aggregation interface down )

·DOWN (Loopback detection down)：由于环路检测模块检测到环路而自动关闭接口

·DOWN ( Monitor-Link uplink down )：由于Monitor Link模块检测到上行链路down而自动关闭接口

·IRF-link-down：当IRF链路检测功能检测到某成员设备上某MDC中的IRF链路状态为DOWN时，会将该成员设备上这个MDC中除了保留接口外的所有物理接口状态设置为DOWN，down的原因会显示为IRF-link-down

·MAD ShutDown：当IRF分裂后，处于Recovery状态的IRF会将除了保留接口外的所有接口状态设置为DOWN，down的原因会显示为MAD ShutDown

·Not connected：表示没有物理连接（可能没有插网线或者网线故障）

·Storm-Constrain：表示端口上因为未知单播、组播或广播报文中某类报文的流量大于其上限阈值而被关闭

·STP DOWN：由于触发了STP BPDU保护而自动关闭接口

·Port Security Disabled：因检测到端口收到非法报文，端口安全的入侵检测机制将端口关闭

·Standby：表示接口处于备份状态

【相关命令】

·**reset counters interface**

**以太网接口 \-- 以太网接口通用配置命令 \-- display packet-drop**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与接口的型号有关，请以设备的实际情况为准。

****

**[display packet-drop**]命令用来显示接口丢弃的报文的信息。

【命令】

**[display packet-drop** { **interface** [ *interface-type* [ *interface-number*  ] \| **summary** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type*]：显示指定类型接口丢弃的报文的信息。不指定该参数时，显示所有接口丢弃的报文的信息。

*[interface-number*]：显示指定编号接口丢弃的报文的信息。不指定该参数时，显示该类型所有接口丢弃的报文的信息。

**[summary**]：将所有接口丢弃报文的统计信息累计后再显示。

【举例】

\# 显示接口GigabitEthernet1/0/1丢弃报文的信息。（本命令显示信息的支持情况与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display packet-drop interface gigabitethernet 1/0/1

GigabitEthernet1/0/1:

Packets dropped due to full GBP or insufficient bandwidth: 301

Packets dropped due to Fast Filter Processor FFP: 261

Packets dropped due to STP non-forwarding state: 321

Packets dropped due to rate-limit: 143

Packets dropped due to broadcast-suppression: 301

Packets dropped due to unicast-suppression: 215

Packets dropped due to multicast-suppression: 241

Packets dropped due to Tx packet aging: 246

\# 将所有接口丢弃报文的统计信息累计后再显示。（本命令显示信息的支持情况与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display packet-drop summary

All interfaces:

  Packets dropped due to full GBP or insufficient bandwidth: 301

  Packets dropped due to FFP: 261

  Packets dropped due to STP non-forwarding state: 321

  Packets dropped due to rate-limit: 143

  Packets dropped due to broadcast-suppression: 301

  Packets dropped due to unicast-suppression: 215

  Packets dropped due to multicast-suppression: 241

  Packets dropped due to Tx packet aging: 246

表1-6 display packet-drop命令显示信息描述表

字段

描述

Packets dropped due to full GBP or insufficient bandwidth

由于芯片缓存满或者带宽不够导致的丢包数

Packets dropped due to Fast Filter Processor FFP

由于数据包被过滤所导致的丢包数

Packets dropped due to STP non-forwarding state

由于STP协议状态为discarding导致的丢包数

Packets dropped due to rate-limit

由于速率限制导致的丢包数（该信息的支持情况与设备的型号有关，请以设备的实际情况为准）

Packets dropped due to broadcast-suppression

由于广播抑制导致的丢包数（该信息的支持情况与设备的型号有关，请以设备的实际情况为准）

Packets dropped due to unicast-suppression

由于未知单播抑制导致的丢包数（该信息的支持情况与设备的型号有关，请以设备的实际情况为准）

Packets dropped due to multicast-suppression

由于组播抑制导致的丢包数（该信息的支持情况与设备的型号有关，请以设备的实际情况为准）

Packets dropped due to Tx packet aging

由于出方向报文超时导致的丢包数（该信息的支持情况与设备的型号有关，请以设备的实际情况为准）

**以太网接口 \-- 以太网接口通用配置命令 \-- duplex**

------------------------------------------------------------------------

**[duplex**]命令用来设置以太网接口的双工模式。

**[undo duplex**]命令用来恢复缺省情况。

【命令】

**[duplex**[ { **auto** \| **full** \| **half** }]]

**[undo duplex**]

【缺省情况】

以太网接口的双工模式为**auto**（自协商）状态，10GE/40GE接口的双工模式为全双工状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：接口与对端接口自动协商双工状态。

**[full**]：全双工状态，接口在发送数据包的同时可以接收数据包。

**[half**]：半双工状态，接口同一时刻只能发送数据包或接收数据包。

【举例】

\# 将以太网接口GigabitEthernet1/0/1接口设置为全双工状态。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 duplex full

**以太网接口 \-- 以太网接口通用配置命令 \-- eee enable**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

设备是否支持本特性以及哪些类型的接口支持本特性与设备的型号有关，请以设备的实际情况为准。

****

**[eee enable**]命令用来使能EEE（Energy Efficient Ethernet）节能功能。

**[undo eee enable**]命令用来恢复缺省情况。

【命令】

**[eee enable**]

**[undo eee enable**]

【缺省情况】

EEE节能功能处于关闭状态。

【视图】

以太网接口视图

【缺省级别】

network-admin

mdc-admin

【使用指导】

接口使能EEE节能功能后，如果在连续一段时间（由芯片规格决定，不能通过命令行配置）内接口状态始终为up且没有收发任何报文，则接口自动进入低功耗模式；当接口需要收发报文时，接口又自动恢复到正常工作模式，从而达到节能的效果。

【举例】

\# 在GigabitEthernet1/0/1下使能EEE节能功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 eee enable

**以太网接口 \-- 以太网接口通用配置命令 \-- flag sdh**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令只有10GE接口工作在WAN模式下时配置才有效。

**[flag sdh**]命令用来设置10GE接口工作在WAN模式下时，SDH（Synchronous Digital Hierarchy，同步数字系列）帧开销字段中J0或J1字节的值。

**[undo flag sdh**]命令用来恢复缺省情况。

【命令】

**[flag **[{ **j0** \| **j1** } **sdh** *value*]]

**[undo flag **[{ **j0** \| **j1** } **sdh**]]

【缺省情况】

J0和J1字节的值为全0。

【视图】

Ten-GigabitEthernet接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[j0**]：再生段踪迹字节。

**[j1**]：通道踪迹字节。

*[value*]：J0或J1字节的值，为1～15个字符的字符串。

【举例】

\# 配置SDH帧中J0字节的值为Sysname。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/1/1

Sysname-Ten-GigabitEthernet1/1/1 port-mode wan

Sysname-Ten-GigabitEthernet1/1/1 flag j0 sdh Sysname

【相关命令】

·**port-mode**

**以太网接口 \-- 以太网接口通用配置命令 \-- flow-control**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·只有本端和对端设备都开启了流量控制功能，才能实现对本端以太网接口的流量控制。

**[flow-control**]命令用来开启以太网接口的流量控制功能。

**[undo flow-control**]命令用来关闭以太网接口流量控制功能。

【命令】

**[flow-control**]

**[undo flow-control**]

【缺省情况】

以太网接口的流量控制功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置**flow-control**命令后，设备具有发送和接收流量控制报文的能力：当本端发生拥塞时，设备会向对端发送流量控制报文；当本端收到对端的流量控制报文后，会停止报文发送。

【举例】

\# 开启以太网接口GigabitEthernet1/0/1的流量控制功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 flow-control

**以太网接口 \-- 以太网接口通用配置命令 \-- flow-control receive enable**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[flow-control receive enable**]命令用来配置以太网接口的接收流量控制功能。

**[undo flow-control**]命令用来关闭以太网接口接收流量控制功能。

【命令】

**[flow-control receive enable**]

**[undo flow-control**]

【缺省情况】

以太网接口的接收流量控制功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置**flow-control receive enable**命令后，设备具有接收流量控制报文的能力，但不具有发送流量控制报文的能力。当设备收到对端的流量控制报文，会停止向对端发送报文；当本端发生拥塞时，设备不能向对端发送流量控制报文。因此，如果要应对单向网络拥塞的情况，可以在一端配置**flow-control receive enable**，在对端配置**flow-control**；如果要求本端和对端网络拥塞都能处理，则两端都必须配置**flow-control**。

【举例】

\# 使能以太网接口GigabitEthernet1/0/1的接收流量控制功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 flow-control receive enable

【相关配置】

·**flow-control**

**以太网接口 \-- 以太网接口通用配置命令 \-- flow-interval**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

·本命令的支持情况与设备型号有关，请以设备的实际情况为准。

·不同型号的设备支持的配置方式不同，请以设备的实际情况为准。但对于同一设备，全局配置和接口下的配置不能同时支持。

**[flow-interval**]命令用来配置接口统计报文信息的时间间隔。

**[undo flow-interval**]命令用来恢复缺省情况。

【命令】

**[flow-interval ***interval*]

**[undo flow-interval**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图/以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：接口统计信息的时间间隔值，取值范围为5～300，单位为秒，步长为5（即取值必须为5的整数倍）。

【使用指导】

用户可以通过全局配置（系统视图下）和接口下（以太网接口视图或端口组视图下）的配置来配置以太网接口统计信息的时间间隔：

·系统视图下的配置对所有以太网接口生效；

·以太网接口视图下的该配置只对当前接口生效。

【举例】

\# 设置以太网接口GigabitEthernet1/0/1的统计信息时间间隔为100秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 flow-interval 100

**以太网接口 \-- 以太网接口通用配置命令 \-- interface**

------------------------------------------------------------------------

**[interface**]命令用来进入相应接口/子接口视图。如果进入视图前，相应子接口不存在，则先创建子接口，再进入该子接口视图。

【命令】

**[interface ***interface-type*[ { *interface-number* \| *interface-number.subnumber* }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type*]：指定接口类型。

*[interface-number*]：指定接口编号。

*[interface-number.subnumber*]：指定子接口编号。其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为1～4094。

【举例】

\# 进入以太网接口GigabitEthernet1/0/1视图。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1

\# 创建以太网子接口GigabitEthernet1/0/1.1并进入该子接口的视图。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1

**以太网接口 \-- 以太网接口通用配置命令 \-- jumboframe enable**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·不同型号的设备支持的配置方式不同，请以设备的实际情况为准。

****

**[jumboframe enable**]命令用来允许超长帧通过。

**[undo jumboframe enable**]命令用来禁止超长帧通过。

【命令】

**[jumboframe enable ** *value* ]

**[undo jumboframe enable**]

【缺省情况】

设备允许指定长度的超长帧通过，但是允许通过的超长帧的长度与设备的型号有关，请以设备的实际情况为准。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：以太网接口上允许通过的超长帧的最大长度，单位为字节。本参数的支持情况以及本参数的取值范围和缺省情况均与设备的型号有关，请以设备的实际情况为准。

【使用指导】

多次执行本命令配置不同的*value*值时，最新的配置生效。

【举例】

\# 允许超长帧通过以太网接口GigabitEthernet1/0/1。（本举例的支持情况与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 jumboframe enable

**以太网接口 \-- 以太网接口通用配置命令 \-- link-delay**

------------------------------------------------------------------------

**[link-delay**]命令用来配置以太网接口物理连接状态抑制功能。

**[undo link-delay**]命令用来恢复缺省情况。

【命令】

**[link-delay **[ **msec**  *delay-time* [ **mode** { **up** \| **updown** } ]]]

**[undo link-delay **[ **msec**  *delay-time* [ **mode** { **up** \| **updown** } ]]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[msec**]：表示配置的抑制时间为毫秒级。不指定该参数时，表示配置的抑制时间为秒级。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[delay-time*]：接口物理连接状态抑制时间值：

·取值范围为0～30，单位为秒。

·当和**msec**参数一起使用的时候，取值范围为0～10000，且为100的倍数，单位为毫秒。

·0表示不抑制，即接口状态改变时立即上报CPU。

**[mode up**]：设置以太网接口物理连接up状态抑制功能。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mode updown**]：设置以太网接口物理连接up和down状态抑制功能。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

使用该命令时，选取的参数不同，抑制效果不同：

·不指定**mode**参数：表示接口状态从up变成down时，不会立即上报CPU。而是等待*delay-time*时间后，再检查接口状态，如果状态仍然是down，再上报。接口状态从down变成up时，立即上报CPU。

·**mode up**：表示接口状态从down变成up时，不会立即上报CPU。而是等待*delay-time*时间后，再检查接口状态，如果状态仍然是up，再上报。接口状态从up变成down时，立即上报CPU。

·**mode updown**：表示接口状态从up变成down或者down变成up时，都不会立即上报CPU。等待*delay-time*时间后，再检查接口状态，如果状态仍然是down或者up，再上报。

同一接口下，接口状态从up变成down的抑制时间和接口状态从down变成up的抑制时间可以不同。如果在同一端口下，多次执行本命令配置了不同的抑制时间，则两个抑制时间会分别以最新配置为准。

对于使能了RRPP、MSTP或Smart Link的端口不推荐使用该命令。

【举例】

\# 设置以太网接口物理连接down状态抑制时间为8秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 link-delay 8

\# 设置以太网接口物理连接up状态抑制时间为800毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 link-delay msec 800 mode up

**以太网接口 \-- 以太网接口通用配置命令 \-- loopback**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[loopback**]命令用来对以太网接口进行环回测试。

**[undo loopback**]命令用来取消环回测试。

【命令】

**[loopback**[ { **external** \| **internal** }]]

**[undo loopback**]

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[external**]：对以太网接口进行对外环回测试。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[internal**]：对以太网接口进行对内环回测试。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

在进行某些特殊功能测试时，例如初步定位以太网故障时，需要对以太网接口进行环回测试。

需要注意的是：

·对以太网接口进行环回测试时，接口将不能正常转发数据包。

·手工关闭以太网接口（接口状态显示为ADM或者Administratively DOWN）时，则不能进行内部和外部环回测试。

·在进行环回测试时系统将禁止在接口上进行**speed**、**duplex**、**mdix-mode**和**shutdown**命令的配置。

·以太网接口进行环回测试时将工作在全双工状态，环回测试结束后恢复原有配置。

【举例】

\# 配置以太网接口GigabitEthernet1/0/1进行对内环回测试。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 loopback internal

**以太网接口 \-- 以太网接口通用配置命令 \-- port auto-power-down**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[port auto-power-down**]命令用来开启down状态接口节能功能。

**[undo port auto-power-down**]命令用来恢复缺省情况。

【命令】

**[port auto-power-down**]

**[undo port auto-power-down**]

【缺省情况】

未开启down状态接口节能功能。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置该命令后，如果在连续一段时间（由芯片规格决定，不能通过命令行配置）内接口状态始终为down，则系统会自动停止对该接口供电，接口自动进入节能模式；当接口状态变为up时，系统会自动恢复对该接口供电，接口自动进入正常模式，从而达到节能的效果。

【举例】

\# 开启以太网接口GigabitEthernet1/0/1的down状态节能功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port auto-power-down

**以太网接口 \-- 以太网接口通用配置命令 \-- port link-mode**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[port link-mode**]命令用来切换以太网接口的工作模式。

**[undo port link-mode**]命令用来恢复缺省情况。

【命令】

**[port link-mode**[ { **bridge** \| **route** }]]

**[undo port link-mode**]

【缺省情况】

不同型号的业务板上接口的工作模式不同，请以实际情况为准。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bridge**]：工作在二层模式。

**[route**]：工作在三层模式。

【使用指导】

基于业务板的硬件构造，设备上的某些接口只能作为二层以太网接口；某些接口只能作为三层以太网接口；某些接口比较灵活，工作模式可以通过命令行设置。如果将工作模式设置为二层模式（**bridge**），则作为一个二层以太网接口使用，如果将工作模式设置为三层模式（**route**），则作为一个三层以太网接口使用。

需要注意的是，接口模式切换后，除了**shutdown**和**combo enable**命令，该以太网接口下的其它所有命令都将恢复到新模式下的缺省情况。

【举例】

\# 使接口GigabitEthernet1/0/1工作在二层模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port link-mode bridge

**以太网接口 \-- 以太网接口通用配置命令 \-- port-mode**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[port-mode**]命令用来设置10GE接口工作在LAN模式或WAN模式。

**[undo port-mode**]命令用来恢复缺省情况。

【命令】

**[port-mode **[{ **lan** \| **wan** }]]

**[undo port-mode**]

【缺省情况】

10GE接口工作在LAN模式。

【视图】

Ten-GigabitEthernet接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lan**]：指定接口工作在LAN模式。工作在该模式下的接口传输以太网报文，用于连接以太网。

**[wan**]：指定接口工作在WAN模式。工作在该模式下的接口传输SDH（Synchronous Digital Hierarchy，同步数字系列）报文，用于连接SDH网络。接口工作在WAN模式下仅支持点到点的报文传输。

【举例】

\# 设置Ten-GigabitEthernet1/1/1接口工作在WAN模式。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet1/1/1

Sysname-Ten-GigabitEthernet1/1/1 port-mode wan

**以太网接口 \-- 以太网接口通用配置命令 \-- priority-flow-control**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令支持的视图与设备的型号有关，请以设备的实际情况为准。

****

**[priority-flow-control**]命令用来配置开启PFC（Priority-based Flow Control，基于优先级的流量控制）功能。

**[undo priority-flow-control**]命令用来关闭PFC功能。

【命令】

**[priority-flow-control **[{ **auto** \| **enable** }]]

**[undo priority-flow-control**]

【缺省情况】

PFC功能处于关闭状态。

【视图】

系统视图/以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auto**]：表示与对端自动协商是否开启PFC功能。

**[enable**]：表示强制开启PFC功能。

【使用指导】

如果本端和对端设备的PFC（Priority-based Flow Control，基于优先级的流量控制）功能处于使能状态，并配置了**priority-flow-control no-drop dot1p ***dot1p-list*命令，则当本端收到的802.1p优先级在*dot1p-list*范围内的报文发生拥塞时，会通知对端设备暂时停止向本端发送对应优先级的报文；拥塞解除后，再通知对端继续发送对应优先级的报文。从而保证本设备在转发802.1p优先级在*dot1p-list*范围内的报文时不丢包。

【举例】

\# 在以太网接口GigabitEthernet1/0/1上配置PFC功能的开启模式为自动协商模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 priority-flow-control auto

【相关命令】

·**priority-flow-control no-drop dot1p**

**以太网接口 \-- 以太网接口通用配置命令 \-- priority-flow-control no-drop dot1p**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令支持的视图与设备的型号有关，请以设备的实际情况为准。

****

**[priority-flow-control no-drop dot1p**]命令用来开启指定802.1p优先级的PFC功能。

**[undo priority-flow-control no-drop dot1p**]命令用来恢复缺省情况。

【命令】

**[priority-flow-control no-drop dot1p ***dot1p-list*]

**[undo priority-flow-control no-drop dot1p**]

【缺省情况】

所有802.1p优先级的PFC功能都处于关闭状态。

【视图】

系统视图/以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dot1p-list*]：802.1p优先级（CoS值，又称为dot1p优先级）列表，例如：1,3-5。（表示数值区间时使用连字符"-"，数值之间用英文格式的逗号","分隔，最多可配置16个字符）

【使用指导】

如果本端和对端设备的PFC功能处于使能状态，并配置了本命令，那么，当网络发生拥塞时，如果本端设备收到的报文的802.1p优先级在*dot1p-list*范围内，则优先发送该报文。

当PFC功能处于enabled状态时又配置了**flow-control**或**flow-control receive enable**，则PFC相应配置优先生效，**flow-control**和**flow-control receive enable**的配置将被忽略；当PFC功能处于disabled状态时又配置了**flow-control**或**flow-control receive enable**，则**flow-control**和**flow-control receive enable**的配置生效。

【举例】

\# 在以太网接口GigabitEthernet1/0/1上配置PFC功能的开启模式为自动协商模式，并开启802.1p优先级5的PFC功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 priority-flow-control auto

Sysname-GigabitEthernet1/0/1 priority-flow-control no-drop dot1p 5

【相关命令】

·**priority-flow-control**

·**flow-control**

·**flow-control receive enable**

**以太网接口 \-- 以太网接口通用配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除接口的统计信息。

【命令】

**[reset counters interface**[ [ *interface-type* [ *interface-number* \| *interface-number.subnumber* ] ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type*]：指定接口类型。

*[interface-number*]：指定接口编号。

*[interface-number.subnumber*]：指定子接口。其中*interface-number*为主接口编号；*subnumber*为子接口编号，取值范围为1～4094。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定*interface-type*和*interface-number*，则清除所有接口的统计信息；

·如果指定*interface-type*而不指定*interface-number*，则清除所有该类型接口的统计信息；

·如果同时指定*interface-type*和*interface-number*，则清除指定接口的统计信息。

【举例】

\# 清除以太网接口GigabitEthernet1/0/1的统计信息。

\<Sysname\> reset counters interface gigabitethernet 1/0/1

【相关命令】

·**display interface**

·**display ****counters interface**

·**display ****counters rate interface**

**以太网接口 \-- 以太网接口通用配置命令 \-- reset ethernet statistics**

------------------------------------------------------------------------

**[reset ethernet statistics**]命令用来清除以太网软件模块收发报文的统计信息。

【命令】

集中式设备：

**[reset ethernet statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset ethernet statistics ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset ethernet statistics ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot ***slot-number*]：清除指定单板的统计信息，*slot-number*表示单板所在的槽位号。不指定该参数时，表示所有单板。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备的统计信息，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，表示所有成员设备。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示IRF中的所有成员设备/PEX。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：清除指定成员设备上指定单板的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，表示IRF中的所有单板。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：清除指定单板/PEX的统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，表示IRF中的所有单板/PEX。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的统计信息，*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 清除以太网软件模块收发报文的统计信息。（集中式设备）

\<Sysname\> reset ethernet statistics

\# 清除以太网软件模块关于6号单板收发报文的统计信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> reset ethernet statistics slot 6

\# 清除以太网软件模块关于成员设备1上1号单板收发报文的统计信息。（分布式设备－IRF模式）

\<Sysname\> reset ethernet statistics chassis 1 slot 1

【相关命令】

·**display ethernet statistics**

**以太网接口 \-- 以太网接口通用配置命令 \-- reset packet-drop interface**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与接口的型号有关，请以设备的实际情况为准。

****

**[reset packet-drop interface**]命令用来清除指定接口丢弃报文的统计信息。

【命令】

**[reset packet-drop interface ** *interface-type*  *interface-number*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type*]：清除指定类型接口丢弃的报文的信息。不指定该参数时，清除所有接口丢弃的报文的信息。

*[interface-number*]：清除指定编号接口丢弃的报文的信息。不指定该参数时，清除该类型所有接口丢弃的报文的信息。

【举例】

\# 清除以太网接口GigabitEthernet1/0/1丢弃报文的统计信息。

\<Sysname\> reset packet-drop interface gigabitethernet 1/0/1

\# 清除所有接口丢弃报文的统计信息。

\<Sysname\> reset packet-drop interface

【相关命令】

·**display packet-drop**

**以太网接口 \-- 以太网接口通用配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭以太网接口/子接口。

**[undo** **shutdown**]命令用来打开以太网接口/子接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

以太网接口视图/以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在某些特殊情况下（例如修改接口的工作参数），接口相关配置不能立即生效，需要关闭再打开接口后，才能生效。

【举例】

\# 关闭以太网接口GigabitEthernet1/0/1后打开该接口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 shutdown

Sysname-GigabitEthernet1/0/1 undo shutdown

\# 关闭以太网子接口Ethernet1/0/1.1后打开该接口。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 shutdown

Sysname-GigabitEthernet1/0/1.1 undo shutdown

**以太网接口 \-- 以太网接口通用配置命令 \-- speed**

------------------------------------------------------------------------

**[speed**]命令用来设置以太网接口的速率。

**[undo speed**]命令用来恢复以太网接口的速率为缺省情况。

【命令】

**[speed**[ { **10** \| **100** \| **1000** \| **10000** \| **20000** \| **40000** \| **100000** \| **auto** }]]

**[undo speed**]

【缺省情况】

本命令的缺省情况与业务板的型号有关，请以设备的实际情况为准。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[10**]：表示接口速率为10Mbps。

**[100**]：表示接口速率为100Mbps。

**[1000**]：表示接口速率为1000Mbps，本参数的支持情况与业务板的型号有关，请以业务板的实际情况为准。

**[10000**]：表示接口速率为10000Mbps，本参数的支持情况与业务板的型号有关，请以业务板的实际情况为准。

**[20000**]：表示接口速率为20000Mbps，本参数的支持情况与业务板的型号有关，请以业务板的实际情况为准。

**[40000**]：表示接口速率为40000Mbps，本参数的支持情况与业务板的型号有关，请以业务板的实际情况为准。

**[100000**]：表示接口速率为100000Mbps，本参数的支持情况与业务板的型号有关，请以业务板的实际情况为准。

**[auto**]：表示接口速率处于自协商状态。

【使用指导】

·光口对本命令参数的支持情况与设备型号有关，请以设备的实际情况为准。

·对于以太网电口来说，使用**speed**命令设置端口速率，目的是使其与对端进行速率匹配；

·对于光口来说，使用**speed**命令设置端口速率，目的是使其与可插拔光模块进行速率匹配。

【举例】

\# 将以太网接口GigabitEthernet1/0/1的速率设置为自协商获得。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 speed auto

【相关命令】

·**speed**** auto**

**以太网接口 \-- 以太网接口通用配置命令 \-- sub-interface rate-statistic**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[sub-interface rate-statistic**]命令用来开启以太网接口/子接口的速率统计功能。

**[undo sub-interface rate-statistic**]命令用来关闭接口/子接口的速率统计功能。

【命令】

**[sub-interface rate-statistic**]

**[undo sub-interface rate-statistic**]

【缺省情况】

以太网接口/子接口的速率统计功能处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启本功能后可能需要耗费大量系统资源，请谨慎使用。

【举例】

\# 开启GigabitEthernet1/0/1接口的子接口速率统计功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sub-interface rate-statistic

This configuration may make a negative effect on the performance. Are you sure to continue? [Y/N:y]

**以太网接口 \-- 以太网接口通用配置命令 \-- threshold**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[threshold**]命令用来配置10GE接口工作在WAN模式下时，接口的SD告警门限和（或）SF告警门限。

**[undo threshold**]命令用来恢复缺省情况。

【命令】

**[threshold**[ { **sd** *sdvalue* \| **sf** *sfvalue* } \*]]

**[undo threshold**[ [ **sd** \| **sf** ]]]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

Ten-GigabitEthernet接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sd**]：表示配置的是SD（Signal Degrade，信号衰减）告警门限。

*[sdvalue*]：以10e-*sdvalue*的形式表示的SD告警门限值，取值范围为3～9。值越大表示SD告警门限越小。

**[sf**]：表示配置的是SF（Signal Fail，信号失败）告警门限。

*[sfvalue*]：以10e-*sfvalue*的形式表示的SF告警门限值，取值范围为3～9。值越大表示SF告警门限越小。

【使用指导】

SD告警和SF告警都用于标识当前线路的性能。SF告警比SD告警严重，SF的误码率门限通常比SD的误码率门限高，即：当出现少量误码时，设备先产生SD告警；而当误码率增大到一定程度、说明线路质量严重下降时，设备才产生SF告警。因此，应使SD的告警门限小于SF的告警门限，*sdvalue*的值应大于*sfvalue*。

【举例】

\# 配置接口Ten-GigabitEthernet1/1/1的SD告警门限为10e-5。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/1/1

Sysname-Ten-GigabitEthernet1/1/1 port-mode wan

Sysname-Ten-GigabitEthernet1/1/1 threshold sd 5

\# 配置接口Ten-GigabitEthernet1/1/1的SD告警门限为10e-7，SF告警门限为10e-5。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/1/1

Sysname-Ten-GigabitEthernet1/1/1 port-mode wan

Sysname-Ten-GigabitEthernet1/1/1 threshold sd 7 sf 5

【相关命令】

·**port-mode**

**以太网接口 \-- 以太网接口通用配置命令 \-- using fortygige**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[using fortygige**]命令用来将从40GE接口拆分的四个10GE接口合并为一个40GE接口，或者将100GE接口切换成40GE接口。

**[undo using fortygige**]命令用来取消对10GE接口的合并，或者取消对100GE接口的切换。

【命令】

**[using fortygige**]

**[undo using fortygige**]

【缺省情况】

40GE接口作为单个接口使用，未拆分；100GE接口未切换成40GE接口。

【视图】

10GE拆分接口视图/100GE接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果用户需要更大的带宽，可以将已拆分的10GE接口合并为40GE接口使用。在任何一个10GE拆分接口下执行该命令均生效，无需在其它拆分接口上配置。

如果对端连接的是40GE接口，或者用户当前只有40GE光模块没有100GE光模块，可以将100GE接口切换成40GE接口使用。

需要注意的是：

·执行本命令后，是否需要重启设备/业务板才能生效，与设备的型号有关，请以设备的实际情况为准。

·只有缺省MDC上支持该命令，非缺省MDC上不支持该命令。

【举例】

\# 将Ten-GigabitEthernet1/1/16:1～Ten-GigabitEthernet1/1/16:4接口合并。

\<System\> system-view

System interface ten-gigabitethernet1/1/16:1

System-Ten-GigabitEthernet1/1/16:1 using fortygige

The interfaces Ten-GigabitEthernet1/1/16:1 through Ten-GigabitEthernet1/1/16:4 will be deleted. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

\# 将HundredGigE1/2/1接口切换成40GE接口。

\<System\> system-view

System interface hundredgige 1/2/1

System-HundredGigE1/2/1 using fortygige

The interface HundredGigE1/2/1 will be deleted. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

【相关命令】

·**using tengige**

·**using hundredgige**

·**using twentygige**

**以太网接口 \-- 以太网接口通用配置命令 \-- using hundredgige**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[using hundredgige**]命令用来将从100GE接口拆分出来的10个或者12个10GE接口合并为一个100GE接口，或者将由100GE接口切换成的40GE接口恢复成100GE接口。

**[undo using hundredgige**]命令用来取消对10个或者12个10GE拆分接口的合并，或者取消40GE接口的切换。

【命令】

**[using hundredgige**]

**[undo using hundredgige**]

【缺省情况】

10GE拆分接口单独使用，不会合并；切换成的40GE接口不会切换回100GE接口。

【视图】

10GE拆分接口视图/40GE切换接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

100GE接口根据不同规格的接口芯片可以被拆分为10个或12个10GE接口。不存在冗余带宽的100GE接口可以被拆分为10个10GE接口，存在20GE冗余带宽的100GE接口可以被拆分为12个10GE接口。

如果用户需要更大的带宽，可以将从100GE接口拆分出来的10个或12个10GE接口合并为一个100GE接口使用。在任何一个10GE拆分接口下执行该命令均生效，无需在其它拆分接口上配置。

如果用户需要更大的带宽，可以将切换成的40GE接口恢复成100GE接口使用。对于普通40GE接口（非100GE接口切换成的40GE接口），执行本命令会提示不支持。

需要注意的是：

·执行本命令后，是否需要重启设备/业务板才能生效，与设备的型号有关，请以设备的实际情况为准。

·只有缺省MDC上支持该命令，非缺省MDC上不支持该命令。

【举例】

\# 将Ten-GigabitEthernet1/1/6:1\~Ten-GigabitEthernet1/1/6:10接口合并。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/1/6:1

Sysname-Ten-GigabitEthernet1/1/6:1using hundredgige

The interfaces Ten-GigabitEthernet1/1/6:1 through Ten-GigabitEthernet1/1/6:10 will be deleted. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

\# 将切换成的FortyGigE1/3/1切换回100GE接口。

\<Sysname\> system-view

Sysname interface fortygige 1/3/1

Sysname-FortyGigE1/3/1 using hundredgige

The interface FortyGigE1/3/1 will be deleted. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

【相关命令】

·**using tengige**

·**using fortygige**

**以太网接口 \-- 以太网接口通用配置命令 \-- using tengige**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[using tengige**]命令用来将一个高带宽的接口拆分成多个10GE接口。

**[undo using tengige**]命令用来取消对接口的拆分。

【命令】

**[using tengige**]

**[undo using tengige**]

【缺省情况】

高带宽的接口单独使用，不拆分。

【视图】

100GE接口视图/40GE接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了提高端口密度，减少用户使用成本，增加组网灵活性，设备支持将一个高带宽的接口拆分成多个10GE接口使用。例如：

·40GE接口FortyGigE1/3/49可以拆分成四个10GE接口Ten-GigabitEthernet1/3/49:1～Ten-GigabitEthernet1/3/49:4；

·100GE接口HundredGigE5/0/50可以拆分成十个或十二个10GE接口Ten-GigabitEthernet5/0/50:1～Ten-GigabitEthernet5/0/50:10或 Ten-GigabitEthernet5/0/50:1～Ten-GigabitEthernet5/0/50:12。

拆分出来的10GE接口除了命名方式外，支持的配置和特性均和普通10GE物理接口相同。

需要注意的是：

·执行本命令后，是否需要重启设备/业务板才能生效，与设备的型号有关，请以设备的实际情况为准。

·只有缺省MDC上支持该命令，非缺省MDC上不支持该命令。

【举例】

\# 将HundredGigE5/0/50接口拆分。

\<Sysname\> system-view

Sysname interface HundredGigE 5/0/50

Sysname-HundredGigE5/0/50 using tengige

The interface HundredGigE5/0/50 will be deleted. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

\# 将40GE接口FortyGigE1/3/49拆分成四个10GE接口。

\<System\> system-view

System interface FortyGigE 1/3/49

System-FortyGigE1/3/49 using tengige

The interface FortyGigE1/3/49 will be deleted. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

【相关命令】

·**using fortygige**

·**using hundredgige**

**以太网接口 \-- 以太网接口通用配置命令 \-- using twentygige**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[using twentygige**]命令用来将一个40GE接口拆分成两个20GE接口。

**[undo using twentygige**]命令用来取消对接口的拆分。

【命令】

**[using twentygige**]

**[undo using twentygige**]

【缺省情况】

40GE接口单独使用，不拆分。

【视图】

40GE接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了提高端口密度，减少用户使用成本，增加组网灵活性，设备支持将一个40GE接口拆分成两个20GE接口使用。例如：40GE接口FortyGigE1/3/49可以拆分成两个20GE接口TwentyGigE1/3/49:1～TwentyGigE1/3/49:2。拆分出来的20GE接口除了命名方式外，支持的配置和特性均和普通20GE物理接口相同。

需要注意的是：

·执行本命令后，是否需要重启设备/业务板才能生效，与设备的型号有关，请以设备的实际情况为准。

·只有缺省MDC上支持该命令，非缺省MDC上不支持该命令。

【举例】

\# 将40GE接口FortyGigE1/3/49拆分成两个20GE接口。

\<System\> system-view

System interface FortyGigE 1/3/49

System-FortyGigE1/3/49 using twentygige

The interface FortyGigE1/3/49 will be deleted. Continue? [Y/N:y]

Reboot device to make the configuration take effect.

【相关命令】

·**using fortygige**

**以太网接口 \-- 二层以太网接口的配置命令 \-- broadcast-suppression**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[broadcast-suppression**]命令用来开启端口广播风暴抑制功能，并设置广播风暴抑制阈值。

**[undo broadcast-suppression**]命令用来恢复缺省情况。

【命令】

**[broadcast-suppression**[ { *ratio \|* **pps** *max-pps \|* **kbps** *max-kbps* }]]

**[undo** **broadcast-suppression**]

【缺省情况】

所有接口不对广播流量进行抑制。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ratio*]：指定以太网接口允许通过的最大广播流量占该接口带宽的百分比，取值范围为0～100。数值越小，允许通过的广播流量也越小。

**[pps*** max-pps*]：指定以太网接口每秒允许转发的最大广播包数，单位为pps（packets per second，每秒转发的报文数），取值范围为0～1.4881×接口带宽。

**[kbps ***max-kbps*]：指定以太网接口每秒允许转发的最大广播流量，单位为kbps（kilobits per second，每秒转发的千比特数），取值范围为0～接口带宽。

【使用指导】

本命令设置的是接口允许通过的最大广播报文流量。当接口上的广播流量超过用户设置的值后，系统将丢弃超出广播流量限制的报文，从而使接口广播流量所占的比例控制在限定的范围内，以便保证业务的正常运行。

执行**broadcast-suppression**或**storm-constrain**命令都能开启端口的广播风暴抑制功能，**storm-constrain**命令通过软件对广播报文进行抑制，对设备性能有一定影响，**broadcast-suppression**通过芯片物理上对广播报文进行抑制，相对**storm-constrain**来说，对设备性能影响较小。请不要同时配置**broadcast-suppression**和**storm-constrain**命令，以免配置冲突，导致抑制效果不确定。

当风暴抑制阈值配置为**pps**或**kbps**时，设备可能会根据芯片支持的步长，将配置值转换成步长的倍数。所以，端口下配置的抑制阈值可能与实际生效抑制阈值不一致，请注意查看设备的提示信息。

【举例】

\# 在以太网接口GigabitEthernet1/0/1上，每秒最多允许10000kbps广播报文通过，对超出该范围的广播报文进行抑制。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 broadcast-suppression kbps 10000

The actual value is 10048 on port GigabitEthernet1/0/1 currently.

以上信息表示：用户配置的值为10000kbps，因为芯片支持的步长为64，所以实际生效的值为10048kbps（64的157倍）。

【相关命令】

·**multicast-suppression**

·**unicast-suppression**

**以太网接口 \-- 二层以太网接口的配置命令 \-- display storm-constrain**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display storm-constrain**]命令用来显示接口流量控制信息。

【命令】

**[display storm-constrain **[[ **broadcast** \| **multicast** \| **unicast** ]  **interface** *interface-type* *interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[broadcast**]：只显示广播报文流量控制信息。

**[multicast**]：只显示组播报文流量控制信息。

**[unicast**]：只显示未知单播报文流量控制信息。

**[interface ***interface-type interface-number*]**：**显示指定接口的报文流量控制信息。*interface-type interface-number*指定接口类型和接口编号。不指定该参数时，显示所有接口报文的流量控制信息。

【使用指导】

不指定**broadcast**、**multicast**和**unicast**参数时，则显示所有类型报文的流量控制信息。

【举例】

\# 显示系统当前所有接口的流量控制信息。

\<Sysname\> display storm-constrain

Abbreviation: BC - broadcast; MC - multicast; UC - unicast{.TerminalDisplayChar}

Flow Statistic Interval: 5 (in seconds)

Port       Type  LowerLimit UpperLimit Unit  CtrlMode   Status     Trap  Log  StateChanges

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

GE1/0/0    MC   100        200        kbps   shutdown  shutdown   off  on    10

GE1/0/0    UC   200        300        kbps   shutdown  normal     off  on    33

XGE1/0/0   BC   500        1500       pps    N/A       normal     on   on    0

表1-7 display storm-constrain命令显示信息描述表

字段

描述

Flow Statistic Interval

流量统计的时间间隔，单位为秒

Port

接口名称缩写

StormType

进行流量阈值控制的报文类型：

·BC：broadcast，表示广播报文

·MC：multicast，表示组播报文

·UC：unicast，表示未知单播报文

LowerLimit

用户配置的流量控制下限阈值或百分比

UpperLimit

用户配置的流量控制上限阈值或百分比

Unit

用户配置的流量阀值的单位，为pps、kbps或百分比

CtrlMode

用户配置的流量阈值超过上限的控制动作：

·block表示阻塞方式

·shutdown表示关闭方式

·N/A表示未配置控制动作

Status

接口报文转发状态，取值为：

·forwarding表示该端口处于正常转发状态

·shutdown表示端口已被关闭

·block表示该端口对该类报文直接丢弃

Trap

Trap信息输出开关：

·on表示打开

·off表示关闭

Log

Log信息输出开关：

·on表示打开

·off表示关闭

StateChanges

接口报文转发状态切换次数

当StateChanges达到65535次时，会自动跳转到0，重新计数

**以太网接口 \-- 二层以太网接口的配置命令 \-- mac-address**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令支持的接口类型与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address**]命令用来配置以太网接口的MAC地址。

**[undo mac-address**]命令用来恢复缺省情况。

【命令】

**[mac-address** *mac-address*]

**[undo mac-address**]

【缺省情况】

以太网接口的MAC地址与设备型号有关，请以设备的实际情况为准。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：MAC地址，形式为H-H-H。

【举例】

\# 配置二层以太网接口GigabitEthernet1/0/1的MAC地址为0001-0001-0001。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address 1-1-1

**以太网接口 \-- 二层以太网接口的配置命令 \-- mdix-mode**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

光类型接口不支持本命令。

****

**[mdix-mode**]命令用来设置以太网接口的MDIX模式。

**[undo mdix-mode**]命令用来恢复缺省情况。

【命令】

**[mdix-mode **[{ **automdix** \| **mdi**\| **mdix** }]]

**[undo mdix-mode**]

【缺省情况】

以太网接口的MDIX模式为**automdix**。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[automdix**]：两端设备通过协商来决定引脚1和2是发送还是接收信号，引脚3和6是接收还是发送信号。

**[mdi**]：使用引脚1和2发送信号，使用引脚3和6接收信号。

**[mdix**]：使用引脚1和2接收信号，使用引脚3和6发送信号。

【举例】

\# 设置以太网接口GigabitEthernet1/0/1的MDIX模式为**mdi**。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mdix-mode mdi

**以太网接口 \-- 二层以太网接口的配置命令 \-- multicast-suppression**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[multicast-suppression**]命令用来开启端口组播风暴抑制功能，并设置组播风暴抑制阈值。

**[undo multicast-suppression**]命令用来恢复缺省情况。

【命令】

**[multicast-suppression**[ { *ratio \|* **pps** *max-pps* \| **kbps** *max-kbps* }]]

**[undo** **multicast-suppression**]

【缺省情况】

所有接口不对组播流量进行抑制。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ratio*]：指定以太网接口允许通过的最大组播流量占该接口带宽的百分比。取值范围为0～100。数值越小，则允许通过的组播流量也越小。

**[pps*** max-pps*]：指定以太网接口每秒最多通过的组播包包数，取值范围为0～1.4881×接口带宽。

**[kbps ***max-kbps*]：指定以太网接口每秒最多通过的组播流量，单位为kbps，取值范围为0～接口带宽。

【使用指导】

本命令设置的是接口允许通过的最大组播报文流量。当接口上的组播流量超过用户设置的值后，系统将丢弃超出组播流量限制的报文，从而使接口组播流量所占的比例控制在限定的范围内，以便保证业务的正常运行。

执行**multicast-suppression**或**storm-constrain**命令都能开启端口的组播风暴抑制功能，**storm-constrain**命令通过软件对组播报文进行抑制，对设备性能有一定影响，**multicast-suppression**通过芯片物理上对组播报文进行抑制，相对**storm-constrain**来说，对设备性能影响较小。请不要同时配置**multicast-suppression**和**storm-constrain**命令，以免配置冲突，导致抑制效果不确定。

当风暴抑制阈值配置为**pps**或**kbps**时，设备可能会根据芯片支持的步长，将配置值转换成步长的倍数。所以，端口下配置的抑制阈值可能与实际生效抑制阈值不一致，请注意查看设备的提示信息。

【举例】

\# 在以太网接口GigabitEthernet1/0/1上，每秒最多允许10000kbps组播报文通过，对超出该范围的组播报文进行抑制。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 multicast-suppression kbps 10000

The actual value is 10048 on port GigabitEthernet1/0/1 currently.

以上信息表示：用户配置的值为10000kbps，因为芯片支持的步长为64，所以实际生效的值为10048kbps（64的157倍）。

【相关命令】

·**broadcast-suppression**

·**unicast-suppression**

**以太网接口 \-- 二层以太网接口的配置命令 \-- port connection-mode**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[port connection-mode**]命令用来设置接口的连接模式。

**[undo port connection-mode**]命令用来恢复缺省情况。

【命令】

**[port connection-mode**[ { **extend** \| **normal** }]]

**[undo port connection-mode**]

【缺省情况】

端口工作在正常连接模式下。

【视图】

10GE接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[extend**]：设置端口工作在扩展连接模式。

**[normal**]：设置端口工作在正常连接模式。

【使用指导】

当设备用于OAA组网环境时，需要分别在设备和OAP插卡上，将设备和OAP插卡的内联接口的连接模式配置为扩展连接模式（**extend**），才能够实现设备和OAP插卡间的通信。

【举例】

\# 设置Ten-GigabitEthernet1/1/1接口的连接模式为扩展连接模式。

\<Sysname\> system-view

\<Sysname\> interface ten-gigabitethernet1/1/1

Sysname-Ten-GigabitEthernet1/1/1 port connection-mode extend

**以太网接口 \-- 二层以太网接口的配置命令 \-- port up-mode**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[port up-mode**]命令用来强制开启光口。

**[undo port up-mode**]命令用来恢复缺省情况。

【命令】

**[port up-mode**]

**[undo port up-mode**]

【缺省情况】

没有强制开启光口，光口的物理状态由光纤的物理状态决定。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

强制开启光口后，不管实际的光纤链路是否连通，甚至没有插入光纤或光模块，光口的物理状态都会变为up。此时，只要光口上有一条光纤链路是连通的，就可以实现报文的单向转发，以达到节约传输链路的效果。

需要注意的是：

·仅GE光口和工作在LAN模式下的10GE、40GE光口支持强制开启功能，电口和Combo口不支持该功能。

·光口必须工作在二层模式下才支持强制开启功能。

·**port up-mode**和**shutdown**命令互斥，不能同时配置。

·光口被强制开启后，光口的物理状态始终为up，不受光纤/光模块拔插的影响。

·光口被强制开启后，GE光口插入光电转换模块、100/1000M光模块、100M光模块后，流量不能正常转发。必须取消强制开启光口配置，才能正常转发。

【举例】

\# 强制开启光口GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 port up-mode

**以太网接口 \-- 二层以太网接口的配置命令 \-- port-type**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

·本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

·本命令视图的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[port-type**]命令用来在二层以太网接口和FC接口间进行类型切换。

【命令】

在二层以太网接口视图下：

**[port-type** **fc**]

在FC接口视图下：

**[port-type** **ethernet**]

【缺省情况】

接口为二层以太网接口类型。

【视图】

二层以太网接口视图/FC接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ethernet**]：将当前接口切换到二层以太网接口类型，切换后的接口速率与设备型号有关，请以设备的实际情况为准。

**[fc**]：将当前接口切换到FC接口类型。

【使用指导】

某些二层以太网接口支持切换到FC接口。如果要将这些二层以太网接口切换为FC接口，则需要进入对应的二层以太网接口视图执行**port-type** **fc**命令；如果要将FC接口切换回二层以太网接口，则需要进入对应的FC接口视图执行**port-type** **ethernet**命令。

接口类型切换后，原接口删除并创建新的接口，切换后的接口编号与切换前保持一致。

【举例】

\# 将二层以太网接口Ten-GigabitEthernet1/1/5切换为FC接口。

\<Sysname\> system-view

Sysname interface ten-gigabitethernet 1/1/5

Sysname-Ten-GigabitEthernet1/1/5 port-type fc

Sysname-Fc1/1/5

**以太网接口 \-- 二层以太网接口的配置命令 \-- speed auto**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image005.png)

本命令的支持情况与设备的型号以及具体的接口类型有关，请以设备的实际情况为准。

****

**[speed auto**]命令用来设置以太网接口的自协商速率范围。

**[undo speed**]命令用来恢复缺省情况。

【命令】

**[speed auto**[ { **10** \| **100** \| **1000** } \*]]

**[undo speed**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

百兆或者千兆二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[10**]：设置接口自协商速率为10Mbps。

**[100**]：设置接口自协商速率为100Mbps。

**[1000**]：设置接口自协商速率为1000Mbps，本参数的支持情况与业务板的型号有关，请以业务板的实际情况为准。

【使用指导】

如果多次使用**speed**、**speed auto**命令设置接口的速率，则最新配置生效。例如：若在接口下先配置了**speed auto 100 1000**，然后又配置**speed 100**，则接口的速率强制为100Mbps，不进行协商；若在接口下先配置了**speed 100**，然后又配置**speed auto 100 1000**，则接口将与对端协商速率，协商的结果只能为100Mbps或1000Mbps。

需要注意的是：

·如果两端使用**speed auto**命令用来设置接口自协商速率的范围完全不同，例如：一端为speed auto 10 100，另一端为speed auto 1000，此时两端速率协商不成功；

·如果两端使用**speed auto**命令用来设置接口自协商速率的范围部分相同，例如：一端为speed auto 10 100，另一端为speed auto 100 1000，此时两端速率协商为双方都有的100 Mbps；

·如果两端使用**speed auto**命令用来设置接口自协商速率的范围完全相同，例如：一端为**speed auto 100 1000**，另一端为**speed auto 100 1000**，此时两端取速率协商范围内最大速率1000 Mbps。

【举例】

\# 设置接口GigabitEthernet1/0/1的自协商速率为10Mbps或1000Mbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 speed auto 10 1000

【相关命令】

·**speed**

**以太网接口 \-- 二层以太网接口的配置命令 \-- storm-constrain**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[storm-constrain**]命令用来开启端口流量阈值控制功能，并设置上限阈值与下限阈值。

**[undo storm-constrain**]命令用来取消端口报文流量上限阈值配置及下限阈值配置。

【命令】

**[storm-constrain **[{ **broadcast** \| **multicast** \| **unicast** } { **pps** \| **kbps** \| **ratio** } *upperlimit lowerlimit*]]

**[undo storm-constrain **[{ **all** \| **broadcast** \| **multicast** \| **unicast** }]]

【缺省情况】

没有设置端口的流量阈值，即不对端口的报文流量进行抑制。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：取消端口所有类型（未知单播、组播和广播）报文流量阈值配置。

**[broadcast**]：设置端口广播报文流量阈值。

**[multicast**]：设置端口组播报文流量阈值。

**[unicast**]：设置端口未知单播报文流量阈值。

**[pps**]：以包每秒为单位统计流量。

**[kbps**]：以千比特每秒为单位统计流量。

**[ratio**]：以每秒钟报文所占接口物理带宽的百分比来统计流量。

*[upperlimit*]：端口报文流量的上限阈值。当和**pps**一起使用时，该参数的取值范围为0～1.4881×接口带宽；当和**kbps**一起使用时，该参数的取值范围为0～接口带宽；当和**ratio**一起使用时，该参数的取值范围为为0～100。

*[lowerlimit*]：端口报文流量的下限阈值。当和**pps**一起使用时，该参数的取值范围为0～1.4881×接口带宽；当和**kbps**一起使用时，该参数的取值范围为0～接口带宽；当和**ratio**一起使用时，该参数的取值范围为为0～100。

【使用指导】

执行本命令后，设备就会周期性地对接口收到的指定类型的报文进行统计，如果流量超过上限阈值，则采取一定的措施。其中，通过**storm-constrain interval**命令可以配置统计周期，通过**storm-constrain control**命令可以配置流量超过上限阈值时采取的控制方式。

执行**storm-constrain**与**broadcast-suppression**、**multicast-suppression**、**unitcast-suppression**命令都能开启端口的风暴抑制功能。**storm-constrain**命令通过软件对报文流量进行抑制，对设备性能有一定影响，**broadcast-suppression**、**multicast-suppression**、**unitcast-suppression**通过芯片物理上对报文流量进行抑制，相对**storm-constrain**来说，对设备性能影响较小。对于某种类型的报文流量，请不要同时配置这两种方式，以免配置冲突，导致抑制效果不确定。

配置时，*upperlimit*值必须大于*lowerlimit*值，建议不要配成相等值。

【举例】

\# 对GigabitEthernet1/0/1端口配置未知单播流量阈值，上限阈值为200pps、下限阈值为150pps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 storm-constrain unicast pps 200 150

\# 对GigabitEthernet1/0/2端口配置广播流量阈值，上限阈值为2000kbps、下限阈值为1500kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 storm-constrain broadcast kbps 2000 1500

\# 对GigabitEthernet1/0/3端口配置组播流量百分比阈值，上限为80%、下限为15%。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 storm-constrain multicast ratio 80 15

【相关命令】

·**storm-constrain control**

·**storm-constrain interval**

**以太网接口 \-- 二层以太网接口的配置命令 \-- storm-constrain control**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[storm-constrain control**]命令用来设置端口未知单播、组播或者广播流量超过上限阈值时采取的控制方式。

**[undo storm-constrain control**]命令用来恢复缺省情况。

【命令】

**[storm-constrain control **[{ **block** \| **shutdown** }]]

**[undo storm-constrain control**]

【缺省情况】

不对端口流量进行任何控制。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[block**]：block方式，即：当端口上未知单播、组播或广播报文中某类报文的流量大于其上限阈值时，端口将暂停转发该类报文（其它类型报文照常转发），端口处于阻塞状态，但仍会统计该类报文的流量。当该类报文的流量小于其下限阈值时，端口将自动恢复对此类报文的转发。

**[shutdown**]：shutdown方式，即：当端口上未知单播、组播或广播报文中某类报文的流量大于其上限阈值时，端口将被关闭，系统停止转发所有报文。当该类报文的流量小于其下限阈值时，端口状态不会自动恢复，此时可通过执行**undo shutdown**命令或取消端口上流量阈值的配置来恢复。

【举例】

\# 配置GigabitEthernet1/0/1端口，当流量超过上限阈值时，采用block方式控制。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 storm-constrain control block

【相关命令】

·**storm-constrain**

·**storm-constrain control**

**以太网接口 \-- 二层以太网接口的配置命令 \-- storm-constrain enable log**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[storm-constrain enable log**]命令用来配置端口流量大于上限阈值或者小于下限阈值时输出Log信息。

**[undo storm-constrain enable log**]命令用来禁止端口流量大于上限阈值或者小于下限阈值时输出Log信息。

【命令】

**[storm-constrain enable** **log**]

**[undo storm-constrain enable log**]

【缺省情况】

端口流量大于上限阈值或者小于下限阈值时输出Log信息。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 当GigabitEthernet1/0/1端口流量大于上限阈值或者小于下限阈值时输出Log信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 storm-constrain enable log

**以太网接口 \-- 二层以太网接口的配置命令 \-- storm-constrain enable trap**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[storm-constrain enable trap**]命令用来配置端口流量大于上限阈值或者小于下限阈值时输出Trap信息。

**[undo storm-constrain enable trap**]命令用来禁止端口流量大于上限阈值或者小于下限阈值时输出Trap信息。

【命令】

**[storm-constrain enable** **trap**]

**[undo storm-constrain enable trap**]

【缺省情况】

端口流量大于上限阈值或者小于下限阈值时输出Trap信息。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 当GigabitEthernet1/0/1端口流量大于上限阈值或者小于下限阈值时输出Trap信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 storm-constrain enable trap

**以太网接口 \-- 二层以太网接口的配置命令 \-- storm-constrain interval**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[storm-constrain interval**]命令用来配置端口流量阈值控制模块流量统计的时间间隔。

**[undo storm-constrain interval**]命令用来恢复缺省情况。

【命令】

**[storm-constrain interval** *seconds*]

**[undo storm-constrain interval**]

【缺省情况】

端口流量统计的时间间隔为10秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：端口流量统计的时间间隔，取值范围为1～300，单位为秒。为了保持网络状态的稳定，建议设置的时间间隔不低于10秒。

【使用指导】

本命令设置的时间间隔专门为**storm-constrain**命令服务的，不同于**flow-interval**命令设置的时间间隔。虽然同样是统计端口流量，但是功能是分开的。

【举例】

\# 配置端口流量统计时间间隔为60秒。

\<Sysname\> system-view

Sysname storm-constrain interval 60

【相关命令】

·**storm-constrain**

·**storm-constrain control**

**以太网接口 \-- 二层以太网接口的配置命令 \-- unicast-suppression**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[unicast-suppression**]命令用来开启端口未知单播风暴抑制功能，并设置未知单播风暴抑制阈值。

**[undo unicast-suppression**]命令用来恢复缺省情况。

【命令】

**[unicast-suppression**[ { *ratio* \| **pps** *max-pps* \| **kbps** *max-kbps* }]]

**[undo** **unicast-suppression**]

【缺省情况】

所有接口不对未知单播流量进行抑制。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ratio*]：指定以太网接口最大未知单播流量占该接口带宽的百分比。取值范围为0～100。数值越小，则允许通过的未知单播流量也越小。

**[pps*** max-pps*]：指定以太网接口每秒最多通过的未知单播包包数，取值范围为0～1.4881×接口带宽。

**[kbps ***max-kbps*]：指定以太网接口每秒通过的未知单播流量，单位为kbps，取值范围为0～接口带宽。

【使用指导】

本命令设置的是接口允许通过的最大未知单播报文流量。当接口上的未知单播流量超过用户设置的值后，系统将丢弃超出未知单播流量限制的报文，从而使接口未知单播流量所占的比例降低到限定的范围，保证网络业务的正常运行。

执行**unicast-suppression**或**storm-constrain**命令都能开启端口的未知单播风暴抑制功能，**storm-constrain**命令通过软件对未知单播报文进行抑制，对设备性能有一定影响，**unitcast-suppression**通过芯片物理上对未知单播报文进行抑制，相对**storm-constrain**来说，对设备性能影响较小。请不要同时配置**unitcast-suppression**和**storm-constrain**命令，以免配置冲突，导致抑制效果不确定。

当风暴抑制阈值配置为**pps**或**kbps**时，设备可能会根据芯片支持的步长，将配置值转换成步长的倍数。所以，端口下配置的抑制阈值可能与实际生效抑制阈值不一致，请注意查看设备的提示信息。

【举例】

\# 在以太网接口GigabitEthernet1/0/1上，每秒最多允许10000kbps未知单播报文通过，对超出该范围的未知单播报文进行抑制。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 unicast-suppression kbps 10000

The actual value is 10048 on port GigabitEthernet1/0/1 currently.

以上信息表示：用户配置的值为10000kbps，因为芯片支持的步长为64，所以实际生效的值为10048kbps（64的157倍）。

【相关命令】

·**broadcast-suppression**

·**multicast-suppression**

**以太网接口 \-- 二层以太网接口的配置命令 \-- virtual-cable-test**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image003.png)

光接口不支持本命令，其他以太网接口对本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[virtual-cable-test**]命令用来对以太网接口连接电缆进行一次检测，并显示检测结果。

【命令】

**[virtual-cable-test**]

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在以太网接口上执行本命令会使已经up的链路自动up、down一次。

·检测结果仅供参考，检测到的长度最大误差为5米。

·如果显示值为"-"，则表示不支持该项参数的检测。

【举例】

\# 开启系统对以太网电口连接电缆的检测功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 virtual-cable-test

Cable status: abnormal(open), 140 metre(s)

Pair Impedance mismatch: -

Pair skew: - ns

Pair swap: -

Pair polarity: -

Insertion loss: - db

Return loss: - db

Near-end crosstalk: - db

表1-8 virtual-cable-test命令显示信息描述表

字段

描述

Cable status

电缆状态，包括：

·normal：正常

·abnormal：异常

·abnormal(open)：异常开路

·abnormal(short)：异常短路

·failure：检测失败

*[n* metres]

当电缆状态为正常时，显示的是电缆的总长度

当电缆状态非正常时，显示的是本接口到异常位置的长度

Pair Impedance mismatch

线对阻抗是否匹配，取值为：

·yes：阻抗匹配

·no：阻抗不匹配

Pair skew

线对不对称

Pair swap

线对交换

Pair polarity

是否极性交换

Insertion loss

插入信号衰减

Return loss

返回信号衰减

Near-end crosstalk

近端串扰

**以太网接口 \-- 三层以太网接口/子接口的配置命令 \-- mac-address**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令支持的接口类型与设备的型号有关，请以设备的实际情况为准。

****

**[mac-address**]命令用来配置以太网接口的MAC地址。

**[undo mac-address**]命令用来恢复缺省情况。

【命令】

**[mac-address** *mac-address*]

**[undo mac-address**]

【缺省情况】

以太网接口的MAC地址与设备型号有关，请以设备的实际情况为准。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：MAC地址，形式为H-H-H。

【使用指导】

·配置三层以太网子接口MAC地址时，子接口与主接口MAC地址不可使用同一地址。

·给子接口配置MAC地址时，请不要使用VRRP协议保留的MAC地址段。

【举例】

\# 配置三层以太网接口GigabitEthernet1/0/1的MAC地址为0001-0001-0001。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mac-address 1-1-1

**以太网接口 \-- 三层以太网接口/子接口的配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来设置三层以太网接口/子接口的MTU值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

三层以太网接口/子接口的MTU值为1500字节。

【视图】

三层以太网接口视图/三层以太网子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：以太网接口允许通过的MTU的大小，取值范围取决于接口的类型，单位为字节。

【使用指导】

由于QoS队列长度的限制（如FIFO队列的缺省长度为75），MTU太小会造成分片太多，从而被QoS队列丢弃。此时，可适当增大MTU值或QoS队列的长度。以太网接口视图下的命令**qos fifo queue-length**可以改变QoS队列长度（具体配置请参见"ACL和QoS配置指导"中的"QoS"）。

【举例】

\# 设置三层以太网接口GigabitEthernet1/0/1的最大传输单元为1430Bytes。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mtu 1430

\# 设置三层以太网子接口GigabitEthernet1/0/1.1的最大传输单元为1430Bytes。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

Sysname-GigabitEthernet1/0/1.1 mtu 1430

**以太网接口 \-- 三层以太网接口/子接口的配置命令 \-- port-type switch**

------------------------------------------------------------------------

![说明](以太网接口命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[port-type switch**]命令用来在POS接口和三层GE接口间进行类型切换。

【命令】

在POS接口视图下：

**[port-type switch gigabitethernet**]

在三层GE接口视图下：

**[port-type switch pos**]

【视图】

POS接口视图/三层GE接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gigabitethernet**]：将当前POS接口切换为三层GE接口。

**[pos**]：将当前三层GE接口切换为POS接口。

【使用指导】

接口类型切换后，原接口删除并创建新的接口，切换后的接口编号与切换前保持一致。

命令执行成功后会自动切换到新接口的接口视图下。

【举例】

\# 将POS接口2/2/0切换为GigabitEthernet2/2/0接口。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 port-type switch gigabitethernet

Changing port type can result in loss of port configuration. Are you sure to continue? [Y/N:y]

Sysname-GigabitEthernet2/2/0

