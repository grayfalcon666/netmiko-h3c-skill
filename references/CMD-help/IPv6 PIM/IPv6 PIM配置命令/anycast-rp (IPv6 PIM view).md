
**IPv6 PIM \-- IPv6 PIM配置命令 \-- anycast-rp (IPv6 PIM view)**

------------------------------------------------------------------------

**[anycast-rp**]命令用来配置Anycast-RP。

**[undo anycast-rp**]命令用来删除Anycast-RP。

【命令】

**[anycast-rp*** ipv6-anycast-rp-address ipv6-member-address*]

**[undo anycast-rp** *ipv6-anycast-rp-address ipv6-member-address*]

【缺省情况】

没有配置Anycast-RP。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-anycast-rp-address*]：指定Anycast-RP地址。必须是合法的IPv6全球单播地址。

*[ipv6-member-address*]：指定Anycast-RP成员地址。必须是合法的IPv6全球单播地址，不能与*ipv6-anycast-rp-address*相同。

【使用指导】

本命令可重复配置，配置时如果指定了相同的Anycast-RP地址，则将Anycast-RP成员地址添加到该Anycast-RP地址所属的Anycast-RP集中。

【举例】

\# 在公网实例中配置如下Anycast-RP集：Anycast-RP地址为1:1::0，两个成员的地址分别为1:1::1和1:2::1（前者为本地接口LoopBack1的地址）。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 anycast-rp 1:1::0 1:1::1

Sysname-pim6 anycast-rp 1:1::0 1:2::1

【相关命令】

·display ipv6 pim rp-info

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bidir-pim enable (IPv6 PIM view)**

------------------------------------------------------------------------

**[bidir-pim** **enable**]命令用来使能IPv6双向PIM。

**[undo** **bidir-pim** **enable**]命令用来关闭IPv6双向PIM。

【命令】

**[bidir-pim** **enable**]

**[undo** **bidir-pim** **enable**]

【缺省情况】

IPv6双向PIM处于关闭状态。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IPv6组播路由，本命令才能生效。

【举例】

\# 使能公网实例中的IPv6组播路由，并使能IPv6双向PIM。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname ipv6 pim

Sysname-pim6 bidir-pim enable

【相关命令】

·**ipv6 multicast routing**（IP组播命令参考/IPv6组播路由与转发）

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bidir-rp-limit (IPv6 PIM view)**

------------------------------------------------------------------------

**[bidir-rp-limit**]命令用来配置IPv6双向PIM RP的最大数目。

**[undo** **bidir-rp-limit**]命令用来恢复缺省情况。

【命令】

**[bidir-rp-limit** *limit*]

