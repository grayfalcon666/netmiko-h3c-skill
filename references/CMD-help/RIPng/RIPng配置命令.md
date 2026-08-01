<!-- CMD-INDEX
  checkzero                           | RIPng视图          | L37
  default cost                        | RIPng视图          | L79
  display ripng                       | 任意视图             | L129
  display ripng database              | 任意视图             | L243
  display ripng graceful-restart      | 任意视图             | L313
  display ripng interface             | 任意视图             | L387
  display ripng neighbor              | 任意视图             | L481
  display ripng non-stop-routing      | 任意视图             | L539
  display ripng route                 | 任意视图             | L607
  enable ipsec-profile                | RIPng视图          | L787
  filter-policy export                | RIPng视图          | L837
  filter-policy import                | RIPng视图          | L909
  graceful-restart                    | RIPng视图          | L973
  graceful-restart interval           | RIPng视图          | L1019
  import-route                        | RIPng视图          | L1061
  maximum load-balancing              | RIPng视图          | L1117
  non-stop-routing                    | RIPng视图          | L1169
  output-delay                        | RIPng视图          | L1211
  preference                          | RIPng视图          | L1263
  reset ripng process                 | 用户视图             | L1315
  reset ripng statistics              | 用户视图             | L1351
  ripng                               | 系统视图             | L1385
  ripng default-route                 | 接口视图             | L1435
  ripng enable                        | 接口视图             | L1517
  ripng ipsec-profile                 | 接口视图             | L1571
  ripng metricin                      | 接口视图             | L1633
  ripng metricout                     | 接口视图             | L1687
  ripng output-delay                  | 接口视图             | L1741
  ripng poison-reverse                | 接口视图             | L1805
  ripng split-horizon                 | 接口视图             | L1855
  ripng summary-address               | 接口视图             | L1915
  timer triggered                     | RIPng视图          | L1979
  timers                              | RIPng视图          | L2031
-->

**RIPng \-- RIPng配置命令 \-- checkzero**

------------------------------------------------------------------------

**[checkzero**]命令用来使能RIPng报文的零域检查功能。

**[undo**] **checkzero**命令用来关闭零域检查功能。

【命令】

**[checkzero**]

**[undo checkzero**]

【缺省情况】

RIPng报文的零域检查功能处于使能状态。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RIPng报文头部中的一些字段必须配置为0，也称为零域。使能RIPng报文的零域检查后，如果报文头部零域中的值不为零，这些报文将被丢弃，不做处理。

【举例】

\# 关闭进程号为100的RIPng进程对RIPng报文的零域检查功能。

\<Sysname\> system-view

Sysname ripng 100

Sysname-ripng-100 undo checkzero

**RIPng \-- RIPng配置命令 \-- default cost**

------------------------------------------------------------------------

**[default cost**]命令用来配置引入路由的缺省度量值。

**[undo default cost**]命令用来恢复缺省情况。

【命令】

**[default cost ***value*]

**[undo default cost**]

【缺省情况】

引入路由的缺省度量值为0。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：引入路由的缺省度量值，取值范围为0～16。

【使用指导】

当使用**import-route**命令从其它协议引入路由时，如果不指定具体的度量值，则引入路由的度量值为**default cost**所指定的值。

【举例】

\# 配置引入路由的缺省度量值为2。

\<Sysname\> system-view

Sysname ripng 100

Sysname-ripng-100 default cost 2

【相关命令】

·**import-route**

**RIPng \-- RIPng配置命令 \-- display ripng**

------------------------------------------------------------------------

**[display ripng**]命令用来显示指定RIPng进程的当前运行状态及配置信息。

【命令】

