
**策略路由 \-- 策略路由配置命令 \-- apply access-vpn vpn-instance**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply access-vpn vpn-instance**]命令用来设置报文在指定VPN实例中进行转发。

**[undo apply access-vpn vpn-instance**]命令用来取消报文在指定VPN实例中进行转发的设置或者删除一个或多个指定的VPN实例对应的配置。

【命令】

**[apply access-vpn vpn-instance*** vpn-instance-name*&\<1-*n*\>]

**[undo apply access-vpn vpn-instance** [ *vpn-instance-name*&\<1-*n*\> ]]

【缺省情况】

未设置报文在指定VPN实例中进行转发。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。指定的VPN实例必须已经存在。

&\<1-*n*\>：表示前面的参数最多可以输入*n*次。*n*的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

每个节点最多可以配置*m*个VPN实例。当满足匹配规则后，将根据第一个可用的VPN实例转发表进行转发。*m*的取值与设备的型号有关，请以设备的实际情况为准。

配置**undo**命令时，如果指定了VPN实例名，将删除该VPN实例对应的配置；如果未指定VPN实例名，将取消报文在指定VPN实例内转发的配置。

【举例】

\# 在策略节点中设置报文在名为vpn1、vpn2的VPN实例中进行转发（VPN实例vpn1、vpn2已存在）。

\<Sysname\> system-view

Sysname policy-based-route policy1 permit node 10

Sysname-pbr-policy1-10 apply access-vpn vpn-instance vpn1 vpn2

**策略路由 \-- 策略路由配置命令 \-- apply continue**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply continue**]命令用来设置匹配成功的当前节点指定转发路径失败后，继续进行后续节点的处理。

**[undo apply continue**]命令用来恢复缺省情况。

【命令】

**[apply continue**]

**[undo apply continue**]

【缺省情况】

匹配成功的当前节点指定转发路径失败后，不再进行下一节点的匹配。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令仅在策略节点的匹配模式为**permit**时生效。

在配置了该命令后，如果当前节点中没有配置影响报文转发路径的五个**apply**子句（**apply access-vpn vpn-instance**、**apply next-hop**、**apply output-interface**、**apply default-next-hop**和**apply default-output-interface**），或者配置了这五个子句中的一个或多个，但配置的子句都失效（下一跳不可达、出接口down或者报文在指定VPN内转发失败）时，会进行下一节点的处理。

【举例】

\# 设置匹配成功的当前节点转发失败后继续进行后续节点的处理。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply continue

**策略路由 \-- 策略路由配置命令 \-- apply default-next-hop**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply default-next-hop**]命令用来设置指导报文转发的缺省下一跳。

**[undo apply default-next-hop**]命令用来取消指导报文转发的缺省下一跳的设置。

【命令】

**[apply default-next-hop **\**[vpn-instance**[ *vpn-instance-name \|* **inbound-vpn** ] { *ip-address*  **direct**   **track** *track-entry-number*  }&\<1-*n*\>]]

**[undo apply default-next-hop **[[ [ **vpn-instance** *vpn-instance-name \|* **inbound-vpn** ] *ip-address*&\<1-*n*\> ]]]

【缺省情况】

未设置指导报文转发的缺省下一跳。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：缺省下一跳所在的VPN实例。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。指定的VPN实例必须已经存在。

**[inbound-vpn**]：报文入接口所在的VPN实例。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ip-address*]：缺省下一跳的IP地址。不指定**vpn-instance**或**inbound-vpn**参数，表示指定的是公网下一跳。

**[direct**]：指定当前缺省下一跳生效的条件为直连下一跳。

**[track** *track-entry-number*]：指定Track项的序号，*track-entry-number*取值范围为1～1024。

&\<1-*n*\>：表示前面的参数最多可以输入*n*次。*n*的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以同时配置多个缺省下一跳（通过一次或多次配置本命令实现），起到主备或负载分担的作用。

每个节点最多可以配置*m*个缺省下一跳。*m*的取值与设备的型号有关，请以设备的实际情况为准。

配置**undo**命令时，如果指定了缺省下一跳IP地址，将取消已配置的该缺省下一跳；如果没有指定缺省下一跳IP地址，将取消已配置的所有缺省下一跳。

