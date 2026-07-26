
**VPLS \-- VPLS配置命令 \-- address-family l2vpn**

------------------------------------------------------------------------

**[address-family l2vpn**]命令用来创建BGP L2VPN地址族，并进入BGP L2VPN地址族视图。

**[undo address-family l2vpn**]命令用来删除BGP L2VPN地址族及BGP L2VPN地址族视图下的所有配置。

【命令】

**[address-family l2vpn**]

**[undo address-family l2vpn**]

【缺省情况】

没有创建BGP L2VPN地址族。

【视图】

BGP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在VPLS组网中，要想建立BGP PW，需要在PE设备的BGP L2VPN地址族视图下通过**peer enable**命令使能BGP对等体，以便PE与该对等体交换L2VPN信息。

【举例】

\# 创建BGP L2VPN地址族，并进入BGP L2VPN地址族视图。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn

**VPLS \-- VPLS配置命令 \-- auto-discovery**

------------------------------------------------------------------------

**[auto-discovery**]命令用来指定VSI采用BGP方式自动发现邻居，并进入VSI自动发现视图。

**[undo auto-discovery**]命令用来取消VSI采用BGP方式自动发现邻居。

【命令】

**[auto-discovery bgp**]

**[undo auto-discovery**]

【缺省情况】

VSI不会采用BGP方式自动发现邻居。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bgp**]：指定VSI采用BGP方式自动发现邻居。

【使用指导】

执行本命令进入VSI自动发现视图后，在该视图下可以配置BGP自动发现的相关参数，如本端站点、VPLS ID、Route Target属性等，以便PE设备通过BGP协议自动发现远端PE设备。

通过BGP协议自动发现远端PE设备后，可以采用LDP或BGP信令协议在PE之间建立PW。**signaling-protocol**命令用来指定采用的信令协议。

【举例】

\# 指定名为aaa的VSI采用BGP方式自动发现邻居，并进入VSI自动发现视图。

\<Sysname\> system-view

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto

【相关命令】

·**display l2vpn pw**

·**display l2vpn ****vsi**

**VPLS \-- VPLS配置命令 \-- backup-peer**

------------------------------------------------------------------------

**[backup-peer**]命令用来配置VPLS的备份PW，并进入VSI LDP备份PW视图或VSI静态备份PW视图。如果指定的备份PW已存在，则直接进入VSI LDP备份PW视图或VSI静态备份PW视图。

**[undo** **backup-peer**]命令用来删除VPLS的备份PW。

【命令】

VSI LDP PW视图：

**[backup-peer ***ip-address* [ **pw-id** *pw-id*  [ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* ] \*]]

**[undo** **backup-peer** *ip-address* **pw-id** *pw-id*]

VSI静态PW视图：

**[backup-peer ***ip-address* [ **pw-id** *pw-id*  **in-label** *label-value* **out-label** *label-value* [ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* ] \*]]

**[undo** **backup-peer** *ip-address* **pw-id** *pw-id*]

【缺省情况】

未配置VPLS的备份PW。

【视图】

VSI LDP PW视图/VSI静态PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定备份PW远端PE的LSR ID。

**[pw-id** *pw-id*]：指定备份PW的PW ID。*pw-id*为PW ID，取值范围为1～4294967295。如果不指定本参数，则备份PW的PW ID为**default-pw-id**命令配置的缺省PW ID。

**[in-label**]*label-value*：指定备份PW的入标签。*label-value*为入标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[out-label**]*label-value*：指定备份PW的出标签。*label-value*为出标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[pw-class** *class-name*]：指定备份PW引用的PW模板。*class-name*表示PW模板名，为1～19个字符的字符串，区分大小写。PW模板中可以配置PW的数据封装类型、是否使用控制字等。如果不指定本参数，则PW数据封装类型为VLAN，不支持控制字功能。

**[tunnel-policy*** tunnel-policy-name*]：指定备份PW的隧道选择策略。*tunnel-policy-name*表示隧道策略名，为1～19个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。

【使用指导】

备份PW作为主PW的备份，可以为主PW提供冗余保护。当主PW出现故障时，设备将通过主PW对应的备份PW转发流量。

需要注意的是：

·配置备份PW时指定的远端PE的LSR ID和PW ID，不能与已经存在的VPLSPW、交叉连接PW的LSR ID和PW ID同时相同。

·无需指定备份PW的hub属性和no-split-horizon属性，备份PW的这些属性与主PW相同。

·如果在VSI视图下通过**default-pw-id**命令配置了缺省PW ID，则执行**backup-peer**命令时可以不指定**pw-id** *pw-id*参数，采用缺省的PW ID；否则，执行**backup-peer**命令时必须指定**pw-id** *pw-id*参数。

·如果为静态PW指定的入标签与已经存在的静态LSP/静态CRLSP的入标签相同，则会导致标签冲突，静态PW不可用。即使修改静态LSP/静态CRLSP的入标签，静态PW仍不可用，需要手工删除该静态PW并重新配置。

【举例】

\# 为名为vpn1的VSI配置主备LDP PW：主PW的远端PE地址为4.4.4.4，PW ID为100；备份PW的远端PE地址为5.5.5.5，PW ID为200。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp peer 4.4.4.4 pw-id 100

Sysname-vsi-vpn1-ldp-4.4.4.4-100 backup-peer 5.5.5.5 pw-id 200

Sysname-vsi-vpn1-ldp-4.4.4.4-100-backup

【相关命令】

·**default-pw-id**

·**display l2vpn ldp**

·**display l2vpn pw**

·**peer**

**VPLS \-- VPLS配置命令 \-- bandwidth（VSI LDP PW view/VSI static PW view）**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置PW的期望带宽。

**[undo bandwidth**]用来恢复缺省情况。

【命令】

**[bandwidth ***bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽为10000000kbps。

【视图】

VSI LDP PW视图/VSI静态PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：PW的期望带宽，取值为1～10000000，单位为kbps。

【使用指导】

接口的期望带宽会对CBQ队列带宽有影响。具体介绍请参见"ACL和QoS配置指导"中的"[拥塞管理"。]

【举例】

\# 在静态PW上配置期望带宽为10000kbps。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling static

Sysname-vsi-vpn1-static peer 5.5.5.5 pw-id 200 in-label 100 out-label 200

Sysname-vsi-vpn1-static-5.5.5.5-200 bandwidth 10000

\# 在LDP PW上配置期望带宽为10000kbps。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp peer 4.4.4.4 pw-id 100

Sysname-vsi-vpn1-ldp-4.4.4.4-100 bandwidth 10000

**VPLS \-- VPLS配置命令 \-- bandwidth（VSI view）**

------------------------------------------------------------------------

!(VPLS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[bandwidth**]命令用来配置VSI的最大带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth ***bandwidth*]

**[undo bandwidth**]

【缺省情况】

VSI的最大带宽值为102400kbps。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth*]：VSI的最大带宽，取值为64～4194303，单位为kbps。

【使用指导】

VSI的最大带宽用来限制指定VSI内创建的所有PW上转发的流量。限制的是PW入方向、出方向流量，还是同时限制入方向和出方向流量，以及超出最大带宽后如何处理，与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置名为vpn1的VSI的最大带宽值为10240kbps。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 bandwidth 10240

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- control-word enable**

------------------------------------------------------------------------

**[control-word enable**]命令用来使能控制字功能。

**[undo control-word enable**]命令用来恢复缺省情况。

【命令】

**[control-word enable**]

**[undo control-word enable**]

【缺省情况】

未使能控制字功能。

【视图】

PW模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

控制字字段位于MPLS标签栈和二层数据之间，用来携带额外的二层数据帧的控制信息，如序列号等。控制字具有如下功能：

·避免报文乱序：在多路径转发的情况下，报文有可能产生乱序，此时可以通过控制字的序列号字段对报文进行排序重组。

·指示净载荷长度：如果PW上传送报文的净载荷长度小于64字节，则需要对报文进行填充，以避免报文发送失败。此时，通过控制字的载荷长度字段可以确定原始载荷的长度，以便从填充后的报文中正确获取原始的报文载荷。

![说明](VPLS命令.files/image002.png)

上述功能的支持情况与设备的型号有关，请以设备的实际情况为准。

本命令用来配置本端是否支持携带控制字字段。报文实际是否携带控制字字段，由两端的配置共同决定：如果两端PE上都使能了控制字功能，则报文中携带控制字字段；否则，报文中不携带控制字字段。

【举例】

\# 使能PW模板pw100的控制字功能。

\<Sysname\> system-view

Sysname pw-class pw100

Sysname-pw-pw100 control-word enable

【相关命令】

·**display l2vpn pw-class**

**VPLS \-- VPLS配置命令 \-- default-pw-id**

------------------------------------------------------------------------

**[default-pw-id**]命令用来配置VSI的缺省PW ID。

**[undo default-pw-id**]命令用来删除为VSI配置的缺省PW ID。

【命令】

**[default-pw-id ***default-pw-id*]

**[undo default-pw-id**]

【缺省情况】

未配置VSI的缺省PW ID。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[default-pw-id*]：缺省PW ID，取值范围为1～4294967295。

【使用指导】

通过本命令指定VSI的缺省PW ID后，执行**backup-peer**、**peer**命令时，可以不指定**pw-id** *pw-id*参数，创建的备份PW、PW采用缺省PW ID，从而简化配置。

【举例】

\# 配置名为vpn1的VSI的缺省PW ID为200。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 default-pw-id 200

【相关命令】

·**backup-peer**

·**peer**

**VPLS \-- VPLS配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置VSI的描述信息。

**[undo description**]命令用来删除VSI的描述信息。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

未配置VSI的描述信息。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：VSI的描述信息，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置名为vpn1的VSI的描述信息为"vsi for vpn1"。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 description vsi for vpn1

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- display bgp l2vpn auto-discovery**

------------------------------------------------------------------------

**[display bgp l2vpn auto-discovery**]命令用来显示通过BGP协议自动发现的VPLS PE信息。

【命令】

