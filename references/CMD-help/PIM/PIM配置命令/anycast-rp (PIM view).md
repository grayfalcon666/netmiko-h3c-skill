<!-- CMD-INDEX
  anycast-rp (PIM view)               | PIM视图            | L63
  bidir-pim enable (PIM view)         | PIM视图            | L117
  bidir-rp-limit (PIM view)           | PIM视图            | L167
  bsm-fragment enable (PIM view)      | PIM视图            | L213
  bsr-policy (PIM view)               | PIM视图            | L255
  c-bsr (PIM view)                    | PIM视图            | L311
  c-rp (PIM view)                     | PIM视图            | L369
  crp-policy (PIM view)               | PIM视图            | L439
  display interface register-tunnel   | 任意视图             | L497
  display pim bsr-info                | 任意视图             | L667
  display pim claimed-route           | 任意视图             | L815
  display pim c-rp                    | 任意视图             | L923
  display pim df-info                 | 任意视图             | L1045
  display pim interface               | 任意视图             | L1143
  display pim nbma-link               | 任意视图             | L1375
  display pim neighbor                | 任意视图             | L1471
  display pim routing-table           | 任意视图             | L1615
  display pim rp-info                 | 任意视图             | L1921
  display pim statistics              | 任意视图             | L2123
  hello-option dr-priority (PIM view) | PIM视图            | L2255
  hello-option holdtime (PIM view)    | PIM视图            | L2305
  hello-option lan-delay (PIM view)   | PIM视图            | L2355
  hello-option neighbor-tracking (PIM view) | PIM视图            | L2409
  hello-option override-interval (PIM view) | PIM视图            | L2455
  holdtime join-prune (PIM view)      | PIM视图            | L2509
  jp-pkt-size (PIM view)              | PIM视图            | L2563
  pim                                 | 系统视图             | L2605
  pim bfd enable                      | 接口视图             | L2659
  pim bsr-boundary                    | 接口视图             | L2731
  pim dm                              | 接口视图             | L2787
  pim hello-option dr-priority        | 接口视图             | L2853
  pim hello-option holdtime           | 接口视图             | L2915
  pim hello-option lan-delay          | 接口视图             | L2977
  pim hello-option neighbor-tracking  | 接口视图             | L3043
  pim hello-option override-interval  | 接口视图             | L3133
  pim holdtime join-prune             | 接口视图             | L3199
  pim nbma-mode                       | ADVPN隧道接口视图      | L3265
  pim neighbor-policy                 | 接口视图             | L3307
  pim require-genid                   | 接口视图             | L3377
  pim sm                              | 接口视图             | L3427
  pim state-refresh-capable           | 接口视图             | L3493
  pim timer graft-retry               | 接口视图             | L3551
  pim timer hello                     | 接口视图             | L3605
  pim timer join-prune                | 接口视图             | L3667
  pim triggered-hello-delay           | 接口视图             | L3735
  register-policy (PIM view)          | PIM视图            | L3789
  register-suppression-timeout (PIM view) | PIM视图            | L3841
  register-whole-checksum (PIM view)  | PIM视图            | L3883
  snmp-agent trap enable pim          | 系统视图             | L3921
  source-lifetime (PIM view)          | PIM视图            | L3971
  source-policy (PIM view)            | PIM视图            | L4013
  spt-switch-threshold (PIM view)     | PIM视图            | L4071
  ssm-policy (PIM view)               | PIM视图            | L4135
  state-refresh-interval (PIM view)   | PIM视图            | L4189
  state-refresh-rate-limit (PIM view) | PIM视图            | L4239
  state-refresh-ttl (PIM view)        | PIM视图            | L4289
  static-rp (PIM view)                | PIM视图            | L4339
  timer hello (PIM view)              | PIM视图            | L4407
  timer join-prune (PIM view)         | PIM视图            | L4457
-->

**PIM \-- PIM配置命令 \-- anycast-rp (PIM view)**

------------------------------------------------------------------------

**[anycast-rp**]命令用来配置Anycast-RP。

**[undo anycast-rp**]命令用来删除Anycast-RP。

【命令】

**[anycast-rp*** anycast-rp-address member-address*]

**[undo anycast-rp** *anycast-rp-address member-address*]

【缺省情况】

没有配置Anycast-RP。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[anycast-rp-address*]：指定Anycast-RP地址。必须是除127.0.0.0/8网段以外的合法单播IP地址。

*[member-address*]：指定Anycast-RP成员地址。必须是除127.0.0.0/8网段以外的合法单播IP地址，不能与*anycast-rp-address*相同。

【使用指导】

本命令可重复配置，配置时如果指定了相同的Anycast-RP地址，则将Anycast-RP成员地址添加到该Anycast-RP地址所属的Anycast-RP集中。

【举例】

\# 在公网实例中配置如下Anycast-RP集：Anycast-RP地址为1.1.0.0，两个成员的地址分别为1.1.0.1和1.2.0.1（前者为本地接口LoopBack1的地址）。

\<Sysname\> system-view

Sysname pim

Sysname-pim anycast-rp 1.1.0.0 1.1.0.1

Sysname-pim anycast-rp 1.1.0.0 1.2.0.1

【相关命令】

·**display****pimrp-info**

**PIM \-- PIM配置命令 \-- bidir-pim enable (PIM view)**

------------------------------------------------------------------------

**[bidir-pim** **enable**]命令用来使能双向PIM。

**[undo** **bidir-pim** **enable**]命令用来关闭双向PIM。

【命令】

**[bidir-pim** **enable**]

**[undo** **bidir-pim** **enable**]

【缺省情况】

双向PIM处于关闭状态。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IP组播路由，本命令才能生效。

【举例】

\# 使能公网实例中的IP组播路由，并使能双向PIM。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname pim

Sysname-pim bidir-pim enable

【相关命令】

·**multicast routing**（IP组播命令参考/组播路由与转发）

**PIM \-- PIM配置命令 \-- bidir-rp-limit (PIM view)**

------------------------------------------------------------------------

**[bidir-rp-limit**]命令用来配置双向PIM RP的最大数目。

**[undo** **bidir-rp-limit**]命令用来恢复缺省情况。

【命令】

**[bidir-rp-limit** *limit*]