【举例】

\# 设置指导报文转发的缺省直连下一跳为1.1.1.1。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply default-next-hop 1.1.1.1 direct

【相关命令】

·**apply loadshare**

**策略路由 \-- 策略路由配置命令 \-- apply default-output-interface**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply default-output-interface**]命令用来设置指导报文转发的缺省出接口。

**[undo apply default-output-interface**]命令用来取消指导报文转发的缺省出接口的设置。

【命令】

**[apply default-output-interface ***[interface-type interface-number * **track** *track-entry-number* ] }&\<1-*n*\>]

**[undo apply default-output-interface** [{ *interface-type interface-number* }&\<1-*n*\> ]]

【缺省情况】

未设置指导报文转发的缺省出接口。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。

**[track ***track-entry-number*]：指定Track项的序号，*track-entry-number*取值范围为1～1024。

&\<1-*n*\>：表示前面的参数最多可以输入*n*次。*n*的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以同时配置多个缺省出接口（通过一次或多次配置本命令实现），起到主备或负载分担的作用。

每个节点最多可以配置*m*个缺省出接口。*m*的取值与设备的型号有关，请以设备的实际情况为准。

指定缺省出接口类型需配置为P2P（Point-to-Point，点到点）接口，对于非P2P接口（广播类型的接口和NBMA类型的接口），比如以太网接口、Virtual-Template接口，由于有多个可能的下一跳，可能会造成报文转发不成功的现象。NBMA（Non Broadcast MultiAccess，非广播多路访问）指全连通、非广播、多点可达的网络，这种网络采用单播方式发送报文。

配置**undo**命令时，如果指定了接口，将取消已配置的该缺省出接口；如果没有指定接口，将取消已配置的所有缺省出接口。

【举例】

\# 设置报文的缺省出接口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply default-output-interface gigabitethernet 1/0/1

【相关命令】

·**apply loadshare**

**策略路由 \-- 策略路由配置命令 \-- apply ip-df**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply ip-df**]命令用来设置IP报文头中的DF（Don't Fragment，不分片）标志。

**[undo apply ip-df**]命令用来恢复缺省情况。

【命令】

**[apply ip-df ***df-value*]

**[undo apply ip-df**]

【缺省情况】

不对IP报文头中的DF标志进行设置。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[df-value*]：设置IP报文头中的DF标志，取值0或1。0表示将IP报文头中的DF标志位置为0；1表示将IP报文头中的DF标志位置为1。

【使用指导】

报文中DF标志位置为0，表示可以对报文进行分片处理。

报文中DF标志位置为1，表示不可对报文进行分片处理。

【举例】

\# 将报文IP首部的DF标志位置为0。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply ip-df 0

**策略路由 \-- 策略路由配置命令 \-- apply loadshare**

------------------------------------------------------------------------

**[apply loadshare**]命令用来设置多个下一跳(出接口、缺省下一跳和缺省出接口)工作在负载分担模式。

**[undo apply loadshare**]命令用来恢复缺省情况。

【命令】

**[apply loadshare**[ { **default-next-hop** \| **default-output-interface** \| **next-hop \| output-interface** }]]

**[undo apply loadshare**[ { **default-next-hop** \| **default-output-interface** \| **next-hop \| output-interface** }]]

【缺省情况】

多个下一跳(出接口、缺省下一跳和缺省出接口)工作在主备模式。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[default-next-hop**]：设置指导报文转发的多个缺省下一跳工作在负载分担模式。

**[default-output-interface**]：设置指导报文转发的多个缺省出接口工作在负载分担模式。

**[next-hop**]：设置指导报文转发的多个下一跳工作在负载分担模式。

**[output-interface**]：设置指导报文转发的多个出接口工作在负载分担模式。

【使用指导】

多个出接口(下一跳、缺省下一跳和缺省出接口)的工作模式有两种：主备模式、负载分担模式。以多个出接口为例：

·主备模式：按照配置顺序，以第一个配置的出接口作为主用出接口，指导报文转发。当主用出接口失效时，按配置顺序选择后续的第一个有效的出接口指导报文转发。

