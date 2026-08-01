<!-- CMD-INDEX
  address-family ipv6                 | IS-IS视图          | L31
  auto-cost enable                    | IS-IS IPv6单播地址族视图 | L79
  bandwidth-reference                 | IS-IS IPv6单播地址族视图** | L131
  circuit-cost                        | IS-IS IPv6单播地址族视图 | L179
  default-route-advertise             | IS-IS IPv6单播地址族视图 | L241
  display isis redistribute ipv6      | 任意视图             | L309
  display isis route ipv6             | 任意视图             | L415
  display isis spf-tree ipv6          | 任意视图             | L631
  filter-policy export                | IS-IS IPv6单播地址族视图 | L1047
  filter-policy import                | IS-IS IPv6单播地址族视图 | L1133
  import-route                        | IS-IS IPv6单播地址族视图 | L1209
  import-route isisv6 level-1 into level-2 | IS-IS IPv6单播地址族视图 | L1279
  import-route isisv6 level-2 into level-1 | IS-IS IPv6单播地址族视图 | L1335
  import-route limit                  | IS-IS IPv6单播地址族视图 | L1391
  isis ipv6 bfd enable                | 接口视图             | L1435
  isis ipv6 cost                      | 接口视图             | L1489
  isis ipv6 enable                    | 接口视图             | L1573
  isis ipv6 prefix-suppression        | 接口视图             | L1651
  isis ipv6 tag                       | 接口视图             | L1705
  ispf enable                         | IS-IS IPv6单播地址族视图 | L1763
  maximum load-balancing              | IS-IS IPv6单播地址族视图 | L1811
  multi-topology                      | IS-IS IPv6地址族视图  | L1861
  preference                          | IS-IS IPv6单播地址族视图 | L1915
  prefix-priority                     | IS-IS IPv6单播地址族视图 | L1965
  set-overload                        | IS-IS IPv6单播地址族视图 | L2029
  summary                             | IS-IS IPv6单播地址族视图 | L2097
  timer spf                           | IS-IS IPv6单播地址族视图 | L2161
-->

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- address-family ipv6**

------------------------------------------------------------------------

**[address-family ipv6**]命令用来创建并进入IS-IS IPv6地址族视图。

**[undo address-family ipv6**]命令用来删除IS-IS IPv6地址族视图。

【命令】

**[address-family ipv6 ** **unicast** ]

**[undo address-family ipv6 ** **unicast** ]

【缺省情况】

没有创建IS-IS IPv6地址族视图。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[unicast**]：表示单播地址族。缺省为单播地址族。

【使用指导】

配置本命令后，进程的IPv6被使能。

【举例】

\# 在IS-IS视图下，创建并进入IS-IS IPv6地址族视图。

\<Sysname\> system-view

Sysname isis 100

Sysname-isis-100 address-family ipv6

Sysname-isis-100-ipv6

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- auto-cost enable**

------------------------------------------------------------------------

**[auto-cost enable**]命令用来使能自动计算接口链路开销值功能。

**[undo auto-cost enable**]命令用来关闭自动计算接口链路开销值功能。

【命令】

**[auto-cost enable**]

**[undo auto-cost enable**]

【缺省情况】

自动计算接口链路开销值功能处于关闭状态。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能自动计算接口链路开销值功能后，将根据带宽参考值自动计算接口的链路度量值。当开销值的类型为**wide**或**wide-compatible**时，可以根据公式"开销=（参考值÷带宽）×10"计算接口的链路度量值。当开销值类型为其他类型时，具体情况如下：接口带宽≤10Mbps时，值为60；接口带宽≤100Mbps时，值为50；接口带宽≤155Mbps时，值为40；接口带宽≤622Mbps时，值为30；接口带宽≤2500Mbps时，值为20；接口带宽\>2500Mbps时，值为10。

【举例】

\# 使能IS-IS进程1的IPv6自动计算接口链路开销值功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 auto-cost enable

【相关命令】

·**bandwidth-reference**

·**cost-style**

·**isis ****ipv6 cost**

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- bandwidth-reference**

------------------------------------------------------------------------

**[bandwidth-reference**]命令用来配置IPv6IS-IS自动计算链路开销值时依据的带宽参考值。

**[undo** **bandwidth-reference**]命令用来恢复缺省情况。

【命令】

**[bandwidth-reference** *value*]

**[undo bandwidth-reference**]

【缺省情况】

IPv6 IS-IS自动计算链路度量值时依据的带宽参考值为100Mbps。

【视图】

IS-IS IPv6单播地址族视图**

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：带宽参考值，取值范围为1～2147483648，单位为Mbps。

【举例】

\# 配置IS-IS进程1的IPv6带宽参考值为200Mbps。

\<Sysname\> system-view

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 bandwidth-reference 200

【相关命令】

·**auto-cost enable**

·**isis cost**

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- circuit-cost**

------------------------------------------------------------------------

**[circuit-cost**]命令用来全局配置IPv6 IS-IS的链路开销值。

