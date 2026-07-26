::: {#601126234 .myid}
[]{#_Toc404790492}[]{#struct_0_x1286_68518_x1233471674}[]{#_Toc285614370}

**静态LSP \-- 静态LSP配置命令 \-- display mpls static-lsp**

------------------------------------------------------------------------

[**[display mpls static-lsp]{lang="EN-US"}**]{#struct_0_x1286_68518_31783239}[命令用来显示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1088775774}

[**[display mpls static-lsp]{lang="EN-US"}**[ \[ **lsp-name** *lsp-name* \]]{lang="EN-US"}]{#struct_0_x1286_68518_x531189711}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x57273781}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1286_68518_x1086764633}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x733064964}

[[network-admin]{lang="EN-US"}]{#struct_0_x1286_68518_x1028190400}

[[network-operator]{lang="EN-US"}]{#struct_0_x1286_68518_1438846374}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1286_68518_x1900401950}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1286_68518_x1233537210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1286_68518_1518857115}

[**[lsp-name]{lang="EN-US"}***[ lsp-name]{lang="EN-US"}*]{#struct_0_x1286_68518_x1855227720}[：显示指定静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[lsp-name]{lang="EN-US"}*[表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1286_68518_931037636}

[[\# ]{lang="EN-US"}]{#struct_0_x1286_68518_x770831228}[显示所有静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls static-lsp]{lang="EN-US"}]{#struct_0_x1286_68518_447123049}

[Total: 4]{lang="EN-US"}

[Name            FEC                In/Out Label Nexthop/Out Interface    State]{lang="EN-US"}

[egress123       -/-                16/NULL      -                        Up]{lang="EN-US"}

[ingress123      202.118.224.132/32 NULL/1022    100.100.100.19           Down]{lang="EN-US"}

[transit123      -/-                32/1022      100.100.100.17           Down]{lang="EN-US"}

[transit124      -/-                34/1020      POS2/2/0                 Down]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display mpls static-lsp]{lang="EN-US"}]{#struct_0_x1286_68518_x359915457}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_687224986}[[字段]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1233340602}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1358715956}

[[Total]{lang="EN-US"}]{#struct_0_x1286_68518_x224983695}

[[静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_x473014377}[的总数]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x1286_68518_280876036}

[[静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_x997058736}[的名称]{style="font-family:宋体"}

[[FEC]{lang="EN-US"}]{#struct_0_x1286_68518_1339195498}

[[转发等价类，即]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1286_68518_762826222}[地址前缀和前缀长度]{style="font-family:宋体"}

[[In/Out Label]{lang="EN-US"}]{#struct_0_x1286_68518_x1233406138}

[[入标签值]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1286_68518_x678800959}[出标签值]{style="font-family:宋体"}

[[Nexthop/Out Interface]{lang="EN-US"}]{#struct_0_x1286_68518_458228479}

[[下一跳地址或出接口]{style="font-family:宋体"}]{#struct_0_x1286_68518_1747793187}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置静态]{style="font-family:宋体"}]{#struct_0_x1286_68518_x922300703}[LSP]{lang="EN-US"}[时指定了出接口，则显示为出接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置静态]{style="font-family:宋体"}]{#struct_0_x1286_68518_1681916151}[LSP]{lang="EN-US"}[时指定了下一跳地址，则显示为下一跳地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1286_68518_x1233864889}

[[静态的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_893766967}[状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1286_68518_x1171628378}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1286_68518_x1459572697}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x1286_68518_x63798783}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的入标签不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dup]{lang="EN-US"}]{#struct_0_x1286_68518_x63864319}[：表示静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[与静态]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}[或静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[使用了相同的入标签]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1759107089 .myid}
[]{#_Toc404790493}[]{#struct_0_x1286_68518_872010241}[]{#_Toc285614371}

**静态LSP \-- 静态LSP配置命令 \-- static-lsp egress**

------------------------------------------------------------------------

[**[static-lsp egress]{lang="EN-US"}**]{#struct_0_x1286_68518_x1070778690}[命令用来配置静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点。]{style="font-family:宋体"}

[**[undo static-lsp egress]{lang="EN-US"}**]{#struct_0_x1286_68518_240799993}[命令用来删除静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1233930425}

[**[static-lsp egress ]{lang="EN-US"}***[lsp-name]{lang="EN-US"}*[ **in-label** *in-label*]{lang="EN-US"}]{#struct_0_x1286_68518_x1891159388}

[**[undo static-lsp]{lang="EN-US"}**[ **egress** *lsp-name*]{lang="EN-US"}]{#struct_0_x1286_68518_114962262}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x678405540}

[[设备上不存在任何静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_2055430227}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1286_68518_1889605910}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1286_68518_344899126}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1960857906}

[[network-admin]{lang="EN-US"}]{#struct_0_x1286_68518_1344135307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1286_68518_1421665766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1233733817}

[*[lsp-name]{lang="EN-US"}*]{#struct_0_x1286_68518_1655458162}[：静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}**[ *in-label*]{lang="EN-US"}]{#struct_0_x1286_68518_x890713758}[：指定入标签值，]{style="font-family:宋体"}*[in-label]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x64323072}

[[如果为静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_1855459497}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[CRLSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[CRLSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1286_68518_1115015284}

[[\# ]{lang="EN-US"}]{#struct_0_x1286_68518_1841259246}[在]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点上配置一条名为]{style="font-family:宋体"}[bj-sh]{lang="EN-US"}[的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[233]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1286_68518_x660054641}

[\[Sysname\] static-lsp egress bj-sh in-label 233]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x635374905}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls static-lsp]{lang="EN-US"}**]{#struct_0_x1286_68518_x520351771}
:::

::: {#112615213 .myid}
[]{#_Toc404790494}[]{#struct_0_x1286_68518_x1695255126}[]{#_Toc285614372}

**静态LSP \-- 静态LSP配置命令 \-- static-lsp ingress**

------------------------------------------------------------------------

[**[static-lsp ingress]{lang="EN-US"}**]{#struct_0_x1286_68518_x1233799353}[命令用来配置静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点。]{style="font-family:宋体"}

[**[undo static-lsp ingress]{lang="EN-US"}**]{#struct_0_x1286_68518_186639855}[命令用来删除静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1618890988}

[**[static-lsp]{lang="EN-US"}***[ ]{lang="EN-US"}***[ingress]{lang="EN-US"}**[ *lsp-name* **destination** *dest-addr* { *mask* \| *mask-length* } { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label*]{lang="EN-US"}]{#struct_0_x1286_68518_1718509307}

[**[undo static-lsp]{lang="EN-US"}***[ ]{lang="EN-US"}***[ingress]{lang="EN-US"}**[ *lsp-name*]{lang="EN-US"}]{#struct_0_x1286_68518_1105540286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1286_68518_937632591}

[[设备上不存在任何静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_760918276}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1286_68518_1602494736}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1286_68518_x736561708}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1286_68518_1378512344}

[[network-admin]{lang="EN-US"}]{#struct_0_x1286_68518_x1233602745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1286_68518_x1254332952}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1083869338}

[*[lsp-name]{lang="EN-US"}*]{#struct_0_x1286_68518_1767789315}[：静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[destination ]{lang="FR"}**]{#struct_0_x1286_68518_x774298836}*[dest-addr]{lang="FR"}*[：指定]{style="font-family:
宋体"}[LSP]{lang="FR"}[的目的]{style="font-family:宋体"}[IP]{lang="FR"}[地址。]{style="font-family:宋体"}

[*[mask]{lang="FR"}*]{#struct_0_x1286_68518_x2065408765}[：]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="FR"}[地址掩码。]{style="font-family:宋体"}

[*[mask-length]{lang="FR"}*]{#struct_0_x1286_68518_326022465}[：]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="FR"}[地址掩码长度]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[。]{style="font-family:宋体"}

[**[nexthop]{lang="EN-US"}***[ next-hop-addr]{lang="EN-US"}*]{#struct_0_x1286_68518_x355394193}[：指定下一跳地址。]{style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1286_68518_769859525}[：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[out-label ]{lang="EN-US"}***[out-label]{lang="EN-US"}*]{#struct_0_x1286_68518_x812934033}[：指定出标签值，]{style="font-family:宋体"}*[out-label]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x445667987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置静态]{style="font-family:宋体"}]{#struct_0_x1286_68518_x1233668281}[LSP]{lang="EN-US"}[时，指定的下一跳或出接口必须与路由表中最优路由的下一跳或出接口保持一致。通过静态路由配置路由信息时，如果静态路由指定的是出接口，则静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[必须指定相同的出接口；如果静态路由指定的是下一跳，则静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[必须指定相同的下一跳。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态]{style="font-family:宋体"}]{#struct_0_x1286_68518_x2138822567}[LSP]{lang="EN-US"}[的出接口上必须使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x2079317220}

[[\# ]{lang="EN-US"}]{#struct_0_x1286_68518_x1683799476}[为]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点配置一条到目的地址]{style="font-family:宋体"}[202.25.38.1/24]{lang="EN-US"}[的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的名称为]{style="font-family:宋体"}[bj-sh]{lang="EN-US"}[，下一跳地址为]{style="font-family:宋体"}[202.55.25.33]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[237]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1286_68518_x2100047867}

[\[Sysname\] static-lsp ingress bj-sh destination 202.25.38.1 24 nexthop 202.55.25.33 out-label 237]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x530963457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls static-lsp]{lang="EN-US"}**]{#struct_0_x1286_68518_1958041485}
:::

::: {#563289275 .myid}
[]{#_Toc404790495}[]{#struct_0_x1286_68518_x1619349394}[]{#_Toc285614373}

**静态LSP \-- 静态LSP配置命令 \-- static-lsp transit**

------------------------------------------------------------------------

[**[static-lsp transit]{lang="EN-US"}**]{#struct_0_x1286_68518_148183193}[命令用来配置静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Transit]{lang="EN-US"}[节点。]{style="font-family:宋体"}

[**[undo static-lsp transit]{lang="EN-US"}**]{#struct_0_x1286_68518_x1233471673}[命令用来删除静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Transit]{lang="EN-US"}[节点配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x371501288}

[**[static-lsp]{lang="EN-US"}***[ ]{lang="EN-US"}***[transit]{lang="EN-US"}**[ *lsp-name* **in-label** *in-label* { **nexthop** *next-hop-addr* \| **outgoing-interface** *interface-type interface-number* } **out-label** *out-label*]{lang="EN-US"}]{#struct_0_x1286_68518_x2004054579}

[**[undo static-lsp transit ]{lang="EN-US"}***[lsp-name]{lang="EN-US"}*]{#struct_0_x1286_68518_443661568}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1286_68518_1380563407}

[[设备上不存在任何静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_x1832779212}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1286_68518_291791774}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1286_68518_1875733490}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1286_68518_927181114}

[[network-admin]{lang="EN-US"}]{#struct_0_x1286_68518_x1233537209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1286_68518_x403391650}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x982227551}

[*[lsp-name]{lang="EN-US"}*]{#struct_0_x1286_68518_x557669868}[：静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[in-label]{lang="EN-US"}***[ in-label]{lang="EN-US"}*]{#struct_0_x1286_68518_455090953}[：指定入标签值，]{style="font-family:宋体"}*[in-label]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nexthop]{lang="EN-US"}***[ next-hop-addr]{lang="EN-US"}*]{#struct_0_x1286_68518_x1103216892}[：指定下一跳地址。]{style="font-family:宋体"}

[**[outgoing-interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1286_68518_366128848}[：指定出接口的接口类型和接口编号。指定的接口必须为点到点连接类型的接口。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[out-label]{lang="EN-US"}***[ out-label]{lang="EN-US"}*]{#struct_0_x1286_68518_2116986423}[：指定出标签值，]{style="font-family:宋体"}*[out-label]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x1032789873}

[[静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_x1533259172}[的出接口上必须使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[如果为静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1286_68518_x64126464}[指定的入标签与已经存在的静态]{style="font-family:宋体"}[CRLSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签相同，则会导致标签冲突，静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[不可用。即使修改静态]{style="font-family:宋体"}[CRLSP/]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的入标签，静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[仍不可用，需要手工删除该静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[并重新配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1286_68518_228502601}

[[\# ]{lang="EN-US"}]{#struct_0_x1286_68518_x1233340601}[为]{style="font-family:宋体"}[Transit]{lang="EN-US"}[节点配置一条名为]{style="font-family:宋体"}[bj-sh]{lang="EN-US"}[的静态]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，入标签为]{style="font-family:宋体"}[123]{lang="EN-US"}[，下一跳地址为]{style="font-family:宋体"}[202.34.114.7]{lang="EN-US"}[，出标签为]{style="font-family:宋体"}[253]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1286_68518_1370167399}

[\[Sysname\] static-lsp transit bj-sh in-label 123 nexthop 202.34.114.7 out-label 253]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1286_68518_x2016248856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls static-lsp]{lang="EN-US"}**]{#struct_0_x1286_68518_x507086229}

[ ]{lang="EN-US"}
:::