·负载分担模式：按照配置顺序，逐包轮流选择有效的出接口指导报文转发。下一跳的负载分担模式则有些不同，会按照下一跳的权重指导报文转发。缺省情况下，多个下一跳会按照缺省的权重值平均分配带宽，多个下一跳的转发流量的比例是相同的。

缺省下一跳和缺省出接口的情况请参考多个出接口。

【举例】

\# 设置多个下一跳工作在负载分担模式。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply next-hop 1.1.1.1 2.2.2.2

Sysname-pbr-aa-11 apply loadshare next-hop

\# 设置多个出接口工作在负载分担模式。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply output-interface Vlan-interface 1 Vlan-interface 2

Sysname-pbr-aa-11 apply loadshare output-interface

\# 设置多个缺省下一跳工作在负载分担模式。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply default-next-hop 1.1.1.1 2.2.2.2

Sysname-pbr-aa-11 apply loadshare default-next-hop

\# 设置多个缺省出接口工作在负载分担模式。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply default-output-interface Vlan-interface 1 Vlan-interface 2

Sysname-pbr-aa-11 apply loadshare default-output-interface

【相关命令】

·**apply default-next-hop**

·**apply default-output-interface**

·**apply next-hop**

·**apply output-interface**

**策略路由 \-- 策略路由配置命令 \-- apply next-hop**

------------------------------------------------------------------------

![说明](策略路由命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[apply next-hop**]命令用来设置报文转发的下一跳。

**[undo apply next-hop**]命令用来取消报文转发下一跳的设置。

【命令】

**[apply next-hop**[ [ **vpn-instance** *vpn-instance-name* \| **inbound-vpn** ] { *ip-address*  **direct**   **track** *track-entry-number*   **weight** *weight-value*  }&\<1-*n*\>]]

**[undo apply next-hop**[ [ [ **vpn-instance** *vpn-instance-name* \| **inbound-vpn** ] *ip-address*&\<1-*n*\> ]]]

【缺省情况】

未设置报文转发的下一跳。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：下一跳所在的VPN实例。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。指定的VPN实例必须已经存在。

**[inbound-vpn**]：报文入接口所在的VPN实例。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ip-address*]：下一跳IP地址。不指定**vpn-instance**或**inbound-vpn**参数，表示指定的是公网下一跳。

**[direct**]：指定当前下一跳生效的条件为直连下一跳。

**[track ***track-entry-number*]：指定Track项的序号，*track-entry-number*取值范围为1～1024。

&\<1-*n*\>：表示前面的参数最多可以输入*n*次。*n*的取值与设备的型号有关，请以设备的实际情况为准。

**[weight ***weight-value*]：指定下一跳负载分担的权重。设备根据权重确定该下一跳转发流量的比例。例如，三个下一跳配置的负载分担权重分别为1、1和2，则它们的负载分担的比例分别为1/4、1/4和1/2。*weight-value*取值范围为1～100，缺省值为10。

【使用指导】

用户可以同时配置多个下一跳（通过一次或多次配置本命令实现），起到主备或负载分担的作用。

每个节点最多可以配置*m*个下一跳。*m*的取值与设备的型号有关，请以设备的实际情况为准。

配置**undo**命令时，如果指定了下一跳IP地址，将取消已配置的该下一跳；如果没有指定下一跳IP地址，将取消已配置的所有下一跳。

【举例】

\# 设置报文的直连下一跳为1.1.1.1。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply next-hop 1.1.1.1 direct

【相关命令】

·**apply loadshare**

**策略路由 \-- 策略路由配置命令 \-- apply output-interface**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply output-interface**]命令用来设置指导报文转发的出接口。

**[undo apply output-interface**]命令用来取消指导报文转发的出接口的设置。

【命令】

**[apply output-interface **{ *interface-type interface-number* [ **track** *track-entry-number*  }&\<1-*n*\>]]

**[undo apply output-interface ** { *interface-type* *interface-number* }&\<1-*n*\> ]

【缺省情况】

未设置指导报文转发的出接口。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定接口类型和接口编号。