**[undo circuit-cost**]命令用来取消该配置。

【命令】

**[circuit-cost**[ *value* [ **level-1** \| **level-2** ]]]

**[undo circuit-cost**[ [ **level-1** \| **level-2** ]]]

【缺省情况】

没有全局配置IPv6 IS-IS的链路开销值。

【视图】

IS-IS IPv6单播地址族视图

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

\# 全局配置IS-IS进程1下IPv6所有接口在计算Level-1路由时的链路开销值为11。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 circuit-cost 11 level-1

【相关命令】

·**cost-style**

·**isis cost**

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- default-route-advertise**

------------------------------------------------------------------------

**[default-route-advertise**]命令用来配置路由器生成Level-1或Level-2级别的IPv6 IS-IS缺省路由。

**[undo default-route-advertise**]命令用来取消此项功能。

【命令】

**[default-route-advertise**[ [ **avoid-learning** \| [ **level-1** \| **level-1-2** \| **level-2** ] \| **route-policy** *route-policy-name* \| **tag** *tag* ] \*]]

**[undo default-route-advertise**]

【缺省情况】

IPv6 IS-IS不发布Level-1或Level-2级别的缺省路由。

【视图】

IS-IS IPv6单播地址族视图

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

·通过使用路由策略，可以强制IPv6 IS-IS只在路由表中有匹配的路由项时才生成缺省路由。如果在路由策略视图中**apply isis level-1**，则可以在L1 LSP中生成缺省路由；如果在路由策略视图中**apply isis level-2**，则可以在L2 LSP中生成缺省路由；如果在路由策略视图中**apply isis level-1-2**，可以在L1 LSP、L2 LSP中各自生成缺省路由。

·如果在路由策略中指定了Tag值，则本命令中的Tag值不生效。

【举例】

\# 配置IPv6 IS-IS进程1发布Level-2级别缺省路由。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 default-route-advertise

【相关命令】

·**apply isis**

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- display isis redistribute ipv6**

------------------------------------------------------------------------

**[display isis redistribute ipv6**]命令用来显示IPv6 IS-IS引入路由信息。

【命令】

