<!-- CMD-INDEX
  ac interface                        | 交叉连接视图/自动发现交叉连接视图 | L68
  address-family l2vpn                | BGP视图            | L186
  auto-discovery                      | 交叉连接组视图          | L230
  backup-peer                         | 交叉连接PW视图         | L284
  bandwidth                           | 交叉连接PW视图         | L364
  ccc                                 | 交叉连接视图           | L414
  cem-class                           | 系统视图             | L500
  cem class-attach                    | 电路仿真接口视图         | L548
  cem clock recover                   | 电路仿真接口视图         | L600
  cem clock transmit differential     | 电路仿真接口视图         | L652
  cem signaling cas                   | 电路仿真接口视图         | L698
  crc                                 | 电路仿真接口视图         | L740
  connection                          | 交叉连接组视图          | L786
  connection remote-site-id           | 站点视图             | L844
  control-word enable                 | PW模板视图           | L898
  default                             | 电路仿真接口视图         | L960
  default-nexthop                     | 接口视图             | L996
  description (交叉连接组视图)               | 交叉连接组视图          | L1062
  description (电路仿真接口视图)              | 电路仿真接口视图         | L1108
  display bgp l2vpn signaling         | 任意视图             | L1150
  display interface circuit-emulation | 任意视图             | L1526
  display l2vpn bgp                   | 任意视图             | L1735
  display l2vpn ldp                   | 任意视图             | L2027
  display l2vpn forwarding            | 任意视图             | L2319
  display l2vpn interface             | 任意视图             | L2709
  display l2vpn pw                    | 任意视图             | L2809
  display l2vpn pw-class              | 任意视图             | L3139
  display l2vpn service-instance      | 任意视图             | L3295
  display l2vpn xconnect-group        | 任意视图             | L3475
  encapsulation                       | 以太网服务实例视图        | L3715
  idle-code                           | 电路仿真类视图          | L3809
  interface circuit-emulation         | 系统视图             | L3855
  interworking                        | 交叉连接视图           | L3897
  jitter-buffer                       | 电路仿真类视图          | L3957
  l2vpn enable                        | 系统视图             | L4007
  l2vpn reflector                     | 系统视图             | L4047
  l2vpn switchover                    | 用户视图             | L4127
  mtu                                 | 交叉连接视图/交叉连接组自动发现视图 | L4171
  payload                             |                  | L4237
  peer                                | 交叉连接视图           | L4297
  peer signaling                      | BGP L2VPN地址族视图   | L4391
  policy vpn-target                   | BGP L2VPN地址族视图   | L4451
  ppp ipcp ignore local-ip            | 接口视图             | L4497
  ppp ipcp proxy                      | 接口视图             | L4547
  protection dual-receive             | 交叉连接视图           | L4601
  pw-class (system view)              | 系统视图             | L4645
  pw-class (cross-connect auto-discovery view) | 交叉连接组自动发现视图      | L4699
  pw-type                             | PW模板视图           | L4761
  reset counters interface            | 用户视图             | L4819
  reset l2vpn statistics pw           | 用户视图             | L4865
  revertive                           | 交叉连接视图           | L4909
  route-distinguisher                 | 交叉连接组自动发现视图      | L4961
  rr-filter                           | BGP L2VPN地址族视图   | L5021
  rtp-header enable                   | 电路仿真类视图          | L5069
  sequencing both                     | PW模板视图           | L5111
  service-instance                    | 二层以太网接口视图/二层聚合接口视图 | L5165
  shutdown (交叉连接组视图)                  | 交叉连接组视图          | L5213
  shutdown (电路仿真接口视图)                 | 电路仿真接口视图         | L5261
  site                                | 交叉连接组自动发现视图      | L5299
  snmp-agent trap enable l2vpn        | 系统视图             | L5379
  statistics enable                   | 交叉连接PW视图         | L5431
  tunnel-policy                       | 自动发现交叉连接视图       | L5487
  vpn-target                          | 交叉连接组自动发现视图      | L5549
  xconnect-group                      | 系统视图             | L5613
-->

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ac interface**

------------------------------------------------------------------------

**[ac interface**]命令用来指定交叉连接关联的接口或以太网服务实例。

**[undo ac interface**]命令用来取消接口或以太网服务实例与交叉连接的关联。

【命令】

**[ac interface ***interface-type interface-number* [ **service-instance** *instance-id*  [ **access-mode** { **ethernet** \| **vlan** } ]]]

**[undo ac interface ***interface-type interface-number* [ **service-instance** *instance-id* ]]

【缺省情况】

交叉连接未关联接口或以太网服务实例。

【视图】

交叉连接视图/自动发现交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定与交叉连接关联的接口信息。*interface-type interface-number*为接口类型和接口编号。

**[service-instance** *instance-id*]：指定以太网服务实例。*instance-id*为以太网服务实例编号，取值范围为1～4096。

**[access-mode**]：指定接入模式。当关联交叉连接的AC为以太网服务实例时，可以指定本参数，接入模式缺省为VLAN；当AC为三层以太网接口时，接入模式始终为Ethernet，不可以指定本参数；当AC为三层以太网子接口、VLAN接口时，接入模式始终为VLAN，不可以指定本参数。

**[ethernet**]：指定接入模式为Ethernet。

**[vlan**]：指定接入模式为VLAN。

【使用指导】

在交叉连接视图/自动发现交叉连接视图下执行本命令后，从关联接口接收到的所有报文或符合指定以太网服务实例报文匹配规则的报文，将通过与该交叉连接关联的PW或另一条AC转发。

接入模式是PE对从CE收到的以太网帧携带的外层VLAN Tag的理解方式，以及PE向CE发送以太网帧的方式。接入模式分为两种：

·VLAN接入模式：CE发送给PE的以太网帧头需要带有一个VLAN Tag，该Tag被称为P-Tag，即服务提供商网络为了区分用户而添加的"服务定界符"。PE发送以太网帧给CE时，也需要携带P-Tag。

·Ethernet接入模式：CE发送给PE的以太网帧头中如果带有VLAN Tag，则该Tag被称为U-Tag，即用户网络的内部VLAN Tag，对于PE设备没有意义。PE发送以太网帧给CE时，不需要携带P-Tag。

需要注意的是，执行本命令关联以太网服务实例前，必须通过**encapsulation**命令为指定的以太网服务实例配置报文匹配规则。

【举例】

\# 在交叉连接组vpna的交叉连接aaa中关联接口GigabitEthernet1/0/1，使该接口接收到的所有报文都通过与该交叉连接关联的PW或另一条AC转发。

Sysname xconnect-group vpna

Sysname-xcg-vpna connection aaa

Sysname-xcg-vpna-aaa ac interface gigabitethernet 1/0/1

\# 接口GigabitEthernet1/0/1下采用以太网服务实例200来匹配外层VLAN Tag为200的报文，在交叉连接组vpn1的交叉连接actopw中关联该以太网服务实例。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 200

Sysname-GigabitEthernet1/0/1-srv200 encapsulation s-vid 200

Sysname-GigabitEthernet1/0/1-srv200 quit

Sysname-GigabitEthernet1/0/1 quit

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection actopw

Sysname-xcg-vpn1-actopw ac interface gigabitethernet 1/0/1 service-instance 200

\# 接口GigabitEthernet1/0/1下采用以太网服务实例200来匹配外层VLAN Tag为200的报文，在交叉连接组vpwsbgp的自动发现交叉连接视图下关联该以太网服务实例。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 200

Sysname-GigabitEthernet1/0/1-srv200 encapsulation s-vid 200

Sysname-GigabitEthernet1/0/1-srv200 quit

Sysname-GigabitEthernet1/0/1 quit

Sysname xconnect-group vpwsbgp

Sysname-xcg-vpwsbgp auto-discovery bgp

Sysname-xcg-vpwsbgp-auto site 1 range 10 default-offset 0

Sysname-xcg-vpwsbgp-auto-1 connection remote-site-id 2

Sysname-xcg-vpwsbgp-auto-1-2 ac interface gigabitethernet 1/0/1 service-instance 200

【相关命令】

·**connection**

·**display l2vpn ****interface**

·**display l2vpn ****service-instance**

·**encapsulation**

·**pw-type**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- address-family l2vpn**

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

在MPLS L2VPN组网中，要想建立BGP PW，需要在PE设备的BGP L2VPN地址族视图下通过**peer enable**命令使能BGP对等体，以便PE与该对等体交换L2VPN信息。

【举例】

\# 创建BGP L2VPN地址族，并进入BGP L2VPN地址族视图。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- auto-discovery**

------------------------------------------------------------------------

**[auto-discovery**]命令用来指定交叉连接组采用BGP方式自动发现邻居、建立PW，并进入交叉连接组自动发现视图。

**[undo auto-discovery**]命令用来取消交叉连接组采用BGP方式自动发现邻居并建立PW。

【命令】

**[auto-discovery bgp**]

**[undo auto-discovery**]

【缺省情况】

交叉连接组不会采用BGP方式自动发现邻居并建立PW。

【视图】

交叉连接组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bgp**]：指定交叉连接组采用BGP方式自动发现邻居并建立PW。

【使用指导】

执行本命令进入交叉连接组自动发现视图后，在该视图下可以配置BGP信令协议的相关参数，如本端站点、远端站点、Route Target属性等，以便PE设备通过BGP信令协议自动发现远端PE设备，并建立连接两端站点的PW。

【举例】

\# 指定名为bbb的交叉连接组使用BGP方式自动发现邻居、建立PW，并进入交叉连接组自动发现视图。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto

【相关命令】

·**display l2vpn pw**

·**display l2vpn xconnect-group**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- backup-peer**

------------------------------------------------------------------------

**[backup-peer**]命令用来配置交叉连接的备份PW，并进入交叉连接备份PW视图。如果指定的备份PW已存在，则直接进入交叉连接备份PW视图。

**[undo** **backup-peer**]命令用来删除交叉连接的备份PW。

【命令】

**[backup-peer ***ip-address* **pw-id** *pw-id* [ **in-label** *label-value* **out-label** *label-value*  [ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* ] \*]]

**[undo** **backup-peer** *ip-address* **pw-id** *pw-id*]

【缺省情况】

未配置交叉连接的备份PW。

【视图】

交叉连接PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定备份PW远端PE的LSR ID。

**[pw-id** *pw-id*]：指定备份PW的PW ID。*pw-id*为PW ID，取值范围为1～4294967295。

**[in-label**]*label-value*：指定备份PW的入标签。*label-value*为入标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[out-label**]*label-value*：指定备份PW的出标签。*label-value*为出标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[pw-class** *class-name*]：指定备份PW引用的PW模板。*class-name*表示PW模板名，为1～19个字符的字符串，区分大小写。PW模板中可以配置PW的数据封装类型、是否使用控制字等。如果不指定本参数，则PW数据封装类型由接口的链路类型决定，对于不强制要求使用控制字的PW数据封装类型，不支持控制字功能。

**[tunnel-policy*** tunnel-policy-name*]：指定备份PW的隧道选择策略。*tunnel-policy-name*表示隧道策略名，为1～19个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。

【使用指导】

备份PW作为主PW的备份，可以为主PW提供冗余保护。当主PW出现故障时，设备将通过主PW对应的备份PW转发流量。

需要注意的是：

·配置备份的静态PW时，必须指定**in-label**和**out-label**参数；配置备份的LDP PW时，无需指定此参数。

·配置备份PW时指定的远端PE的LSR ID和PW ID，不能与已经存在的VPLSPW、交叉连接PW的LSR ID和PW ID同时相同。

·PW冗余保护功能和多段PW功能互斥。即，如果在交叉连接视图下通过重复执行**peer**命令配置了两条PW，则在交叉连接PW视图下不能执行**backup-peer**命令配置备份PW；反之亦然。

·如果为静态PW指定的入标签与已经存在的静态LSP/静态CRLSP的入标签相同，则会导致标签冲突，静态PW不可用。即使修改静态LSP/静态CRLSP的入标签，静态PW仍不可用，需要手工删除该静态PW并重新配置。

【举例】

\# 为交叉连接组vpn2内的交叉连接pw2pw配置主备静态PW：主PW的远端PE地址为6.6.6.6，PW ID为100；备份PW的远端PE地址为7.7.7.7，PW ID为200。

\<Sysname\> system-view

Sysname xconnect-group vpn2

Sysname-xcg-vpn2 connection pw2pw

Sysname-xcg-vpn2-pw2pw peer 6.6.6.6 pw-id 100 in-label 16 out-label 17

Sysname-xcg-vpn2-pw2pw-6.6.6.6-100 backup-peer 7.7.7.7 pw-id 200 in-label 18 out-label 19

Sysname-xcg-vpn2-pw2pw-6.6.6.6-100-backup

【相关命令】

·**display l2vpn ldp**

·**display l2vpn pw**

·**peer**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置PW的期望带宽。

**[undo bandwidth**]用来恢复缺省情况。

【命令】

**[bandwidth ***bandwidth-value*]

**[undo bandwidth**]

【缺省情况】

接口的期望带宽为10000000kbps。

【视图】

交叉连接PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：PW的期望带宽，取值为1\~10000000，单位为kbps。

