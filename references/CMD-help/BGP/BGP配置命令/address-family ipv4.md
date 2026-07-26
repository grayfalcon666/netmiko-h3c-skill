::: {#-32210999 .myid}
[]{#_Toc404788593}[]{#struct_0_65458_x3406_1378928993}

**BGP \-- BGP配置命令 \-- address-family ipv4**

------------------------------------------------------------------------

[**[address-family ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_172855057}[命令用来创建]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族、]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族或]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播地址族，并进入相应地址族视图。]{style="font-family:宋体"}

[**[undo address-family ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_1495675705}[命令用来删除]{style="font-family:
宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族、]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族或]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播地址族，及相应地址族视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1127541482}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1216627159}[视图：]{style="font-family:宋体"}

[**[address-family ipv4]{lang="EN-US"}**[ \[ **multicast** \| **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x2099545735}

[**[undo address-family ipv4]{lang="EN-US"}**[ \[ **multicast** \| **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1518461776}

[[BGP-VPN]{lang="EN-US"}]{#struct_0_65458_x3406_1217085911}[实例视图：]{style="font-family:宋体"}

[**[address-family ipv4]{lang="EN-US"}**[ \[ **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1928929789}

[**[undo address-family ipv4]{lang="EN-US"}**[ \[ **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_1885726244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1069899851}

[[没有创建]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_380773002}[单播地址族、]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族和]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播地址族。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1538333577}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1387760089}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1047496951}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1127607018}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_432753705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1963502184}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1230554009}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族。如果在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下执行本命令并指定本参数，则进入]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图；如果在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下执行本命令并指定本参数，则进入]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_973169397}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播地址族。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_754373799}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x887102854}[单播地址族视图下的配置，只对公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族的路由和对等体生效。]{style="font-family:宋体"}

[[BGP-VPN IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_163404590}[单播地址族视图下的配置，只对指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族的路由和对等体生效。]{style="font-family:宋体"}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1217020375}[组播地址族视图下的配置，只对]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播地址族的路由和对等体生效。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x513342166}[和]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_638832147}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1127672554}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，创建]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族，并进入]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_58196893}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1771756249}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，创建]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族，并进入]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1675430954}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1216561630}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，创建]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播地址族，并进入]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x167079962}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 multicast]{lang="EN-US"}

[\[Sysname-bgp-mul-ipv4\]]{lang="EN-US"}
:::

::: {#-1195010413 .myid}
[]{#_Toc404788594}[]{#struct_0_65458_x3406_1232417919}

**BGP \-- BGP配置命令 \-- address-family ipv6**

------------------------------------------------------------------------

[**[address-family ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x1127738090}[命令用来创建]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族、]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族或]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播地址族，并进入相应地址族视图。]{style="font-family:宋体"}

[**[undo address-family ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x13847008}[命令用来删除]{style="font-family:
宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族、]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族或]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播地址族，及相应地址族视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1658184347}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1216496094}[视图：]{style="font-family:宋体"}

[**[address-family ipv6]{lang="EN-US"}**[ \[ **multicast** \| **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1732121122}

[**[undo address-family ipv6]{lang="EN-US"}**[ \[ **multicast** \| **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_846461293}

[[BGP-VPN]{lang="EN-US"}]{#struct_0_65458_x3406_828790348}[实例视图：]{style="font-family:宋体"}

[**[address-family ipv6]{lang="EN-US"}**[ \[ **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1126755050}

[**[undo address-family ipv6]{lang="EN-US"}**[ \[ **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1531058655}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1831633949}

[[没有创建]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1600406087}[单播地址族、]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族和]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播地址族。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_962739820}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_286979810}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1383816620}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1126820586}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x950358457}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_66361093}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1212429493}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族。如果在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下执行本命令并指定本参数，则进入]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图；如果在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下执行本命令并指定本参数，则进入]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1216365022}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址族。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2045326565}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x562070770}[单播地址族视图下的配置，只对公网]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族的路由和对等体生效。]{style="font-family:宋体"}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_343023710}[单播地址族视图下的配置，只对指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族的路由和对等体生效。]{style="font-family:宋体"}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1011376923}[组播地址族视图下的配置，只对]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播地址族的路由和对等体生效。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1216823774}[和]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1127279341}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_867983732}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，创建]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族，并进入]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_475305632}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1320725395}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，创建]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族，并进入]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1127344877}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1017685585}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，创建]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播地址族，并进入]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1216758238}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 multicast]{lang="EN-US"}

[\[Sysname-bgp-mul-ipv6\]]{lang="EN-US"}
:::

::: {#337432335 .myid}
[]{#_Toc404788595}[]{#struct_0_65458_x3406_x487447274}

**BGP \-- BGP配置命令 \-- advertise-rib-active**

------------------------------------------------------------------------

[**[advertise-rib-active]{lang="EN-US"}**]{#struct_0_65458_x3406_x1761041728}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表中的最优路由。]{style="font-family:宋体"}

[**[undo advertise-rib-active]{lang="EN-US"}**]{#struct_0_65458_x3406_626378311}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1049203472}

[**[advertise-rib-active]{lang="EN-US"}**]{#struct_0_65458_x3406_1876610942}

[**[undo advertise-rib-active]{lang="EN-US"}**]{#struct_0_65458_x3406_2026124481}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1589750630}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_793560018}[视图下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中的最优路由，不管该路由在]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表中是否为最优路由；其他视图下，与]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下的配置保持一致。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1127410413}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1363229357}[视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1046141996}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1399424406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x514609295}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1956379868}

[[配置]{style="font-family:宋体"}**[advertise-rib-active]{lang="EN-US"}**]{#struct_0_65458_x3406_x1461809810}[命令后可以保证发送出去的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由在]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表中是最优的，以减少]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发送的路由数量。]{style="font-family:宋体"}

[[以下路由不受]{style="font-family:宋体"}**[advertise-rib-active]{lang="EN-US"}**]{#struct_0_65458_x3406_x1740230641}[命令的影响：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x2002809718}[命令引入的路由]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[network]{lang="EN-US"}**]{#struct_0_65458_x3406_962151106}[命令发布的路由]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[default-route imported]{lang="EN-US"}**]{#struct_0_65458_x3406_x1127475949}[引入的缺省路由]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_675677778}[的路由]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNv]{lang="EN-US"}]{#struct_0_65458_x3406_1904268863}[6]{lang="EN-US"}[的路由]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1216692702}[组播路由]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x572449875}[组播路由]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x901461754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只对执行本命令后生成的路由生效。若想对执行本命令前生成的路由生效，则需要通过]{style="font-family:宋体"}]{#struct_0_65458_x3406_2133148276}**[reset bgp]{lang="EN-US"}**[命令复位]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1283042570}[视图和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播地址族视图下的配置不同时，以]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播地址族视图下的配置为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_528049664}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1863536684}[配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表中的最优路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x267120941}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] advertise-rib-active]{lang="EN-US"}

[[\# BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x595735079}[单播地址族视图下，配置发布]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表中的最优路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x562789351}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] advertise-rib-active]{lang="EN-US"}
:::

::: {#1984775158 .myid}
[]{#_Toc404788596}[]{#struct_0_65458_x3406_x752869187}[]{#_Toc263170083}[]{#_Toc261504175}[]{#_Toc180224161}[]{#_Toc138238232}

**BGP \-- BGP配置命令 \-- aggregate**

------------------------------------------------------------------------

[**[aggregate]{lang="PT-BR"}**]{#struct_0_65458_x3406_x229956783}[命令用来在]{style="font-family:宋体"}[BGP]{lang="PT-BR"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo aggregate]{lang="PT-BR"}**]{#struct_0_65458_x3406_x1127541485}[命令用来删除指定的聚合路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x6615488}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1385799088}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[aggregate]{lang="EN-US"}**[ *ip-address* { *mask* \| *mask-length* } \[ **as-set** \| **attribute-policy** *route-policy-name* \| **detail-suppressed** \| **origin-policy** *route-policy-name* \| **suppress-policy** *route-policy-name* \] \*]{lang="EN-US"}]{#struct_0_65458_x3406_1031423692}

[**[undo aggregate]{lang="EN-US"}**[ *ip-address* { *mask* \| *mask-length* }]{lang="EN-US"}]{#struct_0_65458_x3406_x692418247}[]{#_Hlt2478411}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1118928560}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[aggregate]{lang="EN-US"}**[ *ipv6-address prefix-length* \[ **as-set** \| **attribute-policy** *route-policy-name* \| **detail-suppressed** \| **origin-policy** *route-policy-name* \| **suppress-policy** *route-policy-name* \] \*]{lang="EN-US"}]{#struct_0_65458_x3406_1132697527}

[**[undo aggregate]{lang="EN-US"}**[ *ipv6-address prefix-length*]{lang="EN-US"}]{#struct_0_65458_x3406_x1806846202}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2051960003}

[[不会进行路由聚合。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1127607021}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1489495060}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_2009765783}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x334406071}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x503514782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_374129590}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x121840320}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_2076443102}[：聚合路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_1478663589}[：聚合路由的网络掩码，点分十进制格式[]{#_Hlt13301146}。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1127672557}[：聚合路由的网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_461481420}[：聚合路由的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1486831323}[：聚合路由的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[as-set]{lang="EN-US"}**]{#struct_0_65458_x3406_x395888428}[：指定聚合路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中包含所有具体路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径信息，该]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性为]{style="font-family:宋体"}[AS_SET]{lang="EN-US"}[类型，即属性中的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号没有顺序要求。如果没有指定本参数，则聚合路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中不会包含具体路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径信息，只包含当前路由器所在的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[**[attribute-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_65458_x3406_376472019}[：根据指定的路由策略设置聚合路由的属性。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[表示路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[detail-suppressed]{lang="EN-US"}**]{#struct_0_65458_x3406_836324195}[：指定仅通告聚合路由，不通告生成该聚合路由的具体路由。如果没有指定本参数，则同时通告聚合路由和生成该聚合路由的具体路由。]{style="font-family:宋体"}

[**[origin-policy]{lang="PT-BR"}**]{#struct_0_65458_x3406_x1826758097}[ *route-policy-name*]{lang="PT-BR"}[：根据指定的路由策略选择用于聚合的源路由，即仅选择符合路由策略的具体路由来生成聚合路由。]{style="font-family:宋体"}*[route-policy-name]{lang="PT-BR"}*[表示路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[suppress-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1792415467}[：根据指定的路由策略过滤具体路由，不通告通过路由策略过滤的具体路由，通告未通过路由策略过滤的具体路由。]{style="font-family:宋体"}*[route-policy-name]{lang="PT-BR"}*[表示路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1290246646}

[[本命令用来手动聚合]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x3770963}[路由。如果]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中存在属于指定的聚合路由的更具体的路由，即存在目的网络地址属于聚合路由的目的网络地址、且掩码长度大于聚合路由掩码长度的路由，则会在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中添加该聚合路由。例如，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中存在目的网络地址为]{style="font-family:宋体"}[10.1.1.0/24]{lang="EN-US"}[和]{style="font-family:宋体"}[10.1.2.0/24]{lang="EN-US"}[的路由，则配置]{style="font-family:宋体"}**[aggregate 10.1.0.0 16]{lang="EN-US"}**[命令后，会生成到达目的网络]{style="font-family:宋体"}[10.1.0.0/16]{lang="EN-US"}[的聚合路由。]{style="font-family:宋体"}

[[如果参与聚合的具体路由所包含的]{style="font-family:宋体"}[Origin]{lang="EN-US"}]{#struct_0_65458_x3406_x1127738093}[属性不同，那么聚合路由按照]{style="font-family:宋体"}[Incomplete]{lang="EN-US"}[、]{style="font-family:宋体"}[EGP]{lang="EN-US"}[、]{style="font-family:宋体"}[IGP]{lang="EN-US"}[的顺序选择]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性。例如，存在]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性为]{style="font-family:宋体"}[Incomplete]{lang="EN-US"}[和]{style="font-family:宋体"}[IGP]{lang="EN-US"}[的具体路由时，聚合路由的]{style="font-family:宋体"}[Origin]{lang="EN-US"}[属性为]{style="font-family:宋体"}[Incomplete]{lang="EN-US"}[。]{style="font-family:宋体"}

[[如果参与聚合的具体路由包含不同的团体属性（或扩展团体属性）值，且聚合后的路由中不包含]{style="font-family:宋体"}[ATOMIC_AGGREGATE]{lang="EN-US"}]{#struct_0_65458_x3406_389437519}[属性（原子聚合属性），则生成的聚合路由的团体属性（或扩展团体属性）中携带所有的团体属性（或扩展团体属性）值。]{style="font-family:宋体"}

[[本命令中各参数的用法及注意事项如]{style="font-family:宋体"}]{#struct_0_65458_x3406_1976479140}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?1984775158#_Ref313456633)[所示。]{style="font-family:宋体"}

[]{#struct_0_65458_x3406_253893388}[]{#_Ref313456633}[[表1-1 ]{lang="EN-US"}[参数的用法]{style="font-family:黑体"}]{#_Ref146010630}[及注意事项]{style="font-family:黑体"}

[]{#table_struct_0_x332279125}[[参数]{style="font-family:黑体"}]{#struct_0_65458_x3406_1344633827}
:::

[[用法及注意事项]{style="font-family:黑体"}]{#struct_0_65458_x3406_x901198089}

[**[as-set]{lang="EN-US"}**]{#struct_0_65458_x3406_899192239}

[[如果指定了该参数，则可以通过]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_1270778398}[属性中携带的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号避免路由环路。当聚合的具体路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径信息较多时，如果具体路由的变化较频繁，则指定]{style="font-family:宋体"}**[as-set]{lang="EN-US"}**[参数]{style="font-family:宋体"}[会导致聚合路由随之频繁改变，引起路由震荡。在这种情况下，不建议指定]{style="font-family:宋体"}**[as-set]{lang="EN-US"}**[参数]{style="font-family:宋体"}

[**[attribute-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1126755053}

[[该参数用来设置聚合路由的属性。通过]{style="font-family:宋体"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1197824700}[等方式也可以实现相同的功能]{style="font-family:宋体"}

[[该参数不能设置聚合路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x760403439}[属性]{style="font-family:宋体"}

[**[detail-suppressed]{lang="EN-US"}**]{#struct_0_65458_x3406_1097170711}

[[该参数用来抑制所有具体路由的通告。如果只想对一部分具体路由进行抑制，可以使用本命令中的]{style="font-family:宋体"}**[suppress-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1399478415}[参数或]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[ **filter-policy**]{lang="EN-US"}[命令]{style="font-family:宋体"}

[**[origin-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x272059568}

[[该参数用来通过路由策略选择生成聚合路由的具体路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1484724186}

[[如果某条路由属于聚合路由，但是该路由没有通过路由策略的过滤，则该路由不作为聚合路由的具体路由。路由通告时，该路由不受本命令中]{style="font-family:宋体"}**[detail-suppressed]{lang="EN-US"}**]{#struct_0_65458_x3406_x1126820589}[和]{style="font-family:宋体"}**[suppress-policy]{lang="EN-US"}**[参数的控制]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}]{#struct_0_65458_x3406_x997412624}**[origin-policy]{lang="PT-BR"}**[参数指定的路由策略中不需要配置]{style="font-family:宋体"}**[apply]{lang="PT-BR"}**[子句，即便配置了]{style="font-family:宋体"}**[apply]{lang="PT-BR"}**[子句，该子句也不会生效]{style="font-family:宋体"}

[**[suppress-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1416741647}

[[该参数用来抑制部分具体路由的通告。可以使用]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x641253754}[的]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[子句有选择地抑制一部分具体路由，其它具体路由仍被通告]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}**[suppress-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1902339059}[参数指定的路由策略中不需要配置]{style="font-family:宋体"}**[apply]{lang="PT-BR"}**[子句，即便配置了]{style="font-family:宋体"}**[apply]{lang="PT-BR"}**[子句，该子句也不会生效]{style="font-family:宋体"}

[ ]{lang="PT-BR"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2083704080}

[[\# BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1127279340}[单播地址族视图下，配置在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[1.1.0.0/16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x698100209}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] aggregate 1.1.0.0 255.255.0.0]{lang="EN-US"}

[[\# BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x390912607}[单播地址族视图下，配置在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[1.1.0.0/16]{lang="EN-US"}[，指定聚合路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中包含所有具体路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径信息，并抑制通告所有的具体路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_643579220}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] aggregate 1.1.0.0 255.255.0.0 as-set detail-suppressed]{lang="EN-US"}

[[\# BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1257840699}[单播地址族视图下，配置在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[1.1.0.0/16]{lang="EN-US"}[，设置聚合路由的团体属性为]{style="font-family:宋体"}[internet]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1555241868}

[\[Sysname\] route-policy commu permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-commu-0\] apply community internet]{lang="EN-US"}

[\[Sysname-route-policy-commu-0\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] aggregate 1.1.0.0 255.255.0.0 attribute-policy commu]{lang="EN-US"}

[[\# BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1127344876}[单播地址族视图下，配置在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[1.1.0.0/16]{lang="EN-US"}[，并配置生成聚合路由的源路由不能是]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1078636667}

[\[Sysname\] ip prefix-list spert deny 1.1.1.0 24]{lang="EN-US"}

[\[Sysname\] ip prefix-list spert permit 0.0.0.0 0 less-equal 32]{lang="EN-US"}

[\[Sysname\] route-policy srcrt permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-srcrt-0\] if-match ip address prefix-list spert]{lang="EN-US"}

[\[Sysname-route-policy-srcrt-0\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] aggregate 1.1.0.0 255.255.0.0 origin-policy srcrt]{lang="EN-US"}

[[\# BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x646778783}[单播地址族视图下，配置在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[1.1.0.0/16]{lang="EN-US"}[，并配置抑制发布具体路由]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1176914352}

[\[Sysname\] ip prefix-list spert permit 1.1.1.0 24]{lang="EN-US"}

[\[Sysname\] ip prefix-list spert deny 0.0.0.0 0 less-equal 32]{lang="EN-US"}

[\[Sysname\] route-policy suprt permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-suprt-0\] if-match ip address prefix-list spert]{lang="EN-US"}

[\[Sysname-route-policy-suprt-0\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] aggregate 1.1.0.0 255.255.0.0 suppress-policy suprt]{lang="EN-US"}

[[\# BGP-VPN IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1317163415}[单播地址族视图下，配置在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[1.1.0.0/16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1127410412}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] aggregate 1.1.0.0 255.255.0.0]{lang="EN-US"}

[[\# BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x202854584}[单播地址族视图下，配置在]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由表中创建一条聚合路由]{style="font-family:宋体"}[12::/64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x826751910}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] aggregate 12:: 64]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x288066025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp routing-table ipv4 multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1216430557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp routing-table ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_130624830}**[ unicast]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp routing-table ipv]{lang="EN-US"}**]{#struct_0_65458_x3406_229704860}**[6]{lang="EN-US"}[ multicast]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp routing-table ipv]{lang="EN-US"}**]{#struct_0_65458_x3406_x1306867452}**[6 unicast]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[summary automatic]{lang="EN-US"}**]{#struct_0_65458_x3406_x1127475948}

::::: {#-2115682295 .myid}
[]{#_Toc404788597}[]{#struct_0_65458_x3406_x890406163}[]{#_Toc263170084}[]{#_Toc261504176}[]{#_Toc180224162}[]{#_Toc138238233}[]{#_Toc44739955}[]{#_Toc43526985}

**BGP \-- BGP配置命令 \-- balance**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BGP命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_65458_x3406_x1280503967}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65458_x3406_385907743}
:::

[ ]{lang="EN-US"}

[**[balance]{lang="EN-US"}**]{#struct_0_65458_x3406_180087887}[命令用来配置进行]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担的路由条数。]{style="font-family:宋体"}

[**[undo balance]{lang="EN-US"}**]{#struct_0_65458_x3406_x1230780481}[命令用来取消]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x331909218}

[**[balance]{lang="EN-US"}**[ \[ **ebgp** \| **eibgp** \| **ibgp** \] *number*]{lang="EN-US"}]{#struct_0_65458_x3406_x1083174090}

[**[undo balance ]{lang="EN-US"}**[\[ **ebgp** \| **eibgp** \| **ibgp** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1127541484}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1559468453}

[[不会进行]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1488767329}[负载分担。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_386520292}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_2015507520}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1061982880}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1668108923}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1202344234}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1979162843}

[**[ebgp]{lang="EN-US"}**]{#struct_0_65458_x3406_x1077902846}[：为]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由配置进行负载分担的路由条数，即只在指定数目的]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由之间进行负载分担。]{style="font-family:宋体"}

[**[eibgp]{lang="EN-US"}**]{#struct_0_65458_x3406_x53258313}[：为]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[和]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由配置进行负载分担的路由条数，且可以在]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[和]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由之间进行负载分担。]{style="font-family:宋体"}

[**[ibgp]{lang="EN-US"}**]{#struct_0_65458_x3406_1000822543}[：为]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由配置进行负载分担的路由条数，即只在指定数目的]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由之间进行负载分担。]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1127607020}[：进行负载分担的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由条数。取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，表示不进行负载分担。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_76588881}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x420759186}[与]{style="font-family:宋体"}[IGP]{lang="EN-US"}[的负载分担不同，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[没有明确的度量值来决定是否对路由进行负载分担。]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的负载分担需要通过改变]{style="font-family:宋体"}[BGP]{lang="EN-US"}[选路规则来实现。]{style="font-family:宋体"}

[[当路由同时满足如下条件时，设备根据本命令配置的进行]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_22026998}[负载分担的路由条数，从这些路由中选择指定数目的路由进行负载分担：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_1558379490}[属性、]{lang="EN-US" style="font-family:宋体"}[LOCAL_PREF]{lang="EN-US"}[属性和]{lang="EN-US" style="font-family:宋体"}[MED]{lang="EN-US"}[属性完全相同。]{lang="EN-US" style="font-family:宋体"}[如果没有配置]{style="font-family:宋体"}**[balance as-path-neglect]{lang="EN-US"}**[命令，则要求]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}[也必须相同；如果配置了该命令，则]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}[可以不同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同为标签路由（具有对应]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2030676633}[MPLS]{lang="EN-US"}[标签值的路由）或同为非标签路由。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1077444095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令中]{style="font-family:宋体"}]{#struct_0_65458_x3406_x527984620}*[number]{lang="EN-US"}*[参数]{style="font-family:宋体"}[的取值范围和]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**[命令相关。通过]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**[命令配置系统支持的最大等价路由条数为]{style="font-family:宋体"}[m]{lang="EN-US"}[，并重启设备后，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[参数的取值范围将修改为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[m]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定]{style="font-family:宋体"}]{#struct_0_65458_x3406_x381846972}**[ebgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[eibgp]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ibgp]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}**[ebgp]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ibgp]{lang="EN-US"}**[，即同时为]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由和]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由配置进行负载分担的路由条数，但是不能在]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[和]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由之间进行负载分担。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}**[balance]{lang="EN-US"}**[ **eibgp** *number*]{lang="EN-US"}]{#struct_0_65458_x3406_x1077378559}[命令后，不能再执行]{style="font-family:宋体"}**[balance]{lang="EN-US"}**[ \[ **ebgp** \| **ibgp** \] *number*]{lang="EN-US"}[命令和]{style="font-family:宋体"}**[undo balance ]{lang="EN-US"}**[\[ **ebgp** \| **ibgp** \]]{lang="EN-US"}[命令；反之亦然。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1063071570}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_799262828}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担的路由条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[条。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1127672556}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] balance 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1104602521}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担的路由条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[条。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1602413620}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] balance 2]{lang="DA"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_272431304}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[balance as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_395580076}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_65458_x3406_x1338801016}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{style="font-family:宋体"}
:::::

::::: {#-1572055565 .myid}
[]{#_Toc404788598}[]{#struct_0_65458_x3406_610605857}

**BGP \-- BGP配置命令 \-- balance as-path-neglect**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BGP命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_65458_x3406_x801264836}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65458_x3406_1519239977}
:::

[ ]{lang="EN-US"}

[**[balance as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_x735758938}[命令用来配置不同]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性的路由能够形成]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担。]{style="font-family:宋体"}

[**[undo balance]{lang="EN-US"}[as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_1927513994}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x165048041}

[**[balance]{lang="EN-US"}**[ **as-path-neglect**]{lang="EN-US"}]{#struct_0_65458_x3406_x647464060}

[**[undo balance ]{lang="EN-US"}[as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_2031369959}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1170503865}

[[不同]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x1396124714}[属性的路由之间不能形成]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_650418313}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x915828377}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_767916022}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2060917599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2101376566}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1922826246}

[[执行]{style="font-family:宋体"}**[balance as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_1981885446}[命令后，只是在进行负载分担时忽略]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性，要使得两条或者两条以上的路由形成负载分担，还需要配置]{style="font-family:宋体"}**[balance]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[执行本命令后，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1204241035}[向外发布的路由只携带最佳路由的路由属性，参与负载分担的路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性丢失，因此，存在发生环路的风险。并且，执行本命令后，可能会对]{style="font-family:宋体"}[Netstream]{lang="EN-US"}[的统计信息造成影响。请谨慎使用本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1075778770}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1123449698}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置不同]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性的路由能够形成]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x44817945}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] balance as-path-neglect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1965348293}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置不同]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性的路由能够形成]{style="font-family:宋体"}[BGP]{lang="EN-US"}[负载分担。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1021364491}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] ]{lang="DA"}[balance as-path-neglect]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1147888016}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;
font-family:Symbol"}**[balance]{lang="EN-US"}**]{#struct_0_65458_x3406_606529445}
:::::

::: {#1067900633 .myid}
[]{#_Toc404788599}[]{#struct_0_65458_x3406_x1367379446}[]{#_Toc316655914}[]{#_Toc312414434}[]{#_Toc312402311}[]{#_Toc43895228}

**BGP \-- BGP配置命令 \-- bestroute as-path-neglect**

------------------------------------------------------------------------

[**[bestroute as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_x1127738092}[命令用来禁止路由器将]{style="font-family:
宋体"}[AS_PATH]{lang="EN-US"}[当作选路算法中的一个因素。]{style="font-family:
宋体"}

[**[undo bestroute as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_x1176646422}[命令用来允许路由器将]{style="font-family:
宋体"}[AS_PATH]{lang="EN-US"}[当作选路算法中的一个因素。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1951444283}

[**[bestroute as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_x735197017}

[**[undo bestroute as-path-neglect]{lang="EN-US"}**]{#struct_0_65458_x3406_1572045885}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2055377615}

[[路由器将]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_722921391}[当作选路算法中的一个因素。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_65458_x3406_1341416}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1169000333}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1126755052}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x368259241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1649012833}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1011571362}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1137151969}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，禁止路由器将]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[当作选路算法中的一个因素。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1698979741}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] bestroute as-path-neglect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1251603698}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，禁止路由器将]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[当作选路算法中的一个因素。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1126820588}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] bestroute as-path-neglect]{lang="EN-US"}
:::

::: {#2068881813 .myid}
[]{#_Toc404788600}[]{#struct_0_65458_x3406_568671317}

**BGP \-- BGP配置命令 \-- bestroute compare-med**

------------------------------------------------------------------------

[**[bestroute compare-med]{lang="EN-US"}**]{#struct_0_65458_x3406_1992684154}[命令用来配置对来自同一]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由进行]{style="font-family:宋体"}[MED]{lang="EN-US"}[排序优选。]{style="font-family:宋体"}

[**[undo bestroute compare-med]{lang="EN-US"}**]{#struct_0_65458_x3406_x41932078}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x70004156}

[**[bestroute compare-med]{lang="EN-US"}**]{#struct_0_65458_x3406_x1187355370}

[**[undo bestroute compare-med]{lang="EN-US"}**]{#struct_0_65458_x3406_1528423941}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251730650}

[[不会对来自同一]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_455091381}[的路由进行]{style="font-family:宋体"}[MED]{lang="EN-US"}[排序优选。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1432768268}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_777924689}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2125015319}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1033893392}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1516669109}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1045116191}

[[缺省情况下，系统不会对来自同一]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1324578802}[的路由进行]{style="font-family:宋体"}[MED]{lang="EN-US"}[排序优选，即]{style="font-family:宋体"}[BGP]{lang="EN-US"}[选择最优路由时是将新的路由和当前]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中的最优路由进行比较，只要新的路由比当前]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中的最优路由更优，新的路由将成为最优路由，路由学习的顺序有可能会影响最优路由的选择结果。]{style="font-family:宋体"}

[[如果执行了本命令，则路由器学习到新的路由后，首先按照路由来自的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1251796186}[分组，对来自同一]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由根据]{style="font-family:宋体"}[MED]{lang="EN-US"}[值的大小进行优选，选出]{style="font-family:宋体"}[MED]{lang="EN-US"}[值最小的路由，然后再对优选出来的、来自不同]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由进行优选，从而避免路由优选结果的不确定性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x716150522}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x280833509}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，设置在选择最佳路由时，对来自同一]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由进行]{style="font-family:宋体"}[MED]{lang="EN-US"}[排序优选。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_712954067}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] bestroute compare-med]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_753736126}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，设置在选择最佳路由时，对来自同一]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由进行]{style="font-family:宋体"}[MED]{lang="EN-US"}[排序优选。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1251861722}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] bestroute compare-med]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x324227216}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，设置在选择最佳路由时，对来自同一]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由进行]{style="font-family:宋体"}[MED]{lang="EN-US"}[排序优选。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_534285338}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] bestroute compare-med]{lang="EN-US"}
:::

::: {#1525011942 .myid}
[]{#_Toc404788601}[]{#struct_0_65458_x3406_x1199391545}[]{#_Toc316655916}[]{#_Toc316646814}[]{#_Toc261504179}[]{#_Toc180224165}[]{#_Toc138238236}[]{#_Toc94930899}[]{#_Toc94586631}[]{#_Toc60036249}[]{#_Toc53707193}[]{#_Toc53518666}[]{#_Toc50836973}[]{#_Toc50503930}[]{#_Toc43895232}[]{#_Toc299632316}

**BGP \-- BGP配置命令 \-- bestroute med-confederation**

------------------------------------------------------------------------

[**[bestroute med-confederation]{lang="EN-US"}**]{#struct_0_65458_x3406_39108390}[命令用来配置允许比较来自同一联盟不同子自治系统邻居路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[**[undo bestroute med-confederation]{lang="EN-US"}**]{#struct_0_65458_x3406_x2007685797}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251927258}

[**[bestroute med-confederation]{lang="EN-US"}**]{#struct_0_65458_x3406_x701041742}

[**[undo bestroute med-confederation]{lang="EN-US"}**]{#struct_0_65458_x3406_x400071404}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1135830297}

[[不比较来自同一联盟不同子自治系统邻居路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}]{#struct_0_65458_x3406_1966347290}[属性值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1994687525}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1393872132}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_508653168}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1907238042}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1251992794}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227242173}

[[只有]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x567599783}[里不包含联盟体外的自治系统编号时，才会比较来自同一联盟不同子自治系统邻居路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。例如，联盟中包含的子自治系统为]{style="font-family:宋体"}[65006]{lang="EN-US"}[、]{style="font-family:宋体"}[65007]{lang="EN-US"}[和]{style="font-family:宋体"}[65009]{lang="EN-US"}[。如果存在三条路由，它们的]{style="font-family:宋体"}[AS-PATH]{lang="EN-US"}[值分别为]{style="font-family:宋体"}[65006 65009]{lang="EN-US"}[、]{style="font-family:宋体"}[65007 65009]{lang="EN-US"}[和]{style="font-family:宋体"}[65008 65009]{lang="EN-US"}[，]{style="font-family:宋体"}[MED]{lang="EN-US"}[值分别为]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:
宋体"}[1]{lang="EN-US"}[，由于第三条路由包含了联盟体外的自治系统编号，因此在选择最优路由时第一条路由将成为最优路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1434849041}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1833379704}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置允许比较来自同一联盟不同子自治系统邻居路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1984644475}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] bestroute med-confederation]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1618561429}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，配置允许比较来自同一联盟不同子自治系统邻居路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1252058330}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] bestroute med-confederation]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x909522454}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，配置允许比较来自同一联盟不同子自治系统邻居路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_2230290}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] bestroute med-confederation]{lang="EN-US"}
:::

::: {#227487896 .myid}
[]{#_Toc404788602}[]{#struct_0_65458_x3406_x517208837}

**BGP \-- BGP配置命令 \-- bgp**

------------------------------------------------------------------------

[**[bgp]{lang="EN-US"}**]{#struct_0_65458_x3406_x559122735}[命令用来启动]{style="font-family:宋体"}[BGP]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo bgp]{lang="EN-US"}**]{#struct_0_65458_x3406_x1995110192}[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x83304397}

[**[bgp ]{lang="EN-US"}***[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_1252123866}

[**[undo bgp ]{lang="EN-US"}**[\[ *as-number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x802699485}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1733293281}

[[系统没有运行]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x334152381}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x514405570}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x796118924}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x369917749}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x364097054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1252189402}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1459377455}

[*[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x590547724}[：本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1843029342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一台路由器只能位于一个]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1460591695}[AS]{lang="EN-US"}[内，一台路由器上只能启动一个]{style="font-family:宋体"}[BGP]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由器支持四字节]{style="font-family:宋体"}]{#struct_0_65458_x3406_1237477560}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x785598780}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1153409018}[启动]{style="font-family:宋体"}[BGP]{lang="EN-US"}[，指定本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1251206362}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\]]{lang="EN-US"}
:::

::::: {#-1932568329 .myid}
[]{#_Toc136937990}[]{#_Toc99445939}[]{#_Toc34203772}[]{#_Toc33197996}[]{#_Toc312419366}[]{#_Toc404788603}[]{#struct_0_65458_x3406_1742667263}[]{#_Toc366658184}

**BGP \-- BGP配置命令 \-- bgp-policy accounting**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BGP命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_65458_x3406_x1876820858}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65458_x3406_1469635922}
:::

[ ]{lang="EN-US"}

[**[bgp-policy accounting]{lang="EN-US"}**]{#struct_0_65458_x3406_451254927}[命令用来在接口上开启]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费功能。]{style="font-family:宋体"}

[**[undo bgp-policy accounting]{lang="EN-US"}**]{#struct_0_65458_x3406_x1453776760}[命令用来在接口上关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x63361255}

[**[bgp-policy accounting]{lang="EN-US"}**[ { **input** \| **output** } \* \[ **source** \]]{lang="EN-US"}]{#struct_0_65458_x3406_687590415}

[**[undo bgp-policy accounting]{lang="EN-US"}**[ { **input** \| **output** } \* \[ **source** \]]{lang="EN-US"}]{#struct_0_65458_x3406_1742732799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x697017787}

[[接口上的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x582247981}[策略计费功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2098945520}

[[接口视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1123893506}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_226827321}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1742798335}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1608050761}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1626088431}

[**[input]{lang="EN-US"}**]{#struct_0_65458_x3406_644602042}[：表示入方向上的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费功能。]{style="font-family:宋体"}

[**[output]{lang="EN-US"}**]{#struct_0_65458_x3406_164963923}[：表示出方向上的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费功能。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_65458_x3406_1742208512}[：表示基于源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对]{style="font-family:宋体"}[IP]{lang="EN-US"}[流量进行分类统计。如果不指定本参数，则表示基于目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对]{style="font-family:宋体"}[IP]{lang="EN-US"}[流量进行分类统计。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_450029808}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x707087352}[策略计费功能利用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[丰富的路由属性（如下一跳、团体属性、]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[等），对]{style="font-family:宋体"}[IP]{lang="EN-US"}[流量进行分类，为同一类的流量分配相同的流量索引值，进而基于流量索引值对该类流量进行统计。]{style="font-family:宋体"}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1592020555}[策略计费对]{style="font-family:宋体"}[IP]{lang="EN-US"}[流量的分类统计方式有如下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基于源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_368924849}[地址：执行]{lang="EN-US" style="font-family:宋体"}**[bgp-policy accounting]{lang="EN-US"}**[命令时指定]{lang="EN-US" style="font-family:
宋体"}**[source]{lang="EN-US"}**[参数。采用该方式时，设备根据报文的源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址查找对应的路由，获取路由的流量索引值，根据该流量索引值判断报文所属的流量，并进行统计。]{lang="EN-US" style="font-family:宋体"}[该方式用来对特定源发送的流量进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基于目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1644377634}[地址：执行]{lang="EN-US" style="font-family:宋体"}**[bgp-policy accounting]{lang="EN-US"}**[命令时不指定]{lang="EN-US" style="font-family:
宋体"}**[source]{lang="EN-US"}**[参数。]{lang="EN-US" style="font-family:宋体"}[采用该方式时，设备根据报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址查找对应的路由，获取路由的流量索引值，根据该流量索引值判断报文所属的流量，并进行统计。该方式用来对发往特定目的的流量进行统计。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1742274048}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_65458_x3406_471298479}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_389398845}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上开启基于源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的入方向和出方向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_993897009}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bgp-policy accounting input output source]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2135018491}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1449021757}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上开启基于源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的入方向和出方向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1742339584}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] bgp-policy accounting input output source]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1126605469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aggregate]{lang="EN-US"}**]{#struct_0_65458_x3406_x865222425}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply traffic-index]{lang="EN-US"}**]{#struct_0_65458_x3406_x1949038122}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_340262485}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_65458_x3406_1742405120}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer default-route-advertise]{lang="EN-US"}**]{#struct_0_65458_x3406_1261626754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_20844327}
:::::

::: {#917281172 .myid}
[]{#_Toc263170090}[]{#_Toc261504182}[]{#_Toc180224168}[]{#_Toc404788604}[]{#struct_0_65458_x3406_x314480205}[]{#_Toc316655918}[]{#_Toc312414438}[]{#_Toc312402315}[]{#_Toc138238238}

**BGP \-- BGP配置命令 \-- compare-different-as-med**

------------------------------------------------------------------------

[**[compare-different-as-med]{lang="EN-US"}**]{#struct_0_65458_x3406_542233245}[命令用来配置允许比较来自不同]{style="font-family:
宋体"}[AS]{lang="EN-US"}[路由的]{style="font-family:
宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[**[undo compare-different-as-med]{lang="EN-US"}**]{#struct_0_65458_x3406_x452654022}[命令用来禁止对来自不同]{style="font-family:
宋体"}[AS]{lang="EN-US"}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值进行比较。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2142691235}

[**[compare-different-as-med]{lang="EN-US"}**]{#struct_0_65458_x3406_1224523296}

[**[undo compare-different-as-med]{lang="EN-US"}**]{#struct_0_65458_x3406_x1216114409}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_310225933}

[[不允许比较来自不同]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1251271898}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_864989359}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x908400190}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x814681751}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1798856263}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_548552928}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1495414414}

[[当一个]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1154602348}[路由器通过不同的]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体得到目的地址相同但下一跳不同的多条路由时，在其它条件相同的情况下，将优先选择]{style="font-family:宋体"}[MED]{lang="EN-US"}[值较小者作为最佳路由。]{style="font-family:宋体"}

[[通常情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1185562462}[只比较来自同一个]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。在某些特殊的应用中，如需强制]{style="font-family:宋体"}[BGP]{lang="EN-US"}[比较来自不同]{style="font-family:宋体"}[AS]{lang="EN-US"}[的路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值，则需要执行]{style="font-family:宋体"}**[compare-different-as-med]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[需要注意的是，除非能够确认不同的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1251730651}[采用了同样的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[和路由选择方式，否则不要使用此命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_455156917}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_76103796}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，允许比较来自不同]{style="font-family:宋体"}[AS]{lang="EN-US"}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1118840030}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] compare-different-as-med]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1941505054}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，允许比较来自不同]{style="font-family:宋体"}[AS]{lang="EN-US"}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_363128159}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] compare-different-as-med]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1251796187}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，允许比较来自不同]{style="font-family:宋体"}[AS]{lang="EN-US"}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[属性值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x716084986}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] compare-different-as-med]{lang="EN-US"}
:::

::: {#1976323699 .myid}
[]{#_Toc404788605}[]{#struct_0_65458_x3406_x219044836}

**BGP \-- BGP配置命令 \-- confederation id**

------------------------------------------------------------------------

[**[confederation id]{lang="EN-US"}**]{#struct_0_65458_x3406_x1942576090}[命令用来配置联盟的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo confederation id]{lang="EN-US"}**]{#struct_0_65458_x3406_x414906769}[命令用来取消配置的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[联盟]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_597867570}

[**[confederation id ]{lang="EN-US"}***[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1911324006}

[**[undo confederation id]{lang="EN-US"}**]{#struct_0_65458_x3406_2120297511}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251861723}

[[未配置联盟的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x324292752}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1077614105}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1376189190}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x401400978}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_380563815}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x711868283}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1623750656}

[*[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_184890233}[：联盟]{style="font-family:宋体"}[ID]{lang="EN-US"}[，即标识联盟这一整体的自治系统号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251927259}

[[联盟是指将一个大的自治系统划分为几个较小的子自治系统，每个子自治系统中均保持]{style="font-family:宋体"}[IBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x701107278}[全连接的状态，这些子自治系统组成一个联盟体。路由的一些关键属性（如下一跳、]{style="font-family:宋体"}[MED]{lang="EN-US"}[、本地优先级）在通过每个子自治系统时没有丢弃，因此每个子自治系统之间虽然存在]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[关系，但是从联盟外部来看这些子自治系统是一个整体，即一个自治系统，这个自治系统的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号就是联盟]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[采用联盟的方法既可以保证自治系统的完整性，同时还可以缓解自治系统中]{style="font-family:宋体"}[IBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x419869012}[连接数过多的问题。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_290259805}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[属于同一个联盟的所有路由器上，都需要配置相同的联盟]{style="font-family:宋体"}]{#struct_0_65458_x3406_382516327}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在联盟外的]{style="font-family:宋体"}]{#struct_0_65458_x3406_956467479}[BGP]{lang="EN-US"}[路由器看来，联盟体内路由器的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为联盟]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x592821354}

[[\# ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1213025782}[号是]{style="font-family:宋体"}[9]{lang="EN-US"}[的联盟体由]{style="font-family:宋体"}[38]{lang="EN-US"}[、]{style="font-family:宋体"}[39]{lang="EN-US"}[、]{style="font-family:宋体"}[40]{lang="EN-US"}[、]{style="font-family:宋体"}[41]{lang="EN-US"}[四个子自治系统组成；对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[是子自治系统]{style="font-family:宋体"}[38]{lang="EN-US"}[中的成员；对等体]{style="font-family:宋体"}[200.1.1.1]{lang="EN-US"}[是]{style="font-family:宋体"}[AS]{lang="EN-US"}[联盟体的外部成员，属于]{style="font-family:宋体"}[AS 98]{lang="EN-US"}[；对于外部成员来讲，]{style="font-family:宋体"}[9]{lang="EN-US"}[号联盟体就是一个统一的自治系统，该自治系统的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[9]{lang="EN-US"}[。以子自治系统]{style="font-family:宋体"}[41]{lang="EN-US"}[为例，子自治系统中路由器的配置如下。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1251992795}

[\[Sysname\] bgp 41]{lang="EN-US"}

[\[Sysname-bgp\] confederation id 9]{lang="EN-US"}

[\[Sysname-bgp\] confederation peer-as 38 39 40]{lang="EN-US"}

[\[Sysname-bgp\] group Confed38 external]{lang="EN-US"}

[\[Sysname-bgp\] peer Confed38 as-number 38]{lang="EN-US"}

[\[Sysname-bgp\] peer 10.1.1.1 group Confed38]{lang="EN-US"}

[\[Sysname-bgp\] group Remote98 external]{lang="EN-US"}

[\[Sysname-bgp\] peer Remote98 as-number 98]{lang="EN-US"}

[\[Sysname-bgp\] peer 200.1.1.1 group Remote98]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227307709}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confederation nonstandard]{lang="EN-US"}**]{#struct_0_65458_x3406_x1303330968}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confederation peer-as]{lang="EN-US"}**]{#struct_0_65458_x3406_1323843439}
:::

::: {#-249751721 .myid}
[]{#_Toc404788606}[]{#struct_0_65458_x3406_241078442}[]{#_Toc263170091}[]{#_Toc261504183}[]{#_Toc180224169}[]{#_Toc138238240}[]{#_Toc32467732}[]{#_Toc32464201}[]{#_Toc30500445}[]{#_Toc26173936}[]{#_Toc290298113}

**BGP \-- BGP配置命令 \-- confederation nonstandard**

------------------------------------------------------------------------

[**[confederation nonstandard]{lang="EN-US"}**]{#struct_0_65458_x3406_2013514483}[命令用来配置设备可以与未遵循]{style="font-family:
宋体"}[RFC 3065]{lang="EN-US"}[实现联盟的路由器互通。]{style="font-family:宋体"}

[**[undo confederation nonstandard]{lang="EN-US"}**]{#struct_0_65458_x3406_1252058331}[命令用来恢复缺省配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x909456918}

[**[confederation nonstandard]{lang="EN-US"}**]{#struct_0_65458_x3406_x2020877673}

[**[undo confederation nonstandard]{lang="EN-US"}**]{#struct_0_65458_x3406_2072853039}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1397908452}

[[设备不能与未遵循]{style="font-family:宋体"}[RFC 3065]{lang="EN-US"}]{#struct_0_65458_x3406_x1853776071}[实现联盟的路由器互通，只能与遵循]{style="font-family:宋体"}[RFC 3065]{lang="EN-US"}[实现联盟的路由器互通。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1662024363}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x797104579}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x810026998}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1252123867}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x802765021}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_966342798}

[[如果联盟中存在未遵循]{style="font-family:宋体"}[RFC 3065]{lang="EN-US"}]{#struct_0_65458_x3406_1581621540}[的路由器，为了与其互通，保证联盟的正常建立，需要在联盟中所有遵循]{style="font-family:宋体"}[RFC 3065]{lang="EN-US"}[的[]{#_Hlt12072448}路由器上配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1927408582}

[[\# ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1701980100}[号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的联盟由]{style="font-family:宋体"}[64000]{lang="EN-US"}[、]{style="font-family:宋体"}[65000]{lang="EN-US"}[两个子自治系统组成，在该联盟内存在未遵循]{style="font-family:宋体"}[RFC 3065]{lang="EN-US"}[实现联盟的路由器。为了保证联盟的正常建立，在遵循]{style="font-family:宋体"}[RFC 3065]{lang="EN-US"}[的路由器上配置其可以与未遵循]{style="font-family:宋体"}[RFC 3065]{lang="EN-US"}[实现联盟的路由器互通。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1374645514}

[\[Sysname\] bgp 64000]{lang="EN-US"}

[\[Sysname-bgp\] confederation id 100]{lang="EN-US"}

[\[Sysname-bgp\] confederation peer-as 65000]{lang="EN-US"}

[\[Sysname-bgp\] confederation nonstandard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1252189403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confederation id]{lang="EN-US"}**]{#struct_0_65458_x3406_1459311919}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confederation peer-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x1446858598}
:::

::: {#-1605171733 .myid}
[]{#_Toc404788607}[]{#struct_0_65458_x3406_x951947285}[]{#_Toc263170092}[]{#_Toc261504184}[]{#_Toc180224170}[]{#_Toc138238241}

**BGP \-- BGP配置命令 \-- confederation peer-as**

------------------------------------------------------------------------

[**[confederation peer-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x283196743}[命令用来指定联盟中包含的子自治系统。]{style="font-family:宋体"}

[**[undo confederation peer-as]{lang="EN-US"}**]{#struct_0_65458_x3406_2104896921}[命令用来删除联盟中的子自治系统。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1728708505}

[**[confederation peer-as]{lang="EN-US"}**[ *as-number-list*]{lang="EN-US"}]{#struct_0_65458_x3406_1865668694}

[**[undo confederation peer-as]{lang="EN-US"}**[ \[ *as-number-list* \]]{lang="EN-US"}]{#struct_0_65458_x3406_1251206363}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314545741}

[[未指定属于联盟的子自治系统。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1027002285}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1161996367}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x849988901}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1134933643}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x384005997}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x533886204}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x536282656}

[*[as-number-list]{lang="EN-US"}*]{#struct_0_65458_x3406_1251271899}[：子自治系统号列表，在同一条命令中最多可配置]{style="font-family:宋体"}[32]{lang="EN-US"}[个子自治系统，表示方式为]{style="font-family:宋体"}*[as-number-list ]{lang="EN-US"}*[= a*s-number*&\<1-32\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[as-number]{lang="EN-US"}*[为子自治系统号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[；]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_865054895}

[[在配置本命令之前，必须通过]{style="font-family:宋体"}**[confederation id]{lang="EN-US"}**]{#struct_0_65458_x3406_936698665}[命令指定联盟]{style="font-family:宋体"}[ID]{lang="EN-US"}[，否则本命令配置不成功。]{style="font-family:宋体"}

[[执行]{style="font-family:宋体"}**[undo confederation peer-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x621597084}[命令时，如果不指定]{style="font-family:宋体"}*[as-number-list]{lang="EN-US"}*[参数，则表示删除联盟中所有的子自治系统；如果指定了]{style="font-family:宋体"}*[as-number-list]{lang="EN-US"}*[参数，则表示删除联盟中指定的子自治系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1076595877}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1237151184}[配置属于联盟]{style="font-family:宋体"}[10]{lang="EN-US"}[的子自治系统号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[和]{style="font-family:宋体"}[2001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_316205520}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] confederation id 10]{lang="EN-US"}

[\[Sysname-bgp\] confederation peer-as 2000 2001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251730648}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confederation id]{lang="EN-US"}**]{#struct_0_65458_x3406_454567092}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confederation nonstandard]{lang="EN-US"}**]{#struct_0_65458_x3406_148844438}
:::

::: {#1245918683 .myid}
[]{#_Toc404788608}[]{#struct_0_65458_x3406_x1177794206}[]{#_Toc307230761}[]{#_Toc290298116}

**BGP \-- BGP配置命令 \-- dampening**

------------------------------------------------------------------------

[**[dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_x2124955927}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减。]{style="font-family:宋体"}

[**[undo dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_x712954643}[命令用来取消]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1976523415}

[**[dampening]{lang="EN-US"}**[ \[ *half-life-reachable half-life-unreachable reuse suppress ceiling* \| **route-policy** *route-policy-name* \] \*]{lang="EN-US"}]{#struct_0_65458_x3406_1550992314}

[**[undo dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_470301362}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251796184}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x716019450}[路由衰减。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x690486798}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_919867235}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_993299672}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1841449684}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1429644083}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2058481389}

[*[half-life-reachable]{lang="EN-US"}*]{#struct_0_65458_x3406_85140302}[：发生振荡的可达路由的半衰期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[45]{lang="EN-US"}[，单位为分钟，缺省值为]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[*[half-life-unreachable]{lang="EN-US"}*]{#struct_0_65458_x3406_1251861720}[：发生振荡的不可达路由的半衰期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[45]{lang="EN-US"}[，单位为分钟，缺省值为]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[*[reuse]{lang="EN-US"}*]{#struct_0_65458_x3406_x324096144}[：路由的再使用阈值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[750]{lang="EN-US"}[。当惩罚值降低到该值以下时，此路由变为可用路由，参与路由选择。路由的再使用阈值必须小于]{style="font-family:宋体"}*[suppress]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[suppress]{lang="EN-US"}*]{#struct_0_65458_x3406_509286202}[：路由的抑制阈值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。当惩罚值超过该值时，此路由被抑制，不参与路由选择。]{style="font-family:宋体"}

[*[ceiling]{lang="EN-US"}*]{#struct_0_65458_x3406_x1893376755}[：惩罚值的上限，取值范围为]{style="font-family:宋体"}[1001]{lang="EN-US"}[～]{style="font-family:宋体"}[20000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[16000]{lang="EN-US"}[。惩罚值达到该值后，不再增加。惩罚值的上限必须大于]{style="font-family:宋体"}*[suppress]{lang="EN-US"}*[。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_2010628537}[：通过路由策略指定对哪些路由进行路由衰减。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1610244675}

[[该命令只对]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_1051697844}[路由生效，对]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1801581710}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1251927256}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减，可达路由和不可达路由的半衰期均为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟，路由的再使用阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，抑制阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[，惩罚值上限为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x700386382}

[\[Sysname\] bgp 100]{lang="EN-US"}

[]{#_Toc138238243}[]{#_Toc94930907}[]{#_Toc94586639}[]{#_Toc60036257}[]{#_Toc53707201}[]{#_Toc53518674}[]{#_Toc50836981}[]{#_Toc50503938}[]{#_Toc43895240}[]{#_Hlt7001923}[]{#_Hlt9148270}[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] dampening 10 10 1000 2000 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1953094222}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减，可达路由和不可达路由的半衰期均为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟，路由的再使用阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，抑制阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[，惩罚值上限为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1157147993}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] dampening 10 10 1000 2000 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x2107711984}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由衰减，可达路由和不可达路由的半衰期均为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟，路由的再使用阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，抑制阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[，惩罚值上限为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1251992792}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] dampening 10 10 1000 2000 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1226848957}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减，可达路由和不可达路由的半衰期均为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟，路由的再使用阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，抑制阈值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[，惩罚值上限为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_989517747}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] dampening 10 10 1000 2000 10000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_23718708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp dampening parameter]{lang="EN-US"}**]{#struct_0_65458_x3406_x1246878495}
:::

::: {#1290786188 .myid}
[]{#_Toc404788609}[]{#struct_0_65458_x3406_x907259515}[]{#_Toc316655923}[]{#_Toc312414443}[]{#_Toc312402319}[]{#_Toc138238244}[]{#_Toc366152610}[]{#_Toc366166353}[]{#_Toc366219889}[]{#_Toc302638025}

**BGP \-- BGP配置命令 \-- default local-preference**

------------------------------------------------------------------------

[**[default local-preference]{lang="EN-US"}**]{#struct_0_65458_x3406_1252058328}[命令用来配置本地优先级的缺省值。]{style="font-family:
宋体"}

[**[undo default local-preference]{lang="EN-US"}**]{#struct_0_65458_x3406_x908998165}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x438921575}

[**[default local-preference]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_65458_x3406_432565848}

[**[undo default local-preference]{lang="EN-US"}**]{#struct_0_65458_x3406_1263518835}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1924312656}

[[本地优先级的缺省值为]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_65458_x3406_1541020982}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x389921843}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x494421530}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1252123864}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x802568413}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x201484772}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x316750893}

[*[value]{lang="EN-US"}*]{#struct_0_65458_x3406_x317926711}[：本地优先级的缺省值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。该值越大，则优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x333792199}

[[除本命令外，还可以通过路由策略中的]{style="font-family:宋体"}**[apply local-preference]{lang="EN-US"}**]{#struct_0_65458_x3406_x22557707}[命令来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的本地优先级。如果没有配置路由策略，则所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的本地优先级均为本命令配置的值；如果配置了路由策略，则通过路由策略过滤的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的本地优先级为]{style="font-family:宋体"}**[apply local-preference]{lang="EN-US"}**[命令配置的值，未通过路由策略过滤的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的本地优先级为本命令配置的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1909820577}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1173413145}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置本地优先级的缺省值为]{style="font-family:宋体"}[180]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1252189400}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] default local-preference 180]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1459246383}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置本地优先级的缺省值为]{style="font-family:宋体"}[180]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_952527273}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] default local-preference 180]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x24626466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply local-preference]{lang="EN-US"}**]{#struct_0_65458_x3406_x1635566022}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_2095816142}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}
:::

::: {#757059416 .myid}
[]{#_Toc404788610}[]{#struct_0_65458_x3406_1251206360}[]{#_Toc316655924}[]{#_Toc312414444}[]{#_Toc312402320}[]{#_Toc180224174}

**BGP \-- BGP配置命令 \-- default med**

------------------------------------------------------------------------

[**[default med]{lang="EN-US"}**]{#struct_0_65458_x3406_x314611277}[命令用来配置]{style="font-family:宋体"}[MED]{lang="EN-US"}[的缺省值。]{style="font-family:宋体"}

[**[undo default med]{lang="EN-US"}**]{#struct_0_65458_x3406_2118475333}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x802662660}

[**[default med]{lang="EN-US"}**[ *med-value*]{lang="EN-US"}]{#struct_0_65458_x3406_x1338242960}

[**[undo default med]{lang="EN-US"}**]{#struct_0_65458_x3406_159159939}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1462550883}

[[MED]{lang="EN-US"}]{#struct_0_65458_x3406_1001906414}[的缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_636947450}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1251271896}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_865906863}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1934812018}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1832190648}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1121411790}

[*[med-value]{lang="EN-US"}*]{#struct_0_65458_x3406_x252008450}[：]{style="font-family:宋体"}[MED]{lang="EN-US"}[的缺省值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x89549192}

[[可以通过多种方式配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1446530676}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值，按照优先级从高到底的顺序依次为：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[通过路由策略中的]{style="font-family:宋体"}]{#struct_0_65458_x3406_1251730649}**[apply cost]{lang="EN-US"}**[命令设置的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值；]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[通过]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_454632628}[命令中的]{style="font-family:宋体"}**[med]{lang="EN-US"}**[参数设置的]{lang="EN-US" style="font-family:宋体"}[MED]{lang="EN-US"}[值；]{lang="EN-US" style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[通过]{style="font-family:宋体"}**[default med]{lang="EN-US"}**]{#struct_0_65458_x3406_388068121}[命令配置的]{lang="EN-US" style="font-family:宋体"}[MED]{lang="EN-US"}[值；]{lang="EN-US" style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[学习到的]{style="font-family:宋体"}]{#struct_0_65458_x3406_576250828}[BGP]{lang="EN-US"}[路由自身的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值，或引入的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由自身]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[metric]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1739678132}

[]{#struct_0_65458_x3406_817854515}[]{#_Toc138238246}[]{#_Toc94930910}[]{#_Toc94586642}[]{#_Toc60036260}[]{#_Toc53707204}[]{#_Toc53518677}[]{#_Toc50836984}[\# ]{lang="EN-US"}[在]{style="font-family:
宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[MED]{lang="EN-US"}[的缺省值为]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1268208617}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] default med 25]{lang="EN-US"}

[]{#struct_0_65458_x3406_1251796185}[[\# ]{lang="EN-US"}]{#_Toc50503941}[在]{style="font-family:
宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[MED]{lang="EN-US"}[的缺省值为]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x715953914}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] default med 25]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2037811921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply cost]{lang="EN-US"}**]{#struct_0_65458_x3406_1294615061}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x994658762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x2095611503}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}
:::

::: {#-567920257 .myid}
[]{#_Toc404788611}[]{#struct_0_65458_x3406_x1099868007}

**BGP \-- BGP配置命令 \-- default-route imported**

------------------------------------------------------------------------

[**[default-route imported]{lang="EN-US"}**]{#struct_0_65458_x3406_1251861721}[命令用来允许将缺省路由引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[**[undo default-route imported]{lang="EN-US"}**]{#struct_0_65458_x3406_x324161680}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1824164504}

[**[default-route imported]{lang="EN-US"}**]{#struct_0_65458_x3406_451828424}

[**[undo default-route imported]{lang="EN-US"}**]{#struct_0_65458_x3406_x707476789}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1936794977}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_991254971}[不允许将缺省路由引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_890131176}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_533115505}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251927257}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x700451918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1953667587}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x227254862}

[[执行]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x190239164}[命令引入]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由时，缺省情况下不会将]{style="font-family:宋体"}[IGP]{lang="EN-US"}[的缺省路由引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。如果执行]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**[命令的同时，执行了]{style="font-family:宋体"}**[default-route imported]{lang="EN-US"}**[命令，则]{style="font-family:宋体"}[IGP]{lang="EN-US"}[的缺省路由可以引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1940255734}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x179153620}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置允许将]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的缺省路由引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1251992793}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] default-route imported]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] import-route ospf 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1226914493}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，配置允许将]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的缺省路由引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1730191274}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] default-route imported]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] import-route ospf 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_147751879}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，配置允许将]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的缺省路由引入到]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1665503125}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] default-route imported]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] import-route ospfv3 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1051635963}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置允许将]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的缺省路由引入到]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1252058329}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] default-route imported]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] import-route ospfv3 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x908932629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x1161361265}
:::

::: {#-1366480728 .myid}
[]{#_Toc304292970}[]{#_Toc289499896}[]{#_Toc307230763}[]{#_Toc404788612}[]{#struct_0_65458_x3406_x1946973941}

**BGP \-- BGP配置命令 \-- display bgp dampening parameter**

------------------------------------------------------------------------

[**[display bgp dampening parameter]{lang="EN-US"}**]{#struct_0_65458_x3406_1544000191}[命令用来显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1268925390}

[**[display bgp dampening parameter ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } { ]{lang="EN-US"}**[multicast ]{lang="EN-US"}**[\| \[ ]{lang="EN-US"}**[unicast ]{lang="EN-US"}**[\] \[ **vpn-instance** ]{lang="EN-US"}*[vpn-instance-name ]{lang="EN-US"}*[\] ]{lang="EN-US"}[}]{lang="EN-US"}]{#struct_0_65458_x3406_x1708549707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1252123865}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x802633949}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1699185395}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x2068125422}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x366088978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x505316475}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x2095326641}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_908990949}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1155567082}[：显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[路由的路由衰减参数。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x1155632618}[：显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[路由的路由衰减参数。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_2087571283}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播路由的路由衰减参数。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1632624551}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播路由的路由衰减参数。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1504077343}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减参数。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由衰减参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1252189401}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1459180847}[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x695851786}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_290304533}[显示公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的路由衰减参数。]{style="font-family:宋体"}

[[\<Sysname\> display bgp dampening parameter ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1174970765}

[Maximum suppression time (in seconds)              : 3973]{lang="EN-US"}

[Ceiling value                                      : 16000]{lang="EN-US"}

[Reuse value                                        : 750]{lang="EN-US"}

[Half-life time for reachable routes (in seconds)   : 900]{lang="EN-US"}

[Half-life time for unreachable routes (in seconds) : 900]{lang="EN-US"}

[Suppression threshold                              : 2000]{lang="EN-US"}

[]{#struct_0_65458_x3406_x1873178224}[]{#_Toc94753884}[]{#_Toc94671210}[]{#_Toc73952285}[[表1-2 ]{lang="EN-US"}[display bgp dampening parameter]{lang="EN-US"}]{#_Toc68319417}[命令]{style="font-family:黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x332650421}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1889484364}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251206361}

[[Maximum suppression time]{lang="EN-US"}]{#struct_0_65458_x3406_x314676813}

[[最大抑制时间，即惩罚值从上限下降到再使用阈值所需要的最大时间，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_573029396}

[[Ceiling value]{lang="EN-US"}]{#struct_0_65458_x3406_x906594067}

[[惩罚值的上限]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1406155855}

[[Reuse value]{lang="EN-US"}]{#struct_0_65458_x3406_x2057409209}

[[再使用阈值]{style="font-family:宋体"}]{#struct_0_65458_x3406_1251271897}

[[Half-life time for reachable routes]{lang="EN-US"}]{#struct_0_65458_x3406_865972399}

[[可达路由的半衰期，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_1546248382}

[[Half-life time for unreachable routes]{lang="EN-US"}]{#struct_0_65458_x3406_x2011240217}

[[不可达路由的半衰期，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_x12385023}

[[Suppression threshold]{lang="EN-US"}]{#struct_0_65458_x3406_x382074403}

[[抑制阈值]{style="font-family:宋体"}]{#struct_0_65458_x3406_1251730646}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_454960308}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_2143009525}

::: {#854974632 .myid}
[]{#_Toc404788613}[]{#struct_0_65458_x3406_x2080876940}[]{#_Toc366152615}[]{#_Toc366166358}[]{#_Toc366219894}[]{#_Toc366152616}[]{#_Toc366166359}[]{#_Toc366219895}[]{#_Toc366152617}[]{#_Toc366166360}[]{#_Toc366219896}[]{#_Toc366152618}[]{#_Toc366166361}[]{#_Toc366219897}[]{#_Toc366152619}[]{#_Toc366166362}[]{#_Toc366219898}[]{#_Toc366152620}[]{#_Toc366166363}[]{#_Toc366219899}[]{#_Toc366152621}[]{#_Toc366166364}[]{#_Toc366219900}[]{#_Toc366152622}[]{#_Toc366166365}[]{#_Toc366219901}[]{#_Toc366152623}[]{#_Toc366166366}[]{#_Toc366219902}[]{#_Toc366152624}[]{#_Toc366166367}[]{#_Toc366219903}[]{#_Toc366152625}[]{#_Toc366166368}[]{#_Toc366219904}[]{#_Toc366152626}[]{#_Toc366166369}[]{#_Toc366219905}[]{#_Toc366152627}[]{#_Toc366166370}[]{#_Toc366219906}[]{#_Toc366152628}[]{#_Toc366166371}[]{#_Toc366219907}[]{#_Toc366152629}[]{#_Toc366166372}[]{#_Toc366219908}[]{#_Toc366152630}[]{#_Toc366166373}[]{#_Toc366219909}[]{#_Toc366152631}[]{#_Toc366166374}[]{#_Toc366219910}[]{#_Toc366152632}[]{#_Toc366166375}[]{#_Toc366219911}[]{#_Toc366152633}[]{#_Toc366166376}[]{#_Toc366219912}[]{#_Toc366152634}[]{#_Toc366166377}[]{#_Toc366219913}[]{#_Toc366152635}[]{#_Toc366166378}[]{#_Toc366219914}[]{#_Toc366152636}[]{#_Toc366166379}[]{#_Toc366219915}[]{#_Toc366152637}[]{#_Toc366166380}[]{#_Toc366219916}[]{#_Toc366152638}[]{#_Toc366166381}[]{#_Toc366219917}[]{#_Toc366152639}[]{#_Toc366166382}[]{#_Toc366219918}[]{#_Toc366152661}[]{#_Toc366166404}[]{#_Toc366219940}[]{#_Toc366152662}[]{#_Toc366166405}[]{#_Toc366219941}[]{#_Toc366152663}[]{#_Toc366166406}[]{#_Toc366219942}

**BGP \-- BGP配置命令 \-- display bgp group**

------------------------------------------------------------------------

[**[display bgp group]{lang="EN-US"}**]{#struct_0_65458_x3406_1900993623}[命令用来显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_178695718}

[**[display bgp ]{lang="EN-US"}[group ipv4 ]{lang="EN-US"}**[{ **mdt** \| **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ **group-name** *group-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x199437277}

[**[display bgp ]{lang="EN-US"}[group ipv6 ]{lang="EN-US"}**[{ **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ **group-name** *group-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1155829228}

[**[display bgp ]{lang="EN-US"}[group vpnv4]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] \[ **group-name** *group-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1077181955}

[**[display bgp ]{lang="EN-US"}[group ]{lang="EN-US"}**[{ **l2vpn** \| **vpnv6** } \[ **group-name** *group-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1077116419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x192308539}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_293044463}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1252123862}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x802961629}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1742117280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_595784049}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1296700060}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x321628078}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1077050883}[：显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x1076985347}[：显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[**[mdt]{lang="EN-US"}**]{#struct_0_65458_x3406_x1155894764}[：显示]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_2008393694}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播对等体组的信息。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1947995198}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播对等体组的信息。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1153637145}[：显示]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[**[l2vpn]{lang="EN-US"}**]{#struct_0_65458_x3406_x1077968387}[：显示]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x558476409}[：显示]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x43866509}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体组的信息。]{style="font-family:宋体"}

[**[group-name]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_833788885}[：显示指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体组的详细信息，]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则显示指定地址族所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体组的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1156025836}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1155567084}[、]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[和]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_650466600}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_667479668}[显示公网所有]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播对等体组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp group ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_x423636460}

[ BGP peer group: group1]{lang="EN-US"}

[ Remote AS: 600]{lang="EN-US"}

[ Type: external]{lang="EN-US"}

[ Members:]{lang="EN-US"}

[  1.1.1.10]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP peer group: group2]{lang="EN-US"}

[ Remote AS number: not specified]{lang="EN-US"}

[ Type: external]{lang="EN-US"}

[ Members:]{lang="EN-US"}

[  2.2.2.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x465954714}[显示公网内]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播对等体组]{style="font-family:宋体"}[group1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp group ipv4 group-name group1]{lang="EN-US"}]{#struct_0_65458_x3406_1251206358}

[ BGP peer group: group1]{lang="EN-US"}

[ Remote AS: 600]{lang="EN-US"}

[ Type: external]{lang="EN-US"}

[ Maximum number of prefixes allowed: 4294967295]{lang="EN-US"}

[ Threshold: 75%]{lang="EN-US"}

[ Configured hold time: 180 seconds]{lang="EN-US"}

[ Keepalive time: 60 seconds]{lang="EN-US"}

[ Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[ Peer preferred value: 0]{lang="EN-US"}

[ Site-of-Origin: Not specified]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing policy configured:]{lang="EN-US"}

[ No routing policy is configured]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Members:]{lang="EN-US"}

[ \* - Dynamically created peer]{lang="EN-US"}

[  Peer                    AS  MsgRcvd  MsgSent OutQ PrefRcv Up/Down  State]{lang="EN-US"}

[ ]{lang="EN-US"}

[  1.1.1.10               600        0        0    0       0 00:00:55 Established]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_844935743}[显示公网内]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播对等体组]{style="font-family:宋体"}[group2]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp group ipv6 group-name group2]{lang="EN-US"}]{#struct_0_65458_x3406_845066815}

[ BGP peer group: group2]{lang="EN-US"}

[ Remote AS: 600]{lang="EN-US"}

[ Type: external]{lang="EN-US"}

[ Maximum number of prefixes allowed: 4294967295]{lang="EN-US"}

[ Threshold: 75%]{lang="EN-US"}

[ Configured hold time: 180 seconds]{lang="EN-US"}

[ Keepalive time: 60 seconds]{lang="EN-US"}

[ Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[ Peer preferred value: 0]{lang="EN-US"}

[ IPsec profile name: profile001]{lang="EN-US"}

[ Site-of-Origin: Not specified]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing policy configured:]{lang="EN-US"}

[ No routing policy is configured]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Members:]{lang="EN-US"}

[ \* - Dynamically created peer]{lang="EN-US"}

[  Peer                    AS  MsgRcvd  MsgSent OutQ PrefRcv Up/Down  State]{lang="EN-US"}

[ ]{lang="EN-US"}

[  2::2                   600        0        0    0       0 00:00:45 Established]{lang="EN-US"}

[  3::3                   600        0        0    0       0 00:00:40 Established]{lang="EN-US"}

[]{#struct_0_65458_x3406_x315135564}[]{#_Toc137998801}[]{#_Toc137998631}[[表1-3 ]{lang="EN-US"}[display bgp group]{lang="EN-US"}]{#_Ref132535095}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x302253877}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x262656027}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1251271894}

 

[[BGP peer group]{lang="EN-US"}]{#struct_0_65458_x3406_865775791}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1370943910}[对等体组名称]{style="font-family:宋体"}

 

[[Remote AS]{lang="EN-US"}]{#struct_0_65458_x3406_x807335514}

[[对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x804177911}[号]{style="font-family:宋体"}

 

[[Type]{lang="EN-US"}]{#struct_0_65458_x3406_887115441}

[[对等体组类型，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1251730647}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_65458_x3406_455025844}[：表示]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_65458_x3406_x706497245}[：表示]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组]{lang="EN-US" style="font-family:宋体"}

 

[[Maximum number of prefixes allowed]{lang="EN-US"}]{#struct_0_65458_x3406_x389918922}

[[允许从对等体学习的最大路由数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1625317259}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_845263423}[对等体组，本字段无意义]{style="font-family:宋体"}

 

[[Threshold]{lang="EN-US"}]{#struct_0_65458_x3406_1251796183}

[[路由器产生日志信息的阈值，即从对等体接收的路由前缀数量与允许的最大路由数的百分比达到此值时，路由器将产生日志信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_1251861719}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_845328959}[对等体组，本字段无意义]{style="font-family:宋体"}

 

[[Configured hold time]{lang="EN-US"}]{#struct_0_65458_x3406_x323637395}

[[配置的保持时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_1251927255}

 

[[Keepalive time]{lang="EN-US"}]{#struct_0_65458_x3406_x700320846}

[[存活时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_1577971996}

 

[[Minimum time between advertisements]{lang="EN-US"}]{#struct_0_65458_x3406_1767161675}

[[路由发布的最小时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_1119340620}

 

[[Peer preferred value]{lang="EN-US"}]{#struct_0_65458_x3406_1251992791}

[[为来自对等体的路由指定的首选值]{style="font-family:宋体"}]{#struct_0_65458_x3406_1227045565}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_844345919}[对等体组，本字段无意义]{style="font-family:宋体"}

 

[[Site-of-Origin]{lang="EN-US"}]{#struct_0_65458_x3406_844411455}

[[为对等体组指定的]{style="font-family:宋体"}[SoO]{lang="EN-US"}]{#struct_0_65458_x3406_844870206}[属性值]{style="font-family:宋体"}

 

[[Routing policy configured]{lang="EN-US"}]{#struct_0_65458_x3406_x2092181995}

[[为对等体组指定的路由策略]{style="font-family:宋体"}]{#struct_0_65458_x3406_1328322233}

[[如果未指定路由策略，则显示为]{style="font-family:宋体"}[No routing policy is configured]{lang="EN-US"}]{#struct_0_65458_x3406_997203260}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_844935742}[对等体组，本字段无意义]{style="font-family:宋体"}

 

[[Members]{lang="EN-US"}]{#struct_0_65458_x3406_1252058327}

[[对等体组包括的对等体信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_x909850133}

 

[[\* - Dynamically created peer]{lang="EN-US"}]{#struct_0_65458_x3406_1339382730}

[[如果对等体的地址前存在"]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_65458_x3406_1339448266}["，则表示该对等体为动态创建的对等体]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_65458_x3406_x417467929}

[[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x311277766}[地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

 

[[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1252123863}

[[对等体所在的自治系统号]{style="font-family:宋体"}]{#struct_0_65458_x3406_x803027165}

 

[[MsgRcvd]{lang="EN-US"}]{#struct_0_65458_x3406_x1744286131}

[[从该对等体收到的消息数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_1608255506}

 

[[MsgSent]{lang="EN-US"}]{#struct_0_65458_x3406_1252189399}

[[向该对等体发送的消息数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_650401064}

 

[[OutQ]{lang="EN-US"}]{#struct_0_65458_x3406_x128121240}

[[等待发往该对等体的消息数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1580239508}

 

[[PrefRcv]{lang="EN-US"}]{#struct_0_65458_x3406_1251206359}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[对于]{style="font-family:宋体"}]{#struct_0_65458_x3406_x315201100}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[和]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族，表示从该对等体收到的前缀数目]{style="font-family:宋体"}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
  Symbol"}]{.TableTextChar}[在]{style="font-family:宋体"}]{#struct_0_65458_x3406_845197886}[MPLS L2VPN]{lang="EN-US"}[应用中，表示从该对等体收到的标签块信息数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_65458_x3406_845263422}[VPLS]{lang="EN-US"}[应用中，表示从该对等体收到的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息数目，包括标签块信息和通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1156287973}[IPv4 MDT]{lang="EN-US"}[地址族，表示从对等体收到的]{style="font-family:宋体"}[MDT]{lang="EN-US"}[信息数目]{style="font-family:宋体"}

 

[[Up/Down]{lang="EN-US"}]{#struct_0_65458_x3406_952982880}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1251271895}[会话处于当前状态的时长]{style="font-family:宋体"}

 

[[State]{lang="EN-US"}]{#struct_0_65458_x3406_865841327}

[[该对等体的状态]{style="font-family:宋体"}]{#struct_0_65458_x3406_1187045473}

 

[[IPsec profile name]{lang="EN-US"}]{#struct_0_65458_x3406_844345918}

[[为]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_844411454}[对等体组应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

::: {#1229422476 .myid}
[]{#_Toc404788614}[]{#struct_0_65458_x3406_x301974890}[]{#_Toc309715689}[]{#_Toc309715690}[]{#_Toc309715691}[]{#_Toc309715692}[]{#_Toc309715693}[]{#_Toc309715694}[]{#_Toc309715698}[]{#_Toc309715699}[]{#_Toc309715700}[]{#_Toc309715701}[]{#_Toc309715702}[]{#_Toc309715703}[]{#_Toc309715704}[]{#_Toc309715705}[]{#_Toc309715706}[]{#_Toc309715707}[]{#_Toc309715709}[]{#_Toc309715712}[]{#_Toc309715714}[]{#_Toc309715717}[]{#_Toc309715718}[]{#_Toc309715737}[]{#_Toc361658804}[]{#_Toc361659391}[]{#_Toc361659978}[]{#_Toc361663551}[]{#_Toc361747011}[]{#_Toc361819374}[]{#_Toc361658805}[]{#_Toc361659392}[]{#_Toc361659979}[]{#_Toc361663552}[]{#_Toc361747012}[]{#_Toc361819375}[]{#_Toc361658806}[]{#_Toc361659393}[]{#_Toc361659980}[]{#_Toc361663553}[]{#_Toc361747013}[]{#_Toc361819376}[]{#_Toc361658807}[]{#_Toc361659394}[]{#_Toc361659981}[]{#_Toc361663554}[]{#_Toc361747014}[]{#_Toc361819377}[]{#_Toc361658808}[]{#_Toc361659395}[]{#_Toc361659982}[]{#_Toc361663555}[]{#_Toc361747015}[]{#_Toc361819378}[]{#_Toc361658809}[]{#_Toc361659396}[]{#_Toc361659983}[]{#_Toc361663556}[]{#_Toc361747016}[]{#_Toc361819379}[]{#_Toc361658810}[]{#_Toc361659397}[]{#_Toc361659984}[]{#_Toc361663557}[]{#_Toc361747017}[]{#_Toc361819380}[]{#_Toc361658811}[]{#_Toc361659398}[]{#_Toc361659985}[]{#_Toc361663558}[]{#_Toc361747018}[]{#_Toc361819381}[]{#_Toc361658812}[]{#_Toc361659399}[]{#_Toc361659986}[]{#_Toc361663559}[]{#_Toc361747019}[]{#_Toc361819382}[]{#_Toc361658813}[]{#_Toc361659400}[]{#_Toc361659987}[]{#_Toc361663560}[]{#_Toc361747020}[]{#_Toc361819383}[]{#_Toc361658814}[]{#_Toc361659401}[]{#_Toc361659988}[]{#_Toc361663561}[]{#_Toc361747021}[]{#_Toc361819384}[]{#_Toc361658815}[]{#_Toc361659402}[]{#_Toc361659989}[]{#_Toc361663562}[]{#_Toc361747022}[]{#_Toc361819385}[]{#_Toc361658816}[]{#_Toc361659403}[]{#_Toc361659990}[]{#_Toc361663563}[]{#_Toc361747023}[]{#_Toc361819386}[]{#_Toc361658817}[]{#_Toc361659404}[]{#_Toc361659991}[]{#_Toc361663564}[]{#_Toc361747024}[]{#_Toc361819387}[]{#_Toc361658818}[]{#_Toc361659405}[]{#_Toc361659992}[]{#_Toc361663565}[]{#_Toc361747025}[]{#_Toc361819388}[]{#_Toc361658819}[]{#_Toc361659406}[]{#_Toc361659993}[]{#_Toc361663566}[]{#_Toc361747026}[]{#_Toc361819389}[]{#_Toc361658820}[]{#_Toc361659407}[]{#_Toc361659994}[]{#_Toc361663567}[]{#_Toc361747027}[]{#_Toc361819390}[]{#_Toc361658821}[]{#_Toc361659408}[]{#_Toc361659995}[]{#_Toc361663568}[]{#_Toc361747028}[]{#_Toc361819391}[]{#_Toc361658822}[]{#_Toc361659409}[]{#_Toc361659996}[]{#_Toc361663569}[]{#_Toc361747029}[]{#_Toc361819392}[]{#_Toc361658823}[]{#_Toc361659410}[]{#_Toc361659997}[]{#_Toc361663570}[]{#_Toc361747030}[]{#_Toc361819393}[]{#_Toc361658824}[]{#_Toc361659411}[]{#_Toc361659998}[]{#_Toc361663571}[]{#_Toc361747031}[]{#_Toc361819394}[]{#_Toc361658825}[]{#_Toc361659412}[]{#_Toc361659999}[]{#_Toc361663572}[]{#_Toc361747032}[]{#_Toc361819395}[]{#_Toc361658826}[]{#_Toc361659413}[]{#_Toc361660000}[]{#_Toc361663573}[]{#_Toc361747033}[]{#_Toc361819396}[]{#_Toc361658827}[]{#_Toc361659414}[]{#_Toc361660001}[]{#_Toc361663574}[]{#_Toc361747034}[]{#_Toc361819397}[]{#_Toc361658828}[]{#_Toc361659415}[]{#_Toc361660002}[]{#_Toc361663575}[]{#_Toc361747035}[]{#_Toc361819398}[]{#_Toc361658829}[]{#_Toc361659416}[]{#_Toc361660003}[]{#_Toc361663576}[]{#_Toc361747036}[]{#_Toc361819399}[]{#_Toc361658830}[]{#_Toc361659417}[]{#_Toc361660004}[]{#_Toc361663577}[]{#_Toc361747037}[]{#_Toc361819400}[]{#_Toc361658831}[]{#_Toc361659418}[]{#_Toc361660005}[]{#_Toc361663578}[]{#_Toc361747038}[]{#_Toc361819401}[]{#_Toc361658832}[]{#_Toc361659419}[]{#_Toc361660006}[]{#_Toc361663579}[]{#_Toc361747039}[]{#_Toc361819402}[]{#_Toc361658833}[]{#_Toc361659420}[]{#_Toc361660007}[]{#_Toc361663580}[]{#_Toc361747040}[]{#_Toc361819403}[]{#_Toc361658834}[]{#_Toc361659421}[]{#_Toc361660008}[]{#_Toc361663581}[]{#_Toc361747041}[]{#_Toc361819404}[]{#_Toc361658835}[]{#_Toc361659422}[]{#_Toc361660009}[]{#_Toc361663582}[]{#_Toc361747042}[]{#_Toc361819405}[]{#_Toc361658836}[]{#_Toc361659423}[]{#_Toc361660010}[]{#_Toc361663583}[]{#_Toc361747043}[]{#_Toc361819406}[]{#_Toc361658837}[]{#_Toc361659424}[]{#_Toc361660011}[]{#_Toc361663584}[]{#_Toc361747044}[]{#_Toc361819407}[]{#_Toc361658838}[]{#_Toc361659425}[]{#_Toc361660012}[]{#_Toc361663585}[]{#_Toc361747045}[]{#_Toc361819408}[]{#_Toc361658839}[]{#_Toc361659426}[]{#_Toc361660013}[]{#_Toc361663586}[]{#_Toc361747046}[]{#_Toc361819409}[]{#_Toc361658840}[]{#_Toc361659427}[]{#_Toc361660014}[]{#_Toc361663587}[]{#_Toc361747047}[]{#_Toc361819410}[]{#_Toc361658841}[]{#_Toc361659428}[]{#_Toc361660015}[]{#_Toc361663588}[]{#_Toc361747048}[]{#_Toc361819411}[]{#_Toc361658842}[]{#_Toc361659429}[]{#_Toc361660016}[]{#_Toc361663589}[]{#_Toc361747049}[]{#_Toc361819412}[]{#_Toc361658843}[]{#_Toc361659430}[]{#_Toc361660017}[]{#_Toc361663590}[]{#_Toc361747050}[]{#_Toc361819413}[]{#_Toc361658844}[]{#_Toc361659431}[]{#_Toc361660018}[]{#_Toc361663591}[]{#_Toc361747051}[]{#_Toc361819414}[]{#_Toc361658845}[]{#_Toc361659432}[]{#_Toc361660019}[]{#_Toc361663592}[]{#_Toc361747052}[]{#_Toc361819415}[]{#_Toc361658846}[]{#_Toc361659433}[]{#_Toc361660020}[]{#_Toc361663593}[]{#_Toc361747053}[]{#_Toc361819416}[]{#_Toc361658847}[]{#_Toc361659434}[]{#_Toc361660021}[]{#_Toc361663594}[]{#_Toc361747054}[]{#_Toc361819417}[]{#_Toc361658848}[]{#_Toc361659435}[]{#_Toc361660022}[]{#_Toc361663595}[]{#_Toc361747055}[]{#_Toc361819418}[]{#_Toc361658849}[]{#_Toc361659436}[]{#_Toc361660023}[]{#_Toc361663596}[]{#_Toc361747056}[]{#_Toc361819419}[]{#_Toc361658850}[]{#_Toc361659437}[]{#_Toc361660024}[]{#_Toc361663597}[]{#_Toc361747057}[]{#_Toc361819420}[]{#_Toc361658851}[]{#_Toc361659438}[]{#_Toc361660025}[]{#_Toc361663598}[]{#_Toc361747058}[]{#_Toc361819421}[]{#_Toc361658852}[]{#_Toc361659439}[]{#_Toc361660026}[]{#_Toc361663599}[]{#_Toc361747059}[]{#_Toc361819422}[]{#_Toc361658853}[]{#_Toc361659440}[]{#_Toc361660027}[]{#_Toc361663600}[]{#_Toc361747060}[]{#_Toc361819423}[]{#_Toc361658854}[]{#_Toc361659441}[]{#_Toc361660028}[]{#_Toc361663601}[]{#_Toc361747061}[]{#_Toc361819424}[]{#_Toc361658855}[]{#_Toc361659442}[]{#_Toc361660029}[]{#_Toc361663602}[]{#_Toc361747062}[]{#_Toc361819425}[]{#_Toc361658856}[]{#_Toc361659443}[]{#_Toc361660030}[]{#_Toc361663603}[]{#_Toc361747063}[]{#_Toc361819426}[]{#_Toc361658923}[]{#_Toc361659510}[]{#_Toc361660097}[]{#_Toc361663670}[]{#_Toc361747130}[]{#_Toc361819493}

**BGP \-- BGP配置命令 \-- display bgp network**

------------------------------------------------------------------------

[**[display bgp network]{lang="EN-US"}**]{#struct_0_65458_x3406_x1476825024}[命令用来显示通过]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令发布的路由信息和通过]{style="font-family:宋体"}**[network short-cut]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[Short-cut]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_702149458}

[**[display bgp network ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } { **multicast** \| \[ **unicast** \] \[ **vpn-instance** ]{lang="EN-US"}*[vpn-instance-name ]{lang="EN-US"}*[\] }]{lang="EN-US"}]{#struct_0_65458_x3406_x1196013822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1470386317}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_985630592}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1545600055}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x285981808}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_73382378}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1476759488}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_124380295}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x940025445}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1181699435}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址族的信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x1404584387}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址族的信息。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1155894757}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播地址族的信息。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x720293053}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播地址族的信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_60871997}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1156025829}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_532888666}[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2080192146}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1129807530}[显示公网]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族下所有通过]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令通告的路由信息和通过]{style="font-family:宋体"}**[network short-cut]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[Short-cut]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp network ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1476693952}

[ ]{lang="EN-US"}

[  BGP local router ID: 192.168.1.135]{lang="EN-US"}

[  Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Network           Mask            Route-policy        Short-cut]{lang="EN-US"}

[  20.1.1.0          255.255.255.0                       No]{lang="EN-US"}

[  40.1.1.0          255.255.255.0   abc                 No]{lang="EN-US"}

[  30.1.1.0          255.255.255.0                       Yes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1126507232}[显示公网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族下所有通过]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令通告的路由信息和通过]{style="font-family:宋体"}**[network short-cut]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[Short-cut]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp network ipv6]{lang="EN-US"}]{#struct_0_65458_x3406_1714077345}

[ ]{lang="EN-US"}

[  BGP local router ID: 192.168.1.135]{lang="EN-US"}

[  Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Network           PrefixLen       Route-policy        Short-cut]{lang="EN-US"}

[  1::               24                                  No]{lang="EN-US"}

[  2::               24                                  No]{lang="EN-US"}

[  3::               64              policy1             No]{lang="EN-US"}

[  2::               24                                  Yes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1028749763}[显示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族下所有通过]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令通告的路由信息和通过]{style="font-family:宋体"}**[network short-cut]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[Short-cut]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp network ipv4 vpn-instance vpn1]{lang="EN-US"}]{#struct_0_65458_x3406_x1477676992}

[ ]{lang="EN-US"}

[  BGP local router ID: 192.168.1.135]{lang="EN-US"}

[  Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Network           Mask            Route-policy        Short-cut]{lang="EN-US"}

[  50.1.1.0          255.255.255.0                       No]{lang="EN-US"}

[  40.1.1.0          255.255.255.0                       Yes]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display bgp network]{lang="EN-US"}]{#struct_0_65458_x3406_x1335748395}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x315779125}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_1351366663}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1053845904}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_904191234}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1477611456}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_1443580074}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x367639762}[号]{style="font-family:宋体"}

[[Network]{lang="EN-US"}]{#struct_0_65458_x3406_x1281167029}

[[通过]{style="font-family:宋体"}**[network]{lang="EN-US"}**]{#struct_0_65458_x3406_762367245}[命令发布的路由或]{style="font-family:宋体"}[Short-cut]{lang="EN-US"}[路由的目的网络地址]{style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_65458_x3406_1735262822}

[[目的网络地址的掩码]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1477152707}

[[PrefixLen]{lang="EN-US"}]{#struct_0_65458_x3406_x945352882}

[[目的网络地址的前缀长度]{style="font-family:宋体"}]{#struct_0_65458_x3406_2093557695}

[[Route-policy]{lang="EN-US"}]{#struct_0_65458_x3406_x1124548383}

[[为该路由应用的路由策略]{style="font-family:宋体"}]{#struct_0_65458_x3406_2004963968}

[[Short-cut]{lang="EN-US"}]{#struct_0_65458_x3406_x1941921409}

[[该路由是否为]{style="font-family:宋体"}[Short-cut]{lang="EN-US"}]{#struct_0_65458_x3406_x1477087171}[路由，取值包括]{style="font-family:宋体"}[Yes]{lang="EN-US"}[和]{style="font-family:宋体"}[No]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1898589308 .myid}
[]{#_Toc404788615}[]{#struct_0_65458_x3406_x1155632613}[]{#_Toc366077069}[]{#_Toc345571243}

**BGP \-- BGP配置命令 \-- display bgp non-stop-routing status**

------------------------------------------------------------------------

[**[display bgp ]{lang="EN-US"}[non-stop-routing status]{lang="EN-US"}**]{#struct_0_65458_x3406_x1156091366}[命令用来显示]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[的运行状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1532346115}

[**[display bgp ]{lang="EN-US"}[non-stop-routing status]{lang="EN-US"}**]{#struct_0_65458_x3406_x1156156902}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x816090739}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_1271189946}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1156222438}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x894652175}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1156287974}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1095071362}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1155829222}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1362752744}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1644510373}[显示]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[的运行状态。]{style="font-family:宋体"}

[[\<Sysname\> display bgp non-stop-routing status]{lang="EN-US"}]{#struct_0_65458_x3406_x1155894758}

[ ]{lang="EN-US"}

[BGP NSR status: Ready]{lang="EN-US"}

[ Location of preferred standby process: Chassiss 0 slot 1]{lang="EN-US"}

[ TCP NSR status: Ready]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display bgp non-stop-routing status]{lang="EN-US"}]{#struct_0_65458_x3406_x317008526}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x245993398}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1155960294}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1156025830}

[[BGP NSR status]{lang="EN-US"}]{#struct_0_65458_x3406_x1155567078}

[[BGP NSR]{lang="EN-US"}]{#struct_0_65458_x3406_1701807816}[的备份状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_65458_x3406_x1155632614}[：]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[已经将]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居和路由信息从主进程备份到备进程。若在该状态下进行主备进程倒换，则现有路由保持不变，不会影响数据转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ready]{lang="EN-US"}]{#struct_0_65458_x3406_409992572}[：]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[正在将]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居和路由信息从主进程备份到备进程。若在该状态下进行主备进程倒换，则可能需要重新建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，导致数据转发中断]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not configured]{lang="EN-US"}]{#struct_0_65458_x3406_x1142208709}[：]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[功能未开启]{style="font-family:宋体"}

[[Location of preferred standby process]{lang="EN-US"}]{#struct_0_65458_x3406_409927036}

[[优选备进程所在单板的槽位号（分布式设备---独立运行模式）]{style="font-family:宋体"}]{#struct_0_65458_x3406_x767081486}

[[优选备进程所在成员设备的编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_65458_x3406_409861500}[设备）]{style="font-family:宋体"}

[[优选备进程所在成员设备的编号及单板的槽位号（分布式设备---]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_65458_x3406_409795964}[模式）]{style="font-family:宋体"}

[[TCP NSR status]{lang="EN-US"}]{#struct_0_65458_x3406_410254716}

[[TCP NSR]{lang="EN-US"}]{#struct_0_65458_x3406_1436118241}[的备份状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_65458_x3406_410189180}[：]{style="font-family:宋体"}[TCP NSR]{lang="EN-US"}[已经将]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接等信息从主进程备份到备进程]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ready]{lang="EN-US"}]{#struct_0_65458_x3406_410123644}[：]{lang="EN-US" style="font-family:宋体"}[TCP NSR]{lang="EN-US"}[正在将]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[连接等信息从主进程备份到备进程]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-916796985 .myid}
[]{#_Toc404788616}[]{#struct_0_65458_x3406_x40984751}

**BGP \-- BGP配置命令 \-- display bgp paths**

------------------------------------------------------------------------

[**[display bgp paths]{lang="EN-US"}**]{#struct_0_65458_x3406_x2146611274}[命令用来显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的路由属性信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_787477447}

[**[display bgp paths]{lang="EN-US"}**[ \[ *as-regular-expression* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x269816541}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1033362790}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_721485421}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1477021635}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1382127668}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1999495078}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_906845312}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1934741187}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_900309015}

[*[as-regular-expression]{lang="EN-US"}*]{#struct_0_65458_x3406_x1850588811}[：显示]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径与指定正则表达式匹配的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由属性的信息。]{style="font-family:宋体"}*[as-regular-expression]{lang="EN-US"}*[表示正则表达式，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[256]{lang="EN-US"}[个字符的字符串。如果不指定本参数，则显示所有的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由属性信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1932969389}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1476956099}[显示所有的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由属性信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp paths]{lang="EN-US"}]{#struct_0_65458_x3406_x876974104}

[ ]{lang="EN-US"}

[  RefCount    MED         Path/Origin]{lang="EN-US"}

[  3           0           ?]{lang="EN-US"}

[  2           0           100i]{lang="EN-US"}

[  3           0           100i]{lang="EN-US"}

[  1           0           ?]{lang="EN-US"}

[  1           0           ?]{lang="EN-US"}

[  1           0           ?]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display bgp paths]{lang="EN-US"}]{#struct_0_65458_x3406_1574819152}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x288887317}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x800843120}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x446792371}

[[RefCount]{lang="EN-US"}]{#struct_0_65458_x3406_x1476890563}

[[使用该路由属性的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x2017219007}[路由条数]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_65458_x3406_x1347975574}

[[MED]{lang="IT"}]{#struct_0_65458_x3406_x278138265}[属性值]{style="font-family:宋体"}

[[Path/Origin]{lang="EN-US"}]{#struct_0_65458_x3406_433741086}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1059913570}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和路由信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x1476825027}[属性记录了此路由经过的所有]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_298864931}[属性标记了此路由如何成为]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[，取值包括：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[i]{lang="EN-US"}]{#struct_0_65458_x3406_x570606857}[：表示路由产生于本]{style="font-family:宋体"}[AS]{lang="EN-US"}[内。通过]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令发布路由的路由信息来源为]{style="font-family:宋体"}[IGP]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[e]{lang="EN-US"}]{#struct_0_65458_x3406_1374994023}[：表示路由是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="EN-US"}[，外部网关协议）学到的。]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[?]{lang="EN-US"}]{#struct_0_65458_x3406_x1896544694}[：表示路由的来源无法确定。]{style="font-family:宋体"}[从]{lang="EN-US" style="font-family:
  宋体"}[IGP]{lang="EN-US"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:
  宋体"}[incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1947727744 .myid}
[]{#_Toc309715740}[]{#_Toc404788617}[]{#struct_0_65458_x3406_x2049475465}

**BGP \-- BGP配置命令 \-- display bgp peer**

------------------------------------------------------------------------

[**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1476759491}[命令用来显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体或对等体组的状态和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1334168340}

[**[display bgp peer ipv4 ]{lang="EN-US"}**[{ **mdt** \| ]{lang="EN-US"}**[multicast]{lang="EN-US"}**[ \| \[ **unicast** \] \[ **vpn-instance** ]{lang="EN-US"}*[vpn-instance-name ]{lang="EN-US"}*[\] } ]{lang="EN-US"}[\[ *ip-address mask-length* \| { *ip-address* *\|* **group-name** *group-name* } **log-info** \| \[ *ip-address* \] **verbose** \]]{lang="EN-US"}]{#struct_0_65458_x3406_409992571}

[**[display bgp peer ipv6 ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[multicast]{lang="EN-US"}**[ \| \[ **unicast** \] \[ ]{lang="EN-US"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[ \] } \[ *ipv6-address* *prefix-length* \| { *ipv6-address* *\|* **group-name** *group-name* } **log-info** \| \[ *ipv6-address* \] **verbose** \]]{lang="EN-US"}]{#struct_0_65458_x3406_409927035}

[**[display bgp peer ipv6 ]{lang="EN-US"}**[\[ **unicast** \] ]{lang="EN-US"}[\[ *ip-address* *mask-length* \| *ip-address* **log-info** \| \[ *ip-address* \] **verbose** \]]{lang="EN-US"}]{#struct_0_65458_x3406_409861499}

[**[display bgp peer vpnv4]{lang="EN-US"}**[ \[ **vpn-instance** ]{lang="EN-US"}*[vpn-instance-name ]{lang="EN-US"}*[\]]{lang="EN-US"}[ \[ *ip-address* *mask-length* \| { *ip-address* *\|* **group-name** *group-name* } **log-info** \| \[ *ip-address* \] **verbose** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1318864424}

[**[display bgp peer ]{lang="EN-US"}**[{ **l2vpn**]{lang="EN-US"}[ \| **vpnv6** } \[ *ip-address* *mask-length* \| { *ip-address* *\|* **group-name** *group-name* } **log-info** \| \[ *ip-address* \] **verbose** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1883685469}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1845548034}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_1054337034}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1198983942}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_650378843}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1111534136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1476693955}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1886022119}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_184585787}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1884471901}[：显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_409861498}[：显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1884013150}[：显示]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}

[**[l2vpn]{lang="EN-US"}**]{#struct_0_65458_x3406_x1883947614}[：显示]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x2027193384}[：显示]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}

[**[mdt]{lang="EN-US"}**]{#struct_0_65458_x3406_409795962}[：显示]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_410254714}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播对等体或对等体组的信息。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1436118239}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播对等体或对等体组的信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1587282996}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体或对等体组的信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1233100494}[：显示指定对等体的信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为对等体]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1339251664}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_410123642}[：显示指定对等体的信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为对等体]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x799563580}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[group-name]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_410058106}[：显示指定对等体组内对等体的信息。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[log-info]{lang="EN-US"}**]{#struct_0_65458_x3406_1203886720}[：显示指定对等体或对等体组的日志信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_65458_x3406_x447214566}[：显示对等体的详细信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1477676995}

[[执行本命令时，如果没有指定任何参数，则显示指定地址族所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1036904600}[对等体的简要信息。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_409992569}[、]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[和]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1868940754}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1770647887}[显示公网所有]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播对等体的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp peer ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1504478253}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.100.1]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ Total number of peers: 1                  Peers in established state: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \* - Dynamically created peer]{lang="EN-US"}

[  Peer                    AS  MsgRcvd  MsgSent OutQ PrefRcv Up/Down  State]{lang="EN-US"}

[ ]{lang="EN-US"}

[  10.2.1.2               200       13       16    0       0 00:10:34 Established]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display bgp peer]{lang="EN-US"}]{#struct_0_65458_x3406_x744925778}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x285688565}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1477611459}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1490634241}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_669264595}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x731146291}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_x166856496}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x855909007}[号]{style="font-family:宋体"}

[[Total number of peers]{lang="EN-US"}]{#struct_0_65458_x3406_x1477152706}

[[对等体的总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_1783530473}

[[Peers in established state]{lang="EN-US"}]{#struct_0_65458_x3406_x1118341429}

[[处于]{style="font-family:宋体"}[Established]{lang="EN-US"}]{#struct_0_65458_x3406_1742247773}[状态的对等体的总数]{style="font-family:宋体"}

[[\* - Dynamically created peer]{lang="EN-US"}]{#struct_0_65458_x3406_1338923985}

[[如果对等体的地址前存在"]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_65458_x3406_x472479593}["，则表示该对等体为动态创建的对等体]{style="font-family:宋体"}

[[Peer]{lang="EN-US"}]{#struct_0_65458_x3406_x291963629}

[[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1477087170}[地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1525099190}

[[对等体所在的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_721440075}[号]{style="font-family:宋体"}

[[MsgRcvd]{lang="EN-US"}]{#struct_0_65458_x3406_x425792842}

[[从对等体接收的消息数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x179443027}

[[MsgSent]{lang="EN-US"}]{#struct_0_65458_x3406_x1477021634}

[[向对等体发送的消息数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_183956273}

[[OutQ]{lang="EN-US"}]{#struct_0_65458_x3406_1589050797}

[[等待发往对等体的消息数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_980580202}

[[PrefRcv]{lang="EN-US"}]{#struct_0_65458_x3406_109926726}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1476956098}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[和]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族，表示从对等体接收到的加入到本地]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中的前缀数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1883554399}[MPLS L2VPN]{lang="EN-US"}[应用中，表示从该对等体收到并存入本地的标签块信息数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1883947616}[VPLS]{lang="EN-US"}[应用中，表示从该对等体收到并存入本地的]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息数目，包括标签块信息和通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议自动发现的]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息数目]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_65458_x3406_410189177}[IPv4 MDT]{lang="EN-US"}[地址族，表示从对等体接收到的]{style="font-family:宋体"}[MDT]{lang="EN-US"}[信息数目]{style="font-family:宋体"}

[[Up/Down]{lang="EN-US"}]{#struct_0_65458_x3406_1851909251}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x517057492}[会话处于当前状态的时长]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_65458_x3406_x477739444}

[[本地路由器与该对等体之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1651960107}[会话的当前状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1339055057}[显示]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[网段范围内的动态对等体信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp peer ipv4 1.1.1.0 24]{lang="EN-US"}]{#struct_0_65458_x3406_1339186129}

[ ]{lang="EN-US"}

[ Type: EBGP link]{lang="EN-US"}

[ ]{lang="EN-US"}[Dynamic address ]{lang="EN-US"}[range: 1.1.1.0 24]{lang="EN-US"}

[ Configured: Active Hold Time: 3 sec     Keepalive Time: 1 sec]{lang="EN-US"}

[ Address family IPv4 Unicast: Configured]{lang="EN-US"}

[ Address family IPv4 Multicast: Configured]{lang="EN-US"}

[ Address family IPv4 Label: Configured]{lang="EN-US"}

[ Address family VPNv4: Configured]{lang="EN-US"}

[ Address family IPv6 Unicast: Configured]{lang="EN-US"}

[ Address family VPNv6: Configured]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Maximum allowed prefix number: 100]{lang="EN-US"}

[ Threshold: 75%]{lang="EN-US"}

[ Minimum time between advertisements is 100 seconds]{lang="EN-US"}

[ Optional capabilities:]{lang="EN-US"}

[  Multi-protocol extended capability has been enabled]{lang="EN-US"}

[  Route refresh capability has been enabled ]{lang="EN-US"}

[ Nexthop self has been configured]{lang="EN-US"}

[ Keep-all-routes has been configured]{lang="EN-US"}

[ Send community has been configured]{lang="EN-US"}

[ Send extend community has been configured]{lang="EN-US"}

[ Default route originating has been configured]{lang="EN-US"}

[ Multi-hop ebgp has been enabled]{lang="EN-US"}

[ Peer preferred value: 100]{lang="EN-US"}

[ BFD: Enabled]{lang="EN-US"}

[ Site-of-Origin: 1:1]{lang="EN-US"}

[ Routing policy configured:]{lang="EN-US"}

[ No import as-path-acl list]{lang="EN-US"}

[ Export as-path-acl list is: 22]{lang="EN-US"}

[ No import prefix list]{lang="EN-US"}

[ Export prefix list is: p1]{lang="EN-US"}

[ No import route policy]{lang="EN-US"}

[ Export route policy is: p1]{lang="EN-US"}

[ No import filter-policy]{lang="EN-US"}

[ No export filter-policy]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Dynamic peers:]{lang="EN-US"}

[  1.1.1.3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1209062460}[显示]{style="font-family:宋体"}[1::/64]{lang="EN-US"}[网段范围内的动态对等体信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp peer ipv6 1:: 64]{lang="EN-US"}]{#struct_0_65458_x3406_1339251665}

[ ]{lang="EN-US"}

[ Type: IBGP link]{lang="EN-US"}

[ ]{lang="EN-US"}[Dynamic address ]{lang="EN-US"}[range: 1:: 64]{lang="EN-US"}

[ Configured: Active Hold Time: 180 sec   Keepalive Time: 60 sec]{lang="EN-US"}

[ Address family IPv6 Unicast: Configured]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Maximum allowed prefix number: 4294967295]{lang="EN-US"}

[ Threshold: 75%]{lang="EN-US"}

[ Minimum time between advertisements is 15 seconds]{lang="EN-US"}

[ Optional capabilities:]{lang="EN-US"}

[  Multi-protocol extended capability has been enabled]{lang="EN-US"}

[  Route refresh capability has been enabled]{lang="EN-US"}

[ Send community has been configured]{lang="EN-US"}

[ Peer preferred value: 0]{lang="EN-US"}

[ Site-of-Origin: Not specified]{lang="EN-US"}

[ Routing policy configured:]{lang="EN-US"}

[ No routing policy is configured]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Dynamic peers:]{lang="EN-US"}

[  1::1]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display bgp peer]{lang="EN-US"}]{#struct_0_65458_x3406_x799629116}[命令显示信息描述表（动态对等体）]{style="font-family:黑体"}

[]{#table_struct_0_x15305517}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_1339317201}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1206667411}

[[Type]{lang="EN-US"}]{#struct_0_65458_x3406_1339382737}

[[本地路由器与该动态对等体之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1339448273}[连接类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_x1238451860}[：]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_1339513809}[：]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[Dynamic address ]{lang="EN-US"}[range]{lang="EN-US"}]{#struct_0_65458_x3406_x1389959375}

[[动态对等体的地址范围]{style="font-family:宋体"}]{#struct_0_65458_x3406_x100396302}

[[Configured ]{lang="EN-US"}]{#struct_0_65458_x3406_x1389893839}

[[本地配置的定时器值，包括会话保持时间间隔（]{style="font-family:宋体"}[Active Hold Time]{lang="EN-US"}]{#struct_0_65458_x3406_x1389828303}[）和存活时间间隔（]{style="font-family:宋体"}[Keepalive Time]{lang="EN-US"}[），单位为秒]{style="font-family:宋体"}

[[Address family IPv4 Unicast]{lang="EN-US"}]{#struct_0_65458_x3406_x1829088861}

[[IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1389762767}[单播地址族能力]{style="font-family:宋体"}

[[Address family IPv6 Unicast]{lang="EN-US"}]{#struct_0_65458_x3406_x1389697231}

[[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_2068684873}[单播地址族能力]{style="font-family:宋体"}

[[Address family IPv4 Multicast]{lang="EN-US"}]{#struct_0_65458_x3406_x1389631695}

[[IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1389566159}[组播地址族能力]{style="font-family:宋体"}

[[Address family IPv6 Multicast]{lang="EN-US"}]{#struct_0_65458_x3406_2131017671}

[[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1389500623}[组播地址族能力]{style="font-family:宋体"}

[[Address family MDT]{lang="EN-US"}]{#struct_0_65458_x3406_x1389435087}

[[IPv4 MDT]{lang="EN-US"}]{#struct_0_65458_x3406_1837313035}[地址族能力]{style="font-family:宋体"}

[[Address family L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x1389369551}

[[L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x1389959374}[地址族能力]{style="font-family:宋体"}

[[Address family L2VPN VPWS (Draft)]{lang="EN-US"}]{#struct_0_65458_x3406_x1666480243}

[[L2VPN VPWS]{lang="EN-US"}]{#struct_0_65458_x3406_x1389893838}[地址族能力]{style="font-family:宋体"}

[[Maximum allowed prefix number]{lang="EN-US"}]{#struct_0_65458_x3406_x1389828302}

[[允许从对等体学习的最大路由数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x263004920}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x1389762766}[对等体组，本字段无意义]{style="font-family:宋体"}

[[Threshold]{lang="EN-US"}]{#struct_0_65458_x3406_x1389697230}

[[路由器产生日志信息的阈值，即从对等体接收的路由数量与允许的最大路由数的百分比达到此值时，路由器将产生日志信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_502600932}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x1389631694}[对等体组，本字段无意义]{style="font-family:宋体"}

[[Minimum time between advertisements]{lang="EN-US"}]{#struct_0_65458_x3406_x1389566158}

[[路由发布最小时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389500622}

[[Optional capabilities]{lang="EN-US"}]{#struct_0_65458_x3406_x876503175}

[[本端支持的可选扩展能力]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389435086}

[[Multi-protocol extended capability has been enabled]{lang="EN-US"}]{#struct_0_65458_x3406_x1389369550}

[[本端支持]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1346020944}[多协议扩展能力]{style="font-family:宋体"}

[[Route refresh capability has been enabled]{lang="EN-US"}]{#struct_0_65458_x3406_x1389959377}

[[本端支持]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1389893841}[路由刷新能力]{style="font-family:宋体"}

[[Nexthop self has been configured]{lang="EN-US"}]{#struct_0_65458_x3406_x1389828305}

[[向对等体发布路由时，将下一跳属性修改为自身的地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389762769}

[[Keep-all-routes has been configured]{lang="EN-US"}]{#struct_0_65458_x3406_1599717313}

[[保存所有来自指定对等体的原始路由更新信息，不管这些路由是否通过了路由策略的过滤]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389697233}

[[Send community has been configured]{lang="EN-US"}]{#struct_0_65458_x3406_x1389631697}

[[向对等体发布团体属性]{style="font-family:宋体"}]{#struct_0_65458_x3406_1305095173}

[[Send extend community has been configured]{lang="EN-US"}]{#struct_0_65458_x3406_x1389566161}

[[向对等体发布扩展团体属性]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389500625}

[[Default route originating has been configured]{lang="EN-US"}]{#struct_0_65458_x3406_x1389435089}

[[向对等体发送缺省路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389369553}

[[Multi-hop ebgp has been enabled]{lang="EN-US"}]{#struct_0_65458_x3406_x1382862411}

[[允许本地路由器同非直连网络上的邻居建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1389959376}[会话]{style="font-family:宋体"}

[[Peer Preferred Value]{lang="EN-US"}]{#struct_0_65458_x3406_x1389893840}

[[为来自对等体的路由配置的首选值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389828304}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x1069573974}[对等体组，本字段无意义]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_65458_x3406_x1389762768}

[[是否配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_65458_x3406_x1389697232}[检测本地路由器和指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体之间的链路]{style="font-family:宋体"}

[[IPsec profile name]{lang="EN-US"}]{#struct_0_65458_x3406_x660198482}

[[为]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1389631696}[对等体应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名]{style="font-family:宋体"}

[[只有显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1389566160}[单播和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址族信息时，显示本字段]{style="font-family:宋体"}

[[Site-of-Origin]{lang="EN-US"}]{#struct_0_65458_x3406_x1389500624}

[[为对等体指定的]{style="font-family:宋体"}[SoO]{lang="EN-US"}]{#struct_0_65458_x3406_286296239}[属性值]{style="font-family:宋体"}

[[Routing policy configured]{lang="EN-US"}]{#struct_0_65458_x3406_x1389435088}

[[为对等体指定的路由策略]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389369552}

[[如果未指定路由策略，则显示为]{style="font-family:宋体"}[No routing policy is configured]{lang="EN-US"}]{#struct_0_65458_x3406_183221530}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x1389959371}[对等体组，本字段无意义]{style="font-family:宋体"}

[[Dynamic peers]{lang="EN-US"}]{#struct_0_65458_x3406_x1389893835}

[[动态对等体中包括的对等体的地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1389828299}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1775950871}[显示公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播对等体]{style="font-family:宋体"}[10.2.1.2]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp peer ipv4 10.2.1.2 verbose]{lang="EN-US"}]{#struct_0_65458_x3406_x1476825026}

[ ]{lang="EN-US"}

[         Peer: 10.2.1.2          Local: 192.168.100.1]{lang="EN-US"}

[         Type: EBGP link]{lang="EN-US"}

[         BGP version 4, remote router ID 192.168.100.2]{lang="EN-US"}

[         BGP current state: Established, Up for 00h11m10s]{lang="EN-US"}

[         BGP current event: RecvKeepalive]{lang="EN-US"}

[         BGP last state: OpenConfirm]{lang="EN-US"}

[         Port:  Local - 179      Remote - 60672]{lang="EN-US"}

[         Configured: Active Hold Time: 180 sec   Keepalive Time: 60 sec]{lang="EN-US"}

[         Received  : Active Hold Time: 180 sec]{lang="EN-US"}

[         Negotiated: Active Hold Time: 180 sec   Keepalive Time: 60 sec]{lang="EN-US"}

[         Peer optional capabilities:]{lang="EN-US"}

[         Peer support BGP multi-protocol extended]{lang="EN-US"}

[         Peer support BGP route refresh capability]{lang="EN-US"}

[         Peer support BGP route AS4 capability]{lang="EN-US"}

[         Address family IPv4 Unicast: advertised and received]{lang="EN-US"}

[ ]{lang="EN-US"}

[ InQ updates: 0, OutQ updates: 0]{lang="EN-US"}

[ NLRI statistics:]{lang="EN-US"}

[         Rcvd:   UnReach NLRI          0,      Reach NLRI          0]{lang="EN-US"}

[         Sent:   UnReach NLRI          0,      Reach NLRI          0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Message statistics:]{lang="EN-US"}

[ Msg type     Last rcvd time/      Current rcvd count/      History rcvd count/]{lang="EN-US"}

[              Last sent time       Current sent count       History sent count]{lang="EN-US"}

[ Open         10:38:50-2013.7.23   1                        1]{lang="EN-US"}

[              10:38:50-2013.7.23   1                        1]{lang="EN-US"}

[ Update       10:38:51-2013.7.23   1                        1]{lang="EN-US"}

[              10:38:51-2013.7.23   1                        1]{lang="EN-US"}

[ Notification -                    0                        0]{lang="EN-US"}

[              -                    0                        0]{lang="EN-US"}

[ Keepalive    10:38:50-2013.7.23   1                        1]{lang="EN-US"}

[              10:38:50-2013.7.23   1                        1]{lang="EN-US"}

[ RouteRefresh -                    0                        0]{lang="EN-US"}

[              -                    0                        0]{lang="EN-US"}

[ Total        -                    3                        3]{lang="EN-US"}

[              -                    3                        3   ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Maximum allowed prefix number: 4294967295]{lang="EN-US"}

[ Threshold: 75%]{lang="EN-US"}

[ Minimum time between advertisements is 30 seconds]{lang="EN-US"}

[ Optional capabilities:]{lang="EN-US"}

[  Multi-protocol extended capability has been enabled]{lang="EN-US"}

[  Route refresh capability has been enabled]{lang="EN-US"}

[ Peer Preferred Value: 0]{lang="EN-US"}

[ BFD: Enabled]{lang="EN-US"}

[ Site-of-Origin: Not specified]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing policy configured:]{lang="EN-US"}

[ No routing policy is configured]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1884537440}[显示公网]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播对等体]{style="font-family:宋体"}[1::2]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp peer ipv6 1::2 verbose]{lang="EN-US"}]{#struct_0_65458_x3406_x1883751009}

[ ]{lang="EN-US"}

[         Peer: 1::2      Local: 192.168.1.136]{lang="EN-US"}

[         Type: EBGP link]{lang="EN-US"}

[         BGP version 4, remote router ID 192.168.1.135]{lang="EN-US"}

[         BGP current state: Established, Up for 00h05m48s]{lang="EN-US"}

[         BGP current event: RecvKeepalive]{lang="EN-US"}

[         BGP last state: OpenConfirm]{lang="EN-US"}

[         Port:  Local - 13184    Remote - 179]{lang="EN-US"}

[         Configured: Active Hold Time: 180 sec   Keepalive Time: 60 sec]{lang="EN-US"}

[         Received  : Active Hold Time: 180 sec]{lang="EN-US"}

[         Negotiated: Active Hold Time: 180 sec   Keepalive Time: 60 sec]{lang="EN-US"}

[         Peer optional capabilities:]{lang="EN-US"}

[         Peer support BGP multi-protocol extended]{lang="EN-US"}

[         Peer support BGP route refresh capability]{lang="EN-US"}

[         Peer support BGP route AS4 capability]{lang="EN-US"}

[         Address family IPv6 Unicast: advertised and received]{lang="EN-US"}

[ ]{lang="EN-US"}

[ InQ updates: 0, OutQ updates: 0        ]{lang="EN-US"}

[ NLRI statistics:                                                               ]{lang="EN-US"}

[         Rcvd:   UnReach NLRI          0,       Reach NLRI          0            ]{lang="EN-US"}

[         Sent:   UnReach NLRI          0,       Reach NLRI          3            ]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[ Message statistics:                                                            ]{lang="EN-US"}

[ Msg type     Last rcvd time/      Current rcvd count/      History rcvd count/ ]{lang="EN-US"}

[              Last sent time       Current sent count       History sent count  ]{lang="EN-US"}

[ Open         18:59:15-2013.4.24   1                        1                   ]{lang="EN-US"}

[              18:59:15-2013.4.24   1                        2                   ]{lang="EN-US"}

[ Update       -                    0                        0                   ]{lang="EN-US"}

[              18:59:16-2013.4.24   1                        1                   ]{lang="EN-US"}

[ Notification -                    0                        0                   ]{lang="EN-US"}

[              18:59:15-2013.4.24   0                        1                   ]{lang="EN-US"}

[ Keepalive    18:59:15-2013.4.24   1                        1                   ]{lang="EN-US"}

[              18:59:15-2013.4.24   1                        1                   ]{lang="EN-US"}

[ RouteRefresh -                    0                        0                   ]{lang="EN-US"}

[              -                    0                        0                   ]{lang="EN-US"}

[ Total        -                    2                        2                   ]{lang="EN-US"}

[              -                    3                        5                  ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Maximum allowed prefix number: 4294967295]{lang="EN-US"}

[ Threshold: 75%]{lang="EN-US"}

[ Minimum time between advertisements is 30 seconds]{lang="EN-US"}

[ Optional capabilities:]{lang="EN-US"}

[  Multi-protocol extended capability has been enabled]{lang="EN-US"}

[  Route refresh capability has been enabled]{lang="EN-US"}

[ Peer preferred value: 0]{lang="EN-US"}

[ BFD: Enabled]{lang="EN-US"}

[ IPsec profile name: profile001]{lang="EN-US"}

[ Site-of-Origin: Not specified]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing policy configured:]{lang="EN-US"}

[ No routing policy is configured]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1883685473}[显示地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[对等体的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp peer l2vpn 10.1.1.1 verbose]{lang="EN-US"}]{#struct_0_65458_x3406_x317863671}

[ ]{lang="EN-US"}

[         Peer: 10.1.1.1  Local: 192.168.1.136]{lang="EN-US"}

[         Type: EBGP link]{lang="EN-US"}

[         BGP version 4, remote router ID 192.168.1.135]{lang="EN-US"}

[         BGP current state: Established, Up for 00h01m25s]{lang="EN-US"}

[         BGP current event: KATimerExpired]{lang="EN-US"}

[         BGP last state: OpenConfirm]{lang="EN-US"}

[         Port:  Local - 179      Remote - 1049]{lang="EN-US"}

[         Configured: Active Hold Time: 180 sec   Keepalive Time: 60 sec]{lang="EN-US"}

[         Received  : Active Hold Time: 180 sec]{lang="EN-US"}

[         Negotiated: Active Hold Time: 180 sec   Keepalive Time: 60 sec]{lang="EN-US"}

[         Peer optional capabilities:]{lang="EN-US"}

[         Peer support BGP multi-protocol extended]{lang="EN-US"}

[         Peer support BGP route refresh capability]{lang="EN-US"}

[         Peer support BGP route AS4 capability]{lang="EN-US"}

[         Address family IPv4 Unicast: advertised and received]{lang="EN-US"}

[         Address family L2VPN: advertised]{lang="EN-US"}

[         Address family L2VPN VPWS (Draft): advertised and received]{lang="EN-US"}

[ ]{lang="EN-US"}

[ InQ updates: 0, OutQ updates: 0        ]{lang="EN-US"}

[ NLRI statistics:                                                               ]{lang="EN-US"}

[         Rcvd:   UnReach NLRI          0,       Reach NLRI          0            ]{lang="EN-US"}

[         Sent:   UnReach NLRI          0,       Reach NLRI          3            ]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[ Message statistics:                                                            ]{lang="EN-US"}

[ Msg type     Last rcvd time/      Current rcvd count/      History rcvd count/ ]{lang="EN-US"}

[              Last sent time       Current sent count       History sent count  ]{lang="EN-US"}

[ Open         18:59:15-2013.4.24   1                        1                   ]{lang="EN-US"}

[              18:59:15-2013.4.24   1                        2                   ]{lang="EN-US"}

[ Update       -                    0                        0                   ]{lang="EN-US"}

[              18:59:16-2013.4.24   1                        1                   ]{lang="EN-US"}

[ Notification -                    0                        0                   ]{lang="EN-US"}

[              18:59:15-2013.4.24   0                        1                   ]{lang="EN-US"}

[ Keepalive    18:59:15-2013.4.24   1                        1                   ]{lang="EN-US"}

[              18:59:15-2013.4.24   1                        1                   ]{lang="EN-US"}

[ RouteRefresh -                    0                        0                   ]{lang="EN-US"}

[              -                    0                        0                   ]{lang="EN-US"}

[ Total        -                    2                        2                   ]{lang="EN-US"}

[              -                    3                        5                  ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Maximum allowed prefix number: 4294967295]{lang="EN-US"}

[ Threshold: 75%]{lang="EN-US"}

[ Minimum time between advertisements is 30 seconds]{lang="EN-US"}

[ Optional capabilities:]{lang="EN-US"}

[  Multi-protocol extended capability has been enabled]{lang="EN-US"}

[  Route refresh capability has been enabled]{lang="EN-US"}

[ Peer Preferred Value: 0]{lang="EN-US"}

[ BFD: Enabled]{lang="EN-US"}

[ Site-of-Origin: Not specified]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing policy configured:]{lang="EN-US"}

[ No routing policy is configured]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display bgp peer verbose]{lang="EN-US"}]{#struct_0_65458_x3406_1864948872}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x293387701}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_2041294288}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_2006803631}

[[Peer]{lang="EN-US"}]{#struct_0_65458_x3406_x1324047927}

[[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1476759490}[地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Local]{lang="EN-US"}]{#struct_0_65458_x3406_x231915601}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x26371087}

[[Type]{lang="EN-US"}]{#struct_0_65458_x3406_x2013716122}

[[本地路由器与该对等体之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1595925432}[连接类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_207926615}[：]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_x1476693954}[：]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[BGP version]{lang="EN-US"}]{#struct_0_65458_x3406_319938178}

[[协议版本号]{style="font-family:宋体"}]{#struct_0_65458_x3406_x181937353}

[[remote router ID]{lang="EN-US"}]{#struct_0_65458_x3406_221160221}

[[对等体的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_616173489}

[[BGP current state]{lang="EN-US"}]{#struct_0_65458_x3406_x1477676994}

[[本地路由器与该对等体之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x529179341}[会话的当前状态]{style="font-family:宋体"}

[[Up for]{lang="EN-US"}]{#struct_0_65458_x3406_1997740611}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x262711219}[会话建立的持续时间]{style="font-family:宋体"}

[[BGP current event]{lang="EN-US"}]{#struct_0_65458_x3406_1841337859}

[[本地路由器与该对等体之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1477611458}[会话的当前事件]{style="font-family:宋体"}

[[BGP last state]{lang="EN-US"}]{#struct_0_65458_x3406_x75449700}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1818901941}[会话的前一个状态]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_65458_x3406_x232216277}

[[建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_65458_x3406_x181077836}[连接时本地（]{style="font-family:宋体"}[Local]{lang="EN-US"}[）和对等体（]{style="font-family:宋体"}[Remote]{lang="EN-US"}[）使用的端口号]{style="font-family:宋体"}

[[Configured ]{lang="EN-US"}]{#struct_0_65458_x3406_x1477152709}

[[本地配置的定时器值，包括会话保持时间间隔（]{style="font-family:宋体"}[Active Hold Time]{lang="EN-US"}]{#struct_0_65458_x3406_x1395691576}[）和存活时间间隔（]{style="font-family:宋体"}[Keepalive Time]{lang="EN-US"}[），单位为秒]{style="font-family:宋体"}

[[Received]{lang="EN-US"}]{#struct_0_65458_x3406_876304581}

[[收到的定时器值，即对等体上配置的定时器值，包括会话保持时间间隔（]{style="font-family:宋体"}[Active Hold Time]{lang="EN-US"}]{#struct_0_65458_x3406_x1760250790}[），单位为秒]{style="font-family:宋体"}

[[Negotiated]{lang="EN-US"}]{#struct_0_65458_x3406_x1477087173}

[[协商后的定时器值，包括会话保持时间间隔（]{style="font-family:宋体"}[Active Hold Time]{lang="EN-US"}]{#struct_0_65458_x3406_x1203784165}[）和存活时间间隔（]{style="font-family:宋体"}[Keepalive Time]{lang="EN-US"}[），单位为秒]{style="font-family:宋体"}

[[Peer optional capabilities]{lang="EN-US"}]{#struct_0_65458_x3406_1822860730}

[[对等体支持的可选扩展能力]{style="font-family:宋体"}]{#struct_0_65458_x3406_1880896217}

[[Peer support BGP multi-protocol extended]{lang="EN-US"}]{#struct_0_65458_x3406_x1477021637}

[[对等体支持]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x219328254}[多协议扩展能力]{style="font-family:宋体"}

[[Peer support BGP route refresh capability]{lang="EN-US"}]{#struct_0_65458_x3406_x750618855}

[[对等体支持]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1623418969}[路由刷新能力]{style="font-family:宋体"}

[[Peer support BGP route AS4 capability]{lang="EN-US"}]{#struct_0_65458_x3406_x1476956101}

[[对等体支持四字节]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1233663217}[号能力]{style="font-family:宋体"}

[[Address family IPv4 Unicast]{lang="EN-US"}]{#struct_0_65458_x3406_324484899}

[[IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1476890565}[单播地址族能力，可以接收（]{style="font-family:宋体"}[received]{lang="EN-US"}[）和发送（]{style="font-family:宋体"}[advertised]{lang="EN-US"}[）该地址族的路由]{style="font-family:宋体"}

[[Address family IPv6 Unicast]{lang="EN-US"}]{#struct_0_65458_x3406_410516864}

[[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_410451328}[单播地址族能力，可以接收（]{style="font-family:宋体"}[received]{lang="EN-US"}[）和发送（]{style="font-family:宋体"}[advertised]{lang="EN-US"}[）该地址族的路由]{style="font-family:宋体"}

[[Address family IPv4 Multicast]{lang="EN-US"}]{#struct_0_65458_x3406_409992575}

[[IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_409927039}[组播地址族能力，可以接收（]{style="font-family:宋体"}[received]{lang="EN-US"}[）和发送（]{style="font-family:宋体"}[advertised]{lang="EN-US"}[）该地址族的路由]{style="font-family:宋体"}

[[Address family IPv6 Multicast]{lang="EN-US"}]{#struct_0_65458_x3406_409861503}

[[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_410254719}[组播地址族能力，可以接收（]{style="font-family:宋体"}[received]{lang="EN-US"}[）和发送（]{style="font-family:宋体"}[advertised]{lang="EN-US"}[）该地址族的路由]{style="font-family:宋体"}

[[Address family MDT]{lang="EN-US"}]{#struct_0_65458_x3406_410189183}

[[IPv4 MDT]{lang="EN-US"}]{#struct_0_65458_x3406_410123647}[地址族能力，可以接收（]{style="font-family:宋体"}[received]{lang="EN-US"}[）和发送（]{style="font-family:宋体"}[advertised]{lang="EN-US"}[）该地址族的信息]{style="font-family:宋体"}

[[Address family L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_410058111}

[[L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_410516863}[地址族能力：可以接收（]{style="font-family:宋体"}[received]{lang="EN-US"}[）和发送（]{style="font-family:宋体"}[advertised]{lang="EN-US"}[）]{style="font-family:宋体"}[L2VPN VPLS]{lang="EN-US"}[和]{style="font-family:宋体"}[VPWS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Address family L2VPN VPWS (Draft)]{lang="EN-US"}]{#struct_0_65458_x3406_410451327}

[[L2VPN VPWS]{lang="EN-US"}]{#struct_0_65458_x3406_x1501573825}[地址族能力：可以接收和发送]{style="font-family:宋体"}[draft-kompella-ppvpn-l2vpn-03]{lang="EN-US"}[草案定义的]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息]{style="font-family:宋体"}

[[InQ updates]{lang="EN-US"}]{#struct_0_65458_x3406_x317929208}

[[待处理的接收到的]{style="font-family:宋体"}[Update]{lang="EN-US"}]{#struct_0_65458_x3406_x317863672}[消息数目]{style="font-family:宋体"}

[[OutQ updates]{lang="EN-US"}]{#struct_0_65458_x3406_x317732600}

[[等待发送给对等体的]{style="font-family:宋体"}[Update]{lang="EN-US"}]{#struct_0_65458_x3406_x317601528}[消息数目]{style="font-family:宋体"}

[[NLRI statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x317535992}

[[NLRI]{lang="EN-US"}]{#struct_0_65458_x3406_x318453496}[统计信息，包括建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话后，从对等体累计接收到的可达路由数目和不可达路由数目，向对等体累计发送的可达路由数目和不可达路由数目]{style="font-family:宋体"}

[[Message statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x317929209}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x317863673}[消息统计信息]{style="font-family:宋体"}

[[Msg type]{lang="EN-US"}]{#struct_0_65458_x3406_x317732601}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x317601529}[消息类型]{style="font-family:宋体"}

[[Last rcvd time/Last sent time]{lang="EN-US"}]{#struct_0_65458_x3406_x317535993}

[[最近一次从对等体接收到]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x318453497}[消息的时间]{style="font-family:宋体"}[/]{lang="EN-US"}[最近一次向对等体发送]{style="font-family:宋体"}[BGP]{lang="EN-US"}[消息的时间]{style="font-family:宋体"}

[[Current rcvd count/Current sent count]{lang="EN-US"}]{#struct_0_65458_x3406_x317929210}

[[在当前]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x317798138}[会话上，从对等体接收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[消息数目]{style="font-family:宋体"}[/]{lang="EN-US"}[在当前]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话上，向对等体发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[消息数目]{style="font-family:宋体"}

[[History rcvd count/History sent count]{lang="EN-US"}]{#struct_0_65458_x3406_x317732602}

[[配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x317601530}[对等体以来，累计从对等体接收到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[消息数目]{style="font-family:宋体"}[/]{lang="EN-US"}[累计向对等体发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[消息数目]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_65458_x3406_x317470458}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x318387962}[发送所有类型消息的总数]{style="font-family:宋体"}

[[Maximum allowed prefix number]{lang="EN-US"}]{#struct_0_65458_x3406_749203625}

[[允许从对等体学习的最大路由数]{style="font-family:宋体"}]{#struct_0_65458_x3406_539895904}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x317667067}[对等体组，本字段无意义]{style="font-family:宋体"}

[[Threshold]{lang="EN-US"}]{#struct_0_65458_x3406_x1476759493}

[[路由器产生日志信息的阈值，即从对等体接收的路由数量与允许的最大路由数的百分比达到此值时，路由器将产生日志信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1477676997}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x317535995}[对等体组，本字段无意义]{style="font-family:宋体"}

[[Minimum time between advertisements]{lang="EN-US"}]{#struct_0_65458_x3406_x2095263282}

[[路由发布最小时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_1510524210}

[[Optional capabilities]{lang="EN-US"}]{#struct_0_65458_x3406_x1477611461}

[[本端支持的可选扩展能力]{style="font-family:宋体"}]{#struct_0_65458_x3406_1846930137}

[[Multi-protocol extended capability has been enabled]{lang="EN-US"}]{#struct_0_65458_x3406_x1765391698}

[[本端支持]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1477152708}[多协议扩展能力]{style="font-family:宋体"}

[[Route refresh capability has been enabled]{lang="EN-US"}]{#struct_0_65458_x3406_1333191779}

[[本端支持]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_763076708}[路由刷新能力]{style="font-family:宋体"}

[[Peer Preferred Value]{lang="EN-US"}]{#struct_0_65458_x3406_x1477087172}

[[为来自对等体的路由配置的首选值]{style="font-family:宋体"}]{#struct_0_65458_x3406_362299776}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x318387963}[对等体组，本字段无意义]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_65458_x3406_x1779059275}

[[是否配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_65458_x3406_x1477021636}[检测本地路由器和指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体之间的链路]{style="font-family:宋体"}

[[IPsec profile name]{lang="EN-US"}]{#struct_0_65458_x3406_x1501901505}

[[为]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1501835969}[对等体应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名]{style="font-family:宋体"}

[[只有显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1502032577}[单播和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址族信息时，显示本字段]{style="font-family:宋体"}

[[Site-of-Origin]{lang="EN-US"}]{#struct_0_65458_x3406_x317863676}

[[为对等体指定的]{style="font-family:宋体"}[SoO]{lang="EN-US"}]{#struct_0_65458_x3406_x317798140}[属性值]{style="font-family:宋体"}

[[Routing policy configured]{lang="EN-US"}]{#struct_0_65458_x3406_1346755687}

[[为对等体指定的路由策略]{style="font-family:宋体"}]{#struct_0_65458_x3406_893379996}

[[如果未指定路由策略，则显示为]{style="font-family:宋体"}[No routing policy is configured]{lang="EN-US"}]{#struct_0_65458_x3406_x1476956100}

[[对于]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x317601532}[对等体组，本字段无意义]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1495220138}[显示公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp peer ipv4 1.1.1.1 log-info]{lang="EN-US"}]{#struct_0_65458_x3406_2004375788}

[ ]{lang="EN-US"}

[ Peer : 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Date      Time    State Notification]{lang="EN-US"}

[                             Error/SubError]{lang="EN-US"}

[ ]{lang="EN-US"}

[  06-Feb-2013 22:54:42 Down  Send notification with error 6/4]{lang="EN-US"}

[                             Cease/Administrative Reset]{lang="EN-US"}

[                             \<administrative reset\>]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display bgp peer log-info]{lang="EN-US"}]{#struct_0_65458_x3406_x838836779}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x301551637}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1476890564}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x94904706}

[[Peer]{lang="EN-US"}]{#struct_0_65458_x3406_595970401}

[[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_342508105}[地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Date]{lang="EN-US"}]{#struct_0_65458_x3406_x1380212748}

[[发送或接收到]{style="font-family:宋体"}[Notification]{lang="EN-US"}]{#struct_0_65458_x3406_1594652826}[消息的日期]{style="font-family:宋体"}

[[Time]{lang="EN-US"}]{#struct_0_65458_x3406_x1476825028}

[[发送或接收到]{style="font-family:宋体"}[Notification]{lang="EN-US"}]{#struct_0_65458_x3406_x1979679730}[消息的时间]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_65458_x3406_579266732}

[[本地与对等体之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x213664505}[会话的状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_65458_x3406_x1880447669}[：表示]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[会话处于]{lang="EN-US" style="font-family:宋体"}[Established]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_65458_x3406_1879169310}[：表示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话断开]{style="font-family:宋体"}

[[Notification Error/SubError]{lang="EN-US"}]{#struct_0_65458_x3406_x1476759492}

[[Notification]{lang="EN-US"}]{#struct_0_65458_x3406_x1394715015}[消息中的错误码，表明了]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话处于]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态的原因]{style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_65458_x3406_968199586}[表示]{style="font-family:宋体"}[Notification]{lang="EN-US"}[消息差错码，指定错误类型；]{style="font-family:宋体"}[SubError]{lang="EN-US"}[表示]{style="font-family:宋体"}[Notification]{lang="EN-US"}[消息差错子码，指定错误类型的详细信息]{style="font-family:宋体"}

[[如果是本端发送]{style="font-family:宋体"}[Notification]{lang="EN-US"}]{#struct_0_65458_x3406_1248613485}[消息通知对等体邻居异常断开，则会显示邻居断开的详细原因（详见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-11]{lang="EN-US"}](?1947727744#_Ref361670983)[）]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_65458_x3406_1247630445}[[表1-11 ]{lang="EN-US"}[邻居断开的详细原因列表]{style="font-family:
黑体"}]{#_Ref361670983}

[]{#table_struct_0_x1502447415}[[差错码]{style="font-family:黑体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_1248154732}[差错子码]{style="font-family:黑体"}

[[邻居断开的详细原因]{style="font-family:黑体"}]{#struct_0_65458_x3406_1248285804}

[[说明]{style="font-family:黑体"}]{#struct_0_65458_x3406_1248416876}

[[1/1]{lang="EN-US"}]{#struct_0_65458_x3406_1248547948}

[[connection not synchronized]{lang="EN-US"}]{#struct_0_65458_x3406_1247630444}

[[连接不同步，目前实现为收到的报文的报文头前]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_65458_x3406_1248154731}[字节不全为]{style="font-family:宋体"}[F]{lang="EN-US"}

[[1/2]{lang="EN-US"}]{#struct_0_65458_x3406_1248285803}

[[bad message length]{lang="EN-US"}]{#struct_0_65458_x3406_1248416875}

[[报文长度无效]{style="font-family:宋体"}]{#struct_0_65458_x3406_1248482411}

[[1/3]{lang="EN-US"}]{#struct_0_65458_x3406_1248613483}

[[bad message type]{lang="EN-US"}]{#struct_0_65458_x3406_1247695979}

[[报文的类型无效]{style="font-family:宋体"}]{#struct_0_65458_x3406_1248220266}

[[3/1]{lang="EN-US"}]{#struct_0_65458_x3406_1248351338}

[[the withdrawn length is too large]{lang="EN-US"}]{#struct_0_65458_x3406_1248482410}

[[撤销信息长度过长]{style="font-family:宋体"}]{#struct_0_65458_x3406_1248613482}

[[the attribute length is too large]{lang="EN-US"}]{#struct_0_65458_x3406_1247695978}

[[属性长度过长]{style="font-family:宋体"}]{#struct_0_65458_x3406_1248220265}

[[one attribute appears more than once]{lang="EN-US"}]{#struct_0_65458_x3406_1248416873}

[[同一个属性在一个]{style="font-family:宋体"}[Update]{lang="EN-US"}]{#struct_0_65458_x3406_1248547945}[消息中出现了多次]{style="font-family:宋体"}

[[the attribute length is too small]{lang="EN-US"}]{#struct_0_65458_x3406_1247630441}

[[属性长度字段不足]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_65458_x3406_x1124498261}[字节]{style="font-family:宋体"}

[[exntended length field is less than two octets]{lang="EN-US"}]{#struct_0_65458_x3406_x1124367189}

[[属性长度为可扩展长度，但长度字段不足]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_65458_x3406_x1124236117}[字节]{style="font-family:宋体"}

[[the length field is less than one octet]{lang="EN-US"}]{#struct_0_65458_x3406_x1124105045}

[[属性长度为正常长度，但长度字段不足]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_65458_x3406_x1125022549}[字节]{style="font-family:宋体"}

[[3/2]{lang="EN-US"}]{#struct_0_65458_x3406_x1124498262}

[unrecognized well-known attribute]{#struct_0_65458_x3406_x1124367190}

[[不支持的公认属性]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1124236118}

[[3/3]{lang="EN-US"}]{#struct_0_65458_x3406_x1124105046}

[*attribute-type*]{#struct_0_65458_x3406_x1125022550} attribute missed

[*attribute-type*]{#struct_0_65458_x3406_x1124498263}[类型的属性丢失，]{style="font-family:宋体"}*attribute-type*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}ORIGIN]{#struct_0_65458_x3406_x1124367191}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}AS_PATH]{#struct_0_65458_x3406_x1124236119}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}LOCAL_PREF]{#struct_0_65458_x3406_x1124105047}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}NEXT_HOP]{#struct_0_65458_x3406_x1125022551}

[[3/4]{lang="EN-US"}]{#struct_0_65458_x3406_x1124432728}

[[attribute flags error]{lang="EN-US"}]{#struct_0_65458_x3406_x1124301656}

[[属性标记错误]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1124170584}

[[3/5]{lang="EN-US"}]{#struct_0_65458_x3406_x1124039512}

[*[attribute-type ]{lang="EN-US"}*[attribute ]{lang="EN-US"}]{#struct_0_65458_x3406_x1124957016}[length error]{lang="EN-US"}

[*attribute-type*]{#struct_0_65458_x3406_x1124432729}[类型的属性长度错误，]{style="font-family:宋体"}*attribute-type*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}AS_PATH]{#struct_0_65458_x3406_x1124301657}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS4_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x1124170585}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLUSTER_LIST]{lang="EN-US"}]{#struct_0_65458_x3406_x1124039513}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}AGGREGATOR]{#struct_0_65458_x3406_x1124957017}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS4_AGGREGATOR]{lang="EN-US"}]{#struct_0_65458_x3406_x1124367194}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_x1124236122}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NEXT_HOP]{lang="EN-US"}]{#struct_0_65458_x3406_x1124105050}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_65458_x3406_x1125022554}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LOCAL_PREF]{lang="EN-US"}]{#struct_0_65458_x3406_441585680}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATOMIC_AGGREGATE]{lang="EN-US"}]{#struct_0_65458_x3406_441716752}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGINATOR_ID]{lang="EN-US"}]{#struct_0_65458_x3406_441847824}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MP_REACH_NLRI]{lang="EN-US"}]{#struct_0_65458_x3406_441978896}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMMUNITIES]{lang="EN-US"}]{#struct_0_65458_x3406_441061392}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extended communities]{lang="EN-US"}]{#struct_0_65458_x3406_441651215}

[[attribute length exceeds]{lang="EN-US"}]{#struct_0_65458_x3406_441782287}

[[属性长度越界]{style="font-family:宋体"}]{#struct_0_65458_x3406_441913359}

[[3/6]{lang="EN-US"}]{#struct_0_65458_x3406_442044431}

[invalid ORIGIN attribute]{#struct_0_65458_x3406_441126927}

[ORIGIN]{#struct_0_65458_x3406_441651214}[属性无效]{style="font-family:宋体"}

[[3/8]{lang="EN-US"}]{#struct_0_65458_x3406_441782286}

[invalid NEXT_HOP attribute]{#struct_0_65458_x3406_441913358}

[[下一跳属性无效]{style="font-family:宋体"}]{#struct_0_65458_x3406_441061390}

[[3/9]{lang="EN-US"}]{#struct_0_65458_x3406_441585677}

[[invalid nexthop length in MP_REACH_NLRI (*address-family*) ]{lang="EN-US"}]{#struct_0_65458_x3406_441716749}

[*[address-family]{lang="EN-US"}*]{#struct_0_65458_x3406_441847821}[地址族]{style="font-family:宋体"}[MP_REACH_NLRI]{lang="EN-US"}[属性的]{style="font-family:宋体"}[Nexthop]{lang="EN-US"}[长度错误，]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4u]{lang="EN-US"}]{#struct_0_65458_x3406_441978893}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MPLS]{lang="EN-US"}]{#struct_0_65458_x3406_441126925}[：表示]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_441651212}[：表示]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6u]{lang="EN-US"}]{#struct_0_65458_x3406_441782284}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNv6]{lang="EN-US"}]{#struct_0_65458_x3406_441913356}[：表示]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_442044428}[：表示]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[the length of MP_UNREACH_NLRI is too small]{lang="EN-US"}]{#struct_0_65458_x3406_441126924}

[[MP_UNREACH_NLRI]{lang="EN-US"}]{#struct_0_65458_x3406_441716747}[的长度小于]{style="font-family:宋体"}[3]{lang="EN-US"}[字节]{style="font-family:宋体"}

[[the MP NLRI attribute length exceeds]{lang="EN-US"}]{#struct_0_65458_x3406_441847819}

[[MP_REACH_NLRI ]{lang="EN-US"}]{#struct_0_65458_x3406_441978891}[或]{style="font-family:宋体"}[MP_UNREACH_NLRI]{lang="EN-US"}[属性长度越界]{style="font-family:宋体"}

[[erroneous MP NLRI attribute end position]{lang="EN-US"}]{#struct_0_65458_x3406_441061387}

[[可达或不可达前缀结束位置与报文属性结束位置不同]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1487085613}

[[3/10]{lang="EN-US"}]{#struct_0_65458_x3406_x1487282221}

[invalid network field]{#struct_0_65458_x3406_x1487413293}

[[网络字段无效]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1487544365}

[[3/11]{lang="EN-US"}]{#struct_0_65458_x3406_x1486626861}

[malformed AS_PATH]{#struct_0_65458_x3406_x1487151150}

[[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1487282222}[路径形式不对]{style="font-family:宋体"}

[[4/0]{lang="EN-US"}]{#struct_0_65458_x3406_x1487413294}

[[hold timer expiration caused by local device]{lang="EN-US"}]{#struct_0_65458_x3406_x1486561326}

[[本地导致]{style="font-family:宋体"}[holdtimer]{lang="EN-US"}]{#struct_0_65458_x3406_x1487085615}[超时]{style="font-family:宋体"}

[[hold timer expiration caused by peer device]{lang="EN-US"}]{#struct_0_65458_x3406_x1487216687}

[[对端导致]{style="font-family:宋体"}[holdtimer]{lang="EN-US"}]{#struct_0_65458_x3406_x1487347759}[超时]{style="font-family:宋体"}

[[5/0]{lang="EN-US"}]{#struct_0_65458_x3406_x1487478831}

[[connection retry timer expires]{lang="EN-US"}]{#struct_0_65458_x3406_x1486561327}

[[ConnectRetry]{lang="EN-US"}]{#struct_0_65458_x3406_x1487151152}[定时器超时]{style="font-family:宋体"}

[[TCP_CR_Acked event received]{lang="EN-US"}]{#struct_0_65458_x3406_x1487282224}

[[收到了]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1487413296}[TCP_CR_Acked]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TCP_Connection_Confirmed event received]{lang="EN-US"}]{#struct_0_65458_x3406_x1487544368}

[[收到了]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1486626864}[TCP_Connection_Confirmed]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[5/3]{lang="EN-US"}]{#struct_0_65458_x3406_x1487151153}

[[open message received]{lang="EN-US"}]{#struct_0_65458_x3406_x1487347761}

[[收到]{style="font-family:宋体"}[open]{lang="EN-US"}]{#struct_0_65458_x3406_x1487478833}[消息]{style="font-family:宋体"}

[[6/0]{lang="EN-US"}]{#struct_0_65458_x3406_x1486561329}

[[manualstop event received]{lang="EN-US"}]{#struct_0_65458_x3406_x1487085618}

[[收到]{style="font-family:宋体"}[manualstop]{lang="EN-US"}]{#struct_0_65458_x3406_x1487216690}[事件]{style="font-family:宋体"}

[[physical interface configuration changed]{lang="EN-US"}]{#struct_0_65458_x3406_x1487413298}

[[物理配置改变，比如接口变化]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1487544370}

[[session down event received from BFD]{lang="EN-US"}]{#struct_0_65458_x3406_x1486626866}

[[收到]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_65458_x3406_78932792}[会话]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[6/1]{lang="EN-US"}]{#struct_0_65458_x3406_78736184}

[[maximum number of prefixes reached]{lang="EN-US"}]{#struct_0_65458_x3406_78605112}

[[前缀数超过]{style="font-family:宋体"}**[peer route-limit]{lang="EN-US"}**]{#struct_0_65458_x3406_79522616}[所配置的数目]{style="font-family:宋体"}

[[maximum number of *address-family* prefixes reached]{lang="EN-US"}]{#struct_0_65458_x3406_78998327}

[*[address-family]{lang="EN-US"}*]{#struct_0_65458_x3406_78801719}[地址族的前缀数超过]{style="font-family:宋体"}**[peer route-limit]{lang="EN-US"}**[所配置的数目，]{style="font-family:宋体"}*[address-family]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 unicast]{lang="EN-US"}]{#struct_0_65458_x3406_78670647}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 unicast]{lang="EN-US"}]{#struct_0_65458_x3406_78539575}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_79457079}[：表示]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPNv6]{lang="EN-US"}]{#struct_0_65458_x3406_78867254}[：表示]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族]{style="font-family:宋体"}

[[6/2]{lang="EN-US"}]{#struct_0_65458_x3406_78736182}

[[configuration of peer ignore changed]{lang="EN-US"}]{#struct_0_65458_x3406_78605110}

[[配置]{style="font-family:宋体"}**[peer ignore]{lang="EN-US"}**]{#struct_0_65458_x3406_78998325}[命令]{style="font-family:宋体"}

[[6/3]{lang="EN-US"}]{#struct_0_65458_x3406_78801717}

[[address family deleted]{lang="EN-US"}]{#struct_0_65458_x3406_78670645}

[[地址族被删除]{style="font-family:宋体"}]{#struct_0_65458_x3406_78539573}

[[peer disabled]{lang="EN-US"}]{#struct_0_65458_x3406_78998324}

[[关闭对等体]{style="font-family:宋体"}]{#struct_0_65458_x3406_78867252}

[[6/4]{lang="EN-US"}]{#struct_0_65458_x3406_78736180}

[[administrative reset]{lang="EN-US"}]{#struct_0_65458_x3406_78539572}

[[执行]{style="font-family:宋体"}**[reset bgp]{lang="EN-US"}**]{#struct_0_65458_x3406_78932787}[命令或者配置改变导致]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话重启]{style="font-family:宋体"}

[[6/5]{lang="EN-US"}]{#struct_0_65458_x3406_78801715}

[[connection rejected]{lang="EN-US"}]{#struct_0_65458_x3406_78605107}

[[连接被拒绝]{style="font-family:宋体"}]{#struct_0_65458_x3406_79522611}

[[6/6]{lang="EN-US"}]{#struct_0_65458_x3406_1645016733}

[[other configuration change]{lang="EN-US"}]{#struct_0_65458_x3406_1644885661}

[[其他配置变化]{style="font-family:宋体"}]{#struct_0_65458_x3406_1644754589}

[[6/7]{lang="EN-US"}]{#struct_0_65458_x3406_1645606557}

[[connection collision resolution]{lang="EN-US"}]{#struct_0_65458_x3406_1645082268}

[[连接冲突]{style="font-family:宋体"}]{#struct_0_65458_x3406_1644885660}

[[two connections exist and one uses MD5]{lang="EN-US"}]{#struct_0_65458_x3406_1644754588}

[[存在两个连接，且其中一个配置了]{style="font-family:宋体"}[MD5]{lang="EN-US"}]{#struct_0_65458_x3406_1644623516}[认证]{style="font-family:宋体"}

[[6/8]{lang="EN-US"}]{#struct_0_65458_x3406_1645082267}

[[no memory to process the attribute]{lang="EN-US"}]{#struct_0_65458_x3406_1644951195}

[[解析属性时内存不够]{style="font-family:宋体"}]{#struct_0_65458_x3406_1644754587}

[[no memory for the route]{lang="EN-US"}]{#struct_0_65458_x3406_1644623515}

[[生成路由或者标签块信息时，获取不到内存]{style="font-family:宋体"}]{#struct_0_65458_x3406_1645082266}

[[no memory to generate unreachable NLRI]{lang="EN-US"}]{#struct_0_65458_x3406_1644951194}

[[封装]{style="font-family:宋体"}[unreachable NLRI]{lang="EN-US"}]{#struct_0_65458_x3406_1644754586}[时申请不到内存]{style="font-family:宋体"}

[[no memory to generate a message]{lang="EN-US"}]{#struct_0_65458_x3406_1644623514}

[[封装报文时申请不到内存]{style="font-family:宋体"}]{#struct_0_65458_x3406_1645541018}

[[can't get the VPN RD]{lang="EN-US"}]{#struct_0_65458_x3406_1644951193}

[[解析前缀时获取不到]{style="font-family:宋体"}[RD]{lang="EN-US"}]{#struct_0_65458_x3406_1644820121}

[[can't get the VPN routing table]{lang="EN-US"}]{#struct_0_65458_x3406_1644623513}

[[解析前缀时获取不到]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_65458_x3406_1645541017}[路由表]{style="font-family:宋体"}

[[can't get the attributes]{lang="EN-US"}]{#struct_0_65458_x3406_1644951192}

[[解析前缀时获取不到属性]{style="font-family:宋体"}]{#struct_0_65458_x3406_1644820120}

[[entered severe memory state]{lang="EN-US"}]{#struct_0_65458_x3406_1644623512}

[[进入二级门限告警]{style="font-family:宋体"}]{#struct_0_65458_x3406_1645541016}

[[entered critical memory state]{lang="EN-US"}]{#struct_0_65458_x3406_x1083932158}

[[进入三级门限告警]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1084063230}

[ ]{lang="EN-US"}

::: {#-332904905 .myid}
[]{#_Toc404788618}[]{#struct_0_65458_x3406_x674405772}[]{#_Toc307230769}[]{#_Toc361658927}[]{#_Toc361659514}[]{#_Toc361660101}[]{#_Toc361663674}[]{#_Toc361747134}[]{#_Toc361819497}[]{#_Toc361658928}[]{#_Toc361659515}[]{#_Toc361660102}[]{#_Toc361663675}[]{#_Toc361747135}[]{#_Toc361819498}[]{#_Toc361658929}[]{#_Toc361659516}[]{#_Toc361660103}[]{#_Toc361663676}[]{#_Toc361747136}[]{#_Toc361819499}[]{#_Toc361658930}[]{#_Toc361659517}[]{#_Toc361660104}[]{#_Toc361663677}[]{#_Toc361747137}[]{#_Toc361819500}[]{#_Toc361658931}[]{#_Toc361659518}[]{#_Toc361660105}[]{#_Toc361663678}[]{#_Toc361747138}[]{#_Toc361819501}[]{#_Toc361658932}[]{#_Toc361659519}[]{#_Toc361660106}[]{#_Toc361663679}[]{#_Toc361747139}[]{#_Toc361819502}[]{#_Toc361658933}[]{#_Toc361659520}[]{#_Toc361660107}[]{#_Toc361663680}[]{#_Toc361747140}[]{#_Toc361819503}[]{#_Toc361658934}[]{#_Toc361659521}[]{#_Toc361660108}[]{#_Toc361663681}[]{#_Toc361747141}[]{#_Toc361819504}[]{#_Toc361658935}[]{#_Toc361659522}[]{#_Toc361660109}[]{#_Toc361663682}[]{#_Toc361747142}[]{#_Toc361819505}[]{#_Toc361658936}[]{#_Toc361659523}[]{#_Toc361660110}[]{#_Toc361663683}[]{#_Toc361747143}[]{#_Toc361819506}[]{#_Toc361658937}[]{#_Toc361659524}[]{#_Toc361660111}[]{#_Toc361663684}[]{#_Toc361747144}[]{#_Toc361819507}[]{#_Toc361658938}[]{#_Toc361659525}[]{#_Toc361660112}[]{#_Toc361663685}[]{#_Toc361747145}[]{#_Toc361819508}[]{#_Toc361658939}[]{#_Toc361659526}[]{#_Toc361660113}[]{#_Toc361663686}[]{#_Toc361747146}[]{#_Toc361819509}[]{#_Toc361658940}[]{#_Toc361659527}[]{#_Toc361660114}[]{#_Toc361663687}[]{#_Toc361747147}[]{#_Toc361819510}[]{#_Toc361658941}[]{#_Toc361659528}[]{#_Toc361660115}[]{#_Toc361663688}[]{#_Toc361747148}[]{#_Toc361819511}[]{#_Toc361658942}[]{#_Toc361659529}[]{#_Toc361660116}[]{#_Toc361663689}[]{#_Toc361747149}[]{#_Toc361819512}[]{#_Toc361658943}[]{#_Toc361659530}[]{#_Toc361660117}[]{#_Toc361663690}[]{#_Toc361747150}[]{#_Toc361819513}[]{#_Toc361658944}[]{#_Toc361659531}[]{#_Toc361660118}[]{#_Toc361663691}[]{#_Toc361747151}[]{#_Toc361819514}[]{#_Toc361658945}[]{#_Toc361659532}[]{#_Toc361660119}[]{#_Toc361663692}[]{#_Toc361747152}[]{#_Toc361819515}[]{#_Toc361658946}[]{#_Toc361659533}[]{#_Toc361660120}[]{#_Toc361663693}[]{#_Toc361747153}[]{#_Toc361819516}[]{#_Toc361658947}[]{#_Toc361659534}[]{#_Toc361660121}[]{#_Toc361663694}[]{#_Toc361747154}[]{#_Toc361819517}[]{#_Toc361658948}[]{#_Toc361659535}[]{#_Toc361660122}[]{#_Toc361663695}[]{#_Toc361747155}[]{#_Toc361819518}[]{#_Toc361658949}[]{#_Toc361659536}[]{#_Toc361660123}[]{#_Toc361663696}[]{#_Toc361747156}[]{#_Toc361819519}[]{#_Toc361658950}[]{#_Toc361659537}[]{#_Toc361660124}[]{#_Toc361663697}[]{#_Toc361747157}[]{#_Toc361819520}[]{#_Toc361658951}[]{#_Toc361659538}[]{#_Toc361660125}[]{#_Toc361663698}[]{#_Toc361747158}[]{#_Toc361819521}[]{#_Toc361658952}[]{#_Toc361659539}[]{#_Toc361660126}[]{#_Toc361663699}[]{#_Toc361747159}[]{#_Toc361819522}[]{#_Toc361658953}[]{#_Toc361659540}[]{#_Toc361660127}[]{#_Toc361663700}[]{#_Toc361747160}[]{#_Toc361819523}[]{#_Toc361658954}[]{#_Toc361659541}[]{#_Toc361660128}[]{#_Toc361663701}[]{#_Toc361747161}[]{#_Toc361819524}[]{#_Toc361658955}[]{#_Toc361659542}[]{#_Toc361660129}[]{#_Toc361663702}[]{#_Toc361747162}[]{#_Toc361819525}[]{#_Toc361658956}[]{#_Toc361659543}[]{#_Toc361660130}[]{#_Toc361663703}[]{#_Toc361747163}[]{#_Toc361819526}[]{#_Toc361658957}[]{#_Toc361659544}[]{#_Toc361660131}[]{#_Toc361663704}[]{#_Toc361747164}[]{#_Toc361819527}[]{#_Toc361658958}[]{#_Toc361659545}[]{#_Toc361660132}[]{#_Toc361663705}[]{#_Toc361747165}[]{#_Toc361819528}[]{#_Toc361658959}[]{#_Toc361659546}[]{#_Toc361660133}[]{#_Toc361663706}[]{#_Toc361747166}[]{#_Toc361819529}[]{#_Toc361658960}[]{#_Toc361659547}[]{#_Toc361660134}[]{#_Toc361663707}[]{#_Toc361747167}[]{#_Toc361819530}[]{#_Toc361658961}[]{#_Toc361659548}[]{#_Toc361660135}[]{#_Toc361663708}[]{#_Toc361747168}[]{#_Toc361819531}[]{#_Toc361658962}[]{#_Toc361659549}[]{#_Toc361660136}[]{#_Toc361663709}[]{#_Toc361747169}[]{#_Toc361819532}[]{#_Toc361658963}[]{#_Toc361659550}[]{#_Toc361660137}[]{#_Toc361663710}[]{#_Toc361747170}[]{#_Toc361819533}[]{#_Toc361659003}[]{#_Toc361659590}[]{#_Toc361660177}[]{#_Toc361663750}[]{#_Toc361747210}[]{#_Toc361819573}[]{#_Toc361659004}[]{#_Toc361659591}[]{#_Toc361660178}[]{#_Toc361663751}[]{#_Toc361747211}[]{#_Toc361819574}[]{#_Toc361659005}[]{#_Toc361659592}[]{#_Toc361660179}[]{#_Toc361663752}[]{#_Toc361747212}[]{#_Toc361819575}[]{#_Toc361659006}[]{#_Toc361659593}[]{#_Toc361660180}[]{#_Toc361663753}[]{#_Toc361747213}[]{#_Toc361819576}[]{#_Toc361659007}[]{#_Toc361659594}[]{#_Toc361660181}[]{#_Toc361663754}[]{#_Toc361747214}[]{#_Toc361819577}[]{#_Toc361659008}[]{#_Toc361659595}[]{#_Toc361660182}[]{#_Toc361663755}[]{#_Toc361747215}[]{#_Toc361819578}[]{#_Toc361659009}[]{#_Toc361659596}[]{#_Toc361660183}[]{#_Toc361663756}[]{#_Toc361747216}[]{#_Toc361819579}[]{#_Toc361659010}[]{#_Toc361659597}[]{#_Toc361660184}[]{#_Toc361663757}[]{#_Toc361747217}[]{#_Toc361819580}[]{#_Toc361659011}[]{#_Toc361659598}[]{#_Toc361660185}[]{#_Toc361663758}[]{#_Toc361747218}[]{#_Toc361819581}[]{#_Toc361659012}[]{#_Toc361659599}[]{#_Toc361660186}[]{#_Toc361663759}[]{#_Toc361747219}[]{#_Toc361819582}[]{#_Toc361659013}[]{#_Toc361659600}[]{#_Toc361660187}[]{#_Toc361663760}[]{#_Toc361747220}[]{#_Toc361819583}[]{#_Toc361659014}[]{#_Toc361659601}[]{#_Toc361660188}[]{#_Toc361663761}[]{#_Toc361747221}[]{#_Toc361819584}[]{#_Toc361659015}[]{#_Toc361659602}[]{#_Toc361660189}[]{#_Toc361663762}[]{#_Toc361747222}[]{#_Toc361819585}[]{#_Toc361659016}[]{#_Toc361659603}[]{#_Toc361660190}[]{#_Toc361663763}[]{#_Toc361747223}[]{#_Toc361819586}[]{#_Toc361659017}[]{#_Toc361659604}[]{#_Toc361660191}[]{#_Toc361663764}[]{#_Toc361747224}[]{#_Toc361819587}[]{#_Toc361659018}[]{#_Toc361659605}[]{#_Toc361660192}[]{#_Toc361663765}[]{#_Toc361747225}[]{#_Toc361819588}[]{#_Toc361659019}[]{#_Toc361659606}[]{#_Toc361660193}[]{#_Toc361663766}[]{#_Toc361747226}[]{#_Toc361819589}[]{#_Toc361659020}[]{#_Toc361659607}[]{#_Toc361660194}[]{#_Toc361663767}[]{#_Toc361747227}[]{#_Toc361819590}[]{#_Toc361659021}[]{#_Toc361659608}[]{#_Toc361660195}[]{#_Toc361663768}[]{#_Toc361747228}[]{#_Toc361819591}[]{#_Toc361659022}[]{#_Toc361659609}[]{#_Toc361660196}[]{#_Toc361663769}[]{#_Toc361747229}[]{#_Toc361819592}[]{#_Toc361659023}[]{#_Toc361659610}[]{#_Toc361660197}[]{#_Toc361663770}[]{#_Toc361747230}[]{#_Toc361819593}[]{#_Toc361659024}[]{#_Toc361659611}[]{#_Toc361660198}[]{#_Toc361663771}[]{#_Toc361747231}[]{#_Toc361819594}[]{#_Toc361659025}[]{#_Toc361659612}[]{#_Toc361660199}[]{#_Toc361663772}[]{#_Toc361747232}[]{#_Toc361819595}[]{#_Toc361659026}[]{#_Toc361659613}[]{#_Toc361660200}[]{#_Toc361663773}[]{#_Toc361747233}[]{#_Toc361819596}[]{#_Toc361659027}[]{#_Toc361659614}[]{#_Toc361660201}[]{#_Toc361663774}[]{#_Toc361747234}[]{#_Toc361819597}[]{#_Toc361659028}[]{#_Toc361659615}[]{#_Toc361660202}[]{#_Toc361663775}[]{#_Toc361747235}[]{#_Toc361819598}[]{#_Toc361659029}[]{#_Toc361659616}[]{#_Toc361660203}[]{#_Toc361663776}[]{#_Toc361747236}[]{#_Toc361819599}[]{#_Toc361659030}[]{#_Toc361659617}[]{#_Toc361660204}[]{#_Toc361663777}[]{#_Toc361747237}[]{#_Toc361819600}[]{#_Toc361659031}[]{#_Toc361659618}[]{#_Toc361660205}[]{#_Toc361663778}[]{#_Toc361747238}[]{#_Toc361819601}[]{#_Toc361659032}[]{#_Toc361659619}[]{#_Toc361660206}[]{#_Toc361663779}[]{#_Toc361747239}[]{#_Toc361819602}[]{#_Toc361659033}[]{#_Toc361659620}[]{#_Toc361660207}[]{#_Toc361663780}[]{#_Toc361747240}[]{#_Toc361819603}[]{#_Toc361659034}[]{#_Toc361659621}[]{#_Toc361660208}[]{#_Toc361663781}[]{#_Toc361747241}[]{#_Toc361819604}[]{#_Toc361659035}[]{#_Toc361659622}[]{#_Toc361660209}[]{#_Toc361663782}[]{#_Toc361747242}[]{#_Toc361819605}[]{#_Toc361659036}[]{#_Toc361659623}[]{#_Toc361660210}[]{#_Toc361663783}[]{#_Toc361747243}[]{#_Toc361819606}[]{#_Toc361659037}[]{#_Toc361659624}[]{#_Toc361660211}[]{#_Toc361663784}[]{#_Toc361747244}[]{#_Toc361819607}[]{#_Toc361659134}[]{#_Toc361659721}[]{#_Toc361660308}[]{#_Toc361663881}[]{#_Toc361747341}[]{#_Toc361819704}[]{#_Toc361659135}[]{#_Toc361659722}[]{#_Toc361660309}[]{#_Toc361663882}[]{#_Toc361747342}[]{#_Toc361819705}[]{#_Toc361659136}[]{#_Toc361659723}[]{#_Toc361660310}[]{#_Toc361663883}[]{#_Toc361747343}[]{#_Toc361819706}[]{#_Toc361659137}[]{#_Toc361659724}[]{#_Toc361660311}[]{#_Toc361663884}[]{#_Toc361747344}[]{#_Toc361819707}[]{#_Toc361659138}[]{#_Toc361659725}[]{#_Toc361660312}[]{#_Toc361663885}[]{#_Toc361747345}[]{#_Toc361819708}[]{#_Toc361659139}[]{#_Toc361659726}[]{#_Toc361660313}[]{#_Toc361663886}[]{#_Toc361747346}[]{#_Toc361819709}[]{#_Toc361659140}[]{#_Toc361659727}[]{#_Toc361660314}[]{#_Toc361663887}[]{#_Toc361747347}[]{#_Toc361819710}[]{#_Toc361659141}[]{#_Toc361659728}[]{#_Toc361660315}[]{#_Toc361663888}[]{#_Toc361747348}[]{#_Toc361819711}[]{#_Toc361659142}[]{#_Toc361659729}[]{#_Toc361660316}[]{#_Toc361663889}[]{#_Toc361747349}[]{#_Toc361819712}[]{#_Toc361659143}[]{#_Toc361659730}[]{#_Toc361660317}[]{#_Toc361663890}[]{#_Toc361747350}[]{#_Toc361819713}[]{#_Toc361659144}[]{#_Toc361659731}[]{#_Toc361660318}[]{#_Toc361663891}[]{#_Toc361747351}[]{#_Toc361819714}[]{#_Toc361659166}[]{#_Toc361659753}[]{#_Toc361660340}[]{#_Toc361663913}[]{#_Toc361747373}[]{#_Toc361819736}

**BGP \-- BGP配置命令 \-- display bgp routing-table dampened**

------------------------------------------------------------------------

[**[display bgp routing-table dampened]{lang="EN-US"}**]{#struct_0_65458_x3406_x1958256554}[命令用来显示衰减的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1777087699}

[**[display bgp routing-table dampened ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** } { ]{lang="EN-US"}**[multicast]{lang="EN-US"}**[ \| \[ ]{lang="EN-US"}**[unicast ]{lang="EN-US"}**[\] \[ **vpn-instance** ]{lang="EN-US"}*[vpn-instance-name ]{lang="EN-US"}*[\] }]{lang="EN-US"}]{#struct_0_65458_x3406_784873585}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1574581321}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1941127533}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_88472482}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_63625660}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1950744263}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2059948618}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1949909986}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_284125858}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1501049539}[：显示衰减的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x1461535333}[：显示衰减的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1501639364}[：显示衰减的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1501573828}[：显示衰减的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1713888243}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[衰减的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网衰减的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1163700472}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_88931235}[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1488524313}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1626190147}[显示公网衰减的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table dampened ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_88996771}

[ ]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.135]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            From            Reuse                         Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[  de 20.1.1.0/24        10.1.1.2        00:56:27                      100i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1501967044}[显示公网衰减的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table dampened ipv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1501115076}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.135]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[  de Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     From    : 10.1.1.1                                 Reuse     : 00:39:49]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[ ]{lang="EN-US"}

[  de Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     From    : 1::1                                     Reuse     : 00:39:49]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[]{#struct_0_65458_x3406_1205845586}[]{#_Toc99255040}[[表1-12 ]{lang="EN-US"}[display bgp routing-table dampened]{lang="EN-US"}]{#_Toc81210267}[命令]{style="font-family:
黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x282648501}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x191862287}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1192346245}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_x1501639357}

[[衰减的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1501573821}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x734327427}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_89062307}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_x944958216}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x319637876}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\* -- valid]{lang="EN-US"}]{#struct_0_65458_x3406_x1751103621}[：合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> -- best]{lang="EN-US"}]{#struct_0_65458_x3406_x2024353081}[：优选最佳路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d - dampened]{lang="EN-US"}]{#struct_0_65458_x3406_89193379}[：振荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h -- history]{lang="EN-US"}]{#struct_0_65458_x3406_175008461}[：历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s -- suppressed]{lang="EN-US"}]{#struct_0_65458_x3406_392385189}[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S -- stale]{lang="EN-US"}]{#struct_0_65458_x3406_1701551752}[：过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- internal]{lang="EN-US"}]{#struct_0_65458_x3406_x404580388}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- external]{lang="EN-US"}]{#struct_0_65458_x3406_89258915}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="IT"}]{#struct_0_65458_x3406_1253546383}

[[路由信息的来源]{style="font-family:宋体"}]{#struct_0_65458_x3406_x820090668}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1456209806}[：表示路由产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[内。通过]{lang="EN-US" style="font-family:宋体"}**[network]{lang="EN-US"}**[命令发布路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="EN-US"}]{#struct_0_65458_x3406_x432465382}[：表示路由是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="EN-US"}[，外部网关协议）学到的。]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="EN-US"}]{#struct_0_65458_x3406_89324451}[：表示路由的来源无法确定。从]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="EN-US"}

[[Network]{lang="IT"}]{#struct_0_65458_x3406_1929232156}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_473963867}

[[PrefixLen]{lang="EN-US"}]{#struct_0_65458_x3406_x1501901501}

[[目的网络地址的前缀长度]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1501835965}

[[From]{lang="EN-US"}]{#struct_0_65458_x3406_1987880374}

[[发布该路由的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_89389987}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Reuse]{lang="EN-US"}]{#struct_0_65458_x3406_x1262638330}

[[路由恢复可用的时间，即还需要等待多长时间该路由将由不可用状态转为可用状态]{style="font-family:宋体"}]{#struct_0_65458_x3406_1559912432}

[[Path/Ogn]{lang="EN-US"}]{#struct_0_65458_x3406_x49661260}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_88406947}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和路由信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_1664246388}[属性记录了此路由经过的所有]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_x127201369}[属性标记了此路由如何成为]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_557217099}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_501031914}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset bgp dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_723526789}

::: {#497567758 .myid}
[]{#_Toc404788619}[]{#struct_0_65458_x3406_x1017496939}[]{#_Toc307230771}[]{#_Toc366152670}[]{#_Toc366166413}[]{#_Toc366219949}[]{#_Toc366152671}[]{#_Toc366166414}[]{#_Toc366219950}[]{#_Toc366152672}[]{#_Toc366166415}[]{#_Toc366219951}[]{#_Toc366152673}[]{#_Toc366166416}[]{#_Toc366219952}[]{#_Toc366152674}[]{#_Toc366166417}[]{#_Toc366219953}[]{#_Toc366152675}[]{#_Toc366166418}[]{#_Toc366219954}[]{#_Toc366152676}[]{#_Toc366166419}[]{#_Toc366219955}[]{#_Toc366152677}[]{#_Toc366166420}[]{#_Toc366219956}[]{#_Toc366152678}[]{#_Toc366166421}[]{#_Toc366219957}[]{#_Toc366152679}[]{#_Toc366166422}[]{#_Toc366219958}[]{#_Toc366152680}[]{#_Toc366166423}[]{#_Toc366219959}[]{#_Toc366152681}[]{#_Toc366166424}[]{#_Toc366219960}[]{#_Toc366152682}[]{#_Toc366166425}[]{#_Toc366219961}[]{#_Toc366152683}[]{#_Toc366166426}[]{#_Toc366219962}[]{#_Toc366152684}[]{#_Toc366166427}[]{#_Toc366219963}[]{#_Toc366152685}[]{#_Toc366166428}[]{#_Toc366219964}[]{#_Toc366152686}[]{#_Toc366166429}[]{#_Toc366219965}[]{#_Toc366152687}[]{#_Toc366166430}[]{#_Toc366219966}[]{#_Toc366152688}[]{#_Toc366166431}[]{#_Toc366219967}[]{#_Toc366152689}[]{#_Toc366166432}[]{#_Toc366219968}[]{#_Toc366152690}[]{#_Toc366166433}[]{#_Toc366219969}[]{#_Toc366152691}[]{#_Toc366166434}[]{#_Toc366219970}[]{#_Toc366152692}[]{#_Toc366166435}[]{#_Toc366219971}[]{#_Toc366152693}[]{#_Toc366166436}[]{#_Toc366219972}[]{#_Toc366152694}[]{#_Toc366166437}[]{#_Toc366219973}[]{#_Toc366152695}[]{#_Toc366166438}[]{#_Toc366219974}[]{#_Toc366152696}[]{#_Toc366166439}[]{#_Toc366219975}[]{#_Toc366152697}[]{#_Toc366166440}[]{#_Toc366219976}[]{#_Toc366152698}[]{#_Toc366166441}[]{#_Toc366219977}[]{#_Toc366152699}[]{#_Toc366166442}[]{#_Toc366219978}[]{#_Toc366152700}[]{#_Toc366166443}[]{#_Toc366219979}[]{#_Toc366152701}[]{#_Toc366166444}[]{#_Toc366219980}[]{#_Toc366152702}[]{#_Toc366166445}[]{#_Toc366219981}[]{#_Toc366152703}[]{#_Toc366166446}[]{#_Toc366219982}[]{#_Toc366152747}[]{#_Toc366166490}[]{#_Toc366220026}[]{#_Toc366152748}[]{#_Toc366166491}[]{#_Toc366220027}[]{#_Toc366152749}[]{#_Toc366166492}[]{#_Toc366220028}[]{#_Toc366152750}[]{#_Toc366166493}[]{#_Toc366220029}

**BGP \-- BGP配置命令 \-- display bgp routing-table flap-info**

------------------------------------------------------------------------

[**[display bgp routing-table flap-info]{lang="EN-US"}**]{#struct_0_65458_x3406_88996769}[命令用来显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1169109741}

[**[display bgp routing-table flap-info ipv4]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[{ **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *network-address* \[ { *mask* \| *mask-length* } \[ **longest-match** \] \] \| **as-path-acl** *as-path-acl-number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_234955636}

[**[display bgp routing-table flap-info ipv6]{lang="NO-BOK"}**[ ]{lang="NO-BOK"}[{ **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *network-address* *prefix-length* \| **as-path-acl** *as-path-acl-number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_64510120}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x423593000}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x484090102}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_283329542}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2051195215}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_581161255}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_89062305}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1327295240}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1487541414}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_64313512}[：显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_64379048}[：显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_856175124}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播路由的振荡统计信息。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_64182440}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播路由的振荡统计信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_988801899}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}

[*[network-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1167200215}[：显示匹配指定目的网络地址的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由或组播路由的振荡统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_x1880697625}[：目的网络地址的掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_492855271}[：目的网络地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[longest-match]{lang="EN-US"}**]{#struct_0_65458_x3406_x1088878539}[：指定根据如下方法判断显示哪条]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由或组播路由的振荡统计信息]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[将用户输入的网络地址和路由的掩码进行与操作；]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1963151994}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[计算结果与路由的网段地址相同，且掩码小于等于用户输入子网掩码的路由中，子网掩码最长的路由将被显示出来。]{style="font-family:宋体"}]{#struct_0_65458_x3406_89127841}

[*[network-address prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_64379047}[：显示匹配指定目的网络地址及前缀长度的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由或组播路由的振荡统计信息。]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[目的网络地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[as-path-acl ]{lang="EN-US"}***[as-path-acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_1002490010}[：显示匹配指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[as-path-acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x297000091}

[[执行]{style="font-family:宋体"}]{#struct_0_65458_x3406_462300472}**[display bgp routing-table flap-info ipv4]{lang="NO-BOK"}**[命令时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定了]{style="font-family:宋体"}]{#struct_0_65458_x3406_2027812840}*[network-address]{lang="EN-US"}*[参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则显示该]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由或组播路由的振荡统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[network-address mask]{lang="EN-US"}*]{#struct_0_65458_x3406_x845279343}[或]{lang="EN-US" style="font-family:宋体"}*[network-address mask-l]{lang="EN-US"}[ength]{lang="EN-US"}*[参数，没有指定]{lang="EN-US" style="font-family:宋体"}**[longe]{lang="EN-US"}[st]{lang="EN-US"}[-]{lang="EN-US"}[match]{lang="EN-US"}**[参数，则显示与指定目的网络]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址和网络掩码（或掩码长度）精确匹配的]{lang="EN-US" style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由]{lang="EN-US" style="font-family:宋体"}[或组播路由]{style="font-family:宋体"}[的振荡统计信息]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_89193377}[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1736676659}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_238599960}[显示公网内所有]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的振荡统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table flap-info ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_89258913}

[ ]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.135]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            From            Flaps  Duration  Reuse        Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[  de 20.1.1.0/24        10.1.1.2        1      00:02:36  00:53:58     100i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1630594057}[显示公网内所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的振荡统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table flap-info ipv6]{lang="EN-US"}]{#struct_0_65458_x3406_1630397449}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.135]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[  de Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     From    : 10.1.1.1                                 Flaps     : 5]{lang="EN-US"}

[     Duration: 00:03:25                                 Reuse     : 00:39:28]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[ ]{lang="EN-US"}

[  de Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     From    : 1::1                                     Flaps     : 5]{lang="EN-US"}

[     Duration: 00:03:25                                 Reuse     : 00:39:28]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display bgp routing-table flap-info]{lang="EN-US"}]{#struct_0_65458_x3406_871209359}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x531230261}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1917402909}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_268498373}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_1630331913}

[[振荡路由的总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_1630135305}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_2087777547}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_89324449}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_x1166199881}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_65458_x3406_100396875}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\* -- valid]{lang="EN-US"}]{#struct_0_65458_x3406_x1109866592}[：合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> -- best]{lang="EN-US"}]{#struct_0_65458_x3406_1367187644}[：优选最佳路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d - dampened]{lang="EN-US"}]{#struct_0_65458_x3406_88406945}[：振荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h -- history]{lang="EN-US"}]{#struct_0_65458_x3406_2046583412}[：历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s -- suppressed]{lang="EN-US"}]{#struct_0_65458_x3406_2006565596}[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S -- stale]{lang="EN-US"}]{#struct_0_65458_x3406_x187343222}[：过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- internal]{lang="EN-US"}]{#struct_0_65458_x3406_88472481}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- external]{lang="EN-US"}]{#struct_0_65458_x3406_x1892689476}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="IT"}]{#struct_0_65458_x3406_413856647}

[[路由信息的来源]{style="font-family:宋体"}]{#struct_0_65458_x3406_x267118838}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="EN-US"}]{#struct_0_65458_x3406_1222736872}[：表示路由产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[内。通过]{lang="EN-US" style="font-family:宋体"}**[network]{lang="EN-US"}**[命令发布路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="EN-US"}]{#struct_0_65458_x3406_1655015177}[：表示路由是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="EN-US"}[，外部网关协议）学到的。]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="EN-US"}]{#struct_0_65458_x3406_x2015306224}[：表示路由的来源无法确定。从]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="EN-US"}

[[Network]{lang="IT"}]{#struct_0_65458_x3406_2028063750}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_1349027125}

[[PrefixLen]{lang="EN-US"}]{#struct_0_65458_x3406_1631118345}

[[目的网络地址的前缀长度]{style="font-family:宋体"}]{#struct_0_65458_x3406_1630594056}

[[From]{lang="EN-US"}]{#struct_0_65458_x3406_1655080713}

[[发布该路由的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x129948399}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Flaps]{lang="EN-US"}]{#struct_0_65458_x3406_x460282210}

[[路由振荡的次数，即路由从可达状态变为不可达状态，及可达路由的属性发生变化的次数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x921040425}

[[Duration]{lang="EN-US"}]{#struct_0_65458_x3406_x529530762}

[[路由发生振荡的持续时间]{style="font-family:宋体"}]{#struct_0_65458_x3406_1655146249}

[[Reuse]{lang="EN-US"}]{#struct_0_65458_x3406_x2012780205}

[[路由恢复可用的时间，即还需要等待多长时间该路由将由不可用状态转为可用状态]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2106681664}

[[Path/Ogn]{lang="EN-US"}]{#struct_0_65458_x3406_468587742}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1655211785}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和路由信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_1457434799}[属性记录了此路由经过的所有]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_x26324440}[属性标记了此路由如何成为]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1699876082}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_363310369}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset bgp flap-info]{lang="EN-US"}**]{#struct_0_65458_x3406_1655277321}

::: {#-345245323 .myid}
[]{#_Toc404788620}[]{#struct_0_65458_x3406_x52991765}[]{#_Toc366077074}[]{#_Toc351482996}[]{#_Toc319500448}[]{#_Toc319650198}[]{#_Toc319918680}[]{#_Toc319937744}[]{#_Toc366152752}[]{#_Toc366166495}[]{#_Toc366220031}[]{#_Toc366152753}[]{#_Toc366166496}[]{#_Toc366220032}[]{#_Toc366152754}[]{#_Toc366166497}[]{#_Toc366220033}[]{#_Toc366152755}[]{#_Toc366166498}[]{#_Toc366220034}[]{#_Toc366152756}[]{#_Toc366166499}[]{#_Toc366220035}[]{#_Toc366152757}[]{#_Toc366166500}[]{#_Toc366220036}[]{#_Toc366152758}[]{#_Toc366166501}[]{#_Toc366220037}[]{#_Toc366152759}[]{#_Toc366166502}[]{#_Toc366220038}[]{#_Toc366152760}[]{#_Toc366166503}[]{#_Toc366220039}[]{#_Toc366152761}[]{#_Toc366166504}[]{#_Toc366220040}[]{#_Toc366152762}[]{#_Toc366166505}[]{#_Toc366220041}[]{#_Toc366152763}[]{#_Toc366166506}[]{#_Toc366220042}[]{#_Toc366152764}[]{#_Toc366166507}[]{#_Toc366220043}[]{#_Toc366152765}[]{#_Toc366166508}[]{#_Toc366220044}[]{#_Toc366152766}[]{#_Toc366166509}[]{#_Toc366220045}[]{#_Toc366152767}[]{#_Toc366166510}[]{#_Toc366220046}[]{#_Toc366152768}[]{#_Toc366166511}[]{#_Toc366220047}[]{#_Toc366152769}[]{#_Toc366166512}[]{#_Toc366220048}[]{#_Toc366152770}[]{#_Toc366166513}[]{#_Toc366220049}[]{#_Toc366152771}[]{#_Toc366166514}[]{#_Toc366220050}[]{#_Toc366152772}[]{#_Toc366166515}[]{#_Toc366220051}[]{#_Toc366152773}[]{#_Toc366166516}[]{#_Toc366220052}[]{#_Toc366152774}[]{#_Toc366166517}[]{#_Toc366220053}[]{#_Toc366152775}[]{#_Toc366166518}[]{#_Toc366220054}[]{#_Toc366152776}[]{#_Toc366166519}[]{#_Toc366220055}[]{#_Toc366152777}[]{#_Toc366166520}[]{#_Toc366220056}[]{#_Toc366152778}[]{#_Toc366166521}[]{#_Toc366220057}[]{#_Toc366152779}[]{#_Toc366166522}[]{#_Toc366220058}[]{#_Toc366152780}[]{#_Toc366166523}[]{#_Toc366220059}[]{#_Toc366152781}[]{#_Toc366166524}[]{#_Toc366220060}[]{#_Toc366152782}[]{#_Toc366166525}[]{#_Toc366220061}[]{#_Toc366152783}[]{#_Toc366166526}[]{#_Toc366220062}[]{#_Toc366152784}[]{#_Toc366166527}[]{#_Toc366220063}[]{#_Toc366152785}[]{#_Toc366166528}[]{#_Toc366220064}[]{#_Toc366152786}[]{#_Toc366166529}[]{#_Toc366220065}[]{#_Toc366152787}[]{#_Toc366166530}[]{#_Toc366220066}[]{#_Toc366152788}[]{#_Toc366166531}[]{#_Toc366220067}[]{#_Toc366152789}[]{#_Toc366166532}[]{#_Toc366220068}[]{#_Toc366152790}[]{#_Toc366166533}[]{#_Toc366220069}[]{#_Toc366152840}[]{#_Toc366166583}[]{#_Toc366220119}[]{#_Toc366152841}[]{#_Toc366166584}[]{#_Toc366220120}[]{#_Toc366152842}[]{#_Toc366166585}[]{#_Toc366220121}

**BGP \-- BGP配置命令 \-- display bgp routing-table ipv4 multicast**

------------------------------------------------------------------------

[**[display bgp routing-table ipv4 multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1098420372}[命令用来显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1098616980}

[**[display bgp routing-table ipv4 multicast ]{lang="EN-US"}**[\[ *network-address* \[ { *mask* \| *mask-length* } \[ **longest-match** \] \] \| *network-address* \[ *mask* \| *mask-length* \] **advertise-info** \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } \[ **whole-match** \] \| *adv-community-list-number* } \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } \[ *network-address* \[ *mask* \| *mask-length* \] \| **statistics** \] \| **statistics** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1098748052}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1098289301}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1098485909}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1098420373}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1098616981}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1098551445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1098748053}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1098682517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1097830549}

[*[network-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1097765013}[：目的网络的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_x1098354830}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1401089478}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[longest-match]{lang="EN-US"}**]{#struct_0_65458_x3406_x1098289294}[：指定根据如下方法判断显示哪条]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[将用户输入的网络地址和路由的掩码进行与操作；]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1098485902}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[计算结果与路由的网段地址相同，且掩码小于等于用户输入子网掩码的路由中，子网掩码最长的路由将被显示出来。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1098420366}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_65458_x3406_x1098616974}[：显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由的通告信息。]{style="font-family:宋体"}

[**[as-path-acl]{lang="EN-US"}***[ as-path-acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1098551438}[：显示匹配指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}*[as-path-acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[community-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1098748046}[：显示匹配指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体列表的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[*[basic-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1098682510}[：基本团体列表号，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[comm-list-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1097830542}[：团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[whole-match]{lang="EN-US"}**]{#struct_0_65458_x3406_x1097765006}[：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。]{style="font-family:宋体"}

[*[adv-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1098354831}[：高级团体列表号，取值范围为]{style="font-family:
宋体"}[100]{lang="EN-US"}[～]{style="font-family:
宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1098289295}[：显示向指定对等体发布或者从指定对等体收到的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[对等体的地址。]{style="font-family:宋体"}

[**[advertised-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_x1098485903}[：显示向指定的对等体发布的路由信息。]{style="font-family:宋体"}

[**[received-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_x1098420367}[：显示从指定的对等体接收到的路由信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_65458_x3406_x1098616975}[：显示路由的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1097765007}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_65458_x3406_823959467}[BGP IPv4]{lang="EN-US"}[组播路由的简要信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定了]{style="font-family:宋体"}]{#struct_0_65458_x3406_824025003}*[network-address]{lang="EN-US"}*[参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则显示该路由的详细信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[network-address mask]{lang="EN-US"}*]{#struct_0_65458_x3406_823828395}[或]{lang="EN-US" style="font-family:宋体"}*[network-address mask-l]{lang="EN-US"}[ength]{lang="EN-US"}*[参数，]{lang="EN-US" style="font-family:宋体"}[没有指定]{style="font-family:宋体"}**[longest-match]{lang="EN-US"}**[参数，]{style="font-family:宋体"}[则显示与指定目的网络]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址和网络掩码（或掩码长度）精确匹配的]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[ IPv4]{lang="EN-US"}[组]{style="font-family:
宋体"}[播]{lang="EN-US" style="font-family:宋体"}[路由的详细信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_823697323}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_823762859}[显示公网所有]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_823566251}

[ ]{lang="EN-US"}

[ Total number of routes: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.62]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  5.5.5.5/32         127.0.0.1       0                     32768   ?]{lang="EN-US"}

[\* \>  192.168.1.0        192.168.1.62    0                     32768   ?]{lang="EN-US"}

[\* \>  192.168.1.62/32    127.0.0.1       0                     32768   ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1194991702}[显示匹配编号为]{style="font-family:宋体"}[20]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast as-path-acl 20]{lang="EN-US"}]{#struct_0_65458_x3406_824549291}

[ ]{lang="EN-US"}

[ Total number of routes: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.62]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  5.5.5.5/32         127.0.0.1       0                     32768   ?]{lang="EN-US"}

[\* \>  192.168.1.0        192.168.1.62    0                     32768   ?]{lang="EN-US"}

[\* \>  192.168.1.62/32    127.0.0.1       0                     32768   ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_823959466}[显示匹配]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体列表]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast community-list 100]{lang="EN-US"}]{#struct_0_65458_x3406_824025002}

[ ]{lang="EN-US"}

[ Total number of routes: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.62]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  5.5.5.5/32         127.0.0.1       0                     32768   ?]{lang="EN-US"}

[\* \>  192.168.1.0        192.168.1.62    0                     32768   ?]{lang="EN-US"}

[\* \>  192.168.1.62/32    127.0.0.1       0                     32768   ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_823828394}[显示向对等体]{style="font-family:宋体"}[192.168.1.139]{lang="EN-US"}[发布的所有]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast peer 192.168.1.139 advertised-routes]{lang="EN-US"}]{#struct_0_65458_x3406_823893930}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.62]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            NextHop         MED        LocPrf             Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  5.5.5.5/32         127.0.0.1       0          100                ?]{lang="EN-US"}

[\* \>  192.168.1.0        192.168.1.62    0          100                ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_823697322}[显示从对等体]{style="font-family:宋体"}[192.168.1.139]{lang="EN-US"}[收到的所有]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast peer 192.168.1.139 received-routes]{lang="EN-US"}]{#struct_0_65458_x3406_823762858}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.62]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>i 8.8.8.8/32         192.168.1.139   0          100        0       ?]{lang="EN-US"}

[\*  i 192.168.1.0        192.168.1.139   0          100        0       ?]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display bgp routing-table ipv4 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_824549290}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x191445531}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_824025001}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_823828393}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_823697321}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_823566249}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_824483753}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_823959464}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_824025000}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_65458_x3406_823893928}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\* -- valid]{lang="DA"}]{#struct_0_65458_x3406_823762856}[[：合法路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> -- best]{lang="EN-US"}]{#struct_0_65458_x3406_823631784}[[：普通优选最佳路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d -- damped]{lang="EN-US"}]{#struct_0_65458_x3406_824549288}[[：震荡抑制路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h -- history]{lang="EN-US"}]{#struct_0_65458_x3406_823959471}[[：历史路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s -- suppressed]{lang="EN-US"}]{#struct_0_65458_x3406_823828399}[[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S -- Stale]{lang="EN-US"}]{#struct_0_65458_x3406_823697327}[[：过期路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- internal]{lang="EN-US"}]{#struct_0_65458_x3406_823566255}[[：内部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- external]{lang="EN-US"}]{#struct_0_65458_x3406_824483759}[[：外部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[Origin]{lang="IT"}]{#struct_0_65458_x3406_823959470}

[[路由信息的来源，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_824025006}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="IT"}]{#struct_0_65458_x3406_823893934}[[：表示路由产生于本]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[AS]{lang="IT"}[[内。通过]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}**[network]{lang="IT"}**[[命令发布路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="IT"}]{#struct_0_65458_x3406_823762862}[[：表示路由是通过]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[EGP]{lang="IT"}[[（]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[Exterior Gateway Protocol]{lang="IT"}[[，外部网关协议）学到的。]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="IT"}]{#struct_0_65458_x3406_823631790}[[：表示路由的来源无法确定。从]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}[[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[incomplete]{lang="IT"}

[[Network]{lang="EN-US"}]{#struct_0_65458_x3406_824549294}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1904858352}

[[NextHop]{lang="EN-US"}]{#struct_0_65458_x3406_x1905054960}

[[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1905186032}[地址]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_65458_x3406_x1905317104}

[[MED]{lang="IT"}]{#struct_0_65458_x3406_x1904399600}[（]{style="font-family:宋体"}[Multi-Exit-Discriminator]{lang="EN-US"}[，多出口区分）属性值]{style="font-family:宋体"}

[[LocPrf]{lang="EN-US"}]{#struct_0_65458_x3406_x1904923889}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1905054961}

[[PrefVal]{lang="EN-US"}]{#struct_0_65458_x3406_x1904989425}

[[路由首选值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1905120497}

[[Path/Ogn]{lang="EN-US"}]{#struct_0_65458_x3406_x1905251569}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1904334065}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和路由信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x1904858354}[[属性记录了此路由经过的所有]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[AS]{lang="EN-US"}[[，可以避免路由环路的出现]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_x1904989426}[[属性标记了此]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[BGP]{lang="EN-US"}[[路由如何生成的]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1905186034}[显示公网内到达目的网络]{style="font-family:宋体"}[5.5.5.5/32]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast 5.5.5.5 32]{lang="EN-US"}]{#struct_0_65458_x3406_x1905120498}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.139]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   1 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 5.5.5.5/32:]{lang="EN-US"}

[ From            : 192.168.1.62 (192.168.1.62)]{lang="EN-US"}

[ Rely nexthop    : 192.168.1.62]{lang="EN-US"}

[ Original nexthop: 192.168.1.62]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : incomplete]{lang="EN-US"}

[ Attribute value : MED 0, localpref 100, pref-val 0]{lang="EN-US"}

[ State           : valid, internal, best]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display bgp routing-table ipv4 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_x1905054963}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x170624011}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1905186035}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1905317107}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1904399603}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1904923884}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_x1905054956}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1905186028}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_x1905120492}

[[路由数信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1905251564}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_65458_x3406_x1904334060}[[：有效路由数目]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_x1904858349}[[：最佳路由数目]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[BGP routing table information of 5.5.5.5/32]{lang="EN-US"}]{#struct_0_65458_x3406_x1904989421}

[[到达目的网络]{style="font-family:宋体"}[5.5.5.5/32]{lang="EN-US"}]{#struct_0_65458_x3406_x1905120493}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表项信息]{style="font-family:宋体"}

[[From]{lang="EN-US"}]{#struct_0_65458_x3406_x1905251565}

[[发布该路由的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1904334061}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Imported route]{lang="EN-US"}]{#struct_0_65458_x3406_x338774411}

[[该路由为引入的路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_x338905483}

[[Rely Nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_x339036555}

[[路由迭代后的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x339167627}[地址，如果没有迭代出下一跳地址，则显示为"]{style="font-family:宋体"}[not resolved]{lang="EN-US"}["]{style="font-family:宋体"}

[[Original nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_x338250123}

[[路由的原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x338839948}[更新消息中获得的路由，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[OutLabel]{lang="IT"}]{#struct_0_65458_x3406_x338971020}

[[路由的出标签值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x339102092}

[[AS-path]{lang="EN-US"}]{#struct_0_65458_x3406_x339233164}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x338315660}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性，记录了此路由经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_65458_x3406_x338839949}

[[路由信息的来源，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x338971021}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="IT"}]{#struct_0_65458_x3406_x339102093}[[：表示路由产生于本]{style="font-family:
  宋体"}]{.TableTextChar}[AS]{lang="IT"}[[内。通过]{style="font-family:宋体"}]{.TableTextChar}**[network]{lang="IT"}**[[命令发布路由的路由信息来源为]{style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="IT"}]{#struct_0_65458_x3406_x339233165}[[：表示路由是通过]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[EGP]{lang="IT"}[[（]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[Exterior Gateway Protocol]{lang="IT"}[[，外部网关协议）学到的。]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[incomplete]{lang="IT"}]{#struct_0_65458_x3406_x338315661}[[：表示路由的来源无法确定。从]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}[[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[incomplete]{lang="IT"}

[[Attribute value]{lang="EN-US"}]{#struct_0_65458_x3406_x338839950}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x338971022}[路由属性信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_65458_x3406_x339102094}[[：与目的网络关联的]{style="font-family:
  宋体"}]{.TableTextChar}[MED]{lang="EN-US"}[[值]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_65458_x3406_x339233166}[[：本地优先级]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_65458_x3406_x339167630}[[：路由首选值]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_65458_x3406_x338250126}[[：协议优先级]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[State]{lang="EN-US"}]{#struct_0_65458_x3406_x338774407}

[[路由当前状态，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x338905479}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_65458_x3406_x339036551}[[：有效路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_65458_x3406_x339167623}[[：内部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_65458_x3406_x338250119}[[：外部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_65458_x3406_x338774408}[[：本地产生路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[synchronize]{lang="EN-US"}]{#struct_0_65458_x3406_x338905480}[[：同步路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_x339036552}[[：最佳路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[IP precedence]{lang="EN-US"}]{#struct_0_65458_x3406_x339233160}

[[路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x338315656}[优先级，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[[QoS local ID]{lang="EN-US"}]{#struct_0_65458_x3406_1227243994}

[[路由的]{style="font-family:宋体"}[Qos-Local-ID]{lang="EN-US"}]{#struct_0_65458_x3406_1227112922}[属性，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1227178458}[显示向对等体]{style="font-family:宋体"}[192.168.1.62]{lang="EN-US"}[发布的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast peer 192.168.1.62 advertised-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_1226981850}

[ ]{lang="EN-US"}

[ Advertised routes total: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1227047386}[显示从对等体]{style="font-family:宋体"}[192.168.1.62]{lang="EN-US"}[收到的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast peer 192.168.1.62 received-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_1226850778}

[ ]{lang="EN-US"}

[ Received routes total: 2]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display bgp routing-table ipv4 multicast peer statistics]{lang="EN-US"}]{#struct_0_65458_x3406_1226916314}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x183666828}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227833818}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227309529}

[[Advertised routes total]{lang="EN-US"}]{#struct_0_65458_x3406_1227178457}

[[向指定对等体发布的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_1227047385}

[[Received routes total]{lang="EN-US"}]{#struct_0_65458_x3406_1226916313}

[[从指定对等体收到的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_1227833817}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1227243992}[显示]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[组播的路由统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast statistics]{lang="EN-US"}]{#struct_0_65458_x3406_1227309528}

[ ]{lang="EN-US"}

[ Total number of routes: 5]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display bgp routing-table ipv4 multicast statistics]{lang="EN-US"}]{#struct_0_65458_x3406_1226981848}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x156981817}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_1226850776}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227768280}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_1227243991}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_1227112919}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1227178455}[显示公网内到达目的网段]{style="font-family:宋体"}[8.8.8.8/32]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 multicast 8.8.8.8 32 advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_1226981847}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.139]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 8.8.8.8/32:]{lang="EN-US"}

[ Advertised to peers (1 in total):]{lang="EN-US"}

[    192.168.1.62]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display bgp routing-table ipv4 multicast advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_1226916311}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x136874515}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227833815}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227309534}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_1227178462}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_1227047390}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_1226916318}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1227833822}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_1227243997}

[[到达指定目的网络的优选路由数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_1227112925}

[[BGP routing table information of 8.8.8.8/32]{lang="EN-US"}]{#struct_0_65458_x3406_1226981853}

[[到达目的网络]{style="font-family:宋体"}[8.8.8.8/32]{lang="EN-US"}]{#struct_0_65458_x3406_1226850781}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的通告信息]{style="font-family:宋体"}

[[Advertised to peers (1 in total)]{lang="EN-US"}]{#struct_0_65458_x3406_1227768285}

[[该路由已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1145409001}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1145343465}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip as-path]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145540073}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145474537}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

::: {#-7131435 .myid}
[]{#_Toc404788621}[]{#struct_0_65458_x3406_2040827164}[]{#_Toc324780824}[]{#_Toc324841503}

**BGP \-- BGP配置命令 \-- display bgp routing-table ipv4 unicast**

------------------------------------------------------------------------

[**[display bgp routing-table ipv4 unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1654490890}[命令用来显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1245371243}

[**[display bgp routing-table ipv4 ]{lang="EN-US"}**[\[ **unicast** \]]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **vpn-instance** ]{lang="EN-US"}*[vpn-instance-name ]{lang="EN-US"}*[\]]{lang="EN-US"}[ ]{lang="EN-US"}[\[ *network-address* \[ { *mask* \| *mask-length* } \[ **longest-match** \] \] \| *network-address* \[ *mask* \| *mask-length* \] **advertise-info** \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } \[ **whole-match** \] \| *adv-community-list-number* } \| **peer** *ip-address* { **advertised-routes** \| **received-routes** } \[ *network-address* \[ *mask* \| *mask-length* \] \| **statistics** \] \| **statistics** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1145605609}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1351298661}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_577620525}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_52789778}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1099994170}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_815336844}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x2145655849}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1654556426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1879206093}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1785655522}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[*[network-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1862843956}[：目的网络的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_x230117224}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_352617533}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[longest-match]{lang="EN-US"}**]{#struct_0_65458_x3406_x1682715286}[：指定根据如下方法判断显示哪条]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[将用户输入的网络地址和路由的掩码进行与操作；]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1621684330}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[计算结果与路由的网段地址相同，且掩码小于等于用户输入子网掩码的路由中，子网掩码最长的路由将被显示出来。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1655015175}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145605610}[：显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的通告信息。]{style="font-family:宋体"}

[**[as-path-acl]{lang="EN-US"}***[ as-path-acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1145802218}[：显示匹配指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}*[as-path-acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[community-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145736682}[：显示匹配指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体列表的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[*[basic-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1144884714}[：基本团体列表号，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[comm-list-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1144819178}[：团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[whole-match]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145409003}[：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。]{style="font-family:宋体"}

[*[adv-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1145343467}[：高级团体列表号，取值范围为]{style="font-family:
宋体"}[100]{lang="EN-US"}[～]{style="font-family:
宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1145540075}[：显示向指定对等体发布或者从指定对等体收到的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[对等体的地址。]{style="font-family:宋体"}

[**[advertised-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145474539}[：显示向指定的对等体发布的路由信息。]{style="font-family:宋体"}

[**[received-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145671147}[：显示从指定的对等体接收到的路由信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_65458_x3406_x1145605611}[：显示路由的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2015175152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_65458_x3406_x249575844}[BGP IPv4]{lang="EN-US"}[单播路由的简要信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定了]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1435847838}*[network-address]{lang="EN-US"}*[参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则显示该路由的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[network-address mask]{lang="EN-US"}*]{#struct_0_65458_x3406_x715702060}[或]{lang="EN-US" style="font-family:宋体"}*[network-address mask-l]{lang="EN-US"}[ength]{lang="EN-US"}*[参数，]{lang="EN-US" style="font-family:宋体"}[没有指定]{style="font-family:宋体"}**[longest-match]{lang="EN-US"}**[参数，]{style="font-family:宋体"}[则显示与指定目的网络]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址和网络掩码（或掩码长度）精确匹配的]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[ IPv4]{lang="EN-US"}[单播]{lang="EN-US" style="font-family:宋体"}[路由的信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时指定]{style="font-family:宋体"}]{#struct_0_65458_x3406_277277067}**[unicast]{lang="EN-US"}**[参数和不指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[参数的效果相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x859297683}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_593936802}[显示公网所有]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_1655211783}

[ ]{lang="EN-US"}

[ Total number of routes: 4]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.100.1]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               ]{lang="EN-US"}[Origin: i - IGP, e - EGP, ? - incomplete]{lang="IT"}

[ ]{lang="IT"}

[     ]{lang="IT"}[Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  10.2.1.0/24        10.2.1.1        0                     0       i]{lang="EN-US"}

[   e                    10.2.1.2        0                     0       200i]{lang="EN-US"}

[\* \>  192.168.1.0        192.168.1.135   0                     0       i]{lang="EN-US"}

[\*  e                    10.2.1.2        0                     0       200i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1145474533}[显示匹配]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 as-path-acl 1]{lang="EN-US"}]{#struct_0_65458_x3406_x1145671141}

[ ]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 2.2.2.2]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>e 30.1.1.0/24        20.1.1.1                              0       200i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1145802213}[显示向对等体]{style="font-family:宋体"}[10.2.1.2]{lang="EN-US"}[发布的所有公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 peer 10.2.1.2 advertised-routes]{lang="EN-US"}]{#struct_0_65458_x3406_x1145736677}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.100.1]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - damped, h - history,]{lang="EN-US"}

[               s - suppressed, S - Stale, i - internal, e - external]{lang="EN-US"}

[               ]{lang="EN-US"}[Origin: i - IGP, e - EGP, ? - incomplete]{lang="IT"}

[ ]{lang="IT"}

[     ]{lang="IT"}[Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  10.2.1.0/24        10.2.1.1        0                     0       i]{lang="EN-US"}

[\* \>  192.168.1.0        192.168.1.135   0                     0       i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1144884709}[显示从对等体]{style="font-family:宋体"}[10.2.1.2]{lang="EN-US"}[收到的所有公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 peer 10.2.1.2 received-routes]{lang="EN-US"}]{#struct_0_65458_x3406_x1144819173}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.100.1]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - damped, h - history,]{lang="EN-US"}

[               s - suppressed, S - Stale, i - internal, e - external]{lang="EN-US"}

[               ]{lang="EN-US"}[Origin: i - IGP, e - EGP, ? - incomplete]{lang="IT"}

[ ]{lang="IT"}

[     ]{lang="IT"}[Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[   e 10.2.1.0/24        10.2.1.2        0                     0       200i]{lang="EN-US"}

[\*  e 192.168.1.0        10.2.1.2        0                     0       200i]{lang="EN-US"}

[]{#struct_0_65458_x3406_1457565871}[[表1-19 ]{lang="EN-US"}[display bgp routing-table ipv4 unicast]{lang="EN-US"}]{#_Ref290364078}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x505839765}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2025136798}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x749575660}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_441037667}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_492165426}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_1655277319}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_1512043798}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_x1396201652}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x621174946}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[\* -- valid]{lang="DA"}]{#struct_0_65458_x3406_1935158884}[：]{lang="EN-US" style="font-family:宋体"}[合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> -- best]{lang="EN-US"}]{#struct_0_65458_x3406_903526860}[：普通优选最佳路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d - dampened]{lang="EN-US"}]{#struct_0_65458_x3406_1655408391}[：震荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h -- history]{lang="EN-US"}]{#struct_0_65458_x3406_x514930323}[：历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s -- suppressed]{lang="EN-US"}]{#struct_0_65458_x3406_1655473927}[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S -- ]{lang="EN-US"}]{#struct_0_65458_x3406_1654490887}[s]{lang="EN-US"}[tale]{lang="EN-US"}[：过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- internal]{lang="EN-US"}]{#struct_0_65458_x3406_1654556423}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- external]{lang="EN-US"}]{#struct_0_65458_x3406_1879009485}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="IT"}]{#struct_0_65458_x3406_x1257170036}

[[路由信息的来源]{style="font-family:宋体"}]{#struct_0_65458_x3406_1713472810}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="IT"}]{#struct_0_65458_x3406_1655015176}[：表示]{lang="EN-US" style="font-family:宋体"}[路由产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="IT"}[内]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:
  宋体"}**[network]{lang="IT"}**[命令发布路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="IT"}]{#struct_0_65458_x3406_x2015371760}[：表示]{lang="EN-US" style="font-family:宋体"}[路由是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="IT"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="IT"}[，]{lang="EN-US" style="font-family:
  宋体"}[外部网关协议]{lang="EN-US" style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}[学到的]{lang="EN-US" style="font-family:
  宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="IT"}]{#struct_0_65458_x3406_x1944068824}[：表示]{lang="EN-US" style="font-family:宋体"}[路由的来源无法确定]{lang="EN-US" style="font-family:宋体"}[。从]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="IT"}

[[Network]{lang="EN-US"}]{#struct_0_65458_x3406_252802272}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1860956014}

[[NextHop]{lang="EN-US"}]{#struct_0_65458_x3406_1655080712}

[[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x129882863}[地址]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_65458_x3406_x472323312}

[[MED]{lang="IT"}]{#struct_0_65458_x3406_1044543162}[（]{style="font-family:宋体"}[Multi-Exit Discriminator]{lang="EN-US"}[，多出口区分）属性值]{style="font-family:宋体"}

[[LocPrf]{lang="EN-US"}]{#struct_0_65458_x3406_1655146248}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2012714669}

[[PrefVal]{lang="EN-US"}]{#struct_0_65458_x3406_1816913433}

[[路由首选值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1063147988}

[[Path/Ogn]{lang="EN-US"}]{#struct_0_65458_x3406_1655211784}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1457369263}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和路由信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x1254861457}[属性记录了此路由经过的所有]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_1856883435}[属性标记了此]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由如何生成的]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1655277320}[显示公网内到达目的网络]{style="font-family:宋体"}[10.2.1.0/24]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 10.2.1.0 24]{lang="EN-US"}]{#struct_0_65458_x3406_1512502547}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.100.1]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   2 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 10.2.1.0/24:]{lang="EN-US"}

[ Imported route.]{lang="EN-US"}

[ Original nexthop: 10.2.1.1]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : MED 0, pref-val 0, pre 0]{lang="EN-US"}

[ State           : valid, local, best]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ From            : 10.2.1.2 (192.168.100.2)]{lang="EN-US"}

[ Rely nexthop    : not resolved]{lang="EN-US"}

[ Original nexthop: 10.2.1.2]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : 200]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : MED 0, pref-val 0, pre 255]{lang="EN-US"}

[ State           : external]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1144819174}[显示公网内到达目的网络]{style="font-family:宋体"}[1.1.1.1/32]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 1.1.1.1 32]{lang="EN-US"}]{#struct_0_65458_x3406_420347260}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.100.1]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   2 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 1.1.1.1/32:]{lang="EN-US"}

[ From            : 10.2.1.1 (192.168.100.3)]{lang="EN-US"}

[ Rely nexthop    : 10.2.1.1]{lang="EN-US"}

[ Original nexthop: 10.2.1.1]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : MED 0, pref-val 0, pre 0]{lang="EN-US"}

[ State           : valid, local, best]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Backup route.]{lang="EN-US"}

[ From            : 10.2.1.2 (192.168.100.2)]{lang="EN-US"}

[ Rely nexthop    : 10.2.1.2]{lang="EN-US"}

[ Original nexthop: 10.2.1.2]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : 200]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : MED 0, pref-val 0, pre 255]{lang="EN-US"}

[ State           : external]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display bgp routing-table ipv4 unicast]{lang="EN-US"}]{#struct_0_65458_x3406_941890375}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x509854485}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_1655342856}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1597883392}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x816720510}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_861328065}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_1743986418}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_891717387}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_1655408392}

[[路由数信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_x514733715}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_65458_x3406_x374246163}[：有效路由数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_1635499385}[：最佳路由数目]{lang="EN-US" style="font-family:宋体"}

[[BGP routing table information of 10.2.1.0/24]{lang="EN-US"}]{#struct_0_65458_x3406_1316111579}

[[到达目的网络]{style="font-family:宋体"}[10.2.1.0/24]{lang="EN-US"}]{#struct_0_65458_x3406_1655473928}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表项信息]{style="font-family:宋体"}

[[Imported route]{lang="EN-US"}]{#struct_0_65458_x3406_1925891773}

[[该路由为引入的路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1960859784}

[[Original nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_86952391}

[[路由的原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1206702008}[更新消息中获得的路由，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[OutLabel]{lang="IT"}]{#struct_0_65458_x3406_1654490888}

[[路由的出标签值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1245895532}

[[AS-path]{lang="EN-US"}]{#struct_0_65458_x3406_16282008}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1687561253}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性，记录了此路由经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_65458_x3406_1654556424}

[[路由信息的来源]{style="font-family:宋体"}]{#struct_0_65458_x3406_1879337165}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="IT"}]{#struct_0_65458_x3406_1015643183}[：表示]{style="font-family:宋体"}[路由产生于本]{style="font-family:宋体"}[AS]{lang="IT"}[内]{style="font-family:宋体"}[。]{style="font-family:宋体"}[通过]{style="font-family:宋体"}**[network]{lang="IT"}**[命令发布路由的路由信息来源为]{style="font-family:宋体"}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="IT"}]{#struct_0_65458_x3406_133867290}[：表示]{lang="EN-US" style="font-family:
  宋体"}[路由是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="IT"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="IT"}[，]{lang="EN-US" style="font-family:
  宋体"}[外部网关协议]{lang="EN-US" style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}[学到的]{lang="EN-US" style="font-family:
  宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[incomplete]{lang="IT"}]{#struct_0_65458_x3406_x2035024369}[：表示]{lang="EN-US" style="font-family:宋体"}[路由的来源无法确定]{lang="EN-US" style="font-family:宋体"}[。从]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="IT"}

[[Attribute value]{lang="EN-US"}]{#struct_0_65458_x3406_1655015173}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x2015044080}[路由属性信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_65458_x3406_x241123744}[：与目的网络关联的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_65458_x3406_x1619157972}[：本地优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_65458_x3406_1655080709}[：路由首选值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_65458_x3406_x130603760}[：协议优先级]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_65458_x3406_x108046478}

[[路由当前状态，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1036179889}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_65458_x3406_1655146245}[：有效路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_65458_x3406_x2011993773}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_65458_x3406_x1514039293}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_65458_x3406_x1064864358}[：本地产生路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[synchronize]{lang="EN-US"}]{#struct_0_65458_x3406_1655211781}[：同步路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_1457696943}[：最佳路由]{lang="EN-US" style="font-family:宋体"}

[[From]{lang="EN-US"}]{#struct_0_65458_x3406_1473866025}

[[发布该路由的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1655277317}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Rely Nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_1512437014}

[[路由迭代后的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1037338308}[地址，如果没有迭代出下一跳地址，则显示为"]{style="font-family:宋体"}[not resolved]{lang="EN-US"}["]{style="font-family:宋体"}

[[IP precedence]{lang="EN-US"}]{#struct_0_65458_x3406_x1130855256}

[[路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1131051864}[优先级，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[[QoS local ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1131182936}

[[路由的]{style="font-family:宋体"}[Qos-Local-ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1130330968}[属性，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[[Backup route]{lang="EN-US"}]{#struct_0_65458_x3406_420674938}

[[该路由为备份的路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_420543866}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_420609402}[显示向对等体]{style="font-family:宋体"}[10.2.1.2]{lang="EN-US"}[发布的公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 peer 10.2.1.2 advertised-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_420478330}

[ ]{lang="EN-US"}

[ Advertised routes total: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_420281722}[显示从对等体]{style="font-family:宋体"}[10.2.1.2]{lang="EN-US"}[收到的公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 peer 10.2.1.2 received-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_420347258}

[ ]{lang="EN-US"}

[ Received routes total: 2]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[display bgp routing-table ipv4 unicast peer statistics]{lang="EN-US"}]{#struct_0_65458_x3406_420609401}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x148134245}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_420478329}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_420347257}

[[Advertised routes total]{lang="EN-US"}]{#struct_0_65458_x3406_420674944}

[[向指定对等体发布的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_420543872}

[[Received routes total]{lang="EN-US"}]{#struct_0_65458_x3406_420412800}

[[从指定对等体收到的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_420281728}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_421199232}[显示公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 statistics]{lang="EN-US"}]{#struct_0_65458_x3406_421264768}

[ ]{lang="EN-US"}

[ Total number of routes: 4]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[display bgp routing-table ipv4 unicast statistics]{lang="EN-US"}]{#struct_0_65458_x3406_420543871}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_140654043}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_420478335}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_420347263}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_421264767}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1508061889}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1507930817}[显示公网内到达目的网段]{style="font-family:宋体"}[10.2.1.0/24]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 10.2.1.0 24 advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_x1508258497}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.100.1]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 10.2.1.0/24:]{lang="EN-US"}

[ Advertised to peers (1 in total):]{lang="EN-US"}

[    10.2.1.2]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[display bgp routing-table ipv4 unicast advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_x1507472065}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_162858092}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1507996354}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1507865282}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1508258498}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1508192962}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_x1507537602}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1508061891}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_x1507930819}

[[到达指定目的网络的优选路由数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1508127427}

[[BGP routing table information of 10.2.1.0/24]{lang="EN-US"}]{#struct_0_65458_x3406_x1507472067}

[[到达目的网络]{style="font-family:宋体"}[10.2.1.0/24]{lang="EN-US"}]{#struct_0_65458_x3406_x1507996356}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的通告信息]{style="font-family:宋体"}

[[Advertised to peers (1 in total)]{lang="EN-US"}]{#struct_0_65458_x3406_x1507865284}

[[该路由已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1508324036}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1508127428}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip as-path]{lang="EN-US"}**]{#struct_0_65458_x3406_x1508192964}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1507472068}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

::: {#-479331979 .myid}
[]{#_Toc404788622}[]{#struct_0_65458_x3406_x1507537604}[]{#_Toc366077076}

**BGP \-- BGP配置命令 \-- display bgp routing-table ipv6 multicast**

------------------------------------------------------------------------

[**[display bgp routing-table ipv6 multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1508061885}[命令用来显示]{style="font-family:宋体"}[BGP IPv6 ]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1507865277}

[**[display bgp routing-table ipv6]{lang="EN-US"}***[ ]{lang="EN-US"}***[multicast ]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *network-address prefix-length* \[ **advertise-info** \] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } \[ **whole-match** \] \| *adv-community-list-number* } \| **peer** *ipv6-address* { **advertised-routes** \| **received-routes** } \[ *network-address prefix-length* \| **statistics** \] \| **statistics** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1508258493}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1507996350}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1508061886}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1507865278}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1507930814}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1508324030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1508127422}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1508192958}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1507472062}

[*[network-address prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1507537598}[：显示与指定的目的网络地址和前缀长度精确匹配的]{style="font-family:
宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[目的网络地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果没有指定本参数，则显示所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的简要信息。]{style="font-family:宋体"}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_65458_x3406_58087588}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的通告信息。如果没有指定本参数，则显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由表的信息。]{style="font-family:宋体"}

[**[as-path-acl ]{lang="EN-US"}***[as-path-acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_58022052}[：显示匹配指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}*[as-path-acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[communit-list]{lang="EN-US"}**]{#struct_0_65458_x3406_58153124}[：显示匹配指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体列表的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[*[basic-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_57825444}[：基本团体列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[comm-list-name]{lang="EN-US"}*]{#struct_0_65458_x3406_57759908}[：团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[whole-match]{lang="EN-US"}**]{#struct_0_65458_x3406_57956516}[：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。]{style="font-family:宋体"}

[*[adv-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_57890980}[：高级团体列表号，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_65458_x3406_58611876}[：显示向指定的对等体发布或者从指定的对等体收到的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_58546340}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[advertised-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_58022051}[：显示向指定的对等体发布的路由信息。]{style="font-family:宋体"}

[**[received-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_58218659}[：显示从指定的对等体接收到的路由信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_65458_x3406_58153123}[：显示路由的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_58218658}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_58153122}[显示所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_57759906}

[ ]{lang="EN-US"}

[ Total number of routes: 5]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.139]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::                                       LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*  i Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::2                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::1                                      LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 2::2                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::1                                      LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>i Network : 5::5                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_57956514}[显示匹配]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast as-path-acl 1]{lang="EN-US"}]{#struct_0_65458_x3406_58546338}

[ ]{lang="EN-US"}

[ Total number of routes: 5]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.139]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::                                       LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*  i Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::2                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::1                                      LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 2::2                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::1                                      LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>i Network : 5::5                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_58087585}[显示匹配]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体列表]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast community-list 100]{lang="EN-US"}]{#struct_0_65458_x3406_58218657}

[ ]{lang="EN-US"}

[ Total number of routes: 5]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.139]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::                                       LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*  i Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::2                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::1                                      LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 2::2                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::1                                      LocPrf    :]{lang="EN-US"}

[     PrefVal : 32768                                    OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>i Network : 5::5                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_58153121}[显示向对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[发布的所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast peer 1::1 advertised-routes]{lang="EN-US"}]{#struct_0_65458_x3406_57825441}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.139]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::                                       LocPrf    : 100]{lang="EN-US"}

[     MED     : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 2::2                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::1                                      LocPrf    : 100]{lang="EN-US"}

[     MED     : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_57956513}[显示从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[收到的所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast peer 1::1 received-routes]{lang="EN-US"}]{#struct_0_65458_x3406_57890977}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.139]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*  i Network : 1::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>i Network : 5::5                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : 1::1                                     LocPrf    : 100]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: ?]{lang="EN-US"}

[[表1-24 ]{lang="EN-US"}[display bgp routing-table ipv6 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_58022056}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_182962420}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_58153128}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_57956520}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_58611880}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_58022055}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_57825447}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_57956519}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_58546343}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1624105993}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\* -- valid]{lang="DA"}]{#struct_0_65458_x3406_1623909385}[[：合法路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> -- best]{lang="EN-US"}]{#struct_0_65458_x3406_1624040457}[[：普通优选最佳路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d -- damped]{lang="EN-US"}]{#struct_0_65458_x3406_1624695817}[[：震荡抑制路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h -- history]{lang="EN-US"}]{#struct_0_65458_x3406_1624105992}[[：历史路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s -- suppressed]{lang="EN-US"}]{#struct_0_65458_x3406_1624237064}[[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S -- Stale]{lang="EN-US"}]{#struct_0_65458_x3406_1623843848}[[：过期路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- internal]{lang="EN-US"}]{#struct_0_65458_x3406_1623974920}[[：内部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- external]{lang="EN-US"}]{#struct_0_65458_x3406_1624171527}[[：外部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[Origin]{lang="IT"}]{#struct_0_65458_x3406_1624302599}

[[路由信息的来源，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1623909383}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="IT"}]{#struct_0_65458_x3406_1623974919}[[：表示路由产生于本]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[AS]{lang="IT"}[[内。通过]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}**[network]{lang="IT"}**[[命令发布路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="IT"}]{#struct_0_65458_x3406_1624630279}[[：表示路由是通过]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[EGP]{lang="IT"}[[（]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[Exterior Gateway Protocol]{lang="IT"}[[，外部网关协议）学到的。]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="IT"}]{#struct_0_65458_x3406_1624105990}[[：表示路由的来源无法确定。从]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}[[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[incomplete]{lang="IT"}

[[Network]{lang="EN-US"}]{#struct_0_65458_x3406_1624237062}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_1624040454}

[[PrefixLen]{lang="EN-US"}]{#struct_0_65458_x3406_1624695814}

[[目的网络地址的前缀长度]{style="font-family:宋体"}]{#struct_0_65458_x3406_1624171533}

[[NextHop]{lang="EN-US"}]{#struct_0_65458_x3406_1624302605}

[[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_1623843853}[地址]{style="font-family:宋体"}

[[LocPrf]{lang="EN-US"}]{#struct_0_65458_x3406_1623974925}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_65458_x3406_1624630285}

[[PrefVal]{lang="EN-US"}]{#struct_0_65458_x3406_1624302604}

[[路由首选值]{style="font-family:宋体"}]{#struct_0_65458_x3406_1623909388}

[[OutLabel]{lang="EN-US"}]{#struct_0_65458_x3406_1624040460}

[[路由的出标签值]{style="font-family:宋体"}]{#struct_0_65458_x3406_1624630284}

[[MED]{lang="EN-US"}]{#struct_0_65458_x3406_x1104777362}

[[ME]{lang="IT"}[D]{lang="EN-US"}]{#struct_0_65458_x3406_x1104646290}[（]{style="font-family:宋体"}[Multi-Exit-Discriminator]{lang="EN-US"}[，多出口区分）属性值]{style="font-family:宋体"}

[[Path/Ogn]{lang="EN-US"}]{#struct_0_65458_x3406_x1104842898}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1104187538}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和路由信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_x1104711827}[[属性记录了此路由经过的所有]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[AS]{lang="EN-US"}[[，可以避免路由环路的出现]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_x1104580755}[[属性标记了此]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[BGP]{lang="EN-US"}[[路由如何生成的]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1104646291}[显示到达目的网络]{style="font-family:宋体"}[2::2/128]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast 2::2 128]{lang="EN-US"}]{#struct_0_65458_x3406_x1104908435}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.139]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   1 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 2::2/128:]{lang="EN-US"}

[ Imported route.]{lang="EN-US"}

[ Original nexthop: ::1]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : incomplete]{lang="EN-US"}

[ Attribute value : MED 0, pref-val 32768]{lang="EN-US"}

[ State           : valid, local, best]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[[表1-25 ]{lang="EN-US"}[display bgp routing-table ipv6 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_x1104646292}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_200998342}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1105039508}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1104187540}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1104711829}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1104580757}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_x1105039509}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1104908437}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_x1104253077}

[[路由数信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1104580750}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_65458_x3406_x1104973966}[[：有效路由数目]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_x1104908430}[[：最佳路由数目]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[BGP routing table information of 2::2/128]{lang="EN-US"}]{#struct_0_65458_x3406_x1104253070}

[[到达目的网络]{style="font-family:宋体"}[2::2/128]{lang="EN-US"}]{#struct_0_65458_x3406_x1104777359}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表项信息]{style="font-family:宋体"}

[[Imported route]{lang="EN-US"}]{#struct_0_65458_x3406_x1104973967}

[[该路由为引入的路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1104842895}

[[Original nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_x1104187535}

[[路由的原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_817536939}[更新消息中获得的路由，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[OutLabel]{lang="IT"}]{#struct_0_65458_x3406_817668011}

[[路由的出标签值]{style="font-family:宋体"}]{#struct_0_65458_x3406_817471403}

[[AS-path]{lang="EN-US"}]{#struct_0_65458_x3406_818126763}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_817536938}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性，记录了此路由经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_65458_x3406_817668010}

[[路由信息的来源，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_817274794}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="IT"}]{#struct_0_65458_x3406_818126762}[[：表示路由产生于本]{style="font-family:
  宋体"}]{.TableTextChar}[AS]{lang="IT"}[[内。通过]{style="font-family:宋体"}]{.TableTextChar}**[network]{lang="IT"}**[[命令发布路由的路由信息来源为]{style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="IT"}]{#struct_0_65458_x3406_817602473}[[：表示路由是通过]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[EGP]{lang="IT"}[[（]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[Exterior Gateway Protocol]{lang="IT"}[[，外部网关协议）学到的。]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[incomplete]{lang="IT"}]{#struct_0_65458_x3406_817733545}[[：表示路由的来源无法确定。从]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[IGP]{lang="IT"}[[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[incomplete]{lang="IT"}

[[Attribute value]{lang="EN-US"}]{#struct_0_65458_x3406_817274793}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_817405865}[路由属性信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_65458_x3406_818061225}[[：与目的网络关联的]{style="font-family:
  宋体"}]{.TableTextChar}[MED]{lang="EN-US"}[[值]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_65458_x3406_817733544}[[：本地优先级]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_65458_x3406_817340328}[[：路由首选值]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_65458_x3406_817471400}[[：协议优先级]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[State]{lang="EN-US"}]{#struct_0_65458_x3406_818061224}

[[路由当前状态，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_817536943}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_65458_x3406_817340335}[[：有效路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_65458_x3406_817471407}[[：内部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_65458_x3406_818061231}[[：外部路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_65458_x3406_817536942}[[：本地产生路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_817668014}[[：最佳路由]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[From]{lang="EN-US"}]{#struct_0_65458_x3406_817471406}

[[发布该路由的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_818126766}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Rely Nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_x1911215344}

[[路由迭代后的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1911608560}[地址，如果没有迭代出下一跳地址，则显示为"]{style="font-family:宋体"}[not resolved]{lang="EN-US"}["]{style="font-family:宋体"}

[[IP precedence]{lang="EN-US"}]{#struct_0_65458_x3406_x1910756592}

[[路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1911280881}[优先级，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[[QoS local ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1911149809}

[[路由的]{style="font-family:宋体"}[Qos-Local-ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1911608561}[属性，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1911411953}[显示内到达目的网段]{style="font-family:宋体"}[2::2/128]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast 2::2 128 advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_x1911477489}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.139]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 2::2/128:]{lang="EN-US"}

[ Advertised to peers (1 in total):]{lang="EN-US"}

[    1::1]{lang="EN-US"}

[[表1-26 ]{lang="EN-US"}[display bgp routing-table ipv6 multicast advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_x1910822129}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_214773464}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1911346418}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1911215346}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1911411954}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1910756594}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_x1911280883}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1911149811}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_x1911608563}

[[到达指定目的网络的优选路由数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1911477491}

[[BGP routing table information of 2::2/128]{lang="EN-US"}]{#struct_0_65458_x3406_x1911280876}

[[到达目的网络]{style="font-family:宋体"}[2::2/128]{lang="EN-US"}]{#struct_0_65458_x3406_x1911149804}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的通告信息]{style="font-family:宋体"}

[[Advertised to peers (1 in total)]{lang="EN-US"}]{#struct_0_65458_x3406_x1911543020}

[[该路由已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1911477484}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1910756588}[显示向对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[发布的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast peer 1::1 advertised-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x1910822124}

[ ]{lang="EN-US"}

[ Advertised routes total: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1911280877}[显示从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[收到的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast peer 1::1 received-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x1911346413}

[ ]{lang="EN-US"}

[ Received routes total: 2]{lang="EN-US"}

[[表1-27 ]{lang="EN-US"}[display bgp routing-table ipv6 multicast peer statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x1911215341}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_205047847}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1911608557}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1911477485}

[[Advertised routes total]{lang="EN-US"}]{#struct_0_65458_x3406_x345196939}

[[向指定对等体发布的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x345065867}

[[Received routes total]{lang="EN-US"}]{#struct_0_65458_x3406_x345459083}

[[从指定对等体收到的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x345393547}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x344672651}[显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播的路由统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 multicast statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x344738187}

[ ]{lang="EN-US"}

[ Total number of routes: 5]{lang="EN-US"}

[[表1-28 ]{lang="EN-US"}[display bgp routing-table ipv6 multicast statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x345131404}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_223307614}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x345524620}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x345393548}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_x345196941}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_x345065869}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x345131405}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip as-path]{lang="EN-US"}**]{#struct_0_65458_x3406_x345524621}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x345328013}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

::: {#-140693803 .myid}
[]{#_Toc404788623}[]{#struct_0_65458_x3406_145418575}[]{#_Toc309715687}[]{#_Toc366152846}[]{#_Toc366166589}[]{#_Toc366152847}[]{#_Toc366166590}[]{#_Toc366152848}[]{#_Toc366166591}[]{#_Toc366152849}[]{#_Toc366166592}[]{#_Toc366152850}[]{#_Toc366166593}[]{#_Toc366152851}[]{#_Toc366166594}[]{#_Toc366152852}[]{#_Toc366166595}[]{#_Toc366152853}[]{#_Toc366166596}[]{#_Toc366152854}[]{#_Toc366166597}[]{#_Toc366152855}[]{#_Toc366166598}[]{#_Toc366152856}[]{#_Toc366166599}[]{#_Toc366152857}[]{#_Toc366166600}[]{#_Toc366152858}[]{#_Toc366166601}[]{#_Toc366152859}[]{#_Toc366166602}[]{#_Toc366152860}[]{#_Toc366166603}[]{#_Toc366152861}[]{#_Toc366166604}[]{#_Toc366152862}[]{#_Toc366166605}[]{#_Toc366152863}[]{#_Toc366166606}[]{#_Toc366152864}[]{#_Toc366166607}[]{#_Toc366152865}[]{#_Toc366166608}[]{#_Toc366152866}[]{#_Toc366166609}[]{#_Toc366152867}[]{#_Toc366166610}[]{#_Toc366152868}[]{#_Toc366166611}[]{#_Toc366152869}[]{#_Toc366166612}[]{#_Toc366152870}[]{#_Toc366166613}[]{#_Toc366152871}[]{#_Toc366166614}[]{#_Toc366152872}[]{#_Toc366166615}[]{#_Toc366152873}[]{#_Toc366166616}[]{#_Toc366152874}[]{#_Toc366166617}[]{#_Toc366152875}[]{#_Toc366166618}[]{#_Toc366152876}[]{#_Toc366166619}[]{#_Toc366152877}[]{#_Toc366166620}[]{#_Toc366152878}[]{#_Toc366166621}[]{#_Toc366152897}[]{#_Toc366166640}[]{#_Toc366152898}[]{#_Toc366166641}[]{#_Toc366152899}[]{#_Toc366166642}[]{#_Toc366152900}[]{#_Toc366166643}[]{#_Toc366152901}[]{#_Toc366166644}[]{#_Toc366152902}[]{#_Toc366166645}[]{#_Toc366152903}[]{#_Toc366166646}[]{#_Toc366152904}[]{#_Toc366166647}[]{#_Toc366152905}[]{#_Toc366166648}[]{#_Toc366152906}[]{#_Toc366166649}[]{#_Toc366152907}[]{#_Toc366166650}[]{#_Toc366152908}[]{#_Toc366166651}[]{#_Toc366152909}[]{#_Toc366166652}[]{#_Toc366152910}[]{#_Toc366166653}[]{#_Toc366152911}[]{#_Toc366166654}[]{#_Toc366152912}[]{#_Toc366166655}[]{#_Toc366152913}[]{#_Toc366166656}[]{#_Toc366152914}[]{#_Toc366166657}[]{#_Toc366152915}[]{#_Toc366166658}[]{#_Toc366152916}[]{#_Toc366166659}[]{#_Toc366152917}[]{#_Toc366166660}[]{#_Toc366152918}[]{#_Toc366166661}[]{#_Toc366152919}[]{#_Toc366166662}[]{#_Toc366152920}[]{#_Toc366166663}[]{#_Toc366152921}[]{#_Toc366166664}[]{#_Toc366152922}[]{#_Toc366166665}[]{#_Toc366152923}[]{#_Toc366166666}[]{#_Toc366152924}[]{#_Toc366166667}[]{#_Toc366152925}[]{#_Toc366166668}[]{#_Toc366152926}[]{#_Toc366166669}[]{#_Toc366152927}[]{#_Toc366166670}[]{#_Toc366152928}[]{#_Toc366166671}[]{#_Toc366152929}[]{#_Toc366166672}[]{#_Toc366152930}[]{#_Toc366166673}[]{#_Toc366152931}[]{#_Toc366166674}[]{#_Toc366152932}[]{#_Toc366166675}[]{#_Toc366152933}[]{#_Toc366166676}[]{#_Toc366152934}[]{#_Toc366166677}[]{#_Toc366152935}[]{#_Toc366166678}[]{#_Toc366152936}[]{#_Toc366166679}[]{#_Toc366152937}[]{#_Toc366166680}[]{#_Toc366152938}[]{#_Toc366166681}[]{#_Toc366152939}[]{#_Toc366166682}[]{#_Toc366152940}[]{#_Toc366166683}[]{#_Toc366152941}[]{#_Toc366166684}[]{#_Toc366152942}[]{#_Toc366166685}[]{#_Toc366152943}[]{#_Toc366166686}[]{#_Toc366152944}[]{#_Toc366166687}[]{#_Toc366152945}[]{#_Toc366166688}[]{#_Toc366152946}[]{#_Toc366166689}[]{#_Toc366152947}[]{#_Toc366166690}[]{#_Toc366152948}[]{#_Toc366166691}[]{#_Toc366152949}[]{#_Toc366166692}[]{#_Toc366152950}[]{#_Toc366166693}[]{#_Toc366152951}[]{#_Toc366166694}[]{#_Toc366152952}[]{#_Toc366166695}[]{#_Toc366152953}[]{#_Toc366166696}[]{#_Toc366152954}[]{#_Toc366166697}[]{#_Toc366152955}[]{#_Toc366166698}[]{#_Toc366152956}[]{#_Toc366166699}[]{#_Toc366152957}[]{#_Toc366166700}[]{#_Toc366152958}[]{#_Toc366166701}[]{#_Toc366152959}[]{#_Toc366166702}[]{#_Toc366152960}[]{#_Toc366166703}[]{#_Toc366152961}[]{#_Toc366166704}[]{#_Toc366152962}[]{#_Toc366166705}[]{#_Toc366152963}[]{#_Toc366166706}[]{#_Toc366152964}[]{#_Toc366166707}[]{#_Toc366152965}[]{#_Toc366166708}[]{#_Toc366152966}[]{#_Toc366166709}[]{#_Toc366152967}[]{#_Toc366166710}[]{#_Toc366152968}[]{#_Toc366166711}[]{#_Toc366152969}[]{#_Toc366166712}[]{#_Toc366152970}[]{#_Toc366166713}[]{#_Toc366152971}[]{#_Toc366166714}[]{#_Toc366152972}[]{#_Toc366166715}[]{#_Toc366152973}[]{#_Toc366166716}[]{#_Toc366152974}[]{#_Toc366166717}[]{#_Toc366152975}[]{#_Toc366166718}[]{#_Toc366152976}[]{#_Toc366166719}[]{#_Toc366152977}[]{#_Toc366166720}[]{#_Toc366152978}[]{#_Toc366166721}[]{#_Toc366152979}[]{#_Toc366166722}[]{#_Toc366152980}[]{#_Toc366166723}[]{#_Toc366152981}[]{#_Toc366166724}[]{#_Toc366152982}[]{#_Toc366166725}[]{#_Toc366152983}[]{#_Toc366166726}[]{#_Toc366152984}[]{#_Toc366166727}[]{#_Toc366152985}[]{#_Toc366166728}[]{#_Toc366152986}[]{#_Toc366166729}[]{#_Toc366152987}[]{#_Toc366166730}[]{#_Toc366152988}[]{#_Toc366166731}[]{#_Toc366152989}[]{#_Toc366166732}[]{#_Toc366152990}[]{#_Toc366166733}[]{#_Toc366152991}[]{#_Toc366166734}[]{#_Toc366152992}[]{#_Toc366166735}[]{#_Toc366152993}[]{#_Toc366166736}[]{#_Toc366152994}[]{#_Toc366166737}[]{#_Toc366152995}[]{#_Toc366166738}[]{#_Toc366152996}[]{#_Toc366166739}[]{#_Toc366152997}[]{#_Toc366166740}[]{#_Toc366152998}[]{#_Toc366166741}[]{#_Toc366152999}[]{#_Toc366166742}[]{#_Toc366153000}[]{#_Toc366166743}[]{#_Toc366153001}[]{#_Toc366166744}[]{#_Toc366153002}[]{#_Toc366166745}[]{#_Toc366153003}[]{#_Toc366166746}[]{#_Toc366153004}[]{#_Toc366166747}[]{#_Toc366153005}[]{#_Toc366166748}[]{#_Toc366153006}[]{#_Toc366166749}[]{#_Toc366153007}[]{#_Toc366166750}[]{#_Toc366153008}[]{#_Toc366166751}[]{#_Toc366153009}[]{#_Toc366166752}[]{#_Toc366153010}[]{#_Toc366166753}[]{#_Toc366153011}[]{#_Toc366166754}[]{#_Toc366153012}[]{#_Toc366166755}[]{#_Toc366153013}[]{#_Toc366166756}[]{#_Toc366153014}[]{#_Toc366166757}[]{#_Toc366153015}[]{#_Toc366166758}[]{#_Toc366153016}[]{#_Toc366166759}[]{#_Toc366153017}[]{#_Toc366166760}[]{#_Toc366153018}[]{#_Toc366166761}[]{#_Toc366153019}[]{#_Toc366166762}[]{#_Toc366153020}[]{#_Toc366166763}[]{#_Toc366153021}[]{#_Toc366166764}[]{#_Toc366153022}[]{#_Toc366166765}[]{#_Toc366153023}[]{#_Toc366166766}[]{#_Toc366153024}[]{#_Toc366166767}[]{#_Toc366153025}[]{#_Toc366166768}[]{#_Toc366153026}[]{#_Toc366166769}[]{#_Toc366153027}[]{#_Toc366166770}[]{#_Toc366153028}[]{#_Toc366166771}[]{#_Toc366153029}[]{#_Toc366166772}[]{#_Toc366153030}[]{#_Toc366166773}[]{#_Toc366153040}[]{#_Toc366166783}[]{#_Toc366153041}[]{#_Toc366166784}[]{#_Toc366153042}[]{#_Toc366166785}[]{#_Toc366153043}[]{#_Toc366166786}[]{#_Toc366153044}[]{#_Toc366166787}[]{#_Toc366153045}[]{#_Toc366166788}[]{#_Toc366153046}[]{#_Toc366166789}[]{#_Toc366153047}[]{#_Toc366166790}[]{#_Toc366153048}[]{#_Toc366166791}[]{#_Toc366153049}[]{#_Toc366166792}[]{#_Toc366153050}[]{#_Toc366166793}[]{#_Toc366153051}[]{#_Toc366166794}[]{#_Toc366153052}[]{#_Toc366166795}[]{#_Toc366153053}[]{#_Toc366166796}[]{#_Toc366153054}[]{#_Toc366166797}[]{#_Toc366153055}[]{#_Toc366166798}[]{#_Toc366153056}[]{#_Toc366166799}[]{#_Toc366153057}[]{#_Toc366166800}[]{#_Toc366153058}[]{#_Toc366166801}[]{#_Toc366153059}[]{#_Toc366166802}[]{#_Toc366153060}[]{#_Toc366166803}[]{#_Toc366153061}[]{#_Toc366166804}[]{#_Toc366153068}[]{#_Toc366166811}[]{#_Toc299201006}[]{#_Toc299632324}[]{#_Toc299201008}[]{#_Toc299632326}[]{#_Toc299201011}[]{#_Toc299632329}[]{#_Toc299201013}[]{#_Toc299632331}[]{#_Toc299201016}[]{#_Toc299632334}[]{#_Toc299201017}[]{#_Toc299632335}

**BGP \-- BGP配置命令 \-- display bgp routing-table ipv6 unicast**

------------------------------------------------------------------------

[**[display bgp routing-table ipv6 unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1909989904}[命令用来显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2082083840}

[**[display bgp routing-table ipv6]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **unicast** \] ]{lang="EN-US"}[\[ ]{lang="EN-US"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name ]{lang="EN-US"}*[\]]{lang="EN-US"}[ ]{lang="EN-US"}[\[ *network-address prefix-length* \[ **advertise-info** \] \| **as-path-acl** *as-path-acl-number* \| **community-list** { { *basic-community-list-number* \| *comm-list-name* } \[ **whole-match** \] \| *adv-community-list-number* } \| **peer** *ipv6-address* { **advertised-routes** \| **received-routes** } \[ *network-address prefix-length* \| **statistics** \] \| **statistics** \]]{lang="EN-US"}]{#struct_0_65458_x3406_1220821463}

[**[display bgp routing-table ipv6 ]{lang="EN-US"}**[\[ **unicast** \] **peer** ]{lang="EN-US"}*[ip-address ]{lang="EN-US"}*[{ **advertised-routes** \| **received-routes** } \[ *network-address prefix-length* \| **statistics** \]]{lang="EN-US"}]{#struct_0_65458_x3406_1221018071}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1546517831}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_1197669420}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_836189942}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x717506745}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x615203913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1814793174}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1946162127}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x959917334}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1211383120}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[*[network-address prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_2024271007}[：显示与指定的目的网络地址和前缀长度精确匹配的]{style="font-family:
宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[目的网络地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果没有指定本参数，则显示所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的简要信息。]{style="font-family:宋体"}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_65458_x3406_377194426}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的通告信息。如果没有指定本参数，则显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由表的信息。]{style="font-family:宋体"}

[**[as-path-acl ]{lang="EN-US"}***[as-path-acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_1220952542}[：显示匹配指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}*[as-path-acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[communit-list]{lang="EN-US"}**]{#struct_0_65458_x3406_1220559326}[：显示匹配指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体列表的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[*[basic-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_1220755934}[：基本团体列表号，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[comm-list-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1220690398}[：团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[whole-match]{lang="EN-US"}**]{#struct_0_65458_x3406_1221345758}[：精确匹配。如果指定了本参数，则只有路由的团体属性列表与指定的团体属性列表完全相同时，才显示该路由的信息；如果未指定本参数，则只要路由的团体属性列表中包含指定的团体属性列表，就显示该路由的信息。]{style="font-family:宋体"}

[*[adv-community-list-number]{lang="EN-US"}*]{#struct_0_65458_x3406_1220887005}[：高级团体列表号，取值范围为]{style="font-family:
宋体"}[100]{lang="EN-US"}[～]{style="font-family:
宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_65458_x3406_1220821469}[：显示向指定的对等体发布或者从指定的对等体收到的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1220952541}[：对等体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1220624861}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[advertised-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_1220755933}[：显示向指定的对等体发布的路由信息。]{style="font-family:宋体"}

[**[received-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_1220690397}[：显示从指定的对等体接收到的路由信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_65458_x3406_1221411293}[：显示路由的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x717441209}

[[执行本命令时指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1411424767}[参数和不指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[参数的效果相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1449360196}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1544076302}[显示公网所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6]{lang="EN-US"}]{#struct_0_65458_x3406_x717375673}

[ ]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.136]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>e Network : 3::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::2                                     LocPrf    :]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     :]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1151241705}[显示匹配]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 as-path-acl 1]{lang="EN-US"}]{#struct_0_65458_x3406_x1151765994}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.136]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>e Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::2                                     LocPrf    :]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     :]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>e Network : 3::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::2                                     LocPrf    :]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     :]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1151634922}[显示匹配]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体列表]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 community-list 100]{lang="EN-US"}]{#struct_0_65458_x3406_x1151700458}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.136]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>e Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::2                                     LocPrf    :]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     :]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>e Network : 3::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : 1::2                                     LocPrf    :]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     :]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1152093674}[显示向对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[发布的所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 peer 1::1 advertised-routes]{lang="EN-US"}]{#struct_0_65458_x3406_x1151962602}

[ ]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.136]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::                                       LocPrf    :]{lang="EN-US"}

[     MED     : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     Path/Ogn: i]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1151241706}[显示从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[收到的所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 peer 1::1 received-routes]{lang="EN-US"}]{#struct_0_65458_x3406_x1151765995}

[ ]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 192.168.1.135]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>e Network : 2::                                      PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::FFFF:10.1.1.1                          LocPrf    :]{lang="EN-US"}

[     PrefVal : 0                                        OutLabel  : NULL]{lang="EN-US"}

[     MED     : 0]{lang="EN-US"}

[     Path/Ogn: 100i]{lang="EN-US"}

[]{#struct_0_65458_x3406_140390437}[[表1-29 ]{lang="EN-US"}[display bgp routing-table ipv6 unicast]{lang="EN-US"}]{#_Ref319653110}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x513489813}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x717310137}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x637087144}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_x323910695}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_247136710}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1167888662}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_1931244172}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_x717244601}

[[路由状态代码：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1417108378}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[\* -- valid]{lang="DA"}]{#struct_0_65458_x3406_x1023273139}[：]{lang="EN-US" style="font-family:宋体"}[合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> -- best]{lang="EN-US"}]{#struct_0_65458_x3406_x27284313}[：普通优选最佳路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d - dampened]{lang="EN-US"}]{#struct_0_65458_x3406_x718162105}[：震荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h -- history]{lang="EN-US"}]{#struct_0_65458_x3406_x1616647965}[：历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s -- suppressed]{lang="EN-US"}]{#struct_0_65458_x3406_x718096569}[：聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S -- ]{lang="EN-US"}]{#struct_0_65458_x3406_x717572284}[s]{lang="EN-US"}[tale]{lang="EN-US"}[：过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- internal]{lang="EN-US"}]{#struct_0_65458_x3406_145221967}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- external]{lang="EN-US"}]{#struct_0_65458_x3406_1715164561}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="IT"}]{#struct_0_65458_x3406_x2122459273}

[[路由信息的来源]{style="font-family:宋体"}]{#struct_0_65458_x3406_1802590678}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="IT"}]{#struct_0_65458_x3406_x717506748}[：表示]{lang="EN-US" style="font-family:宋体"}[路由产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="IT"}[内]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:
  宋体"}**[network]{lang="IT"}**[命令发布路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="IT"}]{#struct_0_65458_x3406_x614483017}[：表示]{lang="EN-US" style="font-family:宋体"}[路由是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="IT"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="IT"}[，]{lang="EN-US" style="font-family:
  宋体"}[外部网关协议]{lang="EN-US" style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}[学到的]{lang="EN-US" style="font-family:
  宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="IT"}]{#struct_0_65458_x3406_1245344972}[：表示]{lang="EN-US" style="font-family:宋体"}[路由的来源无法确定]{lang="EN-US" style="font-family:宋体"}[。从]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="IT"}

[[Network]{lang="EN-US"}]{#struct_0_65458_x3406_x1840418420}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_x717441212}

[[PrefixLen]{lang="EN-US"}]{#struct_0_65458_x3406_x1411883518}

[[目的网络地址的前缀长度]{style="font-family:宋体"}]{#struct_0_65458_x3406_1618434633}

[[NextHop]{lang="EN-US"}]{#struct_0_65458_x3406_x1382164721}

[[下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_1516116448}[地址]{style="font-family:宋体"}

[[LocPrf]{lang="EN-US"}]{#struct_0_65458_x3406_x717375676}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_65458_x3406_140193829}

[[PrefVal]{lang="EN-US"}]{#struct_0_65458_x3406_686344100}

[[路由首选值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1416779170}

[[OutLabel]{lang="EN-US"}]{#struct_0_65458_x3406_x717310140}

[[路由的出标签值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x637152681}

[[MED]{lang="EN-US"}]{#struct_0_65458_x3406_1657785149}

[[MED]{lang="IT"}]{#struct_0_65458_x3406_x717244604}[（]{style="font-family:宋体"}[Multi-Exit Discriminator]{lang="EN-US"}[，多出口区分）属性值]{style="font-family:宋体"}

[[Path/Ogn]{lang="EN-US"}]{#struct_0_65458_x3406_x1416911770}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1087105789}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和路由信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_65458_x3406_869383762}[属性记录了此路由经过的所有]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_65458_x3406_x717179068}[属性标记了此]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由如何生成的]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x682556844}[显示到达目的网络]{style="font-family:宋体"}[2::/64]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 2:: 64]{lang="EN-US"}]{#struct_0_65458_x3406_x718162108}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.135]{lang="EN-US"}

[ Local AS number: 200]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   2 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 2::/64:]{lang="EN-US"}

[ From            : 10.1.1.1 (192.168.1.136)]{lang="EN-US"}

[ Rely nexthop    : ::FFFF:10.1.1.1]{lang="EN-US"}

[ Original nexthop: ::FFFF:10.1.1.1]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : 100]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : MED 0, pref-val 0]{lang="EN-US"}

[ State           : valid, external, best]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Backup route.]{lang="EN-US"}

[ From            : 1::1 (192.168.1.136)]{lang="EN-US"}

[ Rely nexthop    : 1::1]{lang="EN-US"}

[ Original nexthop: 1::1]{lang="EN-US"}

[ OutLabel        : NULL]{lang="EN-US"}

[ AS-path         : 100]{lang="EN-US"}

[ Origin          : igp]{lang="EN-US"}

[ Attribute value : MED 0, pref-val 0]{lang="EN-US"}

[ State           : valid, external]{lang="EN-US"}

[ IP precedence   : N/A]{lang="EN-US"}

[ QoS local ID    : N/A]{lang="EN-US"}

[[表1-30 ]{lang="EN-US"}[display bgp routing-table ipv6 unicast]{lang="EN-US"}]{#struct_0_65458_x3406_x1616975645}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x517018997}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x616571587}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1518951914}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1488613535}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x718096572}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_x25445651}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_191968998}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_68105512}

[[路由数信息]{style="font-family:宋体"}]{#struct_0_65458_x3406_1554808803}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_65458_x3406_x717637819}[：有效路由数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_1660897146}[：最佳路由数目]{lang="EN-US" style="font-family:宋体"}

[[BGP routing table information of 2::/64]{lang="EN-US"}]{#struct_0_65458_x3406_x1872264444}

[[到达目的网络]{style="font-family:宋体"}[2::/64]{lang="EN-US"}]{#struct_0_65458_x3406_x1576476622}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表项信息]{style="font-family:宋体"}

[[Imported route]{lang="EN-US"}]{#struct_0_65458_x3406_x976350830}

[[该路由为引入的路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_x717572283}

[[Original nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_145549647}

[[路由的原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1514051352}[更新消息中获得的路由，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[OutLabel]{lang="IT"}]{#struct_0_65458_x3406_x1093358422}

[[路由的出标签值]{style="font-family:宋体"}]{#struct_0_65458_x3406_x717506747}

[[AS-path]{lang="EN-US"}]{#struct_0_65458_x3406_x615072841}

[[路由的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1031280514}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性，记录了此路由经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免路由环路的出现]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_65458_x3406_812714873}

[[路由信息的来源]{style="font-family:宋体"}]{#struct_0_65458_x3406_1703539297}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="IT"}]{#struct_0_65458_x3406_x717441211}[：表示]{style="font-family:宋体"}[路由产生于本]{style="font-family:宋体"}[AS]{lang="IT"}[内]{style="font-family:宋体"}[。]{style="font-family:宋体"}[通过]{style="font-family:宋体"}**[network]{lang="IT"}**[命令发布路由的路由信息来源为]{style="font-family:宋体"}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="IT"}]{#struct_0_65458_x3406_x1411949054}[：表示]{lang="EN-US" style="font-family:
  宋体"}[路由是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="IT"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="IT"}[，]{lang="EN-US" style="font-family:
  宋体"}[外部网关协议]{lang="EN-US" style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}[学到的]{lang="EN-US" style="font-family:
  宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[incomplete]{lang="IT"}]{#struct_0_65458_x3406_1983432996}[：表示]{lang="EN-US" style="font-family:宋体"}[路由的来源无法确定]{lang="EN-US" style="font-family:宋体"}[。从]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="IT"}

[[Attribute value]{lang="EN-US"}]{#struct_0_65458_x3406_x717375675}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_139997221}[路由属性信息，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_65458_x3406_69234257}[：与目的网络关联的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_65458_x3406_x1722497687}[：本地优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_65458_x3406_x717310139}[：路由首选值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_65458_x3406_x636693928}[：协议优先级]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_65458_x3406_76765037}

[[路由当前状态，取值包括：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2075944676}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_65458_x3406_x717244603}[：有效路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_65458_x3406_x1416977306}[：内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_65458_x3406_1038733793}[：外部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_65458_x3406_1496746318}[：本地产生路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_65458_x3406_x717179067}[：最佳路由]{lang="EN-US" style="font-family:宋体"}

[[From]{lang="EN-US"}]{#struct_0_65458_x3406_x682229164}

[[发布该路由的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x2026236924}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Rely Nexthop]{lang="EN-US"}]{#struct_0_65458_x3406_x718162107}

[[路由迭代后的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_x1616779037}[地址，如果没有迭代出下一跳地址，则显示为"]{style="font-family:宋体"}[not resolved]{lang="EN-US"}["]{style="font-family:宋体"}

[[IP precedence]{lang="EN-US"}]{#struct_0_65458_x3406_435163150}

[[路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_434966542}[优先级，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[[QoS local ID]{lang="EN-US"}]{#struct_0_65458_x3406_434769934}

[[路由的]{style="font-family:宋体"}[Qos-Local-ID]{lang="EN-US"}]{#struct_0_65458_x3406_435228685}[属性，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效值]{style="font-family:宋体"}

[[Backup route]{lang="EN-US"}]{#struct_0_65458_x3406_x1151307237}

[[该路由为备份的路由]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1151634918}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1231293435}[显示公网内到达目的网段]{style="font-family:宋体"}[2::/64]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 2:: 64 advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_x718096571}

[ ]{lang="EN-US"}

[ BGP local router ID: 192.168.1.136]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP routing table information of 2::/64:]{lang="EN-US"}

[ Advertised to peers (2 in total):]{lang="EN-US"}

[    10.1.1.2]{lang="EN-US"}

[    1::2]{lang="EN-US"}

[[表1-31 ]{lang="EN-US"}[display bgp routing-table ipv6 unicast advertise-info]{lang="EN-US"}]{#struct_0_65458_x3406_x25380115}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x486793813}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_327188077}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_2106338070}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_402307995}

[[本地的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x572835763}

[[Local AS number]{lang="EN-US"}]{#struct_0_65458_x3406_x717637822}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_1660569463}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_65458_x3406_x199875863}

[[到达指定目的网络的优选路由数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_2108589176}

[[BGP routing table information of 2::/64]{lang="EN-US"}]{#struct_0_65458_x3406_1757819136}

[[到达目的网络]{style="font-family:宋体"}[2::/64]{lang="EN-US"}]{#struct_0_65458_x3406_x717572286}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的通告信息]{style="font-family:宋体"}

[[Advertised to peers (2 in total)]{lang="EN-US"}]{#struct_0_65458_x3406_145353039}

[[该路由已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1766120329}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1151897062}[显示向对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[发布的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 peer 1::1 advertised-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_x1151241702}

[ ]{lang="EN-US"}

[ Advertised routes total: 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1151307238}[显示从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[收到的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 peer 1::1 received-routes statistics]{lang="EN-US"}]{#struct_0_65458_x3406_414252412}

[ ]{lang="EN-US"}

[ Received routes total: 1]{lang="EN-US"}

[[表1-32 ]{lang="EN-US"}[display bgp routing-table ipv6 unicast peer statistics]{lang="EN-US"}]{#struct_0_65458_x3406_413990268}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_296614}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_414842236}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_414252411}

[[Advertised routes total]{lang="EN-US"}]{#struct_0_65458_x3406_414055803}

[[向指定对等体发布的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_414121339}

[[Received routes total]{lang="EN-US"}]{#struct_0_65458_x3406_414317946}

[[从指定对等体收到的路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_414383482}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_414055802}[显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 statistics]{lang="EN-US"}]{#struct_0_65458_x3406_414186874}

[ ]{lang="EN-US"}

[ Total number of routes: 4]{lang="EN-US"}

[[表1-33 ]{lang="EN-US"}[display bgp routing-table ipv6 unicast statistics]{lang="EN-US"}]{#struct_0_65458_x3406_414317945}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_23526387}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_414055801}

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_414186873}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_414776697}

[[路由总数]{style="font-family:宋体"}]{#struct_0_65458_x3406_414449024}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_414055808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip as-path]{lang="EN-US"}**]{#struct_0_65458_x3406_413990272}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_65458_x3406_414121344}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

::: {#761939889 .myid}
[]{#_Toc404788624}[]{#struct_0_65458_x3406_441522915}[]{#_Toc311730287}[]{#_Toc366153070}[]{#_Toc366166813}[]{#_Toc366220125}[]{#_Toc366153071}[]{#_Toc366166814}[]{#_Toc366220126}[]{#_Toc366153072}[]{#_Toc366166815}[]{#_Toc366220127}[]{#_Toc366153073}[]{#_Toc366166816}[]{#_Toc366220128}[]{#_Toc366153074}[]{#_Toc366166817}[]{#_Toc366220129}[]{#_Toc366153075}[]{#_Toc366166818}[]{#_Toc366220130}[]{#_Toc366153076}[]{#_Toc366166819}[]{#_Toc366220131}[]{#_Toc366153077}[]{#_Toc366166820}[]{#_Toc366220132}[]{#_Toc366153078}[]{#_Toc366166821}[]{#_Toc366220133}[]{#_Toc366153079}[]{#_Toc366166822}[]{#_Toc366220134}[]{#_Toc366153080}[]{#_Toc366166823}[]{#_Toc366220135}[]{#_Toc366153081}[]{#_Toc366166824}[]{#_Toc366220136}[]{#_Toc366153082}[]{#_Toc366166825}[]{#_Toc366220137}[]{#_Toc366153083}[]{#_Toc366166826}[]{#_Toc366220138}[]{#_Toc366153084}[]{#_Toc366166827}[]{#_Toc366220139}[]{#_Toc366153085}[]{#_Toc366166828}[]{#_Toc366220140}[]{#_Toc366153086}[]{#_Toc366166829}[]{#_Toc366220141}[]{#_Toc366153087}[]{#_Toc366166830}[]{#_Toc366220142}[]{#_Toc366153088}[]{#_Toc366166831}[]{#_Toc366220143}[]{#_Toc366153089}[]{#_Toc366166832}[]{#_Toc366220144}[]{#_Toc366153090}[]{#_Toc366166833}[]{#_Toc366220145}[]{#_Toc366153091}[]{#_Toc366166834}[]{#_Toc366220146}[]{#_Toc366153092}[]{#_Toc366166835}[]{#_Toc366220147}[]{#_Toc366153093}[]{#_Toc366166836}[]{#_Toc366220148}[]{#_Toc366153094}[]{#_Toc366166837}[]{#_Toc366220149}[]{#_Toc366153095}[]{#_Toc366166838}[]{#_Toc366220150}[]{#_Toc366153096}[]{#_Toc366166839}[]{#_Toc366220151}[]{#_Toc366153097}[]{#_Toc366166840}[]{#_Toc366220152}[]{#_Toc366153098}[]{#_Toc366166841}[]{#_Toc366220153}[]{#_Toc366153099}[]{#_Toc366166842}[]{#_Toc366220154}[]{#_Toc366153100}[]{#_Toc366166843}[]{#_Toc366220155}[]{#_Toc366153101}[]{#_Toc366166844}[]{#_Toc366220156}[]{#_Toc366153102}[]{#_Toc366166845}[]{#_Toc366220157}[]{#_Toc366153103}[]{#_Toc366166846}[]{#_Toc366220158}[]{#_Toc366153104}[]{#_Toc366166847}[]{#_Toc366220159}[]{#_Toc366153105}[]{#_Toc366166848}[]{#_Toc366220160}[]{#_Toc366153106}[]{#_Toc366166849}[]{#_Toc366220161}[]{#_Toc366153107}[]{#_Toc366166850}[]{#_Toc366220162}[]{#_Toc366153108}[]{#_Toc366166851}[]{#_Toc366220163}[]{#_Toc366153109}[]{#_Toc366166852}[]{#_Toc366220164}[]{#_Toc366153110}[]{#_Toc366166853}[]{#_Toc366220165}[]{#_Toc366153111}[]{#_Toc366166854}[]{#_Toc366220166}[]{#_Toc366153112}[]{#_Toc366166855}[]{#_Toc366220167}[]{#_Toc366153113}[]{#_Toc366166856}[]{#_Toc366220168}[]{#_Toc366153114}[]{#_Toc366166857}[]{#_Toc366220169}[]{#_Toc366153115}[]{#_Toc366166858}[]{#_Toc366220170}[]{#_Toc366153116}[]{#_Toc366166859}[]{#_Toc366220171}[]{#_Toc366153117}[]{#_Toc366166860}[]{#_Toc366220172}[]{#_Toc366153118}[]{#_Toc366166861}[]{#_Toc366220173}[]{#_Toc366153119}[]{#_Toc366166862}[]{#_Toc366220174}[]{#_Toc366153120}[]{#_Toc366166863}[]{#_Toc366220175}[]{#_Toc366153121}[]{#_Toc366166864}[]{#_Toc366220176}[]{#_Toc366153122}[]{#_Toc366166865}[]{#_Toc366220177}[]{#_Toc366153123}[]{#_Toc366166866}[]{#_Toc366220178}[]{#_Toc366153124}[]{#_Toc366166867}[]{#_Toc366220179}[]{#_Toc366153125}[]{#_Toc366166868}[]{#_Toc366220180}[]{#_Toc366153126}[]{#_Toc366166869}[]{#_Toc366220181}[]{#_Toc366153127}[]{#_Toc366166870}[]{#_Toc366220182}[]{#_Toc366153128}[]{#_Toc366166871}[]{#_Toc366220183}[]{#_Toc366153129}[]{#_Toc366166872}[]{#_Toc366220184}[]{#_Toc366153130}[]{#_Toc366166873}[]{#_Toc366220185}[]{#_Toc366153131}[]{#_Toc366166874}[]{#_Toc366220186}[]{#_Toc366153132}[]{#_Toc366166875}[]{#_Toc366220187}[]{#_Toc366153133}[]{#_Toc366166876}[]{#_Toc366220188}[]{#_Toc366153134}[]{#_Toc366166877}[]{#_Toc366220189}[]{#_Toc366153135}[]{#_Toc366166878}[]{#_Toc366220190}[]{#_Toc366153136}[]{#_Toc366166879}[]{#_Toc366220191}[]{#_Toc366153137}[]{#_Toc366166880}[]{#_Toc366220192}[]{#_Toc366153138}[]{#_Toc366166881}[]{#_Toc366220193}[]{#_Toc366153139}[]{#_Toc366166882}[]{#_Toc366220194}[]{#_Toc366153140}[]{#_Toc366166883}[]{#_Toc366220195}[]{#_Toc366153141}[]{#_Toc366166884}[]{#_Toc366220196}[]{#_Toc366153142}[]{#_Toc366166885}[]{#_Toc366220197}[]{#_Toc366153143}[]{#_Toc366166886}[]{#_Toc366220198}[]{#_Toc366153144}[]{#_Toc366166887}[]{#_Toc366220199}[]{#_Toc366153145}[]{#_Toc366166888}[]{#_Toc366220200}[]{#_Toc366153146}[]{#_Toc366166889}[]{#_Toc366220201}[]{#_Toc366153147}[]{#_Toc366166890}[]{#_Toc366220202}[]{#_Toc366153148}[]{#_Toc366166891}[]{#_Toc366220203}[]{#_Toc366153149}[]{#_Toc366166892}[]{#_Toc366220204}[]{#_Toc366153150}[]{#_Toc366166893}[]{#_Toc366220205}[]{#_Toc366153151}[]{#_Toc366166894}[]{#_Toc366220206}[]{#_Toc366153152}[]{#_Toc366166895}[]{#_Toc366220207}[]{#_Toc366153153}[]{#_Toc366166896}[]{#_Toc366220208}[]{#_Toc366153154}[]{#_Toc366166897}[]{#_Toc366220209}

**BGP \-- BGP配置命令 \-- display bgp routing-table ipv6 unicast inlabel**

------------------------------------------------------------------------

[**[display bgp routing-table]{lang="EN-US"}[ ipv6 unicast inlabel]{lang="EN-US"}**]{#struct_0_65458_x3406_1368793254}[命令用来显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的入标签信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1150963391}

[**[display bgp]{lang="EN-US"}**[ **routing-table ipv6** \[ **unicast** \] **inlabel**]{lang="EN-US"}]{#struct_0_65458_x3406_x717572285}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_145156431}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_706630147}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1393643901}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1233324603}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x553893166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1206676167}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1923122504}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x717506749}

[[执行本命令时指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x614417481}[参数和不指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[参数的效果相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_62474047}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1445830460}[显示所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的入标签信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 inlabel]{lang="EN-US"}]{#struct_0_65458_x3406_x717375677}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 2.2.2.2]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 1::1                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : 10::1                                    OutLabel  : NULL]{lang="EN-US"}

[     InLabel : 1279]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  Network : 10::                                     PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::                                       OutLabel  : NULL]{lang="EN-US"}

[     InLabel : 1278]{lang="EN-US"}

[[表1-34 ]{lang="EN-US"}[display bgp routing-table ipv6 unicast inlabel]{lang="EN-US"}]{#struct_0_65458_x3406_140128293}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x493770741}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x803194125}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1012187977}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_252279204}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_84938873}[路由总数]{style="font-family:宋体"}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x717310141}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x637218217}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_1606846153}

[[路由状态代码，请参见]{style="font-family:宋体"}]{#struct_0_65458_x3406_x955118564}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-29]{lang="EN-US"}](?-140693803#_Ref319653110)

[[Origin]{lang="EN-US"}]{#struct_0_65458_x3406_x717244605}

[[路由起源代码，请参见]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1416846234}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-29]{lang="EN-US"}](?-140693803#_Ref319653110)

[[Network]{lang="EN-US"}]{#struct_0_65458_x3406_1052297703}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_476509462}

[[PrefixLen]{lang="EN-US"}]{#struct_0_65458_x3406_x1521217226}

[[目的网络地址的前缀长度]{style="font-family:宋体"}]{#struct_0_65458_x3406_x717179069}

[[NextHop]{lang="EN-US"}]{#struct_0_65458_x3406_x682622380}

[[下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x884122627}[地址]{style="font-family:宋体"}

[[OutLabel]{lang="EN-US"}]{#struct_0_65458_x3406_x2039653585}

[[出标签值，即对端]{style="font-family:宋体"}[6PE]{lang="EN-US"}]{#struct_0_65458_x3406_x958253917}[设备为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由分配的标签值]{style="font-family:宋体"}

[[InLabel]{lang="EN-US"}]{#struct_0_65458_x3406_x718162109}

[[入标签值，即本地]{style="font-family:宋体"}[6PE]{lang="EN-US"}]{#struct_0_65458_x3406_x1616910109}[设备为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由分配的标签值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#732661804 .myid}
[]{#_Toc404788625}[]{#struct_0_65458_x3406_x1696216716}[]{#_Toc311730288}

**BGP \-- BGP配置命令 \-- display bgp routing-table ipv6 unicast outlabel**

------------------------------------------------------------------------

[**[display bgp routing-table]{lang="EN-US"}[ ipv6 unicast outlabel]{lang="EN-US"}**]{#struct_0_65458_x3406_x1638592387}[命令用来显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的出标签信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x849721982}

[**[display bgp]{lang="EN-US"}**[ **routing-table ipv6** \[ **unicast** \] **outlabel**]{lang="EN-US"}]{#struct_0_65458_x3406_x808810988}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x718096573}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x25511187}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1406434662}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x856427056}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x433601969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1058968004}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_1739716116}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1484051582}

[[执行本命令时指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_848446123}[参数和不指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[参数的效果相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_311625009}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1338113128}[显示公网所有]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的出标签信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv6 outlabel]{lang="EN-US"}]{#struct_0_65458_x3406_848577195}

[ ]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP local router ID is 2.2.2.2]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>i Network : 4::4                                     PrefixLen : 128]{lang="EN-US"}

[     NextHop : ::FFFF:3.3.3.3                           OutLabel  : 1279]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>i Network : 20::                                     PrefixLen : 64]{lang="EN-US"}

[     NextHop : ::FFFF:3.3.3.3                           OutLabel  : 1278]{lang="EN-US"}

[[表1-35 ]{lang="EN-US"}[display bgp routing-table ipv6 unicast outlabel]{lang="EN-US"}]{#struct_0_65458_x3406_1907099022}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x491261429}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_137182559}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_1123914199}

[[Total number of routes]{lang="EN-US"}]{#struct_0_65458_x3406_x361996202}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1406870197}[路由总数]{style="font-family:宋体"}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_65458_x3406_848642731}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_541912681}[本地路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Status codes]{lang="EN-US"}]{#struct_0_65458_x3406_1048173881}

[[路由状态代码，请参见]{style="font-family:宋体"}]{#struct_0_65458_x3406_x923152620}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-29]{lang="EN-US"}](?-140693803#_Ref319653110)

[[Origin]{lang="EN-US"}]{#struct_0_65458_x3406_2050288137}

[[路由起源代码，请参见]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1423459035}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-29]{lang="EN-US"}](?-140693803#_Ref319653110)

[[Network]{lang="EN-US"}]{#struct_0_65458_x3406_848708267}

[[目的网络地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_980395976}

[[PrefixLen]{lang="EN-US"}]{#struct_0_65458_x3406_2127256656}

[[目的网络地址的前缀长度]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1775157788}

[[NextHop]{lang="EN-US"}]{#struct_0_65458_x3406_848773803}

[[下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1345852387}[地址]{style="font-family:宋体"}

[[OutLabel]{lang="EN-US"}]{#struct_0_65458_x3406_1707485496}

[[出标签值，即对端]{style="font-family:宋体"}[6PE]{lang="EN-US"}]{#struct_0_65458_x3406_415918709}[设备为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由分配的标签值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#582631216 .myid}
[]{#_Toc404788626}[]{#struct_0_65458_x3406_315397602}[]{#_Toc333308228}[]{#_Toc366153157}[]{#_Toc366166900}[]{#_Toc366220212}[]{#_Toc366153158}[]{#_Toc366166901}[]{#_Toc366220213}[]{#_Toc366153159}[]{#_Toc366166902}[]{#_Toc366220214}[]{#_Toc366153160}[]{#_Toc366166903}[]{#_Toc366220215}[]{#_Toc366153161}[]{#_Toc366166904}[]{#_Toc366220216}[]{#_Toc366153162}[]{#_Toc366166905}[]{#_Toc366220217}[]{#_Toc366153163}[]{#_Toc366166906}[]{#_Toc366220218}[]{#_Toc366153164}[]{#_Toc366166907}[]{#_Toc366220219}[]{#_Toc366153165}[]{#_Toc366166908}[]{#_Toc366220220}[]{#_Toc366153166}[]{#_Toc366166909}[]{#_Toc366220221}[]{#_Toc366153167}[]{#_Toc366166910}[]{#_Toc366220222}[]{#_Toc366153168}[]{#_Toc366166911}[]{#_Toc366220223}[]{#_Toc366153169}[]{#_Toc366166912}[]{#_Toc366220224}[]{#_Toc366153170}[]{#_Toc366166913}[]{#_Toc366220225}[]{#_Toc366153171}[]{#_Toc366166914}[]{#_Toc366220226}[]{#_Toc366153172}[]{#_Toc366166915}[]{#_Toc366220227}[]{#_Toc366153173}[]{#_Toc366166916}[]{#_Toc366220228}[]{#_Toc366153174}[]{#_Toc366166917}[]{#_Toc366220229}[]{#_Toc366153175}[]{#_Toc366166918}[]{#_Toc366220230}[]{#_Toc366153176}[]{#_Toc366166919}[]{#_Toc366220231}[]{#_Toc366153177}[]{#_Toc366166920}[]{#_Toc366220232}[]{#_Toc366153178}[]{#_Toc366166921}[]{#_Toc366220233}[]{#_Toc366153179}[]{#_Toc366166922}[]{#_Toc366220234}[]{#_Toc366153180}[]{#_Toc366166923}[]{#_Toc366220235}[]{#_Toc366153181}[]{#_Toc366166924}[]{#_Toc366220236}[]{#_Toc366153182}[]{#_Toc366166925}[]{#_Toc366220237}[]{#_Toc366153183}[]{#_Toc366166926}[]{#_Toc366220238}[]{#_Toc366153184}[]{#_Toc366166927}[]{#_Toc366220239}[]{#_Toc366153185}[]{#_Toc366166928}[]{#_Toc366220240}[]{#_Toc366153186}[]{#_Toc366166929}[]{#_Toc366220241}[]{#_Toc366153187}[]{#_Toc366166930}[]{#_Toc366220242}[]{#_Toc366153188}[]{#_Toc366166931}[]{#_Toc366220243}[]{#_Toc366153189}[]{#_Toc366166932}[]{#_Toc366220244}[]{#_Toc366153190}[]{#_Toc366166933}[]{#_Toc366220245}[]{#_Toc366153191}[]{#_Toc366166934}[]{#_Toc366220246}[]{#_Toc366153192}[]{#_Toc366166935}[]{#_Toc366220247}[]{#_Toc366153193}[]{#_Toc366166936}[]{#_Toc366220248}[]{#_Toc366153194}[]{#_Toc366166937}[]{#_Toc366220249}[]{#_Toc366153195}[]{#_Toc366166938}[]{#_Toc366220250}[]{#_Toc366153196}[]{#_Toc366166939}[]{#_Toc366220251}[]{#_Toc366153197}[]{#_Toc366166940}[]{#_Toc366220252}[]{#_Toc366153198}[]{#_Toc366166941}[]{#_Toc366220253}[]{#_Toc366153199}[]{#_Toc366166942}[]{#_Toc366220254}[]{#_Toc366153200}[]{#_Toc366166943}[]{#_Toc366220255}[]{#_Toc366153201}[]{#_Toc366166944}[]{#_Toc366220256}[]{#_Toc366153202}[]{#_Toc366166945}[]{#_Toc366220257}[]{#_Toc366153203}[]{#_Toc366166946}[]{#_Toc366220258}[]{#_Toc366153204}[]{#_Toc366166947}[]{#_Toc366220259}[]{#_Toc366153205}[]{#_Toc366166948}[]{#_Toc366220260}[]{#_Toc366153206}[]{#_Toc366166949}[]{#_Toc366220261}[]{#_Toc366153207}[]{#_Toc366166950}[]{#_Toc366220262}[]{#_Toc366153208}[]{#_Toc366166951}[]{#_Toc366220263}[]{#_Toc366153209}[]{#_Toc366166952}[]{#_Toc366220264}[]{#_Toc366153210}[]{#_Toc366166953}[]{#_Toc366220265}[]{#_Toc366153211}[]{#_Toc366166954}[]{#_Toc366220266}[]{#_Toc366153212}[]{#_Toc366166955}[]{#_Toc366220267}[]{#_Toc366153213}[]{#_Toc366166956}[]{#_Toc366220268}[]{#_Toc366153214}[]{#_Toc366166957}[]{#_Toc366220269}[]{#_Toc366153215}[]{#_Toc366166958}[]{#_Toc366220270}[]{#_Toc366153216}[]{#_Toc366166959}[]{#_Toc366220271}[]{#_Toc366153217}[]{#_Toc366166960}[]{#_Toc366220272}[]{#_Toc366153218}[]{#_Toc366166961}[]{#_Toc366220273}[]{#_Toc366153228}[]{#_Toc366166971}[]{#_Toc366220283}[]{#_Toc366153229}[]{#_Toc366166972}[]{#_Toc366220284}[]{#_Toc366153230}[]{#_Toc366166973}[]{#_Toc366220285}[]{#_Toc366153231}[]{#_Toc366166974}[]{#_Toc366220286}[]{#_Toc366153232}[]{#_Toc366166975}[]{#_Toc366220287}[]{#_Toc366153233}[]{#_Toc366166976}[]{#_Toc366220288}[]{#_Toc366153234}[]{#_Toc366166977}[]{#_Toc366220289}[]{#_Toc366153235}[]{#_Toc366166978}[]{#_Toc366220290}[]{#_Toc366153236}[]{#_Toc366166979}[]{#_Toc366220291}[]{#_Toc366153237}[]{#_Toc366166980}[]{#_Toc366220292}[]{#_Toc366153238}[]{#_Toc366166981}[]{#_Toc366220293}[]{#_Toc366153239}[]{#_Toc366166982}[]{#_Toc366220294}[]{#_Toc366153240}[]{#_Toc366166983}[]{#_Toc366220295}[]{#_Toc366153241}[]{#_Toc366166984}[]{#_Toc366220296}[]{#_Toc366153242}[]{#_Toc366166985}[]{#_Toc366220297}[]{#_Toc366153243}[]{#_Toc366166986}[]{#_Toc366220298}[]{#_Toc366153244}[]{#_Toc366166987}[]{#_Toc366220299}[]{#_Toc366153245}[]{#_Toc366166988}[]{#_Toc366220300}[]{#_Toc366153246}[]{#_Toc366166989}[]{#_Toc366220301}[]{#_Toc366153247}[]{#_Toc366166990}[]{#_Toc366220302}[]{#_Toc366153248}[]{#_Toc366166991}[]{#_Toc366220303}[]{#_Toc366153249}[]{#_Toc366166992}[]{#_Toc366220304}[]{#_Toc366153256}[]{#_Toc366166999}[]{#_Toc366220311}[]{#_Toc299632354}[]{#_Toc299632355}[]{#_Toc299632356}[]{#_Toc299632357}[]{#_Toc299632358}[]{#_Toc299632359}[]{#_Toc299632360}[]{#_Toc299632361}[]{#_Toc299632362}[]{#_Toc299632363}[]{#_Toc299632364}[]{#_Toc299632365}[]{#_Toc299632366}[]{#_Toc299632367}[]{#_Toc299632368}[]{#_Toc299632369}[]{#_Toc299632372}[]{#_Toc302638034}[]{#_Toc307230770}

**BGP \-- BGP配置命令 \-- display bgp update-group**

------------------------------------------------------------------------

[**[display bgp ]{lang="EN-US"}[update-group]{lang="EN-US"}**]{#struct_0_65458_x3406_1832804296}[命令用来显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x703708754}

[**[display bgp ]{lang="EN-US"}[update-group]{lang="EN-US"}**[ **ipv4** { **mdt**]{lang="EN-US"}[ \| **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x192718684}

[**[display bgp update-group ipv6 ]{lang="EN-US"}**[{]{lang="EN-US"}**[ multicast]{lang="EN-US"}**[ \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *ipv6-address* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1732012449}

[**[display bgp ]{lang="EN-US"}[update-group ipv6 ]{lang="EN-US"}**[\[ **unicast** \] \[ ]{lang="EN-US"}*[ip-address]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_65458_x3406_x192456540}

[**[display bgp ]{lang="EN-US"}[update-group vpnv4]{lang="EN-US"}**[ \[ **vpn-instance** ]{lang="EN-US"}*[vpn-instance-name ]{lang="EN-US"}*[\]]{lang="EN-US"}[ \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x192063324}

[**[display bgp ]{lang="EN-US"}[update-group ]{lang="EN-US"}**[{ **l2vpn**]{lang="EN-US"}[ \| **vpnv6** } \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_65458_x3406_59826131}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_847921836}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x502027784}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_784682566}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1737805193}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x1672426220}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1522618018}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x704849802}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_899353432}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_59432914}[：显示]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[地址族的打包组信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x192718685}[：显示]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[地址族的打包组信息。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_65458_x3406_59105234}[：显示]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族的打包组信息。]{style="font-family:宋体"}

[**[l2vpn]{lang="EN-US"}**]{#struct_0_65458_x3406_59826130}[：显示]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族的打包组信息。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_65458_x3406_59891666}[：显示]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[地址族的打包组信息。]{style="font-family:宋体"}

[**[mdt]{lang="EN-US"}**]{#struct_0_65458_x3406_x192325469}[：显示]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[地址族的打包组信息。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x192522077}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播地址族的打包组信息。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x192128861}[：显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播地址族的打包组信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x34847649}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组相关信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[打包组相关信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_847987372}[：显示指定对等体所在打包组的信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为对等体]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_59105233}[：显示指定对等体所在打包组的信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为对等体]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1822737457}

[[按组打包技术是指将出口策略相同的对等体归为一组，形成一个打包组，设备向打包组中的对等体发布路由时，统一对路由进行策略过滤，并构造路由更新报文（即打包），以避免重复地进行策略过滤和构造报文。]{style="font-family:宋体"}]{#struct_0_65458_x3406_739098345}

[[实现按组打包后，每条路由前缀信息只需要经过一次策略过滤并打包一次，然后发布给打包组内的所有对等体。例如，如果不采用按组打包，]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_65458_x3406_x1716592068}[条路由向]{style="font-family:宋体"}[1000]{lang="EN-US"}[个对等体发布时，需要匹配]{style="font-family:宋体"}[1000]{lang="EN-US"}[×]{style="font-family:宋体"}[1000]{lang="EN-US"}[次策略，并进行]{style="font-family:宋体"}[1000]{lang="EN-US"}[×]{style="font-family:宋体"}[1000]{lang="EN-US"}[次打包处理；如果采用按组打包，]{style="font-family:宋体"}[1000]{lang="EN-US"}[个对等体的出口策略相同（如数据中心组网中）时，只需要匹配]{style="font-family:宋体"}[1000]{lang="EN-US"}[×]{style="font-family:宋体"}[1]{lang="EN-US"}[次策略，并进行]{style="font-family:
宋体"}[1000]{lang="EN-US"}[×]{style="font-family:宋体"}[1]{lang="EN-US"}[次打包处理，打包效率提高了]{style="font-family:宋体"}[1000]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x192653150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定任何参数，则显示指定地址族公网所有]{style="font-family:宋体"}]{#struct_0_65458_x3406_207887253}[BGP]{lang="EN-US"}[打包组信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定]{lang="EN-US" style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x192325470}[、]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{lang="EN-US" style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1834938886}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_848446121}[显示公网内]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族的所有打包组信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_311625011}

[ ]{lang="EN-US"}

[  Update-group ID: 0 ]{lang="EN-US"}

[  Type: EBGP link ]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 1]{lang="EN-US"}

[    99.1.1.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x618202016}[显示公网内]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播对等体]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[所在打包组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group ipv4 1.1.1.2]{lang="EN-US"}]{#struct_0_65458_x3406_848511657}

[ ]{lang="EN-US"}

[  Update-group ID: 0 ]{lang="EN-US"}

[  Type: EBGP link ]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 2]{lang="EN-US"}

[    1.1.1.2]{lang="EN-US"}

[    1.1.1.3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x192456542}[显示公网内]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播地址族的所有打包组信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group ipv6 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_x192063326}

[ ]{lang="EN-US"}

[  Update-group ID: 0]{lang="EN-US"}

[  Type: EBGP link]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 1]{lang="EN-US"}

[    99::1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x192587615}[显示公网内]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播对等体]{style="font-family:宋体"}[1::2]{lang="EN-US"}[所在打包组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group ipv6 multicast  1::2]{lang="EN-US"}]{#struct_0_65458_x3406_x192718687}

[ ]{lang="EN-US"}

[  Update-group ID: 0]{lang="EN-US"}

[  Type: EBGP link]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 2]{lang="EN-US"}

[    1::2]{lang="EN-US"}

[    1::3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_59236304}[显示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[所在打包组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group vpnv4 vpn-instance vpn1 1.1.1.2]{lang="EN-US"}]{#struct_0_65458_x3406_59367375}

[ ]{lang="EN-US"}

[  Update-group ID: 0 ]{lang="EN-US"}

[  Type: EBGP link ]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  Nesting VPN: vpn1]{lang="EN-US"}

[  Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 2]{lang="EN-US"}

[    1.1.1.2]{lang="EN-US"}

[    1.1.1.3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_59498447}[显示]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族的所有打包组信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group l2vpn]{lang="EN-US"}]{#struct_0_65458_x3406_59236303}

[ ]{lang="EN-US"}

[  Update-group ID: 0]{lang="EN-US"}

[  Type: IBGP link]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  L2VPN signaling (VPLS): Supported]{lang="EN-US"}

[  L2VPN signaling (VPWS): RFC mode]{lang="EN-US"}

[  L2VPN auto-discovery: RFC mode]{lang="EN-US"}

[  Minimum time between advertisements: 15 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 2]{lang="EN-US"}

[    2.2.2.9]{lang="EN-US"}

[    3.3.3.9]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_59891663}[显示]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[所在打包组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group l2vpn 1.1.1.3]{lang="EN-US"}]{#struct_0_65458_x3406_59498446}

[ ]{lang="EN-US"}

[  Update-group ID: 0]{lang="EN-US"}

[  Type: IBGP link]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  L2VPN signaling (VPLS): Supported]{lang="EN-US"}

[  L2VPN signaling (VPWS): Draft mode]{lang="EN-US"}

[  Minimum time between advertisements: 15 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 1]{lang="EN-US"}

[    1.1.1.3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_59105230}[显示]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1.1.1.4]{lang="EN-US"}[所在打包组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp update-group l2vpn 1.1.1.4]{lang="EN-US"}]{#struct_0_65458_x3406_1625385784}

[ ]{lang="EN-US"}

[  Update-group ID: 0]{lang="EN-US"}

[  Type: EBGP link]{lang="EN-US"}

[  4-byte AS number: Supported]{lang="EN-US"}

[  Site-of-Origin: Not specified]{lang="EN-US"}

[  L2VPN signaling (VPLS): Supported]{lang="EN-US"}

[  L2VPN signaling (VPWS): RFC mode]{lang="EN-US"}

[  L2VPN auto-discovery: Non-standard mode]{lang="EN-US"}

[  Minimum time between advertisements: 30 seconds]{lang="EN-US"}

[  OutQ: 0]{lang="EN-US"}

[  Members: 1]{lang="EN-US"}

[    1.1.1.4]{lang="EN-US"}

[[表1-36 ]{lang="EN-US"}[display bgp update-group]{lang="EN-US"}]{#struct_0_65458_x3406_x1664255403}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x498160725}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_x604147914}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_x23179602}

[[Update-group ID]{lang="EN-US"}]{#struct_0_65458_x3406_x63637118}

[[打包组]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_473066926}

[[Type]{lang="EN-US"}]{#struct_0_65458_x3406_848577193}

[[打包组中对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1907099024}[连接类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_137313631}[：]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_1368584331}[：]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Confed IBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_x373807724}[：]{lang="EN-US" style="font-family:
  宋体"}[联盟]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Confed EBGP link]{lang="EN-US"}]{#struct_0_65458_x3406_848642729}[：]{lang="EN-US" style="font-family:
  宋体"}[联盟]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[Label capability: Supported]{lang="EN-US"}]{#struct_0_65458_x3406_x1796739487}

[[打包组中的对等体具有交换带标签路由的能力]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1210997632}

[[4-byte AS number: Supported]{lang="EN-US"}]{#struct_0_65458_x3406_689991884}

[[没有为打包组中的对等体使能]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_65458_x3406_x1417898245}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号抑制功能，即打包组中的对等体支持]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[4-byte AS number: Suppressed]{lang="EN-US"}]{#struct_0_65458_x3406_848708265}

[[为打包组中的对等体使能]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_65458_x3406_980395978}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号抑制功能]{style="font-family:宋体"}

[[Fake AS]{lang="EN-US"}]{#struct_0_65458_x3406_2127256646}

[[为打包组中的对等体配置了虚拟的本地自治系统号]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1775157789}

[[Public-AS-Only: Yes]{lang="EN-US"}]{#struct_0_65458_x3406_848773801}

[[向打包组中的对等体发送]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1345852385}[更新消息时只携带公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，不携带私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_65458_x3406_x1504796062}[时，如果对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则]{style="font-family:宋体"}[AS]{lang="EN-US"}[号作为打包组的分组条件；如果对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则]{style="font-family:宋体"}[AS]{lang="EN-US"}[号不作为打包组的分组条件]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}[No]{lang="EN-US"}]{#struct_0_65458_x3406_638351629}[时，对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号不作为打包组的分组条件]{style="font-family:宋体"}

[[Substitute-AS: Yes]{lang="EN-US"}]{#struct_0_65458_x3406_x1424682386}

[[用本地]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_478507418}[号替换]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性里打包组中对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Site-of-Origin]{lang="EN-US"}]{#struct_0_65458_x3406_1625320248}

[[为打包组中的对等体指定的]{style="font-family:宋体"}[SoO]{lang="EN-US"}]{#struct_0_65458_x3406_1625385783}[属性值]{style="font-family:宋体"}

[[Minimum time between advertisements: *number* seconds]{lang="EN-US"}]{#struct_0_65458_x3406_848839337}

[[向打包组中对等体发布同一路由的最小时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1961091902}

[[Advertising community: Yes]{lang="EN-US"}]{#struct_0_65458_x3406_x1336917474}

[[向打包组中的对等体发布团体属性]{style="font-family:宋体"}]{#struct_0_65458_x3406_x169278845}

[[Route-reflect client: Yes]{lang="EN-US"}]{#struct_0_65458_x3406_848904873}

[[打包组中的对等体是路由反射器的客户机]{style="font-family:宋体"}]{#struct_0_65458_x3406_837020706}

[[Advertising extended community: Yes]{lang="EN-US"}]{#struct_0_65458_x3406_315397591}

[[向打包组中的对等体发布扩展团体属性]{style="font-family:宋体"}]{#struct_0_65458_x3406_693687394}

[[Export AS-path-ACL]{lang="EN-US"}]{#struct_0_65458_x3406_847921833}

[[为打包组中的对等体设置了基于]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x502027779}[路径过滤列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由出方向过滤策略]{style="font-family:宋体"}

[[Export prefix list]{lang="EN-US"}]{#struct_0_65458_x3406_783961677}

[[为打包组中的对等体设置了基于地址前缀列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x721415882}[路由出方向过滤策略]{style="font-family:宋体"}

[[Export route policy]{lang="EN-US"}]{#struct_0_65458_x3406_847987369}

[[对发布给打包组中对等体的路由应用了路由策略]{style="font-family:宋体"}]{#struct_0_65458_x3406_x133577684}

[[Export filter-policy]{lang="EN-US"}]{#struct_0_65458_x3406_2092860587}

[[为打包组中的对等体设置了基于]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_65458_x3406_848446122}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由出发向过滤策略]{style="font-family:宋体"}

[[OutQ]{lang="EN-US"}]{#struct_0_65458_x3406_311625008}

[[等待发往打包组中对等体的前缀数目]{style="font-family:宋体"}]{#struct_0_65458_x3406_1338113129}

[[Members]{lang="EN-US"}]{#struct_0_65458_x3406_848511658}

[[打包组中对等体的数目及对等体的地址]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1664255400}

[[Nesting VPN]{lang="EN-US"}]{#struct_0_65458_x3406_1625320246}

[[打包组中的对等体使能了嵌套]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_65458_x3406_1625385781}[功能]{style="font-family:宋体"}

[[Nexthop invariable: Yes]{lang="EN-US"}]{#struct_0_65458_x3406_1625123637}

[[向打包组中的对等体发布路由时不改变下一跳]{style="font-family:宋体"}]{#struct_0_65458_x3406_1625320245}

[[UPE: Yes]{lang="EN-US"}]{#struct_0_65458_x3406_1625385780}

[[打包组中的对等体为]{style="font-family:宋体"}[UPE]{lang="EN-US"}]{#struct_0_65458_x3406_1625582388}

[[UPE export route policy]{lang="EN-US"}]{#struct_0_65458_x3406_1625320244}

[[为打包组中的]{style="font-family:宋体"}[UPE]{lang="EN-US"}]{#struct_0_65458_x3406_1625385779}[对等体应用了出方向路由策略]{style="font-family:宋体"}

[[L2VPN signaling (VPLS): Supported]{lang="EN-US"}]{#struct_0_65458_x3406_1625582387}

[[打包组中的对等体支持采用]{style="font-family:宋体"}[RFC 4761]{lang="EN-US"}]{#struct_0_65458_x3406_1625254707}[定义的]{style="font-family:宋体"}[NLRI]{lang="EN-US"}[格式发布]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[标签块信息]{style="font-family:宋体"}

[[L2VPN signaling (VPWS): RFC mode]{lang="EN-US"}]{#struct_0_65458_x3406_1625975603}

[[打包组中的对等体支持采用]{style="font-family:宋体"}[RFC 4761]{lang="EN-US"}]{#struct_0_65458_x3406_x1103300963}[定义的]{style="font-family:宋体"}[NLRI]{lang="EN-US"}[格式发布]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息]{style="font-family:宋体"}

[[L2VPN signaling (VPWS): Draft mode]{lang="EN-US"}]{#struct_0_65458_x3406_x1103628643}

[[打包组中的对等体支持采用]{style="font-family:宋体"}[draft-kompella-ppvpn-l2vpn-03]{lang="EN-US"}]{#struct_0_65458_x3406_x1102907747}[草案定义的]{style="font-family:宋体"}[NLRI]{lang="EN-US"}[格式发布]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}[标签块信息]{style="font-family:宋体"}

[[L2VPN auto-discovery: RFC mode]{lang="EN-US"}]{#struct_0_65458_x3406_x1103366500}

[[打包组中的对等体支持采用]{style="font-family:宋体"}[RFC 6074]{lang="EN-US"}]{#struct_0_65458_x3406_x1103628644}[中定义的]{style="font-family:宋体"}[NLRI]{lang="EN-US"}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[L2VPN auto-discovery: Non-standard mode]{lang="EN-US"}]{#struct_0_65458_x3406_x1102907748}

[[打包组中的对等体支持采用非标准]{style="font-family:宋体"}[NLRI]{lang="EN-US"}]{#struct_0_65458_x3406_x1103366501}[格式交换]{style="font-family:宋体"}[VPLS PE]{lang="EN-US"}[信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1097773796 .myid}
[]{#_Toc33197998}[]{#_Toc404788627}[]{#struct_0_65458_x3406_x630444484}[]{#_Toc366658185}

**BGP \-- BGP配置命令 \-- display bgp-policy statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BGP命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_65458_x3406_x630378948}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65458_x3406_x630313412}
:::

[ ]{lang="EN-US"}

[**[display bgp-policy statistics]{lang="EN-US"}**]{#struct_0_65458_x3406_x630182340}[命令用来显示]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x630116804}

[**[display bgp-policy]{lang="EN-US"}**[ { **ip** \| **ipv6** } **statistics** { **input** \| **output** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x630051268}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x629985732}

[[任意视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x629854660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x630444483}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x630378947}

[[network-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x630313411}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x630247875}

[[mdc-operator]{lang="EN-US"}]{#struct_0_65458_x3406_x630116803}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x630051267}

[**[ip]{lang="EN-US"}**]{#struct_0_65458_x3406_x629985731}[：显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[流量的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x629854659}[：显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[流量的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[**[input]{lang="EN-US"}**]{#struct_0_65458_x3406_935639453}[：显示入方向上的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[**[output]{lang="EN-US"}**]{#struct_0_65458_x3406_935704989}[：显示出方向上的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_65458_x3406_935770525}[：显示指定接口上的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果不指定本参数，则显示全局的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_935901597}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_935967133}[显示全局]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[流量入方向的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp-policy ip statistics input]{lang="EN-US"}]{#struct_0_65458_x3406_936032669}

[Statistics for the inbound direction:]{lang="EN-US"}

[ Traffic index     Packets                  Bytes]{lang="EN-US"}

[ 1                 0                        0]{lang="EN-US"}

[ 2                 0                        0]{lang="EN-US"}

[ 3                 0                        0]{lang="EN-US"}

[ 4                 0                        0]{lang="EN-US"}

[ 5                 0                        0]{lang="EN-US"}

[ 6                 0                        0]{lang="EN-US"}

[ 7                 0                        0]{lang="EN-US"}

[ 8                 0                        0]{lang="EN-US"}

[ 9                 0                        0]{lang="EN-US"}

[ 10                0                        0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_936098205}[显示全局]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[流量入方向的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp-policy ipv6 statistics input]{lang="EN-US"}]{#struct_0_65458_x3406_936229277}

[Statistics for the inbound direction:]{lang="EN-US"}

[ Traffic index     Packets                  Bytes]{lang="EN-US"}

[ 1                 0                        0]{lang="EN-US"}

[ 2                 0                        0]{lang="EN-US"}

[ 3                 0                        0]{lang="EN-US"}

[ 4                 0                        0]{lang="EN-US"}

[ 5                 0                        0]{lang="EN-US"}

[ 6                 0                        0]{lang="EN-US"}

[ 7                 0                        0]{lang="EN-US"}

[ 8                 0                        0]{lang="EN-US"}

[ 9                 0                        0]{lang="EN-US"}

[ 10                0                        0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_65458_x3406_935639454}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_935704990}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[流量出方向的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp-policy ip statistics output interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_65458_x3406_935836062}

[Statistics for GigabitEthernet1/0/1 in the outbound direction:]{lang="EN-US"}

[ Traffic index     Packets                  Bytes]{lang="EN-US"}

[ 1                 0                        0]{lang="EN-US"}

[ 2                 0                        0]{lang="EN-US"}

[ 3                 0                        0]{lang="EN-US"}

[ 4                 0                        0]{lang="EN-US"}

[ 5                 0                        0]{lang="EN-US"}

[ 6                 0                        0]{lang="EN-US"}

[ 7                 0                        0]{lang="EN-US"}

[ 8                 0                        0]{lang="EN-US"}

[ 9                 0                        0]{lang="EN-US"}

[ 10                0                        0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_935901598}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[流量出方向的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp-policy ipv6 statistics output interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_65458_x3406_936032670}

[Statistics for GigabitEthernet1/0/1 in the outbound direction:]{lang="EN-US"}

[ Traffic index     Packets                  Bytes]{lang="EN-US"}

[ 1                 0                        0]{lang="EN-US"}

[ 2                 0                        0]{lang="EN-US"}

[ 3                 0                        0]{lang="EN-US"}

[ 4                 0                        0]{lang="EN-US"}

[ 5                 0                        0]{lang="EN-US"}

[ 6                 0                        0]{lang="EN-US"}

[ 7                 0                        0]{lang="EN-US"}

[ 8                 0                        0]{lang="EN-US"}

[ 9                 0                        0]{lang="EN-US"}

[ 10                0                        0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_65458_x3406_936098206}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_936229278}[显示接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[流量出方向的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp-policy ip statistics output interface vlan-interface 10]{lang="EN-US"}]{#struct_0_65458_x3406_935639451}

[Statistics for Vlan-interface10 in the outbound direction:]{lang="EN-US"}

[ Traffic index     Packets                  Bytes]{lang="EN-US"}

[ 1                 0                        0]{lang="EN-US"}

[ 2                 0                        0]{lang="EN-US"}

[ 3                 0                        0]{lang="EN-US"}

[ 4                 0                        0]{lang="EN-US"}

[ 5                 0                        0]{lang="EN-US"}

[ 6                 0                        0]{lang="EN-US"}

[ 7                 0                        0]{lang="EN-US"}

[ 8                 0                        0]{lang="EN-US"}

[ 9                 0                        0]{lang="EN-US"}

[ 10                0                        0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_935704987}[显示接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[流量出方向的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[策略计费信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp-policy ipv6 statistics output interface vlan-interface 10]{lang="EN-US"}]{#struct_0_65458_x3406_935836059}

[Statistics for Vlan-interface10 in the outbound direction:]{lang="EN-US"}

[ Traffic index     Packets                  Bytes]{lang="EN-US"}

[ 1                 0                        0]{lang="EN-US"}

[ 2                 0                        0]{lang="EN-US"}

[ 3                 0                        0]{lang="EN-US"}

[ 4                 0                        0]{lang="EN-US"}

[ 5                 0                        0]{lang="EN-US"}

[ 6                 0                        0]{lang="EN-US"}

[ 7                 0                        0]{lang="EN-US"}

[ 8                 0                        0]{lang="EN-US"}

[ 9                 0                        0]{lang="EN-US"}

[ 10                0                        0]{lang="EN-US"}

[[表1-37 ]{lang="EN-US"}[display bgp-policy statistics]{lang="EN-US"}]{#struct_0_65458_x3406_935901595}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_192956986}[[字段]{style="font-family:黑体"}]{#struct_0_65458_x3406_936032667}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_65458_x3406_936229275}

[[Traffic index]{lang="EN-US"}]{#struct_0_65458_x3406_935704988}

[[流量索引值]{style="font-family:宋体"}]{#struct_0_65458_x3406_935901596}

[[Packets]{lang="EN-US"}]{#struct_0_65458_x3406_936098204}

[[流量索引对应流量的报文个数，入方向时表示接收的报文个数，出方向时表示发送的报文个数]{style="font-family:宋体"}]{#struct_0_65458_x3406_936229276}

[[Bytes]{lang="EN-US"}]{#struct_0_65458_x3406_935770529}

[[流量索引对应流量的报文字节数，入方向时表示接收报文的字节数，出方向时表示发送报文的字节数]{style="font-family:宋体"}]{#struct_0_65458_x3406_935901601}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_935967137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bgp-policy accounting]{lang="EN-US"}**]{#struct_0_65458_x3406_936098209}

::: {#1314940343 .myid}
[]{#_Toc404788628}[]{#struct_0_65458_x3406_848839335}[]{#_Toc361659185}[]{#_Toc361659772}[]{#_Toc361660359}[]{#_Toc361663932}[]{#_Toc361747392}[]{#_Toc361819755}[]{#_Toc361659186}[]{#_Toc361659773}[]{#_Toc361660360}[]{#_Toc361663933}[]{#_Toc361747393}[]{#_Toc361819756}[]{#_Toc361659187}[]{#_Toc361659774}[]{#_Toc361660361}[]{#_Toc361663934}[]{#_Toc361747394}[]{#_Toc361819757}[]{#_Toc361659188}[]{#_Toc361659775}[]{#_Toc361660362}[]{#_Toc361663935}[]{#_Toc361747395}[]{#_Toc361819758}[]{#_Toc361659189}[]{#_Toc361659776}[]{#_Toc361660363}[]{#_Toc361663936}[]{#_Toc361747396}[]{#_Toc361819759}[]{#_Toc361659190}[]{#_Toc361659777}[]{#_Toc361660364}[]{#_Toc361663937}[]{#_Toc361747397}[]{#_Toc361819760}[]{#_Toc361659191}[]{#_Toc361659778}[]{#_Toc361660365}[]{#_Toc361663938}[]{#_Toc361747398}[]{#_Toc361819761}[]{#_Toc361659192}[]{#_Toc361659779}[]{#_Toc361660366}[]{#_Toc361663939}[]{#_Toc361747399}[]{#_Toc361819762}[]{#_Toc361659193}[]{#_Toc361659780}[]{#_Toc361660367}[]{#_Toc361663940}[]{#_Toc361747400}[]{#_Toc361819763}[]{#_Toc361659194}[]{#_Toc361659781}[]{#_Toc361660368}[]{#_Toc361663941}[]{#_Toc361747401}[]{#_Toc361819764}[]{#_Toc361659195}[]{#_Toc361659782}[]{#_Toc361660369}[]{#_Toc361663942}[]{#_Toc361747402}[]{#_Toc361819765}[]{#_Toc361659196}[]{#_Toc361659783}[]{#_Toc361660370}[]{#_Toc361663943}[]{#_Toc361747403}[]{#_Toc361819766}[]{#_Toc361659197}[]{#_Toc361659784}[]{#_Toc361660371}[]{#_Toc361663944}[]{#_Toc361747404}[]{#_Toc361819767}[]{#_Toc361659198}[]{#_Toc361659785}[]{#_Toc361660372}[]{#_Toc361663945}[]{#_Toc361747405}[]{#_Toc361819768}[]{#_Toc361659199}[]{#_Toc361659786}[]{#_Toc361660373}[]{#_Toc361663946}[]{#_Toc361747406}[]{#_Toc361819769}[]{#_Toc361659200}[]{#_Toc361659787}[]{#_Toc361660374}[]{#_Toc361663947}[]{#_Toc361747407}[]{#_Toc361819770}[]{#_Toc361659201}[]{#_Toc361659788}[]{#_Toc361660375}[]{#_Toc361663948}[]{#_Toc361747408}[]{#_Toc361819771}[]{#_Toc361659202}[]{#_Toc361659789}[]{#_Toc361660376}[]{#_Toc361663949}[]{#_Toc361747409}[]{#_Toc361819772}[]{#_Toc361659203}[]{#_Toc361659790}[]{#_Toc361660377}[]{#_Toc361663950}[]{#_Toc361747410}[]{#_Toc361819773}[]{#_Toc361659204}[]{#_Toc361659791}[]{#_Toc361660378}[]{#_Toc361663951}[]{#_Toc361747411}[]{#_Toc361819774}[]{#_Toc361659205}[]{#_Toc361659792}[]{#_Toc361660379}[]{#_Toc361663952}[]{#_Toc361747412}[]{#_Toc361819775}[]{#_Toc361659206}[]{#_Toc361659793}[]{#_Toc361660380}[]{#_Toc361663953}[]{#_Toc361747413}[]{#_Toc361819776}[]{#_Toc361659207}[]{#_Toc361659794}[]{#_Toc361660381}[]{#_Toc361663954}[]{#_Toc361747414}[]{#_Toc361819777}[]{#_Toc361659208}[]{#_Toc361659795}[]{#_Toc361660382}[]{#_Toc361663955}[]{#_Toc361747415}[]{#_Toc361819778}[]{#_Toc361659209}[]{#_Toc361659796}[]{#_Toc361660383}[]{#_Toc361663956}[]{#_Toc361747416}[]{#_Toc361819779}[]{#_Toc361659210}[]{#_Toc361659797}[]{#_Toc361660384}[]{#_Toc361663957}[]{#_Toc361747417}[]{#_Toc361819780}[]{#_Toc361659211}[]{#_Toc361659798}[]{#_Toc361660385}[]{#_Toc361663958}[]{#_Toc361747418}[]{#_Toc361819781}[]{#_Toc361659212}[]{#_Toc361659799}[]{#_Toc361660386}[]{#_Toc361663959}[]{#_Toc361747419}[]{#_Toc361819782}[]{#_Toc361659213}[]{#_Toc361659800}[]{#_Toc361660387}[]{#_Toc361663960}[]{#_Toc361747420}[]{#_Toc361819783}[]{#_Toc361659214}[]{#_Toc361659801}[]{#_Toc361660388}[]{#_Toc361663961}[]{#_Toc361747421}[]{#_Toc361819784}[]{#_Toc361659215}[]{#_Toc361659802}[]{#_Toc361660389}[]{#_Toc361663962}[]{#_Toc361747422}[]{#_Toc361819785}[]{#_Toc361659216}[]{#_Toc361659803}[]{#_Toc361660390}[]{#_Toc361663963}[]{#_Toc361747423}[]{#_Toc361819786}[]{#_Toc361659217}[]{#_Toc361659804}[]{#_Toc361660391}[]{#_Toc361663964}[]{#_Toc361747424}[]{#_Toc361819787}[]{#_Toc361659218}[]{#_Toc361659805}[]{#_Toc361660392}[]{#_Toc361663965}[]{#_Toc361747425}[]{#_Toc361819788}[]{#_Toc361659219}[]{#_Toc361659806}[]{#_Toc361660393}[]{#_Toc361663966}[]{#_Toc361747426}[]{#_Toc361819789}[]{#_Toc361659220}[]{#_Toc361659807}[]{#_Toc361660394}[]{#_Toc361663967}[]{#_Toc361747427}[]{#_Toc361819790}[]{#_Toc361659221}[]{#_Toc361659808}[]{#_Toc361660395}[]{#_Toc361663968}[]{#_Toc361747428}[]{#_Toc361819791}[]{#_Toc361659222}[]{#_Toc361659809}[]{#_Toc361660396}[]{#_Toc361663969}[]{#_Toc361747429}[]{#_Toc361819792}[]{#_Toc361659223}[]{#_Toc361659810}[]{#_Toc361660397}[]{#_Toc361663970}[]{#_Toc361747430}[]{#_Toc361819793}[]{#_Toc361659224}[]{#_Toc361659811}[]{#_Toc361660398}[]{#_Toc361663971}[]{#_Toc361747431}[]{#_Toc361819794}[]{#_Toc361659225}[]{#_Toc361659812}[]{#_Toc361660399}[]{#_Toc361663972}[]{#_Toc361747432}[]{#_Toc361819795}[]{#_Toc361659226}[]{#_Toc361659813}[]{#_Toc361660400}[]{#_Toc361663973}[]{#_Toc361747433}[]{#_Toc361819796}[]{#_Toc361659227}[]{#_Toc361659814}[]{#_Toc361660401}[]{#_Toc361663974}[]{#_Toc361747434}[]{#_Toc361819797}[]{#_Toc361659228}[]{#_Toc361659815}[]{#_Toc361660402}[]{#_Toc361663975}[]{#_Toc361747435}[]{#_Toc361819798}[]{#_Toc361659229}[]{#_Toc361659816}[]{#_Toc361660403}[]{#_Toc361663976}[]{#_Toc361747436}[]{#_Toc361819799}[]{#_Toc361659230}[]{#_Toc361659817}[]{#_Toc361660404}[]{#_Toc361663977}[]{#_Toc361747437}[]{#_Toc361819800}[]{#_Toc361659231}[]{#_Toc361659818}[]{#_Toc361660405}[]{#_Toc361663978}[]{#_Toc361747438}[]{#_Toc361819801}[]{#_Toc361659232}[]{#_Toc361659819}[]{#_Toc361660406}[]{#_Toc361663979}[]{#_Toc361747439}[]{#_Toc361819802}[]{#_Toc361659233}[]{#_Toc361659820}[]{#_Toc361660407}[]{#_Toc361663980}[]{#_Toc361747440}[]{#_Toc361819803}[]{#_Toc361659234}[]{#_Toc361659821}[]{#_Toc361660408}[]{#_Toc361663981}[]{#_Toc361747441}[]{#_Toc361819804}[]{#_Toc361659235}[]{#_Toc361659822}[]{#_Toc361660409}[]{#_Toc361663982}[]{#_Toc361747442}[]{#_Toc361819805}[]{#_Toc361659236}[]{#_Toc361659823}[]{#_Toc361660410}[]{#_Toc361663983}[]{#_Toc361747443}[]{#_Toc361819806}[]{#_Toc361659237}[]{#_Toc361659824}[]{#_Toc361660411}[]{#_Toc361663984}[]{#_Toc361747444}[]{#_Toc361819807}[]{#_Toc361659238}[]{#_Toc361659825}[]{#_Toc361660412}[]{#_Toc361663985}[]{#_Toc361747445}[]{#_Toc361819808}[]{#_Toc361659300}[]{#_Toc361659887}[]{#_Toc361660474}[]{#_Toc361664047}[]{#_Toc361747507}[]{#_Toc361819870}

**BGP \-- BGP配置命令 \-- ebgp-interface-sensitive**

------------------------------------------------------------------------

[**[ebgp-interface-sensitive]{lang="EN-US"}**]{#struct_0_65458_x3406_x1961091900}[命令用来[]{#_Toc297795790}[使能直连]{#_Ref280280493}]{style="font-family:
宋体"}[EBGP]{lang="EN-US"}[会话快速复位功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ebgp-interface-sensitive**]{lang="EN-US"}]{#struct_0_65458_x3406_x174118060}[命令用来关闭直连]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话快速复位功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x125280994}

[**[ebgp-interface-sensitive]{lang="EN-US"}**]{#struct_0_65458_x3406_691929261}

[**[undo ebgp]{lang="EN-US"}**[-**interface-sensitive**]{lang="EN-US"}]{#struct_0_65458_x3406_1702755881}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1698469225}

[[直连]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_848904871}[会话快速复位功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_837020708}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_315397601}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1832804295}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x703643218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1043954953}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_847921831}

[[如果使能了本功能，则连接直连]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x502027781}[对等体的链路]{style="font-family:宋体"}[down]{lang="EN-US"}[后，本地路由器会立即断开与]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体的会话，并重新与该对等体建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话。从而，实现快速发现链路故障，快速重建会话。]{style="font-family:宋体"}

[[如果没有使能本功能，则连接直连]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_784485958}[对等体的链路]{style="font-family:宋体"}[down]{lang="EN-US"}[后，本地路由器不会立即断开与]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体的会话，而是等待会话保持时间（]{style="font-family:宋体"}[Holdtime]{lang="EN-US"}[）超时后，才断开该会话。没有使能本功能时，链路震荡不会影响]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话的状态。]{style="font-family:宋体"}

[[需要注意的是，只有与直连的]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_1811039427}[对等体之间的会话支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1097124508}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x108514411}[使能直连]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话快速复位功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_847987367}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ebgp-interface-sensitive]{lang="EN-US"}
:::

::: {#16120724 .myid}
[]{#_Toc404788629}[]{#struct_0_65458_x3406_x192391001}[]{#_Toc366077082}[]{#_Toc352053201}[]{#_Toc351984310}

**BGP \-- BGP配置命令 \-- fast-reroute route-policy**

------------------------------------------------------------------------

[**[fast-reroute]{lang="EN-US"}**[ **route-policy**]{lang="EN-US"}]{#struct_0_65458_x3406_x192522073}[命令用来在当前]{style="font-family:宋体"}[BGP]{lang="EN-US"}[地址族视图下指定快速重路由引用的路由策略。]{style="font-family:宋体"}

[**[undo fast-reroute]{lang="EN-US"}**[ **route-policy**]{lang="EN-US"}]{#struct_0_65458_x3406_x192456537}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x192063321}

[**[fast-reroute route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_65458_x3406_1373430793}

[**[undo fast-reroute route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1373299721}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1373692937}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1373758473}[快速重路由未引用任何路由策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1373627401}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1374020617}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1373430792}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1373299720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1373692936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1373758472}

[*[route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1373627400}[：]{style="font-family:宋体"}[路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1374020616}

[[开启]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1373430791}[快速重路由功能的方法有如下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_65458_x3406_1373299719}[BGP]{lang="EN-US"}[地址族视图下执行]{style="font-family:宋体"}**[pic]{lang="EN-US"}**[命令开启当前地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由功能。采用这种方法时，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会为当前地址族的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由自动计算备份下一跳，即只要从不同]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体学习到了到达同一目的网络的路由，且这些路由不等价，就会生成主备两条路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1373692935}[地址族视图下执行]{lang="EN-US" style="font-family:宋体"}**[fast-reroute route-policy]{lang="EN-US"}**[命令指定快速重路由引用的路由策略，并在引用的路由策略中，通过]{lang="EN-US" style="font-family:宋体"}**[apply ]{lang="EN-US"}**[\[ **ipv6** \] **fast-reroute backup-nexthop**]{lang="EN-US"}[命令指定备份下一跳的地址。采用这种方式时，只有为主路由计算出的备份下一跳地址与指定的地址相同时，才会为其生成备份下一跳；否则，不会为主路由生成备份下一跳。]{lang="EN-US" style="font-family:宋体"}[在引用的路由策略中，还可以配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[子句，用来决定哪些路由可以进行快速重路由保护，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[只会为通过]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[子句过滤的路由生成备份下一跳。]{style="font-family:宋体"}

[[引用路由策略方式的优先级高于通过]{style="font-family:宋体"}**[pic]{lang="EN-US"}**]{#struct_0_65458_x3406_1373561863}[命令开启]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1373627399}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1374020615}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由引用的路由策略为]{style="font-family:宋体"}[frr-policy]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1373496326}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] fast-reroute route-policy frr-policy]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1373299718}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply fast-reroute]{lang="EN-US"}**]{#struct_0_65458_x3406_1373692934}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply ]{lang="EN-US"}**]{#struct_0_65458_x3406_1373561862}**[ipv6 ]{lang="EN-US"}[fast-reroute]{lang="EN-US"}**[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pic]{lang="EN-US"}**]{#struct_0_65458_x3406_1373627398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1374020614}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1247311243 .myid}
[]{#_Toc404788630}[]{#struct_0_65458_x3406_x133577674}[]{#_Toc316655938}[]{#_Toc312414456}[]{#_Toc312402334}[]{#_Toc180224193}

**BGP \-- BGP配置命令 \-- filter-policy export**

------------------------------------------------------------------------

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_65458_x3406_2092860582}[命令用来配置对发布的路由信息进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy export]{lang="EN-US"}**]{#struct_0_65458_x3406_846678828}[命令用来取消对发布的路由信息进行过滤。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x868890510}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_2102075847}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[filter-policy]{lang="EN-US"}**[ { *acl-number* \| **prefix-list** *prefix-list-name* } **export** \[ *protocol process-id* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1268425100}

[**[undo filter-policy]{lang="EN-US"}**[ **export** \[ *protocol process-id* \]]{lang="EN-US"}]{#struct_0_65458_x3406_1401107037}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_848446120}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[filter-policy]{lang="EN-US"}**[ { *acl6-number* \| **prefix-list** *ipv6-prefix-name* } **export** \[ *protocol process-id* \]]{lang="EN-US"}]{#struct_0_65458_x3406_311625010}

[**[undo filter-policy]{lang="EN-US"}**[ **export** \[ *protocol process-id* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x618202015}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_568584389}

[[不对发布的路由信息进行过滤。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1352601501}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x301091523}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x510171877}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_306666875}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_848511656}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1664255402}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2124735441}

[*[acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_663865715}[：指定用于匹配路由信息目的网络地址的访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x95971175}[：指定用于匹配路由信息目的网络地址的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_65458_x3406_1511030286}[：指定用于匹配路由信息目的网络地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *ipv6-prefix-name*]{lang="EN-US"}]{#struct_0_65458_x3406_1427178780}[：指定用于匹配路由信息目的网络地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表。]{style="font-family:宋体"}*[ipv6-prefix-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_65458_x3406_848577192}[：对从指定]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由协议引入的路由进行过滤。在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图下，取值包括]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[；在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图下，取值包括]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_65458_x3406_1907099025}[：路由协议的进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图下，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[取值为]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[时，可以指定该参数]{style="font-family:宋体"}[;]{lang="EN-US"}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图下，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[取值为]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[时，可以指定该参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_137248095}

[[如果指定了路由协议参数（]{style="font-family:宋体"}**[direct]{lang="EN-US"}**]{#struct_0_65458_x3406_615658622}[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[等]{style="font-family:宋体"}[），则只对从这种协议引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的路由进行过滤，其他]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由不受影响。如果没有指定路由协议参数，则对所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由都进行过滤，包括从]{style="font-family:宋体"}[IGP]{lang="EN-US"}[引入的路由、使用]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令发布的路由、从]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体学习的路由等。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1955875619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过基本]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2109154047}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[）对发布的路由信息进行过滤时，如果配置了]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **source** *source-address* *source-wildcard*]{lang="EN-US"}[命令，则只要路由的目的网络地址与]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}*[source-address source-wildcard]{lang="EN-US"}*[匹配，则该路由与]{style="font-family:
宋体"}**[rule]{lang="EN-US"}**[命令配置的规则匹配，不会再比较路由的目的网络地址掩码。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_65458_x3406_x808178357}[（]{lang="EN-US" style="font-family:宋体"}[3000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[）对发布的路由信息进行过滤时，]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[命令配置的规则用]{lang="EN-US" style="font-family:宋体"}[来过滤指定目的网络地址的路由；]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[命令配置的规则用]{lang="EN-US" style="font-family:宋体"}[来过滤指定目的网络地址和掩码的路由，其中]{lang="EN-US" style="font-family:宋体"}**[source ]{lang="EN-US"}***[sour-addr sour-wildcard]{lang="EN-US"}*[用来过滤路由目的网络地址，]{lang="EN-US" style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[用来过滤路由掩码。]{lang="EN-US" style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[指定的掩码应该是连续的。如果指定的掩码不连续，则该过滤掩码的条件不生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_848642728}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1796739488}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布的所有路由进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1970512519}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 ]{lang="EN-US"}[unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] filter-policy 2000 export]{lang="EN-US"}

[]{#struct_0_65458_x3406_1558264464}[]{#_Toc26173947}[]{#_Toc138238265}[]{#_Toc32467743}[]{#_Toc32464212}[]{#_Toc30500456}[\# ]{lang="EN-US"}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1977527576}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 ]{lang="EN-US"}[unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] filter-policy 2000 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1683136869}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对发布的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由进行过滤，只允许发布]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[一条路由。]{style="font-family:宋体"}

[]{#struct_0_65458_x3406_848708264}[]{#_Toc310604592}[]{#_Toc261504210}[]{#_Toc180224194}[]{#_Toc228610424}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] filter-policy 3000 export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_980395977}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy ]{lang="EN-US"}**]{#struct_0_65458_x3406_2127256657}**[import]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer as-path-acl]{lang="EN-US"}**]{#struct_0_65458_x3406_x1775223324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1110342315}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x272495298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_848773800}
:::

::: {#632247711 .myid}
[]{#_Toc404788631}[]{#struct_0_65458_x3406_x1345852384}[]{#_Toc316655939}[]{#_Toc312414457}[]{#_Toc312402335}

**BGP \-- BGP配置命令 \-- filter-policy import**

------------------------------------------------------------------------

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_65458_x3406_1304200969}[命令用来配置对接收的路由信息进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_65458_x3406_446440494}[命令用来取消对接收的路由信息进行过滤。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1989415357}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1009533456}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[filter-policy ]{lang="EN-US"}**[{ *acl-number* \| **prefix-list** *prefix-list-name* } **import**]{lang="EN-US"}]{#struct_0_65458_x3406_1565774979}

[**[undo filter-policy]{lang="EN-US"}**[ **import**]{lang="EN-US"}]{#struct_0_65458_x3406_848839336}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1961091901}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[filter-policy ]{lang="EN-US"}**[{ *acl6-number* \| **prefix-list** *ipv6-prefix-name* } **import**]{lang="EN-US"}]{#struct_0_65458_x3406_x1740202001}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_65458_x3406_1014318855}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_118729245}

[[不对接收的路由信息进行过滤。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1436257921}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2081638518}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_848904872}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_837020705}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_315397590}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_693687393}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_805072188}

[*[acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_223136244}[：指定用于匹配路由信息目的网络地址的访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_65458_x3406_1508110633}[：指定用于匹配路由信息目的网络地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[访问列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x792583221}[：指定用于匹配路由信息目的网络地址的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[ipv]{lang="EN-US"}[6-prefix-name]{lang="EN-US"}*]{#struct_0_65458_x3406_847921832}[：指定用于匹配路由信息目的网络地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表。]{style="font-family:宋体"}*[ipv]{lang="EN-US"}[6-prefix-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x502027780}

[[通过基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_65458_x3406_784420422}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[）对接收的路由信息进行过滤时，如果配置了]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **source** *source-address* *source-wildcard*]{lang="EN-US"}[命令，则只要路由的目的网络地址与]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}*[source-address source-wildcard]{lang="EN-US"}*[匹配，则该路由与]{style="font-family:
宋体"}**[rule]{lang="EN-US"}**[命令配置的规则匹配，不会再比较路由的目的网络地址掩码。]{style="font-family:
宋体"}

[[通过高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_65458_x3406_1511085988}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）对接收的路由信息进行过滤时，]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[命令配置的规则用]{style="font-family:宋体"}[来过滤指定目的网络地址的路由；]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[命令配置的规则用]{style="font-family:宋体"}[来过滤指定目的网络地址和掩码的路由，其中]{style="font-family:宋体"}**[source ]{lang="EN-US"}***[sour-addr sour-wildcard]{lang="EN-US"}*[用来过滤路由目的网络地址，]{style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[用来过滤路由掩码。]{style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[指定的掩码应该是连续的。如果指定的掩码不连续，则该过滤掩码的条件不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1046831853}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_886355820}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[接收的路由进行过滤。]{style="font-family:宋体"}

[]{#_Toc138238266}[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_847987368}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] filter-policy 2000 import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x133577685}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[接收的路由进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_2092795051}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] filter-policy 2000 import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1137006111}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由进行过滤，只允许接收]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[一条路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1880437232}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[[\[Sysname-bgp-ipv4\] filter-policy 3000 import]{lang="EN-US"}]{#_Toc312402336}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_400873172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy export]{lang="EN-US"}**]{#struct_0_65458_x3406_476218341}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer as-path-acl]{lang="EN-US"}**]{#struct_0_65458_x3406_1378524217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1395915055}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_955485571}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x2095973222}
:::

::: {#63544256 .myid}
[]{#_Toc404788632}[]{#struct_0_65458_x3406_x2068396455}

**BGP \-- BGP配置命令 \-- graceful-restart**

------------------------------------------------------------------------

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880371696}[命令用来使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[graceful-restart]{lang="EN-US"}**]{#struct_0_65458_x3406_x60344888}[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1089497535}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_65458_x3406_1264693175}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_65458_x3406_916762964}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1211973873}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_267560496}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x742655175}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1880306160}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2087459926}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_854211386}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1306138392}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x386019820}

[[BGP GR]{lang="EN-US"}]{#struct_0_65458_x3406_x998435893}[（]{style="font-family:宋体"}[Graceful Restart]{lang="EN-US"}[，平滑重启）是一种在主备倒换或]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议重启时保证转发业务不中断的机制。]{style="font-family:宋体"}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1837073405}[对等体之间通过]{style="font-family:宋体"}[Open]{lang="EN-US"}[消息交互]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。只有双方都具有]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力时，建立起的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话才具备]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[需要注意的是，执行本命令后，设备会重新建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1880240624}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1626504013}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1516789967}[使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x520669958}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] graceful-restart]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1711138031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer purge-time]{lang="EN-US"}**]{#struct_0_65458_x3406_1728118294}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer restart]{lang="EN-US"}**]{#struct_0_65458_x3406_x1333228307}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer wait-for-rib]{lang="EN-US"}**]{#struct_0_65458_x3406_x287628467}
:::

::: {#-1876149571 .myid}
[]{#_Toc404788633}[]{#struct_0_65458_x3406_x1000765061}

**BGP \-- BGP配置命令 \-- graceful-restart timer purge-time**

------------------------------------------------------------------------

[**[graceful-restart timer purge-time]{lang="EN-US"}**]{#struct_0_65458_x3406_1293367562}[命令用来配置]{style="font-family:宋体"}[BGP GR]{lang="EN-US"}[过程中等待通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Routing Information Base]{lang="EN-US"}[，路由信息库）老化失效表项的时间。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[graceful-restart timer purge-time]{lang="EN-US"}**]{#struct_0_65458_x3406_1077267817}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_565318880}

[**[graceful-restart timer purge-time ]{lang="EN-US"}***[timer]{lang="EN-US"}*]{#struct_0_65458_x3406_x376129339}

[**[undo ]{lang="EN-US"}[graceful-restart timer purge-time]{lang="EN-US"}**]{#struct_0_65458_x3406_x5511032}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1346024952}

[[BGP GR]{lang="EN-US"}]{#struct_0_65458_x3406_2131402821}[过程中等待通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}[老化失效表项的时间为]{style="font-family:宋体"}[480]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_683930198}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x377978272}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x241250174}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1476530341}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1150864288}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1834124805}

[*[timer]{lang="EN-US"}*]{#struct_0_65458_x3406_1324833767}[：]{style="font-family:宋体"}[BGP GR]{lang="EN-US"}[过程中等待通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}[老化失效表项的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1662095535}

[[GR Restarter]{lang="EN-US"}]{#struct_0_65458_x3406_763206357}[发生主备倒换或]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议重启时，会启动]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由老化定时器，该定时器的值由本命令来配置。如果在]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由老化定时器超时时没有完成]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的交互，则]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[会强制退出]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程，根据已经学习到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息更新]{style="font-family:宋体"}[RIB]{lang="EN-US"}[表项，删除老化的]{style="font-family:宋体"}[RIB]{lang="EN-US"}[表项。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_333475890}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先使能]{style="font-family:宋体"}]{#struct_0_65458_x3406_x597546070}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1281298240}[路由数量较多时，如果本命令配置的值过小，在]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由老化定时器超时前]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[和]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[无法完成路由交互，则可能会导致流量中断。请根据实际情况，合理调整]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由老化定时器的值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置的值建议大于]{style="font-family:宋体"}**[graceful-restart timer wait-for-rib]{lang="EN-US"}**]{#struct_0_65458_x3406_x1638149408}[命令]{lang="EN-US" style="font-family:宋体"}[配置的值，小于]{style="font-family:宋体"}**[protocol lifetime]{lang="EN-US"}**[命令配置的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_968537871}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1364259011}[配置]{style="font-family:宋体"}[BGP GR]{lang="EN-US"}[过程中等待通知]{style="font-family:宋体"}[RIB]{lang="EN-US"}[老化失效表项的时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1165501392}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] graceful-restart]{lang="EN-US"}

[\[Sysname-bgp\] graceful-restart timer purge-time 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1760345484}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_65458_x3406_2057761659}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer restart]{lang="EN-US"}**]{#struct_0_65458_x3406_x2107202599}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer wait-for-rib]{lang="EN-US"}**]{#struct_0_65458_x3406_x1171210047}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[protocol lifetime]{lang="EN-US"}**]{#struct_0_65458_x3406_x194261543}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{style="font-family:宋体"}
:::

::: {#128483534 .myid}
[]{#_Toc404788634}[]{#struct_0_65458_x3406_x1880175088}

**BGP \-- BGP配置命令 \-- graceful-restart timer restart**

------------------------------------------------------------------------

[**[graceful-restart timer restart]{lang="EN-US"}**]{#struct_0_65458_x3406_1633754880}[命令用来配置对端等待重建]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[会话的时间。]{style="font-family:
宋体"}

[**[undo ]{lang="EN-US"}[graceful-restart timer restart]{lang="EN-US"}**]{#struct_0_65458_x3406_1546404437}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1931702504}

[**[graceful-restart timer restart ]{lang="EN-US"}***[timer]{lang="EN-US"}*]{#struct_0_65458_x3406_x394396176}

[**[undo ]{lang="EN-US"}[graceful-restart timer restart]{lang="EN-US"}**]{#struct_0_65458_x3406_x1614672127}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1597567938}

[[对端等待重建]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1880109552}[会话的时间为]{style="font-family:宋体"}[150]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1237648776}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1217414742}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x902183588}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1130136516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x83714486}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1757220766}

[*[timer]{lang="EN-US"}*]{#struct_0_65458_x3406_1948329300}[：对端等待重建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的最大时间，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880044016}

[[GR Restarter]{lang="EN-US"}]{#struct_0_65458_x3406_x974494587}[通过]{style="font-family:宋体"}[Open]{lang="EN-US"}[消息将本端配置的对端等待重建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的最大时间通告给]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[。]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[发现]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[进行主备倒换或]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议重启后，保留从该]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[学习到的路由，并对这些路由进行失效标记。]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[等待]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[与其重建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。如果在]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[通告的时间内，没有重建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，则删除标记为失效的路由。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1886377203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先使能]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1012935322}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令后，配置的时间不会立即生效，只有重建]{style="font-family:宋体"}]{#struct_0_65458_x3406_226207209}[BGP]{lang="EN-US"}[会话后才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x109891462}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x924096897}[配置对端等待重建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的最大时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1879978480}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] graceful-restart]{lang="EN-US"}

[\[Sysname-bgp\] graceful-restart timer restart 300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_62976008}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_65458_x3406_1727678469}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer purge-time]{lang="EN-US"}**]{#struct_0_65458_x3406_x1000830597}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer wait-for-rib]{lang="EN-US"}**]{#struct_0_65458_x3406_x304686993}
:::

::: {#325012220 .myid}
[]{#_Toc404788635}[]{#struct_0_65458_x3406_1592580833}

**BGP \-- BGP配置命令 \-- graceful-restart timer wait-for-rib**

------------------------------------------------------------------------

[**[graceful-restart timer wait-for-rib]{lang="EN-US"}**]{#struct_0_65458_x3406_1532254218}[命令用来配置本端等待]{style="font-family:宋体"}[End-Of-RIB]{lang="EN-US"}[标记的时间。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[graceful-restart timer wait-for-rib]{lang="EN-US"}**]{#struct_0_65458_x3406_x1692777743}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880961520}

[**[graceful-restart timer wait-for-rib]{lang="EN-US"}***[ timer]{lang="EN-US"}*]{#struct_0_65458_x3406_846277704}

[**[undo ]{lang="EN-US"}[graceful-restart timer wait-for-rib]{lang="EN-US"}**]{#struct_0_65458_x3406_515546507}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_536661391}

[[本端等待]{style="font-family:宋体"}[End-Of-RIB]{lang="EN-US"}]{#struct_0_65458_x3406_x540892834}[标记的时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x24368994}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1004393721}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880895984}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1778576197}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x2105348084}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1694000793}

[*[timer]{lang="EN-US"}*]{#struct_0_65458_x3406_x1880437231}[：本端等待]{style="font-family:宋体"}[End-Of-RIB]{lang="EN-US"}[标记的时间，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1966957113}

[[GR Restarter]{lang="EN-US"}]{#struct_0_65458_x3406_x341867805}[主备倒换或]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议重启完成，并与]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[重新建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话后，]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[和]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[应在本命令指定的时间内收到]{style="font-family:宋体"}[End-Of-RIB]{lang="EN-US"}[标记，即在本命令指定的时间内完成路由信息的交互。]{style="font-family:宋体"}

[[通过本命令可以控制路由收敛的速度。本命令配置的值越小，路由收敛速度越快，但可能会导致接收的路由信息不完整。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1332136651}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1164432437}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置本命令之前，必须先使能]{style="font-family:宋体"}]{#struct_0_65458_x3406_x857623039}[BGP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本端配置的等待]{lang="EN-US" style="font-family:宋体"}[End-Of-RIB]{lang="EN-US"}]{#struct_0_65458_x3406_x1618897673}[标记的时间不会通告给对端，只用来控制本端路由信息交互的时间，即]{lang="EN-US" style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[上配置的时间只用来控制]{lang="EN-US" style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[从]{lang="EN-US" style="font-family:宋体"}[GR Helper]{lang="EN-US"}[接收路由更新的时间，]{lang="EN-US" style="font-family:宋体"}[GR Helper]{lang="EN-US"}[上配置的时间只用来控制]{lang="EN-US" style="font-family:宋体"}[GR Helper]{lang="EN-US"}[从]{lang="EN-US" style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[接收路由更新的时间。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880371695}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1505739053}[配置本端等待]{style="font-family:宋体"}[End-Of-RIB]{lang="EN-US"}[标记的时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x933217034}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] graceful-restart]{lang="EN-US"}

[\[Sysname-bgp\] graceful-restart timer wait-for-rib 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2075753443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_65458_x3406_1905722345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer purge-time]{lang="EN-US"}**]{#struct_0_65458_x3406_x241315710}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart timer ]{lang="EN-US"}**]{#struct_0_65458_x3406_x2055194025}**[restart]{lang="EN-US"}**
:::

::: {#-1172193874 .myid}
[]{#_Toc404788636}[]{#struct_0_65458_x3406_x1001833829}

**BGP \-- BGP配置命令 \-- group**

------------------------------------------------------------------------

[**[group]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880306159}[命令用来创建一个对等体组。]{style="font-family:宋体"}

[**[undo group]{lang="EN-US"}**]{#struct_0_65458_x3406_x997588253}[命令用来删除指定的对等体组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_169443635}

[**[group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*[ \[ **external** \| **internal** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x2047393445}

[**[undo group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_65458_x3406_x1996705932}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_965295337}

[[设备上不存在任何对等体组。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1129585099}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880240623}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_2029788540}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1406743524}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_822528492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1570014399}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x872929574}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x840439444}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_65458_x3406_1708075717}[：创建]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880175087}[：创建]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1095128475}

[[在大规模]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1820585043}[网络中，对等体的数量很多，其中很多对等体具有相同的策略，在配置时会重复使用一些命令。此时，利用对等体组可以简化配置。]{style="font-family:宋体"}

[[对等体组是具有某些相同属性的对等体的集合。当一个对等体加入对等体组中时，此对等体将获得与所在对等体组相同的配置。当对等体组的配置改变时，组内成员的配置也相应改变。]{style="font-family:宋体"}]{#struct_0_65458_x3406_88069480}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_226605525}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[group]{lang="EN-US"}**]{#struct_0_65458_x3406_400395863}[命令时，如果没有指定]{lang="EN-US" style="font-family:宋体"}**[internal]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[external]{lang="EN-US"}**[参数，则创建的是]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果分别对对等体组和对等体组中的对等体进行了某项]{style="font-family:宋体"}]{#struct_0_65458_x3406_1235268215}[BGP]{lang="EN-US"}[配置，则以最后一次配置为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令创建对等体组后，还需要执行]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1908032972}**[peer enable]{lang="EN-US"}**[命令，本地路由器才具有与指定对等体组交换相应地址族路由信息的能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880109551}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1640933303}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，创建一个]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[，其]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并在]{style="font-family:宋体"}[test]{lang="EN-US"}[中添加]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[和]{style="font-family:宋体"}[10.1.2.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1986579987}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] group test external]{lang="EN-US"}

[\[Sysname-bgp\] peer test as-number 200]{lang="EN-US"}

[\[Sysname-bgp\] peer 10.1.1.1 group test]{lang="EN-US"}

[\[Sysname-bgp\] peer 10.1.2.1 group test]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1984120474}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，创建一个]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[，其]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并在]{style="font-family:宋体"}[test]{lang="EN-US"}[中添加]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[和]{style="font-family:宋体"}[10.1.2.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1880044015}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] group test external]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test as-number 200]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 10.1.1.1 group test]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 10.1.2.1 group test]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x571210060}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，创建一个]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[，其]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并在]{style="font-family:宋体"}[test]{lang="EN-US"}[中添加]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[和]{style="font-family:宋体"}[1::2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_193921494}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] group test external]{lang="EN-US"}

[\[Sysname-bgp\] peer test as-number 200]{lang="EN-US"}

[\[Sysname-bgp\] peer 1::1 group test]{lang="EN-US"}

[\[Sysname-bgp\] peer 1::2 group test]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x186629387}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，创建一个]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[，其]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[200]{lang="EN-US"}[，并在]{style="font-family:宋体"}[test]{lang="EN-US"}[中添加]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[和]{style="font-family:宋体"}[1::2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1879978479}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] group test external]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test as-number 200]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 group test]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::2 group test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1985093701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp ]{lang="EN-US"}**]{#struct_0_65458_x3406_x287243561}**[group]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer enable]{lang="EN-US"}**]{#struct_0_65458_x3406_x642434512}
:::

::: {#1472413862 .myid}
[]{#_Toc404788637}[]{#struct_0_65458_x3406_x2019737886}[]{#_Toc263170123}[]{#_Toc261504215}

**BGP \-- BGP配置命令 \-- ignore-first-as**

------------------------------------------------------------------------

[**[ignore-first-as]{lang="EN-US"}**]{#struct_0_65458_x3406_2011485327}[命令用来配置不检测]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由的第一个]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[**[undo ignore-first-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x834316549}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880961519}

[**[ignore-first-as]{lang="EN-US"}**]{#struct_0_65458_x3406_2055934677}

[**[undo ignore-first-as]{lang="EN-US"}**]{#struct_0_65458_x3406_328680660}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_681072318}

[[系统收到]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x300250944}[路由后，会检测路由的第一个]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。如果此]{style="font-family:宋体"}[AS]{lang="EN-US"}[号不是]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，且不是私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则断开与该对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x86118212}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1268381195}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1835033446}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1880895983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1375291670}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x724844369}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1307562131}[配置不检测]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由的第一个]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x2057626963}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ignore-first-as]{lang="EN-US"}
:::

::: {#29262825 .myid}
[]{#_Toc404788638}[]{#struct_0_65458_x3406_2081972533}

**BGP \-- BGP配置命令 \-- import-route**

------------------------------------------------------------------------

[**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x1488420753}[命令用来将]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由协议的路由信息引入到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中，以便通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布引入的路由信息。]{style="font-family:宋体"}

[**[undo import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880437234}[命令用来取消引入]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由协议的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1207442226}

[**[import-route]{lang="EN-US"}**[ *protocol* \[ { *process-id* \| **all-processes** } \[ **allow-direct** \| **med** *med-value* \| **route-policy** *route-policy-name* \] \* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1880371698}

[**[undo import-route]{lang="EN-US"}**[ *protocol* \[ *process-id \|* **all-processes** \]]{lang="EN-US"}]{#struct_0_65458_x3406_1102454526}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1462848156}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x234859415}[不会引入]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由协议的路由信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x749857965}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1144730936}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_323985210}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1333392487}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1880240626}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1505663869}

[*[protocol]{lang="EN-US"}*]{#struct_0_65458_x3406_x1986417132}[：引入指定]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由协议的路由。在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图下，取值包括]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[；在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图下，取值包括]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_65458_x3406_481943698}[：路由协议的进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图下，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[取值为]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[时，可以指定该参数；在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图下，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[取值为]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[时，可以指定该参数。]{style="font-family:宋体"}

[**[all-processes]{lang="EN-US"}**]{#struct_0_65458_x3406_x501098028}[：引入指定路由协议所有进程的路由。在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图下，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[取值为]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[时，可以指定该参数；在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图下，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[取值为]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[时，可以指定该参数。]{style="font-family:宋体"}

[**[allow-direct]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880306161}[：指定引入]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由协议的路由时，同时引入使能了该协议的接口网段路由。如果不指定本参数，则在引入协议路由时不会引入使能了该协议的接口网段路由。当]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[与]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}[参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[配置失效。例如，当配置]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数引入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由时，在路由策略中不要配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[ **route-type**]{lang="EN-US"}[匹配条件，否则，]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数失效。]{style="font-family:宋体"}

[**[med ]{lang="EN-US"}***[med-value]{lang="EN-US"}*]{#struct_0_65458_x3406_x641423429}[：指定引入路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果没有指定]{style="font-family:宋体"}[MED]{lang="EN-US"}[度量值，则被引入路由的]{style="font-family:宋体"}[metric]{lang="EN-US"}[值将作为引入]{style="font-family:宋体"}[BGP]{lang="EN-US"}[之后路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_51879092}[：对引入的路由应用路由策略，以便过滤引入的路由或设置引入后路由的属性。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[表示路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_882652909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x740006258}[命令引入指定]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}[路由协议的路由时，不会引入该协议的缺省路由。只有同时执行]{lang="EN-US" style="font-family:宋体"}**[default-route imported]{lang="EN-US"}**[命令，才会引入该协议的缺省路由。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能引入路由表中状态为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}]{#struct_0_65458_x3406_x1880240625}[的路由。可以通过]{lang="EN-US" style="font-family:宋体"}**[display ip routing-table protocol]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[或]{style="font-family:宋体"}**[display ip]{lang="EN-US"}[v6]{lang="EN-US"}[ routing-table protocol]{lang="EN-US"}**[命令来查看路由的状态是否为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_x1102379342}[命令引入到]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中的路由的]{lang="EN-US" style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[属性为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2113541106}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_590917616}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，引入]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的路由，并指定引入后]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_746454007}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] import-route rip 1 med 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1136838230}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，引入]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的路由，并通过路由策略]{style="font-family:宋体"}[imprt]{lang="EN-US"}[对引入的路由进行过滤，不引入]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[网段的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1880175089}

[\[Sysname\] ip prefix-list imprt deny 1.1.1.0 24]{lang="EN-US"}

[\[Sysname\] ip prefix-list imprt permit 0.0.0.0 0 less-equal 32]{lang="EN-US"}

[\[Sysname\] route-policy imprt permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-imprt-0\] if-match ip address prefix-list imprt]{lang="EN-US"}

[\[Sysname-route-policy-imprt-0\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] import-route rip 1 route-policy imprt]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_67670939}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，引入]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1438998277}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] import-route ripng]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x686361207}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，引入]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1880109553}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] import-route ripng]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1491234579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip routing-table protocol]{lang="EN-US"}**]{#struct_0_65458_x3406_x1121342975}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_65458_x3406_x127988329}**[v6]{lang="EN-US"}[ routing-table protocol]{lang="EN-US"}**[（三层技术]{lang="EN-US" style="font-family:
宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:
宋体"}[/IP]{lang="EN-US"}[路由基础）]{lang="EN-US" style="font-family:
宋体"}
:::

::: {#-790613958 .myid}
[]{#_Toc404788639}[]{#struct_0_65458_x3406_x1831688557}[]{#_Toc292809914}[]{#_Toc289500158}

**BGP \-- BGP配置命令 \-- ip vpn-instance (BGP view)**

------------------------------------------------------------------------

[**[ip vpn-instance]{lang="EN-US"}**]{#struct_0_65458_x3406_937721612}[命令用来创建]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例，并进入]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图。]{style="font-family:宋体"}

[**[undo ip vpn-instance]{lang="EN-US"}**]{#struct_0_65458_x3406_x2004152719}[命令用来删除]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例，及该视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880044017}

[**[ip vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_591589354}

[**[undo ip vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1211340004}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1355583630}

[[设备上不存在任何]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x1355190414}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1390871880}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1300045038}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_295778796}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x644290502}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1879978481}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1629059949}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1083552426}[：]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2113939949}

[[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}]{#struct_0_65458_x3406_1956177378}[实例视图下配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体后，从该对等体学习到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由将被添加到指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的路由表中。]{style="font-family:宋体"}

[[通常在]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_65458_x3406_2080830648}[设备和]{style="font-family:宋体"}[MCE]{lang="EN-US"}[设备上执行本命令及]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下的命令，以实现将不同]{style="font-family:宋体"}[Site]{lang="EN-US"}[的路由学习到不同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，保证]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例之间路由隔离。]{style="font-family:宋体"}

[[需要注意的是，在执行本命令前，必须通过系统视图下的]{style="font-family:宋体"}**[ip vpn-instance]{lang="EN-US"}**]{#struct_0_65458_x3406_854878701}[命令创建]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，并通过]{style="font-family:宋体"}**[route-distinguisher]{lang="EN-US"}**[命令配置该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的路由标识符]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x983886251}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1880961521}[为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[创建]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例，并进入]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1882605651}

[\[Sysname\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn1\] route-distinguisher 100:1]{lang="EN-US"}

[\[Sysname-vpn-instance-vpn1\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1045190664}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[ip vpn-instance ]{lang="EN-US"}**[(system-view)]{lang="EN-US"}]{#struct_0_65458_x3406_x639550819}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/MPLS L3VPN]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}**[route-distinguisher]{lang="EN-US"}**]{#struct_0_65458_x3406_x526065038}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/MPLS L3VPN]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1110888516 .myid}
[]{#_Toc404788640}[]{#struct_0_65458_x3406_x103963995}

**BGP \-- BGP配置命令 \-- log-peer-change**

------------------------------------------------------------------------

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880895985}[命令用来全局使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[日志记录功能。]{style="font-family:宋体"}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_65458_x3406_212492256}[命令用来全局关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[日志记录功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x529658042}

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_65458_x3406_1221043829}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_65458_x3406_x2127326797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2131960511}

[[全局]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x2057173168}[日志记录功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_650358059}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1880437236}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1924725656}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2121804976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2142917618}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2094132996}

[[通过]{style="font-family:宋体"}**[log-peer-change]{lang="EN-US"}**]{#struct_0_65458_x3406_x806395236}[命令]{style="font-family:宋体"}[全局使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[日志记录功能，并执行]{style="font-family:宋体"}**[peer log-change]{lang="EN-US"}**[命令使能与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能后，与该对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话建立以及断开时会生成日志信息，通过]{style="font-family:宋体"}**[display bgp peer ipv4 unicast log-info]{lang="EN-US"}**[命令或]{style="font-family:宋体"}**[display bgp peer ipv6 unicast log-info]{lang="EN-US"}**[命令可以查看记录的日志信息]{style="font-family:宋体"}[。生成的日志信息还将被发送到设备的信息中心，通过设置信息中心的参数，决定日志信息的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）]{style="font-family:宋体"}

[[如果全局关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1918711819}[日志记录功能，或关闭与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能，则]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话建立或断开时不会生成日志信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880371700}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_746813989}[全局使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[日志记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x674756109}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] log-peer-change]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1557118531}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1467561526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer log-change]{lang="EN-US"}**]{#struct_0_65458_x3406_x194392615}
:::

::: {#-815886662 .myid}
[]{#_Toc404788641}[]{#struct_0_65458_x3406_1170151330}[]{#_Toc263170127}[]{#_Toc261504219}[]{#_Toc180224202}[]{#_Toc138238269}

**BGP \-- BGP配置命令 \-- network**

------------------------------------------------------------------------

[**[network]{lang="EN-US"}**]{#struct_0_65458_x3406_x1085816756}[命令用来将本地路由表中指定网段的路由添加到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中，以便通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布该网段路由。]{style="font-family:宋体"}

[**[undo network]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880306164}[命令用来取消已有的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x238138902}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1666549480}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**[ *ip-address* \[ *mask* \| *mask-length* \] \[ **route-policy** *route-policy-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_2128683763}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[network ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}*[\[ *mask \| mask-length* \]]{lang="EN-US"}]{#struct_0_65458_x3406_1134855540}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1164194544}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**[ *ipv6-address* *prefix-length* \[ **route-policy** *route-policy-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x2131122179}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[network ]{lang="EN-US"}***[ipv6-address ]{lang="EN-US"}[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x545214423}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880240628}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x342864455}[不发布任何本地的网段路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_14499681}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1318070038}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1589745137}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1739677197}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_70825744}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880175092}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1854708898}[：目的网络的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[和]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[参数，则采用自然掩码。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_2018372870}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1783492920}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_901296613}[：目的网络的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_216665419}[：目的网络地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x443541006}[：为指定网段的路由应用路由策略，通过路由策略设置路由属性或过滤路由。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[表示路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果没有指定本参数，则表示没有为指定网段的路由应用路由策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1901099574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880109556}[命令指定的网段路由必须存在于本地的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[路由表中，且处于]{style="font-family:
宋体"}[Active]{lang="EN-US"}[状态，否则无法将该网段路由添加到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[network]{lang="EN-US"}**]{#struct_0_65458_x3406_x1087950052}[命令添加到]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中的网段路由的]{lang="EN-US" style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[属性为]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_65458_x3406_x420936665}**[undo network]{lang="EN-US"}**[命令时指定的掩码、掩码长度或前缀长度必须与执行]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令时指定的掩码、掩码长度或前缀长度相同，否则无法删除配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_865343617}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x711294320}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，将本地路由表中到达]{style="font-family:宋体"}[10.0.0.0/16]{lang="EN-US"}[网段的路由添加到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1284744292}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] network 10.0.0.0 255.255.0.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1880044020}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，将本地路由表中到达]{style="font-family:宋体"}[10.0.0.0/16]{lang="EN-US"}[网段的路由添加到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x168122141}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] network 10.0.0.0 255.255.0.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x989918733}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，将本地路由表中到达]{style="font-family:宋体"}[2002::/64]{lang="EN-US"}[网段的路由添加到]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1404739702}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] network 2002:: 64]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1209285884}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，将本地路由表中到达]{style="font-family:宋体"}[2002::/64]{lang="EN-US"}[网段的路由添加到]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1879978484}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] network 2002:: 64]{lang="EN-US"}
:::

::: {#-80514935 .myid}
[]{#_Toc404788642}[]{#struct_0_65458_x3406_x1906392460}[]{#_Toc263170128}[]{#_Toc261504220}

**BGP \-- BGP配置命令 \-- network short-cut**

------------------------------------------------------------------------

[**[network short-cut]{lang="EN-US"}**]{#struct_0_65458_x3406_1051309961}[命令用来提高接收到的指定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由的路由优先级，该]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由称为]{style="font-family:宋体"}[Short-cut]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[undo network short-cut]{lang="EN-US"}**]{#struct_0_65458_x3406_x967879313}[命令用来取消提高接收到的指定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由的路由优先级。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_131854730}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x2091812579}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**[ *ip-address* \[ *mask* \| *mask-length* \] **short-cut**]{lang="EN-US"}]{#struct_0_65458_x3406_4843067}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[network ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}*[\[ *mask \| mask-length* \] **short-cut**]{lang="EN-US"}]{#struct_0_65458_x3406_1853221999}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1880961524}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**[ *ipv6-address prefix-length* **short-cut**]{lang="EN-US"}]{#struct_0_65458_x3406_x1479321124}

[**[undo ]{lang="EN-US"}[network]{lang="EN-US"}**[ *ipv6-address prefix-length* **short-cut**]{lang="EN-US"}]{#struct_0_65458_x3406_181859190}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x477851673}

[[接收到的]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_1639288421}[路由的路由优先级为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1801304626}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1617561989}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880895988}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_165438089}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1248582358}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1847244594}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1713275821}[：目的网络的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[和]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[参数，则采用自然掩码。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_581245347}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1157011161}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_792440956}[：目的网络的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1880437235}[：目的网络地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x358641715}

[[对于相同的目的地，不同的路由协议、直连路由和静态路由可能会发现不同的路由，但这些路由并不都是最优的。为了判断最优路由，各路由协议、直连路由和静态路由都被赋予了一个优先级，具有较高优先级的路由协议发现的路由将成为最优路由。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x286032337}

[[缺省情况下，]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x65185071}[路由的优先级低于本地产生的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的优先级。设备上存在到达某一目的网络的]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由和本地产生的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由时，不会选择]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由。通过执行]{style="font-family:宋体"}**[network shortcut]{lang="EN-US"}**[命令]{style="font-family:宋体"}[，可以使得指定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由的优先级与本地产生的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的优先级相同，从而提高该]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由成为最佳路由的可能性。]{style="font-family:宋体"}

[[用户可以通过]{style="font-family:宋体"}**[preference]{lang="EN-US"}**]{#struct_0_65458_x3406_2131292941}[命令修改]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由和本地产生的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1678511734}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1512414240}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置提高]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由]{style="font-family:宋体"}[10.0.0.0/16]{lang="EN-US"}[的路由优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1880371699}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] network 10.0.0.0 255.255.0.0 short-cut]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x463629415}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置提高]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由]{style="font-family:宋体"}[10::/16]{lang="EN-US"}[的路由优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1788415672}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] network 10:: 16 short-cut]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1257109151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[preference]{lang="EN-US"}**]{#struct_0_65458_x3406_1849923235}
:::

::: {#-1554088180 .myid}
[]{#_Toc404788643}[]{#struct_0_65458_x3406_566730666}[]{#_Toc366077095}[]{#_Toc345571279}

**BGP \-- BGP配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_65458_x3406_567123882}[命令用来开启]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_65458_x3406_566992810}[命令用来关闭]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_567386026}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_65458_x3406_567451562}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_65458_x3406_566927273}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_566796201}

[[BGP NSR]{lang="EN-US"}]{#struct_0_65458_x3406_567189417}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_567058345}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_567386025}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_566861736}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_566730664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_567123880}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_566992808}

[[BGP NSR]{lang="EN-US"}]{#struct_0_65458_x3406_567058344}[（]{style="font-family:宋体"}[Nonstop Routing]{lang="EN-US"}[，不间断路由）是一种通过在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议主备进程之间备份必要的协议状态和数据（如]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居信息和路由信息），使得]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议的主进程中断时，备份进程能够无缝地接管主进程的工作，从而确保对等体感知不到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议中断，保持]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由，并保证转发不会中断的技术。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_567451560}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_566927279}[开启]{style="font-family:宋体"}[BGP NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_566796207}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] non-stop-routing]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_567189423}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp non-stop-routing]{lang="EN-US"}**]{#struct_0_65458_x3406_566992815}**[ status]{lang="EN-US"}**
:::

::: {#1523894421 .myid}
[]{#_Toc404788644}[]{#struct_0_65458_x3406_x779891181}

**BGP \-- BGP配置命令 \-- peer advertise-community**

------------------------------------------------------------------------

[**[peer advertise-community]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880306163}[命令用来配置向对等体]{style="font-family:
宋体"}[/]{lang="EN-US"}[对等体组发布团体属性。]{style="font-family:宋体"}

[**[undo peer advertise-community]{lang="EN-US"}**]{#struct_0_65458_x3406_521375985}[命令用来取消向对等体]{style="font-family:
宋体"}[/]{lang="EN-US"}[对等体组发布团体属性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2050893058}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_578337212}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **advertise-community**]{lang="EN-US"}]{#struct_0_65458_x3406_x1097171624}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **advertise-community**]{lang="EN-US"}]{#struct_0_65458_x3406_x691621935}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1370599882}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **advertise-community**]{lang="EN-US"}]{#struct_0_65458_x3406_x1880240627}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **advertise-community**]{lang="EN-US"}]{#struct_0_65458_x3406_60420072}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_566927278}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **advertise-community**]{lang="EN-US"}]{#struct_0_65458_x3406_566730670}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **advertise-community**]{lang="EN-US"}]{#struct_0_65458_x3406_567123886}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1621955539}

[[不向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_1867751145}[对等体组发布团体属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1078642698}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1320623618}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1560580462}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1880175091}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x288624957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_875501467}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x308450254}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_123662693}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x980317851}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_784477088}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x980186779}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1616107133}

[[团体属性是跟随路由一起发送出去的一组特殊数据。根据需要，一条路由可以携带一个或多个团体属性值（每个团体属性值用一个四字节的整数表示）。接收到该路由的路由器就可以根据团体属性值对路由作出适当的处理（比如决定是否发布该路由、在什么范围发布等），从而能够简化路由策略的应用和降低维护管理的难度。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1660261083}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[peer advertise-community]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880109555}[命令后，本地路由器向对等体]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布的路由中将可以携带团体属性。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo peer advertise-community]{lang="EN-US"}**]{#struct_0_65458_x3406_x684665525}[命令后，如果接收到的路由中携带团体属性，则本地路由器删除该团体属性后，再将路由发布给对等体]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[对等体组。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1697156144}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x992067129}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置允许向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_340040158}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test advertise-community]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x826175361}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，配置允许向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1880044019}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer test advertise-community]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1754388768}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，配置允许向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1109538291}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer test advertise-community]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1301103045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply community]{lang="EN-US"}**]{#struct_0_65458_x3406_1452453684}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match community]{lang="EN-US"}**]{#struct_0_65458_x3406_203474628}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1879978483}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1604954082 .myid}
[]{#_Toc404788645}[]{#struct_0_65458_x3406_x1503107933}[]{#_Toc290298132}

**BGP \-- BGP配置命令 \-- peer advertise-ext-community**

------------------------------------------------------------------------

[**[peer advertise-ext-community]{lang="EN-US"}**]{#struct_0_65458_x3406_475746215}[命令用来配置向对等体]{style="font-family:
宋体"}[/]{lang="EN-US"}[对等体组发布扩展团体属性。]{style="font-family:宋体"}

[**[undo peer advertise-ext-community]{lang="EN-US"}**]{#struct_0_65458_x3406_1920608094}[命令用来取消向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布扩展团体属性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x185608067}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1532452778}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **advertise-ext-community**]{lang="EN-US"}]{#struct_0_65458_x3406_x1528535134}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **advertise-ext-community**]{lang="EN-US"}]{#struct_0_65458_x3406_x172228224}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1880961523}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **advertise-ext-community**]{lang="EN-US"}]{#struct_0_65458_x3406_1249562231}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **advertise-ext-community**]{lang="EN-US"}]{#struct_0_65458_x3406_147741180}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_2132814608}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **advertise-ext-community**]{lang="EN-US"}]{#struct_0_65458_x3406_2133207824}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \|  *ipv6-address* \[ *prefix-length* \] } **advertise-ext-community**]{lang="EN-US"}]{#struct_0_65458_x3406_2133076752}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_12894184}

[[不向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x1628388647}[对等体组发布扩展团体属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1681981446}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1424264308}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1880895987}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x950307158}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_896385520}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_314553700}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x760810318}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x79945272}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_586290373}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_962411760}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_585766086}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1227021613}

[[随着团体属性的应用日益广泛，原有四字节的团体属性无法满足用户的需求。因此，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x314353291}[定义了新的路由属性------扩展团体属性。扩展团体属性与团体属性有如下不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[扩展团体属性为八字节，提供了更多的属性值。]{style="font-family:宋体"}]{#struct_0_65458_x3406_964719732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[扩展团体属性可以划分类型。在不同的组网应用中，可以使用不同类型的扩展团体属性对路由进行过滤和控制。与不区分类型、统一使用同一个属性值空间的团体属性相比，扩展团体属性的配置和管理更为简单。]{style="font-family:宋体"}]{#struct_0_65458_x3406_845224633}

[[需要注意的是]{style="font-family:宋体"}]{#struct_0_65458_x3406_x585727171}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[peer advertise-ext-community]{lang="EN-US"}**]{#struct_0_65458_x3406_95527646}[命令后，本地路由器向对等体]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布的路由中将可以携带扩展团体属性。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[undo peer advertise-ext-community]{lang="EN-US"}**]{#struct_0_65458_x3406_1631601615}[命令后，如果接收到的路由中携带扩展团体属性，则本地路由器删除该扩展团体属性后，再将路由发布给对等体]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[对等体组。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2015404094}

[]{#_Toc263170131}[]{#_Toc261504223}[]{#_Toc180224205}[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_108972941}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置允许向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布扩展团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314287755}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test advertise-ext-community]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_2079475345}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，配置允许向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布扩展团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x277838121}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer test advertise-ext-community]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1336386003}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，配置允许向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布扩展团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314222219}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer test advertise-ext-community]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x607328060}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply extcommunity]{lang="EN-US"}**]{#struct_0_65458_x3406_974231026}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match extcommunity]{lang="EN-US"}**]{#struct_0_65458_x3406_x1103273470}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip extcommunity-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1748052596}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#155622973 .myid}
[]{#_Toc404788646}[]{#struct_0_65458_x3406_1513576158}[]{#_Toc290298134}

**BGP \-- BGP配置命令 \-- peer allow-as-loop**

------------------------------------------------------------------------

[**[peer allow-as-loop]{lang="EN-US"}**]{#struct_0_65458_x3406_145288626}[命令用来配置对于从对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由，允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号在接收路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中出现，并配置允许出现的次数。]{style="font-family:宋体"}

[**[undo peer allow-as-loop]{lang="EN-US"}**]{#struct_0_65458_x3406_1344628845}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314156683}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1806189752}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **allow-as-loop** \[ *number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_1211942620}

[**[undo peer ]{lang="EN-US"}**[{ *group-name \|* *ip-address* \[ *mask-length* \] } **allow-as-loop**]{lang="EN-US"}]{#struct_0_65458_x3406_x154002746}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_2077952107}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **allow-as-loop** \[ *number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_312807539}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **allow-as-loop**]{lang="EN-US"}]{#struct_0_65458_x3406_x1581134444}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1274019722}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **allow-as-loop** \[ *number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x314091147}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **allow-as-loop**]{lang="EN-US"}]{#struct_0_65458_x3406_529292570}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_697017459}

[[不允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x201528940}[号在接收路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中出现。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_883332639}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1861532202}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x370586676}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x314025611}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_916336521}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x180700929}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1687141105}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x728521794}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_585962691}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x442862118}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_586093763}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[number]{lang="EN-US"}*]{#struct_0_65458_x3406_51849371}[：允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号出现的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。如果本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号出现的次数大于此值，则认为出现环路，丢弃该路由。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x224017157}

[[缺省情况下，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x313960075}[不会接受]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中已包含本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号的路由，以避免形成路由环路。但是，在某些特殊的组网环境下（如]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[Hub&Spoke]{lang="EN-US"}[组网），需要允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号在接收路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中出现，否则无法正确发布路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1462424317}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x663018061}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置从对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[接收路由时，允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号在接收路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中出现，允许出现次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1127056507}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test allow-as-loop 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x894423802}[在]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族视图下，配置从对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[接收路由时，允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号在接收路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中出现，允许出现次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x313894539}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family vpnv4]{lang="EN-US"}

[\[Sysname-bgp-vpnv4\] peer test allow-as-loop 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x2107726450}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置从对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[接收路由时，允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号在接收路由的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中出现，允许出现次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_846763863}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer test allow-as-loop 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1599092674}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，配置从对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[接收]{style="font-family:宋体"}[BGP]{lang="EN-US"}[消息时，允许本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号在接收消息的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中出现，允许出现次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x153984350}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] peer test allow-as-loop 2]{lang="EN-US"}
:::

::: {#-2125588215 .myid}
[]{#_Toc404788647}[]{#struct_0_65458_x3406_266936447}

**BGP \-- BGP配置命令 \-- peer as-number (for a BGP peer group)**

------------------------------------------------------------------------

[**[peer as-number]{lang="EN-US"}**]{#struct_0_65458_x3406_x314877579}[命令用来指定对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[**[undo peer as-number]{lang="EN-US"}**]{#struct_0_65458_x3406_x1818802247}[命令用来删除对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1790328848}

[**[peer ]{lang="EN-US"}***[group-name]{lang="EN-US"}*[ **as-number** *as-number*]{lang="EN-US"}]{#struct_0_65458_x3406_x792052350}

[**[undo peer]{lang="EN-US"}**[ *group-name* **as-number**]{lang="EN-US"}]{#struct_0_65458_x3406_192822279}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1073734321}

[[没有指定对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x317342470}[号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_74508557}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x314812043}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x227808793}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1782425275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1518551565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1263828203}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1217810964}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x283201892}[：对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314353290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有当对等体组中不包含对等体时，才允许为对等体组配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_964785268}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为对等体组配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_2041870631}[AS]{lang="EN-US"}[号后，需要加入该对等体组的对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号必须与对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定对等体组的]{style="font-family:宋体"}]{#struct_0_65458_x3406_x723372464}[AS]{lang="EN-US"}[号，则加入该对等体组的对等体保留自己的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，即对等体组中对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号可以相同，也可以不同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1495984710}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1162226163}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，指定对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_202182578}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test as-number 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x314287754}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，指定对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_2079409809}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test as-number 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_540610455}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer group]{lang="EN-US"}**]{#struct_0_65458_x3406_1103226160}
:::

::: {#757380938 .myid}
[]{#_Toc404788648}[]{#struct_0_65458_x3406_x874967708}

**BGP \-- BGP配置命令 \-- peer as-number (for a BGP peer)**

------------------------------------------------------------------------

[**[peer as-number]{lang="EN-US"}**]{#struct_0_65458_x3406_116673003}[命令用来创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体，并指定对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[**[undo peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x799845522}[命令用来删除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314222218}

[**[peer ]{lang="EN-US"}**[{ *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **as-number** *as-number*]{lang="EN-US"}]{#struct_0_65458_x3406_x607393596}

[**[undo peer ]{lang="EN-US"}**[{ *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] }]{lang="EN-US"}]{#struct_0_65458_x3406_x941196164}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1552919261}

[[设备上不存在任何]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x116864015}[对等体。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x621304436}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_732573351}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1847625881}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x314156682}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1806124216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x36964677}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1213390121}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_586224836}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x690354870}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_585766089}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x607586232}[：对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号与本地路由器的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号相同，则该对等体为]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体；如果对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号与本地路由器的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号不同，则该对等体为]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1370675833}

[[除了本命令外，还可以通过]{style="font-family:宋体"}**[peer group]{lang="EN-US"}**]{#struct_0_65458_x3406_x314091146}[命令创建对等体。执行]{style="font-family:宋体"}**[peer group]{lang="EN-US"}**[命令创建对等体的同时，还可以将对等体加入对等体组。]{style="font-family:宋体"}

[[不能通过重复执行]{style="font-family:宋体"}**[peer as-number]{lang="EN-US"}**]{#struct_0_65458_x3406_529358106}[命令修改对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。只能先删除对等体，再为对等体配置新的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}]{#struct_0_65458_x3406_1472451445}[通过本命令创建对等体后，还需要执行]{style="font-family:宋体"}**[peer enable]{lang="EN-US"}**[命令，本地路由器才具有与指定对等体交换相应地址族路由信息的能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_701677540}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1909278891}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，指定对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x483997445}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 as-number 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1177509092}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，指定对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314025610}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 as-number 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_916270985}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x494255813}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer]{lang="EN-US"}**]{#struct_0_65458_x3406_870489946}**[ enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer group]{lang="EN-US"}**]{#struct_0_65458_x3406_x1081059341}
:::

::: {#146282354 .myid}
[]{#_Toc308164274}[]{#_Toc261504226}[]{#_Toc404788649}[]{#struct_0_65458_x3406_x2005507759}[]{#_Toc316655956}[]{#_Toc312414474}[]{#_Toc312402353}[]{#_Toc180224207}[]{#_Toc299201050}[]{#_Toc299632387}

**BGP \-- BGP配置命令 \-- peer as-path-acl**

------------------------------------------------------------------------

[**[peer as-path-acl]{lang="EN-US"}**]{#struct_0_65458_x3406_x313960074}[命令用来为对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组设置基于]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由过滤策略。]{style="font-family:宋体"}**[undo peer as-path-acl]{lang="EN-US"}**[命令用来取消已有的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1462358781}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_196652815}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **as-path-acl** *as-path-acl-number* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1686482510}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **as-path-acl** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_5868984}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1110829584}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **as-path-acl** *as-path-acl-number* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1052523549}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **as-path-acl** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1867258884}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_2133076750}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **as-path-acl** *as-path-acl-number* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_2133469966}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **as-path-acl** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_2132945677}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x313894538}

[[没有设置基于]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x2107660914}[路径过滤列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由过滤策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1806010812}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x769514519}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x628624497}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1353985846}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1412637465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314877578}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1818736711}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1631558756}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_586159306}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1243791082}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_586290378}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[as-path-acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_559051089}[：]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_65458_x3406_1282820100}[：对向指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布的路由应用过滤策略。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_65458_x3406_181827178}[：对从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由应用过滤策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1110479044}

[[配置]{style="font-family:宋体"}**[peer as-path-acl]{lang="EN-US"}**]{#struct_0_65458_x3406_x314812042}[命令时需要同时在系统视图下通过]{style="font-family:宋体"}**[ip as-path]{lang="EN-US"}**[命令配置对应的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表。如果本命令中指定的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表尚未创建，则所有路由均通过过滤。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x227743257}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x177643703}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置利用编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表过滤向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_523597660}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test as-path-acl 1 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1631918554}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，配置利用编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表过滤向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314353293}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer test as-path-acl 1 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_964588660}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，配置利用编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表过滤向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1714398915}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer test as-path-acl 1 export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1832757790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy export]{lang="EN-US"}**]{#struct_0_65458_x3406_x698239262}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy ]{lang="EN-US"}**]{#struct_0_65458_x3406_820907017}**[import]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip as-path]{lang="EN-US"}**]{#struct_0_65458_x3406_x846709386}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x314287757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_2079606417}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_525788267}
:::

::: {#1107524067 .myid}
[]{#_Toc404788650}[]{#struct_0_65458_x3406_x691787412}[]{#_Toc216757382}

**BGP \-- BGP配置命令 \-- peer bfd**

------------------------------------------------------------------------

[**[peer bfd]{lang="EN-US"}**]{#struct_0_65458_x3406_1314298593}[命令用来配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地路由器和指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体之间的链路。]{style="font-family:宋体"}

[**[undo peer bfd]{lang="EN-US"}**]{#struct_0_65458_x3406_84388406}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_319751727}[]{#_Toc216757383}

[**[peer ]{lang="EN-US"}**[{ *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **bfd**]{lang="EN-US"}]{#struct_0_65458_x3406_x1558395606}[]{#_Toc216757384}**[ ]{lang="EN-US"}**[\[ **multi-hop** \| **single-hop** \]]{lang="EN-US"}

[**[undo peer ]{lang="EN-US"}**[{ *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **bfd**]{lang="EN-US"}]{#struct_0_65458_x3406_x314222221}[]{#_Toc216757385}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x607852349}

[[不使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_65458_x3406_1031014571}[检测本地路由器和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体之间的链路。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_124273332}[]{#_Toc216757386}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x989606180}[视图]{style="font-family:宋体"}[]{#_Toc216757387}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[]{#struct_0_65458_x3406_x990957974}[]{#_Toc216757388}[]{#_Toc216757389}[【缺省用户角色】]{style="font-family:
黑体"}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1458136288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x314156685}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1805796536}[]{#_Toc216757390}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_2021065442}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_183005846}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x418002542}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}[]{#_Toc216757391}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182940310}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[multi-hop]{lang="EN-US"}**]{#struct_0_65458_x3406_x2009470849}[：采用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[多跳检测方式。]{style="font-family:宋体"}

[**[single-hop]{lang="EN-US"}**]{#struct_0_65458_x3406_181185908}[：采用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[单跳检测方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x338021278}[]{#_Toc216757392}

[]{#struct_0_65458_x3406_x1589940975}[]{#_Toc216757393}[]{#_Toc216757394}[]{#_Toc216757395}[执行本命令时，如果没有指定]{style="font-family:宋体"}**[multi-hop]{lang="EN-US"}**[和]{style="font-family:宋体"}**[single-hop]{lang="EN-US"}**[参数，则：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用]{style="font-family:宋体"}]{#struct_0_65458_x3406_x314091149}[BFD]{lang="EN-US"}[多跳方式检测本地路由器和指定]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体之间的链路。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果采用直连的物理接口建立]{style="font-family:宋体"}]{#struct_0_65458_x3406_529161498}[EBGP]{lang="EN-US"}[会话，且没有配置]{style="font-family:宋体"}**[peer ebgp-max-hop]{lang="EN-US"}**[命令，则采用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[单跳方式检测本地路由器和指定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体之间的链路；否则，采用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[多跳方式检测。]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_65458_x3406_x1884349741}[多跳和单跳检测方式的详细介绍，请参见"可靠性配置指导"中的"]{style="font-family:宋体"}[BFD]{lang="EN-US"}["。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x344246991}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_697521409}[BGP GR]{lang="EN-US"}[功能后，请慎用]{style="font-family:宋体"}[BGP]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。因为当链路故障时，系统可能还没来得及启用]{style="font-family:宋体"}[GR]{lang="EN-US"}[处理流程，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[已经检测到链路故障，从而导致]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败。如果设备上同时配置了]{style="font-family:宋体"}[BGP GR]{lang="EN-US"}[和]{style="font-family:宋体"}[BGP BFD]{lang="EN-US"}[，则在]{style="font-family:宋体"}[BGP GR]{lang="EN-US"}[期间请勿去使能]{style="font-family:宋体"}[BGP BFD]{lang="EN-US"}[，否则可能导致]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地路由器和]{style="font-family:宋体"}]{#struct_0_65458_x3406_x451614283}[BGP]{lang="EN-US"}[对等体采用的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测方式（单跳或多跳）必须相同，否则无法建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1252712345}[]{#_Toc216757396}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x314025613}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地路由器和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[之间的链路。]{style="font-family:宋体"}[]{#_Toc216757397}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_916205449}[]{#_Toc216757398}

[\[Sysname\] bgp 100[]{#_Toc216757399}]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 bfd]{lang="EN-US"}[]{#_Toc216757400}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_212550599}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地路由器和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[之间的链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1109117352}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1::1 bfd]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x935624287}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地路由器和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[之间的链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_142413937}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 2.2.2.2 bfd]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x313960077}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测本地路由器和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[2::2]{lang="EN-US"}[之间的链路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1462293245}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 2::2 bfd]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1450069533}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1155965536}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bfd session]{lang="EN-US"}**]{#struct_0_65458_x3406_x870972387}[（可靠性命令参考]{style="font-family:宋体"}[/BFD]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#1667558406 .myid}
[]{#_Toc404788651}[]{#struct_0_65458_x3406_x773723102}

**BGP \-- BGP配置命令 \-- peer capability-advertise conventional**

------------------------------------------------------------------------

[**[peer capability-advertise conventional]{lang="EN-US"}**]{#struct_0_65458_x3406_x313894541}[命令用来禁止本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由刷新、多协议扩展和]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号功能。]{style="font-family:宋体"}

[**[undo peer capability-advertise conventional]{lang="EN-US"}**]{#struct_0_65458_x3406_x2107202167}[命令用来使能本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由刷新、多协议扩展和]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x720150453}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **capability-advertise** **conventional**]{lang="EN-US"}]{#struct_0_65458_x3406_2051408079}

[**[undo]{lang="EN-US"}**[ **peer** { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **capability-advertise** **conventional**]{lang="EN-US"}]{#struct_0_65458_x3406_1333509611}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x814791498}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x151560658}[路由刷新、多协议扩展和]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_380891759}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x314877581}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1818277948}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1550114705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_485072410}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_701185543}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_364923509}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1053744457}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182481556}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x314812045}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182612628}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x227939865}

[[路由刷新功能是指发送和接收]{style="font-family:宋体"}[Route-refresh]{lang="EN-US"}]{#struct_0_65458_x3406_938416938}[消息的能力，它用来实现]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的软复位。]{style="font-family:宋体"}

[[多协议扩展功能是指发送和接收多协议扩展的]{style="font-family:宋体"}[Update]{lang="EN-US"}]{#struct_0_65458_x3406_x2067962586}[消息的能力，它用来实现通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[发布不同协议的路由信息，如]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[4]{lang="EN-US"}]{#struct_0_65458_x3406_1540452592}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号功能是指设备支持]{style="font-family:宋体"}[4]{lang="EN-US"}[字节的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，即]{style="font-family:宋体"}[AS]{lang="EN-US"}[号取值占用]{style="font-family:宋体"}[4]{lang="EN-US"}[字节，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，如果同时执行了本命令和]{style="font-family:宋体"}**[peer capability-advertise route-refresh]{lang="EN-US"}**]{#struct_0_65458_x3406_1779883750}[命令，则后执行的配置会覆盖之前的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1484171422}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1459612652}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，禁止本地路由器与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由刷新、多协议扩展和]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314353292}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 as-number 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 capability-advertise conventional]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_964654196}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，禁止本地路由器与对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由刷新、多协议扩展和]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1486236173}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 as-number 100]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 capability-advertise conventional]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_563034326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1894942514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer capability-advertise route-refresh]{lang="EN-US"}**]{#struct_0_65458_x3406_x314287756}
:::

::: {#-1625677124 .myid}
[]{#_Toc404788652}[]{#struct_0_65458_x3406_2079540881}

**BGP \-- BGP配置命令 \-- peer capability-advertise route-refresh**

------------------------------------------------------------------------

[**[peer capability-advertise route-refresh]{lang="EN-US"}**]{#struct_0_65458_x3406_x677369695}[命令用来使能本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由刷新功能。]{style="font-family:宋体"}

[**[undo peer capability-advertise route-refresh]{lang="EN-US"}**]{#struct_0_65458_x3406_1146677441}[命令用来禁止该功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x522126199}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **capability-advertise** **route-refresh**]{lang="EN-US"}]{#struct_0_65458_x3406_124458901}

[**[undo]{lang="EN-US"}**[ **peer** { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **capability-advertise** **route-refresh**]{lang="EN-US"}]{#struct_0_65458_x3406_x1947575129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_392949186}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x314222220}[路由刷新功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x607917885}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1737510815}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1346235274}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x458967221}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x990592337}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_116604111}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x38090650}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x314156684}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182612629}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1805731000}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182743701}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x569512351}

[[路由刷新（]{style="font-family:宋体"}[Route-refresh]{lang="EN-US"}]{#struct_0_65458_x3406_x502199715}[）功能是指发送和接收]{style="font-family:宋体"}[Route-refresh]{lang="EN-US"}[消息的能力。]{style="font-family:宋体"}

[[路由刷新功能用来实现]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x48362928}[会话的软复位：如果]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的路由策略发生了变化，则本地路由器会向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体发送]{style="font-family:宋体"}[Route-refresh]{lang="EN-US"}[消息，收到此消息的对等体将其路由信息重新发给本地路由器，本地路由器根据新的路由策略对接收到的路由信息进行过滤。从而，实现在不中断]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的情况下，对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表进行更新，使新的路由策略生效。]{style="font-family:宋体"}

[[只有本地路由器和对等体都支持路由刷新功能时，本地路由器和对等体之间建立的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_462951671}[会话才具有路由刷新能力。]{style="font-family:宋体"}

[[需要注意的是，如果同时执行了本命令和]{style="font-family:宋体"}**[peer capability-advertise ]{lang="EN-US"}[conventional]{lang="EN-US"}**]{#struct_0_65458_x3406_1339635146}[命令，则后执行的配置会覆盖之前的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314091148}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_529227034}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由刷新功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1858488295}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 as-number 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 capability-advertise route-refresh]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_2082130284}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由刷新功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1642173800}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 as-number 200]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 capability-advertise route-refresh]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1503423160}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x314025612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer capability-advertise conventional]{lang="EN-US"}**]{#struct_0_65458_x3406_x806796867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer keep-all-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_410376889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[refresh bgp]{lang="EN-US"}**]{#struct_0_65458_x3406_x884034533}
:::

::: {#-660781647 .myid}
[]{#_Toc404788653}[]{#struct_0_65458_x3406_1931346481}[]{#_Toc366153282}[]{#_Toc366167025}[]{#_Toc366220337}

**BGP \-- BGP配置命令 \-- peer capability-advertise suppress-4-byte-as**

------------------------------------------------------------------------

[**[peer capability-advertise suppress-4-byte-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x388092928}[命令用来使能]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号抑制功能。]{style="font-family:宋体"}

[**[undo peer capability-advertise suppress-4-byte-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x313960076}[命令用来关闭该功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1462227709}

[**[peer]{lang="EN-US"}**[ { *group-name \| ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **capability-advertise suppress-4-byte-as**]{lang="EN-US"}]{#struct_0_65458_x3406_x1830321077}

[**[undo peer ]{lang="EN-US"}**[{ *group-name \| ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **capability-advertise suppress-4-byte-as**]{lang="EN-US"}]{#struct_0_65458_x3406_1481146620}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x998547321}

[[设备没有使能]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_65458_x3406_1088592543}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号抑制功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x492728939}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x313894540}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2107136631}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1112818051}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1166321912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1551185781}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1579466250}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1190457377}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182743706}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x816984895}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182874778}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314877580}

[[设备支持]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_65458_x3406_x1818212412}[字节的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，即]{style="font-family:宋体"}[AS]{lang="EN-US"}[号取值占用]{style="font-family:宋体"}[4]{lang="EN-US"}[字节，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。缺省情况下，设备在与对端设备建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，通过]{style="font-family:宋体"}[Open]{lang="EN-US"}[消息通告对端设备本端支持]{style="font-family:宋体"}[4]{lang="EN-US"}[字节的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。如果对端设备不支持]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号（只支持]{style="font-family:宋体"}[2]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号），则会导致会话协商失败。此时，在本端与对端设备之间使能]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号抑制功能，可以使得本端设备通过]{style="font-family:宋体"}[Open]{lang="EN-US"}[消息向对端设备谎称自己不支持]{style="font-family:宋体"}[4]{lang="EN-US"}[字节的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，从而确保本端和对端设备之间可以成功建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[需要注意的是，如果对端设备支持]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_65458_x3406_x2031020608}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，请不要使能]{style="font-family:宋体"}[4]{lang="EN-US"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号抑制功能，否则会导致]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话无法建立。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_673854188}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_28279341}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置本端设备与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[进行会话协商时]{style="font-family:宋体"}[抑制]{style="font-family:宋体"}[4]{lang="EN-GB"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_2969933}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 as-number 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 capability-advertise suppress-4-byte-as]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_582328694}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置本端设备与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[进行会话协商时]{style="font-family:宋体"}[抑制]{style="font-family:宋体"}[4]{lang="EN-GB"}[字节]{style="font-family:宋体"}[AS]{lang="EN-US"}[号能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314812044}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1.1.1.1 as-number 200]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1.1.1.1 capability-advertise suppress-4-byte-as]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x227874329}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x141611150}
:::

::: {#909351260 .myid}
[]{#_Toc404788654}[]{#struct_0_65458_x3406_217850335}[]{#_Toc361659324}[]{#_Toc361659911}[]{#_Toc361660498}[]{#_Toc361664071}[]{#_Toc361747531}[]{#_Toc361819894}

**BGP \-- BGP配置命令 \-- peer connect-interface**

------------------------------------------------------------------------

[**[peer connect-interface]{lang="EN-US"}**]{#struct_0_65458_x3406_1490263367}[命令用来指定与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接使用的源接口，即采用指定源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[undo peer connect-interface]{lang="EN-US"}**]{#struct_0_65458_x3406_x314353295}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_964981876}

[**[peer]{lang="EN-US"}**[ { *group-name \| ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **connect-interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_65458_x3406_x1718614205}

[**[undo peer]{lang="EN-US"}**[ { *group-name \| ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **connect-interface**]{lang="EN-US"}]{#struct_0_65458_x3406_741101676}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x302132009}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1803221079}[使用到达]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体的最佳路由出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x648678543}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1804449387}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314287759}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2079737489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2084990822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_995781030}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x653114463}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x745594985}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_182874779}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1978941130}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_183005851}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x314222223}[：接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x607983421}

[[本命令的作用与]{style="font-family:宋体"}**[peer source-address]{lang="EN-US"}**]{#struct_0_65458_x3406_1222232325}[命令的作用类似：]{style="font-family:宋体"}**[peer source-address]{lang="EN-US"}**[命令直接指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址；本命令通过指定源接口，间接指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址。在一台]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器上如果同时执行本命令和]{style="font-family:宋体"}**[peer source-address]{lang="EN-US"}**[命令，则后执行的配置覆盖之前的配置。]{style="font-family:宋体"}

[[在如下场合需要通过本命令或]{style="font-family:宋体"}**[peer source-address]{lang="EN-US"}**]{#struct_0_65458_x3406_1391426861}[命令指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接使用的源接口或源地址：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定的对等体的]{style="font-family:宋体"}]{#struct_0_65458_x3406_x921550499}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址不是本地路由器与对等体之间直连接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址时，需要在对等体上通过本配置将建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接使用的源接口指定为对等体]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址所在的接口。例如，本端设备通过接口]{style="font-family:宋体"}[A]{lang="EN-US"}[和对端设备的接口]{style="font-family:宋体"}[B]{lang="EN-US"}[相连，在本端使用]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[ x.x.x.x **as-number** *as-number*]{lang="EN-US"}[命令将对端指定为自己的对等体，但是]{style="font-family:宋体"}[x.x.x.x]{lang="EN-US"}[不是接口]{style="font-family:宋体"}[B]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，需要在对端设备上使用]{style="font-family:宋体"}**[peer connect-interface]{lang="EN-US"}**[命令配置源接口，指定源接口为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[x.x.x.x]{lang="EN-US"}[所在的接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当建立]{style="font-family:宋体"}]{#struct_0_65458_x3406_x527892158}[BGP]{lang="EN-US"}[连接的路由器之间存在冗余链路时，如果路由器上的一个接口发生故障，链路状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[，建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址可能会随之发生变化，导致]{style="font-family:宋体"}[BGP]{lang="EN-US"}[需要重新建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，造成网络震荡。为了避免该情况的发生，建议网络管理员将建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接所使用的源地址配置为]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的地址，或将源接口配置为]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，以提高]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的可靠性和稳定性。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_65458_x3406_x933631218}[BGP]{lang="EN-US"}[对等体之间同时建立多条]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，如果没有明确指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址，可能会导致根据最优路由选择]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址错误，并影响]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的建立。如果多条]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话基于不同接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立，则建议用户在配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体时，通过配置源接口或源地址明确指定每个]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址；如果多条]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话基于同一接口的不同]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立，则建议用户通过配置源地址，明确指定每个]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1290703303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地路由器源接口的地址和对等体源接口的地址之间必须路由可达。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1744351595}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{style="font-family:宋体"}]{#struct_0_65458_x3406_x314156687}[EBGP]{lang="EN-US"}[对等体上指定非直连接口（除]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口外）作为源接口，则需要配置]{style="font-family:宋体"}**[peer ebgp-max-hop]{lang="EN-US"}**[命令允许本地路由器同非直连网络上的邻居建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上存在多个]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1805927608}[IP]{lang="EN-US"}[地址，则建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时使用接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；如果接口上存在多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，则设备根据内部定义的原则从中选择一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址。源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的选择具有不确定性，因此，在这种情况下，建议用户通过]{style="font-family:宋体"}**[peer source-address]{lang="EN-US"}**[命令明确指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能通过本命令指定建立]{style="font-family:宋体"}]{#struct_0_65458_x3406_x409334085}[TCP]{lang="EN-US"}[连接的源接口为]{style="font-family:宋体"}[VT]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Template]{lang="EN-US"}[，虚拟模板）接口，因为]{style="font-family:宋体"}[VT]{lang="EN-US"}[口只能作为模板口并不处理相关业务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1439340464}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1046792712}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，使用接口]{style="font-family:宋体"}[Loopback0]{lang="EN-US"}[作为建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1996905024}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test connect-interface loopback 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x296241835}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，使用接口]{style="font-family:宋体"}[Loopback0]{lang="EN-US"}[作为建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314091151}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test connect-interface loopback 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_529685785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer ebgp-max-hop]{lang="EN-US"}**]{#struct_0_65458_x3406_868268759}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer source-address]{lang="EN-US"}**]{#struct_0_65458_x3406_x1506782102}
:::

::: {#1246776188 .myid}
[]{#_Toc404788655}[]{#struct_0_65458_x3406_x1296372064}

**BGP \-- BGP配置命令 \-- peer default-route-advertise**

------------------------------------------------------------------------

[**[peer default-route-advertise]{lang="EN-US"}**]{#struct_0_65458_x3406_x1607337500}[命令用来向对等体]{style="font-family:
宋体"}[/]{lang="EN-US"}[对等体组发送缺省路由。]{style="font-family:宋体"}

[**[undo peer default-route-advertise]{lang="EN-US"}**]{#struct_0_65458_x3406_532416902}[命令用来取消向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发送缺省路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1853408210}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1918725769}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **default-route-advertise** \[ **route-policy** *route-policy-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x314025615}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **default-route-advertise**]{lang="EN-US"}]{#struct_0_65458_x3406_916074377}

[[BGP VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_x825634997}[地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ ]{lang="EN-US"}[{ *group-name* \| *ip-address* \[ *mask-length* \] } **default-route-advertise** **vpn-instance** *vpn-instance-name*]{lang="EN-US"}]{#struct_0_65458_x3406_x909168843}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **default-route-advertise** **vpn-instance** *vpn-instance-name*]{lang="EN-US"}]{#struct_0_65458_x3406_x487877197}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_571188038}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **default-route-advertise** \[ **route-policy** *route-policy-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1037634896}

[**[undo]{lang="EN-US"}[ peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **default-route-advertise**]{lang="EN-US"}]{#struct_0_65458_x3406_x313960079}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_2132814611}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **default-route-advertise** \[ **route-policy** *route-policy-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_2133207827}

[**[undo]{lang="EN-US"}[ peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **default-route-advertise** \[ **route-policy** *route-policy-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_2133076755}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1461637885}

[[不向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x507477041}[对等体组发送缺省路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_149901110}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_144172050}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_572605301}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1079672659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1499186997}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x313894543}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x2107333239}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_804185695}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1748565497}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_897819338}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1748499961}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_2007155538}[：为发布的缺省路由应用路由策略，以便修改路由的属性等。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[表示路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示没有为发布的缺省路由应用路由策略。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ ]{lang="EN-US"}*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1313120756}[：]{style="font-family:宋体"}[向对等体或对等体组发布指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的缺省路由。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x49959242}

[[如果配置了]{style="font-family:宋体"}**[peer default-route-advertise]{lang="EN-US"}**]{#struct_0_65458_x3406_x1028047666}[命令，则本地路由器会向指定的对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布一条下一跳为自身的缺省路由。在本地路由器的路由表中不需要存在缺省路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314877583}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1818146876}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，设置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布缺省路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x148216331}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test default-route-advertise]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1456974585}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，设置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布缺省路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x567154511}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer test default-route-advertise]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x314812047}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，设置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布缺省路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x228070937}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer test default-route-advertise]{lang="EN-US"}
:::

::: {#-1234819269 .myid}
[]{#_Toc404788656}[]{#struct_0_65458_x3406_x1965963}

**BGP \-- BGP配置命令 \-- peer description**

------------------------------------------------------------------------

[**[peer description]{lang="EN-US"}**]{#struct_0_65458_x3406_x999477089}[命令用来配置对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的描述信息。]{style="font-family:宋体"}

[**[undo peer description]{lang="EN-US"}**]{#struct_0_65458_x3406_x78013752}[命令用来删除对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1763139015}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **description** *description-text*]{lang="EN-US"}]{#struct_0_65458_x3406_736827508}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **description**]{lang="EN-US"}]{#struct_0_65458_x3406_x314353294}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_965047412}

[[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x209293366}[对等体组没有描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1087798303}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_499765817}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1811767401}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x234047473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2028372955}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314287758}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_2079671953}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1456294862}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1748696570}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x49339679}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1748827642}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[description-text]{lang="EN-US"}*]{#struct_0_65458_x3406_x1027731709}[：对等体的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[79]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1502402285}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1553581513}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[ISP1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x314222222}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test description ISP1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x608048957}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[ISP1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_365991250}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test description ISP1]{lang="EN-US"}
:::

::: {#160840239 .myid}
[]{#_Toc404788657}[]{#struct_0_65458_x3406_1978937937}[]{#_Toc299632393}[]{#_Toc299632394}[]{#_Toc299632395}[]{#_Toc299632396}[]{#_Toc299632397}[]{#_Toc299632398}[]{#_Toc299632399}[]{#_Toc299632400}[]{#_Toc299632401}[]{#_Toc299632402}[]{#_Toc299632403}[]{#_Toc299632404}[]{#_Toc299632405}[]{#_Toc299632406}[]{#_Toc299632407}[]{#_Toc299632408}[]{#_Toc299632409}[]{#_Toc299632410}[]{#_Toc299632411}[]{#_Toc299632413}[]{#_Toc299632414}[]{#_Toc299632416}

**BGP \-- BGP配置命令 \-- peer ebgp-max-hop**

------------------------------------------------------------------------

[**[peer ebgp-max-hop]{lang="EN-US"}**]{#struct_0_65458_x3406_1937603302}[命令用来配置允许本地路由器同非直连网络上的邻居建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话，同时指定允许的最大跳数。]{style="font-family:宋体"}

[**[undo peer ebgp-max-hop]{lang="EN-US"}**]{#struct_0_65458_x3406_x1937995404}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1616255754}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ebgp-max-hop** \[ *hop-count* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x314156686}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ebgp-max-hop**]{lang="EN-US"}]{#struct_0_65458_x3406_x1805862072}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1089291228}

[[不允许同非直连网络上的邻居建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1303319475}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2140048709}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_219929645}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1368929565}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x696376726}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x314091150}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_529751321}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_482339390}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_765754511}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1748762111}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1739668481}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1748893183}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[hop-count]{lang="EN-US"}*]{#struct_0_65458_x3406_796930638}[：最大路由器跳数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1681066609}

[[当前路由器要与另外一个路由器建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x314025614}[会话，它们之间必须具有直连的物理链路，且必须使用直连接口建立会话。如果不满足这一要求，则必须使用]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[ **ebgp-max-hop**]{lang="EN-US"}[命令允许它们经过多跳建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[需要注意的是，执行]{style="font-family:宋体"}]{#struct_0_65458_x3406_x595609995}**[peer ttl-security]{lang="DA"}**[命令后，]{style="font-family:宋体"}[只要本地设备和指定的对等体通过了]{style="font-family:宋体"}[GTSM]{lang="EN-US"}[检查，就允许在二者之间建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话，不管二者之间的跳数是否超过]{style="font-family:宋体"}**[peer ebgp-max-hop]{lang="EN-US"}**[命令指定的跳数范围。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_916008841}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1551420539}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置允许同非直连网络上的]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[建立会话，允许的最大跳数为缺省值]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1678124175}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test ebgp-max-hop]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1258030936}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置允许同非直连网络上的]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[建立会话，允许的最大跳数为缺省值]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1027745042}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test ebgp-max-hop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x595741067}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer ttl-security]{lang="DA"}**]{#struct_0_65458_x3406_x595347851}
:::

::: {#424848829 .myid}
[]{#_Toc404788658}[]{#struct_0_65458_x3406_x313960078}

**BGP \-- BGP配置命令 \-- peer enable**

------------------------------------------------------------------------

[**[peer enable]{lang="EN-US"}**]{#struct_0_65458_x3406_1461572349}[命令用来使能本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换路由信息的能力。]{style="font-family:宋体"}

[**[undo peer enable]{lang="EN-US"}**]{#struct_0_65458_x3406_x1685570469}[命令用来禁止本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x52318390}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x268018011}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP-VPN VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv4 MDT]{lang="EN-US"}[地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] } **enable**]{lang="EN-US"}]{#struct_0_65458_x3406_x491947129}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] } **enable**]{lang="EN-US"}]{#struct_0_65458_x3406_x85419229}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x297662263}[单播地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **enable**]{lang="EN-US"}]{#struct_0_65458_x3406_x313894542}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **enable**]{lang="EN-US"}]{#struct_0_65458_x3406_x2107267703}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x244706025}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **enable**]{lang="EN-US"}]{#struct_0_65458_x3406_89478609}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **enable**]{lang="EN-US"}]{#struct_0_65458_x3406_x725797654}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1716876062}

[[本地路由器不能与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x245336049}[对等体组交换路由信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x314877582}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1818081340}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP-VPN VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv4 MDT]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x645341720}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1327138213}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_370333850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1359036450}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x91072101}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1677238746}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1345477580}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x314812046}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1345608652}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x228005401}

[[在不同的视图下执行]{style="font-family:宋体"}**[peer enable]{lang="EN-US"}**]{#struct_0_65458_x3406_69444259}[命令，可以使能本地路由器与指定对等体交换不同地址族路由信息的能力：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_244569439}[单播地址族视图下，使能的是交换]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[单播路由信息的能力，并且学习到的路由将添加到公网]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP-VPN IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x81238748}[单播地址族视图下，使能的是交换]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[单播路由信息的能力，并且学习到的路由将添加到指定]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_x788576545}[地址族视图下，使能的是交换]{style="font-family:
宋体"}[VPNv4]{lang="EN-US"}[路由信息的能力。]{style="font-family:
宋体"}[MPLS L3VPN]{lang="EN-US"}[组网中，需要在]{style="font-family:
宋体"}[PE]{lang="EN-US"}[设备的]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族视图下执行本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP-VPN VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_1196436996}[地址族视图，使能的是交换]{style="font-family:
宋体"}[VPNv4]{lang="EN-US"}[路由信息的能力。嵌套]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[组网中，在运营商]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备的]{style="font-family:宋体"}[BGP-VPN VPNv4]{lang="DA"}[地址族视图下执行本命令，可以使能]{style="font-family:宋体"}[运营商]{style="font-family:宋体"}[PE]{lang="EN-US"}[和运营商]{style="font-family:宋体"}[CE]{lang="EN-US"}[之间交互]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[路由信息的能力，并且运营商]{style="font-family:宋体"}[PE]{lang="EN-US"}[将学习到的]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[路由添加到某个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的路由表中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1581531494}[单播地址族视图下，使能的是交换]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[单播路由信息的能力，并且学习到的路由将添加到公网]{style="font-family:
宋体"}[IPv6 BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1607961010}[单播地址族视图下，使能的是交换]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[单播路由信息的能力，并且学习到的路由将添加到指定]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP VPNv6]{lang="EN-US"}]{#struct_0_65458_x3406_x939419812}[地址族视图下，使能的是交换]{style="font-family:
宋体"}[VPNv6]{lang="EN-US"}[路由信息的能力。]{style="font-family:
宋体"}[IPv6 MPLS L3VPN]{lang="EN-US"}[组网中，需要在]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备的]{style="font-family:宋体"}[BGP VPNv6]{lang="EN-US"}[地址族视图下执行本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP L2VPN]{lang="EN-US"}]{#struct_0_65458_x3406_2106135247}[地址族视图下，使能的是交换]{style="font-family:
宋体"}[L2VPN]{lang="EN-US"}[信息的能力。]{style="font-family:
宋体"}[MPLS L2VPN]{lang="EN-US"}[和]{style="font-family:
宋体"}[VPLS]{lang="EN-US"}[组网中，需要在]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备的]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下执行本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x596068749}[组播地址族视图下，使能的是交换用于]{style="font-family:
宋体"}[RPF]{lang="EN-US"}[检查的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[单播路由信息的能力。]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查的详细介绍，请参见"]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播配置指导"中的"组播路由与转发"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x595675533}[组播地址族视图下，使能的是交换用于]{style="font-family:
宋体"}[RPF]{lang="EN-US"}[检查的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[单播路由信息的能力。]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查的详细介绍，请参见"]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播配置指导"中的"]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由与转发"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP IPv4 MDT]{lang="EN-US"}]{#struct_0_65458_x3406_x595806605}[地址族视图下，使能的是交换]{style="font-family:
宋体"}[MDT]{lang="EN-US"}[信息的能力。组播]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[组网中，需要在]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备的]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族视图下执行本命令。]{style="font-family:宋体"}

[[如果在某个视图下执行了]{style="font-family:宋体"}**[undo peer enable]{lang="EN-US"}**]{#struct_0_65458_x3406_1187995147}[命令，则本地路由器与指定对等体之间不再交换对应地址族的路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1783872854}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x287077064}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[交换]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播路由信息的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1608026546}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer 1.1.1.1 enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1126494941}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[交换]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播路由信息的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x393637511}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer 1.1.1.1 enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_861182721}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[交换]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由信息的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x68250545}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer 1.1.1.1 enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1840024532}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[交换]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由信息的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1608092082}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer 1::1 enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x752403797}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[交换]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[信息的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x2111793984}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] peer 1.1.1.1 enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x595347853}[在]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族视图下，使能本地路由器与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[交换]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[信息的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x595872142}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 mdt]{lang="EN-US"}

[\[Sysname-bgp-mdt\] peer 1.1.1.1 enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x735104299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x784920678}
:::

::: {#-610957859 .myid}
[]{#_Toc404788659}[]{#struct_0_65458_x3406_1608157618}[]{#_Toc361659330}[]{#_Toc361659917}[]{#_Toc361660504}[]{#_Toc361664077}[]{#_Toc361747537}[]{#_Toc361819900}

**BGP \-- BGP配置命令 \-- peer fake-as**

------------------------------------------------------------------------

[**[peer fake-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x1116438118}[命令用来为对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组指定一个虚拟的本地自治系统号。]{style="font-family:宋体"}

[**[undo peer fake-as]{lang="EN-US"}**]{#struct_0_65458_x3406_199645974}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_499662514}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **fake-as** *as-number*]{lang="EN-US"}]{#struct_0_65458_x3406_2049614397}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **fake-as**]{lang="EN-US"}]{#struct_0_65458_x3406_1086285092}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x740770126}

[[没有为对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_573182318}[对等体组配置虚拟的本地自治系统号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608223154}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_41594773}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1908349832}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_147442104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1720238052}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1120085762}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1943405335}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1608288690}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1345280970}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x386610948}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1345412042}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1031912144}[：本地自治系统号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_595720800}

[[进行系统移植时，例如，]{style="font-family:宋体"}[Router A]{lang="EN-US"}]{#struct_0_65458_x3406_x1868711641}[原来位于]{style="font-family:宋体"}[AS 2]{lang="EN-US"}[，现在将它移植到]{style="font-family:宋体"}[AS 3]{lang="EN-US"}[里，网络管理员需要在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的所有]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体上修改]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。通过在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上为]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组配置一个虚拟的本地自治系统号]{style="font-family:宋体"}[2]{lang="EN-US"}[，可以将本地真实的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}[3]{lang="EN-US"}[隐藏起来。在]{style="font-family:
宋体"}[EBGP]{lang="EN-US"}[对等体看来]{style="font-family:宋体"}[Router A]{lang="EN-US"}[始终位于]{style="font-family:宋体"}[AS 2]{lang="EN-US"}[，不需要改变]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体上的配置。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x111673608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer fake-as]{lang="EN-US"}**]{#struct_0_65458_x3406_1343517966}[命令只适用于]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体和对等体组。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在本地路由器上执行了]{style="font-family:宋体"}]{#struct_0_65458_x3406_x750126042}**[peer fake-as]{lang="EN-US"}**[命令，则在指定的对等体上需要将本地路由器的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号配置为本命令中指定的虚拟本地自治系统号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608354226}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1917192586}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，为对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[指定虚拟的本地自治系统号为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x549597651}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test fake-as 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x583415254}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，为对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[指定虚拟的本地自治系统号为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1359115275}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test fake-as 200]{lang="EN-US"}
:::

::: {#-524914655 .myid}
[]{#_Toc404788660}[]{#struct_0_65458_x3406_1346080942}[]{#_Toc316655966}[]{#_Toc312414484}[]{#_Toc312402363}[]{#_Toc180224216}

**BGP \-- BGP配置命令 \-- peer filter-policy**

------------------------------------------------------------------------

[**[peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1608419762}[命令用来为对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组设置基于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由过滤策略。]{style="font-family:宋体"}

[**[undo peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_407387350}[命令用来取消已有的设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2104267575}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1818594061}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **filter-policy** *acl-number* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x521194563}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **filter-policy** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1694486938}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1712050244}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **filter-policy** *acl6-number* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_2018131697}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **filter-policy** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1607436722}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1706750819}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **filter-policy** *acl6-number* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1145174232}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **filter-policy** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1954385590}

[[BGP VPNv6]{lang="EN-US"}]{#struct_0_65458_x3406_2119785116}[地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **filter-policy** *acl6-number* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x24947115}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **filter-policy** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1317504492}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1607502258}

[[没有设置基于]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_65458_x3406_x930924021}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由过滤策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1559359350}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_2035300466}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1734408203}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1471860445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1324572064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x115084729}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1607961011}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x939485348}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1345477584}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_248224656}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1345608656}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_438391775}[：访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_65458_x3406_343129842}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_65458_x3406_547991857}[：对向指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布的路由应用过滤策略。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_65458_x3406_x1649050081}[：对从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由应用过滤策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608026547}

[[配置]{style="font-family:宋体"}**[peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1126560477}[命令时需要同时在系统视图下通过]{style="font-family:宋体"}**[acl]{lang="EN-US"}**[命令配置对应的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。如果本命令中指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[尚未创建，则所有路由均通过过滤。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1571678119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过基本]{style="font-family:宋体"}]{#struct_0_65458_x3406_1806405613}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[）对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息进行过滤时，如果配置了]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **source** *source-address* *source-wildcard*]{lang="EN-US"}[命令，则只要路由的目的网络地址与]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}*[source-address source-wildcard]{lang="EN-US"}*[匹配，则该路由与]{style="font-family:
宋体"}**[rule]{lang="EN-US"}**[命令配置的规则匹配，不会再比较路由的目的网络地址掩码。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_65458_x3406_x1635292564}[（]{lang="EN-US" style="font-family:宋体"}[3000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[）对]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息进行过滤时，]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[命令配置的规则用]{lang="EN-US" style="font-family:宋体"}[来过滤指定目的网络地址的路由；]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[命令配置的规则用]{lang="EN-US" style="font-family:宋体"}[来过滤指定目的网络地址和掩码的路由，其中]{lang="EN-US" style="font-family:宋体"}**[source ]{lang="EN-US"}***[sour-addr sour-wildcard]{lang="EN-US"}*[用来过滤路由目的网络地址，]{lang="EN-US" style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[用来过滤路由掩码。]{lang="EN-US" style="font-family:宋体"}**[destination ]{lang="EN-US"}***[dest-addr dest-wildcard]{lang="EN-US"}*[指定的掩码应该是连续的。如果指定的掩码不连续，则该过滤掩码的条件不生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x427759854}

[]{#struct_0_65458_x3406_799939307}[]{#_Toc138238283}[]{#_Toc32467756}[]{#_Toc32464225}[]{#_Toc30500469}[\# ]{lang="EN-US"}[在]{style="font-family:
宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置利用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的访问控制列表过滤向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1608092083}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test filter-policy 2000 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x752338261}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置利用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[访问控制列表过滤向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_551458585}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer test filter-policy 2000 export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1154264487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_65458_x3406_x1324518710}[（]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{style="font-family:宋体"}[/ACL]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy export]{lang="EN-US"}**]{#struct_0_65458_x3406_x1027812178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy ]{lang="EN-US"}**]{#struct_0_65458_x3406_x1649118646}**[import]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer as-path-acl]{lang="EN-US"}**]{#struct_0_65458_x3406_1608157619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1116372582}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1078062328}
:::

::: {#232826817 .myid}
[]{#_Toc404788661}[]{#struct_0_65458_x3406_124657215}

**BGP \-- BGP配置命令 \-- peer group**

------------------------------------------------------------------------

[**[peer group]{lang="EN-US"}**]{#struct_0_65458_x3406_721050106}[命令用来向对等体组中添加指定的对等体。]{style="font-family:宋体"}

[**[undo peer group]{lang="EN-US"}**]{#struct_0_65458_x3406_x2116258201}[命令用来从对等体组中删除指定的对等体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_642478468}

[**[peer]{lang="EN-US"}**[ { *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **group** *group-name* \[ **as-number** *as-number* \]]{lang="EN-US"}]{#struct_0_65458_x3406_1608223155}

[**[undo peer]{lang="EN-US"}**[ { *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **group** *group-name*]{lang="EN-US"}]{#struct_0_65458_x3406_41529237}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1882409257}

[[对等体组中不存在任何对等体。]{style="font-family:宋体"}]{#struct_0_65458_x3406_475446982}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_468271312}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1457122870}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1857960895}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x500161549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1608288691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x386676484}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_90320490}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1383602383}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x2031405437}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1383471311}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_28327995}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[**[as-number]{lang="EN-US"}**[ *as-number*]{lang="EN-US"}]{#struct_0_65458_x3406_x441371333}[：对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_163218827}

[[可以通过以下方式将对等体加入对等体组：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1608354227}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[先通过]{lang="EN-US" style="font-family:宋体"}**[peer as-number]{lang="EN-US"}**]{#struct_0_65458_x3406_x1917127050}[命令创建对等体并指定对等体的]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[号，再通过]{lang="EN-US" style="font-family:宋体"}**[peer group]{lang="EN-US"}**[命令将其加入对等体组。采用这种方式时，需要注意：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[peer group]{lang="EN-US"}**]{#struct_0_65458_x3406_x1149889021}[命令时可以指定]{lang="EN-US" style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数，指定的]{lang="EN-US" style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数，必须与]{lang="EN-US" style="font-family:宋体"}**[peer as-number]{lang="EN-US"}**[命令中配置的对等体]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[号相同。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1581884410}**[peer as-number]{lang="EN-US"}**[命令指定了对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号必须与对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号相同，否则无法将对等体加入对等体组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果将对等体加入]{style="font-family:宋体"}]{#struct_0_65458_x3406_912571915}[IBGP]{lang="EN-US"}[对等体组，则该对等体必须是]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[通过]{style="font-family:宋体"}]{#struct_0_65458_x3406_1023175423}**[peer group]{lang="EN-US"}**[命令创建对等体的同时，将其加入对等体组。采用这种方式时，需要注意：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{lang="EN-US" style="font-family:宋体"}**[peer as-number]{lang="EN-US"}**]{#struct_0_65458_x3406_1376900590}[命令指定了对等体组的]{lang="EN-US" style="font-family:
宋体"}[AS]{lang="EN-US"}[号，则执行]{lang="EN-US" style="font-family:宋体"}**[peer group]{lang="EN-US"}**[命令时无需指定]{lang="EN-US" style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数，对等体的]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[号为该对等体组的]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[号。执行]{lang="EN-US" style="font-family:宋体"}**[peer group]{lang="EN-US"}**[命令时如果指定了]{lang="EN-US" style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数，则]{lang="EN-US" style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数必须与对等体组的]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[号相同。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定对等体组的]{style="font-family:宋体"}]{#struct_0_65458_x3406_x829279255}[AS]{lang="EN-US"}[号，且该对等体组为]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组，则执行]{style="font-family:宋体"}**[peer group]{lang="EN-US"}**[命令时必须指定]{style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定对等体组的]{style="font-family:宋体"}]{#struct_0_65458_x3406_1608419763}[AS]{lang="EN-US"}[号，且该对等体组为]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组，则执行]{style="font-family:宋体"}**[peer group]{lang="EN-US"}**[命令时无需指定]{style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数，对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号为本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}[执行]{lang="EN-US" style="font-family:宋体"}**[peer group]{lang="EN-US"}**[命令时如果指定了]{lang="EN-US" style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数，则]{lang="EN-US" style="font-family:宋体"}**[as-number]{lang="EN-US"}**[参数必须与本地]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[号相同。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_407452886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1445954731}**[peer as-number]{lang="EN-US"}**[命令指定了对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则只有与该对等体组]{style="font-family:宋体"}[AS]{lang="EN-US"}[号相同的对等体才能加入该对等体组，即对等体组中所有对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号均相同；如果没有指定对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则加入该对等体组的对等体保留自己的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，即对等体组中对等体的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号可以相同，也可以不同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令将对等体加入对等体组后，还需要执行]{style="font-family:宋体"}]{#struct_0_65458_x3406_x192856243}**[peer enable]{lang="EN-US"}**[命令，本地路由器才具有与指定对等体组交换相应地址族路由信息的能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_605949915}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1944663882}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的对等体加入到]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1607436723}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] group test external]{lang="EN-US"}

[\[Sysname-bgp\] peer 10.1.1.1 group test as-number 2004]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1706685283}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[的对等体加入到]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1357450871}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] group test external ]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 10.1.1.1 group test as-number 2004]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x16146914}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的对等体加入到]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x791678709}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] group test external]{lang="EN-US"}

[\[Sysname-bgp\] peer 1::1 group test as-number 2004]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_363692430}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的对等体加入到]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1607502259}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] group test external ]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 group test as-number 2004]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x930989557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[group]{lang="EN-US"}**]{#struct_0_65458_x3406_x19328206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer as-number]{lang="EN-US"}**]{#struct_0_65458_x3406_x1323484089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer enable]{lang="EN-US"}**]{#struct_0_65458_x3406_1683146990}
:::

::: {#36887261 .myid}
[]{#_Toc404788662}[]{#struct_0_65458_x3406_x64200577}

**BGP \-- BGP配置命令 \-- peer ignore**

------------------------------------------------------------------------

[**[peer ignore]{lang="EN-US"}**]{#struct_0_65458_x3406_1607961008}[命令用来禁止与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组建立会话。]{style="font-family:宋体"}

[**[undo peer ignore]{lang="EN-US"}**]{#struct_0_65458_x3406_x939944099}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_614666389}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ignore**]{lang="EN-US"}]{#struct_0_65458_x3406_x487280503}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ignore**]{lang="EN-US"}]{#struct_0_65458_x3406_183518280}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1945108018}

[[允许与]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_851896464}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组建立会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1441861052}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1608026544}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1126363869}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1633650481}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1871123680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x761747077}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_667701668}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x883895509}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1383209166}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1530229643}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1383078094}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608092080}

[[由于网络升级维护等原因，需要暂时断开与某个对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x752272725}[对等体组的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，可以通过]{style="font-family:宋体"}**[peer ignore]{lang="EN-US"}**[命令禁止与该对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组建立会话。当网络恢复后，通过执行]{style="font-family:宋体"}**[undo peer ignore]{lang="EN-US"}**[命令恢复与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的会话。这样，网络管理员无需删除并重新进行对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组相关配置，减少了网络维护的工作量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本设备和对等体的会话已经建立，则执行]{style="font-family:宋体"}]{#struct_0_65458_x3406_599591086}**[peer ignore]{lang="EN-US"}**[命令后，会停止该会话，并且清除所有相关路由信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本设备和对等体组的会话已经建立，则执行]{style="font-family:宋体"}]{#struct_0_65458_x3406_x905361764}**[peer ignore]{lang="EN-US"}**[命令后，会终止与对等体组内所有对等体之间的会话，并且清除所有相关路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1702009438}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1899352622}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，禁止与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[建立会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1608157616}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 ignore]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1115782758}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，禁止与对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[建立会话。]{style="font-family:宋体"}

[]{#_Toc332980898}[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1961803246}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 ignore]{lang="EN-US"}
:::

::: {#1677942795 .myid}
[]{#_Toc404788663}[]{#struct_0_65458_x3406_1927011914}

**BGP \-- BGP配置命令 \-- peer ignore-originatorid**

------------------------------------------------------------------------

[**[peer ignore-originatorid]{lang="EN-US"}**]{#struct_0_65458_x3406_x1327847302}[命令用来配置忽略]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo peer ignore-originatorid]{lang="EN-US"}**]{#struct_0_65458_x3406_1064140628}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x482651221}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ignore-originatorid**]{lang="EN-US"}]{#struct_0_65458_x3406_1608223152}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ignore-originatorid**]{lang="EN-US"}]{#struct_0_65458_x3406_41725845}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x625412330}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x731977072}[路由器不会忽略]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1008370979}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_414589964}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x85768486}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1500848225}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1608288688}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x387135237}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x685077651}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x640114221}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1383143633}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_46743136}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1383667920}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1152018109}

[[路由反射器从某个对等体接收到路由后，在反射该路由之前为其添加]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}]{#struct_0_65458_x3406_1582322526}[属性，标识该路由在本]{style="font-family:宋体"}[AS]{lang="EN-US"}[内的起源。]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}[属性的值为该对等体的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器接收到路由后，将路由中的]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}[属性值与本地的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[进行比较，如果二者相同则丢弃该路由，从而避免路由环路。]{style="font-family:宋体"}

[[在某些特殊的组网中（如防火墙组网），如果需要接收]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}]{#struct_0_65458_x3406_415597737}[属性值与本地]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[相同的路由，则需要执行本命令忽略]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1917061514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请谨慎使用本命令。如果无法确保执行本命令后网络中不会产生环路，请不要执行本命令。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1075415816}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令后，]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1223064016}[路由的]{lang="EN-US" style="font-family:宋体"}[CLUSTER_LIST]{lang="EN-US"}[属性也会被忽略。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1205816388}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_2031236876}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置忽略从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[收到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1438179555}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 ignore-originatorid]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1608419760}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置忽略从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[收到]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[ORIGINATOR_ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_407518422}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1.1.1.1 ignore-originatorid]{lang="EN-US"}
:::

::: {#-725883394 .myid}
[]{#_Toc404788664}[]{#struct_0_65458_x3406_x376376815}

**BGP \-- BGP配置命令 \-- peer ipsec-profile**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**[ **ipsec-profile**]{lang="EN-US"}]{#struct_0_65458_x3406_x1975403071}[命令用来为]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[**[undo peer]{lang="EN-US"}**[ **ipsec-profile**]{lang="EN-US"}]{#struct_0_65458_x3406_x694606409}[命令用来取消为]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1053036444}

[**[peer]{lang="EN-US"}[ ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **ipsec-profile** *profile-name*]{lang="EN-US"}]{#struct_0_65458_x3406_x1484166797}

[**[undo peer]{lang="EN-US"}[ ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **ipsec-profile**]{lang="EN-US"}]{#struct_0_65458_x3406_1607436720}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1706881891}

[[没有为]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1227294813}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x198811211}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1386721805}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x640357460}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1239075327}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x202846698}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1607502256}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x931579381}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1511592633}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1383602379}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[profile-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x519365812}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x707121109}

[[为了避免路由信息外泄或者非法者对设备进行恶意攻击，可以利用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_65458_x3406_790390137}[安全隧道对]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文进行保护。通过]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[提供的数据机密性、完整性、数据源认证等功能，确保]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文不会被侦听或恶意篡改，并避免非法者构造]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文对设备进行攻击。]{style="font-family:宋体"}

[[在互为]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}]{#struct_0_65458_x3406_803045351}[邻居的两台设备上都配置通过]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[保护]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文后，一端设备在发送]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文时通过]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[对报文进行加封装，另一端设备接收到报文后，通过]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[对报文进行解封装。如果解封装成功，则接收该报文，正常建立]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[对等体关系或学习]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[路由；如果设备接收到不受]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[保护的]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文，或]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文解封装失败，则会丢弃该报文。]{style="font-family:宋体"}

[[配置通过]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_65458_x3406_1607961009}[保护]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文包括如下步骤：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_x940009635}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置手工方式的]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_65458_x3406_1113991646}[安全框架]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[通过本命令为]{style="font-family:宋体"}]{#struct_0_65458_x3406_x769290393}[IPv6 BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[IPsec]{lang="EN-US"}]{#struct_0_65458_x3406_x1790566246}[安全提议和]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的详细介绍，请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPsec]{lang="EN-US"}["。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1467524518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令应用的]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_65458_x3406_x872077930}[安全框架必须是手工方式的]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在一台设备上配置了通过]{style="font-family:宋体"}]{#struct_0_65458_x3406_1608026545}[IPsec]{lang="EN-US"}[保护]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文功能，那么在它的]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[对等体上也必须配置该功能。否则，会导致]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[报文无法正常接收。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1126429405}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1561082285}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，为对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[应用安全框架]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_417676537}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test ipsec-profile profile001]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1479639493}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，为对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[应用安全框架]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x2074885029}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test ipsec-profile profile001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608092081}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp group]{lang="EN-US"}**]{#struct_0_65458_x3406_x752207189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_240566689}
:::

::: {#1499484482 .myid}
[]{#_Toc404788665}[]{#struct_0_65458_x3406_123273434}

**BGP \-- BGP配置命令 \-- peer keep-all-routes**

------------------------------------------------------------------------

[**[peer keep-all-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_999965266}[命令用来保存所有来自指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的原始路由更新信息，不管这些路由是否通过了路由策略的过滤。]{style="font-family:宋体"}

[**[undo peer keep-all-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_x63927081}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x520232463}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x927143451}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **keep-all-routes**]{lang="EN-US"}]{#struct_0_65458_x3406_1608157617}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **keep-all-routes**]{lang="EN-US"}]{#struct_0_65458_x3406_x1115717222}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_52211464}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **keep-all-routes**]{lang="EN-US"}]{#struct_0_65458_x3406_1916680810}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **keep-all-routes**]{lang="EN-US"}]{#struct_0_65458_x3406_335480034}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x595741064}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **keep-all-routes**]{lang="EN-US"}]{#struct_0_65458_x3406_x595347848}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **keep-all-routes**]{lang="EN-US"}]{#struct_0_65458_x3406_970211802}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1964893405}

[[不保存来自对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x55914991}[对等体组的原始路由更新信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1292426687}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1608223153}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_41660309}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x188529812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1483074417}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1469889056}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1726671827}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x892938776}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786624766}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1383236013}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786493694}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608288689}

[[如果本地路由器和对等体不都支持路由刷新功能，那么要实现]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x387200773}[会话的软复位，则需要通过配置本命令将从对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的所有原始路由更新信息保存在本地，当选路策略发生改变后，对保存在本地的所有路由使用新的路由策略重新进行过滤，以实现在不中断]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的情况下，对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由表进行更新，并应用新的选路策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x241875903}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_355251201}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，保存所有来自对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的路由更新信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1201720388}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer 1.1.1.1 keep-all-routes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1756489757}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，保存所有来自对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的路由更新信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1608354225}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer 1.1.1.1 keep-all-routes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1916995978}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，保存所有来自对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的路由更新信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1890212964}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer 1::1 keep-all-routes]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x834179141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer capability-advertise route-refresh]{lang="EN-US"}**]{#struct_0_65458_x3406_1468731977}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[refresh bgp]{lang="EN-US"}**]{#struct_0_65458_x3406_2018756621}
:::

::: {#-754289861 .myid}
[]{#_Toc404788666}[]{#struct_0_65458_x3406_407583958}[]{#_Toc311730307}[]{#_Toc289500163}[]{#_Toc137867322}[]{#_Toc366153296}[]{#_Toc366167039}[]{#_Toc366220351}

**BGP \-- BGP配置命令 \-- peer label-route-capability**

------------------------------------------------------------------------

[**[peer label-route-capability]{lang="EN-US"}**]{#struct_0_65458_x3406_861668641}[命令用来使能与指定对等体]{style="font-family:
宋体"}[/]{lang="EN-US"}[对等体组交换带标签路由的能力。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer label-route-capability**]{lang="EN-US"}]{#struct_0_65458_x3406_x1254291520}[命令用来关闭与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换带标签路由的能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1785004774}

[**[peer]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *group-name* \| *ip-address* \[ *mask-length* \] } **label-route-capability**]{lang="EN-US"}]{#struct_0_65458_x3406_x972881720}

[**[undo]{lang="EN-US"}**[ **peer** { *group-name* \| *ip-address* \[ *mask-length* \] } **label-route-capability**]{lang="EN-US"}]{#struct_0_65458_x3406_x290288022}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1607436721}

[[不具有与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x1706816355}[对等体组交换带标签路由的能力。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_893800485}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1370184765}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1235679402}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x2024611139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1293280960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_336484593}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1607502257}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x931644917}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786690301}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x359657368}

[[跨域]{style="font-family:宋体"}[VPN OptionC]{lang="EN-US"}]{#struct_0_65458_x3406_x1850097008}[组网中，需要在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下执行本命令，使得本地设备和指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组可以交互带标签的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播路由，以便建立跨域的公网]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[6PE]{lang="EN-US"}]{#struct_0_65458_x3406_x861219027}[组网中，需要在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下执行本命令，使得本地设备和指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组可以交互带标签的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由，以便实现跨越]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[网络转发]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2028998557}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1804846750}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，使能与对等体]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[交换带标签]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1607961006}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer 2.2.2.2 label-route-capability]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x939288739}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，使能与对等体]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[交换带标签]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_599361222}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer 2.2.2.2 label-route-capability]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1188929737}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，使能与对等体]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[交换带标签]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由的能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x677829858}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer 2.2.2.2 label-route-capability]{lang="EN-US"}
:::

::: {#1677520439 .myid}
[]{#_Toc404788667}[]{#struct_0_65458_x3406_1236449039}

**BGP \-- BGP配置命令 \-- peer log-change**

------------------------------------------------------------------------

[**[peer log-change]{lang="EN-US"}**]{#struct_0_65458_x3406_x1244052267}[命令用来使能与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer log-change**]{lang="EN-US"}]{#struct_0_65458_x3406_198199167}[命令用来关闭与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1492434316}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **log-change**]{lang="EN-US"}]{#struct_0_65458_x3406_x18442815}

[**[undo]{lang="EN-US"}**[ **peer** { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **log-change**]{lang="EN-US"}]{#struct_0_65458_x3406_23175189}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_73649625}

[[与所有对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x1298715512}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1995963926}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1449327027}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_25820404}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x732919429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1257706294}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2062969095}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_833164512}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_2109990749}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786362624}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1895718843}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786952447}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1118533180}

[[通过]{style="font-family:宋体"}**[log-peer-change]{lang="EN-US"}**]{#struct_0_65458_x3406_x1367492992}[命令]{style="font-family:宋体"}[全局使能]{style="font-family:宋体"}[BGP]{lang="EN-US"}[日志记录功能，并执行本命令后，与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话建立以及断开时会生成日志信息，通过]{style="font-family:宋体"}**[display bgp peer ipv4 unicast log-info]{lang="EN-US"}**[命令或]{style="font-family:宋体"}**[display bgp peer ipv6 unicast log-info]{lang="EN-US"}**[命令可以查看记录的日志信息]{style="font-family:宋体"}[。生成的日志信息还将被发送到设备的信息中心，通过设置信息中心的参数，决定日志信息的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）]{style="font-family:宋体"}

[[如果全局关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_26595458}[日志记录功能，或关闭与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能，则]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话建立或断开时不会生成日志信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1561014801}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1592679399}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，使能与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1567801600}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 as-number 200]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 log-change]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1564621142}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，使能与对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的日志记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x329700438}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1.1.1.1 as-number 200]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1.1.1.1 log-change]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_239927678}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_1236383503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[log-peer-change]{lang="EN-US"}**]{#struct_0_65458_x3406_x1638168103}
:::

::: {#1287743658 .myid}
[]{#_Toc404788668}[]{#struct_0_65458_x3406_1608026542}

**BGP \-- BGP配置命令 \-- peer low-memory-exempt**

------------------------------------------------------------------------

[**[peer low-memory-exempt]{lang="EN-US"}**]{#struct_0_65458_x3406_x1126232797}[命令用来配置系统进入二级内存门限告警状态后，不断开与指定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间的会话。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer low-memory-exempt**]{lang="EN-US"}]{#struct_0_65458_x3406_1390226139}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2132000222}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **low-memory-exempt**]{lang="EN-US"}]{#struct_0_65458_x3406_x1046299308}

[**[undo]{lang="EN-US"}**[ **peer** { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **low-memory-exempt**]{lang="EN-US"}]{#struct_0_65458_x3406_x2017630067}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_45893856}

[[系统在二级内存门限告警状态下，会周期性地选择]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x141578726}[对等体，并断开与该对等体之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608092078}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x752796998}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1449932560}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_812341627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1536203830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x998062876}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1067465736}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1750637136}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786821370}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1608157614}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786690298}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1115651686}

[[当系统进入二级内存门限告警状态后，]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1551343972}[会周期性地选择一个]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体，断开与该对等体之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，直到系统内存恢复为止。用户可以通过本命令来避免在二级内存门限告警状态下，断开与指定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，以达到对特定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组进行保护的目的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1321387875}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x376520857}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置系统进入二级内存门限告警状态后，不断开与]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[之间的会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1171651995}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 as-number 200]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 low-memory-exempt]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1608223150}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置系统进入二级内存门限告警状态后，不断开与]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[之间的会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_41856917}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1.1.1.1 as-number 200]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1.1.1.1 low-memory-exempt]{lang="EN-US"}
:::

::: {#-122757061 .myid}
[]{#_Toc404788669}[]{#struct_0_65458_x3406_161209267}

**BGP \-- BGP配置命令 \-- peer next-hop-local**

------------------------------------------------------------------------

[**[peer next-hop-local]{lang="EN-US"}**]{#struct_0_65458_x3406_x965338123}[命令用来配置向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布路由时，将下一跳属性修改为自身的地址。]{style="font-family:宋体"}

[**[undo peer next-hop-local]{lang="EN-US"}**]{#struct_0_65458_x3406_1819048973}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608288686}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x386742021}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name \| ip-address* \[ *mask-length* \] } **next-hop-local**]{lang="EN-US"}]{#struct_0_65458_x3406_1305500633}

[**[undo peer]{lang="EN-US"}**[ { *group-name \| ip-address* \[ *mask-length* \] } **next-hop-local**]{lang="EN-US"}]{#struct_0_65458_x3406_1568809798}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1216404849}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name \| ipv6-address* \[ *prefix-length* \] } **next-hop-local**]{lang="EN-US"}]{#struct_0_65458_x3406_1443618256}

[**[undo peer]{lang="EN-US"}**[ { *group-name \| ipv6-address* \[ *prefix-length* \] } **next-hop-local**]{lang="EN-US"}]{#struct_0_65458_x3406_x371529625}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608354222}

[[向]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1917454730}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布的所有路由时，都将下一跳属性修改为自身的地址；对于]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[路由，向]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由时，将下一跳属性修改为自身的地址；对于其他地址族的路由，向]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由时，不修改下一跳属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1704164407}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1769685009}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x928106315}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1653151648}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1523011494}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1608419758}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_408042709}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x1786362617}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1598013629}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x220802969}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x825689379}

[[缺省情况下，路由器向]{style="font-family:宋体"}[IBGP]{lang="EN-US"}]{#struct_0_65458_x3406_2132744974}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布路由时，不修改下一跳属性。但有的时候为了保证]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体能够找到下一跳，可以通过本命令将下一跳属性修改为自身的地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x991021548}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1444958046}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由时，将下一跳属性修改为自身的地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1607436718}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test next-hop-local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1707406180}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，配置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由时，将下一跳属性修改为自身的地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1685073036}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer test next-hop-local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1825669367}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，配置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由时，将下一跳属性修改为自身的地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1259207892}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer test next-hop-local]{lang="EN-US"}
:::

::: {#1865672028 .myid}
[]{#_Toc404788670}[]{#struct_0_65458_x3406_1607502254}[]{#_Toc330386832}[]{#_Toc331168097}

**BGP \-- BGP配置命令 \-- peer password**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**[ **password**]{lang="EN-US"}]{#struct_0_65458_x3406_x931710453}[命令用来为指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[**[undo peer]{lang="EN-US"}**[ **password**]{lang="EN-US"}]{#struct_0_65458_x3406_783278771}[命令用来取消为指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x675504896}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **password** { **cipher** \| **simple** } *password*]{lang="EN-US"}]{#struct_0_65458_x3406_1599001810}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **password**]{lang="EN-US"}]{#struct_0_65458_x3406_x491592686}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2047787816}

[[不进行]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1774581088}[的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1607961007}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x939354275}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_999165901}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1289641119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_138537930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x903788712}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x790915490}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1500415073}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x220737432}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1608026543}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x220606360}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_65458_x3406_x1126298333}[：以密文形式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_65458_x3406_1318156965}[：以明文形式设置密钥。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_65458_x3406_x1749225922}[：密钥，字符串形式，区分大小写。如果以密文形式设置密钥，则]{style="font-family:宋体"}*[password]{lang="EN-US"}*[为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[137]{lang="EN-US"}[个字符的密文字符串；如果以明文形式设置密钥，则]{style="font-family:宋体"}*[password]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[80]{lang="EN-US"}[个字符的明文字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_198179454}

[[通过为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1975957119}[对等体配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证，可以在以下两方面提高]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的安全性：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为]{style="font-family:宋体"}]{#struct_0_65458_x3406_941953431}[BGP]{lang="EN-US"}[建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证，只有两台路由器配置的密钥相同时，才能建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，从而避免与非法的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[传递]{style="font-family:宋体"}]{#struct_0_65458_x3406_1608092079}[BGP]{lang="EN-US"}[报文时，对封装]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文段进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[运算，从而保证]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文不会被篡改。]{style="font-family:宋体"}

[[需要注意的是，以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x752731462}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_614497810}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1900923856}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置本地路由器]{style="font-family:宋体"}[10.1.100.1]{lang="EN-US"}[与对等体]{style="font-family:宋体"}[10.1.100.2]{lang="EN-US"}[之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证，密钥为明文字符串]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x218845651}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 10.1.100.2 password simple aabbcc]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_458174701}[在对等体上也需要进行类似的配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1899741349}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 10.1.100.1 password simple aabbcc]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1608157615}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置本地路由器]{style="font-family:宋体"}[10.1.100.1]{lang="EN-US"}[与对等体]{style="font-family:宋体"}[10.1.100.2]{lang="EN-US"}[之间的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证，密钥为明文字符串]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1115586150}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 10.1.100.2 password simple aabbcc]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1074338072}[在对等体上也需要进行类似的配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1976507177}

[\[Sysname\] bgp 200]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 10.1.100.1 password simple aabbcc]{lang="EN-US"}
:::

::: {#-1529250976 .myid}
[]{#_Toc404788671}[]{#struct_0_65458_x3406_x196052122}

**BGP \-- BGP配置命令 \-- peer preferred-value**

------------------------------------------------------------------------

[**[peer preferred-value]{lang="EN-US"}**]{#struct_0_65458_x3406_772291597}[命令用来为从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由分配首选值。]{style="font-family:宋体"}

[**[undo peer preferred-value]{lang="EN-US"}**]{#struct_0_65458_x3406_1608223151}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_41791381}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1006665778}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name \|* ]{lang="EN-US"}*[ip-address ]{lang="EN-US"}*[\[ *mask-length* \] ]{lang="EN-US"}[} **preferred-value** *value*]{lang="EN-US"}]{#struct_0_65458_x3406_90723236}

[**[undo]{lang="EN-US"}**[ **peer** { *group-name \|* ]{lang="EN-US"}*[ip-address ]{lang="EN-US"}*[\[ *mask-length* \] ]{lang="EN-US"}[} **preferred-value**]{lang="EN-US"}]{#struct_0_65458_x3406_2123274960}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1895082837}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **preferred-value** *value*]{lang="EN-US"}]{#struct_0_65458_x3406_x1641775237}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **preferred-value**]{lang="EN-US"}]{#struct_0_65458_x3406_1608288687}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x386807557}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **preferred-value** *value*]{lang="EN-US"}]{#struct_0_65458_x3406_865116986}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **preferred-value**]{lang="EN-US"}]{#struct_0_65458_x3406_952463099}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_20861246}

[[从对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_1587165631}[对等体组接收的路由的首选值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1568555430}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_292108430}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608354223}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1917389194}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1821633610}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x584061449}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1260173468}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1584968064}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x220278682}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1705562488}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x220802965}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_65458_x3406_x281789928}[：为路由分配的首选值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1608419759}

[[当从不同对等体都学习到了到达同一目的网络的路由时，可以使用本命令为从不同对等体学习的路由分配不同的首选值，首选值最大的路由将优先被选作最优路由，从而达到控制]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_408108245}[路径选择的目的。]{style="font-family:宋体"}

[[路由首选值只用于本地路由器的路由选择，不会通告给对等体，只具有本地意义。]{style="font-family:宋体"}]{#struct_0_65458_x3406_844855606}

[[既可以通过本命令配置路由的首选值，也可以通过路由策略中的]{style="font-family:宋体"}**[apply preferred-value]{lang="EN-US"}**]{#struct_0_65458_x3406_820093302}[命令为路由配置首选值。如果同时配置了二者，则优先选择路由策略中配置的首选值。只有当路由策略中没有配置首选值，或没有配置路由策略时，才会选取]{style="font-family:宋体"}**[peer preferred-value]{lang="EN-US"}**[命令设置的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_881248769}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x406220066}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置来自对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的路由的首选值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1607436719}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer 1.1.1.1 preferred-value 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1707340644}[在]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族视图下，配置来自对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的路由的首选值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x741310487}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family vpnv4]{lang="EN-US"}

[\[Sysname-bgp-vpnv4\] peer 1.1.1.1 preferred-value 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1735061244}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置来自对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的路由的首选值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x538472547}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer 1::1 preferred-value 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x169161780}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply preferred-value]{lang="EN-US"}**]{#struct_0_65458_x3406_1607502255}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x931775989}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}
:::

::: {#1193629369 .myid}
[]{#_Toc404788672}[]{#struct_0_65458_x3406_1212521399}[]{#_Toc316655972}[]{#_Toc312414490}[]{#_Toc312402369}[]{#_Toc180224219}

**BGP \-- BGP配置命令 \-- peer prefix-list**

------------------------------------------------------------------------

[**[peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_879398896}[命令用来为对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组设置基于地址前缀列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由过滤策略。]{style="font-family:宋体"}

[**[undo peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x483537270}[命令用来取消已有的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1983095455}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_594984572}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **prefix-list** *prefix-list-name* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x962210917}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] } **prefix-list** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1120922345}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_341325956}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **prefix-list** *ipv6-prefix-name* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1880829084}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **prefix-list** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_577848885}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1862238131}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **prefix-list** *ipv6-prefix-name* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1355329331}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **prefix-list** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1122653556}

[[BGP VPNv6]{lang="EN-US"}]{#struct_0_65458_x3406_385782122}[地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **prefix-list** *ipv6-prefix-name* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1120856809}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **prefix-list** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x461386880}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1041554573}

[[没有设置基于地址前缀列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1470533438}[路由过滤策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_463710623}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_87037571}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1637249732}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_80758168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1120791273}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_97483140}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1838834328}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_2006335913}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x623563208}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1820286412}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x624087495}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_65458_x3406_2052344555}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[ipv6-prefix-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x298957444}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_65458_x3406_x1120725737}[：对向指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布的路由应用过滤策略。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_65458_x3406_x2108874314}[：对从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由[]{#_Hlt2481476}应用过滤策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_668402690}

[[配置]{style="font-family:宋体"}**[peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x205569246}[命令时需要同时在系统视图下通过]{style="font-family:宋体"}**[ip prefix-list]{lang="EN-US"}**[命令配置对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表或通过]{style="font-family:宋体"}**[ipv6 prefix-list]{lang="EN-US"}**[命令配置对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表。如果本命令中指定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址前缀列表尚未创建，则所有路由均通过过滤。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x200865094}

[]{#struct_0_65458_x3406_66730228}[]{#_Toc138238286}[]{#_Toc94930954}[]{#_Toc94586686}[]{#_Toc60036299}[]{#_Toc53707243}[]{#_Toc53518716}[]{#_Toc50837023}[\# ]{lang="EN-US"}[在]{style="font-family:
宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置利用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[list1]{lang="EN-US"}[过滤向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_181472667}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test prefix-list list1 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1120660201}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置利用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[list1]{lang="EN-US"}[过滤向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1905841443}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer test prefix-list list1 export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1790393772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy export]{lang="EN-US"}**]{#struct_0_65458_x3406_x14484737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy ]{lang="EN-US"}**]{#struct_0_65458_x3406_400673480}**[import]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip ]{lang="EN-US"}[prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_1048830392}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_65458_x3406_x2053815595}**[v6]{lang="EN-US"}[ ]{lang="EN-US"}[prefix-list]{lang="EN-US"}**[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer as-path-acl]{lang="EN-US"}**]{#struct_0_65458_x3406_x1120594665}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1569504734}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x97901163}
:::

::: {#-2047278166 .myid}
[]{#_Toc404788673}[]{#struct_0_65458_x3406_x727610111}

**BGP \-- BGP配置命令 \-- peer public-as-only**

------------------------------------------------------------------------

[**[peer public-as-only]{lang="EN-US"}**]{#struct_0_65458_x3406_2071462298}[命令用来配置向指定]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发送]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息时只携带公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，不携带私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[**[undo peer public-as-only]{lang="EN-US"}**]{#struct_0_65458_x3406_x2066738631}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_187481500}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_544575952}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name \|* ]{lang="EN-US"}*[ip-address]{lang="EN-US"}*[ \[ *mask-length* \] } **public-as-only**]{lang="EN-US"}]{#struct_0_65458_x3406_x1120529129}

[**[undo]{lang="EN-US"}**[ **peer** { *group-name \|* ]{lang="EN-US"}*[ip-address ]{lang="EN-US"}*[\[ *mask-length* \] ]{lang="EN-US"}[} **public-as-only**]{lang="EN-US"}]{#struct_0_65458_x3406_x58282042}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1017791855}[单播地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **public-as-only**]{lang="EN-US"}]{#struct_0_65458_x3406_1126797358}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **public-as-only**]{lang="EN-US"}]{#struct_0_65458_x3406_x265240855}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1753931619}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **public-as-only**]{lang="EN-US"}]{#struct_0_65458_x3406_1741178382}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **public-as-only**]{lang="EN-US"}]{#struct_0_65458_x3406_x1120463593}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1148447732}

[[向]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1944134043}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发送]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息时，既可以携带公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，又可以携带私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_293701972}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_786839769}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1302358571}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1302251748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x238184245}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1121446633}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1207390710}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1689134094}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x623890889}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1799178677}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x623759817}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x190794822}

[[私有]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x419301194}[号是内部使用的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，范围为]{style="font-family:宋体"}[64512]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号主要用于测试网络，一般情况下不需要在公共网络中传播。]{style="font-family:宋体"}

[[执行本命令后：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1885625770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果向]{style="font-family:宋体"}]{#struct_0_65458_x3406_x907624912}[EBGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息中]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性只包括私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则删除私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号后，将]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息发送给对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1121381097}[AS_PATH]{lang="EN-US"}[属性中同时带有公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号和私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则本命令不生效，即不删除私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，直接将]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息发送给对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2078433412}[AS_PATH]{lang="EN-US"}[属性中包括对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则本命令不生效，即不删除私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，直接将]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息发送给对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组。]{style="font-family:宋体"}

[[需要注意的是，本命令只适用于]{style="font-family:宋体"}[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x785376343}[对等体和对等体组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1879649754}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1074469709}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置向]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息时只携带公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，不携带私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_70458128}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test public-as-only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1409894949}[在]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族视图下，配置向]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息时只携带公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，不携带私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1120922344}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family vpnv4]{lang="EN-US"}

[\[Sysname-bgp-vpnv4\] peer test public-as-only]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1907409897}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置向]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发送]{style="font-family:宋体"}[BGP]{lang="EN-US"}[更新消息时只携带公有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，不携带私有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1647262944}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer test public-as-only]{lang="EN-US"}
:::

::: {#904068986 .myid}
[]{#_Toc404788674}[]{#struct_0_65458_x3406_x1909826843}[]{#_Toc263170156}[]{#_Toc261504248}[]{#_Toc180224226}[]{#_Toc138238292}[]{#_Toc32467761}[]{#_Toc32464230}[]{#_Toc30500474}[]{#_Toc26173966}[]{#_Toc290298153}[]{#_Toc290298154}[]{#_Toc290298155}[]{#_Toc290298156}[]{#_Toc290298157}[]{#_Toc290298158}[]{#_Toc290298159}[]{#_Toc290298160}[]{#_Toc290298161}[]{#_Toc290298162}[]{#_Toc290298163}[]{#_Toc290298164}[]{#_Toc290298165}[]{#_Toc290298166}[]{#_Toc290298167}[]{#_Toc290298168}[]{#_Toc290298169}[]{#_Toc290298170}[]{#_Toc290298172}[]{#_Toc290298173}[]{#_Toc290298174}[]{#_Toc290298178}[]{#_Toc290298179}[]{#_Toc290298180}[]{#_Toc290298181}[]{#_Toc290298182}[]{#_Toc290298183}[]{#_Toc290298184}[]{#_Toc290298185}[]{#_Toc290298186}[]{#_Toc290298187}[]{#_Toc290298188}[]{#_Toc290298189}[]{#_Toc290298190}[]{#_Toc290298191}[]{#_Toc290298192}[]{#_Toc290298193}[]{#_Toc290298194}[]{#_Toc290298195}[]{#_Toc290298197}[]{#_Toc290298198}[]{#_Toc290298199}[]{#_Toc290298203}[]{#_Toc290298204}[]{#_Toc290298205}[]{#_Toc290298206}[]{#_Toc290298207}[]{#_Toc290298208}[]{#_Toc290298209}[]{#_Toc290298210}[]{#_Toc290298211}[]{#_Toc290298212}[]{#_Toc290298213}[]{#_Toc290298214}[]{#_Toc290298215}[]{#_Toc290298216}[]{#_Toc290298217}[]{#_Toc290298218}[]{#_Toc290298219}[]{#_Toc290298221}[]{#_Toc290298223}[]{#_Toc290298224}[]{#_Toc290298228}[]{#_Toc290298229}[]{#_Toc290298230}[]{#_Toc290298231}[]{#_Toc290298232}[]{#_Toc290298233}[]{#_Toc290298234}[]{#_Toc290298235}[]{#_Toc290298236}[]{#_Toc290298237}[]{#_Toc290298238}[]{#_Toc290298239}[]{#_Toc290298240}[]{#_Toc290298241}[]{#_Toc290298242}[]{#_Toc290298243}[]{#_Toc290298244}[]{#_Toc290298245}[]{#_Toc290298247}[]{#_Toc290298250}[]{#_Toc290298254}[]{#_Toc290298256}[]{#_Toc290298257}[]{#_Toc290298258}[]{#_Toc290298259}[]{#_Toc290298260}[]{#_Toc290298261}[]{#_Toc290298262}[]{#_Toc290298263}[]{#_Toc290298264}[]{#_Toc290298265}[]{#_Toc290298266}[]{#_Toc290298267}[]{#_Toc290298268}[]{#_Toc290298269}[]{#_Toc290298270}[]{#_Toc290298271}[]{#_Toc290298272}[]{#_Toc290298273}[]{#_Toc290298274}[]{#_Toc290298275}[]{#_Toc290298278}[]{#_Toc290298279}[]{#_Toc290298284}[]{#_Toc290298285}[]{#_Toc290298286}[]{#_Toc290298287}[]{#_Toc290298288}[]{#_Toc290298289}[]{#_Toc290298290}[]{#_Toc290298291}[]{#_Toc290298292}[]{#_Toc290298293}[]{#_Toc290298294}[]{#_Toc290298295}[]{#_Toc290298296}[]{#_Toc290298297}[]{#_Toc290298298}[]{#_Toc290298299}[]{#_Toc290298300}[]{#_Toc290298303}[]{#_Toc290298304}[]{#_Toc290298305}[]{#_Toc290298308}[]{#_Toc290298309}[]{#_Toc290298311}[]{#_Toc290298312}[]{#_Toc290298313}[]{#_Toc290298314}[]{#_Toc290298315}[]{#_Toc290298316}[]{#_Toc290298317}[]{#_Toc290298318}[]{#_Toc290298319}[]{#_Toc290298320}[]{#_Toc290298321}[]{#_Toc290298322}[]{#_Toc290298323}[]{#_Toc290298324}[]{#_Toc290298325}[]{#_Toc290298326}[]{#_Toc290298327}[]{#_Toc290298328}[]{#_Toc290298329}[]{#_Toc290298332}[]{#_Toc290298333}[]{#_Toc290298337}[]{#_Toc290298338}[]{#_Toc290298339}[]{#_Toc290298340}[]{#_Toc290298341}[]{#_Toc290298342}[]{#_Toc290298343}[]{#_Toc290298344}[]{#_Toc290298345}[]{#_Toc290298346}[]{#_Toc290298347}[]{#_Toc290298348}[]{#_Toc290298349}[]{#_Toc290298350}[]{#_Toc290298351}[]{#_Toc290298352}[]{#_Toc290298353}[]{#_Toc290298354}[]{#_Toc290298356}[]{#_Toc290298357}[]{#_Toc290298359}[]{#_Toc290298360}[]{#_Toc290298361}[]{#_Toc290298363}[]{#_Toc290298364}[]{#_Toc290298365}[]{#_Toc290298366}[]{#_Toc290298367}[]{#_Toc290298368}[]{#_Toc290298369}[]{#_Toc290298370}[]{#_Toc290298371}[]{#_Toc290298372}[]{#_Toc290298373}[]{#_Toc290298374}[]{#_Toc290298375}[]{#_Toc290298376}[]{#_Toc290298377}[]{#_Toc290298380}[]{#_Toc290298381}[]{#_Toc290298385}[]{#_Toc290298386}[]{#_Toc290298387}[]{#_Toc290298388}[]{#_Toc290298389}[]{#_Toc290298390}[]{#_Toc290298391}[]{#_Toc290298392}[]{#_Toc290298393}[]{#_Toc290298394}[]{#_Toc290298395}[]{#_Toc290298396}[]{#_Toc290298397}[]{#_Toc290298398}[]{#_Toc290298399}[]{#_Toc290298400}[]{#_Toc290298401}[]{#_Toc290298404}[]{#_Toc290298405}[]{#_Toc290298406}[]{#_Toc290298407}[]{#_Toc290298408}[]{#_Toc290298410}[]{#_Toc290298411}[]{#_Toc290298412}[]{#_Toc290298413}[]{#_Toc290298416}[]{#_Toc290298417}[]{#_Toc290298418}[]{#_Toc290298419}[]{#_Toc290298420}[]{#_Toc290298421}[]{#_Toc290298423}[]{#_Toc290298424}[]{#_Toc290298425}[]{#_Toc290298426}[]{#_Toc290298427}[]{#_Toc290298428}[]{#_Toc290298429}[]{#_Toc290298430}[]{#_Toc290298431}[]{#_Toc290298432}[]{#_Toc290298433}[]{#_Toc290298434}[]{#_Toc290298435}[]{#_Toc290298436}[]{#_Toc290298437}[]{#_Toc290298438}[]{#_Toc290298439}[]{#_Toc290298442}[]{#_Toc290298443}[]{#_Toc290298446}[]{#_Toc290298447}[]{#_Toc290298448}[]{#_Toc290298453}[]{#_Toc290298454}[]{#_Toc290298455}[]{#_Toc290298456}[]{#_Toc290298457}[]{#_Toc290298458}[]{#_Toc290298459}[]{#_Toc290298460}[]{#_Toc290298461}[]{#_Toc290298462}[]{#_Toc290298463}[]{#_Toc290298464}[]{#_Toc290298465}[]{#_Toc290298466}[]{#_Toc290298467}[]{#_Toc290298468}[]{#_Toc290298469}[]{#_Toc290298470}[]{#_Toc290298471}[]{#_Toc290298473}[]{#_Toc290298476}[]{#_Toc290298477}[]{#_Toc290298483}[]{#_Toc290298484}[]{#_Toc290298485}[]{#_Toc290298486}[]{#_Toc290298487}[]{#_Toc290298488}[]{#_Toc290298489}[]{#_Toc290298490}[]{#_Toc290298491}[]{#_Toc290298492}[]{#_Toc290298493}[]{#_Toc290298494}[]{#_Toc290298495}[]{#_Toc290298496}[]{#_Toc290298497}[]{#_Toc290298498}[]{#_Toc290298499}[]{#_Toc290298503}[]{#_Toc290298508}[]{#_Toc290298509}[]{#_Toc290298510}[]{#_Toc290298511}[]{#_Toc290298512}[]{#_Toc290298513}[]{#_Toc290298514}[]{#_Toc290298515}[]{#_Toc290298516}[]{#_Toc290298517}[]{#_Toc290298518}[]{#_Toc290298519}[]{#_Toc290298520}[]{#_Toc290298521}[]{#_Toc290298522}[]{#_Toc290298523}[]{#_Toc290298526}[]{#_Toc290298527}[]{#_Toc290298528}[]{#_Toc290298531}[]{#_Toc290298532}[]{#_Toc290298533}[]{#_Toc290298537}[]{#_Toc290298538}[]{#_Toc290298539}[]{#_Toc290298540}[]{#_Toc290298541}[]{#_Toc290298542}[]{#_Toc290298543}[]{#_Toc290298544}[]{#_Toc290298545}[]{#_Toc290298546}[]{#_Toc290298547}[]{#_Toc290298548}[]{#_Toc290298549}[]{#_Toc290298550}[]{#_Toc290298551}[]{#_Toc290298552}[]{#_Toc290298553}[]{#_Toc290298554}[]{#_Toc290298557}[]{#_Toc290298558}[]{#_Toc290298559}[]{#_Toc290298562}[]{#_Toc290298563}[]{#_Toc290298564}[]{#_Toc290298568}[]{#_Toc290298569}[]{#_Toc290298570}[]{#_Toc290298571}[]{#_Toc290298572}[]{#_Toc290298573}[]{#_Toc290298574}[]{#_Toc290298575}[]{#_Toc290298576}[]{#_Toc290298577}[]{#_Toc290298578}[]{#_Toc290298579}[]{#_Toc290298580}[]{#_Toc290298581}[]{#_Toc290298582}[]{#_Toc290298583}[]{#_Toc290298584}[]{#_Toc290298585}[]{#_Toc290298586}[]{#_Toc290298587}[]{#_Toc290298590}[]{#_Toc290298592}[]{#_Toc290298595}[]{#_Toc290298596}[]{#_Toc290298597}[]{#_Toc290298601}[]{#_Toc290298602}[]{#_Toc290298603}[]{#_Toc290298604}[]{#_Toc290298605}[]{#_Toc290298606}[]{#_Toc290298607}[]{#_Toc290298608}[]{#_Toc290298609}[]{#_Toc290298610}[]{#_Toc290298611}[]{#_Toc290298612}[]{#_Toc290298613}[]{#_Toc290298614}[]{#_Toc290298615}[]{#_Toc290298616}[]{#_Toc290298617}[]{#_Toc290298618}[]{#_Toc290298619}[]{#_Toc290298622}[]{#_Toc290298624}[]{#_Toc290298627}[]{#_Toc290298629}[]{#_Toc290298633}

**BGP \-- BGP配置命令 \-- peer reflect-client**

------------------------------------------------------------------------

[**[peer reflect-client]{lang="EN-US"}**]{#struct_0_65458_x3406_x1264815074}[命令用来配置本机作为路由反射器，对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组作为路由反射器的客户机。]{style="font-family:宋体"}

[**[undo peer reflect-client]{lang="EN-US"}**]{#struct_0_65458_x3406_x1880677621}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1120856808}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x2027470821}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv4 MDT]{lang="EN-US"}[地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **reflect-client**]{lang="EN-US"}]{#struct_0_65458_x3406_784617994}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **reflect-client**]{lang="EN-US"}]{#struct_0_65458_x3406_x219528288}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x751405218}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **reflect-client**]{lang="EN-US"}]{#struct_0_65458_x3406_x36787326}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **reflect-client**]{lang="EN-US"}]{#struct_0_65458_x3406_x944210025}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_970408413}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **reflect-client**]{lang="EN-US"}]{#struct_0_65458_x3406_970277341}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \|  *ipv6-address* \[ *prefix-length* \] } **reflect-client**]{lang="EN-US"}]{#struct_0_65458_x3406_970670557}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x286650198}

[[没有配置路由反射器及其客户机。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1120791272}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1468600801}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_64333249}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv4 MDT]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x781897206}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2144903998}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1590542696}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_516452058}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1120725736}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x542790373}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_941930909}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1361908081}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_942061981}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1317098027}

[[路由反射用来解决]{style="font-family:宋体"}[IBGP]{lang="EN-US"}]{#struct_0_65458_x3406_86107239}[对等体需要全连接的问题。在一个]{style="font-family:宋体"}[AS]{lang="EN-US"}[内，一台路由器作为]{style="font-family:宋体"}[RR]{lang="EN-US"}[（]{style="font-family:宋体"}[Route Reflector]{lang="EN-US"}[，路由反射器），其它路由器作为客户机（]{style="font-family:宋体"}[Client]{lang="EN-US"}[）与路由反射器建立]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[连接。路由反射器在客户机之间传递（反射）路由信息，而客户机之间不需要建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1555798109}

[]{#_Toc138238293}[]{#_Toc94930962}[]{#_Toc94586694}[]{#_Toc60036306}[]{#_Toc53707250}[]{#_Toc53518723}[]{#_Toc50837030}[]{#_Toc43895294}[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x986396281}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置本地设备作为路由反射器，]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[作为路由反射器的客户机。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1120660200}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test reflect-client]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x339757502}[在]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族视图下，配置本地设备作为路由反射器，]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[作为路由反射器的客户机。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x388791067}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family vpnv4]{lang="EN-US"}

[\[Sysname-bgp-vpnv4\] peer test reflect-client]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1469561254}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置本地设备作为路由反射器，]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[作为路由反射器的客户机。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x671627327}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer test reflect-client]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x925611579}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，配置本地设备作为路由反射器，]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[作为路由反射器的客户机。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1120594664}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] peer test reflect-client]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1402375657}[在]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族视图下，配置本地设备作为路由反射器，]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[作为路由反射器的客户机。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1401982441}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 mdt]{lang="EN-US"}

[\[Sysname-bgp-mdt\] peer test reflect-client]{lang="EN-US"}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_65458_x3406_3420793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reflect between-clients]{lang="EN-US"}**]{#struct_0_65458_x3406_2066186677}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reflector cluster-id]{lang="EN-US"}**]{#struct_0_65458_x3406_x265878907}
:::

::: {#1064371803 .myid}
[]{#_Toc404788675}[]{#struct_0_65458_x3406_x150766352}[]{#_Toc263170157}[]{#_Toc261504249}[]{#_Toc180224227}

**BGP \-- BGP配置命令 \-- peer route-limit**

------------------------------------------------------------------------

[**[peer route-limit]{lang="EN-US"}**]{#struct_0_65458_x3406_x1552206073}[命令用来设置允许从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组收到的路由数量。]{style="font-family:宋体"}

[**[undo peer route-limit]{lang="EN-US"}**]{#struct_0_65458_x3406_1175640770}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x178965314}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1642831690}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] } **route-limit** *prefix-number* \[ { ]{lang="EN-US"}]{#struct_0_65458_x3406_x1120529128}[[alert-only ]{lang="EN-US"}]{.commandkeywordsCharCharChar}[\|]{lang="EN-US"}[[ discard ]{lang="EN-US"}]{.commandkeywordsCharCharChar}[\| ]{lang="EN-US"}[[reconnect]{lang="EN-US"}]{.commandkeywordsCharCharChar}[ *reconnect-time* } \| *percentage-value* \] \*]{lang="EN-US"}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] } **route-limit**]{lang="EN-US"}]{#struct_0_65458_x3406_1507801899}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1120463592}[单播地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **route-limit** *prefix-number* \[ { **alert-only** \| ]{lang="EN-US"}]{#struct_0_65458_x3406_417636209}[[discard ]{lang="EN-US"}]{.commandkeywordsCharCharChar}[\| **reconnect** *reconnect-time* } \| *percentage-value* \] \*]{lang="EN-US"}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **route-limit**]{lang="EN-US"}]{#struct_0_65458_x3406_1660422434}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1402310122}[组播地址族视图：]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **route-limit** *prefix-number* \[ { **alert-only** \| ]{lang="EN-US"}]{#struct_0_65458_x3406_x1401916906}[[discard]{lang="EN-US"}]{.commandkeywordsCharCharChar}[ \| **reconnect** *reconnect-time* } \| *percentage-value* \] \*]{lang="EN-US"}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **route-limit**]{lang="EN-US"}]{#struct_0_65458_x3406_x1402441195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1121446632}

[[不限制从对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x1521492645}[对等体组接收的路由数量。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1749881569}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_2076683597}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2060083876}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1863674248}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_871404576}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1332970364}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1121381096}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x512349471}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_941996444}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1697383057}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_942061980}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[prefix-numb]{lang="EN-US"}*[er]{lang="EN-US"}]{#struct_0_65458_x3406_x1120856811}[：允许路由器接收的路由的数量，取值范围与设备的型号有关，请以设备的实际情况为准。如果没有指定]{style="font-family:宋体"}[[alert-only]{lang="EN-US"}]{.commandkeywords}[、]{style="font-family:宋体"}[[discard]{lang="EN-US"}]{.commandkeywordsCharCharChar}[和]{style="font-family:宋体"}**[reconnect]{lang="EN-US"}**[参数，则]{style="font-family:宋体"}[从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由的数量大于]{style="font-family:宋体"}*[prefix-numb]{lang="EN-US"}*[er]{lang="EN-US"}[值时，路由器自动断开与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的会话。对于]{style="font-family:宋体"}[BGP]{lang="EN-US"}[动态对等体，本地设备不会尝试与其重新建立会话，但是接收到对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话建立请求后会接受该请求；对于其他非]{style="font-family:宋体"}[BGP]{lang="EN-US"}[动态对等体，本地设备不会尝试与其重新建立会话，可以通过]{style="font-family:宋体"}**[reset bgp]{lang="EN-US"}**[命令重启]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，使得本地设备与对等体重新建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[[alert-only]{lang="EN-US"}]{.commandkeywords}]{#struct_0_65458_x3406_x1120660203}[：如果路由器从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由的数量大于]{style="font-family:宋体"}*[prefix-numb]{lang="EN-US"}*[er]{lang="EN-US"}[值，仅打印日志信息，路由器保持与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的会话，并可以继续接收路由。]{style="font-family:宋体"}

[**[discard]{lang="EN-US"}**]{#struct_0_65458_x3406_x1120594667}[：如果路由器从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由的数量大于]{style="font-family:宋体"}*[prefix-numb]{lang="EN-US"}*[er]{lang="EN-US"}[值，路由器保持与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的会话，但丢弃超出限制的路由，并打印日志信息。从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由数量小于]{style="font-family:宋体"}*[prefix-numb]{lang="EN-US"}*[er]{lang="EN-US"}[后，路由器可以继续接收路由。如果用户想恢复之前丢弃的路由，则需要执行]{style="font-family:宋体"}**[refresh bgp import]{lang="EN-US"}**[命令请求对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组重新发布路由。]{style="font-family:宋体"}

[**[reconnect]{lang="EN-US"}***[ reconnect-time]{lang="EN-US"}*]{#struct_0_65458_x3406_x1120463595}[：如果路由器从指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由的数量大于]{style="font-family:宋体"}*[prefix-numb]{lang="EN-US"}*[er]{lang="EN-US"}[值，则等待指定的时间间隔后重新与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组建立会话。]{style="font-family:宋体"}*[reconnect-time]{lang="EN-US"}*[为路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组重建会话的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。对于]{style="font-family:宋体"}[BGP]{lang="EN-US"}[动态对等体，本参数不会生效。]{style="font-family:宋体"}

[*[percentage-value]{lang="EN-US"}*]{#struct_0_65458_x3406_x1120922346}[：配置路由器产生日志信息的阈值（即路由器接收的路由数量与]{style="font-family:宋体"}*[prefix-numb]{lang="EN-US"}*[er]{lang="EN-US"}[的百分比达到]{style="font-family:宋体"}*[percentage-value]{lang="EN-US"}*[时，路由器将产生日志信息），取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[75]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1224757985}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1120791274}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，设置允许从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[收到的路由数量为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。如果从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[收到的路由数量超过]{style="font-family:宋体"}[10000]{lang="EN-US"}[，则断开与该对等体的会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x662031747}

[\[Sysname\] bgp 109]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer 1.1.1.1 route-limit 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1120660202}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，设置允许从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[收到的路由数量为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。如果从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[收到的路由数量超过]{style="font-family:宋体"}[10000]{lang="EN-US"}[，则断开与该对等体的会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_823041912}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer 1.1.1.1 route-limit 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1120529130}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，设置允许从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[收到的路由数量为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。如果从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[收到的路由数量超过]{style="font-family:宋体"}[10000]{lang="EN-US"}[，则断开与该对等体的会话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1151506003}

[\[Sysname\] bgp 109]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] peer 1::1 route-limit 10000]{lang="EN-US"}
:::

::: {#416978344 .myid}
[]{#_Toc263170159}[]{#_Toc261504251}[]{#_Toc180224229}[]{#_Toc404788676}[]{#struct_0_65458_x3406_1574594764}[]{#_Toc316655976}[]{#_Toc312414494}[]{#_Toc312402373}[]{#_Toc180224228}

**BGP \-- BGP配置命令 \-- peer route-policy**

------------------------------------------------------------------------

[**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_681641677}[命令用来对来自对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的路由或发布给对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的路由应用路由策略，以便对路由进行过滤、修改路由的属性等。]{style="font-family:宋体"}

[**[undo peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1878863783}[命令用来取消已有设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1120463594}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1580435623}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **route-policy** *route-policy-name* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1123794422}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **route-policy** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1570217707}

[[BGP-VPN VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_1052554468}[地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **route-policy** *route-policy-name* **import**]{lang="EN-US"}]{#struct_0_65458_x3406_1655132668}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] } **route-policy** **import**]{lang="EN-US"}]{#struct_0_65458_x3406_1071201217}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x1650933587}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **route-policy** *route-policy-name* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1121446634}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **route-policy** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_1966905597}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_x735340107}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **route-policy** *route-policy-name* { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x1189092783}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ipv6-address* \[ *prefix-length* \] } **route-policy** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_65458_x3406_x734758202}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_334595981}

[[没有为对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_1416057761}[对等体组指定路由策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1121381098}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1675148885}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP-VPN VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_107044940}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_344922896}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_329310184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x39593099}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_402138771}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1219122654}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x729773727}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1120922349}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x729642655}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1271812152}[：路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_65458_x3406_x2003682989}[：对向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布的路由应用路由策略。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_65458_x3406_30590112}[：对从对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收的路由应用路由策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x369647497}

[[配置]{style="font-family:宋体"}**[peer route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1606701514}[命令时需要同时在系统视图下通过]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[命令配置对应的路由策略。如果本命令中指定的路由策略尚未创建，则所有路由均通过过滤。]{style="font-family:宋体"}

[[需要注意的是，如果在本命令指定的路由策略中配置了]{style="font-family:宋体"}**[if-match interface]{lang="EN-US"}**]{#struct_0_65458_x3406_1366661154}[命令，则在路由过滤时忽略此匹配规则，认为所有路由均通过该规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x164444128}

[]{#struct_0_65458_x3406_x1120856813}[]{#_Toc138238295}[]{#_Toc32467748}[]{#_Toc32464217}[]{#_Toc30500461}[\# ]{lang="EN-US"}[在]{style="font-family:
宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置对向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由应用名为]{style="font-family:宋体"}[test-policy]{lang="EN-US"}[的路由策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1057708430}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer test route-policy test-policy export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1372768651}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置对向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布的路由应用名为]{style="font-family:宋体"}[test-policy]{lang="EN-US"}[的路由策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x907374637}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] peer test route-policy test-policy export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1789475984}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy export]{lang="EN-US"}**]{#struct_0_65458_x3406_x39755407}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy ]{lang="EN-US"}**]{#struct_0_65458_x3406_x1120791277}**[import]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer as-path-acl]{lang="EN-US"}**]{#struct_0_65458_x3406_2066851608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer filter-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_x1019364642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer prefix-list]{lang="EN-US"}**]{#struct_0_65458_x3406_x1189886542}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-policy]{lang="EN-US"}**]{#struct_0_65458_x3406_1491533362}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{style="font-family:宋体"}
:::

::: {#671317195 .myid}
[]{#_Toc404788677}[]{#struct_0_65458_x3406_x2043217357}[]{#_Hlt2576466}

**BGP \-- BGP配置命令 \-- peer route-update-interval**

------------------------------------------------------------------------

[**[peer route-update-interval]{lang="EN-US"}**]{#struct_0_65458_x3406_1731692009}[命令用来配置向指定对等体]{style="font-family:
宋体"}[/]{lang="EN-US"}[对等体组发布同一路由的时间间隔。]{style="font-family:宋体"}

[**[undo peer route-update-interval]{lang="EN-US"}**]{#struct_0_65458_x3406_x1120725741}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x946140436}

[]{#_Toc32467763}[]{#_Toc32464232}[]{#_Toc30500476}[]{#_Toc26173968}[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **route-update-interval** *interval*]{lang="EN-US"}]{#struct_0_65458_x3406_736628938}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **route-update-interval**]{lang="EN-US"}]{#struct_0_65458_x3406_x163378737}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1420852238}

[[向]{style="font-family:宋体"}[IBGP]{lang="EN-US"}]{#struct_0_65458_x3406_x326689777}[对等体发布同一路由的时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒，向]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体发布同一路由的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1882004238}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1185499615}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1120660205}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_419757385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1976637953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x254821926}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1328447884}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1879884824}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x729511580}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x2125003155}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_x729839260}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[interval]{lang="EN-US"}*]{#struct_0_65458_x3406_15747391}[：发布同一路由的最小时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1120594669}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x756094094}[路由发生变化时，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器会发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息通知对等体。如果同一路由频繁变化，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器会频繁发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息更新路由，导致路由震荡。通过本命令指定向对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布同一路由的时间间隔，可以避免每次路由变化都发送]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，避免路由震荡。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1955193039}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1534638798}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布同一路由的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1003325370}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test as-number 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test route-update-interval 10]{lang="EN-US"}

[]{#_Toc60036310}[]{#_Toc138238296}[]{#_Toc94930965}[]{#_Toc94586697}[]{#_Toc85013221}[]{#_Toc83205947}[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_301043263}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置向对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[发布同一路由的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1120529133}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test route-update-interval 10]{lang="EN-US"}
:::

::: {#-74601952 .myid}
[]{#_Toc404788678}[]{#struct_0_65458_x3406_1981419534}[]{#_Toc356464767}

**BGP \-- BGP配置命令 \-- peer soo**

------------------------------------------------------------------------

[**[peer soo]{lang="EN-US"}**]{#struct_0_65458_x3406_1981550606}[命令用来为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组配置]{style="font-family:宋体"}[SoO]{lang="EN-US"}[（]{style="font-family:宋体"}[Site of Origin]{lang="EN-US"}[，源站点）属性，即从]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收路由时为路由增加]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性，且向该]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布路由时检查路由的]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo peer soo]{lang="EN-US"}**]{#struct_0_65458_x3406_1982205966}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1981681677}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1981812749}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP-VPN VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ ]{lang="EN-US"}[{ *group-name* \| *ip-address* \[ *mask-length* \] } **soo** *site-of-origin*]{lang="EN-US"}]{#struct_0_65458_x3406_1981419533}

[**[undo]{lang="EN-US"}**[ **peer** ]{lang="EN-US"}[{ *group-name* \| *ip-address* \[ *mask-length* \] } **soo**]{lang="EN-US"}]{#struct_0_65458_x3406_1981550605}

[[BGP IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1982205965}[单播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ ]{lang="EN-US"}[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **soo** *site-of-origin*]{lang="EN-US"}]{#struct_0_65458_x3406_1981681676}

[**[undo]{lang="EN-US"}**[ **peer** ]{lang="EN-US"}[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **soo**]{lang="EN-US"}]{#struct_0_65458_x3406_1981812748}

[[BGP-VPN IPv6]{lang="EN-US"}]{#struct_0_65458_x3406_1981419532}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图：]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ ]{lang="EN-US"}[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **soo** *site-of-origin*]{lang="EN-US"}]{#struct_0_65458_x3406_1981550604}

[**[undo]{lang="EN-US"}**[ **peer** ]{lang="EN-US"}[{ *group-name* \| *ipv6-address* \[ *prefix-length* \] } **soo**]{lang="EN-US"}]{#struct_0_65458_x3406_1982205964}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1981681675}

[[没有为]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1981812747}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组配置]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性，即从]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组接收路由时不会为其增加]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性，且向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组发布路由时不会检查路由的]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1981419531}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1981485067}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP-VPN VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1982140427}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_52944851}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_52813779}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_53206995}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_53075923}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_53469139}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_836637894}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_52944850}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_836310214}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[site-of-origin]{lang="EN-US"}*]{#struct_0_65458_x3406_52813778}[：]{style="font-family:宋体"}[SoO]{lang="EN-US"}[扩展团体属性，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}*[site-of-origin]{lang="EN-US"}*[有三种形式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_65458_x3406_53206994}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_65458_x3406_53075922}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_65458_x3406_53469138}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。例如：]{style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_52944849}

[[SoO]{lang="EN-US"}]{#struct_0_65458_x3406_52813777}[扩展团体属性用来标识路由的原始站点。路由器不会将带有]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性的路由发布给该]{style="font-family:宋体"}[SoO]{lang="EN-US"}[标识的站点，确保来自某个站点的路由不会再被发布到该站点，从而避免路由环路。在]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径信息丢失时，可以通过]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性来避免发生环路。]{style="font-family:宋体"}

[[PE]{lang="EN-US"}]{#struct_0_65458_x3406_53206993}[使用不同接口连接同一站点的多个]{style="font-family:宋体"}[CE]{lang="EN-US"}[时，如果配置了]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号替换功能，则会导致路由环路。这种情况下，需要在]{style="font-family:宋体"}[PE]{lang="EN-US"}[上通过本命令为从同一站点不同]{style="font-family:宋体"}[CE]{lang="EN-US"}[学习到的路由添加相同的]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性，且]{style="font-family:宋体"}[PE]{lang="EN-US"}[向]{style="font-family:宋体"}[CE]{lang="EN-US"}[发布路由时检查]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性，如果路由的]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性与为]{style="font-family:宋体"}[CE]{lang="EN-US"}[配置的]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性相同，则不将该路由发布给]{style="font-family:宋体"}[CE]{lang="EN-US"}[，从而避免路由环路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_53075921}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_53469137}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，为对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[配置]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性为]{style="font-family:宋体"}[100:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_52944848}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] peer 1.1.1.1 soo 100:1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_52813776}[在]{style="font-family:宋体"}[BGP VPN IPv4]{lang="EN-US"}[单播地址族视图下，为对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[配置]{style="font-family:宋体"}[SoO]{lang="EN-US"}[属性为]{style="font-family:宋体"}[100:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_53206992}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] peer 1.1.1.1 soo 100:1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_53075920}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer substitute-as]{lang="EN-US"}**]{#struct_0_65458_x3406_53469136}
:::

::: {#914629416 .myid}
[]{#_Toc404788679}[]{#struct_0_65458_x3406_52944847}

**BGP \-- BGP配置命令 \-- peer source-address**

------------------------------------------------------------------------

[**[peer source-address]{lang="EN-US"}**]{#struct_0_65458_x3406_52813775}[命令用来指定与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接使用的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo peer source-address]{lang="EN-US"}**]{#struct_0_65458_x3406_53206991}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_53075919}

[**[peer]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **source-address** *source-ip-address*]{lang="EN-US"}]{#struct_0_65458_x3406_53469135}

[**[peer]{lang="EN-US"}**[ *ipv6-address* \[ *prefix-length* \] **source-address** *source-ipv6-address*]{lang="EN-US"}]{#struct_0_65458_x3406_52944846}

[**[undo peer]{lang="EN-US"}**[ { *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **source-address**]{lang="EN-US"}]{#struct_0_65458_x3406_52813774}

[**[peer]{lang="EN-US"}**[ *group-name* **source-address** { *source-ip-address* \| *source-ipv6-address* } \*]{lang="EN-US"}]{#struct_0_65458_x3406_53206990}

[**[undo peer]{lang="EN-US"}**[ *group-name* **source-address** \[ *source-ip-address* \| *source-ipv6-address* \]]{lang="EN-US"}]{#struct_0_65458_x3406_53075918}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_53469134}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_53403598}[使用到达]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体的最佳路由出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址与对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1618963256}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1618832184}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1619225400}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1619094328}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1619487544}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1618963255}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1618832183}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_836703428}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[source-ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1619225399}[：源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1619094327}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_836441284}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[source-ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1619487543}[：源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1618963254}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1618832182}

[[本命令的作用与]{style="font-family:宋体"}**[peer connect-interface]{lang="EN-US"}**]{#struct_0_65458_x3406_1619225398}[命令的作用类似：本命令直接指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址；]{style="font-family:宋体"}**[peer connect-interface]{lang="EN-US"}**[命令通过指定源接口，间接指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址。在一台]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器上如果同时执行本命令和]{style="font-family:宋体"}**[peer connect-interface]{lang="EN-US"}**[命令，则后执行的配置覆盖之前的配置。]{style="font-family:宋体"}

[[在如下场合需要通过本命令或]{style="font-family:宋体"}**[peer connect-interface]{lang="EN-US"}**]{#struct_0_65458_x3406_1619094326}[命令指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接使用的源地址：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当建立]{style="font-family:宋体"}]{#struct_0_65458_x3406_1619487542}[BGP]{lang="EN-US"}[连接的路由器之间存在冗余链路时，如果路由器上的一个接口发生故障，链路状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[，建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址可能会随之发生变化，导致]{style="font-family:宋体"}[BGP]{lang="EN-US"}[需要重新建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，造成网络震荡。为了避免该情况的发生，建议网络管理员将建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接所使用的源地址配置为]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的地址，或将源接口配置为]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，以提高]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的可靠性和稳定性。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_65458_x3406_1618963253}[BGP]{lang="EN-US"}[对等体之间同时建立多条]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，如果没有明确指定建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址，可能会导致根据最优路由选择]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址错误，并影响]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的建立。如果多条]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话基于不同接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立，则建议用户在配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体时，通过配置源接口或源地址明确指定每个]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址；如果多条]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话基于同一接口的不同]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址建立，则建议用户通过配置源地址，明确指定每个]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1618832181}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地路由器的源地址和对等体的源地址之间必须路由可达。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1619225397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{style="font-family:宋体"}]{#struct_0_65458_x3406_1619094325}[EBGP]{lang="EN-US"}[对等体上指定非直连接口（除]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口外）的地址作为源地址，则需要配置]{style="font-family:宋体"}**[peer ebgp-max-hop]{lang="EN-US"}**[命令允许本地路由器同非直连网络上的邻居建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以为]{style="font-family:宋体"}]{#struct_0_65458_x3406_1619487541}[BGP]{lang="EN-US"}[对等体组同时指定]{style="font-family:宋体"}*[source-ip-address]{lang="EN-US"}*[和]{style="font-family:宋体"}*[source-ipv6-address]{lang="EN-US"}*[参数]{style="font-family:宋体"}[。本地路由器与对等体组中]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的对等体建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，采用]{style="font-family:宋体"}*[source-ip-address]{lang="EN-US"}*[作为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；]{style="font-family:宋体"}[本地路由器与对等体组中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的对等体建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，采用]{style="font-family:宋体"}*[source-ipv6-address]{lang="EN-US"}*[作为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1618963252}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1618832180}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[和]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1619225396}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test source-address 1.1.1.1 1::1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1619094324}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[创建]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[和]{style="font-family:宋体"}[1::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1619487540}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test source-address 1.1.1.1 1::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1618963251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer connect-interface]{lang="EN-US"}**]{#struct_0_65458_x3406_1619225395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer ebgp-max-hop]{lang="EN-US"}**]{#struct_0_65458_x3406_1619487539}
:::

::: {#2070541752 .myid}
[]{#_Toc404788680}[]{#struct_0_65458_x3406_748221476}[]{#_Toc263170160}[]{#_Toc261504252}[]{#_Toc180224230}

**BGP \-- BGP配置命令 \-- peer substitute-as**

------------------------------------------------------------------------

[**[peer substitute-as]{lang="EN-US"}**]{#struct_0_65458_x3406_1977036828}[命令用来配置用本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号替换]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[**[undo peer substitute-as]{lang="EN-US"}**]{#struct_0_65458_x3406_x1780748117}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1072553140}

[**[peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **substitute-as**]{lang="EN-US"}]{#struct_0_65458_x3406_941205755}

[**[undo peer]{lang="EN-US"}**[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **substitute-as**]{lang="EN-US"}]{#struct_0_65458_x3406_756389707}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1063807885}

[[不会用本地]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_65458_x3406_x1120463597}[号替换]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1177151096}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1454915514}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1804284356}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_489944731}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1829259062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1623564849}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_248209612}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1121446637}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_836310218}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x761977758}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_837031114}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x2062855712}

[[在]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x845187082}[中，如果]{style="font-family:宋体"}[PE]{lang="EN-US"}[和]{style="font-family:宋体"}[CE]{lang="EN-US"}[之间运行]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[，由于]{style="font-family:宋体"}[BGP]{lang="EN-US"}[使用]{style="font-family:宋体"}[AS]{lang="EN-US"}[号检测路由环路，为保证路由信息的正确发送，需要为物理位置不同的站点分配不同的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[如果物理位置不同的]{style="font-family:宋体"}[CE]{lang="EN-US"}]{#struct_0_65458_x3406_x37434948}[复用相同的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，则需要在]{style="font-family:宋体"}[PE]{lang="EN-US"}[上配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号替换功能，将]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性中]{style="font-family:宋体"}[CE]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号替换为]{style="font-family:宋体"}[PE]{lang="EN-US"}[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号，以保证私网路由能够正确发布。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2074601651}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1899514830}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置用本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号替换对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1121381101}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer 1.1.1.1 substitute-as]{lang="EN-US"}

[]{#_Toc138238297}[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1410554655}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置用本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[号替换对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1658050283}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer 1::1 substitute-as]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1109592419}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer s]{lang="EN-US"}**]{#struct_0_65458_x3406_x1109330275}**[oo]{lang="EN-US"}**
:::

::: {#-2102429804 .myid}
[]{#_Toc404788681}[]{#struct_0_65458_x3406_791291144}[]{#_Toc263170161}[]{#_Toc261504253}[]{#_Toc180224231}

**BGP \-- BGP配置命令 \-- peer timer**

------------------------------------------------------------------------

[**[peer timer]{lang="EN-US"}**]{#struct_0_65458_x3406_2114353129}[命令用来配置本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔和保持时间。]{style="font-family:宋体"}

[**[undo peer timer]{lang="EN-US"}**]{#struct_0_65458_x3406_x483288526}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_820879214}

[**[peer]{lang="EN-US"}**[ { *group-name \| ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **timer** **keepalive** *keepalive* **hold** *holdtime*]{lang="EN-US"}]{#struct_0_65458_x3406_x1120922348}

[**[undo peer]{lang="EN-US"}**[ { *group-name \| ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **timer**]{lang="EN-US"}]{#struct_0_65458_x3406_294271789}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1450438694}

[[本地路由器与指定对等体]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_65458_x3406_x889009812}[对等体组之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒，保持时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_65458_x3406_1577928}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x510951317}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x506700187}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2100949388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1120856812}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x508375511}

[*[group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1594214362}[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_2044775574}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_433025687}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1378166422}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_433746583}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[keepalive]{lang="EN-US"}***[ keepalive]{lang="EN-US"}*]{#struct_0_65458_x3406_x1833291309}[：指定存活时间间隔。]{style="font-family:宋体"}*[keepalive]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[21845]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[hold ]{lang="EN-US"}***[holdtime]{lang="EN-US"}*]{#struct_0_65458_x3406_x300361805}[：指定保持时间。]{style="font-family:宋体"}*[holdtime]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。保持时间]{style="font-family:宋体"}[必须大于或等于存活时间的三倍。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_306210204}

[[当对等体间建立了]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1120791276}[会话后，它们定时向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息，以防止路由器认为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话已中断。]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息的发送时间间隔称为存活时间间隔。]{style="font-family:宋体"}

[[若路由器在设定的会话保持时间（]{style="font-family:宋体"}[Holdtime]{lang="EN-US"}]{#struct_0_65458_x3406_500767667}[）内未收到对端的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息或]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，则认为此]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话已中断，从而断开此]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1043725539}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用该命令配置的定时器比使用]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1233918553}**[timer]{lang="EN-US"}**[命令配置的定时器优先级高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果当前路由器上配置的保持时间与对端设备（对等体）上配置的保持时间不一致，则数值较小者作为协商后的保持时间。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1700447879}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[保持时间为]{style="font-family:宋体"}]{#struct_0_65458_x3406_680445411}[0]{lang="EN-US"}[时，不向该对等体发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[消息，与该对等体之间的会话永远不会超时断开；存活时间间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[，协商的保持时间不为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，以协商的保持时间的三分之一作为存活时间间隔；当保持时间和存活时间间隔都不为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，将协商的保持时间的三分之一与配置的存活时间间隔比较，取最小值作为存活时间间隔。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置该命令后，不会马上断开会话，而是等到其他条件触发会话重建（如复位]{style="font-family:宋体"}]{#struct_0_65458_x3406_851499086}[BGP]{lang="EN-US"}[会话）时，再以配置的保持时间协商建立会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1120725740}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_619943505}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置本地路由器与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔与保持时间分别为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒和]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_589142138}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test timer keepalive 60 hold 180]{lang="EN-US"}

[]{#_Toc138238298}[]{#_Toc65038733}[]{#_Toc58333327}[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x94186614}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置本地路由器与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔与保持时间分别为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒和]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1573693908}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test timer keepalive 60 hold 180]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1286362894}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置本地路由器与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔与保持时间都是]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，表示该会话永不超时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1120660204}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test timer keepalive 0 hold 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1985841326}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置本地路由器与对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔与保持时间都是]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，表示该会话永不超时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_84667143}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test timer keepalive 0 hold 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x248506559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1766435438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="EN-US"}**]{#struct_0_65458_x3406_1701730569}
:::

::::: {#1266567706 .myid}
[]{#_Toc357510960}[]{#_Toc356214037}[]{#_Toc356208096}[]{#_Toc257618995}[]{#_Toc404788682}[]{#struct_0_65458_x3406_x1402375654}

**BGP \-- BGP配置命令 \-- peer ttl-security**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BGP命令.files/image001.png){#图片 1 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_65458_x3406_x1401982438}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65458_x3406_163577212}
:::

[ ]{lang="DA"}

[]{#struct_0_65458_x3406_163511676}[]{#_Toc274813078}**[peer ttl-security]{lang="DA"}**[命令用来为对等体]{style="font-family:宋体"}[/]{lang="DA"}[对等体组使能]{style="font-family:宋体"}[BGP]{lang="DA"}[报文的]{style="font-family:宋体"}[GTSM]{lang="DA"}[（]{style="font-family:宋体"}[Generalized TTL Security Mechanism]{lang="DA"}[，]{style="font-family:宋体"}[通用]{style="font-family:宋体"}[TTL]{lang="DA"}[安全保护机制]{style="font-family:宋体"}[）]{style="font-family:宋体"}[安全检测功能。]{style="font-family:宋体"}

[**[undo]{lang="DA"}**]{#struct_0_65458_x3406_163904892}**[ peer ttl-security]{lang="DA"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_163773820}

[**[peer]{lang="DA"}**]{#struct_0_65458_x3406_164167036}[ { *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ttl-security hops** *hop-count*]{lang="DA"}

[**[undo peer ]{lang="EN-US"}**[{ *group-name* \| *ip-address* \[ *mask-length* \] \| *ipv6-address* \[ *prefix-length* \] } **ttl-security hops**]{lang="EN-US"}]{#struct_0_65458_x3406_163642747}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_163511675}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_163904891}[报文的]{style="font-family:宋体"}[GTSM]{lang="EN-US"}[安全检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_163773819}

[]{#struct_0_65458_x3406_164167035}[[BGP]{lang="EN-US"}]{#_Toc257618996}[视图]{style="font-family:
宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_163446138}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_163839354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_163708282}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_164101498}

[]{#struct_0_65458_x3406_163577209}[]{#_Toc274813076}*[group-name]{lang="EN-US"}*[：对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。指定的对等体组必须已经创建。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_163446137}[：对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_433025685}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_163839353}[：对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。指定的对等体必须已经创建。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_433156757}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[hops ]{lang="EN-US"}***[hop-count]{lang="EN-US"}*]{#struct_0_65458_x3406_163708281}[：指定本地设备到达指定对等体的最大跳数。]{style="font-family:宋体"}*[hop-count]{lang="EN-US"}*[表示最大跳数]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[254]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_164101497}

[[执行本命令为对等体]{style="font-family:宋体"}]{#struct_0_65458_x3406_163642752}[/]{lang="DA"}[对等体组使能]{style="font-family:宋体"}[BGP]{lang="DA"}[报文的]{style="font-family:宋体"}[GTSM]{lang="DA"}[安全检测功能后，当设备收到指定对等体发送的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[报文时，会判断报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[是否在]{style="font-family:宋体"}[255-]{lang="EN-US"}["]{style="font-family:宋体"}*[hop-count]{lang="EN-US"}*["]{style="font-family:宋体"}[+1]{lang="EN-US"}[到]{style="font-family:宋体"}[255]{lang="EN-US"}[之间。如果在，则上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}[处理；如果不在，则直接丢弃报文。从而，使设备能够避免受到]{style="font-family:宋体"}[CPU]{lang="EN-US"}[利用（]{style="font-family:宋体"}[CPU-utilization]{lang="EN-US"}[）类型的攻击（如]{style="font-family:宋体"}[CPU]{lang="EN-US"}[过载），增强系统的安全性。]{style="font-family:宋体"}

[[执行本命令后，设备会将发送报文的初始]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_65458_x3406_163511680}[设置为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_163904896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令后，只要本地设备和指定的对等体通过了]{style="font-family:宋体"}]{#struct_0_65458_x3406_163773824}[GTSM]{lang="EN-US"}[检查，就允许在二者之间建立]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话，不管二者之间的跳数是否超过]{style="font-family:宋体"}**[peer ebgp-max-hop]{lang="EN-US"}**[命令指定的跳数范围。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_65458_x3406_164167040}[BGP GTSM]{lang="EN-US"}[功能时，要求本设备和对等体设备上同时配置本特性，指定的]{style="font-family:宋体"}*[hop-count]{lang="EN-US"}*[值可以不同，只要能够满足合法性检查即可。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_163642751}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_163511679}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，为已经创建的对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[使能]{style="font-family:宋体"}[BGP]{lang="DA"}[报文的]{style="font-family:
宋体"}[GTSM]{lang="DA"}[安全检测功能，并指定对等体组中的对等体到达本地设备的最大跳数为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_163708287}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] peer test ttl-security hops 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_164101503}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，为已经创建的对等体组]{style="font-family:宋体"}[test]{lang="EN-US"}[使能]{style="font-family:宋体"}[BGP]{lang="DA"}[报文的]{style="font-family:
宋体"}[GTSM]{lang="DA"}[安全检测功能，并指定对等体组中的对等体到达本地设备的最大跳数为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1765094081}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] peer test ttl-security hops 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1764963009}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer ebgp-max-hop]{lang="EN-US"}**]{#struct_0_65458_x3406_x1764831937}
:::::

::: {#537581611 .myid}
[]{#_Toc404788683}[]{#struct_0_65458_x3406_x1764700865}[]{#_Toc366077132}

**BGP \-- BGP配置命令 \-- pic**

------------------------------------------------------------------------

[**[pic]{lang="EN-US"}**]{#struct_0_65458_x3406_x1764569793}[命令用来开启当前地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由功能。]{style="font-family:宋体"}

[**[undo pic]{lang="EN-US"}**]{#struct_0_65458_x3406_x1765094082}[命令用来关闭当前地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1765028546}

[**[pic]{lang="EN-US"}**]{#struct_0_65458_x3406_x1764897474}

[**[undo pic]{lang="EN-US"}**]{#struct_0_65458_x3406_x1764766402}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1764635330}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1765159619}[快速重路由功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1765028547}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1764897475}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1764766403}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1764635331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1764963012}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1764831940}

[[FRR]{lang="EN-US"}]{#struct_0_65458_x3406_x1764700868}[（]{style="font-family:宋体"}[Fast Reroute]{lang="EN-US"}[，快速重路由）功能用来在双归属的组网环境下，通过为流量转发的主路由指定备份下一跳，并通过]{style="font-family:宋体"}[ARP]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组网）、]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组网）或]{style="font-family:宋体"}[ND]{lang="EN-US"}[（]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组网）检测主路由的状态，实现主路由出现故障时，将流量迅速切换到备份路径，大大缩短了故障恢复时间。]{style="font-family:宋体"}

[[通过本命令开启当前地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1764569796}[快速重路由功能后，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会为当前地址族的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由自动计算备份下一跳，即只要从不同]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体学习到了到达同一目的网络的路由，且这些路由不等价，就会生成主备两条路由。]{style="font-family:宋体"}

[[除了执行本命令外，执行]{style="font-family:宋体"}**[fast-reroute]{lang="EN-US"}**[ **route-policy**]{lang="EN-US"}]{#struct_0_65458_x3406_x1765094077}[命令指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由引用的路由策略，也可以开启快速重路由功能。该方式的优先级高于本命令。路由策略的详细介绍，请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由配置指导"中的"路由策略"。]{style="font-family:宋体"}

[[需要注意的是，在某些组网情况下，执行]{style="font-family:宋体"}**[pic]{lang="EN-US"}**]{#struct_0_65458_x3406_x1764963005}[命令为所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由生成备份下一跳后，可能会导致路由环路，请谨慎使用本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1764831933}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1764700861}[开启]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1764635325}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ]{lang="EN-US"}[address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] pic]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1765159614}

[]{#struct_0_65458_x3406_x1765028542}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fast-reroute route-policy]{lang="EN-US"}**]{#_Toc351625549}
:::

::: {#830408614 .myid}
[]{#_Toc404788684}[]{#struct_0_65458_x3406_x1120594668}[]{#_Toc263170162}[]{#_Toc261504254}[]{#_Toc180224232}

**BGP \-- BGP配置命令 \-- preference**

------------------------------------------------------------------------

[**[preference]{lang="EN-US"}**]{#struct_0_65458_x3406_1972789261}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的优先级。]{style="font-family:宋体"}

[**[undo preference]{lang="EN-US"}**]{#struct_0_65458_x3406_2074549049}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1648758586}

[**[preference]{lang="EN-US"}**[ { *external-preference internal-preference local-preference \|* **route-policy** *route-policy-name* }]{lang="EN-US"}]{#struct_0_65458_x3406_1800071252}

[**[undo preference]{lang="EN-US"}**]{#struct_0_65458_x3406_x2003068792}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x688536327}

[[EBGP]{lang="EN-US"}]{#struct_0_65458_x3406_1808870914}[路由的优先级为]{style="font-family:宋体"}[255]{lang="EN-US"}[，]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由的优先级为]{style="font-family:宋体"}[255]{lang="EN-US"}[，本地产生的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的优先级为]{style="font-family:宋体"}[130]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1120529132}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_x1980661879}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1687766285}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_258609837}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_364037649}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1484423337}

[*[external-preference]{lang="EN-US"}*]{#struct_0_65458_x3406_x52134963}[：]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由（从]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体学来的路由）的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[internal-preference]{lang="EN-US"}*]{#struct_0_65458_x3406_x1120463596}[：]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由（从]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体学来的路由）的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[local-preference]{lang="EN-US"}*]{#struct_0_65458_x3406_x1551732259}[：本地产生的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1651304638}[：根据路由策略设置路由的优先级。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[表示路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。指定本参数后，可以为通过路由策略中匹配条件过滤的特定路由设置优先级，没有通过过滤的路由使用缺省的优先级。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x130442769}

[[对于相同的目的地，不同的路由协议、直连路由和静态路由可能会发现不同的路由，但这些路由并不都是最优的。为了判断最优路由，各路由协议、直连路由和静态路由都被赋予了一个优先级，具有较高优先级的路由协议发现的路由将成为最优路由。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1682191409}

[[本命令用来设置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1071197595}[路由的优先级，以改变]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由被选为最优路由的可能性。]{style="font-family:宋体"}

[[根据路由策略设置路由的优先级时，需要在指定的路由策略中通过]{style="font-family:宋体"}**[apply preference]{lang="EN-US"}**]{#struct_0_65458_x3406_645937716}[命令配置路由的优先级。如果没有在路由策略中配置]{style="font-family:宋体"}**[apply preference]{lang="EN-US"}**[命令，则通过匹配规则过滤的路由使用缺省的优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2131154610}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1121446636}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由、]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由和本地产生的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的优先级分别为]{style="font-family:宋体"}[20]{lang="EN-US"}[、]{style="font-family:宋体"}[20]{lang="EN-US"}[和]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_804106183}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] preference 20 20 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_857330169}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1881613730}

[\[Sysname\] ip prefix-list route permit 1.1.1.0 24]{lang="EN-US"}

[\[Sysname\] route-policy prefer permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-prefer-0\] if-match ip address prefix-list route]{lang="EN-US"}

[\[Sysname-route-policy-prefer-0\] apply preference 200]{lang="EN-US"}

[\[Sysname-route-policy-prefer-0\] quit]{lang="EN-US"}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] preference route-policy prefer]{lang="EN-US"}

[]{#_Toc138238299}[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1575223826}[在]{style="font-family:宋体"}[BGP-VPN IPv6]{lang="EN-US"}[单播地址族视图下，配置]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由、]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由和]{style="font-family:宋体"}[BGP]{lang="EN-US"}[本地产生的路由的优先级分别为]{style="font-family:宋体"}[20]{lang="EN-US"}[、]{style="font-family:宋体"}[20]{lang="EN-US"}[和]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1121381100}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6-vpn1\] preference 20 20 200]{lang="EN-US"}
:::

::::: {#-2107853381 .myid}
[]{#_Toc404788685}[]{#struct_0_65458_x3406_1598407302}

**BGP \-- BGP配置命令 \-- primary-path-detect bfd**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BGP命令.files/image001.png){#图片 22 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_65458_x3406_314035395}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_65458_x3406_1041548885}
:::

[ ]{lang="EN-US"}

[**[primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_65458_x3406_1598472838}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测主路由的下一跳是否可达。]{style="font-family:宋体"}

[**[undo primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_65458_x3406_296578805}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x122969513}

[**[primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_65458_x3406_1598014086}

[**[undo primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_65458_x3406_x2051921136}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1598079622}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x6734021}[快速重路由通过]{style="font-family:宋体"}[ARP]{lang="EN-US"}[检测主路由的下一跳是否可达。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x627962632}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x417884258}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x315447928}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_594560826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x417818722}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1070958597}

[**[echo]{lang="EN-US"}**]{#struct_0_65458_x3406_x417753186}[：]{style="font-family:宋体"}[配置通过]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测主路由的下一跳是否可达。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_131495159}

[[在]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1319341932}[组网中，设备上开启]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由功能，并为主路由生成备份下一跳后，设备将通过如下方式检测主路由的下一跳是否可达：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果执行了本命令，则通过]{style="font-family:宋体"}]{#struct_0_65458_x3406_x417687650}[Echo]{lang="EN-US"}[方式的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[否则，通过]{style="font-family:宋体"}]{#struct_0_65458_x3406_x676313219}[ARP]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x898533673}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x418146402}[配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[快速重路由通过]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话检测主路由的下一跳是否可达。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x2013873328}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] primary-path-detect bfd echo]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x418080866}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fast-reroute]{lang="EN-US"}**[ **route-policy**]{lang="EN-US"}]{#struct_0_65458_x3406_x915156553}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pic]{lang="EN-US"}**]{#struct_0_65458_x3406_1948105549}
:::::

::: {#-1282654330 .myid}
[]{#_Toc404788686}[]{#struct_0_65458_x3406_x1318328700}[]{#_Toc263170163}[]{#_Toc261504255}[]{#_Toc180224233}[]{#_Toc319650250}[]{#_Toc319918741}[]{#_Toc319937805}[]{#_Toc319650251}[]{#_Toc319918742}[]{#_Toc319937806}[]{#_Toc319650252}[]{#_Toc319918743}[]{#_Toc319937807}[]{#_Toc319650253}[]{#_Toc319918744}[]{#_Toc319937808}[]{#_Toc319650254}[]{#_Toc319918745}[]{#_Toc319937809}[]{#_Toc319650255}[]{#_Toc319918746}[]{#_Toc319937810}[]{#_Toc319650256}[]{#_Toc319918747}[]{#_Toc319937811}[]{#_Toc319650257}[]{#_Toc319918748}[]{#_Toc319937812}[]{#_Toc319650258}[]{#_Toc319918749}[]{#_Toc319937813}[]{#_Toc319650259}[]{#_Toc319918750}[]{#_Toc319937814}[]{#_Toc319650260}[]{#_Toc319918751}[]{#_Toc319937815}

**BGP \-- BGP配置命令 \-- reflect between-clients**

------------------------------------------------------------------------

[**[reflect between-clients]{lang="EN-US"}**]{#struct_0_65458_x3406_x137509285}[命令用来允许路由反射器在客户机之间反射路由。]{style="font-family:宋体"}

[**[undo reflect between-clients]{lang="EN-US"}**]{#struct_0_65458_x3406_x900918599}[命令用来禁止路由反射器在客户机之间反射路由。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1672910504}

[**[reflect between-clients]{lang="EN-US"}**]{#struct_0_65458_x3406_1322791903}

[**[undo reflect between-clients]{lang="EN-US"}**]{#struct_0_65458_x3406_1256056026}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1649961329}

[[允许路由反射器在客户机之间反射路由。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1432074059}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1865268558}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1182315306}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv4 MDT]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1246346908}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1158252631}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x939377638}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1255990490}

[[如果配置了路由反射器后，由于组网需要在路由反射器的客户机之间建立了全连接，则客户机之间可以直接交换路由信息，客户机到客户机之间的路由反射是没有必要的。此时，不需要修改网络配置或改变网络拓扑，只需在路由反射器上通过本命令禁止其在客户机之间反射路由，就可以避免路由反射，减少占用的带宽资源。]{style="font-family:宋体"}]{#struct_0_65458_x3406_2116035571}

[[需要注意的是，禁止客户机之间的路由反射后，客户机到非客户机之间的路由仍然可以被反射。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x244951428}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1528854964}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_241758610}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，禁止路由反射器在客户机之间反射路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_864084477}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] undo reflect between-clients]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1628212223}[在]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族视图下，禁止路由反射器在客户机之间反射路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1255924954}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family vpnv4]{lang="EN-US"}

[\[Sysname-bgp-vpnv4\] undo reflect between-clients]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x523349629}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，禁止路由反射器在客户机之间反射路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1090577785}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] undo reflect between-clients]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1998183580}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，禁止路由反射器在客户机之间反射路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1836915075}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] undo reflect between-clients]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1255859418}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，禁止路由反射器在客户机之间反射]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x247442363}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn ]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] undo reflect between-clients]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x198616924}[在]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族视图下，禁止路由反射器在客户机之间反射]{style="font-family:宋体"}[MDT]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x198485852}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 mdt ]{lang="EN-US"}

[\[Sysname-bgp-mdt\] undo reflect between-clients]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_737093662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer reflect-client ]{lang="EN-US"}**]{#struct_0_65458_x3406_1890768910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reflector cluster-id]{lang="EN-US"}**]{#struct_0_65458_x3406_x44584075}
:::

::: {#-867025343 .myid}
[]{#_Toc404788687}[]{#struct_0_65458_x3406_x1262153267}[]{#_Toc263170164}[]{#_Toc261504256}[]{#_Toc180224234}[]{#_Toc138238300}

**BGP \-- BGP配置命令 \-- reflector cluster-id**

------------------------------------------------------------------------

[**[reflector cluster-id]{lang="EN-US"}**]{#struct_0_65458_x3406_1256318170}[命令用来配置路由反射器的集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo reflector cluster-id]{lang="EN-US"}**]{#struct_0_65458_x3406_x747648501}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1378530919}

[**[reflector cluster-id]{lang="EN-US"}**[ { *cluster-id* \| *ip-address* }]{lang="EN-US"}]{#struct_0_65458_x3406_523252837}

[**[undo reflector cluster-id]{lang="EN-US"}**]{#struct_0_65458_x3406_x615339689}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_426050192}

[[每个路由反射器都使用自己的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_1999877001}[作为集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x77476800}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1256252634}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv4]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP VPNv6]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP L2VPN]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv6]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}[/BGP IPv4 MDT]{lang="EN-US"}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_827735066}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_199511795}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x515125970}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1610821607}

[*[cluster-id]{lang="EN-US"}*]{#struct_0_65458_x3406_753241985}[：指定数值形式的集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_636365546}[：指定点分十进制地址形式的集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_834370594}

[[路由反射器及其客户机形成了一个集群。通常情况下，一个集群中只有一个路由反射器，该反射器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_1256187098}[就作为集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用于识别该群。]{style="font-family:宋体"}

[[为了提高网络的可靠性、避免单点故障，一个集群中可以设置多个路由反射器。此时，应使用本命令为集群中所有路由反射器配置相同的集群]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1084623698}[，以便集群具有统一的标识，避免路由环路的产生。]{style="font-family:宋体"}

[[需要注意的是，配置的集群]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_65458_x3406_x611044485}[不要与客户机的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1610898404}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_107275844}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，本地路由器是集群中的路由反射器之一，在本地路由器上配置集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x951218222}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] reflector cluster-id 80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_2004260541}[在]{style="font-family:宋体"}[BGP VPNv4]{lang="EN-US"}[地址族视图下，本地路由器是集群中的路由反射器之一，在本地路由器上配置集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1256121562}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family vpnv4]{lang="EN-US"}

[\[Sysname-bgp-vpnv4\] reflector cluster-id 80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1233104985}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，本地路由器是集群中的路由反射器之一，在本地路由器上配置集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x513195384}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\] reflector cluster-id 80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1831063582}[在]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播地址族视图下，本地路由器是集群中的路由反射器之一，在本地路由器上配置集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1256580314}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv6\] reflector cluster-id 80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x736549777}[在]{style="font-family:宋体"}[BGP L2VPN]{lang="EN-US"}[地址族视图下，本地路由器是集群中的路由反射器之一，在本地路由器上配置集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1746342581}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family l2vpn]{lang="EN-US"}

[\[Sysname-bgp-l2vpn\] reflector cluster-id 80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x198682461}[在]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族视图下，本地路由器是集群中的路由反射器之一，在本地路由器上配置集群]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x198551389}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 mdt]{lang="EN-US"}

[\[Sysname-bgp-mdt\] reflector cluster-id 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_987191994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer reflect-client]{lang="EN-US"}**]{#struct_0_65458_x3406_x1461831031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reflect between-clients]{lang="EN-US"}**]{#struct_0_65458_x3406_1745607233}
:::

::: {#274161898 .myid}
[]{#_Toc404788688}[]{#struct_0_65458_x3406_x805503861}

**BGP \-- BGP配置命令 \-- refresh bgp**

------------------------------------------------------------------------

[**[refresh bgp]{lang="EN-US"}**]{#struct_0_65458_x3406_1306229930}[命令用来手工对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话进行软复位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1256514778}

[**[re]{lang="EN-US"}[fresh]{lang="EN-US"}**]{#struct_0_65458_x3406_x198879071}**[ bgp]{lang="EN-US"}**[ { *ip-address* ]{lang="EN-US"}[\[ *mask-length* \] ]{lang="EN-US"}[\| **all** \| ]{lang="EN-US"}**[external]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[group]{lang="EN-US"}***[ group-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **internal** ]{lang="EN-US"}[}]{lang="EN-US"}[ { **export** \| **import** } **ipv4** { **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}

[**[re]{lang="EN-US"}[fresh]{lang="EN-US"}**]{#struct_0_65458_x3406_x198747999}**[ bgp]{lang="EN-US"}**[ { *ip*]{lang="EN-US"}*[v6]{lang="EN-US"}[-address]{lang="EN-US"}*[ ]{lang="EN-US"}[\[ *prefix-length* \] ]{lang="EN-US"}[\|]{lang="EN-US"}[ ]{lang="EN-US"}**[all]{lang="EN-US"}***[ ]{lang="EN-US"}*[\| ]{lang="EN-US"}**[external]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[group]{lang="EN-US"}***[ group-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **internal** ]{lang="EN-US"}[}]{lang="EN-US"}[ { **export** \| **import** } **ipv6** { **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}

[**[re]{lang="EN-US"}[fresh]{lang="EN-US"}**]{#struct_0_65458_x3406_x198682463}**[ bgp]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}[ \[ *mask-length* \] { **export** \| **import** } **ipv6** \[ **unicast** \]]{lang="EN-US"}

[**[refresh bgp ]{lang="EN-US"}**[{ *ip-address* \[ *mask-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } { **export** \| **import** } **vpnv4** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x198551391}

[**[refresh bgp ]{lang="EN-US"}**[{ *ip-address* \[ *mask-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } { **export** \| **import** } **vpnv6**]{lang="EN-US"}]{#struct_0_65458_x3406_x199075672}

[**[refresh bgp]{lang="EN-US"}**[ { *ip-address* \[ *mask-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } { **export** \| **import** } **l2vpn**]{lang="EN-US"}]{#struct_0_65458_x3406_x198944600}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_352247945}

[[用户视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_1272857945}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1594522378}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x144609584}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1109404427}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1303644716}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1256056027}[：软复位与指定对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1999109628}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1783108804}[：软复位与指定对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1999240700}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_65458_x3406_1650026865}[：软复位指定地址族下的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_65458_x3406_x953128588}[：软复位指定地址族下的所有]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**]{#struct_0_65458_x3406_318412502}*[ ]{lang="EN-US"}[group-name]{lang="EN-US"}*[：软复位与指定对等体组中对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_65458_x3406_x1199720998}[：软复位指定地址族下的所有]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_65458_x3406_x566870914}[：触发出方向的软复位，即采用新的配置对向对等体发布的路由进行过滤。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_65458_x3406_x268164664}[：触发入方向的软复位，即采用新的配置对从对等体接收的路由进行过滤。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x198551385}[：软复位]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_1367008265}[：软复位]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1367139337}[：软复位组播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1367467017}[：软复位单播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_65458_x3406_1367598089}[：软复位]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_65458_x3406_1367073800}[：软复位]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[l2vpn]{lang="EN-US"}**]{#struct_0_65458_x3406_1367204872}[：软复位]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1255990491}[：软复位指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[指定地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则软复位公网指定地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2116101107}

[[软复位]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1367073798}[会话是指在不断开]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居关系的情况下，更新]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息，使新的配置生效。]{style="font-family:宋体"}

[[选路策略发生改变后，执行本命令时，如果指定了]{style="font-family:宋体"}**[export]{lang="EN-US"}**]{#struct_0_65458_x3406_962036648}[参数，则会触发本地路由器根据新的路由发布策略过滤路由信息，并将通过过滤的路由信息发送给]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体；执行本命令时，如果指定了]{style="font-family:宋体"}**[import]{lang="EN-US"}**[参数，则本地路由器会向]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体发送]{style="font-family:宋体"}[Route-refresh]{lang="EN-US"}[消息，收到]{style="font-family:宋体"}[Route-refresh]{lang="EN-US"}[消息的对等体将其路由信息重新发给本地路由器，以便本地路由器根据新的路由策略对接收到的路由信息进行过滤。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_1121347804}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令软复位]{style="font-family:宋体"}]{#struct_0_65458_x3406_x225722520}[BGP]{lang="EN-US"}[会话时，要求当前路由器和对等体都支持]{style="font-family:宋体"}[Route-refresh]{lang="EN-US"}[功能，否则本命令不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_x57808205}**[peer keep-all-routes]{lang="EN-US"}**[命令后，执行]{style="font-family:宋体"}**[refresh bgp]{lang="EN-US"}[ ]{lang="EN-US"}[import]{lang="EN-US"}**[命令不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定]{lang="EN-US" style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1960045261}[和]{lang="EN-US" style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{lang="EN-US" style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x736060711}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1255924955}[手工对所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话进行入方向的软复位。]{style="font-family:宋体"}

[[\<Sysname\> refresh bgp all import ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_x523415165}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1367532550}[手工对所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话进行入方向的软复位。]{style="font-family:宋体"}

[[\<Sysname\> refresh bgp all import ipv6]{lang="EN-US"}]{#struct_0_65458_x3406_1367008269}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1367139341}[手工对所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话进行出方向的软复位。]{style="font-family:宋体"}

[[\<Sysname\> refresh bgp all export ipv4 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_1367467021}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1367598093}[手工对所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话进行出方向的软复位。]{style="font-family:宋体"}

[[\<Sysname\> refresh bgp all export ipv6 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_1367073804}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2081661836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer capability-advertise route-refresh]{lang="EN-US"}**]{#struct_0_65458_x3406_x315760691}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer keep-all-routes]{lang="EN-US"}**]{#struct_0_65458_x3406_x1418014007}
:::

::: {#-306874075 .myid}
[]{#_Toc404788689}[]{#struct_0_65458_x3406_609253996}

**BGP \-- BGP配置命令 \-- retain local-label**

------------------------------------------------------------------------

[**[retain local-label]{lang="EN-US"}**]{#struct_0_65458_x3406_1299390698}[命令用来配置删除本地标签的延迟时间。]{style="font-family:宋体"}

[**[undo retain local-label]{lang="EN-US"}**]{#struct_0_65458_x3406_x956829945}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x276356282}

[**[retain local-label]{lang="EN-US"}**[ *retain-time*]{lang="EN-US"}]{#struct_0_65458_x3406_137084360}

[**[undo retain local-label]{lang="EN-US"}**]{#struct_0_65458_x3406_1772053410}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1492625826}

[[删除本地标签的延迟时间为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_65458_x3406_205969469}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x346929569}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1360114472}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1759850898}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1037753327}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2099858225}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1368768883}

[*[retain-time]{lang="EN-US"}*]{#struct_0_65458_x3406_833859211}[：删除本地标签的延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[21845]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x197315058}

[[本地标签是指本地设备通过]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}]{#struct_0_65458_x3406_x14842982}[路由、]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[路由、带标签的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播路由或带标签的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播路由分配给其他]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签。为路由分配的本地标签发生变化时，如果立即删除本地标签，则]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体可能尚未收到新的标签，仍然采用旧的标签转发报文，从而导致流量中断。为了避免上述情况发生，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[需要延迟一段时间再删除本地标签。通过本命令可以调整本地标签的延迟删除时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1763398999}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_673005555}[配置删除本地标签的延迟时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_253023636}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] retain local-label 100]{lang="EN-US"}
:::

::: {#-1980797884 .myid}
[]{#_Toc404788690}[]{#struct_0_65458_x3406_1367204876}

**BGP \-- BGP配置命令 \-- reset bgp**

------------------------------------------------------------------------

[**[reset bgp]{lang="EN-US"}**]{#struct_0_65458_x3406_1367270412}[命令用来复位指定地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1367401484}

[**[reset bgp]{lang="EN-US"}**[ { *as-number* \| *ip-address* \[ *mask-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } **ipv4** { **mdt** \| **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}]{#struct_0_65458_x3406_x1361416338}

[**[reset bgp]{lang="EN-US"}**[ { *as-number* \| *ipv6-address* \[ *prefix-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } **ipv6** { **multicast** \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] }]{lang="EN-US"}]{#struct_0_65458_x3406_x1361285266}

[**[reset bgp]{lang="EN-US"}**[ *ip-address* \[ *mask-length* \] **ipv6** \[ **unicast** \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1361809555}

[**[reset bgp ]{lang="EN-US"}**[{ *as-number* \| *ip-address* \[ *mask-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } **vpnv4** \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_65458_x3406_x1361744019}

[**[reset bgp ]{lang="EN-US"}**[{ *as-number* \| *ip-address* \[ *mask-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } **vpnv6**]{lang="EN-US"}]{#struct_0_65458_x3406_x1361612947}

[**[reset bgp ]{lang="EN-US"}**[{ *as-number* \| *ip-address* \[ *mask-length* \] \| **all** \| **external** \| **group** *group-name* \| **internal** } **l2vpn**]{lang="EN-US"}]{#struct_0_65458_x3406_x1361481875}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1361350803}

[[用户视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1361678484}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1361547412}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1361416340}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1361285268}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1361875093}

[*[as-number]{lang="EN-US"}*]{#struct_0_65458_x3406_x1361744021}[：复位与指定自治系统内对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[as-number]{lang="EN-US"}*[为自治系统号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_65458_x3406_x1361612949}[：复位与指定对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1999502847}[：网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1782977732}[：复位与指定对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1999175167}[：前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361481877}[：复位指定地址族下的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361809550}[：复位指定地址族下的所有]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1361678478}[：复位与指定对等体组中对等体的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示对等体组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[47]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361547406}[：复位指定地址族下的所有]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361416334}[：复位]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361350798}[：复位]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[mdt]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361875087}[：复位]{style="font-family:宋体"}[MDT]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361744015}[：复位组播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361612943}[：复位单播地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[vpnv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x1361285263}[：复位]{style="font-family:宋体"}[VPNv4]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[vpnv6]{lang="EN-US"}**]{#struct_0_65458_x3406_560504747}[：复位]{style="font-family:宋体"}[VPNv6]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[l2vpn]{lang="EN-US"}**]{#struct_0_65458_x3406_560635819}[：复位]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_560439210}[：复位指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[指定地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则复位公网指定地址族下的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_560570282}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_560897962}[的选路策略改变后，为了使新的策略生效，可以复位]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，即删除并重新建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，以便重新发布路由信息，并应用新的策略对路由信息进行过滤。复位]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，会造成短暂的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话中断。]{style="font-family:宋体"}

[[需要注意的是，执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_561029034}[、]{style="font-family:宋体"}**[mdt]{lang="EN-US"}**[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_560504745}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_560635817}[复位公网]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播地址族下的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp all ipv4]{lang="EN-US"}]{#struct_0_65458_x3406_560701353}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_560832425}[复位公网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播地址族下的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp all ipv6]{lang="EN-US"}]{#struct_0_65458_x3406_560963497}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_560439208}[复位]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[组播地址族下的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp all ipv4 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_560766888}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_560897960}[复位]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址族下的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp all ipv6 multicast]{lang="EN-US"}]{#struct_0_65458_x3406_561029032}
:::

::: {#-644289902 .myid}
[]{#_Toc404788691}[]{#struct_0_65458_x3406_1859222672}[]{#_Toc366153319}[]{#_Toc366167062}[]{#_Toc366220374}[]{#_Toc366153320}[]{#_Toc366167063}[]{#_Toc366220375}[]{#_Toc366153321}[]{#_Toc366167064}[]{#_Toc366220376}[]{#_Toc366153322}[]{#_Toc366167065}[]{#_Toc366220377}[]{#_Toc366153323}[]{#_Toc366167066}[]{#_Toc366220378}[]{#_Toc366153324}[]{#_Toc366167067}[]{#_Toc366220379}[]{#_Toc366153325}[]{#_Toc366167068}[]{#_Toc366220380}[]{#_Toc366153326}[]{#_Toc366167069}[]{#_Toc366220381}[]{#_Toc366153327}[]{#_Toc366167070}[]{#_Toc366220382}[]{#_Toc366153328}[]{#_Toc366167071}[]{#_Toc366220383}[]{#_Toc366153329}[]{#_Toc366167072}[]{#_Toc366220384}[]{#_Toc366153330}[]{#_Toc366167073}[]{#_Toc366220385}[]{#_Toc366153331}[]{#_Toc366167074}[]{#_Toc366220386}[]{#_Toc366153332}[]{#_Toc366167075}[]{#_Toc366220387}[]{#_Toc366153333}[]{#_Toc366167076}[]{#_Toc366220388}[]{#_Toc366153334}[]{#_Toc366167077}[]{#_Toc366220389}[]{#_Toc366153335}[]{#_Toc366167078}[]{#_Toc366220390}[]{#_Toc366153336}[]{#_Toc366167079}[]{#_Toc366220391}[]{#_Toc366153337}[]{#_Toc366167080}[]{#_Toc366220392}[]{#_Toc366153338}[]{#_Toc366167081}[]{#_Toc366220393}[]{#_Toc366153339}[]{#_Toc366167082}[]{#_Toc366220394}[]{#_Toc366153340}[]{#_Toc366167083}[]{#_Toc366220395}[]{#_Toc366153341}[]{#_Toc366167084}[]{#_Toc366220396}[]{#_Toc366153342}[]{#_Toc366167085}[]{#_Toc366220397}[]{#_Toc366153343}[]{#_Toc366167086}[]{#_Toc366220398}[]{#_Toc366153344}[]{#_Toc366167087}[]{#_Toc366220399}[]{#_Toc366153345}[]{#_Toc366167088}[]{#_Toc366220400}[]{#_Toc366153346}[]{#_Toc366167089}[]{#_Toc366220401}[]{#_Toc366153347}[]{#_Toc366167090}[]{#_Toc366220402}[]{#_Toc366153348}[]{#_Toc366167091}[]{#_Toc366220403}[]{#_Toc366153349}[]{#_Toc366167092}[]{#_Toc366220404}[]{#_Toc366153350}[]{#_Toc366167093}[]{#_Toc366220405}

**BGP \-- BGP配置命令 \-- reset bgp all**

------------------------------------------------------------------------

[**[reset bgp all]{lang="EN-US"}**]{#struct_0_65458_x3406_1256121563}[命令用来复位所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1233039449}

[**[reset bgp]{lang="EN-US"}**[ **all**]{lang="EN-US"}]{#struct_0_65458_x3406_x220904100}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x957468847}

[[用户视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x346384539}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_101727876}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x797529535}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1930359661}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1256580315}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x736615313}[的选路策略改变后，为了使新的策略生效，可以复位]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，即删除并重新建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，以便重新发布路由信息，并应用新的策略对路由信息进行过滤。复位]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话时，会造成短暂的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话中断。]{style="font-family:宋体"}

[[执行本命令后，将复位所有地址族下的所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_560570287}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1698522162}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1435878500}[复位所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp all]{lang="EN-US"}]{#struct_0_65458_x3406_294828267}
:::

::: {#-2047602651 .myid}
[]{#_Toc404788692}[]{#struct_0_65458_x3406_x1712370216}[]{#_Toc307230813}[]{#_Toc302638078}[]{#_Toc307230814}

**BGP \-- BGP配置命令 \-- reset bgp dampening**

------------------------------------------------------------------------

[**[reset bgp dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_1827555733}[命令用来清除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的衰减信息，并解除对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的抑制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1829448341}

[**[reset bgp dampening ipv4 ]{lang="EN-US"}**[ { ]{lang="EN-US"}**[multicast]{lang="EN-US"}**[ \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *network-address* \[ *mask* \| *mask-length* \] \]]{lang="EN-US"}]{#struct_0_65458_x3406_1256514779}

[**[reset bgp dampening ipv6 ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[multicast]{lang="EN-US"}**[ \| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *network-address* *prefix-length* \]]{lang="EN-US"}]{#struct_0_65458_x3406_2126850832}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2012041725}

[[用户视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_244745227}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1345696094}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1269546506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_945035556}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_730528819}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_2126981904}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[路由的衰减信息，并解除对]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[路由的抑制。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_2127047440}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[路由的衰减信息，并解除对]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[路由的抑制。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_2126523151}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播]{style="font-family:宋体"}[路由的衰减信息，并解除对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播]{style="font-family:宋体"}[路由的抑制。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_2126654223}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播]{style="font-family:宋体"}[路由的衰减信息，并解除对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播]{style="font-family:宋体"}[路由的抑制。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_x1581273343}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的衰减信息，并解除对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的抑制。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的衰减信息，并解除对]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的抑制。]{style="font-family:宋体"}

[*[network-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1256056024}[：清除匹配指定目的网络地址的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的衰减信息，并解除对该路由的抑制。如果不指定本参数，则清除所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的衰减信息，并解除对所有]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的抑制。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_1650092401}[：目的网络地址的掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_2115976154}[：目的网络地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_2126981907}[：目的网络地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_681500812}

[[执行]{style="font-family:宋体"}**[reset bgp dampening ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_594250874}[命令时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定了]{style="font-family:宋体"}]{#struct_0_65458_x3406_195735674}*[network-address]{lang="EN-US"}*[参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则清除该]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播]{style="font-family:宋体"}[路由或组播路由的衰减信息，并解除对该路由的抑制。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[network-address mask]{lang="EN-US"}*]{#struct_0_65458_x3406_1255990488}[或]{lang="EN-US" style="font-family:宋体"}*[network-address mask-l]{lang="EN-US"}[ength]{lang="EN-US"}*[参数，则清除与指定目的网络]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址和网络掩码（或掩码长度）精确匹配的]{lang="EN-US" style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播]{lang="EN-US" style="font-family:宋体"}[路由]{lang="EN-US" style="font-family:宋体"}[或组播路由]{style="font-family:宋体"}[的衰减信息，并解除对该路由的抑制。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是，执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_2116559858}[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1730554119}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x162250230}[清除公网内到达网络]{style="font-family:宋体"}[20.1.0.0/16]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的衰减信息，并解除对该路由的抑制。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp dampening ipv4 20.1.0.0 255.255.0.0]{lang="EN-US"}]{#struct_0_65458_x3406_x967106401}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x602294668}[清除公网内到达网络]{style="font-family:宋体"}[2345::/16]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的衰减信息，并解除对该路由的抑制。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp dampening ipv6 2345:: 16]{lang="EN-US"}]{#struct_0_65458_x3406_x602229132}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x602098060}[清除到达网络]{style="font-family:宋体"}[1.2.3.4/32]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[组播路由的衰减信息，并解除对该路由的抑制。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp dampening ipv4 multicast 1.2.3.4 32]{lang="EN-US"}]{#struct_0_65458_x3406_x601966988}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x602294669}[清除到达网络]{style="font-family:宋体"}[2345::/16]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[组播路由的衰减信息，并解除对该路由的抑制。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp dampening ipv6 multicast 2345:: 16]{lang="EN-US"}]{#struct_0_65458_x3406_x602163597}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1090593693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_1720752037}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp routing-table dampened]{lang="EN-US"}**]{#struct_0_65458_x3406_x316334927}
:::

::: {#-1435714488 .myid}
[]{#_Toc404788693}[]{#struct_0_65458_x3406_x1393142444}[]{#_Toc307230815}[]{#_Toc366153353}[]{#_Toc366167096}[]{#_Toc366220408}[]{#_Toc366153354}[]{#_Toc366167097}[]{#_Toc366220409}[]{#_Toc366153355}[]{#_Toc366167098}[]{#_Toc366220410}[]{#_Toc366153356}[]{#_Toc366167099}[]{#_Toc366220411}[]{#_Toc366153357}[]{#_Toc366167100}[]{#_Toc366220412}[]{#_Toc366153358}[]{#_Toc366167101}[]{#_Toc366220413}[]{#_Toc366153359}[]{#_Toc366167102}[]{#_Toc366220414}[]{#_Toc366153360}[]{#_Toc366167103}[]{#_Toc366220415}[]{#_Toc366153361}[]{#_Toc366167104}[]{#_Toc366220416}[]{#_Toc366153362}[]{#_Toc366167105}[]{#_Toc366220417}[]{#_Toc366153363}[]{#_Toc366167106}[]{#_Toc366220418}[]{#_Toc366153364}[]{#_Toc366167107}[]{#_Toc366220419}[]{#_Toc366153365}[]{#_Toc366167108}[]{#_Toc366220420}[]{#_Toc366153366}[]{#_Toc366167109}[]{#_Toc366220421}[]{#_Toc366153367}[]{#_Toc366167110}[]{#_Toc366220422}[]{#_Toc366153368}[]{#_Toc366167111}[]{#_Toc366220423}[]{#_Toc366153369}[]{#_Toc366167112}[]{#_Toc366220424}[]{#_Toc366153370}[]{#_Toc366167113}[]{#_Toc366220425}[]{#_Toc366153371}[]{#_Toc366167114}[]{#_Toc366220426}[]{#_Toc366153372}[]{#_Toc366167115}[]{#_Toc366220427}

**BGP \-- BGP配置命令 \-- reset bgp flap-info**

------------------------------------------------------------------------

[**[reset bgp flap-info]{lang="EN-US"}**]{#struct_0_65458_x3406_338150191}[命令用来清除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[振荡统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1297998833}

[**[reset bgp flap-info ipv4 ]{lang="EN-US"}**[{ **multicast** ]{lang="EN-US"}[\| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *network-address* \[ *mask* \| *mask-length* \] \| **as-path-acl** *as-path-acl-number* \| **peer** *ipv4-address* \[ *mask-length* \] \]]{lang="EN-US"}]{#struct_0_65458_x3406_1256252632}

[**[reset bgp flap-info ipv6 ]{lang="EN-US"}**[{ **multicast** ]{lang="EN-US"}[\| \[ **unicast** \] \[ **vpn-instance** *vpn-instance-name* \] } \[ *network-address prefix-length* \| **as-path-acl** *as-path-acl-number* \| **peer** *ipv6-address* \[ *prefix-length* \] \]]{lang="EN-US"}]{#struct_0_65458_x3406_x601966983}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_827866138}

[[用户视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_390191547}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_520053071}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_506794828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x555442975}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_291309913}

[**[ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_x602294664}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[路由的]{style="font-family:宋体"}[振荡统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_65458_x3406_x602163592}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[路由的]{style="font-family:宋体"}[振荡统计信息。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x602098056}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[组播路由的]{style="font-family:宋体"}[振荡统计信息。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_x601966984}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[单播路由的]{style="font-family:宋体"}[振荡统计信息。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_65458_x3406_1697917156}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[振荡统计信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除公网]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[振荡统计信息。]{style="font-family:宋体"}

[*[network-address]{lang="EN-US"}*]{#struct_0_65458_x3406_1256187096}[：清除匹配指定目的网络地址的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_65458_x3406_x1084754770}[：目的网络地址的掩码，点分十进制格式。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_65458_x3406_1289743679}[：目的网络地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_65458_x3406_963985880}[：目的网络地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[as-path-acl ]{lang="EN-US"}***[as-path-acl-number]{lang="EN-US"}*]{#struct_0_65458_x3406_932053629}[：清除匹配指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[as-path-acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ ]{lang="EN-US"}*[ipv4-address ]{lang="EN-US"}*[\[ *mask-length* \]]{lang="EN-US"}]{#struct_0_65458_x3406_1559914536}[：]{style="font-family:宋体"}[清除从指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体学习到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}*[ipv4-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为网络掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ *ipv6*]{lang="EN-US"}*[-address ]{lang="EN-US"}*[\[ *prefix-length* \]]{lang="EN-US"}]{#struct_0_65458_x3406_964051421}[：]{style="font-family:宋体"}[清除从指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体学习到的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的振荡统计信息。]{style="font-family:宋体"}*[ipv6]{lang="EN-US"}[-address]{lang="EN-US"}*[为对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，如果指定本参数，则表示指定网段内的动态对等体。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_743592318}

[[执行]{style="font-family:宋体"}**[reset bgp flap-info ipv4]{lang="EN-US"}**]{#struct_0_65458_x3406_1893036305}[命令时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定了]{style="font-family:宋体"}]{#struct_0_65458_x3406_1233236057}*[network-address]{lang="EN-US"}*[参数，则将指定的网络地址和路由的掩码进行与操作，若计算结果与路由的网段地址相同，则清除该]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由或组播路由的振荡统计信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[network-address mask]{lang="EN-US"}*]{#struct_0_65458_x3406_224668714}[或]{lang="EN-US" style="font-family:宋体"}*[network-address mask-l]{lang="EN-US"}[ength]{lang="EN-US"}*[参数，则清]{lang="EN-US" style="font-family:宋体"}[除与指定目的网络]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址和网络掩码（或掩码长度）精确匹配的]{lang="EN-US" style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由]{lang="EN-US" style="font-family:宋体"}[或组播路由]{style="font-family:宋体"}[的振荡统计信息。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是，执行本命令时，如果没有指定]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**]{#struct_0_65458_x3406_1109192852}[和]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[参数，则缺省为]{style="font-family:宋体"}**[unicast]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1773222554}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x89907581}[清除公网内到达网络]{style="font-family:宋体"}[20.1.0.0/16]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv4 20.1.0.0 16]{lang="EN-US"}]{#struct_0_65458_x3406_x1477934319}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x2140064238}[清除从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[学习到的公网]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv4 peer 1.1.1.1]{lang="EN-US"}]{#struct_0_65458_x3406_1256580312}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1408470505}[清除公网内到达网络]{style="font-family:宋体"}[2345::/16]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv6 2345:: 16]{lang="EN-US"}]{#struct_0_65458_x3406_x1408404969}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1408929258}[清除从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[学习到的公网]{style="font-family:宋体"}[BGP IPv6]{lang="EN-US"}[单播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv6 peer 1::1]{lang="EN-US"}]{#struct_0_65458_x3406_x1408601578}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1408470506}[清除到达网络]{style="font-family:宋体"}[20.1.0.0/16]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv4 ]{lang="EN-US"}[组播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv4 multicast 20.1.0.0 16]{lang="EN-US"}]{#struct_0_65458_x3406_x1408404970}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1408929259}[清除从对等体]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[学习到的]{style="font-family:宋体"}[BGP IPv4 ]{lang="EN-US"}[组播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv4 multicast peer 1.1.1.1]{lang="EN-US"}]{#struct_0_65458_x3406_x1408601579}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1408470507}[清除到达网络]{style="font-family:宋体"}[2345::/16]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP IPv6 ]{lang="EN-US"}[组播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv6 multicast 2345:: 16]{lang="EN-US"}]{#struct_0_65458_x3406_x1408339435}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1408929260}[清除从对等体]{style="font-family:宋体"}[1::1]{lang="EN-US"}[学习到的]{style="font-family:宋体"}[BGP IPv6 ]{lang="EN-US"}[组播路由的振荡统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bgp flap-info ipv6 multicast peer 1::1]{lang="EN-US"}]{#struct_0_65458_x3406_x1408798188}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x736680849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dampening]{lang="EN-US"}**]{#struct_0_65458_x3406_x870980904}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp routing-table flap-info]{lang="EN-US"}**]{#struct_0_65458_x3406_1233847012}
:::

::: {#-704878201 .myid}
[]{#_Toc404788694}[]{#struct_0_65458_x3406_x194305547}[]{#_Toc293665257}[]{#_Toc251058600}[]{#_Toc319500505}[]{#_Toc319650267}[]{#_Toc319918760}[]{#_Toc319937824}[]{#_Toc319500506}[]{#_Toc319650268}[]{#_Toc319918761}[]{#_Toc319937825}[]{#_Toc319500507}[]{#_Toc319650269}[]{#_Toc319918762}[]{#_Toc319937826}[]{#_Toc319500508}[]{#_Toc319650270}[]{#_Toc319918763}[]{#_Toc319937827}[]{#_Toc319500509}[]{#_Toc319650271}[]{#_Toc319918764}[]{#_Toc319937828}[]{#_Toc319500510}[]{#_Toc319650272}[]{#_Toc319918765}[]{#_Toc319937829}[]{#_Toc319500511}[]{#_Toc319650273}[]{#_Toc319918766}[]{#_Toc319937830}[]{#_Toc319500512}[]{#_Toc319650274}[]{#_Toc319918767}[]{#_Toc319937831}[]{#_Toc319500513}[]{#_Toc319650275}[]{#_Toc319918768}[]{#_Toc319937832}[]{#_Toc319500514}[]{#_Toc319650276}[]{#_Toc319918769}[]{#_Toc319937833}[]{#_Toc319500515}[]{#_Toc319650277}[]{#_Toc319918770}[]{#_Toc319937834}[]{#_Toc319500516}[]{#_Toc319650278}[]{#_Toc319918771}[]{#_Toc319937835}[]{#_Toc319500517}[]{#_Toc319650279}[]{#_Toc319918772}[]{#_Toc319937836}[]{#_Toc319500518}[]{#_Toc319650280}[]{#_Toc319918773}[]{#_Toc319937837}[]{#_Toc319500519}[]{#_Toc319650281}[]{#_Toc319918774}[]{#_Toc319937838}[]{#_Toc319500520}[]{#_Toc319650282}[]{#_Toc319918775}[]{#_Toc319937839}[]{#_Toc319500521}[]{#_Toc319650283}[]{#_Toc319918776}[]{#_Toc319937840}[]{#_Toc319500522}[]{#_Toc319650284}[]{#_Toc319918777}[]{#_Toc319937841}[]{#_Toc319500523}[]{#_Toc319650285}[]{#_Toc319918778}[]{#_Toc319937842}[]{#_Toc319500524}[]{#_Toc319650286}[]{#_Toc319918779}[]{#_Toc319937843}[]{#_Toc366153374}[]{#_Toc366167117}[]{#_Toc366220429}[]{#_Toc366153375}[]{#_Toc366167118}[]{#_Toc366220430}[]{#_Toc366153376}[]{#_Toc366167119}[]{#_Toc366220431}[]{#_Toc366153377}[]{#_Toc366167120}[]{#_Toc366220432}[]{#_Toc366153378}[]{#_Toc366167121}[]{#_Toc366220433}[]{#_Toc366153379}[]{#_Toc366167122}[]{#_Toc366220434}[]{#_Toc366153380}[]{#_Toc366167123}[]{#_Toc366220435}[]{#_Toc366153381}[]{#_Toc366167124}[]{#_Toc366220436}[]{#_Toc366153382}[]{#_Toc366167125}[]{#_Toc366220437}[]{#_Toc366153383}[]{#_Toc366167126}[]{#_Toc366220438}[]{#_Toc366153384}[]{#_Toc366167127}[]{#_Toc366220439}[]{#_Toc366153385}[]{#_Toc366167128}[]{#_Toc366220440}[]{#_Toc366153386}[]{#_Toc366167129}[]{#_Toc366220441}[]{#_Toc366153387}[]{#_Toc366167130}[]{#_Toc366220442}[]{#_Toc366153388}[]{#_Toc366167131}[]{#_Toc366220443}[]{#_Toc366153389}[]{#_Toc366167132}[]{#_Toc366220444}[]{#_Toc366153390}[]{#_Toc366167133}[]{#_Toc366220445}[]{#_Toc366153391}[]{#_Toc366167134}[]{#_Toc366220446}[]{#_Toc366153392}[]{#_Toc366167135}[]{#_Toc366220447}[]{#_Toc366153393}[]{#_Toc366167136}[]{#_Toc366220448}[]{#_Toc366153394}[]{#_Toc366167137}[]{#_Toc366220449}[]{#_Toc366153395}[]{#_Toc366167138}[]{#_Toc366220450}[]{#_Toc366153396}[]{#_Toc366167139}[]{#_Toc366220451}[]{#_Toc366153397}[]{#_Toc366167140}[]{#_Toc366220452}[]{#_Toc366153398}[]{#_Toc366167141}[]{#_Toc366220453}[]{#_Toc366153399}[]{#_Toc366167142}[]{#_Toc366220454}[]{#_Toc366153400}[]{#_Toc366167143}[]{#_Toc366220455}[]{#_Toc366153401}[]{#_Toc366167144}[]{#_Toc366220456}[]{#_Toc366153402}[]{#_Toc366167145}[]{#_Toc366220457}[]{#_Toc366153403}[]{#_Toc366167146}[]{#_Toc366220458}[]{#_Toc366153404}[]{#_Toc366167147}[]{#_Toc366220459}[]{#_Toc366153405}[]{#_Toc366167148}[]{#_Toc366220460}[]{#_Toc366153406}[]{#_Toc366167149}[]{#_Toc366220461}[]{#_Toc366153407}[]{#_Toc366167150}[]{#_Toc366220462}[]{#_Toc366153408}[]{#_Toc366167151}[]{#_Toc366220463}[]{#_Toc366153409}[]{#_Toc366167152}[]{#_Toc366220464}[]{#_Toc366153410}[]{#_Toc366167153}[]{#_Toc366220465}[]{#_Toc366153411}[]{#_Toc366167154}[]{#_Toc366220466}[]{#_Toc366153412}[]{#_Toc366167155}[]{#_Toc366220467}[]{#_Toc366153413}[]{#_Toc366167156}[]{#_Toc366220468}[]{#_Toc366153414}[]{#_Toc366167157}[]{#_Toc366220469}[]{#_Toc366153415}[]{#_Toc366167158}[]{#_Toc366220470}[]{#_Toc366153416}[]{#_Toc366167159}[]{#_Toc366220471}[]{#_Toc366153417}[]{#_Toc366167160}[]{#_Toc366220472}[]{#_Toc366153418}[]{#_Toc366167161}[]{#_Toc366220473}[]{#_Toc366153419}[]{#_Toc366167162}[]{#_Toc366220474}[]{#_Toc366153420}[]{#_Toc366167163}[]{#_Toc366220475}[]{#_Toc366153421}[]{#_Toc366167164}[]{#_Toc366220476}[]{#_Toc366153422}[]{#_Toc366167165}[]{#_Toc366220477}[]{#_Toc366153423}[]{#_Toc366167166}[]{#_Toc366220478}[]{#_Toc366153424}[]{#_Toc366167167}[]{#_Toc366220479}[]{#_Toc366153425}[]{#_Toc366167168}[]{#_Toc366220480}[]{#_Toc366153426}[]{#_Toc366167169}[]{#_Toc366220481}[]{#_Toc366153427}[]{#_Toc366167170}[]{#_Toc366220482}[]{#_Toc366153428}[]{#_Toc366167171}[]{#_Toc366220483}[]{#_Toc366153429}[]{#_Toc366167172}[]{#_Toc366220484}[]{#_Toc366153430}[]{#_Toc366167173}[]{#_Toc366220485}[]{#_Toc366153431}[]{#_Toc366167174}[]{#_Toc366220486}[]{#_Toc366153432}[]{#_Toc366167175}[]{#_Toc366220487}[]{#_Toc366153433}[]{#_Toc366167176}[]{#_Toc366220488}[]{#_Toc366153434}[]{#_Toc366167177}[]{#_Toc366220489}[]{#_Toc366153435}[]{#_Toc366167178}[]{#_Toc366220490}[]{#_Toc366153436}[]{#_Toc366167179}[]{#_Toc366220491}[]{#_Toc366153437}[]{#_Toc366167180}[]{#_Toc366220492}[]{#_Toc366153438}[]{#_Toc366167181}[]{#_Toc366220493}[]{#_Toc366153439}[]{#_Toc366167182}[]{#_Toc366220494}[]{#_Toc366153440}[]{#_Toc366167183}[]{#_Toc366220495}[]{#_Toc366153441}[]{#_Toc366167184}[]{#_Toc366220496}[]{#_Toc366153442}[]{#_Toc366167185}[]{#_Toc366220497}[]{#_Toc366153443}[]{#_Toc366167186}[]{#_Toc366220498}[]{#_Toc366153444}[]{#_Toc366167187}[]{#_Toc366220499}[]{#_Toc366153445}[]{#_Toc366167188}[]{#_Toc366220500}[]{#_Toc366153446}[]{#_Toc366167189}[]{#_Toc366220501}[]{#_Toc366153447}[]{#_Toc366167190}[]{#_Toc366220502}[]{#_Toc366153448}[]{#_Toc366167191}[]{#_Toc366220503}[]{#_Toc366153449}[]{#_Toc366167192}[]{#_Toc366220504}[]{#_Toc366153450}[]{#_Toc366167193}[]{#_Toc366220505}[]{#_Toc366153451}[]{#_Toc366167194}[]{#_Toc366220506}[]{#_Toc366153452}[]{#_Toc366167195}[]{#_Toc366220507}[]{#_Toc366153453}[]{#_Toc366167196}[]{#_Toc366220508}[]{#_Toc366153454}[]{#_Toc366167197}[]{#_Toc366220509}[]{#_Toc366153455}[]{#_Toc366167198}[]{#_Toc366220510}[]{#_Toc366153456}[]{#_Toc366167199}[]{#_Toc366220511}[]{#_Toc366153457}[]{#_Toc366167200}[]{#_Toc366220512}[]{#_Toc366153458}[]{#_Toc366167201}[]{#_Toc366220513}[]{#_Toc366153459}[]{#_Toc366167202}[]{#_Toc366220514}[]{#_Toc366153460}[]{#_Toc366167203}[]{#_Toc366220515}[]{#_Toc366153461}[]{#_Toc366167204}[]{#_Toc366220516}[]{#_Toc366153462}[]{#_Toc366167205}[]{#_Toc366220517}

**BGP \-- BGP配置命令 \-- router id**

------------------------------------------------------------------------

[**[router id]{lang="EN-US"}**]{#struct_0_65458_x3406_2043773849}[命令用来配置全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo router id]{lang="EN-US"}**]{#struct_0_65458_x3406_1256580313}[命令用来删除已配置的全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x736746385}

[**[router id ]{lang="EN-US"}***[router-id]{lang="EN-US"}*]{#struct_0_65458_x3406_x2103576185}

[**[undo router id]{lang="EN-US"}**]{#struct_0_65458_x3406_x1785491838}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_855922430}

[[未配置全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_1898277999}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1083388543}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x852012374}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1256514777}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_2012697085}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x559321735}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_733773225}

[*[router-id]{lang="EN-US"}*]{#struct_0_65458_x3406_x1813126141}[：全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的形式标识。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_201300042}

[[一些动态路由协议要求使用]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1723139930}[，如果在启动这些路由协议时没有指定]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，则缺省使用全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[如果配置了全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_1406140851}[，则使用配置的值作为]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。如果没有配置全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，则按照下面的规则进行选择：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果存在配置]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_1256056022}[地址的]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，则选择]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址中最大的作为]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果没有配置]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_65458_x3406_1650223473}[地址的]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，则从其他接口的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址中选择最大的作为]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[（不考虑接口的]{lang="EN-US" style="font-family:宋体"}[up/down]{lang="EN-US"}[状态）。]{lang="EN-US" style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果所有接口上都没有配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_x591607932}[IP]{lang="EN-US"}[地址，则]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1832740096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[存在主备的情况下]{style="font-family:宋体"}]{#struct_0_65458_x3406_x173382457}[，]{style="font-family:宋体"}[系统将备份命令行配置的]{style="font-family:宋体"}[Router ID]{lang="FR"}[或从接口地址中选择出来的]{style="font-family:宋体"}[Router ID]{lang="FR"}[。主备倒换后，系统将检查从地址中选出的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[的有效性，如果无效将重新进行选择。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当且仅当被选为]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1631065255}[Router ID]{lang="EN-US"}[的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址被删除或被修改时，才触发重新选择过程，其他情况（例如：接口]{style="font-family:宋体"}[down]{lang="EN-US"}[；已经选取了一个非]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址后又配置了一个]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址；配置一个更大的接口地址等）不触发重新选择的过程。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_411046403}[改变之后，各协议需要通过手工执行]{lang="EN-US" style="font-family:宋体"}**[reset]{lang="EN-US"}**[命令才会获取新的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1428110575}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1255990486}[配置全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_2116166642}

[\[Sysname\] router id 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x637279883}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[router-id]{lang="EN-US"}**]{#struct_0_65458_x3406_803148325}
:::

::: {#1741398308 .myid}
[]{#_Toc263170170}[]{#_Toc261504262}[]{#_Toc180224240}[]{#_Toc138238306}[]{#_Toc94930974}[]{#_Toc94586706}[]{#_Toc60036320}[]{#_Toc53707263}[]{#_Toc53518736}[]{#_Toc50837044}[]{#_Toc43895309}[]{#_Toc404788695}[]{#struct_0_65458_x3406_56009432}

**BGP \-- BGP配置命令 \-- router-id (BGP view)**

------------------------------------------------------------------------

[**[router-id]{lang="EN-US"}**]{#struct_0_65458_x3406_223125255}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo router-id]{lang="EN-US"}**]{#struct_0_65458_x3406_x832704117}[命令用来删除配置的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1255924950}

[**[router-id]{lang="EN-US"}**[ *router-id*]{lang="EN-US"}]{#struct_0_65458_x3406_x523611773}

[**[undo router-id]{lang="EN-US"}**]{#struct_0_65458_x3406_495023671}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1811917649}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_2146094512}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[与全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[相同。可以通过在系统视图下执行]{style="font-family:宋体"}**[router id]{lang="EN-US"}**[命令，修改全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_237659370}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x2035638972}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_960472696}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1255859414}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x248228795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1700967803}

[*[router-id]{lang="EN-US"}*]{#struct_0_65458_x3406_1159561363}[：]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的形式标识。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1775153101}

[[一台路由器如果要运行]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_970369410}[协议，则必须存在]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。它是一个]{style="font-family:宋体"}[32]{lang="EN-US"}[比特无符号整数，是一台路由器在自治系统中的唯一标识。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x132705349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1799775317}[路由器]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[一旦确定]{lang="EN-US" style="font-family:宋体"}[为非零值]{style="font-family:宋体"}[后不会随着系统视图下]{lang="EN-US" style="font-family:宋体"}**[router id]{lang="EN-US"}**[命令配置的改变而改变。只能在]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下通过]{lang="EN-US" style="font-family:宋体"}**[router-id]{lang="EN-US"}**[命令改变]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了增加网络的可靠性，建议将]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_1256318166}[手工配置为]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个视图下重复执行本命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_65458_x3406_x747517430}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1691301336}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_2132783975}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下]{style="font-family:宋体"}[，指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x239567589}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] router-id 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x185039701}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[router]{lang="EN-US"}**]{#struct_0_65458_x3406_2495433}**[ ]{lang="EN-US"}[id]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[router]{lang="EN-US"}**]{#struct_0_65458_x3406_1256252630}**[-]{lang="EN-US"}[id]{lang="EN-US"}[ ]{lang="EN-US"}**[(BGP-VPN view)]{lang="EN-US"}
:::

::: {#1702359038 .myid}
[]{#_Toc404788696}[]{#struct_0_65458_x3406_827997210}

**BGP \-- BGP配置命令 \-- router-id (BGP-VPN view)**

------------------------------------------------------------------------

[**[router-id]{lang="EN-US"}**]{#struct_0_65458_x3406_773077229}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器在指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo router-id]{lang="EN-US"}**]{#struct_0_65458_x3406_600368124}[命令用来删除配置的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1462535722}

[**[router-id]{lang="EN-US"}**[ { *router-id* \| **auto-select** }]{lang="EN-US"}]{#struct_0_65458_x3406_809252844}

[**[undo router-id]{lang="EN-US"}**]{#struct_0_65458_x3406_x1842819819}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1215967857}

[[未指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_1256187094}[路由器在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。如果在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下执行了]{style="font-family:宋体"}**[router-id]{lang="EN-US"}**[命令，则]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为该命令配置的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[；否则，为系统视图下通过]{style="font-family:宋体"}**[router id]{lang="EN-US"}**[命令配置的全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1084885842}

[[BGP-VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x960575575}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1226205231}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_618387022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1836164361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x919750443}

[*[router-id]{lang="EN-US"}*]{#struct_0_65458_x3406_x1834495300}[：]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的形式标识。]{style="font-family:宋体"}

[**[auto-select]{lang="EN-US"}**]{#struct_0_65458_x3406_1256121558}[：自动选取该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1232711772}

[[一台路由器如果要在某个]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_65458_x3406_x173498330}[实例内运行]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议，则必须为其指定在该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[是一个]{style="font-family:宋体"}[32]{lang="EN-US"}[比特无符号整数，是一台路由器在自治系统中的唯一标识。]{style="font-family:宋体"}

[[执行]{style="font-family:宋体"}**[router-id]{lang="EN-US"}**[ **auto-select**]{lang="EN-US"}]{#struct_0_65458_x3406_1947622824}[命令后，该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[选取原则为：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果存在]{lang="EN-US" style="font-family:宋体"}]{#struct_0_65458_x3406_1133533788}[属于当前]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例、且已]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，则选择]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址中最大的作为]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果不存在满足上述条件的]{style="font-family:宋体"}]{#struct_0_65458_x3406_2088208667}[Loopback]{lang="EN-US"}[接口，则从其他属于当前]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的接口中，选择最大的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[（不考虑接口的]{style="font-family:宋体"}[up/down]{lang="EN-US"}[状态）。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果不存在属于当前]{style="font-family:宋体"}]{#struct_0_65458_x3406_1907017169}[VPN]{lang="EN-US"}[实例的接口地址，则]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[当前]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_65458_x3406_1256580310}[实例内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[一旦确定为非零值，即使存在满足选取原则的更优的接口地址，系统也不会重新选择]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_x736811921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了增加网络的可靠性，建议将]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_65458_x3406_x1284477315}[手工配置为]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一台设备上，可以为不同的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_65458_x3406_1949658686}[实例指定不同的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个视图下重复执行本命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1330243700}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x242120200}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x598404917}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由器的]{style="font-family:宋体"}[Router ID]{lang="FR"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1256514774}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] router-id ]{lang="EN-US"}[1.1.1.1]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2012762621}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[router]{lang="EN-US"}**]{#struct_0_65458_x3406_x531886255}**[ ]{lang="EN-US"}[id]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[router]{lang="EN-US"}**]{#struct_0_65458_x3406_x39323171}**[-]{lang="EN-US"}[id]{lang="EN-US"}[ ]{lang="EN-US"}**[(BGP view)]{lang="EN-US"}
:::

::: {#-1325709270 .myid}
[]{#_Toc263170173}[]{#_Toc261504265}[]{#_Toc180224243}[]{#_Toc138238309}[]{#_Toc316646904}[]{#_Toc261504263}[]{#_Toc180224241}[]{#_Toc138238307}[]{#_Toc404788697}[]{#struct_0_65458_x3406_x682839833}[]{#_Toc327365449}

**BGP \-- BGP配置命令 \-- snmp-agent trap enable bgp**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable bgp**]{lang="EN-US"}]{#struct_0_65458_x3406_x1600842445}[命令用来开启]{style="font-family:宋体"}[BGP]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable bgp**]{lang="EN-US"}]{#struct_0_65458_x3406_660185778}[命令用来关闭]{style="font-family:宋体"}[BGP]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_988702005}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **bgp**]{lang="EN-US"}]{#struct_0_65458_x3406_1256056023}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **bgp**]{lang="EN-US"}]{#struct_0_65458_x3406_1650289009}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1663784335}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1188157997}[模块的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1744229007}

[[系统视图]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2086953921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x619290082}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1796615694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1255990487}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_2116232178}

[[开启]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1769599193}[模块的告警功能后，当]{style="font-family:宋体"}[BGP]{lang="EN-US"}[的邻居状态变化时]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会产生]{style="font-family:宋体"}[RFC 4273]{lang="EN-US"}[中规定的告警信息，该信息包含邻居地址、最近一次出现错误的错误码和错误子码、当前的邻居状态。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_65458_x3406_1333757199}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x758204702}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x176545926}[开启]{style="font-family:宋体"}[BGP]{lang="EN-US"}[模块的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_902062127}

[\[Sysname\] snmp-agent trap enable bgp]{lang="EN-US"}
:::

::: {#1635242134 .myid}
[]{#_Toc404788698}[]{#struct_0_65458_x3406_1511310810}

**BGP \-- BGP配置命令 \-- summary automatic**

------------------------------------------------------------------------

[**[summary automatic]{lang="EN-US"}**]{#struct_0_65458_x3406_1255924951}[命令用来配置对引入的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[子网路由进行自动聚合。]{style="font-family:宋体"}

[**[undo summary automatic]{lang="EN-US"}**]{#struct_0_65458_x3406_x523677309}[命令用来取消对引入的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[子网路由进行自动聚合。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1420129026}

[**[summary automatic]{lang="EN-US"}**]{#struct_0_65458_x3406_432140163}

[**[undo summary automatic]{lang="EN-US"}**]{#struct_0_65458_x3406_1947112443}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1162454395}

[[不对引入的]{style="font-family:宋体"}[IGP]{lang="EN-US"}]{#struct_0_65458_x3406_1516675292}[子网路由进行自动聚合。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1052140220}

[[BGP IPv4]{lang="EN-US"}]{#struct_0_65458_x3406_1255859415}[单播地址族视图]{style="font-family:宋体"}[/BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图]{style="font-family:宋体"}[/BGP IPv4]{lang="EN-US"}[组播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x248163259}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_1328454701}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x910597904}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_306988825}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[summary automatic]{lang="EN-US"}**]{#struct_0_65458_x3406_798663941}[命令]{style="font-family:宋体"}[后，]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[将对通过]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**[命令]{style="font-family:宋体"}[引入的]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}[子网路由]{lang="EN-US" style="font-family:宋体"}[进行聚合]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[从而]{style="font-family:宋体"}[减少路由信息的数量。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[自动聚合生成的路由可以参与手动聚合。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1945447560}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[自动聚合生成的路由不会加入到]{style="font-family:宋体"}]{#struct_0_65458_x3406_x1844904887}[IP]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1256318167}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x747451894}[在]{style="font-family:宋体"}[BGP IPv4]{lang="EN-US"}[单播地址族视图下，对引入的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[子网路由进行自动聚合。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x210663951}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4\] summary automatic]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1823962385}[在]{style="font-family:宋体"}[BGP-VPN IPv4]{lang="EN-US"}[单播地址族视图下，对引入的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[子网路由进行自动聚合。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x849929225}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] address-family ipv4 unicast]{lang="EN-US"}

[\[Sysname-bgp-ipv4-vpn1\]  summary automatic]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_739126052}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aggregate]{lang="PT-BR"}**]{#struct_0_65458_x3406_1256252631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_65458_x3406_828062746}
:::

::: {#-1113860339 .myid}
[]{#_Toc404788699}[]{#struct_0_65458_x3406_699264656}

**BGP \-- BGP配置命令 \-- timer**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1992481998}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔和保持时间。]{style="font-family:宋体"}

[**[undo timer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1214084565}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1936500253}

[**[timer]{lang="EN-US"}**[ **keepalive** *keepalive* **hold** *holdtime*]{lang="EN-US"}]{#struct_0_65458_x3406_1947473013}

[**[undo timer]{lang="EN-US"}**]{#struct_0_65458_x3406_1256187095}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1084951378}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_251873379}[会话的存活时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒，保持时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1036346708}

[[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x1222436374}[视图]{style="font-family:宋体"}[/BGP-VPN]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x145179199}

[[network-admin]{lang="EN-US"}]{#struct_0_65458_x3406_735914551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_65458_x3406_x1830566810}

[[【参数】]{style="font-family:黑体"}]{#struct_0_65458_x3406_1256121559}

[**[keepalive]{lang="EN-US"}***[ keepalive]{lang="EN-US"}*]{#struct_0_65458_x3406_1232646236}[：指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔。]{style="font-family:宋体"}*[keepalive]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[21845]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[hold]{lang="EN-US"}***[ holdtime]{lang="EN-US"}*]{#struct_0_65458_x3406_x188011616}[：指定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的保持时间。]{style="font-family:宋体"}*[holdtime]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:
宋体"}[65535]{lang="EN-US"}[，单位为秒。保持时间]{style="font-family:宋体"}[必须大于或等于存活时间的三倍。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_65458_x3406_481343648}

[[当对等体间建立了]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_65458_x3406_x60761644}[会话后，它们定时向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息，以防止路由器认为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话已中断。]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息的发送时间间隔称为存活时间间隔。]{style="font-family:宋体"}

[[若路由器在设定的会话保持时间（]{style="font-family:宋体"}[Holdtime]{lang="EN-US"}]{#struct_0_65458_x3406_1010817757}[）内未收到对端的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息或]{style="font-family:宋体"}[Update]{lang="EN-US"}[消息，则认为此]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话已中断，从而断开此]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_65458_x3406_381974715}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer]{lang="EN-US"}**]{#struct_0_65458_x3406_x470847130}[命令用来配置本地路由器与所有对等体之间]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[会话的]{style="font-family:宋体"}[存活时间间隔和保持时间；]{style="font-family:宋体"}**[peer timer]{lang="EN-US"}**[命令用来配置本地路由器与指定对等体之间]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的]{style="font-family:宋体"}[存活时间间隔和保持时间。]{style="font-family:宋体"}[如果同时配置了二者，则使用]{lang="EN-US" style="font-family:
宋体"}**[timer]{lang="EN-US"}**[命令配置的定时器比使用]{lang="EN-US" style="font-family:宋体"}**[peer timer]{lang="EN-US"}**[命令配置的定时器优先级要低。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果当前路由器上配置的保持时间与对端设备（对等体）上配置的保持时间不一致，则数值较小者作为协商后的保持时间。]{style="font-family:宋体"}]{#struct_0_65458_x3406_1256580311}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[保持时间为]{style="font-family:宋体"}]{#struct_0_65458_x3406_x736877457}[0]{lang="EN-US"}[时，不向该对等体发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[消息，与该对等体之间的会话永远不会超时断开；存活时间间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[，协商的保持时间不为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，以协商的保持时间的三分之一作为存活时间间隔；当保持时间和存活时间间隔都不为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，将协商的保持时间的三分之一与配置的存活时间间隔比较，取最小值作为存活时间间隔。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_1792050498}**[timer]{lang="EN-US"}**[命令后，不会影响已建立的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话，只对新建立的会话生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_65458_x3406_x2130552667}**[timer]{lang="EN-US"}**[命令后，不会马上断开会话，而是等到其他条件触发会话重建（如复位]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话）时，再以配置的保持时间协商建立会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x736023552}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x2120657338}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔和保持时间分别为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒和]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_65458_x3406_x2081538012}

[\[Sysname\] bgp 100]{lang="DA"}

[\[Sysname-bgp\] timer keepalive 60 hold 180]{lang="DA"}[]{#_Toc34799200}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_1760405003}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔和保持时间分别为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒和]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_1256514775}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] timer keepalive 60 hold 180]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_2012828157}[在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[视图下，配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔和保持时间均为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，表示会话永不超时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_65458_x3406_x577790855}

[\[Sysname\] bgp 100]{lang="DA"}

[\[Sysname-bgp\] timer keepalive 0 hold 0]{lang="DA"}

[[\# ]{lang="EN-US"}]{#struct_0_65458_x3406_x1783889244}[在]{style="font-family:宋体"}[BGP-VPN]{lang="EN-US"}[实例视图下，]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[会话的存活时间间隔与保持时间分别均为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒]{style="font-family:宋体"}[，表示会话永不超时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_65458_x3406_x1601388371}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] ip vpn-instance vpn1]{lang="EN-US"}

[\[Sysname-bgp-vpn1\] timer keepalive 0 hold 0]{lang="EN-US"}[]{#_Ref533495796}[]{#_Hlt24602234}[]{#_Toc228610382}[]{#_Toc228610383}[]{#_Toc228610384}[]{#_Hlt20818899}[]{#_Toc228610386}[]{#_Toc228610387}[]{#_Toc228610388}[]{#_Toc253237964}[]{#_Toc269821362}[]{#_Toc269821423}[]{#_Toc253237967}[]{#_Toc269821365}[]{#_Toc269821426}[]{#_Toc253237968}[]{#_Toc269821366}[]{#_Toc269821427}[]{#_Toc253237970}[]{#_Toc269821368}[]{#_Toc269821429}[]{#_Toc253237973}[]{#_Toc269821371}[]{#_Toc269821432}[]{#_Toc253237974}[]{#_Toc269821372}[]{#_Toc269821433}[]{#_Toc253237983}[]{#_Toc269821383}[]{#_Toc269821444}[]{#_Toc253237986}[]{#_Toc269821386}[]{#_Toc269821447}[]{#_Toc253237987}[]{#_Toc269821387}[]{#_Toc269821448}[]{#_Toc253237989}[]{#_Toc269821389}[]{#_Toc269821450}[]{#_Toc253237992}[]{#_Toc269821392}[]{#_Toc269821453}[]{#_Hlt2479412}[]{#_Toc253237999}[]{#_Toc269821400}[]{#_Toc269821461}[]{#_Toc253238002}[]{#_Toc269821403}[]{#_Toc269821464}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_65458_x3406_x1472827329}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display bgp peer]{lang="EN-US"}**]{#struct_0_65458_x3406_1016983490}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer timer]{lang="EN-US"}**]{#struct_0_65458_x3406_x1934971899}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
