::: {#-1778694699 .myid}
[]{#_Toc404790426}[]{#struct_0_x1176_16249_x104954713}[]{#_Toc356223686}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- anycast-rp (IPv6 PIM view)**

------------------------------------------------------------------------

[**[anycast-rp]{lang="EN-US"}**]{#struct_0_x1176_16249_516998196}[命令用来配置]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo anycast-rp]{lang="EN-US"}**]{#struct_0_x1176_16249_x105151321}[命令用来删除]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1321821560}

[**[anycast-rp]{lang="EN-US"}***[ ipv6-anycast-rp-address ipv6-member-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x775051399}

[**[undo anycast-rp]{lang="EN-US"}**[ *ipv6-anycast-rp-address ipv6-member-address*]{lang="EN-US"}]{#struct_0_x1176_16249_189369592}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x105085785}

[[没有配置]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}]{#struct_0_x1176_16249_115226493}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1271901468}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x104758105}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1835100579}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x458161234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x104692569}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1697646704}

[*[ipv6-anycast-rp-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x2137046624}[：指定]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[地址。必须是合法的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址。]{style="font-family:宋体"}

[*[ipv6-member-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x104889177}[：指定]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[成员地址。必须是合法的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址，不能与]{style="font-family:宋体"}*[ipv6-anycast-rp-address]{lang="EN-US"}*[相同。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_892013398}

[[本命令可重复配置，配置时如果指定了相同的]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x130765983}[地址，则将]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[成员地址添加到该]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[集中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x104823641}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1733131591}[在公网实例中配置如下]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[集：]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1:1::0]{lang="EN-US"}[，两个成员的地址分别为]{style="font-family:宋体"}[1:1::1]{lang="EN-US"}[和]{style="font-family:宋体"}[1:2::1]{lang="EN-US"}[（前者为本地接口]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[的地址）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x104495961}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] anycast-rp 1:1::0 1:1::1]{lang="EN-US"}

[\[Sysname-pim6\] anycast-rp 1:1::0 1:2::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1325414511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[display ipv6 pim rp-info]{lang="EN-US"}]{#struct_0_x1176_16249_528244975}
:::

::: {#-503326435 .myid}
[]{#_Toc80176797}[]{#_Toc288743017}[]{#_Toc94588251}[]{#_Toc78346636}[]{#_Toc311538848}[]{#_Toc404790427}[]{#struct_0_x1176_16249_x248003928}[]{#_Toc345339173}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bidir-pim enable (IPv6 PIM view)**

------------------------------------------------------------------------

[**[bidir-pim]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_1287166929}[命令用来使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bidir-pim** **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_x491954041}[命令用来关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1848572146}

[**[bidir-pim]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_1957714425}

[**[undo]{lang="EN-US"}**[ **bidir-pim** **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_x1021160890}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x423449090}

[[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_x1262675246}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626270441}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_855182035}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1472512092}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x758680195}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x981929261}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1542853900}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_1040109106}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_18832682}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1934344927}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1626729193}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] bidir-pim enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1059016583}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 multicast routing]{lang="EN-US"}**]{#struct_0_x1176_16249_80701799}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[IPv6]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#245740746 .myid}
[]{#_Toc404790428}[]{#struct_0_x1176_16249_1527909535}[]{#_Toc345339174}[]{#_Toc341772846}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bidir-rp-limit (IPv6 PIM view)**

------------------------------------------------------------------------

[**[bidir-rp-limit]{lang="EN-US"}**]{#struct_0_x1176_16249_245910572}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的最大数目。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bidir-rp-limit**]{lang="EN-US"}]{#struct_0_x1176_16249_x1389833946}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x5463889}

[**[bidir-rp-limit]{lang="EN-US"}**[ *limit*]{lang="EN-US"}]{#struct_0_x1176_16249_440784744}

[**[undo]{lang="EN-US"}**[ **bidir-rp-limit**]{lang="EN-US"}]{#struct_0_x1176_16249_x406033588}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626663657}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1176_16249_1467087874}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x957709298}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x687594766}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1990203196}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_2045508373}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1390814127}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x335174777}

[*[limit]{lang="EN-US"}*]{#struct_0_x1176_16249_x2075717729}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的最大数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[到系统所允许的最大值。系统所允许的最大值会随设备的不同而有所差别，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626598121}

[[由于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_1013591668}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[为每个]{style="font-family:宋体"}[RP]{lang="EN-US"}[都要在所有]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[接口上进行]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举，因此实际组网中不建议配置多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[。通过本命令可以限制]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的数目，超出限制值的]{style="font-family:宋体"}[RP]{lang="EN-US"}[不会生效，仅能进行]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举而无法指导转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x555053087}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1424069579}[在公网实例中配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的最大数目为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1319521624}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] bidir-rp-limit 3]{lang="EN-US"}
:::

::: {#398074978 .myid}
[]{#_Toc404790429}[]{#struct_0_x1176_16249_x524382235}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bsm-fragment enable (IPv6 PIM view)**

------------------------------------------------------------------------

[**[bsm-fragment]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_x30807479}[命令用来使能自举报文语义分片功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bsm-fragment** **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_x275266847}[命令用来关闭自举报文语义分片功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626532585}

[**[bsm-fragment]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_232827866}

[**[undo]{lang="EN-US"}**[ **bsm-fragment** **enable**]{lang="EN-US"}]{#struct_0_x1176_16249_x570635281}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1371447143}

[[自举报文语义分片功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1823048020}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1611966822}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_760606005}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x160495000}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x866359221}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1635848024}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1625942761}

[[当]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}]{#struct_0_x1176_16249_x1604160022}[域或双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[域中存在不支持自举报文语义分片的设备时，请关闭本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2023005677}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1009699221}[在公网实例中关闭自举报文语义分片功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_793197849}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] undo bsm-fragment enable]{lang="EN-US"}
:::

::: {#-92147151 .myid}
[]{#_Toc404790430}[]{#struct_0_x1176_16249_1134076239}[]{#_Toc311538849}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- bsr-policy (IPv6 PIM view)**

------------------------------------------------------------------------

[**[bsr-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x753390618}[命令用来配置合法的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址范围，以防止]{style="font-family:宋体"}[BSR]{lang="EN-US"}[欺骗。]{style="font-family:宋体"}

[**[undo bsr-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_1000403526}[命令用来取消]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址范围的限制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1625877225}

[**[bsr-policy]{lang="EN-US"}**[ *acl6-number*]{lang="EN-US"}]{#struct_0_x1176_16249_x1001792296}

[[undo bsr-policy]{lang="EN-US"}]{#struct_0_x1176_16249_x2032447233}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2057056886}

[[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_x188130074}[的地址范围不受任何限制，即认为来自任意源的自举报文都是合法的。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1096334238}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1690672528}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1359362529}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_2059484160}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1626467048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1594448337}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_667005779}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1442143887}

[[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_x1082339564}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定合法]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的源地址]{style="font-family:宋体"}[范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1920210363}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1658950957}[在公网实例中配置合法的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址范围，只允许网段]{style="font-family:宋体"}[2001::2/64]{lang="EN-US"}[中的设备充当]{style="font-family:宋体"}[BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x2076229079}

[\[Sysname\] acl ipv6 number 2000]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] rule permit source 2001::2 64]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] bsr-policy 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626401512}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[c-bsr]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_675144132}
:::