【使用指导】

接口的期望带宽会对CBQ队列带宽有影响。具体介绍请参见"ACL和QoS配置指导"中的"[拥塞管理"。]

【举例】

\# 在PW上配置期望带宽为10000kbps。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection pw2pw

Sysname-xcg-vpn1-pw2pw peer 1.1.1.1 pw-id 1

Sysname-xcg-vpn1-pw2pw-1.1.1.1-1 bandwidth 10000

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ccc**

------------------------------------------------------------------------

![说明](MPLS%20L2VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[ccc**]命令用来创建一条CCC（Circuit Cross Connect，电路交叉连接）远程连接。

**[undo ccc**]命令用来删除CCC远程连接。

【命令】

**[ccc in-label**[ *in-label-value* **out-label** *out-label-value* { **nexthop** *nexthop* \| **out-interface** *interface-type interface-number* } [ **pw-class** *class-name* ]]]

**[undo ccc**]

【缺省情况】

设备上不存在任何CCC远程连接。

【视图】

交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[in-label**]* in-label-value*：指定CCC远程连接的入标签。*in-label-value*为入标签值，取值范围为16～1023。

**[out-label**]* out-label-value*：指定CCC远程连接的出标签。*out-label-value*为出标签值，取值范围为16～1023。

**[nexthop ***nexthop*]：指定CCC远程连接的下一跳IP地址。

**[out-interface **]*interface-type interface-number*：指定CCC远程连接的出接口。*interface-type interface-number*为接口类型和接口编号。

**[pw-class **]*class-name*：指定CCC远程连接引用的PW模板。*class-name*表示PW模板名，为1～19个字符的字符串，区分大小写。PW模板中可以配置PW的数据封装类型、是否使用控制字等。如果不指定本参数，则PW数据封装类型由接口的链路类型决定，对于不强制要求使用控制字的PW数据封装类型，不支持控制字功能。

【使用指导】

CCC远程连接是通过在PE设备上手工指定入标签和出标签而建立的一条静态连接。CCC远程连接不需要公网隧道来承载，它通过在PE之间的P设备上配置两条方向相反的静态LSP，来实现报文跨越公网传送。通过CCC远程连接转发二层用户报文时，只需为用户报文封装一层标签。

建立CCC远程连接时，需要在本地PE和远端PE上均执行本命令创建CCC远程连接。如果两端PE之间存在P设备，则还需要在P设备上配置两条方向相反的静态LSP。配置时，需要确保为某一台设备指定的出标签必须与为其下一跳指定的入标签相同。

在交叉连接视图下建立CCC远程连接后，还需在该视图下执行**ac interface**命令指定关联的接口或以太网服务实例，以实现从关联接口接收到的所有报文或符合指定以太网服务实例报文匹配规则的报文，通过建立的CCC远程连接转发。

需要注意的是：

·只有出接口连接的链路是点到点链路时，才能够使用**out-interface**参数指定出接口。如果出接口连接的链路不是点到点链路，如出接口类型为三层以太网接口、VLAN接口或三层聚合接口，则必须使用**nexthop**参数指定下一跳IP地址。

·创建CCC远程连接时，需要保证两端PE上CCC远程连接的封装类型、控制字功能等配置保持一致，否则可能会导致报文转发失败。

【举例】

\# 在交叉连接视图下创建一条CCC远程连接：下一跳为10.1.1.1，入标签为100，出标签为200，引用的PW模板为pwc1。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb connection ccc1

Sysname-xcg-bbb-ccc1 ccc in-label 100 out-label 200 nexthop 10.1.1.1 pw-class pwc1

\# 在交叉连接视图下创建一条CCC远程连接：出接口为Serial2/1/0，入标签为100，出标签为200，引用的PW模板为pwc1。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb connection ccc1

Sysname-xcg-bbb-ccc1 ccc in-label 100 out-label 200 out-interface serial 2/1/0 pw-class pwc1

【相关命令】

·**ac interface**

·**display l2vpn pw**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem-class**

------------------------------------------------------------------------

**[cem-class**]命令用来创建一个电路仿真类，并进入电路仿真类视图。

**[undo cem-class**]命令用来删除电路仿真类。

【命令】

**[cem-class ***cem-class-name*]

**[undo cem-class** *cem-class-name*]

【缺省情况】

不存在任何电路仿真类。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cem-class-name*]：电路仿真类的名称，为1～19个字符的字符串，不区分大小写。

【使用指导】

通过本命令创建电路仿真类，并进入电路仿真类视图后，可在该视图下指定电路仿真的一组参数或属性，如Jitter-buffer的大小、每个分组净载荷的大小及分组丢失时的填充字符。

当多个TDM电路仿真业务采用相同的一组参数时，通过CEM（Circuit Emulation，电路仿真）类可以简化配置。

【举例】

\# 创建名为satop的电路仿真类，并进入电路仿真类视图。

\<Sysname\> system-view

Sysname cem-class satop

Sysname-cem-satop

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem class-attach**

------------------------------------------------------------------------

**[cem class-attach**]命令用来在接口上引用电路仿真类。

**[undo cem class-attach**]命令用来在接口上取消引用电路仿真类。

【命令】

**[cem class-attach **]*cem-class-name*

**[undo cem class-attach**]

【缺省情况】

接口未引用任何电路仿真类。

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[cem-class-name*]：电路仿真类的名称，为1～19个字符的字符串，不区分大小写。

【使用指导】

在电路仿真接口上引用电路仿真类后，该接口上TDM电路仿真业务采用的参数值为该电路仿真类下配置的值。

【举例】

\# 在E1控制器通道化出来的Circuit-Emulation2/3/0:0上引用电路仿真类satop。

\<Sysname\> system-view

Sysname controller e1 2/3/0

Sysname-E1 2/3/0 cem-set 0 timeslot-list 1-5

Sysname-E1 2/3/0 quit

Sysname interface circuit-emulation 2/3/0:0

Sysname-Circuit-Emulation2/3/0:0 cem class-attach satop

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem clock recover**

------------------------------------------------------------------------

**[cem clock recover**]命令用来配置电路仿真时钟恢复方式。

**[undo cem clock recover**]命令用来恢复缺省情况。

【命令】

**[cem clock recover**[ { **adaptive** \| **differential** }]]

**[undo cem clock recover**]

【缺省情况】

未配置电路仿真时钟恢复方式，即不进行时钟恢复。

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adaptive**]：Adaptive Clock Recovery，自适应时钟恢复方式。

**[differential**]：Differential Clock Recovery，差分时钟恢复方式。

【使用指导】

TDM电路采用时分复用技术，有严格的系统时钟同步要求，以传送实时同步业务。而分组交换网是基于统计复用的分组交换技术，接收端与发送端没有严格的时钟同步要求。所以，当采用分组网来传输TDM业务时，出口PE需进行时钟恢复，时钟恢复方式有以下两种：

·ACR（Adaptive Clock Recovery，自适应时钟恢复）：出口PE根据报文的到达速率和Jitter buffer的填充水平进行时钟恢复。此方式在入口PE和出口PE没有相同的时钟源时使用。

·DCR（Differential Clock Recovery，差分时钟恢复）：出口PE根据报文的RTP头中的差分时间戳信息进行时钟恢复。此方式在当出口PE和入口PE具有相同的时钟源时使用。

【举例】

\# 配置电路仿真时钟恢复方式为自适应时钟恢复方式。

\<Sysname\> system-view

Sysname interface circuit-emulation 2/3/0:0

Sysname-Circuit-Emulation2/3/0:0 cem clock recover adaptive

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem clock transmit differential**

------------------------------------------------------------------------

**[cem clock transmit differential**]命令用来配置采用差分方式传送时间戳。

**[undo cem clock transmit differential**]命令用来恢复缺省情况。

【命令】

**[cem clock transmit differential**]

**[undo cem clock transmit differential**]

【缺省情况】

采用绝对方式传送时间戳。

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

时间戳的传送方式有两种：绝对模式和差分模式。

·绝对模式：入口PE采用从用户侧TDM电路恢复出的时钟来设置RTP头的时间戳。

·差分模式：PW连接的两台PE设备访问同一个高质量同步时钟源，时钟传送的发送方采用TDM时钟与高质量同步时钟源的差值来设置RTP头的时间戳。

【举例】

\# 配置采用差分方式传送时间戳。

\<Sysname\> system-view

Sysname interface circuit-emulation 2/3/0:0

Sysname-Circuit-Emulation2/3/0:0 cem clock transmit differential

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem signaling cas**

------------------------------------------------------------------------

**[cem signaling cas**]命令用来配置电路仿真接口上使用的信令类型为CAS（Channel-associated signaling，随路信令）。

**[undo cem signaling cas**]命令用来恢复缺省情况。

【命令】

**[cem signaling cas**]

**[undo cem signaling cas**]

【缺省情况】

未配置信令类型。

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当对CAS的DS0（数字信号0）业务进行CESoPSN方式的电路仿真时，需通过本命令配置电路仿真接口上使用的信令类型为CAS。

【举例】

\# 配置电路仿真接口上使用的信令类型为随路信令。

\<Sysname\> system-view

Sysname interface circuit-emulation 2/3/0

Sysname-Circuit-Emulation2/3/0 cem signaling cas

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- crc**

------------------------------------------------------------------------

**[crc**]命令用来配置电路仿真接口的CRC校验模式。

**[undo crc**]命令用来恢复缺省情况。

【命令】

**[crc **[{ **16** \| **32** \| **none** }]]

**[undo crc**]

【缺省情况】

使用16位CRC校验。

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[16**]：电路仿真接口使用16位CRC校验。

**[32**]：电路仿真接口使用32位CRC校验。

**[none**]：电路仿真接口不进行CRC校验。

【举例】

\# 配置电路仿真接口Circuit-Emulation2/3/0:0使用32位CRC校验。

\<Sysname\> system-view

Sysname interface circuit-emulation 2/3/0:0

Sysname-Circuit-Emulation2/3/0:0 crc 32

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- connection**

------------------------------------------------------------------------

**[connection**]命令用来创建一条交叉连接，并进入交叉连接视图。如果指定的连接已经存在，则直接进入交叉连接视图。

**[undo connection**]命令用来删除指定的交叉连接。

【命令】

**[connection ***connection-name*]

**[undo connection ***connection-name*]

【缺省情况】

设备上不存在任何L2VPN交叉连接。

【视图】

交叉连接组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[connection-name*]：交叉连接的名称，为1～20个字符的字符串，不能包含字符"-"，区分大小写。

【使用指导】

L2VPN的交叉连接为点到点连接。

在交叉连接视图下，可以：

·执行一次**ac interface**命令和一次**peer**命令将AC和PW关联，以实现从指定AC接收到的报文通过指定的PW转发、从指定PW上接收到的报文转发给指定AC。

·执行两次**ac interface**命令将两条AC关联，以实现报文在两个AC之间进行本地交换。

·执行两次**peer**命令将两条PW关联，以实现多段PW功能。

·执行一次**ac interface**命令和一次**ccc**命令将AC和CCC远程连接关联，以实现从指定AC接收到的报文通过指定的CCC远程连接转发、从指定CCC远程连接上接收到的报文将转发给指定AC。

【举例】

\# 为交叉连接组vpn1创建名为ac2pw的交叉连接，并进入交叉连接视图。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection ac2pw

Sysname-xcg-vpn1-ac2pw

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- connection remote-site-id**

------------------------------------------------------------------------

**[connection **]**remote-site-id**命令用来创建交叉连接，并进入自动发现交叉连接视图。如果指定的交叉连接已经存在，则直接进入自动发现交叉连接视图。

**[undo** **connection** ]**remote-site-id**命令用来删除指定的交叉连接。

【命令】

**[connection**]**remote-site-id*** remote-site-id*

**[undo connection**]**remote-site-id*** remote-site-id*

【缺省情况】

设备上不存在任何交叉连接。

【视图】

站点视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[remote-site-id*]：远端站点的ID。取值范围为0～250。

【使用指导】

执行本命令后，设备将会在创建交叉连接的同时，采用BGP方式在当前站点和指定的远端站点之间建立一条PW，该PW与该交叉连接关联。

自动发现交叉连接视图下，可以执行**ac** **interface**命令将交叉连接与指定的AC关联，以实现从指定AC接收到的报文通过与该交叉连接关联的PW转发、从该PW上接收到的报文将转发给指定AC。

【举例】

\# 在站点视图下创建交叉连接，同时创建连接本地站点1和远端站点3的BGP PW，并进入自动发现交叉连接视图。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto site 1 range 10

Sysname-xcg-bbb-auto-1 connection remote-site-id 3

Sysname-xcg-bbb-auto-1-3

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- control-word enable**

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

·传送特定二层数据帧的标记：如帧中继的FECN（Forward Explicit Congestion Notification，前向显式拥塞通知）比特和BECN（Backward Explicit Congestion Notification，后向显示拥塞通知）比特等。

·传送TDM电路的OAM相关标记：如LOS（Loss of Signal，信号丢失）和AIS（Alarm Indication Signal，告警指示信号）等。

