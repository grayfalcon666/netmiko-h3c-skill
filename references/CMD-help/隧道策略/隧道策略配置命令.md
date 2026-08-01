<!-- CMD-INDEX
  display mpls tunnel                 | 任意视图             | L8
  preferred-path                      | 隧道策略视图           | L114
  select-seq load-balance-number      | 隧道策略视图           | L172
  tunnel-policy                       | 系统视图             | L232
-->

**隧道策略 \-- 隧道策略配置命令 \-- display mpls tunnel**

------------------------------------------------------------------------

**[display mpls tunnel**]命令用来显示隧道信息。

【命令】

**[display mpls tunnel**[ { **all** \| **statistics** \| [ **vpn-instance** *vpn-instance-name* ] **destination** { *tunnel-ipv4-dest* \| *tunnel-ipv6-dest* } }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有隧道的信息。

**[statistics**]：显示隧道的统计信息。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的隧道信息。*vpn-instance-name*为VPN实例名称，为1～31字符的字符串，区分大小写。如果没有指定本参数，则显示公网的隧道信息。

**[destination**]：显示目的地址为指定地址的隧道的信息。

*[tunnel-ipv4-dest*]：显示目的地址为指定IPv4地址的隧道的信息。*tunnel-ipv4-dest*为隧道目的IPv4地址。

*[tunnel-ipv6-dest*]：显示目的地址为指定IPv6地址的隧道的信息。*tunnel-ipv6-dest*为隧道目的IPv6地址。

【举例】

\# 显示所有隧道的信息。

\<Sysname\> display mpls tunnel all

Destination      Type     Tunnel/NHLFE      VPN Instance

2.2.2.2          LSP      NHLFE1024         -

3.3.3.3          CRLSP    Tunnel2           -

3.3.3.3          GRE      Tunnel3           -

4.4.4.4          CRLSP    Tunnel-Bundle0    -

表1-1 display mpls tunnel all命令显示信息描述表

字段

描述

Destination

隧道目的地址

Type

隧道类型，取值包括LSP、GRE和CRLSP（表示MPLS TE隧道）

Tunnel/NHLFE

Tunnel隧道、捆绑隧道或NHLFE表项

取值为NHLFE*number*时，表示与NID为*number*的NHLFE表项对应的Ingress LSP

VPN Instance

VPN实例名称，为"-"表示公网

\# 显示隧道的统计信息。

\<Sysname\> display mpls tunnel statistics

LSP  :     1

GRE  :     0

CRLSP:     0

表1-2 display mpls tunnel statistics命令显示信息描述表

字段

描述

LSP

LSP隧道的数量

GRE

GRE隧道的数量

CRLSP

CRLSP（MPLS TE）隧道的数量

**隧道策略 \-- 隧道策略配置命令 \-- preferred-path**

------------------------------------------------------------------------

**[preferred-path**]命令用来指定到固定目的地址的首选隧道。

**[undo preferred-path**]命令用来恢复缺省情况。

【命令】

**[preferred-path ***[number*[ \| ]**tunnel-bundle ***number* }]

**[undo preferred-path ***[number*[ \| ]**tunnel-bundle ***number* }]

【缺省情况】]

未]指定到固定目的地址的首选隧道。

【视图】

隧道策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tunnel**] *number*：配置指定的MPLS TE隧道或GRE隧道为首选隧道。*number*为隧道接口的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[tunnel-bundle **]*number*：配置指定的捆绑隧道为首选隧道。*number*为隧道捆绑接口的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

通过本命令配置首选隧道后，如果对端PE地址与隧道接口/隧道捆绑接口的目的地址相同，则通过该隧道/捆绑隧道转发到达该PE的流量。该方式为MPLS VPN显式指定了一条MPLS TE隧道、GRE隧道或捆绑隧道，选择的隧道是明确的、可以预期的，便于网络流量规划。推荐使用该方式配置隧道策略。

需要注意的是：

·如果希望隧道/捆绑隧道只被特定策略使用，则不要将同一隧道/捆绑隧道指定为多个策略下的首选隧道。

·如果在同一个隧道策略下配置的多条首选隧道的目的地址相同，则选择配置的第一条首选隧道，如果第一条首选隧道不可用，则选择下一条首选隧道，以此类推。也就是说到达同一个目的地址只能存在一条首选隧道，不会在多条隧道间进行负载分担。

·一个隧道策略下最多可以指定128个首选隧道。

【举例】

\# 配置隧道策略policy1的首选隧道为接口Tunnel1和Tunnel2对应的隧道：优先选择Tunnel1；如果Tunnel1不可用，则选择Tunnel2。

\<Sysname\> system-view

Sysname tunnel-policy policy1

Sysname-tunnel-policy-policy1 preferred-path tunnel 1

Sysname-tunnel-policy-policy1 preferred-path tunnel 2

**隧道策略 \-- 隧道策略配置命令 \-- select-seq load-balance-number**

------------------------------------------------------------------------

**[select-seq load-balance-number**]命令用来配置隧道的选择顺序和负载分担的隧道数目。

**[undo select-seq**]命令用来恢复缺省配置。

【命令】

**[select-seq **[{ **cr-lsp** \| **gre** \| **lsp** } \* **load-balance-number**] *number*]

**[undo select-seq**]

【缺省情况】

按照LSP隧道－\>GRE隧道－\>CR-LSP隧道的优先级顺序选择隧道，负载分担的隧道数目为1。

【视图】

隧道策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cr-lsp**]：CR-LSP隧道。

**[gre**]：GRE隧道。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[lsp**]：LSP隧道。

**[load-balance-number*** number*]：指定负载分担的隧道条数，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在配置隧道选择顺序时，隧道类型越靠近关键字**select-seq**，其优先级越高。并且，只有本命令中列举的隧道类型可以被使用。例如：配置了**select-seq lsp gre load-balance-number 3**命令，则优先选择LSP；在没有LSP或LSP不足3条的情况下，选用GRE隧道；不会选用CR-LSP隧道。

通过本命令配置隧道策略时，选择的隧道具有随机性，不便于网络流量规划。不推荐使用该方式配置隧道策略。

需要注意的是，如果同时配置了本命令和**preferred-path**命令，则优先选择**preferred-path**命令指定的隧道，即：

·如果对端PE地址与某条首选隧道的目的地址相同，则采用该隧道/捆绑隧道转发流量，不会再根据**select-seq load-balance-number**命令指定的隧道选择顺序和负载分担数目选择隧道。

·如果不存在隧道目的地址与对端PE地址相同的首选隧道，则根据**select-seq load-balance-number**命令指定的隧道选择顺序和负载分担数目选择隧道。

【举例】

\# 配置隧道策略policy1为只能使用GRE隧道，负载分担条数为2。

\<Sysname\> system-view

Sysname tunnel-policy policy1

Sysname-tunnel-policy-policy1 select-seq gre load-balance-number 2

**隧道策略 \-- 隧道策略配置命令 \-- tunnel-policy**

------------------------------------------------------------------------

**[tunnel-policy**]命令用来创建隧道策略，并进入隧道策略视图。

**[undo tunnel-policy**]命令用来删除已创建的隧道策略。

【命令】

**[tunnel-policy*** tunnel-policy-name*]

**[undo tunnel-policy*** tunnel-policy-name*]

【缺省情况】

设备上不存在任何隧道策略。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tunnel-policy-name*]：隧道策略名称，为1～19个字符的字符串，区分大小写。

【举例】

\# 创建名为policy1的隧道策略，并进入隧道策略视图。

\<Sysname\> system-view

Sysname tunnel-policy policy1

Sysname-tunnel-policy-policy1