::: {#-898468924 .myid}
[]{#_Toc404790431}[]{#struct_0_x1176_16249_x62156278}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- c-bsr (IPv6 PIM view)**

------------------------------------------------------------------------

[**[c-bsr]{lang="EN-US"}**]{#struct_0_x1176_16249_x2020349322}[命令用来配置]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo c-bsr]{lang="EN-US"}**]{#struct_0_x1176_16249_1470670546}[命令用来删除]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1202468033}

[**[c-bsr]{lang="EN-US"}**[ *ipv6-address* \[ **scope** *scope-id* \] \[ **hash-length** *hash-length* \| **priority** *priority* \] \*]{lang="EN-US"}]{#struct_0_x1176_16249_x68696001}

[**[undo]{lang="EN-US"}**[ **c-bsr** *ipv6-address* \[ **scope** *scope-id* \]]{lang="EN-US"}]{#struct_0_x1176_16249_x1901247155}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1808333031}

[[没有配置]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}]{#struct_0_x1176_16249_x1626335976}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1318080013}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1790313764}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x31393024}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1065800446}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_691950280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x695665243}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x99056581}[：指定]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[scope]{lang="EN-US"}**[ *scope-id*]{lang="EN-US"}]{#struct_0_x1176_16249_1664582616}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[管理域的编号，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。如果未指定本参数，表示配置服务于]{style="font-family:宋体"}[Global]{lang="EN-US"}[域的]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hash-length ]{lang="EN-US"}***[hash-length]{lang="EN-US"}*]{#struct_0_x1176_16249_236338269}[：指定哈希掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[126]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x1176_16249_x1626270440}[：指定]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[64]{lang="EN-US"}[。数值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1873701320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C-BSR]{lang="EN-US"}]{#struct_0_x1176_16249_1683591544}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址必须有对应的本地接口，且该接口上必须使能]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[，否则配置不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果对同一个域多次执行本命令，新配置将覆盖旧配置；而针对不同域的]{style="font-family:宋体"}]{#struct_0_x1176_16249_x525210779}[C-BSR]{lang="EN-US"}[则允许指定相同的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1201012560}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1868815230}[在公网实例中将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1101::1]{lang="EN-US"}[的设备配置为]{style="font-family:宋体"}[Global]{lang="EN-US"}[域的]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_887986636}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] c-bsr 1101::1]{lang="EN-US"}
:::

::: {#1951689723 .myid}
[]{#_Toc404790432}[]{#struct_0_x1176_16249_x180286660}[]{#_Toc288743018}[]{#_Toc94588256}[]{#_Toc315954784}[]{#_Toc315954785}[]{#_Toc315954786}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- c-rp (IPv6 PIM view)**

------------------------------------------------------------------------

[**[c-rp]{lang="EN-US"}**]{#struct_0_x1176_16249_x1626729192}[命令用来配置]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo c-rp]{lang="EN-US"}**]{#struct_0_x1176_16249_x507067358}[命令用来删除]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1729777227}

[**[c-rp ]{lang="EN-US"}***[ipv6-address ]{lang="EN-US"}*[\[ **advertisement-interval** *adv-interval* \| { **group-policy** *acl6-number* \| **scope** *scope-id* } \| **holdtime** *hold-time* \| **priority** *priority* \] \* \[ **bidir** \]]{lang="EN-US"}]{#struct_0_x1176_16249_x1644314911}

[**[undo c-rp]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x1462800878}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1261407000}

[[没有配置]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_1171161989}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1820934075}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_737382347}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626663656}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x98996067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x198621878}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x986336819}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x1556927040}[：指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[advertisement-interval]{lang="EN-US"}**[ *adv-interval*]{lang="EN-US"}]{#struct_0_x1176_16249_1160915329}[：指定发送宣告报文的间隔时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[group-policy]{lang="EN-US"}***[ acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_1106680234}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果指定了本参数，该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[将只为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组服务；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[将为所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组服务。]{style="font-family:宋体"}

[**[scope]{lang="EN-US"}**[ *scope-id*]{lang="EN-US"}]{#struct_0_x1176_16249_413410213}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[管理域的编号，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[holdtime]{lang="EN-US"}**[ *hold-time*]{lang="EN-US"}]{#struct_0_x1176_16249_5302510}[：指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[150]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x1176_16249_x1626598120}[：指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[192]{lang="EN-US"}[。该数值越大，优先级越低。]{style="font-family:宋体"}

[**[bidir]{lang="EN-US"}**]{#struct_0_x1176_16249_x1715291687}[：指定该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[服务于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果未指定本参数，该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[将服务于]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_314058427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_246704460}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址必须有对应的本地接口，且该接口上必须使能]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[，否则配置不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_1093540279}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[所服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围（若指定的不是]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，则此规则不生效），而其它可选参数都将被忽略。该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则用来定义该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[所服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围，只有]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组才会作为]{style="font-family:宋体"}[RP]{lang="EN-US"}[的服务组范围通告出去。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备想要成为多个组范围的]{style="font-family:宋体"}]{#struct_0_x1176_16249_x320972795}[C-RP]{lang="EN-US"}[，则需要在配置]{style="font-family:宋体"}**[group-policy]{lang="EN-US"}**[所对应的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时将多个组范围用多个]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[规则表示出来。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果对同一]{style="font-family:宋体"}]{#struct_0_x1176_16249_1172302588}[IPv6]{lang="EN-US"}[地址多次执行本命令，新配置将覆盖旧配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1589174696}

[]{#_Toc94588257}[]{#_Toc78346641}[]{#_Toc80176799}[]{#struct_0_x1176_16249_x1516790510}[]{#_Toc87442524}[]{#_Toc87787165}[]{#_Toc87852044}[]{#_Toc87852823}[]{#_Toc87853604}[]{#_Toc87867643}[]{#_Toc87442525}[]{#_Toc87787166}[]{#_Toc87852045}[]{#_Toc87852824}[]{#_Toc87853605}[]{#_Toc87867644}[]{#_Toc87442528}[]{#_Toc87787169}[]{#_Toc87852048}[]{#_Toc87852827}[]{#_Toc87853608}[]{#_Toc87867647}[]{#_Toc87442530}[]{#_Toc87787171}[]{#_Toc87852050}[]{#_Toc87852829}[]{#_Toc87853610}[]{#_Toc87867649}[]{#_Toc87442531}[]{#_Toc87787172}[]{#_Toc87852051}[]{#_Toc87852830}[]{#_Toc87853611}[]{#_Toc87867650}[]{#_Toc87442532}[]{#_Toc87787173}[]{#_Toc87852052}[]{#_Toc87852831}[]{#_Toc87853612}[]{#_Toc87867651}[]{#_Toc87442533}[]{#_Toc87787174}[]{#_Toc87852053}[]{#_Toc87852832}[]{#_Toc87853613}[]{#_Toc87867652}[]{#_Toc87442534}[]{#_Toc87787175}[]{#_Toc87852054}[]{#_Toc87852833}[]{#_Toc87853614}[]{#_Toc87867653}[]{#_Toc87442535}[]{#_Toc87787176}[]{#_Toc87852055}[]{#_Toc87852834}[]{#_Toc87853615}[]{#_Toc87867654}[]{#_Toc87442536}[]{#_Toc87787177}[]{#_Toc87852056}[]{#_Toc87852835}[]{#_Toc87853616}[]{#_Toc87867655}[]{#_Toc87442537}[]{#_Toc87787178}[]{#_Toc87852057}[]{#_Toc87852836}[]{#_Toc87853617}[]{#_Toc87867656}[]{#_Toc87442538}[]{#_Toc87787179}[]{#_Toc87852058}[]{#_Toc87852837}[]{#_Toc87853618}[]{#_Toc87867657}[]{#_Toc87442539}[]{#_Toc87787180}[]{#_Toc87852059}[]{#_Toc87852838}[]{#_Toc87853619}[]{#_Toc87867658}[]{#_Toc87442540}[]{#_Toc87787181}[]{#_Toc87852060}[]{#_Toc87852839}[]{#_Toc87853620}[]{#_Toc87867659}[]{#_Toc87442541}[]{#_Toc87787182}[]{#_Toc87852061}[]{#_Toc87852840}[]{#_Toc87853621}[]{#_Toc87867660}[]{#_Toc87442542}[]{#_Toc87787183}[]{#_Toc87852062}[]{#_Toc87852841}[]{#_Toc87853622}[]{#_Toc87867661}[]{#_Toc87442543}[]{#_Toc87787184}[]{#_Toc87852063}[]{#_Toc87852842}[]{#_Toc87853623}[]{#_Toc87867662}[]{#_Toc87442544}[]{#_Toc87787185}[]{#_Toc87852064}[]{#_Toc87852843}[]{#_Toc87853624}[]{#_Toc87867663}[]{#_Toc87442545}[]{#_Toc87787186}[]{#_Toc87852065}[]{#_Toc87852844}[]{#_Toc87853625}[]{#_Toc87867664}[]{#_Toc87442547}[]{#_Toc87787188}[]{#_Toc87852067}[]{#_Toc87852846}[]{#_Toc87853627}[]{#_Toc87867666}[\# ]{lang="EN-US"}[在公网实例中将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[配置为组播组]{style="font-family:宋体"}[FF0E:0:1391::/96]{lang="EN-US"}[的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[，且]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1626532584}

[\[Sysname\] acl ipv6 number 2000]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] rule permit source ff0e:0:1391:: 96]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] c-rp 2001::1 group-policy 2000 priority 10]{lang="EN-US"}
:::

::: {#-1446506679 .myid}
[]{#_Toc288743019}[]{#_Toc94588260}[]{#_Toc80176801}[]{#_Toc404790433}[]{#struct_0_x1176_16249_1798911807}[]{#_Toc311538852}[]{#_Toc135108784}[]{#_Toc135109843}[]{#_Toc136489183}[]{#_Toc135108785}[]{#_Toc135109844}[]{#_Toc136489184}[]{#_Toc135108786}[]{#_Toc135109845}[]{#_Toc136489185}[]{#_Toc135108787}[]{#_Toc135109846}[]{#_Toc136489186}[]{#_Toc135108788}[]{#_Toc135109847}[]{#_Toc136489187}[]{#_Toc135108789}[]{#_Toc135109848}[]{#_Toc136489188}[]{#_Toc135108790}[]{#_Toc135109849}[]{#_Toc136489189}[]{#_Toc135108791}[]{#_Toc135109850}[]{#_Toc136489190}[]{#_Toc135108792}[]{#_Toc135109851}[]{#_Toc136489191}[]{#_Toc135108793}[]{#_Toc135109852}[]{#_Toc136489192}[]{#_Toc135108794}[]{#_Toc135109853}[]{#_Toc136489193}[]{#_Toc135108795}[]{#_Toc135109854}[]{#_Toc136489194}[]{#_Toc135108796}[]{#_Toc135109855}[]{#_Toc136489195}[]{#_Toc135108797}[]{#_Toc135109856}[]{#_Toc136489196}[]{#_Toc135108798}[]{#_Toc135109857}[]{#_Toc136489197}[]{#_Toc135108799}[]{#_Toc135109858}[]{#_Toc136489198}[]{#_Toc135108800}[]{#_Toc135109859}[]{#_Toc136489199}[]{#_Toc135108801}[]{#_Toc135109860}[]{#_Toc136489200}[]{#_Toc135108802}[]{#_Toc135109861}[]{#_Toc136489201}[]{#_Toc135108803}[]{#_Toc135109862}[]{#_Toc136489202}[]{#_Toc135108804}[]{#_Toc135109863}[]{#_Toc136489203}[]{#_Toc87442552}[]{#_Toc87787193}[]{#_Toc87852072}[]{#_Toc87852851}[]{#_Toc87853632}[]{#_Toc87867671}[]{#_Toc87442553}[]{#_Toc87787194}[]{#_Toc87852073}[]{#_Toc87852852}[]{#_Toc87853633}[]{#_Toc87867672}[]{#_Toc87442554}[]{#_Toc87787195}[]{#_Toc87852074}[]{#_Toc87852853}[]{#_Toc87853634}[]{#_Toc87867673}[]{#_Toc87442555}[]{#_Toc87787196}[]{#_Toc87852075}[]{#_Toc87852854}[]{#_Toc87853635}[]{#_Toc87867674}[]{#_Toc87442556}[]{#_Toc87787197}[]{#_Toc87852076}[]{#_Toc87852855}[]{#_Toc87853636}[]{#_Toc87867675}[]{#_Toc87442557}[]{#_Toc87787198}[]{#_Toc87852077}[]{#_Toc87852856}[]{#_Toc87853637}[]{#_Toc87867676}[]{#_Toc87442558}[]{#_Toc87787199}[]{#_Toc87852078}[]{#_Toc87852857}[]{#_Toc87853638}[]{#_Toc87867677}[]{#_Toc87442559}[]{#_Toc87787200}[]{#_Toc87852079}[]{#_Toc87852858}[]{#_Toc87853639}[]{#_Toc87867678}[]{#_Toc87442560}[]{#_Toc87787201}[]{#_Toc87852080}[]{#_Toc87852859}[]{#_Toc87853640}[]{#_Toc87867679}[]{#_Toc87442561}[]{#_Toc87787202}[]{#_Toc87852081}[]{#_Toc87852860}[]{#_Toc87853641}[]{#_Toc87867680}[]{#_Toc87442562}[]{#_Toc87787203}[]{#_Toc87852082}[]{#_Toc87852861}[]{#_Toc87853642}[]{#_Toc87867681}[]{#_Toc87442563}[]{#_Toc87787204}[]{#_Toc87852083}[]{#_Toc87852862}[]{#_Toc87853643}[]{#_Toc87867682}[]{#_Toc87442564}[]{#_Toc87787205}[]{#_Toc87852084}[]{#_Toc87852863}[]{#_Toc87853644}[]{#_Toc87867683}[]{#_Toc87442565}[]{#_Toc87787206}[]{#_Toc87852085}[]{#_Toc87852864}[]{#_Toc87853645}[]{#_Toc87867684}[]{#_Toc87442566}[]{#_Toc87787207}[]{#_Toc87852086}[]{#_Toc87852865}[]{#_Toc87853646}[]{#_Toc87867685}[]{#_Toc87442567}[]{#_Toc87787208}[]{#_Toc87852087}[]{#_Toc87852866}[]{#_Toc87853647}[]{#_Toc87867686}[]{#_Toc87442568}[]{#_Toc87787209}[]{#_Toc87852088}[]{#_Toc87852867}[]{#_Toc87853648}[]{#_Toc87867687}[]{#_Toc87442569}[]{#_Toc87787210}[]{#_Toc87852089}[]{#_Toc87852868}[]{#_Toc87853649}[]{#_Toc87867688}[]{#_Toc87442570}[]{#_Toc87787211}[]{#_Toc87852090}[]{#_Toc87852869}[]{#_Toc87853650}[]{#_Toc87867689}[]{#_Toc87442571}[]{#_Toc87787212}[]{#_Toc87852091}[]{#_Toc87852870}[]{#_Toc87853651}[]{#_Toc87867690}[]{#_Toc87442572}[]{#_Toc87787213}[]{#_Toc87852092}[]{#_Toc87852871}[]{#_Toc87853652}[]{#_Toc87867691}[]{#_Toc87442573}[]{#_Toc87787214}[]{#_Toc87852093}[]{#_Toc87852872}[]{#_Toc87853653}[]{#_Toc87867692}[]{#_Toc60064364}[]{#_Toc60649326}[]{#_Toc76002960}[]{#_Toc76444885}[]{#_Toc60064365}[]{#_Toc60649327}[]{#_Toc76002961}[]{#_Toc76444886}[]{#_Toc60064366}[]{#_Toc60649328}[]{#_Toc76002962}[]{#_Toc76444887}[]{#_Toc60064367}[]{#_Toc60649329}[]{#_Toc76002963}[]{#_Toc76444888}[]{#_Toc60064368}[]{#_Toc60649330}[]{#_Toc76002964}[]{#_Toc76444889}[]{#_Toc60064369}[]{#_Toc60649331}[]{#_Toc76002965}[]{#_Toc76444890}[]{#_Toc60064370}[]{#_Toc60649332}[]{#_Toc76002966}[]{#_Toc76444891}[]{#_Toc60064371}[]{#_Toc60649333}[]{#_Toc76002967}[]{#_Toc76444892}[]{#_Toc60064372}[]{#_Toc60649334}[]{#_Toc76002968}[]{#_Toc76444893}[]{#_Toc60064373}[]{#_Toc60649335}[]{#_Toc76002969}[]{#_Toc76444894}[]{#_Toc60064374}[]{#_Toc60649336}[]{#_Toc76002970}[]{#_Toc76444895}[]{#_Toc60064375}[]{#_Toc60649337}[]{#_Toc76002971}[]{#_Toc76444896}[]{#_Toc60064376}[]{#_Toc60649338}[]{#_Toc76002972}[]{#_Toc76444897}[]{#_Toc60064377}[]{#_Toc60649339}[]{#_Toc76002973}[]{#_Toc76444898}[]{#_Toc60064378}[]{#_Toc60649340}[]{#_Toc76002974}[]{#_Toc76444899}[]{#_Toc60064381}[]{#_Toc60649343}[]{#_Toc76002977}[]{#_Toc76444902}[]{#_Toc60064382}[]{#_Toc60649344}[]{#_Toc76002978}[]{#_Toc76444903}[]{#_Toc60064383}[]{#_Toc60649345}[]{#_Toc76002979}[]{#_Toc76444904}[]{#_Toc60064384}[]{#_Toc60649346}[]{#_Toc76002980}[]{#_Toc76444905}[]{#_Toc60064385}[]{#_Toc60649347}[]{#_Toc76002981}[]{#_Toc76444906}[]{#_Toc60064386}[]{#_Toc60649348}[]{#_Toc76002982}[]{#_Toc76444907}[]{#_Toc60064387}[]{#_Toc60649349}[]{#_Toc76002983}[]{#_Toc76444908}[]{#_Toc60064388}[]{#_Toc60649350}[]{#_Toc76002984}[]{#_Toc76444909}[]{#_Toc60064389}[]{#_Toc60649351}[]{#_Toc76002985}[]{#_Toc76444910}[]{#_Toc60064390}[]{#_Toc60649352}[]{#_Toc76002986}[]{#_Toc76444911}[]{#_Toc60064391}[]{#_Toc60649353}[]{#_Toc76002987}[]{#_Toc76444912}[]{#_Toc60064392}[]{#_Toc60649354}[]{#_Toc76002988}[]{#_Toc76444913}[]{#_Toc60064393}[]{#_Toc60649355}[]{#_Toc76002989}[]{#_Toc76444914}[]{#_Toc60064394}[]{#_Toc60649356}[]{#_Toc76002990}[]{#_Toc76444915}[]{#_Toc60064395}[]{#_Toc60649357}[]{#_Toc76002991}[]{#_Toc76444916}[]{#_Toc60064396}[]{#_Toc60649358}[]{#_Toc76002992}[]{#_Toc76444917}[]{#_Toc60064397}[]{#_Toc60649359}[]{#_Toc76002993}[]{#_Toc76444918}[]{#_Toc60064398}[]{#_Toc60649360}[]{#_Toc76002994}[]{#_Toc76444919}[]{#_Toc60064399}[]{#_Toc60649361}[]{#_Toc76002995}[]{#_Toc76444920}[]{#_Toc60064400}[]{#_Toc60649362}[]{#_Toc76002996}[]{#_Toc76444921}[]{#_Toc60064401}[]{#_Toc60649363}[]{#_Toc76002997}[]{#_Toc76444922}[]{#_Toc60064402}[]{#_Toc60649364}[]{#_Toc76002998}[]{#_Toc76444923}[]{#_Toc60064403}[]{#_Toc60649365}[]{#_Toc76002999}[]{#_Toc76444924}[]{#_Toc60064404}[]{#_Toc60649366}[]{#_Toc76003000}[]{#_Toc76444925}[]{#_Toc60064407}[]{#_Toc60649369}[]{#_Toc76003003}[]{#_Toc76444928}[]{#_Toc60064408}[]{#_Toc60649370}[]{#_Toc76003004}[]{#_Toc76444929}[]{#_Toc60064409}[]{#_Toc60649371}[]{#_Toc76003005}[]{#_Toc76444930}[]{#_Toc60064410}[]{#_Toc60649372}[]{#_Toc76003006}[]{#_Toc76444931}[]{#_Toc60064411}[]{#_Toc60649373}[]{#_Toc76003007}[]{#_Toc76444932}[]{#_Toc60064412}[]{#_Toc60649374}[]{#_Toc76003008}[]{#_Toc76444933}[]{#_Toc60064413}[]{#_Toc60649375}[]{#_Toc76003009}[]{#_Toc76444934}[]{#_Toc60064414}[]{#_Toc60649376}[]{#_Toc76003010}[]{#_Toc76444935}[]{#_Toc60064415}[]{#_Toc60649377}[]{#_Toc76003011}[]{#_Toc76444936}[]{#_Toc60064416}[]{#_Toc60649378}[]{#_Toc76003012}[]{#_Toc76444937}[]{#_Toc60064417}[]{#_Toc60649379}[]{#_Toc76003013}[]{#_Toc76444938}[]{#_Toc60064418}[]{#_Toc60649380}[]{#_Toc76003014}[]{#_Toc76444939}[]{#_Toc60064419}[]{#_Toc60649381}[]{#_Toc76003015}[]{#_Toc76444940}[]{#_Toc60064420}[]{#_Toc60649382}[]{#_Toc76003016}[]{#_Toc76444941}[]{#_Toc60064421}[]{#_Toc60649383}[]{#_Toc76003017}[]{#_Toc76444942}[]{#_Toc60064422}[]{#_Toc60649384}[]{#_Toc76003018}[]{#_Toc76444943}[]{#_Toc60064423}[]{#_Toc60649385}[]{#_Toc76003019}[]{#_Toc76444944}[]{#_Toc60064424}[]{#_Toc60649386}[]{#_Toc76003020}[]{#_Toc76444945}[]{#_Toc60064425}[]{#_Toc60649387}[]{#_Toc76003021}[]{#_Toc76444946}[]{#_Toc60064426}[]{#_Toc60649388}[]{#_Toc76003022}[]{#_Toc76444947}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- crp-policy (IPv6 PIM view)**

------------------------------------------------------------------------

[**[crp-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x1424629014}[命令用来配置合法的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[地址范围及其服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围，以防止]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[欺骗。]{style="font-family:宋体"}

[**[undo crp-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_1596905885}[命令用来取消]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[地址范围及其服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围的限制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1687991646}

[**[crp-policy]{lang="EN-US"}**[ *acl6-number*]{lang="EN-US"}]{#struct_0_x1176_16249_437185257}

[[undo crp-policy]{lang="EN-US"}]{#struct_0_x1176_16249_x1594161203}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2077560181}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x1625942760}[地址范围及其服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围不受任何限制，即认为所有收到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[报文都是合法的。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1124723333}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1055560019}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1500914799}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1824328395}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x816878825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_879458299}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_x1423996749}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1896198219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_x1625877224}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定合法]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址范围，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[参数用来指定该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[所服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，]{style="font-family:宋体"}[而除]{lang="EN-US" style="font-family:
宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令在对]{style="font-family:宋体"}]{#struct_0_x1176_16249_564291645}[C-RP]{lang="EN-US"}[所宣告的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围进行过滤时，只取其前缀部分进行匹配。例如，]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[宣告的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围为]{style="font-family:宋体"}[FF0E:0:1::/96]{lang="EN-US"}[，如果其前缀部分"]{style="font-family:宋体"}[FF0E:0:1::]{lang="EN-US"}["能匹配上本命令所引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则，就认为整个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围"]{style="font-family:宋体"}[FF0E:0:1::/96]{lang="EN-US"}["都通过了过滤。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1229621725}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1684661392}[在公网实例中配置]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[策略，只允许]{style="font-family:宋体"}[2001::2/64]{lang="EN-US"}[范围内的设备充当]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[，且只允许其为]{style="font-family:宋体"}[FF03::101/64]{lang="EN-US"}[范围内的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_892837358}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule permit ipv6 source 2001::2 64 destination ff03::101 64]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] crp-policy 3000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2026679203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[c-rp]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x867024620}
:::

::: {#831947945 .myid}
[]{#_Toc404790434}[]{#struct_0_x1176_16249_1864626894}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim bsr-info**

------------------------------------------------------------------------

[**[display ipv6 pim bsr-info]{lang="EN-US"}**]{#struct_0_x1176_16249_x1626467051}[命令用来显示]{style="font-family:
宋体"}[IPv6 PIM-SM]{lang="EN-US"}[域中的]{style="font-family:
宋体"}[BSR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1490599842}

[**[display ipv6 pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **bsr-info**]{lang="EN-US"}]{#struct_0_x1176_16249_x395727600}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x438592797}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x367277133}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x575909668}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1201739410}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x2049905805}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1268623367}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x1626401515}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1434659019}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_x1640217323}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x159558050}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1784244409}[显示公网实例]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[域中的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[]{#_Toc80176802}[[\<Sysname\> display ipv6 pim bsr-info]{lang="EN-US"}]{#struct_0_x1176_16249_x1626335979}

[ Scope: non-scoped]{lang="EN-US"}

[     State: Accept Preferred]{lang="EN-US"}

[     Bootstrap timer: 00:01:44]{lang="EN-US"}

[     Elected BSR address: 12:12::1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 126]{lang="EN-US"}

[       Uptime: 00:21:56]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Scope: 5]{lang="EN-US"}

[     State: Accept Any]{lang="EN-US"}

[     Scope-zone expiry timer: 00:21:12]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Scope: 6]{lang="EN-US"}

[     State: Elected]{lang="EN-US"}

[     Bootstrap timer: 00:00:26]{lang="EN-US"}

[     Elected BSR address: 17:11::1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 126]{lang="EN-US"}

[       Uptime: 02:53:37]{lang="EN-US"}

[     Candidate BSR address: 17:11::1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 126]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Scope: 7]{lang="EN-US"}

[     State: Candidate]{lang="EN-US"}

[     Bootstrap timer: 00:01:56]{lang="EN-US"}

[     Elected BSR address: 61:37::1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 126]{lang="EN-US"}

[       Uptime: 02:53:32]{lang="EN-US"}

[     Candidate BSR address: 17:12::1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 126]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Scope: 8]{lang="EN-US"}

[     State: Pending]{lang="EN-US"}

[     Bootstrap timer: 00:00:07]{lang="EN-US"}

[     Candidate BSR address: 17:13::1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 126]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ipv6 pim bsr-info]{lang="EN-US"}]{#struct_0_x1176_16249_x1410803342}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1621463934}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626270443}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_x307617379}

[[Scope]{lang="EN-US"}]{#struct_0_x1176_16249_1854164854}

[[域]{style="font-family:宋体"}]{#struct_0_x1176_16249_1653756555}

[[State]{lang="EN-US"}]{#struct_0_x1176_16249_56977672}

[[域状态]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1758348018}

[[Bootstrap timer]{lang="EN-US"}]{#struct_0_x1176_16249_1685047123}

[[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_x1626729195}[定时器]{style="font-family:宋体"}

[[Scope-zone expiry timer]{lang="EN-US"}]{#struct_0_x1176_16249_1865585637}

[[域老化定时器]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1948476881}

[[Elected BSR address]{lang="EN-US"}]{#struct_0_x1176_16249_1157600002}

[[当选]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_1571300559}[的地址]{style="font-family:宋体"}

[[Candidate BSR address]{lang="EN-US"}]{#struct_0_x1176_16249_1392522540}

[[候选]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_x1626663659}[的地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x1176_16249_x1665080008}

[[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_x1901485007}[的优先级]{style="font-family:宋体"}

[[Hash mask length]{lang="EN-US"}]{#struct_0_x1176_16249_x1167352204}

[[哈希掩码长度]{style="font-family:宋体"}]{#struct_0_x1176_16249_x938398453}

[[Uptime]{lang="EN-US"}]{#struct_0_x1176_16249_x1626598123}

[[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_x2118576214}[已存在的时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1215204040 .myid}
[]{#_Toc94588263}[]{#_Toc288743020}[]{#_Toc404790435}[]{#struct_0_x1176_16249_509805571}[]{#_Toc311538854}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim claimed-route**

------------------------------------------------------------------------

[**[display ipv6 pim claimed-route]{lang="EN-US"}**]{#struct_0_x1176_16249_1197909369}[命令用来显示]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[所使用的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1116258795}

[**[display ipv6 pim]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **claimed-route** \[ *ipv6-source-address* \]]{lang="EN-US"}]{#struct_0_x1176_16249_x1394392077}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2042618948}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_320658547}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626532587}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x929971548}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_1268151892}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x181286847}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x2095633030}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1643363641}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_1474809697}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的路由信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的路由信息。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x1176_16249_1753356947}[：组播源的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，显示到达指定组播源的路由信息。如果未指定本参数，将显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[所使用的所有路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1827826069}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1625942763}[显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[在公网实例中使用的所有路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim claimed-route]{lang="EN-US"}]{#struct_0_x1176_16249_1528007860}

[ RPF-route selecting rule: longest-match]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route/mask: 7:11::/64 (unicast (direct))]{lang="EN-US"}

[     RPF interface: Vlan-interface2, RPF neighbor: 8::2]{lang="EN-US"}

[     Total number of (S,G) or (\*,G) dependent on this route entry: 4]{lang="EN-US"}

[     (7:11::10, ff1e::1)]{lang="EN-US"}

[     (7:11::10, ff1e::2)]{lang="EN-US"}

[     (7:11::10, ff1e::3)]{lang="EN-US"}

[     (\*, ff1e::4)]{lang="EN-US"}

[ Route/mask: 7:12::/64 (unicast)]{lang="EN-US"}

[     RPF interface: Vlan-interface2, RPF neighbor: 8::3,]{lang="EN-US"}

[     Total number of (S,G) or (\*,G) dependent on this route entry: 2]{lang="EN-US"}

[     (7:12::10, ff1e::1)]{lang="EN-US"}

[     (7:12::10, ff1e::2)]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipv6 pim claimed-route]{lang="EN-US"}]{#struct_0_x1176_16249_x1121140918}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1618759133}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_x980409928}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1625877227}

[[RPF-route selecting rule]{lang="EN-US"}]{#struct_0_x1176_16249_2130375586}

[[RPF]{lang="EN-US"}]{#struct_0_x1176_16249_1069793528}[路由的选择规则]{style="font-family:宋体"}

[[Route/mask]{lang="EN-US"}]{#struct_0_x1176_16249_1562554686}

[[路由项。括号内为路由类型，包括：]{style="font-family:宋体"}]{#struct_0_x1176_16249_326051228}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="EN-US"}]{#struct_0_x1176_16249_x755682083}[：单播路由（内部网关协议）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="EN-US"}]{#struct_0_x1176_16249_x269874788}[：单播路由（外部网关协议）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unicast (direct)]{lang="EN-US"}]{#struct_0_x1176_16249_x1626467050}[：单播路由（直连）]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unicast]{lang="EN-US"}]{#struct_0_x1176_16249_1238283513}[：其它单播路由（如单播静态路由等）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[mbgp]{lang="EN-US"}]{#struct_0_x1176_16249_1725532663}[：]{lang="EN-US" style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[MBGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}

[[RPF interface]{lang="EN-US"}]{#struct_0_x1176_16249_x2141971344}

[[RPF]{lang="EN-US"}]{#struct_0_x1176_16249_490865401}[接口的名称]{style="font-family:宋体"}

[[RPF neighbor]{lang="EN-US"}]{#struct_0_x1176_16249_x835395046}

[[RPF]{lang="EN-US"}]{#struct_0_x1176_16249_x1626401514}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Total number of (S,G) or (\*,G) dependent ]{lang="EN-US"}]{#struct_0_x1176_16249_x131424922}

[[on this route entry]{lang="EN-US"}]{#struct_0_x1176_16249_x843771863}

[[基于此]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_x1176_16249_1632077322}[路由的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）个数及列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-398258569 .myid}
[]{#_Toc404790436}[]{#struct_0_x1176_16249_x843860149}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim c-rp**

------------------------------------------------------------------------

[**[display ipv6 pim c-rp]{lang="EN-US"}**]{#struct_0_x1176_16249_x1912991282}[命令用来显示]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[域中的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626335978}

[**[display ipv6 pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **c-rp** \[ **local** \]]{lang="EN-US"}]{#struct_0_x1176_16249_155280599}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_13032714}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x708146998}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_945674763}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x58060162}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x1202734652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_680329756}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x952867850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626270442}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_1258466562}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1176_16249_x466327319}[：显示本地配置且生效的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。如果未指定本参数，将显示所有学习到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x530099935}

[[只有当选的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_x1604316690}[上才会有学习到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息，其它设备上只能查看到本地配置生效的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_948042102}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_149752115}[显示公网实例中学习到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim c-rp]{lang="EN-US"}]{#struct_0_x1176_16249_x1626729194}

[ Scope: non-scoped]{lang="EN-US"}

[     Group/MaskLen: FF00::/8 \[B\]]{lang="EN-US"}

[       C-RP address             Priority  HoldTime  Uptime    Expires]{lang="EN-US"}

[       8:12::2 (local)          192       150       00:27:48  00:01:43]{lang="EN-US"}

[     Group/MaskLen: FF23::/92 Expires: 00:02:07]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_299501696}[显示本地配置生效的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim c-rp local]{lang="EN-US"}]{#struct_0_x1176_16249_x2081213080}

[ Candidate RP: 8:12::2(Loop1)]{lang="EN-US"}

[     Priority: 192]{lang="EN-US"}

[     HoldTime: 150]{lang="EN-US"}

[     Advertisement interval: 60]{lang="EN-US"}

[     Next advertisement scheduled at: 00:00:46]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ipv6 pim c-rp]{lang="EN-US"}]{#struct_0_x1176_16249_1534708939}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1612574007}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_1682618766}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_x848965039}

[[Scope]{lang="EN-US"}]{#struct_0_x1176_16249_1178579937}

[[域]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1626663658}

[[Group/MaskLen]{lang="EN-US"}]{#struct_0_x1176_16249_1063803347}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_830124185}[所服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}

[[\[B\]]{lang="EN-US"}]{#struct_0_x1176_16249_1091088973}

[[表示]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x144985126}[服务于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果未显示本字段，则表示服务于]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}

[[C-RP address]{lang="EN-US"}]{#struct_0_x1176_16249_1940435936}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x1626598122}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示本地地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x1176_16249_x552492273}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x835581607}[的优先级]{style="font-family:宋体"}

[[HoldTime]{lang="EN-US"}]{#struct_0_x1176_16249_726691289}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x1099357090}[的超时时间]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_x1176_16249_1266806175}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x1626532586}[已存在的时间，]{style="font-family:宋体"}[w]{lang="EN-US"}[表示星期，]{style="font-family:宋体"}[d]{lang="EN-US"}[表示天，]{style="font-family:宋体"}[h]{lang="EN-US"}[表示小时]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_x1176_16249_636112393}

[[C-RP/]{lang="EN-US"}]{#struct_0_x1176_16249_x944729164}[组播组的超时剩余时间]{style="font-family:宋体"}

[[Candidate RP]{lang="EN-US"}]{#struct_0_x1176_16249_843983586}

[[本地]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x1154291545}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Advertisement interval]{lang="EN-US"}]{#struct_0_x1176_16249_x1625942762}

[[本地]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x38076081}[发送通告报文时间间隔]{style="font-family:宋体"}

[[Next advertisement scheduled at]{lang="EN-US"}]{#struct_0_x1176_16249_128075022}

[[本地]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_1474066195}[发送下一个通告报文的剩余时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2139670395 .myid}
[]{#_Toc288743021}[]{#_Toc404790437}[]{#struct_0_x1176_16249_1698230432}[]{#_Toc345339183}[]{#_Toc341772845}[]{#_Toc321055242}[]{#_Toc263693129}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim df-info**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipv6** **pim** **df-info**]{lang="EN-US"}]{#struct_0_x1176_16249_x771270419}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[DF]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x724958755}

[**[display]{lang="EN-US"}**[ **ipv6** **pim** \[ **vpn-instance** *vpn-instance-name* \] **df-info** \[ *ipv6-rp-address* \]]{lang="EN-US"}]{#struct_0_x1176_16249_x1625877226}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x598507769}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x449930586}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1974735291}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x46558608}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x1185358641}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1621913895}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_1888129168}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_23217944}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_747196759}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[ipv6-rp-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x1626467053}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x327800428}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1766126505}[显示公网实例中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[DF]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim df-info]{lang="EN-US"}]{#struct_0_x1176_16249_1065684814}

[RP address: 12::12]{lang="EN-US"}

[  Interface: GigabitEthernet0/0/4]{lang="EN-US"}

[    State     : Win        DF preference: 10]{lang="EN-US"}

[    DF metric : 1562       DF uptime    : 00:07:15]{lang="EN-US"}

[    DF address: FE80::202:FF:FE00:9 (local)]{lang="EN-US"}

[  Interface: Tunnel0, FE80::20:12]{lang="EN-US"}

[    State     : Lose       DF preference: 0]{lang="EN-US"}

[    DF metric : 0          DF uptime    : 00:07:15]{lang="EN-US"}

[    DF address: FE80::20:12]{lang="EN-US"}

[[表]{style="font-family:黑体"}[1-3 display ipv6 pim df-info]{lang="EN-US"}]{#struct_0_x1176_16249_x962756850}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1727986663}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_1115544838}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_247096731}

[[RP address]{lang="EN-US"}]{#struct_0_x1176_16249_x1951895997}

[[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_1813180672}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1176_16249_603523699}

[[接口名称，使能了]{style="font-family:宋体"}[nbma]{lang="EN-US"}]{#struct_0_x1176_16249_1054608935}[模式的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道口，显示远端连接]{style="font-family:宋体"}[IPv6 link-local]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1176_16249_x2125359656}

[[DF]{lang="EN-US"}]{#struct_0_x1176_16249_x559275715}[的选举状态：]{style="font-family:宋体"}

[[Win]{lang="EN-US"}]{#struct_0_x1176_16249_x1589663008}[：竞选]{style="font-family:宋体"}[DF]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Lose]{lang="EN-US"}]{#struct_0_x1176_16249_1006808226}[：竞选]{style="font-family:宋体"}[DF]{lang="EN-US"}[落败]{style="font-family:宋体"}

[[Offer]{lang="EN-US"}]{#struct_0_x1176_16249_996591548}[：竞选]{style="font-family:宋体"}[DF]{lang="EN-US"}[的初始状态]{style="font-family:宋体"}

[[Backoff]{lang="EN-US"}]{#struct_0_x1176_16249_x1365844769}[：正在充当]{style="font-family:宋体"}[DF]{lang="EN-US"}[，但有更优的设备正在竞选]{style="font-family:宋体"}[DF]{lang="EN-US"}

[[-]{lang="EN-US"}]{#struct_0_x1176_16249_200239172}[：不参与]{style="font-family:宋体"}[DF]{lang="EN-US"}[竞选]{style="font-family:宋体"}

[[DF preference]{lang="EN-US"}]{#struct_0_x1176_16249_94276451}

[[DF]{lang="EN-US"}]{#struct_0_x1176_16249_1766323113}[通告的路由优先级]{style="font-family:宋体"}

[[DF metric]{lang="EN-US"}]{#struct_0_x1176_16249_x962560242}

[[DF]{lang="EN-US"}]{#struct_0_x1176_16249_x460840663}[通告的路由度量值]{style="font-family:宋体"}

[[DF uptime]{lang="EN-US"}]{#struct_0_x1176_16249_247293339}

[[DF]{lang="EN-US"}]{#struct_0_x1176_16249_1043438543}[已存在的时间]{style="font-family:宋体"}

[[DF address]{lang="EN-US"}]{#struct_0_x1176_16249_1813377280}

[[DF]{lang="EN-US"}]{#struct_0_x1176_16249_603458163}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示本地地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#347193684 .myid}
[]{#_Toc404790438}[]{#struct_0_x1176_16249_x1667888202}[]{#_Toc403459938}[]{#_Toc403459939}[]{#_Toc403459940}[]{#_Toc403459941}[]{#_Toc403459942}[]{#_Toc403459943}[]{#_Toc403459944}[]{#_Toc403459974}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim interface**

------------------------------------------------------------------------

[**[display ipv6 pim interface]{lang="EN-US"}**]{#struct_0_x1176_16249_x41097005}[命令用来显示接口上的]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_476369663}

[**[display ipv6 pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **interface** \[ *interface-type interface-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x1176_16249_x1626729197}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1266582245}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_1688494883}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1770305183}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_192265121}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x1465735112}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_813381751}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_142201308}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1249734231}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_x1626663661}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_x1176_16249_x2021244832}[：显示指定接口上的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[信息。如果未指定本参数，将显示所有接口上的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1176_16249_1070704426}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1472595732}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1427673652}[显示公网实例所有接口上的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim interface]{lang="EN-US"}]{#struct_0_x1176_16249_x1074032278}

[ Interface         NbrCnt  HelloInt  DR-Pri     DR-Address]{lang="EN-US"}

[ GE1/0/1           1       30        1          ]{lang="EN-US"}[FE80::200:5EFF:FE04:8700]{lang="DE"}

[[表1-4 ]{lang="EN-US"}[display ipv6 pim interface]{lang="EN-US"}]{#struct_0_x1176_16249_x1783966003}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1642358990}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1999419306}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1626598125}

[[Interface]{lang="EN-US"}]{#struct_0_x1176_16249_x1312007160}

[[接口名称]{style="font-family:宋体"}]{#struct_0_x1176_16249_x522472127}

[[NbrCnt]{lang="EN-US"}]{#struct_0_x1176_16249_x1842091377}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_22443762}[邻居的数量]{style="font-family:宋体"}

[[HelloInt]{lang="EN-US"}]{#struct_0_x1176_16249_x557156333}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_x1626532589}[报文的时间间隔]{style="font-family:宋体"}

[[DR-Pri]{lang="EN-US"}]{#struct_0_x1176_16249_x2092770962}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x1176_16249_x1921006129}[的优先级]{style="font-family:宋体"}

[[DR-Address]{lang="EN-US"}]{#struct_0_x1176_16249_956953879}

[[DR]{lang="EN-US"}]{#struct_0_x1176_16249_1514523759}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（链路本地地址）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_x1176_16249_x368007509}[显示公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[PIM]{lang="SV"}[详细信息。]{style="font-family:宋体"}

[]{#_Toc94588264}[]{#_Toc80176803}[]{#struct_0_x1176_16249_x1625942765}[]{#_Toc87787227}[]{#_Toc87852106}[]{#_Toc87852885}[]{#_Toc87853666}[]{#_Toc87867705}[]{#_Toc87787243}[]{#_Toc87852122}[]{#_Toc87852901}[]{#_Toc87853682}[]{#_Toc87867721}[\<Sysname\> display ipv6 pim interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}

[ ]{lang="EN-US"}[Interface]{lang="DE"}[：]{style="font-family:宋体"} [GigabitEthernet1/0/1, FE80::200:5EFF:FE04:8700]{lang="DE"}

[     PIM version: 2]{lang="DE"}

[     PIM mode: Sparse]{lang="DE"}

[     PIM DR: FE80::200:AFF:FE01:101]{lang="DE"}

[     ]{lang="DE"}[PIM DR Priority (configured): 1]{lang="EN-US"}

[     PIM neighbors count: 1]{lang="EN-US"}

[     PIM hello interval: 30 s]{lang="EN-US"}

[     PIM LAN delay (negotiated): 500 ms]{lang="EN-US"}

[     PIM LAN delay (configured): 500 ms]{lang="EN-US"}

[     PIM override interval (negotiated): 2500 ms]{lang="EN-US"}

[     PIM override interval (configured): 2500 ms]{lang="EN-US"}

[     PIM neighbor tracking (negotiated): disabled]{lang="EN-US"}

[     PIM neighbor tracking (configured): disabled]{lang="EN-US"}

[     PIM generation ID: 0xF5712241]{lang="EN-US"}

[     PIM require generation ID: disabled]{lang="EN-US"}

[     PIM hello hold interval: 105 s]{lang="EN-US"}

[     PIM assert hold interval: 180 s]{lang="EN-US"}

[     PIM triggered hello delay: 5 s]{lang="EN-US"}

[     PIM J/P interval: 60 s]{lang="EN-US"}

[     PIM J/P hold interval: 210 s]{lang="EN-US"}

[     PIM BSR domain border: disabled]{lang="EN-US"}

[     PIM BFD: disabled]{lang="EN-US"}

[     Number of routers on network not using DR priority: 0]{lang="EN-US"}

[     Number of routers on network not using LAN delay: 0]{lang="EN-US"}

[     Number of routers on network not using neighbor tracking: 2]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ipv6 pim interface verbose]{lang="EN-US"}]{#struct_0_x1176_16249_365208446}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1636002463}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1625877229}

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_1323806532}

[[Interface]{lang="EN-US"}]{#struct_0_x1176_16249_1429817763}

[[接口名称与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_x84558269}[地址（链路本地地址）]{style="font-family:宋体"}

[[PIM version]{lang="EN-US"}]{#struct_0_x1176_16249_709568514}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1869913038}[协议的版本号]{style="font-family:宋体"}

[[PIM mode]{lang="EN-US"}]{#struct_0_x1176_16249_x1626467052}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1893884369}[协议的模式，是密集模式还是稀疏模式]{style="font-family:宋体"}

[[PIM DR]{lang="EN-US"}]{#struct_0_x1176_16249_663489858}

[[DR]{lang="EN-US"}]{#struct_0_x1176_16249_x270164627}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（链路本地地址）]{style="font-family:宋体"}

[[PIM DR Priority (configured)]{lang="EN-US"}]{#struct_0_x1176_16249_942593126}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x1176_16249_x982726802}[优先级的配置值]{style="font-family:宋体"}

[[PIM neighbor count]{lang="EN-US"}]{#struct_0_x1176_16249_x1626401516}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1294224336}[邻居的总数]{style="font-family:宋体"}

[[PIM hello interval]{lang="EN-US"}]{#struct_0_x1176_16249_1743091938}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_x1824999309}[报文的时间间隔]{style="font-family:宋体"}

[[PIM LAN delay (negotiated)]{lang="EN-US"}]{#struct_0_x1176_16249_372561938}

[[剪枝报文传输延迟的协商值]{style="font-family:宋体"}]{#struct_0_x1176_16249_977290506}

[[PIM LAN delay (configured)]{lang="EN-US"}]{#struct_0_x1176_16249_x1626335980}

[[剪枝报文传输延迟的配置值]{style="font-family:宋体"}]{#struct_0_x1176_16249_510921135}

[[PIM override interval (negotiated)]{lang="EN-US"}]{#struct_0_x1176_16249_x2097510466}

[[剪枝否决时间的协商值]{style="font-family:宋体"}]{#struct_0_x1176_16249_x2000023093}

[[PIM override interval (configured)]{lang="EN-US"}]{#struct_0_x1176_16249_504967144}

[[剪枝否决时间的配置值]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1626270444}

[[PIM neighbor tracking (negotiated)]{lang="EN-US"}]{#struct_0_x1176_16249_451897508}

[[邻居跟踪使能与否的协商情况]{style="font-family:宋体"}]{#struct_0_x1176_16249_1269058721}

[[PIM neighbor tracking (configured)]{lang="EN-US"}]{#struct_0_x1176_16249_1857400566}

[[邻居跟踪使能与否的配置情况]{style="font-family:宋体"}]{#struct_0_x1176_16249_x826530677}

[[PIM generation ID]{lang="EN-US"}]{#struct_0_x1176_16249_x1626729196}

[[Generation_ID]{lang="SV"}]{#struct_0_x1176_16249_1462301110}[参数值]{style="font-family:宋体"}

[[PIM require generation ID]{lang="EN-US"}]{#struct_0_x1176_16249_x637548405}

[[是否使能不接受无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_x1176_16249_1235715915}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[PIM hello hold interval]{lang="EN-US"}]{#struct_0_x1176_16249_x1626663660}

[[保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_707638523}[邻居的可达状态的时间]{style="font-family:宋体"}

[[PIM assert hold interval]{lang="EN-US"}]{#struct_0_x1176_16249_673478896}

[[保持断言状态的时间]{style="font-family:宋体"}]{#struct_0_x1176_16249_1553439588}

[[PIM triggered hello delay]{lang="EN-US"}]{#struct_0_x1176_16249_x1626598124}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_254076781}[报文的最大延迟时间]{style="font-family:宋体"}

[[PIM J/P interval]{lang="EN-US"}]{#struct_0_x1176_16249_410578991}

[[发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_x238999362}[剪枝报文的时间间隔]{style="font-family:宋体"}

[[PIM J/P hold interval]{lang="EN-US"}]{#struct_0_x1176_16249_x1626532588}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_x526687021}[剪枝状态的保持时间]{style="font-family:宋体"}

[[PIM BSR domain border]{lang="EN-US"}]{#struct_0_x1176_16249_1022856444}

[[该接口是否配置了]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_1797081510}[的服务边界]{style="font-family:宋体"}

[[PIM BFD]{lang="EN-US"}]{#struct_0_x1176_16249_x1625942764}

[[该接口是否使能了]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1200875495}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能]{style="font-family:宋体"}

[[Number of routers on network not using DR priority]{lang="EN-US"}]{#struct_0_x1176_16249_x1623495339}

[[该接口所在网段上没有使用]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x1176_16249_706532013}[优先级字段的路由器数量]{style="font-family:宋体"}

[[Number of routers on network not using LAN delay]{lang="EN-US"}]{#struct_0_x1176_16249_x1625877228}

[[该接口所在网段上未使用]{style="font-family:宋体"}[LAN-delay]{lang="EN-US"}]{#struct_0_x1176_16249_x1405076823}[字段的路由器数量]{style="font-family:宋体"}

[[Number of routers on network not using neighbor tracking]{lang="EN-US"}]{#struct_0_x1176_16249_2121013394}

[[该接口所在网段上未使能邻居跟踪的路由器数量]{style="font-family:宋体"}]{#struct_0_x1176_16249_735503578}

[]{#_Toc400703937}[[ ]{lang="EN-US"}]{#_Toc398976001}

::: {#431704695 .myid}
[]{#_Toc404790439}[]{#struct_0_x1176_16249_200173636}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim nbma-link**

------------------------------------------------------------------------

[**[display ipv6 pim nbma-link ]{lang="EN-US"}**]{#struct_0_x1176_16249_x560267130}[命令用来显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[模块维护的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口对端的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1908715299}

[**[display ipv6 pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **nbma-link** \[ **interface** { *interface-type interface-number* } \]]{lang="EN-US"}]{#struct_0_x1176_16249_1257430574}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1462819702}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x194415242}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1448311814}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x737624654}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x2051141523}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x150815239}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x1164727289}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_131677202}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_1766257577}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1176_16249_x509770675}[：接口类型和接口编号，显示指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[维护对端的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_769192325}

[[\#]{lang="EN-US"}]{#struct_0_x1176_16249_160358977}[显示公网所有]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[维护的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim nbma-link  ]{lang="EN-US"}]{#struct_0_x1176_16249_1186479286}

[Interface: Tunnel1]{lang="EN-US"}

[  Number of links: 1]{lang="EN-US"}

[    Remote address: FE80::1]{lang="EN-US"}

[      Private index    : 0XCE000000]{lang="EN-US"}

[      Private interface: Multicast-NBMA0]{lang="EN-US"}

[Interface: Tunnel2]{lang="EN-US"}

[  Number of links: 1]{lang="EN-US"}

[    Remote address: FE80::2]{lang="EN-US"}

[      Private index    : 0XCE000001]{lang="EN-US"}

[      Private interface: Multicast-NBMA1]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_x1176_16249_1051281081}[显示公网指定]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[维护的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim nbma-link interface tunnel 1]{lang="EN-US"}]{#struct_0_x1176_16249_x1768378192}

[Interface: Tunnel1]{lang="EN-US"}

[  Number of links: 1]{lang="EN-US"}

[    Remote address: FE80::1]{lang="EN-US"}

[      Private index    : 0XCE000000]{lang="EN-US"}

[  Private interface: Multicast-NBMA0]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ipv6 pim nbma-link]{lang="EN-US"}]{#struct_0_x1176_16249_1613830783}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1700355457}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_x962625778}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_247227803}

[[Interface      ]{lang="EN-US"}]{#struct_0_x1176_16249_1813311744}

[[隧道接口名称]{style="font-family:宋体"}]{#struct_0_x1176_16249_1921618089}

[[Number of links]{lang="EN-US"}]{#struct_0_x1176_16249_603130483}

[[该隧道下的远端连接的个数]{style="font-family:宋体"}]{#struct_0_x1176_16249_x2125752872}

[[Remote address]{lang="EN-US"}]{#struct_0_x1176_16249_x559668931}

[[远端连接的地址]{style="font-family:宋体"}]{#struct_0_x1176_16249_1006415010}

[[Private index]{lang="EN-US"}]{#struct_0_x1176_16249_1015376492}

[[对应远端连接的索引]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1366237985}

[[Private interface]{lang="EN-US"}]{#struct_0_x1176_16249_199845956}

[[对应远端连接的接口]{style="font-family:宋体"}]{#struct_0_x1176_16249_1765929897}

[ ]{lang="EN-US"}

::: {#1729716770 .myid}
[]{#_Toc404790440}[]{#struct_0_x1176_16249_x799882100}[]{#_Toc288743022}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim neighbor**

------------------------------------------------------------------------

[**[display ipv6 pim neighbor]{lang="EN-US"}**]{#struct_0_x1176_16249_1376009586}[命令用来显示]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_380967820}

[**[display ipv6 pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **neighbor** \[ *ipv6-neighbor-address* \| **interface** *interface-type interface-number* \| **verbose** \] \*]{lang="EN-US"}]{#struct_0_x1176_16249_x1428635518}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1444427371}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_332397640}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x527613695}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1292673165}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_735438042}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1121127208}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_1698676518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1556790879}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_787226159}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[*[ipv6-neighbor-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x489970005}[：]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，显示指定]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1176_16249_x383630001}[：接口类型和接口编号，显示指定接口上的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居信息。如果未指定本参数，将显示所有接口上的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1176_16249_x1597684436}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2104055833}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_735634650}[显示公网实例所有]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim neighbor]{lang="EN-US"}]{#struct_0_x1176_16249_265113480}

[ Total Number of Neighbors = 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Neighbor        Interface           Uptime   Expires  DR-Priority Mode]{lang="EN-US"}

[ FE80::A01:101:1 GE1/0/1             02:50:49 00:01:31 1           B]{lang="EN-US"}

[ FE80::A01:102:1 GE1/0/2             02:49:39 00:01:42 1]{lang="EN-US"}

[]{#_Toc116822996}[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_993019330}[显示公网实例中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[FE80::A01:101:1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim neighbor fe80::a01:101:1 verbose]{lang="EN-US"}]{#struct_0_x1176_16249_735569114}

[ Neighbor: FE80::A01:101:1]{lang="EN-US"}

[     Interface: GigabitEthernet1/0/3]{lang="EN-US"}

[     Uptime: 00:00:10]{lang="EN-US"}

[     Expiry time: 00:00:30]{lang="EN-US"}

[     DR Priority: 1]{lang="EN-US"}

[     Generation ID: 0x2ACEFE15]{lang="EN-US"}

[     Holdtime: 105 s]{lang="EN-US"}

[     LAN delay: 500 ms]{lang="EN-US"}

[     Override interval: 2500 ms]{lang="EN-US"}

[     State refresh interval: 60 s]{lang="EN-US"}

[     Neighbor tracking: Disabled]{lang="EN-US"}

[     Bidirectional PIM: Enabled]{lang="EN-US"}

[     Secondary address(es):]{lang="EN-US"}

[     1::1]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display ipv6 pim neighbor]{lang="EN-US"}]{#struct_0_x1176_16249_365729222}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1629275022}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_x210423016}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_1023505611}

[[Total Number of Neighbors]{lang="EN-US"}]{#struct_0_x1176_16249_1009571181}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_2015270890}[邻居的总数]{style="font-family:宋体"}

[[Neighbor]{lang="EN-US"}]{#struct_0_x1176_16249_533723243}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_735765722}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[主地址（链路本地地址）]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1176_16249_x872621526}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x484078044}[邻居所在接口的名称]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_x1176_16249_1905172266}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_278739607}[邻居已存在的时间]{style="font-family:宋体"}

[[Expires/Expiry time]{lang="EN-US"}]{#struct_0_x1176_16249_x162049150}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_735700186}[邻居超时的剩余时间，]{style="font-family:宋体"}[never]{lang="EN-US"}[表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居永不超时，即永远可达]{style="font-family:宋体"}

[[DR-Priority/DR Priority]{lang="EN-US"}]{#struct_0_x1176_16249_226006770}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1571321736}[邻居的优先级]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x1176_16249_x949895029}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1783018499}[邻居的模式，]{style="font-family:宋体"}[B]{lang="EN-US"}[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模式，显示为空则表示非]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[Generation ID]{lang="EN-US"}]{#struct_0_x1176_16249_x1469853038}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_735896794}[邻居的]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[（状态随机数）]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_x1176_16249_x1105339341}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1179992386}[邻居的生存时间，]{style="font-family:宋体"}[forever]{lang="EN-US"}[表示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居永远存在，即永远可达]{style="font-family:宋体"}

[[LAN delay]{lang="EN-US"}]{#struct_0_x1176_16249_1070406942}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x85856223}[报文在共享网段中的传输延迟]{style="font-family:宋体"}

[[Override interval]{lang="EN-US"}]{#struct_0_x1176_16249_735831258}

[[剪枝否决的时间间隔]{style="font-family:宋体"}]{#struct_0_x1176_16249_1648632316}

[[State refresh interval]{lang="EN-US"}]{#struct_0_x1176_16249_659315294}

[[状态刷新的时间间隔，只有当]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1158196844}[邻居工作在]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[模式下且具备状态刷新能力时才会显示本字段]{style="font-family:宋体"}

[[Neighbor tracking]{lang="EN-US"}]{#struct_0_x1176_16249_1751689350}

[[邻居跟踪功能是否使能]{style="font-family:宋体"}]{#struct_0_x1176_16249_736027866}

[[Bidirectional PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1045796146}

[[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_x1342076969}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[是否使能]{style="font-family:宋体"}

[[Secondary address(es)]{lang="EN-US"}]{#struct_0_x1176_16249_99939397}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_735962330}[邻居的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[从地址（非链路本地地址）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1322234931 .myid}
[]{#_Toc404790441}[]{#struct_0_x1176_16249_466267284}[]{#_Toc288743023}[]{#_Toc94588265}[]{#_Toc80176804}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim routing-table**

------------------------------------------------------------------------

[**[display ipv6 pim routing-table]{lang="EN-US"}**]{#struct_0_x1176_16249_x1907414840}[命令用来显示]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[路由表的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_182777670}

[**[display ipv6 pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **routing-table** \[ *ipv6-group-address* \[ *prefix-length* \] \| *ipv6-source-address* \[ *prefix-length* \] \| **flags** *flag-value* \| **fsm** \| **incoming-interface** *interface-type* *interface-number* \| **mode** *mode-type* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \] \*]{lang="EN-US"}]{#struct_0_x1176_16249_893864521}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1015932764}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x282453302}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2115096655}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x140320289}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_735503579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x799882101}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_1376075122}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1999138086}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_x872034112}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x1176_16249_1045943302}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[*[ipv6-source-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x189542892}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，显示包含指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x1176_16249_47209374}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址的前缀长度。对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，其取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[；对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址，其取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[flags]{lang="EN-US"}***[ flag-value]{lang="EN-US"}*]{#struct_0_x1176_16249_x448352548}[：]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[标志，显示包含指定标志的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。如果未指定本参数，将显示包含所有标志的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值及含义如下**：**]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[act]{lang="EN-US"}**]{#struct_0_x1176_16249_735438043}[：表示已经有实际数据到达的]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[del]{lang="EN-US"}**]{#struct_0_x1176_16249_1121127209}[：表示计划删除的]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[exprune]{lang="EN-US"}**]{#struct_0_x1176_16249_1698742054}[：表示某些出接口被其它]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由协议剪枝的]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ext]{lang="EN-US"}**]{#struct_0_x1176_16249_x1162907888}[：表示包含了由其它]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播路由协议提供出接口的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loc]{lang="EN-US"}**]{#struct_0_x1176_16249_x1729708041}[：表示在与]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播源处于同一网段的设备上的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[niif]{lang="EN-US"}**]{#struct_0_x1176_16249_1555581008}[：表示未确定入接口的]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nonbr]{lang="EN-US"}**]{#struct_0_x1176_16249_x1734823982}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居查找失败的]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rpt]{lang="EN-US"}**]{#struct_0_x1176_16249_1103690263}[：表示向]{lang="EN-US" style="font-family:宋体"}[RP]{lang="EN-US"}[方向发送过（]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[G]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}[RPT]{lang="EN-US"}[位剪枝的]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spt]{lang="EN-US"}**]{#struct_0_x1176_16249_x109370462}[：表示]{lang="EN-US" style="font-family:宋体"}[SPT]{lang="EN-US"}[上的]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[swt]{lang="EN-US"}**]{#struct_0_x1176_16249_735634651}[：表示正处于向]{style="font-family:
宋体"}[SPT]{lang="EN-US"}[切换过程中的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wc]{lang="EN-US"}**]{#struct_0_x1176_16249_265113481}[：表示带]{lang="EN-US" style="font-family:宋体"}[WC]{lang="EN-US"}[通配符的]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。]{lang="EN-US" style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x1176_16249_993019331}[：显示有限状态机的详细信息。]{style="font-family:宋体"}

[**[incoming-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1176_16249_1170384800}[：显示指定入接口的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。如果未指定本参数，将显示所有入接口的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[**[mode ]{lang="EN-US"}***[mode-type]{lang="EN-US"}*]{#struct_0_x1176_16249_480708502}[：]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[模式，显示指定模式下的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。如果未指定本参数，将显示所有模式下的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}*[mode-type]{lang="EN-US"}*[的取值及含义如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bidir]{lang="EN-US"}**]{#struct_0_x1176_16249_x1977657876}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[模式；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dm]{lang="EN-US"}**]{#struct_0_x1176_16249_x960503389}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[模式；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sm]{lang="EN-US"}**]{#struct_0_x1176_16249_446856958}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[模式；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ssm]{lang="EN-US"}**]{#struct_0_x1176_16249_x623636825}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM-SSM]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}**[ { **exclude** \| **include** \| **match** } *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1176_16249_735569115}[：显示指定出接口的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。其中，]{style="font-family:宋体"}**[exclude]{lang="EN-US"}**[表示不包含指定接口；]{style="font-family:宋体"}**[include]{lang="EN-US"}**[表示包含指定接口；]{style="font-family:宋体"}**[match]{lang="EN-US"}**[表示包含且仅包含指定接口。如果未指定本参数，将显示所有出接口的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_365729221}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x210423017}[显示公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由表的内容。]{style="font-family:宋体"}

[]{#_Toc94588266}[]{#_Toc80176805}[]{#struct_0_x1176_16249_1023440075}[]{#_Toc87787261}[]{#_Toc87852140}[]{#_Toc87852919}[]{#_Toc87853700}[]{#_Toc87867739}[]{#_Toc87787262}[]{#_Toc87852141}[]{#_Toc87852920}[]{#_Toc87853701}[]{#_Toc87867740}[]{#_Toc87787263}[]{#_Toc87852142}[]{#_Toc87852921}[]{#_Toc87853702}[]{#_Toc87867741}[]{#_Toc87787264}[]{#_Toc87852143}[]{#_Toc87852922}[]{#_Toc87853703}[]{#_Toc87867742}[]{#_Toc87787265}[]{#_Toc87852144}[]{#_Toc87852923}[]{#_Toc87853704}[]{#_Toc87867743}[]{#_Toc87787266}[]{#_Toc87852145}[]{#_Toc87852924}[]{#_Toc87853705}[]{#_Toc87867744}[]{#_Toc87787267}[]{#_Toc87852146}[]{#_Toc87852925}[]{#_Toc87853706}[]{#_Toc87867745}[]{#_Toc87787269}[]{#_Toc87852148}[]{#_Toc87852927}[]{#_Toc87853708}[]{#_Toc87867747}[]{#_Toc87787270}[]{#_Toc87852149}[]{#_Toc87852928}[]{#_Toc87853709}[]{#_Toc87867748}[]{#_Toc87787271}[]{#_Toc87852150}[]{#_Toc87852929}[]{#_Toc87853710}[]{#_Toc87867749}[]{#_Toc87442582}[]{#_Toc87787274}[]{#_Toc87852153}[]{#_Toc87852932}[]{#_Toc87853713}[]{#_Toc87867752}[]{#_Toc87442589}[]{#_Toc87787281}[]{#_Toc87852160}[]{#_Toc87852939}[]{#_Toc87853720}[]{#_Toc87867759}[]{#_Toc87442596}[]{#_Toc87787288}[]{#_Toc87852167}[]{#_Toc87852946}[]{#_Toc87853727}[]{#_Toc87867766}[\<Sysname\> display ipv6 pim routing-table]{lang="EN-US"}

[ Total 0 (\*, G) entry; 1 (S, G) entry]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (2001::2, FFE3::101)]{lang="EN-US"}

[     RP: FE80::A01:100:1]{lang="EN-US"}

[     Protocol: pim-sm, Flag: SPT LOC ACT]{lang="EN-US"}

[     UpTime: 02:54:43]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[         Upstream neighbor: NULL]{lang="EN-US"}

[         RPF prime neighbor: NULL]{lang="EN-US"}

[     Downstream interface information:]{lang="EN-US"}

[     Total number of downstream interfaces: 1]{lang="EN-US"}

[         1: GigabitEthernet1/0/2]{lang="EN-US"}

[             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47]{lang="EN-US"}

[]{#_Toc116822997}[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_215036761}[显示公网实例]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由表的状态机信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim routing-table fsm]{lang="EN-US"}]{#struct_0_x1176_16249_735765723}

[ Total 0 (\*, G) entries; 1 (S, G) entries]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Abbreviations for FSM states:]{lang="EN-US"}

[     NI - no info, J - joined, NJ - not joined, P - pruned,]{lang="EN-US"}

[     NP - not pruned, PP - prune pending, W - winner, L - loser,]{lang="EN-US"}

[     F - forwarding, AP - ack pending, DR - designated router,]{lang="EN-US"}

[     NDR - non-designated router, RCV - downstream receivers]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (2001::2, FFE3::101)]{lang="EN-US"}

[     RP: FE80::A01:100:1]{lang="EN-US"}

[     Protocol: pim-sm, Flag: SPT LOC ACT]{lang="EN-US"}

[     UpTime: 02:54:43]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[         Upstream neighbor: NULL]{lang="EN-US"}

[         RPF prime neighbor: NULL]{lang="EN-US"}

[         Join/Prune FSM: \[SPT: J\] \[RPT: NP\]]{lang="EN-US"}

[     Downstream interface information:]{lang="EN-US"}

[     Total number of downstream interfaces: 1]{lang="EN-US"}

[         1: GigabitEthernet1/0/2]{lang="EN-US"}

[             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47]{lang="EN-US"}

[             DR state: \[DR\]]{lang="EN-US"}

[             Join/Prune FSM: \[NI\]]{lang="EN-US"}

[             Assert FSM: \[NI\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[     FSM information for non-downstream interfaces: None]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1006349474}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[应用组网]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由表的内容。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim routing-table]{lang="EN-US"}]{#struct_0_x1176_16249_x196199041}

[ Total 0 (\*, G) entries; 1 (S, G) entries]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (2001::2, FFE3::101)]{lang="EN-US"}

[     RP: FE80::A01:100:1]{lang="EN-US"}

[     Protocol: pim-sm, Flag: SPT LOC ACT]{lang="EN-US"}

[     UpTime: 02:54:43]{lang="EN-US"}

[     Upstream interface: Tunnel0, FE80::20:11]{lang="EN-US"}

[         Upstream neighbor: FE80::1]{lang="EN-US"}

[         RPF prime neighbor: FE80::1]{lang="EN-US"}

[     Downstream interface information:]{lang="EN-US"}

[     Total number of downstream interfaces: 1]{lang="EN-US"}

[         1: Tunnel0, FE80::20:12]{lang="EN-US"}

[             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_797445163}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[应用组网]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[路由表的状态机信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim routing-table fsm]{lang="EN-US"}]{#struct_0_x1176_16249_x1366303521}

[ Total 0 (\*, G) entries; 1 (S, G) entries]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Abbreviations for FSM states:]{lang="EN-US"}

[     NI - no info, J - joined, NJ - not joined, P - pruned,]{lang="EN-US"}

[     NP - not pruned, PP - prune pending, W - winner, L - loser,]{lang="EN-US"}

[     F - forwarding, AP - ack pending, DR - designated router,]{lang="EN-US"}

[     NDR - non-designated router, RCV - downstream receivers]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (2001::2, FFE3::101)]{lang="EN-US"}

[     RP: FE80::A01:100:1]{lang="EN-US"}

[     Protocol: pim-sm, Flag: SPT LOC ACT]{lang="EN-US"}

[     UpTime: 02:54:43]{lang="EN-US"}

[     Upstream interface: Tunnel0, FE80::20:11]{lang="EN-US"}

[         Upstream neighbor: FE80::1]{lang="EN-US"}

[         RPF prime neighbor: FE80::1]{lang="EN-US"}

[         Join/Prune FSM: \[SPT: J\] \[RPT: NP\]]{lang="EN-US"}

[     Downstream interface information:]{lang="EN-US"}

[     Total number of downstream interfaces: 1]{lang="EN-US"}

[         1: Tunnel0, FE80::20:12]{lang="EN-US"}

[            Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47]{lang="EN-US"}

[            DR state: \[DR\]]{lang="EN-US"}

[            Join/Prune FSM: \[NI\]]{lang="EN-US"}

[            Assert FSM: \[NI\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[     FSM information for non-downstream interfaces: None]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ipv6 pim routing-table]{lang="EN-US"}]{#struct_0_x1176_16249_x872621527}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1657509555}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_735700187}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_226006769}

[[Total 0 (\*, G) entries; 1 (S, G) entries]{lang="EN-US"}]{#struct_0_x1176_16249_x767330431}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1218502401}[路由表中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）与（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的总数]{style="font-family:宋体"}

[[Abbreviations for FSM states:]{lang="EN-US"}]{#struct_0_x1176_16249_277952814}

[[NI - no info, J - joined, NJ - not joined, P -- pruned]{lang="EN-US"}]{#struct_0_x1176_16249_x1243380780}

[[NP - not pruned, PP - prune pending, W - winner, L -- loser]{lang="EN-US"}]{#struct_0_x1176_16249_x1746015033}

[[F - forwarding, AP - ack pending, DR - designated router]{lang="EN-US"}]{#struct_0_x1176_16249_735896795}

[[NDR - non-designated router, RCV - downstream receivers]{lang="EN-US"}]{#struct_0_x1176_16249_x1105339340}

[[状态机的缩写：]{style="font-family:宋体"}[NI]{lang="EN-US"}]{#struct_0_x1176_16249_x386091555}[表示初始状态，]{style="font-family:宋体"}[J]{lang="EN-US"}[表示加入状态，]{style="font-family:宋体"}[P]{lang="EN-US"}[表示剪枝状态，]{style="font-family:宋体"}[NP]{lang="EN-US"}[表示未剪枝状态，]{style="font-family:宋体"}[PP]{lang="EN-US"}[表示剪枝未决状态，]{style="font-family:宋体"}[W]{lang="EN-US"}[表示断言当选，]{style="font-family:宋体"}[L]{lang="EN-US"}[表示断言落选，]{style="font-family:宋体"}[F]{lang="EN-US"}[表示转发状态，]{style="font-family:宋体"}[AP]{lang="EN-US"}[表示嫁接确认状态，]{style="font-family:宋体"}[DR]{lang="EN-US"}[表示指定路由器，]{style="font-family:宋体"}[NDR]{lang="EN-US"}[表示非指定路由器，]{style="font-family:宋体"}[RCV]{lang="EN-US"}[表示下游接收者]{style="font-family:宋体"}

[[(2001::2, FFE3::101)]{lang="EN-US"}]{#struct_0_x1176_16249_x320030564}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_382730354}[路由表中的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_735831259}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_1648632317}[的地址]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1176_16249_659380830}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_788895575}[的模式]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_x1176_16249_1558488537}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1288648345}[路由表中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACT]{lang="EN-US"}]{#struct_0_x1176_16249_736027867}[：表示已有实际数据到达]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEL]{lang="EN-US"}]{#struct_0_x1176_16249_1045796145}[：表示计划要删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EXPRUNE]{lang="EN-US"}]{#struct_0_x1176_16249_x1342142505}[：表示某些出接口被其它]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由协议剪枝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EXT]{lang="EN-US"}]{#struct_0_x1176_16249_696268672}[：表示包含了由其它]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由协议提供的出接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LOC]{lang="EN-US"}]{#struct_0_x1176_16249_331215041}[：表示与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源处于同一网段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NIIF]{lang="EN-US"}]{#struct_0_x1176_16249_735962331}[：表示未确定入接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONBR]{lang="EN-US"}]{#struct_0_x1176_16249_466267283}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居查找失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RPT]{lang="EN-US"}]{#struct_0_x1176_16249_x1907414847}[：表示向]{lang="EN-US" style="font-family:宋体"}[RP]{lang="EN-US"}[方向发送过（]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[G]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}[RPT]{lang="EN-US"}[位剪枝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPT]{lang="EN-US"}]{#struct_0_x1176_16249_586062197}[：表示在]{lang="EN-US" style="font-family:宋体"}[SPT]{lang="EN-US"}[上]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SWT]{lang="EN-US"}]{#struct_0_x1176_16249_x1654933462}[：表示正在向]{lang="EN-US" style="font-family:宋体"}[SPT]{lang="EN-US"}[切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WC]{lang="EN-US"}]{#struct_0_x1176_16249_735503576}[：表示带]{style="font-family:宋体"}[WC]{lang="EN-US"}[通配符]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_x1176_16249_x799882106}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1176_16249_1375878514}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项已存在的时间]{style="font-family:宋体"}

[[Upstream interface]{lang="EN-US"}]{#struct_0_x1176_16249_x1053389018}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1176_16249_735438040}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的入接口，使能了]{style="font-family:宋体"}[nbma]{lang="EN-US"}[模式的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道口，显示远端连接]{style="font-family:宋体"}[IPv6 link-local]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Upstream neighbor]{lang="EN-US"}]{#struct_0_x1176_16249_1121127210}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1176_16249_1699200807}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游邻居]{style="font-family:宋体"}

[[RPF prime neighbor]{lang="EN-US"}]{#struct_0_x1176_16249_x1990829842}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1176_16249_735634648}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[邻居：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对（]{style="font-family:宋体"}]{#struct_0_x1176_16249_x2073538672}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项来说，当该路由器是]{style="font-family:宋体"}[RP]{lang="EN-US"}[时，（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[邻居是]{style="font-family:宋体"}[NULL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对（]{style="font-family:宋体"}]{#struct_0_x1176_16249_2034506446}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项来说，当该路由器直连源时，（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[邻居是]{style="font-family:宋体"}[NULL]{lang="EN-US"}

[[DR state]{lang="EN-US"}]{#struct_0_x1176_16249_613752715}

[[DR]{lang="EN-US"}]{#struct_0_x1176_16249_735569112}[的状态]{style="font-family:宋体"}

[[Join/Prune FSM]{lang="EN-US"}]{#struct_0_x1176_16249_365729228}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_x210423010}[剪枝状态机]{style="font-family:宋体"}

[[Assert FSM]{lang="EN-US"}]{#struct_0_x1176_16249_1023374539}

[[断言状态机]{style="font-family:宋体"}]{#struct_0_x1176_16249_735765720}

[[Downstream interface information]{lang="EN-US"}]{#struct_0_x1176_16249_x872621528}

[[下游接口的信息，包括：]{style="font-family:宋体"}]{#struct_0_x1176_16249_x483946972}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的总数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_78392960}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的名称]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_735700184}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口使用的协议类型]{style="font-family:宋体"}]{#struct_0_x1176_16249_226006772}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的存在时间]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_1571321738}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的超时时间]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_735896792}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口（]{lang="EN-US" style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_x1176_16249_x963018994}[隧道口）对应的隧道远端的]{lang="EN-US" style="font-family:宋体"}[IPv6 link-local]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[FSM information for non-downstream interfaces]{lang="EN-US"}]{#struct_0_x1176_16249_x1105339335}

[[非下游接口的状态机信息]{style="font-family:宋体"}]{#struct_0_x1176_16249_x789834834}

[ ]{lang="EN-US"}

::: {#-157723509 .myid}
[]{#_Toc404790442}[]{#struct_0_x1176_16249_x1189210148}[]{#_Toc288743024}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim rp-info**

------------------------------------------------------------------------

[**[display ipv6 pim rp-info]{lang="EN-US"}**]{#struct_0_x1176_16249_2053663537}[命令用来显示]{style="font-family:
宋体"}[IPv6 PIM-SM]{lang="EN-US"}[域中的]{style="font-family:
宋体"}[RP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_735831256}

[**[display ipv6 pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **rp-info** \[ *ipv6-group-address* \]]{lang="EN-US"}]{#struct_0_x1176_16249_1648632310}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_658922078}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_979130802}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1195585027}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1865523168}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_1971826932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_606072738}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_x1816238731}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_736027864}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_1045796144}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[ipv6-group-address]{lang="EN-US"}*]{#struct_0_x1176_16249_x1342208041}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址，显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组所对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息，取值范围为]{style="font-family:宋体"}[FFxy::/16]{lang="EN-US"}[（但不包括下列地址：]{style="font-family:宋体"}[FFx0::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx1::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[FFx2::/16]{lang="EN-US"}[和]{style="font-family:宋体"}[FF0y::]{lang="EN-US"}[），其中]{style="font-family:宋体"}[x]{lang="EN-US"}[和]{style="font-family:宋体"}[y]{lang="EN-US"}[均代表]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[F]{lang="EN-US"}[的任意一个十六进制数。如果未指定本参数，将显示所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播组对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1023989283}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1915465049}[显示公网实例中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF0E::101]{lang="EN-US"}[所对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[]{#_Toc94588267}[]{#_Toc78346652}[]{#struct_0_x1176_16249_210680768}[]{#_Toc87787291}[]{#_Toc87852170}[]{#_Toc87852949}[]{#_Toc87853730}[]{#_Toc87867769}[]{#_Toc87787293}[]{#_Toc87852172}[]{#_Toc87852951}[]{#_Toc87853732}[]{#_Toc87867771}[\<Sysname\> display ipv6 pim rp-info ff0e::101]{lang="EN-US"}

[ BSR RP address is: 7:12::1]{lang="EN-US"}

[     Priority: 192]{lang="EN-US"}

[     HoldTime: 180]{lang="EN-US"}

[     Uptime: 03:01:10]{lang="EN-US"}

[     Expires: 00:02:30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Static RP address is: 7:12::1]{lang="EN-US"}

[     Preferred: No]{lang="EN-US"}

[     Configured ACL: 2003]{lang="EN-US"}

[ ]{lang="EN-US"}

[ RP mapping for this group is: 7:12::1 (local host)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Anycast-RP 7:12::1 members:]{lang="EN-US"}

[     Member address           State]{lang="EN-US"}

[     1:1::1                   Active]{lang="EN-US"}

[     1:1::2                   Local]{lang="EN-US"}

[     1:2::1                   Remote]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_735962328}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim rp-info]{lang="EN-US"}]{#struct_0_x1176_16249_x1490047860}

[ ]{lang="EN-US"}[BSR RP information:]{lang="IT"}

[   Scope: non-scoped]{lang="IT"}

[     ]{lang="IT"}[Group/MaskLen: FF00::/8]{lang="EN-US"}

[       RP address               Priority  HoldTime  Uptime    Expires]{lang="EN-US"}

[       8:12::2 (local)          192       180       03:01:36  00:02:29]{lang="EN-US"}

[     Group/MaskLen: FF23::/92 \[B\]]{lang="EN-US"}

[       RP address               Priority  HoldTime  Uptime    Expires]{lang="EN-US"}

[       7:12::1 (local)          192       180       00:00:39  00:02:57]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Static RP information:]{lang="EN-US"}

[       RP address               ACL   Mode    Preferred]{lang="EN-US"}

[       3:3::1                   2000  pim-sm  No]{lang="EN-US"}

[       3:3::2                   2001  bidir   Yes]{lang="EN-US"}

[       3:3::3                   2002  pim-sm  No]{lang="EN-US"}

[       3:3::4                         pim-sm  No]{lang="EN-US"}

[       3:3::5                   2002  pim-sm  Yes]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Anycast-RP information:]{lang="EN-US"}

[       RP address               Member address           State]{lang="EN-US"}

[       3:3::1                   1:1::1                   Active]{lang="EN-US"}

[       3:3::1                   1:1::2                   Local]{lang="EN-US"}

[       3:3::1                   1:2::1                   Remote]{lang="EN-US"}

[]{#_Toc116822999}[]{#_Toc116823000}[[表1-9 ]{lang="EN-US"}[display ipv6 pim rp-info]{lang="EN-US"}]{#struct_0_x1176_16249_x1763402969}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1655902373}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_1922051616}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_735503577}

[[BSR RP address is]{lang="EN-US"}]{#struct_0_x1176_16249_x799882107}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_1375944050}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[BSR RP information]{lang="EN-US"}]{#struct_0_x1176_16249_x1082128815}

[[BSR RP]{lang="EN-US"}]{#struct_0_x1176_16249_1717758916}[信息]{style="font-family:宋体"}

[[Scope]{lang="EN-US"}]{#struct_0_x1176_16249_1241491866}

[[域]{style="font-family:宋体"}]{#struct_0_x1176_16249_735438041}

[[Group/MaskLen]{lang="EN-US"}]{#struct_0_x1176_16249_1121127211}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_1699266343}[所服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}

[[\[B\]]{lang="EN-US"}]{#struct_0_x1176_16249_x5750232}

[[表示]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_x1176_16249_x369977255}[服务于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果不显示该字段，则表示]{style="font-family:宋体"}[RP]{lang="EN-US"}[服务于]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}

[[RP address]{lang="EN-US"}]{#struct_0_x1176_16249_x1551674909}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_735634649}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示本地地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x1176_16249_x1465228184}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_1022620402}[的优先级]{style="font-family:宋体"}

[[HoldTime]{lang="EN-US"}]{#struct_0_x1176_16249_735569113}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_365729227}[的超时时间]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_x1176_16249_x210423019}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_1022784715}[已存在的时间]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_x1176_16249_x946380524}

[[RP]{lang="EN-US"}]{#struct_0_x1176_16249_735765721}[超时的剩余时间]{style="font-family:宋体"}

[[Static RP information]{lang="EN-US"}]{#struct_0_x1176_16249_x872621529}

[[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_x1176_16249_x484012508}[信息]{style="font-family:宋体"}

[[Static RP address is/RP address]{lang="EN-US"}]{#struct_0_x1176_16249_x98149680}

[[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_x1176_16249_x1564791264}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Preferred]{lang="EN-US"}]{#struct_0_x1176_16249_735700185}

[[是否指定了静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_x1176_16249_226006771}[优先]{style="font-family:宋体"}

[[Configured ACL/ACL]{lang="EN-US"}]{#struct_0_x1176_16249_1571321737}

[[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_x1176_16249_x949829493}[所服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组列表]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x1176_16249_735896793}

[[为]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}]{#struct_0_x1176_16249_x1105339334}[服务还是为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[服务]{style="font-family:宋体"}

[[RP mapping for this group]{lang="EN-US"}]{#struct_0_x1176_16249_1939048521}

[[服务于当前组播组的]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_x1176_16249_193706485}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Anycast-RP 7:12::1 members]{lang="EN-US"}]{#struct_0_x1176_16249_1461391371}

[[Anycast-RP 7:12::1]{lang="EN-US"}]{#struct_0_x1176_16249_1461194763}[的成员]{style="font-family:宋体"}

[[Member address]{lang="EN-US"}]{#struct_0_x1176_16249_x1308416485}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_x1176_16249_1461260299}[成员的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1176_16249_x507816955}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_x1176_16249_1461587979}[成员地址的来源：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1176_16249_1431208801}[：表示]{lang="EN-US" style="font-family:宋体"}[本端激活接口的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_x1176_16249_1461653515}[：表示本端未激活接口的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote]{lang="EN-US"}]{#struct_0_x1176_16249_x99110566}[：表示远端的地址]{style="font-family:宋体"}

[[Anycast-RP information]{lang="EN-US"}]{#struct_0_x1176_16249_x467607597}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_x1176_16249_x1272032822}[信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2123818409 .myid}
[]{#_Toc288743025}[]{#_Toc94588274}[]{#_Toc80176807}[]{#_Toc311538860}[]{#_Toc404790443}[]{#struct_0_x1176_16249_1551778482}[]{#_Toc139255976}[]{#_Toc139259818}[]{#_Toc139267740}[]{#_Toc139269160}[]{#_Toc139366392}[]{#_Toc139448238}[]{#_Toc139255979}[]{#_Toc139259821}[]{#_Toc139267743}[]{#_Toc139269163}[]{#_Toc139366395}[]{#_Toc139448241}[]{#_Toc139255980}[]{#_Toc139259822}[]{#_Toc139267744}[]{#_Toc139269164}[]{#_Toc139366396}[]{#_Toc139448242}[]{#_Toc139255981}[]{#_Toc139259823}[]{#_Toc139267745}[]{#_Toc139269165}[]{#_Toc139366397}[]{#_Toc139448243}[]{#_Toc139255982}[]{#_Toc139259824}[]{#_Toc139267746}[]{#_Toc139269166}[]{#_Toc139366398}[]{#_Toc139448244}[]{#_Toc139255983}[]{#_Toc139259825}[]{#_Toc139267747}[]{#_Toc139269167}[]{#_Toc139366399}[]{#_Toc139448245}[]{#_Toc139255984}[]{#_Toc139259826}[]{#_Toc139267748}[]{#_Toc139269168}[]{#_Toc139366400}[]{#_Toc139448246}[]{#_Toc139255985}[]{#_Toc139259827}[]{#_Toc139267749}[]{#_Toc139269169}[]{#_Toc139366401}[]{#_Toc139448247}[]{#_Toc139255986}[]{#_Toc139259828}[]{#_Toc139267750}[]{#_Toc139269170}[]{#_Toc139366402}[]{#_Toc139448248}[]{#_Toc139255987}[]{#_Toc139259829}[]{#_Toc139267751}[]{#_Toc139269171}[]{#_Toc139366403}[]{#_Toc139448249}[]{#_Toc139255988}[]{#_Toc139259830}[]{#_Toc139267752}[]{#_Toc139269172}[]{#_Toc139366404}[]{#_Toc139448250}[]{#_Toc139255989}[]{#_Toc139259831}[]{#_Toc139267753}[]{#_Toc139269173}[]{#_Toc139366405}[]{#_Toc139448251}[]{#_Toc139255990}[]{#_Toc139259832}[]{#_Toc139267754}[]{#_Toc139269174}[]{#_Toc139366406}[]{#_Toc139448252}[]{#_Toc87787305}[]{#_Toc87852184}[]{#_Toc87852963}[]{#_Toc87853744}[]{#_Toc87867800}[]{#_Toc87787306}[]{#_Toc87852185}[]{#_Toc87852964}[]{#_Toc87853745}[]{#_Toc87867801}[]{#_Toc87787307}[]{#_Toc87852186}[]{#_Toc87852965}[]{#_Toc87853746}[]{#_Toc87867802}[]{#_Toc87787308}[]{#_Toc87852187}[]{#_Toc87852966}[]{#_Toc87853747}[]{#_Toc87867803}[]{#_Toc87787309}[]{#_Toc87852188}[]{#_Toc87852967}[]{#_Toc87853748}[]{#_Toc87867804}[]{#_Toc87787310}[]{#_Toc87852189}[]{#_Toc87852968}[]{#_Toc87853749}[]{#_Toc87867805}[]{#_Toc87787311}[]{#_Toc87852190}[]{#_Toc87852969}[]{#_Toc87853750}[]{#_Toc87867806}[]{#_Toc87787312}[]{#_Toc87852191}[]{#_Toc87852970}[]{#_Toc87853751}[]{#_Toc87867807}[]{#_Toc87787313}[]{#_Toc87852192}[]{#_Toc87852971}[]{#_Toc87853752}[]{#_Toc87867808}[]{#_Toc87787314}[]{#_Toc87852193}[]{#_Toc87852972}[]{#_Toc87853753}[]{#_Toc87867809}[]{#_Toc87787315}[]{#_Toc87852194}[]{#_Toc87852973}[]{#_Toc87853754}[]{#_Toc87867810}[]{#_Toc87787318}[]{#_Toc87852197}[]{#_Toc87852976}[]{#_Toc87853757}[]{#_Toc87867813}[]{#_Toc87787319}[]{#_Toc87852198}[]{#_Toc87852977}[]{#_Toc87853758}[]{#_Toc87867814}[]{#_Toc87787320}[]{#_Toc87852199}[]{#_Toc87852978}[]{#_Toc87853759}[]{#_Toc87867815}[]{#_Toc87787321}[]{#_Toc87852200}[]{#_Toc87852979}[]{#_Toc87853760}[]{#_Toc87867816}[]{#_Toc87787322}[]{#_Toc87852201}[]{#_Toc87852980}[]{#_Toc87853761}[]{#_Toc87867817}[]{#_Toc87787323}[]{#_Toc87852202}[]{#_Toc87852981}[]{#_Toc87853762}[]{#_Toc87867818}[]{#_Toc87787324}[]{#_Toc87852203}[]{#_Toc87852982}[]{#_Toc87853763}[]{#_Toc87867819}[]{#_Toc87787326}[]{#_Toc87852205}[]{#_Toc87852984}[]{#_Toc87853765}[]{#_Toc87867821}[]{#_Toc87787327}[]{#_Toc87852206}[]{#_Toc87852985}[]{#_Toc87853766}[]{#_Toc87867822}[]{#_Toc87787328}[]{#_Toc87852207}[]{#_Toc87852986}[]{#_Toc87853767}[]{#_Toc87867823}[]{#_Toc87787329}[]{#_Toc87852208}[]{#_Toc87852987}[]{#_Toc87853768}[]{#_Toc87867824}[]{#_Toc87787330}[]{#_Toc87852209}[]{#_Toc87852988}[]{#_Toc87853769}[]{#_Toc87867825}[]{#_Toc87787331}[]{#_Toc87852210}[]{#_Toc87852989}[]{#_Toc87853770}[]{#_Toc87867826}[]{#_Toc87787332}[]{#_Toc87852211}[]{#_Toc87852990}[]{#_Toc87853771}[]{#_Toc87867827}[]{#_Toc87787334}[]{#_Toc87852213}[]{#_Toc87852992}[]{#_Toc87853773}[]{#_Toc87867829}[]{#_Toc87787335}[]{#_Toc87852214}[]{#_Toc87852993}[]{#_Toc87853774}[]{#_Toc87867830}[]{#_Toc87787336}[]{#_Toc87852215}[]{#_Toc87852994}[]{#_Toc87853775}[]{#_Toc87867831}[]{#_Toc87787337}[]{#_Toc87852216}[]{#_Toc87852995}[]{#_Toc87853776}[]{#_Toc87867832}[]{#_Toc87787338}[]{#_Toc87852217}[]{#_Toc87852996}[]{#_Toc87853777}[]{#_Toc87867833}[]{#_Toc87787339}[]{#_Toc87852218}[]{#_Toc87852997}[]{#_Toc87853778}[]{#_Toc87867834}[]{#_Toc87442607}[]{#_Toc87787340}[]{#_Toc87852219}[]{#_Toc87852998}[]{#_Toc87853779}[]{#_Toc87867835}[]{#_Toc87442610}[]{#_Toc87787343}[]{#_Toc87852222}[]{#_Toc87853001}[]{#_Toc87853782}[]{#_Toc87867838}[]{#_Toc87442614}[]{#_Toc87787347}[]{#_Toc87852226}[]{#_Toc87853005}[]{#_Toc87853786}[]{#_Toc87867842}[]{#_Toc87442623}[]{#_Toc87787356}[]{#_Toc87852235}[]{#_Toc87853014}[]{#_Toc87853795}[]{#_Toc87867851}[]{#_Toc87442624}[]{#_Toc87787357}[]{#_Toc87852236}[]{#_Toc87853015}[]{#_Toc87853796}[]{#_Toc87867852}[]{#_Toc87442625}[]{#_Toc87787358}[]{#_Toc87852237}[]{#_Toc87853016}[]{#_Toc87853797}[]{#_Toc87867853}[]{#_Toc87442626}[]{#_Toc87787359}[]{#_Toc87852238}[]{#_Toc87853017}[]{#_Toc87853798}[]{#_Toc87867854}[]{#_Toc87442627}[]{#_Toc87787360}[]{#_Toc87852239}[]{#_Toc87853018}[]{#_Toc87853799}[]{#_Toc87867855}[]{#_Toc87442628}[]{#_Toc87787361}[]{#_Toc87852240}[]{#_Toc87853019}[]{#_Toc87853800}[]{#_Toc87867856}[]{#_Toc87442629}[]{#_Toc87787362}[]{#_Toc87852241}[]{#_Toc87853020}[]{#_Toc87853801}[]{#_Toc87867857}[]{#_Toc87442630}[]{#_Toc87787363}[]{#_Toc87852242}[]{#_Toc87853021}[]{#_Toc87853802}[]{#_Toc87867858}[]{#_Toc87442631}[]{#_Toc87787364}[]{#_Toc87852243}[]{#_Toc87853022}[]{#_Toc87853803}[]{#_Toc87867859}[]{#_Toc87442632}[]{#_Toc87787365}[]{#_Toc87852244}[]{#_Toc87853023}[]{#_Toc87853804}[]{#_Toc87867860}[]{#_Toc87442633}[]{#_Toc87787366}[]{#_Toc87852245}[]{#_Toc87853024}[]{#_Toc87853805}[]{#_Toc87867861}[]{#_Toc87442634}[]{#_Toc87787367}[]{#_Toc87852246}[]{#_Toc87853025}[]{#_Toc87853806}[]{#_Toc87867862}[]{#_Toc87442635}[]{#_Toc87787368}[]{#_Toc87852247}[]{#_Toc87853026}[]{#_Toc87853807}[]{#_Toc87867863}[]{#_Toc87442636}[]{#_Toc87787369}[]{#_Toc87852248}[]{#_Toc87853027}[]{#_Toc87853808}[]{#_Toc87867864}[]{#_Toc87442637}[]{#_Toc87787370}[]{#_Toc87852249}[]{#_Toc87853028}[]{#_Toc87853809}[]{#_Toc87867865}[]{#_Toc87442638}[]{#_Toc87787371}[]{#_Toc87852250}[]{#_Toc87853029}[]{#_Toc87853810}[]{#_Toc87867866}[]{#_Toc87442639}[]{#_Toc87787372}[]{#_Toc87852251}[]{#_Toc87853030}[]{#_Toc87853811}[]{#_Toc87867867}[]{#_Toc87442640}[]{#_Toc87787373}[]{#_Toc87852252}[]{#_Toc87853031}[]{#_Toc87853812}[]{#_Toc87867868}[]{#_Toc87442641}[]{#_Toc87787374}[]{#_Toc87852253}[]{#_Toc87853032}[]{#_Toc87853813}[]{#_Toc87867869}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- display ipv6 pim statistics**

------------------------------------------------------------------------

[**[display ipv6 pim statistics]{lang="EN-US"}**]{#struct_0_x1176_16249_735831257}[命令用来显示]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[协议报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1648632311}

[**[display ipv6 pim]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_x1176_16249_658987614}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1764211666}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1607434880}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_392432017}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1955386632}

[[network-operator]{lang="EN-US"}]{#struct_0_x1176_16249_555708742}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_736027865}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1176_16249_1045796143}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1341749289}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x251220250}[显示]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[协议报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 pim statistics]{lang="EN-US"}]{#struct_0_x1176_16249_1221784034}

[ Received PIM packets: 3295]{lang="EN-US"}

[ Sent PIM packets    : 5975]{lang="EN-US"}

[                Valid       Invalid        Succeeded   Failed]{lang="EN-US"}

[     Hello    : 3128        0              4333        0]{lang="EN-US"}

[     Reg      : 14          0              0           0]{lang="EN-US"}

[     Reg-stop : 0           0              0           0]{lang="EN-US"}

[     JP       : 151         0              561         0]{lang="EN-US"}

[     BSM      : 0           0              1081        0]{lang="EN-US"}

[     Assert   : 0           0              0           0]{lang="EN-US"}

[     Graft    : 0           0              0           0]{lang="EN-US"}

[     Graft-ACK: 0           0              0           0]{lang="EN-US"}

[     C-RP     : 0           0              0           0]{lang="EN-US"}

[     SRM      : 0           0              0           0]{lang="EN-US"}

[     DF       : 0           0              0           0]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display ipv6 pim statistics]{lang="EN-US"}]{#struct_0_x1176_16249_735962329}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1650896644}[[字段]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1490047861}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1176_16249_x197319028}

[[Received PIM packets]{lang="EN-US"}]{#struct_0_x1176_16249_1598295123}

[[收到的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1837807293}[协议报文总数]{style="font-family:宋体"}

[[Sent PIM packets]{lang="EN-US"}]{#struct_0_x1176_16249_x1715227063}

[[发出的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x688230772}[协议报文总数]{style="font-family:宋体"}

[[Valid]{lang="EN-US"}]{#struct_0_x1176_16249_735503574}

[[收到的合法]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x799882104}[协议报文数量]{style="font-family:宋体"}

[[Invalid]{lang="EN-US"}]{#struct_0_x1176_16249_1375747442}

[[收到的非法]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1883407439}[协议报文数量]{style="font-family:宋体"}

[[Succeeded]{lang="EN-US"}]{#struct_0_x1176_16249_x1138359445}

[[发送成功的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1019329488}[协议报文数量]{style="font-family:宋体"}

[[Failed]{lang="EN-US"}]{#struct_0_x1176_16249_735438038}

[[发送失败的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1982198990}[协议报文数量]{style="font-family:宋体"}

[[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_x1290357096}

[[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_506515966}[报文统计]{style="font-family:宋体"}

[[Reg]{lang="EN-US"}]{#struct_0_x1176_16249_x857795994}

[[注册报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_735634646}

[[Reg-stop]{lang="EN-US"}]{#struct_0_x1176_16249_x2073538678}

[[注册停止报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_1227937392}

[[JP]{lang="EN-US"}]{#struct_0_x1176_16249_x535642585}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_898288658}[剪枝报文统计]{style="font-family:宋体"}

[[BSM]{lang="EN-US"}]{#struct_0_x1176_16249_735569110}

[[自举报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_365729226}

[[Assert]{lang="EN-US"}]{#struct_0_x1176_16249_x210423020}

[[断言报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_1023374542}

[[Graft]{lang="EN-US"}]{#struct_0_x1176_16249_604266899}

[[嫁接报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_735765718}

[[Graft-ACK]{lang="EN-US"}]{#struct_0_x1176_16249_1466030624}

[[嫁接应答报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_265835470}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_40781184}

[[C-RP]{lang="EN-US"}]{#struct_0_x1176_16249_735700182}[报文统计]{style="font-family:宋体"}

[[SRM]{lang="EN-US"}]{#struct_0_x1176_16249_226006766}

[[状态刷新报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_x767330418}

[[DF]{lang="EN-US"}]{#struct_0_x1176_16249_x1718049602}

[[指定转发者报文统计]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1717852994}

[ ]{lang="EN-US"}

::: {#223489229 .myid}
[]{#_Toc404790444}[]{#struct_0_x1176_16249_x1217912575}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option dr-priority (IPv6 PIM view)**

------------------------------------------------------------------------

[**[hello-option dr-priority]{lang="EN-US"}**]{#struct_0_x1176_16249_x2123226325}[命令用来全局配置竞选]{style="font-family:
宋体"}[DR]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[undo hello-option dr-priority]{lang="EN-US"}**]{#struct_0_x1176_16249_971520265}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_735896790}

[**[hello-option dr-priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_x1176_16249_x1105339337}

[[undo hello-option dr-priority]{lang="EN-US"}]{#struct_0_x1176_16249_x1952634248}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1927432636}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x1176_16249_1071566972}[的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_303099905}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1914750028}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1885591425}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x321167182}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_735831254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1648632312}

[*[priority]{lang="EN-US"}*]{#struct_0_x1176_16249_659053150}[：指定竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。该数值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1661584839}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x264559211}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_980087017}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x2013969793}[在公网实例中全局配置竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1095716958}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] hello-option dr-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_736027862}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 pim]{lang="EN-US"}**[ **hello-option** **dr-priority**]{lang="EN-US"}]{#struct_0_x1176_16249_1045796142}
:::

::: {#1168032064 .myid}
[]{#_Toc404790445}[]{#struct_0_x1176_16249_x1341814825}[]{#_Toc311538861}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option holdtime (IPv6 PIM view)**

------------------------------------------------------------------------

[**[hello-option holdtime]{lang="EN-US"}**]{#struct_0_x1176_16249_1145408791}[命令用来全局配置保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居可达状态的时间。]{style="font-family:宋体"}

[**[undo hello-option holdtime]{lang="EN-US"}**]{#struct_0_x1176_16249_x835655631}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1618502709}

[**[hello-option holdtime]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1176_16249_x1531858493}

[[undo hello-option holdtime]{lang="EN-US"}]{#struct_0_x1176_16249_1639724935}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x897498550}

[[保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_735962326}[邻居可达状态的时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1490047854}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_206162107}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2112994347}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1544800707}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1650868941}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_944097508}

[*[time]{lang="EN-US"}*]{#struct_0_x1176_16249_x988936978}[：指定保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居可达状态的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。如果指定为]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒，则表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居永远可达。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_735503575}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x799882105}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1375812978}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1832444614}[在公网实例中全局配置保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居可达状态的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1870103669}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] hello-option holdtime 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_33906867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option holdtime]{lang="EN-US"}]{#struct_0_x1176_16249_958542310}
:::

::: {#-1507266648 .myid}
[]{#_Toc404790446}[]{#struct_0_x1176_16249_2061705210}[]{#_Toc311538862}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option lan-delay (IPv6 PIM view)**

------------------------------------------------------------------------

[**[hello-option lan-delay]{lang="EN-US"}**]{#struct_0_x1176_16249_533433906}[命令用来全局配置]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文在共享网段中的传输延迟。]{style="font-family:宋体"}

[**[undo hello-option lan-delay]{lang="EN-US"}**]{#struct_0_x1176_16249_735438039}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1982198989}

[**[hello-option lan-delay]{lang="EN-US"}**[ *delay*]{lang="EN-US"}]{#struct_0_x1176_16249_632022741}

[[undo hello-option lan-delay]{lang="EN-US"}]{#struct_0_x1176_16249_x386358913}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1380212814}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1086848687}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2023228874}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x953168912}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1984653601}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_735634647}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x2073538677}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1274991559}

[*[delay]{lang="EN-US"}*]{#struct_0_x1176_16249_660062026}[：指定]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文在共享网段中的传输延迟，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1354824388}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1107334558}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_51836534}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_687207068}[在公网实例中全局配置]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_735569111}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] hello-option lan-delay 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_365729225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hello-option override-interval (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x210423021}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option lan-delay]{lang="EN-US"}]{#struct_0_x1176_16249_1023309006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option override-interval]{lang="EN-US"}]{#struct_0_x1176_16249_x985707146}
:::

::: {#870100713 .myid}
[]{#_Toc404790447}[]{#struct_0_x1176_16249_872194778}[]{#_Toc311538863}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option neighbor-tracking (IPv6 PIM view)**

------------------------------------------------------------------------

[**[hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_x1176_16249_x1848452628}[命令用来全局使能邻居跟踪功能，即禁止加入报文抑制能力。]{style="font-family:
宋体"}

[**[undo hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_x1176_16249_x1587990436}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_735765719}

[[hello-option neighbor-tracking]{lang="EN-US"}]{#struct_0_x1176_16249_1466030623}

[[undo hello-option neighbor-tracking]{lang="EN-US"}]{#struct_0_x1176_16249_266032078}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x627816785}

[[邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。]{style="font-family:宋体"}]{#struct_0_x1176_16249_x24373075}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2140934510}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x2073533537}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1546923066}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1673498488}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_735700183}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_226006765}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x767330419}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1217978111}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1466974413}[在公网实例中全局使能邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x2077022958}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] hello-option neighbor-tracking]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x130635716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}]{#struct_0_x1176_16249_696622029}
:::

::: {#-1954122102 .myid}
[]{#_Toc404790448}[]{#struct_0_x1176_16249_735896791}[]{#_Toc311538864}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- hello-option override-interval (IPv6 PIM view)**

------------------------------------------------------------------------

[**[hello-option override-interval]{lang="EN-US"}**]{#struct_0_x1176_16249_x1105339336}[命令用来全局配置剪枝否决时间。]{style="font-family:
宋体"}

[**[undo hello-option override-interval]{lang="EN-US"}**]{#struct_0_x1176_16249_776249107}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_978234871}

[**[hello-option override-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1176_16249_x1068109629}

[[undo hello-option override-interval]{lang="EN-US"}]{#struct_0_x1176_16249_x1485492957}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1472787693}

[[剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}]{#struct_0_x1176_16249_247233446}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1449458253}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_735831255}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1648632313}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_659118686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1080482818}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1689925799}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_1809300824}[：指定剪枝否决时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x629922801}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x669127950}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1482117368}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_736027863}[在公网实例中全局配置剪枝否决时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1045796141}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] hello-option override-interval 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1341880361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hello-option lan-delay (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_1029121011}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option lan-delay]{lang="EN-US"}]{#struct_0_x1176_16249_x212817827}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option override-interval]{lang="EN-US"}]{#struct_0_x1176_16249_2081245118}
:::

::: {#-139780576 .myid}
[]{#_Toc404790449}[]{#struct_0_x1176_16249_1205514679}[]{#_Toc311538865}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- holdtime join-prune (IPv6 PIM view)**

------------------------------------------------------------------------

[**[holdtime join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_x193464914}[命令用来全局配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间。]{style="font-family:宋体"}

[**[undo holdtime join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_735962327}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1490047855}

[**[holdtime join-prune]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1176_16249_1772246048}

[[undo holdtime join-prune]{lang="EN-US"}]{#struct_0_x1176_16249_x1273368338}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2029172328}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_549654578}[剪枝状态的保持时间为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1671453225}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1719097315}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993379777}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x88025478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1723143852}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1939837332}

[*[time]{lang="EN-US"}*]{#struct_0_x1176_16249_1400485443}[：指定加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x859870615}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1807289588}[IPv6 PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x152162265}[接口向上游邻居发送加入]{style="font-family:
宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_415335003}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1021906924}[在公网实例中全局配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间为]{style="font-family:宋体"}[280]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993445313}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] holdtime join-prune 280]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1706900841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim holdtime join-prune]{lang="EN-US"}]{#struct_0_x1176_16249_x1909382458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[timer join-prune (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x152227801}
:::

::: {#392531114 .myid}
[]{#_Toc404790450}[]{#struct_0_x1176_16249_x178681033}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim**

------------------------------------------------------------------------

[**[ipv6 pim]{lang="EN-US"}**]{#struct_0_x1176_16249_x1643082205}[命令用来进入]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo ipv6 pim]{lang="EN-US"}**]{#struct_0_x1176_16249_x1073944497}[命令用来清除]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1559785330}

[[ipv6 pim \[ vpn-instance *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1176_16249_9384849}

[[undo ipv6 pim \[ vpn-instance *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1176_16249_x377014168}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993248705}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x827328241}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1224517075}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1129430685}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_763704164}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2059896573}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1176_16249_63396845}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1113993735}

[]{#_Toc288743026}[]{#_Toc94588285}[]{#_Toc80176812}[]{#struct_0_x1176_16249_24028716}[]{#_Toc60064435}[]{#_Toc60649397}[]{#_Toc76003031}[]{#_Toc76444956}[\# ]{lang="EN-US"}[先使能公网实例中的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[组播路由，再进入公网实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993314241}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\]]{lang="EN-US"}

[]{#_Toc311538868}[]{#_Toc293993792}[]{#_Toc323281737}[]{#_Toc319654934}[]{#_Toc318291818}[]{#_Toc293993395}[]{#_Toc330453730}[]{#struct_0_x1176_16249_860717601}[]{#_Toc324427652}[]{#_Toc324427653}[\# ]{lang="EN-US"}[先使能]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，再进入该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1788487368}

[\[Sysname\] ipv6 multicast routing vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-mrib6-mvpn\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-pim6-mvpn\]]{lang="EN-US"}
:::

::: {#-914111755 .myid}
[]{#_Toc404790451}[]{#struct_0_x1176_16249_47043772}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim bfd enable**

------------------------------------------------------------------------

[**[ipv6 pim bfd enable]{lang="EN-US"}**]{#struct_0_x1176_16249_x1217760932}[命令用来使能]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[**[undo ipv6 pim bfd enable]{lang="EN-US"}**]{#struct_0_x1176_16249_428902069}[命令用来关闭]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993117633}

[[ipv6 pim bfd enable]{lang="EN-US"}]{#struct_0_x1176_16249_1885104987}

[[undo ipv6 pim bfd enable]{lang="EN-US"}]{#struct_0_x1176_16249_x2013509193}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x582675762}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_208636980}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x655672815}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1596192363}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_243139761}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_977381925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1993183169}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1249115921}

[[只有在接口上先使能了]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}]{#struct_0_x1176_16249_524608996}[或]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x870495165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1929158570}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1021541367}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x88341246}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim dm]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim bfd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1992986561}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1277254130}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1332414386}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim dm]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim bfd enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_780091955}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim dm]{lang="EN-US"}]{#struct_0_x1176_16249_319431869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim sm]{lang="EN-US"}]{#struct_0_x1176_16249_x635655429}
:::

::: {#1276285395 .myid}
[]{#_Toc404790452}[]{#struct_0_x1176_16249_1378851787}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim bsr-boundary**

------------------------------------------------------------------------

[**[ipv6 pim bsr-boundary]{lang="EN-US"}**]{#struct_0_x1176_16249_x1993052097}[命令用来配置]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界，即]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[域的边界。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 pim bsr-boundary**]{lang="EN-US"}]{#struct_0_x1176_16249_1557514829}[命令用来删除]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_483807747}

[[ipv6 pim bsr-boundary]{lang="EN-US"}]{#struct_0_x1176_16249_2004001346}

[**[undo]{lang="EN-US"}**[ **ipv6 pim bsr-boundary**]{lang="EN-US"}]{#struct_0_x1176_16249_380472328}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1668130536}

[[没有配置]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_x1176_16249_1157452717}[的服务边界。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1202731862}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_781555754}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1992855489}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x653741250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_2009824787}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1240590549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_302400303}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x698644180}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_368900314}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim bsr-boundary]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1304692144}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1992921025}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[为]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x2029471891}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim bsr-boundary]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_651055692}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c-bsr (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x2056269810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 multicast boundary]{lang="EN-US"}]{#struct_0_x1176_16249_x357031058}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/IPv6]{lang="EN-US"}[组播路由与转发）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1585538107 .myid}
[]{#_Toc404790453}[]{#struct_0_x1176_16249_x1310360315}[]{#_Toc323281738}[]{#_Toc319654935}[]{#_Toc318291819}[]{#_Toc293993396}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim dm**

------------------------------------------------------------------------

[**[ipv6 pim dm]{lang="EN-US"}**]{#struct_0_x1176_16249_x240761030}[命令用来使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 pim dm]{lang="EN-US"}**]{#struct_0_x1176_16249_1471710735}[命令用来关闭]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993379776}

[[ipv6 pim dm]{lang="EN-US"}]{#struct_0_x1176_16249_x1654109419}

[[undo ipv6 pim dm]{lang="EN-US"}]{#struct_0_x1176_16249_39849751}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_953724531}

[[IPv6 PIM-DM]{lang="EN-US"}]{#struct_0_x1176_16249_x1906709538}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1360035517}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x216353246}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2101316497}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x328374373}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x150131054}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993445312}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_x1021982514}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_414387065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_104607080}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1850063914}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_x1176_16249_1798234091}[]{#_Hlt17604248}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="DE"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim dm]{lang="DE"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_2096048979}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_265987931}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993248704}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim dm]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_738755700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 multicast routing]{lang="EN-US"}**]{#struct_0_x1176_16249_x1451312358}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[IPv6]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#993552084 .myid}
[]{#_Toc404790454}[]{#struct_0_x1176_16249_x721765895}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option dr-priority**

------------------------------------------------------------------------

[**[ipv6 pim hello-option dr-priority]{lang="EN-US"}**]{#struct_0_x1176_16249_x1827298384}[命令用来在接口上配置竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[undo ipv6 pim hello-option dr-priority]{lang="EN-US"}**]{#struct_0_x1176_16249_x581833640}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x815738674}

[[ipv6 pim hello-option dr-priority *priority*]{lang="EN-US"}]{#struct_0_x1176_16249_x215910505}

[[undo ipv6 pim hello-option dr-priority]{lang="EN-US"}]{#struct_0_x1176_16249_x1993314240}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x705366340}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x1176_16249_x676668846}[的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1585816084}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x943016532}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x537897783}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1535605427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_2081563216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_433124984}

[*[priority]{lang="EN-US"}*]{#struct_0_x1176_16249_x1993117632}[：指定竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。该数值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_319021046}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1961996313}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_698791615}

[]{#struct_0_x1176_16249_x1588050995}[]{#_Toc87787387}[]{#_Toc87852266}[]{#_Toc87853045}[]{#_Toc87853826}[]{#_Toc87867882}[]{#_Toc87787388}[]{#_Toc87852267}[]{#_Toc87853046}[]{#_Toc87853827}[]{#_Toc87867883}[]{#_Toc87787389}[]{#_Toc87852268}[]{#_Toc87853047}[]{#_Toc87853828}[]{#_Toc87867884}[]{#_Toc87787390}[]{#_Toc87852269}[]{#_Toc87853048}[]{#_Toc87853829}[]{#_Toc87867885}[]{#_Toc87787391}[]{#_Toc87852270}[]{#_Toc87853049}[]{#_Toc87853830}[]{#_Toc87867886}[]{#_Toc87787392}[]{#_Toc87852271}[]{#_Toc87853050}[]{#_Toc87853831}[]{#_Toc87867887}[]{#_Toc87787393}[]{#_Toc87852272}[]{#_Toc87853051}[]{#_Toc87853832}[]{#_Toc87867888}[]{#_Toc87787394}[]{#_Toc87852273}[]{#_Toc87853052}[]{#_Toc87853833}[]{#_Toc87867889}[]{#_Toc87787396}[]{#_Toc87852275}[]{#_Toc87853054}[]{#_Toc87853835}[]{#_Toc87867891}[]{#_Toc87787398}[]{#_Toc87852277}[]{#_Toc87853056}[]{#_Toc87853837}[]{#_Toc87867893}[]{#_Toc87787399}[]{#_Toc87852278}[]{#_Toc87853057}[]{#_Toc87853838}[]{#_Toc87867894}[]{#_Toc87787400}[]{#_Toc87852279}[]{#_Toc87853058}[]{#_Toc87853839}[]{#_Toc87867895}[]{#_Toc87787401}[]{#_Toc87852280}[]{#_Toc87853059}[]{#_Toc87853840}[]{#_Toc87867896}[]{#_Toc87787403}[]{#_Toc87852282}[]{#_Toc87853061}[]{#_Toc87853842}[]{#_Toc87867898}[]{#_Toc87787404}[]{#_Toc87852283}[]{#_Toc87853062}[]{#_Toc87853843}[]{#_Toc87867899}[]{#_Toc87787405}[]{#_Toc87852284}[]{#_Toc87853063}[]{#_Toc87853844}[]{#_Toc87867900}[]{#_Toc87787406}[]{#_Toc87852285}[]{#_Toc87853064}[]{#_Toc87853845}[]{#_Toc87867901}[]{#_Toc87787407}[]{#_Toc87852286}[]{#_Toc87853065}[]{#_Toc87853846}[]{#_Toc87867902}[]{#_Toc87787408}[]{#_Toc87852287}[]{#_Toc87853066}[]{#_Toc87853847}[]{#_Toc87867903}[]{#_Toc87787409}[]{#_Toc87852288}[]{#_Toc87853067}[]{#_Toc87853848}[]{#_Toc87867904}[]{#_Toc87787410}[]{#_Toc87852289}[]{#_Toc87853068}[]{#_Toc87853849}[]{#_Toc87867905}[]{#_Toc87787412}[]{#_Toc87852291}[]{#_Toc87853070}[]{#_Toc87853851}[]{#_Toc87867907}[]{#_Toc87787413}[]{#_Toc87852292}[]{#_Toc87853071}[]{#_Toc87853852}[]{#_Toc87867908}[]{#_Toc87787414}[]{#_Toc87852293}[]{#_Toc87853072}[]{#_Toc87853853}[]{#_Toc87867909}[]{#_Toc87787415}[]{#_Toc87852294}[]{#_Toc87853073}[]{#_Toc87853854}[]{#_Toc87867910}[]{#_Toc87787418}[]{#_Toc87852297}[]{#_Toc87853076}[]{#_Toc87853857}[]{#_Toc87867913}[]{#_Toc87787419}[]{#_Toc87852298}[]{#_Toc87853077}[]{#_Toc87853858}[]{#_Toc87867914}[]{#_Toc87787420}[]{#_Toc87852299}[]{#_Toc87853078}[]{#_Toc87853859}[]{#_Toc87867915}[]{#_Toc87787421}[]{#_Toc87852300}[]{#_Toc87853079}[]{#_Toc87853860}[]{#_Toc87867916}[]{#_Toc87787422}[]{#_Toc87852301}[]{#_Toc87853080}[]{#_Toc87853861}[]{#_Toc87867917}[]{#_Toc87787423}[]{#_Toc87852302}[]{#_Toc87853081}[]{#_Toc87853862}[]{#_Toc87867918}[]{#_Toc87787424}[]{#_Toc87852303}[]{#_Toc87853082}[]{#_Toc87853863}[]{#_Toc87867919}[]{#_Toc87787425}[]{#_Toc87852304}[]{#_Toc87853083}[]{#_Toc87853864}[]{#_Toc87867920}[]{#_Toc87787428}[]{#_Toc87852307}[]{#_Toc87853086}[]{#_Toc87853867}[]{#_Toc87867923}[]{#_Toc87787429}[]{#_Toc87852308}[]{#_Toc87853087}[]{#_Toc87853868}[]{#_Toc87867924}[]{#_Toc87787430}[]{#_Toc87852309}[]{#_Toc87853088}[]{#_Toc87853869}[]{#_Toc87867925}[]{#_Toc87787432}[]{#_Toc87852311}[]{#_Toc87853090}[]{#_Toc87853871}[]{#_Toc87867927}[]{#_Toc87787433}[]{#_Toc87852312}[]{#_Toc87853091}[]{#_Toc87853872}[]{#_Toc87867928}[]{#_Toc87787434}[]{#_Toc87852313}[]{#_Toc87853092}[]{#_Toc87853873}[]{#_Toc87867929}[]{#_Toc87787435}[]{#_Toc87852314}[]{#_Toc87853093}[]{#_Toc87853874}[]{#_Toc87867930}[]{#_Toc87787436}[]{#_Toc87852315}[]{#_Toc87853094}[]{#_Toc87853875}[]{#_Toc87867931}[]{#_Toc87787437}[]{#_Toc87852316}[]{#_Toc87853095}[]{#_Toc87853876}[]{#_Toc87867932}[]{#_Toc87787438}[]{#_Toc87852317}[]{#_Toc87853096}[]{#_Toc87853877}[]{#_Toc87867933}[]{#_Toc87787439}[]{#_Toc87852318}[]{#_Toc87853097}[]{#_Toc87853878}[]{#_Toc87867934}[]{#_Toc87787440}[]{#_Toc87852319}[]{#_Toc87853098}[]{#_Toc87853879}[]{#_Toc87867935}[]{#_Toc87787443}[]{#_Toc87852322}[]{#_Toc87853101}[]{#_Toc87853882}[]{#_Toc87867938}[]{#_Toc87787444}[]{#_Toc87852323}[]{#_Toc87853102}[]{#_Toc87853883}[]{#_Toc87867939}[]{#_Toc87787445}[]{#_Toc87852324}[]{#_Toc87853103}[]{#_Toc87853884}[]{#_Toc87867940}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_44465399}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1118483220}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim hello-option dr-priority 3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1469454452}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1993183168}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1479767434}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim hello-option dr-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1184902829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option dr-priority]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x358052589}
:::

::: {#-991859120 .myid}
[]{#_Toc404790455}[]{#struct_0_x1176_16249_1655638119}[]{#_Toc311538869}[]{#_Toc293993793}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option holdtime**

------------------------------------------------------------------------

[**[ipv6 pim hello-option holdtime]{lang="EN-US"}**]{#struct_0_x1176_16249_x895366745}[命令用来在接口上配置保持]{style="font-family:
宋体"}[IPv6 PIM]{lang="EN-US"}[邻居的可达状态的时间。]{style="font-family:
宋体"}

[**[undo ipv6 pim hello-option holdtime]{lang="EN-US"}**]{#struct_0_x1176_16249_792727294}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1395393362}

[**[ipv6 pim hello-option holdtime]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1176_16249_x1992986560}

[[undo ipv6 pim hello-option holdtime]{lang="EN-US"}]{#struct_0_x1176_16249_x1451629225}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x561944794}

[[保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1490160613}[邻居可达状态的时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1486017178}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_189810211}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2093641561}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_52942805}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x2045622162}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993052096}

[*[time]{lang="EN-US"}*]{#struct_0_x1176_16249_x8569112}[：指定保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居可达状态的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。如果指定为]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒，则表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居永远可达。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1736532170}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_830210636}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1044502834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1960129489}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x333287392}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居可达状态的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1992855488}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim hello-option holdtime 120]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_2075142105}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_46272859}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置保持]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居可达状态的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x62405199}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim hello-option holdtime 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1469549305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option holdtime]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x770067647}
:::

::: {#-1218195166 .myid}
[]{#_Toc404790456}[]{#struct_0_x1176_16249_x1133557603}[]{#_Toc311538870}[]{#_Toc293993794}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option lan-delay**

------------------------------------------------------------------------

[**[ipv6 pim hello-option lan-delay]{lang="EN-US"}**]{#struct_0_x1176_16249_760699423}[命令用来在接口上配置]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文在共享网段中的传输延迟。]{style="font-family:宋体"}

[**[undo ipv6 pim hello-option lan-delay]{lang="EN-US"}**]{#struct_0_x1176_16249_x1992921024}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x463387950}

[**[ipv6 pim hello-option lan-delay]{lang="EN-US"}**[ *delay*]{lang="EN-US"}]{#struct_0_x1176_16249_1699565861}

[[undo ipv6 pim hello-option lan-delay]{lang="EN-US"}]{#struct_0_x1176_16249_1913959896}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1810680764}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1185942032}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1946979604}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x84386782}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1861563699}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1993379779}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1250824892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_219760568}

[*[delay]{lang="EN-US"}*]{#struct_0_x1176_16249_x1158108617}[：指定]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文在共享网段中的传输延迟，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2127565810}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_122664783}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x142229760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x301323751}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1273136021}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993445315}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim hello-option lan-delay 200]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_900331787}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1427267611}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_963581859}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim hello-option lan-delay 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_148822139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hello-option lan-delay (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x787485626}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hello-option override-interval (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x1707176974}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option override-interval]{lang="EN-US"}]{#struct_0_x1176_16249_x1993248707}
:::

::: {#-1274121472 .myid}
[]{#_Toc404790457}[]{#struct_0_x1176_16249_x1990127655}[]{#_Toc311538871}[]{#_Toc293993795}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option neighbor-tracking**

------------------------------------------------------------------------

[**[ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_x1176_16249_x1744324823}[命令用来在接口上使能邻居跟踪功能，即禁止加入报文抑制能力。]{style="font-family:宋体"}

[**[ipv6 pim hello-option neighbor-tracking disable]{lang="EN-US"}**]{#struct_0_x1176_16249_x1240633677}[命令用来在全局使能了邻居跟踪功能的情况下，关闭当前接口上的邻居跟踪功能。]{style="font-family:宋体"}

[**[undo ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_x1176_16249_1538935013}[命令用来抵消上述两条命令的配置，即让接口与全局配置保持一致。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_620612843}

[[ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}]{#struct_0_x1176_16249_1237232345}

[**[ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}**[ **disable**]{lang="EN-US"}]{#struct_0_x1176_16249_364707479}

[[undo ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}]{#struct_0_x1176_16249_x1455265552}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993314243}

[[邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。]{style="font-family:宋体"}]{#struct_0_x1176_16249_2023517015}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1787867878}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x230566847}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1931475266}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1168100750}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_990860210}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1974314982}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1993117635}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1603293255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_1817926504}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_896724276}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1847765301}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_x1176_16249_x913983300}[在公网实例全局使能了邻居跟踪功能的情况下，关闭接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993183171}

[\[Sysname\]ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\]hello-option neighbor-tracking ]{lang="EN-US"}

[\[Sysname-pim6\]quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim hello-option neighbor-tracking disable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_892820025}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_480136616}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x451676168}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim hello-option neighbor-tracking]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x837929173}[在公网实例全局使能了邻居跟踪功能的情况下，关闭接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上的邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_2138379056}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] hello-option neighbor-tracking]{lang="EN-US"}

[\[Sysname-pim6\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim hello-option neighbor-tracking disable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x715900881}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option neighbor-tracking]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x1992986563}
:::

::: {#-1162551863 .myid}
[]{#_Toc404790458}[]{#struct_0_x1176_16249_114454716}[]{#_Toc311538872}[]{#_Toc293993796}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim hello-option override-interval**

------------------------------------------------------------------------

[**[ipv6 pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_x1176_16249_783023142}[命令用来在接口上配置剪枝否决时间。]{style="font-family:宋体"}

[**[undo ipv6 pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_x1176_16249_1774028474}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_213487669}

[**[ipv6 pim hello-option override-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1176_16249_11869797}

[[undo ipv6 pim hello-option override-interval]{lang="EN-US"}]{#struct_0_x1176_16249_x328517775}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1322808159}

[[剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}]{#struct_0_x1176_16249_x1648065276}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993052099}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1574653053}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1252277389}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x2125107135}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_549013823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2011585871}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_883714373}[：指定剪枝否决时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1796711263}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1992855491}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1009906074}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1926574964}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_2110403822}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置剪枝否决时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x577463463}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim hello-option override-interval 2000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1313966305}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_5457855}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置剪枝否决时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x625357375}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim hello-option override-interval 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1992921027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hello-option lan-delay (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x866672477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hello-option override-interval (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_1828981437}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim hello-option lan-delay]{lang="EN-US"}]{#struct_0_x1176_16249_x1244289197}
:::

::: {#206989217 .myid}
[]{#_Toc404790459}[]{#struct_0_x1176_16249_1570290915}[]{#_Toc311538873}[]{#_Toc293993798}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim holdtime join-prune**

------------------------------------------------------------------------

[**[ipv6 pim holdtime join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_203699529}[命令用来在接口上配置加入]{style="font-family:
宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间。]{style="font-family:宋体"}

[**[undo ipv6 pim holdtime join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_884064321}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_563603587}

[**[ipv6 pim holdtime join-prune]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1176_16249_x1434206962}

[[undo ipv6 pim holdtime join-prune]{lang="EN-US"}]{#struct_0_x1176_16249_x1993379778}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1478058463}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_x86601675}[剪枝状态的保持时间为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1704207363}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_2085040418}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x210081038}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x2129896161}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x602369642}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993445314}

[*[time]{lang="EN-US"}*]{#struct_0_x1176_16249_x1828551568}[：指定加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2052141145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_x1176_16249_62432144}[IPv6 PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x152358874}[接口向上游邻居发送加入]{style="font-family:
宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2025955130}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1835799268}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1973525675}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间为]{style="font-family:宋体"}[280]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1818641177}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim holdtime join-prune 280]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1993248706}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x424043714}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间为]{style="font-family:宋体"}[280]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1748917828}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim holdtime join-prune 280]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_417332137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[holdtime join-prune]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x400184509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 pim timer join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_x152227802}[]{#_Toc400703958}[]{#_Toc398976000}
:::

::: {#146103896 .myid}
[]{#_Toc404790460}[]{#struct_0_x1176_16249_1632433065}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim nbma-mode**

------------------------------------------------------------------------

[**[ipv6 pim nbma-mode]{lang="EN-US"}**]{#struct_0_x1176_16249_x1247704785}[命令用来在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道]{style="font-family:宋体"}[tunnel]{lang="EN-US"}[口上使能]{style="font-family:宋体"}[IPv6 PIM-NBMA]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1919392156}

[**[ipv6 pim nbma-mode]{lang="EN-US"}**]{#struct_0_x1176_16249_x544551309}

[**[undo ipv6 pim nbma-mode]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1176_16249_x677870135}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1257241851}

[[ADVPN]{lang="EN-US"}]{#struct_0_x1176_16249_1353742014}[隧道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x261276805}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1201855556}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_2035902956}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x909315966}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_x1096450290}[组播路由，接口上使能]{style="font-family:宋体"}[IPv6 PIM SM]{lang="EN-US"}[协议，本命令才能生效。本命令不支持]{style="font-family:宋体"}[PIM DM]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_859696506}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1067593421}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel 0]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-NBMA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1522273605}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface Tunnel 0 mode advpn]{lang="EN-US"}
:::

::: {#-1135500882 .myid}
[]{#_Toc311538874}[]{#_Toc404790461}[]{#struct_0_x1176_16249_x1250507957}[]{#_Toc323281745}[]{#_Toc319654942}[]{#_Toc318291826}[]{#_Toc293993404}[]{#_Toc193253318}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim neighbor-policy**

------------------------------------------------------------------------

[**[ipv6 pim neighbor-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x840281804}[命令用来配置合法]{style="font-family:
宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，以防止]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文欺骗。]{style="font-family:宋体"}

[**[undo ipv6 pim neighbor-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_602441031}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993314242}

[**[ipv6 pim neighbor-policy]{lang="EN-US"}**[ *acl6-number*]{lang="EN-US"}]{#struct_0_x1176_16249_457433074}

[**[undo ipv6 pim neighbor-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x1623121952}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1574124663}

[[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_1064082912}[报文的源地址范围不受任何限制，即认为所有收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文都是合法的。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1097809153}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x523878859}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1438341456}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1951419555}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1993117634}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1125590100}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_x2080296131}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x490897188}

[[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_x513959092}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定合法]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1055194299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_895707181}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_864012800}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置合法]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，只允许与来自网段]{style="font-family:宋体"}[FE80:101::101/64]{lang="EN-US"}[中的设备建立]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居关系。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993183170}

[\[Sysname\] acl ipv6 number 2000]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] rule permit source fe80:101::101 64]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim neighbor-policy 2000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1836063330}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1542705808}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置合法]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，只允许与来自网段]{style="font-family:宋体"}[FE80:101::101/64]{lang="EN-US"}[中的设备建立]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[邻居关系。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1998724888}

[\[Sysname\] acl ipv6 basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule permit source fe80:101::101 64]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\][ ipv6 pim neighbor-policy 2000]{.TerminalDisplayChar}]{lang="EN-US"}
:::

::: {#409532265 .myid}
[]{#_Toc404790462}[]{#struct_0_x1176_16249_269691568}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim require-genid**

------------------------------------------------------------------------

[**[ipv6 pim require-genid]{lang="EN-US"}**]{#struct_0_x1176_16249_135637163}[命令用来配置拒绝无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo ipv6 pim require-genid]{lang="EN-US"}**]{#struct_0_x1176_16249_x1992986562}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1680538657}

[[ipv6 pim require-genid]{lang="EN-US"}]{#struct_0_x1176_16249_80073201}

[[undo ipv6 pim require-genid]{lang="EN-US"}]{#struct_0_x1176_16249_x1699343113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_540970294}

[[接受无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_x1176_16249_x620746157}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x71165881}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x282560585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x591837997}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1993052098}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1154230302}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1821170349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_911315963}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x403745974}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[拒绝无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1416247435}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim require-genid]{lang="EN-US"}

[]{#struct_0_x1176_16249_483817983}[]{#_Toc87442659}[]{#_Toc87787453}[]{#_Toc87852332}[]{#_Toc87853111}[]{#_Toc87853892}[]{#_Toc87867949}[]{#_Toc87442660}[]{#_Toc87787454}[]{#_Toc87852333}[]{#_Toc87853112}[]{#_Toc87853893}[]{#_Toc87867950}[]{#_Toc87442662}[]{#_Toc87787456}[]{#_Toc87852335}[]{#_Toc87853114}[]{#_Toc87853895}[]{#_Toc87867952}[]{#_Toc87442663}[]{#_Toc87787457}[]{#_Toc87852336}[]{#_Toc87853115}[]{#_Toc87853896}[]{#_Toc87867953}[]{#_Toc87442664}[]{#_Toc87787458}[]{#_Toc87852337}[]{#_Toc87853116}[]{#_Toc87853897}[]{#_Toc87867954}[]{#_Toc87442665}[]{#_Toc87787459}[]{#_Toc87852338}[]{#_Toc87853117}[]{#_Toc87853898}[]{#_Toc87867955}[]{#_Toc87442666}[]{#_Toc87787460}[]{#_Toc87852339}[]{#_Toc87853118}[]{#_Toc87853899}[]{#_Toc87867956}[]{#_Toc87442667}[]{#_Toc87787461}[]{#_Toc87852340}[]{#_Toc87853119}[]{#_Toc87853900}[]{#_Toc87867957}[]{#_Toc87442668}[]{#_Toc87787462}[]{#_Toc87852341}[]{#_Toc87853120}[]{#_Toc87853901}[]{#_Toc87867958}[]{#_Toc87442669}[]{#_Toc87787463}[]{#_Toc87852342}[]{#_Toc87853121}[]{#_Toc87853902}[]{#_Toc87867959}[]{#_Toc87442670}[]{#_Toc87787464}[]{#_Toc87852343}[]{#_Toc87853122}[]{#_Toc87853903}[]{#_Toc87867960}[]{#_Toc87442671}[]{#_Toc87787465}[]{#_Toc87852344}[]{#_Toc87853123}[]{#_Toc87853904}[]{#_Toc87867961}[]{#_Toc87442672}[]{#_Toc87787466}[]{#_Toc87852345}[]{#_Toc87853124}[]{#_Toc87853905}[]{#_Toc87867962}[]{#_Toc87442673}[]{#_Toc87787467}[]{#_Toc87852346}[]{#_Toc87853125}[]{#_Toc87853906}[]{#_Toc87867963}[]{#_Toc87442674}[]{#_Toc87787468}[]{#_Toc87852347}[]{#_Toc87853126}[]{#_Toc87853907}[]{#_Toc87867964}[]{#_Toc87442675}[]{#_Toc87787469}[]{#_Toc87852348}[]{#_Toc87853127}[]{#_Toc87853908}[]{#_Toc87867965}[]{#_Toc87442676}[]{#_Toc87787470}[]{#_Toc87852349}[]{#_Toc87853128}[]{#_Toc87853909}[]{#_Toc87867966}[]{#_Toc87442677}[]{#_Toc87787471}[]{#_Toc87852350}[]{#_Toc87853129}[]{#_Toc87853910}[]{#_Toc87867967}[]{#_Toc87442678}[]{#_Toc87787472}[]{#_Toc87852351}[]{#_Toc87853130}[]{#_Toc87853911}[]{#_Toc87867968}[]{#_Toc87442679}[]{#_Toc87787473}[]{#_Toc87852352}[]{#_Toc87853131}[]{#_Toc87853912}[]{#_Toc87867969}[]{#_Toc87442680}[]{#_Toc87787474}[]{#_Toc87852353}[]{#_Toc87853132}[]{#_Toc87853913}[]{#_Toc87867970}[]{#_Toc87442681}[]{#_Toc87787475}[]{#_Toc87852354}[]{#_Toc87853133}[]{#_Toc87853914}[]{#_Toc87867971}[]{#_Toc87442682}[]{#_Toc87787476}[]{#_Toc87852355}[]{#_Toc87853134}[]{#_Toc87853915}[]{#_Toc87867972}[]{#_Toc87442683}[]{#_Toc87787477}[]{#_Toc87852356}[]{#_Toc87853135}[]{#_Toc87853916}[]{#_Toc87867973}[]{#_Toc87442684}[]{#_Toc87787478}[]{#_Toc87852357}[]{#_Toc87853136}[]{#_Toc87853917}[]{#_Toc87867974}[]{#_Toc87442685}[]{#_Toc87787479}[]{#_Toc87852358}[]{#_Toc87853137}[]{#_Toc87853918}[]{#_Toc87867975}[]{#_Toc87442686}[]{#_Toc87787480}[]{#_Toc87852359}[]{#_Toc87853138}[]{#_Toc87853919}[]{#_Toc87867976}[]{#_Toc87442687}[]{#_Toc87787481}[]{#_Toc87852360}[]{#_Toc87853139}[]{#_Toc87853920}[]{#_Toc87867977}[]{#_Toc87442688}[]{#_Toc87787482}[]{#_Toc87852361}[]{#_Toc87853140}[]{#_Toc87853921}[]{#_Toc87867978}[]{#_Toc87442689}[]{#_Toc87787483}[]{#_Toc87852362}[]{#_Toc87853141}[]{#_Toc87853922}[]{#_Toc87867979}[]{#_Toc87442690}[]{#_Toc87787484}[]{#_Toc87852363}[]{#_Toc87853142}[]{#_Toc87853923}[]{#_Toc87867980}[]{#_Toc87442691}[]{#_Toc87787485}[]{#_Toc87852364}[]{#_Toc87853143}[]{#_Toc87853924}[]{#_Toc87867981}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1522085877}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[拒绝无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1992855490}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim require-genid]{lang="EN-US"}
:::

::: {#-1584030779 .myid}
[]{#_Toc404790463}[]{#struct_0_x1176_16249_1718977281}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim sm**

------------------------------------------------------------------------

[**[ipv6 pim sm]{lang="EN-US"}**]{#struct_0_x1176_16249_x443778912}[命令用来使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 pim sm]{lang="EN-US"}**]{#struct_0_x1176_16249_441562698}[命令用来关闭]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x920069610}

[[ipv6 pim sm]{lang="EN-US"}]{#struct_0_x1176_16249_1391663590}

[[undo ipv6 pim sm]{lang="EN-US"}]{#struct_0_x1176_16249_1048509089}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x919118674}

[[IPv6 PIM-SM]{lang="EN-US"}]{#struct_0_x1176_16249_x1992921026}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_699411464}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1747055305}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x989279456}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1792283654}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1314456798}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1047635558}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_x1508548016}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_673769872}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1993379781}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x895184356}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1219491851}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim sm]{lang="EN-US"}

[]{#_Toc94588286}[]{#_Toc78346670}[]{#_Toc80176813}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_1582403585}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_626197082}[使能公网实例中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_2009151212}

[\[Sysname\] ipv6 multicast routing]{lang="EN-US"}

[\[Sysname-mrib6\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim sm]{lang="EN-US"}

[]{#_Toc311538876}[]{#_Toc293993804}[]{#_Toc323281748}[]{#_Toc319654945}[]{#_Toc318291829}[]{#_Toc293993407}[]{#struct_0_x1176_16249_445680546}[]{#_Toc324427665}[]{#_Toc324427666}[【相关命令】]{style="font-family:
黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 multicast routing]{lang="EN-US"}**]{#struct_0_x1176_16249_x1993445317}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[IPv6]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#169956355 .myid}
[]{#_Toc404790464}[]{#struct_0_x1176_16249_x262467627}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim state-refresh-capable**

------------------------------------------------------------------------

[**[ipv6 pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_x1176_16249_267800963}[命令用来使能状态刷新能力。]{style="font-family:
宋体"}

[**[undo ipv6 pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_x1176_16249_944443151}[命令用来关闭状态刷新能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_671929748}

[[ipv6 pim state-refresh-capable]{lang="EN-US"}]{#struct_0_x1176_16249_x12821504}

[[undo ipv6 pim state-refresh-capable]{lang="EN-US"}]{#struct_0_x1176_16249_761832161}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2142996831}

[[状态刷新能力处于使能状态。]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1993248709}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1498270587}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_1710184679}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1315952502}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1009050936}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1369188642}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x774042100}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x993072432}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x43238388}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上关闭状态刷新能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993314245}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo ipv6 pim state-refresh-capable]{lang="EN-US"}

[]{#struct_0_x1176_16249_x1464881227}[]{#_Toc87787489}[]{#_Toc87852368}[]{#_Toc87853147}[]{#_Toc87853928}[]{#_Toc87867985}[]{#_Toc87787490}[]{#_Toc87852369}[]{#_Toc87853148}[]{#_Toc87853929}[]{#_Toc87867986}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x69367707}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上关闭状态刷新能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1912759548}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] undo ipv6 pim state-refresh-capable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x680712232}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-hoplimit (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_33250259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-interval (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_908772880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-rate-limit (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x1993117637}
:::

::: {#1124618850 .myid}
[]{#_Toc404790465}[]{#struct_0_x1176_16249_x440493841}[]{#_Toc323281749}[]{#_Toc319654946}[]{#_Toc318291830}[]{#_Toc293993408}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim timer graft-retry**

------------------------------------------------------------------------

[**[ipv6 pim timer graft-retry]{lang="EN-US"}**]{#struct_0_x1176_16249_x1378116425}[命令用来配置嫁接报文的重传时间。]{style="font-family:
宋体"}

[**[undo ipv6 pim timer graft-retry]{lang="EN-US"}**]{#struct_0_x1176_16249_x1497263925}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1879370266}

[**[ipv6 pim timer graft-retry ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_x1325124312}

[[undo ipv6 pim]{lang="SV"}[ ]{lang="SV"}]{#struct_0_x1176_16249_x1695884156}[timer graft-retry]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x645958667}

[[嫁接报文的重传时间为]{style="font-family:宋体"}]{#struct_0_x1176_16249_1291302536}[3]{lang="SV"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993183173}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x269979389}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1059778932}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1911081355}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1455591565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1201057741}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_1255899583}[：]{style="font-family:宋体"}[指定嫁接报文的重传时间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[65535]{lang="SV"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1699632206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x2789580}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1992986565}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置嫁接报文的重传时间为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1048344698}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim timer graft-retry 80]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x1346430423}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_600725888}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置嫁接报文的重传时间为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1377129725}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim timer graft-retry 80]{lang="NO-BOK"}
:::

::: {#-1529954196 .myid}
[]{#_Toc404790466}[]{#struct_0_x1176_16249_915970152}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim timer hello**

------------------------------------------------------------------------

[**[ipv6 pim timer hello]{lang="EN-US"}**]{#struct_0_x1176_16249_629132831}[命令用来在接口上配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo ipv6 pim timer hello]{lang="EN-US"}**]{#struct_0_x1176_16249_x1993052101}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1930424660}

[**[ipv6 pim timer hello]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1176_16249_x1843194630}

[[undo ipv6 pim timer hello]{lang="EN-US"}]{#struct_0_x1176_16249_373800515}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1479359090}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_x224313394}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1116298961}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1801082303}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2114736506}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1992855493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_152893340}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1090547575}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_x1857741977}[：指定发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x956400545}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_91550349}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x793951280}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_602386934}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_572010706}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1992921029}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="EN-US"}[ipv6 pim timer hello 40]{lang="NO-BOK"}

[]{#struct_0_x1176_16249_x60103423}[]{#_Toc87442697}[]{#_Toc87787494}[]{#_Toc87852373}[]{#_Toc87853152}[]{#_Toc87853933}[]{#_Toc87867990}[]{#_Toc87442698}[]{#_Toc87787495}[]{#_Toc87852374}[]{#_Toc87853153}[]{#_Toc87853934}[]{#_Toc87867991}[]{#_Toc87442700}[]{#_Toc87787497}[]{#_Toc87852376}[]{#_Toc87853155}[]{#_Toc87853936}[]{#_Toc87867993}[]{#_Toc87442701}[]{#_Toc87787498}[]{#_Toc87852377}[]{#_Toc87853156}[]{#_Toc87853937}[]{#_Toc87867994}[]{#_Toc87442702}[]{#_Toc87787499}[]{#_Toc87852378}[]{#_Toc87853157}[]{#_Toc87853938}[]{#_Toc87867995}[]{#_Toc87442703}[]{#_Toc87787500}[]{#_Toc87852379}[]{#_Toc87853158}[]{#_Toc87853939}[]{#_Toc87867996}[]{#_Toc87442704}[]{#_Toc87787501}[]{#_Toc87852380}[]{#_Toc87853159}[]{#_Toc87853940}[]{#_Toc87867997}[]{#_Toc87442705}[]{#_Toc87787502}[]{#_Toc87852381}[]{#_Toc87853160}[]{#_Toc87853941}[]{#_Toc87867998}[]{#_Toc87442706}[]{#_Toc87787503}[]{#_Toc87852382}[]{#_Toc87853161}[]{#_Toc87853942}[]{#_Toc87867999}[]{#_Toc87442707}[]{#_Toc87787504}[]{#_Toc87852383}[]{#_Toc87853162}[]{#_Toc87853943}[]{#_Toc87868000}[]{#_Toc87442708}[]{#_Toc87787505}[]{#_Toc87852384}[]{#_Toc87853163}[]{#_Toc87853944}[]{#_Toc87868001}[]{#_Toc87442709}[]{#_Toc87787506}[]{#_Toc87852385}[]{#_Toc87853164}[]{#_Toc87853945}[]{#_Toc87868002}[]{#_Toc87442710}[]{#_Toc87787507}[]{#_Toc87852386}[]{#_Toc87853165}[]{#_Toc87853946}[]{#_Toc87868003}[]{#_Toc87442712}[]{#_Toc87787509}[]{#_Toc87852388}[]{#_Toc87853167}[]{#_Toc87853948}[]{#_Toc87868005}[]{#_Toc87442713}[]{#_Toc87787510}[]{#_Toc87852389}[]{#_Toc87853168}[]{#_Toc87853949}[]{#_Toc87868006}[]{#_Toc87442715}[]{#_Toc87787512}[]{#_Toc87852391}[]{#_Toc87853170}[]{#_Toc87853951}[]{#_Toc87868008}[]{#_Toc87442716}[]{#_Toc87787513}[]{#_Toc87852392}[]{#_Toc87853171}[]{#_Toc87853952}[]{#_Toc87868009}[]{#_Toc87442717}[]{#_Toc87787514}[]{#_Toc87852393}[]{#_Toc87853172}[]{#_Toc87853953}[]{#_Toc87868010}[]{#_Toc87442719}[]{#_Toc87787516}[]{#_Toc87852395}[]{#_Toc87853174}[]{#_Toc87853955}[]{#_Toc87868012}[]{#_Toc87442720}[]{#_Toc87787517}[]{#_Toc87852396}[]{#_Toc87853175}[]{#_Toc87853956}[]{#_Toc87868013}[]{#_Toc87442721}[]{#_Toc87787518}[]{#_Toc87852397}[]{#_Toc87853176}[]{#_Toc87853957}[]{#_Toc87868014}[]{#_Toc87442722}[]{#_Toc87787519}[]{#_Toc87852398}[]{#_Toc87853177}[]{#_Toc87853958}[]{#_Toc87868015}[]{#_Toc87442723}[]{#_Toc87787520}[]{#_Toc87852399}[]{#_Toc87853178}[]{#_Toc87853959}[]{#_Toc87868016}[]{#_Toc87442724}[]{#_Toc87787521}[]{#_Toc87852400}[]{#_Toc87853179}[]{#_Toc87853960}[]{#_Toc87868017}[]{#_Toc87442725}[]{#_Toc87787522}[]{#_Toc87852401}[]{#_Toc87853180}[]{#_Toc87853961}[]{#_Toc87868018}[]{#_Toc87442726}[]{#_Toc87787523}[]{#_Toc87852402}[]{#_Toc87853181}[]{#_Toc87853962}[]{#_Toc87868019}[]{#_Toc87442727}[]{#_Toc87787524}[]{#_Toc87852403}[]{#_Toc87853182}[]{#_Toc87853963}[]{#_Toc87868020}[]{#_Toc87442728}[]{#_Toc87787525}[]{#_Toc87852404}[]{#_Toc87853183}[]{#_Toc87853964}[]{#_Toc87868021}[]{#_Toc87442731}[]{#_Toc87787528}[]{#_Toc87852407}[]{#_Toc87853186}[]{#_Toc87853967}[]{#_Toc87868024}[]{#_Toc87442732}[]{#_Toc87787529}[]{#_Toc87852408}[]{#_Toc87853187}[]{#_Toc87853968}[]{#_Toc87868025}[]{#_Toc87442734}[]{#_Toc87787531}[]{#_Toc87852410}[]{#_Toc87853189}[]{#_Toc87853970}[]{#_Toc87868027}[]{#_Toc87442735}[]{#_Toc87787532}[]{#_Toc87852411}[]{#_Toc87853190}[]{#_Toc87853971}[]{#_Toc87868028}[]{#_Toc87442736}[]{#_Toc87787533}[]{#_Toc87852412}[]{#_Toc87853191}[]{#_Toc87853972}[]{#_Toc87868029}[]{#_Toc87442737}[]{#_Toc87787534}[]{#_Toc87852413}[]{#_Toc87853192}[]{#_Toc87853973}[]{#_Toc87868030}[]{#_Toc87442738}[]{#_Toc87787535}[]{#_Toc87852414}[]{#_Toc87853193}[]{#_Toc87853974}[]{#_Toc87868031}[]{#_Toc87442739}[]{#_Toc87787536}[]{#_Toc87852415}[]{#_Toc87853194}[]{#_Toc87853975}[]{#_Toc87868032}[]{#_Toc87442740}[]{#_Toc87787537}[]{#_Toc87852416}[]{#_Toc87853195}[]{#_Toc87853976}[]{#_Toc87868033}[]{#_Toc87442741}[]{#_Toc87787538}[]{#_Toc87852417}[]{#_Toc87853196}[]{#_Toc87853977}[]{#_Toc87868034}[]{#_Toc87442742}[]{#_Toc87787539}[]{#_Toc87852418}[]{#_Toc87853197}[]{#_Toc87853978}[]{#_Toc87868035}[]{#_Toc87442743}[]{#_Toc87787540}[]{#_Toc87852419}[]{#_Toc87853198}[]{#_Toc87853979}[]{#_Toc87868036}[]{#_Toc87442744}[]{#_Toc87787541}[]{#_Toc87852420}[]{#_Toc87853199}[]{#_Toc87853980}[]{#_Toc87868037}[]{#_Toc87442745}[]{#_Toc87787542}[]{#_Toc87852421}[]{#_Toc87853200}[]{#_Toc87853981}[]{#_Toc87868038}[]{#_Toc87442746}[]{#_Toc87787543}[]{#_Toc87852422}[]{#_Toc87853201}[]{#_Toc87853982}[]{#_Toc87868039}[]{#_Toc87442747}[]{#_Toc87787544}[]{#_Toc87852423}[]{#_Toc87853202}[]{#_Toc87853983}[]{#_Toc87868040}[]{#_Toc87442748}[]{#_Toc87787545}[]{#_Toc87852424}[]{#_Toc87853203}[]{#_Toc87853984}[]{#_Toc87868041}[]{#_Toc87442749}[]{#_Toc87787546}[]{#_Toc87852425}[]{#_Toc87853204}[]{#_Toc87853985}[]{#_Toc87868042}[]{#_Toc87442750}[]{#_Toc87787547}[]{#_Toc87852426}[]{#_Toc87853205}[]{#_Toc87853986}[]{#_Toc87868043}[]{#_Toc87442752}[]{#_Toc87787549}[]{#_Toc87852428}[]{#_Toc87853207}[]{#_Toc87853988}[]{#_Toc87868045}[]{#_Toc87442753}[]{#_Toc87787550}[]{#_Toc87852429}[]{#_Toc87853208}[]{#_Toc87853989}[]{#_Toc87868046}[]{#_Toc87442754}[]{#_Toc87787551}[]{#_Toc87852430}[]{#_Toc87853209}[]{#_Toc87853990}[]{#_Toc87868047}[]{#_Toc87442755}[]{#_Toc87787552}[]{#_Toc87852431}[]{#_Toc87853210}[]{#_Toc87853991}[]{#_Toc87868048}[]{#_Toc87442756}[]{#_Toc87787553}[]{#_Toc87852432}[]{#_Toc87853211}[]{#_Toc87853992}[]{#_Toc87868049}[]{#_Toc87442757}[]{#_Toc87787554}[]{#_Toc87852433}[]{#_Toc87853212}[]{#_Toc87853993}[]{#_Toc87868050}[]{#_Toc87442758}[]{#_Toc87787555}[]{#_Toc87852434}[]{#_Toc87853213}[]{#_Toc87853994}[]{#_Toc87868051}[]{#_Toc87442759}[]{#_Toc87787556}[]{#_Toc87852435}[]{#_Toc87853214}[]{#_Toc87853995}[]{#_Toc87868052}[]{#_Toc87442760}[]{#_Toc87787557}[]{#_Toc87852436}[]{#_Toc87853215}[]{#_Toc87853996}[]{#_Toc87868053}[]{#_Toc87442761}[]{#_Toc87787558}[]{#_Toc87852437}[]{#_Toc87853216}[]{#_Toc87853997}[]{#_Toc87868054}[]{#_Toc87442762}[]{#_Toc87787559}[]{#_Toc87852438}[]{#_Toc87853217}[]{#_Toc87853998}[]{#_Toc87868055}[]{#_Toc87442763}[]{#_Toc87787560}[]{#_Toc87852439}[]{#_Toc87853218}[]{#_Toc87853999}[]{#_Toc87868056}[]{#_Toc87442764}[]{#_Toc87787561}[]{#_Toc87852440}[]{#_Toc87853219}[]{#_Toc87854000}[]{#_Toc87868057}[]{#_Toc87442765}[]{#_Toc87787562}[]{#_Toc87852441}[]{#_Toc87853220}[]{#_Toc87854001}[]{#_Toc87868058}[]{#_Toc87442766}[]{#_Toc87787563}[]{#_Toc87852442}[]{#_Toc87853221}[]{#_Toc87854002}[]{#_Toc87868059}[]{#_Toc87442767}[]{#_Toc87787564}[]{#_Toc87852443}[]{#_Toc87853222}[]{#_Toc87854003}[]{#_Toc87868060}[]{#_Toc87442768}[]{#_Toc87787565}[]{#_Toc87852444}[]{#_Toc87853223}[]{#_Toc87854004}[]{#_Toc87868061}[]{#_Toc87442769}[]{#_Toc87787566}[]{#_Toc87852445}[]{#_Toc87853224}[]{#_Toc87854005}[]{#_Toc87868062}[]{#_Toc87442770}[]{#_Toc87787567}[]{#_Toc87852446}[]{#_Toc87853225}[]{#_Toc87854006}[]{#_Toc87868063}[]{#_Toc87442771}[]{#_Toc87787568}[]{#_Toc87852447}[]{#_Toc87853226}[]{#_Toc87854007}[]{#_Toc87868064}[]{#_Toc87442772}[]{#_Toc87787569}[]{#_Toc87852448}[]{#_Toc87853227}[]{#_Toc87854008}[]{#_Toc87868065}[]{#_Toc87442773}[]{#_Toc87787570}[]{#_Toc87852449}[]{#_Toc87853228}[]{#_Toc87854009}[]{#_Toc87868066}[]{#_Toc87442774}[]{#_Toc87787571}[]{#_Toc87852450}[]{#_Toc87853229}[]{#_Toc87854010}[]{#_Toc87868067}[]{#_Toc87442775}[]{#_Toc87787572}[]{#_Toc87852451}[]{#_Toc87853230}[]{#_Toc87854011}[]{#_Toc87868068}[]{#_Toc87442776}[]{#_Toc87787573}[]{#_Toc87852452}[]{#_Toc87853231}[]{#_Toc87854012}[]{#_Toc87868069}[]{#_Toc87442777}[]{#_Toc87787574}[]{#_Toc87852453}[]{#_Toc87853232}[]{#_Toc87854013}[]{#_Toc87868070}[]{#_Toc87442778}[]{#_Toc87787575}[]{#_Toc87852454}[]{#_Toc87853233}[]{#_Toc87854014}[]{#_Toc87868071}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1773354260}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1668418851}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim timer hello 40]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1950022140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer hello]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_1659714527}
:::

::: {#-1113947205 .myid}
[]{#_Toc404790467}[]{#struct_0_x1176_16249_814764609}[]{#_Toc311538877}[]{#_Toc293993805}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim timer join-prune**

------------------------------------------------------------------------

[**[ipv6 pim timer join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_x1993379780}[命令用来在接口上配置发送加入]{style="font-family:
宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔。]{style="font-family:
宋体"}

[**[undo ipv6 pim timer join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_1833698999}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1465140808}

[**[ipv6 pim timer join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_x1745701521}[ ]{lang="EN-US"}*[interval]{lang="EN-US"}*

[[undo ipv6 pim timer join-prune]{lang="NO-BOK"}]{#struct_0_x1176_16249_597510097}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1946887135}

[[发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_1575680968}[剪枝报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1138701502}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_512794655}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993445316}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1303616314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1410986787}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1877476329}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_x420863990}[：]{style="font-family:宋体"}[指定发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x702914636}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_x1176_16249_1021363251}[IPv6 PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。]{style="font-family:宋体"}]{#struct_0_x1176_16249_x152293340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x152358876}[接口向上游邻居发送加入]{style="font-family:
宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x77753903}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_2061101293}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1993248708}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1230612768}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim timer join-prune 80]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_1857762885}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1662960782}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1145159821}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim timer join-prune 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_822178093}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim holdtime join-prune]{lang="EN-US"}]{#struct_0_x1176_16249_x152162268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer join-prune]{lang="EN-US"}**[ (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_220024163}
:::

::: {#-1503314029 .myid}
[]{#_Toc404790468}[]{#struct_0_x1176_16249_x1993314244}[]{#_Toc311538878}[]{#_Toc293993806}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ipv6 pim triggered-hello-delay**

------------------------------------------------------------------------

[**[ipv6 pim triggered-hello-delay]{lang="EN-US"}**]{#struct_0_x1176_16249_1264002128}[命令用来配置触发]{style="font-family:
宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间。]{style="font-family:宋体"}

[**[undo ipv6 pim triggered-hello-delay]{lang="EN-US"}**]{#struct_0_x1176_16249_x1793639164}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_361312063}

[**[ipv6 pim triggered-hello-delay]{lang="EN-US"}**[ *delay*]{lang="EN-US"}]{#struct_0_x1176_16249_1765604480}

[[undo ipv6 pim triggered-hello-delay]{lang="IT"}]{#struct_0_x1176_16249_x1915542019}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1015034954}

[[触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_922741462}[报文的最大延迟时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1438219930}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1993117636}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2006577782}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x360462659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1725298051}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_233192835}

[*[delay]{lang="EN-US"}*]{#struct_0_x1176_16249_x699880412}[：指定触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x13162839}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1176_16249_x548501580}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x196049455}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1993183172}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 pim triggered-hello-delay 3]{lang="EN-US"}

[]{#struct_0_x1176_16249_1296104552}[]{#_Toc87787580}[]{#_Toc87852459}[]{#_Toc87853238}[]{#_Toc87854019}[]{#_Toc87868076}[]{#_Toc87787581}[]{#_Toc87852460}[]{#_Toc87853239}[]{#_Toc87854020}[]{#_Toc87868077}[]{#_Toc87787582}[]{#_Toc87852461}[]{#_Toc87853240}[]{#_Toc87854021}[]{#_Toc87868078}[]{#_Toc87787583}[]{#_Toc87852462}[]{#_Toc87853241}[]{#_Toc87854022}[]{#_Toc87868079}[]{#_Toc87787584}[]{#_Toc87852463}[]{#_Toc87853242}[]{#_Toc87854023}[]{#_Toc87868080}[]{#_Toc87787585}[]{#_Toc87852464}[]{#_Toc87853243}[]{#_Toc87854024}[]{#_Toc87868081}[]{#_Toc87787586}[]{#_Toc87852465}[]{#_Toc87853244}[]{#_Toc87854025}[]{#_Toc87868082}[]{#_Toc87787587}[]{#_Toc87852466}[]{#_Toc87853245}[]{#_Toc87854026}[]{#_Toc87868083}[]{#_Toc87787588}[]{#_Toc87852467}[]{#_Toc87853246}[]{#_Toc87854027}[]{#_Toc87868084}[]{#_Toc87787589}[]{#_Toc87852468}[]{#_Toc87853247}[]{#_Toc87854028}[]{#_Toc87868085}[]{#_Toc87787590}[]{#_Toc87852469}[]{#_Toc87853248}[]{#_Toc87854029}[]{#_Toc87868086}[]{#_Toc87787592}[]{#_Toc87852471}[]{#_Toc87853250}[]{#_Toc87854031}[]{#_Toc87868088}[]{#_Toc87787593}[]{#_Toc87852472}[]{#_Toc87853251}[]{#_Toc87854032}[]{#_Toc87868089}[]{#_Toc87787594}[]{#_Toc87852473}[]{#_Toc87853252}[]{#_Toc87854033}[]{#_Toc87868090}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_812460799}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1870256277}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 pim triggered-hello-delay 3]{lang="EN-US"}
:::

::: {#-478959173 .myid}
[]{#_Toc311538879}[]{#_Toc323281753}[]{#_Toc321403848}[]{#_Toc293993414}[]{#_Toc404790469}[]{#struct_0_x1176_16249_x783748884}[]{#_Toc311538866}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- jp-pkt-size (IPv6 PIM view)**

------------------------------------------------------------------------

[**[jp-pkt-size]{lang="EN-US"}**]{#struct_0_x1176_16249_528588860}[命令用来配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的最大长度。]{style="font-family:宋体"}

[**[undo jp-pkt-size]{lang="EN-US"}**]{#struct_0_x1176_16249_x339034066}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x27324607}

[**[jp-pkt-size]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x1176_16249_x1992986564}

[[undo jp-pkt-size]{lang="EN-US"}]{#struct_0_x1176_16249_517739243}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1664617823}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_x894204988}[剪枝报文的最大长度为]{style="font-family:宋体"}[8100]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1110771737}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_711894213}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1180761259}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_647792133}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_51028875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1993052100}

[*[size]{lang="EN-US"}*]{#struct_0_x1176_16249_798458695}[：指定加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的最大长度，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[64000]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_527582852}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x840663611}[在公网实例中配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的最大长度为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x206529292}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] jp-pkt-size 1500]{lang="EN-US"}
:::

::: {#-602088370 .myid}
[]{#_Toc404790470}[]{#struct_0_x1176_16249_x708179265}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- register-policy (IPv6 PIM view)**

------------------------------------------------------------------------

[**[register-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x1391785393}[命令用来配置注册报文的过滤策略。]{style="font-family:宋体"}

[**[undo register-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_1479413033}[命令用来删除注册报文的过滤策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1992855492}

[**[register-policy ]{lang="EN-US"}***[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_x1413190601}

[[undo register-policy]{lang="EN-US"}]{#struct_0_x1176_16249_1144851314}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x409356440}

[[没有配置注册报文的过滤策略。]{style="font-family:宋体"}]{#struct_0_x1176_16249_1759238715}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x633943509}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x2032248942}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1709156106}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x187167488}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1992921028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1505980518}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_x1319230783}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_222124442}

[[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_1006392495}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定注册报文中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源地址范围，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[参数用来指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。只有与该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[语句匹配的注册报文才会被]{style="font-family:宋体"}[RP]{lang="EN-US"}[接受。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x159761712}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1010400786}[在公网实例中配置]{style="font-family:宋体"}[RP]{lang="EN-US"}[上对注册报文的过滤策略，只接收来自]{style="font-family:宋体"}[3:1::/64]{lang="EN-US"}[网段的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源发向]{style="font-family:宋体"}[FF0E:13::/64]{lang="EN-US"}[网段的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组的注册报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x427295836}

[\[Sysname\] acl ipv6 number 3000]{lang="EN-US"}

[\[Sysname-acl6-adv-3000\] rule permit ipv6 source 3:1:: 64 destination ff0e:13:: 64]{lang="EN-US"}

[\[Sysname-acl6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] register-policy 3000]{lang="EN-US"}
:::

::: {#274867497 .myid}
[]{#_Toc404790471}[]{#struct_0_x1176_16249_x151769052}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- register-suppression-timeout (IPv6 PIM view)**

------------------------------------------------------------------------

[**[register-suppression-timeout]{lang="EN-US"}**]{#struct_0_x1176_16249_x151834588}[命令用来配置注册抑制时间。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **register-suppression-timeout**]{lang="EN-US"}]{#struct_0_x1176_16249_x368435031}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2063925270}

[**[register-suppression-timeout]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1176_16249_x1545862439}

[**[undo]{lang="EN-US"}**[ **register-suppression-timeout**]{lang="EN-US"}]{#struct_0_x1176_16249_x2063859734}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x44944409}

[[注册抑制时间为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_x1176_16249_x2063794198}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x458826615}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_964704106}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2063728662}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1370680339}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x2064187414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1238728546}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_x2064121878}[：指定注册抑制时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x636770280}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1244586685}[在公网实例中配置注册抑制时间为]{style="font-family:宋体"}[70]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x2064056342}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] register-suppression-timeout 70]{lang="EN-US"}
:::

::: {#-844511274 .myid}
[]{#_Toc404790472}[]{#struct_0_x1176_16249_x1907186974}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- register-whole-checksum (IPv6 PIM view)**

------------------------------------------------------------------------

[**[register-whole-checksum]{lang="EN-US"}**]{#struct_0_x1176_16249_1965822910}[命令用来配置根据注册报文的全部内容来计算校验和。]{style="font-family:宋体"}

[**[undo register-whole-checksum]{lang="EN-US"}**]{#struct_0_x1176_16249_1806908409}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1874708379}

[[register-whole-checksum]{lang="EN-US"}]{#struct_0_x1176_16249_x1751871531}

[[undo register-whole-checksum]{lang="EN-US"}]{#struct_0_x1176_16249_114194247}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1819826556}

[[仅根据注册报文头来计算校验和。]{style="font-family:宋体"}]{#struct_0_x1176_16249_x427361372}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_486438297}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1631135705}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1649069556}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_642014541}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1469138904}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x573824455}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x731982485}[在公网实例中配置根据注册报文的全部内容来计算校验和。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x427164764}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] register-whole-checksum]{lang="EN-US"}
:::

::: {#1763173942 .myid}
[]{#_Toc404790473}[]{#struct_0_x1176_16249_x2063400982}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- snmp-agent trap enable pim6**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **pim6**]{lang="EN-US"}]{#struct_0_x1176_16249_1984440736}[命令用来开启]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **pim6**]{lang="EN-US"}]{#struct_0_x1176_16249_x2063335446}[命令用来关闭]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_21186656}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **pim6** \[ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** \] \*]{lang="EN-US"}]{#struct_0_x1176_16249_x2063925269}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **pim6** \[ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** \] \*]{lang="EN-US"}]{#struct_0_x1176_16249_1539185740}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2063859733}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1967258710}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2063794197}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1176_16249_x2024910556}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x865857105}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x2063728661}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1358203016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2064187413}

[**[candidate-bsr-win-election]{lang="EN-US"}**]{#struct_0_x1176_16249_x1642013073}[：表示]{style="font-family:
宋体"}[C-BSR]{lang="EN-US"}[成功当选]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}

[**[elected-bsr-lost-election]{lang="EN-US"}**]{#struct_0_x1176_16249_x2064121877}[：表示原]{style="font-family:
宋体"}[BSR]{lang="EN-US"}[在新的选举中失败的告警信息。]{style="font-family:宋体"}

[**[neighbor-loss]{lang="EN-US"}**]{#struct_0_x1176_16249_573083301}[：表示邻居丢失的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2064056341}

[[如果未指定任何可选参数，表示开启或关闭]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1767435579}[的全部告警功能。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1497864781}[的告警功能之后，]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2063990805}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x339068319}[关闭]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[的全部告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x2063400981}

[\[Sysname\] undo snmp-agent trap enable pim6]{lang="EN-US"}
:::

::: {#-1769336329 .myid}
[]{#_Toc404790474}[]{#struct_0_x1176_16249_x1037619613}[]{#_Toc311538880}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- source-lifetime (IPv6 PIM view)**

------------------------------------------------------------------------

[**[source-lifetime]{lang="EN-US"}**]{#struct_0_x1176_16249_1148803284}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的生存时间。]{style="font-family:宋体"}

[**[undo source-lifetime]{lang="EN-US"}**]{#struct_0_x1176_16249_1265552955}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1363295324}

[**[source-lifetime]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1176_16249_1618516755}

[[undo source-lifetime]{lang="EN-US"}]{#struct_0_x1176_16249_x211030606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1019597241}

[[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_1740929305}[组播源的生存时间为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x427230300}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_2041708726}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1604246544}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x458027675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1764179611}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1072854995}

[*[time]{lang="EN-US"}*]{#struct_0_x1176_16249_x991099278}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的生存时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31536000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源永不老化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1698433995}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x30082464}[在公网实例中配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源的生存时间为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x427033692}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] source-lifetime 200]{lang="EN-US"}
:::

::: {#1973785565 .myid}
[]{#_Toc404790475}[]{#struct_0_x1176_16249_x1082696132}[]{#_Toc311538881}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- source-policy (IPv6 PIM view)**

------------------------------------------------------------------------

[**[source-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x162913459}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据过滤器。]{style="font-family:宋体"}

[**[undo source-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_1785626487}[命令用来删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_318726253}

[**[source-policy]{lang="EN-US"}**[ *acl6-number*]{lang="EN-US"}]{#struct_0_x1176_16249_x887257735}

[[undo source-policy]{lang="EN-US"}]{#struct_0_x1176_16249_200647190}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x512848760}

[[没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_x427099228}[组播数据过滤器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1136911895}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x1903460554}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1320651652}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1475070625}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_2095265033}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x78861894}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_1983684695}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1776830883}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1176_16249_x426902620}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文的源地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以]{lang="EN-US" style="font-family:宋体"}[外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x1176_16249_1999891185}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文的源地址范围，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[参数用来指定组播组地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以]{lang="EN-US" style="font-family:宋体"}[外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，新配置将覆盖旧配置。]{style="font-family:宋体"}]{#struct_0_x1176_16249_735830802}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1595846656}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x2134294305}[在公网实例中配置接收]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源]{style="font-family:宋体"}[3121::1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文，丢弃]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播源]{style="font-family:宋体"}[3121::2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_687324869}

[\[Sysname\] acl ipv6 number 2000]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] rule permit source 3121::1 128]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] rule deny source 3121::2 128]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] source-policy 2000]{lang="EN-US"}

[\[Sysname-pim6\] quit]{lang="EN-US"}
:::

::: {#1308880610 .myid}
[]{#_Toc404790476}[]{#struct_0_x1176_16249_1479373425}[]{#_Toc311538882}[]{#_Toc308164995}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- spt-switch-threshold (IPv6 PIM view)**

------------------------------------------------------------------------

[**[spt-switch-threshold]{lang="EN-US"}**]{#struct_0_x1176_16249_x426968156}[命令用来配置发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换的条件。]{style="font-family:宋体"}

[**[undo spt-switch-threshold]{lang="EN-US"}**]{#struct_0_x1176_16249_x1905285486}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_411183681}

[**[spt-switch-threshold]{lang="EN-US"}**[ { *traffic-rate* \| **immediacy** \| **infinity** } \[ **group-policy** *acl6-number* \]]{lang="EN-US"}]{#struct_0_x1176_16249_965203953}

[**[undo spt-switch-threshold]{lang="EN-US"}**[ \[ *traffic-rate \|* **immediacy** \| **infinity** \] \[ **group-policy** *acl6-number* \]]{lang="EN-US"}]{#struct_0_x1176_16249_x761892136}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1883769600}

[[设备收到第一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1176_16249_2005157588}[组播数据包后便立即向]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1214352159}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x426771548}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1229092370}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_402070811}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1863959577}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_951657067}

[*[traffic-rate]{lang="EN-US"}*]{#struct_0_x1176_16249_x2073681242}[：指定发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据转发速率阈值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4194304]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。交换机不支持本参数。]{style="font-family:宋体"}

[**[immediacy]{lang="EN-US"}**]{#struct_0_x1176_16249_1095002481}[：表示立即发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换。]{style="font-family:宋体"}

[**[infinity]{lang="EN-US"}**]{#struct_0_x1176_16249_x60854417}[：表示永不发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换。]{style="font-family:宋体"}

[**[group-policy]{lang="EN-US"}**[ *acl6-number*]{lang="EN-US"}]{#struct_0_x1176_16249_802538419}[：表示组策略列表中的一项，与该组策略匹配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组将应用本配置。]{style="font-family:宋体"}*[acl6-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果未指定本参数指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则本配置将应用于所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x426837084}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_1249545545}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组地址范围，]{style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，可以配置多个]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1776425634}[SPT]{lang="EN-US"}[切换阈值。但是，如果配置时所指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则相同，则新配置将覆盖旧配置；如果对同一]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组存在多条配置，则按照配置顺序匹配到的第一条配置将生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于某些设备无法将]{style="font-family:宋体"}]{#struct_0_x1176_16249_x855734855}[IPv6]{lang="EN-US"}[组播报文封装在注册报文中发给]{style="font-family:宋体"}[RP]{lang="EN-US"}[，因此在可能成为]{style="font-family:宋体"}[RP]{lang="EN-US"}[的设备上不建议配置永不发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换，以免导致]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播报文转发失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1843716035}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x89022396}[在公网实例中配置发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播数据转发速率阈值为]{style="font-family:宋体"}[4kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_724617132}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] spt-switch-threshold 4]{lang="EN-US"}

[]{#struct_0_x1176_16249_700096206}[]{#_Toc323215037}[\# ]{lang="EN-US"}[在接收者侧]{style="font-family:
宋体"}[DR]{lang="EN-US"}[的公网实例中配置永不发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换。]{style="font-family:宋体"}[]{#_Toc323215038}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x427295835}[]{#_Toc323215039}

[\[Sysname\] []{#_Toc323215040}ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] spt-switch-threshold infinity]{lang="EN-US"}[]{#_Toc323215041}
:::

::: {#-569769684 .myid}
[]{#_Toc311538883}[]{#_Toc305165304}[]{#_Toc323281758}[]{#_Toc319654954}[]{#_Toc318291838}[]{#_Toc323281760}[]{#_Toc319654956}[]{#_Toc318291840}[]{#_Toc293993424}[]{#_Toc404790477}[]{#struct_0_x1176_16249_x1907252510}[]{#_Toc331681348}[]{#_Toc331681118}[]{#_Toc306713406}[]{#_Toc293993421}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- ssm-policy (IPv6 PIM view)**

------------------------------------------------------------------------

[**[ssm-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x2061270073}[命令用来配置]{style="font-family:宋体"}[IPv6 SSM]{lang="EN-US"}[组播组的范围。]{style="font-family:宋体"}

[**[undo ssm-policy]{lang="EN-US"}**]{#struct_0_x1176_16249_x274938377}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1906662919}

[**[ssm-policy ]{lang="EN-US"}***[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_186333809}

[[undo ssm-policy]{lang="EN-US"}]{#struct_0_x1176_16249_x200429808}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_871369429}

[[IPv6 SSM]{lang="EN-US"}]{#struct_0_x1176_16249_x427361371}[组播组的范围为]{style="font-family:宋体"}[FF3x::/32]{lang="EN-US"}[，其中]{style="font-family:宋体"}[x]{lang="EN-US"}[表示任意合法的]{style="font-family:宋体"}[scope]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_486241689}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1335163624}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1028753813}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1689227601}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1310337660}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2110790727}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_2128324371}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1026995}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_x427164763}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US"}[SSM]{lang="EN-US"}[组播组范围，]{style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令可以定义允许或拒绝的]{style="font-family:宋体"}]{#struct_0_x1176_16249_x1037816221}[IPv6]{lang="EN-US"}[组播组的地址范围：如果匹配通过，则组播运行模式为]{style="font-family:宋体"}[IPv6 PIM-SSM]{lang="EN-US"}[，否则为]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_825639438}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1231580311}[配置]{style="font-family:宋体"}[IPv6 SSM]{lang="EN-US"}[组播组的范围为]{style="font-family:宋体"}[FF3E:0:8192::/96]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x856222599}

[\[Sysname\] acl ipv6 number 2000]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] rule permit source ff3e:0:8192:: 96]{lang="EN-US"}

[\[Sysname-acl6-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] ssm-policy 2000]{lang="EN-US"}
:::

::: {#-1063287539 .myid}
[]{#_Toc404790478}[]{#struct_0_x1176_16249_x865662808}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- state-refresh-hoplimit (IPv6 PIM view)**

------------------------------------------------------------------------

[**[state-refresh-hoplimit]{lang="EN-US"}**]{#struct_0_x1176_16249_44632764}[命令用来配置状态刷新报文的]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo state-refresh-hoplimit]{lang="EN-US"}**]{#struct_0_x1176_16249_x427230299}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_85983405}

[**[state-refresh-hoplimit ]{lang="EN-US"}***[hoplimit-value]{lang="EN-US"}*]{#struct_0_x1176_16249_1575963066}

[[undo state-refresh-hoplimit]{lang="EN-US"}]{#struct_0_x1176_16249_x817387392}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1428601120}

[[状态刷新报文的]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}]{#struct_0_x1176_16249_x1725842302}[值为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1940613518}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x76852902}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1736175849}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x427033691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1082499524}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_956250643}

[*[hoplimit-value]{lang="EN-US"}*]{#struct_0_x1176_16249_1100688627}[：指定状态刷新报文的]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1563113346}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1166885074}[在公网实例中配置状态刷新报文的]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[值为]{style="font-family:宋体"}[45]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x56387120}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] state-refresh-hoplimit 45]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1518311010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim state-refresh-capable]{lang="EN-US"}]{#struct_0_x1176_16249_x427099227}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-interval (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x1136977431}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-rate-limit (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x128360044}
:::

::: {#-377987374 .myid}
[]{#_Toc404790479}[]{#struct_0_x1176_16249_359792891}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- state-refresh-interval (IPv6 PIM view)**

------------------------------------------------------------------------

[**[state-refresh-interval]{lang="EN-US"}**]{#struct_0_x1176_16249_x1054496182}[命令用来配置发送状态刷新报文的时间间隔。]{style="font-family:宋体"}

[**[undo state-refresh-interval]{lang="EN-US"}**]{#struct_0_x1176_16249_x1745905526}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_452520448}

[**[state-refresh-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_x1567535942}

[[undo state-refresh-interval]{lang="EN-US"}]{#struct_0_x1176_16249_x426902619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2000349940}

[[发送状态刷新报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_x1176_16249_x954650571}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x181144884}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x924641589}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1523676733}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_911034982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_929911695}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1412980689}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_x426968155}[：指定发送状态刷新报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1905482094}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1428231027}[在公网实例中配置发送状态刷新报文的时间间隔为]{style="font-family:宋体"}[70]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x1284593477}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] state-refresh-interval 70]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_89962685}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim state-refresh-capable]{lang="EN-US"}]{#struct_0_x1176_16249_x2120506141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-rate-limit (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x1295312156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-hoplimit (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x370567288}
:::

::: {#361096619 .myid}
[]{#_Toc404790480}[]{#struct_0_x1176_16249_x426771547}[]{#_Toc323281759}[]{#_Toc319654955}[]{#_Toc318291839}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- state-refresh-rate-limit (IPv6 PIM view)**

------------------------------------------------------------------------

[**[state-refresh-rate-limit]{lang="EN-US"}**]{#struct_0_x1176_16249_1229813266}[命令用来配置接收新状态刷新报文的等待时间。]{style="font-family:
宋体"}

[**[undo state-refresh-rate-limit]{lang="EN-US"}**]{#struct_0_x1176_16249_1192071343}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x943004650}

[**[state-refresh-rate-limit ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_x1176_16249_x1715913223}

[[undo state-refresh-rate-limit]{lang="EN-US"}]{#struct_0_x1176_16249_859018275}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1469085405}

[[接收新状态刷新报文的等待时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x1176_16249_575304186}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_632594287}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x426837083}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1249742153}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1717525060}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1300259408}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1424244127}

[*[time]{lang="EN-US"}*]{#struct_0_x1176_16249_x555916876}[：指定接收新状态刷新报文的等待时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_288896840}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x1520057136}[在公网实例中配置接收新状态刷新报文的等待时间为]{style="font-family:宋体"}[45]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_x427295838}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] state-refresh-rate-limit 45]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1907055902}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim state-refresh-capable]{lang="EN-US"}]{#struct_0_x1176_16249_x768971511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-interval (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x638413246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state-refresh-hoplimit (IPv6 PIM view)]{lang="EN-US"}]{#struct_0_x1176_16249_x501459151}
:::

::: {#1265838218 .myid}
[]{#_Toc404790481}[]{#struct_0_x1176_16249_491981529}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- static-rp (IPv6 PIM view)**

------------------------------------------------------------------------

[**[static-rp]{lang="EN-US"}**]{#struct_0_x1176_16249_x1085322108}[命令用来配置静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo static-rp]{lang="EN-US"}**]{#struct_0_x1176_16249_x474401961}[命令用来删除静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x427361374}

[**[static-rp]{lang="EN-US"}***[ ipv6-rp-address]{lang="EN-US"}*[ \[ *acl6-number* \| **bidir** \| **preferred** \] \*]{lang="EN-US"}]{#struct_0_x1176_16249_486569369}

[**[undo static-rp]{lang="EN-US"}**[ *ipv6-rp-address*]{lang="EN-US"}]{#struct_0_x1176_16249_1188928857}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_82825592}

[[没有配置静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_x1176_16249_329594940}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x2137639535}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x108063762}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x895255583}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1146584244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x427164766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1037488541}

[*[ipv6-rp-address]{lang="EN-US"}*]{#struct_0_x1176_16249_1467247088}[：指定静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。该地址必须是合法的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_x1176_16249_1839891523}[：指定基本]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果指定了本参数，该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[将只为能够通过该过滤规则的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组服务；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[将为所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组服务。]{style="font-family:宋体"}

[**[bidir]{lang="EN-US"}**]{#struct_0_x1176_16249_1643683706}[：指定该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[服务于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果未指定本参数，该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[将服务于]{style="font-family:宋体"}[IPv6 PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[preferred]{lang="EN-US"}**]{#struct_0_x1176_16249_x900477192}[：表示当网络中同时存在动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[和静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[时，优先选择静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[，只有当静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[失效时，动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[才能生效。如果未指定本参数，则表示优先选择动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[，只有当未配置动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[或动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[失效时，静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[才能生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1675251514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[作为静态]{style="font-family:宋体"}]{#struct_0_x1176_16249_801882286}[RP]{lang="EN-US"}[的接口不必使能]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_x1176_16249_x1775946110}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[所服务的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组范围，]{style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当某个静态]{style="font-family:宋体"}]{#struct_0_x1176_16249_x427230302}[RP]{lang="EN-US"}[引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则发生变化时，需要为所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组重新选举]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，可以配置多个静态]{style="font-family:宋体"}]{#struct_0_x1176_16249_2041577654}[RP]{lang="EN-US"}[。但是，如果配置时所指定的静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则相同，则新配置将覆盖旧配置；如果存在多个静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[服务于同一组播组的情况，则选择]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址最大的静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[为该组服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1483214732}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x746323670}[在公网实例中配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::2]{lang="EN-US"}[的接口为静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[，为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播组]{style="font-family:宋体"}[FF03::101/64]{lang="EN-US"}[提供服务，并优先选择静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1764007018}

[\[Sysname\] acl ipv6 number 2001]{lang="EN-US"}

[\[Sysname-acl6-basic-2001\] rule permit source ff03::101 64]{lang="EN-US"}

[\[Sysname-acl6-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] static-rp 2001::2 2001 preferred]{lang="EN-US"}

[]{#_Toc311538884}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_427983881}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[display ipv6 pim rp-info]{lang="EN-US"}]{#struct_0_x1176_16249_x1164281403}
:::

::: {#1784465819 .myid}
[]{#_Toc404790482}[]{#struct_0_x1176_16249_x427033694}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- timer hello (IPv6 PIM view)**

------------------------------------------------------------------------

[**[timer hello]{lang="EN-US"}**]{#struct_0_x1176_16249_x1082827204}[命令用来全局配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo timer hello]{lang="EN-US"}**]{#struct_0_x1176_16249_1881366629}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x237739827}

[**[timer hello]{lang="EN-US"}**]{#struct_0_x1176_16249_1079710453}[ ]{lang="EN-US"}*[interval]{lang="EN-US"}*

[[undo timer hello]{lang="NO-BOK"}]{#struct_0_x1176_16249_1330459819}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_518341843}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1176_16249_x1041055205}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1948240964}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x427099230}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1137436184}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_1077381261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x1629699955}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1435018187}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_1890666605}[：指定发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x482197087}

[[本配置既可在]{style="font-family:宋体"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_1568907824}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1329823005}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_x426902622}[在公网实例中全局配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1999760113}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] timer hello 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x853911475}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6 pim timer hello]{lang="EN-US"}]{#struct_0_x1176_16249_x216957362}
:::

::: {#69661695 .myid}
[]{#_Toc404790483}[]{#struct_0_x1176_16249_x1731770473}[]{#_Toc311538885}

**IPv6 PIM \-- IPv6 PIM配置命令 \-- timer join-prune (IPv6 PIM view)**

------------------------------------------------------------------------

[**[timer join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_1305805483}[命令用来全局配置发送加入]{style="font-family:宋体"}[/]{lang="FR"}[剪枝报文的时间间隔。]{style="font-family:宋体"}

[**[undo timer join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_1945987569}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1821508694}

[**[timer join-prune]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1176_16249_x426968158}

[[undo timer join-prune]{lang="EN-US"}]{#struct_0_x1176_16249_x1906202990}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1658509793}

[[发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1176_16249_1550753186}[剪枝报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x1851734298}

[[IPv6 PIM]{lang="FR"}]{#struct_0_x1176_16249_1997979070}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1176_16249_2100444694}

[[network-admin]{lang="EN-US"}]{#struct_0_x1176_16249_414444114}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1176_16249_x426771550}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1229616659}

[*[interval]{lang="EN-US"}*]{#struct_0_x1176_16249_x332707229}[：]{style="font-family:宋体"}[指定发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[18000]{lang="FR"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1176601831}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_x1176_16249_541900839}[IPv6 PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。]{style="font-family:宋体"}]{#struct_0_x1176_16249_x2063925274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 PIM]{lang="EN-US"}]{#struct_0_x1176_16249_x2063859738}[接口向上游邻居发送加入]{style="font-family:
宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1176_16249_1055234304}

[[\# ]{lang="EN-US"}]{#struct_0_x1176_16249_1520390887}[在公网实例中全局配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1176_16249_1420833786}

[\[Sysname\] ipv6 pim]{lang="EN-US"}

[\[Sysname-pim6\] timer join-prune 80]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1176_16249_x426837086}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[holdtime join-prune]{lang="EN-US"}**[ (]{lang="EN-US"}]{#struct_0_x1176_16249_x2063794202}[IPv6 ]{lang="EN-US"}[PIM view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 pim timer join-prune]{lang="EN-US"}**]{#struct_0_x1176_16249_1249414473}
:::