·指示净载荷长度：如果PW上传送报文的净载荷长度小于64字节，则需要对报文进行填充，以避免报文发送失败。此时，通过控制字的载荷长度字段可以确定原始载荷的长度，以便从填充后的报文中正确获取原始的报文载荷。

![说明](MPLS%20L2VPN命令.files/image002.png)

上述功能的支持情况与设备的型号有关，请以设备的实际情况为准。

对于某些PW数据封装类型（如帧中继DLCI类型、ATM AAL5 SDU VCC类型），PW上传递的报文必须携带控制字字段，不能通过配置来控制；对于某些PW数据封装类型（如Ethernet、VLAN），控制字字段是可选的，可以通过配置来决定是否携带控制字。

本命令用来配置对于控制字字段可选的PW数据封装类型，本端是否支持携带控制字字段。报文实际是否携带控制字字段，由两端的配置共同决定：如果两端PE上都使能了控制字功能，则报文中携带控制字字段；否则，报文中不携带控制字字段。

【举例】

\# 使能PW模板pw100的控制字功能。

\<Sysname\> system-view

Sysname pw-class pw100

Sysname-pw-pw100 control-word enable

【相关命令】

·**display l2vpn pw-class**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复当前电路仿真接口的缺省配置。

【命令】

**[default**]

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将电路仿真接口Circuit-Emulation2/3/0:0恢复为缺省配置。

\<Sysname\> system-view

Sysname interface circuit-emulation 2/3/0:0

Sysname-Circuit-Emulation2/3/0:0 default

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- default-nexthop**

------------------------------------------------------------------------

**[default-nexthop**]命令用来配置缺省下一跳信息。

**[undo default-nexthop**]命令用来恢复缺省情况。

【命令】

**[default-nexthop **[{ **ip** *ip-address* \| **mac** { *mac-address \|* **broadcast** } }]]

**[undo default-nexthop**]

【缺省情况】

未指定缺省下一跳信息。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip ***ip-address*]：指定缺省下一跳的IP地址。

**[mac**]：指定缺省下一跳的MAC地址。

*[mac-address*]：缺省下一跳的MAC地址。

**[broadcast**]：采用广播MAC地址作为缺省下一跳的MAC地址。

【使用指导】

MPLS L2VPN连接异构网络，且CE接入PE的链路类型为Ethernet时，PE上需要设置缺省下一跳信息，以便PE正确地为发送给CE的报文封装链路层头。

缺省下一跳信息为CE的MAC地址或广播MAC地址时，PE发送给CE的报文将以该MAC地址作为目的MAC地址；缺省下一跳信息为CE的IP地址时，PE通过ARP将IP地址解析为MAC地址，解析到的MAC地址将作为PE发送给CE的报文的目的MAC地址。

【举例】

·路由应用

\# 在PE连接CE的接口GigabitEthernet1/0/1上配置缺省下一跳的IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 default-nexthop ip 1.1.1.1

·交换应用

\# 在PE连接CE的接口Vlan-interface10上配置缺省下一跳的IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 default-nexthop ip 1.1.1.1

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- description (交叉连接组视图)**

------------------------------------------------------------------------

**[description**]命令用来设置交叉连接组的描述信息。

**[undo description**]命令用来删除交叉连接组的描述信息。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

未配置交叉连接组的描述信息。

【视图】

交叉连接组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：交叉连接组的描述信息，为1～80个字符的字符串，区分大小写。

【举例】

\# 配置名为vpn2的交叉连接组的描述信息为"vpws for vpn2"。

\<Sysname\> system-view

Sysname xconnect-group vpn2

Sysname-xcg-vpn2 description vpws for vpn2

【相关命令】

·**display l2vpn ****xconnect-group**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- description (电路仿真接口视图)**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo** **description**]

【缺省情况】

接口的描述信息为"*接口名* Interface"，比如：Circuit-Emulation2/3/0:0 Interface。

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置电路仿真接口Circuit-Emulation2/3/0:0的描述信息为"router-interface"。

\<Sysname\> system-view

Sysname interface circuit-emulation 2/3/0:0

Sysname-Circuit-Emulation2/3/0:0 description router-interface

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display bgp l2vpn signaling**

------------------------------------------------------------------------

**[display bgp l2vpn signaling**]命令用来显示BGP协议的MPLS L2VPN标签块信息。

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

**[peer ***ip-address*]：显示向指定对等体发布或者从指定对等体收到的BGP协议的MPLS L2VPN标签块信息。*ip-address*表示对等体的IP地址。

**[advertised**]：显示向指定对等体发布的BGP协议的MPLS L2VPN标签块信息。

**[received**]：显示从指定对等体接收到的BGP协议的MPLS L2VPN标签块信息。

**[statistics**]：显示BGP协议的MPLS L2VPN标签块的统计信息。

**[route-distinguisher*** route-distinguisher*]：显示指定路由标识符的BGP协议MPLS L2VPN标签块信息。*route-distinguisher*为路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号:16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[site-id*** site-id*]：显示为指定站点分配的BGP协议的MPLS L2VPN标签块信息。*site-id*为站点编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[label-offset ***label-offset*]：显示标签块偏移量为指定值的BGP协议MPLS L2VPN标签块信息。*label-offset*为标签块偏移量，取值范围为0～65535。

**[advertise-info**]：显示BGP协议MPLS L2VPN标签块的通告信息。

【使用指导】

执行本命令时，如果没有指定任何参数，则显示所有BGP协议MPLS L2VPN标签块的简要信息。

【举例】

\# 显示所有BGP协议MPLS L2VPN标签块的简要信息。

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

表1-1 display bgp l2vpn signaling命令简要显示信息描述表

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

·e -- EGP：表示是通过EGP（Exterior Gateway Protocol，外部网关协议）学到的

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

下一跳地址

\# 显示路由标识符为2:2、为站点2分配的、标签块偏移量为0的BGP协议MPLS L2VPN标签块的详细信息。

\<Sysname\> display bgp l2vpn signaling route-distinguisher 2:2 site-id 2 label-offset 0

 BGP local router ID: 192.168.1.135

 Local AS number: 100

 Route distinguisher: 2:2

 Total number of label blocks: 1

 Paths:   1 available, 1 best

 From            : 192.3.3.3 (192.168.1.140)

 Original nexthop: 192.3.3.3

 Ext-Community   : \<RT: 2:2\>, \<L2VPN info: MTU 1500, Encap type VLAN\>

 AS-path         : (null)

 Origin          : igp

 Attribute value : localpref 100, pref-val 0

 Site ID         : 2

 LB offset       : 0

 LB base         : 1162

 LB range        : 10

 State           : valid, internal, best

 CSV             : 0x01000ABFFF

表1-2 display bgp l2vpn signaling命令详细显示信息描述表

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

CSV

接入链路状态

\# 显示指定MPLS L2VPN标签块的通告信息。

\<Sysname\> display bgp l2vpn signaling route-distinguisher 2:2 site-id 1 label-offset 0 advertise-info

 BGP local router ID: 192.168.1.135

 Local AS number: 100

 Route distinguisher: 2:2

 Total number of label blocks: 1

 Paths:   1 best

 Site ID         : 1

 LB offset       : 0

 LB base         : 1034

 LB range        : 10

 CSV             : 0x01000ADFFF

 Advertised to peers (1 in total):

    192.3.3.3

表1-3 display bgp l2vpn signaling adveritse-info命令显示信息描述表

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

·available：有效可达信息条数

·best：最佳可达信息条数

Site ID

站点编号

LB offset

标签块偏移量

LB base

标签块的初始标签值

LB range

标签块大小

CSV

接入链路状态

Advertised to peers (1 in total)

该信息已经向哪些对等体发送，以及对等体的数目

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display interface circuit-emulation**

------------------------------------------------------------------------

**[display interface circuit-emulation**]命令用来显示电路仿真接口的相关信息。

【命令】

