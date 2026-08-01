<!-- CMD-INDEX
  address-family ipv4 (VPN instance view) | VPN实例视图          | L54
  address-family vpnv4                | BGP视图/BGP-VPN实例视图 | L98
  description (VPN instance view)     | VPN实例视图          | L162
  display bgp routing-table ipv4 unicast inlabel | 任意视图             | L208
  display bgp routing-table ipv4 unicast outlabel | 任意视图             | L298
  display bgp routing-table vpnv4     | 任意视图             | L384
  display bgp routing-table vpnv4 inlabel | 任意视图             | L1082
  display bgp routing-table vpnv4 outlabel | 任意视图             | L1180
  display ospf sham-link              | 任意视图             | L1284
  display ip vpn-instance             | 任意视图             | L1444
  domain-id                           | OSPF视图           | L1618
  export route-policy                 | VPN实例视图/IPv4 VPN视图/IPv6 VPN视图 | L1674
  ext-community-type                  | OSPF视图           | L1754
  import route-policy                 | VPN实例视图/IPv4 VPN视图/IPv6 VPN视图 | L1804
  ip binding vpn-instance             | 接口视图             | L1884
  ip vpn-instance (System view)       | 系统视图             | L1954
  nesting-vpn                         | BGP VPNv4地址族视图   | L2000
  peer next-hop-invariable            | BGP VPNv4地址族视图   | L2046
  peer upe                            | BGP VPNv4地址族视图   | L2104
  peer upe route-policy               | BGP VPNv4地址族视图   | L2156
  policy vpn-target                   | BGP VPNv4地址族视图   | L2224
  reserve-vlan (VPN instance view)    | VPN实例视图          | L2268
  route-distinguisher (VPN instance view) | VPN实例视图          | L2328
  route-tag                           | OSPF视图           | L2382
  routing-table limit                 | VPN实例视图/IPv4 VPN视图/IPv6 VPN视图 | L2450
  rr-filter                           | BGP VPNv4地址族视图   | L2532
  sham-link                           | OSPF区域视图         | L2580
  snmp context-name                   | VPN实例视图          | L2676
  snmp-agent trap enable l3vpn        | 系统视图             | L2758
  tnl-policy (VPN instance view/IPv4 VPN view/IPv6 VPN view) | VPN实例视图/IPv4 VPN视图/IPv6 VPN视图 | L2800
  vpn popgo                           | BGP视图            | L2892
  vpn-id                              | VPN实例视图          | L2944
  vpn-instance-capability simple      | OSPF视图           | L2996
  vpn-target (VPN Instance view/IPv4 VPN view/IPv6 VPN view) | VPN实例视图/IPv4 VPN视图/IPv6 VPN视图 | L3040
  address-family ipv6 (VPN instance view) | VPN实例视图          | L3142
  address-family vpnv6                | BGP视图            | L3186
  disable-dn-bit-check                | OSPFv3视图         | L3234
  disable-dn-bit-set                  | OSPFv3视图         | L3290
  display bgp routing-table vpnv6     | 任意视图             | L3346
  display bgp routing-table vpnv6 inlabel | 任意视图             | L3888
  display bgp routing-table vpnv6 outlabel | 任意视图             | L3990
  display ospfv3 sham-link            | 任意视图             | L4094
  domain-id                           | OSPFv3视图         | L4268
  ext-community-type                  | OSPFv3视图         | L4338
  policy vpn-target                   | BGP VPNv6地址族视图   | L4392
  route-tag                           | OSPFv3视图         | L4436
  route-tag-check enable              | OSPFv3视图         | L4508
  rr-filter                           | BGP VPNv6地址族视图   | L4560
  sham-link                           | OSPFv3区域视图       | L4608
  vpn-instance-capability simple      | OSPFv3视图         | L4676
-->

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- address-family ipv4 (VPN instance view)**

------------------------------------------------------------------------

**[address-family ipv4**]命令用来进入IPv4 VPN视图。

**[undo address-family ipv4**]命令用来删除IPv4 VPN视图下的所有配置。

【命令】

**[address-family ipv4**]

**[undo address-family ipv4**]

【视图】

VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在IPv4 VPN视图下可以配置IPv4 VPN的参数，如IPv4 VPN应用的出方向路由策略、入方向路由策略等。

【举例】

\# 进入IPv4 VPN视图。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 address-family ipv4

Sysname-vpn-ipv4-vpn1

【相关命令】

·**address-family ipv6 **(VPN instance view)

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- address-family vpnv4**

------------------------------------------------------------------------

**[address-family vpnv4**]命令用来创建BGP VPNv4地址族或BGP-VPN VPNv4地址族，并进入相应地址族视图。

**[undo address-family vpnv4**]命令用来删除BGP VPNv4地址族或BGP-VPN VPNv4地址族，及相应地址族视图下的所有配置。

【命令】

**[address-family vpnv4**]

**[undo address-family vpnv4**]

【缺省情况】

没有创建BGP VPNv4地址族和BGP-VPN VPNv4地址族。

【视图】

BGP视图/BGP-VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

VPNv4地址是指在IPv4地址前缀前增加RD后，形成的地址。VPNv4路由是指携带VPNv4地址的路由信息。

在PE设备上，进入BGP VPNv4地址族视图或BGP-VPN VPNv4地址族视图，在该视图下通过**peer enable**命令使能BGP对等体后，PE才能与该对等体交换BGP VPNv4路由。

在BGP VPNv4地址族视图下，还可以配置BGP-VPNv4路由的属性，例如为从对等体/对等体组接收的BGP-VPNv4路由分配的首选值、是否允许本地AS号在接收的BGP-VPNv4路由的AS_PATH属性中出现等。

BGP VPNv4地址族视图下的配置用来控制PE设备之间交互的VPNv4路由。

BGP-VPN VPNv4地址族视图下的配置用来控制嵌套VPN组网中，运营商PE和运营商CE之间交互的VPNv4路由。

【举例】

\# 创建BGP VPNv4地址族，并进入BGP VPNv4地址族视图。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv4

Sysname-bgp-vpnv4

\# 创建BGP-VPN VPNv4地址族，进入BGP-VPN VPNv4地址族视图。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp ip vpn-instance vpn1

Sysname-bgp-vpn1 address-family vpnv4

Sysname-bgp-vpnv4-vpn1

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- description (VPN instance view)**

------------------------------------------------------------------------

**[description**]命令用来配置当前VPN实例的描述信息。

**[undo description**]命令用来删除当前VPN实例的描述信息。

【命令】

**[description ***text*]

**[undo** **description**]

【缺省情况】

未配置VPN实例的描述信息。

【视图】

VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：VPN实例的描述信息，为1～79个字符的字符串，区分大小写。

【使用指导】

如果多次执行本命令，则新的配置会覆盖原有配置。

【举例】

\# 配置名为vpn1的VPN实例的描述信息为"This is vpn1"。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 description This is vpn1

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- display bgp routing-table ipv4 unicast inlabel**

------------------------------------------------------------------------

**[display bgp routing-table ipv4 unicast inlabel**]命令用来显示BGP IPv4单播路由的入标签信息。

【命令】

