
**组播VPN \-- 组播VPN配置命令 \-- address-family ipv4 mdt**

------------------------------------------------------------------------

**[address-family ipv4 mdt**]命令用来创建BGP IPv4 MDT地址族，并进入BGP IPv4 MDT地址族视图。

**[undo address-family ipv4 mdt**]命令用来删除BGP IPv4 MDT地址族及该视图下的所有配置。

【命令】

**[address-family ipv4 mdt**]

**[undo address-family ipv4 mdt**]

【缺省情况】

没有创建BGP IPv4 MDT地址族。

【视图】

BGP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有创建BGP IPv4 MDT地址族，并在BGP IPv4 MDT地址族下通过**peer** **enable**命令使能BGP MDT对等体/对等体组后，本地路由器才能与指定的对等体/对等体组交换MDT信息，该信息包含PE地址及PE所在的Default-Group等信息。在公网中运行PIM-SSM时，组播VPN根据MDT信息在公网上建立以PE为根（即组播源）的Default-MDT。

BGP IPv4 MDT地址族视图下的配置，只对BGP MDT信息和BGP MDT对等体/对等体组生效。

【举例】

\# 创建BGP IPv4 MDT地址族，并进入BGP IPv4 MDT地址族视图。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family ipv4 mdt

Sysname-bgp-mdt

【相关命令】

·**peer** **enable**（三层技术-IP路由命令参考/BGP）

**组播VPN \-- 组播VPN配置命令 \-- data-delay**

------------------------------------------------------------------------

