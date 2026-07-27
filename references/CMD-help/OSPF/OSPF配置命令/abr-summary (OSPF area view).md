<!-- CMD-INDEX
  abr-summary (OSPF area view)        | OSPF区域视图         | L95
  area (OSPF view)                    | OSPF视图           | L157
  asbr-summary                        | OSPF视图           | L201
  authentication-mode                 | OSPF区域视图         | L269
  bandwidth-reference (OSPF view)     | OSPF视图           | L353
  default                             | OSPF视图           | L415
  default-cost (OSPF area view)       | OSPF区域视图         | L465
  default-route-advertise (OSPF view) | OSPF视图           | L521
  discard-route                       | ]                | L585
  description (OSPF/OSPF area view)   | OSPF视图/OSPF区域视图  | L637
  display ospf                        | 任意视图             | L693
  display ospf abr-asbr               | 任意视图             | L1335
  display ospf abr-summary            | 任意视图             | L1449
  display ospf asbr-summary           | 任意视图             | L1591
  display ospf event-log              | 任意视图             | L1719
  display ospf fast-reroute lfa-candidate | 任意视图             | L2001
  display ospf graceful-restart       | 任意视图             | L2083
  display ospf interface              | 任意视图             | L2363
  display ospf lsdb                   | 任意视图             | L2587
  display ospf nexthop                | 任意视图             | L2867
  display ospf non-stop-routing status | 任意视图             | L2943
  display ospf peer                   | 任意视图             | L3019
  display ospf peer statistics        | 任意视图             | L3295
  display ospf request-queue          | 任意视图             | L3395
  display ospf retrans-queue          | 任意视图             | L3497
  display ospf routing                | 任意视图             | L3599
  display ospf spf-tree               | 任意视图             | L3853
  display ospf statistics             | 任意视图             | L4153
  display ospf vlink                  | 任意视图             | L4585
  display router id                   | 任意视图             | L4699
  dscp                                | OSPF视图           | L4731
  enable link-local-signaling         | OSPF视图           | L4773
  enable out-of-band-resynchronization | OSPF视图           | L4815
  event-log                           | OSPF视图           | L4867
  fast-reroute (OSPF view)            | OSPF视图           | L4915
  filter (OSPF area View)             | OSPF区域视图         | L4973
  filter-policy export (OSPF View)    | OSPF视图           | L5031
  filter-policy import (OSPF View)    | OSPF视图           | L5109
  graceful-restart (OSPF view)        | OSPF视图           | L5183
  graceful-restart helper enable      | OSPF视图           | L5267
  graceful-restart helper strict-lsa-checking | OSPF视图           | L5317
  graceful-restart interval (OSPF view) | OSPF视图           | L5363
  host-advertise                      | OSPF区域视图         | L5417
  import-route (OSPF view)            | OSPF视图           | L5463
  ispf                                | OSPF视图           | L5547
  log-peer-change                     | OSPF视图           | L5589
  lsa-arrival-interval                | OSPF视图           | L5631
  lsa-generation-interval             | OSPF视图           | L5683
  lsdb-overflow-interval              | OSPF视图           | L5739
  lsdb-overflow-limit                 | OSPF视图           | L5789
  maximum load-balancing (OSPF view)  | OSPF视图           | L5831
  network (OSPF area view)            | OSPF区域视图         | L5887
  non-stop-routing                    | OSPF视图           | L5941
  nssa                                | OSPF区域视图         | L5983
  opaque-capability enable            | OSPF视图           | L6055
  ospf                                | 系统视图             | L6097
  ospf area                           | 接口视图             | L6149
  ospf authentication-mode            | 接口视图             | L6217
  ospf bfd enable                     | 接口视图             | L6331
  ospf cost                           | 接口视图             | L6405
  ospf dr-priority                    | 接口视图             | L6467
  ospf fast-reroute lfa-backup        | 接口视图             | L6525
  ospf mib-binding                    | 系统视图             | L6583
  ospf mtu-enable                     | 接口视图             | L6629
  ospf network-type                   | 接口视图             | L6685
  ospf prefix-suppression             | 接口视图             | L6771
  ospf primary-path-detect bfd echo   | 接口视图             | L6837
  ospf timer dead                     | 接口视图             | L6945
  ospf timer hello                    | 接口视图             | L7007
  ospf timer poll                     | 接口视图             | L7069
  ospf timer retransmit               | 接口视图             | L7133
  ospf trans-delay                    | 接口视图             | L7193
  peer                                | OSPF视图           | L7251
  pic                                 | OSPF视图           | L7309
  preference                          | OSPF视图           | L7357
  prefix-priority                     | OSPF视图           | L7427
  prefix-suppression                  | OSPF视图           | L7485
  reset ospf statistics               | 用户视图             | L7541
  reset ospf event-log                | 用户视图             | L7575
  reset ospf process                  | 用户视图             | L7619
  reset ospf redistribution           | 用户视图             | L7669
  rfc1583 compatible                  | OSPF视图           | L7703
  router id                           | 系统视图             | L7755
  silent-interface (OSPF view)        | OSPF视图           | L7813
  snmp-agent trap enable ospf         | 系统视图             | L7873
  snmp trap rate-limit                | OSPF视图           | L7951
  spf-schedule-interval               | OSPF视图           | L7995
  stub (OSPF area view)               | OSPF区域视图         | L8049
  stub-router                         | OSPF视图           | L8105
  transmit-pacing                     | OSPF视图           | L8161
  vlink-peer (OSPF area view)         | OSPF区域视图         | L8205
-->

**OSPF \-- OSPF配置命令 \-- abr-summary (OSPF area view)**

------------------------------------------------------------------------

**[abr-summary**]命令用来配置ABR路由聚合。

**[undo abr-summary**]命令用来取消该配置。

【命令】

**[abr-summary**[ *ip-address* { *mask-length* \| *mask* } [ **advertise** \| **not-advertise** ]  **cost** *cost* ]]

**[undo**[ **abr-summary** *ip-address* { *mask-length* \| *mask* }]]

【缺省情况】

ABR不对路由进行聚合。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：聚合路由的目的IP地址。

*[mask-length*]：聚合路由的网络掩码长度，取值范围为0～32。

*[mask*]：聚合路由的网络掩码，点分十进制形式。

**[advertise **[\| **not-advertise**]]：是否发布这条聚合路由。缺省时发布聚合路由。

**[cost** *cost*]：聚合路由的开销，取值范围为1～16777215，缺省值为所有被聚合的路由中最大的开销值。

【使用指导】

本命令只适用于区域边界路由器（ABR），用来对某一个区域内的路由信息进行聚合。对于属于该聚合网段范围的路由，ABR向其它区域只发送一条聚合后的路由。一个区域可配置多条聚合网段，这样OSPF可对多个网段进行聚合。

当配置了**undo abr-summary**命令后，原来被聚合的路由又重新被发布。

【举例】

\# 将OSPF区域1中两个网段36.42.10.0/24和36.42.110.0/24的路由聚合成一条聚合路由36.42.0.0/16向其它区域发布。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 1

Sysname-ospf-100-area-0.0.0.1 network 36.42.10.0 0.0.0.255

Sysname-ospf-100-area-0.0.0.1 network 36.42.110.0 0.0.0.255

Sysname-ospf-100-area-0.0.0.1 abr-summary 36.42.0.0 255.255.0.0

**OSPF \-- OSPF配置命令 \-- area (OSPF view)**

------------------------------------------------------------------------

**[area**]命令用来创建OSPF区域，并进入OSPF区域视图。

**[undo area**]命令用来删除指定OSPF区域。

【命令】

**[area** *area-id*]

**[undo area ***area-id*]

【缺省情况】

没有配置OSPF区域。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[area-id*]：区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式。

【举例】

\# 创建OSPF区域0并进入OSPF区域视图。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 0

Sysname-ospf-100-area-0.0.0.0

**OSPF \-- OSPF配置命令 \-- asbr-summary**

------------------------------------------------------------------------

**[asbr-summary**]命令用来配置ASBR路由聚合。

**[undo asbr-summary**]命令用来取消该配置。

【命令】

**[asbr-summary**[ *ip-address* { *mask-length* \| *mask* } [ **cost** *cost* \| **not-advertise** \| **nssa-only** \| **tag** *tag* ] \*]]

**[undo asbr-summary ***ip-address *[{ *mask-length* \| *mask* }]]

【缺省情况】

ASBR不对路由进行聚合。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：聚合路由的目的IP地址。

*[mask-length*]：聚合路由的网络掩码长度，取值范围为0～32。

*[mask*]：聚合路由的网络掩码，点分十进制格式。

**[cost** *cost*]：聚合路由的开销，取值范围为1～16777214。如果未指定本参数，对于Type-1外部路由，*cost*取所有被聚合的路由中最大的开销值作为聚合路由的开销；对于Type-2外部路由，*cost*取所有被聚合的路由中最大的开销值加1作为聚合路由的开销。

**[not-advertise**]：不通告聚合路由。如果未指定本参数，将通告聚合路由。

**[nssa-only**]：设置Type-7 LSA的P比特位为不置位，即在对端路由器上不能转为Type-5 LSA。缺省时，Type-7 LSA的P比特位被置位，即在对端路由器上可以转为Type-5 LSA（如果本地路由器是ABR，则会检查骨干区域是否存在FULL状态的邻居，当FULL状态的邻居存在时，产生的Type-7 LSA中P比特位不置位）。

**[tag*** tag*]：聚合路由的标识，可以通过路由策略控制聚合路由的发布，取值范围为0～4294967295，缺省值为1。

【使用指导】

如果本地路由器是ASBR，对引入的聚合地址范围内的Type-5 LSA描述的路由进行聚合；当配置了NSSA区域时，对引入的聚合地址范围内的Type-7 LSA描述的路由进行聚合。

如果本地路由器同时是ASBR和ABR，并且是NSSA区域的转换路由器，将对由Type-7 LSA转化成的Type-5 LSA进行聚合处理；如果不是NSSA区域的转换路由器，则不进行聚合处理。

配置**asbr-summary**命令后，对处于聚合地址范围内的外部路由，本地路由器只向邻居路由器发布一条聚合后的路由；配置**undo asbr-summary**命令后，原来被聚合的外部路由将重新被发布。

【举例】

\# 配置OSPF对引入的路由进行聚合，聚合路由的标识为2，开销值为100。

\<Sysname\> system-view

Sysname ip route-static 10.2.1.0 24 null 0

Sysname ip route-static 10.2.2.0 24 null 0

Sysname ospf 100

Sysname-ospf-100 import-route static

Sysname-ospf-100 asbr-summary 10.2.0.0 255.255.0.0 tag 2 cost 100

**OSPF \-- OSPF配置命令 \-- authentication-mode**

------------------------------------------------------------------------

**[authentication-mode**]命令用来配置OSPF区域所使用的验证模式。

**[undo authentication-mode**]命令用来恢复缺省情况。

【命令】

MD5/HMAC-MD5验证模式：

**[authentication-mode**[ { **hmac-md5** \| **md5** } *key-id* { **cipher** \| **plain** } *password*]]

**[undo authentication-mode**[ [ { **hmac-md5** \| **md5** } *key-id* ]]]

简单验证模式：

**[authentication-mode simple****[{ **cipher** \| **plain** } *password*]]

**[undo authentication-mode**]

【缺省情况】

没有配置区域验证模式。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hmac-md5**]：HMAC-MD5验证模式。

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

*[key-id*]：验证字标识符，取值范围为0～255。

**[cipher**]：以密文形式设置密码。

**[plain**]：以明文形式设置密码。

*[password*]：验证密码，区分大小写。对于简单验证模式，如果以明文形式键入，则为1～8个字符的字符串；如果以密文形式键入，则为33～41个字符的字符串；对于MD5/HMAC-MD5验证模式，如果以明文形式键入，则为1～16个字符的字符串；如果以密文形式键入，则为33～53个字符的字符串。

【使用指导】

一个区域中所有路由器的验证模式和验证密码必须一致。

以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。

OSPF可指定区域下使用MD5/HMAC-MD5验证或简单验证两种方式，但不能同时指定；使用MD5/HMAC-MD5验证方式时，可配置多条MD5/HMAC-MD5验证命令，但*key-id*是唯一的，同一*key-id*只能配置一个验证字。

修改OSPF区域的MD5/HMAC-MD5验证字的步骤如下：

·首先在该区域配置新的MD5/HMAC-MD5验证字；此时若邻居设备尚未配置新的MD5/HMAC-MD5验证字，便会触发MD5/HMAC-MD5验证平滑迁移过程。在这个过程中，OSPF会发送分别携带各个MD5/HMAC-MD5验证字的多份报文，使得已配置新验证字的邻居设备、和尚未配置新验证字的邻居设备都能验证通过，保持邻居关系。

·然后在各个邻居设备上也都配置相同的新MD5/HMAC-MD5验证字；当本设备上收到所有邻居的携带新验证字的报文后，便会退出MD5/HMAC-MD5验证平滑迁移过程。

·最后在本设备和所有邻居上都删除旧的MD5/HMAC-MD5验证字；建议区域下不要保留多个MD5/HMAC-MD5验证字，每次MD5/HMAC-MD5验证字修改完毕后，应当及时删除旧的验证字，这样可以防止与持有旧验证字的系统继续通信、减少被攻击的可能，还可以减少验证迁移过程对系统、带宽的消耗。

【举例】

\# 配置OSPF区域0使用MD5明文验证模式，验证字标识符为15，验证密码为abc。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 0

Sysname-ospf-100-area-0.0.0.0 authentication-mode md5 15 plain abc

【相关命令】

·**ospf authentication-mode**

**OSPF \-- OSPF配置命令 \-- bandwidth-reference (OSPF view)**

------------------------------------------------------------------------

**[bandwidth-reference**]命令用来配置计算链路开销时所依据的带宽参考值。

**[undo bandwidth-reference**]命令用来恢复缺省情况。

【命令】

**[bandwidth-reference** *value*]

**[undo bandwidth-reference**]

【缺省情况】

计算链路开销时所依据的带宽参考值为100Mbps。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：计算链路开销时所依据的带宽参考值，取值范围为1～4294967，单位为Mbps。

【使用指导】

如果没有配置链路的开销值，OSPF根据链路带宽来计算开销值，接口开销＝带宽参考值÷接口期望带宽（接口期望带宽通过命令**bandwidth**进行配置，具体情况请参见接口分册命令参考中的介绍）。当计算出来的开销值大于65535时，开销取最大值65535；当计算出来的开销值小于1时，开销取最小值1。

常见接口开销的缺省值，如下：

·56kbps串口：缺省值为1785。

·64kbps串口：缺省值为1562。

·E1（2.048Mbps）：缺省值为48。

·Ethernet（100Mbps）：缺省值为1。

·Loopback接口：缺省值为0。

【举例】

\# 配置链路的带宽参考值为1000Mbps。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 bandwidth-reference 1000

【相关命令】

·**ospf ****cost**

**OSPF \-- OSPF配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来配置引入外部路由时的缺省参数，包括OSPF引入外部路由的开销、类型和标记。

**[undo default**]命令用来取消该配置。

【命令】

**[default **[{ **cost** *cost* \| **tag** *tag* \| **type** *type* } \*]]

**[undo default**[ { **cost** \| **tag** \| **type** } \*]]

【缺省情况】

OSPF引入的外部路由的度量值为1，引入的外部路由的标记为1，引入的外部路由类型为2。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cost*** cost*]：OSPF引入的外部路由的缺省度量值，*cost*的取值范围为0～16777214。

**[tag** *tag*]：外部路由的标记，*tag*的取值范围为0～4294967295。

**[type ***type*]：外部路由类型，*type*的取值范围为1～2。

【举例】

\# 配置外部路由开销、标记和类型的缺省值分别为10、100和2。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 default cost 10 tag 100 type 2

【相关命令】

·**import-route**

**OSPF \-- OSPF配置命令 \-- default-cost (OSPF area view)**

------------------------------------------------------------------------

**[default-cost**]命令用来配置发送到Stub区域或NSSA区域的缺省路由的开销。

**[undo default-cost**]命令用来恢复缺省情况。

【命令】

**[default-cost** *cost*]

**[undo default-cost**]

【缺省情况】

发送到Stub区域或NSSA区域的缺省路由的开销为1。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cost*]：发送到Stub区域或NSSA区域的缺省路由的开销，取值范围为0～16777214。

【使用指导】

该命令只有在Stub区域的ABR或NSSA区域的ABR/ASBR上配置才能生效。

【举例】

\# 将区域1设置成Stub区域，配置发送到该Stub区域的缺省路由的开销为20。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 1

Sysname-ospf-100-area-0.0.0.1 stub

Sysname-ospf-100-area-0.0.0.1 default-cost 20

【相关命令】

·**nssa**

·**stub**

**OSPF \-- OSPF配置命令 \-- default-route-advertise (OSPF view)**

------------------------------------------------------------------------

**[default-route-advertise**]命令用来将缺省路由引入到OSPF路由区域。

**[undo default-route-advertise**]命令用来恢复缺省情况。

【命令】

**[default-route-advertise**[ [ [ [ **always** \| **permit-calculate-other** ] \| **cost** *cost* \| **route-policy** *route-policy-name* \| **type** *type* ] \* \| **summary cost** *cost* ]]]

**[undo default-route-advertise**]

【缺省情况】

没有引入缺省路由。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[always**]：如果当前路由器的路由表中没有缺省路由，使用此参数可产生一个描述缺省路由的Type-5 LSA发布出去。如果没有指定该关键字，仅当本地路由器的路由表中存在缺省路由时，才可以产生一个描述缺省路由的Type-5 LSA发布出去。

**[permit-calculate-other**]：当路由器产生并发布了一个描述缺省路由的Type-5 LSA时，指定此参数的路由器仍然会计算来自于其他路由器的缺省路由，未指定此参数的路由器不再计算来自其他路由器的缺省路由。当路由器没有产生一个描述缺省路由的Type-5 LSA时，无论是否指定此参数，路由器都会计算来自其他路由器的缺省路由。

**[cost** *cost*]：该缺省路由的度量值，取值范围为0～16777214，如果没有指定，缺省路由的度量值将取**default cost**命令配置的值。

**[route-policy** *route-policy-name*]：路由策略名，为1～63个字符的字符串，区分大小写。只有当前路由器的路由表中存在缺省路由，并且有路由匹配*route-policy-name*指定的路由策略，才可以产生一个描述缺省路由的Type-5 LSA发布出去，指定的路由策略会影响Type-5 LSA中的值。如果同时指定**always**参数，不论当前路由器的路由表中是否有缺省路由，只要有路由匹配指定的路由策略，就将产生一个描述缺省路由的Type-5 LSA发布出去，指定的路由策略会影响Type-5 LSA中的值。

**[type ***type*]：该Type-5 LSA的类型，取值范围为1～2，如果没有指定，Type-5 LSA的缺省类型将取**default type**命令配置的值。

**[summary**]：发布指定缺省路由的Type-3 LSA。在选用该参数时，必须首先使能VPN，否则路由不能发布。

【使用指导】

使用**import-route**命令不能引入缺省路由，如果要引入缺省路由，必须使用该命令。当本地路由器的路由表中没有缺省路由时，要产生一个描述缺省路由的Type-5 LSA应使用**always**关键字。

**[default-route-advertise summary cost**]命令仅在VPN中应用，以Type-3 LSA引入缺省路由，PE路由器会将引入的缺省路由发布给CE路由器。

【举例】

\# 不管本地路由器的路由表中是否存在缺省路由，将产生的缺省路由引入到OSPF路由区域（本地路由器没有缺省路由）。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 default-route-advertise always

【相关命令】

·**default**

·**import-route**

**OSPF \-- OSPF配置命令 \-- discard-route**

------------------------------------------------------------------------

**[discard-route**]命令用来配置NULL0路由以及NULL0路由的优先级。

**[undo discard-route**]命令用来取消该配置。

【命令】

**[discard-route**]**[external** *[preference*[ \| ]**suppression**[}[ \| ]]**internal** *[preference*[ \| ]**suppression**} } \*

**[undo discard-route**]\**[external**[ \| ]**internal**  ]\*

【缺省情况】]

产生引入聚合]NULL0路由和区域间聚合NULL0路由，且NULL0路由优先级为255。

【视图】]

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[external**]：引入聚合NULL0路由。

*[preference*]：引入聚合NULL0路由的优先级，取值范围为1～255。

**[suppression**]：抑制产生引入聚合NULL0路由。

**[internal**]：区域间聚合NULL0路由。

*[preference*]：区域间聚合NULL0路由的优先级，取值范围为1～255。

**[suppression**]：抑制产生区域间聚合NULL0路由。

【举例】

\# 配置引入聚合路由的NULL0路由的优先级为100，区域间聚合NULL0路由的优先级为200。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 discard-route external 100 internal 200

**OSPF \-- OSPF配置命令 \-- description (OSPF/OSPF area view)**

------------------------------------------------------------------------

**[description**]命令用来配置OSPF进程/OSPF区域的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *description*]

**[undo** **description**]

【缺省情况】

没有配置OSPF进程和区域的描述信息。

【视图】

OSPF视图/OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[description*]：在OSPF视图下，该参数用来描述OSPF进程；在OSPF区域视图下，该参数用来描述OSPF区域，为1～80个字符的字符串。

【使用指导】

本命令仅仅用于标识某OSPF进程/OSPF区域，并无特别的意义和用途。

