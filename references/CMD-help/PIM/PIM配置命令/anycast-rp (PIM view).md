::: {#-746170871 .myid}
[]{#_Toc404789743}[]{#struct_0_17565_x2166_1868542527}[]{#_Toc359414301}

**PIM \-- PIM配置命令 \-- anycast-rp (PIM view)**

------------------------------------------------------------------------

[**[anycast-rp]{lang="EN-US"}**]{#struct_0_17565_x2166_x1060750243}[命令用来配置]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo anycast-rp]{lang="EN-US"}**]{#struct_0_17565_x2166_1329726242}[命令用来删除]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1868608063}

[**[anycast-rp]{lang="EN-US"}***[ anycast-rp-address member-address]{lang="EN-US"}*]{#struct_0_17565_x2166_148025004}

[**[undo anycast-rp]{lang="EN-US"}**[ *anycast-rp-address member-address*]{lang="EN-US"}]{#struct_0_17565_x2166_1730967480}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x542460374}

[[没有配置]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}]{#struct_0_17565_x2166_1869197887}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_468747234}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x703891008}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1869263423}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_109687261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x208638354}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1868673598}

[*[anycast-rp-address]{lang="EN-US"}*]{#struct_0_17565_x2166_1670099298}[：指定]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[地址。必须是除]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段以外的合法单播]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[member-address]{lang="EN-US"}*]{#struct_0_17565_x2166_293084044}[：指定]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[成员地址。必须是除]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段以外的合法单播]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，不能与]{style="font-family:宋体"}*[anycast-rp-address]{lang="EN-US"}*[相同。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1868739134}

[[本命令可重复配置，配置时如果指定了相同的]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}]{#struct_0_17565_x2166_923083569}[地址，则将]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[成员地址添加到该]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[集中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1949863767}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1868804670}[在公网实例中配置如下]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[集：]{style="font-family:宋体"}[Anycast-RP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.0.0]{lang="EN-US"}[，两个成员的地址分别为]{style="font-family:宋体"}[1.1.0.1]{lang="EN-US"}[和]{style="font-family:宋体"}[1.2.0.1]{lang="EN-US"}[（前者为本地接口]{style="font-family:宋体"}[LoopBack1]{lang="EN-US"}[的地址）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1683039541}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] anycast-rp 1.1.0.0 1.1.0.1]{lang="EN-US"}

[\[Sysname-pim\] anycast-rp 1.1.0.0 1.2.0.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1868870206}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_17565_x2166_117199556}**[ ]{lang="EN-US"}[pim]{lang="EN-US"}[ ]{lang="EN-US"}[rp-info]{lang="EN-US"}**
:::

::: {#554987053 .myid}
[]{#_Toc80176797}[]{#_Toc288743017}[]{#_Toc94588251}[]{#_Toc78346636}[]{#_Toc311539003}[]{#_Toc404789744}[]{#struct_0_17565_x2166_229155558}[]{#_Toc345338657}

**PIM \-- PIM配置命令 \-- bidir-pim enable (PIM view)**

------------------------------------------------------------------------

[**[bidir-pim]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_437758488}[命令用来使能双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bidir-pim** **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_685896331}[命令用来关闭双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_145533537}

[**[bidir-pim]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_x1493180884}

[**[undo]{lang="EN-US"}**[ **bidir-pim** **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_x1560639478}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1271308868}

[[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1989185477}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2132516696}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1016914050}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1352741488}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x952127803}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1595130313}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2116462452}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17565_x2166_473276576}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1286650231}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1989251013}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并使能双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x731776857}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] bidir-pim enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2087388798}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast routing]{lang="EN-US"}**]{#struct_0_17565_x2166_428489141}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#-2018724885 .myid}
[]{#_Toc404789745}[]{#struct_0_17565_x2166_1581897123}[]{#_Toc345338658}[]{#_Toc341772846}

**PIM \-- PIM配置命令 \-- bidir-rp-limit (PIM view)**

------------------------------------------------------------------------

[**[bidir-rp-limit]{lang="EN-US"}**]{#struct_0_17565_x2166_x465906628}[命令用来配置双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的最大数目。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bidir-rp-limit**]{lang="EN-US"}]{#struct_0_17565_x2166_x17375927}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1567090990}

[**[bidir-rp-limit]{lang="EN-US"}**[ *limit*]{lang="EN-US"}]{#struct_0_17565_x2166_x1988792261}

[**[undo]{lang="EN-US"}**[ **bidir-rp-limit**]{lang="EN-US"}]{#struct_0_17565_x2166_1610498862}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x860182154}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1672934924}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1623173866}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x2126016105}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1781760211}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1627049624}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_27269206}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_700654521}

[*[limit]{lang="EN-US"}*]{#struct_0_17565_x2166_x1988857797}[：指定双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的最大数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[到系统所允许的最大值。系统所允许的最大值会随设备的不同而有所差别，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1918907601}

[[由于双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1279171315}[为每个]{style="font-family:宋体"}[RP]{lang="EN-US"}[都要在所有]{style="font-family:宋体"}[PIM]{lang="EN-US"}[接口上进行]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举，因此实际组网中不建议配置多个双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[。通过本命令可以限制双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的数目，超出限制值的]{style="font-family:宋体"}[RP]{lang="EN-US"}[不会生效，仅能进行]{style="font-family:宋体"}[DF]{lang="EN-US"}[选举而无法指导转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1557971022}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1436438704}[在公网实例中配置双向]{style="font-family:宋体"}[PIM RP]{lang="EN-US"}[的最大数目为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_598781299}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] bidir-rp-limit 3]{lang="EN-US"}
:::

::: {#-1618657990 .myid}
[]{#_Toc404789746}[]{#struct_0_17565_x2166_1910668231}

**PIM \-- PIM配置命令 \-- bsm-fragment enable (PIM view)**

------------------------------------------------------------------------

[**[bsm-fragment]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_1013819832}[命令用来使能自举报文语义分片功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bsm-fragment** **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_x2093599653}[命令用来关闭自举报文语义分片功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1988923333}

[**[bsm-fragment]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_1356428342}

[**[undo]{lang="EN-US"}**[ **bsm-fragment** **enable**]{lang="EN-US"}]{#struct_0_17565_x2166_x577517215}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1374112101}

[[自举报文语义分片功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_17565_x2166_x705356258}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1667816017}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1042215322}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_993518451}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1797693287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1988988869}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_192151549}

[[当]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}]{#struct_0_17565_x2166_x118499979}[域或双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[域中存在不支持自举报文语义分片的设备时，请关闭本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x872676641}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x518603161}[在公网实例中关闭自举报文语义分片功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_111703311}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] undo bsm-fragment enable]{lang="EN-US"}
:::

::: {#1606751436 .myid}
[]{#_Toc404789747}[]{#struct_0_17565_x2166_199731027}[]{#_Toc311539004}

**PIM \-- PIM配置命令 \-- bsr-policy (PIM view)**

------------------------------------------------------------------------

[**[bsr-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_509434063}[命令用来配置合法的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址范围，以防止]{style="font-family:宋体"}[BSR]{lang="EN-US"}[欺骗。]{style="font-family:宋体"}

[**[undo bsr-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_x76134449}[命令用来取消]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址范围的限制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1988530117}

[**[bsr-policy]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_17565_x2166_1654545475}

[**[undo]{lang="EN-US"}**[ **bsr-policy**]{lang="EN-US"}]{#struct_0_17565_x2166_315219299}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x124243149}

[[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_1425301123}[的地址范围不受任何限制，即认为来自任意源的自举报文都是合法的。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_596355232}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1620824991}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x511941341}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_665738850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1988595653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1392038816}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x1090936937}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x769964080}

[[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_x1833634788}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定合法]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的源地址]{style="font-family:宋体"}[范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x972338866}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1414111924}[在公网实例中配置合法的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[地址范围，只允许网段]{style="font-family:宋体"}[10.1.1.0/24]{lang="EN-US"}[中的设备充当]{style="font-family:宋体"}[BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1989054404}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 10.1.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] bsr-policy 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x470002060}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[c-bsr]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_788851407}
:::