![说明](组播VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[data-delay**]命令用来配置由Default-MDT向Data-MDT切换的延迟时间。

**[undo data-delay**]命令用来恢复缺省情况。

【命令】

**[data-delay** *delay*]

**[undo data-delay**]

【缺省情况】

由Default-MDT向Data-MDT切换的延迟时间为3秒。

【视图】

MD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：表示延迟时间，取值范围为1～60，单位为秒。

【举例】

\# 配置VPN实例mvpn中由Default-MDT向Data-MDT切换的延迟时间为20秒。

\<Sysname\> system-view

Sysname multicast-domain vpn-instance mvpn

Sysname-md-mvpn data-delay 20

**组播VPN \-- 组播VPN配置命令 \-- data-group**

------------------------------------------------------------------------

![说明](组播VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[data-group**]命令用来配置Data-Group的范围和切换条件。

**[undo** **data-group**]命令用来恢复缺省情况。

【命令】

**[data-group**[ *group-address* { *mask-length* \| *mask* } [ **acl** *acl-number* \| **threshold** *threshold-value* ] \*]]

**[undo** **data-group**]

【缺省情况】

没有指定Data-Group的范围，也永不向Data-MDT进行切换。

【视图】

MD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：表示组播组地址，取值范围为224.0.1.0～239.255.255.255。

*[mask-length*]：表示组播组地址的掩码长度。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

*[mask*]：表示组播组地址的掩码。不同型号的设备支持的取值范围不同，请以设备的实际情况为准

**[acl** *acl-number*]：表示高级ACL的编号，取值范围为3000～3999。本参数用来指定Data-Group作用的（S，G）表项；如果未指定本参数，则作用于所有（S，G）表项。在定义该ACL时，只允许使用**rule**命令中类型为**ip**的**source**和**destination**参数来分别指定S和G。

**[threshold** *threshold-value*]：表示切换阈值，取值范围为0～16777216，单位为kbps，缺省值为0kbps。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

需要注意的是：

·在同一台设备上，Data-Group的范围不能包含任何MD的Default-Group，也不能与其它任何MD的Data-Group范围重叠。

·在不同设备上，如果公网为非PIM-SSM模式，则不同MD不能配置重叠的Data-Group。

·在同一个MD下进行重复配置时，新配置将覆盖旧配置。

·在不支持**threshold** *threshold-value*参数的设备上配置了本命令后，当有满足条件的流量且维持了Data-Delay时间后就发起向Data-MDT的切换。

【举例】

\# 配置VPN实例mvpn中Data-Group的范围为从239.1.2.0到239.1.2.255。

\<Sysname\> system-view

Sysname multicast-domain vpn-instance mvpn

Sysname-md-mvpn data-group 239.1.2.0 24

**组播VPN \-- 组播VPN配置命令 \-- data-holddown**

------------------------------------------------------------------------

![说明](组播VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[data-holddown**]命令用来配置由Data-MDT向Default-MDT反向切换的延迟时间。

**[undo data-holddown**]命令用来恢复缺省情况。

【命令】

**[data-holddown** *delay*]

**[undo data-holddown**]

【缺省情况】

由Data-MDT向Default-MDT反向切换的延迟时间为60秒。

【视图】

MD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：表示延迟时间，取值范围为0～180，单位为秒。

【举例】

\# 配置VPN实例mvpn中由Data-MDT向Default-MDT反向切换的延迟时间为120秒。

\<Sysname\> system-view

Sysname multicast-domain vpn-instance mvpn

Sysname-md-mvpn data-holddown 120

**组播VPN \-- 组播VPN配置命令 \-- default-group**

------------------------------------------------------------------------

**[default-group**]命令用来指定Default-Group。

**[undo default-group**]命令用来恢复缺省情况。

【命令】

**[default-group** *group-address*]

**[undo** **default-group**]

【缺省情况】

没有指定Default-Group。

【视图】

MD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-address*]：表示Default-Group的地址，取值范围为224.0.1.0～239.255.255.255。

【使用指导】

需要注意的是：

·在不同的PE上，应该为相同VPN实例的MD指定相同的Default-Group。

·不允许指定已被其它MD使用的Default-Group或Data-Group。

【举例】

\# 指定VPN实例mvpn的Default-Group为239.1.1.1。

\<Sysname\> system-view

Sysname multicast-domain vpn-instance mvpn

Sysname-md-mvpn default-group 239.1.1.1

**组播VPN \-- 组播VPN配置命令 \-- display bgp routing-table ipv4 mdt**

------------------------------------------------------------------------

**[display bgp routing-table ipv4 mdt**]命令用来显示BGP MDT的路由信息。

【命令】

**[display bgp routing-table ipv4 mdt** [ **route-distinguisher** *route-distinguisher*   *ip-address* [ **advertise-info**  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[route-distinguisher** *route-distinguisher*]：显示指定路由标识符的信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。如果未指定本参数，将显示所有路由标识符的信息。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

*[ip-address*]：显示指定组播源的详细信息。*ip-address*为Default-MDT的组播源地址，即PE设备的地址。如果未指定本参数，将显示所有组播源的简要信息。

**[advertise-info**]：显示通告信息。如果未指定本参数，将不显示通告信息。

【举例】

*[\# *]显示所有组播源的BGP MDT简要路由信息。

\<Sysname\> display bgp routing-table ipv4 mdt

 BGP local router ID is 1.1.1.1

 Status codes: \* - valid, \> - best, d - dampened, h - history,

               s - suppressed, S - stale, i - internal, e - external

               Origin: i - IGP, e - EGP, ? - incomplete

 Route distinguisher: 100:1

 Total number of routes: 2

     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn

\* \>  1.1.1.1/32         0.0.0.0                               32768   ?

\* \>i 2.2.2.2/32         2.2.2.2                    100        0       ?

\# 显示组播源1.1.1.1的BGP MDT详细路由信息。

\<Sysname\> display bgp routing-table ipv4 mdt 1.1.1.1

 BGP local router ID: 1.1.1.1

 Local AS number: 100

 Route distinguisher: 100:1

 Total number of routes: 1

 Paths:   1 available, 1 best

 BGP MDT information of source 1.1.1.1:

 Default-group   : 224.1.1.1

 Original nexthop: 0.0.0.0

 AS-path         : (null)

 Origin          : incomplete

 Attribute value : pref-val 32768

 State           : valid, local, best

\# 显示组播源1.1.1.1的BGP MDT路由的通告信息。

\<Sysname\> display bgp routing-table ipv4 mdt 1.1.1.1 advertise-info

 BGP local router ID: 1.1.1.1

 Local AS number: 100

 Route distinguisher: 100:1

 Total number of routes: 1

 Paths:   1 best

 BGP MDT information of source 1.1.1.1:

 Default-group: 224.1.1.1

 Advertised to peers (1 in total):

     6.6.6.6

表1-1 display bgp routing-table ipv4 mdt命令显示信息描述表

字段

描述

BGP local router ID

本地的路由器编号

Status codes

路由状态代码，包括：

·\* -- valid：表示合法路由

·\> -- best：表示普通优选最佳路由

·d -- damped：表示震荡抑制路由

·h -- history：表示历史路由

·s -- suppressed：表示聚合抑制路由

·S -- Stale：表示过期路由

·i -- internal：表示内部路由

·e -- external：表示外部路由

Origin

信息的来源，包括：

·i -- IGP：表示产生于本AS内。通过**network**命令发布路由的路由信息来源为IGP

·e -- EGP：表示是通过EGP（Exterior Gateway Protocol，外部网关协议）学到的

·? -- incomplete：表示来源无法确定。从IGP协议引入路由的路由信息来源为incomplete

Route distinguisher

路由标识符

Total number of routes

BGP MDT信息的总数

Network

Default-MDT的组播源地址

NextHop

下一跳的IP地址

MED

MED（Multi-Exit-Discriminator，多出口区分）属性值

LocPrf

本地优先级

PrefVal

路由首选值

Path/Ogn

AS路径（AS_PATH）属性和信息的来源（ORIGIN）属性，其中：

·AS_PATH属性记录了此信息经过的所有AS，可以避免环路的出现

·ORIGIN属性标记了此BGP MDT信息是如何生成的

Local AS number

本地的AS号

Paths

BGP MDT信息的数目，其中：

·available：表示有效BGP MDT信息的数目

·best：表示最佳BGP MDT信息的数目

BGP MDT information of source 1.1.1.1

组播源1.1.1.1的BGP MDT信息

Default-group

所属的Default-Group地址

Advertised to peers (1 in total)

该信息已经向哪些对等体发送，以及对等体的数目

From

发布该信息的BGP对等体的IP地址

Original nexthop

原始下一跳地址，如果是从BGP更新消息中获得的信息，则该地址为接收到的消息中的下一跳IP地址

AS-path

AS路径（AS_PATH）属性，记录了此信息经过的所有AS，可以避免环路的出现

Attribute value

BGP MDT信息的属性，包括：

·MED：表示与目的网络关联的MED值

·localpref：表示本地优先级

·pref-val：表示路由首选值

·pre：表示协议优先级

State

当前状态，包括：

·valid：表示有效路由

·internal：表示内部路由

·external：表示外部路由

·local：表示本地产生路由

·synchronize：表示同步路由

·best：表示最佳路由

**组播VPN \-- 组播VPN配置命令 \-- display multicast-domain data-group receive**

------------------------------------------------------------------------

![说明](组播VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display multicast-domain data-group receive**]命令用来显示MD中收到的Data-Group信息。

【命令】

**[display multicast-domain**[ **vpn-instance** *vpn-instance-name* **data-group receive** [ **brief** \| [ **active** \| **group** *group-address* \| **sender** *source-address* \| *vpn-source-address* [ **mask** { *mask-length* \| *mask* } ] \| *vpn-group-address* [ **mask** { *mask-length* \| *mask* } ] ] \* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

**[brief**]：显示简要信息。如果未指定本参数，将显示详细信息。

**[active**]：显示收到的已加入Data-MDT的Data-Group信息。

**[group ***group-address*]：显示与指定公网组播组相关的Data-Group信息，取值范围为224.0.1.0～239.255.255.255。

**[sender ***source-address*]：显示与指定公网组播源相关的Data-Group信息。

*[vpn-source-address*]：显示与指定VPN组播源相关的Data-Group信息。

*[mask-length*]：表示VPN组播源或组播组地址的掩码长度，取值范围为0～32，缺省值为32。

*[mask*]：表示VPN组播源或组播组地址的掩码，缺省值为255.255.255.255。

*[vpn-group-address*]：显示与指定VPN组播组相关的Data-Group信息，取值范围为224.0.0.0～239.255.255.255。

【举例】

\# 显示MD中VPN实例mvpn收到的Data-Group信息。

\<Sysname\> display multicast-domain vpn-instance mvpn data-group receive

MD data-group information received by VPN instance: mvpn

Total 2 data-groups for 8 entries

Total 2 data-groups and 8 entries matched

Data-group: 226.1.1.0   Reference count: 4   Active count: 2

  Sender: 172.100.1.1   Active count: 1

    (192.6.1.5, 239.1.1.1)       expires: 00:03:10 active

    (192.6.1.5, 239.1.1.158)     expires: 00:03:10

  Sender:  181.100.1.1, active count: 1

    (195.6.1.2, 239.1.2.12)      expires: 00:03:10 active

    (195.6.1.2, 239.1.2.197)     expires: 00:03:10

Data-group: 229.1.1.0   Reference count: 4   Active count: 2

  Sender: 185.100.1.1   Active count: 1

    (198.6.1.5, 239.1.3.62)      expires: 00:03:10 active

    (198.6.1.5, 225.1.1.109)     expires: 00:03:10

  Sender: 190.100.1.1   Active count: 1

    (200.6.1.2, 225.1.4.80)      expires: 00:03:10 active

    (200.6.1.2, 225.1.4.173)     expires: 00:03:10

\# 显示MD中VPN实例mvpn收到的Data-Group简要信息。

\<Sysname\> display multicast-domain vpn-instance mvpn data-group receive brief

MD data-group information received by VPN instance: mvpn

Total 2 data-groups for 8 entries

Total 2 data-groups and 8 entries matched

Data group: 226.1.1.0   Reference count: 4   Active count: 2

Data group: 229.1.1.0   Reference count: 4   Active count: 2

表1-2 display multicast-domain data-group receive命令显示信息描述表

字段

描述

MD data-group information received by VPN instance: mvpn

VPN实例mvpn收到的Data-Group信息

Total 2 data-groups for 8 entries

总共有2个Data-Group，对应着8个（S，G）表项

Total 2 data-groups and 8 entries matched

总共匹配了2个Data-Group和8个（S，G）表项

Data-group

收到的Data-Group地址

Sender

发送Data-Group信息的PE的BGP对等体地址

Reference count

Data-Group引用的私网组播表项数量

Active count

Data-Group引用的活跃私网组播表项（即存在接收者的组播组）数量

expires

Data-Group引用的私网组播（S，G）表项的超时时间

**组播VPN \-- 组播VPN配置命令 \-- display multicast-domain data-group send**

------------------------------------------------------------------------

![说明](组播VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display multicast-domain data-group send**]命令用来显示MD中发送的Data-Group信息。

【命令】

**[display multicast-domain**[ **vpn-instance** *vpn-instance-name* **data-group** **send** [ **group** *group-address* \| **reuse** *interval* \| *vpn-source-address* [ **mask** { *mask-length* \| *mask* } ] \| *vpn-group-address* [ **mask** { *mask-length* \| *mask* } ] ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

**[group ***group-address*]：显示与指定组播组相关的Data-Group信息，取值范围为224.0.1.0～239.255.255.255。

**[reuse** *interval*]：显示MD在指定时间段内发生重用的Data-Group信息，取值范围为1～2147483647，单位为秒。

*[vpn-source-address*]：显示与指定VPN组播源相关的Data-Group信息。

*[mask-length*]：表示VPN组播源或组播组地址的掩码长度，取值范围为0～32，缺省值为32。

*[mask*]：表示VPN组播源或组播组地址的掩码，缺省值为255.255.255.255。

*[vpn-group-address*]：显示与指定VPN组播组相关的Data-Group信息，取值范围为224.0.0.0～239.255.255.255。

【举例】

\# 显示MD中VPN实例mvpn发送的Data-Group信息。

\<Sysname\> display multicast-domain vpn-instance mvpn data-group send

MD data-group information sent by VPN instance: mvpn

Total 2 data-groups for 6 entries

Total 2 data-groups and 6 entries matched

  Reference count of 226.1.1.0: 3

    (192.6.1.5, 239.1.1.1)                  switch time: 00:00:21

    (192.6.1.5, 239.1.1.158)                switch time: 00:00:21

    (192.6.1.5, 239.1.2.50)                 switch time: 00:00:05

  Reference count of 226.1.1.1: 3

    (192.6.1.2, 225.1.1.1)                  switch time: 00:00:21

    (192.6.1.2, 225.1.2.50)                 switch time: 00:00:05

    (192.6.1.5, 239.1.1.159)                switch time: 00:00:21

\# 显示MD中VPN实例mvpn在30秒内发送的Data-Group的重用信息。

\<Sysname\> display multicast-domain vpn-instance mvpn data-group send reuse 30

MD data-group information sent by VPN instance: mvpn

Total 2 data-groups for 3 entries

Total 2 data-groups and 3 entries matched

  Reuse count of 226.1.1.0: 1

  Reuse count of 226.1.1.1: 1

  Reuse count of 226.1.1.2: 1

表1-3 display multicast-domain data-group send命令显示信息描述表

字段

描述

MD data-group information sent by VPN instance: mvpn

VPN实例mvpn发送的Data-Group信息

Total 2 data-groups for 6 entries

总共有2个Data-Group，对应着6个（S，G）表项

Total 2 data-groups and 6 entries matched

总共匹配了2个Data-Group和6个（S，G）表项

Reference count of 226.1.1.0

发送的Data-Group引用的私网组播组数量

switch time

Data-Group引用的私网组播（S，G）表项的切换时间

Reuse count of 226.1.1.0

发送的Data-Group在指定时间段内的重用数量

**组播VPN \-- 组播VPN配置命令 \-- display multicast-domain default-group**

------------------------------------------------------------------------

**[display multicast-domain** **default-group**]命令用来显示Default-Group的信息。

【命令】

**[display multicast-domain** [ **vpn-instance** *vpn-instance-name*  **default-group** { **local** \| **remote** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有VPN实例的信息。

**[local**]：显示本地Default-Group的信息。

**[remote**]：显示远端Default-Group的信息。

【举例】

\# 显示所有VPN实例中本地Default-Group的信息。

\<Sysname\> display multicast-domain default-group local

MD local default-group information:

 Group address    Source address   Interface     VPN instance

 239.1.1.1        1.1.1.1          MTunnel0      mvpna

 239.2.1.1        1.1.1.1          MTunnel1      mvpnb

 239.3.1.1        \--               MTunnel2      mvpnc

\# 显示所有VPN实例中远端Default-Group的信息。

\<Sysname\> display multicast-domain default-group remote

MD remote default-group information:

 Group address   Source address  Next hop         VPN instance

 239.1.1.1       1.2.0.1         1.2.0.1          a

 239.1.1.1       1.2.0.2         1.2.0.2          a

 239.1.1.1       1.2.0.3         1.2.0.3          a

 239.1.1.2       1.2.0.1         1.2.0.1          b

 239.1.1.2       1.2.0.2         1.2.0.2          b

 239.1.1.3       1.2.0.1         1.2.0.1          -

表1-4 display multicast-domain default-group命令显示信息描述表

字段

描述

Group address

Default-Group的地址

Source address

MTI封装私网组播报文时使用的源地址，即MD源接口的IP地址

Interface

MTI的名称

Next hop

下一跳地址

VPN instance

所属VPN实例的名称

**组播VPN \-- 组播VPN配置命令 \-- log data-group-reuse**

------------------------------------------------------------------------

![说明](组播VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[log** **data-group-reuse**]命令用来打开Data-Group重用日志输出开关。

**[undo log data-group-reuse**]命令用来关闭Data-Group重用日志输出开关。

【命令】

**[log** **data-group-reuse**]

**[undo** **log** **data-group-reuse**]

【缺省情况】

Data-Group重用日志输出开关处于关闭状态。

【视图】

MD视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 打开VPN实例mvpn中的Data-Group重用日志输出开关。

\<Sysname\> system-view

Sysname multicast-domain vpn-instance mvpn

Sysname-md-mvpn log data-group-reuse

**组播VPN \-- 组播VPN配置命令 \-- multicast-domain**

------------------------------------------------------------------------

**[multicast-domain**]命令用来创建指定VPN实例的MD，并进入MD视图。

**[undo multicast-domain**]命令用来清除指定VPN实例MD视图下的配置。

【命令】

**[multicast-domain** **vpn-instance** *vpn-instance-name*]

**[undo** **multicast-domain** **vpn-instance** *vpn-instance-name*]

【缺省情况】

VPN实例不存在对应的MD。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：表示VPN实例。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。

【举例】

\# 创建VPN实例mvpn的MD，并进入MD视图。

\<Sysname\> system-view

Sysname multicast-domain vpn-instance mvpn

Sysname-md-mvpn

**组播VPN \-- 组播VPN配置命令 \-- multicast rpf-proxy-vector compatible**

------------------------------------------------------------------------

【命令】

**[multicast rpf-proxy-vector compatible**]命令用来使能RPF代理向量兼容功能。

**[undo multicast rpf-proxy-vector compatible**]命令用来关闭RPF代理向量兼容功能。

【命令】

**[multicast rpf-proxy-vector compatible**]

**[undo multicast rpf-proxy-vector compatible**]

【缺省情况】

RPF代理向量兼容功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在配置B类跨AS的MD VPN时，如果要与某些厂商的设备互通，则必须在公网中的所有H3C设备上都使能RPF代理向量兼容功能。

【举例】

\# 使能RPF代理向量兼容功能。

\<Sysname\> system-view

Sysname multicast rpf-proxy-vector compatible

**组播VPN \-- 组播VPN配置命令 \-- rpf proxy vector**

------------------------------------------------------------------------

**[rpf proxy vector**]命令用来使能RPF代理向量功能。

**[undo rpf proxy vector**]命令用来关闭RPF代理向量功能。

【命令】

**[rpf proxy vector**]

**[undo rpf proxy vector**]

【缺省情况】

RPF代理向量功能处于关闭状态。

【视图】

MRIB视图

【缺省用户角色】

network-admin

network-operator

【使用指导】

在配置B类跨AS的MD VPN时，必须在PE（不连接组播接收者的PE除外）上使能RPF代理向量功能，从而使PE发送的PIM加入报文可携带用于进行RPF检查的RPF代理向量信息，以创建正确的公网Default-MDT。

需要注意的是，本命令只在VPN实例MRIB视图下生效。公网实例MRIB视图下虽可配置本命令，但不会生效。

【举例】

\# 在VPN实例mvpn中使能RPF代理向量功能。

\<Sysname\> system-view

Sysname multicast routing vpn-instance mvpn

Sysname-mrib-mvpn rpf proxy vector

**组播VPN \-- 组播VPN配置命令 \-- source**

------------------------------------------------------------------------

**[source**]命令用来指定MD源接口。

**[undo** **source**]命令用来恢复缺省情况。

【命令】

**[source** *interface-type* *interface-number*]

**[undo** **source**]

【缺省情况】

没有指定MD源接口。

【视图】

MD视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type* *interface-number*]：表示接口类型和接口编号。

【使用指导】

需要注意的是，MD源接口必须与建立BGP对等体时所使用的源接口相同，否则将无法获取正确的路由信息。

【举例】

\# 假设建立BGP对等体时所使用的源接口为LoopBack1接口，指定该接口为VPN实例mvpn的MD源接口。

\<Sysname\> system-view

Sysname multicast-domain vpn-instance mvpn

Sysname-md-mvpn source loopback 1