**[track ***track-entry-number*]：指定Track项的序号，*track-entry-number*取值范围为1～1024。

&\<1-*n*\>：表示前面的参数最多可以输入*n*次。*n*的取值与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以同时配置多个出接口（通过一次或多次配置本命令实现），起到主备或负载分担的作用。

每个节点最多可以配置*m*个出接口。*m*的取值与设备的型号有关，请以设备的实际情况为准。

指定出接口类型需配置为P2P接口，对于非P2P接口（广播类型的接口和NBMA类型的接口），比如以太网接口、Virtual-Template接口，由于有多个可能的下一跳，可能会造成报文转发不成功的现象。

配置**undo**命令时，如果指定了接口，将取消已配置的该出接口；如果未指定接口，将取消已配置的所有出接口。

【举例】

\# 对已经匹配的IP报文指定出接口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply output-interface gigabitethernet 1/0/1

【相关命令】

·**apply loadshare**

**策略路由 \-- 策略路由配置命令 \-- apply precedence**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[apply precedence****]命令用来设置IP报文的优先级。

**[undo apply precedence**]命令用来恢复缺省情况。

【命令】

**[apply precedence **[{ *type* \| *value* }]]

**[undo apply precedence**]

【缺省情况】

不对IP报文的优先级进行设置。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[type*]：IP报文的优先级类型。