**[display bgp l2vpn auto-discovery **[[ **peer** *ip-address* { **advertised** \| **received** } [ **statistics** ] \| **route-distinguisher** *route-distinguisher*  **pe-address** *ip-address* [ **advertise-info**  ] \| **statistics** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer** *ip-address*]：显示向指定对等体发布或者从指定对等体收到的BGP协议自动发现VPLS PE信息。*ip-address*表示对等体的地址。

**[advertised**]：显示向指定对等体发布的BGP协议自动发现VPLS PE信息。

**[received**]：显示从指定对等体接收到的BGP协议自动发现VPLS PE信息。

**[statistics**]：显示BGP协议自动发现的VPLS PE的统计信息。

**[route-distinguisher*** route-distinguisher*]：显示通过BGP协议自动发现的指定路由标识符的VPLS PE信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[pe-address ***ip-address*]：显示通过BGP协议自动发现的指定VPLS PE的信息。*ip-address*为自动发现的PE的IP地址。

**[advertise-info**]：显示通过BGP协议自动发现的VPLS PE的通告信息。

【使用指导】

执行本命令时，如果没有指定任何参数，则显示所有通过BGP协议自动发现的VPLS PE的简要信息。

【举例】

\# 显示所有通过BGP协议自动发现的VPLS PE的简要信息。

\<Sysname\> display bgp l2vpn auto-discovery

 BGP local router ID is 192.168.1.140

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of automatically discovered PEs: 3

 Route distinguisher: 2:2

 Total number of automatically discovered PEs: 3

     PE address      Nexthop         VPLS ID

\* \>  1.1.1.9         0.0.0.0         100:100

\* \>i 2.2.2.9         2.2.2.9         100:100

\* \>i 3.3.3.9         3.3.3.9         100:100

表1-1 display bgp l2vpn auto-discovery命令简要显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码：

·\* - valid：合法路由

·\> - best：普通优选路由

·d - damped：震荡抑制路由

·h - history：历史路由

·s - suppressed：聚合抑制路由

·S - Stale：过期路由

·i - internal：内部路由

·e - external：外部路由

Origin

通过BGP协议自动发现的VPLS PE信息的来源，取值包括：

·i -- IGP：表示产生于本AS内

·e -- EGP：表示是通过EGP（Exterior Gateway Protocol，外部网关协议）学到的

·? -- incomplete：表示来源无法确定

Total number of automatically discovered PEs

通过BGP协议自动发现的所有VPLS PE信息的总数

Route distinguisher

路由标识符

Total number of automatically discovered PEs

通过BGP协议自动发现的、路由标识符为指定值的VPLS PE信息数目

PE address

自动发现的远端PE在VPLS实例内的标识

Nexthop

远端PE的地址

VPLS ID

VPLS ID，用来标识PE所属的VPLS实例

\# 显示通过BGP协议自动发现的路由标识符为2:2、地址为2.2.2.9的VPLS PE的详细信息。

\<Sysname\> display bgp l2vpn auto-discovery route-distinguisher 2:2 pe-address 2.2.2.9

 BGP local router ID: 192.168.1.140

 Local AS number: 100

 Route distinguisher: 2:2

 Total number of automatically discovered PEs: 1

 Paths:   1 available, 1 best

 From            : 2.2.2.9 (192.168.1.135)

 Original nexthop: 2.2.2.9

 Ext-Community   : \<RT: 2:2\>, \<VPLS ID: 100:100\>

 AS-path         : (null)

 Origin          : igp

 Attribute value : localpref 100, pref-val 0

 PE address      : 2.2.2.9

 State           : valid, internal, best

表1-2 display bgp l2vpn auto-discovery命令详细显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Local AS number

本地自治系统号

Route distinguisher

路由标识符

Total number of automatically discovered PEs

通过BGP协议自动发现的、路由标识符为指定值的VPLS PE信息总数

Paths

通过BGP协议自动发现的VPLS PE信息的数目：

·available：有效可达信息数目

·best：最佳可达信息数目

From

发布该信息的BGP对等体的IP地址

Original nexthop

原始下一跳地址，如果是从BGP更新消息中获得的VPLS PE信息，则该地址为接收到的消息中的下一跳IP地址

Ext-Community

扩展团体属性值，包括：

·RT：Route Target属性

·VPLS ID：用来标识该PE所属的VPLS实例

AS-path

AS路径属性，记录了此VPLS PE信息经过的所有AS，可以避免环路的出现

Origin

通过BGP协议自动发现的VPLS PE信息的起源代码，取值包括

·igp：表示可达信息来源于AS内部

·egp：表示可达信息通过EGP学习

·incomplete：表示可达信息的来源无法确定

Attribute value

通过BGP协议自动发现的VPLS PE信息的属性值，包括：

·MED：与目的网络关联的MED值

·localpref：本地优先级

·pref-val：首选值

·pre：协议优先级

PE address

自动发现的远端PE在VPLS实例内的标识

State

通过BGP协议自动发现的VPLS PE信息的当前状态，取值包括：

·valid：有效信息

·internal：内部信息

·external：外部信息

·local：本地产生信息

·best：最佳信息

\# 显示通过BGP协议自动发现的VPLS PE的通告信息。

\<Sysname\> display bgp l2vpn auto-discovery route-distinguisher 2:2 pe-address 1.1.1.9 advertise-info

 BGP local router ID: 192.168.1.140

 Local AS number: 100

 Route distinguisher: 2:2

 Total number of automatically discovered PEs: 1

 Paths:   1 best

 VPLS ID         : 100:100

 PE address      : 1.1.1.9

 Advertised to peers (2 in total):

    2.2.2.9

    3.3.3.9

表1-3 display bgp l2vpn auto-discovery advertise-info命令显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Local AS number

本地自治系统号

Route distinguisher

路由标识符

Total number of automatically discovered PEs

通过BGP协议自动发现的、路由标识符为指定值的VPLS PE信息数目

Paths

通过BGP协议自动发现的VPLS PE信息的数目：

·available：有效可达信息数目

·best：最佳可达信息数目

VPLS ID

VPLS ID，用来标识PE所属的VPLS实例

PE address

自动发现的远端PE在VPLS实例内的标识

Advertised to peers (2 in total)

该信息已经向哪些对等体发送，以及对等体的数目

**VPLS \-- VPLS配置命令 \-- display bgp l2vpn signaling**

------------------------------------------------------------------------

**[display bgp l2vpn signaling**]命令用来显示BGP协议的VPLS标签块信息。

【命令】

**[display bgp l2vpn signaling**[ [ **peer** *ip-address* { **advertised** \| **received** } [ **statistics** ] \| **route-distinguisher** *route-distinguisher*  **site-id** *site-id* [ **label-offset** *label-offset* [ **advertise-info**  ] ] \| **statistics** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer** *ip-address*]：显示向指定对等体发布或者从指定对等体收到的BGP协议VPLS标签块信息。*ip-address*表示对等体的IP地址。

**[advertised**]：显示向指定对等体发布的BGP协议VPLS标签块信息。

**[received**]：显示从指定对等体接收到的BGP协议VPLS标签块信息。

**[statistics**]：显示BGP协议VPLS标签块的统计信息。

**[route-distinguisher*** route-distinguisher*]：显示指定路由标识符的BGP协议VPLS标签块信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[site-id*** site-id*]：显示为指定站点分配的BGP协议VPLS标签块信息。*site-id*为站点编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[label-offset ***label-offset*]：显示标签块偏移量为指定值的BGP协议VPLS标签块信息。*label-offset*为标签块偏移量，取值范围为0～65535。

**[advertise-info**]：显示BGP协议VPLS标签块的通告信息。

【使用指导】

执行本命令时，如果没有指定任何参数，则显示所有BGP协议VPLS标签块的简要信息。

【举例】

\# 显示所有BGP协议VPLS标签块的简要信息。

\<Sysname\> display bgp l2vpn signaling

 BGP local router ID is 192.168.1.135

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of label blocks: 2

 Route distinguisher: 2:2

 Total number of label blocks: 2

     Site ID  LB offset  LB range  LB base    Nexthop

\* \>  1        0          10        1034       0.0.0.0

\* \>i 2        0          10        1162       192.3.3.3

表1-4 display bgp l2vpn signaling命令简要显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码：

·\* - valid：合法路由

·\> - best：普通优选路由

·d - damped：震荡抑制路由

·h - history：历史路由

·s - suppressed：聚合抑制路由

·S - Stale：过期路由

·i - internal：内部路由

·e - external：外部路由

Origin

标签块信息的来源，取值包括：

·i -- IGP：表示产生于本AS内

·e -- EGP：表示是通过EGP学到的

·? -- incomplete：表示来源无法确定

Total number of label blocks

所有标签块信息的总数

Route distinguisher

路由标识符

Total number of label blocks

路由标识符为指定值的标签块信息的数目

Site ID

站点编号

LB offset

标签块偏移量

LB range

标签块大小

LB base

标签块的初始标签值

Nexthop

远端PE的地址

\# 显示路由标识符为1:1、为站点2分配的、标签块偏移量为0的BGP协议VPLS标签块的详细信息。

\<Sysname\> display bgp l2vpn signaling route-distinguisher 1:1 site-id 2 label-offset 0

 BGP local router ID: 192.168.1.140

 Local AS number: 100

 Route distinguisher: 1:1

 Total number of label blocks: 1

 Paths:   1 available, 1 best

 From            : 2.2.2.9 (192.168.1.135)

 Original nexthop: 2.2.2.9

 Ext-Community   : \<RT: 1:1\>, \<L2VPN info: MTU 1500, Encap type BGP VPLS\>

 AS-path         : (null)

 Origin          : igp

 Attribute value : localpref 100, pref-val 0

 Site ID         : 2

 LB offset       : 0

 LB base         : 1418

 LB range        : 10

 State           : valid, internal, best

表1-5 display bgp l2vpn signaling命令详细显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Local AS number

本地自治系统号

Route distinguisher

路由标识符

Total number of label blocks

路由标识符为指定值的标签块信息的总数

Paths

标签块信息的数目：

·available：有效可达信息条数

·best：最佳可达信息条数

From

发布该信息的BGP对等体的IP地址

Original nexthop

原始下一跳地址，如果是从BGP更新消息中获得的标签块信息，则该地址为接收到的消息中的下一跳IP地址

Ext-Community

扩展团体属性值，包括：

·RT：Route Target属性

·L2VPN info：L2VPN相关信息，包括MTU值、封装类型（Encap type）

AS-path

AS路径属性，记录了此标签块信息经过的所有AS，可以避免环路的出现

Origin

标签块信息的起源代码，取值包括：

·igp：表示可达信息来源于AS内部

·egp：表示可达信息通过EGP学习

·incomplete：表示可达信息的来源无法确定

Attribute value

标签块信息的属性值，包括：

·MED：与目的网络关联的MED值

·localpref：本地优先级

·pref-val：首选值

·pre：协议优先级

Site ID

站点编号

LB offset

标签块偏移量

LB base

标签块的初始标签值

LB range

标签块大小

State

标签块信息的当前状态，取值包括：

·valid：有效信息

·internal：内部信息

·external：外部信息

·local：本地产生信息

·best：最佳信息

\# 显示指定VPLS标签块的通告信息。

\<Sysname\> display bgp l2vpn signaling route-distinguisher 1:1 site-id 1 label-offset 0 advertise-info

 BGP local router ID: 192.168.1.140

 Local AS number: 100

 Route distinguisher: 1:1

 Total number of label blocks: 1

 Paths:   1 best

 Site ID         : 1

 LB offset       : 0

 LB base         : 1418

 LB range        : 10

 Advertised to peers (2 in total):

    2.2.2.9

    3.3.3.9

表1-6 display bgp l2vpn signaling advertise-info命令显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Local AS number

本地自治系统号

Route distinguisher

路由标识符

Total number of label blocks

路由标识符为指定值的标签块信息总数

Paths

标签块信息的数目：

·available：有效可达信息数目

·best：最佳可达信息数目

Site ID

站点编号

LB offset

标签块偏移量

LB base

标签块的初始标签值

LB range

标签块大小

Advertised to peers (2 in total)

该信息已经向哪些对等体发送，以及对等体的数目

**VPLS \-- VPLS配置命令 \-- display l2vpn auto-discovery**

------------------------------------------------------------------------

**[display l2vpn auto-discovery**]命令用来显示VPLS的自动发现信息。

【命令】

**[display l2vpn auto-discovery ** **peer** *ip-address* ]  **vsi** *vsi-name*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer*** ip-address*]：显示指定远端PE的VPLS自动发现相关信息。*ip-address*为远端PE的IP地址。如果没有指定本参数，则显示自动发现的所有VPLS PE的信息。

**[vsi** *vsi-name*]：显示指定VSI内自动发现的VPLS PE信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果没有指定本参数，则显示所有VSI内自动发现的VPLS PE信息。

【举例】

\# 显示自动发现的所有VPLS PE信息。

\<Sysname\> display l2vpn auto-discovery

Total number of automatically discovered peers: 2

VSI Name: bbb

RD                    PE_address      VPLS ID               Nexthop

2:2                   1.1.1.9         100:100               1.1.1.9

2:2                   3.3.3.9         100:100               3.3.3.9

表1-7 display l2vpn auto-discovery命令显示信息描述表

字段

描述

Total number of automatically discovered peers

自动发现的VPLS PE数目

VSI Name

VSI名称

RD

路由标识符

PE address

远端PE在VPLS实例内的标识

VPLS ID

VPLS实例标识符

Nexthop

远端PE的地址

【相关命令】

·**route-distinguisher**

·**vpls-id**

**VPLS \-- VPLS配置命令 \-- display l2vpn bgp**

------------------------------------------------------------------------

**[display l2vpn bgp**]命令用来显示VPLS的标签块信息。

【命令】

**[display l2vpn bgp**[ [ **local** \| **peer** *ip-address* ]  **vsi** *vsi-name*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[local**]：只显示本地分配的标签块信息。

**[peer*** ip-address*]：显示从指定远端PE接收到的标签块信息。*ip-address*为远端PE的地址。

**[vsi** *vsi-name*]：显示指定VSI内的BGP块信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果没有指定本参数，则显示所有VSI的标签块信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【使用指导】

执行本命令时指定了**peer*** ip-address*参数，如果存在与从远端PE接收到的标签块匹配的本地标签块，即接收到的标签块信息中携带的远端Site ID满足条件：本地标签块LO\<=远端Site ID\<=本地标签块LO+LR-1，则同时显示远端标签块和匹配的本地标签块信息；否则，只显示从远端PE接收到的标签块信息。

执行本命令时，如果没有指定**peer*** ip-address*和**local**参数，则显示从所有远端PE接收到的标签块信息。如果存在与远端标签块匹配的本地标签块，则同时显示本地标签块信息。

【举例】

\# 显示从所有远端PE接收到的标签块的简要信息。

\<Sysname\> display l2vpn bgp

Total number of BGP PWs: 2, 2 up, 0 down

VSI Name: aaa

Rmt Site   Offset  RD                    Nexthop          In/Out Label     State

1          0       1:1                   1.1.1.9          1419/1420        Up

3          0       1:1                   3.3.3.9          1421/1282        Up

表1-8 display l2vpn bgp命令显示信息描述表

字段

描述

Total number of BGP PWs

BGP PW的总数，及处于up和down状态的BGP PW数目

VSI Name

VSI名称

Rmt Site

远端Site标识符

Offset

远端标签块的偏移量

RD

路由标识符

Nexthop

远端PE地址

In/Out Label

PW的入标签和出标签值

State

PW状态，取值包括Up、Down

\# 显示从所有远端PE接收到的标签块的详细信息。

\<Sysname\> display l2vpn bgp verbose

VSI Name: aaa

 Remote Site ID     : 1

 Offset             : 0

 RD                 : 1:1

 PW State           : Up

 Encapsulation      : BGP-VPLS

 MTU                : 1500

 Nexthop            : 1.1.1.9

 Local VC Label     : 1419

 Remote VC Label    : 1420

 Link ID            : 9

 Local Label Block  : 1418/10/0

 Remote Label Block : 1418/10/0

 Export Route Target: 1:1

 Remote Site ID     : 3

 Offset             : 0

 RD                 : 1:1

 PW State           : Up

 Encapsulation      : BGP-VPLS

 MTU                : 1500

 Nexthop            : 3.3.3.9

 Local VC Label     : 1421

 Remote VC Label    : 1282

 Link ID            : 10

 Local Label Block  : 1418/10/0

 Remote Label Block : 1280/10/0

 Export Route Target: 1:1

表1-9 display l2vpn bgp verbose命令显示信息描述表

字段

描述

VSI Name

VSI名称

Remote Site ID

远端Site标识符

Offset

远端标签块的偏移量

RD

路由标识符

PW State

PW状态，取值包括Up、Down

Encapsulation

PW数据封装类型

MTU

PW协商后的最大传输单元，单位为字节

Nexthop

远端PE地址

Local VC Label

PW的入标签

Remote VC Label

PW的出标签

Link ID

PW在VSI内的链路标识符

Local Label Block

本端的标签块信息，包括标签块的初始标签值/标签块大小/标签块的偏移量

Remote Label Block

从远端收到的标签块信息，包括标签块的初始标签值/标签块大小/标签块的偏移量

Export Route Target

从远端收到的标签块对应的Route Target属性

\# 显示所有本地分配的标签块的简要信息。

\<Sysname\> display l2vpn bgp local

VSI Name: aaa

Site   Offset  Range  Label Base    RD

2      0       10     1418          1:1

表1-10 display l2vpn bgp local命令显示信息描述表

字段

描述

VSI Name

VSI名称

Site

本端Site标识符

Offset

为该Site分配的标签块的偏移量

Range

为该Site分配的标签块大小

Label Base

为该Site分配的标签块的初始标签值

RD

标签块对应的路由标识符，如果没有配置，则显示为"-"

\# 显示所有本地分配的标签块的详细信息。

\<Sysname\> display l2vpn bgp local verbose

VSI Name: aaa

 Site ID            : 2

 Offset             : 0

 RD                 : 1:1

 Range              : 10

 Label Base         : 1418

 Link ID            : 8,9,10,11,12,13,14,15,16

表1-11 display l2vpn bgp local verbose命令显示信息描述表

字段

描述

VSI Name

VSI名称

Site ID

本端Site标识符

Offset

为该Site分配的标签块的偏移量

RD

标签块对应的路由标识符，如果没有配置，则显示为"-"

Range

为该Site分配的标签块大小

Label Base

为该Site分配的标签块的初始标签值

Link ID

标签块对应的Link ID序列值，即基于该标签块建立的PW的Link ID值

【相关命令】

·**display l2vpn pw**

**VPLS \-- VPLS配置命令 \-- display l2vpn ldp**

------------------------------------------------------------------------

**[display l2vpn ldp**]命令用来显示LDP协议通告的PW标签相关信息。

【命令】

**[display l2vpn ldp **[[ **peer** *ip-address* [ **pw-id** *pw-id* \| **vpls-id** *vpls-id* ] \| **vsi** *vsi-name* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer*** ip-address*]：显示指定远端PE通过LDP通告的PW标签相关信息。*ip-address*为远端PE的LSR ID。如果没有指定本参数，则显示所有远端PE通过LDP通告的PW标签相关信息。

**[pw-id ***pw-id*]：显示指定FEC 128方式的PW标签相关信息。*pw-id*为PW的PW ID，取值范围为1～4294967295。本参数和**peer**参数配合使用，如果只指定了**peer*** ip-address*参数，则显示指定远端PE通过LDP通告的所有PW标签相关信息。

**[vpls-id ***vpls-id*]：显示指定FEC 129方式的PW标签相关信息。*vpls-id*表示VPLS ID，即VPLS实例标识符，为3～21个字符的字符串，VPLS ID有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[vsi ***vsi-name*]：显示指定VSI内LDP协议通告的PW标签相关信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果没有指定本参数，则显示所有VSI内LDP协议通告的PW标签相关信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【使用指导】

LDP可以通过如下两种方式通告PW标签与PW的绑定关系：

·执行**peer**命令手工指定远端PE后，LDP通告FEC 128和PW标签的绑定关系。

·采用BGP协议自动发现远端PE后，LDP通告FEC 129和PW标签的绑定关系。

本命令可以用来显示通过上述两种方式通告的PW标签。

执行本命令时，如果指定了**pw-id ***pw-id*参数，则显示指定FEC 128方式的PW标签相关信息；如果指定了**vpls-id ***vpls-id*参数，则显示指定FEC 129方式的PW标签相关信息；如果没有指定**pw-id ***pw-id*和**vpls-id ***vpls-id*参数，则同时显示FEC 128方式和FEC 129方式的PW标签相关信息。

【举例】

\# 显示LDP协议通告的所有PW标签的简要信息。

\<Sysname\> display l2vpn ldp

Total number of LDP PWs: 6, 4 up, 2 down

Peer            PW ID/VPLS ID         In/Out Label    State Owner

192.3.3.3       1001                  775125/775126   Up    vpls1

192.3.3.3       1003                  775117/775122   Up    vpls3

192.3.3.3       1004                  775120/775120   Up    vpls4

192.3.3.3       10009                 unknown/775134  Down  vpls5

192.4.4.4       100                   775116/unknown  Down  vpls6

2.2.2.2         99:99                 775135/775125   Up    vplsauto

表1-12 display l2vpn ldp命令显示信息描述表

字段

描述

Total number of LDP PWs

LDP PW的总数，及处于up和down状态的LDP PW数目

Peer

PW远端PE的IP地址

PW ID/VPLS ID

对于FEC 128方式，为PW标识符PW ID；对于FEC 129方式，为用来标识PE所属VPLS实例的VPLS ID

只有VPLS支持FEC 129方式

In/Out Label

PW的入标签和出标签

State

PW状态，取值包括：

·Up：PW处于up状态

·Down：PW处于down状态

Owner

PW所属VSI的名称

\# 显示LDP协议通告的所有PW标签的详细信息。

\<Sysname\> display l2vpn ldp verbose

Peer: 2.2.2.9          PW ID: 500

  VSI Name: ccc

  PW State: Up

  PW Status Communication: Notification method

  PW ID FEC (Local/Remote):

    PW Type     : VLAN/VLAN

    Group ID    : 0/0

    Label       : 1552/1552

    Control Word: Disabled/Disabled

    VCCV CV Type: -/-

    VCCV CC Type: -/-

    MTU         : 1500/1500

    PW Status   : PW forwarding/PW forwarding

Peer: 2.2.2.9          VPLS ID: 100:100

  VSI Name: bbb

  PW State: Up

  PW Status Communication: Notification method

  PW ID FEC (Local/Remote):

    Local AII   : (1.1.1.9, 2.2.2.9)

    Remote AII  : (2.2.2.9, 1.1.1.9)

    PW Type     : VLAN/VLAN

    Group ID    : 0/0

    Label       : 1553/1553

    Control Word: Disabled/Disabled

    VCCV CV Type: -/-

    VCCV CC Type: -/-

    MTU         : 1500/1500

    PW Status   : PW forwarding/PW forwarding

Peer: 3.3.3.9          VPLS ID: 100:100

  VSI Name: bbb

  PW State: Up

  PW Status Communication: Notification method

  PW ID FEC (Local/Remote):

    Local AII   : (1.1.1.9, 3.3.3.9)

    Remote AII  : (3.3.3.9, 1.1.1.9)

    PW Type     : VLAN/VLAN

    Group ID    : 0/0

    Label       : 1554/1416

    Control Word: Disabled/Disabled

    VCCV CV Type: -/-

    VCCV CC Type: -/-

    MTU         : 1500/1500

    PW Status   : PW forwarding/PW forwarding

表1-13 display l2vpn ldp verbose命令显示信息描述表

字段

描述

Peer

PW远端PE的IP地址

PW ID

PW标识符

VSI Name

PW所属VSI的名称

PW State

PW状态，取值包括Up和Down

PW Status Communication

PW状态通知方式：

·Notification method：通过Notification消息通知PW状态

·Label withdraw method：标签回收方式，即只有PW连接的AC状态为up时才会为该PW分配PW标签，AC状态变为down时回收该PW的PW 标签

PW ID FEC (Local/Remote)

本地向远端PE通告的PW ID FEC相关信息/远端PE通告给本地的PW ID FEC相关信息

PW Type

PW数据封装类型

Group ID

PW的Group标识符

Label

PW标签

Control Word

是否使能控制字功能，取值包括

·Enabled：PW使能了控制字功能

·Disabled：PW未使能控制字功能

VCCV CV Type

支持的VCCV CV（Connectivity Verification，连通性验证）类型，取值包括：

·LSP Ping：采用MPLS ping检测PW的连通性

·BFD：采用BFD检测PW的连通性，BFD报文的封装方式为IP/UDP Encapsulation(with IP/UDP Headers)

·Raw-BFD：采用BFD检测PW的连通性，BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头

VCCV CC Type

支持的VCCV CC（Control Channel，控制通道）类型，取值包括：

·Control-Word：控制字类型

·Router-Alert：MPLS路由器告警标签类型

·TTL：TTL超时类型

VCCV（Virtual Circuit Connectivity Verification，虚电路连通性验证）的详细介绍，请参见"MPLS配置指导"中的"MPLS OAM"

MTU

VSI的最大传输单元

PW Status

PW状态，取值包括：

·PW forwarding：PW可以转发报文

·PW not forwarding：PW不可以转发报文

·AC receive fault：AC接收方向失效

·AC transmit fault：AC发送方向失效

·PW receive fault：PW接收方向失效

·PW transmit fault：PW发送方向失效

VPLS ID

VPLS实例标识符

Local AII

本端向远端PE发送的SAII（Source Attachment Individual Identifier，源转发实例本地标识符）和TAII（Target Attachment Individual Identifier，目的转发实例本地标识符）

Remote AII

从远端接收到的SAII和TAII

**VPLS \-- VPLS配置命令 \-- display l2vpn forwarding**

------------------------------------------------------------------------

**[display l2vpn forwarding**]命令用来显示L2VPN转发信息。

【命令】

集中式设备：

**[display l2vpn forwarding**[ { **ac** \| **pw** } [ **vsi** *vsi-name* ]  **verbose** ]]

分布式设备―独立运行模式/集中式IRF设备：

**[display l2vpn forwarding**[ { **ac** \| **pw** } [ **vsi** *vsi-name* ] ]**slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]

分布式设备－IRF模式：

**[display l2vpn forwarding**[ { **ac** \| **pw** } [ **vsi** *vsi-name* ]  **chassis** *chassis-number* ]**slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ac**]：显示AC的转发信息。

**[pw**]：显示PW的转发信息。

**[vsi*** vsi-name*]：显示指定VSI的转发信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的转发信息。

**[slot*** slot-number*]：显示指定单板上的L2VPN转发信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示主用主控板上的L2VPN转发信息。（分布式设备―独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的L2VPN转发信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，则显示Master设备上的L2VPN转发信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的L2VPN转发信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，则显示Master设备上的L2VPN转发信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定成员设备上指定单板的L2VPN转发信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示Master设备上主用主控板的L2VPN转发信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的L2VPN转发信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，则显示Master设备上主用主控板的L2VPN转发信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的L2VPN转发信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【举例】

\# 显示所有VSI内AC转发的简要信息。

\<Sysname\> display l2vpn forwarding ac

Total number of VSIs: 1

Total number of ACs: 3

AC                               VSI Name                        Link ID

GE1/0/5 srv1                     test                            3

GE1/0/5 srv2                     test                            4

GE1/0/6                          test                            5

表1-14 display l2vpn forwarding ac命令显示信息描述表

字段

描述

Total number of VSIs

VSI的总数，包括没有关联AC的VSI

Total number of ACs

所有VSI或指定VSI下AC的总数

AC

接入电路，取值有如下两种：

·三层接口名称：如GE1/0/6。在三层接口下关联VSI时，AC取值为此方式

·二层接口名称和以太网服务实例：如GE1/0/5 srv1。在以太网服务实例下关联VSI时，AC取值为此方式

VSI Name

AC所属VSI的名称

Link ID

AC在VSI内的链路标识符

\# 显示所有VSI内AC转发的详细信息。

\<Sysname\> display l2vpn forwarding ac verbose

VSI Name: vpls1

  Interface: Vlan10

    Link ID      : 0

    Access Mode  : VLAN

  Interface: GE1/0/3  Service Instance: 1

    Link ID      : 1

    Access Mode  : VLAN

    Encapsulation: s-vid 1 to 2 15 to 16

VSI Name: vpls2

  Interface: Vlan13

    Link ID      : 0

    Access Mode  : VLAN

    AC Attributes: Hub link

  Interface: GE1/0/3  Service Instance: 4

    Link ID      : 1

    Access Mode  : VLAN

    AC Attributes: Hub link

    Encapsulation: untagged

VSI Name: vpls5

  Interface: Vlan14

    Link ID      : 0

    Access Mode  : VLAN

表1-15 display l2vpn forwarding ac verbose命令显示信息描述表

字段

描述

VSI Name

VSI名称

Interface

接入接口

Service Instance

以太网服务实例，AC为二层接口的以太网服务实例时才显示该字段

Link ID

AC在VSI内的链路标识符

Access Mode

AC接入模式，取值包括：

·VLAN：VLAN模式

·Ethernet：Ethernet模式

AC Attributes

AC的属性，取值包括：

·Hub link：VPLS Hub-spoke组网中，AC为hub链路

·Spoke link：VPLS Hub-spoke组网中，AC为Spoke链路

在与此AC关联的VSI具有Hub-spoke属性时，才显示这个字段

Encapsulation

以太网服务实例的报文匹配规则，AC为二层接口的以太网服务实例时才显示该字段

\# 显示所有VSI内PW转发的简要信息。

\<Sysname\> display l2vpn forwarding pw

Total number of VSIs: 1

Total number of PWs: 2, 2 up, 0 blocked, 0 down

VSI Name                        In/Out Label    NID        Link ID    State

aaa                             1272/1275       1034       8          Up

aaa                             1271/1273       1035       9          Up

表1-16 display l2vpn forwarding pw命令显示信息描述表

字段

描述

Total number of VSIs

VSI的总数，包括没有PW的VSI

Total number of PWs

所有VSI或指定VSI下PW总数，以及处于up、blocked、down状态的PW数目

VSI Name

PW所属VSI的名称

In/Out Label

PW的入标签和出标签

NID

承载PW的隧道对应的NHLFE表项索引

·存在等价隧道时，一个PW会对应多个NID

·如果不存在隧道，显示为None

Link ID

PW在VSI内的链路标识符

State

PW的状态，取值包括Up、Down、Blocked和BFD Defect

其中，Blocked为存在主备PW的情况下，当前没有转发流量、起到备份作用的PW的状态；BFD Defect为BFD检测到PW存在缺陷的状态

\# 显示所有VSI内PW转发的详细信息。

\<Sysname\> display l2vpn forwarding pw verbose

VSI Name: aaa

  Link ID: 8

    PW Type         : VLAN                  PW State : Up

    In Label        : 1272                  Out Label: 1275

    MTU             : 1500

    PW Attributes   : Main

    VCCV CC         : Router-Alert

    VCCV BFD        : Fault Detection with BFD

    Tunnel Group ID : 0x960000000

    Tunnel NHLFE IDs: 1034

  Link ID: 9

    PW Type         : VLAN                  PW State : Up

    In Label        : 1271                  Out Label: 1273

    MTU             : 1500

    PW Attributes   : Main

    VCCV CC         : Router-Alert

    VCCV BFD        : Fault Detection with BFD

    Tunnel Group ID : 0xa60000001

    Tunnel NHLFE IDs: 1035

表1-17 display l2vpn forwarding pw verbose命令显示信息描述表

字段

描述

VSI Name

VSI名称

Link ID

PW在VSI内的链路标识符

PW Type

PW数据封装类型

PW State

PW的状态，取值包括Up、Down、Blocked和BFD Defect

其中，Blocked为存在主备PW的情况下，当前没有转发流量、起到备份作用的PW的状态；BFD Defect为BFD检测到PW存在缺陷的状态

In Label

PW的入标签

Out Label

PW的出标签

MTU

PW协商后的最大传输单元

PW Attributes

PW的属性，取值包括

·Main：主PW

·Backup：备份PW

·No-split-horizon：禁止水平分割

·Hub link：VPLS hub-spoke组网中，PW为hub链路

·Spoke link： VPLS hub-spoke组网中，PW为spoke链路

VCCV CC

检测PW的VCCV控制通道类型，取值包括：

·Control-Word：控制字类型

·Router-Alert：MPLS路由器告警标签类型

·TTL：TTL超时类型

VCCV BFD

检测PW的BFD报文的封装方式，取值包括：

·Fault Detection with BFD：BFD报文的封装方式为IP/UDP Encapsulation(with IP/UDP Headers)

·Fault Detection with Raw-BFD：BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头

Tunnel Group ID

承载PW的隧道组ID

Tunnel NHLFE IDs

承载PW的隧道对应的NHLFE表项索引列表

存在等价隧道时，一个PW会对应多个索引值

如果不存在隧道，显示为None

**VPLS \-- VPLS配置命令 \-- display l2vpn mac-address**

------------------------------------------------------------------------

**[display l2vpn mac-address**]命令用来显示VSI的MAC地址表信息。

【命令】

**[display l2vpn mac-address ** **vsi** *vsi-name* ]  **dynamic**   **count**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi** *vsi-name*]：显示指定VSI的MAC地址表信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的MAC地址表信息。

**[dynamic**]：显示动态生成的MAC地址表项。如果不指定本参数，则显示所有类型的MAC地址表项。目前，只支持动态生成的MAC地址表项。

**[count**]：显示MAC地址表项的数目。如果不指定本参数，则显示MAC地址表项的具体信息。

【举例】

\# 显示所有VSI的MAC地址表信息。

\<Sysname\> display l2vpn mac-address

MAC Address      State    VSI Name                         Link ID/Name  Aging

0000-0000-000a   dynamic  vpn1                             1             Aging

0000-0000-0009   dynamic  vpn1                             2             Aging

\-\-- 2 mac address(es) found  \-\--    

\# 显示所有VSI的MAC地址表项总数。

\<Sysname\> display l2vpn mac-address count

2 mac address(es) found

表1-18 display l2vpn mac-address命令显示信息描述表

字段

描述

MAC Address

MAC地址

State

MAC地址的状态，目前取值只包括dynamic，表示MAC地址是动态学习的

VSI Name

VSI名称

Link ID/Name

Link ID表示MAC表项的出链路标识符，即AC或PW在VSI内的链路标识符

Name用于VXLAN类型的VSI，VPLS类型的VSI不支持Name

Name的支持情况与设备型号有关，请以设备的实际情况为准

Aging

MAC地址表项是否老化，取值包括Aging和NotAging

XX mac address(es) found

VSI的MAC地址表项的总数

【相关命令】

·**reset l2vpn mac-address**

**VPLS \-- VPLS配置命令 \-- display l2vpn interface**

------------------------------------------------------------------------

**[display l2vpn interface**]命令用来显示与VSI关联的三层接口的L2VPN信息。

【命令】

**[display l2vpn interface **[ **vsi** *vsi-name*[ \| *interface-type interface-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi ***vsi-name*]：显示与指定VSI关联的三层接口的L2VPN信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。

*[interface-type interface-number*]：显示指定接口的L2VPN信息。*interface-type interface-number*为接口类型和接口编号。

【使用指导】

执行本命令时，如果没有指定任何参数，则显示所有与VSI关联的三层接口的L2VPN信息。

本命令只能显示与VSI关联的三层接口的L2VPN信息。若要显示以太网服务实例的L2VPN信息，则需要执行**display l2vpn service-instance**命令。

【举例】

\# 显示所有与VSI关联的三层接口的L2VPN信息。

\<Sysname\> display l2vpn interface

Total number of interfaces: 4, 3 up, 1 down

Interface                Owner                           Link ID   State    Type

Vlan10                   vpls1                           0         Up       VSI

Vlan11                   vpls2                           0         Up       VSI

GE1/0/1                  vpls1                           1         Up       VSI

GE1/0/2                  vpls1                           2         Down     VSI

表1-19 display l2vpn interface命令显示信息描述表

字段

描述

Total number of interfaces

与VSI关联的三层接口的总数，及处于up和down状态的接口数目

Interface

与VSI关联的三层接口的名称

Owner

VSI名称

Link ID

接口对应AC在VSI内的链路标识符

State

接口的状态，取值包括Up和Down

Type

接口对应的L2VPN类型，取值包括VSI和VPWS

【相关命令】

·**display l2vpn service-instance**

**VPLS \-- VPLS配置命令 \-- display l2vpn pw**

------------------------------------------------------------------------

**[display l2vpn pw**]命令用来显示L2VPN的PW信息。

【命令】

**[display** **l2vpn** **pw** [ **vsi** *vsi-name*  [ **protocol** { **bgp** \| **ldp** \| **static** } ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi** *vsi-name*]：显示指定VSI内L2VPN的PW信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果没有指定本参数，则显示所有VSI内L2VPN的PW信息。

**[protocol**]：显示采用指定信令协议建立的PW的信息。如果没有指定本参数，则显示所有协议产生的PW信息。

**[bgp**]：显示采用BGP作为PW信令协议建立的PW的信息，即BGP PW信息。

**[ldp**]：显示采用LDP作为PW信令协议建立的PW的信息，包括FEC 128和FEC 129两种方式建立的PW，即LDP PW和BGP自动发现LDP信令PW信息。

**[static**]：显示采用静态方式建立的PW的信息，即静态PW信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【使用指导】

开启PW统计功能后，可使用**display l2vpn pw verbose**命令查看PW的报文统计信息。

【举例】

\# 显示L2VPN所有PW的简要信息。

\<Sysname\> display l2vpn pw

Flags: M - main, B - backup, H - hub link, S - spoke link, N - no split horizon

Total number of PWs: 5

5 up, 0 blocked, 0 down, 0 defect, 0 idle, 0 duplicate

VSI Name: aaa

Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State

2.2.2.9         2                 1420/1419       BGP     M     9        Up

3.3.3.9         3                 1421/1281       BGP     M     10       Up

VSI Name: bbb

Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State

2.2.2.9         -                 1553/1553       LDP     M     8        Up

3.3.3.9         -                 1554/1416       LDP     M     9        Up

VSI Name: ccc

Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State

2.2.2.9         500               1552/1552       LDP     M     8        Up

表1-20 display l2vpn pw命令显示信息描述表

字段

描述

Flags

PW属性标记的取值

Total number of PWs

PW的总数，及处于up、blocked、down、defect、idle和duplicate状态的PW数目

VSI Name

VSI名称

Peer

PW远端PE的IP地址

PW ID/Rmt Site

如果是静态PW或FEC 128方式的LDP PW，则为PW标识符PW ID；如果是FEC 129方式的BGP自动发现LDP信令PW，则显示为"-"；如果是BGP PW，则为远端Site标识符Rmt Site

In/Out Label

PW的入标签和出标签

Proto

建立PW使用的信令协议，取值包括LDP、Static和BGP

Flag

PW属性标记，取值包括：

·M：Main，主PW

·B：Backup ，备份PW

·H：Hub link，VPLS Hub-spoke组网中，PW为hub链路

·S：Spoke link，VPLS Hub-spoke组网中，PW为spoke链路

·N：No-split-horizon，取消水平分割

Link ID

PW在VSI内的链路标识符

State

PW状态，取值包括：

·Up：表示该PW可用

·Down：表示该PW不可用

·Blocked：表示存在主备PW的情况下，该PW当前没有转发流量、起到备份作用

·Defect：表示BFD检测到该PW存在缺陷

·Idle：表示该PW的入标签不可用

·Dup：表示该静态PW的入标签与静态LSP或静态CRLSP的入标签相同

\# 显示L2VPN所有PW的详细信息。

\<Sysname\> display l2vpn pw verbose

VSI Name: aaa

  Peer: 2.2.2.9          Remote Site: 2

    Signaling Protocol  : BGP

    Link ID             : 9          PW State : Up

    In Label            : 1420       Out Label: 1419

    MTU                 : 1500

    PW Attributes       : Main

    VCCV CC             : -

    VCCV BFD            : -

    Tunnel Group ID     : 0x800000960000000

    Tunnel NHLFE IDs    : 1038

  Peer: 3.3.3.9          Remote Site: 3

    Signaling Protocol  : BGP

    Link ID             : 10         PW State : Up

    In Label            : 1421       Out Label: 1281

    MTU                 : 1500

    PW Attributes       : Main

    VCCV CC             : -

    VCCV BFD            : -

    Tunnel Group ID     : 0x800000160000001

    Tunnel NHLFE IDs    : 1030

VSI Name: bbb

  Peer: 2.2.2.9          VPLS ID: 100:100

    Signaling Protocol  : LDP

    Link ID             : 8          PW State : Up

    In Label            : 1553       Out Label: 1553

    MTU                 : 1500

    PW Attributes       : Main

    VCCV CC             : -

    VCCV BFD            : -

    Tunnel Group ID     : 0x800000960000000

    Tunnel NHLFE IDs    : 1038

  Peer: 3.3.3.9          VPLS ID: 100:100

    Signaling Protocol  : LDP

    Link ID             : 9          PW State : Up

    In Label            : 1554       Out Label: 1416

    MTU                 : 1500

    PW Attributes       : Main

    VCCV CC             : -

    VCCV BFD            : -

    Tunnel Group ID     : 0x800000160000001

    Tunnel NHLFE IDs    : 1030

    Input statistics    :

      Octets   : 10600

      Packets  : 100

      Errors   : 0

      Discards : 0

    Output statistics   :

      Octets   : 12600

      Packets  : 100

      Errors   : 0

      Discards : 0

VSI Name: ccc

  Peer: 2.2.2.9          PW ID: 500

    Signaling Protocol  : LDP

    Link ID             : 8          PW State : Up

    In Label            : 1552       Out Label: 1552

    MTU                 : 1500

    PW Attributes       : Main

    VCCV CC             : -

    VCCV BFD            : -

    Tunnel Group ID     : 0x800000960000000

    Tunnel NHLFE IDs    : 1038

表1-21 display l2vpn pw verbose命令显示信息描述表

字段

描述

VSI Name

VSI名称

Peer

PW远端PE的IP地址

PW ID

PW标识符

Signaling Protocol

建立PW使用的信令协议，取值包括LDP、Static和BGP

Link ID

PW在VSI内的链路标识符

PW State

PW状态，取值包括：

·Up：表示该PW可用

·Down：表示该PW不可用

·Blocked：表示存在主备PW的情况下，该PW当前没有转发流量、起到备份作用

·Defect：表示BFD检测到该PW存在缺陷

·Idle：表示该PW的入标签不可用

·Duplicate：表示该静态PW的入标签与静态LSP或静态CRLSP的入标签相同

In Label

PW入标签

Out Label

PW出标签

Wait to Restore Time

回切等待时间，单位为秒。如果配置不回切，显示为Infinite

只会在主备PW同时存在的情况下显示，并且只在主PW上显示

Remaining Time

回切等待的剩余时间，单位为秒。回切等待定时器启动时，才会显示该字段

MTU

PW协商后的最大传输单元

PW Attributes

PW的属性，取值包括：

·Main：主PW

·Backup：备份PW

·Hub link：VPLS Hub-spoke组网中，PW为hub链路

·Spoke link：VPLS Hub-spoke组网中，PW为spoke链路

·No-split-horizon：取消水平分割

VCCV CC

检测PW的VCCV控制通道类型，取值包括：

·Control-Word：控制字类型

·Router-Alert：MPLS路由器告警标签类型

·TTL：TTL超时类型

VCCV BFD

检测PW的BFD报文的封装方式，取值包括：

·Fault Detection with BFD：BFD报文的封装方式为IP/UDP Encapsulation(with IP/UDP Headers)

·Fault Detection with Raw-BFD：BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头

Tunnel Group ID

承载PW的隧道组ID

Tunnel NHLFE IDs

承载PW的隧道对应的NHLFE表项索引列表

存在等价隧道时，一个PW会对应多个索引值

如果不存在隧道，显示为None

VPLS ID

VPLS实例标识符

Remote Site

远端Site标识符

Input statistics

入方向的PW转发统计信息，包括入方向接收的字节数（Octets）、接收的报文数（Packets）、接收的错误报文数（Errors）和丢弃的报文数（Discards）

 Output statistics

出方向的PW转发统计信息，包括出方向发送的字节数（Octets）、发送的报文数（Packets）、发送的错误报文数（Errors）和丢弃的报文数（Discards）

【相关命令】

·**statistics enable**

**VPLS \-- VPLS配置命令 \-- display l2vpn pw-class**

------------------------------------------------------------------------

**[display l2vpn pw-class**]命令用来显示PW模板的信息。

【命令】

**[display l2vpn pw-class** [ *class-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[class-name*]：显示指定PW模板的信息。*class-name*表示PW模板的名称，为1～19个字符的字符串，区分大小写。如果不指定本参数，则显示所有PW模板的信息。

【举例】

\# 显示所有PW模板的信息。

\<Sysname\> display l2vpn pw-class

Total number of PW classes: 2

PW Class Name       PW Type              Control Word   VCCV CC        VCCV BFD

pw1                 Ethernet             Enabled        Control-Word   Raw-BFD

pw2                 VLAN                 Disabled       Router-Alert   BFD

表1-22 display l2vpn pw-class命令显示信息描述表

字段

描述

Total number of PW classes

PW模板的总数

PW Class Name

PW模板的名称

PW Type

PW数据封装类型，取值包括Ethernet和VLAN

Control Word

是否使能控制字功能，取值包括Enabled和Disabled

VCCV CC

检测PW的VCCV控制通道类型，取值包括：

·Control-Word：控制字类型

·Router-Alert：MPLS路由器告警标签类型

·TTL：TTL超时类型

VCCV BFD

检测PW的BFD报文的封装方式，取值包括：

·Fault Detection with BFD：BFD报文的封装方式为IP/UDP Encapsulation(with IP/UDP Headers)

·Fault Detection with Raw-BFD：BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头

【相关命令】

·**pw-class**

**VPLS \-- VPLS配置命令 \-- display l2vpn service-instance**

------------------------------------------------------------------------

**[display l2vpn service-instance**]命令用来显示以太网服务实例的信息。

【命令】

**[display l2vpn service-instance ** **interface**]* interface-type interface-number* [ **service-instance** *instance-id*  ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定二层以太网接口或二层聚合接口上的以太网服务实例信息。*interface-type interface-number*为接口类型和接口编号。如果没有指定本参数，则显示所有二层以太网接口和二层聚合接口上的以太网服务实例信息。

**[service-instance*** instance-id*]：显示指定以太网服务实例的信息。*instance-id*为以太网服务实例的ID，取值范围为1～4096。如果指定了**interface*** interface-type interface-number*参数，没有指定本参数，则显示指定二层以太网接口或二层聚合接口上所有以太网服务实例的信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【举例】

\# 显示所有以太网服务实例的简要信息。

\<Sysname\> display l2vpn service-instance

Total number of service-instances: 8, 8 up, 0 down

Total number of ACs: 4, 4 up, 0 down

Interface                SrvID Owner                           LinkID State Type

GE1/0/3                  1     vpls1                           1      Up    VSI

GE1/0/3                  2     vpls2                           1      Up    VSI

GE1/0/3                  3     vpls3                           1      Up    VSI

GE1/0/3                  4     vpls4                           1      Up    VSI

GE1/0/3                  5                                            Up

表1-23 display l2vpn service-instance命令显示信息描述表

字段

描述

Total number of service-instances

以太网服务实例的总数，及处于up和down状态的以太网服务实例数目

Total number of ACs

AC的总数，及处于up和down状态的AC数目

Interface

二层以太网接口或二层聚合接口名称

SrvID

以太网服务实例的ID

Owner

VSI名称，如果以太网服务实例上尚未关联VSI，则本字段显示为空

LinkID

以太网服务实例对应AC在VSI内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

Type

以太网服务实例所属的L2VPN类型，取值包括VSI和VPWS

\# 显示二层以太网接口GigabitEthernet1/0/3上所有以太网服务实例的详细信息。

\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/3 verbose

Interface: GE1/0/3

  Service Instance: 1

    Encapsulation : s-vid 1 to 16

    VSI Name      : vpls1

    Link ID       : 1

    State         : Up

  Service Instance: 2

    Encapsulation : s-vid 1001 to 1016

                    only-tagged

    VSI Name      : vpls2

    Link ID       : 1

    State         : Up

  Service Instance: 3

    Encapsulation : s-vid 2000

                    c-vid 1001 to 1002 1015 to 1016

    VSI Name      : vpls3

    Link ID       : 1

    State         : Up

表1-24 display l2vpn service-instance verbose命令显示信息描述表

字段

描述

Interface

二层以太网接口或二层聚合接口

Service Instance

以太网服务实例ID

Encapsulation

以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则不显示本字段

VSI Name

与以太网服务实例关联的VSI的名称

Link ID

以太网服务实例对应AC在VSI内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

【相关命令】

·**service-instance**

**VPLS \-- VPLS配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

**[display l2vpn vsi**]命令用来显示VSI的信息。

【命令】

**[display** **l2vpn** **vsi** [ **name** *vsi-name*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name*** vsi-name*]：显示指定VSI的信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有VSI的信息。

**[verbose**]：显示VSI的详细信息。如果不指定本参数，则显示VSI的简要信息。

【举例】

\# 显示所有VSI的简要信息。

\<Sysname\> display l2vpn vsi

Total number of VSIs: 2, 1 up, 1 down, 0 admin down

VSI Name                        VSI Index       MTU    State

vpls1                           0               1500   Up

vpls2                           1               1500   Down

表1-25 display l2vpn vsi命令显示信息描述表

字段

描述

Total number of VSIs

VSI的总数，及处于up、down和admin down状态的VSI数目

VSI Name

VSI名称

VSI Index

VSI索引

MTU

VSI上配置的最大传输单元

State

VSI的状态，取值包括：

·Up：up状态

·Down：down状态

·Admin down：通过**shutdown**命令手工关闭的VSI

\# 显示所有VSI的详细信息。

\<Sysname\> display l2vpn vsi verbose

VSI Name: vpls1

  VSI Index               : 0

  VSI Description         : vsi for vpls1

  VSI State               : Up

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : Unlimited

  Drop Unknown            : Disabled

  LDP PWs:

    Peer            PW ID            Link ID    State

    192.3.3.3       1                8          Up

    192.3.3.3       1001             8          Blocked

  BGP PWs:

    Peer            Remote Site      Link ID    State

    192.4.4.4       1                9          Up

  ACs:

    AC                               Link ID    State

    Vlan10                           0          Up

    GE1/0/3 srv1                     1          Up

表1-26 display l2vpn vsi verbose命令显示信息描述表

字段

描述

VSI Name

VSI名称

VSI Index

VSI索引

VSI Description

VSI的描述信息，如果不配置，则此行不显示

VSI State

VSI的状态，取值包括

·Up：up状态

·Down：down状态

·Administratively down：通过**shutdown**命令手工关闭VSI

MTU

VSI上配置的最大传输单元

Bandwidth

VSI的最大带宽值，单位为kbps

Broadcast Restrain

VSI的广播抑制百分比

Multicast Restrain

VSI的组播抑制百分比

Unknown Unicast Restrain

VSI的未知单播抑制百分比

MAC Learning

是否使能了MAC地址学习功能，取值包括：

·Enabled：使能了MAC地址学习功能

·Disabled：未使能MAC地址学习功能

MAC Tabel Limit

VSI内MAC地址表项的最大数目

取值为Unlimited，表示不限制VSI内MAC地址表项的最大数目

Drop Unknown

当VSI内学习到的MAC地址数达到最大值后，是否禁止转发源MAC地址不在MAC地址表里的报文

·Enabled：表示禁止转发

·Disabled：表示允许转发

Hub-Spoke

是否使能了Hub-spoke能力。取值为Enabled，表示使能了Hub-spoke能力；如果未使能Hub-spoke能力，则不显示此字段

LDP PWs

VSI的LDP PW列表

Static PWs

VSI的静态PW列表

BGP PWs

VSI的BGP PW列表

Peer

PW远端PE的IP地址

PW ID

PW标识符

Remote Site

远端Site标识符

Link ID

PW在VSI内的链路标识符

State

PW的状态，取值包括Up、Down、Blocked和Defect

ACs

VSI的AC列表

AC

接入电路，取值有如下两种：

·三层接口名称：如GE1/0/4。在三层接口下关联VSI时，AC取值为此方式

·二层接口名称和以太网服务实例：如GE1/0/3 srv1。在以太网服务实例下关联VSI时，AC取值为此方式

Link ID

AC在VSI内的链路ID

State

AC的状态，取值包括Up和Down

【相关命令】

·**vsi**

**VPLS \-- VPLS配置命令 \-- encapsulation**

------------------------------------------------------------------------

**[encapsulation**]命令用来配置以太网服务实例的报文匹配规则。

**[undo encapsulation**]命令用来删除以太网服务实例的报文匹配规则。

【命令】

**[encapsulation**[ **c-vid** { *vlan-id* \| *vlan-id-list* }]]

**[encapsulation**[ **s-vid** { *vlan-id* \| *vlan-id-list* } [ **only-tagged** ]]]

**[encapsulation**[ **s-vid** *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]]

**[encapsulation**[ { **default** \| **tagged** \| **untagged** }]]

**[undo encapsulation**]

【缺省情况】

未配置任何报文匹配规则。

【视图】

以太网服务实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[c-vid**[ { *vlan-id* \| *vlan-id-list* }]]：匹配内层VLAN标签（Customer VLAN ID）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ to *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[s-vid**[ { *vlan-id* \| *vlan-id-list* }]]：匹配外层VLAN标签（Service VLAN ID）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[only-tagged**]：表示只匹配携带VLAN标签的报文。当匹配的VLAN为缺省VLAN时，如果未指定本关键字，则会同时匹配所携带VLAN标签为缺省VLAN的报文和未携带VLAN标签的报文；如果指定了本参数，则只匹配所携带VLAN标签为缺省VLAN的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[s-vid**[ *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]]：匹配指定外层VLAN标签和内层VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·*vlan-id*表示VLAN的编号，取值范围为1～4094。

·*vlan-id-list*为VLAN列表，表示一个或多个VLAN的编号。表示方式为*vlan-id-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-8\>]。其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-8\>表示前面的参数最多可以输入8次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

·**al****l**表示所有VLAN。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[default**]：表示缺省的报文匹配规则。

**[tagged**]：表示匹配携带VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

**[untagged**]：表示匹配未携带VLAN标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。

【使用指导】

当同一个接口下配置的不同以太网服务实例的报文匹配规则出现重叠时，如何匹配报文与设备的型号有关，请以设备的实际情况为准。

同一个以太网接口下可以创建多个服务实例，但是最多只能有一个服务实例采用缺省的报文匹配规则（**encapsulation default**）。如果接口下同时存在一个采用缺省报文匹配规则的服务实例和多个采用其他报文匹配规则的服务实例，则没有与任何其他报文匹配规则匹配的报文将匹配缺省报文匹配规则；如果接口下只存在一个采用缺省报文匹配规则的服务实例，则该接口上的所有报文都匹配缺省报文匹配规则。

需要注意的是：

·在同一个以太网服务实例视图下，不能重复执行本命令。

·删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例与VSI的关联。

·内层VLAN标签和外层VLAN标签的介绍请参见"二层技术-以太网交换配置指导"中的"QinQ"。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1的以太网服务实例1上配置如下报文匹配规则：匹配外层VLAN标签为111，内层VLAN标签为20、30～40的报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 1

Sysname-GigabitEthernet1/0/1-srv1 encapsulation s-vid 111 c-vid 20 30 to 40

【相关命令】

·**display l2vpn service-instance**

**VPLS \-- VPLS配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

**[l2vpn enable**]命令用来使能L2VPN功能。

**[undo l2vpn enable**]命令用来关闭L2VPN功能。

【命令】

**[l2vpn enable**]

**[undo l2vpn enable**]

【缺省情况】

L2VPN功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有使能L2VPN功能后，才能进行L2VPN的相关配置。

【举例】

\# 使能L2VPN功能。

\<Sysname\> system-view

Sysname l2vpn enable

**VPLS \-- VPLS配置命令 \-- l2vpn switchover**

------------------------------------------------------------------------

!(VPLS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[l2vpn switchover**]命令用来将指定PW的流量手工倒换到它的冗余备份PW上。

【命令】

**[l2vpn switchover peer ***ip-address* **pw-id** *pw-id*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[peer ***ip-address*]：指定PW远端PE的LSR ID。

**[pw-id** *pw-id*]：指定PW的PW ID。*pw-id*为PW的PW ID，取值范围为1～4294967295。

【使用指导】

PW远端PE的LSR ID地址和PW ID唯一标识了一条PW。如果该PW存在对应的可用主PW或备份PW，则执行本命令后，通过该PW转发的流量将倒换到另一条可用的主PW或备份PW上转发；如果不存在对应的可用主PW和备份PW，则不进行流量倒换。

本命令是PW保护倒换的手工倒换命令，用来方便管理员对网络流量进行管理。

【举例】

\# 远端PE地址为3.3.3.3、PW ID为100的PW存在备份PW，将该PW上的流量手工倒换到它的备份PW上转发。

\<Sysname\> l2vpn switchover peer 3.3.3.3 pw-id 100

**VPLS \-- VPLS配置命令 \-- mac-learning enable**

------------------------------------------------------------------------

!(VPLS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-learning enable**]命令用来开启VSI的MAC地址学习功能。

**[undo mac-learning** **enable**]命令用来关闭VSI的MAC地址学习功能。

【命令】

**[mac-learning enable**]

**[undo mac-learning enable**]

【缺省情况】

VSI的MAC地址学习功能处于开启状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果关闭了VSI的MAC地址学习功能，则设备接收到该VSI内的报文后不会学习该报文的源MAC地址。

【举例】

\# 关闭名为vpn1的VSI的MAC地址学习功能。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 undo mac-learning enable

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- mac-learing rate**

------------------------------------------------------------------------

![说明](VPLS命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-learning rate**]命令用来配置当前VSI学习单个MAC地址的时间间隔。

**[undo mac-learning rate**]命令用来恢复缺省情况。

【命令】

**[mac-learning** **rate** *interva[l*]]

**[undo****mac-learning** **rate**]

【缺省情况】

学习单个MAC地址的时间间隔为0，即不限制MAC地址的学习速率。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定当前VSI学习单个MAC地址的时间间隔，取值范围为0～1000，单位为毫秒。

【使用指导】

通过配置学习单个MAC地址的时间间隔，可对特定VSI的MAC地址学习速率进行限制，以防止在短时间内学习过多的MAC地址表项，占用过多的MAC地址表项资源。

【举例】

\# 配置名为vpn1的VSI学习单个MAC地址的时间间隔为1000毫秒。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 mac-learning rate 1000

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- mac-table limit**

------------------------------------------------------------------------

!(VPLS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[mac-table limit**]命令用来配置允许VSI学习到的最大MAC地址数。

**[undo mac-table limit**]命令用来恢复缺省情况。

【命令】

**[mac-table** **limit** *mac-limit*]

**[undo mac-table** **limit**]

【缺省情况】

不对VSI学习到的最大MAC地址数进行限制。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-limit*]：允许VSI学习到的最大MAC地址数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

通常情况下，设备上能够保存的最大MAC地址表项数目具有一定的限制。本命令可以控制单个VSI的最大MAC地址数，以避免某个VSI的MAC地址表项过多，占用过多的MAC地址表项资源。

【举例】

\# 配置名为vpn1的VSI允许学习到的最大MAC地址数为1024。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 mac-table limit 1024

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- mac-table limit drop-unknown**

------------------------------------------------------------------------

!(VPLS命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[mac-table limit drop-unknown**]命令用来配置当VSI学习到的MAC地址数达到最大值后，禁止转发源MAC地址不在MAC地址表里的报文，即丢弃该报文。对于源MAC地址在MAC地址表里的报文，进行正常转发。

**[undo mac-table limit drop-unknown**]命令用来恢复缺省情况。

【命令】

**[mac-table limit drop-unknown**]

**[undo mac-table limit drop-unknown**]

【缺省情况】

当VSI学习到的MAC地址数达到最大值后，允许转发源MAC地址不在MAC地址表里的报文，但是不会学习报文的源MAC地址。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置名为vpn1的VSI允许学习到的最大MAC地址数为1024，并配置学习到的MAC地址数达到最大值后，丢弃源MAC地址不在MAC地址表里的报文。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 mac-table limit 1024

Sysname-vsi-vpn1 mac-table limit drop-unknown

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置VSI的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *mtu*]

**[undo mtu**]

【缺省情况】

VSI的MTU值为1500字节。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mtu*]：VSI的MTU值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果采用LDP信令协议建立PW，则要求VPLS实例内所有PE上配置的VSI MTU值必须保持一致。

·VSI的MTU是PW上发送报文的MTU值，该MTU值为包括控制字、PW标签和网络层报文在内的报文的最大长度。

【举例】

\# 配置名为vpn1的VSI的MTU值为1400字节。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 mtu 1400

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- peer**

------------------------------------------------------------------------

**[peer**]命令用来配置VPLS的PW，并进入VSI LDP PW视图或VSI静态PW视图。如果指定的PW已存在，则直接进入VSI LDP PW视图或VSI静态PW视图。

**[undo** **peer**]命令用来删除指定的PW。

【命令】

VSI LDP信令视图：

**[peer** *ip-address* [ **pw-id** *pw-id*  [ **hub** \| **no-split-horizon** \| **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* ] \*]]

**[undo** **peer** *ip-address* **pw-id** *pw-id*]

VSI静态配置视图：

**[peer** *ip-address* [ **pw-id** *pw-id*  [ **in-label** *label-value* **out-label** *label-value* [ **hub** \| **no-split-horizon** \| **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* ] \* ]]]

**[undo** **peer** *ip-address* **pw-id** *pw-id*]

【缺省情况】

未配置VPLS的PW。

【视图】

VSI LDP信令视图/VSI静态配置视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定PW远端PE的LSR ID。

**[pw-id ***pw-id*]：指定PW的PW ID。*pw-id*为PW ID，取值范围为1～4294967295。如果不指定本参数，则PW的PW ID为**default-pw-id**命令配置的缺省PW ID。

**[in-label** *l*]*abel-value*：指定PW的入标签。*label-value*为入标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[out-label** *l*]*abel-value*：指定PW的出标签。*label-value*为出标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[hub**]：指定PW在VSI内为hub链路。当VSI使能了hub-spoke能力后，VSI内的PW缺省为spoke链路。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[no-split-horizon**]：指定通过该PW转发报文时，不采用水平分割方式。缺省情况下，通过PW转发报文时，必须采用水平分割方式。

**[pw-class ***class-name*]：指定PW引用的PW模板。*class-name*表示PW模板名，为1～19个字符的字符串，区分大小写。PW模板中可以配置PW的数据封装类型、是否使用控制字等。如果不指定本参数，则PW数据封装类型为VLAN，不支持控制字功能。

**[tunnel-policy ***tunnel-policy-name*]：指定PW的隧道选择策略。*tunnel-policy-name*表示隧道策略名，为1～19个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。

【使用指导】

创建静态PW时，必须指定**in-label**和**out-label**参数；静态PW已经存在，进入VSI静态PW视图时，无需指定**in-label**和**out-label**参数。

需要注意的是：

·PW ID是一对PE之间PW的标识，本端和远端PE上为同一PW指定的PW ID必须相同。

·在本端PE上，远端PE的LSR ID和PW ID唯一标识一条PW。配置PW时指定的远端PE的LSR ID和PW ID，不能与已经存在的VPLS PW、交叉连接PW的LSR ID和PW ID同时相同。

·如果在VSI视图下通过**default-pw-id**命令配置了缺省PW ID，则执行**peer**命令时可以不指定**pw-id** *pw-id*参数，采用缺省的PW ID；否则，执行**peer**命令时必须指定**pw-id** *pw-id*参数。

·如果为静态PW指定的入标签与已经存在的静态LSP/静态CRLSP的入标签相同，则会导致标签冲突，静态PW不可用。即使修改静态LSP/静态CRLSP的入标签，静态PW仍不可用，需要手工删除该静态PW并重新配置。

【举例】

\# 在VSI LDP信令视图下，配置一条VPLS的LDP PW：远端PE的地址为4.4.4.4，PW ID为200，并指定通过本PW转发报文时不采用水平分割方式。配置PW后，将进入VSI LDP PW视图。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp peer 4.4.4.4 pw-id 200 no-split-horizon

Sysname-vsi-vpn1-ldp-4.4.4.4-200

\# 在VSI静态配置视图下，配置一条VPLS的静态PW：远端PE的地址为5.5.5.5，PW ID为200，入标签为100，出标签为200，并指定通过本PW转发报文时不采用水平分割方式。配置PW后，将进入VSI静态PW视图。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling static

Sysname-vsi-vpn1-static peer 5.5.5.5 pw-id 200 in-label 100 out-label 200 no-split-horizon

Sysname-vsi-vpn1-static-5.5.5.5-200

【相关命令】

·**default-pw-id**

·**display l2vpn ldp**

·**display l2vpn pw**

·**pw-class**

·**tunnel-policy**（MPLS命令参考/隧道策略）

**VPLS \-- VPLS配置命令 \-- peer auto-discovery**

------------------------------------------------------------------------

**[peer auto-discovery**]命令用来使能本地路由器与指定对等体/对等体组交换VPLS PE信息的能力。

**[undo peer auto-discovery**]命令用来禁止本地路由器与指定对等体/对等体组交换VPLS PE信息。

【命令】

**[peer**[ { *group-name* \| *ip-address* [ *mask-length* ] } **auto-discovery**  **non-standard** ]]

**[undo peer**[ { *group-name* \| *ip-address* [ *mask-length* ] } **auto-discovery**]]

【缺省情况】

本地路由器具有与BGP L2VPN对等体/对等体组交换VPLS PE信息的能力，并且采用RFC 6074中定义的MP_REACH_NLRI格式交换VPLS PE信息。

【视图】

BGP L2VPN地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：对等体组的名称，为1～47个字符的字符串，区分大小写。指定的对等体组必须已经创建。

*[ip-address*]：对等体的IP地址。指定的对等体必须已经创建。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

**[non-standard**]：指定采用非标准MP_REACH_NLRI格式交换VPLS PE信息。如果不指定本参数，则采用RFC 6074中定义的MP_REACH_NLRI格式交换VPLS PE信息。请根据对等体支持的MP_REACH_NLRI格式类型，选择是否指定本参数。

【使用指导】

BGP L2VPN对等体之间可以通过BGP协议交换VPLS PE信息，以此来自动发现同一个VPLS实例中的PE设备，无需手工指定每一台PE设备，从而简化网络配置和管理。

在BGP L2VPN地址族视图下执行**peer enable**命令后，本地路由器即具有与指定对等体/对等体组交换VPLS PE信息的能力，并使用RFC 6074定义的MP_REACH_NLRI格式交换VPLS PE信息。如需禁止该能力或该对等体不支持交换VPLS PE信息，则执行**undo peer auto-discovery**命令。

【举例】

\# 在BGP L2VPN地址族视图下，使能本地路由器与对等体3.3.3.9交换VPLS PE信息的能力，并采用RFC 6074定义的MP_REACH_NLRI格式交换VPLS PE信息。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn peer 3.3.3.9 auto-discovery

\# 在BGP L2VPN地址族视图下，使能本地路由器与对等体组test交换VPLS PE信息的能力，并采用非标准的MP_REACH_NLRI格式交换VPLS PE信息。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn peer test auto-discovery non-standard

【相关命令】

·**display bgp l2vpn auto-discovery**

**VPLS \-- VPLS配置命令 \-- peer signaling**

------------------------------------------------------------------------

**[peer signaling**]命令用来使能本地路由器与指定对等体/对等体组交换VPLS标签块信息的能力。

**[undo peer signaling**]命令用来禁止本地路由器与指定对等体/对等体组交换VPLS标签块信息。

【命令】

**[peer**[ { *group-name* \| *ip-address* [ *mask-length* ] } **signaling**]]

**[undo peer**[ { *group-name* \| *ip-address* [ *mask-length* ] } **signaling**]]

【缺省情况】

本地路由器具有与BGP L2VPN对等体/对等体组交换标签块信息的能力。

【视图】

BGP L2VPN地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：对等体组的名称，为1～47个字符的字符串，区分大小写。指定的对等体组必须已经创建。

*[ip-address*]：对等体的IP地址。指定的对等体必须已经创建。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

【使用指导】

建立BGP PW时，PE设备通过MP-BGP协议来交换标签块信息。

在BGP L2VPN地址族视图下执行**peer enable**命令后，本地路由器即具有与指定对等体/对等体组交换标签块信息的能力。如需禁止该能力或该对等体不支持交换标签块信息，则执行**undo peer signaling**命令。

【举例】

\# 在BGP L2VPN地址族视图下，使能本地路由器与对等体3.3.3.9交换VPLS标签块信息的能力。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn peer 3.3.3.9 signaling

【相关命令】

·**display bgp l2vpn ****signaling**

**VPLS \-- VPLS配置命令 \-- policy vpn-target**

------------------------------------------------------------------------

**[policy vpn-target**]命令用来对接收到的BGP L2VPN信息使能VPN-Target过滤功能，即只将Export Route Target属性与本地Import Route Target属性匹配的BGP L2VPN信息加入到BGP L2VPN信息表。

**[undo policy vpn-target**]命令用来取消对BGP L2VPN信息的VPN-Target过滤功能，即接收所有的BGP L2VPN信息。

【命令】

**[policy vpn-target**]

**[undo policy vpn-target**]

【缺省情况】

对接收到的BGP L2VPN信息使能VPN-Target过滤功能。

【视图】

BGP L2VPN地址族视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在跨域VPN-OptionB组网中，ASBR-PE需要保存所有BGP L2VPN信息（即通过BGP协议自动发现的VPLS PE信息和标签块信息），以通告给远端ASBR-PE。这种情况下，ASBR-PE上需执行**undo policy vpn-target**命令接收所有的BGP L2VPN信息，不对它们进行VPN-Target过滤。

跨域VPN-OptionB的详细介绍，请参见"MPLS配置指导"中的"MPLS L3VPN"。

【举例】

\# 在BGP L2VPN地址族视图下，取消对BGP L2VPN信息的VPN-Target过滤功能。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn undo policy vpn-target

**VPLS \-- VPLS配置命令 \-- pw-class (system view)**

------------------------------------------------------------------------

**[pw-class**]命令用来创建PW模板，并进入PW模板视图。

**[undo pw-class**]命令用来删除已经创建的PW模板。

【命令】

**[pw-class ***class-name*]

**[undo pw-class ***class-name*]

【缺省情况】

设备上不存在任何PW模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：PW模板名，为1～19个字符的字符串，区分大小写。

【使用指导】

通过本命令创建PW模板，并进入PW模板视图后，可以在PW模板视图下指定PW的属性，如PW的数据封装类型、是否使用控制字。具有相同属性的PW可以通过引用相同的PW模板，实现对PW属性的配置，从而简化配置。

【举例】

\# 创建PW模板pw100，并进入PW模板视图。

\<Sysname\> system-view

Sysname pw-class pw100

Sysname-pw-pw100

【相关命令】

·**control-word enable**

·**display l2vpn pw-class**

·**pw-type**

**VPLS \-- VPLS配置命令 \-- pw-class (VSI auto-discovery view)**

------------------------------------------------------------------------

**[pw-class**]命令用来指定引用的PW模板。

**[undo** **pw-class**]命令用来取消引用PW模板。

【命令】

**[pw-class ***class-name*]

**[undo pw-class**]

【缺省情况】

不引用任何PW模板。

【视图】

VSI自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：PW模板名，为1～19个字符的字符串，区分大小写。

【使用指导】

在VSI自动发现视图下执行本命令指定引用的PW模板后，该PW模板将应用于该视图下建立的所有PW。

【举例】

\# 在VSI自动发现视图下，指定引用的PW模板为pw100。

\<Sysname\> system-view

Sysname pw-class pw100

Sysname-pw-pw100 quit

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto pw-class pw100

【相关命令】

·**control-word enable**

·**display l2vpn pw-class**

·**pw-type**

**VPLS \-- VPLS配置命令 \-- pw-type**

------------------------------------------------------------------------

**[pw-type**]命令用来配置PW数据封装类型。

**[undo pw-type**]命令用来恢复缺省情况。

【命令】

**[pw-type**[ { **ethernet** \| **vlan** }]]

**[undo pw-type**]

【缺省情况】

PW数据封装类型为VLAN。

【视图】

PW模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ethernet**]：PW数据封装类型为Ethernet。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vlan**]：PW数据封装类型为VLAN。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·Ethernet数据封装类型下，PW上传输的帧不能带服务提供商网络为了区分用户而要求用户压入的P-Tag，该Tag又称为服务定界符。对于CE侧的报文，如果PE从CE收到带有P-Tag的报文，则将其去除后再压入PW标签和公网隧道封装转发；如果从CE收到不带P-Tag的报文，则直接压入PW标签和公网隧道封装后转发。对于PE发送给CE的报文，如果**xconnect vsi**命令配置的接入模式为VLAN，则添加P-Tag后转发给CE；如果配置的接入模式为Ethernet，则不添加P-Tag，直接转发给CE；不允许重写或去除已经存在的任何Tag。

·VLAN数据封装类型下，PW上传输的帧必须带P-Tag。对于CE侧的报文，PE从CE收到带有P-Tag的报文后，如果远端PE不要求Ingress改写P-Tag，则保留P-Tag，如果远端PE要求Ingress改写P-Tag，则将P-Tag改写为远端PE期望的VLAN Tag（Tag可能是值为0的空Tag），再压入PW标签和公网隧道封装后转发；从CE收到不带P-Tag的报文后，如果远端PE不要求Ingress改写P-Tag，则添加值为0的空P-Tag，如果远端PE要求Ingress改写P-Tag，则添加一个远端PE期望的VLAN Tag（Tag可能是值为0的空Tag）后，再压入PW标签和公网隧道封装后转发。对于PE发送给CE的报文，如果**xconnect vsi**命令配置的接入模式为VLAN，转发给CE时重写或保留P-Tag；如果配置的接入模式为Ethernet，则去除P-Tag后转发给CE。

【举例】

\# 配置PW数据封装类型为Ethernet。

\<Sysname\> system-view

Sysname pw-class pw100

Sysname-pw-pw100 pw-type ethernet

【相关命令】

·**display l2vpn pw-class**

**VPLS \-- VPLS配置命令 \-- pwsignaling**

------------------------------------------------------------------------

**[pwsignaling**]命令用来指定VSI使用的PW信令协议，并进入对应的信令视图。

**[undo pwsignaling**]命令用来取消VSI使用指定的PW信令协议。

【命令】

**[pwsignaling**[ { **ldp** \| **static** }]]

**[undo pwsignaling **[{ **ldp** \| **static** }]]

【缺省情况】

未指定VSI使用的PW信令协议。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ldp**]：指定VSI使用LDP信令的FEC 128方式建立PW，并进入VSI LDP信令视图。

**[static**]：指定VSI采用静态配置方式建立PW，并进入VSI静态配置视图。

【举例】

\# 指定名为vpn1的VSI使用LDP信令的FEC 128方式建立PW，并进入VSI LDP信令视图。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp

【相关命令】

·**display l2vpn pw**

**VPLS \-- VPLS配置命令 \-- reset l2vpn mac-address**

------------------------------------------------------------------------

!(VPLS命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[reset l2vpn mac-address**]命令用来清除VSI的MAC地址表项。

【命令】

**[reset l2vpn mac-address ** **vsi**]* vsi-name *

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsi*** vsi-name*]：清除指定VSI的MAC地址表项。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则清除所有VSI的MAC地址表项。

【使用指导】

VSI学习到错误的MAC地址表项，或学习的MAC地址表项数目达到最大值时，可以执行本命令，以便重新学习MAC地址表项。

【举例】

\# 清除名为vpn1的VSI的MAC地址表项。

\<Sysname\> reset l2vpn mac-address vsi vpn1

【相关命令】

·**display l2vpn mac-address vsi **

**VPLS \-- VPLS配置命令 \-- reset l2vpn statistics pw**

------------------------------------------------------------------------

![说明](VPLS命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset l2vpn statistics pw**]命令用来清除指定PW的报文统计信息。

【命令】

**[reset l2vpn statistics pw ** **vsi** ]*vsi-name***** **link** *link-id *

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsi **]*vsi-name*：清除指定VSI实例内的PW报文统计信息。*vsi-name*表示VSI实例的名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则清除所有PW的统计信息。

**[link **]*link-id*：清除指定PW的统计信息。*link-id*为VSI实例内标识PW的链路ID，取值范围为0～65534。如果不指定该参数，则清除指定VSI实例内的所有PW统计信息。

【使用指导】

当PW存在备PW时，会同时清除主PW和备PW的报文统计信息。

【举例】

\# 清除本设备上所有PW报文统计信息。

\<Sysname\> reset l2vpn statistics pw

【相关命令】

·**statistics enable**

**VPLS \-- VPLS配置命令 \-- restrain**

------------------------------------------------------------------------

!(VPLS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[restrain**]命令用来配置VSI的广播、组播或未知单播抑制百分比。

**[undo restrain**]命令用来恢复缺省情况。

【命令】

**[restrain**[ { **broadcast** \| **multicast** \| **unknown-unicast** } *ratio*]]

**[undo restrain **[{ **broadcast** \| **multicast** \| **unknown-unicast** }]]

【缺省情况】

VSI的广播抑制百分比为5%，组播抑制百分比为100%，未知单播抑制百分比为100%。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[broadcast**]：配置VSI的广播抑制百分比。

**[multicast**]：配置VSI的组播抑制百分比。

**[unknown-unicast**]：配置VSI的未知单播抑制百分比。未知单播报文是指在MAC地址表中不存在目的MAC地址对应表项的单播报文。

*[ratio*]：VSI的广播、组播或未知单播的抑制百分比值，取值范围为1～100，单位为百分比。

【使用指导】

本命令与**bandwidth**命令配合使用可以抑制VSI的广播、组播和未知单播流量。当广播、组播或未知单播流量超过最大带宽值×对应的抑制百分比时，将丢弃超过该值的广播、组播或未知单播流量。

抑制的是所有PW入方向、出方向流量，还是同时抑制入方向和出方向流量，与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置名为vpn1的VSI的广播抑制百分比为10%，组播抑制百分比为50%，未知单播抑制百分比为50%。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 restrain broadcast 10

Sysname-vsi-vpn1 restrain multicast 50

Sysname-vsi-vpn1 restrain unknown-unicast 50

【相关命令】

·**bandwidth**

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- revertive**

------------------------------------------------------------------------

**[revertive**]命令用来配置PW冗余保护倒换的回切模式，即主PW恢复后流量是否从备份PW回切到主PW，以及回切模式下的回切等待时间，即主PW恢复后，流量从备份PW回切到主PW的等待时间。

**[undo revertive wtr**]命令用来恢复回切等待时间的缺省情况，即回切等待时间为0。

**[undo revertive never**]命令用来恢复缺省情况。

【命令】

**[revertive **[{ **wtr** *wtr-time* \| **never** }]]

**[undo revertive **[{ **wtr** \| **never** }]]

【缺省情况】

开启回切功能，即主PW恢复后，流量会从备份PW回切到主PW；回切等待时间为0，即主PW恢复后，流量会立即从备份PW回切到主PW。

【视图】

VSI LDP信令视图/VSI静态配置视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[wtr ***wtr-time*]：开启回切功能，并指定回切等待时间（wait-to-restore time），即主PW恢复后，等待*wtr-time*时间后，才将流量从备份PW回切到主PW。*wtr-time*取值范围为0～3600，单位为秒。

**[never**]：指定不回切。

【举例】

\# 为名称为vpn1、采用静态配置方式建立的PW开启回切功能，并指定回切等待时间为120秒。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling static

Sysname-vsi-vpn1-static revertive wtr 120

【相关命令】

·**display l2vpn pw**

**VPLS \-- VPLS配置命令 \-- route-distinguisher**

------------------------------------------------------------------------

**[route-distinguisher**]命令用来为当前VSI的BGP方式配置RD（Route Distinguisher，路由标识符）。

**[undo route-distinguisher**]命令用来删除已配置的RD值。

【命令】

**[route-distinguisher** *route-distinguisher*]

**[undo route-distinguisher**]

【缺省情况】

没有为VSI的BGP方式指定RD。

【视图】

VSI自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[route-distinguisher*]：路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

【使用指导】

在VPLS中，RD用来区分不同VPLS实例内编号相同的站点。PE在通过BGP发布其连接的站点信息时，在Site ID前增加RD，通过RD和Site ID来唯一标识网络中的一个站点。

需要注意的是：

·本命令配置的RD对BGP邻居自动发现和VPLS标签块分发均有效。

·不能为不同VSI的BGP方式配置相同的RD。

·不能通过重复执行**route-distinguisher**命令修改RD值。必须先执行**undo route-distinguisher**命令删除RD值，再通过**route-distinguisher**命令配置新的RD值。

【举例】

\# 为名为aaa的VSI的BGP方式配置RD为22:1。

\<Sysname\> system-view

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto route-distinguisher 22:1

**VPLS \-- VPLS配置命令 \-- rr-filter**

------------------------------------------------------------------------

**[rr-filter**]命令用来创建路由反射器的反射策略：通过配置路由反射器支持的扩展团体属性号，对接收的L2VPN信息进行过滤，只有接收的BGP L2VPN信息包含指定的扩展团体属性号时，路由反射器才会反射该L2VPN信息。

**[undo** **rr-filter**]命令用来恢复缺省情况。

【命令】

**[rr-filter ***extended-community-number*]

**[undo rr-filter**]

【缺省情况】

路由反射器不会对反射的L2VPN信息进行过滤。

【视图】

BGP L2VPN地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[extended-community-number*]：路由反射器支持的扩展团体属性号，取值范围1～199。

【使用指导】

当一个集群中存在多个路由反射器时，通过在不同的路由反射器上配置不同的反射策略，可以实现路由反射器之间的负载分担。

【举例】

\# 在BGP L2VPN地址族视图下，配置路由反射器支持的扩展团体属性号为10，即该路由反射器只反射包含扩展团体属性10的BGP L2VPN信息。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn rr-filter 10

**VPLS \-- VPLS配置命令 \-- service-instance**

------------------------------------------------------------------------

**[service-instance**]命令用来创建以太网服务实例，并进入以太网服务实例视图。

**[undo service-instance**]命令用来删除指定的以太网服务实例。

【命令】

**[service-instance ***instance-id*]

**[undo service-instance ***instance-id*]

【缺省情况】

接口上不存在任何以太网服务实例。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-id*]：以太网服务实例的编号，取值范围为1～4096。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1上创建以太网服务实例1，并进入以太网服务实例1的视图。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 1

Sysname-GigabitEthernet1/0/1-srv1

【相关命令】

·**display l2vpn service-instance**

**VPLS \-- VPLS配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前的VSI。

**[undo shutdown**]命令用来恢复缺省情况。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

VSI处于开启状态。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭VSI后，该VSI将不能提供VPLS服务。

关闭VSI功能通常用于暂时禁用VPLS服务，但还需要再次启用该VPLS服务的场景。关闭VSI后，该VSI所有已存在的配置保持不变。在关闭状态下还可以对VSI进行配置。VSI再次被开启后，基于最新的配置提供VPLS服务。

【举例】

\# 关闭名为vpn1的VSI。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 shutdown

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- signaling-protocol**

------------------------------------------------------------------------

**[signaling-protocol**]命令用来配置通过BGP自动发现远端PE后，与该PE建立PW时采用的信令协议，并进入对应的信令视图。

**[undo signal**ing**-protocol**]命令用来取消已配置的PW信令协议。

【命令】

**[signaling-protocol**[ { **bgp** \| **ldp** }]]

**[undo signaling-protocol**]

【缺省情况】

未指定通过BGP自动发现远端PE后，与该PE建立PW时采用的信令协议。

【视图】

VSI自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bgp**]：指定采用BGP协议建立PW，并进入VSI自动发现BGP信令视图。

**[ldp**]：指定采用LDP协议的FEC 129方式建立PW，并进入VSI自动发现LDP信令视图。

【使用指导】

在同一个VSI自动发现视图下只能指定一种PW信令协议。不允许重复执行本命令指定不同的PW信令协议。

【举例】

\# 在VSI自动发现视图下，配置通过BGP自动发现远端PE后，采用LDP协议的FEC 129方式建立PW，并进入VSI自动发现LDP信令视图。

\<Sysname\> system-view

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto signaling-protocol ldp

Sysname-vsi-aaa-auto-ldp

【相关命令】

·**display l2vpn pw**

·**display l2vpn ****vsi**

**VPLS \-- VPLS配置命令 \-- site**

------------------------------------------------------------------------

**[site**]命令用来创建本地站点。

**[undo site**]命令用来删除指定的本地站点。

【命令】

**[site ***site-id***** **range** *range-value* ]  **default-offset** *default-offset*

**[undo site** *site-id*]

【缺省情况】

设备上不存在任何本地站点。

【视图】

VSI自动发现BGP信令视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[site-id*]：本地站点的ID。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[range ***range-value*]：指定VPLS实例内最多包含的站点数目。*range-value*取值范围为2～*site-id*的最大值＋1，缺省值为10。

**[default-offset ***default-offset*]：指定VPLS实例中站点的起始编号。*default-offset*为起始编号，取值为0或1，缺省值为0。取值为0时，表示VPLS实例内的站点从0开始编号；取值为1时，表示VPLS实例内的站点从1开始编号。

【使用指导】

在同一个VSI下，可以创建ID不同的多个本地站点。

允许在*site-id*和*default-offset*不改变的情况下，通过重复执行**site**命令来增大此站点的range值，但不允许将range改小。要想将range改小，则需要删除这个站点，并重新创建。

不能通过重复执行**site**命令来修改*default-offset*。必须先通过**undo site**命令删除本地站点，再通过**site**命令创建本地站点，并指定新的*default-offset*。

【举例】

\# 在名为aaa的VSI下创建本地站点1，指定VPLS实例内最多包含的站点数目为30，站点的起始编号为0。

\<Sysname\> system-view

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto signaling-protocol bgp

Sysname-vsi-aaa-auto-bgp site 1 range 30 default-offset 0

【相关命令】

·**display l2vpn pw**

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- snmp-agent trap enable l2vpn**

------------------------------------------------------------------------

**[snmp-agent trap enable l2vpn**]命令用来开启L2VPN模块的PW状态变化告警功能。

**[undo snmp-agent trap enable l2vpn**]命令用来关闭L2VPN模块的PW状态变化告警功能。

【命令】

**[snmp-agent trap enable l2vpn ** [ **pw-up-down** \| **pw-delete** ] \*]

**[undo snmp-agent trap enable l2vpn ** [ **pw-up-down** \| **pw-delete** ] \*]

【缺省情况】

L2VPN的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pw-up-down**]：开启PW的up-down状态变化告警。

**[pw-delete**]：开启PW删除告警。

【使用指导】

开启L2VPN模块的告警功能后，当PW状态发生变化时会产生告警信息。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启PW的up-down状态变化告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable l2vpn pw-up-down

【相关命令】

·**display snmp-agent trap-list**（网络管理和监控命令参考/SNMP）

**VPLS \-- VPLS配置命令 \-- statistics enable**

------------------------------------------------------------------------

![说明](VPLS命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics enable**]命令用来开启指定PW的统计功能。

**[undo statistics enable**]命令用来关闭指定PW的统计功能。

【命令】

**[statistics enable**]

**[undo statistics enable**]

【缺省情况】

通过命令行创建的PW未开启PW报文统计，通过MIB创建的PW开启PW报文统计。

【视图】

VSI LDP PW视图/VSI静态PW视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

备PW是否开启统计功能与其主PW保持一致，不需要单独开启或关闭备PW的统计功能。

【举例】

\# 开启指定PW的报文统计功能。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 pwsignaling ldp

Sysname-vsi-vpn1-ldp peer 4.4.4.4 pw-id 100

Sysname-vsi-vpn1-ldp-4.4.4.4-100 statistics enable

【相关命令】

·**reset l2vpn statistics pw**

·**display l2vpn pw**

**VPLS \-- VPLS配置命令 \-- tunnel-policy**

------------------------------------------------------------------------

**[tunnel-policy**]命令用来指定引用的隧道策略。

**[undo tunnel-policy**]命令用来取消引用隧道策略。

【命令】

**[tunnel-policy** *tunnel-policy-name*]

**[undo tunnel-policy**]

【缺省情况】

不引用任何隧道策略。

【视图】

VSI自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tunnel-policy-name*]：隧道策略名称，为1～19个字符的字符串，区分大小写。

【使用指导】

在VSI自动发现视图下执行本命令指定引用的隧道策略后，该视图下建立的所有PW都将引用该隧道策略，即根据指定的隧道策略选择承载PW流量的公网隧道。

如果PW没有引用隧道策略或者引用的隧道策略尚未配置，则该PW根据缺省选择策略来选择隧道。缺省选择策略为按照LSP隧道－\>GRE隧道－\>CR-LSP隧道的优先级顺序选择隧道，负载分担的隧道数目为1。

【举例】

\# 在VSI自动发现视图下，指定引用的隧道策略为policy1。

\<Sysname\> system-view

Sysname tunnel-policy policy1

Sysname-tunnel-policy-policy1 quit

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto tunnel-policy policy1

【相关命令】

·**tunnel-policy**（MPLS命令参考/隧道策略）

**VPLS \-- VPLS配置命令 \-- vpls-id**

------------------------------------------------------------------------

**[vpls-id**]命令用来配置VSI的VPLS ID。

**[undo vpls-id**]命令用来删除VSI的VPLS ID。

【命令】

**[vpls-id** *vpls-id*]

**[undo vpls-id**]

【缺省情况】

没有指定VSI的VPLS ID。

【视图】

VSI自动发现LDP信令视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpls-id*]：VPLS ID，为3～21个字符的字符串。VPLS ID有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

【使用指导】

VPLS ID用来唯一标识一个VPLS实例。只有VPLS ID相同时，才会在PE之间建立PW。

VPLS ID应用于通过BGP自动发现远端PE、并采用LDP信令协议FEC 129方式建立PW的情况。一端PE在通过BGP的Update消息发布本端信息时，将VPLS ID作为扩展团体属性一同发布给BGP对等体（即远端PE）。远端PE接收到该消息后，如果消息中的VPLS ID与本端配置的VPLS ID相同，则采用LDP的FEC 129方式在二者之间建立PW；否则，不会在两个PE之间建立PW。

需要注意的是，不能通过重复执行**vpls-id**命令来修改VPLS ID值。必须先执行**undo vpls-id**命令删除VPLS ID值，再通过**vpls-id**命令配置新的VPLS ID值。

【举例】

\# 为名为aaa的VSI配置VPLS ID为100:1。

\<Sysname\> system-view

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto signaling-protocol ldp

Sysname-vsi-aaa-auto-ldp vpls-id 100:1

【相关命令】

·**display l2vpn pw**

·**display l2vpn ****vsi**

**VPLS \-- VPLS配置命令 \-- vpn-target**

------------------------------------------------------------------------

**[vpn-target**]命令用来为当前VSI的BGP方式配置Route Target属性。

**[undo vpn-target**]命令用来删除指定的Route Target属性。

【命令】

**[vpn-target**[ *vpn-target*&\<1-8\> [ **both** \| **export-extcommunity** \| **import-extcommunity** ]]]

**[undo vpn-target**[ { *vpn-target&\<1-8\>* \| **all** } [ **both** \| **export-extcommunity** \| **import-extcommunity** ]]]

【缺省情况】

没有为VSI的BGP方式指定Route Target属性。

【视图】

VSI自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-target*&\<1-8\>]：Route Target属性值，为3～21个字符的字符串。&\<1-8\>表示前面的参数最多可以输入8次。Route Target有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[both**]：指定配置的Route Target值同时作为Import Target和Export Target。没有指定**both**、**export-extcommunity**和**import-extcommunity**中的任何一个参数时，缺省值为**both**。

**[export-extcommunity**]：指定配置的Route Target值为Export Target。

**[import-extcommunity**]：指定配置的Route Target值为Import Target。

**[all**]：所有Route Target值。

【使用指导】

Route Target用来控制BGP L2VPN信息（即通过BGP协议自动发现的VPLS PE信息和标签块信息）的发布。本地PE在通过BGP的Update消息将L2VPN信息发送给远端PE时，将Update消息中携带的VPN target属性设置为Export target。远端PE接收到BGP L2VPN信息后，将该信息中携带的Export Target属性与本地配置的Import Target进行比较，如果二者中存在相同的值，则接受该信息。

【举例】

\# 为名为aaa的VSI的BGP方式配置Import Target为10:1 100:1 1000:1，Export Target为20:1 200:1 2000:1。

\<Sysname\> system-view

Sysname vsi aaa

Sysname-vsi-aaa auto-discovery bgp

Sysname-vsi-aaa-auto vpn-target 10:1 100:1 1000:1 import-extcommunity

Sysname-vsi-aaa-auto vpn-target 20:1 200:1 2000:1 export-extcommunity

**VPLS \-- VPLS配置命令 \-- vsi**

------------------------------------------------------------------------

**[vsi**]命令用来创建一个VSI，并进入VSI视图。如果指定的VSI已经存在，则直接进入VSI视图。

**[undo** **vsi**]命令用来删除指定的VSI。

【命令】

**[vsi**] *vsi-name* [ **hub-spoke** ]

**[undo**]**vsi** *vsi-name*

【缺省情况】

设备上不存在任何VSI。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

**[hub-spoke**]**：**指定VSI具有hub-spoke能力。如果不指定本参数，则表示VSI不具有hub-spoke能力。

【使用指导】

在同一个VSI下，可以同时使用不同的方式（LDP、BGP、静态方式等）建立多条PW。

Hub-Spoke是VPLS的一种组网应用方式。在这种组网方式下，存在一个中心站点（Hub站点）和多个分支站点（Spoke站点），Spoke站点之间的数据必须通过Hub站点进行交换，而不允许各个Spoke站点之间直接进行数据交换。

在Hub-Spoke组网中，需要指定VSI具有hub-spoke能力。使能hub-spoke能力的VSI内的链路（AC或PW）中只能有一个Hub链路（朝向中心站点方向的链路），其它都是Spoke链路（朝向分支站点方向的链路）。缺省情况下，该VSI内的所有链路均为Spoke链路，需要在执行**xconnect**命令或**peer**命令时通过**hub**关键字手工将AC或PW指定为VSI内的Hub链路。

【举例】

\# 创建名为vpls1的VSI，并进入VSI视图。

\<Sysname\> system-view

Sysname vsi vpls1

Sysname-vsi-vpls1

【相关命令】

·**display l2vpn vsi**

**VPLS \-- VPLS配置命令 \-- xconnect vsi**

------------------------------------------------------------------------

**[xconnect vsi**]命令用来将接口或以太网服务实例与VSI关联，并配置和track项的联动功能。

**[undo** **xconnect vsi**]命令用来取消接口或以太网服务实例与VSI的关联及和track的联动。

【命令】

**[xconnect vsi ***vsi-name *[[ **access-mode** { **ethernet** \| **vlan** } \| **hub** ] \*  **track** *track-entry-number*&\<1-3\> ]]

**[undo xconnect vsi**]

【缺省情况】

接口或以太网服务实例没有与VSI关联，且未启动和track项的联动功能。

【视图】

接口视图/以太网服务实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

**[access-mode**]：指定接入模式。当关联VSI的AC为以太网服务实例时，可以指定本参数，接入模式缺省为VLAN；当AC为三层以太网接口时，接入模式始终为Ethernet，不可以指定本参数；当AC为三层以太网子接口、VLAN接口时，接入模式始终为VLAN，不可以指定本参数。

**[ethernet**]：指定接入模式为Ethernet。

**[vlan**]：指定接入模式为VLAN。

**[hub**]：指定AC在VSI内为hub链路。与使能了hub-spoke能力的VSI关联的AC缺省为VSI内的spoke链路。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[track**]：配置接口或以太网服务实例与指定track项联动。

*[track-entry-number*&\<1-3\>]：Track项的序号，取值范围为1～1024。&\<1-3\>表示可以输入1到3个序号，每个序号之间使用空格分隔。

【使用指导】

在接口视图下执行本命令后，从接口接收到的报文将通过查找关联VSI的MAC地址表进行转发；在某个接口的以太网服务实例视图下执行本命令后，从该接口接收到的、符合以太网服务实例报文匹配规则的报文，将通过查找关联VSI的MAC地址表进行转发。

接入模式是PE对从CE收到的以太网帧携带的外层VLAN Tag的理解方式，以及PE向CE发送以太网帧的方式。接入模式分为两种：

·VLAN接入模式：CE发送给PE的以太网帧头需要带有一个VLAN Tag，该Tag被理解为P-Tag，即服务提供商网络为了区分用户而压入的"服务定界符"。PE发送以太网帧给CE时，也需要携带P-Tag。

·Ethernet接入模式：CE发送给PE的以太网帧头中如果带有VLAN Tag，则该Tag被理解为U-Tag，即用户网络的内部VLAN Tag，对于PE设备没有意义。PE发送以太网帧给CE时，不需要携带P-Tag。

配置接口或以太网服务实例与track联动后，仅当关联的track项中至少有一个状态为positive时，AC的状态才会up，否则，AC的状态为down。

需要注意的是：

·在以太网服务实例下配置该命令前，必须先配置**encapsulation**命令。

·只有使能了VSI的Hub-Spoke能力后，才可以进一步指定链路类型为Hub链路或者Spoke链路，缺省的链路类型为Spoke。

【举例】

\# 接口GigabitEthernet1/0/1下采用以太网服务实例200来匹配外层VLAN Tag为200的报文，将该以太网服务实例与名为vpn1的VSI关联，并指定AC在VSI内为hub链路，以及和track项1、2和3联动。

\<Sysname\> system-view

Sysname vsi vpn1 hub-spoke

Sysname-vsi-vpn1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 200

Sysname-GigabitEthernet1/0/1-srv200 encapsulation s-vid 200

Sysname-GigabitEthernet1/0/1-srv200 xconnect vsi vpn1 hub track 1 2 3

【相关命令】

·**display l2vpn interface**

·**display l2vpn service-instance**

·**encapsulation**

·**vsi**
