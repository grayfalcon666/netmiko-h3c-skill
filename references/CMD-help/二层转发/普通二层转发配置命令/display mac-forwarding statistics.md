
**二层转发 \-- 普通二层转发配置命令 \-- display mac-forwarding statistics**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display mac-forwarding statistics**]命令用来显示二层转发统计信息。

【命令】

**[display mac-forwarding statistics** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的二层转发统计信息。其中，*interface-type interface-number*为指定接口类型和接口编号。如果未指定该参数，将显示二层转发全局统计信息。

【举例】

\# 显示二层转发全局统计信息。

\<Sysname\> display mac-forwarding statistics

Input:

   Sum:               888        Unknown Unicast:   0

   Broadcast:         0          Multicast:         0

   Filtered:          0          STP discarded:     0

   Service dropped:   0          Source dropped:    0

   Unknown dropped:   0          Learning dropped:  0

   Attack dropped:    0          Suppress dropped:  0

Deliver:

   Sum:               111        L2 protocol:       11

   Local MAC address: 100

Output:

   Sum:               666        Filtered:          0

   Blackhole dropped: 0          STP discarded:     0

   Service dropped:   0          Dest MAC dropped:  0

\# 显示接口GigabitEthernet1/0/1的二层转发统计信息。

\<Sysname\> display mac-forwarding statistics interface gigabitethernet 1/0/1

GigabitEthernet 1/0/1:

Input frames: 100    Output frames:100

Filtered:     0

表1-1 display mac-forwarding statistics命令显示信息描述表

字段

描述

Input

Sum

接收的以太帧总数

Filtered

按照802.1Q Tagged VLAN入接口过滤规则过滤掉的以太帧数量

STP discarded

由于生成树协议阻塞而丢弃的入报文数量

Service dropped

入方向业务丢弃的以太帧数量

Source dropped

因源MAC地址为全零、组播或广播而丢弃的以太帧数量

Unknown dropped

因设置源未知丢弃而丢弃的以太帧数量

Learning dropped

因设置学满禁止转发而丢弃的以太帧数量

Attack dropped

源MAC地址为攻击MAC地址时丢弃的以太帧数量

Suppress dropped

未知单播、广播或组播报文抑止丢弃的以太帧数量

Broadcast

接收到的广播目的MAC地址以太帧数量

Multicast

接收到的组播目的MAC地址以太帧数量

Unknown unicast

接收到的未知单播MAC地址以太帧数量

Deliver

Sum

上送CPU处理的以太帧总数量

L2 protocol

上送CPU的二层协议以太帧数量

Local MAC address

目的地址为本地三层VLAN虚接口MAC地址的以太帧数量

Output

Blackhole dropped

目的MAC地址为黑洞MAC地址时丢弃的以太帧数量

Sum

发出的以太帧总数

Filtered

按照802.1Q Tagged VLAN出接口过滤规则过滤掉的以太帧数量

STP discarded

由于生成树协议阻塞而丢弃的出报文数量

Service dropped

出方向业务丢弃的以太帧数量

Dest MAC dropped

因设置目的MAC地址丢弃而丢弃的以太帧数量

接口名

Input frames

接口接收以太帧数量

Output frames

接口发送以太帧数量

Filtered

接口过滤掉的其他VLAN的以太帧数量

**二层转发 \-- 普通二层转发配置命令 \-- reset mac-forwarding statistics**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[reset mac-forwarding statistics**]命令用来清除二层转发统计信息。

【命令】

**[reset mac-forwarding statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 清除二层转发统计信息。

\<Sysname\> reset mac-forwarding statistics

**二层转发 \-- 快速二层转发配置命令 \-- display mac-forwarding cache ip**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display mac-forwarding cache ip**]命令用来显示IP快速转发表信息。

【命令】

集中式设备：

**[display mac-forwarding cache ip** [ *ip-address* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mac-forwarding cache ip** [ *ip-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mac-forwarding cache ip** [ *ip-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定IP地址的快速转发表信息。如果不指定*ip-address*，将显示所有快速转发表信息。

**[slot**]*slot-number*：显示指定单板的快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的快速转发表信息。*slot-number*表示单板的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果不指定**slot***slot-number*，将显示所有成员设备的快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定**slot***slot-number*，将显示所有成员设备/PEX的快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有成员设备上所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有成员设备上所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示IP快速转发表信息。

\<Sysname\> display mac-forwarding cache ip

Total number of mac-forwarding entries: 2

SIP            SPort DIP             DPort Pro Input_If    Output_If   VLAN

1.1.1.2        99    1.1.1.1         2048  1   GE1/5/0/46  GE1/5/0/47  2

1.1.1.1        98    1.1.1.2         2012  1   GE1/5/0/47  GE1/5/0/46  2

表1-2 display mac-forwarding cache ip命令显示信息描述表

字段

描述

Total number of mac-forwarding entries

快速转发表项数目

SIP

源IP地址

SPort

源端口号

DIP

目的IP地址

DPort

目的端口号

Pro

协议号

Input_If

报文入接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及入接口，"-"表示接口不存在）

Output_If

报文出接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及出接口，"-"表示接口不存在）

VLAN

VLAN ID

**二层转发 \-- 快速二层转发配置命令 \-- display mac-forwarding cache ip fragment**

------------------------------------------------------------------------

![说明](二层转发命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **mac-forwarding cache ip fragment**]命令用来显示分片报文快速转发表信息。

【命令】

集中式设备：

**[display mac-forwarding cache ip fragment** *ip-address* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display mac-forwarding cache ip fragment** *ip-address* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display mac-forwarding cache ip fragment** *ip-address* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定IP地址的分片报文快速转发表信息。如果不指定*ip-address*，将显示所有分片报文快速转发表信息。

**[slot** *slot-number*]：显示指定单板的分片报文快速转发表信息。如果不指定**slot** *slot-number*，将显示所有单板的分片报文快速转发表信息。*slot-number*表示单板的槽位号，取值范围请以设备的实际情况为准。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的分片报文快速转发表信息。如果不指定**slot** *slot-number*，将显示所有成员设备的分片报文快速转发表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的分片报文快速转发表信息。如果不指定**slot** *slot-number*，将显示所有成员设备/PEX的分片报文快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的分片报文快速转发表信息。如果不指定**chassis** *chassis-number* **slot** *slot-number*，将显示所有成员设备上所有单板的分片报文快速转发表信息。*chassis-number*表示设备在IRF中的成员编号。*slot-number*表示单板的槽位号，取值范围请以设备的实际情况为准。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的分片报文快速转发表信息。如果不指定**chassis** *chassis-number* **slot** *slot-number*，将显示所有成员设备上所有单板的分片报文快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号。*slot-number*表示单板或PEX的槽位号，取值范围请以设备的实际情况为准。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上分片报文快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示分片报文快速转发表信息。

\<Sysname\> display mac-forwarding cache ip fragment

Total number of fragment mac-forwarding entries: 2

SIP             SPort DIP             DPort Pro Input_If    ID     VLAN

1.1.1.1         117   1.1.1.2         0     1   GE1/5/0/47  2828   1

1.1.1.2         110   1.1.1.1         67    17  GE1/5/0/48  2322   1

表1-3 display mac-forwarding cache ip fragcache 命令显示信息描述表

字段

描述

Total number of fragment mac-forwarding entries

分片报文快速转发表项数目

SIP

源IP地址

SPort

源端口号

DIP

目的IP地址

DPort

目的端口号

Pro

协议号

Input_If

报文入接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及入接口，"-"表示接口不存在）

ID

分片IP报文ID

VLAN

VLAN ID

**二层转发 \-- 快速二层转发配置命令 \-- display mac-forwarding cache ipv6**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display mac-forwarding cache** **ipv6**]命令用来显示IPv6快速转发表信息。

【命令】

集中式设备：

**[display mac-forwarding cache ipv6** [ *ipv6-address* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display mac-forwarding cache ipv6** [ *ipv6-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display mac-forwarding cache** **ipv6** [ *ipv6-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-address*]：显示指定IPv6地址的IPv6快速转发表信息。如果不指定*ipv6-address*，将显示所有IPv6地址的IPv6快速转发表信息。

**[slot**]*slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备/PEX的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上IPv6快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示IPv6快速转发表信息。

\<Sysname\> display mac-forwarding cache ipv6

Total number of IPv6 mac-forwarding items: 1

Src IP: 2002::1                                        Src port: 129

Dst IP: 2001::1                                        Dst port: 65535

VLAN ID: 2

Protocol: 2

Input interface: GE1/0/2

Output interface: GE1/0/1

表1-4  display mac-forwarding cache ipv6命令显示信息描述表

字段

描述

Total number of IPv6 mac-forwarding items

IPv6快速转发表项数目

Src IP

源IPv6地址

Src port

源端口号

Dst IP

目的IPv6地址

Dst Port

目的端口号

VLAN ID

VLAN ID

Protocol

协议号

Input interface

报文入接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及入接口，"-"表示接口不存在）

Output interface

报文出接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及出接口，"-"表示接口不存在）

**二层转发 \-- 直通转发配置命令 \-- cut-through enable**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[cut-through enable**]命令用来开启设备的直通转发功能。

**[undo cut-through enable**]命令用来恢复缺省情况。

【命令】

**[cut-through enable**]

**[undo cut-through enable**]

【缺省情况】

设备直通转发功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·直通转发是设备接收到报文的前64个字节后立即转发。该功能可以节省报文在设备中消耗的时间，提高转发性能。

·报文在CRC（Cyclic Redundancy Code，循环冗余校验码）接收前已经转发，因此设备也将转发CRC校验错误的报文。

【举例】

\#开启设备的直通转发功能。

\<Sysname\> system-view

Sysname cut-through enable

**二层转发 \-- Bridge转发配置命令 \-- add interface**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[add interface**]命令用来向反射/透传模式Bridge转发实例添加接口。

**[undo add interface**]命令用来删除反射/透传模式Bridge转发实例中的接口。

【命令】

**[add interface ***interface-type interface-number*]

**[undo add interface ***interface-type interface-number*]

【缺省情况】

反射/透传模式Bridge转发实例中没有添加任何接口。

【视图】

反射模式Bridge视图/透传模式Bridge视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：表示接口类型和编号。

【使用指导】

·此命令只在反射模式Bridge视图/透传模式Bridge视图下生效。

·仅支持添加二层或者三层物理接口到反射/透传模式Bridge转发实例。

·每个反射模式Bridge转发实例只能添加一个接口；每个透传模式Bridge转发实例只能添加两个接口，且这两个接口的类型必须保持一致。同一个接口不能添加到不同的Bridge转发实例。

·若在反射模式Bridge视图下多次配置本命令，则以最新配置为准；若在透传模式Bridge视图下多次配置本命令，则以最近两次的配置为准。

【举例】

\# 配置接口GigabitEthernet1/0/1加入Bridge 1。

\<Sysname\> system-view

Sysname bridge 1

Sysname-bridge1-reflect add interface gigabitethernet 1/0/1

**二层转发 \-- Bridge转发配置命令 \-- add vlan**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[add vlan**]命令用来向跨VLAN模式Bridge转发实例中添加VLAN。

**[undo add vlan**]命令用来删除跨VLAN模式Bridge转发实例中添加的VLAN。

【命令】

**[add vlan ***vlan-id-list*]

**[undo add vlan ** *vlan-id-list* ]

【视图】

跨VLAN模式Bridge视图

【缺省情况】

跨VLAN模式Bridge转发实例下没有任何VLAN。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id-list*]：VLAN列表。表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以重复输入10次。

【使用指导】

·此命令只在跨VLAN模式Bridge视图或透传模式Bridge视图下生效。

·不论VLAN是否被创建，都可以加入到Bridge转发实例中。

·如果多次配置**add vlan**命令，那么加入到Bridge转发实例中的VLAN是多次配置的合集。

·同一个VLAN不能加入到不同Bridge转发实例中。

·执行**undo add vlan**命令的时候，如果没有指定*vlan-id-list*参数，则表示删除跨VLAN模式Bridge转发实例中的所有VLAN。

【举例】

\# 向Bridge 2添加VLAN 2、3、5、50～70。

\<Sysname\> system-view

Sysname bridge 2 inter-vlan

Sysname-bridge2-inter-vlan add vlan 2 3 5 50 to 70

**二层转发 \-- Bridge转发配置命令 \-- bridge**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bridge**]命令用来创建指定转发模式的Bridge转发实例，并进入Bridge视图。

**[undo bridge**]命令用来取消Bridge转发实例的配置。

【命令】

**[bridge ***bridge-index*[ [ **forward** \| **inter-vlan** \| **reflect** ]]]

**[undo bridge**[ { *bridge-index \|* **all** }]]

【缺省情况】

未创建任何Bridge转发实例。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bridge-index*]：Bridge转发实例索引信息，范围1～10。

**[forward**]：指定Bridge转发实例的转发模式为透传模式。

**[inter-vlan**]：指定Bridge转发实例的转发模式为跨VLAN模式。

**[reflect**]：指定Bridge转发实例的转发模式为反射模式。

**[all**]：删除全部Bridge转发实例。

【使用指导】

·指定不同的转发模式后，会进入不同模式的Bridge视图。

·通过本命令创建Bridge转发实例时，必须指定其转发模式。如果指定的Bridge转发实例已创建，则直接进入该Bridge转发实例对应的视图，不需要再指定其工作模式。

·一个Bridge转发实例只能配置一种转发模式。

【举例】

\# 创建Bridge 3，配置其转发模式为透传模式。

\<Sysname\> system-view

Sysname bridge 3 forward

Sysname-bridge3-forward

\# 创建Bridge 2，配置其转发模式为跨VLAN模式。

\<Sysname\> system-view

Sysname bridge 2 inter-vlan

Sysname-bridge2-inter-vlan

\# 创建Bridge 1，配置其转发模式为反射模式。

\<Sysname\> system-view

Sysname bridge 1 reflect

Sysname-bridge1-reflect

**二层转发 \-- Bridge转发配置命令 \-- bridge mac-address timer aging**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[bridge mac-address timer aging**]命令用来设置Bridge转发的MAC地址的老化时间。

**[unod bridge mac-address timer aging**]命令用来恢复缺省情况。

【命令】

**[bridge mac-address timer aging** *seconds*]

**[unod bridge mac-address timer aging**]

【视图】

系统视图

【缺省情况】

Bridge转发的MAC的老化时间为300秒。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：设置MAC地址老化时间，单位为秒。

【使用指导】

当网络拓扑改变后，动态MAC地址表项不会及时自动更新。这样，由于设备学习不到新的MAC地址，会导致用户流量不能正常转发。因此，需要配置动态MAC地址表项老化时间。超出设定的老化时间，动态MAC地址表项被自动删除，设备重新进行MAC地址学习，构建新的动态MAC地址表项。

用户配置的MAC地址老化时间过长或者过短，都可能影响设备的运行性能：

·如果用户配置的老化时间过长，设备可能会保存许多过时的MAC地址表项，从而耗尽MAC地址表资源，导致设备无法根据网络的变化更新MAC地址表。

·如果用户配置的老化时间太短，设备可能会删除有效的MAC地址表项，可能导致设备广播大量的数据报文，影响设备的运行性能。

所以用户需要根据实际情况，配置合适的老化时间来有效的实现MAC地址老化功能。

【举例】

\# 设置Bridge转发的MAC地址老化时间500秒。

\<Sysname\> system-view

Sysname bridge mac-address timer aging 500

**二层转发 \-- Bridge转发配置命令 \-- display bridge mac-address**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display bridge mac-address**]命令用来显示Bridge转发学习的MAC地址信息。

【命令】

集中式设备：

**[display bridge mac-address** [ *bridge-index* [ **vlan** *vlan-id*  ]  **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display bridge mac-address** [ *bridge-index* [ **vlan** *vlan-id*  ]  **count**   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display bridge mac-address** [ *bridge-index* [ **vlan** *vlan-id*  ]  **count**   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[bridge-index*]：显示指定Bridge转发实例的MAC地址。

**[vlan*** vlan-id*]：显示指定VLAN内的MAC地址。

**[count**]：显示MAC地址表项的数量。如果配置本参数，将仅显示符合条件的（由**count**前面的参数决定）MAC地址表项的数量，而不显示MAC地址表项的具体内容。如果不指定本参数，则显示符合条件的MAC地址表的具体内容。

**[slot**]* slot-number*：显示指定单板的MAC地址信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的MAC地址信息。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的MAC地址信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示主用设备的MAC地址信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的MAC地址信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示主用设备的MAC地址信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：显示指定成员设备上指定单板的MAC地址信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板的MAC地址信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：显示指定单板的MAC地址信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板的MAC地址信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上的MAC地址信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果未指定任何参数，将显示所有Bridge转发实例的MAC地址信息。

·Bridge转发中的MAC地址全部是学习的地址，使用本命令查看的MAC地址都是动态MAC地址。

【举例】

\# 显示Bridge 100的MAC地址表项的信息。

\<Sysname\> display bridge mac-address 100

MAC Address      BRIDGE ID  State        VLAN ID  Port            Aging

0033-0033-0033   100        Learned      44       GE1/0/1         Y

0000-0000-0002   100        Learned      66       GE1/0/2         Y

00e0-fc00-5829   100        Learned      88       GE1/0/3         Y

\# 显示Bridge 100的MAC地址表项的数量。

\<Sysname\> display bridge mac-address 100 count

1 mac address(es) found.

表1-5 display bridge mac-address命令显示信息描述表

字段

描述

MAC Address

MAC地址

BRIDGE ID

MAC地址所属的Bridge索引

State

MAC地址表项的状态，取值为Learned，动态MAC地址表项。

VLAN ID

出端口所在的VLAN

Port

出端口

Aging

老化时间，该表项有两种取值：

·Y：表示该表项会被老化

·N：表示该表项不会被老化

1 mac address(es) found

共有1个MAC地址表项

**二层转发 \-- Bridge转发配置命令 \-- mac-address max-mac-count**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-address max-mac-count**]命令用来配置Bridge实例下MAC地址最大学习数。

**[mac-address max-mac-count**]命令用来恢复缺省情况。

【命令】

**[mac-address max-mac-count ***count*]

**[undo mac-address max-mac-count**]

【视图】

跨VLAN模式Bridge视图

【缺省情况】

Bridge转发实例的MAC地址最大学习数为4096。

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：Bridge转发实例的MAC地址数学习上限，取值范围为0～4096，0即表示不允许该Bridge转发实例学习MAC地址。

【使用指导】

通过配置Bridge转发实例的MAC地址数学习上限，用户可以控制设备维护的Bridge的MAC地址表的表项数量。当Bridge实例学习到的MAC地址数达到上限时，该Bridge转发实例将不再对MAC地址进行学习。

【举例】

\# 配置Bridge 2的最大MAC学习数

\<Sysname\> system-view

Sysname bridge 2 inter-vlan

Sysname-bridge2-inter-vlan mac-address max-mac-count 10

**二层转发 \-- 快速Bridge转发配置命令 \-- display bridge cache ip**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display bridge cache ip**]命令用来显示Bridge转发创建的IP快速转发表信息。

【命令】

集中式设备：

**[display bridge cache ip** [ *ip-address* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display bridge cache ip** [ *ip-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display bridge cache ip** [ *ip-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定IP地址的快速转发表信息。如果不指定*ip-address*，将显示所有快速转发表信息。

**[slot**]*slot-number*：显示指定单板的快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的快速转发表信息。*slot-number*表示单板的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果不指定**slot***slot-number*，将显示所有成员设备的快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定**slot***slot-number*，将显示所有成员设备/PEX的快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示Bridge转发创建的IP快速转发表信息。

\<Sysname\> display bridge cache ip

Total number of bridge-forwarding entries: 2

SIP             SPort DIP             DPort Pro InVLAN OutVLAN Output_If

1.1.1.3         470   1.1.1.2         0     1   3      2       XGE9/0/29

1.1.1.2         470   1.1.1.3         2048  1   2      3       XGE9/0/30

表1-6 display bridge cache ip命令显示信息描述表

字段

描述

Total number of bridge-forwarding entries

快速转发表项数目

SIP

源IP地址

SPort

源端口号

DIP

目的IP地址

DPort

目的端口号

Pro

协议号

InVLAN

报文入VLAN

OutVLAN

报文出VLAN

Output_If

报文出接口

**二层转发 \-- 快速Bridge转发配置命令 \-- display bridge cache ip fragment**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display**  **bridge cache ip fragment**]命令用来显示Bridge转发创建的分片报文快速转发表信息。

【命令】

集中式设备：

**[display bridge cache ip fragment** *ip-address* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display bridge cache ip fragment** *ip-address* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display bridge cache ip fragment** *ip-address* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定IP地址的分片报文快速转发表信息。如果不指定*ip-address*，将显示所有分片报文快速转发表信息。

**[slot** *slot-number*]：显示指定单板的分片报文快速转发表信息。如果不指定**slot** *slot-number*，将显示所有单板的分片报文快速转发表信息。*slot-number*表示单板的槽位号，取值范围请以设备的实际情况为准。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的分片报文快速转发表信息。如果不指定**slot** *slot-number*，将显示所有成员设备的分片报文快速转发表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的分片报文快速转发表信息。如果不指定**slot** *slot-number*，将显示所有成员设备/PEX的分片报文快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的分片报文快速转发表信息。如果不指定**chassis** *chassis-number* **slot** *slot-number*，将显所有单板的分片报文快速转发表信息。*chassis-number*表示设备在IRF中的成员编号。*slot-number*表示单板的槽位号，取值范围请以设备的实际情况为准。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的分片报文快速转发表信息。如果不指定**chassis** *chassis-number* **slot** *slot-number*，将显示所有单板的分片报文快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号。*slot-number*表示单板或PEX的槽位号，取值范围请以设备的实际情况为准。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上分片报文快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示Bridge转发创建的分片报文快速转发表信息。

\<Sysname\> display bridge cache ip fragment

Total number of fragment bridge-forwarding entries: 2

SIP             SPort DIP             DPort Pro InVLAN ID

2.1.1.2         2320  2.1.1.1         2048  1   2      7298

2.1.1.1         2048  2.1.1.2         2320  1   3      6826

表1-7 display bridge fragcache ip命令显示信息描述表

字段

描述

Total number of fragment bridge-forwarding entries

分片报文快速转发表项数目

SIP

源IP地址

SPort

源端口号

DIP

目的IP地址

DPort

目的端口号

Pro

协议号

InVLAN

报文入VLAN

ID

分片IP报文ID

**二层转发 \-- 快速Bridge转发配置命令 \-- display bridge cache ipv6**

------------------------------------------------------------------------

![说明](二层转发命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display bridge cache ipv6**]命令用来显示Bridge转发创建的IPv6快速转发表信息。

【命令】

集中式设备：

**[display bridge cache ipv6** [ *ipv6-address* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display bridge cache ipv6** [ *ipv6-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display bridge cache ipv6** [ *ipv6-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-address*]：显示指定IPv6地址的IPv6快速转发表信息。如果不指定*ipv6-address*，将显示所有IPv6地址的IPv6快速转发表信息。

**[slot**]*slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[slot**]* slot-number*：显示指定成员设备的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上IPv6快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示Bridge转发创建的IPv6快速转发表信息。

\<Sysname\> display bridge cache ipv6

Total number of IPv6 bridge-forwarding items: 1

Src IP: 10::12                                         Src Port: 427

Dst IP: 10::11                                         Dst Port: 32768

InVLAN: 2                                              OutVLAN: 3

Protocol: 58

Context ID: 257

Bridge ID: 10

Output interface: XGE9/0/30

表1-8 display bridge cache ipv6命令显示信息描述表

字段

描述

Total number of IPv6 bridge-forwarding items

IPv6快速转发表项数目

Src IP

源IPv6地址

Src port

源端口号

Dst IP

目的IPv6地址

Dst Port

目的端口号

InVLAN

报文入VLAN

OutVLAN

报文出VLAN

Protocol

协议号

Context ID

CONTEXT ID

Bridge ID

Bridge转发实例ID

Output interface

报文出接口类型和接口号（"N/A"表示接口存在但是该快速转发不涉及出接口，"-"表示接口不存在）