**[undo** **bidir-rp-limit**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[limit*]：指定IPv6双向PIM RP的最大数目，取值范围为1到系统所允许的最大值。系统所允许的最大值会随设备的不同而有所差别，请以设备的实际情况为准。

【使用指导】

由于IPv6双向PIM为每个RP都要在所有IPv6 PIM接口上进行DF选举，因此实际组网中不建议配置多个IPv6双向PIM RP。通过本命令可以限制IPv6双向PIM RP的数目，超出限制值的RP不会生效，仅能进行DF选举而无法指导转发。

【举例】

\# 在公网实例中配置IPv6双向PIM RP的最大数目为3。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 bidir-rp-limit 3

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bsm-fragment enable (IPv6 PIM view)**

------------------------------------------------------------------------

**[bsm-fragment** **enable**]命令用来使能自举报文语义分片功能。

**[undo** **bsm-fragment** **enable**]命令用来关闭自举报文语义分片功能。

【命令】

**[bsm-fragment** **enable**]

**[undo** **bsm-fragment** **enable**]

【缺省情况】

自举报文语义分片功能处于使能状态。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当IPv6 PIM-SM域或双向PIM域中存在不支持自举报文语义分片的设备时，请关闭本功能。

【举例】

\# 在公网实例中关闭自举报文语义分片功能。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 undo bsm-fragment enable

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bsr-policy (IPv6 PIM view)**

------------------------------------------------------------------------

**[bsr-policy**]命令用来配置合法的BSR地址范围，以防止BSR欺骗。

**[undo bsr-policy**]命令用来取消BSR地址范围的限制。

【命令】

**[bsr-policy** *acl6-number*]

undo bsr-policy

【缺省情况】

BSR的地址范围不受任何限制，即认为来自任意源的自举报文都是合法的。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本ACL的编号，取值范围为2000～2999。

【使用指导】

ACL规则中的**source**参数用来指定合法BSR的源地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

\# 在公网实例中配置合法的BSR地址范围，只允许网段2001::2/64中的设备充当BSR。

\<Sysname\> system-view

Sysname acl ipv6 number 2000

Sysname-acl6-basic-2000 rule permit source 2001::2 64

Sysname-acl6-basic-2000 quit

Sysname ipv6 pim

Sysname-pim6 bsr-policy 2000

【相关命令】

·**c-bsr** (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- c-bsr (IPv6 PIM view)**

------------------------------------------------------------------------

**[c-bsr**]命令用来配置C-BSR。

**[undo c-bsr**]命令用来删除C-BSR的相关配置。

【命令】

**[c-bsr** *ipv6-address* [ **scope** *scope-id*  [ **hash-length** *hash-length* \| **priority** *priority* ] \*]]

**[undo** **c-bsr** *ipv6-address* [ **scope** *scope-id* ]]

【缺省情况】

没有配置C-BSR。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定C-BSR的IPv6地址。

**[scope** *scope-id*]：指定IPv6管理域的编号，取值范围为3～15。如果未指定本参数，表示配置服务于Global域的C-BSR。

**[hash-length ***hash-length*]：指定哈希掩码长度，取值范围为0～128，缺省值为126。

**[priority** *priority*]：指定C-BSR的优先级，取值范围为0～255，缺省值为64。数值越大，优先级越高。

【使用指导】

·C-BSR的IPv6地址必须有对应的本地接口，且该接口上必须使能IPv6 PIM，否则配置不会生效。

·如果对同一个域多次执行本命令，新配置将覆盖旧配置；而针对不同域的C-BSR则允许指定相同的IPv6地址。

【举例】

\# 在公网实例中将IPv6地址为1101::1的设备配置为Global域的C-BSR。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 c-bsr 1101::1

**IPv6 PIM \-- IPv6 PIM配置命令 \-- c-rp (IPv6 PIM view)**

------------------------------------------------------------------------

**[c-rp**]命令用来配置C-RP。

**[undo c-rp**]命令用来删除C-RP的相关配置。

【命令】

**[c-rp ***ipv6-address *[[ **advertisement-interval** *adv-interval* \| { **group-policy** *acl6-number* \| **scope** *scope-id* } \| **holdtime** *hold-time* \| **priority** *priority* ] \*  **bidir** ]]

**[undo c-rp*** ipv6-address*]

【缺省情况】

没有配置C-RP。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：指定C-RP的IPv6地址。

**[advertisement-interval** *adv-interval*]：指定发送宣告报文的间隔时间，取值范围为1～65535，单位为秒，缺省值为60秒。

**[group-policy*** acl6-number*]：指定IPv6基本ACL的编号，取值范围为2000～2999。如果指定了本参数，该C-RP将只为ACL规则所允许的IPv6组播组服务；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则该C-RP将为所有IPv6组播组服务。

**[scope** *scope-id*]：指定IPv6管理域的编号，取值范围为3～15。

**[holdtime** *hold-time*]：指定C-RP的超时时间，取值范围为1～65535，单位为秒，缺省值为150秒。

**[priority** *priority*]：指定C-RP的优先级，取值范围为0～255，缺省值为192。该数值越大，优先级越低。

**[bidir**]：指定该C-RP服务于IPv6双向PIM。如果未指定本参数，该C-RP将服务于IPv6 PIM-SM。

【使用指导】

·C-RP的IPv6地址必须有对应的本地接口，且该接口上必须使能IPv6 PIM，否则配置不会生效。

·ACL规则中的**source**参数用来指定C-RP所服务的IPv6组播组范围（若指定的不是IPv6组播组地址，则此规则不生效），而其它可选参数都将被忽略。该ACL规则用来定义该C-RP所服务的IPv6组播组范围，只有**permit**的IPv6组播组才会作为RP的服务组范围通告出去。

·如果设备想要成为多个组范围的C-RP，则需要在配置**group-policy**所对应的ACL时将多个组范围用多个**rule**规则表示出来。

·如果对同一IPv6地址多次执行本命令，新配置将覆盖旧配置。

【举例】

\# 在公网实例中将IPv6地址为2001::1配置为组播组FF0E:0:1391::/96的C-RP，且C-RP的优先级为10。

\<Sysname\> system-view

Sysname acl ipv6 number 2000

Sysname-acl6-basic-2000 rule permit source ff0e:0:1391:: 96

Sysname-acl6-basic-2000 quit

Sysname ipv6 pim

Sysname-pim6 c-rp 2001::1 group-policy 2000 priority 10

**IPv6 PIM \-- IPv6 PIM配置命令 \-- crp-policy (IPv6 PIM view)**

------------------------------------------------------------------------

**[crp-policy**]命令用来配置合法的C-RP地址范围及其服务的IPv6组播组范围，以防止C-RP欺骗。

**[undo crp-policy**]命令用来取消C-RP地址范围及其服务的IPv6组播组范围的限制。

【命令】

**[crp-policy** *acl6-number*]

undo crp-policy

【缺省情况】

C-RP地址范围及其服务的IPv6组播组范围不受任何限制，即认为所有收到的C-RP报文都是合法的。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6高级ACL的编号，取值范围为3000～3999。

【使用指导】

·ACL规则中的**source**参数用来指定合法C-RP的IPv6地址范围，**destination**参数用来指定该C-RP所服务的IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·本命令在对C-RP所宣告的IPv6组播组范围进行过滤时，只取其前缀部分进行匹配。例如，C-RP宣告的IPv6组播组范围为FF0E:0:1::/96，如果其前缀部分"FF0E:0:1::"能匹配上本命令所引用的ACL规则，就认为整个IPv6组播组范围"FF0E:0:1::/96"都通过了过滤。

【举例】

\# 在公网实例中配置C-RP策略，只允许2001::2/64范围内的设备充当C-RP，且只允许其为FF03::101/64范围内的IPv6组播组服务。

\<Sysname\> system-view

Sysname acl ipv6 advanced 3000

Sysname-acl-ipv6-adv-3000 rule permit ipv6 source 2001::2 64 destination ff03::101 64

Sysname-acl-ipv6-adv-3000 quit

Sysname ipv6 pim

Sysname-pim6 crp-policy 3000

【相关命令】

·**c-rp** (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim bsr-info**

------------------------------------------------------------------------

**[display ipv6 pim bsr-info**]命令用来显示IPv6 PIM-SM域中的BSR信息。

【命令】

**[display ipv6 pim ** **vpn-instance** *vpn-instance-name* ] **bsr-info**

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

\# 显示公网实例IPv6 PIM-SM域中的BSR信息。

\<Sysname\> display ipv6 pim bsr-info

 Scope: non-scoped

     State: Accept Preferred

     Bootstrap timer: 00:01:44

     Elected BSR address: 12:12::1

       Priority: 64

       Hash mask length: 126

       Uptime: 00:21:56

 Scope: 5

     State: Accept Any

     Scope-zone expiry timer: 00:21:12

 Scope: 6

     State: Elected

     Bootstrap timer: 00:00:26

     Elected BSR address: 17:11::1

       Priority: 64

       Hash mask length: 126

       Uptime: 02:53:37

     Candidate BSR address: 17:11::1

       Priority: 64

       Hash mask length: 126

 Scope: 7

     State: Candidate

     Bootstrap timer: 00:01:56

     Elected BSR address: 61:37::1

       Priority: 64

       Hash mask length: 126

       Uptime: 02:53:32

     Candidate BSR address: 17:12::1

       Priority: 64

       Hash mask length: 126

 Scope: 8

     State: Pending

     Bootstrap timer: 00:00:07

     Candidate BSR address: 17:13::1

       Priority: 64

       Hash mask length: 126

表1-1 display ipv6 pim bsr-info命令显示信息描述表

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

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim claimed-route**

------------------------------------------------------------------------

**[display ipv6 pim claimed-route**]命令用来显示IPv6 PIM所使用的路由信息。

【命令】

**[display ipv6 pim** [ **vpn-instance** *vpn-instance-name*  **claimed-route**  *ipv6-source-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的路由信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的路由信息。

*[ipv6-source-address*]：组播源的IPv6地址，显示到达指定组播源的路由信息。如果未指定本参数，将显示IPv6 PIM所使用的所有路由信息。

【举例】

\# 显示IPv6 PIM在公网实例中使用的所有路由信息。

\<Sysname\> display ipv6 pim claimed-route

 RPF-route selecting rule: longest-match

 Route/mask: 7:11::/64 (unicast (direct))

     RPF interface: Vlan-interface2, RPF neighbor: 8::2

     Total number of (S,G) or (\*,G) dependent on this route entry: 4

     (7:11::10, ff1e::1)

     (7:11::10, ff1e::2)

     (7:11::10, ff1e::3)

     (\*, ff1e::4)

 Route/mask: 7:12::/64 (unicast)

     RPF interface: Vlan-interface2, RPF neighbor: 8::3,

     Total number of (S,G) or (\*,G) dependent on this route entry: 2

     (7:12::10, ff1e::1)

     (7:12::10, ff1e::2)

表1-2 display ipv6 pim claimed-route命令显示信息描述表

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

·mbgp：IPv6 MBGP路由

RPF interface

RPF接口的名称

RPF neighbor

RPF邻居的IPv6地址

Total number of (S,G) or (\*,G) dependent

on this route entry

基于此RPF路由的（S，G）或（\*，G）个数及列表

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim c-rp**

------------------------------------------------------------------------

**[display ipv6 pim c-rp**]命令用来显示IPv6 PIM-SM域中的C-RP信息。

【命令】

**[display ipv6 pim ** **vpn-instance** *vpn-instance-name* ] **c-rp**  **local**

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

\<Sysname\> display ipv6 pim c-rp

 Scope: non-scoped

     Group/MaskLen: FF00::/8 [B]

       C-RP address             Priority  HoldTime  Uptime    Expires

       8:12::2 (local)          192       150       00:27:48  00:01:43

     Group/MaskLen: FF23::/92 Expires: 00:02:07

\# 显示本地配置生效的C-RP信息。

\<Sysname\> display ipv6 pim c-rp local

 Candidate RP: 8:12::2(Loop1)

     Priority: 192

     HoldTime: 150

     Advertisement interval: 60

     Next advertisement scheduled at: 00:00:46

表1-3 display ipv6 pim c-rp命令显示信息描述表

字段

描述

Scope

域

Group/MaskLen

C-RP所服务的IPv6组播组

B

表示C-RP服务于IPv6双向PIM。如果未显示本字段，则表示服务于IPv6 PIM-SM

C-RP address

C-RP的IPv6地址，local表示本地地址

Priority

C-RP的优先级

HoldTime

C-RP的超时时间

Uptime

C-RP已存在的时间，w表示星期，d表示天，h表示小时

Expires

C-RP/组播组的超时剩余时间

Candidate RP

本地C-RP的IPv6地址

Advertisement interval

本地C-RP发送通告报文时间间隔

Next advertisement scheduled at

本地C-RP发送下一个通告报文的剩余时间

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim df-info**

------------------------------------------------------------------------

**[display** **ipv6** **pim** **df-info**]命令用来显示IPv6双向PIM的DF信息。

【命令】

**[display** **ipv6** **pim** [ **vpn-instance** *vpn-instance-name*  **df-info**  *ipv6-rp-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的IPv6双向PIM DF信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的IPv6双向PIM DF信息。

*[ipv6-rp-address*]：指定IPv6双向PIM的RP地址。

【举例】

\# 显示公网实例中IPv6双向PIM的DF信息。

\<Sysname\> display ipv6 pim df-info

RP address: 12::12

  Interface: GigabitEthernet0/0/4

    State     : Win        DF preference: 10

    DF metric : 1562       DF uptime    : 00:07:15

    DF address: FE80::202:FF:FE00:9 (local)

  Interface: Tunnel0, FE80::20:12

    State     : Lose       DF preference: 0

    DF metric : 0          DF uptime    : 00:07:15

    DF address: FE80::20:12

表1-3 display ipv6 pim df-info命令显示信息描述表

字段

描述

RP address

IPv6双向PIM的RP地址

Interface

接口名称，使能了nbma模式的ADVPN隧道口，显示远端连接IPv6 link-local地址

State

DF的选举状态：

Win：竞选DF成功

Lose：竞选DF落败

Offer：竞选DF的初始状态

Backoff：正在充当DF，但有更优的设备正在竞选DF

-：不参与DF竞选

DF preference

DF通告的路由优先级

DF metric

DF通告的路由度量值

DF uptime

DF已存在的时间

DF address

DF的IPv6地址，local表示本地地址

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim interface**

------------------------------------------------------------------------

**[display ipv6 pim interface**]命令用来显示接口上的IPv6 PIM信息。

【命令】

**[display ipv6 pim ** **vpn-instance** *vpn-instance-name* ] **interface**  *interface-type interface-number*   **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的IPv6 PIM信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的IPv6 PIM信息。

*[interface-type* *interface-number*]：显示指定接口上的IPv6 PIM信息。如果未指定本参数，将显示所有接口上的IPv6 PIM信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

【举例】

\# 显示公网实例所有接口上的IPv6 PIM概要信息。

\<Sysname\> display ipv6 pim interface

 Interface         NbrCnt  HelloInt  DR-Pri     DR-Address

 GE1/0/1           1       30        1          FE80::200:5EFF:FE04:8700

表1-4 display ipv6 pim interface命令显示信息描述表

字段

描述

Interface

接口名称

NbrCnt

IPv6 PIM邻居的数量

HelloInt

发送Hello报文的时间间隔

DR-Pri

竞选DR的优先级

DR-Address

DR的IPv6地址（链路本地地址）

\# 显示公网实例接口GigabitEthernet1/0/1上的IPv6 PIM详细信息。

\<Sysname\> display ipv6 pim interface gigabitethernet 1/0/1 verbose

Interface： GigabitEthernet1/0/1, FE80::200:5EFF:FE04:8700

     PIM version: 2

     PIM mode: Sparse

     PIM DR: FE80::200:AFF:FE01:101

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

表1-5 display ipv6 pim interface verbose命令显示信息描述表

字段

描述

Interface

接口名称与IPv6地址（链路本地地址）

PIM version

IPv6 PIM协议的版本号

PIM mode

IPv6 PIM协议的模式，是密集模式还是稀疏模式

PIM DR

DR的IPv6地址（链路本地地址）

PIM DR Priority (configured)

竞选DR优先级的配置值

PIM neighbor count

IPv6 PIM邻居的总数

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

保持IPv6 PIM邻居的可达状态的时间

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

该接口是否使能了IPv6 PIM与BFD联动功能

Number of routers on network not using DR priority

该接口所在网段上没有使用DR优先级字段的路由器数量

Number of routers on network not using LAN delay

该接口所在网段上未使用LAN-delay字段的路由器数量

Number of routers on network not using neighbor tracking

该接口所在网段上未使能邻居跟踪的路由器数量

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim nbma-link**

------------------------------------------------------------------------

**[display ipv6 pim nbma-link **]命令用来显示IPv6 PIM模块维护的ADVPN隧道接口对端的信息。

【命令】

**[display ipv6 pim ** **vpn-instance** *vpn-instance-name* ] **nbma-link**  **interface** { *interface-type interface-number* }

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的IPv6 PIM信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的IPv6 PIM信息。

**[interface** *interface-type* *interface-number*]：接口类型和接口编号，显示指定ADVPN隧道接口上IPv6 PIM维护对端的信息。如果未指定本参数，将显示所有ADVPN隧道接口上对端的信息。

【举例】

\#显示公网所有IPv6 PIM维护的ADVPN隧道接口上对端的信息。

\<Sysname\> display ipv6 pim nbma-link 

Interface: Tunnel1

  Number of links: 1

    Remote address: FE80::1

      Private index    : 0XCE000000

      Private interface: Multicast-NBMA0

Interface: Tunnel2

  Number of links: 1

    Remote address: FE80::2

      Private index    : 0XCE000001

      Private interface: Multicast-NBMA1

\#显示公网指定IPv6 PIM维护的ADVPN隧道接口上对端的信息。

\<Sysname\> display ipv6 pim nbma-link interface tunnel 1

Interface: Tunnel1

  Number of links: 1

    Remote address: FE80::1

      Private index    : 0XCE000000

  Private interface: Multicast-NBMA0

表1-6 display ipv6 pim nbma-link命令显示信息描述表

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

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim neighbor**

------------------------------------------------------------------------

**[display ipv6 pim neighbor**]命令用来显示IPv6 PIM邻居信息。

【命令】

**[display ipv6 pim **[ **vpn-instance** *vpn-instance-name*  **neighbor** [ *ipv6-neighbor-address* \| **interface** *interface-type interface-number* \| **verbose** ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的IPv6 PIM邻居信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的IPv6 PIM邻居信息。

*[ipv6-neighbor-address*]：IPv6 PIM邻居的IPv6地址，显示指定IPv6 PIM邻居的信息。如果未指定本参数，将显示所有IPv6 PIM邻居的信息。

**[interface** *interface-type* *interface-number*]：接口类型和接口编号，显示指定接口上的IPv6 PIM邻居信息。如果未指定本参数，将显示所有接口上的IPv6 PIM邻居信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

【举例】

\# 显示公网实例所有IPv6 PIM邻居的概要信息。

\<Sysname\> display ipv6 pim neighbor

 Total Number of Neighbors = 2

 Neighbor        Interface           Uptime   Expires  DR-Priority Mode

 FE80::A01:101:1 GE1/0/1             02:50:49 00:01:31 1           B

 FE80::A01:102:1 GE1/0/2             02:49:39 00:01:42 1

\# 显示公网实例中IPv6地址为FE80::A01:101:1的IPv6 PIM邻居的详细信息。

\<Sysname\> display ipv6 pim neighbor fe80::a01:101:1 verbose

 Neighbor: FE80::A01:101:1

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

     Secondary address(es):

     1::1

表1-7 display ipv6 pim neighbor命令显示信息描述表

字段

描述

Total Number of Neighbors

IPv6 PIM邻居的总数

Neighbor

IPv6 PIM邻居的IPv6主地址（链路本地地址）

Interface

IPv6 PIM邻居所在接口的名称

Uptime

IPv6 PIM邻居已存在的时间

Expires/Expiry time

IPv6 PIM邻居超时的剩余时间，never表示IPv6 PIM邻居永不超时，即永远可达

DR-Priority/DR Priority

IPv6 PIM邻居的优先级

Mode

IPv6 PIM邻居的模式，B表示IPv6双向PIM模式，显示为空则表示非IPv6双向PIM模式

Generation ID

IPv6 PIM邻居的Generation ID（状态随机数）

Holdtime

IPv6 PIM邻居的生存时间，forever表示IPv6 PIM邻居永远存在，即永远可达

LAN delay

IPv6 PIM报文在共享网段中的传输延迟

Override interval

剪枝否决的时间间隔

State refresh interval

状态刷新的时间间隔，只有当IPv6 PIM邻居工作在IPv6 PIM-DM模式下且具备状态刷新能力时才会显示本字段

Neighbor tracking

邻居跟踪功能是否使能

Bidirectional PIM

IPv6双向PIM是否使能

Secondary address(es)

IPv6 PIM邻居的IPv6从地址（非链路本地地址）

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim routing-table**

------------------------------------------------------------------------

**[display ipv6 pim routing-table**]命令用来显示IPv6 PIM路由表的内容。

【命令】

**[display ipv6 pim **[ **vpn-instance** *vpn-instance-name*  **routing-table**  *ipv6-group-address* [ *prefix-length*  \| *ipv6-source-address*  *prefix-length*  \| **flags** *flag-value* \| **fsm** \| **incoming-interface** *interface-type* *interface-number* \| **mode** *mode-type* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的IPv6 PIM路由项，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的IPv6 PIM路由项。

*[ipv6-group-address*]：IPv6组播组地址，显示指定IPv6组播组的IPv6 PIM路由项，取值范围为FFxy::/16，其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组的IPv6 PIM路由项。

*[ipv6-source-address*]：IPv6组播源地址，显示包含指定IPv6组播源的IPv6 PIM路由项。

*[prefix-length*]：指定IPv6组播组或IPv6组播源地址的前缀长度。对于IPv6组播组地址，其取值范围为8～128，缺省值为128；对于IPv6组播源地址，其取值范围为0～128，缺省值为128。

**[flags*** flag-value*]：IPv6 PIM标志，显示包含指定标志的IPv6 PIM路由项。如果未指定本参数，将显示包含所有标志的IPv6 PIM路由项。*flag-value*的取值及含义如下**：**

·**act**：表示已经有实际数据到达的IPv6 PIM路由项；

·**del**：表示计划删除的IPv6 PIM路由项；

·**exprune**：表示某些出接口被其它IPv6组播路由协议剪枝的IPv6 PIM路由项；

·**ext**：表示包含了由其它IPv6组播路由协议提供出接口的IPv6 PIM路由项；

·**loc**：表示在与IPv6组播源处于同一网段的设备上的IPv6 PIM路由项；

·**niif**：表示未确定入接口的IPv6 PIM路由项；

·**nonbr**：表示IPv6 PIM邻居查找失败的IPv6 PIM路由项；

·**rpt**：表示向RP方向发送过（S，G）RPT位剪枝的IPv6 PIM路由项；

·**spt**：表示SPT上的IPv6 PIM路由项；

·**swt**：表示正处于向SPT切换过程中的IPv6 PIM路由项；

·**wc**：表示带WC通配符的IPv6 PIM路由项。

**[fsm**]：显示有限状态机的详细信息。

**[incoming-interface** *interface-type interface-number*]：显示指定入接口的IPv6 PIM路由项。如果未指定本参数，将显示所有入接口的PIM路由项。

**[mode ***mode-type*]：IPv6 PIM模式，显示指定模式下的IPv6 PIM路由项。如果未指定本参数，将显示所有模式下的IPv6 PIM路由项。*mode-type*的取值及含义如下：

·**bidir**：表示IPv6双向PIM模式；

·**dm**：表示IPv6 PIM-DM模式；

·**sm**：表示IPv6 PIM-SM模式；

·**ssm**：表示IPv6 PIM-SSM模式。

**[outgoing-interface**[ { **exclude** \| **include** \| **match** } *interface-type* *interface-number*]]：显示指定出接口的IPv6 PIM路由项。其中，**exclude**表示不包含指定接口；**include**表示包含指定接口；**match**表示包含且仅包含指定接口。如果未指定本参数，将显示所有出接口的IPv6 PIM路由项。

【举例】

\# 显示公网实例IPv6 PIM路由表的内容。

\<Sysname\> display ipv6 pim routing-table

 Total 0 (\*, G) entry; 1 (S, G) entry

 (2001::2, FFE3::101)

     RP: FE80::A01:100:1

     Protocol: pim-sm, Flag: SPT LOC ACT

     UpTime: 02:54:43

     Upstream interface: GigabitEthernet1/0/1

         Upstream neighbor: NULL

         RPF prime neighbor: NULL

     Downstream interface information:

     Total number of downstream interfaces: 1

         1: GigabitEthernet1/0/2

             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

\# 显示公网实例IPv6 PIM路由表的状态机信息。

\<Sysname\> display ipv6 pim routing-table fsm

 Total 0 (\*, G) entries; 1 (S, G) entries

 Abbreviations for FSM states:

     NI - no info, J - joined, NJ - not joined, P - pruned,

     NP - not pruned, PP - prune pending, W - winner, L - loser,

     F - forwarding, AP - ack pending, DR - designated router,

     NDR - non-designated router, RCV - downstream receivers

 (2001::2, FFE3::101)

     RP: FE80::A01:100:1

     Protocol: pim-sm, Flag: SPT LOC ACT

     UpTime: 02:54:43

     Upstream interface: GigabitEthernet1/0/1

         Upstream neighbor: NULL

         RPF prime neighbor: NULL

         Join/Prune FSM: [SPT: J RPT: NP]

     Downstream interface information:

     Total number of downstream interfaces: 1

         1: GigabitEthernet1/0/2

             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

             DR state: [DR]

             Join/Prune FSM: [NI]

             Assert FSM: [NI]

     FSM information for non-downstream interfaces: None

\# 显示ADVPN应用组网IPv6 PIM路由表的内容。

\<Sysname\> display ipv6 pim routing-table

 Total 0 (\*, G) entries; 1 (S, G) entries

 (2001::2, FFE3::101)

     RP: FE80::A01:100:1

     Protocol: pim-sm, Flag: SPT LOC ACT

     UpTime: 02:54:43

     Upstream interface: Tunnel0, FE80::20:11

         Upstream neighbor: FE80::1

         RPF prime neighbor: FE80::1

     Downstream interface information:

     Total number of downstream interfaces: 1

         1: Tunnel0, FE80::20:12

             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

\# 显示ADVPN应用组网IPv6 PIM路由表的状态机信息。

\<Sysname\> display ipv6 pim routing-table fsm

 Total 0 (\*, G) entries; 1 (S, G) entries

 Abbreviations for FSM states:

     NI - no info, J - joined, NJ - not joined, P - pruned,

     NP - not pruned, PP - prune pending, W - winner, L - loser,

     F - forwarding, AP - ack pending, DR - designated router,

     NDR - non-designated router, RCV - downstream receivers

 (2001::2, FFE3::101)

     RP: FE80::A01:100:1

     Protocol: pim-sm, Flag: SPT LOC ACT

     UpTime: 02:54:43

     Upstream interface: Tunnel0, FE80::20:11

         Upstream neighbor: FE80::1

         RPF prime neighbor: FE80::1

         Join/Prune FSM: [SPT: J RPT: NP]

     Downstream interface information:

     Total number of downstream interfaces: 1

         1: Tunnel0, FE80::20:12

            Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

            DR state: [DR]

            Join/Prune FSM: [NI]

            Assert FSM: [NI]

     FSM information for non-downstream interfaces: None

表1-8 display ipv6 pim routing-table命令显示信息描述表

字段

描述

Total 0 (\*, G) entries; 1 (S, G) entries

IPv6 PIM路由表中（S，G）与（\*，G）表项的总数

Abbreviations for FSM states:

NI - no info, J - joined, NJ - not joined, P -- pruned

NP - not pruned, PP - prune pending, W - winner, L -- loser

F - forwarding, AP - ack pending, DR - designated router

NDR - non-designated router, RCV - downstream receivers

状态机的缩写：NI表示初始状态，J表示加入状态，P表示剪枝状态，NP表示未剪枝状态，PP表示剪枝未决状态，W表示断言当选，L表示断言落选，F表示转发状态，AP表示嫁接确认状态，DR表示指定路由器，NDR表示非指定路由器，RCV表示下游接收者

(2001::2, FFE3::101)

IPv6 PIM路由表中的（S，G）表项

RP

RP的地址

Protocol

IPv6 PIM的模式

Flag

IPv6 PIM路由表中（S，G）或（\*，G）表项的标志：

·ACT：表示已有实际数据到达

·DEL：表示计划要删除

·EXPRUNE：表示某些出接口被其它IPv6组播路由协议剪枝

·EXT：表示包含了由其它IPv6组播路由协议提供的出接口

·LOC：表示与IPv6组播源处于同一网段

·NIIF：表示未确定入接口

·NONBR：表示IPv6 PIM邻居查找失败

·RPT：表示向RP方向发送过（S，G）RPT位剪枝

·SPT：表示在SPT上

·SWT：表示正在向SPT切换

·WC：表示带WC通配符

Uptime

（S，G）或（\*，G）表项已存在的时间

Upstream interface

（S，G）或（\*，G）表项的入接口，使能了nbma模式的ADVPN隧道口，显示远端连接IPv6 link-local地址

Upstream neighbor

（S，G）或（\*，G）表项的上游邻居

RPF prime neighbor

（S，G）或（\*，G）表项的RPF邻居：

·对（\*，G）表项来说，当该路由器是RP时，（\*，G）表项的RPF邻居是NULL

·对（S，G）表项来说，当该路由器直连源时，（S，G）表项的RPF邻居是NULL

DR state

DR的状态

Join/Prune FSM

加入/剪枝状态机

Assert FSM

断言状态机

Downstream interface information

下游接口的信息，包括：

·下游接口的总数

·下游接口的名称

·下游接口使用的协议类型

·下游接口的存在时间

·下游接口的超时时间

·下游接口（ADVPN隧道口）对应的隧道远端的IPv6 link-local地址

FSM information for non-downstream interfaces

非下游接口的状态机信息

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim rp-info**

------------------------------------------------------------------------

**[display ipv6 pim rp-info**]命令用来显示IPv6 PIM-SM域中的RP的信息。

【命令】

**[display ipv6 pim ** **vpn-instance** *vpn-instance-name* ] **rp-info**  *ipv6-group-address*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例的RP信息，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的RP信息。

*[ipv6-group-address*]：IPv6组播组地址，显示指定IPv6组播组所对应的RP信息，取值范围为FFxy::/16（但不包括下列地址：FFx0::/16、FFx1::/16、FFx2::/16和FF0y::），其中x和y均代表0～F的任意一个十六进制数。如果未指定本参数，将显示所有IPv6组播组对应的RP信息。

【举例】

\# 显示公网实例中IPv6组播组FF0E::101所对应的RP信息。

\<Sysname\> display ipv6 pim rp-info ff0e::101

 BSR RP address is: 7:12::1

     Priority: 192

     HoldTime: 180

     Uptime: 03:01:10

     Expires: 00:02:30

 Static RP address is: 7:12::1

     Preferred: No

     Configured ACL: 2003

 RP mapping for this group is: 7:12::1 (local host)

 Anycast-RP 7:12::1 members:

     Member address           State

     1:1::1                   Active

     1:1::2                   Local

     1:2::1                   Remote

\# 显示所有IPv6组播组对应的RP信息。

\<Sysname\> display ipv6 pim rp-info

BSR RP information:

   Scope: non-scoped

Group/MaskLen: FF00::/8

       RP address               Priority  HoldTime  Uptime    Expires

       8:12::2 (local)          192       180       03:01:36  00:02:29

     Group/MaskLen: FF23::/92 [B]

       RP address               Priority  HoldTime  Uptime    Expires

       7:12::1 (local)          192       180       00:00:39  00:02:57

 Static RP information:

       RP address               ACL   Mode    Preferred

       3:3::1                   2000  pim-sm  No

       3:3::2                   2001  bidir   Yes

       3:3::3                   2002  pim-sm  No

       3:3::4                         pim-sm  No

       3:3::5                   2002  pim-sm  Yes

 Anycast-RP information:

       RP address               Member address           State

       3:3::1                   1:1::1                   Active

       3:3::1                   1:1::2                   Local

       3:3::1                   1:2::1                   Remote

表1-9 display ipv6 pim rp-info命令显示信息描述表

字段

描述

BSR RP address is

RP的IPv6地址

BSR RP information

BSR RP信息

Scope

域

Group/MaskLen

RP所服务的IPv6组播组

B

表示RP服务于IPv6双向PIM。如果不显示该字段，则表示RP服务于IPv6 PIM-SM

RP address

RP的IPv6地址，local表示本地地址

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

静态RP的IPv6地址

Preferred

是否指定了静态RP优先

Configured ACL/ACL

静态RP所服务的IPv6组播组列表

Mode

为IPv6 PIM-SM服务还是为IPv6双向PIM服务

RP mapping for this group

服务于当前组播组的RP的IPv6地址

Anycast-RP 7:12::1 members

Anycast-RP 7:12::1的成员

Member address

Anycast-RP成员的IPv6地址

State

Anycast-RP成员地址的来源：

·Active：表示本端激活接口的地址

·Local：表示本端未激活接口的地址

·Remote：表示远端的地址

Anycast-RP information

Anycast-RP信息

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim statistics**

------------------------------------------------------------------------

**[display ipv6 pim statistics**]命令用来显示IPv6 PIM协议报文的统计信息。

【命令】

**[display ipv6 pim** **statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示IPv6 PIM协议报文的统计信息。

\<Sysname\> display ipv6 pim statistics

 Received PIM packets: 3295

 Sent PIM packets    : 5975

                Valid       Invalid        Succeeded   Failed

     Hello    : 3128        0              4333        0

     Reg      : 14          0              0           0

     Reg-stop : 0           0              0           0

     JP       : 151         0              561         0

     BSM      : 0           0              1081        0

     Assert   : 0           0              0           0

     Graft    : 0           0              0           0

     Graft-ACK: 0           0              0           0

     C-RP     : 0           0              0           0

     SRM      : 0           0              0           0

     DF       : 0           0              0           0

表1-10 display ipv6 pim statistics命令显示信息描述表

字段

描述

Received PIM packets

收到的IPv6 PIM协议报文总数

Sent PIM packets

发出的IPv6 PIM协议报文总数

Valid

收到的合法IPv6 PIM协议报文数量

Invalid

收到的非法IPv6 PIM协议报文数量

Succeeded

发送成功的IPv6 PIM协议报文数量

Failed

发送失败的IPv6 PIM协议报文数量

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

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option dr-priority (IPv6 PIM view)**

------------------------------------------------------------------------

**[hello-option dr-priority**]命令用来全局配置竞选DR的优先级。

**[undo hello-option dr-priority**]命令用来恢复缺省情况。

【命令】

**[hello-option dr-priority** *priority*]

undo hello-option dr-priority

【缺省情况】

竞选DR的优先级为1。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：指定竞选DR的优先级，取值范围为0～4294967295。该数值越大，优先级越高。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置竞选DR的优先级为3。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 hello-option dr-priority 3

【相关命令】

·**ipv6 pim** **hello-option** **dr-priority**

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option holdtime (IPv6 PIM view)**

------------------------------------------------------------------------

**[hello-option holdtime**]命令用来全局配置保持IPv6 PIM邻居可达状态的时间。

**[undo hello-option holdtime**]命令用来恢复缺省情况。

【命令】

**[hello-option holdtime** *time*]

undo hello-option holdtime

【缺省情况】

保持IPv6 PIM邻居可达状态的时间为105秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定保持IPv6 PIM邻居可达状态的超时时间，取值范围为1～65535，单位为秒。如果指定为65535秒，则表示PIM邻居永远可达。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置保持IPv6 PIM邻居可达状态的时间为120秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 hello-option holdtime 120

【相关命令】

·ipv6 pim hello-option holdtime

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option lan-delay (IPv6 PIM view)**

------------------------------------------------------------------------

**[hello-option lan-delay**]命令用来全局配置IPv6 PIM报文在共享网段中的传输延迟。

**[undo hello-option lan-delay**]命令用来恢复缺省情况。

【命令】

**[hello-option lan-delay** *delay*]

undo hello-option lan-delay

【缺省情况】

IPv6 PIM报文在共享网段中的传输延迟为500毫秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：指定IPv6 PIM报文在共享网段中的传输延迟，取值范围为1～32767，单位为毫秒。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置IPv6 PIM报文在共享网段中的传输延迟为200毫秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 hello-option lan-delay 200

【相关命令】

·hello-option override-interval (IPv6 PIM view)

·ipv6 pim hello-option lan-delay

·ipv6 pim hello-option override-interval

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option neighbor-tracking (IPv6 PIM view)**

------------------------------------------------------------------------

**[hello-option neighbor-tracking**]命令用来全局使能邻居跟踪功能，即禁止加入报文抑制能力。

**[undo hello-option neighbor-tracking**]命令用来恢复缺省情况。

【命令】

hello-option neighbor-tracking

undo hello-option neighbor-tracking

【缺省情况】

邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局使能邻居跟踪功能。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 hello-option neighbor-tracking

【相关命令】

·ipv6 pim hello-option neighbor-tracking

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option override-interval (IPv6 PIM view)**

------------------------------------------------------------------------

**[hello-option override-interval**]命令用来全局配置剪枝否决时间。

**[undo hello-option override-interval**]命令用来恢复缺省情况。

【命令】

**[hello-option override-interval** *interval*]

undo hello-option override-interval

【缺省情况】

剪枝否决时间为2500毫秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定剪枝否决时间，取值范围为1～65535，单位为毫秒。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置剪枝否决时间为2000毫秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 hello-option override-interval 2000

【相关命令】

·hello-option lan-delay (IPv6 PIM view)

·ipv6 pim hello-option lan-delay

·ipv6 pim hello-option override-interval

**IPv6 PIM \-- IPv6 PIM配置命令 \-- holdtime join-prune (IPv6 PIM view)**

------------------------------------------------------------------------

**[holdtime join-prune**]命令用来全局配置加入/剪枝状态的保持时间。

**[undo holdtime join-prune**]命令用来恢复缺省情况。

【命令】

**[holdtime join-prune** *time*]

undo holdtime join-prune

【缺省情况】

加入/剪枝状态的保持时间为210秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定加入/剪枝状态的保持时间，取值范围为1～65535，单位为秒。

【使用指导】

·本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·IPv6 PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

\# 在公网实例中全局配置加入/剪枝状态的保持时间为280秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 holdtime join-prune 280

【相关命令】

·ipv6 pim holdtime join-prune

·timer join-prune (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim**

------------------------------------------------------------------------

**[ipv6 pim**]命令用来进入IPv6 PIM视图。

**[undo ipv6 pim**]命令用来清除IPv6 PIM视图下的所有配置。

【命令】

ipv6 pim  vpn-instance *vpn-instance-name*

undo ipv6 pim  vpn-instance *vpn-instance-name*

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

【举例】

\# 先使能公网实例中的IPv6组播路由，再进入公网实例的IPv6 PIM视图。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname ipv6 pim

Sysname-pim6

\# 先使能VPN实例mvpn中的IPv6组播路由，再进入该VPN实例的IPv6 PIM视图。

\<Sysname\> system-view

Sysname ipv6 multicast routing vpn-instance mvpn

Sysname-mrib6-mvpn quit

Sysname ipv6 pim vpn-instance mvpn

Sysname-pim6-mvpn

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim bfd enable**

------------------------------------------------------------------------

**[ipv6 pim bfd enable**]命令用来使能IPv6 PIM与BFD联动功能。

**[undo ipv6 pim bfd enable**]命令用来关闭IPv6 PIM与BFD联动功能。

【命令】

ipv6 pim bfd enable

undo ipv6 pim bfd enable

【缺省情况】

IPv6 PIM与BFD联动功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在接口上先使能了IPv6 PIM-DM或IPv6 PIM-SM，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IPv6组播路由，在接口GigabitEthernet1/0/1上使能IPv6 PIM-DM，并使能IPv6 PIM与BFD联动功能。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim dm

Sysname-GigabitEthernet1/0/1 ipv6 pim bfd enable

·交换应用：

\# 使能公网实例中的IPv6组播路由，在接口Vlan-interface100上使能IPv6 PIM-DM，并使能IPv6 PIM与BFD联动功能。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim dm

Sysname-Vlan-interface100 ipv6 pim bfd enable

【相关命令】

·ipv6 pim dm

·ipv6 pim sm

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim bsr-boundary**

------------------------------------------------------------------------

**[ipv6 pim bsr-boundary**]命令用来配置BSR的服务边界，即IPv6 PIM-SM域的边界。

**[undo** **ipv6 pim bsr-boundary**]命令用来删除BSR的服务边界。

【命令】

ipv6 pim bsr-boundary

**[undo** **ipv6 pim bsr-boundary**]

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

Sysname-GigabitEthernet1/0/1 ipv6 pim bsr-boundary

·交换应用：

\# 配置接口Vlan-interface100为BSR的服务边界。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim bsr-boundary

【相关命令】

·c-bsr (IPv6 PIM view)

·ipv6 multicast boundary（IP组播命令参考/IPv6组播路由与转发）

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim dm**

------------------------------------------------------------------------

**[ipv6 pim dm**]命令用来使能IPv6 PIM-DM。

**[undo ipv6 pim dm**]命令用来关闭IPv6 PIM-DM。

【命令】

ipv6 pim dm

undo ipv6 pim dm

【缺省情况】

IPv6 PIM-DM处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IPv6组播路由，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IPv6组播路由，并在接口GigabitEthernet1/0/1上使能IPv6 PIM-DM。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim dm

·交换应用：

\# 使能公网实例中的IPv6组播路由，并在接口Vlan-interface100上使能IPv6 PIM-DM。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim dm

【相关命令】

·**ipv6 multicast routing**（IP组播命令参考/IPv6组播路由与转发）

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option dr-priority**

------------------------------------------------------------------------

**[ipv6 pim hello-option dr-priority**]命令用来在接口上配置竞选DR的优先级。

**[undo ipv6 pim hello-option dr-priority**]命令用来恢复缺省情况。

【命令】

ipv6 pim hello-option dr-priority *priority*

undo ipv6 pim hello-option dr-priority

【缺省情况】

竞选DR的优先级为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：指定竞选DR的优先级，取值范围为0～4294967295。该数值越大，优先级越高。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置竞选DR的优先级为3。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim hello-option dr-priority 3

·交换应用：

\# 在接口Vlan-interface100上配置竞选DR的优先级为3。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim hello-option dr-priority 3

【相关命令】

·**hello-option dr-priority** (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option holdtime**

------------------------------------------------------------------------

**[ipv6 pim hello-option holdtime**]命令用来在接口上配置保持IPv6 PIM邻居的可达状态的时间。

**[undo ipv6 pim hello-option holdtime**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim hello-option holdtime** *time*]

undo ipv6 pim hello-option holdtime

【缺省情况】

保持IPv6 PIM邻居可达状态的时间为105秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定保持IPv6 PIM邻居可达状态的时间，取值范围为1～65535，单位为秒。如果指定为65535秒，则表示PIM邻居永远可达。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置保持PIM邻居可达状态的时间为120秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim hello-option holdtime 120

·交换应用：

\# 在接口Vlan-interface100上配置保持IPv6 PIM邻居可达状态的时间为120秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim hello-option holdtime 120

【相关命令】

·**hello-option holdtime** (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option lan-delay**

------------------------------------------------------------------------

**[ipv6 pim hello-option lan-delay**]命令用来在接口上配置IPv6 PIM报文在共享网段中的传输延迟。

**[undo ipv6 pim hello-option lan-delay**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim hello-option lan-delay** *delay*]

undo ipv6 pim hello-option lan-delay

【缺省情况】

IPv6 PIM报文在共享网段中的传输延迟为500毫秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[delay*]：指定IPv6 PIM报文在共享网段中的传输延迟，取值范围为1～32767，单位为毫秒。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置IPv6 PIM报文在共享网段中的传输延迟为200毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim hello-option lan-delay 200

·交换应用：

\# 在接口Vlan-interface100上配置IPv6 PIM报文在共享网段中的传输延迟为200毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim hello-option lan-delay 200

【相关命令】

·hello-option lan-delay (IPv6 PIM view)

·hello-option override-interval (IPv6 PIM view)

·ipv6 pim hello-option override-interval

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option neighbor-tracking**

------------------------------------------------------------------------

**[ipv6 pim hello-option neighbor-tracking**]命令用来在接口上使能邻居跟踪功能，即禁止加入报文抑制能力。

**[ipv6 pim hello-option neighbor-tracking disable**]命令用来在全局使能了邻居跟踪功能的情况下，关闭当前接口上的邻居跟踪功能。

**[undo ipv6 pim hello-option neighbor-tracking**]命令用来抵消上述两条命令的配置，即让接口与全局配置保持一致。

【命令】

ipv6 pim hello-option neighbor-tracking

**[ipv6 pim hello-option neighbor-tracking** **disable**]

undo ipv6 pim hello-option neighbor-tracking

【缺省情况】

邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上使能邻居跟踪功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim hello-option neighbor-tracking

\#在公网实例全局使能了邻居跟踪功能的情况下，关闭接口GigabitEthernet1/0/1上的邻居跟踪功能。

\<Sysname\> system-view

Sysnameipv6 pim

Sysname-pim6hello-option neighbor-tracking

Sysname-pim6quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim hello-option neighbor-tracking disable

·交换应用：

\# 在接口Vlan-interface100上使能邻居跟踪功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim hello-option neighbor-tracking

\# 在公网实例全局使能了邻居跟踪功能的情况下，关闭接口Vlan-interface100上的邻居跟踪功能。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 hello-option neighbor-tracking

Sysname-pim6 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim hello-option neighbor-tracking disable

【相关命令】

·**hello-option neighbor-tracking** (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option override-interval**

------------------------------------------------------------------------

**[ipv6 pim hello-option override-interval**]命令用来在接口上配置剪枝否决时间。

**[undo ipv6 pim hello-option override-interval**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim hello-option override-interval** *interval*]

undo ipv6 pim hello-option override-interval

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

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置剪枝否决时间为2000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim hello-option override-interval 2000

·交换应用：

\# 在接口Vlan-interface100上配置剪枝否决时间为2000毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim hello-option override-interval 2000

【相关命令】

·hello-option lan-delay (IPv6 PIM view)

·hello-option override-interval (IPv6 PIM view)

·ipv6 pim hello-option lan-delay

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim holdtime join-prune**

------------------------------------------------------------------------

**[ipv6 pim holdtime join-prune**]命令用来在接口上配置加入/剪枝状态的保持时间。

**[undo ipv6 pim holdtime join-prune**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim holdtime join-prune** *time*]

undo ipv6 pim holdtime join-prune

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

·本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·IPv6 PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置加入/剪枝状态的保持时间为280秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim holdtime join-prune 280

·交换应用：

\# 在接口Vlan-interface100上配置加入/剪枝状态的保持时间为280秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim holdtime join-prune 280

【相关命令】

·**holdtime join-prune** (IPv6 PIM view)

·**ipv6 pim timer join-prune**

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim nbma-mode**

------------------------------------------------------------------------

**[ipv6 pim nbma-mode**]命令用来在ADVPN隧道tunnel口上使能IPv6 PIM-NBMA模式。

【命令】

**[ipv6 pim nbma-mode**]

**[undo ipv6 pim nbma-mode**]

【视图】

ADVPN隧道接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IPv6组播路由，接口上使能IPv6 PIM SM协议，本命令才能生效。本命令不支持PIM DM模式。

【举例】

\# 使能公网实例中的IPv6组播路由，并在ADVPN隧道接口Tunnel 0上使能IPv6 PIM-NBMA。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib quit

Sysname interface Tunnel 0 mode advpn

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim neighbor-policy**

------------------------------------------------------------------------

**[ipv6 pim neighbor-policy**]命令用来配置合法Hello报文的源地址范围，以防止Hello报文欺骗。

**[undo ipv6 pim neighbor-policy**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim neighbor-policy** *acl6-number*]

**[undo ipv6 pim neighbor-policy**]

【缺省情况】

Hello报文的源地址范围不受任何限制，即认为所有收到的Hello报文都是合法的。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本ACL的编号，取值范围为2000～2999。

【使用指导】

ACL规则中的**source**参数用来指定合法Hello报文的源地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置合法Hello报文的源地址范围，只允许与来自网段FE80:101::101/64中的设备建立IPv6 PIM邻居关系。

\<Sysname\> system-view

Sysname acl ipv6 number 2000

Sysname-acl6-basic-2000 rule permit source fe80:101::101 64

Sysname-acl6-basic-2000 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim neighbor-policy 2000

·交换应用：

\# 在接口Vlan-interface100上配置合法Hello报文的源地址范围，只允许与来自网段FE80:101::101/64中的设备建立IPv6 PIM邻居关系。

\<Sysname\> system-view

Sysname acl ipv6 basic 2000

Sysname-acl-ipv6-basic-2000 rule permit source fe80:101::101 64

Sysname-acl-ipv6-basic-2000 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim neighbor-policy 2000{.TerminalDisplayChar}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim require-genid**

------------------------------------------------------------------------

**[ipv6 pim require-genid**]命令用来配置拒绝无Generation ID的Hello报文。

**[undo ipv6 pim require-genid**]命令用来恢复缺省情况。

【命令】

ipv6 pim require-genid

undo ipv6 pim require-genid

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

Sysname-GigabitEthernet1/0/1 ipv6 pim require-genid

·交换应用：

\# 配置接口Vlan-interface100拒绝无Generation ID的Hello报文。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim require-genid

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim sm**

------------------------------------------------------------------------

**[ipv6 pim sm**]命令用来使能IPv6 PIM-SM。

**[undo ipv6 pim sm**]命令用来关闭IPv6 PIM-SM。

【命令】

ipv6 pim sm

undo ipv6 pim sm

【缺省情况】

IPv6 PIM-SM处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在相应实例中先使能了IPv6组播路由，本命令才能生效。

【举例】

·路由应用：

\# 使能公网实例中的IPv6组播路由，并在接口GigabitEthernet1/0/1上使能IPv6 PIM-SM。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim sm

·交换应用：

\# 使能公网实例中的IPv6组播路由，并在接口Vlan-interface100上使能IPv6 PIM-SM。

\<Sysname\> system-view

Sysname ipv6 multicast routing

Sysname-mrib6 quit

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim sm

【相关命令】

·**ipv6 multicast routing**（IP组播命令参考/IPv6组播路由与转发）

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim state-refresh-capable**

------------------------------------------------------------------------

**[ipv6 pim state-refresh-capable**]命令用来使能状态刷新能力。

**[undo ipv6 pim state-refresh-capable**]命令用来关闭状态刷新能力。

【命令】

ipv6 pim state-refresh-capable

undo ipv6 pim state-refresh-capable

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

Sysname-GigabitEthernet1/0/1 undo ipv6 pim state-refresh-capable

·交换应用：

\# 在接口Vlan-interface100上关闭状态刷新能力。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 undo ipv6 pim state-refresh-capable

【相关命令】

·state-refresh-hoplimit (IPv6 PIM view)

·state-refresh-interval (IPv6 PIM view)

·state-refresh-rate-limit (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim timer graft-retry**

------------------------------------------------------------------------

**[ipv6 pim timer graft-retry**]命令用来配置嫁接报文的重传时间。

**[undo ipv6 pim timer graft-retry**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim timer graft-retry ***interval*]

undo ipv6 pimtimer graft-retry

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

Sysname-GigabitEthernet1/0/1 ipv6 pim timer graft-retry 80

·交换应用：

\# 在接口Vlan-interface100上配置嫁接报文的重传时间为80秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim timer graft-retry 80

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim timer hello**

------------------------------------------------------------------------

**[ipv6 pim timer hello**]命令用来在接口上配置发送Hello报文的时间间隔。

**[undo ipv6 pim timer hello**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim timer hello** *interval*]

undo ipv6 pim timer hello

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

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置发送Hello报文的时间间隔为40秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim timer hello 40

·交换应用：

\# 在接口Vlan-interface100上配置发送Hello报文的时间间隔为40秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim timer hello 40

【相关命令】

·**timer hello** (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim timer join-prune**

------------------------------------------------------------------------

**[ipv6 pim timer join-prune**]命令用来在接口上配置发送加入/剪枝报文的时间间隔。

**[undo ipv6 pim timer join-prune**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim timer join-prune**]*interval*

undo ipv6 pim timer join-prune

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

·本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。

·IPv6 PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

·路由应用：

\# 在接口GigabitEthernet1/0/1上配置发送加入/剪枝报文的时间间隔为80秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 pim timer join-prune 80

·交换应用：

\# 在接口Vlan-interface100上配置发送加入/剪枝报文的时间间隔为80秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim timer join-prune 80

【相关命令】

·ipv6 pim holdtime join-prune

·**timer join-prune** (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim triggered-hello-delay**

------------------------------------------------------------------------

**[ipv6 pim triggered-hello-delay**]命令用来配置触发Hello报文的最大延迟时间。

**[undo ipv6 pim triggered-hello-delay**]命令用来恢复缺省情况。

【命令】

**[ipv6 pim triggered-hello-delay** *delay*]

undo ipv6 pim triggered-hello-delay

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

Sysname-GigabitEthernet1/0/1 ipv6 pim triggered-hello-delay 3

·交换应用：

\# 在接口Vlan-interface100上配置触发Hello报文的最大延迟时间为3秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ipv6 pim triggered-hello-delay 3

**IPv6 PIM \-- IPv6 PIM配置命令 \-- jp-pkt-size (IPv6 PIM view)**

------------------------------------------------------------------------

**[jp-pkt-size**]命令用来配置加入/剪枝报文的最大长度。

**[undo jp-pkt-size**]命令用来恢复缺省情况。

【命令】

**[jp-pkt-size** *size*]

undo jp-pkt-size

【缺省情况】

加入/剪枝报文的最大长度为8100字节。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：指定加入/剪枝报文的最大长度，取值范围为100～64000，单位为字节。

【举例】

\# 在公网实例中配置加入/剪枝报文的最大长度为1500字节。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 jp-pkt-size 1500

**IPv6 PIM \-- IPv6 PIM配置命令 \-- register-policy (IPv6 PIM view)**

------------------------------------------------------------------------

**[register-policy**]命令用来配置注册报文的过滤策略。

**[undo register-policy**]命令用来删除注册报文的过滤策略。

【命令】

**[register-policy ***acl6-number*]

undo register-policy

【缺省情况】

没有配置注册报文的过滤策略。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6高级ACL的编号，取值范围为3000～3999。

【使用指导】

ACL规则中的**source**参数用来指定注册报文中的IPv6组播源地址范围，**destination**参数用来指定IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。只有与该ACL规则中的**permit**语句匹配的注册报文才会被RP接受。

【举例】

\# 在公网实例中配置RP上对注册报文的过滤策略，只接收来自3:1::/64网段的IPv6组播源发向FF0E:13::/64网段的IPv6组播组的注册报文。

\<Sysname\> system-view

Sysname acl ipv6 number 3000

Sysname-acl6-adv-3000 rule permit ipv6 source 3:1:: 64 destination ff0e:13:: 64

Sysname-acl6-adv-3000 quit

Sysname ipv6 pim

Sysname-pim6 register-policy 3000

**IPv6 PIM \-- IPv6 PIM配置命令 \-- register-suppression-timeout (IPv6 PIM view)**

------------------------------------------------------------------------

**[register-suppression-timeout**]命令用来配置注册抑制时间。

**[undo** **register-suppression-timeout**]命令用来恢复缺省情况。

【命令】

**[register-suppression-timeout** *interval*]

**[undo** **register-suppression-timeout**]

【缺省情况】

注册抑制时间为60秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定注册抑制时间，取值范围为1～65535，单位为秒。

【举例】

\# 在公网实例中配置注册抑制时间为70秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 register-suppression-timeout 70

**IPv6 PIM \-- IPv6 PIM配置命令 \-- register-whole-checksum (IPv6 PIM view)**

------------------------------------------------------------------------

**[register-whole-checksum**]命令用来配置根据注册报文的全部内容来计算校验和。

**[undo register-whole-checksum**]命令用来恢复缺省情况。

【命令】

register-whole-checksum

undo register-whole-checksum

【缺省情况】

仅根据注册报文头来计算校验和。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 在公网实例中配置根据注册报文的全部内容来计算校验和。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 register-whole-checksum

**IPv6 PIM \-- IPv6 PIM配置命令 \-- snmp-agent trap enable pim6**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable** **pim6**]命令用来开启IPv6 PIM的告警功能。

**[undo** **snmp-agent** **trap** **enable** **pim6**]命令用来关闭IPv6 PIM的告警功能。

【命令】

**[snmp-agent**[ **trap** **enable** **pim6** [ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** ] \*]]

**[undo**[ **snmp-agent** **trap** **enable** **pim6** [ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** ] \*]]

【缺省情况】

IPv6 PIM的告警功能处于开启状态。

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

如果未指定任何可选参数，表示开启或关闭IPv6 PIM的全部告警功能。

开启了IPv6 PIM的告警功能之后，IPv6 PIM会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 关闭IPv6 PIM的全部告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable pim6

**IPv6 PIM \-- IPv6 PIM配置命令 \-- source-lifetime (IPv6 PIM view)**

------------------------------------------------------------------------

**[source-lifetime**]命令用来配置IPv6组播源的生存时间。

**[undo source-lifetime**]命令用来恢复缺省情况。

【命令】

**[source-lifetime** *time*]

undo source-lifetime

【缺省情况】

IPv6组播源的生存时间为210秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定IPv6组播源的生存时间，取值范围为0～31536000，单位为秒。0表示无穷大，即IPv6组播源永不老化。

【举例】

\# 在公网实例中配置IPv6组播源的生存时间为200秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 source-lifetime 200

**IPv6 PIM \-- IPv6 PIM配置命令 \-- source-policy (IPv6 PIM view)**

------------------------------------------------------------------------

**[source-policy**]命令用来配置IPv6组播数据过滤器。

**[undo source-policy**]命令用来删除IPv6组播数据过滤器。

【命令】

**[source-policy** *acl6-number*]

undo source-policy

【缺省情况】

没有配置IPv6组播数据过滤器。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本或高级ACL的编号，取值范围为2000～3999。

【使用指导】

·对于IPv6基本ACL，该ACL规则中的**source**参数用来指定IPv6组播数据报文的源地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。

·对于IPv6高级ACL，该ACL规则中的**source**参数用来指定IPv6组播数据报文的源地址范围，**destination**参数用来指定组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。

·重复执行本命令，新配置将覆盖旧配置。

【举例】

\# 在公网实例中配置接收IPv6组播源3121::1的IPv6组播数据报文，丢弃IPv6组播源3121::2的IPv6组播数据报文。

\<Sysname\> system-view

Sysname acl ipv6 number 2000

Sysname-acl6-basic-2000 rule permit source 3121::1 128

Sysname-acl6-basic-2000 rule deny source 3121::2 128

Sysname-acl6-basic-2000 quit

Sysname ipv6 pim

Sysname-pim6 source-policy 2000

Sysname-pim6 quit

**IPv6 PIM \-- IPv6 PIM配置命令 \-- spt-switch-threshold (IPv6 PIM view)**

------------------------------------------------------------------------

**[spt-switch-threshold**]命令用来配置发起SPT切换的条件。

**[undo spt-switch-threshold**]命令用来恢复缺省情况。

【命令】

**[spt-switch-threshold**[ { *traffic-rate* \| **immediacy** \| **infinity** } [ **group-policy** *acl6-number* ]]]

**[undo spt-switch-threshold**[ [ *traffic-rate \|* **immediacy** \| **infinity** ]  **group-policy** *acl6-number* ]]

【缺省情况】

设备收到第一个IPv6组播数据包后便立即向SPT切换。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[traffic-rate*]：指定发起SPT切换的IPv6组播数据转发速率阈值，取值范围为1～4194304，单位为kbps。交换机不支持本参数。

**[immediacy**]：表示立即发起SPT切换。

**[infinity**]：表示永不发起SPT切换。

**[group-policy** *acl6-number*]：表示组策略列表中的一项，与该组策略匹配的IPv6组播组将应用本配置。*acl6-number*表示IPv6基本ACL的编号，取值范围为2000～2999。如果未指定本参数指定的ACL不存在或ACL中未配置有效规则，则本配置将应用于所有IPv6组播组。

【使用指导】

·ACL规则中的**source**参数用来指定IPv6组播组地址范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·重复执行本命令，可以配置多个SPT切换阈值。但是，如果配置时所指定的ACL规则相同，则新配置将覆盖旧配置；如果对同一IPv6组播组存在多条配置，则按照配置顺序匹配到的第一条配置将生效。

·由于某些设备无法将IPv6组播报文封装在注册报文中发给RP，因此在可能成为RP的设备上不建议配置永不发起SPT切换，以免导致IPv6组播报文转发失败。

【举例】

\# 在公网实例中配置发起SPT切换的IPv6组播数据转发速率阈值为4kbps。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 spt-switch-threshold 4

\# 在接收者侧DR的公网实例中配置永不发起SPT切换。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 spt-switch-threshold infinity

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ssm-policy (IPv6 PIM view)**

------------------------------------------------------------------------

**[ssm-policy**]命令用来配置IPv6 SSM组播组的范围。

**[undo ssm-policy**]命令用来恢复缺省情况。

【命令】

**[ssm-policy ***acl6-number*]

undo ssm-policy

【缺省情况】

IPv6 SSM组播组的范围为FF3x::/32，其中x表示任意合法的scope。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl6-number*]：指定IPv6基本ACL的编号，取值范围为2000～2999。

【使用指导】

·ACL规则中的**source**参数用来指定IPv6SSM组播组范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·通过本命令可以定义允许或拒绝的IPv6组播组的地址范围：如果匹配通过，则组播运行模式为IPv6 PIM-SSM，否则为IPv6 PIM-SM。

【举例】

\# 配置IPv6 SSM组播组的范围为FF3E:0:8192::/96。

\<Sysname\> system-view

Sysname acl ipv6 number 2000

Sysname-acl6-basic-2000 rule permit source ff3e:0:8192:: 96

Sysname-acl6-basic-2000 quit

Sysname ipv6 pim

Sysname-pim6 ssm-policy 2000

**IPv6 PIM \-- IPv6 PIM配置命令 \-- state-refresh-hoplimit (IPv6 PIM view)**

------------------------------------------------------------------------

**[state-refresh-hoplimit**]命令用来配置状态刷新报文的Hop Limit值。

**[undo state-refresh-hoplimit**]命令用来恢复缺省情况。

【命令】

**[state-refresh-hoplimit ***hoplimit-value*]

undo state-refresh-hoplimit

【缺省情况】

状态刷新报文的Hop Limit值为255。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[hoplimit-value*]：指定状态刷新报文的Hop Limit值，取值范围为1～255。

【举例】

\# 在公网实例中配置状态刷新报文的Hop Limit值为45。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 state-refresh-hoplimit 45

【相关命令】

·ipv6 pim state-refresh-capable

·state-refresh-interval (IPv6 PIM view)

·state-refresh-rate-limit (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- state-refresh-interval (IPv6 PIM view)**

------------------------------------------------------------------------

**[state-refresh-interval**]命令用来配置发送状态刷新报文的时间间隔。

**[undo state-refresh-interval**]命令用来恢复缺省情况。

【命令】

**[state-refresh-interval ***interval*]

undo state-refresh-interval

【缺省情况】

发送状态刷新报文的时间间隔为60秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送状态刷新报文的时间间隔，取值范围为1～255，单位为秒。

【举例】

\# 在公网实例中配置发送状态刷新报文的时间间隔为70秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 state-refresh-interval 70

【相关命令】

·ipv6 pim state-refresh-capable

·state-refresh-rate-limit (IPv6 PIM view)

·state-refresh-hoplimit (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- state-refresh-rate-limit (IPv6 PIM view)**

------------------------------------------------------------------------

**[state-refresh-rate-limit**]命令用来配置接收新状态刷新报文的等待时间。

**[undo state-refresh-rate-limit**]命令用来恢复缺省情况。

【命令】

**[state-refresh-rate-limit ***time*]

undo state-refresh-rate-limit

【缺省情况】

接收新状态刷新报文的等待时间为30秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定接收新状态刷新报文的等待时间，取值范围为1～65535，单位为秒。

【举例】

\# 在公网实例中配置接收新状态刷新报文的等待时间为45秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 state-refresh-rate-limit 45

【相关命令】

·ipv6 pim state-refresh-capable

·state-refresh-interval (IPv6 PIM view)

·state-refresh-hoplimit (IPv6 PIM view)

**IPv6 PIM \-- IPv6 PIM配置命令 \-- static-rp (IPv6 PIM view)**

------------------------------------------------------------------------

**[static-rp**]命令用来配置静态RP。

**[undo static-rp**]命令用来删除静态RP。

【命令】

**[static-rp*** ipv6-rp-address*[ [ *acl6-number* \| **bidir** \| **preferred** ] \*]]

**[undo static-rp** *ipv6-rp-address*]

【缺省情况】

没有配置静态RP。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-rp-address*]：指定静态RP的IPv6地址。该地址必须是合法的IPv6全球单播地址。

*[acl6-number*]：指定基本IPv6基本ACL的编号，取值范围为2000～2999。如果指定了本参数，该静态RP将只为能够通过该过滤规则的IPv6组播组服务；如果未指定本参数、指定的ACL不存在或ACL中未配置有效规则，则该静态RP将为所有IPv6组播组服务。

**[bidir**]：指定该静态RP服务于IPv6双向PIM。如果未指定本参数，该静态RP将服务于IPv6 PIM-SM。

**[preferred**]：表示当网络中同时存在动态RP和静态RP时，优先选择静态RP，只有当静态RP失效时，动态RP才能生效。如果未指定本参数，则表示优先选择动态RP，只有当未配置动态RP或动态RP失效时，静态RP才能生效。

【使用指导】

·作为静态RP的接口不必使能IPv6 PIM。

·ACL规则中的**source**参数用来指定静态RP所服务的IPv6组播组范围，若指定了**vpn-instance**参数则此规则不生效，而除**fragment**和**time-range**以外的其它可选参数都将被忽略。

·当某个静态RP引用的ACL规则发生变化时，需要为所有IPv6组播组重新选举RP。

·重复执行本命令，可以配置多个静态RP。但是，如果配置时所指定的静态RP地址或ACL规则相同，则新配置将覆盖旧配置；如果存在多个静态RP服务于同一组播组的情况，则选择IPv6地址最大的静态RP为该组服务。

【举例】

\# 在公网实例中配置IPv6地址为2001::2的接口为静态RP，为IPv6组播组FF03::101/64提供服务，并优先选择静态RP。

\<Sysname\> system-view

Sysname acl ipv6 number 2001

Sysname-acl6-basic-2001 rule permit source ff03::101 64

Sysname-acl6-basic-2001 quit

Sysname ipv6 pim

Sysname-pim6 static-rp 2001::2 2001 preferred

【相关命令】

·display ipv6 pim rp-info

**IPv6 PIM \-- IPv6 PIM配置命令 \-- timer hello (IPv6 PIM view)**

------------------------------------------------------------------------

**[timer hello**]命令用来全局配置发送Hello报文的时间间隔。

**[undo timer hello**]命令用来恢复缺省情况。

【命令】

**[timer hello**]*interval*

undo timer hello

【缺省情况】

发送Hello报文的时间间隔为30秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送Hello报文的时间间隔，取值范围为0～18000，单位为秒。0表示无穷大，即永不发送Hello报文。

【使用指导】

本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

【举例】

\# 在公网实例中全局配置发送Hello报文的时间间隔为40秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 timer hello 40

【相关命令】

·ipv6 pim timer hello

**IPv6 PIM \-- IPv6 PIM配置命令 \-- timer join-prune (IPv6 PIM view)**

------------------------------------------------------------------------

**[timer join-prune**]命令用来全局配置发送加入/剪枝报文的时间间隔。

**[undo timer join-prune**]命令用来恢复缺省情况。

【命令】

**[timer join-prune** *interval*]

undo timer join-prune

【缺省情况】

发送加入/剪枝报文的时间间隔为60秒。

【视图】

IPv6 PIM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定发送加入/剪枝报文的时间间隔，取值范围为0～18000，单位为秒。0表示无穷大，即永不发送加入/剪枝报文。

【使用指导】

·本配置既可在IPv6 PIM视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。

·本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。

·IPv6 PIM接口向上游邻居发送加入/剪枝报文的时间间隔必须小于加入/剪枝状态的保持时间，以免上游邻居老化超时。

【举例】

\# 在公网实例中全局配置发送加入/剪枝报文的时间间隔为80秒。

\<Sysname\> system-view

Sysname ipv6 pim

Sysname-pim6 timer join-prune 80

【相关命令】

·**holdtime join-prune** (IPv6 PIM view)

·**ipv6 pim timer join-prune**