**[display interface** [ **circuit-emulation** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定电路仿真接口的信息。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**circuit-emulation**参数，将显示设备支持的所有接口的相关信息。

·如果指定**circuit-emulation**参数，不指定*interface-number*参数，将显示所有已创建的电路仿真接口的相关信息。

【举例】

\# 显示电路仿真接口Circuit-Emulation2/3/0:0的详细信息。

\<Sysname\> display interface circuit-emulation 2/3/0:0

Circuit-Emulation 2/3/0:0

Current state: UP

Line protocol state: UP

Description: Circuit-Emulation2/3/0:0 Interface

Bandwidth: 64kbps\
Maximum Transmit Unit: 0\
Internet protocol processing: disabled\
Last clearing of counters: Never

\# 显示电路仿真接口Circuit-Emulation2/3/0:0的概要信息。

\<Sysname\> display interface circuit-emulation 2/3/0:0 brief

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

Cem2/3/0:0           DOWN \--      \--     \--   \--

\# 显示当前物理状态为down的电路仿真接口的信息以及down的原因。

\<Sysname\> display interface circuit-emulation brief down

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

Cem2/3/0:0           DOWN Not connected

表1-4 display interface circuit-emulation命令显示信息描述表

字段

描述

Current state

电路仿真接口当前的物理状态和管理状态，可能的取值及含义如下：

·DOWN（Administratively）：表示该电路仿真接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该电路仿真接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该电路仿真接口的管理状态和物理状态均为开启

Line protocol state

该接口的链路层协议状态，可能的状态及含义如下：

·UP：表示数据链路层协议状态为开启

·DOWN：表示数据链路层协议状态为关闭

Description

接口的描述信息

Bandwidth

接口的期望带宽

Maximum Transmit Unit

接口的最大传输单元

Internet protocol processing

网络层协议处理状况

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Brief information on interface(s) under bridge mode:

接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Speed or Duplex: (a)/A - auto; H - half; F - full

如果某接口的Speed属性值为"(a)"，则表示该接口的速率是通过自动协商获取的

如果某接口的Duplex属性值为"(a)"或者"A"，则表示该接口的Duplex属性是通过自动协商获取的；取值为"H"则表示为半双工；取值为"F"则表示为全双工

Type: A - access; T - trunk; H - hybrid

接口的链路类型，

·A：表示Access链路类型

·H：表示Hybrid链路类型

·T：表示Trunk链路类型

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Speed

接口的速率，单位为bps

Duplex

接口的双工模式，取值为：

·A：表示双工模式由自动协商结果决定

·F：表示全双工

·F(a)：表示自由协商的结果为全双工

·H：表示半双工

·H(a)：表示自由协商的结果为半双工

Type

链路类型，取值为：

·A：表示Access链路类型

·H：表示Hybrid链路类型

·T：表示Trunk链路类型

PVID

接口所在的缺省VLAN ID

Interface

接口名称缩写

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn bgp**

------------------------------------------------------------------------

**[display l2vpn bgp**]命令用来显示MPLS L2VPN的标签块信息。

【命令】

**[display l2vpn bgp**[ [ **local** \| **peer** *ip-address* ]  **xconnect-group** ]*group-name*  **verbose** ]

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

**[xconnect-group**]*group-name*：显示指定交叉连接组内的标签块信息。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。如果没有指定本参数，则显示所有交叉连接组的标签块信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【使用指导】

执行本命令时指定了**peer*** ip-address*参数，如果存在与从远端PE接收到的标签块匹配的本地标签块，即接收到的标签块信息中携带的远端Site ID满足条件：本地标签块LO\<=远端Site ID\<=本地标签块LO+LR-1，则同时显示远端标签块和匹配的本地标签块信息；否则，只显示从远端PE接收到的标签块信息。

执行本命令时，如果没有指定**peer*** ip-address*和**local**参数，则显示从所有远端PE接收到的标签块信息。如果存在与远端标签块匹配的本地标签块，则同时显示本地标签块信息。

【举例】

\# 显示从所有远端PE接收到的标签块的简要信息。

\<Sysname\> display l2vpn bgp

Total number of BGP PWs: 1, 1 up, 0 down

Xconnect-group Name: vpnb, Site ID:1

Rmt Site   Offset  RD                    Nexthop          In/Out Label     State

2          0       2:2                   192.3.3.3        1036/1163        Up

表1-5 display l2vpn bgp命令显示信息描述表

字段

描述

Total number of BGP PWs

BGP PW的总数，及处于up和down状态的BGP PW数目

Xconnect-group Name

交叉连接组名称

Site ID

本端Site标识符

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

Xconnect-group Name: vpnb, Site ID:1

 Remote Site ID     : 2

 Offset             : 0

 RD                 : 2:2

 PW State           : Up

 Encapsulation      : VLAN

 MTU                : 1500

 Nexthop            : 192.3.3.3

 Local VC Label     : 1036

 Remote VC Label    : 1163

 Link ID            : 1

 Local Label Block  : 1034/10/0

 Remote Label Block : 1162/10/0

 Export Route Target: 2:2

表1-6 display l2vpn bgp verbose命令显示信息描述表

字段

描述

Xconnect-group Name

交叉连接组名称

Site ID

本端Site标识符

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

PW在交叉连接内的链路标识符

Local Label Block

本端的标签块信息，包括标签块的初始标签值/标签块大小/标签块的偏移量

Remote Label Block

从远端收到的标签块信息，包括标签块的初始标签值/标签块大小/标签块的偏移量

Export Route Target

从远端收到的标签块对应的Route Target属性

\# 显示所有本地分配的标签块的简要信息。

\<Sysname\> display l2vpn bgp local

Xconnect-group Name: vpnb

Site   Offset  Range  Label Base    RD

1      0       10     1034          2:2

表1-7 display l2vpn bgp local命令显示信息描述表

字段

描述

Xconnect-group Name

交叉连接组名称

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

Xconnect-group Name: vpnb

 Site ID            : 1

 Offset             : 0

 RD                 : 2:2

 Range              : 10

 Label Base         : 1034

 Link ID            : 1

表1-8 display l2vpn bgp local verbose命令显示信息描述表

字段

描述

Xconnect-group Name

交叉连接组名称

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

对于MPLS L2VPN来说，由于每个交叉连接下只能创建一条BGP PW，因此Link ID固定为1

【相关命令】

·**display l2vpn pw**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn ldp**

------------------------------------------------------------------------

**[display l2vpn ldp**]命令用来显示LDP协议通告的PW标签相关信息。

【命令】

**[display l2vpn ldp **[ **peer** *ip-address* [ **pw-id** *pw-id*  \| ]]**xconnect-group ***group-name*  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer*** ip-address*]：显示指定远端PE通过LDP通告的PW标签相关信息。*ip-address*为远端PE的LSR ID。如果没有指定本参数，则显示所有远端PE通过LDP通告的PW标签相关信息。

**[pw-id ***pw-id*]：显示指定PW的PW标签相关信息。*pw-id*为PW的PW ID，取值范围为1～4294967295。如果指定了**peer*** ip-address*参数，没有指定本参数，则显示指定远端PE通过LDP通告的所有PW标签相关信息。

**[xconnect-group **]*group-name*：显示指定交叉连接组内LDP协议通告的PW标签相关信息。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。如果没有指定本参数，则显示所有交叉连接组内LDP协议通告的PW标签相关信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【举例】

\# 显示LDP协议通告的所有PW标签的简要信息。

\<Sysname\> display l2vpn ldp

Total number of LDP PWs: 5, 4 up, 1 down

Peer            PW ID/VPLS ID         In/Out Label    State Owner

192.3.3.3       1001                  775125/775126   Up    vpws1

192.3.3.3       1001                  775125/775126   Up    vpws1

192.3.3.3       1003                  775117/775122   Up    vpws3

192.3.3.3       1004                  775120/775120   Up    vpws4

192.4.4.4       1000                  775116/unknown  Down  vpws5

表1-9 display l2vpn ldp命令显示信息描述表

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

PW所属交叉连接组的名称

\# 显示LDP协议通告的所有PW标签的详细信息。

\<Sysname\> display l2vpn ldp verbose

Peer: 192.2.2.2        PW ID: 1000

  Xconnect-group: vpn1

  Connection    : ldp

  PW State      : Up

  PW Status Communication: Notification method

  PW ID FEC (Local/Remote):

    PW Type     : VLAN/VLAN

    Group ID    : 0/0

    Label       : 1151/1279

    Control Word: Disabled/Disabled

    VCCV CC Type: -/-

    VCCV CV Type: -/-

    MTU         : 1500/1500

    PW Status   : PW forwarding/PW forwarding

Peer: 192.3.3.3        PW ID: 1

  Xconnect-group: x1

  Connection    : c1

  PW State      : Up

  PW Status Communication: Notification method

  PW ID FEC (Local/Remote):

    PW Type     : TDM-CESoPSN-Basic/TDM-CESoPSN-Basic

    Group ID    : 0/0

    Label       : 710127/710127

    Control Word: Enabled/Enabled

    VCCV CV Type: LSP Ping/LSP Ping

    VCCV CC Type: -/-

    Bit Rate    : 10/10

    Payload     : 80/80

    RTP Header  : Enabled/Enabled

    Timestamping: Differential/Differential

    Frequency   : 0/0

    PW Status   : PW forwarding/PW forwarding

表1-10 display l2vpn ldp verbose命令显示信息描述表

字段

描述

Peer

PW远端PE的IP地址

PW ID

PW标识符

Xconnect-group

PW所属交叉连接组的名称

Connection

PW所属交叉连接的名称

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

VCCV CC Type

支持的VCCV CC（Control Channel，控制通道）类型，取值包括：

·Control-Word：控制字类型

·Router-Alert：MPLS路由器告警标签类型

·TTL：TTL超时类型

VCCV（Virtual Circuit Connectivity Verification，虚电路连通性验证）的详细介绍，请参见"MPLS配置指导"中的"MPLS OAM"

VCCV CV Type

支持的VCCV CV（Connectivity Verification，连通性验证）类型，取值包括：

·LSP Ping：采用MPLS ping检测PW的连通性

·BFD：采用BFD检测PW的连通性，BFD报文的封装方式为IP/UDP Encapsulation (with IP/UDP Headers)

·Raw-BFD：采用BFD检测PW的连通性，BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头

MTU

交叉连接的最大传输单元

Bit Rate

TDM接口比特率，取值与电路仿真接口的电路类型有关（单位：64Kbit/s）：

·SAToP的E1口：32

·SAToP的T1口：24

·CESoPSN的E1或T1接口：时隙数

Payload

TDM接口的负载大小，单位为字节

RTP Header

是否使能RTP头，取值包括：

·Enabled：使能RTP头

·Disabled：未使能RTP头

Timestamping

RTP头上时间戳的传送方式，取值包括：

·Differential：差分时钟模式

·Absolute：绝对时钟模式

Frequency

RTP头上打时间戳的时钟频率

PW Status

PW状态，取值包括：

·PW forwarding：PW可以转发报文

·PW not forwarding：PW不可以转发报文

·AC receive fault：AC接收方向失效

·AC transmit fault：AC发送方向失效

·PW receive fault：PW接收方向失效

·PW transmit fault：PW发送方向失效

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn forwarding**

------------------------------------------------------------------------

**[display l2vpn forwarding**]命令用来显示交叉连接的转发信息。

【命令】

集中式设备：

**[display l2vpn forwarding**[ { **ac** \| **pw** } ]**xconnect-group ***group-name*  **verbose** ]

分布式设备―独立运行模式/集中式IRF设备：

**[display l2vpn forwarding**[ { **ac** \| **pw** } ]**xconnect-group ***group-name* \**slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]

分布式设备－IRF模式：

**[display l2vpn forwarding**[ { **ac** \| **pw** } ]**xconnect-group ***group-name *  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]

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

**[xconnect-group **]*group-name*：显示指定交叉连接组的转发信息。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有交叉连接组的转发信息。

**[slot*** slot-number*]：显示指定单板上的交叉连接转发信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示主用主控板上的交叉连接转发信息。（分布式设备―独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的交叉连接转发信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，则显示Master设备上的交叉连接转发信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的交叉连接转发信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，则显示Master设备上的交叉连接转发信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定成员设备上指定单板的交叉连接转发信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，则显示Master设备上主用主控板的交叉连接转发信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的交叉连接转发信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，则显示Master设备上主用主控板的交叉连接转发信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的交叉连接转发信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【举例】

\# 显示所有交叉连接组的AC转发简要信息。

\<Sysname\> display l2vpn forwarding ac

Total number of cross-connections: 3

Total number of ACs: 3

AC                               Xconnect-group                  Link ID

GE1/0/5 srv1                     vpn1                            0

GE1/0/5 srv2                     vpn2                            1

GE1/0/6                          vpn3                            0

表1-11 display l2vpn forwarding ac命令显示信息描述表

字段

描述

Total number of cross-connections

所有交叉连接组或指定交叉连接组下交叉连接的总数，包括没有关联AC的交叉连接

Total number of ACs

所有交叉连接组或指定交叉连接组下AC的总数

AC

接入电路，取值有如下两种：

·三层接口名称：如GE1/0/6。在交叉连接视图下关联三层接口时，AC取值为此方式

·二层接口名称和以太网服务实例：如GE1/0/5 srv1。在交叉连接视图下关联以太网服务实例时，AC取值为此方式

Xconnect-group

AC所属交叉连接组的名称

Link ID

AC在交叉连接内的链路标识符

\# 显示所有交叉连接组的AC转发详细信息。

\<Sysname\> display l2vpn forwarding ac verbose

Xconnect-group: vpws1

 Connection: actopw

  Interface: GE1/0/3  Service Instance: 1

    Link ID      : 1

    Access Mode  : VLAN

    Encapsulation: s-vid 1 to 16

 Connection: actoac

  Interface: Vlan13

    Link ID      : 0

    Access Mode  : VLAN

  Interface: GE1/0/3  Service Instance: 4

    Link ID      : 1

    Access Mode  : VLAN

    Encapsulation: untagged

    Reflector    :

      IP Address   : 100.1.1.4

      MAC Address  : 8850-fc51-5cee

      Src Port     : 200

      Dst Port     : 201

Xconnect-group: vpws5

 Connection: actopw

  Interface: Vlan14

    Link ID      : 0

    Access Mode  : VLAN

表1-12 display l2vpn forwarding ac verbose命令显示信息描述表

字段

描述

Xconnect-group

交叉连接组名称

Connection

交叉连接名称

Interface

接入接口

Service Instance

以太网服务实例，AC为二层接口的以太网服务实例时才显示该字段

Link ID

AC在交叉连接内的链路标识符

Access Mode

AC接入模式，取值包括：

·VLAN：VLAN模式

·Ethernet：Ethernet模式

Encapsulation

以太网服务实例的报文匹配规则，AC为二层接口的以太网服务实例时才显示该字段

Reflector

报文反射信息

IP Address

待反射报文的目的IP地址

MAC Address

待反射报文的目的MAC地址

Src Port

待反射报文的源UDP端口号

Dst Port

待反射报文的目的UDP端口号

\# 显示所有交叉连接组的PW转发简要信息。

\<Sysname\> display l2vpn forwarding pw

Total number of cross-connections: 1

Total number of PWs: 2, 2 up, 0 blocked, 0 down

Xconnect-group                  In/Out Label    NID        Link ID    State

vpn1                            1279/1151       1025       0          Up

vpn1                            1278/1151       1027       1          Up

表1-13 display l2vpn forwarding pw命令显示信息描述表

字段

描述

Total number of cross-connections

所有交叉连接组或指定交叉连接组下交叉连接的总数，包括没有配置PW的交叉连接

Total number of PWs

所有交叉连接组或指定交叉连接组下PW总数，以及处于up、blocked、down状态的PW数目

Xconnect-group

PW所属交叉连接组的名称

In/Out Label

PW的入标签和出标签

NID

承载PW的隧道对应的NHLFE表项索引

·存在等价隧道时，一个PW会对应多个NID

·如果不存在隧道，显示为None

Link ID

PW在交叉连接内的链路标识符

State

PW的状态，取值包括Up、Down、Blocked和BFD Defect

其中，Blocked为存在主备PW的情况下，当前没有转发流量、起到备份作用的PW的状态；BFD Defect为BFD检测到PW存在缺陷的状态

\# 显示所有交叉连接组的PW转发详细信息。

\<Sysname\> display l2vpn forwarding pw verbose

Xconnect-group: vpn1

 Connection: ldp

  Link ID: 0

    PW Type         : VLAN                  PW State : Up

    In Label        : 1279                  Out Label: 1151

    MTU             : 1500

    PW Attributes   : Main

    VCCV CC         : Router-Alert

    VCCV BFD        : Fault Detection with BFD

    Tunnel Group ID : 0x60000000

    Tunnel NHLFE IDs: 1025

  Link ID: 1

    PW Type         : VLAN                  PW State : Up

    In Label        : 1278                  Out Label: 1151

    MTU             : 1500

    PW Attributes   : Main

    VCCV CC         : Router-Alert

    VCCV BFD        : Fault Detection with BFD

    Tunnel Group ID : 0x160000001

    Tunnel NHLFE IDs: 1027

表1-14 display l2vpn forwarding pw verbose命令显示信息描述表

字段

描述

Xconnect-group

交叉连接组名称

Connection

交叉连接名称

Link ID

PW在交叉连接内的链路标识符

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

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn interface**

------------------------------------------------------------------------

**[display l2vpn interface**]命令用来显示与交叉连接关联的三层接口的L2VPN信息。

【命令】

**[display l2vpn interface ****xconnect-group ***group-name*[\| *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[xconnect-group **]*group-name*：显示指定交叉连接组内与交叉连接关联的三层接口的L2VPN信息。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。

*[interface-type interface-number*]：显示指定接口的L2VPN信息。*interface-type interface-number*为接口类型和接口编号。

【使用指导】

执行本命令时，如果没有指定任何参数，则显示所有与交叉连接关联的三层接口的L2VPN信息。

本命令只能显示与交叉连接关联的三层接口的L2VPN信息。若要显示以太网服务实例的L2VPN信息，则需要执行**display l2vpn service-instance**命令。

【举例】

·路由应用

\# 显示所有与交叉连接关联的三层接口的L2VPN信息。

\<Sysname\> display l2vpn interface

Total number of interfaces: 2, 2 up, 0 down

Interface                Owner                           Link ID   State    Type

GE1/0/1                  vpws1                           1         Up       VPWS

GE1/0/2                  vpws2                           1         Up       VPWS

·交换应用

\# 显示所有与交叉连接关联的三层接口的L2VPN信息。

\<Sysname\> display l2vpn interface

Total number of interfaces: 2, 2 up, 0 down

Interface                Owner                           Link ID   State    Type

Vlan10                   vpws1                           0         Up       VPWS

Vlan11                   vpws2                           0         Up       VPWS

表1-15 display l2vpn interface命令显示信息描述表

字段

描述

Total number of interfaces

与交叉连接关联的三层接口的总数，及处于up和down状态的接口数目

Interface

与交叉连接关联的三层接口的名称

Owner

接口所属的交叉连接组名称

Link ID

接口对应AC在交叉连接内的链路标识符

State

接口的状态，取值包括Up和Down

Type

接口所属的L2VPN类型，取值包括VSI和VPWS

【相关命令】

·**display l2vpn service-instance**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn pw**

------------------------------------------------------------------------

**[display l2vpn pw**]命令用来显示L2VPN的PW信息。

【命令】

**[display** **l2vpn** **pw** **xconnect-group ***group-name*  [ **protocol** { **bgp** \| **ldp** \| **static** } ]  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[xconnect-group **]*group-name*：显示指定交叉连接组内L2VPN的PW信息。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。如果没有指定本参数，则显示所有交叉连接组内L2VPN的PW信息。

**[protocol**]：显示采用指定信令协议建立的PW的信息。如果没有指定本参数，则显示所有协议产生的PW信息。

**[bgp**]：显示采用BGP作为PW信令协议建立的PW的信息，即BGP PW信息。

**[ldp**]：显示采用LDP作为PW信令协议建立的PW的信息，即LDP PW信息。

**[static**]：显示采用静态方式建立的PW的信息，即静态PW信息，包括CCC远程连接信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【使用指导】

开启PW统计功能后，可使用**display l2vpn pw verbose**命令查看PW的报文统计信息。

【举例】

\# 显示L2VPN所有PW的简要信息。

\<Sysname\> display l2vpn pw

Flags: M - main, B - backup, H - hub link, S - spoke link, N - no split horizon

Total number of PWs: 2

2 up, 0 blocked, 0 down, 0 defect, 0 idle, 0 duplicate

Xconnect-group Name: ldp

Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State

192.3.3.3       500               1299/1299       LDP     M     0        Up

Xconnect-group Name: vpnb

Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State

192.3.3.3       2                 1036/1163       BGP     M     1        Up

表1-16 display l2vpn pw命令显示信息描述表

字段

描述

Flags

PW属性标记的取值

Total number of PWs

PW的总数，及处于up、blocked、down、defect、idle和duplicate状态的PW数目

Xconnect-group Name

交叉连接组名称

Peer

PW远端PE的IP地址

PW ID/Rmt Site

如果是静态PW或LDP PW，则为PW标识符PW ID；如果是BGP PW，则为远端Site标识符Rmt Site

In/Out Label

PW的入标签和出标签

Proto

建立PW使用的信令协议，取值包括LDP、Static和BGP

Flag

PW属性标记，取值包括：

·M：Main，主PW

·B：Backup，备份PW

Link ID

PW在交叉连接内的链路标识符

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

Xconnect-group Name: ldp

 Connection Name: ldp

  Peer: 192.3.3.3        PW ID: 500

    Signaling Protocol  : LDP

    Link ID             : 0          PW State : Up

    In Label            : 1299       Out Label: 1299

    MTU                 : 1500

    PW Attributes       : Main

    VCCV CC             : -

    VCCV BFD            : -

    Tunnel Group ID     : 0x800000160000000

    Tunnel NHLFE IDs    : 1026

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

Xconnect-group Name: vpnb

 Connection of auto-discovery: Site 1

  Peer: 192.3.3.3        Remote Site: 2

    Signaling Protocol  : BGP

    Link ID             : 1          PW State : Up

    In Label            : 1036       Out Label: 1163

    MTU                 : 1500

    PW Attributes       : Main

    VCCV CC             : -

    VCCV BFD            : -

    Tunnel Group ID     : 0x800000160000000

    Tunnel NHLFE IDs    : 1026

表1-17 display l2vpn pw verbose命令显示信息描述表

字段

描述

Xconnect-group Name

PW所属的交叉连接组名称

Connection Name

PW所属的交叉连接名称，采用LDP或静态方式建立PW时，显示此信息

Peer

PW远端PE的IP地址

PW ID

PW标识符

Signaling Protocol

建立PW使用的信令协议，取值包括LDP、Static和BGP

Link ID

PW在交叉连接内的链路标识符

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

回切等待时间，单位为秒。如果配置不回切，则显示为Infinite

只会在主备PW同时存在的情况下显示，并且只在主PW上显示

Remaining Time

回切等待的剩余时间，单位为秒。回切等待定时器启动时，才会显示该字段

MTU

PW协商后的最大传输单元

PW Attributes

PW的属性，取值包括：

·Main：主PW

·Backup：备份PW

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

Connection of auto-discovery

通过BGP方式建立的PW

Site

本端Site标识符

Remote site

远端Site标识符

Input statistics

入方向的PW转发统计信息，包括入方向接收的字节数（Octets）、接收的报文数（Packets）、接收的错误报文数（Errors）和丢弃的报文数（Discards）

 Output statistics

出方向的PW转发统计信息，包括出方向发送的字节数（Octets）、发送的报文数（Packets）、发送的错误报文数（Errors）和丢弃的报文数（Discards）

【相关命令】

·**statistics enable**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn pw-class**

------------------------------------------------------------------------

**[display l2vpn pw-class**]命令用来显示PW模板的信息。

【命令】

**[display l2vpn pw-class** [ *class-name*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[class-name*]：显示指定PW模板的信息。*class-name*表示PW模板的名称，为1～19个字符的字符串，区分大小写。如果不指定本参数，则显示所有PW模板的信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

【举例】

\# 显示所有PW模板的信息。

\<Sysname\> display l2vpn pw-class

Total number of PW classes: 2

PW Class Name       PW Type              Control Word   VCCV CC        VCCV BFD

pw1                 Ethernet             Enabled        Control-Word   Raw-BFD

pw2                 VLAN                 Disabled       Router-Alert   BFD

表1-18 display l2vpn pw-class命令显示信息描述表

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

·BFD：BFD报文的封装方式为IP/UDP Encapsulation(with IP/UDP Headers)

·Raw-BFD：BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头

\# 显示所有PW模板的详细信息。

\<Sysname\> display l2vpn pw-class verbose

PW Class Name : pw1

  PW Type     : Ethernet

  Control Word: Enabled

  VCCV CC     : Control-Word

  VCCV BFD    : Raw-BFD

  Sequencing  : Both

PW Class Name : pw2

  PW Type     : VLAN

  Control Word: Disabled

  VCCV CC     : Router-Alert

  VCCV BFD    : BFD

  Sequencing  : -

表1-19 display l2vpn pw-class命令显示信息描述表

字段

描述

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

·BFD：BFD报文的封装方式为IP/UDP Encapsulation (with IP/UDP Headers)

·Raw-BFD：BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头

Sequencing

PW的排序处理，取值为Both。取值为"-"时表示未配置PW的排序处理，即不对PW上传输的报文进行排序

【相关命令】

·**pw-class**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn service-instance**

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

Total number of service-instances: 5, 5 up, 0 down

Total number of ACs: 4, 4 up, 0 down

Interface                SrvID Owner                           LinkID State Type

GE1/0/3                  1     vpws1                           1      Up    VPWS

GE1/0/3                  2     vpws2                           1      Up    VPWS

GE1/0/3                  3     vpws3                           1      Up    VPWS

GE1/0/3                  4     vpws4                           1      Up    VPWS

GE1/0/3                  5                                            Up

表1-20 display l2vpn service-instance命令显示信息描述表

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

交叉连接组名称，如果以太网服务实例尚未关联交叉连接，则本字段显示为空

LinkID

以太网服务实例对应AC在交叉连接内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

Type

以太网服务实例所属的L2VPN类型，取值包括VSI和VPWS

\# 显示二层以太网接口GigabitEthernet1/0/1上所有以太网服务实例的详细信息。

\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/1 verbose

Interface: GE1/0/1

  Service Instance: 1

    Encapsulation : s-vid 1 to 16

    Xconnect-group: vpws1

    Connection    : actopw

    Link ID       : 1

    State         : Up

  Service Instance: 2

    Encapsulation : s-vid 1001 to 1002 1015 to 1016

                    only-tagged

    Xconnect-group: vpws2

    Connection    : pwtopw

    Link ID       : 1

    State         : Up

  Service Instance: 3

    Encapsulation : s-vid 2000

                    c-vid 1001 to 1002 1015 to 1016

    Xconnect-group: vpws3

    AD Connection : Site 1, Remote Site 2

    Link ID       : 1

    State         : Up

表1-21 display l2vpn service-instance verbose命令显示信息描述表

字段

描述

Interface

二层以太网接口或二层聚合接口

Service Instance

以太网服务实例ID

Encapsulation

以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则显示为空

Xconnect-group

以太网服务实例所属的交叉连接组的名称

Connection

与以太网服务实例关联的交叉连接的名称

AD Connection

与以太网服务实例关联的自动发现交叉连接，由本端Site标识符（Site）和远端Site标识符（Remote Site）来标识

Link ID

以太网服务实例对应AC在交叉连接内的链路标识符

State

以太网服务实例的状态，取值包括Up和Down

【相关命令】

·**service-instance**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn xconnect-group**

------------------------------------------------------------------------

**[display l2vpn **]**xconnect-group**命令用来显示交叉连接组的信息。

【命令】

**[display** **l2vpn** ]**xconnect-group ** **name** *group-name*****  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name****]*group-name*：显示指定交叉连接组的信息。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有交叉连接组的信息。

**[verbose**]：显示交叉连接组的详细信息。如果不指定本参数，则显示交叉连接组的简要信息。

【举例】

\# 显示所有交叉连接组的简要信息。

\<Sysname\> display l2vpn xconnect-group

Total number of cross-connections: 3, 0 up, 3 down, 0 admin down

Xconnect-group Name             Connection ID   MTU    State

abc                             0               1500   Down

vpn1                            2               1500   Down

vpn2                            1               1500   Down

表1-22 display l2vpn xconnect-group命令显示信息描述表

字段

描述

Total number of cross-connections

所有交叉连接组或指定交叉连接组下交叉连接的总数，以及处于up、down、admin down状态的交叉连接数目

Xconnect-group Name

交叉连接组名称

Connection ID

交叉连接索引

MTU

交叉连接的最大传输单元

State

交叉连接组的状态，取值包括：

·Up：up状态

·Down：down状态

·Admin down：通过**shutdown**命令手工关闭的交叉连接组

\# 显示所有交叉连接组的详细信息。

\<Sysname\> display l2vpn xconnect-group verbose

Xconnect-group Name: ldp

 Description   : ldp-pw

 Connection Name   : ldp

  Connection ID    : 1

  State            : Down

  MTU              : 1500

  Interworking IPv4: Enabled

  LDP PWs:

    Peer            PW ID            Link ID    State

    192.3.3.3       200              1          Down

  ACs:

    AC                               Link ID    State

    Vlan10                           0          Up

Xconnect-group Name: vpnb

 Connection of auto-discovery: Site 1, Remote Site 2

  Connection ID    : 0

  State            : Up

  MTU              : 1500

  BGP PWs:

    Peer            Remote Site      Link ID    State

    192.3.3.3       2                1          Up

  ACs:

    AC                               Link ID    State

    GE1/0/4                          0          Up

表1-23 display l2vpn xconnect-group verbose命令显示信息描述表

字段

描述

Xconnect-group Name

交叉连接组名称

Description

交叉连接组的描述信息，如果不配置，则此行不显示

Connection Name

交叉连接名称

Connection of auto-discovery

自动发现交叉连接

Site

本端Site标识符

Remote site

远端Site标识符

Connection ID

交叉连接索引

State

交叉连接组的状态，取值包括

·Up：up状态

·Down：down状态

·Administratively down：通过**shutdown**命令手工关闭交叉连接组

MTU

交叉连接的最大传输单元

Interworking IPv4

是否使能IPv4类型的异构互连功能，取值包括：

·Enabled：表示使能该功能

·Disabled：表示未使能该功能

本字段的支持情况与设备型号有关，请以设备的实际情况为准

LDP PWs

LDP PW相关信息

Static PWs

静态PW相关信息

BGP PWs

BGP PW相关信息

Peer

PW远端PE的IP地址

PW ID

PW标识符

Link ID

PW在交叉连接内的链路标识符

State

PW的状态，取值包括Up、Down、Blocked和Defect

ACs

AC相关信息

AC

接入电路，取值有如下两种：

·三层接口名称：如GE1/0/4。在交叉连接视图下关联三层接口时，AC取值为此方式

·二层接口名称和以太网服务实例：如GE1/0/3 srv1。在交叉连接视图下关联以太网服务实例时，AC取值为此方式

Link ID

AC在交叉连接组内的链路ID

State

AC的状态，取值包括Up和Down

【相关命令】

·**xconnect-group**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- encapsulation**

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

·删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例与交叉连接的关联。

·内层VLAN标签和外层VLAN标签的介绍请参见"二层技术-以太网交换配置指导"中的"QinQ"。

【举例】

\# 在二层以太网接口GigabitEthernet1/0/1的以太网服务实例1上配置如下报文匹配规则：匹配外层VLAN标签为111，内层VLAN标签为20、30～40的报文。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 service-instance 1

Sysname-GigabitEthernet1/0/1-srv1 encapsulation s-vid 111 c-vid 20 30 to 40

【相关命令】

·**display l2vpn service-instance**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- idle-code**

------------------------------------------------------------------------

**[idle-code**]命令用来配置出口PE检测到特定电路仿真接口的电路仿真分组丢失时，向TDM线路发送的空闲码。

**[undo idle-code**]命令用来恢复缺省情况。

【命令】

**[idle-code** *bit-pattern*]

**[undo idle-code**]

【缺省情况】

出口PE检测到特定电路仿真接口的电路仿真分组丢失时，向TDM线路发送的空闲码为FF。

【视图】

电路仿真类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bit-pattern*]：空闲码。十六进制形式，取值范围为00～FF。

【使用指导】

出口PE以恒定的速率向TDM线路发送TDM帧。当出口PE检测到电路仿真分组丢失时，每个丢失的电路仿真分组的净载荷必须用等量的替代数据来代替。出口PE使用配置的空闲码作为替代数据。

【举例】

\# 配置电路仿真类satop的电路仿真分组丢失时，向TDM线路发送的空闲码为C2。

\<Sysname\> system-view

Sysname cem-class satop

Sysname-cem-satop idle-code c2

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- interface circuit-emulation**

------------------------------------------------------------------------

**[interface circuit-emulation**]命令用来进入电路仿真接口视图。

【命令】

**[interface circuit-emulation**[ { *interface-number*:0 \| *interface-number*:*set-number* }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-number*]：CE1/PRI接口或CT1/PRI接口的编号。详细信息请参见"接口管理"中的"WAN接口"。

*[set-number*]：该接口上时隙捆绑形成的电路仿真组编号，取值范围为0～30。详细信息请参见"接口管理"中的"WAN接口"。

【使用指导】

·**interface circuit-emulation*** interface-number*:0命令用于在SAToP模式时进入电路仿真接口视图。

·**interface circuit-emulation*** interface-number*:*set-number*命令用于在CESoPSN模式时进入电路仿真接口视图。

【举例】

\# 进入电路仿真接口Circuit-Emulation2/3/0:0接口视图。

\<Sysname\> system-view

Sysname interface circuit-emulation2/3/0:0

Sysname-Circuit-Emulation2/3/0:0

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- interworking**

------------------------------------------------------------------------

![说明](MPLS%20L2VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[interworking**]命令用来使能交叉连接的异构互连功能。

**[undo interworking**]命令用来恢复缺省情况。

【命令】

**[interworking ipv4**]

**[undo interworking**]

【缺省情况】

交叉连接不支持异构互连功能。

【视图】

交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：表示IPv4类型的异构互连。

【使用指导】

AC的链路类型多种多样，如ATM、FR、HDLC、Ethernet、PPP等。执行**interworking**命令使能交叉连接的异构互连功能后，交叉连接可以通过PW连接不同链路类型的AC。例如，IPv4类型的异构互连方式中，PE从所连接的AC接收到报文后，从中提取IPv4报文，通过PW发送给远端PE，远端PE根据它连接的AC的链路类型对接收到的IPv4报文进行封装，并把封装后的报文发送到AC链路，从而屏蔽两端AC的链路类型差异，实现不同链路类型AC的互连。

需要注意的是：

·对于IPv4类型的异构互连，如果从AC上接收到的报文不是IPv4报文，则丢弃该报文。

·如果配置了**interworking**命令，则对PW数据封装类型的配置不会生效。

【举例】

\# 使能交叉连接组vpn1内交叉连接ac2pw的异构互连功能。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection ac2pw

Sysname-xcg-vpn1-ac2pw interworking ipv4

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- jitter-buffer**

------------------------------------------------------------------------

**[jitter-buffer**]命令用来配置电路仿真类的Jitter-buffer的大小。

**[undo jitter-buffer**]命令用来恢复缺省情况。

【命令】

**[jitter-buffer** *size-value*]

**[undo jitter-buffer**]

【缺省情况】

与引用此电路仿真类的电路仿真接口的电路类型有关，不区分SAToP或CESoPSN。具体取值如下：

E1---16ms、T1---16ms、E3---5ms、T3---5ms。

【视图】

电路仿真类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size-value*]：Jitter-buffer的大小，取值范围1～500，单位为毫秒。

【使用指导】

由于出口PE必须以恒定速率向TDM电路发送数据，而PSN网络中分组的时延抖动一般较大。因此，需要通过出口PE上的Jitter-buffer缓存TDM电路仿真分组的净载荷，从而平滑PSN网络传送导致的时延抖动。缓存后再以恒定速率向TDM接口发送。

Jitter buffer越小，抗抖动能力越弱；Jitter buffer越大，抗抖动能力越强，但在数据流重建的时候会引入较大的传送延时。过大或过小的Jitter buffer都不利于业务的高质量传输，请根据实际情况合理选择Jitter buffer的大小。

【举例】

\# 配置电路仿真类satop的Jitter-buffer大小为100毫秒。

\<Sysname\> system-view

Sysname cem-class satop

Sysname-cem-satop jitter-buffer 100

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- l2vpn enable**

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

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- l2vpn reflector**

------------------------------------------------------------------------

![说明](MPLS%20L2VPN命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[l2vpn reflector**]命令用来使能L2VPN的报文反射功能。

**[undo l2vpn reflector**]命令用来恢复缺省情况。

【命令】

**[l2vpn reflector interface **[{ *interface-name* \| *interface-type* *inteface-number* } [ **service-instance** *instance-id* ] **ip** *ip-address*  **mac** *mac-address*   **source-port** *source-port*   **destination-port** *destination-port* ]]

**[undo**[ **l2vpn** **reflector** **interface** { *interface-name* \| *interface-type* *inteface-number* } [ **service-instance** *instance-id* ]]]

【缺省情况】

L2VPN的报文反射功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**]**：**指定AC侧接口。

*[interface-name*]：AC侧接口的名称。

*[interface-type* *inteface-number*]：AC侧接口类型和接口编号。

**[service-instance*** instance-id*]：指定以太网服务实例，*instance-id*为以太网服务实例编号，取值范围为1～4096。

**[ip*** ip-address*]：指定待反射报文的目的IP地址，为点分十进制格式，不能为本设备上CE侧接口IP地址。

**[mac*** mac-address*]：指定待反射报文的目的MAC地址，如果不指定本参数，则表示*interface-name*或者*interface-type* *inteface-number*指定的接口的MAC地址。不支持组播MAC地址和全0的MAC地址。

**[source-port*** source-port*]：指定待反射报文的UDP源端口号，取值范围为1～65535，缺省为49184。

**[destination-port*** destination-port*]：指定待反射报文的UDP目的端口号，取值范围为1～65535，缺省为7。

【使用指导】

使能L2VPN的报文反射功能后，可在设备上生成对应的ARP代答表项，用于回应对指定IP地址的ARP请求，并反射对指定PW的检测报文。

需要注意的是：

·每个以太网服务实例或三层接口下只能配置一条报文反射和ARP代答表项，同一接口下的多个以太网服务实例下可配置多条不同的报文反射和ARP代答表项。

·同一以太网服务实例或三层接口下可多次执行本命令，仅最后一次配置生效。

·每台设备最多可配置8条报文反射和ARP代答表项。

·待反射报文的IP地址需本地唯一，即每个以太网服务实例或三层接口下配置的反射报文的IP地址不能相同。

·执行本命令关联以太网服务实例前，必须通过**encapsulation**命令为指定的以太网服务实例配置报文匹配规则。

·开启L2VPN的报文反射功能时，需同时在AC绑定的交叉连接组下开启ARP泛洪抑制功能。

【举例】

\# 使能L2VPN的报文反射功能：AC侧接口为GigabitEthernet1/0/1，反射报文的目的IP地址为1.0.0.1。

\<Sysname\> system-view

Sysname l2vpn reflector interface gigabitethernet 1/0/1 ip 1.0.0.1

【相关命令】

·**display l2vpn forwarding**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- l2vpn switchover**

------------------------------------------------------------------------

!(MPLS%20L2VPN命令.files/image003.png)

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

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置PW的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *mtu*]

**[undo mtu**]

【缺省情况】

PW的MTU值为1500字节。

【视图】

交叉连接视图/交叉连接组自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mtu*]：PW的MTU值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

【使用指导】

在交叉连接视图/交叉连接组自动发现视图下执行本命令后，该视图下建立的所有PW的MTU值均为本命令配置的值。

PW上发送报文的MTU值为包括控制字、PW标签和网络层报文在内的报文的最大长度。

需要注意的是，如果采用LDP信令协议建立PW，则要求PW两端的PE上为PW配置相同的MTU值。否则，PW无法up。

【举例】

\# 在交叉连接组vpn1的交叉连接ac2pw下，配置PW的MTU值为1400字节。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection ac2pw

Sysname-xcg-vpn1-ac2pw mtu 1400

\# 在交叉连接组自动发现视图下，配置PW的MTU值为1400字节。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto mtu 1400

【相关命令】

·**display l2vpn ****xconnect-group**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- payload**

------------------------------------------------------------------------

**[payload**]命令用来配置电路仿真类中每个分组的净载荷大小。

**[undo payload**]命令用来恢复缺省情况。

【命令】

**[payload ***size-value*]

**[undo payload**]

【缺省情况】

SAToP模式下，净载荷的大小与电路仿真接口的电路类型有关，具体取值如下：

E1---256字节、T1---192字节、E3---1024字节、T3---1024字节。

CESoPSN模式下，净载荷的大小与电路仿真接口的时隙数有关。净载荷大小（L字节）、时隙数（N）、分组化延迟（D毫秒）有如下关系：

L = 8 \* N \* D。

缺省载荷如下：

·N=1时，D为8毫秒，相应的净载荷大小为64字节；

·2\<=N\<=4时，D为4毫秒，相应的净载荷大小为32\*N字节；

·N\>=5时，D为1毫秒，相应的净载荷大小为8\*N字节。

【视图】

电路仿真类视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size-value*]：电路仿真类中每个分组的净载荷大小，取值范围为32～1312，单位为字节。

【使用指导】

通过配置分组的净载荷大小，可控制在PW上传输的分组报文的大小。

【举例】

\# 配置电路仿真类satop中每个分组的净载荷大小为512字节。

\<Sysname\> system-view

Sysname cem-class satop

Sysname-cem-satop payload 512

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- peer**

------------------------------------------------------------------------

**[peer**]命令用来配置交叉连接的PW，并进入交叉连接PW视图。如果指定的PW已存在，则直接进入交叉连接PW视图。

**[undo** **peer**]命令用来删除指定的PW。

【命令】

**[peer** *ip-address* **pw-id** *pw-id* [ **in-label** *label-value* **out-label** *label-value*  [ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* ] \*]]

**[undo** **peer** *ip-address* **pw-id** *pw-id*]

【缺省情况】

未配置交叉连接的PW。

【视图】

交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：指定PW远端PE的LSR ID。

**[pw-id ***pw-id*]：指定PW的PW ID。*pw-id*为PW ID，取值范围为1～4294967295。

**[in-label** *l*]*abel-value*：指定PW的入标签。*label-value*为入标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[out-label** *l*]*abel-value*：指定PW的出标签。*label-value*为出标签值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[pw-class** *class-name*]：指定PW引用的PW模板。*class-name*表示PW模板名，为1～19个字符的字符串，区分大小写。PW模板中可以配置PW的数据封装类型、是否使用控制字等。如果不指定本参数，则PW数据封装类型由接口的链路类型决定，对于不强制要求使用控制字的PW数据封装类型，不支持控制字功能。

**[tunnel-policy** *tunnel-policy-name*]：指定PW的隧道选择策略。*tunnel-policy-name*表示隧道策略名，为1～19个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。

【使用指导】

创建静态PW时，必须指定**in-label**和**out-label**参数；静态PW已经存在，进入交叉连接PW视图时，无需指定**in-label**和**out-label**参数。

执行本命令时，如果没有指定**in-label**和**out-label**参数，且尚未创建静态PW，则表示采用LDP信令协议建立PW。

需要注意的是：

·PW ID是一对PE之间PW的标识，本端和远端PE上为同一PW指定的PW ID必须相同。

·在本端PE上，远端PE的LSR ID和PW ID唯一标识一条PW。配置PW时指定的远端PE的LSR ID和PW ID，不能与已经存在的VPLS PW、交叉连接PW的LSR ID和PW ID同时相同。

·PW冗余保护功能和多段PW功能互斥。即，如果在交叉连接视图下通过重复执行**peer**命令配置了两条PW，则不能在交叉连接PW视图下执行**backup-peer**命令配置备份PW；反之亦然。

·如果为静态PW指定的入标签与已经存在的静态LSP/静态CRLSP的入标签相同，则会导致标签冲突，静态PW不可用。即使修改静态LSP/静态CRLSP的入标签，静态PW仍不可用，需要手工删除该静态PW并重新配置。

【举例】

\# 为交叉连接组vpn1内的交叉连接pw2pw配置一条LDP PW：远端PE的地址为4.4.4.4，PW ID为200，并进入交叉连接PW视图。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection pw2pw

Sysname-xcg-vpn1-pw2pw peer 4.4.4.4 pw-id 200

Sysname-xcg-vpn1-pw2pw-4.4.4.4-200

\# 为交叉连接组vpn1内的交叉连接pw2pw配置一条静态PW：远端PE的地址为5.5.5.5，PW ID为200，入标签为100，出标签为200，并进入交叉连接PW视图。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection pw2pw

Sysname-xcg-vpn1-pw2pw peer 5.5.5.5 pw-id 200 in-label 100 out-label 200

Sysname-xcg-vpn1-pw2pw-5.5.5.5-200

【相关命令】

·**display l2vpn ldp**

·**display l2vpn pw**

·**pw-class**

·**tunnel-policy**（MPLS命令参考/隧道策略）

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- peer signaling**

------------------------------------------------------------------------

**[peer signaling**]命令用来使能本地路由器与指定对等体/对等体组交换MPLS L2VPN标签块信息的能力。

**[undo peer signaling**]命令用来禁止本地路由器与指定对等体/对等体组交换MPLS L2VPN标签块信息。

【命令】

**[peer**[ { *group-name* \| *ip-address* [ *mask-length* ] } **signaling**  **non-standard** ]]

**[undo peer**[ { *group-name* \| *ip-address* [ *mask-length* ] } **signaling**]]

【缺省情况】

本地路由器具有与BGP L2VPN对等体/对等体组交换标签块信息的能力，并且采用RFC 4761中定义的MP_REACH_NLRI格式交换标签块信息。

【视图】

BGP L2VPN地址族视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：对等体组的名称，为1～47个字符的字符串，区分大小写。指定的对等体组必须已经创建。

*[ip-address*]：对等体的IP地址。指定的对等体必须已经创建。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

**[non-standard**]：指定采用draft-kompella-ppvpn-l2vpn-03草案中定义的MP_REACH_NLRI格式交换标签块信息。如果不指定本参数，则采用RFC 4761中定义的MP_REACH_NLRI格式交换标签块信息。请根据对等体支持的MP_REACH_NLRI格式类型，选择是否指定本参数。

【使用指导】

建立BGP PW时，PE设备需要通过MP-BGP协议来交换标签块信息。

在BGP L2VPN地址族视图下执行**peer enable**命令后，本地路由器即具有与指定对等体/对等体组采用RFC 4761中定义的MP_REACH_NLRI格式交换标签块信息的能力。如需禁止该能力或该对等体不支持交换标签块信息，则执行**undo peer signaling**命令。

【举例】

\# 在BGP L2VPN地址族视图下，使能本地路由器与对等体3.3.3.9交换MPLS L2VPN标签块信息的能力，并指定采用draft-kompella-ppvpn-l2vpn-03草案中定义的MP_REACH_NLRI格式交换标签块信息。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn peer 3.3.3.9 signaling non-standard

【相关命令】

·**display bgp l2vpn ****signaling**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- policy vpn-target**

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

在跨域VPN-OptionB组网中，ASBR-PE需要保存所有BGP L2VPN信息（即标签块信息），以通告给远端ASBR-PE。这种情况下，ASBR-PE上需执行**undo policy vpn-target**命令接收所有的BGP L2VPN信息，不对它们进行VPN-Target过滤。

跨域VPN-OptionB的详细介绍，请参见"MPLS配置指导"中的"MPLS L3VPN"。

【举例】

\# 在BGP L2VPN地址族视图下，取消对BGP L2VPN信息的VPN-Target过滤功能。

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp address-family l2vpn

Sysname-bgp-l2vpn undo policy vpn-target

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ppp ipcp ignore local-ip**

------------------------------------------------------------------------

**[ppp ipcp ignore local-ip**]命令用来配置PPP支持IPCP无地址协商。

**[undo** **ppp ipcp ignore local-ip**]命令用来恢复缺省情况。

【命令】

**[ppp ipcp ignore local-ip**]

**[undo ppp ipcp ignore local-ip**]

【缺省情况】

PPP不支持IPCP无地址协商，本端接口必须配置IP地址才会和对端进行IPCP协商。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

MPLS L2VPN连接异构网络时，链路层协商报文不会在网络中传递，CE之间无法直接建立二层连接。因此，PE需要与接入的CE建立二层连接，例如，PPP链路中PE需要与CE进行PPP协商，以建立PPP连接，如果PE连接CE的接口没有配置IP地址，通过本配置，可以确保PE与CE进行无IP地址的IPCP协商，保证IPCP协商通过。

需要注意的是，在PPP链路中，如果PE连接CE的接口配置了IP地址，则无需配置IPCP无地址协商或IPCP代理IP地址。如果PE连接CE的接口没有配置IP地址，则在同一接口下，IPCP无地址协商配置的优先级高于IPCP代理IP地址配置。即，如果在同一接口下同时配置了IPCP无地址协商和IPCP代理IP地址，则采用IPCP无地址协商方式进行IPCP协商。

【举例】

\# 配置PPP支持IPCP无地址协商。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol ppp

Sysname-Serial2/1/0 ppp ipcp ignore local-ip

【相关命令】

·**ppp ipcp proxy**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ppp ipcp proxy**

------------------------------------------------------------------------

**[ppp ipcp proxy**]命令用来指定IPCP代理IP地址。

**[undo** **ppp ipcp proxy**]命令用来恢复缺省情况。

【命令】

**[ppp ipcp proxy ***ip-address*]

**[undo ppp ipcp proxy**]

【缺省情况】

未指定IPCP代理IP地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：IPCP代理IP地址。

【使用指导】

MPLS L2VPN连接异构网络时，链路层协商报文不会在网络中传递，CE之间无法直接建立二层连接。因此，PE需要与接入的CE建立二层连接，例如，PPP链路中PE需要与CE进行PPP协商，以建立PPP连接，如果PE连接CE的接口没有配置IP地址，通过本配置将IPCP代理IP地址配置为远端CE的IP地址，可以确保PE使用这个IP地址与本端CE进行IPCP协商，保证IPCP协商通过。

需要注意的是，在PPP链路中，如果PE连接CE的接口配置了IP地址，则无需配置IPCP无地址协商或IPCP代理IP地址。如果PE连接CE的接口没有配置IP地址，则在同一接口下，IPCP无地址协商配置的优先级高于IPCP代理IP地址配置。即，如果在同一接口下同时配置了IPCP无地址协商和IPCP代理IP地址，则采用IPCP无地址协商方式进行IPCP协商。

【举例】

\# 指定IPCP代理IP地址为1.1.1.1。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol ppp

Sysname-Serial2/1/0 ppp ipcp proxy 1.1.1.1

【相关命令】

·**ppp ipcp ignore local-ip**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- protection dual-receive**

------------------------------------------------------------------------

![说明](MPLS%20L2VPN命令.files/image004.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[protection dual-receive**]命令用来配置PW冗余保护的双收功能，即主PW和备份PW都能接收报文，主备PW工作在单发双收模式。

**[undo protection dual-receive **]命令用来恢复缺省情况。

【命令】

**[protection dual-receive**]

**[undo protection dual-receive**]

【缺省情况】

缺省情况下，未配置PW冗余保护的双收功能，即配置PW冗余保护时，仅主PW能发送和接收报文，备份PW不能发送和接收报文。

【视图】

交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 为交叉连接组vpn1内的交叉连接ac2pw配置PW冗余保护的双收功能。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection ac2pw

Sysname-xcg-vpn1-ac2pw protection dual-receive

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- pw-class (system view)**

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

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- pw-class (cross-connect auto-discovery view)**

------------------------------------------------------------------------

**[pw-class**]命令用来指定引用的PW模板。

**[undo** **pw-class**]命令用来取消引用PW模板。

【命令】

**[pw-class ***class-name*]

**[undo** **pw-class**]

【缺省情况】

不引用任何PW模板。

【视图】

交叉连接组自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[class-name*]：PW模板名，为1～19个字符的字符串，区分大小写。

【使用指导】

在交叉连接组自动发现视图下执行本命令指定引用的PW模板后，该PW模板将应用于该视图下建立的所有PW。

【举例】

\# 在交叉连接组自动发现视图下，指定引用的PW模板为pw100。

\<Sysname\> system-view

Sysname pw-class pw100

Sysname-pw-pw100 quit

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto pw-class pw100

【相关命令】

·**control-word enable**

·**display l2vpn pw-class**

·**pw-class**

·**pw-type**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- pw-type**

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

·Ethernet数据封装类型下，PW上传输的帧不能携带P-Tag。对于CE侧的报文，如果PE从CE收到带有P-Tag的报文，则将其去除后再添加PW标签和公网隧道标签转发；如果从CE收到不带P-Tag的报文，则直接添加PW标签和公网隧道标签后转发。对于PE发送给CE的报文，如果**ac interface**命令配置的接入模式为VLAN，则添加P-Tag后转发给CE；如果配置的接入模式为Ethernet，则不添加P-Tag，直接转发给CE；无论**ac interface**命令配置的接入模式为VLAN还是Ethernet，均不允许重写或去除已经存在的任何Tag。

·VLAN数据封装类型下，PW上传输的帧必须携带P-Tag。对于CE侧的报文，PE从CE收到带有P-Tag的报文后，如果远端PE不要求Ingress改写P-Tag，则保留P-Tag，如果远端PE要求Ingress改写P-Tag，则将P-Tag改写为远端PE期望的VLAN Tag（Tag可能是值为0的空Tag），再添加PW标签和公网隧道标签后转发；从CE收到不带P-Tag的报文后，如果远端PE不要求Ingress改写P-Tag，则添加值为0的空P-Tag，如果远端PE要求Ingress改写P-Tag，则添加一个远端PE期望的VLAN Tag（Tag可能是值为0的空Tag）后，再添加PW标签和公网隧道标签后转发。对于PE发送给CE的报文，如果**ac interface**命令配置的接入模式为VLAN，转发给CE时重写或保留P-Tag；如果配置的接入模式为Ethernet，则去除P-Tag后转发给CE。

需要注意的是，本命令只在AC链路为以太网链路时有效。

【举例】

\# 配置PW数据封装类型为Ethernet。

\<Sysname\> system-view

Sysname pw-class pw100

Sysname-pw-pw100 pw-type ethernet

【相关命令】

·**ac interface**

·**display l2vpn pw-class**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除接口的统计信息。

【命令】

**[reset counters interface** [ **circuit-emulation** [ *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[circuit-emulation**]：清除电路仿真接口的统计信息。

*[interface-number*]：电路仿真接口的编号。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**circuit-emulation**和*interface-number*，则清除所有接口的统计信息；

·如果指定**circuit-emulation**而不指定*interface-number*，则清除所有电路仿真接口的统计信息；

·如果同时指定**circuit-emulation**和*interface-number*，则清除指定电路仿真接口的统计信息。

【举例】

\# 清除接口Circuit-Emulation2/3/0:0的统计信息。

\<Sysname\> reset counters interface circuit-emulation 2/3/0:0

【相关命令】

·**display interface ****circuit-emulation**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- reset l2vpn statistics pw**

------------------------------------------------------------------------

![说明](MPLS%20L2VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset l2vpn statistics pw**]命令用来清除指定PW的报文统计信息。

【命令】

**[reset l2vpn statistics pw ** **xconnect-group** ]*group-name***** **connection** *connection-name *

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[xconnect-group **]*group-name*：清除指定交叉连接组内的PW报文统计信息。*group-name*表示交叉连接组的名称，为1～31个字符的字符串，区分大小写。如果不指定该参数，则清除所有PW的统计信息。

**[connection **]*connection-name*：清除指定PW的统计信息。*connection-name*为交叉连接组内交叉连接的名字，为1～20个字符的字符串，区分大小写。如果不指定该参数，则清除指定交叉连接组内的所有PW统计信息。

【使用指导】

当PW存在备PW时，会同时清除主PW和备PW的报文统计信息。

【举例】

\# 清除本设备上所有PW报文统计信息。

\<Sysname\> reset l2vpn statistics pw

【相关命令】

·**statistics enable**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- revertive**

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

交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[wtr ***wtr-time*]：开启回切功能，并指定回切等待时间（wait-to-restore time），即主PW恢复后，等待*wtr-time*时间后，才将流量从备份PW回切到主PW。*wtr-time*取值范围为0～3600，单位为秒。

**[never**]：指定不回切。

【举例】

\# 为交叉连接组vpn1内的交叉连接ac2pw指定回切等待时间为120秒。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1 connection ac2pw

Sysname-xcg-vpn1-ac2pw revertive wtr 120

【相关命令】

·**display l2vpn pw**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- route-distinguisher**

------------------------------------------------------------------------

**[route-distinguisher**]命令用来为当前交叉连接组的BGP方式配置RD（Route Distinguisher，路由标识符）。

**[undo route-distinguisher**]命令用来删除已配置的RD值。

【命令】

**[route-distinguisher** *route-distinguisher*]

**[undo route-distinguisher**]

【缺省情况】

没有为交叉连接组的BGP方式指定RD。

【视图】

交叉连接组自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[route-distinguisher*]：路由标识符，为3～21个字符的字符串。路由标识符有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

【使用指导】

在MPLS L2VPN中，RD用来区分不同VPN内编号相同的站点。PE在通过BGP发布其连接的站点信息时，在Site ID前增加RD，通过RD和Site ID来唯一标识网络中的一个站点。

需要注意的是：

·不能为不同交叉连接组的BGP方式配置相同的RD。

·不能通过重复执行**route-distinguisher**命令修改RD值。必须先通过**undo route-distinguisher**命令删除RD值，再通过**route-distinguisher**命令配置新的RD值。

【举例】

\# 配置交叉连接组bbb的BGP方式的RD为22:2。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto route-distinguisher 22:2

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- rr-filter**

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

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- rtp-header enable**

------------------------------------------------------------------------

**[rtp-header enable**]命令用来配置电路仿真类中的报文携带RTP头。

**[undo rtp-header enable**]命令用来恢复缺省情况。

【命令】

**[rtp-header enable**]

**[undo rtp-header enable**]

【缺省情况】

电路仿真类的报文不携带RTP头。

【视图】

电路仿真类视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通常情况下，电路仿真类中的报文不携带RTP头。当时钟恢复方式为差分恢复方式时，出口PE需根据分组的RTP头中的差分时间戳信息进行时钟恢复，必须通过本命令配置电路仿真类中的报文携带RTP头。

【举例】

\# 配置电路仿真类satop中的分组携带RTP头。

\<Sysname\> system-view

Sysname cem-class satop

Sysname-cem-satop rtp-header enable

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- sequencing both**

------------------------------------------------------------------------

![说明](MPLS%20L2VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[sequencing both**]命令用来使能对PW上传送的报文进行排序处理。

**[undo sequencing both**]命令用来恢复缺省情况。

【命令】

**[sequencing both**]

**[undo sequencing both**]

【缺省情况】

PW上传送的报文不进行排序处理。

【视图】

PW模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[both**]：PW收发两个方向都要进行排序处理。

【使用指导】

在分组交换中，当转发负载比较重或者网络中有多条传送路径进行负载分担时，报文的传送可能会发生乱序，此时需要对传送的分组进行排序处理，即在发送端为每一个在PW上传送的分组添加一个序列号，接收端根据序列号进行重新排序。

本命令的配置不与对端协商，如果本地开启排序处理，则PW上传送的分组携带序列号，且对从PW上收到的分组进行排序处理。如果本端未开启排序处理，当收到的分组携带序列号时，则忽略该序列号，不对分组进行排序处理。

【举例】

\# 配置对引用PW模板aaa的PW上传送的报文进行排序处理。

\<Sysname\> system-view

Sysname pw-class aaa

Sysname-pwc-aaa sequencing both

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- service-instance**

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

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- shutdown (交叉连接组视图)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭当前的交叉连接组。

**[undo shutdown**]命令用来恢复缺省情况。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

交叉连接组处于开启状态。

【视图】

交叉连接组视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭交叉连接组后，该交叉连接组下所有交叉连接将不能提供L2VPN服务。

关闭交叉连接组功能通常用于暂时禁用L2VPN服务，但还需要再次启用该L2VPN服务的场景。关闭交叉连接组后，该交叉连接组所有已存在的配置保持不变。在关闭状态下还可以对交叉连接组进行配置。交叉连接组再次被开启后，基于最新的配置提供L2VPN服务。

【举例】

\# 关闭名为vpn2的交叉连接组。

\<Sysname\> system-view

Sysname xconnect-group vpn2

Sysname-xcg-vpn2 shutdown

【相关命令】

·**display l2vpn xconnect-group**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- shutdown (电路仿真接口视图)**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭电路仿真接口。

**[undo** **shutdown**]命令用来打开电路仿真接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

电路仿真接口处于打开状态。

【视图】

电路仿真接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 关闭电路仿真接口Circuit-Emulation2/3/0:0。

\<Sysname\> system-view

Sysname interface circuit-emulation 2/3/0:0

Sysname-Circuit-Emulation2/3/0:0 shutdown

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- site**

------------------------------------------------------------------------

**[site**]命令用来创建本地站点，并进入站点视图。

**[undo site**]命令用来删除指定的本地站点。

【命令】

**[site ***site-id***** **range** *range-value* ]  **default-offset** *defalut-offset*

**[undo site** *site-id*]

【缺省情况】

设备上不存在任何本地站点。

【视图】

交叉连接组自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[site-id*]：本地站点的ID。取值范围为0～250。

**[range ***range-value*]：指定VPN内最多包含的站点数目。*range-value*取值范围为2～*site-id*的最大值＋1，缺省值为10。

**[default-offset ***defalut-offset*]：指定VPN中站点的起始编号。*defalut-offset*为起始编号，取值为0或1，缺省值为0。取值为0时，表示VPN内的站点从0开始编号；取值为1时，表示VPN内的站点从1开始编号。

【使用指导】

**[range ***range-value*]和**default-offset ***default-offset*参数决定了PE为当前站点分配的标签块：

·第一次执行**site**命令时指定*range-value*为*range1*，则分配第一个标签块，其LR为*range1*，LO为*default-offset*。

·再次执行**site**命令时将*range-value*增加为*range2*（大于*range1*），则分配第二个标签块，LR为*range2*－*range1*，LO为*range1*＋*default-offset*。以此类推。

例如，在PE上先后执行如下命令，则PE分配三个标签块，分别为：LB1/0/10、LB2/10/12、LB3/22/14。其中，LB1、LB2、LB3为PE自动选取的标签值。

site 1 range 10 default-offset 0

site 1 range 22

site 1 range 36

需要注意的是：

·在同一个交叉连接组下，可以创建ID不同的多个本地站点。

·允许在*site-id*和*defalut-offset*不改变的情况下，通过重复执行**site**命令来增大此站点的range值，但不允许将range改小。要想将range改小，则需要删除这个站点，并重新创建。建议根据对VPN规模发展的预计，把**range***range-value*设置得比实际需要大一些。这样当以后对VPN进行扩容，增加VPN中的站点数目时，就可以尽量少的修改配置。

·不能通过重复执行**site**命令来修改*defalut-offset*。必须先通过**undo site**命令删除本地站点，再通过**site**命令创建本地站点，并指定新的*defalut-offset*。

【举例】

\# 在名为bbb的交叉连接组下创建本地站点1，指定VPN内最多包含的站点数目为30，站点的起始编号为0，并进入站点视图。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto site 1 range 30 default-offset 0

Sysname-xcg-bbb-auto-1

【相关命令】

·**display l2vpn pw**

·**display l2vpn xconnect-group**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- snmp-agent trap enable l2vpn**

------------------------------------------------------------------------

**[snmp-agent trap enable l2vpn**]命令用来开启L2VPN模块的告警功能。

**[undo snmp-agent trap enable l2vpn**]命令用来关闭L2VPN模块的告警功能。

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

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- statistics enable**

------------------------------------------------------------------------

![说明](MPLS%20L2VPN命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[statistics enable**]命令用来开启指定PW的统计功能。

**[undo statistics enable**]命令用来关闭指定PW的统计功能。

【命令】

**[statistics enable**]

**[undo statistics enable**]

【缺省情况】

通过命令行创建的PW未开启PW报文统计，通过MIB创建的PW开启PW报文统计。

【视图】

交叉连接PW视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

备PW是否开启统计功能与其主PW保持一致，不需要单独开启或关闭备PW的统计功能。

【举例】

\# 开启指定PW的报文统计功能。

\<Sysname\> system-view

Sysname xconnect-group vpws

Sysname-xcg-vpws connection ldp

Sysname-xcg-vpws-ldp peer 5.5.5.5 pw-id 120

Sysname-xcg-vpws-ldp-5.5.5.5-120 statistics enable

【相关命令】

·**reset l2vpn statistics pw**

·**display l2vpn pw**

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- tunnel-policy**

------------------------------------------------------------------------

**[tunnel-policy**]命令用来指定引用的隧道策略。

**[undo tunnel-policy**]命令用来取消引用隧道策略。

【命令】

**[tunnel-policy** *tunnel-policy-name*]

**[undo tunnel-policy**]

【缺省情况】

不引用任何隧道策略。

【视图】

自动发现交叉连接视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[tunnel-policy-name*]：隧道策略名称，为1～19个字符的字符串，区分大小写。

【使用指导】

在自动发现交叉连接视图下执行本命令指定引用的隧道策略后，与该交叉连接关联的PW将引用该隧道策略，即根据指定的隧道策略选择承载PW的公网隧道。

如果没有引用隧道策略或者引用的隧道策略尚未配置，则PW根据缺省选择策略来选择公网隧道。缺省选择策略为按照LSP隧道－\>GRE隧道－\>CR-LSP隧道的优先级顺序选择隧道，负载分担的隧道数目为1。

【举例】

\# 在自动发现交叉连接视图下，指定引用的隧道策略为policy1。

\<Sysname\> system-view

Sysname tunnel-policy policy1

Sysname-tunnel-policy-policy1 quit

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto site 2 range 10 default-offset 0

Sysname-xcg-bbb-auto-2 connection remote-site-id 3

Sysname-xcg-bbb-auto-2-3 tunnel-policy policy1

【相关命令】

·**tunnel-policy**（MPLS命令参考/隧道策略）

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- vpn-target**

------------------------------------------------------------------------

**[vpn-target**]命令用来为当前交叉连接组的BGP方式配置Route Target属性。

**[undo vpn-target**]命令用来删除指定的Route Target属性。

【命令】

**[vpn-target**[ *vpn-target*&\<1-8\> [ **both** \| **export-extcommunity** \| **import-extcommunity** ]]]

**[undo vpn-target**[ { *vpn-target&\<1-8\>* \| **all** } [ **both** \| **export-extcommunity** \| **import-extcommunity** ]]]

【缺省情况】

没有为交叉连接组的BGP方式指定Route Target属性。

【视图】

交叉连接组自动发现视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-target*&\<1-8\>]：Route Target属性值，为3～21个字符的字符串。&\<1-8\>表示前面的参数最多可以输入8次。Route Target有三种格式：

·16位自治系统号:32位用户自定义数，例如：101:3。

·32位IP地址:16位用户自定义数，例如：192.168.122.15:1。

·32位自治系统号：16位用户自定义数字，其中的自治系统号最小值为65536。例如：65536:1。

**[both**]：指定配置的Route Target值同时作为Import Target和Export Target。没有指定**both**、**export-extcommunity**和**import-extcommunity**中的任何一个参数时，缺省值为**both**。

**[export-extcommunity**]：指定配置的Route Target值为Export Target。

**[import-extcommunity**]：指定配置的Route Target值为Import Target。

**[all**]：所有Route Target值。

【使用指导】

Route Target用来控制BGP L2VPN信息（即标签块信息）的发布。本地PE在通过BGP的Update消息将L2VPN信息（如本地Site ID、RD、标签块等）发送给远端PE时，将Update消息中携带的VPN target属性设置为Export target。远端PE接收到BGP L2VPN信息后，将该信息中携带的Export Target属性与本地配置的Import Target进行比较，如果二者中存在相同的值，则接收该信息。

【举例】

\# 为交叉连接组bbb的BGP方式配置Import Target为10:1 100:1 1000:1，Export Target为20:1 200:1 2000:1。

\<Sysname\> system-view

Sysname xconnect-group bbb

Sysname-xcg-bbb auto-discovery bgp

Sysname-xcg-bbb-auto vpn-target 10:1 100:1 1000:1 import-extcommunity

Sysname-xcg-bbb-auto vpn-target 20:1 200:1 2000:1 export-extcommunity

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- xconnect-group**

------------------------------------------------------------------------

**[xconnect-group**]命令用来创建一个L2VPN交叉连接组，并进入交叉连接组视图。如果指定的交叉连接组已经存在，则直接进入交叉连接组视图。

**[undo**]**xconnect-group**命令用来删除指定的交叉连接组。

【命令】

**[xconnect-group **]*group-name*

**[undo**]**xconnect-group ***group-name*

【缺省情况】

设备上不存在任何交叉连接组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：交叉连接组的名称，为1～31个字符的字符串，不能包含字符"-"，区分大小写。

【使用指导】

在同一个交叉连接组下，可以同时使用不同的方式（LDP、BGP、静态方式）建立多条PW。

【举例】

\# 创建名为vpn1的交叉连接组，并进入交叉连接组视图。

\<Sysname\> system-view

Sysname xconnect-group vpn1

Sysname-xcg-vpn1

【相关命令】

·**display l2vpn ****xconnect-group**