::: {#1423540901 .myid}
[]{#_Toc404789748}[]{#struct_0_17565_x2166_1941581756}

**PIM \-- PIM配置命令 \-- c-bsr (PIM view)**

------------------------------------------------------------------------

[**[c-bsr]{lang="EN-US"}**]{#struct_0_17565_x2166_x15091765}[命令用来配置]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo c-bsr]{lang="EN-US"}**]{#struct_0_17565_x2166_1204404910}[命令用来删除]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1312688687}

[**[c-bsr]{lang="EN-US"}**[ *ip-address* \[ **scope** *group-address* { *mask-length* \| *mask* } \] \[ **hash-length** *hash-length* \| **priority** *priority* \] \*]{lang="EN-US"}]{#struct_0_17565_x2166_914808689}

[**[undo]{lang="EN-US"}**[ **c-bsr** *ip-address* \[ **scope** *group-address* { *mask-length* \| *mask* } \]]{lang="EN-US"}]{#struct_0_17565_x2166_x1897945661}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1611150669}

[[没有配置]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}]{#struct_0_17565_x2166_x1989119940}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1742272393}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_60709594}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x45937927}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_106832492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1900160605}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1410784309}

[*[ip-address]{lang="EN-US"}*]{#struct_0_17565_x2166_x434444975}[：指定]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[scope]{lang="EN-US"}**[ *group-address*]{lang="EN-US"}]{#struct_0_17565_x2166_x781184980}[：指定管理域]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[所服务的组播组地址，取值范围为]{style="font-family:宋体"}[239.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，表示配置服务于]{style="font-family:宋体"}[Global]{lang="EN-US"}[域的]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_17565_x2166_x1989185476}[：指定组播组地址的掩码长度，取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_17565_x2166_x596366659}[：指定组播组地址的掩码。]{style="font-family:宋体"}

[**[hash-length ]{lang="EN-US"}***[hash-length]{lang="EN-US"}*]{#struct_0_17565_x2166_1648168724}[：指定哈希掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_17565_x2166_1424222352}[：指定]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[64]{lang="EN-US"}[。数值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1757733541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C-BSR]{lang="EN-US"}]{#struct_0_17565_x2166_1842408289}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须有对应的本地接口，且该接口上必须使能]{style="font-family:宋体"}[PIM]{lang="EN-US"}[，否则配置不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果对同一个域多次执行本命令，新配置将覆盖旧配置；而针对不同域的]{style="font-family:宋体"}]{#struct_0_17565_x2166_392161330}[C-BSR]{lang="EN-US"}[则允许指定相同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2116712079}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_214234738}[在公网实例中将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的设备配置为]{style="font-family:宋体"}[Global]{lang="EN-US"}[域的]{style="font-family:宋体"}[C-BSR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1989251012}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] c-bsr 1.1.1.1]{lang="EN-US"}
:::

::: {#-1372017451 .myid}
[]{#_Toc404789749}[]{#struct_0_17565_x2166_1997106498}[]{#_Toc288743018}[]{#_Toc94588256}[]{#_Toc315856972}[]{#_Toc315859218}[]{#_Toc315856973}[]{#_Toc315859219}[]{#_Toc315856974}[]{#_Toc315859220}

**PIM \-- PIM配置命令 \-- c-rp (PIM view)**

------------------------------------------------------------------------

[**[c-rp]{lang="EN-US"}**]{#struct_0_17565_x2166_1289437629}[命令用来配置]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo c-rp]{lang="EN-US"}**]{#struct_0_17565_x2166_x1027287871}[命令用来删除]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_440756731}

[**[c-rp ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}*[\[ **advertisement-interval** *adv-interval* \| **group-policy** *acl-number* \| **holdtime** *hold-time* \| **priority** *priority* \] \* \[ **bidir** \]]{lang="EN-US"}]{#struct_0_17565_x2166_1928293594}

[**[undo c-rp]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_17565_x2166_2049610218}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1455110040}

[[没有配置]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_x1988792260}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_44414921}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_55855684}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x975256994}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1132379510}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x275167876}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_313805054}

[*[ip-address]{lang="EN-US"}*]{#struct_0_17565_x2166_x1067119467}[：指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[advertisement-interval]{lang="EN-US"}**[ *adv-interval*]{lang="EN-US"}]{#struct_0_17565_x2166_510988747}[：指定发送宣告报文的间隔时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[group-policy]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x1988857796}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果指定了本参数，该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[将只为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则所允许的组播组服务；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[将为所有组播组服务。]{style="font-family:宋体"}

[**[holdtime]{lang="EN-US"}**[ *hold-time*]{lang="EN-US"}]{#struct_0_17565_x2166_809975754}[：指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[150]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**[ *priority*]{lang="EN-US"}]{#struct_0_17565_x2166_819128010}[：指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[192]{lang="EN-US"}[。数值越大，优先级越低。]{style="font-family:宋体"}

[**[bidir]{lang="EN-US"}**]{#struct_0_17565_x2166_1527870072}[：指定该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[服务于双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果未指定本参数，该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[将服务于]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_270807774}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_988050741}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须有对应的本地接口，且该接口上必须使能]{style="font-family:宋体"}[PIM]{lang="EN-US"}[，否则配置不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_1339421385}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[所服务的组播组范围（若指定的不是组播组地址，则此规则不生效），而其它可选参数都将被忽略。该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则用来定义该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[所服务的组播组范围，只有]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[的组播组都才会作为]{style="font-family:宋体"}[RP]{lang="EN-US"}[的服务组范围通告出去。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备想要成为多个组范围的]{style="font-family:宋体"}]{#struct_0_17565_x2166_1914347524}[C-RP]{lang="EN-US"}[，则需要在配置]{style="font-family:宋体"}**[group-policy]{lang="EN-US"}**[所对应的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时将多个组范围用多个]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[规则表示出来。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果对同一]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1184794139}[IP]{lang="EN-US"}[地址多次执行本命令，新配置将覆盖旧配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1988923332}

[]{#_Toc94588257}[]{#_Toc78346641}[]{#_Toc80176799}[]{#struct_0_17565_x2166_x1372455013}[]{#_Toc87442524}[]{#_Toc87787165}[]{#_Toc87852044}[]{#_Toc87852823}[]{#_Toc87853604}[]{#_Toc87867643}[]{#_Toc87442525}[]{#_Toc87787166}[]{#_Toc87852045}[]{#_Toc87852824}[]{#_Toc87853605}[]{#_Toc87867644}[]{#_Toc87442528}[]{#_Toc87787169}[]{#_Toc87852048}[]{#_Toc87852827}[]{#_Toc87853608}[]{#_Toc87867647}[]{#_Toc87442530}[]{#_Toc87787171}[]{#_Toc87852050}[]{#_Toc87852829}[]{#_Toc87853610}[]{#_Toc87867649}[]{#_Toc87442531}[]{#_Toc87787172}[]{#_Toc87852051}[]{#_Toc87852830}[]{#_Toc87853611}[]{#_Toc87867650}[]{#_Toc87442532}[]{#_Toc87787173}[]{#_Toc87852052}[]{#_Toc87852831}[]{#_Toc87853612}[]{#_Toc87867651}[]{#_Toc87442533}[]{#_Toc87787174}[]{#_Toc87852053}[]{#_Toc87852832}[]{#_Toc87853613}[]{#_Toc87867652}[]{#_Toc87442534}[]{#_Toc87787175}[]{#_Toc87852054}[]{#_Toc87852833}[]{#_Toc87853614}[]{#_Toc87867653}[]{#_Toc87442535}[]{#_Toc87787176}[]{#_Toc87852055}[]{#_Toc87852834}[]{#_Toc87853615}[]{#_Toc87867654}[]{#_Toc87442536}[]{#_Toc87787177}[]{#_Toc87852056}[]{#_Toc87852835}[]{#_Toc87853616}[]{#_Toc87867655}[]{#_Toc87442537}[]{#_Toc87787178}[]{#_Toc87852057}[]{#_Toc87852836}[]{#_Toc87853617}[]{#_Toc87867656}[]{#_Toc87442538}[]{#_Toc87787179}[]{#_Toc87852058}[]{#_Toc87852837}[]{#_Toc87853618}[]{#_Toc87867657}[]{#_Toc87442539}[]{#_Toc87787180}[]{#_Toc87852059}[]{#_Toc87852838}[]{#_Toc87853619}[]{#_Toc87867658}[]{#_Toc87442540}[]{#_Toc87787181}[]{#_Toc87852060}[]{#_Toc87852839}[]{#_Toc87853620}[]{#_Toc87867659}[]{#_Toc87442541}[]{#_Toc87787182}[]{#_Toc87852061}[]{#_Toc87852840}[]{#_Toc87853621}[]{#_Toc87867660}[]{#_Toc87442542}[]{#_Toc87787183}[]{#_Toc87852062}[]{#_Toc87852841}[]{#_Toc87853622}[]{#_Toc87867661}[]{#_Toc87442543}[]{#_Toc87787184}[]{#_Toc87852063}[]{#_Toc87852842}[]{#_Toc87853623}[]{#_Toc87867662}[]{#_Toc87442544}[]{#_Toc87787185}[]{#_Toc87852064}[]{#_Toc87852843}[]{#_Toc87853624}[]{#_Toc87867663}[]{#_Toc87442545}[]{#_Toc87787186}[]{#_Toc87852065}[]{#_Toc87852844}[]{#_Toc87853625}[]{#_Toc87867664}[]{#_Toc87442547}[]{#_Toc87787188}[]{#_Toc87852067}[]{#_Toc87852846}[]{#_Toc87853627}[]{#_Toc87867666}[\# ]{lang="EN-US"}[在公网实例中将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[配置为]{style="font-family:宋体"}[225.1.0.0/16]{lang="EN-US"}[和]{style="font-family:宋体"}[226.2.0.0/16]{lang="EN-US"}[的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[，且]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_2063304327}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 225.1.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 226.2.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] c-rp 1.1.1.1 group-policy 2000 priority 10]{lang="EN-US"}
:::

::: {#-1860349560 .myid}
[]{#_Toc288743019}[]{#_Toc94588260}[]{#_Toc80176801}[]{#_Toc404789750}[]{#struct_0_17565_x2166_x735962858}[]{#_Toc311539007}[]{#_Toc315856976}[]{#_Toc315859222}[]{#_Toc315856977}[]{#_Toc315859223}[]{#_Toc135108784}[]{#_Toc135109843}[]{#_Toc136489183}[]{#_Toc135108785}[]{#_Toc135109844}[]{#_Toc136489184}[]{#_Toc135108786}[]{#_Toc135109845}[]{#_Toc136489185}[]{#_Toc135108787}[]{#_Toc135109846}[]{#_Toc136489186}[]{#_Toc135108788}[]{#_Toc135109847}[]{#_Toc136489187}[]{#_Toc135108789}[]{#_Toc135109848}[]{#_Toc136489188}[]{#_Toc135108790}[]{#_Toc135109849}[]{#_Toc136489189}[]{#_Toc135108791}[]{#_Toc135109850}[]{#_Toc136489190}[]{#_Toc135108792}[]{#_Toc135109851}[]{#_Toc136489191}[]{#_Toc135108793}[]{#_Toc135109852}[]{#_Toc136489192}[]{#_Toc135108794}[]{#_Toc135109853}[]{#_Toc136489193}[]{#_Toc135108795}[]{#_Toc135109854}[]{#_Toc136489194}[]{#_Toc135108796}[]{#_Toc135109855}[]{#_Toc136489195}[]{#_Toc135108797}[]{#_Toc135109856}[]{#_Toc136489196}[]{#_Toc135108798}[]{#_Toc135109857}[]{#_Toc136489197}[]{#_Toc135108799}[]{#_Toc135109858}[]{#_Toc136489198}[]{#_Toc135108800}[]{#_Toc135109859}[]{#_Toc136489199}[]{#_Toc135108801}[]{#_Toc135109860}[]{#_Toc136489200}[]{#_Toc135108802}[]{#_Toc135109861}[]{#_Toc136489201}[]{#_Toc135108803}[]{#_Toc135109862}[]{#_Toc136489202}[]{#_Toc135108804}[]{#_Toc135109863}[]{#_Toc136489203}[]{#_Toc87442552}[]{#_Toc87787193}[]{#_Toc87852072}[]{#_Toc87852851}[]{#_Toc87853632}[]{#_Toc87867671}[]{#_Toc87442553}[]{#_Toc87787194}[]{#_Toc87852073}[]{#_Toc87852852}[]{#_Toc87853633}[]{#_Toc87867672}[]{#_Toc87442554}[]{#_Toc87787195}[]{#_Toc87852074}[]{#_Toc87852853}[]{#_Toc87853634}[]{#_Toc87867673}[]{#_Toc87442555}[]{#_Toc87787196}[]{#_Toc87852075}[]{#_Toc87852854}[]{#_Toc87853635}[]{#_Toc87867674}[]{#_Toc87442556}[]{#_Toc87787197}[]{#_Toc87852076}[]{#_Toc87852855}[]{#_Toc87853636}[]{#_Toc87867675}[]{#_Toc87442557}[]{#_Toc87787198}[]{#_Toc87852077}[]{#_Toc87852856}[]{#_Toc87853637}[]{#_Toc87867676}[]{#_Toc87442558}[]{#_Toc87787199}[]{#_Toc87852078}[]{#_Toc87852857}[]{#_Toc87853638}[]{#_Toc87867677}[]{#_Toc87442559}[]{#_Toc87787200}[]{#_Toc87852079}[]{#_Toc87852858}[]{#_Toc87853639}[]{#_Toc87867678}[]{#_Toc87442560}[]{#_Toc87787201}[]{#_Toc87852080}[]{#_Toc87852859}[]{#_Toc87853640}[]{#_Toc87867679}[]{#_Toc87442561}[]{#_Toc87787202}[]{#_Toc87852081}[]{#_Toc87852860}[]{#_Toc87853641}[]{#_Toc87867680}[]{#_Toc87442562}[]{#_Toc87787203}[]{#_Toc87852082}[]{#_Toc87852861}[]{#_Toc87853642}[]{#_Toc87867681}[]{#_Toc87442563}[]{#_Toc87787204}[]{#_Toc87852083}[]{#_Toc87852862}[]{#_Toc87853643}[]{#_Toc87867682}[]{#_Toc87442564}[]{#_Toc87787205}[]{#_Toc87852084}[]{#_Toc87852863}[]{#_Toc87853644}[]{#_Toc87867683}[]{#_Toc87442565}[]{#_Toc87787206}[]{#_Toc87852085}[]{#_Toc87852864}[]{#_Toc87853645}[]{#_Toc87867684}[]{#_Toc87442566}[]{#_Toc87787207}[]{#_Toc87852086}[]{#_Toc87852865}[]{#_Toc87853646}[]{#_Toc87867685}[]{#_Toc87442567}[]{#_Toc87787208}[]{#_Toc87852087}[]{#_Toc87852866}[]{#_Toc87853647}[]{#_Toc87867686}[]{#_Toc87442568}[]{#_Toc87787209}[]{#_Toc87852088}[]{#_Toc87852867}[]{#_Toc87853648}[]{#_Toc87867687}[]{#_Toc87442569}[]{#_Toc87787210}[]{#_Toc87852089}[]{#_Toc87852868}[]{#_Toc87853649}[]{#_Toc87867688}[]{#_Toc87442570}[]{#_Toc87787211}[]{#_Toc87852090}[]{#_Toc87852869}[]{#_Toc87853650}[]{#_Toc87867689}[]{#_Toc87442571}[]{#_Toc87787212}[]{#_Toc87852091}[]{#_Toc87852870}[]{#_Toc87853651}[]{#_Toc87867690}[]{#_Toc87442572}[]{#_Toc87787213}[]{#_Toc87852092}[]{#_Toc87852871}[]{#_Toc87853652}[]{#_Toc87867691}[]{#_Toc87442573}[]{#_Toc87787214}[]{#_Toc87852093}[]{#_Toc87852872}[]{#_Toc87853653}[]{#_Toc87867692}[]{#_Toc60064364}[]{#_Toc60649326}[]{#_Toc76002960}[]{#_Toc76444885}[]{#_Toc60064365}[]{#_Toc60649327}[]{#_Toc76002961}[]{#_Toc76444886}[]{#_Toc60064366}[]{#_Toc60649328}[]{#_Toc76002962}[]{#_Toc76444887}[]{#_Toc60064367}[]{#_Toc60649329}[]{#_Toc76002963}[]{#_Toc76444888}[]{#_Toc60064368}[]{#_Toc60649330}[]{#_Toc76002964}[]{#_Toc76444889}[]{#_Toc60064369}[]{#_Toc60649331}[]{#_Toc76002965}[]{#_Toc76444890}[]{#_Toc60064370}[]{#_Toc60649332}[]{#_Toc76002966}[]{#_Toc76444891}[]{#_Toc60064371}[]{#_Toc60649333}[]{#_Toc76002967}[]{#_Toc76444892}[]{#_Toc60064372}[]{#_Toc60649334}[]{#_Toc76002968}[]{#_Toc76444893}[]{#_Toc60064373}[]{#_Toc60649335}[]{#_Toc76002969}[]{#_Toc76444894}[]{#_Toc60064374}[]{#_Toc60649336}[]{#_Toc76002970}[]{#_Toc76444895}[]{#_Toc60064375}[]{#_Toc60649337}[]{#_Toc76002971}[]{#_Toc76444896}[]{#_Toc60064376}[]{#_Toc60649338}[]{#_Toc76002972}[]{#_Toc76444897}[]{#_Toc60064377}[]{#_Toc60649339}[]{#_Toc76002973}[]{#_Toc76444898}[]{#_Toc60064378}[]{#_Toc60649340}[]{#_Toc76002974}[]{#_Toc76444899}[]{#_Toc60064381}[]{#_Toc60649343}[]{#_Toc76002977}[]{#_Toc76444902}[]{#_Toc60064382}[]{#_Toc60649344}[]{#_Toc76002978}[]{#_Toc76444903}[]{#_Toc60064383}[]{#_Toc60649345}[]{#_Toc76002979}[]{#_Toc76444904}[]{#_Toc60064384}[]{#_Toc60649346}[]{#_Toc76002980}[]{#_Toc76444905}[]{#_Toc60064385}[]{#_Toc60649347}[]{#_Toc76002981}[]{#_Toc76444906}[]{#_Toc60064386}[]{#_Toc60649348}[]{#_Toc76002982}[]{#_Toc76444907}[]{#_Toc60064387}[]{#_Toc60649349}[]{#_Toc76002983}[]{#_Toc76444908}[]{#_Toc60064388}[]{#_Toc60649350}[]{#_Toc76002984}[]{#_Toc76444909}[]{#_Toc60064389}[]{#_Toc60649351}[]{#_Toc76002985}[]{#_Toc76444910}[]{#_Toc60064390}[]{#_Toc60649352}[]{#_Toc76002986}[]{#_Toc76444911}[]{#_Toc60064391}[]{#_Toc60649353}[]{#_Toc76002987}[]{#_Toc76444912}[]{#_Toc60064392}[]{#_Toc60649354}[]{#_Toc76002988}[]{#_Toc76444913}[]{#_Toc60064393}[]{#_Toc60649355}[]{#_Toc76002989}[]{#_Toc76444914}[]{#_Toc60064394}[]{#_Toc60649356}[]{#_Toc76002990}[]{#_Toc76444915}[]{#_Toc60064395}[]{#_Toc60649357}[]{#_Toc76002991}[]{#_Toc76444916}[]{#_Toc60064396}[]{#_Toc60649358}[]{#_Toc76002992}[]{#_Toc76444917}[]{#_Toc60064397}[]{#_Toc60649359}[]{#_Toc76002993}[]{#_Toc76444918}[]{#_Toc60064398}[]{#_Toc60649360}[]{#_Toc76002994}[]{#_Toc76444919}[]{#_Toc60064399}[]{#_Toc60649361}[]{#_Toc76002995}[]{#_Toc76444920}[]{#_Toc60064400}[]{#_Toc60649362}[]{#_Toc76002996}[]{#_Toc76444921}[]{#_Toc60064401}[]{#_Toc60649363}[]{#_Toc76002997}[]{#_Toc76444922}[]{#_Toc60064402}[]{#_Toc60649364}[]{#_Toc76002998}[]{#_Toc76444923}[]{#_Toc60064403}[]{#_Toc60649365}[]{#_Toc76002999}[]{#_Toc76444924}[]{#_Toc60064404}[]{#_Toc60649366}[]{#_Toc76003000}[]{#_Toc76444925}[]{#_Toc60064407}[]{#_Toc60649369}[]{#_Toc76003003}[]{#_Toc76444928}[]{#_Toc60064408}[]{#_Toc60649370}[]{#_Toc76003004}[]{#_Toc76444929}[]{#_Toc60064409}[]{#_Toc60649371}[]{#_Toc76003005}[]{#_Toc76444930}[]{#_Toc60064410}[]{#_Toc60649372}[]{#_Toc76003006}[]{#_Toc76444931}[]{#_Toc60064411}[]{#_Toc60649373}[]{#_Toc76003007}[]{#_Toc76444932}[]{#_Toc60064412}[]{#_Toc60649374}[]{#_Toc76003008}[]{#_Toc76444933}[]{#_Toc60064413}[]{#_Toc60649375}[]{#_Toc76003009}[]{#_Toc76444934}[]{#_Toc60064414}[]{#_Toc60649376}[]{#_Toc76003010}[]{#_Toc76444935}[]{#_Toc60064415}[]{#_Toc60649377}[]{#_Toc76003011}[]{#_Toc76444936}[]{#_Toc60064416}[]{#_Toc60649378}[]{#_Toc76003012}[]{#_Toc76444937}[]{#_Toc60064417}[]{#_Toc60649379}[]{#_Toc76003013}[]{#_Toc76444938}[]{#_Toc60064418}[]{#_Toc60649380}[]{#_Toc76003014}[]{#_Toc76444939}[]{#_Toc60064419}[]{#_Toc60649381}[]{#_Toc76003015}[]{#_Toc76444940}[]{#_Toc60064420}[]{#_Toc60649382}[]{#_Toc76003016}[]{#_Toc76444941}[]{#_Toc60064421}[]{#_Toc60649383}[]{#_Toc76003017}[]{#_Toc76444942}[]{#_Toc60064422}[]{#_Toc60649384}[]{#_Toc76003018}[]{#_Toc76444943}[]{#_Toc60064423}[]{#_Toc60649385}[]{#_Toc76003019}[]{#_Toc76444944}[]{#_Toc60064424}[]{#_Toc60649386}[]{#_Toc76003020}[]{#_Toc76444945}[]{#_Toc60064425}[]{#_Toc60649387}[]{#_Toc76003021}[]{#_Toc76444946}[]{#_Toc60064426}[]{#_Toc60649388}[]{#_Toc76003022}[]{#_Toc76444947}

**PIM \-- PIM配置命令 \-- crp-policy (PIM view)**

------------------------------------------------------------------------

[**[crp-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_771410984}[命令用来配置合法的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[地址范围及其服务的组播组范围，以防止]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[欺骗。]{style="font-family:宋体"}

[**[undo crp-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_1045896128}[命令用来取消]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[地址范围及其服务的组播组范围的限制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1341421778}

[**[crp-policy]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_17565_x2166_x1988988868}

[**[undo]{lang="EN-US"}**[ **crp-policy**]{lang="EN-US"}]{#struct_0_17565_x2166_1758235490}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x577577404}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_1005341030}[地址范围及其服务的组播组范围不受任何限制，即认为所有收到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[报文都是合法的。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x800614229}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1900200974}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_549790765}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1898363706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1796408577}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1988530116}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_88461534}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1636548678}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_x1932281524}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定合法]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[的地址范围，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[参数用来指定该]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[所服务的组播组地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，]{style="font-family:宋体"}[而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令在对]{style="font-family:宋体"}]{#struct_0_17565_x2166_1656099563}[C-RP]{lang="EN-US"}[所宣告的组播组范围进行过滤时，只取其前缀部分进行匹配。例如，]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[宣告的组播组范围为]{style="font-family:宋体"}[224.1.0.0/16]{lang="EN-US"}[，如果其前缀部分"]{style="font-family:宋体"}[224.1.0.0]{lang="EN-US"}["能匹配上本命令所引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则，就认为整个组播组范围"]{style="font-family:宋体"}[224.1.0.0/16]{lang="EN-US"}["都通过了过滤。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1282364755}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_2116110846}[在公网实例中配置]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[策略，只允许]{style="font-family:宋体"}[1.1.1.1/24]{lang="EN-US"}[范围内的设备充当]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[，且只允许其为]{style="font-family:宋体"}[225.1.1.0/24]{lang="EN-US"}[范围内的组播组服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1988595652}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule permit ip source 1.1.1.1 0.0.0.255 destination 225.1.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] crp-policy 3000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1336844539}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[c-rp]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_1712931240}
:::

::: {#401267625 .myid}
[]{#_Toc404789751}[]{#struct_0_17565_x2166_1079455784}[]{#_Toc354839447}[]{#_Toc296504298}[]{#_Toc267327363}

**PIM \-- PIM配置命令 \-- display interface register-tunnel**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **interface** **register-tunnel**]{lang="EN-US"}]{#struct_0_17565_x2166_1079259176}[命令用来显示]{style="font-family:宋体"}[Register-Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_957881303}

[**[display]{lang="EN-US"}**[ **interface** \[ **register-tunnel**]{lang="EN-US"}]{#struct_0_17565_x2166_564041642}[ ]{lang="EN-US"}[\[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1079324712}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_1697384343}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x242013377}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x994796596}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_1080176680}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_2009555073}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1905959276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2068856616}

[**[register-tunnel]{lang="EN-US"}**]{#struct_0_17565_x2166_1080242216}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[接口]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[*[interface-number]{lang="PT-BR"}*]{#struct_0_17565_x2166_454594173}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[接口的编号。设备上只存在一个]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[接口，其编号为]{style="font-family:宋体"}[0]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_17565_x2166_1256956455}[：显示概要信息。如果未指定本参数，将显示详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_17565_x2166_1079652389}[：当用户配置的接口描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符时，在概要信息中显示完整的接口描述信息。如果未指定本参数，在概要信息中将只显示前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不会显示。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_17565_x2166_x934636641}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果未指定本参数，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1292312067}

[[Register-Tunnel]{lang="EN-US"}]{#struct_0_17565_x2166_x2021822568}[接口]{style="font-family:宋体"}[是一种虚拟接口，由系统自动创建。用户不能对该接口进行配置和删除，但可使用本命令进行显示。]{style="font-family:宋体"}

[[Register-Tunnel]{lang="EN-US"}]{#struct_0_17565_x2166_286733039}[接口是在组播源注册过程初期，用于在组播源侧]{style="font-family:宋体"}[DR]{lang="PT-BR"}[与]{style="font-family:宋体"}[RP]{lang="PT-BR"}[之间建立一个传输注册报文的通道，具体过程为：当组播源侧]{style="font-family:宋体"}[DR]{lang="PT-BR"}[第一次收到组播源发来的组播数据时，由于组播源侧]{style="font-family:宋体"}[DR]{lang="PT-BR"}[与]{style="font-family:宋体"}[RP]{lang="PT-BR"}[之间尚未建立]{style="font-family:宋体"}[SPT]{lang="PT-BR"}[，于是组播源侧]{style="font-family:宋体"}[DR]{lang="PT-BR"}[通过其]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[接口将封装到注册报文中的组播数据发给]{style="font-family:宋体"}[RP]{lang="PT-BR"}[，而]{style="font-family:宋体"}[RP]{lang="PT-BR"}[也通过其]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[接口接收注册报文，并将解封装后的组播数据转发给接收者。]{style="font-family:宋体"}

[[在上述过程中，]{style="font-family:宋体"}]{#struct_0_17565_x2166_1079717925}[RP]{lang="PT-BR"}[从组播数据中获取到了组播源的位置，于是向组播源方向发送加入报文并最终建立起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[。此后，组播源侧]{style="font-family:宋体"}[DR]{lang="PT-BR"}[便不再通过]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[接口，而是通过]{style="font-family:宋体"}[SPT]{lang="PT-BR"}[将组播数据发送给]{style="font-family:宋体"}[RP]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17565_x2166_2044951471}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定接口类型，将显示设备支持的所有接口的信息。]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1386567008}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于设备上只存在一个]{style="font-family:宋体"}]{#struct_0_17565_x2166_x731428088}[Register-Tunnel]{lang="PT-BR"}[接口（即]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[0]{lang="PT-BR"}[）]{style="font-family:宋体"}[，因此只要指定了]{style="font-family:宋体"}**[register-tunnel]{lang="EN-US"}**[参数，不论是否指定]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，都将显示接口]{style="font-family:宋体"}[Register-Tunnel]{lang="PT-BR"}[0]{lang="PT-BR"}[的相关信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1079521317}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1702739914}[显示接口]{style="font-family:宋体"}[Register-Tunnel]{lang="EN-US"}[0]{lang="PT-BR"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ]{lang="EN-US"}]{#struct_0_17565_x2166_1079586853}[register-tunnel 0]{lang="PT-BR"}

[Register-Tunnel0]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: DOWN]{lang="EN-US"}

[Description: Register-Tunnel0 Interface]{lang="EN-US"}

[Maximum Transmit Unit: 1536]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[Physical: Unknown]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1492717565}[显示接口]{style="font-family:宋体"}[Register-Tunnel]{lang="EN-US"}[0]{lang="PT-BR"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface ]{lang="EN-US"}]{#struct_0_17565_x2166_1128935706}[register-tunnel 0 brief]{lang="PT-BR"}

[Brief information on interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[REG0                 UP   \--       \--]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display interface ]{lang="EN-US"}]{#struct_0_17565_x2166_x263989943}[register-tunnel]{lang="PT-BR"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_499721227}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_1079455781}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1037921700}

[[Current state]{lang="EN-US"}]{#struct_0_17565_x2166_360812223}

[[接口的物理状态，]{style="font-family:宋体"}[Register-Tunnel]{lang="EN-US"}]{#struct_0_17565_x2166_1079259173}[接口的物理状态始终为]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_17565_x2166_957684695}

[[接口的链路状态，]{style="font-family:宋体"}[Register-Tunnel]{lang="EN-US"}]{#struct_0_17565_x2166_1079324709}[接口的链路状态始终为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[Description]{lang="EN-US"}]{#struct_0_17565_x2166_1696663446}

[[接口的描述信息，不可配置]{style="font-family:宋体"}]{#struct_0_17565_x2166_573962901}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_17565_x2166_1080242213}

[[接口的最大传输单元，不可配置]{style="font-family:宋体"}]{#struct_0_17565_x2166_454790781}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_17565_x2166_1079652390}

[[接口能否配置]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17565_x2166_1292770818}[地址，始终为]{style="font-family:宋体"}[disabled]{lang="EN-US"}[，表示不能]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_17565_x2166_1079717926}

[[接口的物理类型，始终为]{style="font-family:宋体"}[Unknown]{lang="EN-US"}]{#struct_0_17565_x2166_2045017007}[，表示未知]{style="font-family:宋体"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_17565_x2166_x552144818}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_17565_x2166_1079521318}[秒钟的平均输入速率，始终均为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_17565_x2166_1701887946}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_17565_x2166_1079586854}[秒钟的平均输出速率，始终均为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Input]{lang="EN-US"}]{#struct_0_17565_x2166_x1492258813}

[[接口输入的报文数、字节数、丢弃报文数，始终均为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_17565_x2166_1079390246}

[[Output]{lang="EN-US"}]{#struct_0_17565_x2166_x1835125466}

[[接口输出的报文数、字节数、丢弃报文数，始终均为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_17565_x2166_1079455782}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_17565_x2166_x1037856164}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_17565_x2166_1079259174}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_17565_x2166_957750231}

[[接口的物理连接状态：]{style="font-family:宋体"}]{#struct_0_17565_x2166_1079324710}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_17565_x2166_1697253271}[：表示接口在物理上连通]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_17565_x2166_204536608}[：表示]{lang="EN-US" style="font-family:宋体"}[接口在物理上]{style="font-family:宋体"}[不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_17565_x2166_1080176678}[：表示接口被手工关闭，需执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[shutdown]{lang="EN-US"}**[命令才能打开]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_17565_x2166_2010079372}[：表示接口为备份接口，可使用]{style="font-family:宋体"}**[display]{lang="EN-US"}**[ ]{lang="EN-US"}**[interface-backup]{lang="EN-US"}**[ ]{lang="EN-US"}**[state]{lang="EN-US"}**[命令查看其主接口]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_17565_x2166_1080242214}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_17565_x2166_454725245}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["，表示该接口的数据链路层协议状态显示为]{style="font-family:宋体"}[UP]{lang="EN-US"}[，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_17565_x2166_1079652387}

[[接口的协议连接状态，对]{style="font-family:宋体"}[Register-Tunnel]{lang="EN-US"}]{#struct_0_17565_x2166_1293229571}[接口]{style="font-family:宋体"}[无意义，始终为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_17565_x2166_1079717923}

[[接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17565_x2166_2045344687}[地址，不可配置。对]{style="font-family:宋体"}[Register-Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[无意义，始终为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_17565_x2166_1079521315}

[[接口物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_17565_x2166_1702608842}[的原因，始终为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[，表示没有物理连接]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1592266100 .myid}
[]{#_Toc404789752}[]{#struct_0_17565_x2166_x1968926874}

**PIM \-- PIM配置命令 \-- display pim bsr-info**

------------------------------------------------------------------------

[**[display pim bsr-info]{lang="EN-US"}**]{#struct_0_17565_x2166_x1330792293}[命令用来显示]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[域中的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1845081550}

[**[display pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **bsr-info**]{lang="EN-US"}]{#struct_0_17565_x2166_1877129332}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_479009652}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_1128541409}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1974949928}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x422970460}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1607859785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x162280155}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_987242653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1441009102}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_134765897}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x324999067}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1876616406}[显示公网实例]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[域中的]{style="font-family:宋体"}[BSR]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[]{#_Toc80176802}[[\<Sysname\> display pim bsr-info]{lang="EN-US"}]{#struct_0_17565_x2166_x423101532}

[ Scope: non-scoped]{lang="EN-US"}

[     State: Accept Preferred]{lang="EN-US"}

[     Bootstrap timer: 00:01:44]{lang="EN-US"}

[     Elected BSR address: 12.12.12.1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 30]{lang="EN-US"}

[       Uptime: 00:21:56]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Scope: 239.4.0.0/16]{lang="EN-US"}

[     State: Accept Any]{lang="EN-US"}

[     Scope-zone expiry timer: 00:21:12]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Scope: 239.1.0.0/16]{lang="EN-US"}

[     State: Elected]{lang="EN-US"}

[     Bootstrap timer: 00:00:26]{lang="EN-US"}

[     Elected BSR address: 17.1.11.1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 30]{lang="EN-US"}

[       Uptime: 02:53:37]{lang="EN-US"}

[     Candidate BSR address: 17.1.11.1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}[Scope: 239.2.2.0/24]{lang="IT"}

[     State: Candidate]{lang="IT"}

[     Bootstrap timer: 00:01:56]{lang="IT"}

[     ]{lang="IT"}[Elected BSR address: 61.2.37.1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 30]{lang="EN-US"}

[       Uptime: 02:53:32]{lang="EN-US"}

[     Candidate BSR address: 17.1.12.1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Scope: 239.3.3.0/24]{lang="EN-US"}

[     State: Pending]{lang="EN-US"}

[     Bootstrap timer: 00:00:07]{lang="EN-US"}

[     Candidate BSR address: 17.1.13.1]{lang="EN-US"}

[       Priority: 64]{lang="EN-US"}

[       Hash mask length: 30]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display pim bsr-info]{lang="EN-US"}]{#struct_0_17565_x2166_1093301615}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x184639190}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_2018174006}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_175164079}

[[Scope]{lang="EN-US"}]{#struct_0_17565_x2166_1902060759}

[[域]{style="font-family:宋体"}]{#struct_0_17565_x2166_1960584173}

[[State]{lang="EN-US"}]{#struct_0_17565_x2166_x423167068}

[[域状态]{style="font-family:宋体"}]{#struct_0_17565_x2166_1508412468}

[[Bootstrap timer]{lang="EN-US"}]{#struct_0_17565_x2166_x1572586963}

[[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_1860228273}[定时器]{style="font-family:宋体"}

[[Scope-zone expiry timer]{lang="EN-US"}]{#struct_0_17565_x2166_x1639796937}

[[域老化定时器]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1381677717}

[[Elected BSR address]{lang="EN-US"}]{#struct_0_17565_x2166_x422708316}

[[当选]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_x2063620524}[的地址]{style="font-family:宋体"}

[[Candidate BSR address]{lang="EN-US"}]{#struct_0_17565_x2166_1107636336}

[[候选]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_x727970597}[的地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_17565_x2166_1295778243}

[[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_214545272}[的优先级]{style="font-family:宋体"}

[[Hash mask length]{lang="EN-US"}]{#struct_0_17565_x2166_x422773852}

[[哈希掩码长度]{style="font-family:宋体"}]{#struct_0_17565_x2166_1519017801}

[[Uptime]{lang="EN-US"}]{#struct_0_17565_x2166_x1889437249}

[[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_1610530470}[已存在的时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1229426954 .myid}
[]{#_Toc94588263}[]{#_Toc404789753}[]{#struct_0_17565_x2166_x432077698}[]{#_Toc311539009}

**PIM \-- PIM配置命令 \-- display pim claimed-route**

------------------------------------------------------------------------

[**[display pim claimed-route]{lang="EN-US"}**]{#struct_0_17565_x2166_481199061}[命令用来显示]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[所使用的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1678241496}

[**[display pim]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **claimed-route** \[ *source-address* \]]{lang="EN-US"}]{#struct_0_17565_x2166_x422839388}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_659823447}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_1483869526}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x716487121}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1713784633}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x397224148}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_235730923}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1329444821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1254552832}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x422904924}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的路由信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的路由信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_17565_x2166_1932930895}[：组播源的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，显示到达指定组播源的路由信息。如果未指定本参数，将显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[所使用的所有路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x493153283}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x188168247}[显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[在公网实例中使用的所有路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim claimed-route]{lang="EN-US"}]{#struct_0_17565_x2166_x422446172}

[ RPF-route selecting rule: longest-match]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Route/mask: 7.11.0.0/16 (unicast (direct))]{lang="EN-US"}

[     RPF interface: Vlan-interface2, RPF neighbor: 8.0.0.2]{lang="EN-US"}

[     Total number of (S,G) or (\*,G) dependent on this route entry: 4]{lang="EN-US"}

[     (7.11.0.10, 225.1.1.1)]{lang="EN-US"}

[     (7.11.0.10, 226.1.1.1)]{lang="EN-US"}

[     (7.11.0.10, 227.1.1.1)]{lang="EN-US"}

[     (\*, 228.1.1.1)]{lang="EN-US"}

[ Route/mask: 7.12.0.0/16 (multicast static)]{lang="EN-US"}

[     RPF interface: Vlan-interface2, RPF neighbor: 8.0.0.3,]{lang="EN-US"}

[     Config NextHop: 8.0.0.5]{lang="EN-US"}

[     Total number of (S,G) or (\*,G) dependent on this route entry: 2]{lang="EN-US"}

[     (7.12.0.10, 226.1.1.1)]{lang="EN-US"}

[     (7.12.0.10, 225.1.1.1)]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display pim claimed-route]{lang="EN-US"}]{#struct_0_17565_x2166_338892839}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x189751515}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_355322106}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1977309265}

[[RPF-route selecting rule]{lang="EN-US"}]{#struct_0_17565_x2166_x57060465}

[[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_591713585}[路由的选择规则]{style="font-family:宋体"}

[[Route/mask]{lang="EN-US"}]{#struct_0_17565_x2166_x532065840}

[[路由项。括号内为路由类型，包括：]{style="font-family:宋体"}]{#struct_0_17565_x2166_x2027185501}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[igp]{lang="EN-US"}]{#struct_0_17565_x2166_x422511708}[：单播路由（内部网关协议）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[egp]{lang="EN-US"}]{#struct_0_17565_x2166_x457804332}[：单播路由（外部网关协议）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unicast (direct)]{lang="EN-US"}]{#struct_0_17565_x2166_743973026}[：单播路由（直连）]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unicast]{lang="EN-US"}]{#struct_0_17565_x2166_x1541801270}[：其它单播路由（如单播静态路由等）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[mbgp]{lang="EN-US"}]{#struct_0_17565_x2166_x1410874347}[：]{lang="EN-US" style="font-family:宋体"}[MBGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicast static]{lang="EN-US"}]{#struct_0_17565_x2166_x386841254}[：组播静态路由]{lang="EN-US" style="font-family:
  宋体"}

[[RPF interface]{lang="EN-US"}]{#struct_0_17565_x2166_x422970459}

[[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1608318534}[接口的名称]{style="font-family:宋体"}

[[RPF neighbor]{lang="EN-US"}]{#struct_0_17565_x2166_x1109383293}

[[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_268137166}[邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Config NextHop]{lang="EN-US"}]{#struct_0_17565_x2166_428138214}

[[配置的下一跳地址，本字段只在组播静态路由配置下一跳时显示]{style="font-family:宋体"}]{#struct_0_17565_x2166_x871859946}

[[Total number of (S,G) or (\*,G) dependent ]{lang="EN-US"}]{#struct_0_17565_x2166_x423035995}

[[on this route entry]{lang="EN-US"}]{#struct_0_17565_x2166_762225306}

[[基于此]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1383827474}[路由的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）个数及列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#542735399 .myid}
[]{#_Toc288743021}[]{#_Toc404789754}[]{#struct_0_17565_x2166_671193065}[]{#_Toc288743020}

**PIM \-- PIM配置命令 \-- display pim c-rp**

------------------------------------------------------------------------

[**[display pim c-rp]{lang="EN-US"}**]{#struct_0_17565_x2166_512550987}[命令用来显示]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[域中的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1834630327}

[**[display pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **c-rp** \[ **local** \]]{lang="EN-US"}]{#struct_0_17565_x2166_x829221673}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x423101531}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_1093367151}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_446745960}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1142755088}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x663296612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1210459068}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x474783732}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1292793664}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x855311743}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_17565_x2166_x423167067}[：显示本地配置且生效的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。如果未指定本参数，将显示所有学习到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1509264436}

[[只有当选的]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_x1576470890}[上才会有学习到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息，其它设备上只能查看到本地配置生效的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1353197666}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x668797769}[显示公网实例中学习到的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim c-rp]{lang="EN-US"}]{#struct_0_17565_x2166_x1617931867}

[ Scope: non-scoped]{lang="EN-US"}

[     Group/MaskLen: 224.0.0.0/4]{lang="EN-US"}

[       C-RP address             Priority  HoldTime  Uptime    Expires]{lang="EN-US"}

[       1.1.1.1 (local)          192       150       03:01:36  00:02:29]{lang="EN-US"}

[       2.2.2.2                  192       150       1d:13h    00:02:02]{lang="EN-US"}

[     Group/MaskLen: 226.1.1.0/24 \[B\] Expires: 00:00:33]{lang="EN-US"}

[     Group/MaskLen: 225.1.0.0/16 \[B\]]{lang="EN-US"}

[       C-RP Address             Priority  HoldTime  Uptime    Expires]{lang="EN-US"}

[       3.3.3.3                  192       150       12w:5d    00:02:05]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x422708315}[显示本地配置生效的]{style="font-family:宋体"}[C-RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim c-rp local]{lang="EN-US"}]{#struct_0_17565_x2166_x2063554988}

[ Candidate RP: 12.12.12.9(Loop1)]{lang="EN-US"}

[     Priority: 192]{lang="EN-US"}

[     HoldTime: 150]{lang="EN-US"}

[     Advertisement interval: 60]{lang="EN-US"}

[     Next advertisement scheduled at: 00:00:48]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display pim c-rp]{lang="EN-US"}]{#struct_0_17565_x2166_102481061}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x195626699}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_89141975}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1856804149}

[[Scope]{lang="EN-US"}]{#struct_0_17565_x2166_x1161207334}

[[域]{style="font-family:宋体"}]{#struct_0_17565_x2166_x422773851}

[[Group/MaskLen]{lang="EN-US"}]{#struct_0_17565_x2166_1519214409}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_x291252270}[所服务的组播组]{style="font-family:宋体"}

[[\[B\]]{lang="EN-US"}]{#struct_0_17565_x2166_x1132118970}

[[表示]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_x189545144}[服务于双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果未显示本字段，则表示服务于]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}

[[C-RP address]{lang="EN-US"}]{#struct_0_17565_x2166_x1898607658}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_1429895397}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示本地地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_17565_x2166_x422839387}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_658971479}[的优先级]{style="font-family:宋体"}

[[HoldTime]{lang="EN-US"}]{#struct_0_17565_x2166_x996725942}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_517243925}[的超时时间]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_17565_x2166_1560742679}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_x422904923}[已存在的时间，]{style="font-family:宋体"}[w]{lang="EN-US"}[表示星期，]{style="font-family:宋体"}[d]{lang="EN-US"}[表示天，]{style="font-family:宋体"}[h]{lang="EN-US"}[表示小时]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_17565_x2166_1932996431}

[[C-RP/]{lang="EN-US"}]{#struct_0_17565_x2166_x878564675}[组播组的超时剩余时间]{style="font-family:宋体"}

[[Candidate RP]{lang="EN-US"}]{#struct_0_17565_x2166_x1319185201}

[[本地]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_1318200538}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Advertisement interval]{lang="EN-US"}]{#struct_0_17565_x2166_x914094748}

[[本地]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_x422446171}[发送通告报文时间间隔]{style="font-family:宋体"}

[[Next advertisement scheduled at]{lang="EN-US"}]{#struct_0_17565_x2166_338958375}

[[本地]{style="font-family:宋体"}[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_x1628636489}[发送下一个通告报文的剩余时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#11591525 .myid}
[]{#_Toc404789755}[]{#struct_0_17565_x2166_x1547576919}[]{#_Toc345338667}[]{#_Toc341772845}[]{#_Toc321055242}[]{#_Toc263693129}

**PIM \-- PIM配置命令 \-- display pim df-info**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **pim** **df-info**]{lang="EN-US"}]{#struct_0_17565_x2166_x77405210}[命令用来显示双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[DF]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x998380848}

[**[display]{lang="EN-US"}**[ **pim** \[ **vpn-instance** *vpn-instance-name* \] **df-info** \[ *rp-address* \]]{lang="EN-US"}]{#struct_0_17565_x2166_x422511707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x456821292}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1639022983}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_501698484}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1957313150}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1449628710}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_8236137}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_690071637}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x422970462}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x1607990857}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的双向]{style="font-family:宋体"}[PIM DF]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[rp-address]{lang="EN-US"}*]{#struct_0_17565_x2166_x1475721944}[：指定双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_173077242}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1533416046}[显示公网实例中双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的]{style="font-family:宋体"}[DF]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim df-info]{lang="EN-US"}]{#struct_0_17565_x2166_x32667895}

[RP address: 12.12.12.12]{lang="EN-US"}

[  Interface: GigabitEthernet0/0/4]{lang="EN-US"}

[    State     : Win        DF preference: 10]{lang="EN-US"}

[    DF metric : 1562       DF uptime    : 00:06:59]{lang="EN-US"}

[    DF address: 30.1.1.11 (local)]{lang="EN-US"}

[  Interface: Tunnel0, 100.1.1.12]{lang="EN-US"}

[    State     : Lose       DF preference: 0]{lang="EN-US"}

[    DF metric : 0          DF uptime    : 00:06:59]{lang="EN-US"}

[    DF address: 100.1.1.12]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display pim df-info]{lang="EN-US"}]{#struct_0_17565_x2166_787588725}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_476683939}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1406114925}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_14386272}

[[RP address]{lang="EN-US"}]{#struct_0_17565_x2166_x1551697669}

[[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_370288952}[的]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_17565_x2166_x1195794989}

[[接口名称，使能了]{style="font-family:宋体"}[nbma]{lang="EN-US"}]{#struct_0_17565_x2166_x1893209022}[模式的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道口，显示远端连接]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_17565_x2166_x792510462}

[[DF]{lang="EN-US"}]{#struct_0_17565_x2166_1936372893}[的选举状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Win]{lang="EN-US"}]{#struct_0_17565_x2166_x1599079516}[：竞选]{lang="EN-US" style="font-family:宋体"}[DF]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lose]{lang="EN-US"}]{#struct_0_17565_x2166_1414831381}[：竞选]{style="font-family:宋体"}[DF]{lang="EN-US"}[落败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offer]{lang="EN-US"}]{#struct_0_17565_x2166_1129803839}[：竞选]{style="font-family:宋体"}[DF]{lang="EN-US"}[的初始状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backoff]{lang="EN-US"}]{#struct_0_17565_x2166_1533088366}[：正在充当]{style="font-family:宋体"}[DF]{lang="EN-US"}[，但有更优的设备正在竞选]{style="font-family:宋体"}[DF]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[-]{lang="EN-US"}]{#struct_0_17565_x2166_x32995575}[[：不参与]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[DF]{lang="EN-US"}[[竞选]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[DF preference]{lang="EN-US"}]{#struct_0_17565_x2166_14058592}

[[DF]{lang="EN-US"}]{#struct_0_17565_x2166_x464179816}[通告的路由优先级]{style="font-family:宋体"}

[[DF metric]{lang="EN-US"}]{#struct_0_17565_x2166_x1552025349}

[[DF]{lang="EN-US"}]{#struct_0_17565_x2166_370223416}[通告的路由度量值]{style="font-family:宋体"}

[[DF uptime]{lang="EN-US"}]{#struct_0_17565_x2166_x1195860525}

[[DF]{lang="EN-US"}]{#struct_0_17565_x2166_x735445487}[已存在的时间]{style="font-family:宋体"}

[[DF address]{lang="EN-US"}]{#struct_0_17565_x2166_x792575998}

[[DF]{lang="EN-US"}]{#struct_0_17565_x2166_1936307357}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示本地地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1945419167 .myid}
[]{#_Toc404789756}[]{#struct_0_17565_x2166_x2125259859}

**PIM \-- PIM配置命令 \-- display pim interface**

------------------------------------------------------------------------

[**[display pim interface]{lang="EN-US"}**]{#struct_0_17565_x2166_296930389}[命令用来显示接口上的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x422708318}

[**[display pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **interface** \[ *interface-type interface-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17565_x2166_x2062703020}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1547496820}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1099657214}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x704200695}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x265752392}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1019934042}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_92448499}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x422773854}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1519411017}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x286748666}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_17565_x2166_x843603917}[：显示指定接口上的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[信息。如果未指定本参数，将显示所有接口上的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17565_x2166_x1864721164}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x730157197}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1728216011}[显示公网实例所有接口上的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim interface]{lang="EN-US"}]{#struct_0_17565_x2166_x1699185154}

[ Interface         NbrCnt  HelloInt  DR-Pri     DR-Address]{lang="EN-US"}

[ GE1/0/1           1       30        1          10.1.1.2]{lang="EN-US"}

[ GE1/0/2           0       30        1          172.168.0.2    (local)]{lang="EN-US"}

[ GE1/0/3           1       30        1          20.1.1.2]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display pim interface]{lang="EN-US"}]{#struct_0_17565_x2166_x422839390}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x197474981}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_659299158}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_1907738411}

[[Interface]{lang="EN-US"}]{#struct_0_17565_x2166_925419618}

[[接口名称]{style="font-family:宋体"}]{#struct_0_17565_x2166_x581335200}

[[NbrCnt]{lang="EN-US"}]{#struct_0_17565_x2166_x857633873}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x83716869}[邻居的数量]{style="font-family:宋体"}

[[HelloInt]{lang="EN-US"}]{#struct_0_17565_x2166_x422904926}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_1932799823}[报文的时间间隔]{style="font-family:宋体"}

[[DR-Pri]{lang="EN-US"}]{#struct_0_17565_x2166_1442006265}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_17565_x2166_60786746}[的优先级]{style="font-family:宋体"}

[[DR-Address]{lang="EN-US"}]{#struct_0_17565_x2166_2088761035}

[[DR]{lang="EN-US"}]{#struct_0_17565_x2166_x422446174}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示本地地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="SV"}]{#struct_0_17565_x2166_339286055}[显示公网实例接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[PIM]{lang="SV"}[详细信息。]{style="font-family:宋体"}

[]{#_Toc94588264}[]{#_Toc80176803}[]{#struct_0_17565_x2166_x422511710}[]{#_Toc87787227}[]{#_Toc87852106}[]{#_Toc87852885}[]{#_Toc87853666}[]{#_Toc87867705}[]{#_Toc87787243}[]{#_Toc87852122}[]{#_Toc87852901}[]{#_Toc87853682}[]{#_Toc87867721}[\<Sysname\> display pim interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}

[ ]{lang="EN-US"}[Interface: GigabitEthernet1/0/1, 10.1.1.1]{lang="FR"}

[     PIM version: 2]{lang="FR"}

[     PIM mode: Sparse]{lang="FR"}

[     ]{lang="FR"}[PIM DR: 10.1.1.2]{lang="EN-US"}

[     PIM DR Priority (configured): 1]{lang="EN-US"}

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

[[表1-7 ]{lang="EN-US"}[display pim interface verbose]{lang="EN-US"}]{#struct_0_17565_x2166_x457280043}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x170105875}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_1471934947}

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1139014064}

[[Interface]{lang="EN-US"}]{#struct_0_17565_x2166_179303404}

[[接口名称与]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17565_x2166_1747528476}[地址]{style="font-family:宋体"}

[[PIM version]{lang="EN-US"}]{#struct_0_17565_x2166_x422970461}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1607794249}[协议的版本号]{style="font-family:宋体"}

[[PIM mode]{lang="EN-US"}]{#struct_0_17565_x2166_591385392}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1376414486}[协议的模式，是密集模式还是稀疏模式]{style="font-family:宋体"}

[[PIM DR]{lang="EN-US"}]{#struct_0_17565_x2166_961938732}

[[DR]{lang="EN-US"}]{#struct_0_17565_x2166_x1027106840}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[PIM DR Priority (configured)]{lang="EN-US"}]{#struct_0_17565_x2166_127508158}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_17565_x2166_x423035997}[优先级的配置值]{style="font-family:宋体"}

[[PIM neighbors count]{lang="EN-US"}]{#struct_0_17565_x2166_762094234}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1868629116}[邻居的总数]{style="font-family:宋体"}

[[PIM hello interval]{lang="EN-US"}]{#struct_0_17565_x2166_916857676}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_174664941}[报文的时间间隔]{style="font-family:宋体"}

[[PIM LAN delay (negotiated)]{lang="EN-US"}]{#struct_0_17565_x2166_x1401725689}

[[剪枝报文传输延迟的协商值]{style="font-family:宋体"}]{#struct_0_17565_x2166_x423101533}

[[PIM LAN delay (configured)]{lang="EN-US"}]{#struct_0_17565_x2166_1093236079}

[[剪枝报文传输延迟的配置值]{style="font-family:宋体"}]{#struct_0_17565_x2166_1225540134}

[[PIM override interval (negotiated)]{lang="EN-US"}]{#struct_0_17565_x2166_x1998507204}

[[剪枝否决时间的协商值]{style="font-family:宋体"}]{#struct_0_17565_x2166_x469412880}

[[PIM override interval (configured)]{lang="EN-US"}]{#struct_0_17565_x2166_x423167069}

[[剪枝否决时间的配置值]{style="font-family:宋体"}]{#struct_0_17565_x2166_1508346932}

[[PIM neighbor tracking (negotiated)]{lang="EN-US"}]{#struct_0_17565_x2166_1105071423}

[[邻居跟踪使能与否的协商情况]{style="font-family:宋体"}]{#struct_0_17565_x2166_x247949177}

[[PIM neighbor tracking (configured)]{lang="EN-US"}]{#struct_0_17565_x2166_x422708317}

[[邻居跟踪使能与否的配置情况]{style="font-family:宋体"}]{#struct_0_17565_x2166_x2063686060}

[[PIM generation ID]{lang="EN-US"}]{#struct_0_17565_x2166_1218007717}

[[Generation_ID]{lang="SV"}]{#struct_0_17565_x2166_1643084223}[参数值]{style="font-family:宋体"}

[[PIM require generation ID]{lang="EN-US"}]{#struct_0_17565_x2166_1076982123}

[[是否使能不接受无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_17565_x2166_x422773853}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[PIM hello hold interval]{lang="EN-US"}]{#struct_0_17565_x2166_1519083337}

[[保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_871737174}[邻居的可达状态的时间]{style="font-family:宋体"}

[[PIM assert hold interval]{lang="EN-US"}]{#struct_0_17565_x2166_x229987721}

[[保持断言状态的时间]{style="font-family:宋体"}]{#struct_0_17565_x2166_x422839389}

[[PIM triggered hello delay]{lang="EN-US"}]{#struct_0_17565_x2166_659888983}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_x1652284743}[报文的最大延迟时间]{style="font-family:宋体"}

[[PIM J/P interval]{lang="EN-US"}]{#struct_0_17565_x2166_958094496}

[[发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_x422904925}[剪枝报文的时间间隔]{style="font-family:宋体"}

[[PIM J/P hold interval]{lang="EN-US"}]{#struct_0_17565_x2166_1932865359}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_x1307587313}[剪枝状态的保持时间]{style="font-family:宋体"}

[[PIM BSR domain border]{lang="EN-US"}]{#struct_0_17565_x2166_x1925116461}

[[该接口是否配置了]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_x422446173}[的服务边界]{style="font-family:宋体"}

[[PIM BFD]{lang="EN-US"}]{#struct_0_17565_x2166_338827303}

[[该接口是否使能了]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_327809556}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能]{style="font-family:宋体"}

[[Number of routers on network not using DR priority]{lang="EN-US"}]{#struct_0_17565_x2166_x1972336048}

[[该接口所在网段上没有使用]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_17565_x2166_x422511709}[优先级字段的路由器数量]{style="font-family:宋体"}

[[Number of routers on network not using LAN delay]{lang="EN-US"}]{#struct_0_17565_x2166_x457738796}

[[该接口所在网段上未使用]{style="font-family:宋体"}[LAN-delay]{lang="EN-US"}]{#struct_0_17565_x2166_x1640458355}[字段的路由器数量]{style="font-family:宋体"}

[[Number of routers on network not using neighbor tracking]{lang="EN-US"}]{#struct_0_17565_x2166_x422970464}

[[该接口所在网段上未使能邻居跟踪的路由器数量]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1607597641}

::: {#1776749277 .myid}
[]{#_Toc400703921}[]{#_Toc398976095}[]{#struct_0_17565_x2166_236661048}[]{#_Toc404789757}

**PIM \-- PIM配置命令 \-- display pim nbma-link**

------------------------------------------------------------------------

[**[display pim nbma-link ]{lang="EN-US"}**]{#struct_0_17565_x2166_x182237307}[命令用来显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模块维护的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_87532057}

[**[display pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **nbma-link** \[ **interface** { *interface-type interface-number* } \]]{lang="EN-US"}]{#struct_0_17565_x2166_x1891971304}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1669667495}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1329422893}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_228020652}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_304698339}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x335100517}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x130293231}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1705748855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1245514676}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_737187721}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_17565_x2166_1483891599}[：接口类型和接口编号，显示指定接口上的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[维护的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_836323753}

[[\#]{lang="EN-US"}]{#struct_0_17565_x2166_x354443817}[显示公网所有]{style="font-family:宋体"}[PIM]{lang="EN-US"}[维护的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim nbma-link   ]{lang="EN-US"}]{#struct_0_17565_x2166_x926138366}

[Interface: Tunnel1]{lang="EN-US"}

[Number of links: 1]{lang="EN-US"}

[    Remote address: 10.0.0.1]{lang="EN-US"}

[      Private index    : 0XCC000000]{lang="EN-US"}

[      Private interface: Multicast-NBMA0]{lang="EN-US"}

[Interface: Tunnel2]{lang="EN-US"}

[Number of links: 1]{lang="EN-US"}

[    Remote address: 20.0.0.2]{lang="EN-US"}

[      Private index    : 0XCC000001]{lang="EN-US"}

[      Private interface: Multicast-NBMA1 ]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_17565_x2166_x950032985}[显示公网指定]{style="font-family:宋体"}[PIM]{lang="EN-US"}[维护的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口上对端的信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim nbma-link interface tunnel 1]{lang="EN-US"}]{#struct_0_17565_x2166_132581479}

[Interface: Tunnel1]{lang="EN-US"}

[Number of links: 1]{lang="EN-US"}

[    Remote address: 10.0.0.1]{lang="EN-US"}

[      Private index    : 0XCC000000]{lang="EN-US"}

[      Private interface: Multicast-NBMA0]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display pim nbma-link]{lang="EN-US"}]{#struct_0_17565_x2166_911695987}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_498113334}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_1802744989}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1732707420}

[[Interface      ]{lang="EN-US"}]{#struct_0_17565_x2166_996175935}

[[隧道接口名称]{style="font-family:宋体"}]{#struct_0_17565_x2166_1399460462}

[[Number of links]{lang="EN-US"}]{#struct_0_17565_x2166_x166623479}

[[该隧道下的远端连接的个数]{style="font-family:宋体"}]{#struct_0_17565_x2166_x119569312}

[[Remote address]{lang="EN-US"}]{#struct_0_17565_x2166_x1685653253}

[[远端连接的地址]{style="font-family:宋体"}]{#struct_0_17565_x2166_236595512}

[[Private index]{lang="EN-US"}]{#struct_0_17565_x2166_x2001171193}

[[对应远端连接的索引]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1329488429}

[[Private interface]{lang="EN-US"}]{#struct_0_17565_x2166_x926203902}

[[对应远端连接的接口]{style="font-family:宋体"}]{#struct_0_17565_x2166_1802679453}

[ ]{lang="EN-US"}

::: {#1909605857 .myid}
[]{#_Toc404789758}[]{#struct_0_17565_x2166_364719700}[]{#_Toc288743022}[]{#_Toc403121863}[]{#_Toc403459842}

**PIM \-- PIM配置命令 \-- display pim neighbor**

------------------------------------------------------------------------

[**[display pim neighbor]{lang="EN-US"}**]{#struct_0_17565_x2166_x728763347}[命令用来显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1469079375}

[**[display pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **neighbor** \[ *neighbor-address* \| **interface** *interface-type interface-number* \| **verbose** \] \*]{lang="EN-US"}]{#struct_0_17565_x2166_926491540}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x423036000}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1230629058}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x196077693}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x818636333}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_1481489426}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x203667789}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1999876227}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1101518647}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x3356645}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[*[neighbor-address]{lang="EN-US"}*]{#struct_0_17565_x2166_x423101536}[：]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，显示指定]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_17565_x2166_1093039471}[：接口类型和接口编号，显示指定接口上的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居信息。如果未指定本参数，将显示所有接口上的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17565_x2166_2037792575}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_103477686}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1694356598}[显示公网实例所有]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim neighbor]{lang="EN-US"}]{#struct_0_17565_x2166_x2116146473}

[ Total Number of Neighbors = 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Neighbor        Interface           Uptime   Expires  DR-Priority Mode]{lang="EN-US"}

[ 10.1.1.2        GE1/0/1             02:50:49 00:01:31 1           B]{lang="EN-US"}

[ 20.1.1.2        GE1/0/2             02:49:39 00:01:42 1           P]{lang="EN-US"}

[]{#_Toc116822996}[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1136939717}[显示公网实例中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[11.110.0.20]{lang="EN-US"}[的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim neighbor 11.110.0.20 verbose]{lang="EN-US"}]{#struct_0_17565_x2166_x423167072}

[ Neighbor: 11.110.0.20]{lang="EN-US"}

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

[     RPF proxy vector: Enabled]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display pim neighbor]{lang="EN-US"}]{#struct_0_17565_x2166_1509067829}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x178922822}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2011659844}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_1163575067}

[[Total Number of Neighbors]{lang="EN-US"}]{#struct_0_17565_x2166_197958186}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x422708320}[邻居的总数]{style="font-family:宋体"}

[[Neighbor]{lang="EN-US"}]{#struct_0_17565_x2166_x2063227307}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x224096705}[邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_17565_x2166_1104222014}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1378403595}[邻居所在接口的名称]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_17565_x2166_x1759606577}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x422773856}[邻居已存在的时间]{style="font-family:宋体"}

[[Expires/Expiry time]{lang="EN-US"}]{#struct_0_17565_x2166_1519279945}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x726452825}[邻居超时的剩余时间，]{style="font-family:宋体"}[never]{lang="EN-US"}[表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居永不超时，即永远可达]{style="font-family:宋体"}

[[DR-Priority/DR Priority]{lang="EN-US"}]{#struct_0_17565_x2166_x1042224497}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1702821230}[邻居的优先级]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_17565_x2166_1381098146}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x422839392}[邻居的模式，]{style="font-family:宋体"}[B]{lang="EN-US"}[表示双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模式，]{style="font-family:宋体"}[P]{lang="EN-US"}[表示开启]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量功能，显示为空则表示非双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模式且关闭]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量功能]{style="font-family:宋体"}

[[Generation ID]{lang="EN-US"}]{#struct_0_17565_x2166_659168086}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_2051684863}[邻居的]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[（状态随机数）]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_17565_x2166_1400391272}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1496422567}[邻居的生存时间，]{style="font-family:宋体"}[forever]{lang="EN-US"}[表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居永远存在，即永远可达]{style="font-family:宋体"}

[[LAN delay]{lang="EN-US"}]{#struct_0_17565_x2166_x422904928}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1933717327}[报文在共享网段中的传输延迟]{style="font-family:宋体"}

[[Override interval]{lang="EN-US"}]{#struct_0_17565_x2166_x501696789}

[[剪枝否决的时间间隔]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1837049119}

[[State refresh interval]{lang="EN-US"}]{#struct_0_17565_x2166_x524166616}

[[状态刷新的时间间隔，只有当]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x422446176}[邻居工作在]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[模式下且具备状态刷新能力时才会显示本字段]{style="font-family:宋体"}

[[Neighbor tracking]{lang="EN-US"}]{#struct_0_17565_x2166_339154983}

[[邻居跟踪功能是否使能]{style="font-family:宋体"}]{#struct_0_17565_x2166_x864733408}

[[Bidirectional PIM]{lang="EN-US"}]{#struct_0_17565_x2166_2522936}

[[双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x422511712}[是否使能]{style="font-family:宋体"}

[[RPF proxy vector]{lang="EN-US"}]{#struct_0_17565_x2166_x1538439936}

[[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1538505472}[代理向量功能（请参见"]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播配置指导"中的"组播]{style="font-family:宋体"}[VPN]{lang="EN-US"}["）是否使能]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#968535103 .myid}
[]{#_Toc404789759}[]{#struct_0_17565_x2166_x457148971}[]{#_Toc288743023}[]{#_Toc94588265}[]{#_Toc80176804}

**PIM \-- PIM配置命令 \-- display pim routing-table**

------------------------------------------------------------------------

[**[display pim routing-table]{lang="EN-US"}**]{#struct_0_17565_x2166_1051236057}[命令用来显示]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[路由表的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1778280884}

[**[display pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **routing-table** \[ *group-address* \[ **mask** { *mask-length* \| *mask* } \] \| *source-address* \[ **mask** { *mask-length* \| *mask* } \] \| **flags** *flag-value* \| **fsm** \| **incoming-interface** *interface-type* *interface-number* \| **mode** *mode-type* \| **outgoing-interface** { **exclude** \| **include** \| **match** } *interface-type* *interface-number* \| **proxy** \] \*]{lang="EN-US"}]{#struct_0_17565_x2166_x2073610944}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x658673883}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1184131839}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x537139646}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1953820088}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x422970463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1607925321}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x899455434}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_528647159}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x93660284}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_17565_x2166_1201785871}[：组播组地址，显示指定组播组的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项，取值范围为]{style="font-family:宋体"}[224.0.0.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_17565_x2166_x691377513}[：组播源地址，显示包含指定组播源的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_17565_x2166_x989750659}[：指定组播组或组播源地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_17565_x2166_x202554102}[：指定组播组或组播源地址的掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[flags]{lang="EN-US"}***[ flag-value]{lang="EN-US"}*]{#struct_0_17565_x2166_x423035999}[：]{style="font-family:宋体"}[PIM]{lang="EN-US"}[标志，显示包含指定标志的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。如果未指定本参数，将显示包含所有标志的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值及含义如下**：**]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[2msdp]{lang="EN-US"}**]{#struct_0_17565_x2166_763011738}[：表示准备向]{style="font-family:
宋体"}[MSDP]{lang="EN-US"}[发出通知，在下一个]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中包含的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[act]{lang="EN-US"}**]{#struct_0_17565_x2166_x1888379476}[：表示已经有实际数据到达的]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[del]{lang="EN-US"}**]{#struct_0_17565_x2166_x1130809554}[：表示计划删除的]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[exprune]{lang="EN-US"}**]{#struct_0_17565_x2166_x1088236583}[：表示某些出接口被其它组播路由协议剪枝的]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ext]{lang="EN-US"}**]{#struct_0_17565_x2166_2016156584}[：表示包含了由其它组播路由协议提供出接口的]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[loc]{lang="EN-US"}**]{#struct_0_17565_x2166_1522590081}[：表示在与组播源处于同一网段的路由器上的]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[msdp]{lang="EN-US"}**]{#struct_0_17565_x2166_x1076874428}[：表示从]{style="font-family:
宋体"}[MSDP]{lang="EN-US"}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中学习到的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[niif]{lang="EN-US"}**]{#struct_0_17565_x2166_1484041549}[：表示未确定入接口的]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nonbr]{lang="EN-US"}**]{#struct_0_17565_x2166_x490804207}[：表示]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[邻居查找失败的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rpt]{lang="EN-US"}**]{#struct_0_17565_x2166_x423101535}[：表示向]{style="font-family:
宋体"}[RP]{lang="EN-US"}[方向发送过（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）]{style="font-family:宋体"}[RPT]{lang="EN-US"}[位剪枝的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rq]{lang="EN-US"}**]{#struct_0_17565_x2166_1093105007}[：表示]{lang="EN-US" style="font-family:宋体"}[Data]{lang="EN-US"}[-MDT]{lang="EN-US"}[切换接收端的]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spt]{lang="EN-US"}**]{#struct_0_17565_x2166_x333662625}[：表示]{lang="EN-US" style="font-family:宋体"}[SPT]{lang="EN-US"}[上的]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sq]{lang="EN-US"}**]{#struct_0_17565_x2166_x1569731575}[：表示]{lang="EN-US" style="font-family:宋体"}[Data]{lang="EN-US"}[-MDT]{lang="EN-US"}[切换发起端的]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[swt]{lang="EN-US"}**]{#struct_0_17565_x2166_1308659565}[：表示正处于向]{style="font-family:
宋体"}[SPT]{lang="EN-US"}[切换过程中的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wc]{lang="EN-US"}**]{#struct_0_17565_x2166_870071573}[：表示带]{style="font-family:
宋体"}[WC]{lang="EN-US"}[通配符的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_17565_x2166_762414197}[：显示有限状态机的详细信息。]{style="font-family:宋体"}

[**[incoming-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17565_x2166_x1471705386}[：显示指定入接口的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。如果未指定本参数，将显示所有入接口的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[**[mode ]{lang="EN-US"}***[mode-type]{lang="EN-US"}*]{#struct_0_17565_x2166_x735700660}[：]{style="font-family:宋体"}[PIM]{lang="EN-US"}[模式，显示指定模式下的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。如果未指定本参数，将显示所有模式下的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}*[mode-type]{lang="EN-US"}*[的取值及含义如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bidir]{lang="EN-US"}**]{#struct_0_17565_x2166_x423167071}[：表示双向]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[模式；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dm]{lang="EN-US"}**]{#struct_0_17565_x2166_1508871221}[：表示]{lang="EN-US" style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[模式；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sm]{lang="EN-US"}**]{#struct_0_17565_x2166_x1581148290}[：表示]{lang="EN-US" style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[模式；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ssm]{lang="EN-US"}**]{#struct_0_17565_x2166_1030333481}[：表示]{lang="EN-US" style="font-family:宋体"}[PIM-SSM]{lang="EN-US"}[模式。]{lang="EN-US" style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}**[ { **exclude** \| **include** \| **match** } *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_17565_x2166_x1860859439}[：显示指定出接口的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。其中，]{style="font-family:宋体"}**[exclude]{lang="EN-US"}**[表示不包含指定接口；]{style="font-family:宋体"}**[include]{lang="EN-US"}**[表示包含指定接口；]{style="font-family:宋体"}**[match]{lang="EN-US"}**[表示包含且仅包含指定接口。如果未指定本参数，将显示所有出接口的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项。]{style="font-family:宋体"}

[**[proxy]{lang="EN-US"}**]{#struct_0_17565_x2166_x1538177792}[：显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项使用的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x680317198}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x780557712}[显示公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由表的内容。]{style="font-family:宋体"}

[]{#_Toc94588266}[]{#_Toc80176805}[]{#struct_0_17565_x2166_x422708319}[]{#_Toc87787261}[]{#_Toc87852140}[]{#_Toc87852919}[]{#_Toc87853700}[]{#_Toc87867739}[]{#_Toc87787262}[]{#_Toc87852141}[]{#_Toc87852920}[]{#_Toc87853701}[]{#_Toc87867740}[]{#_Toc87787263}[]{#_Toc87852142}[]{#_Toc87852921}[]{#_Toc87853702}[]{#_Toc87867741}[]{#_Toc87787264}[]{#_Toc87852143}[]{#_Toc87852922}[]{#_Toc87853703}[]{#_Toc87867742}[]{#_Toc87787265}[]{#_Toc87852144}[]{#_Toc87852923}[]{#_Toc87853704}[]{#_Toc87867743}[]{#_Toc87787266}[]{#_Toc87852145}[]{#_Toc87852924}[]{#_Toc87853705}[]{#_Toc87867744}[]{#_Toc87787267}[]{#_Toc87852146}[]{#_Toc87852925}[]{#_Toc87853706}[]{#_Toc87867745}[]{#_Toc87787269}[]{#_Toc87852148}[]{#_Toc87852927}[]{#_Toc87853708}[]{#_Toc87867747}[]{#_Toc87787270}[]{#_Toc87852149}[]{#_Toc87852928}[]{#_Toc87853709}[]{#_Toc87867748}[]{#_Toc87787271}[]{#_Toc87852150}[]{#_Toc87852929}[]{#_Toc87853710}[]{#_Toc87867749}[]{#_Toc87442582}[]{#_Toc87787274}[]{#_Toc87852153}[]{#_Toc87852932}[]{#_Toc87853713}[]{#_Toc87867752}[]{#_Toc87442589}[]{#_Toc87787281}[]{#_Toc87852160}[]{#_Toc87852939}[]{#_Toc87853720}[]{#_Toc87867759}[]{#_Toc87442596}[]{#_Toc87787288}[]{#_Toc87852167}[]{#_Toc87852946}[]{#_Toc87853727}[]{#_Toc87867766}[\<Sysname\> display pim routing-table]{lang="EN-US"}

[ Total 0 (\*, G) entries; 1 (S, G) entries]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (172.168.0.12, 227.0.0.1)]{lang="EN-US"}

[     RP: 2.2.2.2]{lang="EN-US"}

[     Protocol: pim-sm, Flag: SPT LOC ACT]{lang="EN-US"}

[     UpTime: 02:54:43]{lang="EN-US"}

[     Upstream interface: GigabitEthernet1/0/1]{lang="EN-US"}

[         Upstream neighbor: NULL]{lang="EN-US"}

[         RPF prime neighbor: NULL]{lang="EN-US"}

[     Downstream interface information:]{lang="EN-US"}

[     Total number of downstream interfaces: 1]{lang="EN-US"}

[         1: Vlan-interface2]{lang="EN-US"}

[             ]{lang="EN-US"}[Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47]{lang="PT-BR"}

[ ]{lang="PT-BR"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1802876061}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[应用组网]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由表的内容。]{style="font-family:宋体"}

[[\<Sysname\> display pim routing-table]{lang="EN-US"}]{#struct_0_17565_x2166_1376128030}

[ Total 0 (\*, G) entries; 1 (S, G) entries]{lang="EN-US"}

[ ]{lang="EN-US"}

[ (172.168.0.12, 227.0.0.1)]{lang="EN-US"}

[     RP: 2.2.2.2]{lang="EN-US"}

[     Protocol: pim-sm, Flag: SPT LOC ACT]{lang="EN-US"}

[     UpTime: 02:54:43]{lang="EN-US"}

[     Upstream interface: Tunnel0, 13.1.1.1]{lang="EN-US"}

[         Upstream neighbor: 12.1.1.1]{lang="EN-US"}

[         RPF prime neighbor: 12.1.1.1]{lang="EN-US"}

[     Downstream interface information:]{lang="EN-US"}

[     Total number of downstream interfaces: 1]{lang="EN-US"}

[         1: Tunnel0, 13.1.1.2]{lang="EN-US"}

[             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47]{lang="EN-US"}

[ ]{lang="PT-BR"}

[]{#_Toc116822997}[[表1-10 ]{lang="EN-US"}[display pim routing-table]{lang="EN-US"}]{#struct_0_17565_x2166_x2062768556}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x182631588}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1163403745}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_1999295592}

[[Total 0 (\*, G) entries; 1 (S, G) entries]{lang="EN-US"}]{#struct_0_17565_x2166_x1998276937}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1123473247}[路由表中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）与（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的总数]{style="font-family:宋体"}

[[(172.168.0.12, 227.0.0.1)]{lang="EN-US"}]{#struct_0_17565_x2166_x422773855}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1519476553}[路由表中的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_17565_x2166_514584019}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1944203617}[的模式]{style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_17565_x2166_1659752316}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1161282696}[路由表中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACT]{lang="EN-US"}]{#struct_0_17565_x2166_x422839391}[：表示已有实际数据到达]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEL]{lang="EN-US"}]{#struct_0_17565_x2166_659364694}[：表示计划要删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EXPRUNE]{lang="EN-US"}]{#struct_0_17565_x2166_1169564467}[：表示某些出接口被其它组播路由协议剪枝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EXT]{lang="EN-US"}]{#struct_0_17565_x2166_2140284303}[：表示包含了由其它组播路由协议提供的出接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LOC]{lang="EN-US"}]{#struct_0_17565_x2166_x1706531673}[：表示与组播源处于同一网段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NIIF]{lang="EN-US"}]{#struct_0_17565_x2166_x422904927}[：表示未确定入接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONBR]{lang="EN-US"}]{#struct_0_17565_x2166_1932734287}[：表示]{lang="EN-US" style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居查找失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RPT]{lang="EN-US"}]{#struct_0_17565_x2166_x907197882}[：表示向]{lang="EN-US" style="font-family:宋体"}[RP]{lang="EN-US"}[方向发送过（]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[G]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}[RPT]{lang="EN-US"}[位剪枝]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPT]{lang="EN-US"}]{#struct_0_17565_x2166_x1821880664}[：表示在]{lang="EN-US" style="font-family:宋体"}[SPT]{lang="EN-US"}[上]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SWT]{lang="EN-US"}]{#struct_0_17565_x2166_1317079662}[：表示正在向]{lang="EN-US" style="font-family:宋体"}[SPT]{lang="EN-US"}[切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WC]{lang="EN-US"}]{#struct_0_17565_x2166_x422446175}[：表示带]{style="font-family:宋体"}[WC]{lang="EN-US"}[通配符]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_17565_x2166_339220519}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_17565_x2166_865250753}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项已存在的时间]{style="font-family:宋体"}

[[Upstream interface]{lang="EN-US"}]{#struct_0_17565_x2166_x318042598}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_17565_x2166_x2068256646}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的入接口，使能了]{style="font-family:宋体"}[nbma]{lang="EN-US"}[模式的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道口，显示远端连接]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Upstream neighbor]{lang="EN-US"}]{#struct_0_17565_x2166_x422511711}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_17565_x2166_x457214507}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的上游邻居]{style="font-family:宋体"}

[[RPF prime neighbor]{lang="EN-US"}]{#struct_0_17565_x2166_360193915}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_17565_x2166_560149454}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）或（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[邻居：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对（]{style="font-family:宋体"}]{#struct_0_17565_x2166_x985668135}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项来说，当该路由器是]{style="font-family:宋体"}[RP]{lang="EN-US"}[时，（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[邻居是]{style="font-family:宋体"}[NULL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对（]{style="font-family:宋体"}]{#struct_0_17565_x2166_1143113481}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项来说，当该路由器直连源时，（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[邻居是]{style="font-family:宋体"}[NULL]{lang="EN-US"}

[[RPF proxy vector]{lang="EN-US"}]{#struct_0_17565_x2166_x1538112256}

[[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1537915648}[代理向量，本字段只有在]{style="font-family:宋体"}[B]{lang="EN-US"}[类跨]{style="font-family:宋体"}[AS]{lang="EN-US"}[的]{style="font-family:宋体"}[MD VPN]{lang="EN-US"}[（请参见"]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播配置指导"中的"组播]{style="font-family:宋体"}[VPN]{lang="EN-US"}["）组网中才会显示]{style="font-family:宋体"}

[[Downstream interface information]{lang="EN-US"}]{#struct_0_17565_x2166_2056245012}

[[下游接口的信息，包括：]{style="font-family:宋体"}]{#struct_0_17565_x2166_228905288}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的总数]{style="font-family:宋体"}]{#struct_0_17565_x2166_113410483}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的名称]{style="font-family:宋体"}]{#struct_0_17565_x2166_1143047945}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口使用的协议类型]{style="font-family:宋体"}]{#struct_0_17565_x2166_x609485613}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的存在时间]{style="font-family:宋体"}]{#struct_0_17565_x2166_1565407337}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口的超时时间]{style="font-family:宋体"}]{#struct_0_17565_x2166_1399591534}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下游接口（]{style="font-family:宋体"}]{#struct_0_17565_x2166_x708385938}[ADVPN]{lang="EN-US"}[隧道口）对应的隧道远端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1537981184}[在]{style="font-family:宋体"}[PE]{lang="EN-US"}[设备上显示公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项使用的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim routing-table proxy]{lang="EN-US"}]{#struct_0_17565_x2166_x117403358}

[ (100.0.0.8, 232.1.1.1)]{lang="EN-US"}

[    Proxy: 10:1/192.168.0.4]{lang="EN-US"}

[    Assigner: 0.0.0.0         Origin: BGP MDT]{lang="EN-US"}

[    Uptime: 02:08:18          Expires: Off]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x182160177}[在]{style="font-family:宋体"}[P]{lang="EN-US"}[设备上显示公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项使用的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim routing-table proxy]{lang="EN-US"}]{#struct_0_17565_x2166_x1538439935}

[(100.0.0.8, 232.1.1.1)]{lang="EN-US"}

[    Proxy: 10:1/192.168.0.4]{lang="EN-US"}

[    Assigner: 1.0.3.1         Origin: PIM]{lang="EN-US"}

[    Uptime: 02:19:33          Expires: 00:02:12]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1989112595}[在]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[设备上显示公网实例]{style="font-family:宋体"}[PIM]{lang="EN-US"}[路由项使用的]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim routing-table proxy]{lang="EN-US"}]{#struct_0_17565_x2166_x1538505471}

[(100.0.0.1, 232.1.1.1)]{lang="EN-US"}

[    Proxy: 10:1/local]{lang="EN-US"}

[    Assigner: 1.0.5.9         Origin: PIM]{lang="EN-US"}

[    Uptime: 02:22:04          Expires: 00:02:35]{lang="EN-US"}

[ (100.0.0.8, 232.1.1.1)]{lang="EN-US"}

[    Proxy: 10:1/local]{lang="EN-US"}

[    Assigner: 1.0.4.1         Origin: PIM]{lang="EN-US"}

[    Uptime: 02:21:10          Expires: 00:02:35]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display pim routing-table proxy]{lang="EN-US"}]{#struct_0_17565_x2166_907753909}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_332135292}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1591527150}

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1538308863}

[[Proxy]{lang="EN-US"}]{#struct_0_17565_x2166_1231048843}

[[代理向量信息，包括]{style="font-family:宋体"}[RD]{lang="EN-US"}]{#struct_0_17565_x2166_x1538374399}[（]{style="font-family:宋体"}[Route Distinguisher]{lang="EN-US"}[，路由标识符）和]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量的地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量为本地地址（比如在]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[上）]{style="font-family:宋体"}

[[Assigner]{lang="EN-US"}]{#struct_0_17565_x2166_x477109185}

[[分配]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1538177791}[代理向量的设备地址：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_17565_x2166_x435994781}[PE]{lang="EN-US"}[上，]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量是从]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[路由中获取的，显示为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1538243327}[PE]{lang="EN-US"}[上，]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量是从下游]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居发来的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[加入报文中学到的，显示为下游]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居的接口地址]{style="font-family:宋体"}

[[Origin]{lang="EN-US"}]{#struct_0_17565_x2166_x1192993236}

[[产生]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1538046719}[代理向量的协议：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_17565_x2166_1977794210}[PE]{lang="EN-US"}[上，]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量是从]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}[路由中获取的，显示为]{style="font-family:宋体"}[BGP MDT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1538112255}[PE]{lang="EN-US"}[上，]{style="font-family:宋体"}[RPF]{lang="EN-US"}[代理向量是从下游]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居发来的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[加入报文中学到的，显示为]{style="font-family:宋体"}[PIM]{lang="EN-US"}

[[Uptime]{lang="EN-US"}]{#struct_0_17565_x2166_1445085622}

[[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1537915647}[代理向量已存在的时间]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_17565_x2166_1921198727}

[[RPF]{lang="EN-US"}]{#struct_0_17565_x2166_x1537981183}[代理向量的的超时剩余时间，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示该定时器关闭]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#49471059 .myid}
[]{#_Toc404789760}[]{#struct_0_17565_x2166_1142982409}[]{#_Toc288743024}

**PIM \-- PIM配置命令 \-- display pim rp-info**

------------------------------------------------------------------------

[**[display pim rp-info]{lang="EN-US"}**]{#struct_0_17565_x2166_1298684281}[命令用来显示]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[域中的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2092619041}

[**[display pim ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] **rp-info** \[ *group-address* \]]{lang="EN-US"}]{#struct_0_17565_x2166_x1008451257}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1217022865}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1720771595}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2061767809}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_7139932}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x293147177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1142916873}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1781168368}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x771071578}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x1497461506}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_17565_x2166_x594840205}[：组播组地址，显示指定组播组所对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示所有组播组对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1315297624}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x982040072}[显示公网实例中组播组]{style="font-family:宋体"}[224.0.1.1]{lang="EN-US"}[所对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[]{#_Toc94588267}[]{#_Toc78346652}[]{#struct_0_17565_x2166_1143375625}[]{#_Toc87787291}[]{#_Toc87852170}[]{#_Toc87852949}[]{#_Toc87853730}[]{#_Toc87867769}[]{#_Toc87787293}[]{#_Toc87852172}[]{#_Toc87852951}[]{#_Toc87853732}[]{#_Toc87867771}[\<Sysname\> display pim rp-info 224.0.1.1]{lang="EN-US"}

[ BSR RP address is: 2.2.2.2]{lang="EN-US"}

[     Priority: 192]{lang="EN-US"}

[     HoldTime: 180]{lang="EN-US"}

[     Uptime: 03:01:10]{lang="EN-US"}

[     Expires: 00:02:30]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Static RP address is: 3.3.3.5]{lang="EN-US"}

[     Preferred: Yes]{lang="EN-US"}

[     Configured ACL: 2003]{lang="EN-US"}

[ ]{lang="EN-US"}

[ RP mapping for this group is: 3.3.3.5]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Anycast-RP 3.3.3.5 members:]{lang="EN-US"}

[     Member address           State]{lang="EN-US"}

[     1.1.0.1                  Active]{lang="EN-US"}

[     1.2.0.2                  Local]{lang="EN-US"}

[     1.2.0.1                  Remote]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_506521130}[显示公网实例中所有组播组对应的]{style="font-family:宋体"}[RP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim rp-info]{lang="EN-US"}]{#struct_0_17565_x2166_1143310089}

[ ]{lang="EN-US"}[BSR RP information:]{lang="IT"}

[   Scope: non-scoped]{lang="IT"}

[     ]{lang="IT"}[Group/MaskLen: 224.0.0.0/4]{lang="EN-US"}

[       RP address               Priority  HoldTime  Uptime    Expires]{lang="EN-US"}

[       1.1.1.1 (local)          192       180       03:01:36  00:02:29]{lang="EN-US"}

[       2.2.2.2                  192       180       1d:13h    00:02:02]{lang="EN-US"}

[     Group/MaskLen: 225.1.0.0/16 \[B\]]{lang="EN-US"}

[       RP address               Priority  HoldTime  Uptime    Expires]{lang="EN-US"}

[       3.3.3.3                  192       180       12w:5d    00:02:05]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Static RP information:]{lang="EN-US"}

[       RP address               ACL   Mode    Preferred]{lang="EN-US"}

[       3.3.3.1                  2000  pim-sm  No]{lang="EN-US"}

[       3.3.3.2                  2001  bidir   Yes]{lang="EN-US"}

[       3.3.3.3                  2002  pim-sm  No]{lang="EN-US"}

[       3.3.3.4                        pim-sm  No]{lang="EN-US"}

[       3.3.3.5                  2002  pim-sm  Yes]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Anycast-RP information:]{lang="EN-US"}

[       RP address               Member address           State]{lang="EN-US"}

[       3.3.3.5                  1.1.0.1                  Active]{lang="EN-US"}

[       3.3.3.5                  1.1.0.2                  Local]{lang="EN-US"}

[       3.3.3.5                  1.2.0.1                  Remote]{lang="EN-US"}

[]{#_Toc116822999}[]{#_Toc116823000}[[表1-12 ]{lang="EN-US"}[display pim rp-info]{lang="EN-US"}]{#struct_0_17565_x2166_x275037199}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x154018058}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_x488945511}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_1171819607}

[[BSR RP address is]{lang="EN-US"}]{#struct_0_17565_x2166_1307253388}

[[RP]{lang="EN-US"}]{#struct_0_17565_x2166_x463753335}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[BSR RP information]{lang="EN-US"}]{#struct_0_17565_x2166_550993723}

[[BSR RP]{lang="EN-US"}]{#struct_0_17565_x2166_1143244553}[信息]{style="font-family:宋体"}

[[Scope]{lang="EN-US"}]{#struct_0_17565_x2166_118583727}

[[域]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1198336960}

[[Group/MaskLen]{lang="EN-US"}]{#struct_0_17565_x2166_x1950959992}

[[RP]{lang="EN-US"}]{#struct_0_17565_x2166_1010503199}[所服务的组播组]{style="font-family:宋体"}

[[\[B\]]{lang="EN-US"}]{#struct_0_17565_x2166_x795105606}

[[表示]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_17565_x2166_1143179017}[服务于双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果不显示该字段，则表示]{style="font-family:宋体"}[RP]{lang="EN-US"}[服务于]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}

[[RP address]{lang="EN-US"}]{#struct_0_17565_x2166_x1489085141}

[[RP]{lang="EN-US"}]{#struct_0_17565_x2166_x2013773374}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[local]{lang="EN-US"}[表示本地地址]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_17565_x2166_1143637769}

[[RP]{lang="EN-US"}]{#struct_0_17565_x2166_1308425351}[的优先级]{style="font-family:宋体"}

[[HoldTime]{lang="EN-US"}]{#struct_0_17565_x2166_x1079940504}

[[RP]{lang="EN-US"}]{#struct_0_17565_x2166_633079272}[的超时时间]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_17565_x2166_x1839472697}

[[RP]{lang="EN-US"}]{#struct_0_17565_x2166_1143572233}[已存在的时间]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_17565_x2166_x1824105988}

[[RP]{lang="EN-US"}]{#struct_0_17565_x2166_x1725859734}[超时的剩余时间]{style="font-family:宋体"}

[[Static RP information]{lang="EN-US"}]{#struct_0_17565_x2166_x1212858503}

[[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_17565_x2166_x1376446142}[信息]{style="font-family:宋体"}

[[Static RP address is/RP address]{lang="EN-US"}]{#struct_0_17565_x2166_1143113482}

[[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_17565_x2166_2056441620}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Preferred]{lang="EN-US"}]{#struct_0_17565_x2166_x593320837}

[[是否指定了静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_17565_x2166_x1950276128}[优先]{style="font-family:宋体"}

[[Configured ACL/ACL]{lang="EN-US"}]{#struct_0_17565_x2166_1143047946}

[[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_17565_x2166_x609682221}[所服务的组播组列表]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_17565_x2166_407636075}

[[为]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}]{#struct_0_17565_x2166_x110551072}[服务还是为双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[服务]{style="font-family:宋体"}

[[RP mapping for this group]{lang="EN-US"}]{#struct_0_17565_x2166_1142982410}

[[服务于当前组播组的]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_17565_x2166_1298094458}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Anycast-RP 3.3.3.5 members]{lang="EN-US"}]{#struct_0_17565_x2166_x860209758}

[[Anycast-RP 3.3.3.5]{lang="EN-US"}]{#struct_0_17565_x2166_x1627131808}[的成员]{style="font-family:宋体"}

[[Member address]{lang="EN-US"}]{#struct_0_17565_x2166_x860144222}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_17565_x2166_1039594283}[成员的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_17565_x2166_x860078686}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_17565_x2166_1889827712}[成员地址的来源：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_17565_x2166_x860013150}[：表示]{lang="EN-US" style="font-family:宋体"}[本端激活接口的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_17565_x2166_1044741676}[：表示本端未激活接口的地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote]{lang="EN-US"}]{#struct_0_17565_x2166_x860471902}[：表示远端的地址]{style="font-family:宋体"}

[[Anycast-RP information]{lang="EN-US"}]{#struct_0_17565_x2166_x1658415649}

[[Anycast-RP]{lang="EN-US"}]{#struct_0_17565_x2166_x860406366}[信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#818962442 .myid}
[]{#_Toc288743025}[]{#_Toc94588274}[]{#_Toc80176807}[]{#_Toc311539015}[]{#_Toc404789761}[]{#struct_0_17565_x2166_1818569500}[]{#_Toc139255976}[]{#_Toc139259818}[]{#_Toc139267740}[]{#_Toc139269160}[]{#_Toc139366392}[]{#_Toc139448238}[]{#_Toc139255979}[]{#_Toc139259821}[]{#_Toc139267743}[]{#_Toc139269163}[]{#_Toc139366395}[]{#_Toc139448241}[]{#_Toc139255980}[]{#_Toc139259822}[]{#_Toc139267744}[]{#_Toc139269164}[]{#_Toc139366396}[]{#_Toc139448242}[]{#_Toc139255981}[]{#_Toc139259823}[]{#_Toc139267745}[]{#_Toc139269165}[]{#_Toc139366397}[]{#_Toc139448243}[]{#_Toc139255982}[]{#_Toc139259824}[]{#_Toc139267746}[]{#_Toc139269166}[]{#_Toc139366398}[]{#_Toc139448244}[]{#_Toc139255983}[]{#_Toc139259825}[]{#_Toc139267747}[]{#_Toc139269167}[]{#_Toc139366399}[]{#_Toc139448245}[]{#_Toc139255984}[]{#_Toc139259826}[]{#_Toc139267748}[]{#_Toc139269168}[]{#_Toc139366400}[]{#_Toc139448246}[]{#_Toc139255985}[]{#_Toc139259827}[]{#_Toc139267749}[]{#_Toc139269169}[]{#_Toc139366401}[]{#_Toc139448247}[]{#_Toc139255986}[]{#_Toc139259828}[]{#_Toc139267750}[]{#_Toc139269170}[]{#_Toc139366402}[]{#_Toc139448248}[]{#_Toc139255987}[]{#_Toc139259829}[]{#_Toc139267751}[]{#_Toc139269171}[]{#_Toc139366403}[]{#_Toc139448249}[]{#_Toc139255988}[]{#_Toc139259830}[]{#_Toc139267752}[]{#_Toc139269172}[]{#_Toc139366404}[]{#_Toc139448250}[]{#_Toc139255989}[]{#_Toc139259831}[]{#_Toc139267753}[]{#_Toc139269173}[]{#_Toc139366405}[]{#_Toc139448251}[]{#_Toc139255990}[]{#_Toc139259832}[]{#_Toc139267754}[]{#_Toc139269174}[]{#_Toc139366406}[]{#_Toc139448252}[]{#_Toc87787305}[]{#_Toc87852184}[]{#_Toc87852963}[]{#_Toc87853744}[]{#_Toc87867800}[]{#_Toc87787306}[]{#_Toc87852185}[]{#_Toc87852964}[]{#_Toc87853745}[]{#_Toc87867801}[]{#_Toc87787307}[]{#_Toc87852186}[]{#_Toc87852965}[]{#_Toc87853746}[]{#_Toc87867802}[]{#_Toc87787308}[]{#_Toc87852187}[]{#_Toc87852966}[]{#_Toc87853747}[]{#_Toc87867803}[]{#_Toc87787309}[]{#_Toc87852188}[]{#_Toc87852967}[]{#_Toc87853748}[]{#_Toc87867804}[]{#_Toc87787310}[]{#_Toc87852189}[]{#_Toc87852968}[]{#_Toc87853749}[]{#_Toc87867805}[]{#_Toc87787311}[]{#_Toc87852190}[]{#_Toc87852969}[]{#_Toc87853750}[]{#_Toc87867806}[]{#_Toc87787312}[]{#_Toc87852191}[]{#_Toc87852970}[]{#_Toc87853751}[]{#_Toc87867807}[]{#_Toc87787313}[]{#_Toc87852192}[]{#_Toc87852971}[]{#_Toc87853752}[]{#_Toc87867808}[]{#_Toc87787314}[]{#_Toc87852193}[]{#_Toc87852972}[]{#_Toc87853753}[]{#_Toc87867809}[]{#_Toc87787315}[]{#_Toc87852194}[]{#_Toc87852973}[]{#_Toc87853754}[]{#_Toc87867810}[]{#_Toc87787318}[]{#_Toc87852197}[]{#_Toc87852976}[]{#_Toc87853757}[]{#_Toc87867813}[]{#_Toc87787319}[]{#_Toc87852198}[]{#_Toc87852977}[]{#_Toc87853758}[]{#_Toc87867814}[]{#_Toc87787320}[]{#_Toc87852199}[]{#_Toc87852978}[]{#_Toc87853759}[]{#_Toc87867815}[]{#_Toc87787321}[]{#_Toc87852200}[]{#_Toc87852979}[]{#_Toc87853760}[]{#_Toc87867816}[]{#_Toc87787322}[]{#_Toc87852201}[]{#_Toc87852980}[]{#_Toc87853761}[]{#_Toc87867817}[]{#_Toc87787323}[]{#_Toc87852202}[]{#_Toc87852981}[]{#_Toc87853762}[]{#_Toc87867818}[]{#_Toc87787324}[]{#_Toc87852203}[]{#_Toc87852982}[]{#_Toc87853763}[]{#_Toc87867819}[]{#_Toc87787326}[]{#_Toc87852205}[]{#_Toc87852984}[]{#_Toc87853765}[]{#_Toc87867821}[]{#_Toc87787327}[]{#_Toc87852206}[]{#_Toc87852985}[]{#_Toc87853766}[]{#_Toc87867822}[]{#_Toc87787328}[]{#_Toc87852207}[]{#_Toc87852986}[]{#_Toc87853767}[]{#_Toc87867823}[]{#_Toc87787329}[]{#_Toc87852208}[]{#_Toc87852987}[]{#_Toc87853768}[]{#_Toc87867824}[]{#_Toc87787330}[]{#_Toc87852209}[]{#_Toc87852988}[]{#_Toc87853769}[]{#_Toc87867825}[]{#_Toc87787331}[]{#_Toc87852210}[]{#_Toc87852989}[]{#_Toc87853770}[]{#_Toc87867826}[]{#_Toc87787332}[]{#_Toc87852211}[]{#_Toc87852990}[]{#_Toc87853771}[]{#_Toc87867827}[]{#_Toc87787334}[]{#_Toc87852213}[]{#_Toc87852992}[]{#_Toc87853773}[]{#_Toc87867829}[]{#_Toc87787335}[]{#_Toc87852214}[]{#_Toc87852993}[]{#_Toc87853774}[]{#_Toc87867830}[]{#_Toc87787336}[]{#_Toc87852215}[]{#_Toc87852994}[]{#_Toc87853775}[]{#_Toc87867831}[]{#_Toc87787337}[]{#_Toc87852216}[]{#_Toc87852995}[]{#_Toc87853776}[]{#_Toc87867832}[]{#_Toc87787338}[]{#_Toc87852217}[]{#_Toc87852996}[]{#_Toc87853777}[]{#_Toc87867833}[]{#_Toc87787339}[]{#_Toc87852218}[]{#_Toc87852997}[]{#_Toc87853778}[]{#_Toc87867834}[]{#_Toc87442607}[]{#_Toc87787340}[]{#_Toc87852219}[]{#_Toc87852998}[]{#_Toc87853779}[]{#_Toc87867835}[]{#_Toc87442610}[]{#_Toc87787343}[]{#_Toc87852222}[]{#_Toc87853001}[]{#_Toc87853782}[]{#_Toc87867838}[]{#_Toc87442614}[]{#_Toc87787347}[]{#_Toc87852226}[]{#_Toc87853005}[]{#_Toc87853786}[]{#_Toc87867842}[]{#_Toc87442623}[]{#_Toc87787356}[]{#_Toc87852235}[]{#_Toc87853014}[]{#_Toc87853795}[]{#_Toc87867851}[]{#_Toc87442624}[]{#_Toc87787357}[]{#_Toc87852236}[]{#_Toc87853015}[]{#_Toc87853796}[]{#_Toc87867852}[]{#_Toc87442625}[]{#_Toc87787358}[]{#_Toc87852237}[]{#_Toc87853016}[]{#_Toc87853797}[]{#_Toc87867853}[]{#_Toc87442626}[]{#_Toc87787359}[]{#_Toc87852238}[]{#_Toc87853017}[]{#_Toc87853798}[]{#_Toc87867854}[]{#_Toc87442627}[]{#_Toc87787360}[]{#_Toc87852239}[]{#_Toc87853018}[]{#_Toc87853799}[]{#_Toc87867855}[]{#_Toc87442628}[]{#_Toc87787361}[]{#_Toc87852240}[]{#_Toc87853019}[]{#_Toc87853800}[]{#_Toc87867856}[]{#_Toc87442629}[]{#_Toc87787362}[]{#_Toc87852241}[]{#_Toc87853020}[]{#_Toc87853801}[]{#_Toc87867857}[]{#_Toc87442630}[]{#_Toc87787363}[]{#_Toc87852242}[]{#_Toc87853021}[]{#_Toc87853802}[]{#_Toc87867858}[]{#_Toc87442631}[]{#_Toc87787364}[]{#_Toc87852243}[]{#_Toc87853022}[]{#_Toc87853803}[]{#_Toc87867859}[]{#_Toc87442632}[]{#_Toc87787365}[]{#_Toc87852244}[]{#_Toc87853023}[]{#_Toc87853804}[]{#_Toc87867860}[]{#_Toc87442633}[]{#_Toc87787366}[]{#_Toc87852245}[]{#_Toc87853024}[]{#_Toc87853805}[]{#_Toc87867861}[]{#_Toc87442634}[]{#_Toc87787367}[]{#_Toc87852246}[]{#_Toc87853025}[]{#_Toc87853806}[]{#_Toc87867862}[]{#_Toc87442635}[]{#_Toc87787368}[]{#_Toc87852247}[]{#_Toc87853026}[]{#_Toc87853807}[]{#_Toc87867863}[]{#_Toc87442636}[]{#_Toc87787369}[]{#_Toc87852248}[]{#_Toc87853027}[]{#_Toc87853808}[]{#_Toc87867864}[]{#_Toc87442637}[]{#_Toc87787370}[]{#_Toc87852249}[]{#_Toc87853028}[]{#_Toc87853809}[]{#_Toc87867865}[]{#_Toc87442638}[]{#_Toc87787371}[]{#_Toc87852250}[]{#_Toc87853029}[]{#_Toc87853810}[]{#_Toc87867866}[]{#_Toc87442639}[]{#_Toc87787372}[]{#_Toc87852251}[]{#_Toc87853030}[]{#_Toc87853811}[]{#_Toc87867867}[]{#_Toc87442640}[]{#_Toc87787373}[]{#_Toc87852252}[]{#_Toc87853031}[]{#_Toc87853812}[]{#_Toc87867868}[]{#_Toc87442641}[]{#_Toc87787374}[]{#_Toc87852253}[]{#_Toc87853032}[]{#_Toc87853813}[]{#_Toc87867869}

**PIM \-- PIM配置命令 \-- display pim statistics**

------------------------------------------------------------------------

[**[display pim statistics]{lang="EN-US"}**]{#struct_0_17565_x2166_1845834943}[命令用来显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[协议报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1191743386}

[**[display pim]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_17565_x2166_x741101620}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1382450535}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x794462481}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1142916874}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1780971760}

[[network-operator]{lang="EN-US"}]{#struct_0_17565_x2166_1378913712}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_579512444}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17565_x2166_x1512826383}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1521020464}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1101366921}[显示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[协议报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display pim statistics]{lang="EN-US"}]{#struct_0_17565_x2166_1143375626}

[ Received PIM packets: 3295]{lang="EN-US"}

[ Sent PIM packets    : 5975]{lang="EN-US"}

[                Valid       Invalid        Succeeded   Failed]{lang="EN-US"}

[     Hello    : 3128        0              4333        0]{lang="EN-US"}

[     Reg      : 14          0              0           0]{lang="EN-US"}

[     Reg-stop : 0           0              0           0]{lang="EN-US"}

[     JP       : 151         0              561         0]{lang="EN-US"}

[     BSM      : 0           0              1081        0]{lang="EN-US"}

[     Assert   : 0           0              0           0]{lang="EN-US"}

[     Graft    : 0           0              0           0]{lang="EN-US"}

[     Graft-ACK: 0           0              0           0]{lang="EN-US"}

[     C-RP     : 0           0              0           0]{lang="EN-US"}

[     SRM      : 0           0              0           0]{lang="EN-US"}

[     DF       : 0           0              0           0]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display pim statistics]{lang="EN-US"}]{#struct_0_17565_x2166_506455594}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x159028301}[[字段]{style="font-family:黑体"}]{#struct_0_17565_x2166_702319160}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17565_x2166_x978022698}

[[Received PIM packets]{lang="EN-US"}]{#struct_0_17565_x2166_1619258056}

[[收到的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1143310090}[协议报文总数]{style="font-family:宋体"}

[[Sent PIM packets]{lang="EN-US"}]{#struct_0_17565_x2166_x274447374}

[[发出的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1283700341}[协议报文总数]{style="font-family:宋体"}

[[Valid]{lang="EN-US"}]{#struct_0_17565_x2166_x550356912}

[[收到的合法]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1316894372}[协议报文数量]{style="font-family:宋体"}

[[Invalid]{lang="EN-US"}]{#struct_0_17565_x2166_1939265166}

[[收到的非法]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1143244554}[协议报文数量]{style="font-family:宋体"}

[[Succeeded]{lang="EN-US"}]{#struct_0_17565_x2166_118387119}

[[发送成功的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1063589108}[协议报文数量]{style="font-family:宋体"}

[[Failed]{lang="EN-US"}]{#struct_0_17565_x2166_x1769951794}

[[发送失败的]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x136002040}[协议报文数量]{style="font-family:宋体"}

[[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_x2062431519}

[[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_1143179018}[报文统计]{style="font-family:宋体"}

[[Reg]{lang="EN-US"}]{#struct_0_17565_x2166_x1488102101}

[[注册报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1004779545}

[[Reg-stop]{lang="EN-US"}]{#struct_0_17565_x2166_x563796914}

[[注册停止报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_1143637770}

[[JP]{lang="EN-US"}]{#struct_0_17565_x2166_1309015174}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_x298292490}[剪枝报文统计]{style="font-family:宋体"}

[[BSM]{lang="EN-US"}]{#struct_0_17565_x2166_x1670366140}

[[自举报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_944777325}

[[Assert]{lang="EN-US"}]{#struct_0_17565_x2166_1143572234}

[[断言报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1824171524}

[[Graft]{lang="EN-US"}]{#struct_0_17565_x2166_17780091}

[[嫁接报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_144706519}

[[Graft-ACK]{lang="EN-US"}]{#struct_0_17565_x2166_x1742412292}

[[嫁接应答报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_1143113479}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_2055720735}

[[C-RP]{lang="EN-US"}]{#struct_0_17565_x2166_317659250}[报文统计]{style="font-family:宋体"}

[[SRM]{lang="EN-US"}]{#struct_0_17565_x2166_453645856}

[[状态刷新报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_1143047943}

[[DF]{lang="EN-US"}]{#struct_0_17565_x2166_x849084442}

[[指定转发者报文统计]{style="font-family:宋体"}]{#struct_0_17565_x2166_x848887834}

[ ]{lang="EN-US"}

::: {#1709708274 .myid}
[]{#_Toc404789762}[]{#struct_0_17565_x2166_x609354541}

**PIM \-- PIM配置命令 \-- hello-option dr-priority (PIM view)**

------------------------------------------------------------------------

[**[hello-option dr-priority]{lang="EN-US"}**]{#struct_0_17565_x2166_440714120}[命令用来全局配置竞选]{style="font-family:
宋体"}[DR]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[undo hello-option dr-priority]{lang="EN-US"}**]{#struct_0_17565_x2166_x1186495711}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1771728525}

[**[hello-option dr-priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_17565_x2166_x1032318892}

[**[undo hello-option dr-priority]{lang="EN-US"}**]{#struct_0_17565_x2166_x1712331922}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1625352854}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_17565_x2166_1142982407}[的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1298291065}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1823532118}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x453829516}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1304044361}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x366741924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1690003964}

[*[priority]{lang="EN-US"}*]{#struct_0_17565_x2166_x1264804812}[：指定竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。数值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1323431134}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1142916871}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1781299440}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x558648906}[在公网实例中全局配置竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1038063522}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] hello-option dr-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1872660920}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim]{lang="EN-US"}**[ **hello-option** **dr-priority**]{lang="EN-US"}]{#struct_0_17565_x2166_1473197251}
:::

::: {#1399069803 .myid}
[]{#_Toc404789763}[]{#struct_0_17565_x2166_1035762676}[]{#_Toc311539016}

**PIM \-- PIM配置命令 \-- hello-option holdtime (PIM view)**

------------------------------------------------------------------------

[**[hello-option holdtime]{lang="EN-US"}**]{#struct_0_17565_x2166_x202506761}[命令用来全局配置保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居可达状态的时间。]{style="font-family:宋体"}

[**[undo hello-option holdtime]{lang="EN-US"}**]{#struct_0_17565_x2166_1143375623}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_506652202}

[**[hello-option holdtime ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_17565_x2166_566242401}

[**[undo hello-option holdtime]{lang="EN-US"}**]{#struct_0_17565_x2166_773920184}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_820938427}

[[保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x110227391}[邻居可达状态的时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_943343245}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1130292368}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1826775056}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1143310087}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x274119695}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1894836354}

[*[time]{lang="EN-US"}*]{#struct_0_17565_x2166_x1124777762}[：指定保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居可达状态的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。如果指定为]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒，则表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居永远可达。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1615588536}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_408398170}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x482290239}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1940306875}[在公网实例中全局配置保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居可达状态的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1143244551}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] hello-option holdtime 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_118714799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim hello-option holdtime]{lang="EN-US"}**]{#struct_0_17565_x2166_x2133011171}
:::

::: {#-1775735321 .myid}
[]{#_Toc404789764}[]{#struct_0_17565_x2166_512708856}[]{#_Toc311539017}

**PIM \-- PIM配置命令 \-- hello-option lan-delay (PIM view)**

------------------------------------------------------------------------

[**[hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_2077214642}[命令用来全局配置]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文在共享网段中的传输延迟。]{style="font-family:宋体"}

[**[undo hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_x1619395924}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x279255142}

[**[hello-option lan-delay ]{lang="EN-US"}***[delay]{lang="EN-US"}*]{#struct_0_17565_x2166_x798531670}

[**[undo hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_1143179015}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1488954069}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x256514875}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1292771329}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x871898189}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1480696269}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1206693827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_132755211}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x765453196}

[*[delay]{lang="EN-US"}*]{#struct_0_17565_x2166_1143637767}[：指定]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文在共享网段中的传输延迟，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1309080711}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1450761239}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1250498889}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1140733587}[在公网实例中全局配置]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_2024679855}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] hello-option lan-delay 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1248346393}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option override-interval]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x1392080816}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_1143572231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_x1823974916}
:::

::: {#-1273926563 .myid}
[]{#_Toc404789765}[]{#struct_0_17565_x2166_1832531542}[]{#_Toc311539018}

**PIM \-- PIM配置命令 \-- hello-option neighbor-tracking (PIM view)**

------------------------------------------------------------------------

[**[hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_86417369}[命令用来全局使能邻居跟踪功能，即禁止加入报文抑制能力。]{style="font-family:宋体"}

[**[undo hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_492206397}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_130514089}

[**[hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_x1102240828}

[**[undo hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_x1216339560}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1143113480}

[[邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。]{style="font-family:宋体"}]{#struct_0_17565_x2166_2056310548}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x196995095}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x815430556}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1001706144}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x937030461}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1590813101}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1258027475}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1229916967}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1143047944}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x609551149}[在公网实例中全局使能邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1608148449}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] hello-option neighbor-tracking]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_27379878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_x720066781}
:::

::: {#-1045459119 .myid}
[]{#_Toc404789766}[]{#struct_0_17565_x2166_x1456138443}[]{#_Toc311539019}

**PIM \-- PIM配置命令 \-- hello-option override-interval (PIM view)**

------------------------------------------------------------------------

[**[hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_x314653632}[命令用来全局配置剪枝否决时间。]{style="font-family:
宋体"}

[**[undo hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_1729328395}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1142982408}

[**[hello-option override-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_1298618745}

[**[undo hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_1110160271}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_162137353}

[[剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}]{#struct_0_17565_x2166_328372688}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1742514111}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_2019785943}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1713854042}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x810101108}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1142916872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1781102832}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x2053719045}[：指定剪枝否决时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1864104577}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_772613660}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x687853308}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_2019086546}[在公网实例中全局配置剪枝否决时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_986243550}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] hello-option override-interval 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1143375624}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option lan-delay]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_506586666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_251460864}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_1534238145}
:::

::: {#1471913294 .myid}
[]{#_Toc404789767}[]{#struct_0_17565_x2166_x1085949384}[]{#_Toc311539020}

**PIM \-- PIM配置命令 \-- holdtime join-prune (PIM view)**

------------------------------------------------------------------------

[**[holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_x845901621}[命令用来全局配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间。]{style="font-family:宋体"}

[**[undo holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_285771340}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1920580256}

[**[holdtime join-prune ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_17565_x2166_x907005126}

[**[undo holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_1143310088}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x274971663}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_x2048356797}[剪枝状态的保持时间为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1654475660}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x65020541}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1761695008}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_496814893}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x494036591}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1143244552}

[*[time]{lang="EN-US"}*]{#struct_0_17565_x2166_118518191}[：指定加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1958996975}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_17565_x2166_x2014877621}[PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x848494617}[接口向上游邻居发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1033261541}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1507041478}[在公网实例中全局配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间为]{style="font-family:宋体"}[280]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1775986549}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] holdtime join-prune 280]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_628045878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_x1603160935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer join-prune]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x848560153}
:::

::: {#294352900 .myid}
[]{#_Toc404789768}[]{#struct_0_17565_x2166_1143179016}[]{#_Toc311539021}

**PIM \-- PIM配置命令 \-- jp-pkt-size (PIM view)**

------------------------------------------------------------------------

[**[jp-pkt-size]{lang="EN-US"}**]{#struct_0_17565_x2166_x1489019605}[命令用来配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的最大长度。]{style="font-family:宋体"}

[**[undo jp-pkt-size]{lang="EN-US"}**]{#struct_0_17565_x2166_x569101792}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_305501522}

[**[jp-pkt-size ]{lang="EN-US"}***[size]{lang="EN-US"}*]{#struct_0_17565_x2166_1135269254}

[**[undo jp-pkt-size]{lang="EN-US"}**]{#struct_0_17565_x2166_x408402531}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_981600301}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_x1831222053}[剪枝报文的最大长度为]{style="font-family:宋体"}[8100]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1143637768}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1308490887}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2010784622}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1919666931}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x716116458}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1449477302}

[*[size]{lang="EN-US"}*]{#struct_0_17565_x2166_x1327782798}[：指定加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的最大长度，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1851173674}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1198866038}[在公网实例中配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的最大长度为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1143572232}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] jp-pkt-size 1500]{lang="EN-US"}
:::

::: {#1344150665 .myid}
[]{#_Toc404789769}[]{#struct_0_17565_x2166_x1824040452}

**PIM \-- PIM配置命令 \-- pim**

------------------------------------------------------------------------

[**[pim]{lang="EN-US"}**]{#struct_0_17565_x2166_1704104705}[命令用来进入]{style="font-family:宋体"}[PIM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo pim]{lang="EN-US"}**]{#struct_0_17565_x2166_103544374}[命令用来清除]{style="font-family:宋体"}[PIM]{lang="EN-US"}[视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x973764306}

[**[pim]{lang="EN-US"}**[ \[ *vpn-instance* *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_17565_x2166_849663246}

[**[undo pim]{lang="EN-US"}**[ \[ *vpn-instance* *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_17565_x2166_x867792700}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1608840547}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_1143113477}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2056638239}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1728953769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_710512783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1367119847}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17565_x2166_x302876244}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_913169176}

[]{#_Toc288743026}[]{#_Toc94588285}[]{#_Toc80176812}[]{#struct_0_17565_x2166_x127091232}[]{#_Toc60064435}[]{#_Toc60649397}[]{#_Toc76003031}[]{#_Toc76444956}[\# ]{lang="EN-US"}[先使能公网实例中的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[组播路由，再进入公网实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1143047941}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\]]{lang="EN-US"}

[]{#_Toc311539023}[]{#_Toc293993397}[]{#_Toc319654934}[]{#_Toc318291818}[]{#_Toc293993395}[]{#struct_0_17565_x2166_x609223469}[]{#_Toc324427705}[]{#_Toc324427706}[\# ]{lang="EN-US"}[先使能]{style="font-family:
宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[mvpn]{lang="EN-US"}[中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，再进入该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_2017950750}

[\[Sysname\] multicast routing vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-mrib-mvpn\] quit]{lang="EN-US"}

[\[Sysname\] pim vpn-instance mvpn]{lang="EN-US"}

[\[Sysname-pim-mvpn\]]{lang="EN-US"}
:::

::: {#-5258849 .myid}
[]{#_Toc404789770}[]{#struct_0_17565_x2166_x1150486698}

**PIM \-- PIM配置命令 \-- pim bfd enable**

------------------------------------------------------------------------

[**[pim bfd enable]{lang="EN-US"}**]{#struct_0_17565_x2166_728085987}[命令用来使能]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[**[undo pim bfd enable]{lang="EN-US"}**]{#struct_0_17565_x2166_x1595265352}[命令用来关闭]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_34569678}

[**[pim bfd enable]{lang="EN-US"}**]{#struct_0_17565_x2166_1142982405}

[**[undo pim bfd enable]{lang="EN-US"}**]{#struct_0_17565_x2166_1298422137}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1456697076}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1229523829}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x349985735}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1611877407}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2041056452}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_893322109}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x907756972}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1142916869}

[[只有在接口上先使能了]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}]{#struct_0_17565_x2166_x1781823729}[或]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1271221631}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_753968620}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1365446968}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x796848408}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim dm]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim bfd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x416579120}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1143375621}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[，并使能]{style="font-family:宋体"}[PIM]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_506783274}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim dm]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim bfd enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2133251438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim dm]{lang="EN-US"}**]{#struct_0_17565_x2166_x1970454358}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim sm]{lang="EN-US"}**]{#struct_0_17565_x2166_2121243703}
:::

::: {#-734366402 .myid}
[]{#_Toc404789771}[]{#struct_0_17565_x2166_908428526}

**PIM \-- PIM配置命令 \-- pim bsr-boundary**

------------------------------------------------------------------------

[**[pim bsr-boundary]{lang="EN-US"}**]{#struct_0_17565_x2166_x1393894331}[命令用来配置]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界，即]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[域的边界。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **pim bsr-boundary**]{lang="EN-US"}]{#struct_0_17565_x2166_1143310085}[命令用来删除]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x274250767}

[**[pim bsr-boundary]{lang="EN-US"}**]{#struct_0_17565_x2166_x1280638505}

[**[undo]{lang="EN-US"}**[ **pim bsr-boundary**]{lang="EN-US"}]{#struct_0_17565_x2166_4928024}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x909160172}

[[没有配置]{style="font-family:宋体"}[BSR]{lang="EN-US"}]{#struct_0_17565_x2166_x417206054}[的服务边界。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1072055508}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_1353038934}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1665386986}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1143244549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_119239088}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1818777800}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x1680836257}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1105870467}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_469280145}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim bsr-boundary]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x344404575}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x149012761}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[为]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的服务边界。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1143179013}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim bsr-boundary]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1488822997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[c-bsr]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_73759831}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast boundary]{lang="EN-US"}**]{#struct_0_17565_x2166_1207671080}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#-1653090437 .myid}
[]{#_Toc404789772}[]{#struct_0_17565_x2166_x673277877}[]{#_Toc319654935}[]{#_Toc318291819}[]{#_Toc293993396}

**PIM \-- PIM配置命令 \-- pim dm**

------------------------------------------------------------------------

[**[pim dm]{lang="EN-US"}**]{#struct_0_17565_x2166_x223852322}[命令用来使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo pim dm]{lang="EN-US"}**]{#struct_0_17565_x2166_x1487738092}[命令用来关闭]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_240174109}

[**[pim dm]{lang="EN-US"}**]{#struct_0_17565_x2166_1143637765}

[**[undo pim dm]{lang="EN-US"}**]{#struct_0_17565_x2166_1309211783}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1288804543}

[[PIM-DM]{lang="EN-US"}]{#struct_0_17565_x2166_x1422833446}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_177968576}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1651142001}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1661497996}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1657125773}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1639635661}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1143572229}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17565_x2166_x1823450629}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_626304026}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x877513147}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1904118017}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_17565_x2166_1124112714}[]{#_Hlt17604248}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="DE"}

[\[Sysname-GigabitEthernet1/0/1\] pim dm]{lang="DE"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x919266056}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_93502252}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-DM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1143113478}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim dm]{lang="EN-US"}

[]{#struct_0_17565_x2166_2055786271}[]{#_Toc324427709}[]{#_Toc324427710}[【相关命令】]{style="font-family:
黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast routing]{lang="EN-US"}**]{#struct_0_17565_x2166_x1609999148}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#-443619610 .myid}
[]{#_Toc404789773}[]{#struct_0_17565_x2166_x1748279594}

**PIM \-- PIM配置命令 \-- pim hello-option dr-priority**

------------------------------------------------------------------------

[**[pim hello-option dr-priority]{lang="EN-US"}**]{#struct_0_17565_x2166_1999135106}[命令用来在接口上配置竞选]{style="font-family:
宋体"}[DR]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[undo pim hello-option dr-priority]{lang="EN-US"}**]{#struct_0_17565_x2166_x1246579105}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x592613762}

[**[pim hello-option dr-priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_17565_x2166_1143047942}

[**[undo pim hello-option dr-priority]{lang="EN-US"}**]{#struct_0_17565_x2166_x609420077}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1215623528}

[[竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_17565_x2166_768452368}[的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x229250875}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1561591633}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x725119154}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_594156098}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_385364783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1142982406}

[*[priority]{lang="EN-US"}*]{#struct_0_17565_x2166_1298225529}[：指定竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。数值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1450882750}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x86361386}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1772519591}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_1564596900}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1370943798}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1142916870}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim hello-option dr-priority 3]{lang="EN-US"}

[]{#struct_0_17565_x2166_x1781233904}[]{#_Toc87787387}[]{#_Toc87852266}[]{#_Toc87853045}[]{#_Toc87853826}[]{#_Toc87867882}[]{#_Toc87787388}[]{#_Toc87852267}[]{#_Toc87853046}[]{#_Toc87853827}[]{#_Toc87867883}[]{#_Toc87787389}[]{#_Toc87852268}[]{#_Toc87853047}[]{#_Toc87853828}[]{#_Toc87867884}[]{#_Toc87787390}[]{#_Toc87852269}[]{#_Toc87853048}[]{#_Toc87853829}[]{#_Toc87867885}[]{#_Toc87787391}[]{#_Toc87852270}[]{#_Toc87853049}[]{#_Toc87853830}[]{#_Toc87867886}[]{#_Toc87787392}[]{#_Toc87852271}[]{#_Toc87853050}[]{#_Toc87853831}[]{#_Toc87867887}[]{#_Toc87787393}[]{#_Toc87852272}[]{#_Toc87853051}[]{#_Toc87853832}[]{#_Toc87867888}[]{#_Toc87787394}[]{#_Toc87852273}[]{#_Toc87853052}[]{#_Toc87853833}[]{#_Toc87867889}[]{#_Toc87787396}[]{#_Toc87852275}[]{#_Toc87853054}[]{#_Toc87853835}[]{#_Toc87867891}[]{#_Toc87787398}[]{#_Toc87852277}[]{#_Toc87853056}[]{#_Toc87853837}[]{#_Toc87867893}[]{#_Toc87787399}[]{#_Toc87852278}[]{#_Toc87853057}[]{#_Toc87853838}[]{#_Toc87867894}[]{#_Toc87787400}[]{#_Toc87852279}[]{#_Toc87853058}[]{#_Toc87853839}[]{#_Toc87867895}[]{#_Toc87787401}[]{#_Toc87852280}[]{#_Toc87853059}[]{#_Toc87853840}[]{#_Toc87867896}[]{#_Toc87787403}[]{#_Toc87852282}[]{#_Toc87853061}[]{#_Toc87853842}[]{#_Toc87867898}[]{#_Toc87787404}[]{#_Toc87852283}[]{#_Toc87853062}[]{#_Toc87853843}[]{#_Toc87867899}[]{#_Toc87787405}[]{#_Toc87852284}[]{#_Toc87853063}[]{#_Toc87853844}[]{#_Toc87867900}[]{#_Toc87787406}[]{#_Toc87852285}[]{#_Toc87853064}[]{#_Toc87853845}[]{#_Toc87867901}[]{#_Toc87787407}[]{#_Toc87852286}[]{#_Toc87853065}[]{#_Toc87853846}[]{#_Toc87867902}[]{#_Toc87787408}[]{#_Toc87852287}[]{#_Toc87853066}[]{#_Toc87853847}[]{#_Toc87867903}[]{#_Toc87787409}[]{#_Toc87852288}[]{#_Toc87853067}[]{#_Toc87853848}[]{#_Toc87867904}[]{#_Toc87787410}[]{#_Toc87852289}[]{#_Toc87853068}[]{#_Toc87853849}[]{#_Toc87867905}[]{#_Toc87787412}[]{#_Toc87852291}[]{#_Toc87853070}[]{#_Toc87853851}[]{#_Toc87867907}[]{#_Toc87787413}[]{#_Toc87852292}[]{#_Toc87853071}[]{#_Toc87853852}[]{#_Toc87867908}[]{#_Toc87787414}[]{#_Toc87852293}[]{#_Toc87853072}[]{#_Toc87853853}[]{#_Toc87867909}[]{#_Toc87787415}[]{#_Toc87852294}[]{#_Toc87853073}[]{#_Toc87853854}[]{#_Toc87867910}[]{#_Toc87787418}[]{#_Toc87852297}[]{#_Toc87853076}[]{#_Toc87853857}[]{#_Toc87867913}[]{#_Toc87787419}[]{#_Toc87852298}[]{#_Toc87853077}[]{#_Toc87853858}[]{#_Toc87867914}[]{#_Toc87787420}[]{#_Toc87852299}[]{#_Toc87853078}[]{#_Toc87853859}[]{#_Toc87867915}[]{#_Toc87787421}[]{#_Toc87852300}[]{#_Toc87853079}[]{#_Toc87853860}[]{#_Toc87867916}[]{#_Toc87787422}[]{#_Toc87852301}[]{#_Toc87853080}[]{#_Toc87853861}[]{#_Toc87867917}[]{#_Toc87787423}[]{#_Toc87852302}[]{#_Toc87853081}[]{#_Toc87853862}[]{#_Toc87867918}[]{#_Toc87787424}[]{#_Toc87852303}[]{#_Toc87853082}[]{#_Toc87853863}[]{#_Toc87867919}[]{#_Toc87787425}[]{#_Toc87852304}[]{#_Toc87853083}[]{#_Toc87853864}[]{#_Toc87867920}[]{#_Toc87787428}[]{#_Toc87852307}[]{#_Toc87853086}[]{#_Toc87853867}[]{#_Toc87867923}[]{#_Toc87787429}[]{#_Toc87852308}[]{#_Toc87853087}[]{#_Toc87853868}[]{#_Toc87867924}[]{#_Toc87787430}[]{#_Toc87852309}[]{#_Toc87853088}[]{#_Toc87853869}[]{#_Toc87867925}[]{#_Toc87787432}[]{#_Toc87852311}[]{#_Toc87853090}[]{#_Toc87853871}[]{#_Toc87867927}[]{#_Toc87787433}[]{#_Toc87852312}[]{#_Toc87853091}[]{#_Toc87853872}[]{#_Toc87867928}[]{#_Toc87787434}[]{#_Toc87852313}[]{#_Toc87853092}[]{#_Toc87853873}[]{#_Toc87867929}[]{#_Toc87787435}[]{#_Toc87852314}[]{#_Toc87853093}[]{#_Toc87853874}[]{#_Toc87867930}[]{#_Toc87787436}[]{#_Toc87852315}[]{#_Toc87853094}[]{#_Toc87853875}[]{#_Toc87867931}[]{#_Toc87787437}[]{#_Toc87852316}[]{#_Toc87853095}[]{#_Toc87853876}[]{#_Toc87867932}[]{#_Toc87787438}[]{#_Toc87852317}[]{#_Toc87853096}[]{#_Toc87853877}[]{#_Toc87867933}[]{#_Toc87787439}[]{#_Toc87852318}[]{#_Toc87853097}[]{#_Toc87853878}[]{#_Toc87867934}[]{#_Toc87787440}[]{#_Toc87852319}[]{#_Toc87853098}[]{#_Toc87853879}[]{#_Toc87867935}[]{#_Toc87787443}[]{#_Toc87852322}[]{#_Toc87853101}[]{#_Toc87853882}[]{#_Toc87867938}[]{#_Toc87787444}[]{#_Toc87852323}[]{#_Toc87853102}[]{#_Toc87853883}[]{#_Toc87867939}[]{#_Toc87787445}[]{#_Toc87852324}[]{#_Toc87853103}[]{#_Toc87853884}[]{#_Toc87867940}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1338257173}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置竞选]{style="font-family:宋体"}[DR]{lang="EN-US"}[的优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x25839731}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim hello-option dr-priority 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1468252652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option dr-priority]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x253936313}
:::

::: {#-1774837261 .myid}
[]{#_Toc404789774}[]{#struct_0_17565_x2166_x809027763}[]{#_Toc311539024}[]{#_Toc293993398}

**PIM \-- PIM配置命令 \-- pim hello-option holdtime**

------------------------------------------------------------------------

[**[pim hello-option holdtime]{lang="EN-US"}**]{#struct_0_17565_x2166_x993112499}[命令用来在接口上配置保持]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[邻居的可达状态的时间。]{style="font-family:
宋体"}

[**[undo pim hello-option holdtime]{lang="EN-US"}**]{#struct_0_17565_x2166_x40420251}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1143375622}

[**[pim hello-option holdtime ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_17565_x2166_506717738}

[**[undo pim hello-option holdtime]{lang="EN-US"}**]{#struct_0_17565_x2166_x617712914}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x56759928}

[[保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1667363055}[邻居可达状态的时间为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x623398462}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_899327464}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1235139360}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1428100134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1143310086}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x274054159}

[*[time]{lang="EN-US"}*]{#struct_0_17565_x2166_663540738}[：指定保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居可达状态的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。如果指定为]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒，则表示]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居永远可达。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x188639016}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1276187886}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x214598681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_1870624606}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1581647665}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居可达状态的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1143244550}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim hello-option holdtime 120]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_118649263}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1731031623}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置保持]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居可达状态的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x854690275}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim hello-option holdtime 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_865989324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option holdtime]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x1576541740}
:::

::: {#1008221080 .myid}
[]{#_Toc404789775}[]{#struct_0_17565_x2166_x1793451636}[]{#_Toc311539025}[]{#_Toc293993399}

**PIM \-- PIM配置命令 \-- pim hello-option lan-delay**

------------------------------------------------------------------------

[**[pim hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_x17476092}[命令用来在接口上配置]{style="font-family:
宋体"}[PIM]{lang="EN-US"}[报文在共享网段中的传输延迟。]{style="font-family:宋体"}

[**[undo pim hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_1143179014}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1488888533}

[**[pim hello-option lan-delay ]{lang="EN-US"}***[delay]{lang="EN-US"}*]{#struct_0_17565_x2166_1953573649}

[**[undo pim hello-option lan-delay]{lang="ES"}**]{#struct_0_17565_x2166_x1978808679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1763213696}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1005801001}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1033906649}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_746924738}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_479029833}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1143637766}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1309146247}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1453781755}

[*[delay]{lang="EN-US"}*]{#struct_0_17565_x2166_1223258431}[：指定]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文在共享网段中的传输延迟，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1191565559}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_375567832}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x742932054}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_1641425015}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1143572230}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1823909380}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim hello-option lan-delay 200]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x850322211}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x860223245}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文在共享网段中的传输延迟为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1686733201}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim hello-option lan-delay 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1719369281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option lan-delay]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_296433020}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option override-interval]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x948222296}

[]{#_Toc311539026}[]{#_Toc293993400}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229539514}
:::

::: {#83381429 .myid}
[]{#_Toc404789776}[]{#struct_0_17565_x2166_518176456}

**PIM \-- PIM配置命令 \-- pim hello-option neighbor-tracking**

------------------------------------------------------------------------

[**[pim hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_1797798271}[命令用来在接口上使能邻居跟踪功能，即禁止加入报文抑制能力。]{style="font-family:宋体"}

[**[pim hello-option neighbor-tracking disable]{lang="EN-US"}**]{#struct_0_17565_x2166_x760564884}[命令用来在全局使能了邻居跟踪功能的情况下，关闭当前接口上的邻居跟踪功能。]{style="font-family:宋体"}

[**[undo pim hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_x1253706856}[命令用来抵消上述两条命令的配置，即让接口与全局配置保持一致。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_596237613}

[**[pim hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_689766032}

[**[pim hello-option neighbor-tracking]{lang="EN-US"}**[ **disable**]{lang="EN-US"}]{#struct_0_17565_x2166_x1630258688}

[**[undo pim hello-option neighbor-tracking]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229605050}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x463295058}

[[邻居跟踪功能处于关闭状态，即不禁止加入报文抑制能力。]{style="font-family:宋体"}]{#struct_0_17565_x2166_114583460}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1179881374}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x66287207}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x378074372}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_945476612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x704608488}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_473536131}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1229670586}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1363210034}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x826205361}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x699751713}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x373378645}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim hello-option neighbor-tracking]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_635067722}[在公网实例全局使能了邻居跟踪功能的情况下，关闭接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229736122}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] hello-option neighbor-tracking]{lang="EN-US"}

[\[Sysname-pim\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim hello-option neighbor-tracking disable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_659555114}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x927152701}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1282217461}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim hello-option neighbor-tracking]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x289255431}[在公网实例全局使能了邻居跟踪功能的情况下，关闭接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上的邻居跟踪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x259290292}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] hello-option neighbor-tracking]{lang="EN-US"}

[\[Sysname-pim\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim hello-option neighbor-tracking disable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1695551010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option neighbor-tracking]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x1229277370}
:::

::: {#-1871524019 .myid}
[]{#_Toc404789777}[]{#struct_0_17565_x2166_x2026779534}[]{#_Toc311539027}[]{#_Toc293993401}

**PIM \-- PIM配置命令 \-- pim hello-option override-interval**

------------------------------------------------------------------------

[**[pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_1320923125}[命令用来在接口上配置剪枝否决时间。]{style="font-family:宋体"}

[**[undo pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_750555272}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2072239960}

[**[pim hello-option override-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_1021063496}

[**[undo pim hello-option override-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_x1224830552}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_385614535}

[[剪枝否决时间为]{style="font-family:宋体"}[2500]{lang="EN-US"}]{#struct_0_17565_x2166_x846342802}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229342906}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_596670209}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_862530718}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x712124106}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_753378437}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_260647008}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x158328860}[：指定剪枝否决时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1019570426}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1326356807}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229408442}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x961559436}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1280569575}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置剪枝否决时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1513047693}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim hello-option override-interval 2000]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_139884984}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1483588042}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置剪枝否决时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_389586636}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim hello-option override-interval 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229473978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim hello-option lan-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_2075619668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option lan-delay]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x709554345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello-option override-interval]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_1358021554}
:::

::: {#1213956203 .myid}
[]{#_Toc404789778}[]{#struct_0_17565_x2166_83275897}[]{#_Toc311539028}[]{#_Toc293993403}

**PIM \-- PIM配置命令 \-- pim holdtime join-prune**

------------------------------------------------------------------------

[**[pim holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_x54641062}[命令用来在接口上配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间。]{style="font-family:宋体"}

[**[undo pim holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_339677519}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1402973720}

[**[pim holdtime join-prune ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_17565_x2166_x1333416410}

[**[undo pim holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229015226}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1442682889}

[[加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_450845286}[剪枝状态的保持时间为]{style="font-family:宋体"}[210]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_730605114}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_681279235}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1192428194}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x22690775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_586452255}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x391435160}

[*[time]{lang="EN-US"}*]{#struct_0_17565_x2166_x1229080762}[：指定加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1142031435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_17565_x2166_910276722}[PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_716999502}[接口向上游邻居发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x515858588}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_366835712}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x445547737}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间为]{style="font-family:宋体"}[280]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x2018457049}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim holdtime join-prune 280]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_402963841}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1229539513}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间为]{style="font-family:宋体"}[280]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x241338431}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim holdtime join-prune 280]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x874924600}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[holdtime join-prune]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x648817328}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_1801130606}
:::

::: {#1942658621 .myid}
[]{#_Toc404789779}[]{#struct_0_17565_x2166_353838027}

**PIM \-- PIM配置命令 \-- pim nbma-mode**

------------------------------------------------------------------------

[**[pim nbma-mode]{lang="EN-US"}**]{#struct_0_17565_x2166_979569716}[命令用来在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道]{style="font-family:宋体"}[tunnel]{lang="EN-US"}[口上使能]{style="font-family:宋体"}[PIM-NBMA]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_101575335}

[**[pim nbma-mode]{lang="EN-US"}**]{#struct_0_17565_x2166_515417848}

[**[undo pim nbma-mode]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17565_x2166_1630910670}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1101065224}

[[ADVPN]{lang="EN-US"}]{#struct_0_17565_x2166_2144897291}[隧道接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1949896881}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1734393067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_822945496}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_235046665}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17565_x2166_x497918609}[组播路由，接口上使能]{style="font-family:宋体"}[PIM SM]{lang="EN-US"}[协议，本命令才能生效。本命令不支持]{style="font-family:宋体"}[PIM DM]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1186102862}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_2096348738}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel 0]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-NBMA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1352554830}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface Tunnel 0 mode advpn gre]{lang="EN-US"}

[\[Sysname- Tunnel0\] pim sm]{lang="EN-US"}

[\[Sysname- Tunnel0\] pim nbma-mode]{lang="EN-US"}
:::

::: {#-1513388099 .myid}
[]{#_Toc311539029}[]{#_Toc311538638}[]{#_Toc293993405}[]{#_Toc404789780}[]{#struct_0_17565_x2166_1058392780}[]{#_Toc319654942}[]{#_Toc318291826}[]{#_Toc293993404}[]{#_Toc193253318}

**PIM \-- PIM配置命令 \-- pim neighbor-policy**

------------------------------------------------------------------------

[**[pim neighbor-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_1604795382}[命令用来配置合法]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，以防止]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文欺骗。]{style="font-family:宋体"}

[**[undo pim neighbor-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_x2034603369}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1940402479}

[**[pim neighbor-policy]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_17565_x2166_x1229605049}

[**[undo pim neighbor-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_1458953707}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1383676391}

[[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_x681422918}[报文的源地址范围不受任何限制，即认为所有收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文都是合法的。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1633573812}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1984591599}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1561585539}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_823433776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x298331850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229670585}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x1766494561}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1296327752}

[[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_x722753864}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定合法]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1151164237}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x1179037051}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1621663640}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置合法]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，只允许与来自网段]{style="font-family:宋体"}[10.1.1.0/24]{lang="EN-US"}[中的设备建立]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居关系。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229736121}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 10.1.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\][ pim neighbor-policy 2000]{.TerminalDisplayChar}]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_256270587}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1902087737}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置合法]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的源地址范围，只允许与来自网段]{style="font-family:宋体"}[10.1.1.0/24]{lang="EN-US"}[中的设备建立]{style="font-family:宋体"}[PIM]{lang="EN-US"}[邻居关系。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1578533308}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 10.1.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\][ pim neighbor-policy 2000]{.TerminalDisplayChar}]{lang="EN-US"}
:::

::: {#2119881727 .myid}
[]{#_Toc404789781}[]{#struct_0_17565_x2166_1206429950}

**PIM \-- PIM配置命令 \-- pim require-genid**

------------------------------------------------------------------------

[**[pim require-genid]{lang="EN-US"}**]{#struct_0_17565_x2166_x281068332}[命令用来配置拒绝无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo pim require-genid]{lang="EN-US"}**]{#struct_0_17565_x2166_333029167}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229277369}

[**[pim require-genid]{lang="EN-US"}**]{#struct_0_17565_x2166_1058268645}

[**[undo pim require-genid]{lang="EN-US"}**]{#struct_0_17565_x2166_791202351}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x998273587}

[[接受无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}]{#struct_0_17565_x2166_x1613510742}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1397285452}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x932530493}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_271114877}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1472029419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1229342905}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x969413732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x2043445482}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_100247384}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[拒绝无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x254890297}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim require-genid]{lang="EN-US"}

[]{#struct_0_17565_x2166_185201428}[]{#_Toc87442659}[]{#_Toc87787453}[]{#_Toc87852332}[]{#_Toc87853111}[]{#_Toc87853892}[]{#_Toc87867949}[]{#_Toc87442660}[]{#_Toc87787454}[]{#_Toc87852333}[]{#_Toc87853112}[]{#_Toc87853893}[]{#_Toc87867950}[]{#_Toc87442662}[]{#_Toc87787456}[]{#_Toc87852335}[]{#_Toc87853114}[]{#_Toc87853895}[]{#_Toc87867952}[]{#_Toc87442663}[]{#_Toc87787457}[]{#_Toc87852336}[]{#_Toc87853115}[]{#_Toc87853896}[]{#_Toc87867953}[]{#_Toc87442664}[]{#_Toc87787458}[]{#_Toc87852337}[]{#_Toc87853116}[]{#_Toc87853897}[]{#_Toc87867954}[]{#_Toc87442665}[]{#_Toc87787459}[]{#_Toc87852338}[]{#_Toc87853117}[]{#_Toc87853898}[]{#_Toc87867955}[]{#_Toc87442666}[]{#_Toc87787460}[]{#_Toc87852339}[]{#_Toc87853118}[]{#_Toc87853899}[]{#_Toc87867956}[]{#_Toc87442667}[]{#_Toc87787461}[]{#_Toc87852340}[]{#_Toc87853119}[]{#_Toc87853900}[]{#_Toc87867957}[]{#_Toc87442668}[]{#_Toc87787462}[]{#_Toc87852341}[]{#_Toc87853120}[]{#_Toc87853901}[]{#_Toc87867958}[]{#_Toc87442669}[]{#_Toc87787463}[]{#_Toc87852342}[]{#_Toc87853121}[]{#_Toc87853902}[]{#_Toc87867959}[]{#_Toc87442670}[]{#_Toc87787464}[]{#_Toc87852343}[]{#_Toc87853122}[]{#_Toc87853903}[]{#_Toc87867960}[]{#_Toc87442671}[]{#_Toc87787465}[]{#_Toc87852344}[]{#_Toc87853123}[]{#_Toc87853904}[]{#_Toc87867961}[]{#_Toc87442672}[]{#_Toc87787466}[]{#_Toc87852345}[]{#_Toc87853124}[]{#_Toc87853905}[]{#_Toc87867962}[]{#_Toc87442673}[]{#_Toc87787467}[]{#_Toc87852346}[]{#_Toc87853125}[]{#_Toc87853906}[]{#_Toc87867963}[]{#_Toc87442674}[]{#_Toc87787468}[]{#_Toc87852347}[]{#_Toc87853126}[]{#_Toc87853907}[]{#_Toc87867964}[]{#_Toc87442675}[]{#_Toc87787469}[]{#_Toc87852348}[]{#_Toc87853127}[]{#_Toc87853908}[]{#_Toc87867965}[]{#_Toc87442676}[]{#_Toc87787470}[]{#_Toc87852349}[]{#_Toc87853128}[]{#_Toc87853909}[]{#_Toc87867966}[]{#_Toc87442677}[]{#_Toc87787471}[]{#_Toc87852350}[]{#_Toc87853129}[]{#_Toc87853910}[]{#_Toc87867967}[]{#_Toc87442678}[]{#_Toc87787472}[]{#_Toc87852351}[]{#_Toc87853130}[]{#_Toc87853911}[]{#_Toc87867968}[]{#_Toc87442679}[]{#_Toc87787473}[]{#_Toc87852352}[]{#_Toc87853131}[]{#_Toc87853912}[]{#_Toc87867969}[]{#_Toc87442680}[]{#_Toc87787474}[]{#_Toc87852353}[]{#_Toc87853132}[]{#_Toc87853913}[]{#_Toc87867970}[]{#_Toc87442681}[]{#_Toc87787475}[]{#_Toc87852354}[]{#_Toc87853133}[]{#_Toc87853914}[]{#_Toc87867971}[]{#_Toc87442682}[]{#_Toc87787476}[]{#_Toc87852355}[]{#_Toc87853134}[]{#_Toc87853915}[]{#_Toc87867972}[]{#_Toc87442683}[]{#_Toc87787477}[]{#_Toc87852356}[]{#_Toc87853135}[]{#_Toc87853916}[]{#_Toc87867973}[]{#_Toc87442684}[]{#_Toc87787478}[]{#_Toc87852357}[]{#_Toc87853136}[]{#_Toc87853917}[]{#_Toc87867974}[]{#_Toc87442685}[]{#_Toc87787479}[]{#_Toc87852358}[]{#_Toc87853137}[]{#_Toc87853918}[]{#_Toc87867975}[]{#_Toc87442686}[]{#_Toc87787480}[]{#_Toc87852359}[]{#_Toc87853138}[]{#_Toc87853919}[]{#_Toc87867976}[]{#_Toc87442687}[]{#_Toc87787481}[]{#_Toc87852360}[]{#_Toc87853139}[]{#_Toc87853920}[]{#_Toc87867977}[]{#_Toc87442688}[]{#_Toc87787482}[]{#_Toc87852361}[]{#_Toc87853140}[]{#_Toc87853921}[]{#_Toc87867978}[]{#_Toc87442689}[]{#_Toc87787483}[]{#_Toc87852362}[]{#_Toc87853141}[]{#_Toc87853922}[]{#_Toc87867979}[]{#_Toc87442690}[]{#_Toc87787484}[]{#_Toc87852363}[]{#_Toc87853142}[]{#_Toc87853923}[]{#_Toc87867980}[]{#_Toc87442691}[]{#_Toc87787485}[]{#_Toc87852364}[]{#_Toc87853143}[]{#_Toc87853924}[]{#_Toc87867981}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x980856163}[配置接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[拒绝无]{style="font-family:宋体"}[Generation ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229408441}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim require-genid]{lang="EN-US"}
:::

::: {#-1653090416 .myid}
[]{#_Toc404789782}[]{#struct_0_17565_x2166_1767323919}

**PIM \-- PIM配置命令 \-- pim sm**

------------------------------------------------------------------------

[**[pim sm]{lang="EN-US"}**]{#struct_0_17565_x2166_x1659391554}[命令用来使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo pim sm]{lang="EN-US"}**]{#struct_0_17565_x2166_x1886954455}[命令用来关闭]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1872024143}

[**[pim sm]{lang="EN-US"}**]{#struct_0_17565_x2166_1039796087}

[**[undo pim sm]{lang="EN-US"}**]{#struct_0_17565_x2166_1479420796}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x913951606}

[[PIM-SM]{lang="EN-US"}]{#struct_0_17565_x2166_x255238553}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229473977}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_959874421}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1872709854}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_355539768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_220261368}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_762356488}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17565_x2166_245647202}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x447729696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_2125409005}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1229015225}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1286200466}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim sm]{lang="EN-US"}

[]{#_Toc94588286}[]{#_Toc78346670}[]{#_Toc80176813}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x1294732819}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1777550395}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1457112471}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim sm]{lang="EN-US"}

[]{#_Toc311539031}[]{#_Toc319654945}[]{#_Toc318291829}[]{#_Toc293993407}[]{#struct_0_17565_x2166_1196354265}[]{#_Toc324427720}[]{#_Toc324427721}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast routing]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229080761}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#-38836513 .myid}
[]{#_Toc404789783}[]{#struct_0_17565_x2166_x424052506}

**PIM \-- PIM配置命令 \-- pim state-refresh-capable**

------------------------------------------------------------------------

[**[pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_17565_x2166_x600053334}[命令用来使能状态刷新能力。]{style="font-family:
宋体"}

[**[undo pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_17565_x2166_x1739359259}[命令用来关闭状态刷新能力。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1586628367}

[**[pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_17565_x2166_x1621629664}

[**[undo pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_17565_x2166_305792950}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_592726949}

[[状态刷新能力处于使能状态。]{style="font-family:宋体"}]{#struct_0_17565_x2166_x930464616}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229539516}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x644622958}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1351407522}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1512172753}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1978706685}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1675252716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_780803711}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1007196108}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上关闭状态刷新能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229605052}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo pim state-refresh-capable]{lang="EN-US"}

[]{#struct_0_17565_x2166_x1626094472}[]{#_Toc87787489}[]{#_Toc87852368}[]{#_Toc87853147}[]{#_Toc87853928}[]{#_Toc87867985}[]{#_Toc87787490}[]{#_Toc87852369}[]{#_Toc87853148}[]{#_Toc87853929}[]{#_Toc87867986}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1072979180}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上关闭状态刷新能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_361779516}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] undo pim state-refresh-capable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x842573156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-interval]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x742024039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-rate-limit]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_485309952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-ttl]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_2112045129}
:::

::: {#-75170081 .myid}
[]{#_Toc404789784}[]{#struct_0_17565_x2166_x1229670588}[]{#_Toc319654946}[]{#_Toc318291830}[]{#_Toc293993408}

**PIM \-- PIM配置命令 \-- pim timer graft-retry**

------------------------------------------------------------------------

[**[pim timer graft-retry]{lang="EN-US"}**]{#struct_0_17565_x2166_x1813548728}[命令用来配置嫁接报文的重传时间。]{style="font-family:宋体"}

[**[undo pim timer graft-retry]{lang="EN-US"}**]{#struct_0_17565_x2166_1809075781}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_169503465}

[**[pim timer graft-retry ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x909890787}

[**[undo pim timer graft-retry]{lang="SV"}**]{#struct_0_17565_x2166_x775687698}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1778562608}

[[嫁接报文的重传时间为]{style="font-family:宋体"}]{#struct_0_17565_x2166_833279815}[3]{lang="SV"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229736124}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x147013940}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1017879499}

[[network-admin]{lang="SV"}]{#struct_0_17565_x2166_x805882783}

[[mdc-admin]{lang="SV"}]{#struct_0_17565_x2166_x1067775816}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x267055700}

[*[interval]{lang="SV"}*]{#struct_0_17565_x2166_1610311527}[：]{style="font-family:宋体"}[指定嫁接报文的重传时间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[65535]{lang="SV"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x826961750}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x1915259307}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1229277372}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置嫁接报文的重传时间为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1105388348}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim timer graft-retry 80]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x1052522271}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1377204015}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置嫁接报文的重传时间为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x822671436}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim timer graft-retry 80]{lang="NO-BOK"}
:::

::: {#739575722 .myid}
[]{#_Toc404789785}[]{#struct_0_17565_x2166_1894741554}

**PIM \-- PIM配置命令 \-- pim timer hello**

------------------------------------------------------------------------

[**[pim timer hello]{lang="EN-US"}**]{#struct_0_17565_x2166_416408502}[命令用来在接口上配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo pim timer hello]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229342908}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x209898845}

[**[pim timer hello]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_17565_x2166_x931162438}

[**[undo pim timer hello]{lang="EN-US"}**]{#struct_0_17565_x2166_1940179781}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x842900190}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_1991774652}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2030381757}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1078291625}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x145999044}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1229408444}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x2124358850}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x781457945}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x2129747266}[：指定发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_740012211}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_337453328}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1863474819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x1862000757}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_698894886}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229473980}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="EN-US"}[pim timer hello 40]{lang="NO-BOK"}

[]{#struct_0_17565_x2166_1720241276}[]{#_Toc87442697}[]{#_Toc87787494}[]{#_Toc87852373}[]{#_Toc87853152}[]{#_Toc87853933}[]{#_Toc87867990}[]{#_Toc87442698}[]{#_Toc87787495}[]{#_Toc87852374}[]{#_Toc87853153}[]{#_Toc87853934}[]{#_Toc87867991}[]{#_Toc87442700}[]{#_Toc87787497}[]{#_Toc87852376}[]{#_Toc87853155}[]{#_Toc87853936}[]{#_Toc87867993}[]{#_Toc87442701}[]{#_Toc87787498}[]{#_Toc87852377}[]{#_Toc87853156}[]{#_Toc87853937}[]{#_Toc87867994}[]{#_Toc87442702}[]{#_Toc87787499}[]{#_Toc87852378}[]{#_Toc87853157}[]{#_Toc87853938}[]{#_Toc87867995}[]{#_Toc87442703}[]{#_Toc87787500}[]{#_Toc87852379}[]{#_Toc87853158}[]{#_Toc87853939}[]{#_Toc87867996}[]{#_Toc87442704}[]{#_Toc87787501}[]{#_Toc87852380}[]{#_Toc87853159}[]{#_Toc87853940}[]{#_Toc87867997}[]{#_Toc87442705}[]{#_Toc87787502}[]{#_Toc87852381}[]{#_Toc87853160}[]{#_Toc87853941}[]{#_Toc87867998}[]{#_Toc87442706}[]{#_Toc87787503}[]{#_Toc87852382}[]{#_Toc87853161}[]{#_Toc87853942}[]{#_Toc87867999}[]{#_Toc87442707}[]{#_Toc87787504}[]{#_Toc87852383}[]{#_Toc87853162}[]{#_Toc87853943}[]{#_Toc87868000}[]{#_Toc87442708}[]{#_Toc87787505}[]{#_Toc87852384}[]{#_Toc87853163}[]{#_Toc87853944}[]{#_Toc87868001}[]{#_Toc87442709}[]{#_Toc87787506}[]{#_Toc87852385}[]{#_Toc87853164}[]{#_Toc87853945}[]{#_Toc87868002}[]{#_Toc87442710}[]{#_Toc87787507}[]{#_Toc87852386}[]{#_Toc87853165}[]{#_Toc87853946}[]{#_Toc87868003}[]{#_Toc87442712}[]{#_Toc87787509}[]{#_Toc87852388}[]{#_Toc87853167}[]{#_Toc87853948}[]{#_Toc87868005}[]{#_Toc87442713}[]{#_Toc87787510}[]{#_Toc87852389}[]{#_Toc87853168}[]{#_Toc87853949}[]{#_Toc87868006}[]{#_Toc87442715}[]{#_Toc87787512}[]{#_Toc87852391}[]{#_Toc87853170}[]{#_Toc87853951}[]{#_Toc87868008}[]{#_Toc87442716}[]{#_Toc87787513}[]{#_Toc87852392}[]{#_Toc87853171}[]{#_Toc87853952}[]{#_Toc87868009}[]{#_Toc87442717}[]{#_Toc87787514}[]{#_Toc87852393}[]{#_Toc87853172}[]{#_Toc87853953}[]{#_Toc87868010}[]{#_Toc87442719}[]{#_Toc87787516}[]{#_Toc87852395}[]{#_Toc87853174}[]{#_Toc87853955}[]{#_Toc87868012}[]{#_Toc87442720}[]{#_Toc87787517}[]{#_Toc87852396}[]{#_Toc87853175}[]{#_Toc87853956}[]{#_Toc87868013}[]{#_Toc87442721}[]{#_Toc87787518}[]{#_Toc87852397}[]{#_Toc87853176}[]{#_Toc87853957}[]{#_Toc87868014}[]{#_Toc87442722}[]{#_Toc87787519}[]{#_Toc87852398}[]{#_Toc87853177}[]{#_Toc87853958}[]{#_Toc87868015}[]{#_Toc87442723}[]{#_Toc87787520}[]{#_Toc87852399}[]{#_Toc87853178}[]{#_Toc87853959}[]{#_Toc87868016}[]{#_Toc87442724}[]{#_Toc87787521}[]{#_Toc87852400}[]{#_Toc87853179}[]{#_Toc87853960}[]{#_Toc87868017}[]{#_Toc87442725}[]{#_Toc87787522}[]{#_Toc87852401}[]{#_Toc87853180}[]{#_Toc87853961}[]{#_Toc87868018}[]{#_Toc87442726}[]{#_Toc87787523}[]{#_Toc87852402}[]{#_Toc87853181}[]{#_Toc87853962}[]{#_Toc87868019}[]{#_Toc87442727}[]{#_Toc87787524}[]{#_Toc87852403}[]{#_Toc87853182}[]{#_Toc87853963}[]{#_Toc87868020}[]{#_Toc87442728}[]{#_Toc87787525}[]{#_Toc87852404}[]{#_Toc87853183}[]{#_Toc87853964}[]{#_Toc87868021}[]{#_Toc87442731}[]{#_Toc87787528}[]{#_Toc87852407}[]{#_Toc87853186}[]{#_Toc87853967}[]{#_Toc87868024}[]{#_Toc87442732}[]{#_Toc87787529}[]{#_Toc87852408}[]{#_Toc87853187}[]{#_Toc87853968}[]{#_Toc87868025}[]{#_Toc87442734}[]{#_Toc87787531}[]{#_Toc87852410}[]{#_Toc87853189}[]{#_Toc87853970}[]{#_Toc87868027}[]{#_Toc87442735}[]{#_Toc87787532}[]{#_Toc87852411}[]{#_Toc87853190}[]{#_Toc87853971}[]{#_Toc87868028}[]{#_Toc87442736}[]{#_Toc87787533}[]{#_Toc87852412}[]{#_Toc87853191}[]{#_Toc87853972}[]{#_Toc87868029}[]{#_Toc87442737}[]{#_Toc87787534}[]{#_Toc87852413}[]{#_Toc87853192}[]{#_Toc87853973}[]{#_Toc87868030}[]{#_Toc87442738}[]{#_Toc87787535}[]{#_Toc87852414}[]{#_Toc87853193}[]{#_Toc87853974}[]{#_Toc87868031}[]{#_Toc87442739}[]{#_Toc87787536}[]{#_Toc87852415}[]{#_Toc87853194}[]{#_Toc87853975}[]{#_Toc87868032}[]{#_Toc87442740}[]{#_Toc87787537}[]{#_Toc87852416}[]{#_Toc87853195}[]{#_Toc87853976}[]{#_Toc87868033}[]{#_Toc87442741}[]{#_Toc87787538}[]{#_Toc87852417}[]{#_Toc87853196}[]{#_Toc87853977}[]{#_Toc87868034}[]{#_Toc87442742}[]{#_Toc87787539}[]{#_Toc87852418}[]{#_Toc87853197}[]{#_Toc87853978}[]{#_Toc87868035}[]{#_Toc87442743}[]{#_Toc87787540}[]{#_Toc87852419}[]{#_Toc87853198}[]{#_Toc87853979}[]{#_Toc87868036}[]{#_Toc87442744}[]{#_Toc87787541}[]{#_Toc87852420}[]{#_Toc87853199}[]{#_Toc87853980}[]{#_Toc87868037}[]{#_Toc87442745}[]{#_Toc87787542}[]{#_Toc87852421}[]{#_Toc87853200}[]{#_Toc87853981}[]{#_Toc87868038}[]{#_Toc87442746}[]{#_Toc87787543}[]{#_Toc87852422}[]{#_Toc87853201}[]{#_Toc87853982}[]{#_Toc87868039}[]{#_Toc87442747}[]{#_Toc87787544}[]{#_Toc87852423}[]{#_Toc87853202}[]{#_Toc87853983}[]{#_Toc87868040}[]{#_Toc87442748}[]{#_Toc87787545}[]{#_Toc87852424}[]{#_Toc87853203}[]{#_Toc87853984}[]{#_Toc87868041}[]{#_Toc87442749}[]{#_Toc87787546}[]{#_Toc87852425}[]{#_Toc87853204}[]{#_Toc87853985}[]{#_Toc87868042}[]{#_Toc87442750}[]{#_Toc87787547}[]{#_Toc87852426}[]{#_Toc87853205}[]{#_Toc87853986}[]{#_Toc87868043}[]{#_Toc87442752}[]{#_Toc87787549}[]{#_Toc87852428}[]{#_Toc87853207}[]{#_Toc87853988}[]{#_Toc87868045}[]{#_Toc87442753}[]{#_Toc87787550}[]{#_Toc87852429}[]{#_Toc87853208}[]{#_Toc87853989}[]{#_Toc87868046}[]{#_Toc87442754}[]{#_Toc87787551}[]{#_Toc87852430}[]{#_Toc87853209}[]{#_Toc87853990}[]{#_Toc87868047}[]{#_Toc87442755}[]{#_Toc87787552}[]{#_Toc87852431}[]{#_Toc87853210}[]{#_Toc87853991}[]{#_Toc87868048}[]{#_Toc87442756}[]{#_Toc87787553}[]{#_Toc87852432}[]{#_Toc87853211}[]{#_Toc87853992}[]{#_Toc87868049}[]{#_Toc87442757}[]{#_Toc87787554}[]{#_Toc87852433}[]{#_Toc87853212}[]{#_Toc87853993}[]{#_Toc87868050}[]{#_Toc87442758}[]{#_Toc87787555}[]{#_Toc87852434}[]{#_Toc87853213}[]{#_Toc87853994}[]{#_Toc87868051}[]{#_Toc87442759}[]{#_Toc87787556}[]{#_Toc87852435}[]{#_Toc87853214}[]{#_Toc87853995}[]{#_Toc87868052}[]{#_Toc87442760}[]{#_Toc87787557}[]{#_Toc87852436}[]{#_Toc87853215}[]{#_Toc87853996}[]{#_Toc87868053}[]{#_Toc87442761}[]{#_Toc87787558}[]{#_Toc87852437}[]{#_Toc87853216}[]{#_Toc87853997}[]{#_Toc87868054}[]{#_Toc87442762}[]{#_Toc87787559}[]{#_Toc87852438}[]{#_Toc87853217}[]{#_Toc87853998}[]{#_Toc87868055}[]{#_Toc87442763}[]{#_Toc87787560}[]{#_Toc87852439}[]{#_Toc87853218}[]{#_Toc87853999}[]{#_Toc87868056}[]{#_Toc87442764}[]{#_Toc87787561}[]{#_Toc87852440}[]{#_Toc87853219}[]{#_Toc87854000}[]{#_Toc87868057}[]{#_Toc87442765}[]{#_Toc87787562}[]{#_Toc87852441}[]{#_Toc87853220}[]{#_Toc87854001}[]{#_Toc87868058}[]{#_Toc87442766}[]{#_Toc87787563}[]{#_Toc87852442}[]{#_Toc87853221}[]{#_Toc87854002}[]{#_Toc87868059}[]{#_Toc87442767}[]{#_Toc87787564}[]{#_Toc87852443}[]{#_Toc87853222}[]{#_Toc87854003}[]{#_Toc87868060}[]{#_Toc87442768}[]{#_Toc87787565}[]{#_Toc87852444}[]{#_Toc87853223}[]{#_Toc87854004}[]{#_Toc87868061}[]{#_Toc87442769}[]{#_Toc87787566}[]{#_Toc87852445}[]{#_Toc87853224}[]{#_Toc87854005}[]{#_Toc87868062}[]{#_Toc87442770}[]{#_Toc87787567}[]{#_Toc87852446}[]{#_Toc87853225}[]{#_Toc87854006}[]{#_Toc87868063}[]{#_Toc87442771}[]{#_Toc87787568}[]{#_Toc87852447}[]{#_Toc87853226}[]{#_Toc87854007}[]{#_Toc87868064}[]{#_Toc87442772}[]{#_Toc87787569}[]{#_Toc87852448}[]{#_Toc87853227}[]{#_Toc87854008}[]{#_Toc87868065}[]{#_Toc87442773}[]{#_Toc87787570}[]{#_Toc87852449}[]{#_Toc87853228}[]{#_Toc87854009}[]{#_Toc87868066}[]{#_Toc87442774}[]{#_Toc87787571}[]{#_Toc87852450}[]{#_Toc87853229}[]{#_Toc87854010}[]{#_Toc87868067}[]{#_Toc87442775}[]{#_Toc87787572}[]{#_Toc87852451}[]{#_Toc87853230}[]{#_Toc87854011}[]{#_Toc87868068}[]{#_Toc87442776}[]{#_Toc87787573}[]{#_Toc87852452}[]{#_Toc87853231}[]{#_Toc87854012}[]{#_Toc87868069}[]{#_Toc87442777}[]{#_Toc87787574}[]{#_Toc87852453}[]{#_Toc87853232}[]{#_Toc87854013}[]{#_Toc87868070}[]{#_Toc87442778}[]{#_Toc87787575}[]{#_Toc87852454}[]{#_Toc87853233}[]{#_Toc87854014}[]{#_Toc87868071}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_872523967}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x218667234}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim timer hello 40]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_64178039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer hello]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_1528731322}
:::

::: {#1200337108 .myid}
[]{#_Toc404789786}[]{#struct_0_17565_x2166_466462743}[]{#_Toc311539032}[]{#_Toc293993410}

**PIM \-- PIM配置命令 \-- pim timer join-prune**

------------------------------------------------------------------------

[**[pim timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229015228}[命令用来在接口上配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔。]{style="font-family:宋体"}

[**[undo pim timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_1893021583}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_552854538}

[**[pim timer join-prune ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x1851472537}

[**[undo pim timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_1393440296}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x656779216}

[[发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_x1410522393}[剪枝报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1328853675}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_1953698576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229080764}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x20767979}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_493292318}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1809675106}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_551381679}[：指定发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_516217831}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_17565_x2166_1020698066}[PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。]{style="font-family:宋体"}]{#struct_0_17565_x2166_716999500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_717196108}[接口向上游邻居发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x491005840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_1878622990}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1229539515}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1047907485}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim timer join-prune 80]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_x1071687765}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x896928595}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1235451461}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim timer join-prune 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1073557656}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim holdtime join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_717130572}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer join-prune]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_2094889832}
:::

::: {#1034837471 .myid}
[]{#_Toc404789787}[]{#struct_0_17565_x2166_x1229605051}[]{#_Toc311539033}[]{#_Toc293993411}

**PIM \-- PIM配置命令 \-- pim triggered-hello-delay**

------------------------------------------------------------------------

[**[pim triggered-hello-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_1102788883}[命令用来配置触发]{style="font-family:
宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间。]{style="font-family:宋体"}

[**[undo pim triggered-hello-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_x1677932455}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1373423847}

[**[pim triggered-hello-delay ]{lang="EN-US"}***[delay]{lang="EN-US"}*]{#struct_0_17565_x2166_1089384119}

[**[undo pim triggered-hello-delay]{lang="EN-US"}**]{#struct_0_17565_x2166_x130659838}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_644879119}

[[触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_760125916}[报文的最大延迟时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_564470682}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1229670587}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1365673321}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1507897689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1025802054}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1550437384}

[*[delay]{lang="EN-US"}*]{#struct_0_17565_x2166_x269683625}[：指定触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x152469675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17565_x2166_1787830987}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_2138470001}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229736123}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pim triggered-hello-delay 3]{lang="EN-US"}

[]{#struct_0_17565_x2166_x906528827}[]{#_Toc87787580}[]{#_Toc87852459}[]{#_Toc87853238}[]{#_Toc87854019}[]{#_Toc87868076}[]{#_Toc87787581}[]{#_Toc87852460}[]{#_Toc87853239}[]{#_Toc87854020}[]{#_Toc87868077}[]{#_Toc87787582}[]{#_Toc87852461}[]{#_Toc87853240}[]{#_Toc87854021}[]{#_Toc87868078}[]{#_Toc87787583}[]{#_Toc87852462}[]{#_Toc87853241}[]{#_Toc87854022}[]{#_Toc87868079}[]{#_Toc87787584}[]{#_Toc87852463}[]{#_Toc87853242}[]{#_Toc87854023}[]{#_Toc87868080}[]{#_Toc87787585}[]{#_Toc87852464}[]{#_Toc87853243}[]{#_Toc87854024}[]{#_Toc87868081}[]{#_Toc87787586}[]{#_Toc87852465}[]{#_Toc87853244}[]{#_Toc87854025}[]{#_Toc87868082}[]{#_Toc87787587}[]{#_Toc87852466}[]{#_Toc87853245}[]{#_Toc87854026}[]{#_Toc87868083}[]{#_Toc87787588}[]{#_Toc87852467}[]{#_Toc87853246}[]{#_Toc87854027}[]{#_Toc87868084}[]{#_Toc87787589}[]{#_Toc87852468}[]{#_Toc87853247}[]{#_Toc87854028}[]{#_Toc87868085}[]{#_Toc87787590}[]{#_Toc87852469}[]{#_Toc87853248}[]{#_Toc87854029}[]{#_Toc87868086}[]{#_Toc87787592}[]{#_Toc87852471}[]{#_Toc87853250}[]{#_Toc87854031}[]{#_Toc87868088}[]{#_Toc87787593}[]{#_Toc87852472}[]{#_Toc87853251}[]{#_Toc87854032}[]{#_Toc87868089}[]{#_Toc87787594}[]{#_Toc87852473}[]{#_Toc87853252}[]{#_Toc87854033}[]{#_Toc87868090}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x625306087}[在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上配置触发]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的最大延迟时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1099425832}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] pim triggered-hello-delay 3]{lang="EN-US"}
:::

::: {#-22012 .myid}
[]{#_Toc311539034}[]{#_Toc404789788}[]{#struct_0_17565_x2166_x1496013356}[]{#_Toc321403848}[]{#_Toc293993414}

**PIM \-- PIM配置命令 \-- register-policy (PIM view)**

------------------------------------------------------------------------

[**[register-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_1008063535}[命令用来配置注册报文的过滤策略。]{style="font-family:宋体"}

[**[undo register-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_x312234160}[命令用来删除注册报文的过滤策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1032365153}

[**[register-policy ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x1229277371}

[**[undo register-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_702103821}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_689487665}

[[没有配置注册报文的过滤策略。]{style="font-family:宋体"}]{#struct_0_17565_x2166_1586242915}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1972342398}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_46734937}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1319999814}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1726297148}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1229342907}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2132213146}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x1944134630}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x109779157}

[[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_x2129458443}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定注册报文中的组播源地址范围，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[参数用来指定组播组地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。只有与该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[语句匹配的注册报文才会被]{style="font-family:宋体"}[RP]{lang="EN-US"}[接受。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1936415451}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1572326795}[在公网实例中配置]{style="font-family:宋体"}[RP]{lang="EN-US"}[上对注册报文的过滤策略，只接收来自]{style="font-family:宋体"}[10.10.0.0/16]{lang="EN-US"}[网段的组播源发向]{style="font-family:宋体"}[225.1.0.0/16]{lang="EN-US"}[网段的组播组的注册报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229408443}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule permit ip source 10.10.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] register-policy 3000]{lang="EN-US"}
:::

::: {#-330475930 .myid}
[]{#_Toc404789789}[]{#struct_0_17565_x2166_717589324}

**PIM \-- PIM配置命令 \-- register-suppression-timeout (PIM view)**

------------------------------------------------------------------------

[**[register-suppression-timeout]{lang="EN-US"}**]{#struct_0_17565_x2166_717523788}[命令用来配置注册抑制时间。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **register-suppression-timeout**]{lang="EN-US"}]{#struct_0_17565_x2166_250503758}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2011818316}

[**[register-suppression-timeout]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_17565_x2166_62525736}

[**[undo]{lang="EN-US"}**[ **register-suppression-timeout**]{lang="EN-US"}]{#struct_0_17565_x2166_x2011883852}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x329005290}

[[注册抑制时间为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_17565_x2166_x2011687244}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2011752780}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1657859250}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2012080460}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1340416571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x2012145996}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x915768970}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x2011949388}[：指定注册抑制时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_53811491}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x2012014924}[在公网实例中配置注册抑制时间为]{style="font-family:宋体"}[70]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_707263031}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] register-suppression-timeout 70]{lang="EN-US"}
:::

::: {#-849976577 .myid}
[]{#_Toc404789790}[]{#struct_0_17565_x2166_604524505}

**PIM \-- PIM配置命令 \-- register-whole-checksum (PIM view)**

------------------------------------------------------------------------

[**[register-whole-checksum]{lang="EN-US"}**]{#struct_0_17565_x2166_600950851}[命令用来配置根据注册报文的全部内容来计算校验和。]{style="font-family:宋体"}

[**[undo register-whole-checksum]{lang="EN-US"}**]{#struct_0_17565_x2166_x1110267273}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x477162477}

[**[register-whole-checksum]{lang="EN-US"}**]{#struct_0_17565_x2166_1616177965}

[**[undo register-whole-checksum]{lang="EN-US"}**]{#struct_0_17565_x2166_387611046}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1980312684}

[[仅根据注册报文头来计算校验和。]{style="font-family:宋体"}]{#struct_0_17565_x2166_x13070761}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229473979}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_509535727}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x856048530}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_650679934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1251155660}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x317399571}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_790692480}[在公网实例中配置根据注册报文的全部内容来计算校验和。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1347280313}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] register-whole-checksum]{lang="EN-US"}
:::

::: {#292571168 .myid}
[]{#_Toc404789791}[]{#struct_0_17565_x2166_x2011359564}

**PIM \-- PIM配置命令 \-- snmp-agent trap enable pim**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **pim**]{lang="EN-US"}]{#struct_0_17565_x2166_x2011818315}[命令用来开启]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **pim**]{lang="EN-US"}]{#struct_0_17565_x2166_x340758791}[命令用来关闭]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2011883851}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **pim** \[ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** \] \*]{lang="EN-US"}]{#struct_0_17565_x2166_74279237}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **pim** \[ **candidate-bsr-win-election** \| **elected-bsr-lost-election** \| **neighbor-loss** \] \*]{lang="EN-US"}]{#struct_0_17565_x2166_x2011687243}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1785156225}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x2011752779}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x263472011}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17565_x2166_x2012080459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x130759598}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x2012145995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x512484443}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2011949387}

[**[candidate-bsr-win-election]{lang="EN-US"}**]{#struct_0_17565_x2166_1169556738}[：表示]{style="font-family:
宋体"}[C-BSR]{lang="EN-US"}[成功当选]{style="font-family:宋体"}[BSR]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}

[**[elected-bsr-lost-election]{lang="EN-US"}**]{#struct_0_17565_x2166_x2012014923}[：表示原]{style="font-family:
宋体"}[BSR]{lang="EN-US"}[在新的选举中失败的告警信息。]{style="font-family:宋体"}

[**[neighbor-loss]{lang="EN-US"}**]{#struct_0_17565_x2166_x2011294027}[：表示邻居丢失的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1148110236}

[[如果未指定任何可选参数，表示开启或关闭]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x2011359563}[的全部告警功能。]{style="font-family:宋体"}

[[开启了]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_410810393}[的告警功能之后，]{style="font-family:宋体"}[PIM]{lang="EN-US"}[会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2011818318}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x387812958}[关闭]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的全部告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x2011883854}

[\[Sysname\] undo snmp-agent trap enable pim]{lang="EN-US"}
:::

::: {#-2030032961 .myid}
[]{#_Toc404789792}[]{#struct_0_17565_x2166_x1229015227}[]{#_Toc311539035}

**PIM \-- PIM配置命令 \-- source-lifetime (PIM view)**

------------------------------------------------------------------------

[**[source-lifetime]{lang="EN-US"}**]{#struct_0_17565_x2166_x123401052}[命令用来配置组播源的生存时间。]{style="font-family:宋体"}

[**[undo source-lifetime]{lang="EN-US"}**]{#struct_0_17565_x2166_x1551993354}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x118499750}

[**[source-lifetime ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_17565_x2166_745472733}

[**[undo source-lifetime]{lang="EN-US"}**]{#struct_0_17565_x2166_470473352}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x283075922}

[[组播源的生存时间为]{style="font-family:宋体"}[210]{lang="EN-US"}]{#struct_0_17565_x2166_x196900081}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x388618606}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1229080763}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1586851920}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_653116348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1555993641}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_284850416}

[*[time]{lang="EN-US"}*]{#struct_0_17565_x2166_802972942}[：指定组播源的生存时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31536000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即组播源永不老化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x624335145}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_2024121153}[在公网实例中配置组播源的生存时间为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229539518}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] source-lifetime 200]{lang="EN-US"}
:::

::: {#550596505 .myid}
[]{#_Toc404789793}[]{#struct_0_17565_x2166_2131314564}[]{#_Toc311539036}

**PIM \-- PIM配置命令 \-- source-policy (PIM view)**

------------------------------------------------------------------------

[**[source-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_x89639543}[命令用来配置组播数据过滤器。]{style="font-family:宋体"}

[**[undo source-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_700547992}[命令用来删除组播数据过滤器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x22732047}

[**[source-policy]{lang="EN-US"}***[ acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x146669314}

[**[undo source-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_990522114}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1457501779}

[[没有配置组播数据过滤器。]{style="font-family:宋体"}]{#struct_0_17565_x2166_x423383090}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229605054}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1506073410}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2100014927}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1921324585}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x464734327}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1162087467}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x819320130}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1096405567}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1773750792}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定组播数据报文的源地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以]{lang="EN-US" style="font-family:宋体"}[外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1229670590}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定组播数据报文的源地址范围，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[参数用来指定组播组地址范围，若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以]{lang="EN-US" style="font-family:宋体"}[外的其它可选参数都将被忽略。未通过该过滤规则的报文将被丢弃。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，新配置将覆盖旧配置。]{style="font-family:宋体"}]{#struct_0_17565_x2166_2125253744}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1328184086}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_2087676930}[在公网实例中配置接收组播源为]{style="font-family:宋体"}[10.10.1.2]{lang="EN-US"}[的组播数据，丢弃组播源为]{style="font-family:宋体"}[10.10.1.1]{lang="EN-US"}[的组播数据。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x360360856}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 10.10.1.2 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source 10.10.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] source-policy 2000]{lang="EN-US"}
:::

::: {#-2125713044 .myid}
[]{#_Toc404789794}[]{#struct_0_17565_x2166_1025122536}[]{#_Toc311539037}

**PIM \-- PIM配置命令 \-- spt-switch-threshold (PIM view)**

------------------------------------------------------------------------

[**[spt-switch-threshold]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229736126}[命令用来配置发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换的条件。]{style="font-family:宋体"}

[**[undo spt-switch-threshold]{lang="EN-US"}**]{#struct_0_17565_x2166_x1309813354}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x244383071}

[**[spt-switch-threshold]{lang="EN-US"}**[ { *traffic-rate* \| **immediacy** \| **infinity** } \[ **group-policy** *acl-number* \]]{lang="EN-US"}]{#struct_0_17565_x2166_831429721}

[**[undo spt-switch-threshold]{lang="EN-US"}**[ \[ *traffic-rate \|* **immediacy** \| **infinity** \] \[ **group-policy** *acl-number* \]]{lang="EN-US"}]{#struct_0_17565_x2166_x1029467252}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1454258762}

[[设备收到第一个组播数据包后便立即向]{style="font-family:宋体"}[SPT]{lang="EN-US"}]{#struct_0_17565_x2166_381244984}[切换。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1909206376}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1132268899}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229277374}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x57411066}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_328860153}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1022762034}

[*[traffic-rate]{lang="EN-US"}*]{#struct_0_17565_x2166_1274207099}[：指定发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换的组播数据转发速率阈值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4194304]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。交换机不支持本参数。]{style="font-family:宋体"}

[**[immediacy]{lang="EN-US"}**]{#struct_0_17565_x2166_1063287879}[：表示立即发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换。]{style="font-family:宋体"}

[**[infinity]{lang="EN-US"}**]{#struct_0_17565_x2166_35488844}[：表示永不发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换。]{style="font-family:宋体"}

[**[group-policy]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_17565_x2166_1078026595}[：表示组策略列表中的一项，与该组策略匹配的组播组将应用本配置。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则本配置将应用于所有组播组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2076242080}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_x1229342910}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来指定组播组地址范围，]{style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，可以配置多个]{style="font-family:宋体"}]{#struct_0_17565_x2166_x566194741}[SPT]{lang="EN-US"}[切换阈值。但是，如果配置时所指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则相同，则新配置将覆盖旧配置；如果针对同一组播组存在多条配置，则按照配置顺序匹配到的第一条配置将生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于某些设备无法将组播报文封装在注册报文中发给]{style="font-family:宋体"}]{#struct_0_17565_x2166_410317608}[RP]{lang="EN-US"}[，因此在可能成为]{style="font-family:宋体"}[RP]{lang="EN-US"}[的设备上不建议配置永不发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换，以免导致组播报文转发失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1449719748}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1151425772}[在公网实例中配置发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换的组播数据转发速率阈值为]{style="font-family:宋体"}[4kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_1587010947}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] spt-switch-threshold 4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x2009958539}[在接收者侧]{style="font-family:宋体"}[DR]{lang="EN-US"}[的公网实例中配置永不发起]{style="font-family:宋体"}[SPT]{lang="EN-US"}[切换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1229408446}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] spt-switch-threshold infinity]{lang="EN-US"}
:::

::: {#204819920 .myid}
[]{#_Toc311539038}[]{#_Toc319654954}[]{#_Toc318291838}[]{#_Toc404789795}[]{#struct_0_17565_x2166_1007809032}[]{#_Toc331681118}[]{#_Toc306713406}[]{#_Toc293993421}

**PIM \-- PIM配置命令 \-- ssm-policy (PIM view)**

------------------------------------------------------------------------

[**[ssm-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_x168084394}[命令用来配置]{style="font-family:宋体"}[SSM]{lang="EN-US"}[组播组的范围。]{style="font-family:宋体"}

[**[undo ssm-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_x230886717}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_345307616}

[**[ssm-policy ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x568565529}

[**[undo ssm-policy]{lang="EN-US"}**]{#struct_0_17565_x2166_1859741741}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1713221657}

[[SSM]{lang="EN-US"}]{#struct_0_17565_x2166_x1178365744}[组播组的范围为]{style="font-family:宋体"}[232.0.0.0/8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229473982}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_557441862}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x27361360}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x364152996}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_765135344}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_195931484}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_1869697732}[：指定基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_513573828}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_x1971410546}[规则中的]{lang="EN-US" style="font-family:
宋体"}**[source]{lang="EN-US"}**[参数用来]{lang="EN-US" style="font-family:宋体"}[指定]{lang="EN-US" style="font-family:宋体"}[SSM]{lang="EN-US"}[组播组范围，若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令可以定义允许或拒绝的组播组的地址范围：如果匹配通过，则组播运行模式为]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1229015230}[PIM-SSM]{lang="EN-US"}[，否则为]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2045649817}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1307379055}[配置]{style="font-family:宋体"}[SSM]{lang="EN-US"}[组播组的范围]{style="font-family:宋体"}[232.1.0.0/16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x522306179}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 232.1.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] ssm-policy 2000]{lang="EN-US"}
:::

::: {#1954576936 .myid}
[]{#_Toc404789796}[]{#struct_0_17565_x2166_121182169}

**PIM \-- PIM配置命令 \-- state-refresh-interval (PIM view)**

------------------------------------------------------------------------

[**[state-refresh-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_x1710256247}[命令用来配置发送状态刷新报文的时间间隔。]{style="font-family:宋体"}

[**[undo state-refresh-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_x1601969950}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229080766}

[**[state-refresh-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x1183567393}

[**[undo state-refresh-interval]{lang="EN-US"}**]{#struct_0_17565_x2166_x1328343913}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1022299052}

[[发送状态刷新报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}]{#struct_0_17565_x2166_1223762766}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x716956485}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1456882625}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_815165917}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_337800860}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1229539517}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_2084260397}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_192506552}[：指定发送状态刷新报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x394406383}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1974857885}[在公网实例中配置发送状态刷新报文的时间间隔为]{style="font-family:宋体"}[70]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1376698543}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] state-refresh-interval 70]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1503351762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_17565_x2166_786077865}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-rate-limit]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x1229605053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-ttl]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x60010531}
:::

::: {#1645606705 .myid}
[]{#_Toc404789797}[]{#struct_0_17565_x2166_1739012068}[]{#_Toc319654955}[]{#_Toc318291839}

**PIM \-- PIM配置命令 \-- state-refresh-rate-limit (PIM view)**

------------------------------------------------------------------------

[**[state-refresh-rate-limit]{lang="EN-US"}**]{#struct_0_17565_x2166_x1114374570}[命令用来配置接收新状态刷新报文的等待时间。]{style="font-family:
宋体"}

[**[undo state-refresh-rate-limit]{lang="EN-US"}**]{#struct_0_17565_x2166_x1250175508}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_861398168}

[**[state-refresh-rate-limit ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_17565_x2166_x984896719}

[**[undo state-refresh-rate-limit]{lang="EN-US"}**]{#struct_0_17565_x2166_x1857409373}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x219144863}

[[接收新状态刷新报文的等待时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_17565_x2166_x1229670589}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_915334627}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1448314777}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1129680500}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x1186732184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_263948458}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1078998697}

[*[time]{lang="EN-US"}*]{#struct_0_17565_x2166_x209678575}[：指定接收新状态刷新报文的等待时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1255893379}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x1229736125}[在公网实例中配置接收新状态刷新报文的等待时间为]{style="font-family:宋体"}[45]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x1713097881}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] state-refresh-rate-limit 45]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x585286327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_17565_x2166_2015636859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-interval]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_1704714785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-ttl]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_97580540}
:::

::: {#1328928066 .myid}
[]{#_Toc404789798}[]{#struct_0_17565_x2166_x1152433200}[]{#_Toc319654956}[]{#_Toc318291840}[]{#_Toc293993424}

**PIM \-- PIM配置命令 \-- state-refresh-ttl (PIM view)**

------------------------------------------------------------------------

[**[state-refresh-ttl]{lang="EN-US"}**]{#struct_0_17565_x2166_1860839924}[命令用来配置状态刷新报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo state-refresh-ttl]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229277373}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x460695593}

[**[state-refresh-ttl ]{lang="EN-US"}***[ttl-value]{lang="EN-US"}*]{#struct_0_17565_x2166_636446868}

[**[undo state-refresh-ttl]{lang="EN-US"}**]{#struct_0_17565_x2166_x1182101261}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1291393829}

[[状态刷新报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_17565_x2166_x1485767935}[值为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1730025000}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1479926370}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229342909}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1356185096}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x131736092}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x114558583}

[*[ttl-value]{lang="EN-US"}*]{#struct_0_17565_x2166_233928542}[：指定状态刷新报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_764461391}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1371649167}[在公网实例中配置状态刷新报文的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值为]{style="font-family:宋体"}[45]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_x777184436}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] state-refresh-ttl 45]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1855990680}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim state-refresh-capable]{lang="EN-US"}**]{#struct_0_17565_x2166_x1229408445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-interval]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x558274909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state-refresh-rate-limit]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x1646518406}
:::

::: {#406831110 .myid}
[]{#_Toc404789799}[]{#struct_0_17565_x2166_534253696}

**PIM \-- PIM配置命令 \-- static-rp (PIM view)**

------------------------------------------------------------------------

[**[static-rp]{lang="EN-US"}**]{#struct_0_17565_x2166_411400087}[命令用来配置静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo static-rp]{lang="EN-US"}**]{#struct_0_17565_x2166_x448204771}[命令用来删除静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1128186311}

[**[static-rp]{lang="EN-US"}***[ rp-address]{lang="EN-US"}*[ \[ *acl-number* \| **bidir** \| **preferred** \] \*]{lang="EN-US"}]{#struct_0_17565_x2166_1807834150}

[**[undo static-rp ]{lang="EN-US"}***[rp-address]{lang="EN-US"}*]{#struct_0_17565_x2166_1526330705}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229473981}

[[没有配置静态]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_17565_x2166_154157335}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1203908974}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_1909381765}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1951176870}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_540567891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_1275181187}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_298827845}

[*[rp-address]{lang="EN-US"}*]{#struct_0_17565_x2166_x1723349548}[：指定静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该地址必须是实际存在且合法的单播]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，不能配置为]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址；但对于服务于双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[的静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[来说，允许将其]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址指定为一个实际不存在的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17565_x2166_x1229015229}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果指定了本参数，该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[将只为能够通过该过滤规则的组播组服务；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[将为所有组播组服务。]{style="font-family:宋体"}

[**[bidir]{lang="EN-US"}**]{#struct_0_17565_x2166_326937642}[：指定该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[服务于双向]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。如果未指定本参数，该静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[将服务于]{style="font-family:宋体"}[PIM-SM]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[preferred]{lang="EN-US"}**]{#struct_0_17565_x2166_x926284151}[：表示当网络中同时存在动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[和静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[时，优先选择静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[，只有当静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[失效时，动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[才能生效。如果未指定本参数，则表示优先选择动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[，只有当未配置动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[或动态]{style="font-family:宋体"}[RP]{lang="EN-US"}[失效时，静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[才能生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_291647045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[作为静态]{style="font-family:宋体"}]{#struct_0_17565_x2166_x1686111963}[RP]{lang="EN-US"}[的接口不必使能]{style="font-family:宋体"}[PIM]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_17565_x2166_x1393535094}[规则中的]{style="font-family:宋体"}**[source]{lang="EN-US"}**[参数用来]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[所服务的组播组范围，]{style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="EN-US"}**[参数则此规则不生效，而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="EN-US"}**[以外的其它可选参数都将被忽略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当某个静态]{style="font-family:宋体"}]{#struct_0_17565_x2166_x527780182}[RP]{lang="EN-US"}[引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则发生变化时，需要为所有组播组重新选举]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，可以配置多个静态]{style="font-family:宋体"}]{#struct_0_17565_x2166_x2098069118}[RP]{lang="EN-US"}[。但是，如果配置时所指定的静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则相同，则新配置将覆盖旧配置；如果存在多个静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[服务于同一组播组的情况，则选择]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址最大的静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[为该组服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1229080765}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1545315962}[在公网实例中配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[11.110.0.6]{lang="EN-US"}[的接口为静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[，为组播组]{style="font-family:宋体"}[225.1.1.0/24]{lang="EN-US"}[提供服务，并优先选择静态]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_538240553}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 225.1.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] static-rp 11.110.0.6 2001 preferred]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x40587782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pim rp-info]{lang="EN-US"}**]{#struct_0_17565_x2166_x1440657479}
:::

::: {#-548795270 .myid}
[]{#_Toc404789800}[]{#struct_0_17565_x2166_316990297}[]{#_Toc311539039}

**PIM \-- PIM配置命令 \-- timer hello (PIM view)**

------------------------------------------------------------------------

[**[timer hello]{lang="EN-US"}**]{#struct_0_17565_x2166_933573472}[命令用来全局配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo timer hello]{lang="EN-US"}**]{#struct_0_17565_x2166_336544427}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x2006901189}

[**[timer hello]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_17565_x2166_1455673105}

[**[undo timer hello]{lang="EN-US"}**]{#struct_0_17565_x2166_x704788738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1848863143}

[[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17565_x2166_x1279799325}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1267096396}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_800395109}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1069370580}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_336478891}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x776755562}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1531092876}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x1506063634}[：指定发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1196671632}

[[本配置既可在]{style="font-family:宋体"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x1981357107}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1904227796}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_x2137314129}[在公网实例中全局配置发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_17565_x2166_336413355}

[\[Sysname\] pim]{lang="NO-BOK"}

[\[Sysname-pim\] timer hello 40]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1481025793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim timer hello]{lang="EN-US"}**]{#struct_0_17565_x2166_541572720}
:::

::: {#-2063787226 .myid}
[]{#_Toc404789801}[]{#struct_0_17565_x2166_601385315}[]{#_Toc311539040}

**PIM \-- PIM配置命令 \-- timer join-prune (PIM view)**

------------------------------------------------------------------------

[**[timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_x134706476}[命令用来全局配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔。]{style="font-family:宋体"}

[**[undo timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_403962239}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1860626957}

[**[timer join-prune ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x898232537}

[**[undo timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_1328036938}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17565_x2166_336347819}

[[发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17565_x2166_905946861}[剪枝报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x1957894388}

[[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x380710692}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17565_x2166_502744342}

[[network-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x420183757}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17565_x2166_x348954973}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17565_x2166_1483292482}

[*[interval]{lang="EN-US"}*]{#struct_0_17565_x2166_x1937207690}[：指定发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[18000]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无穷大，即永不发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17565_x2166_336806571}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本配置既可在]{style="font-family:宋体"}]{#struct_0_17565_x2166_1608815184}[PIM]{lang="EN-US"}[视图又可在接口视图下进行，前者对所有接口都生效，而后者只对当前接口生效，但后者的配置优先级较高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令不会立即生效，新配置的发送间隔将在当前发送间隔完成后生效。]{style="font-family:宋体"}]{#struct_0_17565_x2166_x2012146000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PIM]{lang="EN-US"}]{#struct_0_17565_x2166_x2011949392}[接口向上游邻居发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔必须小于加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝状态的保持时间，以免上游邻居老化超时。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x771331600}

[[\# ]{lang="EN-US"}]{#struct_0_17565_x2166_1230605730}[在公网实例中全局配置发送加入]{style="font-family:宋体"}[/]{lang="EN-US"}[剪枝报文的时间间隔为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17565_x2166_765578703}

[\[Sysname\] pim]{lang="EN-US"}

[\[Sysname-pim\] timer join-prune 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17565_x2166_x857548151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[holdtime join-prune]{lang="EN-US"}**[ (PIM view)]{lang="EN-US"}]{#struct_0_17565_x2166_x2012014928}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pim timer join-prune]{lang="EN-US"}**]{#struct_0_17565_x2166_287610695}
:::