**[display isis redistribute ipv6 **[ *ipv6-address mask-length*  [ **level-1** \| **level-2** ]  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-address mask-length*]：显示指定目的IP地址和掩码长度的引入路由。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的IPv6路由信息。

**[level-1**]：显示Level-1的IS-IS路由信息。

**[level-2**]：显示Level-2的IS-IS路由信息。

【使用指导】

如果不指定级别，将同时显示Level-1和Level-2的路由信息。

【举例】

\# 显示IS-IS的IPv6引入路由信息。

\<Sysname\> display isis redistribute ipv6 1

                         Route information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                        Level-1 IPv6 Redistribute Table

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Type       : direct     Destination: 12:1::/64

IntCost    : 0          Tag        :

State      : Active

                        Level-2 IPv6 Redistribute Table

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Type       : direct     Destination: 12:1::/64

IntCost    : 0          Tag        :

State      : Active

表1-1 display isis redistribute ipv6命令显示信息描述表

字段

描述

Route information for IS-IS(1)

指定IS-IS进程引入路由信息

Level-1 IPv6 Redistribute Table

Level-1的IS-IS IPv6引入路由信息

Level-2 IPv6 Redistribute Table

Level-2的IS-IS IPv6引入路由信息

Type

引入的路由类型，包括直连、ISISv6、静态、OSPFv3、BGP4+、RIPng

Destination

IPv6目的地址

IntCost

内部路由Cost

Tag

引入路由发布时的Tag值

State

引入路由是否为最终生效路由

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- display isis route ipv6**

------------------------------------------------------------------------

**[display isis route ipv6**]命令用来显示IPv6 IS-IS路由信息。

【命令】

**[display isis route ipv6** [ *ipv6-address*  [ [ **level-1** \| **level-2** ] \| **verbose** ] \* \*process-id *]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ipv6-address*]：显示指定目的IPv6地址的路由。

**[level-1**]：显示Level-1的IPv6 IS-IS路由。

**[level-2**]：显示Level-2的IPv6 IS-IS路由。

**[verbose**]：显示IPv6 IS-IS路由的详细信息。

*[process-id*]：IPv6 IS-IS进程号，取值范围为1～65535。

【使用指导】

如果不指定级别，默认为显示Level-1和Level-2路由信息，即Level-1-2。

【举例】

\# 显示IPv6 IS-IS的路由信息。

\<Sysname\> display isis route ipv6

                         Route information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                         Level-1 IPv6 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Destination: 2001:1::                                PrefixLen: 64

 Flag       : R/L/-                                   Cost     : 20

 Next Hop   : FE80::200:5EFF:FE64:8905                Interface: GE1/0/1

 Destination: 2001:2::                                PrefixLen: 64

 Flag       : D/L/-                                   Cost     : 10

 Next Hop   : Direct                                  Interface: GE1/0/1

       Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

                         Level-2 IPv6 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Destination: 2001:1::                                PrefixLen: 64

 Flag       : -/-/-                                   Cost     : 20

 Destination: 2001:2::                                PrefixLen: 64

 Flag       : D/L/-                                   Cost     : 10

       Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

表1-2 display isis route ipv6命令显示信息描述表

字段

描述

Destination

IPv6目的地址前缀

PrefixLen

前缀长度

Flag/Flags

路由信息状态标志位

·D：直连路由

·R：该路由是否已放到路由表中

·L：是否已经通过LSP发布

·U：路由渗透状态标识，标识Level-1路由是否来自Level-2。如果配置为"U"则可避免由Level-2发送到Level-1的LSP又返回给Level-2

Cost

开销值

Next Hop

下一跳

Interface

出接口

\# 显示IPv6 IS-IS的详细路由信息。

\<Sysname\> display isis route ipv6 verbose

                         Route information for IS-IS(1)

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                         Level-1 IPv6 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPV6 Dest  : 2001:1::/64                    Cost : 20            Flag : R/L/-

 Admin Tag  : -                         Src Count : 1

 NextHop    :                           Interface :          ExitIndex :

    FE80::200:5EFF:FE64:8905                GE1/0/1             0x00000003

 Nib ID    : 0x24000002

 IPV6 Dest  : 2001:2::/64                    Cost : 10            Flag : D/L/-

 Admin Tag  : -                         Src Count : 2

 NextHop    :                           Interface :          ExitIndex :

    Direct                                  GE1/0/1             0x00000000

      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

                         Level-2 IPv6 Forwarding Table

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 IPV6 Dest  : 2001:1::/64                    Cost : 20            Flag : -/-/-

 Admin Tag  : -                         Src Count : 1

 IPV6 Dest  : 2001:2::/64                    Cost : 10            Flag : D/L/-

 Admin Tag  : -                         Src Count : 2

      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set

表1-3 display isis route ipv6 verbose命令显示信息描述表

字段

描述

IPV6 Dest

IPv6目的地址和前缀信息

Cost

开销值

Flag/Flags

路由信息状态标志位

·D：直连路由

·R：该路由是否已放到路由表中

·L：是否已经通过LSP发布

·U：路由渗透状态标识，标识Level-1路由是否来自Level-2。如果配置为"U"则可避免由Level-2发送到Level-1的LSP又返回给Level-2

Admin Tag

管理标记

Src Count

发布源个数

Next Hop

下一跳

Interface

出接口

ExitIndex

出接口索引

Nib ID

路由管理分配的ID，即下一跳索引

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- display isis spf-tree ipv6**

------------------------------------------------------------------------

**[display isis spf-tree ipv6**]命令用来显示IS-IS的IPv6拓扑信息。

【命令】

**[display isis spf-tree ipv6**[ [ [ **level-1** \| **level-2** ] \| **verbose** ] \*  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[level-1**]：显示Level-1的IS-IS拓扑信息。如果未指定级别，将同时显示Level-1和Level-2的拓扑信息。

**[level-2**]：显示Level-2的IS-IS拓扑信息。如果未指定级别，将同时显示Level-1和Level-2的拓扑信息。

**[verbose**]：显示IS-IS的详细拓扑信息。如果未指定该参数，显示摘要拓扑信息。

*[process-id*]：IS-IS进程号，取值范围为1～65535，显示指定IS-IS进程的拓扑信息。如果未指定IS-IS进程号，将显示所有IS-IS进程的拓扑信息。

【举例】

\# 显示IS-IS的IPv6拓扑信息。

\<Sysname\> display isis spf-tree ipv6

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

                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

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

                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

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

\# 显示IS-IS Level-1的IPv6详细拓扑信息。

\<Sysname\> display isis spf-tree ipv6 level-1 verbose

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

 SpfNode        : 0000.0000.0032.00

 Distance       : 0

 TE distance    : 0

 NodeFlag       : S/-/-/-/-/-

 RelayNibID     : 0x0

 TE tunnel count: 0

 Nexthop count  : 0

 SpfLink count  : 2

 \--\>0000.0000.0032.01

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type    : Adjacent   Interface: N/A

        Cost    : 10         Nexthop  : N/A

\--\>0000.0000.0064.00

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type    : Adjacent   Interface: Tun1

        Cost    : 10         Nexthop  : FE80::A0A:A40

SpfNode        : 0000.0000.0032.01

 Distance       : 10

 TE distance    : 10

 NodeFlag       : S/-/-/R/-/-

 RelayNibID     : 0x0

 TE tunnel count: 0

 Nexthop count  : 0

 SpfLink count  : 2

 \--\>0000.0000.0064.00

    LinkCost    : 0

    LinkNewCost : 0

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type    : Adjacent   Interface: Vlan2

        Cost    : 10         Nexthop  : FE80::200:12FF:FE34:1

\--\>0000.0000.0032.00

    LinkCost    : 0

    LinkNewCost : 0

    LinkFlag    : -/-/-/P/-/-/-/-/-

    LinkSrcCnt  : 1

        Type    : Adjacent   Interface: N/A

        Cost    : 0           Nexthop  : N/A

SpfNode        : 0000.0000.0064.00

 Distance       : 10

 TE distance    : 10

 NodeFlag       : S/-/-/R/-/-

 RelayNibID     : 0x0

 TE tunnel count: 0

 Nexthop count  : 2

     Neighbor  : 0000.0000.0064.00        Interface  : Vlan2

     NextHop   : FE80::200:12FF:FE34:1

     BkNeighbor: N/A                      BkInterface: N/A

     BkNextHop : N/A

     Neighbor  : 0000.0000.0064.00        Interface  : Tun1

     NextHop   : FE80::A0A:A40

     BkNeighbor: N/A                      BkInterface: N/A

     BkNextHop : N/A

 SpfLink count  : 2

 \--\>0000.0000.0032.00

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/-/P/-/-/-/-/-

    LinkSrcCnt  : 1

        Type    : Remote     Interface: N/A

        Cost    : 10         Nexthop  : N/A

        AdvMtID : 0

\--\>0000.0000.0064.00

    LinkCost    : 10

    LinkNewCost : 10

    LinkFlag    : -/-/C/-/-/-/-/-/-

    LinkSrcCnt  : 1

        Type    : Remote     Interface: Tun1

        Cost    : 10         Nexthop  : FE80::A0A:A40

        AdvMtID : 0

表1-1 display isis spf-tree ipv6命令显示信息描述表

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

TE tunnel count

Destination为该节点的隧道条数

Nexthop count

节点的下一跳个数

NextHop

节点的主用下一跳地址/链路发布源下一跳地址

AdvMtID

从哪个拓扑学到的路由：

·0：标准拓扑ID

·6～4094：其它拓扑ID

Interface

节点的主用下一跳出接口/链路发布源下一跳出接口

BkNextHop

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

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- filter-policy export**

------------------------------------------------------------------------

**[filter-policy export**]命令用来配置IPv6 IS-IS对引入的路由进行过滤。

**[undo filter-policy export**]命令用来取消对引入的路由进行过滤。

【命令】

**[filter-policy**[ { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **export** [ *protocol* [ *process-id* ] ]]]

**[undo filter-policy** **export** [ *protocol* [ *process-id*  ]]]

【缺省情况】

IPv6 IS-IS不对引入的路由进行过滤。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：用来过滤引入路由的基本或高级IPv6 ACL的编号，取值范围为2000～3999。

**[prefix-list*** prefix-list-name*]：用来过滤引入路由的IPv6地址前缀列表名称，*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy*** route-policy-name*]：用来过滤引入路由的路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。

*[protocol*]：路由协议名称，指定过滤从哪种路由协议引入的路由信息。目前可包括：**bgp4+**、**direct**、**isisv6**、**ospfv3**、**ripng**和**static**。如果不指定该参数，将对所有引入的路由进行过滤。

*[process-id*]：路由协议进程号，取值范围为1～65535。当*protocol*为**isisv6**、**ospfv3**、**ripng**时，支持该参数。

【使用指导】

某些情况下，可能要求只发布某些满足条件的路由信息，此时，可以定义**filter-policy**配置所发布路由信息的过滤条件，只有通过了过滤的路由信息才能被发布。

**[filter-policy export**]命令一般和**import-route**命令结合使用，它只对已引入的路由在发布给其他路由器时进行过滤。

·如果没有指定*protocol*参数，将对所有协议引入的路由进行过滤；

·如果指定了*protocol*参数，则只对特定协议引入的路由进行过滤。

需要注意的是，当配置的是高级ACL（3000～3999）或者指定的路由策略中配置的是高级ACL时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]来过滤指定目的地址和前缀的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。

【举例】

\# 配置IPv6 IS-IS使用编号为2006的IPv6基本ACL对引入的路由进行过滤。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 filter-policy 2006 export

\# 使用编号为3000的IPv6高级ACL对引入的路由进行过滤，只允许2001::1/128通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128

Sysname-acl-ipv6-adv-3000 rule 100 deny ipv6

Sysname-acl-ipv6-adv-3000 quit

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 filter-policy 3000 export

【相关命令】

·**filter-policy import**

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- filter-policy import**

------------------------------------------------------------------------

**[filter-policy import**]命令用来配置IPv6 IS-IS对接收的路由进行过滤。

**[undo filter-policy import**]命令用来取消对接收的路由进行过滤。

【命令】

**[filter-policy**[ { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **import**]]

**[undo filter-policy** **import**]

【缺省情况】

IPv6 IS-IS不对接收的路由信息进行过滤。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：用来过滤接收的路由的基本或高级IPv6 ACL的编号，取值范围为2000～3999。

**[prefix-list*** prefix-list-name*]：用来过滤接收的路由的IPv6地址前缀列表名称，*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy*** route-policy-name*]：用来过滤接收的路由的路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

某些情况下，可能要求只接收某些满足条件的路由信息，此时，可以定义**filter-policy**配置接收路由信息的过滤条件，只有通过了过滤的路由信息才能被加入路由表。

需要注意的是，当配置的是高级ACL（3000～3999）或者指定的路由策略中配置的是高级ACL时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]来过滤指定目的地址和前缀的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。

【举例】

\# 使用编号为2003的IPv6基本ACL对接收的路由进行过滤。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 filter-policy 2003 import

\# 使用编号为3000的IPv6高级ACL对接收的路由进行过滤，只允许2001::1/128通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128

Sysname-acl-ipv6-adv-3000 rule 100 deny ipv6

Sysname-acl-ipv6-adv-3000 quit

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 filter-policy 3000 import

【相关命令】

·**filter-policy export**

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route**

------------------------------------------------------------------------

**[import-route**]命令用来配置IPv6 IS-IS引入其他协议的路由信息。

**[undo import-route**]命令用来配置IPv6 IS-IS不引入其它协议的路由信息。

【命令】

**[import-route ***protocol* [ *process-id*   **allow-ibgp**  [ **allow-direct** \| **cost** *cost* \| [ **level-1** \| **level-1-2** \| **level-2** ] \| **route-policy** *route-policy-name* \| **tag** *tag* ] \*]]

**[undo import-route ***protocol *\*[ process-id *]]

【缺省情况】

IPv6 IS-IS不引入其它协议的路由信息。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：要引入的路由协议，可以是**direct**、**static**、**ripng**、**isisv6**、**bgp4+**及**ospfv3**。

*[process-id*]：引入路由的源路由协议号，取值范围1～65535，缺省值为1。只有当*protocol*是**ripng、isisv6**及**ospfv3**时，该参数可选。

**[allow-direct**]：在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入协议路由时不会包含使能了该协议的接口网段路由。当**allow-direct**与**route-policy** *route-policy-name*参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致**allow-direct**配置失效。例如，当配置**allow-direct**参数引入OSPFv3直连时，在路由策略中不要配置**if-match** **route-type**匹配条件，否则，**allow-direct**参数失效。

**[cost*** cost*]：引入路由的路由开销，取值范围为0～4261412864。

**[level-1**]：引入路由到Level-1的路由表中。

**[level-1-2**]：引入路由到Level-1和Level-2的路由表中。

**[level-2**]：引入路由到Level-2的路由表中。如果不指定引入的级别，默认为引入路由到Level-2路由表中。

**[route-policy*** route-policy-name*]：用来过滤引入的路由的路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag ***tag*]：为引入的路由分配管理标签号，取值范围1～4294967295。

