::: {#480682551 .myid}
[]{#_Toc404791504}[]{#struct_0_x4077_x5759_654244109}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ac interface**

------------------------------------------------------------------------

[**[ac interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_1396808190}[命令用来指定交叉连接关联的接口或以太网服务实例。]{style="font-family:宋体"}

[**[undo ac interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_1451012820}[命令用来取消接口或以太网服务实例与交叉连接的关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2001781795}

[**[ac interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ \[ **service-instance** *instance-id* \] \[ **access-mode** { **ethernet** \| **vlan** } \]]{lang="EN-US"}]{#struct_0_x4077_x5759_1951504092}

[**[undo ac interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ \[ **service-instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_x4077_x5759_x1062186485}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1552086159}

[[交叉连接未关联接口或以太网服务实例。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1132067746}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1405110450}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_867953311}[/]{lang="PT-BR"}[自动发现交叉连接]{style="font-family:宋体"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2062336742}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_18612806}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1377483759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x584297258}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_1241358869}[：指定与交叉连接关联的接口信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_x4077_x5759_x1652037425}[：指定以太网服务实例。]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为以太网服务实例编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[access-mode]{lang="EN-US"}**]{#struct_0_x4077_x5759_1132133282}[：指定接入模式。当关联交叉连接的]{style="font-family:宋体"}[AC]{lang="EN-US"}[为以太网服务实例时，可以指定本参数，接入模式缺省为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[；当]{style="font-family:宋体"}[AC]{lang="EN-US"}[为三层以太网接口时，接入模式始终为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[，不可以指定本参数；当]{style="font-family:宋体"}[AC]{lang="EN-US"}[为三层以太网子接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口时，接入模式始终为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，不可以指定本参数。]{style="font-family:宋体"}

[**[ethernet]{lang="EN-US"}**]{#struct_0_x4077_x5759_x651720305}[：指定接入模式为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1402670421}[：指定接入模式为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_150810317}

[[在交叉连接视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4077_x5759_x32657612}[自动发现交叉连接]{style="font-family:宋体"}[视图下执行本命令后，从关联接口接收到的所有报文或符合指定以太网服务实例报文匹配规则的报文，将通过与该交叉连接关联的]{style="font-family:宋体"}[PW]{lang="EN-US"}[或另一条]{style="font-family:宋体"}[AC]{lang="EN-US"}[转发。]{style="font-family:宋体"}

[[接入模式是]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_797906945}[对从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到的以太网帧携带的外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的理解方式，以及]{style="font-family:宋体"}[PE]{lang="EN-US"}[向]{style="font-family:宋体"}[CE]{lang="EN-US"}[发送以太网帧的方式。接入模式分为两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_x4077_x5759_x1468333551}[接入模式：]{style="font-family:宋体"}[CE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[PE]{lang="EN-US"}[的以太网帧头需要带有一个]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，该]{style="font-family:宋体"}[Tag]{lang="EN-US"}[被称为]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，即服务提供商网络为了区分用户而添加的"服务定界符"。]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送以太网帧给]{style="font-family:宋体"}[CE]{lang="EN-US"}[时，也需要携带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_x4077_x5759_1132198818}[接入模式：]{style="font-family:
宋体"}[CE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[PE]{lang="EN-US"}[的以太网帧头中如果带有]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，则该]{style="font-family:宋体"}[Tag]{lang="EN-US"}[被称为]{style="font-family:宋体"}[U-Tag]{lang="EN-US"}[，即用户网络的内部]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，对于]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备没有意义。]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送以太网帧给]{style="font-family:宋体"}[CE]{lang="EN-US"}[时，不需要携带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，执行本命令关联以太网服务实例前，必须通过]{style="font-family:宋体"}**[encapsulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_x662062635}[命令为指定的以太网服务实例配置报文匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x759232104}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1167435227}[在交叉连接组]{style="font-family:宋体"}[vpna]{lang="EN-US"}[的交叉连接]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中关联接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，使该接口接收到的所有报文都通过与该交叉连接关联的]{style="font-family:宋体"}[PW]{lang="EN-US"}[或另一条]{style="font-family:宋体"}[AC]{lang="EN-US"}[转发。]{style="font-family:宋体"}

[[\[Sysname\] xconnect-group vpna]{lang="EN-US"}]{#struct_0_x4077_x5759_x1167631835}

[\[Sysname-xcg-vpna\] connection aaa]{lang="EN-US"}

[\[Sysname-xcg-vpna-aaa\] ac interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1770583888}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下采用以太网服务实例]{style="font-family:宋体"}[200]{lang="EN-US"}[来匹配外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的报文，在交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的交叉连接]{style="font-family:宋体"}[actopw]{lang="EN-US"}[中关联该以太网服务实例。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x1330795521}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] encapsulation s-vid 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] quit]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection actopw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-actopw\] ac interface gigabitethernet 1/0/1 service-instance 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1957126403}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下采用以太网服务实例]{style="font-family:宋体"}[200]{lang="EN-US"}[来匹配外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的报文，在交叉连接组]{style="font-family:宋体"}[vpwsbgp]{lang="EN-US"}[的]{style="font-family:宋体"}[自动发现交叉连接]{style="font-family:宋体"}[视图下关联该以太网服务实例。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1132264354}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] encapsulation s-vid 200]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv200\] quit]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] quit]{lang="EN-US"}

[\[Sysname\] xconnect-group vpwsbgp]{lang="EN-US"}

[\[Sysname-xcg-vpwsbgp\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-vpwsbgp-auto\] site 1 range 10 default-offset 0]{lang="EN-US"}

[\[Sysname-xcg-vpwsbgp-auto-1\] connection remote-site-id 2]{lang="EN-US"}

[\[Sysname-xcg-vpwsbgp-auto-1-2\] ac interface gigabitethernet 1/0/1 service-instance 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_925516532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[connection]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1352598543}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x907390234}**[interface]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_x4077_x5759_964817156}**[service-instance]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[encapsulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_x116992417}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-type]{lang="EN-US"}**]{#struct_0_x4077_x5759_1131805602}
:::

::: {#-1604945737 .myid}
[]{#_Toc404791505}[]{#struct_0_x4077_x5759_x91566836}[]{#_Toc337567360}[]{#_Toc336272255}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- address-family l2vpn**

------------------------------------------------------------------------

[**[address-family l2vpn]{lang="EN-US"}**]{#struct_0_x4077_x5759_762476473}[命令用来创建]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族，并进入]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[**[undo address-family l2vpn]{lang="EN-US"}**]{#struct_0_x4077_x5759_x315209943}[命令用来删除]{style="font-family:
宋体"}[BGP L2VPN]{lang="EN-US"}[地址族及]{style="font-family:
宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x219938252}

[**[address-family l2vpn]{lang="EN-US"}**]{#struct_0_x4077_x5759_x752781353}

[**[undo address-family l2vpn]{lang="EN-US"}**]{#struct_0_x4077_x5759_1131871138}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_267689849}

[[没有创建]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_676823612}[地址族。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_893448616}

[[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x1801239292}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1678956337}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_2041311106}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_61975373}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1131936674}

[[在]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x496489791}[组网中，要想建立]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，需要在]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下通过]{style="font-family:宋体"}**[peer enable]{lang="EN-US"}**[命令使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体，以便]{style="font-family:宋体"}[PE]{lang="EN-US"}[与该对等体交换]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x87487303}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x631212129}[创建]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族，并进入]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x345322716}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\]]{lang="EN-US"}
:::

::: {#1067234336 .myid}
[]{#_Toc404791506}[]{#struct_0_x4077_x5759_1792747448}[]{#_Toc339307287}[]{#_Toc336510445}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- auto-discovery**

------------------------------------------------------------------------

[**[auto-discovery]{lang="EN-US"}**]{#struct_0_x4077_x5759_1132002210}[命令用来指定交叉连接组采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居、建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入交叉连接组自动发现视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[auto-discovery]{lang="EN-US"}**]{#struct_0_x4077_x5759_2079325776}[命令用来取消交叉连接组采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居并建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1031240271}

[**[auto-discovery bgp]{lang="EN-US"}**]{#struct_0_x4077_x5759_973949279}

[**[undo auto-discovery]{lang="EN-US"}**]{#struct_0_x4077_x5759_477436781}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x976853268}

[[交叉连接组不会采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x188254308}[方式自动发现邻居并建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1122101580}

[[交叉连接组视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1132592034}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1673592237}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1298013594}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x2043020589}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1911177602}

[**[bgp]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1291248302}[：指定交叉连接组采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居并建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_626959267}

[[执行本命令进入交叉连接组自动发现视图后，在该视图下可以配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_1412439729}[信令协议的相关参数，如本端站点、远端站点、]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性等，以便]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[信令协议自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备，并建立连接两端站点的]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_318715104}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1132657570}[指定名为]{style="font-family:宋体"}[bbb]{lang="EN-US"}[的交叉连接组使用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式自动发现邻居、建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入交叉连接组自动发现视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x1798523135}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_891520504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_1963621565}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn xconnect-group]{lang="EN-US"}**]{#struct_0_x4077_x5759_1104070687}
:::

::: {#2036451628 .myid}
[]{#_Toc404791507}[]{#struct_0_x4077_x5759_151528418}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- backup-peer**

------------------------------------------------------------------------

[**[backup-peer]{lang="EN-US"}**]{#struct_0_x4077_x5759_1549326282}[命令]{style="font-family:宋体"}[用来配置交叉连接的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入交叉连接备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。如果指定的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[已存在，则直接进入交叉连接备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **backup-peer**]{lang="EN-US"}]{#struct_0_x4077_x5759_1773439054}[命令用来删除交叉连接的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1132067747}

[**[backup-peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ **pw-id** *pw-id* \[ **in-label** *label-value* **out-label** *label-value* \] \[ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* \] \*]{lang="EN-US"}]{#struct_0_x4077_x5759_x1405044914}

[**[undo]{lang="EN-US"}**[ **backup-peer** *ip-address* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_x4077_x5759_1235077521}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_476034892}

[[未配置交叉连接的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1589143089}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1025556102}

[[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1274759687}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1885543211}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1470628405}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1132133283}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x651785841}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1762874456}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}]{#struct_0_x4077_x5759_x1976570942}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1626811957}*[label-value]{lang="EN-US"}*[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签。]{style="font-family:宋体"}*[label-value]{lang="EN-US"}*[为入标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_1809351966}*[label-value]{lang="EN-US"}*[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的出标签。]{style="font-family:宋体"}*[label-value]{lang="EN-US"}*[为出标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pw-class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x4077_x5759_x241854298}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板中可以配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的数据封装类型、是否使用控制字等。如果不指定本参数，则]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型由接口的链路类型决定，对于不强制要求使用控制字的]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型，不支持控制字功能。]{style="font-family:宋体"}

[**[tunnel-policy]{lang="EN-US"}***[ tunnel-policy-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_1872707437}[：指定备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的隧道选择策略。]{style="font-family:宋体"}*[tunnel-policy-name]{lang="EN-US"}*[表示隧道策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1132198819}

[[备份]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x662128171}[作为主]{style="font-family:宋体"}[PW]{lang="EN-US"}[的备份，可以为主]{style="font-family:宋体"}[PW]{lang="EN-US"}[提供冗余保护。当主]{style="font-family:宋体"}[PW]{lang="EN-US"}[出现故障时，设备将通过主]{style="font-family:宋体"}[PW]{lang="EN-US"}[对应的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发流量。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_433814501}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置备份的静态]{style="font-family:宋体"}]{#struct_0_x4077_x5759_771078319}[PW]{lang="EN-US"}[时，必须指定]{style="font-family:宋体"}**[in-label]{lang="EN-US"}**[和]{style="font-family:宋体"}**[out-label]{lang="EN-US"}**[参数；配置备份的]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[时，无需指定此参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1418359553}[时指定的远端]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[PW ID]{lang="EN-US"}[，不能与已经存在的]{lang="EN-US" style="font-family:宋体"}[VPLS]{lang="EN-US"}[ ]{lang="EN-US"}[PW]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[PW ID]{lang="EN-US"}[同时相同。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_15488690}[冗余保护功能和多段]{style="font-family:宋体"}[PW]{lang="EN-US"}[功能互斥。即，如果在交叉连接视图下通过重复执行]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令配置了两条]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则在交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图下不能执行]{style="font-family:宋体"}**[backup-peer]{lang="EN-US"}**[命令配置备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[；反之亦然。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果为静态]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1063933038}[PW]{lang="EN-US"}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1335603836}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1086492305}[为交叉连接组]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[内的交叉连接]{style="font-family:宋体"}[pw2pw]{lang="EN-US"}[配置主备静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[：主]{style="font-family:宋体"}[PW]{lang="EN-US"}[的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[6.6.6.6]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[；备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[7.7.7.7]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1132264355}

[\[Sysname\] xconnect-group vpn2]{lang="EN-US"}

[\[Sysname-xcg-vpn2\] connection pw2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn2-pw2pw\] peer 6.6.6.6 pw-id 100 in-label 16 out-label 17]{lang="EN-US"}

[\[Sysname-xcg-vpn2-pw2pw-6.6.6.6-100\] backup-peer 7.7.7.7 pw-id 200 in-label 18 out-label 19]{lang="EN-US"}

