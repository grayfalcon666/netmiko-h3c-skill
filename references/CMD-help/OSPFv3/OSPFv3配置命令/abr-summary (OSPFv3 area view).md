::: {#1560665814 .myid}
[]{#_Toc245205316}[]{#_Toc138238088}[]{#_Toc93984824}[]{#_Toc81478690}[]{#_Toc58333149}[]{#_Toc58294805}[]{#_Toc33866034}[]{#_Toc404789040}[]{#struct_0_14538_x1521_561503191}[]{#_Toc322361657}[]{#_Toc320815905}

**OSPFv3 \-- OSPFv3配置命令 \-- abr-summary (OSPFv3 area view)**

------------------------------------------------------------------------

[**[abr-summary]{lang="EN-US"}**]{#struct_0_14538_x1521_x648708218}[命令用来配置]{style="font-family:宋体"}[ABR]{lang="EN-US"}[路由聚合。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **abr-summary**]{lang="EN-US"}]{#struct_0_14538_x1521_x162482617}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x571078023}

[**[abr-summary]{lang="EN-US"}**[ *ipv6-address prefix-length* \[ **not-advertise** \] \[ **cost** value \]]{lang="EN-US"}]{#struct_0_14538_x1521_x149529404}

[**[undo ]{lang="EN-US"}[abr-summary]{lang="EN-US"}**[ *ipv6-address prefix-length*]{lang="EN-US"}]{#struct_0_14538_x1521_x1104926046}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x400445950}

[[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_746535020}[不对路由进行聚合。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_31668709}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x188791867}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_561568727}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_445671812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x889342647}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1157473449}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_14538_x1521_x626386330}[：]{style="font-family:宋体"}[聚合路由的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_14538_x1521_1081939933}[：聚合路由的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。它指定地址中有多少连续的位组成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网络前缀，即]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址中的网络地址部分。]{style="font-family:宋体"}

[**[not-advertise]{lang="EN-US"}**]{#struct_0_14538_x1521_1291011597}[：不通告聚合的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由。如果未指定本参数，则通告聚合的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_14538_x1521_x1880038391}[：聚合路由的开销，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为所有被聚合的路由中最大的开销值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_234644024}

[[本命令只适用于]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_561634263}[，用来对当前区域进行路由聚合。对于落入该聚合网段的路由，]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向其它区域只发送一条聚合后的路由。一个区域可配置多条聚合网段，这样]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[可对多个网段进行聚合。]{style="font-family:宋体"}