**[allow-ibgp**]：允许引入IBGP路由，只有当*protocol*为bgp4+时，该参数可选。

【使用指导】

对IPv6 IS-IS而言，其它路由协议发现的路由总被当作路由域外部的路由来处理。从其它协议引入IPv6路由时，还可指定引入路由的缺省开销cost。

在IPv6 IS-IS引入路由时，可以指定将路由引入到Level-1级、Level-2级或者Level-1-2级路由表中。

需要注意的是，**import-route bgp4+**表示只引入EBGP路由，**import-route bgp4+ allow-ibgp**表示将IBGP路由也引入，容易引起路由环路，请慎用。

【举例】

\# IPv6 IS-IS引入静态路由，并配置cost值为15。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 import-route static cost 15

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route isisv6 level-1 into level-2**

------------------------------------------------------------------------

**[import-route isisv6 level-1 into level-2**]命令用来配置从Level-1向Level-2进行路由渗透。

**[undo import-route isisv6 level-1 into level-2**]命令用来配置不从Level-1向Level-2进行路由渗透。

【命令】

**[import-route isisv6 level-1 into level-2**[ [ **filter-policy** { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } \| **tag** *tag* ] \*]]

**[undo import-route isisv6 level-1 into level-2**]

【缺省情况】

从Level-1向Level-2进行路由渗透。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[filter-policy**]：过滤策略。