[\[Sysname-xcg-vpn2-pw2pw-6.6.6.6-100-backup\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_925582068}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ldp]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1776073831}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_646084631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer]{lang="EN-US"}**]{#struct_0_x4077_x5759_x522652942}[]{#_Toc300843382}[]{#_Toc300843383}
:::

::: {#1742433432 .myid}
[]{#_Toc404791508}[]{#struct_0_x4077_x5759_1957345692}[]{#_Toc375819693}[]{#_Toc375553164}[]{#_Toc373826859}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x4077_x5759_153673254}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x4077_x5759_754449899}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_73125436}

[**[bandwidth ]{lang="EN-US"}***[bandwidth-value]{lang="EN-US"}*]{#struct_0_x4077_x5759_634361550}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1586837670}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1174459309}

[[接口的期望带宽为]{style="font-family:宋体"}[10000000kbps]{lang="EN-US"}]{#struct_0_x4077_x5759_1956886939}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1379375000}

[[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x2104149581}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1428931656}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_439326440}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1486481832}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1333370743}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x4077_x5759_x782822086}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[的期望带宽，取值为]{style="font-family:宋体"}[1\~10000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1956821403}

[[接口的期望带宽会对]{style="font-family:宋体"}[CBQ]{lang="EN-US"}]{#struct_0_x4077_x5759_x676810898}[队列带宽有影响。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1244200181}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_955725997}[在]{style="font-family:宋体"}[PW]{lang="EN-US"}[上配置期望带宽为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x1892650214}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection pw2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-pw2pw\] peer 1.1.1.1 pw-id 1]{lang="EN-US"}

[\[Sysname-xcg-vpn1-pw2pw-1.1.1.1-1\] bandwidth 10000]{lang="EN-US"}
:::

::::: {#536926232 .myid}
[]{#_Toc336507497}[]{#_Toc404791509}[]{#struct_0_x4077_x5759_919268051}[]{#_Toc339307289}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ccc**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_629306898}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_x9922984}
:::

[ ]{lang="EN-US"}

[**[ccc]{lang="EN-US"}**]{#struct_0_x4077_x5759_2066457230}[命令用来创建一条]{style="font-family:宋体"}[CCC]{lang="EN-US"}[（]{style="font-family:宋体"}[Circuit Cross Connect]{lang="EN-US"}[，电路交叉连接）远程连接。]{style="font-family:宋体"}

[**[undo ccc]{lang="EN-US"}**]{#struct_0_x4077_x5759_1704884239}[命令用来删除]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程]{style="font-family:宋体"}[连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1131805603}

[**[ccc in-label]{lang="EN-US"}**[ *in-label-value* **out-label** *out-label-value* { **nexthop** *nexthop* \| **out-interface** *interface-type interface-number* } \[ **pw-class** *class-name* \]]{lang="EN-US"}]{#struct_0_x4077_x5759_x91501300}

[**[undo ccc]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1526959128}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x976066420}

[[设备上不存在任何]{style="font-family:宋体"}[CCC]{lang="EN-US"}]{#struct_0_x4077_x5759_954318143}[远程连接。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1375414694}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x200795245}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x330024824}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1131871139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_267624313}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1064738015}

[**[in-label]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1219121516}*[ in-label-value]{lang="EN-US"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接的入标签。]{style="font-family:宋体"}*[in-label-value]{lang="EN-US"}*[为入标签值，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1966769853}*[ out-label-value]{lang="EN-US"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接的出标签。]{style="font-family:宋体"}*[out-label-value]{lang="EN-US"}*[为出标签值，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nexthop ]{lang="EN-US"}***[nexthop]{lang="EN-US"}*]{#struct_0_x4077_x5759_x807957524}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接的]{style="font-family:宋体"}[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[out-interface ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1971302506}*[interface-type interface-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接的]{style="font-family:宋体"}[出接口。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[**[pw-class ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1581064631}*[class-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板中可以配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的数据封装类型、是否使用控制字等。如果不指定本参数，则]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型由接口的链路类型决定，对于不强制要求使用控制字的]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型，不支持控制字功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1131936675}

[[CCC]{lang="EN-US"}]{#struct_0_x4077_x5759_x496555327}[远程连接是通过在]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备上手工指定入标签和出标签而建立的一条静态连接。]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接不需要公网隧道来承载，它通过在]{style="font-family:宋体"}[PE]{lang="EN-US"}[之间的]{style="font-family:宋体"}[P]{lang="EN-US"}[设备上配置两条方向相反的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，来实现报文跨越公网传送。通过]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接转发二层用户报文时，只需为用户报文封装一层标签。]{style="font-family:宋体"}

[[建立]{style="font-family:宋体"}[CCC]{lang="EN-US"}]{#struct_0_x4077_x5759_1859879893}[远程连接时，需要在本地]{style="font-family:宋体"}[PE]{lang="EN-US"}[和远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[上均执行本命令创建]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接。如果两端]{style="font-family:宋体"}[PE]{lang="EN-US"}[之间存在]{style="font-family:宋体"}[P]{lang="EN-US"}[设备，则还需要在]{style="font-family:宋体"}[P]{lang="EN-US"}[设备上配置两条方向相反的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。配置时，需要确保为某一台设备指定的出标签必须与为其下一跳指定的入标签相同。]{style="font-family:宋体"}

[[在交叉连接视图下建立]{style="font-family:宋体"}[CCC]{lang="EN-US"}]{#struct_0_x4077_x5759_2026853453}[远程连接后，还需在该视图下执行]{style="font-family:宋体"}**[ac interface]{lang="EN-US"}**[命令指定关联的接口或以太网服务实例，以]{style="font-family:宋体"}[实现从关联接口接收到的所有报文或符合指定以太网服务实例报文匹配规则的报文，通过建立的]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接转发。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_326468653}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有出接口连接的链路是点到点链路时，才能够使用]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1276708655}**[out-interface]{lang="EN-US"}**[参数指定出接口。如果出接口连接的链路不是点到点链路，如出接口类型为三层以太网接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口或三层聚合接口，则必须使用]{style="font-family:宋体"}**[nexthop]{lang="EN-US"}**[参数指定下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1363120083}[CCC]{lang="EN-US"}[远程连接时，需要保证两端]{style="font-family:宋体"}[PE]{lang="EN-US"}[上]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接的封装类型、控制字功能等配置保持一致，否则可能会导致报文转发失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x697543771}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1398065209}[在交叉连接视图下创建]{style="font-family:宋体"}[一条]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接：下一跳为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[100]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[200]{lang="EN-US"}[，引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板为]{style="font-family:宋体"}[pwc1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1132002211}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] connection ccc1]{lang="EN-US"}

[\[Sysname-xcg-bbb-ccc1\] ccc in-label 100 out-label ]{lang="EN-US"}[200 nexthop 10.1.1.1 pw-class pwc1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_2079391312}[在交叉连接视图下创建一条]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接：出接口为]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[100]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[200]{lang="EN-US"}[，引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板为]{style="font-family:宋体"}[pwc1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1687532359}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] connection ccc1]{lang="EN-US"}

[\[Sysname-xcg-bbb-ccc1\] ccc in-label 100 out-label ]{lang="EN-US"}[200 out-interface serial 2/1/0 pw-class pwc1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x714044013}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ac interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1321753563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1528670618}
:::::

::: {#-1111828934 .myid}
[]{#_Toc404791510}[]{#struct_0_x4077_x5759_x213659547}[]{#_Toc385403429}[]{#_Toc379982544}[]{#_Toc374974302}[]{#_Toc371347445}[]{#_Toc260045256}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem-class**

------------------------------------------------------------------------

[**[cem-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_2004878112}[命令用来创建一个电路仿真类，并进入电路仿真类视图。]{style="font-family:宋体"}

[**[undo cem-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1625113798}[命令用来删除电路仿真类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x370715524}

[**[cem-class ]{lang="EN-US"}***[cem-class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_723083381}

[**[undo cem-class]{lang="EN-US"}**[ *cem-class-name*]{lang="EN-US"}]{#struct_0_x4077_x5759_1536323895}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1988463055}

[[不存在任何电路仿真类。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_962986574}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1378421598}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x213594011}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x321084181}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x782815744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_53316720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2009918998}

[*[cem-class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_1184348911}[：电路仿真类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1515924802}

[[通过本命令创建电路仿真类，并进入电路仿真类视图后，可在该视图下指定电路仿真的一组参数或属性，如]{style="font-family:宋体"}]{#struct_0_x4077_x5759_305962435}[Jitter-buffer]{lang="DA"}[的大小、每个分组净载荷的大小及分组丢失时的填充字符。]{style="font-family:宋体"}

[[当多个]{style="font-family:宋体"}[TDM]{lang="EN-US"}]{#struct_0_x4077_x5759_x1910093208}[电路仿真业务采用相同的一组参数时，通过]{style="font-family:宋体"}[CEM]{lang="EN-US"}[（]{style="font-family:宋体"}[Circuit Emulation]{lang="EN-US"}[，电路仿真）类可以简化配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1110203193}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1004361843}[创建名为]{style="font-family:宋体"}[satop]{lang="EN-US"}[的电路仿真类，并进入电路仿真类视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x214183834}

[\[Sysname\] cem-class satop]{lang="EN-US"}

[\[Sysname-cem-satop\]]{lang="EN-US"}
:::

::: {#944336487 .myid}
[]{#_Toc404791511}[]{#struct_0_x4077_x5759_8221768}[]{#_Toc385403430}[]{#_Toc379982545}[]{#_Toc374974303}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem class-attach**

------------------------------------------------------------------------

[**[cem class-attach]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1330722367}[命令用来在接口上引用电路仿真类。]{style="font-family:宋体"}

[**[undo cem class-attach]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1106369848}[命令用来在接口上取消引用电路仿真类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x3009898}

[**[cem class-attach ]{lang="PT-BR"}**]{#struct_0_x4077_x5759_596651037}*[cem-class-name]{lang="PT-BR"}*

[**[undo cem class-attach]{lang="PT-BR"}**]{#struct_0_x4077_x5759_x1876409552}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x548362011}

[[接口未引用任何电路仿真类。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1353701419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x663744337}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1155271729}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x214118298}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1122662123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1567417134}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1791502986}

[*[cem-class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1572180261}[：电路仿真类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2066104850}

[[在电路仿真接口上引用电路仿真类后，该接口上]{style="font-family:宋体"}[TDM]{lang="EN-US"}]{#struct_0_x4077_x5759_x1676864648}[电路仿真业务采用的参数值为该电路仿真类下配置的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1017957998}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x40732510}[在]{style="font-family:宋体"}[E1]{lang="EN-US"}[控制器通道化出来的]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[上引用电路仿真类]{style="font-family:宋体"}[satop]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x830195704}

[\[]{lang="PT-BR"}[Sysname]{lang="EN-US"}[\] controller e1 2/3/0]{lang="PT-BR"}

[\[Sysname-E1 2/3/0\] cem-set 0 timeslot-list 1-5]{lang="EN-US"}

[\[]{lang="PT-BR"}[Sysname]{lang="EN-US"}[-E1 2/3/0\] quit]{lang="PT-BR"}

[\[Sysname\] interface circuit-emulation 2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\] cem class-attach satop]{lang="EN-US"}
:::

::: {#-161169736 .myid}
[]{#_Toc404791512}[]{#struct_0_x4077_x5759_1427151625}[]{#_Toc385403431}[]{#_Toc379982546}[]{#_Toc374974304}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem clock recover**

------------------------------------------------------------------------

[**[cem clock recover]{lang="EN-US"}**]{#struct_0_x4077_x5759_x214314906}[命令用来配置电路仿真时钟恢复方式。]{style="font-family:宋体"}

[**[undo cem clock recover]{lang="EN-US"}**]{#struct_0_x4077_x5759_x10640216}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1220806706}

[**[cem clock recover]{lang="EN-US"}**[ { **adaptive** \| **differential** }]{lang="EN-US"}]{#struct_0_x4077_x5759_x941274718}

[**[undo cem clock recover]{lang="EN-US"}**]{#struct_0_x4077_x5759_x792773057}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x966604679}

[[未配置电路仿真时钟恢复方式，即不进行时钟恢复。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1125190669}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1282479045}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_74870171}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_443139264}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1736894763}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x214249370}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_726336049}

[**[adaptive]{lang="EN-US"}**]{#struct_0_x4077_x5759_273824238}[：]{style="font-family:宋体"}[Adaptive Clock Recovery]{lang="EN-US"}[，自适应时钟恢复方式。]{style="font-family:宋体"}

[**[differential]{lang="EN-US"}**]{#struct_0_x4077_x5759_51966357}[：]{style="font-family:宋体"}[Differential Clock Recovery]{lang="EN-US"}[，差分时钟恢复方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1800231357}

[[TDM]{lang="EN-US"}]{#struct_0_x4077_x5759_1011382530}[电路采用时分复用技术，有严格的系统时钟同步要求，以传送实时同步业务。而分组交换网是基于统计复用的分组交换技术，接收端与发送端没有严格的时钟同步要求。所以，当采用分组网来传输]{style="font-family:宋体"}[TDM]{lang="EN-US"}[业务时，出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[需进行时钟恢复，时钟恢复方式有以下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACR]{lang="EN-US"}]{#struct_0_x4077_x5759_1554062357}[（]{lang="EN-US" style="font-family:
宋体"}[Adaptive Clock Recovery]{lang="EN-US"}[，自适应时钟恢复）：]{lang="EN-US" style="font-family:宋体"}[出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[根据]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}[的到达速率]{lang="EN-US" style="font-family:宋体"}[和]{style="font-family:宋体"}[Jitter buffer]{lang="EN-US"}[的填充水平进行时钟恢复]{lang="EN-US" style="font-family:宋体"}[。此方式在入口]{style="font-family:
宋体"}[PE]{lang="EN-US"}[和出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[没有相同的时钟源时使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DCR]{lang="EN-US"}]{#struct_0_x4077_x5759_1040595935}[（]{lang="EN-US" style="font-family:
宋体"}[Differential Clock Recovery]{lang="EN-US"}[，差分时钟恢复）]{lang="EN-US" style="font-family:宋体"}[：出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[根据报文的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头中的差分时间戳信息进行时钟恢复。此方式在当出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[和入口]{style="font-family:宋体"}[PE]{lang="EN-US"}[具有相同的时钟源时使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_82961761}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1379257618}[配置电路仿真时钟恢复方式为自适应时钟恢复方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x214445978}

[\[Sysname\] interface circuit-emulation 2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\] cem clock recover adaptive]{lang="EN-US"}
:::

::: {#1740252493 .myid}
[]{#_Toc404791513}[]{#struct_0_x4077_x5759_1549217907}[]{#_Toc385403432}[]{#_Toc379982547}[]{#_Toc374974305}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem clock transmit differential**

------------------------------------------------------------------------

[**[cem clock transmit differential]{lang="EN-US"}**]{#struct_0_x4077_x5759_x995295984}[命令用来配置采用差分方式传送时间戳。]{style="font-family:宋体"}

[**[undo cem clock transmit differential]{lang="EN-US"}**]{#struct_0_x4077_x5759_666272588}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1973451838}

[**[cem clock transmit differential]{lang="EN-US"}**]{#struct_0_x4077_x5759_1280688105}

[**[undo cem clock transmit differential]{lang="EN-US"}**]{#struct_0_x4077_x5759_x463613352}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_542670682}

[[采用绝对方式传送时间戳。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1289763407}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_553124470}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_18821612}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x214380442}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1898828352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1784433968}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1000710854}

[[时间戳的传送方式有两种：绝对模式和差分模式。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x8914442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[绝对模式：入口]{style="font-family:宋体"}]{#struct_0_x4077_x5759_2122193364}[PE]{lang="EN-US"}[采用从用户侧]{style="font-family:宋体"}[TDM]{lang="EN-US"}[电路恢复出的时钟来设置]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头的时间戳。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[差分模式：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1524532425}[PW]{lang="EN-US"}[连接的两台]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备访问同一个高质量同步时钟源，时钟传送的发送方采用]{style="font-family:宋体"}[TDM]{lang="EN-US"}[时钟与高质量同步时钟源的差值来设置]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头的时间戳。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1137646708}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1492134819}[配置采用差分方式传送时间戳。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x209442053}

[\[Sysname\] interface circuit-emulation 2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\] cem clock transmit differential]{lang="EN-US"}
:::

::: {#-1121445169 .myid}
[]{#_Toc404791514}[]{#struct_0_x4077_x5759_325847087}[]{#_Toc385403433}[]{#_Toc379982548}[]{#_Toc374974310}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- cem signaling cas**

------------------------------------------------------------------------

[**[cem signaling cas]{lang="EN-US"}**]{#struct_0_x4077_x5759_x214577050}[命令用来配置电路仿真接口上使用的信令类型为]{style="font-family:宋体"}[CAS]{lang="EN-US"}[（]{style="font-family:宋体"}[Channel-associated signaling]{lang="EN-US"}[，随路信令）。]{style="font-family:宋体"}

[**[undo cem signaling cas]{lang="EN-US"}**]{#struct_0_x4077_x5759_x421116130}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_462231454}

[**[cem signaling cas]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1740813235}

[**[undo cem signaling cas]{lang="EN-US"}**]{#struct_0_x4077_x5759_717573892}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1091073506}

[[未配置信令类型。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1381300956}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1427343470}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1426744270}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x498688941}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x673152621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x214511514}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1523998180}

[[当对]{style="font-family:宋体"}[CAS]{lang="EN-US"}]{#struct_0_x4077_x5759_2019743640}[的]{style="font-family:宋体"}[DS0]{lang="EN-US"}[（数字信号]{style="font-family:宋体"}[0]{lang="EN-US"}[）业务进行]{style="font-family:宋体"}[CESoPSN]{lang="EN-US"}[方式的电路仿真时，需通过本命令配置电路仿真接口上使用的信令类型为]{style="font-family:宋体"}[CAS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1338729800}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_234538598}[配置电路仿真接口上使用的信令类型为随路信令。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_666753257}

[\[Sysname\] interface circuit-emulation 2/3/0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0\] cem signaling cas]{lang="EN-US"}
:::

::: {#538040344 .myid}
[]{#_Toc261964950}[]{#_Toc205607557}[]{#_Toc13287744}[]{#_Toc261964936}[]{#_Toc205607543}[]{#_Toc13287735}[]{#_Toc404791515}[]{#struct_0_x4077_x5759_2124488370}[]{#_Toc385403434}[]{#_Toc384916661}[]{#_Toc261964942}[]{#_Toc205607549}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- crc**

------------------------------------------------------------------------

[**[crc]{lang="EN-US"}**]{#struct_0_x4077_x5759_1793248442}[命令用来配置电路仿真接口的]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验模式。]{style="font-family:宋体"}

[**[undo crc]{lang="EN-US"}**]{#struct_0_x4077_x5759_x168512486}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_191367779}

[**[crc ]{lang="EN-US"}**[{ **16** \| **32** \| **none** }]{lang="EN-US"}]{#struct_0_x4077_x5759_x1429767803}

[**[undo crc]{lang="EN-US"}**]{#struct_0_x4077_x5759_x213659546}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2004812576}

[[使用]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_x4077_x5759_1928473906}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[]{#struct_0_x4077_x5759_28479789}[[【视图】]{style="font-family:黑体"}]{#_Toc384916662}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x363407225}

[]{#struct_0_x4077_x5759_847139203}[[【缺省用户角色】]{style="font-family:黑体"}]{#_Toc384916663}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1554593828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x913979746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2061370171}

[**[16]{lang="EN-US"}**]{#struct_0_x4077_x5759_1332954789}[：电路仿真接口使用]{style="font-family:宋体"}[16]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[32]{lang="EN-US"}**]{#struct_0_x4077_x5759_x213594010}[：电路仿真接口使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x4077_x5759_x321149717}[：电路仿真接口不进行]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x23586231}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_852020300}[配置电路仿真接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[使用]{style="font-family:宋体"}[32]{lang="EN-US"}[位]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x1729451141}

[\[Sysname\] interface circuit-emulation 2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\] crc 32]{lang="EN-US"}
:::

::: {#-1550074726 .myid}
[]{#_Toc404791516}[]{#struct_0_x4077_x5759_x1611704105}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- connection**

------------------------------------------------------------------------

[**[connection]{lang="EN-US"}**]{#struct_0_x4077_x5759_1132592035}[命令用来创建一条交叉连接，并进入交叉连接视图。如果指定的连接已经存在，则直接进入交叉连接视图。]{style="font-family:宋体"}

[**[undo connection]{lang="EN-US"}**]{#struct_0_x4077_x5759_1673526701}[命令用来删除指定的交叉连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2071457797}

[**[connection ]{lang="EN-US"}***[connection-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1276153846}

[**[undo connection ]{lang="EN-US"}***[connection-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_675104711}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_362075981}

[[设备上不存在任何]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_307447026}[交叉连接。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_50801931}

[[交叉连接组视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1215623831}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1132657571}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1798588671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x603715435}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1600075912}

[*[connection-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_606235377}[：交叉连接的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[个字符的字符串，不能包含字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_418747258}

[[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x889423435}[的交叉连接为点到点连接。]{style="font-family:宋体"}

[[在交叉连接视图下，可以：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1191956560}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行一次]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1931428030}**[ac interface]{lang="EN-US"}**[命令和一次]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令将]{style="font-family:宋体"}[AC]{lang="EN-US"}[和]{style="font-family:宋体"}[PW]{lang="EN-US"}[关联，以实现从指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[接收到的报文通过指定的]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发、从指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上接收到的报文转发给指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行两次]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1132067744}**[ac interface]{lang="EN-US"}**[命令将两条]{style="font-family:宋体"}[AC]{lang="EN-US"}[关联，以实现报文在两个]{style="font-family:宋体"}[AC]{lang="EN-US"}[之间进行本地交换。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行两次]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1405241522}**[peer]{lang="EN-US"}**[命令将两条]{style="font-family:宋体"}[PW]{lang="EN-US"}[关联，以实现多段]{style="font-family:宋体"}[PW]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行一次]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x236550865}**[ac interface]{lang="EN-US"}**[命令和一次]{style="font-family:宋体"}**[ccc]{lang="EN-US"}**[命令将]{style="font-family:宋体"}[AC]{lang="EN-US"}[和]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接关联，以实现从指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[接收到的报文通过指定的]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接转发、从指定]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接上接收到的报文将转发给指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x403447178}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1782009656}[为交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[创建名为]{style="font-family:宋体"}[ac2pw]{lang="EN-US"}[的交叉连接，并进入交叉连接视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x666220743}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection ac2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-ac2pw\]]{lang="EN-US"}
:::

::: {#1486495603 .myid}
[]{#_Toc404791517}[]{#struct_0_x4077_x5759_x1822482275}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- connection remote-site-id**

------------------------------------------------------------------------

[**[connection ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1671391816}**[remote-site-id]{lang="PT-BR"}**[命令]{style="font-family:宋体"}[用来创建交叉连接，并进入自动发现交叉连接视图。如果指定的交叉连接已经存在，则直接进入自动发现交叉连接视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **connection** ]{lang="EN-US"}]{#struct_0_x4077_x5759_1132133280}**[remote-site-id]{lang="PT-BR"}**[命令用来删除指定的交叉连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x651589233}

[**[connection]{lang="PT-BR"}**[ ]{lang="PT-BR"}]{#struct_0_x4077_x5759_x1464196441}**[remote-site-id]{lang="PT-BR"}***[ remote-site-id]{lang="PT-BR"}*

[**[undo connection]{lang="PT-BR"}**[ ]{lang="PT-BR"}]{#struct_0_x4077_x5759_x1749117130}**[remote-site-id]{lang="PT-BR"}***[ remote-site-id]{lang="PT-BR"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_596374139}

[[设备上不存在任何交叉连接。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x52578301}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x427204790}

[[站点]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1042207167}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_118439967}

[[network-admin]{lang="PT-BR"}]{#struct_0_x4077_x5759_1132198816}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x4077_x5759_x662193707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x17400175}

[*[remote-site-id]{lang="PT-BR"}*]{#struct_0_x4077_x5759_226266363}[：远端站点的]{style="font-family:宋体"}[ID]{lang="PT-BR"}[。取值范围为]{style="font-family:宋体"}[0]{lang="PT-BR"}[～]{style="font-family:宋体"}[250]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2060475043}

[[执行本命令后]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x957692522}[，]{style="font-family:宋体"}[设备将会在创建交叉连接的同时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[BGP]{lang="PT-BR"}[方式在当前站点和指定的远端站点之间建立一条]{style="font-family:宋体"}[PW]{lang="PT-BR"}[，]{style="font-family:宋体"}[该]{style="font-family:宋体"}[PW]{lang="PT-BR"}[与该交叉连接关联。]{style="font-family:宋体"}

[[自动发现交叉连接视图下，可以执行]{style="font-family:宋体"}**[ac]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_x4077_x5759_2115176851}[命令将交叉连接与指定的]{style="font-family:宋体"}[AC]{lang="EN-US"}[关联，以实现从指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[接收到的报文通过与该交叉连接关联的]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发、从该]{style="font-family:宋体"}[PW]{lang="EN-US"}[上接收到的报文将转发给指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1491001716}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1638996975}[在站点视图下创建交叉连接，同时创建连接本地站点]{style="font-family:宋体"}[1]{lang="EN-US"}[和远端站点]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，并进入自动发现交叉连接视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1132264352}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] site 1 range 10]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto-1\] connection remote-site-id 3]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto-1-3\]]{lang="EN-US"}
:::

::::: {#724706928 .myid}
[]{#_Toc404791518}[]{#struct_0_x4077_x5759_925385460}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- control-word enable**

------------------------------------------------------------------------

[**[control-word enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x849972939}[命令用来使能控制字功能。]{style="font-family:宋体"}

[**[undo control-word enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x406312836}[命令用来恢复缺省情况]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1573586894}

[**[control-word enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1891700724}

[**[undo control-word enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x947959225}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1131805600}

[[未使能控制字功能。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x91435764}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_388318939}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1066844531}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_404662266}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x330021279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1303670033}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_151856037}

[[控制字字段位于]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x4077_x5759_x664140674}[标签栈和二层数据之间，用来携带额外的二层数据帧的控制信息，如序列号等。控制字具有如下功能：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[避免报文乱序：在多路径转发的情况下，报文有可能产生乱序，此时可以通过控制字的序列号字段对报文进行排序重组。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x893837123}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[传送特定二层数据帧的标记：如帧中继的]{lang="EN-US" style="font-family:宋体"}[FECN]{lang="EN-US"}]{#struct_0_x4077_x5759_1131871136}[（]{lang="EN-US" style="font-family:宋体"}[Forward Explicit Congestion Notification]{lang="EN-US"}[，前向显式拥塞通知）比特和]{lang="EN-US" style="font-family:宋体"}[BECN]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Backward Explicit Congestion Notification]{lang="EN-US"}[，后向显示拥塞通知）比特等。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[传送]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x997160039}[TDM]{lang="EN-US"}[电路的]{style="font-family:宋体"}[OAM]{lang="EN-US"}[相关标记：如]{style="font-family:宋体"}[LOS]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Loss of Signal]{lang="EN-US"}[，信号丢失]{style="font-family:宋体"}[）和]{lang="EN-US" style="font-family:宋体"}[AIS]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，告警指示信号]{style="font-family:宋体"}[）等。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指示净载荷长度：如果]{style="font-family:宋体"}]{#struct_0_x4077_x5759_266772345}PW[上传送报文的净载荷长度小于]{style="font-family:宋体"}64[字节，则需要对报文进行填充，以避免报文发送失败。此时，通过控制字的载荷长度字段可以确定原始载荷的长度，以便从填充后的报文中正确获取原始的报文载荷。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_x1400068863}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[上述功能的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_486944096}
:::

[ ]{lang="EN-US"}

[[对于某些]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_473644879}[数据封装类型（如帧中继]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[类型、]{style="font-family:宋体"}[ATM AAL5 SDU VCC]{lang="EN-US"}[类型），]{style="font-family:宋体"}[PW]{lang="EN-US"}[上传递的报文必须携带控制字字段，不能通过配置来控制；对于某些]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型（如]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[），控制字字段是可选的，可以通过配置来决定是否携带控制字。]{style="font-family:宋体"}

[[本命令用来配置对于控制字字段可选的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_176661866}[数据封装类型，本端是否支持携带控制字字段。报文实际是否携带控制字字段，由两端的配置共同决定：如果两端]{style="font-family:宋体"}[PE]{lang="EN-US"}[上都使能了控制字功能，则报文中携带控制字字段；否则，报文中不携带控制字字段。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1131936672}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x496883007}[使能]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板]{style="font-family:宋体"}[pw100]{lang="EN-US"}[的控制字功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x85145384}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] control-word enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_343905468}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x324126155}
:::::

::: {#1948332219 .myid}
[]{#_Toc404791519}[]{#struct_0_x4077_x5759_x214380437}[]{#_Toc385403438}[]{#_Toc384916654}[]{#_Toc329007815}[]{#_Toc309912009}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x4077_x5759_1899024959}[命令用来恢复当前电路仿真接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1083888868}

[**[default]{lang="EN-US"}**]{#struct_0_x4077_x5759_342440250}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x609676008}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1909990695}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x4077_x5759_2715803}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_823301934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_585588453}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1870249926}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x199031125}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x4077_x5759_x214577045}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[]{#struct_0_x4077_x5759_x420788451}[[【举例】]{style="font-family:黑体"}]{#_Toc384916655}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1545361840}[将电路仿真接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x548563807}

[\[Sysname\] interface circuit-emulation 2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\] default]{lang="EN-US"}
:::

::: {#-2141619946 .myid}
[]{#_Toc134072797}[]{#_Toc83790647}[]{#_Toc81376605}[]{#_Toc67196386}[]{#_Toc67145435}[]{#_Toc65385665}[]{#_Toc61239885}[]{#_Toc53707301}[]{#_Toc53518774}[]{#_Toc50837082}[]{#_Toc43895348}[]{#_Toc404791520}[]{#struct_0_x4077_x5759_962384470}[]{#_Toc351118429}[]{#_Toc252883295}[]{#_Toc250560251}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- default-nexthop**

------------------------------------------------------------------------

[**[default-nexthop]{lang="EN-US"}**]{#struct_0_x4077_x5759_x185630717}[命令用来配置缺省下一跳信息。]{style="font-family:宋体"}

[**[undo default-nexthop]{lang="EN-US"}**]{#struct_0_x4077_x5759_962450006}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x723562142}

[**[default-nexthop ]{lang="EN-US"}**[{ **ip** *ip-address* \| **mac** { *mac-address \|* **broadcast** } }]{lang="EN-US"}]{#struct_0_x4077_x5759_x1609241998}

[**[undo default-nexthop]{lang="EN-US"}**]{#struct_0_x4077_x5759_682706487}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_448938990}

[[未指定缺省下一跳信息。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1156657683}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2820966}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_962515542}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1239217145}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_581810064}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1511519230}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x949406529}

[**[ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x935176786}[：指定缺省下一跳的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4077_x5759_x273614638}[：指定缺省下一跳的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mac-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_962581078}[：缺省下一跳的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[broadcast]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1129033113}[：采用广播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为缺省下一跳的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1073063790}

[[MPLS L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x985324854}[连接异构网络，且]{style="font-family:宋体"}[CE]{lang="EN-US"}[接入]{style="font-family:宋体"}[PE]{lang="EN-US"}[的链路类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[时，]{style="font-family:宋体"}[PE]{lang="EN-US"}[上需要设置缺省下一跳信息，以便]{style="font-family:宋体"}[PE]{lang="EN-US"}[正确地为发送给]{style="font-family:宋体"}[CE]{lang="EN-US"}[的报文封装链路层头。]{style="font-family:宋体"}

[[缺省下一跳信息为]{style="font-family:宋体"}[CE]{lang="EN-US"}]{#struct_0_x4077_x5759_119346938}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址或广播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时，]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[CE]{lang="EN-US"}[的报文将以该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址；缺省下一跳信息为]{style="font-family:宋体"}[CE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[ARP]{lang="EN-US"}[将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址解析为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，解析到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址将作为]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[CE]{lang="EN-US"}[的报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1658831170}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4077_x5759_x988250492}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_962122326}[在]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置缺省下一跳的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x491737220}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] default-nexthop ip 1.1.1.1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4077_x5759_x1673815323}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1489968568}[在]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置缺省下一跳的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1571500375}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] default-nexthop ip 1.1.1.1]{lang="EN-US"}
:::

::: {#-817303867 .myid}
[]{#_Toc404791521}[]{#struct_0_x4077_x5759_526587804}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- description (交叉连接组视图)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x4077_x5759_x577135484}[命令用来设置交叉连接组的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x4077_x5759_x166633532}[命令用来删除交叉连接组的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1899003732}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x4077_x5759_1132002208}

[**[undo description]{lang="EN-US"}**]{#struct_0_x4077_x5759_2078801489}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2113778411}

[[未配置交叉连接组的描述信息。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1584292516}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1446136700}

[[交叉连接组视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x601323499}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_616529020}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_77084165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1124074343}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1132592032}

[*[text]{lang="EN-US"}*]{#struct_0_x4077_x5759_1673461165}[：交叉连接组的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x224280603}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x69861194}[配置名为]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[的交叉连接组的描述信息为"]{style="font-family:宋体"}[vpws for vpn2]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1129099727}

[\[Sysname\] xconnect-group vpn2]{lang="EN-US"}

[\[Sysname-xcg-vpn2\] description vpws for vpn2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1488670037}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1167755475}**[xconnect-group]{lang="EN-US"}**
:::

::: {#660347730 .myid}
[]{#_Toc404791522}[]{#struct_0_x4077_x5759_x214183828}[]{#_Toc385403441}[]{#_Toc384916656}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- description (电路仿真接口视图)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x4077_x5759_8483911}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x4077_x5759_x152838880}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x923297811}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x4077_x5759_565677082}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x4077_x5759_x948366159}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x576498352}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x4077_x5759_x1732026965}["，比如：]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_x4077_x5759_2017232074}[[【视图】]{style="font-family:黑体"}]{#_Toc384916657}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1176964903}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x659093940}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x214118292}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1123055339}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1976948240}

[*[text]{lang="EN-US"}*]{#struct_0_x4077_x5759_1020104460}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[]{#struct_0_x4077_x5759_376922455}[[【举例】]{style="font-family:黑体"}]{#_Toc384916658}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x630186640}[配置电路仿真接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[router-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_2009528533}

[\[Sysname\] interface circuit-emulation 2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\] description router-interface]{lang="EN-US"}
:::

::: {#1061336316 .myid}
[]{#_Toc339307293}[]{#_Toc404791523}[]{#struct_0_x4077_x5759_x730357663}[]{#_Toc337567367}[]{#_Toc336272262}[]{#_Toc361661557}[]{#_Toc361661558}[]{#_Toc361661559}[]{#_Toc361661560}[]{#_Toc361661561}[]{#_Toc361661562}[]{#_Toc361661563}[]{#_Toc361661564}[]{#_Toc361661565}[]{#_Toc361661566}[]{#_Toc361661567}[]{#_Toc361661568}[]{#_Toc361661569}[]{#_Toc361661570}[]{#_Toc361661571}[]{#_Toc361661572}[]{#_Toc361661573}[]{#_Toc361661574}[]{#_Toc361661575}[]{#_Toc361661576}[]{#_Toc361661577}[]{#_Toc361661578}[]{#_Toc361661579}[]{#_Toc361661580}[]{#_Toc361661581}[]{#_Toc361661582}[]{#_Toc361661583}[]{#_Toc361661584}[]{#_Toc361661585}[]{#_Toc361661586}[]{#_Toc361661587}[]{#_Toc361661588}[]{#_Toc361661589}[]{#_Toc361661590}[]{#_Toc361661591}[]{#_Toc361661592}[]{#_Toc361661593}[]{#_Toc361661594}[]{#_Toc361661595}[]{#_Toc361661596}[]{#_Toc361661597}[]{#_Toc361661660}[]{#_Toc307388003}[]{#_Toc307232835}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display bgp l2vpn signaling**

------------------------------------------------------------------------

[**[display bgp l2vpn signaling]{lang="EN-US"}**]{#struct_0_x4077_x5759_x918649734}[命令用来显示]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1257767705}

[**[display bgp l2vpn signaling]{lang="EN-US"}**[ \[ **peer** *ip-address* { **advertised** \| **received** } \[ **statistics** \] \| **route-distinguisher** *route-distinguisher* \[ **site-id** *site-id* \[ **label-offset** *label-offset* \[ **advertise-info** \] \] \] \| **statistics** \]]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596750071}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1833152742}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1046258034}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_39053549}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1162221994}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_996096188}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_91613008}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_1748387066}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1596684535}

[**[peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_1787626974}[：]{style="font-family:宋体"}[显示向指定对等体发布或者从指定对等体收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[表示对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[advertised]{lang="EN-US"}**]{#struct_0_x4077_x5759_x987406240}[：显示向指定对等体发布的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[**[received]{lang="EN-US"}**]{#struct_0_x4077_x5759_367275556}[：显示从指定对等体接收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_x4077_x5759_929467006}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块的统计信息。]{style="font-family:宋体"}

[**[route-distinguisher]{lang="EN-US"}***[ route-distinguisher]{lang="EN-US"}*]{#struct_0_x4077_x5759_x594708979}[：显示指定路由标识符的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[route-distinguisher]{lang="EN-US"}*[为路由标识符，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。路由标识符有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x4077_x5759_x488275600}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x4077_x5759_x1555461297}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x4077_x5759_x1347441823}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。]{style="font-family:宋体"}[例如：]{lang="EN-US" style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[site-id]{lang="EN-US"}***[ site-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1596618999}[：显示为指定站点分配的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[site-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[站点编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[label-offset ]{lang="EN-US"}***[label-offset]{lang="EN-US"}*]{#struct_0_x4077_x5759_476170805}[：显示标签块偏移量为指定值的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}*[label-offset]{lang="EN-US"}*[为标签块偏移量]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1605789094}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块的通告信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1820548394}

[[执行本命令时，如果没有指定任何参数，则显示所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_1973409822}[协议]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_929372946}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1902533863}[显示所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn signaling]{lang="EN-US"}]{#struct_0_x4077_x5759_x1597077751}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.135]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total number of label blocks: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 2:2]{lang="EN-US"}

[ Total number of label blocks: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Site ID  LB offset  LB range  LB base    Nexthop]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  1        0          10        1034       0.0.0.0]{lang="EN-US"}

[\* \>i 2        0          10        1162       192.3.3.3]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display bgp l2vpn signaling]{lang="EN-US"}]{#struct_0_x4077_x5759_x1137688828}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x568612164}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x369278375}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1873904701}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_x4077_x5759_506332695}

[[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x727712110}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Status codes]{lang="EN-US"}]{#struct_0_x4077_x5759_x1597012215}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x328777387}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\* - valid]{lang="EN-US"}]{#struct_0_x4077_x5759_x553153304}[：合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> - best]{lang="EN-US"}]{#struct_0_x4077_x5759_x1564765132}[：普通优选路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d - damped]{lang="EN-US"}]{#struct_0_x4077_x5759_x1249709432}[：震荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h - history]{lang="EN-US"}]{#struct_0_x4077_x5759_x850606988}[：历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s - suppressed]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596946679}[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S - Stale]{lang="EN-US"}]{#struct_0_x4077_x5759_1245429349}[：过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i - internal]{lang="EN-US"}]{#struct_0_x4077_x5759_1199267009}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e - external]{lang="EN-US"}]{#struct_0_x4077_x5759_x577450614}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x4077_x5759_x140836225}

[[标签块信息的来源，取值包括：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x897493454}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596881143}[：表示产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[内]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x2115352008}[：表示是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="EN-US"}[，外部网关协议）学到的]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="EN-US"}]{#struct_0_x4077_x5759_1674199272}[：表示来源无法确定]{lang="EN-US" style="font-family:宋体"}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_x4077_x5759_829037433}

[[所有标签块信息的总数]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1143323392}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596291319}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x151404461}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_x4077_x5759_1972838435}

[[路由标识符为指定值的标签块信息的数目]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x649359576}

[[Site ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596225783}

[[站点编号]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2096491848}

[[LB offset]{lang="EN-US"}]{#struct_0_x4077_x5759_138897560}

[[标签块偏移量]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1625768622}

[[LB range]{lang="EN-US"}]{#struct_0_x4077_x5759_x958620208}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596815606}

[[LB base]{lang="EN-US"}]{#struct_0_x4077_x5759_187801413}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2111961228}

[[Nexthop]{lang="EN-US"}]{#struct_0_x4077_x5759_x654569017}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596750070}

[ ]{lang="EN-US"}

[]{#_Toc336272264}[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_895730613}[显示路由标识符为]{style="font-family:宋体"}[2:2]{lang="EN-US"}[、为站点]{style="font-family:宋体"}[2]{lang="EN-US"}[分配的、标签块偏移量为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn signaling route-distinguisher 2:2 site-id 2 label-offset 0]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596684534}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.135]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 2:2]{lang="EN-US"}

[ Total number of label blocks: 1]{lang="EN-US"}

[ Paths:   1 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ From            : 192.3.3.3 (192.168.1.140)]{lang="EN-US"}

[ Original nexthop: 192.3.3.3]{lang="EN-US"}

[ Ext-Community   : \<RT: 2:2\>, \<L2VPN info: MTU 1500, Encap type VLAN\>]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : localpref 100, pref-val 0]{lang="EN-US"}

[ Site ID         : 2]{lang="EN-US"}

[ LB offset       : 0]{lang="EN-US"}

[ LB base         : 1162]{lang="EN-US"}

[ LB range        : 10]{lang="EN-US"}

[ State           : valid, internal, best]{lang="EN-US"}

[ CSV             : 0x01000ABFFF]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display bgp l2vpn signaling]{lang="EN-US"}]{#struct_0_x4077_x5759_x941256381}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x539868132}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1194765054}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1506511248}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1426941987}

[[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x776847733}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Local AS number]{lang="EN-US"}]{#struct_0_x4077_x5759_18631180}

[[本地自治系统号]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596618998}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_x4077_x5759_x1089913136}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2048126446}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_x4077_x5759_1355249747}

[[路由标识符为指定值的标签块信息的总数]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1900172692}

[[Paths]{lang="EN-US"}]{#struct_0_x4077_x5759_1725053582}

[[标签块信息的数目：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1597077750}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_x4077_x5759_1591194527}[：有效可达信息条数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_x4077_x5759_x1492964613}[：最佳可达信息条数]{style="font-family:宋体"}

[[From]{lang="EN-US"}]{#struct_0_x4077_x5759_x967758428}

[[发布该信息的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x645366639}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Original nexthop]{lang="EN-US"}]{#struct_0_x4077_x5759_x1597012214}

[[原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x1894861328}[更新消息中获得的标签块信息，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Ext-Community]{lang="EN-US"}]{#struct_0_x4077_x5759_866355290}

[[扩展团体属性值，包括：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_828593733}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT]{lang="EN-US"}]{#struct_0_x4077_x5759_829353972}[：]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2VPN ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596946678}[i]{lang="EN-US"}[nfo]{lang="EN-US"}[：]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[相关信息，包括]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值、封装类型（]{style="font-family:宋体"}[Encap ]{lang="EN-US"}[t]{lang="EN-US"}[ype]{lang="EN-US"}[）]{style="font-family:宋体"}

[[AS-path]{lang="EN-US"}]{#struct_0_x4077_x5759_x1483454006}

[[AS]{lang="EN-US"}]{#struct_0_x4077_x5759_1774522059}[路径属性，记录了此标签块信息经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免环路的出现]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_x4077_x5759_968170900}

[[标签块信息的起源代码，取值包括：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596881142}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="EN-US"}]{#struct_0_x4077_x5759_x549268067}[：表示可达信息来源于]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="EN-US"}]{#struct_0_x4077_x5759_949204349}[：表示可达信息通过]{style="font-family:宋体"}[EGP]{lang="EN-US"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[incomplete]{lang="EN-US"}]{#struct_0_x4077_x5759_x1355802517}[：表示可达信息的来源无法确定]{lang="EN-US" style="font-family:宋体"}

[[Attribute value]{lang="EN-US"}]{#struct_0_x4077_x5759_x1522241172}

[[标签块信息的属性值，包括：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596291318}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_x4077_x5759_x1717488402}[：与目的网络关联的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_x4077_x5759_976714957}[：本地优先级]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_x4077_x5759_x1185529476}[：首选值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596225782}[：协议优先级]{style="font-family:宋体"}

[[Site ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x530407907}

[[站点编号]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1193182401}

[[LB offset]{lang="EN-US"}]{#struct_0_x4077_x5759_x555585704}

[[标签块偏移量]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596815609}

[[LB base]{lang="EN-US"}]{#struct_0_x4077_x5759_x2090743248}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_x4077_x5759_2024872133}

[[LB range]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596750073}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x670353328}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x120359210}

[[标签块信息的当前状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1650203243}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596684537}[：有效信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_x4077_x5759_624827560}[：内部信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_x4077_x5759_x600455106}[：外部信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596619001}[：本地产生信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_x4077_x5759_966749958}[：最佳信息]{lang="EN-US" style="font-family:宋体"}

[[CSV]{lang="EN-US"}]{#struct_0_x4077_x5759_x982237014}

[[接入链路状态]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2129419752}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1597077753}[显示指定]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp l2vpn signaling route-distinguisher 2:2 site-id 1 label-offset 0 advertise-info]{lang="EN-US"}]{#struct_0_x4077_x5759_1994479054}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.135]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 2:2]{lang="EN-US"}

[ Total number of label blocks: 1]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Site ID         : 1]{lang="EN-US"}

[ LB offset       : 0]{lang="EN-US"}

[ LB base         : 1034]{lang="EN-US"}

[ LB range        : 10]{lang="EN-US"}

[ CSV             : 0x01000ADFFF]{lang="EN-US"}

[ Advertised to peers (1 in total):]{lang="EN-US"}

[    192.3.3.3]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display bgp l2vpn signaling adveritse-info]{lang="EN-US"}]{#struct_0_x4077_x5759_1048395441}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x543156516}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x89332188}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_600551729}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1597012217}

[[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_834022027}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Local AS number]{lang="EN-US"}]{#struct_0_x4077_x5759_x1852416608}

[[本地自治系统号]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1449446801}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_x4077_x5759_x1160607824}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x97630095}

[[Total number of label blocks]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596946681}

[[路由标识符为指定值的标签块信息总数]{style="font-family:宋体"}]{#struct_0_x4077_x5759_889395597}

[[Paths]{lang="EN-US"}]{#struct_0_x4077_x5759_585355571}

[[标签块信息的数目：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x978072212}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_x4077_x5759_x1916212528}[：]{style="font-family:宋体"}[有效可达信息条数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_x4077_x5759_x860990840}[：最佳可达信息条数]{style="font-family:宋体"}

[[Site ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1596881145}

[[站点编号]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1373046234}

[[LB offset]{lang="EN-US"}]{#struct_0_x4077_x5759_x569708374}

[[标签块偏移量]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2015069041}

[[LB base]{lang="EN-US"}]{#struct_0_x4077_x5759_x2017445425}

[[标签块的初始标签值]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596291321}

[[LB range]{lang="EN-US"}]{#struct_0_x4077_x5759_x507569285}

[[标签块大小]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1032779075}

[[CSV]{lang="EN-US"}]{#struct_0_x4077_x5759_53027753}

[[接入链路状态]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1596225785}

[[Advertised to peers (1 in total)]{lang="EN-US"}]{#struct_0_x4077_x5759_x933692434}

[[该信息已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x534262776}

[[ ]{lang="EN-US"}]{#_Toc337567369}

::: {#1088233300 .myid}
[]{#_Toc404791524}[]{#struct_0_x4077_x5759_x617533896}[]{#_Toc385403443}[]{#_Toc383502040}[]{#_Toc261964945}[]{#_Toc205607552}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display interface circuit-emulation**

------------------------------------------------------------------------

[**[display interface circuit-emulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_x442010445}[命令用来显示电路仿真接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1894182810}

[**[display interface]{lang="EN-US"}**[ \[ **circuit-emulation** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x4077_x5759_x2051416725}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x146671014}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2093578710}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_135388394}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1702938172}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_x617730504}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1183132993}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_x1655154732}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2103632817}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_1897410166}[：显示指定电路仿真接口的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1231857625}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1528209986}[：显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x4077_x5759_597143131}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x617664968}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}**[circuit-emulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_x848583348}[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[circuit-emulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_30973080}[参数，不指定]{lang="EN-US" style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[电路仿真接口]{style="font-family:
宋体"}[的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x153574443}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x535945214}[显示电路仿真接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface circuit-emulation 2/3/0:0]{lang="EN-US"}]{#struct_0_x4077_x5759_932223983}

[Circuit-Emulation 2/3/0:0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Circuit-Emulation2/3/0:0 Interface]{lang="EN-US"}

[Bandwidth: 64kbps\
Maximum Transmit Unit: 0\
Internet protocol processing: disabled\
Last clearing of counters: Never]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_633629466}[显示电路仿真接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface circuit-emulation 2/3/0:0 brief]{lang="EN-US"}]{#struct_0_x4077_x5759_x617861576}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Speed or Duplex: (a)/A - auto; H - half; F - full]{lang="EN-US"}

[Type: A - access; T - trunk; H - hybrid]{lang="EN-US"}

[Interface            Link Speed   Duplex Type PVID Description]{lang="EN-US"}

[Cem2/3/0:0           DOWN \--      \--     \--   \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_393502340}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的电路仿真接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface circuit-emulation brief down]{lang="EN-US"}]{#struct_0_x4077_x5759_1287487796}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[Cem2/3/0:0           DOWN Not connected]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display interface circuit-emulation]{lang="EN-US"}]{#struct_0_x4077_x5759_x452471610}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x902231563}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x617796040}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1231766535}

[[Current state]{lang="EN-US"}]{#struct_0_x4077_x5759_x616944072}

[[电路仿真接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x826956438}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4077_x5759_71112838}[（]{lang="EN-US" style="font-family:宋体"}[Administratively]{lang="EN-US"}[）：表示该]{lang="EN-US" style="font-family:宋体"}[电路仿真接口]{style="font-family:宋体"}[已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4077_x5759_x616878536}[：表示该电路仿真接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x4077_x5759_309032955}[：该电路仿真接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x4077_x5759_x617468359}

[[该接口的链路层协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x434735239}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x4077_x5759_x421356622}[：表示数据链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4077_x5759_x617402823}[：表示数据链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x4077_x5759_x2010715800}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x617599431}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x4077_x5759_x996832357}

[[接口的期望带宽]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1671380334}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x4077_x5759_x1712835290}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x996766821}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x4077_x5759_x264040576}

[[网络层协议处理状况]{style="font-family:宋体"}]{#struct_0_x4077_x5759_2094932061}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x4077_x5759_x997356652}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_902172415}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Brief information on interface(s) under bridge mode:]{lang="EN-US"}]{#struct_0_x4077_x5759_x1236860229}

[[接口的概要信息]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1428671952}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x4077_x5759_x617533895}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x442075981}[Link]{lang="EN-US"}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x4077_x5759_x617730503}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Speed or Duplex: (a)/A - auto; H - half; F - full]{lang="EN-US"}]{#struct_0_x4077_x5759_x1183198529}

[[如果某接口的]{style="font-family:宋体"}[Speed]{lang="EN-US"}]{#struct_0_x4077_x5759_696577020}[属性值为"]{style="font-family:宋体"}[(a)]{lang="EN-US"}["，则表示该接口的速率是通过自动协商获取的]{style="font-family:宋体"}

[[如果某接口的]{style="font-family:宋体"}[Duplex]{lang="EN-US"}]{#struct_0_x4077_x5759_x617664967}[属性值为"]{style="font-family:宋体"}[(a)]{lang="EN-US"}["或者"]{style="font-family:宋体"}[A]{lang="EN-US"}["，则表示该接口的]{style="font-family:宋体"}[Duplex]{lang="EN-US"}[属性是通过自动协商获取的；取值为"]{style="font-family:宋体"}[H]{lang="EN-US"}["则表示为半双工；取值为"]{style="font-family:宋体"}[F]{lang="EN-US"}["则表示为全双工]{style="font-family:宋体"}

[[Type: A - access; T - trunk; H - hybrid]{lang="EN-US"}]{#struct_0_x4077_x5759_x847993524}

[[接口的链路类型，]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x541156074}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x4077_x5759_x617861575}[：表示]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x4077_x5759_393567876}[：表示]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x4077_x5759_x617796039}[：表示]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[链路类型]{style="font-family:宋体"}

[[Link]{lang="EN-US"}]{#struct_0_x4077_x5759_x997291116}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x997225580}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x4077_x5759_1683456844}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4077_x5759_x2022285281}[：表示]{lang="EN-US" style="font-family:宋体"}[接口]{style="font-family:宋体"}[物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x4077_x5759_x997160044}[：表示接口被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x4077_x5759_886711710}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_x4077_x5759_x1232225294}

[[接口的速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}]{#struct_0_x4077_x5759_886935303}

[[Duplex]{lang="EN-US"}]{#struct_0_x4077_x5759_x616944071}

[[接口的双工模式，取值为：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x827153046}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x4077_x5759_x616878535}[：表示双工模式由自动协商结果决定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_x4077_x5759_308967419}[：表示全双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F(a)]{lang="EN-US"}]{#struct_0_x4077_x5759_x127778411}[：表示自由协商的结果为全双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x4077_x5759_x617468362}[：表示半双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H(a)]{lang="EN-US"}]{#struct_0_x4077_x5759_x434276486}[：表示自由协商的结果为半双工]{lang="EN-US" style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x4077_x5759_x617402826}

[[链路类型，取值为：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2010912408}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x4077_x5759_x617599434}[：表示]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x4077_x5759_x1237187909}[：表示]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x4077_x5759_x818228262}[：表示]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[链路类型]{style="font-family:宋体"}

[[PVID]{lang="EN-US"}]{#struct_0_x4077_x5759_x617533898}

[[接口所在的缺省]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x442927949}[VLAN ID]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x4077_x5759_x617730506}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1183001921}

[[Cause]{lang="EN-US"}]{#struct_0_x4077_x5759_x1231897607}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x4077_x5759_x616944074}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时]{style="font-family:宋体"}[表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1558825221 .myid}
[]{#_Toc404791525}[]{#struct_0_x4077_x5759_x709917140}[]{#_Toc339307294}[]{#_Toc353355090}[]{#_Toc353355091}[]{#_Toc353355092}[]{#_Toc353355093}[]{#_Toc353355094}[]{#_Toc353355095}[]{#_Toc353355096}[]{#_Toc353355097}[]{#_Toc353355098}[]{#_Toc353355099}[]{#_Toc353355100}[]{#_Toc353355101}[]{#_Toc353355102}[]{#_Toc353355103}[]{#_Toc353355104}[]{#_Toc353355105}[]{#_Toc353355106}[]{#_Toc353355107}[]{#_Toc353355108}[]{#_Toc353355109}[]{#_Toc353355110}[]{#_Toc353355111}[]{#_Toc353355112}[]{#_Toc353355113}[]{#_Toc353355114}[]{#_Toc353355115}[]{#_Toc353355116}[]{#_Toc353355117}[]{#_Toc353355118}[]{#_Toc353355119}[]{#_Toc353355120}[]{#_Toc353355121}[]{#_Toc353355122}[]{#_Toc353355123}[]{#_Toc353355124}[]{#_Toc353355125}[]{#_Toc353355126}[]{#_Toc353355127}[]{#_Toc353355128}[]{#_Toc353355129}[]{#_Toc353355130}[]{#_Toc353355131}[]{#_Toc353355132}[]{#_Toc353355133}[]{#_Toc353355134}[]{#_Toc353355135}[]{#_Toc353355136}[]{#_Toc353355137}[]{#_Toc353355138}[]{#_Toc353355139}[]{#_Toc353355187}[]{#_Toc361661662}[]{#_Toc361661663}[]{#_Toc361661664}[]{#_Toc361661665}[]{#_Toc361661666}[]{#_Toc361661667}[]{#_Toc361661668}[]{#_Toc361661669}[]{#_Toc361661670}[]{#_Toc361661671}[]{#_Toc361661672}[]{#_Toc361661673}[]{#_Toc361661674}[]{#_Toc361661675}[]{#_Toc361661676}[]{#_Toc361661677}[]{#_Toc361661678}[]{#_Toc361661679}[]{#_Toc361661680}[]{#_Toc361661681}[]{#_Toc361661682}[]{#_Toc361661683}[]{#_Toc361661684}[]{#_Toc361661685}[]{#_Toc361661686}[]{#_Toc361661687}[]{#_Toc361661688}[]{#_Toc361661728}[]{#_Toc361661729}[]{#_Toc361661730}[]{#_Toc361661731}[]{#_Toc361661732}[]{#_Toc361661733}[]{#_Toc361661734}[]{#_Toc361661735}[]{#_Toc361661736}[]{#_Toc361661737}[]{#_Toc361661738}[]{#_Toc361661739}[]{#_Toc361661740}[]{#_Toc361661741}[]{#_Toc361661742}[]{#_Toc361661743}[]{#_Toc361661744}[]{#_Toc361661745}[]{#_Toc361661746}[]{#_Toc361661747}[]{#_Toc361661748}[]{#_Toc361661749}[]{#_Toc361661750}[]{#_Toc361661751}[]{#_Toc361661752}[]{#_Toc361661753}[]{#_Toc361661754}[]{#_Toc361661755}[]{#_Toc361661756}[]{#_Toc361661757}[]{#_Toc361661758}[]{#_Toc361661759}[]{#_Toc361661760}[]{#_Toc361661761}[]{#_Toc361661762}[]{#_Toc361661763}[]{#_Toc361661862}[]{#_Toc361661863}[]{#_Toc361661864}[]{#_Toc361661865}[]{#_Toc361661866}[]{#_Toc361661867}[]{#_Toc361661868}[]{#_Toc361661869}[]{#_Toc361661870}[]{#_Toc361661871}[]{#_Toc361661872}[]{#_Toc361661873}[]{#_Toc361661874}[]{#_Toc361661875}[]{#_Toc361661897}[]{#_Toc361661898}[]{#_Toc361661899}[]{#_Toc361661900}[]{#_Toc361661901}[]{#_Toc361661902}[]{#_Toc361661903}[]{#_Toc361661904}[]{#_Toc361661905}[]{#_Toc361661906}[]{#_Toc361661907}[]{#_Toc361661908}[]{#_Toc361661909}[]{#_Toc361661910}[]{#_Toc361661911}[]{#_Toc361661912}[]{#_Toc361661913}[]{#_Toc361661914}[]{#_Toc361661915}[]{#_Toc361661916}[]{#_Toc361661917}[]{#_Toc361661918}[]{#_Toc361661919}[]{#_Toc361661920}[]{#_Toc361661921}[]{#_Toc361661922}[]{#_Toc361661923}[]{#_Toc361661924}[]{#_Toc361661925}[]{#_Toc361661926}[]{#_Toc361661927}[]{#_Toc361661928}[]{#_Toc361661929}[]{#_Toc361661930}[]{#_Toc361661931}[]{#_Toc361661932}[]{#_Toc361661933}[]{#_Toc361661934}[]{#_Toc361661935}[]{#_Toc361661936}[]{#_Toc361661974}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn bgp**

------------------------------------------------------------------------

[**[display l2vpn bgp]{lang="EN-US"}**]{#struct_0_x4077_x5759_325433158}[命令用来显示]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[的标签块信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_964470683}

[**[display l2vpn bgp]{lang="EN-US"}**[ \[ **local** \| **peer** *ip-address* \] \[ **xconnect-group** ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1728666121}*[group-name]{lang="IT"}[ ]{lang="IT"}*[\] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x108187024}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_225857198}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1708612592}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x389084834}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_326022982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x690677043}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_1329568517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1737435114}

[**[local]{lang="EN-US"}**]{#struct_0_x4077_x5759_2136747971}[：只显示本地分配的标签块信息。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_326088518}[：显示]{style="font-family:宋体"}[从指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的标签块信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址。]{style="font-family:宋体"}

[**[xconnect-group]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_1542557921}*[group-name]{lang="IT"}*[：显示指定交叉连接组内的标签块信息。]{style="font-family:宋体"}*[group-name]{lang="IT"}*[表示]{style="font-family:宋体"}[交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示所有交叉连接组的标签块信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1285555155}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1957453353}

[[执行本命令时指定了]{style="font-family:宋体"}**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_325498695}[参数，如果存在与从远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的标签块匹配的本地标签块，即接收到的标签块信息中携带的远端]{style="font-family:宋体"}[Site ID]{lang="EN-US"}[满足条件：本地标签块]{style="font-family:宋体"}[LO\<=]{lang="EN-US"}[远端]{style="font-family:宋体"}[Site ID\<=]{lang="EN-US"}[本地标签块]{style="font-family:宋体"}[LO+LR-1]{lang="EN-US"}[，则同时显示远端标签块和匹配的本地标签块信息；否则，只显示从远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的标签块信息。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x2112856117}[和]{style="font-family:宋体"}**[local]{lang="EN-US"}**[参数，则]{style="font-family:宋体"}[显示从所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的]{style="font-family:宋体"}[标签块信息。如果存在与远端标签块匹配的本地标签块，则同时显示本地标签块信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x989123517}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1348087859}[显示从所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的]{style="font-family:宋体"}[标签块的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp]{lang="EN-US"}]{#struct_0_x4077_x5759_325564231}

[Total number of BGP PWs: 1, 1 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Xconnect-group Name: vpnb, Site ID:1]{lang="EN-US"}

[Rmt Site   Offset  RD                    Nexthop          In/Out Label     State]{lang="EN-US"}

[2          0       2:2                   192.3.3.3        1036/1163        Up]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display l2vpn bgp]{lang="EN-US"}]{#struct_0_x4077_x5759_x1760218214}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x774381380}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1565027486}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_253813958}

[[Total number of BGP PWs]{lang="EN-US"}]{#struct_0_x4077_x5759_582695037}

[[BGP PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1106304560}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_325629767}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_60877837}

[[Site ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1273557550}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x4555928}[标识符]{style="font-family:宋体"}

[[Rmt Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x1590285673}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_325695303}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_x4077_x5759_1248116122}

[[远端标签块的偏移量]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1003321325}

[[RD]{lang="EN-US"}]{#struct_0_x4077_x5759_x637998064}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1974044621}

[[Nexthop]{lang="EN-US"}]{#struct_0_x4077_x5759_x860747915}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_325236551}[地址]{style="font-family:宋体"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_x4077_x5759_1125897512}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_250592828}[的入标签和出标签值]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_1018608367}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_325302087}[状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x425255800}[显示从所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到的]{style="font-family:宋体"}[标签块的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_325367623}

[Xconnect-group Name: vpnb, Site ID:1]{lang="EN-US"}

[ Remote Site ID     : 2]{lang="EN-US"}

[ Offset             : 0]{lang="EN-US"}

[ RD                 : 2:2]{lang="EN-US"}

[ PW State           : Up]{lang="EN-US"}

[ Encapsulation      : VLAN]{lang="EN-US"}

[ MTU                : 1500]{lang="EN-US"}

[ Nexthop            : 192.3.3.3]{lang="EN-US"}

[ Local VC Label     : 1036]{lang="EN-US"}

[ Remote VC Label    : 1163]{lang="EN-US"}

[ Link ID            : 1]{lang="EN-US"}

[ Local Label Block  : 1034/10/0]{lang="EN-US"}

[ Remote Label Block : 1162/10/0]{lang="EN-US"}

[ Export Route Target: 2:2]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display l2vpn bgp verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_1521836336}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x773516388}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_634407332}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1700613704}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_x1329085542}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x364668556}

[[Site ID]{lang="EN-US"}]{#struct_0_x4077_x5759_325433159}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_964470684}[标识符]{style="font-family:宋体"}

[[Remote Site ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1728666122}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_295097503}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_x4077_x5759_x283324355}

[[远端标签块的偏移量]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1768024326}

[[RD]{lang="EN-US"}]{#struct_0_x4077_x5759_326022983}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x690677044}

[[PW State]{lang="EN-US"}]{#struct_0_x4077_x5759_1329109765}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1369591094}[状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Encapsulation]{lang="EN-US"}]{#struct_0_x4077_x5759_x1147418675}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_326088519}[数据封装类型]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_x4077_x5759_1542557920}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1285489619}[协商后的最大传输单元，单位为字节]{style="font-family:宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_x4077_x5759_1056428945}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_325498692}[地址]{style="font-family:宋体"}

[[Local VC Label]{lang="EN-US"}]{#struct_0_x4077_x5759_x2112856120}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1748441796}[的入标签]{style="font-family:宋体"}

[[Remote VC Label]{lang="EN-US"}]{#struct_0_x4077_x5759_774924671}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1488884116}[的出标签]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_325564228}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_578433939}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[Local Label Block]{lang="EN-US"}]{#struct_0_x4077_x5759_1930704474}

[[本端的标签块信息，包括标签块的初始标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4077_x5759_1966817877}[标签块大小]{style="font-family:宋体"}[/]{lang="EN-US"}[标签块的偏移量]{style="font-family:宋体"}

[[Remote Label Block]{lang="EN-US"}]{#struct_0_x4077_x5759_325629764}

[[从远端收到的标签块信息，包括标签块的初始标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4077_x5759_60877836}[标签块大小]{style="font-family:宋体"}[/]{lang="EN-US"}[标签块的偏移量]{style="font-family:宋体"}

[[Export ]{lang="EN-US"}[Route Target]{lang="EN-US"}]{#struct_0_x4077_x5759_x682757586}

[[从远端收到的标签块对应的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}]{#struct_0_x4077_x5759_x1269194011}[属性]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_325695300}[显示所有本地分配的标签块的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp local]{lang="EN-US"}]{#struct_0_x4077_x5759_1248116119}

[Xconnect-group Name: vpnb]{lang="EN-US"}

[Site   Offset  Range  Label Base    RD]{lang="EN-US"}

[1      0       10     1034          2:2]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display l2vpn bgp local]{lang="EN-US"}]{#struct_0_x4077_x5759_x1003649002}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x777355588}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1150068564}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1910229487}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_325236548}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1212754641}

[[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_1226518539}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x1005070316}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_x4077_x5759_1238866118}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_325302084}[分配的标签块的偏移量]{style="font-family:宋体"}

[[Range]{lang="EN-US"}]{#struct_0_x4077_x5759_x425255797}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x575495460}[分配的标签块大小]{style="font-family:宋体"}

[[Label Base]{lang="EN-US"}]{#struct_0_x4077_x5759_1075667029}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_1978104778}[分配的标签块的初始标签值]{style="font-family:宋体"}

[[RD]{lang="EN-US"}]{#struct_0_x4077_x5759_821430103}

[[标签块对应的路由标识符，如果没有配置，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x4077_x5759_325367620}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1521836335}[显示所有本地分配的标签块的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn bgp local verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_325433156}

[Xconnect-group Name: vpnb]{lang="EN-US"}

[ Site ID            : 1]{lang="EN-US"}

[ Offset             : 0]{lang="EN-US"}

[ RD                 : 2:2]{lang="EN-US"}

[ Range              : 10]{lang="EN-US"}

[ Label Base         : 1034]{lang="EN-US"}

[ Link ID            : 1]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display l2vpn bgp local verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_964470669}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x783402212}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_183018993}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x571259592}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_x1690769310}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x976833580}

[[Site ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1750829146}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_326022980}[标识符]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_x4077_x5759_x690677045}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_1329175301}[分配的标签块的偏移量]{style="font-family:宋体"}

[[RD]{lang="EN-US"}]{#struct_0_x4077_x5759_x549988880}

[[标签块对应的路由标识符，如果没有配置，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x4077_x5759_x1852918126}["]{style="font-family:宋体"}

[[Range]{lang="EN-US"}]{#struct_0_x4077_x5759_326088516}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_1542557923}[分配的标签块大小]{style="font-family:宋体"}

[[Label Base]{lang="EN-US"}]{#struct_0_x4077_x5759_x1285424083}

[[为该]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_868495803}[分配的标签块的初始标签值]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1767566668}

[[标签块对应的]{style="font-family:宋体"}[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1878527688}[序列值，即基于该标签块建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[Link ID]{lang="EN-US"}[值]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_325498693}[来说，由于每个交叉连接下只能创建一条]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，因此]{style="font-family:宋体"}[Link ID]{lang="EN-US"}[固定为]{style="font-family:宋体"}[1]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2112856119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}[pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_x538784823}

::: {#-821721945 .myid}
[]{#_Toc404791526}[]{#struct_0_x4077_x5759_562434119}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn ldp**

------------------------------------------------------------------------

[**[display l2vpn ldp]{lang="EN-US"}**]{#struct_0_x4077_x5759_57644960}[命令用来显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2084765903}

[**[display l2vpn ldp ]{lang="EN-US"}**[\[ **peer** *ip-address* \[ **pw-id** *pw-id* \] \| ]{lang="EN-US"}]{#struct_0_x4077_x5759_x795389761}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}[ ]{lang="IT"}*[\] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_325564229}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_578433938}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1930704475}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1966883413}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_75214996}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x2054013748}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_1647306438}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_91457619}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_325629765}[：显示指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。如果没有指定本参数，则显示所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_60877835}[：显示指定]{style="font-family:
宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果指定了]{style="font-family:宋体"}**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[参数，没有指定本参数，则显示指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[xconnect-group ]{lang="IT"}**]{#struct_0_x4077_x5759_1655894574}*[group-name]{lang="IT"}*[：显示指定交叉连接组内]{style="font-family:
宋体"}[LDP]{lang="EN-US"}[协议通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[group-name]{lang="IT"}*[表示]{style="font-family:宋体"}[交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示所有交叉连接组内]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4077_x5759_1463112099}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_534199516}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1658377204}[显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn ldp]{lang="EN-US"}]{#struct_0_x4077_x5759_325695301}

[Total number of LDP PWs: 5, 4 up, 1 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer            PW ID/VPLS ID         In/Out Label    State Owner]{lang="EN-US"}

[192.3.3.3       1001                  775125/775126   Up    vpws1]{lang="EN-US"}

[192.3.3.3       1001                  775125/775126   Up    vpws1]{lang="EN-US"}

[192.3.3.3       1003                  775117/775122   Up    vpws3]{lang="EN-US"}

[192.3.3.3       1004                  775120/775120   Up    vpws4]{lang="EN-US"}

[192.4.4.4       1000                  775116/unknown  Down  vpws5]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display l2vpn ldp]{lang="EN-US"}]{#struct_0_x4077_x5759_1248116120}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x787217124}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1003190253}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1536649172}

[[Total number of LDP PWs]{lang="EN-US"}]{#struct_0_x4077_x5759_x801260615}

[[LDP PW]{lang="EN-US"}]{#struct_0_x4077_x5759_340455615}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_x4077_x5759_x1081211648}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_325236549}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID/VPLS ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1212754640}

[[对于]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}]{#struct_0_x4077_x5759_x1502364816}[方式，为]{style="font-family:宋体"}[PW]{lang="EN-US"}[标识符]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[；对于]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式，为用来标识]{style="font-family:宋体"}[PE]{lang="EN-US"}[所属]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例的]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}

[[只有]{style="font-family:宋体"}[VPLS]{lang="EN-US"}]{#struct_0_x4077_x5759_x1535857960}[支持]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_x4077_x5759_2000339805}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_325302085}[的入标签和出标签]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x425255798}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x575954212}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_x848767666}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x4077_x5759_x1130771864}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[处于]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[Owner]{lang="EN-US"}]{#struct_0_x4077_x5759_325367621}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1521836334}[所属交叉连接组的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_634538404}[显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议通告的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn ldp verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_325433157}

[Peer: 192.2.2.2        PW ID: 1000]{lang="EN-US"}

[  Xconnect-group: vpn1]{lang="EN-US"}

[  Connection    : ldp]{lang="EN-US"}

[  PW State      : Up]{lang="EN-US"}

[  PW Status Communication: Notification method]{lang="EN-US"}

[  PW ID FEC (Local/Remote):]{lang="EN-US"}

[    PW Type     : VLAN/VLAN]{lang="EN-US"}

[    Group ID    : 0/0]{lang="EN-US"}

[    Label       : 1151/1279]{lang="EN-US"}

[    Control Word: Disabled/Disabled]{lang="EN-US"}

[    VCCV CC Type: -/-]{lang="EN-US"}

[    VCCV CV Type: -/-]{lang="EN-US"}

[    MTU         : 1500/1500]{lang="EN-US"}

[    PW Status   : PW forwarding/PW forwarding]{lang="EN-US"}

[Peer: 192.3.3.3        PW ID: 1]{lang="EN-US"}

[  Xconnect-group: x1]{lang="EN-US"}

[  Connection    : c1]{lang="EN-US"}

[  PW State      : Up]{lang="EN-US"}

[  PW Status Communication: Notification method]{lang="EN-US"}

[  PW ID FEC (Local/Remote):]{lang="EN-US"}

[    PW Type     : TDM-CESoPSN-Basic/TDM-CESoPSN-Basic]{lang="EN-US"}

[    Group ID    : 0/0]{lang="EN-US"}

[    Label       : 710127/710127]{lang="EN-US"}

[    Control Word: Enabled/Enabled]{lang="EN-US"}

[    VCCV CV Type: LSP Ping/LSP Ping]{lang="EN-US"}

[    VCCV CC Type: -/-]{lang="EN-US"}

[    Bit Rate    : 10/10]{lang="EN-US"}

[    Payload     : 80/80]{lang="EN-US"}

[    RTP Header  : Enabled/Enabled]{lang="EN-US"}

[    Timestamping: Differential/Differential]{lang="EN-US"}

[    Frequency   : 0/0]{lang="EN-US"}

[    PW Status   : PW forwarding/PW forwarding]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display l2vpn ldp verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_964470670}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x784699620}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1773296134}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x600943604}

[[Peer]{lang="EN-US"}]{#struct_0_x4077_x5759_x545686229}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_879056363}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID]{lang="EN-US"}]{#struct_0_x4077_x5759_326022981}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x690677046}[标识符]{style="font-family:宋体"}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_1329240837}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1751895009}[所属交叉连接组的名称]{style="font-family:宋体"}

[[Connection]{lang="EN-US"}]{#struct_0_x4077_x5759_x958840888}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x891751659}[所属交叉连接的名称]{style="font-family:宋体"}

[[PW State]{lang="EN-US"}]{#struct_0_x4077_x5759_326088517}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1542557922}[状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[PW Status Communication]{lang="EN-US"}]{#struct_0_x4077_x5759_x1285358547}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1661028195}[状态通知方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Notification method]{lang="EN-US"}]{#struct_0_x4077_x5759_567455468}[：通过]{lang="EN-US" style="font-family:
  宋体"}[Notification]{lang="EN-US"}[消息通知]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Label withdraw method]{lang="EN-US"}]{#struct_0_x4077_x5759_325498690}[：标签回收方式，即只有]{style="font-family:宋体"}[PW]{lang="EN-US"}[连接的]{style="font-family:宋体"}[AC]{lang="EN-US"}[状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[时才会为该]{style="font-family:宋体"}[PW]{lang="EN-US"}[分配]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签，]{style="font-family:宋体"}[AC]{lang="EN-US"}[状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[时回收该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ]{lang="EN-US"}[标签]{style="font-family:宋体"}

[[PW ID FEC (Local/Remote)]{lang="EN-US"}]{#struct_0_x4077_x5759_x2112856122}

[[本地向远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_x585642382}[通告的]{style="font-family:宋体"}[PW ID FEC]{lang="EN-US"}[相关信息]{style="font-family:宋体"}[/]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通告给本地的]{style="font-family:宋体"}[PW ID FEC]{lang="EN-US"}[相关信息]{style="font-family:宋体"}

[[PW Type]{lang="EN-US"}]{#struct_0_x4077_x5759_x277521411}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x2133160506}[数据封装类型]{style="font-family:宋体"}

[[Group ID]{lang="EN-US"}]{#struct_0_x4077_x5759_325564226}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_578433953}[的]{style="font-family:宋体"}[Group]{lang="EN-US"}[标识符]{style="font-family:宋体"}

[[Label]{lang="EN-US"}]{#struct_0_x4077_x5759_x1217251760}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1888895942}[标签]{style="font-family:宋体"}

[[Control Word]{lang="EN-US"}]{#struct_0_x4077_x5759_325629762}

[[是否使能控制字功能，取值包括]{style="font-family:宋体"}]{#struct_0_x4077_x5759_60877842}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4077_x5759_841431349}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[使能了控制字功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4077_x5759_x2119384763}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[未使能控制字功能]{lang="EN-US" style="font-family:宋体"}

[[VCCV CC Type]{lang="EN-US"}]{#struct_0_x4077_x5759_844067531}

[[支持的]{style="font-family:宋体"}[VCCV CC]{lang="EN-US"}]{#struct_0_x4077_x5759_325695298}[（]{style="font-family:宋体"}[Control Channel]{lang="EN-US"}[，控制通道）类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_x4077_x5759_491336250}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_x4077_x5759_x641988915}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_x4077_x5759_4961929}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV]{lang="EN-US"}]{#struct_0_x4077_x5759_325236546}[（]{style="font-family:宋体"}[Virtual Circuit Connectivity Verification]{lang="EN-US"}[，虚电路连通性验证）的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS OAM]{lang="EN-US"}["]{style="font-family:宋体"}

[[VCCV CV Type]{lang="EN-US"}]{#struct_0_x4077_x5759_x1212754655}

[[支持的]{style="font-family:宋体"}[VCCV CV]{lang="EN-US"}]{#struct_0_x4077_x5759_x1099145825}[（]{style="font-family:宋体"}[Connectivity Verification]{lang="EN-US"}[，连通性验证）类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP Ping]{lang="EN-US"}]{#struct_0_x4077_x5759_325302082}[：采用]{lang="EN-US" style="font-family:宋体"}[MPLS ping]{lang="EN-US"}[检测]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x425255795}[：]{style="font-family:宋体"}[采用]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性，]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:宋体"}[IP/UDP Encapsulation (with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Raw-BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x575626532}[：采用]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性，]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内的]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_x4077_x5759_x1640251807}

[[交叉连接的最大传输单元]{style="font-family:宋体"}]{#struct_0_x4077_x5759_325367618}

[[Bit Rate]{lang="EN-US"}]{#struct_0_x4077_x5759_x617730500}

[[TDM]{lang="EN-US"}]{#struct_0_x4077_x5759_x1183395137}[接口比特率，取值与电路仿真接口的电路类型有关（单位：]{style="font-family:宋体"}[64Kbit/s]{lang="EN-US"}[）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SAToP]{lang="EN-US"}]{#struct_0_x4077_x5759_x617664964}[的]{lang="EN-US" style="font-family:宋体"}[E1]{lang="EN-US"}[口：]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SAToP]{lang="EN-US"}]{#struct_0_x4077_x5759_x847796916}[的]{lang="EN-US" style="font-family:宋体"}[T1]{lang="EN-US"}[口：]{lang="EN-US" style="font-family:宋体"}[24]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CESoPSN]{lang="EN-US"}]{#struct_0_x4077_x5759_x617861572}[的]{lang="EN-US" style="font-family:宋体"}[E1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[T1]{lang="EN-US"}[接口：时隙数]{lang="EN-US" style="font-family:宋体"}

[[Payload]{lang="EN-US"}]{#struct_0_x4077_x5759_393240196}

[[TDM]{lang="EN-US"}]{#struct_0_x4077_x5759_x617796036}[接口的负载大小，单位为字节]{style="font-family:宋体"}

[[RTP Header]{lang="EN-US"}]{#struct_0_x4077_x5759_x1232159758}

[[是否使能]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x4077_x5759_x616944068}[头，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4077_x5759_x616878532}[：使能]{lang="EN-US" style="font-family:宋体"}[RTP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4077_x5759_309295099}[：未使能]{lang="EN-US" style="font-family:宋体"}[RTP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[Timestamping]{lang="EN-US"}]{#struct_0_x4077_x5759_x617468355}

[[RTP]{lang="EN-US"}]{#struct_0_x4077_x5759_x433948807}[头上时间戳的传送方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Differential]{lang="EN-US"}]{#struct_0_x4077_x5759_x617402819}[：差分时钟模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absolute]{lang="EN-US"}]{#struct_0_x4077_x5759_x2010322585}[：绝对时钟模式]{lang="EN-US" style="font-family:宋体"}

[[Frequency]{lang="EN-US"}]{#struct_0_x4077_x5759_x617599427}

[[RTP]{lang="EN-US"}]{#struct_0_x4077_x5759_x1237253444}[头上打时间戳的时钟频率]{style="font-family:宋体"}

[[PW Status]{lang="EN-US"}]{#struct_0_x4077_x5759_x434478809}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x445020309}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW forwarding]{lang="EN-US"}]{#struct_0_x4077_x5759_x2036199318}[：]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[可以转发报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW not forwarding]{lang="EN-US"}]{#struct_0_x4077_x5759_325433154}[：]{lang="EN-US" style="font-family:
  宋体"}[PW]{lang="EN-US"}[不可以转发报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC receive fault]{lang="EN-US"}]{#struct_0_x4077_x5759_964470671}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[接收方向失效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AC transmit fault]{lang="EN-US"}]{#struct_0_x4077_x5759_x1773296135}[：]{lang="EN-US" style="font-family:
  宋体"}[AC]{lang="EN-US"}[发送方向失效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW receive fault]{lang="EN-US"}]{#struct_0_x4077_x5759_326022978}[：]{lang="EN-US" style="font-family:
  宋体"}[PW]{lang="EN-US"}[接收方向失效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW transmit fault]{lang="EN-US"}]{#struct_0_x4077_x5759_2030312147}[：]{lang="EN-US" style="font-family:
  宋体"}[PW]{lang="EN-US"}[发送方向失效]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

::: {#-697284031 .myid}
[]{#_Toc404791527}[]{#struct_0_x4077_x5759_x319426263}[]{#_Toc242067216}[]{#_Toc185927308}[]{#_Toc123026768}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn forwarding**

------------------------------------------------------------------------

[**[display l2vpn forwarding]{lang="EN-US"}**]{#struct_0_x4077_x5759_x162808871}[命令用来显示交叉连接的转发信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1075018989}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1299353639}

[**[display l2vpn forwarding]{lang="EN-US"}**[ { **ac** \| **pw** } \[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_1071315714}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}*[ ]{lang="IT"}[\] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备―独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4077_x5759_326088514}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display l2vpn forwarding]{lang="EN-US"}**[ { **ac** \| **pw** } \[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_1542557925}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}*[ ]{lang="IT"}[\] \[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4077_x5759_x1285293011}[模式：]{style="font-family:宋体"}

[**[display l2vpn forwarding]{lang="EN-US"}**[ { **ac** \| **pw** } \[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_916126968}**[xconnect-group ]{lang="IT"}***[group-name ]{lang="IT"}*[\] \[ **chassis** *chassis-number* ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1164656993}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1078849741}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_105752630}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x140678964}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_325498691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x2112856121}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_x182357855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_118792799}

[**[ac]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2120035291}[：显示]{style="font-family:宋体"}[AC]{lang="EN-US"}[的转发信息。]{style="font-family:宋体"}

[**[pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_959463552}[：显示]{style="font-family:宋体"}[PW]{lang="EN-US"}[的转发信息。]{style="font-family:宋体"}

[**[xconnect-group ]{lang="IT"}**]{#struct_0_x4077_x5759_1757139937}*[group-name]{lang="IT"}*[：显示指定交叉连接组的转发信息。]{style="font-family:
宋体"}*[group-name]{lang="IT"}*[表示]{style="font-family:宋体"}[交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有交叉连接组的转发信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_x2049092305}[：显示指定单板上的交叉连接转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示主用主控板上的交叉连接转发信息。（分布式设备―独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1864847431}[：显示指定成员设备上的交叉连接转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的交叉连接转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_1371760653}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的交叉连接转发信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的交叉连接转发信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_325564227}[：显示指定成员设备上指定单板的交叉连接转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主用主控板的交叉连接转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_x35048277}[：显示指定单板的交叉连接转发信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主用主控板的交叉连接转发信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_1891411902}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的交叉连接转发信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4077_x5759_578433952}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1217251759}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1196152237}[显示所有交叉连接组的]{style="font-family:宋体"}[AC]{lang="EN-US"}[转发简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding ac]{lang="EN-US"}]{#struct_0_x4077_x5759_x1184338089}

[Total number of cross-connections: 3]{lang="EN-US"}

[Total number of ACs: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[AC                               Xconnect-group                  Link ID]{lang="EN-US"}

[GE1/0/5 srv1                     vpn1                            0]{lang="EN-US"}

[GE1/0/5 srv2                     vpn2                            1]{lang="EN-US"}

[GE1/0/6                          vpn3                            0]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display l2vpn forwarding ac]{lang="EN-US"}]{#struct_0_x4077_x5759_x1470634438}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x756779652}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_325629763}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_60877841}

[[Total number of cross-connections]{lang="EN-US"}]{#struct_0_x4077_x5759_x1114883787}

[[所有交叉连接组或指定交叉连接组下交叉连接的总数，包括没有关联]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_2058002436}[的交叉连接]{style="font-family:宋体"}

[[Total number of ACs]{lang="EN-US"}]{#struct_0_x4077_x5759_x332058787}

[[所有交叉连接组或指定交叉连接组下]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_x1588623745}[的总数]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_325695299}

[[接入电路，取值有如下两种：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_491336251}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层接口名称：如]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x641988916}[GE1/0/6]{lang="EN-US"}[。在交叉连接视图下关联三层接口时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层接口名称和以太网服务实例：如]{style="font-family:宋体"}]{#struct_0_x4077_x5759_5158537}[GE1/0/5 srv1]{lang="EN-US"}[。在交叉连接视图下关联以太网服务实例时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_500491416}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_325236547}[所属交叉连接组的名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1212754654}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_466938116}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_734573374}[显示所有交叉连接组的]{style="font-family:宋体"}[AC]{lang="EN-US"}[转发详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding ac verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_325302083}

[Xconnect-group: vpws1]{lang="EN-US"}

[ Connection: actopw]{lang="EN-US"}

[  Interface: GE1/0/3  Service Instance: 1]{lang="EN-US"}

[    Link ID      : 1]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[    Encapsulation: s-vid 1 to 16]{lang="EN-US"}

[ Connection: actoac]{lang="EN-US"}

[  Interface: Vlan13]{lang="EN-US"}

[    Link ID      : 0]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[  Interface: GE1/0/3  Service Instance: 4]{lang="EN-US"}

[    Link ID      : 1]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[    Encapsulation: untagged]{lang="EN-US"}

[    Reflector    : ]{lang="EN-US"}

[      IP Address   : 100.1.1.4]{lang="EN-US"}

[      MAC Address  : 8850-fc51-5cee]{lang="EN-US"}

[      Src Port     : 200]{lang="EN-US"}

[      Dst Port     : 201]{lang="EN-US"}

[Xconnect-group: vpws5]{lang="EN-US"}

[ Connection: actopw]{lang="EN-US"}

[  Interface: Vlan14]{lang="EN-US"}

[    Link ID      : 0]{lang="EN-US"}

[    Access Mode  : VLAN]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display l2vpn forwarding ac verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_x425255796}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x763136356}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x575560996}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1175650918}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_1433810116}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_325367619}

[[Connection]{lang="EN-US"}]{#struct_0_x4077_x5759_x434478810}

[[交叉连接名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x444561558}

[[Interface]{lang="EN-US"}]{#struct_0_x4077_x5759_681018831}

[[接入接口]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x708015082}

[[Service Instance]{lang="EN-US"}]{#struct_0_x4077_x5759_325433155}

[[以太网服务实例，]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_964470672}[为二层接口的以太网服务实例时才显示该字段]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1773296136}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_561855810}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[Access Mode]{lang="EN-US"}]{#struct_0_x4077_x5759_139303261}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_326022979}[接入模式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_x4077_x5759_2030312146}[：]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_x4077_x5759_x319491799}[：]{lang="EN-US" style="font-family:宋体"}[Ethernet]{lang="EN-US"}[模式]{lang="EN-US" style="font-family:宋体"}

[[Encapsulation]{lang="EN-US"}]{#struct_0_x4077_x5759_1414356489}

[[以太网服务实例的报文匹配规则，]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_x1352733066}[为二层接口的以太网服务实例时才显示该字段]{style="font-family:宋体"}

[[Reflector]{lang="EN-US"}]{#struct_0_x4077_x5759_x2034825010}

[[报文反射信息]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x101413219}

[[IP Address]{lang="EN-US"}]{#struct_0_x4077_x5759_x112445173}

[[待反射报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4077_x5759_x1551814541}[地址]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_x4077_x5759_x1851208689}

[[待反射报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x4077_x5759_x1678529114}[地址]{style="font-family:宋体"}

[[Src Port]{lang="EN-US"}]{#struct_0_x4077_x5759_1745124701}

[[待反射报文的源]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x4077_x5759_344944970}[端口号]{style="font-family:宋体"}

[[Dst Port]{lang="EN-US"}]{#struct_0_x4077_x5759_1050354241}

[[待反射报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x4077_x5759_1770279620}[端口号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_326088515}[显示所有交叉连接组的]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding pw]{lang="EN-US"}]{#struct_0_x4077_x5759_1542557924}

[Total number of cross-connections: 1]{lang="EN-US"}

[Total number of PWs: 2, 2 up, 0 blocked, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Xconnect-group                  In/Out Label    NID        Link ID    State]{lang="EN-US"}

[vpn1                            1279/1151       1025       0          Up]{lang="EN-US"}

[vpn1                            1278/1151       1027       1          Up]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display l2vpn forwarding pw]{lang="EN-US"}]{#struct_0_x4077_x5759_x1285227475}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x760480196}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2117395723}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_837057160}

[[Total number of cross-connections]{lang="EN-US"}]{#struct_0_x4077_x5759_x22881872}

[[所有交叉连接组或指定交叉连接组下交叉连接的总数，包括没有配置]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891582635}[的交叉连接]{style="font-family:宋体"}

[[Total number of PWs]{lang="EN-US"}]{#struct_0_x4077_x5759_x1230410029}

[[所有交叉连接组或指定交叉连接组下]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_19049187}[总数，以及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[blocked]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_x1621313282}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1152705057}[所属交叉连接组的名称]{style="font-family:宋体"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_x4077_x5759_1891648171}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1890694028}[的入标签和出标签]{style="font-family:宋体"}

[[NID]{lang="EN-US"}]{#struct_0_x4077_x5759_1861954261}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1702222573}[的隧道对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[存在等价隧道时，一个]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x924488188}[PW]{lang="EN-US"}[会对应多个]{style="font-family:宋体"}[NID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不存在隧道，显示为]{lang="EN-US" style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_x4077_x5759_x1589860808}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1891713707}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x2014184837}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x404062046}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1453455548}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[和]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}

[[其中，]{style="font-family:宋体"}[Blocked]{lang="EN-US"}]{#struct_0_x4077_x5759_414376933}[为存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，当前没有转发流量、起到备份作用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的状态；]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}[为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷的状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1891779243}[显示所有交叉连接组的]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn forwarding pw verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_1884831453}

[Xconnect-group: vpn1]{lang="EN-US"}

[ Connection: ldp]{lang="EN-US"}

[  Link ID: 0]{lang="EN-US"}

[    PW Type         : VLAN                  PW State : Up]{lang="EN-US"}

[    In Label        : 1279                  Out Label: 1151]{lang="EN-US"}

[    MTU             : 1500]{lang="EN-US"}

[    PW Attributes   : Main]{lang="EN-US"}

[    VCCV CC         : Router-Alert]{lang="EN-US"}

[    VCCV BFD        : Fault Detection with BFD]{lang="EN-US"}

[    Tunnel Group ID : 0x60000000]{lang="EN-US"}

[    Tunnel NHLFE IDs: 1025]{lang="EN-US"}

[  Link ID: 1]{lang="EN-US"}

[    PW Type         : VLAN                  PW State : Up]{lang="EN-US"}

[    In Label        : 1278                  Out Label: 1151]{lang="EN-US"}

[    MTU             : 1500]{lang="EN-US"}

[    PW Attributes   : Main]{lang="EN-US"}

[    VCCV CC         : Router-Alert]{lang="EN-US"}

[    VCCV BFD        : Fault Detection with BFD]{lang="EN-US"}

[    Tunnel Group ID : 0x160000001]{lang="EN-US"}

[    Tunnel NHLFE IDs: 1027]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display l2vpn forwarding pw verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_1891320491}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x764123684}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x471836471}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1167475038}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_548709839}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_215138717}

[[Connection]{lang="EN-US"}]{#struct_0_x4077_x5759_781641645}

[[交叉连接名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1891386027}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1477394952}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1584461933}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[PW Type]{lang="EN-US"}]{#struct_0_x4077_x5759_1844834960}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1593347992}[数据封装类型]{style="font-family:宋体"}

[[PW State]{lang="EN-US"}]{#struct_0_x4077_x5759_1447082784}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891451563}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[和]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}

[[其中，]{style="font-family:宋体"}[Blocked]{lang="EN-US"}]{#struct_0_x4077_x5759_x1242111092}[为存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，当前没有转发流量、起到备份作用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的状态；]{style="font-family:宋体"}[BFD Defect]{lang="EN-US"}[为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷的状态]{style="font-family:宋体"}

[[In Label]{lang="EN-US"}]{#struct_0_x4077_x5759_x1178483560}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1759814624}[的入标签]{style="font-family:宋体"}

[[Out Label]{lang="EN-US"}]{#struct_0_x4077_x5759_957060259}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891517099}[的出标签]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_x4077_x5759_x1261908818}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1242268543}[协商后的最大传输单元]{style="font-family:宋体"}

[[PW Attributes]{lang="EN-US"}]{#struct_0_x4077_x5759_x822734521}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1892106923}[的属性，取值包括]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Main]{lang="EN-US"}]{#struct_0_x4077_x5759_1752908226}[：主]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x4077_x5759_562088131}[：备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[VCCV CC]{lang="EN-US"}]{#struct_0_x4077_x5759_x886204913}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_2147292851}[的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_x4077_x5759_1892172459}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_x4077_x5759_2143514461}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_x4077_x5759_x1835440882}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_1798083302}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891582636}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x1230475565}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[IP/UDP]{lang="EN-US"}[ Encapsulation]{lang="EN-US"}[ ]{lang="EN-US"}[(with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with Raw-BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x2069926572}[：]{style="font-family:
  宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:
  宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[Tunnel Group ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x516952880}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891648172}[的隧道组]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Tunnel NHLFE IDs]{lang="EN-US"}]{#struct_0_x4077_x5759_1890628492}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1611877478}[的隧道对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引列表]{style="font-family:宋体"}

[[存在等价隧道时，一个]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1281344957}[会对应多个索引值]{style="font-family:宋体"}

[[如果不存在隧道，显示为]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_x4077_x5759_1891713708}

[ ]{lang="EN-US"}

::: {#1506055251 .myid}
[]{#_Toc404791528}[]{#struct_0_x4077_x5759_x2013595013}[]{#_Toc300843391}[]{#_Toc300843392}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn interface**

------------------------------------------------------------------------

[**[display l2vpn interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_x702179286}[命令用来显示与交叉连接关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1760556471}

[**[display l2vpn interface ]{lang="EN-US"}**[\[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_x394172689}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}*[ ]{lang="IT"}[\| *interface-type interface-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1582285724}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1168994219}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1891779244}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1884634845}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_x456570472}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1478554221}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_x1317534002}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x827208200}

[**[xconnect-group ]{lang="IT"}**]{#struct_0_x4077_x5759_1228907918}*[group-name]{lang="IT"}*[：显示指定交叉连接组内与交叉连接关联的三层接口的]{style="font-family:
宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[group-name]{lang="IT"}*[表示]{style="font-family:宋体"}[交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_1569504799}[：显示指定接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1891320492}

[[执行本命令时，如果没有指定任何参数，则显示所有与交叉连接关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x471639863}[信息。]{style="font-family:宋体"}

[[本命令只能显示与交叉连接关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_84142416}[信息。若要显示以太网服务实例的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息，则需要执行]{style="font-family:宋体"}**[display l2vpn service-instance]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1463320168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4077_x5759_1558936428}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1140418633}[显示所有与交叉连接关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn interface]{lang="EN-US"}]{#struct_0_x4077_x5759_x2116949973}

[Total number of interfaces: 2, 2 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                Owner                           Link ID   State    Type]{lang="EN-US"}

[GE1/0/1                  vpws1                           1         Up       VPWS]{lang="EN-US"}

[GE1/0/2                  vpws2                           1         Up       VPWS]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4077_x5759_1891386028}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1476805128}[显示所有与交叉连接关联的三层接口的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn interface ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1929670190}

[Total number of interfaces: 2, 2 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                Owner                           Link ID   State    Type]{lang="EN-US"}

[Vlan10                   vpws1                           0         Up       VPWS]{lang="EN-US"}

[Vlan11                   vpws2                           0         Up       VPWS]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display l2vpn interface]{lang="EN-US"}]{#struct_0_x4077_x5759_x384170121}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x767999748}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_233391205}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1962020734}

[[Total number of interfaces]{lang="EN-US"}]{#struct_0_x4077_x5759_1891451564}

[[与交叉连接关联的三层接口的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x4077_x5759_x1242045556}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的接口数目]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4077_x5759_444167660}

[[与交叉连接关联的三层接口的名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x183995401}

[[Owner]{lang="EN-US"}]{#struct_0_x4077_x5759_56265814}

[[接口所属的交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1241802689}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1891517100}

[[接口对应]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_693816485}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_1365845196}

[[接口的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_x1995990574}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x4077_x5759_1836180669}

[[接口所属的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_1892106924}[类型，取值包括]{style="font-family:宋体"}[VSI]{lang="EN-US"}[和]{style="font-family:宋体"}[VPWS]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1753366978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x4077_x5759_1821403538}

::: {#947157421 .myid}
[]{#_Toc404791529}[]{#struct_0_x4077_x5759_1240568110}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn pw**

------------------------------------------------------------------------

[**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_1437722636}[命令用来显示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1789394419}

[**[display]{lang="EN-US"}**[ **l2vpn** **pw** \[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_832522751}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}*[ \] \[ **protocol** { **bgp** \| **ldp** \| **static** } \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_123918609}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1892172460}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2143973210}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_904970608}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_1878762979}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1762189853}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_1483308036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1876503872}

[**[xconnect-group ]{lang="IT"}**]{#struct_0_x4077_x5759_784181482}*[group-name]{lang="IT"}*[：显示指定交叉连接组内]{style="font-family:
宋体"}[L2VPN]{lang="EN-US"}[的]{style="font-family:
宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[group-name]{lang="IT"}*[表示]{style="font-family:宋体"}[交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示所有交叉连接组内]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**]{#struct_0_x4077_x5759_1891582633}[：显示采用指定信令协议建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息。如果没有指定本参数，则显示所有协议产生的]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[bgp]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1230803245}[：显示采用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[作为]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息，即]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[ldp]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1133419168}[：显示采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[作为]{style="font-family:宋体"}[PW]{lang="EN-US"}[信令协议建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息，即]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x4077_x5759_297560683}[：显示采用静态方式建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}[的信息，即静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息，包括]{style="font-family:宋体"}[CCC]{lang="EN-US"}[远程连接信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4077_x5759_x815995799}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x4439203}

[[开启]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1104425622}[统计功能后，可使用]{style="font-family:宋体"}**[display l2vpn pw verbose]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[PW]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1001795804}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x550868336}[显示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw]{lang="EN-US"}]{#struct_0_x4077_x5759_1891648169}

[Flags: M - main, B - backup, H - hub link, S - spoke link, N - no split horizon]{lang="EN-US"}

[Total number of PWs: 2]{lang="EN-US"}

[2 up, 0 blocked, 0 down, 0 defect, 0 idle, 0 duplicate]{lang="EN-US"}

[ ]{lang="EN-US"}

[Xconnect-group Name: ldp]{lang="EN-US"}

[Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State]{lang="EN-US"}

[192.3.3.3       500               1299/1299       LDP     M     0        Up]{lang="EN-US"}

[ ]{lang="EN-US"}

[Xconnect-group Name: vpnb]{lang="EN-US"}

[Peer            PW ID/Rmt Site    In/Out Label    Proto   Flag  Link ID  State]{lang="EN-US"}

[192.3.3.3       2                 1036/1163       BGP     M     1        Up]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display l2vpn pw]{lang="EN-US"}]{#struct_0_x4077_x5759_1890169741}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x740802020}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1903771423}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x9791450}

[[Flags]{lang="EN-US"}]{#struct_0_x4077_x5759_1299808656}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_322286288}[属性标记的取值]{style="font-family:宋体"}

[[Total number of PWs]{lang="EN-US"}]{#struct_0_x4077_x5759_1891713705}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x2014315909}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[blocked]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[、]{style="font-family:宋体"}[defect]{lang="EN-US"}[、]{style="font-family:宋体"}[idle]{lang="EN-US"}[和]{style="font-family:宋体"}[duplicate]{lang="EN-US"}[状态的]{style="font-family:宋体"}[PW]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_1959061192}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1888202861}

[[Peer]{lang="EN-US"}]{#struct_0_x4077_x5759_x22835584}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891779241}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID/Rmt Site]{lang="EN-US"}]{#struct_0_x4077_x5759_1884962525}

[[如果是静态]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_674139411}[或]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[，则为]{style="font-family:宋体"}[PW]{lang="EN-US"}[标识符]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[；如果是]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}[，则为远端]{style="font-family:宋体"}[Site]{lang="EN-US"}[标识符]{style="font-family:宋体"}[Rmt Site]{lang="EN-US"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_x4077_x5759_x1321381054}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_260473285}[的入标签和出标签]{style="font-family:宋体"}

[[Proto]{lang="EN-US"}]{#struct_0_x4077_x5759_1891320489}

[[建立]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x471312184}[使用的信令协议，取值包括]{style="font-family:宋体"}[LDP]{lang="EN-US"}[、]{style="font-family:宋体"}[Static]{lang="EN-US"}[和]{style="font-family:宋体"}[BGP]{lang="EN-US"}

[[Flag]{lang="EN-US"}]{#struct_0_x4077_x5759_x767562916}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x109245863}[属性标记，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M]{lang="EN-US"}]{#struct_0_x4077_x5759_x584632383}[：]{lang="EN-US" style="font-family:宋体"}[Main]{lang="EN-US"}[，主]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B]{lang="EN-US"}]{#struct_0_x4077_x5759_1891386025}[：]{lang="EN-US" style="font-family:宋体"}[Backup]{lang="EN-US"}[，备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1891451561}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1242242164}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x1746903258}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_2062495416}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671045165}[：表示该]{style="font-family:宋体"}[PW]{lang="EN-US"}[可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671110701}[：表示该]{style="font-family:宋体"}[PW]{lang="EN-US"}[不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Blocked]{lang="EN-US"}]{#struct_0_x4077_x5759_x1149268265}[：表示存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，该]{style="font-family:宋体"}[PW]{lang="EN-US"}[当前没有转发流量、起到备份作用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Defect]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671700526}[：表示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到该]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671766062}[：表示该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dup]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671831598}[：表示该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签与静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1891517097}[显示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_1892106921}

[Xconnect-group Name: ldp]{lang="EN-US"}

[ Connection Name: ldp]{lang="EN-US"}

[  Peer: 192.3.3.3        PW ID: 500]{lang="EN-US"}

[    Signaling Protocol  : LDP]{lang="EN-US"}

[    Link ID             : 0          PW State : Up]{lang="EN-US"}

[    In Label            : 1299       Out Label: 1299]{lang="EN-US"}

[    MTU                 : 1500]{lang="EN-US"}

[    PW Attributes       : Main]{lang="EN-US"}

[    VCCV CC             : -]{lang="EN-US"}

[    VCCV BFD            : -]{lang="EN-US"}

[    Tunnel Group ID     : 0x800000160000000]{lang="EN-US"}

[    Tunnel NHLFE IDs    : 1026]{lang="EN-US"}

[    Input statistics    : ]{lang="EN-US"}

[      Octets   : 10600]{lang="EN-US"}

[      Packets  : 100]{lang="EN-US"}

[      Errors   : 0]{lang="EN-US"}

[      Discards : 0 ]{lang="EN-US"}

[    Output statistics   : ]{lang="EN-US"}

[      Octets   : 12600]{lang="EN-US"}

[      Packets  : 100]{lang="EN-US"}

[      Errors   : 0]{lang="EN-US"}

[      Discards : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Xconnect-group Name: vpnb]{lang="EN-US"}

[ Connection of auto-discovery: Site 1]{lang="EN-US"}

[  Peer: 192.3.3.3        Remote Site: 2]{lang="EN-US"}

[    Signaling Protocol  : BGP]{lang="EN-US"}

[    Link ID             : 1          PW State : Up]{lang="EN-US"}

[    In Label            : 1036       Out Label: 1163]{lang="EN-US"}

[    MTU                 : 1500]{lang="EN-US"}

[    PW Attributes       : Main]{lang="EN-US"}

[    VCCV CC             : -]{lang="EN-US"}

[    VCCV BFD            : -]{lang="EN-US"}

[    Tunnel Group ID     : 0x800000160000000]{lang="EN-US"}

[    Tunnel NHLFE IDs    : 1026]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display l2vpn pw verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_1753039298}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x743094916}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2137478470}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1434627573}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_x66341119}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x379611673}[所属的交叉连接组名称]{style="font-family:宋体"}

[[Connection Name]{lang="EN-US"}]{#struct_0_x4077_x5759_1892172457}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_2143645533}[所属的交叉连接名称，采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[或静态方式建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[时，显示此信息]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_x4077_x5759_x1447503419}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x12279125}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x1976142317}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891582634}[标识符]{style="font-family:宋体"}

[[Signaling Protocol]{lang="EN-US"}]{#struct_0_x4077_x5759_x1230344493}

[[建立]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x328782172}[使用的信令协议，取值包括]{style="font-family:宋体"}[LDP]{lang="EN-US"}[、]{style="font-family:宋体"}[Static]{lang="EN-US"}[和]{style="font-family:宋体"}[BGP]{lang="EN-US"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x589567312}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1352442522}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[PW State]{lang="EN-US"}]{#struct_0_x4077_x5759_1891648170}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1890759564}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671569455}[：表示该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671634991}[：表示该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Blocked]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671700527}[：表示存在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的情况下，该]{style="font-family:宋体"}[PW]{lang="EN-US"}[当前没有转发流量、起到备份作用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Defect]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671766063}[：表示]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到该]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[存在缺陷]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671831599}[：表示该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Duplicate]{lang="EN-US"}]{#struct_0_x4077_x5759_x1671897135}[：表示该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签与静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同]{style="font-family:宋体"}

[[In Label]{lang="EN-US"}]{#struct_0_x4077_x5759_x679276392}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1083064969}[入标签]{style="font-family:宋体"}

[[Out Label]{lang="EN-US"}]{#struct_0_x4077_x5759_1891713706}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x2014250373}[出标签]{style="font-family:宋体"}

[[Wait to Restore Time]{lang="EN-US"}]{#struct_0_x4077_x5759_x791971680}

[[回切等待时间，单位为秒。如果配置不回切，则显示为]{style="font-family:宋体"}[Infinite]{lang="EN-US"}]{#struct_0_x4077_x5759_330281462}

[[只会在主备]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891779242}[同时存在的情况下显示，并且只在主]{style="font-family:宋体"}[PW]{lang="EN-US"}[上显示]{style="font-family:宋体"}

[[Remaining Time]{lang="EN-US"}]{#struct_0_x4077_x5759_1884765917}

[[回切等待的剩余时间，单位为秒。回切等待定时器启动时，才会显示该字段]{style="font-family:宋体"}]{#struct_0_x4077_x5759_302562841}

[[MTU]{lang="EN-US"}]{#struct_0_x4077_x5759_1605226615}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891320490}[协商后的最大传输单元]{style="font-family:宋体"}

[[PW ]{lang="EN-US"}[Attributes]{lang="EN-US"}]{#struct_0_x4077_x5759_x471770935}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_839647909}[的属性，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Main]{lang="EN-US"}]{#struct_0_x4077_x5759_677468248}[：主]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_x4077_x5759_1891386026}[：备份]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}

[[VCCV CC]{lang="EN-US"}]{#struct_0_x4077_x5759_1477460488}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_452539531}[的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_x4077_x5759_x1579106067}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_x4077_x5759_1891451562}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_x4077_x5759_x1242176628}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x1835896770}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891517098}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x1261974354}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[IP/UDP]{lang="EN-US"}[ Encapsulation]{lang="EN-US"}[ ]{lang="EN-US"}[(with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault Detection with Raw-BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x1827050055}[：]{style="font-family:
  宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:
  宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[Tunnel Group ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1892106922}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1752973762}[的隧道组]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Tunnel NHLFE IDs]{lang="EN-US"}]{#struct_0_x4077_x5759_x2128820706}

[[承载]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x883839357}[的隧道对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}[表项索引列表]{style="font-family:宋体"}

[[存在等价隧道时，一个]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1892172458}[会对应多个索引值]{style="font-family:宋体"}

[[如果不存在隧道，显示为]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_x4077_x5759_2143448925}

[[Connection of auto-discovery]{lang="EN-US"}]{#struct_0_x4077_x5759_506256563}

[[通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_1891582631}[方式建立的]{style="font-family:宋体"}[PW]{lang="EN-US"}

[[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x1230672173}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x232499570}[标识符]{style="font-family:宋体"}

[[Remote site]{lang="EN-US"}]{#struct_0_x4077_x5759_1891648167}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_1890300813}[标识符]{style="font-family:宋体"}

[[Input statistics]{lang="EN-US"}]{#struct_0_x4077_x5759_x4373670}

[[入方向的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x4570278}[转发统计信息，包括入方向接收的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、接收的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、接收的错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ Output statistics]{lang="EN-US"}]{#struct_0_x4077_x5759_977003403}

[[出方向的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1589519613}[转发统计信息，包括出方向发送的字节数（]{style="font-family:宋体"}[Octets]{lang="EN-US"}[）、发送的报文数（]{style="font-family:宋体"}[Packets]{lang="EN-US"}[）、发送的错误报文数（]{style="font-family:宋体"}[Errors]{lang="EN-US"}[）和丢弃的报文数（]{style="font-family:宋体"}[Discards]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x4504742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[statistics enable]{lang="NO-BOK"}**]{#struct_0_x4077_x5759_1369981280}

::: {#365063371 .myid}
[]{#_Toc404791530}[]{#struct_0_x4077_x5759_x2016323375}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn pw-class**

------------------------------------------------------------------------

[**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x464130899}[命令用来显示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1617502394}

[**[display l2vpn pw-class]{lang="EN-US"}**[ \[ *class-name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4077_x5759_1891713703}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2013922693}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_187576433}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2086012693}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1500479052}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_1850067299}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1626802997}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_129843097}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x147171290}

[*[class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_1891779239}[：显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4077_x5759_948287902}[：显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1884438236}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1991585257}[显示所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw-class ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1801544078}

[Total number of PW classes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[PW Class Name       PW Type              Control Word   VCCV CC        VCCV BFD]{lang="EN-US"}

[pw1                 Ethernet             Enabled        Control-Word   Raw-BFD]{lang="EN-US"}

[pw2                 VLAN                 Disabled       Router-Alert   BFD]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display l2vpn pw-class]{lang="EN-US"}]{#struct_0_x4077_x5759_1170755100}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x753604996}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1622119031}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1891320487}

[[Total number of PW classes]{lang="EN-US"}]{#struct_0_x4077_x5759_x471443256}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x764905699}[模板的总数]{style="font-family:宋体"}

[[PW Class Name]{lang="EN-US"}]{#struct_0_x4077_x5759_x352425802}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_2110761858}[模板的名称]{style="font-family:宋体"}

[[PW Type]{lang="EN-US"}]{#struct_0_x4077_x5759_580617197}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1891386023}[数据封装类型，取值包括]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Control Word]{lang="EN-US"}]{#struct_0_x4077_x5759_1477132808}

[[是否使能控制字功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_x4077_x5759_x395239906}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[VCCV CC]{lang="EN-US"}]{#struct_0_x4077_x5759_1610812432}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1599333655}[的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_x4077_x5759_1891451559}[：控制字]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_x4077_x5759_x1241717879}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[器]{style="font-family:宋体"}[告警标签]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_x4077_x5759_x240604356}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x1621737689}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1686775648}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_1891517095}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[IP/UDP]{lang="EN-US"}[ Encapsulation]{lang="EN-US"}[ ]{lang="EN-US"}[(with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Raw-BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_x1262695250}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_948615579}[显示所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw-class verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_948681115}

[PW Class Name : pw1]{lang="EN-US"}

[  PW Type     : Ethernet]{lang="EN-US"}

[  Control Word: Enabled]{lang="EN-US"}

[  VCCV CC     : Control-Word]{lang="EN-US"}

[  VCCV BFD    : Raw-BFD]{lang="EN-US"}

[  Sequencing  : Both]{lang="EN-US"}

[ ]{lang="EN-US"}

[PW Class Name : pw2]{lang="EN-US"}

[  PW Type     : VLAN]{lang="EN-US"}

[  Control Word: Disabled]{lang="EN-US"}

[  VCCV CC     : Router-Alert]{lang="EN-US"}

[  VCCV BFD    : BFD]{lang="EN-US"}

[  Sequencing  : -]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display l2vpn pw-class]{lang="EN-US"}]{#struct_0_x4077_x5759_x996734304}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x835516969}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_865007796}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_948484507}

[[PW Class Name]{lang="EN-US"}]{#struct_0_x4077_x5759_948550043}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x490564362}[模板的名称]{style="font-family:宋体"}

[[PW Type]{lang="EN-US"}]{#struct_0_x4077_x5759_948353435}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1920571552}[数据封装类型，取值包括]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Control Word]{lang="EN-US"}]{#struct_0_x4077_x5759_948418971}

[[是否使能控制字功能，取值包括]{style="font-family:宋体"}[Enabled]{lang="EN-US"}]{#struct_0_x4077_x5759_x1257872097}[和]{style="font-family:宋体"}[Disabled]{lang="EN-US"}

[[VCCV CC]{lang="EN-US"}]{#struct_0_x4077_x5759_948222363}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1127604066}[的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Control-Word]{lang="EN-US"}]{#struct_0_x4077_x5759_948287899}[：控制字类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router-Alert]{lang="EN-US"}]{#struct_0_x4077_x5759_949139867}[：]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由器告警标签类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TTL]{lang="EN-US"}]{#struct_0_x4077_x5759_x1240542721}[：]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型]{style="font-family:宋体"}

[[VCCV BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_949205403}

[[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1333348514}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_948615580}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:宋体"}[IP/UDP Encapsulation (with IP/UDP Headers)]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Raw-BFD]{lang="EN-US"}]{#struct_0_x4077_x5759_1764482146}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{lang="EN-US" style="font-family:宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{lang="EN-US" style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内的]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[头]{lang="EN-US" style="font-family:宋体"}

[[Sequencing]{lang="EN-US"}]{#struct_0_x4077_x5759_948681116}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_948484508}[的排序处理，取值为]{style="font-family:宋体"}[Both]{lang="EN-US"}[。取值为"]{style="font-family:宋体"}[-]{lang="EN-US"}["时表示未配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的排序处理，即不对]{style="font-family:宋体"}[PW]{lang="EN-US"}[上传输的报文进行排序]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1842543731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1126052201}

::: {#-1122099741 .myid}
[]{#_Toc404791531}[]{#struct_0_x4077_x5759_x623414908}[]{#_Toc300843396}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn service-instance**

------------------------------------------------------------------------

[**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2104348949}[命令用来显示以太网服务实例的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1892106919}

[**[display l2vpn service-instance ]{lang="EN-US"}**[\[ **interface**]{lang="EN-US"}*[ interface-type interface-number]{lang="EN-US"}*[ \[ **service-instance** *instance-id* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4077_x5759_1753563589}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x582760796}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x544520941}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x256110286}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1234891262}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_2033295230}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_366788944}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_1354242464}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1892172455}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_2143776605}[：显示指定二层以太网接口或二层聚合接口上的以太网服务实例信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果没有指定本参数，则显示所有二层以太网接口和二层聚合接口上的以太网服务实例信息。]{style="font-family:
宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_909802388}[：显示指定以太网服务实例的信息。]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。如果指定了]{style="font-family:宋体"}**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*[参数，没有指定本参数，则显示指定二层以太网接口或二层聚合接口上所有以太网服务实例的信息。]{style="font-family:
宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1950607252}[：显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x441470887}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x2138435242}[显示所有以太网服务实例的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance]{lang="EN-US"}]{#struct_0_x4077_x5759_1891582632}

[Total number of service-instances: 5, 5 up, 0 down]{lang="EN-US"}

[Total number of ACs: 4, 4 up, 0 down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                SrvID Owner                           LinkID State Type]{lang="EN-US"}

[GE1/0/3                  1     vpws1                           1      Up    VPWS]{lang="EN-US"}

[GE1/0/3                  2     vpws2                           1      Up    VPWS]{lang="EN-US"}

[GE1/0/3                  3     vpws3                           1      Up    VPWS]{lang="EN-US"}

[GE1/0/3                  4     vpws4                           1      Up    VPWS]{lang="EN-US"}

[GE1/0/3                  5                                            Up]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display l2vpn service-instance]{lang="EN-US"}]{#struct_0_x4077_x5759_x1230737709}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x751573092}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x399066410}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1253117558}

[[Total number of service-instances]{lang="EN-US"}]{#struct_0_x4077_x5759_1899033786}

[[以太网服务实例的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x4077_x5759_x616891692}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的以太网服务实例数目]{style="font-family:宋体"}

[[Total number of ACs]{lang="EN-US"}]{#struct_0_x4077_x5759_1891648168}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_1890235277}[的总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的]{style="font-family:宋体"}[AC]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4077_x5759_x1270171967}

[[二层以太网接口或二层聚合接口名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x634384513}

[[SrvID ]{lang="EN-US"}]{#struct_0_x4077_x5759_1337724900}

[[以太网服务实例的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4077_x5759_1891713704}

[[Owner]{lang="EN-US"}]{#struct_0_x4077_x5759_x2014381445}

[[交叉连接组名称，如果以太网服务实例尚未关联交叉连接，则本字段显示为空]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1964402840}

[[LinkID]{lang="EN-US"}]{#struct_0_x4077_x5759_1262459513}

[[以太网服务实例对应]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_x1626463478}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_1891779240}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_1884896989}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x4077_x5759_740122536}

[[以太网服务实例所属的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x1251192529}[类型，取值包括]{style="font-family:宋体"}[VSI]{lang="EN-US"}[和]{style="font-family:宋体"}[VPWS]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x275043122}[显示二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上所有以太网服务实例的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn service-instance interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_1891320488}

[Interface: GE1/0/1]{lang="EN-US"}

[  Service Instance: 1]{lang="EN-US"}

[    Encapsulation : s-vid 1 to 16]{lang="EN-US"}

[    Xconnect-group: vpws1]{lang="EN-US"}

[    Connection    : actopw]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 2]{lang="EN-US"}

[    Encapsulation : s-vid 1001 to 1002 1015 to 1016]{lang="EN-US"}

[                    only-tagged]{lang="EN-US"}

[    Xconnect-group: vpws2]{lang="EN-US"}

[    Connection    : pwtopw]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[  Service Instance: 3]{lang="EN-US"}

[    Encapsulation : s-vid 2000]{lang="EN-US"}

[                    c-vid 1001 to 1002 1015 to 1016]{lang="EN-US"}

[    Xconnect-group: vpws3]{lang="EN-US"}

[    AD Connection : Site 1, Remote Site 2]{lang="EN-US"}

[    Link ID       : 1]{lang="EN-US"}

[    State         : Up]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[display l2vpn service-instance verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_x471246648}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x725399524}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x770720389}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1891386024}

[[Interface]{lang="EN-US"}]{#struct_0_x4077_x5759_1477591560}

[[二层以太网接口或二层聚合接口]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x343162941}

[[Service Instance]{lang="EN-US"}]{#struct_0_x4077_x5759_x1142282351}

[[以太网服务实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4077_x5759_2065193724}

[[Encapsulation]{lang="EN-US"}]{#struct_0_x4077_x5759_1891451560}

[[以太网服务实例的报文匹配规则，如果没有配置报文匹配规则，则显示为空]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1242307700}

[[Xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_x1017860960}

[[以太网服务实例所属的交叉连接组的名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x578048331}

[[Connection]{lang="EN-US"}]{#struct_0_x4077_x5759_x1868473147}

[[与以太网服务实例关联的交叉连接的名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1891517096}

[[AD Connection]{lang="EN-US"}]{#struct_0_x4077_x5759_x1262629714}

[[与以太网服务实例关联的自动发现交叉连接，由本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_1042809757}[标识符（]{style="font-family:宋体"}[Site]{lang="EN-US"}[）和远端]{style="font-family:宋体"}[Site]{lang="EN-US"}[标识符（]{style="font-family:宋体"}[Remote Site]{lang="EN-US"}[）来标识]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x95790012}

[[以太网服务实例对应]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_x268635412}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_1892106920}

[[以太网服务实例的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_1753104834}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1047417478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service-instance]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1049494456}

::: {#1470473848 .myid}
[]{#_Toc404791532}[]{#struct_0_x4077_x5759_1954173413}[]{#_Toc300843398}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- display l2vpn xconnect-group**

------------------------------------------------------------------------

[**[display l2vpn ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2112305374}**[xconnect-group]{lang="IT"}**[命令用来显示交叉连接组的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1784359907}

[**[display]{lang="EN-US"}**[ **l2vpn** ]{lang="EN-US"}]{#struct_0_x4077_x5759_113959371}**[xconnect-group ]{lang="IT"}**[\[ **name** ]{lang="EN-US"}*[group-name]{lang="IT"}***[ ]{lang="IT"}**[\] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1892172456}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_2143579997}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1062121246}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_2067863902}

[[network-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_x1030511596}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x692121405}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4077_x5759_x337268474}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1307150018}

[**[name]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_x4077_x5759_x837300720}*[group-name]{lang="IT"}*[：显示指定交叉连接组的信息。]{style="font-family:宋体"}*[group-name]{lang="IT"}*[表示交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有交叉连接组的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4077_x5759_x926686668}[：显示交叉连接组的详细信息。如果不指定本参数，则显示交叉连接组的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_262215782}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x943803808}[显示所有交叉连接组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_264609079}

[Total number of cross-connections: 3, 0 up, 3 down, 0 admin down]{lang="EN-US"}

[ ]{lang="EN-US"}

[Xconnect-group Name             Connection ID   MTU    State]{lang="EN-US"}

[abc                             0               1500   Down]{lang="EN-US"}

[vpn1                            2               1500   Down]{lang="EN-US"}

[vpn2                            1               1500   Down]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[display l2vpn xconnect-group]{lang="EN-US"}]{#struct_0_x4077_x5759_x1562560677}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x728557412}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837235184}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x536896798}

[[Total number of cross-connections]{lang="EN-US"}]{#struct_0_x4077_x5759_x1209927191}

[[所有交叉连接组或指定交叉连接组下交叉连接的总数，以及处于]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x4077_x5759_822233354}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[、]{style="font-family:宋体"}[admin down]{lang="EN-US"}[状态的交叉连接数目]{style="font-family:宋体"}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_471313311}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x772697616}

[[Connection ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x837169648}

[[交叉连接索引]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x972090807}

[[MTU]{lang="EN-US"}]{#struct_0_x4077_x5759_x1044708965}

[[交叉连接的最大传输单元]{style="font-family:宋体"}]{#struct_0_x4077_x5759_413161363}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x903318148}

[[交叉连接组的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x837104112}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_x2105405531}[：]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x4077_x5759_x1405871185}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Admin down]{lang="EN-US"}]{#struct_0_x4077_x5759_1973705961}[：通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令手工关闭]{lang="EN-US" style="font-family:宋体"}[的交叉连接组]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1272746621}[显示所有交叉连接组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn xconnect-group verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_x837562864}

[Xconnect-group Name: ldp]{lang="EN-US"}

[ Description   : ldp-pw]{lang="EN-US"}

[ Connection Name   : ldp]{lang="EN-US"}

[  Connection ID    : 1]{lang="EN-US"}

[  State            : Down]{lang="EN-US"}

[  MTU              : 1500]{lang="EN-US"}

[  Interworking IPv4: Enabled]{lang="EN-US"}

[  LDP PWs:]{lang="EN-US"}

[    Peer            PW ID            Link ID    State]{lang="EN-US"}

[    192.3.3.3       200              1          Down]{lang="EN-US"}

[  ACs:]{lang="EN-US"}

[    AC                               Link ID    State]{lang="EN-US"}

[    Vlan10                           0          Up]{lang="EN-US"}

[ ]{lang="EN-US"}

[Xconnect-group Name: vpnb]{lang="EN-US"}

[ Connection of auto-discovery: Site 1, Remote Site 2]{lang="EN-US"}

[  Connection ID    : 0]{lang="EN-US"}

[  State            : Up]{lang="EN-US"}

[  MTU              : 1500]{lang="EN-US"}

[  BGP PWs:]{lang="EN-US"}

[    Peer            Remote Site      Link ID    State]{lang="EN-US"}

[    192.3.3.3       2                1          Up]{lang="EN-US"}

[  ACs:]{lang="EN-US"}

[    AC                               Link ID    State]{lang="EN-US"}

[    GE1/0/4                          0          Up]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[display l2vpn xconnect-group verbose]{lang="EN-US"}]{#struct_0_x4077_x5759_945015724}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x726358180}[[字段]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837497328}

[[描述]{style="font-family:黑体"}]{#struct_0_x4077_x5759_264406212}

[[Xconnect-group Name]{lang="EN-US"}]{#struct_0_x4077_x5759_182930972}

[[交叉连接组名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2074587784}

[[Description]{lang="EN-US"}]{#struct_0_x4077_x5759_729972895}

[[交叉连接组的描述信息，如果不配置，则此行不显示]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x837431792}

[[Connection Name]{lang="EN-US"}]{#struct_0_x4077_x5759_641297919}

[[交叉连接名称]{style="font-family:宋体"}]{#struct_0_x4077_x5759_710154363}

[[Connection of auto-discovery]{lang="EN-US"}]{#struct_0_x4077_x5759_1200723241}

[[自动发现交叉连接]{style="font-family:宋体"}]{#struct_0_x4077_x5759_499822322}

[[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_733275677}

[[本端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x837366256}[标识符]{style="font-family:宋体"}

[[Remote site]{lang="EN-US"}]{#struct_0_x4077_x5759_1002830081}

[[远端]{style="font-family:宋体"}[Site]{lang="EN-US"}]{#struct_0_x4077_x5759_x283958550}[标识符]{style="font-family:宋体"}

[[Connection ID]{lang="EN-US"}]{#struct_0_x4077_x5759_976920692}

[[交叉连接索引]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1463997131}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x836776432}

[[交叉连接组的状态，取值包括]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1372191107}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x4077_x5759_x585449395}[：]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x4077_x5759_x1036577611}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_x4077_x5759_x836710896}[：通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令手工关闭]{lang="EN-US" style="font-family:宋体"}[交叉连接组]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_x4077_x5759_251847359}

[[交叉连接的最大传输单元]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x645358771}

[[Interworking IPv4]{lang="EN-US"}]{#struct_0_x4077_x5759_x1047480867}

[[是否使能]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x4077_x5759_x837300719}[类型的异构互连功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4077_x5759_x926227917}[：表示使能该功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4077_x5759_x1654092774}[：表示未使能该功能]{lang="EN-US" style="font-family:宋体"}

[[本字段的支持情况与设备型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x4077_x5759_2008374220}

[[LDP PWs]{lang="EN-US"}]{#struct_0_x4077_x5759_x1510741708}

[[LDP PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x837235183}[相关信息]{style="font-family:宋体"}

[[Static PWs]{lang="EN-US"}]{#struct_0_x4077_x5759_x537224478}

[[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1518203009}[相关信息]{style="font-family:宋体"}

[[BGP PWs]{lang="EN-US"}]{#struct_0_x4077_x5759_x837169647}

[[BGP PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x971763127}[相关信息]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_x4077_x5759_1367570239}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x542551256}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PW ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x837104111}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x2105339995}[标识符]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x718728264}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1491761049}[在交叉连接内的链路标识符]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x837562863}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_945343404}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[、]{style="font-family:宋体"}[Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[和]{style="font-family:宋体"}[Defect]{lang="EN-US"}

[[ACs]{lang="EN-US"}]{#struct_0_x4077_x5759_x1370722363}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_x837497327}[相关信息]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_264864964}

[[接入电路，取值有如下两种：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1806717197}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层接口名称：如]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1599962797}[GE1/0/4]{lang="EN-US"}[。在交叉连接视图下关联三层接口时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[二层接口名称和以太网服务实例：如]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x837431791}[GE1/0/3 srv1]{lang="EN-US"}[。在交叉连接视图下关联以太网服务实例时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x4077_x5759_641494527}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_228476441}[在交叉连接组内的链路]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_x4077_x5759_x837366255}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_1002633473}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_517320454}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[xconnect-group]{lang="EN-US"}**]{#struct_0_x4077_x5759_1502017197}

::: {#-900899430 .myid}
[]{#_Toc404791533}[]{#struct_0_x4077_x5759_1155891635}[]{#_Toc288911611}[]{#_Toc203551099}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- encapsulation**

------------------------------------------------------------------------

[**[encapsulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_x836776431}[命令用来配置以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_1372387715}[命令用来删除以太网服务实例的报文匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1769309134}

[**[encapsulation]{lang="EN-US"}**[ **c-vid** { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x4077_x5759_x401574427}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** { *vlan-id* \| *vlan-id-list* } \[ **only-tagged** \]]{lang="EN-US"}]{#struct_0_x4077_x5759_1516487597}

[**[encapsulation]{lang="EN-US"}**[ **s-vid** *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_x4077_x5759_x1715046076}

[**[encapsulation]{lang="EN-US"}**[ { **default** \| **tagged** \| **untagged** }]{lang="EN-US"}]{#struct_0_x4077_x5759_793667807}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_1918082884}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x836710895}

[[未配置任何报文匹配规则。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_251781823}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1819188240}

[[以太网服务实例视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x99702302}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1301530482}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x889183409}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1212796876}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_497806849}

[**[c-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x4077_x5759_x837300722}[：匹配内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Customer VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_x926817740}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x4077_x5759_1020038461}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ to *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ { *vlan-id* \| *vlan-id-list* }]{lang="EN-US"}]{#struct_0_x4077_x5759_x1242507074}[：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签（]{style="font-family:宋体"}[Service VLAN ID]{lang="EN-US"}[）为指定值的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_938334779}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x4077_x5759_353956727}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[only-tagged]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1333154003}[：表示只匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。当匹配的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，如果未指定本关键字，则会同时匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文和未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文；如果指定了本参数，则只匹配所携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为缺省]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s-vid]{lang="EN-US"}**[ *vlan-id* **c-vid** { *vlan-id-list* \| **all** }]{lang="EN-US"}]{#struct_0_x4077_x5759_x1555409269}[：匹配指定外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签和内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_x317710431}[表示]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vlan-id-list]{lang="EN-US"}*]{#struct_0_x4077_x5759_x837235186}[为]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示一个或多个]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。表示方式为]{lang="EN-US" style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-8\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[al]{lang="EN-US"}**]{#struct_0_x4077_x5759_x537027870}**[l]{lang="EN-US"}**[表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_x4077_x5759_x789740580}[：表示缺省的报文匹配规则。]{style="font-family:宋体"}

[**[tagged]{lang="EN-US"}**]{#struct_0_x4077_x5759_444220692}[：表示匹配携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[untagged]{lang="EN-US"}**]{#struct_0_x4077_x5759_484930421}[：表示匹配未携带]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的报文。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x369337273}

[[当同一个接口下配置的不同以太网服务实例的报文匹配规则出现重叠时，如何匹配报文与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1560456921}

[[同一个以太网接口下可以创建多个服务实例，但是最多只能有一个服务实例采用缺省的报文匹配规则（]{style="font-family:宋体"}**[encapsulation default]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1401705540}[）。如果接口下同时存在一个采用缺省报文匹配规则的服务实例和多个采用其他报文匹配规则的服务实例，则没有与任何其他报文匹配规则匹配的报文将匹配缺省报文匹配规则；如果接口下只存在一个采用缺省报文匹配规则的服务实例，则该接口上的所有报文都匹配缺省报文匹配规则。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x837169650}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个以太网服务实例视图下，不能重复执行本命令。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x971566518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除以太网服务实例下的报文匹配规则后，会自动取消以太网服务实例]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1362476547}[与]{style="font-family:宋体"}[交叉连接的关联。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[内层]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x711455002}[VLAN]{lang="EN-US"}[标签和外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签的介绍请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[QinQ]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_488190061}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1385930459}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[上配置如下报文匹配规则：匹配外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[111]{lang="EN-US"}[，内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[标签为]{style="font-family:宋体"}[20]{lang="EN-US"}[、]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[40]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1870646033}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\] encapsulation s-vid 111 c-vid 20 30 to 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837104114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2105012315}
:::

::: {#-2059163527 .myid}
[]{#_Toc404791534}[]{#struct_0_x4077_x5759_949139873}[]{#_Toc385403453}[]{#_Toc379982564}[]{#_Toc374974306}[]{#_Toc371347449}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- idle-code**

------------------------------------------------------------------------

[**[idle-code]{lang="EN-US"}**]{#struct_0_x4077_x5759_715772419}[命令用来配置出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[检测到特定电路仿真接口的电路仿真分组丢失时，向]{style="font-family:宋体"}[TDM]{lang="EN-US"}[线路发送的空闲码。]{style="font-family:宋体"}

[**[undo idle-code]{lang="EN-US"}**]{#struct_0_x4077_x5759_1203320915}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_795091982}

[**[idle-code]{lang="EN-US"}**[ *bit-pattern*]{lang="EN-US"}]{#struct_0_x4077_x5759_873479347}

[**[undo idle-code]{lang="EN-US"}**]{#struct_0_x4077_x5759_x415653066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_949205409}

[[出口]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_1333348520}[检测到特定电路仿真接口的电路仿真分组丢失时，向]{style="font-family:宋体"}[TDM]{lang="EN-US"}[线路发送的空闲码为]{style="font-family:宋体"}[FF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x33637864}

[[电路仿真类视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1865709810}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1910402625}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1701001441}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_114968420}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1098157784}

[*[bit-pattern]{lang="EN-US"}*]{#struct_0_x4077_x5759_x706822105}[：空闲码。十六进制形式，取值范围为]{style="font-family:宋体"}[00]{lang="EN-US"}[～]{style="font-family:宋体"}[FF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_791742639}

[[出口]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_1080808424}[以恒定的速率向]{style="font-family:宋体"}[TDM]{lang="EN-US"}[线路发送]{style="font-family:宋体"}[TDM]{lang="EN-US"}[帧。当出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[检测到电路仿真分组丢失时，每个丢失的电路仿真分组的净载荷必须用等量的替代数据来代替。出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[使用配置的空闲码作为替代数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_948615586}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1764482148}[配置电路仿真类]{style="font-family:宋体"}[satop]{lang="EN-US"}[的电路仿真分组丢失时，向]{style="font-family:宋体"}[TDM]{lang="EN-US"}[线路发送的空闲码为]{style="font-family:宋体"}[C2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_2023373945}

[\[Sysname\] cem-class satop]{lang="EN-US"}

[\[Sysname-cem-satop\] idle-code c2]{lang="EN-US"}
:::

::: {#1425876805 .myid}
[]{#_Toc404791535}[]{#struct_0_x4077_x5759_569251578}[]{#_Toc387667759}[]{#_Toc383502069}[]{#_Toc326826700}[]{#_Toc325029185}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- interface circuit-emulation**

------------------------------------------------------------------------

[**[interface ]{lang="EN-US"}[circuit-emulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_409380310}[命令用来进入]{style="font-family:宋体"}[电路仿真接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1868962703}

[**[interface circuit-emulation]{lang="EN-US"}**[ { *interface-number*:0 \| *interface-number*:*set-number* }]{lang="EN-US"}]{#struct_0_x4077_x5759_x943887170}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1441450696}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x987413671}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_569317114}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1119235350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x545540511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1851059923}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_x2058706622}[：]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口或]{style="font-family:宋体"}[CT1/PRI]{lang="EN-US"}[接口的编号。详细信息请参见"接口管理"中的"]{style="font-family:宋体"}[WAN]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[*[set-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_1038625402}[：]{style="font-family:宋体"}[该接口上时隙捆绑形成的电路仿真组编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。详细信息请参见"接口管理"中的"]{style="font-family:宋体"}[WAN]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[]{#struct_0_x4077_x5759_349228498}[[【使用指导】]{style="font-family:黑体"}]{#_Toc387667760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface circuit-emulation]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[:0]{lang="EN-US"}]{#struct_0_x4077_x5759_2114527837}[命令用于在]{lang="EN-US" style="font-family:宋体"}[SAToP]{lang="EN-US"}[模式时]{style="font-family:宋体"}[进入电路仿真接口视图。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface circuit-emulation]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[:*set-number*]{lang="EN-US"}]{#struct_0_x4077_x5759_x2006880929}[命令]{style="font-family:宋体"}[用于在]{lang="EN-US" style="font-family:宋体"}[CESoPSN]{lang="EN-US"}[模式时]{style="font-family:宋体"}[进入电路仿真接口视图。]{lang="EN-US" style="font-family:宋体"}

[]{#struct_0_x4077_x5759_165442766}[[【举例】]{style="font-family:黑体"}]{#_Toc387667761}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1237584819}[进入电路仿真接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x1228614695}

[\[Sysname\] interface circuit-emulation2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\]]{lang="EN-US"}
:::

::::: {#-2011087879 .myid}
[]{#_Toc404791536}[]{#struct_0_x4077_x5759_x2028634420}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- interworking**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image001.png){#图片 23 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_x839991848}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_1980657241}
:::

**[ ]{lang="EN-US"}**

[**[interworking]{lang="EN-US"}**]{#struct_0_x4077_x5759_1504236797}[命令用来使能交叉连接的异构互连功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[interworking]{lang="EN-US"}**]{#struct_0_x4077_x5759_x918811302}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1675189894}

[**[interworking ipv4]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837562866}

[**[undo interworking]{lang="EN-US"}**]{#struct_0_x4077_x5759_945146796}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x801762826}

[[交叉连接不支持异构互连功能。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1969158063}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x527858676}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x523786574}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1263081541}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_654166123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1995269690}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837497330}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4077_x5759_264930499}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的异构互连。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1804035150}

[[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_x709203212}[的链路类型多种多样，如]{style="font-family:宋体"}[ATM]{lang="EN-US"}[、]{style="font-family:宋体"}[FR]{lang="EN-US"}[、]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[、]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[、]{style="font-family:宋体"}[PPP]{lang="EN-US"}[等。执行]{style="font-family:宋体"}**[interworking]{lang="EN-US"}**[命令使能交叉连接的异构互连功能后，交叉连接可以通过]{style="font-family:宋体"}[PW]{lang="EN-US"}[连接不同链路类型的]{style="font-family:宋体"}[AC]{lang="EN-US"}[。例如，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的异构互连方式中，]{style="font-family:宋体"}[PE]{lang="EN-US"}[从所连接的]{style="font-family:宋体"}[AC]{lang="EN-US"}[接收到报文后，从中提取]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文，通过]{style="font-family:宋体"}[PW]{lang="EN-US"}[发送给远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[，远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[根据它连接的]{style="font-family:宋体"}[AC]{lang="EN-US"}[的链路类型对接收到的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文进行封装，并把封装后的报文发送到]{style="font-family:宋体"}[AC]{lang="EN-US"}[链路，从而屏蔽两端]{style="font-family:宋体"}[AC]{lang="EN-US"}[的链路类型差异，实现不同链路类型]{style="font-family:宋体"}[AC]{lang="EN-US"}[的互连。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1344439259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x4077_x5759_18860846}[IPv4]{lang="EN-US"}[类型的异构互连，如果从]{style="font-family:宋体"}[AC]{lang="EN-US"}[上接收到的报文不是]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文，则丢弃该报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{lang="EN-US" style="font-family:宋体"}**[interworking]{lang="EN-US"}**]{#struct_0_x4077_x5759_1603025441}[命令，则对]{lang="EN-US" style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型的配置不会生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1606576884}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x837431794}[使能交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内交叉连接]{style="font-family:宋体"}[ac2pw]{lang="EN-US"}[的异构互连功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_641691135}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection ac2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-ac2pw\] interworking ipv4]{lang="EN-US"}
:::::

::: {#-819113915 .myid}
[]{#_Toc404791537}[]{#struct_0_x4077_x5759_948484514}[]{#_Toc385403455}[]{#_Toc379982566}[]{#_Toc374974307}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- jitter-buffer**

------------------------------------------------------------------------

[**[jitter-buffer]{lang="EN-US"}**]{#struct_0_x4077_x5759_1067572493}[命令用来配置电路仿真类的]{style="font-family:宋体"}[Jitter-buffer]{lang="EN-US"}[的大小。]{style="font-family:宋体"}

[**[undo jitter-buffer]{lang="EN-US"}**]{#struct_0_x4077_x5759_577977448}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1293355251}

[**[jitter-buffer]{lang="EN-US"}**[ *size-value*]{lang="EN-US"}]{#struct_0_x4077_x5759_371798100}

[**[undo jitter-buffer]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1006860544}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_948550050}

[[与引用此电路仿真类的电路仿真接口的电路类型有关，不区分]{style="font-family:宋体"}[SAToP]{lang="EN-US"}]{#struct_0_x4077_x5759_1465750775}[或]{style="font-family:宋体"}[CESoPSN]{lang="EN-US"}[。具体取值如下：]{style="font-family:宋体"}

[[E1]{lang="EN-US"}]{#struct_0_x4077_x5759_x1543548046}[---]{style="font-family:宋体"}[16ms]{lang="EN-US"}[、]{style="font-family:宋体"}[T1]{lang="EN-US"}[---]{style="font-family:宋体"}[16ms]{lang="EN-US"}[、]{style="font-family:宋体"}[E3]{lang="EN-US"}[---]{style="font-family:宋体"}[5ms]{lang="EN-US"}[、]{style="font-family:宋体"}[T3]{lang="EN-US"}[---]{style="font-family:宋体"}[5ms]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1167190187}

[[电路仿真类视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1918129061}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_77346117}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_581996535}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1069961448}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1550203068}

[*[size-value]{lang="EN-US"}*]{#struct_0_x4077_x5759_1085510521}[：]{style="font-family:宋体"}[Jitter-buffer]{lang="EN-US"}[的大小，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_948353442}

[[由于出口]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_1565091681}[必须以恒定速率向]{style="font-family:宋体"}[TDM]{lang="EN-US"}[电路发送数据，而]{style="font-family:宋体"}[PSN]{lang="EN-US"}[网络中分组的时延抖动一般较大。因此，需要通过出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[上的]{style="font-family:宋体"}[Jitter-buffer]{lang="EN-US"}[缓存]{style="font-family:宋体"}[TDM]{lang="EN-US"}[电路仿真分组的净载荷，从而平滑]{style="font-family:宋体"}[PSN]{lang="EN-US"}[网络传送导致的时延抖动。缓存后再以恒定速率向]{style="font-family:宋体"}[TDM]{lang="EN-US"}[接口发送。]{style="font-family:宋体"}

[[Jitter buffer]{lang="EN-US"}]{#struct_0_x4077_x5759_x1008809890}[越小，抗抖动能力越弱；]{style="font-family:宋体"}[Jitter buffer]{lang="EN-US"}[越大，抗抖动能力越强，但在数据流重建的时候会引入较大的传送延时。过大或过小的]{style="font-family:宋体"}[Jitter buffer]{lang="EN-US"}[都不利于业务的高质量传输，请根据实际情况合理选择]{style="font-family:宋体"}[Jitter buffer]{lang="EN-US"}[的大小。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_539533087}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1554167853}[配置电路仿真类]{style="font-family:宋体"}[satop]{lang="EN-US"}[的]{style="font-family:宋体"}[Jitter-buffer]{lang="EN-US"}[大小为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_176717302}

[\[Sysname\] cem-class satop]{lang="EN-US"}

[\[Sysname-cem-satop\] jitter-buffer 100]{lang="EN-US"}
:::

::: {#2070950537 .myid}
[]{#_Toc404791538}[]{#struct_0_x4077_x5759_1267495855}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1972921782}[命令用来使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1097501944}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_811715667}

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_2137917448}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837366258}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1002436865}

[[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x650244966}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1741611148}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_510151867}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2639834}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x386555811}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1691978707}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_602190509}

[[只有使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x836776434}[功能后，才能进行]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1372060035}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x168545016}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_549677101}

[\[Sysname\] l2vpn enable]{lang="EN-US"}
:::

::::: {#-1203155056 .myid}
[]{#_Toc404791539}[]{#struct_0_x4077_x5759_2126317774}[]{#_Toc391555303}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- l2vpn reflector**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image003.png){#图片 2 width="60" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_516469278}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_x1500435268}
:::

[ ]{lang="EN-US"}

[**[l2vpn reflector]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2026277025}[命令用来使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的报文反射功能。]{style="font-family:宋体"}

[**[undo l2vpn reflector]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1038146419}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_x246269685}

[**[l2vpn reflector interface ]{lang="EN-US"}**[{ *interface-name* \| *interface-type* *inteface-number* } \[ **service-instance** *instance-id* \] **ip** *ip-address* \[ **mac** *mac-address* \] \[ **source-port** *source-port* \] \[ **destination-port** *destination-port* \]]{lang="EN-US"}]{#struct_0_x4077_x5759_x517002729}

[**[undo]{lang="EN-US"}**[ **l2vpn** **reflector** **interface** { *interface-name* \| *interface-type* *inteface-number* } \[ **service-instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_x4077_x5759_1497688196}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_1895740314}

[[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x1130342323}[的报文反射功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_1316376988}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1116082570}

[[【缺省用户角色】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_x1594366133}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1812353626}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1567657072}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_x1127395589}

[**[interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_x877400968}**[：]{style="font-family:宋体"}**[指定]{style="font-family:宋体"}[AC]{lang="EN-US"}[侧接口。]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_1185546885}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[侧接口的名称。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *inteface-number*]{lang="EN-US"}]{#struct_0_x4077_x5759_x1551802355}[：]{style="font-family:宋体"}[AC]{lang="EN-US"}[侧接口类型和接口编号。]{style="font-family:宋体"}

[**[service-instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_883398274}[：指定以太网服务实例，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为以太网服务实例编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_1250367749}[：指定待反射报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为点分十进制格式，不能为本设备上]{style="font-family:宋体"}[CE]{lang="EN-US"}[侧接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x683412237}[：指定待反射报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，如果不指定本参数，则表示]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[或者]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *inteface-number*]{lang="EN-US"}[指定的接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。不支持组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和全]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[source-port]{lang="EN-US"}***[ source-port]{lang="EN-US"}*]{#struct_0_x4077_x5759_1084840886}[：指定待反射报文的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[源端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省为]{style="font-family:宋体"}[49184]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}***[ destination-port]{lang="EN-US"}*]{#struct_0_x4077_x5759_916529729}[：指定待反射报文的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[目的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_1999413722}

[[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x826672550}[的报文反射功能后，可在设备上生成对应的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代答表项，用于回应对指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求，并反射对指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的检测报文。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_437643987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个以太网服务实例或三层接口下只能配置一条报文反射和]{style="font-family:宋体"}]{#struct_0_x4077_x5759_33228568}[ARP]{lang="EN-US"}[代答表项，同一接口下的多个以太网服务实例下可配置多条不同的报文反射和]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代答表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一以太网服务实例或三层接口下可多次执行本命令，仅最后一次配置生效。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_629881507}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每台设备最多可配置]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x127821312}[8]{lang="EN-US"}[条报文反射和]{style="font-family:宋体"}[ARP]{lang="EN-US"}[代答表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[待反射报文的]{style="font-family:宋体"}]{#struct_0_x4077_x5759_562132598}[IP]{lang="EN-US"}[地址需本地唯一，即每个以太网服务实例或三层接口下配置的反射报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令关联以太网服务实例前，必须通过]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x649554212}**[encapsulation]{lang="EN-US"}**[命令为指定的以太网服务实例配置报文匹配规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1289666879}[L2VPN]{lang="EN-US"}[的报文反射功能时，需同时在]{style="font-family:宋体"}[AC]{lang="EN-US"}[绑定的交叉连接组下开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪抑制功能]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_898616829}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1172247479}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[的报文反射功能：]{style="font-family:宋体"}[AC]{lang="EN-US"}[侧接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，反射报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4077_x5759_563552668}

[[\[Sysname\] l2vpn reflector interface gigabitethernet 1/0/1 ip 1.0.0.1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4077_x5759_1352932157}

[[【相关命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x4077_x5759_1274100409}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn forwarding]{lang="EN-US"}**]{#struct_0_x4077_x5759_1723098783}
:::::

::::: {#-1924536592 .myid}
[]{#_Toc404791540}[]{#struct_0_x4077_x5759_x1394236243}[]{#_Toc302467222}[]{#_Toc360712276}[]{#_Toc361661986}[]{#_Toc360712277}[]{#_Toc361661987}[]{#_Toc360712278}[]{#_Toc361661988}[]{#_Toc360712279}[]{#_Toc361661989}[]{#_Toc360712280}[]{#_Toc361661990}[]{#_Toc360712281}[]{#_Toc361661991}[]{#_Toc360712282}[]{#_Toc361661992}[]{#_Toc360712283}[]{#_Toc361661993}[]{#_Toc360712284}[]{#_Toc361661994}[]{#_Toc360712285}[]{#_Toc361661995}[]{#_Toc360712286}[]{#_Toc361661996}[]{#_Toc360712287}[]{#_Toc361661997}[]{#_Toc360712288}[]{#_Toc361661998}[]{#_Toc360712289}[]{#_Toc361661999}[]{#_Toc360712290}[]{#_Toc361662000}[]{#_Toc360712291}[]{#_Toc361662001}[]{#_Toc360712292}[]{#_Toc361662002}[]{#_Hlt24806852}[]{#_Toc360712293}[]{#_Toc361662003}[]{#_Toc360712294}[]{#_Toc361662004}[]{#_Toc360712295}[]{#_Toc361662005}[]{#_Toc360712296}[]{#_Toc361662006}[]{#_Toc360712297}[]{#_Toc361662007}[]{#_Toc360712298}[]{#_Toc361662008}[]{#_Toc360712299}[]{#_Toc361662009}[]{#_Toc360712300}[]{#_Toc361662010}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- l2vpn switchover**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](MPLS%20L2VPN命令.files/image003.png){width="60" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_x507553476}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_1350728876}
:::

**[ ]{lang="EN-US"}**

[**[l2vpn switchover]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1336489585}[命令用来将指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的流量手工倒换到它的冗余备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_129431336}

[**[l2vpn switchover peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_x4077_x5759_x837169649}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x972156343}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1920025190}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x999811845}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_291549706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_815951297}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_192107804}

[**[peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_594794684}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pw-id]{lang="EN-US"}**[ *pw-id*]{lang="EN-US"}]{#struct_0_x4077_x5759_x837104113}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2105471067}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_410822029}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识了一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[。如果该]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在对应的可用主]{style="font-family:宋体"}[PW]{lang="EN-US"}[或备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则执行本命令后，通过该]{style="font-family:宋体"}[PW]{lang="EN-US"}[转发的流量将倒换到另一条可用的主]{style="font-family:宋体"}[PW]{lang="EN-US"}[或备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[上转发；如果不存在对应的可用主]{style="font-family:宋体"}[PW]{lang="EN-US"}[和备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则不进行流量倒换。]{style="font-family:宋体"}

[[本命令是]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_265031458}[保护倒换的手工倒换命令，用来方便管理员对网络流量进行管理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x986954360}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x450095179}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[、]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[存在备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[，将该]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的流量手工倒换到它的备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[上转发。]{style="font-family:宋体"}

[[\<Sysname\> l2vpn switchover peer 3.3.3.3 pw-id 100]{lang="EN-US"}]{#struct_0_x4077_x5759_1468770971}
:::::

::: {#988247972 .myid}
[]{#_Toc404791541}[]{#struct_0_x4077_x5759_x701082766}[]{#_Toc306302337}[]{#_Toc300843409}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x4077_x5759_28903237}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[mtu]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837562865}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_944950188}

[**[mtu]{lang="EN-US"}**[ *mtu*]{lang="EN-US"}]{#struct_0_x4077_x5759_749983214}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x4077_x5759_1705924349}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_501675314}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x813325}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x216641104}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1019960900}[/]{lang="PT-BR"}[交叉连接组自动发现视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837497329}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_264471748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x998576090}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1867452229}

[*[mtu]{lang="EN-US"}*]{#struct_0_x4077_x5759_1469136000}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。本参数的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x305393841}

[[在]{style="font-family:宋体"}]{#struct_0_x4077_x5759_436698218}[交叉连接视图]{style="font-family:宋体"}[/]{lang="PT-BR"}[交叉连接组自动发现视图下执行本命令后，该视图下建立的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值均为本命令配置的值。]{style="font-family:宋体"}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1755568466}[上发送报文的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为包括控制字、]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和网络层报文在内的报文的最大长度。]{style="font-family:宋体"}

[[需要注意的是，如果采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_x4077_x5759_x837431793}[信令协议建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则要求]{style="font-family:宋体"}[PW]{lang="EN-US"}[两端的]{style="font-family:宋体"}[PE]{lang="EN-US"}[上为]{style="font-family:宋体"}[PW]{lang="EN-US"}[配置相同的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。否则，]{style="font-family:宋体"}[PW]{lang="EN-US"}[无法]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_641363455}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x2023835421}[在交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的交叉连接]{style="font-family:宋体"}[ac2pw]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1400]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1742287254}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection ac2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-ac2pw\] mtu 1400]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1840448235}[在交叉连接组自动发现视图下，配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1400]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1446905526}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] mtu 1400]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1380981540}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837366257}**[xconnect-group]{lang="EN-US"}**
:::

::: {#-1030704014 .myid}
[]{#_Toc404791542}[]{#struct_0_x4077_x5759_949205410}[]{#_Toc385403459}[]{#_Toc379982570}[]{#_Toc374974308}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- payload**

------------------------------------------------------------------------

[**[payload]{lang="EN-US"}**]{#struct_0_x4077_x5759_x622966623}[命令用来配置电路仿真类中每个分组的净载荷大小。]{style="font-family:宋体"}

[**[undo payload]{lang="EN-US"}**]{#struct_0_x4077_x5759_x967341728}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x283273856}

[**[payload ]{lang="EN-US"}***[size-value]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1346383960}

[**[undo payload]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1550602203}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1702615682}

[[SAToP]{lang="EN-US"}]{#struct_0_x4077_x5759_x544970058}[模式下，净载荷的大小与电路仿真接口的电路类型有关，具体取值如下：]{style="font-family:宋体"}

[[E1]{lang="EN-US"}]{#struct_0_x4077_x5759_x1063710291}[---]{style="font-family:宋体"}[256]{lang="EN-US"}[字节、]{style="font-family:宋体"}[T1]{lang="EN-US"}[---]{style="font-family:宋体"}[192]{lang="EN-US"}[字节、]{style="font-family:宋体"}[E3]{lang="EN-US"}[---]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节、]{style="font-family:宋体"}[T3]{lang="EN-US"}[---]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[CESoPSN]{lang="EN-US"}]{#struct_0_x4077_x5759_x1237070609}[模式下，净载荷的大小与电路仿真接口的时隙数有关。净载荷大小（]{style="font-family:宋体"}[L]{lang="EN-US"}[字节）、时隙数（]{style="font-family:宋体"}[N]{lang="EN-US"}[）、分组化延迟（]{style="font-family:宋体"}[D]{lang="EN-US"}[毫秒）有如下关系：]{style="font-family:宋体"}

[[L = 8 \* N \* D]{lang="EN-US"}]{#struct_0_x4077_x5759_1022616994}[。]{style="font-family:宋体"}

[[缺省载荷如下：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x915781009}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N=1]{lang="EN-US"}]{#struct_0_x4077_x5759_x348299739}[时，]{style="font-family:宋体"}[D]{lang="EN-US"}[为]{style="font-family:宋体"}[8]{lang="EN-US"}[毫秒，相应的净载荷大小为]{style="font-family:宋体"}[64]{lang="EN-US"}[字节；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2\<=N\<=4]{lang="EN-US"}]{#struct_0_x4077_x5759_x101570020}[时，]{style="font-family:
宋体"}[D]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}[毫秒，相应的净载荷大小为]{style="font-family:宋体"}[32\*N]{lang="EN-US"}[字节；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N\>=5]{lang="EN-US"}]{#struct_0_x4077_x5759_x967407264}[时，]{style="font-family:宋体"}[D]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[毫秒，相应的净载荷大小为]{style="font-family:宋体"}[8\*N]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2020823431}

[[电路仿真类视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2000124885}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_98102146}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1549912254}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x207005317}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1061996668}

[*[size-value]{lang="EN-US"}*]{#struct_0_x4077_x5759_x810099616}[：电路仿真类中每个分组的净载荷大小，取值范围为]{style="font-family:宋体"}[32]{lang="EN-US"}[～]{style="font-family:宋体"}[1312]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2052784629}

[[通过配置分组的净载荷大小，可控制在]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_2031830535}[上传输的分组报文的大小。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1849161835}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x967472800}[配置电路仿真类]{style="font-family:宋体"}[satop]{lang="EN-US"}[中每个分组的净载荷大小为]{style="font-family:宋体"}[512]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x1122432390}

[\[Sysname\] cem-class satop]{lang="EN-US"}

[\[Sysname-cem-satop\] payload 512]{lang="EN-US"}
:::

::: {#1903411553 .myid}
[]{#_Toc404791543}[]{#struct_0_x4077_x5759_1002764545}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- peer**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**]{#struct_0_x4077_x5759_x686361095}[命令用来配置交叉连接的]{style="font-family:宋体"}[PW]{lang="EN-US"}[，并进入交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[PW]{lang="EN-US"}[已存在，则直接进入交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer**]{lang="EN-US"}]{#struct_0_x4077_x5759_830978362}[命令用来删除指定的]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1844197165}

[**[peer]{lang="EN-US"}**[ *ip-address* **pw-id** *pw-id* \[ **in-label** *label-value* **out-label** *label-value* \] \[ **pw-class** *class-name* \| **tunnel-policy** *tunnel-policy-name* \] \*]{lang="EN-US"}]{#struct_0_x4077_x5759_911302860}

[**[undo]{lang="EN-US"}**[ **peer** *ip-address* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_x4077_x5759_x1954691195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_347786764}

[[未配置交叉连接的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x836776433}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1372256643}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1360006929}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1445982177}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1486488352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_396009324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1874089705}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x2139098062}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_x836710897}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}**[ *l*]{lang="EN-US"}]{#struct_0_x4077_x5759_251912895}*[abel-value]{lang="EN-US"}*[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[入标签。]{style="font-family:宋体"}*[l]{lang="EN-US"}[abel-value]{lang="EN-US"}*[为入标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}**[ *l*]{lang="EN-US"}]{#struct_0_x4077_x5759_1996791063}*[abel-value]{lang="EN-US"}*[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[出标签。]{style="font-family:宋体"}*[l]{lang="EN-US"}[abel-value]{lang="EN-US"}*[为出标签值]{style="font-family:宋体"}[。本参数]{style="font-family:宋体"}[的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pw-class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x4077_x5759_1692263351}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板中可以配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[的数据封装类型、是否使用控制字等。如果不指定本参数，则]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型由接口的链路类型决定，对于不强制要求使用控制字的]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型，不支持控制字功能。]{style="font-family:宋体"}

[**[tunnel-policy]{lang="EN-US"}**[ *tunnel-policy-name*]{lang="EN-US"}]{#struct_0_x4077_x5759_1994521378}[：指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的隧道选择策略。]{style="font-family:宋体"}*[tunnel-policy-name]{lang="EN-US"}*[表示隧道策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则使用缺省的隧道选择策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x928717974}

[[创建静态]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x837300724}[时，必须指定]{style="font-family:宋体"}**[in-label]{lang="EN-US"}**[和]{style="font-family:宋体"}**[out-label]{lang="EN-US"}**[参数；静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[已经存在，进入交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图时，无需指定]{style="font-family:宋体"}**[in-label]{lang="EN-US"}**[和]{style="font-family:宋体"}**[out-label]{lang="EN-US"}**[参数。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[in-label]{lang="EN-US"}**]{#struct_0_x4077_x5759_x926424524}[和]{style="font-family:宋体"}**[out-label]{lang="EN-US"}**[参数，且尚未创建静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则表示采用]{style="font-family:宋体"}[LDP]{lang="EN-US"}[信令协议建立]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1043017454}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW ID]{lang="EN-US"}]{#struct_0_x4077_x5759_x55444270}[是一对]{style="font-family:宋体"}[PE]{lang="EN-US"}[之间]{style="font-family:宋体"}[PW]{lang="EN-US"}[的标识，本端和远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[上为同一]{style="font-family:宋体"}[PW]{lang="EN-US"}[指定的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[必须相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在本端]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1797851474}[PE]{lang="EN-US"}[上，远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识一条]{style="font-family:宋体"}[PW]{lang="EN-US"}[。配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[时指定的远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，不能与已经存在的]{style="font-family:宋体"}[VPLS PW]{lang="EN-US"}[、交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[同时相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_755360528}[冗余保护功能和多段]{style="font-family:宋体"}[PW]{lang="EN-US"}[功能互斥。即，如果在交叉连接视图下通过重复执行]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令配置了两条]{style="font-family:宋体"}[PW]{lang="EN-US"}[，则不能在交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图下执行]{style="font-family:宋体"}**[backup-peer]{lang="EN-US"}**[命令配置备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[；反之亦然。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果为静态]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x105026763}[PW]{lang="EN-US"}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[LSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x394607787}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_356162314}[为交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内的交叉连接]{style="font-family:宋体"}[pw2pw]{lang="EN-US"}[配置一条]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[：远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[4.4.4.4]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并进入交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x837235188}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection pw2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-pw2pw\] peer 4.4.4.4 pw-id 200]{lang="EN-US"}

[\[Sysname-xcg-vpn1-pw2pw-4.4.4.4-200\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x536634654}[为交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内的交叉连接]{style="font-family:宋体"}[pw2pw]{lang="EN-US"}[配置一条静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[：远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的地址为]{style="font-family:宋体"}[5.5.5.5]{lang="EN-US"}[，]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[100]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并进入交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x396619667}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection pw2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-pw2pw\] peer 5.5.5.5 pw-id 200 in-label 100 out-label 200]{lang="EN-US"}

[\[Sysname-xcg-vpn1-pw2pw-5.5.5.5-200\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1818627318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ldp]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1253148291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2015070668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837169652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel-policy]{lang="EN-US"}**]{#struct_0_x4077_x5759_x971435446}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道策略）]{lang="EN-US" style="font-family:宋体"}[]{#_Toc300843411}
:::

::: {#-1992627212 .myid}
[]{#_Toc339307309}[]{#_Toc404791544}[]{#struct_0_x4077_x5759_x180264876}[]{#_Toc337567385}[]{#_Toc336272256}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- peer signaling**

------------------------------------------------------------------------

[**[peer signaling]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837104116}[命]{style="font-family:宋体"}[令用来使能本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息的能力。]{style="font-family:宋体"}

[**[undo peer signaling]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2105143387}[命令用来禁止本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837562868}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **signaling** \[ **non-standard** \]]{lang="EN-US"}]{#struct_0_x4077_x5759_944753580}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **signaling**]{lang="EN-US"}]{#struct_0_x4077_x5759_2119107466}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_403533016}

[[本地路由器具有与]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x548208653}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换标签块信息的能力，并且采用]{style="font-family:宋体"}[RFC 4761]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换标签块信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x994790016}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x141285815}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1678920998}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_348629753}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x837497332}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_265061571}

[*[group-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_196792777}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1075281179}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x4077_x5759_x967734944}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[non-standard]{lang="EN-US"}**]{#struct_0_x4077_x5759_277291691}[：指定采用]{style="font-family:宋体"}[draft-kompella-ppvpn-l2vpn-03]{lang="EN-US"}[草案中定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换标签块信息。如果不指定本参数，则采用]{style="font-family:宋体"}[RFC 4761]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换标签块信息。请根据对等体支持的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式类型，选择是否指定本参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x461249825}

[[建立]{style="font-family:宋体"}[BGP PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x41750429}[时，]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备需要通过]{style="font-family:宋体"}[MP-BGP]{lang="EN-US"}[协议来交换标签块信息。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x294476557}[地址族视图下执行]{style="font-family:宋体"}**[peer enable]{lang="EN-US"}**[命令后，本地路由器即具有与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组采用]{style="font-family:宋体"}[RFC 4761]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换标签块信息的能力。如需禁止该能力或该对等体不支持交换标签块信息，则执行]{style="font-family:宋体"}**[undo peer signaling]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837431796}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_641560063}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[3.3.3.9]{lang="EN-US"}[交换]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息的能力，并指定采用]{style="font-family:宋体"}[draft-kompella-ppvpn-l2vpn-03]{lang="EN-US"}[草案中定义的]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[格式交换标签块信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x837366260}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] peer 3.3.3.9 signaling non-standard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1002961154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp l2vpn ]{lang="EN-US"}**]{#struct_0_x4077_x5759_481662819}**[signaling]{lang="EN-US"}**
:::

::: {#-985333979 .myid}
[]{#_Toc404791545}[]{#struct_0_x4077_x5759_456037817}[]{#_Toc338409090}[]{#_Toc336412980}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- policy vpn-target**

------------------------------------------------------------------------

[**[policy vpn-target]{lang="EN-US"}**]{#struct_0_x4077_x5759_102406604}[命令用来对接收到的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息使能]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能，即只将]{style="font-family:宋体"}[Export Route Target]{lang="EN-US"}[属性与本地]{style="font-family:宋体"}[Import Route Target]{lang="EN-US"}[属性匹配的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息加入到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息表。]{style="font-family:宋体"}

[**[undo policy vpn-target]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1471133010}[命令用来取消对]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息的]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能，即接收所有的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_828460764}

[**[policy vpn-target]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1917456754}

[**[undo policy vpn-target]{lang="EN-US"}**]{#struct_0_x4077_x5759_x836776436}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1371928963}

[[对接收到的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_409374474}[信息使能]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_427038335}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_138581115}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x934221048}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1426625198}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x552316638}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x836710900}

[[在跨域]{style="font-family:宋体"}[VPN-OptionB]{lang="EN-US"}]{#struct_0_x4077_x5759_x1704336714}[组网中，]{style="font-family:宋体"}[ASBR-PE]{lang="EN-US"}[需要保存所有]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息（即标签块信息），以通告给远端]{style="font-family:宋体"}[ASBR-PE]{lang="EN-US"}[。这种情况下，]{style="font-family:宋体"}[ASBR-PE]{lang="EN-US"}[上需执行]{style="font-family:宋体"}**[undo policy vpn-target]{lang="EN-US"}**[命令接收所有的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息，不对它们进行]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤。]{style="font-family:宋体"}

[[跨域]{style="font-family:宋体"}[VPN-OptionB]{lang="EN-US"}]{#struct_0_x4077_x5759_x837300723}[的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x926883276}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_257712042}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，取消对]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息的]{style="font-family:宋体"}[VPN-Target]{lang="EN-US"}[过滤功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_240134178}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] undo policy vpn-target]{lang="EN-US"}
:::

::: {#-996922335 .myid}
[]{#_Toc203821279}[]{#_Toc202771657}[]{#_Toc202151059}[]{#_Toc196128370}[]{#_Toc195449622}[]{#_Toc189301791}[]{#_Toc180990992}[]{#_Toc404791546}[]{#struct_0_x4077_x5759_x1766564424}[]{#_Toc351118430}[]{#_Toc252883315}[]{#_Toc250560271}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ppp ipcp ignore local-ip**

------------------------------------------------------------------------

[**[ppp ipcp ignore local-ip]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1765974600}[命令用来配置]{style="font-family:
宋体"}[PPP]{lang="EN-US"}[支持]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ppp ipcp ignore local-ip**]{lang="EN-US"}]{#struct_0_x4077_x5759_1148912405}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1852089991}

[**[ppp ipcp ignore local-ip]{lang="EN-US"}**]{#struct_0_x4077_x5759_2081474030}

[**[undo ppp ipcp ignore local-ip]{lang="PT-BR"}**]{#struct_0_x4077_x5759_808402404}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1765909064}

[[PPP]{lang="EN-US"}]{#struct_0_x4077_x5759_x422611616}[不支持]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商，本端接口必须配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址才会和对端进行]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1499428404}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x207768751}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2060293722}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x200414944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1850031150}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1260756426}

[[MPLS L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x637057387}[连接异构网络时，链路层协商报文不会在网络中传递，]{style="font-family:宋体"}[CE]{lang="EN-US"}[之间无法直接建立二层连接。因此，]{style="font-family:宋体"}[PE]{lang="EN-US"}[需要与接入的]{style="font-family:宋体"}[CE]{lang="EN-US"}[建立二层连接，例如，]{style="font-family:宋体"}[PPP]{lang="EN-US"}[链路中]{style="font-family:宋体"}[PE]{lang="EN-US"}[需要与]{style="font-family:宋体"}[CE]{lang="EN-US"}[进行]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商，以建立]{style="font-family:宋体"}[PPP]{lang="EN-US"}[连接，如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，通过本配置，可以确保]{style="font-family:宋体"}[PE]{lang="EN-US"}[与]{style="font-family:宋体"}[CE]{lang="EN-US"}[进行无]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商，保证]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商通过。]{style="font-family:宋体"}

[[需要注意的是，在]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x4077_x5759_x675576875}[链路中，如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则无需配置]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商或]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则在同一接口下，]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商配置的优先级高于]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置。即，如果在同一接口下同时配置了]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商和]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则采用]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商方式进行]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1522287098}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x200349408}[配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[支持]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1624115828}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol ppp]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp ipcp ignore local-ip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1847994895}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp ipcp proxy]{lang="EN-US"}**]{#struct_0_x4077_x5759_760176888}
:::

::: {#-688489117 .myid}
[]{#_Toc404791547}[]{#struct_0_x4077_x5759_x200283872}[]{#_Toc351118431}[]{#_Toc252883316}[]{#_Toc250560272}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- ppp ipcp proxy**

------------------------------------------------------------------------

[**[ppp ipcp proxy]{lang="EN-US"}**]{#struct_0_x4077_x5759_x668632034}[命令用来指定]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ppp ipcp proxy**]{lang="EN-US"}]{#struct_0_x4077_x5759_746130106}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1831841410}

[**[ppp ipcp proxy ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1744461961}

[**[undo ppp ipcp proxy]{lang="EN-US"}**]{#struct_0_x4077_x5759_x200218336}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1622447509}

[[未指定]{style="font-family:宋体"}[IPCP]{lang="EN-US"}]{#struct_0_x4077_x5759_x2135048512}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x200677088}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1098363011}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x128501134}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1136686547}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1301795937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x200611552}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4077_x5759_x682465726}[：]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_282299378}

[[MPLS L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_1511097311}[连接异构网络时，链路层协商报文不会在网络中传递，]{style="font-family:宋体"}[CE]{lang="EN-US"}[之间无法直接建立二层连接。因此，]{style="font-family:宋体"}[PE]{lang="EN-US"}[需要与接入的]{style="font-family:宋体"}[CE]{lang="EN-US"}[建立二层连接，例如，]{style="font-family:宋体"}[PPP]{lang="EN-US"}[链路中]{style="font-family:宋体"}[PE]{lang="EN-US"}[需要与]{style="font-family:宋体"}[CE]{lang="EN-US"}[进行]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商，以建立]{style="font-family:宋体"}[PPP]{lang="EN-US"}[连接，如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，通过本配置将]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置为远端]{style="font-family:宋体"}[CE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，可以确保]{style="font-family:宋体"}[PE]{lang="EN-US"}[使用这个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与本端]{style="font-family:宋体"}[CE]{lang="EN-US"}[进行]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商，保证]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商通过。]{style="font-family:宋体"}

[[需要注意的是，在]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x4077_x5759_1798207936}[链路中，如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则无需配置]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商或]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[连接]{style="font-family:宋体"}[CE]{lang="EN-US"}[的接口没有配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则在同一接口下，]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商配置的优先级高于]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址配置。即，如果在同一接口下同时配置了]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商和]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则采用]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[无地址协商方式进行]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x200546016}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_465820282}[指定]{style="font-family:宋体"}[IPCP]{lang="EN-US"}[代理]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1530472215}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol ppp]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] ppp ipcp proxy 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_768212429}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp ipcp ignore local-ip]{lang="EN-US"}**]{#struct_0_x4077_x5759_262484031}
:::

::::: {#319473676 .myid}
[]{#_Toc404791548}[]{#struct_0_x4077_x5759_x967472799}[]{#_Toc373221162}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- protection dual-receive**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image004.png){#图片 8 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_x1843066239}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_x857926817}
:::

[ ]{lang="EN-US"}

[**[protection dual-receive]{lang="EN-US"}**]{#struct_0_x4077_x5759_x967538335}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[冗余保护的双收功能，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[和备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[都能接收报文，主备]{style="font-family:宋体"}[PW]{lang="EN-US"}[工作在单发双收模式。]{style="font-family:宋体"}

[**[undo protection dual-receive ]{lang="EN-US"}**]{#struct_0_x4077_x5759_1704885324}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2084989418}

[**[protection dual-receive]{lang="EN-US"}**]{#struct_0_x4077_x5759_1369913706}

[**[undo protection dual-receive]{lang="EN-US"}**]{#struct_0_x4077_x5759_1604431990}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1192585207}

[[缺省情况下，未配置]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1865391963}[冗余保护的双收功能，即配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[冗余保护时，仅主]{style="font-family:宋体"}[PW]{lang="EN-US"}[能发送和接收报文，备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[不能发送和接收报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x692664184}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x760153894}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_318733960}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_316030546}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x967603871}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1606713176}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x562975002}[为交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内的交叉连接]{style="font-family:宋体"}[ac2pw]{lang="EN-US"}[配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[冗余保护的双收功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x853907281}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection ac2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-ac2pw\] protection dual-receive]{lang="EN-US"}
:::::

::: {#-1410971825 .myid}
[]{#_Toc404791549}[]{#struct_0_x4077_x5759_x33518743}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- pw-class (system view)**

------------------------------------------------------------------------

[**[pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837235187}[命令用来创建]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板]{style="font-family:宋体"}[，并]{style="font-family:宋体"}[进入]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x536962334}[命令用来删除已经创建的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_385797166}

[**[pw-class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1606900013}

[**[undo pw-class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_2113170726}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x366872511}

[[设备上不存在任何]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x972551427}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1261669827}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x837169651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x971632054}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x2144343046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_994816080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2105172415}

[*[class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_155200977}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x453094060}

[[通过本命令创建]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x1384767689}[模板，并进入]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图后，可以在]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图下指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的属性，如]{style="font-family:宋体"}[PW]{lang="EN-US"}[的数据封装类型、是否使用控制字。具有相同属性的]{style="font-family:宋体"}[PW]{lang="EN-US"}[可以通过引用相同的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板，实现对]{style="font-family:宋体"}[PW]{lang="EN-US"}[属性的配置，从而简化配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x837104115}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x2105077851}[创建]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板]{style="font-family:宋体"}[pw100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_416571703}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1634365288}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[control-word enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x545862098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1436145500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-type]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1328702376}
:::

::: {#-783763110 .myid}
[]{#_Toc339307311}[]{#_Toc337714174}[]{#_Toc404791550}[]{#struct_0_x4077_x5759_x1865387509}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- pw-class (cross-connect auto-discovery view)**

------------------------------------------------------------------------

[**[pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837562867}[命令用来指定引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **pw-class**]{lang="EN-US"}]{#struct_0_x4077_x5759_945081260}[命令用来取消引用]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1892571755}

[**[pw-class ]{lang="EN-US"}***[class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_x996285588}

[**[undo]{lang="EN-US"}**[ **pw-class**]{lang="EN-US"}]{#struct_0_x4077_x5759_x1471380660}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_585771529}

[[不引用任何]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1140116902}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_289769493}

[[交叉连接组自动发现视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x837497331}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_264996035}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1299368440}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1501339060}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1468580479}

[*[class-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_x739818363}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_416974828}

[[在交叉连接组自动发现视图下执行本命令指定引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_597531214}[模板后，该]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板将应用于该视图下建立的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_341904736}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x837431795}[在交叉连接组自动发现视图下，指定引用的]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板为]{style="font-family:宋体"}[pw100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_641756671}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] quit]{lang="EN-US"}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] pw-class pw100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x261304304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[control-word enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x381619377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1445194512}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_1403694562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pw-type]{lang="EN-US"}**]{#struct_0_x4077_x5759_x837366259}
:::

::: {#1550157549 .myid}
[]{#_Toc404791551}[]{#struct_0_x4077_x5759_1002371329}[]{#_Toc349050372}[]{#_Toc349564616}[]{#_Toc349050373}[]{#_Toc349564617}[]{#_Toc349050374}[]{#_Toc349564618}[]{#_Toc349050375}[]{#_Toc349564619}[]{#_Toc349050376}[]{#_Toc349564620}[]{#_Toc349050377}[]{#_Toc349564621}[]{#_Toc349050378}[]{#_Toc349564622}[]{#_Toc349050379}[]{#_Toc349564623}[]{#_Toc349050380}[]{#_Toc349564624}[]{#_Toc349050381}[]{#_Toc349564625}[]{#_Toc349050382}[]{#_Toc349564626}[]{#_Toc349050383}[]{#_Toc349564627}[]{#_Toc349050384}[]{#_Toc349564628}[]{#_Toc349050385}[]{#_Toc349564629}[]{#_Toc349050386}[]{#_Toc349564630}[]{#_Toc349050387}[]{#_Toc349564631}[]{#_Toc349050388}[]{#_Toc349564632}[]{#_Toc349050389}[]{#_Toc349564633}[]{#_Toc349050390}[]{#_Toc349564634}[]{#_Toc349050391}[]{#_Toc349564635}[]{#_Toc349050392}[]{#_Toc349564636}[]{#_Toc349050393}[]{#_Toc349564637}[]{#_Toc349050394}[]{#_Toc349564638}[]{#_Toc349050395}[]{#_Toc349564639}[]{#_Toc349050396}[]{#_Toc349564640}[]{#_Toc349050397}[]{#_Toc349564641}[]{#_Toc349050398}[]{#_Toc349564642}[]{#_Toc349050399}[]{#_Toc349564643}[]{#_Toc349050400}[]{#_Toc349564644}[]{#_Toc349050401}[]{#_Toc349564645}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- pw-type**

------------------------------------------------------------------------

[**[pw-type]{lang="EN-US"}**]{#struct_0_x4077_x5759_862820522}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型。]{style="font-family:宋体"}

[**[undo pw-type]{lang="EN-US"}**]{#struct_0_x4077_x5759_163246039}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1248389985}

[**[pw-type]{lang="EN-US"}**[ { **ethernet** \| **vlan** }]{lang="EN-US"}]{#struct_0_x4077_x5759_x1568299355}

[**[undo pw-type]{lang="EN-US"}**]{#struct_0_x4077_x5759_x441496578}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1367823793}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x836776435}[数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1372125571}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_993235644}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x905491956}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x59611648}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1248005839}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2080630278}

[**[ethernet]{lang="EN-US"}**]{#struct_0_x4077_x5759_1619553078}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1369856339}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x836710899}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_x4077_x5759_728783221}[数据封装类型下，]{style="font-family:
宋体"}[PW]{lang="EN-US"}[上传输的帧不能携带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[。对于]{style="font-family:宋体"}[CE]{lang="EN-US"}[侧的报文，如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到带有]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文，则将其去除后再添加]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道标签转发；如果从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到不带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文，则直接添加]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道标签后转发。对于]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[CE]{lang="EN-US"}[的报文，如果]{style="font-family:宋体"}**[ac interface]{lang="EN-US"}**[命令配置的接入模式为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则添加]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[后转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[；如果配置的接入模式为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[，则不添加]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，直接转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[；无论]{style="font-family:宋体"}**[ac interface]{lang="EN-US"}**[命令配置的接入模式为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[还是]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[，均不允许重写或去除已经存在的任何]{style="font-family:宋体"}[Tag]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_x4077_x5759_728848757}[数据封装类型下，]{style="font-family:宋体"}[PW]{lang="EN-US"}[上传输的帧必须携带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[。对于]{style="font-family:宋体"}[CE]{lang="EN-US"}[侧的报文，]{style="font-family:宋体"}[PE]{lang="EN-US"}[从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到带有]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文后，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[不要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则保留]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则将]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[改写为远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[期望的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（]{style="font-family:宋体"}[Tag]{lang="EN-US"}[可能是值为]{style="font-family:宋体"}[0]{lang="EN-US"}[的空]{style="font-family:宋体"}[Tag]{lang="EN-US"}[），再添加]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道标签后转发；从]{style="font-family:宋体"}[CE]{lang="EN-US"}[收到不带]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[的报文后，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[不要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则添加值为]{style="font-family:宋体"}[0]{lang="EN-US"}[的空]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，如果远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[要求]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[改写]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[，则添加一个远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[期望的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[（]{style="font-family:宋体"}[Tag]{lang="EN-US"}[可能是值为]{style="font-family:宋体"}[0]{lang="EN-US"}[的空]{style="font-family:宋体"}[Tag]{lang="EN-US"}[）后，再添加]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签和公网隧道标签后转发。对于]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送给]{style="font-family:宋体"}[CE]{lang="EN-US"}[的报文，如果]{style="font-family:宋体"}**[ac interface]{lang="EN-US"}**[命令配置的接入模式为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[时重写或保留]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[；如果配置的接入模式为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[，则去除]{style="font-family:宋体"}[P-Tag]{lang="EN-US"}[后转发给]{style="font-family:宋体"}[CE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，本命令只在]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x4077_x5759_122731218}[链路为以太网链路时有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x559997647}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x442383700}[配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[数据封装类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_728914293}

[\[Sysname\] pw-class pw100]{lang="EN-US"}

[\[Sysname-pw-pw100\] pw-type ethernet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2067559578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ac interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_x546957518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw-class]{lang="EN-US"}**]{#struct_0_x4077_x5759_1543555754}
:::

::: {#2052875588 .myid}
[]{#_Toc404791552}[]{#struct_0_x4077_x5759_1561513664}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1895911177}[命令用来清除接口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2043459409}

[**[reset counters interface]{lang="EN-US"}**[ \[ **circuit-emulation** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x4077_x5759_x514633396}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1138985706}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x698733595}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1970849917}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1561579200}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1657938667}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_564971719}

[**[circuit-emulation]{lang="EN-US"}**]{#struct_0_x4077_x5759_1842932840}[：清除电路仿真接口的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_1257986429}[：电路仿真接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1663526982}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1144254766}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4077_x5759_1282122118}**[c]{lang="EN-US"}[ircuit-]{lang="EN-US"}[e]{lang="EN-US"}[mulation]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4077_x5759_x981496290}**[c]{lang="EN-US"}[ircuit-]{lang="EN-US"}[e]{lang="EN-US"}[mulation]{lang="EN-US"}**[而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[电路仿真]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4077_x5759_1561906880}**[c]{lang="EN-US"}[ircuit-]{lang="EN-US"}[e]{lang="EN-US"}[mulation]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除指定]{lang="EN-US" style="font-family:宋体"}[电路仿真]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_855379534}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1542256523}[清除接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface circuit-emulation 2/3/0:0]{lang="EN-US"}]{#struct_0_x4077_x5759_1045334131}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x166104688}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1621757147}**[c]{lang="EN-US"}[ircuit-]{lang="EN-US"}[e]{lang="EN-US"}[mulation]{lang="EN-US"}**
:::

::::: {#1457959242 .myid}
[]{#_Toc404791553}[]{#struct_0_x4077_x5759_449820087}[]{#_Toc389644990}[]{#_Toc378236125}[]{#_Toc375224253}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- reset l2vpn statistics pw**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_1659913203}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_x1560361448}
:::

[ ]{lang="EN-US"}

[**[reset l2vpn statistics pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1511609021}[命令用来清除指定]{style="font-family:
宋体"}[PW]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1561972416}

[**[reset l2vpn statistics pw ]{lang="EN-US"}**[\[ **xconnect-group** ]{lang="EN-US"}]{#struct_0_x4077_x5759_x698795047}*[group-name]{lang="FR"}***[ ]{lang="FR"}**[\[ **connection** ]{lang="EN-US"}*[connection-name ]{lang="FR"}*[\] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x429882340}

[[用户]{style="font-family:宋体"}]{#struct_0_x4077_x5759_255060750}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x652875628}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1098011641}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_475755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_275796086}

[**[xconnect-group ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1638525120}*[group-name]{lang="FR"}*[：清除指定交叉连接组内的]{style="font-family:宋体"}[PW]{lang="FR"}[报文统计信息。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定该参数，则清除所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[connection ]{lang="EN-US"}**]{#struct_0_x4077_x5759_1383979822}*[connection-name]{lang="FR"}*[：清除指定]{style="font-family:宋体"}[PW]{lang="FR"}[的统计信息。]{style="font-family:宋体"}*[connection-name]{lang="FR"}*[为交叉连接组内交叉连接的名字，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[20]{lang="FR"}[个字符的字符串，区分大小写。如果不指定该参数，则清除指定交叉连接组内的所有]{style="font-family:
宋体"}[PW]{lang="FR"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1561382589}

[[当]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1226718492}[存在备]{style="font-family:宋体"}[PW]{lang="EN-US"}[时，会同时清除主]{style="font-family:宋体"}[PW]{lang="EN-US"}[和备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_951572560}

[[\# ]{lang="FR"}]{#struct_0_x4077_x5759_x1967226692}[清除本设备上所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset l2vpn statistics pw]{lang="FR"}]{#struct_0_x4077_x5759_x2110164014}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1848538964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[statistics enable]{lang="NO-BOK"}**]{#struct_0_x4077_x5759_x1200939873}
:::::

::: {#1047826473 .myid}
[]{#_Toc288911613}[]{#_Toc265738467}[]{#_Toc404791554}[]{#struct_0_x4077_x5759_x1991340188}[]{#_Toc288911631}[]{#_Toc264644583}[]{#_Toc325545612}[]{#_Toc325545613}[]{#_Toc325545614}[]{#_Toc325545615}[]{#_Toc325545616}[]{#_Toc325545617}[]{#_Toc325545618}[]{#_Toc325545619}[]{#_Toc325545620}[]{#_Toc325545621}[]{#_Toc325545622}[]{#_Toc325545623}[]{#_Toc325545624}[]{#_Toc325545625}[]{#_Toc325545626}[]{#_Toc325545627}[]{#_Toc325545628}[]{#_Toc325545629}[]{#_Toc325545630}[]{#_Toc325545631}[]{#_Toc325545632}[]{#_Toc325545633}[]{#_Toc325545634}[]{#_Toc325545635}[]{#_Toc325545636}[]{#_Toc325545637}[]{#_Toc366747005}[]{#_Toc366769348}[]{#_Toc366747006}[]{#_Toc366769349}[]{#_Toc366747007}[]{#_Toc366769350}[]{#_Toc366747008}[]{#_Toc366769351}[]{#_Toc366747009}[]{#_Toc366769352}[]{#_Toc366747010}[]{#_Toc366769353}[]{#_Toc366747011}[]{#_Toc366769354}[]{#_Toc366747012}[]{#_Toc366769355}[]{#_Toc366747013}[]{#_Toc366769356}[]{#_Toc366747014}[]{#_Toc366769357}[]{#_Toc366747015}[]{#_Toc366769358}[]{#_Toc366747016}[]{#_Toc366769359}[]{#_Toc366747017}[]{#_Toc366769360}[]{#_Toc366747018}[]{#_Toc366769361}[]{#_Toc366747019}[]{#_Toc366769362}[]{#_Toc366747020}[]{#_Toc366769363}[]{#_Toc366747021}[]{#_Toc366769364}[]{#_Toc366747022}[]{#_Toc366769365}[]{#_Toc366747023}[]{#_Toc366769366}[]{#_Toc366747024}[]{#_Toc366769367}[]{#_Toc366747025}[]{#_Toc366769368}[]{#_Toc366747026}[]{#_Toc366769369}[]{#_Toc366747027}[]{#_Toc366769370}[]{#_Toc366747028}[]{#_Toc366769371}[]{#_Toc366747029}[]{#_Toc366769372}[]{#_Toc366747030}[]{#_Toc366769373}[]{#_Toc366747031}[]{#_Toc366769374}[]{#_Toc366747032}[]{#_Toc366769375}[]{#_Toc366747033}[]{#_Toc366769376}[]{#_Toc366747034}[]{#_Toc366769377}[]{#_Toc366747035}[]{#_Toc366769378}[]{#_Toc366747036}[]{#_Toc366769379}[]{#_Toc366747037}[]{#_Toc366769380}[]{#_Toc366747038}[]{#_Toc366769381}[]{#_Toc366747039}[]{#_Toc366769382}[]{#_Toc366747040}[]{#_Toc366769383}[]{#_Toc366747041}[]{#_Toc366769384}[]{#_Toc366747042}[]{#_Toc366769385}[]{#_Toc366747043}[]{#_Toc366769386}[]{#_Toc366747044}[]{#_Toc366769387}[]{#_Toc366747045}[]{#_Toc366769388}[]{#_Toc366747046}[]{#_Toc366769389}[]{#_Toc366747047}[]{#_Toc366769390}[]{#_Toc366747048}[]{#_Toc366769391}[]{#_Toc366747049}[]{#_Toc366769392}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- revertive**

------------------------------------------------------------------------

[**[revertive]{lang="EN-US"}**]{#struct_0_x4077_x5759_x166373704}[命令用来配置]{style="font-family:宋体"}[PW]{lang="EN-US"}[冗余保护倒换的回切模式，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后流量是否从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[，以及回切模式下的回切等待时间，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后，流量从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[的等待时间。]{style="font-family:宋体"}

[**[undo revertive wtr]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2022408524}[命令用来恢复回切等待时间的缺省情况，即回切等待时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo revertive never]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1330132096}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1485479773}

[**[revertive ]{lang="EN-US"}**[{ **wtr** *wtr-time* \| **never** }]{lang="EN-US"}]{#struct_0_x4077_x5759_729373045}

[**[undo revertive ]{lang="EN-US"}**[{ **wtr** \| **never** }]{lang="EN-US"}]{#struct_0_x4077_x5759_694828639}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x934647178}

[[开启回切功能，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x262699771}[恢复后，流量会从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[；回切等待时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后，流量会立即从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1252658870}

[[交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x2032193527}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1254671736}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_572829745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_728783222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1911584188}

[**[wtr ]{lang="EN-US"}***[wtr-time]{lang="EN-US"}*]{#struct_0_x4077_x5759_1831917302}[：开启回切功能，并指定回切等待时间（]{style="font-family:宋体"}[wait-to-restore time]{lang="EN-US"}[），即主]{style="font-family:宋体"}[PW]{lang="EN-US"}[恢复后，等待]{style="font-family:宋体"}*[wtr-time]{lang="EN-US"}*[时间后，才将流量从备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[回切到主]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}*[wtr-time]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[never]{lang="EN-US"}**]{#struct_0_x4077_x5759_209106467}[：]{style="font-family:宋体"}[指定不回切。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1728913055}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x473788276}[为交叉连接组]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内的交叉连接]{style="font-family:宋体"}[ac2pw]{lang="EN-US"}[指定回切等待时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x84714039}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\] connection ac2pw]{lang="EN-US"}

[\[Sysname-xcg-vpn1-ac2pw\] revertive wtr 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728848758}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_122731217}
:::

::: {#263693428 .myid}
[]{#_Toc404791555}[]{#struct_0_x4077_x5759_x559997640}[]{#_Toc339307314}[]{#_Toc336507500}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- route-distinguisher**

------------------------------------------------------------------------

[**[route-distinguisher]{lang="EN-US"}**]{#struct_0_x4077_x5759_x442187092}[命令用来为当前交叉连接组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[RD]{lang="EN-US"}[（]{style="font-family:宋体"}[Route Distinguisher]{lang="EN-US"}[，路由标识符）。]{style="font-family:宋体"}

[**[undo route-distinguisher]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1911043651}[命令用来删除已配置的]{style="font-family:
宋体"}[RD]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1221974412}

[**[route-distinguisher]{lang="EN-US"}**[ *route-distinguisher*]{lang="EN-US"}]{#struct_0_x4077_x5759_1479074385}

[**[undo route-distinguisher]{lang="EN-US"}**]{#struct_0_x4077_x5759_x2111568021}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728914294}

[[没有为交叉连接组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_2067559571}[方式指定]{style="font-family:宋体"}[RD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x546367694}

[[交叉连接组自动发现视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x401815044}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_710818025}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_243403330}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1111194933}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x233253007}

[*[route-distinguisher]{lang="EN-US"}*]{#struct_0_x4077_x5759_x191867252}[：路由标识符，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。路由标识符有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x4077_x5759_728979830}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x4077_x5759_1720629327}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x4077_x5759_x723432178}[位自治系统号：]{style="font-family:宋体"}[16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。]{style="font-family:宋体"}[例如：]{lang="EN-US" style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1600001388}

[[在]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_1242965242}[中，]{style="font-family:宋体"}[RD]{lang="EN-US"}[用来区分不同]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内编号相同的站点。]{style="font-family:宋体"}[PE]{lang="EN-US"}[在通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布其连接的站点信息时，在]{style="font-family:宋体"}[Site ID]{lang="EN-US"}[前增加]{style="font-family:宋体"}[RD]{lang="EN-US"}[，通过]{style="font-family:宋体"}[RD]{lang="EN-US"}[和]{style="font-family:宋体"}[Site ID]{lang="EN-US"}[来唯一标识网络中的一个站点。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x203889438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能为不同交叉连接组的]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x98366630}[BGP]{lang="EN-US"}[方式配置相同的]{style="font-family:宋体"}[RD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能通过重复执行]{lang="EN-US" style="font-family:宋体"}**[route-distinguisher]{lang="EN-US"}**]{#struct_0_x4077_x5759_1786850914}[命令修改]{lang="EN-US" style="font-family:
宋体"}[RD]{lang="EN-US"}[值。必须先通过]{lang="EN-US" style="font-family:
宋体"}**[undo route-distinguisher]{lang="EN-US"}**[命令删除]{lang="EN-US" style="font-family:宋体"}[RD]{lang="EN-US"}[值，再通过]{lang="EN-US" style="font-family:宋体"}**[route-distinguisher]{lang="EN-US"}**[命令配置新的]{lang="EN-US" style="font-family:宋体"}[RD]{lang="EN-US"}[值。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728521078}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1992973746}[配置交叉连接组]{style="font-family:宋体"}[bbb]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[RD]{lang="EN-US"}[为]{style="font-family:宋体"}[22:2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1930230201}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] route-distinguisher 22:2]{lang="EN-US"}
:::

::: {#-190074586 .myid}
[]{#_Toc404791556}[]{#struct_0_x4077_x5759_385815901}[]{#_Toc338409099}[]{#_Toc336412987}[]{#_Toc289500177}[]{#_Toc137867338}[]{#_Toc83790635}[]{#_Toc81376594}[]{#_Toc70477292}[]{#_Toc67196376}[]{#_Toc67145423}[]{#_Toc65385660}[]{#_Toc61239880}[]{#_Toc53707296}[]{#_Toc53518769}[]{#_Toc50837077}[]{#_Toc43895343}[]{#_Toc391026654}[]{#_Toc391367234}[]{#_Toc391026655}[]{#_Toc391367235}[]{#_Toc391026656}[]{#_Toc391367236}[]{#_Toc391026657}[]{#_Toc391367237}[]{#_Toc391026658}[]{#_Toc391367238}[]{#_Toc391026659}[]{#_Toc391367239}[]{#_Toc391026660}[]{#_Toc391367240}[]{#_Toc391026661}[]{#_Toc391367241}[]{#_Toc391026662}[]{#_Toc391367242}[]{#_Toc391026663}[]{#_Toc391367243}[]{#_Toc391026664}[]{#_Toc391367244}[]{#_Toc391026665}[]{#_Toc391367245}[]{#_Toc391026666}[]{#_Toc391367246}[]{#_Toc391026667}[]{#_Toc391367247}[]{#_Toc391026668}[]{#_Toc391367248}[]{#_Toc391026669}[]{#_Toc391367249}[]{#_Toc391026670}[]{#_Toc391367250}[]{#_Toc391026671}[]{#_Toc391367251}[]{#_Toc391026672}[]{#_Toc391367252}[]{#_Toc391026673}[]{#_Toc391367253}[]{#_Toc391026674}[]{#_Toc391367254}[]{#_Toc391026675}[]{#_Toc391367255}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- rr-filter**

------------------------------------------------------------------------

[**[rr-filter]{lang="EN-US"}**]{#struct_0_x4077_x5759_x285258578}[命令用来创建路由反射器的反射策略：通过配置路由反射器支持的扩展团体属性号，对接收的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息进行过滤，只有接收的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息包含指定的扩展团体属性号时，路由反射器才会反射该]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rr-filter**]{lang="EN-US"}]{#struct_0_x4077_x5759_1245224809}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_510489004}

[**[rr-filter ]{lang="EN-US"}***[extended-community-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_728586614}

[**[undo rr-filter]{lang="EN-US"}**]{#struct_0_x4077_x5759_2002274350}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_458942864}

[[路由反射器不会对反射的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x1333412322}[信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1409739541}

[[BGP L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_1330003200}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1824749130}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1467328966}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1260540139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728652150}

[*[extended-community-number]{lang="EN-US"}*]{#struct_0_x4077_x5759_x87174684}[：路由反射器支持的扩展团体属性号，取值范围]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1150435776}

[[当一个集群中存在多个路由反射器时，通过在不同的路由反射器上配置不同的反射策略，可以实现路由反射器之间的负载分担。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_429932667}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1842097338}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1637743824}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，配置路由反射器支持的扩展团体属性号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，即该路由反射器只反射包含扩展团体属性]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_1607502162}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] rr-filter 10]{lang="EN-US"}
:::

::: {#1345955901 .myid}
[]{#_Toc404791557}[]{#struct_0_x4077_x5759_x966817442}[]{#_Toc385403472}[]{#_Toc379982582}[]{#_Toc374974309}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- rtp-header enable**

------------------------------------------------------------------------

[**[rtp-header enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1909239295}[命令用来配置电路仿真类中的报文携带]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头。]{style="font-family:宋体"}

[**[undo rtp-header enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_476267865}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1775475385}

[**[rtp-header enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1784049061}

[**[undo rtp-header enable]{lang="EN-US"}**]{#struct_0_x4077_x5759_1756111351}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_344895577}

[[电路仿真类的报文不携带]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x4077_x5759_1608440931}[头。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_x4077_x5759_9380712}

[[电路仿真类视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x153387162}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x966882978}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1685457659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x644950853}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1769410989}

[[通常情况下，电路仿真类中的报文不携带]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x4077_x5759_x660188337}[头。当时钟恢复方式为差分恢复方式时，出口]{style="font-family:宋体"}[PE]{lang="EN-US"}[需根据分组的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头中的差分时间戳信息进行时钟恢复，必须通过本命令配置电路仿真类中的报文携带]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1890834503}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1205253272}[配置电路仿真类]{style="font-family:宋体"}[satop]{lang="EN-US"}[中的分组携带]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x828463827}

[\[Sysname\] cem-class satop]{lang="EN-US"}

[\[Sysname-cem-satop\] rtp-header enable]{lang="EN-US"}
:::

::::: {#650863658 .myid}
[]{#_Toc404791558}[]{#struct_0_x4077_x5759_x2110890197}[]{#_Toc385403473}[]{#_Toc379982583}[]{#_Toc374974300}[]{#_Toc371347442}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- sequencing both**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_x967341729}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_x283208320}
:::

**[ ]{lang="EN-US"}**

[**[sequencing]{lang="EN-US"}[ both]{lang="EN-US"}**]{#struct_0_x4077_x5759_x159408274}[命令用来使能对]{style="font-family:宋体"}[PW]{lang="EN-US"}[上传送的报文进行排序处理。]{style="font-family:宋体"}

[**[undo sequencing both]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1386637466}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_543203463}

[**[sequencing both]{lang="EN-US"}**]{#struct_0_x4077_x5759_2040213932}

[**[undo sequencing both]{lang="EN-US"}**]{#struct_0_x4077_x5759_1263387255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1039500329}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_704713846}[上传送的报文不进行排序处理。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_63491847}

[[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x89956153}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x967407265}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_2020888967}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_320523061}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1781734181}

[**[both]{lang="EN-US"}**]{#struct_0_x4077_x5759_2130987396}[：]{style="font-family:宋体"}[PW]{lang="EN-US"}[收发两个方向都要进行排序处理。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1686132361}

[[在分组交换中，当转发负载比较重或者网络中有多条传送路径进行负载分担时，报文的传送可能会发生乱序，此时需要对传送的分组进行排序处理，即在发送端为每一个在]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_1857977920}[上传送的分组添加一个序列号，接收端根据序列号进行重新排序。]{style="font-family:宋体"}

[[本命令的配置不与对端协商，如果本地开启排序处理，则]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x459476053}[上传送的分组携带序列号，且对从]{style="font-family:宋体"}[PW]{lang="EN-US"}[上收到的分组进行排序处理。如果本端未开启排序处理，当收到的分组携带序列号时，则忽略该序列号，不对分组进行排序处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1392363798}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x1419949539}[配置对引用]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[上传送的报文进行排序处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x967472801}

[\[Sysname\] pw-class aaa]{lang="EN-US"}

[\[Sysname-pwc-aaa\] sequencing both]{lang="EN-US"}
:::::

::: {#-1902885513 .myid}
[]{#_Toc404791559}[]{#struct_0_x4077_x5759_728717686}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- service-instance**

------------------------------------------------------------------------

[**[service-instance]{lang="EN-US"}**]{#struct_0_x4077_x5759_1845249793}[命令用来创建以太网服务实例，并进入以太网服务实例视图。]{style="font-family:宋体"}

[**[undo service-instance]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1703322238}[命令用来删除指定的以太网服务实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1441676815}

[**[service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_x1331722255}

[**[undo service-instance ]{lang="EN-US"}***[instance-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_56495196}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x932229875}

[[接口上不存在任何以太网服务实例。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1426723367}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_729307510}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4077_x5759_1474534648}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1431238964}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_611626150}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1719038659}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2025346559}

[*[instance-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_847946994}[：以太网服务实例的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2081737547}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_729373046}[在二层以太网接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上创建以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入以太网服务实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_694828636}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] service-instance 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1-srv1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x934647185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn service-instance]{lang="EN-US"}**]{#struct_0_x4077_x5759_x262372084}
:::

::: {#-765413528 .myid}
[]{#_Toc404791560}[]{#struct_0_x4077_x5759_x110687711}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- shutdown (交叉连接组视图)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x4077_x5759_157042553}[命令用来关闭当前的交叉连接组。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x4077_x5759_588157526}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_127446492}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x4077_x5759_728783219}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x4077_x5759_x44730955}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_170404453}

[[交叉连接组处于开启状态。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_474281560}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1464676455}

[[交叉连接组视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x671422352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x521999431}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1759779632}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_728848755}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_122731220}

[[关闭交叉连接组后，该交叉连接组下所有交叉连接将不能提供]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_1396317497}[服务。]{style="font-family:宋体"}

[[关闭交叉连接组功能通常用于暂时禁用]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x1339634332}[服务，但还需要再次启用该]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[服务的场景。关闭交叉连接组后，该交叉连接组所有已存在的配置保持不变。在关闭状态下还可以对交叉连接组进行配置。交叉连接组再次被开启后，基于最新的配置提供]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1640640967}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_x263669385}[关闭名为]{style="font-family:宋体"}[vpn2]{lang="EN-US"}[的交叉连接组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x836374191}

[\[Sysname\] xconnect-group vpn2]{lang="EN-US"}

[\[Sysname-xcg-vpn2\] shutdown]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728914291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn xconnect-group]{lang="EN-US"}**]{#struct_0_x4077_x5759_2067559576}
:::

::: {#-1174850195 .myid}
[]{#_Toc404791561}[]{#struct_0_x4077_x5759_x967669409}[]{#_Toc385403476}[]{#_Toc384916659}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- shutdown (电路仿真接口视图)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x4077_x5759_2084827465}[命令用来关闭电路仿真接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x4077_x5759_x1393375296}[命令用来打开电路仿真接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_855366430}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x4077_x5759_8612875}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x4077_x5759_x967734945}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2003432399}

[[电路仿真接口处于打开状态。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_910700208}

[]{#struct_0_x4077_x5759_x333817788}[[【视图】]{style="font-family:黑体"}]{#_Toc384916660}

[[电路仿真接口视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x383417010}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1996578118}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1331061370}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_521773189}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1006927910}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_659587221}[关闭电路仿真接口]{style="font-family:宋体"}[Circuit-Emulation2/3/0:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x930721032}

[\[Sysname\] interface circuit-emulation 2/3/0:0]{lang="EN-US"}

[\[Sysname-Circuit-Emulation2/3/0:0\] shutdown]{lang="EN-US"}
:::

::: {#1273103123 .myid}
[]{#_Toc404791562}[]{#struct_0_x4077_x5759_x546040014}[]{#_Toc339307317}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- site**

------------------------------------------------------------------------

[**[site]{lang="EN-US"}**]{#struct_0_x4077_x5759_x793112470}[命令用来创建本地站点，并进入站点视图。]{style="font-family:宋体"}

[**[undo site]{lang="EN-US"}**]{#struct_0_x4077_x5759_x972931992}[命令用来删除指定的本地站点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1448374702}

[**[site ]{lang="EN-US"}***[site-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **range** *range-value* \] \[ **default-offset** *defalut-offset* \]]{lang="EN-US"}]{#struct_0_x4077_x5759_x1455053681}

[**[undo site]{lang="EN-US"}**[ *site-id*]{lang="EN-US"}]{#struct_0_x4077_x5759_1900399281}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728979827}

[[设备上不存在任何本地站点。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x235685814}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x652895283}

[[交叉连接组自动发现视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x361059315}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x542117854}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_661899710}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1808966431}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_52279574}

[*[site-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_1154002685}[：本地站点的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[250]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[range ]{lang="EN-US"}***[range-value]{lang="EN-US"}*]{#struct_0_x4077_x5759_728521075}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内最多包含的站点数目。]{style="font-family:宋体"}*[range-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}*[site-id]{lang="EN-US"}*[的最大值＋]{style="font-family:宋体"}[1]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[default-offset ]{lang="EN-US"}***[defalut-offset]{lang="EN-US"}*]{#struct_0_x4077_x5759_1992973741}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中站点的起始编号。]{style="font-family:宋体"}*[defalut-offset]{lang="EN-US"}*[为起始编号，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的站点从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始编号；取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的站点从]{style="font-family:宋体"}[1]{lang="EN-US"}[开始编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1930557881}

[**[range ]{lang="EN-US"}***[range-value]{lang="EN-US"}*]{#struct_0_x4077_x5759_x368789841}[和]{style="font-family:宋体"}**[default-offset ]{lang="FR"}***[default-offset]{lang="FR"}*[参数决定了]{style="font-family:宋体"}[PE]{lang="EN-US"}[为当前站点分配的标签块：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[第一次执行]{style="font-family:宋体"}**[site]{lang="EN-US"}**]{#struct_0_x4077_x5759_728652147}[命令时指定]{style="font-family:宋体"}*[range-value]{lang="EN-US"}*[为]{style="font-family:宋体"}*[range]{lang="FR"}[1]{lang="FR"}*[，则分配第一个标签块，其]{style="font-family:宋体"}[LR]{lang="FR"}[为]{style="font-family:宋体"}*[range]{lang="FR"}[1]{lang="FR"}*[，]{style="font-family:宋体"}[LO]{lang="FR"}[为]{style="font-family:宋体"}*[default-offset]{lang="FR"}*[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[再次执行]{style="font-family:宋体"}**[site]{lang="EN-US"}**]{#struct_0_x4077_x5759_728717683}[命令时将]{style="font-family:宋体"}*[range-value]{lang="EN-US"}*[增加为]{style="font-family:宋体"}*[range]{lang="FR"}[2]{lang="FR"}*[（大于]{style="font-family:宋体"}*[range]{lang="FR"}[1]{lang="FR"}*[），则分配第二个标签块，]{style="font-family:宋体"}[LR]{lang="FR"}[为]{style="font-family:宋体"}*[range]{lang="FR"}[2]{lang="FR"}*[－]{style="font-family:宋体"}*[range]{lang="FR"}[1]{lang="FR"}*[，]{style="font-family:宋体"}[LO]{lang="FR"}[为]{style="font-family:宋体"}*[range1]{lang="FR"}*[＋]{style="font-family:宋体"}*[default-offset]{lang="FR"}*[。以此类推。]{style="font-family:宋体"}

[[例如，在]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x4077_x5759_1845249798}[上先后执行如下命令，则]{style="font-family:宋体"}[PE]{lang="EN-US"}[分配三个标签块，分别为：]{style="font-family:宋体"}[LB1/0/10]{lang="EN-US"}[、]{style="font-family:宋体"}[LB2/10/12]{lang="EN-US"}[、]{style="font-family:宋体"}[LB3/22/14]{lang="EN-US"}[。其中，]{style="font-family:宋体"}[LB1]{lang="EN-US"}[、]{style="font-family:宋体"}[LB2]{lang="EN-US"}[、]{style="font-family:宋体"}[LB3]{lang="EN-US"}[为]{style="font-family:宋体"}[PE]{lang="EN-US"}[自动选取的标签值。]{style="font-family:宋体"}

[[site 1 range 10 default-offset 0]{lang="EN-US"}]{#struct_0_x4077_x5759_x1703649918}

[site 1 range 22]{lang="EN-US"}

[site 1 range 36]{lang="EN-US"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1775939108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个交叉连接组下，可以创建]{style="font-family:宋体"}]{#struct_0_x4077_x5759_729307507}[ID]{lang="EN-US"}[不同的多个本地站点。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[允许在]{lang="EN-US" style="font-family:宋体"}*[site-id]{lang="EN-US"}*]{#struct_0_x4077_x5759_x481780487}[和]{lang="EN-US" style="font-family:宋体"}*[defalut-offset]{lang="EN-US"}*[不改变的情况下，通过重复执行]{lang="EN-US" style="font-family:宋体"}**[site]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[来]{style="font-family:宋体"}[增大此站点的]{lang="EN-US" style="font-family:宋体"}[range]{lang="EN-US"}[值，但不允许将]{lang="EN-US" style="font-family:宋体"}[range]{lang="EN-US"}[改小。要想将]{lang="EN-US" style="font-family:宋体"}[range]{lang="EN-US"}[改小，则需要删除这个站点，并重新创建。]{lang="EN-US" style="font-family:宋体"}[建议根据对]{style="font-family:宋体"}[VPN]{lang="EN-US"}[规模发展的预计，把]{style="font-family:宋体"}**[range]{lang="FR"}**[ ]{lang="FR"}*[range-value]{lang="EN-US"}*[设置得比实际需要大一些。这样当以后对]{style="font-family:宋体"}[VPN]{lang="EN-US"}[进行扩容，增加]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中的站点数目时，就可以尽量少的修改配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能通过重复执行]{lang="EN-US" style="font-family:宋体"}**[site]{lang="EN-US"}**]{#struct_0_x4077_x5759_1718568213}[命令]{lang="EN-US" style="font-family:宋体"}[来]{style="font-family:宋体"}[修改]{lang="EN-US" style="font-family:宋体"}*[defalut-offset]{lang="EN-US"}*[。必须先通过]{lang="EN-US" style="font-family:宋体"}**[undo site]{lang="EN-US"}**[命令删除本地站点，再通过]{lang="EN-US" style="font-family:宋体"}**[site]{lang="EN-US"}**[命令创建本地站点，并指定新的]{lang="EN-US" style="font-family:宋体"}*[defalut-offset]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1476503896}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1628547336}[在名为]{style="font-family:宋体"}[bbb]{lang="EN-US"}[的交叉连接组下创建本地站点]{style="font-family:宋体"}[1]{lang="EN-US"}[，指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内最多包含的站点数目为]{style="font-family:宋体"}[30]{lang="EN-US"}[，站点的起始编号为]{style="font-family:宋体"}[0]{lang="EN-US"}[，并进入站点视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x618086750}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] site 1 range 30 default-offset 0]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto-1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x232408341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="EN-US"}**]{#struct_0_x4077_x5759_729373043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn xconnect-group]{lang="EN-US"}**]{#struct_0_x4077_x5759_694828641}[]{#_Toc336507504}
:::

::: {#1066584173 .myid}
[]{#_Toc404791563}[]{#struct_0_x4077_x5759_x354771324}[]{#_Toc389645001}[]{#_Toc378236132}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- snmp-agent trap enable l2vpn**

------------------------------------------------------------------------

[**[snmp-agent trap enable l2vpn]{lang="FR"}**]{#struct_0_x4077_x5759_x397443565}[命令用来开启]{style="font-family:宋体"}[L2VPN]{lang="FR"}[模块的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable l2vpn]{lang="FR"}**]{#struct_0_x4077_x5759_x354312572}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="FR"}[模块的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1984034567}

[**[snmp-agent trap enable l2vpn ]{lang="FR"}**]{#struct_0_x4077_x5759_x2089657405}[\[ **pw-up-down** \| **pw-delete** \] \*]{lang="FR"}

[**[undo snmp-agent trap enable l2vpn ]{lang="FR"}**]{#struct_0_x4077_x5759_x2037959518}[\[ **pw-up-down** \| **pw-delete** \] \*]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1286125438}

[[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_1946294445}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1562480208}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_913889121}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x354378108}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1225746688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_317534744}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1761250521}

[**[pw-up-down]{lang="FR"}**]{#struct_0_x4077_x5759_428828497}[：开启]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[up-down]{lang="EN-US"}[状态变化告警。]{style="font-family:宋体"}

[**[pw-delete]{lang="FR"}**]{#struct_0_x4077_x5759_850670884}[：开启]{style="font-family:宋体"}[PW]{lang="EN-US"}[删除告警。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1413619133}

[[开启]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}]{#struct_0_x4077_x5759_x551455297}[模块的告警功能后，当]{style="font-family:宋体"}[PW]{lang="EN-US"}[状态发生变化时会产生告警信息。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x4077_x5759_x354443644}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1170904252}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1644889681}[开启]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[up-down]{lang="EN-US"}[状态变化告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x4077_x5759_x1853924280}

[\[Sysname\] snmp-agent trap enable l2vpn pw-up-down]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1037336961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display snmp-agent trap-list]{lang="NO-BOK"}**]{#struct_0_x4077_x5759_85142534}[（网络管理和监控命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[SNMP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-655052582 .myid}
[]{#_Toc404791564}[]{#struct_0_x4077_x5759_2044762210}[]{#_Toc389645002}[]{#_Toc378236133}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- statistics enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20L2VPN命令.files/image001.png){#图片 16 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4077_x5759_x354509180}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4077_x5759_342893231}
:::

[ ]{lang="EN-US"}

[**[statistics enable]{lang="FR"}**]{#struct_0_x4077_x5759_x892988562}[命令用来开启指定]{style="font-family:宋体"}[PW]{lang="FR"}[的统计功能。]{style="font-family:宋体"}

[**[undo statistics enable]{lang="FR"}**]{#struct_0_x4077_x5759_1015906732}[命令用来关闭指定]{style="font-family:宋体"}[PW]{lang="FR"}[的统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2049109299}

[**[statistics enable]{lang="FR"}**]{#struct_0_x4077_x5759_247222382}

[**[undo statistics enable]{lang="FR"}**]{#struct_0_x4077_x5759_1085906141}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x2142543995}

[[通过命令行创建的]{style="font-family:宋体"}]{#struct_0_x4077_x5759_579407222}[PW]{lang="FR"}[未开启]{style="font-family:宋体"}[PW]{lang="FR"}[报文统计]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[通过]{style="font-family:
宋体"}[MIB]{lang="FR"}[创建的]{style="font-family:宋体"}[PW]{lang="FR"}[开启]{style="font-family:宋体"}[PW]{lang="FR"}[报文统计。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x354050428}

[[交叉连接]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1143337383}[PW]{lang="FR"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_544144618}

[[network-admin]{lang="FR"}]{#struct_0_x4077_x5759_x2138146900}

[[mdc-admin]{lang="FR"}]{#struct_0_x4077_x5759_x718092379}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1969166207}

[[备]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x218276239}[PW]{lang="FR"}[是否开启统计功能与其主]{style="font-family:宋体"}[PW]{lang="FR"}[保持一致，不需要单独]{style="font-family:宋体"}[开启或关闭备]{style="font-family:宋体"}[PW]{lang="EN-US"}[的统计功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x354115964}

[[\# ]{lang="FR"}]{#struct_0_x4077_x5759_420063993}[开启指定]{style="font-family:宋体"}[PW]{lang="FR"}[的报文统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x4077_x5759_x1085396701}

[\[Sysname\] xconnect-group vpws]{lang="FR"}

[\[Sysname-xcg-vpws\] connection ldp]{lang="EN-US"}

[\[Sysname-xcg-vpws-ldp\] peer 5.5.5.5 pw-id 120]{lang="EN-US"}

[\[Sysname-xcg-vpws-ldp-5.5.5.5-120\] statistics enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x564100699}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[reset l2vpn statistics pw]{lang="NO-BOK"}**]{#struct_0_x4077_x5759_x969203529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw]{lang="NO-BOK"}**]{#struct_0_x4077_x5759_1867611761}
:::::

::: {#95151371 .myid}
[]{#_Toc339307318}[]{#_Toc404791565}[]{#struct_0_x4077_x5759_639330926}[]{#_Toc342066786}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- tunnel-policy**

------------------------------------------------------------------------

[**[tunnel-policy]{lang="EN-US"}**]{#struct_0_x4077_x5759_541401368}[命令用来指定引用的隧道策略。]{style="font-family:宋体"}

[**[undo tunnel-policy]{lang="EN-US"}**]{#struct_0_x4077_x5759_1793234520}[命令用来取消引用隧道策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_172501848}

[**[tunnel-policy]{lang="EN-US"}**[ *tunnel-policy-name*]{lang="EN-US"}]{#struct_0_x4077_x5759_969398447}

[**[undo tunnel-policy]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1583789554}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728783220}

[[不引用任何隧道策略。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_1911584190}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1832441591}

[[自动发现交叉连接视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_77897731}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1295584689}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1401433199}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x640046587}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_851203263}

[*[tunnel-policy-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_728848756}[：隧道策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[19]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_122731219}

[[在自动发现交叉连接视图下执行本命令指定引用的隧道策略后，与该交叉连接关联的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x559997646}[将引用该隧道策略，即根据指定的隧道策略选择承载]{style="font-family:宋体"}[PW]{lang="EN-US"}[的公网隧道。]{style="font-family:宋体"}

[[如果没有引用隧道策略或者引用的隧道策略尚未配置，则]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x4077_x5759_x442318164}[根据缺省选择策略来选择公网隧道。缺省选择策略为按照]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道－]{style="font-family:宋体"}[\>GRE]{lang="EN-US"}[隧道－]{style="font-family:宋体"}[\>CR-LSP]{lang="EN-US"}[隧道的优先级顺序选择隧道，负载分担的隧道数目为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1565308363}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1414246168}[在自动发现交叉连接视图下，指定引用的隧道策略为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_728914292}

[\[Sysname\] tunnel-policy policy1]{lang="EN-US"}

[\[Sysname-tunnel-policy-policy1\] quit]{lang="EN-US"}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] site 2 range 10 default-offset 0]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto-2\] connection remote-site-id 3]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto-2-3\] tunnel-policy policy1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2067559577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel-policy]{lang="EN-US"}**]{#struct_0_x4077_x5759_x545974478}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道策略）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-595395675 .myid}
[]{#_Toc404791566}[]{#struct_0_x4077_x5759_x1840627901}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- vpn-target**

------------------------------------------------------------------------

[**[vpn-target]{lang="EN-US"}**]{#struct_0_x4077_x5759_x75196483}[命令用来为当前交叉连接组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo vpn-target]{lang="EN-US"}**]{#struct_0_x4077_x5759_763764866}[命令用来删除指定的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_850042692}

[**[vpn-target]{lang="EN-US"}**[ *vpn-target*&\<1-8\> \[ **both** \| **export-extcommunity** \| **import-extcommunity** \]]{lang="EN-US"}]{#struct_0_x4077_x5759_932587078}

[**[undo vpn-target]{lang="EN-US"}**[ { *vpn-target&\<1-8\>* \| **all** } \[ **both** \| **export-extcommunity** \| **import-extcommunity** \]]{lang="EN-US"}]{#struct_0_x4077_x5759_728979828}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x235685817}

[[没有为交叉连接组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x4077_x5759_x652829747}[方式指定]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x379051195}

[[交叉连接组自动发现视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_974359799}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1016849846}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x461800853}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_1871520195}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_728521076}

[*[vpn-target]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_x4077_x5759_1992973744}[：]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[属性值，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x4077_x5759_1930361273}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x4077_x5759_1941479586}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x4077_x5759_x59220787}[位自治系统号：]{style="font-family:宋体"}[16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。]{style="font-family:宋体"}[例如：]{lang="EN-US" style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x4077_x5759_x13329896}[：指定配置的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值同时作为]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[和]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[。没有指定]{style="font-family:宋体"}**[both]{lang="EN-US"}**[、]{style="font-family:宋体"}**[export-extcommunity]{lang="EN-US"}**[和]{style="font-family:宋体"}**[import-extcommunity]{lang="EN-US"}**[中的任何一个参数时，缺省值为]{style="font-family:宋体"}**[both]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[export-extcommunity]{lang="EN-US"}**]{#struct_0_x4077_x5759_2078770883}[：指定配置的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值为]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[import-extcommunity]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1467733921}[：指定配置的]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值为]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x4077_x5759_728586612}[：所有]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2002274344}

[[Route Target]{lang="EN-US"}]{#struct_0_x4077_x5759_458680719}[用来控制]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息（即标签块信息）的发布。本地]{style="font-family:宋体"}[PE]{lang="EN-US"}[在通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息将]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息（如本地]{style="font-family:宋体"}[Site ID]{lang="EN-US"}[、]{style="font-family:宋体"}[RD]{lang="EN-US"}[、标签块等）发送给远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[时，将]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息中携带的]{style="font-family:宋体"}[VPN target]{lang="EN-US"}[属性设置为]{style="font-family:宋体"}[Export target]{lang="EN-US"}[。远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[接收到]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息后，将该信息中携带的]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[属性与本地配置的]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[进行比较，如果二者中存在相同的值，则接收该信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x45891890}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_1238079430}[为交叉连接组]{style="font-family:宋体"}[bbb]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[方式配置]{style="font-family:宋体"}[Import Target]{lang="EN-US"}[为]{style="font-family:宋体"}[10:1 100:1 1000:1]{lang="EN-US"}[，]{style="font-family:宋体"}[Export Target]{lang="EN-US"}[为]{style="font-family:宋体"}[20:1 200:1 2000:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x1408809639}

[\[Sysname\] xconnect-group bbb]{lang="EN-US"}

[\[Sysname-xcg-bbb\] auto-discovery bgp]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] vpn-target 10:1 100:1 1000:1 import-extcommunity]{lang="EN-US"}

[\[Sysname-xcg-bbb-auto\] vpn-target 20:1 200:1 2000:1 export-extcommunity]{lang="EN-US"}
:::

::: {#2040829526 .myid}
[]{#_Toc404791567}[]{#struct_0_x4077_x5759_295150350}

**MPLS L2VPN \-- MPLS L2VPN配置命令 \-- xconnect-group**

------------------------------------------------------------------------

[**[xconnect-group]{lang="IT"}**]{#struct_0_x4077_x5759_728652148}[命令]{style="font-family:宋体"}[用来创建一个]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[交叉连接组，并进入交叉连接组视图。如果指定的交叉连接组已经存在，则直接进入交叉连接组视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4077_x5759_1869140460}**[xconnect-group]{lang="IT"}**[命令用来删除指定的交叉连接组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_517231535}

[**[xconnect-group ]{lang="IT"}**]{#struct_0_x4077_x5759_x2013036036}*[group-name]{lang="IT"}*

[**[undo]{lang="IT"}**]{#struct_0_x4077_x5759_1884541889}[ ]{lang="IT"}**[xconnect-group ]{lang="IT"}***[group-name]{lang="IT"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x62788750}

[[设备上不存在任何交叉连接组。]{style="font-family:宋体"}]{#struct_0_x4077_x5759_x1226339008}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_2144356196}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4077_x5759_728717684}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1845249791}

[[network-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1703191166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4077_x5759_x1632003309}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x600592227}

[*[group-name]{lang="EN-US"}*]{#struct_0_x4077_x5759_1758595086}[：交叉连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不能包含字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_208854382}

[[在同一个交叉连接组下，可以同时使用不同的方式（]{style="font-family:宋体"}[LDP]{lang="EN-US"}]{#struct_0_x4077_x5759_x2096105865}[、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[、静态方式）建立多条]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_x1301194794}

[[\# ]{lang="EN-US"}]{#struct_0_x4077_x5759_729307508}[创建名为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的交叉连接组，并进入交叉连接组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4077_x5759_x481780480}

[\[Sysname\] xconnect-group vpn1]{lang="EN-US"}

[\[Sysname-xcg-vpn1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4077_x5759_1719026965}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_x4077_x5759_x1639518624}**[xconnect-group]{lang="IT"}**

[ ]{lang="EN-US"}
:::