[[当配置了]{style="font-family:宋体"}**[undo abr-summary]{lang="EN-US"}**]{#struct_0_14538_x1521_1123355402}[命令后，原来被聚合的路由将重新被发布。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1167316530}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_363859860}[将]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域]{style="font-family:宋体"}[1]{lang="EN-US"}[中两条路由]{style="font-family:宋体"}[2000:1:1:1::/64]{lang="EN-US"}[、]{style="font-family:宋体"}[2000:1:1:2::/64]{lang="EN-US"}[的路由聚合成一条前缀]{style="font-family:宋体"}[2000:1:1::/48]{lang="EN-US"}[向其它区域发送。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_640332245}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] area 1]{lang="EN-US"}

[\[Sysname-ospfv3-1-area-0.0.0.1\] abr-summary 2000:1:1:: 48]{lang="EN-US"}
:::

::: {#1184612688 .myid}
[]{#_Toc404789041}[]{#struct_0_14538_x1521_1606573008}

**OSPFv3 \-- OSPFv3配置命令 \-- area**

------------------------------------------------------------------------

[**[area]{lang="EN-US"}**]{#struct_0_14538_x1521_1406185131}[命令用来创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域，并进入区域视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **area**]{lang="EN-US"}]{#struct_0_14538_x1521_x1248040239}[命令用来删除指定的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1872739872}

[**[area]{lang="EN-US"}**[ *area-id*]{lang="EN-US"}]{#struct_0_14538_x1521_357178170}

[**[undo area ]{lang="EN-US"}***[area-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1606507472}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_191201556}

[[没有创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1811324164}[区域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1232789295}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1406188304}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_406292642}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1591605540}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1606441936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x918054909}

[*[area-id]{lang="EN-US"}*]{#struct_0_14538_x1521_44147749}[：区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其处理成]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式）或]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x276904138}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_940889423}[进入]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域]{style="font-family:宋体"}[0]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1799482137}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] area 0]{lang="EN-US"}

[\[Sysname-ospfv3-1-area-0.0.0.0\]]{lang="EN-US"}
:::

::: {#1524698147 .myid}
[]{#_Toc404789042}[]{#struct_0_14538_x1521_x2145011295}[]{#_Toc375657047}[]{#_Toc364781563}

**OSPFv3 \-- OSPFv3配置命令 \-- asbr-summary (OSPFv3 view)**

------------------------------------------------------------------------

[**[asbr-summary]{lang="EN-US"}**]{#struct_0_14538_x1521_x1937211701}[命令用来配置]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由聚合。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **asbr-summary**]{lang="EN-US"}]{#struct_0_14538_x1521_1709671074}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x581593027}

[**[asbr-summary]{lang="EN-US"}**[ *ipv6-address prefix-length* \[ **cost** *cost* \| **not-advertise \|** **nssa-only** \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_x453128143}

[**[undo ]{lang="EN-US"}[asbr-summary]{lang="EN-US"}**[ *ipv6-address prefix-length*]{lang="EN-US"}]{#struct_0_14538_x1521_x1026517286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x794488340}

[[ASBR]{lang="EN-US"}]{#struct_0_14538_x1521_532709712}[不对路由进行聚合。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x388125117}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x2145076831}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x27172553}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1342333046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_360435546}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1093755403}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_14538_x1521_420460061}[：聚合路由的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_14538_x1521_226561966}[：聚合路由的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。它指定地址中有多少连续的位组成]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[网络前缀，即]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址中的网络地址部分。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_14538_x1521_x991881390}[：聚合路由的开销，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}*[cost]{lang="EN-US"}*[取所有被聚合的路由中最大的开销值作为聚合路由的开销；如果是]{style="font-family:宋体"}[Type-7]{lang="EN-US"}[ LSA]{lang="EN-US" style="color:black"}[转化成的]{style="font-family:宋体;
color:black"}[Type-5]{lang="EN-US"}[ LSA]{lang="EN-US" style="color:black"}[描述的路由]{style="font-family:宋体;color:black"}[匹配聚合、且是]{style="font-family:宋体"}[Type2]{lang="EN-US"}[外部路由，则]{style="font-family:宋体"}*[cost]{lang="EN-US"}*[取所有被聚合的路由中最大的开销值加]{style="font-family:宋体"}[1]{lang="EN-US"}[作为聚合路由的开销。]{style="font-family:宋体"}

[**[not-advertise]{lang="EN-US"}**]{#struct_0_14538_x1521_x2145142367}[：不通告聚合路由。如果未指定本参数，将通告聚合路由。]{style="font-family:宋体"}

[**[nssa-only]{lang="EN-US"}**]{#struct_0_14538_x1521_x441310005}**[：]{style="font-family:宋体"}**[设置]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位为不置位]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[即在对端路由器上不能转为]{style="font-family:
宋体"}[Type-5 LSA]{lang="EN-US"}[。缺省时，]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位被置位，即在对端路由器上可以转为]{style="font-family:
宋体"}[Type-5 LSA]{lang="EN-US"}[（如果本地路由器是]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，则会检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，当]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居存在时，产生的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位）]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}***[ tag]{lang="EN-US"}*]{#struct_0_14538_x1521_x613281555}[：聚合路由的标记，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1350262108}

[[如果本地路由器是]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_14538_x1521_1021000733}[，对引入的聚合地址范围内的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[描述的路由进行聚合；当配置了]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域时，对引入的聚合地址范围内的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[描述的路由进行聚合。]{style="font-family:宋体"}

[[如果本地路由器同时是]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_14538_x1521_1530016737}[和]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，并且是]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的转换路由器，则对由]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转化成的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[描述的路由进行聚合处理；如果不是]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的转换路由器，则[]{#_Hlt15702645}不进行聚合处理。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[asbr-summary]{lang="EN-US"}**]{#struct_0_14538_x1521_3222503}[命令后，对处于聚合地址范围内的外部路由，本地路由器只向邻居路由器发布一条聚合后的路由；配置]{style="font-family:宋体"}**[undo asbr-summary]{lang="EN-US"}**[命令后，原来被聚合的外部路由将重新被发布。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1956216393}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x547293350}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[对引入的路由进行聚合，聚合路由为]{style="font-family:宋体"}[2000::/16]{lang="EN-US"}[，开销值为]{style="font-family:宋体"}[100]{lang="EN-US"}[，标记为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x2145207903}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] asbr-summary 2000:: 16 cost 100 tag 2]{lang="EN-US"}
:::

::: {#-644987809 .myid}
[]{#_Toc245205321}[]{#_Toc138238092}[]{#_Toc93984834}[]{#_Toc81478700}[]{#_Toc58333172}[]{#_Toc58294823}[]{#_Toc33866047}[]{#_Toc45164773}[]{#_Toc404789043}[]{#struct_0_14538_x1521_300727317}[]{#_Toc309373508}[]{#_Toc300320675}[]{#_Toc138212539}[]{#_Toc93984764}[]{#_Toc61236304}[]{#_Toc61093051}[]{#_Toc58812028}[]{#_Toc56887157}[]{#_Toc45164828}[]{#_Toc135622057}[]{#_Toc135622058}[]{#_Toc135622059}[]{#_Toc135622060}[]{#_Toc135622061}[]{#_Toc135622062}[]{#_Toc135622063}[]{#_Toc135622064}[]{#_Toc135622065}[]{#_Toc135622066}[]{#_Toc135622067}[]{#_Toc135622068}[]{#_Toc135622069}[]{#_Toc135622070}[]{#_Toc135622071}[]{#_Toc135622073}[]{#_Toc135622074}[]{#_Hlt19606757}[]{#_Toc135622077}[]{#_Toc135622078}[]{#_Toc135622079}[]{#_Toc135622080}[]{#_Toc135622081}[]{#_Toc135622082}[]{#_Toc135622083}[]{#_Toc135622084}[]{#_Toc135622085}[]{#_Toc135622086}[]{#_Toc135622087}[]{#_Toc135622088}[]{#_Toc135622089}[]{#_Toc135622091}[]{#_Toc135622092}[]{#_Toc135622093}[]{#_Toc135622094}[]{#_Toc135622095}[]{#_Toc135622096}[]{#_Toc135622097}[]{#_Toc135622098}[]{#_Toc135622099}[]{#_Toc135622100}[]{#_Toc135622101}[]{#_Toc135622102}[]{#_Toc135622103}[]{#_Toc135622104}[]{#_Toc135622105}[]{#_Toc135622106}[]{#_Toc135622107}[]{#_Toc135622108}[]{#_Toc135622109}[]{#_Toc135622111}[]{#_Toc135622112}[]{#_Toc135622114}[]{#_Toc135622115}[]{#_Toc135622116}[]{#_Toc135622117}[]{#_Toc135622118}[]{#_Toc135622119}[]{#_Toc135622120}[]{#_Toc135622121}[]{#_Toc135622122}[]{#_Toc135622123}[]{#_Toc135622124}[]{#_Toc135622127}[]{#_Toc135622128}[]{#_Toc135622129}[]{#_Toc135622130}[]{#_Toc135622131}[]{#_Toc135622132}[]{#_Toc135622133}[]{#_Toc135622134}[]{#_Toc135622135}[]{#_Toc135622136}[]{#_Toc135622137}[]{#_Toc135622138}[]{#_Toc135622139}[]{#_Toc135622140}[]{#_Toc135622141}[]{#_Toc135622142}[]{#_Toc135622143}[]{#_Toc135622144}[]{#_Toc135622145}[]{#_Toc135622147}[]{#_Toc135622148}[]{#_Toc135622149}[]{#_Toc135622150}[]{#_Toc135622151}[]{#_Toc135622152}[]{#_Toc135622153}[]{#_Toc135622154}[]{#_Toc135622155}[]{#_Toc135622156}[]{#_Toc135622157}[]{#_Toc135622158}[]{#_Toc135622159}[]{#_Toc135622160}[]{#_Toc135622161}[]{#_Toc177295242}[]{#_Toc177295243}[]{#_Toc177295244}[]{#_Toc177295245}[]{#_Toc177295246}[]{#_Toc177295247}[]{#_Toc177295248}[]{#_Toc177295249}[]{#_Toc177295250}[]{#_Toc177295251}[]{#_Toc177295252}[]{#_Toc177295253}[]{#_Hlt20631934}

**OSPFv3 \-- OSPFv3配置命令 \-- bandwidth-reference (OSPFv3 view)**

------------------------------------------------------------------------

[**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_14538_x1521_255370888}[命令用来配置计算链路开销时所依据的带宽参考值。]{style="font-family:宋体"}

[**[undo bandwidth-reference]{lang="EN-US"}**]{#struct_0_14538_x1521_x425870016}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_208732635}

[**[bandwidth-reference]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_14538_x1521_561699800}

[**[undo bandwidth-reference]{lang="EN-US"}**]{#struct_0_14538_x1521_1471584241}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1200617780}

[[计算链路开销时所依据的带宽参考值为]{style="font-family:宋体"}[100Mbps]{lang="EN-US"}]{#struct_0_14538_x1521_x2029462755}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1385732126}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_134651939}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_846552239}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1159309763}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_336445016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1132612560}

[*[value]{lang="EN-US"}*]{#struct_0_14538_x1521_561765336}[：计算链路开销时所依据的带宽参考值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x392390889}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1676486092}[有两种方式来配置接口的开销值，第一种方法是在接口视图下直接配置开销值；第二种方法是配置接口的带宽参考值，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[根据带宽参考值自动计算接口的开销值，计算公式为：接口开销＝带宽参考值÷接口带宽，当计算出来的开销值大于]{style="font-family:宋体"}[65535]{lang="EN-US"}[，开销取最大值]{style="font-family:宋体"}[65535]{lang="EN-US"}[；当计算出来的开销值小于]{style="font-family:宋体"}[1]{lang="EN-US"}[时，开销取最小值]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[如果没有在接口视图下显式的配置此接口的开销值，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x543363027}[会根据该接口的带宽自动计算其开销值[.]{lang="EN-US"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1025416303}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1665813030}[配置计算链路开销时所依据的带宽参考值为]{style="font-family:宋体"}[1000Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x906383209}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] bandwidth-reference 1000]{lang="EN-US"}
:::

::: {#1160081792 .myid}
[]{#_Toc404789044}[]{#struct_0_14538_x1521_x2145404511}[]{#_Toc375657050}[]{#_Toc364781566}

**OSPFv3 \-- OSPFv3配置命令 \-- default tag**

------------------------------------------------------------------------

[**[default tag]{lang="EN-US"}**]{#struct_0_14538_x1521_x1849615441}[命令用来配置引入外部路由的全局标记。]{style="font-family:宋体"}

[**[undo default tag]{lang="EN-US"}**]{#struct_0_14538_x1521_1841722226}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x615032255}

[**[default tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_14538_x1521_x2144421471}

[**[undo default tag]{lang="EN-US"}**]{#struct_0_14538_x1521_x1165751337}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_752728107}

[[引入外部路由的全局标记为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_14538_x1521_x1322217799}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x23788483}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1104089260}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1829159581}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1209204735}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x2144487007}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2038390785}

[*[tag]{lang="EN-US"}*]{#struct_0_14538_x1521_2019733462}[：外部路由的全局标记，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1718904134}

[[如果在配置相关命令时没有指定]{style="font-family:宋体"}]{#struct_0_14538_x1521_103481703}[标记]{style="font-family:宋体"}[，则缺省使用本命令配置的全局]{style="font-family:宋体"}[标记。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1368342093}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_828128542}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[引入外部路由的标记为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_217024865}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] default tag 2]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1813281943}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-route-advertise]{lang="EN-US"}**[ (OSPFv3 view)]{lang="EN-US"}]{#struct_0_14538_x1521_x1122179279}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}**[import-route]{lang="EN-US"}**]{#struct_0_14538_x1521_2087342502}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}**[route-tag]{lang="EN-US"}**]{#struct_0_14538_x1521_x678788840}[（]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/MPLS L3VPN]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#580160747 .myid}
[]{#_Toc311016199}[]{#_Toc404789045}[]{#struct_0_14538_x1521_x1786151834}[]{#_Toc322361660}

**OSPFv3 \-- OSPFv3配置命令 \-- default-cost (OSPFv3 area view)**

------------------------------------------------------------------------

[**[default-cost]{lang="EN-US"}**]{#struct_0_14538_x1521_561830872}[命令用来配置发送到]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的缺省路由的开销。]{style="font-family:宋体"}

[**[undo default-cost]{lang="EN-US"}**]{#struct_0_14538_x1521_x1018521319}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2044903263}

[**[default-cost ]{lang="EN-US"}***[cost]{lang="EN-US"}*]{#struct_0_14538_x1521_609010027}

[**[undo default-cost]{lang="EN-US"}**]{#struct_0_14538_x1521_x1367721272}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_852447588}

[[发送到]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_x1905856725}[区域或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的缺省路由的开销为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1950817956}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1193758937}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_561896408}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x227818115}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1367300429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x644673237}

[*[cost]{lang="EN-US"}*]{#struct_0_14538_x1521_191864051}[：发送到]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的缺省路由的开销，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x280886046}

[[该命令只有在]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_x1283051872}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR/ASBR]{lang="EN-US"}[上配置才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2098027275}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_561437656}[将]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域]{style="font-family:宋体"}[1]{lang="EN-US"}[设置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域，使发送到该]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域的缺省路由开销为]{style="font-family:宋体"}[60]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_849010035}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] area 1]{lang="NO-BOK"}

[\[Sysname-ospfv3-1-area-0.0.0.1\] stub]{lang="NO-BOK"}

[\[Sysname-ospfv3-1-area-0.0.0.1\] default-cost 60]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_685470296}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[nssa ]{lang="EN-US"}**[(OSPFv3 area view)]{lang="EN-US"}]{#struct_0_14538_x1521_874519885}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[stub]{lang="EN-US"}**]{#struct_0_14538_x1521_x1589640614}**[ ]{lang="EN-US"}**[(OSPFv3 area view)]{lang="EN-US"}
:::

::: {#-138723334 .myid}
[]{#_Toc404789046}[]{#struct_0_14538_x1521_x221457759}[]{#_Toc322361661}

**OSPFv3 \-- OSPFv3配置命令 \-- default-route-advertise (OSPFv3 view)**

------------------------------------------------------------------------

[**[default-route-advertise]{lang="EN-US"}**]{#struct_0_14538_x1521_x1351512896}[命令用来将缺省路由引入到]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由区域。]{style="font-family:宋体"}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_14538_x1521_561503192}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x648708217}

[**[default-route-advertise ]{lang="EN-US"}**[\[ \[ **always** \| **permit-calculate-other** \] \| **cost** *cost* \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_x163203513}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_14538_x1521_1767210610}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1596435442}

[[没有引入缺省路由。]{style="font-family:宋体"}]{#struct_0_14538_x1521_122284665}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2035304869}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x2059782775}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2011297173}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1913613560}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_561568728}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_445671801}

[**[always]{lang="EN-US"}**]{#struct_0_14538_x1521_1066972490}[：如果当前路由器的路由表中没有缺省路由，使用此参数可产生一个描述缺省路由的]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[发布出去。如果没有指定该关键字，仅当本地路由器的路由表中存在缺省路由时，才可以产生一个描述缺省路由的]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[发布出去。]{style="font-family:宋体"}

[**[permit-calculate-other]{lang="EN-US"}**]{#struct_0_14538_x1521_1323383780}[：]{style="font-family:宋体"}[当路由器产生并发布了一个描述缺省路由的]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[时，指定此参数的路由器仍然会计算来自于其他路由器的缺省路由，未指定此参数的路由器不再计算来自其他路由器的缺省路由。当路由器没有产生一个描述缺省路由的]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[时，无论是否指定此参数，路由器都会计算来自其他路由器的缺省路由]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_14538_x1521_1789563340}[：该缺省路由的度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_14538_x1521_x1148255697}[：]{style="font-family:宋体"}[路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。只有当前路由器的路由表中存在缺省路由，并且有路由匹配]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[指定的路由策略，才可以产生一个描述缺省路由的]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[发布出去，指定的路由策略会影响]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[中的值。如果同时指定]{style="font-family:宋体"}**[always]{lang="EN-US"}**[参数，不论当前路由器的路由表中是否有缺省路由，只要有路由匹配指定的路由策略，就将产生一个描述缺省路由的]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[发布出去，指定的路由策略会影响]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[中的值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_14538_x1521_216762721}[：外部路由的标记，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，将根据]{style="font-family:宋体"}**[default tag]{lang="EN-US"}**[命令的配置进行取值。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ *type*]{lang="EN-US"}]{#struct_0_14538_x1521_x1580978840}[：该]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[的类型，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:
宋体"}[缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x7753071}

[[使用]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_14538_x1521_x769824056}[命令不能引入缺省路由，如果要引入缺省路由，必须使用本命令。当本地路由器的路由表中没有缺省路由时，要产生一个描述缺省路由的]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[应使用]{style="font-family:宋体"}**[always]{lang="EN-US"}**[关键字]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_561634264}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1123355401}[将产生的缺省路由引入到]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[自治系统中（本地路由器没有缺省路由）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1167119922}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] default-route-advertise always]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1542267758}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[import-route]{lang="EN-US"}**]{#struct_0_14538_x1521_x128320235}**[ ]{lang="EN-US"}**[(OSPFv3 area view)]{lang="EN-US"}
:::

::: {#738738689 .myid}
[]{#_Toc404789047}[]{#struct_0_14538_x1521_x14352134}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3**

------------------------------------------------------------------------

[**[display ospfv3]{lang="EN-US"}**]{#struct_0_14538_x1521_x259029554}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的进程信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1060119005}

[**[display ospfv3]{lang="EN-US"}**[ \[ *process-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_14538_x1521_978002800}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_562224088}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1782915877}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_862436694}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1064082281}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_124635043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_305546236}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x1621806113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1660720030}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_614747746}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的概要信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_x1266360628}[：显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_562289624}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1786955719}[显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 verbose]{lang="EN-US"}]{#struct_0_14538_x1521_216959329}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ RouterID: 1.1.1.1          Router type:  ABR  ASBR  NSSA]{lang="EN-US"}

[ Route tag: 0]{lang="EN-US"}

[ Route tag check: Disabled]{lang="EN-US"}

[ Multi-VPN-Instance: Disabled]{lang="EN-US"}

[ Type value of extended community attributes:]{lang="EN-US"}

[    Domain ID : 0x0005]{lang="EN-US"}

[    Route type: 0x0306]{lang="EN-US"}

[    Router ID : 0x0107]{lang="EN-US"}

[ Domain-id: 0.0.0.0]{lang="EN-US"}

[ DN-bit check: Enabled]{lang="EN-US"}

[ DN-bit set: Enabled]{lang="EN-US"}

[ Originating router-LSAs with maximum metric]{lang="EN-US"}

[    Condition: On startup while BGP is converging for 600 seconds, State: Inactive]{lang="EN-US"}

[    Advertise summary-LSAs with metric 16711680]{lang="EN-US"}

[    Advertise external-LSAs with metric 16711680]{lang="EN-US"}

[    Advertise intra-area-prefix-LSAs with maximum metric]{lang="EN-US"}

[ SPF-schedule-interval: 5 50 200]{lang="EN-US"}

[ LSA generation interval: 5]{lang="EN-US"}

[ LSA arrival interval: 1000]{lang="EN-US"}

[ Transmit pacing: Interval: 20 Count: 3]{lang="EN-US"}

[ Default ASE parameters: Tag: 1]{lang="EN-US"}

[ Route preference: 10]{lang="EN-US"}

[ ASE route preference: 150]{lang="EN-US"}

[ SPF calculation count: 0]{lang="EN-US"}

[ External LSA count: 0]{lang="EN-US"}

[ LSA originated count: 0]{lang="EN-US"}

[ LSA received count: 0]{lang="EN-US"}

[ Area count: 2  Stub area Count: 0  NSSA area Count: 1]{lang="EN-US"}

[ ExChange/Loading neighbors: 0]{lang="EN-US"}

[ Max equal cost paths: 32]{lang="EN-US"}

[ Up interfaces: 1]{lang="EN-US"}

[ Full neighbors: 1]{lang="EN-US"}

[ Normal areas with up interfaces: 1]{lang="EN-US"}

[ Calculation trigger type: Full]{lang="EN-US"}

[ Current calculation type: SPF calculation]{lang="EN-US"}

[ Current calculation phase: Calculation area topology]{lang="EN-US"}

[[ Redistribute timer: Off]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_217549153}

[[ Redistribute schedule type: RIB]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_990819442}

[[ Redistribute route count: 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1574104003}

[[ Process reset state: N/A]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1544234140}

[[ Current reset type: N/A]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_1481954152}

[[ Next reset type: N/A]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1793963844}

[[ Reset prepare message replied: -/-/-/-]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_x2074439835}

[[ Reset process message replied: -/-/-/-]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_217614689}

[[ Reset phase of module:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1842617394}

[[   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A]{lang="EN-US"}]{#struct_0_14538_x1521_561699801}

[ ]{lang="EN-US"}

[ Area: 0.0.0.0]{lang="EN-US"}

[ Area flag: Normal]{lang="EN-US"}

[ SPF scheduled count: 0]{lang="EN-US"}

[ ExChange/Loading neighbors: 0]{lang="EN-US"}

[ LSA count: 0]{lang="EN-US"}

[ IPsec profile name: Profile000]{lang="EN-US"}

[ Up interfaces: 0]{lang="EN-US"}

[ MTU: 1440]{lang="EN-US"}

[ Default cost: 1]{lang="EN-US"}

[ Created by Vlink]{lang="EN-US"}

[ Process reset state: N/A]{lang="EN-US"}

[ Current reset type: N/A]{lang="EN-US"}

[ Reset prepare message replied: -/-/-/-]{lang="EN-US"}

[ Reset process message replied: -/-/-/-]{lang="EN-US"}

[ Reset phase of module:]{lang="EN-US"}

[   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.2]{lang="EN-US"}

[ Area flag: Normal]{lang="EN-US"}

[ SPF scheduled count: 0]{lang="EN-US"}

[ ExChange/Loading neighbors: 0]{lang="EN-US"}

[ LSA count: 0]{lang="EN-US"}

[ Up interfaces: 1]{lang="EN-US"}

[ MTU: 1500]{lang="EN-US"}

[ Default cost: 1]{lang="EN-US"}

[ Process reset state: N/A]{lang="EN-US"}

[ Current reset type: N/A]{lang="EN-US"}

[ Reset prepare message replied: -/-/-/-]{lang="EN-US"}

[ Reset process message replied: -/-/-/-]{lang="EN-US"}

[ Reset phase of module:]{lang="EN-US"}

[   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.3]{lang="EN-US"}

[ Area flag: NSSA]{lang="EN-US"}

[ 7/5 translator state: Disabled]{lang="EN-US"}

[ 7/5 translate stability timer interval: 0]{lang="EN-US"}

[ SPF Scheduled Count: 0]{lang="EN-US"}

[ ExChange/Loading neighbors: 0]{lang="EN-US"}

[ LSA Count: 0]{lang="EN-US"}

[ Up interfaces: 0]{lang="EN-US"}

[ MTU: 1440]{lang="EN-US"}

[ Default cost: 1]{lang="EN-US"}

[ Process reset flag: N/A]{lang="EN-US"}

[ Current reset type: N/A]{lang="EN-US"}

[ Reset prepare message replied: -/-/-/-]{lang="EN-US"}

[ Reset process message replied: -/-/-/-]{lang="EN-US"}

[ Reset phase of module:]{lang="EN-US"}

[   M-N/A, P-N/A, S-N/A, C-N/A, R-N/A]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ospfv3 verbose]{lang="EN-US"}]{#struct_0_14538_x1521_x1018521320}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1508151015}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_122785570}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_1819792647}

[[OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}]{#struct_0_14538_x1521_561896409}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x227818116}[进程是]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[是]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}

[[RouterID]{lang="EN-US"}]{#struct_0_14538_x1521_x1367497037}

[[本路由器的]{style="font-family:宋体"}]{#struct_0_14538_x1521_x439212516}[Router ID]{lang="FR"}

[[Router type]{lang="EN-US"}]{#struct_0_14538_x1521_433965862}

[[路由器类型，取值为：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x2008635976}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_1911149741}[表示区域边界路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASBR]{lang="EN-US"}]{#struct_0_14538_x1521_561437657}[表示自治系统边界路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_849010034}[表示支持]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{lang="EN-US" style="font-family:宋体"}

[[为空表示非上面三种情况]{style="font-family:宋体"}]{#struct_0_14538_x1521_685470297}

[[Route tag]{lang="EN-US"}]{#struct_0_14538_x1521_216893792}

[[当前进程引入外部路由的缺省标记]{style="font-family:宋体"}]{#struct_0_14538_x1521_216959328}

[[Route tag check]{lang="EN-US"}]{#struct_0_14538_x1521_539665719}

[[当前进程是否使能]{style="font-family:宋体"}]{#struct_0_14538_x1521_217549152}[检查]{style="font-family:宋体"}[OSPFv3 LSA]{lang="EN-US"}[的标记]{style="font-family:宋体"}

[[Multi-VPN-Instance]{lang="EN-US"}]{#struct_0_14538_x1521_874519884}

[[当前进程对]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14538_x1521_x1589640615}[PE]{lang="EN-US" style="font-size:9.0pt"}[、多]{style="font-size:9.0pt;font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例的支持情况：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multi-VPN-Instance]{lang="EN-US"}]{#struct_0_14538_x1521_217024863}[：]{style="font-family:宋体"}[Disabled]{lang="EN-US"}[表示不支持多]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multi-VPN-instance]{lang="EN-US"}]{#struct_0_14538_x1521_217090399}[：]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[表示支持多]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PE Router, Multi-VPN-Instance]{lang="EN-US"}]{#struct_0_14538_x1521_x1058169905}[：]{style="font-family:
  宋体"}[Enabled]{lang="EN-US"}[表示为]{style="font-family:宋体"}[PE]{lang="EN-US"}

[[Type value of extended community attributes]{lang="EN-US"}]{#struct_0_14538_x1521_217155935}

[[OSPFv3]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_14538_x1521_217221471}[扩展团体属性的类型编码]{style="font-size:9.0pt;font-family:宋体"}

[[Domain-id]{lang="EN-US"}]{#struct_0_14538_x1521_216762719}

[[OSPFv3]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_14538_x1521_216828255}[域标识符]{style="font-size:9.0pt;font-family:宋体"}

[[DN-bit check]{lang="EN-US"}]{#struct_0_14538_x1521_x1779421124}

[[当前进程是否使能检查]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14538_x1521_216893791}[OSPFv3 LSA]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[DN]{lang="EN-US" style="font-size:9.0pt"}[位]{style="font-size:9.0pt;
  font-family:宋体"}

[[DN-bit set]{lang="EN-US"}]{#struct_0_14538_x1521_216959327}

[[当前进程是否使能设置]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14538_x1521_539665728}[OSPFv3 LSA]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}[DN]{lang="EN-US" style="font-size:9.0pt"}[位]{style="font-size:9.0pt;
  font-family:宋体"}

[[Originating router-LSAs with maximum metric/Originating router-LSAs with R-bit clear]{lang="EN-US"}]{#struct_0_14538_x1521_x1122638030}

[[Router LSA]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_14538_x1521_x1121720526}[中使用最大开销值发布]{style="font-size:9.0pt;font-family:宋体"}[/Router LSA]{lang="EN-US" style="font-size:9.0pt"}[中清除]{style="font-size:
  9.0pt;font-family:宋体"}[R-bit]{lang="EN-US" style="font-size:9.0pt"}

[[Condition]{lang="EN-US"}]{#struct_0_14538_x1521_x1122179281}

[[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_x1122244817}[路由器的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Always]{lang="EN-US"}]{#struct_0_14538_x1521_x1122310353}[代表始终生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On startup while BGP is converging for XXX seconds]{lang="EN-US"}]{#struct_0_14538_x1521_x1122375889}[代表]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}[收敛超时时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On startup for XXX seconds]{lang="EN-US"}]{#struct_0_14538_x1521_x1122441425}[代表重启后生效时间]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_14538_x1521_x1122572497}

[[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_x1122638033}[路由器是否生效：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_14538_x1521_x1121654993}[表示生效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_14538_x1521_x1121720529}[表示不生效]{lang="EN-US" style="font-family:宋体"}

[[Advertise summary-LSAs with metric]{lang="EN-US"}]{#struct_0_14538_x1521_x1122179280}

[[Summary LSA]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_14538_x1521_x1122244816}[发布使用的开销值]{style="font-size:9.0pt;font-family:宋体"}

[[Advertise external-LSAs with metric]{lang="EN-US"}]{#struct_0_14538_x1521_x1122375888}

[[外部]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14538_x1521_x1122441424}[LSA]{lang="EN-US" style="font-size:9.0pt"}[发布使用的开销值]{style="font-size:9.0pt;font-family:宋体"}

[[Advertise intra-area-prefix-LSAs with maximum metric]{lang="EN-US"}]{#struct_0_14538_x1521_x1122506960}

[[Intra-area-prefix-LSA]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_14538_x1521_x1122572496}[发布使用的开销值]{style="font-size:9.0pt;
  font-family:宋体"}

[[SPF-schedule-interval]{lang="EN-US"}]{#struct_0_14538_x1521_x1787541700}

[[进行]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_14538_x1521_561503193}[计算的时间间隔]{style="font-family:宋体"}

[[LSA generation interval]{lang="EN-US"}]{#struct_0_14538_x1521_x648708216}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x163137977}[生成时间间隔]{style="font-family:宋体"}

[[LSA arrival interval]{lang="EN-US"}]{#struct_0_14538_x1521_1796886777}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x446152479}[重复到达的最小时间间隔]{style="font-family:宋体"}

[[Transmit pacing]{lang="EN-US"}]{#struct_0_14538_x1521_561568729}

[[接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_445671802}[报文的速率，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interval]{lang="EN-US"}]{#struct_0_14538_x1521_1066972489}[表示接口发送]{lang="EN-US" style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Count]{lang="EN-US"}]{#struct_0_14538_x1521_1323973603}[表示接口一次发送]{lang="EN-US" style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的最大个数]{lang="EN-US" style="font-family:宋体"}

[[Default ASE parameters]{lang="EN-US"}]{#struct_0_14538_x1521_217614687}

[[引入外部路由的缺省参数值，其中]{style="font-family:宋体"}[Tag]{lang="EN-US"}]{#struct_0_14538_x1521_217024862}[代表路由标记]{style="font-family:宋体"}

[[Route preference]{lang="EN-US"}]{#struct_0_14538_x1521_x151416694}

[[内部路由优先级]{style="font-family:宋体"}]{#struct_0_14538_x1521_561634265}

[[ASE route preference]{lang="EN-US"}]{#struct_0_14538_x1521_1123355400}

[[外部路由优先级]{style="font-family:宋体"}]{#struct_0_14538_x1521_1167185458}

[[SPF calculation count]{lang="EN-US"}]{#struct_0_14538_x1521_x36791623}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1351819958}[进程的路由计算总数]{style="font-family:宋体"}

[[External LSA count]{lang="EN-US"}]{#struct_0_14538_x1521_562224089}

[[外部]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1782915878}[数目，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Count]{lang="EN-US"}]{#struct_0_14538_x1521_862895446}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[checksum Sum]{lang="EN-US"}]{#struct_0_14538_x1521_1357806633}[：校验和]{lang="EN-US" style="font-family:宋体"}

[[LSA originated count]{lang="EN-US"}]{#struct_0_14538_x1521_562289625}

[[产生的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1786955718}[数目]{style="font-family:宋体"}

[[LSA received count]{lang="EN-US"}]{#struct_0_14538_x1521_x1029935764}

[[接收的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_909634380}[数目]{style="font-family:宋体"}

[[Area count]{lang="EN-US"}]{#struct_0_14538_x1521_x1316742905}

[[区域总数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_2127783737}

[[Stub area Count]{lang="EN-US"}]{#struct_0_14538_x1521_938706194}

[[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_2127849273}[区域数目]{style="font-family:宋体"}

[[NSSA area Count]{lang="EN-US"}]{#struct_0_14538_x1521_x1051115567}

[[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_2127914809}[区域数目]{style="font-family:宋体"}

[[ExChange/Loading neighbors]{lang="EN-US"}]{#struct_0_14538_x1521_x253406294}

[[处于]{style="font-family:宋体"}[ExChange/Loading]{lang="EN-US"}]{#struct_0_14538_x1521_1527396078}[状态的邻居数]{style="font-family:宋体"}

[[Calculation trigger type]{lang="EN-US"}]{#struct_0_14538_x1521_2127980345}

[[触发路由计算的类型，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_2106795538}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full]{lang="EN-US"}]{#struct_0_14538_x1521_x407151022}[：触发全部路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Area topology change]{lang="EN-US"}]{#struct_0_14538_x1521_x802921096}[：区域拓扑改变触发路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Intra router change]{lang="EN-US"}]{#struct_0_14538_x1521_2127521593}[：增量的区域内路由器路由变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ASBR change]{lang="EN-US"}]{#struct_0_14538_x1521_179870740}[：增量的]{style="font-family:
  宋体"}[ASBR]{lang="EN-US"}[路由变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full IP prefix]{lang="EN-US"}]{#struct_0_14538_x1521_1742261478}[：触发全部]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full intra AS]{lang="EN-US"}]{#struct_0_14538_x1521_2127587129}[：触发全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Inc intra AS]{lang="EN-US"}]{#struct_0_14538_x1521_x239488283}[：触发增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full inter AS]{lang="EN-US"}]{#struct_0_14538_x1521_x1054767245}[：触发全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Inc inter AS]{lang="EN-US"}]{#struct_0_14538_x1521_x1554224595}[：触发增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Nexthop calculation]{lang="EN-US"}]{#struct_0_14538_x1521_2127652665}[：触发下一跳计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_550244569}[：未触发计算]{style="font-family:宋体"}

[[Current calculation type]{lang="EN-US"}]{#struct_0_14538_x1521_x390243735}

[[当前路由计算的类型，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_2127718201}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[SPF calculation]{lang="EN-US"}]{#struct_0_14538_x1521_517262360}[：进行区域]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Intra router calculation]{lang="EN-US"}]{#struct_0_14538_x1521_x1977706140}[：区域内路由器路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ASBR calculation]{lang="EN-US"}]{#struct_0_14538_x1521_2128308025}[：区域间]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inc intra router]{lang="EN-US"}]{#struct_0_14538_x1521_720423830}[：增量区域内路由器路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Inc ASBR calculation]{lang="EN-US"}]{#struct_0_14538_x1521_x2131710214}[：增量区域间]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full intra AS]{lang="EN-US"}]{#struct_0_14538_x1521_2128373561}[：进行全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Inc intra AS]{lang="EN-US"}]{#struct_0_14538_x1521_1523811467}[：进行增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full inter AS]{lang="EN-US"}]{#struct_0_14538_x1521_x1079203976}[：进行全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inc inter AS]{lang="EN-US"}]{#struct_0_14538_x1521_108287994}[：进行增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_2127783738}[：未触发计算]{style="font-family:宋体"}

[[Current calculation phase]{lang="EN-US"}]{#struct_0_14538_x1521_939033874}

[[当前路由计算调度运行到的阶段，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x508964356}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation area topology]{lang="EN-US"}]{#struct_0_14538_x1521_2127849274}[：计算区域拓扑]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation router]{lang="EN-US"}]{#struct_0_14538_x1521_x1051312175}[：计算路由器路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Calculation intra AS]{lang="EN-US"}]{#struct_0_14538_x1521_328399456}[：计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation ASBR]{lang="EN-US"}]{#struct_0_14538_x1521_2127914810}[：计算]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation inter AS]{lang="EN-US"}]{#struct_0_14538_x1521_x252816471}[：计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Calculation end]{lang="EN-US"}]{#struct_0_14538_x1521_358823784}[：计算收尾阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_2127980346}[：未触发计算]{style="font-family:宋体"}

[[Redistribute timer]{lang="EN-US"}]{#struct_0_14538_x1521_2106598930}

[[引入路由定时器，其中：]{style="font-family:宋体"}]{#struct_0_14538_x1521_2127521594}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_14538_x1521_179411988}[：]{style="font-family:宋体"} [关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_14538_x1521_x1409466606}[：开启]{style="font-family:宋体"}

[[Redistribute schedule type]{lang="EN-US"}]{#struct_0_14538_x1521_2127587130}

[[引入路由调度类型，其中：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x240078108}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RIB]{lang="EN-US"}]{#struct_0_14538_x1521_1435153730}[：]{style="font-family:宋体"} [触发遍历]{style="font-family:宋体"}[RIB]{lang="EN-US"}[表进行引入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Self]{lang="EN-US"}]{#struct_0_14538_x1521_2127652666}[：]{style="font-family:宋体"} [触发遍历自身引入表进行引入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_550441177}[：未触发引入]{style="font-family:宋体"}

[[Redistribute route count]{lang="EN-US"}]{#struct_0_14538_x1521_644450315}

[[引入路由计数]{style="font-family:宋体"}]{#struct_0_14538_x1521_2127718202}

[[Process reset state]{lang="EN-US"}]{#struct_0_14538_x1521_517458968}

[[进程重启状态标志，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_2128308026}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_720227222}[：进程未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Under reset]{lang="EN-US"}]{#struct_0_14538_x1521_x1206181650}[：进程正在重启]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Under RIB smooth]{lang="EN-US"}]{#struct_0_14538_x1521_2128373562}[：进程]{style="font-family:宋体"}[正在同步]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由]{style="font-family:宋体"}

[[Current reset type]{lang="EN-US"}]{#struct_0_14538_x1521_1523745931}

[[当前进程重启类型，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_2127783739}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_939099410}[：进程未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[GR quit]{lang="EN-US"}]{#struct_0_14538_x1521_x988067318}[：]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[异常退出进行普通重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_14538_x1521_2127849275}[：删除]{style="font-family:
  宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Undo router-id]{lang="EN-US"}]{#struct_0_14538_x1521_x1051246639}[：删除]{style="font-family:宋体"}[Router-id]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Set router-id]{lang="EN-US"}]{#struct_0_14538_x1521_2127914811}[：设置]{style="font-family:宋体"}[Router-id]{lang="EN-US"}

[[Next reset type]{lang="EN-US"}]{#struct_0_14538_x1521_x252882007}

[[即将调度进程重启类型，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x860878377}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_2127980347}[：进程未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[GR quit]{lang="EN-US"}]{#struct_0_14538_x1521_2106664466}[：]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[异常退出进行普通重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_14538_x1521_2127521595}[：删除]{style="font-family:
  宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Undo router-id]{lang="EN-US"}]{#struct_0_14538_x1521_179477524}[：删除]{style="font-family:宋体"}[Router-id]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Set router-id]{lang="EN-US"}]{#struct_0_14538_x1521_2127587131}[：设置]{style="font-family:宋体"}[Router-id]{lang="EN-US"}

[[Reset prepare message replied]{lang="EN-US"}]{#struct_0_14538_x1521_x240012572}

[[响应准备重启消息的模块，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x843831503}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_14538_x1521_2127652667}[代表邻居维护模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_14538_x1521_550375641}[代表]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_14538_x1521_2127718203}[代表路由计算模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_14538_x1521_517393432}[代表路由引入模块]{style="font-family:宋体"}

[[Reset process message replied]{lang="EN-US"}]{#struct_0_14538_x1521_2128308027}

[[响应进程重启消息的模块，具体如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_720292758}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_14538_x1521_2128373563}[代表邻居维护模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_14538_x1521_1523680395}[代表]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_14538_x1521_1278948262}[代表路由计算模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_14538_x1521_2127783740}[代表路由引入模块]{style="font-family:宋体"}

[[Reset phase of module]{lang="EN-US"}]{#struct_0_14538_x1521_938509589}

[[各模块所处重启阶段。其中]{style="font-family:宋体"}[M]{lang="EN-US"}]{#struct_0_14538_x1521_2127849276}[代表主控制模块，]{style="font-family:宋体"}[P]{lang="EN-US"}[代表邻居维护模块，]{style="font-family:宋体"}[S]{lang="EN-US"}[代表]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_x1051443247}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete ASE]{lang="EN-US"}]{#struct_0_14538_x1521_2127914812}[：删除所有]{style="font-family:
  宋体"}[ASE LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete area LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x252685399}[：删除区域相关]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete area IF]{lang="EN-US"}]{#struct_0_14538_x1521_2127980348}[：删除区域下接口]{style="font-family:宋体"}

[[C]{lang="EN-US"}]{#struct_0_14538_x1521_2106992146}[代表路由计算模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_2127521596}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Delete topology]{lang="EN-US"}]{#struct_0_14538_x1521_179543060}[：删除区域拓扑]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete router]{lang="EN-US"}]{#struct_0_14538_x1521_2127587132}[：删除路由器路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete intra AS]{lang="EN-US"}]{#struct_0_14538_x1521_x240209180}[：删除]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete inter AS]{lang="EN-US"}]{#struct_0_14538_x1521_2127652668}[：删除]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Delete ASBR]{lang="EN-US"}]{#struct_0_14538_x1521_551096537}[：删除]{style="font-family:
  宋体"}[ASBR]{lang="EN-US"}[路由]{style="font-family:宋体"}

[[R]{lang="EN-US"}]{#struct_0_14538_x1521_2127718204}[代表路由引入模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14538_x1521_517590040}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete import]{lang="EN-US"}]{#struct_0_14538_x1521_2128308028}[：删除引入路由]{style="font-family:宋体"}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_719571862}

[[区域信息]{style="font-family:宋体"}]{#struct_0_14538_x1521_2128373564}

[[Area flag]{lang="EN-US"}]{#struct_0_14538_x1521_1523614859}

[[区域类型]{style="font-family:宋体"}]{#struct_0_14538_x1521_2127783741}

[[SPF scheduled count]{lang="EN-US"}]{#struct_0_14538_x1521_938575125}

[[OSPF]{lang="EN-US"}]{#struct_0_14538_x1521_2127849277}[区域的路由计算总数]{style="font-family:宋体"}

[[LSA count]{lang="EN-US"}]{#struct_0_14538_x1521_x1051377711}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_2127914813}[数目，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Count]{lang="EN-US"}]{#struct_0_14538_x1521_x252750935}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[checksum Sum]{lang="EN-US"}]{#struct_0_14538_x1521_2127980349}[：校验和]{lang="EN-US" style="font-family:宋体"}

[[IPsec profile name]{lang="EN-US"}]{#struct_0_14538_x1521_2107057682}

[[IPsec]{lang="EN-US"}]{#struct_0_14538_x1521_2127521597}[安全框架名]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_179608596}

[[区域的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_2127587133}[值]{style="font-family:宋体"}

[[Default cost]{lang="EN-US"}]{#struct_0_14538_x1521_2127652669}

[[路由的缺省开销值]{style="font-family:宋体"}]{#struct_0_14538_x1521_551031001}

[[Created by Vlink]{lang="EN-US"}]{#struct_0_14538_x1521_2127718205}

[[区域由]{style="font-family:宋体"}[Vlink]{lang="EN-US"}]{#struct_0_14538_x1521_517524504}[创建]{style="font-family:宋体"}

[[7/5 translator state]{lang="EN-US"}]{#struct_0_14538_x1521_2128308029}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_2128373565}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者状态，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_14538_x1521_2127783742}[：表示本设备是通过命令指定的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Elected]{lang="EN-US"}]{#struct_0_14538_x1521_2127849278}[：表示本设备是通过选举指定的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14538_x1521_2127914814}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[本设备不是]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{style="font-family:宋体"}

[[7/5 translate stability timer interval]{lang="EN-US"}]{#struct_0_14538_x1521_x252554327}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_2127980350}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[转换稳定定时器的超时时间间隔，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#2112964411 .myid}
[]{#_Toc404789048}[]{#struct_0_14538_x1521_2106467857}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 abr-asbr**

------------------------------------------------------------------------

[**[display ospfv3 abr-asbr]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}**]{#struct_0_14538_x1521_x1888389701}[命令用来显示到]{style="font-size:10.5pt;font-family:宋体"}[OSPFv3]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[的区域边界路由器和自治系统边界路由器的路由信息。]{style="font-size:10.5pt;font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2127521598}

[**[display ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **abr-asbr**]{lang="EN-US"}]{#struct_0_14538_x1521_179149844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1945128116}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1252316020}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x174632963}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x2087785479}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x835336937}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1557592319}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1674984246}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2127587134}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x239815964}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程下到区域边界路由器和自治系统边界路由器的路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_948280334}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1980047723}[显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[和]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 abr-asbr]{lang="EN-US"}]{#struct_0_14538_x1521_x1218783931}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination :1.1.1.2                                   Rtr Type : ABR]{lang="EN-US"}

[ Area        :0.0.0.0                                   Path Type: Intra]{lang="EN-US"}

[ NextHop     :FE80:1:1::1                               Cost     : 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination :1.1.1.3                                   Rtr Type : ASBR]{lang="EN-US"}

[ Area        :0.0.0.0                                   Path Type: Intra]{lang="EN-US"}

[ NextHop     :FE80:2:1::1                               Cost     : 1]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ospfv3 abr-asbr]{lang="EN-US"}]{#struct_0_14538_x1521_x713328367}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1193224871}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1196591315}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_2127652670}

[[OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}]{#struct_0_14538_x1521_550572250}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1838230102}[进程是]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[是]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}

[[Destination]{lang="EN-US"}]{#struct_0_14538_x1521_418649437}

[[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_x963627678}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Rtr Type]{lang="EN-US"}]{#struct_0_14538_x1521_x2040442428}

[[路由器类型，包括]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_x481945409}[和]{style="font-family:宋体"}[ASBR]{lang="EN-US"}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_2127718206}

[[下一跳地址所在的区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_517721112}

[[Path Type]{lang="EN-US"}]{#struct_0_14538_x1521_511225768}

[[到]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_x1145870074}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的路由类型，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Intra]{lang="EN-US"}]{#struct_0_14538_x1521_559678302}[表示区域内路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inter]{lang="EN-US"}]{#struct_0_14538_x1521_x291313028}[表示区域间路由]{lang="EN-US" style="font-family:宋体"}

[[NextHop]{lang="EN-US"}]{#struct_0_14538_x1521_2128308030}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_14538_x1521_720096149}

[[Cost]{lang="EN-US"}]{#struct_0_14538_x1521_1268547553}

[[从本路由器到达]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_x940997789}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1056752937 .myid}
[]{#_Toc245205323}[]{#_Toc138238093}[]{#_Toc93984835}[]{#_Toc81478701}[]{#_Toc58333176}[]{#_Toc58294826}[]{#_Toc33866050}[]{#_Toc303674203}[]{#_Toc303084625}[]{#_Toc404789049}[]{#struct_0_14538_x1521_x373568844}[]{#_Toc348020485}[]{#_Toc132709342}[]{#_Toc133749766}[]{#_Toc132709343}[]{#_Toc133749767}[]{#_Toc132709344}[]{#_Toc133749768}[]{#_Toc132709345}[]{#_Toc133749769}[]{#_Toc132709346}[]{#_Toc133749770}[]{#_Toc132709347}[]{#_Toc133749771}[]{#_Toc132709348}[]{#_Toc133749772}[]{#_Toc132709349}[]{#_Toc133749773}[]{#_Toc132709350}[]{#_Toc133749774}[]{#_Toc132709351}[]{#_Toc133749775}[]{#_Toc132709352}[]{#_Toc133749776}[]{#_Toc132709353}[]{#_Toc133749777}[]{#_Toc132709354}[]{#_Toc133749778}[]{#_Toc132709355}[]{#_Toc133749779}[]{#_Toc132709356}[]{#_Toc133749780}[]{#_Toc132709360}[]{#_Toc133749784}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 abr-summary**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ospfv3** **abr-summary**]{lang="EN-US"}]{#struct_0_14538_x1521_x1270194804}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1178259095}

[**[display]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] \[ **area** *area-id* \] **abr-summary** \[ *ipv6-address* *prefix-length* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_14538_x1521_2128373566}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1523483787}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1640206644}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1879013255}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1788007315}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1889760772}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1957918488}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1660995786}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_112892339}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x601099618}[：当前的聚合配置所在进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}**[ *area-id*]{lang="EN-US"}]{#struct_0_14538_x1521_x1799616015}[：显示位于指定区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。如果未指定本参数，将显示所有区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[为区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其处理成]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式）或]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*[ *prefix-length*]{lang="EN-US"}]{#struct_0_14538_x1521_x524332981}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_1182526020}[：显示]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1061068797}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1504006873}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 1 abr-summary]{lang="EN-US"}]{#struct_0_14538_x1521_x601034082}

[ ]{lang="EN-US"}

[             OSPFv3 Process 1 with Router ID 2.2.2.2]{lang="EN-US"}

[ ]{lang="EN-US"}

[                     Area: 1.1.1.1]{lang="EN-US"}

[ Total summary addresses: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Prefix      : 1000:4::/32]{lang="EN-US"}

[ Status      : Advertise]{lang="EN-US"}

[ NULL0       : Active]{lang="EN-US"}

[ Cost        : 1 (Configured)]{lang="EN-US"}

[ Routes count: 2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ospfv3 abr-summary]{lang="EN-US"}]{#struct_0_14538_x1521_2138358497}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1198789095}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_1244179670}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1551147731}

[[Total summary addresses]{lang="EN-US"}]{#struct_0_14538_x1521_x1268538330}

[[聚合路由的路由数]{style="font-family:宋体"}]{#struct_0_14538_x1521_1549099290}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_x269001407}

[[聚合路由所在的区域]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1680173829}

[[Prefix]{lang="EN-US"}]{#struct_0_14538_x1521_x600968546}

[[聚合路由的地址前缀]{style="font-family:宋体"}]{#struct_0_14538_x1521_969643674}

[[Status]{lang="EN-US"}]{#struct_0_14538_x1521_x250257662}

[[聚合路由的状态：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1265942948}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advertise]{lang="EN-US"}]{#struct_0_14538_x1521_1366047711}[：已发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not-advertise]{lang="EN-US"}]{#struct_0_14538_x1521_180126728}[：未发布]{style="font-family:宋体"}

[[NULL0]{lang="EN-US"}]{#struct_0_14538_x1521_x600903010}

[[NULL0]{lang="EN-US"}]{#struct_0_14538_x1521_592411946}[路由：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_14538_x1521_x450741206}[：激活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_14538_x1521_1100906001}[：未激活]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_14538_x1521_407636985}

[[聚合路由的开销]{style="font-family:宋体"}]{#struct_0_14538_x1521_379258477}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Configured]{lang="EN-US"}]{#struct_0_14538_x1521_x601361762}[：配置的聚合开销]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Not Configured]{lang="EN-US"}]{#struct_0_14538_x1521_x168925771}[：未配置聚合开销]{style="font-family:宋体"}

[[Routes count]{lang="EN-US"}]{#struct_0_14538_x1521_1754753195}

[[被聚合的路由数]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1474836763}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x346700801}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合详细]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 1 abr-summary verbose]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1120996007}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[             OSPFv3 Process 1 with Router ID 2.2.2.2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_2071284099}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[                        Area: 1.1.1.1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1120275111}

[[Total summary addresses: 1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1693636176}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[ Prefix      : 1000:4::/32]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1531821669}

[[ Status      : Advertise]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1367442398}

[[ NULL0       : Active]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1707656059}

[[ Cost        : 1 (Configured)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1955264689}

[[ Routes count: 2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_616780511}

[[   Destination                                        Metric]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1597145513}

[[   1000:4:10:3::/96                                   1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1120340647}

[[   1000:4:11:3::/96                                   1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_2101425151}

[[表1-2 ]{lang="EN-US"}[display ospfv3 abr-summary verbose]{lang="EN-US"}]{#struct_0_14538_x1521_x569708360}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1202428295}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2014806896}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1123371675}

[[Destination]{lang="EN-US"}]{#struct_0_14538_x1521_1760202375}

[[被聚合路由的目的地址]{style="font-family:宋体"}]{#struct_0_14538_x1521_1088503110}

[[Metric]{lang="EN-US"}]{#struct_0_14538_x1521_x1275002315}

[[路由的开销值]{style="font-family:宋体"}]{#struct_0_14538_x1521_x803641141}

[ ]{lang="EN-US"}

::: {#1204678285 .myid}
[]{#_Toc404789050}[]{#struct_0_14538_x1521_217221476}[]{#_Toc375657056}[]{#_Toc364781572}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 asbr-summary**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ospfv3** **asbr-summary**]{lang="EN-US"}]{#struct_0_14538_x1521_x48825686}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_216762724}

[**[display]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **asbr-summary** \[ *ipv6-address* *prefix-length* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_14538_x1521_1526298574}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_216828260}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x205443009}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2105705273}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1728983666}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_216893796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1293579833}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x398836074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_216959332}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x1798986435}[：当前的聚合配置所在进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*[ *prefix-length*]{lang="EN-US"}]{#struct_0_14538_x1521_x1598802393}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_x1367191420}[：显示]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_217549156}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_990819437}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 1 asbr-summary]{lang="EN-US"}]{#struct_0_14538_x1521_217614692}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 2.2.2.2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total summary addresses: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Prefix      : 1000:4::/32]{lang="EN-US"}

[ Status      : Advertise]{lang="EN-US"}

[ NULL0       : Active]{lang="EN-US"}

[ Cost        : 1 (Configured)]{lang="EN-US"}

[ Tag         : (Not configured)]{lang="EN-US"}

[ Nssa-only   : (Not configured)]{lang="EN-US"}

[ Routes count: 2]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ospfv3 asbr-summary]{lang="EN-US"}]{#struct_0_14538_x1521_496034757}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x546829553}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1910935840}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_1783108806}

[[Total summary addresses]{lang="EN-US"}]{#struct_0_14538_x1521_1783174342}

[[聚合路由的路由数]{style="font-family:宋体"}]{#struct_0_14538_x1521_2010073538}

[[Prefix]{lang="EN-US"}]{#struct_0_14538_x1521_1783239878}

[[聚合路由的地址前缀和前缀长度]{style="font-family:宋体"}]{#struct_0_14538_x1521_1783305414}

[[Status]{lang="EN-US"}]{#struct_0_14538_x1521_x348471654}

[[聚合路由的状态：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1782846662}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advertise]{lang="EN-US"}]{#struct_0_14538_x1521_x1884463195}[：已发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not-advertise]{lang="EN-US"}]{#struct_0_14538_x1521_1782912198}[：未发布]{style="font-family:宋体"}

[[NULL0]{lang="EN-US"}]{#struct_0_14538_x1521_x1486385893}

[[NULL0]{lang="EN-US"}]{#struct_0_14538_x1521_1782977734}[路由：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_14538_x1521_1783043270}[：激活]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_14538_x1521_x697302307}[：未激活]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_14538_x1521_1783633094}

[[聚合路由的开销：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x316734819}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Configured]{lang="EN-US"}]{#struct_0_14538_x1521_1783698630}[：配置的聚合开销]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Not configured]{lang="EN-US"}]{#struct_0_14538_x1521_x1835347370}[：未配置聚合开销]{style="font-family:宋体"}

[[Tag]{lang="EN-US"}]{#struct_0_14538_x1521_1783108805}

[[聚合路由的标记：]{style="font-family:宋体"}]{#struct_0_14538_x1521_536793722}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Configured]{lang="EN-US"}]{#struct_0_14538_x1521_1783174341}[：配置的聚合标记]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Not configured]{lang="EN-US"}]{#struct_0_14538_x1521_2009876930}[：未配置聚合标记]{style="font-family:宋体"}

[[Nssa-only]{lang="EN-US"}]{#struct_0_14538_x1521_1783239877}

[[是否配置]{style="font-family:宋体"}[Nssa-only]{lang="EN-US"}]{#struct_0_14538_x1521_1783305413}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Configured]{lang="EN-US"}]{#struct_0_14538_x1521_x348012902}[：配置了]{style="font-family:
  宋体"}[Nssa-only]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Not configured]{lang="EN-US"}]{#struct_0_14538_x1521_1782846661}[：未配置]{style="font-family:宋体"}[Nssa-only]{lang="EN-US"}

[[Routes count]{lang="EN-US"}]{#struct_0_14538_x1521_x1884528731}

[[被聚合的路由数]{style="font-family:宋体"}]{#struct_0_14538_x1521_1782912197}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1486844645}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合详细]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 1 asbr-summary verbose]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1786336592}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[               OSPFv3 Process 1 with Router ID 2.2.2.2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1782977733}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[ Total summary addresses: 1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1120545764}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[ Prefix      : 1000:4::/32]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_2094373023}

[[ Status      : Advertise]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x58462790}

[[ NULL0       : Active]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1783043269}

[[ Cost        : 1 (Configured)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x696712484}

[[ Tag         : (Not configured)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1007534823}

[[ Nssa-only   : (Not configured)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1783633093}

[[ Routes count: 2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x316931427}

[[  Destination                                 Protocol Process Type Metric]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x765763995}

[[  1000:4:10:3::/96                            Static   0       2    1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1783698629}

[[  1000:4:11:3::/96                            Static   0       2    1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1835937195}

[[表1-4 ]{lang="EN-US"}[display ospfv3 asbr-summary verbose]{lang="EN-US"}]{#struct_0_14538_x1521_170496145}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x803269523}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_1783108804}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_536728186}

[[Destination]{lang="EN-US"}]{#struct_0_14538_x1521_1783174340}

[[被聚合路由的前缀和前缀长度]{style="font-family:宋体"}]{#struct_0_14538_x1521_2009942466}

[[Protocol]{lang="EN-US"}]{#struct_0_14538_x1521_1783239876}

[[被聚合路由的协议类型]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1039382663}

[[Process]{lang="EN-US"}]{#struct_0_14538_x1521_1783305412}

[[被聚合路由的协议进程]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x348078438}

[[Type]{lang="EN-US"}]{#struct_0_14538_x1521_1782846660}

[[被聚合路由的类型]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1884594267}

[[Metric]{lang="EN-US"}]{#struct_0_14538_x1521_1782912196}

[[被聚合路由的开销]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1486779109}

[ ]{lang="EN-US"}

::::: {#-887885025 .myid}
[]{#_Toc404789051}[]{#struct_0_14538_x1521_x601165154}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 graceful-restart**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_x1755564064}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_1752368186}
:::

[ ]{lang="EN-US"}

[**[display ospfv3 graceful-restart]{lang="EN-US"}**]{#struct_0_14538_x1521_x1796093437}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x955308258}

[**[display ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **graceful-restart** \[ **verbose** \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1756784891}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1300720702}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1812454333}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2023696626}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x600575330}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1753102410}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_209533882}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x1553553741}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x883119025}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1639846952}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_x1525791485}[：显示]{style="font-family:宋体"}[GR]{lang="EN-US"}[详细状态信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_270084833}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1117305557}[显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息（]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 graceful-restart]{lang="EN-US"}]{#struct_0_14538_x1521_x600509794}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 3.3.3.3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Graceful-restart capability     : Enable]{lang="EN-US"}

[ Graceful-restart support        : Planned and un-planned, Partial]{lang="EN-US"}

[ Helper capability               : Enable]{lang="EN-US"}

[ Helper support                  : Planned and un-planned]{lang="EN-US"}

[ Current GR state                : Normal]{lang="EN-US"}

[ Graceful-restart period         : 120 seconds]{lang="EN-US"}

[ Number of neighbors under helper: 0]{lang="EN-US"}

[ Number of restarting neighbors  : 0]{lang="EN-US"}

[ Last exit reason:]{lang="EN-US"}

[   Restarter: None]{lang="EN-US"}

[   Helper   : None]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ospfv3 graceful-restart]{lang="EN-US"}]{#struct_0_14538_x1521_x992146756}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1203287175}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1611591979}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_287888001}

[[OSPFv3 Process 1 with Router ID 3.3.3.3]{lang="EN-US"}]{#struct_0_14538_x1521_1828857727}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x469975489}[进程是]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[是]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息]{style="font-family:宋体"}

[[Graceful-restart capability]{lang="EN-US"}]{#struct_0_14538_x1521_x601099617}

[[是否使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1799419407}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_14538_x1521_1398433553}[：]{lang="EN-US" style="font-family:宋体"}[使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_14538_x1521_2033318483}[：]{lang="EN-US" style="font-family:宋体"}[未使能]{style="font-family:宋体"}

[[Graceful-restart support]{lang="EN-US"}]{#struct_0_14538_x1521_x1525463808}

[[进程]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_14538_x1521_x1525529344}[支持模式（]{style="font-family:宋体"}[GR]{lang="EN-US"}[使能时才显示）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Planned and un-planned]{lang="EN-US"}]{#struct_0_14538_x1521_x1525660416}[：支持计划和非计划]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Planned only]{lang="EN-US"}]{#struct_0_14538_x1521_x1525725952}[：只支持计划性]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Partial]{lang="EN-US"}]{#struct_0_14538_x1521_x1525791488}[：支持接口级]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Global]{lang="EN-US"}]{#struct_0_14538_x1521_x1525857024}[：不支持接口级]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[，支持全局]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[Helper capability]{lang="EN-US"}]{#struct_0_14538_x1521_x1647924009}

[[是否使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1699430053}[协议的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_14538_x1521_x601034081}[：]{lang="EN-US" style="font-family:宋体"}[使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_14538_x1521_2138292961}[：]{lang="EN-US" style="font-family:宋体"}[未使能]{style="font-family:宋体"}

[[Helper support]{lang="EN-US"}]{#struct_0_14538_x1521_x1525005056}

[[显示]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_14538_x1521_x1525463807}[的支持模式（]{style="font-family:宋体"}[Helper]{lang="EN-US"}[使能时才显示）：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Strict LSA check]{lang="EN-US"}]{#struct_0_14538_x1521_x1525529343}[：]{lang="EN-US" style="font-family:
  宋体"}[Helper]{lang="EN-US"}[端支持严格的]{lang="EN-US" style="font-family:
  宋体"}[LSA]{lang="EN-US"}[检查]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Planned and un-planned]{lang="EN-US"}]{#struct_0_14538_x1521_x1525660415}[：支持作为计划和非计划]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Helper]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Planned only]{lang="EN-US"}]{#struct_0_14538_x1521_x1525725951}[：只支持作为计划]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Helper]{lang="EN-US"}

[[Current GR state]{lang="EN-US"}]{#struct_0_14538_x1521_x1915031160}

[[当前]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_14538_x1521_174909191}[的状态，其状态有如下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_14538_x1521_x1926055823}[：表示正处在非]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[的正常状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Under GR]{lang="EN-US"}]{#struct_0_14538_x1521_1043789964}[：表示正在]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[过程中，自身作为]{lang="EN-US" style="font-family:宋体"}[Restarter]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Under Helper]{lang="EN-US"}]{#struct_0_14538_x1521_x600968545}[：表示正在]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[过程中，自身作为]{lang="EN-US" style="font-family:宋体"}[Helper]{lang="EN-US"}

[[Graceful-restart period]{lang="EN-US"}]{#struct_0_14538_x1521_969709210}

[[GR]{lang="EN-US"}]{#struct_0_14538_x1521_952143102}[重启间隔时间]{style="font-family:宋体"}

[[Number of neighbors under helper]{lang="EN-US"}]{#struct_0_14538_x1521_x2106079840}

[[处于]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_14538_x1521_x881666509}[模式的邻居个数]{style="font-family:宋体"}

[[Number of restarting neighbors]{lang="EN-US"}]{#struct_0_14538_x1521_x600903009}

[[处于]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}]{#struct_0_14538_x1521_592870699}[模式的邻居个数]{style="font-family:宋体"}

[[Last exit reason]{lang="EN-US"}]{#struct_0_14538_x1521_1121061544}

[[上次退出原因，其中：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1121127080}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Restarter]{lang="EN-US"}]{#struct_0_14538_x1521_1316863774}[：表示退出]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[的原因]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[None]{lang="EN-US"}]{#struct_0_14538_x1521_x1161999439}[：无]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Completed]{lang="EN-US"}]{#struct_0_14538_x1521_x272545374}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[完成]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Interval]{lang="EN-US"}]{#struct_0_14538_x1521_x1949605836}[ ]{lang="EN-US"}[timer]{lang="EN-US"}[ ]{lang="EN-US"}[is]{lang="EN-US"}[ ]{lang="EN-US"}[fired]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_404084502}[ ]{lang="EN-US"}[state]{lang="EN-US"}[ ]{lang="EN-US"}[change]{lang="EN-US"}[：接口状态变化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Received]{lang="EN-US"}]{#struct_0_14538_x1521_x718614632}[ ]{lang="EN-US"}[1-way]{lang="EN-US"}[ ]{lang="EN-US"}[hello]{lang="EN-US"}[：收到邻居的]{lang="EN-US" style="font-family:宋体"}[1-way]{lang="EN-US"}[ H]{lang="EN-US"}[ello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Reset]{lang="EN-US"}]{#struct_0_14538_x1521_x1600936631}[ ]{lang="EN-US"}[neighbor]{lang="EN-US"}[：邻居发生]{lang="EN-US" style="font-family:宋体"}[Reset]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DR]{lang="EN-US"}]{#struct_0_14538_x1521_1970168443}[ ]{lang="EN-US"}[or]{lang="EN-US"}[ ]{lang="EN-US"}[BDR]{lang="EN-US"}[ ]{lang="EN-US"}[change]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[DR]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[BDR]{lang="EN-US"}[发生变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Helper]{lang="EN-US"}]{#struct_0_14538_x1521_807904849}[：表示退出]{style="font-family:宋体"}[Helper]{lang="EN-US"}[的原因]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[None]{lang="EN-US"}]{#struct_0_14538_x1521_x927821804}[：无]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Completed]{lang="EN-US"}]{#struct_0_14538_x1521_1012561527}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[完成]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Received]{lang="EN-US"}]{#struct_0_14538_x1521_x758714912}[ ]{lang="EN-US"}[1-way]{lang="EN-US"}[ ]{lang="EN-US"}[hello]{lang="EN-US"}[：收到邻居的]{lang="EN-US" style="font-family:宋体"}[1-way]{lang="EN-US"}[ H]{lang="EN-US"}[ello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Grace]{lang="EN-US"}]{#struct_0_14538_x1521_x1801772994}[ ]{lang="EN-US"}[Period]{lang="EN-US"}[ ]{lang="EN-US"}[timer]{lang="EN-US"}[ ]{lang="EN-US"}[is]{lang="EN-US"}[ ]{lang="EN-US"}[fired]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Lsa]{lang="EN-US"}]{#struct_0_14538_x1521_168643822}[ ]{lang="EN-US"}[check]{lang="EN-US"}[ ]{lang="EN-US"}[failed]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[检查未通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Reset]{lang="EN-US"}]{#struct_0_14538_x1521_807369029}[ ]{lang="EN-US"}[neighbor]{lang="EN-US"}[：邻居发生]{lang="EN-US" style="font-family:宋体"}[Reset]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Received]{lang="EN-US"}]{#struct_0_14538_x1521_562712151}[ ]{lang="EN-US"}[MAXAGE]{lang="EN-US"}[ ]{lang="EN-US"}[gracelsa]{lang="EN-US"}[ ]{lang="EN-US"}[but]{lang="EN-US"}[ ]{lang="EN-US"}[neighbor]{lang="EN-US"}[ ]{lang="EN-US"}[is]{lang="EN-US"}[ ]{lang="EN-US"}[not]{lang="EN-US"}[ ]{lang="EN-US"}[full]{lang="EN-US"}[：收到]{lang="EN-US" style="font-family:宋体"}[到达老化时间]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[Grace]{lang="EN-US"}[ LSA]{lang="EN-US"}[，]{style="font-family:宋体"}[但邻居状态未达到]{lang="EN-US" style="font-family:宋体"}[FULL]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1524939519}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[详细状态信息（]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 graceful-restart verbose]{lang="EN-US"}]{#struct_0_14538_x1521_x1525529338}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 3.3.3.3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Graceful-restart capability     : Enable]{lang="EN-US"}

[ Graceful-restart support        : Planned and un-planned, Partial]{lang="EN-US"}

[ Helper capability               : Enable]{lang="EN-US"}

[ Helper support                  : Planned and un-planned]{lang="EN-US"}

[ Current GR state                : Normal]{lang="EN-US"}

[ Graceful-restart period         : 120 seconds]{lang="EN-US"}

[ Number of neighbors under helper: 0]{lang="EN-US"}

[ Number of restarting neighbors  : 0]{lang="EN-US"}

[ Last exit reason:]{lang="EN-US"}

[   Restarter: None]{lang="EN-US"}

[   Helper   : None]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.0]{lang="EN-US"}

[ Area flag: Normal]{lang="EN-US"}

[ Area up interface count: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Virtual-link Neighbor-ID: 100.1.1.1, Neighbor-state: Full]{lang="EN-US"}

[ Restarter state: Normal   State: P-2-P    Type: Virtual]{lang="EN-US"}

[ Interface: 6696 (Vlan-interface200), Instance-ID: 0]{lang="EN-US"}

[ Local  IPv6 address: 200:1:FFFF::1]{lang="EN-US"}

[ Remote IPv6 address: 201:FFFF::2]{lang="EN-US"}

[ Transit area: 0.0.0.1]{lang="EN-US"}

[ Last exit reason:]{lang="EN-US"}

[   Restarter: None]{lang="EN-US"}

[   Helper   : None]{lang="EN-US"}

[ Neighbor       GR state       Last helper exit reason]{lang="EN-US"}

[ 100.1.1.1      Normal         None]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.1]{lang="EN-US"}

[ Area flag: Transit]{lang="EN-US"}

[ Area up interface count: 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Interface: 5506 (Vlan-interface3), Instance-ID: 0]{lang="EN-US"}

[ Restarter state: Normal   State: DR       Type: Broadcast]{lang="EN-US"}

[ Last exit reason:]{lang="EN-US"}

[   Restarter: None]{lang="EN-US"}

[   Helper   : None]{lang="EN-US"}

[ Neighbor count of this interface: 0]{lang="EN-US"}

[ Number of neighbors under helper: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Interface: 6696 (Vlan-interface200), Instance-ID: 0]{lang="EN-US"}

[ Restarter state: Normal   State: DR       Type: Broadcast]{lang="EN-US"}

[ Last exit reason:]{lang="EN-US"}

[   Restarter: None]{lang="EN-US"}

[   Helper   : None]{lang="EN-US"}

[ Neighbor count of this interface: 1]{lang="EN-US"}

[ Number of neighbors under helper: 0]{lang="EN-US"}

[ Neighbor       GR state       Last helper exit reason]{lang="EN-US"}

[ 100.1.1.1      Normal         None]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Sham-link Neighbor-ID: 100.1.1.1, Neighbor-state: Full]{lang="EN-US"}

[ Restarter state: Normal   State: P-2-P    Type: Sham]{lang="EN-US"}

[ Interface-ID: 2147483649, Instance-ID: 0]{lang="EN-US"}

[ Source      : 8000:88::FFFF]{lang="EN-US"}

[ Destination : 7000:77::FFFF]{lang="EN-US"}

[ Last exit reason:]{lang="EN-US"}

[   Restarter: None]{lang="EN-US"}

[   Helper   : None]{lang="EN-US"}

[ Neighbor       GR state       Last helper exit reason]{lang="EN-US"}

[ 100.1.1.1      Normal         None]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.5]{lang="EN-US"}

[ Area flag: NSSANoSummaryNoImportRoute]{lang="EN-US"}

[ 7/5 translator state: Disabled]{lang="EN-US"}

[ 7/5 translate stability timer interval: 0]{lang="EN-US"}

[ Area up interface count: 0]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ospfv3 graceful-restart]{lang="EN-US"}]{#struct_0_14538_x1521_x658305108}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_539349137}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1525594874}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1525660410}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_x1525725946}

[[区域信息]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1525791482}

[[Area flag]{lang="EN-US"}]{#struct_0_14538_x1521_x1525857018}

[[区域类型：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1525922554}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_14538_x1521_809993974}[：普通区域]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_14538_x1521_x1524939514}[：传输区]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_x1525005050}[：]{lang="EN-US" style="font-family:宋体"}[Stub]{lang="EN-US"}[区域]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StubNoSummary]{lang="EN-US"}]{#struct_0_14538_x1521_x1525463801}[：完全]{lang="EN-US" style="font-family:宋体"}[Stub]{lang="EN-US"}[区域]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1525529337}[：]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSANoSummary]{lang="EN-US"}]{#struct_0_14538_x1521_x1525594873}[：完全]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSANoSummaryNoImportRoute]{lang="EN-US"}]{#struct_0_14538_x1521_x1525660409}[：完全]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域，配置了]{lang="EN-US" style="font-family:宋体"}[no-import-route]{lang="EN-US"}[参数]{lang="EN-US" style="font-family:宋体"}

[[7/5 translator state]{lang="EN-US"}]{#struct_0_14538_x1521_x1525725945}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1525791481}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者状态，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_14538_x1521_x1525857017}[：表示通过命令指定]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Elected]{lang="EN-US"}]{#struct_0_14538_x1521_x1525922553}[：表示通过选举指定]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14538_x1521_x1524939513}[：表示不是]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{lang="EN-US" style="font-family:宋体"}

[[7/5 translate stability timer interval]{lang="EN-US"}]{#struct_0_14538_x1521_x1525005049}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_40620135}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[转换稳定定时器的超时时间，单位为秒]{style="font-family:宋体"}

[[Area up interface count]{lang="EN-US"}]{#struct_0_14538_x1521_40554599}

[[区域下]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_14538_x1521_40489063}[的接口计数]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_40423527}

[[区域内的普通接口，以及虚连接所属的出接口]{style="font-family:宋体"}]{#struct_0_14538_x1521_40357991}

[[Instance-ID]{lang="EN-US"}]{#struct_0_14538_x1521_40292455}

[[接口实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_40226919}

[[Restarter state]{lang="EN-US"}]{#struct_0_14538_x1521_40161383}

[[作为]{style="font-family:宋体"}[Restarter]{lang="EN-US"}]{#struct_0_14538_x1521_41144423}[的状态]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_14538_x1521_41078887}

[[接口状态]{style="font-family:宋体"}]{#struct_0_14538_x1521_40620136}

[[Type]{lang="EN-US"}]{#struct_0_14538_x1521_40554600}

[[接口的网络类型]{style="font-family:宋体"}]{#struct_0_14538_x1521_40489064}

[[Neighbor count of this interface]{lang="EN-US"}]{#struct_0_14538_x1521_40423528}

[[接口下的邻居个数]{style="font-family:宋体"}]{#struct_0_14538_x1521_40357992}

[[Neighbor]{lang="EN-US"}]{#struct_0_14538_x1521_40292456}

[[邻居]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_40226920}

[[GR state]{lang="EN-US"}]{#struct_0_14538_x1521_40161384}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_14538_x1521_41144424}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_14538_x1521_41078888}[：普通状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Under GR]{lang="EN-US"}]{#struct_0_14538_x1521_40620133}[：进程正在]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Under Helper]{lang="EN-US"}]{#struct_0_14538_x1521_40554597}[：进程正在作为]{lang="EN-US" style="font-family:宋体"}[GR Helper]{lang="EN-US"}

[[Last helper exit reason]{lang="EN-US"}]{#struct_0_14538_x1521_40489061}

[[上一次作为该邻居]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_14538_x1521_40423525}[退出的原因]{style="font-family:宋体"}

[[Virtual-link Neighbor-ID]{lang="EN-US"}]{#struct_0_14538_x1521_40357989}

[[虚连接的邻居]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_40292453}

[[Neighbor-State]{lang="EN-US"}]{#struct_0_14538_x1521_40226917}

[[虚连接和邻居的状态，包括]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_14538_x1521_40161381}[、]{style="font-family:宋体"}[Init]{lang="EN-US"}[、]{style="font-family:宋体"}[2-Way]{lang="EN-US"}[、]{style="font-family:宋体"}[ExStart]{lang="EN-US"}[、]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[、]{style="font-family:宋体"}[Loading]{lang="EN-US"}[和]{style="font-family:宋体"}[Full]{lang="EN-US"}

[[Local  IPv6 address]{lang="EN-US"}]{#struct_0_14538_x1521_41144421}

[[本地]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_14538_x1521_41078885}[地址]{style="font-family:宋体"}

[[Remote IPv6 address]{lang="EN-US"}]{#struct_0_14538_x1521_40554598}

[[对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_14538_x1521_40489062}[地址]{style="font-family:宋体"}

[[Transit area]{lang="EN-US"}]{#struct_0_14538_x1521_40423526}

[[传输区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_40357990}

[[Sham-link Neighbor-ID]{lang="EN-US"}]{#struct_0_14538_x1521_40292454}

[[Shamlink]{lang="EN-US"}]{#struct_0_14538_x1521_40226918}[的邻居]{style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[Source]{lang="EN-US"}]{#struct_0_14538_x1521_40161382}

[[Shamlink]{lang="EN-US"}]{#struct_0_14538_x1521_41144422}[源地址]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_14538_x1521_41078886}

[[Shamlink]{lang="EN-US"}]{#struct_0_14538_x1521_40620139}[目的地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#318907167 .myid}
[]{#_Toc404789052}[]{#struct_0_14538_x1521_x727303610}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 interface**

------------------------------------------------------------------------

[**[display ospfv3 interface]{lang="EN-US"}**]{#struct_0_14538_x1521_x1428726042}[命令用来显示]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2083570519}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **interface** \[ *interface-type interface-number* \| **verbose** \]]{lang="EN-US"}]{#struct_0_14538_x1521_1472162579}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1660608991}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_408204030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_690774639}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x601361761}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x168860235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x587128375}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_28286859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_163235315}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1095993819}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14538_x1521_x807470666}[：接口类型和接口编号。显示指定接口的详细信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_385413480}[：显示所有接口的详细信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1665878532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_14538_x1521_x601296225}[OSPFv3]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的接口概要信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定接口或参数]{style="font-family:宋体"}]{#struct_0_14538_x1521_1338038771}**[verbose]{lang="EN-US"}**[，将显示所有接口的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1232750088}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x1434099634}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x2095289948}[显示运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14538_x1521_x601230689}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.0]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ GigabitEthernet1/0/1 is up, line protocol is up]{lang="EN-US"}

[  Interface ID 3        Instance ID 0]{lang="EN-US"}

[  IPv6 prefixes]{lang="EN-US"}

[    fe80::200:12ff:fe34:1  (Link-Local address)]{lang="EN-US"}

[    2001::1]{lang="EN-US"}

[  Cost: 1       State: BDR       Type: Broadcast    MTU: 1500]{lang="EN-US"}

[  Priority: 1]{lang="EN-US"}

[  Designated router: 2.2.2.2]{lang="EN-US"}

[  Backup designated router: 1.1.1.1]{lang="EN-US"}

[  Timers: Hello 10, Dead 40, Poll 40, Retransmit 5, Transmit delay 1]{lang="EN-US"}

[  Neighbor count is 1, Adjacent neighbor count is 1]{lang="EN-US"}

[  IPsec profile name: profile001]{lang="EN-US"}

[  Exchanging/Loading neighbors: 0]{lang="EN-US"}

[  Wait timer: Off,  LsAck timer: Off]{lang="EN-US"}

[  Prefix-suppression is enabled]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x570167113}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1767356159}[显示运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface1]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 interface vlan-interface 1]{lang="EN-US"}]{#struct_0_14538_x1521_x601165153}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.0]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Vlan-interface1 is up, line protocol is up]{lang="EN-US"}

[  Interface ID 65697        Instance ID 0]{lang="EN-US"}

[  IPv6 prefixes]{lang="EN-US"}

[    fe80::200:12ff:fe34:1  (Link-Local address)]{lang="EN-US"}

[    2001::1]{lang="EN-US"}

[  Cost: 1       State: BDR       Type: Broadcast    MTU: 1500]{lang="EN-US"}

[  Priority: 1]{lang="EN-US"}

[  Designated router: 2.2.2.2]{lang="EN-US"}

[  Backup designated router: 1.1.1.1]{lang="EN-US"}

[  Timers: Hello 10, Dead 40, Poll 40, Retransmit 5, Transmit delay 1]{lang="EN-US"}

[  Neighbor count is 1, Adjacent neighbor count is 1]{lang="EN-US"}

[  IPsec profile name: profile001]{lang="EN-US"}

[  Exchanging/Loading neighbors: 0]{lang="EN-US"}

[  Wait timer: Off,  LsAck timer: Off]{lang="EN-US"}

[  Prefix-suppression is enabled]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display ospfv3 interface]{lang="EN-US"}]{#struct_0_14538_x1521_x1756022816}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1200635175}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x600575329}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_1752643659}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_x163461382}

[[接口所属的区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x546728473}

[[Interface ID]{lang="EN-US"}]{#struct_0_14538_x1521_323401289}

[[接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_501478870}

[[Instance ID]{lang="EN-US"}]{#struct_0_14538_x1521_55876000}

[[实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x600509793}

[[IPv6 prefixes]{lang="EN-US"}]{#struct_0_14538_x1521_x991819076}

[[IPv6]{lang="EN-US"}]{#struct_0_14538_x1521_1299713331}[前缀]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_14538_x1521_x494536066}

[[接口开销]{style="font-family:宋体"}]{#struct_0_14538_x1521_423890750}

[[State]{lang="EN-US"}]{#struct_0_14538_x1521_x585981698}

[[根据]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x601099616}[接口状态机确定的当前接口状态]{style="font-family:宋体"}[，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_14538_x1521_x1799484943}[表示在接口上没有发送和接收任何路由协议的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting]{lang="EN-US"}]{#struct_0_14538_x1521_x2122911305}[表示接口开始发送和接收]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，并试图去识别网络上的]{style="font-family:宋体"}[DR]{lang="EN-US"}[和]{style="font-family:宋体"}[BDR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P-2-P]{lang="EN-US"}]{#struct_0_14538_x1521_2092203591}[表示接口将每隔]{style="font-family:宋体"}[HelloInterval]{lang="EN-US"}[的时间间隔发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，并尝试和接口链路另一端相连的路由器建立邻接关系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DR]{lang="EN-US"}]{#struct_0_14538_x1521_1262743074}[表示路由器是所连网络的指定路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BDR]{lang="EN-US"}]{#struct_0_14538_x1521_x1679576765}[表示路由器是所连网络的备份指定路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DROther]{lang="EN-US"}]{#struct_0_14538_x1521_x601034080}[表示路由器既不是所连网络的指定路由器，也不是所连网络的备份指定路由器]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_14538_x1521_2138227425}

[[接口的网络类型，取值为：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1310567045}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PTP]{lang="EN-US"}]{#struct_0_14538_x1521_x1155434215}[表示网络类型为点对点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PTMP]{lang="EN-US"}]{#struct_0_14538_x1521_1862519974}[表示网络类型为点对多点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Broadcast]{lang="EN-US"}]{#struct_0_14538_x1521_x600968544}[表示网络类型为广播]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NBMA]{lang="EN-US"}]{#struct_0_14538_x1521_969774746}[表示网络类型为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}

[[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_2146626312}

[[接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_x1279493130}[的值]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_14538_x1521_x600903008}

[[接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_14538_x1521_592936235}[优先级]{style="font-family:宋体"}

[[Designated router]{lang="EN-US"}]{#struct_0_14538_x1521_848628794}

[[本链路上的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_14538_x1521_x1382748406}

[[Backup designated router]{lang="EN-US"}]{#struct_0_14538_x1521_590588956}

[[本链路上的]{style="font-family:宋体"}[BDR]{lang="EN-US"}]{#struct_0_14538_x1521_x601361760}

[[Timer interval configured]{lang="EN-US"}]{#struct_0_14538_x1521_x168794699}

[[配置的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_954594268}[定时器，分别定义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_14538_x1521_x296060536}[：接口发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dead]{lang="EN-US"}]{#struct_0_14538_x1521_x601296224}[：邻居的失效时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Poll]{lang="EN-US"}]{#struct_0_14538_x1521_x601230688}[：]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[网络上发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Retransmit]{lang="EN-US"}]{#struct_0_14538_x1521_x601165152}[：接口重传]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transmit ]{lang="EN-US"}]{#struct_0_14538_x1521_x1755957280}[d]{lang="EN-US"}[elay]{lang="EN-US"}[：接口对]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的传输延迟时间]{lang="EN-US" style="font-family:宋体"}

[[Neighbor count]{lang="EN-US"}]{#struct_0_14538_x1521_1153495835}

[[接口的邻居数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1276453497}

[[Adjacent neighbor count]{lang="EN-US"}]{#struct_0_14538_x1521_x600575328}

[[接口的邻接数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_1752578123}

[[IPsec profile name]{lang="EN-US"}]{#struct_0_14538_x1521_x1793603257}

[[IPsec]{lang="EN-US"}]{#struct_0_14538_x1521_x1947378090}[安全框架名]{style="font-family:宋体"}

[[Exchanging/Loading neighbors]{lang="EN-US"}]{#struct_0_14538_x1521_1677838451}

[[处于]{style="font-family:宋体"}[Exchanging]{lang="EN-US"}]{#struct_0_14538_x1521_x47870165}[或]{style="font-family:宋体"}[Loading]{lang="EN-US"}[状态的邻居个数]{style="font-family:宋体"}

[[Wait timer]{lang="EN-US"}]{#struct_0_14538_x1521_x601099615}

[[等待定时器，其中：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1799288335}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_14538_x1521_1385379339}[：]{style="font-family:宋体"} [关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_14538_x1521_x601034079}[：]{style="font-family:宋体"} [开启]{lang="EN-US" style="font-family:宋体"}

[[LsAck timer]{lang="EN-US"}]{#struct_0_14538_x1521_2137768680}

[[报文确认定时器，其中：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1058647371}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_14538_x1521_1620571275}[：]{style="font-family:宋体"} [关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_14538_x1521_x600968543}[：]{style="font-family:宋体"} [开启]{lang="EN-US" style="font-family:宋体"}

[[Prefix-suppression is enabled]{lang="EN-US"}]{#struct_0_14538_x1521_40292460}

[[接口处于前缀抑制]{style="font-family:宋体"}]{#struct_0_14538_x1521_40226924}

[ ]{lang="EN-US"}

::: {#1757904747 .myid}
[]{#_Toc404789053}[]{#struct_0_14538_x1521_969315994}[]{#_Toc245205324}[]{#_Toc138238094}[]{#_Toc93984836}[]{#_Toc81478702}[]{#_Toc58333177}[]{#_Toc58294827}[]{#_Toc33866051}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 lsdb**

------------------------------------------------------------------------

[**[display ospfv3 lsdb]{lang="EN-US"}**]{#struct_0_14538_x1521_1285840166}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_838170224}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **lsdb** \[ { **external** \| **grace** \| **inter-prefix** \| **inter-router** \| **intra-prefix** \| **link** \| **network** \| **nssa** \| **router** \| **unknown** \[ *type* \] } \[ *link-state-id* \] \[ **originate-router** *router-id* \| **self-originate** \] \| **statistics** \| **total** \| **verbose** \]]{lang="EN-US"}]{#struct_0_14538_x1521_1656661950}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1337610192}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x600903007}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_592215339}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_2035712151}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_617935284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_270401561}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_488660590}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_584559164}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_308455382}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的链路状态数据库信息。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_14538_x1521_x1723532612}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[AS External LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[grace]{lang="EN-US"}**]{#struct_0_14538_x1521_1355148006}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-11 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[inter-prefix]{lang="EN-US"}**]{#struct_0_14538_x1521_x601361759}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Inter-Area-Prefix LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[inter-router]{lang="EN-US"}**]{#struct_0_14538_x1521_x169384522}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-4 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Inter-Area-Router LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[intra-prefix]{lang="EN-US"}**]{#struct_0_14538_x1521_x211946671}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-9 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Intra-Area-Prefix LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[link]{lang="EN-US"}**]{#struct_0_14538_x1521_x2123449293}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-8 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Link LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**]{#struct_0_14538_x1521_1944408608}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-2 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Network LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[nssa]{lang="EN-US"}**]{#struct_0_14538_x1521_450226218}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[NSSA LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[router]{lang="EN-US"}**]{#struct_0_14538_x1521_412755450}[：显示链路状态数据库中]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[unknown]{lang="EN-US"}**]{#struct_0_14538_x1521_x601296223}[：显示链路状态数据库中未知类型]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[*[type]{lang="EN-US"}*]{#struct_0_14538_x1521_1338169843}[：]{style="font-family:宋体"}[LSA]{lang="EN-US"}[类型，取值范围十六进制]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[FFFF]{lang="EN-US"}[。如果未指定本参数，将显示所有未知类型]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[*[link-state-id]{lang="EN-US"}*]{#struct_0_14538_x1521_686048573}[：链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址形式。]{style="font-family:宋体"}

[**[originate-router]{lang="EN-US"}**[ *router-id*]{lang="EN-US"}]{#struct_0_14538_x1521_1074625741}[：发布该]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[self-originate]{lang="EN-US"}**]{#struct_0_14538_x1521_x1534553454}[：显示本地路由器自己产生的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_14538_x1521_212136203}[：显示链路状态数据库中]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[total]{lang="EN-US"}**]{#struct_0_14538_x1521_901779443}[：显示链路状态数据库中各种]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的总数。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_x406457029}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x601230687}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x569249609}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 lsdb]{lang="EN-US"}]{#struct_0_14538_x1521_x1998720924}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Link-LSA (Interface GigabitEthernet1/0/1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix]{lang="EN-US"}

[ 0.15.0.8        2.2.2.2          0691  0x80000041 0x8315      1]{lang="EN-US"}

[ 0.0.0.3         1.1.1.1          0623  0x80000001 0x0fee      1]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Router-LSA (Area 0.0.0.1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum    Link]{lang="EN-US"}

[ 0.0.0.0         1.1.1.1          0013  0x80000068 0x5d5f      2]{lang="EN-US"}

[ 0.0.0.0         2.2.2.2          0024  0x800000ea 0x1e22      0]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Network-LSA (Area 0.0.0.1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum]{lang="EN-US"}

[ 0.15.0.8        2.2.2.2          0019  0x80000007 0x599e]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Intra-Area-Prefix-LSA (Area 0.0.0.1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix  Reference]{lang="EN-US"}

[ 0.0.0.2         2.2.2.2          3600  0x80000002 0x2eed      2 Network-LSA]{lang="EN-US"}

[ 0.0.0.1         2.2.2.2          0018  0x80000001 0x1478      1 Network-LSA]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ospfv3 lsdb]{lang="EN-US"}]{#struct_0_14538_x1521_x584563713}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1178886183}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x601165151}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1755891744}

[[Link State ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1538763696}

[[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1328632828}

[[Origin Router]{lang="EN-US"}]{#struct_0_14538_x1521_1300578387}

[[产生]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1412876327}[的路由器]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_14538_x1521_x600575327}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1753036875}[老化时间]{style="font-family:宋体"}

[[SeqNum]{lang="EN-US"}]{#struct_0_14538_x1521_x125605515}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x888364088}[序列号]{style="font-family:宋体"}

[[CkSum]{lang="EN-US"}]{#struct_0_14538_x1521_1924863741}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1988063059}[校验和]{style="font-family:宋体"}

[[Prefix]{lang="EN-US"}]{#struct_0_14538_x1521_x1415791517}

[[前缀数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_x600509791}

[[Link]{lang="EN-US"}]{#struct_0_14538_x1521_x991950148}

[[链路数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_2038703750}

[[Reference]{lang="EN-US"}]{#struct_0_14538_x1521_1503165721}

[[引用的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1172673837}[类型]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x289572329}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[链路状态数据库中]{style="font-family:宋体"}[Link-LSA]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 lsdb link]{lang="EN-US"}]{#struct_0_14538_x1521_x601099614}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[                  Link-LSA ]{lang="SV"}[(Interface GigabitEthernet1/0/1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  LS age            : 833]{lang="EN-US"}

[  LS Type           : Link-LSA]{lang="EN-US"}

[  Link State ID     : 0.15.0.8]{lang="EN-US"}

[  Originating Router: 2.2.2.2]{lang="EN-US"}

[  LS Seq Number     : 0x80000041]{lang="EN-US"}

[  Checksum          : 0x8315]{lang="EN-US"}

[  Length            : 56]{lang="EN-US"}

[  Priority          : 1]{lang="EN-US"}

[  Options           : 0x000013 (-\|R\|-\|-\|E\|V6)]{lang="FR"}

[  Link-Local Address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[  Number of Prefixes: 1]{lang="EN-US"}

[      Prefix        : 1001::/64]{lang="EN-US"}

[      Prefix Options: 0 (-\|-\|-\|-)]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display ospfv3 lsdb link]{lang="EN-US"}]{#struct_0_14538_x1521_x1799353871}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1185071591}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_481009107}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x601034078}

[[LS age]{lang="EN-US"}]{#struct_0_14538_x1521_2137703144}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x2050720486}[老化时间]{style="font-family:宋体"}

[[LS Type]{lang="EN-US"}]{#struct_0_14538_x1521_2123634970}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1886431944}[类型]{style="font-family:宋体"}

[[Link State ID]{lang="EN-US"}]{#struct_0_14538_x1521_403905629}

[[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_1871517419}

[[Originating Router]{lang="EN-US"}]{#struct_0_14538_x1521_x600968542}

[[产生]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_969381530}[的路由器]{style="font-family:宋体"}

[[LS Seq Number]{lang="EN-US"}]{#struct_0_14538_x1521_811062541}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x618038210}[序列号]{style="font-family:宋体"}

[[Checksum]{lang="EN-US"}]{#struct_0_14538_x1521_1707898513}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1962526650}[校验和]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_14538_x1521_x600903006}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_592280875}[长度]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_14538_x1521_2041366087}

[[路由器优先级]{style="font-family:宋体"}]{#struct_0_14538_x1521_467303192}

[[Options]{lang="EN-US"}]{#struct_0_14538_x1521_x1763464342}

[[选项]{style="font-family:宋体"}]{#struct_0_14538_x1521_x601361758}

[[Link-Local Address]{lang="EN-US"}]{#struct_0_14538_x1521_x169318986}

[[链路本地]{style="font-family:宋体"}]{#struct_0_14538_x1521_x588284909}[地址]{style="font-family:宋体"}

[[Number of Prefixes]{lang="EN-US"}]{#struct_0_14538_x1521_494540467}

[[前缀的数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_x680305426}

[[Prefix]{lang="EN-US"}]{#struct_0_14538_x1521_x601296222}

[[地址前缀]{style="font-family:宋体"}]{#struct_0_14538_x1521_1338104307}

[[Prefix Options]{lang="EN-US"}]{#struct_0_14538_x1521_1156268688}

[[前缀选项]{style="font-family:宋体"}]{#struct_0_14538_x1521_x2009150941}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_262234691}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[链路状态数据库中]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<System\> display ospfv3 lsdb statistics]{lang="EN-US"}]{#struct_0_14538_x1521_x601165150}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Area ID         Router Network IntePre  InteRou IntraPre NSSA]{lang="EN-US"}

[ 0.0.0.1         2      0       0        0       2        0]{lang="EN-US"}

[ 0.0.0.3         1      0       0        0       1        1]{lang="EN-US"}

[ Total           2      0       0        0       3        1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[                 Link   Grace   ASE]{lang="EN-US"}

[ Total           4      0       0]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display ospfv3 lsdb statistics]{lang="EN-US"}]{#struct_0_14538_x1521_x1755826208}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1189088359}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x614550808}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x657403267}

[[Area ID]{lang="EN-US"}]{#struct_0_14538_x1521_1373738173}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x600575326}[，显示该区域各类]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的总数]{style="font-family:宋体"}

[[Router]{lang="EN-US"}]{#struct_0_14538_x1521_1752971339}

[[Type-1 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x202068145}[的数目]{style="font-family:宋体"}

[[Network]{lang="EN-US"}]{#struct_0_14538_x1521_x2025155246}

[[Type-2 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x655370673}[的数目]{style="font-family:宋体"}

[[IntePre]{lang="EN-US"}]{#struct_0_14538_x1521_x600509790}

[[Type-3 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x991884612}[的数目]{style="font-family:宋体"}

[[InteRou]{lang="EN-US"}]{#struct_0_14538_x1521_x601099613}

[[Type-4 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1799157263}[的数目]{style="font-family:宋体"}

[[IntraPre]{lang="EN-US"}]{#struct_0_14538_x1521_x150227821}

[[Type-9 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_831766952}[的数目]{style="font-family:宋体"}

[[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_x601034077}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x600968541}[的数目]{style="font-family:宋体"}

[[Link]{lang="EN-US"}]{#struct_0_14538_x1521_969447066}

[[Type-8 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x480545330}[的数目]{style="font-family:宋体"}[（只显示总数）]{style="font-family:宋体"}

[[Grace]{lang="EN-US"}]{#struct_0_14538_x1521_152800209}

[[Type-11 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x600903005}[的数目]{style="font-family:宋体"}

[[ASE]{lang="EN-US"}]{#struct_0_14538_x1521_592084267}

[[Type-5 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x531821913}[的数目]{style="font-family:宋体"}[（只显示总数）]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_14538_x1521_x1532465540}

[[不同区域相同类型]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x967863279}[的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x601361757}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的链路状态数据库的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 lsdb verbose]{lang="EN-US"}]{#struct_0_14538_x1521_x601296221}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Link-LSA (Interface GigabitEthernet1/0/1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix]{lang="EN-US"}

[ 0.15.0.8        2.2.2.2          0691  0x80000041 0x8315      1]{lang="EN-US"}

[                 SendCnt: 0       RxmtCnt: 0       Status: Stale]{lang="EN-US"}

[ 0.0.0.3         1.1.1.1          0623  0x80000001 0x0fee      1]{lang="EN-US"}

[                 SendCnt: 0       RxmtCnt: 0       Status: Stale]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Router-LSA (Area 0.0.0.1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum    Link]{lang="EN-US"}

[ 0.0.0.0         1.1.1.1          0013  0x80000068 0x5d5f      2]{lang="EN-US"}

[                 SendCnt: 0       RxmtCnt: 0       Status: Stale]{lang="EN-US"}

[ 0.0.0.0         2.2.2.2          0024  0x800000ea 0x1e22      0]{lang="EN-US"}

[                 SendCnt: 0       RxmtCnt: 0       Status: Stale]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Network-LSA (Area 0.0.0.1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum]{lang="EN-US"}

[ 0.15.0.8        2.2.2.2          0019  0x80000007 0x599e]{lang="EN-US"}

[                 SendCnt: 0       RxmtCnt: 0       Status: Stale]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Intra-Area-Prefix-LSA (Area 0.0.0.1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Link State ID   Origin Router    Age   SeqNum     CkSum  Prefix  Reference]{lang="EN-US"}

[ 0.0.0.2         2.2.2.2          3600  0x80000002 0x2eed      2 Network-LSA]{lang="EN-US"}

[                 SendCnt: 0       RxmtCnt: 0       Status: Stale]{lang="EN-US"}

[ 0.0.0.1         2.2.2.2          0018  0x80000001 0x1478      1 Network-LSA]{lang="EN-US"}

[                 SendCnt: 0       RxmtCnt: 0       Status: Stale]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display ospfv3 lsdb verbose]{lang="EN-US"}]{#struct_0_14538_x1521_1338300915}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1165041383}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_1098454335}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_395782806}

[[SendCnt]{lang="EN-US"}]{#struct_0_14538_x1521_x1864384519}

[[待发送该]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_839871348}[的接口数目]{style="font-family:宋体"}

[[RxmtCnt]{lang="EN-US"}]{#struct_0_14538_x1521_x300018598}

[[该]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x601230685}[在重传列表中的数目]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_14538_x1521_x569380681}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x108125958}[所处的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_14538_x1521_982530019}[：正常状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delayed]{lang="EN-US"}]{#struct_0_14538_x1521_x1348251116}[：]{lang="EN-US" style="font-family:宋体"}[延迟生成的]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Maxage routed]{lang="EN-US"}]{#struct_0_14538_x1521_x239100298}[：]{style="font-family:宋体"}[Maxage]{lang="EN-US"}[的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[且已经经过拓扑前缀处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Self originated]{lang="EN-US"}]{#struct_0_14538_x1521_x601165149}[：收到自己产生的]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stale]{lang="EN-US"}]{#struct_0_14538_x1521_x1756416031}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程中收到自己产生的]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1413730789 .myid}
[]{#_Toc245205327}[]{#_Toc138238096}[]{#_Toc93984837}[]{#_Toc81478703}[]{#_Toc58333179}[]{#_Toc58294829}[]{#_Toc33866053}[]{#_Toc404789054}[]{#struct_0_14538_x1521_1457511309}[]{#_Toc348020490}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 nexthop**

------------------------------------------------------------------------

[**[display ospfv3 nexthop]{lang="EN-US"}**]{#struct_0_14538_x1521_338341843}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的路由下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1183790439}

[**[display]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **nexthop**]{lang="EN-US"}]{#struct_0_14538_x1521_1763044347}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1382209989}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x852982532}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x600575325}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1752905803}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1829952738}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_293149678}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1975328736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x26898347}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x1322156171}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的下一跳信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_308625279}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_830375295}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[路由下一跳]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1120864938}**[ ]{lang="EN-US" style="font-size:8.5pt"}**[display ospfv3 1 nexthop]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1736269933}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[ Nexthop : FE80::20C:29FF:FED7:F308                Interface: GE1/0/2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x941144680}

[[ RefCount: 4                                       Status   : Valid]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1540046423}

[[ NbrID   : 1.1.1.1                                 NbrIntID : 21]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1120668330}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[ Nexthop : FE80::20C:29FF:FED7:F312                Interface: GE1/0/3]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1270667379}

[[ RefCount: 3                                       Status   : Valid]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1814201403}

[[ NbrID   : 1.1.1.1                                 NbrIntID : 38]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_958304730}

[[表1-12 ]{lang="EN-US"}[display ospfv3 nexthop]{lang="EN-US"}]{#struct_0_14538_x1521_2131288981}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1163490855}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_964984323}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1693913651}

[[Nexthop]{lang="EN-US"}]{#struct_0_14538_x1521_1823567280}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_14538_x1521_1892335274}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_x237652320}

[[出接口名]{style="font-family:宋体"}]{#struct_0_14538_x1521_351915017}

[[RefCount]{lang="EN-US"}]{#struct_0_14538_x1521_113376380}

[[下一跳引用计数]{style="font-family:宋体"}]{#struct_0_14538_x1521_965049859}

[[Status]{lang="EN-US"}]{#struct_0_14538_x1521_1677584133}

[[该下一跳的状态：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1034094288}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_14538_x1521_x1714994521}[：有效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_14538_x1521_x474399323}[：无效]{style="font-family:宋体"}

[[NbrID]{lang="EN-US"}]{#struct_0_14538_x1521_x986322771}

[[邻居路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_965115395}

[[NbrIntID]{lang="EN-US"}]{#struct_0_14538_x1521_1387586859}

[[邻居的接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_1624072194}

[ ]{lang="EN-US"}

::::: {#-2028541488 .myid}
[]{#_Toc404789055}[]{#struct_0_14538_x1521_x876837914}[]{#_Toc360624052}[]{#_Toc347491133}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 non-stop-routing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_x877427737}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x735819385}
:::

[ ]{lang="EN-US"}

[**[display ospfv3 non-stop-routing]{lang="EN-US"}**]{#struct_0_14538_x1521_1117590363}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x608500612}

[**[display ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **non-stop-routing**]{lang="EN-US"}]{#struct_0_14538_x1521_x719130303}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_339005977}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x877362201}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1531122860}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x860113895}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1471512203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1953373594}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_360171356}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1727879435}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x877296665}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_64208249}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1539657946}[显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 non-stop-routing]{lang="EN-US"}]{#struct_0_14538_x1521_1763030787}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 3.3.3.3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Nonstop Routing capability: Enabled]{lang="EN-US"}

[ Upgrade phase             : Normal]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display ospfv3 non-stop-routing]{lang="EN-US"}]{#struct_0_14538_x1521_1349669827}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1016762765}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x877231129}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_1224379712}

[[Nonstop Routing capability]{lang="EN-US"}]{#struct_0_14538_x1521_1069960567}

[[是否使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1971475111}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_14538_x1521_x877165593}[：]{lang="EN-US" style="font-family:宋体"}[使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14538_x1521_x1523097658}[：]{lang="EN-US" style="font-family:宋体"}[未使能]{style="font-family:宋体"}

[[Upgrade phase]{lang="EN-US"}]{#struct_0_14538_x1521_x579455916}

[[NSR]{lang="EN-US"}]{#struct_0_14538_x1521_391798864}[的各个阶段，有如下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_14538_x1521_1861197912}[：普通状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Preparation]{lang="EN-US"}]{#struct_0_14538_x1521_x877100057}[：准备阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Smooth]{lang="EN-US"}]{#struct_0_14538_x1521_1994392057}[：数据平滑阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Precalculation]{lang="EN-US"}]{#struct_0_14538_x1521_x1304137833}[：路由计算预处理阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Calculation]{lang="EN-US"}]{#struct_0_14538_x1521_779049282}[：路由计算阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redistribution]{lang="EN-US"}]{#struct_0_14538_x1521_x877034521}[：路由引入阶段]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1632291379 .myid}
[]{#_Toc404789056}[]{#struct_0_14538_x1521_x1503257330}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 peer**

------------------------------------------------------------------------

[**[display ospfv3 peer]{lang="EN-US"}**]{#struct_0_14538_x1521_x1818836203}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x475312937}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] \[ **area** *area-id* \] **peer** \[ \[ *interface-type interface-number* \] \[ **verbose** \] \| *peer-router-id* \| **statistics** \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1761154217}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x924179724}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_965180931}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_512521182}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1476237239}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1565490253}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x207269052}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x315160018}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1729352219}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x2043667145}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}***[ area-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x1268422878}[：显示位于指定区域的邻居信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[为区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其处理成]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式）或]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14538_x1521_1446219150}[：接口类型和接口编号。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_964722179}[：显示邻居的详细信息。]{style="font-family:宋体"}

[*[peer-router-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x706554301}[：显示指定邻居的信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_14538_x1521_358532014}[：显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[邻居的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_495611530}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1049638746}[OSPFv3]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的邻居信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定区域，将显示所有区域的邻居信息。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1287072638}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口参数、邻居]{style="font-family:宋体"}]{#struct_0_14538_x1521_1509454087}[Router ID]{lang="EN-US"}[参数都不输入，则显示所有接口的邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x822020647}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x450887568}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_964787715}

[[\<Sysname\> display ospfv3 1 peer gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14538_x1521_964853251}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Router ID       Pri State             Dead-Time InstID Interface]{lang="EN-US"}

[ 2.2.2.2         1   Full/DR           00:00:33  0      GE1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_277641251}

[[\<Sysname\> display ospfv3 1 peer vlan-interface 1]{lang="EN-US"}]{#struct_0_14538_x1521_965508611}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Router ID       Pri State             Dead-Time InstID Interface]{lang="EN-US"}

[ 2.2.2.2         1   Init/ -           00:00:36  0      Vlan1]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display ospfv3 peer]{lang="EN-US"}]{#struct_0_14538_x1521_x467302665}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1169362983}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x75101665}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_758789631}

[[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_965574147}

[[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x873476555}

[[Pri]{lang="EN-US"}]{#struct_0_14538_x1521_x926499292}

[[邻居路由器优先级]{style="font-family:宋体"}]{#struct_0_14538_x1521_x546825518}

[[State]{lang="EN-US"}]{#struct_0_14538_x1521_964984324}

[[邻居状态]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1693913650}

[[Dead-Time]{lang="EN-US"}]{#struct_0_14538_x1521_965049860}

[[邻居路由器的失效时间]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1043405044}

[[Inst ID]{lang="EN-US"}]{#struct_0_14538_x1521_1403636678}

[[实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_965115396}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_1387586862}

[[和邻居相连的接口]{style="font-family:宋体"}]{#struct_0_14538_x1521_965180932}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_512521183}[显示接口上的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的邻居详细信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_964722180}

[[\<Sysname\> display ospfv3 1 peer gigabitethernet 1/0/2 verbose]{lang="EN-US"}]{#struct_0_14538_x1521_13489722}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area 0.0.0.1 interface GE1/0/2\'s neighbors]{lang="EN-US"}

[ Router ID: 2.2.2.2          Address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[   State: Full  Mode: Nbr is master  Priority: 1]{lang="EN-US"}

[   DR: 2.2.2.2  BDR: None   MTU: 1500]{lang="EN-US"}

[   Options is 0x000013 (-\|R\|-\|x\|E\|V6)]{lang="EN-US"}

[   Dead timer due in 00:00:38]{lang="EN-US"}

[   Neighbor is up for 00:19:07]{lang="EN-US"}

[   Neighbor state change count: 120]{lang="EN-US"}

[   Database Summary List 0]{lang="EN-US"}

[   Link State Request List 0]{lang="EN-US"}

[   Link State Retransmission List 3]{lang="EN-US"}

[   Neighbor interface ID: 8037]{lang="EN-US"}

[   GR state: Normal]{lang="EN-US"}

[   Grace period: 0           Grace period timer: Off]{lang="EN-US"}

[   DD Rxmt timer: Off        LS Rxmt timer: On]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x1666888996}

[[\<Sysname\> display ospfv3 1 peer vlan-interface 1 verbose]{lang="EN-US"}]{#struct_0_14538_x1521_964787716}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area 0.0.0.1 interface Vlan1\'s neighbors]{lang="EN-US"}

[ Router ID: 2.2.2.2          Address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[   State: ExStart  Mode: None  Priority: 1]{lang="EN-US"}

[   DR: 2.2.2.2  BDR: None   MTU: 1500]{lang="EN-US"}

[   Options is 0x000013 (-\|R\|-\|x\|E\|V6)]{lang="EN-US"}

[   Dead timer due in 00:00:33]{lang="EN-US"}

[   Neighbor is up for 00:24:19]{lang="EN-US"}

[   Neighbor state change count: 205]{lang="EN-US"}

[   Database Summary List 0]{lang="EN-US"}

[   Link State Request List 0]{lang="EN-US"}

[   Link State Retransmission List 0]{lang="EN-US"}

[   Neighbor interface ID: 8037]{lang="EN-US"}

[   GR state: Normal]{lang="EN-US"}

[   Grace period: 0           Grace period timer: Off]{lang="EN-US"}

[   DD Rxmt timer: Off        LS Rxmt timer: On]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display ospfv3 peer verbose]{lang="EN-US"}]{#struct_0_14538_x1521_1257839460}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1144629511}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1496558516}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_263851889}

[[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_964853252}

[[邻居的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_277641254}

[[Address]{lang="EN-US"}]{#struct_0_14538_x1521_42734147}

[[接口链路本地地址]{style="font-family:宋体"}]{#struct_0_14538_x1521_925890327}

[[State]{lang="EN-US"}]{#struct_0_14538_x1521_1470359092}

[[邻居状态]{style="font-family:宋体"}]{#struct_0_14538_x1521_842668976}

[[Mode]{lang="EN-US"}]{#struct_0_14538_x1521_964918788}

[[路由器在数据库同步阶段，路由器与邻居协商的主从关系，取值为：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1396513471}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nbr is ]{lang="EN-US"}]{#struct_0_14538_x1521_630127156}[m]{lang="EN-US"}[aster]{lang="EN-US"}[：邻居路由器为主路由器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nbr is ]{lang="EN-US"}]{#struct_0_14538_x1521_x489391424}[slave]{lang="EN-US"}[：邻居路由器为从路由器]{lang="EN-US" style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_14538_x1521_1558886694}

[[邻居路由器优先级]{style="font-family:宋体"}]{#struct_0_14538_x1521_965508612}

[[DR]{lang="EN-US"}]{#struct_0_14538_x1521_x467302664}

[[接口所属网段的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_14538_x1521_x75036129}

[[BDR]{lang="EN-US"}]{#struct_0_14538_x1521_723484067}

[[接口所属网段的]{style="font-family:宋体"}[BDR]{lang="EN-US"}]{#struct_0_14538_x1521_1239547038}

[[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_x1380927834}

[[接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_965574148}[的值]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_14538_x1521_x873476556}

[[邻居的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x926695900}[选项，各选项含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DC]{lang="EN-US"}]{#struct_0_14538_x1521_807106885}[：支持按需链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_14538_x1521_x1206146627}[：是否为活跃路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_14538_x1521_x1921776470}[：是否支持]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[外部]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[x]{lang="EN-US"}]{#struct_0_14538_x1521_x355692529}[：保留]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_14538_x1521_x1598027373}[：]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[外部]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的接受能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V6]{lang="EN-US"}]{#struct_0_14538_x1521_1210391412}[：是否参与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[Dead timer due in 33  sec]{lang="EN-US"}]{#struct_0_14538_x1521_1493148617}

[[邻居将在]{style="font-family:宋体"}[33]{lang="EN-US"}]{#struct_0_14538_x1521_x181095497}[秒后被认为不可达]{style="font-family:宋体"}

[[Neighbor is up for 00:24:19]{lang="EN-US"}]{#struct_0_14538_x1521_964984325}

[[与邻居建立的时长]{style="font-family:宋体"}[00:24:19]{lang="EN-US"}]{#struct_0_14538_x1521_x1693913649}

[[Neighbor state change count]{lang="EN-US"}]{#struct_0_14538_x1521_1467402456}

[[邻居状态发生改变的次数]{style="font-family:宋体"}]{#struct_0_14538_x1521_307182713}

[[Database Summary List]{lang="EN-US"}]{#struct_0_14538_x1521_965049861}

[[需要]{style="font-family:宋体"}[DD]{lang="EN-US"}]{#struct_0_14538_x1521_x1043405043}[报文发送的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[Link State Request List]{lang="EN-US"}]{#struct_0_14538_x1521_x2131815731}

[[链路状态请求列表中]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x40415024}[个数]{style="font-family:宋体"}

[[Link State Retransmission List]{lang="EN-US"}]{#struct_0_14538_x1521_x670043941}

[[链路状态重传列表中]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_965115397}[个数]{style="font-family:宋体"}

[[Neighbor interface ID]{lang="EN-US"}]{#struct_0_14538_x1521_1387586861}

[[邻居的接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_1623547903}

[[GR state]{lang="EN-US"}]{#struct_0_14538_x1521_512521184}

[[GR]{lang="EN-US"}]{#struct_0_14538_x1521_1476237237}[状态，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_14538_x1521_1564572749}[：普通状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Doing GR]{lang="EN-US"}]{#struct_0_14538_x1521_964722181}[：正在作为]{lang="EN-US" style="font-family:宋体"}[GR ]{lang="EN-US"}[Restarter]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Complete GR]{lang="EN-US"}]{#struct_0_14538_x1521_13489723}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Helper]{lang="EN-US"}]{#struct_0_14538_x1521_671763164}[：]{lang="EN-US" style="font-family:宋体"}[正在作为]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}

[[Grace period]{lang="EN-US"}]{#struct_0_14538_x1521_2117300698}

[[发送]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}]{#struct_0_14538_x1521_964787717}[的间隔]{style="font-family:宋体"}

[[Grace period timer]{lang="EN-US"}]{#struct_0_14538_x1521_1257839461}

[[发送]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1496492980}[的间隔定时器]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_14538_x1521_964853253}[：]{style="font-family:宋体"} [关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_14538_x1521_277641253}[：开启]{style="font-family:宋体"}

[[DD Rxmt timer]{lang="EN-US"}]{#struct_0_14538_x1521_42734140}

[[DD]{lang="EN-US"}]{#struct_0_14538_x1521_x1412761833}[报文重传定时器]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_14538_x1521_964918789}[：]{style="font-family:宋体"} [关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_14538_x1521_1396513470}[：开启]{style="font-family:宋体"}

[[LS Rxmt timer]{lang="EN-US"}]{#struct_0_14538_x1521_630192692}

[[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_1468330048}[报文重传定时器]{style="font-family:宋体"}[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_14538_x1521_965508613}[：]{style="font-family:宋体"} [关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_14538_x1521_x467302663}[：开启]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x74970593}[显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[邻居的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 peer statistics]{lang="EN-US"}]{#struct_0_14538_x1521_965574149}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Area ID         Down Attempt Init 2-Way ExStart Exchange Loading Full Total]{lang="EN-US"}

[ 0.0.0.0         0    0       0    0     0       0        0       1    1]{lang="EN-US"}

[ Total           0    0       0    0     0       0        0       1    1]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display ospfv3 peer statistics]{lang="EN-US"}]{#struct_0_14538_x1521_x873476557}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1146130823}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x926630364}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_964984326}

[[Area ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1693913648}

[[区域标识]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1261480899}

[[Down]{lang="EN-US"}]{#struct_0_14538_x1521_x5884732}

[[该状态为]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x118165102}[建立邻居关系的初始化状态，表示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由器在一定时间之内没有收到从某一邻居路由器发送来的信息]{style="font-family:宋体"}

[[Attempt]{lang="EN-US"}]{#struct_0_14538_x1521_965049862}

[[该状态仅对]{style="font-family:宋体"}[NBMA]{lang="EN-US"}]{#struct_0_14538_x1521_965115398}[网络上的邻居有效，表示最近没有从邻居收到信息，但仍需作出进一步的尝试，用以与邻居联系]{style="font-family:宋体"}

[[Init]{lang="EN-US"}]{#struct_0_14538_x1521_1387586864}

[[此状态表示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1623744511}[路由器已经接收到邻居路由器发送来的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[数据包，但该]{style="font-family:宋体"}[Hello]{lang="EN-US"}[数据包内没有包含自己的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，还没有建立起双方的双向通信]{style="font-family:宋体"}

[[2-Way]{lang="EN-US"}]{#struct_0_14538_x1521_965180934}

[[此状态表示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_512521185}[路由器与邻居路由器的双向通信已经建立。]{style="font-family:宋体"}[DR]{lang="EN-US"}[及]{style="font-family:宋体"}[BDR]{lang="EN-US"}[的选择是在这个状态（或更高的状态）完成的]{style="font-family:宋体"}

[[ExStart]{lang="EN-US"}]{#struct_0_14538_x1521_1476237236}

[[在此状态，路由器要确定邻居双方的主从关系并决定初始的]{style="font-family:宋体"}[DD]{lang="EN-US"}]{#struct_0_14538_x1521_1564507213}[报文的序列号]{style="font-family:宋体"}

[[Exchange]{lang="EN-US"}]{#struct_0_14538_x1521_187794276}

[[在此状态，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x334029544}[路由器向其邻居路由器发送]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文来交换链路状态信息]{style="font-family:宋体"}

[[Loading]{lang="EN-US"}]{#struct_0_14538_x1521_964722182}

[[在此状态，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_13489720}[路由器向邻居路由器发送]{style="font-family:宋体"}[LSR]{lang="EN-US"}[报文，请求最新的链路状态信息]{style="font-family:宋体"}

[[Full]{lang="EN-US"}]{#struct_0_14538_x1521_x1284551972}

[[在此状态，建立起邻居关系的路由器之间已经完成了数据库同步的工作，它们的链路状态数据库已经一致]{style="font-family:宋体"}]{#struct_0_14538_x1521_x2113428139}

[[Total]{lang="EN-US"}]{#struct_0_14538_x1521_4567115}

[[所有区域中处于相同状态的邻居数目的总和]{style="font-family:宋体"}]{#struct_0_14538_x1521_964787718}

[ ]{lang="EN-US"}

::: {#76341947 .myid}
[]{#_Toc58333184}[]{#_Toc58294834}[]{#_Toc33866060}[]{#_Toc245205331}[]{#_Toc138238100}[]{#_Toc93984838}[]{#_Toc81478704}[]{#_Toc58333182}[]{#_Toc58294832}[]{#_Toc33866056}[]{#_Toc404789057}[]{#struct_0_14538_x1521_1257839446}[]{#_Toc322361669}[]{#_Toc320815916}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 request-queue**

------------------------------------------------------------------------

[**[display ospfv3 request-queue]{lang="EN-US"}**]{#struct_0_14538_x1521_x1496689590}[命令用来显示]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[请求列表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x526404036}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] \[ **area** *area-id* \] **request-queue** \[ *interface-type interface-number* \] \[ *neighbor-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1449275118}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1143740858}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x738188823}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1152284951}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_964853254}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_277641248}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1999049271}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x1220395201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1872954315}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_983456969}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}***[ area-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x492936490}[：显示位于指定区域的信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[为区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其处理成]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式）或]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14538_x1521_x608170039}[：接口类型和编号。]{style="font-family:宋体"}

[*[neighbor-id]{lang="EN-US"}*]{#struct_0_14538_x1521_438235359}[：邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_964918790}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定]{style="font-family:宋体"}]{#struct_0_14538_x1521_x942138697}[OSPFv3]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的请求列表信息。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定]{style="font-family:宋体"}]{#struct_0_14538_x1521_x576342628}[OSPFv3]{lang="EN-US"}[区域号，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域的请求列表信息。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定接口，将显示所有接口的请求列表信息。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1757418639}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定邻居路由器，将显示所有邻居路由器的请求列表信息。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1319225708}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x889052830}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_758930129}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[请求列表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 request-queue]{lang="EN-US"}]{#struct_0_14538_x1521_965508614}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[                   Area: 0.0.0.0]{lang="EN-US"}

[                   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[                   Nbr-ID 1.3.3.3 Request List]{lang="EN-US"}

[ Type    LinkState ID    AdvRouter       SeqNum       Age   CkSum]{lang="EN-US"}

[ 0x4005  0.0.34.127      1.3.3.3         0x80000001   0027  0x274d]{lang="EN-US"}

[ 0x4005  0.0.34.128      1.3.3.3         0x80000001   0027  0x2d45]{lang="EN-US"}

[ 0x4005  0.0.34.129      1.3.3.3         0x80000001   0027  0x333d]{lang="EN-US"}

[ 0x4005  0.0.34.130      1.3.3.3         0x80000001   0027  0x3935]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ospfv3 request-queue]{lang="EN-US"}]{#struct_0_14538_x1521_x467302662}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1156985927}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x74905057}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_1615007848}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_x1445037629}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x674059670}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_1617684518}

[[接口类型和序号]{style="font-family:宋体"}]{#struct_0_14538_x1521_965574150}

[[Nbr-ID]{lang="EN-US"}]{#struct_0_14538_x1521_1082838588}

[[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x807546470}

[[Request List]{lang="EN-US"}]{#struct_0_14538_x1521_1928911484}

[[请求列表信息]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1469143204}

[[Type]{lang="EN-US"}]{#struct_0_14538_x1521_x534233435}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_964984327}[类型]{style="font-family:宋体"}

[[LinkState ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1693913647}

[[链路状态标示符]{style="font-family:宋体"}]{#struct_0_14538_x1521_660833402}

[[AdvRouter]{lang="EN-US"}]{#struct_0_14538_x1521_x1538271185}

[[通告路由器]{style="font-family:宋体"}]{#struct_0_14538_x1521_x2126835247}

[[SeqNum]{lang="EN-US"}]{#struct_0_14538_x1521_965049863}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1043405041}[序列号]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_14538_x1521_1000352151}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_619789012}[老化时间]{style="font-family:宋体"}

[[CkSum]{lang="EN-US"}]{#struct_0_14538_x1521_x1965933518}

[[校验和]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1668827442}

[]{#_Toc322361670}[[ ]{lang="EN-US"}]{#_Toc320815917}

::: {#1795586797 .myid}
[]{#_Toc404789058}[]{#struct_0_14538_x1521_965115399}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 retrans-queue**

------------------------------------------------------------------------

[**[display ospfv3 retrans-queue]{lang="EN-US"}**]{#struct_0_14538_x1521_1387586863}[命令用来显示]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[重传列表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1623678975}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] \[ **area** *area-id* \] **retrans-queue** \[ *interface-type interface-number* \] \[ *neighbor-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_589748336}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1196692894}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1931660375}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1762453743}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x222711532}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x697010663}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_965180935}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_512521186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1476237235}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1564703821}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}***[ area-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1010282809}[：显示位于指定区域的信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[为区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其处理成]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式）或]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14538_x1521_x1950475215}[：接口类型和编号。]{style="font-family:宋体"}

[*[neighbor-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1623076465}[：邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x591574353}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定]{style="font-family:宋体"}]{#struct_0_14538_x1521_x317785996}[OSPFv3]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的重传列表信息。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定]{style="font-family:宋体"}]{#struct_0_14538_x1521_763834522}[OSPFv3]{lang="EN-US"}[区域号，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域的重传列表信息。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定接口，将显示所有接口的重传列表信息。]{style="font-family:宋体"}]{#struct_0_14538_x1521_964722183}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果未指定邻居路由器，将显示所有邻居路由器的重传列表信息。]{style="font-family:宋体"}]{#struct_0_14538_x1521_13489721}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1054100188}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1227414294}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[重传列表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 retrans-queue]{lang="EN-US"}]{#struct_0_14538_x1521_405843605}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[                   Area: 0.0.0.0]{lang="EN-US"}

[                   Interface GigabitEthernet1/0/1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[                   Nbr-ID 1.2.2.2 Retransmit List]{lang="EN-US"}

[ Type    LinkState ID    AdvRouter       SeqNum       Age   CkSum]{lang="EN-US"}

[ 0x2009  0.0.0.0         1.3.3.3         0x80000001   3600  0x49fb]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ospfv3 retrans-queue]{lang="EN-US"}]{#struct_0_14538_x1521_x1898425099}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1126590407}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_964787719}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_1257839447}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_x1496624054}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_53402079}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_x1473450864}

[[接口类型和序号]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1619104604}

[[Nbr-ID]{lang="EN-US"}]{#struct_0_14538_x1521_395877760}

[[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_964853255}

[[Retransmit List]{lang="EN-US"}]{#struct_0_14538_x1521_277641247}

[[重传列表信息]{style="font-family:宋体"}]{#struct_0_14538_x1521_1999049280}

[[Type]{lang="EN-US"}]{#struct_0_14538_x1521_x1220460750}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x587490196}[类型]{style="font-family:宋体"}

[[LinkState ID]{lang="EN-US"}]{#struct_0_14538_x1521_964918791}

[[链路状态标示符]{style="font-family:宋体"}]{#struct_0_14538_x1521_x942138698}

[[AdvRouter]{lang="EN-US"}]{#struct_0_14538_x1521_x575883876}

[[通告路由器]{style="font-family:宋体"}]{#struct_0_14538_x1521_1911388060}

[[SeqNum]{lang="EN-US"}]{#struct_0_14538_x1521_x2093241826}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1852602824}[序列号]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_14538_x1521_965508615}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x467302661}[老化时间]{style="font-family:宋体"}

[[CkSum]{lang="EN-US"}]{#struct_0_14538_x1521_x74839521}

[[校验和]{style="font-family:宋体"}]{#struct_0_14538_x1521_x313740486}

[ ]{lang="EN-US"}

::: {#-1464390174 .myid}
[]{#_Toc404789059}[]{#struct_0_14538_x1521_x2064002360}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 routing**

------------------------------------------------------------------------

[**[display ospfv3 routing]{lang="EN-US"}**]{#struct_0_14538_x1521_x1406987473}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_965574151}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **routing** \[ *ipv6-address* *prefix-length* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1082838587}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x806825574}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_317143274}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1073408445}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1780960000}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x73876370}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_849041232}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x475166566}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_964984328}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x1693913662}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的路由表信息。]{style="font-family:宋体"}

[*[ipv6-address prefix-length]{lang="EN-US"}*]{#struct_0_14538_x1521_257679947}[：显示指定]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2123428102}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1773436914}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 routing]{lang="EN-US"}]{#struct_0_14538_x1521_965115400}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 9.9.9.9]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ I  - Intra area route,  E1 - Type 1 external route,  N1 - Type 1 NSSA route]{lang="EN-US"}

[ IA - Inter area route,  E2 - Type 2 external route,  N2 - Type 2 NSSA route]{lang="EN-US"}

[ \*  - Selected route]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \*Destination: 3::3/128]{lang="EN-US"}

[  Type       : I                                         Cost     : 0]{lang="EN-US"}

[  Nexthop    : ::                                        Interface: Loop1]{lang="EN-US"}

[  AdvRouter  : 9.9.9.9                                   Area     : 0.0.0.0]{lang="EN-US"}

[  Preference : 10]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \*Destination: 4::4/128]{lang="EN-US"}

[  Type       : I                                         Cost     : 1]{lang="EN-US"}

[  Nexthop    : FE80::20C:29FF:FED4:7171                  Interface: GE1/0/2]{lang="EN-US"}

[  AdvRouter  : 8.8.8.8                                   Area     : 0.0.0.0]{lang="EN-US"}

[  Preference : 10]{lang="EN-US"}

[ ]{lang="EN-US"}

[ \*Destination: 6::/64]{lang="EN-US"}

[  Type       : I                                         Cost     : 1]{lang="EN-US"}

[  Nexthop    : ::                                        Interface: GE1/0/2]{lang="EN-US"}

[  AdvRouter  : 9.9.9.9                                   Area     : 0.0.0.0]{lang="EN-US"}

[  Preference : 10]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total: 3]{lang="EN-US"}

[ Intra area: 3         Inter area: 0         ASE: 0         NSSA: 0]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display ospfv3 routing]{lang="EN-US"}]{#struct_0_14538_x1521_x1768263539}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1125241735}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_1647010473}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_965180936}

[[Destination]{lang="EN-US"}]{#struct_0_14538_x1521_512521187}

[[目的网段]{style="font-family:宋体"}]{#struct_0_14538_x1521_1476237234}

[[Type]{lang="EN-US"}]{#struct_0_14538_x1521_1564638285}

[[路由类型]{style="font-family:宋体"}]{#struct_0_14538_x1521_x2093044039}

[[Cost]{lang="EN-US"}]{#struct_0_14538_x1521_x28400469}

[[路由开销值]{style="font-family:宋体"}]{#struct_0_14538_x1521_964722184}

[[Nexthop]{lang="EN-US"}]{#struct_0_14538_x1521_13489726}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_14538_x1521_1863404252}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_2097948079}

[[出接口]{style="font-family:宋体"}]{#struct_0_14538_x1521_240690692}

[[AdvRouter]{lang="EN-US"}]{#struct_0_14538_x1521_1941372756}

[[发布路由器]{style="font-family:宋体"}]{#struct_0_14538_x1521_964787720}

[[Area]{lang="EN-US"}]{#struct_0_14538_x1521_x1080812706}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1907945275}

[[Tag]{lang="EN-US"}]{#struct_0_14538_x1521_964853256}

[[外部路由标记]{style="font-family:宋体"}]{#struct_0_14538_x1521_964918792}

[[Preference]{lang="EN-US"}]{#struct_0_14538_x1521_x942138695}

[[路由优先级]{style="font-family:宋体"}]{#struct_0_14538_x1521_965508616}

[[Total]{lang="EN-US"}]{#struct_0_14538_x1521_x467302660}

[[路由总数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_x74773985}

[[Intra area]{lang="EN-US"}]{#struct_0_14538_x1521_149105382}

[[区域内路由数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1602094370}

[[Inter area]{lang="EN-US"}]{#struct_0_14538_x1521_965574152}

[[区域间路由数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_1082838586}

[[ASE]{lang="EN-US"}]{#struct_0_14538_x1521_x806891110}

[[5]{lang="EN-US"}]{#struct_0_14538_x1521_x1407668672}[类外部路由数目]{style="font-family:宋体"}

[[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407603136}

[[7]{lang="EN-US"}]{#struct_0_14538_x1521_x1407537600}[类外部路由数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1826513397 .myid}
[]{#_Toc245205332}[]{#_Toc138238101}[]{#_Toc404789060}[]{#struct_0_14538_x1521_1810881253}[]{#_Toc348020493}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 spf-tree**

------------------------------------------------------------------------

[**[display ospfv3 spf-tree]{lang="EN-US"}**]{#struct_0_14538_x1521_x1407472064}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域的拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x345773937}

[**[display]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] \[ **area** *area-id* \] **spf-tree** \[ **verbose** \]]{lang="EN-US"}]{#struct_0_14538_x1521_1848286425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_846170228}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_648107648}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1386200277}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x97851807}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1243372939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x943695162}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x1407930816}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_326145681}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1198262127}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的区域拓扑信息。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}***[ area-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1381396407}[：显示位于指定区域的信息。如果未指定本参数，将显示所有区域的拓扑信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[为区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其处理成]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式）或]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14538_x1521_x1407865280}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x602698686}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x749627773}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US" style="font-family:,\"serif\""}[下区域]{style="font-family:宋体"}[0]{lang="EN-US" style="font-family:,\"serif\""}[的最短路径树信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 1 area 0 spf-tree]{lang="EN-US"}]{#struct_0_14538_x1521_1247398539}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Flags: S-Node is on SPF tree       R-Node is directly reachable]{lang="EN-US"}

[        I-Node or Link is init      D-Node or Link is to be deleted]{lang="EN-US"}

[        P-Neighbor is parent        A-Node is in candidate list]{lang="EN-US"}

[        C-Neighbor is child         H-Nexthop changed]{lang="EN-US"}

[        N-Link is a new path        V-Link is involved]{lang="EN-US"}

[ ]{lang="EN-US"}

[                 Area: 0.0.0.0  Shortest Path Tree]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SPFNode         Type   Flag         SPFLink         Type   Cost  Flag]{lang="EN-US"}

[\>1.1.1.1         Router S R]{lang="EN-US"}

[                                  \--\>2.2.2.2         RT2RT  1     C]{lang="EN-US"}

[                                  \--\>2.2.2.2         RT2RT  1     P]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display ospfv3 spf-tree]{lang="EN-US"}]{#struct_0_14538_x1521_1863641300}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1140731719}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_156157989}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1407799744}

[[SPFNode]{lang="EN-US"}]{#struct_0_14538_x1521_1571776960}

[[SPF]{lang="EN-US"}]{#struct_0_14538_x1521_x172691391}[节点，以宣告路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[作为标识，其中，]{style="font-family:宋体"}[Type]{lang="EN-US"}[为节点类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Network]{lang="EN-US"}]{#struct_0_14538_x1521_x62091731}[：网络节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_14538_x1521_x2029548256}[：路由器节点]{lang="EN-US" style="font-family:宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_14538_x1521_x378111356}[为节点]{lang="EN-US" style="font-family:宋体"}[标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_14538_x1521_x1407734208}[：节点处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_14538_x1521_1325086225}[：节点在候选列表上]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_14538_x1521_x658158932}[：节点在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_14538_x1521_1102812894}[：该节点与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_14538_x1521_1109277107}[：该节点将被删除]{lang="EN-US" style="font-family:宋体"}

[[SPFLink]{lang="EN-US"}]{#struct_0_14538_x1521_x1322876419}

[[SPF]{lang="EN-US"}]{#struct_0_14538_x1521_x1407144384}[链路，以宣告路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[作为标识，其中，]{style="font-family:宋体"}[Type]{lang="EN-US"}[为链路类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT2RT]{lang="EN-US"}]{#struct_0_14538_x1521_1228130765}[：表示路由器到路由器链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NET2RT]{lang="EN-US"}]{#struct_0_14538_x1521_1624650691}[：表示网络到路由器链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT2NET]{lang="EN-US"}]{#struct_0_14538_x1521_x331402330}[：表示路由器到网络链路]{lang="EN-US" style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_14538_x1521_114150346}[为链路花费，]{style="font-family:宋体"}[Flag]{lang="EN-US"}[为链路标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_14538_x1521_x1407078848}[：链路处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_14538_x1521_x1146265637}[：目的节点是父节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_14538_x1521_1168762789}[：目的节点是子节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_14538_x1521_x2146091879}[：链路将要被删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_14538_x1521_x1096225630}[：下一跳发生改变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_14538_x1521_x1407668671}[：目的节点删除或者是新增节点时，链路的目的节点不在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上或处于删除状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_14538_x1521_1645746083}[：新增链路，并且源节点和目的节点都在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_14538_x1521_596543450}[：链路在区域变化列表中]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_969741752}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US" style="font-family:,\"serif\""}[下区域]{style="font-family:宋体"}[0]{lang="EN-US" style="font-family:,\"serif\""}[的最短路径树详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 1 area 0 spf-tree verbose]{lang="EN-US"}]{#struct_0_14538_x1521_x1407603135}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Flags: S-Node is on SPF tree       R-Node is directly reachable]{lang="EN-US"}

[        I-Node or Link is init      D-Node or Link is to be deleted]{lang="EN-US"}

[        P-Neighbor is parent        A-Node is in candidate list]{lang="EN-US"}

[        C-Neighbor is child         H-Nexthop changed]{lang="EN-US"}

[        N-Link is a new path        V-Link is involved]{lang="EN-US"}

[ ]{lang="EN-US"}

[           Area: 0.0.0.0  Shortest Path Tree]{lang="EN-US"}

[ ]{lang="EN-US"}

[\>SPFNode\[0\]]{lang="EN-US"}

[  AdvID        : 1.1.1.1                  LsID       : 0.0.0.0]{lang="EN-US"}

[  NodeType     : Router                   Distance   : 1]{lang="EN-US"}

[  NodeFlag     ]{lang="EN-US"}[: S R]{lang="EN-US"}

[  Nexthop count: 1]{lang="EN-US"}

[ \--\>NbrID      : 1.1.1.1                  NbrIntID   : 21]{lang="EN-US"}

[    Interface  : GE1/0/2                  NhFlag     : Valid]{lang="EN-US"}

[    Nexthop    : FE80::20C:29FF:FED7:F308]{lang="EN-US"}

[    RefCount   : 4]{lang="EN-US"}

[  SPFLink count: 1]{lang="EN-US"}

[ \--\>AdvID      : 1.1.1.1                  LsID       : 0.0.0.0]{lang="EN-US"}

[    IntID      : 232                      NbrIntID   : 465]{lang="EN-US"}

[    NbrID      : 2.2.2.2                  LinkType   : RT2RT]{lang="EN-US"}

[    LinkCost   : 1                        LinkNewCost: 1]{lang="EN-US"}

[    LinkFlag   : C]{lang="EN-US"}[                        NexthopCnt : 0]{lang="EN-US"}

[  ParentLink count: 1]{lang="EN-US"}

[ \--\>AdvID      : 1.1.1.1                  LsID       : 0.0.0.0]{lang="EN-US"}

[    IntID      : 215                      NbrIntID   : 466]{lang="EN-US"}

[    NbrID      : 2.2.2.2                  LinkType   : RT2RT]{lang="EN-US"}

[    LinkCost   : 1                        LinkNewCost: 1]{lang="EN-US"}

[    LinkFlag   : P                        NexthopCnt : 0]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display ospfv3 spf-tree verbose]{lang="EN-US"}]{#struct_0_14538_x1521_x2108089868}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1137392199}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_x780778822}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x531914702}

[[SPFNode]{lang="EN-US"}]{#struct_0_14538_x1521_x1407537599}

[[SPF]{lang="EN-US"}]{#struct_0_14538_x1521_x110974297}[节点]{style="font-family:宋体"}

[[AdvID]{lang="EN-US"}]{#struct_0_14538_x1521_x1814125193}

[[通告路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x560681101}

[[LsID]{lang="EN-US"}]{#struct_0_14538_x1521_x1138649568}

[[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1407472063}

[[NodeType]{lang="EN-US"}]{#struct_0_14538_x1521_1576540364}

[[节点类型]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1345440671}

[[Distance]{lang="EN-US"}]{#struct_0_14538_x1521_x1543501194}

[[到根节点的开销]{style="font-family:宋体"}]{#struct_0_14538_x1521_917280422}

[[NodeFlag]{lang="EN-US"}]{#struct_0_14538_x1521_x1620630011}

[[节点标志]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407930815}

[[Nexthop count]{lang="EN-US"}]{#struct_0_14538_x1521_1892229622}

[[下一跳计数]{style="font-family:宋体"}]{#struct_0_14538_x1521_604323706}

[[NbrID]{lang="EN-US"}]{#struct_0_14538_x1521_x823140598}

[[邻居路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x861601586}

[[NbrIntID]{lang="EN-US"}]{#struct_0_14538_x1521_x1407865279}

[[邻居的接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_1319287935}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_199064063}

[[出接口]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1849075608}

[[NhFlag]{lang="EN-US"}]{#struct_0_14538_x1521_2060853315}

[[下一跳标志：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407799743}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_14538_x1521_812262073}[：有效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_14538_x1521_1187728682}[：无效]{style="font-family:
  宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_14538_x1521_1887556145}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1381212159}

[[RefCount]{lang="EN-US"}]{#struct_0_14538_x1521_x1407734207}

[[下一跳的引用计数]{style="font-family:宋体"}]{#struct_0_14538_x1521_x691336410}

[[SPFLink count]{lang="EN-US"}]{#struct_0_14538_x1521_x226029800}

[[SPF]{lang="EN-US"}]{#struct_0_14538_x1521_1392908775}[链路计数]{style="font-family:宋体"}

[[IntID]{lang="EN-US"}]{#struct_0_14538_x1521_x1407144383}

[[接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_1987645652}

[[LinkType]{lang="EN-US"}]{#struct_0_14538_x1521_x807354830}

[[链路类型：]{style="font-family:宋体"}]{#struct_0_14538_x1521_1095025520}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT2RT]{lang="EN-US"}]{#struct_0_14538_x1521_x1407078847}[：表示路由器到路由器链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NET2RT]{lang="EN-US"}]{#struct_0_14538_x1521_63587944}[：表示网络到路由器链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RT2NET]{lang="EN-US"}]{#struct_0_14538_x1521_x1908719108}[：表示路由器到网络链路]{lang="EN-US" style="font-family:宋体"}

[[LinkCost]{lang="EN-US"}]{#struct_0_14538_x1521_226448070}

[[当前链路花费]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407668670}

[[LinkNewCost]{lang="EN-US"}]{#struct_0_14538_x1521_79662142}

[[新的链路花费]{style="font-family:宋体"}]{#struct_0_14538_x1521_1725175219}

[[LinkFlag]{lang="EN-US"}]{#struct_0_14538_x1521_621598190}

[[链路标志：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407603134}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_14538_x1521_620793487}[：链路处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_14538_x1521_462477689}[：目的节点是父节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_14538_x1521_x1407537598}[：目的节点是子节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_14538_x1521_1455109644}[：链路将要被删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_14538_x1521_2053427}[：下一跳发生改变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_14538_x1521_1979442362}[：目的节点删除或者是新增节点时，链路的目的节点不在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上或处于删除状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_14538_x1521_x1407472062}[：新增链路，并且源节点和目的节点都在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_14538_x1521_x1152342991}[：链路在区域变化列表中]{style="font-family:宋体"}

[[NexthopCnt]{lang="EN-US"}]{#struct_0_14538_x1521_x538917265}

[[下一跳个数]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407930814}

[[ParentLink count]{lang="EN-US"}]{#struct_0_14538_x1521_x836653733}

[[父链路计数]{style="font-family:宋体"}]{#struct_0_14538_x1521_x602515603}

[ ]{lang="EN-US"}

::: {#1434631863 .myid}
[]{#_Toc404789061}[]{#struct_0_14538_x1521_x330811319}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 statistics**

------------------------------------------------------------------------

[**[display ospfv3 statistics]{lang="EN-US"}**]{#struct_0_14538_x1521_x1407865278}[命令用来显示]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x246796006}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **statistics** \[ **error** \]]{lang="EN-US"}]{#struct_0_14538_x1521_337860047}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_192621772}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1019002757}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x939779086}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_574034683}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_1812297551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1553365509}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x1407799742}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1916621282}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x253558954}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_14538_x1521_1875154759}[：显示错误统计信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的报文、]{style="font-family:宋体"}[LSA]{lang="EN-US"}[和路由的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1436154023}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1482664331}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 statistics]{lang="EN-US"}]{#struct_0_14538_x1521_x1407668669}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[                   Packet Statistics]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Type                         Recv                Send]{lang="EN-US"}

[ Hello                        1746                1284]{lang="EN-US"}

[ ]{lang="EN-US"}[DB Description               505                 941]{lang="FR"}

[ Ls Req                       252                 136]{lang="FR"}

[ Ls Upd                       851                 1553]{lang="FR"}

[ ]{lang="FR"}[Ls Ack                       416                 450]{lang="EN-US"}

[ ]{lang="EN-US"}

[             Local Originated LSAs Statistics]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Type                                             Count]{lang="EN-US"}

[ Router-LSA                                       192]{lang="EN-US"}

[ Network-LSA                                      0]{lang="EN-US"}

[ ]{lang="EN-US"}[Inter-Are]{lang="PT-BR"}[a-Prefix-LSA                            0]{lang="EN-US"}

[ Inter-Area-Router-LSA                            0]{lang="EN-US"}

[ AS-external-LSA                                  0]{lang="EN-US"}

[ NSSA-LSA                                         0]{lang="EN-US"}

[ Link-LSA                                         10]{lang="EN-US"}

[ Intra-Area-Prefix-LSA                            112]{lang="EN-US"}

[ Grace-LSA                                        0]{lang="EN-US"}

[ Unknown-LSA                                      0]{lang="EN-US"}

[ Total                                            314]{lang="EN-US"}

[ ]{lang="EN-US"}

[                   Routes Statistics]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Type                                             Count]{lang="EN-US"}

[ Intra Area                                       0]{lang="EN-US"}

[ Inter Area                                       0]{lang="EN-US"}

[ ASE                                              0]{lang="EN-US"}

[ NSSA                                             0]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display ospfv3 statistics]{lang="EN-US"}]{#struct_0_14538_x1521_2001910907}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1114036615}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_663426592}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1407603133}

[[Packet Statistics]{lang="EN-US"}]{#struct_0_14538_x1521_1024078014}

[[收发报文统计]{style="font-family:宋体"}]{#struct_0_14538_x1521_48748727}

[[Hello]{lang="EN-US"}]{#struct_0_14538_x1521_x351662635}

[[Hello]{lang="EN-US"}]{#struct_0_14538_x1521_x915142254}[报文]{style="font-family:宋体"}

[[DB Description]{lang="EN-US"}]{#struct_0_14538_x1521_1576462561}

[[数据库描述报文]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407537597}

[[Ls Req]{lang="EN-US"}]{#struct_0_14538_x1521_x561312991}

[[链路状态请求报文]{style="font-family:宋体"}]{#struct_0_14538_x1521_479660591}

[[Ls Upd]{lang="EN-US"}]{#struct_0_14538_x1521_x414014913}

[[链路状态更新报文]{style="font-family:宋体"}]{#struct_0_14538_x1521_x153312220}

[[Ls Ack]{lang="EN-US"}]{#struct_0_14538_x1521_x1407472061}

[[链路状态确认报文]{style="font-family:宋体"}]{#struct_0_14538_x1521_413740950}

[[Local Originated LSAs Statistics]{lang="EN-US"}]{#struct_0_14538_x1521_669593817}

[[生成的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1512543993}[统计]{style="font-family:宋体"}

[[Router-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1752213175}

[[Type-1 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1735538812}[的数目]{style="font-family:宋体"}

[[Network-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407930813}

[[Type-2 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_729430208}[的数目]{style="font-family:宋体"}

[[Inter-Area-Prefix-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1755359848}

[[Type-3 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x889415683}[的数目]{style="font-family:宋体"}

[[Inter-Area-Router-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407865277}

[[Type-4 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_2125856989}[的数目]{style="font-family:宋体"}

[[AS-external-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x468370135}

[[Type-5 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_2064785638}[的数目]{style="font-family:宋体"}

[[NSSA-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407734205}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407144381}[的数目]{style="font-family:宋体"}

[[Link-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_824846238}

[[Type-8 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_934638525}[的数目]{style="font-family:宋体"}

[[Intra-Area-Prefix-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_105907245}

[[Type-9 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407078845}[的数目]{style="font-family:宋体"}

[[Grace]{lang="EN-US"}[-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1099211470}

[[Type-11 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1570557359}[的数目]{style="font-family:宋体"}

[[Unknown]{lang="EN-US"}[-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_2133818213}

[[Unknown-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407668668}[数目]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_14538_x1521_435826966}

[[总数目]{style="font-family:宋体"}]{#struct_0_14538_x1521_2019246227}

[[Routes Statistics]{lang="EN-US"}]{#struct_0_14538_x1521_185000342}

[[路由计数]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407603132}

[[Intra Area]{lang="EN-US"}]{#struct_0_14538_x1521_x542005927}

[[区域内路由]{style="font-family:宋体"}]{#struct_0_14538_x1521_x125324646}

[[Inter Area]{lang="EN-US"}]{#struct_0_14538_x1521_x1407537596}

[[区域间路由]{style="font-family:宋体"}]{#struct_0_14538_x1521_1004770950}

[[ASE]{lang="EN-US"}]{#struct_0_14538_x1521_x1407472060}

[[5]{lang="EN-US"}]{#struct_0_14538_x1521_x1407865276}[类外部路由]{style="font-family:宋体"}

[[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407799740}

[[7]{lang="EN-US"}]{#struct_0_14538_x1521_x1407734204}[类外部路由]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x288051883}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的错误统计信息。]{style="font-family:宋体"}

[[\<sysname\> display ospfv3 statistics error]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x790898069}

[ ]{lang="EN-US"}

[[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1966112306}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[ 0         : Transmit error               0         : Neighbor state low]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x790701461}

[[ 0         : Packet too small             0         : Bad version]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x818761298}

[[ 0         : Bad checksum                 0         : Unknown neighbor]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x467247570}

[[ 0         : Bad area ID                  0         : Bad packet]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x790766997}

[[ 0         : Packet dest error            0         : Inactive area packet]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_332271492}

[[ 0         : Router ID confusion          0         : Bad virtual link]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1860851987}

[[ 0         : HELLO: Hello-time mismatch   0         : HELLO: Dead-time mismatch]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x791094677}

[[ 0         : HELLO: Ebit option mismatch  0         : DD: Ebit option mismatch]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_1118042027}

[[ 0         : DD: Unknown LSA type         0         : DD: MTU option mismatch]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_778378225}

[[ 0         : REQ: Empty request           0         : REQ: Bad request]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_891581419}

[[ 0         : UPD: LSA checksum bad        0         : UPD: Unknown LSA type]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x791160213}

[[ 0         : UPD: Less recent LSA         0         : UPD: LSA length bad]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x473225824}

[[ 0         : UPD: LSA AdvRtr id bad       0         : ACK: Bad ack packet]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x1259380820}

[[ 0         : ACK: Invalid ack             0         : Interface down]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14538_x1521_x790963605}

[[ 0         : Multicast incapable]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_14538_x1521_1911539896}

[[表1-21 ]{lang="EN-US"}[display ospfv3 statistics error]{lang="EN-US"}]{#struct_0_14538_x1521_x1486487335}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1092666215}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_570627079}

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1207692496}

[[Transmit error]{lang="EN-US"}]{#struct_0_14538_x1521_x1496890307}

[[发送出错的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1298986306}[报文数]{style="font-family:宋体"}

[[Neighbor state low]{lang="EN-US"}]{#struct_0_14538_x1521_x1407603131}

[[在低邻居状态收到的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14538_x1521_x138721400}[OSPFv3]{lang="EN-US" style="font-size:9.0pt"}[报文数]{style="font-size:9.0pt;font-family:宋体"}

[[Packet too small]{lang="EN-US"}]{#struct_0_14538_x1521_x1821413861}

[[报文长度太小的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1857712774}[报文数]{style="font-family:宋体"}

[[Bad version]{lang="EN-US"}]{#struct_0_14538_x1521_1929264001}

[[错误版本号的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x686530122}[报文数]{style="font-family:宋体"}

[[Bad checksum]{lang="EN-US"}]{#struct_0_14538_x1521_x1407537595}

[[校验和出错的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1724112405}[报文数]{style="font-family:宋体"}

[[Unknown neighbor]{lang="EN-US"}]{#struct_0_14538_x1521_80105450}

[[未知的邻居发来的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x47492099}[报文数]{style="font-family:宋体"}

[[Bad area ID]{lang="EN-US"}]{#struct_0_14538_x1521_963445485}

[[非法的区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_1031233487}[的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[Bad packet]{lang="EN-US"}]{#struct_0_14538_x1521_x1407472059}

[[非法的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_770167918}[报文数]{style="font-family:宋体"}

[[Packet dest error]{lang="EN-US"}]{#struct_0_14538_x1521_328737448}

[[目的地址错误的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_714031363}[报文数]{style="font-family:宋体"}

[[Inactive area packet]{lang="EN-US"}]{#struct_0_14538_x1521_x1407930811}

[[非活动区域中接收到的报文数]{style="font-family:宋体"}]{#struct_0_14538_x1521_x433369206}

[[Router ID confusion]{lang="EN-US"}]{#struct_0_14538_x1521_x1507782033}

[[含有重复路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1080014310}[的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[Bad virtual link]{lang="EN-US"}]{#struct_0_14538_x1521_1865600107}

[[错]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1407865275}[误的虚链路的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[HELLO: Hello-time mismatch]{lang="EN-US"}]{#struct_0_14538_x1521_x1006310893}

[[Hello]{lang="EN-US"}]{#struct_0_14538_x1521_x403810051}[定时器不匹配的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[HELLO: Dead-time mismatch]{lang="EN-US"}]{#struct_0_14538_x1521_218886625}

[[Dead]{lang="EN-US"}]{#struct_0_14538_x1521_x1407799739}[定时器不匹配的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[HELLO: Ebit option mismatch]{lang="EN-US"}]{#struct_0_14538_x1521_x1963609913}

[[Option]{lang="EN-US"}]{#struct_0_14538_x1521_x1419559864}[字段]{style="font-family:宋体"}[E]{lang="EN-US"}[位不匹配的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[DD: Ebit option mismatch]{lang="EN-US"}]{#struct_0_14538_x1521_405469391}

[[Option]{lang="EN-US"}]{#struct_0_14538_x1521_1923724036}[字段]{style="font-family:宋体"}[E]{lang="EN-US"}[位不匹配的]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[DD: Unknown LSA type]{lang="EN-US"}]{#struct_0_14538_x1521_x1407734203}

[[DD]{lang="EN-US"}]{#struct_0_14538_x1521_1278032058}[报文中含有未知类型]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[DD: MTU option mismatch]{lang="EN-US"}]{#struct_0_14538_x1521_x1960174016}

[[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_69640970}[不匹配的]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[REQ: Empty request]{lang="EN-US"}]{#struct_0_14538_x1521_x1407144379}

[[不含有任何请求信息的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14538_x1521_1181928566}[LSR]{lang="EN-US" style="font-size:9.0pt"}[报文数]{style="font-size:9.0pt;font-family:宋体"}

[[REQ: Bad request]{lang="EN-US"}]{#struct_0_14538_x1521_x872361611}

[[请求错误]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1407078843}[的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[UPD: LSA checksum bad]{lang="EN-US"}]{#struct_0_14538_x1521_x1905780524}

[[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_1157698424}[报文中含有错误校验和]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[UPD: Unknown LSA type]{lang="EN-US"}]{#struct_0_14538_x1521_1139591589}

[[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_158415269}[报文中含有未知类型]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[UPD: Less recent LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1271959059}

[[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_1752570482}[报文中含有不是最新]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[UPD: LSA length bad]{lang="EN-US"}]{#struct_0_14538_x1521_x958126987}

[[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_158480805}[报文中含有错误长度]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[UPD: LSA AdvRtr id bad]{lang="EN-US"}]{#struct_0_14538_x1521_1689702806}

[[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_x162558502}[报文中含有错误宣告路由器]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[ACK: Bad ack packet]{lang="EN-US"}]{#struct_0_14538_x1521_158546341}

[[对]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_878707283}[报文错误确认的]{style="font-family:宋体"}[ack]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[ACK: Invalid ack]{lang="EN-US"}]{#struct_0_14538_x1521_x988567611}

[[LSAck]{lang="EN-US"}]{#struct_0_14538_x1521_2141299357}[报文中无效确认]{style="font-family:宋体"}[ack]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[Interface down]{lang="EN-US"}]{#struct_0_14538_x1521_158611877}

[[接口]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_14538_x1521_1146016383}[计数]{style="font-family:宋体"}

[[Multicast incapable]{lang="EN-US"}]{#struct_0_14538_x1521_x1290237908}

[[加入组播组出错计数]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14538_x1521_158153125}

[ ]{lang="EN-US"}

::: {#-55249222 .myid}
[]{#_Toc138238107}[]{#_Toc93984844}[]{#_Toc81478710}[]{#_Toc245205343}[]{#_Toc303674209}[]{#_Toc303084621}[]{#_Toc404789062}[]{#struct_0_14538_x1521_1112796004}[]{#_Toc322361672}[]{#_Toc264986086}[]{#_Toc264986087}[]{#_Toc264986088}[]{#_Toc264986089}[]{#_Toc264986090}[]{#_Toc264986091}[]{#_Toc264986092}[]{#_Toc264986093}[]{#_Toc264986094}[]{#_Toc264986095}[]{#_Toc264986096}[]{#_Toc264986097}[]{#_Toc264986098}[]{#_Toc264986099}[]{#_Toc264986100}[]{#_Toc264986101}

**OSPFv3 \-- OSPFv3配置命令 \-- display ospfv3 vlink**

------------------------------------------------------------------------

[**[display ospfv3 vlink]{lang="EN-US"}**]{#struct_0_14538_x1521_1955917306}[命令用来显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的虚连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2077101139}

[**[display ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **vlink**]{lang="EN-US"}]{#struct_0_14538_x1521_x2115228475}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1630681420}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_158218661}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1753653113}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1304645805}

[[network-operator]{lang="EN-US"}]{#struct_0_14538_x1521_x1123784017}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1417109602}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14538_x1521_629318998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1543184732}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x564235957}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的虚连接信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_214198181}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_158284197}[显示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的虚连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospfv3 vlink]{lang="EN-US"}]{#struct_0_14538_x1521_1030023947}

[ ]{lang="EN-US"}

[               OSPFv3 Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Virtual-link Neighbor-id: 12.2.2.2, Neighbor-state: Full]{lang="EN-US"}

[ Interface: 2348 (Vlan-interface12), Instance-ID: 0]{lang="EN-US"}

[ Local  IPv6 address: 3:3333::12]{lang="EN-US"}

[ Remote IPv6 address: 2:2222::12]{lang="EN-US"}

[ Cost: 1  State: P-2-P  Type: Virtual]{lang="EN-US"}

[ Transit area: 0.0.0.1]{lang="EN-US"}

[ Timers: Hello 10, Dead 40, Retransmit 5, Transmit Delay 1]{lang="EN-US"}

[ IPsec profile name: profile001]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ospfv3 vlink]{lang="EN-US"}]{#struct_0_14538_x1521_x284587590}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1102653959}[[字段]{style="font-family:黑体"}]{#struct_0_14538_x1521_789357221}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14538_x1521_x987802289}

[[Virtual-link Neighbor-ID]{lang="EN-US"}]{#struct_0_14538_x1521_158349733}

[[通过虚连接相连的邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_x581577535}

[[Neighbor-state]{lang="EN-US"}]{#struct_0_14538_x1521_x1202281828}

[[邻居状态，包括]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_14538_x1521_1572226975}[、]{style="font-family:宋体"}[Init]{lang="EN-US"}[、]{style="font-family:宋体"}[2-Way]{lang="EN-US"}[、]{style="font-family:宋体"}[ExStart]{lang="EN-US"}[、]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[、]{style="font-family:宋体"}[Loading]{lang="EN-US"}[和]{style="font-family:宋体"}[Full]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_14538_x1521_x308547347}

[[此虚连接的本端接口的端口号和名称]{style="font-family:宋体"}]{#struct_0_14538_x1521_158415270}

[[Instance-ID]{lang="EN-US"}]{#struct_0_14538_x1521_x684356068}

[[实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_x1009963560}

[[Local IPv6 address]{lang="EN-US"}]{#struct_0_14538_x1521_x552685845}

[[本地]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_14538_x1521_1948691399}[地址]{style="font-family:宋体"}

[[Remote IPv6 address]{lang="EN-US"}]{#struct_0_14538_x1521_985970742}

[[对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_14538_x1521_158480806}[地址]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_14538_x1521_1689702807}

[[接口的路由开销]{style="font-family:宋体"}]{#struct_0_14538_x1521_x162624038}

[[State]{lang="EN-US"}]{#struct_0_14538_x1521_994964463}

[[接口状态]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1352429875}

[[Type]{lang="EN-US"}]{#struct_0_14538_x1521_158546342}

[[类型：虚连接]{style="font-family:宋体"}]{#struct_0_14538_x1521_878707284}

[[Transit area]{lang="EN-US"}]{#struct_0_14538_x1521_x988567608}

[[传输区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14538_x1521_2141758108}[（如果当前接口为虚连接，则显示）]{style="font-family:宋体"}

[[Timers]{lang="EN-US"}]{#struct_0_14538_x1521_158611878}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1146016370}[定时器，分别定义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_14538_x1521_x1290303431}[：接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dead]{lang="EN-US"}]{#struct_0_14538_x1521_x573098042}[：邻居的失效时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Retransmit]{lang="EN-US"}]{#struct_0_14538_x1521_90397886}[：接口重传]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[时间间隔]{lang="EN-US" style="font-family:宋体"}[，单位为秒]{style="font-family:宋体"}

[[Transmit Delay]{lang="EN-US"}]{#struct_0_14538_x1521_158153126}

[[接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1112796007}[的传输延迟时间，单位为秒]{style="font-family:宋体"}

[[IPsec profile name]{lang="EN-US"}]{#struct_0_14538_x1521_1955982842}

[[IPsec]{lang="EN-US"}]{#struct_0_14538_x1521_x875873608}[安全框架名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1009486692 .myid}
[]{#_Toc322361674}[]{#_Toc404789063}[]{#struct_0_14538_x1521_1302427550}

**OSPFv3 \-- OSPFv3配置命令 \-- enable ipsec-profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_158218662}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_x1753653110}
:::

[ ]{lang="EN-US"}

[**[enable ipsec-profile]{lang="EN-US"}**]{#struct_0_14538_x1521_1707930332}[命令用来在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[**[undo enable ipsec-profile]{lang="EN-US"}**]{#struct_0_14538_x1521_1967334083}[命令用来取消在]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[区域应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1482611117}

[**[enable ipsec-profile]{lang="EN-US"}**[ *profile-name*]{lang="EN-US"}]{#struct_0_14538_x1521_x665040920}

[**[undo enable ipsec-profile]{lang="EN-US"}**]{#struct_0_14538_x1521_x65462175}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158284198}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1030023948}[区域没有应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x285439558}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x308931408}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1837472158}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1450106872}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x481802632}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_962026553}

[*[profile-name]{lang="EN-US"}*]{#struct_0_14538_x1521_731116503}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158349734}

[[本命令应结合]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_14538_x1521_x581577542}[安全框架使用，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的具体情况请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPsec]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1202609505}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x934386277}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[区域]{style="font-family:宋体"}[0]{lang="EN-US"}[的安全框架为]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysnam]{lang="EN-US"}]{#struct_0_14538_x1521_x230229757}[e\> system-view]{lang="NO-BOK"}

[\[Sysname\] ospfv3 1]{lang="NO-BOK"}

[\[Sysname-ospfv3-1\] area 0]{lang="NO-BOK"}

[\[Sysname-ospfv3-1-area-0.0.0.0\] enable ipsec-profile profile001]{lang="NO-BOK"}
:::::

::: {#646144833 .myid}
[]{#_Toc404789064}[]{#struct_0_14538_x1521_x843181527}

**OSPFv3 \-- OSPFv3配置命令 \-- filter (OSPFv3 area view)**

------------------------------------------------------------------------

[**[filter]{lang="EN-US"}**]{#struct_0_14538_x1521_1609401700}[命令用来配置对]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[**[undo filter]{lang="EN-US"}**]{#struct_0_14538_x1521_1219663872}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158939558}

[**[filter]{lang="EN-US"}**[ { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } { **export** \| **import** }]{lang="EN-US"}]{#struct_0_14538_x1521_1332526739}

[**[undo]{lang="EN-US"}**[ **filter** { **export** \| **import** }]{lang="EN-US"}]{#struct_0_14538_x1521_1181231937}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1441918028}

[[没有配置对]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x257890427}[进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_854651663}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1146265978}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_691201608}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_159005094}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x664840016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1276042808}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_14538_x1521_x642341094}[：指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本或高级访问控制列表，对进出本区域的]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[进行过滤，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_14538_x1521_1467254174}[：指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表，对进出本区域的]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[进行过滤，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[route-policy-name]{lang="EN-US"}*]{#struct_0_14538_x1521_x97245573}[：指定的路由策略，对进出本区域的]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[进行过滤，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_14538_x1521_2010341457}[：对]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向其它区域发布的]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_14538_x1521_1550812001}[：对]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向本区域发布的]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1470612782}

[[此命令只在]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_158415271}[路由器上有效，对区域内部路由器无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x684356069}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1009898024}[根据]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[my-prefix-list]{lang="EN-US"}[和编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[分别对进出]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x73516257}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] area 1]{lang="NO-BOK"}

[\[Sysname-ospfv3-1-area-0.0.0.1\] ]{lang="NO-BOK"}[filter prefix-list my-prefix-list import]{lang="EN-US"}

[\[Sysname-ospfv3-1-area-0.0.0.1\] ]{lang="NO-BOK"}[filter 2000 export]{lang="EN-US"}
:::

::: {#-254037253 .myid}
[]{#_Toc404789065}[]{#struct_0_14538_x1521_730450754}[]{#_Toc322361675}

**OSPFv3 \-- OSPFv3配置命令 \-- filter-policy export (OSPFv3 View)**

------------------------------------------------------------------------

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_14538_x1521_x1960482922}[命令用来配置对引入的路由信息进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy export]{lang="EN-US"}**]{#struct_0_14538_x1521_1229090934}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158480807}

[**[filter-policy]{lang="FR"}**]{#struct_0_14538_x1521_1689702808}[ { *acl6-number* \| **prefix-list** *prefix-list-name* } **export** \[ *protocol* \[ *process-id* \] \]]{lang="FR"}

[**[undo filter-policy export]{lang="FR"}**[ \[ ]{lang="EN-US"}]{#struct_0_14538_x1521_x161903142}*[protocol]{lang="FR"}*[ \[ ]{lang="EN-US"}*[process-id]{lang="FR"}*[ \] \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_734691190}

[[没有对引入的路由信息进行过滤。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1421369388}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_550121585}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1031841237}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_279643393}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_386068187}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_158546343}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_878707285}

[*[acl6-number]{lang="FR"}*]{#struct_0_14538_x1521_x988567609}[：用于过滤路由信息目的地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本或高级访问控制列表编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[prefix-list-name]{lang="FR"}*]{#struct_0_14538_x1521_2141823644}[：]{style="font-family:宋体"}[用于过滤路由信息目的地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[protocol]{lang="FR"}*]{#struct_0_14538_x1521_651936182}[：]{style="font-family:宋体"}[路由协议名称，指定何种路由协议的路由信息将被过滤。目前可包括：]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}[、]{style="font-family:宋体"}[direct]{lang="EN-US"}[、]{style="font-family:宋体"}[isisv6]{lang="EN-US"}[、]{style="font-family:宋体"}[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。如果没有指定]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[参数，对引入的任何一个协议产生的路由都要进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[process-id]{lang="FR"}*]{#struct_0_14538_x1521_1258975843}[：]{style="font-family:宋体"}[路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[为]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[时，支持该参数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2078745369}

[[当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_14538_x1521_1434321762}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour-addr sour-prefix*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour-addr sour-prefix* **destination** *dest-addr dest-prefix*]{lang="EN-US"}[来过滤指定目的地址和掩码的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。]{style="font-family:宋体"}

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_14538_x1521_158611879}[命令只对本设备使用]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**[引入的路由起作用。如果没有配置]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**[命令来引入其它外部路由（包括不同进程的[OSPFv3]{lang="EN-US"}路由），则]{style="font-family:宋体"}**[filter-policy export]{lang="EN-US"}**[命令无效]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1146016369}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1290893254}[根据]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[abc]{lang="EN-US"}[对引入的路由信息进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_326130182}

[\[Sysname\] ipv6 prefix-list abc permit 2002:1:: 64]{lang="EN-US"}

[\[Sysname\] ospfv3]{lang="EN-US"}

[\[Sysname-ospfv3-1\] filter-policy prefix-list abc export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_445235074}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对引入的路由进行过滤，只允许]{style="font-family:宋体"}[2001::1/128]{lang="EN-US"}[通过]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_2140147691}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 100 deny ipv6]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ospfv3]{lang="EN-US"}

[\[Sysname-ospfv3-1\] filter-policy 3000 export]{lang="EN-US"}
:::

::: {#304084253 .myid}
[]{#_Toc404789066}[]{#struct_0_14538_x1521_1059975156}[]{#_Toc322361676}

**OSPFv3 \-- OSPFv3配置命令 \-- filter-policy import (OSPFv3 View)**

------------------------------------------------------------------------

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_14538_x1521_158153127}[命令]{style="font-family:宋体"}[用来过滤通过接收到的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[计算出来的路由信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_14538_x1521_1112796006}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1956048378}

[**[filter-policy]{lang="FR"}**]{#struct_0_14538_x1521_58051054}[ { *acl6-number* \[ **gateway** *prefix-list-name* \] \| **prefix-list** *prefix-list-name* \[ **gateway** *prefix-list-name* \] \| **gateway** *prefix-list-name* \| **route-policy** *route-policy-name* } **import**]{lang="FR"}

[**[undo filter-policy import]{lang="FR"}**]{#struct_0_14538_x1521_1911052977}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1087642612}

[[不对通过接收到的]{style="font-family:宋体"}]{#struct_0_14538_x1521_1277529593}[LSA]{lang="FR"}[计算出来的路由信息进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x533193990}

[[OSPFv3]{lang="FR"}]{#struct_0_14538_x1521_158218663}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1753653111}

[[network-admin]{lang="FR"}]{#struct_0_14538_x1521_141846391}

[[mdc-admin]{lang="FR"}]{#struct_0_14538_x1521_1851958991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2040674101}

[*[acl6-number]{lang="FR"}*]{#struct_0_14538_x1521_500060410}[：]{style="font-family:宋体"}[用]{style="font-family:宋体"}[于过滤路由信息目的地址的]{style="font-family:宋体"}[IPv6]{lang="FR"}[基本或高级访问控制列表编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="FR"}[～]{style="font-family:宋体"}[3999]{lang="FR"}[。]{style="font-family:
宋体"}

[**[gateway ]{lang="FR"}**]{#struct_0_14538_x1521_x179313128}*[prefix-list-name]{lang="FR"}*[：]{style="font-family:宋体"}[指定的]{style="font-family:宋体"}[IPv6]{lang="FR"}[地址前缀列表]{style="font-family:宋体"}[，]{style="font-family:宋体"}[基于要加入到路由表的路由信息的下一跳进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则不会基于要加入到路由表的路由信息的下一跳进行过滤。]{style="font-family:宋体"}

[**[prefix-list]{lang="FR"}**]{#struct_0_14538_x1521_x2024442181}[ *prefix-list-name*]{lang="FR"}[：指定的地址前缀列表，基于目的地址对接收的路由信息进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="FR"}**]{#struct_0_14538_x1521_658393571}[ *route-policy-name*]{lang="FR"}[：]{style="font-family:宋体"}[指定路由策略名，基于路由策略对接收的路由信息进行过滤。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158284199}

[[当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_14538_x1521_1030023949}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）或者指定的路由策略中配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-prefix*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-prefix* **destination** *dest-addr dest-prefix*]{lang="EN-US"}[来过滤指定目的地址和前缀的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。]{style="font-family:宋体"}

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_14538_x1521_x285505094}[命令只对]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[计算出来的路由进行过滤，没有通过过滤的路由将不被加入路由表中，从而不能指导报文转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x349598757}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1663977972}[根据]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[abc]{lang="EN-US"}[对接收的路由信息进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x778624769}

[\[Sysname\] ipv6 prefix-list abc permit 2002:1:: 64]{lang="EN-US"}

[\[Sysname\] ospfv3]{lang="EN-US"}

[\[Sysname-ospfv3-1\] filter-policy prefix-list abc import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x106506962}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由进行过滤，只允许]{style="font-family:宋体"}[2001::1/128]{lang="EN-US"}[通过]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_158349735}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 100 deny ipv6]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ospfv3]{lang="EN-US"}

[\[Sysname-ospfv3-1\] filter-policy 3000 import]{lang="EN-US"}
:::

::::: {#-235989138 .myid}
[]{#_Toc404789067}[]{#struct_0_14538_x1521_x581577541}

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_x1202543969}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_1497939183}
:::

[ ]{lang="EN-US"}

[**[graceful-restart enable]{lang="EN-US"}**]{#struct_0_14538_x1521_x815579621}[命令用来使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart enable]{lang="EN-US"}**]{#struct_0_14538_x1521_1343423161}[命令用来关闭]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1187656011}

[**[graceful-restart enable ]{lang="EN-US"}**[\[ **global** \| **planned-only** \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_158939559}

[**[undo graceful-restart enable]{lang="EN-US"}**]{#struct_0_14538_x1521_1332526738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1181166401}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1318100855}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x170918537}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_913464843}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1911084886}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1653090423}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1259625871}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1203091873}

[**[global]{lang="EN-US"}**]{#struct_0_14538_x1521_1543739530}[：全局]{style="font-family:宋体"}[GR]{lang="EN-US"}[，必须保证所有的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[都存在，整个]{style="font-family:宋体"}[GR]{lang="EN-US"}[才会完成，如果有一个]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[失效（比如，接口]{style="font-family:宋体"}[down]{lang="EN-US"}[），则整个]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败。如果未指定本参数，表示支持接口级]{style="font-family:宋体"}[GR]{lang="EN-US"}[，即只要有一个]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[存在，则整个]{style="font-family:宋体"}[GR]{lang="EN-US"}[会完成。]{style="font-family:宋体"}

[**[planned-only]{lang="EN-US"}**]{#struct_0_14538_x1521_1203026337}[：表示只支持计划重启。如果未指定本参数，表示计划重启和非计划重启都支持。计划重启指的是手动通过命令执行重启或主备倒换，在进行重启或主备倒换前]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[会先发送]{style="font-family:宋体"}[Grace-LSA]{lang="EN-US"}[；非计划]{style="font-family:宋体"}[GR]{lang="EN-US"}[指的是由于设备故障等原因进行重启或主备倒换，在进行重启或主备倒换前]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[不会事先发送]{style="font-family:宋体"}[Grace-LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_159005095}

[**[graceful-restart enable]{lang="EN-US"}**]{#struct_0_14538_x1521_689246027}[和]{style="font-family:宋体"}**[non-stop-routing]{lang="SV"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[支持]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x664840015}[的]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[能力的设备主备倒换后，为了实现设备转发业务的不中断，它必须完成下列两项任务：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重启过程]{lang="EN-US" style="font-family:宋体"}[GR Restarter]{lang="EN-US"}]{#struct_0_14538_x1521_x1276239416}[转发表项保持稳定；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重启流程结束后重建所有邻居关系，重新获取完整的网络拓扑信息；]{style="font-family:宋体"}]{#struct_0_14538_x1521_825313809}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1462494104}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1059904076}[使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1103341583}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] graceful-restart enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_565072419}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_14538_x1521_158415272}
:::::

::::: {#939141431 .myid}
[]{#_Toc404789068}[]{#struct_0_14538_x1521_x684356066}[]{#_Toc303674210}[]{#_Toc303084622}

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart helper enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_x1009308200}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_688103158}
:::

[ ]{lang="EN-US"}

[**[graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_14538_x1521_x1380200816}[命令用来使能]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_14538_x1521_1468362906}[命令用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_464076069}

[**[graceful-restart helper enable ]{lang="EN-US"}**[\[ **planned-only** \]]{lang="EN-US"}]{#struct_0_14538_x1521_1619472176}

[**[undo graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_14538_x1521_158480808}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1689702809}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x161968678}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力处于开启状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1561625396}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_517334109}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1987137660}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x395778234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_9142643}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1203354018}

[**[planned-only]{lang="EN-US"}**]{#struct_0_14538_x1521_x1615923590}[：表示只支持计划重启。如果未指定本参数，表示计划重启和非计划重启（即异常重启）都支持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x271466396}

[[收到]{style="font-family:宋体"}[Grace-LSA]{lang="EN-US"}]{#struct_0_14538_x1521_158546344}[后，如果支持]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力则进入]{style="font-family:宋体"}[Helper]{lang="EN-US"}[模式（此时该邻居称为]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[）。在]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[重新建立邻居的时候，]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[帮助]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[的同步]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_878707278}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1708611636}[使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1535499213}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] graceful-restart helper enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x711310124}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart enable]{lang="EN-US"}**]{#struct_0_14538_x1521_x1440230823}
:::::

::::: {#-914000413 .myid}
[]{#_Toc404789069}[]{#struct_0_14538_x1521_1251227561}[]{#_Toc303674211}[]{#_Toc303084623}

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart helper strict-lsa-checking**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_108721432}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_158611880}
:::

[ ]{lang="EN-US"}

[**[graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_14538_x1521_425972346}[命令用来使能]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力。]{style="font-family:宋体"}

[**[undo graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_14538_x1521_1876341412}[命令]{style="font-family:宋体"}[用来关闭]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x760561520}

[**[graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_14538_x1521_x2041801279}

[**[undo graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_14538_x1521_1951125067}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_508288493}

[[GR Helper]{lang="EN-US"}]{#struct_0_14538_x1521_1096038259}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158153128}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1112796017}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1955982843}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x875808072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1370185256}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1243508034}

[[使能]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_14538_x1521_x1883579780}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力，当检查到]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[设备的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[发生变化时候，]{style="font-family:宋体"}[Helper]{lang="EN-US"}[设备退出]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x336758094}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_158218664}[使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1753653108}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] graceful-restart helper strict-lsa-checking]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2064095156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_14538_x1521_x2073129385}
:::::

::::: {#16863910 .myid}
[]{#_Toc404789070}[]{#struct_0_14538_x1521_x1291344631}[]{#_Toc303674212}[]{#_Toc303084624}[]{#_Toc197336393}

**OSPFv3 \-- OSPFv3配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_661002297}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_x22020502}
:::

[ ]{lang="EN-US"}

[**[graceful-restart interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_14538_x1521_x570383645}[命令用来配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间。]{style="font-family:宋体"}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_14538_x1521_158284200}[命令]{style="font-family:
宋体"}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_624004403}

[**[graceful-restart interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_14538_x1521_704730088}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_14538_x1521_2003446263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1277952289}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_2126519582}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1653031149}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_46706809}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_304882861}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_158349736}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x581577540}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1202478433}

[*[interval-value]{lang="EN-US"}*]{#struct_0_14538_x1521_216749773}[：指定]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间，取值范围为]{style="font-family:宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1600817137}

[[配置此命令的用户需要确保配置的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_14538_x1521_x1929477136}[重启间隔不小于]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[所有接口的邻居失效时间的最大值，否则可能造成]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_552356821}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x287520745}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_158939560}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] graceful-restart interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x241451365}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospfv3 timer dead]{lang="EN-US"}**]{#struct_0_14538_x1521_292849135}
:::::

::: {#-1658574843 .myid}
[]{#_Toc404789071}[]{#struct_0_14538_x1521_1267833979}[]{#_Toc309373520}

**OSPFv3 \-- OSPFv3配置命令 \-- import-route (OSPFv3 view)**

------------------------------------------------------------------------

[**[import-route]{lang="EN-US"}**]{#struct_0_14538_x1521_x1158565734}[命令用来配置引入外部路由信息。]{style="font-family:宋体"}

[**[undo import-route]{lang="EN-US"}**]{#struct_0_14538_x1521_356712108}[命令用来取消引入外部路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1865236531}

[**[import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \| **all-processes** \| **allow-ibgp** \] \[ **allow-direct** \| **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_158415273}

[**[undo import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \| **all-processes** \]]{lang="EN-US"}]{#struct_0_14538_x1521_158480809}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1689702810}

[[没有引入外部路由信息。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x162427431}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x172404350}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_721147118}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_621901336}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1247185357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x2000165397}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2119402135}

[*[protocol]{lang="EN-US"}*]{#struct_0_14538_x1521_158546345}[：指定引入的路由协议，可以是]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[或]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_878707279}[：路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[时该参数可选。]{style="font-family:宋体"}

[**[all-processes]{lang="EN-US"}**]{#struct_0_14538_x1521_x1708611637}[：引入指定路由协议所有进程的路由，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[或]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[时可以指定该参数。]{style="font-family:宋体"}

[**[allow-ibgp]{lang="EN-US"}**]{#struct_0_14538_x1521_x1193384142}[：允许引入]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}**[时该参数可选。]{style="font-family:宋体"}

[**[allow-direct]{lang="EN-US"}**]{#struct_0_14538_x1521_158611881}[：]{style="font-family:宋体"}[在引入的路由中包含使能了该协议的接口网段路由。]{style="font-family:宋体"}[如果未指定本参数]{style="font-family:
宋体"}[，在引入]{style="font-family:宋体"}[协议]{style="font-family:宋体"}[路由时不会包含使能了]{style="font-family:宋体"}[该]{style="font-family:宋体"}[协议的接口网段路由。当]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[与]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}[参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[配置失效。例如，当配置]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数引入]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[直连时，在路由策略中不要配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[ **route-type**]{lang="EN-US"}[匹配条件，否则，]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数失效。]{style="font-family:宋体"}

[**[cost ]{lang="EN-US"}***[cost]{lang="EN-US"}*]{#struct_0_14538_x1521_425972345}[：路由开销值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nssa-only]{lang="EN-US"}**]{#struct_0_14538_x1521_1876341413}[：设置]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位，即在对端路由器上不能转为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位被置位，即在对端路由器上可以转为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[（如果本地路由器是]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，则会检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，当]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居存在时，产生的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位）。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_14538_x1521_158153129}[：]{style="font-family:宋体"}[配置只能引入符合指定路由策略的路由。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_14538_x1521_1112796016}[：外部]{style="font-family:宋体"}[LSA]{lang="EN-US"}[中的标记，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，将根据]{style="font-family:宋体"}**[default tag]{lang="EN-US"}**[命令的配置进行取值。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ *type*]{lang="EN-US"}]{#struct_0_14538_x1521_1956048379}[：度量值类型，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_58116590}

[[外部路由是指到达自治系统外部的路由，有两类：]{style="font-family:宋体"}]{#struct_0_14538_x1521_158218665}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[第一类外部路由（]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1753653109}[Type1 External]{lang="EN-US"}[）：这类路由的可信程度较高，并且和]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[自身路由的开销具有可比性，所以到第一类外部路由的开销等于本路由器到相应的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销与]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[到该路由目的地址的开销之和。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[第二类外部路由（]{style="font-family:宋体"}]{#struct_0_14538_x1521_498011215}[Type2 External]{lang="EN-US"}[）：这类路由的可信度比较低，所以]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议认为从]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[到自治系统之外的开销远远大于在自治系统之内到达]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销。所以计算路由开销时将主要考虑前者，即到第二类外部路由的开销等于]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[到该路由目的地址的开销。如果计算出开销值相等的两条路由，再考虑本路由器到相应的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14538_x1521_x823691053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令不能引入缺省路由。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x822774216}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route bgp4+]{lang="EN-US"}**]{#struct_0_14538_x1521_x2012729584}[表示只引入]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[；]{lang="EN-US" style="font-family:
宋体"}**[import-route bgp4+ allow-ibgp]{lang="EN-US"}**[表示将]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由也引入]{lang="EN-US" style="font-family:宋体"}[，容易引起路由环路，]{lang="EN-US" style="font-family:宋体"}[请慎用]{lang="EN-US" style="font-family:
宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route ]{lang="EN-US"}**]{#struct_0_14538_x1521_158284201}**[nssa-only]{lang="EN-US"}**[命令配置后，引入的路由只在]{style="font-family:宋体"}[NSSA]{lang="FR"}[区域产生]{style="font-family:宋体"}[Type-7 LSA]{lang="FR"}[，不会在非]{style="font-family:宋体"}[NSSA]{lang="FR"}[区域产生]{style="font-family:宋体"}[Type-5 LSA]{lang="FR"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_624004404}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_704730081}[指定引入进程号为]{style="font-family:宋体"}[10]{lang="EN-US"}[的]{style="font-family:宋体"}[RIPn]{lang="FR"}[g]{lang="EN-US"}[路由为]{style="font-family:宋体"}[第二]{style="font-family:宋体"}[类路由，路由开销值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_14538_x1521_2003446256}[-vi]{lang="FR"}[ew]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysna]{lang="FR"}[me\] ospfv3]{lang="EN-US"}

[\[S]{lang="FR"}[ysname-ospfv3-1\] import-route ripng 10 type 2 cost 50]{lang="EN-US"}

[[\# OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1277755680}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[引入]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[160]{lang="EN-US"}[发现的路由]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_158349737}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] import-route ospfv3 160]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x581577539}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-route-advertise]{lang="EN-US"}**]{#struct_0_14538_x1521_x1203068260}**[ ]{lang="EN-US"}**[(OSPFv3 view)]{lang="EN-US"}
:::

::: {#-1110888516 .myid}
[]{#_Toc404789072}[]{#struct_0_14538_x1521_245800180}

**OSPFv3 \-- OSPFv3配置命令 \-- log-peer-change**

------------------------------------------------------------------------

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_14538_x1521_107127797}[命令用来打开邻居状态变化的输出开关。]{style="font-family:宋体"}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_14538_x1521_1868069969}[命令]{style="font-family:宋体"}[用来关闭邻居状态变化的输出开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1856298091}

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_14538_x1521_2093072096}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_14538_x1521_x1108647185}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158939561}

[[邻居状态变化的输出开关处于打开状态。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x241451366}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_292652527}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1054329266}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2029496977}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1011664525}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_751490893}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1961202012}

[[打开邻居状态输出开关后，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_159005097}[邻居状态变化]{style="font-family:宋体"}[时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定]{style="font-family:宋体"}[日志信息]{style="font-family:宋体"}[的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x664840013}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1276370488}[关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的邻居状态变化的输出开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1513678279}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] undo log-peer-change]{lang="EN-US"}
:::

::: {#125214695 .myid}
[]{#_Toc245205345}[]{#_Toc138238108}[]{#_Toc93984845}[]{#_Toc81478711}[]{#_Toc404789073}[]{#struct_0_14538_x1521_1294969269}[]{#_Toc303674214}[]{#_Toc303084618}

**OSPFv3 \-- OSPFv3配置命令 \-- lsa-generation-interval**

------------------------------------------------------------------------

[**[lsa-generation-interval]{lang="EN-US"}**]{#struct_0_14538_x1521_234241557}[命令用来配置]{style="font-family:宋体"}[OSPFv3 LSA]{lang="EN-US"}[重新生成的时间间隔。]{style="font-family:宋体"}

[**[undo lsa-generation-interval]{lang="EN-US"}**]{#struct_0_14538_x1521_777116167}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1225172679}

[**[lsa-generation-interval ]{lang="EN-US"}***[maximum-interval ]{lang="EN-US"}*[\[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1642914566}

[**[undo lsa-generation-interval]{lang="EN-US"}**]{#struct_0_14538_x1521_158415274}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x684356064}

[[OSPFv3 LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1009177128}[重新生成的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[0]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[0]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1942603566}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x500012659}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_938542916}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1292606377}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_633502823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158480810}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_x266612335}[：]{style="font-family:宋体"}[OSPFv3 LSA]{lang="EN-US"}[重新生成的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_x1144714567}[：]{style="font-family:宋体"}[OSPFv3 LSA]{lang="EN-US"}[重新生成的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[毫秒时表示不对]{style="font-family:宋体"}[OSPFv3 LSA]{lang="EN-US"}[重新生成的最小时间间隔进行限制。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_x1253611483}[：]{style="font-family:宋体"}[OSPFv3 LSA]{lang="EN-US"}[重新生成的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x806173475}

[[通过调节]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x1215595457}[重新生成的时间间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。在网络变化不频繁的情况下，将]{style="font-family:宋体"}[LSA]{lang="EN-US"}[重新生成时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*[，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_1725544606}[和]{style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1333042992}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1317306070}[设置]{style="font-family:宋体"}[LSA]{lang="EN-US"}[重新生成的最大时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_158546346}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] lsa-generation-interval 2 100 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_878707280}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lsa-arrival-interval]{lang="EN-US"}**]{#struct_0_14538_x1521_x988567612}
:::

::::: {#1589792029 .myid}
[]{#_Toc404789074}[]{#struct_0_14538_x1521_2141364893}[]{#_Toc309373523}

**OSPFv3 \-- OSPFv3配置命令 \-- maximum load-balancing (OSPFv3 view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image003.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_x99982259}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_1525169530}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[maximum load-balancing]{lang="EN-US"}**]{#struct_0_14538_x1521_1520651572}[命令用来配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[支持的等价路由的最大条数。]{style="font-family:宋体"}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_14538_x1521_x1312708557}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158611882}

[**[maximum load-balancing]{lang="EN-US"}**[ *maximum*]{lang="EN-US"}]{#struct_0_14538_x1521_425972348}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_14538_x1521_1876341402}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x760561521}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1653799766}[支持的等价路由的最大条数与]{style="font-family:宋体"}[系统支持最大等价路由的条数相同。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2091850401}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x973518044}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_895049100}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_2063911323}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_158153130}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1225856151}

[*[maximum]{lang="EN-US"}*]{#struct_0_14538_x1521_1097085077}[：等价路由的最大条数，当]{style="font-family:宋体"}*[maximum]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，相当于不进行负载分担。不同型号的设备支持的取值范围与缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_184596099}

[[如果通过]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_14538_x1521_1122058936}[命令配置系统支持最大等价路由的条数为]{style="font-family:宋体"}[m]{lang="EN-US"}[，则本命令的缺省值为]{style="font-family:宋体"}[m]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[m]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_14538_x1521_x538054519}[命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_380623033}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x819651801}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[支持的]{style="font-family:宋体"}[等价路由的最大条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> syste]{lang="EN-US"}]{#struct_0_14538_x1521_158218666}[m-view]{lang="NO-BOK"}

[\[Sysname\] ospfv3 100]{lang="NO-BOK"}

[\[Sysname-ospfv3-100\] ma]{lang="NO-BOK"}[ximum load-balancing 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1753653106}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_14538_x1521_901295742}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{style="font-family:宋体"}
:::::

::::: {#-1554088180 .myid}
[]{#_Toc347491152}[]{#_Toc404789075}[]{#struct_0_14538_x1521_285568280}[]{#_Toc360624072}

**OSPFv3 \-- OSPFv3配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_x662818916}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14538_x1521_285633816}
:::

**[ ]{lang="EN-US"}**

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_14538_x1521_x106447677}[命令用来使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_14538_x1521_782847800}[命令用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1417657934}

[**[non-stop-routing]{lang="SV"}**]{#struct_0_14538_x1521_x308643461}

[**[undo non-stop-routing]{lang="SV"}**]{#struct_0_14538_x1521_285699352}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_726907252}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1295572102}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[能力处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x457645382}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_285764888}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x138232414}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_2064173862}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1490330805}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_285830424}

[**[non-stop-routing]{lang="SV"}**]{#struct_0_14538_x1521_x614054531}[和]{style="font-family:宋体"}**[graceful-restart enable]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2006492199}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1414999728}[使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_285895960}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] non-stop-routing]{lang="EN-US"}
:::::

::: {#1852618108 .myid}
[]{#_Toc404789076}[]{#struct_0_14538_x1521_x1314088785}[]{#_Toc346635708}

**OSPFv3 \-- OSPFv3配置命令 \-- nssa (OSPFv3 area view)**

------------------------------------------------------------------------

[**[nssa]{lang="EN-US"}**]{#struct_0_14538_x1521_158284202}[命令用来配置一个区域为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[undo nssa]{lang="EN-US"}**]{#struct_0_14538_x1521_158349738}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_158939562}

[**[nssa ]{lang="SV"}**[\[ **default-route-advertise**]{lang="EN-US"}[ \[ **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* \] \* \| **no-import-route** \| **no-summary** \| \[ **translate-always** \| **translate-never** \] \| **suppress-fa** \| **translator-stability-interval** *value* \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_x241451367}

[**[undo nssa]{lang="SV"}**]{#struct_0_14538_x1521_159005098}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724499210}

[[没有区域被配置为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_1724564746}[区域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x554475316}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1724630282}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724695818}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1724237066}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_625590152}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724302602}

[**[default-route-advertise]{lang="EN-US"}**]{#struct_0_14538_x1521_1724368138}[：该参数只用于]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[，配置后，对于]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，不论本地是否存在缺省路由，都将生成一条]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[向区域内发布缺省路由；对于]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[，只有当本地存在缺省路由时，才产生]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[向区域内发布缺省路由。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_14538_x1521_1724433674}[：该缺省路由的度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。如果未指定本参数，缺省路由的度量值将取]{style="font-family:宋体"}**[default-cost]{lang="EN-US"}**[命令配置的值。]{style="font-family:宋体"}

[**[nssa-only]{lang="EN-US"}**]{#struct_0_14538_x1521_x961572565}[：]{style="font-family:宋体"}[设置]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位，即在对端路由器上不能转为]{style="font-family:
宋体"}[Type-5 LSA]{lang="EN-US"}[，对端路由器不能引入]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[产生的外部路由]{style="font-family:宋体"}[。如果未指定本参数，]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位被置位，即在对端路由器上可以转为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[，对端路由器可以引入]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[产生的外部路由]{style="font-family:宋体"}[（如果本地路由器是]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，则会检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，当]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居存在时，产生的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位）。]{style="font-family:
宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_14538_x1521_1725023498}[：路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。只有]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[指定的路由策略匹配时，才可以产生一个描述缺省路由的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[发布出去，指定的路由策略会影响]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中的属性。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_14538_x1521_1725089034}[：缺省路由的标识，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ *type*]{lang="EN-US"}]{#struct_0_14538_x1521_1724499211}[：该]{style="font-family:宋体"}[NSSA LSA]{lang="EN-US"}[的类型，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[，缺省类型为]{style="font-family:
宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-import-route]{lang="EN-US"}**]{#struct_0_14538_x1521_1724564747}[：该参数用于禁止将]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由以]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的形式引入到]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域中，这个参数通常只用在既是]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，也是]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[自治系统的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的路由器上，以保证所有外部路由信息能正确地进入]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由域。]{style="font-family:宋体"}

[**[no-summary]{lang="EN-US"}**]{#struct_0_14538_x1521_x554409780}[：该参数只用于]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，配置后，]{style="font-family:宋体"}[NSSA ABR]{lang="EN-US"}[只通过]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[向区域内发布一条缺省路由，不再向区域内发布任何其它]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[（这种区域又称为]{style="font-family:宋体"}[Totally NSSA]{lang="EN-US"}[区域）。]{style="font-family:宋体"}

[**[translate-always]{lang="EN-US"}**]{#struct_0_14538_x1521_1724630283}[：指定]{style="font-family:宋体"}[ABR]{lang="EN-US"}[为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换路由器。]{style="font-family:宋体"}

[**[translate-never]{lang="EN-US"}**]{#struct_0_14538_x1521_1724695819}[：指定]{style="font-family:宋体"}[ABR]{lang="EN-US"}[不能将]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[suppress-fa]{lang="EN-US"}**]{#struct_0_14538_x1521_x2045913651}[：指定当]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[时，生成的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[不携带]{style="font-family:宋体"}[Forwarding Address]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[translator-stability-interval]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_14538_x1521_1724237067}[：当有新的设备成为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换路由器后，原]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换路由器保持转换能力的时间。]{style="font-family:宋体"}*[value]{lang="EN-US"}*[为保持时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[900]{lang="EN-US"}[，单位为秒。缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，即不保持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724302603}

[[如果要将一个区域配置成]{style="font-family:宋体"}[NSSA]{lang="EN-US"}]{#struct_0_14538_x1521_1724368139}[区域，则该区域中的所有路由器都必须配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1744951511}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1724433675}[将区域]{style="font-family:宋体"}[1]{lang="EN-US"}[配置成]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1725023499}

[\[Sysname\] ospfv3 120]{lang="EN-US"}

[\[Sysname-ospfv3-120\] area 1]{lang="EN-US"}

[\[Sysname-ospfv3-120-area-0.0.0.1\] nssa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1725089035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-cost ]{lang="EN-US"}**[(OSPFv3 area view)]{lang="EN-US"}]{#struct_0_14538_x1521_1724499212}
:::

::: {#-261559909 .myid}
[]{#_Toc404789077}[]{#struct_0_14538_x1521_1783385295}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3**

------------------------------------------------------------------------

[**[ospfv3]{lang="EN-US"}**]{#struct_0_14538_x1521_x1478115694}[命令用来启动]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程，并进入]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo ospfv3]{lang="EN-US"}**]{#struct_0_14538_x1521_x1155976637}[命令用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1760855388}

[**[ospfv3 ]{lang="SV"}**]{#struct_0_14538_x1521_1660458801}[\[ *process-id* ]{lang="SV"}[\| **vpn-instance** *vpn-instance-name* ]{lang="EN-US"}[\] \*]{lang="SV"}

[**[undo ospfv3 ]{lang="SV"}**]{#struct_0_14538_x1521_595439215}[\[ *process-id* \]]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2085737729}

[[系统没有运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1132713647}[进程。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724564748}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x554606388}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1297402064}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x310519040}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1973026113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1161232054}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_342834503}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_14538_x1521_696962347}[：指定]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x81816851}

[[只有在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1724630284}[视图下配置了]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程才能正常运行，否则只能看到该进程，但无法生成]{style="font-family:宋体"}[LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1322962011}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1939806695}[启动进程号为]{style="font-family:宋体"}[120]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程并配置路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1402481380}

[\[Sysname\] ospfv3 120]{lang="EN-US"}

[\[Sysname-ospfv3-120\] router-id 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_568170505}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[router-id]{lang="EN-US"}**]{#struct_0_14538_x1521_x1174032866}
:::

::: {#-1681318261 .myid}
[]{#_Toc138238109}[]{#_Toc93984847}[]{#_Toc81478713}[]{#_Toc58333193}[]{#_Toc58294841}[]{#_Toc33866065}[]{#_Toc404789078}[]{#struct_0_14538_x1521_1355301226}[]{#_Toc245205346}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 area**

------------------------------------------------------------------------

[**[ospfv3 area]{lang="EN-US"}**]{#struct_0_14538_x1521_x1185238885}[命令用来在接口上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议，并指定所属区域。]{style="font-family:宋体"}

[**[undo ospfv3 area]{lang="EN-US"}**]{#struct_0_14538_x1521_1724695820}[命令用来在接口上关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2045323830}

[**[ospfv3 ]{lang="EN-US"}***[process-id]{lang="EN-US"}*[ **area** *area-id* \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_598380166}

[**[undo ospfv3 ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ area]{lang="EN-US"}**[ *area-id* \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x2129340001}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2114503654}

[[接口上没有使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1694160072}[协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x862037870}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x234205030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_109484775}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1724237068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_625721224}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_92347928}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_237956987}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[area-id]{lang="EN-US"}*]{#struct_0_14538_x1521_189861687}[：区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其处理成]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式）或]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x682868326}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x68771689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1564094025}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1724302604}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上启动]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的运行，并使能到]{style="font-family:宋体"}[Area 1]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_614669624}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 1 area 1 instance 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_649750917}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x812310295}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上启动]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的运行，并使能到]{style="font-family:宋体"}[Area 1]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1910231621}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 1 area 1 instance 1]{lang="EN-US"}
:::

::::: {#426531893 .myid}
[]{#_Toc245205348}[]{#_Toc404789079}[]{#struct_0_14538_x1521_1469550794}[]{#_Toc303674217}[]{#_Toc303084626}[]{#_Toc237923133}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 bfd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_2087867186}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_841074626}
:::

[ ]{lang="EN-US"}

[**[ospfv3 bfd enable]{lang="EN-US"}**]{#struct_0_14538_x1521_1724368140}[命令用来在运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的接口下使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ospfv3 bfd enable]{lang="EN-US"}**]{#struct_0_14538_x1521_1745410270}[命令]{style="font-family:宋体"}[用来在运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的接口下关闭]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x52542640}

[**[ospfv3 bfd enable]{lang="EN-US"}**[ \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x400418783}

[**[undo ospfv3 bfd enable ]{lang="EN-US"}**[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_715101762}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1541874868}

[[运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1913366582}[的接口未使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2106946746}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1149546643}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724433676}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x961441493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1634833894}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1785628854}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_800707156}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_653505040}

[[BFD]{lang="EN-US"}]{#struct_0_14538_x1521_2068510613}[（]{style="font-family:宋体"}[Bidirectional Forwarding Detection]{lang="EN-US"}[，双向转发检测）能够为]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[邻居之间的链路提供快速检测功能。当邻居之间的链路出现故障时，加快]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的收敛速度。]{style="font-family:宋体"}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1139849363}[通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文实现]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2056367389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1725023500}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x2127785552}[使能接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1882522128}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 bfd enable instance 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1465018314}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1622322931}[使能接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_988159285}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] ospfv3 bfd enable instance 1]{lang="EN-US"}
:::::

::: {#-832173441 .myid}
[]{#_Toc404789080}[]{#struct_0_14538_x1521_618703806}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 cost**

------------------------------------------------------------------------

[**[ospfv3 cost]{lang="EN-US"}**]{#struct_0_14538_x1521_1725089036}[命令用来配置运行不同]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例的接口的开销值。]{style="font-family:宋体"}

[**[undo ospfv3 cost]{lang="EN-US"}**]{#struct_0_14538_x1521_x1338880683}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2047938095}

[**[ospfv3 cost]{lang="EN-US"}**[ *value* \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_827448027}

[**[undo ospfv3 cost]{lang="EN-US"}**[ \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x98415065}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1090304924}

[[路由器接口按照带宽自动计算运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1226492730}[协议所需的开销；对于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[；对于]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_166993043}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x396537179}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724499213}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1783319759}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1461958822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_497898920}

[*[value]{lang="EN-US"}*]{#struct_0_14538_x1521_x1848375992}[：接口运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的路由开销，]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，其他接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x1430166323}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x509072023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x11663543}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1712468141}[指定运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的开销为]{style="font-family:宋体"}[33]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1724564749}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 cost 33 instance 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x554540852}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1286671764}[指定运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[的开销为]{style="font-family:宋体"}[33]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1577911835}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 cost 33 instance 1]{lang="EN-US"}
:::

::: {#559093326 .myid}
[]{#_Toc404789081}[]{#struct_0_14538_x1521_1384095532}[]{#_Toc245205349}[]{#_Toc138238110}[]{#_Toc93984848}[]{#_Toc81478714}[]{#_Toc58333194}[]{#_Toc58294842}[]{#_Toc33866066}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 dr-priority**

------------------------------------------------------------------------

[**[ospfv3 dr-priority]{lang="EN-US"}**]{#struct_0_14538_x1521_1737997946}[命令用来配置运行不同]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例的接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ospfv3 dr-priority]{lang="EN-US"}**]{#struct_0_14538_x1521_1030600230}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724630285}

[**[ospfv3 dr-priority]{lang="EN-US"}***[ priority]{lang="EN-US"}*[ \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1323027547}

[**[undo ospfv3 dr-priority]{lang="EN-US"}**[ \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1331354801}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x388284521}

[[接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_14538_x1521_x1649928526}[优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1829695959}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1470289352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1526457383}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_608647245}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1724695821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2045389366}

[*[priority]{lang="EN-US"}*]{#struct_0_14538_x1521_x1173031659}[：接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1174553520}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1759553789}

[[接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_14538_x1521_x589904220}[优先级决定了该接口在选举]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[时所具有的资格，优先级高的在选举时被首先考虑。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2111903676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1353816451}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1837012886}[设置运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在选举]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[时的优先级为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1724237069}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 dr-priority 8 instance 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_625655688}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_122047261}[设置运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在选举]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[时的优先级为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x960029551}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 dr-priority 8 instance 1]{lang="EN-US"}
:::

::::: {#82240944 .myid}
[]{#_Toc245205360}[]{#_Toc138238117}[]{#_Toc93984853}[]{#_Toc81478719}[]{#_Toc58333207}[]{#_Toc58294854}[]{#_Toc33866078}[]{#_Toc303084617}[]{#_Toc300320722}[]{#_Toc138212591}[]{#_Toc93984817}[]{#_Toc61236368}[]{#_Toc61093167}[]{#_Toc58812090}[]{#_Toc56887219}[]{#_Toc45164815}[]{#_Toc30906018}[]{#_Toc14516707}[]{#_Toc13738149}[]{#_Toc12073427}[]{#_Toc10449486}[]{#_Toc303674220}[]{#_Toc303084620}[]{#_Toc309373531}[]{#_Toc404789082}[]{#struct_0_14538_x1521_x1450708962}[]{#_Toc141494286}[]{#_Toc141494287}[]{#_Toc141494290}[]{#_Toc141494291}[]{#_Toc141494292}[]{#_Toc141494293}[]{#_Toc141494294}[]{#_Toc141494295}[]{#_Toc141494296}[]{#_Toc141494297}[]{#_Toc141494298}[]{#_Toc141494299}[]{#_Toc141494300}[]{#_Toc141494301}[]{#_Toc141494305}[]{#_Toc141494306}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 ipsec-profile**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPFv3命令.files/image001.png){#图片 3 width="63" height="25"}]{lang="EN-US"}]{#struct_0_14538_x1521_1387611767}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14538_x1521_x1814959163}
:::

[ ]{lang="EN-US"}

[**[ospfv3 ipsec-profile]{lang="EN-US"}**]{#struct_0_14538_x1521_1724302605}[命令用来在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口上应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[**[undo ospfv3 ipsec-profile]{lang="EN-US"}**]{#struct_0_14538_x1521_614735160}[命令用来取消]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[接口上应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1835375177}

[**[ospfv3 ipsec-profile]{lang="EN-US"}[ ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*[ \[ **instance** **** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x811807178}

[**[undo ospfv3 ipsec-profile]{lang="EN-US"}**[ \[ **instance** **** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1866250311}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1952019647}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x868146169}[接口]{style="font-family:宋体"}[没有应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2029378653}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1724368141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1745475806}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1571953280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1457469321}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_701322444}

[*[profile-name]{lang="EN-US"}*]{#struct_0_14538_x1521_598130125}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个]{style="font-family:宋体"}[字符]{style="font-family:宋体"}[的字符串，不区分大小写。]{style="font-family:宋体"}

[*[instance-id]{lang="FR"}*]{#struct_0_14538_x1521_1897847601}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1619145664}

[[本命令应结合]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_14538_x1521_x390719340}[安全框架使用，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的具体情况请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPsec]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724433677}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x961507029}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1600147808}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架为]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_1396801947}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="NO-BOK"}

[\[Sysname-GigabitEthernet1/0/1\] os]{lang="NO-BOK"}[pfv3 ipsec-profile profile001]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1844437774}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1884683336}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架为]{style="font-family:宋体"}[profile001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_x2010316142}

[\[Sysname\] interface vlan-interface 10]{lang="NO-BOK"}

[\[Sysname-Vlan-interface10\] ospfv3 ]{lang="NO-BOK"}[ipsec-profile profile001]{lang="EN-US"}
:::::

::: {#-822337401 .myid}
[]{#_Toc404789083}[]{#struct_0_14538_x1521_x1030862712}[]{#_Toc369250858}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 mib-binding**

------------------------------------------------------------------------

[**[ospfv3 mib-binding]{lang="EN-US"}**]{#struct_0_14538_x1521_x1226324884}[命令用来配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ospfv3 mib-binding]{lang="EN-US"}**]{#struct_0_14538_x1521_1715310581}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x140311233}

[**[ospfv3 mib-binding]{lang="EN-US"}**[ *process-id*]{lang="EN-US"}]{#struct_0_14538_x1521_1698020643}

[**[undo ospfv3 mib-binding]{lang="EN-US"}**]{#struct_0_14538_x1521_x1151903568}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1070874597}

[[MIB]{lang="EN-US"}]{#struct_0_14538_x1521_x1694459907}[绑定在进程号最小的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1761102272}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1878012060}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1317396925}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_443534758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_345088560}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2018585568}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_131936702}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1026521573}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1508550611}*[process-id]{lang="FR"}*[不存在，配置]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="FR"}[进程绑定命令时将会提示]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程不存在，无法完成配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_14538_x1521_x784063675}[OSPFv3]{lang="FR"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="FR"}[，若删除]{style="font-family:宋体"}*[process-id]{lang="FR"}*[对应的]{style="font-family:宋体"}[OSPFv3]{lang="FR"}[进程，则同时删除]{style="font-family:宋体"}[OSPFv3]{lang="FR"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="FR"}[配置，]{style="font-family:宋体"}[MIB]{lang="EN-US"}[绑定到进程号最小的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x459681943}

[[\#]{lang="EN-US"}]{#struct_0_14538_x1521_x1468170700}[ ]{lang="EN-US" style="font-family:宋体"}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_889073652}

[\[Sysname\] ospfv3 mib-binding 100]{lang="EN-US"}
:::

::: {#896243864 .myid}
[]{#_Toc404789084}[]{#struct_0_14538_x1521_1725023501}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 mtu-ignore**

------------------------------------------------------------------------

[**[ospfv3 mtu-ignore]{lang="EN-US"}**]{#struct_0_14538_x1521_x2127720016}[命令用来配置接口在进行]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文交换时忽略]{style="font-family:宋体"}[MTU]{lang="EN-US"}[检查]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ospfv3 mtu-ignore]{lang="EN-US"}**]{#struct_0_14538_x1521_x872829403}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1115679120}

[**[ospfv3 mtu-ignore]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1441281310}

[**[undo ospfv3 mtu-ignore]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_137410738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1487701017}

[[接口在进行]{style="font-family:宋体"}[DD]{lang="EN-US"}]{#struct_0_14538_x1521_1725089037}[报文交换时执行]{style="font-family:宋体"}[MTU]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724499214}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1783778511}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_475058743}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1178001398}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_330088547}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x923574016}

[*[instance-id]{lang="FR"}*]{#struct_0_14538_x1521_x1816514866}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="FR"}[，取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[255]{lang="FR"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724564750}

[[双方的接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_14538_x1521_x554082101}[必须相同才能建立邻居关系]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1386481774}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_67169158}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x792636837}[配置运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在进行]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文交换时忽略]{style="font-family:宋体"}[MTU]{lang="EN-US"}[检查]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_x1729359973}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="NO-BOK"}

[\[Sysname-GigabitEthernet1/0/1\] os]{lang="NO-BOK"}[pfv3 mtu-ignore instance 1]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1531425950}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_436718988}[配置运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在进行]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文交换时忽略]{style="font-family:宋体"}[MTU]{lang="EN-US"}[检查]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_1724630286}

[\[Sysname\] interface vlan-interface 10]{lang="NO-BOK"}

[\[Sysname-Vlan-interface10\] ospfv3 mtu-ignore instance 1]{lang="NO-BOK"}
:::

::: {#976798763 .myid}
[]{#_Toc404789085}[]{#struct_0_14538_x1521_x1322830939}[]{#_Toc322361690}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 network-type**

------------------------------------------------------------------------

[**[ospfv3 network-type]{lang="EN-US"}**]{#struct_0_14538_x1521_x1173697919}[命令用来配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口的网络类型。]{style="font-family:宋体"}

[**[undo ospfv3 network-type]{lang="EN-US"}**]{#struct_0_14538_x1521_x150779439}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1131487980}

[**[ospfv3 network-type ]{lang="EN-US"}**[{]{lang="EN-US"}**[ broadcast]{lang="EN-US"}**[ \| **nbma** \| **p2mp** \[ **unicast** \] \| **p2p** } \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1863366350}

[**[undo ospfv3 network-type]{lang="EN-US"}**[ \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_911347598}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1614577682}

[[当接口封装的链路层协议不同时，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x306808540}[接口网络类型的缺省值也不同：]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[当接口封装的链路层协议是]{style="font-family:宋体"}]{#struct_0_14538_x1521_1724695822}[Ethernet]{lang="EN-US"}[、]{style="font-family:宋体"}[FDDI]{lang="EN-US"}[时，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口网络类型的缺省值为广播类型；]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[当接口封装的链路层协议是]{style="font-family:宋体"}]{#struct_0_14538_x1521_x2045454902}[ATM]{lang="EN-US"}[、帧中继或]{style="font-family:宋体"}[X.25]{lang="EN-US"}[时，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口网络类型的缺省值为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[；]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[当接口封装的链路层协议是]{style="font-family:宋体"}]{#struct_0_14538_x1521_616694766}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[LAPB]{lang="EN-US"}[、]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[或]{style="font-family:宋体"}[POS]{lang="EN-US"}[时，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口网络类型的缺省值为]{style="font-family:宋体"}[P2P]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2036308179}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1264005359}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x229903960}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_2318216}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x149168581}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724237070}

[**[broadcast]{lang="EN-US"}**]{#struct_0_14538_x1521_625196937}[：配置接口的网络类型为广播类型。]{style="font-family:宋体"}

[**[nbma]{lang="EN-US"}**]{#struct_0_14538_x1521_793655409}[：配置接口的网络类型为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[p2mp]{lang="EN-US"}**]{#struct_0_14538_x1521_x768071537}[：配置接口的网络类型为点到多点类型。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_14538_x1521_x638544643}[：]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[类型支持单播发送报文，缺省情况下是组播方式发送报文。]{style="font-family:宋体"}

[**[p2p]{lang="EN-US"}**]{#struct_0_14538_x1521_x2014506997}[：配置接口的网络类型为点到点类型。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_449462473}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_11998943}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[如果在广播网络上有不支持组播地址的路由器，可以将接口的网络类型改为]{style="font-family:宋体"}]{#struct_0_14538_x1521_1163074388}[NBMA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[在]{style="font-family:宋体"}]{#struct_0_14538_x1521_1724302606}[NBMA]{lang="EN-US"}[网络中，如果任意两台路由器之间都有一条虚电路直接可达，或者说，这个网络是全连通的，那么可以把]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口的网路类型配置为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[；否则，需要把]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口的网络类型配置为点到多点，这样，两台不能直接可达的路由器之间可以通过一台与两者都直接可达的路由器来交换路由信息。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[接口的网络类型为]{style="font-family:宋体"}]{#struct_0_14538_x1521_614800696}[NBMA]{lang="EN-US"}[或]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[（]{style="font-family:宋体"}[unicast]{lang="EN-US"}[）时，必须使用]{style="font-family:宋体"}[peer]{lang="EN-US"}[命令来配置邻接点。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[接口的网络类型为]{style="font-family:宋体"}]{#struct_0_14538_x1521_457992877}[P2MP]{lang="EN-US"}[（]{style="font-family:宋体"}[unicast]{lang="EN-US"}[）时，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议在该接口上发送的报文均为单播报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1474332191}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x2030511421}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1300971777}[设置运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[网络类型为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1274112159}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 network-type nbma]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x1945815253}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x2102760555}[设置运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface20]{lang="EN-US"}[网络类型为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1724368142}

[\[Sysname\] interface vlan-interface 20]{lang="EN-US"}

[\[Sysname-Vlan-interface20\] ospfv3 network-type nbma]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1745279198}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ospfv3 dr-priority]{lang="EN-US"}**]{#struct_0_14538_x1521_300178819}
:::

::: {#903988763 .myid}
[]{#_Toc404789086}[]{#struct_0_14538_x1521_x1764310948}[]{#_Toc322361691}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 peer**

------------------------------------------------------------------------

[**[ospfv3 peer]{lang="EN-US"}**]{#struct_0_14538_x1521_x672939553}[命令用来指定邻居接口的链路本地地址，并指定该邻居是否有选举权。]{style="font-family:宋体"}

[**[undo ospfv3 peer]{lang="EN-US"}**]{#struct_0_14538_x1521_x1757550229}[命令用来取消该操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_621350100}

[**[ospfv3 peer]{lang="EN-US"}**[ *ipv6-address* \[ **cost** *value* \| **dr-priority** *dr-priority* \] \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1724433678}

[**[undo ospfv3 peer]{lang="EN-US"}**[ *ipv6-address* \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x961310421}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1085464347}

[[没有指定邻居接口的链路本地地址。]{style="font-family:宋体"}]{#struct_0_14538_x1521_1238269484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1407040110}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1269851081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1539654531}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1117171910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1656302059}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1725023502}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_14538_x1521_x2127916624}[：邻居的链路本地地址。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}***[ value]{lang="EN-US"}*]{#struct_0_14538_x1521_927658920}[：表示网络邻居的开销，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dr-priority]{lang="EN-US"}***[ dr-priority]{lang="EN-US"}*]{#struct_0_14538_x1521_2143893785}[：表示网络邻居的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x681786950}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x364237243}

[[当路由器的接口类型为如下网络类型时，需要为其指定相邻路由器]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14538_x1521_319967451}[地址：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NBMA]{lang="EN-US"}]{#struct_0_14538_x1521_206054104}[网络]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2MP]{lang="EN-US"}]{#struct_0_14538_x1521_1324661773}[网络（仅当接口选择单播形式发送报文时，需要此配置）]{style="font-family:宋体"}

[[由于无法通过广播]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_14538_x1521_1725089038}[报文的形式发现相邻路由器，必须手工指定相邻路由器的本地链路地址。对于]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[网络，可以指定该相邻路由器是否有选举权等。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1339273899}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_628749661}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x844086624}[在运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上指定邻居的链路本地地址为]{style="font-family:宋体"}[FE80::1111]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1127371978}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 peer fe80::1111]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x1835751267}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1666902194}[在运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上指定邻居的链路本地地址为]{style="font-family:宋体"}[FE80::1111]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1811072031}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 peer fe80::1111]{lang="EN-US"}
:::

::: {#684633393 .myid}
[]{#_Toc404789087}[]{#struct_0_14538_x1521_x737703580}[]{#_Toc376507160}[]{#_Toc374005801}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 prefix-suppression**

------------------------------------------------------------------------

[**[ospfv3 prefix-suppression]{lang="EN-US"}**]{#struct_0_14538_x1521_x737638044}[命令用来抑制接口进行前缀发布。]{style="font-family:
宋体"}

[**[undo ospfv3 prefix-suppression]{lang="EN-US"}**]{#struct_0_14538_x1521_1771341744}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x738227867}

[**[ospfv3 prefix-suppression]{lang="EN-US"}**[ \[ **disable** \] \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x738162331}

[**[undo ospfv3 prefix-suppression ]{lang="EN-US"}**[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_44550982}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x738096795}

[[不抑制接口进行前缀发布。]{style="font-family:宋体"}]{#struct_0_14538_x1521_1279588465}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x738031259}

[[接口]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1881838320}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x737965723}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x737900187}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x913186049}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x737834651}

[**[disable]{lang="EN-US"}**]{#struct_0_14538_x1521_x2057826137}[：不抑制接口进行前缀发布。]{style="font-family:宋体"}

[**[instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_14538_x1521_x737769115}[：]{style="font-family:宋体"}[接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x737703579}

[[如果]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1051678545}[进程配置了抑制前缀发布，但某个接口不想进行抑制，此时可以配置本命令并指定]{style="font-family:宋体"}**[disable]{lang="EN-US"}**[参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x737638043}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1771145136}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_827856069}[抑制接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[进行前缀发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_827921605}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 prefix-suppression]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1146686065}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_827987141}[抑制接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[进行前缀发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1544627458}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 prefix-suppression]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828052677}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[prefix-suppression]{lang="SV"}**]{#struct_0_14538_x1521_828118213}
:::

::: {#798864272 .myid}
[]{#_Toc404789088}[]{#struct_0_14538_x1521_1724499215}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer dead**

------------------------------------------------------------------------

[**[ospfv3 timer dead]{lang="EN-US"}**]{#struct_0_14538_x1521_1783712975}[命令用来设置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的邻居失效时间。]{style="font-family:宋体"}

[**[undo ospfv3 timer dead]{lang="EN-US"}**]{#struct_0_14538_x1521_1680575955}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1134838320}

[**[ospfv3 timer dead ]{lang="EN-US"}***[seconds ]{lang="EN-US"}*[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_81376766}

[**[undo ospfv3 timer dead ]{lang="EN-US"}**[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1724564751}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724630287}

[[P2P]{lang="EN-US"}]{#struct_0_14538_x1521_x1322896475}[、]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[类型接口的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[邻居失效的时间为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒；]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[、]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型接口的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[邻居失效的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_572968148}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1596942284}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x405679486}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_45878047}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_2018589046}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x229889784}

[*[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_1561992023}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[邻居失效的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1724695823}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x2045520438}[邻居的失效时间是指：在该时间间隔内，若未收到邻居的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，就认为该邻居已失效。]{style="font-family:宋体"}**[dead]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值至少应为]{style="font-family:宋体"}**[hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值的]{style="font-family:宋体"}[4]{lang="EN-US"}[倍，同一网段上的接口的]{style="font-family:宋体"}**[dead ]{lang="EN-US"}***[seconds]{lang="EN-US"}*[也必须相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_807482202}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1602435276}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_438659691}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的邻居失效时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_114117575}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 timer dead 60]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1431758315}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x618940013}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上的邻居失效时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1724237071}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 timer dead 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_625131401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospfv3 timer hello]{lang="EN-US"}**]{#struct_0_14538_x1521_x1491454852}
:::

::: {#2019013512 .myid}
[]{#_Toc404789089}[]{#struct_0_14538_x1521_x92610291}[]{#_Toc303674221}[]{#_Toc303084619}[]{#_Toc300320711}[]{#_Toc138212579}[]{#_Toc93984805}[]{#_Toc61236355}[]{#_Toc61093154}[]{#_Toc58812077}[]{#_Toc56887206}[]{#_Toc45164806}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer hello**

------------------------------------------------------------------------

[**[ospfv3 timer hello]{lang="EN-US"}**]{#struct_0_14538_x1521_x2058491380}[命令用来配置接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo ospfv3 timer hello]{lang="EN-US"}**]{#struct_0_14538_x1521_421167686}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1027922460}

[**[ospfv3 timer hello ]{lang="EN-US"}***[seconds ]{lang="EN-US"}*[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1153375217}

[**[undo ospfv3 timer hello ]{lang="EN-US"}**[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1724302607}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_614866232}

[[P2P]{lang="EN-US"}]{#struct_0_14538_x1521_867580915}[、]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[类型接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒；]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[、]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x329042393}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_220457377}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x165829902}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1773538933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x14810701}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x681129531}

[*[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_1724368143}[：接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1745344734}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_340816265}

[*[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_x1738132968}[的值越小，发现网络拓扑改变的速度越快，对系统资源的开销也就越大。同一网段上的接口的]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[必须相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_483220926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x747753315}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1328898860}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_2135758093}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 timer hello 20]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1927261514}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1724433679}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x961375957}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 timer hello 20]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_863070191}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[ospfv3 timer dead]{lang="EN-US"}**]{#struct_0_14538_x1521_x1874740730}
:::

::: {#-1523845146 .myid}
[]{#_Toc303674222}[]{#_Toc309373532}[]{#_Toc404789090}[]{#struct_0_14538_x1521_x439935385}[]{#_Toc322361694}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer poll**

------------------------------------------------------------------------

[**[ospfv3 timer poll]{lang="EN-US"}**]{#struct_0_14538_x1521_x346252295}[命令用来配置在]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[接口上向状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的邻居路由器发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo ospfv3 timer poll]{lang="EN-US"}**]{#struct_0_14538_x1521_x1437259923}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_268588639}

[**[ospfv3 timer poll ]{lang="EN-US"}***[seconds ]{lang="EN-US"}*[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1725023503}

[**[undo ospfv3 timer poll]{lang="EN-US"}**[ \[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x2127851088}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1933394218}

[[在]{style="font-family:宋体"}[NBMA]{lang="EN-US"}]{#struct_0_14538_x1521_x875478317}[接口上向状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的邻居路由器发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x590848602}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1322746320}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_654330443}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x2117643452}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1996431869}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1725089039}

[*[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_x1339208363}[：向状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的邻居路由器发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_x5434343}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1227333595}

[[在]{style="font-family:宋体"}[NBMA]{lang="EN-US"}]{#struct_0_14538_x1521_1920611105}[的网络上，当邻居失效后，将按轮询时间间隔定期地发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。用户可配置轮询时间间隔以指定该接口在与相邻路由器构成邻居关系之前发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_14538_x1521_232695865}[报文的时间间隔至少应为发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文时间间隔的]{style="font-family:宋体"}[4]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1129630441}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_381105050}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1068696413}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1004384145}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 timer poll 120]{lang="NO-BOK"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x1736009885}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x523274807}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_175451721}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospfv3 timer poll 120]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2076439599}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ospfv3 timer hello]{lang="EN-US"}**]{#struct_0_14538_x1521_726273936}
:::

::: {#-2115878694 .myid}
[]{#_Toc404789091}[]{#struct_0_14538_x1521_x465368770}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 timer retransmit**

------------------------------------------------------------------------

[**[ospfv3 timer retransmit]{lang="EN-US"}**]{#struct_0_14538_x1521_x1004318609}[命令用来配置接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔。]{style="font-family:宋体"}

[**[undo ospfv3 timer retransmit]{lang="EN-US"}**]{#struct_0_14538_x1521_x2108037433}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x181708628}

[**[ospfv3 timer retransmit ]{lang="EN-US"}***[seconds ]{lang="EN-US"}*[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_1843896375}

[**[undo ospfv3 timer retransmit ]{lang="EN-US"}**[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1453816015}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1319781179}

[[接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1134086581}[的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1569707043}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_1170922441}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1004253073}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x827688801}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1137138062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1069953814}

[*[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_x1457376082}[：接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1107957964}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x395738986}

[[当一台路由器向它的邻居发送一条]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_44728696}[后，需要等到对方的确认报文。若在该重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔内未收到对方的确认报文，就会重传这条]{style="font-family:宋体"}[LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[相邻路由器重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_595856172}[时间间隔的值不要设置得太小，否则将会引起不必要的重传。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1004187537}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x443842403}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x733468516}[指定运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔为]{style="font-family:宋体"}[12]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_x347437205}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="NO-BOK"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 timer retransmit 12 instance 1]{lang="NO-BOK"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x1028142521}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_593250915}[指定运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔为]{style="font-family:宋体"}[12]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_998782142}

[\[Sysname\] interface vlan-interface 10]{lang="NO-BOK"}

[\[Sysname-Vlan-interface10\] ospfv3 timer retransmit 12 instance 1]{lang="NO-BOK"}
:::

::: {#-391043086 .myid}
[]{#_Toc404789092}[]{#struct_0_14538_x1521_x1004646289}[]{#_Toc309373533}[]{#_Toc300320714}[]{#_Toc138212582}[]{#_Toc93984808}[]{#_Toc61236358}[]{#_Toc61093157}[]{#_Toc58812080}[]{#_Toc56887209}[]{#_Toc45164809}

**OSPFv3 \-- OSPFv3配置命令 \-- ospfv3 trans-delay**

------------------------------------------------------------------------

[**[ospfv3 trans-delay]{lang="EN-US"}**]{#struct_0_14538_x1521_1062708494}[命令用来配置接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的传输延迟时间。]{style="font-family:宋体"}

[**[undo ospfv3 trans-delay]{lang="EN-US"}**]{#struct_0_14538_x1521_2049683084}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1670593804}

[**[ospfv3 trans-delay ]{lang="EN-US"}***[seconds ]{lang="EN-US"}*[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1385538853}

[**[undo ospfv3 trans-delay ]{lang="EN-US"}**[\[ **instance** *instance-id* \]]{lang="EN-US"}]{#struct_0_14538_x1521_x1968285405}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1243812882}

[[接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_1399609760}[的传输延迟时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x660455694}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1004580753}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1203262219}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1185400075}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x903329474}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_350882427}

[*[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_x1989809050}[：接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的传输延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_145106491}[：接口所属的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1205054812}

[[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_x430987977}[在本路由器的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中会随时间老化（]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的老化时间每秒钟加]{style="font-family:宋体"}[1]{lang="EN-US"}[），但在网络的传输过程中却不会，所以有必要在发送之前在]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的老化时间上增加一定的延迟时间。此配置对低速率的网络尤其重要。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1004515217}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_1954776649}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x2091751150}[指定运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[洪泛]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时延值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_1062661304}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="NO-BOK"}

[\[Sysname-GigabitEthernet1/0/1\] ospfv3 trans-delay 3 instance 1]{lang="NO-BOK"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_17025061}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1492976288}[指定运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[洪泛]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时延值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_1426677516}

[\[Sysname\] interface vlan-interface 10]{lang="NO-BOK"}

[\[Sysname-Vlan-interface10\] ospfv3 trans-delay 3 instance 1]{lang="NO-BOK"}[]{#_Toc123036171}[]{#_Toc93984810}[]{#_Toc61236360}[]{#_Toc61093161}[]{#_Toc58812084}[]{#_Toc56887213}[]{#_Toc45164811}
:::

::: {#830408614 .myid}
[]{#_Toc404789093}[]{#struct_0_14538_x1521_66961154}[]{#_Toc309373534}[]{#_Toc300320716}[]{#_Toc138212584}

**OSPFv3 \-- OSPFv3配置命令 \-- preference**

------------------------------------------------------------------------

[**[preference]{lang="EN-US"}**]{#struct_0_14538_x1521_x1004449681}[命令用来配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议路由的优先级。]{style="font-family:宋体"}

[**[undo preference]{lang="EN-US"}**]{#struct_0_14538_x1521_1549552106}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1376279036}

[**[preference]{lang="EN-US"}**[ \[ **ase** \] { *preference* \| **route-policy** *route-policy-name* } \*]{lang="EN-US"}]{#struct_0_14538_x1521_1570577363}

[**[undo preference]{lang="EN-US"}**[ \[ **ase** \]]{lang="EN-US"}]{#struct_0_14538_x1521_2138536808}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2031820679}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_872941465}[内部路由的优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[外部路由的优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1993573741}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x104558052}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1003859857}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x2014950734}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x56246357}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x439386341}

[**[ase]{lang="EN-US"}**]{#struct_0_14538_x1521_x766641920}[：配置外部路由的优先级。如果未指定该参数，配置内部路由优先级。]{style="font-family:宋体"}

[*[preference]{lang="EN-US"}*]{#struct_0_14538_x1521_956836327}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。优先级的值越小，其实际的优先程度越高。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_14538_x1521_x1992518114}[：]{style="font-family:宋体"}[应用路由策略，对特定的路由设置优先级。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[是路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1975252554}

[[由于路由器上可能同时运行多个动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题，所以为每一种路由协议指定了一个缺省的优先级。在不同的路由协议发现去往同一目的地的多条路由时，优先级高的协议发现的路由将被选中以转发]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_14538_x1521_x459158892}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1003794321}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_157057379}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议路由的优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> sy]{lang="EN-US"}]{#struct_0_14538_x1521_x950490875}[stem-view]{lang="NO-BOK"}

[\[Sysname\] ospfv3]{lang="NO-BOK"}

[\[Sysname-ospfv3-1\] p]{lang="NO-BOK"}[reference 150]{lang="EN-US"}
:::

::: {#56918495 .myid}
[]{#_Toc404789094}[]{#struct_0_14538_x1521_828052675}[]{#_Toc376507167}[]{#_Toc374005800}

**OSPFv3 \-- OSPFv3配置命令 \-- prefix-suppression**

------------------------------------------------------------------------

[**[prefix-suppression]{lang="EN-US"}**]{#struct_0_14538_x1521_828118211}[命令用来抑制]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程进行前缀发布。]{style="font-family:宋体"}

[**[undo prefix-suppression]{lang="EN-US"}**]{#struct_0_14538_x1521_x871847965}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828183747}

[**[prefix-suppression]{lang="EN-US"}**]{#struct_0_14538_x1521_1485434839}

[**[undo prefix-suppression]{lang="EN-US"}**]{#struct_0_14538_x1521_828249283}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828314819}

[[不抑制]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_211151945}[进程进行前缀发布。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828380355}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1388176019}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828445891}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_827856068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_15748675}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_827921604}

[[接口使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_827987140}[后，会将接口下的所有网段路由都通过]{style="font-family:宋体"}[LSA]{lang="EN-US"}[发布，但有时候网段路由是不希望被发布的。通过前缀抑制配置，可以减少]{style="font-family:宋体"}[LSA]{lang="EN-US"}[中携带不需要的前缀，即不发布某些网段路由，从而提高网络安全性，加快路由收敛。]{style="font-family:宋体"}

[[全局配置前缀抑制不能抑制]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}]{#struct_0_14538_x1521_x1544627459}[接口和处于]{style="font-family:宋体"}[silent-interface]{lang="EN-US"}[状态接口对应的前缀。如果想对]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口或处于]{style="font-family:宋体"}[silent-interface]{lang="EN-US"}[状态接口进行抑制，可以通过接口下配置前缀抑制（]{style="font-family:宋体"}**[ospfv3 prefix-suppression]{lang="EN-US"}**[命令）来实现。]{style="font-family:宋体"}

[[当使能前缀抑制时，具体处理如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_828052676}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[Type-8 ]{lang="EN-US"}[LSA]{lang="EN-US"}]{#struct_0_14538_x1521_828118212}[中不发布处于抑制的接口前缀信息。]{lang="EN-US" style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[对于广播网]{style="font-family:宋体"}]{#struct_0_14538_x1521_x871847962}[/NBMA]{lang="EN-US"}[网络，]{style="font-family:宋体"}[DR]{lang="EN-US"}[在生成]{style="font-family:宋体"}[Type-9 LSA]{lang="EN-US"}[引用]{style="font-family:宋体"}[Type-2 LSA]{lang="EN-US"}[时，不发布处于抑制的接口前缀信息。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[对于]{style="font-family:宋体"}]{#struct_0_14538_x1521_828183748}[P2P/P2MP]{lang="EN-US"}[网络，生成]{style="font-family:宋体"}[Type-9 LSA]{lang="EN-US"}[引用]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[时，不发布处于抑制的接口前缀信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1485434828}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_828249284}[抑制]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的前缀发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_828314820}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] prefix-suppression]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2127500222}

[[l[   ]{style="font:7.0pt "}]{lang="SV" style="font-size:6.5pt;font-family:Wingdings"}**[ospfv3 prefix-suppression]{lang="SV"}**]{#struct_0_14538_x1521_828380356}
:::

::: {#2042025648 .myid}
[]{#_Toc404789095}[]{#struct_0_14538_x1521_828445892}[]{#_Toc376507168}[]{#_Toc374005802}

**OSPFv3 \-- OSPFv3配置命令 \-- reset ospfv3 process**

------------------------------------------------------------------------

[**[reset ospfv3 process]{lang="EN-US"}**]{#struct_0_14538_x1521_x1449923651}[命令用来重启]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_827856073}

[**[reset]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **process** \[ **graceful-restart** \]]{lang="EN-US"}]{#struct_0_14538_x1521_827921609}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1146686077}

[[用户]{style="font-family:宋体"}]{#struct_0_14538_x1521_827987145}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1544627454}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_828052681}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_828118217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x871847959}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_828183753}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指]{style="font-family:宋体"}[定本参数，则]{style="font-family:宋体"}[重启所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_14538_x1521_828249289}[：以]{style="font-family:宋体"}[GR]{lang="EN-US"}[方式重启]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x576608422}

[[使用]{style="font-family:宋体"}**[reset ospfv3 process]{lang="EN-US"}**]{#struct_0_14538_x1521_828314825}[命令重启]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[，可以获得如下结果：]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[可以立即清除无效的]{style="font-family:宋体"}]{#struct_0_14538_x1521_x2127500219}[LSA]{lang="EN-US"}[，而不必等到]{style="font-family:宋体"}[LSA]{lang="EN-US"}[超时。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[方便重新选举]{style="font-family:宋体"}]{#struct_0_14538_x1521_828380361}[DR]{lang="EN-US"}[、]{style="font-family:宋体"}[BDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}[重启前的]{style="font-family:宋体"}]{#struct_0_14538_x1521_828445897}[OSPFv3]{lang="EN-US"}[配置不会丢失。]{style="font-family:宋体"}

[[执行该命令后，系统提示用户确认是否重启]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1449923654}[协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_827856074}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1940566457}[重启所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[\<Sysname\> reset ospfv3 process]{lang="EN-US"}]{#struct_0_14538_x1521_827921610}

[Reset OSPFv3 process? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#-405028247 .myid}
[]{#_Toc404789096}[]{#struct_0_14538_x1521_827987146}[]{#_Toc376507170}[]{#_Toc374005804}

**OSPFv3 \-- OSPFv3配置命令 \-- reset ospfv3 redistribution**

------------------------------------------------------------------------

[**[reset ospfv3 redistribution]{lang="EN-US"}**]{#struct_0_14538_x1521_828052682}[命令用来重新向]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[引入外部路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1500674542}

[**[reset]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **redistribution**]{lang="EN-US"}]{#struct_0_14538_x1521_828118218}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828183754}

[[用户]{style="font-family:宋体"}]{#struct_0_14538_x1521_x853217320}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828249290}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_828314826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x2127500216}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828380362}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_568139110}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定]{style="font-family:宋体"}[本参数]{style="font-family:宋体"}[，所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程都将重新引入外部路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_828445898}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_424571542}[重新向]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[引入外部路由]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset ospfv3 redistribution]{lang="EN-US"}]{#struct_0_14538_x1521_1233703269}
:::

::: {#730515215 .myid}
[]{#_Toc404789097}[]{#struct_0_14538_x1521_424637078}[]{#_Toc376507169}[]{#_Toc374005803}

**OSPFv3 \-- OSPFv3配置命令 \-- reset ospfv3 statistics**

------------------------------------------------------------------------

[**[reset ospfv3 statistics]{lang="EN-US"}**]{#struct_0_14538_x1521_x1264111940}[命令用来清除]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424702614}

[**[reset]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **statistics**]{lang="EN-US"}]{#struct_0_14538_x1521_424768150}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x60382156}

[[用户]{style="font-family:宋体"}]{#struct_0_14538_x1521_424833686}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1807125748}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_424899222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_424964758}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1352919178}

[*[process-id]{lang="EN-US"}*]{#struct_0_14538_x1521_425030294}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定]{style="font-family:宋体"}[本参数]{style="font-family:宋体"}[，则清除所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x305518923}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_425095830}[清除所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ospfv3 statistics]{lang="EN-US"}]{#struct_0_14538_x1521_425161366}
:::

::: {#-1108162728 .myid}
[]{#_Toc404789098}[]{#struct_0_14538_x1521_855094017}

**OSPFv3 \-- OSPFv3配置命令 \-- router-id**

------------------------------------------------------------------------

[**[router-id]{lang="EN-US"}**]{#struct_0_14538_x1521_424571543}[命令用来配置运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo router-id]{lang="EN-US"}**]{#struct_0_14538_x1521_424637079}[命令用来删除已配置的路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1264111941}

[**[router-id]{lang="FR"}**]{#struct_0_14538_x1521_424702615}[ *router-id*]{lang="FR"}

[**[undo router-id]{lang="FR"}**]{#struct_0_14538_x1521_x1196395730}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424768151}

[[运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_424833687}[协议的路由器没有]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1807125749}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_424899223}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1414839211}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_424964759}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_425030295}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x305518924}

[*[router-id]{lang="EN-US"}*]{#struct_0_14538_x1521_425095831}[：路由器标识符，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1940933732}

[[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_425161367}[是一台运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的路由器在自治系统中的唯一标识。如果用户没有指定路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，则]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程无法运行。]{style="font-family:宋体"}

[[设置路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_14538_x1521_424571540}[时，必须保证自治系统中任意两个进程的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[都不相同。]{style="font-family:宋体"}

[[通过指定不同的进程号，可以在一台路由器上运行多个]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1233703271}[进程，在这种情况下，必须为不同进程指定不同的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424637076}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_424702612}[设置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10.1.1.3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1196395729}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] router-id 10.1.1.3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424768148}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospfv3]{lang="EN-US"}**]{#struct_0_14538_x1521_424833684}
:::

::: {#924654522 .myid}
[]{#_Toc404789099}[]{#struct_0_14538_x1521_x1030294898}[]{#_Toc309373535}[]{#_Toc300320721}[]{#_Toc138212589}[]{#_Toc93984815}[]{#_Toc61236366}[]{#_Toc61093166}[]{#_Toc58812089}[]{#_Toc56887218}[]{#_Hlt581565}

**OSPFv3 \-- OSPFv3配置命令 \-- silent-interface (OSPFv3 view)**

------------------------------------------------------------------------

[**[silent-interface]{lang="EN-US"}**]{#struct_0_14538_x1521_659711842}[命令用来禁止接口收发]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo silent-interface]{lang="EN-US"}**]{#struct_0_14538_x1521_x1016359444}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1099349996}

[**[silent-interface]{lang="EN-US"}**[ { *interface-type interface-number* \| **all** }]{lang="EN-US"}]{#struct_0_14538_x1521_1594703702}

[**[undo silent-interface]{lang="EN-US"}**[ { *interface-type interface-number* \| **all** }]{lang="EN-US"}]{#struct_0_14538_x1521_x1004384144}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_992873470}

[[允许接口收发]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x269320421}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x110157595}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_541279918}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_688530685}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x834583933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_767514382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2007928826}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14538_x1521_x1004318608}[：接口类型和接口号，]{style="font-family:宋体"}[禁止指定]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口收发]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_14538_x1521_x541953492}[：禁止所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口收发]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x17523426}

[]{#struct_0_14538_x1521_x566700989}[[不同的进程可以对同一接口禁止收发]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#_Hlt19601446}[报文，但]{style="font-family:宋体"}**[silent-interface]{lang="EN-US"}**[命令只对本进程已经使能的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[接口起作用，对其它进程的接口不起作用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x274456210}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_x895238624}

[[\#]{lang="EN-US"}]{#struct_0_14538_x1521_1625850025}[禁止接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[和]{style="font-family:宋体"}[200]{lang="EN-US"}[中收发]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_x1004253072}

[\[Sysname\] ospfv3 100]{lang="NO-BOK"}

[\[Sysname-ospfv3-100\] router-id 10.100.1.9]{lang="NO-BOK"}

[\[Sysname-ospfv3-100\] silent-interface gigabitethernet 1/0/1]{lang="NO-BOK"}

[\[Sysname-ospfv3-100\] quit]{lang="NO-BOK"}

[\[Sysname\] ospfv3 200]{lang="NO-BOK"}

[\[Sysname-ospfv3-200\] router-id 20.100.1.9]{lang="NO-BOK"}

[\[Sysname-ospfv3-200\] silent-interface gigabitethernet 1/0/1]{lang="NO-BOK"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14538_x1521_738395140}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1909969776}[禁止接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[和]{style="font-family:宋体"}[200]{lang="EN-US"}[中收发]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_14538_x1521_x2009121735}

[\[Sysname\] ospfv3 100]{lang="NO-BOK"}

[\[Sysname-ospfv3-100\] router-id 10.100.1.9]{lang="NO-BOK"}

[\[Sysname-ospfv3-100\] silent-interface ]{lang="NO-BOK"}[vlan-interface 10]{lang="EN-US"}

[\[Sysname-ospfv3-100\] quit]{lang="NO-BOK"}

[\[Sysname\] ospfv3 200]{lang="NO-BOK"}

[\[Sysname-ospfv3-200\] router-id 20.100.1.9]{lang="NO-BOK"}

[\[Sysname-ospfv3-200\] silent-interface ]{lang="NO-BOK"}[vlan-interface 10]{lang="EN-US"}
:::

::: {#26182052 .myid}
[]{#_Toc404789100}[]{#struct_0_14538_x1521_2101108562}[]{#_Toc369250860}

**OSPFv3 \-- OSPFv3配置命令 \-- snmp-agent trap enable ospfv3**

------------------------------------------------------------------------

[**[snmp-agent trap enable ospfv3]{lang="EN-US"}**]{#struct_0_14538_x1521_1576516570}[命令用来开启]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable ospfv3**]{lang="EN-US"}]{#struct_0_14538_x1521_x1784942590}[命令用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_476687711}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable ospfv3** \[ **grrestarter-status-change** \| **grhelper-status-change** \| **if-state-change** \| **if-cfg-error** \| **if-bad-pkt** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **virtif-bad-pkt** \| **virtif-cfg-error** \|**virtif-state-change** \| **virtgrhelper-status-change** \| **virtneighbor-state-chang** \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_535024621}

[**[undo snmp-agent]{lang="EN-US"}**[ **trap** **enable ospfv3** \[ **grrestarter-status-change** \| **grhelper-status-change** \| **if-state-change** \| **if-cfg-error** \| **if-bad-pkt** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **virtif-bad-pkt** \| **virtif-cfg-error** \|**virtif-state-change** \| **virtgrhelper-status-change** \| **virtneighbor-state-change**\] \*]{lang="EN-US"}]{#struct_0_14538_x1521_271079596}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_538531419}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1337509642}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1675075387}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1545825585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x904266863}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x94905872}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1011436220}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1387289680}

[**[grrestarter-status-change]{lang="EN-US"}**]{#struct_0_14538_x1521_x80171011}[：]{style="font-family:
宋体"}[GR Restarter]{lang="EN-US"}[状态变化。]{style="font-family:宋体"}

[**[grhelper-status-change]{lang="EN-US"}**]{#struct_0_14538_x1521_x1599344250}[：]{style="font-family:宋体"}[邻居]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[状态变化。]{style="font-family:宋体"}

[**[if-state-change]{lang="EN-US"}**]{#struct_0_14538_x1521_x1550408431}[：接口状态变化。]{style="font-family:宋体"}

[**[if-cfg-error]{lang="EN-US"}**]{#struct_0_14538_x1521_x95042638}[：]{style="font-family:宋体"}[接口配置错误。]{style="font-family:宋体"}

[**[if-bad-pkt]{lang="EN-US"}**]{#struct_0_14538_x1521_x1045088529}[：]{style="font-family:宋体"}[接口接收了错误报文。]{style="font-family:宋体"}

[**[neighbor-state-change]{lang="EN-US"}**]{#struct_0_14538_x1521_1264174302}**[：]{style="font-family:宋体"}**[邻居状态变化。]{style="font-family:宋体"}

[**[nssatranslator-status-change]{lang="EN-US"}**]{#struct_0_14538_x1521_x1018878439}[：]{style="font-family:
宋体"}[NSSA]{lang="EN-US"}[转换路由器状态变化。]{style="font-family:宋体"}

[**[virtif-bad-pkt]{lang="EN-US"}**]{#struct_0_14538_x1521_1279241607}[：]{style="font-family:宋体"}[虚接口接收错误报文。]{style="font-family:宋体"}

[**[virt-config-error]{lang="EN-US"}**]{#struct_0_14538_x1521_x1165836114}[：虚接口配置错误。]{style="font-family:宋体"}

[**[virtif-state-change]{lang="EN-US"}**]{#struct_0_14538_x1521_1341593675}[：虚接口状态变化。]{style="font-family:宋体"}

[**[virtgrhelper-status-change]{lang="EN-US"}**]{#struct_0_14538_x1521_483249811}[：虚接口邻居]{style="font-family:
宋体"}[GR Helper]{lang="EN-US"}[状态变化。]{style="font-family:
宋体"}

[**[virtneighbor-state-change]{lang="EN-US"}**]{#struct_0_14538_x1521_x338057867}[：虚接口邻居状态变化。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x834894884}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1970606259}[关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x991104926}

[\[Sysname\] undo snmp-agent trap enable ospfv3]{lang="EN-US"}
:::

::: {#870763228 .myid}
[]{#_Toc404789101}[]{#struct_0_14538_x1521_x1454835700}[]{#_Toc369250861}

**OSPFv3 \-- OSPFv3配置命令 \-- snmp context-name**

------------------------------------------------------------------------

[**[snmp]{lang="EN-US"}**[ **context-name**]{lang="EN-US"}]{#struct_0_14538_x1521_x232566940}[命令用来创建一个管理]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp** **context-name**]{lang="EN-US"}]{#struct_0_14538_x1521_243398978}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x896841592}

[**[snmp]{lang="EN-US"}**[ **context-name** *context-name*]{lang="EN-US"}]{#struct_0_14538_x1521_684306965}

[**[undo]{lang="EN-US"}**[ **snmp** **context-name**]{lang="EN-US"}]{#struct_0_14538_x1521_x400212031}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1995700345}

[[没有配置管理]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1861863397}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1811329180}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1617311101}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1143115948}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_555279850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1873983883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1832041763}

[*[context-name]{lang="EN-US"}*]{#struct_0_14538_x1521_460103814}[：]{style="font-family:宋体"}[上下文的名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2126230458}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_527902490}[使用]{style="font-family:宋体"}[MIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Management Information Base]{lang="EN-US"}[，管理信息库）为]{style="font-family:宋体"}[NMS]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Management System]{lang="EN-US"}[，网络管理系统）提供对]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例的管理，但标准]{style="font-family:宋体"}[OSPFv3 MIB]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[为单实例管理对象，无法对多个]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例进行管理。因此，参考]{style="font-family:宋体"}[RFC 4750]{lang="EN-US"}[中对]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[多实例的管理方法，为管理]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体定义一个上下文名称，以此来区分不同的]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例，实现对多个]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[实例进行管理。需要注意的是，由于上下文名称只是]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[独有的概念，对于]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[，会将团体名映射为上下文名]{style="font-family:宋体"}[称以对不同协议进行区分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x823265681}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1494131421}[配置管理]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称为]{style="font-family:宋体"}[mib]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1592321009}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] snmp context-name mib]{lang="EN-US"}
:::

::: {#-132773443 .myid}
[]{#_Toc404789102}[]{#struct_0_14538_x1521_360244276}[]{#_Toc369250859}

**OSPFv3 \-- OSPFv3配置命令 \-- snmp trap rate-limit**

------------------------------------------------------------------------

[**[snmp trap rate-limit]{lang="EN-US"}**]{#struct_0_14538_x1521_93139639}[命令用来配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[在指定时间间隔内允许输出的告警信息条数。]{style="font-family:宋体"}

[**[undo snmp trap rate-limit]{lang="EN-US"}**]{#struct_0_14538_x1521_265957822}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1593328248}

[**[snmp trap rate-limit interval]{lang="EN-US"}***[ trap-interval ]{lang="EN-US"}***[count]{lang="EN-US"}**[ *trap-number*]{lang="EN-US"}]{#struct_0_14538_x1521_499388269}

[**[undo snmp trap rate-limit]{lang="EN-US"}**]{#struct_0_14538_x1521_x404793083}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1251572978}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_92420915}[在]{style="font-family:宋体"}[10]{lang="EN-US"}[内]{style="font-family:宋体"}[秒允许输出]{style="font-family:宋体"}[7]{lang="EN-US"}[条告警信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1241667172}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_425428487}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1006255595}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x184587478}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1615813985}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1300126119}

[*[trap-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_1860539576}[：指定时间间隔，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[trap-number]{lang="EN-US"}*]{#struct_0_14538_x1521_x1243143449}[：在指定时间间隔内允许输出的告警信息条数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，为]{style="font-family:宋体"}[0]{lang="EN-US"}[时表示不输出告警信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2000600381}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1410799523}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[在]{style="font-family:宋体"}[5]{lang="EN-US"}[秒内允许输出]{style="font-family:
宋体"}[10]{lang="EN-US"}[条告警信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x344771325}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] snmp trap rate-limit interval 5 count 10]{lang="EN-US"}
:::

::: {#-940476118 .myid}
[]{#_Toc404789103}[]{#struct_0_14538_x1521_x839608297}[]{#_Toc384373973}[]{#_Toc384373974}[]{#_Toc384373975}[]{#_Toc384373976}[]{#_Toc384373977}[]{#_Toc384373978}[]{#_Toc384373979}[]{#_Toc384373980}[]{#_Toc384373981}[]{#_Toc384373982}[]{#_Toc384373983}[]{#_Toc384373984}[]{#_Toc384373985}[]{#_Toc384373986}[]{#_Toc384373987}[]{#_Toc384373988}[]{#_Toc384373989}[]{#_Toc384373990}[]{#_Toc384373991}[]{#_Toc384373992}[]{#_Toc384373993}[]{#_Toc384373994}[]{#_Toc384373995}[]{#_Toc384373996}[]{#_Toc384373997}[]{#_Toc384373998}

**OSPFv3 \-- OSPFv3配置命令 \-- spf-schedule-interval**

------------------------------------------------------------------------

[**[spf-schedule-interval]{lang="EN-US"}**]{#struct_0_14538_x1521_x399276108}[命令用来配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由计算的时间间隔。]{style="font-family:宋体"}

[**[undo spf-schedule-interval]{lang="EN-US"}**]{#struct_0_14538_x1521_x327741767}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x341150188}

[**[spf-schedule-interval]{lang="EN-US"}**[ *maximum-interval* \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_14538_x1521_1279463619}

[**[undo spf-schedule-interval]{lang="EN-US"}**]{#struct_0_14538_x1521_x1004515216}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x774106706}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1723383197}[路由计算的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1156288970}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_1935657516}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_906082055}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_174092895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x590026871}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1839657355}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_x1004449680}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由计算的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_x16531835}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由计算的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_1694465040}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由计算的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1265191435}

[[根据本地维护的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_14538_x1521_1972525773}[，运行]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[协议的路由器通过]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节]{style="font-family:宋体"}[SPF]{lang="EN-US"}[的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。]{style="font-family:宋体"}

[[本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_2022543920}[，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_14538_x1521_x162626223}[和]{style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1754145498}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_207406803}[设置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由计算最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1003859856}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] spf-schedule-interval 10 500 ]{lang="EN-US"}[300]{lang="EN-US"}
:::

::: {#472995689 .myid}
[]{#_Toc404789104}[]{#struct_0_14538_x1521_x448866793}[]{#_Toc322361702}

**OSPFv3 \-- OSPFv3配置命令 \-- stub (OSPFv3 area view)**

------------------------------------------------------------------------

[**[stub]{lang="EN-US"}**]{#struct_0_14538_x1521_2008438327}[命令用来配置一个区域为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[undo stub]{lang="EN-US"}**]{#struct_0_14538_x1521_x1132610361}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_307515571}

[**[stub]{lang="EN-US"}**[ \[ **default-route-advertise-always** \| **no-summary** \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_x373454280}

[**[undo stub]{lang="EN-US"}**]{#struct_0_14538_x1521_x1738615565}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_51073125}

[[没有区域被设置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_x1003794320}[区域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1723141320}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x414734243}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1349540568}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_372652850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1505308518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1040703576}

[**[default-route-advertise-always]{lang="EN-US"}**]{#struct_0_14538_x1521_x927419276}[：该参数用于设置总是通告默认路由。]{style="font-family:
宋体"}

[**[no-summary]{lang="EN-US"}**]{#struct_0_14538_x1521_x544531760}[：该参数只用于]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，配置后]{style="font-family:宋体"}[ABR]{lang="EN-US"}[只向区域内发布一条缺省路由的]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[。这种既没有]{style="font-family:宋体"}[AS-external-LSA]{lang="EN-US"}[，也没有其它]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}[、]{style="font-family:宋体"}[Inter-Area-Router-LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域，又称为]{style="font-family:宋体"}[Totally Stub]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1004384143}

[[如果需要在]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_1752388357}[上取消配置]{style="font-family:宋体"}[no-summary]{lang="EN-US"}[参数，可以通过重新执行]{style="font-family:宋体"}[stub]{lang="EN-US"}[命令覆盖之前配置即可。]{style="font-family:宋体"}

[[如果要将一个区域配置成]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_x1376859634}[区域，则该区域中的所有路由器都必须配置此属性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1474472144}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1068868346}[将]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[区域]{style="font-family:宋体"}[1]{lang="EN-US"}[设置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1241456821}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] area 1]{lang="NO-BOK"}

[\[Sysname-ospfv3-1-area-0.0.0.1\] stub]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_816525352}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[default]{lang="EN-US"}**]{#struct_0_14538_x1521_2021116778}**[-]{lang="EN-US"}[cost]{lang="EN-US"}[ ]{lang="EN-US"}**[(OSPFv3 area view)]{lang="EN-US"}
:::

::: {#202080031 .myid}
[]{#_Toc374005799}[]{#_Toc404789105}[]{#struct_0_14538_x1521_424964757}[]{#_Toc376507175}

**OSPFv3 \-- OSPFv3配置命令 \-- stub-router**

------------------------------------------------------------------------

[**[stub-router]{lang="EN-US"}**]{#struct_0_14538_x1521_425030293}[命令用来配置当前路由器为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[**[undo stub-router]{lang="EN-US"}**]{#struct_0_14538_x1521_x305518922}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_425095829}

[**[stub-router]{lang="EN-US"}**[ **r-bit** \[ **include-stub** \| **on-startup** { *seconds* \| **wait-for-bgp** \[ *seconds* \] } \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_425161365}

[**[stub-router]{lang="EN-US"}**[ **max-metric** \[ **external-lsa** \[ *max-metric-value* \] \| **summary-lsa** \[ *max-metric-value* \] \| **include-stub** \| **on-startup** { *seconds* \| **wait-for-bgp** \[ *seconds* \] } \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_424571546}

[**[undo stub-router]{lang="EN-US"}**]{#struct_0_14538_x1521_1233703273}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424637082}

[[当前路由器没有被配置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_424702618}[路由器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1196395719}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_424768154}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424833690}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_424899226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x1414839214}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424964762}

[**[r-bit]{lang="EN-US"}**]{#struct_0_14538_x1521_425030298}[：路由器发布的]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[中，]{style="font-family:宋体"}[options]{lang="EN-US"}[域的]{style="font-family:宋体"}[R-bit]{lang="EN-US"}[将清除。]{style="font-family:宋体"}

[**[max-metric]{lang="EN-US"}**]{#struct_0_14538_x1521_x305518911}[：路由器发布的]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[的链路度量值将设置为最大值]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[external-lsa ]{lang="EN-US"}***[max-metric-value]{lang="EN-US"}*]{#struct_0_14538_x1521_425095834}[：路由器发布的外部]{style="font-family:宋体"}[LSA]{lang="EN-US"}[链路度量值。]{style="font-family:宋体"}*[max-metric-value]{lang="EN-US"}*[表示链路度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[16711680]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[summary-lsa]{lang="EN-US"}***[ max-metric-value]{lang="EN-US"}*]{#struct_0_14538_x1521_425161370}[：路由器发布的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[和]{style="font-family:宋体"}[Type-4 LSA]{lang="EN-US"}[链路度量值。]{style="font-family:宋体"}*[max-metric-value]{lang="EN-US"}*[表示链路度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[16711680]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[include-stub]{lang="EN-US"}**]{#struct_0_14538_x1521_x1483558141}[：路由器发布的引用]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[Type-9 LSA]{lang="EN-US"}[中，链路度量值将设置为最大值]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[on-startup]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_424571547}[：在路由器重启期间，路由器做为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[表示超时时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[wait-for-bgp]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_1233703272}[：在路由器重启后，等待]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由收敛期间，路由器做为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[表示超时时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424637083}

[[将当前路由器配置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_14538_x1521_424702619}[路由器的功能，可通过]{style="font-family:宋体"}[R-bit]{lang="EN-US"}[和]{style="font-family:宋体"}[max-metric]{lang="EN-US"}[两种模式来实现：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R-bit]{lang="EN-US"}]{#struct_0_14538_x1521_424768155}[模式：通过清除该路由器发布]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[options]{lang="EN-US"}[域的]{style="font-family:宋体"}[R-bit]{lang="EN-US"}[，使其他路由器只能计算到该路由器但是不会通过该路由器来转发数据。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[max-metric]{lang="EN-US"}]{#struct_0_14538_x1521_424833691}[模式：该路由器发布的]{style="font-family:
宋体"}[Type-1 LSA]{lang="EN-US"}[的链路度量值将设为最大值]{style="font-family:
宋体"}[65535]{lang="EN-US"}[，这样其邻居计算出这条路由的开销就会很大，如果邻居上有到这个目的地址开销更小的路由，则数据不会通过这个]{style="font-family:
宋体"}[Stub]{lang="EN-US"}[路由器转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_424899227}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x1414839215}[配置当前路由器为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_424964763}

[\[Sysname\] ospfv3 100]{lang="EN-US"}

[\[Sysname-ospfv3-100\] stub-router r-bit]{lang="EN-US"}
:::

::: {#2015842796 .myid}
[]{#_Toc322361703}[]{#_Toc404789106}[]{#struct_0_14538_x1521_x1004318607}[]{#_Toc345409326}[]{#_Toc341864224}

**OSPFv3 \-- OSPFv3配置命令 \-- transmit-pacing**

------------------------------------------------------------------------

[**[transmit-pacing]{lang="EN-US"}**]{#struct_0_14538_x1521_x1657698739}[用来配置接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔和一次发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的最大个数。]{style="font-family:宋体"}

[**[undo transmit-pacing]{lang="EN-US"}**]{#struct_0_14538_x1521_x999072110}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x2012791798}

[**[transmit-pacing]{lang="EN-US"}**[ **interval** *interval* **count** *count*]{lang="EN-US"}]{#struct_0_14538_x1521_1138714533}

[**[undo]{lang="EN-US"}**[ **transmit-pacing**]{lang="EN-US"}]{#struct_0_14538_x1521_909918801}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_826528191}

[[接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_14538_x1521_x1375149517}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1725649752}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_x1004253071}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_335110613}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_x909877039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1521569720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x161919823}

[**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_14538_x1521_18805098}[：接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔，]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为毫秒。当路由器上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能的接口数比较多时，建议增大该值，以控制路由器每秒钟发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的总数。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_14538_x1521_x1830144139}[：接口一次发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的最大个数，]{style="font-family:宋体"}*[count]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。当路由器上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能的接口数比较多时，建议减小该值，以控制路由器每秒钟发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的总数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_2023872799}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_x583921770}[配置]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的所有接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_x1004187535}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] transmit-pacing interval 30 count 10]{lang="EN-US"}
:::

::: {#-591574322 .myid}
[]{#_Toc404789107}[]{#struct_0_14538_x1521_x1606641817}

**OSPFv3 \-- OSPFv3配置命令 \-- vlink-peer (OSPFv3 area view)**

------------------------------------------------------------------------

[**[vlink-peer]{lang="EN-US"}**]{#struct_0_14538_x1521_x891503954}[命令用来创建并配置一条虚连接。]{style="font-family:宋体"}

[**[undo vlink-peer]{lang="EN-US"}**]{#struct_0_14538_x1521_1127729210}[命令用来删除一条已有的虚连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1038070541}

[**[vlink-peer ]{lang="EN-US"}***[router-id]{lang="EN-US"}*[ \[ **dead** *seconds* \| **hello** *seconds* \| **instance** *instance-id* \| **ipsec-profile** *profile-name* \| **retransmit** *seconds* \| **trans-delay** *seconds* \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_828789342}

[**[undo vlink-peer ]{lang="EN-US"}***[router-id]{lang="EN-US"}*[ \[ **dead** \| **hello** \| **ipsec-profile** \| **retransmit** \| **trans-delay** \] \*]{lang="EN-US"}]{#struct_0_14538_x1521_x58450586}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14538_x1521_1276087255}

[[没有虚连接。]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1004646287}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14538_x1521_612369800}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14538_x1521_347847181}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x168707987}

[[network-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1294750124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14538_x1521_1738299470}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1886763620}

[*[router-id]{lang="EN-US"}*]{#struct_0_14538_x1521_1126772085}[：虚连接邻居的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dead ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_917576877}[：失效时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32768]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。该值必须和与其建立虚连接路由器的]{style="font-family:宋体"}**[dead]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值相等，并至少为]{style="font-family:宋体"}**[hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值的]{style="font-family:宋体"}[4]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[**[hello ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_x1004580751}[：接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8192]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。该值必须和与其建立虚连接路由器上的]{style="font-family:宋体"}[hello seconds]{lang="EN-US"}[值相等。]{style="font-family:宋体"}

[**[instance]{lang="EN-US"}***[ instance-id]{lang="EN-US"}*]{#struct_0_14538_x1521_40462805}[：设置虚连接的实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipsec-profile]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_14538_x1521_x1901382792}[：应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[retransmit ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_x1698497472}[：接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[trans-delay]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_14538_x1521_1936827214}[：接口延迟发送]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x1940081087}

[[对于没有和骨干区域直接相连的非骨干区域，或者不连续的骨干区域来说，可以使用]{style="font-family:宋体"}**[vlink-pee]{lang="EN-US"}**[r]{lang="EN-US"}]{#struct_0_14538_x1521_x1201168877}[命令建立逻辑上的连通性。在某种程度上，可以将虚连接看作一个普通的使能了]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[的接口，因为在其上配置的]{style="font-family:宋体"}**[hello]{lang="EN-US"}**[、]{style="font-family:宋体"}**[dead]{lang="EN-US"}**[、]{style="font-family:宋体"}**[retransmit]{lang="EN-US"}**[和]{style="font-family:宋体"}**[trans-delay]{lang="EN-US"}**[等参数的原理是类似的。]{style="font-family:宋体"}

[[各参数取值规则如下：]{style="font-family:宋体"}]{#struct_0_14538_x1521_642924279}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[hello]{lang="EN-US"}**]{#struct_0_14538_x1521_x480510120}[值越小，发现网络变化的速度越快，消耗的网络资源也就越多**。**]{style="font-family:
宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[不能将]{style="font-family:宋体"}]{#struct_0_14538_x1521_x1004515215}**[retransmit]{lang="EN-US"}**[值设置的太小，否则将会引起不必要的重传。网络速度相对较慢的时候应把该值设的更大一些。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[设置]{lang="EN-US" style="font-family:宋体"}**[trans-delay]{lang="EN-US"}**]{#struct_0_14538_x1521_x1177391233}[值时必须考虑接口的发送延迟。]{lang="EN-US" style="font-family:宋体"}

[[虚连接的两端必须是]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_14538_x1521_x1758657040}[，]{style="font-family:宋体"}**[vlink-peer]{lang="EN-US"}**[命令必须在两端同时配置才可生效。]{style="font-family:宋体"}

[[IPsec]{lang="EN-US"}]{#struct_0_14538_x1521_1172566976}[安全框架的具体情况请参见"安全配置指导"中的"]{style="font-family:宋体"}[IPsec]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x31657983}

[[\# ]{lang="EN-US"}]{#struct_0_14538_x1521_1601307322}[创建一条到]{style="font-family:宋体"}[10.10.0.3]{lang="EN-US"}[的虚连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14538_x1521_1745846747}

[\[Sysname\] ospfv3 1]{lang="EN-US"}

[\[Sysname-ospfv3-1\] area 1]{lang="NO-BOK"}

[\[Sysname-ospfv3-1-area-0.0.0.1\] vlink-peer 10.10.0.3]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14538_x1521_x821786833}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[display ospfv3 vlink]{lang="EN-US"}**]{#struct_0_14538_x1521_x1004449679}

[ ]{lang="EN-US"}
:::