*[acl6-number*]：IPv6 ACL的编号，取值范围2000～3999。

**[prefix-list*** prefix-list-name*]：IPv6地址前缀列表名称，*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy*** route-policy-name*]：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag** *tag*]：为引入的路由分配管理标签号，取值范围1～4294967295。

【使用指导】

Level-1-2路由器可以将它所知道的其他区域的Level-1区域路由信息发布给本区域的Level-2和Level-1-2路由器。

【举例】

\# 设定路由器从Level-1向Level-2进行路由渗透。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 import-route isisv6 level-1 into level-2

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route isisv6 level-2 into level-1**

------------------------------------------------------------------------

**[import-route isisv6 level-2 into level-1**]命令用来配置从Level-2向Level-1进行路由渗透。

**[undo import-route isisv6 level-2 into level-1**]命令用来恢复缺省情况。

【命令】

**[import-route isisv6 level-2 into level-1**[ [ **filter-policy** { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } \| **tag** *tag* ] \*]]

**[undo import-route isisv6 level-2 into level-1**]

【缺省情况】

不从Level-2向Level-1进行路由渗透。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[filter-policy**]：过滤策略。

*[acl6-number*]：IPv6 ACL的编号，取值范围2000～3999。

**[prefix-list*** prefix-list-name*]：IPv6地址前缀列表名称，*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy*** route-policy-name*]：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。