**[display bgp** **routing-table ipv4** [ **unicast**   **vpn-instance** *vpn-instance-name*  **inlabel**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例内BGP IPv4单播路由的入标签信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网BGP IPv4单播路由的入标签信息。

【使用指导】

执行本命令时指定**unicast**参数和不指定**unicast**参数的效果相同。

【举例】

\# 显示公网内所有BGP IPv4单播路由的入标签信息。

\<Sysname\> display bgp routing-table ipv4 inlabel

 Total number of routes: 1

 BGP local router ID is 3.3.3.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

     Network            NextHop         OutLabel        InLabel

\* \>  2.2.2.9/32         1.1.1.2         1151            1279

表1-1 display bgp routing-table ipv4 unicast inlabel命令输出信息描述表

字段

描述

Total number of routes

BGP路由总数

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码，请参见 表1-3(?-98344000#_Ref309652945)

Origin

路由起源代码，请参见 表1-3(?-98344000#_Ref309652945)

Network

目的网络地址

NextHop

下一跳IP地址

OutLabel

出标签值，即对等体为IPv4路由分配的标签

InLabel

入标签值，即本地为IPv4路由分配的标签

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- display bgp routing-table ipv4 unicast outlabel**

------------------------------------------------------------------------

**[display bgp routing-table ipv4 unicast outlabel**]命令用来显示BGP IPv4单播路由的出标签信息。

【命令】

**[display bgp** **routing-table ipv4** [ **unicast**   **vpn-instance** *vpn-instance-name*  **outlabel**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance ***vpn-instance-name*]：显示指定VPN实例内BGP IPv4单播路由的出标签信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示公网BGP IPv4单播路由的出标签信息。

【使用指导】

执行本命令时指定**unicast**参数和不指定**unicast**参数的效果相同。

【举例】

\# 显示公网所有BGP IPv4单播路由的出标签信息。

\<Sysname\> display bgp routing-table ipv4 outlabel

 Total number of routes: 1

 BGP local router ID is 3.3.3.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

     Network            NextHop         OutLabel

\* \>  2.2.2.9/32         1.1.1.2         1151

表1-2 display bgp routing-table ipv4 unicast outlabel命令输出信息描述表

字段

描述

Total number of routes

BGP路由总数

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码，请参见 表1-3(?-98344000#_Ref309652945)

Origin

路由起源代码，请参见 表1-3(?-98344000#_Ref309652945)

Network

目的网络地址

NextHop

下一跳IP地址

OutLabel

出标签值，即对等体为IPv4路由分配的标签

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- display bgp routing-table vpnv4**

------------------------------------------------------------------------

**[display bgp routing-table vpnv4**]命令用来显示BGP VPNv4路由信息。

【命令】

**[display bgp routing-table vpnv4 **[ [ **route-distinguisher** *route-distinguisher*  [ *network-address* [ { *mask* \| *mask-length* } [ **longest-match** ] ] \| *network-address* [ *mask* \| *mask-length* ] **advertise-info** \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } ] \|  **vpn-instance** *vpn-instance-name*  **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* [ *mask* \| *mask-length* ] \| **statistics** ] \| **statistics** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的BGP VPNv4路由信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

*[network-address*]：目的网段的IP地址。

*[mask*]：网络掩码，为点分十进制格式。

*[mask-l*]*ength*：掩码长度，取值范围为0～32。

**[longest-match**]：指定根据如下方法判断显示哪条BGP VPNv4路由信息：

(1)将用户输入的网络地址和路由的掩码进行与操作；

(2)计算结果与路由的网段地址相同，且掩码小于等于用户输入子网掩码的路由中，子网掩码最长的路由将被显示出来。

**[advertise-info**]：显示BGP VPNv4路由的通告信息。

**[as-path-acl*** as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP VPNv4路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[communit-list**]：显示匹配指定BGP团体列表的BGP VPNv4路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[vpn-instance ***vpn-instance-name*]：显示向指定对等体发布或者从指定对等体收到的指定VPN实例内BGP VPNv4路由信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示向指定对等体发布或者从指定对等体收到的公网内BGP VPNv4路由信息。

**[peer**]：显示向指定对等体发布或者从指定对等体收到的BGP VPNv4路由信息。

*[ip-address*]：对等体的地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示BGP VPNv4路由的统计信息。

【使用指导】

·如果没有指定任何参数，则显示所有BGP VPNv4路由的信息。

·如果指定了*network-address mask*或*network-address mask-length*参数，则显示与指定目的网段IP地址和网络掩码（或掩码长度）精确匹配的BGP VPNv4路由的信息。

·如果只指定了*network-address*参数，没有指定*mask*和*mask-length*参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则显示该路由的信息。

【举例】

\# 显示所有BGP VPNv4路由的简要信息。

\<Sysname\> display bgp routing-table vpnv4

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 2

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 6

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>  10.1.1.0/24        10.1.1.2        0                     32768   ?

\*  e                    10.1.1.1        0                     0       65410?

\* \>  10.1.1.2/32        127.0.0.1       0                     32768   ?

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>e 192.168.1.0        10.1.1.1        0                     0       65410?

\*  i                    3.3.3.9         0          100        0       65420?

 Route distinguisher: 200:1

 Total number of routes: 2

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>i 192.168.1.0        3.3.3.9         0          100        0       65420?

\# 显示路由标识符为100:1的所有BGP VPNv4路由的简要信息。

\<Sysname\> display bgp routing-table vpnv4 route-distinguisher 100:1

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 6

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>  10.1.1.0/24        10.1.1.2        0                     32768   ?

\*  e                    10.1.1.1        0                     0       65410?

\* \>  10.1.1.2/32        127.0.0.1       0                     32768   ?

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>e 192.168.1.0        10.1.1.1        0                     0       65410?

\*  i                    3.3.3.9         0          100        0       65420?

\# 显示匹配AS路径过滤列表1的BGP VPNv4路由信息。

\<Sysname\> display bgp routing-table vpnv4 as-path-acl 1

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 2

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 6

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>  10.1.1.0/24        10.1.1.2        0                     32768   ?

\*  e                    10.1.1.1        0                     0       65410?

\* \>  10.1.1.2/32        127.0.0.1       0                     32768   ?

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>e 192.168.1.0        10.1.1.1        0                     0       65410?

\*  i                    3.3.3.9         0          100        0       65420?

 Route distinguisher: 200:1

 Total number of routes: 2

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>i 192.168.1.0        3.3.3.9         0          100        0       65420?

\# 显示匹配BGP团体列表100的BGP VPNv4路由信息。

\<Sysname\> display bgp routing-table vpnv4 community-list 100

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 2

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 6

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>  10.1.1.0/24        10.1.1.2        0                     32768   ?

\*  e                    10.1.1.1        0                     0       65410?

\* \>  10.1.1.2/32        127.0.0.1       0                     32768   ?

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>e 192.168.1.0        10.1.1.1        0                     0       65410?

\*  i                    3.3.3.9         0          100        0       65420?

 Route distinguisher: 200:1

 Total number of routes: 2

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>i 192.168.1.0        3.3.3.9         0          100        0       65420?

\# 显示向对等体3.3.3.9发布的所有公网BGP VPNv4路由信息。

\<Sysname\> display bgp routing-table vpnv4 peer 3.3.3.9 advertised-routes

 Total number of routes: 2

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 100:1

 Total number of routes: 2

     Network            NextHop         MED        LocPrf             Path/Ogn

\* \>  10.1.1.0/24        10.1.1.2        0                             ?

\* \>e 192.168.1.0        10.1.1.1        0                             65410?

\# 显示从对等体3.3.3.9收到的所有公网BGP VPNv4路由信息。

\<Sysname\> display bgp routing-table vpnv4 peer 3.3.3.9 received-routes

 Total number of routes: 2

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 200:1

 Total number of routes: 2

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>i 10.3.1.0/24        3.3.3.9         0          100        0       ?

\* \>i 192.168.1.0        3.3.3.9         0          100        0       65420?

表1-3 display bgp routing-table vpnv4命令简要显示信息描述表

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

·i - internal：内部路由

·e - external：外部路由

·s - suppressed：聚合抑制路由

·S - Stale：过期路由

Origin

路由信息的来源，取值包括：

·i -- IGP：表示路由产生于本AS内。通过**network**命令发布路由的路由信息来源为IGP

·e -- EGP：表示路由是通过EGP（Exterior Gateway Protocol，外部网关协议）学到的。

·? -- incomplete：表示路由的来源无法确定。从IGP协议引入路由的路由信息来源为incomplete

Total number of routes from all PEs

来自所有PE设备的VPNv4路由总数

Route distinguisher

路由标识符

Total number of routes

路由标识符为指定值的VPNv4路由总数

Network

目的网络地址

NextHop

下一跳IP地址

MED

MED（Multi-Exit Discriminator，多出口区分）属性值

LocPrf

本地优先级

PrefVal

路由首选值

Path/Ogn

路由的AS路径（AS_PATH）属性和路由信息的来源（ORIGIN）属性，其中：

·AS_PATH属性记录了此路由经过的所有AS，可以避免路由环路的出现

·ORIGIN属性标记了此BGP路由如何生成的

\# 显示网段10.3.1.0/24的BGP VPNv4路由的详细信息。

\<Sysname\> display bgp routing-table vpnv4 10.3.1.0 24

 BGP local router ID: 1.1.1.9

 Local AS number: 100

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 1

 Paths:   1 available, 1 best

 BGP routing table information of 10.3.1.0/24:

 From            : 3.3.3.9 (3.3.3.9)

 Rely nexthop    : 172.1.1.2

 Original nexthop: 3.3.3.9

 OutLabel        : 1279

 Ext-Community   : \<RT: 111:1\>

 AS-path         : (null)

 Origin          : incomplete

 Attribute value : MED 0, localpref 100, pref-val 0

 State           : valid, internal, best

 IP precedence   : N/A

 QoS local ID    : N/A

 Route distinguisher: 200:1

 Total number of routes: 1

 Paths:   1 available, 1 best

 BGP routing table information of 10.3.1.0/24:

 From            : 3.3.3.9 (3.3.3.9)

 Rely nexthop    : 172.1.1.2

 Original nexthop: 3.3.3.9

 OutLabel        : 1279

 Ext-Community   : \<RT: 111:1\>

 AS-path         : (null)

 Origin          : incomplete

 Attribute value : MED 0, localpref 100, pref-val 0

 State           : valid, internal, best

 IP precedence   : N/A

 QoS local ID    : N/A

\# 显示路由标识符为100:1、目的网络地址为10.3.1.0/24的BGP VPNv4路由的详细信息。

\<Sysname\> display bgp routing-table vpnv4 route-distinguisher 100:1 10.3.1.0 24

 BGP local router ID: 1.1.1.9

 Local AS number: 100

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 1

 Paths:   1 available, 1 best

 BGP routing table information of 10.3.1.0/24:

 From            : 3.3.3.9 (3.3.3.9)

 Rely nexthop    : 172.1.1.2

 Original nexthop: 3.3.3.9

 OutLabel        : 1279

 Ext-Community   : \<RT: 111:1\>

 AS-path         : (null)

 Origin          : incomplete

 Attribute value : MED 0, localpref 100, pref-val 0

 State           : valid, internal, best

 IP precedence   : N/A

 QoS local ID    : N/A

表1-4 display bgp routing-table vpnv4命令详细显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Local AS number

本地自治系统号

Route distinguisher

路由标识符

Total number of routes

路由总数

Paths

路由数信息

·available：有效路由条数

·best：最佳路由条数

BGP routing table information of 10.3.1.0/24

到达目的网络10.3.1.0/24的BGP路由表项信息

From

发布该路由的BGP对等体的IP地址

Rely Nexthop

路由迭代后的下一跳IP地址，如果没有迭代出下一跳地址，则显示为"not resolved"

Original nexthop

路由的原始下一跳地址，如果是从BGP更新消息中获得的路由，则该地址为接收到的消息中的下一跳IP地址

OutLabel

路由的出标签值

Ext-Community

扩展团体属性值

AS-path

路由的AS路径（AS_PATH）属性，记录了此路由经过的所有AS，可以避免路由环路的出现

Origin

路由信息的来源，取值包括：

·igp：表示路由产生于本AS内。通过**network**命令发布路由的路由信息来源为IGP

·egp：表示路由是通过EGP（Exterior Gateway Protocol，外部网关协议）学到的。

·incomplete：表示路由的来源无法确定。从IGP协议引入路由的路由信息来源为incomplete

Attribute value

BGP路由属性信息，包括：

·MED：与目的网络关联的MED值

·{.TableTextChar}localpref：本地优先级

·{.TableTextChar}pref-val：路由首选值

·pre：协议优先级

State

路由当前状态，取值包括：

·{.TableTextChar}valid：有效路由

·{.TableTextChar}internal：内部路由

·{.TableTextChar}external：外部路由

·{.TableTextChar}local：本地产生路由

·{.TableTextChar}synchronize：同步路由

·best：最佳路由

IP precedence

路由的IP优先级，取值范围是0～7，N/A表示无效值

QoS local ID

路由的Qos-Local-ID属性，取值范围是1～4095，N/A表示无效值

\# 显示到达目的网段10.1.1.0/24的BGP VPNv4路由的通告信息。

\<Sysname\> display bgp routing-table vpnv4 10.1.1.0 24 advertise-info

 BGP local router ID: 1.1.1.9

 Local AS number: 100

 Route distinguisher: 100:1

 Total number of routes: 1

 Paths:   1 best

 BGP routing table information of 10.1.1.0/24:

 Advertised to VPN peers (1 in total):

    3.3.3.9

 Inlabel         : 1279

表1-5 display bgp routing-table vpnv4 advertise-info命令显示信息描述表

字段

描述

BGP local router ID

本地的路由器ID

Local AS number

本地的AS号

Route distinguisher

路由标识符

Total number of routes

路由总数

Paths

到达指定目的网络的优选路由数目

BGP routing table information of 10.1.1.0/24

到达目的网络10.1.1.0/24的BGP路由的通告信息

Advertised to VPN peers (1 in total)

该路由已经向哪些VPNv4对等体发送，以及对等体的数目

Inlabel

路由的入标签

\# 显示向对等体3.3.3.9发布的公网BGP VPNv4路由的统计信息。

\<Sysname\> display bgp routing-table vpnv4 peer 3.3.3.9 advertised-routes statistics

 Advertised routes total: 2

\# 显示从对等体3.3.3.9收到的公网BGP VPNv4路由的统计信息。

\<Sysname\> display bgp routing-table vpnv4 peer 3.3.3.9 received-routes statistic

 Received routes total: 2

表1-6 display bgp routing-table vpnv4 peer statistic命令显示信息描述表

字段

描述

Advertised routes total

向指定对等体发布的路由总数

Received routes total

从指定对等体收到的路由总数

\# 显示公网BGP VPNv4路由的统计信息。

\<Sysname\> display bgp routing-table vpnv4 statistics

 Total number of routes from all PEs: 2

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 6

 Route distinguisher: 200:1

 Total number of routes: 2

表1-7 display bgp routing-table vpnv4 statistics命令显示信息描述表

字段

描述

Total number of routes from all PEs

来自所有PE设备的VPNv4路由总数

Route distinguisher

路由标识符

Total number of routes

路由标识符为指定值的VPNv4路由总数

【相关命令】

·**ip as-path**（三层技术-IP路由命令参考/路由策略）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- display bgp routing-table vpnv4 inlabel**

------------------------------------------------------------------------

**[display bgp routing-table vpnv4 inlabel**]命令用来显示所有BGP VPNv4路由的入标签信息。

【命令】

**[display bgp** **routing-table vpnv4** **inlabel**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有BGP VPNv4路由的入标签信息。

\<Sysname\> display bgp routing-table vpnv4 inlabel

 Total number of routes: 2

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 100:1

 Total number of routes: 2

     Network            NextHop         OutLabel        InLabel

\* \>  10.1.1.0/24        10.1.1.2        NULL            1279

\* \>e 192.168.1.0        10.1.1.1        NULL            1278

表1-8 display bgp routing-table vpnv4 inlabel命令输出信息描述表

字段

描述

Total number of routes

BGP路由总数

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码，请参见 表1-3(?-98344000#_Ref309652945)

Origin

路由起源代码，请参见 表1-3(?-98344000#_Ref309652945)

Route distinguisher

路由标识符

Total number of routes

路由标识符为指定值的路由总数

Network

目的网络地址

NextHop

下一跳IP地址

OutLabel

出标签值，即对端PE为VPNv4路由分配的私网标签

取值为exp-null表示为显式空标签

InLabel

入标签值，即本地PE为VPNv4路由分配的私网标签

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- display bgp routing-table vpnv4 outlabel**

------------------------------------------------------------------------

**[display bgp routing-table vpnv4 outlabel**]命令用来显示所有BGP VPNv4路由的出标签信息。

【命令】

**[display bgp** **routing-table vpnv4** **outlabel**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有BGP VPNv4路由的出标签信息。

\<Sysname\> display bgp routing-table vpnv4 outlabel

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 2

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 2

     Network            NextHop         OutLabel

\* \>i 10.3.1.0/24        3.3.3.9         1279

\*  i 192.168.1.0        3.3.3.9         1278

 Route distinguisher: 200:1

 Total number of routes: 2

     Network            NextHop         OutLabel

\* \>i 10.3.1.0/24        3.3.3.9         1279

\* \>i 192.168.1.0        3.3.3.9         1278

表1-9 display bgp routing-table vpnv4 outlabel命令输出信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码，请参见 表1-3(?-98344000#_Ref309652945)

Origin

路由起源代码，请参见 表1-3(?-98344000#_Ref309652945)

Total number of routes from all PEs

来自所有PE设备的路由数

Route distinguisher

路由标识符

Total number of routes

路由标识符为指定值的路由总数

Network

目的网络地址

NextHop

下一跳IP地址

OutLabel

出标签值，即对端PE为VPNv4路由分配的私网标签

取值为exp-null表示为显式空标签

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- display ospf sham-link**

------------------------------------------------------------------------

**[display ospf sham-link**]命令用来显示OSPF伪连接信息。

【命令】

**[display ospf ** *process-id* ] **sham-link**  **area** *area-id*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定OSPF进程内的伪连接信息。*process-id*为OSPF进程号，取值范围为1～65535。如果不指定本参数，则显示所有OSPF进程的伪连接信息。

**[area** *area-id*]：显示指定OSPF区域内的伪连接信息。*area-id*为OSPF区域号，可以是整数形式，也可以是IPv4地址形式。当是整数形式时，取值范围为0～4294967295。如果不指定本参数，则显示所有OSPF区域的伪连接信息。

【使用指导】

执行本命令时，如果不指定进程号和区域号，则显示所有的OSPF伪连接信息。

【举例】

\# 显示所有OSPF伪连接信息。

\<Sysname\> display ospf sham-link

          OSPF Process 1 with Router ID 125.1.1.1

                  Sham link

 Area            Neighbor ID     Source IP       Destination IP  State  Cost

 0.0.0.0         95.1.1.1        125.2.1.1       95.2.1.1        P-2-P  1

表1-10 display ospf sham-link命令显示信息描述表

字段

描述

Area

伪连接所属的OSPF区域

Neighbor ID

伪连接邻居的Router ID

Source IP

伪连接的源IP地址

Destination IP

伪连接的目的IP地址

State

伪连接的接口状态，取值包括Down和P-2-P

Cost

伪连接的开销

\# 显示OSPF区域1内的OSPF伪连接信息。

\<Sysname\> display ospf sham-link area 1

          OSPF Process 100 with Router ID 100.1.1.2

 Sham link: 3.3.3.3 \--\> 5.5.5.5

 Neighbor ID: 120.1.1.2        State: Full

 Area: 0.0.0.1

 Cost: 1  State: P-2-P  Type: Sham

 Timers: Hello 10, Dead 40, Retransmit 5, Transmit Delay 1

 Request list: 0  Retransmit list: 0

 MD5 authentication enabled.

    The last key is 3.

    The rollover is in progress, 1 neighbor(s) left.

表1-11 display ospf sham-link area命令显示信息描述表

字段

描述

Sham link

伪连接，从源IP地址到目的IP地址

Neighbor ID

伪连接邻居的Router ID

State

伪连接的邻居状态，取值包括Down、Init、2-Way、ExStart、Exchange、Loading和Full

Area

伪连接所属的OSPF区域

Cost

伪连接的开销

State

伪连接的状态，，取值包括Down和P-2-P

Type

伪连接的类型，取值为Sham

Timers

伪连接的定时器，包括Hello，Dead，Retransmit和Transmit Delay定时器，单位为秒

Request list 

请求列表个数

Retransmit list

重传列表个数

MD5 authentication enabled

使能了MD5认证功能

The last key

最新的MD5验证密钥

The rollover is in progress, 1 neighbor(s) left

正在进行MD5验证平滑迁移，尚未完成MD5验证平滑迁移的邻居个数为1

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- display ip vpn-instance**

------------------------------------------------------------------------

**[display ip vpn-instance**]命令用来显示VPN实例的信息。

【命令】

**[display ip vpn-instance** [ **instance-name** *vpn-instance-name*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[instance-name*** vpn-instance-name*]：显示指定VPN实例的详细信息。*vpn-instance-name*表示VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示创建的所有VPN实例的简要信息。

【举例】

\# 显示所有VPN实例的简要信息。

\<Sysname\> display ip vpn-instance

  Total VPN-Instances configured : 1

  VPN-Instance Name               RD                     Create time

  abc                             1:1                    2011/05/18 10:48:17

表1-12 display ip vpn-instance命令显示信息描述表

字段

描述

VPN-Instance Name

VPN实例名称

RD

VPN实例的路由标识符

Create time

VPN实例创建的时间

\# 显示名为vpn1的VPN实例的详细信息。

\<Sysname\> display ip vpn-instance instance-name vpn1

  VPN-Instance Name and Index : vpn1, 2

  Route Distinguisher : 100:1

  VPN ID : 1:1

  Description : vpn1

  Interfaces : GigabitEthernet1/0/2

  Address-family IPv4:

   Export VPN Targets :

       2:2

   Import VPN Targets :

       3:3

   Export Route Policy : outpolicy

   Import Route Policy : inpolicy

   Tunnel Policy : tunnel1

   Maximum Routes Limit : 500

   Threshold Value(%): 50

  Address-family IPv6:

   Export VPN Targets :

       2:2

   Import VPN Targets :

       3:3

   Export Route Policy : outpolicy

   Import Route Policy : inpolicy

   Tunnel Policy : tunnel1

   Maximum Routes Limit :500

   Threshold Value(%): 50

表1-13 display ip vpn-instance instance-name命令显示信息描述表

字段

描述

VPN-Instance Name and Index

VPN实例名称和索引

Route Distinguisher

VPN实例的路由标识符值

VPN ID

VPN实例的ID，即VPN实例的全局唯一标识

Description

VPN实例的描述信息

Interfaces

关联该VPN实例的接口

Address-family IPv4

IPv4 VPN的信息

Address-family IPv6

IPv6 VPN的信息

Export VPN Targets

IPv4 VPN或IPv6 VPN的出方向扩展团体属性

Import VPN Targets

IPv4 VPN或IPv6 VPN的入方向扩展团体属性

Export Route Policy

IPv4 VPN或IPv6 VPN的出方向路由策略

Import Route Policy

IPv4 VPN或IPv6 VPN的入方向路由策略

Tunnel Policy

IPv4 VPN或IPv6 VPN的隧道策略

Maximum Routes Limit

IPv4 VPN或IPv6 VPN的路由最大条数

Threshold Value(%)

IPv4 VPN或IPv6 VPN实例中激活路由条数的告警门限值

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- domain-id**

------------------------------------------------------------------------

**[domain-id**]命令用来配置OSPF域标识符。

**[undo domain-id**]命令用来恢复缺省情况。

【命令】

**[domain-id** *domain-id* [ **secondary** ]]

**[undo domain-id** [ *domain-id* ]]

【缺省情况】

OSPF域标识符为0。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id*]：OSPF域标识符，可以采用以下三种形式。

·整数形式，取值范围为0～4294967295，例如：1。

·点分十进制形式，例如：0.0.0.1。

·点分十进制形式:16位用户自定义数，取值范围0～65535，例如：0.0.0.1:512。

**[secondary**]：配置的域标识符作为从标识符。如果不配置，表示配置主标识符。

【使用指导】

如果通过**domain-id**命令配置了OSPF域标识符，则PE将OSPF路由引入到BGP时，主域标识符被附加到BGP VPNv4路由上，作为BGP的扩展团体属性传递给对端PE。对端PE接收到BGP路由后，将本地配置的OSPF主域标识符、从域标识符和路由中携带的OSPF域标识符进行比较：如果主域标识符或从域标识符与其相同，且为区域内或区域间路由，则将路由重新引入到OSPF时，该路由作为Network Summary LSA（即Type-3 LSA）发布给CE；否则，该路由将作为AS External LSA（即Type-5 LSA）或NSSA External LSA（即Type-7 LSA）发布给CE。

执行**undo domain-id**命令时，如果不指定参数，将删除所有域标识符。

【举例】

\# 配置OSPF域标识符为234。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 domain-id 234

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- export route-policy**

------------------------------------------------------------------------

**[export route-policy**]命令用来配置当前VPN实例应用出方向路由策略。

**[undo export** **route-policy**]命令用来取消当前VPN实例应用出方向路由策略。

【命令】

**[export route-policy ***route-policy*]

**[undo export route-policy**]

【缺省情况】

VPN实例没有应用出方向路由策略，不对发布的路由进行过滤。

【视图】

VPN实例视图/IPv4 VPN视图/IPv6 VPN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[route-policy*]：VPN实例的出方向路由策略名，为1～63个字符的字符串，区分大小写。

【使用指导】

如果在设备上通过本命令指定了VPN实例应用的出方向路由策略，则该VPN实例在向其他VPN实例发布路由时，将利用指定的路由策略对发布的路由进行过滤、改变发布路由的属性等。使用本命令可以更加精确、灵活地控制VPN实例之间路由的发布。

需要注意的是：

·如果多次执行本命令，则新的配置会覆盖原有配置。

·VPN实例视图下的配置，既可以用于IPv4 VPN，也可以用于IPv6 VPN；IPv4 VPN视图下的配置只能用于IPv4 VPN；IPv6 VPN视图下的配置只能用于IPv6 VPN。

·IPv4 VPN视图、IPv6 VPN视图下的配置优先级高于VPN实例视图下的配置，即如果同时在IPv4 VPN视图（或IPv6 VPN视图）和VPN实例视图下进行了配置，则IPv4 VPN（或IPv6 VPN）采用IPv4 VPN视图（或IPv6 VPN视图）下的配置。

【举例】

\# 对名为vpn1的VPN实例应用出方向路由策略poly-1。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 export route-policy poly-1

\# 对名为vpn2的IPv4 VPN应用出方向路由策略poly-2。

\<Sysname\> system-view

Sysname ip vpn-instance vpn2

Sysname-vpn-instance-vpn2 address-family ipv4

Sysname-vpn-ipv4-vpn2 export route-policy poly-2

\# 对名为vpn3的IPv6 VPN应用出方向路由策略poly-3。

\<Sysname\> system-view

Sysname ip vpn-instance vpn3

Sysname-vpn-instance-vpn3 address-family ipv6

Sysname-vpn-ipv6-vpn3 export route-policy poly-3

【相关命令】

·**import route-policy**

·**route-policy**（三层技术-IP路由命令参考/路由策略）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- ext-community-type**

------------------------------------------------------------------------

**[ext-community-type**]命令用来配置OSPF扩展团体属性的类型编码。

**[undo ext-community-type**]命令用来恢复缺省情况。

【命令】

**[ext-community-type**  { **domain-id** *type-code1* \| **router-id** *type-code2* \| **route-type** *type-code3* }]

**[undo ext-community-type ** [ **domain-id** \| **router-id** \| **route-type** ]]

【缺省情况】

OSPF扩展团体属性Domain ID的类型编码是0x0005，Router ID的类型编码是0x0107，Route Type的类型编码是0x0306。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain-id **]*type-code1*：指定OSPF扩展团体属性Domain ID的类型编码。*type-code1*取值可以为十六进制数值0005、0105、0205和8005。

**[router-id**]* type-code2*：指定OSPF扩展团体属性Router ID的类型编码。*type-code2*取值可以为十六进制数值0107和8001。

**[router-type **]*type-code3*：指定OSPF扩展团体属性Route Type的类型编码。*type-code3*取值可以为十六进制数值0306和8000。

【举例】

\# 为OSPF进程100配置OSPF扩展团体属性Domain ID的类型编码为0x8005，Router ID的类型编码为0x8001，Route Type的类型编码为0x8000。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 ext-community-type domain-id 8005

Sysname-ospf-100 ext-community-type router-id 8001

Sysname-ospf-100 ext-community-type route-type 8000

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- import route-policy**

------------------------------------------------------------------------

**[import route-policy**]命令用来配置当前VPN实例应用入方向路由策略。

**[undo import route-policy**]命令用来取消当前VPN实例应用入方向路由策略。

【命令】

**[import route-policy** *route-policy*]

**[undo import route-policy**]

【缺省情况】

VPN实例没有应用入方向路由策略。如果接收到的路由携带的Route Target属性中存在与本地配置的Import Target相同的值，则接收该路由。

【视图】

VPN实例视图/IPv4 VPN视图/IPv6 VPN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[route-policy*]：VPN实例的入方向路由策略名，为1～63个字符的字符串，区分大小写。

【使用指导】

如果在设备上通过本命令指定了VPN实例应用的入方向路由策略，则该VPN实例在接收其他VPN实例的路由后，将利用指定的路由策略对接收的路由进行过滤、改变接收路由的属性等。使用本命令可以更加精确、灵活地控制VPN实例之间路由的接收。

需要注意的是：

·如果多次执行本命令，则新的配置会覆盖原有配置。

·VPN实例视图下的配置，既可以用于IPv4 VPN，也可以用于IPv6 VPN；IPv4 VPN视图下的配置只能用于IPv4 VPN；IPv6 VPN视图下的配置只能用于IPv6 VPN。

·IPv4 VPN视图、IPv6 VPN视图下的配置优先级高于VPN实例视图下的配置，即如果同时在IPv4 VPN视图（或IPv6 VPN视图）和VPN实例视图下进行了配置，则IPv4 VPN（或IPv6 VPN）采用IPv4 VPN视图（或IPv6 VPN视图）下的配置。

【举例】

\# 对名为vpn1的VPN实例应用入方向路由策略poly-1。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 import route-policy poly-1

\# 对名为vpn2的IPv4 VPN应用入方向路由策略poly-2。

\<Sysname\> system-view

Sysname ip vpn-instance vpn2

Sysname-vpn-instance-vpn2 address-family ipv4

Sysname-vpn-ipv4-vpn2 import route-policy poly-2

\# 对名为vpn3的IPv6 VPN应用入方向路由策略poly-3。

\<Sysname\> system-view

Sysname ip vpn-instance vpn3

Sysname-vpn-instance-vpn3 address-family ipv6

Sysname-vpn-ipv6-vpn3 import route-policy poly-3

【相关命令】

·**export route-policy**

·**route-policy**（三层技术-IP路由命令参考/路由策略）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- ip binding vpn-instance**

------------------------------------------------------------------------

**[ip binding vpn-instance**]命令用来配置当前接口与指定VPN实例关联。

**[undo ip binding vpn-instance**]命令用来取消接口与VPN实例的关联。

【命令】

**[ip binding vpn-instance ***vpn-instance-name*]

**[undo ip binding vpn-instance**]

【缺省情况】

接口不与任何VPN实例关联，接口属于公网。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：接口关联的VPN实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

本命令用于在PE设备上将连接CE的接口与该CE所属的VPN实例关联。

需要注意的是：

·配置或取消接口与VPN实例关联后，该接口上的IP地址、路由协议等配置将被删除。建议在接口视图下通过**display this**命令查看接口的当前配置，并根据需要重新配置IP地址、路由协议等。

·接口关联的VPN实例，必须已经通过系统视图下的**ip vpn-instance**命令创建。

·不能通过重复执行本命令修改接口关联的VPN实例。只能通过**undo ip binding vpn-instance**命令取消关联的VPN实例后，再通过**ip binding vpn-instance**命令关联新的VPN实例。

【举例】

·路由应用

\# 将接口GigabitEthernet1/0/1与名为vpn1的VPN实例关联。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip binding vpn-instance vpn1

·交换应用

\# 将接口Vlan-interface2与名为vpn1的VPN实例关联。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 ip binding vpn-instance vpn1

【相关命令】

·**ip vpn-instance **(System view)

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- ip vpn-instance (System view)**

------------------------------------------------------------------------

**[ip vpn-instance**]命令用来创建VPN实例，并进入VPN实例视图。

**[undo ip vpn-instance**]命令用来删除指定的VPN实例。

【命令】

**[ip vpn-instance ***vpn-instance-name*]

**[undo ip vpn-instance ***vpn-instance-name*]

【缺省情况】

设备上不存在任何VPN实例。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-instance-name*]：VPN实例的名称，为1～31个字符的字符串，区分大小写。

【举例】

\# 创建一个名为vpn1的VPN实例，并进入VPN实例视图。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1

【相关命令】

·**route-distinguisher**

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- nesting-vpn**

------------------------------------------------------------------------

**[nesting-vpn**]命令用来使能嵌套VPN功能。

**[undo nesting-vpn**]命令用来禁止嵌套VPN功能。

【命令】

**[nesting-vpn**]

**[undo nesting-vpn**]

【缺省情况】

嵌套VPN功能处于禁止状态。

【视图】

BGP VPNv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

嵌套VPN是指在运营商通过MPLS L3VPN骨干网为用户提供一个大的VPN的基础上，用户可以根据实际需要管理和划分自己的内部VPN，而这些内部VPN的划分对于运营商骨干网来说是透明的。嵌套VPN为用户提供了多样化的VPN组网方式，实现了用户对内部VPN以及多层VPN之间的互访权限控制管理，可以满足多种用户网络的需求。

需要注意的是，只有在BGP VPNv4地址族视图下使能了嵌套VPN功能后，BGP-VPN VPNv4地址族视图下通过**peer enable**命令激活的对等体之间才能成功协商VPNv4路由交换能力，才能接收和发布VPNv4路由。

【举例】

\# 使能嵌套VPN功能。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv4

Sysname-bgp-vpnv4 nesting-vpn

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- peer next-hop-invariable**

------------------------------------------------------------------------

**[peer next-hop-invariable**]命令用来配置向EBGP对等体/对等体组发布路由时不改变下一跳。

**[undo peer next-hop-invariable**]命令用来恢复缺省情况。

【命令】

**[peer**[{ *group-name* \| *ip-address* [ *mask-length* ] } **next-hop-invariable**]]

**[undo** **peer** [{ *group-name* \| *ip-address* [ *mask-length* ] } **next-hop-invariable**]]

【缺省情况】

向EBGP对等体/对等体组发布路由时会将下一跳改为自己的地址。

【视图】

BGP VPNv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：对等体组的名称，为1～47个字符的字符串，区分大小写。

*[ip-address*]：对等体的IP地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

【使用指导】

如果在跨域VPN OptionC组网中使用路由反射器RR（Route Reflector）通告VPNv4路由，则需要在路由反射器上通过本命令配置向EBGP邻居和反射客户通告VPNv4路由时，不改变路由的下一跳，以保证私网路由下一跳不会被修改。

需要注意的是，本命令与**peer next-hop-local**命令互斥。

【举例】

\# 在BGP VPNv4地址族视图下，配置向EBGP对等体1.1.1.1发布路由时不改变下一跳。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv4

Sysname-bgp-af-vpnv4 peer 1.1.1.1 next-hop-invariable

【相关命令】

·**peer next-hop-local**（三层技术-IP路由命令参考/BGP）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- peer upe**

------------------------------------------------------------------------

**[peer upe**]命令用来在BGP VPNv4地址族视图下，指定BGP对等体或对等体组作为HoVPN的UPE。

**[undo peer upe**]命令用来取消该配置。

【命令】

**[peer**[ { *group-name* \| *ip-address* [ *mask-length* ] } **upe**]]

**[undo**[ **peer** { *group-name* \| *ip-address* [ *mask-length* ] } **upe**]]

【缺省情况】

BGP对等体或对等体组不是HoVPN的UPE。

【视图】

BGP VPNv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：对等体组的名称，为1～47个字符的字符串，区分大小写。指定的对等体组必须已经创建。

*[ip-address*]：对等体的IP地址。指定的对等体必须已经创建。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

【使用指导】

UPE是一类特殊的VPNv4对等体，它可以接收SPE上每个相关VPN实例的一条缺省路由，也可以接收SPE上发送的通过路由策略过滤的路由信息。SPE是普通的VPN对等体。

【举例】

\# 指定对等体1.1.1.1作为UPE。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv4

Sysname-bgp-vpnv4 peer 1.1.1.1 upe

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- peer upe route-policy**

------------------------------------------------------------------------

**[peer upe route-policy**]命令用来配置向指定的UPE发布经过路由策略过滤的路由信息。

**[undo peer upe route-policy**]命令用来恢复缺省情况。

【命令】

**[peer**[{ *group-name* \| *ip-address* [ *mask-length* ] } **upe route-policy** *route-policy-name* **export**]]

**[undo**[ **peer** { *group-name* \| *ip-address* [ *mask-length* ] } **upe route-policy export**]]

【缺省情况】

不向对等体发布路由。

【视图】

BGP VPNv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：对等体组的名称，为1～47个字符的字符串，区分大小写。指定的对等体组必须已经创建。

*[ip-address*]：对等体的IP地址。指定的对等体必须已经创建。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[route-policy-name*]：路由策略的名称，为1～63个字符的字符串，区分大小写。

**[export**]：对发布的路由应用过滤策略。

【使用指导】

本命令必须和**peer upe**命令配合使用。

【举例】

\# 在BGP VPNv4地址族视图下，配置对等体1.1.1.1为UPE，并向1.1.1.1发送通过路由策略hope过滤的路由信息。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp peer 1.1.1.1 as-number 200

Sysname-bgp address-family vpnv4

Sysname-bgp-vpnv4 peer 1.1.1.1 enable

Sysname-bgp-vpnv4 peer 1.1.1.1 upe

Sysname-bgp-vpnv4 peer 1.1.1.1 upe route-policy hope export

【相关命令】

·**peer upe**

·**route-policy**（三层技术-IP路由命令参考/路由策略）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- policy vpn-target**

------------------------------------------------------------------------

**[policy vpn-target**]命令用来对接收到的VPNv4路由使能VPN-Target过滤功能，即只将Export Route Target属性与本地Import Route Target属性匹配的VPNv4路由加入到路由表。

**[undo policy vpn-target**]命令用来取消对VPNv4路由的VPN-Target过滤功能，即接收所有VPNv4路由。

【命令】

**[policy vpn-target**]

**[undo policy vpn-target**]

【缺省情况】

对接收到的VPNv4路由使能VPN-Target过滤功能。

【视图】

BGP VPNv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在跨域VPN OptionB组网中，ASBR需要保存所有VPNv4路由信息，以通告给对端ASBR。这种情况下，ASBR上需执行**undo policy vpn-target**命令接收所有的VPNv4路由信息，不对它们进行Route Target过滤。

【举例】

\# 在BGP VPNv4地址族视图下，取消对VPNv4路由的Route Target过滤功能。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv4

Sysname-bgp-vpnv4 undo policy vpn-target

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- reserve-vlan (VPN instance view)**

------------------------------------------------------------------------

**[reserve-vlan**]命令用来配置VPN实例的保留VLAN。

**[undo reserve-vlan**]命令用来恢复缺省情况。

【命令】

**[reserve-vlan** *vlan-id*]

**[undo reserve-vlan**]

【缺省情况】

没有指定VPN实例的保留VLAN。

【视图】

VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：保留VLAN的VLAN ID。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

保留VLAN用来为VPN实例预留一定的系统资源，以便满足VPN实例的报文转发需求。

需要注意的是：

·普通VLAN（缺省VLAN、通过**vlan**命令创建的VLAN、动态学习到的VLAN）不能指定为VPN实例的保留VLAN；将某个VLAN指定为VPN实例的保留VLAN后，不能通过**vlan**命令创建该VLAN，也不能动态学习该VLAN。

·为不同VPN实例指定的保留VLAN不能相同。

![说明](MPLS%20L3VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置VPN实例vpn1的保留VLAN为VLAN 100。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 reserve-vlan 100

【相关命令】

·**vlan**（二层技术-以太网交换命令参考/VLAN）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- route-distinguisher (VPN instance view)**

------------------------------------------------------------------------

**[route-distinguisher**]命令用来配置VPN实例的RD（Route Distinguisher，路由标识）。

**[undo route-distinguisher**]命令用来删除VPN实例的RD值。

【命令】

**[route-distinguisher** *route-distinguisher*]

**[undo route-distinguisher**]

【缺省情况】

没有指定VPN实例的RD。

【视图】

VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[route-distinguisher*]：路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

【使用指导】

RD用于解决不同VPN之间地址空间重叠的问题。如果在配置时保证了RD的全局唯一性，则将RD添加到一个IPv4前缀之前，就可以使之成为全局唯一的VPN IPv4前缀。这样，即使不同VPN使用了同样的IPv4地址空间，PE路由器也可以向各VPN发布不同VPN IPv4前缀的路由。

需要注意的是，不能通过重复执行**route-distinguisher**命令修改VPN实例的RD值。必须先通过**undo route-distinguisher**命令删除VPN实例的RD值，再通过**route-distinguisher**命令配置新的RD值。

【举例】

\# 配置VPN实例vpn1的RD为22:1。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 route-distinguisher 22:1

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- route-tag**

------------------------------------------------------------------------

**[route-tag**]命令用来配置VPN引入路由的外部路由标记值。

**[undo route-tag**]命令用来恢复缺省值。

【命令】

**[route-tag** *tag-value*]

**[undo route-tag**]

【缺省情况】

若MPLS骨干网上配置了BGP路由协议，并且BGP的AS号不大于65535，则外部路由标记值的前面两个字节固定为0xD000，后面的两个字节为本端BGP的AS号；否则，外部路由标记值为0。例如，本端BGP AS号为100时，外部路由标记的缺省值为十进制值3489661028，即0xD0000000对应的十进制值（3489660928）+100。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag-value*]：VPN引入路由的外部路由标记值，取值范围为0～4294967295。

【使用指导】

在CE双归属（CE连接两个PE）、且PE和CE之间采用OSPF协议交互私网路由的组网中，外部路由标记可以用来避免路由环路。CE连接的一台PE将从对端PE接收到的BGP路由引入OSPF，并通过Type-5或Type-7 LSA发布给CE时，为该Type-5或Type-7 LSA添加本地配置的外部路由标记。另一台PE接收到CE发布的Type-5或Type-7 LSA后，将其中的外部路由标记值与本地配置的值进行比较。如果相同，则在进行路由计算时忽略该LSA，从而避免路由环路。

外部路由标记值的配置方式及各种方式的优先级为：

·**import-route**命令配置的tag值优先级最高；

·**route-tag**命令配置的tag值优先级其次；

·**default tag**命令配置的tag值优先级最低。

需要注意的是：

·同一个区域的PE建议配置相同的外部路由标记值。

·外部路由标记值不会在BGP的扩展团体属性中传递，它只在收到BGP路由并且产生OSPF Type-5或Type-7 LSA的PE路由器上起作用。

·可以为不同的OSPF进程配置相同的外部路由标记值。

【举例】

\# 为OSPF进程100配置VPN引入路由的外部路由标记值为100。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 route-tag 100

【相关命令】

·**import-route**（三层技术-IP路由命令参考/OSPF）

·**default**（三层技术-IP路由命令参考/OSPF）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- routing-table limit**

------------------------------------------------------------------------

**[routing-table limit**]命令用来限制当前VPN实例支持的最多激活路由前缀数。

**[undo routing-table limit**]命令用来恢复缺省情况。

【命令】

**[routing-table**[ **limit** *number* { *warn-threshold* \| **simply-alert** }]]

**[undo routing-table limit**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

VPN实例视图/IPv4 VPN视图/IPv6 VPN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：指定一个VPN实例最多可以支持的激活路由前缀数。不同设备支持的取值范围不同，请以设备的实际情况为准。

*[warn-threshold*]：告警门限值，取值范围为1～100，单位为百分比。当（VPN实例中的激活路由前缀数/最多支持激活路由前缀数×100）达到告警门限值时，产生一条告警信息，但仍然允许激活路由前缀。当VPN实例中的激活路由前缀数达到最多支持激活路由前缀数目时，不再激活新的路由前缀。

**[simply-alert**]：指定当VPN实例的激活路由前缀数超过最多支持的激活路由前缀数目时，可以继续激活新的路由前缀，但会产生一条系统日志Syslog信息。

【使用指导】

通过本命令可以避免PE路由器引入太多的VPN激活路由前缀。

需要注意的是：

·VPN实例视图下的配置，既可以用于IPv4 VPN，也可以用于IPv6 VPN；IPv4 VPN视图下的配置只能用于IPv4 VPN；IPv6 VPN视图下的配置只能用于IPv6 VPN。

·IPv4 VPN视图、IPv6 VPN视图下的配置优先级高于VPN实例视图下的配置，即如果同时在IPv4 VPN视图（或IPv6 VPN视图）和VPN实例视图下进行了配置，则IPv4 VPN（或IPv6 VPN）采用IPv4 VPN视图（或IPv6 VPN视图）下的配置。

【举例】

\# 限制名为vpn1的VPN实例最多可支持1000条激活路由前缀，并且当激活路由前缀数超过最多支持激活路由前缀数时，可以继续激活新的路由前缀，但是会产生一条系统日志Syslog信息。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 route-distinguisher 100:1

Sysname-vpn-instance-vpn1 routing-table limit 1000 simply-alert

\# 限制名为vpn2的IPv4 VPN最多可支持1000条激活路由前缀，并且当激活路由前缀数超过最多支持激活路由前缀数时，可以继续激活新的路由前缀，但是会产生一条系统日志Syslog信息。

\<Sysname\> system-view

Sysname ip vpn-instance vpn2

Sysname-vpn-instance-vpn2 route-distinguisher 100:2

Sysname-vpn-instance-vpn2 address-family ipv4

Sysname-vpn-ipv4-vpn2 routing-table limit 1000 simply-alert

\# 限制名为vpn3的IPv6 VPN最多可支持1000条激活路由前缀，并且当激活路由前缀数超过最多支持激活路由前缀数时，可以继续激活新的路由前缀，但是会产生一条系统日志Syslog信息。

\<Sysname\> system-view

Sysname ip vpn-instance vpn3

Sysname-vpn-instance-vpn3 route-distinguisher 100:3

Sysname-vpn-instance-vpn3 address-family ipv6

Sysname-vpn-ipv4-vpn3 routing-table limit 1000 simply-alert

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- rr-filter**

------------------------------------------------------------------------

**[rr-filter**]命令用来创建路由反射器的反射策略：通过配置路由反射器支持的扩展团体属性号，对接收的路由信息进行过滤，只有接收的VPNv4路由包含指定的扩展团体属性号时，路由反射器才会反射该路由。

**[undo** **rr-filter**]命令用来恢复缺省情况。

【命令】

**[rr-filter ***extended-community-number*]

**[undo rr-filter**]

【缺省情况】

路由反射器不会对反射的路由进行过滤。

【视图】

BGP VPNv4地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[extended-community-number*]：路由反射器支持的扩展团体属性号，取值范围1～199。

【使用指导】

当一个集群中存在多个路由反射器时，通过在不同的路由反射器上配置不同的反射策略，可以实现路由反射器之间的负载分担。

【举例】

\# 在BGP VPNv4地址族视图下，配置路由反射器支持的扩展团体属性号为10，即该路由反射器只反射包含扩展团体属性10的VPNv4路由。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv4

Sysname-bgp-vpnv4 rr-filter 10

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- sham-link**

------------------------------------------------------------------------

**[sham-link**]命令用来创建一条OSPF伪连接。

**[undo sham-link**]命令用来删除一条已有的OSPF伪连接，或者将指定OSPF伪连接的参数恢复为缺省值。

【命令】

**[sham-link ***source-ip-address*[ *destination-ip-address* [ **cost** *cost* \| **dead** *dead-interval* \| **hello** *hello-interval* \| { { **hmac-md5** \| **md5** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* } \| **simple** { **cipher** *cipher-string* \| **plain** *plain-string* } } \| **retransmit** *retrans-interval* \| **trans-delay** *delay* ] \*]]

**[undo sham-link ***source-ip-address******destination-ip-address*****[[ **cost** \| **dead** \| **hello** \| { { **hmac-md5** \| **md5** } *key-id* \| **simple** } \| **retransmit** \| **trans-delay** ] \*]]

【缺省情况】

设备上不存在任何OSPF伪连接。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-ip-address*]：OSPF伪连接的源IP地址。

*[destination-ip-address*]：OSPF伪连接的目的IP地址。

**[cost*** cost*]：伪连接开销，取值范围为1～65535，缺省值为1。

**[dead ***dead-interval*]：失效间隔，取值范围为1～32768，单位为秒，缺省值为40秒。建立伪连接的两个路由器上需要配置相同的*dead-interval*，且至少为*hello-interval*的4倍。

**[hello*** hello-interval*]：接口上发送Hello报文的时间间隔，取值范围为1～8192，单位为秒，缺省值为10秒。建立伪连接的两个路由器上需要配置相同的*hello-interval*。

**[hmac-md5**]：HMAC-MD5验证模式。

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

*[key-id*]：MD5/HMAC-MD5验证字标识符，取值范围为1～255。

**[cipher**]：以密文形式设置密钥。

*[cipher-string*]：密文密钥，区分大小写。对于简单验证模式，为33～41个字符的字符串，对于MD5/HMAC-MD5验证模式，为33～53个字符的字符串。

**[plain**]：以明文形式设置密钥。

*[plain-string*]：明文密钥，区分大小写。对于简单验证模式，为1～8个字符的字符串，对于MD5/HMAC-MD5验证模式，为1～16个字符的字符串。

**[retransmit*** retrans-interval*]：接口上重传LSA报文的时间间隔，取值范围是1～3600，单位为秒，缺省值为5秒。

**[trans-delay ***delay*]：接口上延迟发送LSA报文的时间间隔，取值范围为1～3600，单位为秒，缺省值为1秒。

【使用指导】

属于同一个VPN的两个Site之间存在一条区域内OSPF链路（backdoor链路）时，为了避免VPN流量总是通过backdoor链路转发而不走骨干网，可以在PE路由器之间建立OSPF伪连接（Sham-link），使经过MPLS VPN骨干网的路由也成为OSPF区域内路由，确保VPN流量通过骨干网转发。

可以使用MD5/HMAC-MD5验证或简单验证两种方式对OSPF伪连接进行验证，但不能同时使用两种验证方式。使用MD5/HMAC-MD5验证方式时，可配置多条MD5/HMAC-MD5验证命令，但同一*key-id*只能配置一个验证字。

修改伪连接的OSPF MD5/HMAC-MD5验证字的步骤如下：

(1)为伪连接配置新的MD5/HMAC-MD5验证字。此时若邻居设备尚未配置新的MD5/HMAC-MD5验证字，便会触发MD5/HMAC-MD5验证平滑迁移过程。在这个过程中，OSPF会发送分别携带各个MD5/HMAC-MD5验证字的多份报文，使得无论邻居设备上是否配置新验证字都能验证通过，保持邻居关系。

(2)在邻居设备上也配置相同的新MD5/HMAC-MD5验证字。当本设备上收到邻居的携带新验证字的报文后，便会退出MD5/HMAC-MD5验证平滑迁移过程。

(3)在本设备和邻居上都执行**undo sham-link**命令删除旧的MD5/HMAC-MD5验证字。建议不要为伪连接保留多个MD5/HMAC-MD5验证字，每次MD5/HMAC-MD5验证字修改完毕后，应当及时删除旧的验证字，这样可以防止与持有旧验证字的系统继续通信、减少被攻击的可能，还可以减少验证迁移过程对系统、带宽的消耗。

需要注意的是：

·同一VPN实例的不同OSPF进程下，不能配置源地址、目的地址都相同的伪连接。

·两端PE上配置的伪连接必须属于相同的OSPF区域，否则，无法建立OSPF邻居。

【举例】

\# 创建一条OSPF伪连接，源地址为1.1.1.1，目的地址为2.2.2.2。

\<Sysname\> system-view

Sysname ospf

Sysname-ospf-1 area 0

Sysname-ospf-1-area-0.0.0.0 sham-link 1.1.1.1 2.2.2.2

【相关命令】

·**display ospf sham-link**

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- snmp context-name**

------------------------------------------------------------------------

**[snmp context-name**]命令用来配置VPN实例的SNMP上下文。

**[undo snmp context-name**]命令用来恢复缺省情况。

【命令】

**[snmp context-name ***context-name*]

**[undo snmp context-name**]

【缺省情况】

没有指定VPN实例的SNMP上下文。

【视图】

VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：SNMP上下文名称，为1～32个字符的字符串，区分大小写。

【使用指导】

对于支持多VPN实例的功能（如AAA、NAT），通过MIB（Management Information Base，管理信息库）节点对这些功能进行管理时，这些功能无法获知被管理的节点属于哪个VPN实例。为不同的VPN实例配置不同的SNMP上下文可以解决上述问题。

设备接收到SNMP报文后，根据报文中携带的上下文（对于SNMPv3）或团体名称（对于SNMPv1/v2c），判断如何进行处理：

·对于SNMPv3报文：

¡如果报文中不携带上下文，则功能模块对公网的MIB节点进行相应处理。

¡如果报文中携带上下文，设备上存在对应的SNMP上下文（通过系统视图下的**snmp-agent context**命令创建），且该上下文与为某一个VPN实例配置的上下文相同，则功能模块对该VPN实例的MIB节点进行相应处理。

¡其他情况下，不允许对任何MIB节点进行处理。

·对于SNMPv1/v2c报文：

¡如果设备上没有通过系统视图下的**snmp-agent community-map**命令将报文中的团体名映射为SNMP上下文，则功能模块对公网的MIB节点进行相应处理。

¡如果设备上将团体名映射为SNMP上下文，设备上存在对应的SNMP上下文，且该上下文与为某一个VPN实例配置的上下文相同，则功能模块对该VPN实例的MIB节点进行相应处理。

¡其他情况下，不允许对任何MIB节点进行处理。

SNMP上下文和团体名的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

需要注意的是：

·为不同VPN实例配置的SNMP上下文不能相同。

·在同一个VPN实例下重复执行本命令，则新的配置将覆盖已有配置。

【举例】

\# 配置VPN实例vpna的SNMP上下文为vpna。

\<Sysname\> system-view

Sysname snmp-agent context vpna

Sysname ip vpn-instance vpna

Sysname-vpn-instance-vpna route-distinguisher 22:33

Sysname-vpn-instance-vpna snmp context-name vpna

【相关命令】

·**snmp-agent context**（网络管理和监控命令参考/SNMP）

·**snmp-agent community-map**（网络管理和监控命令参考/SNMP）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- snmp-agent trap enable l3vpn**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable l3vpn**]命令用来开启L3VPN模块的告警功能。

**[undo** **snmp-agent** **trap** **enable l3vpn**]命令用来关闭L3VPN模块的告警功能。

【命令】

**[snmp-agent** **trap** **enable** **l3vpn**]

**[undo** **snmp-agent** **trap** **enable** **l3vpn**]

【缺省情况】

L3VPN模块的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启L3VPN模块的告警功能后，在VPN实例内的路由数达到告警门限等情况下，L3VPN模块会产生RFC 4382中规定的告警信息。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启L3VPN模块的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable l3vpn

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- tnl-policy (VPN instance view/IPv4 VPN view/IPv6 VPN view)**

------------------------------------------------------------------------

**[tnl-policy**]命令用来配置当前VPN实例与指定的隧道策略关联。

**[undo tnl-policy**]命令用来取消当前VPN实例与隧道策略的关联。

【命令】

**[tnl-policy** *tunnel-policy-name*]

**[undo tnl-policy**]

【缺省情况】

VPN实例不与任何隧道策略关联。

【视图】

VPN实例视图/IPv4 VPN视图/IPv6 VPN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tunnel-policy-name*]：VPN实例的隧道策略名称，为1～19个字符的字符串，区分大小写。

【使用指导】

在设备上配置VPN实例与隧道策略关联后，设备将根据指定的隧道策略选择转发该VPN实例流量的隧道。

如果VPN实例没有关联隧道策略或者关联的隧道策略尚未配置，则该VPN实例根据缺省选择策略来选择隧道。缺省选择策略为按照LSP隧道－\>GRE隧道－\>CR-LSP隧道的优先级顺序选择隧道，负载分担的隧道数目为1。

需要注意的是：

·VPN实例视图下的配置，既可以用于IPv4 VPN，也可以用于IPv6 VPN；IPv4 VPN视图下的配置只能用于IPv4 VPN；IPv6 VPN视图下的配置只能用于IPv6 VPN。

·IPv4 VPN视图、IPv6 VPN视图下的配置优先级高于VPN实例视图下的配置，即如果同时在IPv4 VPN视图（或IPv6 VPN视图）和VPN实例视图下进行了配置，则IPv4 VPN（或IPv6 VPN）采用IPv4 VPN视图（或IPv6 VPN视图）下的配置。

【举例】

\# 将名为vpn1的VPN实例和隧道策略po1关联起来。

\<Sysname\> system-view

Sysname tunnel-policy po1

Sysname-tunnel-policy-po1 select-seq lsp load-balance-number 1

Sysname-tunnel-policy-po1 quit

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 route-distinguisher 22:33

Sysname-vpn-instance-vpn1 tnl-policy po1

Sysname-vpn-instance-vpn1 quit

\# 将名为vpn2的IPv4 VPN和隧道策略po1关联起来。

Sysname ip vpn-instance vpn2

Sysname-vpn-instance-vpn2 route-distinguisher 11:22

Sysname-vpn-instance-vpn2 address-family ipv4

Sysname-vpn-ipv4-vpn2 tnl-policy po1

Sysname-vpn-ipv4-vpn2 quit

Sysname-vpn-instance-vpn2 quit

\# 将名为vpn3的IPv6 VPN和隧道策略po1关联起来。

Sysname ip vpn-instance vpn3

Sysname-vpn-instance-vpn3 route-distinguisher 11:33

Sysname-vpn-instance-vpn3 address-family ipv6

Sysname-vpn-ipv6-vpn3 tnl-policy po1

【相关命令】

·**tunnel-policy**（MPLS命令参考/隧道策略）

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- vpn popgo**

------------------------------------------------------------------------

**[vpn popgo**]命令用来将Egress PE上私网路由的标签操作方式配置为根据标签查找出接口转发。

**[undo** **vpn popgo**]命令用来将Egress PE上私网路由的标签操作方式恢复为根据标签查找FIB转发。

【命令】

**[vpn popgo**]

**[undo vpn popgo**]

【缺省情况】

Egress PE上私网路由的标签操作方式为根据标签查找FIB转发。

【视图】

BGP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置**vpn popgo**命令后，Egress PE会自动断开并重建与私网内BGP邻居之间的会话，重新学习私网路由。

配置**vpn popgo**命令后，Egress PE将报文转发给私网时，不支持在多个私网BGP邻居之间进行BGP负载分担。

【举例】

\# 将Egress PE上私网路由的标签操作方式定制为根据标签查找出接口转发。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp vpn popgo

\# 将Egress PE上私网路由的标签操作方式定制为根据标签查找FIB转发。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp undo vpn popgo

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- vpn-id**

------------------------------------------------------------------------

**[vpn-id**]命令用来配置VPN实例的ID。

**[undo vpn-id**]命令用来删除VPN实例的ID。

【命令】

**[vpn-id ***vpn-id*]

**[undo vpn-id**]

【缺省情况】

没有指定VPN实例的ID。

【视图】

VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-id*]：VPN实例的ID，取值形式为OUI:Index，OUI和Index均为十六进制数。其中，OUI（Organizationally Unique Identifier，全球统一标识符）的取值范围为0\~FFFFFF；Index的取值范围为0\~FFFFFFFF。

【使用指导】

VPN ID是VPN实例的唯一标识，不同VPN实例的VPN ID不能相同。

需要注意的是，VPN ID的取值不能为0:0。

【举例】

\# 配置VPN实例vpn1的ID为20:1。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 vpn-id 20:1

【相关命令】

·**display ip vpn-instance**

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- vpn-instance-capability simple**

------------------------------------------------------------------------

**[vpn-instance-capability simple**]命令用来关闭OSPF实例的路由环路检测功能。

**[undo vpn-instance-capability**]命令用来恢复缺省情况。

【命令】

**[vpn-instance-capability simple**]

**[undo vpn-instance-capability**]

【缺省情况】

OSPF实例的路由环路检测功能处于开启状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

MCE组网环境中，需要在MCE设备上关闭OSPF实例的路由环路检测功能。否则，MCE不会接收PE发送过来的OSPF路由，导致路由丢失。

需要注意的是，只有OSPF进程属于某个VPN时，才能在该进程对应的OSPF视图下成功执行本命令。

【举例】

\# 关闭OSPF实例的路由环路检测功能。

\<Sysname\> system-view

Sysname ospf 100 vpn-instance vpna

Sysname-ospf-100 vpn-instance-capability simple

**MPLS L3VPN \-- MPLS L3VPN配置命令 \-- vpn-target (VPN Instance view/IPv4 VPN view/IPv6 VPN view)**

------------------------------------------------------------------------

**[vpn-target**]命令用来配置当前VPN实例的Route Target。

**[undo vpn-target**]命令用来删除当前VPN实例的Route Target。

【命令】

**[vpn-target*** vpn-target*[&\<1-8\> [ **both** \| **export-extcommunity** \| **import-extcommunity** ]]]

**[undo vpn-target****[{ **all** \| *vpn-target*&\<1-8\> [ **both** \| **export-extcommunity** \| **import-extcommunity** ] }]]

【缺省情况】

没有指定VPN实例的Route Target。

【视图】

VPN实例视图/IPv4 VPN视图/IPv6 VPN视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-target*&\<1-8\>]：指定Route Target值。*vpn-target*为3～21个字符的字符串，取值为AS-number:nn或IP-address:nn。&\<1-8\>表示前面的参数最多可以输入8次。

Route Target有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[both**]：指定配置的Route Target值同时作为Import Target和Export Target。没有指定**both**、**export-extcommunity**和**import-extcommunity**中的任何一个参数时，缺省值为**both**。

**[export-extcommunity**]：指定配置的Route Target值为Export Target。

**[import-extcommunity**]：指定配置的Route Target值为Import Target。

**[all**]：所有Route Target值。

【使用指导】

Route Target用来控制VPN路由的发布。PE在发布的VPN路由中添加Route Target扩展团体属性，该属性的值为配置的Export Target。对端PE接收到VPN路由后，将路由中携带的Route Target属性与本地配置的VPN实例的Import Target进行比较，如果二者中存在相同的值，则将该路由学习到该VPN实例的路由表中。

需要注意的是：

·VPN实例视图下的配置，既可以用于IPv4 VPN，也可以用于IPv6 VPN；IPv4 VPN视图下的配置只能用于IPv4 VPN；IPv6 VPN视图下的配置只能用于IPv6 VPN。

·IPv4 VPN视图、IPv6 VPN视图下的配置优先级高于VPN实例视图下的配置，即如果同时在IPv4 VPN视图（或IPv6 VPN视图）和VPN实例视图下进行了配置，则IPv4 VPN（或IPv6 VPN）采用IPv4 VPN视图（或IPv6 VPN视图）下的配置。

【举例】

\# 为名为vpn1的VPN实例配置Route Target。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 vpn-target 3:3 export-extcommunity

Sysname-vpn-instance-vpn1 vpn-target 4:4 import-extcommunity

Sysname-vpn-instance-vpn1 vpn-target 5:5 both

\# 为名为vpn2的IPv4 VPN配置Route Target。

\<Sysname\> system-view

Sysname ip vpn-instance vpn2

Sysname-vpn-instance-vpn2 address-family ipv4

Sysname-vpn-ipv4-vpn2 vpn-target 3:3 export-extcommunity

Sysname-vpn-ipv4-vpn2 vpn-target 4:4 import-extcommunity

Sysname-vpn-ipv4-vpn2 vpn-target 5:5 both

\# 为名为vpn3的IPv6 VPN配置Route Target。

\<Sysname\> system-view

Sysname ip vpn-instance vpn3

Sysname-vpn-instance-vpn3 address-family ipv6

Sysname-vpn-ipv6-vpn3 vpn-target 3:3 export-extcommunity

Sysname-vpn-ipv6-vpn3 vpn-target 4:4 import-extcommunity

Sysname-vpn-ipv6-vpn3 vpn-target 5:5 both

\

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- address-family ipv6 (VPN instance view)**

------------------------------------------------------------------------

**[address-family ipv6**]命令用来进入IPv6 VPN视图。

**[undo address-family ipv6**]命令用来删除IPv6 VPN视图下的所有配置。

【命令】

**[address-family ipv6**]

**[undo address-family ipv6**]

【视图】

VPN实例视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在IPv6 VPN视图下可以配置IPv6 VPN的参数，如IPv6 VPN应用的出方向路由策略、入方向路由策略等。

【举例】

\# 进入IPv6 VPN视图。

\<Sysname\> system-view

Sysname ip vpn-instance vpn1

Sysname-vpn-instance-vpn1 address-family ipv6

Sysname-vpn-ipv6-vpn1

【相关命令】

·**address-family ipv4 **(VPN instance view)

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- address-family vpnv6**

------------------------------------------------------------------------

**[address-family vpnv6**]命令用来创建BGP VPNv6地址族，并进入BGP VPNv6地址族视图。

**[undo address-family vpnv6**]命令用来删除BGP VPNv6地址族及该视图下的所有配置。

【命令】

**[address-family vpnv6**]

**[undo address-family vpnv6**]

【缺省情况】

没有创建BGP VPNv6地址族。

【视图】

BGP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

VPN-IPv6地址是指在IPv6地址前缀前增加RD后，形成的地址。在IPv6 MPLS L3VPN组网中，PE设备之间需要交换VPN-IPv6地址族的路由信息（即BGP VPNv6路由）。

在PE设备上，进入BGP VPNv6地址族视图，在该视图下通过**peer enable**命令使能BGP对等体（通常为对端PE设备）后，PE才能与该对等体交换BGP VPNv6路由。

在BGP VPNv6地址族视图下，还可以配置BGP-VPNv6路由的属性，例如为从对等体/对等体组接收的BGP-VPNv6路由分配的首选值、是否允许本地AS号在接收的BGP-VPNv6路由的AS_PATH属性中出现等。

【举例】

\# 创建BGP VPNv6地址族，并进入BGP VPNv6地址族视图。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv6

Sysname-bgp-af-vpnv6

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- disable-dn-bit-check**

------------------------------------------------------------------------

**[disable-dn-bit-check**]命令用来忽略OSPFv3 LSA的DN位检查。

**[undo disable-dn-bit-check**]命令用来恢复缺省情况。

【命令】

**[disable-dn-bit-check**]

**[undo disable-dn-bit-check**]

【缺省情况】

PE上需要检查OSPFv3 LSA的DN位。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DN位用于防止路由环路。当PE设备将BGP路由引入OSPFv3，并生成OSPFv3 LSA时，PE为生成的LSA设置DN位。当其他PE设备收到DN位置位的LSA后，在计算路由时忽略该LSA，从而避免再次通过BGP协议发布该路由造成路由环路。

如果PE在路由计算时希望考虑其他PE发布的所有LSA，则可以配置**disable-dn-bit-check**命令，使得PE在计算路由时不检查LSA的DN位，DN位置位的LSA也参与路由计算。

需要注意的是：

·执行**disable-dn-bit-check**命令，可能会导致路由环路，请谨慎使用本命令。

·只有在未配置**vpn-instance-capability simple**命令的OSPFv3多实例进程下执行时，本命令才会生效。

【举例】

\# 配置OSPFv3多实例进程100不检查LSA的DN位。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 disable-dn-bit-check

【相关命令】

·**disable-dn-bit-set**

·**display ospfv3**（三层技术-IP路由命令参考/OSPFv3）

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- disable-dn-bit-set**

------------------------------------------------------------------------

**[disable-dn-bit-set**]命令用来禁止设置OSPFv3 LSA的DN位。

**[undo disable-dn-bit-set**]命令用来恢复缺省情况。

【命令】

**[disable-dn-bit-set**]

**[undo disable-dn-bit-set**]

【缺省情况】

PE上将BGP路由引入OSPFv3，并生成OSPFv3 LSA时，为生成的LSA设置DN位。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

DN位用于防止路由环路。当PE设备将BGP路由引入OSPFv3，并生成OSPFv3 LSA时，PE为生成的LSA设置DN位。当其他PE设备收到DN位置位的LSA后，在计算路由时忽略该LSA，从而避免再次通过BGP协议发布该路由造成路由环路。

如果PE希望其他的PE在路由计算时考虑本PE发布的所有LSA，则可以执行**disable-dn-bit-set**命令，使得本PE在发布LSA时不设置DN位。

需要注意的是：

·执行**disable-dn-bit-set**命令，可能会导致路由环路，请谨慎使用本命令。

·只有在未配置**vpn-instance-capability simple**命令的OSPFv3多实例进程下执行时，本命令才会生效。

【举例】

\# 配置OSPFv3多实例进程100不设置LSA的DN位。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 disable-dn-bit-set

【相关命令】

·**disable-dn-bit-check**

·**display ospfv3**（三层技术-IP路由命令参考/OSPFv3）

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- display bgp routing-table vpnv6**

------------------------------------------------------------------------

**[display bgp routing-table vpnv6**]命令用来显示BGP VPNv6路由信息。

【命令】

**[display bgp routing-table vpnv6 **[ [ **route-distinguisher** *route-distinguisher*   *network-address prefix-length* [ **advertise-info**  \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* }  **whole-match**  \| *adv-community-list-number* } ] \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } [ *network-address* *prefix-length* \| **statistics** ] \| **statistics** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的BGP VPNv6路由信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

*[network-address prefix-l*]*ength*：显示与指定目的网段地址及前缀长度精确匹配的BGP VPNv6路由信息。*network-address*为目的网段的IPv6地址；*prefix-length*为目的网段地址的前缀长度，取值范围为0～128。如果没有指定本参数，则显示所有BGP VPNv6路由信息。

**[advertise-info**]：显示BGP VPNv6路由的通告信息。

**[as-path-acl*** as-path-acl-number*]：显示匹配指定AS路径过滤列表的BGP VPNv6路由信息。*as-path-acl-number*为AS路径过滤列表号，取值范围为1～256。

**[communit-list**]：显示匹配指定BGP团体列表的BGP VPNv6路由信息。

*[basic-community-list-number*]：基本团体列表号，取值范围为1～99。

*[comm-list-name*]：团体属性列表名，为1～63个字符的字符串，区分大小写。

**[whole-match**]：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。

*[adv-community-list-number*]：高级团体列表号，取值范围为100～199。

**[peer**]：显示向指定对等体发布或者从指定对等体收到的BGP VPNv6路由信息。

*[ip-address*]：对等体的IPv4地址。

**[advertised-routes**]：显示向指定的对等体发布的路由信息。

**[received-routes**]：显示从指定的对等体接收到的路由信息。

**[statistics**]：显示BGP VPNv6路由的统计信息。

【举例】

\# 显示所有BGP VPNv6路由的信息。

\<Sysname\> display bgp routing-table vpnv6

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 1

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 4

\* \>  Network : 2001:1::                                 PrefixLen : 96

     NextHop : ::                                       LocPrf    :

     PrefVal : 32768                                    OutLabel  : NULL

     MED     : 0

     Path/Ogn: ?

\*  e Network : 2001:1::                                 PrefixLen : 96

     NextHop : 2001:1::1                                LocPrf    :

     PrefVal : 0                                        OutLabel  : NULL

     MED     : 0

     Path/Ogn: 65410?

\* \>  Network : 2001:1::2                                PrefixLen : 128

     NextHop : ::1                                      LocPrf    :

     PrefVal : 32768                                    OutLabel  : NULL

     MED     : 0

     Path/Ogn: ?

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           LocPrf    : 100

     PrefVal : 0                                        OutLabel  : 1279

     MED     : 0

     Path/Ogn: ?

 Route distinguisher: 200:1

 Total number of routes: 1

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           LocPrf    : 100

     PrefVal : 0                                        OutLabel  : 1279

     MED     : 0

     Path/Ogn: ?

\# 显示匹配AS路径过滤列表1的BGP VPNv6路由信息。

\<Sysname\> display bgp routing-table vpnv6 as-path-acl 1

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 1

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 4

\* \>  Network : 2001:1::                                 PrefixLen : 96

     NextHop : ::                                       LocPrf    :

     PrefVal : 32768                                    OutLabel  : NULL

     MED     : 0

     Path/Ogn: ?

\*  e Network : 2001:1::                                 PrefixLen : 96

     NextHop : 2001:1::1                                LocPrf    :

     PrefVal : 0                                        OutLabel  : NULL

     MED     : 0

     Path/Ogn: 65410?

\* \>  Network : 2001:1::2                                PrefixLen : 128

     NextHop : ::1                                      LocPrf    :

     PrefVal : 32768                                    OutLabel  : NULL

     MED     : 0

     Path/Ogn: ?

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           LocPrf    : 100

     PrefVal : 0                                        OutLabel  : 1279

     MED     : 0

     Path/Ogn: ?

 Route distinguisher: 200:1

 Total number of routes: 1

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           LocPrf    : 100

     PrefVal : 0                                        OutLabel  : 1279

     MED     : 0

     Path/Ogn: ?

\# 显示匹配BGP团体列表100的BGP VPNv6路由信息。

\<Sysname\> display bgp routing-table vpnv6 community-list 100

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 1

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 4

\* \>  Network : 2001:1::                                 PrefixLen : 96

     NextHop : ::                                       LocPrf    :

     PrefVal : 32768                                    OutLabel  : NULL

     MED     : 0

     Path/Ogn: ?

\*  e Network : 2001:1::                                 PrefixLen : 96

     NextHop : 2001:1::1                                LocPrf    :

     PrefVal : 0                                        OutLabel  : NULL

     MED     : 0

     Path/Ogn: 65410?

\* \>  Network : 2001:1::2                                PrefixLen : 128

     NextHop : ::1                                      LocPrf    :

     PrefVal : 32768                                    OutLabel  : NULL

     MED     : 0

     Path/Ogn: ?

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           LocPrf    : 100

     PrefVal : 0                                        OutLabel  : 1279

     MED     : 0

     Path/Ogn: ?

 Route distinguisher: 200:1

 Total number of routes: 1

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           LocPrf    : 100

     PrefVal : 0                                        OutLabel  : 1279

     MED     : 0

     Path/Ogn: ?

\# 显示向对等体3.3.3.9发布的所有公网BGP VPNv6路由信息。

\<Sysname\> display bgp routing-table vpnv6 peer 3.3.3.9 advertised-routes

 Total number of routes: 1

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 100:1

 Total number of routes: 1

\* \>  Network : 2001:1::                                 PrefixLen : 96

     NextHop : ::                                       LocPrf    :

     MED     : 0                                        OutLabel  : NULL

     Path/Ogn: ?

\# 显示从对等体3.3.3.9收到的所有公网BGP VPNv6路由信息。

\<Sysname\> display bgp routing-table vpnv6 peer 3.3.3.9 received-routes

 Total number of routes: 1

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 200:1

 Total number of routes: 1

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           LocPrf    : 100

     PrefVal : 0                                        OutLabel  : 1279

     MED     : 0

     Path/Ogn: ?

表2-1 display bgp routing-table vpnv6命令显示信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Status codes

路由状态值：

·\* - valid：合法路由

·\> - best：普通优选路由

·d - damped：震荡抑制路由

·h - history：历史路由

·i - internal：内部路由

·e - external：外部路由

·s - suppressed：聚合抑制路由

·S - Stale：过期路由

Origin

路由信息的来源，取值包括：

·i -- IGP：表示路由产生于本AS内。通过**network**命令发布路由的路由信息来源为IGP

·e -- EGP：表示路由是通过EGP（Exterior Gateway Protocol，外部网关协议）学到的。

·? -- incomplete：表示路由的来源无法确定。从IGP协议引入路由的路由信息来源为incomplete

Total number of routes from all PEs

来自所有PE设备的VPNv6路由总数

Route distinguisher

路由标识符

Total number of routes

路由的总数

Network

目的网络地址

PrefixLen

目的网络地址的前缀长度

NextHop

下一跳的IPv6地址

LocPrf

本地优先级

PrefVal

路由首选值

OutLabel

路由的出标签值

MED

MED（Multi-Exit Discriminator，多出口区分）属性值

Path/Ogn

路由的AS路径（AS_PATH）属性和路由信息的来源（ORIGIN）属性，其中：

·AS_PATH属性记录了此路由经过的所有AS，可以避免路由环路的出现

·ORIGIN属性标记了此BGP路由如何生成的

\# 显示到达目的网段2001:1::/96的BGP VPNv6路由的通告信息。

\<Sysname\> display bgp routing-table vpnv6 2001:1:: 96 advertise-info

 BGP local router ID: 1.1.1.9

 Local AS number: 100

 Route distinguisher: 100:1

 Total number of routes: 1

 Paths:   1 best

 BGP routing table information of 2001:1::/96:

 Advertised to VPN peers (1 in total):

    3.3.3.9

 Inlabel         : 1279

表2-2 display bgp routing-table vpnv6 advertise-info命令显示信息描述表

字段

描述

BGP local router ID

本地的路由器ID

Local AS number

本地的AS号

Route distinguisher

路由标识符

Total number of routes

路由总数

Paths

到达指定目的网络的优选路由数目

BGP routing table information of 2001:1::/96

到达目的网络2001:1::/96的BGP路由的通告信息

Advertised to VPN peers (1 in total)

该路由已经向哪些VPNv6对等体发送，以及对等体的数目

Inlabel

路由的入标签

\# 显示向对等体3.3.3.9发布的公网BGP VPNv6路由的统计信息。

\<Sysname\> display bgp routing-table vpnv6 peer 3.3.3.9 advertised-routes statistics

 Advertised routes total: 2

\# 显示从对等体3.3.3.9收到的公网BGP VPNv6路由的统计信息。

\<Sysname\> display bgp routing-table vpnv6 peer 3.3.3.9 received-routes statistic

 Received routes total: 2

表2-3 display bgp routing-table vpnv6 peer statistics命令显示信息描述表

字段

描述

Advertised routes total

向指定对等体发布的路由总数

Received routes total

从指定对等体收到的路由总数

\# 显示公网BGP VPNv6路由的统计信息。

\<Sysname\> display bgp routing-table vpnv6 statistics

 Total number of routes from all PEs: 1

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 4

 Route distinguisher: 200:1

 Total number of routes: 1

表2-4 display bgp routing-table vpnv6 statistics命令显示信息描述表

字段

描述

Total number of routes from all PEs

来自所有PE设备的VPNv6路由总数

Route distinguisher

路由标识符

Total number of routes

路由标识符为指定值的VPNv6路由总数

【相关命令】

·**ip as-path**（三层技术-IP路由命令参考/路由策略）

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- display bgp routing-table vpnv6 inlabel**

------------------------------------------------------------------------

**[display bgp routing-table vpnv6 inlabel**]命令用来显示所有BGP VPNv6路由的入标签信息。

【命令】

**[display bgp** **routing-table vpnv6** **inlabel**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有BGP VPNv6路由的入标签信息。

\<Sysname\> display bgp routing-table vpnv6 inlabel

 Total number of routes: 1

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 100:1

 Total number of routes: 1

\* \>  Network : 2001:1::                                 PrefixLen : 96

     NextHop : ::                                       OutLabel  : NULL

     InLabel : 1279

表2-5 display bgp routing-table vpnv6 inlabel命令输出信息描述表

字段

描述

Total number of routes

BGP路由总数

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码，请参见 表1-3(?-98344000#_Ref309652945)

Origin

路由起源代码，请参见 表1-3(?-98344000#_Ref309652945)

Route distinguisher

路由标识符

Total number of routes

路由标识符为指定值的路由总数

Network

目的网络地址

PrefixLen

目的网络地址的前缀长度

NextHop

下一跳IP地址

OutLabel

出标签值，即对端PE为VPNv6路由分配的私网标签

取值为exp-null表示为显式空标签

InLabel

入标签值，即本地PE为VPNv6路由分配的私网标签

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- display bgp routing-table vpnv6 outlabel**

------------------------------------------------------------------------

**[display bgp routing-table vpnv6 outlabel**]命令用来显示所有BGP VPNv6路由的出标签信息。

【命令】

**[display bgp** **routing-table vpnv6** **outlabel**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示所有BGP VPNv6路由的出标签信息。

\<Sysname\> display bgp routing-table vpnv6 outlabel

 BGP local router ID is 1.1.1.9

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Total number of routes from all PEs: 1

 Route distinguisher: 100:1(vpn1)

 Total number of routes: 1

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           OutLabel  : 1279

 Route distinguisher: 200:1

 Total number of routes: 1

\* \>i Network : 2001:3::                                 PrefixLen : 96

     NextHop : ::FFFF:3.3.3.9                           OutLabel  : 1279

表2-6 display bgp routing-table vpnv6 outlabel命令输出信息描述表

字段

描述

BGP local router ID

BGP本地路由器ID

Status codes

路由状态代码，请参见 表1-3(?-98344000#_Ref309652945)

Origin

路由起源代码，请参见 表1-3(?-98344000#_Ref309652945)

Total number of routes from all PEs

来自所有PE设备的路由数

Route distinguisher

路由标识符

Total number of routes

路由标识符为指定值的路由总数

Network

目的网络地址

PrefixLen

目的网络地址的前缀长度

NextHop

下一跳IP地址

OutLabel

出标签值，即对端PE为VPNv6路由分配的私网标签

取值为exp-null表示为显式空标签

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- display ospfv3 sham-link**

------------------------------------------------------------------------

**[display ospfv3 sham-link**]命令用来显示OSPFv3伪连接信息。

【命令】

**[display ospfv3 ** *process-id* ]  **area** *area-id*  **sham-link**  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定OSPFv3进程内的伪连接信息。*process-id*为OSPFv3进程号，取值范围为1～65535。如果不指定本参数，则显示所有OSPFv3进程的伪连接信息。

**[area** *area-id*]：显示指定OSPFv3区域内的伪连接信息。*area-id*为OSPFv3区域号，可以是整数形式，也可以是IPv4地址形式。当是整数形式时，取值范围为0～4294967295。如果不指定本参数，则显示所有OSPFv3区域的伪连接信息。

**[verbose**]：显示伪连接的详细信息。如果不指定本参数，则显示伪连接的概要信息。

【举例】

\# 显示所有OSPFv3伪连接的概要信息。

\<Sysname\> display ospfv3 sham-link

               OSPFv3 Process 1 with Router ID 125.0.0.1

 Sham-link (Area: 0.0.0.1)

 Neighbor ID      State  Instance ID  Destination address

 0.0.0.0          Down   1            1:1::58

 95.0.0.1         P-2-P  1            1:1::95

表2-7 display ospfv3 sham-link命令显示信息描述表

字段

描述

Area

伪连接所属的OSPFv3区域

Neighbor ID

伪连接邻居的Router ID

State

伪连接的接口状态，取值包括Down和P-2-P

Instance ID

伪连接的接口实例ID

Destination address

伪连接的目的地址

\# 显示所有OSPFv3伪连接的详细信息。

\<Sysname\> display ospfv3 sham-link verbose

               OSPFv3 Process 1 with Router ID 125.0.0.1

 Sham-link (Area: 0.0.0.1)

 Source      : 1:1::125

 Destination : 1:1::58

 Interface ID: 2147483649

 Neighbor ID : 0.0.0.0, Neighbor state: Down

 Cost: 1  State: Down  Type: Sham  Instance ID: 1

 Timers: Hello 10, Dead 40, Retransmit 5, Transmit delay 1

 Request list: 0  Retransmit list: 0

 Source      : 1:1::125

 Destination : 1:1::95

 Interface ID: 2147483650

 Neighbor ID : 95.0.0.1, Neighbor state: Full

 Cost: 1  State: P-2-P  Type: Sham  Instance ID: 1

 Timers: Hello 10, Dead 40, Retransmit 5, Transmit delay 1

 Request list: 0  Retransmit list: 0

 IPsec profile name: profile001

表2-8 display ospf sham-link verbose命令显示信息描述表

字段

描述

Area

伪连接所属的OSPFv3区域

Source

伪连接的源地址

Destination

伪连接的目的地址

Interface ID

伪连接的接口索引

Neighbor ID

伪连接邻居的Router ID

Neighbor state

伪连接邻居状态，取值包括Down、Init、2-Way、ExStart、Exchange、Loading和Full

Cost

伪连接的开销

State

伪连接的接口状态，取值包括Down和P-2-P

Type

接口类型，取值固定为Sham，表示为伪连接

Instance ID

伪连接的接口实例ID

Timers

伪连接的定时器，单位为秒，包括Hello，Dead，Retransmit和Transmit Delay定时器

Request list

请求列表中LSA的个数

Retransmit list

重传列表中LSA的个数

IPsec profile name

伪连接引用的IPsec安全框架名

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- domain-id**

------------------------------------------------------------------------

**[domain-id**]命令用来配置OSPFv3域标识符。

**[undo domain-id**]命令用来恢复缺省情况。

【命令】

**[domain-id **[ *domain-id* [ **secondary**  \| **null** }]]

**[undo domain-id **[[ *domain-id* \| **null** ]]]

【缺省情况】]

OSPFv3域标识符为0。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-id*]：OSPFv3域标识符，可以采用以下三种形式：

·整数形式，取值范围为0～4294967295，例如：1；

·点分十进制形式，例如：0.0.0.1；

·点分十进制:16位二进制数，例如：0.0.0.1:512。

**[secondary**]：指定配置的域标识符作为从域标识符。如果不指定本参数，表示配置的域标识符为主域标识符。

**[null**]：指定无域标识符，即团体属性中不携带域标识符。

【使用指导】

如果通过**domain-id**命令配置了OSPFv3域标识符，则PE将OSPFv3路由引入到BGP时，配置的主域标识符被附加到BGP VPNv6路由上作为BGP的扩展团体属性传递给对端PE。对端PE接收到BGP VPNv6路由后，将本地配置的OSPFv3主域标识符、从域标识符和路由中携带的OSPFv3域标识符进行比较：如果主域标识符或从域标识符与路由携带的域标识符相同，且为区域内或区域间路由，则将路由重新引入到OSPFv3时，该路由将作为Inter-Area-Prefix LSA（即Type-3 LSA）向外发布；否则，该路由将作为AS External LSA（即Type-5 LSA）或NSSA External LSA（即Type-7 LSA）向外发布。

需要注意的是：

·如果一端PE的域标识符配置为**null**，另一端PE配置为0，则比较域标识符时，认为二者的域标识符相同。

·主域标识符的值为0时，不能配置从域标识符。

·执行**undo** **domain-id**命令时，如果不指定任何参数，将删除所有域标识符。

·只有在未配置**vpn-instance-capability simple**命令的OSPFv3多实例进程下执行时，本命令才会生效。

【举例】

\# 配置OSPFv3多实例进程100的主域标识符为1.1.1.1。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 domain-id 1.1.1.1

【相关命令】

·**display ospfv3**（三层技术-IP路由命令参考/OSPFv3）

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- ext-community-type**

------------------------------------------------------------------------

**[ext-community-type**]命令用来配置OSPFv3扩展团体属性的类型编码。

**[undo ext-community-type**]命令用来恢复缺省情况。

【命令】

**[ext-community-type ** { **domain-id** *type-code1* \| **route-type** *type-code2* \| **router-id** *type-code3* }]

**[undo ext-community-type ** [ **domain-id** \| **route-type** \| **router-id** ]]

【缺省情况】

OSPFv3扩展团体属性Domain ID的类型编码是0x0005，Route Type的类型编码是0x0306，Router ID的类型编码是0x0107。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[domain-id **]*type-code1*：指定OSPFv3扩展团体属性Domain ID的类型编码。*type-code1*取值可以为十六进制数值0005、0105、0205和8005。

**[route-type **]*type-code2*：指定OSPFv3扩展团体属性Route Type的类型编码。*type-code2*取值可以为十六进制数值0306和8000。

**[router-id**]* type-code3*：指定OSPFv3扩展团体属性Router ID的类型编码。*type-code3*取值可以为十六进制数值0107和8001。

【举例】

\# 配置OSPFv3多实例进程100扩展团体属性Domain ID的类型编码为0x8005，Route Type的类型编码为0x8000，Router ID的类型编码为0x8001。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 ext-community-type domain-id 8005

Sysname-ospfv3-100 ext-community-type route-type 8000

Sysname-ospfv3-100 ext-community-type router-id 8001

【相关命令】

·**display ospfv3**（三层技术-IP路由命令参考/OSPFv3）

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- policy vpn-target**

------------------------------------------------------------------------

**[policy vpn-target**]命令用来对接收到的VPNv6路由使能VPN-Target过滤功能，即只将Export Route Target属性与本地Import Route Target属性匹配的VPNv6路由加入到路由表。

**[undo policy vpn-target**]命令用来取消对VPNv6路由的VPN-Target过滤功能，即接收所有VPNv6路由。

【命令】

**[policy vpn-target**]

**[undo policy vpn-target**]

【缺省情况】

对接收到的VPNv6路由使能VPN-Target过滤功能。

【视图】

BGP VPNv6地址族视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在跨域VPN OptionB组网中，ASBR需要保存所有VPNv6路由信息，以通告给对端ASBR。这种情况下，ASBR上需执行**undo policy vpn-target**命令接收所有的VPNv6路由信息，不对它们进行Route Target过滤。

【举例】

\# 在BGP VPNv6地址族视图下，取消对VPNv6路由的Route Target过滤功能。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv6

Sysname-bgp-af-vpnv6 undo policy vpn-target

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- route-tag**

------------------------------------------------------------------------

**[route-tag**]命令用来配置VPN引入路由的外部路由标记值。

**[undo route-tag**]命令用来恢复缺省情况。

【命令】

**[route-tag** *tag-value*]

**[undo route-tag**]

【缺省情况】

若MPLS骨干网上配置了BGP路由协议，并且BGP的AS号不大于65535，则外部路由标记值的前面两个字节固定为0xD000，后面的两个字节为本端BGP的AS号；否则，外部路由标记值为0。例如，本端BGP AS号为100时，外部路由标记的缺省值为十进制值3489661028，即0xD0000000对应的十进制值（3489660928）+100。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tag-value*]：VPN引入路由的外部路由标记值，取值范围为0～4294967295。

【使用指导】

在CE双归属（CE连接两个PE）、且PE和CE之间采用OSPFv3协议交互私网路由的组网中，外部路由标记可以用来避免路由环路。CE连接的一台PE将从对端PE接收到的BGP VPNv6路由引入OSPFv3，并通过Type-5或Type-7 LSA发布给CE时，为该Type-5或Type-7 LSA添加本地配置的外部路由标记。另一台PE上如果通过**route-tag-check enable**命令使能了OSPFv3 LSA的tag标记检查，则PE接收到CE发布的Type-5或Type-7 LSA后，将其中的外部路由标记值与本地配置的值进行比较。如果相同，则在进行路由计算时忽略该LSA，从而避免路由环路。

外部路由标记值的配置方式及各种方式的优先级为：

·**import-route**命令配置的tag值优先级最高。

·**route-tag**、**default tag**命令配置的tag优先级其次。其中，**route-tag**命令用于PE设备，**default tag**命令用于CE和MCE设备。

需要注意的是：

·同一个区域的PE建议配置相同的外部路由标记值。

·外部路由标记值不会在BGP的扩展团体属性中传递，它只在收到BGP路由并且产生OSPFv3 Type-5或Type-7 LSA的PE路由器上起作用。

·可以为不同的OSPF进程配置相同的外部路由标记值。

·本命令只能在OSPFv3多实例进程下执行，并且只有在未配置**vpn-instance-capability simple**命令的OSPFv3多实例进程下执行时，本命令才会生效。

【举例】

\# 配置OSPFv3多实例进程100的VPN引入路由的外部路由标记值为100。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 route-tag 100

【相关命令】

·**default tag**（三层技术-IP路由命令参考/OSPFv3）

·**display ospfv3**（三层技术-IP路由命令参考/OSPFv3）

·**import-route**（三层技术-IP路由命令参考/OSPFv3）

·**route-tag-check enable**

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- route-tag-check enable**

------------------------------------------------------------------------

**[route-tag-check enable**]命令用来使能OSPFv3 LSA的外部路由标记检查。

**[undo route-tag-check enable**]命令用来恢复缺省情况。

【命令】

**[route-tag-check enable**]

**[undo route-tag-check enable**]

【缺省情况】

不检查OSPFv3 LSA的外部路由标记。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在CE双归属（CE连接两个PE）、且PE和CE之间采用OSPFv3协议交互私网路由的组网中，外部路由标记可以用来避免路由环路。CE连接的一台PE将从对端PE接收到的BGP VPNv6路由引入OSPFv3，并通过Type-5或Type-7 LSA发布给CE时，为该Type-5或Type-7 LSA添加本地配置的外部路由标记。另一台PE上如果通过**route-tag-check enable**命令使能了OSPFv3 LSA的tag标记检查，则PE接收到CE发布的Type-5或Type-7 LSA后，将其中的外部路由标记值与本地配置的值进行比较。如果相同，则在进行路由计算时忽略该LSA，从而避免路由环路。

通常情况下，在上述组网中PE通过DN位来避免路由环路。LSA的外部路由标记检查只是为了兼容不支持DN位的设备。如果网络中不存在这类设备，建议不要配置本命令。

只有在未配置**vpn-instance-capability simple**命令的OSPFv3多实例进程下执行时，本命令才会生效。

【举例】

\# 配置OSPFv3多实例进程100检查LSA的tag标记。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 route-tag-check enable

【相关命令】

·**display ospfv3**（三层技术-IP路由命令参考/OSPFv3）

·**route****-tag**

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- rr-filter**

------------------------------------------------------------------------

**[rr-filter**]命令用来创建路由反射器的反射策略：通过配置路由反射器支持的扩展团体属性号，对接收的路由信息进行过滤，只有接收的VPNv6路由包含指定的扩展团体属性号时，路由反射器才会反射该路由。

**[undo** **rr-filter**]命令用来恢复缺省情况。

【命令】

**[rr-filter ***extended-community-number*]

**[undo rr-filter**]

【缺省情况】

路由反射器不会对反射的路由进行过滤。

【视图】

BGP VPNv6地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[extended-community-number*]：路由反射器支持的扩展团体属性号，取值范围为1～199。

【使用指导】

当一个集群中存在多个路由反射器时，通过在不同的路由反射器上配置不同的反射策略，可以实现路由反射器之间的负载分担。

【举例】

\# 在BGP VPNv6地址族视图下，配置路由反射器支持的扩展团体属性号为10，即该路由反射器只反射包含扩展团体属性10的VPNv6路由。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family vpnv6

Sysname-bgp-vpnv6 rr-filter 10

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- sham-link**

------------------------------------------------------------------------

**[sham-link**]命令用来创建一条OSPFv3伪连接。

**[undo sham-link**]命令用来删除一条已有的OSPFv3伪连接，或者将指定OSPFv3伪连接的参数恢复为缺省值。

【命令】

**[sham-link**[ *source-ipv6-address destination-ipv6-address* [ **cost** *cost* \| **dead** *dead-interval* \| **hello** *hello-interval* \| **instance** *instance-id* \| **ipsec-profile** *profile-name* \| **retransmit** *retrans-interval* \| **trans-delay** *delay* ] \*]]

**[undo sham-link**[ *source-ipv6-address destination-ipv6-address* [ **cost** \| **dead** \| **hello** \| **ipsec-profile** \| **retransmit** \| **trans-delay** ] \*]]

【缺省情况】

设备上不存在任何OSPFv3伪连接。

【视图】

OSPFv3区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-ipv6-address*]：OSPFv3伪连接的源IPv6地址。

*[destination-ipv6-address*]：OSPFv3伪连接的目的IPv6地址。

**[cost*** cost*]：伪连接开销，取值范围为1～65535，缺省值为1。

**[dead ***dead-interval*]：失效时间间隔，取值范围为1～32768，单位为秒，缺省值为*hello-interval*的4倍。建立伪连接的两个路由器上需要配置相同的*dead-interval*，且至少为*hello-interval*的4倍。

**[hello*** hello-interval*]：接口上发送Hello报文的时间间隔，取值范围为1～8192，单位为秒，缺省值为10秒。建立伪连接的两个路由器上需要配置相同的*hello-interval*。

**[instance*** instance-id*]：伪连接的实例ID，取值范围为0～255，缺省值为0。

**[ipsec-profile*** profile-name*]：指定伪连接引用的IPsec安全框架。*profile-name*为IPsec安全框架名称，为1～63个字符的字符串，不区分大小写。

**[retransmit*** retrans-interval*]：接口上重传LSA报文的时间间隔，取值范围是1～3600，单位为秒，缺省值为5秒。

**[trans-delay ***delay*]：接口上延迟发送LSA报文的时间间隔，取值范围为1～3600，单位为秒，缺省值为1秒。

【使用指导】

属于同一个VPN的两个Site之间存在一条区域内OSPFv3链路（backdoor链路）时，为了避免VPN流量总是通过backdoor链路转发而不走骨干网，可以在PE设备之间建立OSPFv3伪连接（sham-link），使经过MPLS VPN骨干网的路由也成为OSPFv3区域内路由，确保VPN流量通过骨干网转发。

【举例】

\# 创建一条OSPFv3伪连接，源地址为1::1，目的地址为2::2。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 area 0

Sysname-ospfv3-100-area-0.0.0.0 sham-link 1::1 2::2

【相关命令】

·**display ospf****v3 sham-link**

**IPv6 MPLS L3VPN \-- IPv6 MPLS L3VPN配置命令 \-- vpn-instance-capability simple**

------------------------------------------------------------------------

**[vpn-instance-capability simple**]命令用来关闭OSPFv3的路由环路检测功能。

**[undo vpn-instance-capability**]命令用来恢复缺省情况。

【命令】

**[vpn-instance-capability simple**]

**[undo vpn-instance-capability**]

【缺省情况】

OSPFv3的路由环路检测功能处于开启状态。

【视图】

OSPFv3视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

MCE组网环境中，需要在MCE设备上关闭OSPFv3的路由环路检测功能。否则，MCE设备不会接收PE设备发送过来的OSPFv3路由，导致路由丢失。

该命令只能在OSPFv3多实例进程下执行。

【举例】

\# 关闭OSPFv3多实例进程100的路由环路检测功能。

\<Sysname\> system-view

Sysname ospfv3 100 vpn-instance vpn1

Sysname-ospfv3-100 vpn-instance-capability simple