**[display ripng** [ *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。如果未指定本参数，则显示所有已配置的RIPng进程的信息。

【举例】

\# 显示所有已配置的RIPng进程的当前运行状态及配置信息。

\<Sysname\> display ripng

  Public VPN-instance name:

    RIPng process: 1

       Preference: 100

           Routing policy: abc

       Checkzero: Enabled

       Default cost: 0

       Maximum number of load balanced routes: 6

       Update time   :   30 secs  Timeout time         :  180 secs

       Suppress time :  120 secs  Garbage-collect time :  120 secs

       Number of periodic updates sent: 256

       Number of trigger updates sent: 1

表1-1 display ripng命令显示信息描述表

字段

描述

Public VPN-instance name/Private VPN-instance name

RIPng进程运行在公网实例下/RIPng进程应用于指定VPN实例

RIPng Process

RIPng进程号

Preference

RIPng路由优先级

Routing policy

路由策略

Checkzero

RIPng报文头部的零域检查功能：Enabled表示使能，Disabled表示未使能

Default cost

引入路由的缺省度量值

Maximum number of load balanced routes

等价路由的最大数目

Update time

Update定时器的值，单位为秒

Timeout time

Timeout定时器的值，单位为秒

Suppress time

Suppress定时器的值，单位为秒

Garbage-collect time

Garbage-Collect定时器的值，单位为秒

Number of periodic updates sent

定时发送的RIPng更新报文的统计数量

Number of trigger updates sent

触发发送的RIPng更新报文的统计数量

**RIPng \-- RIPng配置命令 \-- display ripng database**

------------------------------------------------------------------------

**[display ripng database**]命令用来显示指定RIPng进程发布数据库的所有激活路由。这些路由以常规RIPng更新报文的形式发送。

【命令】

**[display ripng** *process-id* **database** [ *ipv6-address prefix-length* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

*[ipv6-address******prefix-length*]：显示指定IPv6地址的激活路由信息。*ipv6-address*表示IPv6地址；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。

【举例】

\# 显示进程号为1的RIPng进程发布数据库中的激活路由。

\<Sysname\> display ripng 1 database

   1::/64,

        cost 0, RIPng-interface

   10::/32,

        cost 0, imported

   2::2/128,

       via FE80::20C:29FF:FE7A:E3E4, cost 1

表1-2 display ripng database命令显示信息描述表

字段

描述

cost

度量值

RIPng-interface

从使能RIPng协议的接口学来的路由

imported

表示该条路由是从其它路由协议引入的

via

下一跳IPv6地址

**RIPng \-- RIPng配置命令 \-- display ripng graceful-restart**

------------------------------------------------------------------------

**[display ripng** **graceful-restart**]命令用来显示RIPng进程的GR状态信息。

【命令】

**[display ripng ** *process-id* ] **graceful-restart**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【举例】

\# 显示RIPng 1进程的GR状态信息。

\<Sysname\> display ripng 1 graceful-restart

RIPng process: 1

 Graceful Restart capability    : Enabled

 Current GR state               : Normal

 Graceful Restart period        : 60  seconds

 Graceful Restart remaining time: 0   seconds

表1-3 display ripng graceful-restart命令显示信息描述表

字段

描述

Graceful Restart capability

GR使能状态

·Enabled：使能了GR能力

·Disabled：关闭了GR能力

Current GR state

当前GR所处状态

·Under GR：进程正在GR

·Normal：普通状态

Graceful Restart period

GR间隔

Graceful Restart remaining time

GR结束剩余时间

**RIPng \-- RIPng配置命令 \-- display ripng interface**

------------------------------------------------------------------------

**[display ripng interface**]命令用来显示指定RIPng进程的接口信息。

【命令】

**[display ripng ***process-id* **interface** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，则显示指定RIPng进程的所有接口信息。

【举例】

\# 显示RIPng进程1的接口信息。

\<Sysname\> display ripng 1 interface

 Interface: GigabitEthernet1/0/2

         Link-local address: FE80::20C:29FF:FEC8:B4DD

         Split-horizon: On                Poison-reverse: Off

         MetricIn: 0                      MetricOut: 1

         Default route: Off

         Summary address:

                1::/16

表1-4 display ripng interface命令显示信息描述表

字段

意义

Interface

运行RIPng协议的接口的名称

Link-local address

运行RIPng协议的接口的链路本地地址

Split-horizon

是否使能了水平分割（On表示使能，Off表示关闭）

Poison-reverse

是否使能了毒性逆转（On表示使能，Off表示关闭）

MetricIn/MetricOut

接收/发送路由时添加的附加度量值

Default route

是否配置了发布缺省路由以及发布缺省路由的模式/取消发布缺省路由/缺省路由处于garbage-collect时间：

·配置了发布缺省路由：此时从接口发布缺省路由的模式有两种Only/Originate。Only表示从接口只发布缺省路由，Originate表示同时发布缺省路由和其他RIPng路由。处于这种状态时，路由器相应的显示：Default route: Only，或者Default route: Originate

·取消发布缺省路由：表示当前没有配置发布缺省路由或者是取消发布默认路由后garbage-collect已经超时，此时接口不发送RIPng的缺省路由。处于这种状态时，路由器显示：Default route: Off

·缺省路由正处于garbage-collect时间：取消发布缺省路由配置后，缺省路由会进入garbage-collect状态，此时从接口发送metric为16的缺省路由。处于这种状态时，路由器显示：Default route: In garbage-collection status (*x*s)

Default route cost

RIPng接口下配置发布缺省路由的cost值

Summary address

在接口配置的聚合的IPv6地址以及被聚合的路由的IPv6前缀

**RIPng \-- RIPng配置命令 \-- display ripng neighbor**

------------------------------------------------------------------------

**[display ripng neighbor**]命令用来显示RIPng进程的邻居信息。

【命令】

**[display ripng ***process-id*** neighbor** [ *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示RIPng的所有邻居信息。

【举例】

\# 显示RIPng进程1的邻居信息。

\<Sysname\> display ripng 1 neighbor

Neighbor Address: FE80::230:FF:FE00:0

     Interface  : Vlan-interface1

     Version    : RIPng version 1     Last update: 00h00m27s

     Bad packets: 0                   Bad routes : 0

表1-5 display ripng neighbor命令显示信息描述表

字段

描述

Version

收到邻居RIPng报文的版本

Last update

上次收到邻居更新报文距离现在时间

**RIPng \-- RIPng配置命令 \-- display ripng non-stop-routing**

------------------------------------------------------------------------

**[display ripng** **non-stop-routing**]命令用来显示RIPng进程的NSR状态信息。

【命令】

**[display ripng** [ *process-id*  **non-stop-routing**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【举例】

\# 显示RIPng 1进程的NSR状态信息。

\<Sysname\> display ripng 1 non-stop-routing

RIPng process: 1

 Nonstop Routing capability: Enabled

 Current NSR state         : Finish

表1-6 display ripng non-stop-routing命令显示信息描述表

字段

描述

Nonstop Routing capability

NSR使能状态：

·Enabled：使能NSR

·Disabled：不使能NSR

Current NSR state

当前NSR所处状态：

·Initialization：初始准备

·Smooth：数据平滑

·Advertising：发布路由

·Redistribution：路由引入处理

·Finish：完成

**RIPng \-- RIPng配置命令 \-- display ripng route**

------------------------------------------------------------------------

**[display ripng route**]命令用来显示指定RIPng进程的路由信息。

【命令】

**[display ripng ***process-id*** route **[ *ipv6-address* *prefix-length* [ **verbose**  \| **peer** *ipv6-address* \| **statistics** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

*[ipv6-address prefix-length*]：显示指定IPv6地址的路由信息。*ipv6-address*表示IPv6地址；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。

**[verbose**]：显示当前RIPng路由表中的指定前缀路由的所有路由信息。如果未指定本参数，则只显示指定IPv6目的地址和前缀的最优RIPng路由。

**[peer ***ipv6-address*]：显示从指定邻居学到的所有路由信息。

**[statistics**]：显示路由的统计信息。路由的统计信息包括路由总数目，各个邻居的路由数目。

【举例】

\# 显示进程号为1的RIPng进程的路由信息。

\<Sysname\> display ripng 1 route

   Route Flags: A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct

                O - Optimal, F - Flush to RIB

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Peer FE80::20C:29FF:FED4:7171 on GigabitEthernet1/0/2

 Destination 4::4/128,

     via FE80::20C:29FF:FED4:7171, cost 1, tag 0, AOF, 5 secs

 Local route

 Destination 3::3/128,

     via ::, cost 0, tag 0, DOF

 Destination 6::/64,

     via ::, cost 0, tag 0, DOF

\# 显示进程号为1的RIPng进程中指定地址3::3/128的所有路由信息。

\<Sysname\> display ripng 1 route 3::3 128 verbose

   Route Flags: A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct

                O - Optimal, F - Flush to RIB

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 Local route

 Destination 3::3/128,

     via ::, cost 0, tag 0, DOF

表1-7 display ripng route命令显示信息描述表

字段

描述

A - Aging

此路由项处于老化状态

S - Suppressed

此路由项处于抑制状态

G - Garbage-collect

此路由项处于Garbage-collect状态

D - Direct

此路由项是RIPng生成的直连路由

Local route

RIPng本地生成的直连路由

O - Optimal

此路由项处于最优路由状态

F - Flush to RIB

此路由项已经被下刷到RIB

Peer

与接口相连的邻居

Destination

目的IPv6地址

via

下一跳IPv6地址

cost

度量值

tag

路由标签

secs

此路由项处于某种状态的时间

\# 显示进程号为1的RIPng进程路由信息的统计计数。

\<Sysname\> display ripng 1 route statistics

 Peer                                            Optimal/Aging    Garbage

 FE80::20C:29FF:FED4:7171                        1/2              0

 Local                                           2/0              0

 total                                           3/2              0

表1-8 display ripng route statistics命令显示信息描述表

字段

描述

Peer

RIPng邻居IPv6地址

Optimal

路由信息中处于最优路由状态的路由条数

Aging

路由信息中处于老化状态的路由条数

Garbage

路由信息中处于Garbage-collection状态的路由条数

Local

RIPng本地生成的直连路由条数的总和

total

从所有RIPng邻居学习到的路由条数的总和

**RIPng \-- RIPng配置命令 \-- enable ipsec-profile**

------------------------------------------------------------------------

![说明](RIPng命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[enable ipsec-profile**]命令用来在RIPng进程应用IPsec安全框架。

**[undo enable ipsec-profile**]命令用来取消在RIPng进程应用的IPsec安全框架。

【命令】

**[enable ipsec-profile ***profile-name*]

**[undo enable ipsec-profile**]

【缺省情况】

RIPng没有应用IPsec安全框架。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：安全框架名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

本命令应结合IPsec安全框架使用，IPsec安全框架的具体情况请参见"安全配置指导"中的"IPsec"。

【举例】

\# 配置RIPng进程1的IPsec安全框架为profile001。

\<Sysname\> system-view

Sysname ripng 1

Sysname-ripng-1 enable ipsec-profile profile001

**RIPng \-- RIPng配置命令 \-- filter-policy export**

------------------------------------------------------------------------

**[filter-policy export**]命令用来配置RIPng输出路由过滤策略，只有通过过滤的路由才能通过更新报文发布出去。

**[undo filter-policy** **export**]命令用来取消输出路由过滤策略。

【命令】

**[filter-policy **[{ *acl6-number* \| **prefix-list** *prefix-list-name* } **export** [ *protocol* [ *process-id* ] ]]]

**[undo filter-policy** **export** [ *protocol* [ *process-id*  ]]]

【缺省情况】

RIPng不对发布的路由信息进行过滤。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定的IPv6基本或高级访问控制列表，用于对发布的路由信息进行过滤，取值范围为2000～3999。

**[prefix-list** *prefix-list-name*]：指定用于过滤发布路由信息的IPv6地址前缀列表名称。*prefix-list-name*为1～63个字符的字符串。

*[protocol*]：被过滤路由信息的路由协议。目前可选择bgp4+、direct、isisv6、ospfv3、ripng、static。

*[process-id*]：被过滤路由信息的路由协议的进程号，取值范围为1～65535。仅当路由协议为ripng、ospfv3、isisv6时需要指定进程号，若未指定，缺省进程号为1。

【使用指导】

·如果指定*protocol*参数，则只对从指定路由协议引入的路由信息进行过滤；否则将对所有要发布的路由信息进行过滤。

·当配置的是高级ACL（3000～3999）时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]来过滤指定目的地址和前缀的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。

【举例】

\# 用地址前缀列表过滤发布的RIPng更新报文。

\<Sysname\> system-view

Sysname ipv6 prefix-list abc index 10 permit 100:1:: 32

Sysname ripng 100

Sysname-ripng-100 filter-policy prefix-list abc export

\# 用编号为3000的IPv6高级ACL对发布的路由进行过滤，只允许2001::1/128通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128

Sysname-acl-ipv6-adv-3000 rule 100 deny ipv6

Sysname-acl-ipv6-adv-3000 quit

Sysname ripng 100

Sysname-ripng-100 filter-policy 3000 export

**RIPng \-- RIPng配置命令 \-- filter-policy import**

------------------------------------------------------------------------

**[filter-policy import**]命令用来对接收的路由信息进行过滤，符合过滤条件的路由才能被接收。**undo filter-policy** **import**命令用来取消对接收的路由信息进行过滤。

【命令】

**[filter-policy**[ { *acl6-number* \| **prefix-list** *prefix-list-name* } **import**]]

**[undo filter-policy** **import**]

【缺省情况】

RIPng不对接收的路由信息进行过滤。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：用于过滤接收的路由信息的访问控制列表号，取值范围为2000～3999。

**[prefix-list** *prefix-list-name*]：指定用于过滤接收路由信息的IPv6地址前缀列表名称。*prefix-list-name*为1～63个字符的字符串。

【使用指导】

当配置的是高级ACL（3000～3999）时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]来过滤指定目的地址和前缀的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。

【举例】

\# 用地址前缀列表过滤收到的RIPng更新报文。

\<Sysname\> system-view

Sysname ipv6 prefix-list abc index 10 permit 100:1:: 32

Sysname ripng 100

Sysname-ripng-100 filter-policy prefix-list abc import

\# 使用编号为3000的IPv6高级ACL对接收的路由进行过滤，只允许2001::1/128通过。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128

Sysname-acl-ipv6-adv-3000 rule 100 deny ipv6

Sysname-acl-ipv6-adv-3000 quit

Sysname ripng 100

Sysname-ripng-100 filter-policy 3000 import

**RIPng \-- RIPng配置命令 \-- graceful-restart**

------------------------------------------------------------------------

![说明](RIPng命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart**]命令用来使能RIPng协议的GR能力。

**[undo graceful-restart**]命令用来关闭RIPng协议的GR能力。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

RIPng协议的GR能力处于关闭状态。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RIPng GR特性与RIPng NSR特性互斥，即**graceful-restart**和**non-stop-routing**命令互斥，不能同时配置。

【举例】

\# 使能RIPng进程1的GR能力。

\<Sysname\> system-view

Sysname ripng 1

Sysname-ripng-1 graceful-restart

**RIPng \-- RIPng配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

**[graceful-restart interval**]命令用来配置RIPng协议的GR重启间隔时间。

**[undo graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[graceful-restart interval ***interval-value*]

**[undo graceful-restart interval**]

【缺省情况】

RIPng协议的GR重启间隔时间为60秒。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：指定Restarter路由器平滑重启的时长，取值范围是5～360，单位是秒。

【举例】

\# 配置RIPng进程1平滑重启间隔。

\<Sysname\> system-view

Sysname ripng 1

Sysname-ripng-1 graceful-restart interval 200

**RIPng \-- RIPng配置命令 \-- import-route**

------------------------------------------------------------------------

**[import-route**]命令用来从其它路由协议引入路由。

**[undo import-route**]命令用来取消引入外部路由信息。

【命令】

**[import-route** *protocol* [ *process-id*   **allow-ibgp**  [ **allow-direct** \| **cost** *cost* \| **route-policy** *route-policy-name* ] \*]]

**[undo import-route** *protocol* [ *process-id* ]]

【缺省情况】

RIPng不引入其它路由。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：指定要引入的路由协议，可以是bgp4+、direct、isisv6、ospfv3、ripng或static。

*[process-id*]：路由协议进程号，取值范围为1～65535，缺省值为1。只有当protocol是isisv6、ospfv3或ripng时该参数可选。

**[allow-ibgp**]：当*protocol*为bgp4+时，**allow-ibgp**为可选关键字。

**[allow-direct**]：在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入协议路由时不会包含使能了该协议的接口网段路由。当**allow-direct**与**route-policy** *route-policy-name*参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致**allow-direct**配置失效。例如，当配置**allow-direct**参数引入OSPFv3直连时，在路由策略中不要配置**if-match** **route-type**匹配条件，否则，**allow-direct**参数失效。

**[cost*** cost*]：所要引入路由的度量值，取值范围为0～16。如果没有指定度量值，则使用缺省度量值0。

**[route-policy**]* route-policy-name*：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

**[import-route bgp4+**]表示只引入EBGP路由，**import-route bgp4+ allow-ibgp**表示也将IBGP路由引入，容易引起路由环路，请慎用。

【举例】

\# 引入IPv6 IS-IS协议（进程号7）的路由信息，并将其度量值设置为7。

\<Sysname\> system-view

Sysname ripng 100

Sysname-ripng-100 import-route isisv6 7 cost 7

**RIPng \-- RIPng配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

**[maximum load**]**-balancing**命令用来配置RIPng最大等价路由条数。

**[undo maximum load-balancing**]命令用来恢复缺省情况。

【命令】

**[maximum load-balancing** *number*]

**[undo maximum load-balancing**]

【缺省情况】

RIPng支持的等价路由的最大条数与系统支持最大等价路由的条数相同。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：等价路由的最大条数，当*maximum*取值为1时，相当于不进行负载分担。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

如果通过**max-ecmp-num**命令配置系统支持最大等价路由的条数为m，则本命令的缺省值为m，取值范围为1～m。

**[max-ecmp-num**]命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置RIPng最大等价路由条数为2。

\<Sysname\> system-view

Sysname ripng 100

Sysname-ripng-100 maximum load-balancing 2

【相关命令】

·**max-ecmp-num**（三层技术-IP路由命令参考/IP路由基础）

**RIPng \-- RIPng配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

**[non-stop-routing**]命令用来使能RIPng协议的NSR功能。

**[undo non-stop-routing**]命令用来关闭RIPng协议的NSR功能。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【缺省情况】

RIPng协议的NSR功能处于关闭状态。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

RIPng NSR特性与RIPng GR特性互斥，即**non-stop-routing**和**graceful-restart**命令互斥，不能同时配置。

【举例】

\# 配置RIPng进程1使能NSR功能。

\<Sysname\> system-view

Sysname ripng 1

Sysname-ripng-1 non-stop-routing

**RIPng \-- RIPng配置命令 \-- output-delay**

------------------------------------------------------------------------

**[output-delay**]用来配置RIPng报文的发送速率。

**[undo output-delay**]命令用来恢复缺省情况。

【命令】

**[output-delay*** time ***count ***count*]

**[undo output-delay**]

【缺省情况】

发送RIPng报文的时间间隔为20毫秒，一次最多发送3个RIPng报文。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：发送RIPng报文的时间间隔，取值范围为10～100，单位为毫秒。

*[count*]：一次发送RIPng报文的最大个数，取值范围为1～30。

【使用指导】

如果全局和接口都进行了配置，以接口的配置为准。

【举例】

\# 配置RIPng进程1发送RIPng报文的时间间隔为60毫秒，一次最多发送10个RIPng报文。

\<Sysname\> system-view

Sysname ripng 1

Sysname-ripng-1 output-delay 60 count 10

【相关命令】

·**ripng output-delay**

**RIPng \-- RIPng配置命令 \-- preference**

------------------------------------------------------------------------

**[preference**]命令用来配置RIPng路由的优先级。

**[undo preference**]命令用来恢复缺省情况。

【命令】

**[preference**[{ *preference* \| **route-policy** *route-policy-name* } \*]]

**[undo preference**]

【缺省情况】

RIPng路由优先级的值为100。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference*]：RIPng路由优先级的值，取值范围为1～255。取值越小，优先级越高。

**[route-policy*** route-policy*-*name*]：路由策略名称，*route-policy*-*name*为1～63个字符的字符串，区分大小写。对满足特定条件的路由设置优先级。

【使用指导】

通过指定**route-policy**参数，可应用路由策略对特定的路由设置优先级：

·如果在路由策略中已经设置了匹配路由的优先级，则匹配路由取路由策略设置的优先级，其它路由取**preference**命令所设优先级。

·如果在路由策略中没有设置匹配路由的优先级，则所有路由都取**preference**命令所设优先级。

【举例】

\# 配置RIPng路由的优先级为120。

\<Sysname\> system-view

Sysname ripng 100

Sysname-ripng-100 preference 120

**RIPng \-- RIPng配置命令 \-- reset ripng process**

------------------------------------------------------------------------

**[reset ripng process**]命令用来重启指定RIPng进程。

【命令】

**[reset ripng **]*process-id***process**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【使用指导】

执行该命令后，系统提示用户确认是否重启RIPng协议。

【举例】

\# 重启进程号为100的RIPng进程。

\<Sysname\> reset ripng 100 process

Reset RIPng process? [Y/N:y]

**RIPng \-- RIPng配置命令 \-- reset ripng statistics**

------------------------------------------------------------------------

**[reset ripng statistics**]命令用来清除RIPng进程的统计信息。

【命令】

**[reset ripng**] *process-id* **statistics**

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【举例】

\# 清除进程号为100的RIPng进程的统计信息。

\<Sysname\> reset ripng 100 statistics

**RIPng \-- RIPng配置命令 \-- ripng**

------------------------------------------------------------------------

**[ripng**]命令用来创建RIPng进程，并进入RIPng视图。

**[undo ripng**]命令用来关闭RIPng进程。

【命令】

**[ripng** [ *process-id*   **vpn-instance** *vpn-instance-name* ]]

**[undo** **ripng** [ *process-id* ]]

【缺省情况】

没有RIPng进程在运行。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535，缺省值为1。

**[vpn-instance**]* vpn-instance-name*：指定RIPng所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示RIPng位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·必须先创建RIPng进程，才能配置RIPng的各种全局性参数，而配置与接口相关的参数时，可以不受这个限制。

·停止运行RIPng进程后，原来配置的接口参数也同时失效。

【举例】

\# 创建RIPng进程100并进入其视图。

\<Sysname\> system-view

Sysname ripng 100

Sysname-ripng-100

**RIPng \-- RIPng配置命令 \-- ripng default-route**

------------------------------------------------------------------------

**[ripng default-route**]命令用来以指定度量值向RIPng邻居发布一条缺省路由。

**[undo ripng default-route**]命令用来禁止发布RIPng缺省路由和转发IPv6缺省路由。

【命令】

**[ripng default-route**  { **only** \| **originate** } [ **cost** *cost \|* ]**route-policy ***route-policy-name * \*]

**[undo ripng default-route**]

【缺省情况】

RIPng进程不发布缺省路由。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[only**]：只发布IPv6缺省路由（::/0），抑制其它路由的发布。

**[originate**]：发布IPv6缺省路由（::/0），但不影响其它路由的发布。

*[cost*]：发布缺省路由的度量值，取值范围为1～15，缺省值为1。

**[route-policy ***route-policy-name*]：路由策略名称，*route-policy-name*为1～63个字符的字符串，区分大小写。只有当前路由器的路由表中有路由匹配*route-policy-name*指定的路由策略时，才发送缺省路由。

【使用指导】

通过该命令的设置，生成的RIPng缺省路由将强制通过指定接口的路由更新报文发布出去。该IPv6缺省路由的发布不考虑其是否已经存在于IPv6路由表中。

配置发布缺省路由的RIPng接口不接收来自RIPng邻居的缺省路由。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置RIPng只将缺省路由以更新报文的形式从接口发布。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng default-route only

\# 在接口GigabitEthernet1/0/1上配置RIPng将缺省路由同其它路由一起以更新报文的形式从接口发布。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng default-route originate

·交换应用

\# 在接口Vlan-interface100上配置RIPng只将缺省路由以更新报文的形式从接口发布。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng default-route only

\# 在接口Vlan-interface101上配置RIPng将缺省路由同其它路由一起以更新报文的形式从接口发布。

\<Sysname\> system-view

Sysname interface vlan-interface 101

Sysname-Vlan-interface101 ripng default-route originate

**RIPng \-- RIPng配置命令 \-- ripng enable**

------------------------------------------------------------------------

**[ripng** **enable**]命令用来在接口上使能RIPng路由协议。

**[undo ripng enable**]命令用来在接口上关闭RIPng路由协议。

【命令】

**[ripng** *process-id* **enable**]

**[undo ripng****enable**]

【缺省情况】

接口禁用RIPng路由协议。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：RIPng进程号，取值范围为1～65535。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使能RIPng 100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng 100 enable

·交换应用

\# 在接口Vlan-interface100上使能RIPng 100。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng 100 enable

**RIPng \-- RIPng配置命令 \-- ripng ipsec-profile**

------------------------------------------------------------------------

![说明](RIPng命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ripng ipsec-profile**]命令用来在RIPng接口上应用安全框架。

**[undo ripng ipsec-profile**]命令用来取消RIPng接口上应用的安全框架。

【命令】

**[ripng ipsec-profile***profile-name*]

**[undo ripng ipsec-profile**]

【缺省情况】

RIPng接口没有应用安全框架。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：安全框架名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

本命令应结合IPsec安全框架使用，IPsec安全框架的具体情况请参见"安全配置指导"中的"IPsec"。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1应用的IPsec安全框架为profile001。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng ipsec-profile profile001

·交换应用

\# 配置接口Vlan-interface100应用的IPsec安全框架为profile001。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng ipsec-profile profile001

**RIPng \-- RIPng配置命令 \-- ripng metricin**

------------------------------------------------------------------------

**[ripng metricin**]命令用来配置接口接收RIPng路由时的附加度量值。

**[undo ripng metricin**]命令用来恢复缺省情况

【命令】

**[ripng**] **metricin** *value*

**[undo ripng**] **metricin**

【缺省情况】

接口接收RIPng路由时的附加度量值为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接收附加度量值，取值范围为0～16。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1在接收RIPng路由时的附加度量值为12。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng metricin 12

·交换应用

\# 指定接口Vlan-interface100在接收RIPng路由时添加的附加度量值为12。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng metricin 12

**RIPng \-- RIPng配置命令 \-- ripng metricout**

------------------------------------------------------------------------

**[ripng metricout**]命令用来配置接口发送RIPng路由时的附加度量值。

**[undo ripng metricout**]命令用来恢复缺省情况。

【命令】

**[ripng metricout**] *value*

**[undo **]**ripng metricout**

【缺省情况】

接口发送RIPng路由时的附加度量值为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：发送附加度量值，取值范围为1～16。

【举例】

·路由应用

\# 设置接口GigabitEthernet1/0/1发送RIPng路由时添加的附加度量值为12。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng metricout 12

·交换应用

\# 设置接口Vlan-interface100发送RIPng路由时添加的附加度量值为12。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng metricout 12

**RIPng \-- RIPng配置命令 \-- ripng output-delay**

------------------------------------------------------------------------

**[ripng output-delay**]命令用来配置接口下RIPng报文的发送速率。

**[undo ripng output-delay**]命令用来恢复缺省情况。

【命令】

**[ripng output-delay*** time*** count*** count*]

**[undo ripng output-delay**]

【缺省情况】

RIPng报文的发包速率由进程全局的配置决定。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：接口发送RIP报文的时间间隔，取值范围为10～100，单位为毫秒。

*[count*]：接口一次发送RIPng报文的最大个数，取值范围为1～30。

【使用指导】

如果全局和接口都进行了配置，以接口的配置为准。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1配置发送RIPng报文的时间间隔为30毫秒，一次最多发送6个RIPng报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng output-delay 30 count 6

·交换应用

\# 在接口Vlan-interface100配置发送RIPng报文的时间间隔为30毫秒，一次最多发送6个RIPng报文。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng output-delay 30 count 6

【相关命令】

·**output-delay**

**RIPng \-- RIPng配置命令 \-- ripng poison-reverse**

------------------------------------------------------------------------

**[ripng poison-reverse**]命令用来使能毒性逆转功能。

**[undo ripng poison-reverse**]命令用来关闭毒性逆转功能。

【命令】

**[ripng poison-reverse**]

**[undo ripng poison-reverse**]

【缺省情况】

毒性逆转功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置对RIPng更新报文进行毒性逆转。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng poison-reverse

·交换应用

\# 在接口Vlan-interface100上配置对RIPng更新报文进行毒性逆转。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng poison-reverse

**RIPng \-- RIPng配置命令 \-- ripng split-horizon**

------------------------------------------------------------------------

**[ripng** **split-horizon**]命令用来使能水平分割功能。

**[undo ripng split-horizon**]命令用来关闭水平分割。

【命令】

**[ripng split-horizon**]

**[undo ripng split-horizon**]

【缺省情况】

水平分割功能处于使能状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·通常情况下，为了防止路由环路的出现，水平分割都是必要的，因此，建议不要关闭水平分割。

·只是在某些特殊情况下，为保证协议的正确执行，需要关闭水平分割。在关闭水平分割时一定要确认是否必要。

·如果同时使能了水平分割和毒性逆转，则只有毒性逆转功能生效。

·在帧中继和X.25等NBMA（Non-Broadcast Multi-Access，非广播多路访问）网络中，当主接口和点到多点子接口配置了多条虚电路时，为了保证路由信息的正确传播，需要关闭水平分割功能。关于帧中继和X.25的详细信息，请参见"二层技术-广域网接入配置指导"中的"帧中继"和"LAPB和X.25"。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置水平分割。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ripng split-horizon

·交换应用

\# 在接口Vlan-interface100上配置水平分割。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ripng split-horizon

**RIPng \-- RIPng配置命令 \-- ripng summary-address**

------------------------------------------------------------------------

**[ripng summary-address**]命令用来配置RIPng在接口发布聚合的IPv6地址，并指定被聚合的路由的IPv6前缀。

**[undo ripng summary-address**]命令用来禁止RIPng路由器发布聚合的IPv6地址。

【命令】

**[ripng summary-address ***ipv6-address**prefix-length*]

**[undo ripng summary-address** *ipv6-address prefix-length*]

【缺省情况】

没有配置RIPng在接口发布聚合的IPv6地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：聚合路由的目的IPv6地址。

*[prefix-length*]：聚合路由的目的IPv6地址前缀长度，取值范围为0～128。它指定地址中有多少连续的位组成IPv6网络前缀，即IPv6地址中的网络地址部分。

【使用指导】

如果一条路由的前缀和前缀长度与定义的IPv6前缀匹配，则这个自定义的IPv6前缀将取代原来的路由被发布出去。这样，多条路由将由一条路由所代替，而且，这条路由的度量值是原多条路由中最低的。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置IPv6地址2001:200::3EFF:FE11:6770，前缀长度为64位。通过RIPng聚合为IPv6地址前缀2001:200::/35。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 address 2001:200::3EFF:FE11:6770/64

Sysname-GigabitEthernet1/0/1 ripng summary-address 2001:200:: 35

·交换应用

\# 在接口Vlan-interface100上配置IPv6地址2001:200::3EFF:FE11:6770，其前缀长度为64位。通过RIPng聚合为IPv6地址前缀2001:200::/35。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 address 2001:200::3EFF:FE11:6770/64

Sysname-Vlan-interface100 ripng summary-address 2001:200:: 35

**RIPng \-- RIPng配置命令 \-- timer triggered**

------------------------------------------------------------------------

**[timer triggered**]命令用来配置触发更新的时间间隔。

**[undo timer triggered**]命令用来恢复缺省情况。

【命令】

**[timer triggered ***maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo timer triggered**]

【缺省情况】

发送触发更新的最大时间间隔为5秒，最小间隔为50毫秒，增量惩罚间隔为200毫秒。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：触发更新的最大间隔时间。取值范围是1{.varname}～5{.varname}，单位是秒。{.varname}

*[minimum-interval*]：触发更新的最小间隔时间。取值范围是10{.varname}～5000{.varname}，单位是毫秒。{.varname}

*incremental-interval*{.varname}：触发更新间隔的增加时间。取值范围是100{.varname}～1000{.varname}，单位是毫秒。{.varname}

【使用指导】

本命令在网络变化不频繁的情况下将触发更新的时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将时间间隔按照配置的惩罚增量延长，最大不超过*maximum-interval*。

*[minimum-interval*]和*incremental-interval*配置值不允许大于*maximum-interval*配置值。

【举例】

\# 配置发送触发更新的最大时间间隔为2秒，最小时间间隔为100毫秒，惩罚增量为100毫秒。

\<Sysname\> system-view

Sysname ripng 100

Sysname-ripng-100 timer triggered 2 100 100

**RIPng \-- RIPng配置命令 \-- timers**

------------------------------------------------------------------------

**[timers**]命令用来配置RIPng定时器的值。

**[undo timers**]命令用来恢复缺省情况。

【命令】

**[timers **[{ **garbage-collect** *garbage-collect-value* \| **suppress** *suppress-value* \| **timeout** *timeout-value* \| **update** *update-value* } \*]]

**[undo timers **[{ **garbage-collect** \| **suppress** \| **timeout** \| **update** } \*]]

【缺省情况】

Garbage-collect定时器的值为120秒，Suppress定时器的值为120秒，Timeout定时器的值为180秒，Update定时器的值为30秒。

【视图】

RIPng视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[garbage-collect-value*]：Garbage-collect定时器的值，取值范围为1～86400，单位为秒。

*[suppress-value*]：Suppress定时器的值，取值范围为0～86400，单位为秒。

*[timeout-value*]：Timeout定时器的值，取值范围为1～86400，单位为秒。

*[update-value*]：Update定时器的值，取值范围为1～86400，单位为秒。

【使用指导】

RIPng受四个定时器的控制，分别是Update、Timeout、Suppress和Garbage-Collect，其中：

·Update定时器，定义了发送更新报文的时间间隔。

·Timeout定时器，定义了路由老化时间。如果在老化时间内没有收到关于某条路由的更新报文，则该条路由在路由表中的度量值将会被设置为16。

·Suppress定时器，定义了RIPng路由处于抑制状态的时间段长度。当一条路由的度量值变为16时，该路由将进入被抑制状态。在被抑制状态，只有来自同一邻居，且度量值小于16的路由更新才会被路由器接收，取代不可达路由。

·Garbage-Collect定时器，定义了一条路由从度量值变为16开始，直到它从路由表里被删除所经过的时间。在Garbage-Collect时间内，RIPng以16作为度量值向外发送这条路由的更新，如果Garbage-Collect超时，该路由仍没有得到更新，则该路由将从路由表中被彻底删除。

需要注意的是：

·通常情况下，无需改变各定时器的缺省值，该命令须谨慎使用。

·各个定时器的值在网络中所有的路由器上必须保持一致。

【举例】

\# 分别设置RIPng进程1各定时器的值：其中，Update定时器的值为5秒、Timeout定时器的值为15秒、Suppress定时器的值为15秒、Garbage-Collect定时器的值为30秒。

\<Sysname\> system-view

Sysname ripng 1

Sysname-ripng-1 timers update 5 timeout 15 suppress 15 garbage-collect 30