**[tag** *tag*]：为引入的路由分配管理标签号，取值范围1～4294967295。

【使用指导】

Level-1-2路由器可以将它所知道的其他区域的Level-2区域路由信息发布给本区域的Level-1和Level-1-2路由器。

【举例】

\# 设定路由器从Level-2向Level-1进行路由渗透。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 import-route isisv6 level-2 into level-1

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route limit**

------------------------------------------------------------------------

**[import-route limit**]命令用来配置引入Level1/Level2的IPv6路由最大条数。

**[undo import-route limit**]命令用来恢复缺省情况。

【命令】

**[import-route limit ***number*]

**[undo import-route limit**]

【缺省情况】

引入Level1/Level2的IPv6路由最大条数与设备的型号有关，请以设备的实际情况为准。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：引入Level1/Level2的IPv6路由最大条数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。

【举例】

\# 配置IS-IS进程1引入Level1/Level2的IPv6路由最大条数为1000。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 import-route limit 1000

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 bfd enable**

------------------------------------------------------------------------

![说明](IPv6%20IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[isis ipv6 bfd enable**]命令用来在使能IPv6 IS-IS的BFD功能。

**[undo** **isis ipv6** **bfd enable**]命令用来关闭IPv6 IS-IS的BFD功能。

【命令】

**[isis ipv6 bfd enable**]

**[undo**]**isis ipv6 bfd enable**

【缺省情况】

IPv6 IS-IS的BFD功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 使能接口GigabitEthernet1/0/1的IPv6 IS-IS BFD功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis ipv6 bfd enable

·交换应用

\# 使能接口Vlan-interface11的IPv6 IS-IS BFD功能。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 isis ipv6 bfd enable

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 cost**

------------------------------------------------------------------------

**[isis ipv6 cost**]命令用来配置接口的IPv6链路开销值。

**[undo isis ipv6 cost**]命令用来取消该配置。

【命令】

**[isis ipv6 cost ***value*****[[ **level-1** \| **level-2** ]]]

**[undo isis ipv6 cost **[[ **level-1** \| **level-2** ]]]

【缺省情况】

没有配置接口的IPv6链路开销值。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：链路开销值，取值范围为1～16777215。

**[level-1**]：配置在计算Level-1路由时使用的链路开销值。

**[level-2**]：配置在计算Level-2路由时使用的链路开销值。

【使用指导】

接口必须使能IPv6 IS-IS功能。

只有IS-IS支持IPv6拓扑标准模式的情况下，接口中配置的IPv6链路开销值才会生效。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1的IPv6链路开销值为10。

\<Sysname\> system-view

Sysname isis 100

Sysname-isis-100 address-family ipv6 unicast

Sysname-isis-100-ipv6 quit

Sysname-isis-100 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis ipv6 enable 100

Sysname-GigabitEthernet1/0/1 isis ipv6 cost 10

·交换应用

\# 配置接口Vlan-interface11的IPv6链路开销值为10。

\<Sysname\> system-view

Sysname isis 100

Sysname-isis-100 address-family ipv6 unicast

Sysname-isis-100-ipv6 quit

Sysname-isis-100 quit

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 isis ipv6 enable 100

Sysname-Vlan-interface11 isis ipv6 cost 10

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 enable**

------------------------------------------------------------------------

**[isis ipv6 enable**]命令用来使能接口IS-IS的IPv6能力。

**[undo isis ipv6 enable**]命令用来恢复缺省情况。

【命令】

**[isis ipv6 enable** [ *process-id* ]]

**[undo**]**isis ipv6 enable**

【缺省情况】

没有使能接口IS-IS的IPv6能力。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：IS-IS进程号，取值范围1～65535，缺省值为1。

【举例】

·路由应用

\# 创建IS-IS进程1，使能IPv6能力，并在接口GigabitEthernet1/0/1上使能IS-IS的IPv6能力。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 10.0001.1010.1020.1030.00

Sysname-isis-1 address-family ipv6 unicast

Sysname-isis-1-ipv6 quit

Sysname-isis-1 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2002::1/64

Sysname-GigabitEthernet1/0/1 isis ipv6 enable 1

·交换应用

\# 创建IS-IS进程1，使能IPv6能力，并在接口Vlan-interface100上使能IS-IS的IPv6能力。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 network-entity 10.0001.1010.1020.1030.00

Sysname-isis-1 address-family ipv6 unicast

Sysname-isis-1-ipv6 quit

Sysname-isis-1 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2002::1/64

Sysname-Vlan-interface100 isis ipv6 enable 1

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 prefix-suppression**

------------------------------------------------------------------------

**[isis ipv6 prefix-suppression**]命令用来配置接口的前缀抑制功能。

**[undo isis ipv6 prefix-suppression**]命令用来恢复缺省情况。

【命令】

**[isis ipv6 prefix-suppression **]

**[undo isis ipv6 prefix-suppression **]

【缺省情况】

未配置接口的前缀抑制功能。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口上使能IS-IS时，有时候不希望在LSP中发布此接口的前缀，可以通过在接口上配置此命令，减少此接口的前缀在LSP中携带，屏蔽内部节点被发布，提高安全性，加快路由收敛。

【举例】

·路由应用

\# 接口GigabitEthernet1/0/1使能前缀抑制功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 isis ipv6 prefix-suppression

·交换应用

\# 接口Vlan-interface10使能前缀抑制功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis ipv6 prefix-suppression

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 tag**

------------------------------------------------------------------------

**[isis ipv6 tag**]命令用来配置接口的Tag值。

**[undo isis ipv6 tag**]命令用来恢复缺省情况。

【命令】

**[isis ipv6 tag ***tag*]

**[undo isis ipv6 tag**]

【缺省情况】

没有配置接口的Tag值。

【视图】

接口视图

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

Sysname-GigabitEthernet1/0/1 isis ipv6 tag 4294967295

·交换应用

\# 配置接口Vlan-interface10的Tag值。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 isis ipv6 tag 4294967295

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- ispf enable**

------------------------------------------------------------------------

![说明](IPv6%20IS-IS命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ispf enable**]命令用来使能IPv6 IS-IS ISPF功能，即增量SPF计算功能。

**[undo ispf enable**]命令用来关闭IPv6 IS-IS ISPF功能。

【命令】

**[ispf enable**]

**[undo ispf enable**]

【缺省情况】

使能IPv6 IS-IS ISPF功能。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能增量SPF计算功能后，当网络的拓扑结构发生变化影响到最短路径树的结构时，只将受影响的部分节点进行修正，而不重建整棵最短路径树。

【举例】

\# 使能增量SPF计算功能。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 ispf enable

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

**[maximum load**-**balancing**]命令用来配置IPv6 IS-IS支持的等价路由的最大条数。

**[undo maximum load-balancing**]命令用来恢复缺省情况。

【命令】

**[maximum load-balancing ***number*]

**[undo maximum load-balancing**]

【缺省情况】

IPv6 IS-IS支持的等价路由的最大条数与与系统支持最大等价路由的条数相同。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：等价路由的最大条数，不同型号的设备支持的取值范围和缺省值不同，请以设备的情况为准。

【使用指导】

如果通过**max-ecmp-num**命令配置系统支持最大等价路由的条数为m，则本命令的缺省值为m，取值范围为1～m。

**[max-ecmp-num**]命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置IPv6 IS-IS支持的等价路由的最大条数为2。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 maximum load-balancing 2

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- multi-topology**

------------------------------------------------------------------------

**[multi-topology**]命令用来配置IS-IS支持IPv6拓扑。

**[undo multiple-topology**]命令用来取消IS-IS支持IPv6拓扑。

【命令】

**[multi-topology** [ **compatible** ]]

**[undo multi-topology**]

【缺省情况】

没有配置支持IPv6拓扑。

【视图】

IS-IS IPv6地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[compatible**]：支持IPv6拓扑兼容模式，发布IPv6前缀时，会向IPv4拓扑和IPv6拓扑中分别发布一份。如果未指定本参数，表示不支持IPv6拓扑兼容模式，发布IPv6前缀时，只会向IPv6拓扑中发布一份。

【使用指导】

配置此命令之后，IS-IS的IPv4和IPv6将分拓扑进行计算。

本命令必须在链路开销值类型为**wide**、**compatible**或**wide-compatible**时才能配置。

【举例】

\# 配置IS-IS支持IPv6拓扑。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 multi-topology

【相关命令】

·**cost-style**

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- preference**

------------------------------------------------------------------------

**[preference**]命令用来配置IPv6 IS-IS路由优先级。

**[undo preference**]命令用来恢复缺省情况。

【命令】

**[preference **[{ *preference* \| **route-policy** *route-policy-name* } \*]]

**[undo preference**]

【缺省情况下】

IPv6 IS-IS路由优先级为15。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference*]：IPv6 IS-IS协议优先级，取值范围为1～255。