【举例】

\# 配置OSPF进程100的描述信息为"abc"。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 description abc

\# 配置OSPF区域0的描述信息为"bone area"。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 0

Sysname-ospf-100-area-0.0.0.0 description bone area

**OSPF \-- OSPF配置命令 \-- display ospf**

------------------------------------------------------------------------

**[display ospf**]命令用来显示OSPF的进程信息。

【命令】

**[display ospf ** *process-id* ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF的进程信息。

**[verbose**]：显示OSPF进程的详细信息。如果未指定本参数，将显示OSPF进程的概要信息。

【举例】

\# 显示OSPF的详细信息。

\<Sysname\> display ospf verbose

          OSPF Process 1 with Router ID 192.168.1.2

                  OSPF Protocol Information

 RouterID: 192.168.1.2      Router type:  NSSA

 Route tag: 0

 Multi-VPN-Instance is not enabled

 Ext-community type: domain ID 0x105, route type 0x8000, router ID 0x8001

 Domain ID: 0.0.0.0:23

 Opaque capable

 Originating router-LSAs with maximum metric

    Condition: On startup while BGP is converging, State: Inactive

    Advertise stub links with maximum metric in router-LSAs

    Advertise summary-LSAs with metric 16711680

    Advertise external-LSAs with metric 16711680

 ISPF is enabled

 SPF-schedule-interval: 5 50 200

 LSA generation interval: 5

 LSA arrival interval: 1000

 Transmit pacing: Interval: 20 Count: 3

 Default ASE parameters: Metric: 1 Tag: 1 Type: 2

 Route preference: 10

 ASE route preference: 150

 SPF computation count: 22

 RFC 1583 compatible

 Graceful restart interval: 120

 SNMP trap rate limit interval: 2  Count: 300

 This process is currently bound to MIB

 Area count: 1   NSSA area count: 1

 Normal areas with up interfaces: 0

 NSSA areas with up interfaces: 1

 Up interfaces: 1

 ExChange/Loading neighbors: 0

 Full neighbors:3

 Calculation trigger type: Full

 Current calculation type: SPF calculation

 Current calculation phase: Calculation area topology

 Process reset state: N/A

 Current reset type: N/A

 Next reset type: N/A

 Reset prepare message replied: -/-/-/-

 Reset process message replied: -/-/-/-

 Reset phase of module：

   M-N/A, P-N/A, L-N/A, C-N/A, R-N/A

 Area: 0.0.0.1          (MPLS TE  not enabled)

 Authtype: None    Area flag: NSSA

 7/5 translator state: Disabled

 7/5 translate stability timer interval: 0

 SPF scheduled count: 5

 ExChange/Loading neighbors: 0

 Up interfaces: 1

 Interface: 192.168.1.2 (GigabitEthernet1/0/1)

 Cost: 1       State: DR        Type: Broadcast    MTU: 1500

 Priority: 1

 Designated router: 192.168.1.2

 Backup designated router: 192.168.1.1

 Timers: Hello 10 , Dead 40 , Poll  40 , Retransmit 5 , Transmit Delay 1

 FRR backup: Enabled

 Enabled by network configuration

表1-1 display ospf verbose命令显示信息描述表

字段

描述

OSPF Process 1 with Router ID 192.168.1.2

OSPF进程号以及OSPF Router ID

RouterID

本路由器的Router ID

Router type

路由器类型，取值为：

·ABR表示区域边界路由器

·ASBR表示自治系统边界路由器

·NSSA表示支持NSSA区域

·为空表示非上面三种情况

Route tag

与外部路由相关联的标记

Multi-VPN-Instance is not enabled

当前进程不支持多VPN实例

Ext-community type

OSPF扩展团体属性类型编码。其中：

·domain ID代表domain ID属性编码

·route type代表route type属性编码

·router ID代表router ID属性编码

Domain ID

OSPF域标识符（主标识符）

Opaque capable

使能OSPF的Opaque LSA发布接收能力

Originating router-LSAs with maximum metric

Router LSA中除Stublink外使用最大开销值发布

Condition

Stub路由器的状态：

·Always代表始终生效

·On startup while BGP is converging代表BGP收敛前生效

·On startup while BGP is converging for XXX seconds代表BGP收敛超时时间

·On startup for XXX seconds代表重启后生效时间

State

Stub路由器是否生效：

·Active表示生效

·Inactive表示不生效

Advertise stub links with maximum metric in router-LSAs

Router LSA使用最大开销值发布

Advertise summary-LSAs with metric

Summary LSA发布使用的开销值

Advertise external-LSAs with metric

外部LSA发布使用的开销值

ISPF is enabled

使能增量SPF计算功能

SPF-schedule-interval

进行SPF计算的时间间隔

LSA generation interval

LSA生成时间间隔

LSA arrival interval

LSA重复到达的最小时间间隔

Transmit pacing

接口发送LSU报文的速率，其中：

·Interval表示接口发送LSU报文的时间间隔

·Count表示接口一次发送LSU报文的最大个数

Default ASE parameters

引入外部路由的缺省参数值，其中：

·Metric代表度量值

·Tag代表路由标记

·Type代表路由类型

Route preference

内部路由优先级

ASE route preference

外部路由优先级

SPF computation count

OSPF进程的路由计算总数

RFC1583 compatible

兼容RFC 1583路由选择优先规则

Graceful restart interval

GR重启间隔时间

SNMP trap rate limit interval

TRAP发送间隔

Count

TRAP发送个数

This process is currently bound to MIB

当前进程绑定MIB

Area count

当前进程中的区域数

NSSA area count

当前进程中的NSSA区域数

Normal areas with up interfaces

有Up接口的外部能力区域个数

NSSA areas with up interfaces

有Up接口的NSSA区域个数

Up interfaces

处于Up状态的接口计数

ExChange/Loading neighbors

处于ExChange/Loading状态的邻居数

Full neighbors

处于Full状态的邻居数

Calculation trigger type

触发路由计算的类型，具体如下：

·Full：触发全部路由计算

·Area topology change：区域拓扑改变触发路由计算

·Intra router change：增量的区域内路由器路由变化

·ASBR change：增量的ASBR路由变化

·7to5 translator：7转5角色变化

·Full IP prefix：触发全部IP前缀计算

·Full intra AS：触发全部AS内部前缀计算

·Inc intra AS：触发增量AS内部前缀计算

·Full inter AS：触发全部AS外部前缀计算

·Inc inter AS：触发增量AS外部前缀计算

·N/A：未触发计算

Current calculation type

当前路由计算的类型，具体如下：

·SPF calculation：进行区域SPF计算

·Intra router calculation：区域内路由器路由计算

·ASBR calculation：区域间ASBR路由计算

·Inc intra router：增量区域内路由器路由计算

·Inc ASBR calculation：增量区域间ASBR路由计算

·7to5 translator：7转5角色路由计算

·Full intra AS：进行全部AS内部前缀计算

·Inc intra AS：进行增量AS内部前缀计算

·Full inter AS：进行全部AS外部前缀计算

·Inc inter AS：进行增量AS外部前缀计算

·Forward address：转发地址计算

·N/A：未触发计算

Current calculation phase

当前路由计算调度运行到的阶段，具体如下：

·Calculation area topology：计算区域拓扑

·Calculation router：计算路由器路由

·Calculation intra AS：计算AS内部路由

·7to5 translator：计算7转5角色路由

·Forward address：计算转发地址

·Calculation inter AS：计算AS外部路由

·Calculation end：计算收尾阶段

·N/A：未触发计算

Process reset state

进程重启状态状态，具体如下：

·N/A：进程未重启

·Under reset：进程重启过程中

·Under RIB smooth：进程正在同步RIB路由

Current reset type

当前进程重启类型，具体如下：

·N/A：进程未重启

·Normal：普通重启

·GR quit：GR异常退出进行普通重启

·Delete：删除OSPF进程

·VPN delete：删除VPN

Next reset type

即将调度进程重启类型，具体如下：

·N/A：进程未重启

·Normal：普通重启

·GR quit：GR异常退出进行普通重启

·Delete：删除OSPF进程

·VPN delete：删除VPN

Reset prepare message replied

响应准备重启消息的模块，具体如下：

·P代表邻居维护模块

·L代表LSDB同步模块

·C代表路由计算模块

·R代表路由引入模块

Reset process message replied

响应进程重启消息的模块，具体如下：

·P代表邻居维护模块

·L代表LSDB同步模块

·C代表路由计算模块

·R代表路由引入模块

Reset phase of module

各模块所处重启阶段。其中M代表主控制模块，其阶段有：

·N/A：未重启

·Delete area：删除区域

·Delete process：删除进程

P代表邻居维护模块，其阶段有：

·N/A：未重启

·Delete neighbor：删除邻居

·Delete interface：删除接口

·Delete vlink：删除虚连接

·Delete shamlink：删除伪连接

L代表LSDB同步模块，其阶段有：

·N/A：未重启

·Stop timer：停止计时器

·Delete ASE：删除所有ASE LSA

·Delete ASE maps：删除ASE LSA的map

·Clear process data：清除进程数据

·Delete area LSA：删除区域相关LSA及其map

·Delete area interface：删除区域下接口

·Delete process：删除进程相关资源

·Restart：重启进程相关资源

C代表路由计算模块，其阶段有：

·N/A：未重启

·Delete topology：删除区域拓扑

·Delete router：删除路由器路由

·Delete intra AS：删除AS内部路由

·Delete inter AS：删除AS外部路由

·Delete forward address：删除转发地址列表

·Delete advertise：删除发布源列表

R代表路由引入模块，其阶段有：

·N/A：未重启

·Delete ABR summary：删除ABR聚合路由

·Delete ASBR summary：删除ASBR聚合路由

·Delete import：删除引入路由

Area

开始列举当前进程中各区域的信息。显示当前区域ID，IP地址格式

Authtype

区域验证模式，取值为：

·None表示无验证

·Simple表示简单验证模式

·MD5表示MD5验证模式

Area flag

区域类型：

·Normal：普通区域

·Stub：Stub区域

·StubNoSummary：完全Stub区域

·NSSA：NSSA区域

·NSSANoSummary：完全NSSA区域

7/5 translator state

Type-7 LSA转换为Type-5 LSA的转换者状态，取值为：

·Enabled表示通过命令指定Type-7 LSA转换为Type-5 LSA的转换者

·Elected表示通过选举指定Type-7 LSA转换为Type-5 LSA的转换者

·Disabled表示不是Type-7 LSA转换为Type-5 LSA的转换者

7/5 translate stability timer interval

Type-7 LSA转换为Type-5 LSA转换稳定定时器超时时间间隔

SPF scheduled Count

OSPF区域的路由计算总数

Interface

区域内的接口信息

Cost

接口的开销值

State

接口状态

Type

接口的网络类型

MTU

接口的MTU值

Priority

路由器优先级

Designated router

接口所属网段的DR

Backup designated router

接口所属网段的BDR

Timers

OSPF定时器的值，其中：

·Hello表示接口发送Hello报文的时间间隔

·Dead表示邻居的失效时间

·Poll表示接口发送轮询Hello报文的时间间隔

·Retransmit表示定接口重传LSA时间间隔

Transmit Delay

接口对LSA的传输延迟时间

FRR backup

是否使能接口参与LFA（Loop Free Alternate）计算：

·Enabled：使能

·Disabled：关闭

Enabled by network configuration

接口由网络配置使能到该区域

**OSPF \-- OSPF配置命令 \-- display ospf abr-asbr**

------------------------------------------------------------------------

**[display ospf abr-asbr**]命令用来显示到OSPF的区域边界路由器和自治系统边界路由器的路由信息。

【命令】

**[display ospf** [ *process-id*  **abr-asbr**  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程下到区域边界路由器和自治系统边界路由器的路由信息。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

【使用指导】

如果在Stub区域的路由器上执行此命令，不显示有关ASBR的信息。

【举例】

\# 显示到OSPF的区域边界路由器和自治系统边界路由器的路由概要信息。

\<Sysname\> display ospf abr-asbr

          OSPF Process 1 with Router ID 192.168.1.112

                  Routing Table to ABR and ASBR

 Type    Destination     Area            Cost     Nexthop         RtType

 Inter   3.3.3.3         0.0.0.0         3124     10.1.1.2        ASBR

 Intra   2.2.2.2         0.0.0.0         1562     10.1.1.2        ABR

\# 显示到OSPF的区域边界路由器和自治系统边界路由器的路由详细信息。

\<Sysname\> display ospf abr-asbr verbose

          OSPF Process 10 with Router ID 101.1.1.11

                  Routing Table to ABR and ASBR

 Destination: 1.1.1.1             RtType     : ASBR

 Area       : 0.0.0.1             Type       : Intra

 Nexthop    : 150.0.1.12          BkNexthop  : 0.0.0.0

 Interface  : GE1/0/1             BkInterface: N/A

 Cost       : 1000

表1-2 display ospf abr-asbr命令显示信息描述表

字段

描述

Type

到ABR或ASBR的路由类型，取值为：

·Intra表示区域内路由

·Inter表示区域间路由

Destination

ABR或ASBR的路由器ID

Area

下一跳地址所在的区域ID

Cost

从本路由器到达ABR或ASBR的开销

Nexthop

下一跳地址

BkNexthop

备份下一跳地址

RtType

路由器类型，包括ABR和ASBR

Interface

路由出接口

BkInterface

路由备份出接口

**OSPF \-- OSPF配置命令 \-- display ospf abr-summary**

------------------------------------------------------------------------

**[display ospf abr-summary**]命令用来显示OSPF的ABR聚合信息。

【命令】

**[display ospf **[ *process-id*   **area** *area-id*  **abr-summary** [ *ip-address* { *mask-length* \| *mask* } ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的ABR聚合信息。

**[area**]* area-id*：显示指定区域的ABR聚合相关信息。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*如果未指定本参数，将显示所有区域的信息。

*[ip-address*]：指定的聚合路由的目的IP地址。

*[mask-length*]：网络掩码长度，取值范围为0～32。

*[mask*]：网络掩码，点分十进制格式。

**[verbose**]：显示ABR聚合的详细信息。如果未指定本参数，将显示ABR聚合的概要信息。

【使用指导】

如果未指定IP地址和掩码，将显示所有的ABR聚合信息。

【举例】

\# 显示OSPF的ABR聚合信息。

\<Sysname\> display ospf abr-summary

          OSPF Process 1 with Router ID 2.2.2.2

                  ABR Summary Addresses

                          Area: 0.0.0.1

 Total summary addresses: 1

 Net             Mask            Status        Count      Cost

 100.0.0.0       255.0.0.0       Advertise     1          (Not Configured)

表1-3 display ospf abr-summary命令显示信息描述表

字段

描述

Area

聚合路由所在的区域

Total summary addresses

聚合路由的路由数

Net

聚合路由的网络地址

Mask

聚合路由的网络掩码

Status

聚合路由的状态：

·Advertise：已发布

·Not-Advertise：未发布

Count

被聚合的路由数

Cost

聚合路由的开销

\# 显示OSPF的ABR聚合详细信息。

\<Sysname\> display ospf abr-summary verbose

          OSPF Process 1 with Router ID 2.2.2.2

                  ABR Summary Addresses

                          Area: 0.0.0.1

 Total summary addresses: 1

 Net         : 100.0.0.0

 Mask        : 255.0.0.0

 Status      : Advertise

 Cost        : (Not Configured)

 Routes count: 1

   Destination            NetMask                 Metric

   100.1.1.0              255.255.255.0           1000

表1-4 display ospf [abr-summaryverbose]命令显示信息描述表

字段

描述

Destination

被聚合路由的网络地址

NetMask

被聚合路由的网络掩码

Metric

路由的开销值

**OSPF \-- OSPF配置命令 \-- display ospf asbr-summary**

------------------------------------------------------------------------

**[display ospf asbr-summary**]命令用来显示OSPF的ASBR聚合信息。

【命令】

**[display ospf **\*****[process-id*****]** asbr-summary**[ [ *ip-address* { *mask-length* \| *mask* } ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的ASBR聚合信息。

*[ip-address*]：指定的聚合路由的目的IP地址。

*[mask-length*]：网络掩码长度，取值范围为0～32。

*[mask*]：网络掩码，点分十进制格式。

【使用指导】

如果未指定IP地址和掩码，将显示所有的ASBR聚合信息。

【举例】

\# 显示OSPF进程1的ASBR聚合信息。

\<Sysname\> display ospf 1 asbr-summary

          OSPF Process 1 with Router ID 2.2.2.2

                  Summary Addresses

 Total Summary Address Count: 1

                  Summary Address

 Net         : 30.1.0.0

 Mask        : 255.255.0.0

 Tag         : 20

 Status      : Advertise

 Cost        : 10 (Configured)

 The Count of Route is : 2

 Destination     Net Mask        Proto      Process   Type     Metric

 30.1.2.0        255.255.255.0   OSPF       2         2        1

 30.1.1.0        255.255.255.0   OSPF       2         2        1

表1-5 display ospf asbr-summary命令显示信息描述表

字段

描述

Total Summary Address Count

聚合路由的路由数

Net

聚合路由的网络地址

Mask

聚合路由的网络掩码

Tag

聚合路由的标记字段

Status

聚合路由的发布状态

Cost

聚合路由的开销

The Count of Route

被聚合的路由数

Destination

被聚合路由的网络地址

Net Mask

被聚合路由的网络掩码

Proto

引入路由的协议类型

Process

引入路由的协议进程号

Type

外部路由类型

Metric

路由的开销值

**OSPF \-- OSPF配置命令 \-- display ospf event-log**

------------------------------------------------------------------------

**[display ospf event-log**]命令用来显示OSPF的日志信息。

【命令】

**[display ospf** [ *process-id*  **event-log** { **lsa-flush** \| **peer** \| **spf** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有进程的日志信息。

**[lsa-flush**]：LSA老化的日志信息。

**[peer**]：邻居的日志信息。

**[spf**]：路由计算的日志信息。

【使用指导】

路由计算的日志信息是指更新到IP路由表的路由计数信息。

邻居的日志信息包括OSPF邻居状态倒退到DOWN，以及收到BadLSReq、SeqNumberMismatch和1-Way事件导致邻居状态倒退的信息。

【举例】

\# 显示OSPF的LSA 老化日志信息。

\<Sysname\> display ospf event-log lsa-flush

          OSPF Process 1 with Router ID 1.1.1.1

                  LSA Flush Log

 Date: 2013-09-22 Time: 14:47:33 Received MaxAge LSA from 10.1.1.1

 Type: 1   LSID: 2.2.2.2         AdvRtr: 2.2.2.2           Seq#: 80000001

 Date: 2013-09-22 Time: 14:47:33 Flushed MaxAge LSA by the self

 Type: 1   LSID: 1.1.1.1         AdvRtr: 1.1.1.1           Seq#: 80000001

 Date: 2013-09-22 Time: 14:47:33 Received MaxAge LSA from 10.1.2.2

 Type: 1   LSID: 2.2.2.2         AdvRtr: 2.2.2.2           Seq#: 80000001

 Date: 2013-09-22 Time: 14:47:33 Flushed MaxAge LSA by the self

 Type: 1   LSID: 1.1.1.1         AdvRtr: 1.1.1.1           Seq#: 80000001

表1-6 display ospf lsdb lsa-flush命令显示信息描述表

字段

描述

Date &Time

收到MaxAge LSA的时间

Received MaxAge LSA from X.X.X.X

从源地址收到MaxAge LSA

Flushed MaxAge LSA by the self

由自己发起老化，洪泛MaxAge LSA

Type

LSA类型

LSID

LSA链路状态ID

AdvRtr

LSA发布路由器

Seg#

LSA序列号

\# 显示OSPF路由计算的日志信息。

\<Sysname\> display ospf event-log spf

          OSPF Process 1 with Router ID 1.1.1.2

                  SPF log

Date       Time     Duration   Intra Inter External Reason

2012-06-27 15:28:26 0.95       1     1     10000    Intra-area LSA

2012-06-27 15:28:23 0.2        0     0     0        Area 0 full neighbor

2012-06-27 15:28:19 0          0     0     0        Intra-area LSA

2012-06-27 15:28:19 0          0     0     0        external LSA

2012-06-27 15:28:19 0.3        0     0     0        Intra-area LSA

2012-06-27 15:28:12 0          1     0     0        Intra-area LSA

2012-06-27 15:28:11 0          0     0     0        Routing policy

2012-06-27 15:28:11 0          0     0     0        Intra-area LSA

表1-7 display ospf event-log spf命令显示信息描述表

字段

描述

Date/Time

路由计算开始的时间

Duration

路由计算持续时间，单位为秒

Intra

区域内路由变化的个数

Inter

区域间路由变化的个数

External

外部路由变化的个数

Reason

路由计算的原因：

·Intra-area LSA：区域内LSA变化

·Inter-area LSA：区域间LSA变化

·External LSA：外部LSA变化

·Configuration：配置变化

·Area 0 full neighbor：区域0FULL邻居个数变化

·Area 0 up interface：区域0UP接口个数变化

·LSDB overflow state：overflow状态变化

·AS number：AS号变化

·ABR summarization：ABR聚合变化

·GR end：GR结束

·Routing policy：路由策略变化

·Intra-area tunnel：区域内隧道变化

·Others：除上述原因之外的其他原因

\# 显示OSPF邻居的日志信息。

\<Sysname\> display ospf 1 event-log peer

          OSPF Process 1 with Router ID 1.1.1.1

                  Neighbors log

Date       Time     Local Address   Remote Address  Router ID       Reason

2012-12-31 12:35:45 197.168.1.1     197.168.1.2     2.2.2.2         IntPhyChange

2012-12-31 12:35:19 197.168.1.1     197.168.1.2     2.2.2.2         ConfNssaArea

2012-12-31 12:34:59 197.168.1.1     197.168.1.2     2.2.2.2         SilentInt

表1-8 display ospf event-log peer命令显示信息描述表

字段

描述

Date &Time

邻居状态变化的时间

Local Address

建立邻居关系的本端地址

Remote Address

建立邻居关系的对端地址

Router ID

邻居的Router ID

Reason

邻居状态变化的原因：

·ResetConnect：内存不足断连接

·IntChange：接口参数改变

·VlinkChange：虚连接参数改变

·ShamlinkChange：伪连接参数改变

·ResetOspf：重启OSPF进程

·UndoOspf：删除OSPF进程

·UndoArea：删除OSPF区域

·UndoNetwork：接口去使能

·SilentInt：配置抑制接口

·IntLogChange：接口逻辑属性变化

·IntPhyChange：接口物理属性变化

·IntVliChange：接口虚连接属性变化

·VlinkDown：虚连接Down

·ShamlinkDown：伪连接Down

·DeadExpired：Dead Timer超时

·ConfStubArea：配置Stub区域参数

·ConfNssaArea：配置NSSA区域参数

·AuthChange：认证类型变化

·OpaqueChange：Opaque能力改变

·Retrans：重传过多

·LLSChange：LLS能力变化

·OOBChange：OOB能力变化

·GRChange：GR能力变化

·BFDDown：BFD Down

·BadLSReq：收到BadLSReq事件

·SeqMismatch：收到SeqNumberMismatch事件

·1-Way：收到1-Way事件

【相关命令】

·**reset ospf event-log**

**OSPF \-- OSPF配置命令 \-- display ospf fast-reroute lfa-candidate**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display ospf fast-reroute lfa-candidate**]命令用来显示区域中FRR备份下一跳候选列表。

【命令】

**[display ospf ** *process-id* ]  **area** *area-id*  **fast-reroute lfa-candidate**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有进程的备份下一跳候选列表。

**[area**]* area-id*：显示指定区域FRR备份下一跳候选列表。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*如果未指定本参数，将显示所有区域的信息。

【举例】

\# 显示OSPF的FRR备份下一跳候选列表。

\<Sysname\> display ospf 1 area 0 fast-reroute lfa-candidate

          OSPF Process 1 with Router ID 2.2.2.2

                  LFA Candidate List

 Area: 0.0.0.0

 Candidate nexthop count: 2

 NextHop          IntIP            Interface

 10.0.1.1         10.0.1.2         Vlan10

 10.0.11.1        10.0.11.2        Vlan20

表1-9 display ospf fast-reroute lfa-candidate命令显示信息描述表

字段

描述

Area

显示该区域的备份下一跳信息

Candidate nexthop count

备份下一跳个数

NextHop

备份下一跳地址

IntIP

出接口IP地址

Interface

出接口

**OSPF \-- OSPF配置命令 \-- display ospf graceful-restart**

------------------------------------------------------------------------

![说明](OSPF命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display ospf graceful-restart**]命令用来查看OSPF进程的GR状态信息。

【命令】

**[display ospf** [ *process-id*  **graceful-restart**  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的GR状态信息。

**[verbose**]：显示GR详细状态信息。如果未指定本参数，将显示OSPF进程的GR状态概要信息。

【举例】

\# 显示OSPF进程的GR详细状态信息。

\<Sysname\> display ospf graceful-restart verbose

          OSPF Process 1 with Router ID 1.1.1.1

              Graceful Restart information

Graceful Restart capability     : Enable(IETF)

Graceful Restart support        : Planned and un-planned,Partial

Helper capability                  : Enable(IETF)

Helper support                  : Planned and un-planned(IETF),Strict LSA check

Current GR state                : Normal

Graceful Restart period         : 40 seconds

Number of neighbors under Helper: 0

Number of restarting neighbors  : 0

Last exit reason:

  Restarter  : None

  Helper     : None

Area: 0.0.0.0

Authtype: None Area flag: Normal

Area up Interface count: 2

Interface: 40.4.0.1 (Vlan-interface40)

Restarter state: Normal  State: P-2-P     Type: PTP

Last exit reason:

  Restarter  : None

  Helper     : None

Neighbor count of this interface: 1

Number of neighbors under Helper：0

Neighbor        IP address      GR state     Last Helper exit reason

3.3.3.3         40.4.0.3        Normal       None

Virtual-link Neighbor-ID  -\> 4.4.4.4, Neighbor-State: Full

Restarter state: Normal

Interface: 20.2.0.1 (Vlink)

Transit Area：0.0.0.1

Last exit reason:

  Restarter  : None

  Helper     : None

Neighbor        IP address      GR state     Last Helper exit reason

4.4.4.4         20.2.0.4        Normal       Reset neighbor

表1-10 display ospf graceful-restart命令显示信息描述表

字段

描述

OSPF Process 1 with Router ID 1.1.1.1

Graceful Restart information

OSPF进程是1，Router ID是1.1.1.1的GR状态信息

Graceful Restart capability

进程GR能力配置：

·Enable(IETF)：使能IETF GR能力

·Enable(Nonstandard)：使能非IETF GR能力

·Disable：关闭了GR能力

Graceful Restart support

进程GR支持模式（GR使能时才显示）：

·Planned and un-planned：支持计划和非计划GR

·Planned only：只支持计划性GR

·Partial：支持接口级GR

·Global：不支持接口级GR，支持全局GR

Helper capability

进程Help能力配置：

·Enabled (IETF)：支持作为标准GR Helper的能力

·Enabled (Nonstandard)：支持作为非标准GR Helper的能力

·Enabled (IETF and nonstandard)：同时支持作为标准和非标准GR Helper的能力

·Disabled：不支持作为GR Helper的能力

Helper support

显示支持Helper的策略（Helper使能时才显示）：

·Strict LSA check：Helper端支持严格的LSA检查；

·Planned and un-planned：支持作为计划和非计划重启的Helper

·Planned only：只支持作为计划GR的 Helper

Current GR state

当前OSPF进程的GR状态：

·Normal：普通状态

·Under GR：进程正在GR

·Under Helper：进程正在作为GR Helper

Graceful-restart period

GR周期

Number of neighbors under helper

处于Helper状态的邻居数量

Number of restarting neighbors

Helper端显示的处于重启路由器的数量

Last exit reason

上次退出原因，其中：

·Restarter：表示退出Restarter的原因

·Helper：表示退出Helper的原因

Area

开始列举当前进程中各区域的信息。显示当前区域ID，IP地址格式

Authtype

区域验证模式，取值为：

·None：表示无验证

·Simple：表示简单验证模式

·MD5：表示MD5验证模式

Area flag

区域类型：

·Normal：普通区域

·Stub：Stub区域

·StubNoSummary：完全Stub区域

·NSSA：NSSA区域

·NSSANoSummary：完全NSSA区域

Area up Interface count

区域下UP的接口计数

Interface

区域内的接口信息

Restarter state

作为Restarter的状态

State

接口状态

Type

接口的网络类型

Neighbor count of this interface

接口下的邻居

Neighbor

邻居Router ID

IP address

邻居IP地址

GR state

邻居的GR状态：

·Normal：普通状态

·Under GR：进程正在GR

·Under Helper：进程正在作为GR Helper

Last Helper exit reason

上一次作为该邻居Helper退出的原因

Virtual-link Neighbor-ID

Vlink的邻居Router ID

Neighbor-State

Vlink和邻居的状态，包括Down、Init、2-Way、ExStart、Exchange、Loading和Full

Interface

Vlink接口所属的出接口

**OSPF \-- OSPF配置命令 \-- display ospf interface**

------------------------------------------------------------------------

**[display ospf interface**]命令用来显示OSPF的接口信息。

【命令】

**[display ospf ** *process-id* ] **interface** [[ *interface-type* *interface-number* \| **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的接口信息。

*[interface-type interface-number*]：接口类型和编号。显示指定接口的OSPF详细信息。

**[verbose**]：显示所有接口的OSPF详细信息。

【使用指导】

如果未指定接口或参数**verbose**，将显示所有接口的OSPF概要信息。

【举例】

\# 显示所有接口的OSPF概要信息。

\<Sysname\> display ospf interface

          OSPF Process 1 with Router ID 192.168.1.1

                  Interfaces

 Area: 0.0.0.0

 IP Address      Type         State    Cost  Pri   DR              BDR

 192.168.1.1     PTP          P-2-P    1562  1     0.0.0.0         0.0.0.0

 Area: 0.0.0.1

 IP Address      Type         State    Cost  Pri   DR              BDR

 172.16.0.1      Broadcast    DR       1     1     172.16.0.1      0.0.0.0

表1-11 display ospf interface命令显示信息描述表

字段

描述

Area

接口所属的区域ID

IP address

接口IP地址（不管是否使能了流量工程）

Type

接口的网络类型，取值为：

·PTP表示网络类型为点对点

·PTMP表示网络类型为点对多点

·Broadcast表示网络类型为广播

·NBMA表示网络类型为NBMA

State

根据OSPF接口状态机确定的当前接口状态，取值为：

·DOWN表示在接口上没有发送和接收任何路由协议的报文

·Loopback表示路由器到网络的接口处于环回状态，不能用于正常的数据传输

·Waiting表示接口开始发送和接收Hello报文，并试图去识别网络上的DR和BDR

·P-2-P表示接口将每隔HelloInterval的时间间隔发送Hello报文，并尝试和接口链路另一端相连的路由器建立邻接关系

·DR表示路由器是所连网络的指定路由器

·BDR表示路由器是所连网络的备份指定路由器

·DROther表示路由器既不是所连网络的指定路由器，也不是所连网络的备份指定路由器

Cost

接口开销

Pri

路由器优先级

DR

接口所属网段的DR

BDR

接口所属网段的BDR

\# 显示OSPF指定接口GigabitEthernet1/0/1的详细信息。

\<Sysname\> display ospf interface gigabitethernet 1/0/1

          OSPF Process 1 with Router ID 192.168.1.1

                  Interfaces

 Interface: 172.16.0.1 (GigabitEthernet1/0/1)

 Cost: 1       State: DR        Type: Broadcast    MTU: 1500

 Priority: 1

 Designated router: 172.16.0.1

 Backup designated router: 0.0.0.0

 Timers: Hello 10, Dead 40, Poll  40, Retransmit 5, Transmit Delay 1

 FRR backup: Enabled

 Enabled by interface configuration (including secondary IP addresses)

 MD5 authentication enabled.

    The last key is 3.

    The rollover is in progress, 2 neighbor(s) left.

 LDP state: No-LDP

 LDP sync state: Achieved

表1-12 display ospf interface verbose命令显示信息描述表

字段

描述

Interface

接口IP地址等信息

MTU

最大传输单元

Timers

OSPF定时器的值，其中：

·Hello表示接口发送Hello报文的时间间隔

·Dead表示邻居的失效时间

·Poll表示接口发送轮询Hello报文的时间间隔

·Retransmit表示定接口重传LSA时间间隔

FRR backup

是否使能接口参与LFA（Loop Free Alternate）计算：

·Enabled：使能

·Disabled：关闭

Enabled by interface configuration (including secondary IP addresses)

接口使能OSPF，包括接口从IP地址

MD5 authentication enabled

验证模式

The last key

最新的MD5验证字标识符

neighbor(s)

尚未完成MD5验证平滑迁移的邻居个数

LDP state

LDP状态：

·Init：表示处于初始化状态，LDP还没有上报状态

·No-LDP：表示未配置LDP

·Not ready：表示未建立LDP会话

·Ready：表示已建立LDP会话

LDP sync state

LDP IGP同步状态：

·Init：表示初始化

·Achieved：表示已同步

·Max cost：表示保持最大开销值

**OSPF \-- OSPF配置命令 \-- display ospf lsdb**

------------------------------------------------------------------------

**[display ospf lsdb**]命令用来显示OSPF的链路状态数据库信息。

【命令】

**[display ospf ** *process-id* ] **lsdb**  **brief** [\| ]**originate-router***advertising-router-id*[ \| ]**self-originate**

**[display ospf** [ *process-id*  **lsdb** { **opaque-as** \| **ase** }  *link-state-id*  [ **originate-router** *advertising-router-id* \| **self-originate** ]]]

**[display ospf** [ *process-id*   **area** *area-id*  **lsdb** { **asbr** \| **network** \| **nssa** \| **opaque-area** \| **opaque-link** \| **router** \| **summary** }  *link-state-id*  [ **originate-router** *advertising-router-id* \| **self-originate** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的链路状态数据库信息。

**[area*** area-id*]：显示数据库中指定区域的LSA信息。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*如果未指定本参数，将显示所有区域的信息。

**[brief**]：显示数据库的概要信息。

**[asbr**]：显示数据库中Type-4 LSA（ASBR Summary LSA）的信息。

**[ase**]：显示数据库中Type-5 LSA（AS External LSA）的信息。

**[network**]：显示数据库中Type-2 LSA（Network LSA）的信息。

**[nssa**]：显示数据库中Type-7 LSA（NSSA External LSA）的信息。

**[opaque-area**]：显示数据库中Type-10 LSA （Opaque-area LSA）的信息。

**[opaque-as**]：显示数据库中Type-11 LSA （Opaque-AS LSA）的信息。

**[opaque-link**]：显示数据库中Type-9 LSA（Opaque-link LSA）的信息。

**[router**]：显示数据库中Type-1 LSA（Router LSA）的信息。

**[summary**]：显示数据库中Type-3 LSA（Network Summary LSA）的信息。

*[link-state-id*]：链路状态ID，IP地址格式。

**[originate-router ***advertising-router-id*]：发布LSA报文的路由器的Router ID。

**[self-originate**]：显示本地路由器自己产生的LSA的数据库信息。

【举例】

\# 显示OSPF的链路状态数据库信息。

\<Sysname\> display ospf lsdb

          OSPF Process 1 with Router ID 192.168.0.1

                  Link State Database

                          Area: 0.0.0.0

 Type      LinkState ID    AdvRouter          Age  Len   Sequence   Metric

 Router    192.168.0.2     192.168.0.2        474  36    80000004   0

 Router    192.168.0.1     192.168.0.1        21   36    80000009   0

 Network   192.168.0.1     192.168.0.1        321  32    80000003   0

 Sum-Net   192.168.1.0     192.168.0.1        321  28    80000002   1

 Sum-Net   192.168.2.0     192.168.0.2        474  28    80000002   1

                         Area: 0.0.0.1

 Type      LinkState ID    AdvRouter          Age  Len   Sequence   Metric

Router    192.168.0.1     192.168.0.1        21   36    80000005   0

 Sum-Net   192.168.2.0     192.168.0.1        321  28    80000002   2

 Sum-Net   192.168.0.0     192.168.0.1        321  28    80000002   1

Type 9 Opaque (Link-Local Scope) Database

 Flags: \* -Vlink interface LSA

 Type      LinkState ID    AdvRouter          Age  Len   Sequence   Interfaces

\*Opq-Link  3.0.0.0         7.2.2.1            8    14    80000001   10.1.1.2

\*Opq-Link  3.0.0.0         7.2.2.2            8    14    80000001   20.1.1.2

表1-13 display ospf lsdb命令显示信息描述表

字段

描述

 

Area

显示该区域的LSDB信息

 

Type

LSA类型

 

LinkState ID

LSA链路状态ID

 

AdvRouter

LSA发布路由器

 

Age

LSA的老化时间

 

Len

LSA的长度

 

Sequence

LSA序列号

 

Metric

度量值

 

\*Opq-Link

表示Vlink接口产生的Opequa LSA

\# 显示进程号为1的OSPF进程的链路状态数据库中网络LSA的信息。

\<Sysname\> display ospf 1 lsdb network

          OSPF Process 1 with Router ID 192.168.1.1

                          Area: 0.0.0.0

                  Link State Database

    Type      : Network

    LS ID     : 192.168.0.2

    Adv Rtr   : 192.168.2.1

    LS Age    : 922

    Len       : 32

    Options   :  E

    Seq#      : 80000003

    Checksum  : 0x8d1b

    Net Mask  : 255.255.255.0

       Attached Router    192.168.1.1

       Attached Router    192.168.2.1

                          Area: 0.0.0.1

                  Link State Database

    Type      : Network

    LS ID     : 192.168.1.2

    Adv Rtr   : 192.168.1.2

    LS Age    : 782

    Len       : 32

    Options   :  NP

    Seq#      : 80000003

    Checksum  : 0x2a77

    Net Mask  : 255.255.255.0

       Attached Router    192.168.1.1

       Attached Router    192.168.1.2

表1-14 display ospf lsdb network命令显示信息描述表

字段

描述

Type

LSA类型

LS ID

DR的IP地址

Adv Rtr

发布路由器

LS Age

LSA的老化时间

Len

LSA的长度

Options

LSA选项，各选项含义如下：

·O：Opaque LSA发布接受能力

·E：AS外部LSA的接受能力

·EA：外部扩展属性LSA的接受和转发能力

·DC：支持按需链路

·N：是否支持NSSA外部LSA

·P：非纯末稍区域中的ABR路由器将Type-7 LSA转换为Type-5 LSA的能力

Seq#

LSA序列号

Checksum

LSA校验和

Net Mask

网络掩码

Attached Router

与DR形成了完全邻接关系的路由器的Router ID，也包括DR自身的Router ID

**OSPF \-- OSPF配置命令 \-- display ospf nexthop**

------------------------------------------------------------------------

**[display ospf nexthop**]命令用来显示进程中的下一跳信息。

【命令】

**[display ospf ** *process-id* ] **nexthop**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有进程的下一跳信息。

【举例】

\# 显示OSPF路由下一跳信息。

\<Sysname\> display ospf nexthop

          OSPF Process 1 with Router ID 1.1.1.2

                  Neighbor Nexthop Information

 NbrID           Nexthop         Interface                RefCount   Status

 1.1.1.2         4.4.4.4         Loop1                    1          Valid

 1.1.1.1         1.1.1.1         GE1/0/2                 3          Valid

 1.1.1.2         1.1.1.2         GE1/0/2                 4          Valid

表1-15 display ospf nexthop命令显示信息描述表

字段

描述

NbrID

邻居路由器ID

Nexthop

下一跳地址

Interface

出接口

RefCount

该下一跳被引用次数

Status

该下一跳状态：

·Valid：生效

·Invalid：未生效

**OSPF \-- OSPF配置命令 \-- display ospf non-stop-routing status**

------------------------------------------------------------------------

**[display ospf non-stop-routing status**]命令用来显示OSPF的NSR阶段信息。

【命令】

**[display ospf** [ *process-id*  **non-stop-routing status**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的NSR阶段信息。

【举例】

\# 显示OSPF的NSR阶段信息。

\<Sysname\> display ospf non-stop-routing status

                   OSPF Process 1 with Router ID 192.168.33.12

                          Non Stop Routing information

                   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Non Stop Routing capability : Enabled

Upgrade phase : Normal

表1-16 display ospf non-stop-routing status命令显示信息描述表

字段

描述

Non Stop Routing capability

是否使能NSR功能，其中：

·Enabled：使能NSR

·Disabled：不使能NSR

Upgrade phase

升级的各个阶段：

·Prepare：升级准备阶段

·Restore Smooth：升级数据平滑阶段

·Preroute：路由计算预处理阶段

·Calculating：路由计算阶段

·Redisting：路由引入阶段

·Original and age：LSA生成和老化阶段

·Normal：普通状态

**OSPF \-- OSPF配置命令 \-- display ospf peer**

------------------------------------------------------------------------

**[display ospf peer**]命令用来显示OSPF中各区域邻居的信息。

【命令】

**[display ospf ** *process-id* ] **peer**  **verbose**   *interface-type interface-number*   *neighbor-id*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的各区域邻居的信息。

**[verbose**]：显示OSPF各区域邻居的详细信息。如果未指定本参数，将显示OSPF进程各区域邻居的概要信息。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示所有接口的OSPF邻居的信息。

*[neighbor-id*]：邻居路由器的Router ID。如果未指定本参数，将显示所有邻居路由器的OSPF邻居的信息。

【举例】

\# 显示OSPF邻居详细信息。

\<Sysname\> display ospf peer verbose

          OSPF Process 1 with Router ID 1.1.1.1

                  Neighbors

 Area 0.0.0.0 interface 1.1.1.1(GigabitEthernet1/0/1)\'s neighbors

 Router ID: 1.1.1.2          Address: 1.1.1.2          GR state: Normal

   State: Full  Mode: Nbr is master  Priority: 1

   DR: 1.1.1.2  BDR: 1.1.1.1  MTU: 0

[   Options is 0x02 (-\|-\|-\|-\|-\|-\|E\|-)]

   Dead timer due in 33  sec

   Neighbor is up for 02:03:35

   Authentication Sequence: [ 0 ]

   Neighbor state change count: 6

   BFD status: Disabled

 Last Neighbor Down Event:

 Router ID: 22.22.22.22

 Local Address: 11.11.11.11

 Remote Address: 22.22.22.22

 Time: Apr  9 03:18:19 2014

 Reason: Ospf_ifachange

表1-17 display ospf peer verbose命令显示信息描述表

字段

描述

Area *areaID* interface *IPAddress*(*InterfaceName*)\'s neighbors

显示接口在指定区域邻居信息，其中：

·*areaID*表示邻居所属的区域

·*IPAddress*表示接口IP地址

·*InterfaceName*表示接口名称

Router ID

邻居路由器ID

Address

邻居接口地址

GR State

GR状态，取值为：

·Normal：普通状态

·Restarter：正在作为GR Restarter

·Complete：GR完成

·Helper：正在作为GR Helper

State

邻居状态，取值为：

·Down表示邻居关系的初始状态

·Init表示在邻居失效时间内收到来自邻居路由器的Hello报文，但该Hello数据包内没有包含自己的Router ID，双向通信还没有建立起来

·Attempt该状态仅对NBMA网络上的邻居有效，表示最近没有从邻居收到信息，但仍需作出进一步的尝试，用以与邻居联系

·2-Way表示双向通信已经建立，在从邻居路由器收到的Hello报文中看到了自己的RouterID

·Exstart表示路由器和邻居建立主/从关系、确定初始DD报文的序列号，为交换DD报文做好准备

·Exchange表示路由器向其邻居发送描述自己LSDB的DD报文

·Loading表示路由器向邻居发送链路状态请求报文，请求最新的LSA

·Full表示路由器与邻居路由器之间建立起完全邻接关系

Mode

路由器在数据库同步阶段，路由器与邻居协商的主从关系，取值为：

·Nbr is Master表示邻居路由器为主路由器

·Nbr is standby表示邻居路由器为从路由器

Priority

邻居路由器优先级

DR

接口所属网段的DR

BDR

接口所属网段的BDR

MTU

接口MTU的值

Options

邻居的LSA选项，各选项含义如下：

·O：Opaque LSA发布接受能力

·E：AS外部LSA的接受能力

·EA：外部扩展属性LSA的接受和转发能力

·DC：支持按需链路

·N：是否支持NSSA外部LSA

·P：非纯末稍区域中的ABR路由器将Type-7 LSA转换为Type-5 LSA的能力

Dead timer due in 33  sec

邻居将在33秒后被认为不可达

Neighbor is up for 02:03:35

与邻居建立的时长02:03:35

Authentication Sequence

验证序列号

Neighbor state change count

邻居状态发生改变的次数

BFD status

BFD状态，各状态含义如下：

·Disabled：未使能BFD

·Enabled (Control mode)：已使能BFD，并处于控制模式

·Enabled (Echo mode)：已使能BFD，并处于回应模式

Last Neighbor Down Event

最后一次邻居down事件

Local Address

本端IP地址

Remote Address

对端IP地址

Time

邻居down的时间

Reason

邻居down的原因

\# 显示OSPF邻居概要信息。

\<Sysname\> display ospf peer

          OSPF Process 1 with Router ID 1.1.1.1

               Neighbor Brief Information

 Area: 0.0.0.0

 Router ID       Address         Pri Dead-Time  State             Interface

 1.1.1.2         1.1.1.2         1   40         Full/DR           GE1/0/1

 Sham link: 11.11.11.11 -\> 22.22.22.22

 Router ID       Address         Pri Dead-Time  State

 22.22.22.22     22.22.22.22     1   36         Full

表1-18 display ospf peer命令显示信息描述表

字段

描述

Area

邻居所属的区域

Router ID

邻居路由器ID

Address

邻居接口IP地址

Pri

邻居路由器优先级

Dead-Time

OSPF的邻居失效时间

Interface

与邻居相连的接口

State

邻居状态（Down、Init、Attempt、2-Way、Exstart、Exchange、Loading、Full）

Sham link 11.11.11.11 -\> 22.22.22.22

源地址为11.11.11.11、目的地址为22.22.22.22的伪连接

**OSPF \-- OSPF配置命令 \-- display ospf peer statistics**

------------------------------------------------------------------------

**[display ospf peer statistics**]命令用来显示本地路由器所有OSPF邻居的统计信息，即处于各种状态的邻居数目。

【命令】

**[display ospf** [ *process-id*  **peer** **statistics**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的邻居统计信息。

【举例】

\# 显示所有OSPF邻居的统计信息。

\<Sysname\> display ospf peer statistics

          OSPF Process 1 with Router ID 192.168.1.112

                    Neighbor Statistics

  Area ID         Down Attempt Init 2-Way ExStart Exchange Loading Full Total

  0.0.0.0         0    0       0    0     0       0        0       1    1

  0.0.0.2         0    0       0    0     0       0        0       1    1

  Total           0    0       0    0     0       0        0       2    2

  Sham links\' neighbors (Total: 1):

    Down: 0, Init: 0, 2-Way: 0, ExStart: 0, Exchange: 0, Loading: 0, Full: 1

表1-19 display ospf peer statistics命令显示信息描述表

字段

描述

Area ID

区域ID，显示当前路由器位于该区域所有邻居路由器的状态统计信息

Down

同一个区域内状态为Down的邻居路由器数目

Attempt

同一个区域内状态为Attempt的邻居路由器数目

Init

同一个区域内状态为Init的邻居路由器数目

2-Way

同一个区域内状态为2-Way的邻居路由器数目

ExStart

同一个区域内状态为ExStart的邻居路由器数目

Exchange

同一个区域内状态为Exchange的邻居路由器数目

Loading

同一个区域内状态为Loading的邻居路由器数目

Full

同一个区域内状态为Full的邻居路由器数目

Total

处于各种状态（Down/Attempt/Init/2-Way/ExStart/Exchange/Loading/Full）邻居路由器的总和

Sham links\' neighbors

sham-link邻居统计信息

**OSPF \-- OSPF配置命令 \-- display ospf request-queue**

------------------------------------------------------------------------

**[display ospf request-queue**]命令用来显示OSPF的请求列表信息。

【命令】

**[display ospf ** *process-id* ] **request-queue** [ *interface-type interface-number*   *neighbor-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的请求列表信息。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示所有接口的请求列表信息。

*[neighbor-id*]：邻居路由器的Router ID。如果未指定本参数，将显示所有邻居路由器的请求列表信息。

【举例】

\# 显示OSPF请求列表信息。

\<Sysname\> display ospf request-queue

          OSPF Process 100 with Router ID 192.168.1.59

                  Link State Request List

  The Router\'s Neighbor is Router ID 2.2.2.2         Address 10.1.1.2

  Interface 10.1.1.1         Area 0.0.0.0

  Request list:

       Type       LinkState ID      AdvRouter         Sequence   Age

       Router     2.2.2.2           1.1.1.1           80000004   1

       Network    192.168.0.1       1.1.1.1           80000003   1

       Sum-Net    192.168.1.0       1.1.1.1           80000002   2

表1-20 display ospf request-queue命令显示信息描述表

字段

描述

The Router\'s Neighbor is Router ID

邻居路由器的Router ID

Address

邻居接口IP地址

Interface

本地接口IP地址

Area

区域ID

Request list

请求列表信息

Type

LSA类型

LinkState ID

链路状态ID

AdvRouter

发布路由器的Router ID

Sequence

LSA的序列号

Age

LSA的老化时间

**OSPF \-- OSPF配置命令 \-- display ospf retrans-queue**

------------------------------------------------------------------------

**[display ospf retrans-queue**]命令用来显示OSPF的重传列表信息。

【命令】

**[display ospf ** *process-id* ] **retrans-queue** [ *interface-type interface-number*   *neighbor-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的重传列表信息。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示所有接口的重传列表信息。

*[neighbor-id*]：邻居路由器的Router ID。如果未指定本参数，将显示所有邻居路由器的重传列表信息。

【举例】

\# 显示OSPF重传列表信息。

\<Sysname\> display ospf retrans-queue

          OSPF Process 100 with Router ID 192.168.1.59

                  Link State Retransmission List

  The Router\'s Neighbor is Router ID 192.168.1.111   Address 111.1.1.1

  Interface 111.1.1.2        Area 0.0.0.1

  Retransmit list:

       Type       LinkState ID      AdvRouter         Sequence   Age

       Router     2.2.2.2           2.2.2.2           80000004   1

       Network    12.18.0.1         2.2.2.2           80000003   1

       Sum-Net    12.18.1.0         2.2.2.2           80000002   2

表1-21 display ospf retrans-queue命令显示信息描述表

字段

描述

The Router\'s Neighbor is Router ID

邻居路由器ID

Address

邻居接口IP地址

Interface

本地接口IP地址

Area

区域ID

Retransmit List

重传列表信息

Type

LSA类型

LinkState ID

链路状态ID

AdvRouter

发布路由器的Router ID

Sequence

LSA的序列号

Age

LSA的老化时间

**OSPF \-- OSPF配置命令 \-- display ospf routing**

------------------------------------------------------------------------

**[display ospf routing**]命令用来显示OSPF路由表的信息。

【命令】

**[display ospf** [ *process-id*  **routing** ] [[ *ip-address* { *mask-length* \| *mask* } ] ]]\**[interface ***interface-type interface-number*   **nexthop** *nexthop-address*   **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的路由表信息。

*[ip-address*]：路由的目的IP地址。

*[mask-length*]：网络掩码长度，取值范围为0～32。

*[mask*]：网络掩码，点分十进制格式。

**[interface ***interface-type interface-number*]：显示指定出接口的路由信息。*interface-type interface-number*为接口类型和编号。如果未指定本参数，将显示所有接口的路由表信息。

**[nexthop ***nexthop-address*]：显示指定下一跳IP地址的路由信息。如果未指定本参数，将显示所有的OSPF路由表信息。

**[verbose**]：显示路由表详细信息。如果未指定本参数，将显示路由表的概要信息。

【举例】

\# 显示OSPF路由表的信息。

\<Sysname\> display ospf routing

          OSPF Process 1 with Router ID 192.168.1.112

                   Routing Tables

 Routing for Network

 Destination        Cost     Type    NextHop         AdvRouter       Area

 192.168.1.0/24     1562     Stub    192.168.1.2     192.168.1.2     0.0.0.0

 172.16.0.0/16      1563     Inter   192.168.1.1     192.168.1.1     0.0.0.0

 Total nets: 2

 Intra area: 1  Inter area: 1  ASE: 0  NSSA: 0

表1-22 display ospf routing命令显示信息描述表

字段

描述

Destination

目的网络

Cost

到达目的地址的开销

Type

路由类型（Intra-area、Transit、Stub、Inter-Area、 Type1 External和Type2 External）

NextHop

下一跳地址

AdvRouter

发布路由器

Area

区域ID

Total nets

区域内部、区域间、ASE和NSSA区域的路由总数

Intra area

区域内部路由总数

Inter area

区域间路由总数

ASE

OSPF区域外路由总数

NSSA

NSSA区域路由总数

\# 显示OSPF路由表的详细信息。

\<Sysname\> display ospf routing verbose

          OSPF Process 2 with Router ID 192.168.1.112

                   Routing Tables

 Routing for Network

Destination: 192.168.1.0/24

    Priority: Low                     Type: Stub

   AdvRouter: 192.168.1.2             Area: 0.0.0.0

  SubProtoID: 0x1               Preference: 10

     NextHop: 192.168.1.2        BkNextHop: N/A

      IfType: Broadcast           BkIfType: N/A

   Interface: GE1/0/2          BkInterface: N/A

       NibID: 0x1300000c            Status: Normal

        Cost: 1562

Destination: 172.16.0.0/16

    Priority: Low                     Type: Inter

   AdvRouter: 192.168.1.1             Area: 0.0.0.0

  SubProtoID: 0x1               Preference: 10

     NextHop: 192.168.1.1        BkNextHop: N/A

      IfType: Broadcast           BkIfType: N/A

   Interface: GE1/0/3          BkInterface: N/A

       NibID: 0x1300000c            Status: Normal

        Cost: 1563                 SpfCost: 65535

 Total nets: 2

 Intra area: 2  Inter Area: 0  ASE: 0  NSSA: 0

表1-23 display ospf routing verbose命令显示信息描述表

字段

描述

Priority

前缀优先级，取值为：Critical、High、Medium和Low

 

Type

路由类型（Intra-area、Transit、Stub、Inter-Area、 Type1 External和Type2 External）

 

AdvRouter

发布路由器

 

Area

区域ID

 

SubProtoID

子协议ID

Preference

OSPF路由优先级

NextHop

主下一跳IP地址

BkNextHop

备份下一跳IP地址

IfType

路由主下一跳网络类型

BkIfType

路由备份下一跳网络类型

Interface

路由出接口

BkInterface

路由备份出接口

NibID

路由下一跳信息的ID值

Status

路由状态，具体如下：

·Local：该条路由在本地，未发送给路由管理模块

·Invalid：路由下一跳无效

·Stale：该路由下一跳较旧

·Normal：正常可用状态

·Delete：处于删除状态

·Host-Adv：该条路由为主机路由

·Rely：该条路由为迭代路由

Cost

到达目的地址的开销

SpfCost

SPF开销

**OSPF \-- OSPF配置命令 \-- display ospf spf-tree**

------------------------------------------------------------------------

**[display ospf spf-tree**]命令用来显示OSPF区域中的拓扑信息。

【命令】

**[display** **ospf** [ *process-id*   **area** *area-id*  **spf-tree**  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的区域拓扑信息。

**[area**]* area-id*：显示指定区域OSPF拓扑信息。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*如果未指定本参数，将显示所有区域的信息。

**[verbose**]：显示spf-tree的详细信息。如果未指定本参数，将显示spf-tree的概要信息。

【举例】

\# 显示进程1下区域0内的最短路径树。

\<Sysname\> display ospf 1 area 0 spf-tree

          OSPF Process 1 with Router ID 100.0.0.4

        Flags: S-Node is on SPF tree       R-Node is directly reachable

               I-Node or Link is init      D-Node or Link is to be deleted

               P-Neighbor is parent        A-Node is in candidate list

               C-Neighbor is child         T-Node is tunnel destination

               H-Nexthop changed           N-Link is a new path

               V-Link is involved          G-Link is in change list

                  Area: 0.0.0.0  Shortest Path Tree

 SpfNode         Type    Flag      SpfLink         Type   Cost  Flag

\>192.168.119.130 Network S R

                                \--\>114.114.114.111 NET2RT 0     C

                                \--\>100.0.0.4       NET2RT 0     P

\>114.114.114.111 Router  S

                                \--\>192.168.119.130 RT2NET 65535 P

\>100.0.0.4       Router  S

                                \--\>192.168.119.130 RT2NET 10    C

表1-24 display ospf spf-tree命令显示信息描述表

字段

描述

SpfNode

spf节点，若节点类型为路由器，则为路由器ID；若节点类型为网络，则为该网络DR接口IP地址。其中，Type为节点类型：

·Network：表示网络节点

·Router：表示路由器节点

Flag为节点标志：

·I：节点处于初始化状态

·A：节点在候选列表上

·S：节点在SPF树上

·R：该节点与根节点直连

·D：该节点将被删除

·T：该节点为隧道的终点

SpfLink

spf链路，其值表示对端节点。其中，Cost为链路开销，Type为链路类型：

·RT2RT：表示路由器到路由器链路

·NET2RT：表示网络到路由器链路

·RT2NET：表示路由器到网络链路

Flag为链路标志：

·I：链路处于初始化状态

·P：目的节点是父节点

·C：目的节点是子节点

·D：链路将要被删除

·H：下一跳发生改变

·V：目的节点删除或者是新增节点时，链路的目的节点不在SPF树上或处于删除状态

·N：新增链路，并且源节点和目的节点都在SPF树上

·G：链路在区域变化列表中

\# 显示进程1下区域0内的最短路径树详细信息。

\<Sysname\> display ospf 1 area 0 spf-tree verbose

          OSPF Process 1 with Router ID 100.0.0.4

        Flags: S-Node is on SPF tree       R-Node is directly reachable

               I-Node or Link is init      D-Node or Link is to be deleted

               P-Neighbor is parent        A-Node is in candidate list

               C-Neighbor is child         T-Node is tunnel destination

               H-Nexthop changed           N-Link is a new path

               V-Link is involved          G-Link is in change list

                  Area: 0.0.0.0  Shortest Path Tree

\>LsId(192.168.119.130)

 AdvId    : 100.0.0.4       NodeType     : Network

 Mask     : 255.255.255.0   SPFLinkCnt   : 2

 Distance : 10

 VlinkData: 0.0.0.0         ParentLinkCnt: 1           NodeFlag: S R

 NextHop  : 1

   192.168.119.130    Interface: GE1/0/2

 BkNextHop: 1

   0.0.0.0            Interface: GE1/0/2

 \--\>LinkId(114.114.114.111)

    AdvId   : 100.0.0.4       LinkType   : NET2RT

    LsId    : 192.168.119.130 LinkCost   : 0           NextHopCnt: 1

    LinkData: 0.0.0.0         LinkNewCost: 0           LinkFlag  : C

 \--\>LinkId(100.0.0.4)

    AdvId   : 100.0.0.4       LinkType   : NET2RT

    LsId    : 192.168.119.130 LinkCost   : 0           NextHopCnt: 1

    LinkData: 0.0.0.0         LinkNewCost: 0           LinkFlag  : P

表1-25 display ospf spf-tree verbose命令显示信息描述表

字段

描述

LsId

链路状态ID

AdvId

通告路由器ID

NodeType

节点类型，其中：

·Network：表示网络节点

·Router：表示路由器节点

Mask

网络掩码，若为路由器节点掩码为0

SPFLinkCnt

SPF链路个数

Distance

表示到根节点的开销

VlinkData

Vlink报文的目的地址

ParentLinkCnt

父链路个数

NodeFlag

节点标志：

·I：节点处于初始化状态

·A：节点在候选列表上

·S：节点在SPF树上

·R：该节点与根节点直连

·D：该节点将被删除

·T：该节点为隧道的终点

NextHop

下一跳信息

Interface

出接口

BkNextHop

备份下一跳信息

LinkId

链路ID

LinkType

链路类型，其中：

·RT2RT：表示路由器到路由器链路

·NET2RT：表示网络到路由器链路

·RT2NET：表示路由器到网络链路

LinkCost

当前链路开销

NextHopCnt

下一跳个数

LinkData

链路数据

LinkNewCost

新的链路开销

LinkFlag

链路标志：

·I：链路处于初始化状态

·P：目的节点是父节点

·C：目的节点是子节点

·D：链路将要被删除

·H：下一跳发生改变

·V：目的节点删除或者是新增节点时，链路的目的节点不在SPF树上或处于删除状态

·N：新增链路，并且源节点和目的节点都在SPF树上

·G：链路在区域变化列表中

**OSPF \-- OSPF配置命令 \-- display ospf statistics**

------------------------------------------------------------------------

**[display ospf statistics**]命令用来显示OSPF的统计信息。

【命令】

**[display ospf **[ *process-id*  **statistics** [ **error** \| **packet** [ *interface-type* *interface-number* ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的统计信息。

**[error**]：显示错误统计信息。如果未指定本参数，将显示OSPF进程的报文、LSA和路由的统计信息。

**[packet**]：显示OSPF的报文统计信息。

*[interface-type interface-number*]：接口类型和编号。显示指定接口的统计信息。如果未指定本参数，将显示所有接口的统计信息。

【举例】

\# 显示OSPF进程的统计信息。

\<Sysname\> display ospf statistics

          OSPF Process 1 with Router ID 2.2.2.2

                  Statistics

 I/O statistics

  Type                      Input     Output

  Hello                     61        122

  DB Description            2          3

  Link-State Req            1          1

  Link-State Update         3          3

  Link-State Ack            3          2

 LSAs originated by this router

  Router  : 4

Network : 0

  Sum-Net : 0

  Sum-Asbr: 0

  External: 0

  NSSA    : 0

Opq-Link: 0

  Opq-Area: 0

  Opq-As  : 0

 LSAs originated: 4  LSAs received: 7

 Routing table:

   Intra area: 2  Inter area: 3  ASE/NSSA: 0

表1-26 display ospf statistics命令显示信息描述表

字段

描述

I/O statistics

收发的报文和LSA的详细统计信息

Type

OSPF报文类型

Input

接收报文数

Output

发送报文数

Hello

OSPF Hello报文

DB Description

OSPF数据库描述报文

Link-State Req

OSPF链路状态请求报文

Link-State Update

OSPF链路状态更新报文

Link-State Ack

OSPF链路状态确认报文

LSAs originated by this router

本路由器发布LSA的详细统计信息

Router

生成Type-1 LSA的数目

Network

生成Type-2 LSA的数目

Sum-Net

生成Type-3 LSA的数目

Sum-Asbr

生成Type-4 LSA的数目

External

生成Type-5 LSA的数目

NSSA

生成Type-7 LSA的数目

Opq-Link

生成Type-9 LSA的数目

Opq-Area

生成Type-10 LSA的数目

Opq-As

生成Type-11 LSA的数目

LSA originated

生成的LSA的总数

LSA received

接收的LSA的总数

Routing table

路由表信息

Intra area

区域内路由的数量

Inter area

区域间路由的数量

ASE

ASE路由的数量

\# 显示OSPF进程的错误统计信息。

\<Sysname\> display ospf statistics error

          OSPF Process 1 with Router ID 192.168.1.112

                  OSPF Packet Error Statistics

0         : Router ID confusion        0         : Bad packet

 0         : Bad version                0         : Bad checksum

 0         : Bad area ID                0         : Drop on unnumbered link

 0         : Bad virtual link           0         : Bad authentication type

 0         : Bad authentication key     0         : Packet too small

 0         : Neighbor state low         0         : Transmit error

 0         : Interface down             0         : Unknown neighbor

 0         : HELLO: Netmask mismatch    0         : HELLO: Hello-time mismatch

 0         : HELLO: Dead-time mismatch  0         : HELLO: Ebit option mismatch

 0         : DD: MTU option mismatch    0         : DD: Unknown LSA type

 0         : DD: Ebit option mismatch   0         : ACK: Bad ack

 0         : ACK: Unknown LSA type      0         : REQ: Empty request

 0         : REQ: Bad request           0         : UPD: LSA checksum bad

 0         : UPD: Unknown LSA type      0         : UPD: Less recent LSA

表1-27 display ospf statistics error命令显示信息描述表

字段

描述

Router ID confusion

含有重复路由器ID的OSPF报文数

Bad packet

非法的OSPF报文数

Bad version

错误版本号的OSPF报文数

Bad checksum

校验和出错的OSPF报文数

Bad area ID

非法的区域ID的OSPF报文数

Drop on unnumbered link

在地址借用链路上丢弃的OSPF报文数

Bad virtual link

错误的虚链路的OSPF报文数

Bad authentication type

含有非法验证类型的OSPF报文数

Bad authentication key

含有错误验证码的OSPF报文数

Packet too small

报文长度太小的OSPF报文数

Neighbor state low

在低邻居状态收到的OSPF报文数

Transmit error

传输出错的OSPF报文数

Interface down

接口down的计数

Unknown neighbor

未知的邻居发来的OSPF报文数

HELLO: Netmask mismatch

网络掩码不匹配的Hello报文数

HELLO: Hello-time mismatch

Hello定时器不匹配的Hello报文数

HELLO: Dead-time mismatch

Dead定时器不匹配的Hello报文数

HELLO: Ebit option mismatch

Option字段E位不匹配的Hello报文数

DD: MTU option mismatch

MTU不匹配的DD报文数

DD: Unknown LSA type

DD报文中描述未知类型LSA数目

DD: Ebit option mismatch

Option字段E位不匹配的DD报文数

ACK: Bad ack

收到不匹配的ack数目

ACK: Unknown LSA type

收到LSA类型未知的ack数目

REQ: Empty request

不含有任何请求信息的LSR报文数

REQ: Bad request

请求错误LSA的LSR报文数

UPD: LSA checksum bad

LSU报文中LSA校验和出错的LSA数目

UPD: Unknown LSA type

LSU报文中含有未知类型LSA数目

UPD: Less recent LSA

LSU报文中含有不是最新的LSA数目

\# 显示OSPF进程和接口的报文统计信息。

\<Sysname\> display ospf statistics packet

          OSPF Process 100 with Router ID 192.168.1.59

                  Packet Statistics

 Waiting to send packet count: 0

         Hello      DD         LSR        LSU        ACK        Total

 Input : 489        6          2          44         40         581

 Output: 492        8          2          45         40         587

 Area: 0.0.0.1

 Interface: 20.1.1.1 (GigabitEthernet1/0/1)

         DD         LSR        LSU        ACK        Total

 Input : 0          0          0          0          0

 Output: 0          0          0          0          0

 Interface: 100.1.1.1 (GigabitEthernet1/0/9)

         DD         LSR        LSU        ACK        Total

 Input : 3          1          22         16         42

 Output: 2          1          19         20         42

表1-28 display ospf statistics packet命令显示信息描述表

字段

描述

Waiting to send packet count

等待发送报文数

Hello

Hello报文

DD

数据库描述报文

LSR

链路状态请求报文

LSU

链路状态更新报文

ACK

链路状态确认报文

Total

报文总数

Input

接收报文数

Output

发送报文数

Area

区域ID

Interface

接口地址和接口名

【相关命令】

·**reset ospf statistics**

**OSPF \-- OSPF配置命令 \-- display ospf vlink**

------------------------------------------------------------------------

**[display ospf vlink**]命令用来显示OSPF的虚连接信息。

【命令】

**[display ospf** [ *process-id*  **vlink**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的虚连接信息。

【举例】

\# 显示OSPF的虚连接信息。

\<Sysname\> display ospf vlink

          OSPF Process 1 with Router ID 3.3.3.3

                  Virtual Links

 Virtual-link Neighbor-ID  -\> 2.2.2.2, Neighbor-State: Full

 Interface: 10.1.2.1 (GigabitEthernet1/0/1)

 Cost: 1562  State: P-2-P  Type: Virtual

 Transit Area: 0.0.0.1

 Timers: Hello 10 , Dead 40 , Retransmit 5 , Transmit Delay 1

 MD5 authentication enabled.

    The last key is 3.

    The rollover is in progress, 2 neighbor(s) left.

表1-29 display ospf vlink命令显示信息描述表

字段

描述

Virtual-link Neighbor-id

通过虚连接相连的邻居路由器的Router ID

Neighbor-State

邻居状态，包括Down、Init、2-Way、ExStart、Exchange、Loading和Full

Interface

此虚连接的本端接口的IP地址和名称

Cost

接口的路由开销

State

接口状态

Type

类型：虚连接

Transit Area

传输区域ID（如果当前接口为虚连接，则显示）

Timers

OSPF定时器，分别定义如下：

·Hello：接口发送Hello报文的时间间隔

·Dead：邻居的失效时间

·Retransmit：接口重传LSA时间间隔

Transmit Delay

接口对LSA的传输延迟时间

MD5 authentication enabled

验证模式

The last key

最新的MD5验证字标识符

neighbor(s)

尚未完成MD5验证平滑迁移的邻居个数

**OSPF \-- OSPF配置命令 \-- display router id**

------------------------------------------------------------------------

**[display router id**]命令用来显示全局Router ID。

【命令】

**[display router id**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示已配置的全局Router ID。

\<Sysname\> display router id

         Configured router ID is 1.1.1.1

**OSPF \-- OSPF配置命令 \-- dscp**

------------------------------------------------------------------------

**[dscp**]命令用来配置OSPF发送协议报文的DSCP优先级。

**[undo dscp**]命令用来恢复缺省情况。

【命令】

**[dscp** *dscp-value*]

**[undo dscp**]

【缺省情况】

OSPF发送协议报文的DSCP优先级为48。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：DSCP优先级，取值范围为0～63。

【举例】

\# 配置OSPF进程1发送协议报文的DSCP优先级为63。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 dscp 63

**OSPF \-- OSPF配置命令 \-- enable link-local-signaling**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[enable link-local-signaling**]命令用来使能OSPF本地链路的信令能力。

**[undo enable link-local-signaling**]命令用来关闭OSPF本地链路的信令能力。

【命令】

**[enable link-local-signaling**]

**[undo enable link-local-signaling**]

【缺省情况】

OSPF本地链路的信令能力处于关闭状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能OSPF进程1的本地链路的信令能力。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 enable link-local-signaling

**OSPF \-- OSPF配置命令 \-- enable out-of-band-resynchronization**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[enable out-of-band-resynchronization**]命令用来使能OSPF带外同步能力。

**[undo enable out-of-band-resynchronization**]命令用来关闭OSPF带外同步能力。

【命令】

**[enable out-of-band-resynchronization**]

**[undo enable out-of-band-resynchronization**]

【缺省情况】

OSPF带外同步能力处于关闭状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在配置本命令之前，必须先使能OSPF本地链路的信令能力。

【举例】

\# 使能OSPF进程1的带外同步能力。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 enable link-local-signaling

Sysname-ospf-1 enable out-of-band-resynchronization

【相关命令】

·**enable link-local-signaling**

**OSPF \-- OSPF配置命令 \-- event-log**

------------------------------------------------------------------------

**[event-log**]命令用来配置OSPF的日志信息个数。

**[undo event-log**]命令用来恢复缺省情况。

【命令】

**[event-log**[ { **lsa-flush** \| **peer** \| **spf** } **size** *count*]]

**[undo event-log**[ { **lsa-flush** \| **peer** \| **spf** } **size**]]

【缺省情况】

路由计算和邻居的日志信息个数为10。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lsa-flush**]：LSA老化日志信息个数。

**[peer**]：邻居日志信息个数。

**[spf**]：SPF日志信息个数。

*[count*]：日志信息个数，取值范围为0～65535。

【举例】

\# 配置OSPF进程100的路由计算日志信息个数为50。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 event-log spf size 50

**OSPF \-- OSPF配置命令 \-- fast-reroute (OSPF view)**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[fast-reroute**]命令用来配置OSPF快速重路由功能。

**[undo fast-reroute**]命令用来关闭OSPF快速重路由功能。

【命令】

**[fast-reroute ****[lfa **[ **abr-only**  \| **route-policy** *route-policy-name* }]]

**[undo fast-reroute**]

【缺省情况】]

OSPF快速重路由功能处于关闭状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lfa**]**：**为所有路由通过LFA（Loop Free Alternate）算法选取备份下一跳信息。

**[abr-only**]：仅选取到ABR设备的路由作为备份下一跳。

**[route-policy*** route-policy-name*]：为通过策略的路由指定备份下一跳，*route-policy-name*为路由策略名，为1～63个字符的字符串，区分大小写。

【使用指导】

·OSPF快速重路由功能不能与OSPF的BFD功能同时使用，否则可能导致快速重路由功能失效。

·OSPF快速重路由功能（通过LFA算法选取备份下一跳信息）不能与**vlink-peer**命令同时使用。

·OSPF快速重路由功能和前缀无关收敛功能同时配置时，OSPF快速重路由功能生效。

【举例】

\# 使能OSPF进程1的快速重路由功能，为所有路由通过LFA算法选取备份下一跳信息。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 fast-reroute lfa

**OSPF \-- OSPF配置命令 \-- filter (OSPF area View)**

------------------------------------------------------------------------

**[filter**]命令用来配置对Type-3 LSA进行过滤。

**[undo filter**]命令用来取消对Type-3 LSA的过滤。

【命令】

**[filter**[ { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } { **export** \| **import** }]]

**[undo filter**[ { **export** \| **import** }]]

【缺省情况】

不对Type-3 LSA进行过滤。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：指定的基本或高级访问控制列表，对进出本区域的Type-3 LSA进行过滤，取值范围为2000～3999。

*[prefix-list-name*]：指定的地址前缀列表，对进出本区域的Type-3 LSA进行过滤，为1～63个字符的字符串，区分大小写。

*[route-policy-name*]：指定的路由策略，对进出本区域的Type-3 LSA进行过滤，为1～63个字符的字符串，区分大小写。

**[export**]：对ABR向其它区域发布的Type-3 LSA进行过滤。

**[import**]：对ABR向本区域发布的Type-3 LSA进行过滤。

【使用指导】

此命令只在ABR路由器上有效，对区域内部路由器无效。

【举例】

\# 根据地址前缀列表my-prefix-list和编号为2000的基本ACL分别对进出OSPF区域1的Type-3 LSA进行过滤。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 1

Sysname-ospf-100-area-0.0.0.1 filter prefix-list my-prefix-list import

Sysname-ospf-100-area-0.0.0.1 filter 2000 export

**OSPF \-- OSPF配置命令 \-- filter-policy export (OSPF View)**

------------------------------------------------------------------------

**[filter-policy export**]命令用来配置对引入的路由信息进行过滤。

**[undo filter-policy export**]命令用来取消该配置。

【命令】

**[filter-policy**[ { *acl-number* \| **prefix-list** *prefix-list-name* } **export** [ *protocol* [ *process-id* ] ]]]

**[undo filter-policy export** [ *protocol* [ *process-id*  ]]]

【缺省情况】

不对引入的路由信息进行过滤。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：用于过滤路由信息目的地址的基本或高级访问控制列表编号，取值范围为2000～3999。

*[prefix-list-name*]：用于过滤路由信息目的地址的IP地址前缀列表的名称，为1～63个字符的字符串，区分大小写。

*[protocol*]：路由协议名称，指定何种路由协议的路由信息将被过滤。目前可包括：**bgp、direct、isis、ospf**、**rip**和**static**。如果没有指定*protocol*参数，对引入的任何一个协议产生的路由都要进行过滤。

*[process-id*]：路由协议进程号，取值范围为1～65535。只有当*protocol*为**isis**、**ospf**、**rip**时，支持该参数。

【使用指导】

当配置的是高级ACL（3000～3999）时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]来过滤指定目的地址和掩码的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。

【举例】

\# 使用编号为2000的基本ACL对OSPF引入的路由进行过滤。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule deny source 192.168.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname ospf 100

Sysname-ospf-100 filter-policy 2000 export

\# 使用编号为3000的高级ACL对引入的路由进行过滤，只允许113.0.0.0/16通过。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0

Sysname-acl-ipv4-adv-3000 rule 100 deny ip

Sysname-acl-ipv4-adv-3000 quit

Sysname ospf 100

Sysname-ospf-100 filter-policy 3000 export

【相关命令】

·**import-route**

**OSPF \-- OSPF配置命令 \-- filter-policy import (OSPF View)**

------------------------------------------------------------------------

**[filter-policy import**]命令用来过滤通过接收到的LSA计算出来的路由信息。

**[undo filter-policy import**]命令用来恢复缺省情况。

【命令】

**[filter-policy** { *acl-number* [ **gateway** *prefix-list-name*  \| **gateway** *prefix-list-name* \| **prefix-list** *prefix-list-name*  **gateway** *prefix-list-name*  \| **route-policy** *route-policy-name* } **import**]]

**[undo filter-policy import**]

【缺省情况】

OSPF不对通过接收到的LSA计算出来的路由信息进行过滤。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：用于过滤路由信息目的地址的基本或高级访问控制列表编号，取值范围为2000～3999。

**[gateway ***prefix-list-name*]：指定的地址前缀列表，基于要加入到路由表的路由信息的下一跳进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[prefix-list ***prefix-list-name*]：指定的地址前缀列表，基于目的地址对接收的路由信息进行过滤。*prefix-list-name*为1～63个字符的字符串，区分大小写。

**[route-policy** *route-policy-name*]：指定路由策略名，基于路由策略对接收的路由信息进行过滤。*route-policy-name*为1～63个字符的字符串，区分大小写。

【使用指导】

当配置的是高级ACL（3000～3999）或者指定的路由策略中配置的是高级ACL时，ACL中的规则需要使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]来过滤指定目的地址的路由；使用命令**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]来过滤指定目的地址和掩码的路由，其中**source**用来过滤路由目的地址，**destination**用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。

【举例】

\# 使用编号为2000的基本ACL对接收的路由信息进行过滤。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule deny source 192.168.10.0 0.0.0.255

Sysname-acl-ipv4-basic-2000 quit

Sysname ospf 100

Sysname-ospf-100 filter-policy 2000 import

\# 使用编号为3000的高级ACL对接收的路由进行过滤，只允许113.0.0.0/16通过。

\<Sysname\> system-view

Sysname acl advanced 3000

Sysname-acl-ipv4-adv-3000 rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0

Sysname-acl-ipv4-adv-3000 rule 100 deny ip

Sysname-acl-ipv4-adv-3000 quit

Sysname ospf 100

Sysname-ospf-100 filter-policy 3000 import

**OSPF \-- OSPF配置命令 \-- graceful-restart (OSPF view)**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart**]命令用来使能OSPF协议的GR能力。

**[undo graceful-restart**]命令用来关闭OSPF协议的GR能力。

【命令】

**[graceful-restart**[ [ **ietf** \| **nonstandard**   **global** \| **planned-only** ] \*]]

**[undo graceful-restart**]

【缺省情况】

OSPF协议的GR能力处于关闭状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ietf**]：IETF标准GR能力选项。

**[nonstandard**]：非IETF标准GR能力选项。

**[global**]：全局GR，必须保证所有的GR Helper都存在，整个GR才会完成，如果有一个GR Helper失效（比如，接口down），则整个GR失败。如果未指定本参数，表示支持接口级GR，即只要有一个GR Helper存在，则整个GR会完成。

**[planned-only**]：表示只支持计划重启。如果未指定本参数，表示计划重启和非计划重启都支持。计划重启指的是手动通过命令执行重启或主备倒换，在进行重启或主备倒换前GR Restarter会先发送Grace-LSA；非计划GR指的是由于设备故障等原因进行重启或主备倒换，在进行重启或主备倒换前GR Restarter不会事先发送Grace-LSA。

【使用指导】

·在使能OSPF协议的IETF标准GR能力前，需要先使能OSPF不透明链路状态发布接收能力（**opaque-capability enable**）。

·在使能OSPF协议的非IETF标准的GR能力前，需要先使能OSPF本地链路的信令能力（**enable link-local-signaling**）和OSPF带外同步能力（**enable out-of-band-resynchronization**）。

·如果在使能OSPF协议的GR能力时不指定可选参数**nonstandard**和**ietf**，则**nonstandard**为缺省配置。

·OSPF GR特性与OSPF NSR特性互斥，即**graceful-restart**和**non-stop-routing**命令互斥，不能同时配置。

【举例】

\# 使能OSPF进程1的IETF标准GR能力。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 opaque-capability enable

Sysname-ospf-1 graceful-restart ietf

\# 使能OSPF进程1的非IETF标准GR能力。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 enable link-local-signaling

Sysname-ospf-1 enable out-of-band-resynchronization

Sysname-ospf-1 graceful-restart nonstandard

【相关命令】

·**enable link-local-signaling**

·**enable out-of-band-resynchronization**

·**opaque-capability enable**

**OSPF \-- OSPF配置命令 \-- graceful-restart helper enable**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart helper enable**]命令用来使能OSPF的GR Helper能力。

**[undo graceful-restart helper enable**]命令用来关闭OSPF的GR Helper能力。

【命令】

**[graceful-restart helper enable** [ **planned-only** ]]

**[undo graceful-restart helper enable**]

【缺省情况】

OSPF的GR Helper能力处于开启状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[planned-only**]：表示只支持计划重启。如果未指定本参数，表示计划重启和非计划重启（即异常重启）都支持。

【使用指导】

参数**planned-only**只有在IETF标准GR Helper的时候使用。

【举例】

\# 使能OSPF进程1的GR Helper能力。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 graceful-restart helper enable

**OSPF \-- OSPF配置命令 \-- graceful-restart helper strict-lsa-checking**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart helper strict-lsa-checking**]命令用来使能GR Helper严格LSA检查能力。

**[undo graceful-restart helper strict-lsa-checking**]命令用来关闭GR Helper严格LSA检查能力。

【命令】

**[graceful-restart helper strict-lsa-checking**]

**[undo graceful-restart helper strict-lsa-checking**]

【缺省情况】

OSPF协议的GR Helper严格LSA检查能力处于关闭状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当检查到GR Helper设备的LSA发生变化时候，Helper设备退出GR Helper模式。

【举例】

\# 使能OSPF进程1的GR Helper严格LSA检查能力。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 graceful-restart helper strict-lsa-checking

**OSPF \-- OSPF配置命令 \-- graceful-restart interval (OSPF view)**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart interval**]命令用来配置OSPF协议的GR重启间隔时间。

**[undo graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[graceful-restart interval ***interval-value*]

**[undo graceful-restart interval**]

【缺省情况】

OSPF协议的GR重启间隔时间为120秒。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：指定OSPF协议的GR重启间隔时间（期望重启时间），取值范围为40～1800，单位为秒。

【使用指导】

OSPF协议的GR重启间隔时间不能小于OSPF所有接口中邻居失效时间的最大值，否则可能会造成OSPF协议的GR重启失败。

【举例】

\# 配置OSPF进程1的GR重启间隔时间为100秒。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 graceful-restart interval 100

【相关命令】

·**ospf timer dead**

**OSPF \-- OSPF配置命令 \-- host-advertise**

------------------------------------------------------------------------

**[host-advertise**]命令用来配置并发布一条主机路由。

**[undo host-advertise**]命令用来恢复删除一条主机路由。

【命令】

**[host-advertise** *ip-address cost*]

**[undo host-advertise ***ip-address*]

【缺省情况】

OSPF不发布主机路由。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：主机IP地址。

*[cost*]：主机路由的开销值，取值范围为1～65535。

【举例】

\# 配置发布一条路由1.1.1.1，并设置其开销为100。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 0

Sysname-ospf-100-area-0.0.0.0 host-advertise 1.1.1.1 100

**OSPF \-- OSPF配置命令 \-- import-route (OSPF view)**

------------------------------------------------------------------------

**[import-route**]命令用来配置引入外部路由信息。

**[undo import-route**]命令用来取消引入外部路由信息。

【命令】

**import-route**[ *protocol* [ *process-id* \| **all-processes** \| **allow-ibgp**   **allow-direct** \| **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* ] \*]

**[undo import-route**[ *protocol* [ *process-id* \| **all-processes** ]]]

【缺省情况】

不引入外部路由信息。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[protocol*]：指定引入的路由协议，可以是**bgp**、**direct**、**isis**、**ospf**、**rip**或**static**。

*[process-id*]：路由协议进程号，取值范围为1～65535，缺省值为1。

**[all-processes**]：引入指定路由协议所有进程的路由，只有当*protocol*是**rip**、**ospf**或**isis**时可以指定该参数。

**[allow-ibgp**]：允许引入IBGP路由。只有当*protocol*是**bgp**时该参数可选。

**[allow-direct**]：在引入的路由中包含使能了该协议的接口网段路由，只有当*protocol*是**rip**、**ospf**或**isis**时可以指定该参数。如果未指定本参数，在引入协议路由时不会包含使能了该协议的接口网段路由。当**allow-direct**与**route-policy** *route-policy-name*参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致**allow-direct**配置失效。例如，当配置**allow-direct**参数引入OSPF直连时，在路由策略中不要配置**if-match** **route-type**匹配条件，否则，**allow-direct**参数失效。

**[cost ***cost*]：路由开销值，取值范围为0～16777214，缺省值为1。

**[nssa-only**]：设置Type-7 LSA的P比特位不置位，即在对端路由器上不能转为Type-5 LSA。如果未指定本参数，Type-7 LSA的P比特位被置位，即在对端路由器上可以转为Type-5 LSA（如果本地路由器是ABR，则会检查骨干区域是否存在FULL状态的邻居，当FULL状态的邻居存在时，产生的Type-7 LSA中P比特位不置位）。

**[route-policy ***route-policy-name*]：配置只能引入符合指定路由策略的路由。*route-policy-name*为路由策略名称，为1～63个字符的字符串，区分大小写。

**[tag** *tag*]：外部LSA中的标记，取值范围为0～4294967295，缺省值为1。

**[type** *type*]：度量值类型，取值范围为1～2，缺省值为2。

【使用指导】

外部路由是指到达自治系统外部的路由，有两类：

·第一类外部路由（Type1 External）：这类路由的可信程度较高，并且和OSPF自身路由的开销具有可比性，所以到第一类外部路由的开销等于本路由器到相应的ASBR的开销与ASBR到该路由目的地址的开销之和。

·第二类外部路由（Type2 External）：这类路由的可信度比较低，所以OSPF协议认为从ASBR到自治系统之外的开销远远大于在自治系统之内到达ASBR的开销。所以计算路由开销时将主要考虑前者，即到第二类外部路由的开销等于ASBR到该路由目的地址的开销。如果计算出开销值相等的两条路由，再考虑本路由器到相应的ASBR的开销。

需要注意的是：

·该命令不能引入缺省路由。

·**import-route bgp**命令表示只引入EBGP路由；**import-route bgp allow-ibgp**命令表示将IBGP路由也引入，容易引起路由环路，请慎用。

·只能引入路由表中状态为active的路由，是否为active状态可以通过**display ip routing-table** **protocol**命令来查看。

·**undo import-route** *protocol* **all-processes**命令只能取消**import-route ***protocol ***all-processes**命令的配置，不能取消**import-route** *protocol* *process-id*命令的配置。

·**import****-route nssa-only**命令配置后，引入的路由只在NSSA区域产生Type-7 LSA，不会在非NSSA区域产生Type-5LSA。

【举例】

\# 指定引入的进程号为40的RIP路由为Type-2外部路由，路由标记为33，度量值为50。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 import-route rip 40 type 2 tag 33 cost 50

【相关命令】

·**default-route-advertise** (OSPF view)

**OSPF \-- OSPF配置命令 \-- ispf**

------------------------------------------------------------------------

**[ispf enable**]命令用来使能增量SPF计算功能。

**[undo ispf enable**]命令用来关闭增量SPF计算功能。

【命令】

**[ispf enable**]

**[undo ispf enable**]

【缺省情况】

使能增量SPF计算功能。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能增量SPF计算功能后，当网络的拓扑结构发生变化影响到最短路径树的结构时，只将受影响的部分节点进行修正，而不重建整棵最短路径树。

【举例】

\# 关闭OSPF进程100的增量SPF计算功能。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 undo ispf enable

**OSPF \-- OSPF配置命令 \-- log-peer-change**

------------------------------------------------------------------------

**[log-peer-change**]命令用来打开邻居状态变化的输出开关。

**[undo log-peer-change**]命令用来关闭邻居状态变化的输出开关。

【命令】

**[log-peer-change**]

**[undo log-peer-change**]

【缺省情况】

邻居状态变化的输出开关处于打开状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

打开邻接状态输出开关后，OSPF邻居状态变化时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）

【举例】

\# 关闭OSPF进程100的邻居状态变化的输出开关。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 undo log-peer-change

**OSPF \-- OSPF配置命令 \-- lsa-arrival-interval**

------------------------------------------------------------------------

**[lsa-arrival-interval**]命令用来配置OSPF LSA重复到达的最小时间间隔。

**[undo lsa-arrival-interval**]命令用来恢复缺省情况。

【命令】

**[lsa-arrival-interval ***interval*]

**[undo lsa-arrival-interval**]

【缺省情况】

OSPF LSA重复到达的最小时间间隔为1000毫秒。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：OSPF LSA重复到达的最小时间间隔，取值范围为0～60000，单位为毫秒。

【使用指导】

如果在*interval*的时间间隔内又收到一条LSA类型、LS ID、生成路由器ID均相同的LSA则直接丢弃，这样就可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。

建议*interval*小于或等于**lsa-generation-interval**命令所配置的*initial-interval*。

【举例】

\# 设置OSPF LSA重复到达的最小时间间隔为200毫秒。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 lsa-arrival-interval 200

【相关命令】

·**lsa-generation-interval**

**OSPF \-- OSPF配置命令 \-- lsa-generation-interval**

------------------------------------------------------------------------

**[lsa-generation-interval**]命令用来配置OSPF LSA重新生成的时间间隔。

**[undo lsa-generation-interval**]命令用来恢复缺省情况。

【命令】

**[lsa-generation-interval ***maximum-interval * *minimum-interval*  *incremental-interval*  ]

**[undo lsa-generation-interval**]

【缺省情况】

OSPF LSA重新生成的最大时间间隔为5秒，最小时间间隔为50毫秒，时间间隔惩罚增量为200毫秒。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：OSPF LSA重新生成的最大时间间隔，取值范围为1～60，单位为秒。

*[minimum-interval*]：OSPF LSA重新生成的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：OSPF LSA重新生成的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

通过调节LSA重新生成的时间间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。在网络变化不频繁的情况下，将LSA重新生成时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

需要注意的是，*minimum-interval*和*incremental-interva*l配置值不允许大于*maximum-interval*配置值。

【举例】

\# 设置LSA重新生成的最大时间间隔为2秒，最小时间间隔为100毫秒，惩罚增量为100毫秒。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 lsa-generation-interval 2 100 100

【相关命令】

·**lsa-arrival-interval**

**OSPF \-- OSPF配置命令 \-- lsdb-overflow-interval**

------------------------------------------------------------------------

**[lsdb-overflow-interval**]命令用来配置OSPF 尝试退出overflow状态的定时器时间间隔。

**[undo** **lsdb-overflow-interval**]命令用来恢复缺省情况。

【命令】

**[lsdb-overflow-interval** *interval*]

undo **lsdb-overflow-interval**

【缺省情况】

OSPF尝试退出overflow状态的定时器时间间隔是300秒。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：OSPF尝试退出overflow状态的定时器时间间隔，取值范围为0～2147483647，单位为秒。

【使用指导】

网络中出现过多LSA，会占用大量系统资源。当设置的LSDB中External LSA的最大数量达到上限时，LSDB会进入overflow状态，在overflow状态中，不再接收External LSA，同时删除自己生成的External LSA，对于已经收到的External LSA则不会删除。这样就可以减少LSA从而节省系统资源。

通过调整定时器间隔，可以调整OSPF退出overflow状态的时间。

配置为0秒表示不启动定时器，不退出overflow状态。

【举例】

\# 配置OSPF尝试退出overflow的定时器间隔为10秒。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 lsdb-overflow-interval 10

**OSPF \-- OSPF配置命令 \-- lsdb-overflow-limit**

------------------------------------------------------------------------

**[lsdb-overflow-limit**]命令用来配置OSPF的LSDB中External LSA的最大条目数。

**[undo** **lsdb-overflow-limit**]命令用来恢复缺省情况。

【命令】

**[lsdb-overflow-limit** *number*]

**[undo lsdb-overflow-limit**]

【缺省情况】

不对LSDB中External LSA的最大条目数进行限制。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：LSDB中External LSA的最大条目数，取值范围为1～1000000。

【举例】

\# 设置LSDB中External LSA的最大条目数为400000。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 lsdb-overflow-limit 400000

**OSPF \-- OSPF配置命令 \-- maximum load-balancing (OSPF view)**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[maximum load-balancing**]命令用来配置OSPF支持的等价路由的最大条数。

**[undo maximum load-balancing**]命令用来恢复缺省情况。

【命令】

**[maximum load-balancing** *maximum*]

**[undo maximum load-balancing**]

【缺省情况】

OSPF支持的等价路由的最大条数与系统支持最大等价路由的条数相同。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum*]：等价路由的最大条数，当*maximum*取值为1时，相当于不进行负载分担。不同型号的设备支持的取值范围与缺省值不同，请以设备的实际情况为准。

【使用指导】

如果通过**max-ecmp-num**命令配置系统支持最大等价路由的条数为m，则本命令的缺省值为m，取值范围为1～m。

**[max-ecmp-num**]命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置OSPF支持的等价路由的最大条数为2。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 maximum load-balancing 2

【相关命令】

·**max-ecmp-num**（三层技术-IP路由命令参考/IP路由基础）

**OSPF \-- OSPF配置命令 \-- network (OSPF area view)**

------------------------------------------------------------------------

**[network**]命令用来配置OSPF区域所包含的网段并在指定网段的接口上使能OSPF。

**[undo network**]命令用来删除区域所包含的网段并关闭指定网段接口上的OSPF功能。

【命令】

**[network ***ip-address wildcard-mask*]

**[undo** **network** *ip-address wildcard-mask*]

【缺省情况】

接口不属于任何区域且OSPF功能处于关闭状态。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：接口所在的网段地址。

*[wildcard-mask*]：IP地址掩码的反码，相当于将IP地址的掩码取反（0变1，1变0）。其中，"1"表示忽略IP地址中对应的位，"0"表示必须保留此位。（例如：子网掩码255.0.0.0，该掩码的通配符掩码为0.255.255.255）。

【使用指导】

该命令可以在一个区域内配置一个或多个接口。在接口上运行OSPF协议，此接口的主IP地址必须在**network**命令指定的网段范围之内。如果此接口只有从IP地址在**network**命令指定的网段范围之内，接口不运行OSPF协议。

【举例】

\# 指定运行OSPF协议的接口的主IP地址位于网段131.108.20.0/24，接口所在的OSPF区域ID为2。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 2

Sysname-ospf-100-area-0.0.0.2 network 131.108.20.0 0.0.0.255

【相关命令】

·**ospf**

**OSPF \-- OSPF配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

**[non-stop-routing**]命令用来使能OSPF协议的NSR功能。

**[undo non-stop-routing**]命令用来关闭OSPF协议的NSR功能。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【缺省情况】

OSPF协议的NSR功能处于关闭状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

OSPF NSR特性与OSPF GR特性互斥，即**non-stop-routing**和**graceful-restart**命令互斥，不能同时配置。

【举例】

\# 在OSPF进程100中使能NSR功能。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 non-stop-routing

**OSPF \-- OSPF配置命令 \-- nssa**

------------------------------------------------------------------------

**[nssa**]命令用来配置一个区域为NSSA区域。

**[undo nssa**]命令用来恢复缺省情况。

【命令】

**[nssa **[ **default-route-advertise**[ [ **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **type** *type* ] \* \| **no-import-route** \| **no-summary** \| **suppress-fa** \| [ **translate-always** \| **translate-never** ] \| **translator-stability-interval** *value* ] \*]]

**[undo nssa**]

【缺省情况】

没有区域被配置为NSSA区域。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[default-route-advertise**]：该参数只用于NSSA区域的ABR或ASBR，配置后，对于ABR，不论本地是否存在缺省路由，都将生成一条Type-7 LSA向区域内发布缺省路由；对于ASBR，只有当本地存在缺省路由时，才产生Type-7 LSA向区域内发布缺省路由。

**[cost** *cost*]：该缺省路由的度量值，取值范围为0～16777214。如果未指定本参数，缺省路由的度量值将取**default cost**命令配置的值。

**[nssa-only**]：设置Type-7 LSA的P比特位不置位，即在对端路由器上不能转为Type-5 LSA。缺省时，Type-7 LSA的P比特位被置位，即在对端路由器上可以转为Type-5 LSA（如果本地路由器是ABR，则会检查骨干区域是否存在FULL状态的邻居，当FULL状态的邻居存在时，产生的Type-7 LSA中P比特位不置位）。

**[route-policy** *route-policy-name*]：路由策略名，为1～63个字符的字符串，区分大小写。只有当前路由器的路由表中存在缺省路由，并且有路由匹配*route-policy-name*指定的路由策略，才可以产生一个描述缺省路由的Type-7 LSA发布出去，指定的路由策略会影响Type-7 LSA中的值。

**[type ***type*]：该Type-7 LSA的类型，取值范围为1～2，如果未指定指定本参数，Type-7 LSA的缺省类型将取**default type**命令配置的值。

**[no-import-route**]：该参数用于禁止将AS外部路由以Type-7 LSA的形式引入到NSSA区域中，这个参数通常只用在既是NSSA区域的ABR，也是OSPF自治系统的ASBR的路由器上，以保证所有外部路由信息能正确地进入OSPF路由域。

**[no-summary**]：该参数只用于NSSA区域的ABR，配置后，ABR只通过Type-3 LSA向区域内发布一条缺省路由，不再向区域内发布任何其它Type-3 LSA（这种区域又称为Totally NSSA区域）。

**[suppress-fa**]：指定当Type-7 LSA转换为Type-5 LSA时，生成的Type-5 LSA中的Forwarding Address不生效。

**[translate-always**]：指定ABR为NSSA区域的Type-7 LSA转换为Type-5 LSA的转换路由器。

**[translate-never**]：指定ABR不能将NSSA区域的Type-7 LSA转换为Type-5 LSA。

**[translator-stability-interval ***value*]：当有新的设备成为NSSA区域的Type-7 LSA转换为Type-5 LSA的转换路由器后，原Type-7 LSA转换为Type-5 LSA的转换路由器保持转换能力的时间。*value*为保持时间，取值范围为0～900，单位为秒。缺省值为0秒，即不保持。

【使用指导】

如果要将一个区域配置成NSSA区域，则该区域中的所有路由器都必须配置命令。

【举例】

\# 将区域1配置成NSSA区域。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 1

Sysname-ospf-100-area-0.0.0.1 nssa

【相关命令】

·**default-cost** (OSPF area view)

**OSPF \-- OSPF配置命令 \-- opaque-capability enable**

------------------------------------------------------------------------

**[opaque-capability enable**]命令用来使能OSPF的Opaque LSA发布接收能力。

**[undo opaque-capability**]命令用来关闭OSPF的Opaque LSA发布接收能力。

【命令】

**[opaque-capability enable**]

**[undo opaque-capability**]

【缺省情况】

OSPF的Opaque LSA发布接收能力处于开启状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能OSPF的Opaque LSA发布接收能力后，OSPF可以发布接收Type9的Opaque LSA，接收Type10和Type11的Opaque LSA。

【举例】

\# 关闭OSPF的Opaque LSA发布接收能力。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 undo opaque-capability

**OSPF \-- OSPF配置命令 \-- ospf**

------------------------------------------------------------------------

**[ospf**]命令用来启动OSPF，并进入OSPF视图。

**[undo ospf**]命令用来关闭OSPF。

【命令】

**[ospf **[[ *process-id* \| **router-id** *router-id* \| **vpn-instance** *vpn-instance-name* ] \*]]

**[undo ospf **\*[process-id* ]]

【缺省情况】

系统没有运行OSPF。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535，缺省值为1。

**[router-id*** router-id*]：OSPF进程使用的Router ID，点分十进制形式。

**[vpn-instance*** vpn-instance-name*]：指定OSPF进程所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示OSPF位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

通过指定不同的进程号，可以在一台路由器上运行多个OSPF进程。这种情况下，建议使用命令中的*router-id*为不同进程指定不同的Router ID。

必须先启动OSPF进程才能配置相关参数。

【举例】

\# 启动OSPF进程100并配置Router ID为10.10.10.1。

\<Sysname\> system-view

Sysname ospf 100 router-id 10.10.10.1

Sysname-ospf-100

**OSPF \-- OSPF配置命令 \-- ospf area**

------------------------------------------------------------------------

**[ospf area**]命令用来在接口上使能OSPF。

**[undo ospf area**]命令用来取消该配置。

【命令】

**[ospf** *process-id* **area** *area-id* [ **exclude-subip** ]]

**[undo ospf** *process-id* **area** [ **exclude-subip** ]]

【缺省情况】

接口上未使能OSPF。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

*[area-id*]：区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*

**[exclude-subip**]：不包含从IP地址。如果未指定本参数，则会包含从IP地址。

【使用指导】

接口配置优先，接口使能OSPF优于命令**network**的配置。

接口使能OSPF时，如果不存在进程和区域，则创建对应的进程和区域；接口去使能OSPF时，不删除已经创建的进程和区域。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/2使能OSPF进程1，接口所在的OSPF区域ID为2，不包含从IP地址。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname- GigabitEthernet1/0/2 ospf 1 area 2 exclude-subip

·交换应用

\# 配置接口Vlan-interface10使能OSPF进程1，接口所在的OSPF区域ID为2，不包含从IP地址。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf 1 area 2 exclude-subip

【相关命令】

·**network**

**OSPF \-- OSPF配置命令 \-- ospf authentication-mode**

------------------------------------------------------------------------

**[ospf authentication-mode**]命令用来设置接口对OSPF报文进行验证的验证模式及验证字。

**[undo ospf authentication-mode**]命令用来删除接口下已设置的验证模式。

【命令】

MD5/HMAC-MD5验证模式：

**[ospf authentication-mode**[ { **hmac-md5** \| **md5** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* }]]

**[undo ospf authentication-mode **[{ **hmac-md5** \| **md5** } *key-id*]]

简单验证模式：

**[ospf authentication-mode simple**[ { **cipher** *cipher-string* \| **plain** *plain-string* }]]

**[undo ospf authentication-mode simple**]

【缺省情况】

接口不对OSPF报文进行验证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hmac-md5**]：HMAC-MD5验证模式。

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

*[key-id*]：验证字标识符，取值范围为1～255。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，区分大小写。对于简单验证模式，可以是长度为33～41个字符的字符串，对于MD5/HMAC-MD5验证模式，可以是长度为33～53个字符的字符串。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，区分大小写。对于简单验证模式，可以是长度为1～8个字符的字符串，对于MD5/HMAC-MD5验证模式，可以是长度为1～16个字符的字符串。

【使用指导】

以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。

同一网段的接口的验证字口令必须相同，可指定使用MD5/HMAC-MD5验证或简单验证两种方式，但不能同时指定；使用MD5/HMAC-MD5验证方式时，可配置多条MD5/HMAC-MD5验证命令，但*key-id*是唯一的，同一*key-id*只能配置一个验证字。

修改接口的OSPF MD5/HMAC-MD5验证字的步骤如下：

·首先在该接口配置新的MD5/HMAC-MD5验证字；此时若邻居设备尚未配置新的MD5/HMAC-MD5验证字，便会触发MD5/HMAC-MD5验证平滑迁移过程。在这个过程中，OSPF会发送分别携带各个MD5/HMAC-MD5验证字的多份报文，使得已配置新验证字的邻居设备、和尚未配置新验证字的邻居设备都能验证通过，保持邻居关系。

·然后在各个邻居设备上也都配置相同的新MD5/HMAC-MD5验证字；当设备上收到所有邻居的携带新验证字的报文后，便会退出MD5/HMAC-MD5验证平滑迁移过程。

·最后在本设备和所有邻居上都删除旧的MD5/HMAC-MD5验证字；建议接口下不要保留多个MD5/HMAC-MD5验证字，每次MD5/HMAC-MD5验证字修改完毕后，应当及时删除旧的验证字，这样可以防止与持有旧验证字的系统继续通信、减少被攻击的可能，还可以减少验证迁移过程对系统、带宽的消耗。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1采用MD5明文验证模式，验证字标识符为15，验证密码为123456。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1ospf authentication-mode md5 15 plain 123456

·交换应用

\# 配置接口Vlan-interface10采用MD5明文验证模式，验证字标识符为15，验证密码为123456。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf authentication-mode md5 15 plain 123456

·路由应用

\# 配置接口GigabitEthernet1/0/1采用简单明文验证模式，验证密码为123456。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1ospf authentication-mode simple plain 123456

·交换应用

\# 配置接口Vlan-interface10采用简单明文验证模式，验证密码为123456。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf authentication-mode simple plain 123456

【相关命令】

·**authentication-mode**

**OSPF \-- OSPF配置命令 \-- ospf bfd enable**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ospf bfd enable**]命令用来使能OSPF的BFD功能。

**[undo** **ospf** **bfd enable**]命令用来关闭OSPF的BFD功能。

【命令】

**[ospf bfd enable **] **echo**

**[undo**] **ospf bfd enable**

【缺省情况】

OSPF的BFD功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[echo**]：通过BFD echo报文方式实现BFD功能。如果不指定本参数，表示通过BFD控制报文方式实现BFD功能。

【使用指导】

OSPF的BFD功能不能与OSPF快速重路由功能同时使用，否则可能导致快速重路由功能失效。

【举例】

·路由应用

\# 使能接口GigabitEthernet1/0/1的OSPF BFD功能。

\<Sysname\> system-view

Sysname ospf

Sysname-ospf-1 area 0

Sysname-ospf-1-area-0.0.0.0 network 192.168.0.0 0.0.255.255

Sysname-ospf-1-area-0.0.0.0 interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf bfd enable

·交换应用

\# 使能接口Vlan-interface11的OSPF BFD功能。

\<Sysname\> system-view

Sysname ospf

Sysname-ospf-1 area 0

Sysname-ospf-1-area-0.0.0.0 network 192.168.0.0 0.0.255.255

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 ospf bfd enable

**OSPF \-- OSPF配置命令 \-- ospf cost**

------------------------------------------------------------------------

**[ospf cost**]命令用来配置接口运行OSPF协议所需的开销。

**[undo ospf cost**]命令用来恢复缺省情况。

【命令】

**[ospf cost ***value*]

**[undo ospf cost**]

【缺省情况】

接口按照当前的带宽自动计算接口运行OSPF协议所需的开销。对于Loopback接口，缺省值为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：接口运行OSPF协议所需的开销，Loopback接口的取值范围为0～65535，其他接口的取值范围为1～65535。

【使用指导】

本命令可用来手动设置接口的开销值，否则OSPF会按照当前的带宽自动计算接口运行OSPF协议所需的开销。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1运行OSPF协议的开销为65。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf cost 65

·交换应用

\# 指定接口Vlan-interface10运行OSPF协议的开销为65。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf cost 65

【相关命令】

·**bandwidth-reference**

**OSPF \-- OSPF配置命令 \-- ospf dr-priority**

------------------------------------------------------------------------

**[ospf dr-priority**]命令用来设置接口的DR优先级。

**[undo ospf dr-priority**]命令用来恢复缺省情况。

【命令】

**[ospf dr-priority*** priority*]

**[undo ospf dr-priority**]

【缺省情况】

接口的DR优先级为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：接口的DR优先级，取值范围为0～255。

【使用指导】

接口的DR优先级决定了该接口在选举DR/BDR时所具有的资格，数值越大，优先级越高。优先级高的在选举权发生冲突时被首先考虑。如果一台设备的优先级为0，则它不会被选举为DR或BDR。

【举例】

·路由应用

\# 设置接口GigabitEthernet1/0/1在选举DR时的优先级为8。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf dr-priority 8

·交换应用

\# 设置接口Vlan-interface10在选举DR时的优先级为8。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf dr-priority 8

**OSPF \-- OSPF配置命令 \-- ospf fast-reroute lfa-backup**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ospf fast-reroute lfa-backup**]命令用来使能接口参与LFA（Loop Free Alternate）计算。

**[undo ospf fast-reroute lfa-backup**]命令用来禁止接口参与LFA计算。

【命令】

**[ospf fast-reroute lfa-backup**]

**[undo ospf fast-reroute lfa-backup**]

【缺省情况】

使能接口参与LFA计算。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口使能LFA计算，使其有资格成为备份接口。去使能此配置后，则接口不会被选为备份接口。

【举例】

·路由应用

\# 禁止接口GigabitEthernet1/0/1参与LFA计算。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo ospf fast-reroute lfa-backup

·交换应用

\# 禁止接口Vlan-interface11参与LFA计算。

\<Sysname\> system-view

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 undo ospf fast-reroute lfa-backup

**OSPF \-- OSPF配置命令 \-- ospf mib-binding**

------------------------------------------------------------------------

**[ospf mib-binding**]命令用来配置OSPF进程绑定MIB。

**[undo ospf mib-binding**]命令用来恢复缺省情况。

【命令】

**[ospf mib-binding** *process-id*]

**[undo ospf mib-binding**]

【缺省情况】

MIB绑定在进程号最小的OSPF进程上。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

【使用指导】

·如果指定的*process-id*不存在，配置OSPF进程绑定命令时将会提示OSPF进程不存在，无法完成配置。

·如果配置了OSPF进程绑定MIB，若删除*process-id*对应的OSPF进程，则同时删除OSPF进程绑定MIB配置，MIB绑定到进程号最小的OSPF进程上。

【举例】

\#配置OSPF进程100绑定MIB。

\<Sysname\> system-view

Sysname ospf mib-binding 100

**OSPF \-- OSPF配置命令 \-- ospf mtu-enable**

------------------------------------------------------------------------

**[ospf mtu-enable**]命令用来配置DD报文中MTU域的值为发送该报文接口的MTU值。

**[undo ospf mtu-enable**]命令用来恢复缺省情况。

【命令】

**[ospf mtu-enable**]

**[undo ospf mtu-enable**]

【缺省情况】

接口发送的DD报文中MTU域的值为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·通过Virtual-Template或Tunnel建立虚连接后，不同厂商的设备接口发送的DD报文中MTU域的缺省值可能不同，为了保证一致，应该将接口发送的DD报文中MTU域的值恢复为缺省值0。

·当配置了该命令后，接收到DD报文时会检查报文中的MTU值是否大于接收接口的MTU值，如果大于则将报文丢弃。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1在发送DD报文时，填写MTU值域。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf mtu-enable

·交换应用

\# 指定接口Vlan-interface10在发送DD报文时，填写MTU值域。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf mtu-enable

**OSPF \-- OSPF配置命令 \-- ospf network-type**

------------------------------------------------------------------------

**[ospf network-type**]命令用来配置OSPF接口的网络类型。

**[undo ospf network-type**]命令用来将OSPF接口网络类型恢复为缺省情况。

【命令】

**[ospf network-type**[{ **broadcast** \| **nbma** \| **p2mp** [ **unicast** ] \| **p2p**  **peer-address-check**  }]]

**[undo ospf network-type**]

【缺省情况】

当接口封装的链路层协议不同时，OSPF接口网络类型的缺省值也不同：

·当接口封装的链路层协议是Ethernet、FDDI时，OSPF接口网络类型的缺省值为广播类型；

·当接口封装的链路层协议是ATM、帧中继或X.25时，OSPF接口网络类型的缺省值为NBMA；

·当接口封装的链路层协议是PPP、LAPB、HDLC或POS时，OSPF接口网络类型的缺省值为点对点。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[broadcast**]：配置接口的网络类型为广播类型。

**[nbma**]：配置接口的网络类型为NBMA类型。

**[p2mp**]：配置接口的网络类型为点到多点类型。

**[unicast**]：P2MP类型支持单播发送报文，缺省情况下是组播方式发送报文。

**[p2p**]：配置接口的网络类型为点到点类型。

**[peer-address-check**]：配置建立邻接关系必须在同一网段的检查功能，即在接收Hello报文时，对端的IP地址与当前接口必须在同一网段。

【使用指导】

·如果在广播网络上有不支持组播地址的路由器，可以将接口的网络类型改为NBMA。

·在NBMA网络中，如果任意两台路由器之间都有一条虚电路直接可达，或者说，这个网络是全连通的，那么可以把OSPF接口的网路类型配置为NBMA；否则，需要把OSPF接口的网络类型配置为点到多点，这样，两台不能直接可达的路由器之间可以通过一台与两者都直接可达的路由器来交换路由信息。

·接口的网络类型为NBMA或P2MP（unicast）时，必须使用**peer**命令来配置邻接点。

·如果一网段内只有两台路由器运行OSPF协议，也可以将接口的网络类型改为点到点。

·接口的网络类型为P2MP（unicast）时，OSPF协议在该接口上发送的报文均为单播报文。

【举例】

·路由应用

\# 将接口GigabitEthernet1/0/1设置为NBMA类型。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf network-type nbma

·交换应用

\# 将接口Vlan-interface10设置为NBMA类型。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf network-type nbma

【相关命令】

·**ospf dr-priority**

**OSPF \-- OSPF配置命令 \-- ospf prefix-suppression**

------------------------------------------------------------------------

**[ospf prefix-suppression**]命令用来抑制接口进行前缀发布。

**[undo ospf prefix-suppression**]命令用来恢复缺省情况。

【命令】

**[ospf prefix-suppression** [ **disable** ]]

**[undo ospf prefix-suppression**]

【缺省情况】

不抑制接口进行前缀发布。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disable**]：不抑制接口进行前缀发布。

【使用指导】

接口配置不能抑制从地址对应的前缀。

如果OSPF进程配置了抑制前缀发布，但某个接口不想进行抑制，此时可以配置本命令并指定**disable**参数。

具体内容请参见命令**prefix-suppression**中的使用指导。

【举例】

·路由应用

\# 抑制接口GigabitEthernet1/0/2进行前缀发布。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 ospf prefix-suppression

·交换应用

\# 抑制接口Vlan-interface10进行前缀发布。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf prefix-suppression

【相关命令】

·**prefix-suppression**

**OSPF \-- OSPF配置命令 \-- ospf primary-path-detect bfd echo**

------------------------------------------------------------------------

![说明](OSPF命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[ospf primary-path-detect bfd echo**]命令用来使能OSPF协议中主用链路的BFD（Echo方式）检测功能。

**[undo ospf primary-path-detect bfd**]命令用来恢复缺省情况。

【命令】

**[ospf primary-path-detect bfd echo**]

**[undo ospf primary-path-detect bfd**]

【缺省情况】

OSPF协议中主用链路的BFD（Echo方式）检测功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置本功能后，OSPF协议的快速重路由特性和PIC特性中的主用链路将使用BFD（Echo方式）进行检测。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置OSPF协议快速重路由特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 fast-reroute lfa

Sysname-ospf-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf primary-path-detect bfd echo

\# 在接口GigabitEthernet1/0/2上配置OSPF协议PIC特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 pic additional-path-always

Sysname-ospf-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 ospf primary-path-detect bfd echo

·交换应用

\# 在接口Vlan-interface10上配置OSPF协议快速重路由特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 fast-reroute lfa

Sysname-ospf-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf primary-path-detect bfd echo

\# 在接口Vlan-interface11上配置OSPF协议PIC特性中主用链路使能BFD（Echo方式）检测功能。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 pic additional-path-always

Sysname-ospf-1 quit

Sysname bfd echo-source-ip 1.1.1.1

Sysname interface vlan-interface 11

Sysname-Vlan-interface11 ospf primary-path-detect bfd echo

**OSPF \-- OSPF配置命令 \-- ospf timer dead**

------------------------------------------------------------------------

**[ospf timer dead**]命令用来设置OSPF的邻居失效时间。

**[undo ospf timer dead**]命令用来恢复缺省情况。

【命令】

**[ospf timer dead ***seconds*]

**[undo ospf timer dead**]

【缺省情况】

P2P、Broadcast类型接口的OSPF邻居失效的时间为40秒；P2MP、NBMA类型接口的OSPF邻居失效的时间为120秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：OSPF邻居失效的时间，取值范围为1～2147483647，单位为秒。

【使用指导】

OSPF邻居的失效时间是指：在该时间间隔内，若未收到邻居的Hello报文，就认为该邻居已失效。**dead** *seconds*值至少应为**hello** *seconds*值的4倍，同一网段上的接口的**dead ***seconds*也必须相同。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1上的邻居失效时间为60秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf timer dead 60

·交换应用

\# 配置接口Vlan-interface10上的邻居失效时间为60秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf timer dead 60

【相关命令】

·**ospf timer hello**

**OSPF \-- OSPF配置命令 \-- ospf timer hello**

------------------------------------------------------------------------

**[ospf timer hello**]命令用来配置接口发送Hello报文的时间间隔。

**[undo ospf timer hello**]命令用来恢复缺省情况。

【命令】

**[ospf timer hello ***seconds*]

**[undo ospf timer hello**]

【缺省情况】

P2P、Broadcast类型接口发送Hello报文的时间间隔为10秒；P2MP、NBMA类型接口发送Hello报文的时间间隔为30秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口发送Hello报文的时间间隔，取值范围为1～65535，单位为秒。

【使用指导】

*[seconds*]的值越小，发现网络拓扑改变的速度越快，对系统资源的开销也就越大。同一网段上的接口的*seconds*必须相同。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1发送Hello报文的时间间隔为20秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf timer hello 20

·交换应用

\# 配置接口Vlan-interface10发送Hello报文的时间间隔为20秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf timer hello 20

【相关命令】

·**ospf timer dead**

**OSPF \-- OSPF配置命令 \-- ospf timer poll**

------------------------------------------------------------------------

**[ospf timer poll**]命令用来配置在NBMA接口上向状态为down的邻居路由器发送轮询Hello报文的时间间隔。

**[undo ospf timer poll**]命令用来恢复缺省情况。

【命令】

**[ospf timer poll** *seconds*]

**[undo ospf timer poll**]

【缺省情况】

在NBMA接口上向状态为down的邻居路由器发送轮询Hello报文的时间间隔为120秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：向状态为down的邻居路由器发送轮询Hello报文的时间间隔，取值范围为1～2147483647，单位为秒。

【使用指导】

在NBMA的网络上，当邻居失效后，将按轮询时间间隔定期地发送Hello报文。用户可配置轮询时间间隔以指定该接口在与相邻路由器构成邻居关系之前发送Hello报文的时间间隔。

发送轮询Hello报文的时间间隔至少应为发送Hello报文时间间隔的4倍。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1上发送轮询Hello报文的时间间隔为130秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf timer poll 130

·交换应用

\# 配置接口上Vlan-interface10发送轮询Hello报文的时间间隔为130秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf timer poll 130

【相关命令】

·**ospf timer hello**

**OSPF \-- OSPF配置命令 \-- ospf timer retransmit**

------------------------------------------------------------------------

**[ospf timer retransmit**]命令用来配置接口重传LSA的时间间隔。

**[undo ospf timer retransmit**]命令用来恢复缺省情况。

【命令】

**[ospf timer retransmit ***seconds*]

**[undo ospf timer retransmit**]

【缺省情况】

接口重传LSA的时间间隔为5秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口重传LSA的时间间隔，取值范围为1～3600，单位为秒。

【使用指导】

当一台路由器向它的邻居发送一条LSA后，需要等到对方的确认报文。若在该重传LSA的时间间隔内未收到对方的确认报文，就会重传这条LSA。

请合理配置接口重传LSA的时间间隔，避免引起不必要的重传。比如，对于低速链路，可以适当把这个时间间隔值设置大一点。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1与邻接路由器之间传送LSA的重传间隔为8秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf timer retransmit 8

·交换应用

\# 指定接口Vlan-interface10与邻接路由器之间传送LSA的重传间隔为8秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf timer retransmit 8

**OSPF \-- OSPF配置命令 \-- ospf trans-delay**

------------------------------------------------------------------------

**[ospf trans-delay**]命令用来配置接口对LSA的传输延迟时间。

**[undo ospf trans-delay**]命令用来恢复缺省情况。

【命令】

**[ospf trans-delay ***seconds*]

**[undo ospf trans-delay**]

【缺省情况】

接口对LSA的传输延迟时间为1秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口对LSA的传输延迟时间，取值范围为1～3600，单位为秒。

【使用指导】

LSA在本路由器的LSDB中会随时间老化（LSA的老化时间每秒钟加1），但在网络的传输过程中却不会，所以有必要在发送之前在LSA的老化时间上增加一定的延迟时间。此配置对低速率的网络尤其重要。

【举例】

·路由应用

\# 指定接口GigabitEthernet1/0/1上传送LSA的时延值为3秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ospf trans-delay 3

·交换应用

\# 指定接口Vlan-interface10上传送LSA的时延值为3秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 ospf trans-delay 3

**OSPF \-- OSPF配置命令 \-- peer**

------------------------------------------------------------------------

**[peer**]命令用来配置NBMA网络或P2MP单播网络的邻居。

**[undo peer**]命令用来取消该操作。

【命令】

**[peer*** ip-address*[ [ **cost** *value* \| **dr-priority** *dr-priority* ]]]

**[undo peer ***ip-address*]

【缺省情况】

没有配置邻居。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：邻居的IP地址。

**[cost*** value*]：邻居的开销，取值范围为1～65535。

**[dr-priority ***dr-priority*]：邻居的优先级，取值范围为0～255，缺省值为1。

【使用指导】

NBMA网络或P2MP单播网络采用单播形式发送协议报文，必须手工指定邻居。

本命令设置的开销值仅用于P2MP链路上建立的邻居，如果没有配置开销值，去往该邻居的花费等于接口的开销值。

本命令设置的优先级仅用于表示路由器是否主动向该邻居发送Hello报文，并不用于实际的DR选举，**ospf dr-priority**命令设置的优先级用于实际的DR选举。

【举例】

\# 指定邻居的IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 peer 1.1.1.1

【相关命令】

·**ospf dr-priority**

**OSPF \-- OSPF配置命令 \-- pic**

------------------------------------------------------------------------

**[pic**]命令用来使能前缀无关收敛功能。

**[undo pic**]命令用来关闭前缀无关收敛功能。

【命令】

**[pic** [ **additional-path-always** ]]

**[undo pic**]

【缺省情况】

使能前缀无关收敛功能。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[additional-path-always**]：支持非直连的次优路由作为备份。

【使用指导】

PIC（Prefix Independent Convergence，前缀无关收敛），即收敛时间与前缀数量无关，加快收敛速度。传统的路由计算快速收敛都与前缀数量相关，收敛时间与前缀数量成正比。OSPF只实现区域间路由以及外部路由的前缀无关收敛。

OSPF快速重路由功能和PIC同时配置时，OSPF快速重路由功能生效。

【举例】

\# 使能OSPF协议的PIC支持非直连次优路由做备份功能。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 pic additional-path-always

**OSPF \-- OSPF配置命令 \-- preference**

------------------------------------------------------------------------

**[preference**]命令用来配置OSPF协议路由的优先级。

**[undo preference**]命令用来恢复缺省情况。

【命令】

**[preference** [ **ase**  { *preference* \| **route-policy** *route-policy-name* } \*]]

**[undo preference** [ **ase** ]]

【缺省情况】

OSPF内部路由的优先级为10，OSPF外部路由的优先级为150。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ase**]：配置外部路由的优先级。如果未指定该参数，配置内部路由优先级。

*[preference*]：OSPF路由的优先级，取值范围为1～255。优先级的值越小，其实际的优先程度越高。

**[route-policy*** route-policy-name*]：应用路由策略，对特定的路由设置优先级。*route-policy-name*是路由策略名称，为1～63个字符的字符串，区分大小写。

【使用指导】

配置了**route-policy**参数后，如果**route-policy**中对某些匹配的路由优先级进行了修改，则这些匹配的路由取**route-policy**修改的优先级，其它路由的优先级均取**preference**命令所设的值。

由于路由器上可能同时运行多个动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题，所以为每一种路由协议指定了一个缺省的优先级。在不同的路由协议发现去往同一目的地的多条路由时，优先级高的协议发现的路由将被选中以转发IP报文。

【举例】

\# 配置OSPF协议外部路由的优先级为200。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 preference ase 200

\# 配置OSPF协议内部路由的优先级，匹配路由策略pre的路由优先级为100，未匹配的路由优先级为150。

\<Sysname\> system-view

Sysname ip prefix-list test index 10 permit 100.1.1.0 24

Sysname route-policy pre permit node 10

Sysname-route-policy-pre-10 if-match ip address prefix-list test

Sysname-route-policy-pre-10 apply preference 100

Sysname-route-policy-pre-10 quit

Sysname ospf 100

Sysname-ospf-100 preference route-policy pre 150

**OSPF \-- OSPF配置命令 \-- prefix-priority**

------------------------------------------------------------------------

**[prefix-priority**]命令用来使能OSPF的前缀按优先权快速收敛功能。

**[undo prefix-priority**]命令用来关闭OSPF的前缀按优先权快速收敛功能。

【命令】

**[prefix-priority route-policy** *route-policy-name*]

**[undo prefix-priority**]

【缺省情况】

OSPF的前缀按优先权快速收敛功能处于关闭状态。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[route-policy*** route-policy-name*]：应用路由策略，对特定的路由前缀设置优先权。*route-policy-name*是路由策略名称，为1～63个字符的字符串，区分大小写。

【使用指导】

通过策略指定优先权，不同前缀按优先权顺序下发，由高到低分为4个优先权（Critical、High、Medium和Low），如果一条路由符合多个收敛优先权的匹配规则，则这些收敛优先权中最高者当选为路由的收敛优先权。

OSPF路由的32位主机路由为Medium优先权，其它为Low优先权。

【举例】

\# 配置通过路由策略pre修改特定路由前缀的优先权为Medium。

\<Sysname\> system-view

Sysname ip prefix-list test index 10 permit 100.1.1.0 24

Sysname route-policy pre permit node 10

Sysname-route-policy-pre-10 if-match ip address prefix-list test

Sysname-route-policy-pre-10 apply prefix-priority medium

Sysname-route-policy-pre-10 quit

Sysname ospf 100

Sysname-ospf-100 prefix-priority route-policy pre

**OSPF \-- OSPF配置命令 \-- prefix-suppression**

------------------------------------------------------------------------

**[prefix-suppression**]命令用来抑制OSPF进程进行前缀发布。

**[undo prefix-suppression**]命令用来恢复缺省情况。

【命令】

**[prefix-suppression**]

**[undo prefix-suppression**]

【缺省情况】

不抑制OSPF进程进行前缀发布。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果需要抑制前缀发布，建议整个OSPF网络都配置本命令。

全局配置不能抑制从地址、LoopBack接口以及处于抑制状态的接口对应的前缀。如果想对LoopBack接口或处于抑制状态的接口进行抑制，可以通过配置接口前缀抑制（**ospf prefix-suppression**命令）来实现。

OSPF使能网段时会将接口上匹配该网段的所有网段路由与主机路由都通过LSA发布，但有时候主机路由或网段路由是不希望被发布的。通过前缀抑制配置，可以减少LSA中携带不需要的前缀，即不发布某些网段路由和主机路由，从而提高网络安全性，加快路由收敛。

当使能前缀抑制时，具体情况如下：

·P2P或P2MP类型网络：Type-1 LSA中不发布接口的主地址，即Type-1 LSA中链路类型为3的Stub链路被抑制，不生成接口路由，但其他路由信息可以正常计算，不会影响流量转发。

·广播类型或者NBMA网络：DR发布的Type-2 LSA的掩码字段会填成32位，即不生成网段路由，但其他路由信息可以正常计算，不会影响流量转发。另外，如果没有邻居，发布的Type-1 LSA中也不发布接口的主地址，即Type-1 LSA中链路类型为3的Stub链路被抑制。

【举例】

\# 抑制OSPF进程1的前缀发布。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 prefix-suppression

【相关命令】

·**ospf prefix-suppression**

**OSPF \-- OSPF配置命令 \-- reset ospf statistics**

------------------------------------------------------------------------

**[reset ospf statistics**]命令用来清除OSPF的统计信息。

【命令】

**[reset ospf** [ *process-id*  **statistics**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535，清除指定OSPF进程的统计信息。

【举例】

\# 清除所有OSPF进程的统计信息。

\<Sysname\> reset ospf statistics

【相关命令】

·**display ospf statistics**

**OSPF \-- OSPF配置命令 \-- reset ospf event-log**

------------------------------------------------------------------------

**[reset ospf event-log**]命令用于清除OSPF的日志信息。

【命令】

**[reset ospf** [ *process-id*  **event-log** [ **lsa-flush** \| **peer** \| **spf** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，则清除所有OSPF进程的日志信息。

**[lsa-flush**]：LSA老化日志信息个数。

**[peer**]：清除邻居的日志信息。

**[spf**]：清除路由计算的日志信息。

【使用指导】

如果未指定日志类型，则所有日志信息都被清除。

【举例】

\# 清除所有OSPF进程路由计算的日志信息。

\<Sysname\> reset ospf event-log spf

【相关命令】

·**display**** ospf event-log**

**OSPF \-- OSPF配置命令 \-- reset ospf process**

------------------------------------------------------------------------

**[reset ospf process**]命令用来重启OSPF进程。

【命令】

**[reset ospf** [ *process-id*  **process**  **graceful-restart** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

**[graceful-restart**]：以GR方式重启OSPF进程。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

如果未指定*process-id*，则重启所有OSPF进程。

使用**reset ospf process**命令重启OSPF，可以获得如下结果：

·可以立即清除无效的LSA，而不必等到LSA超时。

·如果改变了Router ID，该命令的执行会导致新的Router ID生效。

·方便重新选举DR、BDR。

·重启前的OSPF配置不会丢失。

执行该命令后，系统提示用户确认是否重启OSPF协议。

【举例】

\# 重启所有OSPF进程。

\<Sysname\> reset ospf process

Reset OSPF process? [Y/N:y]

**OSPF \-- OSPF配置命令 \-- reset ospf redistribution**

------------------------------------------------------------------------

**[reset ospf redistribution**]命令用来重新向OSPF引入外部路由。

【命令】

**[reset ospf** [ *process-id*  **redistribution**]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。

【使用指导】

如果未指定OSPF进程号，所有OSPF进程都将重新引入外部路由。

【举例】

\# 重新向OSPF引入外部路由。

\<Sysname\> reset ospf redistribution

**OSPF \-- OSPF配置命令 \-- rfc1583 compatible**

------------------------------------------------------------------------

**[rfc1583 compatible**]命令用来使能兼容RFC 1583的路由选择优先规则。

**[undo rfc1583 compatible**]命令用来禁止此方式。

【命令】

**[rfc1583 compatible**]

**[undo rfc1583 compatible**]

【缺省情况】

使能兼容RFC 1583的路由选择优先规则。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当有多条路径可以到达同一个外部路由时，在选择最优路由的问题上，RFC 2328中定义的选路规则与RFC 1583的有所不同，进行此配置可以兼容RFC 1583中定义的规则。

具体的选路规则如下：

(1)当RFC 2328兼容RFC 1583时，所有到达ASBR的路由优先级相同。当RFC 2328不兼容RFC 1583时，非骨干区的区域内路由优先级最高，区域间路由与骨干区区域内路由优先级相同，优选非骨干区的区域内路由，尽量减少骨干区的负担；

(2)若存在多条优先级相同的路由时，按开销值优选，优选开销值小的路由；

(3)若存在多条开销值相同路由时，按路由来源区域的区域ID选择，优选区域ID大的路由。

为了避免路由环路，同一路由域内的路由器建议统一配置相同规则。

【举例】

\# 禁止兼容RFC 1583的路由选择规则。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 undo rfc1583 compatible

**OSPF \-- OSPF配置命令 \-- router id**

------------------------------------------------------------------------

**[router id**]命令用来配置全局Router ID。

**[undo router id**]命令用来恢复缺省情况。

【命令】

**[router id ***router-id*]

**[undo router id**]

【缺省情况】

未配置全局Router ID。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[router-id*]：IPv4地址形式的Router ID。

【使用指导】

一些动态路由协议要求使用Router ID，如果在启动这些路由协议时没有指定Router ID，则缺省使用全局路由器ID。

如果配置了全局路由器ID，则使用配置的值作为Router ID。如果没有配置全局路由器ID，则按照下面的规则进行选择：

(1)如果存在配置IP地址的Loopback接口，则选择Loopback接口地址中最大的作为Router ID。

(2)如果没有配置IP地址的Loopback接口，则从其他接口的IP地址中选择最大的作为Router ID（不考虑接口的up/down状态）。

需要注意的是：

·存在主备的情况下，系统将备份命令行配置的Router ID或从接口地址中选择出来的Router ID。主备倒换后，系统将检查从地址中选出的Router ID的有效性，如果无效将重新进行选择。

·当且仅当被选为Router ID的接口IP地址被删除或被修改时，才触发重新选择过程，其他情况（例如：接口down；已经选取了一个非Loopback接口地址后又配置了一个Loopback接口地址；配置一个更大的接口地址等）不触发重新选择的过程。

·Router ID改变之后，各协议需要通过手工执行**reset**命令才会获取新的Router ID。

【举例】

\# 配置全局Router ID为1.1.1.1。

\<Sysname\> system-view

Sysname router id 1.1.1.1

**OSPF \-- OSPF配置命令 \-- silent-interface (OSPF view)**

------------------------------------------------------------------------

**[silent-interface**]命令用来禁止接口收发OSPF报文。

**[undo silent-interface**]命令用来取消该配置。

【命令】

**[silent-interface**[ { *interface-type interface-number* \| **all** }]]

**[undo silent-interface**[ { *interface-type interface-number* \| **all** }]]

【缺省情况】

允许接口收发OSPF报文。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：接口类型和接口号，禁止指定OSPF接口收发OSPF报文。

**[all**]：禁止所有OSPF接口收发OSPF报文。

【使用指导】

如果要使OSPF路由信息不被某一网络中的路由器获得，可使用本命令禁止在此接口上收发OSPF报文。

【举例】

·路由应用

\# 禁止接口GigabitEthernet1/0/1收发OSPF报文。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 silent-interface gigabitethernet 1/0/1

·交换应用

\# 禁止接口Vlan-interface10收发OSPF报文。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 silent-interface vlan-interface 10

**OSPF \-- OSPF配置命令 \-- snmp-agent trap enable ospf**

------------------------------------------------------------------------

**[snmp-agent trap enable ospf**]命令用来开启OSPF的告警功能。

**[undo** **snmp-agent** **trap** **enable ospf**]命令用来关闭OSPF的告警功能。

【命令】

**[snmp-agent**[ **trap** **enable ospf** [ **authentication-failure** \| **bad-packet** \| **config-error** \| **grhelper-status-change** \| **grrestarter-status-change** \| **if-state-change** \| **lsa-maxage** \| **lsa-originate** \| **lsdb-approaching-overflow** \| **lsdb-overflow** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **retransmit** \| **virt-authentication-failure** \| **virt-bad-packet** \| **virt-config-error** \| **virt-retransmit** \| **virtgrhelper-status-change** \| **virtif-state-change** \| **virtneighbor-state-change** ] \*]]

**[undo snmp-agent**[ **trap** **enable ospf** [ **authentication-failure** \| **bad-packet** \| **config-error** \| **grhelper-status-change** \| **grrestarter-status-change** \| **if-state-change** \| **lsa-maxage** \| **lsa-originate** \| **lsdb-approaching-overflow** \| **lsdb-overflow** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **retransmit** \| **virt-authentication-failure** \| **virt-bad-packet** \| **virt-config-error** \| **virt-retransmit** \| **virtgrhelper-status-change** \| **virtif-state-change** \| **virtneighbor-state-change** ] \*]]

【缺省情况】

OSPF的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[authentication-failure**]：接口认证失败。

**[bad-packet**]：接收了错误报文。

**[config-error**]：接口配置错误。

**[grhelper-status-change**]：邻居GR Helper状态变化。

**[grrestarter-status-change**]：GR Restarter状态变化。

**[if-state-change**]：接口状态变化。

**[lsa-maxage**]：LSA的max age。

**[lsa-originate**]：本地生成LSA。

**[lsdb-approaching-overflow**]：LSDB接近溢出。

**[lsdb-overflow**]：LSDB溢出。

**[neighbor-state-change**]：邻居状态变化。

**[nssatranslator-status-change**]：NSSA转换路由器状态变化。

**[retransmit**]：接口接收和转发报文。

**[virt-authentication-failure**]：虚接口认证失败。

**[virt-bad-packet**]：虚接口接收错误报文。

**[virt-config-error**]：虚接口配置错误。

**[virt-retransmit**]：虚接口接收和转发报文。

**[virtgrhelper-status-change**]：虚接口邻居GR Helper状态变化。

**[virtif-state-change**]：虚接口状态变化。

**[virtneighbor-state-change**]：虚接口邻居状态变化。

【举例】

\# 关闭OSPF的告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable ospf

**OSPF \-- OSPF配置命令 \-- snmp trap rate-limit**

------------------------------------------------------------------------

**[snmp trap rate-limit**]命令用来配置OSPF在指定时间间隔内允许输出的告警信息条数。

**[undo snmp trap rate-limit**]命令用来恢复缺省情况。

【命令】

**[snmp trap rate-limit interval*** trap-interval ***count** *trap-number*]

**[undo snmp trap rate-limit**]

【缺省情况】

OSPF在10秒内允许输出7条告警信息。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[trap-interval*]：指定时间间隔，取值范围为2～60，单位为秒。

*[trap-number*]：在指定时间间隔内允许输出的告警信息条数，取值范围为0～300。

【举例】

\# 配置OSPF在5秒内允许输出10条告警信息。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 snmp trap rate-limit interval 5 count 10

**OSPF \-- OSPF配置命令 \-- spf-schedule-interval**

------------------------------------------------------------------------

**[spf-schedule-interval**]命令用来配置OSPF路由计算的时间间隔。

**[undo spf-schedule-interval**]命令用来恢复缺省情况。

【命令】

**[spf-schedule-interval** *maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo spf-schedule-interval**]

【缺省情况】

OSPF路由计算的最大时间间隔为5秒，最小时间间隔为50毫秒，时间间隔惩罚增量为200毫秒。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：OSPF路由计算的最大时间间隔，取值范围为1～60，单位为秒。

*[minimum-interval*]：OSPF路由计算的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：OSPF路由计算的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

根据本地维护的LSDB，运行OSPF协议的路由器通过SPF算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节SPF的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。

本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到*minimum-interval*，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过*maximum-interval*。

需要注意的是，*minimum-interval*和*incremental-interva*l配置值不允许大于*maximum-interval*配置值。

【举例】

\# 设置OSPF路由计算最大时间间隔为10秒，最小时间间隔为500毫秒，惩罚增量为300毫秒。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 spf-schedule-interval 10 500 300

**OSPF \-- OSPF配置命令 \-- stub (OSPF area view)**

------------------------------------------------------------------------

**[stub**]命令用来配置一个区域为Stub区域。

**[undo stub**]命令用来恢复缺省情况。

【命令】

**[stub**[ [ **default-route-advertise-always** \| **no-summary** ] \*]]

**[undo stub**]

【缺省情况】

没有区域被设置为Stub区域。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[default-route-advertise-always**]：该参数只用于Stub区域的ABR，配置后，ABR向Stub区域内发布缺省路由的Type-3 LSA时不检查骨干区域是否存在FULL状态的邻居。如果未指定本参数，ABR向Stub区域内发布缺省路由的Type-3 LSA时需要检查骨干区域是否存在FULL状态的邻居，如果不存在FULL状态的邻居，则ABR不会向Stub区域内发布缺省路由的Type-3 LSA。

**[no-summary**]：该参数只用于Stub区域的ABR，配置后，ABR只向Stub区域内发布一条缺省路由的Type-3 LSA，不生成任何其它Type-3 LSA（这种区域又称为Totally Stub区域）。

【使用指导】

如果需要在ABR上取消配置**default-route-advertise-always**或**no-summary**参数，可以通过重新执行**stub**命令覆盖之前配置即可。

如果要将一个区域配置成Stub区域，则该区域中的所有路由器都必须配置此属性。

【举例】

\# 将OSPF区域1设置为Stub区域。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 1

Sysname-ospf-100-area-0.0.0.1 stub

【相关命令】

·**default-cost******(OSPF area view)

**OSPF \-- OSPF配置命令 \-- stub-router**

------------------------------------------------------------------------

**[stub-router**]命令用来配置当前路由器为Stub路由器。

**[undo stub-router**]命令用来恢复缺省情况。

【命令】

**[stub-router **[ **external-lsa** [ *max-metric-value*  \| **include-stub** \| **on-startup** { *seconds* \| **wait-for-bgp**  *seconds*  } \| **summary-lsa**  *max-metric-value*  ] \*]]

**[undo stub-router**]

【缺省情况】

当前路由器没有被配置为Stub路由器。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[external-lsa ***max-metric-value*]：路由器发布的外部LSA链路度量值。*max-metric-value*表示链路度量值，取值范围为1～16777215，缺省值为16711680。

**[include-stub**]：路由器发布的Router-LSA中，链路类型为3的Stub链路度量值将设置为最大值65535。

**[on-startup*** seconds*]：在路由器重启期间，路由器做为Stub路由器。*seconds*表示超时时间，取值范围为5～86400，单位为秒。

**[wait-for-bgp*** seconds*]：在路由器重启后，等待BGP路由收敛期间，路由器做为Stub路由器。*seconds*表示超时时间，取值范围为5～86400，单位为秒，缺省值为600秒。

**[summary-lsa*** max-metric-value*]：路由器发布的3类LSA链路度量值。*max-metric-value*表示链路度量值，取值范围为1～16777215，缺省值为16711680。

【使用指导】

通过将当前路由器配置为Stub路由器，在该路由器发布的Router-LSA中，当链路类型取值为3表示连接到Stub网络时，链路度量值不变；当链路类型为1、2、4分别表示通过P2P链路与另一路由器相连、连接到传送网络、虚连接时，链路度量值将设置为最大值65535。

这样其邻居计算出这条路由的开销就会很大，如果邻居上有到这个目的地址开销更小的路由，则数据不会通过这个Stub路由器转发。

【举例】

\# 配置当前路由器为Stub路由器。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 stub-router

**OSPF \-- OSPF配置命令 \-- transmit-pacing**

------------------------------------------------------------------------

**[transmit-pacing**]命令用来配置接口发送LSU报文的时间间隔和一次发送LSU报文的最大个数。

**[undo transmit-pacing**]命令用来恢复缺省情况。

【命令】

**[transmit-pacing interval*** interval ***count ***count*]

**[undo transmit-pacing**]

【缺省情况】

接口发送LSU报文的时间间隔为20毫秒，一次最多发送3个LSU报文。

【视图】

OSPF视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval*** interval*]：接口发送LSU报文的时间间隔，*interval*的取值范围为10～1000，单位为毫秒。当路由器上使能OSPF功能的接口数比较多时，建议增大该值，以控制路由器每秒钟发送LSU报文的总数。

**[count*** count*]：接口一次发送LSU报文的最大个数，*count*的取值范围为1～200。当路由器上使能OSPF功能的接口数比较多时，建议减小该值，以控制路由器每秒钟发送LSU报文的总数。

【举例】

\# 配置OSPF进程1的所有接口发送LSU报文的时间间隔为30毫秒，一次最多发送10个LSU报文。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 transmit-pacing interval 30 count 10

**OSPF \-- OSPF配置命令 \-- vlink-peer (OSPF area view)**

------------------------------------------------------------------------

**[vlink-peer**]命令用来创建并配置一条虚连接。

**[undo vlink-peer**]命令用来删除一条已有的虚连接。

【命令】

**[vlink-peer**[ *router-id* [ **dead** *seconds* \| **hello** *seconds* \| { { **hmac-md5** \| **md5** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* } \| **simple** { **cipher** *cipher-string* \| **plain** *plain-string* } } \| **retransmit** *seconds* \| **trans-delay** *seconds* ] \*]]

**[undo**[ **vlink-peer** *router-id* [ **dead** \| **hello** \| { **hmac-md5** \| **md5** } *key-id* \| **retransmit** \| **simple** \| **trans-delay** ] \*]]

【缺省情况】

没有虚链接。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[router-id*]：虚连接邻居的路由器ID。

**[dead** *seconds*]：失效时间间隔，取值范围为1～32768，单位为秒，缺省值为40秒。该值必须和与其建立虚连接路由器的**dead** *seconds*值相等，并至少为**hello ***seconds*值的4倍。

**[hello** *seconds*]：接口发送Hello报文的时间间隔，取值范围为1～8192，单位为秒，缺省值为10秒。该值必须和与其建立虚连接路由器上的**hello** *seconds*值相等。

**[hmac-md5**]：HMAC-MD5验证模式。

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

*[key-id*]：MD5/HMAC-MD5验证字标识符，取值范围为1～255。

**[cipher**]：表示输入的密码为密文。

*[cipher-string*]：表示设置的密文密码，对于简单验证模式，为33～41个字符的字符串，对于MD5/HMAC-MD5验证模式，为33～53个字符的字符串。

**[plain**]：表示输入的密码为明文。

*[plain-string*]：表示设置的明文密码，对于简单验证模式，为1～8个字符的字符串，对于MD5/HMAC-MD5验证模式，为1～16个字符的字符串。

**[retransmit ***seconds*]：接口重传LSA报文的时间间隔，取值范围为1～3600，单位为秒，缺省值为5秒。

**[trans-delay ***seconds*]：接口延迟发送LSA报文的时间间隔，取值范围为1～3600，单位为秒，缺省值为1秒。

【使用指导】

根据RFC 2328的规定，OSPF的所有非骨干区域必须是和骨干区域保持连通的，可以使用**vlink-peer**命令建立逻辑上的连通性。

各参数取值规则如下：

·**hello**值越小，发现网络变化的速度越快，消耗的网络资源也就越多。

·不能将**retransmit**值设置的太小，否则将会引起不必要的重传。网络速度相对较慢的时候应把该值设的更大一些。

·设置**trans-delay**值时必须考虑接口的发送延迟。

以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。

虚连接可指定使用MD5/HMAC-MD5验证或简单验证两种方式，但不能同时指定；使用MD5/HMAC-MD5验证方式时，可配置多条MD5/HMAC-MD5验证命令，但*key-id*是唯一的，同一*key-id*只能配置一个验证字。

修改虚连接的OSPF MD5/HMAC-MD5验证字的步骤如下：

·首先为该虚连接配置新的MD5/HMAC-MD5验证字；此时若邻居设备尚未配置新的MD5/HMAC-MD5验证字，便会触发MD5/HMAC-MD5验证平滑迁移过程。在这个过程中，OSPF会发送分别携带各个MD5/HMAC-MD5验证字的多份报文，使得无论邻居设备上是否配置了新验证字都能验证通过，保持邻居关系。

·然后在邻居设备上也都配置相同的新MD5/HMAC-MD5验证字；当本设备上收到邻居的携带新验证字的报文后，便会退出MD5/HMAC-MD5验证平滑迁移过程。

·最后在本设备和邻居上都删除旧的MD5/HMAC-MD5验证字；建议不要为虚连接保留多个MD5/HMAC-MD5验证字，每次MD5/HMAC-MD5验证字修改完毕后，应当及时删除旧的验证字，这样可以防止与持有旧验证字的系统继续通信、减少被攻击的可能，还可以减少验证迁移过程对系统、带宽的消耗。

【举例】

\# 配置虚连接，对端路由器Router ID为1.1.1.1。

\<Sysname\> system-view

Sysname ospf 100

Sysname-ospf-100 area 2

Sysname-ospf-100-area-0.0.0.2 vlink-peer 1.1.1.1

【相关命令】

·**authentication-mode**

·**display ospf vlink**