**[undo** **bidir-rp-limit**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：指定双向PIM RP的最大数目，取值范围为1到系统所允许的最大值。系统所允许的最大值会随设备的不同而有所差别，请以设备的实际情况为准。

【使用指导】

由于双向PIM为每个RP都要在所有PIM接口上进行DF选举，因此实际组网中不建议配置多个双向PIM RP。通过本命令可以限制双向PIM RP的数目，超出限制值的RP不会生效，仅能进行DF选举而无法指导转发。

【举例】

\# 在公网实例中配置双向PIM RP的最大数目为3。

\<Sysname\> system-view

Sysname pim

Sysname-pim bidir-rp-limit 3

**PIM \-- PIM配置命令 \-- bsm-fragment enable (PIM view)**

------------------------------------------------------------------------

**[bsm-fragment** **enable**]命令用来使能自举报文语义分片功能。

**[undo** **bsm-fragment** **enable**]命令用来关闭自举报文语义分片功能。

【命令】

**[bsm-fragment** **enable**]

**[undo** **bsm-fragment** **enable**]

【缺省情况】

自举报文语义分片功能处于使能状态。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当PIM-SM域或双向PIM域中存在不支持自举报文语义分片的设备时，请关闭本功能。

【举例】

\# 在公网实例中关闭自举报文语义分片功能。

\<Sysname\> system-view

Sysname pim

Sysname-pim undo bsm-fragment enable

**PIM \-- PIM配置命令 \-- bsr-policy (PIM view)**

------------------------------------------------------------------------

**[bsr-policy**]命令用来配置合法的BSR地址范围，以防止BSR欺骗。

**[undo bsr-policy**]命令用来取消BSR地址范围的限制。

【命令】

**[bsr-policy** *acl-number*]

**[undo** **bsr-policy**]

【缺省情况】

BSR的地址范围不受任何限制，即认为来自任意源的自举报文都是合法的。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本ACL的编号，取值范围为2000～2999。

【使用指导】

ACL规则中的**source**参数用来指定合法BSR的源地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

\# 在公网实例中配置合法的BSR地址范围，只允许网段10.1.1.0/24中的设备充当BSR。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 10.1.1.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname pim

Sysname-pim bsr-policy 2000

【相关命令】

·**c-bsr** (PIM view)

**PIM \-- PIM配置命令 \-- c-bsr (PIM view)**

------------------------------------------------------------------------

**[c-bsr**]命令用来配置C-BSR。

**[undo c-bsr**]命令用来删除C-BSR的相关配置。

【命令】

**[c-bsr**[ *ip-address* [ **scope** *group-address* { *mask-length* \| *mask* }   **hash-length** *hash-length* \| **priority** *priority* ] \*]]

**[undo**[ **c-bsr** *ip-address* [ **scope** *group-address* { *mask-length* \| *mask* } ]]]

【缺省情况】

没有配置C-BSR。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定C-BSR的IP地址。

**[scope** *group-address*]：指定管理域C-BSR所服务的组播组地址，取值范围为239.0.0.0～239.255.255.255。如果未指定本参数，表示配置服务于Global域的C-BSR。

*[mask-length*]：指定组播组地址的掩码长度，取值范围为8～32。

*[mask*]：指定组播组地址的掩码。

**[hash-length ***hash-length*]：指定哈希掩码长度，取值范围为0～32，缺省值为30。

**[priority** *priority*]：指定C-BSR的优先级，取值范围为0～255，缺省值为64。数值越大，优先级越高。

【使用指导】

·C-BSR的IP地址必须有对应的本地接口，且该接口上必须使能PIM，否则配置不会生效。

·如果对同一个域多次执行本命令，新配置将覆盖旧配置；而针对不同域的C-BSR则允许指定相同的IP地址。

【举例】

\# 在公网实例中将IP地址为1.1.1.1的设备配置为Global域的C-BSR。

\<Sysname\> system-view

Sysname pim

Sysname-pim c-bsr 1.1.1.1

**PIM \-- PIM配置命令 \-- c-rp (PIM view)**

------------------------------------------------------------------------

**[c-rp**]命令用来配置C-RP。

**[undo c-rp**]命令用来删除C-RP的相关配置。

【命令】

**[c-rp ***ip-address *[[ **advertisement-interval** *adv-interval* \| **group-policy** *acl-number* \| **holdtime** *hold-time* \| **priority** *priority* ] \*  **bidir** ]]

**[undo c-rp*** ip-address*]

【缺省情况】

没有配置C-RP。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定C-RP的IP地址。

**[advertisement-interval** *adv-interval*]：指定发送宣告报文的间隔时间，取值范围为1～65535，单位为秒，缺省值为60秒。

**[group-policy*** acl-number*]：指定IPv4基本ACL的编号，取值范围为2000～2999。如果指定了本参数，该C-RP将只为ACL规则所允许的组播组服务；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则该C-RP将为所有组播组服务。

**[holdtime** *hold-time*]：指定C-RP的超时时间，取值范围为1～65535，单位为秒，缺省值为150秒。

**[priority** *priority*]：指定C-RP的优先级，取值范围为0～255，缺省值为192。数值越大，优先级越低。

**[bidir**]：指定该C-RP服务于双向PIM。如果未指定本参数，该C-RP将服务于PIM-SM。

【使用指导】

·C-RP的IP地址必须有对应的本地接口，且该接口上必须使能PIM，否则配置不会生效。

·ACL规则中的**source**参数用来指定C-RP所服务的组播组范围（若指定的不是组播组地址，则此规则不生效），而其它可选参数都将被忽略。该ACL规则用来定义该C-RP所服务的组播组范围，只有**permit**的组播组都才会作为RP的服务组范围通告出去。

·如果设备想要成为多个组范围的C-RP，则需要在配置**group-policy**所对应的ACL时将多个组范围用多个**rule**规则表示出来。

·如果对同一IP地址多次执行本命令，新配置将覆盖旧配置。

【举例】

\# 在公网实例中将IP地址为1.1.1.1配置为225.1.0.0/16和226.2.0.0/16的C-RP，且C-RP的优先级为10。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 225.1.0.0 0.0.255.255

Sysname-acl-ipv4-basic-2000 rule permit source 226.2.0.0 0.0.255.255

Sysname-acl-ipv4-basic-2000 quit

Sysname pim

Sysname-pim c-rp 1.1.1.1 group-policy 2000 priority 10

**PIM \-- PIM配置命令 \-- crp-policy (PIM view)**

------------------------------------------------------------------------

**[crp-policy**]命令用来配置合法的C-RP地址范围及其服务的组播组范围，以防止C-RP欺骗。

**[undo crp-policy**]命令用来取消C-RP地址范围及其服务的组播组范围的限制。

【命令】

**[crp-policy** *acl-number*]

**[undo** **crp-policy**]

【缺省情况】

C-RP地址范围及其服务的组播组范围不受任何限制，即认为所有收到的C-RP报文都是合法的。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4高级ACL的编号，取值范围为3000～3999。

【使用指导】

·ACL规则中的**source**参数用来指定合法C-RP的地址范围，**destination**参数用来指定该C-RP所服务的组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·本命令在对C-RP所宣告的组播组范围进行过滤时，只取其前缀部分进行匹配。例如，C-RP宣告的组播组范围为224.1.0.0/16，如果其前缀部分"224.1.0.0"能匹配上本命令所引用的ACL规则，就认为整个组播组范围"224.1.0.0/16"都通过了过滤。

【举例】

\# 在公网实例中配置C-RP策略，只允许1.1.1.1/24范围内的设备充当C-RP，且只允许其为225.1.1.0/24范围内的组播组服务。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule permit ip source 1.1.1.1 0.0.0.255 destination 225.1.1.0 0.0.0.255

Sysname-acl-ipv4-adv-3000 quit

Sysname pim

Sysname-pim crp-policy 3000

【相关命令】

·**c-rp** (PIM view)

**PIM \-- PIM配置命令 \-- display interface register-tunnel**

------------------------------------------------------------------------

**[display** **interface** **register-tunnel**]命令用来显示Register-Tunnel接口的相关信息。

【命令】

**[display** **interface** [ **register-tunnel**] *interface-number*   **brief** [ **description** \| **down** ] ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[register-tunnel**]：显示指定Register-Tunnel接口的信息。

*[interface-number*]：表示Register-Tunnel接口的编号。设备上只存在一个Register-Tunnel接口，其编号为0。

**[brief**]：显示概要信息。如果未指定本参数，将显示详细信息。

**[description**]：当用户配置的接口描述信息超过27个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前27个字符，超出部分不会显示。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。如果未指定本参数，将不会根据接口物理状态来过滤显示信息。

【使用指导】

Register-Tunnel接口是一种虚拟接口，由系统自动创建。用户不能对该接口进行配置和删除，但可使用本命令进行显示。

Register-Tunnel接口是在组播源注册过程初期，用于在组播源侧DR与RP之间建立一个传输注册报文的通道，具体过程为：当组播源侧DR第一次收到组播源发来的组播数据时，由于组播源侧DR与RP之间尚未建立SPT，于是组播源侧DR通过其Register-Tunnel接口将封装到注册报文中的组播数据发给RP，而RP也通过其Register-Tunnel接口接收注册报文，并将解封装后的组播数据转发给接收者。

在上述过程中，RP从组播数据中获取到了组播源的位置，于是向组播源方向发送加入报文并最终建立起SPT。此后，组播源侧DR便不再通过Register-Tunnel接口，而是通过SPT将组播数据发送给RP。

需要注意的是：

·如果未指定接口类型，将显示设备支持的所有接口的信息。

·由于设备上只存在一个Register-Tunnel接口（即Register-Tunnel0），因此只要指定了**register-tunnel**参数，不论是否指定*interface-number*参数，都将显示接口Register-Tunnel0的相关信息。

【举例】

\# 显示接口Register-Tunnel0的详细信息。

\<Sysname\> display interface register-tunnel 0

Register-Tunnel0

Current state: UP

Line protocol state: DOWN

Description: Register-Tunnel0 Interface

Maximum Transmit Unit: 1536

Internet protocol processing: disabled

Physical: Unknown

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 0 packets, 0 bytes, 0 drops

Output: 0 packets, 0 bytes, 0 drops

\# 显示接口Register-Tunnel0的概要信息。

\<Sysname\> display interface register-tunnel 0 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

REG0                 UP   \--       \--

表1-1 display interface register-tunnel命令显示信息描述表

字段

描述

Current state

接口的物理状态，Register-Tunnel接口的物理状态始终为UP

Line protocol state

接口的链路状态，Register-Tunnel接口的链路状态始终为DOWN

Description

接口的描述信息，不可配置

Maximum Transmit Unit

接口的最大传输单元，不可配置

Internet protocol processing

接口能否配置IP地址，始终为disabled，表示不能

Physical

接口的物理类型，始终为Unknown，表示未知

Last 300 seconds input rate

最近300秒钟的平均输入速率，始终均为0

Last 300 seconds output rate

最近300秒钟的平均输出速率，始终均为0

Input

接口输入的报文数、字节数、丢弃报文数，始终均为0

Output

接口输出的报文数、字节数、丢弃报文数，始终均为0

Brief information on interface(s) under route mode

三层接口的概要信息

Link: ADM - administratively down; Stby - standby

接口的物理连接状态：

·UP：表示接口在物理上连通

·DOWN：表示接口在物理上不通

·ADM：表示接口被手工关闭，需执行**undo****shutdown**命令才能打开

·Stby：表示接口为备份接口，可使用**display****interface-backup****state**命令查看其主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常NULL、LoopBack等接口会具有该属性

Protocol

接口的协议连接状态，对Register-Tunnel接口无意义，始终为"\--"

Main IP

接口的IP地址，不可配置。对Register-Tunnel接口无意义，始终为"\--"

Cause

接口物理状态为down的原因，始终为Not connected，表示没有物理连接

**PIM \-- PIM配置命令 \-- display pim bsr-info**

------------------------------------------------------------------------

**[display pim bsr-info**]命令用来显示PIM-SM域中的BSR信息。

【命令】

**[display pim ** **vpn-instance** *vpn-instance-name* ] **bsr-info**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的BSR信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的BSR信息。

【举例】

\# 显示公网实例PIM-SM域中的BSR信息。

\<Sysname\> display pim bsr-info

 Scope: non-scoped

     State: Accept Preferred

     Bootstrap timer: 00:01:44

     Elected BSR address: 12.12.12.1

       Priority: 64

       Hash mask length: 30

       Uptime: 00:21:56

 Scope: 239.4.0.0/16

     State: Accept Any

     Scope-zone expiry timer: 00:21:12

 Scope: 239.1.0.0/16

     State: Elected

     Bootstrap timer: 00:00:26

     Elected BSR address: 17.1.11.1

       Priority: 64

       Hash mask length: 30

       Uptime: 02:53:37

     Candidate BSR address: 17.1.11.1

       Priority: 64

       Hash mask length: 30

Scope: 239.2.2.0/24

     State: Candidate

     Bootstrap timer: 00:01:56

Elected BSR address: 61.2.37.1

       Priority: 64

       Hash mask length: 30

       Uptime: 02:53:32

     Candidate BSR address: 17.1.12.1

       Priority: 64

       Hash mask length: 30

 Scope: 239.3.3.0/24

     State: Pending

     Bootstrap timer: 00:00:07

     Candidate BSR address: 17.1.13.1

       Priority: 64

       Hash mask length: 30

表1-2 display pim bsr-info命令显示信息描述表

字段

描述

Scope

域

State

域状态

Bootstrap timer

BSR定时器

Scope-zone expiry timer

域老化定时器

Elected BSR address

当选BSR的地址

Candidate BSR address

候选BSR的地址

Priority

BSR的优先级

Hash mask length

哈希掩码长度

Uptime

BSR已存在的时间

**PIM \-- PIM配置命令 \-- display pim claimed-route**

------------------------------------------------------------------------

**[display pim claimed-route**]命令用来显示PIM所使用的路由信息。

【命令】

**[display pim** [ **vpn-instance** *vpn-instance-name*  **claimed-route**  *source-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的路由信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的路由信息。

*[source-address*]：组播源的IP地址，显示到达指定组播源的路由信息。如果未指定本参数，将显示PIM所使用的所有路由信息。

【举例】

\# 显示PIM在公网实例中使用的所有路由信息。

\<Sysname\> display pim claimed-route

 RPF-route selecting rule: longest-match

 Route/mask: 7.11.0.0/16 (unicast (direct))

     RPF interface: Vlan-interface2, RPF neighbor: 8.0.0.2

     Total number of (S,G) or (\*,G) dependent on this route entry: 4

     (7.11.0.10, 225.1.1.1)

     (7.11.0.10, 226.1.1.1)

     (7.11.0.10, 227.1.1.1)

     (\*, 228.1.1.1)

 Route/mask: 7.12.0.0/16 (multicast static)

     RPF interface: Vlan-interface2, RPF neighbor: 8.0.0.3,

     Config NextHop: 8.0.0.5

     Total number of (S,G) or (\*,G) dependent on this route entry: 2

     (7.12.0.10, 226.1.1.1)

     (7.12.0.10, 225.1.1.1)

表1-3 display pim claimed-route命令显示信息描述表

字段

描述

RPF-route selecting rule

RPF路由的选择规则

Route/mask

路由项。括号内为路由类型，包括：

·igp：单播路由（内部网关协议）

·egp：单播路由（外部网关协议）

·unicast (direct)：单播路由（直连）

·unicast：其它单播路由（如单播静态路由等）

·mbgp：MBGP路由

·multicast static：组播静态路由

RPF interface

RPF接口的名称

RPF neighbor

RPF邻居的IP地址

Config NextHop

配置的下一跳地址，本字段只在组播静态路由配置下一跳时显示

Total number of (S,G) or (\*,G) dependent

on this route entry

基于此RPF路由的（S，G）或（\*，G）个数及列表

**PIM \-- PIM配置命令 \-- display pim c-rp**

------------------------------------------------------------------------

**[display pim c-rp**]命令用来显示PIM-SM域中的C-RP信息。

【命令】

**[display pim ** **vpn-instance** *vpn-instance-name* ] **c-rp**  **local**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的C-RP信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的C-RP信息。

**[local**]：显示本地配置且生效的C-RP信息。如果未指定本参数，将显示所有学习到的C-RP信息。

【使用指导】

只有当选的BSR上才会有学习到的C-RP信息，其它设备上只能查看到本地配置生效的C-RP信息。

【举例】

\# 显示公网实例中学习到的C-RP信息。

\<Sysname\> display pim c-rp

 Scope: non-scoped

     Group/MaskLen: 224.0.0.0/4

       C-RP address             Priority  HoldTime  Uptime    Expires

       1.1.1.1 (local)          192       150       03:01:36  00:02:29

       2.2.2.2                  192       150       1d:13h    00:02:02

     Group/MaskLen: 226.1.1.0/24 [B Expires: 00:00:33]

     Group/MaskLen: 225.1.0.0/16 [B]

       C-RP Address             Priority  HoldTime  Uptime    Expires

       3.3.3.3                  192       150       12w:5d    00:02:05

\# 显示本地配置生效的C-RP信息。

\<Sysname\> display pim c-rp local

 Candidate RP: 12.12.12.9(Loop1)

     Priority: 192

     HoldTime: 150

     Advertisement interval: 60

     Next advertisement scheduled at: 00:00:48

表1-4 display pim c-rp命令显示信息描述表

字段

描述

Scope

域

Group/MaskLen

C-RP所服务的组播组

B

表示C-RP服务于双向PIM。如果未显示本字段，则表示服务于PIM-SM

C-RP address

C-RP的IP地址，local表示本地地址

Priority

C-RP的优先级

HoldTime

C-RP的超时时间

Uptime

C-RP已存在的时间，w表示星期，d表示天，h表示小时

Expires

C-RP/组播组的超时剩余时间

Candidate RP

本地C-RP的IP地址

Advertisement interval

本地C-RP发送通告报文时间间隔

Next advertisement scheduled at

本地C-RP发送下一个通告报文的剩余时间

**PIM \-- PIM配置命令 \-- display pim df-info**

------------------------------------------------------------------------

**[display** **pim** **df-info**]命令用来显示双向PIM的DF信息。

【命令】

**[display** **pim** [ **vpn-instance** *vpn-instance-name*  **df-info**  *rp-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的双向PIM DF信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的双向PIM DF信息。

*[rp-address*]：指定双向PIM的RP地址。

【举例】

\# 显示公网实例中双向PIM的DF信息。

\<Sysname\> display pim df-info

RP address: 12.12.12.12

  Interface: GigabitEthernet0/0/4

    State     : Win        DF preference: 10

    DF metric : 1562       DF uptime    : 00:06:59

    DF address: 30.1.1.11 (local)

  Interface: Tunnel0, 100.1.1.12

    State     : Lose       DF preference: 0

    DF metric : 0          DF uptime    : 00:06:59

    DF address: 100.1.1.12

表1-5 display pim df-info命令显示信息描述表

字段

描述

RP address

双向PIM的RP地址

Interface

接口名称，使能了nbma模式的ADVPN隧道口，显示远端连接IP地址

State

DF的选举状态：

·Win：竞选DF成功

·Lose：竞选DF落败

·Offer：竞选DF的初始状态

·Backoff：正在充当DF，但有更优的设备正在竞选DF

·-：不参与{.TableTextChar}DF竞选{.TableTextChar}

DF preference

DF通告的路由优先级

DF metric

DF通告的路由度量值

DF uptime

DF已存在的时间

DF address

DF的IP地址，local表示本地地址

**PIM \-- PIM配置命令 \-- display pim interface**

------------------------------------------------------------------------

**[display pim interface**]命令用来显示接口上的PIM信息。

【命令】

**[display pim ** **vpn-instance** *vpn-instance-name* ] **interface**  *interface-type interface-number*   **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的PIM信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的PIM信息。

*[interface-type* *interface-number*]：显示指定接口上的PIM信息。如果未指定本参数，将显示所有接口上的PIM信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

【举例】

\# 显示公网实例所有接口上的PIM概要信息。

\<Sysname\> display pim interface

 Interface         NbrCnt  HelloInt  DR-Pri     DR-Address

 GE1/0/1           1       30        1          10.1.1.2

 GE1/0/2           0       30        1          172.168.0.2    (local)

 GE1/0/3           1       30        1          20.1.1.2

表1-6 display pim interface命令显示信息描述表

字段

描述

Interface

接口名称

NbrCnt

PIM邻居的数量

HelloInt

发送Hello报文的时间间隔

DR-Pri

竞选DR的优先级

DR-Address

DR的IP地址，local表示本地地址

\# 显示公网实例接口GigabitEthernet1/0/1上的PIM详细信息。

\<Sysname\> display pim interface gigabitethernet 1/0/1 verbose

Interface: GigabitEthernet1/0/1, 10.1.1.1

     PIM version: 2

     PIM mode: Sparse

PIM DR: 10.1.1.2

     PIM DR Priority (configured): 1

     PIM neighbors count: 1

     PIM hello interval: 30 s

     PIM LAN delay (negotiated): 500 ms

     PIM LAN delay (configured): 500 ms

     PIM override interval (negotiated): 2500 ms

     PIM override interval (configured): 2500 ms

     PIM neighbor tracking (negotiated): disabled

     PIM neighbor tracking (configured): disabled

     PIM generation ID: 0xF5712241

     PIM require generation ID: disabled

     PIM hello hold interval: 105 s

     PIM assert hold interval: 180 s

     PIM triggered hello delay: 5 s

     PIM J/P interval: 60 s

     PIM J/P hold interval: 210 s

     PIM BSR domain border: disabled

     PIM BFD: disabled

     Number of routers on network not using DR priority: 0

     Number of routers on network not using LAN delay: 0

     Number of routers on network not using neighbor tracking: 2

表1-7 display pim interface verbose命令显示信息描述表

字段

描述

Interface

接口名称与IP地址

PIM version

PIM协议的版本号

PIM mode

PIM协议的模式，是密集模式还是稀疏模式

PIM DR

DR的IP地址

PIM DR Priority (configured)

竞选DR优先级的配置值

PIM neighbors count

PIM邻居的总数

PIM hello interval

发送Hello报文的时间间隔

PIM LAN delay (negotiated)

剪枝报文传输延迟的协商值

PIM LAN delay (configured)

剪枝报文传输延迟的配置值

PIM override interval (negotiated)

剪枝否决时间的协商值

PIM override interval (configured)

剪枝否决时间的配置值

PIM neighbor tracking (negotiated)

邻居跟踪使能与否的协商情况

PIM neighbor tracking (configured)

邻居跟踪使能与否的配置情况

PIM generation ID

Generation_ID参数值

PIM require generation ID

是否使能不接受无Generation ID的Hello报文

PIM hello hold interval

保持PIM邻居的可达状态的时间

PIM assert hold interval

保持断言状态的时间

PIM triggered hello delay

发送Hello报文的最大延迟时间

PIM J/P interval

发送加入/剪枝报文的时间间隔

PIM J/P hold interval

加入/剪枝状态的保持时间

PIM BSR domain border

该接口是否配置了BSR的服务边界

PIM BFD

该接口是否使能了PIM与BFD联动功能

Number of routers on network not using DR priority

该接口所在网段上没有使用DR优先级字段的路由器数量

Number of routers on network not using LAN delay

该接口所在网段上未使用LAN-delay字段的路由器数量

Number of routers on network not using neighbor tracking

该接口所在网段上未使能邻居跟踪的路由器数量

**PIM \-- PIM配置命令 \-- display pim nbma-link**

------------------------------------------------------------------------

**[display pim nbma-link **]命令用来显示PIM模块维护的ADVPN隧道接口上对端的信息。

【命令】

**[display pim ** **vpn-instance** *vpn-instance-name* ] **nbma-link**  **interface** { *interface-type interface-number* }

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的PIM信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的PIM信息。

**[interface** *interface-type* *interface-number*]：接口类型和接口编号，显示指定接口上的PIM维护的ADVPN隧道接口上对端的信息。如果未指定本参数，将显示所有ADVPN隧道接口上对端的信息。

【举例】

\#显示公网所有PIM维护的ADVPN隧道接口上对端的信息。

\<Sysname\> display pim nbma-link  

Interface: Tunnel1

Number of links: 1

    Remote address: 10.0.0.1

      Private index    : 0XCC000000

      Private interface: Multicast-NBMA0

Interface: Tunnel2

Number of links: 1

    Remote address: 20.0.0.2

      Private index    : 0XCC000001

      Private interface: Multicast-NBMA1

\#显示公网指定PIM维护的ADVPN隧道接口上对端的信息。

\<Sysname\> display pim nbma-link interface tunnel 1

Interface: Tunnel1

Number of links: 1

    Remote address: 10.0.0.1

      Private index    : 0XCC000000

      Private interface: Multicast-NBMA0

表1-8 display pim nbma-link命令显示信息描述表

字段

描述

Interface     

隧道接口名称

Number of links

该隧道下的远端连接的个数

Remote address

远端连接的地址

Private index

对应远端连接的索引

Private interface

对应远端连接的接口

**PIM \-- PIM配置命令 \-- display pim neighbor**

------------------------------------------------------------------------

**[display pim neighbor**]命令用来显示PIM邻居信息。

【命令】

**[display pim **[ **vpn-instance** *vpn-instance-name*  **neighbor** [ *neighbor-address* \| **interface** *interface-type interface-number* \| **verbose** ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的PIM邻居信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的PIM邻居信息。

*[neighbor-address*]：PIM邻居的IP地址，显示指定PIM邻居的信息。如果未指定本参数，将显示所有PIM邻居的信息。

**[interface** *interface-type* *interface-number*]：接口类型和接口编号，显示指定接口上的PIM邻居信息。如果未指定本参数，将显示所有接口上的PIM邻居信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

【举例】

\# 显示公网实例所有PIM邻居的概要信息。

\<Sysname\> display pim neighbor

 Total Number of Neighbors = 2

 Neighbor        Interface           Uptime   Expires  DR-Priority Mode

 10.1.1.2        GE1/0/1             02:50:49 00:01:31 1           B

 20.1.1.2        GE1/0/2             02:49:39 00:01:42 1           P

\# 显示公网实例中IP地址为11.110.0.20的PIM邻居的详细信息。

\<Sysname\> display pim neighbor 11.110.0.20 verbose

 Neighbor: 11.110.0.20

     Interface: GigabitEthernet1/0/3

     Uptime: 00:00:10

     Expiry time: 00:00:30

     DR Priority: 1

     Generation ID: 0x2ACEFE15

     Holdtime: 105 s

     LAN delay: 500 ms

     Override interval: 2500 ms

     State refresh interval: 60 s

     Neighbor tracking: Disabled

     Bidirectional PIM: Enabled

     RPF proxy vector: Enabled

表1-9 display pim neighbor命令显示信息描述表

字段

描述

Total Number of Neighbors

PIM邻居的总数

Neighbor

PIM邻居的IP地址

Interface

PIM邻居所在接口的名称

Uptime

PIM邻居已存在的时间

Expires/Expiry time

PIM邻居超时的剩余时间，never表示PIM邻居永不超时，即永远可达

DR-Priority/DR Priority

PIM邻居的优先级

Mode

PIM邻居的模式，B表示双向PIM模式，P表示开启RPF代理向量功能，显示为空则表示非双向PIM模式且关闭RPF代理向量功能

Generation ID

PIM邻居的Generation ID（状态随机数）

Holdtime

PIM邻居的生存时间，forever表示PIM邻居永远存在，即永远可达

LAN delay

PIM报文在共享网段中的传输延迟

Override interval

剪枝否决的时间间隔

State refresh interval

状态刷新的时间间隔，只有当PIM邻居工作在PIM-DM模式下且具备状态刷新能力时才会显示本字段

Neighbor tracking

邻居跟踪功能是否使能

Bidirectional PIM

双向PIM是否使能

RPF proxy vector

RPF代理向量功能（请参见"IP组播配置指导"中的"组播VPN"）是否使能

**PIM \-- PIM配置命令 \-- display pim routing-table**

------------------------------------------------------------------------

**[display pim routing-table**]命令用来显示PIM路由表的内容。

【命令】

**[display pim **[ **vpn-instance** *vpn-instance-name*  **routing-table** [ *group-address* [ **mask** { *mask-length* \| *mask* } ] \| *source-address* [ **mask** { *mask-length* \| *mask* } ] \| **flags** *flag-value* \| **fsm** \| **incoming-interface** *interface-type* *interface-number* \| **mode** *mode-type* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \| **proxy** ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的PIM路由项，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的PIM路由项。

*[group-address*]：组播组地址，显示指定组播组的PIM路由项，取值范围为224.0.0.0～239.255.255.255。如果未指定本参数，将显示所有组播组的PIM路由项。

*[source-address*]：组播源地址，显示包含指定组播源的PIM路由项。

*[mask-length*]：指定组播组或组播源地址的掩码长度，取值范围为0～32，缺省值为32。

*[mask*]：指定组播组或组播源地址的掩码，缺省值为255.255.255.255。

**[flags*** flag-value*]：PIM标志，显示包含指定标志的PIM路由项。如果未指定本参数，将显示包含所有标志的PIM路由项。*flag-value*的取值及含义如下**：**

·**2msdp**：表示准备向MSDP发出通知，在下一个SA报文中包含的PIM路由项；

·**act**：表示已经有实际数据到达的PIM路由项；

·**del**：表示计划删除的PIM路由项；

·**exprune**：表示某些出接口被其它组播路由协议剪枝的PIM路由项；

·**ext**：表示包含了由其它组播路由协议提供出接口的PIM路由项；

·**loc**：表示在与组播源处于同一网段的路由器上的PIM路由项；

·**msdp**：表示从MSDP的SA报文中学习到的PIM路由项；

·**niif**：表示未确定入接口的PIM路由项；

·**nonbr**：表示PIM邻居查找失败的PIM路由项；

·**rpt**：表示向RP方向发送过（S，G）RPT位剪枝的PIM路由项；

·**rq**：表示Data-MDT切换接收端的PIM路由项；

·**spt**：表示SPT上的PIM路由项；

·**sq**：表示Data-MDT切换发起端的PIM路由项；

·**swt**：表示正处于向SPT切换过程中的PIM路由项；

·**wc**：表示带WC通配符的PIM路由项。

**[fsm**]：显示有限状态机的详细信息。

**[incoming-interface** *interface-type interface-number*]：显示指定入接口的PIM路由项。如果未指定本参数，将显示所有入接口的PIM路由项。

**[mode ***mode-type*]：PIM模式，显示指定模式下的PIM路由项。如果未指定本参数，将显示所有模式下的PIM路由项。*mode-type*的取值及含义如下：

·**bidir**：表示双向PIM模式；

·**dm**：表示PIM-DM模式；

·**sm**：表示PIM-SM模式；

·**ssm**：表示PIM-SSM模式。

**[outgoing-interface**[ { **exclude** \| **include** \| **match** } *interface-type* *interface-number*]]：显示指定出接口的PIM路由项。其中，**exclude**表示不包含指定接口；**include**表示包含指定接口；**match**表示包含且仅包含指定接口。如果未指定本参数，将显示所有出接口的PIM路由项。

**[proxy**]：显示PIM路由项使用的RPF代理向量信息。

【举例】

\# 显示公网实例PIM路由表的内容。

\<Sysname\> display pim routing-table

 Total 0 (\*, G) entries; 1 (S, G) entries

 (172.168.0.12, 227.0.0.1)

     RP: 2.2.2.2

     Protocol: pim-sm, Flag: SPT LOC ACT

     UpTime: 02:54:43

     Upstream interface: GigabitEthernet1/0/1

         Upstream neighbor: NULL

         RPF prime neighbor: NULL

     Downstream interface information:

     Total number of downstream interfaces: 1

         1: Vlan-interface2

Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

\# 显示ADVPN应用组网PIM路由表的内容。

\<Sysname\> display pim routing-table

 Total 0 (\*, G) entries; 1 (S, G) entries

 (172.168.0.12, 227.0.0.1)

     RP: 2.2.2.2

     Protocol: pim-sm, Flag: SPT LOC ACT

     UpTime: 02:54:43

     Upstream interface: Tunnel0, 13.1.1.1

         Upstream neighbor: 12.1.1.1

         RPF prime neighbor: 12.1.1.1

     Downstream interface information:

     Total number of downstream interfaces: 1

         1: Tunnel0, 13.1.1.2

             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

表1-10 display pim routing-table命令显示信息描述表

字段

描述

Total 0 (\*, G) entries; 1 (S, G) entries

PIM路由表中（S，G）与（\*，G）表项的总数

(172.168.0.12, 227.0.0.1)

PIM路由表中的（S，G）表项

Protocol

PIM的模式

Flag

PIM路由表中（S，G）或（\*，G）表项的标志：

·ACT：表示已有实际数据到达

·DEL：表示计划要删除

·EXPRUNE：表示某些出接口被其它组播路由协议剪枝

·EXT：表示包含了由其它组播路由协议提供的出接口

·LOC：表示与组播源处于同一网段

·NIIF：表示未确定入接口

·NONBR：表示PIM邻居查找失败

·RPT：表示向RP方向发送过（S，G）RPT位剪枝

·SPT：表示在SPT上

·SWT：表示正在向SPT切换

·WC：表示带WC通配符

Uptime

（S，G）或（\*，G）表项已存在的时间

Upstream interface

（S，G）或（\*，G）表项的入接口，使能了nbma模式的ADVPN隧道口，显示远端连接IP地址

Upstream neighbor

（S，G）或（\*，G）表项的上游邻居

RPF prime neighbor

（S，G）或（\*，G）表项的RPF邻居：

·对（\*，G）表项来说，当该路由器是RP时，（\*，G）表项的RPF邻居是NULL

·对（S，G）表项来说，当该路由器直连源时，（S，G）表项的RPF邻居是NULL

RPF proxy vector

RPF代理向量，本字段只有在B类跨AS的MD VPN（请参见"IP组播配置指导"中的"组播VPN"）组网中才会显示

Downstream interface information

下游接口的信息，包括：

·下游接口的总数

·下游接口的名称

·下游接口使用的协议类型

·下游接口的存在时间

·下游接口的超时时间

·下游接口（ADVPN隧道口）对应的隧道远端的IP地址

\# 在PE设备上显示公网实例PIM路由项使用的RPF代理向量信息。

\<Sysname\> display pim routing-table proxy

 (100.0.0.8, 232.1.1.1)

    Proxy: 10:1/192.168.0.4

    Assigner: 0.0.0.0         Origin: BGP MDT

    Uptime: 02:08:18          Expires: Off

\# 在P设备上显示公网实例PIM路由项使用的RPF代理向量信息。

\<Sysname\> display pim routing-table proxy

(100.0.0.8, 232.1.1.1)

    Proxy: 10:1/192.168.0.4

    Assigner: 1.0.3.1         Origin: PIM

    Uptime: 02:19:33          Expires: 00:02:12

\# 在ASBR设备上显示公网实例PIM路由项使用的RPF代理向量信息。

\<Sysname\> display pim routing-table proxy

(100.0.0.1, 232.1.1.1)

    Proxy: 10:1/local

    Assigner: 1.0.5.9         Origin: PIM

    Uptime: 02:22:04          Expires: 00:02:35

 (100.0.0.8, 232.1.1.1)

    Proxy: 10:1/local

    Assigner: 1.0.4.1         Origin: PIM

    Uptime: 02:21:10          Expires: 00:02:35

表1-11 display pim routing-table proxy命令显示信息描述表

字段

描述

Proxy

代理向量信息，包括RD（Route Distinguisher，路由标识符）和RPF代理向量的地址，local表示RPF代理向量为本地地址（比如在ASBR上）

Assigner

分配RPF代理向量的设备地址：

·在PE上，RPF代理向量是从BGP MDT路由中获取的，显示为0.0.0.0

·在非PE上，RPF代理向量是从下游PIM邻居发来的PIM加入报文中学到的，显示为下游PIM邻居的接口地址

Origin

产生RPF代理向量的协议：

·在PE上，RPF代理向量是从BGP MDT路由中获取的，显示为BGP MDT

·在非PE上，RPF代理向量是从下游PIM邻居发来的PIM加入报文中学到的，显示为PIM

Uptime

RPF代理向量已存在的时间

Expires

RPF代理向量的的超时剩余时间，Off表示该定时器关闭

**PIM \-- PIM配置命令 \-- display pim rp-info**

------------------------------------------------------------------------

**[display pim rp-info**]命令用来显示PIM-SM域中的RP信息。

【命令】

**[display pim ** **vpn-instance** *vpn-instance-name* ] **rp-info**  *group-address*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的RP信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的RP信息。

*[group-address*]：组播组地址，显示指定组播组所对应的RP信息，取值范围为224.0.1.0～239.255.255.255。如果未指定本参数，将显示所有组播组对应的RP信息。

【举例】

\# 显示公网实例中组播组224.0.1.1所对应的RP信息。

\<Sysname\> display pim rp-info 224.0.1.1

 BSR RP address is: 2.2.2.2

     Priority: 192

     HoldTime: 180

     Uptime: 03:01:10

     Expires: 00:02:30

 Static RP address is: 3.3.3.5

     Preferred: Yes

     Configured ACL: 2003

 RP mapping for this group is: 3.3.3.5

 Anycast-RP 3.3.3.5 members:

     Member address           State

     1.1.0.1                  Active

     1.2.0.2                  Local

     1.2.0.1                  Remote

\# 显示公网实例中所有组播组对应的RP信息。

\<Sysname\> display pim rp-info

BSR RP information:

   Scope: non-scoped

Group/MaskLen: 224.0.0.0/4

       RP address               Priority  HoldTime  Uptime    Expires

       1.1.1.1 (local)          192       180       03:01:36  00:02:29

       2.2.2.2                  192       180       1d:13h    00:02:02

     Group/MaskLen: 225.1.0.0/16 [B]

       RP address               Priority  HoldTime  Uptime    Expires

       3.3.3.3                  192       180       12w:5d    00:02:05

 Static RP information:

       RP address               ACL   Mode    Preferred

       3.3.3.1                  2000  pim-sm  No

       3.3.3.2                  2001  bidir   Yes

       3.3.3.3                  2002  pim-sm  No

       3.3.3.4                        pim-sm  No

       3.3.3.5                  2002  pim-sm  Yes

 Anycast-RP information:

       RP address               Member address           State

       3.3.3.5                  1.1.0.1                  Active

       3.3.3.5                  1.1.0.2                  Local

       3.3.3.5                  1.2.0.1                  Remote

表1-12 display pim rp-info命令显示信息描述表

字段

描述

BSR RP address is

RP的IP地址

BSR RP information

BSR RP信息

Scope

域

Group/MaskLen

RP所服务的组播组

B

表示RP服务于双向PIM。如果不显示该字段，则表示RP服务于PIM-SM

RP address

RP的IP地址，local表示本地地址

Priority

RP的优先级

HoldTime

RP的超时时间

Uptime

RP已存在的时间

Expires

RP超时的剩余时间

Static RP information

静态RP信息

Static RP address is/RP address

静态RP的IP地址

Preferred

是否指定了静态RP优先

Configured ACL/ACL

静态RP所服务的组播组列表

Mode

为PIM-SM服务还是为双向PIM服务

RP mapping for this group

服务于当前组播组的RP的IP地址

Anycast-RP 3.3.3.5 members

Anycast-RP 3.3.3.5的成员

Member address

Anycast-RP成员的IP地址

State

Anycast-RP成员地址的来源：

·Active：表示本端激活接口的地址

·Local：表示本端未激活接口的地址

·Remote：表示远端的地址

Anycast-RP information

Anycast-RP信息

**PIM \-- PIM配置命令 \-- display pim statistics**

------------------------------------------------------------------------

**[display pim statistics**]命令用来显示PIM协议报文的统计信息。

【命令】

**[display pim** **statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示PIM协议报文的统计信息。

\<Sysname\> display pim statistics

 Received PIM packets: 3295

 Sent PIM packets    : 5975

                Valid       Invalid        Succeeded   Failed

     Hello    : 3128        0              4333        0

     Reg      : 14          0              0           0

     Reg-stop : 0           0              0           0

     JP       : 151         0              561         0

     BSM      : 0           0              1081        0

     Assert   : 0           0              0           0

     Graft    : 0           0              0           0

     Graft-ACK: 0           0              0           0

     C-RP     : 0           0              0           0

     SRM      : 0           0              0           0

     DF       : 0           0              0           0

表1-13 display pim statistics命令显示信息描述表

字段

描述

Received PIM packets

收到的PIM协议报文总数

Sent PIM packets

发出的PIM协议报文总数

Valid

收到的合法PIM协议报文数量

Invalid

收到的非法PIM协议报文数量

Succeeded

发送成功的PIM协议报文数量

Failed

发送失败的PIM协议报文数量

Hello

Hello报文统计

Reg

注册报文统计

Reg-stop

注册停止报文统计

JP

加入/剪枝报文统计

BSM

自举报文统计

Assert

断言报文统计

Graft

嫁接报文统计

Graft-ACK

嫁接应答报文统计

C-RP

C-RP报文统计

SRM

状态刷新报文统计

DF

指定转发者报文统计

**PIM \-- PIM配置命令 \-- hello-option dr-priority (PIM view)**

------------------------------------------------------------------------

**[hello-option dr-priority**]命令用来全局配置竞选DR的优先级。

**[undo hello-option dr-priority**]命令用来恢复缺省情况。

【命令】

**[hello-option dr-priority ***priority*]

**[undo hello-option dr-priority**]

【缺省情况】

竞选DR的优先级为1。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：指定竞选DR的优先级，取值范围为0～4294967295。数值越大，优先级越高。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置竞选DR的优先级为3。

\<Sysname\> system-view

Sysname pim

Sysname-pim hello-option dr-priority 3

【相关命令】

·**pim** **hello-option** **dr-priority**

**PIM \-- PIM配置命令 \-- hello-option holdtime (PIM view)**

------------------------------------------------------------------------

**[hello-option holdtime**]命令用来全局配置保持PIM邻居可达状态的时间。

**[undo hello-option holdtime**]命令用来恢复缺省情况。

【命令】

**[hello-option holdtime ***time*]

**[undo hello-option holdtime**]

【缺省情况】

保持PIM邻居可达状态的时间为105秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定保持PIM邻居可达状态的超时时间，取值范围为1～65535，单位为秒。如果指定为65535秒，则表示PIM邻居永远可达。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置保持PIM邻居可达状态的时间为120秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim hello-option holdtime 120

【相关命令】

·**pim hello-option holdtime**

**PIM \-- PIM配置命令 \-- hello-option lan-delay (PIM view)**

------------------------------------------------------------------------

**[hello-option lan-delay**]命令用来全局配置PIM报文在共享网段中的传输延迟。

**[undo hello-option lan-delay**]命令用来恢复缺省情况。

【命令】

**[hello-option lan-delay ***delay*]

**[undo hello-option lan-delay**]

【缺省情况】

PIM报文在共享网段中的传输延迟为500毫秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：指定PIM报文在共享网段中的传输延迟，取值范围为1～32767，单位为毫秒。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置PIM报文在共享网段中的传输延迟为200毫秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim hello-option lan-delay 200

【相关命令】

·**hello-option override-interval** (PIM view)

·**pim hello-option lan-delay**

·**pim hello-option override-interval**

**PIM \-- PIM配置命令 \-- hello-option neighbor-tracking (PIM view)**

------------------------------------------------------------------------

**[hello-option neighbor-tracking**]命令用来全局使能邻居跟踪功能，即禁止加入报文抑制能力。

**[undo hello-option neighbor-tracking**]命令用来恢复缺省情况。

【命令】

**[hello-option neighbor-tracking**]

**[undo hello-option neighbor-tracking**]

【缺省情况】

邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局使能邻居跟踪功能。

\<Sysname\> system-view

Sysname pim

Sysname-pim hello-option neighbor-tracking

【相关命令】

·**pim hello-option neighbor-tracking**

**PIM \-- PIM配置命令 \-- hello-option override-interval (PIM view)**

------------------------------------------------------------------------

**[hello-option override-interval**]命令用来全局配置剪枝否决时间。

**[undo hello-option override-interval**]命令用来恢复缺省情况。

【命令】

**[hello-option override-interval ***interval*]

**[undo hello-option override-interval**]

【缺省情况】

剪枝否决时间为2500毫秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定剪枝否决时间，取值范围为1～65535，单位为毫秒。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置剪枝否决时间为2000毫秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim hello-option override-interval 2000

【相关命令】

·**hello-option lan-delay** (PIM view)

·**pim hello-option lan-delay**

·**pim hello-option override-interval**

**PIM \-- PIM配置命令 \-- holdtime join-prune (PIM view)**

------------------------------------------------------------------------

**[holdtime join-prune**]命令用来全局配置加入/剪枝状态的保持时间。

**[undo holdtime join-prune**]命令用来恢复缺省情况。

【命令】

**[holdtime join-prune ***time*]

**[undo holdtime join-prune**]

【缺省情况】

加入/剪枝状态的保持时间为210秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定加入/剪枝状态的保持时间，取值范围为1～65535，单位为秒。

【使用指导】

·本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

\# 在公网实例中全局配置加入/剪枝状态的保持时间为280秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim holdtime join-prune 280

【相关命令】

·**pim holdtime join-prune**

·**timer join-prune** (PIM view)

**PIM \-- PIM配置命令 \-- jp-pkt-size (PIM view)**

------------------------------------------------------------------------

**[jp-pkt-size**]命令用来配置加入/剪枝报文的最大长度。

**[undo jp-pkt-size**]命令用来恢复缺省情况。

【命令】

**[jp-pkt-size ***size*]

**[undo jp-pkt-size**]

【缺省情况】

加入/剪枝报文的最大长度为8100字节。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：指定加入/剪枝报文的最大长度，取值范围为100～8100，单位为字节。

【举例】

\# 在公网实例中配置加入/剪枝报文的最大长度为1500字节。

\<Sysname\> system-view

Sysname pim

Sysname-pim jp-pkt-size 1500

**PIM \-- PIM配置命令 \-- pim**

------------------------------------------------------------------------

**[pim**]命令用来进入PIM视图。

**[undo pim**]命令用来清除PIM视图下的所有配置。

【命令】

**[pim** [ *vpn-instance* *vpn-instance-name* ]]

**[undo pim** [ *vpn-instance* *vpn-instance-name* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【举例】

\# 先使能公网实例中的IP组播路由，再进入公网实例的PIM视图。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname pim

Sysname-pim

\# 先使能VPN实例mvpn中的IP组播路由，再进入该VPN实例的PIM视图。

\<Sysname\> system-view

Sysname multicast routing vpn-instance mvpn

Sysname-mrib-mvpn quit

Sysname pim vpn-instance mvpn

Sysname-pim-mvpn

**PIM \-- PIM配置命令 \-- pim bfd enable**

------------------------------------------------------------------------

**[pim bfd enable**]命令用来使能PIM与BFD联动功能。

**[undo pim bfd enable**]命令用来关闭PIM与BFD联动功能。

【命令】

**[pim bfd enable**]

**[undo pim bfd enable**]

【缺省情况】

PIM与BFD联动功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在接口上先使能了PIM-DM或PIM-SM，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IP组播路由，在接口GigabitEthernet1/0/1上使能PIM-DM，并使能PIM与BFD联动功能。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim dm

Sysname-GigabitEthernet1/0/1 pim bfd enable

·交换应用：

\# 使能公网实例中的IP组播路由，在接口Vlan-interface100上使能PIM-DM，并使能PIM与BFD联动功能。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim dm

Sysname-Vlan-interface100 pim bfd enable

【相关命令】

·**pim dm**

·**pim sm**

**PIM \-- PIM配置命令 \-- pim bsr-boundary**

------------------------------------------------------------------------

**[pim bsr-boundary**]命令用来配置BSR的服务边界，即PIM-SM域的边界。

**[undo** **pim bsr-boundary**]命令用来删除BSR的服务边界。

【命令】

**[pim bsr-boundary**]

**[undo** **pim bsr-boundary**]

【缺省情况】

没有配置BSR的服务边界。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用：

\# 配置接口GigabitEthernet1/0/1为BSR的服务边界。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim bsr-boundary

·交换应用：

\# 配置接口Vlan-interface100为BSR的服务边界。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim bsr-boundary

【相关命令】

·**c-bsr** (PIM view)

·**multicast boundary**（IP组播命令参考/组播路由与转发）

**PIM \-- PIM配置命令 \-- pim dm**

------------------------------------------------------------------------

**[pim dm**]命令用来使能PIM-DM。

**[undo pim dm**]命令用来关闭PIM-DM。

【命令】

**[pim dm**]

**[undo pim dm**]

【缺省情况】

PIM-DM处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IP组播路由，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IP组播路由，并在接口GigabitEthernet1/0/1上使能PIM-DM。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim dm

·交换应用：

\# 使能公网实例中的IP组播路由，并在接口Vlan-interface100上使能PIM-DM。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim dm

【相关命令】

·**multicast routing**（IP组播命令参考/组播路由与转发）

**PIM \-- PIM配置命令 \-- pim hello-option dr-priority**

------------------------------------------------------------------------

**[pim hello-option dr-priority**]命令用来在接口上配置竞选DR的优先级。

**[undo pim hello-option dr-priority**]命令用来恢复缺省情况。

【命令】

**[pim hello-option dr-priority ***priority*]

**[undo pim hello-option dr-priority**]

【缺省情况】

竞选DR的优先级为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：指定竞选DR的优先级，取值范围为0～4294967295。数值越大，优先级越高。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置竞选DR的优先级为3。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim hello-option dr-priority 3

·交换应用：

\# 在接口Vlan-interface100上配置竞选DR的优先级为3。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim hello-option dr-priority 3

【相关命令】

·**hello-option dr-priority** (PIM view)

**PIM \-- PIM配置命令 \-- pim hello-option holdtime**

------------------------------------------------------------------------

**[pim hello-option holdtime**]命令用来在接口上配置保持PIM邻居的可达状态的时间。

**[undo pim hello-option holdtime**]命令用来恢复缺省情况。

【命令】

**[pim hello-option holdtime ***time*]

**[undo pim hello-option holdtime**]

【缺省情况】

保持PIM邻居可达状态的时间为105秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定保持PIM邻居可达状态的时间，取值范围为1～65535，单位为秒。如果指定为65535秒，则表示PIM邻居永远可达。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置保持PIM邻居可达状态的时间为120秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim hello-option holdtime 120

·交换应用：

\# 在接口Vlan-interface100上配置保持PIM邻居可达状态的时间为120秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim hello-option holdtime 120

【相关命令】

·**hello-option holdtime** (PIM view)

**PIM \-- PIM配置命令 \-- pim hello-option lan-delay**

------------------------------------------------------------------------

**[pim hello-option lan-delay**]命令用来在接口上配置PIM报文在共享网段中的传输延迟。

**[undo pim hello-option lan-delay**]命令用来恢复缺省情况。

【命令】

**[pim hello-option lan-delay ***delay*]

**[undo pim hello-option lan-delay**]

【缺省情况】

PIM报文在共享网段中的传输延迟为500毫秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：指定PIM报文在共享网段中的传输延迟，取值范围为1～32767，单位为毫秒。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置PIM报文在共享网段中的传输延迟为200毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim hello-option lan-delay 200

·交换应用：

\# 在接口Vlan-interface100上配置PIM报文在共享网段中的传输延迟为200毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim hello-option lan-delay 200

【相关命令】

·**hello-option lan-delay** (PIM view)

·**hello-option override-interval** (PIM view)

·**pim hello-option override-interval**

**PIM \-- PIM配置命令 \-- pim hello-option neighbor-tracking**

------------------------------------------------------------------------

**[pim hello-option neighbor-tracking**]命令用来在接口上使能邻居跟踪功能，即禁止加入报文抑制能力。

**[pim hello-option neighbor-tracking disable**]命令用来在全局使能了邻居跟踪功能的情况下，关闭当前接口上的邻居跟踪功能。

**[undo pim hello-option neighbor-tracking**]命令用来抵消上述两条命令的配置，即让接口与全局配置保持一致。

【命令】

**[pim hello-option neighbor-tracking**]

**[pim hello-option neighbor-tracking** **disable**]

**[undo pim hello-option neighbor-tracking**]

【缺省情况】

邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上使能邻居跟踪功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim hello-option neighbor-tracking

\# 在公网实例全局使能了邻居跟踪功能的情况下，关闭接口GigabitEthernet1/0/1上的邻居跟踪功能。

\<Sysname\> system-view

Sysname pim

Sysname-pim hello-option neighbor-tracking

Sysname-pim quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim hello-option neighbor-tracking disable

·交换应用：

\# 在接口Vlan-interface100上使能邻居跟踪功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim hello-option neighbor-tracking

\# 在公网实例全局使能了邻居跟踪功能的情况下，关闭接口Vlan-interface100上的邻居跟踪功能。

\<Sysname\> system-view

Sysname pim

Sysname-pim hello-option neighbor-tracking

Sysname-pim quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim hello-option neighbor-tracking disable

【相关命令】

·**hello-option neighbor-tracking** (PIM view)

**PIM \-- PIM配置命令 \-- pim hello-option override-interval**

------------------------------------------------------------------------

**[pim hello-option override-interval**]命令用来在接口上配置剪枝否决时间。

**[undo pim hello-option override-interval**]命令用来恢复缺省情况。

【命令】

**[pim hello-option override-interval ***interval*]

**[undo pim hello-option override-interval**]

【缺省情况】

剪枝否决时间为2500毫秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定剪枝否决时间，取值范围为1～65535，单位为毫秒。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置剪枝否决时间为2000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim hello-option override-interval 2000

·交换应用：

\# 在接口Vlan-interface100上配置剪枝否决时间为2000毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim hello-option override-interval 2000

【相关命令】

·**pim hello-option lan-delay**

·**hello-option lan-delay** (PIM view)

·**hello-option override-interval** (PIM view)

**PIM \-- PIM配置命令 \-- pim holdtime join-prune**

------------------------------------------------------------------------

**[pim holdtime join-prune**]命令用来在接口上配置加入/剪枝状态的保持时间。

**[undo pim holdtime join-prune**]命令用来恢复缺省情况。

【命令】

**[pim holdtime join-prune ***time*]

**[undo pim holdtime join-prune**]

【缺省情况】

加入/剪枝状态的保持时间为210秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定加入/剪枝状态的保持时间，取值范围为1～65535，单位为秒。

【使用指导】

·本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置加入/剪枝状态的保持时间为280秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim holdtime join-prune 280

·交换应用：

\# 在接口Vlan-interface100上配置加入/剪枝状态的保持时间为280秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim holdtime join-prune 280

【相关命令】

·**holdtime join-prune** (PIM view)

·**pim timer join-prune**

**PIM \-- PIM配置命令 \-- pim nbma-mode**

------------------------------------------------------------------------

**[pim nbma-mode**]命令用来在ADVPN隧道tunnel口上使能PIM-NBMA模式。

【命令】

**[pim nbma-mode**]

**[undo pim nbma-mode**]

【视图】

ADVPN隧道接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IP组播路由，接口上使能PIM SM协议，本命令才能生效。本命令不支持PIM DM模式。

【举例】

\# 使能公网实例中的IP组播路由，并在ADVPN隧道接口Tunnel 0上使能PIM-NBMA。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface Tunnel 0 mode advpn gre

Sysname- Tunnel0 pim sm

Sysname- Tunnel0 pim nbma-mode

**PIM \-- PIM配置命令 \-- pim neighbor-policy**

------------------------------------------------------------------------

**[pim neighbor-policy**]命令用来配置合法Hello报文的源地址范围，以防止Hello报文欺骗。

**[undo pim neighbor-policy**]命令用来恢复缺省情况。

【命令】

**[pim neighbor-policy** *acl-number*]

**[undo pim neighbor-policy**]

【缺省情况】

Hello报文的源地址范围不受任何限制，即认为所有收到的Hello报文都是合法的。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本ACL的编号，取值范围为2000～2999。

【使用指导】

ACL规则中的**source**参数用来指定合法Hello报文的源地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置合法Hello报文的源地址范围，只允许与来自网段10.1.1.0/24中的设备建立PIM邻居关系。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 10.1.1.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim neighbor-policy 2000{.TerminalDisplayChar}

·交换应用：

\# 在接口Vlan-interface100上配置合法Hello报文的源地址范围，只允许与来自网段10.1.1.0/24中的设备建立PIM邻居关系。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 10.1.1.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim neighbor-policy 2000{.TerminalDisplayChar}

**PIM \-- PIM配置命令 \-- pim require-genid**

------------------------------------------------------------------------

**[pim require-genid**]命令用来配置拒绝无Generation ID的Hello报文。

**[undo pim require-genid**]命令用来恢复缺省情况。

【命令】

**[pim require-genid**]

**[undo pim require-genid**]

【缺省情况】

接受无Generation ID的Hello报文。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用：

\# 配置接口GigabitEthernet1/0/1拒绝无Generation ID的Hello报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim require-genid

·交换应用：

\# 配置接口Vlan-interface100拒绝无Generation ID的Hello报文。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim require-genid

**PIM \-- PIM配置命令 \-- pim sm**

------------------------------------------------------------------------

**[pim sm**]命令用来使能PIM-SM。

**[undo pim sm**]命令用来关闭PIM-SM。

【命令】

**[pim sm**]

**[undo pim sm**]

【缺省情况】

PIM-SM处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IP组播路由，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IP组播路由，并在接口GigabitEthernet1/0/1上使能PIM-SM。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim sm

·交换应用：

\# 使能公网实例中的IP组播路由，并在接口Vlan-interface100上使能PIM-SM。

\<Sysname\> system-view

Sysname multicast routing

Sysname-mrib quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim sm

【相关命令】

·**multicast routing**（IP组播命令参考/组播路由与转发）

**PIM \-- PIM配置命令 \-- pim state-refresh-capable**

------------------------------------------------------------------------

**[pim state-refresh-capable**]命令用来使能状态刷新能力。

**[undo pim state-refresh-capable**]命令用来关闭状态刷新能力。

【命令】

**[pim state-refresh-capable**]

**[undo pim state-refresh-capable**]

【缺省情况】

状态刷新能力处于使能状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上关闭状态刷新能力。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo pim state-refresh-capable

·交换应用：

\# 在接口Vlan-interface100上关闭状态刷新能力。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 undo pim state-refresh-capable

【相关命令】

·**state-refresh-interval** (PIM view)

·**state-refresh-rate-limit** (PIM view)

·**state-refresh-ttl** (PIM view)

**PIM \-- PIM配置命令 \-- pim timer graft-retry**

------------------------------------------------------------------------

**[pim timer graft-retry**]命令用来配置嫁接报文的重传时间。

**[undo pim timer graft-retry**]命令用来恢复缺省情况。

【命令】

**[pim timer graft-retry ***interval*]

**[undo pim timer graft-retry**]

【缺省情况】

嫁接报文的重传时间为3秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定嫁接报文的重传时间，取值范围为1～65535，单位为秒。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置嫁接报文的重传时间为80秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim timer graft-retry 80

·交换应用：

\# 在接口Vlan-interface100上配置嫁接报文的重传时间为80秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim timer graft-retry 80

**PIM \-- PIM配置命令 \-- pim timer hello**

------------------------------------------------------------------------

**[pim timer hello**]命令用来在接口上配置发送Hello报文的时间间隔。

**[undo pim timer hello**]命令用来恢复缺省情况。

【命令】

**[pim timer hello** *interval*]

**[undo pim timer hello**]

【缺省情况】

发送Hello报文的时间间隔为30秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送Hello报文的时间间隔，取值范围为0～18000，单位为秒。0表示无穷大，即永不发送Hello报文。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置发送Hello报文的时间间隔为40秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim timer hello 40

·交换应用：

\# 在接口Vlan-interface100上配置发送Hello报文的时间间隔为40秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim timer hello 40

【相关命令】

·**timer hello** (PIM view)

**PIM \-- PIM配置命令 \-- pim timer join-prune**

------------------------------------------------------------------------

**[pim timer join-prune**]命令用来在接口上配置发送加入/剪枝报文的时间间隔。

**[undo pim timer join-prune**]命令用来恢复缺省情况。

【命令】

**[pim timer join-prune ***interval*]

**[undo pim timer join-prune**]

【缺省情况】

发送加入/剪枝报文的时间间隔为60秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送加入/剪枝报文的时间间隔，取值范围为0～18000，单位为秒。0表示无穷大，即永不发送加入/剪枝报文。

【使用指导】

·本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。

·PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置发送加入/剪枝报文的时间间隔为80秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim timer join-prune 80

·交换应用：

\# 在接口Vlan-interface100上配置发送加入/剪枝报文的时间间隔为80秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim timer join-prune 80

【相关命令】

·**pim holdtime join-prune**

·**timer join-prune** (PIM view)

**PIM \-- PIM配置命令 \-- pim triggered-hello-delay**

------------------------------------------------------------------------

**[pim triggered-hello-delay**]命令用来配置触发Hello报文的最大延迟时间。

**[undo pim triggered-hello-delay**]命令用来恢复缺省情况。

【命令】

**[pim triggered-hello-delay ***delay*]

**[undo pim triggered-hello-delay**]

【缺省情况】

触发Hello报文的最大延迟时间为5秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：指定触发Hello报文的最大延迟时间，取值范围为1～60，单位为秒。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置触发Hello报文的最大延迟时间为3秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pim triggered-hello-delay 3

·交换应用：

\# 在接口Vlan-interface100上配置触发Hello报文的最大延迟时间为3秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 pim triggered-hello-delay 3

**PIM \-- PIM配置命令 \-- register-policy (PIM view)**

------------------------------------------------------------------------

**[register-policy**]命令用来配置注册报文的过滤策略。

**[undo register-policy**]命令用来删除注册报文的过滤策略。

【命令】

**[register-policy ***acl-number*]

**[undo register-policy**]

【缺省情况】

没有配置注册报文的过滤策略。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4高级ACL的编号，取值范围为3000～3999。

【使用指导】

ACL规则中的**source**参数用来指定注册报文中的组播源地址范围，**destination**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。只有与该ACL规则中的**permit**语句匹配的注册报文才会被RP接受。

【举例】

\# 在公网实例中配置RP上对注册报文的过滤策略，只接收来自10.10.0.0/16网段的组播源发向225.1.0.0/16网段的组播组的注册报文。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule permit ip source 10.10.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255

Sysname-acl-ipv4-adv-3000 quit

Sysname pim

Sysname-pim register-policy 3000

**PIM \-- PIM配置命令 \-- register-suppression-timeout (PIM view)**

------------------------------------------------------------------------

**[register-suppression-timeout**]命令用来配置注册抑制时间。

**[undo** **register-suppression-timeout**]命令用来恢复缺省情况。

【命令】

**[register-suppression-timeout** *interval*]

**[undo** **register-suppression-timeout**]

【缺省情况】

注册抑制时间为60秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定注册抑制时间，取值范围为1～65535，单位为秒。

【举例】

\# 在公网实例中配置注册抑制时间为70秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim register-suppression-timeout 70

**PIM \-- PIM配置命令 \-- register-whole-checksum (PIM view)**

------------------------------------------------------------------------

**[register-whole-checksum**]命令用来配置根据注册报文的全部内容来计算校验和。

**[undo register-whole-checksum**]命令用来恢复缺省情况。

【命令】

**[register-whole-checksum**]

**[undo register-whole-checksum**]

【缺省情况】

仅根据注册报文头来计算校验和。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在公网实例中配置根据注册报文的全部内容来计算校验和。

\<Sysname\> system-view

Sysname pim

Sysname-pim register-whole-checksum

**PIM \-- PIM配置命令 \-- snmp-agent trap enable pim**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable** **pim**]命令用来开启PIM的告警功能。

**[undo** **snmp-agent** **trap** **enable** **pim**]命令用来关闭PIM的告警功能。

【命令】

**[snmp-agent**[ **trap** **enable** **pim** [ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** ] \*]]

**[undo**[ **snmp-agent** **trap** **enable** **pim** [ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** ] \*]]

【缺省情况】

PIM的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[candidate-bsr-win-election**]：表示C-BSR成功当选BSR的告警信息。

**[elected-bsr-lost-election**]：表示原BSR在新的选举中失败的告警信息。

**[neighbor-loss**]：表示邻居丢失的告警信息。

【使用指导】

如果未指定任何可选参数，表示开启或关闭PIM的全部告警功能。

开启了PIM的告警功能之后，PIM会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 关闭PIM的全部告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable pim

**PIM \-- PIM配置命令 \-- source-lifetime (PIM view)**

------------------------------------------------------------------------

**[source-lifetime**]命令用来配置组播源的生存时间。

**[undo source-lifetime**]命令用来恢复缺省情况。

【命令】

**[source-lifetime ***time*]

**[undo source-lifetime**]

【缺省情况】

组播源的生存时间为210秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定组播源的生存时间，取值范围为0～31536000，单位为秒。0表示无穷大，即组播源永不老化。

【举例】

\# 在公网实例中配置组播源的生存时间为200秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim source-lifetime 200

**PIM \-- PIM配置命令 \-- source-policy (PIM view)**

------------------------------------------------------------------------

**[source-policy**]命令用来配置组播数据过滤器。

**[undo source-policy**]命令用来删除组播数据过滤器。

【命令】

**[source-policy*** acl-number*]

**[undo source-policy**]

【缺省情况】

没有配置组播数据过滤器。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定IPv4基本或高级ACL的编号，取值范围为2000～3999。

【使用指导】

·对于IPv4基本ACL，该ACL规则中的**source**参数用来指定组播数据报文的源地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。

·对于IPv4高级ACL，该ACL规则中的**source**参数用来指定组播数据报文的源地址范围，**destination**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。

·重复执行本命令，新配置将覆盖旧配置。

【举例】

\# 在公网实例中配置接收组播源为10.10.1.2的组播数据，丢弃组播源为10.10.1.1的组播数据。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 10.10.1.2 0

Sysname-acl-ipv4-basic-2000 rule deny source 10.10.1.1 0

Sysname-acl-ipv4-basic-2000 quit

Sysname pim

Sysname-pim source-policy 2000

**PIM \-- PIM配置命令 \-- spt-switch-threshold (PIM view)**

------------------------------------------------------------------------

**[spt-switch-threshold**]命令用来配置发起SPT切换的条件。

**[undo spt-switch-threshold**]命令用来恢复缺省情况。

【命令】

**[spt-switch-threshold**[ { *traffic-rate* \| **immediacy** \| **infinity** } [ **group-policy** *acl-number* ]]]

**[undo spt-switch-threshold**[ [ *traffic-rate \|* **immediacy** \| **infinity** ]  **group-policy** *acl-number* ]]

【缺省情况】

设备收到第一个组播数据包后便立即向SPT切换。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[traffic-rate*]：指定发起SPT切换的组播数据转发速率阈值，取值范围为1～4194304，单位为kbps。交换机不支持本参数。

**[immediacy**]：表示立即发起SPT切换。

**[infinity**]：表示永不发起SPT切换。

**[group-policy** *acl-number*]：表示组策略列表中的一项，与该组策略匹配的组播组将应用本配置。*acl-number*表示IPv4基本ACL的编号，取值范围为2000～2999。如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则本配置将应用于所有组播组。

【使用指导】

·ACL规则中的**source**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·重复执行本命令，可以配置多个SPT切换阈值。但是，如果配置时所指定的ACL规则相同，则新配置将覆盖旧配置；如果针对同一组播组存在多条配置，则按照配置顺序匹配到的第一条配置将生效。

·由于某些设备无法将组播报文封装在注册报文中发给RP，因此在可能成为RP的设备上不建议配置永不发起SPT切换，以免导致组播报文转发失败。

【举例】

\# 在公网实例中配置发起SPT切换的组播数据转发速率阈值为4kbps。

\<Sysname\> system-view

Sysname pim

Sysname-pim spt-switch-threshold 4

\# 在接收者侧DR的公网实例中配置永不发起SPT切换。

\<Sysname\> system-view

Sysname pim

Sysname-pim spt-switch-threshold infinity

**PIM \-- PIM配置命令 \-- ssm-policy (PIM view)**

------------------------------------------------------------------------

**[ssm-policy**]命令用来配置SSM组播组的范围。

**[undo ssm-policy**]命令用来恢复缺省情况。

【命令】

**[ssm-policy ***acl-number*]

**[undo ssm-policy**]

【缺省情况】

SSM组播组的范围为232.0.0.0/8。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定基本ACL的编号，取值范围为2000～2999。

【使用指导】

·ACL规则中的**source**参数用来指定SSM组播组范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·通过本命令可以定义允许或拒绝的组播组的地址范围：如果匹配通过，则组播运行模式为PIM-SSM，否则为PIM-SM。

【举例】

\# 配置SSM组播组的范围232.1.0.0/16。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 232.1.0.0 0.0.255.255

Sysname-acl-ipv4-basic-2000 quit

Sysname pim

Sysname-pim ssm-policy 2000

**PIM \-- PIM配置命令 \-- state-refresh-interval (PIM view)**

------------------------------------------------------------------------

**[state-refresh-interval**]命令用来配置发送状态刷新报文的时间间隔。

**[undo state-refresh-interval**]命令用来恢复缺省情况。

【命令】

**[state-refresh-interval ***interval*]

**[undo state-refresh-interval**]

【缺省情况】

发送状态刷新报文的时间间隔为60秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送状态刷新报文的时间间隔，取值范围为1～255，单位为秒。

【举例】

\# 在公网实例中配置发送状态刷新报文的时间间隔为70秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim state-refresh-interval 70

【相关命令】

·**pim state-refresh-capable**

·**state-refresh-rate-limit** (PIM view)

·**state-refresh-ttl** (PIM view)

**PIM \-- PIM配置命令 \-- state-refresh-rate-limit (PIM view)**

------------------------------------------------------------------------

**[state-refresh-rate-limit**]命令用来配置接收新状态刷新报文的等待时间。

**[undo state-refresh-rate-limit**]命令用来恢复缺省情况。

【命令】

**[state-refresh-rate-limit ***time*]

**[undo state-refresh-rate-limit**]

【缺省情况】

接收新状态刷新报文的等待时间为30秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定接收新状态刷新报文的等待时间，取值范围为1～65535，单位为秒。

【举例】

\# 在公网实例中配置接收新状态刷新报文的等待时间为45秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim state-refresh-rate-limit 45

【相关命令】

·**pim state-refresh-capable**

·**state-refresh-interval** (PIM view)

·**state-refresh-ttl** (PIM view)

**PIM \-- PIM配置命令 \-- state-refresh-ttl (PIM view)**

------------------------------------------------------------------------

**[state-refresh-ttl**]命令用来配置状态刷新报文的TTL值。

**[undo state-refresh-ttl**]命令用来恢复缺省情况。

【命令】

**[state-refresh-ttl ***ttl-value*]

**[undo state-refresh-ttl**]

【缺省情况】

状态刷新报文的TTL值为255。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ttl-value*]：指定状态刷新报文的TTL值，取值范围为1～255。

【举例】

\# 在公网实例中配置状态刷新报文的TTL值为45。

\<Sysname\> system-view

Sysname pim

Sysname-pim state-refresh-ttl 45

【相关命令】

·**pim state-refresh-capable**

·**state-refresh-interval** (PIM view)

·**state-refresh-rate-limit** (PIM view)

**PIM \-- PIM配置命令 \-- static-rp (PIM view)**

------------------------------------------------------------------------

**[static-rp**]命令用来配置静态RP。

**[undo static-rp**]命令用来删除静态RP。

【命令】

**[static-rp*** rp-address*[ [ *acl-number* \| **bidir** \| **preferred** ] \*]]

**[undo static-rp ***rp-address*]

【缺省情况】

没有配置静态RP。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rp-address*]：指定静态RP的IP地址。该地址必须是实际存在且合法的单播IP地址，不能配置为127.0.0.0/8网段的地址；但对于服务于双向PIM的静态RP来说，允许将其IP地址指定为一个实际不存在的IP地址。

*[acl-number*]：指定IPv4基本ACL的编号，取值范围为2000～2999。如果指定了本参数，该静态RP将只为能够通过该过滤规则的组播组服务；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则该静态RP将为所有组播组服务。

**[bidir**]：指定该静态RP服务于双向PIM。如果未指定本参数，该静态RP将服务于PIM-SM。

**[preferred**]：表示当网络中同时存在动态RP和静态RP时，优先选择静态RP，只有当静态RP失效时，动态RP才能生效。如果未指定本参数，则表示优先选择动态RP，只有当未配置动态RP或动态RP失效时，静态RP才能生效。

【使用指导】

·作为静态RP的接口不必使能PIM。

·ACL规则中的**source**参数用来指定静态RP所服务的组播组范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·当某个静态RP引用的ACL规则发生变化时，需要为所有组播组重新选举RP。

·重复执行本命令，可以配置多个静态RP。但是，如果配置时所指定的静态RP地址或ACL规则相同，则新配置将覆盖旧配置；如果存在多个静态RP服务于同一组播组的情况，则选择IP地址最大的静态RP为该组服务。

【举例】

\# 在公网实例中配置IP地址为11.110.0.6的接口为静态RP，为组播组225.1.1.0/24提供服务，并优先选择静态RP。

\<Sysname\> system-view

Sysname acl basic 2001

Sysname-acl-ipv4-basic-2001 rule permit source 225.1.1.0 0.0.0.255

Sysname-acl-ipv4-basic-2001 quit

Sysname pim

Sysname-pim static-rp 11.110.0.6 2001 preferred

【相关命令】

·**display pim rp-info**

**PIM \-- PIM配置命令 \-- timer hello (PIM view)**

------------------------------------------------------------------------

**[timer hello**]命令用来全局配置发送Hello报文的时间间隔。

**[undo timer hello**]命令用来恢复缺省情况。

【命令】

**[timer hello** *interval*]

**[undo timer hello**]

【缺省情况】

发送Hello报文的时间间隔为30秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送Hello报文的时间间隔，取值范围为0～18000，单位为秒。0表示无穷大，即永不发送Hello报文。

【使用指导】

本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置发送Hello报文的时间间隔为40秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim timer hello 40

【相关命令】

·**pim timer hello**

**PIM \-- PIM配置命令 \-- timer join-prune (PIM view)**

------------------------------------------------------------------------

**[timer join-prune**]命令用来全局配置发送加入/剪枝报文的时间间隔。

**[undo timer join-prune**]命令用来恢复缺省情况。

【命令】

**[timer join-prune ***interval*]

**[undo timer join-prune**]

【缺省情况】

发送加入/剪枝报文的时间间隔为60秒。

【视图】

PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送加入/剪枝报文的时间间隔，取值范围为0～18000，单位为秒。0表示无穷大，即永不发送加入/剪枝报文。

【使用指导】

·本配置既可在PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。

·PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

\# 在公网实例中全局配置发送加入/剪枝报文的时间间隔为80秒。

\<Sysname\> system-view

Sysname pim

Sysname-pim timer join-prune 80

【相关命令】

·**holdtime join-prune** (PIM view)

·**pim timer join-prune**
