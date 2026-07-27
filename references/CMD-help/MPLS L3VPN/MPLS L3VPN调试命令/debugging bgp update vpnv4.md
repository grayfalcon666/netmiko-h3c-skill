<!-- CMD-INDEX
  debugging bgp update vpnv4          | 用户视图             | L12
  debugging bgp update vpn-instance ipv4 | 用户视图             | L158
  debugging bgp update-group vpnv4    | 用户视图             | L282
  debugging bgp label                 | 用户视图             | L394
  debugging bgp lsp                   | 用户视图             | L512
  debugging bgp update vpnv6          | 用户视图             | L644
  debugging bgp update vpn-instance ipv6 | 用户视图             | L770
  debugging bgp update-group vpnv6    | 用户视图             | L894
-->

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp update vpnv4**

------------------------------------------------------------------------

【命令】

**[debugging bgp update** *ip-address* [ *mask-length*  **vpnv4** [ **receive** \| **send** ]]]

**[undo debugging bgp update** *ip-address* [ *mask-length*  **vpnv4** [ **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：对等体的IP地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

**[receive**]：表示接收的BGP报文。

**[send**]：表示发送的BGP报文。

【描述】

**[debugging bgp update vpnv4**]命令用来打开BGP VPNv4的Update报文调试信息开关。**undo** **debugging bgp vpnv4**命令用来关闭BGP VPNv4的Update报文调试信息开关。

缺省情况下，BGP VPNv4的Update报文调试信息开关处于关闭状态。

表1-1 debugging bgp update vpnv4命令输出信息描述表

字段

描述

BGP_L3VPN.: Recv UPDATE from peer *ip-address* with following destinations

从对等体*ip-address*接收到Update消息

BGP_L3VPN.: Send UPDATE to peer *ip-address* for following destinations

向对等体*ip-address*发送Update消息

Update message length

Update消息的长度，单位为字节

Origin

路由的Origin属性，即路由信息的来源，取值包括：

·IGP：网络层可达信息来源于AS内部

·EGP：网络层可达信息通过EGP学习

·Incomplete：网络层可达信息通过其他方式学习

AS path

路由的AS Path属性，即路由从本地到目的地址所要经过的所有AS号

Next hop

路由的下一跳属性

Local pref

路由的本地优先级

MED

路由的MED（Multi-Exit Discriminator，多出口区分）值

Ext-Community

路由的扩展团体属性

*[prefix/mask *(RD *route-distinguisher*, Label *label*)]

路由前缀为*prefix*、路由前缀的掩码长度为*mask*、RD值为*route-distinguisher*、标签值为*label*

Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*

向地址族*address-family*的对等体*peer-address*发送Update消息，下一跳地址为*next-hop*

【举例】

\# 打开对等体1.1.1.1的BGP VPNv4的Update报文调试信息开关。从对等体1.1.1.1接收、向对等体1.1.1.1发送BGP VPNv4的Update报文时打印相关调试信息。

\<Sysname\> debugging bgp update 1.1.1.1 vpnv4

\*Mar 25 16:49:43:054 2011 Sysname BGP/7/DEBUG: -MDC=1;

BGP_L3VPN.: Recv UPDATE from peer 3.3.3.3 with following destinations:

         Update message length : 98

         Origin       : Incomplete

         AS path      : 20

         Next hop     : 3.3.3.3

         Local pref   : 100

         MED          : 0

         Ext-Community: \<RT: 1:2\>

         8.8.8.8/32 (RD 1：2, Label 1000120)

*// 从对等体1.1.1.1接收到BGP VPNv4的Update消息，消息长度为98字节，路由信息通过IGP、EGP之外的其他方式学习，AS路径为20，下一跳为3.3.3.3，本地优先级为100，MED值为0，Route Target为1:2，路由前缀为8.8.8.8/32，RD为1:2，标签值为1000120。*

\*Mar 25 16:49:43:065 2011 Sysname BGP/7/DEBUG: -MDC=1;

         BGP_L3VPN.: Send UPDATE to peer 3.3.3.3 for following destinations:

         Origin       : Incomplete

         AS path      : 20

         Next hop     : 3.3.3.1

         Local pref   : 100

         MED          : 0

         Ext-Community: \<RT: 1:2\>

         8.8.8.8/32 (RD 1：2, Label 1000120)

*// 向对等体3.3.3.3发送BGP VPNv4的Update消息，路由信息通过IGP、EGP之外的其他方式学习，AS路径为20，下一跳为3.3.3.1，本地优先级为100，MED值为0，Route Target为1:2，路由前缀为8.8.8.8/32，RD为1:2，标签值为1000120。*

\*Mar 25 16:49:44:012 2011Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: Send UPDATE MSG to peer 3.3.3.3(IPv4-VPN) NextHop: 3.3.3.1.

*// 向BGP对等体3.3.3.3发送路由更新，下一跳地址为3.3.3.1。*

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp update vpn-instance ipv4**

------------------------------------------------------------------------

【命令】

**[debugging bgp update** **vpn-instance** *vpn-instance-name* *ip-address* [ *mask-length*  **ipv4** [ **receive** \| **send** ]]]

**[undo debugging bgp update******vpn-instance ***vpn-instance-name******ip-address* [ *mask-length*  **ipv4** [ **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：对等体的IP地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[vpn-instance-name*]：VPN实例名称，为1～31个字符的字符串，区分大小写。

**[receive**]：表示接收的BGP报文。

**[send**]：表示发送的BGP报文。

【描述】

**[debugging bgp update vpn-instance ipv4**]命令用来打开指定VPN实例的BGP IPv4 Update报文调试信息开关。**undo** **debugging bgp update vpn-instance ipv4**命令用来关闭指定VPN实例的BGP IPv4 Update报文调试信息开关。

缺省情况下，所有VPN实例的BGP IPv4 Update报文调试信息开关均处于关闭状态。

表1-2 debugging bgp update vpn-instance ipv4命令输出信息描述表

字段

描述

BGP.vpn1: Recv UPDATE from peer *ip-address* with following destinations

从对等体*ip-address*接收到Update消息

BGP.: Send UPDATE to peer *ip-address* for following destinations

向对等体*ip-address*发送Update消息

Update message length

Update消息的长度

Origin

路由的Origin属性，即路由信息的来源，取值包括：

·IGP：网络层可达信息来源于AS内部

·EGP：网络层可达信息通过EGP学习

·Incomplete：网络层可达信息通过其他方式学习

AS path

路由的AS Path属性，即路由从本地到目的地址所要经过的所有AS号

Next hop

路由的下一跳属性

Local pref

路由的本地优先级

MED

路由的MED属性

Ext-Community

路由的扩展团体属性

*[prefix*/*mask*]

路由前缀为*prefix*、路由前缀的掩码长度为*mask*

Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*

向地址族*address-family*的对等体*peer-address*发送Update消息，下一跳地址为*next-hop*

【举例】

\# 打开VPN实例vpn1中对等体1.1.1.1的BGP IPv4 Update报文调试信息开关。在VPN实例vpn1内向对等体1.1.1.1发送Update报文时打印相关调试信息。

\<Sysname\> debugging bgp update 1.1.1.1 vpn-instance vpn1 ipv4 send

\*Jul  9 18:10:27:900 2010 Sysname BGP/7/BGPDEBUG:

         BGP.vpn1: Send UPDATE to peer 1.1.1.1 for following destinations:

         Origin       : Incomplete

         AS path      :

         Next hop     : 1.1.1.2

         Local pref   : 100

         MED          : 0

         11.1.1.0/24

*// 在vpn1内向对等体1.1.1.1发送BGP IPv4 Update报文，路由信息通过IGP、EGP之外的其他方式学习，下一跳为1.1.1.2，本地优先级为100，MED值为0，路由前缀为11.1.1.0/24。*

\*Jul  9 18:10:27:950 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: Send UPDATE MSG to peer 1.1.1.1(IPv4-UNC) NextHop: 1.1.1.2.

*// 向vpn1内对等体1.1.1.1发送路由更新，下一跳地址为1.1.1.2。*

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp update-group vpnv4**

------------------------------------------------------------------------

【命令】

**[debugging bgp update-group vpnv4**]

**[undo debugging bgp update-group vpnv4**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp update-group vpnv4**]命令用来打开BGP VPNv4地址族的打包组调试信息开关。**undo debugging bgp update-group vpnv4**命令用来关闭BGP VPNv4地址族的打包组调试信息开关。

缺省情况下，BGP VPNv4地址族的打包组调试信息开关处于关闭状态。

打开调试信息开关会影响系统的性能，因此，请不要轻易打开调试信息开关，调试完毕后，请及时关闭调试信息开关。

表1-3 debugging bgp update-group vpnv4命令输出信息描述表

字段

描述

Send UPDATE to update-group *group-id*

向BGP打包组*group-id*发送路由更新

Send UPDATE(Withdraw) to update-group *group-id*

向BGP打包组*group-id*发送路由撤销

*[destination-address*/*mask-length*]

发布的路由前缀的目的地址和掩码

Update message length

Update消息长度

Origin

BGP的Origin属性

AS path

BGP的AS Path属性

Next hop

BGP的Next Hop属性

Local pref

BGP的Local Pref属性

MED

BGP的MED属性

Community

BGP的团体属性

Ext-Community

BGP的扩展团体属性

update-group *group-id* *address-family* created

创建地址族*address-family*的打包组*group-id*

update-group *group-id* *address-family* deleted

删除地址族*address-family*的打包组*group-id*

【举例】

\# 打开BGP VPNv4打包组调试信息开关，发布BGP VPNv4路由时，设备上将打印如下信息。

\<Sysname\> debugging bgp update-group vpnv4

\*Apr 16 21:06:16:48 2012 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.L3VPN: Send UPDATE to update-group 0 for following destinations:

         Origin       : Incomplete

         AS path      : 100

         Next hop     : 192.168.109.88

         Ext-Community: \<RT: 1:2\>

         8.8.8.8/32 (RD 1:2, Label 1000120)

*// 向BGP打包组0发送路由更新，路由的Origin属性为Incomplete，AS path属性为100，下一跳地址为192.168.109.88，路由的扩展团体属性RT为1:2，发布的路由前缀为111.1.1.1/32，RD为1:2，通告的标签为1000120。*

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp label**

------------------------------------------------------------------------

【命令】

**[debugging bgp label **]

**[undo debugging bgp label**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp label**]命令用来打开BGP标签分配调试信息开关。**undo** **debugging bgp label**命令用来关闭BGP标签分配调试信息开关。

缺省情况下，BGP标签分配调试信息开关处于关闭状态。

表1-4 debugging bgp label命令输出信息描述表

字段

描述

SEND LABEL In/Out/Op

标签相关调试信息，包括入标签（In）、出标签（Out）和操作类型（Op）

其中，Op取值包括：

·ALLOC_NEW：生成标签数据

·FREE：释放标签数据

·FREE_STALE：释放STALE标签

·FREE_USED：释放在用标签

·FIND_EXIST_LABEL：查找到对应的标签数据

·FIND_STALE_LABEL：查找到对应的、存在STALE标记的标签数据

·RECV_NO_EXIST_FEC_LABEL：从LSM收到没有记录的标签

·RECV_EXIST_FEC_LABEL：从LSM收到记录在用的标签

·INCREASE_CNT：标签引用计数增加

·DECREASE_CNT：标签引用计数减少

·TRIGGER_ILM：触发ILM表项更新

·FLUSH_LSM：重新向LSM下刷在用标签

Type

类型，取值包括：

·NH：表示为下一跳分配或删除标签

·PF：表示为前缀分配或删除标签

Fec

标签对应的FEC信息

Nid

邻居信息

取值为0时，表示无效的邻居信息；取值为非0值时，表示邻居的地址

Vrf

VPN实例索引，取值为0时表示公网

Flag

标签数据状态标记，目前取值只能为0x01，表示标签数据处于STALE状态

Ref

引用标签的路由数

【举例】

\# 打开BGP的标签分配调试信息开关，收到标签分配信息时打印相关调试信息。

\<Sysname\> debugging bgp label

\*Feb  1 02:27:22:739 2012 Sysname BGP/7/DEBUG: -MDC=1;

 SEND LABEL In/Out/Op         : 1279/4294967295/ALLOC_NEW

 Type/Fec/Nid/Vrf/Flag/Ref    : NH/106.1.1.2(0)/2a000000/1/0x0/1

*[// BGP*]*为下一跳106.1.1.2/0分配入标签1279，出标签值为4294967295，下一跳所在VPN实例索引为1，邻居Nid为2a000000。*

\*Feb  1 02:27:22:739 2012 Sysname BGP/7/DEBUG: -MDC=1;

 SEND LABEL In/Out/Op         : 1279/4294967295/TRIGGER_ILM

 Type/Fec/Nid/Vrf/Flag/Ref    : NH/106.1.1.2(0)/2a000000/1/0x0/1

*// 删除BGP为下一跳106.1.1.2/0分配的入标签1279，出标签值为4294967295，下一跳所在VPN实例索引为1，邻居Nid为2a000000。*

**MPLS L3VPN \-- MPLS L3VPN调试命令 \-- debugging bgp lsp**

------------------------------------------------------------------------

【命令】

**[debugging bgp lsp**]

**[undo debugging bgp lsp**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp lsp**]命令用来打开BGP创建LSP的调试信息开关。**undo** **debugging bgp lsp**命令用来关闭BGP创建LSP的调试信息开关。

缺省情况下，BGP创建LSP的调试信息开关处于关闭状态。

表1-5 debugging bgp lsp命令输出信息描述表

字段

描述

LSP Type

LSP类型，取值包括ILM、NHLFE、LOCAL_NHLFE;

Op

操作类型，取值包括

·ADD：创建表项

·DELETE：删除表项

Type

FEC类型，PREFIX表示前缀类型的表项，NEXTHOP表示下一跳类型的表项，LOCIFNET表示LocalIfnet类型的表项

Fec

Type取值为PREFIX和LOCIFNET时，表示前缀信息；Type取值为NEXTHOP时，表示下一跳信息

Vrf

下一跳所在的VPN实例索引

OutLabel

出标签

InLabel

入标签值

InLabel/Ref/Flag

入标签值/引用计数/下刷标记

OutFlushNum/OutSegNum

出方向下刷个数/出方向个数

LSP Op

下刷LSP表项操作类型：

·FLUSH_LSM：下刷LSM

·EXIST_NHLFE_NOT_FLUSH：存在NHLFE表项，不需要下刷

·NO_LSP_TO_DELETE：不存在需要删除的LSP

·BEFORE_RECV_TUNNEL_CHG：隧道变化前结果

·AFTER_RECV_TUNNEL_CHG：隧道变化后结果

OutSeg Info No.

出方向信息

Nexthop/vrf/OutLabel

出方向相关信息：下一跳信息/下一跳所在的VPN实例索引/出标签

ifIndex/Nid

出接口索引/出方向隧道的NID

【举例】

\# 基本MPLS L3VPN组网环境下，在PE 1上打开BGP创建LSP的调试信息开关。在VPN实例vpn1上引入静态路由时，打印相关调试信息。

\<Sysname\> debugging bgp lsp

\*Jan 31 10:11:29:123 2012 Sysname BGP/7/DEBUG: -MDC=1;

 SEND LSP Type/Op             : ILM/ADD

 Type/Fec/Vrf/OutLabel        : NEXTHOP/106.1.1.2(0)/1/4294967295

 InLabel                      : 1279

*// 为FEC（106.1.1.2/0）分配标签1279，并创建ILM表项*

\*Jan 31 10:11:29:123 2012 Sysname BGP/7/DEBUG: -MDC=1;

 SEND LSP Op                  : FLUSH_LSM

 Type/Fec/Vrf/OutLabel        : NEXTHOP/106.1.1.2(0)/1/4294967295

 InLabel/Ref/Flag             : 1279/0/0x1

 OutFlushNum/OutSegNum        : 0/0

*// 下刷LSM*

\

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN调试命令 \-- debugging bgp update vpnv6**

------------------------------------------------------------------------

【命令】

**[debugging bgp update** *ip-address* [ *mask-length*  **vpnv6** [ **receive** \| **send** ]]]

**[undo debugging bgp update** *ip-address* [ *mask-length*  **vpnv6** [ **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：对等体的IP地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

**[receive**]：表示接收的BGP报文。

**[send**]：表示发送的BGP报文。

【描述】

**[debugging bgp update vpnv6**]命令用来打开BGP VPNv6的Update报文调试信息开关。**undo** **debugging bgp vpnv6**命令用来关闭BGP VPNv6的Update报文调试信息开关。

缺省情况下，BGP VPNv6的Update报文调试信息开关处于关闭状态。

表2-1 debugging bgp update vpnv6命令输出信息描述表

字段

描述

BGP_6VPE.: Recv UPDATE from peer *ip-address* with following destinations

从对等体*ip-address*接收到Update消息

BGP_6VPE.: Send UPDATE to peer *ip-address* for following destinations

向对等体*ip-address*发送Update消息

Update message length

Update消息的长度，单位为字节

Origin

路由的Origin属性，即路由信息的来源，取值包括：

·IGP：网络层可达信息来源于AS内部

·EGP：网络层可达信息通过EGP学习

·Incomplete：网络层可达信息通过其他方式学习

AS path

路由的AS Path属性，即路由从本地到目的地址所要经过的所有AS号

Next hop

路由的下一跳属性

Local pref

路由的本地优先级

MED

路由的MED（Multi-Exit Discriminator，多出口区分）值

Ext-Community

路由的扩展团体属性

*[prefix/prefix-length *(RD *route-distinguisher*, Label *label*)]

路由前缀为*prefix*、路由前缀的前缀长度为*prefix-length*、RD值为*route-distinguisher*、标签值为*label*

Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*

向地址族*address-family*的对等体*peer-address*发送Update消息，下一跳地址为*next-hop*

【举例】

\# 打开对等体3.3.3.9的BGP VPNv6的Update报文调试信息开关。从对等体3.3.3.9接收、向对等体3.3.3.9发送BGP VPNv6的Update报文时打印相关调试信息。

\<Sysname\> debugging bgp update 3.3.3.9 vpnv6

\*May 14 14:00:49:845 2012 Sysname BGP/7/DEBUG: -MDC=1;

         BGP_6VPE.: Recv UPDATE from peer 3.3.3.9 with following destinations:

         Update message length : 112

         Origin       : Incomplete

         AS path      :

         Next hop     : ::FFFF:3.3.3.9

         Local pref   : 100

         MED          : 0

         Ext-Community: \<RT: 111:1\>

         2001:3::/96 (RD 200:1, Label 1279)

*// 从对等体3.3.3.9接收到BGP VPNv6的Update消息，消息长度为112字节，路由信息通过IGP、EGP之外的其他方式学习，下一跳为::FFFF:3.3.3.9，本地优先级为100，MED值为0，Route Target为111:1，路由前缀为2001:3::/96，RD为200:1，标签值为1279。*

\*May 14 14:00:49:860 2012 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: Send UPDATE MSG to peer 3.3.3.9(IPv6-VPN) NextHop: ::FFFF:3.3.3.1.

*// 向BGP对等体3.3.3.9发送VPNv6路由更新，下一跳地址为::FFFF:3.3.3.1。*

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN调试命令 \-- debugging bgp update vpn-instance ipv6**

------------------------------------------------------------------------

【命令】

**[debugging bgp update** **vpn-instance** *vpn-instance-name* *ipv6-address* [ *prefix-length*  **ipv6** [ **receive** \| **send** ]]]

**[undo debugging bgp update******vpn-instance ***vpn-instance-name******ipv6-address* [ *prefix-length*  **ipv6** [ **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：对等体的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。如果指定本参数，则表示指定网段内的动态对等体。

*[vpn-instance-name*]：VPN实例名称，为1～31个字符的字符串，区分大小写。

**[receive**]：表示接收的BGP报文。

**[send**]：表示发送的BGP报文。

【描述】

**[debugging bgp update vpn-instance ipv6**]命令用来打开指定VPN实例的BGP IPv6 Update报文调试信息开关。**undo** **debugging bgp update vpn-instance ipv6**命令用来关闭指定VPN实例的BGP IPv6 Update报文调试信息开关。

缺省情况下，所有VPN实例的BGP IPv6 Update报文调试信息开关均处于关闭状态。

表2-2 debugging bgp update vpn-instance ipv6命令输出信息描述表

字段

描述

BGP.IPV6_vpn1: Recv UPDATE from peer *ipv6-address* with following destinations

从对等体*ipv6-address*接收到Update消息

BGP.: Send UPDATE to peer *ipv6-address* for following destinations

向对等体*ipv6-address*发送Update消息

Update message length

Update消息的长度

Origin

路由的Origin属性，即路由信息的来源，取值包括：

·IGP：网络层可达信息来源于AS内部

·EGP：网络层可达信息通过EGP学习

·Incomplete：网络层可达信息通过其他方式学习

AS path

路由的AS Path属性，即路由从本地到目的地址所要经过的所有AS号

Next hop

路由的下一跳属性

Local pref

路由的本地优先级

MED

路由的MED属性

Ext-Community

路由的扩展团体属性

*[prefix*/*prefix-length*]

路由前缀为*prefix*、路由前缀的前缀长度为*prefix-length*

Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*

向地址族*address-family*的对等体*peer-address*发送Update消息，下一跳地址为*next-hop*

【举例】

\# 打开VPN实例vpn1中对等体19::1的BGP IPv6 Update报文调试信息开关。从VPN实例vpn1内的对等体19::1接收、向其发送Update报文时打印相关调试信息。

\<Sysname\> debugging bgp update vpn-instance vpn1 19::1 ipv6

\*Sep 26 17:55:17:419 2011 H3C BGP/7/DEBUG: -MDC=1;                              

         BGP_IPV6.vpn1: Recv UPDATE from peer 19::1 with following destinations:

         Update message length : 77                                            

         Origin       : Incomplete                                              

         AS path      : 200                                                    

         Next hop     : 19::1                                                  

         MED          : 0                                                       

         19::/64, 

*// 在vpn1内收到对等体19::1发送BGP IPv6 Update报文，路由信息通过IGP、EGP之外的其他方式学习，AS路径为200，下一跳为19::1，MED值为0，路由前缀为19::/64。*

\*Sep 26 17:55:17:520 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: Send UPDATE MSG to peer 19::1(IPv6-UNC) NextHop: 19::2.

*// 向vpn1内对等体19::1发送路由更新，下一跳地址为19::2。*

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN调试命令 \-- debugging bgp update-group vpnv6**

------------------------------------------------------------------------

【命令】

**[debugging bgp update-group vpnv6**]

**[undo debugging bgp update-group vpnv6**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp update-group vpnv6**]命令用来打开BGP VPNv6地址族的打包组调试信息开关。**undo debugging bgp update-group vpnv6**命令用来关闭BGP VPNv6地址族的打包组调试信息开关。

缺省情况下，BGP VPNv6地址族的打包组调试信息开关处于关闭状态。

打开调试信息开关会影响系统的性能，因此，请不要轻易打开调试信息开关，调试完毕后，请及时关闭调试信息开关。

表2-3 debugging bgp update-group vpnv6命令输出信息描述表

字段

描述

Send UPDATE to update-group *group-id*

向BGP打包组*group-id*发送路由更新

Send UPDATE(Withdraw) to update-group *group-id*

向BGP打包组*group-id*发送路由撤销

*[destination-address*/*mask-length*]

发布的路由前缀的目的地址和掩码

Update message length

Update消息长度

Origin

BGP的Origin属性

AS path

BGP的AS Path属性

Next hop

BGP的Next Hop属性

Local pref

BGP的Local Pref属性

MED

BGP的MED属性

Community

BGP的团体属性

Ext-Community

BGP的扩展团体属性

update-group *group-id* *address-family* created

创建地址族*address-family*的打包组*group-id*

update-group *group-id* *address-family* deleted

删除地址族*address-family*的打包组*group-id*

【举例】

\# 打开BGP VPNv6打包组调试信息开关，发布BGP VPNv6路由时，设备上将打印如下信息。

\<Sysname\> debugging bgp update-group vpnv6

\*Apr 16 21:06:16:48 2012 Sysname BGP/7/DEBUG: -MDC=1;

         BGP_6VPE.: Send UPDATE to update-group 0 for following destinations:

         Origin       : Incomplete

         AS path      : 100

         Next hop     : 100::1

         Ext-Community: \<RT: 1:2\>

         2::/64 (RD 1:2, Label 1000120)

*// 向BGP打包组0发送路由更新，路由的Origin属性为Incomplete，AS path属性为100，下一跳地址为100::1，路由的扩展团体属性RT为1:2，发布的路由前缀为2::/64，RD为1:2，通告的标签为1000120。*

**