**[route-policy*** route-policy-name*]：指定路由策略名。*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

由于在一台路由器上可能同时运行多种动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题。系统为每一种路由协议配置一个优先级，当不同协议都发现了到同一目的地址的路由时，优先级高的协议将起决定作用。

【举例】

\# 配置IPv6 IS-IS路由优先级为20。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 preference 20

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- prefix-priority**

------------------------------------------------------------------------

**[prefix-priority**]命令用来配置指定IPv6 IS-IS路由收敛的优先级。

**[undo prefix-priority**]命令用来取消该配置。

【命令】

**[prefix-priority**[ { **critical** \| **high** \| **medium** } { **prefix-list** *prefix-list-name* \| **tag** *tag-value* }]]

**[prefix-priority route-policy** *route-policy-name*]

**[undo prefix-priority**[ { **critical** \| **high** \| **medium** } [ **prefix-list** \| **tag** ]]]

**[undo prefix-priority route-policy**]

【缺省情况】

IPv6 IS-IS路由收敛的优先级为低优先级。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[critical**]：最高优先级。

**[high**]：高优先级。

**[medium**]：中优先级。

**[route-policy** *route-policy-name*]：指定路由策略名，配置路由收敛的优先级。*route-policy-name*为1～63个字符的字符串，区分大小写。

