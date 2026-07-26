::: {#-1744116002 .myid}
[]{#_Toc404789860}[]{#struct_0_x1693_29802_1879733382}[]{#_Toc365900725}

**组播VPN \-- 组播VPN配置命令 \-- address-family ipv4 mdt**

------------------------------------------------------------------------

[**[address-family ipv4 mdt]{lang="EN-US"}**]{#struct_0_x1693_29802_x928077511}[命令用来创建]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族，并进入]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[**[undo address-family ipv4 mdt]{lang="EN-US"}**]{#struct_0_x1693_29802_1879667846}[命令用来删除]{style="font-family:
宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族及该视图下的所有配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_575306696}

[**[address-family ipv4 mdt]{lang="EN-US"}**]{#struct_0_x1693_29802_1825069160}

[**[undo address-family ipv4 mdt]{lang="EN-US"}**]{#struct_0_x1693_29802_1722830169}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1130443485}

[[没有创建]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}]{#struct_0_x1693_29802_x2073196230}[地址族。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1343455586}

[[BGP]{lang="EN-US"}]{#struct_0_x1693_29802_x1579096695}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x477541416}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_1880388742}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x938159431}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x978644404}

[[只有创建]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}]{#struct_0_x1693_29802_x1142237907}[地址族，并在]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族下通过]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[ **enable**]{lang="EN-US"}[命令使能]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组后，本地路由器才能与指定的对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组交换]{style="font-family:宋体"}[MDT]{lang="EN-US"}[信息，该信息包含]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址及]{style="font-family:宋体"}[PE]{lang="EN-US"}[所在的]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[等信息。在公网中运行]{style="font-family:宋体"}[PIM-SSM]{lang="EN-US"}[时，组播]{style="font-family:宋体"}[VPN]{lang="EN-US"}[根据]{style="font-family:宋体"}[MDT]{lang="EN-US"}[信息在公网上建立以]{style="font-family:宋体"}[PE]{lang="EN-US"}[为根（即组播源）的]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[。]{style="font-family:宋体"}

[[BGP IPv4 MDT]{lang="EN-US"}]{#struct_0_x1693_29802_1503603181}[地址族视图下的配置，只对]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[信息和]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[对等体]{style="font-family:宋体"}[/]{lang="EN-US"}[对等体组生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x761417964}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_1096765830}[创建]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族，并进入]{style="font-family:宋体"}[BGP IPv4 MDT]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_1880323206}

[\[Sysname\] bgp 100]{lang="EN-US"}

[\[Sysname-bgp\] address-family ipv4 mdt]{lang="EN-US"}

[\[Sysname-bgp-mdt\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x610925830}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1693_29802_x1598017325}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/BGP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#1639499420 .myid}
[]{#_Toc299461496}[]{#_Toc94588230}[]{#_Toc80176777}[]{#_Toc327804448}[]{#_Toc404789861}[]{#struct_0_x1693_29802_x778267398}[]{#_Toc347846328}[]{#_Toc346528397}[]{#_Toc327804444}

**组播VPN \-- 组播VPN配置命令 \-- data-delay**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1693_29802_x923973412}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1693_29802_870735759}
:::

[ ]{lang="EN-US"}

[**[data-delay]{lang="EN-US"}**]{#struct_0_x1693_29802_x1632692970}[命令用来配置由]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[向]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[切换的延迟时间。]{style="font-family:宋体"}

[**[undo data-delay]{lang="EN-US"}**]{#struct_0_x1693_29802_1889777901}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x822356766}

[**[data-delay]{lang="EN-US"}**[ *delay*]{lang="EN-US"}]{#struct_0_x1693_29802_727062471}

[**[undo data-delay]{lang="EN-US"}**]{#struct_0_x1693_29802_x1007751994}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x350437422}

[[由]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}]{#struct_0_x1693_29802_1438761550}[向]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[切换的延迟时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_441557028}

[[MD]{lang="EN-US"}]{#struct_0_x1693_29802_x2116685763}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_971076270}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x1632758506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x1239138057}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1965471184}

[*[delay]{lang="EN-US"}*]{#struct_0_x1693_29802_x693192038}[：表示延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1539228564}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_x2015983758}[配置]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[中由]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[向]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[切换的延迟时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_x1849935497}

[\[Sysname\] multicast-domain vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-md-mvpn\] data-delay 20]{lang="EN-US"}
:::::

::::: {#1697116571 .myid}
[]{#_Toc404789862}[]{#struct_0_x1693_29802_942111302}[]{#_Toc347846329}[]{#_Toc346528398}[]{#_Toc327804445}

**组播VPN \-- 组播VPN配置命令 \-- data-group**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1693_29802_x733499496}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1693_29802_x1632299754}
:::

[ ]{lang="EN-US"}

[**[data-group]{lang="EN-US"}**]{#struct_0_x1693_29802_509404803}[命令用来配置]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[的范围和切换条件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **data-group**]{lang="EN-US"}]{#struct_0_x1693_29802_x814701870}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1826250276}

[**[data-group]{lang="EN-US"}**[ *group-address* { *mask-length* \| *mask* } \[ **acl** *acl-number* \| **threshold** *threshold-value* \] \*]{lang="EN-US"}]{#struct_0_x1693_29802_851457059}

[**[undo]{lang="EN-US"}**[ **data-group**]{lang="EN-US"}]{#struct_0_x1693_29802_x385147295}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1331649999}

[[没有指定]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_x122442015}[的范围，也永不向]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[进行切换。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_384166541}

[[MD]{lang="EN-US"}]{#struct_0_x1693_29802_x1632365290}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_811381779}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x1927179190}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_550897461}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1546970185}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1693_29802_1543455414}[：表示组播组地址，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1693_29802_616949121}[：表示组播组地址的掩码长度。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x1693_29802_x623138209}[：表示组播组地址的掩码。不同型号的设备支持的取值范围不同，请以设备的实际情况为准]{style="font-family:宋体"}

[**[acl]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x1693_29802_x228481620}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。本参数用来指定]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[作用的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项；如果未指定本参数，则作用于所有（]{style="font-family:
宋体"}[S]{lang="EN-US"}[，]{style="font-family:
宋体"}[G]{lang="EN-US"}[）表项。在定义该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时，只允许使用]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中类型为]{style="font-family:宋体"}**[ip]{lang="EN-US"}**[的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[和]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[参数来分别指定]{style="font-family:宋体"}[S]{lang="EN-US"}[和]{style="font-family:宋体"}[G]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[threshold]{lang="EN-US"}**[ *threshold-value*]{lang="EN-US"}]{#struct_0_x1693_29802_x1632824045}[：表示切换阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777216]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0kbps]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1693_29802_488411906}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1693_29802_1122775503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一台设备上，]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_1196610990}[的]{style="font-family:宋体"}[范围不能包含任何]{lang="EN-US" style="font-family:宋体"}[MD]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Default-Group]{lang="EN-US"}[，也不能与其它任何]{style="font-family:宋体"}[MD]{lang="EN-US"}[的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[范围重叠]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在不同设备上，如果公网为非]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1693_29802_414275698}[PIM-]{lang="EN-US"}[SSM]{lang="EN-US"}[模式，则不同]{lang="EN-US" style="font-family:宋体"}[MD]{lang="EN-US"}[不能配置重叠的]{lang="EN-US" style="font-family:宋体"}[Data-Group]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个]{style="font-family:宋体"}]{#struct_0_x1693_29802_549811086}[MD]{lang="EN-US"}[下进行重复配置时，新配置将覆盖旧配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1693_29802_1662076804}[不支持]{lang="EN-US" style="font-family:宋体"}**[threshold]{lang="EN-US"}**[ *threshold-value*]{lang="EN-US"}[参数]{lang="EN-US" style="font-family:
宋体"}[的设备]{style="font-family:宋体"}[上配置了本命令后，当有满足条件的流量且维持了]{lang="EN-US" style="font-family:宋体"}[Data-Delay]{lang="EN-US"}[时间后就发起向]{lang="EN-US" style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[的切换。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_416878445}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_1339691421}[配置]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[中]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[的范围为从]{style="font-family:宋体"}[239.1.2.0]{lang="EN-US"}[到]{style="font-family:宋体"}[239.1.2.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_x1632889581}

[\[Sysname\] multicast-domain vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-md-mvpn\] data-group 239.1.2.0 24]{lang="EN-US"}
:::::

::::: {#427559692 .myid}
[]{#_Toc404789863}[]{#struct_0_x1693_29802_1671501211}[]{#_Toc347846330}[]{#_Toc346528399}[]{#_Toc327804446}

**组播VPN \-- 组播VPN配置命令 \-- data-holddown**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1693_29802_x2079277113}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1693_29802_764593888}
:::

[ ]{lang="EN-US"}

[**[data-holddown]{lang="EN-US"}**]{#struct_0_x1693_29802_x1388523512}[命令用来配置由]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[向]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[反向切换的延迟时间。]{style="font-family:宋体"}

[**[undo data-holddown]{lang="EN-US"}**]{#struct_0_x1693_29802_944233763}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_2020023037}

[**[data-holddown]{lang="EN-US"}**[ *delay*]{lang="EN-US"}]{#struct_0_x1693_29802_x1235057357}

[**[undo data-holddown]{lang="EN-US"}**]{#struct_0_x1693_29802_x347650211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1632955117}

[[由]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}]{#struct_0_x1693_29802_3913110}[向]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[反向切换的延迟时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_180352295}

[[MD]{lang="EN-US"}]{#struct_0_x1693_29802_264780302}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1611972943}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_389618379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x69012940}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x964096978}

[*[delay]{lang="EN-US"}*]{#struct_0_x1693_29802_x549659649}[：表示延迟时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[180]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1633020653}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_234770155}[配置]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[中由]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[向]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[反向切换的延迟时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_x252859436}

[\[Sysname\] multicast-domain vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-md-mvpn\] data-holddown 120]{lang="EN-US"}
:::::

::: {#1442857008 .myid}
[]{#_Toc404789864}[]{#struct_0_x1693_29802_1465459531}

**组播VPN \-- 组播VPN配置命令 \-- default-group**

------------------------------------------------------------------------

[**[default-group]{lang="EN-US"}**]{#struct_0_x1693_29802_447030028}[命令用来指定]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo default-group]{lang="EN-US"}**]{#struct_0_x1693_29802_x759422995}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x234813093}

[**[default-group]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_x1693_29802_x699181127}

[**[undo]{lang="EN-US"}**[ **default-group**]{lang="EN-US"}]{#struct_0_x1693_29802_x21384952}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1632561901}

[[没有指定]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}]{#struct_0_x1693_29802_x1394327695}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1045754649}

[[MD]{lang="EN-US"}]{#struct_0_x1693_29802_x212157216}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x311277898}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x1907997043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x134599679}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1211559244}

[*[group-address]{lang="EN-US"}*]{#struct_0_x1693_29802_1132128551}[：表示]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[的地址，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1632627437}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1693_29802_2065792052}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在不同的]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x1693_29802_1070739557}[上，应]{lang="EN-US" style="font-family:宋体"}[该]{style="font-family:宋体"}[为相同]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[MD]{lang="EN-US"}[指定相同的]{lang="EN-US" style="font-family:宋体"}[Default-Group]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不允许指定已被其它]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1693_29802_x1605756104}[MD]{lang="EN-US"}[使用的]{lang="EN-US" style="font-family:宋体"}[Default-Group]{lang="EN-US"}[或]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1276008522}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_x975597519}[指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[的]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[为]{style="font-family:宋体"}[239.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_721045864}

[\[Sysname\] multicast-domain vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-md-mvpn\] default-group 239.1.1.1]{lang="EN-US"}
:::

::: {#-1680442493 .myid}
[]{#_Toc404789865}[]{#struct_0_x1693_29802_1879667843}[]{#_Toc365900728}

**组播VPN \-- 组播VPN配置命令 \-- display bgp routing-table ipv4 mdt**

------------------------------------------------------------------------

[**[display bgp routing-table ipv4 mdt]{lang="EN-US"}**]{#struct_0_x1693_29802_1880388739}[命令用来显示]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x938618176}

[**[display bgp routing-table ipv4 mdt]{lang="EN-US"}**[ \[ **route-distinguisher** *route-distinguisher* \] \[ *ip-address* \[ **advertise-info** \] \]]{lang="EN-US"}]{#struct_0_x1693_29802_565610414}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_578896253}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1693_29802_1880323203}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x611253510}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x1579125718}

[[network-operator]{lang="EN-US"}]{#struct_0_x1693_29802_x1887599417}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_1739683766}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1693_29802_1879864452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x152369554}

[**[route-distinguisher]{lang="EN-US"}**[ *route-distinguisher*]{lang="EN-US"}]{#struct_0_x1693_29802_x550886806}[：显示指定路由标识符的信息。]{style="font-family:宋体"}*[route-distinguisher]{lang="EN-US"}*[为路由标识符，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。如果未指定本参数，将显示所有路由标识符的信息。路由标识符有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x1693_29802_x1048168598}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x1693_29802_1879798916}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x1693_29802_1450414031}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。]{style="font-family:宋体"}[例如：]{lang="EN-US" style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1693_29802_1875792418}[：显示指定组播源的详细信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[的组播源地址，即]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备的地址。如果未指定本参数，将显示所有组播源的简要信息。]{style="font-family:宋体"}

[**[advertise-info]{lang="EN-US"}**]{#struct_0_x1693_29802_x617800227}[：显示通告信息。如果未指定本参数，将不显示通告信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1879995524}

[*[\# ]{lang="EN-US"}*]{#struct_0_x1693_29802_x890793553}[显示所有组播源的]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[简要路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 mdt]{lang="EN-US"}]{#struct_0_x1693_29802_1514326132}

[ ]{lang="EN-US"}

[ BGP local router ID is 1.1.1.1]{lang="EN-US"}

[ Status codes: \* - valid, \> - best, d - dampened, h - history,]{lang="EN-US"}

[               s - suppressed, S - stale, i - internal, e - external]{lang="EN-US"}

[               Origin: i - IGP, e - EGP, ? - incomplete]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 100:1]{lang="EN-US"}

[ Total number of routes: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[     Network            NextHop         MED        LocPrf     PrefVal Path/Ogn]{lang="EN-US"}

[ ]{lang="EN-US"}

[\* \>  1.1.1.1/32         0.0.0.0                               32768   ?]{lang="EN-US"}

[\* \>i 2.2.2.2/32         2.2.2.2                    100        0       ?]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_1879929988}[显示组播源]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[详细路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 mdt 1.1.1.1]{lang="EN-US"}]{#struct_0_x1693_29802_x1305798027}

[ ]{lang="EN-US"}

[ BGP local router ID: 1.1.1.1]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 100:1]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ Paths:   1 available, 1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP MDT information of source 1.1.1.1:]{lang="EN-US"}

[ Default-group   : 224.1.1.1]{lang="EN-US"}

[ Original nexthop: 0.0.0.0]{lang="EN-US"}

[ AS-path         : (null)]{lang="EN-US"}

[ Origin          : incomplete]{lang="EN-US"}

[ Attribute value : pref-val 32768]{lang="EN-US"}

[ State           : valid, local, best]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_x27007963}[显示组播源]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[路由的通告信息。]{style="font-family:宋体"}

[[\<Sysname\> display bgp routing-table ipv4 mdt 1.1.1.1 advertise-info]{lang="EN-US"}]{#struct_0_x1693_29802_1879602308}

[ ]{lang="EN-US"}

[ BGP local router ID: 1.1.1.1]{lang="EN-US"}

[ Local AS number: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route distinguisher: 100:1]{lang="EN-US"}

[ Total number of routes: 1]{lang="EN-US"}

[ Paths:   1 best]{lang="EN-US"}

[ ]{lang="EN-US"}

[ BGP MDT information of source 1.1.1.1:]{lang="EN-US"}

[ Default-group: 224.1.1.1]{lang="EN-US"}

[ Advertised to peers (1 in total):]{lang="EN-US"}

[     6.6.6.6]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display bgp routing-table ipv4 mdt]{lang="EN-US"}]{#struct_0_x1693_29802_1799429627}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1210282295}[[字段]{style="font-family:黑体"}]{#struct_0_x1693_29802_1879536772}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1693_29802_x933236735}

[[BGP local router ID]{lang="EN-US"}]{#struct_0_x1693_29802_1879733380}

[[本地的路由器编号]{style="font-family:宋体"}]{#struct_0_x1693_29802_x927946439}

[[Status codes]{lang="EN-US"}]{#struct_0_x1693_29802_x889251706}

[[路由状态代码]{style="font-family:宋体"}]{#struct_0_x1693_29802_1879667844}[，包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[\* -- valid]{lang="DA"}]{#struct_0_x1693_29802_575175624}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[合法路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\> -- best]{lang="EN-US"}]{#struct_0_x1693_29802_1880388740}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[普通优选最佳路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[d -- damped]{lang="EN-US"}]{#struct_0_x1693_29802_x938028359}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[震荡抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[h -- history]{lang="EN-US"}]{#struct_0_x1693_29802_1880323204}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[历史路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s -- suppressed]{lang="EN-US"}]{#struct_0_x1693_29802_x611056902}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[聚合抑制路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S -- Stale]{lang="EN-US"}]{#struct_0_x1693_29802_x1584416018}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[过期路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i -- internal]{lang="EN-US"}]{#struct_0_x1693_29802_1879864449}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e -- external]{lang="EN-US"}]{#struct_0_x1693_29802_x153090449}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[外部路由]{lang="EN-US" style="font-family:宋体"}

[[Origin]{lang="IT"}]{#struct_0_x1693_29802_1879798913}

[[信息的来源]{style="font-family:宋体"}]{#struct_0_x1693_29802_1450741711}[，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[i -- IGP]{lang="IT"}]{#struct_0_x1693_29802_1879995521}[：表示]{lang="EN-US" style="font-family:宋体"}[产生于本]{lang="EN-US" style="font-family:宋体"}[AS]{lang="IT"}[内]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:
  宋体"}**[network]{lang="IT"}**[命令发布路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[e -- EGP]{lang="IT"}]{#struct_0_x1693_29802_x890465873}[：表示]{lang="EN-US" style="font-family:宋体"}[是通过]{lang="EN-US" style="font-family:宋体"}[EGP]{lang="IT"}[（]{lang="EN-US" style="font-family:宋体"}[Exterior Gateway Protocol]{lang="IT"}[，]{lang="EN-US" style="font-family:
  宋体"}[外部网关协议]{lang="EN-US" style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}[学到的]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[? -- incomplete]{lang="IT"}]{#struct_0_x1693_29802_1879929985}[：表示]{lang="EN-US" style="font-family:宋体"}[来源无法确定]{lang="EN-US" style="font-family:宋体"}[。从]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="IT"}[协议引入路由的路由信息来源为]{lang="EN-US" style="font-family:宋体"}[incomplete]{lang="IT"}

[[Route distinguisher]{lang="EN-US"}]{#struct_0_x1693_29802_x1306125707}

[[路由标识符]{style="font-family:宋体"}]{#struct_0_x1693_29802_1879602305}

[[Total number of routes]{lang="EN-US"}]{#struct_0_x1693_29802_1799101947}

[[BGP MDT]{lang="EN-US"}]{#struct_0_x1693_29802_1321919478}[信息的总数]{style="font-family:宋体"}

[[Network]{lang="EN-US"}]{#struct_0_x1693_29802_1879536769}

[[Default-MDT]{lang="EN-US"}]{#struct_0_x1693_29802_1879733377}[的组播源地址]{style="font-family:宋体"}

[[NextHop]{lang="EN-US"}]{#struct_0_x1693_29802_x927749816}

[[下一跳的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1693_29802_1879667841}[地址]{style="font-family:宋体"}

[[MED]{lang="EN-US"}]{#struct_0_x1693_29802_575372232}

[[MED]{lang="IT"}]{#struct_0_x1693_29802_1880388737}[（]{style="font-family:宋体"}[Multi-Exit-Discriminator]{lang="EN-US"}[，多出口区分）属性值]{style="font-family:宋体"}

[[LocPrf]{lang="EN-US"}]{#struct_0_x1693_29802_x937962816}

[[本地优先级]{style="font-family:宋体"}]{#struct_0_x1693_29802_1880323201}

[[PrefVal]{lang="EN-US"}]{#struct_0_x1693_29802_x611384582}

[[路由首选值]{style="font-family:宋体"}]{#struct_0_x1693_29802_1879864450}

[[Path/Ogn]{lang="EN-US"}]{#struct_0_x1693_29802_x152500626}

[[AS]{lang="EN-US"}]{#struct_0_x1693_29802_1879798914}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性和信息的来源（]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[）属性，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AS_PATH]{lang="EN-US"}]{#struct_0_x1693_29802_1450282959}[属性记录了此]{lang="EN-US" style="font-family:宋体"}[信息]{style="font-family:宋体"}[经过的所有]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免环路的出现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ORIGIN]{lang="EN-US"}]{#struct_0_x1693_29802_1879995522}[属性标记了此]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[ MDT]{lang="EN-US"}[信息是]{style="font-family:
  宋体"}[如何生成的]{lang="EN-US" style="font-family:宋体"}

[[Local AS number]{lang="EN-US"}]{#struct_0_x1693_29802_x890400337}

[[本地的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_x1693_29802_1879929986}[号]{style="font-family:宋体"}

[[Paths]{lang="EN-US"}]{#struct_0_x1693_29802_x1305929099}

[[BGP MDT]{lang="EN-US"}]{#struct_0_x1693_29802_1879602306}[信息的数目，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[available]{lang="EN-US"}]{#struct_0_x1693_29802_1799036411}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[有效]{lang="EN-US" style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[信息的数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_x1693_29802_1879536770}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[最佳]{lang="EN-US" style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[信息的数目]{lang="EN-US" style="font-family:宋体"}

[[BGP MDT information of source 1.1.1.1]{lang="EN-US"}]{#struct_0_x1693_29802_x933105663}

[[组播源]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}]{#struct_0_x1693_29802_1879733378}[的]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Default-group]{lang="EN-US"}]{#struct_0_x1693_29802_x927422136}

[[所属的]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}]{#struct_0_x1693_29802_1879667842}[地址]{style="font-family:宋体"}

[[Advertised to peers (1 in total)]{lang="EN-US"}]{#struct_0_x1693_29802_575568840}

[[该信息已经向哪些对等体发送，以及对等体的数目]{style="font-family:宋体"}]{#struct_0_x1693_29802_1880388738}

[[From]{lang="EN-US"}]{#struct_0_x1693_29802_x938552640}

[[发布该信息的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1693_29802_1880323202}[对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Original nexthop]{lang="EN-US"}]{#struct_0_x1693_29802_x611187974}

[[原始下一跳地址，如果是从]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1693_29802_x492788542}[更新消息中获得的信息，则该地址为接收到的消息中的下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[AS-path]{lang="EN-US"}]{#struct_0_x1693_29802_194085228}

[[AS]{lang="EN-US"}]{#struct_0_x1693_29802_x492854078}[路径（]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[）属性，记录了此信息经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[，可以避免环路的出现]{style="font-family:宋体"}

[[Attribute value]{lang="EN-US"}]{#struct_0_x1693_29802_1331755282}

[[BGP MDT]{lang="EN-US"}]{#struct_0_x1693_29802_x492657470}[信息的属性，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MED]{lang="EN-US"}]{#struct_0_x1693_29802_970889987}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[与目的网络关联的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[localpref]{lang="EN-US"}]{#struct_0_x1693_29802_x492723006}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[本地优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pref-val]{lang="EN-US"}]{#struct_0_x1693_29802_x601110409}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[路由首选值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pre]{lang="EN-US"}]{#struct_0_x1693_29802_x493050686}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[协议优先级]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1693_29802_172893497}

[[当前状态，包括：]{style="font-family:宋体"}]{#struct_0_x1693_29802_x493116222}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_x1693_29802_x492919614}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[有效路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[internal]{lang="EN-US"}]{#struct_0_x1693_29802_x174191336}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[内部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[external]{lang="EN-US"}]{#struct_0_x1693_29802_x492985150}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[外部路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[local]{lang="EN-US"}]{#struct_0_x1693_29802_911836248}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[本地产生路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[synchronize]{lang="EN-US"}]{#struct_0_x1693_29802_x492264254}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[同步路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[best]{lang="EN-US"}]{#struct_0_x1693_29802_1712584682}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[最佳路由]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#2075289780 .myid}
[]{#_Toc327804451}[]{#_Toc404789866}[]{#struct_0_x1693_29802_x184643697}[]{#_Toc347846332}[]{#_Toc346528401}[]{#_Toc327804449}

**组播VPN \-- 组播VPN配置命令 \-- display multicast-domain data-group receive**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1693_29802_x1632692973}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1693_29802_1486493374}
:::

**[ ]{lang="EN-US"}**

[**[display multicast-domain data-group receive]{lang="EN-US"}**]{#struct_0_x1693_29802_x1795292592}[命令用来显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[中收到的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x681981715}

[**[display multicast-domain]{lang="EN-US"}**[ **vpn-instance** *vpn-instance-name* **data-group receive** \[ **brief** \| \[ **active** \| **group** *group-address* \| **sender** *source-address* \| *vpn-source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *vpn-group-address* \[ **mask** { *mask-length* \| *mask* } \] \] \* \]]{lang="EN-US"}]{#struct_0_x1693_29802_x1946437144}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1947878958}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1693_29802_565338725}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1507662867}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_923410504}

[[network-operator]{lang="EN-US"}]{#struct_0_x1693_29802_x1632758509}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x1642422584}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1693_29802_x121043048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x664969663}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1693_29802_1482682729}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x1693_29802_x1534554632}[：显示简要信息。如果未指定本参数，将显示详细信息。]{style="font-family:宋体"}

[**[active]{lang="EN-US"}**]{#struct_0_x1693_29802_x1531269969}[：显示收到的已加入]{style="font-family:宋体"}[Data-MDT]{lang="EN-US"}[的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[group ]{lang="EN-US"}***[group-address]{lang="EN-US"}*]{#struct_0_x1693_29802_x557929055}[：显示与指定公网组播组相关的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sender ]{lang="EN-US"}***[source-address]{lang="EN-US"}*]{#struct_0_x1693_29802_x1082055899}[：显示与指定公网组播源相关的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[vpn-source-address]{lang="EN-US"}*]{#struct_0_x1693_29802_x1632299757}[：显示与指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播源相关的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1693_29802_106120276}[：表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播源或组播组地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x1693_29802_2125217094}[：表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播源或组播组地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vpn-group-address]{lang="EN-US"}*]{#struct_0_x1693_29802_1842000523}[：显示与指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播组相关的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1226916824}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_1433880961}[显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[中]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[收到的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-domain vpn-instance mvpn data-group receive]{lang="EN-US"}]{#struct_0_x1693_29802_x1632365293}

[MD data-group information received by VPN instance: mvpn]{lang="EN-US"}

[Total 2 data-groups for 8 entries]{lang="EN-US"}

[Total 2 data-groups and 8 entries matched]{lang="EN-US"}

[ ]{lang="EN-US"}

[Data-group: 226.1.1.0   Reference count: 4   Active count: 2]{lang="EN-US"}

[  Sender: 172.100.1.1   Active count: 1]{lang="EN-US"}

[    (192.6.1.5, 239.1.1.1)       expires: 00:03:10 active]{lang="EN-US"}

[    (192.6.1.5, 239.1.1.158)     expires: 00:03:10]{lang="EN-US"}

[  Sender:  181.100.1.1, active count: 1]{lang="EN-US"}

[    (195.6.1.2, 239.1.2.12)      expires: 00:03:10 active]{lang="EN-US"}

[    (195.6.1.2, 239.1.2.197)     expires: 00:03:10]{lang="EN-US"}

[Data-group: 229.1.1.0   Reference count: 4   Active count: 2]{lang="EN-US"}

[  Sender: 185.100.1.1   Active count: 1]{lang="EN-US"}

[    (198.6.1.5, 239.1.3.62)      expires: 00:03:10 active]{lang="EN-US"}

[    (198.6.1.5, 225.1.1.109)     expires: 00:03:10]{lang="EN-US"}

[  Sender: 190.100.1.1   Active count: 1]{lang="EN-US"}

[    (200.6.1.2, 225.1.4.80)      expires: 00:03:10 active]{lang="EN-US"}

[    (200.6.1.2, 225.1.4.173)     expires: 00:03:10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_x754702162}[显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[中]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[收到的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-domain vpn-instance mvpn data-group receive brief]{lang="EN-US"}]{#struct_0_x1693_29802_1267403127}

[MD data-group information received by VPN instance: mvpn]{lang="EN-US"}

[Total 2 data-groups for 8 entries]{lang="EN-US"}

[Total 2 data-groups and 8 entries matched]{lang="EN-US"}

[ ]{lang="EN-US"}

[Data group: 226.1.1.0   Reference count: 4   Active count: 2]{lang="EN-US"}

[Data group: 229.1.1.0   Reference count: 4   Active count: 2]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display multicast-domain data-group receive]{lang="EN-US"}]{#struct_0_x1693_29802_1605546267}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_300681330}[[字段]{style="font-family:黑体"}]{#struct_0_x1693_29802_1900022906}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1632824044}

[[MD data-group information received by VPN instance: mvpn]{lang="EN-US"}]{#struct_0_x1693_29802_x1077672035}

[[VPN]{lang="EN-US"}]{#struct_0_x1693_29802_1182511059}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[收到的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Total 2 data-groups for 8 entries]{lang="EN-US"}]{#struct_0_x1693_29802_493742951}

[[总共有]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1693_29802_1175662810}[个]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[，对应着]{style="font-family:宋体"}[8]{lang="EN-US"}[个（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Total 2 data-groups and 8 entries matched]{lang="EN-US"}]{#struct_0_x1693_29802_650452474}

[[总共匹配了]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1693_29802_247650311}[个]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[和]{style="font-family:宋体"}[8]{lang="EN-US"}[个（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Data-group]{lang="EN-US"}]{#struct_0_x1693_29802_x1632889580}

[[收到的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_105417270}[地址]{style="font-family:宋体"}

[[Sender]{lang="EN-US"}]{#struct_0_x1693_29802_x2021311556}

[[发送]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_x978644698}[信息的]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体地址]{style="font-family:宋体"}

[[Reference count]{lang="EN-US"}]{#struct_0_x1693_29802_x1524837068}

[[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_x2055374783}[引用的私网组播表项数量]{style="font-family:宋体"}

[[Active count]{lang="EN-US"}]{#struct_0_x1693_29802_x1632955116}

[[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_1569997051}[引用的活跃私网组播表项（即存在接收者的组播组）数量]{style="font-family:宋体"}

[[expires]{lang="EN-US"}]{#struct_0_x1693_29802_x2096528668}

[[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_x1652870215}[引用的私网组播（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的超时时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#240641865 .myid}
[]{#_Toc404789867}[]{#struct_0_x1693_29802_779839418}[]{#_Toc347846333}[]{#_Toc346528402}[]{#_Toc327804450}

**组播VPN \-- 组播VPN配置命令 \-- display multicast-domain data-group send**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VPN命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1693_29802_162468153}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1693_29802_x1633020652}
:::

**[ ]{lang="EN-US"}**

[**[display multicast-domain data-group send]{lang="EN-US"}**]{#struct_0_x1693_29802_x1331313786}[命令用来显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[中发送的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x775743361}

[**[display multicast-domain]{lang="EN-US"}**[ **vpn-instance** *vpn-instance-name* **data-group** **send** \[ **group** *group-address* \| **reuse** *interval* \| *vpn-source-address* \[ **mask** { *mask-length* \| *mask* } \] \| *vpn-group-address* \[ **mask** { *mask-length* \| *mask* } \] \] \*]{lang="EN-US"}]{#struct_0_x1693_29802_1357084478}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1678355798}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1693_29802_x1542414352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1945449488}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x2140776673}

[[network-operator]{lang="EN-US"}]{#struct_0_x1693_29802_x1195935950}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x1632561900}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1693_29802_1334555660}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_284347755}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1693_29802_x1904021297}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[group ]{lang="EN-US"}***[group-address]{lang="EN-US"}*]{#struct_0_x1693_29802_x216096441}[：显示与指定组播组相关的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[reuse]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1693_29802_x967656725}[：显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[在指定时间段内发生重用的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[vpn-source-address]{lang="EN-US"}*]{#struct_0_x1693_29802_478469414}[：显示与指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播源相关的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1693_29802_x2007353948}[：表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播源或组播组地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x1693_29802_x1632627436}[：表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播源或组播组地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vpn-group-address]{lang="EN-US"}*]{#struct_0_x1693_29802_499708111}[：显示与指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[组播组相关的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_138661648}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_86794350}[显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[中]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-domain vpn-instance mvpn data-group send]{lang="EN-US"}]{#struct_0_x1693_29802_1278444512}

[MD data-group information sent by VPN instance: mvpn]{lang="EN-US"}

[Total 2 data-groups for 6 entries]{lang="EN-US"}

[Total 2 data-groups and 6 entries matched]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Reference count of 226.1.1.0: 3]{lang="EN-US"}

[    (192.6.1.5, 239.1.1.1)                  switch time: 00:00:21]{lang="EN-US"}

[    (192.6.1.5, 239.1.1.158)                switch time: 00:00:21]{lang="EN-US"}

[    (192.6.1.5, 239.1.2.50)                 switch time: 00:00:05]{lang="EN-US"}

[  Reference count of 226.1.1.1: 3]{lang="EN-US"}

[    (192.6.1.2, 225.1.1.1)                  switch time: 00:00:21]{lang="EN-US"}

[    (192.6.1.2, 225.1.2.50)                 switch time: 00:00:05]{lang="EN-US"}

[    (192.6.1.5, 239.1.1.159)                switch time: 00:00:21]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_766314222}[显示]{style="font-family:宋体"}[MD]{lang="EN-US"}[中]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[在]{style="font-family:宋体"}[30]{lang="EN-US"}[秒内发送的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[的重用信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-domain vpn-instance mvpn data-group send reuse 30]{lang="EN-US"}]{#struct_0_x1693_29802_x1632692972}

[MD data-group information sent by VPN instance: mvpn]{lang="EN-US"}

[Total 2 data-groups for 3 entries]{lang="EN-US"}

[Total 2 data-groups and 3 entries matched]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Reuse count of 226.1.1.0: 1]{lang="EN-US"}

[  Reuse count of 226.1.1.1: 1]{lang="EN-US"}

[  Reuse count of 226.1.1.2: 1]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display multicast-domain data-group send]{lang="EN-US"}]{#struct_0_x1693_29802_x1242389981}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_294491904}[[字段]{style="font-family:黑体"}]{#struct_0_x1693_29802_757299163}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1693_29802_845195211}

[[MD data-group information sent by VPN instance: mvpn]{lang="EN-US"}]{#struct_0_x1693_29802_1493587594}

[[VPN]{lang="EN-US"}]{#struct_0_x1693_29802_915131566}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Total 2 data-groups for 6 entries]{lang="EN-US"}]{#struct_0_x1693_29802_x1632758508}

[[总共有]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1693_29802_x76338643}[个]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[，对应着]{style="font-family:宋体"}[6]{lang="EN-US"}[个（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Total 2 data-groups and 6 entries matched]{lang="EN-US"}]{#struct_0_x1693_29802_x1006379871}

[[总共匹配了]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x1693_29802_1414550057}[个]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[和]{style="font-family:宋体"}[6]{lang="EN-US"}[个（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Reference count of 226.1.1.0]{lang="EN-US"}]{#struct_0_x1693_29802_1015153791}

[[发送的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_1279108910}[引用的私网组播组数量]{style="font-family:宋体"}

[[switch time]{lang="EN-US"}]{#struct_0_x1693_29802_x1632299756}

[[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_1672204217}[引用的私网组播（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的切换时间]{style="font-family:宋体"}

[[Reuse count of 226.1.1.0]{lang="EN-US"}]{#struct_0_x1693_29802_x1836120139}

[[发送的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_x176098285}[在指定时间段内的重用数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-787647772 .myid}
[]{#_Toc404789868}[]{#struct_0_x1693_29802_507731131}

**组播VPN \-- 组播VPN配置命令 \-- display multicast-domain default-group**

------------------------------------------------------------------------

[**[display multicast-domain]{lang="EN-US"}**[ **default-group**]{lang="EN-US"}]{#struct_0_x1693_29802_342994828}[命令用来显示]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1816252183}

[**[display multicast-domain]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **default-group** { **local** \| **remote** }]{lang="EN-US"}]{#struct_0_x1693_29802_x1063904215}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1632365292}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1693_29802_1974181193}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_359776326}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_140636802}

[[network-operator]{lang="EN-US"}]{#struct_0_x1693_29802_329828583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_1382067643}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1693_29802_1142674759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1431604957}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1693_29802_x1265368452}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1693_29802_x492788544}[：显示本地]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1693_29802_193954156}[：显示远端]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_746185946}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_721750803}[显示所有]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中本地]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-domain default-group local]{lang="EN-US"}]{#struct_0_x1693_29802_x1738764329}

[MD local default-group information:]{lang="EN-US"}

[ Group address    Source address   Interface     VPN instance]{lang="EN-US"}

[ 239.1.1.1        1.1.1.1          MTunnel0      mvpna]{lang="EN-US"}

[ 239.2.1.1        1.1.1.1          MTunnel1      mvpnb]{lang="EN-US"}

[ 239.3.1.1        \--               MTunnel2      mvpnc]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_x492657472}[显示所有]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中远端]{style="font-family:宋体"}[Default-Group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display multicast-domain default-group remote]{lang="EN-US"}]{#struct_0_x1693_29802_971021059}

[MD remote default-group information:]{lang="EN-US"}

[ Group address   Source address  Next hop         VPN instance]{lang="EN-US"}

[ 239.1.1.1       1.2.0.1         1.2.0.1          a]{lang="EN-US"}

[ 239.1.1.1       1.2.0.2         1.2.0.2          a]{lang="EN-US"}

[ 239.1.1.1       1.2.0.3         1.2.0.3          a]{lang="EN-US"}

[ 239.1.1.2       1.2.0.1         1.2.0.1          b]{lang="EN-US"}

[ 239.1.1.2       1.2.0.2         1.2.0.2          b]{lang="EN-US"}

[ 239.1.1.3       1.2.0.1         1.2.0.1          -]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display multicast-domain default-group]{lang="EN-US"}]{#struct_0_x1693_29802_x459483318}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_295903675}[[字段]{style="font-family:黑体"}]{#struct_0_x1693_29802_516658359}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1693_29802_1880727799}

[[Group address]{lang="EN-US"}]{#struct_0_x1693_29802_x1006250789}

[[Default-Group]{lang="EN-US"}]{#struct_0_x1693_29802_746251482}[的地址]{style="font-family:宋体"}

[[Source address]{lang="EN-US"}]{#struct_0_x1693_29802_x614855663}

[[MTI]{lang="EN-US"}]{#struct_0_x1693_29802_851456239}[封装私网组播报文时使用的源地址，即]{style="font-family:宋体"}[MD]{lang="EN-US"}[源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1693_29802_1602172203}

[[MTI]{lang="EN-US"}]{#struct_0_x1693_29802_x1475200364}[的名称]{style="font-family:宋体"}

[[Next hop]{lang="EN-US"}]{#struct_0_x1693_29802_x493050688}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_x1693_29802_172500281}

[[VPN instance]{lang="EN-US"}]{#struct_0_x1693_29802_x227999002}

[[所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1693_29802_x612492496}[实例的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1869872416 .myid}
[]{#_Toc327804453}[]{#_Toc404789869}[]{#struct_0_x1693_29802_746317018}[]{#_Toc347846335}[]{#_Toc346528404}[]{#_Toc327804452}

**组播VPN \-- 组播VPN配置命令 \-- log data-group-reuse**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](组播VPN命令.files/image001.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1693_29802_1333541423}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_x1693_29802_x779903013}
:::

**[ ]{lang="EN-US"}**

[**[log]{lang="EN-US"}**[ **data-group-reuse**]{lang="EN-US"}]{#struct_0_x1693_29802_x106924163}[命令用来打开]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[重用日志输出开关。]{style="font-family:宋体"}

[**[undo log data-group-reuse]{lang="EN-US"}**]{#struct_0_x1693_29802_421905453}[命令用来关闭]{style="font-family:
宋体"}[Data-Group]{lang="EN-US"}[重用日志输出开关。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_2013840013}

[**[log]{lang="EN-US"}**[ **data-group-reuse**]{lang="EN-US"}]{#struct_0_x1693_29802_1801451421}

[**[undo]{lang="EN-US"}**[ **log** **data-group-reuse**]{lang="EN-US"}]{#struct_0_x1693_29802_x1598973949}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_746382554}

[[Data-Group]{lang="EN-US"}]{#struct_0_x1693_29802_x1448050087}[重用日志输出开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1172341835}

[[MD]{lang="EN-US"}]{#struct_0_x1693_29802_x2572142}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1333444258}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x300991887}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_279537258}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1239245402}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_986173014}[打开]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[中的]{style="font-family:宋体"}[Data-Group]{lang="EN-US"}[重用日志输出开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_745923802}

[\[Sysname\] multicast-domain vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-md-mvpn\] log data-group-reuse]{lang="EN-US"}
:::::

::: {#1809835764 .myid}
[]{#_Toc404789870}[]{#struct_0_x1693_29802_x1850232797}

**组播VPN \-- 组播VPN配置命令 \-- multicast-domain**

------------------------------------------------------------------------

[**[multicast-domain]{lang="EN-US"}**]{#struct_0_x1693_29802_x1255603101}[命令用来创建指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[MD]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[MD]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo multicast-domain]{lang="EN-US"}**]{#struct_0_x1693_29802_512857697}[命令用来清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[MD]{lang="EN-US"}[视图下的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1235535346}

[**[multicast-domain]{lang="EN-US"}**[ **vpn-instance** *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1693_29802_x1881287408}

[**[undo]{lang="EN-US"}**[ **multicast-domain** **vpn-instance** *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1693_29802_x849641036}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x2259416}

[[VPN]{lang="EN-US"}]{#struct_0_x1693_29802_x334325957}[实例不存在对应的]{style="font-family:宋体"}[MD]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_745989338}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1693_29802_522497722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_743484728}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_752721604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x903794459}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x393952274}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x1693_29802_x1825555121}[：表示]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_665649023}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_933037732}[创建]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[的]{style="font-family:宋体"}[MD]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[MD]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_746054874}

[\[Sysname\] multicast-domain vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-md-mvpn\]]{lang="EN-US"}
:::

::: {#-941077528 .myid}
[]{#_Toc404789871}[]{#struct_0_x1693_29802_1085543622}[]{#_Toc377395759}[]{#_Toc376534346}

**组播VPN \-- 组播VPN配置命令 \-- multicast rpf-proxy-vector compatible**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1737687602}

[**[multicast rpf-proxy-vector compatible]{lang="EN-US"}**]{#struct_0_x1693_29802_699250439}[命令用来使能]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量兼容功能。]{style="font-family:宋体"}

[**[undo multicast rpf-proxy-vector compatible]{lang="EN-US"}**]{#struct_0_x1693_29802_325979334}[命令用来关闭]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量兼容功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_665239269}

[**[multicast rpf-proxy-vector compatible]{lang="EN-US"}**]{#struct_0_x1693_29802_1084953795}

[**[undo multicast rpf-proxy-vector compatible]{lang="EN-US"}**]{#struct_0_x1693_29802_x1768881735}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1207550349}

[[RPF]{lang="EN-US"}]{#struct_0_x1693_29802_x1831918781}[代理向量兼容功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x876121463}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1693_29802_x758149797}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x231923143}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_1511806863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_680652120}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1085019331}

[[在配置]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_x1693_29802_x552253642}[类跨]{style="font-family:宋体"}[AS]{lang="EN-US"}[的]{style="font-family:宋体"}[MD VPN]{lang="EN-US"}[时，如果要与某些厂商的设备互通，则必须在公网中的所有]{style="font-family:宋体"}[H3C]{lang="EN-US"}[设备上都使能]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量兼容功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x10251247}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_1874724880}[使能]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量兼容功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_1734477578}

[\[Sysname\] multicast rpf-proxy-vector compatible]{lang="EN-US"}[]{#_Toc369013821}
:::

::: {#266511071 .myid}
[]{#_Toc404789872}[]{#struct_0_x1693_29802_x432359740}[]{#_Toc377395760}[]{#_Toc376534347}

**组播VPN \-- 组播VPN配置命令 \-- rpf proxy vector**

------------------------------------------------------------------------

[**[rpf proxy vector]{lang="EN-US"}**]{#struct_0_x1693_29802_48763507}[命令用来使能]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量功能。]{style="font-family:宋体"}

[**[undo rpf proxy vector]{lang="EN-US"}**]{#struct_0_x1693_29802_x481876824}[命令用来关闭]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1085084867}

[**[rpf proxy vector]{lang="EN-US"}**]{#struct_0_x1693_29802_x187610652}

[**[undo rpf proxy vector]{lang="EN-US"}**]{#struct_0_x1693_29802_x2061875921}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x2128749382}

[[RPF]{lang="EN-US"}]{#struct_0_x1693_29802_x783163799}[代理向量功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_2012598210}

[[MRIB]{lang="EN-US"}]{#struct_0_x1693_29802_1745526174}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1964669043}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_x801010782}

[[network-operator]{lang="EN-US"}]{#struct_0_x1693_29802_1085150403}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x212437165}

[[在配置]{style="font-family:宋体"}[B]{lang="EN-US"}]{#struct_0_x1693_29802_1658210110}[类跨]{style="font-family:宋体"}[AS]{lang="EN-US"}[的]{style="font-family:宋体"}[MD VPN]{lang="EN-US"}[时，必须在]{style="font-family:宋体"}[PE]{lang="EN-US"}[（不连接组播接收者的]{style="font-family:宋体"}[PE]{lang="EN-US"}[除外）上使能]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量功能，从而使]{style="font-family:宋体"}[PE]{lang="EN-US"}[发送的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[加入报文可携带用于进行]{style="font-family:宋体"}[RPF]{lang="EN-US"}[检查的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量信息，以创建正确的公网]{style="font-family:宋体"}[Default-MDT]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，本命令只在]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1693_29802_x791272109}[实例]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[视图下生效。公网实例]{style="font-family:宋体"}[MRIB]{lang="EN-US"}[视图下虽可配置本命令，但不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x60539828}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_1066178032}[在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[中使能]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_x960450860}

[\[Sysname\] multicast routing vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-mrib-mvpn\] rpf proxy vector]{lang="EN-US"}
:::

::: {#-773629 .myid}
[]{#_Toc404789873}[]{#struct_0_x1693_29802_x836987697}[]{#_Toc327804454}

**组播VPN \-- 组播VPN配置命令 \-- source**

------------------------------------------------------------------------

[**[source]{lang="EN-US"}**]{#struct_0_x1693_29802_x952335056}[命令用来指定]{style="font-family:宋体"}[MD]{lang="EN-US"}[源接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_x1693_29802_x5723354}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x1406041710}

[**[source]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1693_29802_x1403741098}

[**[undo]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_x1693_29802_x1057800054}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1693_29802_601374949}

[[没有指定]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_x1693_29802_190518989}[源接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1693_29802_746120410}

[[MD]{lang="EN-US"}]{#struct_0_x1693_29802_x910095248}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1693_29802_277360518}

[[network-admin]{lang="EN-US"}]{#struct_0_x1693_29802_1875216016}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1693_29802_926216426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1693_29802_1433093155}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x1693_29802_1613728185}[：表示接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1693_29802_x596334173}

[[需要注意的是，]{style="font-family:宋体"}[MD]{lang="EN-US"}]{#struct_0_x1693_29802_x307103672}[源接口必须与建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体时所使用的源接口相同，否则将无法获取正确的路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1693_29802_746710234}

[[\# ]{lang="EN-US"}]{#struct_0_x1693_29802_x1651891367}[假设建立]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体时所使用的源接口为]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[接口，指定该接口为]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[的]{style="font-family:宋体"}[MD]{lang="EN-US"}[源接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1693_29802_826593246}

[\[Sysname\] multicast-domain vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-md-mvpn\] source loopback ]{lang="EN-US"}[1]{lang="EN-US"}
:::