*[value*]：IP报文的优先级值，IP报文共有8（0～7）个优先级，每个数值对应一个优先级类型。在输入参数的时候可以输入数值，也可以输入优先级类型。对应关系如[表]1-1(?908845892#_Ref329186298)所示。

表1-1 IP优先级值与优先级类型对应表

优先级值

优先级类型

0

routine

1

priority

2

immediate

3

flash

4

flash-override

5

critical

6

internet

7

network

【举例】

\# 设置IP报文的优先级为5（critical）。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 apply precedence critical

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route**

------------------------------------------------------------------------

**[display ip policy-based-route**]命令用来显示已经配置的策略。

【命令】

**[display ip policy-based-route **\**[ policy ***policy-name *]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[policy*** policy-name*]：显示指定的策略。*policy-name*表示策略名，唯一标识一个策略，为1～19个字符的字符串，区分大小写。

【使用指导】

如果不指定策略名，将显示所有已经配置的策略；如果指定策略名，将显示指定的策略。

【举例】

\# 显示所有已经配置的策略。

\<Sysname\> display ip policy-based-route

Policy name: aaa

  node 1 permit:

    if-match acl 2000

    apply next-hop 1.1.1.1

表1-2 display ip policy-based-route命令显示信息描述表

字段

描述

Policy name

策略名

node 1 permit

节点1的匹配模式为允许

if-match acl

满足ACL的报文被匹配

apply next-hop

为匹配的报文指定下一跳

【相关命令】

·**policy-based-route**

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route interface**

------------------------------------------------------------------------

**[display ip policy-based-route interface**]命令用来显示接口下转发策略路由的配置信息和统计信息。

【命令】

集中式设备：

**[display ip policy-based-route interface ***interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display ip policy-based-route interface ***interface-type interface-number* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ip policy-based-route interface ***interface-type interface-number***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：用来指定接口的类型和编号。

**[slot*** slot-number*]：显示指定单板上转发策略路由的配置信息和统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上转发策略路由的配置信息和统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的转发策略路由的配置信息和统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上转发策略路由的配置信息和统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的转发策略路由的配置信息和统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上转发策略路由的配置信息和统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示接口GigabitEthernet1/0/1下转发策略路由的配置信息和统计信息。

\<Sysname\> display ip policy-based-route interface gigabitethernet 1/0/1

Policy based routing information for interface GigabitEthernet1/0/1(failed):

Policy name: aaa

  node 0 deny:

  Matched: 0

  node 1 permit:

    if-match acl 3999

  Matched: 0

  node 2 permit:

    if-match acl 2000

    apply next-hop 2.2.2.2

  Matched: 0

  node 5 permit:

    if-match acl 3101

    apply next-hop 1.1.1.1

    apply output-interface GigabitEthernet1/0/2 track 1 (down)

    apply output-interface GigabitEthernet1/0/3 track 2 (inactive)

  Matched: 0

Total matched: 0

\<Sysname\> display ip policy-based-route interface gigabitethernet 1/0/1

Policy based routing information for interface GigabitEthernet1/0/1:

Policy name: aaa

  node 0 deny(not support):

  Matched: 0

  node 1 permit:

    if-match acl 3999

  Matched: 0

  node 2 permit(no resource):

    if-match acl 2000

    apply next-hop 2.2.2.2

    apply output-interface GigabitEthernet1/0/2 track 1 (down)

    apply output-interface GigabitEthernet1/0/3 track 2 (inactive)

  Matched: 0

  node 5 permit:

    if-match acl 3101

    apply next-hop 1.1.1.1

  Matched: 0 (no statistics resource)

Total matched: 0

表1-3 display ip policy-based-route interface命令显示信息描述表

字段

描述

Policy based routing information for interface GigabitEthernet1/0/1(failed)

接口GigabitEthernet1/0/1下转发策略路由的配置信息和统计信息（failed表示策略下发驱动失败，此时所有节点都下发失败，不再显示节点一级的失败提示）

![说明](策略路由命令.files/image001.png)

显示全局接口（全局接口只有一维编号，例如VLAN接口10）的信息时，必须在命令中指定**slot*** slot-number*或**chassis** *chassis-number* **slot** *slot-number*参数，才会显示括号中的信息。

Policy name

策略名

node 0 deny(not support)

node 2 permit(no resource)

节点的匹配模式为允许（permit）/拒绝（deny）。（not support表示设备不支持该节点设置的规则；no resource表示设备的ACL等资源不足，为该节点分配ACL等资源失败）

![说明](策略路由命令.files/image001.png)

显示全局接口（全局接口只有一维编号，例如VLAN接口10）的信息时，必须在命令中指定**slot*** slot-number*或**chassis** *chassis-number* **slot** *slot-number*参数，才会显示括号中的信息。

if-match acl

满足ACL的报文被匹配

apply next-hop

为匹配的报文指定下一跳

apply output-interface GigabitEthernet1/0/2 track 1 (down)

为匹配的报文指定出接口。括号中显示接口的状态：up、down、inactive。接口不在位时，显示inactive；接口网络层down时，显示down

Matched: 0 (no statistics resource)

节点匹配成功的次数（no statistics resource表示统计资源不足）

![说明](策略路由命令.files/image001.png)

显示全局接口（全局接口只有一维编号，例如VLAN接口10）的信息时，必须在命令中指定**slot*** slot-number*或**chassis** *chassis-number* **slot** *slot-number*参数，才会显示括号中的信息。

Total matched

策略所有节点匹配成功的次数

【相关命令】

·**reset ip policy-based-route statistics**

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route local**

------------------------------------------------------------------------

**[display ip policy-based-route local**]命令用来显示本地策略路由的配置信息和统计信息。

【命令】

集中式设备：

**[display ip policy-based-route local**]

分布式设备－独立运行模式/集中式IRF设备：

**[display ip policy-based-route local** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display ip policy-based-route local ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板上本地策略路由的配置信息和统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上本地策略路由的配置信息和统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的本地策略路由的配置信息和统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上本地策略路由的配置信息和统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的本地策略路由的配置信息和统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上本地策略路由的配置信息和统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示本地策略路由的配置信息和统计信息。

\<Sysname\> display ip policy-based-route local

Policy based routing information for local:

Policy name: aaa

  node 0 deny:

  Matched: 0

  node 1 permit:

    if-match acl 3999

  Matched: 0

  node 2 permit:

    if-match acl 2000

    apply next-hop 2.2.2.2

  Matched: 0

  node 5 permit:

    if-match acl 3101

    apply next-hop 1.1.1.1

  Matched: 0

Total matched: 0

表1-4 display ip policy-based-route local命令显示信息描述表

字段

描述

Policy based routing information for local

本地策略路由的配置信息和统计信息

Policy name

策略名

node 0 deny/node 2 permit

节点的匹配模式为允许（permit）/拒绝（deny）

if-match acl

满足ACL的报文被匹配

apply next-hop

为匹配的报文指定下一跳

Matched: 0

节点匹配成功的次数

Total matched

策略所有节点匹配成功的次数

【相关命令】

·**reset ip policy-based-route statistics**

**策略路由 \-- 策略路由配置命令 \-- display ip policy-based-route setup**

------------------------------------------------------------------------

**[display ip policy-based-route setup**]命令用来显示已经应用的策略路由信息。

【命令】

**[display ip policy-based-route setup**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示已经应用的策略路由信息。

\<Sysname\> display ip policy-based-route setup

Policy Name              Interface Name

pr01                     GigabitEthernet 1/0/1

表1-5 display ip policy-based-route setup命令显示信息描述表

字段

描述

policy Name

策略名

Interface Name

应用策略的接口

【相关命令】

·**ip policy-based-route**

**策略路由 \-- 策略路由配置命令 \-- if-match acl**

------------------------------------------------------------------------

**[if-match acl**]命令用来设置ACL匹配规则。

**[undo if-match acl**]命令用来删除ACL匹配规则。

【命令】

**[if-match acl**[ { *acl-number \|* **name** *acl-name* }]]

**[undo if-match acl**]

【缺省情况】

未设置ACL匹配规则。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：访问控制列表号，取值范围为2000～3999。其中：

·基本ACL，*acl-number*取值范围为2000～2999；

·高级ACL，*acl-number*取值范围为3000～3999。

**[name*** acl-name*]：指定ACL的名称。*acl-name*表示ACL的名称，为1～63个字符的字符串，不区分大小写，必须以英文字母a～z或A～Z开头。为避免混淆，ACL的名称不允许使用英文单词all。

【举例】

\# 设置满足ACL 2011的报文被匹配。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 if-match acl 2011

\# 设置满足ACL名称为aaa的报文被匹配。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 if-match acl name aaa

**策略路由 \-- 策略路由配置命令 \-- if-match packet-length**

------------------------------------------------------------------------

![说明](策略路由命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[if-match packet-length**]命令用来设置IP报文长度匹配规则。

**[undo if-match packet-length**]命令用来删除IP报文长度匹配规则的设置。

【命令】

**[if-match packet-length** *min-len max-len*]

**[undo if-match packet-length**]

【缺省情况】

未设置IP报文长度匹配规则。

【视图】

策略节点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[min-len*]：最短IP报文长度，取值范围为1～65535，单位为字节。

*[max-len*]：最长IP报文长度，取值范围为1～65535，单位为字节。*max-len*应该不小于*min-len*。

【使用指导】

长度匹配含边界值，如指定*min-len*为100，*max-len*为200，则报文长度为100与200的报文都是匹配报文。

【举例】

\# 设置报文长度在100～200字节之间的报文被匹配。

\<Sysname\> system-view

Sysname policy-based-route aa permit node 11

Sysname-pbr-aa-11 if-match packet-length 100 200

**策略路由 \-- 策略路由配置命令 \-- ip local policy-based-route**

------------------------------------------------------------------------

**[ip local policy-based-route**]命令用来对本地报文应用策略。

**[undo ip local policy-based-route**]命令用来删除对本地报文应用策略的设置。

【命令】

**[ip local policy-based-route** *policy-name*]

**[undo ip local policy-based-route**]

【缺省情况】

对本地报文没有应用策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名，唯一标识一个策略，为1～19个字符的字符串，区分大小写。该策略必须已经存在。

【使用指导】

对本地报文只能应用一个策略。应用新的策略前必须删除本地原来已经应用的策略。

对本地报文应用的策略将对本地产生的所有报文进行匹配。若无特殊需求，建议用户不要配置本地策略路由。

【举例】

\# 对本地报文应用策略aaa。

\<Sysname\> system-view

Sysname ip local policy-based-route aaa

【相关命令】

·**display ip policy-based-route setup**

·**policy-based-route**

**策略路由 \-- 策略路由配置命令 \-- ip policy-based-route**

------------------------------------------------------------------------

**[ip policy-based-route**]命令用来对接口转发的报文应用策略。

**[undo ip policy-based-route**]命令用来删除对接口转发的报文应用的策略。

【命令】

**[ip policy-based-route*** policy-name*]

**[undo ip policy-based-route**]

【缺省情况】

对接口转发的报文没有应用策略。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名，唯一标识一个策略，为1～19个字符的字符串，区分大小写。该策略必须已经存在。

【使用指导】

对接口转发的报文应用策略时，一个接口只能应用一个策略。应用新的策略前必须删除接口上原来已经应用的策略。

【举例】

·路由应用

\# 对接口GigabitEthernet1/0/1转发的报文应用策略aaa。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip policy-based-route aaa

·交换应用

\# 对接口Vlan-interface2转发的报文应用策略aaa。

\<Sysname\> system-view

Sysname vlan 2

Sysname-Vlan2 interface vlan-interface 2

Sysname-Vlan-interface2 ip policy-based-route aaa

【相关命令】

·**display ip policy-based-route setup**

·**policy-based-route**

**策略路由 \-- 策略路由配置命令 \-- policy-based-route**

------------------------------------------------------------------------

**[policy-based-route**]命令用来创建策略节点，并进入策略节点视图。如果指定的策略节点已创建，则该命令直接用来进入该策略节点的视图。

**[undo policy-based-route**]命令用来删除已创建的策略或策略节点。

【命令】

**[policy-based-route**[ *policy-name* [ **deny** \| **permit** ] **node** *node-number*]]

**[undo policy-based-route**[ *policy-name* [ **deny** \| **node** *node-number* \| **permit** ]]]

【缺省情况】

没有创建策略节点。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：策略名，唯一标识一个策略，为1～19个字符的字符串，区分大小写。

**[deny**]：指定策略节点的匹配模式为拒绝模式。

**[permit**]：指定策略节点的匹配模式为允许模式。缺省匹配模式为**permit**。

**[node*** node-number*]：策略节点编号。节点编号越小优先级越高，先对优先级高的节点进行匹配操作。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

删除策略之前，必须先取消该策略在所有接口或者本地上的应用，否则删除失败。

配置**undo**命令时，如果指定了策略节点，将删除指定的节点；如果指定了节点模式，将按模式删除策略内所有与该模式匹配的所有节点；如果两者都没有指定，将删除整个策略。

【举例】

\# 配置一个策略policy1，其节点序列号为10，匹配模式为**permit**，并进入策略节点视图。

\<Sysname\> system-view

Sysname policy-based-route policy1 permit node 10

Sysname-pbr-policy1-10

【相关命令】

·**display ip policy-based-route**

**策略路由 \-- 策略路由配置命令 \-- reset ip policy-based-route statistics**

------------------------------------------------------------------------

**[reset ip policy-based-route statistics**]命令用来清除策略路由的统计信息。

【命令】

**[reset ip policy-based-route statistics** [ **policy** *policy-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[policy ***policy-name*]：清除指定策略的统计信息。*policy-name*表示策略名，唯一标识一个策略，为1～19个字符的字符串，区分大小写。

【使用指导】

系统按照策略名清除策略路由的统计信息。如果不指定策略名，将清除所有配置策略的匹配统计信息（该统计信息可以通过**display ip policy-based-route interface**命令查看）；如果指定策略名，将清除指定策略的匹配统计信息。

【举例】

\# 清除所有配置策略的统计信息。

\<Sysname\> reset ip policy-based-route statistics

【相关命令】

·**display ip policy-based-route interface**

·**display ip policy-based-route local**

**策略路由 \-- 策略路由配置命令 \-- snmp-agent trap enable policy-based-route**

------------------------------------------------------------------------

![说明](策略路由命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[snmp-agent trap enable policy-based-route**]命令用来开启下一跳失效告警功能。

**[undo snmp-agent trap enable policy-based-route**]命令用来关闭下一跳失效告警功能。

【命令】

**[snmp-agent trap enable policy-based-route**]

**[undo snmp-agent trap enable policy-based-route**]

【缺省情况】

下一跳失效告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启策略路由模块的告警功能后，当下一跳的状态由有效变为无效时，该模块会生成包含下一跳地址的告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 启用告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable policy-based-route