**[prefix-list ***prefix-list-name*]：指定IPv6地址前缀列表名，唯一标识一个IPv6地址前缀列表。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[tag*** tag-value*]：指定要求的标记值，取值范围为1～4294967295。

【使用指导】

IPv6 IS-IS路由的优先级越高收敛的速度越快。

需要注意的是，IPv6 IS-IS主机路由的优先级为中优先级。

【举例】

\# 配置前缀列表standtest的IPv6 IS-IS路由收敛的优先级为高优先级。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 prefix-priority high prefix-list standtest

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- set-overload**

------------------------------------------------------------------------

**[set-overload**]命令用来为当前路由器配置IPv6拓扑的过载标志位。

**[undo set-overload**]命令用来清除IPv6拓扑的过载标志位。

【命令】

**[set-overload** [ **on-startup** [ [ **start-from-nbr** *system-id* [ *timeout1* [ *nbr-timeout*  ] ] \| *timeout2* \| **wait-for-bgp4+**  *timeout3*  ]   **allow** { **external** \| **interlevel** } \* ]]]

**[undo set-overload**]

【缺省情况】

没有配置过载标志位。

【视图】

IS-IS IPv6单播地址族视图

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

**[wait-for-bgp4+** [ *timeout3* ]]：从系统启动时开始计算，如果在*timeout3*参数指定的时长内IPv6 BGP仍未收敛，过载标志位将结束置位状态。*timeout3*取值范围为5～86400秒，缺省值为600秒（10分钟）。

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

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 set-overload

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- summary**

------------------------------------------------------------------------

**[summary**]命令用来配置IPv6 IS-IS聚合路由。

**[undo summary**]命令用来删除该聚合路由。

【命令】

**[summary ***ipv6-prefix prefix-length*[ [ **avoid-feedback** \| **generate_null0_route** \| [ **level-1** \| **level-1-2** \| **level-2** ] \| **tag** ]*tag * \*]]

**[undo summary ***ipv6-prefix prefix-length *[[ **level-1** \| **level-1-2** \| **level-2** ]]]

【缺省情况】

没有配置IPv6 IS-IS聚合路由。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-prefix*]：IPv6 IS-IS聚合路由前缀。

*[prefix-length*]：IPv6 IS-IS聚合路由前缀长度，取值范围为0～128。

**[avoid-feedback**]：避免通过路由计算学习到聚合路由。

**[generate_null0_route**]：为防止路由循环而生成NULL 0路由。

**[level-1**]：只对引入到Level-1区域的路由进行聚合。

**[level-1-2**]：对向Level-1区域和Level-2区域引入的路由都进行聚合。

**[level-2**]：只对引入到Level-2区域的路由进行聚合。

*[tag*]：管理标签号，取值范围1～4294967295。

【使用指导】

如果命令中没有指定Level，缺省为**level-2**。

可以将有相同下一跳的路由聚合为一条路由，这样一方面可以减小路由表规模，另一方面可以减少本路由器生成的LSP报文和LSDB的规模。其中，被聚合的路由可以是IS-IS协议发现的路由，也可以是被引入的路由。另外，聚合后路由的开销取所有被聚合路由中最小的开销值。

【举例】

\# 配置一条2002::/32的聚合路由。

\<Sysname\> system-view

Sysname isis

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 summary 2002:: 32

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- timer spf**

------------------------------------------------------------------------

**[timer spf**]命令用来配置IPv6IS-IS路由计算的时间间隔。

**[undo timer spf**]命令用来恢复缺省情况。

【命令】

**[timer spf ***maximum-interval***** *minimum-interval*  *incremental-interval*  ]

**[undo timer spf**]

【缺省情况】

IPv6 IS-IS路由计算的最大时间间隔为5秒，最小时间间隔为50毫秒，时间间隔惩罚增量为200毫秒。

【视图】

IS-IS IPv6单播地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：IPv6 IS-IS路由计算的最大时间间隔，取值范围为1～120，单位为秒。

*[minimum-interval*]：IPv6 IS-IS路由计算的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：IPv6 IS-IS路由计算的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

根据本地维护的LSDB，运行IS-IS协议的路由器通过SPF算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。

本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

需要注意的是，*minimum-interval*和*incremental-interval*配置值不允许大于*maximum-interval*配置值。

【举例】

\# 配置路由器Sysname的IPv6 IS-IS路由计算的最大时间间隔为10秒，最小时间间隔为100毫秒，惩罚增量为300毫秒。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 address-family ipv6

Sysname-isis-1-ipv6 timer spf 10 100 300

